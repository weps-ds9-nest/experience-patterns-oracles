# Stop using those boring loading spinners in your user interfaces. Seriously. It’s killing your apps’ experience more than you know.

Stop using those boring loading spinners in your user interfaces. Seriously. It’s killing your apps’ experience more than you know.

A loading spinner might be the solution to your content loading problems. But I’m here to tell you that it’s not.

You might even use some of those fancy animated loading Spinners. But they’re not any better either.

By Tobias Ahlin on Dribbble

## Why the Loading Spinner doesn’t work

From a long time we’re following, or rather influenced by hard rules from design languages. I don’t blame you though.

> _The key to wisdom is this — constant and frequent questioning, for by doubting we are led to question and by questioning we arrive at the truth. — Peter Abelard_

A Loading Spinner is one of the most used progress indicators in user interface design. But it has its own flaws which are generally overlooked.

Facebook using Loading Spinners for images and Pagination

Whenever I see that many Loading Spinners, I get a mini anxiety attack.

## 1. No sign of progress

What does the loading spinner tell you? It denotes that content is currently loading. But does it say how much has loaded? Does it say how much remains to load?

No. It doesn’t

Moreover, it’s difficult to determine. If it could, we’d be using a Progress Bar right?

## 2. That period of uncertainty

By Chanpory Rith on Dribbble

How long did you spend looking at that? Were you expecting some content to load after some time? I’m sorry to disappoint.

Ok, let’s assume that GIF loading actually completed and some content displays. Ask yourselves these questions and give me an honest response. I’m sure you’ve stared at enough Loading Spinners to know.

When you looked at the Loading Spinner, did you know:

*   how much time remains to complete?
*   how much of the content has loaded?
*   how much remains to load?

We simply sit staring at a Loading Spinner. Hoping that it loads in time, with no answer to either of those 3 questions.

Moreover, network connections might be unstable. So we can never take for granted that content will always load fast.

## 3. Perceived to be slower than actual

Loading Spinners make loading appear slower. Period.

It’s like a clock, constantly ticking. It shows the time you’re wasting by staring at it. Like that GIF above, which I made you stare at.

## 4. What comes next is a surprise

Until everything has loaded, do you have any idea what to expect on screen? I bet you don’t. You might even get surprised once the UI and content display.

Now think about your users. Until everything has loaded, they have completely no idea what to expect on screen. I bet they’ll get surprised too.

This won’t be their fault. You didn’t tell them what to expect in the first place!

### A ‘Surprise’ isn’t always a good thing.

> _An unexpected or astonishing event, fact, etc. — Surprise_

From the very definition of the word, a surprise indicates an ’ _unexpected_ ’ event. People tend to have polarising reactions to such events. This could either positive or negative.

Surprises don’t often tend to leave a positive impact on people. Unless it’s their birthday. It depends upon how a person takes it. Thus, herein lies the problem.

Take a good look at both the images. See the image on the right. Could you honestly predict the UI would finally look like that? I’m sure not.

Alright, the final UI is a low fidelity design. But you get the point.

I deliberately did not pull examples from existing apps. Because you and I both know what it will look like. With a known app, we’ve already seen the interface, even before its loaded.

## 5. Emotions affect our sense of time

Did you know? We humans can actually predict time. That too quite accurately!

But under an emotional influence, our sense of time is significantly clouded.

We’ve all experienced this. Time seems to fly when you’re doing what you love. But if it’s something you hate, time seems to drag. Even when you’re bored, staring at the clock waiting for your favourite show. Time moves even slower then.

This same holds true for our interfaces.

The point I’m trying to make is, your content might not take much time to load. In fact, it might not be a big deal. But it may appear longer than it actually takes. It is just how people might perceive it.

What we can do, is help change their perception. We can make our app ‘appear’ faster than it actually is.

**_NOTE:_**_Don’t get too carried away trying to fake it. Your interface needs a combination of real and perceived speed to succeed._

## The Illusion of Alternatives

Typically, we have two options to denote loading content:

1.   **Finite progress bar** — if we can determine load times
2.   **Loading Spinner** (infinite loading progress) — if load times are unknown

But take a closer look at the choices again. Do you realise, there is no real choice here?

We can’t use a finite progress bar because we cannot measure load times. Also, we already know that the Loading Spinner is no good.

### A good progress indicator

A good progress indicator is one which obviously doesn’t have any of the negatives I mentioned above. But for a more optimistic tone, let me list them out.

1.   Gives immediate feedback
2.   Provides a sense of time ( how much has progressed, and how much is pending)
3.   Removes doubt (gradual progress reassures people that the app is working)

## Some proof as backup

Some of you might not believe what I said. Even I wouldn’t. After all, where is the proof? Do loading indicators really harm? Who has experienced it?

Well, then consider yourself lucky. You get to learn from someone else’s mistakes.

The [iOS app Polar strongly suggests avoiding the Spinner](http://www.lukew.com/ff/entry.asp?1797=).

Polar received a lot of complaints about their app being slow. This was because of the loading spinners they included in their app.

> _With progress indicators, we had made people watch the clock. As a result, time went slower and so did our app. We focused on the indicator and not the progress, that is making it clear you are advancing toward your goal not just waiting around. —_ Polar

I guess I’ve rambled enough about why Loading Spinners are bad. The problem with a Spinner lies in not providing a sense of progress. Though, we can remedy this.

How, you ask? The answer is ‘ **_Skeleton Screens_** ‘.

## Skeleton Screens to the rescue

Unlike Loading Spinners, where the UI displays all at once. A skeleton screen helps load a user interface gradually, a little at a time.

## Get Suleiman Shakir’s stories in your inbox

Join Medium for free to get updates from this writer.

This means that the barebones UI displays first. Then the loaded content is gradually populated on-screen.

> _“A skeleton screen is essentially a blank version of a page into which information is gradually loaded.” — Luke Wroblewski_

LinkedIn recently started using Skeleton Screens for loading.

Skeleton screens shift the attention of users. It makes people focus on the progress, rather than the wait time.

Skeleton screens visually tells users what to expect from the interface. It gives them a heads up on what’s going to come and creates a sense of gradual progress.

Most of all, it makes people perceive your site to be faster than it actually is. Remember that we are designing interfaces for use by real people. We need to give people the illusion of speed.

> _The more the system gives information about the waiting time, the better the satisfaction of the user. —_[_How to Improve Perceived Waiting Time in HCI_](http://www.guillaumegronier.com/cv/resources/Articles/2013_WorkshopHCI_Gronier.pdf)

Using a skeleton screen gives you the following benefits:

*   Helps people perceive your screen to load faster
*   Eliminates surprises
*   Gradual loading of UI — clear indication of progress
*   Shows exactly what’s loaded and what’s yet to load

## Gradual progression

I know it’s a fancy term. But what it means is, loading your content gradually. Folks from web design and development know this as ‘ _Lazy-loading_ ’.

> _Defer initialization of an object until the point at which it is needed. —_[_Lazy Loading_](https://en.wikipedia.org/wiki/Lazy_loading)

First, lay out the bare bones UI (Skeleton screen). Next, load the text data. By now, the user knows they’ve received the content. Finally, lazy load the images. The user now understands that most of the content has loaded and what’s left are the images.

In this way, you’ve given users:

*   A clear sense of progress
*   What to expect next
*   What’s left to expect

Notice how Instagram intelligently handles loading here.

Instagram loading — gradual progression

First, Instagram shows a loading spinner for a brief period. Next, it lays out the barebones UI. This is the skeleton screen or Placeholder UI. This indicates the place where content will eventually fill.

Also, notice that the text data has already populated the screen. Finally, in the third screenshot, the images are gradually loaded into place.

Here are some websites that use skeleton screens to show loading.

Skeleton Loading used in Facebook

Look at how Medium handles loading.

Loading seen on Medium.com

You might argue that these websites use Loading Spinners too. But notice how it is used.

**A Spinner alone is not displayed from start to finish!** It is shown only for a brief period, followed by the Skeleton Screen.

**_TIP:_**_If your load time is longer, you can briefly display a Loading Spinner, before Skeleton UI. This should buy your task some more time to complete._

## Progressive Loading for Images

You can even apply gradual progression to image loading. For example, Medium and Google use progressive loading for their images.

Google displays the image’s prominent color first.

Progressive Loading in Google Image Search

Medium handles it a little differently. The website uses an extremely small, pixelated image and blurs it. Later, it loads a higher quality image to replace it, coupled with a nice fade-in animation.

Progressive Image Loading in Medium

I’m sure you’ve seen either one of these. Maybe you didn’t know it had a proper name until now.

Here are the generic steps on progressive loading for images.

1.   Display the skeleton screen
2.   Load a very low quality (pixelated) version of the image (or prominent color)
3.   Load the high-quality image in background
4.   Fade in the high-quality image, replacing the previous low-quality one

Note that you’ve not given then a clear indication of WHEN the task will complete. There is still no solid time estimate. But you have told that what has completed and what remains. That itself is clear sign of progress.

## Skeleton Screens on Android and iOS

You might argue saying most of the skeleton screen examples are websites. So how do I do this on mobile? You’re absolutely right. Reading all this wouldn’t be worth it if I didn’t even give you a hint on how to do this.

### Shimmer by Facebook

Facebook has written a library called Shimmer for both [Android](https://github.com/facebook/shimmer-android) and [iOS](https://github.com/facebook/Shimmer).

It works just like how Facebook uses skeleton UI to load incoming content. The shimmer animation depicts that content is currently loading.

You can use this library to display skeleton screens that denote loading in your apps.

## Handling Failure with Skeleton Screens

There’s no guarantee that a request will always execute successfully. So we cannot assume that if a content loads gradually, it will eventually complete. Chances are, it might fail mid-way. The most common reasons include faulty, slow or no connectivity.

Assume you’ve started a request to load content. Next, the skeleton screen is also displayed. Then suddenly, your internet goes off. How would you handle this?

Typically, you must inform the user and allow them to retry.

> Remember that giving feedback is good interaction design and positive user experience.

**TIP:**

_Consider using ‘_[**_Empty States_**](https://material.io/guidelines/patterns/empty-states.html)_’. It allows you to provide clear feedback with a ‘Call to Action’ (CTA) button._

Empty states occur when an item’s content can’t be shown.

### Connectivity in Android and iOS

Here are a couple of resources that can help you handle connectivity.

**Android**

*   [Use a Snackbar](http://blog.iamsuleiman.com/material-design-snackbar/) to provide feedback with CTA button
*   [Connectivity](https://gist.github.com/emil2k/5130324) — network handling utility class

**iOS — Swift**

*   [iOS Alerts](https://github.com/vsouza/awesome-ios#alerts) — collection of alert libraries to chose from
*   [Reachability](https://github.com/ashleymills/Reachability.swift) — network handling

## Wrapping Up

Apps are getting smart. People are starting to realise that the Loading Spinner is hurting their UX. Hence, it’s about time you did too.

Skeleton screens provide incremental progress in loading your interface. Such incremental feedback gives better user experience and reduces uncertainty. Moreover, people would be willing to wait a bit longer.

So what do you think about Skeleton screens? Is it a viable alternative to a Loading Spinner? Let me know in the comments.

## Related
[Add wiki-links manually or run update_wikilinks.py]