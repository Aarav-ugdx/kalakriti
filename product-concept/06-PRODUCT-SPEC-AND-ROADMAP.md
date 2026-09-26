# Faye product spec and evidence roadmap

**Status:** concept-side working proposal, 26 September 2026. The graded hackathon screens, order, Cult.fit brand fidelity, and five decisions in `CLAUDE.md` stay locked. Nothing here is represented as a shipped feature, a clinical claim, or legal clearance. `brief/` remains the source of truth for the submitted flow.

## Product thesis and boundary

Faye gives a first-time therapy seeker a calm way to understand the next step, book a human session, and keep a private, lightweight record of how they feel. The first distribution test is inside Cult.fit's existing member base; that business choice does not narrow the design brief's first-time seeker audience. The commercial pilot persona is the intersection: a member who has never booked therapy. A newcomer who has not used Cult.fit must still understand prices, privacy, and the booking outcome without fitness terminology. A different secondary group is an existing member already in therapy elsewhere. Their job is to compare options, not necessarily to switch. A working therapeutic relationship should never be disrupted merely to consolidate apps or earn a membership discount. If someone already wants to change providers, offer an optional transfer path with explicit, recipient-specific consent for any context they choose to share.

The promise is **control and clarity before and after a booking**, not an inferred diagnosis or an “AI therapist.” The core action is a booked session with a verified provider. Mood logging is an optional, repeatable free companion; it is never a gate to booking. The product does not read a mood icon as a crisis signal, sell urgency, score mental health, or measure success with daily return streaks.

## First build slice: one complete journey

The first slice extends the four locked screens with the smallest useful states around them. Each row is a build contract, not an instruction to change the submission.

| Moment | User-facing behavior | Hard state and recovery | Evidence to collect |
|---|---|---|---|
| Entry | Faye appears in existing Cult.fit navigation; first run explains privacy and offers **Explore therapists** or **Check in**. Neither action requires the other. | If consent cannot be saved, show the choice as unsaved and do not process the related data. Let the user retry or browse non-personalized content. | Comprehension: can users tell whether Faye is private from fitness? |
| Discovery | Filter by concern, language, availability, and preference; show credential scope, next slot, price, and session mode. No stars or review counts. | No matches: remove one filter at a time and show a non-manipulative alternate path. No slots: “Fully booked for now” and other providers, without invented scarcity. | Qualified profile view to booking start; filter dead ends. |
| Booking | Show total charge, cancellation terms, mode, time zone, and who receives booking details before confirmation. Reuse Cult.fit's booking shape. | Payment timeout or uncertain confirmation: show **Checking booking**, never success or a second debit. Resolve via server booking state and idempotency key. | Confirmed-to-attended rate, payment uncertainty, support contacts. |
| After booking | A persistent My Sessions record, a calm confirmation, session logistics, and a first-session prep card. | Provider cancels: notify discreetly, show refund or credit status and rebook choice. Session link fails: show support route and status, not an empty screen. | No-show reasons, reschedule completion, prep-card use. |
| Mood and resource | One icon check-in with optional note, honest sparse history, one optional suggestion, concern-filtered content with duration. | Offline log: state **Saved on this device, waiting to sync** only if durable local storage exists; otherwise state **Not saved**. Never synthesize missing trend points. | Whether users find the log useful, not daily-open maximization. |
| Privacy | A permanent route in existing account settings for consent, data requests, and notification choices. | Failed consent write: keep prior effective state visible, explain failure, and retry. Data-request failure: retain a reference and support route. | User comprehension and successful request completion. |

### First-session prep card

Available after a confirmed first booking and again in My Sessions until the session begins. It answers exactly four questions: **where and when**, **what happens at the start**, **what can I say if I do not know where to begin**, and **how do I change the booking**. It includes a plain cancellation link and optional, editable “one thing I want to mention” note. The note starts private to the user. A separate, explicit **Share with this therapist for this session** action is required; the chosen recipient and expiry appear before sharing. No chat thread, automatic sharing, diagnosis prompt, symptom checklist, or push to disclose. If sharing fails, the card says **Not shared** and the booking remains valid. A therapist may have a different workflow; provider agreements and user testing must validate the prep-card content before release.

Proposed short copy, to test rather than ship verbatim:

> Not sure where to start? You can say that in your session.

> Add a note for yourself. Share it only if you choose.

### Privacy receipt

After a booking, consent change, note share, or data request, show a compact receipt in Faye and make it retrievable in account settings. It states **what happened, what data, with whom, for what purpose, when, and what can be changed**. Booking receipts distinguish the provider's logistics access from the user's mood history; a therapist must not inherit mood history merely because a booking exists. If an action is pending or failed, say so; do not issue a success receipt. The receipt is a transparent view of server-confirmed events, not a second source of truth.

### Discreet notifications

Default to transaction-only reminders that use neutral lock-screen text such as **“You have an upcoming appointment in Cult.fit.”** Avoid therapist name, “therapy,” mood, concern, or session notes in push title/body. Let the user choose no push, in-app only, or email where the platform supports it. Preview the exact lock-screen text. Respect operating-system and existing Cult.fit notification settings. A user-initiated “tell me when a slot opens” alert is a separate opt-in and expires after a short defined period; it cannot silently become marketing consent. A missed push must never be the only route to session details. Any behavior-triggered mood nudge is deferred until users explicitly opt in and a privacy review finds a useful, non-intrusive version.

## Data and consent contract

1. **Separate purposes.** Booking logistics, payments, private mood history, optional note-to-therapist sharing, fitness personalization, notifications, and product analytics each need an explicit purpose and access map. A general Cult.fit login does not grant all of them. Fitness cross-sharing starts off. No advertising or employer audience receives individual Faye events.
2. **Minimum access.** The user sees their Faye data. A booked provider sees only the logistics and any session-specific note the user deliberately shared. Operations sees the minimum needed to resolve payment, booking, or safety incidents, with audited access. Product analytics uses event counts and funnel states without note text or raw mood labels where aggregate counts suffice.
3. **Server-confirmed consent.** Store purpose, scope, recipient, state, timestamp, copy version, actor, and event ID. Enforce the effective state server-side. Withdrawal stops new processing for that purpose and initiates an assessed erasure workflow for data held on that consent, subject to lawful retention; show a pending state until recipients confirm. The [official DPDP Act](https://www.meity.gov.in/static/uploads/2024/02/Digital-Personal-Data-Protection-Act-2023.pdf) addresses withdrawal in §6, erasure on withdrawal in §8(7), and a separate erasure-request route in §12(3). Provide a trackable deletion/correction request route as well. Exact application, exceptions, commencement, and schedules need current counsel review before production.
4. **Deletion and retention.** Publish a per-data-type schedule before launch: logs, optional notes, booking records, payment records, consent events, and support cases may have different justified lifetimes. Do not claim “deleted everywhere” until downstream recipients confirm. The prior 90-day therapist-switch note window is a proposal, not a general retention policy. Test backup and vendor deletion paths.
5. **Security and offline.** Encrypt transport and stored sensitive data, scope provider authorization to the specific booking, audit privileged reads, and exclude Faye payloads from ad pixels and broad analytics SDKs. If offline mood logging is offered, the device queue needs explicit local protection, sync conflict rules, and a clear delete action; otherwise do not promise offline save. These are release requirements to validate in the actual host app, not facts about its current implementation.
6. **Care boundary.** A persistent, non-triggered help link belongs on mood and content surfaces. Support information must come from a maintained, reviewed source with hours, language, and review date. The current status of any named helpline must be confirmed from an authoritative operator before it appears in a product build. No algorithmic crisis inference from mood icons.

## Ideas borrowed as patterns, with firm boundaries

The prior Bee/CycleSync work contributes the **shape** “log quickly → see an honest trend → choose one small action.” It does not contribute cycle data, content, brand, hormonal explanations, or automatic correlation between fitness and mood. Importing it would break Faye's privacy promise and the project's brand rules. One optional later experiment is a user-selected, non-medical reflection prompt tied only to the current check-in, with a “skip” route and no push.

Relationship AI contributes a **user-controlled preparation pattern**: help someone form one question or sentence before a human conversation. The first implementation is a static template in the prep card, not a chatbot. A later bounded tool could help rewrite a user-authored prep sentence for clarity only if it passes a separate safety, privacy, and clinical review. It must not interpret a relationship, label another person, infer risk, impersonate a therapist, or create an ongoing companion relationship. No cross-app data pool, hidden graph, or shared identity layer is proposed.

## Business experiments and decision gates

The original ₹1,200 price, 25% take rate, member count, and conversion funnel are scenario inputs. The corrected illustrative funnel in MIDAS yields 1,000–18,000 repeat payers under its invented extremes; it is not a forecast. BetterHelp subscription price and therapist pay cannot be treated as an apples-to-apples take-rate benchmark.

Cult.fit already markets a [corporate wellness subscription](https://business.cult.fit/organizations/corpsupport) that mentions therapy for “heart and mind.” This is evidence of an existing employer distribution surface, not evidence that Kalakriti's proposed booking flow, therapist network, unit economics, confidentiality terms, or employer contracts already exist. An employer route is therefore a specific integration and buyer hypothesis, not a channel invented from scratch or a proven scale lever.

| Gate | Minimum test | Decision evidence |
|---|---|---|
| Provider and legal feasibility | Current counsel review of provider category, credential checks, contracts, consent, data rights, incident process, and payment disclosures; interviews with providers. | Written approval and signed provider terms; otherwise stop before a live session pilot. |
| Desirability | Moderated walkthroughs with first-time seekers, existing members, and people in both groups; include privacy receipt, descriptor disclosure, empty states, and prep card. | Users accurately explain what is private, who sees the prep note, the total price, and what happens after confirmation. Revise until major misunderstandings are resolved. |
| Supply and unit economics | In one or two locations, measure available slots, attended sessions, provider payout, payment/support costs, cancellation/refund costs, and repeat use. | Contribution per attended session after actual variable costs; provider retention and acceptable availability. No expansion on gross booking volume alone. |
| Packaging | Compare a clear single-session price with an optional, clearly expiring credit pack only after repeat demand exists. | Incremental attended sessions and margin, not prepaid credits sold or unused breakage. |
| Employer channel | Separate buyer discovery, procurement review, and privacy/legal design. Test an employer contract with no individual-level reporting. | Paid buyer commitment and positive service economics without weakening user confidentiality. It is an unvalidated channel, not the base plan. |

**Metric guardrails:** report activation as first meaningful choice (check-in or therapist exploration), booking conversion as an attended paid session, and retention as user-chosen continued use. Monitor mistaken booking states, support complaints, unwanted-notification reports, provider cancellations, and privacy request failures alongside revenue. Do not optimize for more mood logs or more sessions per person as an inherent good.

## Sequence and ownership

1. **Now, concept and hackathon:** keep `brief/` and `design/` stable. Use this document for discussion, not as a claim that added screens are submitted. Gather a small comprehension check for “Steady”; it remains an untested name and the transactional default is “therapy session.”
2. **Before any live pilot:** product and legal owners settle provider scope, payment disclosure across actual rails, consent and retention policy, crisis-content ownership, incident response, and employer data boundaries. Engineering maps real Cult.fit services instead of assuming the conceptual Flutter module describes them exactly.
3. **Pilot slice:** discovery → booking → My Sessions → first-session prep → receipt, plus optional free check-in/resource and permanent privacy route. Build empty, failed, offline, and recovery states before adding personalization. Review the implemented journey with users and providers.
4. **Only after pilot evidence:** add therapist switching with opt-in carry-forward, longer mood history, credit packs, slot alerts, or employer distribution one at a time. Each addition gets a stated user problem, data purpose, owner, and stop criterion. An open chatbot, peer community, and between-session therapist messaging remain outside this roadmap.

This sequence aims for a trustworthy, repeatable service. A large company outcome would require proven distribution, supply, unit economics, and safety; no feature list can establish that by itself.

See [`07-CROSS-POLLINATION-AND-CONSUMER-REVIEW.md`](./07-CROSS-POLLINATION-AND-CONSUMER-REVIEW.md) for the exact Bee/Relationship AI pattern transfer, what the current annotated screens show, and the consumer-prioritized next improvements. The endorsed experience identity is proposed in [`../design/BRAND-AND-EXPERIENCE.md`](../design/BRAND-AND-EXPERIENCE.md); no screen change is implied.
