# ATELIER — feature map for a complete "Faye" section

**Scope note:** this is planning beyond the four locked hackathon screens (`brief/screen-flow.md`). An experimental onboarding prototype was archived and is not part of the submission. Nothing here changes the locked deliverable — it asks what a shippable service would require: what earns a place on the core path, what can wait, and what its hardest state looks like. Fixed inputs treated as given, not relitigated: HERMES's persona and copy (`02-HERMES-offer-and-persona.md`), MIDAS's scenario economics and regulatory review (`01-MIDAS-business-model.md` §2, §5), and the locked product rules in `CLAUDE.md` (no star ratings, no numeric mood scores, no streaks/gamification in this section).

**Current status:** this is a feature exploration, not a production-ready requirement list. `06-PRODUCT-SPEC-AND-ROADMAP.md` selects the first build slice and supersedes assumptions here that credit packs are fixed, a payment descriptor can be promised before rail testing, or any particular helpline is ready to ship. The therapist-switch note, expanded history, and passive slot alert come later only if users need them and governance is ready.

A feature earns "core" here on one test: **does Ananya's own stated fear or the regulatory reality in MIDAS §5 require it to exist**, not "would a mature wellness app typically have this." Several things a mature wellness app typically has are rejected below for exactly that reason.

---

## Core path

### 1. Therapist detail / profile page

**What:** a full profile behind each discovery card — credentials (registration status where applicable, not just a bare "Verified" badge), approach/specialisation in plain language, languages, a short written intro in the provider's own words, and clear session terms. Avoid unsupported "recommended by members like you" social proof, star ratings, or review counts. The no-ratings lock from `CLAUDE.md` §3 applies here just as much as on the discovery list.

**Why core, not nice-to-have:** the discovery card is a summary built for scanning several therapists at once; it cannot carry the weight of an actual trust decision. Asking her to book directly from a card she tapped once, with no fuller picture of the person, works against the entire trust-transfer thesis this section is built on. A first-time seeker deciding whether to trust a specific stranger with something this personal needs more surface area than a card gives, or the booking flow is skipping the actual decision point and pretending the card already made it.

**Hardest state:** two, not one.
- **No availability in the visible window.** Never a dead end and never fake urgency in the other direction ("only 2 slots left!" is refused outright — it's the same dark pattern this brief already refuses on cancellation policy, just inverted). The honest version: "Fully booked for now" plus a passive, opt-in "Tell me when a slot opens" (no countdown, no pressure), plus two or three similar-concern therapists surfaced immediately below so she isn't left with nothing to do.
- **Thin profile (new-to-platform therapist, bio not yet filled in).** Must not read as broken or untrustworthy by omission. Concretely: the credential badge and specialisation tags still render fully (those are operationally required data, always present), only the optional written intro is missing, and its absence is filled with a plain, non-apologetic placeholder ("New on Faye — full credentials verified, bio coming soon") rather than an empty gap that reads like a loading failure.

### 2. My Sessions (booking management)

**What:** a persistent list of upcoming and past bookings — reschedule/cancel already exists per-session in the confirmation screen, but there's currently no way to see what you've booked *besides* the one confirmation screen you saw right after booking. Reuses the existing card/kv component language verbatim.

**Why core:** without this, every session becomes a fresh "did I actually book this" moment — the opposite of the calm, low-cognitive-load design this whole section is arguing for. A booking flow with a confirmation screen and no persistent record of that confirmation is an incomplete flow, not a trimmed one.

**Hardest state:** the empty state, first time, zero sessions ever booked. This is the one place in the whole feature map where a generic app would default to a pushy "Book your first session!" activation nudge — refused here on the same non-forcible-language grounds HERMES cites in §4 (the doubled-engagement finding for autonomy-respecting phrasing). The honest version: a single quiet line ("Nothing booked yet — that's alright") and one calm, ghost-style link back to discovery, not a coral CTA competing for attention against nothing.

### 3. Credit pack & billing

**What:** view/buy a Steady credit pack (per MIDAS §2's locked packaging), remaining credit balance, and a plain-language billing/statement view.

**Why core, and why it's a stronger feature than it sounds:** HERMES names Ananya's fear #1 explicitly — her parents finding a session on a shared family card. That fear has a concrete, buildable answer that isn't just copy: **this screen should state, in plain words, exactly what the charge will look like on a bank or card statement** — e.g. "This will show as *CULTFIT WELLNESS* on your statement, not a therapist's name and not the word 'therapy.'" That is a real product decision (it requires the actual payment gateway to be configured with that statement descriptor, not just UI text promising it — flagging this for Lego explicitly, see closing note) built directly from a named, specific persona fear, not a decorative addition.

**Hardest state:** a failed or declined payment mid-purchase. This must never silently consume a credit or show a false "purchased" state. An unconfirmed transaction is never treated as confirmed: show the failure plainly, keep her existing credit balance untouched and visible, and offer retry.

### 4. Crisis-support pattern

**What:** a single, quietly persistent, always-visible link — same location on the mood dashboard and the content/resource screen, never a popup that interrupts a routine check-in — reading something like "Need urgent support?" It leads to one plain screen that says Faye is not an emergency service and shows a small, operator-verified, maintained list of help routes with hours and languages. No number from this concept document should be hardcoded without current verification; see Lego §3.

**Why core:** MIDAS §5 names this directly — an adverse event during or after a session booked through this platform is real legal exposure, not a bad review, and it's a binary risk that can't be designed around after the fact. A mental-health surface with no visible "this isn't for emergencies, here's what is" pattern anywhere in it is an actual gap, not a missing nice-to-have.

**Hardest state:** the help link's visibility stays constant regardless of what she logs. A "Low" or "Anxious" icon, even on several days, is not a diagnostic or crisis signal; it must not trigger a clinical warning, popup, or automatic paid-session prompt. The user can choose resources or therapist discovery through their ordinary routes. This preserves a calm, predictable interface and avoids treating sparse mood entries as clinical evidence.

**Added from an independent cross-domain safety review, 2026-09-26: two notification-copy requirements this map didn't previously state.** (1) Any push notification for Faye/Steady must show generic content on a lock screen — "Cult.fit: you have a reminder," never a therapist's name, session time, or the word "therapy" — matching the same discretion HERMES's persona fear #1 already drives everywhere else in this flow; a notification is the one surface that bypasses every in-app privacy control by design, since it renders before the app is even opened. (2) No notification copy anywhere in Faye may use loss-framed or urgency language ("don't lose your progress," "you're falling behind") — this extends the existing no-gamification/no-streaks lock from the UI layer, where it's already enforced, to push-copy specifically, which is a separate surface the lock doesn't automatically cover.

### 5. Privacy controls, surfaced after onboarding

**What:** any future fitness-cross-share choice needs a permanent home after onboarding — most naturally a "Privacy" row inside the existing Profile tab (reusing wherever Cult.fit's account settings already live) rather than a new settings surface invented just for Faye.

**Why core:** a consent choice that can only be set once at first run, with no route back, cannot support a meaningful change or withdrawal. A permanent control and clear status are required before making a "change it anytime" promise.

**Hardest state:** she turns the toggle off after having had it on for a while. The UI must stop new cross-sharing and show the server-confirmed status. A follow-up primary-law review found that DPDP §8(7) can require erasure on withdrawal unless legal retention is necessary; §12 also provides a separate erasure-request route. Show deletion as pending until recipients confirm, explain any lawful retention, and keep a separate data-request path. Legal scope and commencement still need counsel review; see Lego §4 and the build spec.

### 6. Therapist-switch flow, with a one-time carry-forward note

**What:** an easy, guilt-free "this isn't the right fit" path off the therapist detail/My Sessions screens, paired with a short structured note — the concern tags she already picked during discovery, plus one optional free-text line — that she fills in once and can choose to share with a *new* therapist if she switches, rather than starting from a blank page with someone new.

**Why core:** this is HERMES's persona fear #2, named directly in §1 — "picking the wrong therapist and having to explain everything again from scratch." That's not a vague UX nicety, it's a specific, named blocker to activation, and it has a concrete design answer: let the switch be easy, and let the *tags*, not a full case history, travel with her if she opts in. This is opt-in, per-switch, and never automatic — the same consent discipline as everything else in this section.

**Hardest state:** she wants to switch but has an upcoming *paid* session already booked with the original therapist. This needs a graceful reschedule-to-new-therapist or refund-to-credit path, not a dead end where switching means losing money already spent — a real edge case, not a rare one, given fear #2 is named as common.

### 7. Extended mood history

**What:** the existing weekly arc component (`s3`), given a second, equally simple time window — "past month" alongside "this week" — same visual language, same one-line note, nothing new invented.

**Why core-ish (the one item on this list closest to the line):** a therapist relationship benefits from being able to glance back further than seven days, and it costs nothing structurally — no new component, no new interaction pattern, just the same arc rendered over a longer window. It stays in "core" rather than "nice-to-have" because it's this cheap to build honestly within the system that already exists.

**Hardest state:** sparse data (she's only logged three times in the last month). The arc must degrade honestly — a thin, partial arc and "3 check-ins this month" rather than smoothing or interpolating gaps into something that looks like more data than she actually gave it. Manufacturing the appearance of a fuller picture than she provided is a small, specific dishonesty this system should never commit.

---

## Explicitly rejected or deferred, and why

**Therapist messaging between sessions — rejected for the first build.** An open inbox creates expectations about reply times, emergencies, documentation, and provider workload. Those obligations have not been specified or tested here. Offer session-scoped logistics (reschedule, cancel, reminders) and an optional, one-way prep note for a specific appointment instead. Reconsider messaging only with provider contracts, response coverage, record rules, and safety review.

**Peer community / forums — rejected.** A common pattern elsewhere in this category, wrong here specifically: unmoderated peer mental-health content carries real moderation and liability burden (the same MIDAS §5 risk class as messaging, now multiplied across every user instead of one therapist relationship), and it runs directly against the persona's #1 named fear — exposure. A feature that asks her to be visible to other users in a section she opened specifically because it's private is the opposite of what this product is for.

**Referral / sharing ("invite a friend," "share your check-in streak") — rejected.** Directly against the no-gamification, no-comparison lock in `CLAUDE.md` §5, and a second, sharper reason: asking her to surface her use of a mental-health feature socially, even to friends, contradicts the exact privacy promise the whole section is selling. This isn't a gamification call this time, it's a trust call.

**A general "browse all content" library, separate from the concern-filtered resource screen — rejected.** The existing content screen (`s4`) is deliberately narrow and concern-filtered — "the calmest screen in the flow," per the README, on purpose. A second, broader library surface pulls this toward being a general wellness-content app (Headspace/Calm's actual core product) rather than staying a quiet, bounded companion to a therapy-booking flow. That's scope creep dressed as generosity — more content isn't more useful here, it's more to sort through in a state screen-flow.md's own accessibility checklist already names as a low-cognitive-load moment.

**A conversational AI check-in / chatbot (the Wysa pattern) — deferred, not rejected outright.** HERMES cites Wysa favorably for its non-scored, judgment-free framing, and the instinct is reasonable. But a chatbot is not a smaller version of the mood-icon check-in — it's an open-ended text surface that can be asked anything, including things that read as a crisis or a request for clinical advice, and "what does this say back to her" is a much larger safety and liability review than anything else on this list, closer to the messaging question above than to a UI feature. Building it now, inside a craft pass, without that review, would be novelty ahead of use — exactly the thing ATELIER's brief says to refuse. Worth a real look in a later round, with its own dedicated safety pass, not folded into this map as if it were routine.

**A standalone Faye-specific notification-preferences screen — rejected.** The behavior-triggered "Notice" prompt from HERMES §4 and a session reminder both need to exist, but a whole parallel settings surface just for Faye's notifications duplicates wherever Cult.fit's account-wide notification settings already live, and fragments where privacy-adjacent controls live across the app — worse for her, not better, than one consistent place. Reuse the existing surface; don't build a second one.

**A denser analytics/quantified-self dashboard (multi-metric history, correlations, exportable data) — rejected.** This is the most tempting kind of scope-bloat because it looks like "more value" — it is in fact the opposite of the locked design bet: a single soft arc instead of a dense chart is a named, deliberate decision in `screen-flow.md` §3, made specifically to avoid the clinical, overstimulating register this whole section exists to move away from. Item 7 above (a longer time window on the *same* simple arc) is the correct-sized version of "more history"; a dashboard is not.

---

## For Lego (feasibility next)

Four things in this map are craft-complete but not feasibility-complete, and need a real pass before any of it is buildable:

1. **The statement-descriptor claim on the credit-pack/billing screen** is a real product commitment, not just copy — it requires the actual payment gateway integration to be configured with that descriptor, and needs confirming it can even be guaranteed across every processor Cult.fit uses.
2. **The therapist-switch carry-forward note** is a small data-sharing decision with real consent-scope questions attached: who can read it, how long it persists, and how to obtain a separate, recipient-specific yes.
3. **Crisis-line content** (item 4) cannot ship as copy hardcoded once and forgotten — helpline numbers and services change, and this is the one piece of content in the entire section where being stale is a real-world harm, not a UX nit.
4. **The withdrawal/erasure implementation** under item 5 needs legal review and a real cross-system workflow. The earlier “only stop new sharing” interpretation was corrected after checking DPDP §8(7); see Lego §4.
