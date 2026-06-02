# The Undo Problem in AI Products

AI products skipped designing undo, shipped branching as retrofit. Two are not same. Cmd+Z is one of software design's most successful conventions—works identically in 1987 Mac and 2026 Figma. Lineage starts Xerox PARC (mid-1970s) with Larry Tesler and Tim Mott's modeless Gypsy editor. Apple's 1987 HIG codified Edit→Undo as system primitive. Don Norman's Design of Everyday Things named principle: system should forgive users. Jakob Nielsen's Heuristic #3 codifies: support Undo and Redo. Yet ChatGPT, Claude, Gemini shipped without it. No keystroke restores previous state. Branching (March 2026 ChatGPT change) is heavyweight navigation not undo. Industry making same retrofit pattern as memory and search: heavyweight solution instead of lightweight primitive.

## Key Patterns & Concepts

- **Undo Lineage**: Tesler/Mott Gypsy (modeless), Apple HIG (1987), Norman (forgiveness), Nielsen (heuristic), Victor (reversibility)
- **Cmd+Z Success**: Most successful keystroke in personal computing history; works without tutorial, settings, menu
- **Current AI Products**: Generate paragraph, press Cmd+Z—nothing happens; regenerate button forward not backward
- **No Undo Properties**: Must: take back action, cost one keystroke, restore previous state, no confusion
- **User Workarounds**: Cmd+A→Cmd+C reflex (copy before action); screenshot reflex (save visual before next click)
- **Branching Not Undo**: Heavyweight, deliberate, navigational; requires knowing affordance exists, finding UI, deciding branch preservation
- **Undo Properties**: One keystroke, syntactic level output, no navigation cost; reversibility output level not just conversation
- **Four Load-Bearing Properties**: Reversibility at output level; one-keystroke ambient access; stack semantics (multiple undos); visibility (persistent affordance)
- **Stack Semantics**: Linear stack not branching tree; users press Cmd+Z until reaching desired state continuing from there
- **Visibility Matters**: Persistent affordance saying "you can come back" reduces screenshot reflex and Cmd+A→Cmd+C anxiety
- **Design Decisions Not Technical**: All four properties are design decisions platforms could ship in quarter
- **Deeper Failure**: Inheritance of messaging-app skeleton; retrofit creative-tool affordances late and partially; model-centric design ignoring interface augmentation

## Related

[[the-forgotten-conversation-problem-ai]]
[[the-ux-of-ai]]
[[ai-product-ux-debt]]
