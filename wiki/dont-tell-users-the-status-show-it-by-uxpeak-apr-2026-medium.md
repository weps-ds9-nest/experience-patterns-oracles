# Dont Tell Users The Status Show It By Uxpeak Apr 2026 Medium

## Why “Out for delivery” is a worse design than a moving pin on a map, and how the same rule applies to every screen where users wait.

Every time a food delivery app says “Out for delivery,” a small part of your brain goes _okay but where._

That gap, between what the app says and what you actually want to know, is one of the most common, most expensive, and most ignored design problems in modern interfaces. It shows up everywhere users wait. It generates support tickets. It causes uninstalls. And it’s almost always fixable with a single decision: stop describing the status, and start showing it.

This post is about that decision. Why it matters, what makes the “telling” version feel broken, what makes the “showing” version feel calm, and a four-question audit you can run on any waiting screen in your product this week.

## The same order, two screens

Imagine the same delivery: same restaurant, same courier, same twelve minutes until your door. Two ways an app could communicate this to you.

**Version A** is a vertical timeline of text labels.

> _Order confirmed, 1:58 PM ✓ Preparing your food, 2:05 PM ✓ Picked up by courier, 2:22 PM ✓_**_Out for delivery_**_, Now Delivered, pending_

It’s tidy. It’s informative. It’s also completely silent about the thing the user actually wants to know: where the courier is _right now,_ and how that translates to “should I be by the door in two minutes or in fifteen.”

**Version B** is a live map. There’s a pin for the restaurant, a pin for your address, and a third pin (pulsing, slowly moving) for the courier. A small banner at the top reads “12 min away.” A bottom sheet shows the courier’s name, photo, rating, and two buttons: Call and Message.

Same information. Completely different cognitive load.

Version A asks the user to interpret. Version B _answers._

## Why the “telling” version creates anxiety

The problem isn’t that Version A is wrong. The information it gives you is accurate. The problem is that it leaves three specific gaps that the user’s brain is forced to fill on its own.

**It gives a range, not a moment.** “ETA: 2:35 to 2:45” is a ten-minute window. The user still has to decide what to do with that window. Should they get up now? Wait? Start something they can’t easily interrupt? The app knows the answer. It just isn’t saying it.

**Its labels are stale.** “Out for delivery” looked exactly the same five minutes ago. The user has no way to tell if the system is still working, if the driver has stopped, if the data feed has frozen. There’s nothing on the screen that visibly changes over time, which is the only honest way an interface can say _I’m still here._

**It refuses to answer the spatial question.** “Where is my courier?” is the single most common reason users tap their delivery app. Version A doesn’t answer it. So the user opens Maps. Or refreshes. Or, worse from the company’s perspective, taps the “Where is my order?” button, which generates a real cost in support volume for what is, fundamentally, a UI failure.

The information was never the issue. The format was.

## Why the “showing” version creates calm

Version B does three things differently. None of them are technically harder. All of them respect how human attention actually works.

**It commits to one number, not a window.** “12 min away” is a single, definite answer. No mental math, no guessing what to plan for. The user looks once, makes a decision, and gets on with their life. (When the number changes, and it will, that’s also visible, which is itself a form of honesty.)

**It shows live position, visibly moving.** The pulsing courier pin proves the system is awake. The user doesn’t have to read anything to know the order is progressing. They can glance, see the pin has moved a block since last time, and put the phone down. Visual change is the simplest, fastest, most universal way for an interface to signal _something is happening._

**It surfaces a face, a name, and a way out.** Marco R., 4.9 stars, Call and Message buttons. If anything goes wrong (driver missed the building, can’t find the apartment number, the food got dropped) the user already knows what to do. The interface anticipated the failure mode and put the recovery path in their hand before they had to ask for it.

That’s what calm looks like in a UI: the user has fewer questions after looking at the screen than they had before.

## This isn’t a delivery problem. It’s a pattern.

The “show, don’t tell” rule shows up anywhere users wait. Once you start looking for it, you see broken versions of the pattern everywhere.

**File uploads.** “Uploading…” with a spinner that gives no indication of progress is the digital equivalent of standing in a line you can’t see the front of. The fix is mundane and well-known: a progress bar with a percentage, an estimated time remaining, and ideally a thumbnail of the file so the user knows the right thing is being uploaded. None of this is technically novel. Most products still don’t do it.

**Payment processing.** The number of checkout flows that show “Processing your payment…” with a spinner for six to ten seconds, and nothing else, is staggering. A stepper showing card → bank → confirmation, with each stage visibly completing, would cut abandonment in checkout by a meaningful amount. Stripe’s animation when a payment confirms (the green check that draws itself) is doing real work. It’s not decoration.

**Data syncs.** “Syncing your data…” is one of the most anxiety-inducing labels in B2B software. Users have no idea if they should keep working, close the tab, or go get coffee. A counter showing “847 of 1,200 records imported” turns the same wait into a measurable, finite event.

**Password strength.** “Weak password” as a static label tells the user nothing actionable. A live meter that fills as they type, with checkmarks appearing next to each requirement as they’re satisfied, turns password creation from a guessing game into an obvious, satisfying flow.

In every case the underlying truth is the same: _the system already knows what’s happening. The only question is whether it bothers to show the user._

## A four-question audit

If you want to run this rule on your own product, here’s the audit. Open every screen where the user has to wait, even briefly, for the system to do something. For each one, ask:

**1. Is there one definite answer?** Not a range, not “soon,” not “in a few moments.” A single number, position, percentage, or step the user can act on.

**2. Can the user see something change?** A pulsing pin, a filling bar, a stepper advancing, a counter ticking. Proof that the system is alive. Not just an animation, actual progress that visibly accumulates.

**3. Is the unit of progress visible?** Distance, percentage, files completed, steps remaining, items processed. Something countable. Without a unit, the user has no way to estimate whether the wait is almost over or has barely started.

**4. Is there a way out if it stalls?** A contact button, a retry, a cancel, a refresh. Anywhere users wait, they need an exit. Not having one is the most reliable way to turn a five-second wait into a one-star review.

If you can answer “yes” to all four, you’re showing, not telling. Anything less, and your interface is asking the user to trust you on faith. Most of the time, they won’t.

Most interfaces that frustrate users aren’t slow. They’re _silent._ They know more than they’re willing to share, and they leave the user to fill the gap with worry.

The fix isn’t more information. It’s the right format. Text describes. Visuals answer.

The next time you ship a screen where users wait, run the four questions. Then go look at one waiting screen in a product you didn’t build, and run the four questions on that one. You’ll see the pattern everywhere, and once you see it, it’s hard to ship the silent version again.

_This piece is part of an ongoing series of practical UX/UI design tips. If it was useful, share it with one designer working on a flow where users wait._

If you want to learn more about UX/UI design visit our website.

## Related
[Add wiki-links manually or run update_wikilinks.py]