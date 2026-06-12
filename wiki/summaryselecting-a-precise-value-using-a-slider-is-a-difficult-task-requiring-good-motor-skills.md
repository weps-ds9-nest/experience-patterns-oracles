# Summary:Selecting a precise value using a slider is a difficult task requiring good motor skills, even if the slider is well designed. If picking an exact value is important to the goal of the interface, choose an alternate UI element.

Summary:Selecting a precise value using a slider is a difficult task requiring good motor skills, even if the slider is well designed. If picking an exact value is important to the goal of the interface, choose an alternate UI element.

Sliders are often the UI control of choice for letting users select a value or range from a fixed set of options. However, in practice, **sliders are difficult to manipulate**. Especially on touch interfaces, the level of control needed to meticulously operate a slider to an exact value is simply not realistic.

> **Slider:**A control element that uses a knob or lever moved horizontally to control a variable, such as volume on a radio or brightness on a screen.

*   [Imprecise Interactions](https://www.nngroup.com/articles/gui-slider-controls/#toc-imprecise-interactions-1)
*   [Is an Exact Value Necessary?](https://www.nngroup.com/articles/gui-slider-controls/#toc-is-an-exact-value-necessary-2)
*   [Think About the Thumb](https://www.nngroup.com/articles/gui-slider-controls/#toc-think-about-the-thumb-3)
*   [Conclusion](https://www.nngroup.com/articles/gui-slider-controls/#toc-conclusion-4)

## Imprecise Interactions

When designing a usable UI we must consider the context in which the interface will be used. For mobile design in particular, users often hold their device in one hand while doing other activities—watching television, walking, or even driving. In such circumstances it can be daunting to tap and drag a control precisely to a particular spot. Sliders are subjected to the **steering law**, which describes the time needed to navigate through a tunnel—as you might guess, the longer and narrower the tunnel, the more time it takes to steer through it. (The steering law also applies to drop-down menus and [horizontal scrollbars](https://www.nngroup.com/articles/horizontal-scrolling/).) With mobile devices being, well, mobile, it is not surprising that we see many users accidentally nudge the slider off the value they were attempting to select _just_ as they lift their finger off the screen.

![Image 1: Screenshot of Kayak iOS app filters](https://s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/multiplesliders.png)

_The Kayak app uses multiple sliders for filtering based on the time of flights. The_ Depart _and_ Arrive _sliders only allow whole hour values, but the_ Duration _sliders force users to select a value down to the precise minute._

Another major consideration when designing a touch interface is the [accessibility](https://www.nngroup.com/topic/accessibility/) of various UI elements. Think about how challenging it would be to interact with a slider control for users with motor difficulties. Would they be able to select a value even close to what they wanted? How much effort and how many tries would it take them? Many [older users have less steady hands](https://www.nngroup.com/articles/usability-for-senior-citizens/) than younger users and would have similar difficulties performing precise gestures to manipulate small UI elements. Unless you want to render these users helpless, a slider control may not be the best choice.

## Is an Exact Value Necessary?

Allowing the selection of a very specific value is often not necessary, nor very helpful, to the user.

Sliders work **best when the specific value does not matter** to the user, but an approximate value is good enough. Thus, Kayak may get away with using sliders for duration and arrival and departure hours, as most users will be fine with a departure time that is, say, midday, and won’t care to specify the exact moment of the departure. But whenever the exact value matters, sliders are not okay. For instance, if you had to enter quantities such as age or current weight or height within a form, a slider would not be appropriate.

**The wider or the denser the range selectable through a slider, the harder it is to select a precise value**. The _Delectable_ app asks users to rate wine on a 6-10 scale, accurate to a tenth of a point. Not only is the abnormal scale is confusing, but selecting the precise value (9.5 vs. 9.3, for instance) is quite a motor feat. One could perhaps argue that the user won’t mind rating the wine a 9.3 instead of a 9.5, since the values are in the same ballpark. But then, why bother with the tenths of a rating and not use a simpler 5-point scale instead?

![Image 2: Screenshots of product rating elements on Delectable iOS app and Amazon iOS app](https://s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/ratingslidervsstars.png)

_Left: The Delectable app uses a slider for assigning a very specific rating to a bottle of wine. Right: Amazon app uses the more common, and easier to select, tappable stars to assign a rating for a product._

![Image 3: Screenshot of Weightbot iOS app slider](https://s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/toopreciseslider.png)

_Weightbot, a weight-tracking app, commits a double error: (1) it uses a slider (that is an imprecise control) for something that needs to be indicated with precision (weight) and (1) the slider moves in very small increments (.1 lb). Plus, the value it starts with is random: if you weigh 120 or 210 lbs, good luck adjusting the slider!_

## Think About the Thumb

In cases where the use of a slider may be appropriate, ensure that the visual design of the element does not hinder its usability. For touchscreens, consider where the user’s finger will be placed on the screen—and what areas of the screen will thus be covered—while manipulating the slider. While labels placed directly below the slider may work on desktop designs used with a mouse cursor, the same label placement does not work well for mobile devices and other touchscreen designs because the labels may be obscured by the users’ finger while they are interacting with the control.

![Image 4: Screenshots of filters on BrilliantEarth.com and AirBnB.com](https://s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/sliderthumbs.png)

_Left: The sliders on BrilliantEarth.com place the labels describing the slider increments below the slider track, where they will be obscured by the user’s thumb during the interaction. Right: AirBnB.com correctly displays the slider values above the UI element, so they would remain visible throughout use._

In order to remain visible during use, any labels describing the slider or its currently selected value must appear beside or above both thumbs involved: the thumb of the user, and the thumb of the slider (also known as the knob or elevator).

## Conclusion

Use a slider only when the precise value won’t matter to the user, but rather only the approximate range. Make sure that the users can select that range correctly without having to struggle too much to hit a precise value. In addition, any slider labels must be displayed above or beside the slider, rather than below it, in order to remain visible while the user is selecting a value. Alternatively, consider a different UI element that allows users to tap or even type to specify their choice rather than relying on press-and-drag gestures.

## Related
[Add wiki-links manually or run update_wikilinks.py]