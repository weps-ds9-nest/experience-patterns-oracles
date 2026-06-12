# You fill out a form. Everything looks complete. Then, you notice that the “Submit” button is still disabled. And you can’t help but wonder: “What’s going on?”

You fill out a form. Everything looks complete. Then, you notice that the “Submit” button is still disabled. And you can’t help but wonder: “What’s going on?”

For quite some time, we’ve been told that disabling a “Submit” or “Save” button until a form is valid is best practice, both from a coding and UX perspective. The idea is to prevent users from accidentally submitting incomplete or incorrect information, and the reasoning behind it seems solid:

*   **Prevents error states before they happen**: By preventing submission until the form is valid, we avoid unnecessary error messages and backend validations.
*   **Helps users understand what’s missing or invalid**: It guides the user by making it clear that something still needs to be completed or corrected.
*   **Reduces frustration from failed form submissions**: Users aren’t left wondering why their submission failed; the form enforces correctness upfront.

But is that the full story? Are there deeper considerations to take into account? Is this truly the ultimate best practice for forms and buttons?

As a disclaimer, I personally believe that there’s rarely a one-size-fits-all solution, especially in UX. Context, user needs, and the purpose of the form should all be taken into account. Even if your organization has followed one practice for years, it’s worth questioning and revisiting those decisions. That kind of reflection is extremely healthy.

And now, let’s start!

## The case against disabled buttons

As I hinted in the title of this article, there’s a bit of a debate around this topic. One of the most prominent voices questioning this practice is Adam Silver. While researching for this article, I found his piece on the topic referenced nearly everywhere. It’s definitely worth examining what he says and analysing it critically.

In his article **“**[**The Problem with Disabled Buttons and What to Do Instead**](https://adamsilver.io/blog/the-problem-with-disabled-buttons-and-what-to-do-instead/)**”**, Adam Silver argues that disabled buttons can be misleading and inaccessible. They are often hard to spot, can feel broken, and typically don’t provide useful feedback.

Take this disabled button for example:

Kotak Net Banking form showing an inaccessible, disabled submission button.

Using my favourite [contrast checker](https://colourcontrast.cc/), it’s immediately clear that this button fails in terms of accessibility. And if you, like me, prefer lower screen brightness, the button can become almost invisible, blending into the background.

Screenshot showing that the disabled button fails to meet accessibility standards.

From an accessibility standpoint, it gets worse: sometimes these buttons aren’t even reachable by keyboard or screen reader. In those cases, users with disabilities may be completely unable to understand that an action is even available, let alone how to complete it.

So, even with the best of intentions, disabling buttons can cause real harm to usability and accessibility.

## Ben Nadel’s take

Another relevant voice in the debate is Ben Nadel. In his article **“**[**The User Experience (UX) of Disabled Form Buttons**](https://www.bennadel.com/blog/4419-the-user-experience-ux-of-disabled-form-buttons.htm)**”**, he starts pretty strongly by stating the following:

> “By default, form buttons aren’t disabled […] until a web developer decides to get ‘clever’ and starts disabling buttons. […] Unfortunately, many developers are not quite as clever as they think they are.”

This is a reality check for many of us. Beyond the cheeky tone, Nadel makes an excellent argument: if a user feels like they can submit an incomplete form, and the system lets them try, the form itself is already communicating poorly. Something is missing in the UI. Something is misleading them into thinking it’s ready. The form is providing a bad user experience. And disabling the button solves the wrong problem actually creating new ones in the process, as we discussed above.

But let’s see another example as well.

Nadel also notes that on mobile devices, auto-filled or pasted input often doesn’t trigger a form’s validation logic. A user might complete a form correctly, but the button remains disabled unless they manually interact with every field. That’s confusing, and frustrating. That’s bad UX.

## So what’s the middle ground?

Both sides make valid points, and once again, I believe that the best solution depends on the context. There are definitely cases where disabling a button makes sense. For example, immediately after submission, to prevent double submissions. But disabling buttons before a form is valid? That’s trickier.

As Nadel mentions:

> “If you feel the need to disable a button to prevent user errors, maybe it’s time to reconsider how your form is designed in the first place”.

## A better approach

Good UX is about communication. Instead of using a disabled button as a gatekeeper, help your users by:

*   Providing **clear instructions and hints** for each input.
*   Showing **real-time validation messages** for incorrect or missing fields.
*   Visually indicating which fields are **required**.
*   Using tooltips, helper text, and contextual cues to **guide the user**.

[**“A Complete Guide to Live Validation UX**](https://www.smashingmagazine.com/2022/09/inline-validation-web-forms-ux/)**”** is a great starting point if you’d like to explore these ideas in more depth. Especially when it comes to guiding users through form completion with clarity and real-time feedback.

Scrabble tiles arranged to spell out the phrase ‘Allow for error’. Credit: Brett Jordan — Unsplash

That doesn’t mean we should let users submit completely broken forms. But instead of throwing up a wall, we can guide them with confidence and clarity.

And if, after all considerations, you still prefer to disable your “Submit” or “Save” buttons, it doesn’t cost much to explain why that’s necessary. Because in the end, any developer can disable a button, but a truly clever one designs with empathy, communicates with intention, and earns the user’s trust through clarity, not control.

Thank you for taking the time to read this article. I am looking forward to hearing your opinions and starting our own debate!

### Resources

*   [https://adamsilver.io/blog/the-problem-with-disabled-buttons-and-what-to-do-instead/](https://adamsilver.io/blog/the-problem-with-disabled-buttons-and-what-to-do-instead/)
*   [https://uxplanet.org/disabled-buttons-in-user-interface-4dafda3e6fe7](https://uxplanet.org/disabled-buttons-in-user-interface-4dafda3e6fe7)
*   [https://www.bennadel.com/blog/4419-the-user-experience-ux-of-disabled-form-buttons.htm](https://www.bennadel.com/blog/4419-the-user-experience-ux-of-disabled-form-buttons.htm)
*   [https://ux.stackexchange.com/questions/9788/disabled-submit-button-on-form-vs-allow-submit-then-show-errors](https://ux.stackexchange.com/questions/9788/disabled-submit-button-on-form-vs-allow-submit-then-show-errors)

## Related
[Add wiki-links manually or run update_wikilinks.py]