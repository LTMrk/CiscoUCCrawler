---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-10-0-english-admin-guide-ip05-bk-a6e3f5ab-00-adminguide-3905-10--bbb69ce17c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/10_0/english/admin_guide/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0_chapter_0111.html
retrieved_at: 2026-08-21T14:35:16.727234+00:00
---

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

# Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

Updated: May 9, 2025

Chapter: Cisco Unified SIP Phone Security

## Chapter: Cisco Unified SIP Phone Security

# Cisco Unified SIP Phone Security

## Cisco Unified SIP Phone Security Features

Topic

Reference

Detailed explanation of security, including set up,
                                             					 configuration, and troubleshooting information for Cisco Unified
                                                				Communications Manager and Cisco UnifiedIP Phones

See the Troubleshooting Guide for Cisco Unified
                                                   				Communications Manager .

Security and the phone startup process

See Verify Phone Startup .

Security and phone configuration files

See Phone Addition Methods .

Disabling access to a phone web pages

See Control Phone Web Page Access .

Troubleshooting

- See Troubleshooting

- See the Troubleshooting Guide for Cisco Unified
                                                      				Communications Manager

Resetting or restoring the phone

See Basic Reset .

802.1X Authentication for Cisco Unified IP Phones

See these sections:

802.1X Authentication

Troubleshooting

### 802.1X
                           	 Authentication

The Cisco IP
                                 		  Phones support 802.1X Authentication.

Cisco IP
                                 		  Phones and Cisco Catalyst switches traditionally use Cisco Discovery Protocol
                                 		  (CDP) to identify each other and determine parameters such as VLAN allocation
                                 		  and inline power requirements. CDP does not identify locally attached
                                 		  workstations. Cisco IP Phones provide an EAPOL pass-through mechanism. This
                                 		  mechanism allows a workstation attached to the Cisco IP Phone to pass EAPOL
                                 		  messages to the 802.1X authenticator at the LAN switch. The pass-through
                                 		  mechanism ensures that the IP phone does not act as the LAN switch to
                                 		  authenticate a data endpoint before accessing the network.

Cisco IP
                                 		  Phones also provide a proxy EAPOL Logoff mechanism. In the event that the
                                 		  locally attached PC disconnects from the IP phone, the LAN switch does not see
                                 		  the physical link fail, because the link between the LAN switch and the IP
                                 		  phone is maintained. To avoid compromising network integrity, the IP phone
                                 		  sends an EAPOL-Logoff message to the switch on behalf of the downstream PC,
                                 		  which triggers the LAN switch to clear the authentication entry for the
                                 		  downstream PC.

Support
                                 		  for 802.1X authentication requires several components:

Cisco IP
                                       				Phone: The phone initiates the request to access the network. Cisco IP Phones
                                       				contain an 802.1X supplicant. This supplicant allows network administrators to
                                       				control the connectivity of IP phones to the LAN switch ports. The current
                                       				release of the phone 802.1X supplicant uses the EAP-FAST and EAP-TLS options
                                       				for network authentication.

Cisco Secure
                                       				Access Control Server (ACS) (or other third-party authentication server): The
                                       				authentication server and the phone must both be configured with a shared
                                       				secret that authenticates the phone.

Cisco Catalyst
                                       				Switch (or other third-party switch): The switch must support 802.1X, so it can
                                       				act as the authenticator and pass the messages between the phone and the
                                       				authentication server. After the exchange completes, the switch grants or
                                       				denies the phone access to the network.

You must perform
                                 		  the following actions to configure 802.1X.

Configure the
                                       				other components before you enable 802.1X Authentication on the phone.

Configure PC
                                       				Port: The 802.1X standard does not consider VLANs and thus recommends that only
                                       				a single device should be authenticated to a specific switch port. However,
                                       				some switches (including Cisco Catalyst switches) support multidomain
                                       				authentication. The switch configuration determines whether you can connect a
                                       				PC to the PC port of the phone.

Enabled:
                                             					 If you are using a switch that supports multidomain authentication, you can
                                             					 enable the PC port and connect a PC to it. In this case, Cisco IP Phones
                                             					 support proxy EAPOL-Logoff to monitor the authentication exchanges between the
                                             					 switch and the attached PC. For more information about IEEE 802.1X support on
                                             					 the Cisco Catalyst switches, see the Cisco Catalyst switch configuration guides
                                             					 at:

http://www.cisco.com/en/US/products/hw/switches/ps708/tsd_products_support_series_home.html

Disabled:
                                             					 If the switch does not support multiple 802.1X-compliant devices on the same
                                             					 port, you should disable the PC Port when 802.1X authentication is enabled. If
                                             					 you do not disable this port and subsequently attempt to attach a PC to it, the
                                             					 switch denies network access to both the phone and the PC.

- Enabled: If you are using a
                                          				  switch that supports multidomain authentication, you can continue to use the
                                          				  voice VLAN.

- Disabled: If the switch
                                          				  does not support multidomain authentication, disable the Voice VLAN and
                                          				  consider assigning the port to the native VLAN.

## Set Device Authentication Field

Step 1

Press Applications .

Step 2

Choose Admin
                                             				  Settings > Security > 802.1X
                                             				  Authentication > Device
                                             				  Authentication .

Step 3

Press Select .

Step 4

Set the Device Authentication option to Enabled or Disabled.

Step 5

Press Select to confirm.

## Set Shared Secret Field

Choose a password to use on the phone and on
                              					 the authentication server. The password must be between 6 and 32 characters,
                              					 consisting of any combination of numbers or letters.

If you disable 802.1X authentication or perform a factory
                                          						reset of the phone, the shared secret is deleted.

Step 1

Press Applications .

Step 2

Choose Admin
                                             				  Settings > Security > 802.1X
                                             				  Authentication > EAP-MD5 > Shared
                                             				  Secret .

Step 3

Press Select .

Step 4

Enter the shared secret.

Step 5

Press Select to confirm.

| Topic | Reference |
|---|---|
| Detailed explanation of security, including set up,
                                             					 configuration, and troubleshooting information for Cisco Unified
                                                				Communications Manager and Cisco UnifiedIP Phones | See the Troubleshooting Guide for Cisco Unified
                                                   				Communications Manager . |
| Security and the phone startup process | See Verify Phone Startup . |
| Security and phone configuration files | See Phone Addition Methods . |
| Disabling access to a phone web pages | See Control Phone Web Page Access . |
| Troubleshooting | See Troubleshooting See the Troubleshooting Guide for Cisco Unified
                                                      				Communications Manager |
| Resetting or restoring the phone | See Basic Reset . |
| 802.1X Authentication for Cisco Unified IP Phones | See these sections: 802.1X Authentication Troubleshooting |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Choose Admin
                                             				  Settings > Security > 802.1X
                                             				  Authentication > Device
                                             				  Authentication . |
| Step 3 | Press Select . |
| Step 4 | Set the Device Authentication option to Enabled or Disabled. |
| Step 5 | Press Select to confirm. |

| Note | If you disable 802.1X authentication or perform a factory
                                          						reset of the phone, the shared secret is deleted. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Choose Admin
                                             				  Settings > Security > 802.1X
                                             				  Authentication > EAP-MD5 > Shared
                                             				  Secret . |
| Step 3 | Press Select . |
| Step 4 | Enter the shared secret. |
| Step 5 | Press Select to confirm. |