# Visual direction — synthesized from Love's references

Supersedes the earlier "5th Aurora, Midnight-based, dimmed" idea in `brief/research.md` with something better-grounded: the references Love sent aren't muted/dark-calm, they're **warm, soft, glassmorphic, and a little playful** — and that direction actually resolves the brand-fidelity tension *better* than a dimmed dark theme does, because it stays inside Aurora's own existing palette instead of just turning the lights down.

## References, what each contributes

- **Mental-health app mockups (uploaded):** the real precedent pattern — warm gradient mesh backgrounds (purple→orange, peach→lavender), frosted glassmorphic cards floating on top, a small illustrated mascot character carrying emotional tone ("keep your head up"), mood logged via a rainbow arc / icon chips rather than a number, symptom/concern tagging as pill chips.
- **vibebevvy.com:** jewel-tone-into-pastel palette, bold rounded friendly sans-serif type, hand-drawn ornamental touches that soften a functional interface, generous whitespace.
- **vibrant.noomoagency.com:** confident high-contrast presentation, willingness to make wellness feel current/interactive rather than clinical.
- **habitsupps.com:** restrained, credible "science-backed but approachable" tone — a reminder not to overdo the playfulness for the booking/checkout-style screens (Aurora's own task-focused type mode already tells us the same thing).

## The resolution

Same brand, dialled toward warmth instead of toward darkness:

- **Palette:** pull forward Aurora's own **Yellow** and **Pink**, plus the **Golden Hour** gradient logic, rather than inventing new brand colours. Coral (`#F06055`) stays reserved for primary CTAs only — this is both the energetic-tone-of-voice requirement and the reference mood, satisfied by the same choice.
- **Background:** soft gradient mesh (peach → lavender → pale pink), not a flat dark surface — matches the references, still uses hues already in Aurora's family.
- **Cards:** glassmorphic, frosted, rounded-2xl, soft shadow — this *is* literally Aurora's documented visual language already, no invention needed.
- **Mascot:** one original illustrated companion, built from cult.fit's own logomark geometry (circular, soft-rounded, symmetric — Aurora's stated logomark intent). Not a copy of any named brand's mascot. Carries warmth/reassurance on the mood + resource screens the way the reference mascots do.
- **Typography:** a rounded geometric sans for headers/emotive moments (mirrors the references' "bold rounded friendly" type and Aurora's emotive mode), a plain clean sans for booking/task screens (Aurora's task-focused mode, and habitsupps.com's restraint).
- **Mood tracking:** icon/chip based, plus a rainbow-arc trend view echoing the reference "Weekly Mood" pattern — no numeric 1–10 score anywhere.

This is what `screens.html` in this folder implements.

## Endorsed experience identity

An endorsed **Faye by cult.fit** identity is now live inside the existing Faye tab — the nav label, a small gradient-dot lockup ("Faye · cult.fit") in the discovery and mood-dashboard topbars, and a refined gradient mascot are built into `screens.html`, preserving the four required screens, Aurora-derived palette, and app shell. The naming, brand, and official-logo boundary is in [`BRAND-AND-EXPERIENCE.md`](./BRAND-AND-EXPERIENCE.md). Obtaining the official Cult.fit master logo asset for a real branded export remains open — see that file's "Final visual pass" section.
