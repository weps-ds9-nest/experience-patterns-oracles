# Buttons 103 Button States

## Because it is not always about emotional state

Image showcasing button states

Keeping users involved and in the loop is a crucial part of delivering an intuitive, user-centric experience. Button states are a vital component whenever we’re designing digital interfaces and design systems. They keep not only the designer informed but, more importantly, communicate all the actions available to the user, making each action easily distinguishable.

Button states, as the name suggests, show the state of the button before, during and after the action. This feedback helps users understand what actions they’re conducting and the state they’re currently in.

This is the fourth article in this series, so if you haven’t read the previous article, what are you waiting for? [Go check it out!!!](https://medium.com/@laxmanradhin/everything-about-buttons-youll-ever-need-to-know-be359612161f). Let’s begin.

## Default State

The very first and the foundational button state.

It denotes that a button or setting is interactive and ready for user engagement. When a button is in this state, it’s available to be clicked or tapped, and will perform its intended action.

The design of the button should be legible and accessible to all users. This is critical because all other button states are derived and created from this default state.

The default state is the most important button state, as many primary actions are initiated through it. It’s a vital part of the overall design system and **sets the tone for user interactions across one’s entire product.**

## Disabled State

[https://www.nngroup.com/articles/button-states-communicate-interaction/](https://www.nngroup.com/articles/button-states-communicate-interaction/)

A state that indicates a button is **not currently available for interaction**. It communicates when a component or element isn’t interactive and prevents users from taking actions that aren’t possible at that moment.

The disabled state should feel muted, inert, and de-emphasised. This effect is usually signalled through **muted colours, reduced opacity, or reduced elevation**. The visual treatment should clearly signal “not available” without confusing users.

One of the most popular methods of styling disabled buttons is to lower their opacity, but be very careful, as this approach is tricky to handle. It works well for buttons with similar default styles, but can create problems when a disabled button has more saturated colours than its neighbouring active buttons. The contrast can make it unclear which button is actually disabled.

Though understated, **a disabled button should still be legible.**

## Hover State

[https://www.nngroup.com/articles/button-states-communicate-interaction/](https://www.nngroup.com/articles/button-states-communicate-interaction/)

The hover state communicates when a user has placed a cursor above an interactive element. It **activates when the user moves their cursor over the button, providing immediate visual feedback.** A slight delay of around **150–200ms** should be added to this state to prevent the colour change from happening when users don’t mean to hover over a button

Typical **_hover_** states have a **slight darkening of the background colour** compared to the enabled state. There is also a **change of the cursor from an arrow to a hand.**

This subtle microinteraction goes a very long way in creating an intuitive user experience. The hover effect gives users a clear signal about the interactivity of buttons before they click. It brings components to life and makes interfaces feel responsive and engaging.

> **Important note:** Don’t make the mistake of creating a hover state for buttons in digital interfaces, like tablets and mobile devices, where the primary interaction is through touch. So if you’re designing exclusively for these devices, you don’t need to worry about this state

## Focus State

[https://www.nngroup.com/articles/button-states-communicate-interaction/](https://www.nngroup.com/articles/button-states-communicate-interaction/)

Focused states are crucial when designing for accessibility, as screen readers and keyboard navigation rely on focus states for visually impaired users or those with limited mobility. This state helps **users know which****interactive element currently has keyboard focus.**

The focused state communicates when a user has highlighted an element using a keyboard or voice command. It shows exactly where the user is on the page without requiring a mouse. When a user presses the Tab key to move across various interactive elements on a page, the focus state indicates which element is currently selected and could be activated by pressing the Enter key.

If your user has poor fine motor skills, they may need to use keyboard navigation to move through your interface. The user will press Tab to move from one interactive element to the next, which is why there needs to be a clear focus state for buttons to show “this is clickable, but not clicked yet.”

**The focus state should appear within 100–150 milliseconds** after the user uses the keyboard. This timing prevents the user from tabbing again and accidentally skipping past their desired button.

Another example of a focus state is when you click on an input field. When you start typing, only the focused input field will populate with text — the focus state establishes the context for your actions.

**The default focus state is the blue outline or ‘glow’** that you’ve undoubtedly seen during your internet explorations. While functional, many designers customise this to match their brand while maintaining accessibility standards.

## Pressed State

[https://www.nngroup.com/articles/button-states-communicate-interaction/](https://www.nngroup.com/articles/button-states-communicate-interaction/)

The pressed state communicates a user click, tap, or press. It activates **when a user initiates contact with a button through a cursor, keyboard, or voice input method.**

This is the momentary state when the **user’s cursor or finger is actively holding down on the button**. **The pressed state should appear within 100–150 milliseconds for the user to register that the pressing action is instantaneous**. If this feedback isn’t timely, users may press the button multiple times, potentially causing errors or duplicate actions. When the user releases their finger or cursor over the button, the action registers as complete and the button is ‘clicked’.

Pressed states are usually **denoted through darker colours or inner shadows to skeuomorphically represent that the button is being depressed, just like physical buttons.**

As mentioned earlier in the [article](https://medium.com/@laxmanradhin/everything-about-buttons-youll-ever-need-to-know-be359612161f), buttons on digital interfaces are imitations of real physical push buttons. This design choice gives users that familiar, lifelike experience of pressing an actual button, creating an intuitive connection between digital and physical interactions.

These are the few standard states that designers are expected to include and know. However, there are additional states I haven’t mentioned in this article, such as selected state, clicked state, active state, and loading state, among others.

I would love to hear from you about what you think of this article. What button states did I miss that you find essential? Where can I improve? Is the content helpful, and what should I include or exclude in future pieces? This is just me documenting my learning journey, so any insights from your side would be incredibly valuable.

Until next time, bye-bye!

## Related
[Add wiki-links manually or run update_wikilinks.py]