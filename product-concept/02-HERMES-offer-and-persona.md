# HERMES — offer, persona, and copy for the Faye tab

**Scope note:** builds on `01-MIDAS-business-model.md` and the locked product rules in `CLAUDE.md`. The commercial pilot focuses on existing Cult.fit members because in-app distribution is available; the design brief's primary audience remains first-time therapy seekers. Ananya is deliberately **both**: an existing member and a first-time seeker. This intersection is a pilot hypothesis, not a redefinition of the wider userbase. The later MIDAS correction supersedes references below to monthly free “triage” and fixed credit packs: mood logging is repeatable and free; sessions start as pay-per-session; packs require a test.

---

## 1. The persona

**Audience distinction.** The hackathon IA must also work for a first-time seeker who is new to Cult.fit: she needs clear therapist credentials, a plain booking price, an explanation of what happens after confirming, and privacy controls without membership jargon. The existing member cross-shopping from fitness recognizes Cult.fit's booking pattern but must not assume workout data and Faye data are combined. Offer a familiar booking layout and explicit separation of data. The two can use the same four locked screens; copy and the first-run explanation carry the difference. Neither should be pushed into therapy by a low mood.

**Ananya, 24. Marketing exec at a D2C startup in Bangalore. Renting with two flatmates. Eight months into a Cult.fit membership, three workouts a week, pays for it herself.**

Not "urban millennials." Specifically her, because the specifics are what make the copy work:

- She has never sat across from a therapist. She has, however, googled "why do I feel like this all the time" at 1am more than once.
- Her fear isn't that therapy doesn't work. It's three narrower, more concrete fears: (1) her parents finding a session on a shared family card or asking why she's "not fine," (2) picking the wrong therapist and having to explain everything again from scratch to someone else, (3) not being "sick enough" to deserve a therapist's time, therapy still coded in her circle as something for people in crisis, not people who are just tired and wound tight.
- She knows Cult.fit's booking and fitness interface, but has not yet decided whether to trust it with therapy-related information. Familiar navigation lowers learning effort; a clear privacy model, honest provider details, and reliable service must earn the new kind of trust.

### Schwartz stage, the actual call

Most write-ups of Indian first-time therapy seekers default to "problem-aware, solution-unaware" (per the standard 5-stage model: unaware → problem-aware → solution-aware → product-aware → most-aware ([Selzee, Schwartz's 5 Levels](https://selzee.com/eugene-schwartz-5-levels-of-awareness))). That's wrong for Ananya specifically, and getting this wrong would misdirect the copy toward educating her that therapy exists, which she already knows and would find condescending.

**The actual call: she is problem-aware and solution-aware, but not product-aware, and specifically un-activated by stigma and trust deficit rather than by ignorance.** She knows what therapy is. She has probably recommended it to a friend. What she has never done is picked a specific therapist through a specific platform and clicked confirm. The blocker isn't "does this solution exist," it's "can I trust this particular door into it, quietly, without the wrong person finding out."

**Market sophistication for online therapy in India specifically: low-to-medium, not saturated.** Unlike the US market Schwartz's own examples come from, Indian consumers haven't been marketed at by a dozen competing therapy platforms making increasingly wild claims — Practo, YourDOST, and Wysa exist but none has the cultural penetration of, say, BetterHelp in the US. That matters for angle selection: a saturated market forces a "new mechanism" angle (some novel claim competitors haven't made) because audiences are numb to plain claims. A low-sophistication market doesn't need that escalation — a plain, specific, credible claim still lands. What Ananya IS jaded by is generic wellness-app cheer ("you've got this! 🎉") and stigma-loaded language, not by therapy-marketing claims specifically.

**The angle this implies: identification, not mechanism.** Not "here's our unique 7-step method" (a mechanism angle, wasted on a low-sophistication market and actively wrong for a regulated, non-diagnostic product that legally cannot claim clinical differentiation per MIDAS §5). Instead: "this is the same place you already trust, now for this too" — an identification/permission angle that transfers existing brand trust onto a new, higher-stakes category. That's the thread running through the copy in §5.

---

## 2. The offer, run through the Hormozi Value Equation

Value = (Dream Outcome × Perceived Likelihood of Achievement) ÷ (Time Delay × Effort & Sacrifice). Showing the work separately for the **free, non-clinical check-in** and the **paid session**, because collapsing them into one number hides where the offer is actually strong.

### Free layer: the mood check-in (the real "offer" this copy has to sell)

- **Dream outcome:** not "cured." Regulatory reality (MIDAS §5: counselors cannot diagnose, and copy must never imply otherwise) rules out promising a clinical outcome anyway, which is a constraint, not a weakness. The honest, sellable dream outcome for a first-timer is smaller and more true: *feel steadier today, without having to explain herself to anyone, without it going on record as "something wrong with her."* That's an achievable, specific promise, not an inflated one.
- **Perceived likelihood ↑:** familiar booking patterns may reduce friction, while privacy and provider quality still need proof. Show credentials, price, cancellation terms, and data boundaries. The unsupported "recommended by members like you" line was removed from the current screens.
- **Time delay ↓:** this is the layer's entire job. Zero wait, zero form, one tap, today. The free check-in is structurally the time-delay-killer for the whole funnel: it lets her get *some* value the same day she notices the tab, without committing to the multi-week, real-cost thing (an actual session) that still has genuine time delay baked into it.
- **Effort & sacrifice ↓:** chip-tap, not a form (screen-flow.md's existing pattern reused). No numeric self-rating (already locked, and it also lowers psychological effort, not just UI friction, since a number invites self-judgment). No cost. No visible record anywhere else in the app unless she opts in.

**Verdict: this passes the equation cleanly, deliberately, because it's designed to be nearly frictionless and nearly risk-free.** That's the point. It should not be trying to sell the paid session directly. Its only job is to be an offer so easy to say yes to that saying yes becomes the on-ramp.

### Paid layer: the actual session (single-session pilot)

- **Dream outcome:** same honest ceiling as above, now with an actual professional attached, which raises it somewhat but not to "life-changing" (overclaiming here is the exact liability MIDAS §5 flags).
- **Perceived likelihood ↑:** credential verification shown quietly (reusing the existing trainer-verification visual language, per screen-flow.md), not a star rating. A first-time buyer trusts a visible credential more than a crowd-sourced score for something this personal, this is also why BetterHelp and comparable platforms lead with matching/credentials, not reviews.
- **Time delay ↓, but honestly, not artificially:** same-day/this-week availability as a filter chip (already spec'd), which is a real lever, not a fake urgency trick.
- **Effort & sacrifice ↓, but this is the layer where MIDAS's structural constraint actually bites:** real money, a real calendar commitment, and a 1:1 session cost (MIDAS §1). Copy cannot remove that cost. It can show the actual price and cancellation terms before payment, explain who sees the booking, and avoid implying an ongoing commitment. The illustrative ₹1,200 is not a launch price; a discounted four-session pack is a later test.

**Verdict: this offer is not, and should not try to be, a screaming yes on its own.** It becomes a yes because the free layer already did the trust-building and habit-forming work first (see §4, §6). Trying to make the paid session itself irresistible through copy alone, without that on-ramp, would mean either overclaiming (a compliance and trust problem) or discounting hard (a margin problem MIDAS already flagged as thin). The correct place to spend persuasive effort is the free layer and the loop that follows it, not a harder sales pitch on session one.

---

## 3. Name verdict: "Faye" (supersedes the earlier "Mind" verdict below)

**Revision, 26 Sep 2026:** the original verdict in this section (preserved further down for the record) tested "Mind" against Rule 4 and correctly flagged it as inert and generic — "could belong to Headspace, Calm, or any wellness competitor without anyone noticing the swap" — but then recommended keeping it anyway, purely for nav-bar scannability. Love overrode that call directly: a flat category noun borrowed from every competitor's IA is not a brand, tab-label convenience or not. "Faye" was chosen specifically because it passes the test "Mind" failed — it is not interchangeable with a Headspace/Calm/Wysa nav item, it reads as a name (not a category), and it gives HERMES's persuasion work in §4 an actual proper noun to write around ("Faye" can open a sentence, invite, have a voice — "Mind" could only ever label a shelf).

- **As a nav-bar tab label, "Faye" still scans fine.** Its siblings are "Fitness," "Transform," "Profile" — flat category nouns — but a single first-name-style word is exactly as fast to scan in a five-item bottom nav as a category noun is; short proper nouns are common in real product navigation (a person's own name, a pet, a mascot) and don't need to be evocative to be legible in under a second. The original worry (an evocative tab label would "stick out") doesn't actually apply to a plain short name — it applies to a slogan-length label, which "Faye" isn't.
- **The name still does double duty**, same as the original analysis wanted "Mind" to: it's the nav label *and* it's now also the thing booking-flow copy, push copy, and content-card bylines can write around directly ("Faye suggests," "a note from Faye") instead of needing a second in-tab product name layered on top. That collapses the "tab label vs. persuasive offer name" split the original verdict proposed — one name now does both jobs, because unlike "Mind" it's actually capable of the second one.
- **Open, not closed:** "Faye" has not been tested with first-time seekers or existing members any more than "Mind" was. Test comprehension, trust, and tone before it reaches production copy. Until then, say "therapy session" in transactional steps, same guardrail as before.

<details>
<summary>Original verdict (superseded, kept for the record — argued to keep "Mind")</summary>

Rule 4: a name is doing marketing work or it's doing nothing. Testing "Mind" against that bar honestly, it fails as a persuasive name — it's inert, generic, and could belong to Headspace, Calm, or any wellness competitor without anyone noticing the swap. It carried zero of the specific promise this section needs to make (privacy, ease, "you don't have to be in crisis to be here").

The actual call was framed as a split, not a flat rename, because "Mind" was doing a different job than a persuasive name is supposed to do: as a nav-bar tab label it was argued to be correct and worth keeping (flat, one-word, low-drama, matching "Fitness"/"Transform"/"Profile"), while the name Rule 4 was really pointing at was framed as the product/offer *inside* the tab, not the tab label itself. Love's call above rejects the premise that a nav label gets a pass from being a brand — see the revision note.

</details>

---

## 4. The non-gamified habit loop: what brings her back after session one

The brief's hardest constraint: no streaks, no badges, no points, even though that's the default retention playbook and even though Cult.fit uses exactly that playbook everywhere else in the app. Building the loop from actual research on what else works, not a guess:

- Streaks and badges are the most commonly deployed mechanic across mental-health apps (progress levels appeared in 10 of the apps surveyed, unlockable rewards in 9, badges in 7), but the same research is explicit that they underperform long-term and that "meaningful design matters more than quantity of techniques" ([Cambridge Core, *Gamification and Nudging Techniques for Improving User Engagement in Mental Health and Well-Being Apps*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EB2BEF667BFAE42422FE27C04FA2B0A3/S2732527X21004260a.pdf/gamification-and-nudging-techniques-for-improving-user-engagement-in-mental-health-and-wellbeing-apps.pdf)). A broader meta-analysis of gamification specifically in depression apps found effects on engagement were mixed and inconsistent across studies, not a reliable lever on its own ([JMIR Mental Health, *Examining the Effectiveness of Gamification in Mental Health Apps for Depression*](https://mental.jmir.org/2021/11/e32199)). The lock isn't just a brand-tone preference, it's backed by the evidence: gamification is the *weaker* option here, not the stronger option we're being asked to sacrifice.
- What the same research found actually works, without competition: a **narrative/character device** sustained daily engagement over 18 months through a simple plant-growing interaction loop, no leaderboard involved; **personalization that matches a suggestion to the emotional state just logged** (not a generic tip) drove higher session frequency in comparable apps; and **"non-forcible," autonomy-respecting nudge language literally doubled chatbot engagement** versus pushier phrasing (same Cambridge source). Separately, a systematic review of digital habit-formation design found that **prompts/cues (used in 80% of studies) and self-monitoring (60%) were the most applied and most durable techniques**, while virtual rewards showed limited sustained effect; the strongest emerging pattern was **context-aware, behavior-triggered cues rather than fixed-schedule reminders** ([PMC, *Digital Behavior Change Intervention Designs for Habit Formation: Systematic Review*](https://pmc.ncbi.nlm.nih.gov/articles/PMC11161714/)). Wysa's own positioning leans on the same idea in practice: it markets itself as judgment-free conversation ("Talking to Wysa is empathetic, helpful, and will never judge") rather than a scored, gamified tracker.

**The loop, built from those four findings, and named for what it actually asks her to do: Notice → Name → Nudge.**

1. **Notice** — make a check-in available when she opens Faye. Do not use a workout, app-open history, or notification to infer an appropriate moment without a separate, explicit choice to receive that kind of prompt. The mascot can invite reflection inside Faye without joining Fitness and Faye data.
2. **Name** — the one-tap mood-icon log already locked in `screen-flow.md` (no numeric score). This is the self-monitoring technique the habit-formation review found most durable, and it's already the lowest-effort action in the whole product.
3. **Nudge** — instead of a badge or a point, the payoff is the personalized-suggestion mechanism already spec'd for the mood dashboard (one adaptive suggestion, never a wall of them), delivered in the mascot's voice, phrased as an invitation rather than an instruction ("non-forcible" language, per the doubled-engagement finding above). That single line is the entire reward. No progress bar, no unlock animation.
4. **A user-controlled bridge to human help:** the locked screen flow permits one adaptive suggestion. A low mood trend does not establish that she needs a paid session. Any booking suggestion should be optional, plainly labeled, and tested for pressure and misunderstanding; it must not be framed as a clinical escalation. The user can always book directly without logging a mood. “Steady” remains an untested name.
5. **Quiet trust layer:** show credential scope, language, price, and availability on therapist profiles. Keep resources organised by stated concern and duration. Do not claim other members like her used a therapist or resource unless there is a verified, consent-respecting basis for that claim; the current submission removes that unsupported line.

---

## 5. Onboarding copy: first-run sequence, ready to hand to ATELIER

This is proposed production copy for a service with real consent and storage controls. The current submission is an annotated screen flow with no live consent, mood storage, or booking backend. Keep production promises separate from screen concepts until the controls actually exist.

Three screens. Existing Cult.fit member, first time opening the Faye tab. Every line under 15 words, zero em dashes, written to the identification angle from §1 (same place you trust, now for this too), not an education angle (she doesn't need therapy explained to her) and not a hype angle (she's tired of wellness-app cheer).

### Screen 1 — Entry (the trust-transfer moment)

- **Headline:** Same Cult.fit. A quieter room inside it.
- **Subhead:** Faye is for what workouts cannot fix. No forms, no diagnosis, just support.
- **CTA:** Step in

### Screen 2 — Privacy and consent (carries the actual DPDP purpose-limitation requirement)

- **Headline:** Your check-ins stay private by default.
- **Subhead:** We use this only to support you here. Nothing crosses over without your yes.
- **Toggle (off by default, separate and explicit, per DPDP purpose limitation):** Also use this to shape my fitness recommendations
- **Helper line under toggle:** Off unless you turn it on. Change it anytime.
- **CTA:** Continue privately

### Screen 3 — Activation (the first meaningful action, per §6)

- **Headline:** How are you, really, today?
- **Subhead:** Pick what fits. No score, no judgment, ten seconds tops.
- **[Row of expressive mood icons, no numeric scale, per locked product rule]**
- **CTA:** Log today

Notes for ATELIER: screen 1 is the moment the theme-shift (warm gradient mesh, per `design/DIRECTION.md`) should visually land, it's doing the same "different register, same app" job the copy is doing. Screen 2 needs the toggle to read as genuinely optional, not a dark-patterned pre-checked box, this is a compliance requirement (DPDP), not a design preference. Screen 3 is where the mascot should first appear responding to her tap, since that response is the first beat of the Notice → Name → Nudge loop in §4, not a separate, disconnected onboarding moment.

---

## 6. The funnel

- **Awareness — mechanism: the existing nav item, seen once, not sold.** No separate acquisition spend, no ad, per MIDAS §4's growth call (retention/upsell, not an acquisition wedge). The only "awareness" device is a single, one-time discovery indicator on the Faye tab icon the first time it ships (a plain "new" dot, not a recurring badge/counter, which would cross into the locked no-gamification rule). It disappears the first time she taps it and never reappears.
- **Activation — mechanism: the first meaningful choice.** She can explore therapists or try the optional check-in. A mood entry is not required before booking, and a booked session is not required to count an exploratory first visit. Measure the two paths separately rather than forcing everyone through one funnel.
- **Retention — mechanism: useful repeatable check-ins and easy return to an upcoming session.** Keep suggestions inside Faye by default; any behavior-triggered notification needs separate opt-in and a discreet preview. Measure whether users voluntarily find value, not whether prompts increase opens. Booking remains user initiated, never an algorithmic conclusion from mood history.

---

## 7. Existing member already in therapy elsewhere

The follow-up stress test identified a second member situation distinct from Ananya: someone already using therapy through another provider or platform. That person understands the category but may be comparing options after a move, schedule change, or other self-chosen reason. Familiar Cult.fit navigation is helpful, but it is not a reason to disrupt a working therapeutic relationship.

For this group, keep the same discovery and booking structure. Explain credentials, mode, price, and availability plainly. An optional “Already seeing someone?” path can explain what a first conversation with a new provider involves. If the person chooses to move, a private prep or carry-forward note is user-authored, recipient-specific, previewed, and never shared automatically. This is a concept to test, not a new required hackathon screen or a claim that switching is beneficial.

*Prepared as a concept exploration. The persona, naming, and copy need comprehension testing before production use; the locked hackathon screens remain governed by `brief/` and `CLAUDE.md`.*
