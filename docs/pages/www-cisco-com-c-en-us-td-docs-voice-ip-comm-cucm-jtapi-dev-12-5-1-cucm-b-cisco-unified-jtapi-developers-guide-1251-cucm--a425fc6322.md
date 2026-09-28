---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-jtapi-dev-12-5-1-cucm-b-cisco-unified-jtapi-developers-guide-1251-cucm--a425fc6322
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/jtapi_dev/12_5_1/cucm_b_cisco-unified-jtapi-developers-guide-1251/cucm_b_cisco-unified-jtapi-developers-guide-1251_chapter_01.html
retrieved_at: 2026-08-16T18:11:47.188253+00:00
---

Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

# Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

Updated: June 11, 2025

Chapter: New and Changed Information

## Chapter: New and Changed Information

# New and Changed Information

This chapter
                        		describes new and changed JTAPI information for this release  of Cisco Unified Communications
                        		Manager and features supported in the previous releases.

For more
                        		information,  go to the Programming Guides website at http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_programming_reference_guides_list.html .

## Cisco Unified Communications Manager Release 12.5(1)

This section contains information about the new and changed features for Cisco Unified Communications Manager, Release 12.5(1):

Call Recording for SIP or TLS Authenticated Calls

Multi-fork Recording using CUBE Media Proxy Server

Linux and Windows installation procedure is updated in Installing the Cisco Unified JTAPI Software section.

## Cisco Unified
                        	 Communications Manager, Release 11.5(1)

This section
                           		contains information about the new and changed features for Cisco Unified
                           		Communications Manager, Release 11.5(1):

Starting from Release 11.5(1)SU9 and any subsequent SU or ES releases in this release train, the Cisco JTAPI Plugin follows installer less approach. You must
                           have JRE installed on the system before the installation. The installation runs in the command prompt and does not have a
                           GUI. Also, the same will not be listed in the software installed list of Windows Control Panel.

Cisco Spark Device has been added as a new device type for this release of Unified Communications Manager and may appear in the user's control list. However, Cisco Spark Device is not a supported device for this release of Cisco
                                       Unified JTAPI.

## Cisco Unified Communications Manager, Release 11.0(1)

This section contains information about the new and changed features for Cisco Unified Communications Manager, Release 11.0(1).

Default CTI IP Addressing for Devices

Ringback on SIP 183 for Transferred Calls

## Cisco Unified Communications Manager Release 10.5(2)

This section contains the new and changed features for Cisco Unified Communications Manager release 10.5(2):

AES 256 Algorithm IDs

## Cisco Unified
                        	 Communications Manager Release 10.0(1)

## Cisco Unified Communications Manager Release 9.0(1)

This section describes the new and changed features in Cisco Unified Communications Manager release 9.0(1):

## Cisco Unified Communications Manager Release 8.6(1)

This section describes the new and changed features in Cisco Unified Communications Manager release 8.6(1):

Account Lockout

EnergyWise Deep Sleep Mode

FIPS Compliance

Password Expiry

New JTAPI x64 client for 64-bit operating systems.

## Cisco Unified Communications Manager Release 8.5(1)

This section describes the new and changed features in Cisco Unified Communications Manager release 8.5(1):

## Cisco Unified Communications Manager Release 8.0(1)

## Cisco Unified Communications Manager Release 7.1(3)

This section describes the new and changed features in Cisco Unified Communications Manager release 7.1(3):

Terminal and Address Capability Settings .

## Cisco Unified Communications Manager Release 7.1(2)

## Cisco Unified
                        	 Communications Manager Release 7.0(1)

This
                           		section describes the new and changed features in Cisco Unified Communications
                           		Manager from release 6.1 to release 7.0(1) and Cisco Unified JTAPI
                           		enhancements. It has the following sections:

Cisco Unified
                                       		  Communications Manager release 7.0(1) does not support the following IPv6
                                       		  related methods:

canSupportIPv6()

setProviderOpenRetryAttempts (int retryAttempts)

getProviderOpenRetryAttempts()

getIPAddressingMode() ( available on CiscoMediaTerminal and CiscoRouteTerminal
                                          			 interfaces )

register(java.net.InetAddress address,  int port, 
                                       		  CiscoMediaCapability [] capabilities,  int[] algorithmIDs,  java.net.InetAddress
                                       		  address_v6,  int activeAddressingMode)

register(CiscoMediaCapability [] capabilities,  int[] int
                                       		  registration Type,  int[] algorithmIDs,  int activeAddressingMode)

getTerminals() ( available on new interface
                                          			 CiscoProviderTermCapabilityChangedEv )

getAddressingModeForMedia()

getCallingPartyIpAddr_v6() ( available on
                                          			 CiscoCallCtlConnOfferedEv and CiscoRouteEvent interfaces )

CTIERR_IPADDRMODEMISMATCH

CTIERR_DYNREG_IPADDRMODE_MISMATCH

hasIPv6CapabilityChanged()

CiscoTerminal.IP_ADDRESSING_MODE_IPv4

CiscoTerminal.IP_ADDRESSING_MODE_IPv6

CiscoTerminal.IP_ADDRESSING_MODE_IPv4_v6

CiscoTerminal.IP_ADDRESSING_MODE_Unknown

CiscoTermRegistrationFailedEv.IP_ADDRESSING_MODE_MISMATCH

For the features, 
                                       		  Join Across Lines,  Do Not Disturb-Reject,  and Calling Party Normalization,  each
                                       		  Cisco JTAPI must be upgraded to a version that supports these features.
                                       		  Additionally,  if you are upgrading from release 5.1 and you use Join Across
                                       		  Lines,  the Conference Chaining feature must not be enabled or used until all
                                       		  applications are either upgraded to a version compatible with the new unified
                                       		  CM version. Also,  you should verify that the applications are not impacted by
                                       		  the Conference Chaining feature.

## Cisco Unified Communications Manager Release 6.1

This section describes the new and changed features in Cisco Unified Communications Manager from release 6.0 to release 6.1
                           and Cisco Unified JTAPI enhancements. It has the following sections:

Certificate Download API Enhancement

Intercom Support for Extension Mobility

Join Across Lines

## Cisco Unified
                        	 Communications Manager Release 6.0

## Cisco Unified
                        	 Communications Manager Release 5.1

This
                           		section describes the new and changed features in Cisco Unified Communications
                           		Manager,  from release 5.0 to release 5.1 and Cisco Unified JTAPI enhancements.
                           		It has the following sections:

## Cisco Unified
                        	 Communications Manager Release 5.0

| Note | Cisco Spark Device has been added as a new device type for this release of Unified Communications Manager and may appear in the user's control list. However, Cisco Spark Device is not a supported device for this release of Cisco
                                       Unified JTAPI. |
|---|---|

| Note | Cisco Unified
                                       		  Communications Manager release 7.0(1) does not support the following IPv6
                                       		  related methods: canSupportIPv6() setProviderOpenRetryAttempts (int retryAttempts) getProviderOpenRetryAttempts() getIPAddressingMode() ( available on CiscoMediaTerminal and CiscoRouteTerminal
                                          			 interfaces ) register(java.net.InetAddress address,  int port, 
                                       		  CiscoMediaCapability [] capabilities,  int[] algorithmIDs,  java.net.InetAddress
                                       		  address_v6,  int activeAddressingMode) register(CiscoMediaCapability [] capabilities,  int[] int
                                       		  registration Type,  int[] algorithmIDs,  int activeAddressingMode) getTerminals() ( available on new interface
                                          			 CiscoProviderTermCapabilityChangedEv ) getAddressingModeForMedia() getCallingPartyIpAddr_v6() ( available on
                                          			 CiscoCallCtlConnOfferedEv and CiscoRouteEvent interfaces ) CTIERR_IPADDRMODEMISMATCH CTIERR_DYNREG_IPADDRMODE_MISMATCH hasIPv6CapabilityChanged() CiscoTerminal.IP_ADDRESSING_MODE_IPv4 CiscoTerminal.IP_ADDRESSING_MODE_IPv6 CiscoTerminal.IP_ADDRESSING_MODE_IPv4_v6 CiscoTerminal.IP_ADDRESSING_MODE_Unknown CiscoTermRegistrationFailedEv.IP_ADDRESSING_MODE_MISMATCH |
|---|---|

| Note | For the features, 
                                       		  Join Across Lines,  Do Not Disturb-Reject,  and Calling Party Normalization,  each
                                       		  Cisco JTAPI must be upgraded to a version that supports these features.
                                       		  Additionally,  if you are upgrading from release 5.1 and you use Join Across
                                       		  Lines,  the Conference Chaining feature must not be enabled or used until all
                                       		  applications are either upgraded to a version compatible with the new unified
                                       		  CM version. Also,  you should verify that the applications are not impacted by
                                       		  the Conference Chaining feature. |
|---|---|