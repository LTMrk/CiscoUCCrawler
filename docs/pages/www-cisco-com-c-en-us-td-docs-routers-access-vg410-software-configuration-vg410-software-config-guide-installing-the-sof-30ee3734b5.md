---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-installing-the-sof-30ee3734b5
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/installing-the-software-using-install-commands.html
retrieved_at: 2026-08-22T01:14:18.638642+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Installing the Software Using install Commands

## Chapter: Installing the Software Using install Commands

# Installing the Software Using install Commands

From Cisco IOS XE Cupertino 17.9.1a, Cisco Voice Gateways VG400, VG420, and VG450 are shipped in install mode by default.
                        From Cisco IOS XE 17.12.1a, Cisco Voice Gateway VG410 is also shipped in the install mode. You can boot the platform, and
                        upgrade or downgrade to Cisco IOS XE software versions using a set of install commands that are detailed in the following sections.

## Restrictions for Installing the Software Using install Commands

ISSU is not covered in this feature.

Install mode requires a reboot of the system.

## Information About Installing the Software Using install Commands

From Cisco IOS XE Cupertino 17.9.1a release, for devices shipped in install mode, a set of install commands can be used for starting, upgrading and downgrading of platforms in install mode. This update is applicable to the
                           Cisco Voice Gateway 400 Series.

The following table describes the differences between Bundle mode and Install mode:

Bundle Mode

Install Mode

This mode provides a consolidated boot process, using local (hard disk, flash) or remote (TFTP) .bin image.

This mode uses the local (bootflash) packages.conf file for the boot process.

This mode uses a single .bin file.

.bin file is replaced with expanded .pkg files in this mode.

```
#boot system file < filename >
```

```
#install add file bootflash: [activate commit]
```

To upgrade in this mode, point the boot system to the new image.

To upgrade in this mode, use the install commands.

### Install Mode Process Flow

The install mode process flow comprises three commands to perform installation and upgrade of software on platforms– install add , install activate , and install commit .

The following flow chart explains the install process with install commands:

The install add command copies the software package from a local or remote location to the platform. The location can be FTP, HTTP, HTTPs,
                              or TFTP. The command extracts individual components of the .package file into subpackages and packages.conf files. It also
                              validates the file to ensure that the image file is specific to the platform on which it is being installed.

The install activate command performs the required validations and provisions the packages previously added using the install add command. It also triggers a system reload.

The install commit command confirms the packages previously activated using the install activate command, and makes the updates persistent over reloads.

The following set of install commands is available:

Command

Syntax

Purpose

install add

install add file location:filename.bin

Copies the contents of the image and the package to the software repository. File location may be local or remote. This command
                                          does the following:

Validates the file–checksum, platform compatibility checks, and so on.

Extracts individual components of the package into subpackages and packages.conf

Copies the image into the local inventory and makes it available for the next steps.

install activate

install activate

Activates the package added using the install add command.

Use the show install summary command to see which image is inactive. This image will get activated.

System reloads on executing this command. Confirm if you want to proceed with the  activation. Use this command with the prompt-level none keyword to automatically ignore any confirmation prompts.

(install activate) auto abort-timer

install activate auto-abort timer < 30-1200 >

The auto-abort timer starts automatically, with a default value of 120 minutes. If the install commit command is not executed within the time provided, the activation process is terminated, and the system returns to the last-committed
                                          state.

You can change the time value while executing the install activate command.

The install commit command stops the timer, and continues the installation process.

The install activate auto-abort timer stop command stops the timer without committing the package.

Use this command with the prompt-level none keyword to automatically ignore any confirmation prompts.

This command is valid only in the three-step install variant.

install commit

install commit

Commits the package activated using the install activate command, and makes it persistent over reloads.

Use the show install summary command to see which image is uncommitted. This image will get committed.

install abort

install abort

Terminates the installation and returns the system to the last-committed state.

This command is applicable only when the package is in activated status (uncommitted state).

If you have already committed the image using the install commit command, use the install rollback to command to return to the preferred version.

install remove

install remove {file <filename> | inactive}

Deletes inactive packages from the platform repository. Use this command to free up space.

file : Removes specified files.

inactive : Removes all the inactive files.

install rollback to

install rollback to {base | label | committed | id}

Rolls back the software set to a saved installation point or to the last-committed installation point. The following are the
                                          characteristics of this command:

Requires reload.

Is applicable only when the package is in committed state.

Use this command with the prompt-level none keyword to automatically ignore any confirmation prompts.

The following show commands are also available:

Command

Syntax

Purpose

show install log

show install log

Provides the history and details of all install operations that have been performed since the platform was booted.

show install package

show install package < filename >

Provides details about the .pkg/.bin file that is specified.

show install summary

show install summary

Provides an overview of the image versions and their corresponding install states.

show install active

show install active

Provides information about the active packages.

show install inactive

show install inactive

Provides information about the inactive packages, if any.

show install committed

show install committed

Provides information about the committed packages.

show install uncommitted

show install uncommitted

Provides information about uncommitted packages, if any.

show install rollback

show install rollback {point-id | label}

Displays the package associated with a saved installation point.

show version

show version [rp-slot] [installed [user-interface] | provisioned | running]

Displays information about the current package, along with hardware and platform information.

### Booting the Platform in Install Mode

You can install, activate, and commit a software package using a single command (one-step install) or multiple separate commands
                              (three-step install).

If the platform is working in bundle mode, the one-step install procedure must be used to initially convert the platform from
                              bundle mode to install mode. Subsequent installs and upgrades on the platform can be done with either one-step or three-step
                              variants.

### One-Step Installation or Converting from Bundle Mode to Install Mode

All the CLI actions (for example, add, activate, and so on) are executed.

The configuration save prompt will appear if an unsaved configuration is detected.

The reload prompt will appear after the second step in this workflow. Use the prompt-level none keyword to automatically ignore the confirmation prompts.

If the prompt-level is set to None, and there is an unsaved configuration, the install fails. You must save the configuration
                                                   before reissuing the command.

Use the one-step install procedure described below to convert a platform running in bundle boot mode to install mode. After
                                 the command is executed, the platform reboots in install boot mode.

Later, the one-step install procedure can also be used to upgrade the platform.

This procedure uses the install add file activate commit command in privileged EXEC mode to install a software package, and to upgrade the platform to a new version.

### SUMMARY STEPS

- enable

- install add file location: filename [ activate commit ]

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device>enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

install add file location: filename [ activate commit ]

#### Example:

```
Device# install add file bootflash:vg4x0-universalk9.17.12.01a.SPA.bin activate commit
```

Copies the software install package from a local or remote location (through FTP, HTTP, HTTPs, or TFTP) to the platform and
                                             extracts the individual components of the .package file into subpackages and packages.conf files. It also performs a validation
                                             and compatibility check for the platform and image versions, activates the package, and commits the package to make it persistent
                                             across reloads.

The platform reloads after this command is run.

Step 3

exit

#### Example:

```
Device# exit
```

Exits privileged EXEC mode and returns to user EXEC mode.

### Three-Step Installation

All the CLI actions (for example, add, activate, and so on) are executed.

The configuration save prompt will appear if an unsaved configuration is detected.

The reload prompt will appear after the install activate step in this workflow. Use the prompt-level none keyword to automatically ignore the confirmation prompts.

The three-step installation procedure can be used only after the platform is in install mode. This option provides more flexibility
                                 and control to the customer during installation.

This procedure uses individual install add , install activate , and install commit commands for installing a software package, and to upgrade the platform to a new version.

### SUMMARY STEPS

- enable

- install add file location: filename

- show install summary

- install activate [ auto-abort-timer <time> ]

- install abort

- install commit

- install rollback to committed

- install remove { file filesystem: filename | inactive }

- show install summary

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device>enable
```

Enables privileged EXEC mode. Enter your password, if prompted.

Step 2

install add file location: filename

#### Example:

```
Device# install add file bootflash:vg4x0-universalk9.17.12.01a.SPA.bin
```

Copies the software install package from a remote location (through FTP, HTTP, HTTPs, or TFTP) to the platform, and extracts
                                             the individual components of the .package file into subpackages and packages.conf files.

Step 3

show install summary

#### Example:

```
Device# show install summary
```

(Optional) Provides an overview of the image versions and their corresponding install state.

Step 4

install activate [ auto-abort-timer <time> ]

#### Example:

```
Device# install activate auto-abort-timer 120
```

Activates the previously added package and reloads the platform.

When doing a full software install, do not provide a package filename.

In the three-step variant, auto-abort-timer starts automatically with the install activate command; the default for the timer is 120 minutes. If the install commit command is not run before the timer expires, the install process is automatically terminated. The platform reloads and boots
                                                   up with the last committed version.

Step 5

install abort

#### Example:

```
Device# install abort
```

(Optional) Terminates the software install activation and returns the platform to the last committed version.

Use this command only when the image is in activated state and not when the image is in committed state.

Step 6

install commit

#### Example:

```
Device# install commit
```

Commits the new package installation and makes the changes persistent over reloads.

Step 7

install rollback to committed

#### Example:

```
Device# install rollback to committed
```

(Optional) Rolls back the platform to the last committed state.

Step 8

install remove { file filesystem: filename | inactive }

#### Example:

```
Device# install remove inactive
```

(Optional) Deletes the software installation files.

file : Deletes a specific file.

inactive : Deletes all the unused and inactive installation files.

Step 9

show install summary

#### Example:

```
Device# show install summary
```

(Optional) Displays information about the current state of the system. The output of this command varies according to the install commands run prior to this command.

Step 10

exit

#### Example:

```
Device# exit
```

Exits privileged EXEC mode and returns to the user EXEC mode.

### Upgrading to a New Cisco IOS Release

To install or upgrade to a new Cisco IOS release, see How to Update or Upgrade Cisco IOS Software .

For Cisco VG410 Voice Gateway , the vDSP container is automatically upgraded when you upgrade the Cisco IOS XE image.

### Downgrading in Install Mode

Use the install rollback command to downgrade the platform to a previous version by pointing it to the appropriate image, provided the image you are
                              downgrading to was installed in install mode.

The install rollback command reloads the platform and boots it with the previous image.

Alternatively, you can downgrade by installing the older image using the install commands.

### Terminating a Software Installation

You can terminate the activation of a software package in the following ways:

When the platform reloads after activating a new image, the auto-abort-timer is triggered (in the three-step install variant).
                                    If the timer expires before issuing the install commit command, the installation process is terminated, and the platform reloads and boots with the last committed version of the
                                    software image.

Alternatively, use the install auto-abort-timer stop command to stop this timer, without using the install commit command. The new image remains uncommitted in this process.

Using the install abort command returns the platform to the version that was running before installing the new software. Use this command before
                                    issuing the install commit command.

### Configuration Examples: Install the Software Using Install Commands

The following is an example of the one-step installation or converting from bundle mode to install mode:

```
vg410# install add file flash:vg4x0-universalk9.17.12.01a.SPA.bin
*Sep 22 16:05:26.116: %SYS-6-PRIVCFG_ENCRYPT_SUCCESS: Successfully encrypted private config file

*Sep 22 16:05:29.836: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install add bootflash:vg4x0-universalk9.17.12.01a.SPA.bin install_add: START Fri Sep 22 16:05:29 UTC 2023
install_add: Adding IMG
 [1]  R0 FAILED: Booted in bundle mode. For Bundle-to-Install mode conversion, please use one-shot CLI - install add file <> activate commit
FAILED: install_add /bootflash/vg4x0-universalk9.17.12.01a.SPA.bin Fri Sep 22 16:05:29 UTC 2023

vg410#
*Sep 22 16:05:29.841: %INSTALL-3-OPERATION_ERROR_MESSAGE: R0/0: install_mgr: Failed to install add package bootflash:/vg4x0-universalk9.17.12.01a.SPA.bin, Error: Booted in bundle mode. For Bundle-to-Install mode conversion, please use one-shot CLI - install add file <> activate commitinstall add file flash:vg4x0-univer$ file flash:vg4x0-universalk9.17.12.01a.SPA.bin activate ?          
  commit  Commit the changes to the loadpath

vg410#$ file flash:vg4x0-universalk9.17.12.01a.SPA.bin activate com        
install_add_activate_commit: START Fri Sep 22 16:06:47 UTC 2023
install_add: START Fri Sep 22 16:06:47 UTC 2023
install_add: Adding IMG
--- Starting initial file syncing ---
Copying bootflash:vg4x0-universalk9.17.12.01a.SPA.bin from  R0 to  R0
Info: Finished copying to the selected 
Finished initial file syncing

--- Starting Add ---
Performing Add on all members

*Sep 22 16:06:47.521: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install add_activate_commit bootflash:vg4x0-universalk9.17.12.01a.SPA.bin
Checking status of Add on [R0]
Add: Passed on [R0]
Image added. Version: 17.12.01a.0.118

Finished Add

install_activate: START Fri Sep 22 16:06:55 UTC 2023
install_activate: Activating IMG
Following packages shall be activated:
/bootflash/vg4x0-firmware_vg4x0_vdsp.17.12.01a.SPA.pkg
/bootflash/vg4x0-mono-universalk9.17.12.01a.SPA.pkg
/bootflash/vg4x0-rpboot.17.12.01a.SPA.pkg

This operation may require a reload of the system. Do you want to proceed? [y/n]
*Sep 22 16:06:55.053: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install activate NONEy

--- Starting Activate ---
Performing Activate on all members

 [1] Activate package(s) on  R0

*Sep 22 16:07:11.447: %INSTALL-5-INSTALL_AUTO_ABORT_TIMER_PROGRESS: R0/0: rollback_timer: Install auto abort timer will expire in 7200 seconds
Building configuration...
[OK] [1] Finished Activate on  R0
Checking status of Activate on [R0]
Activate: Passed on [R0]
Finished Activate

--- Starting Commit ---
Performing Commit on all members
 [1] Commit package(s) on  R0

*Sep 22 16:07:25.031: %SYS-6-PRIVCFG_ENCRYPT_SUCCESS: Successfully encrypted private config file [1] Finished Commit on  R0
Checking status of Commit on [R0]
Commit: Passed on [R0]
Finished Commit operation

SUCCESS: install_add_activate_commit Fri Sep 22 16:07:35 UTC 2023

vg410#
*Sep 22 16:07:35.004: %INSTALL-5-INSTALL_COMPLETED_INFO: R0/0: install_mgr: Completed install add_activate_commitS

Initializing Hardware ...

Checking for PCIe device presence...done
System integrity status: 0x610

Rom image verified correctly

System Bootstrap, Version 17.12(1r), RELEASE SOFTWARE
Copyright (c) 1994-2023 by cisco Systems, Inc.

Current image running: Boot ROM0

Last reset cause: LocalSoft
VG410-48FXS platform with 8388608 Kbytes of main memory

........
Located packages.conf
#

###############################

Package header rev 3 structure detected
IsoSize = 0
Calculating SHA-1 hash...Validate package: SHA-1 hash:
	calculated 226B404A:303E3E89:749B2335:BDB2A32C:6164E25A
	expected   226B404A:303E3E89:749B2335:BDB2A32C:6164E25A
Validate package: start secure boot validation

Secure verification of the image PASSED
Sep 22 16:09:29.919: %BOOT-5-OPMODE_LOG: R0/0: binos: System booted in AUTONOMOUS mode

              Restricted Rights Legend

Use, duplication, or disclosure by the Government is
subject to restrictions as set forth in subparagraph
(c) of the Commercial Computer Software - Restricted
Rights clause at FAR sec. 52.227-19 and subparagraph
(c) (1) (ii) of the Rights in Technical Data and Computer
Software clause at DFARS sec. 252.227-7013.

           Cisco Systems, Inc.
           170 West Tasman Drive
           San Jose, California 95134-1706

Cisco IOS Software [Dublin], vg4x0 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.12.1a, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2023 by Cisco Systems, Inc.
Compiled Sat 19-Aug-23 00:41 by mcpre

This software version supports only Smart Licensing as the software licensing mechanism.

PLEASE READ THE FOLLOWING TERMS CAREFULLY. INSTALLING THE LICENSE OR
LICENSE KEY PROVIDED FOR ANY CISCO SOFTWARE PRODUCT, PRODUCT FEATURE,
AND/OR SUBSEQUENTLY PROVIDED SOFTWARE FEATURES (COLLECTIVELY, THE
"SOFTWARE"), AND/OR USING SUCH SOFTWARE CONSTITUTES YOUR FULL
ACCEPTANCE OF THE FOLLOWING TERMS. YOU MUST NOT PROCEED FURTHER IF YOU
ARE NOT WILLING TO BE BOUND BY ALL THE TERMS SET FORTH HEREIN.

Your use of the Software is subject to the Cisco End User License Agreement
(EULA) and any relevant supplemental terms (SEULA) found at
http://www.cisco.com/c/en/us/about/legal/cloud-and-software/software-terms.html.

You hereby acknowledge and agree that certain Software and/or features are
licensed for a particular term, that the license to such Software and/or
features is valid only for the applicable term and that such Software and/or
features may be shut down or otherwise terminated by Cisco after expiration
of the applicable license term (e.g., 90-day trial period). Cisco reserves
the right to terminate any such Software feature electronically or by any
other means available. While Cisco may provide alerts, it is your sole
responsibility to monitor your usage of any such term Software feature to
ensure that your systems and networks are prepared for a shutdown of the
Software feature.

cisco VG410-48FXS (1RU) processor with 3686972K/6147K bytes of memory.
Processor board ID FGL2731LMP4
Router operating mode: Autonomous
2 Gigabit Ethernet interfaces
48 Voice FXS interfaces
32768K bytes of non-volatile configuration memory.
8388608K bytes of physical memory.
7573503K bytes of flash memory at bootflash:.

 WARNING: Command has been added to the configuration using a type 0 password. However, recommended to migrate to strong type-6 encryption
SETUP: new interface Service-Engine0/1/0 placed in "shutdown" state

 WARNING: ** NOTICE **  The H.323 protocol is no longer supported from IOS-XE release 17.6.1. Please consider using SIP for multimedia applications.

Press RETURN to get started!

*Sep 22 16:09:39.583: %CRYPTO-5-SELF_TEST_START: Crypto algorithms release (Rel5a), Entropy release (3.4.1)
       begin self-test
*Sep 22 16:09:39.841: %CRYPTO-5-SELF_TEST_END: Crypto algorithms self-test completed successfully
       All tests passed.
*Sep 22 16:09:42.115: %ISR_THROUGHPUT-6-LEVEL: Throughput level has been set to 1000000 kbps
*Sep 22 16:09:42.818: %SMART_LIC-6-AGENT_ENABLED: Smart Agent for Licensing is enabled 
*Sep 22 16:09:43.143: %SMART_LIC-6-EXPORT_CONTROLLED: Usage of export controlled features is not allowed
*Sep 22 16:09:47.210: %SPANTREE-5-EXTENDED_SYSID: Extended SysId enabled for type vlan
*Sep 22 16:09:47.342: %CRYPTO_ENGINE-5-CSDL_COMPLIANCE_ENFORCED: Cisco PSB security compliance is being enforced
*Sep 22 16:09:47.390: %CUBE-3-LICENSING:  SIP trunking (CUBE) licensing is now based on dynamic sessions counting, static license capacity configuration through 'mode border-element license capacity' would be ignored.
*Sep 22 16:09:47.404: %SIP-5-LICENSING: CUBE license reporting period has been set to the minimum value of 8 hours.
*Sep 22 16:09:47.462: %VOICE_HA-7-STATUS: CUBE HA-supported platform detected.pm_platform_init() line :3156 

*Sep 22 16:09:47.799: %LINK-3-UPDOWN: Interface EOBC0, changed state to up
*Sep 22 16:09:47.854: %LINK-3-UPDOWN: Interface Lsmpi0, changed state to up
*Sep 22 16:09:47.854: %LINEPROTO-5-UPDOWN: Line protocol on Interface LI-Null0, changed state to up
*Sep 22 16:09:47.854: %LINEPROTO-5-UPDOWN: Line protocol on Interface VoIP-Null0, changed state to up
*Sep 22 16:09:47.855: %LINK-3-UPDOWN: Interface LIIN0, changed state to up
*Sep 22 16:09:47.983: %VOICE_HA-7-STATUS: Create VOICE HA INFRA processes now....
*Sep 22 16:09:47.999: %PNP-6-PNP_DISCOVERY_STARTED: PnP Discovery started
*Sep 22 16:09:29.916: %BOOT-5-OPMODE_LOG: R0/0: binos: System booted in AUTONOMOUS mode
*Sep 22 16:09:36.826: %CMRP_PFU-6-FANASSY_INSERTED: R0/0: cmand: Fan Assembly is inserted.
*Sep 22 16:09:48.816: %LINEPROTO-5-UPDOWN: Line protocol on Interface EOBC0, changed state to up
*Sep 22 16:09:48.865: %LINEPROTO-5-UPDOWN: Line protocol on Interface Lsmpi0, changed state to up
*Sep 22 16:09:48.865: %LINEPROTO-5-UPDOWN: Line protocol on Interface LIIN0, changed state to up
*Sep 22 16:09:49.205: %ONEP_BASE-6-SS_ENABLED: ONEP: Service set Base was enabled by Default
*Sep 22 16:09:51.771: %SYS-7-NVRAM_INIT_WAIT_TIME: Waited 0 seconds for NVRAM to be available
*Sep 22 16:09:52.442: %CRYPTO_ENGINE-5-KEY_ADDITION: A key named TP-self-signed-3402504622 has been generated or imported by crypto config
*Sep 22 16:09:52.445: %SYS-6-PRIVCFG_DECRYPT_SUCCESS: Successfully apply the private config file
*Sep 22 16:09:52.512: %SYS-5-LOG_CONFIG_CHANGE: Buffer logging: level debugging, xml disabled, filtering disabled, size (50000000)
*Sep 22 16:09:52.519:
```

The following is an example of the three-step installation:

```
vg410# install add bootflash:vg4x0-universalk9.vg4x0-universalk9.17.12.01a.SPA.bin

Sep 24 07:39:28.863: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install add_activate_commit bootflash:vg4x0-universalk9.vg4x0-universalk9.17.12.01a.SPA.bin install_add_activate_commit: START Sun Sep 24 07:39:28 UTC 2023
install_add: START Sun Sep 24 07:39:28 UTC 2023
install_add: Adding IMG
--- Starting initial file syncing ---
Copying bootflash:vg4x0-universalk9.vg4x0-universalk9.17.12.01a.SPA.bin from  R0 to  R0
Info: Finished copying to the selected
Finished initial file syncing

--- Starting Add ---
Performing Add on all members
Checking status of Add on [R0]
Add: Passed on [R0]
Image added. Version: 17.12.01.0.186080

Finished Add

install_activate: START Sun Sep 24 07:40:26 UTC 2023
install_activate: Activating IMG
Following packages shall be activated:
/bootflash/vg4x0-firmware_vg4x0_vdsp.BLD_POLARIS_DEV_LATEST_20230910_172549_V17_14_0_3.SSA.pkg
/bootflash/vg4x0-mono-universalk9.BLD_POLARIS_DEV_LATEST_20230910_172549_V17_14_0_3.SSA.pkg
/bootflash/vg4x0-rpboot.BLD_POLARIS_DEV_LATEST_20230910_172549_V17_14_0_3.SSA.pkg

This operation may require a reload of the system. Do you want to proceed? [y/n]
*Sep 24 07:40:26.929: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install activate NONEy

--- Starting Activate ---
Performing Activate on all members
 [1] Activate package(s) on  R0
*Sep 24 07:40:47.197: %INSTALL-5-INSTALL_AUTO_ABORT_TIMER_PROGRESS: R0/0: rollback_timer: Install auto abort timer will expire in 7200 seconds
Building configuration...
[OK] [1] Finished Activate on  R0
Checking status of Activate on [R0]
Activate: Passed on [R0]
Finished Activate

vg410# install commit
--- Starting Commit ---
Performing Commit on all members
 [1] Commit package(s) on  R0

*Sep 24 07:41:05.121: %SYS-6-PRIVCFG_ENCRYPT_SUCCESS: Successfully encrypted private config file [1] Finished Commit on  R0
Checking status of Commit on [R0]
Commit: Passed on [R0]
Finished Commit operation

SUCCESS: install_add_activate_commit Sun Sep 24 07:41:20 UTC 2023

vg410#
*Sep 24 07:41:20.211: %INSTALL-5-INSTALL_COMPLETED_INFO: R0/0: install_mgr: Completed install add_activate_commitSep 24 07:41:34.778: %PMAN-5-EXITACTION: R0/0: pvp: Process manager is exiting: reload action requested

Initializing Hardware ...

Checking for PCIe device presence...done
System integrity status: 0x610

Rom image verified correctly

System Bootstrap, Version 17.12(1r), RELEASE SOFTWARE
Copyright (c) 1994-2023 by cisco Systems, Inc.

Current image running: Boot ROM1

Last reset cause: LocalSoft
VG410-24FXS/4FXO platform with 8388608 Kbytes of main memory

........
Located packages.conf
```

The following is an example of terminating a software installation:

```
vg410# install abort
install_abort: START Mon Sep 25 09:15:34 UTC 2023

This operation may require a reload of the system. Do you want to proceed? [y/n]y

--- Starting Abort ---
Performing Abort on all members
 [1] Abort packages(s) on  R0
Checking status of Abort on [R0]
Abort: Passed on [R0]
Finished Abort operation

SUCCESS: install_abort START Mon Sep 25 09:15:34 UTC 2023
vg410# Mon Sep 25 09:15:34: %PMAN-5-EXITACTION: R0/0: pvp: Process manager is exiting: reload action requested

Initializing Hardware ...
  :
  :
  Press RETURN to get started!

vg410>
```

The following are sample outputs for show commands:

show version

```
vg410# show version
Cisco IOS XE Software, Version 17.12.01a
Cisco IOS Software [Dublin], vg4x0 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.12.1a, RELEASE SOFTWARE (fc3)
Copyright (c) 1986-2023 by Cisco Systems, Inc.
Compiled Sun 10-Sep-23 12:48 by mcpre

Cisco IOS-XE software, Copyright (c) 2005-2023 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.

ROM: 17.12(1r)
)

VG410 uptime is 53 minutes
Uptime for this control processor is 54 minutes
System returned to ROM by Reload Command
System image file is "bootflash/vg4x0-universalk9.17.12.01a.SPA.bin"
Last reload reason: Reload Command

This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Suite License Information for Module:'esg'

--------------------------------------------------------------------------------
Suite Suite Current Type Suite Next reboot
--------------------------------------------------------------------------------

Technology Package License Information:

-----------------------------------------------------------------
Technology Technology-package Technology-package
Current Type Next reboot
------------------------------------------------------------------
uck9 uck9 Smart License uck9
securityk9 securityk9 Smart License securityk9
ipbase ipbasek9 Smart License ipbasek9

The current throughput level is unthrottled

Smart Licensing Status: Smart Licensing Using Policy

cisco VG410-24FXS/4FXO (1RU) processor with 3686896K/6147K bytes of memory.
Processor board ID FGL2731LMZY
Router operating mode: Autonomous
2 Gigabit Ethernet interfaces
4 Voice FXO interfaces
24 Voice FXS interfaces
32768K bytes of non-volatile configuration memory.
8388608K bytes of physical memory.
7573503K bytes of flash memory at bootflash:.

Configuration register is 0x0
```

```
vg410# show install log
[0|install_op_boot]: START Sun Sep 24 07:42:52 Universal 2023
[0|install_op_boot(INFO, )]: Mount IMG INI state base image
[0|install_op_boot]: END SUCCESS  Sun Sep 24 07:42:53 Universal 2023
```

```
vg410# show install summary
[ R0 ] Installed Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
IMG   C    17.12.01.0.186080

--------------------------------------------------------------------------------
Auto abort timer: inactive
--------------------------------------------------------------------------------
```

```
vg410# show install package flash:vg4x0-universalk9.17.12.01a.SPA.bin
  Package: vg4x0-universalk9.17.12.01a.SPA.bin
    Size: 658481669
    Timestamp: 
  Canonical path: /bootflash/vg4x0-universalk9.17.12.01a.SPA.bin

    Raw disk-file SHA1sum:
      9c43dfa47b2cb6591f71bbf461cde8d51291bb8a
  Header size:     1040 bytes
  Package type:    30000
  Package flags:   0
  Header version:  3

  Internal package information:
    Name: rp_super
    BuildTime: 2023-07-27_23.17
    ReleaseDate: 2023-07-28_05.52
    BootArchitecture: i686
    RouteProcessor: vg4x0
    Platform: VG4X0
    User: occp
    PackageName: universalk9
    Build: 17.12.01a
    CardTypes: 
  Package is bootable from media and tftp
```

```
vg410# show install active
[ R0 ] Active Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
IMG   C    17.12.01.0.186080

--------------------------------------------------------------------------------
Auto abort timer: inactive
--------------------------------------------------------------------------------
```

```
vg410# show install inactive
[ R0 ] Inactive Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
No Inactive Packages
```

```
vg410_B# show install committed
[ R0 ] Committed Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
IMG   C    17.12.01.0.186080

--------------------------------------------------------------------------------
Auto abort timer: inactive
--------------------------------------------------------------------------------
```

```
vg410# show install uncommitted
[ R0 ] Uncommitted Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
No Uncommitted Packages
```

## Troubleshooting Software Installation Using install Commands

Problem Troubleshooting the software installation

Solution Use the following show commands to view installation summary, logs, and software versions.

show install summary

show install log

show version

show version running

Problem Other installation issues

Solution Use the following commands to resolve installation issue:

dir < install directory >

more location: packages.conf

show tech-support install : this command automatically runs the show commands that display information specific to installation.

request platform software trace archive target bootflash < location > : this command archives all the trace logs relevant to all the processes running on the system since the last reload, and
                                    saves this information in the specified location.

| Bundle Mode | Install Mode |
|---|---|
| This mode provides a consolidated boot process, using local (hard disk, flash) or remote (TFTP) .bin image. | This mode uses the local (bootflash) packages.conf file for the boot process. |
| This mode uses a single .bin file. | .bin file is replaced with expanded .pkg files in this mode. |
| CLI: #boot system file < filename > | CLI: #install add file bootflash: [activate commit] |
| To upgrade in this mode, point the boot system to the new image. | To upgrade in this mode, use the install commands. |

| Note | Installing an update replaces any previously installed software image. At any time, only one image can be installed in a device. |
|---|---|

| Command | Syntax | Purpose |
|---|---|---|
| install add | install add file location:filename.bin | Copies the contents of the image and the package to the software repository. File location may be local or remote. This command
                                          does the following: Validates the file–checksum, platform compatibility checks, and so on. Extracts individual components of the package into subpackages and packages.conf Copies the image into the local inventory and makes it available for the next steps. |
| install activate | install activate | Activates the package added using the install add command. Use the show install summary command to see which image is inactive. This image will get activated. System reloads on executing this command. Confirm if you want to proceed with the  activation. Use this command with the prompt-level none keyword to automatically ignore any confirmation prompts. |
| (install activate) auto abort-timer | install activate auto-abort timer < 30-1200 > | The auto-abort timer starts automatically, with a default value of 120 minutes. If the install commit command is not executed within the time provided, the activation process is terminated, and the system returns to the last-committed
                                          state. You can change the time value while executing the install activate command. The install commit command stops the timer, and continues the installation process. The install activate auto-abort timer stop command stops the timer without committing the package. Use this command with the prompt-level none keyword to automatically ignore any confirmation prompts. This command is valid only in the three-step install variant. |
| install commit | install commit | Commits the package activated using the install activate command, and makes it persistent over reloads. Use the show install summary command to see which image is uncommitted. This image will get committed. |
| install abort | install abort | Terminates the installation and returns the system to the last-committed state. This command is applicable only when the package is in activated status (uncommitted state). If you have already committed the image using the install commit command, use the install rollback to command to return to the preferred version. |
| install remove | install remove {file <filename> \| inactive} | Deletes inactive packages from the platform repository. Use this command to free up space. file : Removes specified files. inactive : Removes all the inactive files. |
| install rollback to | install rollback to {base \| label \| committed \| id} | Rolls back the software set to a saved installation point or to the last-committed installation point. The following are the
                                          characteristics of this command: Requires reload. Is applicable only when the package is in committed state. Use this command with the prompt-level none keyword to automatically ignore any confirmation prompts. Note If you are performing install rollback to a previous image, the previous image must be installed in install mode. | Note | If you are performing install rollback to a previous image, the previous image must be installed in install mode. |
| Note | If you are performing install rollback to a previous image, the previous image must be installed in install mode. |

| Note | If you are performing install rollback to a previous image, the previous image must be installed in install mode. |
|---|---|

| Command | Syntax | Purpose |
|---|---|---|
| show install log | show install log | Provides the history and details of all install operations that have been performed since the platform was booted. |
| show install package | show install package < filename > | Provides details about the .pkg/.bin file that is specified. |
| show install summary | show install summary | Provides an overview of the image versions and their corresponding install states. |
| show install active | show install active | Provides information about the active packages. |
| show install inactive | show install inactive | Provides information about the inactive packages, if any. |
| show install committed | show install committed | Provides information about the committed packages. |
| show install uncommitted | show install uncommitted | Provides information about uncommitted packages, if any. |
| show install rollback | show install rollback {point-id \| label} | Displays the package associated with a saved installation point. |
| show version | show version [rp-slot] [installed [user-interface] \| provisioned \| running] | Displays information about the current package, along with hardware and platform information. |

| Note | All the CLI actions (for example, add, activate, and so on) are executed. The configuration save prompt will appear if an unsaved configuration is detected. The reload prompt will appear after the second step in this workflow. Use the prompt-level none keyword to automatically ignore the confirmation prompts. If the prompt-level is set to None, and there is an unsaved configuration, the install fails. You must save the configuration
                                                   before reissuing the command. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device>enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | install add file location: filename [ activate commit ] Example: Device# install add file bootflash:vg4x0-universalk9.17.12.01a.SPA.bin activate commit | Copies the software install package from a local or remote location (through FTP, HTTP, HTTPs, or TFTP) to the platform and
                                             extracts the individual components of the .package file into subpackages and packages.conf files. It also performs a validation
                                             and compatibility check for the platform and image versions, activates the package, and commits the package to make it persistent
                                             across reloads. The platform reloads after this command is run. |
| Step 3 | exit Example: Device# exit | Exits privileged EXEC mode and returns to user EXEC mode. |

| Note | All the CLI actions (for example, add, activate, and so on) are executed. The configuration save prompt will appear if an unsaved configuration is detected. The reload prompt will appear after the install activate step in this workflow. Use the prompt-level none keyword to automatically ignore the confirmation prompts. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device>enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | install add file location: filename Example: Device# install add file bootflash:vg4x0-universalk9.17.12.01a.SPA.bin | Copies the software install package from a remote location (through FTP, HTTP, HTTPs, or TFTP) to the platform, and extracts
                                             the individual components of the .package file into subpackages and packages.conf files. |
| Step 3 | show install summary Example: Device# show install summary | (Optional) Provides an overview of the image versions and their corresponding install state. |
| Step 4 | install activate [ auto-abort-timer <time> ] Example: Device# install activate auto-abort-timer 120 | Activates the previously added package and reloads the platform. When doing a full software install, do not provide a package filename. In the three-step variant, auto-abort-timer starts automatically with the install activate command; the default for the timer is 120 minutes. If the install commit command is not run before the timer expires, the install process is automatically terminated. The platform reloads and boots
                                                   up with the last committed version. |
| Step 5 | install abort Example: Device# install abort | (Optional) Terminates the software install activation and returns the platform to the last committed version. Use this command only when the image is in activated state and not when the image is in committed state. |
| Step 6 | install commit Example: Device# install commit | Commits the new package installation and makes the changes persistent over reloads. |
| Step 7 | install rollback to committed Example: Device# install rollback to committed | (Optional) Rolls back the platform to the last committed state. |
| Step 8 | install remove { file filesystem: filename \| inactive } Example: Device# install remove inactive | (Optional) Deletes the software installation files. file : Deletes a specific file. inactive : Deletes all the unused and inactive installation files. |
| Step 9 | show install summary Example: Device# show install summary | (Optional) Displays information about the current state of the system. The output of this command varies according to the install commands run prior to this command. |
| Step 10 | exit Example: Device# exit | Exits privileged EXEC mode and returns to the user EXEC mode. |

| Note | For Cisco VG410 Voice Gateway , the vDSP container is automatically upgraded when you upgrade the Cisco IOS XE image. |
|---|---|

| Note | The install rollback command succeeds only if you have not removed the previous file using the install remove inactive command. |
|---|---|