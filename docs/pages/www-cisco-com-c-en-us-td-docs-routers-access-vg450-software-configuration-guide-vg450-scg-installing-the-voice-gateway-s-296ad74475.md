---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg450-software-configuration-guide-vg450-scg-installing-the-voice-gateway-s-296ad74475
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg450/software/configuration/guide/vg450-scg/installing-the-voice-gateway-software.html
retrieved_at: 2026-08-22T01:15:05.449264+00:00
---

Cisco VG450 Voice Gateway Software Configuration Guide

# Cisco VG450 Voice Gateway Software Configuration Guide

Updated: April 22, 2022

Chapter: Installing the Software Using Install Commands

## Chapter: Installing the Software Using Install Commands

# Installing the Software Using Install Commands

## Installing the Software Using install Commands

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

See the following examples:

```
Device#install add file bootflash:vg400-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.bin activate commit
```

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

See the following examples:

```
Device#install add file bootflash:vg400-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.bin
```

```
Device#install add file bootflash:vg410-universalk9.BLD_V1712_THROTTLE_LATEST_20230828_043130_V17_12_1_1.SSA.bin
```

Copies the software install package from a remote location (through FTP, HTTP, HTTPs, or TFTP) to the platform, and extracts
                                             the individual components of the .package file into subpackages and packages.conf files.

Step 3

show install summary

#### Example:

```
Device#show install summary
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
Device#install abort
```

(Optional) Terminates the software install activation and returns the platform to the last committed version.

Use this command only when the image is in activated state and not when the image is in committed state.

Step 6

install commit

#### Example:

```
Device#install commit
```

Commits the new package installation and makes the changes persistent over reloads.

Step 7

install rollback to committed

#### Example:

```
Device#install rollback to committed
```

(Optional) Rolls back the platform to the last committed state.

Step 8

install remove { file filesystem: filename | inactive }

#### Example:

```
Device#install remove inactive
```

(Optional) Deletes the software installation files.

file : Deletes a specific file.

inactive : Deletes all the unused and inactive installation files.

Step 9

show install summary

#### Example:

```
Device#show install summary
```

(Optional) Displays information about the current state of the system. The output of this command varies according to the install commands run prior to this command.

Step 10

exit

#### Example:

```
Device#exit
```

Exits privileged EXEC mode and returns to the user EXEC mode.

### Upgrading in Install Mode

Use either the one-step installation or the three-step installation to upgrade the platform in install mode.

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

## Configuration Examples for Installing the Software Using install Commands

## Examples

The following is an example of the one-step installation or converting from bundle mode to install mode:

```
install-vg400# install add file bootflash:vg400-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.bin activate commit

*May 11 23:45:54.588: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install add_activate_commit bootflash:vg400-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.bininstall_add_activate_commit: START Wed May 11 23:45:54 UTC 2022
install_add: Adding IMG
--- Starting initial file syncing ---
Copying bootflash:vg400-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.bin from  R0 to  R0
Info: Finished copying to the selected 
Finished initial file syncing

--- Starting Add ---
Performing Add on all members
 [1] Finished Add package(s) on  R0
Checking status of Add on [R0]
Add: Passed on [R0]
Finished Add

Image added. Version: 17.09.01.0.5

install_activate: Activating IMG
Following packages shall be activated:
/bootflash/vg400-firmware_sm_dsp_sp2700.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.pkg
/bootflash/vg400-mono-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.pkg
/bootflash/vg400-rpboot.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.pkg

This operation may require a reload of the system. Do you want to proceed? [y/n]y

--- Starting Activate ---
Performing Activate on all members
 [1] Activate package(s) on  R0

*May 11 23:47:07.393: %INSTALL-5-INSTALL_AUTO_ABORT_TIMER_PROGRESS: R0/0: rollback_timer: Install auto abort timer will expire in 7200 seconds [1] Finished Activate on  R0
Checking status of Activate on [R0]
Activate: Passed on [R0]
Finished Activate

--- Starting Commit ---
Performing Commit on all members
 [1] Commit package(s) on  R0
 [1] Finished Commit on  R0
Checking status of Commit on [R0]
Commit: Passed on [R0]
Finished Commit operation

SUCCESS: install_add_activate_commit Wed May 11 23:47:53 UTC 2022

install-vg400#
*May 11 23:47:53.019: %INSTALL-5-INSTALL_COMPLETED_INFO: R0/0: install_mgr: Completed install add_activate_commitMay 11 23:4350: %PMAN-5-EXITACTION: R0/0: pvp: Process manager is exiting: reload action requested

Initializing Hardware ...

   :
Press RETURN to get started!
```

## Examples

The following is an example of the three-step installation:

```
install-vg400# install add bootflash:vg400-universalk9_npe.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bin

*May 12 00:11:54.785: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install add bootflash:vg400-universalk9_npe.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bininstall_add: START Thu May 12 00:11:54 UTC 2022
install_add: Adding IMG
--- Starting initial file syncing ---
Copying bootflash:vg400-universalk9_npe.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bin from  R0 to  R0
Info: Finished copying to the selected 
Finished initial file syncing

--- Starting Add ---
Performing Add on all members
 [1] Finished Add package(s) on  R0
Checking status of Add on [R0]
Add: Passed on [R0]
Finished Add

Image added. Version: 17.09.01.0.158205

SUCCESS: install_add /bootflash/vg400-universalk9_npe.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bin Thu May 12 00:12:26 UTC 2022

install-vg400#
*May 12 00:12:26.874: %INSTALL-5-INSTALL_COMPLETED_INFO: R0/0: install_mgr: Completed install add bootflash:/vg400-universalk9_npe.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bin
install-vg400#

install-vg400# install activate

*May 12 00:14:37.594: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install activate NONEinstall_activate: START Thu May 12 00:14:37 UTC 2022
install_activate: Activating IMG
Following packages shall be activated:
/bootflash/vg400-firmware_sm_dsp_sp2700.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.pkg
/bootflash/vg400-mono-universalk9_npe.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.pkg
/bootflash/vg400-rpboot.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.pkg

This operation may require a reload of the system. Do you want to proceed? [y/n]y

--- Starting Activate ---
Performing Activate on all members

*May 12 00:18:06.168: %INSTALL-5-INSTALL_AUTO_ABORT_TIMER_PROGRESS: R0/0: rollback_timer: Install auto abort timer will expire in 7200 seconds [1] Activate package(s) on  R0
 [1] Finished Activate on  R0
Checking status of Activate on [R0]
Activate: Passed on [R0]
Finished Activate

SUCCESS: install_activate Thu May 12 00:18:27 UTC 2022

install-vg400#
*May 12 00:18:27.511: %INSTALL-5-INSTALL_COMPLETED_INFO: R0/0: install_mgr: Completed install activateMay 12 00:18:36.881: %PMAN-5-EXITACTION: R0/0: pvp: Process manager is exiting: reload action requested

Initializing Hardware ...
     :
     :
     
Press RETURN to get started!

install-vg400>

install-vg400# install commit

*May 12 01:20:23.889: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install commitinstall_commit: START Thu May 12 01:20:23 UTC 2022
--- Starting Commit ---
Performing Commit on all members
 [1] Commit packages(s) on  R0
 [1] Finished Commit packages(s) on  R0
Checking status of Commit on [R0]
Commit: Passed on [R0]
Finished Commit operation

SUCCESS: install_commit Thu May 12 01:20:31 UTC 2022

install-vg400#
*May 12 01:20:31.351: %INSTALL-5-INSTALL_COMPLETED_INFO: R0/0: install_mgr: Completed install commit
```

## Examples

The following is an example of downgrading in install mode:

```
install-vg400# install add file bootflash:vg400-universalk9.17.08.01a.SPA.bin activate commit      

*May 12 02:13:24.633: %INSTALL-5-INSTALL_START_INFO: R0/0: install_mgr: Started install add_activate_commit bootflash:vg400-universalk9.17.08.01a.SPA.bininstall_add_activate_commit: START Thu May 12 02:13:24 UTC 2022
install_add: Adding IMG
--- Starting initial file syncing ---
Copying bootflash:vg400-universalk9.17.08.01a.SPA.bin from  R0 to  R0
Info: Finished copying to the selected 
Finished initial file syncing

--- Starting Add ---
Performing Add on all members
 [1] Finished Add package(s) on  R0
Checking status of Add on [R0]
Add: Passed on [R0]
Finished Add

Image added. Version: 17.08.01.0.1526

install_activate: Activating IMG
Following packages shall be activated:
/bootflash/vg400-firmware_sm_dsp_sp2700.17.08.01a.SPA.pkg
/bootflash/vg400-mono-universalk9.17.08.01a.SPA.pkg
/bootflash/vg400-rpboot.17.08.01a.SPA.pkg

This operation may require a reload of the system. Do you want to proceed? [y/n]y

--- Starting Activate ---
Performing Activate on all members
 [1] Activate package(s) on  R0

*May 12 02:17:10.699: %INSTALL-5-INSTALL_AUTO_ABORT_TIMER_PROGRESS: R0/0: rollback_timer: Install auto abort timer will expire in 7200 seconds [1] Finished Activate on  R0
Checking status of Activate on [R0]
Activate: Passed on [R0]
Finished Activate

--- Starting Commit ---
Performing Commit on all members
 [1] Commit package(s) on  R0
 [1] Finished Commit on  R0
Checking status of Commit on [R0]
Commit: Passed on [R0]
Finished Commit operation

SUCCESS: install_add_activate_commit Thu May 12 02:17:55 UTC 2022

install-vg400#
*May 12 02:17:55.312: %INSTALL-5-INSTALL_COMPLETED_INFO: R0/0: install_mgr: Completed install add_activate_commitMay 12 02:18:08.796: %PMAN-5-EXITACTION: R0/0: pvp: Process manager is exiting: reload action requested

Initializing Hardware ...
     :
     :
Press RETURN to get started!

install-vg400# show version
Cisco IOS XE Software, Version 17.08.01a
Cisco IOS Software [Cupertino], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.8.1a, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2022 by Cisco Systems, Inc.
Compiled Wed 20-Apr-22 13:16 by mcpre

Cisco IOS-XE software, Copyright (c) 2005-2022 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.

ROM: 16.12(2r)

install-vg400 uptime is 1 minute
Uptime for this control processor is 4 minutes
System returned to ROM by Install 
System image file is "bootflash:packages.conf"
Last reload reason: Install 

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
Suite                 Suite Current         Type           Suite Next reboot     
--------------------------------------------------------------------------------

Technology Package License Information: 

-----------------------------------------------------------------
Technology    Technology-package           Technology-package
              Current       Type           Next reboot  
------------------------------------------------------------------
uck9             uck9             Smart License    uck9
securityk9       None             Smart License    None
ipbase           ipbasek9         Smart License    ipbasek9

The current throughput level is 35000 kbps 

Smart Licensing Status: Smart Licensing Using Policy

cisco VG400-8FXS (1RU) processor with 1654554K/3071K bytes of memory.
Processor board ID FGL2517L2XS
Router operating mode: Autonomous
2 Gigabit Ethernet interfaces
8 Voice FXS interfaces
32768K bytes of non-volatile configuration memory.
4194304K bytes of physical memory.
6598655K bytes of flash memory at bootflash:.

Configuration register is 0x2102

install-vg400#
```

## Examples

The following is an example of terminating a software installation:

```
install-vg400# install abort
install_abort: START Tue May 03 18:31:20 UTC 2022

This operation may require a reload of the system. Do you want to proceed? [y/n]y

--- Starting Abort ---
Performing Abort on all members
 [1] Abort packages(s) on  R0
Checking status of Abort on [R0]
Abort: Passed on [R0]
Finished Abort operation

SUCCESS: install_abort Tue May 03 18:32:43 UTC 2022
install-vg400#May  3 18:32:48.735: %PMAN-5-EXITACTION: R0/0: pvp: Process manager is exiting: reload action requested

Initializing Hardware ...
  :
  :
  Press RETURN to get started!

install-vg400>
```

## Examples

The following are sample outputs for show commands:

```
install-vg400# show install log
[0|install_op_boot]: START Thu May 12 06:22:15 Universal 2022
[0|install_op_boot]: END SUCCESS  Thu May 12 06:22:17 Universal 2022
```

```
install-vg400# show install summary
[ R0 ] Installed Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
IMG   C    17.09.01.0.5

--------------------------------------------------------------------------------
Auto abort timer: inactive
--------------------------------------------------------------------------------
```

```
install-vg400# show install package bootflash:vg400-universalk9.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bin
  Package: vg400-universalk9.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bin
    Size: 648938943
    Timestamp:
  Canonical path: /bootflash/vg400-universalk9.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.bin

    Raw disk-file SHA1sum:
      80700b261910c44785f46cac327b3aa81ed42edb
  Header size:     1152 bytes
  Package type:    30000
  Package flags:   0
  Header version:  3

  Internal package information:
    Name: rp_super
    BuildTime: 2022-04-26_20.04
    ReleaseDate: 2022-04-27_02.02
    BootArchitecture: i686
    RouteProcessor: goldbeach
    Platform: VG400
    User: mcpre
    PackageName: universalk9
    Build: BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6
    CardTypes:

  Package is bootable from media and tftp.
  Package contents:

  Package: vg400-mono-universalk9.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.pkg
    Size: 606901316
    Timestamp:

    Raw disk-file SHA1sum:
      53642fa806fa46a262aa247118272e49b48f14c0
    Header size:     1092 bytes
    Package type:    30000
    Package flags:   0
    Header version:  3

    Internal package information:
      Name: mono
      BuildTime: 2022-04-26_20.04
      ReleaseDate: 2022-04-27_02.02
      BootArchitecture: i686
      RouteProcessor: goldbeach
      Platform: VG400
      User: mcpre
      PackageName: mono-universalk9
      Build: BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6
      CardTypes:

    Package is bootable from media and tftp.
    Package contents:

  Package: vg400-firmware_sm_dsp_sp2700.BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6.SSA.pkg
    Size: 2094140
    Timestamp:

    Raw disk-file SHA1sum:
      3cc7413e84187ee831a8b92fde7516ccff8f68b2
    Header size:     1084 bytes
    Package type:    40000
    Package flags:   0
    Header version:  3

    Internal package information:
      Name: firmware_sm_dsp_sp2700
      BuildTime: 2022-04-26_20.04
      ReleaseDate: 2022-04-27_02.02
      BootArchitecture: none
      RouteProcessor: goldbeach
      Platform: VG400
      User: mcpre
      PackageName: firmware_sm_dsp_sp2700
      Build: BLD_POLARIS_DEV_LATEST_20220427_001035_V17_9_0_6
      CardTypes:

    Package is not bootable.
```

```
install-vg400# show install active
[ R0 ] Active Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
IMG   C    17.09.01.0.5

--------------------------------------------------------------------------------
Auto abort timer: inactive
--------------------------------------------------------------------------------
```

```
install-vg400# show install inactive
[ R0 ] Inactive Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
No Inactive Packages
```

```
install-vg400# show install committed
[ R0 ] Committed Package(s) Information:
State (St): I - Inactive, U - Activated & Uncommitted,
            C - Activated & Committed, D - Deactivated & Uncommitted
--------------------------------------------------------------------------------
Type  St   Filename/Version
--------------------------------------------------------------------------------
IMG   C    17.09.01.0.5

--------------------------------------------------------------------------------
Auto abort timer: inactive
--------------------------------------------------------------------------------
```

```
install-vg400# show install uncommitted
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
| Step 2 | install add file location: filename [ activate commit ] Example: See the following examples: VG400 : Device#install add file bootflash:vg400-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.bin activate commit VG410 : Device# install add file bootflash:vg4x0-universalk9.17.12.01a.SPA.bin activate commit | Copies the software install package from a local or remote location (through FTP, HTTP, HTTPs, or TFTP) to the platform and
                                             extracts the individual components of the .package file into subpackages and packages.conf files. It also performs a validation
                                             and compatibility check for the platform and image versions, activates the package, and commits the package to make it persistent
                                             across reloads. The platform reloads after this command is run. |
| Step 3 | exit Example: Device# exit | Exits privileged EXEC mode and returns to user EXEC mode. |

| Note | All the CLI actions (for example, add, activate, and so on) are executed. The configuration save prompt will appear if an unsaved configuration is detected. The reload prompt will appear after the install activate step in this workflow. Use the prompt-level none keyword to automatically ignore the confirmation prompts. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device>enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | install add file location: filename Example: See the following examples: VG400 : Device#install add file bootflash:vg400-universalk9.BLD_V179_THROTTLE_LATEST_20220428_010838_V17_9_0_23.SSA.bin VG410 : Device#install add file bootflash:vg410-universalk9.BLD_V1712_THROTTLE_LATEST_20230828_043130_V17_12_1_1.SSA.bin | Copies the software install package from a remote location (through FTP, HTTP, HTTPs, or TFTP) to the platform, and extracts
                                             the individual components of the .package file into subpackages and packages.conf files. |
| Step 3 | show install summary Example: Device#show install summary | (Optional) Provides an overview of the image versions and their corresponding install state. |
| Step 4 | install activate [ auto-abort-timer <time> ] Example: Device# install activate auto-abort-timer 120 | Activates the previously added package and reloads the platform. When doing a full software install, do not provide a package filename. In the three-step variant, auto-abort-timer starts automatically with the install activate command; the default for the timer is 120 minutes. If the install commit command is not run before the timer expires, the install process is automatically terminated. The platform reloads and boots
                                                   up with the last committed version. |
| Step 5 | install abort Example: Device#install abort | (Optional) Terminates the software install activation and returns the platform to the last committed version. Use this command only when the image is in activated state and not when the image is in committed state. |
| Step 6 | install commit Example: Device#install commit | Commits the new package installation and makes the changes persistent over reloads. |
| Step 7 | install rollback to committed Example: Device#install rollback to committed | (Optional) Rolls back the platform to the last committed state. |
| Step 8 | install remove { file filesystem: filename \| inactive } Example: Device#install remove inactive | (Optional) Deletes the software installation files. file : Deletes a specific file. inactive : Deletes all the unused and inactive installation files. |
| Step 9 | show install summary Example: Device#show install summary | (Optional) Displays information about the current state of the system. The output of this command varies according to the install commands run prior to this command. |
| Step 10 | exit Example: Device#exit | Exits privileged EXEC mode and returns to the user EXEC mode. |

| Note | The install rollback command succeeds only if you have not removed the previous file using the install remove inactive command. |
|---|---|