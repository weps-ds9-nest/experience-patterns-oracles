# 4 Major Patterns for Accessible Drag-and-Drop

Drag-and-drop interactions are critical in modern applications, but inaccessible implementations exclude assistive technology users. Making these interactions accessible requires communicating three essential pieces of information to screen readers: identity, operation, and state. Four core patterns emerge: list sorting, canvas object manipulation, list-to-list transfers, and custom interactions—each using ARIA live regions to announce changes immediately.

## Key Patterns & Concepts

- **ARIA Live Regions**: Use assertive regions to place announcements at front of screen reader queue for immediate announcement
- **Three Information Layers**: Always provide identity (what), operation (how), and state (status) to users
- **Pattern 1: Sorting a List**: Reorder list items with spacebar grab/drop and arrow key navigation; announce position changes
- **Pattern 2: Canvas Object Manipulation**: Move and resize objects on grid-based canvas with keyboard; reference positions using grid coordinates
- **Pattern 3: List-to-List Transfers**: Move items between lists while maintaining accessible announcements of source/destination
- **Pattern 4: Custom Interactions**: Hide complex drag mechanics behind simple button-and-keyboard workflows
- **Keyboard Alternatives**: All drag operations should have keyboard equivalents; avoid relying on mouse-only interactions
- **Grab and Drop Model**: Separate selection from drag operation; use spacebar to grab, arrows to navigate, spacebar to drop

## Full Article

Accessible drag-and-drop requires providing assistive technology users with three basic pieces of information: identity, operation, and state. The solution uses ARIA live regions to relay status and operational instructions.

### ARIA Live Regions Strategy

Screen reader users hear text as they navigate. All text encountered is added to the end of the screen reader's queue (FIFO). Live regions bypass this, placing text right at the front of the queue through "assertive" regions, so users hear updates immediately.

### Pattern 1: Sorting a List

When a user tabs to a list item with a grab handle and presses spacebar, they should hear: "Item Name, grabbed. Current position: 1 of 4. Use arrow keys to change position, spacebar to drop, Escape to cancel."

As they press down arrow: "Item Name. Current position: 2 of 4."

When they press spacebar to drop: "Item Name, dropped. Final position: 2 of 4."

If escape is pressed: "Item Name reorder cancelled."

### Pattern 2: Canvas Object Manipulation

For 2D canvases, reference positions using grid coordinates (Row, Column). When grabbing Object B at Row 1, Column 6, announce the position. As users press right arrow, update: "Row 1, Column 7." When dropped, confirm final position.

For resizing, use bottom-right corner as resize reference. Announce current size (width x height) and provide directions: "Use right arrow to make wider, left arrow to make narrower, down arrow to make taller, up arrow to make shorter."

### Pattern 3: List-to-List Transfers

Transfer items between lists (source and destination) while maintaining clear announcements of operation phases and final position in new list.

### Pattern 4: Custom Interactions

For interactions that don't map to standard drag-drop, separate the selection phase (button click) from the positioning phase (keyboard navigation). New objects start at default position (e.g., canvas top-left) and users navigate to final position using arrow keys.

## Related

[[accessible-design-patterns]]
