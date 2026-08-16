---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--d1f5518dfe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/reporting-concepts-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/reporting-in-unified-cce.html
retrieved_at: 2026-08-16T20:41:10.742058+00:00
---

Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

# Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

Updated: June 27, 2023

Chapter: Reporting in Unified CCE

## Chapter: Reporting in Unified CCE

# Reporting in Unified CCE

## Overview

Cisco Unified Intelligence Center is a reporting platform for users of Cisco Contact Center products. It is a web-based application that provides Historical,
                           Real-time, and Live Data reporting and dashboards.

Unified Intelligence Center serves the following primary purposes:

Obtains data from the base solution's database. The base solution can be any of the Contact Center products.

Allows you to create custom queries to obtain specific data.

Customizes the visual presentation of the reports.

Customizes the report data.

Allows different groups of people to view specific data based on their roles.

### Customer Journey Analyzer

Unified Intelligence Center users can use the reporting platform to launch Customer Journey Analyzer using Analyzer from the left navigation pane.

You can customize the default Analyzer URL using the CLI set cuic analyzer url <urlname> .

For more information on the CLI, see Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

The Customer Journey Analyzer mines historical data from multiple data sources and systems to generate specific business views of data. The Analyzer visually
                              displays trends to help you identify patterns and gain insight for continuous improvement.

You must have completed the on boarding process for Cloud Connect to access Customer Journey Analyzer . Cloud Connect allows Cisco Contact Center on premises customers to connect to cloud services, such as Customer Journey Analyzer to use Business Metrics.

For more information, see Business Metrics related information in Cisco Unified Contact Center Express Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html

For more information, see Business Metrics related information in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

## Access Unified Intelligence Center

The URL for logging in to the Unified Intelligence Center reporting application is :

HTTPS

https://<HOST>:8444/cuicui/Main.jsp

Where HOST is the DNS name of a Unified Intelligence Center node.

Cisco Unified Intelligence Center does not support HTTP.

Cisco Unified Intelligence Center , Release 12.6(1) supports custom logon message for users. If your administrator has defined the custom logon messages, then
                              the message is displayed in the Sign In page.

Custom logon messages are not displayed to users signing in with SSO.

## Stock
                        	 Reports

The following report
                           		bundles are available as stock reports for Cisco Unified Intelligence Center:

Realtime and
                                 			 Historical Transitional templates - Introductory templates designed for new
                                 			 users. These templates are simplified versions of the All Fields templates, and
                                 			 are similar to templates available in other contact center solutions.

Realtime and
                                 			 Historical All Fields templates - Templates that provide data from all fields
                                 			 in a database. These templates are most useful as a basis for creating custom
                                 			 reports, and include templates for precision queue routing data.

Realtime and
                                 			 Historical Outbound templates - Templates for reporting on Outbound Option
                                 			 activity. Import these templates if your deployment includes Outbound Option.

Live Data templates - Templates for reports that use the Live Data stream processing system as a data source. Refresh rates
                                 for these reports are much faster than the Realtime or Historical reports--usually less than every 3 seconds. Reports are
                                 available for Agent, Agent Skill Group, Precision Queue, Skill Group, Recent State History and Recent Call History.

Contact Sharing
                                 			 templates - Templates for reporting on a Contact Sharing system. You can use
                                 			 the Contact Sharing reports to understand the current configuration and
                                 			 behavior of the Contact Sharing system. You can view data on the active
                                 			 configuration of the Contact Sharing routing, the number of calls routed to
                                 			 each target system for each group, and the calls that have errors during the
                                 			 routing process.

Cisco Unified
                                 			 Intelligence Center Admin Security templates - Templates to report on Cisco
                                 			 Unified Intelligence Server audit trails, permissions, and template ownership.

License Consumption Report - Use this report to monitor the agent
                                 			 license consumption and other related ports such as the VRU-IVR ports and the
                                 			 outbound dialer ports. It helps you ascertain the number of licenses you must
                                 			 procure to cover the peak or maximum license usage during the license agreement
                                 			 period.

The report bundles are available as downloads from Cisco.com. Click the Intelligence Center Reports link on the downloads page ( https://software.cisco.com/download/type.html?mdfid=282163829&catid=null ). Depending on how it was deployed, your installation of Unified Intelligence Center may include all or a subset of these
                           reports.

For information on importing report bundles or custom reports, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/prod_installation_guides_list.html . Navigate to Initial Configuration>Configure Cisco Unified Intelligence Center>Import Report Bundles.

## Customize Report
                        	 Templates

You can modify
                           		existing report templates or create custom reports templates if you determine
                           		that the stock report templates do not meet your reporting needs. For example,
                           		you might customize an existing report template to monitor a department's
                           		activity and performance by creating a collection with objects from only that
                           		department.

See the Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/en/US/products/ps9755/tsd_products_support_series_home.html for directions on customizing report templates.

| Note | You must have completed the on boarding process for Cloud Connect to access Customer Journey Analyzer . Cloud Connect allows Cisco Contact Center on premises customers to connect to cloud services, such as Customer Journey Analyzer to use Business Metrics. |
|---|---|

| Note | Cisco Unified Intelligence Center does not support HTTP. |
|---|---|

| Note | Custom logon messages are not displayed to users signing in with SSO. |
|---|---|