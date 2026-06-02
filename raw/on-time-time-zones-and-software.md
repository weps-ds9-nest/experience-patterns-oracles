Title: Article from lukasz.medium.com

URL Source: https://smry.ai/https:/lukasz.medium.com/on-time-time-zones-and-software-6617a4c22d05

Markdown Content:
## Time zones are tricky. Basics, a bit of history, and tips in this article will help designers and developers create UIs with good UX.

S [ystem time](https://en.wikipedia.org/wiki/System_time) is the way we deal with **time in software**. This is universally defined as seconds that passed since [1 January 1970 00:00:00 UT](https://en.wikipedia.org/wiki/Unix_epoch). From the software perspective, the time is the same, and identified in relation to Universal Time (UT).

Time in different parts of the world is determined by [time zones](https://en.wikipedia.org/wiki/Time_zone). Time zones are a function of the Earth movement, the Sun and human agreements.

Today, the world uses [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) (UTC) as a **standard to set our clocks and time**. [Offsets](https://en.wikipedia.org/wiki/List_of_UTC_time_offsets) are how the time changes while going east and west of UTC. [Historically](https://youtu.be/g52A2CPEi4A), [GMT](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) was used.

Some [countries are located within **a few time zones**](https://en.wikipedia.org/wiki/List_of_time_zones_by_country). Thus, knowing a country name does not imply knowing the time (or a time zone).

Many countries use [daylight saving time](https://en.wikipedia.org/wiki/Daylight_saving_time) (DST). This leads to different abbreviations and time zone names. **UTC does not change with DST**, so some countries, like Poland, change from one UTC offset (UTC+1) to another (UTC+2) — by picking offset manually only, people need to remember to change the offset when daylight saving time is being used. Also, UTC offset is not limited to hour increments, we have UTC+9:30 and UTC+12:45.

Locally, [the time zone names](https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations) (with its abbreviations) are used. The timezones include DST, like CET (Central European Time) and CEST (Central European Summer Time).

Map of the World Time Zones divided into Coordinated Universal Time, UTC

There are **38 time zones based on UTC offsets** (with Iran on Standard Time, 37 with Iran on DST). In the end, the software needs to know in which of the offsets is the timestamp saved. This is more complicated than the usual definition of 24 time zones being 24 zones with borders defined by 15° wide meridians. In the military, there are [25 zones designated with letters](https://en.wikipedia.org/wiki/List_of_military_time_zones). The Zulu time zone corresponds to UTC.

To add to that, there are a few thing to consider:

*   we have [**leap seconds**](https://en.wikipedia.org/wiki/Leap_second) (when leap second is included, there is a minute that lasts 61 seconds, 0–60), that are included in UTC, but not with Unix Epoch, and are not included with UT1 and UT2 used by astronomers,
*   in history, [we have gone through **calendar changes**](https://en.wikipedia.org/wiki/List_of_adoption_dates_of_the_Gregorian_calendar_per_country), when weeks were skipped from time continuum, and the changes happen at different time for different countries,
*   there are regions, which have **different timezones in parallel**,
*   some countries changed time zone, which resulted in **skipping a full day**,
*   sometimes the **changes are done with a very short notice**, and can happen few times a year,
*   **Daylight Saving Time goes into effect at different dates for different countries**.

Remembering all of the complexities is hard. When working with computer software, the [**tz database**](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) comes with help, as it provides names for timezones (TZ), like Europe/Warsaw (also called Olson ID). [tz database](https://en.wikipedia.org/wiki/Tz_database) (tzdata) is a part of most programming languages, like [Go](https://golang.org/pkg/time/#Location), and covers all the rules. And it is open source.

[Official source of the Time Zone Database](https://www.iana.org/time-zones) provides additional resources and latest distributions.

TZ database stores not only **Canonical** time zone IDs (the primary, preferred zone name) but also _Aliases_ (an alternative name, which may fit better within a particular country) and _Deprecated_ (left in the tz database for backwards compatibility, which should not be used if not necessary) statuses.

[Some libraries](https://momentjs.com/timezone/)**augment the tz database with additional information**, like countries. It is important to consider the reliability of the data, but also an ability to connect Olson Time Zone ID and countries, as en example

**W3C Working Group maintains**[guidelines and best practices for working with time zones](https://www.w3.org/TR/timezone/) in applications and document formats. It includes general consideration for programming, but also tips for [negotiating time zones with the user](https://www.w3.org/TR/timezone/#negotiating).

There are 3 important categories for considering time zones and software:

(_i_) **Storing, passing and retrieval of a time data** (with data and time information) within the system — for that purpose, using the UTC is a reliable choice, as this allows to standardise the time across the whole year and the globe. The important part is to remember that offset will change for DST time zones, but for storing, passing and retrieval purposes, we can do it on the fly.

(_ii_) **Display of the timezone for users** — for this scenario few pieces of information and formats might be useful:

*   Actual time (f.e. 10:00 or 10 am) with appropriate granularity.
*   _Local_ time zone names, like CEST, PST/PDT.
*   UTC offset.
*   Name of the timezone according to the tz database, like _Europe/Warsaw_.
*   Geographical name, like continent, **country** or city.

(_iii_) **Time zone picker for set-up or configuration** purpose:

*   Name of the timezone based of the tz database seems like a minimum and important middle ground between UTC used as a storage and the usability of timezones for users.
*   The helpful thing is a country name, that can be a two-step process: pick the country, then pick a specific time zone for the country.

In the end, **the most important things to consider** are:

*   **Reliability of the data stored within the system** — here, the UTC is the best choice.
*   **Reliability of the time zone names and identifiers** — picking a library that is ofter updated and follows the worldwide changes is crucial. The tz database is a no brainer here.
*   **Usability** of time zone selection — the system should consider dailies saving time on the fly for people and allow them to search based on names (timezone name, continent, country, city — with cities being the bare minimum).
*   **Lowering cognitive load**, by surfacing information about timezone name, country, current date and time, UTC offset.
*   Making all the information **accessible** and the **experience** as easy as possible with autocomplete features, a grouping of the data, and clean interface surfacing time zone data and identification.

[The International Date Line](https://youtu.be/aBppb2quqkE) is a fantastically interesting topic that is worth exploring but does not impact UI’s (apart from communicating a change in day for rare timezones) or time storage.

### Glossary:

[**ISO 8601**](https://www.iso.org/iso-8601-date-and-time-format.html) — international standard for numeric representation of dates and time.

[**ISO 3166**](https://www.iso.org/iso-3166-country-codes.html) — contry codes, like PL for Poland.

**UTC** — Coordinated Universal Time, the same as GMT (Greenwich Mean Time) but language-neutral.

**DST** — Daylight Saving Time, also called Summer Time. It does not affect the UTC offset. Standard Time is a legal time, without DST.

**LMT** — Local Mean Time, is a solar time at a specific location. This was the time used before standard time.

[**NTP**](https://tools.ietf.org/html/rfc1305) — Network Time Protocol

[**RFC 3339**](https://tools.ietf.org/html/rfc3339), Date and Time on the Internet: Timestamps
