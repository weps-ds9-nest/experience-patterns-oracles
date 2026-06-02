# Beautiful Interactions: Crafting Elegant Drag-and-Drop Animations

Drag-and-drop interactions should feel like moving physical objects without snapping behavior breaking visual language. Moving between lists challenged elegant animation design through placeholder collapse issues and item shifting conflicts. Solution: insert placeholder at list end instead of original position, instantly shift items downward in same browser update creating visual stillness, animate placeholder close only when dragging over foreign list (no item impact), and never let animations fight each other. Key insight: avoid scenarios where animations cancel each other out; instead architecture interactions so all movements work in harmony toward smooth, non-jarring experience.

## Key Patterns & Concepts

- **No Snapping**: Visual language of physical object movement requires continuous motion; snapping breaks immersion
- **Placeholder Strategy**: Insert at list end instead of item's original spot; allows smooth closing without impacting surrounding items
- **Instant Offsetting**: Shift items downward same browser update when dragging started; creates visual position maintenance
- **Avoid Animation Conflicts**: Never let expansion/collapse animations fight item shift animations; causes jittering
- **Three-Phase Architecture**: Lift (remove from flow, insert placeholder), Move (reposition items), Drop (finalize placement)
- **Foreign List Pattern**: Different logic for list item entered—allows clean interaction patterns avoiding home list chaos
- **Home List vs Foreign List**: Distinct interaction patterns; home list behavior simpler when placeholder at end
- **Virtualization**: Only visible items shifted improving performance with large lists
- **Announcement Phase**: Grab → Position → Drop states clearly announced for screen reader users
- **Performance Considerations**: Shifting large item sets potential performance issue; virtualized displacement solution
- **Error Prevention**: Communicating home list identity without snapping when dropped outside lists

## Full Article

Open source library aiming providing beautiful, accessible drag-and-drop experience for lists (react-beautiful-dnd). Goal: provide drag-drop experience feeling like dragging physical objects. Avoid interactions where something immediately **snaps** from place to another. **Snapping** breaks physical object moving visual language—not how physical objects behave.

Most interactions achieve no snapping. However, still interaction containing snapping: **moving between lists**. Detailed journey toward removing snapping when moving between lists. As turned out, making experience elegant and robust, **lot** needed doing.

### Terminology

- 🏠 **home list**: list dragging item started in
- ✈️ **foreign list**: list dragging item didn't start in
- **placeholder**: space inserted into list

### Challenge 1: Shifting Items in Home List

When item dragged, other items move making room for dragging item.

Here's how items behaved in **home list:**

**Step 1: Lift** 🏋️♀️
- Dragging item (A) removed from document flow; space normally collapse
- Placeholder instantly inserted A's location maintaining space and stopping list collapse
- B and C untouched

**Step 2: Moving Down** ↓
- Placeholder remains in A's original place
- B shifted upwards with transform making room for A
- C untouched

**Step 3: Moving to Foreign List** →
_Things start going badly_

- Placeholder inserted foreign list making space for A
- 🔥 Placeholder in home list animates closed
- 🔥 B's transform upwards reversed counteracting collapsing placeholder trying keeping B visual spot at list top
- C still untouched but shifted up by placeholder closing in home list

Counteracting collapsing placeholder animation led B jittering. Expanding placeholder pushing B down while transform trying pulling B up. Even opposite animations caused jittering.

**Step 4: Moving Back into Home List** ←
_Things continue going badly_

- Placeholder removed foreign list
- 🔥 Placeholder in home list animates open in A's original spot
- 🔥 B applying transform shifting upwards being top list
- C still untouched but shifted down by placeholder expanding

Placeholder expansion clashing upward B shift caused bad animation experience.

### Alternative Interaction Pattern

Things work differently in foreign lists. Taking closer look at same interaction:

**Step 1: Lift** 🏋️♀️
- Dragging item (A) removed document flow
- Placeholder instantly inserted A's location maintaining space
- B and C untouched

**Step 2: Moving Over Foreign List** →
- Placeholder animates closed in home list
- Placeholder animates open foreign list end making space for A
- B and C shift down with transform

**Step 3: Moving Back to Home List** ←
- Placeholder animates closed foreign list
- B and C animate shift back up removing transform
- Placeholder animates open home list

### What Can Be Learned from Foreign List Pattern?

Foreign list displacement and placeholder pattern result no strange animations. Looks great. **Big thing noticing: no animations fighting each other**. In home list, scenarios existed placeholder expansion/collapse animations not working well running next item shifting up/down.

> Tip: avoid scenarios where animations try canceling each other out

### New Home List Pattern

Created new interaction pattern for home list based foreign list working.

**Step 1: Lift** 🏋️♀️
- Dragging item (A) removed document flow
- Placeholder inserted **at list end**; previously inserted A spot preventing collapse
- As A removed from document flow, space in list collapsed; everything after A **should move up**
- Same browser update, **everything after A instantly shifted down counteracting A collapse**; visually looks nothing moved 👨🎨

**Step 2: Moving Down** ↓
- Remove initial non-animated downward shift from B; removal causes B move up
- Placeholder remains list end
- C continues being shifted forward

**Step 3: Moving Over Foreign List** →
- Placeholder animates closed in home list; doesn't shift items as it's list end
- Remove initial non-animated downward shift from C causing upward movement; moves upwards due space created list by A removal when lifting
- Placeholder animates open foreign list end making space for A

**Step 4: Moving Back to Home List** ←
- Placeholder animates open **at home list end**; doesn't impact item placement
- Animate C movement downwards making room for A
- B untouched

### Beautiful Result 🌹

This new pattern overcomes animation issues caused previous home interaction pattern. Looking fantastic 😍.

## Related

[[accessible-dnd-salesforce]]
[[ui-microinteractions]]
[[animation-principles]]
