# Performance Design Designing For The Illusion Of Speed

## Learn how the labor illusion and benevolent deception work to improve our perception of interface loading times.

[Source](https://dribbble.com/shots/6642842-Loading-Dark-Mode-Gradients/attachments/6642842-Loading-Dark-Mode-Gradients?mode=media)

D **id you know every second Walmart shaves off of its e-commerce website** improves its conversion by [two percent](https://juneuprising.medium.com/designing-for-the-appearance-of-speed-aaabc7f568c2) (860 million out of [43 billion dollars per year](https://www.statista.com/statistics/1109330/walmart-ecommerce-sales-by-division-worldwide/))? [Studies](https://www.radware.com/homepage/home-page) show that a mere 0.5-second delay results in a 26 percent in user frustration and an 8 percent drop in engagement. Let’s face it; slow sites impact purchase intent and user trust.

The lucky few have the luxury of lightning-fast 4G LTE connections, but most of the world still relies on 3G (<15 Mbps) network speeds. We need to start designing for realistic internet speeds. Welcome to the world of performance design.

## Measurable vs. perceived performance

There are two methods to address performance: (1) reducing the measurable (actual) wait times vs. (2) creating the illusion of shorter wait times.

[Source](https://www.atlasobscura.com/articles/history-of-elevator-music)

We can learn a lot about the power of perceived performance from a [story about an old New York building](https://www.samuelthomasdavies.com/elevator-waiting-times/) where tenants complained about “excessive” elevator wait times. The building manager could not develop a feasible solution to reduce the wait times (measurable performance).

After some deliberation, one of his staff came up with the ingenious solution of installing mirrors to alleviate the boredom of waiting. Despite no improvements to measurable performance, all the complaints disappeared!

The Houston airport had a [similar problem](https://www.nytimes.com/2012/08/19/opinion/sunday/why-waiting-in-line-is-torture.html) due to complaints about excessive wait times at baggage claims. Despite hiring more staff to increase measurable performance, complaints existed. Similar to the elevator scenario, people were upset at the unoccupied time and boredom rather than true performance.

Their ingenious solution was to move the arrival gates farther from the baggage claim, so people had to walk longer, eliminating all the unoccupied time and the complaints.

These stories aren’t meant to discount the importance of measurable performance but instead call out that sometimes the root problem is behavioral.

When evaluating which performance to improve, consider the context of the use case. Sometimes the perceived performance is more important than the actual “under the hood” performance measured in milliseconds.

## Improving perceived performance

## Skeleton screens

When loading a new page [instead of using spinners](https://www.lukew.com/ff/entry.asp?1797=), opt for skeleton screens instead. Users will [expect a 1:1 mapping](https://www.linkedin.com/pulse/how-linked-got-skeleton-screens-wrong-parimala-hariprasad/) between the skeleton screen and the content once it’s loaded. This is known as the principle of [natural mapping](https://en.wikipedia.org/wiki/Natural_mapping_(interface_design)#:~:text=The%20term%20natural%20mapping%20comes,memory%20to%20perform%20a%20task.).

The skeleton content (rendered as blocks) should be replaced with actual content (images, text, etc.) as the page loads. The skeleton content should be in the same position and have similar dimensions as the actual content once it’s loaded.

When there’s a mismatch between the skeleton and real content, the page will “jerk” as it scrambles to rearrange itself. This creates the impression that the page is not well built and reduces user trust.

LinkedIn’s skeleton loading screen ( source ).

Instant page transitions like this reduce the perception of waiting through movement. The best skeleton states [implement a low left-to-right “shimmer” animation](https://uxdesign.cc/what-you-should-know-about-skeleton-screens-a820c45a571a) across the placeholder blocks to reinforce this principle.

Youtube’s skeleton loading screen ( source )

To learn more about skeleton screens, I recommend reading Bill Chung’s [guide](https://uxdesign.cc/what-you-should-know-about-skeleton-screens-a820c45a571a) (which includes interesting research findings & user tests).

> An interesting finding from an old AB test I ran: when mobile users encounter “native” loaders (standard loaders in their OS), they tend to blame their device instead of the app or website.

## Smooth animations

Poor animation in an interface also hurts perceived performance. Animations that are not well designed, too complex, and don’t move as expected impose higher mental interaction costs (MIC) on the user.

## Get Richard Yang (@richard.ux)’s stories in your inbox

Join Medium for free to get updates from this writer.

Animations [should be smooth and rendered at 60 fps](https://allenpike.com/2011/providing-joy-at-60-fps), which is required to eliminate the perception of stuttering. This is even more critical in animations that respond to a user’s action; even a slight lag between touch and response makes the experience feel “sluggish.” When applicable, use [momentum-based scrolling](https://miro.medium.com/max/1600/0*BHCeMwJ88gcol-dt.gif) (smooth scrolling mimicking real finger motions) instead of fake scrolling (unnatural scrolling with abrupt stops).

Protip: To achieve 60fps animations, leverage CSS transformations accelerated using a hardware graphics processor such as position (translate), scale, rotation, etc. For newbies, I wrote an intro to UI motion design [here](https://uxdesign.cc/get-started-with-motion-design-in-8-minutes-3c21889ec28b). For more technical designers (who can code), look into building progressive web apps (which cache parts of the interface) with [app shell models](https://developers.google.com/web/fundamentals/architecture/app-shell) and [service workers](https://developers.google.com/web/fundamentals/primers/service-workers).

## Benevolent deception and the illusion of labor

There are some unique scenarios where you want to insert an artificial progress bar or loader to instill confidence in the user’s actions. This practice is known as “ [benevolent deception](http://www.cond.org/benevolent.html),” where products insert a fake loader for the user’s benefit.

Humans tend to have a natural heuristic where fast = simple or cheap, and good things are worth the wait.

[Source](https://turbotax.intuit.com/)

For example, TurboTax creates a static fake loader animation after the user submits their tax information to “double-check their return for every possible tax break…” The fake loader helps build users’ confidence in the product they just entrusted with their financial information.

Other times, this technique [builds excitement](https://www.uxmas.com/2013/wait-for-it) and instills a feeling of accomplishment. In the mobile version of the Ticket to Ride board game, the final scores are tallied one at a time, with the user’s scores tallied last.

[Source](https://store.steampowered.com/app/108230/Ticket_to_Ride__Europe/)

A quick reveal of the final scores would kill the experience. Instead, you get a stirring, climactic end to a game you’ve invested a good deal of your time playing. Consider that [dopamine is released in anticipation of the reward](https://www.youtube.com/watch?v=axrywDP9Ii0) (rather than when the reward is given). Dopamine is not about pleasure; it’s about the anticipation of pleasure.

The “fake” loader or excessive animation is a common design practice known as “ [labor illusion](https://www.hbs.edu/faculty/Pages/default.aspx).” Studies show that users trust and value important results (e.g., tax returns) more after waiting for them (even if the results can be computed instantly).

## Pacing tricks

There are [several interesting techniques](https://uxmovement.com/buttons/how-to-make-progress-bars-feel-faster-to-users/) to improve the perception of loaders. For progress bars, implementing “gradient ribbings” that move backward (while the bar progresses forwards) [reduces our perception of wait time](http://.net/projects/progressbars2/ProgressBarsHarrison.pdf).

Another trick for reducing perceived wait times for determinate linear loaders is to accelerate progress near the end. Ever get frustrated when a progress bar is 99 percent, but the last 1 percent takes forever to complete?

Users tend to be more forgiving of pauses and extended wait times at the start of a progress bar. In contrast, when there are pauses near the end of progress bars, it becomes more evident and frustrates users focusing on it.

[Source](https://www.grubstreet.com/2017/11/app-truthers-claim-dominos-lies-about-who-makes-their-pizza.html)

For indeterminate circle loaders, increasing the number of pulsations or revolutions also reduces the perception of wait times. When a progress bar pulsates, it acts like a metronome counting the “tempo” of the progress time.

Spinner icon.

In conclusion, while designing fast-loading experiences and reducing waiting times is a good practice, it’s essential to consider when it makes sense to improve perceived performance (i.e., skeleton screens, smooth animations, and pacing tricks) over measured performance.

In some scenarios, the root problem isn’t the actual loading time but rather the user’s waiting behavior. Other times, the product experience might benefit from the “labor illusion” and benevolent deception. It’s up to us, as designers, to consider the situation and do what’s best for our users.

The UX Collective donates US$1 for each article we publish. This story contributed to World-Class Designer School: a college-level, tuition-free design school focused on preparing young and talented African designers for the local and international digital product market. Build the design community you believe in.

## Related
[Add wiki-links manually or run update_wikilinks.py]