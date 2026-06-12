# Ui Cheat Sheets Buttons

## UI cheat sheets: buttons

Tess Gadd·18 min read·Jul 10, 2019

Clean article found smry-fast Reading stack medium.com · 2,990 words

The article is ready without leaving the reader. Source: Direct extraction.

My favourite design element is the buttons. In fact, I [insert swear word of your choice] love buttons. In this cheat sheet, we will go through different types of buttons, states, and interactions. For the purpose of this story, we will be ignoring radio buttons, tabs, checkboxes, and other types of buttons — we will just be looking at ‘normal’ buttons.

What we will cover in this cheat sheet:

1.   Button actions
2.   Common button styles
3.   Button colours & styling
4.   Button states and feedback
5.   Button labelling
6.   Touch targets
7.   Button positions
8.   Button hall of fame
9.   Closing thoughts

## 1. Button actions

In this section, we will look at the hierarchy of buttons and the language that they communicate. Button actions are not determined by how they look (although users should be able to learn what the buttons mean by their styling), but rather by how they are used.

### 1. Call to action (CTA / C2A)

A call to action button, depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do.

Call to action button

For CTA buttons I like to use rounded buttons as they are striking and eye-catching.

### 2. Primary action

While a CTA button and a primary button can look the same, I like to separate them out. While CTA buttons are what the interface would want you to do, primary buttons should be a strong visual indicator to help the user to complete their journey. Primary buttons should be used in situations where the user may want to go ‘next’, ‘complete’, ‘start’, etc.

Primary action button

For primary actions, I like to use solid buttons.

### 3. Secondary action

Secondary buttons are the ‘go back’ to the primary button’s ‘next’, or the ‘cancel’ button to the ‘submit’ button. Secondary buttons are the alternative we give users to the primary action.

Two variations of secondary actions next to primary ones.

I (and the rest of the internet) tend to use line buttons or text links as secondary buttons.

### 4. Tertiary action

Tertiary buttons are usually used for miscellaneous actions: the action is important, but may not be what the user is looking to do right then. This is things like ‘add friend’, ‘add new’, ‘edit’, or ‘delete’, provided that they aren’t a primary action.

Tertiary actions in different forms.

Generally speaking, one will use smaller or less prominent buttons style for this.

## 2. Common button styles

In this section, we will look at common button styles. The style is just the aesthetics of the button and not how it should be used.

### Solid buttons

Solid buttons are exactly what they sound like — they are buttons with a solid fill. Done.

A solid button.

### Line & ghost buttons

Line buttons are also exactly what they sound like: a button without a fill — just an outline. While often used interchangeably, I prefer to think of line buttons as being on a light colour (with a dark outline and text), and ghost button as being on a dark colour (with a light outline and text).

A line button (left) and a ghost button (right).

### Rounded buttons

Rounded buttons are buttons whose edges are set to the max rounded border-radius.

A rounded button.

**Side note:** Rounded buttons look horrible stacked. Every time you stack rounded buttons a UI Designer cries.

If you want to find out more about rounded buttons, I recently read [this](https://uxdesign.cc/make-sense-of-rounded-corners-on-buttons-dfc8e13ea7f7) story by

[Shan Shen](https://medium.com/u/637feb10787a?source=post_page---user_mention--7856ff90f544---------------------------------------)

about rounded buttons and can’t recommend it enough.

### FAB (Floating action button)

Floating action buttons are a clever design pattern, made popular by Google’s Material Design. While they may look like an icon button, they are actually used for the primary action on a screen.

A FAB button.

If you want to find out more about the FAB, I recommend checking out [‘Buttons: floating action button’](https://material.io/design/components/buttons-floating-action-button.html#) on Material Design’s site.

### Text link

Text links are a very simple button type. There are a couple of different ways to show that something is a link. This could be with a colour, or an underline, or the position of the link, or even just the text itself (e.g. “Read more”).

Text links styled differently.

When it comes to colour, most sites use blue, as it is the most identifiable as a link. And why is the classic text links ‘blue’ you may ask? It goes all the way back to Sir Tim Berners-Lee, is generally credited as the inventor of the World Wide Web (side note: imagine having ‘Invented the World Wide Web’ on your CV). While it appears that accessibility wasn’t on his mind when he chose the colour — the cool thing about blue is that even people with colour blindness can usually still see it.

**_Post published correction:_**_In the first publication, it was written that Sir Tim Berners-Lee was the ‘inventor of the internet’ when in reality he was the inventor of the World Wide Web. My bad and apologise for the miss information._

### Icon with a label button

Icon buttons have grown in popularity, but some buttons still need a label to ensure that the button communicates properly.

A button with an icon and a label.

The trickiest thing when dealing with icons and labels is figuring out how big to make the icon in relation to the font. Option 1: you make the icon’s size similar to the cap height of the font. Option 2: You make the icon’s size a lot bigger than the line height. A word of caution: if the icon is only a little bit bigger than the cap-height, it will look unbalanced or like a mistake. It should either be approximately the same cap-height, or a lot bigger — avoid inbetweens.

### Icon button

Icon buttons have no label and are only an icon. Because they don’t have a label, they save a lot of space in an interface. Icon buttons also allow you to stack other icon buttons next to them in a small space.

Icon buttons with different styles.

**A word of caution**: If you are designing products for people with low computer literacy, I would always recommend rather using a button with a label — especially for more abstract meanings.

### Icon with a text link

Some text links may have an icon with them. These usually don’t sit within a body of text.

Various icon with link buttons.

## 3. Button colouring and styling

When designing buttons, there are a couple of different elements to take into consideration.

### Colour

When designing for a product, you should always be thinking of people with impairments. To ensure that your colours are accessible by everyone, you can use an online contrast checker. [This](http://accessible-colors.com/) is the one I use.

Buttons with different colours.

Also, think about the colour language when choosing your colour palette. Having a red button, as opposed to a green button, may communicate a different message within the context.

A ‘Delete’, ‘See warnings’, ‘Save’ and ‘More’ Button.

For example, a green ‘delete’ button would cause confusion, as would a red ‘save’ button (unless you are Pinterest).

### 2. Border-radius

The border-radius is what gives buttons a lot of their personality (in my opinion). Sharp edge buttons look more serious, while buttons with a rounder radius look more playful.

Buttons with different border-radius settings.

**Side note:** as mentioned before, rounded buttons don’t look good stacked.

### 3. Shadow

The shadow on a button makes the button feel like it is sitting off the page and naturally brings attention to it. Shadows can also be used to indicate different states as well. [Material Design](https://material.io/design/environment/elevation.html#depicting-elevation) does this particularly well by making the button come ‘closer’ to you on hover.

Buttons with different shadow settings.

### 4. Label styling

The label styling comes down to the font and how easy is it to read. When choosing a font, make sure that it is legible.

Buttons with different label styles.

Here are a few easy wins to make a font readable:

1.   Choose sentence case or title case over uppercase. (This being said, Material Design does use buttons with uppercase labels.)
2.   Make sure the label colour stands out against the button fill. You can check using [http://accessible-colors.com/](http://accessible-colors.com/). Always make sure that your colours meet the AAA requirements.
3.   When choosing a font, make sure it is legible, big enough to see, and a medium(ish) weight.

### 5. Vertical padding

The sizing of your button plays a big role in the accessibility of your interface. Most inexperienced designers will say something like, “Buttons should have a height of 36 pixels”. This isn’t the best approach — especially if you are designing for web. You should always take the line hight of the font you are using and add a unit to it. For example: “My button’s label has a line height of 20px and vertical padding of 8px”.

Buttons with different vertical padding.

“Why?” you ask. This is for two reasons. 1) People with visual impairments may increase the font in their browser and, consequently, they need the font size to change without the button height cutting it off. 2) That’s how developers create buttons — they add padding to their div containers, not heights.

### 6. Horizontal padding

There are 2 ways you can approach horizontal padding.

**First option:**Make the button width align to the grid. This is a nice way of keeping all your buttons a consistent length. It does, however, limit the number of words you can use.

Buttons whose width is determined by a grid.

**Second option:**

 Have fixed padding on the sides. I also usually add a clause for a minimum width of a button, to avoid really small buttons. While this allows for the case where you can have different amounts of text, it can make your buttons very uneven.

Buttons whose width is determined by padding & label length.

## 4. Button states and feedback

Button states let the user know whether they can click or have clicked, or had successfully clicked a button. You should also bear in mind that a button can have overlapping states. For example, it could be ‘active’ and ‘hover’ at the same time.

### 1. Active & disabled state

The active state is when a button is ‘clickable’/’tappable’. While that may sound a bit obvious, the important thing to note here is that a button can be disabled if the user hasn’t completed the necessary steps. For example, if a user hasn’t entered their name and email address, they shouldn’t be able to submit their details.

An active and disabled button.

### 2. Hover & hover off (mouse over & mouse off)

On desktop devices, a button should have different states to let the user know that it is clickable. It can also encourage users to click if they see an animation. Usually, a ‘hover off’ state will be the reverse of a ‘hover on’ state, but not necessarily. You may want to indicate that you had previously hovered over a button.

A button demonstrating hover.

**Don’t be a N00b tip:** Hover states will never be seen on tablet and mobile because your fingers can’t ‘hover’. So if you are designing for an app, don’t worry about this state.

### 3. Focus

The focus state can be a bit confusing to wrap your head around. (It was for me anyway.) So the easiest way to explain it is to show its use, then work backwards.

If your user has poor fine motor skills, they may need to use [tabbing navigation](https://www.nngroup.com/articles/keyboard-accessibility/). The user will click ‘tab’ to move around the site, from one navigational link to the next. This means that there needs to be a ‘focus’ state for a button to show that it is ‘clickable, but not clicked yet’.

Another example of a focus state is when you click on an input field. If you were to start typing, only that input field — not another — would start populating.

The default focus state is the blue ‘glow’ that you have undoubtedly seen during your internet explorations. Luckily, we live in a time where we can make our own custom button states. Most designers seem to use the same visual cues for hover and focus states.

Two different examples of the ‘On focus’ state.

### 4. Pressed

The pressed state is the state when the user’s cursor or finger is ‘holding down’ on the button. When the user ‘releases’ their finger or cursor over the button, then the button registers as ‘clicked’.

A button demonstrating the ‘Pressed’ state.

### 5. Clicked

Buttons need a ‘clicked’ state to indicate to the user that it has been clicked.

A button demonstrating the ‘Clicked’ state.

## 5. Button labelling

The trick to button labelling is consistency. And if you are a better person than I, then it helps a lot to decide on your rules early on in a project to avoid having to painstakingly go and change all your button copy later.

### 1. Use of verbs

Most buttons contain verbs to indicate what the button will do, e.g. ‘Save’, ‘Publish’, ‘Edit’. While ‘Back’, and ‘Next’ aren’t verbs, in the context of an interface they seem to work in the same way. I like to keep the ‘verb’ + ‘noun’ structure when writing button labels — this makes the action more prescriptive, e.g. ‘Save post’, ‘Next step’, etc, as opposed to ‘Save’, ‘Next’ — but the choice is up to you and your users.

### 2. Case

You should also decide on what font case to use. Here are some general guidelines that I use:

1.   **All caps**, e.g. ‘NEXT SECTION’. I use them for more ‘professional’ type platforms. Material Design uses buttons with all caps.
2.   **Title case**, e.g. ‘Next Section’. I tend to avoid using title case as it doesn’t read as easily as sentence case. In terms of tone, I would imagine that it is halfway between ‘professional’ and ‘conversational’.
3.   **Sentence case**, e.g. ‘Next section’. I use sentence case for more ‘friendly’ or ‘conversational’ platforms. Note: Yes, it is sentence case, and yes, there should be a full stop if it was true sentence case — but for the love of all things good and designy, please don’t add a full stop.
4.   **Lower case**, e.g. ‘next section’. Like title case, I don’t tend to use lower case buttons labels that often. I would imagine that they are the most ‘causal’ case.

### 3. Consistency

When writing copy for buttons, make sure that you keep consistency. Here are a few guidelines I like to set in place at the beginning of a project:

1.   **Chose amount of words:** One, or two, or more words per button
2.   **Choose case:** Sentence case, or upper case, or title case, or lower case
3.   **Label structure:** e.g. ‘verb’ + ‘noun’, or ‘verb’, or ‘verb’ + a + ‘noun’, etc.

**_Post Publish edit:_**_I recently read_[_5 Rules for Choosing the Right Words on Button Labels_](https://medium.com/@uxmovement/5-rules-for-choosing-the-right-words-on-button-labels-dc3f74c2c2a3)_by_[_UX Movement_](https://uxdesign.cc/u/40dd56d8f87d)_and highly recommend it. Check it out to learn more about button labelling done right._

## 6. Touch targets

### Button sizing for desktop (click)

Because a cursor on a desktop is smaller than a finger on a touch screen, you can make your buttons a lot smaller. But would you want to?

A user should never have to search for a button, so it is up to you to work out the correct hierarchy and navigation for your interface.

### Button sizing for touch screen (tap)

[MIT Touch Lab](http://touchlab.mit.edu/publications/2003_009.pdf) study showed that the part of the finger used for touching screens is 8–10mm, therefore the minimum target size needs to be 10mm or larger if you want to avoid users making [fat finger mistakes](https://www.urbandictionary.com/define.php?term=fat+finger). As mentioned before — I am all about big buttons.

So, what size should you make your buttons then? Well, here is what the experts say:

**Material Design** suggests that the touch target should be 48dp x 48dp with 8dp between different touch points. [Source](https://support.google.com/accessibility/android/answer/7101858?hl=en)

While I can’t find any documentation on **iOS’** design system’s target size, the general understanding is that its minimum target size is 44 x 44pts.

If you are struggling with dimensions and what size to use, I highly recommend

[Zac Dickerson](https://medium.com/u/a6438a90066?source=post_page---user_mention--7856ff90f544---------------------------------------)

’s

[story on accessibility](https://medium.com/@zacdicko/size-matters-accessibility-and-touch-targets-56e942adc0cc)
.

## 7. Button position

### The great primary button position debate

If you were to have 2 buttons placed side by side, on which side should the primary button sit?

Two different positions for the primary and secondary actions.

Option A shows the primary button on the left. The argument here is that it is probably what the user wants to see first, so show it first.

Option B shows the primary button on the right. The argument here is that we want the user to see the secondary button first so that they know their options before they continue. Items placed on the right also indicate continuation.

## 8. Button hall of fame

This section is just to celebrate some cool design principles and systems. I love the Material Design System’s buttons just because their principles are really well thought through.

## Material Design System’s button

Material Design button image

No conversation about buttons is complete without mentioning the Material Design System and their work on buttons and how they interact with the other components within the system. I partially like how the buttons interact with the user on touch.

Check out their section on buttons here: [https://material.io/design/components/buttons.html#anatomy](https://material.io/design/components/buttons.html#anatomy)

I am also a fan of their work on floating action buttons. Check it out here: [https://material.io/design/components/buttons-floating-action-button.html](https://material.io/design/components/buttons-floating-action-button.html)

## 9. Closing thoughts

You can’t really build interfaces without buttons; they deserve more attention that they often get (poor dears). Take the time to understand how they work and how to use them to make the best possible experience for your users.

If you have any thoughts or tricks when it comes to styling buttons, please let me know!

## Related
[Add wiki-links manually or run update_wikilinks.py]