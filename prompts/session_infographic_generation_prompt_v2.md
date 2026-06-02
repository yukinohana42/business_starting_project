# Session Infographic Generation Prompt v2

You are creating a visual learning experience for the junior entrepreneurship workshop.

## Required Reading

Read:

- `SOURCE_OF_TRUTH.md`
- `DESIGN.md`
- `docs/visual_learning_system_v2.md`
- `docs/global_visual_acceptance_criteria.md`
- `docs/session_visual_design_map_v2.md`
- Target session files under `sessions/` or `outputs/`

## Core Rule

Do not create an ordinary explanation slide deck. Create a discovery-game learning sequence.

## Process

1. Identify the target session: Day1, Day2, Day3, Day4, Day5, or parent material.
2. Classify each page as Mission Board, Quest Map, Detective Note, Case File, Evidence Board, Card Table, Experiment Lab, Pitch Stage, Final Mission Sheet, or Reflection Log.
3. For each page, define:
   - Main message
   - Character action
   - Game element
   - Learner action
   - Visible Before/After or learning change
   - Safety risk to avoid
4. Create an acceptance table.
5. Only after the table passes, create copy, layout plan, HTML/CSS, or PNG instructions.

## Mandatory Visual Requirements

- Characters must act: memo, observe, point, arrange cards, write sticky notes, sketch, ask, test, watch reactions, reflect, or present.
- Game elements must function: cards, notes, stamps, maps, logs, and sheets must guide a learner action.
- Value must be visible as change in a person or situation.
- Keep 1 page 1 message.
- Keep Zoom readability, but do not sacrifice the discovery-game experience.

## Prohibitions

- Round icons only.
- Face-only characters.
- Name labels only.
- Game words in titles only.
- Heading + body + cards only.
- Score, ranking, trophy, reward bait.
- Money hype.
- Existing IP, existing characters, or specific manga artist imitation.

## Stop Rule

If the page can be described as a clean explanation slide, stop and redesign it as a learning screen.

## Manual Handoff Rule

If image generation is involved, use manual handoff mode. Create prompt packets that a user can paste into ChatGPT / GPT image generation. Do not assume Codex will generate images or that an OpenAI API key is available.

Each prompt packet must include final prompt, checklist, correction template, candidate save path, and return-to-Codex template.
