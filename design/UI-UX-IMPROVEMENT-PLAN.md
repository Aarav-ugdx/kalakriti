# UI and UX improvement plan — planning only

**26 September 2026. No screen or prototype changes are part of this plan.** Keep the Health & Well-Being/Cult.fit scenario, required order (discovery → booking confirmation → mood dashboard → resources), warm Aurora v2 direction, and all five decisions in `CLAUDE.md`. The annotated `screens.html` and exported PNGs remain the current submission. The changes below are specific design tasks for a later approved execution pass.

## Product experience to design toward

The first-time customer has four immediate questions: **Can I find someone suitable? What will this cost? Who will know? What happens after I book?** The current work answers parts of each. A stronger experience puts those answers before the first payment and carries them through the first session. The visual identity should make the transfer from Cult.fit Fitness into Faye unmistakable while lowering the volume at sensitive moments.

The visual system is **Faye by cult.fit**, an endorsed naming proposal, inside the existing Faye tab. Cult.fit's [Aurora system](https://blog.cult.fit/posts/aurora-design) already supports multiple intent themes, glass surfaces, functional motion, and familiar components. Its [brand guide](https://design.cult.fit/popup/) says to use the master logo artwork and not recreate the logotype. The repo lacks that asset. Obtain it before a final branded export; use a plainly labeled text endorsement only for internal concept work. Cult.fit has [already described therapy in its wellness category](https://blog.cult.fit/posts/cultfit-rebranding), so present this as a proposed integrated service journey, not the invention of mental wellness at Cult.fit.

## Visual-system upgrades

| Element | Exact direction | Guardrail / check |
|---|---|
| Layout | Use a 12-column mobile grid, consistent 8/16/24/32 spacing, and one primary action in the reachable bottom area. Reserve real negative space around the first decision. | At 320px width, text must wrap without truncating price, credentials, or safety content. |
| Colour | Retain Aurora yellow/pink/Golden Hour logic in a warm gradient mesh. Limit strong coral to the current decision and use the measured deeper coral for white button text. | Recompute contrast for every new text-on-glass state; do not assume translucent surfaces pass. |
| Type | One expressive headline at entry; task-focused, high-contrast labels for therapists, price, policy, and data access. Sentence case over slogan stacks. | Readability at 200% zoom and with large system text. |
| Brand signature | A restrained Faye identity at entry and a quiet, repeated circular cue in section headers. Keep Cult.fit shell/navigation recognizable. | Do not trace the Cult.fit logo or use Bee's name, icon, or assets. |
| Imagery | Provider trust comes from consented, authentic portraits and credential detail. The companion can welcome and soften a check-in, then recede around money, cancellation, and crisis routes. | If real portraits are unavailable, label placeholders as illustrative. No invented clinician identity presented as real. |
| Motion | A short Fitness→Faye threshold transition and subtle card focus only when it helps orientation. No idle motion behind policy or payment text. | Full `prefers-reduced-motion` fallback and no timed content. |

## Screen-by-screen execution brief

### 0. Entry and identity, before the graded sequence

- Show the current Cult.fit tab shell first, then a warm Faye surface. The nav label **Faye** and a restrained **Faye · cult.fit** lockup are now live in `screens.html`; a full landing-page endorsement treatment (beyond the current small topbar lockup) is what still wants brand-asset review before going further.
- Two clear routes: **Find a therapist** and **Check in**. Resource browsing is secondary. No mood log is required to discover or book.
- Move privacy from an abstract “safe space” claim to a short, testable statement: the Faye view is separated from shared fitness activity; booking, device, notification, and billing exposure have separate controls.
- Empty state: someone can browse non-personalized resources when they decline optional data sharing.

### 1. Therapist discovery

- Lead with **“Find someone you can talk to”** or another tested plain-language title. Put concern, language, modality, and availability in a compact filter row; show active filters and one-tap clearing. No dead-end search.
- Each card must answer: provider name, qualification and registration scope where relevant, plain-language approach, languages, next bookable slot, format, duration, total session price. A “verified” badge alone is insufficient.
- In the full profile, let a real provider explain how a first session works and what they can/cannot help with. Avoid popularity ranks, star ratings, review counts, fabricated scarcity, and “members like you” social proof.
- No results: say which filters conflict, then offer to clear a filter or view another provider. No slot: provide a neutral other-provider route and optional user-requested availability alert.

### 2. Booking review and confirmation

- Before the final action, show the **total price**, taxes/fees if any, duration, format, timezone, cancellation/refund terms, contact route, and the intended payment statement description **only if verified on that rail**.
- Add a compact **Who can see this?** explanation before confirmation: scheduling access for the provider and authorized support; mood notes stay separate unless deliberately shared. Include a preview of discreet reminder text and an in-app-only choice.
- Confirmation has one specific success state and a recoverable **Checking booking** state if payment and booking status differ. Do not invite a second debit while status is uncertain.
- After a real confirmation, show session link/status, My Sessions, reschedule, support, and the optional first-session prep card. A privacy receipt belongs here once server-confirmed access and consent events exist.

### 3. Mood dashboard

- Keep expressive icons, no number, no streak. Ask once; do not nag. Sparse history should say “A few check-ins so far” rather than draw a confident trend from missing data.
- Replace a generic “mostly good” arc with an honest dated view that can show gaps and self-selected labels. One suggestion follows an explicitly chosen concern or preference, never a low-mood sales trigger or crisis inference.
- “Skip today,” edit/delete, and data controls should be as easy to find as “log.” If offline support is unbuilt, say **Not saved**; do not imply a queued save.

### 4. Resources

- Keep concern-based organization and visible duration. Add author/clinical-review owner, last-reviewed date, and a concrete first action to every item.
- Split **Learn** (short explanation) from **Try now** (brief exercise) in the content card, so the customer knows what they are opening. Offer text alternatives to audio and avoid auto-play.
- Keep help accessible as a separate, maintained route with verified local numbers, hours, and languages; do not trigger it algorithmically from a mood icon.

## Cross-project features to plan, not copy

- **Bee:** “state → one useful choice → source/uncertainty → privacy receipt” becomes an optional Faye check-in and a transparent access receipt. No cycle or wearable data moves across.
- **Relationship AI:** a short, user-controlled first-session rehearsal becomes three optional starter sentences and possibly a private note. No partner analysis, continuous AI therapist, shared memory, or auto-message. Device/household privacy research informs lock-screen and email choices.
- Put both in the **after-booking journey**, not between the four required graded screens. Their full gates and consumer priorities are in `product-concept/07-CROSS-POLLINATION-AND-CONSUMER-REVIEW.md`.

## Review gates and order

1. **First, content and fidelity:** confirm original brief and locked screen order, get the official Cult.fit logo asset, validate provider sample facts and copy. No fabricated clinical or booking claim.
2. **Then one coordinated design pass:** update screens, prototype if explicitly requested, and exported PNGs together. Never let the static submission and any interactive demo disagree.
3. **Moderated comprehension check:** test five first-time seekers and five existing members. Ask them to find a provider, state total cost/cancellation rule, explain who sees a booking versus mood history, find the post-booking next step, and return from an empty result. Observe errors rather than asking if they “like” the design.
4. **Accessibility and hard-state check:** contrast, keyboard and screen-reader order, large text, reduced motion, 320px width, no-results, no-availability, uncertain payment, notification privacy, and offline save truthfulness.
5. **Presentation:** lead with the Fitness→Faye transition, then the four required screens. Defend each move with the user question it answers. Separate a design concept from a functioning therapy service.

**Highest-value next visual change:** strengthen therapist credibility and pre-payment transparency before adding another mascot, motion layer, or AI feature. That is where a first-time customer decides whether to trust the experience.
