# The Ultimate Selection Control Cheat Sheet

## A practical guide to finding the right fit for your components!

Choosing which type of component should be used to select an option in a digital product can be more tricky than you think.

 Dropdowns are usually the go-to solution because they’re compact, widely supported, familiar to users, and easy to implement. But, are they always the best choice?

According to several usability tests, dropdowns are one of the most questionable elements, and relying exclusively on them can result in slower and less usable experiences. As Luke Wroblewski says they “ [should be the UI of last resort](https://www.lukew.com/ff/entry.asp?1950=) ”.

**Let’s consider some of their weaknesses:**

 - Not immediately visible options 

 - Select is a multi-step process (open → scan → scroll → pick) 

 - The list can be long 

 - Options cannot contain long and clear text

In this article, we’ll explore some alternative options while taking into account guidelines and best practices for choosing and designing the right selection control component.

**Specifically, we will look at:**

 - Checkbox 

 - Radio button 

 - Toggle switch 

 - Toggle button 

 - Dropdown 

 - Segmented control 

 - Numeric selectors

## Checkbox

**✅ Use checkboxes when:**

*   You have a list of independent options that can be selected.
*   Options have long text or are composed of multiple text strings.
*   You can have an implicit default state.
*   You need to turn on/off a single item, using a stand-alone checkbox.

Google Chrome settings interface

Don’t forget the handy ‘Not all Selected’ intermediate state used inside of bulk selection. Always support bulk selection if needed. Your users will thank you for making it effortless.

A screen from copy.ai showing 2/5 items selected

🧐 **More info:**

*   When the list allows choosing between more than 15 choices consider using a multiple selection bar to allow users to remove options immediately.
*   Let users select an option by clicking on either the button/box itself or its label. ([Fitts’s law](https://www.asktog.com/columns/022DesignedToGiveFitts.html))

Mobbin UI elements selection

## Radio Button

**✅ Use Radio buttons when:**

*   There isn’t a recommended option (if so, the dropdown should be prioritized because it can show only that).
*   You have to insert a long text that can’t be shown inside of a dropdown.
*   You need to use multiple text strings.

Using a dropdown, in this case, would limit the visibility of options by slowing down the flow

❌ **Don’t use when:**

*   You are designing for a desktop environment and there are too many possibilities (5+) to be shown. It’s probably not the best solution to adopt because will take up a lot of vertical space.
*   You can’t “ **always offer a default selection for radio button lists** ”. By definition, radio buttons always have exactly one option selected as [NN/g explains](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/). Often a review of the software metrics can quickly determine the most popular option, tipping designers which of these items should be the default selection.
*   You need to show a list of options but you don’t have vertical space. Radio button lists must always be vertically aligned.

🧐 **More info:**

*   If needed, consider providing a way out if neither option may apply “none of the above”.
*   Let users select an option by clicking on either the button/box itself or its label.
*   In iOS, Apple ditched those old-fashioned radio buttons with a component called “option select” made up of the option + a check icon. Nowadays you can find this kind of solution in many digital products. Just make sure to keep things consistent in your design, _unlike Apple sometimes ahem forgets to do…_ ”

Two option selection screens in iOS. Notice how the position of the check icon is first to the right and then to the left. iOS standard should be on the left.

*   One trick often used in E-commerce is to visually display options.

Tesla car configurator

## Toggle Switch

**✅ Use toggle switched when:**

*   You have to switch between options not necessarily on/off e.g. a dark-mode switch.
*   Selection will immediately take effect e.g. auto to adjust brightness. You won’t have to save the change.

❌ **Don’t use when:**

*   The action doesn’t take effect immediately. In this case, it’s better to replace the toggle switch with a single checkbox that will be applied once the settings are saved. _(This is not a mandatory rule, but it helps keep things consistent!)._

## Toggle Select/Chips

**✅ Use toggle select when:**

*   The vertical space can represent an issue. Also, toggle tokens halve the number of visual elements used. Minimizing visual noise allows users to focus on the options.
*   When the choice takes immediate effect.

❌ **Don’t use when:**

*   The list contains a long text. This would lead to components of enormous size.

## Dropdown

**✅ Use dropdown when:**

*   You have many options that it’s not good to display side by side because it becomes cluttered and takes a lot of time to scan. The ideal number should be between 5 and 10 options.
*   For a long dropdown menu, it’s also suggested to provide a typehead where the user can type the option name and the list displays only the filtered options. If the item needs to be found from a list of common user options, auto-completion is also suggested. In some cases, when there are many unfamiliar options, you might want to consider replacing the dropdown with an open search field that displays options via autosuggest.
*   You need to choose between a large number of familiar options e.g. zoom selection. In this way, you will hide other possibilities when the recommended option is already selected. This will save space and discourage users from switching.

Google Chrome page setting

❌ **Don’t use when:**

*   You have more than 20 options. It can be intimidating for the user that needs to find the input. While a list of countries may not be terrible because they are sorted alphabetically, they are still not the best solution. In this case, for example, you can try to avoid this type of selection through the zip code autodetection automatically selecting the country.

## Segmented Control

Segmented control buttons need to have a cohesive background that visually indicates to users that they need to select a single option. In addition, maintaining consistent segment widths is key. When all segments have the same size, the segmented control feels more balanced.

**✅ Use segmented control when:**

*   You have to see all the options together e.g. filter or sorting
*   You have no more than 5/7 choices

## Numeric Selectors

There are 2 possibilities in case you are picking a number:

1.   **Low-variability numbers**. Numbers characterized by a high degree of predictability due to the frequency of choice e.g. date of an appointment you’re scheduling, number of tickets for an event.
2.   **High-variability numbers**. Numbers that have a _s_ imilar probability of being anywhere in a wide range of time, e.g. date of birth.

For numbers with low variability, it is preferable to make it easy to choose numbers in the most common range.

 A **calendar date picker** fits really well in this case. If you know that the date to be picked is most likely in the next 2–4 weeks, you’re on a roll.

[Google Flights](https://www.google.com/travel/flights) for example set the default dates roughly 2 weeks in the future. It’s fine if choosing dates out of this range is a little harder because they will be selected less frequently.

Airbnb uses a stepper to select the number of guests. In this case, we have a preselection occurring more frequently (1) and the type of control makes it easier to pick numbers close to the preselected value. You will need 1 ticket many times, but 10 not so often.

Use a slider if you have a wide range of numeric options and if the user needs to have a minimum and a maximum number ( not necessarily shown ).

For numbers with high variability and no limit instead, text inputs are probably the best option because there’s no reason to favor any number over another, and so all options will be equally difficult to select.

 A best practice, in this case, is to provide the user with a hint that helps him understand what should be filled in.

❌ **Don’t use:**

*   Dropdowns when you are picking low-variability numbers.
*   Dropdowns when you’re counting — e.g. the number of tickets, the number of people, etc.

## Final conclusions

In this brief overview we’ve seen together, we analyzed several use cases and solutions to choose which type of component is the most appropriate for each common context.

 Deciding whether a component is the most appropriate choice, however, is like picking the perfect ice cream flavor: it’s all about what will satisfy your users’ cravings. When you’re deciding which solution to go with, consider the list of ingredients carefully: the typology of selection, the size of the list, the familiarity with the options, and the overall layout of the interface can all impact the effectiveness of your choice. Will a basic dropdown do the trick, or do you need to spice things up using some other component?

By understanding the various options and their strengths and weaknesses, you can make an informed decision that strikes the right balance between usability and design. So, take the time to assess your needs and carefully evaluate each solution to find the best fit for your situation.

### Useful links:

## [Checkboxes vs. Radio Buttons](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/?source=post_page-----dde495365d55---------------------------------------)

### [I recently encountered the following box on a major website's registration page. It contains at least two design… www.nngroup.com](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/?source=post_page-----dde495365d55---------------------------------------)
## [Toggle-Switch Guidelines](https://www.nngroup.com/articles/toggle-switch-guidelines/?source=post_page-----dde495365d55---------------------------------------)

### [Every morning, I wake up, pour water into my tea kettle, and flip the switch on. Once the water is boiling, I turn the… www.nngroup.com](https://www.nngroup.com/articles/toggle-switch-guidelines/?source=post_page-----dde495365d55---------------------------------------)
## [Listboxes vs. Dropdown Lists](https://www.nngroup.com/articles/listbox-dropdown/?source=post_page-----dde495365d55---------------------------------------)

### [Many UI controls allow users to select options; they include checkboxes, radio buttons, toggle switches, steppers… www.nngroup.com](https://www.nngroup.com/articles/listbox-dropdown/?source=post_page-----dde495365d55---------------------------------------)
## [Radio Buttons: Always Select One?](https://www.nngroup.com/articles/radio-buttons-default-selection/?source=post_page-----dde495365d55---------------------------------------)

### [You are probably wondering how anyone could muster enough words for an entire article about the humble, ubiquitous…](https://www.nngroup.com/articles/radio-buttons-default-selection/?source=post_page-----dde495365d55---------------------------------------)

[www.nngroup.com](https://www.nngroup.com/articles/radio-buttons-default-selection/?source=post_page-----dde495365d55---------------------------------------)
## [UI cheat sheet: dropdown field](https://uxdesign.cc/ui-cheat-sheet-dropdown-field-a30025c0f432?source=post_page-----dde495365d55---------------------------------------)

### [Dropdowns get a lot of flak from the UI world – and if we are honest, it’s not without reason. Done badly, they become… uxdesign.cc](https://uxdesign.cc/ui-cheat-sheet-dropdown-field-a30025c0f432?source=post_page-----dde495365d55---------------------------------------)
## [Dropdown alternatives for better (mobile) forms](https://medium.com/@kollinz/dropdown-alternatives-for-better-mobile-forms-53e40d641b53?source=post_page-----dde495365d55---------------------------------------)

### [Using a dropdown menu usually seems a no-brainer but it’s also easy to misuse due to its limitations. You can do… medium.com](https://medium.com/@kollinz/dropdown-alternatives-for-better-mobile-forms-53e40d641b53?source=post_page-----dde495365d55---------------------------------------)
## [4 Rules for Intuitive UX](https://www.learnui.design/blog/4-rules-intuitive-ux.html?source=post_page-----dde495365d55---------------------------------------)

### [This is my advice on improving the UX of your designs WITHOUT hours of user research sessions, paper prototyping… www.learnui.design](https://www.learnui.design/blog/4-rules-intuitive-ux.html?source=post_page-----dde495365d55---------------------------------------)

## Related
[Add wiki-links manually or run update_wikilinks.py]