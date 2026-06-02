Title: Article from medium.com

URL Source: https://smry.ai/https:/medium.com/vmwaredesign/5-steps-to-effective-dashboard-design-c1813455e159

Markdown Content:
An illustration showing a woman pointing at a dashboard with graphs

Data visualization has always been a key skill for designers. We visualize simple things like how much we’ve spent on coffee this week or how much closer we are to a weight goal this month. Simple visualizations like these can be inserted as charts for context in other screens, but when the data is more complex, the display often turns into a dashboard. But what exactly is (and maybe more importantly isn’t) a dashboard?

I’ve heard some interesting answers… everything from “any page with charts on it” to “a way for users to build their own UI”. Those are both a bit extreme, but there are some good definitions floating around the internet (as well as more than a few bad ones). My personal favorite comes from [Stephen Few](http://www.stephen-few.com/idd.php), who says,

> “A dashboard is a visual display of the most important information needed to achieve one or more objectives; consolidated and arranged on a single screen so the information can be monitored at a glance.”

Why that definition? Because, not only does it capture that a dashboard has a **visual display of data**, but also that that visual display has a **distinct purpose or value**. The most common mistake I see designers make when building dashboards is the desire to start with something that looks good and fills a space, and then try to layer functionality on top. Starting with a pretty dashboard on [Dribbble](https://dribbble.com/search/dashboards) and hoping you’ll get to an effective interface is a recipe for disaster (a pretty disaster, but a disaster nonetheless).

## Why are dashboards important?

We use dashboards to help users quickly assess state and determine what needs to be done in response. The usability of the dashboards can literally be the difference between a small dip in a service’s availability and a full-blown outage that impacts the business’ bottom line.

For the last four years, I’ve been the design lead for operations software at VMware, where I set the design direction for multiple products including [vRealize Operations Manager](https://www.vmware.com/products/vrealize-operations.html), [vRealize Log Insight](https://www.vmware.com/products/vrealize-log-insight.html), and [Wavefront by VMware](https://www.wavefront.com/). Each includes some sort of custom dashboard feature. The designers on my team create dashboards that help users overcome the complexities of large-scale and often disorganized data. These products are used by software developers and IT professionals to manage and operate some of the most important applications in the world, and for these users, the time it takes to analyze data isn’t just important — it’s critical.

## 5 steps to effective dashboard design

While I’m sure there are many differing methods, the following steps reflect how I typically approach a project that has identified a need for dashboards. I’ve found these steps helpful when I design dashboards at VMware, and I hope others find them useful as well.

## 1. Define the people & their purpose

As designers, we know that we don’t design software for ourselves but for our users. And just like any other part of an application, dashboards should be focused on meeting user needs. That means we first need to identify who the dashboard is for.

To use the source metaphor, a car’s dashboard is built around the things that the driver needs. If you were building for the passenger, things like [engine RPMs](https://www.autoblog.com/2018/07/18/a-brief-explanation-of-rpm-video/) may not matter much, but what station is on the radio becomes critical. It’s all about what’s important to that particular user. Secondly, we need to know what their purpose is in this context. Are they the driver trying to get the car from point A to point B, or are they the passenger trying to select just the right songs for a road trip? Every design decision is a choice, so understanding your primary target user’s goals will help you in making choices.

Photo courtesy of Createria via Unsplash

## 2. Choose the right type of dashboard

So far, I’ve been referring to dashboards generically, but in reality dashboards come in many shapes and sizes. From my experience, I’ve found it useful to classify them into three main types:

*   Monitoring Dashboards
*   Interactive Analytic Dashboards
*   Navigational Dashboards

### Monitoring Dashboards

Monitoring dashboards are the most traditional style of dashboard. They are likely what most people think of when first asked to define one, and again, conjure images of a car’s dashboard. That’s a good example of a monitoring dashboard because it shows information that should be constantly visible to the user and is available at a glance. It also assumes that potential actions prompted by the information are taken elsewhere. For example, if the displayed speed is above the limit, you may want to let up on the accelerator, and if it’s way over, then you may want to press the brake. A common example we see of this in VMware software is for dashboards that are displayed on a large shared monitor in an operations center. Many people may be expected to view the dashboard, but no one interacts directly with it. It informs actions that are performed elsewhere.

Wavefront by VMware — Dashboard of Single Stats

### Interactive Analytic Dashboards

Interactive analytic dashboards have become more common in recent years, where their purpose isn’t to immediately show a nugget of information but to give the user tools in the form of data visualizations, so they can expose the information they need. This is typically achieved by connecting charts together through common filters and selection.

vRealize Operations Manager — Troubleshoot a VM Analytics Dashboard

### Navigational Dashboards

Navigational dashboards act as a sort of “table of contents” in a hub-and-spoke navigational model, where a central page leads to detail pages. What makes this different is that each statistic represents a broader element. The value differentiates the items, which makes it clear to the user which to interact with to get more information.

Wavefront by VMware — Dashboard to Dashboard Navigation

These definitions aren’t fixed or siloed types of dashboards. There are often dashboards that expose multiple traits. A common pattern I see is to have a monitoring dashboard that’s shared on a monitor and across a team. The monitored items are navigational and allow team members to drill-down to a separate dashboard with more specific details about that item. In that case, it’s both a monitoring dashboard and a navigational dashboard.

## 3. Display the right data in the right way

### Data Granularity

Once you know the user, their purpose, and dashboard type, it is time to convert that information into one or more simple questions. This is where the user will find the true value of the dashboard. If the question is too broad, you may not be able to answer it, or you’ll need a lot of data to answer it with any sort of accuracy. On the other hand, if the question is too narrow, it’s unlikely to be able to address the user’s larger purpose. Finding the right questions to answer is the art of dashboard design. Like most design work, it really starts with research. Finding the right question may be as simple as polling a number of representative users, or it may take some deeper conversations and contextual inquiry. Only when you know the questions in your user’s head will you know if you actually have the data to answer it properly.

To better understand user goals, [we encourage designers to tell the user’s story](https://medium.com/vmwaredesign/multi-layered-design-stories-7a2204dec40f) and visualize how the story flows through the software. Part of a story may see the user needing to answer a question. If the product can help answer the question, a dashboard may be the best mechanism, but the product has to have the right data for the answer to be useful.

If you find that you do have the data, that’s great! If you don’t, then you need to see whether you can either get the data (sometimes by merging data you do have), or whether you can carefully alter the question to something that can be answered with the available data.

The classic pitfall at this stage is letting the data you do have dictate the content of the dashboard you’re creating. Just because an API exposes 20 unique metrics, doesn’t mean that you should show 20 charts. Advocate for the user, not the data!

### Time and Comparison

Data changes over time, which is why it’s interesting. The fact that it changes provides the first type of comparison, which is visualizing that change over time.

Assuming a time change is interesting, we need to consider the right display mechanism: How does it relate to time? Is the present state the only thing that matters? Then maybe a single-stat or gauge is the right way to show it. Do past trends matter? Then you may consider pairing that single-stat with a simple spark line to show trend. Is a spark line enough fidelity, or do you need to see exact values at exact times? If so, then a detailed line graph with clear axis labels may be the best.

Progression from Single Stat to Spark Line to Line Chart

But time’s not the only type of comparison. Sometimes it’s just as important to compare multiple sources to each other. If so, then the right answer may be as simple as two single-stats side-by-side. But what if it’s more than two sources? Is it important to compare the values to each other using a bar or column chart, or more important to compare the value to the whole using a pie chart. And what if comparing to other sources and comparing over time are both important? In that case, you might find yourself turning to a stacked area chart.

Progression from Bar Chart to Pie Chart to Stacked Area Chart

## 4. Organize logically and progressively

More often than not, you’re answering multiple questions using multiple displays, so how should they be laid out on the dashboard? Returning to the questions you identified, they can often form a hierarchy. Imagine you’re designing a dashboard for personal trainers to track their client’s progress. The first question might be to understand if the client has reached their monthly goal. If the answer is ‘no’, then the trainer would want to know whether this was a steady progression in the wrong direction or a ‘blip’ in the trend reflecting the client’s “cheat day”. By organizing your questions, you can logically group the widgets to best answer the questions.

When arranging charts, consider:

*   natural reading direction of your target users (L to R or R to L?)
*   display size (4K monitor or tiny iPhone 6se? If it’s both, be ready with an answer for responsiveness.)
*   time alignment (multiple charts that show the same time range are easier to correlate if they’re stacked vertically)

So now you have a dashboard filled with logically ordered charts and widgets that answer all the questions you foresee the user asking, but fitting that on a single screen is hard and scrolling defeats the _glanceability_ of a dashboard. What to do? Again, this is where the question structure helps. If you’ve identified the primary question, then start by identifying what’s required to answer it. **That** is your default dashboard display. Your front-end developers will also like that you’re not asking them to render as many charts initially.

For those secondary and beyond questions, you can disclose them progressively, either by collapsing them on the dashboard by default, or moving them out to their own separate navigable dashboard. If you use the secondary dashboard method, be sure to make the navigation clear and accessible. Developers will often dictate whether this is a choice, but be cognizant of the trade-offs for each:

*   Navigating seems easy, but maintaining context can often be hard.
*   Collapsing also seems easy, but overloading the page may stress both the user and the system rendering the dashboard.

In rare cases, you may find that the user for whom you’re advocating only has a single question, and you only have to display that answer. If so, this section isn’t really necessary, but I can count the number of instances where I’ve seen this on one hand.

## 5. Enhance with styling

You now have one or more dashboards filled with chart displays that can be interpreted by users to answer important questions. Some might call that adequate and be done, but as designers we strive to not only make it so users can interpret data, but so they can do it easily and even delightfully. The use of colors and fonts can extend a dashboard from being functional to being truly usable.

### Colors

Previously, the comparison was considered, and one of the most common things to compare across charts is the data source. It’s important that data on multiple charts (even different chart types) should represent the same sources in the same way, especially with regard to color.

Additionally, be mindful of how colors can be interpreted. For example, many users would interpret red charts as errors or green charts as normal and healthy. Red and green also present another consideration: accessibility. Red-green color blindness (deuteranopia and deuteranomaly) affects up to 7% of the male population, so it’s important to use simulation tools to validate that your charts are distinguishable.

Same charts from above but simulating deuteranopia… uh oh.

### Fonts

Choosing the right font for an interface is difficult enough on its own, but charts present their own specific challenges. Charts display text at significantly smaller sizes than most body text, so finding a readable font at small sizes is key. Additionally, fonts for charts are used for numeric values far more often than other parts of the interface, so carefully consider how numbers are rendered. For example, many fonts add a slash or dot to zeros to differentiate from the letter ‘O’, but at small sizes, they might start looking like the number ‘8’.

Data visualization is a key challenge for designers and the ability to effectively design dashboards is a valuable tool to have in your tool belt. As with any craft, it’s important not only to have the right tool, but to know how to use it effectively. While it takes special skill to make a beautiful chart or graph, it takes thought and planning to make a dashboard that solves user problems and does so with delight.

## We’re hiring!

The VMware Design team is looking for talented designers to help us continue transforming enterprise design. [Check out our open positions](http://vmware.design/careers.html)!
