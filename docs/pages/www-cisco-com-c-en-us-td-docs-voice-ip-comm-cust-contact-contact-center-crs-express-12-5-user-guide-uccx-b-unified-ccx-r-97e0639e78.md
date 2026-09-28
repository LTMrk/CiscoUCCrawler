---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-unified-ccx-r-97e0639e78
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_unified-ccx-reporting-user-guide-125/uccx_b_unified-ccx-reporting-user-guide-125_chapter_0110.html
retrieved_at: 2026-08-16T21:26:39.048758+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Gadget Toolbar

## Chapter: Gadget Toolbar

- Gadget Toolbar

- Gadget Toolbar Improvements

# Gadget Toolbar

## Gadget Toolbar Improvements

Cisco Unified Intelligence Center provides you with a toolbar on Live Data reporting gadget on the Cisco Finesse Desktop.

You can remove this toolbar by configuring the parameter hideGadgetToolbar to true in the gadget URL.

For example: <gadget>https:// <Server Name> :8444/cuic/gadget/LiveData/LiveDataGadget. xml ?gadgetHeight= 150& hideGadgetToolbar=true &viewId=EF94123F10000164000000FD0A6B2D41&filterId= AgentCallLogDetailStats.agentID=loginId</gadget>

If the parameter hideGadgetToolbar is unavailable in the gadget URL or if it is set to false, then the toolbar is displayed
                                       by default.

### Reports View Selector

As a reporting gadget user, you can select and view multiple reports from the Reports View Selector on the toolbar.

The Reports View Selector is a drop-down list that displays the list of reports in the Report name - View name format. The Report View Selector list allows you to view the five report views.

For Historical Gadgets, only one view is supported.

To add a new report to the Reports View Selector, contact the Cisco Finesse Administrator.

### Toolbar Hide or Unhide

The gadget toolbar displays an arrow tab in the center to hide and unhide the toolbar.

Click the arrow tab to hide the toolbar on the reporting gadget to get a clear view of the report.

When you click the arrow tab again, the toolbar becomes visible on the gadget. When you hover over the arrow tab, the hide
                              and unhide message is displayed.

### Pause and Play

You can pause and resume event updates in Live Data gadgets using the pause or play icons respectively. As a reporting user,
                              the pause or play button works as follows:

Pause - The updates are stopped.

Play - The updates resume and are displayed on the gadget.

When the button is paused and updates are available on the gadget, a notification appears over the pause or play button.

### Show Threshold Only

When you check the Show Thresholds Only box, only rows with matching threshold values are displayed in the report. By default, this check box is unchecked for every
                              report.

### Gadget Help

The gadget toolbar displays a Help icon. When you click the help icon, a window appears, displaying the report template help
                              for the relevant reporting gadgets.

| Note | If the parameter hideGadgetToolbar is unavailable in the gadget URL or if it is set to false, then the toolbar is displayed
                                       by default. |
|---|---|

| Note | For Historical Gadgets, only one view is supported. To add a new report to the Reports View Selector, contact the Cisco Finesse Administrator. |
|---|---|

| Note | When the button is paused and updates are available on the gadget, a notification appears over the pause or play button. |
|---|---|