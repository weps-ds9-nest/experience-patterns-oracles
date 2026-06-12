# Photo by Rahul Mishra on Unsplash

Photo by Rahul Mishra on Unsplash

I want to talk about something most design system articles skip entirely: what happens when the codebase under your system is a mess.

Not a small mess. Ten years of Angular, jQuery, and React all living in the same repo. Feature flags from 2017 still active. Three different validation libraries. API responses that return the same data in different shapes depending on which service you hit. That kind of mess.

When I started building the design system on top of this, I kept looking for writing from other designers who had done something similar. Most of what I found was either architecture-level content about the Facade pattern written for backend engineers, or process-y design system migration guides that assumed you had a clean modern codebase to work with. Neither described what I was actually doing: trying to create consistent, trustworthy UI patterns on top of code that actively resisted consistency.

## The goat problem

There’s no polite way to describe it. Building a design system on top of a legacy codebase feels like putting a tuxedo on a goat. The goat doesn’t want the tuxedo. The tuxedo wasn’t made for a goat. And everyone in the room can tell something is off, even if the goat looks surprisingly presentable from certain angles.

The instinct is to rewrite everything. Start fresh. Burn it down. I’ve sat in meetings where people genuinely proposed this with straight faces, as if a full rewrite of a decade-old enterprise product was something you could just schedule into a quarter.

We weren’t going to rewrite. We didn’t have the time, the budget, or the organizational appetite. So we needed a different strategy.

## Using the design system as a facade

The Facade pattern in software architecture is about creating a clean, simple interface that hides the complexity behind it. A front door that looks like it belongs to a nice building, even if the hallways behind it are a disaster. We applied the same idea at the component level.

We built modern React components that wrapped the legacy logic underneath. To anyone using them, a designer pulling from the library or a newer developer building a…

Did you enjoy reading this on SMRY?

Tell us what would make the reader better

Did you enjoy reading this on SMRY?

Tell us what would make the reader better

## Related
[Add wiki-links manually or run update_wikilinks.py]