Title: Dashboard Types

URL Source: https://dashboarddesignpatterns.github.io/types.html

Markdown Content:
Our analysis revealed several _dashboard types_, with shared characteristics, similar use of [design patterns](https://dashboarddesignpatterns.github.io/patterns.html), and similar goals. These demonstrate common ways of putting [design patterns](https://dashboarddesignpatterns.github.io/patterns.html) into practice. These dashboard types be used in design exploration and can inform discussion about the ‘best’ dashboard design for a given context.

We see a distinction between **curated dashboards** and **data collection dashboards**:

*   **Curated dashboards**: 
    *   Highly selective of data and visual representations;
    *   Have a specific goal, e.g., to inform viewers about something in particular;
    *   Could be considered as _author-driven storytelling_ [Segel and Heer]

*   **Data collection dashboards**: 
    *   Aim to transmit large volumes of information;
    *   Allow viewers to seek the information most relevant to _their_ needs.
    *   Could be considered as _reader-driven storytelling_ [Segel and Heer]

* * *

## 2. Curated Dashboards

## 2.1 Static Dashboards

Common design patterns:

By static dashboard, we refer to the traditional notion of a dashboard as a _non-interactive_ and _flat_ structured display of information. These are less common now than one might imagine, which we attribute to the fact that modern dashboards are digital and it is easy to support interaction and drill-down tasks through more complex structures. Another reason might be that the range of display sizes on desktop computers, tablets, and mobiles encourages adaptive solutions (e.g., use of **overflow** or **paginated** structures).

### Static Dashboard Example

![Image 1](https://dashboarddesignpatterns.github.io/docs/assets/dashboards/StaticDashboard.png)

Example of a **Static Dashboard**.

* * *

## 2.2 Magazine Dashboards

Common design patterns:

Many dashboards relating to Covid-19, climate change, politics, etc, are typically created by news agencies and similar media outlets. These dashboards are found as integral part of journalistic articles and resemble visualizations of the _magazine_ genre. The text goes beyond basic meta information to provide additional commentary and storytelling about the data. These dashboards are often broken into several pages and have an **overflow** page structure with **linear layout**, with visualizations positioned at appropriate points in the text to tell a story about what the data shows.

As an example, The Economist Covid-19 tracker (shown below) provides viewers with a snapshot of Covid-19 cases and deaths across Europe, with tables, timeseries, trend lines and spike maps interleaved with narrative text. In addition to regular visualization updates, written content is also frequently updated as the ‘story’ changes, e.g., responding to emerging trends, the effects of vaccination, etc. These dashboards naturally require more effort to design and maintain; whilst visualizations may update automatically as the data changes, editorial oversight is necessary to ensure the story remains consistent with the changing data and its visual representation.

### Magazine Dashboard Example

![Image 2](https://dashboarddesignpatterns.github.io/docs/assets/dashboards/dashboard-journal.png)

Example of a **Magazine Dashboard**; note this appears to viewers as one continuous page.

* * *

## 2.3 Infographic Dashboards

Common design patterns:

Some dashboards have similar designs to infographics, including decorative graphical elements and other non-data ink shown alongside data representations. Similar to magazine dashboards, they use non-data media to annotate and embellish data. For example, the image below shows an infographic style dashboard that uses text, annotations and other embellishments to enhance data presentation and, in turn, help the data to convey a story.

Infographic dashboards are often used to represent static datasets; e.g., presenting snapshots of key data on a monthly or yearly basis. Often these infographics exceeded the vertical screen-space and could be explored through scrolling). The artistic content of infographic dashboards may require additional design time and chosen annotations and embellishments will be tailored to particular data points, so are less suited for dynamic dashboard use where data changes often. These dashboards may thus have a different intended use, with an audience expected to discover them over a longer period of time, rather than checking in frequently for updates.

### Infographic Dashboard Example

![Image 3](https://dashboarddesignpatterns.github.io/docs/assets/dashboards/DB117.jpg)

Example of an **Infographic Dashboard**.

* * *

## 2.4 Embedded Mini Dashboards

Common design patterns:

Dashboards can be embedded into other applications such as news websites. These concise _miniature_ dashboards only occupy a small area on screen and usually come with a range of interactive features for navigation, or to parameterize the content. The image below shows two pages from a mini Covid-19 dashboard embedded into a news website; like similar mini dashboards, it uses _navigation_ interactions to allow movement between pages and is _linked_ to a more in-depth narrative dashboard that invites further exploration beyond the initial data at-a-glance.

### Embedded Mini Dashboard Example

![Image 4](https://dashboarddesignpatterns.github.io/docs/assets/dashboards/MiniDashboard.png)

Example of a **Mini Dashboard**.

* * *

## 3. Data Collection Dashboards

## 3.1 Analytic Dashboards

Common design patterns:

This dashboard type is what Stephen Few would call a _Faceted Analytic Display_. We see strong parallels to the concept of _Multiple Coordinates Views_. This type generally uses complete **visualizations** (rather than simpler **signature charts** and **trend arrows**). Many of the dashboard elements are fully interactive, providing for pan+zoom, focus+context, tooltips, brushing+linking and other **exploration** and **navigation** strategies. These dashboards can also provide **parameterization**, and use **tabs** or **linking** to switch between _multiple pages_ of the dashboard. Importantly, these dashboards generally do not use _overflow_ pagination, since scrolling makes it more difficult to compare visualizations.

### Analytic Dashboard Example

![Image 5](https://dashboarddesignpatterns.github.io/docs/assets/dashboards/AnalyticDashboard.png)

Example of an **Analytic Dashboard**.

* * *

## 3.2 Repository Dashboards

Common design patterns:

Many dashboards list a multitude of charts on a single website, with **overflow** page structures that make proper analytics difficult, i.e., making it more challenging to compare views. Their charts often lack textual or other narrative explanations, except for meta data information (which is often extensive). Charts may provide some interaction and usually provide links to _explore_, _filter_, and eventually _download_ the raw data. Data and visualizations are updated, while choosing very common **visualizations** and **numbers** to visualize data. Extensive **meta information** is often provided for transparency and to support reuse. The images below show two examples of repository dashboard.

### Repository Dashboard Examples

![Image 6](https://dashboarddesignpatterns.github.io/docs/assets/dashboards/dashboards-chartwebsite.png)

Two examples of a **Repository Dashboard**, which act like landing pages for large collections of data.
