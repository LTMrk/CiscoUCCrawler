---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-solution-release-notes-html-index--0c6e9337c0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Solution_Release_Notes/html/index/Cisco-Unified-Intelligence-Center-for-HCS-for-Contact-Center-for-Release-12-5-1.html
retrieved_at: 2026-08-21T23:56:28.495097+00:00
---

Release Notes for Cisco Hosted Collaboration Solution for Contact Center Solution, Release 12.5(1)

# Release Notes for Cisco Hosted Collaboration Solution for Contact Center Solution, Release 12.5(1)

Updated: January 23, 2024

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

A new Service Update (SU) release is available for Cisco Unified Intelligence Center 12.5(1). You can perform a fresh installation or upgrade to Cisco Unified Intelligence Center 12.5(1) SU on supported virtual machines from previous versions. For more information, see the ReadMe .

## New Features

- Edge Chromium Browser Support

- User Experience Changes

- CUIC CORS Enablement

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge). For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### User Experience Changes

This release provides an improved user experience to configure, edit, and manage the following Administration Console entities:

User Management

Device Configuration

Log and Trace Settings

Control Center Management

Cluster Configuration

Tools Management

For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

### CUIC CORS Enablement

In this release, an administrator can perform the following actions for Cross-Origin Resource Sharing (CORS) on Unified Intelligence Center:

Enable, disable, and view CORS status

Add, delete, and list the allowed headers

Add, delete, and list the exposed headers

Add, delete, and list the allowed origin URLs

For Unified Intelligence Centre gadgets (Live Data and Historical) to load in Cisco Finesse, you must:

Enable CORS using the utils cuic cors enable command.

Set the Finesse host URL in the utils cuic cors allowed_origin add URLs command.

For Live Data gadgets, in addition to the above settings, ensure to enable CORS using the utils live-data cors enable command and set the Finesse host URL in the utils live-data cors allowed_origin add URLs command. For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

## Updated Features

- User Role Changes

- Enable or Disable Custom Widgets in Dashboards

### User Role Changes

When you modify the user account information of a user who is currently signed in, that user gets signed out automatically.

When the signed in user is in the Run As mode of another user, modifying the user account information of either of the users stops the Run As mode.

### Enable or Disable Custom Widgets in Dashboards

In this release, to address injection vulnerabilities, the Custom Widget feature in Dashboards is disabled by default. If any custom widgets were added to the Dashboards in versions earlier to Unified Intelligence Center 12.5, those widgets are visible in the read-only mode post upgrade to version 12.5. You can opt to retain or delete them.

An administrator can enable or disable the Custom Widget feature using the set cuic properties dashboard-customwidget-enabled CLI.

For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

## Important Notes

### Access Administration Console

The URL to access the Administration Console is https://<HOST ADDRESS>/oampui, where HOST ADDRESS is the IP Address or Hostname of your server.

You must access the legacy OAMP user interface (https://<HOST ADDRESS>/oamp) to configure Policy Information for the user.

### Certificate Removed on Upgrade

After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki .

For information about adding a certificate, see Insert a new tomcat-trust certificate .

### Large Schedules Frequency on Upgrade

After upgrade to Unified Intelligence Center version 12.5, all large schedules with frequency more than once per day will be converted to run only once per day.

### Report Thresholds - Image Location

This release supports only image URLs that are reachable from Unified Intelligence Center server. Maximum size limit that is allowed for an image is 5MB.

### Install Language ES

After successful install or upgrade, if you want to use the Cisco Unified Intelligence Center interface in a language other than English, you have to download and install the language pack ES.

## Deprecated Features

### Internet Explorer 11

In this release, Internet Explorer version 11 is deprecated. Edge Chromium (Microsoft Edge v79 and later) is the replacement.

## Removed and Unsupported Features

### Cisco Unified Intelligence Center Licenses

In this release, the application of Cisco Unified Intelligence Center licenses during fresh install or upgrade is removed.

By default, Cisco Unified Intelligence Center is provisioned with licenses when you install or upgrade to version 12.5.

### HTTP Support for Unified Intelligence Center

In this release, the HTTP support for Unified Intelligence Center has been removed. The users can now securely communicate to Unified Intelligence Center over HTTPS.

The following CLIs are removed from Unified Intelligence Center release 12.5:

show cuic properties http-enabled

set cuic properties http-enabled

show cuic properties hsts

set cuic properties hsts on [max-age value in seconds]

set cuic properties hsts off

### Authenticated Excel Permalink on Office 365

Authenticated Excel report permalink is not supported on Office 365.

### MediaSense Reports

In this release, MediaSense reports are removed and users cannot run MediaSense reports.

## Third Party Software Impacts

None.

| Note | A new Service Update (SU) release is available for Cisco Unified Intelligence Center 12.5(1). You can perform a fresh installation or upgrade to Cisco Unified Intelligence Center 12.5(1) SU on supported virtual machines from previous versions. For more information, see the ReadMe . |
|---|---|