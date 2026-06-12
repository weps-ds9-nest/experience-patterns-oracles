# This article follows on my previous article, which detailed [guidelines for time indication in systems](https://medium.com/@chris_kiess/guidelines-for-time-indication-and-progress-bars-in-user-interaction-design-4d5038084c84) and comes directly from the work of Steven Seow, [Designing and Engineering Time](https://www.amazon.com/Designing-Engineering-Time-Psychology-Perception/dp/0321509188). I cannot recommend his book enough as it truly encapsulates most, if not all, problems you might encounter in attempting to represent time and mitigate waits in UI design.

This article follows on my previous article, which detailed [guidelines for time indication in systems](https://medium.com/@chris_kiess/guidelines-for-time-indication-and-progress-bars-in-user-interaction-design-4d5038084c84) and comes directly from the work of Steven Seow, [Designing and Engineering Time](https://www.amazon.com/Designing-Engineering-Time-Psychology-Perception/dp/0321509188). I cannot recommend his book enough as it truly encapsulates most, if not all, problems you might encounter in attempting to represent time and mitigate waits in UI design.

In my previous article, I discussed time anchors as a technique for representing time in “human language.” That is, we want to represent time in a system or UI in the same way we, humans, speak of time. Consider how we converse about time. If I were to ask you how long you walked your dog today, you would not report to me an exact number such as 38 minutes. You would say, “About a half-hour.” This is the idea behind time anchors.

As humans, we round off time when we speak of it and estimate in both round numbers and round ranges. Another example: At your doctor’s office, you might inquire as to how long the wait will be. You would not be given an answer of, “Oh, about 5–20 minutes.” It is more likely you would be given an answer like, “About 5–10 minutes.” Time anchors help us represent ranges.

In short, use time anchors when following the rules below as they will provide round numbers. Additionally, ranges help prevent us from being held to exact numbers when exact numbers are hard or nearly impossible to estimate.

### Rule 1: Avoid elapsed time when possible

Elapsed time is simply showing how much time has passed (counting up instead of down). This is usually done showing seconds, minutes and hours. You generally want to avoid this with the exception of processes where the amount of time passing is clearly needed. For example, elapsed time is valuable for processes where a payment might be time dependent (a long-distance phone call) or where a process needs to be timed (production facilities or cooking food).

Showing elapsed time for any other process is the equivalent of watching your soup come to a boil on a cold winter’s day. Stand over the stove and watch the soup heat up and 5 minutes will seem like an eternity (especially if you are hungry). Go sit down, watch some TV and 5 minutes will go so fast you might just have to worry about scalding your soup.

When we show elapsed time, psychologically it is a bit of torture for the user and it accentuates the passing of each and every second and minute. You want to avoid this in an interface, when at all possible.

The best example (or perhaps the worst) I can think of in regards to this rule is the old drive-thru timers fast-food restaurants used to use. About 5–10 years ago, fast-food restaurants would place these timers at the drive-thru windows and show you exactly how much time was elapsing before your order was supposed to be up. These timers rarely exist today (possibly for the reasons I am citing here in rule 1).

*   Only use elapsed time when there is a clear value for the user to know how much time has passed for a process that has a time dependency.
*   For progress indication in interfaces, use a countdown timer to show time remaining (a more specific indication) rather than elapsed time (a non-specific indication).
*   For longer durations, use time anchors to specify a range.

### Rule 2: Write singular units as non-plural entities

It’s a small detail, but much like the fit and finish on an automobile. When using a singular unit of time (i.e. “1 minute, 1 “second”) do not code the interface to state “1 minutes.” That is just lazy programming. Take the extra time to code the progress indication so 1 minute or 1 second (singular units of exactly 1) are written in the singular voice and multiple minutes are written as plural. This just gives your software a more professional feel.

### Rule 3: Finish on time

If you provide an indication that a process will take 10 minutes, ensure that the indication does not take longer. In short, finish within the stated time. Do not stop the timer or bounce it from 7 minutes back up to 8 minutes. Likewise, ensure the progress bar does not bounce back and forth. That is, a progress bar should progressively fill — not reach 80% and then move back to 60%.

## Get Chris Kiess’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

When such techniques are employed in interfaces, it gives the user an impression that the time indication is inaccurate and unreliable. They will cease to trust or have any faith in the estimations of progress, which will result in a lack of specificity. Lacking specificity is essentially putting your user in a time limbo where they will not know how long the wait will be. This is the equivalent of being stuck in traffic when you cannot see how long the traffic jam is and have no idea what is causing it. Time seems to go on forever when there is no accurate indication or estimation of how long a process or wait will take.

### Rule 4: Use numbers or words, but be consistent

This is a simple one and like rule 2 above, it simply gives your software a polished feel and makes time units less confusing for the user in terms of not forcing them to cognitively shift gears for language inconsistencies.

Either use numbers to express time units (“this process will take 1 to 2 minutes”) or use words (“this process will take one to two minutes”). Do note: Double-digit numbers are better expressed as numbers rather than words as it is easier for us to process longer numbers as digital entities.

### Rule 5: Avoid ambiguity

Do not use terms such as “awhile” or “in a moment.” These terms lack specificity (see my point above on specificity). They will likely frustrate your user more than simply not saying anything at all. Be clear concerning the amount of time or the range of time a user should expect to wait on a process to finish.

### When you cannot estimate the length of a process

What do you do when you don’t know how long a process will take and cannot estimate the length? I received a similar question when I presented on this topic at IA Summit this year. There are two possible ways to handle this and I have used both in interfaces.

First, you can find some means of reporting on the processes being completed. In many instances, this can be a progress bar slowly filling with a description of the processes being completed underneath it — number of files scanned, number of documents copied, compiling, completing final details, etc. And, you can show these stages sequentially to indicate they are staged. This is better than showing nothing and though it does lack in specificity in some ways, it still shows the user each stage of a process and indicates the process is progressing.

One thing to remember here: Don’t stop the progress bar. You might leave the descriptive terms (i.e. “extracting files”) under the progress bar for several minutes, but keep the progress bar moving. This will still give the user an indication progress is being made.

Second, use a refresh or time-out feature for processes that may move beyond the normal estimated time for a process. This means you need to know how long the process should normally take and where the failure point falls. For example, perhaps your process should normally take 10 seconds and you find the failure rate is 80% if the process moves beyond 20 seconds. In this scenario, you would simply work an algorithm into the code where 20 seconds would be the trigger (the time-out) for either a retry or a refresh button.

Keep in mind: Processes that last longer than 10 seconds should always have a cancel button or a way for the user to get out of the process.

## Related
[Add wiki-links manually or run update_wikilinks.py]