# “Instagram would like access to your photos.”

“Instagram would like access to your photos.”

“Uber would like to use your location.”

“Stitcher would like to send you notifications.”

We’ve all seen these sentences, or ones like them, on the mobile apps we’ve downloaded. It’s common for both Android and iOS applications to request device permissions when a user first installs an app and completes the onboarding process (that is, registers and completes tutorials).

However, most of us have also experienced an app asking for information out of nowhere, or barraging us with requests that seem irrelevant. That lack of explanation causes mistrust; in other words, it’s bad UX. Trust and comfort are crucial emotions for new users.

If you’re a UX/UI designer or app developer, you can’t afford to neglect permission priming, or placing permissions requests in a logical context. A new [study by B2B research company Clutch](https://clutch.co/app-developers/resources/mobile-app-onboarding-survey-2017) shows that 82% of respondents find it somewhat to very important that they know _why_ an app is asking for certain information (such as device permissions, a credit card number, or personal details). That’s over 4 out of 5 mobile app users.

Bafflingly, plenty of popular apps crash and burn when it comes to permission priming. Lucky for us, we can learn from the mistakes of apps like YouTube and Starbucks. We can also emulate the successes of Bitmoji and Duolingo.

Let’s go through some of the worst and best examples of permission priming habits, shall we?

## Hall of Shame

YouTube commits the cardinal sin of asking for total phone access without a word of explanation, while Starbucks doesn’t give users a single peek at the menu before they grant notification permission and hand over personal detail after detail.

### YouTube Update: Unnecessary Permissions Extravaganza

In April of 2017, YouTube released an update for the Android version of its mobile app. When Android users downloaded that update, they were confronted with the following request:

Source: Imgur

Not only did YouTube ask for far too many permissions, it didn’t prepare users by telling them why the app needed access to so much information. These decisions left some people distrustful of the video app — after all, why did it need SMS and contact data?

YouTube eventually had to post a statement on the Google/Android support site that described why they wanted access to each function.

Source: YouTube/Google Support

App companies know they’ve made a mistake if something like app permissions is so unclear that the company must write an explanation on their website. The YouTube developers could have executed their request for all these phone functions in a much savvier way.

First, the developers should have only asked for the permissions they absolutely needed during onboarding. If a user isn’t recording videos as they get onboarded, for example, then there’s no need to let YouTube use their microphone right away. Should they decide to use the microphone later, YouTube can ask then.

Second, why the lack of context? The reason why YouTube wants in on users’ SMS information makes sense…but YouTube didn’t provide those reasons during update onboarding. If the app had a pop-up explaining the request before the app made users grant (or not grant) permission, it’s likely that more people would have trusted YouTube.

In fact, the [Android Developer guidelines](https://developer.android.com/training/permissions/requesting.html) suggest that apps which ask for ‘dangerous’ permissions (microphone, camera, calendar, etc.) prep users first.

Source: Android Developers

Next time, YouTube should take a leaf out of Android’s book. After all, the company distributes its app on Android devices!

### Starbucks: Provide Every Piece of Personal Information You Have

You may have heard about the [bottlenecking created by the Starbucks app](https://clutch.co/app-development/resources/why-starbucks-preorder-app-caused-long-lines): baristas get overwhelmed dealing with mobile orders, so app users have to wait despite ordering ahead. That’s bad UX right there, but the app onboarding experience has issues, too. It’s both brusque and nosy (why do people love this app?).

Right out of the gate, Starbucks hits users with an un-contextualized permission request.

Uncontextualized push requests are common, but that doesn’t make them any less annoying. A new user doesn’t know the first thing about how this app works, so they have no incentive to say yes.

## Get Elizabeth Ballou’s stories in your inbox

Join Medium for free to get updates from this writer.

No matter what people choose, Starbucks then hits users with a wall of form blanks. It wants their full name, their email address, their zip code, their first-born child, etc.

Then Starbucks asks for their credit card number. Users haven’t even seen the menu yet! This is an awful lot of sensitive information just to get inside the app.

In the end, the app’s appeal comes down to a single factor: name recognition. Starbucks expects people to give away their permissions and personal details because they know and trust its brand. If a new user isn’t a diehard fan, though, why would they be so open?

To avoid Starbucks’ mistake, let users ease into your app before asking for anything. If your mobile app requires financial details, at least wait until users have placed an item in the shopping cart.

## Hall of Fame

Both Bitmoji and Duolingo have breezy, gamified onboarding processes that ask for a minimal level of system and user information. When the apps do ask, they make saying yes into the logical choice.

### Bitmoji: When the Aesthetic Matches the Onboarding

Bitmoji’s not just adorable, it’s a joy to use. The app allows users to create a cartoon version of themselves, which can then be used as emojis in Snapchats and texts.

What takes Bitmoji from novel to genius, though, is the way it seamlessly merges its style with the onboarding process. For starters, the app doesn’t ask for any permissions when users open it. Instead, they dive straight into bitmoji creation, picking out eye color and outfits.

Once new users are finished, Bitmoji wants to know if it can connect to Snapchat, which is the app’s main appeal.

Not only does Bitmoji wait until the end, when people are emotionally invested in the mini-me they’ve just created, the app includes a cute graphic of the creation’s face with a cartoonish question mark hovering over its head. Who would say no to that?

Once users grant access to Snapchat, they can wallpaper Snaps with their own personalized emoji. The onboarding process is simple, interactive, and friendly.

### Duolingo: Giving, not Taking, Information

Duolingo, an app that helps users learn a new language, is another example of permission priming (and onboarding overall) done excellently. Duolingo invites its new users to try the app’s main function before giving it any information at all. By the time Duolingo asks a user to register an account and grant (scant) permissions, they’re already invested in the service Duolingo can give them.

First, a new user picks a language they want to learn out of a list. Once they’ve chosen, they complete a short lesson on language basics.

I chose Irish, and by the time I finished the introductory lesson, I could say simple phrases like “I am a woman” and “the girl and the boy.” Cool, right?

Each question requires the user to build on a vocabulary word or sentence construction they just learned, and Duolingo automatically reads the correct pronunciation aloud if headphones are plugged in. Still no permissions requests.

Only after the user is done does Duolingo ask them to make an account and grant push notification permissions.

An cailín!

The app is clear about why, too: users have to practice their language every day for the lessons to stick. Not only does Duolingo show people its value right out of the gate, it only sends notifications for users’ own good. Hard to beat permission priming that solid!

## To Prime or Not to Prime? The Answer is Clear

As you’re building wireframes or code for your own mobile apps, think about the information you’ll have to ask your users to turn over. Do you really need access to every phone function? For those you know are necessary, what is the least intimidating way to ask users?

A 2016 study by Localytics says that [23% of app users quit an app](http://info.localytics.com/blog/23-of-users-abandon-an-app-after-one-use) after only opening it once. That’s nearly a quarter, and there’s no reason to increase your chances of users abandoning all your hard work because you neglected to explain a permissions request.

Once you make permission priming part of your app creation routine, however, working your permissions requests into the UX of your app will become second nature.

Consider the definition of user experience: it’s “how you feel about every interaction you have with what’s in front of you in the moment you’re using it,” according to [User Testing](https://www.usertesting.com/blog/2015/08/13/what-is-user-experience/). Ultimately, you want your users to feel comfortable and entertained — and permission priming can help you accomplish that.

## Related
[Add wiki-links manually or run update_wikilinks.py]