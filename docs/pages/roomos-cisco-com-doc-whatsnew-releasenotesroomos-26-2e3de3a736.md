---
doc_id: roomos-cisco-com-doc-whatsnew-releasenotesroomos-26-2e3de3a736
source_url: https://roomos.cisco.com/doc/WhatsNew/ReleaseNotesRoomOS_26
retrieved_at: 2026-09-01T14:45:56.725955+00:00
---

# RoomOS 26

# Release notes

D15563.03 - August 2026

## Document revision history

## Introduction to Cisco RoomOS 26

This release note describes new software features and capabilities included in RoomOS 26 for on-premises deployment . RoomOS 26 is supported by the following Cisco collaboration devices:

Note: If you attempt to upgrade an unsupported device to RoomOS 26.x.x.x, it will not damage the device, but the upgrade will fail.

The software described in this document is released to https://www.cisco.com for on-premises deployment. If you register a Cisco Room Device to Webex or another supported cloud service, you will be upgraded to the latest available RoomOS cloud version for that service. RoomOS cloud software is not supported for on-premises deployment unless you are linked to Webex Edge for Devices with Cloud Software Management enabled .

You can tell the difference between a cloud and on-premises RoomOS version by looking at the third version number. For example:

- 26.X. 1 .x = Cloud

- 26.X. X > 1 .x = On-premises

26.2. 1 .x = Cloud
26.2. 4 .x = On-premises

RoomOS 26 is based on RoomOS 11 but has major changes

This means that the first release of RoomOS 26 inherits most of the same underlying features and functionality as seen in RoomOS 11. The big difference is that RoomOS 26 comes with changes to the user interface and is only supported by newer hardware.

RoomOS 26 can be downloaded here .

## General notes and warnings for RoomOS 26

Please read this before upgrading to RoomOS 26.

Provisioning Mode "VCS" is obsolete The setting "xConfiguration Provisioning Mode: VCS" is deprecated in RoomOS 26

Tips button is removed The feature providing the Tips button has been removed and deprecated.

Several hardware products do not support RoomOS 26 and require RoomOS 11 Any device running s53200 software, such as Cisco Room Kit, Room Kit Plus, Room Kit Mini, Room 55, Room 55 Dual, Room 70 (Single and Dual), Board 55/70, Board 55S/70S/85S, and Room USB.

It is important to note that previously supported hardware combinations involving peripherals and cameras, such as Touch 10 and SpeakerTrack 60 / Precision 60 together with Cisco Room Kit Pro, Room 70 G2, Room Panorama, or Room 70 Panorama, are not supported in standard RoomOS 26. You can continue to use these setups on RoomOS 11. However, to upgrade to RoomOS 26, you need a supported peripheral combination (Cisco Room Navigator instead of Touch 10, and Cisco Quad Camera or Webex PTZ 4K instead of SpeakerTrack 60 / Precision 60). Note: SpeakerTrack 60 has limited support in Microsoft Teams Rooms (MTR) scenarios on RoomOS 26.

For more information about End of Life of Cisco RoomOS Devices, please find a detailed overview here: End of Support for RoomOS Devices

# Release summary for RoomOS 26.7

## Notes and warnings for this software release

### RoomOS 26.7

This release builds on the previous RoomOS 26 release and adds support for Cisco Board Pro 55 and 75 G3 together with quality and stability improvements for selected devices.

Current known limitations

No noteworthy limitations to mention at this time.

## RoomOS 26.7.2.2

Support for Cisco Board Pro 55 and 75 G3

Quality and stability improvements for Codec Pro G2 and Desk Pro G2

Bug fixes

- Click here for a list of resolved defects in RoomOS 26.7.2.2

# RoomOS 26.7.2.2 feature descriptions

## Support for Cisco Board Pro 55 and 75 G3

RoomOS 26 now adds support for Cisco Board Pro 55 and 75 G3. Cisco Board Pro G3 is an all-in-one video device and collaboration board designed as a complete hybrid meeting room solution for small and medium spaces. It combines a dual camera system, built-in speakers and microphones, an interactive touch screen, an AI-powered computing engine, and flexible mounting options in a premium, integrated design.

Powered by the Cisco RoomOS core operating system, Cisco Board Pro G3 supports both Cisco Rooms and Microsoft Teams Rooms experiences. It enables AI-enhanced video meetings, touch-enabled collaborative teamwork, streamlined deployment, and scalable cloud management with a single solution.

See the Cisco Board Pro G3 data sheet for more information .

## Quality and stability improvements for Codec Pro G2 and Desk Pro G2

This release includes quality and stability improvements for Codec Pro G2 and Desk Pro G2. The updates improve overall reliability and help provide a more stable meeting experience on these devices.

# Release summary for RoomOS 26.5

## Notes and warnings for this software release

### RoomOS 26.5

This release builds on the previous RoomOS 26 release and adds new device support, meeting enhancements, administration improvements, and new collaboration capabilities.

Current known limitations

No noteworthy limitations to mention at this time.

## RoomOS 26.5.2.2

# RoomOS 26.5.2.2 feature descriptions

## Digital Signage for Room Schedulers

Room schedulers can now display digital signage when they are not actively being used for booking. This allows the same signage experience available inside the room to also be shown on paired or standalone Room Navigator panels in Cisco Room Booking and Microsoft Teams Panel mode.

## Support for Cisco Desk Pro G2

RoomOS 26 now adds support for Cisco Desk Pro G2. The new device introduces a significant CPU and AI performance increase, a new camera module with both main and wide lenses, improved I/O, and a refined display with better contrast, color reproduction, and blue light filtering.

Read more about Cisco Desk Pro G2 Here

## Support for Cisco Room Kit Pro G2

RoomOS 26 now adds support for Cisco Room Kit Pro G2. Room Kit Pro G2 brings an AI-first collaboration device solution to high-impact spaces, including large conference rooms, multi-camera spaces, training rooms, boardrooms, and divisible-room deployments. With an AI room engine, intelligent camera options, an intuitive touch controller, and support for room accessories, it provides a scalable foundation for next-generation meeting workflows, high-end AV over IP room orchestration, and extensive conferencing integrations.

Read more about Cisco Room Kit Pro G2 Here

## Room Bar Pro BYOD

BYOD mode is now available for Cisco Room Bar Pro. This lets you use the device as a high-performance USB-C passthrough for laptop-hosted meetings, bringing Room Bar Pro camera and audio capabilities into third-party meeting experiences without requiring a Navigator controller.

## Improved call quality on Wi-Fi networks

This release improves call stability on Wi-Fi by preventing the device from going off-channel to collect radio measurement data during calls. That helps reduce interruptions while still preserving the wireless behavior needed for stationary collaboration devices.

## High-Performance Background Noise Removal

High-Performance Background Noise Removal uses advanced AI processing to reduce distracting background noise with greater efficiency. This improves audio clarity in demanding environments while keeping device performance high.

## Moving PTZ cameras in multicamera setups

Support for moving PTZ cameras in multicamera setups enables more flexible camera placement in larger rooms. By using physical pan, tilt, and zoom for framing, the system can deliver clearer video without relying on digital cropping and can better support cross-view room designs.

## Exclusion zone UI

The new exclusion zone UI makes it easier for administrators to define areas where people should not be detected or tracked by the camera. This helps improve framing and reduces unwanted tracking in more complex room layouts.

## Miracast sharing support on 5 GHz channels

Miracast direct sharing now supports selected 5 GHz Wi-Fi channels. Using 5 GHz can provide higher throughput, less interference, and better sharing quality in environments where the 2.4 GHz band is congested.

## 4K sharing with Miracast

Miracast now supports 4K content sharing on supported devices and displays. This provides sharper image quality and more detail when sharing high-resolution content wirelessly.

# Release summary for RoomOS 26.2

## Notes and warnings for this software release

### RoomOS 26.2

This release builds on the previous major version of RoomOS (RoomOS 11). For features released in earlier RoomOS versions, refer to the respective release notes. RoomOS 26 inherits the same core feature set as RoomOS 11 and continues that software stream with major UI and hardware support changes.

Current known limitations

No noteworthy limitations to mention at this time.

## RoomOS 26.2.2.2

# RoomOS 26.2.2.2 feature descriptions

## RoomOS 26 Visual Changes

RoomOS 26 introduces a refreshed visual identity across the user interface. The update modernizes the look and feel while preserving familiar workflows.

## Side panel design changes

The side panel has been redesigned on both Navigator and Desk/Board devices. The new design improves visual consistency and makes common controls easier to find and use.

## Meeting Zone - Improvements

Meeting Zone setup has been improved with a more flexible configuration experience. Administrators can now show or hide the Meeting Zone overlay on the room display, zoom in and out during setup, and update the room layout shape more easily.

## Grouping of whiteboard content

Whiteboarding now supports intuitive grouping behavior when objects are placed on top of each other. This makes it easier to move or delete related content as a group and improves editing efficiency on complex canvases.

## Display ultrasound signal levels in the VuMeter

The VuMeter in the web interface can now be used to inspect ultrasound signal levels in addition to regular audio levels. This is useful for diagnostics, especially when troubleshooting ultrasound sources that do not originate from the codec.

## Force Active Pen to always draw

With Active Pen Always Draw enabled, the active pen is prioritized for inking while finger-touch input is used for selection. This makes whiteboarding interactions more predictable and reduces accidental mode switching during annotation.

## Deep sleep mode for Cisco Board Pro

Cisco Board Pro introduces a new Deep Sleep standby mode focused on improved power savings. This mode is designed to reduce energy consumption when the device is idle.

## Wireless Touch Redirect for Miracast

Wireless Touch Redirect for Miracast allows users to control a Miracast sender device from the RoomOS touch display. The feature uses Wi-Fi Display UIBC (User Input Back Channel) to send touch input back to supported sender devices.

## Dynamic Camera Mode

Dynamic Camera Mode extends framing behavior to better support larger in-room groups. The feature adapts framing across one or two rows, for example one row for smaller groups and two rows for larger groups.

## DHCP sub options support for SCEP

RoomOS now supports SCEP profiles delivered through DHCP sub-options, providing the same deployment method as PhoneOS for consistent zero-touch provisioning across phones and room devices. Sub-options 11, 12, 13, and 14 are used for simple SCEP enrollment, and when 802.1X is enabled, the required Ethernet settings are applied automatically after reboot.

## Support for 21:9 aspect ratio

RoomOS now supports 21:9 output resolution in single-screen room scenarios. Application-level behavior may vary until each app fully adopts the additional display area, and mixed-screen combinations are not part of this release scope.

## Auto-Lower a raised hand

Auto-Lower a Raised Hand helps keep meeting controls accurate by reducing stale raised-hand states after participants have contributed. This improves meeting flow for hosts and participants by minimizing manual clean-up of hand status.

## Support for Greek Language and text input

RoomOS now includes support for Greek as a user interface language and for Greek text input. This improves localization support for Greek-speaking users and deployments.

## Cameras Calibration Diagnostics tool for the cinematic view

This release adds a Cameras Calibration Diagnostics tool for cinematic view scenarios. The tool helps administrators validate camera calibration behavior and troubleshoot setup issues more efficiently.

## Desk Specific ULP Model

This update introduces a Desk-specific ULP model to improve noise reduction behavior on Desk series devices. The result is cleaner audio pickup in typical desk and personal workspace conditions.

## Audio Exclusion Zone

Audio Exclusion Zone enables administrators to attenuate pickup from selected areas outside the intended meeting space. This improves clarity and privacy by reducing distracting background audio; initial availability is targeted for Ceiling Microphone Pro deployments.

# Software upgrade and downgrade

## Upgrading software on a Cisco Room Device

Before performing an upgrade or downgrade, verify product compatibility and minimum supported software for your device. Use the compatibility matrices in this document as reference.

RoomOS 26 software packages use .k4.cop.sha512 signatures. For older step-upgrade scenarios, the same package handling rules introduced in RoomOS 11 still apply:

- For upgrades using TMS, xAPI (SSH), or the device web interface, the endpoint itself must be able to unpack the .k4.cop.sha512 package.

- For very old starting points, a step upgrade to RoomOS 10.15.x or later may still be required before proceeding. Please refer to previous documentation for the respective versions.

- UCM can still be used as a bridging path because UCM handles package unpacking before distribution.

To illustrate the upgrade pattern:

Before you start, make sure you download software for the correct platform.

*** Contains the MTR module, you can upgrade using this package in order to get the option to select between RoomOS and MTR

## MTR version contained in the MTR cop file

### RoomOS 26.7

cmterm-s53300-mtr-ce26_7_2_2.k4.cop.sha512

- MTR: 1449/1.0.96.2026087210

cmterm-s53600-mtr-ce26_7_2_2.k4.cop.sha512

- MTR: 1449/1.0.96.2026087210

cmterm-s53350-mtp-ce26_7_2_2.k4.cop.sha512

- MTP: 1449/1.0.97.2025385601

### RoomOS 26.5

cmterm-s53300-mtr-ce26_5_2_2.k4.cop.sha512

- MTR: 1449/1.0.96.2026048906

cmterm-s53600-mtr-ce26_5_2_2.k4.cop.sha512

- MTR: 1449/1.0.96.2026048906

cmterm-s53350-mtp-ce26_5_2_2.k4.cop.sha512

- MTP: 1449/1.0.97.2025364207

### RoomOS 26.2

- MTR: 1449/1.0.96.2025341701

- MTP: 1449/1.0.97.2025364207

The "All products" cop file (super cop) must only be installed to a Unified CM. This package provides software to all supported video models and peripherals, so you only have to install one cop file if you have multiple products.

WARNING: Do not delete ".pkg" files that are stated to be "Not in use" on Unified CM. The devices may be pointed to a loads file that tells it what package to use for the different peripherals. UCM is not aware that the ".pkg" is in use. By deleting peripheral or device software the device will fail to upgrade or fail to upgrade its peripherals.

### Software integrity verification after download

To verify the integrity of the software image you have downloaded from cisco.com, you can calculate a SHA512 checksum and verify that it matches with the one listed on the software download page. To find the checksum, hover the mouse pointer over the software image you have downloaded.

At the bottom you find the SHA512 checksum, if you do not see the whole checksum you can expand it by pressing the "..." at the end. 
To calculate a SHA512 checksum on your local desktop please see below.

#### SHA512 checksum calculation command examples

Microsoft Windows

Open a command line window and type the following command:

```
> certutil.exe -hashfile filename.k4.cop.sha512 SHA512
```

macOS

Open a terminal window and type the following command:

```
$ shasum -a 512 filename.k4.cop.sha512
```

Linux

Open a terminal window and type the following command:

```
$ sha512sum filename.k4.cop.sha512
Or
$ shasum -a 512 filename.k4.cop.sha512
```

If the SHA512 checksum matches, there is a high level of certainty that no one has tampered with the software image or the image has not been corrupted during download.

If the SHA512 checksum does not match, we advise you to not attempt upgrading any systems with the software image. Download the software again and verify the SHA512 checksum again. If there is a constant mismatch, please open a case with the Cisco Technical Assistance Center.

Note:
You should always use the .cop file when upgrading the devices listed above. Upgrading using .pkg on these devices can leave the device unable to upgrade peripherals, and you may see software mismatch errors after upgrade. If this happens, run the upgrade again using the .cop file. Cisco releases .cop files for RoomOS 11 and later, including RoomOS 26.

Upgrade using the web interface

Access the web interface of the device on:

https://codecIP/web/software

Upload the correct software package by following the instructions on the web page. The upgrade will start, and the device will reboot with the new software.

If you are on an older software version such as RoomOS 10.1.x or below, refer to the RoomOS 10 release note for step-upgrade guidance before proceeding toward RoomOS 26.

Upgrade using UCM

Install the appropriate “xx.k4.cop.sha512” file containing the software for the device platform you wish to upgrade according to the cop installation process on UCM.

Go into the device default loads on the UCM administration page and make sure the platform has populated the correct filename.

For Cisco Room devices on s53300, the load file name should not contain any extension at all, for example:

Platform-specific packages: s53300ce26_X_X_X.pkg ( wrong ) s53300ce26_X_X_X ( correct )

All products (containing software for all supported products): ce26_X_X_X ( correct )

Upgrade using TMS

Upload the software to TMS according to the TMS instructions of software upgrade.

Note: There is a known limitation with older TMS versions. The affected versions do not accept the sha512 extension of the RoomOS software. Please upgrade to the latest TMS software version or refer to the TMS documentation for information about the minimum version you need to use.

Also note that devices may need to run RoomOS 10.15.x or above as an intermediate step for successful upgrades via TMS when starting from very old versions. Refer to documentation for the version in question.

Upgrade using the xAPI

If none of the above methods are applicable, you can use an existing HTTP server or setup a HTTP server that is reachable by the device(s) you want to upgrade.

Log into the xAPI CLI using SSH or Serial. Type the following command to initiate the upgrade:

```
xCommand SystemUnit SoftwareUpgrade URL: http(s)://yourHTTPserver/path/to/file
xCommand SystemUnit SoftwareUpgrade URL: http(s)://yourUCMserver:6970/file
xCommand SystemUnit SoftwareUpgrade URL: http(s)://yourTMSserver/public/path/to/file
```

/path/to/file is replaced with the location of the xx.k4.cop.sha512 file.

The device will download the software package and upgrade without warning. If you want the user to be warned and postpone the upgrade, add the parameter: “Forced: False” to the command as the default is “Forced: True” .

If you are upgrading to RoomOS 26 using this method from a very old starting point, make sure the device is on RoomOS 11.17.x or later as an intermediate step first.

### Downgrading

Downgrading is performed the same way as upgrading, using a software version lower than the one currently running. Not all products are compatible with all software versions. Verify the minimum supported software in the compatibility matrix before downgrading or upgrading your product.

If you plan to downgrade across major versions (for example from RoomOS 26 to RoomOS 11), verify in the target release note that your device compatibility level is supported in that version. This information can often be found in the respective version release notes.

## Software deferral policy

A software version is deferred when we find critical issues within the software. This is to prevent users from downloading and installing affected software versions. Replacement software will always be in place before a software version is deferred.

Older software versions will be deferred on a regular basis from the download section on https://www.cisco.com to avoid providing potentially vulnerable software after security fixes. As a general rule, you will be able to download the latest release and the version before it. Older software versions will be removed from cisco.com regularly. Cisco always recommends using the latest available software.

Example:

RoomOS 26.X.Y.z = Major.Minor.Patch.Buildnumber

For RoomOS versions provided by the Webex cloud, "Y" will always be 1 (26.X. 1 .z), while a RoomOS version released to cisco.com will have a number higher than 1 and increment by one for each patch release.

If, for example, RoomOS 26.1.2.x and RoomOS 26.2.2.x are released and RoomOS 26.3.2.x becomes available, RoomOS 26.1.2.x may be removed as part of the deferral policy. A minor software version is typically supported for two release cycles (6-9 months).

Cisco supports the latest minor release (for example, RoomOS 26.3.1.x) and the previous minor release (for example, RoomOS 26.2.2.x) per product as a general rule.

Exceptions are made if supported hardware or particular feature deployments are depending on a major release. Deferral of older maintenance releases still applies.

The RoomOS major version will follow the year (RoomOS 26 equals Year 20 26 ) and will change each year going forward.

## Deferred RoomOS 26 software

## Open and resolved caveats in RoomOS 26

### Using the Bug Search Tool

You can use the Bug Search Tool to find information about caveats (bugs) for this release, including a description of the problems and available workarounds. The Bug Search Tool lists both open and resolved caveats. No subset of open or resolved bugs will be listed in the release notes unless deemed relevant for a particular software version.

A pre-defined link will provide the correct list of all open or resolved bugs. Please note that the "Series/Model" listed in the pre-defined search is universal and will list all relevant bugs relating to all products that runs RoomOS Software.

Please refer to the release summary for a link to open and resolved bugs under the specific release.

To use the Bug Search Tool, follow these steps:

- Step 1 Access the Bug Search Tool by navigating to https://bst.cloudapps.cisco.com/bugsearch/

- Step 2 Log in with your Cisco.com user ID and password

- Step 3 To look for information about a specific problem, enter the bug ID number in the ‘Search for bug ID’ field, then click ‘Go’

## Known limitations and advisories for RoomOS 26

### Resource consumption

Extended Logging

Extended logging is a troubleshooting feature that consumes significant system resources when enabled. In production environments, this can impact call quality and, in rare cases, lead to instability. Enable this only for short troubleshooting windows, for example when reproducing issues together with Cisco TAC.

Note on IP Filtering Capabilities

Room devices support IP filtering for SSH, HTTP, and HTTPS to improve administrative access control. Other services, such as SIP and H.323, do not support IP filtering. We recommend deploying these services in secure network environments and using external security controls as needed to reduce exposure to denial-of-service (DoS) attacks.

Network Congestion

Anything that degrades network performance can affect voice and video quality and, in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

- Administrative tasks such as an internal port scan or security scan

- Attacks that occur on your network, such as a denial-of-service attack

To reduce or eliminate any adverse effects to conferences, schedule any administrative network tasks during a time when the Cisco Room Device is not being used, or exclude the Cisco Room systems from the testing.

### Wi-Fi connection

Due to compliance regulations, 802.11d must be enabled on access points for the product to operate properly within 5725 MHz - 5875 MHz. Wi-Fi can be used as a flexible option, but Ethernet is always preferred for high performance.

WPA-EAP There is currently no diagnostic message for expired certificates

CA Certificates CA certificates must be uploaded per endpoint. You can use xAPI to perform manual or automated mass distribution of certificates to devices. Note that the endpoint must be connected to a wired or WPA2-PSK wireless network to upload a certificate before attempting to connect to a WPA-EAP-enabled network that requires a CA certificate.

Web Engine

Web Engine supports 1080p and above. Full-screen web views at 720p are not supported.

Network-paired Cisco Room Navigator is not supported when the video system is connected through Wi-Fi Even if this connectivity works, operational issues may occur if Wi-Fi connectivity is lost, for example when the Wi-Fi password changes. To reconfigure Wi-Fi, you may need direct pairing between the video system and the Cisco Room Navigator before reconnecting the Navigator over the network. When the video system uses Wi-Fi connectivity, Cisco recommends direct pairing of the Room Navigator.

### Cisco Webex and Cisco Webex Edge for Devices

Pairing Cisco Room Navigator To activate a device on Webex with a LAN-paired Cisco Room Navigator panel, pair the panel before activating the system on Webex.

If the device is already registered to Webex and local device user accounts are locked, you can initiate PIN pairing of the panel from Control Hub.

We always recommend that you upgrade to the latest available RoomOS version before activating your device on Webex.

Encryption is required to activate a Room Device on Webex A Room Device with hardware encryption support is required to activate the device on Webex and Webex Edge for Devices. Cisco Room Devices with the K7 flag in the device part number (visible through xStatus) do not support encryption and cannot be registered or linked to Webex. Encryption support is hardware-based and not controlled through software option keys.

Devices flagged with K9 in the part number support encryption.

You can verify encryption capability in the web interface under option keys. This capability cannot be added or removed because it is tied to the hardware model (K7: no crypto, K9: crypto).

### Peripherals

Max processed requests per second: Authenticated (for example POST to /putxml with basic authentication): 1 (queue 30)

Using session cookies (for example being logged in to the web interface via a browser): 15 (queue 90)

To explain what these numbers mean, let’s take for example the "authenticated" method: If you send 30 authenticated HTTP requests at once, it will take minimum 30 seconds before you get a response to the last request. If you send 31 requests, assuming all is coming in at the same time, the 31st request will get a http 503 response.

If you hit the rate-limiting (max requests per second), the request is queued until others are processed. This happens until the queue is full, and then new requests will get a HTTP 503 response instead of being queued.

Logs will show when the requests are being rate limited.

## Interoperability for RoomOS 26

The interoperability section describes the equipment and software revisions that have been tested for interoperability with this release. Please note: The absence of a device or revision from this section does not imply a lack of interoperability.

## Camera firmware and support

Note: Camera firmware has parity with the version installed on the Room Device. Camera software for Cisco Quad Camera is automatically updated when the Room Device is upgraded or downgraded. Camera firmware should share the same hash as the software currently installed on the Room Device.

Third party cameras

Third-party and older cameras may work with our integration room devices, but this is not tested and functionality cannot be guaranteed. TAC support may be rejected or limited.

## Cisco collaboration certification program

Cisco collaboration devices partner ecosystem is built on our certification program to ensure that customers get the best experience out of their Cisco collaboration devices and make integration as seamless as possible when integrating with third-party technology.

For more information, click here

HDMI Cable quality Cisco recommends use of high-quality HDMI 2.0 certified cables. Lower quality cables may work but may also have an impact on the image quality.

If you experience problems and do not have access to high-quality cables, try using shorter HDMI cables.

## xAPI Changes

We recommend endpoint configuration through the web interface and not from the xAPI command line.

The admin user has access to only a subset of relevant commands and configuration from the xAPI. The admin user can fully manage the system from the web interface, where all configurations are available. The remotesupport user has access to the full list of xAPI commands when utilized (requires TAC engagement).

Specific xAPI changes are not published in the release notes. Please refer to the Cisco API Reference Guides for the integrator products at the following locations:

Cisco Room Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-command-reference-list.html

Cisco Boards: https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-board/products-command-reference-list.html

Please also visit https://roomos.cisco.com for a great overview of the xAPI and other resources.

## Hardware revision and software dependencies

Due to occasional updates to hardware components, there can be constraints on running older software on newly manufactured Room Devices.

To identify a Room Device compatibility level, access the Room Device web interface and click Settings > Statuses. Scroll down to the compatibility level on this page. The tables below can be used to identify software constraints based on the compatibility level of your endpoint. Downgrading to an unsupported software version will fail. 
The latest software release is backward compatible with previous hardware revisions.

Note: RoomOS 26 currently supports all hardware revisions for the listed products.
Devices flagged with "NR" (No Radio) do not have Wi-Fi capability.

## Cisco Room Series software compatibility matrix

## Cisco Board Series Software Compatibility Matrix

## Cisco Desk Series Software Compatibility Matrix

## Cisco Peripheral Software Compatibility Matrix

Cisco peripheral software compatibility refers to touch devices and cameras requesting software from the Room Device. Some peripherals may require a higher software version than the Room Device is currently running.

Touch devices

If you see an error on the touch screen about the software not being compatible with the current software, please upgrade the Room Device software to the latest available version and try again.

## Cisco Terms of Service

Your use of Cisco software and cloud services are subject to these terms and conditions

Your use of Cisco APIs is subject to the Cisco Webex Developer Terms of Service

## Permitted Commercial Use for Scheduled Meeting Join Experience

The following use case requires separate permission for commercial use:

Providing a scheduled meeting join experience such as one button to push.

This includes use of any API that updates the device with calendar data from an external source to provide this functionality, including xCommand Bookings Put or previous private APIs such as bookingsputxml . In addition, using other APIs to accomplish the same functionality also requires permission for commercial use.

If you are providing a Scheduled Meeting Join Experience, you must either comply with the permitted commercial use terms below or use it only for non-commercial use. Non-commercial use is defined as use solely for your internal business operations and not for activities that involve using the API as part of, or in furtherance of, an income-generating service or product, whether directly or indirectly.

Any use to provide a Scheduled Meeting Join Experience that does not qualify under non-commercial use requires separate permission from Cisco. 
Cisco reserves the right to revoke your license to use our API if, in our sole discretion, we deem that your use is for unauthorized commercial purposes or otherwise violates the Webex Developer Terms of Service.

Please contact us at devsupport@webex.com if you have any questions about whether your intended use of the API is permitted, or to inquire about obtaining permission.

## Webex Certified and Webex Compatible vendors

To view a list of Webex Certified and Webex Compatible vendors, please visit: https://cs.co/certifiedvendors

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at www.cisco.com/go/offices .

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

| Revision | Date | Description |
|---|---|---|
| 03 | August 3rd, 2026 | Release of RoomOS 26.7.2.2 402ae006770, Minor |
| 02 | June 1, 2026 | Release of RoomOS 26.5.2.2 fb095ca4236, Minor |
| 01 | March 13, 2026 | Release of RoomOS 26.2.2.2 6f5a9c4b07c, Major |

| Cisco Room Series |
|---|
| Cisco Room Kit Pro, Room Kit Pro G2, Room Kit EQ, Room Kit EQX, Room Bar, Room Bar Pro Cisco Codec Pro, Codec EQ Cisco Room 70 G2 (Single/Dual) Cisco Room Panorama, Room 70 Panorama Cisco Room Navigator (Wall and Table Standalone) |
| Cisco Board Series |
| Cisco Board Pro 55 and 75 Cisco Board Pro 55 and 75 G2 Cisco Board Pro 55 and 75 G3 |
| Cisco Desk Series |
| Cisco Desk, Desk Pro, Desk Pro G2, Desk Mini |

| From | To | UCM | TMS | Web | SSH |
|---|---|---|---|---|---|
| 11.x | 26.x | YES | YES | YES | YES |
| >=10.15.x | 26.x (step upgrade may be required) | YES | YES | YES | YES |
| <=10.11.x | 26.x (step upgrade required) | YES | NO | NO | NO |

| Device | Software platform identifier | Latest available RoomOS 26 software |
|---|---|---|
| Cisco Room Kit Pro, Room Kit EQ, Room Kit EQX, Room Bar, Room Bar Pro, Codec Pro, Codec EQ, Room 70 G2, Room Panorama, Room 70 Panorama, Desk, Desk Pro, Desk Mini, Cisco Board Pro 55 and 75, Cisco Board Pro 55 and 75 G2 | s53300 | cmterm-s53300ce26_7_2_2.k4.cop.sha512 * cmterm-s53300-mtr-ce26_7_2_2.k4.cop.sha512 *** |
| Cisco Desk Pro G2, Cisco Room Kit Pro G2, Cisco Board Pro 55 and 75 G3 | s53600 | cmterm-s53600ce26_7_2_2.k4.cop.sha512 * cmterm-s53600-mtr-ce26_7_2_2.k4.cop.sha512 *** |
| Cisco Room Navigator (standalone) | s53350 | s53350ce26_7_2_2.pkg cmterm-s53350-mtp-ce26_7_2_2.k4.cop.sha512 |
| All RoomOS 26-supported products | N/A | cmterm-ce26_7_2_2.k4.cop.sha512 |
| Follow this link to find and download software for the device you are about to upgrade. |

| Deferral date | Versions | Note |
|---|---|---|
| N/A | None | No RoomOS 26 software versions have been deferred yet. |

| Feature / equipment | Limitations and advisories |
|---|---|
| Unified CM | H.323 and SIP consideration when provisioned by UCM When using UCM provisioning, the endpoint cannot register to a VCS (SIP or H.323) at the same time. This use case is not supported. When UCM provisioning is active, H.323 mode is disabled. We recommend migrating from H.323 to SIP.
Please note that being registered to UCM without having provisioning mode set to “CUCM” is not a supported scenario. NTP The collaboration endpoints do not support broadcast NTP servers from UCM, unicast only. |
| SIP / H323 | SIP Listen Port diagnostics warning When registered to a SIP proxy and SIP Listen Port is enabled, a diagnostic warning is displayed in the web interface: “SIPListenPortAndRegistration”. We recommend that SIP Listen Port is turned off when registered to a SIP proxy. Dual protocol enablement for SIP and H323 is not supported Having SIP and H323 enabled at the same time will generate a warning message on-screen indicating that having both protocols enabled (SIP and H323) is not supported. This message cannot be removed unless you disable one of the protocols. Having both protocols enabled and using them at the same time in different scenarios may introduce unexpected behavior. TAC will not support call scenarios where both protocols are enabled. |
| Web interface | HTTP Rate limiting To increase device stability and security rate limiting is in effect on the Room Devices. Max processed requests per second: Authenticated (for example POST to /putxml with basic authentication): 1 (queue 30) Using session cookies (for example being logged in to the web interface via a browser): 15 (queue 90) To explain what these numbers mean, let’s take for example the "authenticated" method: If you send 30 authenticated HTTP requests at once, it will take minimum 30 seconds before you get a response to the last request. If you send 31 requests, assuming all is coming in at the same time, the 31st request will get a http 503 response. If you hit the rate-limiting (max requests per second), the request is queued until others are processed. This happens until the queue is full, and then new requests will get a HTTP 503 response instead of being queued. Logs will show when the requests are being rate limited. |
| SNMP | The collaboration endpoint software is configured with default SNMP community strings. SNMP community strings should be treated as credentials and must be changed after initial configuration. RoomOS 26 provides basic support for SNMPv2 and SNMPv3 with default MIB only. |
| Security | Set a passphrase during initial device setup. On first login, you are also prompted to change the password. Note: This can affect automated provisioning workflows that rely on immediate login and configuration push, so automation should handle the password-change step explicitly. |
| Startup Wizard | While Startup Wizard is active, the system runs with Do Not Disturb (DND) enabled by design. DND cannot be turned off until Startup Wizard is completed. To remove Startup Wizard, complete it normally or set RunStartupWizard to False . If Startup Wizard is active, a diagnostics message appears in the web interface with a shortcut to that configuration. |
| Layout controls in Webex meetings | Layout control for on-premises devices in Webex Calls On-premises devices that are calling into Webex meetings will currently not have the same control options of the meeting that a Webex registered / linked device have. There are still some actions that are available through DTMF tones. Please visit https://help.webex.com/en-us/nli1uz4/DTMF-Commands-for-Video-Device-Enabled-Cisco-Webex-Meetings for a list of valid DTMF tones that can be sent to the Webex meeting to invoke certain actions. |
| Cisco Room Panorama | Cisco Precision 60 camera Cisco Room Panorama does not support Precision 60 cameras. Please note this when upgrading a Room 70 into a Room 70 Panorama, in case you have one connected and want to keep using it. |
| Encryption and Ciphers | Supported Ciphers You can check which ciphers that the device supports for its different services (HTTPS Server, SIP TLS, Syslog TLS, HTTPS Client) by typing xCommand Security Ciphers List in the xAPI. The supported ciphers may change between versions. |

| H323 gatekeepers / traversal servers | Minimum software |
|---|---|
| Cisco Expressway C / E (VCS) | Latest version available |
| SIP registrars / proxy servers |
| Cisco Expressway C / E (VCS) | Latest version available |
| Unified CM | Latest version available For device support, make sure you have the latest UCM device pack for your version installed. |
| Conference bridge interoperability |
| Cisco Meeting Server (CMS) | Latest version available For the latest conferencing features in CMS, the latest available software is always recommended. |
| Management server interoperability |
| TelePresence Management Suite | Latest version available Older versions of TMS do not support uploading software files for device upgrades. |

| Room Device | Camera | Comments |
|---|---|---|
| Cisco Codec Pro | Cisco Quad Camera | Full support |
| Webex PTZ 4K | Full support |
| Sony SRG-120DH Sony EVI-120DH | Pairing over IP and basic usage with pan, tilt, and zoom functionality are supported. Camera firmware updates are not supported. |
| Cisco Room Codec EQ | Webex PTZ 4K | Full support |
| Sony SRG-120DH Sony EVI-120DH | Pairing over IP and basic usage with pan, tilt, and zoom functionality are supported. Camera firmware updates are not supported. |
| Cisco Quad Camera | Full support |

| Device | Compatibility level | Minimum version of RoomOS 26 |
|---|---|---|
| Cisco Room Kit Pro | All revisions | 26.2.2.2 |
| Cisco Room Kit Pro G2 | All revisions | 26.5.2.2 |
| Cisco Room Kit EQ | All revisions | 26.2.2.2 |
| Cisco Room Kit EQX | All revisions | 26.2.2.2 |
| Cisco Room Bar | All revisions | 26.2.2.2 |
| Cisco Room Bar Pro | All revisions | 26.2.2.2 |
| Cisco Room Navigator (Wall and Table Standalone) | All revisions | 26.2.2.2 |
| Cisco Codec Pro | All revisions | 26.2.2.2 |
| Cisco Codec EQ | All revisions | 26.2.2.2 |
| Cisco Room 70 G2 (Single/Dual) | All revisions | 26.2.2.2 |
| Cisco Room Panorama | All revisions | 26.2.2.2 |
| Cisco Room 70 Panorama | All revisions | 26.2.2.2 |

| Device | Compatibility level | Minimum version of RoomOS 26 |
|---|---|---|
| Cisco Board Pro 55 | All revisions | 26.2.2.2 |
| Cisco Board Pro 75 | All revisions | 26.2.2.2 |
| Cisco Board Pro 55 and 75 G2 | All revisions | 26.2.2.2 |
| Cisco Board Pro 55 and 75 G3 | All revisions | 26.7.2.2 |

| Device | Compatibility level | Minimum version of RoomOS 26 |
|---|---|---|
| Cisco Desk Pro | All revisions | 26.2.2.2 |
| Cisco Desk Pro G2 | All revisions | 26.5.2.2 |
| Cisco Desk | All revisions | 26.2.2.2 |
| Cisco Desk Mini | All revisions | 26.2.2.2 |

| Device | Compatibility level | Minimum version of RoomOS 26 |
|---|---|---|
| Cisco Room Navigator | All revisions | 26.2.2.2 |