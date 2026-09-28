---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-ip-phone-8800-series-multiplatform-firmware-220134-delete-use-628602d1d0
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/220134-delete-user-password-saved-in-mpp-device.html
retrieved_at: 2026-08-17T01:12:54.543900+00:00
---

Delete User Password Saved in MPP Devices

# Delete User Password Saved in MPP Devices

### Download Options

Updated: November 24, 2023

Document ID: 220134

Contents

## Contents

## Introduction

This document describes how to delete the local password on an MPP phone.

## Prerequisites

### Requirements

This document is not restricted to specific Multiplatform software and hardware versions.

## How to Delete the Local Password on an MPP Device

When you have a brand new MPP phone and you plug it for the first time,  it prompts you for a user password. This can be skipped or you can set it. You can also set or change the user password from the phone screen menu: Applications > Device administration > Set password . The user password is locally saved to the phone and Cisco does not handle it. This password allows you to set or change the password for access the phone web interfaces and the menus (such as Recent calls, Speed dials, User Preferences and Network configurations.) on the phone screen. You can notice that a local password was set in the phone if you see a padlock on the upper right corner.

## User Password Menu in Control Hub

If the phone is assigned to a user in Control Hub, you can disable the password by going to Devices > Select the device > Device Settings. Scroll down and find Show User Password Menu . Disable the toggle, then Save the changes.

After saving the changes go back to the Device, select Actions and Apply Settings.

Apply Changes

If you dont have a way to access to Control Hub to disable User Password Menu and you don`t know the User Password you must apply a factory reset.

If the phone is assigned to a user in Control Hub, after the factory reset it must try to register back again to Webex Calling. If the phone does not register back again please contact the Cisco Webex Calling TAC team.

## Related Information

- Factory reset your Webex Calling Multi Platform Phones

### Revision History

2.0

24-Nov-2023

Initial Release

1.0

11-Jan-2023

Initial Release

### Contributed by Cisco Engineers

Enrique Martinez

Technical Consulting Engineer

### Customers Also Viewed

- Place a Call on Hold with Call Park on a Cisco IP Phone 8800 Series Multiplatform Phone

### This Document Applies to These Products

- IP Phone 8800 Series

- IP Phone 8800 Series with Multiplatform Firmware

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 24-Nov-2023 | Initial Release |
| 1.0 | 11-Jan-2023 | Initial Release |