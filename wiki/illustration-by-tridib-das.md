# Illustration by Tridib Das

Illustration by Tridib Das

Gone are the days where websites are a collection of images and static assets. Today, web and mobile experiences are significantly more interactive than ever before, and as designers, we need to accommodate for that.

Understanding how to design for these [micro-interactions](https://xd.adobe.com/ideas/principles/human-computer-interaction/how-micro-interactions-can-enhance-the-user-experience/) with UI elements can help you add value to your product, and improve the end-user experience. In this guide we’ll explore how to use button states to create interactive elements in your design.

![Image 1: A selection of button styles, shapes and interactive states.](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031626-0.png)

## What are States?

Before we can cover how to design for states, we should define what they are. States refer to the different forms an element can take based on the context that it is being used in. Take for example a non-dimming light-switch; the switch has two states, on and off, and in each state it looks different. The same applies to something like a toggle switch in a UI, where an ‘on’ state may be represented by a green fill, and off with a grey.

![Image 2: A button has distinct states when toggled on (green fill) and off (grey fill).](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031627-1.png)

States aren’t just limited to static ‘toggle’ states though, and in today’s world of powerful front end languages, they’re interactive and evolving.

## Types of button states in interfaces

To understand what types of states are used in interface design, let’s focus on buttons – a very common element used for interactivity in UI design. Buttons can have several states as they’re one of the most highly interacted-with elements in a UI. The following states are common CSS button states used in web development.

*   **Default**: How the button looks when it isn’t being interacted with, but is available to be interacted with. This could also be called the ‘Normal’ state.

*   **Hover**: The hover state is specific to web design as mobile devices don’t typically support a hover interaction. This is the state that a button will be in as the mouse cursor rolls over the button on the screen. This is a helpful state in indicating that something can be interacted with as the cursor moves around the screen.

*   **Focus**: The focus state is important for [accessibility](https://xd.adobe.com/ideas/principles/web-design/a-quick-intro-in-web-accessibility/). Though many styles don’t draw attention to this state today, it’s presence is crucial for highlighting buttons as someone uses ‘tab’ to navigate a website. Often you’ll see this state as a light blue outline around a button or clickable object, but this varies depending on browser defaults.

*   **Active**: The active state is also often underutilized. The active state can be used for the ‘click’, or down press of a button, and may often resemble the look of a ‘pressed’ button.

*   **Disabled**: This state signifies that a button is not available for interaction. This is used if a process is loading as a way of blocking action, or in situations where the action is tied to a premium feature that requires upgrade before use. In both cases it should be paired with a tooltip to describe why the action is unavailable.

*   **Loading / Processing**: The loading state is used when an action has been taken and the system is ‘working’ to process that. For example if a page is saving, or a file is being uploaded, often the button will turn into a loading state where text changes, and a progress spinner appears. This can often be paired with the disabled state to prevent duplicate action.

The types of states may vary depending on the elements you’re designing. For instance, an input field will also have focused, hover, and disabled states, but may also include states for empty fields, error states, and others.

## Designing button states

When designing the states for your buttons, and other UI elements, it is important to keep in mind the purpose that state is serving so you can design accordingly. Start with your default button state, this is likely the version you have mapped out in your designs. If you haven’t designed a button yet, this [tutorial will get you up to speed with buttons in your design.](https://xd.adobe.com/ideas/process/ui-design/button-design-integration-ui/)

To get started, it can be helpful to map out all of your button states side by side on an artboard so that you can see how they relate to each other. You’ll also want to do this for other button types (primary, secondary etc).

![Image 3: A visual matrix that illustrates a range of button states for a set of primary and secondary buttons.](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031628-2.png)

From here you can start to style your states, keeping in mind conventions and common patterns for each common state, this will vary depending on the style of your site.

### Hover state

The hover state should be designed to indicate that a button state is clickable. Common hover state styles are darkening / lightening the background fill color or changing the [elevation](https://material.io/design/environment/elevation.html#default-elevations) or position of a button.

![Image 4: A hover state applied to a default button darkens the button color fill.](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031628-3.png)

### Focus state

The focus state of a button traditionally follows a standard pattern of an outline around the button. Since this state is focused around accessibility it can be helpful to follow convention to make it easier to understand. Most modern browsers have a default focus state, and where possible should be left in-tact. In Chrome this is a blue outline that looks something like this.

![Image 5: A focus state applied to a default button with green fill adds a blue outline.](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031628-4.png)

### Active state

The active state is often under-used but serves a helpful purpose in ‘flat’ style UI design. With a variety of input devices, mice, trackpads, it is not always clear when you have made a ‘click’ action. Using the active state you can design subtle visual clues that a button has been clicked.

Try adding a darker border, and darkening the background fill slightly to give the effect that a button is being pressed into the page. You can also use scaling to reduce the button size slightly, to further reinforce the effect.

![Image 6: An active state applied to a default button adds a darker border and darkens the fill.](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031629-5.png)

### Disabled state

The disabled state of a button should be designed to articulate that an action is not available at the moment. Therefore you don’t want the disabled state to look active. A common technique is reducing opacity to make a button look less prominent. You don’t want to change the colors and style of button as you may risk it being confused for another button type. But by reducing the opacity you can reduce the button’s prominence. Also removing any box-shadows or elevation will help relay the message.

![Image 7: A disabled state applied to a default button lowers the opacity to reduce the button's prominence.](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031630-6.png)

### Loading state

A common approach to the loading or processing button is the introduction of an icon, often animated, in unison with the button label. Using a spinner or loading icon that rotates while processing takes place will indicate that an action is in progress.

![Image 8: A loading state applied to a default button introduces an animated spinner icon.](https://xd.adobe.com/ideas/wp-content/uploads/2021/07/1618031630-7.png)

## Things to keep in mind

When working with button design, and designing states for these interactive UI elements, it’s important to remember a few things.

*   **Follow common conventions** – Buttons are a highly interactive, and common UI element. There are expectations users have for how they behave and function. Avoid reinventing the wheel too much to avoid confusion.

*   **Keep consistent with your style**– Drastically straying from the style of your website, product or brand can make your button states feel foreign to the experience you’re creating. Keep states within your brand constraints.

*   **Test your states** – Don’t forget the importance of testing, even for something as seemingly small as button states. Understanding how people react, and interact with your states can make a large impact to how they experience your product.

*   **Avoid complex animations –**Simple animations and transitions can add value to your states, making it clear that you’re moving between states. However, using complex CSS animations, spins, and fancy effects can distract from the intent of the action.

Just like with buttons, states can be applied to many elements in your UI to make it feel dynamic, provide valuable user feedback in the application, and direct audiences to the destinations and actions you intend for them to take. Take caution, and design these interactions intentionally to ensure the best result.

![Image 9](https://xd.adobe.com/ideas/wp-content/uploads/2020/01/image1-wpcf_90x90.jpg)

Words by 

 Matt Rae

Designer Advocate for Adobe XD

Matt Rae is a Designer Advocate for Adobe XD. Coming from nearly a decade in product design, across travel, autonomous vehicles, EdTech and advertising technology, he’s now focused on equipping designers with resources to design the best experiences using the XD platform. He has a passion for user experience, and developing the design community.

## Related
[Add wiki-links manually or run update_wikilinks.py]