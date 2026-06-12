# Designing a **time-zone selection** is hard. Not only are time zones difficult to scan and understand; they also change over time, with or without daylight saving at different times, and there is no universal way of organizing and displaying them.

Designing a **time-zone selection** is hard. Not only are time zones difficult to scan and understand; they also change over time, with or without daylight saving at different times, and there is no universal way of organizing and displaying them.

[![Image 1: A screenshot of lukasz.medium.com](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/time-zone-selection-ux/01-time-zones-complexity.jpg)](https://lukasz.medium.com/on-time-time-zones-and-software-6617a4c22d05)

[Time zones are hard](https://lukasz.medium.com/on-time-time-zones-and-software-6617a4c22d05), a wonderful article by Łukasz Tyrała with details about time zones and tips for better time-zone selection UX.

And then there are **dozens of time zones** and hundreds of mysterious abbreviations — UTC, GMT, DST, CET — which sometimes change, and sometimes not. Ironically, users often need most time when choosing the right time zone. How do we make it easier for them? Let’s figure it out. (You can find more details on that in the [usability chapters in the video library](https://smart-interface-design-patterns.com/).)

## 1. Use a Complete List of Time Zones [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#1-use-a-complete-list-of-time-zones)

In total, there are [352 time zones around the world](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), with 245 different abbreviations (as defined by the [Time Zone Database](https://www.iana.org/time-zones)). Of course **time zones evolve over time**; they get changed or deprecated, so it shouldn’t be surprising to discover that our legacy applications might be showing some time zones which are no longer relevant.

[![Image 2: A section of time zones around the world](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/time-zone-selection-ux/02-time-zones-global-map.jpg)](https://mcusercontent.com/16b832d9ad4b28edf261f34df/images/3853277e-f22f-a9bd-e6cc-b4b8fcbb6e01.jpeg)

A section of time zones around the world: [download the complete list](https://mcusercontent.com/16b832d9ad4b28edf261f34df/images/3853277e-f22f-a9bd-e6cc-b4b8fcbb6e01.jpeg).

Of all the different time zones, _Coordinated Universal Time_ (or UTC) is the one reliable, true compass for time definition. It never changes and serves as a **constant time of reference**, in which other time zones are relative. It’s also seen as a successor to the Greenwich Mean Time (GMT). Unsurprisingly, it will have to make its appearance in our time-zone selection UI.

## 2. Users Think in Their Local Time [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#2-users-think-in-their-local-time)

Because UTC is standardized, we should be able to rely on it and display just that. However, as it turns out, **users often don’t think about UTC** at all. [Nor do they understand time zones](https://www.nngroup.com/articles/time-zone-selectors/), or the difference between UTC and GMT, or when and where daylight saving times are. However, GMT in general is better understood than UTC.

[![Image 3: Time Zone Selectors UX study](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/time-zone-selection-ux/03-proportion-of-correct-offset-selections.jpg)](https://www.nngroup.com/articles/time-zone-selectors/)

[Time Zone Selectors UX study](https://www.nngroup.com/articles/time-zone-selectors/). All groups had more correct selections in GMT than UTC. But it was statistically significant only in UK.

Instead, users typically think about the **local time in their city**, or in their region. And when arranging a call or meeting, they need to look-up the time for a specific date in a specific location where their partner will be connecting from. In fact, the selection of a city is way more important than time zones.

## 3. Always Add Autocomplete For Location [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#3-always-add-autocomplete-for-location)

It’s not surprising that scrolling through the endless list of countries and time zones isn’t particularly exciting. So whenever possible, include autocomplete to allow users to **type their city or country** and locate the needed time zone faster.

[![Image 4: Always encourage users to start typing.](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/time-zone-selection-ux/04-time-zone-selection-zoom.png)](https://mcusercontent.com/16b832d9ad4b28edf261f34df/images/51e8fb86-ae6d-14ad-60e6-ef5c960df672.png)

Always encourage users to start typing. When placeholders matter: “Start typing” might work better than “Select” as users might scroll instead.

Most people will be searching for a specific city, but they can type larger areas — counties, states and localities — as well. This typically means that we need to **support cities and countries** as a minimum. And if a country has more than one time zone, we need to highlight distinct time zones for each country match.

## 4. Show Current Times in Locations [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#4-show-current-times-in-locations)

Sometimes selecting a time zone is only one part of the story though. What if a user needs to make a decision about the right timing as well? We can display the current time on location to help there.

[![Image 5: No UTC/GMT times are displayed on Calendly.](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/time-zone-selection-ux/05-time-zone-selection-grouping.png)](https://mcusercontent.com/16b832d9ad4b28edf261f34df/images/816fe5ca-f208-f0ae-dc18-c7b08fab58f7.png)

No UTC/GMT times are displayed on [Calendly](https://calendly.com/). Instead, they show the current time on location instead. Source: [NN Group](https://www.nngroup.com/articles/time-zone-selectors).

## 5. Detect and Suggest User’s Time Zone [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#5-detect-and-suggest-users-time-zone)

Based on current user’s location and their past selections, we can suggest a time zone that is most likely to work for the user. These suggestions would be displayed above the list for quick access. Of course, IP detection is never bulletproof, so we need to always include a way to **override the suggestions** as well.

[![Image 6: We can suggest a time zone based on user’s current location and their preferences.](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/time-zone-selection-ux/06-time-zone-selection-autocomplete.png)](https://mcusercontent.com/16b832d9ad4b28edf261f34df/images/7818b0ae-7f00-fde4-8acc-9e163aea6587.png)

We can suggest a time zone based on user’s current location and their preferences. [Source: NN Group](https://www.nngroup.com/articles/time-zone-selectors/).

## 6. Sort Countries Alphabetically, Not By UTC/GMT Offsets [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#6-sort-countries-alphabetically-not-by-utcgmt-offsets)

Since many users orient themselves in time zones through cities and countries, we could sort time zones options alphabetically, by country and at least large cities. We still need to provide UTC/GMT offsets or current time as well.

[![Image 7: A sophisticated time zone selection UX in Grafana.](https://res.cloudinary.com/indysigner/image/fetch/c_fill/f_auto,q_auto/https://main--smart-interface-design-patterns.netlify.app/static/img/blog/time-zone-selection-ux/07-time-zone-selection-type-to-search.png)](https://www.youtube.com/watch?v=GnJe-psrUA8&ab_channel=Grafana)

A sophisticated time zone selection UX in [Grafana](https://www.youtube.com/watch?v=GnJe-psrUA8&ab_channel=Grafana).

In [Grafana](https://www.youtube.com/watch?v=GnJe-psrUA8&ab_channel=Grafana), users can search by region, country, city, UTC offsets time zone abbreviations or use default settings. All cities and countries are sorted alphabetically and grouped into continents.

## Time Zone Selection UX Checklist [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#time-zone-selection-ux-checklist)

Our goal is to drive users towards an accurate selection, faster. To do that, we can embed a few little details into our interfaces:

*   **Detect and suggest user’s time zones**.

*   Support typing for city, country, locality, UTC offset.

*   Always show current times in locations.

*   Use a placeholder "Start typing..." or "Search..."

*   **Display local time zone names** (CEST, PST etc.).

*   Sort counties and cities alphabetically.

*   Don’t sort time zone options by UTC/GMT offsets.

*   **Surface critical details** (calendar availability, weather conditions, custom preferences etc.)

*   Keep your timezone database up-to-date.

## Useful Resources [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#useful-resources)

*   [A Complete Timezone List](https://gist.github.com/sandcastle/ad1e527388cad4b1236d68724a78db00), a list with grouping by timezone, in TypeScript.

*   [Standard Time Zones Of The World](https://i.stack.imgur.com/KDJun.jpg) (as of April 2014).

*   [It’s Time We Addressed Time-Zone Selectors](https://www.nngroup.com/articles/time-zone-selectors/), a wonderful usability study by Norman-Nielsen Group.

*   [On Time, Time Zones, and Software](https://lukasz.medium.com/on-time-time-zones-and-software-6617a4c22d05), a fantastic write-up all around time zones, UX and implementation details by Łukasz Tyrała.

## Wrapping Up [#](https://smart-interface-design-patterns.com/articles/time-zone-selection-ux/#wrapping-up)

Sometimes allowing users to type instead of scrolling is much faster. Time-zone selection is just an example of that. This also goes for country selectors, sliders and sometimes even navigation. The challenge is to **hide complexity** by showing users things that matter and hiding things that do not.

## Related
[Add wiki-links manually or run update_wikilinks.py]