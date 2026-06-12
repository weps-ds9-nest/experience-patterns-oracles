# Access permissions include Read, Write, None, and Display.

Access permissions include Read, Write, None, and Display.

For descriptions of these options, see [Accessing Ancestor Members in Ad Hoc Grids](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/saas/planning-budgeting-cloud/pfusa&id=SVPBC-GUID-42895151-0DF4-4620-9C6D-85D3EE8C3133).

You can also set who can launch which rules.

*   Launch: Allow launch privileges

View user types have no Write permission to dimension members, so can't launch rules having runtime prompts that include members, dimensions, member ranges, or cross-dimension runtime prompt types. They can, however, launch rules having runtime prompts of other types (for example, date type).  
*   No Launch: Disallow launch privileges

If a user inherits Launch permission to a rule by belonging to a group, and is also assigned No Launch permissions by belonging to another group, the more restrictive No Launch assignment takes precedence.  

You can specify access permission for individual users and each group. When you assign a user to a group, that user acquires the group's access permissions. If an individual's access permissions conflict with those of a group the user belongs to, user access permissions take precedence.

You can use groups to provide access permissions to your application artifacts such as forms, rules, and dashboards. Oracle Fusion Cloud Enterprise Performance Management recognizes three types of groups:

*   Predefined: These groups are automatically created for each application role. All users are assigned to a predefined group based on their application role (for example, Power User).

*   EPM: These are the groups that you create in Access Control in Tools.

*   IDCS: These are the groups that you create in the Oracle Cloud Identity Console. You can view them in Access Control and assign them to granular roles and EPM groups.

For more information, see [Managing Groups](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/saas/planning-budgeting-cloud/pfusa&id=PAPPM-GUID-EE110263-1117-4ED7-87EA-8C72DB835945) in Administering Access Control.

Inheriting Permissions

Inheritance determines the user or group’s access permissions. You can specify an attribute that causes the children or descendants of that member to inherit its permissions. Assigned permissions take precedence over inherited permissions. You can include or exclude the member from the permissions setting.

Table 5-1 Options for Inheriting Access Permissions

| Inheritance Option | Permission Assignment |
| --- | --- |
| Member | Only to the currently selected member |
| Children | To all children members in the level below the currently selected member |
| iChildren | To the currently selected member and all children members in the level below it |
| Descendant | To all descendant members below the currently selected member |
| iDescendant | To the currently selected member and all descendant members below it |

How Permissions are Evaluated

When evaluating permissions, the application gives precedence in this order:

1.   Role-level security. Users with the Service Administrator role have permissions to all application elements.

2.   For Power User, User, and Viewer user types, permissions that are specifically assigned to users.

3.   Permission assignments that are acquired by belonging to a group.

If one member belongs to two groups with different permissions assigned to group members, the least restrictive permission takes precedence. For example, if one group assigns the member Read permission and another group assigns the same member Write permission, Write takes precedence. However if one of the groups assigns no permission (None) to its members, None takes precedence over Read and Write.  
4.   Parent-level assignments (for example, to parent members or folders).

## Related
[Add wiki-links manually or run update_wikilinks.py]