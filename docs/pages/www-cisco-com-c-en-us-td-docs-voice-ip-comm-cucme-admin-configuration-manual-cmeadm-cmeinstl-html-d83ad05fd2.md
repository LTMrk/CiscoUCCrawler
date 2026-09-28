---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeinstl-html-d83ad05fd2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeinstl.html
retrieved_at: 2026-08-21T07:22:00.221734+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Install and Upgrade Cisco Unified CME Software

## Chapter: Install and Upgrade Cisco Unified CME Software

# Install and Upgrade Cisco Unified CME Software

## Prerequisites for
                        	 Installing Cisco Unified CME Software

Hardware

- Your IP network is
                              		  operational and you can access Cisco web.

- You have a valid Cisco.com
                              		  account.

- You have access to a TFTP
                              		  server for downloading files.

- Cisco router and all recommended
                              		  services hardware for Cisco Unified CME is installed. For installation
                              		  information, see Install Cisco Voice Services Hardware .

Cisco IOS
                              		  Software

- Recommended Cisco IOS IP Voice or
                              		  higher image is downloaded to flash memory in the router. To determine which
                              		  Cisco IOS software release supports the recommended Cisco Unified CME version,
                              		  see Cisco Unified CME and
                                 			 Cisco IOS Software Compatibility Matrix . For installation information,
                              		  see Install Cisco IOS Software .

## Cisco Unified CME
                        	 Software

This section contains a list of the types of files that must be downloaded and installed in the router flash memory to use
                           with Cisco Unified CME. The files listed in this section are included in zipped or tar archives that are downloaded from the
                           Cisco Unified CME software download website at https://software.cisco.com/download/home/277641082 .

### Basic Files

A tar archive contains the basic files you need for Cisco Unified CME. Be sure to download the correct version for the Cisco IOS
                              software release that is running on your router. The basic tar archive generally also contains the phone firmware files that
                              you require, although you may occasionally need to download individual phone firmware files. For information about installing
                              Cisco Unified CME, see Install Cisco Unified CME Software .

### Phone Firmware
                           	 Files

Phone firmware
                              		files provide code to enable phone displays and operations. These files are
                              		specialized for each phone type and protocol, SIP or SCCP, and are periodically
                              		revised. You must be sure to have the appropriate phone firmware files for the
                              		types of phones, protocol being used, and Cisco Unified CME version at your
                              		site.

New IP phones are
                              		shipped from Cisco with a default manufacturing SCCP image. When a IP phone
                              		downloads its configuration profile, the phone compares the phone firmware
                              		mentioned in the configuration profile with the firmware already installed on
                              		the phone. If the firmware version differs from the one that is currently
                              		loaded on the phone, the phone contacts the TFTP server to upgrade to the new
                              		phone firmware and downloads the new firmware before registering with
                              		Cisco Unified CME.

Generally, phone
                              		firmware files are included in the Cisco Unified CME software archive that you
                              		download. They can also be posted on the software download website as
                              		individual files or archives.

Early versions of
                              		Cisco phone firmware for SCCP and SIP IP phones had filenames as follows:

SCCP
                                    			 firmware—P003xxyy.bin

SIP
                                    			 firmware—P0S3xxyy.bin

In both bases, x
                              		represents the major version, and y represented the minor version. The third
                              		character represents the protocol, “0” for SCCP or “S” for SIP.

In later versions,
                              		the following conventions are used:

SCCP
                                    			 firmware—P003xxyyzzww, where x represents the major version, y represents the
                                    			 major subversion, z represents the maintenance version, and w represents the
                                    			 maintenance subversion.

SIP
                                    			 firmware—P0S3-xx-y-zz, where x represents the major version, y represents the
                                    			 minor version, and z represents the subversions.

The third
                                    			 character in a filename—Represents the protocol, “0” for SCCP or “S” for SIP.

There are exceptions
                              		to the general guidelines. For Cisco ATA, the filename begins with AT. For
                              		Cisco Unified IP Phone 7002, 7905, and 7912, the filename can begin with CP.

Signed and unsigned
                              		versions of phone firmware are available for certain phone types. Signed binary
                              		files support image authentication, which increases system security. We
                              		recommend signed versions if your version of Cisco Unified CME supports them.
                              		Signed binary files have .sbn file extensions, and unsigned files have .bin
                              		file extensions.

For Java-based IP
                              		phones, such as the Cisco Unified IP Phone 7911, 7941, 7941GE, 7961, 7961GE,
                              		7970, and 7971, the firmware consists of multiple files including JAR and tone
                              		files. All of the firmware files for each phone type must be downloaded the
                              		TFTP server before they can be downloaded to the phone.

The following
                              		example shows a list of phone firmware files that are installed in flash memory
                              		for the Cisco Unified IP Phone 7911:

```
tftp-server flash:SCCP11.7-2-1-0S.loads
tftp-server flash:term06.default.loads
tftp-server flash:term11.default.loads
tftp-server flash:cvm11.7-2-0-66.sbn
tftp-server flash:jar11.7-2-0-66.sbn
tftp-server flash:dsp11.1-0-0-73.sbn
tftp-server flash:apps11.1-0-0-72.sbn
tftp-server flash:cnu11.3-0-0-81.sbn
```

However, you only
                              		specify the filename for the image file when configuring Cisco Unified CME. For
                              		Java-based IP phones, the following naming conventions are used for image
                              		files:

SCCP
                                    			 firmware—TERMnn.xx-y-z-ww or SCCPnn.xx-y-zz-ww, where n represents the phone
                                    			 type, x represents the major version, y represents the major subversion, z
                                    			 represents the maintenance version, and w represents the maintenance
                                    			 subversion.

The following
                              		example shows how to configure Cisco Unified CME so that the
                              		Cisco Unified IP Phone 7911 can download the appropriate SCCP firmware from
                              		flash memory:

```
Router(config)# telephony-service
```

```
Router(config-telephony)# load 7911 SCCP11.7-2-1-0S
```

Table 1 contains firmware-naming convention examples, in alphabetical order:

SCCP
                                          				  Phones

SIP Phones

Image

Version

Image

Version

P00303030300

3.3(3)

P0S3-04-4-00

4.4

P00305000200

5.0(2)

P0S3-05-2-00

5.2

P00306000100

6.0(1)

P0S3-06-0-00

6.0

SCCP41.8-0-4ES4-0-1S

8.0(4)

SIP70.8-0-3S

8.0(3)

TERM41.7-0-3-0S

7.0(3)

—

—

The phone firmware
                              		filenames for each phone type and Cisco Unified CME version are listed in the
                              		appropriate document available at Cisco CME Supported Firmware,
                                 		  Platforms, Memory, and Voice Products .

For information
                              		about installing firmware files, see Install Cisco Unified CME Software .

For information
                              		about configuring Cisco Unified CME for upgrading between versions or
                              		converting between SCCP and SIP, see Install and Upgrade Cisco Unified CME Software .

### XML Template

The file called xml.template can be copied and modified to allow or restrict specific functions to customer administrators,
                              a class of administrative users with limited capabilities in a Unified CME system. This file is included in tar archives (cme-basic-...).
                              To install the file, see Install Cisco Unified CME Software .

### Music-on-Hold
                           	 (MOH) File

An audio file named
                              		music-on-hold.au provides music for external callers on hold when a live feed
                              		is not used. This file is included in the tar archive with basic files
                              		(cme-basic-...). To install the file, see Install Cisco Unified CME Software .

### Script
                           	 Files

Archives containing
                              		Tcl script files are listed individually on the Cisco Unified CME software
                              		download website. For example, the file named app-h450-transfer.2.0.0.9.zip.tar
                              		contains a script that adds H.450 transfer and forwarding support for analog
                              		FXS ports.

The
                              		Cisco Unified CME Basic Automatic Call Distribution and Auto Attendant Service
                              		(B-ACD) requires a number of script files and audio files, which are contained
                              		in a tar archive with the name cme-b-acd-.... For a list of files in the
                              		archive and for more information about the files, see Cisco CME B-ACD and TCL
                                 		  Call-Handling Applications .

For information
                              		about installing Tcl script file or an archive, see Install Cisco Unified CME Software .

### Bundled TSP Archive

An archive is available at the Cisco Unified CME software download website that contains several Telephony Application Programming Interface (TAPI) Telephony Service Provider (TSP) files.
                              These files are needed to set up individual PCs for Cisco Unified IP phone users who wish to make use of Cisco Unified CME-TAPI
                              integration with TAPI-capable PC software. To install the files from the archive, see the installation instructions in TAPI Developer Guide for Cisco CME/SRST .

### File Naming Conventions

Most of the files available at the Cisco Unified CME software download
                              		website are archives that must be uncompressed before individual files can be
                              		copied to the router. In general, the following naming conventions apply to
                              		files on the Cisco Unified CME software download website:

```
cme-basic-...
```

Basic Cisco Unified CME files, including phone firmware files for a particular Cisco Unified CME version or versions.

```
cmterm..., P00..., 7970..
```

Phone firmware files.

```
cme-b-acd...
```

Files required for Cisco Unified CME B-ACD service.

## Install and
                        	 Upgrade Cisco Unified CME Software

### Install Cisco
                           	 Unified CME Software

Step 1

Go to https://software.cisco.com/download/home/277641082 .

Step 2

Select the
                                          			 file to download.

Step 3

Download zip
                                          			 file to tftp server.

Step 4

Use the zip
                                          			 program to extract the file to be installed, then:

If the
                                                				  file is an individual file, use the copy command to copy the files to router flash:

```
Router# copy tftp://x.x.x.x/P00307020300.sbn flash:
```

If the
                                                				  file is a tar file, use the archive
                                                      						tar command to extract the files to flash memory.

```
Router# archive tar /xtract source-url flash: /file-url
```

Step 5

Verify the
                                          			 installation. Use the show flash: command to list the files installed in in flash memory.

```
Router# show flash:
 
 31      128996 Sep 19 2005 12:19:02 -07:00 P00307020300.bin
 32         461 Sep 19 2005 12:19:02 -07:00 P00307020300.loads
 33      681290 Sep 19 2005 12:19:04 -07:00 P00307020300.sb2
 34      129400 Sep 19 2005 12:19:04 -07:00 P00307020300.sbn
```

Step 6

Use the archive tar
                                                				  /create command to create a backup tar file of all the files
                                          			 stored in flash. You can create a tar file that includes all files in a
                                          			 directory or a list of up to four files from a directory.

For example,
                                             				the following command creates a tar file of the three files listed:

```
archive tar /create flash:abctestlist.tar flash:orig1 sample1.txt sample2.txt sample3.txt
```

The following
                                             				command creates a tar file of all the files in the directory:

```
archive tar /create flash:abctest1.tar flash:orig1
```

The following
                                             				command creates a tar file to backup the flash files to a USB card, on
                                             				supported platforms:

```
archive tar /create usbflash1:abctest1.tar flash:orig1
```

#### What to do next

If you
                                       				installed Cisco Unified CME software and Cisco Unified CME is not configured on your router, see Network Parameters .

If
                                       				Cisco Unified IP phones presently connected to Cisco Unified CME are using the
                                       				SCCP protocol to receive and place calls and the firmware version must be
                                       				upgraded to a recommended version, or if the phones to be connected to
                                       				Cisco Unified CME are brand new, out-of-the-box, the phone firmware preloaded
                                       				at the factory must be upgraded to the recommended version before your phones
                                       				can complete registration, see Upgrade or Downgrade SCCP Phone Firmware .

If
                                       				Cisco Unified IP phones presently connected to Cisco Unified CME are using the
                                       				SIP protocol to receive and place calls and the firmware version must be
                                       				upgraded to a recommended version, see Upgrade or Downgrade SIP Phone Firmware .

If
                                       				Cisco Unified IP phones presently connected to Cisco Unified CME are using the
                                       				SCCP protocol to receive and place calls and you now want some or all of these
                                       				phones to use the SIP protocol, the phone firmware for each phone type must be
                                       				upgraded from SCCP to the recommended SIP version before the phones can
                                       				register. See Phone Firmware Conversion from SCCP to SIP .

If
                                       				Cisco Unified IP phones to be connected to Cisco Unified CME are using the SIP
                                       				protocol and are brand new, out-of-the-box, the phone firmware preloaded at the
                                       				factory must be upgraded to the recommended SIP version before your SIP phones
                                       				can complete registration. See Phone Firmware Conversion from SCCP to SIP .

If
                                       				Cisco Unified IP phones presently connected to Cisco Unified CME are using the
                                       				SIP protocol to receive and place calls and you now want some or all of these
                                       				phones to use the SCCP protocol, the phone firmware for each phone type must be
                                       				upgraded from SIP to the recommended SCCP version before the phones can
                                       				register. See Phone Firmware Conversion from SIP to SCCP .

### Upgrade or
                           	 Downgrade SCCP Phone Firmware

#### Before you begin

Phone firmware
                                       				for Cisco Unified IP phones to be connected to Cisco Unified CME, including all
                                       				versions required during an upgrade or downgrade sequence, must be loaded in
                                       				the flash memory of the TFTP server from which the phones download their
                                       				configuration profiles. For information about installing firmware files in
                                       				flash memory, see Install Cisco Unified CME Software .

### SUMMARY STEPS

- enable

- configure terminal

- tftp-server device : firmware-file

- telephony-service

- load phone-type
                                       				  firmware-file

- create cnf-files

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

tftp-server device : firmware-file

#### Example:

```
Router(config)# tftp-server flash:P00307020300.loads Router(config)# tftp-server flash:P00307020300.sb2 Router(config)# tftp-server flash:P00307020300.sbn Router(config)# tftp-server flash:P00307020300.bin
```

(Optional)
                                             				Creates TFTP bindings to permit IP phones served by the Cisco Unified CME
                                             				router to access the specified file.

A
                                                   					 separate tftp-server command is required for each phone type.

Required
                                                   					 for Cisco Unified CME 7.0/4.3 and earlier versions.

Cisco Unified CME 7.0(1) and later versions: Required only if
                                                   					 the location for cnf files is not flash or
                                                   					 slot 0. Use the complete filename, including the file suffix, for phone
                                                   					 firmware versions later than version 8-2-2 for all phone types.

Step 4

telephony-service

#### Example:

```
Router(config)# telephony service
```

Enters
                                             				telephony-service configuration mode.

Step 5

load phone-type
                                                				  firmware-file

#### Example:

```
Router(config-telephony)# load 7960-7940 P00307020300
```

Associates a
                                             				phone type with a phone firmware file.

A separate load command is required for each IP phone type.

firmware-file —Filenames are case-sensitive.

In
                                                   					 Cisco Unified CME 7.0/4.3 and earlier versions, do not use the file suffix
                                                   					 (.bin, .sbin, .loads) for any phone type except the Cisco ATA and Cisco Unified
                                                   					 IP Phone 7905 and 7912.

In
                                                   					 Cisco Unified CME 7.0(1) and later versions, you must use the complete
                                                   					 filename, including the file suffix, for phone firmware versions later than
                                                   					 version 8-2-2 for all phone types.

Step 6

create cnf-files

#### Example:

```
Router(config-telephony)# create cnf-files
```

Builds XML
                                             				configuration files required for SCCP phones.

Step 7

end

#### Example:

```
Router(config-telephony)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

If the
                                       				Cisco Unified IP phone to be upgraded is not configured in Cisco Unified CME,
                                       				see Configure Phones for a PBX System .

If the
                                       				Cisco Unified IP phone is already configured in Cisco Unified CME and can make
                                       				and receive calls, you are ready to reboot the Cisco Unified IP phones to
                                       				download the phone firmware to the phone. See Reset and Restart Cisco Unified IP Phones .

### Upgrade or
                           	 Downgrade SIP Phone Firmware

The upgrade and
                                 		  downgrade sequences for SIP phones differ per phone type as follows:

Upgrading or downgrading the phone firmware for Cisco Unified IP Phone 7905G, Cisco Unified IP Phone 7912G, and Cisco ATA
                                       Analog Telephone Adapter is straightforward; modify the load command to upgrade directly to the target load.

The phone firmware version upgrade sequence for Cisco Unified IP Phone 7940Gs and 7960Gs is from version [234].x to 4.4, to
                                       5.3, to 6.x, to 7.x. You cannot go directly from version [234].x to version 7.x.

To downgrade phone firmware for Cisco Unified IP Phone 7940Gs and 7960Gs, first upgrade to version 7.x, then modify the load command to downgrade directly to the target phone firmware.

Restriction

Cisco Unified IP Phone 7905G, Cisco Unified IP Phone 7912G, and Cisco ATA—Signed load starts from SIP v1.1. After you upgrade
                                                   the firmware to a signed load, you cannot downgrade the firmware to an unsigned load.

Cisco Unified IP Phone 7940G and Cisco Unified IP Phone 7960G—Signed load starts from SIP v5.x. Once you upgrade the firmware
                                                   to a signed load, you cannot downgrade the firmware to an unsigned load.

The procedures for upgrading phone firmware files for SIP phones is the same for all Cisco Unified IP phones. For other limits
                                                   on firmware upgrade between versions, see Cisco 7940 and 7960 IP Phones Firmware Upgrade Matrix .

#### Before you begin

Phone firmware for
                                 		  Cisco Unified IP phones to be connected to Cisco Unified CME, including all
                                 		  versions required during an upgrade or downgrade sequence, must be loaded in
                                 		  the flash memory of the TFTP server from which the phones will download their
                                 		  configuration profiles. For information about installing firmware files in
                                 		  flash memory, see Install Cisco Unified CME Software .

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- mode cme

- load phone-type
                                       				  firmware-file

- upgrade

- Repeat Step 5
                                 			 and Step 6.

- file text

- create profile

- exit

- voice register
                                       				  pool pool-tag

- reset

- exit

- voice register
                                       				  global

- no upgrade

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice register global configuration mode to set parameters for all supported SIP phones in Cisco Unified CME.

Step 4

mode cme

#### Example:

```
Router(config-register-global)# mode cme
```

Enables mode for provisioning SIP phones in Cisco Unified CME.

Step 5

load phone-type
                                                				  firmware-file

#### Example:

```
Router(config-register-global)# load 7960-7940 P0S3-06-0-00
```

Associates a
                                             				phone type with a phone firmware file.

A separate load command is required for each IP phone type.

firmware-file —Filename to be associated with the specified Cisco Unified IP phone type.

Do not use the .sbin or .loads file extension except for Cisco Unified IP Phone 7905 and 7912.

Step 6

upgrade

#### Example:

```
Router(config-register-global)# upgrade
```

Generates a
                                             				file with the universal application loader image for upgrading phone firmware
                                             				and performs the TFTP server alias binding.

Step 7

Repeat Step 5
                                          			 and Step 6.

#### Example:

```
Router(config-register-global)# load 7960-7940 P0S3-07-4-00
```

```
Router(config-register-global)# upgrade
```

(Optional)
                                             				Repeat for each version required in multistep upgrade sequences only.

Step 8

file text

#### Example:

```
Router(config-register-global)# file text
```

(Optional) Generates ASCII text files for Cisco Unified IP Phone 7905s and 7905Gs, Cisco Unified IP Phone 7912s and 7912Gs,
                                             Cisco ATA-186, or Cisco ATA-188.

Default—System generates binary files to save disk space.

Step 9

create profile

#### Example:

```
Router(config-register-global)# create profile
```

Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command.

Step 10

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits from the
                                             				current command mode to the next highest mode in the configuration mode
                                             				hierarchy.

Step 11

voice register
                                                				  pool pool-tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones.

pool-tag —Unique sequence number of the SIP phone to be configured. Range is 1 to 100 or the upper limit is as defined by max-pool command.

Step 12

reset

#### Example:

```
Router(config-register-pool)# reset
```

Performs a
                                             				complete reboot of the single SIP phone specified with the voice register pool command and contacts the DHCP server and the TFTP
                                             				server for updated information.

Step 13

exit

#### Example:

```
Router(config-register-pool)# exit
```

Exits from
                                             				the current command mode to the next highest mode in the configuration mode
                                             				hierarchy.

Step 14

voice register
                                                				  global

#### Example:

```
Router(config)# voice register global
```

Enters voice register global configuration mode to set parameters for all supported SIP phones in Cisco Unified CME.

Step 15

no upgrade

#### Example:

```
Router(config-register-global)# no upgrade
```

Return to the default for the upgrade command.

Step 16

end

#### Example:

```
Router(config-register-global)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### Example

The following example shows the configuration steps for upgrading firmware for a Cisco Unified IP Phone 7960G or Cisco Unified
                                 IP Phone 7940G from SIP 5.3 to SIP 6.0, then from SIP 6.0 to SIP 7.4:

```
Router(config)# voice register global
Router(config-register-global)# mode cme
Router(config-register-global)# load 7960 P0S3-06-0-00
Router(config-register-global)# upgrade
Router(config-register-global)# load 7960 P0S3-07-4-00
Router(config-register-global)# create profile
```

The following example shows the configuration steps for downgrading firmware for a Cisco Unified IP Phone 7960/40 from SIP
                                 7.4 to SIP 6.0:

```
Router(config)# voice register global
Router(config-register-global)# mode cme
Router(config-register-global)# load 7960 P0S3-06-0-00
Router(config-register-global)# upgrade
Router(config-register-global)# create profile
```

#### What to do next

If the Cisco Unified IP phone to be upgraded is not configured in Cisco Unified CME, see Configure Phones for a PBX System .

If the Cisco Unified IP phone is already configured in Cisco Unified CME and can make and receive calls, you are ready to
                                       reboot the Cisco Unified IP phones to download the phone firmware to the phone. See Reset and Restart Cisco Unified IP Phones .

### Phone Firmware
                           	 Conversion from SCCP to SIP

If
                                 		  Cisco Unified IP phones presently connected to Cisco Unified CME are using the
                                 		  SCCP protocol to receive and place calls and you now want some or all of these
                                 		  phones to use the SIP protocol, the phone firmware for each phone type must be
                                 		  upgraded from SCCP to the recommended SIP version before the phones can
                                 		  register. If Cisco Unified IP phones to be connected to Cisco Unified CME are
                                 		  brand new, out-of-the-box, the SCCP phone firmware preloaded at the factory
                                 		  must be upgraded to the recommended SIP version before your SIP phones can
                                 		  complete registration.

#### Before you begin

Phone firmware
                                       				for Cisco Unified IP phones to be connected to Cisco Unified CME, including all
                                       				versions required during an upgrade or downgrade sequence, must be loaded in
                                       				the flash memory of the TFTP server from which the phones download their
                                       				configuration profiles. For information about installing firmware files in
                                       				flash memory, see Install Cisco Unified CME Software .

Cisco Unified IP Phone 7940Gs and Cisco Unified IP Phone
                                       				7960Gs—If these IP phones are already configured in Cisco Unified CME to use
                                       				the SCCP protocol, the SCCP phone firmware on the phone must be version 5.x. If
                                       				required, upgrade the SCCP phone firmware to 5.x before upgrading to SIP.

### SUMMARY STEPS

- enable

- configure terminal

- no ephone ephone-tag

- exit

- no ephone-dn dn-tag

- exit

- voice register global

- mode cme

- load phone-type
                                       				  firmware-file

- upgrade

- Repeat Step
                                 			 9 and Step 10.

- create
                                       				  profile

- file text

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

no ephone ephone-tag

#### Example:

```
Router (config)# no ephone 23
```

(Optional)
                                             				Disables the ephone and removes the ephone configuration.

Required
                                                   					 only if the Cisco Unified IP phone to be configured is already connected to
                                                   					 Cisco Unified CME and is using SCCP protocol.

ephone-tag —Particular IP phone to which this
                                                   					 configuration change will apply.

Step 4

exit

#### Example:

```
Router(config-ephone)# exit
```

(Optional)
                                             				Exits from the current command mode to the next highest mode in the
                                             				configuration mode hierarchy.

Required
                                                   					 only if you performed the previous step.

Step 5

no ephone-dn dn-tag

(Optional)
                                             				Disables the ephone-dn and removes the ephone-dn configuration.

Required
                                                   					 only if this directory number is not now nor will be associated to any SCCP
                                                   					 phone line, intercom line, paging line, voice-mail port, or message-waiting
                                                   					 indicator (MWI) connected to Cisco Unified CME.

dn-tag —Particular configuration to which this
                                                   					 change will apply.

Step 6

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

(Optional)
                                             				Exits from the current command mode to the next highest mode in the
                                             				configuration mode hierarchy.

Required
                                                   					 only if you performed the previous step.

Step 7

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 8

mode cme

#### Example:

```
Router(config-register-global)# mode cme
```

Enables mode
                                             				for provisioning SIP phones in Cisco Unified CME.

Step 9

load phone-type
                                                				  firmware-file

#### Example:

```
Router(config-register-global)# load 7960-7940 P0S3-06-3-00
```

Associates a
                                             				phone type with a phone firmware file.

A separate load command is required for each IP phone type.

Step 10

upgrade

#### Example:

```
Router(config-register-global)# upgrade
```

Generates a
                                             				file with the universal application loader image for upgrading phone firmware
                                             				and performs the TFTP server alias binding.

Step 11

Repeat Step
                                          			 9 and Step 10.

#### Example:

```
Router(config-register-global)# load 7960-7940 P0S3-07-4-00
```

```
Router(config-register-global)# upgrade
```

(Optional)
                                             				Repeat for each version required in multistep upgrade sequences only.

Step 12

create
                                                				  profile

#### Example:

```
Router(config-register-global)# create profile
```

Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command.

Step 13

file text

#### Example:

```
Router(config-register-global)# file text
```

(Optional)
                                             				Generates ASCII text files for Cisco Unified IP Phones 7905 and 7905G,
                                             				Cisco Unified IP Phone 7912 and Cisco Unified IP  Phone 7912G, Cisco ATA-186,
                                             				or Cisco ATA-188.

Default—System generates binary files to save disk space.

Step 14

end

#### Example:

```
Router(config-register-global)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### Example

The following
                                 		  example shows the configuration steps for converting firmware on an
                                 		  Cisco Unified IP phone already connected in Cisco Unified CME and using the
                                 		  SCCP protocol, from SCCP 5.x to SIP 7.4:

```
Router(config)# telephony-service
```

```
Router(config-telephony)# no create cnf
```

```
CNF files deleted
```

```
Router(config-telephony)# voice register global
```

```
Router(config-register-global)# mode cme
```

```
Router(config-register-global)# load 7960 P0S3-07-4-00
```

```
Router(config-register-global)# upgrade
```

```
Router(config-register-global)# create profile
```

#### What to do next

After you
                                 		  configure the upgrade command, refer to the following statements to determine which task to perform
                                 		  next.

If the
                                       				Cisco Unified IP phone to be upgraded is already connected in Cisco Unified CME
                                       				and you removed the SCCP configuration file for the phone but have not
                                       				configured this phone for SIP in Cisco Unified CME, see Configure Phones for a PBX System .

If the
                                       				Cisco Unified IP phones to be upgraded are already configured in
                                       				Cisco Unified CME, see Reset and Restart Cisco Unified IP Phones .

### Phone Firmware
                           	 Conversion from SIP to SCCP

If
                                 		  Cisco Unified IP phones presently connected to Cisco Unified CME are using the
                                 		  SIP protocol to receive and place calls and you now want some or all of these
                                 		  phones to use the SCCP protocol, the phone firmware for each phone type must be
                                 		  upgraded from SIP to SCCP before the phones can register.

If codec values
                                             			 for the dial peers of a connection do not match, the call fails. The default
                                             			 codec for the POTS dial peer for an SCCP phone is G.711 and the default codec
                                             			 for a VoIP dial peer for a SIP phone is G.729. If neither the SCCP phone nor
                                             			 the SIP phone in Cisco Unified CME has been specifically configured to change
                                             			 the codec, calls between the two IP phones on the same router will produce a
                                             			 busy signal caused by the mismatched default codecs. To avoid codec mismatch,
                                             			 specify the codec for SIP and SCCP phones in Cisco Unified CME. For more
                                             			 information, see Configure Phones for a PBX System .

#### Before you begin

Phone firmware
                                          				for Cisco Unified IP phones to be connected to Cisco Unified CME, including all
                                          				versions required during an upgrade or downgrade sequence, must be loaded in
                                          				the flash memory of the TFTP server from which the phones will download their
                                          				configuration profiles. For information about installing firmware files in
                                          				flash memory, see Install Cisco Unified CME Software .

Cisco Unified IP Phone 7940Gs and Cisco Unified IP Phone
                                          				7960Gs—If these IP phones are already configured in Cisco Unified CME to use
                                          				the SIP protocol, the SIP phone firmware must be version 7.x. See Upgrade or Downgrade SIP Phone Firmware .

#### Remove SIP
                              	 Configuration Profile

To remove the SIP
                                    		  configuration profile before downloading the SCCP phone firmware to convert a
                                    		  phone from SIP to SCCP, perform the steps in this task.

### SUMMARY STEPS

- enable

- configure terminal

- no voice register
                                          				  pool pool-tag

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

no voice register
                                                   				  pool pool-tag

##### Example:

```
Router(config)# no voice register pool 1
```

Disables voice
                                                				register pool and removes the voice pool configuration.

pool-tag —Unique sequence number for a particular
                                                      					 SIP phone to which this configuration applies.

Step 4

end

##### Example:

```
Router(config-register-pool)# end
```

Exits from the
                                                				current command mode to the next highest mode in the configuration mode
                                                				hierarchy.

#### Generate SCCP XML
                              	 Configuration File to Upgrade from SIP to SCCP

To create an ephone entry and generate a new SCCP XML configuration file for upgrading a particular Cisco Unified IP phone
                                    in Cisco Unified CME from SIP to SCCP, perform the steps in this task.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- exit

- tftp-server device : firmware-file

- telephony-service

- load phone-type firmware-file

- create cnf-files

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

ephone-dn dn-tag

##### Example:

```
Router(config)# ephone dn 1
```

Enters
                                                				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                                				dual-line status.

dn-tag —Unique sequence number that identifies this ephone-dn during configuration tasks. The maximum number of ephone-dns in Cisco
                                                      Unified CME is version and platform specific. Type ? to display range.

Step 4

exit

##### Example:

```
Router(config-ephone-dn)# exit
```

Exits from the
                                                				current command mode to the next highest mode in the configuration mode
                                                				hierarchy.

Step 5

tftp-server device : firmware-file

##### Example:

```
Router(config)# tftp-server flash:P00307020300.loads Router(config)# tftp-server flash:P00307020300.sb2 Router(config)# tftp-server flash:P00307020300.sbn Router(config)# tftp-server flash:P00307020300.bin
```

(Optional)
                                                				Creates TFTP bindings to permit IP phones served by the Cisco Unified CME
                                                				router to access the specified file.

A separate tftp-server command is required for each phone type.

Required
                                                      					 for Cisco Unified CME 7.0/4.3 and earlier versions.

Cisco Unified CME 7.0(1) and later versions: Required only if
                                                      					 the location for cnf files is not flash or slot 0. Use the complete filename, including the
                                                      					 file suffix, for phone firmware versions later than version 8-2-2 for all phone
                                                      					 types.

Step 6

telephony-service

##### Example:

```
Router(config)# telephony service
```

Enters
                                                				telephony-service configuration mode.

Step 7

load phone-type firmware-file

##### Example:

```
Router(config-telephony)# load 7960-7940 P00307020300
```

Associates a
                                                				phone type with a phone firmware file.

A separate load command is required for each IP phone type.

firmware-file —Filename is case-sensitive.

Cisco Unified CME 7.0/4.3 and earlier versions: Do not use the .sbin or .loads file extension except for Cisco Unified IP
                                                      Phone 7905 and 7912.

Cisco Unified CME 7.0(1) and later versions: Use the complete filename, including the file suffix, for phone firmware versions
                                                      later than version 8-2-2 for all phone types.

Step 8

create cnf-files

##### Example:

```
Router(config-telephony)# create cnf-files
```

Builds XML
                                                				configuration files required for SCCP phones.

Step 9

end

##### Example:

```
Router(config-telephony)# end
```

Exits to
                                                				privileged EXEC mode.

#### Example

The following
                                    		  example shows the configuration steps for upgrading firmware for a
                                    		  Cisco Unified IP Phone 7960G from SIP to SCCP. First the SIP firmware is
                                    		  upgraded to SIP 6.3 and from SIP 6.3 to SIP 7.4; then, the phone firmware is
                                    		  upgraded from SIP 7.4 to SCCP 7.2(3). The SIP configuration profile is deleted
                                    		  and a new ephone configuration profile is created for the Cisco Unified IP
                                    		  phone.

```
Router(config)# v oice register global
Router(config-register-global)# mode cme
Router(config-register-global)# load 7960 P0S3-06-0-00
Router(config-register-global)# upgrade
Router(config-register-global)# load 7960 P0S3-07-4-00
Router(config-register-global)# exit
Router(config)# no voice register pool 1
Router(config-register-pool)# exit
Router(config)# v oice register global
Router(config-register-global)# no upgrade
Router(config-register-global)# exit
Router(config)# ephone-dn 1
Router(config-ephone-dn)# exit
Router(config)# tftp-server flash:P00307020300.loads
Router(config)# tftp-server flash:P00307020300.sb2
Router(config)# tftp-server flash:P00307020300.sbn
Router(config)# tftp-server flash:P00307020300.bin
Router(config)# telephony service
Router(config-telephony)# load 7960-7940 P00307000100
Router(config-telephony)# create cnf-files
```

#### What to Do Next

After you configure the upgrade command:

If the Cisco Unified IP phone to be upgraded is already connected in Cisco Unified CME and you removed the SIP configuration
                                       file for the phone and have not configured the SCCP phone in Cisco Unified CME, see Configure Phones for a PBX System .

If the Cisco Unified IP phones to be upgraded are already configured in Cisco Unified CME, see Reset and Restart Cisco Unified IP Phones .

### Verify SCCP Phone
                           	 Firmware Version

Step 1

show flash:

Use this
                                             				command to learn the filenames associated with that phone firmware

```
Router# show flash:
```

```
31      128996 Sep 19 2005 12:19:02 -07:00 P00307020300.bin
```

```
32         461 Sep 19 2005 12:19:02 -07:00 P00307020300.loads
```

```
33      681290 Sep 19 2005 12:19:04 -07:00 P00307020300.sb2
```

```
34      129400 Sep 19 2005 12:19:04 -07:00 P00307020300.sbn
```

Step 2

show ephone phone-load

Use this
                                             				command to verify which phone firmware is installed on a particular ephone. The
                                             				DeviceName includes the MAC address for the IP phone.

```
Router# show ephone phone-load
```

```
DeviceName        CurrentPhoneload       PreviousPhoneload      LastReset
```

```
=====================================================================
```

```
SEP000A8A2C8C6E   7.3(3.02)                                     Initialized
```

### Troubleshooting Tips for Cisco Phone Firmware

Use the debug tftp event command to troubleshoot an attempt to upgrade or convert Cisco phone firmware files for SIP phones.

| SCCP
                                          				  Phones | SIP Phones |
|---|---|
| Image | Version | Image | Version |
| P00303030300 | 3.3(3) | P0S3-04-4-00 | 4.4 |
| P00305000200 | 5.0(2) | P0S3-05-2-00 | 5.2 |
| P00306000100 | 6.0(1) | P0S3-06-0-00 | 6.0 |
| SCCP41.8-0-4ES4-0-1S | 8.0(4) | SIP70.8-0-3S | 8.0(3) |
| TERM41.7-0-3-0S | 7.0(3) | — | — |

| cme-basic-... | Basic Cisco Unified CME files, including phone firmware files for a particular Cisco Unified CME version or versions. |
|---|---|
| cmterm..., P00..., 7970.. | Phone firmware files. Note Not all firmware files to be downloaded to a phone are specified in the load command. For a list of file names to be installed in flash memory, and which file names are to be specified by using the load command, see Cisco Unified CME Supported Firmware, Platforms, Memory, and Voice Products. | Note | Not all firmware files to be downloaded to a phone are specified in the load command. For a list of file names to be installed in flash memory, and which file names are to be specified by using the load command, see Cisco Unified CME Supported Firmware, Platforms, Memory, and Voice Products. |
| Note | Not all firmware files to be downloaded to a phone are specified in the load command. For a list of file names to be installed in flash memory, and which file names are to be specified by using the load command, see Cisco Unified CME Supported Firmware, Platforms, Memory, and Voice Products. |
| cme-b-acd... | Files required for Cisco Unified CME B-ACD service. |

| Note | Not all firmware files to be downloaded to a phone are specified in the load command. For a list of file names to be installed in flash memory, and which file names are to be specified by using the load command, see Cisco Unified CME Supported Firmware, Platforms, Memory, and Voice Products. |
|---|---|

| Note | Customers who
                                    		purchase a router bundle enabled with Cisco Unified CME will have the necessary
                                    		Cisco Unified CME files installed at time of manufacture. |
|---|---|

| Step 1 | Go to https://software.cisco.com/download/home/277641082 . |
|---|---|
| Step 2 | Select the
                                          			 file to download. |
| Step 3 | Download zip
                                          			 file to tftp server. |
| Step 4 | Use the zip
                                          			 program to extract the file to be installed, then: If the
                                                				  file is an individual file, use the copy command to copy the files to router flash: Router# copy tftp://x.x.x.x/P00307020300.sbn flash: If the
                                                				  file is a tar file, use the archive
                                                      						tar command to extract the files to flash memory. Router# archive tar /xtract source-url flash: /file-url |
| Step 5 | Verify the
                                          			 installation. Use the show flash: command to list the files installed in in flash memory. Router# show flash:
 
 31      128996 Sep 19 2005 12:19:02 -07:00 P00307020300.bin
 32         461 Sep 19 2005 12:19:02 -07:00 P00307020300.loads
 33      681290 Sep 19 2005 12:19:04 -07:00 P00307020300.sb2
 34      129400 Sep 19 2005 12:19:04 -07:00 P00307020300.sbn |
| Step 6 | Use the archive tar
                                                				  /create command to create a backup tar file of all the files
                                          			 stored in flash. You can create a tar file that includes all files in a
                                          			 directory or a list of up to four files from a directory. For example,
                                             				the following command creates a tar file of the three files listed: archive tar /create flash:abctestlist.tar flash:orig1 sample1.txt sample2.txt sample3.txt The following
                                             				command creates a tar file of all the files in the directory: archive tar /create flash:abctest1.tar flash:orig1 The following
                                             				command creates a tar file to backup the flash files to a USB card, on
                                             				supported platforms: archive tar /create usbflash1:abctest1.tar flash:orig1 |

| Note | For certain IP
                                          		  phones, such as the Cisco Unified IP Phone 7911, 7941, 7961, 7970, and 7971,
                                          		  the firmware consists of multiple files including JAR and tone files. All of
                                          		  the firmware files must be downloaded to the TFTP server before they can be
                                          		  downloaded to the phone. For a list of files in each firmware version, see the
                                          		  appropriate Cisco Unified CME Supported
                                             			 Firmware, Platforms, Memory, and Voice Products . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | tftp-server device : firmware-file Example: Router(config)# tftp-server flash:P00307020300.loads Router(config)# tftp-server flash:P00307020300.sb2 Router(config)# tftp-server flash:P00307020300.sbn Router(config)# tftp-server flash:P00307020300.bin | (Optional)
                                             				Creates TFTP bindings to permit IP phones served by the Cisco Unified CME
                                             				router to access the specified file. A
                                                   					 separate tftp-server command is required for each phone type. Required
                                                   					 for Cisco Unified CME 7.0/4.3 and earlier versions. Cisco Unified CME 7.0(1) and later versions: Required only if
                                                   					 the location for cnf files is not flash or
                                                   					 slot 0. Use the complete filename, including the file suffix, for phone
                                                   					 firmware versions later than version 8-2-2 for all phone types. |
| Step 4 | telephony-service Example: Router(config)# telephony service | Enters
                                             				telephony-service configuration mode. |
| Step 5 | load phone-type
                                                				  firmware-file Example: Router(config-telephony)# load 7960-7940 P00307020300 | Associates a
                                             				phone type with a phone firmware file. A separate load command is required for each IP phone type. firmware-file —Filenames are case-sensitive. In
                                                   					 Cisco Unified CME 7.0/4.3 and earlier versions, do not use the file suffix
                                                   					 (.bin, .sbin, .loads) for any phone type except the Cisco ATA and Cisco Unified
                                                   					 IP Phone 7905 and 7912. In
                                                   					 Cisco Unified CME 7.0(1) and later versions, you must use the complete
                                                   					 filename, including the file suffix, for phone firmware versions later than
                                                   					 version 8-2-2 for all phone types. |
| Step 6 | create cnf-files Example: Router(config-telephony)# create cnf-files | Builds XML
                                             				configuration files required for SCCP phones. |
| Step 7 | end Example: Router(config-telephony)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Cisco Unified IP Phone 7905G, Cisco Unified IP Phone 7912G, and Cisco ATA—Signed load starts from SIP v1.1. After you upgrade
                                                   the firmware to a signed load, you cannot downgrade the firmware to an unsigned load. Cisco Unified IP Phone 7940G and Cisco Unified IP Phone 7960G—Signed load starts from SIP v5.x. Once you upgrade the firmware
                                                   to a signed load, you cannot downgrade the firmware to an unsigned load. The procedures for upgrading phone firmware files for SIP phones is the same for all Cisco Unified IP phones. For other limits
                                                   on firmware upgrade between versions, see Cisco 7940 and 7960 IP Phones Firmware Upgrade Matrix . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set parameters for all supported SIP phones in Cisco Unified CME. |
| Step 4 | mode cme Example: Router(config-register-global)# mode cme | Enables mode for provisioning SIP phones in Cisco Unified CME. |
| Step 5 | load phone-type
                                                				  firmware-file Example: Router(config-register-global)# load 7960-7940 P0S3-06-0-00 | Associates a
                                             				phone type with a phone firmware file. A separate load command is required for each IP phone type. firmware-file —Filename to be associated with the specified Cisco Unified IP phone type. Do not use the .sbin or .loads file extension except for Cisco Unified IP Phone 7905 and 7912. |
| Step 6 | upgrade Example: Router(config-register-global)# upgrade | Generates a
                                             				file with the universal application loader image for upgrading phone firmware
                                             				and performs the TFTP server alias binding. |
| Step 7 | Repeat Step 5
                                          			 and Step 6. Example: Router(config-register-global)# load 7960-7940 P0S3-07-4-00 Router(config-register-global)# upgrade | (Optional)
                                             				Repeat for each version required in multistep upgrade sequences only. |
| Step 8 | file text Example: Router(config-register-global)# file text | (Optional) Generates ASCII text files for Cisco Unified IP Phone 7905s and 7905Gs, Cisco Unified IP Phone 7912s and 7912Gs,
                                             Cisco ATA-186, or Cisco ATA-188. Default—System generates binary files to save disk space. |
| Step 9 | create profile Example: Router(config-register-global)# create profile | Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command. |
| Step 10 | exit Example: Router(config-register-global)# exit | Exits from the
                                             				current command mode to the next highest mode in the configuration mode
                                             				hierarchy. |
| Step 11 | voice register
                                                				  pool pool-tag Example: Router(config)# voice register pool 1 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones. pool-tag —Unique sequence number of the SIP phone to be configured. Range is 1 to 100 or the upper limit is as defined by max-pool command. |
| Step 12 | reset Example: Router(config-register-pool)# reset | Performs a
                                             				complete reboot of the single SIP phone specified with the voice register pool command and contacts the DHCP server and the TFTP
                                             				server for updated information. |
| Step 13 | exit Example: Router(config-register-pool)# exit | Exits from
                                             				the current command mode to the next highest mode in the configuration mode
                                             				hierarchy. |
| Step 14 | voice register
                                                				  global Example: Router(config)# voice register global | Enters voice register global configuration mode to set parameters for all supported SIP phones in Cisco Unified CME. |
| Step 15 | no upgrade Example: Router(config-register-global)# no upgrade | Return to the default for the upgrade command. |
| Step 16 | end Example: Router(config-register-global)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | If codec
                                          		  values for the dial peers of a connection do not match, the call fails. The
                                          		  default codec for the POTS dial peer for an SCCP phone is G.711 and the default
                                          		  codec for a VoIP dial peer for a SIP phone is G.729. If neither the SCCP phone
                                          		  nor the SIP phone in Cisco Unified CME has been specifically configured to
                                          		  change the codec, calls between the two IP phones on the same router will
                                          		  produce a busy signal caused by the mismatched default codecs. To avoid codec
                                          		  mismatch, specify the codec for IP phones in Cisco Unified CME. For
                                          		  configuration information, see Configure Individual IP Phones for Key System on SCCP Phone . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | no ephone ephone-tag Example: Router (config)# no ephone 23 | (Optional)
                                             				Disables the ephone and removes the ephone configuration. Required
                                                   					 only if the Cisco Unified IP phone to be configured is already connected to
                                                   					 Cisco Unified CME and is using SCCP protocol. ephone-tag —Particular IP phone to which this
                                                   					 configuration change will apply. |
| Step 4 | exit Example: Router(config-ephone)# exit | (Optional)
                                             				Exits from the current command mode to the next highest mode in the
                                             				configuration mode hierarchy. Required
                                                   					 only if you performed the previous step. |
| Step 5 | no ephone-dn dn-tag | (Optional)
                                             				Disables the ephone-dn and removes the ephone-dn configuration. Required
                                                   					 only if this directory number is not now nor will be associated to any SCCP
                                                   					 phone line, intercom line, paging line, voice-mail port, or message-waiting
                                                   					 indicator (MWI) connected to Cisco Unified CME. dn-tag —Particular configuration to which this
                                                   					 change will apply. |
| Step 6 | exit Example: Router(config-ephone-dn)# exit | (Optional)
                                             				Exits from the current command mode to the next highest mode in the
                                             				configuration mode hierarchy. Required
                                                   					 only if you performed the previous step. |
| Step 7 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 8 | mode cme Example: Router(config-register-global)# mode cme | Enables mode
                                             				for provisioning SIP phones in Cisco Unified CME. |
| Step 9 | load phone-type
                                                				  firmware-file Example: Router(config-register-global)# load 7960-7940 P0S3-06-3-00 | Associates a
                                             				phone type with a phone firmware file. A separate load command is required for each IP phone type. |
| Step 10 | upgrade Example: Router(config-register-global)# upgrade | Generates a
                                             				file with the universal application loader image for upgrading phone firmware
                                             				and performs the TFTP server alias binding. |
| Step 11 | Repeat Step
                                          			 9 and Step 10. Example: Router(config-register-global)# load 7960-7940 P0S3-07-4-00 Router(config-register-global)# upgrade | (Optional)
                                             				Repeat for each version required in multistep upgrade sequences only. |
| Step 12 | create
                                                				  profile Example: Router(config-register-global)# create profile | Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command. |
| Step 13 | file text Example: Router(config-register-global)# file text | (Optional)
                                             				Generates ASCII text files for Cisco Unified IP Phones 7905 and 7905G,
                                             				Cisco Unified IP Phone 7912 and Cisco Unified IP  Phone 7912G, Cisco ATA-186,
                                             				or Cisco ATA-188. Default—System generates binary files to save disk space. |
| Step 14 | end Example: Router(config-register-global)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | If codec values
                                             			 for the dial peers of a connection do not match, the call fails. The default
                                             			 codec for the POTS dial peer for an SCCP phone is G.711 and the default codec
                                             			 for a VoIP dial peer for a SIP phone is G.729. If neither the SCCP phone nor
                                             			 the SIP phone in Cisco Unified CME has been specifically configured to change
                                             			 the codec, calls between the two IP phones on the same router will produce a
                                             			 busy signal caused by the mismatched default codecs. To avoid codec mismatch,
                                             			 specify the codec for SIP and SCCP phones in Cisco Unified CME. For more
                                             			 information, see Configure Phones for a PBX System . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | no voice register
                                                   				  pool pool-tag Example: Router(config)# no voice register pool 1 | Disables voice
                                                				register pool and removes the voice pool configuration. pool-tag —Unique sequence number for a particular
                                                      					 SIP phone to which this configuration applies. |
| Step 4 | end Example: Router(config-register-pool)# end | Exits from the
                                                				current command mode to the next highest mode in the configuration mode
                                                				hierarchy. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone dn 1 | Enters
                                                				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                                				dual-line status. dn-tag —Unique sequence number that identifies this ephone-dn during configuration tasks. The maximum number of ephone-dns in Cisco
                                                      Unified CME is version and platform specific. Type ? to display range. |
| Step 4 | exit Example: Router(config-ephone-dn)# exit | Exits from the
                                                				current command mode to the next highest mode in the configuration mode
                                                				hierarchy. |
| Step 5 | tftp-server device : firmware-file Example: Router(config)# tftp-server flash:P00307020300.loads Router(config)# tftp-server flash:P00307020300.sb2 Router(config)# tftp-server flash:P00307020300.sbn Router(config)# tftp-server flash:P00307020300.bin | (Optional)
                                                				Creates TFTP bindings to permit IP phones served by the Cisco Unified CME
                                                				router to access the specified file. A separate tftp-server command is required for each phone type. Required
                                                      					 for Cisco Unified CME 7.0/4.3 and earlier versions. Cisco Unified CME 7.0(1) and later versions: Required only if
                                                      					 the location for cnf files is not flash or slot 0. Use the complete filename, including the
                                                      					 file suffix, for phone firmware versions later than version 8-2-2 for all phone
                                                      					 types. |
| Step 6 | telephony-service Example: Router(config)# telephony service | Enters
                                                				telephony-service configuration mode. |
| Step 7 | load phone-type firmware-file Example: Router(config-telephony)# load 7960-7940 P00307020300 | Associates a
                                                				phone type with a phone firmware file. A separate load command is required for each IP phone type. firmware-file —Filename is case-sensitive. Cisco Unified CME 7.0/4.3 and earlier versions: Do not use the .sbin or .loads file extension except for Cisco Unified IP
                                                      Phone 7905 and 7912. Cisco Unified CME 7.0(1) and later versions: Use the complete filename, including the file suffix, for phone firmware versions
                                                      later than version 8-2-2 for all phone types. |
| Step 8 | create cnf-files Example: Router(config-telephony)# create cnf-files | Builds XML
                                                				configuration files required for SCCP phones. |
| Step 9 | end Example: Router(config-telephony)# end | Exits to
                                                				privileged EXEC mode. |

| Step 1 | show flash: Use this
                                             				command to learn the filenames associated with that phone firmware Router# show flash: 31      128996 Sep 19 2005 12:19:02 -07:00 P00307020300.bin 32         461 Sep 19 2005 12:19:02 -07:00 P00307020300.loads 33      681290 Sep 19 2005 12:19:04 -07:00 P00307020300.sb2 34      129400 Sep 19 2005 12:19:04 -07:00 P00307020300.sbn |
|---|---|
| Step 2 | show ephone phone-load Use this
                                             				command to verify which phone firmware is installed on a particular ephone. The
                                             				DeviceName includes the MAC address for the IP phone. Router# show ephone phone-load DeviceName        CurrentPhoneload       PreviousPhoneload      LastReset ===================================================================== SEP000A8A2C8C6E   7.3(3.02)                                     Initialized |