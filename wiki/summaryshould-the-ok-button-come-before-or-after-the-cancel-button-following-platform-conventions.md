# Summary:Should the OK button come before or after the Cancel button? Following platform conventions is more important than optimizing an individual dialog box.

Summary:Should the OK button come before or after the Cancel button? Following platform conventions is more important than optimizing an individual dialog box.

We get countless questions about small details in UI design that _don't matter much_ to the overall user experience. One classic is the **order of buttons** in dialog boxes:

*   _OK / Cancel_
*   _Cancel / OK_

Both are reasonable choices, and people can argue for hours about their preferences:

*   Listing _OK_**first** supports the **natural reading order** in English and other languages that read left-to-right. Many other button sets have a natural progression (say, _Yes / No_ or _Previous / Next)_. You should always list these so that the reading order matches the logical order — in this case, _OK / Cancel_. Further, assuming users need _OK_ much more frequently than _Cancel_, it's better to place this option first so that keyboard-driven users who tab to the buttons can get to their preferred choice with one less keystroke.
*   Listing _OK_**last** improves the flow, because the dialog box **"ends" with its conclusion**. Also, as with _Previous/Next_, you could argue that _OK_ is the choice that moves the user forward, whereas _Cancel_ moves the user back. Thus, _OK_ should be in the same location as _Next_: on the right.

In cases like this, it often **doesn't matter** what you do. Either choice has good arguments in its favor, and no choice is likely to cause usability catastrophes. It might save some users 0.1 seconds if you pick the "right" choice for certain circumstances, but it's simply not worth it to conduct sufficiently elaborate research to find out what that choice is. Better to spend your usability resources on those things that can [change your key performance indicators by 83%](https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/ "Alertbox: Usability ROI Declining, But Still Strong") or more. (Critical application design issues are covered further in the full-day [course on Application Design](https://www.nngroup.com/courses/application-ux/).)

So, to make this specific choice — as well as many other small choices in application design — it's best to follow the **platform GUI standard**. Applying consistent design that follows user expectations saves people much more time (and many more mistakes) than doing something that might be a tiny bit more optimal for your application but introduces an inconsistency.

*   [Inconsistency Costs More Time than It Saves](https://www.nngroup.com/articles/ok-cancel-or-cancel-ok/#toc-inconsistency-costs-more-time-than-it-saves-1)
*   [Dialog Buttons for Web-Based Apps](https://www.nngroup.com/articles/ok-cancel-or-cancel-ok/#toc-dialog-buttons-for-web-based-apps-2)

## Inconsistency Costs More Time than It Saves

**Deviate from the standard, and you'll easily cost users several minutes** — or possibly hours — as they overlook or misuse UI elements. The time people spend pondering inconsistencies typically sums to much more than the small savings you'll hypothetically derive from a specialized design.

Sadly, the  Windows User Experience Guidelines  differ from the  Apple Human Interface Guidelines  when it comes to the sequence of _OK / Cancel_ buttons:

*   Windows puts _OK_ first
*   Apple puts _OK_ last

If you're designing a desktop application for one of these two personal computer platforms, your choice is easy: **Do what the platform owner tells you to do**.

## Dialog Buttons for Web-Based Apps

If you're designing a **web-based application**, the decision is harder, but you should probably go with the **platform preferred by most of your users**. Your server logs will show you the percentage of Windows vs. MacOS users for your specific website or intranet. Of course, Windows generally has many more users, so if you can't be bothered to check the logs, then the guideline that will apply to most situations is:

*   **_OK_ first, _Cancel_ last**, as in this screenshot from Office 2007:

![Image 1: Screenshot from Office 2007, showing buttons labeled 'Save' and 'Cancel'.](https://media.nngroup.com/media/editor/alertbox/ok-cancel-buttons.gif)

The screenshot illustrates two additional guidelines for dialog box buttons:

*   It's often better to **name a button to explain what it does** than to use a generic label (like "OK"). An explicit label serves as just-in-time help, giving users more confidence in selecting the correct action.
*   **Make the most commonly selected button the [default](https://www.nngroup.com/articles/the-power-of-defaults/ "Alertbox: The Power of Defaults") and highlight it** (except if its action is particularly dangerous; in those cases, you want users to explicitly select the button rather than accidentally activating it by hitting _Enter_).

## Related
[Add wiki-links manually or run update_wikilinks.py]