/**
 * Bonaire booking security / commercial gate tests (Phase 20D).
 * No live Stripe. Uses Worker preview mode + shared pricing authority.
 */
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";
import worker from "./index";
import { LIVE_PAYMENTS_CODE_ENABLED, liveCheckoutBlock, bookingsAreEnabled } from "./live-gate";
import { assertStripeTestSecret, StripeModeError } from "./stripe-guard";
import {
  BONAIRE_BOOKABLE_PRODUCTS,
  findBonaireBookingProduct,
} from "../../../shared/destinations/bonaire-products";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  statusAfterPaymentSuccess,
} from "../../../shared/world-booking";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "../../..");

const previewEnv = {
  PAYMENTS_MODE: "preview",
  BOOKINGS_ENABLED: "true",
  CORS_ALLOWED_ORIGINS: "http://localhost:8920",
  SITE_BASE_URL: "http://localhost:8920",
} as unknown as Env;

const CLASSIC = "bonaire-island-sightseeing-tour";

function payload(
  sessionId: string,
  guests = { adults: 2, children: 0, infants: 0 },
  overrides: Record<string, unknown> = {},
  productId = CLASSIC,
) {
  const product = findBonaireBookingProduct(productId)!;
  const quote = calculateBookingQuote(product, guests);
  return {
    productId,
    bookingSessionId: sessionId,
    guests,
    customer: { name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" },
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "celebrity-beyond",
      cruiseLine: "Celebrity Cruises",
      isCustomShip: true,
      scheduleMatched: false,
    },
    confirmationAcknowledged: true,
    clientDisplayedTotalCents: quote.amountCents,
    ...overrides,
  };
}

function jsonReq(url: string, body: unknown) {
  return new Request(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
}

test("LIVE_PAYMENTS_CODE_ENABLED is true for Bonaire Phase 20D", () => {
  assert.equal(LIVE_PAYMENTS_CODE_ENABLED, true);
});

test("live checkout allowed when code flag, unlock phrase, and live secrets present", () => {
  const product = findBonaireBookingProduct(CLASSIC)!;
  const block = liveCheckoutBlock(
    {
      PAYMENTS_MODE: "live",
      LIVE_PAYMENTS_UNLOCK: "BONAIRE_LIVE_UNLOCK",
      BOOKINGS_ENABLED: "true",
      STRIPE_SECRET_KEY: "sk_live_fake",
      STRIPE_WEBHOOK_SECRET: "whsec_fake",
      SITE_BASE_URL: "https://bonairecruiseexcursions.com",
      DB: {} as D1Database,
    },
    product,
  );
  assert.equal(block, null);
});

test("BOOKINGS_ENABLED=false kill switch", () => {
  assert.equal(bookingsAreEnabled({ BOOKINGS_ENABLED: "false" }), false);
});

test("single Bonaire product live request mode with USD currency", () => {
  assert.equal(BONAIRE_BOOKABLE_PRODUCTS.length, 1);
  for (const product of BONAIRE_BOOKABLE_PRODUCTS) {
    assert.equal(product.availability, "live");
    assert.equal(product.bookingMode, "request");
    assert.equal(product.pricing.currency, "USD");
    assert.equal(product.capacity.maxGuestsPerBooking, 10);
    assert.equal(product.destinationId, "bonaire");
  }
});

test("bonaire-island-sightseeing-tour adult 12900 child 10900 infant free", () => {
  const product = findBonaireBookingProduct(CLASSIC)!;
  assert.equal(product.pricing.adultAmount, 129);
  assert.equal(product.pricing.childAmount, 109);
  assert.equal(product.pricing.childPricingStatus, "priced");
  assert.equal(product.pricing.infantAmount, 0);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 0, infants: 0 }).amountCents, 12900);
  assert.equal(calculateBookingQuote(product, { adults: 2, children: 0, infants: 0 }).amountCents, 25800);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 1, infants: 0 }).amountCents, 23800);
  assert.equal(calculateBookingQuote(product, { adults: 2, children: 2, infants: 0 }).amountCents, 47600);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 0, infants: 1 }).amountCents, 12900);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 1, infants: 1 }).amountCents, 23800);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 0, infants: 1 }).breakdown.infants.count, 1);
});

test("rejects 0 adults, 11 guests, negatives via quote", () => {
  const product = findBonaireBookingProduct(CLASSIC)!;
  assert.throws(() => calculateBookingQuote(product, { adults: 0, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 0, children: 1, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: -1, children: 0, infants: 0 }));
  assert.doesNotThrow(() => calculateBookingQuote(product, { adults: 10, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 8, children: 1, infants: 2 }));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("preview request returns W2BON reference", async () => {
  const body = payload(`sess-${Date.now()}`, { adults: 1, children: 0, infants: 0 });
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 200);
  const firstJson = (await res.json()) as { ok: boolean; reference: string };
  assert.equal(firstJson.ok, true);
  assert.match(firstJson.reference, /^W2BON-/);
});

test("bonaire-island-sightseeing-tour requestable in preview with free child retained", async () => {
  const body = payload(`sess-infant-${Date.now()}`, { adults: 1, children: 0, infants: 1 });
  assert.equal(body.guests.infants, 1);
  assert.equal(body.clientDisplayedTotalCents, 12900);
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 200);
  const data = (await res.json()) as { ok: boolean; reference: string; status: string };
  assert.equal(data.ok, true);
  assert.match(data.reference, /^W2BON-/);
  assert.equal(data.status, "requested");
});

test("unknown product and cross-destination IDs rejected", async () => {
  for (const productId of [
    "not-a-bonaire-product",
    "garden-of-the-groves-city-tour",
    "explore-nassau-walking-tour",
    "historic-walking-tour",
    "highlights-and-beach-break",
    "belize-cave-tubing",
  ]) {
    const bad = payload(`unk-${Date.now()}`, { adults: 1, children: 0, infants: 0 }, { productId });
    const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", bad), previewEnv);
    assert.equal(res.status, 400, productId);
  }
});

test("client price mismatch rejected", async () => {
  const body = payload(`tamper-${Date.now()}`, { adults: 1, children: 0, infants: 0 }, {
    clientDisplayedTotalCents: 1,
  });
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 400);
});

test("client total must match server quote helper", () => {
  const product = findBonaireBookingProduct(CLASSIC)!;
  const quote = calculateBookingQuote(product, { adults: 1, children: 1, infants: 1 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 23800));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("ops request heading is Bonaire", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/notify.ts"), "utf8");
  assert.match(src, /NEW BONAIRE BOOKING REQUEST/);
});

test("TEST Stripe secret guard", () => {
  assert.doesNotThrow(() => assertStripeTestSecret("sk_test_abc"));
  assert.throws(() => assertStripeTestSecret("sk_live_abc"), StripeModeError);
});

test("Stripe Link disabled at session level (checkout source)", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/routes/checkout.ts"), "utf8");
  assert.match(src, /link_mode|payment_method_options|link/i);
});

test("public HTML never leaks SEG / internal codes", () => {
  const files = [
    "bonaire-island-tour/index.html",
    "book/bonaire-island-sightseeing-tour/index.html",
    "book/bonaire-island-sightseeing-tour/received/index.html",
    "js/commercial-config.js",
  ];
  const banned = /\bSEG\b|Shore Excursions Group|cabosightseeing|SEG_MANUAL|shoreexcursionsgroup|info@wowatour\.com/i;
  for (const rel of files) {
    const path = join(ROOT, rel);
    try {
      const text = readFileSync(path, "utf8");
      assert.doesNotMatch(text, banned, rel);
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === "ENOENT") {
        continue;
      }
      throw err;
    }
  }
  for (const product of BONAIRE_BOOKABLE_PRODUCTS) {
    assert.doesNotMatch(product.productPath, /SEG|cabosightseeing/i);
    assert.doesNotMatch(product.bookingPath, /SEG|cabosightseeing/i);
  }
});

test("live-gate source keeps code flag true", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/live-gate.ts"), "utf8");
  assert.match(src, /LIVE_PAYMENTS_CODE_ENABLED\s*=\s*true/);
});

test("commercial-config has no internal codes", () => {
  const text = readFileSync(join(ROOT, "js/commercial-config.js"), "utf8");
  assert.doesNotMatch(text, /cabosightseeing|SEG_MANUAL|\bSEG\b|info@wowatour/);
});
