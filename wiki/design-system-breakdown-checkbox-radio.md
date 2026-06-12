# Design System Breakdown Checkbox Radio

## Design system breakdown: checkbox & radio

Steve Dennis·2 min read·Jan 16, 2023

Clean article found smry-fast Reading stack uxdesign.cc · 308 words

The article is ready without leaving the reader. Source: Direct extraction.

## Part 2 of a deep dive series on specific design system components

Checkbox and Radio components typically share so much DNA, that when we prioritized them early in [Castor](https://castor.vercel.app/?path=%2Fdocs%2Freact-checkbox--playground) ’s development, we built them in parallel with a lot of shared research and specs. Here I’ll cover some of the design decisions, and tradeoffs that went into both of these components.

Checkbox and Radio components in unselected and selected states

## Design goals

We started as we always do, by performing a visual audit of our products containing checkbox and radio controls. We found some common patterns with varying visual implementations that seemed perfect candidates for consolidating into one consistent pattern, while improving accessibility and usability of these controls.

Our goals were:

1.   Raise the bar for accessibility
2.   Replace existing custom implementations with a consistent component

## Accessibility

Accessibility is often our starting point, our baseline for what we really want to improve. Our audit revealed that many of our existing implementations had touch-areas that were too small, some with low contrast (especially in dark mode), and almost all of them lacked highly visible focus states.

A collection of different checkbox and radio implementations with no coherent style across them, but similarities that pointed to similar requirements.

## Size & Touch area

With some experimentation, we quickly discovered that checkbox/radio look incredibly, incredibly weird if you make the visible control the size of the touch area (in our case, 48px tall). At that size, they were too easily confused with short-width text inputs when unchecked, and just look comically oversized in the contexts we had when checked, compared to what people are used to.

I do need to shout out the GOV.UK design system and their [40x40 checkboxes](https://design-system.service.gov.uk/components/checkboxes/) though. In their context that’s largely form-filling, and with a general aesthetic that supports it it makes total sense.

## Related
[Add wiki-links manually or run update_wikilinks.py]