# Radio Buttons Checkboxes Toggle Switches And Dropdown Lists Design Tips For Using Selection

## Radio buttons, checkboxes, toggle switches, and dropdown lists: design tips for using selection…

Nick Babich·9 min read·Oct 4, 2022

Clean article found smry-fast Reading stack uxplanet.org · 1,447 words

The article is ready without leaving the reader. Source: Direct extraction.

## Plus 7 common scenarios for using controls

Radio buttons, checkboxes, toggles, and dropdowns are UI controls that allow users to make a selection. Although they have been in user interfaces for a long time, product designers still have a lot of trouble choosing the proper control for their tasks.

This article will review 4 popular types of selectors, teach general rules on when and how to use them, and explore 7 common scenarios of using selection control.

## 1. Radio buttons

Radio buttons are selectors used for the list of two or more options, and all options in this list are _mutually exclusive_. Users must select exactly _one_ option. When users click on a non-selected radio button, it will deselect whatever other option was previously selected in the list.

Radio buttons

### How to design radio buttons

Here is a quick tutorial that shows how to design radio buttons in Figma:

### Benefits of using radio buttons

Radio buttons expose all available options. Users can see all available options at a glance and make a selection.

### Downsides of using radio buttons

*   Take screen estate. Each option takes a row on the screen. It might be a problem for mobile screens.
*   Can be ignored by users. Since radio buttons always come with one option pre-selected, users might simply ignore it. They might assume that the system already chooses the best possible option for them.

### Design best practices for radio buttons

*   Radio buttons always have exactly one option selected. You should never display radio buttons without a default selection. The only exception to this rule is when you use radio buttons for online survey. In this case, you should leave the option unselected.

Radio buttons should always have one option pre-selected

*   Use radio buttons when all options in the list have the same weight. There is an equal possibility that the user can choose any option from the list.

The list of options is from the same domain and has the same weight.

*   Provide option “None” if users might want to refrain from making a selection. Never force users to choose the option they don’t want to choose.

Add the “None” option when the user might want to refrain from making a selection.

*   Try to avoid the horizontal arrangement of radio buttons. Horizontal radio buttons can be difficult to scan — it can be challenging for users to tell which label the radio button corresponds to.

Horizontal vs. vertical arrangement of radio buttons.

*   Make both the circle and label clickable. Ensure the user can click either on the circle or label to select an option.

Larger clickable areas make it easier for the user to make a selection

## 2. Checkboxes

A checkbox can be a single option or a set of options available for selection. Checkboxes are used when the user may select any number of choices, including zero, one, or several. Each checkbox in the set is independent of all other checkboxes, so checking one box doesn’t do anything to the others.

Checkbox

### How to design checkboxes

Here is a quick tutorial that shows how to design checkboxes in Figma:

### Benefits of using checkboxes

Checkboxes expose all available options. Users can see all available options at a glance and make a selection.

### Downsides of using checkboxes

Take screen estate. Each option takes a row on the screen. It might be a problem for mobile screens that have limited screen estate.

### Design best practices for checkboxes

*   If the user has to select a few options from the list, you should tell the user before they start doing that. By showing the message, you minimize the chance of displaying an error message like “You should select at least X options.”t

Asking the user to choose at least X number of options from the list

*   Checkbox can present a list containing sub-selections. When the user clicks on the parent element, all options in the sub-section become selected.

Nested checkboxes logic. Image by Material Design.

*   Use positive and active wordingfor labels. It will help users understand what will happen if they turn on the checkbox.

Avoid negations such as “Don’t send me promo emails,” because it would mean that the user should have to check the box in order for something not to happen.

## 3. Toggle switch

Switch prompts users to choose between two mutually exclusive options and always has a default value. It works well when users have to answer Yes/No questions and for binary operations (such as enabling or disabling a particular setting).

The toggle switch represents a physical switch that allows users to turn things on or off.

### How to design switches

Here is a quick tutorial that shows how to design an interactive toggle switch in Figma:

### Benefits of using switches

Toggle is easier for the thumb. This property makes it suitable for mobile devices.

### Downsides of using switches

*   Take screen estate. Each option takes a row on the screen.
*   A user might accidentally trigger the wrong option. Once pressed, switches immediately activate or deactivate something.

### Design best practices for using toggle switches

*   Toggles should provide immediate results. They should _not_ require the user to click Save/Submit button to apply the new state.

Don’t add Save/Submit button to apply the new state.

## 4. Dropdown

Dropdown is a list of options that become visible when the user clicks on the input box. This control is typically used for a long list of options (i.e., 6 or more).

Dropdown list

### How to design dropdown

Here is a quick tutorial that shows how to design an interactive dropdown list or menu in Figma:

### Benefits of using dropdown lists

Dropdown saves screen estate. It uses less space because all options become visible only when the user presses the _Select_ button.

### Downsides of using dropdown lists

*   Require extra action to see the options. Options are hidden by default, and the user should click the Select button to see them.
*   It might require a scroll to see the options. Long lists of options (such as Country selector) will force a user to scroll to find the suitable choice. This problem becomes even more noticeable on mobile because scroll within the scroll is a terrible solution.

Scrollable list of options.

### Design best practices for using dropdown lists

*   Dropdowns should be the last resort. Whenever possible, instead of dropdown, try to use alternative controls that help the user to complete the task but have better usability.

Using alternative UI controls.

*   Use dropdown with the autosuggest mechanism. Once the user starts typing the sentence, the list of options becomes narrow to show the relevant results.

An autosuggest mechanism for the country dropdown list. Image by Dzone.

## 7 typical scenarios for using selectors in UI design

### Scenario 1

_Q: I have a list of options (i.e., different types of health insurance policies), and the user has to pick one option from the list._

## Get Nick Babich’s stories in your inbox

Join Medium for free to get updates from this writer.

_A: If you have 6 or fewer options, you should use the radio button with the most convenient option pre-selected. Typically you should pre-select the option that provides the most benefit for users, not your business. If you have more than 6 options, you should consider the dropdown selector._

### Scenario 2

_Q: I have a list of options (i.e., different types of toppings for pizza), and the user can choose zero, one, or a few toppings._

_A: You should use a set of checkboxes. The set should not have any options pre-selected, and UI should not force the user to make a selection._

### Scenario 3

_Q: I have a setting that the user can be turned On or Off (i.e., turn Wi-Fi on or off)_

_A: You should use a toggle switch. The toggle switch reinforces the feeling of action (turning something off or on)._

### Scenario 4

_Q: I want to ask users if they want to receive notifications_

_A: You should use a toggle switch. Just make sure that the label is clear “Receive Notifications.”_

### Scenario 5

_Q: I want to ask the user if they want to subscribe to the newsletter_

_A: You should use a checkbox. Make sure the label says, “Subscribe to promo emails.”_

### Scenario 6

_Q: I want to ask the user if they agree with terms and services_

_A: You should use a checkbox. The fact that the checkbox requires users to click the Submit/Save button gives users more time to think about their choice._

### Scenario 7

_Q: I want to ask the user a direct question “Are you older than 21?”_

_A: Use radio buttons “Yes/No.”_

## Related
[Add wiki-links manually or run update_wikilinks.py]