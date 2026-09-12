/**
 * Bonaire destination booking core.
 * Product catalogue: shared/destinations/bonaire-products.ts
 * Public editorial: equity pages via scripts/build-bonaire-site.py
 * Internal supply mapping: product.supplierReferenceNotes (never public HTML)
 */
import type { DestinationBookingCore } from "../world-booking/types";

export const bonaireBookingCore = {
  id: "bonaire",
  siteName: "Bonaire Cruise Excursions",
  siteHostname: "bonairecruiseexcursions.com",
  siteUrl: "https://bonairecruiseexcursions.com",
  bookingEmail: "hello@bonairecruiseexcursions.com",
  originatingSite: "bonairecruiseexcursions.com",
  originatingPort: "Kralendijk, Bonaire",
  bookingRefPrefix: "W2BON",
  sessionKeyPrefix: "w2-bon-booking",
  sessionKeyVersion: 1,
  currencyCode: "USD",
  bookableWindow: {
    start: "2026-09-01",
    end: "2028-12-31",
  },
  /** No Bonaire schedule import — cruise date/ship are customer-entered. */
  schedulePortSlug: "bonaire",
  customShipSlug: "not-listed",
  contactPath: "/contact",
  termsPath: "/terms",
  privacyPath: "/privacy",
} as const satisfies DestinationBookingCore;
