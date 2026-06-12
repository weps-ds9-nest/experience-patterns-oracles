# App Login Design Choosing The Right User Login Option For Your App

### Weighing up the app login design options

When deciding on your app’s login method, choosing between security and user convenience is somewhat of a balancing act. User data is of utmost importance, but protect it too zealously with Byzantine login methods, and you risk alienating users. However, defend it too weakly in a bid to drive up user retention, and you risk losing data, trust, and credibility.

There are a host of login methods for developers to choose from. Each comes with its own pros and cons. Below we list the most common and best practice login options and weigh up their relative merits.

### Password login

Password Authentication is still the most commonly used security method. It’s simple, familiar, and convenient. Users sign up with an email or username — or both — and provide a password when they need access to the platform.

**Pros:**

The beauty of a password login lies in its simplicity. A user can lay claim to an identity (username or email) and validate this by demonstrating knowledge of the password associated with that identity on an app’s server.

![Image 1](https://uxmag.com/wp-content/uploads/2021/06/Applogindesign1-1024x512.jpeg)

Smiling Mind app account registration

Another plus comes through signing up. Generally, users must provide a valid email from which they click a confirmation link. Some may see this as an extra barrier to entry, but this gives developers a confirmed email address. Developers can use this as a marketing lead for paid services and future offers. With email service providers becoming more aggressive in filtering spam, requiring a user to open and act on an email will also help you on the whitelist.

**Cons:**

One of the drawbacks of this app login design method is that it places specific demands on its memory. Users must walk the line between a password being easy to recall but not so weak that it can be cracked or guessed. A secure, uncrackable password might take the form of a long stream of numbers, randomly capitalized letters, and perhaps symbols. These are not recallable for most people.

As a result, users frequently forget their supposedly memorable piece of information. An app or service must then have a mechanism in place that can deal with both forgotten and compromised passwords. This leads to additional development effort and maintenance.

Because of the difficulties outlined above, users frequently use password managers and check the options that allow them to stay logged in. These are a conscious step toward a more seamless user experience. However, should a device fall into the wrong hands, the password mechanism as a piece of knowledge being known only to the user becomes entirely invalid.

Another issue caused by “password fatigue” is that users habitually employ the same password for various apps/sites. With data breaches and hacks commonplace, a reliance on email and password authentication means your security can only be as good as the security of the other platforms your users hold accounts with.

### Social login and third-party login

Social media logins use the credentials contained on a user’s social media account to register or log in to third-party apps and platforms. As a login method, this can prove to be a convenient alternative for both users and developers. This is because it offers streamlined ways to register users that don’t require filling in forms or accessing emails to verify credentials.

![Image 2](https://uxmag.com/wp-content/uploads/2021/06/Applogindesign2-1024x512.jpeg)

Hubspot mobile app login design UX (Click image to enlarge)

**Pros:**

The lack of friction involved in a 1-click sign-in translates into higher signups and conversions. This is a huge benefit and arguably the biggest reason for its growth in popularity. Additionally, users are grateful for having one less password to memorize. Logging in via a familiar social media platform can also feel more secure.

For developers, logins through third parties provide access to a trove of data — conditional on app permissions. User preferences, interests, friends, and online behaviors are excellent sources of data. Depending on their business model, developers can leverage this rich data for market research or targeted advertising.

The application programming interfaces (API) required to access platforms like Facebook, Google, Apple, or LinkedIn are mainly free. Some charge based on how much data is needed. Another plus is that social login is very mobile-friendly and is perfect for the world of touch screen media devices.

**Cons:**

But with big data comes big responsibilities. Using social logins obliges developers to comply with[GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)responsibilities. They must also familiarise themselves with the specific practices of each third party. On a similar note, relying solely on social or third-party logins may alienate your app from the ever-growing body of people who don’t use social media due to trust issues.

Relying on third parties also poses a security risk. Social media giants have had their share of data breaches over the years. So, social logins end up having many of the same issues identified with traditional email & password logins.

Other potential drawbacks to consider are that many business or college networks block access to social media. Over-reliance on these methods means your functionality depends on theirs. So any downtime on their service — or network restrictions imposed by other organizations — locks your users out of your platform.

Something for developers to be aware of is that Apple’s third-party IOS app sign-in option — Sign In with Apple — is mandatory for apps on the Apple Store under certain conditions. Any app with Facebook, Google, or any other social sign-in options must also offer Apple sign-in to be eligible for sale in the Apple Store.

**Social login vs. registration**

Comparing the two in a nutshell:

*   Quicker and simpler for users than email registration and login
*   Increased signup conversion
*   Simplified account registration UX
*   Potential GDPR compliance obligations
*   Reliance on third-party technology
*   Fewer user email addresses for marketing purposes

## Mobile number login

The preferred method of companies like Uber, Lyft, and WhatsApp, mobile login makes sense in a world gone mobile. It’s a simple and effective way to quickly authenticate users without the need for lengthy sign-up or login forms.

![Image 3](https://uxmag.com/wp-content/uploads/2021/06/Applogindesign3-1024x512.jpeg)

Uber login UX

**Pros:**

Mobile number login has a distinct advantage over email & password because a phone tends to be a much more unique identifier. Users can — and do — set up multiple email addresses, but a login that requires a verified phone number is more difficult, but not impossible, to abuse.

One of the biggest advantages is that mobile number login doesn’t require the user to remember a password. So long as they can receive an SMS, they’ll always be able to log in.

If geolocation details are essential to the functioning of your app, a mobile phone login is a handy option.

**Cons:**

Phone numbers change. People leave jobs, industries, or countries and change their digits. If this is the sole login method, migrating accounts becomes more complicated than it needs to be. An email address or social media account are more permanent fixtures that users tend to keep despite changes in circumstance.

For these reasons, mobile login is most likely to find the best use as a secondary or additional security option. But it’s not exactly airtight. One issue with mobile login is that occasionally hackers have been able to breach this security layer by forwarding the service to another phone and intercepting SMS messages to gain access to accounts.

## Multi-factor authentication

Multi-factor authentication (MFA) requires more than one distinct login method for successful access. Most typically, this comes in the form of two-factor authentication, also known as 2FA. An example of 2FA is where a user logs in to a platform with an email address and must cross-verify the identity with a code sent to a second device like a mobile phone.

![Image 4](https://uxmag.com/wp-content/uploads/2021/06/Applogindesign4-1024x512.jpeg)

Multi-factor authorization flow

**Pros:**

MFA’s main strength is security. The second layer of security provides protection against weak or compromised passwords, with additional safeguarding in the event of a lost device.

Depending on the market you wish to cater to, MFA compliance might fall under the EU’s[Payment Services Directive 2](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32015L2366)(PSD2) for the UK and European companies. Article 4 (30) mandates Strong Customer Authentication (SCA) by December 2020 for e-commerce merchants.

This has led to the adoption of various MFA methods, such as a link or temporary PIN being sent by SMS or push notifications alerting users of account activity. Third-party authenticator apps can also be used to provide temporary passwords or QR codes that grant access to platforms.

Other MFA that are available are retina, biometrics, or fingerprint; however, the cost of these methods is considered prohibitive by some.

**Cons:**

Often, MFA requires a second device. This can pose a problem for some users if they are locked out due to a lost, misplaced, or broken device.

User experience can become more complicated due to the additional factors of MFA. On top of the extra time and steps involved with this login method, recovery is conditional on the second identity provider. However, should a user forget or lose access to this second identity provider, they may lose access to the platform altogether in the case of an attack or suspicious activity.

There are vulnerabilities to be considered with MFA in regards to the second identity layer. Devices, hardware tokens can be stolen along with other hacks that replicate factors like voice, eyes, and fingerprints. For more challenging security, rotating several different factors is recommended.

While MFA does provide an extra layer of protection, as commonly implemented, it’s not a foolproof solution.

### How to design a signup page UX

There is an infinite number of ways to design an app account registration and signup page. However, most apps tend to stick to a few common logins and register UI standards. Here are some things to consider when designing your app login screen:

**An email with password login and registration UX**

*   Ask the user to confirm their password (type it twice) to reduce the possibility of typos.
*   Remember to ask the user to agree to your terms and conditions
*   Don’t forget a password recovery/reset feature
*   Break long registration/sign up forms up in multiple steps
*   Instead of requiring the user to remember a password, you could simply send them a single-use login link via email every time they need to login
*   Allow space for the keyboard, ideally without having to move things around on the screen to accommodate it
*   Don’t ask for any user information you don’t absolutely need. The more fields you include, the lower the likelihood of completion

![Image 5](https://uxmag.com/wp-content/uploads/2021/06/Applogindesign5-1024x512.jpeg)

Puntshare app account registration

**Social and third-party login UX**

*   Stick to the basics like Facebook, Google, and Apple. Enabling a ton of obscure options will cost more than it’s worth initially.
*   Make sure login truly is just one click (plus social network login if required). Enabling social login is all about reducing barriers to entry and increasing conversion.
*   Make sure to automatically take the user to social login if they try to login via email instead of using a social login email address.
*   When using third-party login options, it’s extra important to keep the app up to date with the latest versions of third-party login SDKs.

**Mobile login and registration UX**

*   Make sure the user can resend the PIN code SMS if they don’t receive it
*   When the user enters the last digit of their PIN, you can automatically validate the PIN without requiring the user to tap a ‘next’ or ‘continue’ button.
*   Ensure you handle country codes and mobile number formatting gracefully so the user isn’t left guessing how they should enter their phone number.

![Image 6](https://uxmag.com/wp-content/uploads/2021/06/Applogindesign6-1024x512.jpeg)

Snackr app login design ux

**Multi-factor login and registration UX**

*   Make sure the login complexity is proportionate to the security requirements of the app. Requiring PIN, mobile number, fingerprint, and third-party app authentication just to log into a note-taking app is overkill, and users won’t tolerate it.
*   Provide recovery options for users that switch phone numbers or forget PINs etc.

Choosing the right app login method is dependent on several factors particular to your niche and what user information you plan to hold or use. Tighter security can lead to a more complicated user experience. Still, with compliance legislation for all payment processing required, some combination of the above methods is likely to become very familiar to most users.

[![Image 7](https://uxmag.com/wp-content/uploads/2020/02/02book-1024x536.jpg)](https://invisiblemachines.ai/?utm_source=uxmag&utm_medium=referral&utm_campaign=article_applogindesign:choosingtherightuserloginoptionforyourapp&utm_content=ad2)

## Related
[Add wiki-links manually or run update_wikilinks.py]