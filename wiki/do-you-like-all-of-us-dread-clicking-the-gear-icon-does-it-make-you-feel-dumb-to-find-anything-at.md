# Do you, like all of us, dread clicking the gear icon? Does it make you feel dumb to find anything at all in settings? If yes, then who is to blame here? It is we, the designers!

Do you, like all of us, dread clicking the gear icon? Does it make you feel dumb to find anything at all in settings? If yes, then who is to blame here? It is we, the designers!

For far too long settings have been reduced as an afterthought when designing products. A google search on the subject barely returns any useful content. To shake this up and make all of our life easier, I in this case study have documented my process of designing settings for a B2B product.

Sneakpeak of the redesigned settings

## Project Background

Graphy has acquired Spayee the market leader in India in CBC courses. Since the merger, the design team has been tasked with redesigning the Spayee product. As a part of this effort, settings are to be redesigned.

Being a feature-rich B2B product the current settings over time became too complex to achieve anything at all. In fact, it came to a point where even for simple config changes users were dialing up the support team. 🤬

With this redesign, we wanted to enable the users to achieve desired changes within minutes! 😄

**Project brief:** Redesigning the settings section to make it user-friendly with a reliable and scalable framework.

**Design timeline:** ~1 week

**Team:**Sanyam Jain (Designer), Vishant Batta (Product Manager), and Abhishek Damodara (Design Manager)

## Defining key pain points

Most of the problems contributing to an overwhelming settings experience can be categorized into 4 groups:

1.   Lack of **discovery** of all the configs that existed in the product.
2.   Lack of easy **navigation** to a specific config user might be looking for.
3.   Lack of **understanding** of what a certain config means and the implications changing it can have.
4.   Lack of scalable **framework** to accommodate ever-expanding features with their corresponding configurations.

The current design of the settings page

### Setting out to solve 😉

## I. Adding buckets…

Buckets are adding a level of obvious filtering for the user. It allows easy navigation to the relevant settings. Another advantage of bucketing is adding icons and helper text for additional context to the user. The current Spayee product settings is loosely bucketed into 6 categories: _Domain, Payments, Security, Email, Custom Fields, and Miscellaneous._

We #1, combed through all configs and

1.   divided _payment_ into two buckets, _payment integration_&_invoice_. The payment integration bucket contains gateway setup and country-specific pricing. The invoice contains creating invoice templates and management of invoices.
2.   removed _miscellaneous_ to create _user experience and permission_ for all experience level changes and _live class_ to handle the management of zoom and other live class solutions.

#2, categorized buckets further into two groups:

1.   **Website management**: Containing domains, security, payments integration, Email communication, and invoices
2.   **User experience**: User experience and permission, live class

and 

 finally, #3 added icons and relevant copy to each bucket

Dividing settings into buckets from the user's pov

Adding buckets contributed to solving all pain points. Bingo!! 🎰

Tracking how adding buckets helped solve the pain points (Green means solved)

## II. Coming up with a layout…

Laying all the configs in a neat and orderly manner was imperative for the best user experience. The current design was a two-column card-based layout. There were some obvious fixes that could have been done to improve the experience but we took this opportunity to think from the ground up.

Current layout

Key expectations from the upcoming layout:

*   **Crisp overview** for the user so they can easily scan through sections.
*   Accounting for labels, helper text, and its control/input.
*   Scalable enough to easily add config in the future without input from the design team.
*   Flexible to not break in case a unique kind of config control is added.
*   Clean with plenty of whitespaces to **deal with information overload.**

Now, let's start with the explorations 🏃🏻

I researched how other products go about the layout. Inspiration was taken from consumers as well as complex SaaS products. I did not want to confine my research to like-for-like products as that often results in a lack of innovation.

Exploration

### Ideating layouts

I explored multiple layouts to find the one that fits best and to help with the decision-making process I defined four parameters:

1.   _Ease to scan_ through the layout
2.   _Levels of hierarchy_ that can be cleanly created
3.   _Real estate_ needed to place layout efficiently (essential if it needs to fit in a side panel)
4.   _Flexible_ to accomadate complex configs

To make this a bit fun, I will be **scoring the layout on a scale of 1-5** on each of the above parameters. Below are the explorations for layout –

### 🔍 Single column layout:

*   Scores low on ease of scan, the reason it being a single column layout. This could have been solved with high contrast and hierarchy but inherently a single column layout scores low.
*   Adding hierarchy can get messy as all are in a single column. Especially in case, we need multiple levels of hierarchy.

*   Scores high on real estate required meaning it can be easily squeezed into limited space.
*   The lack of rigid structure enables flexibility to add all sorts of complex operations.

### 🔍 Single column card layout:

*   The card-based layout increases the ease of scan as it helps in guiding the user's focus.
*   Adding cards to the layout does not affect the adding hierarchy much.

*   The extra margins required for a card-based layout mean more real estate required. Hence, a lower score.
*   Scores are similar in the flexibility of adding complex configs.

### 🏆 Two column layout:

*   Inherently a two column layout is much easier to scan through. The left column is read-only with config labels while the right column is with config operations.
*   Hierarchy can be added using indentation and styles. The two column layout means added hierarchy is much more effective.

*   The real estate required score is low for obvious reasons of two columns needed.
*   Adding operation requires a bit more thought and effort compared to a single column. Hence, lower flexibility.

**Winner 🎉**

Two column layout was picked as the most suitable option with its high score on ease of scanning and hierarchy. The reason for prioritising the first two parameters is that they contribute most to solving the pain points.

Once the layout was final, all the essential components that exist in a settings page were added. Below is the manifestation of the selected layout with all the components placed –

Anatomy of the layout with all the components

Tracking how coming up with a layout helped solve the pain points.

## III. Defining interface and its interaction…

The current interface was a simple tab-based interface. Although simple to use there were the following **limitations with the current tab based pattern**:

*   Adding helper copy for additional context was not possible.
*   Limited scalability as the design will break if there are too many tabs.
*   The first tab is always pre-selected which creates an unnecessary hierarchy

Current interface for settings

To address all the above concerns and come up with a full-proof solution we explored different interfaces to navigate.

### 🔍 Exploration 1:

Choose a bucket from page → Bucket opens on a new page

Exploration #1: Choose settings from the page → Opens on a new page

**Pros:

 -** focused and clean navigation 

 - complete real estate to layout dense information and configuration

**Cons:

 -** friction to quickly switch between different buckets 

 - possible loss of context when switching user

> Pattern can be found in operation system settings. (think macOS and windows system setting)

### 🔍 Exploration 2:

Choose a bucket from the page → Selected bucket opens in a floating side panel

Exploration 2: Choose a bucket from the page → Selected bucket opens in a floating side panel

**Pros:

 -** reduced friction to switch as it allows users to switch buckets without changing of page 

 - focused on the selected bucket as everything else is blurred out

**Cons:

 -** constant transition to switch between buckets in the short intervals can be disturning 

 - lack of visibility of other buckets when any bucket is selected

### 🔍 Exploration 3

Choose a bucket from the page → Selected bucket opens in a fixed side panel

**Pros:**

 - clean layout on the first click of settings easing the decision making of the user 

 - always visible buckets meant easy switching

**Cons:

 -** intense transition on first bucket selection 

 - cannot preserve the last selected bucket state

Inspiration for this exploration was from the Crafts App ❤️

### 🏆 Exploration 4

_Choose buckets from the page → Selected bucket opens in the right panel_

Exploration 3: Choose buckets from the page → Bucket opens on the right panel

**Pros**

 - always visible buckets which means easy context switching 

 - optimised for first user experience 

 - common pattern for settings in complex products

**Cons 

 -** information-heavy**,** too much to look at first glance 

 - on smaller screen sizes the list of buckets panel will require a scroll

**Winner 🎉**

Out of the four explorations, the last two clearly stood out as the best. But we decided to go with the 4th exploration. The reason is the familiarity of this pattern with the user along with the other advantages listed above.

> At the time we all favoured the 4th exploration but in hindsight while compiling this case study I feel even the 3rd one should have worked. The fact that that there wasn’t a strong enough reason to go ahead with it tilted us to a familiar pattern.

Tracking how defining interface and its interaction helped solve the pain points

Sigh!! this was all about architecting the interface for settings. 😮💨

## IV. Concluding thoughts

The process of intensive exploration helped build confidence around the end solution. It might have taken slightly more time but now that the architecture is set, we can go all out designing individual settings. Also, now that we have a pattern for two-panel navigation it can be easily applied to other parts of the product.

Personally, upon being given the task to redesign settings I felt overwhelmed by how I’m going to find the motivation to execute a not-so-exciting project. But as it turned out I enjoyed and proactively worked on it. It remains one of the projects which I and my team are super proud about!

## Related
[Add wiki-links manually or run update_wikilinks.py]