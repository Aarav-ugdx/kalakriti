# Stress test — MIDAS/HERMES/ATELIER/Lego product-concept chain

**What this is:** an independent review of `01-MIDAS-business-model.md` through `04-Lego-technical-and-compliance.md` plus `00-RESEARCH-PILLARS-INDEX.md`, done from a separate session with no stake in the original work, at Love's explicit request to stress-test rather than regenerate. Fact-claims were checked against live sources where checkable (web search + direct page fetch), not just re-read and trusted. Doesn't touch the graded Round 1 deliverable (`brief/` + `design/`) — none of this blocks or changes that.

**Bottom line, stated plainly:** this is unusually rigorous for a hackathon side-document — it already self-audits (the risk register in `00-RESEARCH-PILLARS-INDEX.md` catches several real things), it corrects its own overclaims (DPDP, the KIRAN/Vandrevala helpline check), and it did real Playwright testing instead of assuming ARIA attributes work. Most of what I independently checked holds up. What follows is the actual delta: places where a claim was more confident than its sourcing supports, one real math imprecision, and — the most substantive finding — a business-model lever the analysis never tests at all.

---

## Independently verified — holds up

Checked live, not just re-read:

- **Vandrevala Foundation's number is +91 9999 666 555, 24×7×365** — confirmed directly from their own contact page. Matches Lego's claim exactly.
- **Tele MANAS is 14416** (also listed as 1800-89-14416) — confirmed on the government's own current National Mental Health Programme page (`dghs.mohfw.gov.in`). That page does **not** mention KIRAN at all — see caveat below on what this does and doesn't prove.
- **DPDP withdrawal/erasure finding retracted after a primary-source check.** The original review read §12 in isolation and missed §8(7) of the [official Act](https://www.meity.gov.in/static/uploads/2024/02/Digital-Personal-Data-Protection-Act-2023.pdf), which provides for erasure on consent withdrawal unless legal retention is necessary. §6(4)–(6) covers withdrawal and cessation; §12(3) also gives a separate erasure-request route. Lego's earlier “toggle only stops future use” conclusion was wrong. The corrected product behavior and legal-review gate are in `04-Lego-technical-and-compliance.md` §4.
- **BetterHelp's $7.8M FTC settlement for sharing health data with ad platforms** — confirmed directly on ftc.gov. Real precedent, correctly cited.
- **Aurora's gradient names (Golden Hour, Daylight, Midnight) and the #F06055 "Burnt Sienna" accent** — confirmed on `design.cult.fit/popup/` and `brandfetch.com/cult.fit`. I checked the *other* cited source (`blog.cult.fit`) first and it didn't name the gradients, which almost became a false "unverifiable claim" finding — flagging that so whoever cites this doesn't hit the same false alarm. The underlying research is sound; the whole Round 2 answer to "colour rationale" (*"we pulled Aurora's own gradient logic forward, we didn't invent a palette"*) is a genuinely accurate claim, not marketing gloss.
- **The accessibility work is real, not asserted** — I didn't re-run the Playwright session myself, but the methodology described (drive real key events, read `document.activeElement` and computed styles post-transition, catch and correct a false alarm from reading state before a CSS transition finished) is exactly what rigorous testing looks like, and it's internally consistent with the two contrast audits' shared root-cause diagnosis (translucent light-on-light reads far worse than the alpha value suggests). No reason to doubt it.

## Where the sourcing was thinner than it reads

1. **KIRAN "discontinued" — the cited evidence is weaker than the confidence with which it's used.** Lego's doc cites one unrelated GitHub project's commit message ("Replace the discontinued KIRAN helpline") as its evidence. On its own, a stranger's commit message is not proof a national government helpline is dead — it's one person's assumption, possibly wrong. My own check adds a slightly better signal (the government's *current* mental-health-programme page lists only Tele MANAS and doesn't mention KIRAN), but that's still absence-of-mention, not a confirmed shutdown notice. **The decision itself (lead with Tele MANAS, don't hardcode KIRAN) is still the right call** — just say so as "status genuinely unclear, erring toward not listing it" rather than implying it's confirmed dead. Low stakes for Round 1 (not graded), but this is exactly the one screen in the whole concept where being wrong is a real-world harm, so the epistemic honesty matters more here than anywhere else in the document.

2. **The BetterHelp take-rate range (50–68%) understates the actual spread.** BetterHelp pricing is $260–400/mo (~4.3 sessions/mo → $60–93/session); therapist pay is $25–35/hr. The stated 50–68% range comes from pairing low-with-low and high-with-high. Crossing the full ranges properly (cheapest session vs. highest pay, priciest session vs. lowest pay) actually spans roughly **42–73%**, a wider band. Doesn't change the conclusion — Cult.fit's assumed 25% take is generous either way — but the number as stated implies more precision than two independently-sourced ranges actually give you.

3. **The market-sizing funnel has an unstated arithmetic gap.** 50,000–200,000 trial users × "single-digit % repeat-conversion" mechanically lands somewhere in the low-thousands-to-~20k range, not cleanly at "low tens of thousands" — that phrase is only true if you're near the top of both ranges at once, which isn't stated. Either show the multiplication or soften the claim to "thousands to tens of thousands." Minor, but it's the kind of unshown-work gap that undermines an otherwise carefully-graded (🟢/🟡/🟠) document.

## Real gaps — not in the existing risk register

4. **The employer channel needs its own model.** MIDAS initially compared consumer acquisition with retention inside membership, omitting a corporate buyer. [Cult.fit's corporate site](https://business.cult.fit/organizations/corpsupport) already mentions therapy in wellness subscriptions, so this is an existing distribution surface worth investigating. It does not establish Kalakriti's buyer demand, clinical supply, pricing, confidentiality terms, or margin. Employer contracts could change acquisition economics; they could also add procurement and service costs. Test them rather than treating B2B as the automatic fix to a thin consumer model.

5. **Reputational risk is only modeled in one direction.** MIDAS's "brand credibility" risk (#3) asks whether users trust *Cult.fit* to do therapy well. It doesn't ask the reverse, arguably bigger question: what a bad outcome — a missed crisis, a therapist complaint, a data leak on the most sensitive data category in the app — does to the *entire* Cult.fit brand, fitness included. ATELIER's crisis-link firewall (never inferring risk from mood data) mitigates some of this at the design layer, but the business-risk framing never names brand-contagion as its own line item, and it's a real one given Cult.fit's core business is unrelated and much larger than this feature.

6. **The secondary persona is asserted, never actually designed for — and it's a named Round 2 judging line.** The rulebook explicitly asks for "userbase identification... first-time therapy seekers vs. existing Cult.fit members — **and how the design serves both**." HERMES built one persona (Ananya, first-timer) end to end: Schwartz stage, value equation, copy, funnel, habit loop. The secondary persona (existing members cross-shopping) gets one sentence in `screen-flow.md` and nothing else — no distinct copy, no distinct funnel moment, no feature. If a Round 2 judge asks "show me the design decision that serves an existing member differently than a first-timer," there is currently nothing in this repo to point to. Cheap to fix with a short HERMES-style addendum before Round 2; not fixable by asserting the persona exists in a bullet point.

7. **"Steady" — already self-flagged as untested, and it's cheap to actually de-risk before Round 2.** The existing docs correctly caught that this name propagated as if-settled two documents after HERMES flagged it as a bet. Since it costs nothing but a few minutes, an informal gut-check with 3–5 people (team, friends, anyone outside the project) before Round 2 turns "flagged as untested" into either "held up" or "changed" — better than presenting a flagged-but-unactioned risk to judges.

## Status update (2026-09-26, same day)

Items 1, 3, and 6 above were acted on directly in the source docs, not left as standing findings:
- **#1 (KIRAN sourcing):** `04-Lego-technical-and-compliance.md` now notes a second independent signal (gov't current programme page omits KIRAN) while still correctly declining to assert it's confirmed dead.
- **#2/#3 (BetterHelp range, market-sizing math):** `01-MIDAS-business-model.md` now states the fuller 42–73% crossed range alongside the like-with-like 50–68%, and shows the trial×conversion multiplication explicitly instead of asserting "low tens of thousands" as a bare conclusion.
- **#4 (enterprise/B2B channel):** flagged in `01-MIDAS-business-model.md` and given a buyer/privacy gate in `06-PRODUCT-SPEC-AND-ROADMAP.md`; no economic model or buyer proof exists yet.
- **#6 (secondary persona):** `02-HERMES-offer-and-persona.md` §7 now covers an existing-therapy cross-shopper without pressuring someone to leave a working provider. `brief/screen-flow.md` distinguishes this group from an existing-member first-time seeker.
- **#5 (reputational risk):** MIDAS now names failure spillover to the parent brand and an incident-ownership gate. **#7 ("Steady" name-test)** still needs actual people to test comprehension; no document edit can substitute for that.
- **New primary-law correction:** the earlier DPDP finding above missed §8(7); `04-Lego-technical-and-compliance.md`, `00-RESEARCH-PILLARS-INDEX.md`, and the build spec now carry the revised withdrawal/erasure workflow. Counsel still has to review scope and commencement before launch.

## What actually needs doing with ~18 hours left

None of this blocks Round 1 — `product-concept/` was correctly kept separate from day one and the graded deliverable doesn't reference it. In priority order if there's time before Round 2 prep:

1. Fix #6 (secondary persona) — it's the only item above that maps directly to a named judging criterion with currently nothing to show.
2. Soften #1 and #3's stated confidence (one sentence each) — costs nothing, removes an honest-but-avoidable overclaim.
3. Note #4 (enterprise channel) as a real open question for anyone who treats this as more than a hackathon exercise — not a Round 2 requirement, but the single most consequential gap if this concept goes anywhere after judging.
4. #2, #5, #7 are worth a mention in passing if Round 2 discussion goes deep on the business model, not worth dedicated prep time.

*Independent review — flags things, doesn't silently fix them, per the same discipline the original docs used on each other.*
