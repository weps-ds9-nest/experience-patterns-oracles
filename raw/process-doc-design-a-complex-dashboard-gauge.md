Title: Article from medium.com

URL Source: https://smry.ai/https:/medium.com/@lodestar-design/process-doc-design-a-complex-dashboard-gauge-3d93973db80

Markdown Content:
## The Mission

A client from my company recently asked me to provide a design for a gauge. The gauge is meant to be used by engineers who need to monitor equipment status and quickly address any faults or alarms when flagged by the system.

Unlike a regular gauge we see in consumer apps, the client demands that users should have access to all the following readings, ranked by priority:

*   Current meter reading
*   Min/max/average reading reached in the past 24 hours. This is so that engineers returning back to work know what happened outside their shifts.
*   Up to four thresholds where warnings and alarms may be triggered.
*   Gauge min/max

These gauges are meant to be packed in highly-dense dashboards to allow easy side-by-side comparisons across different sensor readings.

Our target users are expected to use a dashboard like this to identify anomalies, where gauges are placed in a large matrix.

## Previous Attempts

Before we jump into what I did, I have to point out that this was not their first design attempt. However, the design iterations before mine were unsatisfactory for the Product Owner, because they lack either clarity or consistency.

Lack of clarity — what are these lines? To be fair, these designs included micro-interactions, like hover animations, to help users decipher its meaning. But they are not obvious at a glance.

Lack of consistency — sometimes a colored bar is used to indicate the range, other times it is used for the current reading. Neither is that triangle indicator used inconsistently.

Judging from these designs, I learned that the client was looking for a dashboard widget that:

*   contains all readings
*   consistent — users should not be forced to learn to read a new gauge when they are on a different page
*   flexible —the gauge can show or not show historical readings

The final design attempt from the previous designer before it was handed over to me.

## Inspirations

Initially, I was thinking about a simple line chart:

Line charts like these are great for stock market apps, but can be deceiving on what the current value is.

But I soon realized that line charts like these focus on the historical trends, but care less about the absolute value, let alone compare readings side-by-side on a dashboard.

The next closest thing that puts a greater emphasis on the current reading but still visualizes data history is the Weather app on iOS:

The Weather app on iOS, showing not only the current temperature but also the min/max in a 24-hour period with the colorized comfort level.

## Iteration 1: Real-time indicator

I was motivated by “real-time indicators” frequently used by maps and data visualizations. Whether it is to indicate the user’s current location, or that a dashboard is automatically refreshed, the user interface often includes a pulsing animation like this:

Pulsing animation

I was instantly in love with that idea:

However, when I plug in the design into an actual dashboard, I started to notice how distractive a pulsing animation can get:

Three green dots on a busy dashboard are yelling together to the user, “Look at me! I said LOOK AT ME!”

I needed to think of a better way to highlight the gauge’s current meter reading.

## Iteration 2: Align those numbers

One additional flaw I noticed from this previous iteration was that these number labels are extremely hard to read on a dashboard page. Dashboard users should be able to quickly learn about a system’s status quo and quickly identify problems, if any. Users who need to examine a full-blown data visualization should do so on a separate page, not on a dashboard where everything is competing for the user’s attention.

Users should not be forced to shift their sight left and right constantly to read numbers:

While reading through the dashboard, the poor user’s focus is forced to shift left and right. Maybe we should keep these numbers more aligned?

Imagine a data table with different cell width! So I took the data out of these gauges and placed numbers on the side:

Insightful and easier to scan

This design concept also added a lot of flexibility to the card layout:

In addition to lists, gauges can be placed in cards too.

I applied edge cases to the design too:

Edge cases, when data show irregular behaviors

I like this version. But can we do even better?

## Iteration 3: Highlight the anomaly and de-emphasize the regular state

As mentioned before, engineers — our targeted users—care more about anomalies than regular states. When an alarm goes off and they log on to see the dashboard, engineers want to quickly locate the source of the alarm before committing to any further actions.

Thus we want the alarm to put more emphasis on the red and yellow colors:

Make red extra red

If the gauge’s current meter reading falls in one of the anomaly states, the dashboard should highlight the anomaly even more:

Side stripe and gradient combined to bring extra attention from the user, without coloring the entire dashboard card yellow

## Iteration 4: Avoid distractions from other colors

Many engineers are very accustomed to the “traffic light system”. One person I interviewed for user research once told me every day he “opens the cabinet and if everything is green, he knows he’s in good shape.”

This is a small touch, but I find it effective at removing distractors:

Left: Original. Right: Remove the colors of the thresholds, and reveal them again on mouse hover.

## Final

Here’s the final design:

The accepted version. Note that this is intentionally made busy to cover all edge cases; normally you would not have this many alarms.

One thing worth noting is that the client initially preferred the design displayed in “Iteration 1”, for all the data are labeled directly on the gauge. I had to explain how dashboards are meant to give people a quick glance to identify a problem, while charts are meant for people to sit down and examine details more carefully. Eventually, the whole team was convinced and unilaterally voted for this final version to be implemented.

## Lingering Problems

Although I have finished my design work from the client, there are still a few extra lingering problems to be solved if we want to componentize this design. To include it in a design system, I have to think about all possible ways that this design can possibly fail.

First, what if the thresholds are extremely close to each other? For example, what if “green” ranges from 0 to 76, “yellow” ranges from 77 to 78, and green ranges from 79 to 80?

Gauges with tight thresholds

We might be able to have a non-linear scale that shrinks the length of the green section and increase the yellow and red sections. But will users find that deceiving?

The second problem is that the historical data range can be deceiving. Imagine if your dashboard looks like this:

What’s the current reading?

New users might think the current reading is where the green bar ends instead of where the white dot is. This problem exacerbates when you try to use a vertical gauge — people might perceive it more like how thermometers work:

Now, what does this gauge reading? Should I read it like a thermometer?

There was a place in the client’s application where they tried to use a vertical gauge like this. I was eventually able to convince them to use a horizontal gauge for consistency. Still, I think the problem is not negligible. This might be prone to human error and can have serious consequences depending on the operation.

Perhaps this will mitigate the problem a bit?
