---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-c104920caf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01001010.html
retrieved_at: 2026-08-16T17:36:53.350450+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure QoS with APIC-EM Controller

## Chapter: Configure QoS with APIC-EM Controller

# Configure QoS with APIC-EM Controller

## APIC-EM Controller Overview

The APIC-EM Controller provides a centralized system for
                              managing network traffic so that you always have the bandwidth to
                              maintain communications, even in congested networks. You can configure Cisco Unified Communications Manager to use the APIC-EM
                              Controller to manage SIP media flows thereby providing the following benefits:

Centralizes QoS management, thereby eliminating the need for
                                    endpoints to assign DSCP values.

Applies differential QoS treatment for different media flows. For
                                    example, you can prioritize audio over video to ensure that basic
                                    audio communication is always maintained, even when network bandwidth is
                                    low.

External QoS setting in the SIP Profile allows you to target which
                                    users will use the APIC-EM. For example, you may have Cisco Jabber
                                    users use the APIC-EM to manage media flows, while Cisco Unified IP
                                    Phone users use the DSCP settings in Cisco Unified Communications
                                    Manager.

### SIP Media Flow Management

For SIP calls that use APIC-EM, Cisco Unified
                              Communications Manger sends the policy request to the APIC-EM
                              Controller at the call outset notifying the APIC-EM of the media flow that is being set up. The
                              policy request contains information about the call, including the IP
                              address and ports for source and destination devices, the media
                              type for the flow and the protocol.

The APIC-EM notifies the switch at the
                              beginning of the call flow of the DSCP values for the associated
                              media flows. The switch inserts those DSCP values into individual
                              media packets, overwriting any values that the endpoint inserts. If
                              a gateway in the call flow experiences congestion, that gateway
                              sends through the packets with the higher DSCP values first. This
                              ensures that high priority audio and video streams are not blocked
                              by lower-priority network traffic such as email, print jobs, or
                              software downloads. When the call ends, Cisco Unified Communications Manager notifies the APIC-EM and the APIC-EM notifies
                              the
                              switch to delete the flow.

### External QoS Support

In order for Cisco Unified Communications Manager to use the APIC-EM to manage media flows, the External QoS
                              parameter must be enabled at both the system level, via a clusterwide service
                              parameter, and at the device level, via the SIP Profile.

## APIC-EM Controller Prerequisites

Before using APIC-EM, you must do the following:

Configure DSCP priority for different SIP media flows in Cisco Unified Communications Manager. For details, see DSCP Settings Configuration Task Flow .

Configure the APIC-EM controller hardware within your network. For details, see the hardware documentation that comes with
                                 the APIC-EM controller.

## APIC-EM Controller Configuration Task Flow

Complete these tasks on Cisco Unified Communications Manager to enable APIC-EM Controller to manage SIP media flows.

### Before you begin

Review APIC-EM Controller Prerequisites .

Step 1

Upload APIC-EM Controller Certificate

Upload the APIC-EM certificate into Cisco Unified OS Administration.

Step 2

Configure HTTPS Connection to APIC-EM Controller

Configure an HTTP Profile that points to the APIC-EM service.

Step 3

Enable External QoS Service for System

Enable the External QoS Enable service parameter to configure  the system to use the APIC-EM to manage media flows. The service parameter must be enabled
                                          for devices to use the APIC-EM for SIP media flow management.

You must also enable external QoS within the SIP Profile for devices that will use the APIC-EM for SIP media flow management.

Step 4

Configure External QoS Service at SIP Profile Level

Enable external QoS  within a SIP Profile. All devices that use this SIP Profile will be able to use the APIC-EM to manage
                                          SIP media flows

You can use the SIP Profile setting to configure which devices and device types you want the APIC-EM to manage media flows.

Step 5

Assign SIP Profile to Phones

Associate the external QoS-enabled SIP Profile to a phone.

### Configure the APIC-EM Controller

Use this procedure on the APIC-EM Controller to add Cisco Unified Communications Manager as a user.  APIC-EM's role-based
                                 access control feature provides Cisco Unified Communications Manager with access to APIC-EM resources.

Step 1

On  the APIC-EM Controller, choose Settings > Internal Users .

Step 2

Create a new user with the following role: ROLE_POLICY_ADMIN . Keep track of the username and password that you enter because you must enter identical credentials in Cisco Unified Communications
                                          Manager's HTTP Profile window.

Step 3

Go to the Discovery tab and add a discovery with CDP or the IP address range of the available devices.

Step 4

Select the Device Inventory tab and select the reachable devices.

Step 5

Click  on Set Policy Tag .

Step 6

Create  a policy tag and set it for the devices.

Step 7

On  the EasyQoS tab, select the policy that you created and enable DynamicQoS .

#### What to do next

Upload APIC-EM Controller Certificate

### Upload APIC-EM Controller Certificate

Use this procedure to upload the APIC-EM controller certificate into Cisco Unified Communications Manager.

Step 1

From Cisco Unified OS Administration, choose Security > Certificate Management .

Step 2

Click Upload Certificate/Certificate Chain .

Step 3

From the Certificate Purpose drop-down list, choose CallManager-trust .

Step 4

Enter a Description for the certificate.

Step 5

Click Browse to search for, and select, the certificate.

Step 6

Click Upload .

#### What to do next

Configure HTTPS Connection to APIC-EM Controller

### Configure HTTPS Connection to APIC-EM Controller

Use this procedure to set up an HTTP Profile to connect Cisco Unified Communications Manager to the APIC-EM Controller. In
                                 this connection, Cisco Unified Communications Manager acts as an HTTP user and the APIC-EM acts as the HTTP server.

#### Before you begin

Upload APIC-EM Controller Certificate

Step 1

From Cisco Unified CM Administration, choose Call Routing > HTTP Profile .

Step 2

Enter a Name for the service.

Step 3

Enter the User Name and Password for this HTTP connection. The user name does not have to be a configured end user in Cisco Unified Communications Manager,
                                          but the user name and password must match the values that are configured in the APIC-EM Controller.

Step 4

In the Web Service Root URI text box, enter the IP address or fully qualified domain name of the APIC-EM service.

Step 5

Configure any remaining fields in the HTTP Profile window. For help with the fields and their options, refer to the online
                                          help.

Step 6

Click Save .

#### What to do next

Enable External QoS Service for System

### Enable External QoS Service for System

Use this procedure to configure Cisco Unified Communications Manager to use an external service for QoS management. You must
                                 enable this service parameter in order to use an APIC-EM controller for QoS.

#### Before you begin

Configure HTTPS Connection to APIC-EM Controller

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, select the publisher node.

Step 3

From the Service drop-down list, select Cisco CallManager .

Step 4

Set the value of the External QoS Enabled service parameter to True .

Step 5

Click Save .

To use the APIC-EM to manage call flows for devices, you must also enable external QoS  within the SIP Profile for the device.

#### What to do next

Configure External QoS Service at SIP Profile Level

### Configure External QoS Service at SIP Profile Level

If you have enabled the External QoS Enabled clusterwide service parameter, use this procedure to enable external QoS for SIP devices that use this SIP Profile.

#### Before you begin

Enable External QoS Service for System

Step 1

In Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Do one of the following:

- Click Find and select an existing SIP Profile.

- Click Add New to create a new SIP Profile.

Step 3

Check the Enable External QoS check box. This check box must be checked for   phones that use this SIP Profile to use the APIC-EM Controller to manage
                                          QoS.

Step 4

Complete the remaining fields in the SIP Profile Configuration window. For help with the fields and their settings, see the online help.

Step 5

Click Save .

#### What to do next

Assign SIP Profile to Phones

### Assign SIP Profile to Phones

Use this procedure if you want to assign the external QoS-enabled SIP Profile that you created to a phone.

Tip

Use the Bulk Administration Tool to update the SIP Profile for a large selection of phones in a single operation. For details,
                                             see the Bulk Administration Guide for Cisco Unified Communications Manager.

#### Before you begin

Assign SIP Profile to Phones

Step 1

In Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select an existing phone.

Step 3

From the SIP Profile drop-down list box, select the SIP Profile that you updated for phones that will use the APIC-EM Controller to manage traffic.

Step 4

Complete any remaining fields in the Phone Configuration window. For help with the fields and their settings, see the online help.

Step 5

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Upload APIC-EM Controller Certificate | Upload the APIC-EM certificate into Cisco Unified OS Administration. |
| Step 2 | Configure HTTPS Connection to APIC-EM Controller | Configure an HTTP Profile that points to the APIC-EM service. |
| Step 3 | Enable External QoS Service for System | Enable the External QoS Enable service parameter to configure  the system to use the APIC-EM to manage media flows. The service parameter must be enabled
                                          for devices to use the APIC-EM for SIP media flow management. Note You must also enable external QoS within the SIP Profile for devices that will use the APIC-EM for SIP media flow management. | Note | You must also enable external QoS within the SIP Profile for devices that will use the APIC-EM for SIP media flow management. |
| Note | You must also enable external QoS within the SIP Profile for devices that will use the APIC-EM for SIP media flow management. |
| Step 4 | Configure External QoS Service at SIP Profile Level | Enable external QoS  within a SIP Profile. All devices that use this SIP Profile will be able to use the APIC-EM to manage
                                          SIP media flows You can use the SIP Profile setting to configure which devices and device types you want the APIC-EM to manage media flows. |
| Step 5 | Assign SIP Profile to Phones | Associate the external QoS-enabled SIP Profile to a phone. |

| Note | You must also enable external QoS within the SIP Profile for devices that will use the APIC-EM for SIP media flow management. |
|---|---|

| Step 1 | On  the APIC-EM Controller, choose Settings > Internal Users . |
|---|---|
| Step 2 | Create a new user with the following role: ROLE_POLICY_ADMIN . Keep track of the username and password that you enter because you must enter identical credentials in Cisco Unified Communications
                                          Manager's HTTP Profile window. |
| Step 3 | Go to the Discovery tab and add a discovery with CDP or the IP address range of the available devices. |
| Step 4 | Select the Device Inventory tab and select the reachable devices. |
| Step 5 | Click  on Set Policy Tag . |
| Step 6 | Create  a policy tag and set it for the devices. |
| Step 7 | On  the EasyQoS tab, select the policy that you created and enable DynamicQoS . |

| Step 1 | From Cisco Unified OS Administration, choose Security > Certificate Management . |
|---|---|
| Step 2 | Click Upload Certificate/Certificate Chain . The Upload Certificate/Certificate Chain popup window appears. |
| Step 3 | From the Certificate Purpose drop-down list, choose CallManager-trust . |
| Step 4 | Enter a Description for the certificate. |
| Step 5 | Click Browse to search for, and select, the certificate. |
| Step 6 | Click Upload . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > HTTP Profile . |
|---|---|
| Step 2 | Enter a Name for the service. |
| Step 3 | Enter the User Name and Password for this HTTP connection. The user name does not have to be a configured end user in Cisco Unified Communications Manager,
                                          but the user name and password must match the values that are configured in the APIC-EM Controller. |
| Step 4 | In the Web Service Root URI text box, enter the IP address or fully qualified domain name of the APIC-EM service. |
| Step 5 | Configure any remaining fields in the HTTP Profile window. For help with the fields and their options, refer to the online
                                          help. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, select the publisher node. |
| Step 3 | From the Service drop-down list, select Cisco CallManager . |
| Step 4 | Set the value of the External QoS Enabled service parameter to True . |
| Step 5 | Click Save . Note To use the APIC-EM to manage call flows for devices, you must also enable external QoS  within the SIP Profile for the device. | Note | To use the APIC-EM to manage call flows for devices, you must also enable external QoS  within the SIP Profile for the device. |
| Note | To use the APIC-EM to manage call flows for devices, you must also enable external QoS  within the SIP Profile for the device. |

| Note | To use the APIC-EM to manage call flows for devices, you must also enable external QoS  within the SIP Profile for the device. |
|---|---|

| Note | External QoS must be enabled at both the system level and in the SIP Profile to use the APIC-EM to manage QoS. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Do one of the following: Click Find and select an existing SIP Profile. Click Add New to create a new SIP Profile. |
| Step 3 | Check the Enable External QoS check box. This check box must be checked for   phones that use this SIP Profile to use the APIC-EM Controller to manage
                                          QoS. |
| Step 4 | Complete the remaining fields in the SIP Profile Configuration window. For help with the fields and their settings, see the online help. |
| Step 5 | Click Save . |

| Tip | Use the Bulk Administration Tool to update the SIP Profile for a large selection of phones in a single operation. For details,
                                             see the Bulk Administration Guide for Cisco Unified Communications Manager. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select an existing phone. |
| Step 3 | From the SIP Profile drop-down list box, select the SIP Profile that you updated for phones that will use the APIC-EM Controller to manage traffic. |
| Step 4 | Complete any remaining fields in the Phone Configuration window. For help with the fields and their settings, see the online help. |
| Step 5 | Click Save . |