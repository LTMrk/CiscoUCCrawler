---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8832-english-adminguide-cs88-b-conference-8832-admin-guide-cucm-cs88--022470316f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8832/english/adminguide/cs88_b_conference-8832-admin-guide-cucm/cs88_b_conference-8832-admin-guide-cucm_chapter_0110.html
retrieved_at: 2026-08-21T13:36:59.414236+00:00
---

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

# Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Cisco IP Conference Phone Customization

## Chapter: Cisco IP Conference Phone Customization

# Cisco IP Conference Phone Customization

## Custom Phone Ringtones

The Cisco IP Phone ships with two default ringtones that are implemented in hardware: Chirp1 and Chirp2. Cisco Unified Communications
                              Manager also provides a default set of additional phone ringtones that are implemented in software as pulse code modulation
                              (PCM) files. The PCM files, along with an XML file that describes the ring list options that are available at your site, exist
                              in the TFTP directory on each Cisco Unified Communications Manager server.

Attention

All file names are case sensitive. If you use the wrong case for the file name, the phone will not apply your changes.

For more information, see the "Custom Phone Rings and Backgrounds" chapter, Feature Configuration Guide for Cisco Unified Communications Manager .

### Set Up a Custom Phone Ring

Step 1

Create a PCM
                                          			 file for each custom ring (one ring per file).

Ensure the PCM files comply with
                                             			 the format guidelines that are listed in the Custom Ring File Formats section.

Step 2

Upload the new
                                          			 PCM files that you created to the Cisco TFTP server for each Cisco Unified
                                          			 Communications Manager in your cluster.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

Step 3

Save your modifications and close the Ringlist-wb file.

Step 4

To cache the new Ringlist-wb file:

- Stop and start the TFTP service by using Cisco Unified Serviceability

- Disable and reenable the "Enable Caching of Constant and Bin Files at Startup" TFTP service parameter, located in the Advanced Service Parameters area.

### Custom Ring File Formats

The Ringlist-wb.xml file defines an XML object that contains a
                                 		list of phone ring types. This file includes up to 50 ring types. Each ring
                                 		type contains a pointer to the PCM file that is used for that ring type and the
                                 		text that appears on the Ring Type menu on a Cisco IP Phone for that
                                 		ring. The Cisco TFTP server for each Cisco Unified Communications Manager
                                 		contains this file.

The CiscoIPPhoneRinglist XML object uses the following simple
                                 		tag set to describe the information:

```
<CiscoIPPhoneRingList>   
   <Ring>
      <DisplayName/>
      <FileName/>
   </Ring>
</CiscoIPPhoneRingList>
```

The following characteristics apply to the definition names.
                                 		You must include the required DisplayName and FileName for each phone ring
                                 		type.

DisplayName specifies the name of the custom ring for the associated
                                       			 PCM file that displays on the Ring Type menu of the Cisco IP Phone.

FileName specifies the name of the PCM file for the custom ring to
                                       			 associate with DisplayName.

The DisplayName and FileName fields must not exceed 25 characters in length.

This example shows a Ringlist-wb.xml file that defines two phone
                                 		ring types:

```
<CiscoIPPhoneRingList>
 <Ring>
      <DisplayName>Analog Synth 1</DisplayName>
      <FileName>Analog1.rwb</FileName>
   </Ring>
   <Ring>
      <DisplayName>Analog Synth 2</DisplayName>
      <FileName>Analog2.rwb</FileName>
   </Ring>
</CiscoIPPhoneRingList>
```

The PCM files for the rings must meet the following
                                 		requirements for proper playback on Cisco IP Phones:

Raw PCM (no header)

8000 samples per second

8 bits per sample

Mu-law compression

Maximum ring size = 16080 samples

Minimum ring size =  240 samples

Number of samples in the ring = multiple of 240.

Ring start and end at zero crossing.

To create PCM files for custom phone rings,  use any
                                 		standard audio editing package that supports these file format requirements.

## Customize the Dial Tone

You can set up your phones so that users hear different dial tones for internal and external calls. Depending upon your needs,
                              you can choose from three dial tone options:

Default: A different dial tone for inside and outside calls.

Inside: The inside dial tone is used for all calls.

Outside: The outside dial tone is used for all calls.

Always Use Dial Tone is a required field on Cisco Unified Communications Manager.

Step 1

In Cisco Unified Communications Manager Administration, select System > Service Parameters .

Step 2

Select the appropriate Server.

Step 3

Select Cisco CallManager as the Service.

Step 4

Scroll to the Clusterwide Parameters pane.

Step 5

Set Always Use Dial Tone to one of the following:

- Outside

- Inside

- Default

Step 6

Select Save .

Step 7

Restart your phones.

| Attention | All file names are case sensitive. If you use the wrong case for the file name, the phone will not apply your changes. |
|---|---|

| Step 1 | Create a PCM
                                          			 file for each custom ring (one ring per file). Ensure the PCM files comply with
                                             			 the format guidelines that are listed in the Custom Ring File Formats section. |
|---|---|
| Step 2 | Upload the new
                                          			 PCM files that you created to the Cisco TFTP server for each Cisco Unified
                                          			 Communications Manager in your cluster. For more information, see the documentation for your particular Cisco Unified Communications Manager release. |
| Step 3 | Save your modifications and close the Ringlist-wb file. |
| Step 4 | To cache the new Ringlist-wb file: Stop and start the TFTP service by using Cisco Unified Serviceability Disable and reenable the "Enable Caching of Constant and Bin Files at Startup" TFTP service parameter, located in the Advanced Service Parameters area. |

| Note | The DisplayName and FileName fields must not exceed 25 characters in length. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select System > Service Parameters . |
|---|---|
| Step 2 | Select the appropriate Server. |
| Step 3 | Select Cisco CallManager as the Service. |
| Step 4 | Scroll to the Clusterwide Parameters pane. |
| Step 5 | Set Always Use Dial Tone to one of the following: Outside Inside Default |
| Step 6 | Select Save . |
| Step 7 | Restart your phones. |