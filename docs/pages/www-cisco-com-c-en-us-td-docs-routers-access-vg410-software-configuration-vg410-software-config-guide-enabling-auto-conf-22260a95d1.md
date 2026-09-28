---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-enabling-auto-conf-22260a95d1
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/enabling-auto-configuration.html
retrieved_at: 2026-08-22T01:18:22.059679+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Enabling Auto Configuration

## Chapter: Enabling Auto Configuration

# Enabling Auto Configuration

Feature or Enhancement

IOS XE Release

Feature Description

Support for Auto Configuration

Cisco IOS XE 16.12.1a and later

This feature allows you to simplify SIP line configurations by pushing an XML configuration file from the CUCM to the voice
                                    gateway. This, in turn, provides ease of configuring dial peer automatically. Auto Configuration also saves you the time and
                                    efforts to manually configure the port and phone number for each FXS port.

Enhancements to Auto-Configuration

Cisco IOS XE 17.15.1a

Secure flag in XML configuration file : The XML Auto Configuration file contains a secure flag, which indicates whether the SIP line is secure or not.

Failover or fallback for Auto Configuration : Failover/fallback is also configured without manual intervention, from this release.

Individual tenant-based configuration for each SIP line endpoint to register individually is supported. This enhancement provides
                                          the flexibility to enable features such as failover/fallback at a port level rather than on a system level.

## Enabling the Auto Configuration

For the auto configuration to work, you must first specify the CUCM to the SIP line. Doing so indicates that the CUCM is the
                           configuration server to the SIP line. To perform this step and enable the SIP line auto-configuration feature, run the ccm-manager sipana auto-config local command.

Then, run the ccm-manager config server command. This command initiates a download request of the configuration file. After the file is downloaded from the CUCM
                           server, the XML file is parsed to determine the number of ports that are configured on the CUCM and the corresponding port
                           IDs. The auto configuration then processes all the port information before configuring the corresponding dial-peers to set
                           the endpoint to a SIP line. The dial-peers are added for each of the endpoints that are configured on CUCM.

For DSAPP auto-configuration, only pots dial-peer is auto configured. You must manually configure the outbound dial-peer and
                                       the voice card.

```
!
ccm-manager sipana auto-config local GigabitEthernet x/y/z
!
ccm-manager config server x.x.x.x
```

Here, GigabitEthernet x/y/z  is the interface that is used for the SIP signaling.

### Sample Configuration

```
! 
ccm-manager sipana auto-config local GigabitEthernet0/0/1
!
ccm-manager config server 172.19.156.84                                                                                                                            
!
```

## Prerequisites

This list specifies the prerequisites that are required for Auto Configuration to work as expected.

Your CUCM version should be 15 SU2 or later.

All the FXS ports should be onhook state. To check whether all the FXS ports are onhook state, run the show voice call summary command.

## Enable Auto Configuration

To trigger Auto Configuration, perform the following configurations on the voice gateway:

### Before you begin

Ensure a TFTP server is enabled from CUCM to download the XML configuration files to the gateway and a local ethernet interface
                              needs to be configured so that the gateway and the endpoint’s MAC address can be obtained.

### SUMMARY STEPS

- enable

- configure terminal

- ccm-manager config server <cucm ipv4 address1> <cucm ipv4 address2> or ccm-manager config server <cucm ipv6 address1> <cucm ipv6 address2>

- ccm-manager sipana auto-config local <interface>

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

ccm-manager config server <cucm ipv4 address1> <cucm ipv4 address2> or ccm-manager config server <cucm ipv6 address1> <cucm ipv6 address2>

### Example:

```
ccm-manager config server 10.12.1.1
```

Specifies the IP address of the CUCM server that acts as the TFTP server for downloading the configuration file.

Step 4

ccm-manager sipana auto-config local <interface>

### Example:

```
ccm-manager sipana auto-config local GigabitEthernet x/y/z
```

Specifies the CUCM to the SIP line, which indicates that the CUCM is the configuration server to the SIP line. In the example, GigabitEthernet x/y/z is the interface that is used for the SIP signaling.

After the file is downloaded from the CUCM server, the XML file is parsed to determine the number of ports that are configured
                              on the CUCM and the corresponding port IDs. The auto configuration then processes all the port information before configuring
                              the corresponding dial-peers to set the endpoint to a SIP line. The dial-peers are added for each of the endpoints that are
                              configured on the CUCM.

### Sample Configuration

```
ccm-manager config server 172.19.156.84
!
ccm-manager sipana auto-config local GigabitEthernet0/0/1
```

For IPv6 mode, run this CLI before executing

```
ccm-manager sipana auto-config local GigabitEthernet0/0/1"
         sip-ua
         protocol mode ipv6
```

## Failover

From Cisco IOS XE 17.15.1a release, failover and fallback functionalities are supported as a part of Auto Configuration. No
                           manual configuration is needed to enable these functionalities in your Voice Gateway. However, you must configure the primary
                           and secondary CUCM nodes to the same cluster for failover and fallback to work as expected.

### What is failover?

A failover is a scenario where the endpoints are forced to transition from the primary CUCM to the secondary CUCM. Failovers
                              can be triggered due to network outage, socket errors, and send failures.

### When is a failover triggered?

A failover is triggered in the scenarios listed in this section:

If a SIP 503 message response is received from the CUCM when making a call, failover is triggered.

A failover is typically triggered per endpoint. However, since all the endpoints share the same socket, in the event of a
                                    socket error, all the registrations tied to the socket experience failover.

During normal operation, polling is run in the background to send a REGISTER message to the active CUCM. Here, the keep alive
                                    timer depends on the response of the SIP message. When the register message polling fails, it could trigger a failover.

Failovers can also happen with an active call. In this scenario, the media of the active call is preserved, but signaling
                                    is not preserved.

The outbound proxy is an FQDN, and this proxy will be runtime resolved to the primary and secondary servers' IP addresses.
                              If the primary server fails, the system will failover to the secondary server, which is the end of the list. In this scenario,
                              there will be a wait for a few minutes before the next DNS query to the primary server again.

## Fallback

Fallback is a scenario when endpoints fall back to the primary CUCM from secondary. Fallback happens in the following scenarios:

When a periodic register message polling fails, for example, during a network outage, socket error, or during a no 200 OK
                                 response, fallback could be triggered with or without an active call.

After the DNS cache timer expires. A fresh DNS request is triggered to refresh the proxy IP table. In this scenario, fallback
                                 happens without an active call and if the primary CUCM is responsive.

## CUCM Restart State

When the Voice Gateway cannot communicate to the CUCM, but the CUCM is in an active state, the CUCM might get into a timeout
                           state as it does not receive the REGISTER message from the Voice Gateway. The CUCM then transitions to a restart state. The
                           active CUCM node fails and the standby CUCM then becomes active. The newly active CUCM might be in restart state and it could
                           take up to 30 seconds for the CUCM to the active state.

After a failover or a fallback, wait until the standby becomes active before making any calls. If call is made before the
                                       standby CUCM is ready, calls fail with a SIP 503 error message.

| Feature or Enhancement | IOS XE Release | Feature Description |
|---|---|---|
| Support for Auto Configuration | Cisco IOS XE 16.12.1a and later | This feature allows you to simplify SIP line configurations by pushing an XML configuration file from the CUCM to the voice
                                    gateway. This, in turn, provides ease of configuring dial peer automatically. Auto Configuration also saves you the time and
                                    efforts to manually configure the port and phone number for each FXS port. |
| Enhancements to Auto-Configuration | Cisco IOS XE 17.15.1a | Secure flag in XML configuration file : The XML Auto Configuration file contains a secure flag, which indicates whether the SIP line is secure or not. Failover or fallback for Auto Configuration : Failover/fallback is also configured without manual intervention, from this release. Individual tenant-based configuration for each SIP line endpoint to register individually is supported. This enhancement provides
                                          the flexibility to enable features such as failover/fallback at a port level rather than on a system level. |

| Note | For DSAPP auto-configuration, only pots dial-peer is auto configured. You must manually configure the outbound dial-peer and
                                       the voice card. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | ccm-manager config server <cucm ipv4 address1> <cucm ipv4 address2> or ccm-manager config server <cucm ipv6 address1> <cucm ipv6 address2> Example: ccm-manager config server 10.12.1.1 | Specifies the IP address of the CUCM server that acts as the TFTP server for downloading the configuration file. |
| Step 4 | ccm-manager sipana auto-config local <interface> Example: ccm-manager sipana auto-config local GigabitEthernet x/y/z | Specifies the CUCM to the SIP line, which indicates that the CUCM is the configuration server to the SIP line. In the example, GigabitEthernet x/y/z is the interface that is used for the SIP signaling. |

| Note | After a failover or a fallback, wait until the standby becomes active before making any calls. If call is made before the
                                       standby CUCM is ready, calls fail with a SIP 503 error message. |
|---|---|