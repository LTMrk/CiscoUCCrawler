---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-express-211257-cucme-configurat-aeaf2c922a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-express/211257-CUCME-Configuration-Best-Practices.html
retrieved_at: 2026-08-21T09:48:05.282428+00:00
---

CUCME Configuration Best Practices

# CUCME Configuration Best Practices

### Download Options

Updated: May 22, 2017

Document ID: 211257

Contents

## Contents

## Introduction

This document describes the best practice rules for Cisco Unified Communication  Manager Express (CUCME).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communication Manager Express (CUCME)

### Components Used

The information in this document is based on these software versions:

- CUCME 7.X and later

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Best Practices for Specific Scenarios

### Transfer Pattern Configuration Check

#### Symptom:

Unable to transfer calls to external numbers from IP phones registered to CUCME.

#### Configuration Check:

Check for the presence of transfer-pattern command under the telephony-service command mode.

```
telephony-service transfer-pattern [\.0-9T]+
```

#### Recommended Action:

Review documentation:

http://www.cisco.com/en/US/partner/docs/voice_ip_comm/cucme/admin/configuration/guide/cmetrans.html#wp1167239

http://www.cisco.com/en/US/partner/docs/voice_ip_comm/cucme/command/reference/cme_t1ht.html#wp1018955

Modify Configuration:

Add or modify the transfer-pattern command so that calls can be transferred.

Example 1: Allows transfer to any number.

```
telephony-service transfer-pattern .T
```

Example 2:  Allows transfers only to local numbers, where local numbers are 10 digits with the 919 area code.

```
telephony-service transfer-pattern 919.......
```

### Multicast Paging

#### Symptom:

Some members of the paging group may not receive the paging call if the total number of members in an unicast paging group is greater than 10.

#### Configuration Check:

Check to see if the paging-dn command is configured under any of the ephone's defined.

```
ephone [0-9]+ 
   mac-address[0-9ABCDEF\.]*
   type.*
   button.* paging-dn [0-9]*
```

For any paging-dn found in the above step, look for the paging ip[.\.]+ command.  This denotes whether it's defined for multicast or unicast paging. If not found, it's unicast.

#### Recommended Action:

If the paging dn is not defined for multicast, then the group can only contain 10 members. For groups with more than 10, re-configure the paging dn for multicast by adding the paging ip command.

Example #1

```
ephone-dn 1 number 3001 paging ip 239.1.1.1 port 2000
```

Review documentation for additional information:

http://www.cisco.com/en/US/partner/docs/voice_ip_comm/cucme/admin/configuration/guide/cmepage.html

http://www.cisco.com/en/US/partner/docs/voice_ip_comm/cucme/command/reference/cme_p1ht.html#wp1047557

### CUCME Multicast Music on Hold  (MoH)

#### Symptom:

Internal calls (i.e. calls between IP phones registered to the same CUCME) when kept on hold do not receive MOH instead they hear a periodic tone.

#### Configuration Check:

Check for the multicast moh command under telephony-service.

```
telephony-service multicast moh [.\.]+
```

#### Recommended Action:

Multicast MoH must be enabled in order for internal to internal IP phone calls to receive MoH. If not configured, enable it using the multicast moh command. Also make sure CUCME  is running on the router.

Refer to documentation for additional information:

http://www.cisco.com/en/US/partner/docs/voice_ip_comm/cucme/admin/configuration/guide/cmemoh.html

### CUCME Hardware Conferencing

#### Symptom:

IP Phone registered to CUCME cannot create a conference call with more than 3 parties.

#### Configuration Check:

Check to see if the conference hardware command is configured under telephony-service .

```
telephony-service conference hardware
```

Verify dsp service dspfarm is configured under the voice-card sub-command mode.

```
voice-card $tag1 dsp service dspfarm
```

Verify that the dspfarm conference profile is in a no shutdown state and associate application SCCP is configured.

```
dspfarm profile $tag2 conference associate application SCCP no shutdown
```

Ensure the $tag for the dspfarm profile is associated with the sccp ccm group defined for the CME.

```
sccp ccm group $tag3 associate profile $tag2 register $name
```

Ensure that the correct sccp ccm group $tag3 is defined under telephony-service .

```
telephony-service sdspfarm tag $tag4 $name
```

Ensure there are ephone-dn's configured with the conference ad-hoc or conference meetme options and that they have valid a number .

```
ephone-dn $tag number [0-9ABCDEF]* conference ad-hoc
```

```
ephone-dn $tag number [0-9ABCDEF]* conference meetme
```

#### Recommended Action:

Verify configuration is correct. Ensure that the conference resource is up and in a registered state. Issue the show sccp command to determine the status.

Refer to the documentation for additional information:

http://www.cisco.com/en/US/docs/voice_ip_comm/cucme/admin/configuration/guide/cmeconf.html

### Olson Timezone File Check

#### Symptom:

The Olson Timezone feature allows for the user to update the timezones available to IP phones by uploading new tzupdater.jar and TzDataCSV.csv files. The files need to be accessible via TFTP for the phones to download and use. This allows for timezone changes to be incorporated into CUCME much faster as it only requires the files to be updated and not a new CUCME release.

#### Configuration Check:

Determine if the Olsen Timezone feature is being used in either CUCME Session Initiation Protocol (SIP) or Skinny Client Control Protocol (SCCP). Look for the olsontimezone command.

```
telephony-service olsontimezone $timezone version $version
```

```
voice register global olsontimezone $timezone version $version
```

Check for the tftp-server commands for the two files used by the feature.

```
tftp-server flash:tzupdater.jar tftp-server flash:TzDataCSV.csv
```

#### Recommended Action:

If the olsontimezone command is not configured then the files are not needed. If the feature is in use or needs to be configured, due to recent changes to the timezone or DST changes,  then configure the feature and ensure the files are available for the phones to download.

Refer to the documentation for additional information:

http://www.cisco.com/en/US/docs/voice_ip_comm/cucme/admin/configuration/guide/cmenetwk.html#wpmkr1070767

### End User License Agreement (EULA) Check

#### Symptom:

If CUCME  or CUCME-as-SRST (Survivable Remote Site Telephony) is configured on an Integrated Services Routers Generation 2 (ISR-G2) router but the EULA (End-User License Agreement) has not been accepted, the router will not allow any IP phones to register.

#### Configuration Check:

Check the status of EULA for the cme-srst license. Look at the output of show license detail cme-srst and check for "EULA not accepted" under the License State: section

```
Router#sh license detail cme-srst Feature: cme-srst                        Period left: 8  weeks 4  days Index: 1 	Feature: cme-srst                          Version: 1.0 License Type: EvalRightToUse License State: Not in Use, EULA not accepted Evaluation total period: 8  weeks 4  days Evaluation period left: 8  weeks 4  days Period used: 0  minute  0  second License Count: 0/0  (In-use/Violation) License Priority: None Store Index: 7 Store Name: Built-In License Storage
```

#### Recommended Action:

Issue the license accept end user agreement command to accept the EULA.

Refer to the documentation for additional information:

http://www.cisco.com/en/US/docs/routers/access/sw_activation/SA_on_ISR.html#wp1155517

### SIP Trunk - Forward and Transfer

#### Symptom:

When an inbound call from a SIP Trunk provider to CUCME is forwarded or transferred to another destination across SIP Trunk, call forward / transfer may not be successful.

#### Configuration Check:

Determine whether REFER and Call Forward Supplementary services are disabled under voice service voip :

```
voice service voip no supplementary-service sip moved-temporarily no supplementary-service sip refer
```

#### Recommended Action:

Most service providers don't support either SIP REFER or 302 Moved Temporarily to transfer or forward calls. It's best to have the CUCME perform the supplementary service. Ensure both are disabled.

```
voice service voip no supplementary-service sip moved-temporarily no supplementary-service sip refer
```

Refer to the documentation for additional information:

http://www.cisco.com/en/US/products/sw/voicesw/ps4625/products_configuration_example09186a00808f9666.shtml

### GUI Access

#### Symptom:

Users are unable to access the CUCME GUI or the pages don't fully load.

#### Configuration Check:

Ensure GUI access for System/Customer Administrators is enabled under telephony-service by checking for show run | sec web admin system name or show run | sec web admin customer name

```
telephony-service web admin system name cmesystemadmin secret 0 P@55w0Rd web admin customer name CMEuser password hussain123
```

Ensure HTTP server is enabled by checking for following commands in show run . The parameters in curly braces {...} below can be anything but the ones listed in the example are the most common ones and should not be accounted for in the check.

```
ip http server ip http authentication {local} ip http path {flash:}
```

Check if the GUI files are available in the flash memory of the router by checking for show flash: | include .html and ensuring the listed html files are present.

```
Router#sh flash: | i .html 45        3987 Aug 21 2012 11:32:54 admin_user.html 52        6146 Aug 21 2012 11:33:08 ephone_admin.html 54        3866 Aug 21 2012 11:33:08 normal_user.html 59        2431 Aug 21 2012 11:33:12 telephony_service.html 61        9968 Aug 21 2012 11:33:14 xml-test.html
```

#### Recommended Action:

Ensure all GUI related commands are configured and files available on flash.

Refer to the documentation for additional information:

http://www.cisco.com/en/US/docs/voice_ip_comm/cucme/admin/configuration/guide/cmegui.html

### CUCME Basic Automatic Call Distribution and Auto-Attendant Service (B-ACD) Music-on-Hold

#### Symptom:

If the CUCME Router's flash does not have the B-ACD Music on Hold file, en_bacd_music_on_hold.au, callers in the queue will hear silence while waiting for an agent to become available.

#### Configuration Check:

The BACD service will use the default moh file name, en_bacd_music_on_hold.au, for MOH. Check to make sure that the file is in the flash and has the correct filename.

```
show flash: | sec "en_bacd_music_on_hold.au"
```

#### Recommended Action:

If the file is not in flash, download it from cisco.com. It's available in the BACD zip file, http://tools.cisco.com/squish/E8220 ,  but can be downloaded individually.

Check that the filename is correct. It should be en_bacd_music_on_hold.au .

If it's a custom MOH file, ensure it was created correctly. It should be " G.711 audio file (.au) format with 8-bit, mu-law, and 8-kHz encoding. "

Refer to the documentation for additional information.

http://www.cisco.com/en/US/docs/voice_ip_comm/cucme/bacd/configuration/guide/40bacd.html

### SIP/SCCP Phone Timezone Configuration

#### Symptom:

When the 'timezone' and 'olsontimezone' commands are not configured under Cisco Unified Communications Manager Express (CUCME),  SIP/SCCP IP phones  registered may not display the correct time. They may also not react to daylight savings time changes.

#### Configuration Check:

For SIP phones, check for either the timezone or olsontimezone commands under voice register global .

```
voice register global olsontimezone $timezone version $version
```

or

```
voice register global timezone [1-56]
```

For SCCP phones, check for either the time-zone or olsontimezone commands under telephony-service .

```
telephony-service olsontimezone $timezone version $version
```

or

```
telephony-service time-zone [1-56]
```

#### Recommended Action:

Configure the necessary command under voice register global or telephony-service and assign the correct value. Refer to the CUCME system configuration guide. http://www.cisco.com/en/US/docs/voice_ip_comm/cucme/admin/configuration/guide/cmesystm.html http://www.cisco.com/en/US/docs/voice_ip_comm/cucme/admin/configuration/guide/cmenetwk.html

### Contributed by Cisco Engineers

Felipe Garrido

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager Express