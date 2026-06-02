Title: Article from medium.com

URL Source: https://smry.ai/https:/medium.com/designing-atlassian/designed-for-delight-built-for-performance-da836950e78d

Markdown Content:
In order to help promote consistency in what we design and what we ship to our users, we created Pragmatic drag and drop tooling for Figma. Having Figma tooling enables our designers and engineers work with the same visual design language. The modular nature of Pragmatic drag and drop posed a challenge for our Figma outputs, so we focused on simplicity over fidelity. We knew it would be challenging to create a rich drag and drop prototype in Figma that would just ‘work’ — instead, we broke the components down into each part and state of the drag process. We also recorded Looms to provide guidance on how to show the different stages of a drag experience.

By working closely together, we were able to ensure that the implementation decisions designers and engineers would come to make would look and feel great for our users, while providing valid alternatives and escape hatches to account for any scenario.

## Designing within constraints

Leveraging the browser’s built-in drag and drop primitives comes with a lot of performance benefits, but it also comes with some fairly painful design constraints. For example, you cannot control the opacity or box shadow on the drag preview (the picture that the user moves around during a drag).

The native drag preview has a built in opacity of about 0.95 and a box shadow that cannot be disabled

Knowing that we were unlocking huge performance benefits when leveraging the web platform, we decided we would design affordances that would play well within the constraints.

One way we leaned into the constraints was by deciding to simplify drag previews, so they only contained crucial information. This constraint actually resulted in a better outcome that was more usable and accessible, since we reduced the amount of information that was being dragged by columns or rows.

The goals of Pragmatic drag and drop helped to guide our visual outputs. Wanting to make a solution that was fast encouraged us to create visual affordances that require a small amount of code and are easy for the browser to render. Our desire for flexibility pushed us towards adopting simple patterns that work well for a large amount of use cases.

[**react-beautiful-dnd**](https://github.com/atlassian/react-beautiful-dnd) is an older solution of ours for drag and drop that demonstrates a more complex approach:

A board interface powered by react-beautiful-dnd

*   Relies on movement to communicate placement
*   Relying on movement works well for lists and lists of lists, but the pattern does not work well for other types of interfaces.
*   This type of pattern can also feel slow at times as you have to wait for animations to finish before parsing the interface and continuing.

Using movement to communicate placement in a tree experience

We can start to feel the limitations of this pattern with structures that are not flat lists. It can be hard to know what a drag operations will do ahead of time in a tree when whitespace is the only indication of change.

Let’s now look at the design language we have gone for with **Pragmatic drag and drop:**

*   Leverages lines, borders and background color changes to communicate placement.
*   A lack of animations helps makes the interface feel snappy.
*   Works well for almost experience.
*   If a particular experience doesn’t work well with these affordances, then we can create alternatives — with every experience only including that code it needs for that experience.

Using borders, background colors and lines to communicate placement in a tree experience

Lines, borders and background colors lets us have extreme amounts of flexibility in how we communicate what is being achieved.

## A great experience for every user

Accessibility has to not just be a consideration but an integral part of any design decision. We have created a robust set of patterns that allow people leveraging assistive technologies to achieve all the same outcomes as a drag and drop operation.

A diagram showing how we think assistive technologies can be used to trigger outcomes

Drag and drop is a visual, pointer-based interaction that not everyone can perform at all times. We spent a long time trying to understand how we could translate this into a delightful and powerful interaction for every user.

In the past, we would have solved this by trying to create a closer relation between pointer-based movements and keyboard interactions, but in research for Pragmatic drag and drop we landed on a different idea that was simple, yet powerful:

> _Rather than trying to get assistive technologies to perform_ drag and drop operations _, we should enable assistive technologies to achieve the same_ outcomes _in a delightful way._

An outcome could be something like “move this issue from ‘to do’ to ‘in progress’”. Some users might achieve that outcome with a pointer based drag and drop operation, but we can also enable users to achieve the same outcome using controls and flows that are common and friendly for assistive technologies.

One of the main patterns are using to help provide a great experience for assistive technology users is the adding of action menu to draggable entities which includes menu items that allow all movement outcomes to be achieved

An item with a dropdown menu. The dropdown menu contains actions, such as “Move to top” and “Add label”

This approach gives us the flexibility to use different approaches for some experiences, as well as to potentially add a number of different approaches for different types of assistive technologies.

We have created [accessibility guidelines and outputs](https://atlassian.design/components/pragmatic-drag-and-drop/accessibility-guidelines) for our makers to help them add accessible outcomes to any experience.

## You can benefit from our work as well

We hope you enjoy using Pragmatic drag and drop through our products. We have also released Pragmatic drag and drop as an [open source project](https://github.com/atlassian/pragmatic-drag-and-drop) that you can use it to power drag and drop in your own applications too. You are welcome to use our design guidelines and accessibility guidelines as well, but we have decoupled the behaviour of Pragmatic drag and drop from its design and accessibility outputs, so you can use Pragmatic drag and drop with your own visual language and approach to accessibility.

This article was written by

[Alex Reardon](https://medium.com/u/ea5e41121e55?source=post_page---user_mention--da836950e78d---------------------------------------)

, 
[Lewis Healey](https://medium.com/u/89c3169fa65f?source=post_page---user_mention--da836950e78d---------------------------------------)

, Melissa Jaén and 
[Maria Christley](https://medium.com/u/d32eda7e73af?source=post_page---user_mention--da836950e78d---------------------------------------)

.
