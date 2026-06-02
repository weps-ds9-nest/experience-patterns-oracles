Title: Article from tassyomah.medium.com

URL Source: https://smry.ai/https:/tassyomah.medium.com/custom-role-creation-and-permission-management-feature-case-study-acd4f4cb7ac3

Markdown Content:
While creating arole, I broke the form down into 3 parts to make it easy to create. These three parts are: Basic details, set permissions and review.

**Basic details:** Here, the admin is able to add basic role information, so there’s enough room to accommodate as much details as needed.

**Set permissions:** This screen allows admins to manage the permissions of each role, including what areas of the software they can access and what actions they can perform. Since permissions here are not defined yet and information could be more, I created a structure that allows for more inputs and updates.

I used toggles instead of checkboxes to depict a clear on/off or binary choice to be made, checkboxes sometimes give off a feeling of multiple choices.

**Review/summary:** This was created as a separate section due to how prone to mistakes human beings are. This enables them review the permissions and details of the role before creating.

Role summary/review

I initially thought to make it a simple modal but considering the importance of the process and complexity of the information which could increase over time, I figured a modal wasn’t the best bet.

## Assign Role:

Came up with several ideas for an Admin to assign a role. First is, directly from the employee page, the second is while creating a new role, the third is assigning a role from the employee details page, and the fourth is directly from the roles page.

PS: A role can have multiple individuals or a team assigned to it.

**While creating a new role I can assign it to a team or individuals:**

Select individual or team

As an admin I can, I can assign a role by searching/selecting from a list of employees/team

Assign to selected individuals

Searching keywords to find teams or individuals

**From the employee page:**

An assign a role modal from here requires an admin to select a role and an individual/team

Employee page

Assign from employee page

**From Employee profile/details page:**

Here an individual profile is already selected by default, so an admin can edit their role

Employee profile/details page with the edit button to their roles

Assign from employee profile/details page

Assign existing role

## Permissions

Aside the edit role/edit permission and create role and set permission option, I accounted for scenarios where an admin wants to manage general permissions. The get to do this from the permissions tab under roles or from their settings.

permissions tab For All roles

Set permissions for custom selected individuals — Empty

Set permissions for custom selected individuals

I also figured setting specific permissions individually may be cumbersome so I designed for a scenario where certain permissions have already been set for different access levels within the organisation, and all the admin has to do is assign a level to an individual or team as the case may be

(For this scenario, role permissions can’t be edited, but can only be assigned because they have already been set from the backend and can be customized only based on customer(organization) request)

Set permissions for custom selected individuals

## Conclusion

At several points in the flow, I made sure to add info tips at areas admins might not be commonly familiar with. Since it’s a new Major feature being integrated into an existing system, the purpose is to ease them into the process of understanding and using it.

> “This new feature is expected to increase user adoption and retention while reducing churn”

How then does this design increase user adoption while reducing churn?

*   The set permissions/edit permissions simplifies the management of employee permissions within the organization.
*   The create/assign roles provides more flexibility to create and assign roles that align with the specific needs of the business and also ensures employees only have access to what they need.
*   The edit roles flow allows admins to easily adjust roles and to accommodate changing organizational needs for employee roles. As organizations grow and evolve, it provides scalability, flexibility, reduces churn, and supports the adoption of the system as it aligns with the changing requirements of the organization. (E.g in cases of layoffs and promotions, probation, switching roles internally etc)
*   This feature overall provides increased efficiency, security and a competitive advantage in the market, especially among businesses that need more granular control over employees, roles and permissions.

## Next steps

I attempted to cover a comprehensive range of use cases and considered as many scenarios as I could think of during this process.

If After testing I realize some necessary screens and functionalities are missing, the next steps would be to conduct further research to identify the missing screens and functionalities that users need, collaborate with the product team to prioritize the new functionalities and screens, design the missing screens and test to further validate.

Here’s a link to my figma**:**[**Tassyomah**](http://figma.com/@tassyomah)
