---
doc_id: roomos-cisco-com-print-whatsnew-releasenotesroomos-10-f16b17e881
source_url: https://roomos.cisco.com/print/WhatsNew/ReleaseNotesRoomOS_10
retrieved_at: 2026-09-01T19:39:52.613145+00:00
---

# Cisco RoomOS 10

# Release notes

D15463.23 - July 2024

## Document revision history

## RoomOS 10 is end of support

Support for RoomOS 10 has ended, and it is strongly recommended to upgrade your devices to RoomOS 11 or higher. If you are using an older version of RoomOS 10 that does not support upgrading with large files or cop files ending in cop.sha512 (specifically, versions 10.15 and below), you should use the RoomOS 10.19.5 Step Upgrade file to upgrade to RoomOS 11.

The RoomOS 10.19 Step Upgrade file is specifically for transitioning from RoomOS 10 to RoomOS 11. When you install this package, all other functionality is disabled. You can upgrade the device via the web interface as usual, using the step upgrade packages.

The respective packages for s53300 products and s53200 products are listed below. You will find these software files on the Cisco Software Site under the product you selected.

Note that this is only for devices that have had support for RoomOS 10.

s53300ce10_19_5-step-upgrade.pkg
s53200ce10_19_5-step-upgrade.pkg

## Introduction to Cisco RoomOS 10

This release note describes new software features and capabilities included in RoomOS 10 for on-premises deployment . RoomOS 10 is supported by the following products:

The software described in this document is released to https://www.cisco.com for on-premises deployment. If you register a Room Device to Webex you will be upgraded to the latest RoomOS cloud version available. RoomOS cloud software is not supported for on-premises deployment unless you are linked to Webex Edge for Devices with Cloud Software Management enabled .

You can tell the difference between a cloud and on-premises RoomOS version by looking at the third version number. For example:

- 10.X. 1 .x = Cloud

- 10.X. X > 1 .x = On-premises

Cisco RoomOS 10 is based on Collaboration Endpoint Software 9 (CE9) and is a continuation of the same software

This means that the first release of RoomOS 10 inherits the same features as CE9.15.3.17 as of April 2021. In the future, there will be a difference between the CE9 and RoomOS 10 since RoomOS 10 will be running on newer products. If you own a product that supports RoomOS 10+ but are running CE9.x, you should start planning the upgrade to RoomOS. These products will no longer get software releases from CE9.15.x and in order to stay up-to-date you must upgrade the device to RoomOS 10 or above.

Note: You will still find “ce” notations in provisioning services (TMS, UCM etc.), xAPI and on the software packages. If you look at the software version on the Touch panel bug you will see that the name has changed from CE to RoomOS.

Cisco RoomOS 10 can be downloaded here .

## Notes and warnings for the next major release RoomOS 11

These notes are to prepare you for the upcoming changes in RoomOS 11.

RoomOS 10 will soon be deprecated and EOS The next on-premises software release for RoomOS 11 targeted end of June 2023 will make RoomOS 10 obsolete and end of support. Cisco supports and releases new software versions for two minor software releases per product. Since all products that have support for RoomOS 10 also have support for RoomOS 11, the RoomOS 10 software line will go end of support quicker than for example CE9 that several supported legacy products still depends on.

RoomOS 10 will not be removed from cisco.com right away, but will likely happen during last 2023. Please prepare your devices and environment for upgrade to RoomOS 11 in order to stay on supported software.

RoomOS 11 will have a new UI In RoomOS 11 we are introducing a new graphical user interface that changes the current user interaction flow. The UI will become available in cloud a couple of months before released for on-premises.

NOTE: We previously announced that SNMP would be removed from RoomOS 11. RoomOS 11 will continue to support basic SNMP as before until further notice.

NOTE: Facility Service will soon be deprecated from newer software as quick dial functionality can be created using UI Extensions and macros .

# Release summary for RoomOS 10.19

## Notes and warnings for this software release

RoomOS 10.19.2.2 is unfortunately hit by the following bug, CSCwd23669 . To avoid more users hitting this issue, we have decided to remove the software from cisco.com even before a replacement is in place. The replacement software will be released as soon as we have resolved the bug. It may take a few days, but we can assure you that we are working as fast as we can! Click here for a list of deferred software versions.

The above issue is resolved in RoomOS 10.19.3.0

### RoomOS 11 UI Experience can be enabled on all supported devices from RoomOS 10.19.2.2

Several of the features we announce with RoomOS 10.19.2.2 requires that you enable the RoomOS 11 UI Experience. It is completely optional to enable the RoomOS 11 UI in RoomOS 10.19.2.2 but as RoomOS 11 is around the corner we recommend that you enable a few devices to get familiar with the new UI and also confirm that your existing deployments will still work with this UI. You enable the RoomOS 11 UI Experience on a per device basis or using Control Hub if you have devices on Webex Edge for Devices.

For feedback regarding the RoomOS 11 UI Experience you can send us an e-mail to webex-roomos11-ui-feedback@cisco.com . We appreciate your feedback and will help us create the best experience for everyone but we have a particular interest for functionality in custom integration scenarios. Please note that the feedback mailer is temporary and will be decommissioned without notice early CY2023.

For all other issues, please contact the Cisco Technical Assistance Center.

RoomOS 11 UI Experience - Limitations

- Creating and editing camera presets currently has to be done via the xAPI

- Room booking functionality (inside rooms) is not yet supported.

- Room signage on multi-screen systems shows on one screen only

- People focus works on single screen systems only

- No support yet for video stitching and video matrix

- Board Pro not supported in companion mode yet

- Room Panorama, Room USB, and Samsung Flip not supported yet

- Classroom/briefing room/presenter track features not supported yet

- Unbind feature missing from Room Navigator

- Barging shared line calls and remote resume is not supported

- Broadcast / Unobstructed mode is not supported yet

- Snap to whiteboard is not supported and is not planned for implementation in RoomOS 11

### Cisco Desk Limited Edition - Product Upgrade

If you have a Cisco Desk Limited Edition and upgrade it to RoomOS 10.19.2.2 it will become a Cisco Desk Pro . It will stay as a Webex Desk Pro as long as it is running software 10.19.2.2 or above. If you choose to downgrade to a version lower than 10.19.2.2 it will again identify itself as a Cisco Desk Limited Edition. This is a free but mandatory upgrade and you cannot choose to keep it as a Webex Desk Limited Edition on software that is equal to or higher than 10.19.2.2.

Note: The Cisco Desk Limited Edition is in fact a Webex Desk Pro by hardware specifications so there is no differences between a Desk Pro and a Desk Limited Edition on the hardware side.

Note: If you are registered on UCM / Webex Edge for Devices, the device type will change. This may cause the device to lose registration to UCM after upgrade. Please prepare to re-register the device as a Desk Pro post upgrade to RoomOS 10.19.

## RoomOS 10.19.5.6

RoomOS 10.19.5.6 is a patch release and contains only bugfixes

- Click here for a list of resolved defects in RoomOS 10.19.5.6

## RoomOS 10.19.4.2

RoomOS 10.19.4.2 is a patch release and contains a fix for CSCwd33600.

NOTE: Cisco Room 55 Dual, Room 70 Single, Room 70 Dual and Codec Plus will not have the option to enable the RoomOS 11 UI Experience in this release.

- Click here for a list of resolved defects in RoomOS 10.19.4.2

## RoomOS 10.19.3.0

RoomOS 10.19.3.0 is a patch release and contains bugfixes.

NOTE: Cisco Room 55 Dual, Room 70 Single, Room 70 Dual and Codec Plus will not have the option to enable the RoomOS 11 UI Experience in this release.

- Click here for a list of resolved defects in RoomOS 10.19.3.0

## RoomOS 10.19.2.2

# RoomOS 10.19.2.2 feature descriptions

## RoomOS 11 UI Experience (optional enablement)

As already announced many times, RoomOS 11 will come with a new user interface. Some devices like Cisco Board Pro, Desk Mini, Room Bar and Desk Hub already requires the use of RoomOS 11 UI and devices with a cloud deployment has been able to enable this UI for a while. But with RoomOS 10.19.2.2 we invite everyone with a supported device to try it out! With a configuration you can now enable the new UI and experience it first hand.

From the web interface:
Go to configurations and search for "concept" and set the UserInterface Concept Mode to "Compositor".

From the xAPI: 
For Board, Desk, and Room Series devices set xConfiguration UserInterface Concept Mode to "Compositor".

Set the configurations to "Desktop" to switch back to the RoomOS 10 UI.

Please make sure you read the list of known limitations before enabling the RoomOS 11 UI Experience. Also note that many of the new features coming will only work with the RoomOS 11 UI.

Click here to learn mode

Supported products

All products except Cisco Room 70 Panorama, Room Panorama and Room USB

## Standby Control / Energy Saving - Office Hours

Office hours is a new feature designed to give your equipment a longer life and save energy while the devices are not in use. The feature is turned on by default and your office hours is pre-defined from 7am to 7pm, Monday to Friday. The Office Hours feature is fully configurable from the web interface or the xAPI for you to define your own office hours or disable the feature completely.

Although you can disable the feature, it is not recommended to do so. This feature is designed to benefit the life expectancy of the device monitors, especially if signage is being used. It also helps save energy as the device will have a lower amount of automatic wake up events and keeps the screens in standby as much as possible outside office hours.

While the device is "outside of office hours", for example during nights and weekends by default:

- Digital Signage will be disabled

- Wake-up on motion detection is disabled

- You can configure a shorter standby delay when the device is outside office hours (also shorter by default)

- Touching the touch panel, incoming calls, users pairing and connecting a laptop to the device will wake up the device as normal

- The device will not go into standby while doing a local presentation or while being in a call, even in this mode

- xStatus Time OfficeHours OutsideOfficeHours will be set to "True", indicating that the device is in this mode currently

- You can still use the devices as normal in "OutsideOfficeHours" mode, but it may have a shorter delay for entering standby

- Known issue - Scheduler do not go to standby when the device is in out of office hours mode.

During office hours:

- It will work as normal for the defined duration

- xStatus Time OfficeHours OutsideOfficeHours will be set to "False" and the device will wake up automatically into half-wake and act according to the regular configurations.

Supported products

All products

## Frames

When this feature is turned on, the device will crop out a focused image of one individual or a smaller group of individuals sitting close to each other in the room. The images that are framed will be put together into one image sent to the far end. Excess space between the cropped individuals are removed.

Speaker Track is required for this feature to work. Framing / processing is done on the sender side before the image is sent so, the receiver do not have to support this feature.

The feature can be activated from the touch panel UI. The camera supports up to 4 frames.

Supported products

Cisco Room Kit Mini, Room Kit, Room 55, Room Bar and Board Series Requires RoomOS 11 UI Experience

## Support for Cisco Room Bar

Room Bar is an all-in-one video conferencing bar that does it all—from native, laptop-free video conferencing and wireless sharing to seamless BYOD experiences. Power your meetings with a codec-powered appliance or connect your computer via a single USB-C cable.

Note: In order to register this product on UCM you will need the device pack released 22nd of September for either UCM 12.5 or UCM 14, follow the links below to download. UCM 12.5 UCM 14

These device packs includes a fix for CSCvn11243. We have removed the fields for SMTP and HTTPProxy credentials from the device specific configurations.

For more information about the Cisco Room Bar, please follow this link

Cisco Room Bar is designed to run RoomOS 11 UI natively.

## Call from laptop

"Call from laptop" is a new icon you will notice on the touch panel. This feature allow you to use the device camera and microphone with any PC application together with a HDMI to USB converter. You to connect the HDMI output from the device to the HDMI to USB device for camera and microphone passthrough to your laptop. This will allow you to use the device camera and microphone as a normal USB web camera / microphone for the the application you use on your laptop - for example the Webex client.

In order to use the speakers on the Room Device at the same time, you have to connect your laptop directly to one of the input sources of the device (like a normal content share).

You can use the camera controls and mute buttons on the room device as you would in a call from the device itself. Speaker Track and Presenter Track will also work, but the device will be put in DnD mode while this feature is active.

See related xAPI commands

To remove the icon from the touch panel you can issue the command (depending on the product):

```
xConfiguration UserInterface Features Call Webcam: Visible/Hidden
xConfiguration UserInterface Features Call HdmiPassthrough: Visible/Hidden
```

Supported products

Webex Room Kit, Codec Plus, Codec Pro, Room 70S, Room 70 G2 and Room 55 Note: This feature is to compensate for devices without a USB-C for USB-passthrough but devices with existing support for USB-passthrough will still see the button "Call from laptop". Note: We have tested capture devices from Inogeni to work but other similar devices may work as well

Requires RoomOS 11 UI Experience

## Wireless share with Miracast®

RoomOS 10.19.2.2 comes with support for direct wireless sharing using Miracast®. Miracast® will allow the laptop running Windows to create a wireless network link with a nearby device and stream the screen share at a high framerate / quality including audio to the device. This stream can be shared in a call or displayed locally as a normal content share. This type of share do not require any client software as it is built into Windows natively.

Wi-Fi Direct (2.4GHz only - TCP port 7236) is used to establish a connection between the Windows Laptop and the Webex Device. This feature do not require guests to be connected to the corporate network but is required to enter a code that is displayed on the device screen in order to connect.

Requires that the Webex Room Device is connected to the network using Ethernet (cabled network).

For more information, check out this article .

Supported products

All products (except Desk Hub) with a Wi-Fi beacon and on a cabled network Devices with optional Wi-Fi antennas should have these attached before using this feature. Requires RoomOS 11 UI Experience

## Webex Edge for Devices only

This section describes features you gain by linking the device to the cloud via Webex Edge for Devices.

## Support for Embedded Apps

Embedded apps are apps that can be opened inside the meeting and extend the meeting experience. Currently our devices has support for three embedded apps (Miro, Mural and Slido).

For more information about this feature, see this article

Supported products

Cisco Desk, Desk Mini, Desk Pro, Board / Board Pro series Requires RoomOS 11 UI Experience

## Hide tentative meetings from the UI

Allow admins to show or hide tentative calendar meetings and other related alerts for shared mode devices. Only meetings that has been approved by the calendar proxy or resource manager will be displayed.

This feature is turned off by default and must be enabled to take effect.

View related xConfigurations

Supported products

All products

## Support for immersive shares from Webex client

Devices now render immersive shares from the Webex client correctly.

Supported products

All products

## People presence

Show a presence indicator on your device in personal mode on your avatar. Also see the presence of others when searching for people in the directory (cloud users only), in recent list and the participant list of meetings.

You can update your status directly from your personal device and set custom status that will be reflected on your cloud user in other clients as well.

Supported products

Cisco Devices in personal mode Requires RoomOS 11 UI Experience

## Hot desk pairing with QR code

Devices in hot desk mode will now display a QR code that can be scanned by the user in order to pair and book the device. Once you scan the QR code the Webex App will open and exchange the pairing token. This is an addition to the already existing pairing options.

Supported products

Cisco Desk Series Requires RoomOS 11 UI Experience

# Release summary for RoomOS 10.15

## Notes and warnings for this software release

### The legacy media resilience protocol (FLUX) is now removed from RoomOS 10.15

As mentioned in the RoomOS 10.3 release, we planned to deprecate the FLUX media resilience protocol. This change has now been committed and FLUX is no longer supported.

### Input connector quality configuration

We have changed the value space of the xConfiguration Video Input Connector[x] Quality to make it more specific. Previously we had Motion and Sharpness only. We have added Auto that will start with sharpness quality and move towards motion if motion is detected. In previous versions Sharpness acted the same way as the new Auto configuration but is now providing Sharpness quality exclusively.

### Brightness reduction on Cisco Room 70D

Due to an issue with some of the backlight LED burning out on the Cisco Room 70D screens, we have slightly lowered the brightness on these LEDs to increase their life expectancy.

### Some features are only supported with the RoomOS 11 UI Experience

For this release we have some features that will only be available for the RoomOS 11 UI Experience. This means that some devices that do not have support for the new UI yet in an on-premises deployment, will have to wait in order to use those features described in the next section. This is the reason why only a select few devices is mentioned under "Supported products" for now.

## RoomOS 10.15.5.3

This is a patch release and contains bugfixes only.

- Click here for a list of resolved defects in RoomOS 10.15.5.3

## RoomOS 10.15.4.1

This is a patch release and contains bugfixes only.

- Click here for a list of resolved defects in RoomOS 10.15.4.1

## RoomOS 10.15.3.0

RoomOS 10.15.3.0 is a patch release to add support for Cisco Desk Mini with compatibility level 1 , and will also be the minimum software version for this device. Please refer to the desk compatibility matrix in this release note.

- No bugfixes in this release

## RoomOS 10.15.2.2

# RoomOS 10.15.2.2 feature descriptions

## WebEngine Kiosk Mode

WebEngine Kiosk mode allow you to hide the normal user interface and render a full screen web app, tailored for your company needs. This feature is ideal for self service terminals located in a reception area or similar. The device is configured to open a URL pointing to your Web App.

Click here for more information to get started

Supported products

Cisco Board Pro Series and Desk Mini*

## Persistent Web Apps on Webex Room Navigator

Persistent Web Apps on a Webex Room Navigator is similar to the Kiosk Mode described above but for the Webex Room Navigator. This feature has native integration with the device xAPI. With this integration you may have one single Web App that is adapting to the device connecting to the Web App, which is suitable for multiple room deployments. This feature is great for custom user or room booking interfaces. Persistent Web App is a new mode you can select when setting up the Room Navigator for the first time.

The Room Navigator must be paired to the device remotely in order to use this feature.

Click here for more information to get started

Supported products

Cisco Room Navigator*

## Alarm detection on xAPI

When enabled, the device can detect a T3 standard alarm signal, which is the industry-standard alarm pattern in the United States, and change the xStatus RoomAnalytics T3AlarmDetected from False to True. Using a macro, you can configure the device to enhance safety and security by display a web page containing instructions on how to exit the building in case of a fire alarm for example. Keep in mind that it is not guaranteed that the device will detect an alarm signal (for example, having low microphone levels may not be able to detect the signal) and you should not use this feature as a replacement for any other safety and security measures and documentation.

Click here for more information

Supported products

All products

## Open Microsoft OneDrive whitebaords

Store and open whiteboards from Microsoft OneDrive directly from the "Files" button on your device.

Supported products

Cisco Board Pro, Cisco Desk Mini*

## Portrait cropping on Desk and Board devices

Portrait cropping or "People focus" is a new layout option that can be applied in any layout family. People focus optimizes the available space on the screen by removing parts of the background from the image frame, keeping the person in focus.

Supported products

Cisco Board Pro, Cisco Desk Mini*

Click here for more information

## Added support for SNMPv3

Cisco previously announced that SNMPv2 was going away but this was reverted. We landed on keeping the SNMPv2 implementation but also adding support for SNMPv3, which is more secure than SNMPv2. There are no changes to the MIB used (both SystemContact and SystemLocation are used by v2c and v3), so the feature is the same functionality wise.

The existing xAPI configuration is the same and the xConfiguration NetworkServices SNMP Mode applies to both SNMPv2 and SNMPv3. In order to use SNMPv3 only, you can set the xConfiguration NetworkServices SNMP CommunityName to "" (empty string).

The following new commands adds support for SNMPv3 USM (User-based Security Model)

xCommand Network SNMP USM User Add xCommand Network SNMP USM User Delete xCommand Network SNMP USM User List

Note:

The authentication protocol must be selected between SHA-224, SHA-256, SHA-384 and SHA-512

The PrivacyPassword is optional and will if not set, default to the AuthenticationPassword

The protocol is always AES

Authentication and privacy is always on (security level authPriv)

We do not support MD or SHA1 for authentication protocol

We do not support DES for privacy protocol

We do not support authNoPriv or noAuthNoPriv as security level

Example

On device:
xConfiguration NetworkServices SNMP Mode: ReadWrite
xCommand Network SNMP USM User Add Name: Name AuthenticationProtocol: SHA-512 AuthenticationPassword: myAuthenticationPassword PrivacyPassword: myPrivacyPassword

On linux with net-snmp installed:
snmpwalk -u Name -l authPriv -a SHA-512 -A myAuthenticationPassword -x AES -X myPrivacyPassword

NET-SNMP version: 5.9.1 and above

Supported products

All products

## USB Forwarding support added for Desk Hub

You can turn on USB forwarding for the Desk Hub's USB-A port or left USB-C port (seen from the back) using the BYOD USBForwarding configurations. When USB forwarding is enabled for a USB port, only a computer connected to the Desk Hub can use peripherals that are connected to that port; the Desk Hub itself can't find or use these peripherals.

A common use case is to connect a keyboard and mouse to use with the laptop to a port with USB forwarding enabled. Alternatively, you can connect the laptop peripherals to a screen's built-in USB hub, and then connect the screen to a port with USB forwarding enabled. In both cases this allows you to connect and disconnect only one cable (the blue USB-C) when you come or leave the desk. This may also be convenient in a hot desking type of environment.

## Test microphone with self-hear

Self-hear is a new feature under microphone options that allows a user to test the microphone by taking a short recording of your voice and playing it back to you. Just like self-view, only with audio. This is useful to identify if you need to enable noise cancellation or voice optimization.

Supported products

Cisco Desk Mini, Desk Hub, Board Pro*

## Webex Edge for Devices only

This section describes features you gain by linking the device to the cloud via Webex Edge for Devices.

## Webex Panorama: Support for Panorama Video in cloud calls

Cisco Room Panorama now supports panorama video in cloud calls.

Supported products

Cisco Room Panorama, Room 70 Panorama

## Hot desk support

A device in Hot Desk mode allows you to sign in using your Webex Identity and convert the device into your personal device for a selected time frame or the whole day. The device automatically signs out when the booking ends, making it available for the next person. The device must have RoomOS 11 UI Experience enabled for this feature to work.

Supported products

Cisco Desk Mini, Desk Hub*

## Webex Client pairing using USB-C

When pairing a USB-C cable from your Webex Desk device to your laptop, your Webex client will automatically pair to the device, so you can make calls from the device. This creates a more consistent pairing method (compared to ultrasound or manual pairing over the network) where everything goes over the USB-C cable, audio, video and pairing signal.

Also note: Connecting a USB-C cable to a device in hot desk mode will automatically start the booking sequence and the registration process.

* Requires RoomOS 11 UI Experience

# Release summary for RoomOS 10.11

## Notes and warnings for this software release

New product support with RoomOS 11 Experience UI

From RoomOS 10.11.2.2 we have added support for new products that has been designed to only work with the new RoomOS 11 Experience UI that is planned to be released for all supported products with RoomOS 11. It is currently a small feature gap on the new UI compared to the old, please read below for an updated list of known limitations related to the new UI and the new products. We are constantly working to close the feature gap and the list of known limitations will be updated continuously.

RoomOS 11 Experience is an app-based UI designed for multi-tasking and seamless switching between activities. It has a few new features that will be properly announced when we release RoomOS 11. Some of the new features you will see for the new products are:

- Navigate the UI by opening menus and closing apps with touch gestures

- "Optimize my voice" is an extension of the noise canceller that will also remove background speech.

- Note: "Tips" can be disabled from the xAPI

Click here for more information

Known limitations

NOTE: Known limitations for RoomOS 11 UI Experience listed here has been moved to the 10.19 section

See the software upgrade section

## RoomOS 10.11.6.0

This is a patch release and contains bugfixes only.

- Click here for a list of resolved defects in RoomOS 10.11.6.0

## RoomOS 10.11.5.2

This is a patch release and contains bug fixes only.

- Click here for a list of resolved defects in RoomOS 10.11.5.2

## RoomOS 10.11.4.1

This is a patch release and contains bug fixes only.

- Click here for a list of resolved defects in RoomOS 10.11.4.1

## RoomOS 10.11.3.0

This is a patch release and contains patches for some of the known limitations for the new device support introduced in RoomOS 10.11.2.2. Please refer to the above list of known limitations for the new products in RoomOS 10.11.x

- Click here for a list of resolved defects in RoomOS 10.11.3.0

## RoomOS 10.11.2.2

# RoomOS 10.11.2.2 feature descriptions

## Support for Webex Board Pro 55 and 75

Webex® Board Pro is an all-in-one device that provides everything you need for hybrid teamwork: it brings your local and remote teams together to collaborate in a connected digital workspace. Board Pro is a purpose-built solution combining premium visual collaboration, video conferencing, ideation, and co-creation, allowing your teams to join video-first meetings, digitally whiteboard, wirelessly present, and share content.

Click here for more information

## Support for Webex Desk Mini

The Webex® Desk Mini is a portable all-in-one collaboration device that enables you to make any space an office. Easily turn your dining room or any small space into a productive workspace. The Webex Desk Mini is designed with an integrated handle which makes it easy to move around from one room to another. It also comes equipped with privacy features such as noise removal, video backgrounds and easy access to in-meeting controls — so you can always show up and look professional in meetings even from your kitchen or living room.

Providing everything you need to work; with its USB-C connection you can double up your screen real estate, interact with any laptop content and applications as well as join any conference app running on your laptop. It’s the perfect work companion to your laptop with a 64-degree, 8 MP camera, intelligent microphone array for focused sound pickup and powerful speaker system you get a high-quality video and audio experience every time.

Click here for more information

## Support for Webex Desk Hub

The Webex® Desk Hub enables the office space of tomorrow through advanced collaboration, personalized experiences, and native shared desk experiences to deliver a modernized, clutter-free safe environment for the hybrid worker. experiences designed for Hot Desking, Hoteling, and advanced Collaboration.

The Desk Hub will sit within the single portfolio for Webex Collaboration devices and be a bridge between video phones and our integrated video endpoints like the Webex Desk or Webex Desk Pro. The Webex Desk Hub has unique hardware and software capabilities which enable shared office space use cases like seamless Desk Reservation, built-in IOT sensors, and Personalized Experiences for the reserved user. The Webex Desk Hub is a new desktop device targeted to enable the next generation of transformed office spaces for shared and dedicated desks or home office. The Desk Hub has a modular form factor and unique

Click here for more information

## Support for pairing touch panels using PIN

We are making it easier to remotely pair a touch panel to a Room Device by adding PIN pairing. You can choose between using credentials as before or providing a one-time PIN in order to pair the touch panel. The PIN pairing do not require you to create an additional user to pair or expose the Room Device credentials.

This feature is supported for both the Cisco Touch 10" and Cisco Room Navigator.

To initiate PIN pairing you have to access the Room Device CLI using SSH or a serial connection. If your device is linked to Webex via Webex Edge for Devices you can generate a PIN from Webex Control Hub.

Execute xCommand Peripherals Pairing PinPairing Start . By default the PIN will be displayed on the monitor in the room as well as being printed out in the CLI. Provide the PIN to the person who is pairing the touch panel to the Room Device. You can choose to not display the PIN on the screen. A note will be displayed asking the user to contact the system administrator to get the PIN.

By default the PIN is active for 60 minutes but can be configured to work for up to 24 hours. After that a new PIN has to be generated.

By default the user has three attempts but can be configured up to ten. The number of attempts left will be displayed on the screen when there are less than 3 attempts left. You have to generate a new PIN if all the attempts fail.

Connect the touch panel to the network and type in the host IP of the Room Device you want to pair to. The Room Device must be running RoomOS 10.11.2.2 for PIN pairing to work. The touch panel will upgrade automatically when successfully connecting to the Room Device.

You will now be asked to type in the credentials of the Room Device, but you will see another option for PIN pairing. When pressed you get a field to type in the PIN and on a successful attempt the touch panel will pair to the device. You can only pair one touch panel per PIN code generated.

See also xCommand Peripherals Pairing PinPairing Stop as this will abort a pending PIN pairing at any time if necessary.

# Release summary for RoomOS 10.8

## Notes and warnings for this software release

Webex Desk software upgrade Please note that Webex Desk use a new software package with l4t in the package name. This is part of a transition that will eventually apply to all the devices. This message is just to make you aware of the current package name difference. You cannot currently upgrade the Webex Desk using the non-l4t s53300 software package even though they are the same platform.

Note: Webex Desk do not have support for WebRTC in RoomOS 10.8.2.5, this will be added in a future release.

See the software upgrade section

## RoomOS 10.8.4.0

This is a patch release and contains bug fixes only.

- Click here for a list of resolved defects in RoomOS 10.8.4.0

## RoomOS 10.8.3.1

This is a patch release and contains stability adjustments for the Webex Room Navigator. Added support for new compatibility level for Webex Desk.

- Click here for a list of resolved defects in RoomOS 10.8.3.1

## RoomOS 10.8.2.5

# RoomOS 10.8.2.5 feature descriptions

## Support for Cisco Desk

The Webex Desk is the all-in-one collaboration and productivity device for your desk—at home, in the office, or in a shared space. It is purpose-built for collaborating, whether you’re in a meeting, sharing your laptop screen, or brainstorming with a teammate. The Webex Desk device features a 24-inch, interactive 1080p display, 64-degree UHD camera, full-range speaker, and a mic array with AI-powered background noise suppression.

This powerful device creates a clutter-free desk space, enabling you to be organized and productive. Manage your workday with dynamic layouts and custom views, take the strain off your laptop, and optimize your meetings—all from a single system. Meet without distractions or background noise. Rock a presentation with immersive sharing. Co-create with digital whiteboarding and live content annotations.

Easy setup and management capabilities allow customers to deploy and support thousands of devices at once. And with Control Hub you’ll gain insight into environmental health and device usage with the ability to triage issues from anywhere.

For more information about the Cisco Desk, follow this link .

## Support for Cisco Microphone array for Cisco Room Panorama / Panorama 70

The Cisco Microphone Array is a premium directional microphone array designed to provide the Cisco Room Panorama immersive video collaboration system with crystal-clear, spatial audio. It can capture participant voices from different directions and deliver multiple streams of high-fidelity audio. The Microphone Array recognizes which side of the table the speaker is on. To the far-end participants, it provides a more immersive, natural experience as voices coming from the left of the table are played back remotely from the left speaker, and vice versa. It supports immersive and inclusive executive meeting and conferencing scenarios for in-person and remote participants alike—just as if they were all in the same room. Better still, the Microphone Array supports an IP-based AV setup, allowing for enhanced flexibility and lower deployment costs.

For more information about the Cisco Microphone Array please follow this link

Supported devices

Cisco Room Panorama / Panorama 70 / Panorama 70 Upgrade

## Support for 802.1x with Cisco Room Navigator

You can now use 802.1x for network authentication using credentials or client certificates with the Cisco Room Navigator.

When connecting the Room Navigator to a 802.1x secured network, you will see a message on the screen saying that it was not able to obtain an IP address.

- In the network settings on the Touch panel UI, tap the "Ethernet" button and scroll down to you see "Use IEEE 802.1x" and enable it.

- Enter the 802.1x credentials to obtain an IP address

If you are using client certificates, this has to be uploaded to the Room Navigator manually and requires more steps.

- Factory reset the Cisco Navigator (do not pair it to a device yet as this will destroy the admin user and you will not be able to log in)

- Connect the Room Navigator to a separate and isolated LAN where it can receive an IP so you can connect to the Room Navigator via SSH (don't use serial)

- Log in with admin and no password

- Run xCommand Security Certificates Services Add and paste in the client certificate PEM

- Run xCommand Security Certificates Services Show and copy the certificate fingerprint

- Run xCommand Security Certificates Services Activate Fingerprint: PASTE_FINGERPRINT Purpose: 802.1X

- Connect the Room Navigator to the 802.1x network and pair to a codec when the device is successfully connected to the network. Make sure that "Use Client Certificate" is enabled on the 802.1x network settings in the Room Navigator

Supported products

Cisco Room Navigator

## Synchronize software with Cisco Room Navigator

Requires default credentials on the codec for the Room Navigator to connect. 
Requires that the Room Navigator is running RoomOS 10.8.2.5 or above.

Both locally paired and network paired scenarios work as long as the above requirements are met.

In some scenarios where the Cisco Room Navigator is unable to pair to a Cisco Room Device because the Room Device is running software that is not supported by the device. This recovery feature will make it easier to upgrade the Room Device and also configure the device network settings.

In a scenario like described above, you will see an error message on the screen and a red button saying "Troubleshooting page". When tapping this button you will be directed to the software recovery page that provides two options for upgrading the Room Device. You can upgrade the device by pointing to a LAN hosted software package on UCM, TMS or your own web server (URL) or you can upgrade via cloud. Cloud upgrade is the simplest option but it requires that the device has Internet access.

If you upgrade the device via cloud it's important to upgrade again to the latest version of RoomOS available on cisco.com if you are deploying the device for on-premises. The cloud upgrade method is only provided to make it easier to upgrade and recover quickly from the pairing incompatibility.

Supported products

Cisco Room Navigator

## Local web app management from the Touch Interface

You can now let users add local web apps directly from the Touch Interface without having access to the device web interface.

The feature is disabled by default but can be enabled from the configuration in the web interface or by the following command:

xConfiguration WebEngine Features LocalWebAppManagement

When enabled, a new item will be available from the settings in the Touch Interface allowing a user to create new UI buttons that opens their specified web app. The user types in a name and a URL and saves it directly on the device it self.

Supported products

Cisco Desk Series
Cisco Board Series

## Support for third party USB microphones and audio interfaces

Added extended support for third party USB microphone and audio interfaces in addition to the existing USB headset support depending on how you configure the xConfiguration Audio USB Mode .

The USB Mode configures whether the input or output (or both) should be used to/from the connected USB audio device. Set the configuration to "Speaker" to use the output only, "Microphone" to use input only or "SpeakerAndMicrophone" for both input and output.

The below list of devices is not exhaustive, but have been tested and are known to work.

- Blue Microphones Yeti Nano

- Blue Microphones Yeti

- Rode NT-USB Mini

- Shure MV7

- MXL ac-404

- Audient EVO4

- Roland UA-25EX

- Audinate Dante USB I/O Module

- Shure INTELLIMIX P300

- Shure ANIUSB-MATRIX

- M-Audio M-TRACK SOLO

- Extron dmp 128 plus

Supported products

Cisco Room Kit Mini, Room Kit, Room 55 
Cisco Desk, Desk Pro

## New layout menu

We have changed the default layout menu to a dropdown menu that also illustrates how the layout looks like.
The prominent layout has changed to more grid based layout with with 1 large + N small images.

Supported products

All products

## Whiteboard shape recognition for curves/arcs and arrows

The whiteboard shape recognizer now understands curves and arrows.

Automatic shape recognition can be triggered while drawing a shape, without needing to toggle the feature on.  Once a shape is drawn, keep your finger or pen on the screen and a preview of the corrected shape will be shown, release your finger to adjust the shape.

Supported Room Devices

Cisco Board Series
Cisco Desk Series

## Gesture recognition for Raise hand

While in a CMS meeting that supports raise hand (you see a raise hand button on the touch interface), the device will recognize the gesture of raising your hand physically.

When your hand is raised a confirmation timer will show on-screen. When the timer is complete it will trigger "raise hand" in the meeting for your participant as if you where clicking the "raise hand" button.

Supported devices

Cisco Desk Series

## Webex Edge for Devices specific features

The features listed below are only available when the device is linked to Webex via Webex Edge for Devices.

Gesture recognition for reactions

In a Webex meeting with reactions and gesture recognition enabled, you will be able to send reactions to the meeting using physical gestures. 
Reaction gestures include thumbs up and down. Also see " Gesture recognition for Raise hand "

Supported devices

Cisco Desk Series

Cloud pairing for Webex Edge for Devices

You can now pair your device to your Webex App manually by searching for the device or automatically using ultrasound.

Supported products

All products

Direct share from Webex

To improve the quality of content charing, with direct share the Webex App prefers to share the content directly to the pairing Webex device over the local network. In setups where direct share is not available, the app continues to route content share media through the cloud.

Supported products

All products

## Other changes

Complete keyboard language support is now turned on by default

We have introduced complete keyboard language support in an earlier version but the feature was by default turned off which is an incorrect setting. This has now been set to be turned on by default. This means that the keyboard will change to localized mode after upgrade (the letters on the keyboard will change to the selected device language).

You always have access to a keyboard with english letters by clicking the globe icon next to the space bar. The globe icon is only visible if a non-english device language has been selected.

Please note that this change includes minor modifications to the keyboard layout.

All products

WPA1 is no longer supported (Wi-Fi)

WPA1 Personal and Enterprise is removed and no longer supported.

All products that has support for Wi-Fi

H323 now supports AES256 encryption

Added support for AES256 encryption for H323. When H323 is configured to use AES256, you should also set the H323 Encryption KeySize to Min2048bit.

All products

Webex activation network test

Only applicable if you are registering the device to Webex. If the initial Webex activation fails, you will now see a Cloud Connection Test button on the interface. Tapping the button opens a screen showing the network status and the result of the test.

The connection test is also available in the settings after you have successfully registered the device to Webex.

All products

# Release summary for RoomOS 10.3

## Notes and warnings for this release

### The legacy media resilience protocol (FLUX) will soon be deprecated

Predicted version where this feature will be deprecated: Future RoomOS release

A media resilience protocol is present to make the media resilient to loss in lossy network conditions. RoomOS 10 has support for a much more effective protocol (Media Assurance) which is also supported by CE9 and is used in all supported backend's. This is the primary resilience protocol used today.

How this change will affect you

FLUX has been kept for backwards compatibility with endpoints that is running TC7.x software. This upcoming change means that 1:1 calling between a TC7.x and RoomOS 10.8.x+ devices, may in lossy network conditions experience degraded media quality.

## RoomOS 10.3.4.0

This is a patch release and contains bugfixes only.

- Click here for a list of resolved defects in RoomOS 10.3.4.0

## RoomOS 10.3.3.0

This is a patch release and contains bugfixes only.

- Click here for a list of resolved defects in RoomOS 10.3.3.0

## RoomOS 10.3.2.0

# RoomOS 10.3.2.0 feature descriptions

### Initial feature parity with Collaboration Endpoint Software CE9.15.3.17

New features in CE9.15.3.17 also included in RoomOS 10:

- CMS Raise hand (requires Cisco Meeting Server (CMS) 3.2)

- Share WebApps in call

- Whiteboard shapes

- Direct ad-hoc booking from inside meeting rooms (requires Webex Edge for Devices or Webex registration)

Click here for more information about CE9.15.3.17 and the features above.

### Support for Cisco Desk Limited Edition

Cisco Desk Limited Edition is a new product in the Cisco Desk Series and is only supported with RoomOS 10 and above.

### Immersive share for Cisco Desk Pro and Desk Limited Edition

Deliver more engaging presentations, by placing yourself in front of any content you share from your computer.

- You need to enable Virtual Backgrounds before using Immersive Share.

- Your computer must be connected to the Cisco Desk Pro or Desk Limited Edition with the USB-C cable.

The presentation and video are both sent in the content stream so you will stay in focus until you stop sharing. This is available through the floating content bar.

The main video is muted while you are in immersive share mode.

Known limitation: While in immersive share mode, the camera LED is not lit. A workaround is to look at the screen, you will see yourself in the presentation as a indication that the camera is enabled. This will be resolved in a future release.

Click here for more information about immersive share

### Other changes

Added a new button to enable Personally Identifiable Information (PII) logging from the Touch interface

On the touch panel. Go into the settings menu and press "Issues and diagnostics". A new button is available to enable PII logging.

When PII Logging is enabled the device will write PII information in the logs. A PII warning banner is displayed on the Touch device and on the screen.

This feature can be used for troubleshooting purposes when unobscured logs are required. This setting does not persist a reboot.

Added Room Analytics dashboard in the Web UI

If you have enabled any Room Analytics features on your Cisco Device, a Room Analytics dashboard will appear on the web interface home page.

### Important notes and warnings for this software release

RoomOS 10 do not have support for older device models

Click here for an overview of supported devices

ISDN Link is no longer supported

Software support for ISDN Link has been removed in RoomOS 10. If you require to use ISDN Link, please use the latest Collaboration Endpoint Software version supported by the Room Devices.

Cisco Proximity Share To Clients Removed

The Cisco Proximity for Mobile app is being phased out, and no further development is planned on these apps. As a step in this process the "share to clients" functionality has been removed from RoomOS 10.3.2.0. The Cisco Proximity for Desktop version is still supported (share from clients) and will receive updates going forward.

# Software upgrade and downgrade

## Upgrading software on a Cisco Room Device

Upgrading from any CE9 version directly is supported, however there may be limitations to the different upgrade methods that you need to take into consideration . Using the xAPI method to download the “.cop” software from a HTTP server should work from any CE9 version to RoomOS 10.

You can upgrade devices using the native web interface of the device, Unified CM, TMS or using the device xAPI.

If you are having issues upgrading from even older software versions, you can upgrade the device using the "CE9.15.6 Step upgrade" file that is available on cisco.com for applicable devices before upgrading to RoomOS.

Note: If you upgrade to RoomOS 10 from version < CE9.13.x, any settings that no longer exist in RoomOS 10 will be removed from the configuration database. When you now downgrade back to a version < CE9.13.x, the settings will be set to the default value on the respective version.

Before you start, please make sure you have downloaded the software for the correct platform.

The "All products" cop file (super cop) must only be installed to a provisioning service, for example Unified CM. This package provides software to all supported video models and peripherals, so you only have to install one cop file.

NOTE: The all products cop file do not contain l4t images

NOTE: Upgrading from the device web interface using .k4.cop.sha512 files is not supported, please use the .k3.cop.sgn files

WARNING: Do not delete ".pkg" files that are stated to be "Not in use" on Unified CM. The devices are pointed to a loads file that tells it what package to use for the different peripherals. UCM is not aware that the ".pkg" is in use. By deleting peripheral or device software the device will fail to upgrade or fail to upgrade its peripherals.

### Software integrity verification after download

To verify the integrity of the software image you have downloaded from cisco.com, you can calculate a SHA512 checksum and verify that it matches with the one listed on the software download page. To find the checksum, hover the mouse pointer over the software image you have downloaded.

At the bottom you find the SHA512 checksum, if you do not see the whole checksum you can expand it by pressing the "..." at the end. 
To calculate a SHA512 checksum on your local desktop please see below.

#### SHA512 checksum calculation command examples

Microsoft Windows

Open a command line window and type the following command:

```
> certutil.exe -hashfile filename.k3.cop.sgn SHA512
```

macOS

Open a terminal window and type the following command:

```
$ shasum -a 512 filename.k3.cop.sgn
```

Linux

Open a terminal window and type the following command:

```
$ sha512sum filename.k3.cop.sgn
Or
$ shasum -a 512 filename.k3.cop.sgn
```

If the SHA512 checksum matches, there is a high level of certainty that no one has tampered with the software image or the image has not been corrupted during download.

If the SHA512 checksum does not match, we advise you to not attempt upgrading any systems with the software image. Download the software again and verify the SHA512 checksum again. If there is a constant mismatch, please open a case with the Cisco Technical Assistance Center.

Note:
You should always use the “.cop” file when upgrading the devices listed above. Upgrading using “.pkg” on these devices will leave the device unable to upgrade the peripherals and you may experience error messages regarding software mismatch after upgrade. Such issues could happen if you used the “.pkg” extension when upgrading the device from UCM or in other ways. To resolve this, upgrade the software again using the “.cop” file. Cisco only release “.cop” files for RoomOS 10 and above.

Upgrade using the web interface

Access the web interface of the device on:

https://codecIP/web/software

Upload the correct software package by following the instructions on the web page. The upgrade will start, and the device will reboot with the new software.

If you are on a software version before CE9.9.1 or CE9.8.2 you may experience a file size warning if the file you are uploading are larger than 1GB. If you experience this, please upgrade using one of the other methods described below.

Upgrade using UCM

Install the appropriate “.cop” file containing the software for the device platform you wish to upgrade according to the cop installation process on UCM.

Go into the device default loads on the UCM administration page and make sure the platform has populated the correct filename.

For Cisco Room devices s53200 and s53300, the load file name should not contain any extension at all if the device is running software >= CE9.8.2. For example:

Platform Specific packages: s53200ce10_X_X_X.pkg ( wrong ) s53200ce10_X_X_X ( correct )

All products (containing all software versions for all products): ce10_X_X_X ( correct )

If the device is running software lower than CE9.8.2 the above method may not work, please use the xAPI method to upgrade. See below.

Upgrade using TMS

Upload the software to TMS according to the TMS instructions of software upgrade.

Upgrade using the xAPI

If none of the above methods are applicable, you can use an existing HTTP server or setup a HTTP server that is reachable by the device(s) you want to upgrade.

Log into the xAPI CLI using SSH or Serial. Type the following command to initiate the upgrade:

```
xCommand SystemUnit SoftwareUpgrade URL: http(s)://yourHTTPserver/path/to/file
xCommand SystemUnit SoftwareUpgrade URL: http(s)://yourUCMserver:6970/file
xCommand SystemUnit SoftwareUpgrade URL: http(s)://yourTMSserver/public/path/to/file
```

The device will download the software package and upgrade without warning. If you want the user to be warned and postpone the upgrade, add the parameter: “Forced: False” to the command as the default is “Forced: True” .

Note: If the above methods do not work or the upgrade is failing because the software is too old, please find the "step upgrade" file on the product page on Cisco.com . Upgrade the device using the step upgrade file, then upgrade the device again with the desired RoomOS software version.

### Downgrading

Downgrading is performed the same way as described above, using a software version lower than the one you are currently running. Not all products are compatible with all software versions. Please verify the minimum software version in the compatibility matrix before downgrading or upgrading your product.

If you are planning to downgrade to a version lower than the one you are currently on, make sure your compatibility level is mentioned in the release note of that version with a minimum version. For example downgrading from RoomOS 11 to RoomOS 10. If the compatibility level of your device is listed with a version of RoomOS 10, then it will be supported from that version. If the number is not mentioned with a version of RoomOS 10 but only RoomOS 11, then the device cannot be downgraded. Check the respective release note of the version you are downgrading to as we do not mention previous version compatibility levels in newer versions of the release notes.

When downgrading from RoomOS 10 to CE9.12.x or lower, the provisioning mode setting will reset to the default value even if the setting exists on both versions. The workaround is to manually configure the provisioning mode after downgrade.

## Software deferral policy

A software version is deferred when we find critical issues within the software. This is to prevent users from downloading and installing affected software versions. Replacement software will always be in place before a software version is deferred.

Older software versions will be deferred on a regular basis from the download section on https://www.cisco.com to avoid providing potential vulnerable software after security fixes. As a general rule you will be able to download the latest release and the version before. Older software versions will be removed from cisco.com regularly. Cisco always recommend using the latest available software.

Example:

RoomOS 10.X.Y.z = Major.Minor.Patch.Buildnumber

For RoomOS versions that has been provided by the Webex cloud, "Y" will always be 1 (10.X. 1 .z) while a RoomOS version released to cisco.com the same number will always be higher than 1 and will increment by one for each patch release.

If for example, RoomOS 10.3.2.x and RoomOS 10.6.2.x is released and RoomOS 10.9.2.x becomes available. RoomOS 10.3.2.x may be removed as part of the deferral policy for end of support. A minor software version is typically supported for two release cycles (6-9 months).

Cisco supports the latest minor release and the previous minor release (i.e. RoomOS 10.3.2.x) and the newest (i.e. RoomOS 10.6.2.x) per product as a general rule.

Exceptions are made if supported hardware or particular feature deployments are depending on a major release. Deferral of older maintenance releases still applies.

## Deferred software

## Open and resolved caveats in RoomOS 10

### Using the Bug Search Tool

You can use the Bug Search Tool to find information about caveats (bugs) for this release, including a description of the problems and available workarounds. The Bug Search Tool lists both open and resolved caveats. No subset of open or resolved bugs will be listed in the release notes unless deemed relevant for a particular software version.

A pre-defined link will provide the correct list of all open or resolved bugs. Please note that the "Series/Model" listed in the pre-defined search is universal and will list all relevant bugs relating to all products that runs RoomOS Software.

Please refer to the release summary for a link to open and resolved bugs under the specific release.

To use the Bug Search Tool, follow these steps:

- Step 1 Access the Bug Search Tool by navigating to https://bst.cloudapps.cisco.com/bugsearch/

- Step 2 Log in with your Cisco.com user ID and password

- Step 3 To look for information about a specific problem, enter the bug ID number in the ‘Search for bug ID’ field, then click ‘Go’

## Known limitations and advisories for RoomOS 10

### Resource consumption

Extended Logging Extended logging is a troubleshooting feature and will consume a high amount of resources when enabled. Enabling extended logging can generate unexpected behavior in production calls and in rare cases, cause the device to crash due to resource consumption. This feature should therefore only be enabled in short periods if higher data collection is required when reproducing issues for example, in cooperation with Cisco TAC.

Network Congestion Anything that degrades network performance can affect voice and video quality and, in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

- Administrative tasks such as an internal port scan or security scan

- Attacks that occur on your network, such as a denial-of-service attack

To reduce or eliminate any adverse effects to conferences, schedule any administrative network tasks during a time when the Cisco Room system is not being used, or exclude the Cisco Room systems from the testing.

### Wi-Fi Connection

Due to compliance regulations, it is required to enable 802.11d in access points for the product to operate properly within 5725 MHz – 5875 MHz. As Wi-Fi connections can be used as a flexible option, an Ethernet connection is always preferred for high performance.

WPA-EAP There is currently no diagnostic message for expired certificates

CA Certificates CA certificates must be uploaded per endpoint. There is currently no way to mass-distribute certificates to endpoints running software version < CE9.2.1. Please also note that the endpoint must be connected to a wired or WPA2-PSK wireless network in order to upload a certificate before attempting to connect to a WPA-EAP enabled network that requires a CA certificate.

Devices flagged with "NR" (No Radio) do not have Wi-Fi capability.

Network paired Cisco Touch 10 not supported when the video system is connected through Wi-Fi Even though this connectivity works, you may end up in cumbersome scenarios if the Wi-Fi connectivity is lost for any reason, for example when the Wi-Fi password is changed. In order to reconfigure the Wi-Fi connection, you need to setup a direct pairing between the video system and the Touch 10 before reconnecting the Cisco Touch 10. When the video system is using Wi-Fi connectivity Cisco recommends that you have the Touch 10 directly paired with the video system.

### Cisco Webex and Cisco Webex Edge for Devices

Pairing Cisco Touch 10 or Room Navigator To activate a system on Webex Teams with a LAN paired Cisco Touch 10 or Cisco Room Navigator panel, you must pair the touch device before you activate the system on Webex Teams.

Note: In newer versions you can now create new user accounts to pair the touch device after registration. 
We recommend that you upgrade to the latest available RoomOS version before activating your device on Webex Teams.

From RoomOS 10.11 (January 2022) we have support for PIN pairing of touch panels that can be initiated from Webex Control Hub.

Encryption is required to activate a Room Device on Webex A Room Device with support for encryption is required to activate the device on Webex and Webex Edge for Devices. Cisco Room Devices with the K7 flag in the partnumber, do not have support for encryption and cannot be registered or linked to Webex. Encryption support for Cisco Room Devices are determined by hardware and are not using encryption option keys.

If the device do not have the encryption option, then the device is a K7 device. Devices flagged with K9 in the partnumber have support for encryption.

You can check if the device have the encryption option key from the web interface under "option keys". This key can neither be added or removed as it is based on the hardware model you have with K7 (no crypto) or K9 (crypto) notation.

### Peripherals

Cisco Touch 10

An area may appear dead on the Cisco Touch 10 controller’s screen if this area has been touched during start-up of the panel. In the start-up phase, a touch calibration process takes place. If something is in contact with the touch panel at this time, this area may lose its function until the Touch 10 has been restarted. Do not touch the touch panel during boot to avoid this.

Max processed requests per second: Authenticated (for example POST to /putxml with basic authentication): 1 (queue 30)

Using session cookies (for example being logged in to the web interface via a browser): 15 (queue 90)

To explain what these numbers mean, let’s take for example the "authenticated" method: If you send 30 authenticated HTTP requests at once, it will take minimum 30 seconds before you get a response to the last request. If you send 31 requests, assuming all is coming in at the same time, the 31st request will get a http 503 response.

If you hit the rate-limiting (max requests per second), the request is queued until others are processed. This happens until the queue is full, and then new requests will get a HTTP 503 response instead of being queued.

Logs will show when the requests are being rate limited.

All content is considered as HDCP when enabled When the input has been configured to support HDCP, it will consider anything connected to this input as HDCP content, even if it´s not. This will prevent you from sharing content from this port in a call. You can share anything locally the same way as before but note that on a dual screen device you may only see content on one screen. Check if your room device has support for one or two HDCP outputs.

## Interoperability for RoomOS 10

The interoperability section describes the equipment and software revisions that have been tested for interoperability with this release. Please note: The absence of a device or revision from this section does not imply a lack of interoperability.

## Camera firmware and support

Note: The camera firmware has parity with the version installed on the Room Device. Camera software for Cisco Quad Camera, Cisco TelePresence Precision 60 and Cisco TelePresence SpeakerTrack 60 will automatically be updated when the Room Device is upgraded or downgraded. The camera firmware should share the same hash as the current software installed on the Room Device.

Third party cameras

Third-party and older cameras may work with our Integration Room Devices but this is not tested and functionality cannot be guaranteed. TAC support may be rejected or limited.

## Cisco collaboration certification program

Cisco collaboration devices partner ecosystem is built on our certification program to ensure that customers get the best experience out of their Cisco collaboration devices and make integration as seamless as possible when integrating with third-party technology.

For more information, click here

HDMI Cable quality Cisco recommends use of high-quality HDMI 2.0 certified cables. Lower quality cables may work but may also have an impact on the image quality.

If you experience problems and do not have access to high quality cables, try using shorter HDMI cables.

## xAPI Changes

We recommend endpoint configuration through the web interface and not from the xAPI command line.

The admin user has access to only a subset of relevant commands and configuration from the xAPI. The admin user can fully manage the system from the web interface where all the configurations are available. The "remotesupport" user has access to the full list of xAPI commands when utilized (requires TAC engagement).

Specific xAPI changes are not published in the release notes. Please refer to the Cisco API Reference Guides for the integrator products at the following locations:

Cisco Room Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-command-reference-list.html

Cisco Boards: https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-board/products-command-reference-list.html

Please also visit https://roomos.cisco.com for a great overview of the xAPI and other resources.

## Hardware revision and software dependencies

Due to occasional updates to hardware components, there can be constraints on running older software on newly manufactured Room Devices.

To identify a Room Device compatibility level, you can access the web interface of the Room Device and click on Settings > Statuses. Scroll down to the compatibility level on this page. The below tables can be used to identify software constraints based on the compatibility level of your endpoint. Downgrading to an unsupported software version will fail. 
The latest software release is backward compatible with previous hardware revisions.

Note: When "all" is mentioned as the minimum version it is referring to all software versions of RoomOS 10 that is or has been released on https://www.cisco.com .

## Cisco Room Series software compatibility matrix

## Cisco Board Series Software Compatibility Matrix

## Cisco Desk Series Software Compatibility Matrix

## Cisco Peripheral Software Compatibility Matrix

Cisco peripheral software compatibility refers to touch devices and cameras that are requesting software from the Room Device. Some of the peripherals may require a higher software version than the Room Device is currently running.

Touch devices

If you see an error on the touch screen about the software not being compatible with the current software, please upgrade the Room Device software to the latest available version and try again.

Cameras

Notes for Cisco Quad Camera

Systems that support Quad Camera are Cisco Codec Pro, Codec Plus, Room 70 and Room 70 G2 (single / dual).
Hardware revisions of the Quad Camera can be identified using xStatus.

Example:

```
xStatus: Peripherals ConnectedDevice XXXX HardwareInfo: "73-100746-1".
```

Notes for Cisco TelePresence Precision 60

Systems that support Cisco TelePresence Precision 60 with RoomOS 10 is Cisco Codec Pro, Codec Plus, Room 70 and Room 70 G2 (single / dual).

New hardware revisions of the Cisco TelePresence Precision 60 camera are identified by production date printed on a sticker underneath the base. If there no sticker is present and you still see an error message on screen about the camera not being compatible with the current software version, please upgrade the room device to the latest software.

Notes for Webex PTZ 4K

The camera setup switch is for selecting the video signal format to be "output" from the HDMI OUT terminal. This should always be set to 6 in order to be controlled by the Room Device.

For more information about the Webex PTZ 4K Camera, please follow this link .

## Cisco Terms of Service

Your use of Cisco software and cloud services are subject to these terms and conditions

Your use of Cisco APIs is subject to the Cisco Webex Developer Terms of Service

## Permitted Commercial Use for Scheduled Meeting Join Experience

The following use case requires separate permission for commercial use:

Providing a scheduled meeting join experience like one button to push.

This includes use of any API that updates the device with calendar data from an external source to provide this functionality including ´xCommand Bookings Put´ or previous private API’s such as ´bookingsputxml´ In addition, using other APIs to accomplish the same functionality would also require permission for commercial use.

If you are providing a Scheduled Meeting Join Experience you either must comply with the below permitted commercial use terms or it must be for non-commercial use. Non-commercial use is defined as being solely for your internal business operations only and not for any activities that involve you using the API as part of or in furtherance of an income-generating service or product, whether directly or indirectly.

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
| 23 | July 30th 2024 | Release of RoomOS 10.19 Step Upgrade Package RoomOS 10 is deprecated and this release note is kept for historical reference. |
| 22 | September 21st 2023 | Minor corrections |
| 21 | July 7th 2023 | Software deferral |
| 20 | May 12th 2023 | EOS announcement for RoomOS 10 |
| 19 | March 17th 2023 | Release of Cisco RoomOS 10.19.5.6 7cd166d6be0, patch |
| 18 | January 25th 2023 | Release of Cisco RoomOS 10.15.5.3 9f26a1da03d, patch |
| 17 | December 8th 2022 | Release of Cisco RoomOS 10.19.4.2 1cadf49eefd, patch |
| 16 | October 20th 2022 | Release of Cisco RoomOS 10.19.3.0 bb11ddae620, patch |
| 15 | October 10th 2022 | Deferral of Cisco RoomOS 10.19.2.2 |
| 14 | September 29th 2022 | Release of Cisco RoomOS 10.19.2.2 7c9a4721f0d, minor |
| 13 | September 9th 2022 | Release of Cisco RoomOS 10.15.4.1 a4d3db640f0, patch Release of Cisco RoomOS 10.11.6.0 cb912c2adbe, patch |
| 12 | July 6th 2022 | Release of Cisco RoomOS 10.15.3.0 7c44f1ceb87, patch |
| 11 | June 17th 2022 | Release of Cisco RoomOS 10.15.2.2 5c5c0acc9e0, minor |
| 10 | May 19th 2022 | Release of Cisco RoomOS 10.8.4.0 dc63a82915b, patch |
| 9 | April 12th 2022 | Release of Cisco RoomOS 10.11.5.2 f6c72c48bd7, patch |
| 8 | March 18th 2022 | Release of Cisco RoomOS 10.11.4.1 99a0337a074, patch |
| 7 | March 3rd 2022 | Release of Cisco RoomOS 10.11.3.0 6426fe09359, patch |
| 6 | February 3rd 2022 | Release of Cisco RoomOS 10.11.2.2 4d365f74e2c, minor |
| 5 | December 14th 2021 | Release of Cisco RoomOS 10.8.3.1 6d131e0418f, patch |
| 4 | November 17th 2021 | Release of Cisco RoomOS 10.3.4.0 e47befa1e68, patch |
| 3 | October 27th 2021 | Release of Cisco RoomOS 10.8.2.5 ed4f9434f88, minor |
| 2 | June 24th 2021 | Release of Cisco RoomOS 10.3.3.0 e383f779e98, patch |
| 1 | April 29th 2021 | Release of Cisco RoomOS 10.3.2.0 85049347ae0, major |

| Cisco Room Series |
|---|
| Cisco Room USB, Room Kit Mini, Room Kit, Room Bar, Room 55 Cisco Codec Plus, Codec Pro Cisco Room 55 Dual, Room 70 (Single/Dual), Room 70 G2 (Single/Dual) Cisco Room Panorama, Room 70 Panorama |
| Cisco Board Series |
| Cisco Board 55/55S, 70/70S and 85S Cisco Board Pro 55 and 75 |
| Cisco Desk Series |
| Cisco Desk, Desk Limited Edition, Desk Pro, Desk Mini and Desk Hub |

| What | Description |
|---|---|
| Current limitations with RoomOS 11 UI Experience (10.19) | Creating and editing camera presets currently has to be done via the xAPI Room booking functionality (inside rooms) is not yet supported. Room signage on multi-screen systems shows on one screen only People focus works on single screen systems only No support yet for video stitching and video matrix Board Pro not supported in companion mode yet Room Panorama, Room USB, and Samsung Flip not supported yet Classroom/briefing room/presenter track features not supported yet Unbind feature missing from Room Navigator Barging shared line calls and remote resume is not supported Broadcast / Unobstructed mode is not supported yet Snap to whiteboard is not supported and is not planned for implementation in RoomOS 11 |
| xAPI | xCommand UserInterface Extensions: Clear / Panel Remove | Not working on touch controller, so no method of removing extensions |
| xCommand UserInterface Message Alert Display | Alert shows up only on controller. Should be visible on both controller and screen. |
| xCommand UserInterface Message TextInput Display | TextInput: not able to see what you are typing as the keyboard pops up and input field disappears. Padding is incorrect. |
| xCommand UserInterface Message TextLine Display | TextLine only visible on controller. It should only be shown on passive screen. On Desk Series TextLine disappears when you tap the screen. |
| xCommand Video Selfview Set OnMonitorRole: Second/third | Doesn't move selfview to second and third screen. |
| xConfiguration Audio Input ... VideoAssociation | Inputs not muted if associated video input is not shown in any layout. |
| xConfiguration Video Selfview Default OnMonitorRole | Not able to move fullscreen selfview from screen 1. Not able to move selfview pip from screen 1. |
| xStatus Video Selfview | Selfview xstatus is not always in sync with the actual selfview state. |
| Work in Progress | xCommand Video Matrix xCommand Presentation Start PresentationSource: n PresentationSource: o PresentationSource: p xConfiguration UserInterface Accessibility IncomingCallNotification xConfiguration UserInterface OSD Mode xConfiguration UserInterface OSD Output xConfiguration UserInterface Security Mode: Strong xConfiguration UserInterface SettingsMenu Visibility xConfiguration Video Presentation DefaultPIPPosition xConfiguration Video Selfview Default Mode xConfiguration Video Selfview OnCall Mode/Duration |

| Known working USB microphones |
|---|
| Blue Microphones Yeti Nano Blue Microphones Yeti Rode NT-USB Mini Shure MV7 MXL ac-404 |
| Known working USB Audio Interfaces |
| Audient EVO4 Roland UA-25EX Audinate Dante USB I/O Module Shure INTELLIMIX P300 Shure ANIUSB-MATRIX M-Audio M-TRACK SOLO Extron dmp 128 plus |

| The following devices and older are not supported with RoomOS 10: |
|---|
| Cisco TelePresence SX10, SX20, SX80 |
| Cisco TelePresence DX70, DX80 |
| Cisco TelePresence MX700, MX800, MX800 Dual, MX200 G2, MX300 G2 |

| Device | Software platform identifier | Latest available RoomOS software |
|---|---|---|
| Cisco Codec Plus, Room USB, Room Kit Mini, Room Kit, Room 55, Room 55 Dual, Room 70, Board Series (except Webex Board Pro 55 and 75) | s53200 | cmterm-s53200ce10_19_5_6.k3.cop.sgn cmterm-s53200ce10_19_5_6.k4.cop.sha512 * |
| Cisco Codec Pro, Room 70 G2, Room 70 Panorama, Room Panorama, Desk Series (except Cisco Desk, Desk Mini and Desk Hub) | s53300 | cmterm-s53300ce10_19_5_6.k3.cop.sgn cmterm-s53300ce10_19_5_6.k4.cop.sha512 * |
| Cisco Desk, Desk Mini, Room Bar and Cisco Board Pro 55 and 75 | s53300 | cmterm-s53300ce10_19_5_6-l4t.k3.cop.sgn cmterm-s53300ce10_19_5_6-l4t.k4.cop.sha512 * |
| Cisco Desk Hub | s53400 | cmterm-s53400ce10_19_5_6.k3.cop.sgn cmterm-s53400ce10_19_5_6.k4.cop.sha512 * |
| All products | N/A | cmterm-ce10_19_5_6.k3.cop.sgn cmterm-ce10_19_5_6.k4.cop.sha512 * |
| Follow this link to find and download software for the Room Device you are about to upgrade. * .cop.sha512 cop files are used with UCM 14 and above ** Cisco Desk, Desk Mini and Webex Board Pro 55 and 75 requires s53300 l4t package. |

| Deferral date | Versions | Note |
|---|---|---|
| July 30th 2024 | 10.19.4.2 10.19.5.6 | Deferred according to policy (end of support for RoomOS 10) |
| July 7th 2023 | 10.19.3.0 10.15.2.2 10.15.3.0 10.15.4.1 10.15.5.3 | Deferred according to policy (end of support for RoomOS 10.15) |
| October 10th 2022 | 10.19.2.2 | Deferred due to a bug causing Room Navigators to not connect to the codec after upgrade. See CSCwd23669 |
| September 29th 2022 | 10.11.4.1 10.11.5.2 10.11.6.0 | Deferred according to policy (end of support for RoomOS 10.11) |
| September 9th 2022 | 10.8.4.0 10.8.3.1 10.8.2.5 | Deferred according to policy (end of support for RoomOS 10.8) |
| May 5th 2022 | 10.3.2.0 10.3.3.0 10.3.4.0 10.11.2.2 10.11.3.0 | Deferred according to policy (end of support for RoomOS 10.3) |

| Feature / equipment | Limitations and advisories |
|---|---|
| Unified CM | H.323 and SIP consideration when provisioned by CUCM When using CUCM provisioning, the endpoint cannot register to a VCS (SIP or H.323) at the same time. This use-case is not supported. When             CUCM provisioning is active, H.323 mode is disabled. We recommend TelePresence customers to migrate from H.323 to SIP. 
Please note that being registered to CUCM without having provisioning mode set to “CUCM” is not a supported scenario. NTP The collaboration endpoints do not support broadcast NTP servers from CUCM, unicast only. |
| SIP / H323 | SIP Listen Port diagnostics warning When registered to a SIP proxy and SIP Listen Port is enabled, a diagnostics warning will be displayed in the web interface “SIPListenPortAndRegistration”. We recommend that SIP Listen Port is turned off when registered to a SIP proxy Dual protocol enablement for SIP and H323 is not supported Having SIP and H323 enabled at the same time will generate a warning message on-screen indicating that having both protocols enabled (SIP and H323) is not supported. This message cannot be removed unless you disable one of the protocols. Having both protocols enabled and using them at the same time in different scenarios may introduce unexpected behavior. TAC will not support call scenarios where both protocols are enabled. |
| Cisco Intelligent Proximity | Please refer to the Cisco Support Forums for questions and support If you have issues with Cisco Intelligent Proximity, read the Cisco Proximity troubleshooting guide |
| Web interface | HTTP Rate limiting To increase device stability and security rate limiting is in effect on the Room Devices. Max processed requests per second: Authenticated (for example POST to /putxml with basic authentication): 1 (queue 30) Using session cookies (for example being logged in to the web interface via a browser): 15 (queue 90) To explain what these numbers mean, let’s take for example the "authenticated" method: If you send 30 authenticated HTTP requests at once, it will take minimum 30 seconds before you get a response to the last request. If you send 31 requests, assuming all is coming in at the same time, the 31st request will get a http 503 response. If you hit the rate-limiting (max requests per second), the request is queued until others are processed. This happens until the queue is full, and then new requests will get a HTTP 503 response instead of being queued. Logs will show when the requests are being rate limited. |
| SNMP | The Collaboration Endpoint Software is configured with the default SNMP community strings. SNMP community strings should be treated as credentials, and therefore these must be changed after initial configuration. RoomOS 10 only has basic support for SNMPv2 with default MIB only. |
| Security | The codecs shipped with RoomOS 10 software do not meet the Cisco standard passphrase policy. Cisco recommends users to set a passphrase on the system when installed to avoid the system from being compromised. This issue will be addressed in a future release. |
| PresenterTrack | PresenterTrack is disabled in MultiSite calls The PresenterTrack feature is not available in MultiSite calls. 
Note that PresenterTrack will work in a Dual Screen call with CMS from CE9. Trigger zone configuration There is a known limitation when configuring the trigger zone through the web interface; whenever the blue square is moved around and placed the trigger zone will be saved (regardless if the "save" button is pressed or not. The blue square that is displaying in the self-view on the endpoint do not disappear until the configuration has been saved manually from web or activate the PresenterTrack preset from the Touch interface. |
| SpeakerTrack | Face masks SpeakerTrack (Quad Camera and integrated cameras, for example on Room Kits) with the Cisco Room Series has been improved with an additional “head detector” that will detect the head instead of the face. Note that this may also increase the frequency of detecting objects with a “head” in the room. This functionality will give an improved experience in a meeting where the people in the room are wearing face masks. |
| Startup Wizard | While the Startup Wizard is active the system will have “Do Not Disturb” mode enabled by design. The DND mode cannot be turned off while the Startup Wizard is active. To remove the Startup Wizard, finish the Startup Wizard normally by following the steps or turn off the “RunStartupWizard” by setting the value to “False”. If the Startup Wizard is active, a diagnostics message will be active in the web interface with a link to the configuration to turn it off. This should only be done by advanced users that wants to configure the system manually. |
| Custom wallpaper and branding | A system using custom wallpaper will not display on-screen elements for example, custom branding, the clock, today’s bookings or One Button to Push. This limitation is intentional as we do not know how these elements will appear on customized wallpapers. |
| Audio Console | You need to create equalizers through the xAPI as you are only able to select between equalizers in the Audio Console UI and not create them. When adding HDMI input connectors that have set “Mute on inactive video”, it will look like it has not been added the first time and needs to be added a second time. The settings will update live when configuring the Audio Console but will not be stored in a macro until it is saved. If you do not save the Audio Console setup it will get lost if you reboot the device. |
| HDCP | Device is not entering standby
If you connect for example, a Google Chromecast, the device will not be able to enter standby because the standby activity makes the Chromecast send “Active” signal to the codec forcing it to wake up again. All content is considered as HDCP when enabled When the input has been configured to support HDCP, it will consider anything connected to this input as HDCP content, even if it´s not. This will prevent you from sharing content from this port in a call. You can share anything locally the same way as before but note that on a dual screen device you may only see content on one screen. Check if your room device has support for one or two HDCP outputs. |
| Layout controls in Webex meetings | Layout control for on-premises devices in Webex Calls On-premises devices that are calling into Webex meetings will currently not have the same control options of the meeting that a Webex registered / linked device have. There are still some actions that are available through DTMF tones. Please visit https://help.webex.com/en-us/nli1uz4/DTMF-Commands-for-Video-Device-Enabled-Cisco-Webex-Meetings for a list of valid DTMF tones that can be sent to the Webex meeting to invoke certain actions. |
| Immersive share | Camera LED is not lit when immersive share is enabled You will see yourself on the screen as an indication of being filmed by the camera. This limitation will be resolved in a future release and is valid for Cisco Desk Pro and Desk Limited Edition. |
| Cisco Room Navigator | Keyboard clicks inaudible on some units Some units will not produce audible key clicks when tapping on the keyboard. This is not an issue from RoomOS 10.8.2.5. |
| Cisco Room Panorama | Cisco Precision 60 camera Cisco Room Panorama do not have support for Precision 60 cameras. Please note this when upgrading a Room 70 into a Room 70 Panorama, in case you have one connected and want to keep using it. |
| Encryption and Ciphers | Supported Ciphers You can check which ciphers that the device supports for its different services (HTTPS Server, SIP TLS, Syslog TLS, HTTPS Client) by typing xCommand Security Ciphers List in the xAPI. The supported ciphers may change between versions. |

| H323 gatekeepers / traversal servers | Minimum software |
|---|---|
| Cisco TelePresence System Video Communication Server (VCS) | Latest version available |
| SIP registrars / proxy servers |
| Cisco TelePresence System Video Communication Server (VCS) | Latest version available |
| Unified CM | 10.5 For device support, please make sure you have the latest UCM device pack for your version installed. |
| MCU Interoperability |
| Cisco Meeting Server (CMS) | 2.8 For the latest conferencing features available in CMS, the latest available software is always recommended. |
| Cisco TelePresence Server 7010 Virtual TelePresence Server Cisco TelePresence Server MSE 8710 Cisco MCU 53xx Cisco MCU 42xx Cisco MCU 45xx | Latest version available |
| Management server interoperability |
| TelePresence Management Suite | Latest version available |

| Room Device | Camera | Comments |
|---|---|---|
| Cisco Codec Pro | Cisco TelePresence Precision 60 | Full support |
| Cisco Quad Camera | Full support |
| Cisco TelePresence SpeakerTrack 60 | Full support |
| Webex PTZ 4K | Full support |
| Sony SRG-120DH Sony EVI-120DH | Pairing over IP and basic usage with pan tilt and zoom functionality is supported, Camera firmware update is not supported. |
| Cisco Room Codec Plus | Cisco TelePresence Precision 60 | Full support |
| Webex PTZ 4K | Full support |
| Sony SRG-120DH Sony EVI-120DH | Pairing over IP and basic usage with pan tilt and zoom functionality is supported, Camera firmware update is not supported. |
| Cisco Quad Camera | Full support |
| Cisco TelePresence SpeakerTrack 60 | Full support |

| Device | Compatibility level | Minimum version of RoomOS 10 |
|---|---|---|
| Cisco Room Kit |
| 0-2 | All |
| 3 | 10.19.2.2 |
| Cisco Codec Plus | 0-2 | All |
| Cisco Room 55 Dual | 0-2 | All |
| Cisco Room 70S/70D | 0-2 | All |
| Cisco Codec Pro | 0-2 | All |
| Cisco Room 70/70D G2 | 0-2 | All |
| Cisco Room Kit Mini | 0 | All |
| Cisco Room USB | 0 | All |

| Device | Compatibility level | Minimum version of RoomOS 10 |
|---|---|---|
| Cisco Board 55 | 0 | All |
| Cisco Board 70 | 0 | All |
| Cisco Board 55S | 0 | All |
| Cisco Board 70S | 0 | All |
| Cisco Board 85S | 0 | All |
| Cisco Board Pro 55 | 0 | 10.11.2.2 |
| Cisco Board Pro 75 | 0 | 10.11.2.2 |

| Device | Compatibility level | Minimum version of RoomOS 10 |
|---|---|---|
| Cisco Desk Pro | 0-2 | All |
| Cisco Desk Limited Edition | 0-2 | All |
| Cisco Desk |
| 0 | 10.8.2.5 |
| 1 | 10.8.3.1 |
| 2 | 11.1.2.4 |
| Cisco Desk Mini |
| 0 | 10.11.2.2 |
| 1 | 10.15.3.0 |
| 2 | 11.1.2.4 |

| Device | Compatibility level | Minimum version of RoomOS 10 |
|---|---|---|
| Cisco Touch 10 | 102300-3 102310-0 102310-1 | All |
| Cisco Room Navigator | 101864-0 101864-1 | All |

| Device | Compatibility level | Minimum version of RoomOS 10 |
|---|---|---|
| Cisco Quad Camera | 73-100746-0 73-100746-1 73-100746-2 73-100746-3 | All |
| Cisco TelePresence Precision 60 | 2018/07 and earlier 2018/08 and later | All |
| Webex PTZ 4K | N/A | All |