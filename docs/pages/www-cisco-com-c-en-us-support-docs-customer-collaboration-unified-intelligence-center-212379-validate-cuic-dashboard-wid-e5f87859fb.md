---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-212379-validate-cuic-dashboard-wid-e5f87859fb
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/212379-validate-cuic-dashboard-widgets-before-a.html
retrieved_at: 2026-08-16T19:25:42.638846+00:00
---

Validate CUIC Dashboard Widgets Before an Upgrade

# Validate CUIC Dashboard Widgets Before an Upgrade

Updated: October 23, 2017

Document ID: 212379

Contents

## Contents

## Introduction

This document describes additional validation procedure for Cisco Unified Intelligence Center (CUIC) server upgrade to version 11.6. It contains a set of database queries that list unsupported dashboard widgets to be dropped after the upgrade.

## Prerequisites

### Components Used

The information in this document is based on CUIC version 11.5.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

After Cisco Unified Intelligence Center server upgrade from previous versions to 11.6 version all unsupported dashboard widgets are discarded without explicit notification to the system administrator. In order to prevent loss of the widgets the document suggests and provide guidance on how to validate the existing widgets.

Note : A valid backup ensures that all of the configuration can be restored, so it is always recommended to take a backup before an upgrade.

## Solution

### Schedule Widget

Use this SQL query to list all dashboards with scheduled type widgets.

Note : All the lines of the query in bold font must be entered to get the output. The backslash character is used for better query presentation.

```
admin: run sql SELECT dw.parentdashboardid,d.name dashboard,dw.name widget \ FROM cuic_data:cuicdashboardwidget dw \ INNER JOIN cuic_data:cuicdashboard d \ ON d.id=dw.parentdashboardid \ WHERE widgettype='SCHEDU' parentdashboardid                dashboard                       widget ================================ =============================== ================== 09BCDE8D1000015E0000005A0A302F8E case1_validate_scheduled_widget scheduled_widget_1
```

The widgets of this type are unsupported in CUIC version 11.6 and are discarded after the upgrade.

### URL Widget with Dashboard Permalink

URL widgets with a permalink to another dashboard are called nested dashboards.

The widgets of this type are unsupported in CUIC version 11.6 and are discarded after the upgrade.

This article does not have specific SQL queries to list dashboards and widgets of this type.

### Widget that Exceeds Dashboard Canvas Size Limit

The widgets of this type are unsupported in CUIC version 11.6 and are discarded after the upgrade.

This article does not have specific SQL queries to list dashboards and widgets of this type.

### Excel and XML Permalink Widget Type

Use this SQL query to list all dashboards and widgets with XML and Excel types of permalinks.

```
admin: run sql SELECT dw.parentdashboardid,d.name dashboard,dw.name widget \ FROM cuic_data:cuicdashboardwidget dw \ INNER JOIN cuic_data:cuicdashboard d \ ON d.id=dw.parentdashboardid \ WHERE url LIKE '%linkType=excelType%' OR url LIKE '%linkType=xmlType%' parentdashboardid                dashboard                 widget ================================ ========================= ================= 09C13E6A1000015E0000006F0A302F8E case4_excel_xml_permalink url_permlnk_xml 09C13E6A1000015E0000006F0A302F8E case4_excel_xml_permalink url_permlnk_excel
```

After CUIC server upgrade to version 11.6 all dashboard widgets with excel and XML type permalinks will be converted to HTML permalinks.

### Dashboard with 11 Widgets or more

Use this SQL query to list all dashboard that has more than 10 widgets associated.

```
admin: run sql SELECT dw.parentdashboardid,d.name dashboard,COUNT(dw.parentdashboardid)AS widget_count \ FROM cuic_data:cuicdashboardwidget dw \ INNER JOIN cuic_data:cuicdashboard d \ ON d.id=dw.parentdashboardid \ GROUP BY parentdashboardid,d.name \ HAVING 10<COUNT(parentdashboardid) parentdashboardid                dashboard            widget_count ================================ ==================== ============ 09A902BB1000015E000000070A302F8E case5_10plus_widgets 12
```

After CUIC server upgrade to version 11.6 all dashboards with more than 10 widgets are preserved, but you cannot make changes to them.

### Revision History

1.0

25-Oct-2017

Initial Release

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-Oct-2017 | Initial Release |