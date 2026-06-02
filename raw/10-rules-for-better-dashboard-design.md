Title: Article from uxplanet.org

URL Source: https://smry.ai/https:/uxplanet.org/10-rules-for-better-dashboard-design-ef68189d734c

Markdown Content:
## Practical guide

## One view to rule them all

Dashboard design is a frequent request these days. Businesses dream about a simple view that presents all information, shows trends and risky areas, updates users on what happened — a view that will guide them into a bright financial future.

For me, a dashboard — is an at a glance preview of the most crucial information for the user at the moment he is looking at it, and an easy way to navigate directly to various areas of the application that require users attention. The term “dashboard” is a metaphor for a car dashboard, sometimes also called the cockpit area, usually near the front of an aircraft or spacecraft, from which a pilot controls the aircraft.

## Get Taras Bakusevych’s stories in your inbox

Join Medium for free to get updates from this writer.

Working on enterprise projects for years, I have designed countless dashboards. And every new one is the next challenge for me. A good dashboard can be a daunting thing to design. Based on my experience, I put together a list of useful suggestions to help you in the future. Whether you just starting, or are seasoned designer, I’m sure you will find something interesting here.

## 1.Define the purpose of the dashboard.

Like any other view in your product, the dashboard has a specific purpose that it’s undertaken to serve. Getting this wrong renders your further efforts meaningless. There are multiple popular ways to categorize dashboards based on their purpose(Analytical, Strategic, Operational, Tactical etc). 

 To keep things simple I will divide them into 2 more general forms:

### Operational dashboard

Operational dashboards aim to impart critical information quickly to users as they are engaged in time-sensitive tasks. The main goals of the operational dashboard are to present data deviations to the user quickly and clearly, show current resources, and display their status. It’s a digital control room designed to help users be quick, proactive, and efficient.

Operational dashboard key qualities

### Analytical dashboard

In contrast to Operational dashboards, Analytical dashboards provide the user with at-a-glance information used for analysis and decision making. They are less time-sensitive and not focused on immediate action. A primary goal of this kind of dashboard is to help users make the best sense of the data, analyze trends and drive decision making.

Analytical dashboard key qualities

The type of dashboard you need should be determined by the user roles and needs you to seek to satisfy. Your product may have multiple roles that should each get a unique dashboard. Lower tier managers may require operational dashboards, while higher management may have a greater need for an analytical dashboard. Often designers mix those, providing the user that suppose to react fast and take action, with a ton of analytics and vise versa.

## 2. Chose the right representation for the data.

When we talk dashboards, we talk charts). Data representation is a complex task, especially since you will want to display multiple types of information in a dashboard, be it static or dynamic changes over time. This can be quite challenging. Choosing the wrong chart type, or defaulting to the most common type of data visualization could confuse users or lead to data misinterpretation. Before you start, take a look into internal documents and reports to get some inspiration. If you are starting from scratch here are some visualization suggestions that are based on what users need to see:

Graphs types that will help you see a relationship in data

Scatter charts are primarily used for correlation and distribution analysis. Bubble chart helps introduce the third dimension into the chart. 

 A network diagram is handy when even the most minor connection between data points are very important.

Graphs types that will help you compare values

Using visualization to compare one or many values sets is so much easier than looking at numbers in the grid. Column and line charts are probably the most used. Some recommendations: 

 - When one of your dimensions is a time it should always be an axis X, as time in charts flows from left to right 

 - When using a horizontal or vertical bar chart, try to sort columns by biggest value rather than not randomly sorting them.

 - With the line graph, charts shouldn’t show more than 5 values and with bar charts, it’s not recommendable to show more than 7 values.

Graphs types that will help you see a composition

Pie and Donut charts have a bad reputation for data visualization. These charts are among the most frequently used, and they are also the most frequently misused charts. They are quite difficult to read when there are too many components or include very similar values. It is hard for humans to differentiate values when it comes to angles and areas.

Graphs types that will help you see a distribution

Distribution charts help you to illustrate outliers, the normal tendency, and the range of information in your values.

Charts types to avoid

But certain chart types should be entirely avoided. Gauges were a big trend in dashboards in the past, but trying to replicate physical objects digitally is a bad idea. 3D charts and overstyled charts have lower readability, distract the viewer from data, and even more difficult to develop, so there is little reason to use them.

When to use various graph types

To help you choose the right representation type for the chart, ask yourself these questions:

 - How many variables do you want to show in a single chart? 

 - Will you display values over a period of time, or among items or groups?

 - How many data points are needed to display for each variable?

## 3. Follow clear and consistent naming conventions and consistent date formatting, and truncate large values.

As the main goal of the dashboard is to get the message across at a glance, every little thing counts. The biggest benefit of using a clear framework is data consistency. If your data is named the same way in each tool, it will be easier for you to use those tools. One framework. No questions.

## 4. Define the layout and flow. Prioritize.

Grids can help you to achieve effective alignment and consistency with little effort and create a basic structure or a skeleton for your design. They consist of “invisible” lines upon which your design elements can be placed. Doing so ties them together in an overall “system” and supports your composition rationally. That’s is crucial for dashboard design as you will need to organize a ton of information in a seamless way.

Grid and modules

When making decisions on what information should go were, keep this in mind:

 - The top left corner of the screen will naturally get more attention so try to position key info from left to right. This is based on the way we read information, so it may vary depending on the region of the users for which you are designing.

 When readers finish with the first row, they will move down to the next one.

 - If there are dependencies that will affect decisions making on one group of information from based on info from another, create a layout in a way that users do not need to go back and forth — create a continuous flow for easy scanning across the dashboard.

## 5. Use building blocks with consistent structure.

After we defined the grid, we can start work with multiple “widgets” that will hold the info, charts, and controls. Cards are easy to arrange. The most important thing about cards is that they are almost infinitely manipulatable. They are a good choice for responsive design since cards act as content containers that easily scale up or down.

An important characteristic of cards is the consistent layout of controls and data inside. Put the name in the top left corner, align view controls or actions to in the top right corner of the card, and leave the rest for the content. When all have a consistent structure, it’s easier for the users to work with the interface — they find everything where they expect it.

Using the suggested above layout has additional benefits of flexibility when it comes to responsive design or user customization. While the card gets larger or smaller all main components remain anchored to specific locations. This is also beneficial for developers, and the overall scalability of your designs in the future.

## 6. Double your margins

White space, also known as negative space, is the area between elements in a design composition. Readers aren’t usually aware of the importance of the negative space, but designers pay a lot of attention to it. If the white space is not balanced, a copy will be hard to read. That’s why negative space matters as much as any other typography element.

12px vs 24px margin visual difference

## 7. Don’t hide information or rely on interactions too much.

As one of the primary goals of the dashboard is to surface information at a glance, relying on scrolling or many interactions dilutes the whole purpose.

Empire state dashboard

Designing long scrollable dashboards is one of the most frequent mistakes designers make. They try to display more information in a clear way, positioning it one under another in order to avoid overwhelming the user. As a result, only the information visible above the screen fold is likely to be discovered by users. Everything below gets little attention from users. So what’s the point? 

 The solution is prioritization. After doing more research and interviews, you should be able to identify core information. You should work only with space above the fold to display it. Don’t tell the full story — summarize instead, and surface only key info. You can use additional interactions as a way to fit more content, and not overwhelm the user with data.

Don’t rely on too many interactions to surface information

Interactions help surface secondary information. Fully relying on them as the main way to work with the dashboard is a big mistake. In the example above we see how a user will have to painfully switch between multiple tabs to get the full picture. This hides information from all other tabs from user, just like content below the fold.

Data overloaded dashboard example

Trying to truly make your dashboard informative may lead to extreme cases. We should always remember that humans are bad at keeping track of multiple things at once. Don’t demand too much from your users, and don’t overwhelm them with data. Use a maximum of 5–7 different widgets to create a view. Otherwise, it will be hard for a user to focus and get a clear overview.

## 8. Personalization rather than customization.

Users expect that the content they see will be relevant to their individual needs. Personalization and customization are techniques that can help you ensure that users see what matters to them.

 Personalization is done by the system itself. The system should be set to identify users and deliver to them the content, experience, or functionality that matches their role. Customization is done by the user. A system may enable users to customize or make changes to the experience to meet their specific needs by configuring the layout, content, or system functionality.

Customizable dashboard

Giving users more power to customize the dashboard is a good initiative, as long the view is already personalized. Designing more ways to customize is often an excuse to avoid a tedious process of truly finding out what each user role truly needs to see. In the end, the user is left on his own, to build a view for himself.

## 9. When integrating data tables or lists, make sure they are interactive and data is aligned correctly.

A data table is a great solution when you need to show a lot of information for a large number of items. For example, a list of clients with their ID, status, contacts, last activity, etc., would be best displayed as a data table. There are many other benefits — it’s a great use of space, offers easy scalability, easier development, and users are typically comfortable working with grids as many people are already comfortable working with Microsoft Excel. It’s an easy way to find and change something. You can find out more about the data tables in this article.

## [Data Tables Design](https://medium.com/@taras.bakusevych/data-tables-design-3c705b106a64?source=post_page-----ef68189d734c---------------------------------------)

### [Basics medium.com](https://medium.com/@taras.bakusevych/data-tables-design-3c705b106a64?source=post_page-----ef68189d734c---------------------------------------)
## 10. Design the dashboard last.

Since the dashboard is one of the most visually exciting views, it’s often one of the first things to be designed. I would recommend the opposite. A dashboard is a summary view of everything else and displays key info from various parts of the application. It’s just more practical to design it at the end. Otherwise, you will need to constantly go back and update your dashboard designs while you are working on all the other pages. Furthermore, once a majority of the views are designed, you will have a ton of components to work with when putting together a dashboard.

Hope this was useful for you. Thanks for reading through.
