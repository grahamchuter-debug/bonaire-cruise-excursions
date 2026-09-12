/**
 * Shared booking engine tests — Bonaire Phase 20D (Island Sightseeing only).
 */
import assert from "node:assert/strict";
import { test } from "node:test";
import {
  BONAIRE_BOOKABLE_PRODUCTS,
  BONAIRE_CANCELLATION_COPY,
  findBonaireBookingProduct,
} from "../destinations/bonaire-products";
import { bonaireBookingCore } from "../destinations/bonaire";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  createBookingReference,
  destinationBrandFromCore,
  requestedCustomerEmail,
  statusAfterPaymentSuccess,
  supplierRequestEmail,
  validateCruise,
  validateCustomer,
} from "./index";

const brand = destinationBrandFromCore(bonaireBookingCore);
const island = findBonaireBookingProduct("bonaire-island-sightseeing-tour");
assert.ok(island);

test("single Bonaire product ID present", () => {
  assert.equal(BONAIRE_BOOKABLE_PRODUCTS.length, 1);
  assert.equal(BONAIRE_BOOKABLE_PRODUCTS[0]!.id, "bonaire-island-sightseeing-tour");
});

test("island tour adult 129 child 109 free 0-5; requires adult", () => {
  assert.equal(island!.pricing.adultAmount, 129);
  assert.equal(island!.pricing.childAmount, 109);
  assert.equal(island!.pricing.childPricingStatus, "priced");
  assert.equal(island!.pricing.infantAmount, 0);
  assert.equal(island!.pricing.infantPricingStatus, "priced");
  assert.equal(calculateBookingQuote(island!, { adults: 1, children: 0, infants: 0 }).amountCents, 12900);
  assert.equal(calculateBookingQuote(island!, { adults: 2, children: 0, infants: 0 }).amountCents, 25800);
  assert.equal(calculateBookingQuote(island!, { adults: 1, children: 1, infants: 0 }).amountCents, 23800);
  assert.equal(calculateBookingQuote(island!, { adults: 2, children: 2, infants: 0 }).amountCents, 47600);
  assert.equal(calculateBookingQuote(island!, { adults: 1, children: 0, infants: 1 }).amountCents, 12900);
  assert.equal(calculateBookingQuote(island!, { adults: 1, children: 1, infants: 1 }).amountCents, 23800);
  assert.equal(calculateBookingQuote(island!, { adults: 1, children: 0, infants: 1 }).partySize, 2);
  assert.throws(() => calculateBookingQuote(island!, { adults: 0, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(island!, { adults: 0, children: 1, infants: 0 }));
  assert.throws(() => calculateBookingQuote(island!, { adults: 0, children: 0, infants: 0 }));
});

test("max 10 guests; 11 rejected; free children count toward max", () => {
  assert.equal(island!.capacity.maxGuestsPerBooking, 10);
  assert.doesNotThrow(() => calculateBookingQuote(island!, { adults: 10, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(island!, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(island!, { adults: 0, children: 0, infants: 0 }));
  assert.doesNotThrow(() => calculateBookingQuote(island!, { adults: 8, children: 1, infants: 1 }));
  assert.throws(() => calculateBookingQuote(island!, { adults: 8, children: 1, infants: 2 }));
});

test("client total must match server quote", () => {
  const quote = calculateBookingQuote(island!, { adults: 1, children: 1, infants: 1 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 23800));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("booking references use Bonaire W2BON prefix", () => {
  assert.match(createBookingReference(bonaireBookingCore), /^W2BON-/);
  assert.equal(bonaireBookingCore.bookingRefPrefix, "W2BON");
});

test("customer and cruise validation", () => {
  assert.equal(
    validateCustomer({ name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" }),
    null,
  );
  assert.ok(validateCustomer({ name: "A", email: "x", phone: "1" }));
  assert.ok(
    validateCruise({
      date: "2020-01-01",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
  );
  assert.equal(
    validateCruise({
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
    null,
  );
});

test("cancellation copy covers 14-day policy and full refund", () => {
  assert.match(BONAIRE_CANCELLATION_COPY.customerCancellation, /outside 14 days/i);
  assert.match(BONAIRE_CANCELLATION_COPY.customerCancellation, /14th day/i);
  assert.match(BONAIRE_CANCELLATION_COPY.unableToConfirm, /full refund/i);
  assert.match(BONAIRE_CANCELLATION_COPY.paymentNotConfirmation, /confirm.*separately|separately.*confirm/i);
});

test("customer email never exposes SEG or internal codes", () => {
  const mail = requestedCustomerEmail({
    brand,
    product: island!,
    reference: "W2BON-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 1, infants: 1 },
    amountLabel: "USD $238.00",
    customerName: "Alex Traveller",
  });
  const blob = JSON.stringify(mail);
  assert.doesNotMatch(blob, /\bSEG\b|cabosightseeing|Shore Excursions Group|info@wowatour/i);
  assert.match(blob, /request|confirm/i);
});

test("ops email includes internal supply notes for Graham", () => {
  const mail = supplierRequestEmail({
    product: island!,
    reference: "W2BON-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 1, infants: 1 },
    amountLabel: "USD $238.00",
    customer: {
      name: "Alex Traveller",
      email: "alex@example.com",
      phone: "+447700900123",
    },
    destinationLabel: "Bonaire Cruise Excursions — new booking request",
  });
  const blob = JSON.stringify(mail);
  assert.match(blob, /cabosightseeing|SEG_MANUAL/i);
  assert.match(blob, /\+447700900123|phone/i);
});

test("reject foreign destination product lookup", () => {
  assert.equal(findBonaireBookingProduct("garden-of-the-groves-city-tour"), null);
  assert.equal(findBonaireBookingProduct("explore-nassau-walking-tour"), null);
  assert.equal(findBonaireBookingProduct("historic-walking-tour"), null);
});
