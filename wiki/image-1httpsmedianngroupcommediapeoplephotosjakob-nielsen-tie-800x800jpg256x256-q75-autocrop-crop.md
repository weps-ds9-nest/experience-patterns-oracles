# ![Image 1](https://media.nngroup.com/media/people/photos/Jakob-Nielsen-tie-800x800.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg)

![Image 1](https://media.nngroup.com/media/people/photos/Jakob-Nielsen-tie-800x800.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg)

Summary:User interface guidelines for when to use a checkbox control and when to use a radio button control. Twelve usability issues for checkboxes and radio buttons.

I recently encountered the following box on a major website's registration page. It contains at least two design mistakes. See if you can find them before reading further.

Stay informed! Get updates about featured products, solutions, services and educational opportunities. Let Foobar Corp. and selected organizations provide you with information about other offerings.

May we send you updates using e-mail?
Yes, please use e-mail to send me information about other offerings.

If you prefer, we will not contact you using the data you provided in this instance.
Please do not use the contact details provided here to send me information about other offerings.

Mistake #1 is the primary focus of this article: The erroneous use of checkboxes where radio buttons should be. Because the two choices above are mutually exclusive, the page should present users with radio buttons, which restrict them to selecting exactly one option.

Mistake #2 is to present two questions in the first place, and then to put them in a big, verbose box. A single, shorter question would be far better here: "Yes, send me information about other featured products, solutions, services, and educational opportunities."

Ironically, with a single question, using a checkbox would have been correct because the user would be answering yes or no. The recommendation from [user testing of ecommerce sites](https://www.nngroup.com/reports/ecommerce-user-experience/ "Nielsen Norman Group report: Design guidelines for ecommerce user experience") is to **leave the checkbox blank by default**, so users must actively click it to opt in for further messages.

*   [When to Use Which Widgets](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/#toc-when-to-use-which-widgets-1)
*   [Additional Guidelines](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/#toc-additional-guidelines-2)
*   [Why These Guidelines Matter](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/#toc-why-these-guidelines-matter-3)

Ever since the first edition of  Inside Macintosh  in 1984, the rule has been the same for when to use checkboxes versus radio buttons. All subsequent GUI standards and the official W3C Web standards have included the same definition of these two controls:

1.   **Radio buttons** are used when there is a list of two or more options that are **mutually exclusive** and the user must select exactly one choice. In other words, clicking a non-selected radio button will deselect whatever other button was previously selected in the list.
2.   **Checkboxes** are used when there are lists of options and the user may **select any number** of choices, including zero, one, or several. In other words, each checkbox is independent of all other checkboxes in the list, so checking one box doesn't uncheck the others.
3.   **A stand-alone checkbox** is used for a single option that the user can turn on or off.

Sounds simple enough, right?

Yet I frequently encounter web pages that use radio buttons and checkboxes wrong. Even after twenty years, it's worth stating these guidelines once again.

## Additional Guidelines

1.   **Use standard visual representations.** A checkbox should be a small square that has a checkmark or an X when selected. A radio button should be a small circle that has a solid circle inside it when selected.
2.   **Visually present groups of choices as groups,** and clearly separate them from other groups on the same page. The boxed example above violates this guideline because the layout makes the two checkboxes appear to be addressing separate topics when theyre actually alternative options for a single topic. 
    *   **Use subheads to break up a long list of checkboxes** into logical groups. This makes the choices faster to scan and easier to understand. The risk is that users might view each subgroup as a separate set of options, but this is not necessarily fatal for checkboxes — each box is an independent choice anyway. A list of radio buttons, however, must always appear unified, so you cannot use subheads to break it up.

3.   **Lay out your lists vertically**, with one choice per line. If you must use a horizontal layout with multiple options per line, make sure to space the buttons and labels so that it's abundantly clear which choice goes with which label. In the following list, for example, it's difficult to see the correct radio button to click for option four. 
4.   **Use positive and active wording** for checkbox labels, so that it's clear what will happen if the user turns on the checkbox. In other words, avoid negations such as "Don't send me more email," which would mean that the user would have to check the box in order for something _not_ to happen. 
    *   Write checkbox labels so that users know both what will happen if they check a particular box, and what will happen if they leave it unchecked.
    *   If you can't do this, it might be better to use two radio buttons — one for having the feature on, and one for having it off — and write clear labels for each of the two cases.

5.   **If possible, use radio buttons rather than drop-down menus**. Radio buttons have [lower cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/ "Minimize Cognitive Load to Maximize Usability") because they make all options permanently visible so that users can easily compare them. Radio buttons are also easier to operate for users who have difficulty making precise mouse movements. (Limited space might sometimes force you to violate this guideline, but do try to keep choices visible whenever possible.)
6.   **Always offer a default selection for radio button lists**. By definition, [radio buttons always have exactly one option selected](https://www.nngroup.com/articles/radio-buttons-default-selection/), and you therefore shouldn't display them without a default selection. (Checkboxes, in contrast, often default to having none of the options selected.) 
    *   If users might need to refrain from making a selection, you should provide a radio button for this choice, such as one labeled "None." Offering users an explicit, neutral option to click is better than requiring the implicit act of not selecting from the list, especially because doing the latter violates the rule of always having exactly one option chosen.

7.   **Because radio buttons require exactly one choice, make sure that the options are both comprehensive and clearly distinct**. In [tests with older users](https://www.nngroup.com/reports/senior-citizens-on-the-web/ "Nielsen Norman Group report: Senior Citizens (Ages 65 and older) on the Web"), for example, people couldn't complete a form that required them to select their job because it didn't offer "retired" as an option. If it's impossible to be comprehensive, offer a button labeled "Other," supplemented by a type-in field.
8.   **Let users select an option by clicking on either the button/box itself or its label**: a bigger target is faster to click according to [Fitts's Law](http://www.asktog.com/columns/022DesignedToGiveFitts.html "AskTog: A Quiz Designed to Give You Fitts"). In HTML forms, you can easily achieve this by [coding each label with <label> elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label "Use of the <LABEL> element in HTML"), as I've done for the example with horizontal radio buttons above (to select that option, click on the word "Four"). In testing [web-based applications in Flash](https://www.nngroup.com/articles/ephemeral-web-based-applications/ "Alertbox: Ephemeral Web-Based Applications"), we found that user errors are further reduced by generous click zones that extend a few pixels beyond the visibly clickable area. (This effect can be hard to achieve in HTML, though some CSS hacks might do the trick.)
9.   **Use checkboxes and radio buttons only to change settings, not as action buttons** that make something happen. Also, the changed settings should not take effect until the user clicks the command button (labeled "OK" for example, or "Proceed to XXX" where "XXX" is the next step in a process). 
    *   If the user clicks the _Back_ button, any changes made to checkboxes or radio buttons on the page should be discarded and the original settings reinstated. The same guideline obviously holds if the user clicks a _Cancel_ button (though navigational web pages [don't need a cancel option](https://www.nngroup.com/articles/reset-and-cancel-buttons/ "Alertbox: Reset and Cancel Buttons") because the _Back_ button serves the same purpose).
    *   If the user first clicks _Back_ and then _Forward_, then it's most appropriate to interpret this sequence as an Undo-Redo pair, meaning that the appearance of the controls should show the user's changes as if the user had never clicked _Back_. These changes should still not take effect on the backend until the user clicks "OK" or an equivalent command.

## Why These Guidelines Matter

Am I just being picky when I insist on the correct use of checkboxes and radio buttons? No. There are [good usability reasons to follow GUI standards and use the controls correctly.](https://www.nngroup.com/articles/do-interface-standards-stifle-design-creativity/)

Most important, **[following design standards](https://www.nngroup.com/articles/the-need-for-web-design-standards/ "Alertbox: The Need for Web Design Standards") enhances users' ability to predict what a control will do** and how they'll operate it. When they see a list of checkboxes, users know that they can select multiple options. When they see a list of radio buttons, they know that they can only select one. (Of course, not every user knows this, but many do, especially since this has been a design standard since 1984.)

Because many people know how to operate standard GUI widgets, employing these design elements correctly [enhances users' sense of mastery](https://www.nngroup.com/articles/ideologies-of-web-design/ "Alertbox: Mastery, Mystery, and Misery: The Ideologies of Web Design") over technology. Conversely, **violating the standards makes the user interface feel brittle**— as if anything can happen without warning. Say, for example, that you assume you can click on a radio button without any immediate impact, and can thus consider your choices after making a selection but before hitting "OK." In such a case, it's jarring when a website violates this standard and unexpectedly moves you to the next page once you enter a selection. Worse, it makes you fear what may happen as you work with forms elsewhere on the site.

**The biggest usability problems for checkboxes and radio buttons come from labels that are vague, misleading, or describe options that are impossible for average users to understand**. Contextual help can alleviate the latter problem, but it's still best to user test any important set of interaction controls. Luckily, checkboxes and radio buttons are easy to test using [paper prototyping](https://www.nngroup.com/reports/paper-prototyping-training-video/ "Nielsen Norman Group: Paper Prototyping – A How-To Training Video"), so you don't need to implement anything to see if users understand the labels and can use the widgets correctly.

No professional interaction designer would make the mistake of using checkboxes when radio buttons are called for. The distinction between these two controls is one of the first things taught in any interaction design class. So here's a final reason to use the right widget: if you don't, you'll be taken for an amateur.

## Learn More:

## Related Articles:

*   [Top 10 Application-Design Mistakes Jakob Nielsen and Page Laubheimer · 13 min](https://www.nngroup.com/articles/top-10-application-design-mistakes/?lm=checkboxes-vs-radio-buttons&pt=article)
*   [Website Forms Usability: Top 10 Recommendations Kathryn Whitenton · 6 min](https://www.nngroup.com/articles/web-form-design/?lm=checkboxes-vs-radio-buttons&pt=article)
*   [Ephemeral Web-Based Applications Jakob Nielsen · 10 min](https://www.nngroup.com/articles/ephemeral-web-based-applications/?lm=checkboxes-vs-radio-buttons&pt=article)
*   [Progressive Disclosure Jakob Nielsen · 7 min](https://www.nngroup.com/articles/progressive-disclosure/?lm=checkboxes-vs-radio-buttons&pt=article)
*   [Popups: 10 Problematic Trends and Alternatives Anna Kaley · 12 min](https://www.nngroup.com/articles/popups/?lm=checkboxes-vs-radio-buttons&pt=article)
*   [Indicators, Validations, and Notifications: Pick the Correct Communication Option Kim Flaherty · 9 min](https://www.nngroup.com/articles/indicators-validations-notifications/?lm=checkboxes-vs-radio-buttons&pt=article)

## Related
[Add wiki-links manually or run update_wikilinks.py]