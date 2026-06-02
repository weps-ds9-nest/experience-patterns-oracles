Title: Article from haroldajagu.medium.com

URL Source: https://smry.ai/https:/haroldajagu.medium.com/designing-better-dashboards-e9e65e8f59f4

Markdown Content:
Photo by Luke Chesser on Unsplash

So you just got a brief to design another dashboard for some operational process in the business. You skim through the requirements, and they all seem a bit abstract, yet you can find some meaning to it (at least) but it just seems like “a lot”.

You’ve definitely designed some dashboards in the past, but then, you knew it wasn’t all that. It just basically showed — Active Users, Deactivated users and a few other datasets that were most of the time static and not fed any real-time data. But here you have multiple sets of requirements all pointing towards different channels, and different sections of the business operations. Numerous values that all need attention, and needs to be shown to the user.

Scenarios like this are quite common and are often times why designing dashboards can be like an extreme sport! (at least in product design)

So, I’ll be going over some good practices and key principles that can help with guidance when coming up with dashboards.

### Design for Scale

Learnt this a while back during my first rodeo in proper dashboard designs. It was a phrase my boss would always use and constantly reference during our design review sessions.

Now you would ask, what is actually “designing for scale”? This basically means treating the dashboard as an organic matter (in very simple terms). Given that, the volume of data and information that will be available for exploration on a dashboard will only get bigger and keep growing. Datasets, items, functions, entries will only increase as time goes on.

Knowing this, it is imperative that when designing the user interface, we have to keep this in mind, as this will not only influence our design choices, but will visibly affect the approach we will take in coming up with the overall design for our project. For example;

_Use Case (From a Drive-to-purchase startup) — “On the existing dashboard, the business needs to know all the drivers that have issues with their contracts so that the analyst can take a required action”_

Fig 1 — Drivers’ Overview Dashboard

From the image above, I could easily create another filter that shows — good standing contracts and troubled contracts. Or I could add an extra tab that shows you the list of drivers with bad contracts. But that doesn’t take in accordance the idea that we have established prior; data and information will always grow despite current requirements.

From analysing the business, you should know what sort of dataset is likely to increase in volume and also functions. For a dataset such as ‘troubled contracts’, it will definitely increase in volume due to its relation to drivers on the platform. And in the near future it will develop extended functionalities due to the nature of that dataset.

Fig 2 — Function Added

Applying this knowledge, we can better handle this requirement. With this way, it can serve as a heads up display as well as a notification to take action. Also serves as a link to a “ **Contract** ” page which we anticipate to evolve into a more robust module given its nature.

Fig 3 — Full Contracts Page

Looking at the image above, we can see how that one requirement about contracts has morphed into a full contracts page. The image above shows the latter stages of such requirement over time.

### Widgets are your friends

To design very good dashboards, you need to be able to utilise widgets. Because of the data and information your typical dashboard can hold, even to the core users of the platform, it can present itself as a handful, and this is where your widgets come in.

Widgets in dashboards help give the user an extra layer of context to the information being viewed. With helpful widgets, you can reduce overall click times, reduce the decision making time of whoever is viewing said information, and reduce cognitive load on the user. Lets look at an example;

Fig 4 — Ticket Management

Above is a ticket management module with the primary function of creating an issue ticket for drivers. Here the driver has been selected, as well as an issue, and we can see the details of the selected driver on the right. Neat.

However, we can create more context for the analyst here by adding some additional widgets.

Fig 5 — Ticket Management with Widgets

Here, we see that we have added more widgets that gives extra context to the said driver. Now when an analyst searches for a driver, he gets more information about Driver such as — **Driver’s vehicle, Previous Ticket History, and Payment Status**. This extra information adds more context and helps the decision making of the analyst that is about to carry out a function.

### Modals

Often times when we hear the word “modals” we think those neat dialog boxes that give us information or tell us to select an option and then it closes. What if you **extended** the modal features to a do a lot more than that.

Fig 6— Regular Modal

Modals can be used to extend the details of a particular component on a page, thereby adding more context and extra information before a user takes an action. You will find out that, modals are capable of handling more, making an extra page most times, not necessary.

Fig 7— Ticket Management with Extended Modal

### In Conclusion

Dashboards can feel daunting at first when starting off, but there will always be constants and key principles to follow to make your dashboards really effective.

A dashboard is only as effective, as the information it is trying to convey. For the information to be effective, we must understand the context behind why we are displaying such information and this will greatly inform our design decisions and choices.

I will definitely be posting a follow up to this topic, as there are more principles and best practices that still need to be explored. But until then, ciao!
