# Stitch prompts — regenerating or extending the Faye screens

**What this is for.** `design/screens.html` is the hand-built, locked source of truth for the six submitted/comparison screens — it is what got measured in `CONTRAST-AUDIT.md` and exported to `design/screens/*.png`. This file is a **separate, parallel tool**: ready-to-paste prompts for [Google Stitch](https://stitch.withgoogle.com) (Google Labs' text/image-to-UI generator), for anyone on the team who wants to explore visual variations, generate new screens beyond the required four, or produce a second reference render to sanity-check the hand-built HTML against. Nothing generated from these prompts replaces or gets exported over `screens.html` without a human choosing to bring it in — Stitch output is a reference to adapt, the same way the team's own external mockup references were adapted in `DIRECTION.md`, not a drop-in replacement for the audited, contrast-checked file.

**If a screen generated from these prompts ever gets adopted into the submission:** re-run the contrast method in `brief/CONTRAST-AUDIT.md` against it before shipping. Stitch does not know this repo's WCAG fixes (`--coral-deep`, the badge-pill simplification, the toggle/step-dot fixes) and will not apply them on its own — carry every locked color decision below across by hand, then re-measure.

---

## 0. Style prompt — paste this first, once per Stitch project

Paste this as the opening prompt (or as Stitch's "theme"/system-level input if the project supports one) before any per-screen prompt below. It encodes everything in `design/DIRECTION.md` and `design/BRAND-AND-EXPERIENCE.md` that every screen must share.

> Design a mobile app screen for **Faye**, a therapy-booking and mood-tracking section living **inside Cult.fit's existing fitness app** — not a standalone app. This is a warm, calming counterpart to Cult.fit's usual high-energy fitness UI, built from Cult.fit's own real design system (called Aurora), not a generic wellness-app template.
>
> **Background:** a soft gradient mesh — peach/cream at the top-left, blending through pale pink at the top-right, into a light lavender at the bottom. Airy and warm, never a flat solid color, never dark.
>
> **Cards and surfaces:** frosted glassmorphism — semi-transparent white (roughly 60–80% opacity), backdrop blur, soft drop shadows, generous rounded corners (20–24px radius). Cards float on the gradient, they don't box it in with hard edges.
>
> **Color palette (exact hex, do not substitute):**
> - Coral (`#F06055`) — decorative only: mascot cheeks, avatar gradients, small accent icons. Never as text or a solid button fill on a light background.
> - Coral-deep (`#AD453D`) — the ONLY color for primary-button fills with white text, badge text, and the active nav-icon color. This darker shade exists specifically because bright coral fails WCAG contrast as text/fill on light backgrounds — always use coral-deep, never bright coral, for any of those three uses.
> - Yellow (`#FFC94A`), Pink (`#FF9FCE`) — secondary gradient stops, avatar backgrounds, mascot variants.
> - Ink (`#17151A`) — primary text and active filter-chip fill.
> - Ink-soft (`#4A4652`) — secondary/muted text.
> - Frost white (`rgba(255,255,255,0.55–0.85)`) — card and chip fills.
>
> **Typography:** a rounded, friendly geometric sans-serif for large headlines (bold, slightly tight letter-spacing) — think warm and human, not corporate. A plain, highly-legible sans for body text, prices, and form-style content. Sentence case everywhere, never ALL-CAPS except tiny section eyebrow labels (11px, letter-spaced, uppercase, muted color — e.g. "SESSION DETAILS").
>
> **The Faye mark:** a small circular companion character — a soft, rounded blob face (radial gradient fill, one color family per context: pink-toned or yellow-toned), two simple round dot eyes, one simple curved smile line, two faint blush ellipses under the eyes. No limbs, no accessories. Built from Cult.fit's own circular logomark geometry — friendly and inclusive, not a mascot-brand show. It appears large (~90px) only on the Faye landing screen and the post-booking confirmation illustration; everywhere else it shrinks to an 18px "dot" icon used inline next to the wordmark, e.g. "🔴 **Faye** · cult.fit" in a small top bar — a tiny circular gradient dot standing in for the full character.
>
> **Bottom navigation:** four items, icon + label, in this exact order: **Fitness, Faye, Transform, Profile**. Inactive items are muted grey-ink. The active item (Faye, on every Faye-section screen) is colored in coral-deep, both icon and label — this exact color, not bright coral.
>
> **Tone of voice:** warm, plain-language, calm — never clinical, never falsely cheerful, never using words like "score," "diagnosis," or "patient." Cult.fit's native energetic voice is dialed down here, not abandoned — this is still confident and clear, just quieter.
>
> **Hard exclusions — do not generate any of these, even if they'd be typical for a wellness app:**
> - No star ratings or review counts anywhere on a therapist card or profile.
> - No numeric mood score (no "7/10", no slider with a number) — mood is always expressive icons/emoji-style faces with a text label underneath (Calm, Good, Okay, Low, Anxious), never a number.
> - No streaks, badges, points, levels, or any gamification element anywhere in a Faye-section screen (Cult.fit's Fitness section does use streaks — that's correct there, wrong here; this is a deliberate, named exception).
> - No auto-advancing carousels or countdown timers.
> - No dense multi-metric charts — trends are a single soft arc or simple line, one takeaway, not a dashboard of numbers.

---

## 1. Screen — Faye landing (entry / threshold)

Reference: `design/screens.html` frame `#s0m`, exported as `design/screens/00b-faye-tab-landing.png`.

> The very first screen a Cult.fit member sees after tapping the **Faye** tab from the fitness home screen — a calm threshold moment, not a dashboard. Center-aligned, generous vertical whitespace, nothing crowded.
>
> Top: status bar only, no header text.
> Center: the large Faye mascot (pink-toned gradient variant, ~90px), then below it the headline **"Welcome to Faye"** in the rounded display font, then two lines of warm plain-language subtext: "Same membership, a quieter part of the app — book a therapist, check in with how you're doing, or just read something short."
> Below that, two full-width buttons stacked with a gap: a solid coral-deep primary button "Find a therapist", then a ghost/outline secondary button (transparent fill, thin ink border) "How are you feeling today?".
> Bottom: the four-item nav bar with **Faye** active (coral-deep).
> No other content — this screen is intentionally sparse.

---

## 2. Screen — Therapist discovery

Reference: `design/screens.html` frame `#s1`, exported as `design/screens/01-therapist-discovery.png`.

> A therapist-discovery screen for Faye. Top bar: a small rounded-square back button on the left, the small "Faye · cult.fit" lockup (18px gradient dot + wordmark) centered.
> Headline: "Find your space." Subtext: "Talk to someone who gets it — book a session that fits your week."
> A search field styled as a frosted pill with a magnifying-glass icon and placeholder "Search by concern, language...".
> Two rows of horizontally-scrolling filter chips (pill-shaped, tap targets, not a form): row one is concern — Anxiety (shown active/selected, filled dark ink with white text), Stress, Relationships, Sleep; row two is logistics — This week, Video, In-person.
> Below the chips, a vertical list of therapist cards (frosted glass, rounded-24px). Each card: a square avatar with a soft gradient fill (pink-to-yellow or yellow-to-pink, no photo), the therapist's name in bold, a one-line role/specialty underneath in muted text, then a row of two small pill badges — e.g. "Verified" and "8 yrs practice" — text colored coral-deep on a plain light pill (not a coral-tinted pill — a tinted background against coral text actually lowers contrast, keep the pill neutral). Below the badges, a row with the next available slot on the left ("Next: Today, 6:30 PM", bold) and the price on the right in muted text ("₹1,200 / session").
> Include at least two therapist cards with different avatar gradients and different specialties.
> **Do not** add a star rating, a numeric review score, or a review count to any card — use only the credential badges as the trust signal.
> Bottom: four-item nav, Faye active.

---

## 3. Screen — Booking confirmation

Reference: `design/screens.html` frame `#s2`, exported as `design/screens/02-booking-confirmation.png`.

> The **post-confirmation** state of a booking flow (not the review-before-confirming step) — this is what a first-time user sees right after their first therapy booking succeeds, and the tone should answer "who knows about this?" before it answers "did it work?"
> Top bar: back chevron, centered plain-text label "Booking confirmed" (no lockup icon here — the mascot recedes around booking/money moments per the brand rules).
> Center block: the Faye mascot in its yellow-toned gradient variant (smaller, ~74px), headline "You're booked", subtext "Take a breath — the hard part (reaching out) is done."
> A frosted card labeled (small uppercase eyebrow) "SESSION DETAILS" with a simple key-value list: Therapist / Dr. [name], When / [date+time], Format / Video call, Price / ₹1,200 — keys in muted text left-aligned, values bold right-aligned, thin hairline dividers between rows.
> A second frosted card labeled "CANCELLATION" with one plain-language sentence: "Free to reschedule or cancel up to 4 hours before your session. No questions asked." — the cancellation policy must be visible here, not buried in fine print or a separate terms page.
> Below the cards, a lower-contrast note-style block (a lock icon + text) stating a privacy line: "This booking stays out of shared activity, streaks, and your profile feed. Your therapist and authorised booking support can access the details needed for your session."
> Fixed bottom area (not scrolling with the content): a solid coral-deep button "Add to calendar", then a ghost secondary button "Reschedule". Exactly these two actions, nothing else.

---

## 4. Screen — Mood-tracking dashboard

Reference: `design/screens.html` frame `#s3`, exported as `design/screens/03-mood-dashboard.png`.

> A daily mood check-in and trend screen for Faye. Top bar: the "Faye · cult.fit" lockup on the left, a small rounded notification-bell icon on the right.
> Headline: "Hi [name]" (personalized greeting), subtext "How are you feeling today?"
> A horizontal row of five mood options, each a circular "face" icon (frosted white circle containing a simple emoji-style expressive face) with a one-word label underneath: Calm, Good, Okay, Low, Anxious. One is shown selected — a thin coral ring around its circle and a solid (non-frosted) white fill to distinguish it. **No numbers anywhere in this row** — expressive faces and words only, this is a hard rule, not a style choice.
> A frosted card labeled "THIS WEEK" containing a single soft arc (a rounded half-donut/arc shape, not a bar chart or line graph, drawn thin with rounded end-caps, background track in a pale neutral, filled portion in bright coral) next to a short label stack: "Mostly" then bold "Good 🙂". Below the arc, one line of supportive, honest copy: "You've checked in 3 times this week — steadier than last week." (Note: if check-in history is sparse, this line should say so plainly — e.g. "A few check-ins so far" — never imply a confident trend from only one or two data points.)
> A second frosted card labeled "FOR YOU TODAY" with a small rounded-square gradient icon, a bold one-line suggestion title ("5-minute breathing space"), and a muted one-line description underneath. Exactly one suggestion — never a list of several.
> **Do not** add a streak counter, a flame icon, a number of consecutive days, or any badge/achievement element to this screen — that is a deliberate, named exception to how the rest of Cult.fit works (the Fitness section does use streaks; this section explicitly does not).
> Bottom: four-item nav, Faye active.

---

## 5. Screen — Content / resources

Reference: `design/screens.html` frame `#s4`, exported as `design/screens/04-content-resources.png`.

> The calmest screen in the flow — deliberately no gamification, no urgency, generous whitespace. Top bar: back chevron, centered plain label "Learn".
> Headline: "A little help, gently." Subtext: "Short, real, no jargon — pick what fits your day."
> A row of filter chips organized **by concern** (the same taxonomy as the discovery screen's concern filters, for consistency): Anxiety (active), Sleep, Relationships, Stress.
> A vertical list of resource cards (frosted, rounded), each with: a small square thumbnail with a soft gradient fill (a different pastel pairing per card — pink/purple, yellow/coral, purple/pink), a bold one-line title, and a muted metadata line stating **format and duration up front** — e.g. "Article · 4 min read", "Audio · 10 min", "Guided exercise · 5 min". Every card must show its time cost before the user taps in.
> Include at least three cards with visibly different formats (article, audio, guided exercise).
> No progress bars, no "streak of days read," no badges for completing content.
> Bottom: four-item nav, Faye active.

---

## 6. Optional — the Fitness-to-Faye threshold comparison

Reference: `design/screens.html` frames `#s0f` (dark) and `#s0m` (warm), exported as `00a-existing-fitness-home.png` / `00b-faye-tab-landing.png`. Only generate this if you specifically need a fresh version of the *comparison* pair for a presentation — screen 1 above already covers the Faye-landing half on its own.

> Generate two screens side by side that make one visual point: the same app, a deliberate register shift.
>
> **Screen A (dark, "Fitness"):** a near-black background with a subtle dark purple/maroon radial glow at the top corners. Header "Good evening, [name]" with a bell icon. Bold white headline "Push your limits today", muted stat line "3 classes booked this week · 1,240 kcal burned". Two class cards with dark jewel-tone gradient fills (deep purple-to-maroon, deep blue-to-green), a coral "LIVE NOW" or time-stamp tag, a bold white class title and muted subtitle. A streak row with a flame icon in bright coral, bold white "12-day streak" and a muted supporting line. Nav bar on dark background, Fitness active in bright coral (not coral-deep — this dark screen already passes contrast with the brighter shade and should keep it).
>
> **Screen B (warm, "Faye"):** exactly the Faye landing screen from prompt 1 above.
>
> The point of generating them together is the one-glance contrast: dark/high-energy/red-accented vs. warm/gentle/pastel — same bottom nav, same brand, deliberately different register for a different moment.

---

## How to use these with Stitch, practically

1. Start a new Stitch project, paste the **style prompt (§0)** first so the color, type, and exclusion rules anchor every screen that follows in the same project/thread.
2. Paste one per-screen prompt at a time (§1–§5, and optionally §6) and generate. Stitch tends to drift on exact hex values and on the "no numbers in mood tracking" / "no streaks" rules over a long session — re-state the relevant exclusion line from §0 in the same message if a regeneration starts drifting.
3. Treat everything Stitch returns as a **reference**, the same way `DIRECTION.md` treated the external mockup references (vibebevvy.com, habitsupps.com, etc.) — cross-check it against the locked decisions in `CLAUDE.md` before anyone treats it as a candidate to adopt.
4. If a Stitch output is adopted into the actual submission, it replaces the relevant `#sX` frame in `screens.html` (or is rebuilt by hand to match it) — never just drop a Stitch export in as a competing, unaudited PNG next to the contrast-checked set. Re-run `brief/CONTRAST-AUDIT.md`'s method against the new colors/text pairs before it ships.
5. Export from Stitch to Figma if the team wants to hand-tune spacing/type afterward — Stitch's own export path supports that handoff.
