# Lego — technical feasibility and compliance calls for the Faye feature map

**2026-09-26 implementation caveat:** this is a concept architecture, not legal advice or a verified production inventory of Cult.fit systems. The DPDP interpretation and clinical-professional classifications below require review against current primary law and counsel before launch. In particular, withdrawal, erasure, exceptions, implementation dates, and recipient deletion cannot be reduced to a UI toggle rule without that review. The safe product contract is narrower: record consent changes, stop newly authorized sharing, offer a separate data request path, and tell the user accurately what happened. `06-PRODUCT-SPEC-AND-ROADMAP.md` defines the operational states and release gates. The current status of KIRAN is unconfirmed; do not infer discontinuation from an unrelated commit or absence from one page.

**Scope note:** answers ATELIER's four named items in `03-ATELIER-feature-map.md` (§"For Lego"), then states the architecture for the full feature map as a Flutter module inside Cult.fit's existing Aurora app — not a from-scratch system. Fixed inputs treated as given: MIDAS's regulatory findings (`01-MIDAS-business-model.md` §5, including the 2026-09-26 verification pass), HERMES's persona/copy, ATELIER's feature map and its four flags, and the locked product rules in `CLAUDE.md`. Per my own discipline: **observed fact**, **inference**, and **proposal** are kept visibly separate below — nothing here is dressed up as more settled than it is.

---

## 1. Payment statement descriptor

**Observed fact:** Razorpay's own dashboard documentation confirms a business "display name" / "profile name" account setting exists, separate from the registered legal entity name (checked directly against `razorpay.com/docs/payments/dashboard/account-settings/account-details`, not assumed). No public Razorpay or Cashfree documentation I could find states, in one place, that this display name is guaranteed to be **the exact string that appears on a customer's card-network or UPI statement, across every rail, self-service, on demand** — that specific end-to-end guarantee is not directly confirmed by either gateway's public docs, and I'm flagging that gap rather than papering over it.

**Inference (reasoned from how Indian payment aggregation actually works, not asserted as fact):** statement-descriptor behavior differs by rail, and this matters directly for Ananya's named fear:
- **UPI** (the most likely dominant rail for a mid-market Indian consumer app): the "payee name" a customer sees, both at authorization and in their UPI app's transaction history, is the merchant's registered VPA display name with the PSP (Razorpay/Cashfree acting as PSP). This is set during merchant onboarding/KYC, not typically a live self-service toggle.
- **Card networks** (Visa/Mastercard/RuPay): the descriptor a bank prints on a statement is tied to the merchant's MID (Merchant ID) with the acquiring bank, provisioned by the gateway during onboarding. This is the layer most likely to still show a generic aggregator string (e.g. `RAZORPAY*CULTFIT` or similar) unless explicitly negotiated with the acquirer — Stripe's own public docs, which are unusually explicit about this exact mechanic, confirm that even there a `statement_descriptor` has real length/character constraints and network-specific quirks; there's no reason to assume Indian card rails are more flexible than that, and some reason (bank-attached MID logic) to think they can be less flexible.
- **Netbanking**: narration is typically bank-controlled, not merchant-controlled, and the weakest link of the three.

**Proposal:** treat the credit-pack screen's statement-descriptor copy as **provisionally correct for UPI, unconfirmed for cards/netbanking** until verified. Concretely:
1. Cult.fit's payments/finance team confirms with their Razorpay/Cashfree account manager (not just the public docs) what descriptor each rail will actually show for the specific MID/VPA used for Faye bookings — and whether Faye needs its **own** MID/sub-merchant ID separate from Cult.fit's fitness MID, because if it's the *same* MID, whatever descriptor gets set applies to every Cult.fit charge, fitness included, which may or may not be what the business wants.
2. Run one real sandbox transaction per rail (UPI, card, netbanking) and read the actual descriptor that lands in a test bank/UPI statement — not the dashboard's stated intent, the observed result.
3. Only after that, let the UI copy make a specific claim ("This will show as X"). Until then, the honest interim copy is a *qualified* claim ("Your statement should show *Cult.fit Wellness*, not a therapist's name") rather than an absolute one, or the claim should be scoped to whichever rail is actually confirmed.

**Status: blocked, needs Cult.fit's payment-gateway account/finance team + one round of sandbox verification.** This is not something Lego can close from documentation alone, and I'm not going to assert a gateway capability as confirmed when the confirmation I could actually find only covers half the claim.

---

## 2. Therapist-switch carry-forward: consent scope

**The actual call (data-model decision, not a legal question — I'm making it):**

Two different things travel in ATELIER's spec, and they need two different consent postures:

- **Structured concern tags** (e.g. "Anxiety," "Sleep") were already collected under the *original* booking's purpose (matching her to a therapist). Re-showing them to a **new, different therapist** is a new disclosure to a new recipient, even though the purpose (matching/context) is similar — under DPDP's purpose-limitation principle (MIDAS §5), a new recipient for even a *similar* purpose still needs its own consent event, not a silent carry-over. ATELIER already designed this correctly as opt-in, per-switch, never automatic — I'm confirming that's the right call, not just a cautious one.
- **The free-text line** is materially higher-risk than the tags: it's unstructured, she wrote it herself, and it can contain anything, including content that reads closer to a clinical disclosure than a tag ever could. It needs the *same* opt-in gate as the tags, plus two things the tags don't need:
  - **A named, scoped recipient, not a stored profile field.** The note must be modeled as "shared with therapist X, as of switch event Y" — not as a persistent attribute of her profile that any future therapist could read. If a second switch happens later, that's a *third* consent event with a *third* scope, not an extension of the first.
  - **A retention boundary.** This product explicitly has no clinician session-notes/documentation regime (ATELIER rejected therapist messaging for exactly this reason — no licensed record-keeping duty exists here for counselors). That means this note is user-authored context, not part of a clinical record, and indefinite retention of it is pure liability with no corresponding duty-of-care benefit. Proposal: it's visible to the new therapist until their first session together happens, or for 90 days, whichever is sooner, then purged from that therapist's access. She can always write a fresh one on a future switch.

**This needs its own consent artifact, distinct from the onboarding fitness-cross-share toggle** — different purpose, different recipient, different data. Reusing the onboarding toggle's consent record for this would itself be a purpose-limitation violation.

**Status: decided.** This is squarely a data-model/architecture call, and I'm making it rather than escalating it — MIDAS and ATELIER were right to flag the *existence* of the question, but "what scope, what recipient boundary, what retention" is exactly the kind of decision this role owns.

---

## 3. Crisis-support content mechanism

**Observed fact, found by actually checking rather than reusing the names ATELIER listed:** I re-verified the specific helplines named in the feature map instead of assuming they're still current, and the check justified the caution ATELIER already flagged:
- **KIRAN (1800-599-0019)** has conflicting public signals: older government releases mention it, one unrelated project's commit calls it discontinued, and the government's current mental-health-programme page lists Tele MANAS without mentioning KIRAN. Neither a stranger's commit nor absence from a page confirms shutdown. Its present operator status is unresolved, so do not hardcode it into a crisis screen without direct operator verification.
- **Tele MANAS — 14416**, the Ministry of Health's current national helpline (24/7, 20+ languages, at `telemanas.mohfw.gov.in`), appears to be the operative government successor and is the more defensible anchor listing today.
- **Vandrevala Foundation's current number is +91 9999 666 555** (24/7, call + WhatsApp), confirmed directly from their own contact page — notably *different* from the number commonly cited in older write-ups, which is itself a small live demonstration of why this can't be a copy-pasted list.
- **iCall is 10 AM–8 PM, Monday–Saturday, not 24/7** — including it on a screen that implies always-available help without stating its hours would be a real, specific harm (someone reaching out at 2 AM to a line that isn't staffed), not a formatting nitpick.

**Proposal — mechanism, not just "someone should own this":**
1. **A small, versioned config served from the backend** (`{ helplines: [{name, phone, hours, mode}], last_reviewed_at, reviewed_by }`) fetched at runtime — not compiled into the Flutter app binary as a literal string, because a build-baked helpline number can only be corrected by an app-store release cycle, which is the exact failure mode that produced the KIRAN evidence above.
2. **A small bundled fallback snapshot inside the app binary**, used only when the runtime fetch fails (offline, backend down) — because "the crisis link shows nothing because the network hiccuped" is worse than a possibly-slightly-stale fallback. This is a reliability requirement, not a nice-to-have: the crisis-support link is explicitly the one place in this app where "weak network" is part of the core path, not an edge case.
3. **Ownership: whoever at Cult.fit owns trust & safety / compliance review** (the same function that would own MIDAS's regulatory posture), not engineering, and not "whoever's free" — with a mandatory review cadence (proposal: quarterly) that writes `last_reviewed_at`/`reviewed_by`, so staleness is an auditable fact, not an assumption. Engineering's job is making that config easy to update without a release, not deciding what it says.
4. **Content call:** lead with Tele MANAS (14416) as the anchor, since it's the most robust against exactly this kind of drift; include Vandrevala Foundation with its verified current number; include iCall only with its actual hours stated, not omitted. This list still needs Cult.fit's own compliance sign-off before ship — I'm proposing the mechanism and a defensible starting list, not certifying it as final.

**Status: proposed mechanism and starting content, with the config-vs-hardcoded architecture decided; final helpline list needs Cult.fit compliance sign-off, not just my verification.**

---

## 4. Consent-toggle-off semantics (DPDP)

**Correction from the primary statute:** the earlier reading of §12 alone was incomplete. The [official DPDP Act text](https://www.meity.gov.in/static/uploads/2024/02/Digital-Personal-Data-Protection-Act-2023.pdf) gives withdrawal rights and cessation duties in §6(4)–(6), requires erasure on withdrawal or when the purpose ends in §8(7) unless retention is necessary for compliance with law, and also provides an explicit erasure-request route in §12(3). The earlier claim that withdrawal never triggers erasure was wrong. Application, exceptions, commencement, and cross-system scope need current counsel review.

**Proposed product contract:** turning fitness cross-sharing off records a server-confirmed withdrawal, stops new processing for that purpose, and starts an auditable assessment and erasure workflow for data held solely on that consent. Show **Pending**, **Stopped and deletion complete**, or a specific lawful retention reason; do not say “deleted everywhere” before recipients and processors confirm. Keep an accessible separate data-request route as well, because a person may seek erasure or correction without using this toggle. The exact copy depends on the implemented workflow and legal review.

**Status: design direction, legal clearance open.** This is a build requirement, not a claim that the annotated screens store data or implement the DPDP workflow.

---

## 5. Architecture: the Faye feature set as a Flutter module

**The proposed architecture is a Faye route/module inside Cult.fit's Aurora app, with booking, payment, and account integration to verify against real systems.** Aurora's published Flutter migration explains the glassmorphism performance context (`brief/research.md`); it does not establish current service interfaces. The static `design/screens.html` illustrates cards, chips, navigation, and colours at the design-token level, not a production component library.

### Client-state only (no new service required)
- Onboarding step-dots, in-flow toggle visual state *before* submission, the two-step mood-pick-then-confirm interaction, the mascot's reaction copy (a pure lookup keyed by which mood was picked), and the offline-queued-log banner's own visibility. All of this is ephemeral UI state that either gets submitted to a service or discarded — none of it is data of record.
- **Important boundary:** client state renders the *mood log queued offline* banner, but the mood log itself is not client-state once it's meant to feed the dashboard trend and the adaptive-suggestion logic (HERMES §4) — that needs a service, covered below. The client owns the *queuing UX*, not the *data*.

### Needs an existing service, extended — not a new one
- **Booking + payment (therapist discovery, booking confirmation, My Sessions, credit-pack/billing):** Cult.fit already has a class/session booking and payment pipeline for fitness classes. This extends it to 1:1 therapist slots and a credit-ledger concept instead of building parallel infrastructure. The credit balance specifically **must** live server-side — a client-held credit count is a trivial tamper/double-spend surface, not an architecture choice.
- **Consent state (the DPDP toggle, and any future consent event like the therapist-switch note):** this is the single most important "must be a service, not a client flag" call in the whole map. The Act's §6(10) places a proof burden on the data fiduciary where consent is questioned; withdrawal and erasure also need enforceable records. A client-local boolean cannot do that — every consent toggle needs a server-recorded event: `{purpose, scope, recipient, granted|withdrawn, timestamp, consent_copy_version}` and a linked deletion/retention outcome. This is backend work regardless of how polished the client UI is.
- **Mood log + trend + adaptive suggestion:** needs a data store keyed to the user, tagged with the consent scope under which each entry was logged (so a later toggle change can't accidentally make old entries look like they were shared when they weren't, or vice versa). The "one adaptive suggestion" logic (HERMES §4) is a modest rules/lookup service, not a new ML system — nothing here justifies a new model-serving layer for a hackathon-scope feature.
- **Therapist-switch carry-forward note:** needs real, scoped access control (§2 above) — this is an authorization rule ("this note is readable by therapist X, for this switch event, until this boundary"), which has to live server-side; a client-side permission check is not a permission check.
- **Crisis-support config:** needs the small versioned config endpoint from §3, plus a CDN/cache layer so it's cheap and fast — not a full CMS platform, a lightweight config service is enough.

### Deliberately NOT specified here, and why
- No new database technology choice, deployment topology, or infra provisioning — Cult.fit already runs services for booking/payments/accounts; this reuses them. Naming a specific DB engine or hosting setup would be inventing infrastructure that doesn't change what ships.
- No therapist-matching algorithm, no RCI-credential-verification pipeline design — those are vetting/ops processes (MIDAS §5's "vetting/curation layer" cost), not a client/service architecture question this pass needs to resolve.
- No chat/messaging infrastructure — ATELIER already rejected therapist messaging on regulatory grounds; building the infrastructure for a feature that was correctly refused would be exactly the "unjustified dependency" this role refuses.
- No payment-gateway contract/MID negotiation detail beyond what §1 already scopes as blocked — that's a business/ops action item, not a software architecture decision.

This is a hackathon/concept-pass architecture statement, not a production engineering spec: the real claim here is narrower and more useful than "you'd need a backend" — it's *which three existing services* (booking/payment, account/consent, content-config) this extends, and which one new cross-cutting concern (a real, server-recorded consent-event model) doesn't yet exist in Cult.fit's fitness-only product and has to be built once, correctly, because DPDP compliance depends on it existing at all.

---

*Prepared by Lego (technical architecture / compliance / accessibility) against `01-MIDAS-business-model.md`, `02-HERMES-offer-and-persona.md`, and `03-ATELIER-feature-map.md`. Accessibility findings for the onboarding screens are in `brief/CONTRAST-AUDIT.md`'s "Onboarding addenda" section, not duplicated here.*
