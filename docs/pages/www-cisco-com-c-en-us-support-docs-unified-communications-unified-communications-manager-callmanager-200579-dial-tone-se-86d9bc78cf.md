---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200579-dial-tone-se-86d9bc78cf
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200579-Dial-Tone-Settings-For-Cisco-SIP-IP-Phon.html
retrieved_at: 2026-08-21T13:55:04.801450+00:00
---

Dial Tone Settings For Cisco SIP IP Phones

# Dial Tone Settings For Cisco SIP IP Phones

### Download Options

Updated: July 25, 2016

Document ID: 200579

Contents

## Contents

## Introduction

This document describes the Dial Tone Settings behaviour for Cisco Session Initiation Protocol (SIP) IP Phones registered on Cisco Unified Communications Manager (CUCM).

Contributed Ebrahim Riyaz Abdul Nazir and Divjot Nanda, Cisco TAC Engineers.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM version 11.5  and above

- SIP phone frimware 11.5 and above.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco CUCM 11.5

- Cisco 8841 SIP IP phone with firmare 11.5

Note : SIP phones for which 11.5 firmware is not present will not have the code changes made for this feature.

The information in this document was created with devices in a specific lab environment. All devices used in this document had a default configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

SIP Phones play dial tones based on its dial plan, which does not take the existing CUCM dial tone service parameter - Always Use Dial Tone Setting . But in case of Skinny Call Control Protocol (SCCP), phones always plays dial tones based on this service parameter.

This feature adds the functionality to SIP Phones, enabling the SIP endpoints to play dial tone based on the Service Parameter setting.

This feature is supported on SIP Phones having firmware version 11.5 and above. This feature added <dialToneSetting> tag in the TFTP configuration file for the SIP phone. This tag when presented to the phone is used to play CUCM configured dial tone to the phone user.

Feature Overview

1. Always Use Dial Tone Setting service parameter is used to instruct the Endpoints to play either Inside/Outside or Default dial tone.

2.Interpretation of dial tones

I. Default : Outside dial tone can differ from inside dial tone.

II. Inside : Always play inside dial tone, even for calls that are destined for OffNet (no distinction between inside and outside dial tone).

III. Outside : Always play outside dial tone, even for calls that are destined for OnNet (no distinction between inside and outside dial tone).

3. Expected SIP phone behaviour with and without SIP dial rules is shown as:

Phone with SIP dial rules

Phone without SIP dial rules

4. In order to change the service parameter navigate to Always Use Dial Tone Setting > System > Service Parameters > Service > CallManager , this allows CUCM to rebuild the SIP Phones TFTP Configuration files. User resets the SIP Phones for the changes to take effect (which are instructed by a popup on changing this Service parameter value).

Note : 1. SIP phones need to be reset, for the change to take effect. 2. SCCP phones, take the changes and no reset is required.

4. After reset, TFTP file for the SIP phone has < dialToneSetting > tag with value set to 1-3.

<dialToneSetting>1</dialToneSetting>, or <dialToneSetting>2</dialToneSetting>, or <dialToneSetting>3</dialToneSetting> Interpretation

1 : Default, 2 : Always Play Inside Dial Tone, 3 : Always Play Outside Dial Tone

## Configure

Navigate to System > Service Parameter  > Service  > CallManager > Always Use dial tone Setting and select the type of dial-tone setting preffered.

You get an alert message upon the change of the dial-tone setting, which mentions the need to RESET the SIP phones for the configuration to take effect.

## Verify and Troubleshoot

1. In order to verify or troubleshoot any dial tone issues in SIP phones, check for the <dialtonesetting> tag value in SIP Phones TFTP configuration file.

2. If < dialtonesetting > tag is not present in TFTP configuration file with CUCM Version 11.5 and above, check and upgrade SIP Phones firmware version to 11.5 or above.

For example:

A.  Configuration file for 8841 SIP phone registered with CUCM 10.5 does not contain the dial tone setting parameter:

```
<secureServicesURL>https://10.106.110.12:8443/ccmcip/getservicesmenu.jsp</secureServicesURL>
<dscpForSCCPPhoneConfig>96</dscpForSCCPPhoneConfig>
<dscpForSCCPPhoneServices>0</dscpForSCCPPhoneServices>
<dscpForCm2Dvce>96</dscpForCm2Dvce>
<transportLayerProtocol>3</transportLayerProtocol>
<dndCallAlert>5</dndCallAlert>
<phonePersonalization>0</phonePersonalization>
<rollover>0</rollover>
<singleButtonBarge>0</singleButtonBarge>
<joinAcrossLines>0</joinAcrossLines>
```

B. Configuration file for 8841 SIP phone with CUCM 11.5 contains the information about the dial-tone settings with the value (1,2 or 3).

```
<secureServicesURL>https://RZCUCM11:8443/ccmcip/getservicesmenu.jsp</secureServicesURL>
<dscpForSCCPPhoneConfig>96</dscpForSCCPPhoneConfig>
<dscpForSCCPPhoneServices>0</dscpForSCCPPhoneServices>
<dscpForCm2Dvce>96</dscpForCm2Dvce>
<transportLayerProtocol>4</transportLayerProtocol> <dialToneSetting>1</dialToneSetting> <dndCallAlert>5</dndCallAlert>
<phonePersonalization>0</phonePersonalization>
<rollover>0</rollover>
<singleButtonBarge>0</singleButtonBarge>
<joinAcrossLines>0</joinAcrossLines>
```

### Contributed by Cisco Engineers

Ebrahim Riyaz Abdul Nazir

Cisco TAC Engineer

Divjot Nanda

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Service Parameter Configuration | OffHook DialTone | Outside Routable |
|---|---|---|
| Default | Inside | Outside |
| Inside | Inside | Inside |
| Outside | Outside | Outside |

| Service Parameter Configuration | OffHook DialTone | Outside Routable |
|---|---|---|
| Default | Inside | Outside |
| Inside | Inside | (none) |
| Outside | Outside | Outside |