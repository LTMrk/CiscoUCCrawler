---
doc_id: help-webex-com-en-us-article-nt45atdb-615acf5fc8
source_url: https://help.webex.com/en-us/article/nt45atdb
retrieved_at: 2026-11-02T13:12:34.692565+00:00
---

## Mobile and Remote Access (MRA)

Mobile and Remote Access (MRA) lets remote workers easily and securely connect into the corporate network without using a virtual private network (VPN) client tunnel.

When users are away from the office, the phone detects that it is in off-premises mode. As administrator, you can generate a 16-digit activation code for users to register their phones to Cisco Unified Communications Manager (Unified CM). If the phones have been configured with alternate TFTP, ask the users to clear the phone settings with a factory reset in the phone menu so they can register the phone with the activation code through MRA.

During the phone registration process, the phone synchronizes the displayed date and time with the Network Time Protocol (NTP) server. With MRA, the DHCP option 42 tag is used to locate the IP addresses of the NTP servers designated for time and date synchronization. If the DHCP option 42 tag is not found in the configuration information, the phone looks for the 0.tandberg.pool.ntp.org tag to identify the NTP servers.

After registration, the phone uses information from the SIP message to synchronize the displayed date and time unless an NTP server is configured in the phone configuration on Unified CM.

If the phone security profile for any of your phones has TFTP Encrypted Config checked,
          you cannot use the phone with Mobile and Remote Access. The MRA solution does not support
          device interaction with Certificate Authority Proxy Function (CAPF).

For SIP OAuth in Mobile and Remote Access (MRA) mode, use only Activation Code Onboarding
          with Mobile and Remote Access when you deploy the phone. Activation with a username and
          password is not supported.

SIP OAuth mode requires Expressway x12.7(1) or later, and Cisco Unified Communications Manager 14.0(1) or later.

For additional information on SIP OAuth mode, see the SIP OAuth Mode section
          in Feature Configuration Guide for Cisco Unified
            Communications Manager , Release 14.0(1) or later.

### MRA for Expressway

MRA works with Cisco Expressway. You must be familiar with the Cisco Expressway documentation available at http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/tsd-products-support-series-home.html .

Only the IPv4 protocol is supported for Mobile and Remote Access
				Through Expressway users.

For additional information about working with Mobile and Remote Access
				Through Expressway, see:

Cisco Preferred Architecture for Enterprise Collaboration, Design Overview

Versions: 12.x | 11.0 | 10.x

Cisco Preferred Architecture for Enterprise Collaboration, CVD

Versions: 12.x | 11.0 | 10.x

Unified Communications Mobile and Remote Access via Cisco VCS Deployment Guide

Versions: 8.11 | 8.10 | 8.9 | 8.8 | 8.7 | 8.6 | 8.5 | 8.2 | 8.1.1 |

## Configure user credentials persistent for Expressway sign-in

When a user signs in to the network with Mobile and Remote Access Through Expressway, the user is prompted for a service domain, username, and password. Typically, the sign-in procedure occurs when the phone is under registration, after a phone reboot or firmware upgrade.

If you enable the feature, user login credentials are stored so that users do not need to enter this sign-in information again. This feature is disabled by default.

You can set up credentials to persist for a single phone, a group of phones, or all phones.

In the Cisco Unified Communications Manager Administration, select one of the following windows:

- Select Device > Phone .

- Select Device > Device Settings > Common Phone Profile .

- Select System > Enterprise Phone Configuration .

Navigate to the Product Specific Configuration Layout area and set the following field:

User Credentials Persistent for Expressway Sign in : Determine whether the phone stores the users' sign-in credentials.

Disabled : The user is always prompted to sign into the Expressway server for Mobile and Remote Access (MRA) after the phone reboots.

Enabled : The Expressway login credentials are persistent. The user then only has to enter their login credentials for the first time.

Default value: Disabled

Click Save .

## Phone features available for MRA

Mobile and Remote Access (MRA) provides secure VPN-less access to collaboration services for Cisco mobile and remote users. But to preserve network security, it limits access to some phone features.

The following list shows the phone features available with MRA.

Phone feature

8875 release (recommended)

| 1 | In the Cisco Unified Communications Manager Administration, select one of the following windows: Select Device > Phone . Select Device > Device Settings > Common Phone Profile . Select System > Enterprise Phone Configuration . |
|---|---|
| 2 | Navigate to the Product Specific Configuration Layout area and set the following field: User Credentials Persistent for Expressway Sign in : Determine whether the phone stores the users' sign-in credentials. Disabled : The user is always prompted to sign into the Expressway server for Mobile and Remote Access (MRA) after the phone reboots. Enabled : The Expressway login credentials are persistent. The user then only has to enter their login credentials for the first time. Default value: Disabled |
| 3 | Click Save . |

| Phone feature | 8875 release (recommended) | 9800 Series release (recommended) |
|---|---|---|
| Audio/Video Call | 2.1 and later | 3.1 and later |
| Auto Answer | 3.3 and later | 3.3 and later |
| Barge and cBarge | 3.3 and later | 3.3 and later |
| Busy Lamp Field (BLF) | 3.3 and later | 3.3 and later |
| Busy Lamp Field (BLF) Pickup | 3.3 and later | 3.1 and later |
| Busy Lamp Field (BLF) Speed Dial | 3.3 and later | 3.1 and later |
| Call Back | 3.3 and later | 3.1 and later |
| Call Forward | 3.3 and later | 3.1 and later |
| Call Forward Notification | 3.3 and later | 3.3 and later |
| Call Park | 3.3 and later | 3.3 and later |
| Call Pickup | 3.3 and later | 3.3 and later |
| Conf Tranf Active Call | 3.3 and later | 3.3 and later |
| Conference | 2.1 and later | 3.1 and later |
| Conference List / Remove Participant | 3.3 and later | 3.3 and later |
| Contacts | 3.3 and later | 3.1 and later |
| Corporate Directory | 3.3 and later | 3.3 and later |
| Decline incoming call | 2.1 and later | 3.1 and later |
| Direct Transfer | 3.3 and later | 3.3 and later |
| Directed Call Park | 3.3 and later | 3.3 and later |
| Divert | 3.3 and later | 3.3 and later |
| DND | 2.1 and later | 3.1 and later |
| Failover/Fallback | 3.3 and later | 3.1 and later |
| Forced Access Codes and Client Matter Codes | 3.3 and later | 3.3 and later |
| Group Call Pickup | 3.3 and later | 3.3 and later |
| Hold/Resume | 2.1 and later | 3.1 and later |
| Hold Reversion | 3.3 and later | 3.3 and later |
| Ignore incoming call | 3.3 and later | 3.1 and later |
| Immediate Divert | 3.3 and later | 3.3 and later |
| Intercom | 3.3 and later | 3.1 and later |
| KEM with same capabilities (only for 9851/9861/9871) | N/A | 3.3 and later |
| Meet Me Conference | 3.3 and later | 3.3 and later |
| Message Waiting Indicator | 2.1 and later | 3.1 and later |
| Multilevel Precedence and Preemption (MLPP) | 3.3 and later | 3.3 and later |
| Multiple Calls | 3.3 and later | 3.3 and later |
| Multiple Lines | 2.1 and later | 3.1 and later |
| Music On Hold | 3.3 and later | 3.3 and later |
| Mute | 3.3 and later | 3.3 and later |
| Off-hook Dialing | 2.1 and later | 3.1 and later |
| On-hook Dialing | 2.1 and later | 3.1 and later |
| Plus Dialing | 3.3 and later | 3.3 and later |
| Privacy | 2.1 and later | 3.1 and later |
| Private Line Automated Ringdown (PLAR) | 3.3 and later | 3.3 and later |
| PRT | 3.3 and later | 3.1 and later |
| Recents | 3.3 and later | 3.1 and later |
| Redial | 2.1 and later | 3.1 and later |
| Reset/Restart | 3.3 and later | 3.1 and later |
| Security-encrypted mode | 3.3 and later | 3.1 and later |
| Services URL button | 3.3 and later | 3.3 and later |
| Shared line | 2.1 and later | 3.1 and later |
| Speed Dial | 2.1 and later | 3.1 and later |
| Transfer | 2.1 and later | 3.1 and later |
| Upgrade/downgrade | 3.3 and later | 3.1 and later |
| Uniform Resource Identifier (URI) Dialing | 2.1 and later | 3.1 and later |
| Voicemail | 2.1 and later | 3.1 and later |