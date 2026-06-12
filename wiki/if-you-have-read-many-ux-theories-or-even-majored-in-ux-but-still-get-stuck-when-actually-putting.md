# If you have read many UX theories or even majored in UX but still get stuck when actually putting it into practice, you are not alone.

If you have read many UX theories or even majored in UX but still get stuck when actually putting it into practice, you are not alone.

The year 2022 counted as my fourth year of designing SaaS products. Like thousands of other practitioners in the product field, at some point, I read the book The Design of Everyday Things, the bible of UX study. I immediately got the jargons: that it is all about discoverability, making the experience seamless, and there is no such thing as human error — only bad design. But how to actually make good design? I found it troublesome at first to find relevant sources, especially for SaaS products. That is why this article is written with a focus on Saas applications.

This article assumes you have been familiar with the terms coined in the book, but if you have not, feel free to refer to my [summary](https://www.notion.so/The-Design-of-Everyday-Things-3951f19e66da45f88443c5be3bfc2d38).

## Designing the visual aspects

Generally speaking, SaaS products’ interface is not various in style, the pages are mainly filled with navigation bars, tables, and dashboards. In fact, their signifiers and mapping logic ([Gestalt’s law of proximity](https://www.nngroup.com/articles/gestalt-proximity/)) are pretty basic with the CTAs placed on the side of the screen, whereas the center is kept for the main content, some include tabular data with the pagination at the bottom of the page.

OneDrive allows users to switch team spaces on the sidebar, whereas the main content takes most of the screen space.

Source: OneDrive & Slack. Using a similar structure to split the menu bar and the content.

Source: Salesforce. Displaying a more customizable menu within tabs and pinned pages.

Since the structure is quite similar, designers can just refer to some existing libraries out there. I personally look up to [Carbon](https://carbondesignsystem.com/components/overview/), [Ant Design](https://ant.design/components/overview/), [Ant Design Pro](https://procomponents.ant.design/en-US/components/), [Ant Design Charts](https://charts.ant.design/en/examples/gallery), [Essential JS2](https://ej2.syncfusion.com/home/), and [ReTool](https://retool.com/). These few are my go-to tools and more often than not, they fulfill most of the design requirements and allow me to spend more time on the research and the UX design bits. Those libraries are mostly great, but often we build for specific use for specific users with different backgrounds. The cultural differences and specific use cases have to always be kept in mind, like when displaying the date format, should it be DD/MM/YYYY or YYYY/MM/DD or any other way? Another example is a table that has two columns of “Debit Amount” and “Credit Amount”. Yes, the definition always remains the same, “debit” simply means an increase in assets or a decrease in liabilities. But imagine a banking system that tracks how much cashback that has been given to the account holders. Obviously, it’s a debit transaction from the user’s perspective, but a credit from the bank which might be better indicated by “-” symbol and red color. Unless we are designing the client-facing product, then it might as well be shown in green with the “+” symbol. Things don’t stop there and get even more complicated when the bank staff needs to check both internal and client-facing platforms, how do we reduce the possible error made by the staff when they are seeing two different perspectives on two platforms? That would be a challenge and therefore, designers need to keep in mind that a library is just a tool, they probably don’t provide many specific use cases.

Source: Sinopac Bank’s client-facing website. Good distinction for users to know money in and out.

Source: AntD framework. Like any flexible library, designers are encouraged to not blindly copy the components to their projects, instead of thinking about how to fit their use cases.

## Designing the technical aspects

It is important to note that SaaS products mainly serve B2B customers. The information a company requires is far more than individuals, and it often causes the interface to look more complicated. Not to mention the cost of clicking the wrong button could literally mean a million-dollar loss. Is the user the one to blame? Chapter 5’s title of the book puts it right to the point.

> “Human errors? No, bad design” — Don Norman

The product team is highly encouraged to focus on the holistic view of the whole organization, rather than a single task or a user flow. Especially when there are some external factors to consider. An example would be 24/7 customer service work, they have got long work hours, a few shift-workers colleagues doing the same tasks with a lack of documentation, and need to multitask in a limited time (when the customer is on the call). I have also observed a department of 5 members designated for manually checking tens of thousands of bank transactions on paper — on. a. daily. basis. — only to label the transaction as “successful” in the system. At this point, we do not need to talk about UX and user pain points first, but instead the value proposition for the system they use. The core value of its business needs to be redefined.

Paraphrasing Don Norman, computers are good with accuracy, but humans are not. Let alone the human errors that can be made, this administrative job can be frustrating and the employee turnover is relatively high. Imagine we can automate those tasks, how much more time will the business have to focus on business development? How many customers wouldn’t need to wait on the call line to get their problems solved? How happy are the operators going to be? Designing solutions to a problem should not only be based on asking what the users want.

> “If I had asked people what they wanted, they would have said faster horses.” — Henry Ford

The system has to help the users by doing some validations both on the frontend and backend sides. An easy most commonly seen example, filling an input text is much more straightforward with the frontend validation rather than waiting for the user to submit.

Source: Carbon Design System. An immediate feedback on a numeric input.

Source: Carbon Design System. An immediate feedback on a text input.

Another example that is more complex from my experience can be seen below. The original backend logic was to let the system skip some data, if — for any reason — the data consumption faced some errors. This obviously led to more manual work on the user side, where they need to compare data between the system and the actual bank transaction details by end of the week and month (refer to the red lines and boxes). Let alone during the peak season when the data could grow huge to hundreds of thousands of records, this is without a doubt, a case where a designer is expected to be meticulous. After this issue was raised and discussed with the developers, the discussion and solution were astonishingly quick and simple. By adding a retry mechanism, to let the micro-service consumes once more from the message queue, we were saving 15 work hours for every staff in a month.

Source: Self-created flow. How a simple logic solves huge pain points.

Yes, it is easier said than done. Frontend and backend validation do need more time to plan and implement, but at the very least, the product team could do two things: to prevent the obviously unwanted scenario to happen based on the possible edge cases, and, communicate the result of each user action.

## Designing all of the thinkable flows

From my experience, there are two aspects in SaaS (or essentially any product, but often seen more in SaaS) products that are double-edged swords: system flexibility and user collaboration. These two can lead to dependencies and complexity, which is something the product team has to pay attention to. Let’s take Google Meets for an example, assuming by 2022 most people have used this video-call platform. Imagine you are the product team and there was no single similar product in the market. The main requirement might be very basic: any account can open a meeting “room” and share it. Additionally, this meeting “room” can be shared with anyone or limited to a specific account. That might be all. These two requirements sound pretty basic, and the stakeholder might not see a good moment for the product people to sit together and brainstorm as many use cases and edge-cases as possible.

*   When a user sets a meeting for 3 other participants — namely A, B, and C accounts — can the organizer add more participants after the meeting link is shared?
*   What is the maximum number of participants in a meeting?
*   Can the organizer remove A or B or C? Can A remove B?
*   Is it possible to grant A permission to add/remove but not for B and C?
*   Can B reject A’s or the organizer’s request to be kicked?
*   Can A invite more accounts and if yes, should the organizer be informed?
*   What if after A sends out invitations to more participants A got removed, how to treat A’s invitees?
*   For the sake of privacy, can A/B/C remove themselves and block the meeting organizer’s account for future invitations?

The list goes on and on… And mind that all of these cases are only under 1 basic requirement, or should I say 1 user story. We haven’t covered after the meeting starts, the available functions during the meeting, and after it ends. Ideally, the product team needs to cater all of these scenarios into the feature list and inform the possible impacts before an action is done.

The second aspect mentioned above can lead to complexity: user collaboration. This happens quite a lot within one or across departments. Giving an example in banking, changing sensitive information (e.g. national ID) or wire-transferring a big amount of money abroad by a clerk needs their supervisor’s approval (within a department). The questions should be made are:

*   To what extent can the supervisor see the information keyed in by the clerk?
*   Can a senior clerk have permission to both key in data and approve? If not, in the case of the bank doesn’t have a supervisor, is it okay to let the clerk keep signing out and back to the system with two different accounts only for approval?
*   Can the supervisor change the information before approving or can they only reject it?
*   Can the clerk edit the rejected request or should they repeat the editing process?
*   Does the system need to detect if a clerk keys in ID or any other info that cannot be duplicated with other account holders’ information?

To remind you again, all these questions are raised only for perhaps 1 approve and 1 reject button added on the UI. Lastly, an example for cross-department collaboration. Imagine being in a crypto-exchange platform, where KYC (Know Your Customer; personal ID verification process) is needed before allowing users to withdraw their money. This KYC sometimes can be done via contacting Customer Support (CS). However, it makes more sense to not allow the CS to do both KYC verification and approving withdrawals, this might create a conflict of interest or SOP loopholes to attract fraud to happen. I believe the company would rather have another team to focus on the withdrawals, and that perhaps is why most of this kind of call by the crypto-holders usually ends up with the CS informing the user that KYC is successfully done and they should wait for a little while for the transaction to be approved. Some of the questions should be considered:

*   Since the cryptocurrency rate fluctuates, I assume the cashout attempt to fiat would be rejected as long as the KYC is not done. Is it correct?
*   How should the CS notify the withdrawal team? Do we need a notification system or let them use their internal communication channel?
*   What if multiple users are calling and CS have verified the KYC, would the system compile a list for the withdrawal team?

Feedback, feedback, feedback — good feedback does not only consist of a message but culturally intuitive visuals. Don Norman gave a great example of what blinking car lights can mean differently in a different place. Imagine two cars are from different directions and about to cross the narrow bridge fitting one car. The first driver who blinks the light, in some cultures, would go first on the bridge. While another culture will regard it as a sign of letting the other go first.

Following Don Norman’s theory of giving feedback with clear messages and at the right time, here are some good examples done well by Google Meets.

A black screen shows a word “Joining” after a user starts a meeting in Google Meet.

A black screen shows the word “Loading” with the spinning wheel, a second after seeing the word “Joining”.

Source: Google Meets. Constantly keeps the users aware of the current state.

## Designing the restrictions

Yes, feedback is great to inform failures or successful actions. But what is better than showing error messages? To prevent it from even happening in the first place. Jakob Nielsen summarized it well in his [heuristic evaluation](https://www.nngroup.com/articles/ten-usability-heuristics/), principle number 5: “Error Prevention”. In Saas products, form is commonly seen, I believe the concept of auto-correct, auto-complete, and suggested input are not foreign anymore and would be good uses for filtering or submitting data.

Source: AntD framework. Auto-complete component.

The book also discussed how people can naturally guess how to slide AA batteries in without knowing which are the positive and negative ends, by the visible/physical constraint. Don Norman pointed physical constraint restricts most possible actions through a design that guides users to take the correct one. In Saas, data query limitation is common as the table is too complex or the record is too big, filtering too long will lead to high loading or even errors. Rather than letting the user select and feedback error, the physical constraint can be applied by disabling the dates.

Source: Self-tweaked component. To prevent users from selecting today or any previous dates.

The second constraint is called logical, this is useful when the user can mentally eliminate the options and narrow them into one. I used to receive some requirements of different ways of logging into a back office for business use usually offering to login with AD (Active Directory) such as Google, and Yahoo, but manually inputting email and password is also available for the unsupported ADs (e.g. Hotmail).

Source: Todoist login page. Giving options in one glance for users to quickly pick the preferred method.

Source: Salesforce. Different view options for different use-case and/or different user groups.

Another type is called interlocks which require some sequential actions. For example, in order to select which credit card for the check-out, the user needs to first select the payment method. If they select by wire transfer, credit card selection is not necessary. Another example is to fill in addresses, starting from the dropdown of country, state, and city. This is a great help to prevent memory lapse when the design is only an input box, the user might forget to fill in the state or city. On the contrary, it has to be noted that this creates dependency, and when a user would like to change input, they might need to change many dropdowns.

Source: Essential Studio for Javascript. An efficient way to let users choose a parent.

An expanded dropdown that shows limited option based on another selected dropdown.

Source: Essential Studio for Javascript. Dependent dropdown list in different states. Good to let the users know ahead how many selections are needed to complete their tasks.

Source: Jira. Disabled input is more recommended than showing “No options” as shown here.

The last constraint is called lock-in, which is used to keep users on track to their initial goal. Sometimes a user is required to leave a half-filled form, to refer to some information before continue filling it out. The initial goal is still to finish the form. Meaning, if the system doesn’t provide an auto-save function, user progress is taking a backward step.

Despite its benefits, constraints can be confusing and have to be designed carefully. Especially when the action is expected like being able to switch pages quickly in the middle of form-filling, it is important to let users know why the restriction exists or provide options. On some rare occasions, restrictions are available in a very specific situation. Norman puts it nicely as “layers of Swiss cheese”, and there is some situation when all the holes of different cheese layers are all aligned, though the chance is low. In this case, an alert is necessary to remind the users.

Source: Confluence. The main use-case for a document writer is to gather information from different sources, which means switching pages is necessary. The auto-save function will play a good role.

The term “design” can be translated or connected to beauty, visuals, and art. However, as you might have noticed in this article, most of the design work especially for SaaS products is to understand the business value, clarify the cross-department collaboration or off-screen works, and how to utilize technology to improve the usability of the product. It is not a surprise even after all of these examples, this article has not covered a lot of use cases. However, I do hope this could become a good practice bringing the theory closer to implementation, mainly in Saas products.

## Related
[Add wiki-links manually or run update_wikilinks.py]