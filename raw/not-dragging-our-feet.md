Title: Article from medium.com

URL Source: https://smry.ai/https:/medium.com/carbondesign/not-dragging-our-feet-a03ea57150e

Markdown Content:
Illustration of hand dragging an object

## Tackling future accessibility considerations in today’s designs

Not that long ago, accessibility issues were raised during testing or at best tackled during development. Two years ago, IBM Accessibility started a ‘shift left’ campaign to reposition accessibility considerations earlier in the software development cycle. These days, that strategy has been taken on fully by IBM Design.

During a recent design playback on range selection in a complex data chart, I brought up the idea of eliminating a reliance on dragging — which will likely become a future requirement in version 2.2 of the Web Content Accessibility Guidelines (WCAG).

## Dragging movements

[2.5.7 Dragging Movements](https://w3c.github.io/wcag/understanding/dragging-movements.html) basically says you can’t use dragging as the only way to operate a pointer. A control must also be usable with simpler pointer actions, such as mouse clicks (Figure 1). Who benefits most? Users with decreased fine motor skills, who may have challenges with press-and-hold actions, especially in combination with mousing precision.

Figure 1. Dragging an object is still fine, but offer ways for users to do the same thing with simple pointer interactions, like moving an object by clicking a button

WCAG 2.2 is unlikely to become a standard this year, and then won’t be fully adopted by IBM for some time after that. Yet the attitude on a recent playback was that if the user need is known, it made sense to consider now as a good design principle. After years of struggling to get _current_ requirements properly assessed, that willingness to look to the future felt like a real game changer.

## Dragging in a selection bar

So, what exactly is a range selection bar and what are the dragging interaction considerations? The range selector is basically an enhanced slider. Instead of one thumb slider, it has two that allow a user to define a segment of data from anywhere along a range, such as a few days in the middle of a one-month time bar (Figure 2).

Figure 2. Simplified range bar, showing thumb controls being used to display only a portion of the entire data set

In a traditional single thumb slider (Figure 3), the user positions the pointer on the control and drags to the desired value.The alternative to dragging is to allow the user to click anywhere in the slider’s range and reposition to that click point. It’s a common part of many implementations. You can use this [ARIA example](https://www.w3.org/WAI/ARIA/apg/example-index/slider/slider-seek.html) to try the basic interaction.

Figure 3. Volume slider with a range from 0 to 100 and the thumb slider currently positioned on 18

Another form of simplified activation of a thumb slider is to add input steppers, typically two buttons at the ends, which allow the value to be adjusted by single clicks.

With two thumb sliders, how could steppers work? IBM’s open-source design system, Carbon, already has such a [zoom mechanism for a timeline](https://carbon-design-system.github.io/carbon-charts/?path=%2Fstory%2Futility-toolbar--vertical-stacked-bar-time-series) (Figure 4).

Figure 4. Zoom bar, showing + (increase) and – (decrease) zoom buttons that, when clicked, adjust both thumb sliders in concert

It’s a fairly elegant implementation. A shortcoming is that both thumb slider’s range limits are affected by the stepper change. There is no ability to step them individually. You could achieve independence by allowing one slider control to be selected, and then step just its value. But that potentially adds more user effort, so how valuable is stepping in a large data set? [Neilsen Norman Group writes](https://www.nngroup.com/articles/input-steppers/) not to use such controls for a wide range of values “with no one value being entered significantly more often.” IBM is designing broadly for varied data sets, so we set steppers aside as suboptimal.

## Solution: a clickable slider bar

After discussion, the team opted to try a range bar, clickable across its length, with a proximity heuristic. Whichever control is closer to the click point would orient to that location. When the click is outside the current selection range, it’s obvious which slider is going to expand. But what if the user clicks roughly equidistant between the control? Or what if the two controls were very close together? The heuristic should still work.

Figure 5. Animation showing thumb sliders responding to clicks on the slider bar

With near-equidistant clicks, it will bring the _closer_ slider to the click location. Where the controls are overlapping, the click can still reposition the nearer control. Where the controls are on the same point, or the click occurs precisely halfway between, which control is moved is a moot point. One of the controls moves. The other remains in its prior location, and can then be adjusted as necessary.

## Other range considerations

The team also discussed the ability to enter in values manually where precision is needed, something already offered in [Carbon’s slider component](https://www.carbondesignsystem.com/components/slider/usage/) (Figure 3). Numeric text inputs at each end can provide this — although it’s a somewhat inelegant visual solution and the inputs lack visible labels (Figure 6). One additional benefit of inputs: they allow for the display of the values. The click not only repositions the control but updates the input numbers.

Figure 6. Lo-fi concept of a range selector bar with (unlabelled) inputs at each end, allowing for manual entry of precise starting and end values for a range (in this case degrees Celsius)

Speaking of displaying values, Diana Stanciulescu, the designer focusing on these data visualizations, had _already_ led the call through discussions on labelling, including exposing both the terminal ranges and the selection values. IBM Design is trying to use persistently displayed values where it makes sense (instead of relying on hover, with its accompanying accessibility challenges). After discussion, she began to explore placing the values for controls above their location (Figure 7), since pointers or users’ fingers are likely to obscure values located underneath the control.

Figure 7. A temperature range bar, with starting and end values as well as current selection values displayed

Finally, another designer on the playback mentioned putting the thumb controls in the tab order so there is a _keyboard_ method for the slider. This is an important established pattern which can offer the ability for a keyboard user to change the values, often incrementing steps by scales of 10 (see the [ARIA example](https://www.w3.org/TR/wai-aria-practices-1.2/examples/slider/slider-1.html)). It should be simple to adopt this on a multi-thumb slider. However, it’s important to emphasize that this doesn’t replace these future needs for better _pointer_ interaction, the focus of our discussion.

I’m sure Diana will iterate this zoom bar to an even better interaction. I’m just as sure that designers are much better positioned to deal with nuances of interaction than a developer under the gun to get an implementation out the door. It’s another example of how accessibility doesn’t need to (ahem) drag down good design.

Illustration of hand dragging an object

_First dragging iIllustration by_[_Jess Lin_](https://medium.com/@hiraeth_)_; all others by_[_Diana Stanciulescu_](https://www.linkedin.com/in/d-stanciulescu)_, who also provided article input._
