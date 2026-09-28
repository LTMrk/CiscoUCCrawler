---
doc_id: help-webex-com-en-us-article-nqvsbmq-c331e8194c
source_url: https://help.webex.com/en-us/article/nqvsbmq
retrieved_at: 2026-09-01T20:26:44.556198+00:00
---

- Software upgrades

- Announcements

## Automatic upgrades

We recommend enabling automatic upgrades so new releases are automatically installed.

## Download Directory Connector

For a fresh installation of the Directory Connector:

Download the installation zip file from this link .

Follow the Install Cisco Directory Connector procedure in the deployment guide (from Step 3 onward).

## 3.8.7000

April 4, 2024

We've made the following change in this release of Directory Connector:

- We've added a text field in ObjectSelectionCriteria so admins can exclude the organization unit from synchronization.

## 3.8.5000

February 12, 2024

We've made the following change in this release of Directory Connector:

- User avatars won't be synchronized when the email ID is left blank.

## 3.8.2000

March 30, 2023

The following feature is now available:

- Configuring and synchronizing contact attributes

## 3.8.1005

February 16, 2023

We've made the following changes in this release of the Directory Connector:

This version of Directory Connector does not synchronize Distribution groups.
            Distribution groups are not used in Control Hub, so now we only synchronize the Security
            groups.

- Directory Connector now uses the Windows user profile folder. We changed from using the
          browser cache folder because that folder can have access restrictions.

- The software has an updated code signing certificate.

## 3.8.1001

October 31, 2022

We've made the following improvements:

- Directory Connector now uses Microsoft Edge as the default browser, which supports
            web-based functions, such as the Duo SSO login page.

- Upgraded the Directory Connector client to use Microsoft .NET Framework 4.5 as the
            runtime library.

## 3.7.5000

August 5, 2022

The following features are now available:

- Remove User Attribute Mapping

- Manage Profile Pictures

## 3.7.2000

November 4, 2021

This update addresses a customer-found issue with synchronizing avatars from Active Directory. The new version has a 2 MB limit on the avatar file size. If an avatar file is greater than 2 MB, it does not prevent the synchronization.

## 3.7.1001

October 29, 2020

Added an in-product message that informs you to switch to auto
                        synchronization mode if the Directory Connector is using a manual
                        synchronization mode.

## 3.6

June 18, 2020

Added the following features and enhancements: shortcut to Directory Connector created on desktop after installation, dry runs now show a progress count, and you can now configure attributes for room objects.

Fixed the issue where user attribute mapping couldn't find userproxy attributes.

Refreshed Symantec code signing certificate.

## 3.5.1001

October 8, 2019

Added the following features and enhancements: send directory synchronization report to specific email addresses, avatar sync support for a proxy user in AD LDS, support for the avatar pattern 'cn' attribute, and Troubleshooting feature enhancements.

Changed the default incremental synchronization schedule from every 30 minutes to every 4 hours.

Fixed a scaling resolution issue that affected how Directory Connector was displayed in remote desktop sessions.

Fixed an issue so that groups are always shown on the Add Objects page even after a synchronization is performed.

## 3.4.1001

May 20, 2019

Added the following features: diagnostic tool, secure LDAP (LDAPS), and enhancements to attribute verification messages. For more information, see the Announcements tab and the deployment guide.

Enhanced the mismatch object deleting messages.

Fixed the issue where an admin could not sign in when FIPS was enabled.

Fixed the issue where the root domain guid couldn't be retrieved while the connector registered.

Fixed the issue where the connector crashed from a remote session to Windows Server 2012.

Fixed a sign in failure when the admin email contained +.

Fixed the issues where Active Directory avatar testing and uid format verification was not supported for AD LDS.

## 3.3.1003

February 15, 2019

Added the following features: customized attributes, Kerberos proxy support, embedded avatar profile synchronization, more attribute mappings to uid, automatic software upgrade, and support for credentials to access URL based avatar files. For more information, see the Announcements tab and the deployment guide.

Microsoft had a cookie issue which caused the Directory Connector incremental sync to fail. In this version, the problem is fixed.

## 3.0.1003

June 19, 2018

Security enhancement for TLS1.2 and its dependency, .NET Framework 4.5. The framework is enforced with this release, so the software can support TLS1.2.

This is a required upgrade, because Cisco will no longer support TLS1.0 and TLS1.1. Please upgrade to this release as soon as possible.

While we strongly recommend that you upgrade to 3.0.1003, if you upgraded to 3.0.1001, you must be running .NET Framework 4.5 for your deployment to be in compliance.

## 3.0.1001

April 23, 2018

Added new features: support for Active Directory deployments with multiple domains under a single forest or multiple forests, NTLM support, userPrincipalName (Active Directory attribute) can be mapped to uid (cloud attribute), and TLS 1.2 support.  For more information, see the Announcements tab and the deployment guide.

This page covers announcements to help you prepare your Hybrid Directory connector deployment for new releases.

Go to https://www.cisco.com/go/hybrid-services-directory to access the Deployment Guide for Directory Connector .

## Automatic upgrades

We recommend enabling automatic upgrades so new releases are automatically installed.

## Download the Directory Connector

For a fresh installation of the Directory Connector:

Download the installation zip file from this link .

Follow the Install Directory Connector procedure in the deployment guide (from Step 3 onward).

## April 15, 2022

Delete users permanently after soft delete

You can now delete users permanently at the next synchronization after they're soft deleted instead of having to wait for the seven-day grace period.

For more information, see this section of the deployment guide.

## October 31, 2019

Windows Server 2019

## October 8, 2019

New features for Directory Connector 3.5

We released Cisco directory connector version 3.5. For an existing installation, you'll see an upgrade prompt. We recommend enabling automatic upgrades so new releases are automatically installed. For a new installation, use the steps and links at the top of the release notes.

This release contains the following feature updates and enhancements (and corresponding documentation updates):

```
<Installation Location>\Cisco Systems\Cisco Systems\Cisco Directory
    Connector\Logs
```

## June 26, 2019

New user soft delete feature

Cisco directory connector has checks and balances to prevent unintentional deletion of users. Unfortunately, accidents happen; you may have incorrectly configured an LDAP filter in Active Directory, which deleted some users when synchronized to the cloud. The soft delete feature can help you recover from these accidents and reestablish the user accounts.

For more information, see this section of the deployment guide.

Although this is a cloud-side feature and is not tied to a specific software release, we strongly recommend that you upgrade to the latest version of Cisco directory connector.

## May 20, 2019

New features for Directory Connector 3.4

We released Cisco directory connector version 3.4. For an existing installation, you'll see an upgrade prompt. We recommend enabling automatic upgrades so new releases are automatically installed. For a new installation, use the steps and links at the top of the release notes.

This release contains the following feature updates and enhancements (and corresponding documentation updates):

Cisco directory connector verifies the attribute value of uid in the cloud identity service and retrieves 3 available users under the filter options that you chose. If all of these 3 users have a valid email format, the software shows you a verification pop up. If any errors appear during this test, you'll see a warning message.

## February 15, 2019

New features for Directory Connector 3.3

We released Cisco directory connector version 3.3. For an existing installation, you'll see an upgrade prompt. For a new installation, use the steps and links at the top of the release notes.

This release contains the following feature updates and enhancements (and corresponding documentation updates):

Cisco directory connector can now support expression-based attribute customization. Previously, the application had several predefined hard-coded combinations to support customer requests such as "GivenName SN". When customers had different requests for the attribute combination, engineering needed to add it manually. This feature gives more flexibility by letting you define your own attribute combination.

It's important to keep your Cisco directory connector updated to the latest version. In 3.3, you can let the application do an automatic upgrade when a new version is ready. You just check a checkbox and then the app can do the installs silently. If you change your mind, you can go back to the configuration setting to uncheck the function.

You may manage avatar resources in a web resource server where credentials are required. In the new version, you can provide the credentials before synchronization and then the Directory Connector can sync up all avatar data to the cloud.

## April 23, 2018

New features for Directory Connector 3.0

We released Cisco directory connector version 3.0. For an existing installation, you'll see an upgrade prompt; for a new installation, get the latest version by going to the customer view in https://admin.webex.com , clicking Users , and then choosing Manage Users > Enable Directory Synchronization .

This release contains the following feature updates and enhancements (and corresponding documentation updates):

Cisco directory connector now supports multiple domains either under a single forest or under multiple forests (without the need for AD LDS). You can install a Cisco directory connector for each domain, bind each domain to your organization, and then synchronize each user base into Webex. Control Hub reflects the status by showing the synchronization state for multiple Cisco directory connectors, allows you to turn off synchronization for a specific domain, and deactivate a Cisco directory connector in a high availability deployment. The dry run synchronization helps you match the on-premises Active Directory user data with the user data in the Webex cloud, and any mismatched user objects are flagged so you can make a decision.

For steps to deploy Cisco directory connector in a multiple domain environment, see the procedures in the Deploy Directory Connector chapter.