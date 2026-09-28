---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-13e8edfcf6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_0110.html
retrieved_at: 2026-08-21T13:38:09.898987+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Cisco Unified IP
	 Conference Phone Customization

## Chapter: Cisco Unified IP
	 Conference Phone Customization

# Cisco Unified IP
                     	 Conference Phone Customization

## Cisco Unified IP
                        	 Conference Phone Customization Overview

This chapter explains how you customize configuration files, Cisco
                           		Unified IP Conference Phone ring sounds, and the idle display at your
                           		site. Ring sounds play when the conference phone receives a call. The idle
                           		display appears on the LCD screen when the conference phone has not been used
                           		for a designated period.

## Configuration File Customization and Modification

You can modify configuration files and add customized files to the TFTP directory. You can modify files or
                           		add customized files to the TFTP directory in Cisco Unified Communications
                           		Operating System Administration, from the TFTP Server File Upload window. For
                           		information about how to upload files to the TFTP folder on a Cisco Unified
                           		Communications Manager server, see the Cisco Unified Communications Manager System Guide .

You can obtain a copy of the Ringlist.xml or Ringlist-wb.xml files and the List.xml file
                           		from the system using the following admin command-line interface (CLI) "file" commands:

admin:file

file list

file view

file search

file get

file dump

file tail

file delete

For more information, see the Cisco Intercompany Media Engine Command Line Interface Reference
                              		  Guide .

## Custom Phone Ring
                        	 Creation

The default ringtone
                           		implemented in the conference phone hardware is Chirp1. Cisco Unified
                           		Communications Manager also provides a default set of additional conference
                           		phone ring sounds that are implemented in software as pulse code modulation
                           		(PCM) files. The PCM files, along with an XML file, Ringlist-wb.xml , which describe the ring list options
                           		that are available at your site, are found in the TFTP directory on each Cisco
                           		Unified Communications Manager.

Both file formats
                           		can be used simultaneously on the conference phone.

The conference phone
                           		ringtone formats are backward compatible with the G.711ulaw/8-bit/8000 Hz raw
                           		format as well as with previous Cisco Unified Communications Manager versions.

For more
                           		information, see the Cisco Unified
                              		  Communications Manager System Guide , “Cisco TFTP” chapter, and Cisco Unified
                              		  Communications Operating System Administration Guide , “Software
                           		Upgrades” chapter.

The following
                           		sections describe how you can customize the conference phone ringtones that are
                           		available at your site by creating PCM files and editing the Ringlist-wb.xml
                           		file.

### Ringlist-wb.xml
                           	 File Format Requirements

The Ringlist-wb.xml file defines an XML object that
                              		contains a list of conference phone ring types. This file can include up to 50
                              		ring types. Each ring type contains a pointer to the PCM file that is used for
                              		that ring type and the text that will appear on the Ring Type menu on a
                              		conference phone for that ring. The Cisco TFTP server for each Cisco Unified
                              		Communications Manager contains this file.

The CiscoIPconference stationRingList XML object uses the
                              		following simple tag set to describe the information:

```
<CiscoIPconference stationRingList>
	<Ring>
	<DisplayName/>
	<FileName/>
	</Ring>
</CiscoIPconference stationRingList>
```

DisplayName defines the name of the custom ring for the associated PCM file that will
                                       			 display on the Ring Type menu of the conference phone.

FileName specifies
                                       			 the name of the PCM file for the custom ring to associate with DisplayName .

The DisplayName and FileName fields must not exceed 25 characters.

This example shows a Ringlist-wb.xml file that defines two conference
                              		phone ring types:

```
<CiscoIPconference stationRingList>
	<Ring>
	<DisplayName>Analog Synth 1</DisplayName>
	<FileName>Analog1.rwb</FileName>
	</Ring>
	<Ring>
	<DisplayName>Analog Synth 2</DisplayName>
	<FileName>Analog2.rwb</FileName>
	</Ring>
</CiscoIPconference stationRingList>
```

### PCM File
                           	 Requirements for Custom Ring Types

The PCM files for
                              		the ring types must meet the following requirements for proper playback on
                              		conference phones:

Raw PCM (no
                                    			 header)

16000 samples
                                    			 per second

16 bits per
                                    			 sample

Least
                                    			 Significant Bit

Minimum ring
                                    			 size is 240 samples

Number of
                                    			 samples in the ring is evenly divisible by 240

Maximum ring
                                    			 duration is 10 seconds

Ring starts and
                                    			 ends at the zero crossing

To create PCM
                                    			 files for custom conference phone rings, you can use any standard audio editing
                                    			 packages that support these file format requirements

### Set Up Custom
                           	 Ringtone

To create custom
                                 		  conference phone rings for the conference phone, follow these steps:

Create a PCM
                                          			 file for each custom ring (one ring per file). Ensure the PCM files comply with
                                          			 the format guidelines that are listed in the PCM File Requirements for Custom Ring Types section.

Upload the new
                                          			 PCM files that you created to the Cisco TFTP server for each Cisco Unified
                                          			 Communications Manager in your cluster. For more information, see the Cisco
                                             				Unified Communications Operating System Administration Guide , “Software
                                          			 Upgrades” chapter.

Use a text
                                          			 editor to edit the Ringlist-wb.xml file. See the Ringlist-wb.xml File Format Requirements section for information about how
                                          			 to format this file and for a sample Ringlist-wb.xml file.

Save your
                                          			 modifications and close the Ringlist-wb.xml file.

Cache the new Ringlist-wb.xml file:

Log on to
                                                				  Cisco Unified Communications Manager Administration.

From the
                                                				  Navigation drop-down list at the top right of the window, select Cisco Unified Serviceability , and then press Go .

Choose Tools > Control Center - Feature Services .

In the CM
                                                				  Services area, locate, stop, and start the Cisco TFTP service.

## Idle Display
                        	 Setup

You can specify an
                           		idle display that appears on the conference phone LCD screen. The idle display
                           		is an XML service that the conference phone invokes when the conference phone
                           		has been idle (not in use) for a designated period and no feature menu is open.

XML services that
                           		can be used as idle displays include company logos, product pictures, and stock
                           		quotes.

Formatting an
                                    			 image for display on the conference phone.

Configuring
                                    			 Cisco Unified Communications Manager to display the image on the conference
                                    			 phone.

For detailed
                           		instructions about creating and displaying the idle display, see Creating Idle
                              		  URL Using Graphics on Cisco IP Phone at this URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_tech_note09186a00801c0764.shtml .

Specifying the
                                    			 URL of the idle display XML service:

For a single
                                          				  conference phone: Idle field on the Phone Template Configuration page in the
                                          				  Bulk Administration Tool (BAT)

For multiple
                                          				  conference phones simultaneously: URL Idle Time field on the Cisco Unified
                                          				  Communications Manager Enterprise Parameters page, or the Idle field in the
                                          				  Bulk Administration Tool (BAT)

Specifying the
                                    			 length of time that the conference phone is not used before the idle display
                                    			 XML service is invoked:

For a single
                                          				  conference phone: Idle Timer field on the Cisco Unified Communications Manager
                                          				  Administration Phone Configuration page

For multiple
                                          				  conference phones simultaneously: URL Idle Time field on the Cisco Unified
                                          				  Communications Manager Administration Enterprise Parameters Configuration page,
                                          				  or the Idle Timer field in the Bulk Administration Tool (BAT)

From a conference
                           		phone, you can see settings for the idle display XML service URL and the length
                           		of time that the conference phone is not used before this service is invoked.
                           		To see these settings, choose Apps > Settings > Device
                                 			 Configuration > HTTP Configuration , and then scroll to
                           		the Idle URL and the Idle URL Time parameters.

| Note | The DisplayName and FileName fields must not exceed 25 characters. |
|---|---|

| Step 1 | Create a PCM
                                          			 file for each custom ring (one ring per file). Ensure the PCM files comply with
                                          			 the format guidelines that are listed in the PCM File Requirements for Custom Ring Types section. |
|---|---|
| Step 2 | Upload the new
                                          			 PCM files that you created to the Cisco TFTP server for each Cisco Unified
                                          			 Communications Manager in your cluster. For more information, see the Cisco
                                             				Unified Communications Operating System Administration Guide , “Software
                                          			 Upgrades” chapter. |
| Step 3 | Use a text
                                          			 editor to edit the Ringlist-wb.xml file. See the Ringlist-wb.xml File Format Requirements section for information about how
                                          			 to format this file and for a sample Ringlist-wb.xml file. |
| Step 4 | Save your
                                          			 modifications and close the Ringlist-wb.xml file. |
| Step 5 | Cache the new Ringlist-wb.xml file: Log on to
                                                				  Cisco Unified Communications Manager Administration. From the
                                                				  Navigation drop-down list at the top right of the window, select Cisco Unified Serviceability , and then press Go . Choose Tools > Control Center - Feature Services . In the CM
                                                				  Services area, locate, stop, and start the Cisco TFTP service. |