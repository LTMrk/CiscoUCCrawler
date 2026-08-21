---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-fecdeff708
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_01000010.html
retrieved_at: 2026-08-21T17:54:02.635818+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Extension Mobility Cross Cluster Template

## Chapter: Extension Mobility Cross Cluster Template

# Extension Mobility Cross Cluster Template

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to insert, update,
                        		or delete Extension Mobility Cross Cluster (EMCC) in batches, rather than
                        		performing individual updates through Cisco Unified Communications Manager Administration.

## EMCC Templates

Use BAT EMCC templates to define the common EMCC attributes to
                              		  add a group of new EMCC. Prior to creating the template, make sure EMCC
                              		  settings have already been configured in Cisco Unified Communications Manager Administration. You cannot create new settings
                              		  in BAT.

### Find EMCC Template

Because you might have several EMCC templates, Cisco Unified Communications Manager lets you locate specific templates on the
                                 		  basis of specific criteria. Use the following procedure to locate templates.

During your work in a browser session, your find/list search
                                             			 preferences are stored in the cookies on the client machine. If you navigate to
                                             			 other menu items and return to this menu item, or if you close the browser and
                                             			 then reopen a new browser window, your Cisco Unified Communications Manager search preferences are retained until you
                                             			 modify your search.

Choose Bulk
                                                				  Administration > EMCC > EMCC
                                                				  Template .

From the first Find EMCC Template where drop-down list box,
                                          			 choose one of the following criteria:

- Template Name

- Description

From the second Find EMCC Template where drop-down list box,
                                             				choose one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

Specify the appropriate search text, if applicable, and click Find .

To find all EMCC Templates that are registered in the database,
                                                         				  click Find without entering any search text.

A list of discovered templates displays.

From the list of records, click the device name that matches your
                                          			 search criteria.

### Create New EMCC Template

Use BAT to create an EMCC template.

Choose Bulk
                                                				  Administration > EMCC > EMCC
                                                				  Template .

Click Add New .

Enter the EMCC settings that this batch has in common.

After you have entered all the settings for this EMCC template,
                                          			 click Save .

#### What to do next

After creating the template, set a default template from the Insert
                                 		  page. You can access the Insert page through Bulk
                                       				Administration > EMCC > Insert/Update
                                       				EMCC .

### Delete EMCC Template

You can delete EMCC BAT templates when you no longer require
                                 		  them.

The template that is set as the default EMCC template cannot be
                                             			 deleted from the system. You can find the default EMCC template from the
                                             			 Insert/Update EMCC page, or from the Delete EMCC page. You can also find it
                                             			 from the EMCC Template Find List page. On the Find List page, no check box
                                             			 displays against the default template.

Find the EMCC Template that you want to delete.

In the EMCC Template Configuration window, verify
                                          			 that this is the template that you want to delete and click Delete .

You can also delete the EMCC template from the EMCC Template Find and List window. Check
                                                         				  the check box next to the template that you want to delete and click Delete Selected .

To delete the template, click OK . The template name disappears from the list
                                          			 of EMCC templates list on the Find and List EMCC Templates window.

If you submit a job that uses a particulate EMCC template and if
                                                         				  you delete the template, the job also gets deleted.

### BAT EMCC Template Field Descriptions

The following table provides descriptions of all possible
                                 		  fields that display when you are adding an EMCC template.

Some fields display the values that were configured in Cisco Unified Communications Manager Administration.

In the BAT user interface, field names that have an asterisk
                                 		  require an entry. Treat fields that do not have an asterisk as optional.

Field

Description

Device Information

Template Name

Enter the name for the template.

Description

Enter a description for the EMCC template that you want to
                                             					 create. The description can include up to 50 characters in any language, but it
                                             					 cannot include double-quotes ( " ), percentage sign
                                             					 ( % ), ampersand (&), back-slash
                                             					 ( \ ), or angle brackets (<>).

Device Pool

Choose the device pool for this EMCC.

For devices, a device pool defines sets of common
                                             					 characteristics, such as region, date/time group, Cisco Unified Communications Manager group, and calling search space for
                                             					 auto-registration.

SIP Profile

Choose the default SIP profile or a specific profile that was
                                             					 previously created. SIP profiles provide specific SIP information for the phone
                                             					 such as default telephony event payload type, registration and keepalive
                                             					 timers, media ports, Iris, and dynamic DNS server addresses.

Common Device Configuration

Choose the common device configuration to which you want this
                                             					 EMCC assigned. The common device configuration includes the attributes
                                             					 (services or features) that are associated with a particular user. You
                                             					 configure the Common device configurations in the Common Device Configuration
                                             					 window.

To see the common device configuration settings, click the
                                             					 View Details link.

Common Phone Profile

From the drop-down list box, choose a common phone profile
                                             					 from the list of available common phone profiles.

## Topics Related to EMCC Templates

| Note | During your work in a browser session, your find/list search
                                             			 preferences are stored in the cookies on the client machine. If you navigate to
                                             			 other menu items and return to this menu item, or if you close the browser and
                                             			 then reopen a new browser window, your Cisco Unified Communications Manager search preferences are retained until you
                                             			 modify your search. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > EMCC > EMCC
                                                				  Template . The EMCC Template Find and List window displays. Use
                                          			 the two drop-down list boxes to search for a template. |
|---|---|
| Step 2 | From the first Find EMCC Template where drop-down list box,
                                          			 choose one of the following criteria: Template Name Description From the second Find EMCC Template where drop-down list box,
                                             				choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable, and click Find . Tip To find all EMCC Templates that are registered in the database,
                                                         				  click Find without entering any search text. A list of discovered templates displays. | Tip | To find all EMCC Templates that are registered in the database,
                                                         				  click Find without entering any search text. |
| Tip | To find all EMCC Templates that are registered in the database,
                                                         				  click Find without entering any search text. |
| Step 4 | From the list of records, click the device name that matches your
                                          			 search criteria. The window displays the EMCC template that you choose. |

| Tip | To find all EMCC Templates that are registered in the database,
                                                         				  click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > EMCC > EMCC
                                                				  Template . The EMCC Template Find and List window displays. |
|---|---|
| Step 2 | Click Add New . The EMCC Template Configuration window displays. |
| Step 3 | Enter the EMCC settings that this batch has in common. See Table 1 for field descriptions. |
| Step 4 | After you have entered all the settings for this EMCC template,
                                          			 click Save . This creates the template. |

| Note | The template that is set as the default EMCC template cannot be
                                             			 deleted from the system. You can find the default EMCC template from the
                                             			 Insert/Update EMCC page, or from the Delete EMCC page. You can also find it
                                             			 from the EMCC Template Find List page. On the Find List page, no check box
                                             			 displays against the default template. |
|---|---|

| Step 1 | Find the EMCC Template that you want to delete. |
|---|---|
| Step 2 | In the EMCC Template Configuration window, verify
                                          			 that this is the template that you want to delete and click Delete . Note You can also delete the EMCC template from the EMCC Template Find and List window. Check
                                                         				  the check box next to the template that you want to delete and click Delete Selected . A message displays that asks you to confirm the delete
                                          			 operation. | Note | You can also delete the EMCC template from the EMCC Template Find and List window. Check
                                                         				  the check box next to the template that you want to delete and click Delete Selected . |
| Note | You can also delete the EMCC template from the EMCC Template Find and List window. Check
                                                         				  the check box next to the template that you want to delete and click Delete Selected . |
| Step 3 | To delete the template, click OK . The template name disappears from the list
                                          			 of EMCC templates list on the Find and List EMCC Templates window. Caution If you submit a job that uses a particulate EMCC template and if
                                                         				  you delete the template, the job also gets deleted. | Caution | If you submit a job that uses a particulate EMCC template and if
                                                         				  you delete the template, the job also gets deleted. |
| Caution | If you submit a job that uses a particulate EMCC template and if
                                                         				  you delete the template, the job also gets deleted. |

| Note | You can also delete the EMCC template from the EMCC Template Find and List window. Check
                                                         				  the check box next to the template that you want to delete and click Delete Selected . |
|---|---|

| Caution | If you submit a job that uses a particulate EMCC template and if
                                                         				  you delete the template, the job also gets deleted. |
|---|---|

| Field | Description |
|---|---|
| Device Information |
| Template Name | Enter the name for the template. |
| Description | Enter a description for the EMCC template that you want to
                                             					 create. The description can include up to 50 characters in any language, but it
                                             					 cannot include double-quotes ( " ), percentage sign
                                             					 ( % ), ampersand (&), back-slash
                                             					 ( \ ), or angle brackets (<>). |
| Device Pool | Choose the device pool for this EMCC. For devices, a device pool defines sets of common
                                             					 characteristics, such as region, date/time group, Cisco Unified Communications Manager group, and calling search space for
                                             					 auto-registration. |
| SIP Profile | Choose the default SIP profile or a specific profile that was
                                             					 previously created. SIP profiles provide specific SIP information for the phone
                                             					 such as default telephony event payload type, registration and keepalive
                                             					 timers, media ports, Iris, and dynamic DNS server addresses. |
| Common Device Configuration | Choose the common device configuration to which you want this
                                             					 EMCC assigned. The common device configuration includes the attributes
                                             					 (services or features) that are associated with a particular user. You
                                             					 configure the Common device configurations in the Common Device Configuration
                                             					 window. To see the common device configuration settings, click the
                                             					 View Details link. |
| Common Phone Profile | From the drop-down list box, choose a common phone profile
                                             					 from the list of available common phone profiles. |