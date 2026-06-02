Title: Article from medium.muz.li

URL Source: https://smry.ai/https:/medium.muz.li/how-to-design-access-control-system-for-saas-application-b6455c944186

Markdown Content:
Almost all Saas apps have some kind access control system implemented as part of the product. Most of them use RBAC (Role Based Access Control) that allows to organize permissions for certain users groups (roles). Even in basic products there are some actions that should not be available for everyone, like updating billing information or manipulating global passwords or settings.

source: undraw.io

## Access control systems basics

There are a few models for applying access control for some more advanced systems.

**ACL (Access Control List)** allows to define access rights in more granular way. Permission (access to certain object like file or action ) is a starting point here allowing user to perform a particular operation and can be applied for each user separately. There are no access rights groups as roles that users can be assigned to and ultimately gain access to set of permissions at once. As a result each user can have a different set of permissions.

**RBAC system** on the other hand mirrors most companies organizational structures in more accurate way. Permissions to perform certain operations within a system are grouped in a form of a _Role_. There is no need to give access per operation but user get the set of permissions which refer to related actions, often grouped in categories. In this case updates can be done globally within the role.

It also means that in case there is a new feature implemented the role can be updated affecting all users assigned that will get more access right automatically. It helps avoiding updating rights for individual users and is proved to be more effective. RBAC system helps to avoid cases when the permissions applied for the user are overlapping or even worse, contradict each other creating conflicts in the system.

Those 2 approaches can be mixed and Role-based system applied as a core one and the an ad-hoc access to certain part of the app that use ACL as a complimentary one (similar to sharing rights on Google Drive, which also can be temporary like “expiring links”).

Generally each control system helps with:

*   ensuring security (extra control for sensitive data, tracking logs etc.)
*   managing the risk (only data necessary for user)
*   making interface more clear to the users (they get only what they need)
*   efficient management of large organizations in the system (with roles)

## Product design perspective

I had a chance to redesign access control system (RBAC) for app in the HR industry. Those systems can can get quite complex considering the amount of data stored in it. There is a lot of sensitive information about candidates, companies etc. that are being processed in software so it is really important to make permissions system working right. Also since EU GDPR regulations came into light last year, it is even more important now to protect personal data from external threats or any kind of “inside job”.

Why there should be access restrictions in HR app:

*   data, candidates lists can be leaked or stolen by competition/former employee
*   current employees can sneak where they have no purpose to be
*   personal details can be leaked
*   sensitive data like salary expectations should not be visible to everyone

There are particular rules and patterns I would recommend to follow in order achieve best results and avoid painful errors in the future:

## Get Anna Savytska’s stories in your inbox

Join Medium for free to get updates from this writer.

**Permissions can varied**

*   allow for different operations for same access area: read/view, create, update/edit, delete
*   add different types of permissions: security, privacy and the rest
*   add different system roles and team roles which means users can have combined both global access rights (system) and team-specific access rights (different per different team, if user can be in more than one team)
*   remember about “external actors” — there can be _guest permissions_ designed for temporary users or users with very limited rights who somehow operate outside of the organization

**Proper model should be chosen (RBAC recommended) and key elements in this system should be defined and implemented according to its purpose**

*   _User function:_ who is the person, what is her/his role
*   _Core actions:_ what actions person needs to perform to do its role (fulfill function)
*   _Permission_: ability to perform certain action / set of actions (manage/CRUD) or access certain information (view only), user should always be granted access, never denied
*   _Role:_ set of permissions that allow to assign them all at once for the user and basically define access level as well as user’s function in the organization

**User research is a key so make sure you understand your users**

*   what level of granularity is needed for system users (industry specific)
*   how app users usually structure their roles in the company
*   make sure users with particular roles only access data that is absolutely necessary to do their jobs
*   everyone from company administrators responsible for purchase and account management, through managers performing mostly high level operations and checking the reports, recruiters focused on core processes to accountants interested in accessing invoices, should have smooth and pleasant experience with app interface, adjusted specifically to their needs

**Make sure the interface is properly adjusted for all the access levels (roles) and any limitations communicated clearly**

*   it is best to integrate role assignment into onboarding / account creation flow
*   users with different permissions sets can access some part of the app, but some of them might not be available (only elements needed to complete their individual goals)
*   make roles system usable and essential, but preferably unnoticeable
*   always test how users with each role experience the application
*   allow to ask for more access rights when user encounter limitations
*   consider the onboarding flow and product tours for various user types (each role can experience app slightly differently): signup, tour / videos, onboarding related emails

**Find sweet spot between making permissions system granular enough but still providing easy to comprehend control system**

*   it’s important for proper product adoption and can help to avoid support tickets or requiring implementation consultations
*   simplicity and ease of use can be achieved by adjusting granularity, making roles that will meet users organizational needs and providing really good in-app descriptions for each permission
*   do not overcomplicate it at the beginning, test MVP and then built upon that
*   system can get complicated when there are custom roles available — users can create their own set of permissions so you need to consider edge cases and think about issues to resolve upfront
*   if you want to allow custom roles creation — tie permission to operations not roles, so they can be moved between roles in a flexible way

**Proper documentation / help articles and roles descriptions have to be provided**

*   match the permission names to feature/ action names
*   create comparison charts
*   ideally design with hierarchy in mind so the permissions sets _grow_ gradually from the most limited users to power users (highest roles in hierarchy)
*   make sure you know which permissions are about privacy, data safety and which are other access controls

**Design “super user role” carefully**

*   many times super users tend to do more harm than good deleting stuff accidentally so make sure their permissions list is not too wild
*   provide another security level for high-impact, global operations
*   it’s important to recommend using standard account (different role) for non-administrational operations (if those users want to use core features) in order to avoid painful mistakes that can happen (like deleting important data on single profile just because they can)
*   make sure superadmins are provided the thorough descriptions of how permissions are created for them and how they actually work

## Summing up

Designing access levels for Saas app is not an easy task. It is a complex and very technical component. Making this system manageable and scalable is as much of a challenge for developers as it is for product design team. But when following certain rules having in mind first and foremost all of the end users experience as well as security aspects, this can be done in elegant and efficient way, providing customers a powerful tools for improving their day to day operations in your application.
