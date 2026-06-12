# Radio Buttons Ux Design

## by Nick Babich

Radio buttons are an essential element of forms. Theyare used when there is a list of two or more options that are _mutually exclusive_ and the user must select exactly one choice. Clicking a non-selected radio button will deselect whatever other button was previously selected in the list.

Generic radio buttons control

Radio buttons are great when used correctly — they simplify the task of selecting an option. In this article, we’ll overview practical guidelines for radio buttons that have been crafted from usability testing.

## How Radio Button Got Its Name?

The software radio button was modeled after these physical radio buttons. Old car radios have physical buttons which were used for selecting stations. When the driver selected a particular station, all buttons pop out, leaving only one button pressed.

Only one button can be pressed at one time. Image credit: Tumblr

## Best Practices for Radio Buttons

### Don’t use radio buttons to perform actions

Radio buttons should not be used to perform commands.

### Logical order for options

The list the options should be structured in a _logical order_**,** such from simplest operation to most complex, or least risk to most.

### Options Should Be Comprehensive and Clearly Distinct

Similar to any other interactive elements, the biggest usability problems for radio buttons come from labels. Vague or misleading labels can cause a lot of problems for users because they will need to understand the meaning. Always test your labels for clarity. Both the vocabulary and context should be clear to your users.

### Always Offer a Default Selection

One of the [10 heuristics of UI design](https://uxplanet.org/golden-rules-of-user-interface-design-19282aeb06b) says that users should be able to undo (and redo) their actions. This means enabling people to set a UI control back to its original state. In case of radio buttons this means that _radio buttons should always have exactly one option pre-selected._ Select the safest and most secure option (to prevent data loss).

## Get Nick Babich’s stories in your inbox

Join Medium for free to get updates from this writer.

If users might need to skip making a selection, you should provide a radio button for this choice labeled as“None.” Offering users explicit option to select is much better than forcing users to select something from the list.

### Try To Lay Out Your Lists Vertically

When radio buttons lay our horizontally, users can face problems scanning the option— it hard to tell with which label corresponds to which option: the one before the button or the one after. Vertical positioning of radio buttons is safer.

> _Try to lay out your lists vertically, with one choice per line._

If you still need a horizontal layout with multiple options per line, make sure to space the buttons and labels so that it’s absolutely clear which choice goes with which label. For example, you should prevent a situation like this where it’s really difficult to see the correct radio button to click for option four.

Bad: Horizontal radio buttons

Good horizontal radio buttons can be found in Duolingo app: they’ve used a classic horizontal radio buttons, but made the targets visually distinguishable and large enough for touch-enabled devices.

Good: Horizontal radio buttons

### Use Label Tags as Click Targets

When it comes to measuring the interaction cost, the size of the target plays important role. Radio buttons are tiny in nature, and, they can be hard to click or tap. Try to increase the target area to make it easier to select the option. Let users select an option not just by clicking on a circle, but also by clicking on the label.

Left: Only limited area is available for click. Right: Large clickable area.

### Use Radio Buttons Rather Than Drop-downs

_If possible, use radio buttons rather than_[_drop-down menus_](https://uxplanet.org/ux-design-drop-downs-in-forms-c6943ec30037#.2k4dxws4e)_._ Drop-down menus will require extra action (the user needs to tap on a drop down element to see the options). Radio buttons, on the other hand, make all options visible so that users can easily compare them.

Radio buttons for gender selection. Gender Select UI design by Istvan Szabo

### Avoid Nesting

_Avoid nesting radio buttons with other radio buttons or checkboxes._ You should keep all options at the same level to avoid confusion.

Using nested options adds unnecessary complexity

### Use Animation and Visual Feedback

Well-designed animations make the experience feel crafted. Interactive elements like radio buttons should appear _tangible—_ motion cues acknowledge input immediately and add _clarity_ through visual reactions to user input.

Image credit: Dribbble

## Should I use a Check Box instead of Radio Buttons?

When users have to choose from two mutually exclusive options (i.e. questions like “Do you agree to receive messages from our team?”), you could use a single _checkbox_ instead of radio buttons. However, checkboxes are suitable only for turning a single option ON or OFF, whereas radio buttons can be used for completely different alternatives.

Checkbox control. Image credit: Material Design

You should remember following moments if both solutions are possible:

**Alternatives.** Use radio buttons if the meaning of the empty checkbox isn’t obvious. In example below, the choices are opposites so radio buttons are the better choice for this option.

Select orientation for the document (Landscape or Portrait)

**Wizard.** You should use radio buttons on wizard pages to make the alternatives clear, even if a check box is otherwise acceptable. Designs with a radio button selected by default make a strong suggestion to the user. The default choice may lead the users into making the best decision, and may increase their confidence as they proceed.

If an option is strongly recommended, add “(recommended)” to the label. Image credit: Dropbox

**Simple Yes or No answer.** Using a checkbox is correct when you have a single simple question and the user will answer either “yes” or “no”.

Simple question can be asked in a form of checkbox

## Conclusion

When designing radio buttons, most important to make this UI element predictable for users, because this enhances users’ ability to control the system.

Thank you!

_Follow UX Planet:_[_Twitter_](https://twitter.com/101babich)_|_[_Facebook_](https://www.facebook.com/uxplanet/)

## Related
[Add wiki-links manually or run update_wikilinks.py]