---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su2-cucm-b-security-guide-1251su2-cucm-b-security-guide--5f219d36ed
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU2/cucm_b_security-guide-1251SU2/cucm_b_security-guide-1251SU2_chapter_010001.html
retrieved_at: 2026-08-21T08:40:41.281612+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: March 22, 2024

Chapter: Voice-Messaging Ports Security Setup

## Chapter: Voice-Messaging Ports Security Setup

# Voice-Messaging Ports Security Setup

This chapter provides information about voice-messaging ports security setup.

## Voice-Messaging Security

To configure security for Unified Communications Manager voice-messaging ports and Cisco Unity devices that are running SCCP or Cisco Unity Connection devices that are running SCCP, you choose a secure device security mode for the port. If you choose an authenticated voicemail
                              port, a TLS connection opens, which authenticates the devices by using a mutual certificate exchange (each device accepts
                              the certificate of the other device). If you choose an encrypted voicemail port, the system first authenticates the devices
                              and then sends encrypted voice streams between the devices.

Cisco Unity Connection connects to Unified Communications Manager through the TLS port. When the device security mode is nonsecure, Cisco Unity Connection connects to Unified Communications Manager through the SCCP port.

In this chapter, the use of the term "server" refers to a Unified Communications Manager server. The use of the phrase "voicemail server" refers to a Cisco Unity server or to a Cisco Unity Connection server.

## Voice-Messaging
                        	 Security Setup Tips

Consider
                              		  the following information before you configure security:

For Cisco Unity , you must perform security tasks by using the Cisco Unity Telephony Integration Manager (UTIM); for Cisco Unity Connection , you must perform security tasks by using Cisco Unity Connection Administration . For information on how to perform these tasks, refer to the applicable Unified Communications Manager integration guide for Cisco Unity or for Cisco Unity Connection .

In addition to the procedures that are described in this chapter, you must use the certificate management feature in Unified Communications Manager to save the Cisco Unity certificate to the trusted store.

For more information, see the "To Add Voice
                                       				  Messaging Ports in Cisco Unity Connection Administration" procedure in the Cisco
                                       				  Unified Communications Manager SCCP Integration Guide for Cisco Unity
                                       				  Connection at the following URL:

http://www.cisco.com/en/US/docs/voice_ip_comm/connection/10x/integration/guide/cucm_sccp/guide/cucintcucmskinny230.html

After you copy the certificate, you must restart the CiscoCallManager service on each Unified Communications Manager server in the cluster.

If Cisco Unity certificates expire or change for any reason, use the certificate management feature in the Administration Guide for Cisco Unified Communications Manager to update the certificates in the trusted store. The TLS authentication fails when certificates do not match, and voice messaging
                                    does not work because it cannot register to Unified Communications Manager .

When configuring
                                    				voice-mail server ports, you must select a device security mode.

The setting that you specify in the Cisco Unity Telephony Integration Manager (UTIM) or in Cisco Unity Connection Administration must match the voice-messaging port device security mode that is configured in Unified Communications Manager Administration . In Cisco Unity Connection Administration , you apply the device security mode to the voice-messaging port in the Voice Mail Port Configuration window (or in the Voice
                                    Mail Port Wizard).

Tip

If the device security mode settings do not match, the voicemail server ports fail to register with Unified Communications Manager , and the voicemail server cannot accept calls on those ports.

Changing the security profile for the port requires a reset of Unified Communications Manager devices and a restart of the voicemail server software. If you apply a security profile in Unified Communications Manager Administration that uses a different device security mode than the previous profile, you must change the setting on the voicemail server.

You cannot change the Device Security Mode for existing voice-mail servers through the VoiceMail Port Wizard. If you add ports
                                    to an existing voicemail server, the device security mode that is currently configured for the profile automatically applies
                                    to the new ports.

## Set Up Secure
                        	 Voice-Messaging Port

The
                              		  following procedure provides the tasks used to configure security for
                              		  voice-messaging ports.

Step 1

Verify that you installed and configured the CiscoCTL Client for Mixed Mode.

Step 2

Verify that you
                                       			 configured the phones for authentication or encryption.

Step 3

Use the certificate management feature in Cisco Unified Communications Operating System Administration to copy the Cisco Unity certificate to the trusted store on the Unified Communications Manager server; then restart the CiscoCallManager service.

For more information, see the Administration Guide for Cisco Unified Communications Manager and Cisco Unified Serviceability Administration Guide .

Tip

Step 4

In Unified Communications Manager Administration , configure the device security mode for the voice-messaging ports.

Step 5

Perform
                                       			 security-related configuration tasks for Cisco Unity or Cisco Unity
                                          				Connection voice-messaging ports; for example, configure Cisco Unity to
                                       			 point to the Cisco TFTP server.

For more information, see Unified Communications Manager Integration Guide for Cisco Unity or for Cisco Unity Connection

Step 6

Reset the devices in Unified Communications Manager Administration and restart the Cisco Unity software.

For more information, see the Unified Communications Manager Integration Guide for Cisco Unity or for Cisco Unity Connection .

## Apply Security
                        	 Profile to Single Voice-Messaging Port

To apply a
                              		  security profile to a single voice-messaging port, perform the following
                              		  procedure.

This
                              		  procedure assumes that you added the device to the database and installed a
                              		  certificate in the phone, if a certificate does not already exist. After you
                              		  apply a security profile for the first time or if you change the security
                              		  profile, you must reset the device.

### Before you begin

Before you
                              		  apply a security profile, review topics related to voice-messaging security and
                              		  secure voice-messaging port setup.

Step 1

Find the voice-messaging port, as described in the Administration Guide for
                                             				  Cisco Unified Communications Manager .

Step 2

After the
                                       			 configuration window for the port displays, locate the Device
                                          				Security Mode setting. From the drop-down list box, choose the
                                       			 security mode that you want to apply to the port. The database predefines these
                                       			 options. The default value specifies Not
                                          				Selected .

Step 3

Click Save .

Step 4

Click Reset .

## Apply Security
                        	 Profile Using Voice Mail Port Wizard

Use this
                              		  procedure to apply the Device Security Mode setting in the Voice Mail Port
                              		  Wizard for a new voice-mail server.

To change
                              		  the security setting for an existing voice-mail server, see topics related to
                              		  applying the security profile to a single voice-messaging port.

### Before you begin

Before you
                              		  apply a security profile, review topics related to voice-messaging security and
                              		  secure voice-messaging port setup.

Step 1

Unified Communications Manager Administration , choose Voice Mail > Cisco Voice Mail Port Wizard .

Step 2

Enter the name
                                       			 of the voice-mail server; click Next .

Step 3

Choose the
                                       			 number of ports that you want to add; click Next .

Step 4

In the Cisco
                                          				Voice Mail Device Information window, choose a Device
                                          				Security Mode from the drop-down list box. The database predefines
                                       			 these options. The default value specifies Not
                                          				Selected .

Step 5

Configure the other device settings, as described in the Administration Guide for
                                             				  Cisco Unified Communications Manager . Click Next .

Step 6

Continue the configuration process, as described in the Administration Guide for
                                             				  Cisco Unified Communications Manager . When the Summary window displays, click Finish .

| Note | In this chapter, the use of the term "server" refers to a Unified Communications Manager server. The use of the phrase "voicemail server" refers to a Cisco Unity server or to a Cisco Unity Connection server. |
|---|---|

| Tip | If the device security mode settings do not match, the voicemail server ports fail to register with Unified Communications Manager , and the voicemail server cannot accept calls on those ports. |
|---|---|

| Step 1 | Verify that you installed and configured the CiscoCTL Client for Mixed Mode. |
|---|---|
| Step 2 | Verify that you
                                       			 configured the phones for authentication or encryption. |
| Step 3 | Use the certificate management feature in Cisco Unified Communications Operating System Administration to copy the Cisco Unity certificate to the trusted store on the Unified Communications Manager server; then restart the CiscoCallManager service. For more information, see the Administration Guide for Cisco Unified Communications Manager and Cisco Unified Serviceability Administration Guide . Tip Activate the Cisco CTL Provider service on each Unified Communications Manager server in the cluster; then restart the CiscoCallManager service on all servers. | Tip | Activate the Cisco CTL Provider service on each Unified Communications Manager server in the cluster; then restart the CiscoCallManager service on all servers. |
| Tip | Activate the Cisco CTL Provider service on each Unified Communications Manager server in the cluster; then restart the CiscoCallManager service on all servers. |
| Step 4 | In Unified Communications Manager Administration , configure the device security mode for the voice-messaging ports. |
| Step 5 | Perform
                                       			 security-related configuration tasks for Cisco Unity or Cisco Unity
                                          				Connection voice-messaging ports; for example, configure Cisco Unity to
                                       			 point to the Cisco TFTP server. For more information, see Unified Communications Manager Integration Guide for Cisco Unity or for Cisco Unity Connection |
| Step 6 | Reset the devices in Unified Communications Manager Administration and restart the Cisco Unity software. For more information, see the Unified Communications Manager Integration Guide for Cisco Unity or for Cisco Unity Connection . |

| Tip | Activate the Cisco CTL Provider service on each Unified Communications Manager server in the cluster; then restart the CiscoCallManager service on all servers. |
|---|---|

| Step 1 | Find the voice-messaging port, as described in the Administration Guide for
                                             				  Cisco Unified Communications Manager . |
|---|---|
| Step 2 | After the
                                       			 configuration window for the port displays, locate the Device
                                          				Security Mode setting. From the drop-down list box, choose the
                                       			 security mode that you want to apply to the port. The database predefines these
                                       			 options. The default value specifies Not
                                          				Selected . |
| Step 3 | Click Save . |
| Step 4 | Click Reset . |

| Step 1 | Unified Communications Manager Administration , choose Voice Mail > Cisco Voice Mail Port Wizard . |
|---|---|
| Step 2 | Enter the name
                                       			 of the voice-mail server; click Next . |
| Step 3 | Choose the
                                       			 number of ports that you want to add; click Next . |
| Step 4 | In the Cisco
                                          				Voice Mail Device Information window, choose a Device
                                          				Security Mode from the drop-down list box. The database predefines
                                       			 these options. The default value specifies Not
                                          				Selected . |
| Step 5 | Configure the other device settings, as described in the Administration Guide for
                                             				  Cisco Unified Communications Manager . Click Next . |
| Step 6 | Continue the configuration process, as described in the Administration Guide for
                                             				  Cisco Unified Communications Manager . When the Summary window displays, click Finish . |