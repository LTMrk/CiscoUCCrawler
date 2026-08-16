---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-systemconfig-cucm-b-system-configuration-guide-15-cucm-b-syste-199894d95d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15/cucm_b_system-configuration-guide-14_chapter_01010.html
retrieved_at: 2026-08-16T16:08:46.046857+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: August 7, 2026

Chapter: Configure SRST

## Chapter: Configure SRST

# Configure SRST

## Survivable Remote Site Telephony Overview

Survivable Remote Site Telephony (SRST) is an optional feature for sites that depend on a Wide Area Network (WAN) connection
                           to a Unified Communications Manager node. SRST references, which are configured in the Unified Communications Manager Administration interface, allow IP gateways to provide limited telephony service to IP phones at the remote site in the event of a WAN outage:

IP phones at the remote site can call each other

calls from the PSTN can reach the IP phones

calls from the IP phones can reach the external world through the PSTN

When phones at the remote site lose connectivity to all associated Unified Communications Manager nodes, the phones connect to the SRST reference IP gateway. The status line indication on the IP phone shows the phone has
                           failed over to the backup SRST gateway. When the connection to Unified Communications Manager is restored, the IP phones reregister with Unified Communications Manager and full telephony services are restored.

SRST supports remote sites that may have a mix of SCCP and SIP endpoints in addition to PSTN gateway access.

### Connection Monitor Duration

An IP phone that connects to an SRST gateway over a Wide Area Network (WAN) reconnects itself to Unified Communications Manager as soon as it can establish a connection with Unified Communications Manager over the WAN link. However, if the WAN link is unstable, the IP phone switches back and forth between the SRST gateway and Unified Communications Manager . This situation causes temporary loss of phone service (no dial tone). These reconnect attempts, known as WAN link flapping
                              issues, continue until the IP phone successfully reconnects itself to Unified Communications Manager .

To resolve the WAN link flapping issues between Unified Communications Manager and an SRST gateway, you can define the number of seconds (Connection Monitor Duration) that the IP Phone monitors its connection
                              to Unified Communications Manager before it unregisters from the SRST gateway and reregisters to Unified Communications Manager . The IP phone receives the connection monitor duration value in the XML configuration file.

## Survivable Remote
                        	 Site Telephony Configuration Task Flow

### Before you begin

Examine the dial plan. If there are 7 or 8 digits in the dial plan, you may need to configure translation rules. For more
                              information about translation rules, see Configure Translation Patterns .

Step 1

Configure an SRST Reference

Step 2

Assign the SRST Reference to a Device Pool

Step 3

Perform one of
                                       			 the following tasks:

- Configure Connection Monitor Duration for the Cluster

- Configure Connection Monitor Duration for a Device Pool

Optional : Configure the connection monitor duration. You can apply a cluster-wide default value, or apply the configuration to the
                                          devices in a device pool.

Step 4

Enable SRST on the SRST Gateway

### Configure an SRST Reference

An SRST reference comprises the gateway that can provide limited Cisco Unified Communications Manager functionality when all other Cisco Unified Communications Manager nodes for a device are unreachable.

Step 1

Log into Cisco Unified CM Administration and choose System > SRST .

Step 2

Click Add New .

Step 3

Configure the fields in the SRST Reference Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

### Assign the SRST
                           	 Reference to a Device Pool

You can configure
                                 		  SRST for each device pool of phones. When you assign an SRST reference to a
                                 		  device pool, all phones in the device pool try to connect to the assigned SRST
                                 		  gateway if they cannot reach any Cisco Unified Communications Manager node.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Device
                                                				  Pool .

Step 2

Click Find and choose the device pool to which the remote
                                          			 IP phones are registered.

Step 3

In the Roaming
                                          			 Sensitive Settings area, choose the SRST reference from the SRST
                                             				Reference drop-down list.

The SRST
                                                				  Reference drop-down list contains the following options:

Disable —If a phone cannot reach any Cisco Unified
                                                      						Communications Manager node, it does not try to connect to an SRST
                                                   					 gateway.

Use Default Gateway —If a phone cannot reach any Cisco Unified
                                                      						Communications Manager node, it tries to connect to its IP gateway as
                                                   					 an SRST gateway.

User-Defined —If a phone cannot reach any Cisco Unified Communications Manager node, it tries to connect to this SRST gateway.

Step 4

Click Save .

### Configure Connection Monitor Duration for the Cluster

This procedure is optional. Complete this procedure only if you want to change the system value (enterprise parameter) for
                                 the  connection monitor duration.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

Enter a value in the Connection Monitor Duration field. The default value is 120 seconds. The maximum number of seconds that you can enter in the field
                                          is 2592000.

Step 3

Click Save .

You must restart all services for the change to take effect.

The enterprise parameter forms the cluster default for the Connection Monitor Duration. However, if an overriding configuration
                                                         exists within a device pool, that setting overrides the enterprise parameter setting for the devices that use the device pool.

### Configure Connection Monitor Duration for a Device Pool

This procedure is optional. Complete this procedure only if the following is true:

You do not want to use the cluster-wide value for the connection monitor duration.

You want to define a separate connection monitor duration value for this device pool.

Tip

When you change the value of the connection monitor duration for a device pool, it
                                             applies only to the device pool that is being updated. All other
                                             device pools use the value in their own Connection Monitor Duration
                                             fields or use the cluster-wide value that is configured in the Connection Monitor Duration enterprise
                                             parameter.

Step 1

From Cisco Unified CM Administration, choose System > Device Pool .

Step 2

Click Find and choose the device pool to which the remote IP phones are registered.

Step 3

In the Roaming Sensitive Settings area, enter a value in the Connection Monitor Duration field. The maximum number of seconds that you can enter in the field
                                          is 2592000.

This setting overrides the enterprise parameter setting for connection monitor duration.

Step 4

Click Save .

### Enable SRST on the
                           	 SRST Gateway

#### Before you begin

Assign the SRST Reference to a Device Pool

(Optional) Perform one of the following tasks:

Configure Connection Monitor Duration for the Cluster

Configure Connection Monitor Duration for a Device Pool

Step 1

Log into the
                                          			 SRST gateway (router).

Step 2

Enter the
                                          			 command call-manager-fallback

Step 3

Enter the
                                          			 command max-ephones max-phones , where max-phones is the maximum number of supported Cisco
                                          			 IP phones.

Step 4

Enter the
                                          			 command max-dn max-directory-numbers where max-directory-numbers is the maximum number of
                                          			 directory numbers (DN) or virtual voice ports that can be supported by a
                                          			 router.

Step 5

Enter the
                                          			 command ip
                                             				source-address ip-address where ip-address is a preexisting router IP address,
                                          			 typically one of the addresses of the Ethernet port of the router.

## SRST
                        	 Restrictions

Restriction

Description

Deleting SRST References

You cannot delete SRST references that device pools or other items are using. To find out which device pools are using the
                                       SRST reference, click the Dependency Records link from the SRST Reference Configuration window. If the dependency records are not enabled for the system, the dependency records summary window displays a message.
                                       If you try to delete an SRST reference that is in use, Unified Communications Manager displays an error message. Before you delete an SRST reference that is currently in use, perform either or both of the following
                                       tasks:

Assign a different SRST reference to any device pools that are using the SRST reference that you want to delete.

Delete the device pools that are using the SRST reference that you want to delete.

Before you delete an SRST reference, check carefully to ensure that you are deleting the correct SRST reference. You cannot
                                                   retrieve deleted SRST references. If an SRST reference is accidentally deleted, you must rebuild it.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure an SRST Reference | Configure the gateway that can provide limited call control functionality when all other Unified Communications Manager nodes are unreachable. |
| Step 2 | Assign the SRST Reference to a Device Pool | For each device pool, assign the gateways that calling devices search when they attempt to complete a call if Unified Communications Manager is unavailable. |
| Step 3 | Perform one of
                                       			 the following tasks: Configure Connection Monitor Duration for the Cluster Configure Connection Monitor Duration for a Device Pool | Optional : Configure the connection monitor duration. You can apply a cluster-wide default value, or apply the configuration to the
                                          devices in a device pool. |
| Step 4 | Enable SRST on the SRST Gateway | Configure SRST parameters on the gateway. |

| Step 1 | Log into Cisco Unified CM Administration and choose System > SRST . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Configure the fields in the SRST Reference Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Device
                                                				  Pool . |
|---|---|
| Step 2 | Click Find and choose the device pool to which the remote
                                          			 IP phones are registered. |
| Step 3 | In the Roaming
                                          			 Sensitive Settings area, choose the SRST reference from the SRST
                                             				Reference drop-down list. The SRST
                                                				  Reference drop-down list contains the following options: Disable —If a phone cannot reach any Cisco Unified
                                                      						Communications Manager node, it does not try to connect to an SRST
                                                   					 gateway. Use Default Gateway —If a phone cannot reach any Cisco Unified
                                                      						Communications Manager node, it tries to connect to its IP gateway as
                                                   					 an SRST gateway. User-Defined —If a phone cannot reach any Cisco Unified Communications Manager node, it tries to connect to this SRST gateway. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Enter a value in the Connection Monitor Duration field. The default value is 120 seconds. The maximum number of seconds that you can enter in the field
                                          is 2592000. |
| Step 3 | Click Save . Note You must restart all services for the change to take effect. The enterprise parameter forms the cluster default for the Connection Monitor Duration. However, if an overriding configuration
                                                         exists within a device pool, that setting overrides the enterprise parameter setting for the devices that use the device pool. | Note | You must restart all services for the change to take effect. The enterprise parameter forms the cluster default for the Connection Monitor Duration. However, if an overriding configuration
                                                         exists within a device pool, that setting overrides the enterprise parameter setting for the devices that use the device pool. |
| Note | You must restart all services for the change to take effect. The enterprise parameter forms the cluster default for the Connection Monitor Duration. However, if an overriding configuration
                                                         exists within a device pool, that setting overrides the enterprise parameter setting for the devices that use the device pool. |

| Note | You must restart all services for the change to take effect. The enterprise parameter forms the cluster default for the Connection Monitor Duration. However, if an overriding configuration
                                                         exists within a device pool, that setting overrides the enterprise parameter setting for the devices that use the device pool. |
|---|---|

| Tip | When you change the value of the connection monitor duration for a device pool, it
                                             applies only to the device pool that is being updated. All other
                                             device pools use the value in their own Connection Monitor Duration
                                             fields or use the cluster-wide value that is configured in the Connection Monitor Duration enterprise
                                             parameter. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Device Pool . |
|---|---|
| Step 2 | Click Find and choose the device pool to which the remote IP phones are registered. |
| Step 3 | In the Roaming Sensitive Settings area, enter a value in the Connection Monitor Duration field. The maximum number of seconds that you can enter in the field
                                          is 2592000. Note This setting overrides the enterprise parameter setting for connection monitor duration. | Note | This setting overrides the enterprise parameter setting for connection monitor duration. |
| Note | This setting overrides the enterprise parameter setting for connection monitor duration. |
| Step 4 | Click Save . |

| Note | This setting overrides the enterprise parameter setting for connection monitor duration. |
|---|---|

| Step 1 | Log into the
                                          			 SRST gateway (router). |
|---|---|
| Step 2 | Enter the
                                          			 command call-manager-fallback This
                                          			 command enables SRST on the router. |
| Step 3 | Enter the
                                          			 command max-ephones max-phones , where max-phones is the maximum number of supported Cisco
                                          			 IP phones. |
| Step 4 | Enter the
                                          			 command max-dn max-directory-numbers where max-directory-numbers is the maximum number of
                                          			 directory numbers (DN) or virtual voice ports that can be supported by a
                                          			 router. |
| Step 5 | Enter the
                                          			 command ip
                                             				source-address ip-address where ip-address is a preexisting router IP address,
                                          			 typically one of the addresses of the Ethernet port of the router. This command enables the SRST router to receive messages from Cisco IP Phones through the specified IP address. |

| Restriction | Description |
|---|---|
| Deleting SRST References | You cannot delete SRST references that device pools or other items are using. To find out which device pools are using the
                                       SRST reference, click the Dependency Records link from the SRST Reference Configuration window. If the dependency records are not enabled for the system, the dependency records summary window displays a message.
                                       If you try to delete an SRST reference that is in use, Unified Communications Manager displays an error message. Before you delete an SRST reference that is currently in use, perform either or both of the following
                                       tasks: Assign a different SRST reference to any device pools that are using the SRST reference that you want to delete. Delete the device pools that are using the SRST reference that you want to delete. Note Before you delete an SRST reference, check carefully to ensure that you are deleting the correct SRST reference. You cannot
                                                   retrieve deleted SRST references. If an SRST reference is accidentally deleted, you must rebuild it. | Note | Before you delete an SRST reference, check carefully to ensure that you are deleting the correct SRST reference. You cannot
                                                   retrieve deleted SRST references. If an SRST reference is accidentally deleted, you must rebuild it. |
| Note | Before you delete an SRST reference, check carefully to ensure that you are deleting the correct SRST reference. You cannot
                                                   retrieve deleted SRST references. If an SRST reference is accidentally deleted, you must rebuild it. |

| Note | Before you delete an SRST reference, check carefully to ensure that you are deleting the correct SRST reference. You cannot
                                                   retrieve deleted SRST references. If an SRST reference is accidentally deleted, you must rebuild it. |
|---|---|