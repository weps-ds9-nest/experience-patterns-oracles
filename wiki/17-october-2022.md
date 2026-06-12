# 17 October 2022

17 October 2022

In 2021 I worked on a service that allows teacher training providers to set up interviews with trainees.

We needed to find the best way for users to enter a time.

But it’s harder than it seems because:

*   a time is made up of hours, minutes and a period (AM or PM)
*   there are many different formats for the same time like ‘12am’ ‘24:00’, 12.00am’, ‘12a.m.’ and ‘00’

We explored multiple patterns like autocompletes and multi-input fields.

But after several rounds of research and data analysis we ended up with something much simpler.

Here’s what I’ll cover:

*   how to avoid the complexity of entering time in the first place
*   the 4 different patterns we considered
*   the 1 simple pattern that works the best and why

## How to avoid making users enter a time

The best form field is the one we don’t even ask users to fill out.

For example, I’m working on a service that has a closing time field for a job advert.

Ideally, we wouldn’t ask users to enter a time at all - instead we could automatically set the closing time to 11:59pm.

But as our users need greater control we provide 4 common times as radio buttons.

![Image 1](https://adamsilver.io/assets/images/designing-a-time-input/radios.png)

Radio buttons with options for 9am, 12pm, 5pm and 11:59pm

## Different ways of entering a time

There are four approaches:

1.   Native time input
2.   Multiple inputs
3.   Autocomplete
4.   Single input

Exploring each one will show you why I recommend the single text input.

### Solution #1: Using the native time input (`type="time"`)

As usual, the first approach to look at is what browsers give us for free - the native time input.

It works differently depending on the browser or device.

Chrome on desktop, for example, gives users a text input with slot for the hour and minute separated by a colon.

It also provides a clock icon, which when clicked reveals a menu to select the hour and minute.

![Image 2](https://adamsilver.io/assets/images/designing-a-time-input/time-input--chrome.png)

Chrome’s native time input

This is problematic for a few reasons.

Firstly, once the hour has been selected, focus is moved automatically to the minute slot. If the user made a mistake, they have to move the focus back to the hour slot.

Due to the colon, it may not be clear that the focus can be moved back by pressing Left. I think a lot of users will opt to use their mouse. Either way it’s long winded.

Secondly, the colon cannot be selected even though it’s inside the box. This is misleading because normally the contents of an input can be selected.

Thirdly, it’s not clear that the clock icon reveals a menu or what that menu will consist of.

Finally, users cannot cut and paste a time into the input.

Chrome on Android gives users an empty text input with a little down arrow. When focused it reveals a dial.

![Image 3](https://adamsilver.io/assets/images/designing-a-time-input/time-input--android.png)

Android’s time input

This is also problematic.

1.   Before the user focuses the input, it looks a bit like a select box due to the down arrow. Opening a dial may be unexpected.
2.   The dial isn’t particulary intuitive and has action labels that cannot be customised.
3.   Sometimes hint text is needed - but that’s covered up by the dialog.

(Note: browsers that lack support for the native time input will get a standard text input.)

### Solution #2: Using multiple inputs

The second approach involves using multiple inputs for:

*   hour - as a text input or select box
*   minute - as a text input or select box
*   AM or PM - as a select box or radio buttons

![Image 4](https://adamsilver.io/assets/images/designing-a-time-input/multiple-fields.png)

Multiple inputs for hours, minutes and AM or PM

This avoids having to deal with different formats.

But [select boxes should be used as a last resort](https://www.youtube.com/watch?v=CUkMCQR4TpY). And [multiple inputs are problematic](https://adamsilver.io/blog/form-design-multiple-inputs-versus-one-input/) because:

*   they stop users from cutting and pasting
*   they require more effort to use
*   they can be difficult to label (‘AM or PM’ is a bit awkward here)

(Note: the input for ‘AM and PM’ is needed because otherwise some users incorrectly enter ‘12’ or ‘00’ for midnight.)

### Solution #3: Using an autocomplete

The third approach is to use an autocomplete input. This is like a text input and a select box combined.

![Image 5](https://adamsilver.io/assets/images/designing-a-time-input/autocomplete.png)

Google Calendar’s autocomplete input

Clicking the input reveals a list of times - typically at 30 minute intervals.

Users can select a time or type to narrow down the suggestions.

The problem with this approach is that:

*   users are less aware of how to operate an autocomplete
*   users may enter a time in 24 hour format with the options shown in a 12 hour format (see above screenshot)
*   [making an accessible autocomplete is hard](https://adamsilver.io/blog/building-an-accessible-autocomplete-control/)
*   autocompletes rely on JavaScript which means a non-JavaScript solution needs to be considered before enhancement

### Solution #4: Using a single text input

The final approach - which I recommend - uses a single text input for time.

![Image 6](https://adamsilver.io/assets/images/designing-a-time-input/single-input.png)

A single input for time

It works well. It’s consistent across all browsers and devices. Users type what they like.

My research shows that using a single input works very well as long as you [accept a wide range of formats](https://bat-design-history.netlify.app/manage-teacher-training-applications/allowing-a-wider-range-of-input-formats-for-interview-time/).

The one pushback is the effort needed to accept all these formats.

But I don’t count this as a problem because:

*   it’s doing the hard work to make it simple
*   it’s far easier to build than an autocomplete
*   we have to do this anyway when considering progressive enhancement
*   it’s not that much effort to build (we used [Timeliness](https://github.com/adzap/timeliness) with minimal configuration)

I also want to highlight that even:

*   if research showed that an autocomplete works better we’d still need to use a single input [when JavaScript is unavailable](https://adamsilver.io/blog/javascript-isnt-always-available-and-its-not-the-users-fault/)
*   if research showed that the native time input works best, we’d still need to use a single input for browsers that lack support

So we may as well start with a single input and prove through research that it’s worth the extra effort of doing anything more.

## Related
[Add wiki-links manually or run update_wikilinks.py]