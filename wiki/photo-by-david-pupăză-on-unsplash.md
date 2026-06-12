# Photo by David Pupăză on Unsplash.

Photo by David Pupăză on Unsplash.

At my previous company, I was the sole UX Writer. It was a fun time, but also challenging. It’s easy to become a bottleneck; it’s also inevitable that you have to prioritize some things, which means deprioritizing some others.

One of my favorite projects, though, was working on error messages. It’s something I’m constantly researching, because when they go wrong, they go _wrong_.

Bringing content design to errors can make them actually helpful, and even limit a few along the way.

### What is an error message?

Errors appear when something isn’t working the way it should. If you google writing error messages, the main advice you’ll see is about tone, and that’s certainly important. Never blame the user, and never throw out technical jargon or code. The main goal is to clearly and simply state what went wrong and, if there’s a solution, to explain what that is.

Component-wise, errors appear as in-line help text, banners, toasts, popups, modals, etc. The choice is with you and your design system, but a good rule of thumb is to keep the message in close proximity to the error itself.

### What are the types of errors?

I’m not going to list out all the error codes that exist, because that helps no one. Working alongside a dev team, we realized that all errors can be categorized into two buckets: errors that are _our_ fault, and errors that are the _user’s_ fault.

### When it’s our fault

Company-caused errors can be further categorized into five smaller buckets:

**Not found**: This means that the information the user is trying to pull up no longer exists. They need to know why, and be taken to a new area or back to the previous screen.

**Bad request**: The info that the user’s searching for exists, but can’t be accessed right now. This is usually because set conditions aren’t met, or there are issues with the API. It could also mean that our company messed up with the product logic.

**Server**: This is for sad techy problems. All you can do is ask the user to try again.

## Related
[Add wiki-links manually or run update_wikilinks.py]