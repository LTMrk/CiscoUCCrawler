---
doc_id: help-webex-com-en-us-article-ml8pm7-cisco-desk-camera-4k-release-notes-3291ab76ca
source_url: https://help.webex.com/en-us/article/ml8pm7/Cisco-Desk-Camera-4K-release-notes
retrieved_at: 2026-09-01T20:08:41.621488+00:00
---

- New features

- Open and resolved bugs

- Known limitations

## June 17, 2023

Firmware Release 2.5(1.34)

This is a maintenance release with some fixes.

For the fixes, see the Resolved bugs list in the Open and resolved bugs section.

## April 12, 2023

Firmware Release 2.5(1.16)

This is a maintenance release with some fixes.

For the fixes, see the Resolved bugs list in the Open and resolved bugs section.

## October 18, 2022

Firmware Release 2.5(1.8)

This is a maintenance release with some fixes incremental to 2.5(1.4).

For the fixes, see the Resolved bugs list in the Open and resolved bugs section.

Firmware Release 2.5(1.4)

Cisco Desk Camera 4K with Firmware Release 2.5(1.4) has been certified for Microsoft Teams. All releases later than 2.5(1.4) are by default Microsoft Teams certified.

## March 24, 2022

Firmware Release 2.4(1.1) contains some fixes and no new features.

For the details about the fixes, see Resolved bugs .

## September 30, 2021

Firmware Release 2.4(1) contains the following new features:

Best Overview

Best overview ensures that you’re properly framed in your video, even if you move about your workspace. Use this feature if you often move around during your meetings.

By default, this feature is disabled. You can enable it from the Cisco Accessory Hub desktop app.

Saturation Setting

Saturation setting allows you to control the vividness of your image so you always look your best. You can adjust the setting from the Cisco Accessory Hub desktop app.

New Color Theme for the Camera App

We changed the Cisco Accessory Hub desktop app interface to dark color mode. Update your camera app to the latest version to experience the new user interface. This change doesn't need any configuration.

## August 9, 2021

Firmware Release 2.3(1.1) contains the following improvements:

Improved Camera App Restart

This enhancement for the Cisco Webex Desk Camera app allows you to return to work even quicker. It will take less than ten seconds for the app to restart after the next update.

This improvement doesn't require any configuration.

Improved Camera Firmware for Manufacturing

This improvement is for manufacturing only and has no impact on users.

## June 1, 2021

Firmware Release 2.3(1) contains the following improvements:

Camera Firmware and App Update

You can use the Updates button on the Cisco Accessory Hub desktop app and easily update both your camera firmware and your camera app.

Improvements on Autofocus and Image Noise Reduction

In this release, we deliver image quality improvements including autofocus and image noise reduction. This improves your video experience in different workspaces and light conditions.

## February 2021

Cisco Desk Camera 4K is launched with Firmware Release 2.2(1).

Open bugs of severity 1 to 4

Resolved bugs of severity 1 to 4

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time new firmware is released.

Before you begin

An internet connection

A web browser

A Cisco.com username and password

Open the Bug Search Tool .

Sign in with your Cisco.com username and password.

Enter the bug ID number in the Search for field and press Enter .

What to do next

Open bugs

There are no unresolved bugs in the most recent firmware release.

Resolved bugs

### June 17, 2023

Version 2-5-0101-34

We resolved the following issues in this release:

CSCwf43440 Video Tearing at bottom of screen with 4K camera

- CSCwf23093 After login back on a Windows Hello Facial Recognition enabled computer, cannot restart video.

### April 3, 2023

Version 2-5-0101-16

We resolved the following issue in this release:

- CSCwe69895 Can't use 4k camera with WeChat on Windows

### October 18, 2022

Version 2-5-0001-8

We resolved the following issue in this release:

- CSCwd28731 (macOS) Can't go into sleep mode after open the PC Tool/Webex.

Version 2-5-0001-4

This is a baseline firmware release certified for Microsoft Teams and doesn't contain bug fixes.

### March 24, 2022

Version 2-4-0101-8

We resolved the following issues in this release:

CSCvz70222 Webex 41.8 blocks the camera app to set camera parameters on Mac

CSCvz22247 Camera app can't adjust parameters for camera on MacOS 12.0, both Intel and ARM chip

CSCwa68784 Best Overview adjustment should be perfectly smooth

### September 30, 2021

Version 2-4-0001-4

We resolved the following issues in this release:

CSCvz70225 Camera app Brightness adjustment range should be more narrow

CSCvz70226 The Saturation slider can't be reset to default

### August 9, 2021

Version 2-3-0101-7

We resolved the following issues in this release:

CSCvy90793 Desk app takes about 15-20 seconds to install the new version

CSCvz20781 Desk app can't detect the camera on Mac OS 12 beta and can't show preview neither

### June 1, 2021

Version 2-3-0001-7

We resolved the following issues in this release:

CSCvw63115 Users can see film grains/noise at black/grey objects area in the image or under low light condition.

CSCvx13115 When the camera doesn't detect human faces, auto focus jitters occur.

CSCvx28199 Camera app gets stuck as a blank white window(intermittent).

CSCvw61198 Camera app has high CPU utilization.

CSCvx17160 Sometimes the camera outputs video of low resolution720P@30fps

CSCvy22489 Cisco Webex Desk Camera Information Disclosure Vulnerability

CSCvy40854 Image quality improvements on Webex Desk Camera

CSCvy48934 Audio Tuning for Webex Desk Camera

Computer system requirements

The operation of the camera requires the computer to meet or exceed the minimum system requirements. For the detailed system requirements, see System Requirements for Cisco Desk Camera App .

The computers with low performance may cause the following problems:

On macOS, the live view mode at a 4K resolution through the Cisco Accessory Hub desktop app causes a high CPU usage.

If your computer is under a heavy load, lip sync, low frame rate, or video delay may occur in recordings or in meetings.

Limitation on specific laptops

When you connect Cisco Desk Camera 4K to an ASUS GL552V, ASUS Zenbook 15, or MSI laptop with the USB C-C cable, the laptop can't detect the camera. Always use the shipped USB C-A cable on these laptops.

Can't change the camera advanced settings on Webex App

You may not be able to configure the camera advanced settings on Webex App under the following conditions:

- You’re using the camera with Webex App version 42.11 or earlier on Windows OS.

- You have upgraded the camera firmware to version 2-5-0001-4 or later from version 2-4-0101-12 or earlier.

This issue happens because the Windows system cached the camera driver with the legacy device name—Cisco Webex Desk Camera. The camera name has been rebranded as Cisco Desk Camera 4K . The mismatch between the camera name and the driver name means that Webex App can't read the camera advanced settings.

To resolve this issue, reinstall the camera driver by following these steps:

- Go to Device Manager on your computer and uninstall Cisco Webex Desk Camera driver.

The system installs the new driver automatically.

- Verify that Cisco Desk Camera 4K is available in Device Manager.

| 1 | Open the Bug Search Tool . |
|---|---|
| 2 | Sign in with your Cisco.com username and password. |
| 3 | Enter the bug ID number in the Search for field and press Enter . |