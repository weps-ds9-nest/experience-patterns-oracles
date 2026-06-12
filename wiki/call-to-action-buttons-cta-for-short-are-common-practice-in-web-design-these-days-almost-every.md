# Call to Action buttons (CTA, for short) are common practice in web design these days, almost every website you enter have a _“log in”_ button or a _“try now”_ or _“learn more”_ button, those buttons are called Call to Action because they nudge the user to make a certain action.

Call to Action buttons (CTA, for short) are common practice in web design these days, almost every website you enter have a _“log in”_ button or a _“try now”_ or _“learn more”_ button, those buttons are called Call to Action because they nudge the user to make a certain action.

An example for a CTA Button, if you intuitively tried to click it, it worked.

These buttons normally come after a paragraph of text or some video and they are usually the only clickable thing, short of a menu, above the fold, meaning you don’t need to scroll and find them, they lead the user to the path of least resistance, which means most users will just click on them without thinking about it.

The problem with this approach is that it doesn’t scale. The power of the CTA button is that it’s the only one thing to click, so how can you make multiple CTAs in a website? how can the user know which one to click?

As everything else in web design, the answer is part design and part good writing, the user should instinctively know which button to click by their labels and good writing should make both distinct, not the generic _“Sign in”_ and _“Sign up”_ because it’s too confusing, _“Create an Account”_ and _“Log in”_ are a much better option.

But let’s talk about the design part of it, because that’s more fun, so how do we make multiple CTA buttons? The answer isn’t to just make 2 identical buttons as seen below.

Confusing, isn’t it?

## Button Design

Buttons on the web (and in apps, too) are usually not a one-of design, normally the designer will design a few button designs and all the buttons in the project will follow those rules, so we can’t just change anything we want, these rules are often a part of a Design System of Brand Guidelines designed to cover all the different design elements in a given project.

Buttons normally have those traits in common: font style, font size, font color, button color, button size, borders, rounded corners, drop shadow or glow effects, hover state and animations.

If we try to change too many of these traits, the buttons might feel too foreign to the general design of the project, and in this case the user will just click the most distinct one, and we’re basically back to just one CTA button.

Seems those buttons come from two different projects.

Another example, those aren’t any better.

I want to give a formula for getting the secondary CTA button right, but the truth is it’s very dependent on the specific project, it’s all about context, the buttons should feel similar enough to be a part of the same project and to register as buttons.

On the other hand, the buttons should be different enough to represent two distinct paths the user can choose from, for example the user knows if he or she already have an account, the user will know if he or she is ready to download or they want to learn more.

As a rule of thumb, I would say you should design your CTA buttons identical but **change up to 2 traits** from the list mentioned above, mostly color changes work best in my opinion.

I think this works, even though the colors are almost the same.

This has the benefit of different colors, which might be a privilege your brand doesn’t have.

The 2 traits change shouldn’t become a solid rule, because some changes are technically more traits but your user will still perceive them as one trait, the example below is technically a 3 traits change: button color, border color, and font color, but the user can just perceive those buttons as “invert” state of each other, even though a designer can easily say it’s not the case.

technically 3 traits change button color, border color, and font color.

## Google and Apple’s Guidelines

I like to always check Google and Apple’s Guidelines when I can, both companies have excellent design guidelines and both make products we all use every day, so their guidelines are something we’re all used to by now, between them they cover almost every design problem I can think of, including multiple buttons.

> _“…when using multiple buttons, indicate the more important action by placing it in a contained button (next to a text button).”_**— Google Material Design Guidelines**

That means that you should make one button a text-only button, it could be accompanied by an icon, but no actual button shape to contain it, so it’s obvious to the user which button is more “ _important_ “, or more ingrained to the process or pipeline of the app.

Google’s Material Design Guidelines, which get used widely on Android apps and Google products.

Google’s Guidelines gives us another option to make two buttons, this time both contained but in a varying level of emphasis, notice the bordered button isn’t as pronounced.

> _“…when using multiple buttons, you can place a outlined button (medium emphasis) next to a contained button (high emphasis).”_**— Google Material Design Guidelines**

Google’s Guidelines give us another option, if we want them both to be contained buttons.

You can read Google’s Guidelines here: [Buttons- Material Design](https://material.io/design/components/buttons.html#hierarchy-placement)

Apple’s macOS Guidelines are a bit different, they go a step further with not only thinner border (as Google did) but also a monochrome color palette, so the colored button really stands out.

> _“A default push button is prominent in appearance and automatically performs its action when the user presses Return. There can only be a single default button in a view”_**— Apple’s macOS Human Interface Guidelines**

That means that if we have multiple buttons, the one that is not the “single default button” should be less prominent in appearance, the visual example we get on a mac is something like this:

Apple’s macOS Guidelines inspired buttons.

Read Apple’s macOS guidelines here: [Apple’s Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/macos/buttons/push-buttons/)

Apple’s iOS, on the other hand refers to multiple buttons either as _“Buttons”_ or as _“Segmented Controls”_, _“Buttons”_ should be broken apart into the two corners of the screen (left and right), as _“Segmented Controls”_ should have at least three of them and they should be all touching each other, you can see the differences in the examples below:

iOS “Buttons” are for two conflicting options and separated by the app or screen title, notice the “Back” button is not as bold as the “Next” button signaling the user which one of them is the path to complete his action.

iOS “Segmented Controls” used for in-app options and is clearly marking where we are in the process.

Both options Apple gives us for iOS are not really CTA buttons because the iOS guidelines are meant for App Development and not Web Development, but I think it’s still worth to know their App guidelines because their design solution here is very interesting.

Read all of Apple’s iOS guidelines here: [iOS Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/controls/buttons/)

## Hover States

Hover states are the state an element transforms to when the mouse cursor “hovers” on it, usually a button will change state to indicate it is clickable, CTA buttons should behave the same in their Hover states, unless you have a custom animation for Hover, in that case you can tweak it for a second CTA button, but keep in mind that even if it’s different, it should provide a similar feeling to the user.

Simple hover state animations, notice the color change to a lighter color, not a blue-er color.

This is another example for a simple hover state, both CTA buttons get the same hover animation.

Sometimes our design calls for a more fancy animation, that’s what I’d call a custom animation, but in the case of the example below duplicating the same hover animation twice just seem lazy.

Lazy duplicated hover states, this animation seems too custom to duplicate.

Much better, the second button rotation was flipped and now both animations seem custom.

## Summary

In conclusion, multiple CTA buttons should be carefully examined, they should work together but be distinct enough to signal the user each represents a different path, they should differ from one another in about one or two traits and should never compromise the design or our brand guidelines.

This isn’t a rule though, you can change more than two traits, just keep in mind that the buttons should appear similar to the user, so try not to over design one of them while the other stays too simple, they should still appear to be from the same project or same design system.

There isn’t a “one size fits all” solution here, but I prefer to either change the button color or to “invert” the logical colors of the second button, now should the more important button be on the left or on the right?

That’s a question for a different time.

This is my preferred solution, but every project is different and there isn’t a “one size fits all” solution.

_Originally published at_[_https://uxdesign.cc_](https://uxdesign.cc/button-differentiation-done-right-5553605ea08a)_on June 13, 2019._

## Related
[Add wiki-links manually or run update_wikilinks.py]