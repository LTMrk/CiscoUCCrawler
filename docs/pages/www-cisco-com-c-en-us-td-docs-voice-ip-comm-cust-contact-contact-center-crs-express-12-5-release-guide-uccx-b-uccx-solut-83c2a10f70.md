---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-release-guide-uccx-b-uccx-solut-83c2a10f70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/release/guide/uccx_b_uccx-solution-release-notes-125/uccx_b_uccx-solution-release-notes-125_chapter_0110.html
retrieved_at: 2026-08-16T21:01:53.272419+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1)

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1)

Updated: January 31, 2020

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

# Cisco Unified Intelligence Center

## New Features

### CUIC CORS Enablement

In this release, an administrator can perform the following actions for Cross-Origin Resource Sharing (CORS) on Unified Intelligence
                              Center:

Enable, disable, and view CORS status

Add, delete, and list the allowed headers

Add, delete, and list the exposed headers

Add, delete, and list the allowed origin URLs

For more information, see Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

### Report Definition Feature

This release includes CUIC Premium License in Unified CCX, which enables the Report Definition feature in Cisco Unified Intelligence
                              Center for Unified CCX. For more information, see Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/en/US/products/ps9755/products_user_guide_list.html .

## Updated Features

### User Role Changes

When you modify the user account information of a user who is currently signed in, that user gets signed out  automatically.

When the signed in user is in the Run As mode of another user, modifying the user account information of either of the users
                                    stops the Run As mode.

### Enable or Disable Custom Widgets in Dashboards

In this release, to address injection vulnerabilities, the Custom Widget feature in Dashboards is disabled by default. If any custom widgets were added to the Dashboards in versions earlier to Unified Intelligence Center 12.5, those widgets are visible in the read-only mode post upgrade to
                              version 12.5. You can opt to retain or delete them.

An administrator can enable or disable the Custom Widget feature using the set cuic properties dashboard-customwidget-enabled CLI.

For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

## Important Notes

### Security Enhancements

To secure the communication between standalone Cisco Unified Intelligence Center and Unified CCX, you must import the following
                              security certificates (unapproved CA signed certificate or self-signed certificate):

The standalone Cisco Unified Intelligence Center certificate to Unified CCX.

The Unified CCX certificate to standalone Cisco Unified Intelligence Center.

For information about adding a certificate, see Insert a new tomcat-trust certificate .

### Large Schedules Frequency on Upgrade

After upgrade to Unified Intelligence Center version 12.5, all large schedules with frequency more than once per day will
                              be converted to run only once per day.

### Report Thresholds - Image Location

This release supports only image URLs that are reachable from Unified Intelligence Center server. Maximum size limit that
                              is allowed for an image is 5MB.

### Install Language ES

After successful install or upgrade, if you want to use the Cisco Unified Intelligence Center interface in a language other
                              than English, you have to download and install the language pack ES.

## Deprecated Features

### Internet Explorer 11

In this release, Internet Explorer version 11 is deprecated. Edge Chromium (Microsoft
                              Edge v79 and later) is the replacement.

## Removed and Unsupported Features

### HTTP Support for Unified Intelligence Center

In this release, the HTTP support for Unified Intelligence Center has been removed. The users can now securely communicate
                              to Unified Intelligence Center over HTTPS.

The following CLIs are removed from Unified Intelligence Center release 12.5:

show cuic properties http-enabled

set cuic properties http-enabled

show cuic properties hsts

set cuic properties hsts on [max-age value in seconds]

set cuic properties hsts off

### Authenticated Excel Permalink on Office 365

Authenticated Excel report permalink is not supported on Office 365.

## Third Party Software Impacts

None.