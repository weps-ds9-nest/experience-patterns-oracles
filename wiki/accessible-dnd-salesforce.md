# Accessible Drag-and-Drop Examples & Patterns

Salesforce UX has documented five core accessible drag-and-drop interaction patterns: interacting with canvas objects, resizing in one dimension, moving items between lists, and two list-sorting patterns. All use keyboard-accessible alternatives with ARIA live regions announcing state changes. The patterns demonstrate that drag-and-drop interactions needn't exclude assistive technology users when designed with intentional accessibility from the start.

## Key Patterns & Concepts

- **Canvas Interaction**: Move and resize objects on canvas using spacebar grab/drop and arrow keys; reference positions using grid coordinates
- **One-Dimension Resize**: Resize single dimension (e.g., column width) with drag or arrow keys; announce size changes
- **Multi-List Transfer**: Move items between lists with accessible affordances; announce source/destination for each move
- **List Sorting (Standard)**: Reorder list items using spacebar grab/drop and arrow key navigation; announce current position continuously
- **List Sorting (Listbox)**: Sort listbox options with arrow keys for selection, spacebar for drag mode, arrow keys for positioning, spacebar to drop
- **ARIA Live Regions**: Use assertive regions immediately announcing changes without forcing user navigation
- **Three Information Layers**: Always provide identity (what), operation (how), and state (status)
- **Keyboard Equivalents**: All drag operations have keyboard alternatives; spacebar grab, arrows navigate, spacebar drop
- **Announcement Strategy**: Immediate status updates (grabbed, position, dropped); operational instructions (press arrow keys, spacebar to drop, Escape to cancel)
- **Verified Accessibility**: Salesforce's patterns tested with assistive technology; patterns ensure screen reader users have same capabilities as mouse users

## Full Article

Drag-and-drop essential in modern applications but inaccessible implementations exclude assistive technology users. Making accessible requires communicating three information pieces to screen readers: identity, operation, and state.

### Five Interaction Patterns

**Pattern 1: Canvas Object Manipulation**

Move and resize objects on grid-based canvas. Reference positions using grid coordinates (Row, Column).

- **Moving**: Tab to object grab handle, press spacebar to grab, arrow keys to move, spacebar to drop
- **Resizing**: Tab to resize handle, spacebar to grab, arrow keys to resize, spacebar to confirm

Announce: "Object name grabbed, Current position: Row 1, Column 6. Use arrow keys to change position, spacebar to drop, Escape to cancel."

As user presses right arrow: "Row 1, Column 7."

When dropped: "Object name dropped, Final position: Row 1, Column 8."

**Pattern 2: One-Dimension Resizing**

Resize single dimension like column width. Drag handle or use arrow keys. Announce current size and directions for resize control.

**Pattern 3: Multi-List Item Transfer**

Move items between lists. Press item's Move button to open menu of available lists, arrow keys select list, Enter to drop, Escape to cancel. Announce source and destination clearly.

**Pattern 4: List Sorting (Standard)**

Reorder list items. Tab to item, spacebar enters drag mode, down/right arrows move down, up/left arrows move up, spacebar to drop, Escape to cancel.

Announce at each phase:
- Grab: "Ice Cream, grabbed. Current position in list: 1 of 4. Press up/down arrow keys to change position, spacebar to drop, Escape to cancel."
- Move: "Ice Cream. Current position in list: 2 of 4."
- Drop: "Ice Cream, dropped. Final position in list: 2 of 4."

**Pattern 5: List Sorting (Listbox)**

Sort listbox options. Arrow keys select option, spacebar enters drag mode, arrow keys reposition, spacebar to drop.

### Implementation Key

All patterns use ARIA live regions (assertive type) to immediately announce changes without requiring user navigation. This ensures screen reader users get instant feedback—critical for understanding drag-drop operations.

## Related

[[accessible-design-patterns]]
[[ui-design-patterns]]
