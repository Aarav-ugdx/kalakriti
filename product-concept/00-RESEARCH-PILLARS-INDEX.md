# Research pillars index — how this concept actually fits together

**What this is, and isn't.** Not a table of contents — `product-concept/01–04` and `brief/` already say what each doc contains, and re-summarizing them here would just be a worse copy. This traces the actual dependency graph: which pillar's finding forced, changed, or gated another pillar's conclusion, where two pillars are in live tension that hasn't been closed, and what genuinely follows from all of it as a risk register. Where a doc grades its own confidence (MIDAS's 🟢/🟡/🟠), that grade is carried forward here rather than flattened into "the research says."

**Scope reminder:** `brief/` + the annotated `design/screens.html` and PNGs are the graded Round 1/2 hackathon submission. Their scenario, four-screen order, brand direction, and five decisions in `CLAUDE.md` remain locked. An experimental clickable prototype was archived so it cannot be mistaken for part of this submission. `product-concept/01–07` extends the idea into a fuller service concept and is not itself the graded deliverable. Several risks below are build-phase gates rather than Round 1 blockers. `design/BRAND-AND-EXPERIENCE.md` and `design/UI-UX-IMPROVEMENT-PLAN.md` are planning only.

---

## Pillar 1 — Market & regulatory reality

**Sources:** `brief/research.md` (Cult.fit brand/market baseline), `product-concept/01-MIDAS-business-model.md` §5 including its 2026-09-26 regulatory verification pass, `product-concept/03-ATELIER-feature-map.md` (rejections built on this pillar), `product-concept/04-Lego-technical-and-compliance.md` §4.

**Settled vs. asserted:**
- Researched, not cleared: provider qualification, documentation, and platform duties differ across psychiatrists, clinical psychologists, and counsellors. MIDAS cites primary guidance for the RMP/telepsychiatry track; its non-medical professional analysis relies partly on secondary commentary. Both need current legal and provider review before a live pilot.
- Corrected, not just verified: MIDAS's own earlier claim that DPDP creates a "stricter" regime for health data specifically was checked and found **wrong** — DPDP 2023 has no elevated "sensitive data" category the way GDPR or India's old SPDI Rules did. It runs ordinary consent + breach-notification rules for all personal data. The doc caught and corrected its own overclaim rather than letting it stand.
- Asserted/order-of-magnitude, 🟠: Cult.fit's actual member base size and blended ARPU (no published numbers available).

**What this gates downstream:**
- **ATELIER's rejection of inter-session therapist messaging** rests on unbuilt coverage, response-time, documentation, and provider-workload rules. Its legal implications need counsel rather than a blanket claim that a professional category has no record-keeping duty.
- **ATELIER's crisis-support "never auto-escalate from mood data" refusal** is gated by the same "counselors cannot diagnose" fact — algorithmically inferring risk from mood logs would mean the product making a clinical judgment call it has no license to make.
- **HERMES's angle selection** ("identification, not mechanism," §1) is gated by the same regulatory read: a mechanism-style claim ("our unique method works better") would imply exactly the clinical differentiation a non-diagnostic product legally cannot claim.
- **Lego's consent-event architecture** (§5) exists *because* of the DPDP purpose-limitation finding here, not as a generic "good practice" choice.

**Unresolved gate:** legal and provider-operating clearance has not happened. The concept can inform a hackathon presentation; it cannot stand in for approval to offer care.

---

## Pillar 2 — Unit economics & business viability

**Sources:** `product-concept/01-MIDAS-business-model.md` (whole document).

**Settled vs. asserted:** the service uses individual provider time, unlike a shared-capacity class. The ₹1,200 price, 25% take rate, member base, conversion, and ~12–17% contribution are scenario inputs, not Cult.fit measurements. BetterHelp subscription price and reported provider pay cannot establish a comparable marketplace take rate. MIDAS now shows its illustrative multiplication rather than presenting a national user forecast.

**Current verdict:** there is no demonstrated business case yet. A consumer marketplace inside existing membership is the first pilot hypothesis; employer distribution is a separate hypothesis because [Cult.fit already markets corporate wellness that mentions therapy](https://business.cult.fit/organizations/corpsupport). Neither route has measured provider economics, demand, or privacy terms for this flow. Provider/legal clearance precedes a live pilot; attended sessions and actual contribution determine scale.

**What this gates downstream:**
- **MIDAS §2's revised pricing call** keeps optional repeatable mood logging and selected resources free, starts with a clearly priced single session, and treats credit packs as a later test rather than a fixed input.
- **MIDAS §4's distribution call** starts with existing members; it does not rule out other channels without testing. HERMES's first-run design now allows either therapist exploration or a check-in, so the free log is not a booking gate.
- **MIDAS risk #2 (therapist supply liquidity)** is the reason ATELIER's therapist-profile "hardest state" (§1) treats "no availability" as a first-class, expected state rather than an edge case — the honest "Fully booked for now" + passive notify pattern is the *design-layer* acknowledgment of a business-layer constraint MIDAS names but can't solve with design.

**Open tension:** HERMES, ATELIER, and Lego produced useful concept work before legal and economic gates cleared. Keep that work as hypotheses. Do not treat the dependency order of the documents as evidence that a real service is feasible.

---

## Pillar 3 — Persona & positioning

**Sources:** `product-concept/02-HERMES-offer-and-persona.md` (whole document).

**Settled vs. asserted:** the Schwartz-stage call (problem-aware + solution-aware, *not* product-aware; blocked by stigma/trust, not ignorance) is a reasoned judgment call against a named persona, not a measured fact — HERMES argues it explicitly rather than defaulting to the generic write-up, which is the right posture for something inherently a judgment call. The Hormozi Value Equation breakdown is a structured argument, not a data point, and it's honest about where it's weakest: the paid-session layer is explicitly *not* claimed to be a strong yes on its own (§2), which is a rarer kind of honesty than most positioning docs allow themselves.

The one item explicitly flagged as an **untested bet**, in HERMES's own words: the "Steady" product name (§3). HERMES is clear this needs real user-testing before ship, not that it's already validated.

**What this gates downstream, and where the untested bet already leaked forward:**
- HERMES §2's free check-in/paid human-session split informs **ATELIER's core path**. The My Sessions record is a service-continuity need; the credit pack remains a later packaging experiment.
- HERMES's persona fear #1 (parents finding a session on a shared card) is the *specific, named* reason ATELIER's credit-pack screen (§3) makes a concrete statement-descriptor commitment, not decorative copy — traceable line: persona fear → feature requirement → (see Pillar 5) an unresolved technical dependency.
- HERMES's persona fear #2 (re-explaining to a new therapist) is the *specific, named* reason ATELIER builds the therapist-switch carry-forward flow (§6) at all.
- **The "Steady" name remains untested.** Earlier drafts propagated it as settled; the updated HERMES document restores it to a candidate and uses “therapy session” for transactional copy until comprehension testing.

---

## Pillar 4 — Product & interaction design

**Sources:** `brief/screen-flow.md`, `CLAUDE.md` locked decisions 3–5, `product-concept/03-ATELIER-feature-map.md` (whole document).

**Settled vs. asserted:** no therapist star ratings, numeric mood scores, or Faye streaks are locked in `CLAUDE.md`. The case against gamification is supported by cited research but still needs caution about generalising across products and populations. The current screens express the lock through one optional suggestion, clear duration, and quiet trust signals.

The revised **Notice → Name → Nudge** idea starts when the user opens Faye: optional icon logging and one small suggestion from a stated concern or preference. Behavior-triggered notifications and Fitness/Faye data joins are deferred until explicit opt-in and privacy testing. A user can reach therapist discovery directly.

**What this gates downstream:**
- ATELIER's crisis-support item (§4) stays visible and unchanged by mood logs. Sparse entries do not trigger crisis inference or a paid-session upsell. Booking and help remain user-accessible through separate ordinary routes.
- ATELIER's own rejections (peer community, referral/sharing, general content library, denser analytics dashboard, notification-preferences screen) are each traced to a *named* constraint — Pillar 1's regulatory read, the persona's exposure fear, or the locked no-gamification rule — not to generic "keep it simple" instinct. Worth noting since the task brief asks whether rejections are genuinely justified: they are, and each one cites which upstream fact justifies it, rather than asserting good taste.

**Boundary to validate:** a suggestion based on a user's explicit concern can remain a lightweight content choice. A mood trend should not be converted into a clinical assessment, crisis inference, or sales trigger. The always-visible help link is a separate path. Test this distinction with users and providers before personalization.

---

## Pillar 5 — Technical architecture & compliance

**Sources:** `product-concept/04-Lego-technical-and-compliance.md` (whole document).

**Settled vs. asserted, kept separate on Lego's own terms (it labels observed fact / inference / proposal explicitly, which is worth preserving rather than flattening):**
- **Corrected after a primary-law check:** reading DPDP §12 alone missed §8(7), which provides for erasure on withdrawal unless legal retention is necessary. §6 covers withdrawal/cessation and §12 also offers a separate erasure-request route. A production toggle needs a server-confirmed stop-and-erasure workflow plus an independent data-request route, with counsel reviewing exceptions, commencement, and recipient scope. See Lego §4 and the [official Act](https://www.meity.gov.in/static/uploads/2024/02/Digital-Personal-Data-Protection-Act-2023.pdf).
- **Decided, not blocked:** the therapist-switch carry-forward consent scope (§2) — Lego makes the call rather than escalating it further: structured tags need per-switch opt-in consent (confirming ATELIER's instinct was correct, not just cautious); the free-text note needs a scoped, time-bounded recipient grant (90 days or first session, whichever is sooner) because no clinician record-keeping duty exists to justify indefinite retention.
- **Proposed mechanism, content still pending sign-off:** crisis-support config (§3). The illustrative list needed checking: KIRAN's current status remains unclear, an older Vandrevala number was stale, and iCall must show its hours. A maintained, reviewed source with an offline fallback is preferable to hardcoded claims. Final operator, number, hours, and language availability require owner verification before release.
- **Blocked, correctly stated as blocked rather than assumed away:** the payment statement-descriptor claim (§1). This is the strongest concrete unresolved dependency chain in the entire concept — see Pillar 3 above for where it starts, and the risk register below for why it matters.

**What this gates or corrects downstream:** Lego's consent-event model (`{purpose, scope, recipient, granted|withdrawn, timestamp, consent_copy_version}`, §5) is a required new capability for the concept. Booking, payment, account, provider access, and deletion integration must be checked against Cult.fit's actual systems; this document does not verify that they can simply be reused.

---

## Pillar 6 — Accessibility

**Sources:** `brief/CONTRAST-AUDIT.md` (both the original pass and the 2026-09-26 onboarding addendum).

**Settled vs. asserted:** everything here is measured, not asserted — that's the whole point of the document existing (screen-flow.md's checklist had claimed accessibility properties without computing them). Two real WCAG failures in the original six-screen pass (CTA button text, therapist-badge text, both from brand coral being too mid-tone for text-on-fill use) were found and fixed with a new `--coral-deep` token, scoped only to the two failing text uses, with the dark-frame Fitness screen's original coral deliberately left alone (already passing, brand-fidelity preserved).

**What actually connects this pillar to the others, not just alongside them:**
- The onboarding addendum's most important finding is a **direct hit on Pillar 5's compliance work**: the DPDP consent toggle (`onb2`) — the same toggle Lego's architecture section says must be backed by a server-recorded, provable consent event — was found to render at **1.01:1 contrast in its default (off) state**, effectively invisible, on what the audit itself calls "the single most legally load-bearing screen in the flow." An invisible consent control undermines the *meaningfulness* of consent as much as a missing server record would — this is accessibility and legal-compliance work converging on the same screen, not two unrelated checklists. It was caught and fixed (track/border changed to a visible neutral tone, re-verified post-fix).
- Same addendum, same method, caught two more real failures on the onboarding sequence (consent-error banner text at 3.57:1, inactive step-dots at 1.37–1.40:1) — both fixed the same way as the original audit's root-cause pattern: a translucent light fill on an already-light background reads far closer to white-on-white than its CSS alpha suggests, and raising the tint's opacity was tried and made contrast *worse*, not better, both times. That repeated, named failure mode across two audit passes is itself a real finding worth keeping visible, not just the final numbers.
- **Follow-up fix:** the onboarding mood radiogroup now has one Tab stop, arrow-key selection, and focus transfer after the check-in preview. A fresh Chromium check verified the behavior; the original audit records both the finding and the repair.

---

## Consolidated risk register

Each item: what it is, which pillar owns resolving it, and whether it blocks anything actually graded (Round 1 — already submitted and locked; Round 2 — the shortlist presentation, if it happens) or is a build-phase/Round-2-prep item only, since `product-concept/` itself is explicitly outside the graded deliverable.

| # | Risk | Owner | Severity |
|---|---|---|---|
| 1 | **Payment statement-descriptor claim is unconfirmed for card and netbanking rails** — ATELIER's credit-pack screen states a specific claim ("This will show as CULTFIT WELLNESS...") built directly on HERMES's named persona fear #1, but Lego's own investigation found no gateway documentation guarantees that exact string across every rail, and flags it explicitly as blocked pending Cult.fit's payments/finance team + real sandbox verification per rail. This is the single most concrete unresolved dependency chain in the whole concept: a persona fear → a specific screen commitment → a technical claim that cannot currently be verified as written. | Lego (verification) / Cult.fit payments team (sandbox + MID decision) | **Build-phase only.** Doesn't touch Round 1 or Round 2 — the graded deliverable never claims this screen exists. Blocks this *specific feature* from shipping as literally copy'd if this concept moves toward a real build. |
| 2 | **"Steady" is an untested naming bet that has already been treated as settled two documents later.** HERMES names it explicitly as needing real user-testing before ship; ATELIER and Lego both use it as a working product name without re-raising that flag. | HERMES (owns the test), everyone downstream (should keep flagging it as provisional in any future doc) | **Round-2-presentation-relevant, not blocking.** Fine to present as a proposed name; would be a real gap if presented as decided. |
| 3 | **Future interactive accessibility:** an archived onboarding prototype repaired mood-radio Tab and arrow-key behavior, but the submitted screen flow is static. | Design/Lego | Carry the tested keyboard pattern into any later interactive build; verify it again in the actual product. |
| 4 | **MIDAS's "doesn't work yet" verdict rests on 🟡/🟠 assumptions, and the recommended sequencing (legal clearance → pilot → confirmed economics, in that order) was not actually followed** — HERMES/ATELIER/Lego were all built on top of those assumptions as fixed inputs before any of the three prerequisite steps happened. | MIDAS / founder (decides whether to gate further work on this) | **Build-phase only; not a hackathon blocker** (Round 2 judges concept and design quality, not proven unit economics) — but the largest real risk if this concept is ever treated as an actual business decision rather than a design exercise. |
| 5 | **Provider qualification and telehealth duties need qualified review.** Requirements differ by professional category, and the current source set does not establish a complete licensing or operating rule for this proposed service. A documented credential check, scope-of-practice policy, referral boundary, and provider oversight process are unbuilt. | MIDAS/legal + clinical operations | **Build-phase release gate.** Review the provider model with Indian counsel and qualified clinicians. The separate decision to defer between-session messaging also reflects unbuilt coverage and response-time operations. |
| 6 | **Therapist supply liquidity** (scarce, credentialed labor pool vs. Cult.fit's abundant fitness-trainer pipeline) — ATELIER's "Fully booked for now" honest-state design acknowledges this at the UI layer but doesn't solve the underlying operational bottleneck. | MIDAS/Cult.fit ops | **Build-phase only.** |
| 7 | **Consent withdrawal and erasure workflow remains unbuilt.** Earlier docs wrongly said withdrawal does not trigger erasure because they read §12 without §8(7). The real build needs cessation, assessed erasure, lawful retention explanation, and a separate data-request path. | Legal/privacy + Lego + ATELIER | Build-phase release gate; the current annotated screens store no personal data. |
| 8 | **Crisis-helpline content needs maintained verification.** KIRAN's current status is not confirmed; older Vandrevala references were stale. A versioned config with a reviewed offline fallback is proposed, but neither the mechanism nor final list is built. | Lego (mechanism) / Cult.fit compliance (content sign-off) | Build-phase release gate, especially before any mockup displays actionable numbers. |
| 9 | **Therapist-switch free-text note retention policy (90 days or first session, whichever sooner) is Lego's proposal, not yet validated against Cult.fit's actual legal position or built.** | Lego / Cult.fit legal | **Build-phase only.** |
| 10 | **Minors are never addressed anywhere in `brief/` or `product-concept/`.** DPDP Act 2023 requires verifiable parental consent to process a minor's personal data, and Cult.fit almost certainly has under-18 members through family memberships and school-age fitness users. Nobody has decided whether Faye excludes under-18 Cult.fit members in v1, gates them behind parental consent, or ignores age entirely (the unsafe default). Cross-checked against an independent safety-research doc on a different product, which treats this as non-negotiable rather than optional. | MIDAS/legal + Cult.fit (a product-scope decision, not a design fix) | **Build-phase, but more consequential than most items above** — not a Round 1/2 blocker, but the single biggest unaddressed compliance gap if this ever becomes a real feature. |
| 11 | **Family/shared-membership account visibility is a related, second edge case nobody has modeled.** If Cult.fit sells family plans with a parent/admin account, it's undecided whether that admin view can see a dependent's Faye activity — the same discretion fear HERMES already named for persona fear #1 (a session showing on a shared card), but worse if an admin account has direct visibility rather than just a billing line. | ATELIER (account/permissions model) / MIDAS (membership structure) | **Build-phase only.** Same root cause as #10 — age and account structure were never modeled in the feature map. |


**Next decision:** validate the first-session prep card and privacy receipt before adding personalization. They solve the named user fears more directly than a behavior-triggered nudge, and they expose the data-access and provider-workflow questions that must be answered for a real service. See `06-PRODUCT-SPEC-AND-ROADMAP.md` and the ranked customer review in `07-CROSS-POLLINATION-AND-CONSUMER-REVIEW.md`.
