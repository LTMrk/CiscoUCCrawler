---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-report-614cd87182
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_Reporting-User-Guide-12_6_1/pcce_b_cisco-packaged-contact-center-enterprise_chapter_010.html
retrieved_at: 2026-08-21T16:53:29.740559+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 10, 2021

Chapter: Custom and Stock Report Templates

## Chapter: Custom and Stock Report Templates

# Custom and Stock Report Templates

## Stock
                        	 Reports

The following Cisco
                           		Unified Intelligence Center report bundles are available as downloads from
                           		Cisco.com https://software.cisco.com/download/type.html?mdfid=282163829&catid=null .
                           		Click the Intelligence
                              		  Center Reports link to view all available report bundles:

Realtime and
                                 			 Historical Transitional templates - Introductory templates designed for new
                                 			 users. These templates are simplified versions of the All Fields templates, and
                                 			 are similar to templates available in other contact center solutions.

Realtime and
                                 			 Historical All Fields templates - Templates that provide data from all fields
                                 			 in a database. These templates are most useful as a basis for creating custom
                                 			 report templates.

Live Data
                                 			 templates - Templates that provide up to the moment data for contact center
                                 			 activity.

Realtime and
                                 			 Historical Outbound templates - Templates for reporting on Outbound Option
                                 			 activity. Import these templates if your deployment includes Outbound Option.

Enterprise Chat and
                                       						Email - Templates for reporting on Enterprise Chat and
                                       						Email activity. Include these templates if your deployment includes Enterprise Chat and
                                       						Email .

Cisco Unified
                                 			 Intelligence Center Admin Security templates - Templates to report on Cisco
                                 			 Unified Intelligence Server audit trails, permissions, and template ownership.

Additionally,
                           		sample custom report templates are available from the Cisco Developer Network
                           		( https://developer.cisco.com/site/reporting/overview/ ), and include templates for
                           		Cisco Unified Customer Voice Portal (Unified CVP).

When downloading
                           		report template bundles, select bundles for the version of software deployed in
                           		your contact center.

For information on
                           		importing report bundles, see the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-install-and-upgrade.html .

## Report Summary
                        	 Rows

Many reports have one Summary row or several Summary rows. These summaries are enabled in the Grouping page of the grid editor
                              and show the footer values for the fields. You configure these values in the footer for each report column in the Report Definition.

These footer
                              		  values can be:

None (blank)

Footer values
                                    				can be blank, when a summary metric is not applicable or it is not logical to
                                    				summarize the value when the data is null, and for intervals in certain call
                                    				type reports, which are configured values.

Avg (average
                                    				of all items in the column)

Examples are
                                    				percentages and the average length of time associated with the value the column
                                    				represents.

Sum (total of
                                    				the values in the column)

Count (total
                                    				of all items in the column)

Min (minimum
                                    				value in the column)

Max (maximum
                                    				value in the column)

Custom
                                    				(calculation derived from a custom formula that was applied to the footer
                                    				value)

## Customize Report
                        	 Templates

You can modify
                           		existing report templates or create custom reports templates if you determine
                           		that the stock report templates do not meet your reporting needs. For example,
                           		you might customize an existing report template to monitor a department's
                           		activity and performance by creating a collection with objects from only that
                           		department.

See the Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/en/US/products/ps9755/tsd_products_support_series_home.html for directions on customizing report templates.