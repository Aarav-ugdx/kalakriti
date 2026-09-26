# For any LLM picking this repo up cold

This is a live hackathon submission with a hard deadline (see README). If you're a teammate's assistant (Claude, ChatGPT, Gemini, Cursor, whatever) landing here without prior context: read this file and `brief/` in full before proposing changes to scope, persona, or IA. Don't restart discovery — the decisions below are already made and defended; challenge them explicitly if you disagree, don't silently redo them.

## Locked, cannot change

- Theme: Health & Well-Being. Scenario: Cult.fit (mental health & therapy booking pivot). Once submitted for Round 1 this cannot be swapped for Round 2 — don't propose a different scenario or theme.
- Required screens, in order: therapist discovery → booking confirmation → mood-tracking dashboard → content/resource screen.
- Brand fidelity: Cult.fit's colours/logo, energetic tone of voice, existing membership/class-booking interaction patterns, existing fitness-tracking UI conventions must stay recognisable. This is not a from-scratch wellness app — it's a redesign living inside Cult.fit's existing shell.

## Decisions already made — see `brief/` for full reasoning, don't relitigate without cause

1. **Colour/tone resolution (v2, current):** Cult.fit's Aurora system is already glassmorphic with 4 colour themes across its products — the resolution pulls forward Aurora's own **Yellow**, **Pink**, and **Golden Hour**-gradient logic into a warm gradient-mesh background (peach → lavender → pale pink) with frosted glassmorphic cards, an original mascot built from Aurora's own circular/soft-rounded logomark geometry, and coral reserved for primary CTAs only. This replaced an earlier v1 idea (a dark "Midnight" theme) once the team supplied real design references (vibebevvy.com, habitsupps.com, and several mental-health-app mockups) that pointed toward warmth over darkness — see `design/DIRECTION.md` for the full reasoning and `design/screens/` for the built screens.
2. **Userbase:** primary = first-time therapy seekers, urban 20-somethings, likely renters/students/early-career. Secondary = existing Cult.fit members cross-shopping from fitness. Every screen-level decision in `brief/screen-flow.md` traces back to this.
3. **No star ratings / review counts on therapist profiles** — public reviews of a therapist read as a client privacy leak. Use a quieter trust signal instead.
4. **Mood tracking uses expressive icons, not a 1–10 numeric scale** — numeric scoring reads clinical/diagnostic, which the brief explicitly wants avoided.
5. **No streaks/gamification badges in the mental-health section**, even though Cult.fit uses them elsewhere for fitness — deliberate, named exception, state it explicitly rather than hiding it.
6. **Section name: "Faye" (locked 26 Sep 2026), not "Mind."** "Mind" was the working nav-tab label through most of the build; Love rejected it directly as generic and interchangeable with any competitor's IA. The team evaluated and rejected Steady/Ease/Tend/Still/Nook/Bask/Wren/Nima/Neev (each already used by some small mental-health app globally, and Nima/Neev specifically collide with real Indian clinics — the same category of problem as the earlier rejected "Saath") before landing on **Faye**, which reads as a name rather than a category. The nav label, the mascot/lockup, and every doc reference are updated; see `design/BRAND-AND-EXPERIENCE.md` for the full naming writeup and `product-concept/02-HERMES-offer-and-persona.md` §3 for the superseded "keep Mind" reasoning, kept on record rather than deleted.

## What's genuinely reused vs. what isn't

The team's prior CycleSync/"Bee" project (a separate, unrelated SIH submission) solved a structurally similar problem — tracking a personal, sensitive state without going clinical. The *pattern language* (log fast → see trend → one adaptive suggestion; a "care handoff" moment; a non-preachy content/education surface) is reused here. Bee's actual content, brand, and copy are not reused or referenced in this submission — don't pull Bee-specific names, copy, or assets in.

## Working agreement

- Keep `brief/` as the source of truth for content/IA. Design files (Figma/Canva links, exported screens) go under `design/` once that phase starts.
- If you materially disagree with a locked decision above, say so explicitly with reasoning — don't just override it in a draft.
- This repo must stay **public** — a private repo is an automatic disqualification per the rulebook.
