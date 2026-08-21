---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-admin-guide-cfin-b-150-cisc-84cf949cb9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/admin/guide/cfin_b_150_cisco-finesse-administration-guide/cfin_m_150_manage-team-resources.html
retrieved_at: 2026-08-21T12:04:44.344895+00:00
---

Cisco Finesse Administration Guide, Release 15.0(1)

# Cisco Finesse Administration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Manage Team Resources

## Chapter: Manage Team Resources

# Manage Team Resources

## Team Resources

Use the Manage Team Resources gadget on the Team Resources tab to assign and unassign phone books, reasons, custom desktop
                              layouts, and workflows to teams. Click the Name or ID header to sort the teams in ascending or descending order.

The Manage Team Resources gadget contains six tabs, each enabling you to assign or unassign resources to a team. The tabs
                              are defined in the following table:

Tab Name

Description

Desktop Layout

Use this tab to customize the desktop layout for the team. The default layout is defined in the Manage Desktop Layout gadget.
                                          You can define one custom layout for the team.

Phone Books

Use this tab to assign and unassign phone books to the team. Only phone books that are defined in the Manage Phone Books gadget
                                          as available to teams are available for assignment.

Reason Codes (Not Ready)

Use this tab to assign and unassign Not Ready reason codes to the team. Only Not Ready reason codes that are defined in the
                                          Manage Reason Codes (Not Ready) gadget as available to teams (not global) are available for assignment.

Reason Codes (Sign Out)

Use this tab to assign and unassign Sign Out reason codes to the team. Only Sign Out reason codes that are defined in the
                                          Manage Reason Codes (Sign Out) gadget as available to teams (not global) are available for assignment.

Wrap-Up Reasons

Use this tab to assign and unassign Wrap-Up reasons to the team. Only Wrap-Up reasons that are defined in the Manage Wrap-Up
                                          Reasons gadget as available to teams (not global) are available for assignment.

Workflows

Use this tab to assign and unassign workflows to the team. Only workflows that are defined in the Manage Workflows gadget
                                          are available for assignment.

### Actions on the Manage Team Resources Gadget

Add : Assign a phone book, reason, or workflow to the team

Save : Save the phone book, reason, desktop layout assignment, or workflow to the team

Revert : Cancel any changes made before they are saved

Refresh : Refresh the list of teams

If you select a team and then click Refresh, the team is deselected and the Resources area for that team disappears. The list
                                                of teams is refreshed and you must select a team again.

### Add or Delete a Team When Database is Not Accessible

If you add or delete a team when Finesse cannot access the Finesse database, those changes do not appear in the Finesse administration
                              console unless you restart Cisco Finesse Tomcat or the CTI server.

## Assign Phone Books and Reasons to Team

Step 1

In the Manage Team Resources gadget, select a team.

Step 2

Click the tab for the resource you want to assign for the selected team.

Step 3

Click Add .

Step 4

Select one or more resources from the list to assign them to the team.

Resources you assign are highlighted in blue in the Add <resources> popup and added to the List of <resources> area.

Step 5

When you finish assigning resources, click Save .

You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved.

## Unassign Phone Books and Reasons from Team

Step 1

In the Manage Team Resources gadget, select a team.

Step 2

Click the tab for the resource you want to unassign from the selected team.

Step 3

Click the red X next to the resource you want to unassign.

Step 4

Click Save .

## Assign Custom Desktop Layout to Team

Step 1

In the Manage Team Resources gadget, select a team.

Step 2

Click Desktop Layout .

The Desktop Layout XML area appears. The area contains the default desktop layout XML.

Step 3

Select the Override System Default check box.

The XML becomes editable.

Step 4

Select from the following editors:

- Text Editor

- XML Editor

For more information, see Default Layout XML .

Step 5

Edit the XML.

Step 6

Click Save .

The custom desktop layout replaces the default desktop layout for the team after 10 seconds. If a supervisor or agent is signed
                                          in when the change is saved, the change does not take effect on their desktop until the supervisor or agent signs out and
                                          signs in again.

If you clear the Override System Default check box, any changes you made to the XML are lost and the XML in the editing pane
                                                      reverts to the default desktop layout XML.

If the Supervisor is managing single/multiple teams, the custom layout of the team for which the supervisor is a resource/agent
                                          is displayed. However, if the supervisor is not the resource/agent of a team, the default layout is displayed.

### Customize Desktop Properties at Team Level

You can customize the Finesse desktop properties for a specific team.

Step 1

In the Manage Team Resources gadget, select a team.

Step 2

Click Desktop Layout .

Step 3

Select the Override System Default check box.

Step 4

Select from the following editors:

- Text Editor

- XML Editor

Step 5

Enter the desktop property name in the config key tag.

Step 6

Enter the possible value of the desktop property in the value tag.

The following are the sample desktop property entries, as displayed in the default Desktop Layout . To change these desktop property entries in Text Editor , remove the comment (<!-- and -->) and set appropriate values.

If the property value is defined in the team-specific desktop layout ( Manage Team Resources > Desktop Layout ), then the team-specific desktop layout takes precedence over the property value defined in the Desktop Layout and CLI .

For more information on customizing desktop properties at Desktop Layout , see Customize Desktop Properties .

For more information on Finesse CLIs, see Desktop Properties .

The following table lists the desktop properties that support team-level
                                             updates:

Config Key

Value

Default Value

enableDragDropAndResizeGadget

true|false

false

enableShortCutKeys

true|false

true

forceWrapUp

true|false

true

wrapUpCountDown

true|false

true

showWrapUpTimer

true|false

true

desktopChatAttachmentEnabled

true|false

true

desktopChatMaxAttachmentSize

Range: 5 to 10 (MB)

5

desktopChatUnsupportedFileTypes

Unsupported file formats include comma-separated valid
                                                         file extensions. For example: .exe, .sh

.exe, .msi, .sh, .bat

showAgentHistoryGadgets

true|false

true

showActiveCallDetails

(for Supervisor Only)

true|false

true

pendingDTMFThresholdCount

Range: 1—20

20

dtmfRequestTimeoutInMs

Range: 1000—200000 (1 to 200 seconds)

5000 (5 seconds)

enableDropParticipantFor

supervisor_only|conference_controller_

and_supervisor|all

supervisor_only

dropParticipant

agents|all

agents

For more
                                             information on Finesse desktop properties, see Desktop
                                                Properties .

Step 7

Click Save .

The change takes effect when the agent or supervisor refreshes the Finesse desktop or sign out and sign in again.

If you clear the Override System Default check box and click Save . The changes are overwritten, and the editing pane reverts to the default desktop layout XML.

## Assign Workflows to Team

Step 1

In the Manage Team Resources gadget, select a team.

Step 2

Click the Workflows tab.

Step 3

Click Add .

Step 4

Select one or more workflows from the list to assign them to the team.

Workflows you assign are highlighted in blue in the Add Workflows popup and added to the List of Workflows area.

Step 5

Workflows are run in the order they are listed. Use the up and down arrows to move a selected workflow to the desired position
                                       in the list.

Step 6

When you has finished assigning workflows, click Save .

You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not on others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved.

## Unassign Workflows from Team

Step 1

In the Manage Team Resources gadget, select a team.

Step 2

Click the Workflows tab.

Step 3

Click the red X next to the workflow to unassign.

Step 4

Click Save .

| Tab Name | Description |
|---|---|
| Desktop Layout | Use this tab to customize the desktop layout for the team. The default layout is defined in the Manage Desktop Layout gadget.
                                          You can define one custom layout for the team. |
| Phone Books | Use this tab to assign and unassign phone books to the team. Only phone books that are defined in the Manage Phone Books gadget
                                          as available to teams are available for assignment. |
| Reason Codes (Not Ready) | Use this tab to assign and unassign Not Ready reason codes to the team. Only Not Ready reason codes that are defined in the
                                          Manage Reason Codes (Not Ready) gadget as available to teams (not global) are available for assignment. |
| Reason Codes (Sign Out) | Use this tab to assign and unassign Sign Out reason codes to the team. Only Sign Out reason codes that are defined in the
                                          Manage Reason Codes (Sign Out) gadget as available to teams (not global) are available for assignment. |
| Wrap-Up Reasons | Use this tab to assign and unassign Wrap-Up reasons to the team. Only Wrap-Up reasons that are defined in the Manage Wrap-Up
                                          Reasons gadget as available to teams (not global) are available for assignment. |
| Workflows | Use this tab to assign and unassign workflows to the team. Only workflows that are defined in the Manage Workflows gadget
                                          are available for assignment. |

| Note | If you select a team and then click Refresh, the team is deselected and the Resources area for that team disappears. The list
                                                of teams is refreshed and you must select a team again. |
|---|---|

| Step 1 | In the Manage Team Resources gadget, select a team. |
|---|---|
| Step 2 | Click the tab for the resource you want to assign for the selected team. |
| Step 3 | Click Add . |
| Step 4 | Select one or more resources from the list to assign them to the team. Resources you assign are highlighted in blue in the Add <resources> popup and added to the List of <resources> area. |
| Step 5 | When you finish assigning resources, click Save . Note You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. | Note | You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. |
| Note | You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. |

| Note | You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. |
|---|---|

| Step 1 | In the Manage Team Resources gadget, select a team. |
|---|---|
| Step 2 | Click the tab for the resource you want to unassign from the selected team. |
| Step 3 | Click the red X next to the resource you want to unassign. |
| Step 4 | Click Save . |

| Step 1 | In the Manage Team Resources gadget, select a team. |
|---|---|
| Step 2 | Click Desktop Layout . The Desktop Layout XML area appears. The area contains the default desktop layout XML. |
| Step 3 | Select the Override System Default check box. The XML becomes editable. |
| Step 4 | Select from the following editors: Text Editor XML Editor For more information, see Default Layout XML . |
| Step 5 | Edit the XML. |
| Step 6 | Click Save . The custom desktop layout replaces the default desktop layout for the team after 10 seconds. If a supervisor or agent is signed
                                          in when the change is saved, the change does not take effect on their desktop until the supervisor or agent signs out and
                                          signs in again. Note If you clear the Override System Default check box, any changes you made to the XML are lost and the XML in the editing pane
                                                      reverts to the default desktop layout XML. | Note | If you clear the Override System Default check box, any changes you made to the XML are lost and the XML in the editing pane
                                                      reverts to the default desktop layout XML. |
| Note | If you clear the Override System Default check box, any changes you made to the XML are lost and the XML in the editing pane
                                                      reverts to the default desktop layout XML. |

| Note | If you clear the Override System Default check box, any changes you made to the XML are lost and the XML in the editing pane
                                                      reverts to the default desktop layout XML. |
|---|---|

| Note | If the Supervisor is managing single/multiple teams, the custom layout of the team for which the supervisor is a resource/agent
                                          is displayed. However, if the supervisor is not the resource/agent of a team, the default layout is displayed. |
|---|---|

| Step 1 | In the Manage Team Resources gadget, select a team. |
|---|---|
| Step 2 | Click Desktop Layout . |
| Step 3 | Select the Override System Default check box. |
| Step 4 | Select from the following editors: Text Editor XML Editor |
| Step 5 | Enter the desktop property name in the config key tag. |
| Step 6 | Enter the possible value of the desktop property in the value tag. The following are the sample desktop property entries, as displayed in the default Desktop Layout . To change these desktop property entries in Text Editor , remove the comment (<!-- and -->) and set appropriate values. Note If the property value is defined in the team-specific desktop layout ( Manage Team Resources > Desktop Layout ), then the team-specific desktop layout takes precedence over the property value defined in the Desktop Layout and CLI . For more information on customizing desktop properties at Desktop Layout , see Customize Desktop Properties . For more information on Finesse CLIs, see Desktop Properties . The following table lists the desktop properties that support team-level
                                             updates: Config Key Value Default Value enableDragDropAndResizeGadget true\|false false enableShortCutKeys true\|false true forceWrapUp true\|false true wrapUpCountDown true\|false true showWrapUpTimer true\|false true desktopChatAttachmentEnabled true\|false true desktopChatMaxAttachmentSize Range: 5 to 10 (MB) 5 desktopChatUnsupportedFileTypes Unsupported file formats include comma-separated valid
                                                         file extensions. For example: .exe, .sh .exe, .msi, .sh, .bat showAgentHistoryGadgets true\|false true showActiveCallDetails (for Supervisor Only) true\|false true pendingDTMFThresholdCount Range: 1—20 20 dtmfRequestTimeoutInMs Range: 1000—200000 (1 to 200 seconds) 5000 (5 seconds) enableDropParticipantFor supervisor_only\|conference_controller_ and_supervisor\|all supervisor_only dropParticipant agents\|all agents For more
                                             information on Finesse desktop properties, see Desktop
                                                Properties . | Note | If the property value is defined in the team-specific desktop layout ( Manage Team Resources > Desktop Layout ), then the team-specific desktop layout takes precedence over the property value defined in the Desktop Layout and CLI . For more information on customizing desktop properties at Desktop Layout , see Customize Desktop Properties . For more information on Finesse CLIs, see Desktop Properties . | Config Key | Value | Default Value | enableDragDropAndResizeGadget | true\|false | false | enableShortCutKeys | true\|false | true | forceWrapUp | true\|false | true | wrapUpCountDown | true\|false | true | showWrapUpTimer | true\|false | true | desktopChatAttachmentEnabled | true\|false | true | desktopChatMaxAttachmentSize | Range: 5 to 10 (MB) | 5 | desktopChatUnsupportedFileTypes | Unsupported file formats include comma-separated valid
                                                         file extensions. For example: .exe, .sh | .exe, .msi, .sh, .bat | showAgentHistoryGadgets | true\|false | true | showActiveCallDetails (for Supervisor Only) | true\|false | true | pendingDTMFThresholdCount | Range: 1—20 | 20 | dtmfRequestTimeoutInMs | Range: 1000—200000 (1 to 200 seconds) | 5000 (5 seconds) | enableDropParticipantFor | supervisor_only\|conference_controller_ and_supervisor\|all | supervisor_only | dropParticipant | agents\|all | agents |
| Note | If the property value is defined in the team-specific desktop layout ( Manage Team Resources > Desktop Layout ), then the team-specific desktop layout takes precedence over the property value defined in the Desktop Layout and CLI . For more information on customizing desktop properties at Desktop Layout , see Customize Desktop Properties . For more information on Finesse CLIs, see Desktop Properties . |
| Config Key | Value | Default Value |
| enableDragDropAndResizeGadget | true\|false | false |
| enableShortCutKeys | true\|false | true |
| forceWrapUp | true\|false | true |
| wrapUpCountDown | true\|false | true |
| showWrapUpTimer | true\|false | true |
| desktopChatAttachmentEnabled | true\|false | true |
| desktopChatMaxAttachmentSize | Range: 5 to 10 (MB) | 5 |
| desktopChatUnsupportedFileTypes | Unsupported file formats include comma-separated valid
                                                         file extensions. For example: .exe, .sh | .exe, .msi, .sh, .bat |
| showAgentHistoryGadgets | true\|false | true |
| showActiveCallDetails (for Supervisor Only) | true\|false | true |
| pendingDTMFThresholdCount | Range: 1—20 | 20 |
| dtmfRequestTimeoutInMs | Range: 1000—200000 (1 to 200 seconds) | 5000 (5 seconds) |
| enableDropParticipantFor | supervisor_only\|conference_controller_ and_supervisor\|all | supervisor_only |
| dropParticipant | agents\|all | agents |
| Step 7 | Click Save . The change takes effect when the agent or supervisor refreshes the Finesse desktop or sign out and sign in again. Note If you clear the Override System Default check box and click Save . The changes are overwritten, and the editing pane reverts to the default desktop layout XML. | Note | If you clear the Override System Default check box and click Save . The changes are overwritten, and the editing pane reverts to the default desktop layout XML. |
| Note | If you clear the Override System Default check box and click Save . The changes are overwritten, and the editing pane reverts to the default desktop layout XML. |

| Note | If the property value is defined in the team-specific desktop layout ( Manage Team Resources > Desktop Layout ), then the team-specific desktop layout takes precedence over the property value defined in the Desktop Layout and CLI . For more information on customizing desktop properties at Desktop Layout , see Customize Desktop Properties . For more information on Finesse CLIs, see Desktop Properties . |
|---|---|

| Config Key | Value | Default Value |
|---|---|---|
| enableDragDropAndResizeGadget | true\|false | false |
| enableShortCutKeys | true\|false | true |
| forceWrapUp | true\|false | true |
| wrapUpCountDown | true\|false | true |
| showWrapUpTimer | true\|false | true |
| desktopChatAttachmentEnabled | true\|false | true |
| desktopChatMaxAttachmentSize | Range: 5 to 10 (MB) | 5 |
| desktopChatUnsupportedFileTypes | Unsupported file formats include comma-separated valid
                                                         file extensions. For example: .exe, .sh | .exe, .msi, .sh, .bat |
| showAgentHistoryGadgets | true\|false | true |
| showActiveCallDetails (for Supervisor Only) | true\|false | true |
| pendingDTMFThresholdCount | Range: 1—20 | 20 |
| dtmfRequestTimeoutInMs | Range: 1000—200000 (1 to 200 seconds) | 5000 (5 seconds) |
| enableDropParticipantFor | supervisor_only\|conference_controller_ and_supervisor\|all | supervisor_only |
| dropParticipant | agents\|all | agents |

| Note | If you clear the Override System Default check box and click Save . The changes are overwritten, and the editing pane reverts to the default desktop layout XML. |
|---|---|

| Step 1 | In the Manage Team Resources gadget, select a team. |
|---|---|
| Step 2 | Click the Workflows tab. |
| Step 3 | Click Add . |
| Step 4 | Select one or more workflows from the list to assign them to the team. Workflows you assign are highlighted in blue in the Add Workflows popup and added to the List of Workflows area. |
| Step 5 | Workflows are run in the order they are listed. Use the up and down arrows to move a selected workflow to the desired position
                                       in the list. |
| Step 6 | When you has finished assigning workflows, click Save . Note You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not on others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. | Note | You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not on others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. |
| Note | You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not on others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. |

| Note | You can make changes on all resource tabs and then save them at the same time. If there is an error on one resource tab but
                                                      not on others, the changes on the tabs with no errors are saved while the changes on the tab with errors are not saved. |
|---|---|

| Step 1 | In the Manage Team Resources gadget, select a team. |
|---|---|
| Step 2 | Click the Workflows tab. |
| Step 3 | Click the red X next to the workflow to unassign. |
| Step 4 | Click Save . |