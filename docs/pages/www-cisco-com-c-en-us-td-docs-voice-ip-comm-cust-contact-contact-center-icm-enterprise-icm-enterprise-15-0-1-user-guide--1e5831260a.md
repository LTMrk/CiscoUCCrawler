---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-guide--1e5831260a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1501/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_0111.html
retrieved_at: 2026-08-16T20:34:09.637416+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Unified Intelligence Center Gadgets in Cisco Finesse

## Chapter: Unified Intelligence Center Gadgets in Cisco Finesse

# Unified Intelligence Center Gadgets in Cisco Finesse

## Configure Live Data Gadgets in Cisco Finesse with compositeFilterId

The compositeFilterId filter is used in gadget filter criteria to achieve the
                              advanced filter criteria. The following example illustrates the compositeFilterId
                              filter usage for advanced filtering in Cisco Finesse desktop.

To add mrDomainID to the existing "Agent Skill Group" live data gadget filter criteria, perform the following steps:

Step 1

Retrieve the existing gadget configuration for "Agent Skill Group" report from the desktop layout:

<gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp ?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL</gadget>

Step 2

Run the Agent Skill Group live data report in Unified Intelligence Center and click the Field Filters tab.

Step 3

Copy the Field Filter name to add to the existing filter criteria and assign the filter value as illustrated in the following
                                       syntax:

<gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget. jsp?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL &compositeFilterId=agent.agentMRDs.mrDomainID=<mrdomainId> </gadget>

Where,

filterId is for basic filter criteria.

compositeFilterId is for Advanced filtering.

agent.id and agent.agentMRDs.mrDomainID are the keys to identify the filter field names.

CL is the value for agent.id to identify all the collections on which agent.id has permissions.

mrdomainId is the value for the key agent.agentMRDs.mrDomainID to filter on the given mrdomainId by replacing the tag <mrdomainId> in
                                                the above URL.

Ensure to:

Replace <my-cuic-server> with the FQDN of the Cisco Unified Intelligence Center server.

Use HTTP or HTTPS based on how the Cisco Finesse desktop is being accessed.

Replace <mrdomainId> with the appropriate mrdid.

If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax:

This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.)

For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5}

<gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_2=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget>

If the gadget URL parameter isDynamicFilterEnabled is set to false, you can set the agent ID(s) as filter parameter, provided the agents or supervisors have access to the agents
                                                            Value List. Ensure that All Users group has read permission on the agents Value List for this to work.

Default value for this parameter is true.

Example:

```
<gadget>https://<cuic.fqdn>:8444/cuicui/gadget/LiveData
LiveDataGadget.xml?gadgetHeight=310&
vie
wId_1=99E6C8E210000141000000D80A0006C4&filterId_1
=agent.id=5002,5011&isDynamicFilterEn
able d=false</gadget>;
```

Configuration changes related to live data gadgets are automatically updated in gadgets and does not require a manual page
                                                      refresh.

## Configure Historical Report Gadgets in Cisco Finesse

In Enterprise deployment ( Unified CCE and Packaged CCE ), Cisco Unified Intelligence Center Historical reporting gadget is available out of the box on Cisco Finesse Supervisor desktop
                                          only and is not supported on Agent desktop.

For Historical Gadgets, only one view is supported.

Cisco Unified Intelligence Center historical report as a gadget does not support grouping and drill-downs in Cisco Finesse
                                          desktop.

Code Snippet

```
<gadget>https://<my-cuic-server>:8444/cuic/gadget/Historical/HistoricalGadget.jsp?gadgetHeight=310
&viewId=F2D86F191000015B000000640A4E5A54&linkType=htmlType&viewType=Grid
&EventTime=RELDATE%20LASTWEEK&User=VL%20CUIC%5Cadministrator</gadget>
```

```
https://<my-cuic-server>:8444/cuic/gadget/Historical/HistoricalGadget.jsp?gadgetHeight=310
```

```
&viewId=F2D86F191000015B000000640A4E5A54&linkType=htmlType&viewType=Grid
```

```
&EventTime=RELDATE%20LASTWEEK&User=VL%20CUIC%5Cadministrator</gadget>
```

For more information on applying the variable parameters, see Variable Parameters in a Permalink section in the Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

## Gadget Toolbar Improvements

Cisco Unified Intelligence Center provides you with a toolbar on Live Data reporting gadget on the Cisco Finesse Desktop.

The following figure shows an example of a gadget toolbar:

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

| Step 1 | Retrieve the existing gadget configuration for "Agent Skill Group" report from the desktop layout: <gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp ?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL</gadget> |
|---|---|
| Step 2 | Run the Agent Skill Group live data report in Unified Intelligence Center and click the Field Filters tab. |
| Step 3 | Copy the Field Filter name to add to the existing filter criteria and assign the filter value as illustrated in the following
                                       syntax: <gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget. jsp?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL &compositeFilterId=agent.agentMRDs.mrDomainID=<mrdomainId> </gadget> Where, filterId is for basic filter criteria. compositeFilterId is for Advanced filtering. agent.id and agent.agentMRDs.mrDomainID are the keys to identify the filter field names. CL is the value for agent.id to identify all the collections on which agent.id has permissions. mrdomainId is the value for the key agent.agentMRDs.mrDomainID to filter on the given mrdomainId by replacing the tag <mrdomainId> in
                                                the above URL. Ensure to: Replace <my-cuic-server> with the FQDN of the Cisco Unified Intelligence Center server. Use HTTP or HTTPS based on how the Cisco Finesse desktop is being accessed. Replace <mrdomainId> with the appropriate mrdid. Note If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_2=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> If the gadget URL parameter isDynamicFilterEnabled is set to false, you can set the agent ID(s) as filter parameter, provided the agents or supervisors have access to the agents
                                                            Value List. Ensure that All Users group has read permission on the agents Value List for this to work. Default value for this parameter is true. Example: <gadget>https://<cuic.fqdn>:8444/cuicui/gadget/LiveData
LiveDataGadget.xml?gadgetHeight=310&
vie
wId_1=99E6C8E210000141000000D80A0006C4&filterId_1
=agent.id=5002,5011&isDynamicFilterEn
able d=false</gadget>; Note Configuration changes related to live data gadgets are automatically updated in gadgets and does not require a manual page
                                                      refresh. | Note | If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_2=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> If the gadget URL parameter isDynamicFilterEnabled is set to false, you can set the agent ID(s) as filter parameter, provided the agents or supervisors have access to the agents
                                                            Value List. Ensure that All Users group has read permission on the agents Value List for this to work. Default value for this parameter is true. Example: <gadget>https://<cuic.fqdn>:8444/cuicui/gadget/LiveData
LiveDataGadget.xml?gadgetHeight=310&
vie
wId_1=99E6C8E210000141000000D80A0006C4&filterId_1
=agent.id=5002,5011&isDynamicFilterEn
able d=false</gadget>; | Note | Configuration changes related to live data gadgets are automatically updated in gadgets and does not require a manual page
                                                      refresh. |
| Note | If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_2=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> If the gadget URL parameter isDynamicFilterEnabled is set to false, you can set the agent ID(s) as filter parameter, provided the agents or supervisors have access to the agents
                                                            Value List. Ensure that All Users group has read permission on the agents Value List for this to work. Default value for this parameter is true. Example: <gadget>https://<cuic.fqdn>:8444/cuicui/gadget/LiveData
LiveDataGadget.xml?gadgetHeight=310&
vie
wId_1=99E6C8E210000141000000D80A0006C4&filterId_1
=agent.id=5002,5011&isDynamicFilterEn
able d=false</gadget>; |
| Note | Configuration changes related to live data gadgets are automatically updated in gadgets and does not require a manual page
                                                      refresh. |

| Note | If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>http://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_2=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> If the gadget URL parameter isDynamicFilterEnabled is set to false, you can set the agent ID(s) as filter parameter, provided the agents or supervisors have access to the agents
                                                            Value List. Ensure that All Users group has read permission on the agents Value List for this to work. Default value for this parameter is true. Example: <gadget>https://<cuic.fqdn>:8444/cuicui/gadget/LiveData
LiveDataGadget.xml?gadgetHeight=310&
vie
wId_1=99E6C8E210000141000000D80A0006C4&filterId_1
=agent.id=5002,5011&isDynamicFilterEn
able d=false</gadget>; |
|---|---|

| Note | Configuration changes related to live data gadgets are automatically updated in gadgets and does not require a manual page
                                                      refresh. |
|---|---|

| Note | In Enterprise deployment ( Unified CCE and Packaged CCE ), Cisco Unified Intelligence Center Historical reporting gadget is available out of the box on Cisco Finesse Supervisor desktop
                                          only and is not supported on Agent desktop. For Historical Gadgets, only one view is supported. |
|---|---|

| Note | Cisco Unified Intelligence Center historical report as a gadget does not support grouping and drill-downs in Cisco Finesse
                                          desktop. |
|---|---|

| Note | You can retrieve this information from any report permalink. |
|---|---|

| Note | For Historical Gadgets, only one view is supported. To add a new report to the Reports View Selector, contact the Cisco Finesse Administrator. |
|---|---|

| Note | When the button is paused and updates are available on the gadget, a notification appears over the pause or play button. |
|---|---|