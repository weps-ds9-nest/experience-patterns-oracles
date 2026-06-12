# ![Image 1: Marian Harbach](https://web.dev/images/authors/marianharbach.jpg)

![Image 1: Marian Harbach](https://web.dev/images/authors/marianharbach.jpg)

Marian Harbach

![Image 2: Thomas Steiner](https://web.dev/images/authors/thomassteiner.jpg)

Permission prompts are the web's main mechanism to protect powerful capabilities that are potentially dangerous to users' privacy and security. With permission prompts, browsers aim to ensure that a user intends to let the requesting website access the capability in question. Permission prompts are used for a number of APIs, including media capture (camera and microphone), geolocation, storage access, MIDI, and notifications (see [the Permissions API documentation on MDN](https://developer.mozilla.org/docs/Web/API/Permissions_API#permission-aware_apis) for more information).

This guide outlines the best practices for showing permission prompts to users based on [Chrome usage statistics and user research](https://research.google/pubs/websites-need-your-permission-too-user-sentiment-and-decision-making-on-web-permission-prompts-in-desktop-chrome/). When following these best practices, users should encounter fewer unnecessary prompts, leading to developers getting fewer "block" decisions. The article ends with some code patterns for working with permission-gated APIs, and best practices for helping users to recover from a blocked state.

## Prompting best practices

You should ask for permission after a user interaction, in a moment where users can understand why you are asking, and what benefit they will get from allowing. Where possible, you should allow users to use an alternative means to accomplish the same functionality. As a general guideline, asking for permission less frequently by choosing the moments in which you ask carefully lowers the chances that your users get into a blocked state that is hard to recover from. The following best practices offer more detail on each of these suggestions.

## Never ask on page load or without user interaction

Asking users for permission on page load is equivalent to asking a customer for a sensitive piece of information as they walk into a physical store. Seeing a permission prompt (possibly among several other prompts for newsletter signup and cookie consent) is a very jarring experience. Users won't understand [why they are being asked and how they will benefit](https://web.dev/articles/permissions-best-practices?hl=en#only_ask_when_users_can_understand_why_you_are_asking).

Even if your web application can't work without access to a certain capability, you should give users a chance to understand why it's needed. For example, by prefacing the permission prompt with a prompt of your own that explains the need and gives users a choice (for example, where possible, by [providing alternative means to accomplish the same functionality](https://web.dev/articles/permissions-best-practices?hl=en#provide_alternative_means_to_accomplish_the_same_functionality_where_possible)). If you can't think of a better moment to ask for permission than on page load, there are a few examples later in this guide.

A similarly bad situation to ask for permission is without a prior user interaction (also known as [transient user activation](https://developer.mozilla.org/docs/Web/Security/User_activation)). Chrome telemetry shows that 77% of permission prompts on Desktop Chrome are shown without such a very basic signal of user intent and consequently only 12% of such prompts get allowed. After a user interaction, allow rates increase to 30%. So, only ask for permission after the user has interacted with the page in some form.

## Only ask when users can understand why you are asking

Permission decisions are often privacy decisions. Based on the [contextual integrity framework](https://en.wikipedia.org/wiki/Contextual_integrity), we know that privacy decisions are highly contextual. Understanding why an access is necessary can be considered a key aspect of this. Therefore, you should only request capabilities you need to provide users with value (and where users are likely to agree with you that they will indeed get value). Additionally, you should ask for permission in a moment where it is apparent to the user why the capability is helpful. The aim is to make it as easy as possible for your users to understand the usage context.

Our [user research](https://research.google/pubs/websites-need-your-permission-too-user-sentiment-and-decision-making-on-web-permission-prompts-in-desktop-chrome/) shows that users are substantially more likely to allow access when they understand why a site is asking for access and also perceive a benefit. We also find that users expect to explore unfamiliar sites first to better understand the value they can get in return for allowing access. They will often dismiss or ignore permission prompts in the meantime. With one-time permissions, they might allow for a single visit first. Your application needs to support these behaviors.

## Provide alternative means to accomplish the same functionality where possible

The outcome of some capabilities may not be helpful to users. For example, a geolocation of a desktop device without a GPS sensor may return the wrong location because that person is connected to a VPN. Other users may not want to provide clipboard access because they prefer to stay in control and trigger these events with key combinations manually. In situations like these, it is important to provide an alternative means to accomplish the same outcomes. For example, if requesting geolocation permission, offer a text field where your users can enter a zip code or address themselves. With clipboard, make sure that elements to be copied can also be selected and copied through a key-combination or the context menu. With notifications, offer that people receive emails instead of push notifications.

A useful pattern is to use the alternative UI also as the explanation for why access could be beneficial. Users seeing an option to enter a location next to a button that triggers the geolocation API will feel in control of what is going to happen, because they understand they can also just type in their address. Similarly, if there is a choice between receiving notifications through push or email, or joining a meeting without allowing camera and microphone access, users more naturally understand the tradeoffs they are making.

## Don't get yourself into a blocked state, it is hard to recover from

Once a user has decided to permanently not allow access to a permission-gated capability, browsers honor that decision. If it was possible to keep prompting for access, ill-meaning sites would continue bombarding users with prompts. Therefore, recovering from the blocked state of a capability intentionally takes a bit of effort from the user. Accordingly, avoid asking users for permission in situations where it's likely that many users won't allow access.

A common way to do this is to use a so-called pre-prompt, where you explain to your users what is about to happen and why your application needs the capability you are going to request. Only when users react affirmatively to such a pre-prompt should you trigger the browser's permission prompt. There are situations where users may legitimately need to recover from that state. See the section [Help users recover from a blocked state](https://web.dev/articles/permissions-best-practices?hl=en#help_users_recover_from_a_blocked_state) for more on this.

## Pay attention to third-party content

There is an unexpected source of permission prompts to be aware of. If you include third-party scripts on your site, they may trigger permission prompts that you did not intend to show. This can impact users' experience of your website, especially if such prompts don't follow the best practices already outlined. To stay in control of your users' experiences, you should carefully read the documentation of any third-party libraries and scripts that you add to your own code.

## When to ask for permission

Here are a few examples of moments that work well to ask for permission, following the best practices already described:

*   After a user clicks a button that says "use my location" next to a form field for entering an address manually.
*   After a user subscribed to a video channel or posts, and clicked an affirmative button on a dialog describing that the updates could be delivered as emails or notifications to their phone or desktop.
*   After a user arrives at a page that prepares them to join a video call and answers affirmatively that they want to be seen and heard in a pre-prompt (see this [case study from Google Meet](https://web.dev/case-studies/google-meet-permissions-best-practices)).

## Code patterns for asking for permission

Getting permission to use an API happens through different means, depending on the API. Some (typically older) APIs use a model where the browser automatically asks for permission the first time you try to use the API. One example is the Geolocation API when calling [`navigator.geolocation.getCurrentPosition()`](https://developer.mozilla.org/docs/Web/API/Geolocation/getCurrentPosition).

```
try {
  navigator.geolocation.getCurrentPosition((pos) => console.log(pos));
} catch (error) {
  console.error(error);
}
```

Other APIs use a model where you explicitly need to request permission first using a static method. A good example is [`Notification.requestPermission()`](https://developer.mozilla.org/docs/Web/API/Notification/requestPermission_static) for allowing notifications, or the less common [`DeviceOrientationEvent.requestPermission()`](https://developer.mozilla.org/docs/Web/API/DeviceOrientationEvent), which is part of the Device Orientation Events API. Note that some browsers may automatically grant permission to given APIs. For example, Chrome always allows access to a device's orientation, whereas Safari shows a prompt.

```
const result = await DeviceOrientationEvent.requestPermission();
console.log(`The user's decision when prompted to use the Device Orientation
Events API was: ${result}.`);
if (result === 'granted') {
  /* Use the API. */
}
```

## How to check the state of permissions

To check if you can use a certain API, use the [`navigator.permissions.query()`](https://developer.mozilla.org/docs/Web/API/Permissions/query) method from the Permissions API.

```
const result = await navigator.permissions.query({ name: 'geolocation' });
console.log(`The result of querying for the Geolocation API is:
${result.state}.`);
if (result.state === 'granted') {
  // Use the API.
}
```

## Help users recover from a blocked state

To help users troubleshoot access problems, detect that they blocked access using the Permissions API and offer them a guide on how to change their settings. For example, when users interact with UI elements that are associated with a permissions-gated capability, use the pattern described in the previous section and open a troubleshooting dialog. The exact steps to change permission state vary by browser, so you might want to offer matching descriptions based on the user agent string and for the most commonly used browsers in your product.

In Chrome, users should go to **Site Controls** by clicking the "tune" icon on the left-hand side of the address bar. Here, they can toggle the respective permission on. In some cases, they may have to reload the page, before using the capability. In that case, a message bar will show across the top of the window that offers to reload when clicking the respective button.

![Image 3: Site controls in the Chrome browser.](https://web.dev/static/articles/permissions-best-practices/webdevwebpermi--amzfrutpcya.png)

![Image 4: A reload prompt after changing permissions using site controls.](https://web.dev/static/articles/permissions-best-practices/webdevwebpermi--rfxeicfrxoa.png)

Similar UIs for controlling permissions exist in other browsers (for example, [see how this works in Firefox](https://support.mozilla.org/en-US/kb/site-permissions-panel)).

## Related
[Add wiki-links manually or run update_wikilinks.py]