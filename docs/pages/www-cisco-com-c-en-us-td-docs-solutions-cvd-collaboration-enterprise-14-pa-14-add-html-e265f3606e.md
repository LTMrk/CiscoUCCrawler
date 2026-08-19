---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-enterprise-14-pa-14-add-html-e265f3606e
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/enterprise/14/PA_14_Add.html
retrieved_at: 2026-08-19T00:34:23.732189+00:00
---

Addendum: Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments

# Addendum: Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments

### Download Options

Updated: September 6, 2023

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

NOTE: Available paragraph styles are listed in the Quick Styles Gallery in the Styles group on the Home tab. Alternatively, they can be accessed via the Styles window (press Alt + Ctrl + Shift + S ).

Table of Contents

Addendum: Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments . 1

## Addendum: Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments

The following information applies to all deployments of the Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments as documented in the Cisco Validate Design (CVD) available at https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/enterprise/14/collbcvd.html .

1. LDAP bind transaction times <= to 150 ms

To ensure timely and successful client user authentication against LDAP, the required LDAP bind transaction between Unified CM and LDAP for authentication must be completed within 150 milliseconds (ms). This includes the time for network communication between Unified CM and LDAP. As such, LDAP bind transaction times that exceed 150 ms (whether due to long network round trip times or to LDAP server performance) can result in queued authentication requests and in turn delayed or failed authentication for clients. In cases of poor LDAP performance and/or slow response times, ensure the network round trip time between Unified CM nodes and LDAP nodes are well below the required 150 ms total transaction time to compensate for delayed LDAP responses.

This information belongs in the following sections/subsections of the Call Control chapter of the CVD:

■ Architecture > User Authentication with LDAP

■ Deployment > LDAP System Configuration > User Authentication with LDAP

2. Push Notifications for Jabber and Webex App on mobile

It is recommended to enable Push Notifications for Jabber and Webex App on mobile (iOS and Android) for seamless calling experience. Cisco Unified Communications Manager and the IM and Presence Service use either the Apple, or Google cloud’s Push Notification service to send push notifications to compatible Cisco Jabber or Webex clients that run on iOS or Android devices. Push Notifications let your system communicate with the client, even after it has entered into background mode (also known as suspended mode). Without Push Notifications, the system may not be able to send calls or messages to clients that have entered into background mode.

For more information on Push Notifications with Unified CM refer to the Push Notifications Deployment guide available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_01.html#reference_6775E9AB9A99CC00F1E81EFE51C40163 .

This information belongs in the following sections/subsections of the Call Control chapter of the CVD:

■ Architecture > Integration with Apple Push Notification Service (APNs)

■ Deployment Overview > Initial Cisco Unified CM Configuration > Onboarding for Push Notifications via Apple Push Notification Service (APNs)

### This Document Applies to These Products

- Collaboration Systems Release 14