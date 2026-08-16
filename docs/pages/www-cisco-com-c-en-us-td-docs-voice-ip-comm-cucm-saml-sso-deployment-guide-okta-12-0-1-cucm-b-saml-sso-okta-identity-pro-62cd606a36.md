---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-saml-sso-deployment-guide-okta-12-0-1-cucm-b-saml-sso-okta-identity-pro-62cd606a36
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/SAML_SSO_deployment_guide/okta/12_0_1/cucm_b_saml-sso-okta-identity-provider.html
retrieved_at: 2026-08-16T21:16:16.199659+00:00
---

SAML SSO Okta Identity Provider

# SAML SSO Okta Identity Provider

### Download Options

Updated: August 31, 2017

# SAML SSO Okta Identity Provider

Refer to the SAML SSO Deployment Guide for Cisco Unified Communications Applications for your release to find out if Okta has been tested with your release.

## Introduction

Single sign-on (SSO) is a session or user authentication process
that enables a user to provide credentials to access one or more
applications. The process authenticates the user for all
applications they have been given rights to and eliminates further
prompts when they switch applications during a particular
session.

For more information about the SAML SSO Solution, see: SAML SSO Deployment Guide for Cisco Unified Communications Applications .

This document provides steps to configure Okta as SAML SSO Identity Provider (IdP) for Cisco Unified Communications Manager (Unified
CM), Cisco Unified Communications Manager IM and Presence Service
(IM and Presence Service), Cisco Unity Connection, or Cisco Prime
Collaboration Assurance.

## Configure Okta as Identity Provider

Use this procedure to configure Okta as the SAML SSO Identity Provider (IdP) for Cisco Unified Communications Manager.

Okta is a cloud-hosted IdP. SAML SSO can be enabled using Okta IdP with the cluster-wide option only. The per node option is not available for Okta.

For details on how to configure SAML SSO on Cisco Unified Communications Manager, refer to the SAML SSO Deployment Guide at https:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html .

- Single sign on URL —From the metadata file, enter the SSO URL of the publisher node. You can find this by searching for the information on index 0 of the AssertionConsumerService and enter the details for this field.

- Use this for Recipient URL and Destination URL —Check this option to enable matching of the recipient and destination URLs.

- Allow this app to request other SSO URLs —Check this option if you have multiple nodes in your UC deployment and you want to allow requests from other SSO URLs besides the publisher.

You do not need to add HTTP-Redirect URLs to this field.

- Audience URI (SP Identity ID) —From the metadata file, search for the entityID address and enter the details for this field.

- Name ID Format —Choose Transient from this drop-down list.

- Application username —Choose the username format that matches the UserID field that is available in the Cisco Unified Communications Manager cluster.

Ensure that the attribute UID value matches the userID field value that is available in Cisco Unified CM Administration on the User Management > End User page. Following is an example where the userID is mapped to sAMAccountName via a UID string of String.substringBefore(user.email, "@") .

## Enable SAML SSO on Unified Communications Applications

When you have configured the IdP appropriately, follow these steps to enable SSO.

- Cisco Unified Communications Manager— Using a web browser, sign in to Unified CM as administrator, and navigate to System > SAML Single Sign On .

- Cisco Unified Communications Manager IM and Presence Service— Using a web browser, sign in to Unified CM as administrator, and navigate to System > SAML Single Sign On .

- Cisco Unity Connection— Using a web browser, sign in to Cisco Unity Connection as administrator, and navigate to System Settings > SAML Single Sign On .

- Cisco Prime Collaboration Assurance— Using a web browser, sign in to  Prime Collaboration Assurance as globaladmin, and navigate to Administration > System Setup > Single Sign On .

With Okta, you must use a Cluster wide agreement (one metadata file per cluster). Okta will not work with per node agreements.

For detailed SAML SSO configuration steps, refer to the SAML SSO Deployment Guide for Cisco Unified Communications Applications .

## Test SSO on Okta

After you have configured SAML SSO on both Okta and Cisco Unified Communications Manager, test the SSO connection.

| Note | Refer to the SAML SSO Deployment Guide for Cisco Unified Communications Applications for your release to find out if Okta has been tested with your release. |
|---|---|

| Note | For details on how to configure SAML SSO on Cisco Unified Communications Manager, refer to the SAML SSO Deployment Guide at https:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html . |
|---|---|

| Step 1 | Log in to the Service Provider (Cisco Unified Communications Manager) and download the metadata XML file. |
|---|---|
| Step 2 | Log in to the Okta server user interface and click Admin tab. |
| Step 3 | From the Okta dashboard, select Applications > Applications . |
| Step 4 | From the Applications window, click the Add Application button. Various options to create an application or to choose from existing applications appear. |
| Step 5 | Click Create New App to use wizard to create new application integration. |
| Step 6 | On the Create a New Application Integration window, from the Platform drop-down list, choose Web and for the Sign On method field, choose SAML 2.0 . |
| Step 7 | Click Create . |
| Step 8 | Enter a name for the application and click Next . |
| Step 9 | On the Create SAML Integration window, enter the details for fields of the General Settings tab, and click Next . |
| Step 10 | Enter details for the following mandatory fields for SAML Settings. These details are available in the metadata XML file that you downloaded from the Service Provider. Single sign on URL —From the metadata file, enter the SSO URL of the publisher node. You can find this by searching for the information on index 0 of the AssertionConsumerService and enter the details for this field. Use this for Recipient URL and Destination URL —Check this option to enable matching of the recipient and destination URLs. Allow this app to request other SSO URLs —Check this option if you have multiple nodes in your UC deployment and you want to allow requests from other SSO URLs besides the publisher. Requestable SSO URLs —This field appears only if you check the above check box. You can enter SSO URLS for your other nodes. You can find the ACS URLs in the metadata file by searching for all the AssertionConsumerService (ACS) addresses that use the HTTP-POST Binding. Add those details for this field. Click the Add Another button to add multiple URLs. Note You do not need to add HTTP-Redirect URLs to this field. Audience URI (SP Identity ID) —From the metadata file, search for the entityID address and enter the details for this field. Name ID Format —Choose Transient from this drop-down list. Application username —Choose the username format that matches the UserID field that is available in the Cisco Unified Communications Manager cluster. | Note | You do not need to add HTTP-Redirect URLs to this field. |
| Note | You do not need to add HTTP-Redirect URLs to this field. |
| Step 11 | (Optional) Enter the attribute UID to the Cisco Unified Communications Manager cluster. Note Ensure that the attribute UID value matches the userID field value that is available in Cisco Unified CM Administration on the User Management > End User page. Following is an example where the userID is mapped to sAMAccountName via a UID string of String.substringBefore(user.email, "@") . Figure 1. Sample UID Mapping | Note | Ensure that the attribute UID value matches the userID field value that is available in Cisco Unified CM Administration on the User Management > End User page. Following is an example where the userID is mapped to sAMAccountName via a UID string of String.substringBefore(user.email, "@") . |
| Note | Ensure that the attribute UID value matches the userID field value that is available in Cisco Unified CM Administration on the User Management > End User page. Following is an example where the userID is mapped to sAMAccountName via a UID string of String.substringBefore(user.email, "@") . |
| Step 12 | On the Feedback tab, select “ I'm a software vendor. I'd like to integrate my app with Okta ” and click Finish . |
| Step 13 | On the Import tab, assign the users or groups that you want to enable, and click Done . |
| Step 14 | On the Sign On tab, click the Identity Provider metadata link to download the Okta metadata file. |
| Step 15 | Open the downloaded metadata file, change the two lines of NameIDFormat to <md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</md:NameIDFormat> , and then save the file. |

| Note | You do not need to add HTTP-Redirect URLs to this field. |
|---|---|

| Note | Ensure that the attribute UID value matches the userID field value that is available in Cisco Unified CM Administration on the User Management > End User page. Following is an example where the userID is mapped to sAMAccountName via a UID string of String.substringBefore(user.email, "@") . |
|---|---|

| Step 1 | Navigate to the following page for each application: Cisco Unified Communications Manager— Using a web browser, sign in to Unified CM as administrator, and navigate to System > SAML Single Sign On . Cisco Unified Communications Manager IM and Presence Service— Using a web browser, sign in to Unified CM as administrator, and navigate to System > SAML Single Sign On . Cisco Unity Connection— Using a web browser, sign in to Cisco Unity Connection as administrator, and navigate to System Settings > SAML Single Sign On . Cisco Prime Collaboration Assurance— Using a web browser, sign in to  Prime Collaboration Assurance as globaladmin, and navigate to Administration > System Setup > Single Sign On . |
|---|---|
| Step 2 | Click Enable SAML SSO and follow the steps. Note With Okta, you must use a Cluster wide agreement (one metadata file per cluster). Okta will not work with per node agreements. | Note | With Okta, you must use a Cluster wide agreement (one metadata file per cluster). Okta will not work with per node agreements. |
| Note | With Okta, you must use a Cluster wide agreement (one metadata file per cluster). Okta will not work with per node agreements. |

| Note | With Okta, you must use a Cluster wide agreement (one metadata file per cluster). Okta will not work with per node agreements. |
|---|---|

| Note | For detailed SAML SSO configuration steps, refer to the SAML SSO Deployment Guide for Cisco Unified Communications Applications . |
|---|---|

| Step 1 | Log in to Okta to authenticate the Okta service. A confirmation message, showing that the SSO configuration is successful, appears. |
|---|---|
| Step 2 | Click Close and then click Finish |
| Step 3 | Close the web browser and wait for a couple of minutes for the SAML SSO configuration changes to take effect on Cisco Unified Communications Manager. |
| Step 4 | Enter the Cisco Unified Communications Manager URL in the address bar of the web browser to verify that SSO is enabled. The Recovery URL to bypass Single Sign On (SSO) link appears below the Cisco Unified Communications Manager link. The Recovery URL to bypass Single Sign On (SSO) link appears when the SSO is enabled. |