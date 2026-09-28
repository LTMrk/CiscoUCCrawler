---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-interdomain-federation-14-cup0-b-interdomain-federation-gui-2c8d255d01
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/interdomain_federation/14/cup0_b_interdomain-federation-guide-14/cup0_b_interdomain-federation-1251su3_chapter_01111.html
retrieved_at: 2026-08-16T16:28:19.129841+00:00
---

Interdomain Federation Guide for the IM and Presence Service, Release 14 and SUs

# Interdomain Federation Guide for the IM and Presence Service, Release 14 and SUs

Updated: January 22, 2023

Chapter: Email Address for Federation Configuration

## Chapter: Email Address for Federation Configuration

# Email Address for Federation Configuration

This chapter provides information about the Email Address for Federation feature and multiple domain configuration.

## Email for Federation Enablement

When you turn on the email address for federation feature, the IM and Presence Service changes the JID of the local user to the email address of the contact.

If you have an intercluster deployment, you must turn on the email address for federation on all intercluster nodes in your
                              deployment. You must then restart the Cisco XCP Router service after the email for federation feature is turned on.

In an XMPP federation deployment, the email address for federation feature does not currently support temporary or persistent
                              chat rooms in a multicluster IM and Presence Service deployment. In the deployment scenario where there are multiple IM and Presence Service clusters in the local domain, the local users actual JID may be sent to the federated user. The only impact to the chat room
                              is that the name that displays to the federated user is the userid of the local user, instead of the email address of the
                              local user; all other chat room functionality operates as normal. This only occurs in temporary or persistent chat rooms with
                              federated users.

For more information about the email address for federation feature for SIP and XMPP federation, and for instructions to turn
                              on the feature, see topics related to email address for federation configuration.

## Email Address for Federation Considerations

When you configure the IM and Presence Service to use the email address for SIP or XMPP federation, the IM and Presence Service swaps the IM address of the local user for the user's email address in all communications with a federated contact.

Before you turn on email address for interdomain federation, note the following:

If you have not yet attempted to federate with the external domain, and you wish to turn on email for federation, we recommend
                                    that you turn on this setting before users begin to add any federated contacts.

If you turn on email address for federation, and a user does not have an email address configured in Active Directory, the IM and Presence Service uses the JID of the user for federation.

A prerequisite for this feature is that the Cisco Unified Communications Maanger Mail ID for each user must match the full email address for the user.

If the Mail ID field for the user is empty or does not contain a full email address, the IM and Presence Service defaults to using the IM and Presence Service JID of the user for federation

If you turn on email address for federation, and a federated contact uses the JID of an IM and Presence Service user rather than using the email address, the IM and Presence Service drops these requests (even if a valid email address is configured for the user).

The IM and Presence Service does not support email aliases for the email address for federation feature.

This feature applies to both SIP and XMPP federation.

### Email Address for Federation Support of Multiple Domains

The Email Address for Federation feature supports multiple domains. The following figure shows an example of multiple email
                                 domains that are being used for federated traffic.

If the local IM and Presence Service deployment is managing multiple email domains, you must publish the required DNS SRV records for each local email domain.

For XMPP federation, the
                                 cup-xmpp-s2s security certificate must have all local IM and email domains included as
                                 Subject Alt Names.

### Email Domain Configuration Overview

Manually adding and editing email domains for use with the Email Address for Federation feature is optional since the IM and Presence Service automatically reads all unique domains for each of the user's email addresses and uses that information for the Email Address
                                 for Federation feature.

If you have domains that have users who are not yet configured for the IM and Presence Service but plan to configure those users, then you can manually add those domains to the IM and Presence Service using the Cisco Unified CM IM and Presence Administration user interface. A domain that does not currently have any users assigned is not automatically listed as a local email domain
                                 in the user interface.

User domains that are used for Email Address for Federation are listed as system-managed domains on the Email Domain window in the Cisco Unified CM IM and Presence Administration user interface. These are not configurable with the user interface.

### Information to Provide to the Administrator of an External Domain

Before you turn on email address for federation, you must alert the system administrator of the external domain to the following:

You are using email address for federation, and that the users in the external domain must specify an email address when adding
                                       a federated contact to their contact list.

If you are already federating with the external domain, and you wish to turn on email for federation, users in the external
                                       domain must remove the existing federated contacts in their contact list, and add these federated contacts again specifying
                                       an email address.

### Information to Provide IM and Presence Service Users

When you turn on email address for federation, you must notify all IM and Presence Service users of the following:

Federated contacts now use email addresses rather than the user_id@domain addresses.

When adding new contacts to their contact list, federated contacts must now use the email address for IM and Presence Service users, rather than the user_id@domain.

Existing IM and Presence Service contacts (on the federated watcher's contact list) that were added with user_id@domain must be removed, and added again using
                                       the email address for the IM and Presence Service user.

Any messages that the IM and Presence Service receives from federated contacts to the user_id@domain address are dropped (unless it happens to be the same as the email
                                       address configured in Active Directory, and the address configured in the users table on the IM and Presence Service ).

If IM and Presence Service users already have federated contacts on their contact list, when these users sign in to the client again, the federated
                                       contact may get a pop-up containing the email address.

When you turn on email address for federation, the IM and Presence Service user does NOT need to change anything on the client when they connect to the IM and Presence Service , nor do they interact any differently with the IM and Presence Service node.

### Email Domain Management Interactions and Restrictions

You can add or delete only administrator-managed domains that are associated with the local cluster.

You cannot edit system managed domains.

You cannot edit system-managed or administrator managed domains that are  associated with other clusters.

It is possible to have a domain configured on two clusters, but in use on only the peer cluster. This appears as a system-managed
                                       domain on the local cluster, but is identified as being in use on only the peer cluster.

For  XMPP Federation  over TLS, you must regenerate the TLS certificate cup-xmpp-s2s if adding or removing an IM address domain.

Email Address for Federation Configuration and Email Domain Management

## Turn On Email for Federation

If you have an intercluster deployment, you must turn on the email
                                          			 address for federation on any intercluster nodes in your deployment.

Step 1

Log in to the Cisco Unified CM IM and
                                          			 Presence
                                          				  Administration user interface. Choose Presence > Settings .

Step 2

Check 
                                       			 the Enable use of Email Address for Inter-domain Federation check box.

Step 3

Read the warning message, and click OK .

Step 4

Click Save .

Step 5

After you turn on email for federation, restart the Cisco XCP
                                       			 Router. Log in to the Cisco Unified IM and
                                          			 Presence Serviceability user interface. Choose Tools > Control Center -
                                             				  Network Services .

If you want to edit routing parameters for Federation, go to Configure Federation Routing Parameters .

## View Email  Domains

System-managed domains and local domains that are administrator-managed are displayed on the Find and List Email Domains window
                              using the Cisco Unified CM IM and Presence Administration user interface. This window also specifies whether each administrator-managed  domain was configured on the local cluster,
                              peer cluster, or both.

Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Presence > Inter-Domain Federation > Email Federated Domains .
                                       		   The Find and List Email Domains window appears.

## Add or Update Email Domain

You can manually add IM address domains to your local cluster and update existing IM address domains that are on your local
                              cluster using Cisco Unified CM IM and Presence Administration user interface.

You can enter a domain name of up to a maximum of 255 characters and each domain must be unique across the cluster. Allowable
                              values are any upper or lower case letter (a-z,  A-Z), any number (0-9), the hyphen (-), or the dot (.). The dot serves as
                              a domain label separator. Domain labels must not start with a hyphen. The last label (for example, .com) must not start with
                              a number. Abc.1om is an example of an invalid domain.

System-managed domains and local domains that are administrator-managed are displayed on the Find and List Domains window.
                              This window also specifies whether each administrator-managed  domain was configured on the local cluster, peer cluster, or
                              both.

System-managed domains cannot be edited because they are in use. A system-managed domain automatically becomes an administrator-managed
                              domain if there are no longer users on the system with that IM address domain (for example, due to user deletion). You can
                              edit or delete administrator-managed domains.

Step 1

Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Presence > Inter-Domain Federation > Email Federated Domains .

The Find and List Email Domains window appears displaying all administrator-managed and system-managed email domains.

Step 2

Perform one of the following actions:

Click Add New to add a new domain. The Email Domain window appears.

Choose the domain to edit  from the list of domains. The Email Domain window appears.

Step 3

Enter the new domain name   in the Domain Name field, and then click Save .

Enter a unique domain name up to a maximum of 255 characters. Allowable values are any upper or lower case letter (a-z, A-Z),
                                          any number (0-9), the hyphen (-), or the dot (.). Domain labels must not start with a hyphen, and the last label (for example,
                                          .com) must not start with a number.

Tip

A warning message appears. If you are using TLS XMPP federation, you should proceed to generate a new TLS certificate.

## Delete an Email Domain

You can delete administrator-managed email address domains that are in the local cluster using Cisco Unified CM IM and Presence Administration user interface.

System-managed domains cannot be deleted because they are in use. A system-managed domain automatically becomes an administrator-managed
                              domain if there are no longer users on the system with that email domain (for example, due to user deletion). You can edit
                              or delete administrator-managed domains.

If you delete an administrator-managed domain that is configured on both local and peer clusters, the domain remains in the
                                          administrator-managed domains list; however, that domain is marked as configured on the peer cluster only. To completely remove
                                          the entry, you must delete the domain from all clusters on which it is configured.

Step 1

Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Presence > Inter-Domain Federation > Email Federated Domains .

The Find and List Email Domains window appears displaying all administrator-managed and system-managed email address domains.

Step 2

Choose the administrator-managed domains to delete using one of the following methods, and then click Delete Selected .

Check the check boxes beside the domains to delete.

Click Select All to select all domains in the list of administrator-managed domains.

Tip

Click Clear All to clear all selections.

Step 3

Click OK to confirm the deletion or click Cancel .

| Note | This feature applies to both SIP and XMPP federation. |
|---|---|

| Note | When you turn on email address for federation, the IM and Presence Service user does NOT need to change anything on the client when they connect to the IM and Presence Service , nor do they interact any differently with the IM and Presence Service node. |
|---|---|

| Note | If you have an intercluster deployment, you must turn on the email
                                          			 address for federation on any intercluster nodes in your deployment. |
|---|---|

| Step 1 | Log in to the Cisco Unified CM IM and
                                          			 Presence
                                          				  Administration user interface. Choose Presence > Settings . |
|---|---|
| Step 2 | Check 
                                       			 the Enable use of Email Address for Inter-domain Federation check box. |
| Step 3 | Read the warning message, and click OK . |
| Step 4 | Click Save . |
| Step 5 | After you turn on email for federation, restart the Cisco XCP
                                       			 Router. Log in to the Cisco Unified IM and
                                          			 Presence Serviceability user interface. Choose Tools > Control Center -
                                             				  Network Services . |

| Note | If you want to edit routing parameters for Federation, go to Configure Federation Routing Parameters . |
|---|---|

| Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Presence > Inter-Domain Federation > Email Federated Domains .
                                       		   The Find and List Email Domains window appears. |
|---|

| Step 1 | Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Presence > Inter-Domain Federation > Email Federated Domains . The Find and List Email Domains window appears displaying all administrator-managed and system-managed email domains. |
|---|---|
| Step 2 | Perform one of the following actions: Click Add New to add a new domain. The Email Domain window appears. Choose the domain to edit  from the list of domains. The Email Domain window appears. |
| Step 3 | Enter the new domain name   in the Domain Name field, and then click Save . Enter a unique domain name up to a maximum of 255 characters. Allowable values are any upper or lower case letter (a-z, A-Z),
                                          any number (0-9), the hyphen (-), or the dot (.). Domain labels must not start with a hyphen, and the last label (for example,
                                          .com) must not start with a number. Tip A warning message appears. If you are using TLS XMPP federation, you should proceed to generate a new TLS certificate. | Tip | A warning message appears. If you are using TLS XMPP federation, you should proceed to generate a new TLS certificate. |
| Tip | A warning message appears. If you are using TLS XMPP federation, you should proceed to generate a new TLS certificate. |

| Tip | A warning message appears. If you are using TLS XMPP federation, you should proceed to generate a new TLS certificate. |
|---|---|

| Note | If you delete an administrator-managed domain that is configured on both local and peer clusters, the domain remains in the
                                          administrator-managed domains list; however, that domain is marked as configured on the peer cluster only. To completely remove
                                          the entry, you must delete the domain from all clusters on which it is configured. |
|---|---|

| Step 1 | Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Presence > Inter-Domain Federation > Email Federated Domains . The Find and List Email Domains window appears displaying all administrator-managed and system-managed email address domains. |
|---|---|
| Step 2 | Choose the administrator-managed domains to delete using one of the following methods, and then click Delete Selected . Check the check boxes beside the domains to delete. Click Select All to select all domains in the list of administrator-managed domains. Tip Click Clear All to clear all selections. | Tip | Click Clear All to clear all selections. |
| Tip | Click Clear All to clear all selections. |
| Step 3 | Click OK to confirm the deletion or click Cancel . |

| Tip | Click Clear All to clear all selections. |
|---|---|