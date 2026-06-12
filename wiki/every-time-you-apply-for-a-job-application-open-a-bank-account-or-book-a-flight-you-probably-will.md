# Every time you apply for a job application, open a bank account or book a flight, you probably will be typing in your **date of birth**. As designers, we don’t just care about the completion rates, but also **completion times** and the accuracy of input.

Every time you apply for a job application, open a bank account or book a flight, you probably will be typing in your **date of birth**. As designers, we don’t just care about the completion rates, but also **completion times** and the accuracy of input.

We also want to support browser’s auto-fill and minimize mistakes. To achieve the last goal, we often rely on a **date-picker-widget** (native or custom) or a group of drop-downs.

It turns out that both solutions are **suboptimal**, and unnecessary — and they often cause more accessibility issues that can be avoided with a much simpler technique.

## The Pitfalls Of Native Date Pickers [#](https://smart-interface-design-patterns.com/articles/birthday-picker/#the-pitfalls-of-native-date-pickers)

Unfortunately, **native date pickers**, prompted by `<input type="date">`, come along with [plenty of accessibility nightmares](https://www.hassellinclusion.com/blog/input-type-date-ready-for-use/). At the moment of writing, when used out-of-the-box, they **aren’t a very accessible choice** for pretty much any kind of date input. Not only are there plenty of screen reader issues, but also focus and layout issues as well as confusing and generic error messages.

[![Image 1: https://vimeo.com/548336844](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/birthday-picker/birthday-picker-calendar-inaccessible-keyboard-issues.png)](https://smart-interface-design-patterns.com/articles/birthday-picker/A%20screenshot%20of%20a%20calendar%20view)

A calendar view with very strict input requirements. Accessible only for mouse users. The keyboard input is disabled. It took me 52 seconds (!) to provide my birthday. [(Video preview)](https://vimeo.com/548336844)

On top of that, many implementations **disable keyboard input** altogether, requiring customers to use a native date picker’s calendar widget exclusively to reduce mistakes. Without a keyboard input fallback, users have to embark on a long-winded journey between days, months and years, taking up **dozens and dozens of taps or clicks**.

As humans, we usually know our birthday, and we don’t really need to look it up in a calendar. Yet the interface requires us to navigate between dates, and then find our date in the calendar overview once we get there. This is useful when booking a flight, but not very useful when typing a birthday.

## The Pitfalls of Drop-Downs [#](https://smart-interface-design-patterns.com/articles/birthday-picker/#the-pitfalls-of-drop-downs)

Compared to native date pickers, **drop-downs** seem to be much faster and easier to navigate. They are accessible by default, plus rather than navigating between months and years, it’s enough to locate the right numbers in 3 lists — days, months and years.

[![Image 2: https://www.hassellinclusion.com/blog/input-type-date-ready-for-use/](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/birthday-picker/date-of-birth-ios-wheel.png)](https://smart-interface-design-patterns.com/articles/birthday-picker/A%20screenshot%20of%20iOS%20calendar)

The iOS calendar reels are shown after tapping onto the date control. [(Image source)](https://www.hassellinclusion.com/blog/input-type-date-ready-for-use/)

[But drop-downs are still slow](https://designnotes.blog.gov.uk/2013/12/05/asking-for-a-date-of-birth/). They have [zooming issues](https://twitter.com/JoshWComeau/status/1379782931116351490). Pinching scrollable options is tiring. **They take up a lot of space**. The list of years is long. And when specifying the input, we need to tap the control, then scroll (usually more than once), find and select the target, and continue to the next dropdown. [It’s not exhilarating either](https://medium.com/re-write/you-know-what-fuck-dropdowns-5b29151eddd5).

That’s why [dropdowns are considered the UI of last resort](https://www.lukew.com/ff/entry.asp?1950), and usually replaced with buttons (e.g. for filters), toggles, segmented controls, or autocomplete boxes. Dropdowns can be useful for a long list of selections; but “operating” them takes a lot of time, and it’s not comfortable either.

## The Default Values Dilemma [#](https://smart-interface-design-patterns.com/articles/birthday-picker/#the-default-values-dilemma)

And then there is a question about default values. While with dropdowns we default to no input whatsoever (mm/dd/yyyy), with a date picker we need to provide some starting point. In the latter case, ironically, the “starting” date usually happens to be just around the date of when the form is filled. This doesn’t appear optimal of course, but what should be the _right_ date? We need to start _somewhere_, right?

[![Image 3: https://airbnb.io/projects/react-dates/](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/birthday-picker/birthday-picker-airbnb-menu.jpg)](https://smart-interface-design-patterns.com/articles/birthday-picker/A%20screenshot%20of%20airbnb.com)

When a date-picker with default values makes sense: when booking flights or vacation. [Open sourced](https://airbnb.io/projects/react-dates/) by AirBnB. [(Video preview)](https://vimeo.com/548336844)

Well, **there really isn’t a right date**. We could start early or late, 3 months ago or tomorrow, but in the case of a birthday picker, all of these options are pure guesswork. And as such, they are somewhat frustrating: without any input, customers might need to scroll all the way from 1901 to the late 1980s, and with some input set, they’ll need to correct it, often jumping decades back and forth.

No matter what choice we make, we will be **wrong almost all the time**. This is likely to be different for a hotel booking website, or a food delivery service, and plenty of other use cases — just not birthday input.

## Designing A Better Birthday Input [#](https://smart-interface-design-patterns.com/articles/birthday-picker/#designing-a-better-birthday-input)

If somebody asks you for your birthday, you probably will have a particular string of digits in mind. It might be ordered in dd/mm/yyyy or mm/dd/yyyy, but it will be a string of 8 digits that you’ve been repeating in all kinds of documents since a very young age.

We can tap into this simple model of what a birthday input is with a **simple, single-input field** which would combine all three inputs — day, month, and year. That would mean that the user would just type a string of 8 numbers, staying on the keyboard all the time.

[![Image 4: https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/c616aff8-a308-4a4c-823e-93b03f930698/7-birthday-picker.png/](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/birthday-picker/birthday-picker-single-inputs.png)](https://smart-interface-design-patterns.com/articles/birthday-picker/A%20screenshot%20of%20a%20good%20input)

Using one input for a date is ambiguous and difficult to validate. Using multiple inputs for date is not ambiguous, and much easier to validate. Designed by [Adam Silver](https://adamsilver.io/blog/form-design-multiple-inputs-versus-one-input/). [(Large preview)](https://adamsilver.io/blog/form-design-multiple-inputs-versus-one-input/)

However, this approach brings up a few issues:

*   we need to support **auto-formatting and masking**,

*   we need to explain the position of the day/month input,

*   we need to support the behavior of the Backspace button across the input,

*   we need to **support jumps** into a specific value (e.g. month),

*   we need to minimize rage clicks and navigation within the input to change a specific value on mobile devices,

*   If auto-making isn’t used, we need to come up with a set of **clean-up and validation rules** to support any kind of delimiters.

In his book on [Form Design Patterns](https://formdesignpatterns.com/), Adam Silver argues that [using multiple inputs instead of one input](https://adamsilver.io/blog/form-design-multiple-inputs-versus-one-input/) is rarely a good idea, but it is a **good option for dates**. We can clearly communicate what each input represents, and we can highlight the specific input with focus styles. Also, validation is much easier, and we can communicate easily what specific part of the input seems to be invalid, and how to fix it.

To explain the input, we’d need to provide **labels** for the day, month and year, and perhaps also show an example of the correct input. [The labels shouldn’t be floating labels](https://www.smashingmagazine.com/2021/03/floating-labels-performance-lighthouse/) but could live comfortably above the input field, along with any hints or examples that we might want to display. Plus, every input could be highlighted on focus as well.

[![Image 5: https://design-system.service.gov.uk/components/date-input/](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/birthday-picker/date-of-birth-input-separate-input-fields.jpg)](https://smart-interface-design-patterns.com/articles/birthday-picker/A%20screenshot%20of%20a%20Design%20pattern)

Design pattern, as [suggested](https://design-system.service.gov.uk/components/date-input/) by Gov.UK team. [(Jump to the demo)](https://design-system.service.gov.uk/components/date-input/date-of-birth/index.html)

Over the years, I couldn’t spot a single problem with this solution throughout years of testing, and it’s not surprising the pattern [being used on Gov.uk](https://design-system.service.gov.uk/components/date-input/) as well.

## When You Need A Date Picker After All [#](https://smart-interface-design-patterns.com/articles/birthday-picker/#when-you-need-a-date-picker-after-all)

While the solution above is probably more than enough for a birthday input, it might not be good enough for more general situations. We might need a date input that’s less literal than a birth day, where customers will have to pick a day rather than provide it (e.g. _“first Saturday in July”_).

For this case, we could enhance the three input fields with a **calendar widget** that users could use as well. A default input would depend on either the current date, or a future date that most customers tend to choose.

[![Image 6: https://mcusercontent.com/16b832d9ad4b28edf261f34df/images/6aa970a5-fd9e-62a6-cb7d-1c2cf4590801.png](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/birthday-picker/birthday-picker-separate-inputs.png)](https://smart-interface-design-patterns.com/articles/birthday-picker/A%20screenshot%20of%20a%20simple%20code%20example%20for%20the%20Memorable%20date%20pattern)

Adam provides a simple [code example](https://nostyle.herokuapp.com/components/memorable-date) for the Memorable date pattern in his [NoStyle Design System](https://nostyle.herokuapp.com/).

Adam provides a simple [code example](https://nostyle.herokuapp.com/components/memorable-date) for the Memorable date pattern in his [NoStyle Design System](https://nostyle.herokuapp.com/components/memorable-date). It solves plenty of development work and avoids plenty of accessibility issues, and all of that by avoiding tapping around calendar widgets or unnecessary scrolling around dropdown wheels.

## Wrapping Up [#](https://smart-interface-design-patterns.com/articles/birthday-picker/#wrapping-up)

Of course, a good form control depends on the kind of date input that we are expecting. When we ask our customers about their **date of birth**, we are asking for a very specific date — a very specific string, referring to an exact day, month, and year.

In that case, a **drop-down is unnecessary**. Neither is a calendar look-up, defaulting to a more-or-less random value. If you do need one, avoid native date pickers and native drop-downs if possible and use an accessible custom solution instead. And rely on three simple input fields, with labels and explanations placed above the input field.

## Related
[Add wiki-links manually or run update_wikilinks.py]