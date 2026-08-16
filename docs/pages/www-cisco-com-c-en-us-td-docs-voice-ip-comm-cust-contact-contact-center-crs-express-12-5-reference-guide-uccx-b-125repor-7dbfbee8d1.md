---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-reference-guide-uccx-b-125repor-7dbfbee8d1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/reference/guide/uccx_b_125report-developers-guide/uccx_b_125report-developers-guide_chapter_01.html
retrieved_at: 2026-08-16T21:04:08.057348+00:00
---

Cisco Unified Contact Center Express Report Developer Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Report Developer Guide, Release 12.5(1)

## Results

Updated: February 7, 2020

Chapter: Introduction

## Chapter: Introduction

- Introduction

- Overview

- Common                              	 Terms

# Introduction

## Overview

Cisco Unified Intelligence Center is a reporting platform for users of Cisco Contact Center products. It is a web-based application that provides Historical,
                           Real-time, and Live Data reporting and dashboards.

Unified Intelligence Center serves the following primary purposes:

Obtains data from the base solution's database. The base solution can be any of the Contact Center products.

Allows you to create custom queries to obtain specific data.

Customizes the visual presentation of the reports.

Customizes the data presented in the reports.

Allows different groups of people to view specific data based on their roles.

As a reporting user, you can use the new Unified Intelligence Center page to perform the following tasks:

Create, edit, and manage Dashboards.

Create, edit, run, and manage Reports.

Filter data in a report.

View permalink for Dashboards and Reports.

Set sharing permissions for Dashboards and Reports.

Select locale for the Unified Intelligence Center .

Search for Dashboard and Report.

Mark Dashboards and Reports as favorites.

View the personal list of favorites for Dashboards and Reports.

Schedule reports to run at selected intervals.

Creating and viewing;

Report Definitions

Data Sources

Value Lists and Collections

Users and Permissions (Security)

## Common
                        	 Terms

### Data
                              		  Source

Data source defines the
                              		  sources that contain data for the report. Unified Intelligence Center supports
                              		  two types of data sources: IBM Informix (Historical Reports) and Streaming
                              		  (Live-Data Reports). Data sources are preconfigured for you.

Additional
                                             				data sources are not supported.

### Report
                              		  Definition

Each report has a
                              		  report definition that represents how data is retrieved from the data source
                              		  for that report template. In addition, a report definition contains the dataset
                              		  that is obtained. This includes the fields, filters, formulas, refresh rate,
                              		  and key criteria field for the report.

### Reports

Reports show data returned by
                              		  Report Definitions. This data is extracted by database queries.

### Stock
                              		  Report

Report that is
                              		  pre-bundled in Unified Intelligence Center.

### Report Views

A report can be presented in
                              		  multiple formats like a grid, chart, or a graph and gauge. Each view can have
                              		  its own set of fields. A single report can have multiple views.

### Report Help

You can attach a help page
                              		  specifically for your report.

| Note | Additional
                                             				data sources are not supported. |
|---|---|