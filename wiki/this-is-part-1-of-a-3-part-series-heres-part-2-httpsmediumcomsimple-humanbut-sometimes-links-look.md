# _This is part 1 of a 3-part series. Here’s_[_part 2_](https://medium.com/simple-human/but-sometimes-links-look-like-buttons-and-buttons-look-like-links-9b371c57b3d2)_and_[_part 3_](https://medium.com/@adambsilver/buttons-shouldnt-have-a-hand-cursor-part-2-4a6e1c8423a5)_._

_This is part 1 of a 3-part series. Here’s_[_part 2_](https://medium.com/simple-human/but-sometimes-links-look-like-buttons-and-buttons-look-like-links-9b371c57b3d2)_and_[_part 3_](https://medium.com/@adambsilver/buttons-shouldnt-have-a-hand-cursor-part-2-4a6e1c8423a5)_._

There’s a belief that the hand (pointer) cursor means clickable, but this is wrong and potentially problematic.

### The hand does not mean clickable

It’s no accident that browsers don’t give buttons (and other elements) a pointer cursor — it’s because they’re not meant to. See the following screenshot:

Google’s search page on Chrome on Mac OS

Almost every element is interactive and clickable — the menu, the tabs, the whitespace, the browser buttons, the bookmark bar and Google’s search box—none of them have a pointer cursor**.**

There are more interactive and clickable elements not shown above: select menus, sliders, checkboxes, radios, labels, images, empty space (e.g right click — view source) and text — again, none of them have a pointer cursor.

The same applies for the operating system. You can tap, drag, select, press, left click and right click on a plethora of different elements including buttons. But, buttons aren’t signified by the pointer cursor showing on hover.

License Agreement is a link and gets the pointer cursor. Buttons don’t.

Perceived affordance is provided by the way something looks _regardless_ of the cursor. Remember, the cursor is only available when hovering with a pointing device such as a mouse.

This is why, for example, [checkboxes are never round](http://danieldelaney.net/checkboxes) (and radios are never square). This is also why links are typically underlined. **This is why links do, in fact, have a hand cursor.**

### What the authorities say

[Microsoft’s design guides](https://msdn.microsoft.com/en-us/library/windows/desktop/dn742466(v=vs.85).aspx) talk about weak affordance:

> Text and graphics links use a hand […] pointer […] because of their weak affordance. While links may have other visual clues to indicate that they are links (such as underlines and special placement), displaying the hand pointer on hover is the definitive indication of a link.
> 
> 
> **To avoid confusion, it is imperative not to use the hand pointer for other purposes.** For example, command buttons already have a strong affordance, so they don’t need a hand pointer. The hand pointer must mean “this target is a link” and nothing else.

[Apple’s Human Interface Guidelines](https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/OSXHIGuidelines/Pointers.html) states that the hand cursor should be used when “the content is a URL link”. [W3C User Interface guidelines](https://www.w3.org/TR/CSS21/ui.html#propdef-cursor) says the same thing again with “The cursor is a pointer that indicates a link”.

### The hand cursor is for links

The hand (and often underlined text) signifies a link. Links are not buttons. Links came along with the web. To help users understand that they are different, they are given the hand cursor. It serves as an extra clue. Here’s why:

1.   Clicking a link opens a web page or resource.
2.   (On desktop) I can _right-click_ on a link and do many things (that I can’t do with a button). Open in new tab/window, save a link, copy address, add to reading list, bookmark it and more.
3.   (On mobile devices) I can tap and hold on a link and get a similar context menu as per the previous point.
4.   A link also tells me that I am _just_ going somewhere else. I am not [modifying any data or making changes](http://uxmovement.com/buttons/when-to-use-a-button-or-link/) in anyway (like a button is likely to do).

### Summary

When a button has the hand cursor, it subtly suggests that the user is interacting with a link when they’re not. If you want to give visual feedback when the user hovers, you can do so with other style changes such as background colour. A well-designed button does not need a hand cursor to help the user realise it does something.

The hand cursor is reserved for links. This is because they are unique in their behaviour. Browsers and Operating Systems have done the work for you — because contrary to popular belief — browsers know best.

Links have always been handled this way since the web came along — this is the convention of the web that you need not innovate on. You can rest easy knowing that browsers have you covered. This leaves you and your team to solve _real_ problems.

## Follow up posts

*   [But Sometimes Links Look Like Buttons](https://medium.com/simple-human/but-sometimes-links-look-like-buttons-and-buttons-look-like-links-9b371c57b3d2)
*   [Buttons Shouldn’t Have A Hand Cursor Part 2](https://medium.com/@adambsilver/buttons-shouldnt-have-a-hand-cursor-part-2-4a6e1c8423a5)

_By the way, I’m writing a book called Form Design Patterns. If you want to know when it’s released_[_subscribe here_](http://adamsilver.io/signup/)_and I’ll keep you posted._

## Related
[Add wiki-links manually or run update_wikilinks.py]