/**
 * Public commercial status for Bonaire Cruise Excursions (Phase 20D).
 * INTERNAL supply refs must never be rendered on customer pages.
 *
 * Gate values:
 * - PRODUCTION_READY_LOCKED — journey visible; live Pay & request disabled
 * - BOOKING_ENABLED — checkout allowed against the configured Worker
 */
window.BON_COMMERCIAL = {
  bookingsApiUrl: "https://bonaire-bookings-prod.dark-violet-8d91.workers.dev",
  email: "hello@bonairecruiseexcursions.com",
  siteName: "Bonaire Cruise Excursions",
  defaultPublicBookingStatus: "BOOKING_ENABLED",
  cancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  meetingInstructions:
    "Meeting point is the cruise ship pier. Exact meeting instructions will be provided after confirmation / on your e-ticket.",
  overTenGuidance:
    "For groups larger than 10, email hello@bonairecruiseexcursions.com before requesting.",
  products: {
    "bonaire-island-sightseeing-tour": {
      productId: "bonaire-island-sightseeing-tour",
      slug: "bonaire-island-sightseeing-tour",
      name: "Bonaire Island Sightseeing Tour",
      shortTitle: "Bonaire Island Sightseeing Tour",
      productPath: "/bonaire-island-tour",
      bookingPath: "/book/bonaire-island-sightseeing-tour",
      receivedPath: "/book/bonaire-island-sightseeing-tour/received",
      adultUsd: 129,
      childUsd: 109,
      infantUsd: 0,
      guestModel: "adult_child_infant",
      durationLabel: "3 hours",
      maxGuests: 10,
      publicBookingStatus: "BOOKING_ENABLED",
      displayPrice: "Adults age 12+ $129 · Children age 6–11 $109 · Children age 0–5 free",
    },
  },
};
