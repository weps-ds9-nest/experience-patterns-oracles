# First of all, speed matters for most users. There are definitely users that don’t notice the difference between native desktop software (I don’t count all those [Electron](https://electron.atom.io/) -based desktop versions of online software) and their online counterparts, but, typically, most users prefer native versions for frequently used software. Spreadsheets, image editors, big text processing — all these tasks can be completed much faster using native software. At the same time, online [software](https://hackernoon.com/tagged/software) is the [future](https://hackernoon.com/tagged/future) for most tasks due to its wonderful multi-platform and collaboration possibilities. Thus, making it faster is one of the main objectives in order to make users happier.

First of all, speed matters for most users. There are definitely users that don’t notice the difference between native desktop software (I don’t count all those [Electron](https://electron.atom.io/) -based desktop versions of online software) and their online counterparts, but, typically, most users prefer native versions for frequently used software. Spreadsheets, image editors, big text processing — all these tasks can be completed much faster using native software. At the same time, online [software](https://hackernoon.com/tagged/software) is the [future](https://hackernoon.com/tagged/future) for most tasks due to its wonderful multi-platform and collaboration possibilities. Thus, making it faster is one of the main objectives in order to make users happier.

We can bring online software user interface responsiveness closer to compiled ones using well-known tricks. One of these tricks is to fire event execution as soon as a user pushes the left mouse button (before releasing it), or taps a mobile (before removing his/her finger). I often wonder why using the onMouseDown event, for many controls in user interfaces, is so rare in web interfaces. It is obviously not an unknown property and is used in many places. For example, MS Office uses the onMouseDown event for switching menu tabs and all dropdowns — but still uses click event for any buttons:

Mozilla Thunderbird uses the onMouseDown event for message lists; Chrome and Firefox for switching tabs; and Firefox for preferences tabs:

It is the same for every tab in the [Directory Opus](https://www.gpsoft.com.au/) file manager:

Interesting, that Google online spreadsheet software supports the onMouseDown event for many operations as well. For example, for all dropdowns and tabs switching.

And many other desktop software applications use this feature.

Check if you see any speed differences [in this sample](https://artemsyzonenko.github.io/click-vs-mousedown/home.html):

onMouseDown vs onClick

You can test your average saved time here: [http://instantclick.io/click-test](http://instantclick.io/click-test), “Click - Mousedown” value.

According to Robert Miller, “ [Response time in man-computer conversational transactions](http://theixdlibrary.com/pdf/Miller1968.pdf),” study and Card, S. K., Robertson, G. G., and Mackinlay, J. D. “ [The information visualizer: An information workspace](http://www2.parc.com/istl/groups/uir/publications/items/UIR-1991-01-Card-CHI91-IV.pdf),” and others, a response time of 100 ms is perceived as instantaneous. So when you use the click event, you can barely get an instantaneous interface, even for preloaded content. When you need to get some content with AJAX, you will need to add an additional 50–500 ms delay. Which all means you may get “fast” interface response in the best case, but it won’t be instantaneous.

You should definitely, avoid any onMouseDown events if the onDrag event is in use as firing onMouseDown at the same time is not desirable. For example, for blocks that target some other screen, but you don’t want to switch the user to another screen when drag-n-drop is all the user may need.

Moreover, if a dragging event may follow the onMouseDown event, it, too, is not a problem. You can check any Google Sheets document and how sheet dragging works: onMouseDown + onDrag works without any breaks. Selected sheet activates and then drags.

So, if you want to improve your web application performance, think about using onMouseDown event. It can speed up every user action by about 100 ms, without any big effort from your side.

Take your TV remote control and test if it is actuated by pushing (onMouseDown) any button, or by pushing and releasing (onClick). I am sure you will find it is just pushing.

Be cautious with touch screens as onMouseDown will prevent scrolling, so it should be applied to small elements only. Better do not implement these events for touch devices at all. Similar problem with keyboard accessibility, as it is not possible to fire onMouseDown action using keyboard using Space or Enter key. It may be just couple of your website users, but anyway, you need to know about this issue (thanks Oliver!). You may deal with this case using [onkeydown](https://www.w3.org/WAI/GL/WCAG20/WD-WCAG20-TECHS-20071102/SCR20.html) JS event handling.

## Related
[Add wiki-links manually or run update_wikilinks.py]