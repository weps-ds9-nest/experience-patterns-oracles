# Should I Use A Button Or A Link Ashlee M Boyer

## Table of Contents

1.   [Existing resources](https://ashleemboyer.com/blog/should-i-use-a-button-or-a-link#existing-resources)
2.   [How do buttons and links behave differently?](https://ashleemboyer.com/blog/should-i-use-a-button-or-a-link#how-do-buttons-and-links-behave-differently)
3.   [Why are buttons and links styled differently?](https://ashleemboyer.com/blog/should-i-use-a-button-or-a-link#why-are-buttons-and-links-styled-differently)
4.   [So what’s the answer?](https://ashleemboyer.com/blog/should-i-use-a-button-or-a-link#so-whats-the-answer)

One of the most seemingly contentious questions in web accessibility is whether or a button or link should be used when creating certain kinds of interactive elements. Why is it so contentious? The question has been answered countless times over the years by accessibility experts. There is also a wealth of reference documentation that answers the question.

The answer is straightforward, and I think it’s only contentious when there is lack of consideration of why links and buttons both look different and behave in completely different ways.

## Existing resources

Before reading the rest of this article, I highly recommend reading the wealth of knowledge that’s already out there. Here’s a list a small list to get you started:

*   [Links vs. Buttons in Modern Web Applications](https://marcysutton.com/links-vs-buttons-in-modern-web-applications) - Marcy Sutton
*   [On Link Underlines](https://adrianroselli.com/2016/06/on-link-underlines.html) - Adrian Roselli
*   [Why are hyperlinks blue?](https://blog.mozilla.org/en/internet-culture/deep-dives/why-are-hyperlinks-blue/) - Elise Blanchard
*   [Revisiting why hyperlinks are blue](https://blog.mozilla.org/en/internet-culture/why-are-hyperlinks-blue-revisited/) - Elise Blanchard
*   [Guidelines for Visualizing Links](https://www.nngroup.com/articles/guidelines-for-visualizing-links/) - Jakob Nielsen
*   [Formatting Links for Usability](https://baymard.com/blog/formatting-links-for-usability) - Baymard Institute
*   [Interaction Cost](https://www.nngroup.com/articles/interaction-cost-definition/) - Raluca Budiu
*   [Long-Term Exposure to Flat Design: How the Trend Slowly Decreases User Efficiency](https://www.nngroup.com/articles/flat-design-long-exposure/) - Kate Moran
*   [Beyond Blue Links: Making Clickable Elements Recognizable](https://www.nngroup.com/articles/clickable-elements/) - Hoa Loranger
*   [Improving text readability for dyslexic users with skip-ink underlines](https://medium.com/@iamhiwelo/improving-text-readability-for-dyslexic-users-with-skip-ink-underlines-bf52a2f3426b) - Damien Senger
*   [Accessible Links Re:visited](https://www.filamentgroup.com/lab/a11y-links.html) - Maggie Wachs
*   [How To Use Underlined Text To Improve User Experience](https://www.smashingmagazine.com/2017/12/underlined-text-improve-ux/) - Nick Babich
*   [HTML5 Accessibility Chops: Just use a (native HTML) button](https://www.tpgi.com/html5-accessibility-chops-just-use-a-button/) - Steve Faulkner

## How do buttons and links behave differently?

First, it’s important to understand how buttons and links differ. I’ve seen them mistakenly conflated and oversimplified as elements that “perform an action”. And while they both enable a user to perform different actions, that doesn’t make them the same element.

We’ll answer the question of differing behavior by reading some bits of [the HTML Living Standard](https://html.spec.whatwg.org/multipage/) and [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/).

The HTML Living Standard also talks about the `<link>`, `<area>`, and `<form>` elements in the context of links, but we won’t discuss those here since they have different purposes than the `<a>` element.

### About Links

The HTML Living Standard has [an entire section dedicated to links](https://html.spec.whatwg.org/multipage/links.html#links). Here’s the paraphrased definition provided by that document:

> Links are a conceptual construct that represent a connection between two resources.

It goes on to say there are two types of links: [links to external resources](https://html.spec.whatwg.org/multipage/links.html#external-resource-link) and [hyperlinks](https://html.spec.whatwg.org/multipage/links.html#hyperlink). Let’s look at some examples of each.

#### Links to external resources

Links to external resources are resources outside of the current site. These can be denoted by setting the `rel` property to `"external"`, and then they can also have unique styling applied to them using a CSS attribute selector like `a[rel="external"]`. As an example, you might choose to append the text “(external link)” to every link with `rel="external"`. This can be done with CSS like this:

```
a[rel="external"]::after {
  content: " (external link)";
}
```

You can also apply special styles to to links with `target="_blank"`. In the following example, the text “(opens in new tab)” is appended to the link to give users a warning that multiple context changes will happen when the link is activated.

```
a[target="_blank"]::after {
  content: " (opens in new tab)";
}
```

This is related to [Success Criterion 3.2.5: Change on Request](https://www.w3.org/TR/WCAG21/#change-on-request), which says:

> Changes of context are initiated only by user request or a mechanism is available to turn off such changes.

It’s important to warn users that context will change with an action for many reasons. Some users may not be able to detect changes in context because of cognitive limitations or visual, reading, or intellectual disabilities. For users with limited motor control, unexpected and unwanted context changes will cause extra effort on their part to get back to where they were.

It’s best to give users all the information they need to make an informed and empowered decision for themselves.

#### Hyperlinks

Hyperlinks are links to resources within the current site. Here are some examples:

*   Links to another location on the current page, such as a table of contents having a link to a heading element
*   Links to another page in the site, such as linking to a related blog post from another
*   Links to downloadable files that are intended to be used later, rather than immediately

According to the HTML Living Standard, there are several values for the `rel` property on `<a>` elements that designate the element as a hyperlink: [alternate](https://html.spec.whatwg.org/multipage/links.html#rel-alternate), [author](https://html.spec.whatwg.org/multipage/links.html#link-type-author), [bookmark](https://html.spec.whatwg.org/multipage/links.html#link-type-bookmark), [help](https://html.spec.whatwg.org/multipage/links.html#link-type-help), [license](https://html.spec.whatwg.org/multipage/links.html#link-type-license), [next](https://html.spec.whatwg.org/multipage/links.html#link-type-next), [prev](https://html.spec.whatwg.org/multipage/links.html#link-type-prev), [search](https://html.spec.whatwg.org/multipage/links.html#link-type-search), and [tag](https://html.spec.whatwg.org/multipage/links.html#link-type-tag).

I don’t include this long list of values because I think it’s important to know each one. I include it so it’s more obvious just how much functionality is handled by native `<a>` elements. You may have heard that you can apply `role="link"` to `<button>` elements when you want to turn them into links, but it’s just not enough.

There is a major loss in functionality by not using a native `<a>` element when you want to render a link, and this one property we’ve discussed only brushes the surface. The first rule of ARIA is extremely important to note here:

> If you can use a native HTML element or attribute with the semantics and behaviour you require already built in, instead of re-purposing an element and adding an ARIA role, state or property to make it accessible, then do so.

#### The `link` ARIA role

We have one more topic to cover for defining links, and that’s [the `link` ARIA role](https://www.w3.org/TR/wai-aria-1.2/#link). `link` is the default role for `<a>` elements. Here’s how the role is defined:

> An interactive reference to an internal or external resource that, when activated, causes the user agent to navigate to that resource.

There is also a note that reads:

> If pressing the link triggers an action but does not change browser focus or page location, authors are advised to consider using the button role instead of the link role.

With all of the information we have covered so far, I think we can move forward with the following definition for links: An element that connects two resources and does one of the following when activated: downloads the linked resource, changes the browser focus to another part of the page, or changes the browser’s location to another page.

### About Buttons

Let’s move on to defining buttons. We’ve already seen a little bit of information that tells us buttons are different from links, but let’s look for some more so we’re well equipped for inevitable future buttons vs. links debates. [The HTML Living Standard](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element) does not give us as much non-technical information about buttons as it does about links, so I’ll rely on the MDN Web Docs and WAI-ARIA 1.2 Specification for definitions.

#### The `<button>` element

The MDN Web Docs [definition for the Button element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button) reads:

> The `<button>` HTML element is an interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it then performs a programmable action, such as submitting a form or opening a dialog.

_Shameless plug: [I wrote this definition](https://github.com/mdn/content/pull/13834) back in March of 2022. 🥳_

Take a look at the [long list of attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button#attributes) the button element accepts:

*   autofocus
*   autocomplete
*   disabled
*   form
*   formaction
*   formenctype
*   formmethod
*   formnovalidate
*   formtarget
*   name
*   type
*   value

That is _a lot_ of functionality. This list should serve as another reason why it’s not a good idea to mix and match the `<a>` and `<button>` elements. Just applying `role="button"` to `<a>` elements is no where near enough to make the anchor elment match the native implementation of the button element. In fact, just changing a `role`[does not change the look or behavior](https://www.w3.org/TR/using-aria/#role-not) of an element at all if you’re not using assistive technology.

#### The `button` ARIA role

The WAI-ARIA 1.2 Specification says [the `button` role is](https://www.w3.org/TR/wai-aria-1.2/#button):

> An input that allows for user-triggered actions when clicked or pressed. […] Buttons are mostly used for discrete actions. Standardizing the appearance of buttons enhances the user’s recognition of the widgets as buttons […].

This says that buttons are typically used to perform a single action at a time. It also says that users benefit from their appearance being standardized, so they are recognizable as an interactive element.

There’s one supported ARIA state for the `button` role that the `link` role does not have. That state is [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed). It communicates the “pressed” state of toggle buttons. This is not a quality of a `<a>` elements. It’s another example of just how much buttons and links differ from one another.

#### The `Button` WAI-ARIA Widget

The [ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/about/) is a useful for resource for learning about accessibility semantics and keyboard interfaces. It has several examples of commonly used widgets. It also includes resources on common practices.

One of its widget examples is [the Button widget](https://www.w3.org/WAI/ARIA/apg/patterns/button/). Right after defining the widget and naming two additional supported button types (toggle and menu), it calls out the importance of distinguishing links and buttons:

> The types of actions performed by buttons are distinctly different from the function of a link. It is important that both the appearance and role of a widget match the function it provides.

It also notes that sometimes links have the visual style of a button, but it says there’s still a better solution: adjust the design.

> Nevertheless, elements occasionally have the visual style of a link but perform the action of a button. In such cases, giving the element role button helps assistive technology users understand the function of the element. However, a better solution is to adjust the visual design so it matches the function and ARIA role.

### Comparing Links and Buttons

By now, we should have a pretty good idea how different links and buttons are. I’ll still list a few more examples of differences:

*   Did you know the mouse cursor for buttons and links are different? The mouse cursor for a `<a>` element on hover is `pointer`. For the `<button>` element, it’s the default/auto cursor. Read Adam Silver’s [Buttons shouldn’t have a hand cursor](https://medium.com/simple-human/buttons-shouldnt-have-a-hand-cursor-b11e99ca374b) for more background.
*   A native `<button>` is always reachable with the keyboard, even if its role is `link`. A native `<a>` is only reachable by keyboard if it has the `href` attribute defined, even if its role is `button`. This means you have extra work to do to make the keyboard interface work if you decide not to use the native elements for their intended purposes.
*   User agents and assistive technology provide navigation lists containing different types of elements. One example of this is [the VoiceOver rotor on Mac](https://support.apple.com/guide/voiceover/with-the-voiceover-rotor-mchlp2719/mac). Buttons are listed under “form controls”, and links are listed under “links”. If an element is not coded in a way it can be recognized by assistive technology, then users won’t be able to navigate a page as they normally should. This is not a failure of screen readers. Native elements are already compatible, so use them!
*   User agents and assistive technology also provide commands and gestures for interacting with different types of elements. Not using native elements can interfere with this functionality and cause users to be confused and frustrated. This is not a failure of screen readers. Native elements are already compatible, so use them! 
    *   For example, VoiceOver has a command for “find the next visited link”. This command will not recognize `<button>` elements with `role="link"`.

How many more user agent or assistive technology features are broken by poorly coded elements? I don’t know. Do you want to test every single one and find out? I highly doubt it. Just use native HTML elements!

Remember the first rule of ARIA use:

> If you can use a native HTML element or attribute with the semantics and behaviour you require already built in, instead of re-purposing an element and adding an ARIA role, state or property to make it accessible, then do so.

And don’t forget the second rule of ARIA use:

> Do not change native semantics, unless you really have to.

The native semantics are present for a reason. I promise no one put them there to make your software development life more difficult. They’re there to make websites usable by everyone. You want more users, right? You want them to be happy and impressed with your hard work, right? :)

## Why are buttons and links styled differently?

There are [four principles of accessibility](https://www.w3.org/WAI/WCAG21/Understanding/intro#understanding-the-four-principles-of-accessibility) that inform how we must build the web and content for it. You can remember them with the acronym POUR: information and interfaces must be Perceivable, Operable, Understandable, and Robust. The Web Content Accessibility Guidelines (WCAG) are organized under these 4 principles. I’m not taking a deep dive into all of them here, but if you want to start on your own the latest standard is [WCAG 2.1](https://www.w3.org/TR/WCAG21).

Anyways, what does the look of buttons and links have to do with [four principles of accessibility](https://www.w3.org/WAI/WCAG21/Understanding/intro#understanding-the-four-principles-of-accessibility)? Well…

*   Before a user can **operate** an interface, they must be able to **perceive** what elements in it are interactive.
*   In order for a user to make informed decisions before they operate the interface, it must be **understandable**.
*   And in order for a user to operate the interface in many conditions and environments, it must be **robust**.

Here are some WCAG guidelines and success criteria relevant to this topic you may find insightful:

*   [Guideline 1.3: Adaptable](https://www.w3.org/WAI/WCAG21/Understanding/adaptable): Create content that can be presented in different ways (for example simpler layout) without losing information or structure. 
    *   [Success Criterion 1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships): Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text.
    *   [Success Criterion 1.3.6: Identify Purpose](https://www.w3.org/WAI/WCAG21/Understanding/identify-purpose): In content implemented using markup languages, the purpose of user interface components, icons, and regions can be programmatically determined.

*   [Guideline 2.1: Keyboard Accessible](https://www.w3.org/WAI/WCAG21/Understanding/keyboard-accessible): Make all functionality available from a keyboard. 
    *   [Success Criterion 2.1.1: Keyboard](https://www.w3.org/WAI/WCAG21/Understanding/keyboard): All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes, except where the underlying function requires input that depends on the path of the user’s movement and not just the endpoints.

*   [Guideline 2.4: Navigable](https://www.w3.org/WAI/WCAG21/Understanding/navigable)
    *   [Success Criterion 2.4.4: Link Purpose (In Context)](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context): The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context, except where the purpose of the link would be ambiguous to users in general.
    *   [Success Criterion 2.4.9: Link Purpose (Link Only)](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-link-only): A mechanism is available to allow the purpose of each link to be identified from link text alone, except where the purpose of the link would be ambiguous to users in general.

*   [Guideline 2.5: Input Modalities](https://www.w3.org/WAI/WCAG21/Understanding/input-modalities): Make it easier for users to operate functionality through various inputs beyond keyboard. 
    *   “Often, people use devices that offer several input methods, for example, mouse input, touch input, keyboard input, and speech input. These should be supported concurrently as users may at any time swich preferred input methods due to situational circumstances, for example, the availability of a flat support for mouse operation, or situational impediments through motion or changes of ambient light.”

*   [Guideline 3.2: Predictable](https://www.w3.org/WAI/WCAG21/Understanding/predictable)
    *   [Success Criterion 3.2.2: On Input](https://www.w3.org/WAI/WCAG21/Understanding/on-input): Changing the setting of any user interface component does not automatically cause a change of context unless the user has been advised of the behavior before using the component.
    *   [Success Criterion 3.2.5: Change on Request](https://www.w3.org/WAI/WCAG21/Understanding/change-on-request): Changes of context are initiated only by user request or a mechanism is available to turn off such changes.

*   [Guideline 4.1: Compatible](https://www.w3.org/WAI/WCAG21/Understanding/compatible): Maximize compatibility with current and future user agents, including assistive technologies.

## So what’s the answer?

I think most people already know the answer to this question, and many of those who scour the internet for a different answer are looking for “permission” to do something they “unconventional”. But to end on a very clear note:

*   **Use an anchor element** when you need to connect two resources, and one of the following needs to happen when the element is activated: 
    *   download the linked resource
    *   change the browser focus to another part of the page
    *   change the browser’s location to another page

*   **Use a button element** when you need enable a user to perform a programmable action, such as submitting a form or opening a dialog.

## Related
[Add wiki-links manually or run update_wikilinks.py]