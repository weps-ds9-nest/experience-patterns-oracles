# Summary:Select a single radio button by default in most cases. Reasons to deviate or not: expedite tasks, the power of suggestion, user expectations, safety nets.

Summary:Select a single radio button by default in most cases. Reasons to deviate or not: expedite tasks, the power of suggestion, user expectations, safety nets.

*   [Introduction](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-introduction-1)
*   [Historical Metaphor](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-historical-metaphor-2)
*   [Select a Radio Button by Default](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-select-a-radio-button-by-default-3)
*   [1. Give People Control and Align with Their Expectations](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-1-give-people-control-and-align-with-their-expectations-4)
*   [2. Expedite Tasks](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-2-expedite-tasks-5)
*   [3. Harness the Power of Suggestion](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-3-harness-the-power-of-suggestion-6)
*   [Overcome the Excuses](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-overcome-the-excuses-7)
*   [How to Determine the Best Default Radio-Button Choice](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-how-to-determine-the-best-default-radio-button-choice-8)
*   [Summary: Select One Radio Button by Default](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-summary-select-one-radio-button-by-default-9)
*   [Extra Credit Answer](https://www.nngroup.com/articles/radio-buttons-default-selection/#toc-extra-credit-answer-10)

## Introduction

You are probably wondering how anyone could muster enough words for an entire article about the humble, ubiquitous radio button—and specifically, whether the designers should choose one of the options to be selected by default or not. Before you hit the _Back_ button, think of the old adage "the devil is in the details," and that so many radio buttons today are downright devious. So read on to avoid creating a diabolical design.

First and foremost, a quick reminder of what radio buttons do: They display a set of mutually exclusive options from which a person may **select exactly one**. People sometimes [confuse radio buttons and checkboxes](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/), but checkboxes are the GUI widget to employ when users can select any number of the choices (zero, one, or many.)

![Image 1: 4 radio buttons with option 1 selected, options 2,3, and 4 not selected](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/radio-wireframe.png)

_A radio button wireframe._

In traditional application design, the first radio button in the list was always selected by default. But the unbridled world of website design challenged this practice, making it fairly common to have no radio button selected by default. Today’s websites, forms, and applications inconsistently select one or leave all radio buttons blank by default. If none of the buttons is selected by default, users have no way to revert to this original state after they’ve made a selection. The lack of a standard can be confusing to users.

The time of analog radios has long passed. The used Chevy Impala I drove (that is when the engine actually turned over) in the 1980’s boasted a radio with mechanical buttons, like the one in the image below.

![Image 2: mechanical radio with chrome buttons](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/radio_old-chevy.png)

_An example of a radio with mechanical buttons, found in older cars._

Using this and other radios of the age required physical strength to push in the buttons and change the station. You also needed a master’s degree to successfully “program” one of the buttons. (Extra credit: What are the steps to program one of these buttons to a radio station? Answer at the end of this article.)

The software radio button was modeled after these physical radio buttons. Skeuomorphism naysayers may baulk, but using metaphors that simulate the physical world can be helpful and engaging. However, in this particular case these antiquated radios are foreign to most of the web-user population today. This is an argument against matching this real-world metaphor.

A second reason for abandoning this unique metaphor is because the physical design itself was flawed. Namely, most people did not realize that it was possible to have no buttons selected, because there were no [perceived affordance](http://www.jnd.org/dn.mss/affordances_and.html) signals. In typical usage, pressing a button would pop out (deselect) the already selected button. But you could also go back to the “none selected” state by pulling quite hard on the selected button until it came out to the deselected state. How would people know this? They had to be told, read it in the owner's manual, or just plain guess it was possible. (My sister Deb told me when we were kids, and I thought she was Einstein from then on.)

This original design defect continues to mar today’s websites, applications, and mobile designs. Basically, designers don't know which way is up (or in or out) with the rules about default radio button selection.

## Select a Radio Button by Default

The main guideline for radio button design is to **select one of the radio buttons by default**(i.e., when the page loads, in the case of a web application.) This is good usability and elegant design. I say this not because I am waving a banner for traditionalism, or even for consistency. Rather the banners I’d parade in this case would be decorated with concepts such as the following:

*   user control,
*   expediting tasks, and
*   the power of suggestion.

## 1. Give People Control and Align with Their Expectations

One of the [10 heuristics of UI design](https://www.nngroup.com/articles/ten-usability-heuristics/) says that users should be able to undo (and redo) their actions. This means enabling people to set a UI control back to its original state. For most controls you may “un-choose” a selection you make. (Required elements may catch you with a note or error message later.) But you cannot click or tap a selected radio button to deselect it.

The finality of the action of selecting is not conveyed when none are selected by default. This interaction model is confusing and unexpected, and causes people to feel out of control. And it also instigates people to do crazy things, such as go back and possibly lose content, refresh the page, double- and triple-click (or tap) the radio button to deselect it, and act in other superstitious ways.

Selecting a radio button by default prevents these issues and communicates to the user from the start that he is required to choose one in the set.

## 2. Expedite Tasks

When a choice in a set of radio buttons is known to be the most desired or frequently selected one, it is very helpful to select this by default in the design. Doing this reduces the [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) and can save the user time and clicks.

For example, years ago I joined Care.com to find a dog sitter for my Cairn terrier, Columbo, when I traveled. After I found someone, I decided to unjoin the service. As I canceled my membership the site astutely presented a page with two radio buttons: one for unsubscribing and one for keeping my membership in case I needed backup care, or needed other types of care. (Perhaps my fig tree needed tending?)

The message the site presented--_Yes, switch my membership and save up to 83%_--may have sold some people on postponing canceling, as did placing the promotion in the first position in the radio-button list. But, understanding that most people really do want to unsubscribe if they have reached this particular point, the designers selected by default the radio button which reads _No thanks, continue downgrading my membership._ This default enabled me to just scan the choices and click the _Continue_ button, rather than needing to click and select the _No,_ and feeling annoyed by having to do that when I had just told the site I wanted to unsubscribe.

![Image 3: car.com message says you're almost done, but shows benefits of keeping the mebership](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/caredotcom_good-radio-selected.png)

_Care.com smartly made the radio button associated with canceling the membership the default selection._

On Massachusetts’ Department of Transportation site, the payment page for renewing a car registration offers payment methods: _Electronic Check_ or _Credit Card,_ but no default selection.

![Image 4: electronic check and credit card radio buttons are both blank](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/masdot_car-reg-renew.png)

A review of site [metrics](https://www.nngroup.com/courses/analytics-and-user-experience/) and placed orders could quickly determine the most popular payment method, tipping designers off on which of these should be the default selection.

## 3. Harness the Power of Suggestion

Designs with a radio button selected by default make a strong suggestion—an endorsement even—to the user. The default choice may lead the user into making the best decision, and may increase his confidence as he proceeds. In particular, default radio selections can assist the person, and sway a person in the direction in which the organization wants him to go.

### **Assist the Person**

Defaults help users. They are especially obliging in situations where the choices may be complex or unfamiliar. When the labels and descriptions are foreign, a default directs the user to the best choice among ones he may not understand. For example, one of Dropbox's install screens selects the radio button labelled _Typical_ to help people get their install started. Additionally, the term _Advanced_ juxtaposed against _Typical_ makes the latter more attractive to less savvy users. And the words _recommended_ and _normal_ also instill confidence.

![Image 5: typical radio is selected, advanced is not](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/dropbox_setup_6_setup-type.png)

_An install dialog in Dropbox assists users by offering a default selection._

### **Sway the Person**

It’s no secret that organizations have motives and often want to persuade their users to act in ways that are beneficial to them. [Default selections can coax people](https://www.nngroup.com/articles/the-power-of-defaults/) down a particular path. A default selection may also cause a person to perceive the organization a particular way, or may affect his feeling of belonging.

Take the example of donating money to a cause—a sensitive topic for people who are self-conscious about the amount they plan to donate. Consider how a person might react to the amounts suggested by the radio buttons, and especially to the selected default. Let’s think of 2 short scenarios to guide us:

_**Scenario 1: Person plans to give $30. He sees the radio buttons and:**_

*   decides that $30 is less than what the organization wants, so he does not donate at all. This situation is negative to the organization and user.
*   overextends himself to give the $50. The decision is positive to the organization (at least in the short term) and negative to the user.

_**Scenario 2: Person wants to donate $10,000. He sees the radio buttons and:**_

*   decides that giving all $10,000 is exorbitant and decreases his donation to a much smaller amount. This selection is negative to the organization.
*   follows the recommendation and gives $50 (and donates the rest of the $10K elsewhere.) Again, this decision is negative to the organization.

Occasionally, users’ assumptions may be wrong or they may go against the organization’s goals or best interest. They may also make the user feel alienated if his intended choice is very different from the available or suggested choices. A selected amount could be presumptuous, off-putting to some, and may lower donation amounts of others. So, to make the best selection, **be sure to know your organization’s goals and your users’ typical behavior.**

If you can’t confidently collect the information about your users, consider an alternative UI control (besides radio buttons with none selected.) Maybe do what the World Wildlife Fund does for their monthly donation section for the polar bears: an empty field with a suggested amount appearing after the field.

![Image 6: There is no default amount in a donation field](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/wwwf_polarbears_donation-empty-field.png)

_World Wildlife Fund allows people to type the amount they want to donate monthly, but makes a suggestion for the amount after the field._

In another example, the Environmental Defense Fund website suggests donation amounts between $25 and $5,000. Notwithstanding the default selection, the mere fact that there are proposed amounts sets the stage by telling users that the organization expects people to donate at least $25.

![Image 7: the $50 radio is selected, $25, $100, $500, $1,000, and $5,000 are blank](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/edf_radio-selected-by-default.png)![Image 8: Radio buttons wrap on the phone making it hard to tell which amount corresponds with which radio](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/edf_phone_default-select_cropped.png)

_The Environmental Defense Fund website sets $50 as the default donation, as seen in two [responsive-design](https://www.nngroup.com/articles/responsive-web-design-definition/) versions on a laptop (left) and a phone (right.)_

The radio button associated with $50 is selected by default. I don’t know exactly how EDF arrived at this default, but I can guess that they chose it to assists users, and that conceivably $50 is the most common donation amount. Or maybe the site is personalized or uses a cookie, and knows that $50 is what the person donated in the past.

But let’s assume for a moment that the motive is to sway people into [donating](https://www.nngroup.com/articles/donation-usability/) $50 or more. In this design people see that it’s plausible that people donate $5,000; the $50 is [trivial in comparison](http://www.nngroup.com/courses/credibility-and-persuasive-web-design/). So the site is basically saying, “People give 5,000, but we’d be happy with $50.” This humility may even charm some donators to bestowing $100 or $500.

**Design Notes**

*   Horizontal radio buttons are sometimes difficult to scan. As seen from the EDF examples, the horizontal arrangement of the radio buttons can make it challenging to tell with which label the radio button corresponds: the one before the button or the one after. This problem is even more noticeable when this EDF responsive-design site is viewed on a phone. Vertical positioning of radio buttons is safer.
*   Radio buttons are tiny in nature, and, thus, according to [Fitts’ law](http://www.nngroup.com/courses/hci/), they can be hard to click or tap. To enlarge the target area, let users select an option by clicking or tapping not just that button, but also the label or associated words. This is easier than having to acquire the tiny target of the button itself.

## Overcome the Excuses

Below I identify a few common defenses for leaving radios blank.

### **Not Knowing What Most Users Want or Do**

It is important to study users when suggesting any choices, and it is possible to do this effectively with methods listed in the next section of this article.

### **Avoiding a Presumptuous or Estranging Default Selection**

A radio button default selection that designers often struggle with is whether to select a gender or a designation such as Mr., Mrs., Ms., or Miss. Designers don't want to offend customers or risk addressing a person with the wrong designation, so they leave the radio buttons all blank by default. This doesn't solve the problem though, because even the order in which designations are presented may have an effect similar to that of a default selection. Better alternatives to no default selection include the following:

*   Study your user population to determine the designation most people fall under. Select it by default.
*   Ensure that the radio buttons are visible so the person can approve or change the selection.
*   If you already know who the user is (for example, via a role-based system,) select the correct designation.
*   Offer an open field in which people can type the designation, and the website does the work on the backend to keep the database clean.
*   Consider whether you need to ask for this information at all. Knowing the user’s designation does provide the opportunity to add a level of formality and respect to you future correspondences with the person. But if that gesture is not particularly important, you might take a cue form sites such as JohnDeereGifts.com and ask for the person’s name alone, with no designation.

![Image 9: The form asks for first name and last name, but not mr. mrs. ms. miss, etcis](https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/05/27/johndeeregifts_no-mr-mrs.png)

_JohnDeereGifts.com doesn’t ask for Mr., Mrs., Miss, Ms. designations at all._

### **Needing a Safety Net**

Some designers fear that people won’t see a default selection option. Or an organization’s attorneys or federal agencies mandate that users actively click and accept a choice. In some of these situations designs offer radios with no default selection. The user may be unable to submit a form, for example, until he has selected a radio button, or if he can submit the form he will get an error message scolding him to make a selection.

This is an unimaginative design safety net. It is unpleasant to deal with, and is an ungraceful way to force attention. Consider other options, such as:

*   Use a linear step-by-step process that leads people though the possible choices.
*   Design the page layout with adequate spacing, text, size, and color to direct users' attention to an important choice.
*   Consider restructuring the content and offering a checkbox for confirming a choice.
*   If simple enough, include the confirmation as part of the button name that proceeds or submits the page or dialog.

## How to Determine the Best Default Radio-Button Choice

Designers have many choices for UX research methods—rapid or involved, cheap or expensive, high or low confidence—to help them find the answer about what’s best for users. Start with these research methods to determine what a reasonable default may be:

*   track site [metrics](https://www.nngroup.com/courses/analytics-and-user-experience/), review past orders and selections (and consider personalization and cookies for repeat users)
*   [survey](https://www.nngroup.com/articles/keep-online-surveys-short/) users
*   conduct task analysis and [ethnographic studies](https://www.nngroup.com/consulting-field-studies/)
*   refer to [personas](https://www.nngroup.com/articles/persona/), stories, and scenarios

As for the business needs and desires, discuss with the powers that be what the business needs to excel, and direct people to those selections, overtly and scrupulously.

## Summary: Select One Radio Button by Default

Design questions and choices used in radio buttons in such a way a default selection is helpful and makes a suggestion in a positive way. If you are considering selecting no radio button by default, think hard about your reasons for doing so.

**Reasons for A Default Selection**

*   Match the metaphor of the old radio (Bad): This is not a good reason because it is not necessary (or likely helpful) to match this particular metaphor.
*   Expedite tasks (Good): Making a default selection is helpful if you have conducted task analysis and most users make the same choice.
*   Give people control and align with their expectations (Good): It is better to have a selected radio button by default, given that people cannot deselect and set the button back to its original state once one has been selected. A default selection sets the correct user expectation.
*   Power of suggestion (Good): Selecting is directive. Some things to watch out for though are being presumptuous, pushy, offensive, or alienating. Consider the content and the default selection, how users will react to it, and the effect the selection will have on the user and the organization in both the short and long term. Unless it’s been thoroughly tested (via observational methods as well as with metrics) and proven successful, avoid presumptuous default selections.

**Excuses for No Default Selection**

*   Not knowing what users want or do: In this and any design situation, it behooves us to know our users and what they want and need, and do most often.
*   Presumptuous or alienating choice: This is probably the most valid reason for not selecting a radio button by default. But consider whether you need to ask for the information at all, or whether you can use a different UI control to capture the data you need.
*   Safety net: Catch people, ensure they see and actively select a choice: There is probably a more elegant way to design the interaction than to expect the user to miss a command and catch him with an error message after the fact. Seek an alternate method to direct the users’ attention.

If you cannot confidently and contently provide a default selection in the list of radio buttons, consider using an alternate UI control that accommodates the particular situation and its goals and constraints.

Do you give up about how to “program” a station with those old-school, mechanical buttons? Here’s how to do it. Use the tuner dial to get to the station you want then locate the button to “program” the station to. Now pull that button OUT, past the "not selected" state. Pull it hard as though you are really trying to break the radio. Then push it back all the way in so it is selected. That works, usually. To test it, change the station, then press the button again and see if it tunes to the station you wanted it to. If it works, relax with nice bit of Neil Diamond. If it doesn't work then repeat, better.

**For more about radio buttons and other GUI widgets, also see our [Application Design for Web and Desktop](https://www.nngroup.com/courses/application-ux/) course.**

## Related
[Add wiki-links manually or run update_wikilinks.py]