# Broadly speaking, it’s best not to disable buttons or inputs. Instead we can allow data entry and provide helpful error text (either inline on-the-go or on form submission).

Broadly speaking, it’s best not to disable buttons or inputs. Instead we can allow data entry and provide helpful error text (either inline on-the-go or on form submission).

HTML buttons and inputs accept a Boolean `disabled` attribute. This stops the element from receiving events like clicks and keyboard focus. Browsers usually present the button or input as greyed out.

## Some reasons not to disable an element

*   A sighted user may be able can see greyed out element is greyed out, but might not know why.
*   A sighted user might see the button as clickable and be confused when it doesn’t respond.
*   A low vision user might not be able to see the greyed out element.
*   A screen reader user won’t know about the disabled element as it’s functionally invisible to them.
*   It can be an excuse to avoid writing clear, concise, helpful error messages.

## If an input is disabled, can it be presented another way instead?

*   Can we show it as text instead of a form element?
*   Can we remove it from the form and only show it when it’s relevant?

## If we really have to set a button or input to disabled

We could add a hover-based tooltip to the disabled button. This isn’t ideal though. Since the button doesn’t focus, sighted keyboard users won’t see the message. Screen readers ignore disabled controls, so screen reader users won’t hear the message.

*   Add some nearby visible help text for the button. This would work for sighted users, but not necessarily for low vision users or blind users using a screen reader.
*   Add `aria-disabled="true”` instead of `disabled`. Programmatically link some contextual help text using `aria-describedby="id-of-the-help-text”`, use JS to stop `click` and `submit` events.

## Further reading

*   [Disabled buttons suck](https://axesslab.com/disabled-buttons-suck/)
*   [Disabled buttons don’t have to suck](https://stories.justinewin.com/disabled-buttons-dont-have-to-suck-10da0bb6d37e)

## Related
[Add wiki-links manually or run update_wikilinks.py]