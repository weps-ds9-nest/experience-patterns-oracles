# Image: Atlassian Design

Image: Atlassian Design

Date picker is an input field that allows you to select dates through textual input or interaction with a calendar overlay. Despite this is a relatively simple component, it’s one of the most frequently used elements in forms. Every time we fill out the date of birth, make an online appointment to doctor or book a vacation, we interact with date pickers.

Well-designed date pickers streamline date selection — users select a date in a few clicks or taps. But how to design a date picker that has good usability?

In this article, I want to focus on two important elements of date picker — _numerical input field_ and _calendar overlay._

## Numerical input field

### Use placeholders to indicate the input format

In many cases, it’s better not to leave the input field blank and pre-populate it with a date placeholder, showing an example of the correct input.

The placeholder indicates the order of the day, month and year input.

### Provide format suggestions when the user activates the field

Because in some implementations the placeholder disappears once the input is activated, some users will forget the expected format — o _ut of sight, out of mind._ That’s why the expected date format suggestion should be visible when the user activates the input field.

Keep the placeholder displayed as the user inputs the date. If that’s not possible, use a floating label to continue displaying the format.

### Don’t hide the separator

When you hide the separator, some users will try to add it manually. Most probably, users will use a separator sign like a hyphen (`-`) or slash (`/`) and this can cause problems during inline validation. That’s why it’s better to keep the delimiters displayed as the users manually input the date.

### Design for seamless movement between day-month-year

As the user starts typing, the transition between day, month and year should happen automatically, without any effort from the user side. All the user should do is to keep typing on the numerical keyboard.

### Should the input field contain default prepopulated values?

The answer to this question in the context of your form and the information you know about your users. In a nutshell, it’s a good idea to prepopulate the dates only if you are certain that the user is likely to choose these dates.

## Get Nick Babich’s stories in your inbox

Join Medium for free to get updates from this writer.

_Avoid setting random values_. Setting random values for the user will force users to change the values to the ones they are actually looking for. It will introduce extra work and increase the interaction cost.

### Once the user has selected dates but refreshes the page, should the input be persistent in the fields?

Yes. If the user accidentally refreshes the page, they won’t be delighted about their input being lost and having to retype it again.

## Date calendar

### Do we need to include a calendar in all date input fields?

No, date input doesn’t necessarily require a calendar. For example, if the date is likely to be quite far in the past or the future (for example, date of birth), a regular numerical input is a good solution.

### Indicate current date

Don’t forget to indicate the current day, so that users won’t need to access OS calendar to see what the day is today.

Highlighting today’s date. Image: Atlassian Design

Today’s date is visually separated from the selected date

### Show only dates that return non-zero results

This is critical for service-ordering forms. For example, if you use date calendar in the apartment’s availability form, and you know that the apartment is not available on some dates in this month, it’s better to restrict the date selection by making those inactive — by doing that you will help users avoid selecting unavailable dates and end up in zero-results dead ends.

Avoid displaying unavailable dates. Airbnb displays available and unavailable options right in the date picker. This eliminates a frustrating zero-results-page.

### Simplify decision-making process by providing additional helpful information

This is particularly helpful for cases when users want to explore available options. For example, when a user is looking for a holidays trip within the next few weeks, but they don’t have exact dates in mind, you can help them by displaying pricing and availability.

Ryanair provides price option per day and simplifies the decision-making process

### Should we show the days of the week in the calendar?

Again, it depends on the nature of your form. Displaying an actual day of the week is important for booking appointment forms. But it can be irrelevant for forms that ask for personal details (such as date of birth).

### Should the calendar open automatically?

Should we show the calendar automatically when the user clicks/taps on date input filed? There is no universal answer to this question. But one thing for sure, we need to design a seamless user journey. If the auto-triggering calendar helps users save time, we should do it.

Hipmunk seamlessly drives the user forward through the input, displaying the date picker automatically.

_Originally published at_[_uxpro.cc_](https://uxpro.cc/publications/date-picker-design-best-practices/)

## Related
[Add wiki-links manually or run update_wikilinks.py]