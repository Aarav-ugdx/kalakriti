# MIDAS — business model read on the Cult.fit mental-health pivot

**Scope note:** this is exploratory material for the fuller product concept, separate from the graded `brief/` and `design/` submission. The question is whether therapy booking could be contribution-positive inside an existing membership business. Every number below is graded 🟢 measured / 🟡 comparable-inferred / 🟠 asserted order-of-magnitude. No Cult.fit member count, therapy conversion, provider agreement, or margin is measured here; the model is a scenario, not a forecast.

**Correction, 2026-09-26:** §2's “one check-in / triage interaction per month” conflicts with the free daily mood log in the locked screen flow and HERMES's activation model. Mood logging and the weekly view should be free and repeatable. “Triage” implies clinical sorting and should not describe this feature. Human sessions remain paid. The 25% take rate, funnel size, and employer route are hypotheses. See `06-PRODUCT-SPEC-AND-ROADMAP.md`.

---

## 1. The number that matters, first

**Therapy is not a group fitness class — it has zero operating leverage, and that's the whole story.**

Cult.fit's core gym/class economics work because one trainer serves 15–30 members simultaneously in a shared physical space it already owns or leases — marginal cost per additional member in a class is close to zero once the class is running. 🟢 (structural fact about group fitness, not specific to Cult.fit)

Therapy is strictly 1:1. A 50-minute session is one therapist's time for one client, full stop — there is no shared-capacity version of this. Every session sold is a linear unit of COGS from session one, with no scale discount on the labor side. This kills the exact mechanism that makes the rest of Cult.fit's membership model profitable, and it's the reason this can't be priced or resourced like "one more class type."

### Unit economics — marketplace vs. employed-therapist

| | Marketplace / commission model | Employed-therapist model |
|---|---|---|
| Structure | Cult.fit lists vetted independent therapists, takes a cut per session | Cult.fit puts licensed therapists on payroll/retainer, like it could staff trainers |
| Fixed cost exposure | Low — no cost if no bookings | High — pays salary regardless of utilization |
| Demand-risk bearer | Therapist (variable income) | Cult.fit (fixed cost against unproven demand) |
| Precedent | Practo, Urban Company, most India telehealth marketplaces, BetterHelp's underlying network | Cult.fit's own gym trainers (works *because* of shared-class leverage above) |
| Quality/brand control | Harder — need vetting/curation layer | Easier — but only pays off at high, predictable utilization |

**Call: marketplace/commission model is the viable one, not employed-therapist.** 🟡 The employed model only makes sense once utilization is proven and predictable — exactly what a brand-new, unproven-demand feature inside a fitness app doesn't have. Cult.fit's own trainer-employment model is not a valid precedent here because it depends on shared-capacity economics that don't exist for 1:1 therapy.

### The actual margin math (illustrative, not measured)

- Consumer price per session: **₹1,200** 🟡 (mid-market for India online therapy — comparable platforms run roughly ₹800–2,000/session)
- Marketplace take rate: **25%** 🟠 as a Cult.fit scenario input, with no disclosed Indian comparable to calibrate it. BetterHelp's subscriber price and reported therapist pay do not give a clean marketplace take rate: subscription coverage, utilization, and non-session costs differ. Even simple price/pay arithmetic spans roughly **42–73%** when the endpoints are crossed, not the previously stated 50–68%. Do not use that range to validate Cult.fit's 25% assumption. Get provider quotes and actual settlement data.
- → Platform revenue/session ≈ **₹300**, therapist payout ≈ **₹900**
- Less payment processing, vetting/QA overhead, support, allocated tech/ops (~10% of session revenue, asserted): net contribution ≈ **₹150–200/session**, i.e. roughly **12–17% of face-value session price** 🟠

Compare against membership ARPU: Cult.fit's blended membership ARPU is roughly **₹2,000–2,500/month** 🟠 (order-of-magnitude, not published). Two therapy sessions/month at ₹1,200 = ₹2,400 in *additional* spend — comparable in size to the *entire* existing membership fee. That's a meaningful ARPU-expansion lever **per user who actually adopts it** — but the platform only nets ~₹300–400 of that ₹2,400 as its own margin, and adoption will be a minority behavior (see §3). This is a high-ARPU-per-adopter, low-adoption-rate feature — not a broad-based ARPU lift across the base.

---

## 2. Pricing/packaging call

Not a menu — an actual call: **hybrid, weighted toward pay-per-session, with only a thin free layer bundled into membership.**

Why not full bundling ("N sessions included per tier"): a gym's utilization is self-limiting by physical square footage and class scheduling — a member literally cannot show up to unlimited classes without hitting real constraints Cult.fit already manages for. Teletherapy has **no such physical constraint**. Bundling included sessions into a flat membership fee reproduces the classic gym adverse-selection problem *without* the physical cap that makes it survivable for gyms: the members who use it least subsidize the (unpredictable, possibly clinically heavier-need) minority who use it most, and Cult.fit is now carrying open-ended session-cost liability against a flat fee. 🟠

Why not pure pay-per-session either: zero packaging means zero demand-smoothing for therapist scheduling, and it forfeits the retention value of making mental-health access feel like a membership benefit rather than an upsell store.

**The call:** keep membership as-is; offer repeatable mood logging, simple history, and selected resources without a monthly quota. Price therapist sessions separately, initially as singles; test an optional small credit pack after repeat use and provider capacity are measured. This is a product hypothesis, not a tested packaging win. The free layer still has storage, support, content, and privacy costs. It does not perform clinical triage.

**Named as policy, not just current behavior — what can never sit behind any paywall, at any pricing tier:** the crisis-support link, all consent/export/delete controls, and the basic free mood check-in. This is already true in practice everywhere else in this concept (ATELIER's crisis pattern is always-visible by design), but it has not been stated here as a pricing principle a future packaging change could accidentally violate. Stating it here closes that gap.

---

## 3. Market sizing — order of magnitude only

- Cult.fit's active member base: roughly **1–3 million cumulative/registered users, low-hundred-thousands actively paying at any given time**, across ~20–30 Indian cities. 🟠 (general knowledge, not published current data, and may be stale relative to my training cutoff — treat as a rough anchor, not a real number to plan against)
- India's mental-health treatment gap is widely cited in public health literature at roughly 70–80% of those needing care not receiving it, out of a population-level need estimated in the hundreds of millions. 🟡 (well-known public stat, not something I measured)
- Urban, teletherapy-comfortable, willing-to-pay-online segment is a much smaller slice of that gap — existing dedicated players (Wysa, YourDOST, and similar) suggest a real but still nascent paying market, not a mass-market one yet. 🟡

**TAM/SAM logic for Cult.fit specifically:**
An illustrative funnel is: eligible active members × Faye discovery × first check-in × booking intent × attended paid session × repeat. None of these factors is measured. The earlier example of ~1–2M × 5–10% produced 50,000–200,000 trial users; applying a hypothetical 2–9% repeat-paid conversion produces **1,000–18,000** repeat-paying users. Both the base and rates are invented scenario inputs, so even this range is not a market-size estimate. Use a real eligible-member denominator and pilot cohorts before sizing. 🟠

This is a **niche-volume, high-relevance feature**, not a mass product line — its case has to be made on retention/margin-per-adopter, not on total addressable users.

---

## 4. Growth strategy call

**First hypothesis: retention/upsell among existing members.** 🟠 It is unmeasured and does not rule out other channels.

Reasoning: someone looking for their first therapist does not go looking inside a fitness app for it — a fitness brand has near-zero discoverability or credibility as a *primary* mental-health destination for someone who isn't already a Cult.fit customer. Acquiring net-new users specifically for this feature would mean competing for the same paid search/content intent as dedicated players (Practo, YourDOST, insurance-linked EAPs) who already own that category association — a high, undifferentiated CAC fight Cult.fit has no structural advantage in.

It may work better as a cross-sell inside an existing membership: in-app discovery could lower paid-media spend, while placement, support, provider supply, and privacy costs still need measuring. Any effect on member retention or lifetime value is a pilot question, not an assumed return.

**One channel this section still doesn't name: employer-paid (B2B/EAP-style) contracts.** Everything above compares individual acquisition vs. individual retention/upsell — it doesn't test whether Cult.fit's existing corporate-wellness relationships could carry this the way Lyra Health/Spring Health scale 1:1 therapy in practice: the employer pays per contract, not the individual per conversion, which sidesteps the whole CAC/trial-rate question this section is built around. Flagged, not modeled — it needs real B2B pricing data nobody here has — but it's a materially different growth path than either option this section actually compares, and worth naming rather than leaving implicit in "does not rule out other channels."

---

## 5. The real constraint that could kill this

**Added risk:** failure in Faye can affect the parent Cult.fit brand. A privacy breach, misleading emergency promise, provider-quality complaint, or bad support response may reduce trust in the fitness product too. The pilot needs incident ownership, insurance and liability review, provider escalation, and an exit plan. This risk is separate from whether a new user trusts Cult.fit enough to book.

Three candidates; ranking by how *structurally fatal* each one is, not by how loudly it's discussed:

1. **Regulatory/liability exposure (primary, and likely fatal if under-designed for).** Provider qualifications, documentation, data duties, and platform responsibility differ by professional category and service model. The notes below identify questions, not legal clearance. An adverse event or privacy failure could affect people and the parent Cult.fit brand. Provider scope, contracts, insurance, and incident ownership must be settled before a live pilot.

2. **Therapist supply liquidity (secondary, operational).** Cult.fit already has a proven pipeline for hiring/training fitness trainers, who are a comparatively abundant labor pool. Licensed clinical psychologists/psychiatrists in India are a scarce, credentialed pool with real attrition to private practice — matching supply across Cult.fit's multi-city footprint at consistent quality is a genuine bottleneck the fitness-hiring playbook doesn't transfer to.

3. **Brand credibility risk (real, but the most mitigable of the three).** A high-energy fitness brand asking users to trust it with therapy booking is a legitimate skepticism to expect — but this is the risk the actual design work already addresses well (separate visual register for the Faye tab, quiet trust signals instead of public reviews, de-emphasized gamification). Design can meaningfully de-risk #3; it cannot de-risk #1 or #2.

### Regulatory research (reviewed 2026-09-26; counsel clearance still required)

The following is a research map, not a legal conclusion about a proposed Cult.fit implementation. The non-medical professional discussion below relies partly on secondary commentary; obtain current primary regulatory guidance and specialist review before using it to define provider eligibility or clinical claims.

**Telemedicine Practice Guidelines 2020 + Mental Healthcare Act 2017 — confirmed provisions, and they cut two different ways depending on who's being booked.**

- TPG 2020 governs **Registered Medical Practitioners (RMPs) only** — i.e., psychiatrists (MBBS + MD Psychiatry) doing tele-*psychiatry*. They must hold a valid MCI/NMC registration and, per the jointly-issued NIMHANS/Indian Psychiatric Society Telepsychiatry Operational Guidelines 2020, complete a mandatory telemedicine training course within 3 years of notification. Consent must be explicit and documented, patient identity and decision-making capacity must be verified before a session, and consultation logs, prescriptions, and progress notes must be retained under Mental Healthcare Act 2017 §25. Sources: [Telepsychiatry Operational Guidelines 2020 (NIMHANS PDF)](https://nimhans.co.in/wp-content/uploads/2021/09/Telepsychiatry-Operational-Guidelines-2020.pdf); [Indian Journal of Psychiatry commentary on TPG 2020](https://journals.lww.com/indianjpsychiatry/fulltext/2021/63010/telemedicine_practice_guidelines_of_india,_2020_.16.aspx); [Mental Healthcare Act 2017 full text](https://www.indiacode.nic.in/bitstream/123456789/2249/1/A2017-10.pdf).
- Critically, **TPG 2020 does not cover non-medical mental-health professionals** — the clinical psychologists and counselors a "therapist discovery" flow aimed at first-time, non-clinical seekers would most plausibly list. That population instead falls under **RCI registration** (Rehabilitation Council of India, for clinical psychologists) or the ethical codes of bodies like the Indian Association of Clinical Psychologists for counseling psychologists, with **no central telemedicine-specific statute** governing them — and they cannot diagnose or prescribe. Source: [Legal Requirements for Online Therapy in India (2025)](https://www.lifehetu.com/blog/legal-requirements-for-online-therapy-india-2025).
- **What this changes:** the original claim ("real licensing and duty-of-care requirements on anyone facilitating clinical mental-health services") was directionally right but imprecise about *which* requirements apply to *whom*. If the platform books psychiatrists, it inherits the full RMP/TPG compliance burden (registration verification, training-compliance checks, prescription/record-keeping duties) — a heavier but at least *codified* bar. If it books counselors/clinical psychologists — the more likely product fit here — the compliance bar is credential verification (confirm RCI listing) rather than a single binding telemedicine regime, which is lighter but also murkier: there's no regulator-issued checklist to point to for defensibility, so Cult.fit's own vetting/curation layer (already flagged in §1's table as a cost) is doing real regulatory work, not just brand-quality work.
- **Grading change:** the platform's #1 kill-risk claim upgrades from 🟠 (asserted general impression) to **🟢 for the psychiatrist/RMP track** (TPG 2020 + Telepsychiatry Guidelines are explicit, citable, unambiguous) and to **🟡 for the counselor/clinical-psychologist track** (real and confirmable via RCI registration, but the operational compliance bar is inferred from professional-ethics codes, not spelled out in one binding document the way it is for psychiatrists).

**DPDP Act 2023 — confirmed provisions, and one correction to what this doc originally claimed.**

- **Correction:** the original line — "sensitive health data now sits under the DPDP Act's stricter handling requirements" — overstates what DPDP actually does. Unlike the GDPR or India's own 2011 SPDI Rules (which DPDP replaces), the **DPDP Act 2023 does not create a distinct "sensitive personal data" category with heightened obligations for health data specifically** — all personal data runs through the same consent-first framework. Source: [Sense and Sensitivity: 'Sensitive' Information Under India's New Data Regime — SNR Law](https://www.snrlaw.in/sense-and-sensitivity-sensitive-information-under-indias-new-data-regime/).
- Health data is referenced only narrowly, via §8's "deemed consent" carve-outs (medical emergencies, public-health threats, and employer processing of biometric health data for narrow purposes like attendance) — none of which relaxes or tightens the obligations for a routine, non-emergency therapy-booking flow. Ordinary explicit consent governs it, same as any other personal data field.
- What the [official Act](https://www.meity.gov.in/static/uploads/2024/02/Digital-Personal-Data-Protection-Act-2023.pdf) establishes is a data-breach notification duty and a penalty schedule. The [final 2025 Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) specify operational details with staged commencement. Do not use a draft-rule summary or secondary checklist as the release requirement; have counsel map the provisions in force for the pilot date.
- Purpose limitation is real and directly relevant to what Lego builds: data collected for one purpose (booking a session) cannot be silently repurposed (marketing, a recommendation engine, insurance sharing) without fresh explicit consent. BetterHelp's 2023 FTC fine ($7.8M, specifically for sharing health data with ad platforms) is a live precedent for exactly this failure mode, in a comparable product category, under a different but analogous regime.
- No India-specific data-localization requirement for health data was established by this review; do not infer that every hosting arrangement is allowed. The [Digital Personal Data Protection Rules, 2025](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) were notified on 13 November 2025, with staged commencement. Recheck the provisions in force and other applicable law with counsel before a build.
- **Grading change:** the earlier "DPDP's stricter handling requirements for health data" framing does not survive — downgrade/correct rather than upgrade. Replace it with the verified claim: DPDP applies its *ordinary* (not health-elevated) consent and breach-notification regime, which is still a real build constraint, just a different and more precise one than originally stated.

**Take-rate / pricing — checked directly, mixed result.**

- No real, disclosed take-rate was found for Practo or YourDOST. The 25% commission input for this Cult.fit scenario remains 🟠, not a measured or calibrated comparable.
- BetterHelp's subscriber pricing and reported therapist pay are useful prompts for questions, not a verified take-rate benchmark. Session utilization and included services make a direct comparison unreliable; the simple endpoint arithmetic spans roughly 42–73% before those differences. The Cult.fit 25% scenario needs its own provider agreements and transaction data.

---

## 6. Verdict

**Open channel hypothesis:** [Cult.fit already describes corporate wellness subscriptions that include therapy](https://business.cult.fit/organizations/corpsupport), so an employer distribution surface exists. No employer buyer interview, contract terms, procurement cycle, provider capacity, Faye-specific economics, or privacy boundary has been validated for this proposed flow. Model it separately from consumer cross-sell. Employer access must not depend on employers seeing individual bookings, moods, or therapist identities. Do not present B2B as a fix until buyer willingness to pay and aggregate-only reporting terms are tested.

**Current decision:** consumer singles with free repeatable check-ins are the first pilot package. Credit packs are a later experiment, not a precondition for the product. Earlier assertions in this document that packs are fixed or that BetterHelp establishes a 25% take-rate benchmark are superseded by the correction above.

**It doesn't work yet — and here is exactly what would fix that.**

Under the consumer scenario modeled here, a marketplace retention feature is a plausible first test. The illustrative ~12–17% contribution per attended session is sensitive to provider payout, support, payment, and safety costs; it is not a demonstrated margin. An employer route could have different economics and must be modeled separately before making a growth verdict for the whole product.

But nothing above is measured — it's comparable-inferred (🟡) or asserted order-of-magnitude (🟠), because there is no pilot data, no confirmed therapist pricing/take-rate agreement, and no regulatory sign-off. Before this becomes a real business decision rather than a design concept, go find out, in this order:

1. **Legal/compliance clearance first** — confirm what licensing structure and liability allocation (Cult.fit vs. marketplace therapist vs. insurer) is actually required under the Mental Healthcare Act and current telemedicine/data-protection rules. This gates everything else; if this doesn't clear, nothing below matters.
2. **A real pilot cohort** in 1–2 cities to measure actual trial and repeat-paid conversion from the existing member base against the 5–10% trial-rate and single-digit-percent repeat-conversion assumptions used above — these are the two numbers this entire model is most sensitive to, and both are currently guesses.
3. **Confirmed therapist-side economics** — real negotiated take-rate and real local therapist supply/availability in the pilot cities, not the comparable-based 25%/₹1,200 assumed here.

If those tests support the assumptions above, the consumer route may become a contribution-positive retention feature. If conversion, provider capacity, or compliance cost disappoint, a persuasive deck will not make the service viable. Do not treat the invented national user range as a forecast.

---

*Prepared by MIDAS (business model / unit economics) for HERMES (offer/copy) to build on. The free check-in, paid single session, and provider/legal release gate are current concept choices; pricing, packaging, and channel economics remain open to evidence.*
