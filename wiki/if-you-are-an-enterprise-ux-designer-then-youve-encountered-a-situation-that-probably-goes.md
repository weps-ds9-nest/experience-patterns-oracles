# If you are an Enterprise UX designer, then you’ve encountered a situation that probably goes something like this.

If you are an Enterprise UX designer, then you’ve encountered a situation that probably goes something like this.

You have a few records/items/products that need to be changed/updated/moved at the same time in the same manner. This is most commonly found on lists or data tables with rows or lists of different sorts. Few elements are more commonly used than a good old data table. They are also one of the most fragile components in terms of implementing good UX.

The combination of a data table with checkboxes on each row is a union as old as enterprise design itself. The combination allows our users to apply the same action to multiple items at the same time, removing the need for repetitive actions, which we all know, suck. This is especially true in enterprise design, as the user is usually an employee who did not buy nor have a say in the software they are using, but as Atishay Goyal points out in this [case study](https://uxdesign.cc/ux-design-enterprise-applications-e73887822873),

> “Even if they usability is poor, the number of clicks are 10x [sic] or the page needs to be refreshed 20 times to load a result, enterprise users will do it to complete their work”.

Our Job as Designers is to make that process as efficient and seamless as possible. A large part of this is removing the guesswork and experimentation needed to find the fastest way to accomplish a task.

**The Challange**

Recently my team decided to move from an older UI system to the new Salesforce Lightning Design System (SLDS). This being the case, we also had to build some custom data tables to handle some of the custom functionality that we had built previously that does not come standard with Salesforce. This meant thinking through all the small details that usually come built-in with a platform like Salesforce.

One of the items that came up was how to implement the checkboxes on a lazy Loading data table.

(a lazy loading table is one that loads a standard number of records when the page loads so that the interface looks full, and continues to load more as the user scrolls down. This removes the need for pagination, which can become obsolete on tables that have 1000+ records)

![Image 1: A Standard Lazy Loading Data-table (SLDS)](//:0)

_It is important to note that the points here will apply specifically to these types of tables, as the research may have played out differently with a paginated table._

There are technically 2 aspects to a table checkbox. The master checkbox, and the row checkbox.

The master checkbox lets the user immediately select all rows to take action on them. This is convenient for when there is a way to filter the table by a criterion of sorts, and you need to take action on all those that fit the criteria.

The row checkbox allows users can also check individual rows from the table to take action on. We found that users used this most commonly after applying one of the 2 criteria methods (text search and Data-query) and then wanted to take action on a few of those records that showed in the results but not all.

The first challenge is the Master Checkbox. With a lazy loading table especially, there is the automatic assumption that if there is a master checkbox, once selected, it selects everything in the table down to the bottom.

![Image 2: A basic master checkbox component (Salesforce Lightning Design System)](//:0)

This means that if the user applies some sort of criteria to the page, whether that is a text search or a table filter, once the table loads the appropriate results, the checkbox applies to everything on the page.

But what happens when the user applies the master checkbox and then adjusts the table? Do you maintain his selection from before the change, and any changes he makes after will affect that original number, or do you only apply it to the items still on the table?

The same issue presents itself when the user has selected a specific subset of records and then adjusts the table data. This also presents an additional challenge that it is possible for there to be no checkboxes visible from his previous selection, so there may be items that he is taking action on that he has no way of knowing, from this most current view, that they are checked at all. This is not the case when the master checkbox is applied, as this at least indicates that a selection was made before the adjustment, and that selection remains in some form.

An additional point is that since lazy loading by definition does not load all records, you do not have the ability to display an accurate number of rows selected should the user select the master checkbox. It will instead simply show the number currently loaded, with a “+”. This means that even if the user changes the criteria, and we choose to only keep items that fit the current criteria in our selection, the total number may not change, depending on how few records are loaded initially.

**So I decided to test some hypotheses to make the most informed decision.**

My theory was that there is a difference between using a criteria filter, and a search box (text filter).

The biggest challenge we faced was finding users who had no premonitions about how the page would operate so that we could get an opinion based primarily on basic user expectations and not just past software systems used.

We also found that we could not use the same test user twice, as once they used one of our solution options, they expected that the next time we assigned them a task, and now had new biased expectations.

We asked users about their history and experience with enterprise software, and if they had used data tables extensively before.

We then gave them a series of tasks, using the 2 checkbox methods, to see how they went about accomplishing it, and if the table behaved according to their expectations.

The results were mostly as we had expected.

**When using the master checkbox:**

Users who filtered using criteria (Eg: Field 1 = “TRUE”) and then changed the criteria, weather on the same field or any other, considered the results to be a new set of data and did not expect the selections from the previous state to carry over.

Although very uncommon in our observations, the same was not true with the search textbox.

After selecting the master checkbox, then searching for rows with specific text, they expected the original selection to remain throughout.

**When selecting individual rows:**

Users who selected specific rows, and then filtered used a criterion (Eg: Field 1 = “TRUE”), did not expect the selection to be maintained, but were also not frustrated when we tested the scenario where we did maintain the selection, but showed a “# of rows selected” indicator. They simply looked for a "clear selected rows" option.

This part of the test was considered inconclusive and we are still in the process of getting a consensus.

We had a similar result when they used the text search box at the top of the page.

They started going through names they know and checking them off, before typing in a new name, and checking that off as well, then expected to be able to take action on all the items they had checked off, despite the fact that by the time they reached the final row to check off, none of the other checked items where visible on the page.

We saw this result even though we removed the number of records selected indicator on the side.

Users expected this 100% of the time when we re-added the total number of records selected to the page.

**The conclusion**

We settled on this design, where we tracked the master checkbox so long as the user did not change the filter criteria. Searching in the Textbox did not affect the selection, even if the users unchecked an individual.

From a technical perspective, we did this by saving the table Criteria when the user selected the master checkbox and used this to apply the action to all that fit the criteria.

When the user unselected a record, while the master checkbox was selected, we were able to record just that row id and pass that into the parameters of the mass action, to not include that row/s.

When the user selected individual rows, with the help of the “# of rows selected” indicator, we were able to maintain those specific items checked regardless of how the user changed the table data. This decision is subject to change after some more quantitative research.

This was simply done by collecting the Row ID for each row that was checked, which we then used to take action on only those selected rows, regardless of any table changes the user made.

**The results**

We saw a significant increase in user adoption of this Mass Actions features that use the checkbox, with a clear increase in the number of records changed using this process, but a decrease in the number of attempts it took a single user to update all the records they wanted to be changed in a single session.

## Related
[Add wiki-links manually or run update_wikilinks.py]