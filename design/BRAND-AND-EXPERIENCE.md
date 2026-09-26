# Faye by cult.fit — endorsed experience direction

**Status: shipped in the submitted screens, 26 September 2026.** Earlier drafts of this document described "Mind by cult.fit" as a planning-only proposal with no lockup applied. That's superseded — Love rejected "Mind" outright as a name ("generic, could be any wellness app"), the team named it **Faye** instead, and the rename plus a small live lockup (a gradient companion-dot icon + "Faye · cult.fit") are now built into `design/screens.html` and the exported PNGs, not just proposed. The required four-screen order and five decisions in `CLAUDE.md` stay fixed — only the name and its lockup changed.

## Brand architecture

**Faye by cult.fit** is the visible experience name inside the existing navigation destination (nav label: **Faye**). Unlike "Mind" — a flat category noun several competitors could use unchanged — "Faye" reads as a name, not a shelf label: it can open a sentence in product copy ("Faye suggests...") the way "Mind" never could (see `product-concept/02-HERMES-offer-and-persona.md` §3 for the full reasoning and the superseded original verdict). "By cult.fit" still transfers familiarity without making a session feel like a workout.

Names considered and rejected before landing on Faye, and why: **Steady / Ease / Tend / Still / Nook / Bask / Wren / Nima / Neev** — every one of these is already the name of some small mental-health or wellness app somewhere globally (2026 app-store saturation, not a sign the names are bad); **Nima** and **Neev** specifically collide with real Indian mental-health clinics/apps, the same category of problem that ruled out **Saath** (an [existing Indian mental-health service](https://www.saathmentalhealth.com/)) — that Indian-market, same-category collision is the actual disqualifying bar, borrowed from the Saath precedent, not "does any app anywhere use this word." **Faye** cleared that bar: the only close hit is an obscure US "AI self-care companion" app, not an Indian service and not prominent. Do **not** rename the tab "Bee" — Bee is a separate CycleSync project, and its name, data, copy, and mark do not belong in this submission. "Steady" remains a separately-considered, untested paid-session label, not the section name.

Cult.fit's [own rebranding statement](https://blog.cult.fit/posts/cultfit-rebranding) already places therapy and teleconsultation in its wellness category. Its [Aurora system](https://blog.cult.fit/posts/aurora-design) explicitly supports multiple intent-specific themes, glass surfaces, and functional motion. The pitch should present this as a **new integrated therapy-booking experience for the imaginary brief**, not claim Cult.fit has never offered mental-wellness services.

## What makes the UI recognisably Cult.fit

| Inherited element | Faye expression | Reason |
|---|---|---|
| Existing app navigation and booking shape | Same bottom tabs, filter chips, provider cards, a familiar review/confirmation rhythm | Reduces learning cost for members. |
| Aurora colour logic | Yellow/pink/golden-hour family softened into peach → lavender → pale pink mesh | Makes a new mood without a foreign wellness palette. |
| Aurora glass material | Frosted cards, short shadows, large negative space | Keeps brand texture while reducing visual noise. |
| Task and emotive type modes | Clear task hierarchy for discovery/booking; one warmer expressive headline on landing | Separates attention from delight. |
| Coral accent | One dominant action per step, with a deeper accessible coral for white text | Retains energy and measured contrast. |
| Cult.fit identity | Proposed “by cult.fit” endorsement using the real master artwork when available | Makes ownership legible without inventing a new parent logo. |

**Logo fidelity gap:** the repository has no official master vector logo file. Cult.fit's [official guide says not to recreate its logotype](https://design.cult.fit/popup/). The current HTML's plain “Cult.fit” text is not the official logo. For a final branded export, obtain the authorised master artwork and place it at its prescribed clear space. Do not trace the wordmark, improvise a lookalike, or claim the current HTML already contains the official logo.

## Signature design moves

1. **A threshold, not a hard rebrand.** The dark Fitness comparison passes into the warm Faye landing through the same tab bar. The shift is visible in one glance and explained in one sentence.
2. **A small identity, not a mascot show.** The circular companion (now with a soft radial-gradient face and a subtle blush, refined 26 Sep) is for welcome, mood, and content moments, and doubles as the small "dot" icon in the new `Faye · cult.fit` topbar lockup on the discovery and mood screens. It should recede during provider selection, money, cancellation, and safety information — it does not appear on the booking-confirmation or resource screens' topbars, only as the mood-confirmation illustration. The booking screen's current illustration is decorative; a next visual pass should shrink it if moderated review finds it too playful.
3. **A privacy receipt as a brand moment.** Plan a receipt after a real confirmation to show booking access, mood-history boundary, and prep-note boundary. Do not show a successful receipt in a static or failed service state.
4. **A softer first session.** Plan a prep card with optional opening lines and a few logistics answers. It would show a practical human-care bridge without an AI therapist or an overwhelming intake form.
5. **One next action.** Every main screen offers a clear action, a route back, and visible effort/time. No mood streak, star rating, numeric mood score, or behavior-triggered sales prompt.

## Presentation story

For the **current** submission, show: **illustrative Cult.fit Fitness → Faye threshold → therapist discovery → booking confirmation → mood dashboard → resources.** The four graded screens remain in their required order. Prep and privacy-receipt details are proposed future states, not screens in this submission. Use the annotated screens and PNGs as the stable presentation record. Say explicitly that no live booking, data access, payment, or consent service is represented.

## Final visual pass before a real brand release

- Obtain the official master logo asset and check its placement at mobile size.
- Replace gradient placeholder provider avatars with consented, authentic headshots or clearly labeled illustrative portraits. A real clinician profile also needs verified credentials and session terms.
- Test the lockup, mascot intensity, accent contrast, and checkout tone with first-time therapy seekers and existing members. Keep the warmer Aurora solution only if both groups read it as trustworthy and recognisably Cult.fit.
- Confirm that the screenshot exports match the saved HTML after any change; do not submit a stale image set.
