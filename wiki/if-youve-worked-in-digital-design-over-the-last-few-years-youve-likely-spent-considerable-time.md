# If you've worked in digital design over the last few years, you've likely spent considerable time researching or/and designing cookie consent banners. These ubiquitous interface elements, born from privacy regulations like GDPR and CCPA, have become a frequent source of UX frustration.

If you've worked in digital design over the last few years, you've likely spent considerable time researching or/and designing cookie consent banners. These ubiquitous interface elements, born from privacy regulations like GDPR and CCPA, have become a frequent source of UX frustration.

Beyond the obvious annoyance factor, cookie banners represent a fascinating case study in how interface design influences user decision-making in privacy contexts. A recent study by [Papenmeier and colleagues (2025)](https://www.sciencedirect.com/science/article/pii/S0747563225000883?dgcid=rss_sd_all#sec4) offers some insight into this relationship, examining how both external design factors and internal user characteristics affect privacy choices.

The study was recently published in _Computers in Human Behavior_ and explored factors influencing users when they interact with cookie consent banners. The researchers conducted two experiments to investigate:

1.   External choice factors: Design elements like the effort required to reject cookies and visual highlighting of buttons

2.   Internal choice factors: User characteristics like privacy concerns, age, thinking style preferences, and personal attitudes

The study relies on several important theoretical concepts. Some of them have been covered in previous UX Psychology articles but a brief overview is provided below:

*   [Nudging](https://uxpsychology.substack.com/p/guiding-choices-in-ux-the-role-and) refers to subtle design techniques that guide users toward specific choices without restricting their freedom ([Thaler & Sunstein, 2008](https://psycnet.apa.org/record/2008-03730-000)). Originally conceptualised as a way to help people make better decisions, in digital contexts these techniques can be deployed either to enhance or deteriorate privacy ([Kitkowska et al., 2020](https://www.researchgate.net/publication/338985425_Psychological_Effects_and_Their_Role_in_Online_Privacy_Interactions_A_Review)).

*   When websites prioritise profit over user experience, they often employ what are known as [dark patterns (or deceptive patterns)](https://uxpsychology.substack.com/p/dark-patterns-using-human-psychology), design elements that steer users toward choices that may not align with their actual preferences or best interests ([Brignull, 2023](https://www.amazon.co.uk/Deceptive-Patterns-Exposing-Companies-Control/dp/1739454405)).

*   The study also draws on [dual-process theories of cognition](https://uxpsychology.substack.com/p/dark-patterns-using-human-psychology) ([Epstein, 1994](https://psycnet.apa.org/record/1994-45153-001); [Kahneman, 2003](https://psycnet.apa.org/record/2003-08746-001)), which differentiate between:

    *   Type 1 processing: Fast, intuitive, and emotionally-driven decision-making

    *   Type 2 processing: Slower, deliberate, and more analytical decision-making

These theories help explain why certain design elements might be particularly effective in influencing user behaviour by triggering automatic responses through the faster Type 1 pathway before the more deliberate Type 2 processing has a chance to engage.

The first experiment manipulated how much effort was required to reject optional cookies using three different banner designs:

1.   Privacy-friendly design: Made it easy to select only necessary cookies

2.   Dark pattern 1: Required an additional step to reject optional cookies

3.   Dark pattern 2: Similar to dark pattern 1 but with more ambiguous labelling of the "more options" button

Researchers found that the higher the effort required to reject optional cookies, the higher the acceptance rate. The privacy-friendly design led to only 6% of participants accepting all cookies, compared to dramatically higher rates with both dark pattern designs.

Show Image _Figure: The three cookie banner designs used in Experiment 1, showing varying levels of effort required to reject cookies._

This effect occurred regardless of participants' stated privacy concerns or technological affinity, suggesting that _interface design can override individual preferences in decision contexts_.

The second experiment examined how visual highlighting of either the accept or reject button interacted with users' thinking styles:

*   Participants encountered 12 websites with cookie banners

*   Half had the accept button highlighted, half had the reject button highlighted

*   Researchers measured participants' preferences for rational thinking and experiential thinking

[![Image 1: Fig. 4](https://substackcdn.com/image/fetch/$s_!jQU3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d3e62df-fef5-44f8-8691-ee71495c95dc_811x721.jpeg)](https://substackcdn.com/image/fetch/$s_!jQU3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d3e62df-fef5-44f8-8691-ee71495c95dc_811x721.jpeg)

Cookie banner versions used in the second experiment ([source](https://www.sciencedirect.com/science/article/pii/S0747563225000883?dgcid=rss_sd_all#sec4))

The results showed that _button highlighting strongly influenced behaviour_, resulting in more frequent clicks on highlighted buttons. Surprisingly, participants who scored higher on rational thinking (not experiential thinking as expected) were more influenced by the highlighting. About two-thirds of participants showed stable behaviour — either always accepting or always rejecting cookies. Finally, younger participants and those with stronger privacy concerns were less likely to accept cookies.

The study demonstrates just how powerful interface design can be in shaping user decisions. Even simple elements like button highlighting or the number of steps required for a task can drastically alter user behaviour, regardless of the users' stated preferences.

For example, in Experiment 1, the privacy-friendly design resulted in most users selecting only necessary cookies, while designs requiring more effort to reject cookies led to significantly higher acceptance rates. This reveals how the _choice architecture (how options are presented) can be more influential than users' internal preferences in determining behaviour_.

While the study clearly shows that dark patterns "work" in steering users toward accepting cookies, it raises important ethical questions for UX professionals:

1.   Short-term gains vs. long-term trust: Manipulative designs may increase immediate conversion rates but potentially damage user trust over time

2.   Regulatory compliance vs. genuine consent: While technically compliant with regulations, designs that manipulate users into cookie acceptance may violate the spirit of informed consent

3.   Responsibility to users: As UX professionals, we face the challenge of balancing business goals with ethical responsibilities to users

The finding that about two-thirds of users showed consistent behaviour (either always accepting or always rejecting cookies regardless of design) has important implications for segmenting users:

*   Some users appear to have developed heuristics or automatic behaviours when dealing with cookie banners

*   Different demographic groups may respond differently to the same interface (e.g., younger users were less likely to accept cookies)

*   Thinking styles can impact how susceptible users are to design manipulations

This suggests that we should be designing with these different user segments in mind, rather than assuming uniform behaviour across all users.

Based on these research findings, here are concrete recommendations for designing more ethical and effective consent interfaces:

*   Design for informed consent, not conversion: Balance effort symmetrically between accepting and rejecting cookies. Avoid hiding rejection options behind additional clicks. Use clear, straightforward language that communicates the actual consequences of choices. Consider designs that allow for granular cookie selection without excessive cognitive load

*   Test design elements with different user segments: Conduct usability tests with users of varying ages and privacy attitudes, and pay attention to how different thinking styles might interact with your design.

*   Monitor regulatory developments and stay compliant: Regulations around cookie consent continue to evolve, meaning that designs that may be technically compliant today might not remain so. Stay informed about emerging standards and best practices in privacy-centred design.

*   Consider alternative approaches to data collection: Pause and question whether all tracking cookies are necessary for your business goals. Explore privacy-preserving analytics alternatives. Be transparent about value exchange and explain why data collection benefits users.

*   Document design decisions and their rationale: Keep records of why specific design choices were made and how they affect the users. Document how ethical considerations factored into design decisions. This approach creates accountability and helps demonstrate good-faith efforts toward ethical design.

This new study by Papenmeier et al. (2025) highlights the complex relationship between interface design and user psychology in privacy decisions. While external design factors exert powerful influence, internal user factors still play an important role.

As UX professionals, we have significant power to shape user behaviour through design. This power, of course, comes with great responsibility to create interfaces that facilitate genuine informed consent rather than manipulating users toward business-preferred outcomes.

By designing consent mechanisms that respect user agency while still meeting business needs, we can contribute to a digital ecosystem that values both privacy and transparency, ultimately, building stronger, more trusting relationships with users.

## Related
[Add wiki-links manually or run update_wikilinks.py]