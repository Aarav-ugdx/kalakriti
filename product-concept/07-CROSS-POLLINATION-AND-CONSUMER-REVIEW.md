# Cross-pollination and consumer review

**Status:** planning-only review, 26 September 2026. Bee (CycleSync) and Relationship AI remain separate projects. No accounts, content, private data, model memory, or visual assets move between them. The graded Kalakriti flow and `CLAUDE.md` locks stay intact. This pass does not change any submission screen.

## Transfer decisions

| Source pattern | Kalakriti adaptation | Current / proposed | Production gate |
|---|---|---|---|
| Bee: start with the decision, ask only what changes the next step | Entry should offer **Find a therapist**, optional check-in, and resources; discovery uses concern/language/availability choices. | The annotated discovery screen exists; the entry choices remain a plan. | Test whether a first-time seeker can reach a suitable provider without completing mood onboarding. |
| Bee: show source, uncertainty, and a privacy receipt | A proposed receipt separates booking logistics from mood history and prep notes. | **Proposed:** receipt after confirmation; not in submitted screens. | Server-confirmed event model, purpose/access map, deletion and retention rules, legal review. |
| Bee: care handoff rather than endless self-tracking | A short prep card helps the member take the next human step. | **Proposed:** first-session card in My Sessions; not in submitted screens. | Provider review and interviews on what actually reduces first-session uncertainty. |
| Bee: one useful action with no penalty for skipping | Mood logging is optional; resource suggestions need a user-stated concern. | The required flow shows discovery before mood; skip behavior remains an interaction requirement. | Validate that no hidden recommendation or notification treats mood as a sales or clinical signal. |
| Relationship AI: guided rehearsal for a hard conversation | A few fixed opening lines could help a user begin a first session; later, an editable private note could be shared by explicit action. | **Proposed:** optional, private line choices; not in submitted screens. | If note sharing is built, show recipient, purpose, expiry, and a real **Not shared** failure state. |
| Relationship AI: shared-household privacy and anti-dependence | Neutral lock-screen reminders, no partner/family visibility, no ongoing AI companion. | Privacy copy in screens; reminder control remains specified in `06`. | Device and billing-disclosure tests with people in shared homes, plus provider and safety review. |

The distinctive product idea is **a calm bridge from private uncertainty to a trusted human session**. Its competitive value would depend on reliable providers, availability, and honest privacy controls. A branded chat companion or a larger content library would add surface area without proving that bridge works.

## Customer walk-through: what still feels weak

1. **“Is this really private from my family or my fitness feed?”** The current screen says booking activity stays out of shared fitness features, but a real member may share a phone, email, payment card, or notifications. Show a privacy preview *before* checkout: lock-screen text, payment descriptor if verified, and who can access the booking. Let users choose in-app-only reminders. Do not promise a specific card descriptor until a real payment-rail test confirms it.
2. **“How do I know this therapist is right for me?”** Two sample cards and generic “verified” wording are weak trust evidence. A real profile needs qualification and registration scope where applicable, language, approach in plain words, session mode, availability, price, cancellation terms, and an authentic intro. Provider vetting and claims require qualified review. Do not add star ratings.
3. **“What happens after I pay?”** The annotated confirmation screen is calmer, but a full product needs My Sessions, video-link delivery, time-zone clarity, reschedule, refunds, and a reliable status when payment succeeds but booking confirmation is uncertain. A future prep card should live there, not disappear after one screen.
4. **“Can I use this without logging my mood?”** The required sequence puts discovery before mood. In a future interactive flow, keep the direct therapist route prominent; the first-run check-in must remain optional and cannot be a funnel tax.
5. **“Does this content actually help me today?”** Short article/audio cards show duration, but the sample titles are generic. Test concern-specific exercises with a concrete action and an honest source/author; offer one suggestion that follows a user-selected concern, with no inference from sparse mood points.
6. **“Can I trust the pretty interface?”** The warm mesh is distinctive, but placeholder portraits, a decorative smiling mascot at booking, and a text-only Cult.fit endorsement limit credibility. Use the official master logo, authentic provider imagery, and lower the illustration volume at money/safety steps. The concept should look considered rather than cute everywhere.

## Ranked improvements

| Priority | Recommendation | Why it matters to the customer | Status / acceptance test |
|---|---|---|---|
| 1 | Add **before-payment privacy and cost preview** | Prevents exposure and price surprises at the highest-anxiety moment. | Next design pass. A user can state who sees booking details and the total cost before confirming. |
| 2 | Replace generic therapist cards with **credible profiles** | The provider, not the mascot, is the product. | Needs verified sample information and consented imagery. Users can compare two providers without ratings. |
| 3 | Build **My Sessions and booking recovery** | A service is not complete at the success screen. | Product pilot. Covers uncertain payment, provider cancellation, video-link failure, refund, and reschedule. |
| 4 | Add the **first-session prep card + optional private note** | Helps a first-time seeker arrive with less uncertainty. | Plan only. Note sharing remains gated; users must know what is and is not sent. |
| 5 | Deliver a **server-backed privacy receipt and controls** | Makes the promised separation between mood, booking, fitness, and employer data inspectable. | Plan only. No success receipt on a failed write. |
| 6 | Add **discreet reminders with a preview** | A neutral lock screen matters more than another engagement prompt. | Concept spec only. A user can preview and disable every notification channel. |
| 7 | Make **content actionable and attributable** | A five-minute exercise should answer “what do I do now?” | Content review. Each card shows duration, author/source, and an opt-out. |
| 8 | Test the **Faye by cult.fit identity** with the genuine Cult.fit logo | Builds recognition without making therapy feel like fitness gamification. | Plan only; official master logo asset absent. Five first-time seekers and five members can explain the relationship to Cult.fit. |
| 9 | Audit **empty, slow, offline, and shared-device states** | These are ordinary consumer conditions, not edge cases. | Partly previewed. No false “saved,” “booked,” or “private” message when the relevant service fails. |
| 10 | Test **business packaging only after attended-session evidence** | Discounts and packs can obscure price and incentivize sessions people do not want. | Research gate. Compare single-session comprehension, attendance, contribution, and cancellation burden. |

## Designathon focus

The near-term story is three proof points: **the Cult.fit-to-Faye threshold, a trustworthy first booking, and calm continuity afterward**. A judge can see the screen-order requirement in the stable screenshots; prep/receipt states are future design opportunities, not prototype content today. In the presentation, distinguish designed behavior from live service promises and explicitly mention Cult.fit's existing wellness heritage. The interface can be more ownable without adding another brand name or changing the locked flow.
