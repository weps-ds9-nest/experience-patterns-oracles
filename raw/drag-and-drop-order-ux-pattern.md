Title: Drag and Drop Order UX Pattern

URL Source: https://commadot.com/drag-and-drop-order-ux-pattern/

Published Time: 2021-09-24T18:53:21+00:00

Markdown Content:
This has been covered pretty extensively, but I often find myself wanting to have some stuff compiled for easy access.

Drag and drop patterns are different depending on what you are doing, but I generally put them into two camps.

### Grid drag-drop

The two most obvious examples are a spreadsheet and a Tree. GMail uses this method for some situations as well. The reordering has the following characteristics.

*   The original row stays put but is highlighted in some way
*   The drop target is indicated by a single stroke (vertical or horizontal depending on row or column dragging.)
*   No 3D effect or animation

[![Image 1](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/reorder-spreadsheet-columns.gif?resize=446%2C312&ssl=1)](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/reorder-spreadsheet-columns.gif?ssl=1)

Reorder column in Google Sheet

Another example of this is a tree.

[![Image 2](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/34426768-d1126e6c-ebee-11e7-9122-47e82cd8bd10.gif?resize=573%2C353&ssl=1)](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/34426768-d1126e6c-ebee-11e7-9122-47e82cd8bd10.gif?ssl=1)

Reorder in a tree

You should use this style of dragging and dropping when your content is in a structure that 3D would be confusing. This is especially true in a table. Removing a row or a column would be potentially strange.

### Content drag-drop

This alternative is more immersive and is used for moving cards and other kinds of content. It has the following characteristics:

*   The original item is removed from the stack completely
*   The dragged item is moved towards the user in the z-dimension
*   As the user drags, it moved content out of the way and makes room for the new content.
*   Animation is not always used, but enhanced the effect.

The gold standard of this is Trello. When introduced, this was a breath of fresh air. The little tilt of the item was perfect and made the entire reorder operation feel comfortable, obvious, and clear.

[![Image 3](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/Trello-Butler-Done-Drag-1.gif?resize=1024%2C512&ssl=1)](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/Trello-Butler-Done-Drag-1.gif?ssl=1)

Trello – The gold standard. Notice to tilt.

My favoite JavaScript example is [Beautiful Reorder Demo](http://chenglou.github.io/react-motion/demos/demo8-draggable-list/) using [React Motion](https://react.rocks/example/React-motion_reorder_list)

[![Image 4](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/image-3.png?resize=290%2C319&ssl=1)](http://chenglou.github.io/react-motion/demos/demo8-draggable-list/)

React Motion

The animation is gorgeous and makes me happy just playing with it. It is the example I use when I want to introduce sorting of complex content into any application.

Some people may see the animation as a waste of engineering resources, but I think that the UX benefits far outweigh the cost. UX is a huge advantage if you put in the little details like this. It will increase task completion, loyalty, and brand identity. Don’t skimp on the UX! (Says the UX guy!)

### The cursor

In both techniques, you should change the cursor when you hover something sortable. The hand open/close is best. I used this in Marketo in 2007. Worked great! I stole it from the Netflix queue UI.

[![Image 5](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/w7o3l.gif?resize=268%2C140&ssl=1)](https://i0.wp.com/commadot.com/wp-content/uploads/2021/09/w7o3l.gif?ssl=1)

Use the hand cursor

### Research

*   [Nielsen Norman article](https://www.nngroup.com/articles/drag-drop/)
*   [Alex Reardon Medium article](https://medium.com/@alexandereardon/rethinking-drag-and-drop-d9f5770b4e6b)
*   [Grace Noh UXDesign article](https://uxdesign.cc/drag-and-drop-for-design-systems-8d40502eb26d)
*   [The 7 Commandments of DnD Interfaces](https://uxstudioteam.com/ux-blog/drag-and-drop-interface/)

Did I miss anything?
