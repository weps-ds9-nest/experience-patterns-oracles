# For many SaaS applications, product designers need to design permission systems due to privacy concerns and data safety, or in order to make it more efficient and relevant for different types of users. It could be a challenge to set up the structure and continue scaling it as your product evolves.

For many SaaS applications, product designers need to design permission systems due to privacy concerns and data safety, or in order to make it more efficient and relevant for different types of users. It could be a challenge to set up the structure and continue scaling it as your product evolves.

Let me share some concepts and ideas based on my experience designing permissions for an enterprise data and workflow management tool.

**Things to expect in this article:**

*   User and role management
*   Permissions management: page, operation, and data permissions
*   Permission precedence rules
*   Tips for designing permissions

## 1. User and Role Management

### 1) RBAC model

The most popular model in terms of organizing permissions is RBAC ([Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control#Design)), which uses roles to categorize users and manages permissions for each role. Instead of explicitly listing all the available options to individual users ([ACL](https://en.wikipedia.org/wiki/Access-control_list)), this method can largely save admins’ time. It also makes it easier to configure permissions correctly by working the way that administrators think.

ACL vs RBAC model

User roles are serving as a hub between users and permissions, so admins only need to assign roles to each user and configure which permissions the roles have.

Roles as hubs

A popular way to manage users is to design a user list to show users’ information and allow admins to assign users’ roles.

User management

After assigning roles to users, admins need to configure the permissions for each role. They may also need to add new roles or delete existing roles.

User role management

### 2) User group permissions

As your product becomes more complex and starts serving hundreds of people within a company, directly assigning roles to each user becomes time-consuming and hard to manage. Imagine you’re trying to onboard a new office to the software and have to assign roles to 50 users one by one.

Here’s where user groups come in. Beyond the basic RBAC model, you can use groups to categorize users and simply permissions to the groups.

RBAC + User groups

The user groups usually follow human organizational structures. For internal users, the groups could be departments or offices. For external users invited to the application, user groups could be companies.

User groups for internal users and external companies

### 3) Inheriting permissions

For large organizations, the super admin may want to assign a sub-admin within each group in order to allow micro permission management. Also, the permissions within a group can be inherited. This means the leader of the group should have the collection of all the members’ permissions and extra permissions as well.

Inheriting permissions

### 4) How permissions take precedence

Depending on applications and use cases, you may be able to assign permissions to both individual users and each group as a whole. It’s important to specify how the application gives precedence among individual user permission, group permission, and inherited permission.

## Get Licia’s stories in your inbox

Join Medium for free to get updates from this writer.

The designer should try to align this permission precedence with the actual administration system. I’ve shown the permission precedence rule of [Oracle](https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/pfusa/types_of_access_permissions.html) below as an example.

> **Oracle gives permission precedence in this order:**
> 
>  1. Service Admin role has the highest permissions.
> 
>  2. Permissions that are specifically assigned to dividual users.
> 
>  3. Permission assignments that are acquired by belonging to a group.
> 
> **Note:** If one member belongs to two groups with different permissions assigned to groups, the least restrictive permission takes precedence. For example, if one group assigned Read permission and another group assigned Write permission, Write takes precedence. However if one of the groups assigned no permission, None takes precedence over Read and Write. 4. Parent-level assignments

## 2. Permission Management

Setting up the structure of users, roles, and permissions using the RBAC model is referred to as “building anatomy”. Then, it is necessary to determine what the permissions are and how granular they should be.

### 1) Three levels of permissions

There are three common levels of permissions:

*   **Page permission**: access to a page or a function.
*   **Operation permission**: access to a specific action on a page or within a function. Limited by page permissions.
*   **Data permission**: access to specific data on a page or a section. Independent from operation permissions.

Three levels of permissions

The precedence of permissions should also follow the above relationship. For example, if an individual user has access to the “Invite” button but the group to which he or she belongs has no access to the “User List” page, page permission takes precedence.

In most cases, the permission for page and operation is yes/no, and the common options for data permissions are Add, Edit, Delete, and Hide(no access).

Permission levels and types

### 2) Scalability and independency

When designing the information architecture of permissions, one needs to consider the scalability of how to easily add controls for new features. If the application has too many permissions, you can introduce permission groups to make it easier to configure access, just like with user groups for users.

The other important thing to keep in mind is to try to keep each permission independent. That ensures a continuous experience for the users who don’t have complete access to the software. Independency is also required when you have an _a la carte_ pricing model.

Illustration by Rocio Egio Studio

## 3. Balance Granularity and Ease of Use

When a SaaS application grows, so does its complexity. Therefore, ease of use in permission control is a challenge that needs to be addressed. From my experience, there are some points to consider to make it more seamless when onboarding users.

### 1) The need for front-end configuration

If the app is designed for some specific industries with a standard administration system, some permission controls can only be written from the back-end and are not editable for users.

### 2) Default roles and permissions

Presetting some default roles and permissions can largely save users time and potentially prevent serious accidents, such as allowing clients to view vendors’ profits.

### 3) Simplify options

Depending on use cases, permission options may be simplified. For example, Add, Edit, and Delete permissions can be combined as “Edit” for the front-end. For the back-end, it might be a good idea to keep each original option separate in order to preserve flexibility for future changes.

## Summing up

Designing access permission for a SaaS app is not an easy task, but it is a good exercise in figuring out what your use cases are and thinking of how to make your application manageable and scalable.

I hope you find this article helpful and can better understand the relationship between users, groups, roles, and different levels/types of permissions. After figuring this out, you can design permission systems in an effective and elegant way. If you have any questions or doubts, feel free to leave a comment or contact me directly.

## Related
[Add wiki-links manually or run update_wikilinks.py]