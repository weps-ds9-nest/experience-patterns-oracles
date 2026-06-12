# Rethinking Drag And Drop

## Taking something basic and making it beautiful

introducing react-beautiful-dnd

Drag and drop is an intuitive way of moving and rearranging things. We at Atlassian have recently released `react-beautiful-dnd` which makes drag and drop for lists on the web more beautiful, natural and accessible.

## Physicality

The core design idea of `react-beautiful-dnd` is physicality: we want users to feel like they are moving physical objects around. This is best illustrated through contrast — so let’s explore some standard drag and drop behaviour and how we have tried to do better.

jquery-sortable

> This example uses the amazing `jquery-sortable`. It’s drag and drop mechanism is fairly standard and serves as a good reference point.

### Movement

instant movement is standard

When dragging items around, other items disappear and reappear as needed. Also, when you drop an item it appears in its new home position immediately.

a more natural movement

For a more natural drag we animate the movement of items as they need to move out of the way while dragging to more clearly show a drags effect. We also animate the drop of an item so that it animates into its new home position. At no point is an item instantly moved anywhere — regardless of whether it is dragging or not.

### Knowing when to move

It is quite common for drag and drop interactions to be based on the position that user started the drag from

impact based on selection point

In this example the user is grabbing the top right corner of the first item. The user needs to drag a fair way down before the second item moves to its new position. This is because the calculations are based on the initial selection position of the user.

impact based on centre of gravity

In `react-beautiful-dnd` a dragging items impact is based on its centre of gravity — regardless of where a user grabs an item from. A dragging items impact follows similar rules to a set of scales ⚖️. Here are some rules that are followed to allow for a natural drag experience even with items of flexible height:

*   A list is _dragged over_ when the centre position of a dragging item goes over one of the boundaries of the list
*   A resting drag item will move out of the way of a dragging item when the centre position of the dragging item goes over the edge of the resting item. Put another way: once the centre position of an item (A) goes over the edge of another item (B), B moves out of the way.

## Accessible

Traditionally drag and drop interactions have been exclusively a mouse or touch interaction. `react-beautiful-dnd` ships with support for drag and drop interactions **using only a keyboard**. This enables power users to drive their experience entirely from the keyboard. As well as opening up these experiences to users who would have been excluded previously.

### Respecting the browser

In addition to supporting keyboard, we have also audited how the keyboard shortcuts interact with standard browser keyboard interactions. When the user is not dragging they can use their keyboard as they normally would. While dragging we override and disable certain browser shortcuts (such as `tab`) to ensure a fluid experience for the user.

## Carefully designed animations

With things moving a lot it would be easy for the user to become distracted by the animations or for them to get in the way. We have tweaked the various animations to ensure the right balance of guidance, performance and interactivity.

### Maximise interactivity

`react-beautiful-dnd` works really hard to avoid as many periods of non-interactivity as possible. The user should feel like they are in control of the interface and not waiting for an animation to finish before they can continue to interact with the interface.

### Dropping

When you drop a dragging item its movement is based on physics (thanks `react-motion`). This results in the drop feeling more weighted and physical.

### Moving out of the way

Items that are moving out of the way of a dragging item do so with a CSS transition rather than physics. This is to maximise performance by allowing the GPU to handle the movement. The CSS animation curve has been designed to communicate _getting out of the way_.

How it is composed:

1.   A warm up period to mimic a natural response time
2.   A small phase to quickly move out of the way
3.   A long tail so that people can read any text that is being animated in the second half of the animation

animation curve used when moving out of the way

## Plays well with others

We have done a lot of work to ensure that things work intuitively while providing flexibility.

### Sloppy clicks and click blocking

When a user presses the mouse down on an element, we cannot determine if the user was clicking or dragging. Also, sometimes when a user clicks they can move the cursor slightly — a sloppy click. So we only start a drag once the user has moved beyond a certain distance with the mouse down (the drag threshold) — more than they would move the mouse if they where just making a sloppy click. If the drag threshold is not exceeded then the user interaction behaves just like a regular click. If the drag threshold is exceeded then the interaction will be classified as a drag and the standard click action will not occur.

This allows consumers to wrap interactive elements such as an anchor and have it be both a standard anchor as well as a draggable item.

### Focus management

`react-beautiful-dnd` works hard to ensure that it does not impact the usual tab flow of a document. For example, if you are wrapping an _anchor_ tag then the user will still be able to tab to the anchor directly and not an element surrounding the anchor. We add a `tab-index` to draggable items to ensure that even you are not wrapping something that is usually interactive (such as a `div`) then the user will still be able to access it with their keyboard to drag it.

## Not for everyone

There are a lot of libraries out there that allow for drag and drop interactions within React. Most notable of these is the amazing `react-dnd`. It does an incredible job at providing a great set of drag and drop primitives which work especially well with the [wildly inconsistent](https://www.quirksmode.org/blog/archives/2009/09/the_html5_drag.html) html5 drag and drop feature. `react-beautiful-dnd`**is a higher level abstraction specifically built for vertical and horizontal lists**. Within that subset of functionality `react-beautiful-dnd` offers a powerful, natural and beautiful drag and drop experience. However, it does not provide the breadth of functionality offered by `react-dnd`. So this library might not be for you depending on what your use case is.

## Engineering

### Clean, powerful API

Before this library was released a lot of time an attention was given to crafting a declarative, clean and powerful api. It should feel really easy to get started with and provide the right level of control over the whole drag experience. It is based off a lot of research into other libraries as well as collective experience in building drag and drop products. I won’t go into all the details of the api here — but you can find a comprehensive guide [repo](https://github.com/atlassian/react-beautiful-dnd)

### Performance

`react-beautiful-dnd` is designed to be extremely performant — it is part of its DNA. It builds on prior investigations into React performance that you can read about [here](https://medium.com/@alexandereardon/performance-optimisations-for-react-applications-b453c597b191) and [here](https://medium.com/@alexandereardon/performance-optimisations-for-react-applications-round-2-2042e5c9af97). It is designed to perform the minimum number of renders required for each task.

**Highlights**

*   Using connected-components with memoization to ensure the only components that render are the ones that need to — thanks `react-redux`, `reselect` and `memoize-one`.
*   All drag movements are throttled with `requestAnimationFrame` — thanks `raf-schd`
*   Memoization is used all over the place — thanks `memoize-one`
*   Conditionally disabling `pointer-events` on all draggable items while dragging to prevent the browser needing to do redundant work — you can read more about the technique [here](https://www.thecssninja.com/css/pointer-events-60fps)
*   Non primary animations are done on the GPU

minimal amount of react updates

minimal amount of browser paints

### Tested

`react-beautiful-dnd` uses a number of different testing strategies including unit, performance and integration tests. Testing various aspects of the system helps to promote its quality and stability.

While code coverage is [not a guarantee of code health](https://stackoverflow.com/a/90021/1374236), it is a good indicator. This code base currently sits at **~95% coverage**.

### Typed

This codebase is typed with `flowtype` to promote greater internal consistency and more resilient code. It also provides for a greater developer documentation story as the whole api is typed.

## Final words

We think the web will be a more beautiful and accessible place because of `react-beautiful-dnd`. For more information and [examples](https://react-beautiful-dnd.netlify.com/) 🎉 head over to the [repository](https://github.com/atlassian/react-beautiful-dnd).

A huge thank you to everyone at Atlassian who made this possible

Cheers

### Blog translation

This blog has been [translated into Chinese](http://www.zcfy.cc/article/rethinking-drag-and-drop-alex-reardon-medium-4195.html) by [@leesirbupt](https://twitter.com/leesirbupt)! Enjoy!

## Related
[Add wiki-links manually or run update_wikilinks.py]