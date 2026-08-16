---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-212291-troubleshoot-cuic-dashboard-53398bbe97
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/212291-troubleshoot-cuic-dashboard-widget-unexp.html
retrieved_at: 2026-08-16T19:25:29.933071+00:00
---

Troubleshoot CUIC Dashboard Widget Unexpected Changes After an Upgrade to Version 11.6

# Troubleshoot CUIC Dashboard Widget Unexpected Changes After an Upgrade to Version 11.6

Updated: November 2, 2017

Document ID: 212291

Contents

## Contents

## Introduction

This document describes how to troubleshoot Cisco Unified Intellegence Center (CUIC) dashboard widget unexpected changes after an upgrade to 11.6 version.

## Troubleshoot CUIC Dashboard Widget Changes After an Upgrade to Version 11.6

After CUIC server upgrade to version 11.6 unsupported dashboard widgets disappear.

In order to troubleshoot the issue determine the type of the widget that disappeared.

If the widget is of a no longer supported type rollback CUIC server to the previous version and determine all of the widgets that are not supported in CUIC 11.6.

You can use article  to get the list of unsupported widgets.

Change CUIC widget configuration to avoid unsupported widgets loss after the upgrade.

### List of Unsupported Dashboard Widget Types

These unsupported dashboard widgets are dropped after CUIC server upgrade:

- Widgets with schedule type

- Widgets of URL type with dashboard permalink (nested dashboard)

- Widgets placed beyond dashboard canvas size limit

Warning : These unsupported widgets are dropped without any indication in CUIC logs.

These dashboard widgets are affected by CUIC server upgrade:

- Excel and XML Permalinks Type Widget

- Dashboard with More Than 10 Widgets

### Schedule Widget

After CUIC server upgrade to version 11.6 all scheduled type dashboard widgets are no longer supported and they are automatically removed.

### URL Widget with Dashboard Permalink (Nested Dashboard)

After CUIC server upgrade to version 11.6 all widgets with nested dashboards are no longer supported and they are automatically removed.

### Widget Placed Beyond New Dashboard Canvas Size Limit

After CUIC server upgrade to version 11.6 a ll widgets that cross canvas size limit are no longer supported and they are automatically removed.

### Excel and XML Permalinks Type Widget

After CUIC server upgrade to version 11.6 all dashboard widgets with excel and XML type permalinks will be converted to HTML permalinks.

In the CUIC Reporting logs these messages are generated. They are very descriptive and reveal dashboard and widget names.

```
0000000053: 10.48.47.142: Aug 22 2017 16:20:22.241 +0200: %CCBU___________CUIC-4-WARN: Dashboard Migration : Weburl widget : Dashboard : case4_excel_xml_permalink Widget : url_permlnk_excel Widget url : https://cuic11.allevich.local:8444/cuic/permalink/PermalinkViewer.htmx?viewId=ED4BBBF710000155000001300A302F8E&linkType=excelType - Converting excel-xml permalink to html permalink. 0000000054: 10.48.47.142: Aug 22 2017 16:20:22.242 +0200: %CCBU___________CUIC-4-WARN: Dashboard Migration : Weburl widget : Dashboard : case4_excel_xml_permalink Widget : url_permlnk_xml Widget url : https://cuic11.allevich.local:8444/cuic/permalink/PermalinkViewer.htmx?viewId=ED4BBBF710000155000001300A302F8E&linkType=xmlType&viewType=Grid - Converting excel-xml permalink to html permalink. 0000000055: 10.48.47.142: Aug 22 2017 16:20:22.435 +0200: %CCBU___________CUIC-4-WARN: Dashboard Migration : Weburl widget : Dashboard : SR681697619_Allianz_report_TO Widget : dashbrd_rt_rpt7_link Widget url : http://cuic11.allevich.local:8081/cuic/permalink/PermalinkViewer.htmx?viewId=36A441C91000015A00000CD40A302F8E&linkType=htmlType&viewType=Grid&refreshRate=15&widgetId=36A5A2361000015A00000D170A302F8E&uuid=601b78c6-2764-431c-a28f-e2f7a2913294&widgetId=36A5A2361000015A00000D170A302F8E&uuid=null - Converting variable permalink to html permalink. 0000000056: 10.48.47.142: Aug 22 2017 16:20:22.436 +0200: %CCBU___________CUIC-4-WARN: Dashboard Migration : Weburl widget : Dashboard : SR681697619_Allianz_report_TO Widget : dashbrd_rt_rpt8_link Widget url : http://cuic11.allevich.local:8081/cuic/permalink/PermalinkViewer.htmx?viewId=36A6398E1000015A00000DA90A302F8E&linkType=htmlType&viewType=Grid&refreshRate=15&widgetId=36A8E7331000015A00000E4E0A302F8E&uuid=null - Converting variable permalink to html permalink. 0000000057: 10.48.47.142: Aug 22 2017 16:20:22.436 +0200: %CCBU___________CUIC-4-WARN: Dashboard Migration : Weburl widget : Dashboard : SR681697619_Allianz_report_TO Widget : dashbrd_rt_rpt9_link Widget url : http://cuic11.allevich.local:8081/cuic/permalink/PermalinkViewer.htmx?viewId=36AB40401000015A00000E640A302F8E&linkType=htmlType&viewType=Chart - Converting variable permalink to html permalink.
```

### Dashboard with More Than 10 Widgets

After CUIC server upgrade to version 11.6 all dashboards with more than 10 widgets are preserved, but you cannot make changes to them.

If you try to make changes on a dashboard with more than 10 widgets after an upgrade you will get an error "Dashboard edit failed. Please try again".

In the CUIC Reporting logs these messages are generated.

```
0000028566: 10.48.47.142: Aug 23 2017 14:39:28.498 +0200: %CCBU_CUIC_DATA_PROCESSING-7-HIBERNATE_SESSION_INTERCEPTOR: %[ARGUMENT=null][MARKER=END][MARKER=END][METHOD=preHandle]: Hibernate Session Interceptor 0000028567: 10.48.47.142: Aug 23 2017 14:39:28.499 +0200: %CCBU_CUIC_DATA_PROCESSING-7-DAO_GET_BY_ID: %[ARGUMENT=1111111111111111111111111111AAAA][MARKER=START][TARGET_CLASS=com.cisco.ccbu.cuic.objectmodel.security.CuicUserImpl]: Dao getById() to retrieve the specified object 0000028568: 10.48.47.142: Aug 23 2017 14:39:28.499 +0200: %CCBU_CUIC_DATA_PROCESSING-7-DAO_GET_BY_ID: %[ARGUMENT=1111111111111111111111111111AAAA][MARKER=END][TARGET_CLASS=com.cisco.ccbu.cuic.objectmodel.security.CuicUserImpl]: Dao getById() to retrieve the specified object 0000000060: 10.48.47.142: Aug 23 2017 14:39:28.513 +0200: %CCBU_CUIC_MODEL_OBJECTS-0-ERROR: <- CuicDashboardRESTProvider.java:338 Maximum number of widgets allowed on a dashboard is {0} 0000028569: 10.48.47.142: Aug 23 2017 14:39:28.516 +0200: %CCBU_CUIC_DATA_PROCESSING-7-HIBERNATE_SESSION_INTERCEPTOR: %[ARGUMENT=null][MARKER=START][MARKER=START][METHOD=postHandle]: Hibernate Session Interceptor 0000028570: 10.48.47.142: Aug 23 2017 14:39:28.516 +0200: %CCBU_CUIC_DATA_PROCESSING-7-HIBERNATE_SESSION_INTERCEPTOR: %[ARGUMENT=null][MARKER=RETRIEVE_HTTPSESSION][MARKER=START][METHOD=postHandle]: Hibernate Session Interceptor 0000028571: 10.48.47.142: Aug 23 2017 14:39:28.516 +0200: %CCBU_CUIC_DATA_PROCESSING-7-HIBERNATE_SESSION_INTERCEPTOR: %[ARGUMENT=org.apache.catalina.session.StandardSessionFacade@963aa2][MARKER=RETRIEVE_HTTPSESSION][MARKER=END][METHOD=postHandle]: Hibernate Session Interceptor 0000028572: 10.48.47.142: Aug 23 2017 14:39:28.516 +0200: %CCBU_CUIC_DATA_PROCESSING-7-HIBERNATE_SESSION_INTERCEPTOR: %[ARGUMENT=SessionImpl(PersistenceContext[entityKeys=[EntityKey[com.cisco.ccbu.cuic.objectmodel.security.CuicGroupImpl#2222222222222222222222222222BBBB], EntityKey[com.cisco.ccbu.cuic.objectmodel.security.CuicUserImpl#1111111111111111111111111111AAAA]],collectionKeys=[CollectionKey[com.cisco.ccbu.cuic.objectmodel.security.CuicGroupMemberAbstract.parentGroups#2222222222222222222222222222BBBB], CollectionKey[com.cisco.ccbu.cuic.objectmodel.security.CuicGroupMemberAbstract.parentGroups#1111111111111111111111111111AAAA], CollectionKey[com.cisco.ccbu.cuic.objectmodel.security.CuicGroupImpl.groupMembers#2222222222222222222222222222BBBB], CollectionKey[com.cisco.ccbu.cuic.objectmodel.security.CuicUserImpl.favorites#1111111111111111111111111111AAAA]]];ActionQueue[insertions=[] updates=[] deletions=[] collectionCreations=[] collectionRemovals=[] collectionUpdates=[]])][MARKER=CURRENT_SESSION][MARKER=INFO][METHOD=postHandle]: Hibernate Session Interceptor
```

Use this command to isolate the problem with 10 widgets limit.

```
admin: file search activelog /cuic/logs/cuic/CCBU-cuic.2017-08-22T16-19-54.610.startup.log "Maximum number of widgets allowed on a dashboard" Searching file: /var/log/active//cuic/logs/cuic/CCBU-cuic.2017-08-22T16-19-54.610.startup.log 0000000059: 10.48.47.142: Aug 23 2017 14:38:40.728 +0200: %CCBU_CUIC_MODEL_OBJECTS-0-ERROR: <- CuicDashboardRESTProvider.java:338Maximum number of widgets allowed on a dashboard is {0} 0000000060: 10.48.47.142: Aug 23 2017 14:39:28.513 +0200: %CCBU_CUIC_MODEL_OBJECTS-0-ERROR: <- CuicDashboardRESTProvider.java:338Maximum number of widgets allowed on a dashboard is {0}
```

## Related Information

### Revision History

1.0

07-Nov-2017

Initial Release

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Nov-2017 | Initial Release |