# ![Image 1: Date picker UI design](https://studio.uxpincdn.com/studio/wp-content/uploads/2022/07/Date-picker-UI-design-1024x512.png.webp)

![Image 1: Date picker UI design](https://studio.uxpincdn.com/studio/wp-content/uploads/2022/07/Date-picker-UI-design-1024x512.png.webp)
Date pickers are some of the most familiar [UI patterns](https://www.uxpin.com/studio/blog/ux-design-patterns-focus-on/) in digital product design. UX designers use date pickers on websites, applications, games, enterprise software, operating systems, and more.

Designers must understand how these date pickers will work across screen sizes, operating systems, devices, etc., to test the impact on the product’s aesthetics, functionality, and overall user experience.

UX designers can’t build date pickers using traditional image-based design tools…but they can with UXPin Merge!This technology allows you to import a fully functional date picker from Git repository or npm package, as well as bring one from Storybook.

The date picker that you will sync to UXPin will behave like a date picker in the end product. No need to link static artboards to create interactions! [Request access to Merge](https://www.uxpin.com/merge).

Reach a new level of prototyping

Design with interactive components coming from your team’s design system.

![Image 2](https://uxpin.com/studio/wp-content/themes/uxpin-juggernaut/img/cta-banner-merge.png)

## Table of Contents

[SHOW]

1.   [What is a Date Picker?](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-what-is-a-date-picker)
    1.   [Why are Date Pickers Necessary?](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-why-are-date-pickers-necessary)

2.   [Date Picker UI Design for Mobile vs. Desktop](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-date-picker-ui-design-for-mobile-vs-desktop)
    1.   [Mobile Date Picker](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-mobile-date-picker)
    2.   [Desktop Date Picker](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-desktop-date-picker)

3.   [5 Types of Date Picker UI Design](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-5-types-of-date-picker-ui-design)
    1.   [Numerical Input Field](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-numerical-input-field)
    2.   [Dropdown Date Selector](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-dropdown-date-selector)
    3.   [Scrolling Date Pickers](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-scrolling-date-pickers)
    4.   [Calendar Date Picker](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-calendar-date-picker)
    5.   [Timeline Pickers](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-timeline-pickers)

4.   [Date Picker UI and UX Best Practices](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-date-picker-ui-and-ux-best-practices)
    1.   [Date Picker Accessibility](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-date-picker-accessibility)
    2.   [Show Current Date](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-show-current-date)
    3.   [Block Unavailable Dates](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-block-unavailable-dates)
    4.   [Provide Additional Critical Decision-Making Data](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-provide-additional-critical-decision-making-data)
    5.   [Reduce Unnecessary Data](https://www.uxpin.com/studio/blog/date-picker-ui-design/#h-reduce-unnecessary-data)

5.   [How to design a date picker in UXPin](https://www.uxpin.com/studio/blog/date-picker-ui-design/#toc_How-to-design-a-date-picker-in-UXPin)
    1.   [Styling the date picker Component](https://www.uxpin.com/studio/blog/date-picker-ui-design/#toc_Styling-the-date-picker-Component)

6.   [**Using real Components instead**](https://www.uxpin.com/studio/blog/date-picker-ui-design/#toc_Using-real-Components-instead)

## What is a Date Picker?

Date pickers are UI patterns that allow users to choose a specific date, time, or combination of both–for example, selecting a date of birth. The purpose of these date pickers is to streamline date capture while ensuring format consistency.

### Why are Date Pickers Necessary?

People worldwide use different date formats. For example, the United States places the month before the day (mm/dd/yyyy), whereas the UK uses the _day, month, year_ format.

Although these differences seem subtle, a [database](https://www.dreamfactory.com/) cannot distinguish whether the user uses the US or UK format. It can only decipher a date correctly in one or the other format. Let’s look at October 1, 2022, numerically:

*   US: 10/01/2022 (10 January 2022 in the UK)
*   UK: 01/10/2022 (January 10, 2022, in the US)

In this example, the database would interpret each entry as January rather than October.

Users can also enter this same date multiple ways and use different separators. Here are a few examples:

*   Oct 1, 2022
*   Oct 1, 22
*   1 Oct 2022
*   1 Oct 22
*   10-01-22 / 01.01.2022 / 10/01/22
*   22/10/01 / 2022/10/01

Date pickers eliminate ambiguity and ensure systems receive a consistent, accurate format by users selecting the day, month, and year individually.

## Date Picker UI Design for Mobile vs. Desktop

### Mobile Date Picker

It’s important for designers to recognize how mobile operating systems like iOS and Android display date pickers to users. The native iOS picker uses an infinite scroll UI, while Android applications use a calendar view displaying the entire month.

A mobile date picker aims to make it accessible to a user’s thumb reach. iOS allows users to scroll using their thumb, while Android’s UI is optimized for thumb taps.

While you can use a custom date picker from your design system, using the native options creates familiarity and reduces the product’s learning curve. If you decide to use native date pickers for mobile apps, make sure you’re not creating usability issues, as we pointed out with iOS.

### Desktop Date Picker

Most desktop websites and applications use calendar date pickers. The extra space and mouse make it easy for users to choose a date with just a few clicks. Many products also provide an input field for users to enter a date manually.

Numerical date input fields work well on desktops too. UX designers must include a placeholder and helpful error messages to guide users toward the correct format.

## 5 Types of Date Picker UI Design

### Numerical Input Field

The most basic date picker is a numerical input or text input field. These fields might include a [modal popup](https://www.uxpin.com/studio/blog/modal-ui-dialogs/) with a date picker, or users must type out the date with separators.

Some products offer users the option to type the date or use a modal, like [this example from US Web Design Systems](https://designsystem.digital.gov/components/date-picker/).

![Image 3: date picker component in US web design system](https://lh5.googleusercontent.com/719wSlRkw9eSBC3DIIKdBDzLyWAUKD9DokIChRjOqa26M8n4bc9klZShZWvkeRBqRt9PuMvtoRX0OEmaqyjo_X0bjQLRLZL_Iw0JwXgyjZmguGZXPbjD3y5whzhWjglZ-iGBctqaOmpDj_i6HA)
Placeholders must show users how to format the date, i.e., MM/DD/YYYY. UX designers can take this further by applying an auto-format for the date where separators appear as users complete the month and day. Designers can also add helper text below, so users know how to complete the form. [See the example](https://codepen.io/mattchza/pen/ZEreLoW).

### Dropdown Date Selector

Designers commonly use dropdown date-selectors for websites and desktop applications. These date pickers work well with a mouse, but with little space between options, they might be challenging for mobile device users, especially those with large fingers and thumbs.

Dropdown selectors take up more space than a single input field with a calendar modal. And they’re more time-consuming to complete because users have to select the day, month, and year individually.

Dropdown selectors are best for desktop applications and websites but might create bottlenecks for onboarding forms.

### Scrolling Date Pickers

Scrolling date pickers work similarly to dropdowns as users choose a day, month, and year separately. These scrollers are most useful on mobile devices where users can use their thumbs to scroll to a day, month, and year.

Many users complain that scrolling date pickers are not suitable for dates far in the future or past. Scrolling through decades takes time and can be challenging for users, especially those with hand or finger disabilities.

The iOS default date picker is the most common example of a scrolling date picker; however, Apple often uses a calendar picker for dates far in the past or future.

### Calendar Date Picker

Calendar UIs are the most commonly used date pickers. These calendar date pickers work well across operating systems, devices, and screen sizes.

As people are used to seeing calendars in physical and digital formats, these date pickers create familiarity for users, reducing cognitive load and the product’s learning curve.

Calendar UIs are especially helpful for date range pickers, allowing users to visualize their choice and make quick adjustments.

### Timeline Pickers

Timeline pickers work well for selecting a short date range (up to a week) or timeframe (a few hours). Timeline UIs are especially useful on mobile devices because users can drag indicators to choose a start and end date.

While you can use timeline pickers for dates, they’re best suited for selecting a time window.

## Date Picker UI and UX Best Practices

### Date Picker Accessibility

Poorly designed date pickers can be frustrating for users with disabilities and screen readers. Keeping things simple is crucial to ensure date selection is accessible to all users.

Here are some recommendations for making date pickers accessible:

*   **Use explicit labels for your date fields**. For example, if someone is booking an appointment, label the field _Appointment Date_ or _Choose an Appointment Date_ so screen readers and users with cognitive disabilities know what date you need.
*   **Include format hints** in the placeholder and above or below the input field. This validation makes date pickets more accessible while benefiting all users with clear instructions.
*   **Users must be able to use a date picker using touch, a mouse, screen readers, and a keyboard**. UX designers must test date pickers to ensure all users and devices can interact with the UI and choose a date effortlessly.
*   **Separating day, month, and year fields** make it easy for screen readers and keyboard users to enter dates. UX designers can also include a button or calendar icon for users to complete their selection using a calendar, a win-win for all users. ([See this date picker example from USWDS](https://designsystem.digital.gov/components/date-picker/)).

![Image 4: uswds date picker](https://studio.uxpincdn.com/studio/wp-content/uploads/2022/07/uswds-date-picker-1024x287.jpg.webp)
Date picker accessibility resources:

*   [Collecting dates in an accessible way by Hassell Inclusion](https://www.hassellinclusion.com/blog/collecting-dates-accessible/)
*   [Date picker by US Web Design System](https://designsystem.digital.gov/components/date-picker/)
*   [General accessibility guidance for forms by US Web Design System](https://designsystem.digital.gov/components/form/)

### Show Current Date

It is important to show users the current date and their selection on calendar pickers. Highlighting the current date gives users a reference for their choice, which is especially important for booking travel and appointments.

Differentiating between the current date and the user’s selection is crucial to avoid confusion. [Material UI clarifies this distinction](https://material.io/components/date-pickers) with an outline for the current date and a shaded background for the selected date.

![Image 5: MUI date picker UI example](https://lh4.googleusercontent.com/FrGiCmpuyCufe3MLmCxyJc1BOeB5GniVq7eHQ8snt0syDXgjWbgEjW-UQs3eqGM8FhnhBj8mbFH2VYh0ux4sFrzj3gRpYorUn3hQe5G6WDnroCwLYZGsVLNUNW-4IElXlGXbzGjHdsRkRxBFmQ)
### Block Unavailable Dates

Choosing a date only to find it’s unavailable is one of the most frustrating user experiences. Users have to start their selection over and try until they find availability. Blocking out unavailable dates allows users to choose without returning to the calendar.

### Provide Additional Critical Decision-Making Data

Many travel booking apps, including Booking.com and Airbnb, show the price per night below each date so users can find the best rates. This information creates a positive user experience because the product helps users save money.

![Image 6: date picker examples](https://lh6.googleusercontent.com/DlEQUq3MYjkmsQufx_i1-giAr1uL5EySxsU3MrSfSgkMgBMNPIS_yHZYplvpOtG8o-Rgwm_wgMP4SuV3qYJGuIc5HjIWrOejnPaxg7RsjuPi--GLnzW1nKf9tJDs3fookWl_t4qMv9TSW2htJQ)
### Reduce Unnecessary Data

Calendar user interfaces can be busy and overwhelming. Designers must reduce as many UI elements, lines, and other content to make the calendar easier to read and complete tasks. For example, users don’t need to see the days of the week when choosing their date of birth.

UX designers must also use solid backgrounds for modal overlays to block out content behind the calendar, which may confuse users.

## How to design a date picker in UXPin

UXPin is an advanced prototyping tool used to create interactive, dynamic, high-fidelity prototypes. Where most prototyping tools require designers to create multiple artboards to prototype just one interaction, UXPin enables designers to use [States](https://www.uxpin.com/docs/editor/states/), [Variables](https://www.uxpin.com/docs/editor/variables/), and [Conditions](https://www.uxpin.com/docs/editor/interactions/#conditional-interactions) to create fully-functioning pages.

To insert a date picker in UXPin, start by clicking on the “Search All Assets” search icon (**command + F** / **Ctrl + F**) in the vertical toolbar.

![Image 7: date picker ui uxpin](https://studio.uxpincdn.com/studio/wp-content/uploads/2022/07/date-picker-ui-uxpin-1024x640.png.webp)
Next, search for “date” or “calendar” using the input field.

Several options will be available under the “Components” heading, some of which are best for touch users and others for keyboard users. “Input calendar”, however, provides a calendar for touch users _and_ an input field for keyboard users, offering the best of both worlds and is perhaps the simplest solution overall.

![Image 8: how to find date picker ui component](https://studio.uxpincdn.com/studio/wp-content/uploads/2023/09/how-to-find-date-picker-ui-component-1024x640.png.webp)
### Styling the date picker Component

UXPin Components are already designed to offer great user experiences, but you’ll probably want to style them to match your brand’s visual identity and app/website’s aesthetic. To do this, use the Properties panel on the right.

![Image 9: customizing date picker ui](https://studio.uxpincdn.com/studio/wp-content/uploads/2023/09/customizing-date-picker-ui-1024x640.png.webp)
If you’re using [UXPin Design System Libraries](https://www.uxpin.com/docs/design-systems/design-systems/) (especially Text Styles and Color Styles), you can utilize the Styles that you’ve already established to help maintain some degree of visual consistency between the date picker Component and the rest of your design.

To customize your component, select the Layer that you’d like to style, navigate to your UXPin Design System Library after clicking on the “Design System Libraries” icon (**⌥ + 2** / **alt + 2**), and then select the Style that you’d like to apply to the Layer.

![Image 10: date picker design](https://studio.uxpincdn.com/studio/wp-content/uploads/2023/09/date-picker-design-1024x640.png.webp)
## **Using real Components instead**

Rather than reinventing the wheel by inserting and styling the same Component over and over again, designers can use production-ready Components that’ve already been built by developers. You can pull them from [Git](https://www.uxpin.com/merge/git-integration), [Storybook](https://www.uxpin.com/merge/storybook-integration), or [NPM](https://www.uxpin.com/merge/npm-integration) (no coding required) and they’ll look and work just like the real thing (because they are). Learn about UXPin’s technology that makes this happen. [Request access today](https://uxpin.com/merge).

## Related
[Add wiki-links manually or run update_wikilinks.py]