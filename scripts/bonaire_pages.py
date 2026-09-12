"""Bonaire World 2.0 page bodies and page assembly (Phase 20B)."""
from __future__ import annotations

from bonaire_config import (
    CRUISE_PORT,
    CRUISE_PORT_ALT,
    EMAIL,
    FLAMINGO,
    FLAMINGO_ALT,
    SNORKEL,
    SNORKEL_ALT,
)
from bonaire_shell import (
    cruise_snapshot,
    editorial_cta,
    faq_section,
    hero_band,
    page_shell,
    related_links,
)

# --- FAQ data (q, a) for schema + UI ---

FAQ_HOME: list[tuple[str, str]] = [
    (
        "Where do cruise ships dock in Bonaire?",
        "Most ships use the Kralendijk cruise piers on the town waterfront — commonly described as North Pier and South Pier. Both put you close to shops, taxis, and many excursion meeting points. Confirm your berth on the ship’s daily programme.",
    ),
    (
        "What should first-time cruise visitors do in Bonaire?",
        "Pick one primary plan that fits your usable hours: a south-island sightseeing loop (salt pans, flamingo viewing from public roads, slave huts), a Klein Bonaire boat/snorkel outing, or an easy town-and-beach day. Avoid stacking a full north park visit with Klein and a long south loop on a short call.",
    ),
    (
        "Do I need a Nature Fee for Bonaire?",
        "Water activities in Bonaire National Marine Park and visits to Washington Slagbaai National Park are managed by STINAPA and require a Nature Fee. Rules and day rates for cruise visitors can change — verify current requirements with official STINAPA sources or your operator before you enter the water or the park.",
    ),
    (
        "Can I see flamingos on a cruise day?",
        "Many south-island tours pass salt-pan landscapes near the Pekelmeer sanctuary area. The sanctuary itself is protected and closed to visitors; viewing is typically from public roadside vantage points, and bird distance varies. Treat sightings as possible, never guaranteed.",
    ),
]

FAQ_ISLAND: list[tuple[str, str]] = [
    (
        "What does a Bonaire island tour usually cover?",
        "Cruise-friendly sightseeing tours often emphasise southern highlights — salt pans, roadside flamingo viewing opportunities, historic slave huts, and coastal landmarks such as the Willemstoren lighthouse — sometimes with Kralendijk context and selected north viewpoints. Exact stops vary by operator.",
    ),
    (
        "Can I enter the Pekelmeer Flamingo Sanctuary?",
        "No. Pekelmeer is a protected sanctuary. Visitors are not admitted into the closed area. Observation is generally from public roads and designated roadside viewpoints. Keep distance, stay on public ground, and do not expect close approaches.",
    ),
    (
        "Is Washington Slagbaai realistic on a short cruise call?",
        "A full Washington Slagbaai National Park visit can consume a large share of a port day (driving, entry timing, and Nature Fee rules). Many cruise sightseeing tours treat the north as viewpoints or distant context rather than a full park circuit. Confirm with your operator.",
    ),
    (
        "How long should I allow for an island sightseeing tour?",
        "Many land sightseeing products run roughly two to four hours, but usable time depends on your ship’s all-aboard call, pier location, and traffic on busy days. Keep a personal return buffer and do not rely on marketing promises.",
    ),
]

FAQ_KLEIN: list[tuple[str, str]] = [
    (
        "What is Klein Bonaire?",
        "Klein Bonaire is an uninhabited islet just off Kralendijk, inside Bonaire National Marine Park. Cruise visitors typically reach it by boat or water taxi for beach time and snorkelling near places such as No Name Beach.",
    ),
    (
        "How do I get to Klein Bonaire from the cruise pier?",
        "You need a boat transfer. Some operators meet near the pier; others require a short walk to a marina or water-taxi departure point. Confirm meeting instructions on your confirmation and allow extra time for queues on busy ship days.",
    ),
    (
        "Is Klein Bonaire suitable if I have limited mobility?",
        "Often not. Boat boarding, beach landings, and reef entries can be difficult. Some water products cannot accommodate wheelchairs or significant mobility limits. Ask the operator about boarding method and sea conditions before you book.",
    ),
    (
        "Do marine park rules apply at Klein Bonaire?",
        "Yes. Klein Bonaire sits within the marine park framework managed with STINAPA. Expect Nature Fee requirements for water activities and follow local conservation rules. Verify current fee and entry rules before you go.",
    ),
]

FAQ_PORT: list[tuple[str, str]] = [
    (
        "What is the difference between North Pier and South Pier?",
        "Both are cruise berths along Kralendijk’s central waterfront. Your ship may use either depending on the day’s berthing plan. Walking into town is generally convenient from both; exact walking times and pickup points still vary.",
    ),
    (
        "Is Kralendijk walkable from the ship?",
        "Yes for many guests — shops, cafés, and waterfront strolling are close to the piers. That does not mean Klein Bonaire or the south salt pans are walkable; those need a boat or road transfer.",
    ),
    (
        "How should I plan my return to the ship?",
        "Note all-aboard time from the ship’s programme, then build your own buffer for tenders (if any), taxi queues, boat returns, and traffic. Independent operators may aim to return early, but weather and congestion can still delay you — plan conservatively.",
    ),
    (
        "What currency is used in Bonaire?",
        "The US dollar is the everyday currency. Cards are widely accepted in Kralendijk; keep some cash for small purchases and tips if needed.",
    ),
]


def home_body() -> str:
    return f"""
<section class="pt-10 pb-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
      <div>
        <p class="text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3">Kralendijk · Dutch Caribbean</p>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 leading-snug mb-5">Plan a realistic Bonaire cruise day</h2>
        <p class="text-gray-600 leading-relaxed mb-4">Bonaire rewards cruise passengers who choose one clear plan. The island is compact, but south salt-pan loops, Klein boat transfers, and north viewpoints are not interchangeable add-ons on a short call.</p>
        <p class="text-gray-600 leading-relaxed mb-4">This site is an independent planning guide for shore excursions and port logistics from Kralendijk — not a cruise line and not a booking marketplace.</p>
        <p class="text-gray-600 leading-relaxed mb-8">Start with the decision spine below, then deepen on the island-tour, Klein, and port-guide pages.</p>
        <a href="/best-bonaire-shore-excursions" class="btn-ocean inline-flex items-center text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-md">Compare excursion types</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-xl overflow-hidden">
        <img src="{CRUISE_PORT}" alt="{CRUISE_PORT_ALT}" width="800" height="600" loading="eager" decoding="async" />
      </div>
    </div>
  </div>
</section>

<section class="py-16 bg-sand-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-12">
      <h2 class="text-3xl font-display font-bold text-gray-900">Decision spine for your port day</h2>
      <p class="mt-3 text-gray-500 max-w-2xl mx-auto">Five practical branches — not a fake catalogue.</p>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <a href="/bonaire-island-tour" class="card-hover bg-white rounded-2xl border border-ocean-50 p-6 shadow-sm block">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Island tour</h3>
        <p class="text-sm text-gray-500 leading-relaxed">South salt pans, flamingo viewing context, slave huts, lighthouse, and Kralendijk orientation.</p>
      </a>
      <a href="/klein-bonaire-snorkeling" class="card-hover bg-white rounded-2xl border border-ocean-50 p-6 shadow-sm block">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Klein Bonaire</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Uninhabited islet by boat — beach and snorkel context inside the marine park.</p>
      </a>
      <a href="/best-bonaire-shore-excursions" class="card-hover bg-white rounded-2xl border border-ocean-50 p-6 shadow-sm block">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Snorkelling / sail</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Water days depend on sea state, boarding method, and Nature Fee rules — compare carefully.</p>
      </a>
      <a href="/bonaire-island-tour#flamingos-salt" class="card-hover bg-white rounded-2xl border border-ocean-50 p-6 shadow-sm block">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Flamingos &amp; salt flats</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Protected sanctuary context and roadside viewing — covered inside the island-tour guide.</p>
      </a>
      <a href="/bonaire-cruise-port-guide" class="card-hover bg-white rounded-2xl border border-ocean-50 p-6 shadow-sm block sm:col-span-2 lg:col-span-1">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Easy / town day</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Walk Kralendijk, keep transfers short, and protect your return window.</p>
      </a>
    </div>
  </div>
</section>

<section class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div class="info-image rounded-3xl aspect-[4/3] overflow-hidden shadow-lg order-2 lg:order-1">
        <img src="{FLAMINGO}" alt="{FLAMINGO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
      <div class="order-1 lg:order-2">
        <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">South island character, without wildlife promises</h2>
        <p class="text-gray-600 leading-relaxed mb-4">Bonaire’s south coast is known for salt works landscapes and flamingo habitat around Pekelmeer. The sanctuary itself is closed; public roadside viewpoints are the usual cruise-day approach.</p>
        <p class="text-gray-600 leading-relaxed mb-6">Read the island-tour page for slave huts, lighthouse context, and honest north/south trade-offs before you stack activities.</p>
        <a href="/bonaire-island-tour" class="text-ocean-600 font-semibold text-sm hover:text-ocean-800">Explore Bonaire island tours →</a>
      </div>
    </div>
  </div>
</section>

{cruise_snapshot([
    ("Port", "Kralendijk (North Pier / South Pier)"),
    ("Currency", "US dollar"),
    ("Typical call", "Often a full daytime window — confirm your ship"),
    ("Key choice", "Land sightseeing vs Klein boat vs easy town"),
])}

{faq_section(FAQ_HOME, heading="Bonaire cruise excursion questions")}

{editorial_cta(
    "Ready to request the island sightseeing tour?",
    "Request Bonaire Island Sightseeing Tour online — payment creates a booking request; confirmation follows separately.",
    "/book/bonaire-island-sightseeing-tour",
    "Request island sightseeing tour",
)}

{related_links([
    ("/bonaire-island-tour", "Island tour guide"),
    ("/best-bonaire-shore-excursions", "Compare options"),
    ("/bonaire-cruise-port-guide", "Port guide"),
    ("/contact", "Contact"),
])}
"""


def island_tour_body() -> str:
    return f"""
{cruise_snapshot([
    ("Best for", "Sightseeing without a boat transfer"),
    ("Signature themes", "Salt pans, flamingo viewing context, slave huts"),
    ("Watch-outs", "No sanctuary entry; wildlife not guaranteed"),
    ("Port link", '<a href="/bonaire-cruise-port-guide" class="text-ocean-600 underline">Kralendijk pier guide</a>'),
])}

<section class="pt-8 pb-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Island touring from the cruise port</h2>
        <p class="text-gray-600 leading-relaxed mb-4">A Bonaire island tour from Kralendijk is usually a road-based sightseeing outing. Operators differ, but cruise-friendly products often prioritise the south loop’s salt-pan landscapes and historic landmarks, with optional north viewpoints when time allows.</p>
        <p class="text-gray-600 leading-relaxed mb-4">This page explains what those themes mean for a ship day — not a fixed timed itinerary. Stop order, dwell time, and inclusions vary. Confirm details with your operator and keep a personal return buffer.</p>
        <p class="text-gray-600 leading-relaxed">If your priority is reef time on an uninhabited islet, see <a href="/klein-bonaire-snorkeling" class="text-ocean-600 font-semibold underline">Klein Bonaire snorkelling</a> instead.</p>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] overflow-hidden shadow-xl">
        <img src="{FLAMINGO}" alt="{FLAMINGO_ALT}" width="800" height="600" loading="eager" decoding="async" />
      </div>
    </div>
  </div>
</section>

<section id="flamingos-salt" class="py-16 bg-sand-50 scroll-mt-20">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Flamingos and salt flats — careful framing</h2>
    <p class="text-gray-600 leading-relaxed mb-4 max-w-3xl">Southern Bonaire is famous for salt works and Caribbean flamingo habitat around the <strong>Pekelmeer Flamingo Sanctuary</strong>. The sanctuary is a protected area. Visitors are not allowed into the closed sanctuary itself.</p>
    <p class="text-gray-600 leading-relaxed mb-4 max-w-3xl">Cruise-day viewing is typically from <strong>public roadside vantage points</strong> along the south coastal road. Birds may be distant; numbers and proximity change with season, time of day, and disturbance. Treat sightings as <em>possible viewing opportunities</em>, never as guaranteed wildlife encounters.</p>
    <p class="text-gray-600 leading-relaxed max-w-3xl">Stay on public ground, keep respectful distance, and follow local guidance. Do not enter fenced or posted sanctuary areas.</p>
  </div>
</section>

<section class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-10 text-center">Themes often included on south-focused tours</h2>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
      <div class="rounded-2xl border border-gray-100 p-6 bg-white shadow-sm">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Salt pans</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Evaporation ponds and salt-work landscapes create the pink-and-white scenery many visitors associate with southern Bonaire.</p>
      </div>
      <div class="rounded-2xl border border-gray-100 p-6 bg-white shadow-sm">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Slave huts</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Historic stone huts near the salt works are a common photo stop and a sober reminder of the island’s salt-industry history.</p>
      </div>
      <div class="rounded-2xl border border-gray-100 p-6 bg-white shadow-sm">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Willemstoren lighthouse</h3>
        <p class="text-sm text-gray-500 leading-relaxed">The southern lighthouse area is a frequent landmark stop on coastal loops — useful orientation, not a lengthy attraction by itself.</p>
      </div>
      <div class="rounded-2xl border border-gray-100 p-6 bg-white shadow-sm">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Kralendijk</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Colourful waterfront streets sit beside the cruise piers. Some tours include a short town orientation; others leave free time at the end.</p>
      </div>
      <div class="rounded-2xl border border-gray-100 p-6 bg-white shadow-sm">
        <h3 class="font-display font-semibold text-gray-900 mb-2">1000 Steps viewpoint</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Often a brief north-coast photo stop. The name overstates the stair count; a full beach descent is not always part of a sightseeing tour.</p>
      </div>
      <div class="rounded-2xl border border-gray-100 p-6 bg-white shadow-sm">
        <h3 class="font-display font-semibold text-gray-900 mb-2">North / south contrast</h3>
        <p class="text-sm text-gray-500 leading-relaxed">South is salt and sanctuary landscapes; north trends rockier and greener. Full Washington Slagbaai park circuits usually need more time than a short cruise call comfortably allows.</p>
      </div>
    </div>
  </div>
</section>

<section class="py-16 bg-sand-50">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Cruise-day practicality</h2>
    <ul class="space-y-3 text-gray-600 text-sm leading-relaxed list-disc pl-5">
      <li>Meeting points are usually near the Kralendijk cruise pier — confirm your berth and pickup sign.</li>
      <li>Land tours avoid boat weather risk, but vehicles still face traffic and heat on busy days.</li>
      <li>Do not stack a full north park day with Klein Bonaire unless your call is unusually long.</li>
      <li>Nature Fee rules mainly affect marine park water entry and Washington Slagbaai — verify if your product needs them.</li>
    </ul>
  </div>
</section>

{faq_section(FAQ_ISLAND, heading="Island tour questions")}

{editorial_cta(
    "Request Bonaire Island Sightseeing Tour",
    "Pay securely to send a booking request. Confirmation is emailed separately after we arrange your places. Free cancellation outside 14 days before your excursion.",
    "/book/bonaire-island-sightseeing-tour",
    "Request this tour",
)}

{related_links([
    ("/bonaire-cruise-port-guide", "Port guide"),
    ("/klein-bonaire-snorkeling", "Klein Bonaire"),
    ("/best-bonaire-shore-excursions", "Best excursions"),
    ("/", "Home"),
])}
"""


def klein_body() -> str:
    return f"""
{cruise_snapshot([
    ("Access", "Boat or water taxi from near Kralendijk"),
    ("Known beach", "No Name Beach (among others)"),
    ("Setting", "Uninhabited islet · marine park"),
    ("Key risks", "Weather, boarding, mobility, return timing"),
])}

<section class="pt-8 pb-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Klein Bonaire for cruise passengers</h2>
        <p class="text-gray-600 leading-relaxed mb-4">Klein Bonaire is the small, uninhabited island lying just west of Kralendijk. It is part of the wider Bonaire National Marine Park story and is popular for beach time and snorkelling when sea conditions cooperate.</p>
        <p class="text-gray-600 leading-relaxed mb-4">It is not a walk-off excursion. You need a boat transfer. Meeting points may be pier-adjacent or a short walk to a marina / water-taxi area — read your confirmation carefully.</p>
        <p class="text-gray-600 leading-relaxed">For land-only flamingo and salt-pan sightseeing, use the <a href="/bonaire-island-tour" class="text-ocean-600 font-semibold underline">island tour guide</a> instead.</p>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] overflow-hidden shadow-xl">
        <img src="{SNORKEL}" alt="{SNORKEL_ALT}" width="800" height="600" loading="eager" decoding="async" />
      </div>
    </div>
  </div>
</section>

<section class="py-16 bg-sand-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-8">What to plan for</h2>
    <div class="grid md:grid-cols-2 gap-8">
      <div class="bg-white rounded-2xl border border-gray-100 p-6">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Boat logistics</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Crossings are short relative to many Caribbean island hops, but boarding queues and tendering (if your ship is not pier-side) can still consume morning time. Build buffer before all aboard.</p>
      </div>
      <div class="bg-white rounded-2xl border border-gray-100 p-6">
        <h3 class="font-display font-semibold text-gray-900 mb-2">No Name Beach &amp; snorkelling</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Many visitors associate Klein with No Name Beach and nearby reef entry. Clarity and marine life vary with conditions. Do not treat turtles, specific fish, or calm seas as promises.</p>
      </div>
      <div class="bg-white rounded-2xl border border-gray-100 p-6">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Marine park / STINAPA</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Water activities fall under marine-park conservation rules. A STINAPA Nature Fee is typically required for park water use — verify current rates and cruise-day options with official sources or your operator.</p>
      </div>
      <div class="bg-white rounded-2xl border border-gray-100 p-6">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Weather &amp; mobility</h3>
        <p class="text-sm text-gray-500 leading-relaxed">Wind and swell can change comfort and safety. Beach landings and boat steps can be difficult with limited mobility. Ask about boarding method before you commit.</p>
      </div>
    </div>
  </div>
</section>

<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Honest return planning</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Operators often schedule returns with ship times in mind, but delays happen — weather holds, medical assists, crowded docks. Keep your own buffer and know how to reach the pier independently if plans change.</p>
    <p class="text-gray-600 leading-relaxed">This guide does not guarantee ship return. Your all-aboard time is defined by your cruise line.</p>
  </div>
</section>

{faq_section(FAQ_KLEIN, heading="Klein Bonaire questions")}

{editorial_cta(
    "Still deciding between land and water?",
    "Compare Klein against island sightseeing and easier town options on the excursions hub.",
    "/best-bonaire-shore-excursions",
    "Compare excursion types",
)}

{related_links([
    ("/bonaire-cruise-port-guide", "Port guide"),
    ("/bonaire-island-tour", "Island tour"),
    ("/best-bonaire-shore-excursions", "Best excursions"),
])}
"""


def port_guide_body() -> str:
    return f"""
{cruise_snapshot([
    ("Piers", "North Pier and South Pier (Kralendijk waterfront)"),
    ("Town", "Generally walkable from the ship"),
    ("Transfers", "Taxi / tour pickup for south or north loops"),
    ("Klein", "Requires boat departure — not a pier stroll"),
])}

<section class="pt-8 pb-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Kralendijk cruise port orientation</h2>
        <p class="text-gray-600 leading-relaxed mb-4">Cruise ships calling at Bonaire dock at Kralendijk. Pier naming in passenger materials often distinguishes <strong>North Pier</strong> and <strong>South Pier</strong> along the central waterfront. Both place you near town; your exact berth still matters for meeting signs and walking routes.</p>
        <p class="text-gray-600 leading-relaxed mb-4">We do not invent taxi fares or minute-by-minute transfer times. Use this page for orientation, then confirm live instructions with your ship and operator.</p>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] overflow-hidden shadow-xl">
        <img src="{CRUISE_PORT}" alt="{CRUISE_PORT_ALT}" width="800" height="600" loading="eager" decoding="async" />
      </div>
    </div>
  </div>
</section>

<section class="py-16 bg-sand-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-8 text-center">Practical building blocks</h2>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="bg-white rounded-2xl p-6 border border-gray-100">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Walkability</h3>
        <p class="text-sm text-gray-500">Kralendijk’s waterfront and shopping streets are close enough for many guests to explore on foot. Heat and sun still matter — carry water.</p>
      </div>
      <div class="bg-white rounded-2xl p-6 border border-gray-100">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Tour pickup</h3>
        <p class="text-sm text-gray-500">Island tours typically meet near the pier. Confirm colour cards, vehicle type, and whether your berth is North or South Pier that day.</p>
      </div>
      <div class="bg-white rounded-2xl p-6 border border-gray-100">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Klein departures</h3>
        <p class="text-sm text-gray-500">Boat products may start at the pier area or after a short walk to a marina. Budget time for the walk and boarding, not only the crossing.</p>
      </div>
      <div class="bg-white rounded-2xl p-6 border border-gray-100">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Island-tour logistics</h3>
        <p class="text-sm text-gray-500">South loops reach salt pans and sanctuary roadside viewpoints relatively quickly; combining them with a full north park visit is a different day shape.</p>
      </div>
      <div class="bg-white rounded-2xl p-6 border border-gray-100">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Marine park context</h3>
        <p class="text-sm text-gray-500">Snorkel and dive days interact with STINAPA Nature Fee rules. Land-only sightseeing may not need a fee — verify for your specific plan.</p>
      </div>
      <div class="bg-white rounded-2xl p-6 border border-gray-100">
        <h3 class="font-display font-semibold text-gray-900 mb-2">Short vs longer calls</h3>
        <p class="text-sm text-gray-500">A shorter window favours town, a short south loop, or a carefully timed boat trip — not stacking Klein plus Washington Slagbaai plus shopping.</p>
      </div>
    </div>
  </div>
</section>

<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Return planning</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Treat all-aboard as a hard constraint from your cruise line. Build buffer for taxi queues, boat returns, and pier congestion. Mobility needs change boarding time — ask operators early.</p>
    <p class="text-gray-600 leading-relaxed">See also: <a href="/bonaire-island-tour" class="text-ocean-600 underline">island tour</a> · <a href="/klein-bonaire-snorkeling" class="text-ocean-600 underline">Klein Bonaire</a>.</p>
  </div>
</section>

{faq_section(FAQ_PORT, heading="Port day questions")}

{editorial_cta(
    "Choose your shore plan",
    "With pier orientation clear, compare island sightseeing versus Klein and easier town options.",
    "/best-bonaire-shore-excursions",
    "Compare Bonaire shore excursions",
)}

{related_links([
    ("/bonaire-island-tour", "Island tour"),
    ("/klein-bonaire-snorkeling", "Klein Bonaire"),
    ("/", "Home"),
])}
"""


def best_body() -> str:
    return f"""
<section class="pt-10 pb-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Compare Bonaire shore excursion types</h2>
    <p class="text-gray-600 leading-relaxed">This is a comparison guide for cruise passengers — not a ranked top-ten, not a review scoreboard, and not a live booking list. Match the category to your usable hours, mobility, and risk tolerance.</p>
  </div>
</section>

<section class="py-12 bg-sand-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <article class="bg-white rounded-2xl border border-gray-100 p-6 md:p-8 shadow-sm">
      <h3 class="text-xl font-display font-semibold text-gray-900 mb-2">Island tour</h3>
      <p class="text-sm text-gray-500 leading-relaxed mb-3">Land sightseeing from Kralendijk — salt pans, flamingo viewing context from public roads, slave huts, lighthouse, and town orientation. Lower sea-state risk than boat days; wildlife still not guaranteed.</p>
      <a href="/bonaire-island-tour" class="text-ocean-600 text-sm font-semibold">Explore Bonaire island tours →</a>
    </article>
    <article class="bg-white rounded-2xl border border-gray-100 p-6 md:p-8 shadow-sm">
      <h3 class="text-xl font-display font-semibold text-gray-900 mb-2">Klein Bonaire</h3>
      <p class="text-sm text-gray-500 leading-relaxed mb-3">Boat access to an uninhabited marine-park islet for beach and snorkel time. Logistics, weather, and mobility matter more than on a van tour.</p>
      <a href="/klein-bonaire-snorkeling" class="text-ocean-600 text-sm font-semibold">Read the Klein Bonaire guide →</a>
    </article>
    <article class="bg-white rounded-2xl border border-gray-100 p-6 md:p-8 shadow-sm">
      <h3 class="text-xl font-display font-semibold text-gray-900 mb-2">Snorkel / sail</h3>
      <p class="text-sm text-gray-500 leading-relaxed mb-3">Coastal sail or snorkel products may use marine-park waters, sometimes near Klein. Check age rules, swimming ability, boarding walk, and Nature Fee needs. Reef life is never guaranteed.</p>
      <a href="/bonaire-cruise-port-guide" class="text-ocean-600 text-sm font-semibold">Port logistics to consider →</a>
    </article>
    <article class="bg-white rounded-2xl border border-gray-100 p-6 md:p-8 shadow-sm">
      <h3 class="text-xl font-display font-semibold text-gray-900 mb-2">South island / flamingo–salt focus</h3>
      <p class="text-sm text-gray-500 leading-relaxed mb-3">Shorter south loops emphasise salt works and sanctuary roadside views. Often overlaps with island-tour products — covered in depth on the island-tour page rather than a separate flamingo site.</p>
      <a href="/bonaire-island-tour#flamingos-salt" class="text-ocean-600 text-sm font-semibold">Flamingos &amp; salt section →</a>
    </article>
    <article class="bg-white rounded-2xl border border-gray-100 p-6 md:p-8 shadow-sm">
      <h3 class="text-xl font-display font-semibold text-gray-900 mb-2">Easy / town day</h3>
      <p class="text-sm text-gray-500 leading-relaxed mb-3">Stay near Kralendijk: waterfront walking, cafés, light shopping. Best when you want minimal transfer risk or have a short call.</p>
      <a href="/bonaire-cruise-port-guide" class="text-ocean-600 text-sm font-semibold">Kralendijk port guide →</a>
    </article>
  </div>
</section>

{editorial_cta(
    "Request the island sightseeing tour",
    "If land sightseeing is your lead choice, request Bonaire Island Sightseeing Tour — or keep reading the editorial island-tour guide first.",
    "/book/bonaire-island-sightseeing-tour",
    "Request island sightseeing tour",
)}

{related_links([
    ("/bonaire-island-tour", "Island tour guide"),
    ("/klein-bonaire-snorkeling", "Klein"),
    ("/bonaire-cruise-port-guide", "Port"),
    ("/", "Home"),
])}
"""


def contact_body() -> str:
    return f"""
<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Contact</h2>
    <p class="text-gray-600 leading-relaxed mb-6">Editorial questions about this Bonaire cruise planning guide can be sent to:</p>
    <p class="text-lg font-semibold text-ocean-700 mb-8"><a href="mailto:{EMAIL}" class="hover:underline">{EMAIL}</a></p>
    <p class="text-sm text-gray-500 leading-relaxed mb-4">You can request Bonaire Island Sightseeing Tour online at <a href="/book/bonaire-island-sightseeing-tour" class="text-ocean-600 underline">/book/bonaire-island-sightseeing-tour</a>. Payment creates a booking request — confirmation is emailed separately.</p>
    <p class="text-sm text-gray-500 leading-relaxed">For urgent ship-day issues, contact your cruise line guest services or your tour operator directly.</p>
  </div>
</section>
"""


def about_body() -> str:
    return f"""
<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 prose-like">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">About Bonaire Cruise Excursions</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Bonaire Cruise Excursions is an independent editorial site that helps cruise passengers understand port logistics and excursion trade-offs when calling at Kralendijk.</p>
    <p class="text-gray-600 leading-relaxed mb-4">We are not a cruise line, not a shore-excursion marketplace, and not affiliated with STINAPA or Cargill salt operations. Content emphasises cruise-day usefulness over tourism filler.</p>
    <p class="text-gray-600 leading-relaxed">Contact: <a href="mailto:{EMAIL}" class="text-ocean-600 underline">{EMAIL}</a></p>
  </div>
</section>
"""


def privacy_body() -> str:
    return f"""
<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Privacy</h2>
    <p class="text-gray-600 leading-relaxed mb-4">This website is an editorial planning guide. If you email {EMAIL}, we use your message only to respond to your enquiry.</p>
    <p class="text-gray-600 leading-relaxed mb-4">We do not operate an on-site booking checkout in this phase. Standard hosting and analytics logs may be processed by our infrastructure providers (including Cloudflare) to operate and secure the site.</p>
    <p class="text-gray-600 leading-relaxed">We do not sell personal data. For privacy questions, email {EMAIL}.</p>
  </div>
</section>
"""


def terms_body() -> str:
    return f"""
<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Terms</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Content on bonairecruiseexcursions.com is general information for cruise passengers. It is not a contract for travel services, not professional advice, and not a guarantee of conditions ashore.</p>
    <p class="text-gray-600 leading-relaxed mb-4">Port operations, marine-park rules, Nature Fees, wildlife presence, weather, and operator policies can change. Always confirm details with your cruise line and service providers before travel.</p>
    <p class="text-gray-600 leading-relaxed">You are responsible for returning to your ship on time. Questions: {EMAIL}.</p>
  </div>
</section>
"""


def methodology_body() -> str:
    return f"""
<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Methodology</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Phase 20B rebuilt this site as static, crawlable HTML with extensionless canonical URLs. We prioritised cruise usefulness: pier orientation, activity trade-offs, and honest limits on wildlife and return claims.</p>
    <p class="text-gray-600 leading-relaxed mb-4">Flamingo sanctuary access language reflects publicly documented STINAPA / destination guidance that Pekelmeer is closed to visitors and viewing is from public roads. Nature Fee details should be rechecked at official STINAPA sources before travel.</p>
    <p class="text-gray-600 leading-relaxed mb-4">We do not publish supplier codes, live prices, or fabricated reviews. Image provenance for some assets remains unresolved and is documented in images/ATTRIBUTION.md.</p>
    <p class="text-gray-600 leading-relaxed">Contact: <a href="mailto:{EMAIL}" class="text-ocean-600 underline">{EMAIL}</a></p>
  </div>
</section>
"""


def not_found_body() -> str:
    return """
<section class="py-24 bg-white">
  <div class="max-w-xl mx-auto px-4 text-center">
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Page not found</h2>
    <p class="text-gray-600 mb-8">That URL is not part of this Bonaire cruise planning guide.</p>
    <a href="/" class="btn-ocean inline-flex text-white font-semibold px-7 py-3 rounded-full text-sm">Back to homepage</a>
  </div>
</section>
"""


def all_pages() -> dict[str, str]:
    pages: dict[str, str] = {}

    pages["/"] = page_shell(
        title="Bonaire Cruise Excursions | Kralendijk Shore Tours & Port Planning",
        description="Plan Bonaire cruise excursions from Kralendijk — island sightseeing, Klein Bonaire snorkelling context, salt-pan landscapes, and realistic port-day choices.",
        canonical_path="/",
        page_id="home",
        hero_html=hero_band(
            eyebrow="Bonaire · Dutch Caribbean",
            title_html='Bonaire Cruise<br/><span class="text-teal-300">Excursions</span>',
            lead="Independent planning for cruise guests in Kralendijk — island tours, Klein Bonaire, and port logistics without wildlife or return guarantees.",
            image=CRUISE_PORT,
            aria_label=CRUISE_PORT_ALT,
            actions=(
                '<a href="/best-bonaire-shore-excursions" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare options</a>'
                '<a href="/bonaire-island-tour" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Island tour</a>'
            ),
            tags=["Island tour", "Klein Bonaire", "Kralendijk", "Salt & flamingos"],
        ),
        main_html=home_body(),
        og_image=CRUISE_PORT,
        faq_entities=FAQ_HOME,
    )

    pages["/bonaire-island-tour"] = page_shell(
        title="Bonaire Island Tour from the Cruise Port | Salt Pans & Sightseeing",
        description="Plan a Bonaire island tour from Kralendijk — salt pans, Pekelmeer flamingo viewing context, slave huts, lighthouse, and cruise-day sightseeing trade-offs.",
        canonical_path="/bonaire-island-tour",
        page_id="island-tour",
        hero_html=hero_band(
            eyebrow="Sightseeing · From Kralendijk",
            title_html='Bonaire Island Tour<br/><span class="text-teal-300">from the Cruise Port</span>',
            lead="South salt pans, roadside flamingo viewing context, slave huts, and lighthouse landmarks — planned around a ship day, without invented itineraries or wildlife guarantees.",
            image=FLAMINGO,
            aria_label=FLAMINGO_ALT,
            breadcrumb="Island Tour",
            actions=(
                '<a href="/best-bonaire-shore-excursions" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare options</a>'
                '<a href="/bonaire-cruise-port-guide" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Port guide</a>'
            ),
            tags=["Salt pans", "Flamingo viewing", "Slave huts", "Kralendijk"],
        ),
        main_html=island_tour_body(),
        og_image=FLAMINGO,
        faq_entities=FAQ_ISLAND,
    )

    pages["/klein-bonaire-snorkeling"] = page_shell(
        title="Klein Bonaire Snorkelling | Cruise Day Boat Planning from Kralendijk",
        description="Plan Klein Bonaire from a Bonaire cruise call — boat logistics, No Name Beach context, marine park notes, weather, mobility, and honest return buffers.",
        canonical_path="/klein-bonaire-snorkeling",
        page_id="klein",
        hero_html=hero_band(
            eyebrow="Marine park · Uninhabited islet",
            title_html='Klein Bonaire<br/><span class="text-teal-300">Snorkelling</span>',
            lead="Boat access to Bonaire’s uninhabited sister isle — beach and reef context for cruise guests, without return or wildlife guarantees.",
            image=SNORKEL,
            aria_label=SNORKEL_ALT,
            breadcrumb="Klein Bonaire",
            actions=(
                '<a href="/bonaire-cruise-port-guide" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Port guide</a>'
                '<a href="/best-bonaire-shore-excursions" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Compare options</a>'
            ),
            tags=["Boat transfer", "No Name Beach", "Marine park", "Cruise planning"],
        ),
        main_html=klein_body(),
        og_image=SNORKEL,
        faq_entities=FAQ_KLEIN,
    )

    pages["/bonaire-cruise-port-guide"] = page_shell(
        title="Bonaire Cruise Port Guide | Kralendijk North & South Pier",
        description="Bonaire cruise port guide for Kralendijk — North Pier and South Pier orientation, walkability, tour pickup, Klein boat practicality, and return planning.",
        canonical_path="/bonaire-cruise-port-guide",
        page_id="port",
        hero_html=hero_band(
            eyebrow="Port orientation",
            title_html='Bonaire<br/><span class="text-teal-300">Cruise Port Guide</span>',
            lead="Kralendijk pier orientation for cruise passengers — walkability, pickup logic, and how island tours and Klein boat days fit a ship schedule.",
            image=CRUISE_PORT,
            aria_label=CRUISE_PORT_ALT,
            breadcrumb="Port Guide",
            actions=(
                '<a href="/best-bonaire-shore-excursions" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare options</a>'
                '<a href="/bonaire-island-tour" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Island tour</a>'
            ),
            tags=["North Pier", "South Pier", "Kralendijk", "Pickup"],
        ),
        main_html=port_guide_body(),
        og_image=CRUISE_PORT,
        faq_entities=FAQ_PORT,
    )

    pages["/best-bonaire-shore-excursions"] = page_shell(
        title="Best Bonaire Shore Excursions | Compare Island, Klein & Town Options",
        description="Compare Bonaire shore excursion types for cruise passengers — island tour, Klein Bonaire, snorkel/sail, south flamingo-salt focus, and easy town days.",
        canonical_path="/best-bonaire-shore-excursions",
        page_id="excursions",
        hero_html=hero_band(
            eyebrow="Comparison guide",
            title_html='Best Bonaire<br/><span class="text-teal-300">Shore Excursions</span>',
            lead="A category comparison for cruise days in Kralendijk — no fake rankings, ratings, or popularity scores.",
            image=None,
            aria_label="Bonaire shore excursion planning",
            css_only=True,
            breadcrumb="Excursions",
            actions=(
                '<a href="/bonaire-island-tour" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Island tour</a>'
                '<a href="/klein-bonaire-snorkeling" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Klein Bonaire</a>'
            ),
            tags=["Compare", "Island", "Klein", "Town"],
        ),
        main_html=best_body(),
        og_image=FLAMINGO,
    )

    for path, title, desc, page_id, body_fn in [
        ("/contact", "Contact | Bonaire Cruise Excursions", "Contact Bonaire Cruise Excursions for editorial questions about this Kralendijk cruise planning guide.", "contact", contact_body),
        ("/about", "About | Bonaire Cruise Excursions", "About Bonaire Cruise Excursions — independent cruise planning editorial for Kralendijk, Bonaire.", "about", about_body),
        ("/privacy", "Privacy | Bonaire Cruise Excursions", "Privacy information for bonairecruiseexcursions.com.", "privacy", privacy_body),
        ("/terms", "Terms | Bonaire Cruise Excursions", "Terms of use for the Bonaire Cruise Excursions planning guide.", "terms", terms_body),
        ("/methodology", "Methodology | Bonaire Cruise Excursions", "How Bonaire Cruise Excursions approaches cruise-useful editorial content.", "methodology", methodology_body),
    ]:
        pages[path] = page_shell(
            title=title,
            description=desc,
            canonical_path=path,
            page_id=page_id,
            hero_html=hero_band(
                eyebrow="Bonaire Cruise Excursions",
                title_html=title.split("|")[0].strip(),
                lead=desc,
                image=None,
                aria_label=title,
                css_only=True,
                breadcrumb=title.split("|")[0].strip(),
            ),
            main_html=body_fn(),
            og_image=None,
            include_trust=False,
        )

    pages["/404.html"] = page_shell(
        title="Page not found | Bonaire Cruise Excursions",
        description="The requested page was not found on Bonaire Cruise Excursions.",
        canonical_path="/404.html",
        page_id="notfound",
        hero_html=hero_band(
            eyebrow="Error",
            title_html="404",
            lead="This page is not part of the guide.",
            image=None,
            aria_label="Not found",
            css_only=True,
        ),
        main_html=not_found_body(),
        og_image=None,
        robots="noindex",
        include_trust=False,
    )

    return pages
