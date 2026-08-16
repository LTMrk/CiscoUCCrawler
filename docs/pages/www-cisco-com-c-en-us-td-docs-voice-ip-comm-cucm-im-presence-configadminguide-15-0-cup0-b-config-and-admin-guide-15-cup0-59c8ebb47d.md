---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-15-0-cup0-b-config-and-admin-guide-15-cup0-59c8ebb47d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/15_0/cup0_b_config-and-admin-guide-15/cup0_b_config-and-admin-guide-1401_chapter_011.html
retrieved_at: 2026-08-16T15:57:31.009785+00:00
---

Configuration and Administration of the IM and Presence Service, Release 15 and SUs

# Configuration and Administration of the IM and Presence Service, Release 15 and SUs

Updated: January 7, 2026

Chapter: Configure IM Addressing Scheme

## Chapter: Configure IM Addressing Scheme

# Configure IM Addressing Scheme

## IM Addressing Scheme Overview

The IM and Presence Service supports two IM addressing schemes:

UserID@Default_Domain is the default IM address scheme when you install the IM and Presence Service.

Directory URI IM address scheme supports multiple domains, alignment with the user's email address, and alignment with Microsoft
                                 SIP URI.

You must use the same IM address scheme across all IM and Presence Service clusters.

### IM Address Using User@Default_Domain

The default addressing scheme for IM and Presence Service is UserID@Default_Domain .

When you use the UserID@Default_Domain IM address scheme, all IM addresses are part of a single, default IM domain. The default domain value must be consistent
                              across all clusters. Because IM addresses are part of the IM and Presence default domain, multiple domains are not supported.

The UserID can be free-form or synced from LDAP. The following fields are supported:

sAMAccountName

User Principle Name (UPN)

Email address

Employee number

Telephone number

If  you map the UserID to an LDAP field on Cisco Unified Communications Manager , that LDAP mapping must be consistent across all clusters.

Although you can map the  UserID  to the email address, that does not mean the IM URI equals the email address. Instead it
                              becomes <email-address>@Default_Domain . For example, amckenzie@example.com@sales-example.com . The Active Directory (AD) mapping setting that you choose is global to all users within that IM and Presence Service cluster.
                              It is not possible to set different mappings for individual users.

### IM Address Using Directory URI

The Directory URI address scheme aligns a user's IM address with their Cisco Unified Communications Manager Directory URI.

The Directory URI IM address scheme provides the following IM addressing features:

Multiple domain support. IM addresses do not need to use a single IM and Presence Service domain.

Alignment with the user's email address. You can configure the Cisco Unified Communications Manager Directory URI to align with a user's email address to provide a consistent identity for email, IM, voice and video communications.

Alignment with Microsoft SIP URI. The Cisco Unified Communications Manager Directory URI can be configured to align with the Microsoft SIP URI to ensure that the user's identity is maintained when
                                    migrating from Microsoft OCS/Lync to IM and Presence Service.

If you configure the node to use Directory URI as the IM address scheme, we recommend that you deploy only clients that support
                              Directory URI. Any client that does not support Directory URI will not work if the Directory URI IM address scheme is enabled.
                              Cisco recommends that you use the UserID@Default_Domain IM address scheme and not the Directory URI IM address scheme if you have any deployed clients that do not support Directory
                              URI.

The Directory URI IM address settings are global and apply to all users in the cluster. You cannot set a different Directory
                              URI IM address for individual users in the cluster.

For details on provisioning directory URIs from an external LDAP Directory, see Configure LDAP Directory .

### Multiple IM Domains

IM and Presence Service supports IM addressing across multiple IM address domains and automatically lists all domains in the
                              system. You can add, edit, or delete domains. For information on configuring IM domains, see Configure the Domain Overview .

If you are interoperating with Cisco Expressway, see the Cisco Expressway Administrator Guide at http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-maintenance-guides-list.html .

## IM Addressing Scheme Prerequisites

The IM and Presence Service default domain and the IM address scheme that you use must be consistent across all IM and Presence
                              Service clusters. Before you begin, Configure the Default Domain on IM and Presence Service .

The IM address scheme you set affects all user JIDs and cannot be performed in a phased manner without disrupting communication
                              between clusters that may have different settings.

If any of the deployed clients do not support directory URI as the IM address, administrators should disable the directory
                              URI IM address scheme.

## Configure IM Addressing Scheme Task Flow

Complete these tasks in the following order to configure your IM addressing scheme.

Step 1

Verify User Provisioning

Verify that end users are correctly provisioned and that there are no duplicate or invalid users.

Step 2

Disable High Availability

You must temporarily disable high availability for the presence redundancy group. Configuring the IM addressing scheme requires
                                          you to stop services temporarily; if you stop the
                                          services while high availability is enabled, a system failover will
                                          occur.

Step 3

Stop Services

Prior to updating your IM addressing scheme configuration stop essential IM and Presence Services. Make sure to stop services
                                          in the prescribed order.

Step 4

Assign IM Addressing Scheme

Use this procedure to configure a new domain and IM address scheme, or to update an existing domain and address scheme.

Step 5

Restart Services

Once your IM addressing scheme is configured, restart services. You must do this prior to updating user address information
                                          or provisioning new users. Make sure to follow the prescribed order when you restart services.

Step 6

Enable High Availability

You can enable high availability for the presence redundancy groups after you have configured the IM addressing scheme and
                                          restarted IM and Presence services. All services must be running on IM and Presence database publisher nodes and subscriber nodes before you enable high availability.

Step 7

If you chose Directory URI as the IM addressing scheme:

- Assign the LDAP Source for Directory URIs

- Manually Assign a Directory URI

Optional. If you are syncing users from an external LDAP directory, set the LDAP source field for your directory URI values.

For non-LDAP users, you must provision directory URIs manually. You can do this on a user-by-user basis, or via the Bulk Administration
                                          Tool.

### Verify User Provisioning

Use this procedure to verify that end users are correctly provisioned before you configure the addressing scheme.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter .

Step 2

In the User Troubleshooter section, verify that end users are correctly provisioned and that there are no duplicate or invalid users.

#### What to do next

Disable High Availability

### Disable High Availability

Disable High Availability in each presence redundancy group in your cluster. Editing the addressing scheme requires you to
                                 stop services temporarily. If you stop services with High Availability  enabled, a system failover occurs.

The Presence Redundancy Group Details page shows all the active JSM sessions, even when the high availability is disabled in the cluster.

#### Before you begin

Take a record of the number of active users for each cluster node in each Presence Redundancy Group. You can find this information
                                 in the ( System > Presence Topology ) window of Cisco Unified CM IM and Presence Administration. You will need these numbers later when you re-enable High Availability.

Step 1

From the Cisco Unified CM Administration user interface, choose System > Presence Redundancy Groups .

Step 2

Click Find and select the group.

Step 3

On the Presence Redundancy Group Configuration window, uncheck the Enable High Availability check box.

Step 4

Click Save .

Step 5

Repeat this procedure for each Presence Redundancy Group.

Step 6

When you are done, wait at least two minutes to sync the new HA settings across the cluster before you make any further changes

#### What to do next

Stop Services

### Stop Services

Prior to updating your IM addressing scheme configuration stop essential IM and Presence Services. Make sure to stop services
                                 in the prescribed order.

#### Before you begin

Disable High Availability

Step 1

In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center – Network Services .

Step 2

Stop the following IM and Presence Services, in this order, by selecting the service and clicking the Stop button:

Cisco Sync Agent

Cisco Client Profile Agent

Step 3

After both services have stopped, choose Tools > Control Center – Feature Services and stop the following services in this order:

Cisco Presence Engine

Cisco SIP Proxy

Step 4

After both services have stopped, choose Tools > Control Center – Feature Services and stop the following service:

- Cisco XCP Router

When you stop the XCP Router service, all related XCP feature services stop automatically.

#### What to do next

Assign IM Addressing Scheme

### Assign IM Addressing Scheme

Use this procedure to configure a new domain and IM address scheme, or to update an existing domain and address scheme.

Make sure that the IM addressing scheme that you configure is consistent across all clusters.

#### Before you begin

Stop Services

Step 1

In Cisco Unified CM IM and Presence Administration , choose Presence > Settings > Advanced Configuration.

Step 2

To assign a new default domain, check the Default Domain check box and, in the text box, enter the new domain.

Step 3

To change the address scheme, check the IM Address Scheme check box, and select one of the following options from the drop-down list box:

UserID@[Default_Domain] — Each IM user address is derived from the UserID along with the default domain. This is the default setting.

Directory URI — Each IM user address matches the directory URI that is configured for that user in Cisco Unified Communications Manager.

When you choose this option, all deployed clients must support Directory URI as the IM address and use either EDI-based or
                                                            UDS-based directory integration. For UDS-based integration with Jabber, you must be running Jabber Release 10.6 or later.

Step 4

Click Save.

You can monitor the progress of the update in the status area.

If you chose Directory URI as the IM address scheme, you may be prompted to ensure that the deployed clients can support multiple
                                             domains. Click OK to proceed or click Cancel .

If any user has an invalid Directory URI setting, a dialog box appears. Click OK to proceed or click Cancel , and then fix the user settings before reconfiguring the IM address scheme.

A system update can take up to 1 hour to complete. Click Re-try to reapply the changes or click Cancel .

#### What to do next

If you configured user@default_domain as the addressing scheme, and you are not using the Directory URI, then proceed to Restart Services .

If you configured Directory URI as the addressing scheme, choose on the of the following options:

Assign the LDAP Source for Directory URIs

Manually Assign a Directory URI

#### IM Address Examples

Sample IM address options that are available for IM and Presence Service.

IM and Presence Service Default Domain: cisco.com

User: John Smith

User ID: js12345

Mail ID: jsmith@cisco-sales.com

SIPURI: john.smith@webex.com

IM Address Format

Directory URI Mapping

IM Address

<userid>@<domain>

n/a

js12345@cisco.com

Directory URI

mailid

jsmith@cisco-sales.com

Directory URI

msRTCSIP-PrimaryUserAddress

john.smith@webex.com

### Restart Services

Once your IM addressing scheme is configured, restart services. You must do this prior to updating user address information
                                 or provisioning new users. Make sure to follow the prescribed order when you restart services.

#### Before you begin

Assign IM Addressing Scheme

If you configured  Directory URI as the addressing scheme, complete one of the following options before you restart services:

Assign the LDAP Source for Directory URIs

Manually Assign a Directory URI

Step 1

In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center – Network Services .

Step 2

Start the following service by selecting the service and clicking the Start button:

- Cisco XCP Router

Step 3

After the service starts, choose Tools > Control Center – Feature Services and start the following services in this order:

Cisco SIP Proxy

Cisco Presence Engine

Step 4

Confirm that the Cisco Presence Engine service is running on all nodes before proceeding to the next step.

Step 5

Choose Tools > Control Center – Network Services and start the following services in this order:

Cisco Client Profile Agent

Cisco Sync Agent

#### What to do next

Enable High Availability

### Enable High Availability

After you have configured your IM addressing scheme and restarted services, use this procedure to re-enable high availability
                                 for each presence redundancy group in your cluster

#### Before you begin

All services must be running on IM and Presence database publisher nodes and subscriber nodes before you enable high availability. If it has been less than 30 minutes since
                                 your services restarted,  confirm that your Cisco Jabber sessions have been recreated before you enable High Availability.
                                 Otherwise, Presence won't work for Jabber clients whose sessions aren't created.

To obtain the number of Cisco Jabber sessions, run the show perf query counter Cisco Presence Engine Active JsmSessions CLI command on all cluster nodes. The number of active sessions should match the number of users that you recorded when you
                                 disabled high availability.

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

Step 2

From the Server list, choose the node on which you want to reactivate services and click Go .

Step 3

In the IM and Presence Services area, select the following services:

Cisco Client Profile Agent

Cisco Sync Agent

Cisco XCP Router

Step 4

Click Restart .

Step 5

From the Related Links drop-down list, select Service Activation and click Go .

Step 6

In the IM and Presence Services area, select the following services:

Cisco SIP Proxy

Cisco Presence Engine

Step 7

Click Save .

### Assign  the LDAP Source for Directory URIs

If you are syncing users from an external LDAP directory, you can use this procedure to assign the external LDAP Directory
                                 source field that is used to assign the directory URI. When your LDAP directory sync occurs, the directory URI will be assigned
                                 from the value of the field that you configure.

You cannot apply edits to an existing LDAP configuration in Cisco Unified Communications Manager if the initial sync has already
                                             occured. You can sync new items that were added to the external LDAP directory, but you cannot edit the LDAP configuration
                                             in Cisco Unified Communications Manager. If you've already synced your LDAP directory:

Use the Bulk Administration Tool to assign directory URIs to users.
                                                   For details, see the Bulk Administration Guide for Cisco Unified
                                                      Communications Manager .

Assign the directory URI to a user manually

#### Before you begin

Assign IM Addressing Scheme

Step 1

From Cisco Unified CM Administration, select System > LDAP > LDAP
                                                Directory .

Step 2

From the Directory URI drop-down list, select one of the following options:

- mail : Map the Directory URI to the user's email address to provide a consistent identity for email, IM, voice and video communications.

- msRTCSIP-PrimaryUserAddress : Map the Directory URI to the Microsoft OCS/Lync SIP URI.

#### What to do next

Restart Services

### Manually Assign a Directory URI

If you are not using LDAP, you can use this procedure to enter a Directory URI manually on a user-by-user basis.

You can also use the Bulk Administration Tool to provision directory URIs for a large number of end users via a csv file.
                                             For Bulk Administration details, see the Bulk Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

If you haven't yet synced your LDAP directory, you can provision directory URIs for users via an LDAP directory sync.

#### Before you begin

Assign IM Addressing Scheme

Step 1

In Cisco Unified CM Administration , choose User Management > End User .

Step 2

Enter the appropriate search criteria and click Find .

Step 3

Select the end user that you want to configure.

Step 4

In the User Information area, enter a directory URI in the Directory URI field.

Step 5

Click Save .

#### What to do next

Restart Services

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Verify User Provisioning | Verify that end users are correctly provisioned and that there are no duplicate or invalid users. |
| Step 2 | Disable High Availability | You must temporarily disable high availability for the presence redundancy group. Configuring the IM addressing scheme requires
                                          you to stop services temporarily; if you stop the
                                          services while high availability is enabled, a system failover will
                                          occur. |
| Step 3 | Stop Services | Prior to updating your IM addressing scheme configuration stop essential IM and Presence Services. Make sure to stop services
                                          in the prescribed order. |
| Step 4 | Assign IM Addressing Scheme | Use this procedure to configure a new domain and IM address scheme, or to update an existing domain and address scheme. |
| Step 5 | Restart Services | Once your IM addressing scheme is configured, restart services. You must do this prior to updating user address information
                                          or provisioning new users. Make sure to follow the prescribed order when you restart services. |
| Step 6 | Enable High Availability | You can enable high availability for the presence redundancy groups after you have configured the IM addressing scheme and
                                          restarted IM and Presence services. All services must be running on IM and Presence database publisher nodes and subscriber nodes before you enable high availability. |
| Step 7 | If you chose Directory URI as the IM addressing scheme: Assign the LDAP Source for Directory URIs Manually Assign a Directory URI | Optional. If you are syncing users from an external LDAP directory, set the LDAP source field for your directory URI values. For non-LDAP users, you must provision directory URIs manually. You can do this on a user-by-user basis, or via the Bulk Administration
                                          Tool. |

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter . The System Troubleshooter runs. |
|---|---|
| Step 2 | In the User Troubleshooter section, verify that end users are correctly provisioned and that there are no duplicate or invalid users. |

| Note | The Presence Redundancy Group Details page shows all the active JSM sessions, even when the high availability is disabled in the cluster. |
|---|---|

| Step 1 | From the Cisco Unified CM Administration user interface, choose System > Presence Redundancy Groups . |
|---|---|
| Step 2 | Click Find and select the group. |
| Step 3 | On the Presence Redundancy Group Configuration window, uncheck the Enable High Availability check box. |
| Step 4 | Click Save . |
| Step 5 | Repeat this procedure for each Presence Redundancy Group. |
| Step 6 | When you are done, wait at least two minutes to sync the new HA settings across the cluster before you make any further changes |

| Step 1 | In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center – Network Services . |
|---|---|
| Step 2 | Stop the following IM and Presence Services, in this order, by selecting the service and clicking the Stop button: Cisco Sync Agent Cisco Client Profile Agent |
| Step 3 | After both services have stopped, choose Tools > Control Center – Feature Services and stop the following services in this order: Cisco Presence Engine Cisco SIP Proxy |
| Step 4 | After both services have stopped, choose Tools > Control Center – Feature Services and stop the following service: Cisco XCP Router Note When you stop the XCP Router service, all related XCP feature services stop automatically. | Note | When you stop the XCP Router service, all related XCP feature services stop automatically. |
| Note | When you stop the XCP Router service, all related XCP feature services stop automatically. |

| Note | When you stop the XCP Router service, all related XCP feature services stop automatically. |
|---|---|

| Note | Make sure that the IM addressing scheme that you configure is consistent across all clusters. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Presence > Settings > Advanced Configuration. |
|---|---|
| Step 2 | To assign a new default domain, check the Default Domain check box and, in the text box, enter the new domain. |
| Step 3 | To change the address scheme, check the IM Address Scheme check box, and select one of the following options from the drop-down list box: UserID@[Default_Domain] — Each IM user address is derived from the UserID along with the default domain. This is the default setting. Directory URI — Each IM user address matches the directory URI that is configured for that user in Cisco Unified Communications Manager. Note When you choose this option, all deployed clients must support Directory URI as the IM address and use either EDI-based or
                                                            UDS-based directory integration. For UDS-based integration with Jabber, you must be running Jabber Release 10.6 or later. | Note | When you choose this option, all deployed clients must support Directory URI as the IM address and use either EDI-based or
                                                            UDS-based directory integration. For UDS-based integration with Jabber, you must be running Jabber Release 10.6 or later. |
| Note | When you choose this option, all deployed clients must support Directory URI as the IM address and use either EDI-based or
                                                            UDS-based directory integration. For UDS-based integration with Jabber, you must be running Jabber Release 10.6 or later. |
| Step 4 | Click Save. You can monitor the progress of the update in the status area. If you chose Directory URI as the IM address scheme, you may be prompted to ensure that the deployed clients can support multiple
                                             domains. Click OK to proceed or click Cancel . If any user has an invalid Directory URI setting, a dialog box appears. Click OK to proceed or click Cancel , and then fix the user settings before reconfiguring the IM address scheme. A system update can take up to 1 hour to complete. Click Re-try to reapply the changes or click Cancel . |

| Note | When you choose this option, all deployed clients must support Directory URI as the IM address and use either EDI-based or
                                                            UDS-based directory integration. For UDS-based integration with Jabber, you must be running Jabber Release 10.6 or later. |
|---|---|

| IM and Presence Service Default Domain: cisco.com User: John Smith User ID: js12345 Mail ID: jsmith@cisco-sales.com SIPURI: john.smith@webex.com |
|---|

| IM Address Format | Directory URI Mapping | IM Address |
|---|---|---|
| <userid>@<domain> | n/a | js12345@cisco.com |
| Directory URI | mailid | jsmith@cisco-sales.com |
| Directory URI | msRTCSIP-PrimaryUserAddress | john.smith@webex.com |

| Step 1 | In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center – Network Services . |
|---|---|
| Step 2 | Start the following service by selecting the service and clicking the Start button: Cisco XCP Router |
| Step 3 | After the service starts, choose Tools > Control Center – Feature Services and start the following services in this order: Cisco SIP Proxy Cisco Presence Engine |
| Step 4 | Confirm that the Cisco Presence Engine service is running on all nodes before proceeding to the next step. |
| Step 5 | Choose Tools > Control Center – Network Services and start the following services in this order: Cisco Client Profile Agent Cisco Sync Agent |

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . |
|---|---|
| Step 2 | From the Server list, choose the node on which you want to reactivate services and click Go . |
| Step 3 | In the IM and Presence Services area, select the following services: Cisco Client Profile Agent Cisco Sync Agent Cisco XCP Router |
| Step 4 | Click Restart . |
| Step 5 | From the Related Links drop-down list, select Service Activation and click Go . |
| Step 6 | In the IM and Presence Services area, select the following services: Cisco SIP Proxy Cisco Presence Engine |
| Step 7 | Click Save . |

| Note | You cannot apply edits to an existing LDAP configuration in Cisco Unified Communications Manager if the initial sync has already
                                             occured. You can sync new items that were added to the external LDAP directory, but you cannot edit the LDAP configuration
                                             in Cisco Unified Communications Manager. If you've already synced your LDAP directory: Use the Bulk Administration Tool to assign directory URIs to users.
                                                   For details, see the Bulk Administration Guide for Cisco Unified
                                                      Communications Manager . Assign the directory URI to a user manually |
|---|---|

| Step 1 | From Cisco Unified CM Administration, select System > LDAP > LDAP
                                                Directory . |
|---|---|
| Step 2 | From the Directory URI drop-down list, select one of the following options: mail : Map the Directory URI to the user's email address to provide a consistent identity for email, IM, voice and video communications. msRTCSIP-PrimaryUserAddress : Map the Directory URI to the Microsoft OCS/Lync SIP URI. Note The directory URI isn't provisioned until the LDAP sync occurs. For details on configuring an LDAP Directory sync, see Configure LDAP Directory . | Note | The directory URI isn't provisioned until the LDAP sync occurs. For details on configuring an LDAP Directory sync, see Configure LDAP Directory . |
| Note | The directory URI isn't provisioned until the LDAP sync occurs. For details on configuring an LDAP Directory sync, see Configure LDAP Directory . |

| Note | The directory URI isn't provisioned until the LDAP sync occurs. For details on configuring an LDAP Directory sync, see Configure LDAP Directory . |
|---|---|

| Note | You can also use the Bulk Administration Tool to provision directory URIs for a large number of end users via a csv file.
                                             For Bulk Administration details, see the Bulk Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . If you haven't yet synced your LDAP directory, you can provision directory URIs for users via an LDAP directory sync. |
|---|---|

| Step 1 | In Cisco Unified CM Administration , choose User Management > End User . |
|---|---|
| Step 2 | Enter the appropriate search criteria and click Find . |
| Step 3 | Select the end user that you want to configure. |
| Step 4 | In the User Information area, enter a directory URI in the Directory URI field. |
| Step 5 | Click Save . |