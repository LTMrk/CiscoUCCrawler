---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-guide--f68a0b04da
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/guide/ucce_b_scripting-and-media-routing-guide-for-cisco-unified-icm-contact-center-enterprise-release-15_0/script_editor_feature_control.html
retrieved_at: 2026-08-16T20:38:53.855520+00:00
---

Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Script Editor Feature Control

## Chapter: Script Editor Feature Control

# Script Editor Feature Control

## Script Feature Control Methods

Administrators can use Script Editor Feature Control to restrict users, or classes of users, from some or all of the functionality
                           of the Unified CCE Script Editor software. In a possible deployment scenario, a Unified CCE administrator can restrict certain people from doing specific types of script editing.

An administrator has two means to restrict access to the
                           editing features of Script Editor and Internet Script Editor:

Edit Options

Script Node Control

Administrators control script editing by creating feature sets that they assign to users. The feature set controls which script
                           nodes are accessible to the user, and which edit modes are available to the
                           user.

For more information about Feature Control, see the Configuration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Edit Options

The administrator can assign one of two editing options:

Full Edit (Includes Quick Edit)

Quick Edit Only

You can only access the Full Edit mode or the Quick Edit mode from the
                              Monitor or the Browse modes. The Full Edit and the Quick Edit modes cannot
                              be accessed from each other.

### Full Edit (Includes Quick Edit)

Full Edit mode allows you to use Full Edit mode or Quick Edit mode
                                 when working with scripts. Both Full Edit and Quick Edit are enabled on
                                 the Script Editor toolbar. When changing from Monitor or Browse mode to
                                 Full Edit mode, the Script Editor workspace background goes from gray to
                                 white.

Your Full Edit mode editing capabilities are determined by
                                 whether or not you are assigned to a feature control set:

If you are a full-edit user and are not assigned to a feature
                                       control set, you can add, edit, or delete any script or node.

If you are a full-edit user and are assigned to a feature
                                       control set, you can add, edit, or delete any script. You only
                                       have Full Edit permissions for those scripts that do not contain
                                       nodes that are marked as unavailable to you in a feature set.

Full Edit gives you restricted editing capabilities if you are
                                 assigned a feature control set. You can still edit any script, however,
                                 your ability to edit specific script nodes is determined by which nodes
                                 are selected in the Node Control table (located on the Script Editor
                                 Feature Control dialog) of the assigned feature control set. This allows
                                 you to edit the structure of a script or to create, edit, and delete
                                 scripts containing the selected nodes.

If a script is opened that contains a disabled node, you can browse or
                                 monitor the script but you cannot put the script into edit mode. If you
                                 attempt to put this script into edit mode a message indicating you are
                                 not authorized to enter edit mode appears. However, you can still
                                 Quick Edit the script, just not the node.

You might want to use Quick Edit mode so as not to accidentally change
                                 the structure of a script.

### Quick Edit Only

Quick Edit mode allows you (the feature-control-set member) to work
                                 only with scripts in Quick Edit mode. Edit is disabled and Quick Edit is
                                 enabled on the Script Editor toolbar. When changing from Monitor or
                                 Browse mode to Quick Edit mode, the Script Editor workspace background
                                 goes from gray to yellow.

In Quick Edit mode:

You cannot add or delete a node.

You can adjust most of the properties of the script nodes
                                       selected in the Node Control table of your assigned feature
                                       control set.  However, in 	Quick Edit Mode, you cannot edit any properties of the selected nodes that
                                       change the structure of a script or that reset previous
                                       reporting data.

As a Quick Edit Only User:

You can only edit scripts through Quick Edit mode.

You cannot create or delete a script.

You can access the Properties of any script node in any mode
                                       by either right clicking on the node and selecting Properties,
                                       or by double-clicking on the node.

You cannot edit the Call Type Manager dialog box (Script > Call
                                       Type Manager).

You cannot edit the Administrative Manager dialog box  (Script >
                                       Administrative Manager).

You cannot edit the Custom Functions dialog box (Script >
                                       Custom Functions).

Script > Make Active Version is disabled.

Script > Make Active Version is disabled.

You cannot import scripts.

You cannot use the File > Script Locks tool.

### Access Quick Edit Mode

Choose Script > Quick
                                       Edit .

Click Quick Edit on the Script Editor
                                    toolbar.

Right-click in the Script Editor workspace and choose Quick Edit .

From within the script in Monitor mode, double-click the node
                                    you want to edit. (This is only available if Options >
                                    Preferences > Allow for Quick Edit from Monitor Mode is
                                    checked.)

#### What to do next

When in Quick Edit mode, the disabled nodes are removed from the
                                 object palette.

## Script Node Control

Script Editor Feature Control allows an administrator to create feature
                              sets that can be assigned to users.  Administrators use a Node Control Table in the feature set to control which script
                              nodes are accessible to the user.

### Node Control Table

The Node Control table (on the Unified CCE Configuration Manager Script Editor Feature Control dialog box) has two columns, the Node column and the Available column.
                                 This table allows an administrator to create feature control sets that can be assigned to users. The feature control set controls
                                 which script nodes are accessible to the user.

If a script is opened that contains a disabled node, you can browse or
                                 monitor the script but you cannot put the script into edit mode. If you
                                 attempt to put this script into edit mode a message indicating you are
                                 not authorized to enter edit mode appears. However, you can still
                                 Quick Edit the script, just not the node.

### Node Column

A node is an executable element within a script. A script consists of
                                 nodes, connections, routing targets, and comments. Every script begins
                                 with a Start node. This column lists of all the nodes that you can use
                                 in a script.

### Available Column

Each checked node in this column appears on the editing palette of the
                                 feature-control-set user, regardless of the edit mode (Full Edit or
                                 Quick Edit Only).

Disabled nodes are removed from the object palette.

## Create a Feature Control Set

The system administrator can create a feature control set using the Unified CCE Configuration Manager on Administration & Data Server:

Step 1

Ensure the users the feature set is to be assigned to are
                                       configured.

Step 2

Start the Unified CCE Configuration Manager.

Step 3

Choose Tools > List Tools > Feature Control Set
                                          List .

Step 4

In the Feature Control Set section (on the left), click Add.

Step 5

Enter the name of the feature control set. The name appears in the
                                       left section when Enter or Tab is pressed.

Step 6

Optionally, enter a description.

## Assign Users to a Feature Control Set

## Select Script Nodes and Edit Options for a Feature Control Set

Step 1

In the Feature Control Set List dialog box, select the name of the
                                       feature control set to be assigned.

Step 2

Select Advanced (under Script Editor).

Step 3

In the Script Editor Feature Control dialog box, select the nodes
                                       for this feature control set and an edit option (Full Edit or Quick
                                       Edit).

Step 4

Click OK .

Step 5

Click Save .

| Note | When Unified CCE runs on a partitioned system, users need at least reference access to objects to edit scripts that contain references to
                                    those objects. For example, a user needs at least reference access to skill groups to edit a script in which those skill groups
                                    are included in the Skill Group node. |
|---|---|

| Note | The Line Connector node is always available. |
|---|---|

| Step 1 | Ensure the users the feature set is to be assigned to are
                                       configured. |
|---|---|
| Step 2 | Start the Unified CCE Configuration Manager. |
| Step 3 | Choose Tools > List Tools > Feature Control Set
                                          List . |
| Step 4 | In the Feature Control Set section (on the left), click Add. |
| Step 5 | Enter the name of the feature control set. The name appears in the
                                       left section when Enter or Tab is pressed. |
| Step 6 | Optionally, enter a description. |

| Step 1 | In the Feature Control Set List dialog box, select the name of the
                                       feature control set to be assigned. |
|---|---|
| Step 2 | Select Advanced (under Script Editor). |
| Step 3 | In the Script Editor Feature Control dialog box, select the nodes
                                       for this feature control set and an edit option (Full Edit or Quick
                                       Edit). |
| Step 4 | Click OK . |
| Step 5 | Click Save . |