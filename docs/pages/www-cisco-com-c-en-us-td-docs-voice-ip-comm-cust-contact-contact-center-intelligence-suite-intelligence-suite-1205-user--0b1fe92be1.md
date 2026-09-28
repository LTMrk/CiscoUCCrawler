---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1205-user--0b1fe92be1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1205/user/guide/cuic_b_user-guide-1205/cuic_b_user-guide-1205_chapter_0111.html
retrieved_at: 2026-08-21T04:38:52.856977+00:00
---

Cisco Unified Intelligence Center User Guide, Release 12.5(1)

# Cisco Unified Intelligence Center User Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Unified Intelligence Center Gadgets in Cisco Finesse

## Chapter: Unified Intelligence Center Gadgets in Cisco Finesse

# Unified Intelligence Center Gadgets in Cisco Finesse

## Configure Cross-Origin Resource Sharing (CORS) for Unified Intelligence Center Gadgets

To ensure that Cisco Unified Intelligence Center gadgets load correctly within Cisco Finesse, add all the Finesse host URLs
                           used to access Finesse to the Unified Intelligence Center's CORS allowed origins list using the following commands:

```
utils cuic cors allowed_origin add https://<Finesse_FQDN>
utils cuic cors allowed_origin add https://<Finesse_FQDN>:8445
```

## Configure Live Data Gadgets in Cisco Finesse with compositeFilterId

The compositeFilterId filter is used in gadget filter criteria to achieve the
                              advanced filter criteria. The following example illustrates the compositeFilterId
                              filter usage for advanced filtering in Cisco Finesse desktop.

To add mrDomainID to the existing "Agent Skill Group" live data gadget filter criteria, perform the following steps:

Step 1

Retrieve the existing gadget configuration for "Agent Skill Group" report from the desktop layout:

<gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp ?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL</gadget>

Step 2

Run the Agent Skill Group live data report in Unified Intelligence Center and click the Field Filters tab.

Step 3

Copy the Field Filter name to add to the existing filter criteria and assign the filter value as illustrated in the following
                                       syntax:

<gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget. jsp?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL &compositeFilterId=agent.agentMRDs.mrDomainID=<mrdomainId> </gadget>

Where,

filterId is for basic filter criteria.

'loginId' and 'teamName' work as place-holders in the filterId parameter:

'loginId' is replaced with the logged in user Id.

'teamName' is replaced with the team that the logged in user belongs to.

compositeFilterId is for Advanced filtering.

agent.id and agent.agentMRDs.mrDomainID are the keys to identify the filter field names.

CL is the value for agent.id to identify all the collections on which agent.id has permissions.

mrdomainId is the value for the key agent.agentMRDs.mrDomainID to filter on the given mrdomainId by replacing the tag <mrdomainId> in
                                                the above URL.

Ensure to:

Replace <my-cuic-server> with the FQDN of the Cisco Unified Intelligence Center server.

Use HTTPS based on how the Cisco Finesse desktop is being accessed.

Replace <mrdomainId> with the appropriate mrdid.

If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax:

This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.)

For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5}

<gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_1=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget>

If the agent's or supervisor's password is changed, it takes 20 to 40 minutes to load the Cisco Unified Intelligence Center
                                                      gadgets properly for that user.

## Configure Historical Report Gadgets in Cisco Finesse

In Enterprise deployment ( Unified CCE and Packaged CCE ), Cisco Unified Intelligence Center Historical reporting gadget is available out of the box on Cisco Finesse Supervisor desktop
                                          only and is not supported on Agent desktop.

For Historical Gadgets, only one view is supported.

Cisco Unified Intelligence Center historical report as a gadget does not support grouping and drill-downs in Cisco Finesse
                                          desktop.

If an agent's or supervisor's password is changed, it takes 20 to 40 minutes to load the Cisco Unified Intelligence Center
                                          gadgets properly for that user.

Code Snippet

```
<gadget>https://<my-cuic-server>:8444/cuic/gadget/Historical/HistoricalGadget.jsp?gadgetHeight=310
&viewId=F2D86F191000015B000000640A4E5A54&linkType=htmlType&viewType=Grid
&EventTime=RELDATE%20LASTWEEK&User=VL%20CUIC%5Cadministrator</gadget>
```

'~loginId~' and '~teams~' work as place-holders in the filter criteria:

'~loginId~' is replaced with the logged in user Id.

'~teams~' is replaced with the teams that the logged in user supervises.

Examples:

```
https://my-cuic-server:8444/cuic/gadget/Historical/HistoricalGadget.jsp?viewId=
BD9A8B7DBE714E7EB758A9D472F0E7DC&linkType=htmlType&viewType=Grid&refreshRate=900&@start_date=
RELDATE%20THISWEEK&@end_date=RELDATE%20THISWEEK&@agent_list=CL%20~teams~&gadgetHeight=360
```

```
https://my-cuic-server:8444/cuic/gadget/Historical/HistoricalGadget.jsp?viewId=
BD9A8B7DBE714E7EB758A9D472F0E7DC&linkType=htmlType&viewType=Grid&refreshRate=900&@start_date=
RELDATE%20THISWEEK&@end_date=RELDATE%20THISWEEK&@agent.id=~loginId~
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

## Live Data
                        	 Failover

Live Data reports
                              		  can be viewed as gadgets in the Cisco Finesse desktop and on the report viewer
                              		  in Unified Intelligence Center. Live Data failover occurs when any of the
                              		  following fails:

Live Data
                                    				Socket.IO Service

Network
                                    				Connectivity

Live Data Web
                                    				Service

Unified CCE Live Data NGINX Service

“Live Data is not availab le after repeated attempts. Retrying” message is displayed during failover when the gadget and the report viewer aren’t able to connect to the primary and secondary
                              Live Data server. The gadget and Unified Intelligence Center continue to retry until it connects to one of the servers and
                              regain updates to the reports.

The Live Data gadget fails to load if the Intelligence Center Reporting Service is unavailable when the Live Data gadget is
                              being rendered. If the service is unavailable after the gadget is rendered, it has no effect. By configuring the alternateHosts attribute to have a fallback Cisco Unified Intelligence Center VM host name, you can achieve failover for the Intelligence
                              Center Reporting Service. For more information, see the alternateHosts Configuration section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

## Gadget Toolbar Improvements

Cisco Unified Intelligence Center provides you with a toolbar on Live Data reporting gadget on the Cisco Finesse Desktop.

You can remove this toolbar by configuring the parameter hideGadgetToolbar to true in the gadget URL.

For example: <gadget>https:// my-cuic-server :8444/cuic/gadget/LiveData/LiveDataGadget. xml ?gadgetHeight= 150& hideGadgetToolbar=true &viewId=EF94123F10000164000000FD0A6B2D41&filterId= AgentCallLogDetailStats.agentID=loginId</gadget>

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

| Step 1 | Retrieve the existing gadget configuration for "Agent Skill Group" report from the desktop layout: <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp ?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL</gadget> |
|---|---|
| Step 2 | Run the Agent Skill Group live data report in Unified Intelligence Center and click the Field Filters tab. |
| Step 3 | Copy the Field Filter name to add to the existing filter criteria and assign the filter value as illustrated in the following
                                       syntax: <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget. jsp?gadgetHeight=310&viewId=9AB7848B10000141000001C50A0006C4&filterId=agent.id=CL &compositeFilterId=agent.agentMRDs.mrDomainID=<mrdomainId> </gadget> Where, filterId is for basic filter criteria. Note 'loginId' and 'teamName' work as place-holders in the filterId parameter: 'loginId' is replaced with the logged in user Id. 'teamName' is replaced with the team that the logged in user belongs to. compositeFilterId is for Advanced filtering. agent.id and agent.agentMRDs.mrDomainID are the keys to identify the filter field names. CL is the value for agent.id to identify all the collections on which agent.id has permissions. mrdomainId is the value for the key agent.agentMRDs.mrDomainID to filter on the given mrdomainId by replacing the tag <mrdomainId> in
                                                the above URL. Ensure to: Replace <my-cuic-server> with the FQDN of the Cisco Unified Intelligence Center server. Use HTTPS based on how the Cisco Finesse desktop is being accessed. Replace <mrdomainId> with the appropriate mrdid. Note If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_1=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> Note If the agent's or supervisor's password is changed, it takes 20 to 40 minutes to load the Cisco Unified Intelligence Center
                                                      gadgets properly for that user. | Note | 'loginId' and 'teamName' work as place-holders in the filterId parameter: 'loginId' is replaced with the logged in user Id. 'teamName' is replaced with the team that the logged in user belongs to. | Note | If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_1=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> | Note | If the agent's or supervisor's password is changed, it takes 20 to 40 minutes to load the Cisco Unified Intelligence Center
                                                      gadgets properly for that user. |
| Note | 'loginId' and 'teamName' work as place-holders in the filterId parameter: 'loginId' is replaced with the logged in user Id. 'teamName' is replaced with the team that the logged in user belongs to. |
| Note | If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_1=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> |
| Note | If the agent's or supervisor's password is changed, it takes 20 to 40 minutes to load the Cisco Unified Intelligence Center
                                                      gadgets properly for that user. |

| Note | 'loginId' and 'teamName' work as place-holders in the filterId parameter: 'loginId' is replaced with the logged in user Id. 'teamName' is replaced with the team that the logged in user belongs to. |
|---|---|

| Note | If the filter is associated with a value list (example in the above URL), <mrdomainId> can be replaced with CL to consider
                                                            all the collections of the value list in the following syntax: compositeFilterId=agent.agentMRDs.mrDomainID=CL This example is for illustration purpose only. (As mrdomainId cannot be associated with a value list based on existing 'Agent
                                                            Skill Group' stock report.) For configuring multiple views in the gadget, use viewId, filterId and compositeFilterId parameters with numbering in the
                                                            gadget URL like: viewId_{1...5}, filterId_{1...5}, compositeFilterId_{1...5} <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp? gadgetHeight=310&viewId_1=9AB7848B10000141000001C50A0006C4&
                                                               filterId_1=agent.id=CL&compositeFilterId_1=agent.agentMRDs.mrDomainID=1& viewId_2=99E6C8E210000141000000D80A0006C4&filterId_2=agent.id=CL%20teamName&
                                                               compositeFilterId_1=agent.agentMRDs.mrDomainID=1<mrdomainId></gadget> |
|---|---|

| Note | If the agent's or supervisor's password is changed, it takes 20 to 40 minutes to load the Cisco Unified Intelligence Center
                                                      gadgets properly for that user. |
|---|---|

| Note | In Enterprise deployment ( Unified CCE and Packaged CCE ), Cisco Unified Intelligence Center Historical reporting gadget is available out of the box on Cisco Finesse Supervisor desktop
                                          only and is not supported on Agent desktop. For Historical Gadgets, only one view is supported. |
|---|---|

| Note | Cisco Unified Intelligence Center historical report as a gadget does not support grouping and drill-downs in Cisco Finesse
                                          desktop. |
|---|---|

| Note | If an agent's or supervisor's password is changed, it takes 20 to 40 minutes to load the Cisco Unified Intelligence Center
                                          gadgets properly for that user. |
|---|---|

| Note | '~loginId~' and '~teams~' work as place-holders in the filter criteria: '~loginId~' is replaced with the logged in user Id. '~teams~' is replaced with the teams that the logged in user supervises. Examples: https://my-cuic-server:8444/cuic/gadget/Historical/HistoricalGadget.jsp?viewId=
BD9A8B7DBE714E7EB758A9D472F0E7DC&linkType=htmlType&viewType=Grid&refreshRate=900&@start_date=
RELDATE%20THISWEEK&@end_date=RELDATE%20THISWEEK&@agent_list=CL%20~teams~&gadgetHeight=360 https://my-cuic-server:8444/cuic/gadget/Historical/HistoricalGadget.jsp?viewId=
BD9A8B7DBE714E7EB758A9D472F0E7DC&linkType=htmlType&viewType=Grid&refreshRate=900&@start_date=
RELDATE%20THISWEEK&@end_date=RELDATE%20THISWEEK&@agent.id=~loginId~ |
|---|---|

| Note | You can retrieve this information from any report permalink. |
|---|---|

| Note | If the parameter hideGadgetToolbar is unavailable in the gadget URL or if it is set to false, then the toolbar is displayed
                                       by default. |
|---|---|

| Note | For Historical Gadgets, only one view is supported. To add a new report to the Reports View Selector, contact the Cisco Finesse Administrator. |
|---|---|

| Note | When the button is paused and updates are available on the gadget, a notification appears over the pause or play button. |
|---|---|