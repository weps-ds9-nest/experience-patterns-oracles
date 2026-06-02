Title: Article from southshoreanalytics.medium.com

URL Source: https://smry.ai/https:/southshoreanalytics.medium.com/visualization-theory-the-secret-to-game-changing-dashboards-f27add19f1aa

Markdown Content:
Photo by 1981 Digital on Unsplash

If you have been following along with our [recent content](https://southshoreanalytics.medium.com/mastering-your-data-stack-part-3-how-to-transform-your-data-with-dbt-a08ab37bf4eb), you will know we’ve been putting together a [Series](https://medium.com/@southshoreanalytics/mastering-your-data-part-1-selecting-the-right-pieces-for-your-data-stack-db532b48f45c) outlining our tips and tricks for building a world class data stack. While writing the entry on Data Visualization, we found ourselves expounding on the theory behind visualization itself. So, we decided to publish a separate post specifically diving into Information Visualization Theory! In this article, we will walk through some of the foundational principles around Data Visualization and introduce a few concepts we think will be very helpful as you progress through your data journey.

**Defining Your Objectives**

As we have emphasized in the past, planning and designing each aspect of your data stack is as critical as the actual implementations themselves. This is especially true when it comes to constructing dashboards, as there is no direct formula or singularly correct way to make any analytical visualization. Instead, we must stick to a repeatable thought pattern and iterative design philosophy to achieve successful and effective statistical graphics based our data subsets and analytical goals.

The first step is to craft a set of clearly defined goals or questions that you would like to be revealed from your data. For example, you might ask things like:

*   How does my company’s daily revenue change over the course of the year?
*   How many newly acquired customers come back in the subsequent three months?
*   How does seasonality affect our product mix?

Whatever these questions might be, it is crucial to outline them upfront. The last thing you want to do is spend your time aimlessly constructing visualizations only to later realize no one finds them particularly useful.

**Data Types & Encoding Channels**

To create effective visualizations, it’s helpful to understand two key concepts: **data types** and **encoding channels**. Data types describe the content of your data fields — such as numerical (ordered) or qualitative (categorical). Encoding channels, on the other hand, determine how we visually represent these data points — like length, position, or color hue. The chart below ranks these channels by effectiveness, separating those best suited for ordered versus categorical data.

Visualizations come to life by matching data types to appropriate encoding channels. For example, length is commonly used in bar charts, position in scatter plots, and area in dot maps. When working with quantitative data like revenue, using a categorical channel like color hue would be ineffective. Instead, channels with higher expressiveness, such as position or length, should be prioritized for key metrics, while less critical fields can use more subtle channels.

For example, to analyze daily revenue (a continuous quantitative variable) over time (an ordinal quantitative variable), a line graph or scatter plot would be ideal. Positioning these variables across two axes provides the clearest visual comparison — highlighting revenue changes over time.

> **_An interesting design note on bar graphs_**_— be cautious to avoid running into the_ moire effect _, an optical illusion in which the bars appear to move and distort when a large number of thin lines or bars are in close proximity. You might be familiar with this concept from looking at picket fences, barcodes, or even art that reveals hidden images when superimposing two repetitive patterns of lines._

**Principles of Data Visualization**

When designing graphics, it’s essential to follow some key visualization principles to avoid distorting or misrepresenting your data. A foundational voice in this field is Edward Tufte, whose book _The Visual Display of Quantitative Information_ outlines core principles for effective design. Tufte emphasizes that among other things, visualizations should:

*   Show the Data
*   Induce the viewer to think about the substance rather than any aspect of its design
*   Avoid distorting what the data has to say
*   Make large data sets coherent
*   Reveal the data at several levels of detail — from a broad overview to the fine structure
*   Be closely integrated with the statistical and verbal descriptions of a data set

Some of the above principles, like ensuring the completeness of your data, are relatively straightforward. Others, like drawing focus to the substance of a visualization or providing multiple levels of detail, are more nuanced and case-specific. Ultimately, great visualizations originate from and stay true to the data itself — delivering a clear narrative without prioritizing design over substance.

**Conclusions**

No matter the size or complexity of your data stack, every visualization should start with a clear objective and a thoughtful plan. By applying these foundational principles and techniques, you can ensure that your final, user-facing data products are both effective and insightful!

## About Us

[South Shore Analytics (SSA)](http://southshore.llc/) is an Analytics Consulting Firm, co-founded by James Burke and Nick Lisauskas, both highly skilled professionals with more than a decade of invaluable experience in the field of Analytics. Their shared passion for data-driven insights and business optimization led them to establish SSA, aiming to provide top-notch services to various businesses, irrespective of their size or stage of development.
