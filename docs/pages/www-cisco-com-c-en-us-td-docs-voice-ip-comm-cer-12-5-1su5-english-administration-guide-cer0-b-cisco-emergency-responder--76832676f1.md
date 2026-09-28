---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su5-english-administration-guide-cer0-b-cisco-emergency-responder--76832676f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su5/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251su5/cer0_b_cisco-emergency-responder-administration-guide-1251su3_chapter_01100.html
retrieved_at: 2026-08-21T15:37:33.642502+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU5

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU5

Updated: August 23, 2023

Chapter: Cisco Emergency Responder User Preparation

## Chapter: Cisco Emergency Responder User Preparation

# Cisco Emergency Responder User Preparation

## Cisco Emergency
                        	 Responder User Preparation Overview

This chapter
                           		describes the various roles for CiscoEmergencyResponder (Emergency Responder)
                           		users. The topics describe not only the use of the software, but help you
                           		understand the larger policy and procedure decisions your organization must
                           		make to determine how Emergency Responder fits into your organization's
                           		emergency response needs.

## Emergency
                        	 Responder Onsite Alert Personnel Preparations

You probably
                           		already have emergency response policies and procedures in place. Consider how
                           		CiscoEmergency Responder (Emergency Responder) fits into these policies and
                           		procedures, and work with your emergency response teams (onsite alert or
                           		security personnel) to update these procedures if necessary.

Consider
                           		training these personnel on these aspects of Emergency Responder:

How to use the
                                 			 Emergency Responder web interface. See the Emergency Responder user web
                                 			 interface online help for information about these topics. The online help
                                 			 includes a user's guide in PDF format that you can print out and distribute to
                                 			 your users. The information in the user's guide is the same as the information
                                 			 in the online help. Train users on these areas:

How to log
                                       				  into the user web interface.

How alerts
                                       				  show up on the screen and how to view specific (if set by the administrator) or
                                       				  all alerts in the system.

How to
                                       				  obtain more information about the location of the call. Summary information
                                       				  includes the actual extension of the caller; the ELIN, which is the phone
                                       				  number the PSAP gets as the number of the emergency caller; the phone location
                                       				  associated with the switch port; and the location field of the ALI. Users can
                                       				  also view the entire ALI.

How to
                                       				  acknowledge the call and add comments to it. Consider developing rules for
                                       				  these procedures to ensure consistent behavior from your emergency response
                                       				  teams.

How to look
                                       				  up emergency calls in the emergency call history.

A web alert
                                          				  appears for everyone logged into the Emergency Responder user web interface.

All
                                          				  personnel assigned to an ERL receive a telephone call when an emergency call is
                                          				  made from the ERL. The telephone call includes information about the extension
                                          				  of the caller.

If you
                                          				  configure email addresses for the personnel, they also receive an email, which
                                          				  includes more information than the phone call, including ERL name and phone
                                          				  location. If the email address is for an email-based pager, they are paged.
                                          				  Paging is the most efficient way of getting information to users who are not at
                                          				  their desks.

If the
                                          				  standby CiscoEmergency Responder server handles an emergency call, all onsite
                                          				  alert personnel get notified of the call, and of the fact that the standby
                                          				  server handled the call. Decide how you want people to respond to these
                                          				  notifications.

Explain the ERL
                                 			 naming and phone location you are using. This is the primary information the
                                 			 personnel have for identifying the location of the emergency caller.

Explain the
                                 			 organization's policy for responding to emergency calls. Work with the
                                 			 emergency response teams to develop an acceptable policy if you do not already
                                 			 have one.

## Emergency Responder
                        	 ERL Administrator Role

The
                              		  following table lists the recurring tasks for which an ERL administrator is
                              		  responsible. A system administrator can also perform these tasks.

Recurring Task

Description

More Information

Assign ERLs to new or changed switch ports

If
                                          					 switches are added to the network, or if modules with additional ports are
                                          					 added to existing switches, assign the new ports ERLs.

Switch Port Configuration

Create ERLs as required

As
                                          					 your business expands, create new ERLs as required. Work with the telephony
                                          					 administrators to obtain ELINs for the ERLs, and with the network administrator
                                          					 to get the new switches defined in Emergency Responder.

- ERL Creation

- Switch Port Configuration

Export ALI data and submit to your service provider

If
                                          					 you make changes to ALI data, add or remove ERLs, or change the ELINs assigned
                                          					 to an ERL (for example, by adding or removing them), export the ALI and
                                          					 resubmit it to your service provider.

Audit the manually defined phones

Regularly check your manual phone definitions to ensure each
                                          					 phone is still assigned to the correct ERL. Work with the telephony
                                          					 administrator to get notification of any adds, moves, or changes that involve
                                          					 these phones. Add phones as required.

- Manually Define Phones

Audit the unlocated phones list

Regularly audit the unlocated phones list, and work with the
                                          					 network administrator to determine why CiscoEmergency Responder cannot locate
                                          					 the phones and to resolve the problems.

- Identify Unlocated Phones

- Unlocated Phones

Add
                                          					 new onsite personnel or remove old ones; update phone numbers

As
                                          					 onsite alert personnel are added, define them in CiscoEmergency Responder and
                                          					 assign them to the appropriate ERLs. Likewise, as personnel are removed, remove
                                          					 them from their ERLs and then from CiscoEmergency Responder. Update phone
                                          					 numbers, email address, and other contact information as they change.

- Add Onsite Security Personnel

- ERL Creation

Add
                                          					 IP subnet for the IP subnets to be tracked

If
                                          					 there is a new IP subnet that needs to be discovered by Emergency Responder,
                                          					 then perform the following tasks:

- Configure an ERL spanning the
                                             						new IP subnet's geographical location.

- Configure this new IP subnet
                                             						and the appropriate mask and assign this IP subnet to the created ERL.

- Set Up IP Subnet-based ERLs

## Emergency Responder
                        	 Network Administrator Role

The
                              		  following table lists the recurring tasks for which a network administrator is
                              		  responsible. A system administrator can also perform these tasks.

Recurring Task

Description

More Information

Add
                                          					 new switches

Add
                                          					 any switches that you add to the network to the CiscoEmergency Responder
                                          					 configuration. A switch is considered new if it has an IP address not defined
                                          					 in CiscoEmergency Responder.

- LAN Switch Identification

- Manually Run the Switch-Port and Phone Update Process

Remove old switches

Remove switches from the CiscoEmergency Responder configuration
                                          					 if you remove them from the network. Nonexistent switches in the
                                          					 CiscoEmergency Responder configuration do not create problems, but they do
                                          					 increase the time required to do phone tracking, because CiscoEmergency
                                          					 Responder attempts to connect to the switch must time out before moving on to
                                          					 the next switch.

- LAN Switch Identification

Update the SNMP read community if it changes

If
                                          					 you change the read community string on any defined switch, you must update the
                                          					 SNMP settings in CiscoEmergency Responder. Until the setting is updated,
                                          					 CiscoEmergency Responder cannot track phones attached to the switch.

- Set Up SNMPv2

Update or remove Unified CM servers

If
                                          					 a Unified CM cluster is added to the network, or one is removed, update the
                                          					 configuration for the CiscoEmergency Responder group that supports the
                                          					 cluster. Although you have the authority to make these updates, your
                                          					 organization might assign the primary responsibility to the CiscoEmergency
                                          					 Responder system administrator.

- Identify Cisco Unified Communications Manager Clusters

Check ERL assignments

Use
                                          					 the ERL Debug Tool to check that the correct and expected ERL is used for a
                                          					 selected phone.

- Emergency Responder Admin Utility

## Emergency Responder
                        	 System Administrator Role

The
                              		  following table lists the recurring tasks for which a system administrator is
                              		  responsible. A system administrator might also be responsible for some or all
                              		  of the ERL and network administrators' tasks, as explained in the Emergency Responder ERL Administrator Role and the Emergency Responder Network Administrator Role .

Recurring Task

Description

More Information

Add additional CiscoEmergency Responder groups

As
                                          					 telephones are added to the network, you might need additional CiscoEmergency
                                          					 Responder groups. Install and define them and their telephony settings.

Work with the telephony administrator to complete the required
                                          					 Unified CM configuration.

Monitor the system and troubleshoot any problems

Help resolve any problems that arise. Work with the network and
                                          					 ERL administrators, and the telephony administrator, as appropriate.

Create new CiscoEmergency Responder users; remove old users

As
                                          					 onsite alert personnel change, or as CiscoEmergency Responder system, network,
                                          					 and ERL administrators change, add or remove them as required.

- Emergency Responder User Management

Add or remove Unified CM servers

If
                                          					 a Unified CM cluster is added to the network, or one is removed, update the
                                          					 configuration for the CiscoEmergency Responder group that supports the
                                          					 cluster. Although you have the authority to make these updates, your
                                          					 organization might assign the primary responsibility to the CiscoEmergency
                                          					 Responder network administrator.

- Identify Cisco Unified Communications Manager Clusters

Monitor the email alerts that CiscoEmergency Responder
                                          					 generates

If
                                          					 your email ID is configured in the server group settings, CiscoEmergency
                                          					 Responder sends email alerts about critical errors to you. You are expected to
                                          					 understand the error and take action to correct the problem.

See Troubleshoot Email Alerts for information to help you understand the email alerts and resolve problems.

- Set Up a Server Group

| Recurring Task | Description | More Information |
|---|---|---|
| Assign ERLs to new or changed switch ports | If
                                          					 switches are added to the network, or if modules with additional ports are
                                          					 added to existing switches, assign the new ports ERLs. | Switch Port Configuration |
| Create ERLs as required | As
                                          					 your business expands, create new ERLs as required. Work with the telephony
                                          					 administrators to obtain ELINs for the ERLs, and with the network administrator
                                          					 to get the new switches defined in Emergency Responder. | ERL Creation Switch Port Configuration |
| Export ALI data and submit to your service provider | If
                                          					 you make changes to ALI data, add or remove ERLs, or change the ELINs assigned
                                          					 to an ERL (for example, by adding or removing them), export the ALI and
                                          					 resubmit it to your service provider. |  |
| Audit the manually defined phones | Regularly check your manual phone definitions to ensure each
                                          					 phone is still assigned to the correct ERL. Work with the telephony
                                          					 administrator to get notification of any adds, moves, or changes that involve
                                          					 these phones. Add phones as required. | Manually Define Phones |
| Audit the unlocated phones list | Regularly audit the unlocated phones list, and work with the
                                          					 network administrator to determine why CiscoEmergency Responder cannot locate
                                          					 the phones and to resolve the problems. | Identify Unlocated Phones Unlocated Phones |
| Add
                                          					 new onsite personnel or remove old ones; update phone numbers | As
                                          					 onsite alert personnel are added, define them in CiscoEmergency Responder and
                                          					 assign them to the appropriate ERLs. Likewise, as personnel are removed, remove
                                          					 them from their ERLs and then from CiscoEmergency Responder. Update phone
                                          					 numbers, email address, and other contact information as they change. | Add Onsite Security Personnel ERL Creation |
| Add
                                          					 IP subnet for the IP subnets to be tracked | If
                                          					 there is a new IP subnet that needs to be discovered by Emergency Responder,
                                          					 then perform the following tasks: Configure an ERL spanning the
                                             						new IP subnet's geographical location. Configure this new IP subnet
                                             						and the appropriate mask and assign this IP subnet to the created ERL. | Set Up IP Subnet-based ERLs |

| Recurring Task | Description | More Information |
|---|---|---|
| Add
                                          					 new switches | Add
                                          					 any switches that you add to the network to the CiscoEmergency Responder
                                          					 configuration. A switch is considered new if it has an IP address not defined
                                          					 in CiscoEmergency Responder. | LAN Switch Identification Manually Run the Switch-Port and Phone Update Process |
| Remove old switches | Remove switches from the CiscoEmergency Responder configuration
                                          					 if you remove them from the network. Nonexistent switches in the
                                          					 CiscoEmergency Responder configuration do not create problems, but they do
                                          					 increase the time required to do phone tracking, because CiscoEmergency
                                          					 Responder attempts to connect to the switch must time out before moving on to
                                          					 the next switch. | LAN Switch Identification |
| Update the SNMP read community if it changes | If
                                          					 you change the read community string on any defined switch, you must update the
                                          					 SNMP settings in CiscoEmergency Responder. Until the setting is updated,
                                          					 CiscoEmergency Responder cannot track phones attached to the switch. | Set Up SNMPv2 |
| Update or remove Unified CM servers | If
                                          					 a Unified CM cluster is added to the network, or one is removed, update the
                                          					 configuration for the CiscoEmergency Responder group that supports the
                                          					 cluster. Although you have the authority to make these updates, your
                                          					 organization might assign the primary responsibility to the CiscoEmergency
                                          					 Responder system administrator. | Identify Cisco Unified Communications Manager Clusters |
| Check ERL assignments | Use
                                          					 the ERL Debug Tool to check that the correct and expected ERL is used for a
                                          					 selected phone. | Emergency Responder Admin Utility |

| Recurring Task | Description | More Information |
|---|---|---|
| Add additional CiscoEmergency Responder groups | As
                                          					 telephones are added to the network, you might need additional CiscoEmergency
                                          					 Responder groups. Install and define them and their telephony settings. Work with the telephony administrator to complete the required
                                          					 Unified CM configuration. |  |
| Monitor the system and troubleshoot any problems | Help resolve any problems that arise. Work with the network and
                                          					 ERL administrators, and the telephony administrator, as appropriate. |  |
| Create new CiscoEmergency Responder users; remove old users | As
                                          					 onsite alert personnel change, or as CiscoEmergency Responder system, network,
                                          					 and ERL administrators change, add or remove them as required. | Emergency Responder User Management |
| Add or remove Unified CM servers | If
                                          					 a Unified CM cluster is added to the network, or one is removed, update the
                                          					 configuration for the CiscoEmergency Responder group that supports the
                                          					 cluster. Although you have the authority to make these updates, your
                                          					 organization might assign the primary responsibility to the CiscoEmergency
                                          					 Responder network administrator. | Identify Cisco Unified Communications Manager Clusters |
| Monitor the email alerts that CiscoEmergency Responder
                                          					 generates | If
                                          					 your email ID is configured in the server group settings, CiscoEmergency
                                          					 Responder sends email alerts about critical errors to you. You are expected to
                                          					 understand the error and take action to correct the problem. See Troubleshoot Email Alerts for information to help you understand the email alerts and resolve problems. | Set Up a Server Group |