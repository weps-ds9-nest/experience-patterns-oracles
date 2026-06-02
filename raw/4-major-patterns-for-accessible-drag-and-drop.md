Title: Article from medium.com

URL Source: https://smry.ai/https:/medium.com/salesforce-ux/4-major-patterns-for-accessible-drag-and-drop-1d43f64ebf09

Markdown Content:
## Describing an Interaction for Assistive Technology Users

Let’s briefly focus on the needs of assistive technology users and the type of information they need in order to successfully complete a task. The basic fundamentals of making any interaction accessible for both keyboard and screen reader users comes down to providing 3 basic pieces of information: identity, operation, and state.

For these drag and drop patterns, we will use all three techniques described in my article on [Describing Complex Designs](https://medium.com/salesforce-ux/how-to-describe-complex-designs-for-users-with-disabilities-ba05f5224130): Native Controls, WAI-ARIA, and Live Regions with Hidden Text.

### Using ARIA Live Regions to Communicate Operation, Identity, and State

To relay status and in some cases, operational instructions information to the user, we will primarily use [ARIA live regions](https://www.w3.org/TR/2011/CR-wai-aria-20110118/states_and_properties#attrs_liveregions). Live regions are a great tool for updating the status of a drag and drop operation, because of how they can be used to jump text to the front of “the queue” of a screen reader.

Screen reader users typically hear text as they navigate a web page or application. There are several ways in which a screen reader navigates the page, but all of the text they encounter is added to the end of the screen reader’s queue, and is relayed to the user on a first in, first out basis.

Live regions are a tool for placing text into the queue without needing the user to navigate to that text on the page. There are two types of live regions: _polite_ and _assertive_.

*   _Polite_ regions place text at the end of the screen reader’s queue
*   _Assertive_ regions place text right at the front of the queue

For the purposes of drag and drop, we’ll need to use an assertive region so the user hears an update immediately. To begin, place the following span with the accompanied CSS on your page at page load. The contents placed in this span will be immediately read out loud to screen reader users. It is visually hidden from sighted users.

```
.assistive-text {
  position: absolute;
  margin: -1px;
  border: 0;
  padding: 0;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}<span aria-live=”assertive” class="assistive-text"> </span>
```

The second part is a piece of code that will both clear the contents of the _<span>_ and place new text inside. Each time new text is placed inside of the span, the information is immediately read to screen reader users.

```
updateLiveText (String announcement) {
 //code to update text to our aria-live span 
}
```

## Putting it all Together: 4 Accessible Patterns for Drag and Drop

With this in mind, along with the other techniques discussed in [Describing Complex Designs](https://medium.com/salesforce-ux/how-to-describe-complex-designs-for-users-with-disabilities-ba05f5224130), we’re ready to explain our 4 types of accessible drag and drop.

### Pattern #1: Sorting a List

For this example we are going to change the order of a list. We will allow the ARIA _listbox_ role to describe the arrow key navigation for the list itself and our hidden region with _aria-live_ to describe the drag and drop operation.

```
<span aria-live="assertive" class="assistive-text"></span><span id="operation" class="assistive-text">
  Press Spacebar to reorder
</span><ol role="listbox">
  <li role="option" draggable="true" aria-describedby="operation" 
      tabindex="0">
    Ice Cream
  </li>
  <li role="option" draggable="true" aria-describedby="operation" 
      tabindex="-1">
    Pie
  </li>
  <li role="option" draggable="true" aria-describedby="operation" 
      tabindex="-1">
    Cake
  </li>
  <li role="option" draggable="true" aria-describedby="operation" 
      tabindex="-1">
    Cupcake
  </li>
</ol>
```

When a user tabs to our list, their focus will be placed on the first list item, Ice Cream. They will learn a few things in terms of _Identity_.

**_“Listbox. 1 of 4. Ice Cream. Press Spacebar to reorder.”_**

*   They are interacting with a listbox, which [implicitly tells users](http://w3c.github.io/aria-practices/#Listbox) they can navigate the list with the arrow keys.
*   The number of items in the list.
*   The currently focused item is “Ice Cream”.
*   The hidden text, “Press Spacebar to Reorder”, tells the user that reordering the list is a possibility.

**Now our user presses the spacebar.** We must provide instructions as to the _operation_ and the _state_ of this drag and drop interaction.

`updateLiveText("Ice Cream, grabbed. Current position in list: 1 of 4. Press up and down arrow keys to change position, Spacebar to drop, Escape key to cancel.");`
This call to the live region will provide three pieces of information:

1.   Confirmation that we have grabbed the Ice Cream item.
2.   The position in the list where Ice Cream currently resides.
3.   Details on how to operate the drag and drop control using the keyboard, including how to cancel the operation.

**Now our user presses the down arrow key.** The “Ice Cream” item is moved down one step in the list.

`updateLiveText("Ice Cream. Current position in list: 2 of 4.");`
At this point, the users wants to drop the item and **presses the spacebar key**.

`updateLiveText("Ice Cream, dropped. Final position in list: 2 of 4.");`
The interaction is complete. This live text update confirms the final state:

1.   The item has been dropped.
2.   The item is now in position 2 of 4.

If our user was to **press the escape key** and cancel the operation we would say something such as:

`updateLiveText("Ice Cream reorder cancelled.");`
[Try out sorting a list on our example site](https://salesforce-ux.github.io/dnd-a11y-patterns/#/sortB).

We are going to use a very similar approach for our next popular drag and drop interaction model.

### Pattern #2: Interacting with an Object on a Canvas

Tools such as Photoshop, Illustrator, Sketch, OmniGraffle and PowerPoint work on the premise that a user can move or resize objects on a canvas. While they may lack accessibility and screen reader support, all of these tools allow users to move or nudge these objects using a keyboard. The operation is fairly typical: select the object somehow and move it around using the arrow keys. Here is how we make this interaction accessible within a web application.

**Moving and Object Around A Canvas** Consider our canvas to be a 20 x 20 grid. The top left corner is cell 1, 1. The cell to the right of that is cell 1, 2. To the right of that is 1, 3 and so on. The second row starts at 2,1 and goes from there.

A 20 x 20 grid with no objects

In the example below, we have two objects on the canvas. Both objects are 5x5 cells in size. They are sitting next to each other side by side. Object A is positioned with its top left corner in cell 1,1. Object B is situated in cell 1,6.

The same grid but with two 5x5 objects

From here on out, we are going to use the same techniques as in the pattern #1 (Sort a List) to inform our user as to the identity, operation, and state of this drag and drop interaction.

Consider how we can inform a screen reader user as to the current state of a 2-dimensional drag and drop operation.

Let’s start by moving Object B two spots over to the right. Our user will **press the tab key** until their focus is placed on the grab handle for Object B.

```
<span id="operation" class="assistive-text">
  Press Spacebar to Grab
</span><div>
  <span>Object A</span>
  <button aria-describedby="operation">
   <svg aria-hidden="true">...</svg>
   <span class="assistive-text">Move Object A</span>
  </button>
</div><div>
  <span>Object B</span>
  <button aria-describedby="operation">
   <svg aria-hidden="true">...</svg>
   <span class="assistive-text">Move Object B</span>
  </button>
</div>
```

Our user then **presses the spacebar** to grab Object B.

`updateLiveText("Object B grabbed, Current position starts: Row 1, Column 6. Use the arrow keys to change position of the top left corner on canvas, Spacebar to drop, Escape key to cancel.");`
User **presses the right arrow key** once.

`updateLiveText("Row 1, Column 7.");`

Object B moved one position to the right.

User **presses the right arrow key** again.

`updateLiveText("Row 1, Column 8.");`
User **presses the spacebar** to drop the object.

`updateLiveText("Object B dropped, Final position: Row 1, Column 8.");`

Object B moved to Row 1, Column 8.

**Dragging An Object From A Palette To The Canvas** Many canvas based tools start with a object palette and a mouse user drags objects from the palette onto the the canvas. How would we change this to incorporate that behavior? The answer is we wouldn’t, as we would consider this two separate operations. The first being a simple key press or click on the palette to add an object to the canvas. New objects could start at 1, 1 as in our example above. The second operation would be our accessible drag and drop for final positioning.

**Resizing An Object On A Canvas** What if we wanted to resize our objects? What sort of information would we need to know and what sort of reference point would we need?

Given that we reserved the top left corner as a reference point for an object’s position, let’s use the bottom right corner for resizing. Staying with our example from above, let’s stretch the size of Object A so that it sits neatly abutting Object B. Let’s again begin by tabbing to the element that will be resized.

Focus is on Object A’s drag handle

First, our user then **presses the spacebar** to grab the resize handle for Object A.

`updateLiveText("Resize Object A, Current size: 5 cells wide by 5 cells tall. Press Right arrow to make wider, Left arrow to make narrower, Down arrow to make taller, Up arrow to make shorter, space bar to finish, Escape key to cancel.");`
Our user **presses the right arrow key** once.

`updateLiveText("Width: 6, Height: 5.”);`

Object A increased in size by one cell in width

Our user **presses the right arrow key** again.

`updateLiveText("Width: 7, Height: 5.");`

Object A increased in size by another cell in width

Our user **presses the spacebar** to drop the complete the resize..

`updateLiveText("Object A Resize Complete, New size: 7 cells wide by 5 cells tall.");`
There you have it, accessible drag and drop to resize. Depending on whether or not objects may overlap, you will have to provide information about adjacent objects as they may have shifted position.

Resize operation completed

[Try out these canvas patterns on our example site](https://salesforce-ux.github.io/dnd-a11y-patterns/#/canvas).

### Pattern #3: Moving an item from one list to another list

Let’s say you have a series of lists, and you want to move an item from one list to another. At this point, order within the list isn’t important. This is common in Kanban type products where users want to sort records by status.

Sample Kanban

In this example, we will only be moving items from one list to another. We will not be reordering any of the lists, but consider how you can user pattern #1 (Sorting a List) to combine techniques.

We are going to use a [WAI-ARIA accessible menu](http://w3c.github.io/aria-practices/#menu) as our means of moving an item to another list. To begin with, the user will tab to the grab handle for movable item.

```
<h2>Desk</h2>
<ul>
  <li draggable="true">
    <span>Phone</span>
    <button aria-haspopup="true">
      <svg aria-hidden="true">...</svg>
      <span class="assistive-text">Move Phone</span>
    </button>
  </li>
  <li draggable="true">
    <span>Phone Charger</span>
    <button aria-haspopup="true">
      <svg aria-hidden="true">...</svg>
      <span class="assistive-text">Move Phone Charger</span>
    </button>
  </li>
</ul><h2>Backpack</h2>
<ul>
  <li draggable="true">
    <span>Notebook</span>
    <button aria-haspopup="true">
      <svg aria-hidden="true">...</svg>
      <span class="assistive-text">Move Notebook</span>
    </button>
  </li>
  <li draggable="true">
    <span>Pencil</span>
    <button aria-haspopup="true">
      <svg aria-hidden="true">...</svg>
      <span class="assistive-text">Move Pencil</span>
    </button>
  </li>
  <li draggable="true">
    <span>Hand Sanitizer</span>
    <button aria-haspopup="true">
      <svg aria-hidden="true">...</svg>
      <span class="assistive-text">Move Hand Sanitizer</span>
    </button>
  </li>
</ul><h2>Pocket</h2>
<ul>
  <li draggable="true">
    <span>Keys</span>
    <button aria-haspopup="true">
      <svg aria-hidden="true">...</svg>
      <span class="assistive-text">Move Keys</span>
    </button>
  </li>
  <li draggable="true">
    <span>Wallet</span>
    <button aria-haspopup="true">
      <svg aria-hidden="true">...</svg>
      <span class="assistive-text">Move Wallet</span>
    </button>
  </li>
</ul><h2>Recycling Bin</h2>
<ul>
</ul>
```

The _aria-haspopup=“true”_ on our buttons will tell screen reader users that these buttons will trigger a menu.

First, our user **tabs to the the move button in the object** they want to move and hears the following:

**_“Move Phone, Button, Has popup.”_**

Our user then **presses the spacebar**, which opens an accessible menu.

Menu open on the Phone record.

They can then use the arrow keys, to choose which List to place their record in and press the Enter key to finish the operation. In our example, we are moving Phone from the list, Desk, to the Recycling Bin.

Phone now in the Recycling Bin

Since menu interaction is standardized by the WAI, there is no need to describe its operation using a live region. This is handled by the browser and the screen reader.

[Try out moving items between lists on our example site](https://salesforce-ux.github.io/dnd-a11y-patterns/#/bucket).

### Pattern #4: Resizing an Object in 1 Dimension

Say you want to resize the width of a table column. A mouse user grabs onto the little space between “Name” and “Role” and drags left to right.

Dragging the width of a column

Generally, these grab handles are just _<div>_ tags that are used for the mouse operation. Instead, let’s use a native HTML element that already provides us identity, operation and state. By doing so, screen reader users will receive updates in real time, as they interact with the control. Developers would not have to use any ARIA, including a live region, because the browser would already communicate identity, operation, and state to the user.

Behold the humble range input.

`<input type="range" min="1" max="100" value="70">`

A simple 

Let’s place this input inside of the header cell and hide it using our assistive-text class. Additionally, let’s use _aria-label_ to describe the input instead of a separate _<label>_. This way the input’s label is not included by a screen reader when a cell’s heading is announced.

`<input class="assistive-text" aria-label="Width of Column A" type="range" min="1" max="100" value="50">`
Now our user can tab to the input and interact with it as they would any other range slider, by using the left and right arrow keys. This is the standard keyboard interaction for a range input.

Note that we create a visual focus state on the grab handle when the input is in focus. Also note how the user is told that they are interacting with a slider and given the current size.

Column slider is in focus. VoiceOver says, “150, Width of Name Column, slider, table 3 columns, 4 rows”

Our user **presses the right arrow key**.

User presses the right arrow key. VoiceOver says, “160”

Notice how the status is continuously delivered to the screen reader user as they press the arrow keys. This is all baked into the _<input type=“range”>_ element.

[Try out resizing a column on our example site](https://salesforce-ux.github.io/dnd-a11y-patterns/#/resize).

As you build drag and drop interactions, consider the type of drag and drop that you are creating and make the best experience for your users. Sometimes you will need hidden _aria-live_ regions, other time you can use WAI-ARIA patters, and sometimes you can even use native HTML.

_Jesse Hausler (@jessehausler) and Cordelia McGee-Tubb (@cordeliadillon) are Accessibility Specialists at Salesforce._
