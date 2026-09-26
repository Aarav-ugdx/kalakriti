# Cult.fit design-language research (Aurora) — grounding for "brand fidelity"

**What this is:** direct research on Cult.fit's own published design system, done because the rulebook's "must stay intact" column (brand colors/logo/tone, existing booking/tracking UI conventions) is a factual claim that should be backed by Cult.fit's actual design language, not assumed. Confirms and extends what `design/DIRECTION.md` already asserted. Sources checked live just now: `blog.cult.fit/posts/aurora-design` and `design.cult.fit/popup/`.

## What's confirmed, with specifics `DIRECTION.md` can now cite directly

- **Name and philosophy:** Cult.fit's current design system is called **Aurora**, explicitly named after the northern lights. Four stated principles: *Bold. Energetic. Immersive.* / *Intent-Driven* / *Simply Efficient* / *Break the Mould*. "Energetic" isn't a vibe Love's team inferred — it's Cult.fit's own word.
- **The signature visual device is a live, animated background** ("active interface") behind glassmorphic (semi-transparent) surface cards — not a static gradient. Cult.fit's team says they spent "hours of iteration" tuning the motion values specifically. This matters for Round 2: a static gradient screenshot is a reasonable hackathon simplification, but if judges know the product, they may expect to hear that the motion/glassmorphism was a conscious simplification, not an oversight.
- **Palette:** Black, White, Yellow, Blue, Pink as core brand colors, plus three named gradients — **Golden Hour, Daylight, Midnight** — confirming the earlier stress-test's fact-check. Status colors (positive/neutral/awaiting/error) are also named, which is directly useful for Faye's booking-state screens (confirmed / pending / cancelled).
- **Logo:** lowercase serif logotype, rounded logomark — Cult.fit's own language for this is "friendliness and warmth" plus "professionalism." Useful phrase to borrow if Round 2 asks why the mascot/tone reads playful but not childish.
- **Typography:** two intentional registers — "task-focused" (fast comprehension) vs. "emotive" (provokes reaction). This maps well onto Faye's own split: booking/dashboard screens should read as task-focused Cult.fit; mascot/resource copy can lean emotive. Worth stating this mapping explicitly in Round 2 if asked "how did you decide when to use which voice."
- **Photography direction:** "bold, real, energetic" — real people, natural light, action shots, not posed stock photography, inclusive across body types/backgrounds. Directly relevant if any therapist-profile photography or mood-dashboard illustration work happens before Round 2 — matching this direction (not stock-therapy-photo aesthetics) is a concrete, checkable brand-fidelity criterion.
- **Layout:** 12-column grid, atomic design methodology (sub-atomic particles → atoms → molecules → organisms → templates). If the Figma/prototype work continues, structuring components this way is a legitimate "we followed Cult.fit's actual system, not just its colors" claim for judges.

## What this changes or adds to existing docs

- Nothing here contradicts `design/DIRECTION.md`'s existing Aurora-gradient reasoning — it's independently confirmed, now with the four named design principles and the glassmorphism/motion detail added, which `DIRECTION.md` didn't have.
- **One real, cheap addition for Round 2 prep:** if asked "why does your screen look static/flat compared to the real app," the honest, prepared answer is "Aurora's signature is an animated background — we used a static equivalent for a hackathon prototype, and would build the actual motion layer in a real implementation." That's a materially better answer than being caught unprepared by the question.
- Not fixed in any file yet — this is new research, not yet merged into `DIRECTION.md` or `round-2-prep.md`, pending the file-coordination question in the chat reply.

## Sources

- [Meet Aurora, cult's design language — The .fit Way](https://blog.cult.fit/posts/aurora-design)
- [design.cult.fit/popup/](https://design.cult.fit/popup/)
- Cross-checked against the earlier stress-test's already-verified gradient names (Golden Hour/Daylight/Midnight, #F06055 Burnt Sienna accent) via `brandfetch.com/cult.fit` — consistent, no contradiction.
