import { bonaireBookingCore } from "./bonaire";
import type { AgeBand, BookableProductConfig, ProductCapacity, ProductPricing } from "../world-booking/types";

/**
 * Operational routing: Wow A Tour ops mailbox for Graham’s manual fulfilment.
 * Public customers never see SEG. Graham places corresponding bookings via his
 * established SEG affiliate / white-label account using INTERNAL supply refs only.
 */
const OPERATIONS = {
  id: "wow-a-tour-operations",
  displayName: "Wow A Tour",
  notificationEmail: "info@wowatour.com",
  routingStatus: "production_ready" as const,
};

const REQUEST_SETTLEMENT = "charge_refund" as const;

/** Graham online max — never describe as supplier / vehicle capacity. */
const BON_CAPACITY: ProductCapacity = {
  minGuests: 1,
  maxGuestsPerBooking: 10,
  maxGuestsPerBookingSource: "approved",
  supplierGroupSize: null,
  maxGuestsPerGuide: null,
};

/**
 * Phase 20D Graham-approved bands:
 * - Ages 0–5 free (recorded) — explicit on source
 * - Ages 6–11 paid child — explicit on source ($109)
 * - Ages 12+ adult residual band for WOW UX — source prints “Adults” + child 6–11;
 *   SEG does NOT explicitly print “adult age 12+” as a lower-bound label.
 *
 * Engine still requires ≥1 adult (ADULT_REQUIRED). Adult = paying ages 12+ in WOW UX.
 * Do not invent a separate adult-accompaniment rule beyond this engine constraint.
 */
const ISLAND_AGE_BANDS: readonly AgeBand[] = [
  { id: "adult", label: "Adults age 12+", minAge: 12, maxAge: null, pricingStatus: "priced" },
  { id: "child", label: "Children age 6–11", minAge: 6, maxAge: 11, pricingStatus: "priced" },
  { id: "infant", label: "Children age 0–5 (free)", minAge: 0, maxAge: 5, pricingStatus: "priced" },
];

function adultChildInfantUsd(adultAmount: number, childAmount: number): ProductPricing {
  return {
    model: "adult_child",
    currency: "USD",
    adultAmount,
    childAmount,
    childPricingStatus: "priced",
    infantAmount: 0,
    infantPricingStatus: "priced",
    pricingNeedsConfirmation: false,
  };
}

const SHARED_PENDING = [
  "Customer cancellation APPROVED: free outside 14 days before excursion; from the 14th day non-refundable.",
  "Unable to confirm after payment: full refund to original payment method.",
  "Meeting: Cruise ship pier; exact instructions after confirmation / on e-ticket.",
  "Fulfilment: Graham places corresponding booking via established SEG affiliate / white-label route (INTERNAL).",
  "Payment received ≠ excursion confirmed.",
  "Online max 10 guests per booking including free 0–5 (Graham online limit — not supplier capacity).",
  "At least one adult (ages 12+) required by booking engine (ADULT_REQUIRED).",
  "Do not overclaim: Washington park entry, full circumference, lighthouse visit, guaranteed flamingos, all 28 POIs as stops, beach stop guaranteed, exact stop order.",
  "Activity: Moderate. Wheelchair accessible ONLY if guest can get into the vehicle without assistance.",
  "commercial_status=SEG_FULFILMENT_READY · fulfilment_mode=SEG_MANUAL · supplier=UNKNOWN · direct_supplier_status=NOT_CONTACTED · net_cost=UNKNOWN · margin=UNKNOWN",
] as const;

export const BONAIRE_CANCELLATION_COPY = {
  customerCancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable. If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  freeWindow: "Free cancellation outside 14 days before your excursion.",
  insideWindow: "From the 14th day before your excursion, bookings are non-refundable.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  meetingInstructions:
    "Meeting point is the cruise ship pier. Exact meeting instructions will be provided after confirmation / on your e-ticket.",
  overTenGuidance: "For groups larger than 10, email hello@bonairecruiseexcursions.com before requesting.",
} as const;

const ISLAND_SIGHTSEEING: BookableProductConfig = {
  id: "bonaire-island-sightseeing-tour",
  destinationId: bonaireBookingCore.id,
  slug: "bonaire-island-sightseeing-tour",
  name: "Bonaire Island Sightseeing Tour",
  durationLabel: "3 hours",
  bookingMode: "request",
  availability: "live",
  bookingPath: "/book/bonaire-island-sightseeing-tour",
  receivedPath: "/book/bonaire-island-sightseeing-tour/received",
  confirmedPath: "/book/bonaire-island-sightseeing-tour/received",
  productPath: "/bonaire-island-tour",
  pricing: adultChildInfantUsd(129, 109),
  ageBands: ISLAND_AGE_BANDS,
  capacity: BON_CAPACITY,
  requiredCustomerFields: ["name", "email", "phone"],
  supplier: OPERATIONS,
  paymentSettlement: REQUEST_SETTLEMENT,
  schedulePortSlug: "bonaire",
  pendingCommercialRules: [
    ...SHARED_PENDING,
    "Adult USD 129 (WOW ages 12+) · Child USD 109 (6–11) · Ages 0–5 FREE (must record) · require ≥1 adult",
    "Land sightseeing · ~28 points of interest with ~6 short stops · south + north contrast",
    "Themes (source-supported): salt landscape, White Slave Huts, 1000 Steps viewpoint, Goto Lake / flamingo area, Kralendijk, Harbour Village Marina, Trans World Radio, Te Amo / Donkey Beach mentions",
    "Public name omits 'Full Island' overclaim — editorial equity page remains /bonaire-island-tour",
    "Age note: 0–5 and 6–11 explicit on source; 12+ is WOW residual band from source partition (Adults + child 6–11), not SEG-printed lower-bound text",
  ],
  supplierReferenceNotes: [
    "INTERNAL SUPPLY: SEG_MANUAL · cabosightseeing",
    "INTERNAL CODE: cabosightseeing",
    "Fulfilment mode: SEG_MANUAL",
    "Supplier contact: UNKNOWN · NOT_CONTACTED · net/margin UNKNOWN",
    "Fulfilment: place via established SEG affiliate / white-label route (manual — do not automate).",
    "Selling: Adult USD 129 (WOW 12+) · Child USD 109 (6–11) · Ages 0–5 FREE (recorded).",
    "Customer cancellation: Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
    "Unable to confirm after payment: full refund to original payment method.",
  ],
};

export const BONAIRE_BOOKABLE_PRODUCTS: readonly BookableProductConfig[] = [ISLAND_SIGHTSEEING];

export function findBonaireBookingProduct(productId: string): BookableProductConfig | null {
  return BONAIRE_BOOKABLE_PRODUCTS.find((p) => p.id === productId) ?? null;
}

export function listBonaireBookingProducts(): readonly BookableProductConfig[] {
  return BONAIRE_BOOKABLE_PRODUCTS;
}
