---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-english-userguide-cs78-b-conference-7832-user-guide-cucm-cs78-b--75bec89b58
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832/english/userguide/cs78_b_conference-7832-user-guide-cucm/cs78_b_conference-7832-user-guide-cucm_chapter_00.html
retrieved_at: 2026-08-21T01:50:28.661154+00:00
---

Cisco IP Conference Phone 7832 User Guide

# Cisco IP Conference Phone 7832 User Guide

Updated: August 25, 2017

Chapter: Your Phone

## Chapter: Your Phone

# Your Phone

## The Cisco IP Conference Phone 7832

The Cisco IP Conference Phone 7832 enhances people-centric communications, combining superior high‑definition (HD) audio performance and 360-degree coverage
                              for all sizes of conference rooms and executive offices. It provides an audiophile sound experience with a full-duplex two-way
                              wideband (G.722) audio hands-free speaker. The Cisco IP Conference Phone 7832 is a simple solution that meets the challenges of the most diverse rooms.

The phone has sensitive microphones with 360-degree coverage. This coverage lets users speak in a normal voice and be heard
                              clearly from up to 7 feet (2.1 m) away. The phone also features technology that resists interference from mobile phones and
                              other wireless devices, assuring delivery of clear communications without distractions.

G.711 a-law

G.711 mu-law

G.722

G722.2 AMR-WB

G.729a/G.729ab

G.726

iLBC

Opus

iSAC

Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone might cause interference. For
                                          more information, see the manufacturer’s documentation of the interfering device.

Cisco IP Phones provide traditional telephony functionality, such as call forwarding and transferring, redialing, speed dialing,
                              conference calling, and voice messaging system access. Cisco IP Phones also provide a variety of other features.

As with other network devices, you must configure Cisco IP Phones to prepare them to access Cisco Unified Communications Manager
                              and the rest of the IP network. By using DHCP, you have fewer settings to configure on a phone. If your network requires it,
                              however, you can manually configure information such as: an IP address, TFTP server, and subnet information.

Cisco IP Phones can interact with other services and devices on your IP network to provide enhanced functionality. For example,
                              you can integrate Cisco Unified Communications Manager with the corporate Lightweight Directory Access Protocol 3 (LDAP3)
                              standard directory to enable users to search for coworker contact information directly from their IP phones. You can also
                              use XML to enable users to access information such as weather, stocks, quote of the day, and other web-based information.

Finally, because the Cisco IP Phone is a network device, you can obtain detailed status information from it directly. This
                              information can assist you with troubleshooting any problems users might encounter when using their IP phones. You can also
                              obtain statistics about an active call or firmware versions on the phone.

To function in the IP telephony network, the Cisco IP Phone must connect to a network device, such as a Cisco Catalyst switch.
                              You must also register the Cisco IP Phone with a Cisco Unified Communications Manager system before sending and receiving
                              calls.

### Feature Support

This document describes all the features that the device supports. However, not all features may be supported with your current
                                 configuration. For information on supported features, contact your administrator.

## New and Changed Information

You can use the information in the following sections to understand what has changed in the document. Each section contains
                           the major changes.

### New and Changed Information for Firmware Release 14.1(1)

No user guide updates were required for Firmware Release 14.1(1).

### New and Changed Information for Firmware Release 14.0(1)

Feature

New or Changed

Hunt Group Enhancements

Recent Calls List

### New and Changed Information for Firmware Release 12.8(1)

Feature

New or Changed Content

Phone Data Migration

### New and Changed for Firmware Release 12.7(1)

The following table shows the changes made for Firmware Release 12.7(1).

Revision

Updated Section

Updated for hunt group calls on Call Alert

Answer a Call Within Your Hunt Group

General changes

In certain circumstances, users who dialed a number that was busy received the reorder tone. With this release, the user hears
                                             the busy tone.

New section Phone Icons

### New and Changed Information for Firmware Release 12.6(1)

No user guide updates were required for Firmware Release 12.6(1).

### New and Changed Information for Firmware Release 12.5(1)SR3

The following table shows the changes made for Firmware Release 12.5(1)SR3.

Revision

New or Updated Section

New topic

Phone Keypad Characters

### New and Changed Information for Firmware Release 12.5(1)SR2

No user guide updates were required for Firmware Release 12.5(1)SR2.

Firmware Release 12.5(1)SR2 replaces Firmware Release 12.5(1) and Firmware 12.5(1)SR1. Firmware Release 12.5(1) and Firmware
                                 Release 12.5(1)SR1 have been deferred in favor of Firmware Release 12.5(1)SR2.

### New and Changed Information for Firmware Release 12.5(1)SR1

The following table shows the changes made for Firmware Release 12.5(1)SR1.

Revision

New or Updated Section

Support for Activation Code Onboarding

Connect with Activation Code Onboarding

### New and Changed Information for Firmware Release 12.5(1)

No updates were required for Firmware Release 12.5(1).

### New and Changed Information for Firmware Release 12.1(1)

The following table shows the changes made for Firmware Release 12.1(1).

Revision

New or Updated Section

Support for Mobile and Remote Access Through Expressway

Connect to the Network

Connect to Expressway

Support for CMC and FAC

Calls That Require a Billing Code or Authorization Code

## Phone Setup

Your administrator sets up your phone and connects it to the network. If your phone is not set up and connected, contact your
                           administrator for instructions.

### Ways to Provide Power to Your Conference Phone

Your conference phone needs power
                                 from one of these sources:

Power over Ethernet (PoE), which
                                       your network supplies.

Cisco IP Phone Power
                                       Injector.

A PoE Power Cable and Power Cube 3.

The following figure shows the PoE and PoE power cable power
                                 options.

### Connect to the Network

You need to connect the phone to the network.

Wired network connection—The phone is plugged into the network with an Ethernet cable.

After connecting the phone to the network, your phone may be set up for:

Mobile and Remote Access Through Expressway—If your administrator sets up Mobile and Remote Access Through Expressway and
                                       you connect your phone to the network, it connects to the Expressway server.

#### Connect with Activation Code Onboarding

If your network has been configured to support this feature, then you can use Activation Code Onboarding to connect to your
                                    company's phone network.

##### Enter an Activation Code

Activation codes are used to set up your new phone. They can only be used once, and expire after 1 week. Contact your administrator
                                       if you don't know your code or if you need a new one.

Enter your activation code on the activation screen.

Press Submit .

#### Connect to Expressway

You can use Mobile and Remote Access
                                       				Through Expressway to connect to your corporate network when you are working away from your office.

Reset service mode through Settings > Admin Settings > Reset Settings > Service mode .

Press Select when prompted to change the service mode.

Enter your activation code or service domain on the Welcome screen and press Continue .

Enter your username and password.

Select Sign in .

### Replace Your Existing Phone with a New Phone

You can change your phone model. The change can be required for a number of reasons, for example:

You have updated your Cisco Unified
                                          				Communications Manager (Unified CM) to a software version that doesn't support the phone model.

You wants a different phone model from their current model.

Your phone requires repair or replacement.

Limitation : If the old phone has more lines or line buttons than the new phone, the new phone doesn't have the extra lines or line buttons
                                 configured.

The phone reboots when the configuration is complete.

#### Before you begin

Your administrator needs to set up Cisco Unified
                                    				Communications Manager to enable the phone migration.

You need a new phone that hasn't been connected to the network or previously configured.

Power off the old phone.

Power on the new phone.

If prompted, enter your activation code.

Select Replace an existing phone .

Enter the primary extension of the old phone.

If the old phone had a PIN assigned, enter the PIN.

Press Submit .

If you have several devices, select the device to replace from the list and press Continue .

## Activate and Sign In to Your Phone

You may need to activate or sign in to your phone. Activation happens once for your phone, and connects the phone to the call
                           control system. Your administrator gives you your sign-in and activation credentials.

### Sign In to Your Phone

#### Before you begin

Get your user ID and PIN or password from your administrator.

Enter your user ID in the User ID field.

Enter your PIN or password in the PIN or Password field, then press Submit .

### Sign In to Your Extension from Another Phone

You can use Cisco Extension Mobility to sign in to a different phone in your network and have it act the same as your phone.
                                 After you sign in, the phone adopts your user profile, including your phone lines, features, established services, and web-based
                                 settings. Your administrator sets you up for the Cisco Extension Mobility service.

#### Before you begin

Get your user ID and PIN from your administrator.

Press Apps .

Select Extension Mobility (name can vary).

Enter your user ID and PIN.

If prompted, select a device profile.

### Sign Out of Your Extension from Another Phone

Press Apps .

Select Extension Mobility .

Press Yes to sign out.

## Self Care Portal

You can customize some phone settings with the Self Care portal web site, which you access from your computer. The Self Care
                           portal is part of your organization's Cisco Unified Communications Manager.

Your administrator gives you the URL to access the Self Care portal, and provides your user ID and password.

In the Self Care portal, you can control features, line settings, and phone services for your phone.

Phone features include speed dial, do not disturb, and your personal address book.

Line settings affect a specific phone line (directory number) on your phone. Line settings can include call forwarding, visual
                                 and audio message indicators, ring patterns, and other line-specific settings.

Phone services can include special phone features, network data, and web-based information (such as stock quotes and movie
                                 listings). Use the Self Care Portal to subscribe to a phone service before you access it on your phone.

The following table describes some specific features that you configure with the Self Care portal. For more information, see
                           the Self Care portal documentation for your call control system.

Features

Description

Call forward

Use the number that receives calls when call forward is enabled on the phone. Use the Self Care portal to set up more complicated
                                       call forward functions, for example, when your line is busy.

Additional phones

Specify the additional phones such as your mobile phone that you want to use to make and receive calls with the same directory
                                       numbers as your desk phone. You can also define blocked and preferred contacts to restrict or allow calls from certain numbers
                                       to be sent to your mobile phone. When you set up additional phones, you can also set up these features:

Single number reach—Specify whether the additional phone should ring when someone calls your desk phone.

Mobile calls—If the additional phone is a mobile phone, you can set it up to allow you to transfer mobile calls to your desk
                                             phone or desk phone calls to your mobile phone.

Speed dial

Assign phone numbers to speed-dial numbers so that you can quickly call that person.

### Speed-Dial Numbers

When you dial a number on your phone, you enter a series of digits. When you set up a speed-dial number, the speed-dial number
                                 must contain all the digits you need to make the call. For example, if you need to dial 9 to get an outside line, you enter
                                 the number 9 and then the number you want to dial.

You can also add other dialed digits to the number. Examples of additional digits include a meeting access code, an extension,
                                 a voicemail password, an authorization code, and a billing code.

The dial string can contain the following characters:

0 to 9

Pound (#)

Asterisk (*)

Comma (,)—This is the pause character, and gives a 2 second delay in the dialing. You can have several commas in a row. For
                                       example, two commas (,,) represent a pause of 4 seconds.

The rules for dial strings are:

Use the comma to separate the parts of the dial string.

An authorization code must always precede a billing code in the speed-dial string.

A single comma is required between the authorization code and the billing code in the string.

A speed-dial label is required for speed dials with authorization codes and additional digits.

Before you configure the speed dial, try to dial the digits manually at least once to ensure that the digit sequence is correct.

Your phone does not save the authorization code, billing code, or extra digits from the speed dial in the call history. If
                                 you press Redial after you connect to a speed-dial destination, the phone prompts you to enter any required authorization code, billing code,
                                 or additional digits manually.

#### Example

To set up a speed-dial number to call a person at a specific extension, and if you need an authorization code and billing
                                 code, consider the following requirements:

You need to dial 9 for an outside line.

You want to call 5556543 .

You need to input the authorization code 1234 .

You need to input the billing code 9876 .

You must wait for 4 seconds.

After the call connects, you must dial the extension 56789# .

In this scenario, the speed-dial number is 95556543,1234,9876,,56789# .

## Cisco IP Phone 7832 Buttons and Hardware

The following figure shows the Cisco IP Conference Phone 7832.

The following table describes the buttons on the Cisco IP Conference Phone 7832.

1

Mute bar

Toggle the microphone on or off. When the microphone is muted, the LED bar is lit red.

2

LED bar

Indicates call states:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

3

Softkey buttons

Access functions and services.

4

Navigation bar and Select button

Scroll through menus, highlight items, and select the highlighted item.

When the phone is idle, press Up to access the recent calls list and press Down to access the favorites list.

5

Volume button

Adjust the speakerphone volume (off hook) and the ringer volume (on hook).

When you change the volume, the LED bar lights white to show the volume change.

### Phone Keypad Characters

The phone keypad allows you to enter letters, numbers, and special characters. You press the Two (2) to Nine (9) keys to get the letters and numbers. You use the One (1) , Zero (0) ), Asterisk (*) , and Pound (#) keys for special characters. The following table lists the special characters for each key for the English locale. Other
                                 locales will have their own characters.

Keypad Key

Special Characters

One (1)

/ . @ : ; = ? -_ & %

Zero (0)

(space) , ! ^ ' " |

Asterisk (*)

+ * ~ ` < >

Pound (#)

# $ £ ◻ \ ( ) { } [ ]

### Conference Phone Navigation

Use the Navigation bar to scroll through menus. Use the inner Select button of the Navigation bar to select menu items.

If a menu item has an index number, you can enter the index number with the keypad to select the item.

### Conference Phone Softkeys

You can interact with the features on your phone with the softkeys. Softkeys, located below the screen, give you access to
                                 the function displayed on the screen above the softkey. The softkeys change depending on what you are doing at the time.

The ●● softkey indicates more softkey functions are available.

### Conference Phone Screen

The phone screen shows information about your phone such as directory number, active call status, and softkeys. The screen
                                 is made up of three sections: the header row, the middle section, and the footer row.

1

At the top of the screen is the header row. The header row displays the current date and time, and the phone number.

2

The middle of the phone screen displays the information associated with the calls or line.

3

The bottom row of the screen contains the softkey labels. Each label indicates the action for the softkey button below the
                                             screen.

#### Phone Icons

Your phone screen displays many icons. This section gives images of the common icons

Icons are in color or grayscale, depending on the screen.

##### Recents

Icon

Description

Incoming call

Outgoing call

Missed call

#### Clean the Phone Screen

If your phone screen gets dirty, wipe it with a soft, dry cloth.

Do not use any liquids or powders on the phone because they can contaminate the phone components and cause failures.

### Differences Between Phone Calls and Lines

We use the terms lines and calls in very specific ways to explain how to use your phone.

Lines—On the Cisco IP Conference Phone 7832, you have a single line.

Calls—Each line can support multiple calls. By default, your phone supports four connected calls per line, but your administrator
                                       can adjust this number according to your needs.

Only one call can be active at any time; other calls are automatically placed on hold.

## Phone Firmware and Upgrades

Your phone comes pre-installed with firmware that is specific to the call control system.

Occasionally, your administrator upgrades the phone firmware for you. This upgrade happens when you are not using your phone
                           because the phone resets to use the new firmware.

### Postpone a Phone Upgrade

When new  firmware is  available, the Ready to upgrade window is displayed on your phone and a timer begins a 15-second countdown. If you do nothing, the upgrade proceeds.

You can postpone your firmware upgrade for 1 hour and up to 11 times. The upgrade is also postponed if you make or receive
                                 a phone call.

Select Delay to postpone a phone upgrade.

### View the Progress of a Phone Firmware Upgrade

During a phone firmware upgrade, you can view the upgrade progress.

Press Settings .

Select Phone information , highlight Last Upgrade , and press Details .

Press Exit .

## Energy Savings

Your administrator can reduce the amount of power your phone screen uses with the following options:

Power Save—The backlight or screen turns off when the phone is inactive for a set interval.

Power Save Plus—Your phone screen turns on and off at times that are based on your work schedule. If your work hours or work
                                    days change, you can contact your administrator to reconfigure your phone.

For example, your administrator can set your phone to alert you 10 minutes before it turns off. You see the Select button light up and you get a message that your phone is turning off soon. You get notifications at these intervals:

For example, your administrator can set your phone to alert you 10 minutes before it turns off. You get a message that your
                              phone is turning off soon and you get notifications at these intervals:

Four rings at 10 minutes before power off

Four rings at 7 minutes before power off

Four rings at 4 minutes before power off

15 rings at 30 seconds before power off

If your phone is active, it waits until it has been inactive for a set interval  before it notifies  you of the pending power
                              shutdown.

### Turn  On Your Phone

When your phone turns  off to save energy, the phone screen is blank and the Select button lights up.

Press Select to turn  your phone back on.

## Additional Help
                        	 and Information

If you have questions about the functions available on your phone, contact your administrator.

The Cisco website ( https://www.cisco.com ) contains more information about the phones and call control systems.

### Accessibility Features

The Cisco IP
                                 		  Conference Phone 7832 provides accessibility features for the blind,
                                 		  and the visually, hearing, and mobility impaired. Because many of these
                                 		  features are standard, users with disabilities can access them without
                                 		  any special configuration.

In this document, the term phone support pages refers to the web pages that users can access to set up certain features. For Cisco Unified Communications Manager (Release
                                 10.0 and later), these pages are the Self Care Portal. For Cisco Unified Communications Manager (Release 9.1 and earlier),
                                 these pages are the User Options web pages.

For additional information, see the phone User Guide, located here: http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-user-guide-list.html

Cisco is committed
                                 		  to designing and delivering accessible products and technologies to meet the
                                 		  needs of your organization. You can find more information about Cisco and its
                                 		  commitment to accessibility at this URL: http://www.cisco.com/go/accessibility

#### Hearing-Impaired Accessibility Features

Your conference phone comes with standard accessibility features that require little or no setup.

The following table describes the hearing-impaired accessibility features on the Cisco IP Conference Phone 7832.

Item

Accessibility Feature

Description

1

LED bar

The phone screen displays the current state and the LED bar displays:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

2

Visual notification of the phone state and message-waiting indicator

The phone screen displays the current state.

When you have a message, a message is displayed on the phone screen. Your phone also provides an audible message-waiting indicator.

To change the audible voice-message indicator, sign in to the Self Care portal and access the message-indicator settings.
                                                You can change each setting to on or off.

Your administrator can also change your settings.

3

Adjustable ringtone, pitch, and volume

Select Settings > Preferences to change the ringtone.

Adjust the volume level for the phone ring. When not in a call, press Volume to raise or lower the volume.

When you adjust the volume, the LED bar lights white to show the volume increase or decrease.

Your administrator can also change your  settings.

#### Vision-Impaired and Blind Accessibility Features

Your phone comes with standard accessibility features that require little or no setup.

The following table describes the vision-impaired and blind accessibility features on the Cisco IP Conference Phone 7832.

Item

Accessibility Feature

Description

1

Mute button

This button is located above the LED bar and the screen.

Use
                                                the Mute button to toggle the microphone on or off. When the microphone is muted, the LED bar lights red. When you turn on Mute, your
                                                phone beeps once; when you turn off Mute, your phone beeps twice.

2

High-contrast visual and audible alert of an incoming call with the LED bar

The LED bar is located between the Mute button and the screen.

Alerts you to an incoming call. The LED flashes during incoming calls.

Colors indicate your phone's status:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

3

Back-lit grayscale LCD screen with  adjustable contrast on the Cisco IP Phone

Allows you to adjust your phone screen contrast.

4

Softkeys

- These are buttons just below the LCD.

Provide access to special functions. The LCD displays the functions.

5

Navigation cluster (includes the  Navigation bar and the Select button)

- The Navigation cluster is located to the right of the keypad.

Use the Navigation bar to move up and down in the phone LCD. The Select button is in the center of the Navigation bar.

6

Standard 12-key layout

Allows you to use existing or familiar key positions. Key 5 has a nib.

7

Volume key

- This key is located to the left of the keypad.

Allows you  to increase or decrease the ring volume or the sound.

Press up on the rocker key to increase the volume. Press down on the rocker key to decrease the volume.

When you adjust the volume, the LED bar lights white to show the volume increase or decrease.

#### Mobility-Impaired Accessibility Features

Your conference phone comes with standard accessibility features that require
                                    little or no setup.

The following table describes the mobility-impaired accessibility features on the Cisco IP Conference Phone 7832.

Item

Accessibility Feature

Description

1

LED bar

Indicates your phone's status:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

2

Tactile-discernible buttons and functions, including a nib on
                                                					 Key 5

Allow you to easily locate your phone's keys. For example, Key 5 has a nib, which you can use to locate other key positions.

#### Third-Party Accessibility Applications

Cisco works closely with partners to provide solutions that complement the accessibility and usability of Cisco products and
                                    solutions. There are third-party applications such as real-time captioning on Cisco IP Phones, Text Telephones for the Deaf
                                    (TDD/TTY), Real Time Text (RTT), hearing/voice carry over (HCO/VCO), audible caller ID, inline amplifiers for handsets for
                                    louder call sound, "busy lights" , audio/visual emergency notifications through Cisco IP Phones (supporting users with disabilities), etc.

For more information about third-party applications, contact your administrator.

### Troubleshooting

You may experience issues related to the following scenarios:

Your phone
                                    			 cannot communicate with the call control system.

The call control
                                    			 system has communication or internal problems.

Your phone has
                                    			 internal problems.

If you experience problems, your administrator can help troubleshoot the root cause of the problem.

#### Find Information About Your Phone

Your administrator may ask for information about your phone. This information uniquely identifies the phone for troubleshooting
                                    purposes.

Press Settings .

Select Phone information .

(Optional) Press Show detail to view the active load information.

Press Exit .

#### Report Call
                              	 Quality Issues

Your administrator
                                    		  may temporarily configure your phone with the Quality Reporting Tool (QRT) to
                                    		  troubleshoot performance problems. Depending on the configuration, use the QRT to:

Immediately
                                          				report an audio problem on a current call.

Select a
                                          				general problem from a list of categories and choose reason codes.

Press Report .

Scroll and
                                             			 select the item that closely matches your problem.

Press the Select softkey to send the information to your system administrator.

#### Report All Phone Issues

You can use the Cisco Collaboration Problem Report Tool (PRT) to collect and send phone logs, and to report problems to your
                                    administrator. If you see a message that the PRT upload has failed, the problem report is saved on the phone and you should
                                    alert your administrator.

Select Settings > Phone information > Report .

Enter the date and time that you experienced the problem in the Date of problem and Time of problem fields.

Select Problem description .

Select a description from the displayed list, then press Submit .

#### Lost
                              	 Phone Connectivity

Sometimes your phone loses its connection to the phone network. When this connection is lost, your phone displays a message.

If you are on an active call when the connection is lost, the call continues. But, you don't have access to all normal phone
                                    features because some functions require information from the call control system. For example, your softkeys might not work
                                    as you expect.

When the phone reconnects to the call control system, you'll be able to use your phone normally again.

### Cisco One-Year
                           	 Limited Hardware Warranty Terms

Special terms apply
                              		to your hardware warranty and services that you can use during the warranty
                              		period.

Your formal Warranty Statement, including the warranties and license agreements applicable to Cisco software, is available
                              on Cisco.com at this URL: https://www.cisco.com/go/hwwarranty .

| Caution | Using a cell, mobile, or GSM phone, or two-way radio in close proximity to a Cisco IP Phone might cause interference. For
                                          more information, see the manufacturer’s documentation of the interfering device. |
|---|---|

| Feature | New or Changed |
|---|---|
| Hunt Group Enhancements | Recent Calls List |

| Feature | New or Changed Content |
|---|---|
| Phone Data Migration |  |

| Revision | Updated Section |
|---|---|
| Updated for hunt group calls on Call Alert | Answer a Call Within Your Hunt Group |
| General changes | In certain circumstances, users who dialed a number that was busy received the reorder tone. With this release, the user hears
                                             the busy tone. New section Phone Icons |

| Revision | New or Updated Section |
|---|---|
| New topic | Phone Keypad Characters |

| Revision | New or Updated Section |
|---|---|
| Support for Activation Code Onboarding | Connect with Activation Code Onboarding |

| Revision | New or Updated Section |
|---|---|
| Support for Mobile and Remote Access Through Expressway | Connect to the Network Connect to Expressway |
| Support for CMC and FAC | Calls That Require a Billing Code or Authorization Code |

| Step 1 | Enter your activation code on the activation screen. |
|---|---|
| Step 2 | Press Submit . |

| Step 1 | Reset service mode through Settings > Admin Settings > Reset Settings > Service mode . |
|---|---|
| Step 2 | Press Select when prompted to change the service mode. |
| Step 3 | Enter your activation code or service domain on the Welcome screen and press Continue . |
| Step 4 | Enter your username and password. |
| Step 5 | Select Sign in . |

| Step 1 | Power off the old phone. |
|---|---|
| Step 2 | Power on the new phone. |
| Step 3 | If prompted, enter your activation code. |
| Step 4 | Select Replace an existing phone . |
| Step 5 | Enter the primary extension of the old phone. |
| Step 6 | If the old phone had a PIN assigned, enter the PIN. |
| Step 7 | Press Submit . |
| Step 8 | If you have several devices, select the device to replace from the list and press Continue . |

| Step 1 | Enter your user ID in the User ID field. |
|---|---|
| Step 2 | Enter your PIN or password in the PIN or Password field, then press Submit . |

| Step 1 | Press Apps . |
|---|---|
| Step 2 | Select Extension Mobility (name can vary). |
| Step 3 | Enter your user ID and PIN. |
| Step 4 | If prompted, select a device profile. |

| Step 1 | Press Apps . |
|---|---|
| Step 2 | Select Extension Mobility . |
| Step 3 | Press Yes to sign out. |

| Features | Description |
|---|---|
| Call forward | Use the number that receives calls when call forward is enabled on the phone. Use the Self Care portal to set up more complicated
                                       call forward functions, for example, when your line is busy. |
| Additional phones | Specify the additional phones such as your mobile phone that you want to use to make and receive calls with the same directory
                                       numbers as your desk phone. You can also define blocked and preferred contacts to restrict or allow calls from certain numbers
                                       to be sent to your mobile phone. When you set up additional phones, you can also set up these features: Single number reach—Specify whether the additional phone should ring when someone calls your desk phone. Mobile calls—If the additional phone is a mobile phone, you can set it up to allow you to transfer mobile calls to your desk
                                             phone or desk phone calls to your mobile phone. |
| Speed dial | Assign phone numbers to speed-dial numbers so that you can quickly call that person. |

| 1 | Mute bar | Toggle the microphone on or off. When the microphone is muted, the LED bar is lit red. |
|---|---|---|
| 2 | LED bar | Indicates call states: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 3 | Softkey buttons | Access functions and services. |
| 4 | Navigation bar and Select button | Scroll through menus, highlight items, and select the highlighted item. When the phone is idle, press Up to access the recent calls list and press Down to access the favorites list. |
| 5 | Volume button | Adjust the speakerphone volume (off hook) and the ringer volume (on hook). When you change the volume, the LED bar lights white to show the volume change. |

| Keypad Key | Special Characters |
|---|---|
| One (1) | / . @ : ; = ? -_ & % |
| Zero (0) | (space) , ! ^ ' " \| |
| Asterisk (*) | + * ~ ` < > |
| Pound (#) | # $ £ ◻ \ ( ) { } [ ] |

| 1 | At the top of the screen is the header row. The header row displays the current date and time, and the phone number. |
|---|---|
| 2 | The middle of the phone screen displays the information associated with the calls or line. |
| 3 | The bottom row of the screen contains the softkey labels. Each label indicates the action for the softkey button below the
                                             screen. |

| Icon | Description |
|---|---|
|  | Incoming call |
|  | Outgoing call |
|  | Missed call |

| If your phone screen gets dirty, wipe it with a soft, dry cloth. Caution Do not use any liquids or powders on the phone because they can contaminate the phone components and cause failures. | Caution | Do not use any liquids or powders on the phone because they can contaminate the phone components and cause failures. |
|---|---|---|
| Caution | Do not use any liquids or powders on the phone because they can contaminate the phone components and cause failures. |

| Caution | Do not use any liquids or powders on the phone because they can contaminate the phone components and cause failures. |
|---|---|

| Select Delay to postpone a phone upgrade. |
|---|

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Phone information , highlight Last Upgrade , and press Details . |
| Step 3 | Press Exit . |

| Press Select to turn  your phone back on. |
|---|

| Item | Accessibility Feature | Description |
|---|---|---|
| 1 | LED bar | The phone screen displays the current state and the LED bar displays: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 2 | Visual notification of the phone state and message-waiting indicator | The phone screen displays the current state. When you have a message, a message is displayed on the phone screen. Your phone also provides an audible message-waiting indicator. To change the audible voice-message indicator, sign in to the Self Care portal and access the message-indicator settings.
                                                You can change each setting to on or off. Your administrator can also change your settings. |
| 3 | Adjustable ringtone, pitch, and volume | Select Settings > Preferences to change the ringtone. Adjust the volume level for the phone ring. When not in a call, press Volume to raise or lower the volume. When you adjust the volume, the LED bar lights white to show the volume increase or decrease. Your administrator can also change your  settings. |

| Item | Accessibility Feature | Description |
|---|---|---|
| 1 | Mute button This button is located above the LED bar and the screen. | Use
                                                the Mute button to toggle the microphone on or off. When the microphone is muted, the LED bar lights red. When you turn on Mute, your
                                                phone beeps once; when you turn off Mute, your phone beeps twice. |
| 2 | High-contrast visual and audible alert of an incoming call with the LED bar The LED bar is located between the Mute button and the screen. | Alerts you to an incoming call. The LED flashes during incoming calls. Colors indicate your phone's status: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 3 | Back-lit grayscale LCD screen with  adjustable contrast on the Cisco IP Phone | Allows you to adjust your phone screen contrast. |
| 4 | Softkeys These are buttons just below the LCD. | Provide access to special functions. The LCD displays the functions. |
| 5 | Navigation cluster (includes the  Navigation bar and the Select button) The Navigation cluster is located to the right of the keypad. | Use the Navigation bar to move up and down in the phone LCD. The Select button is in the center of the Navigation bar. |
| 6 | Standard 12-key layout | Allows you to use existing or familiar key positions. Key 5 has a nib. |
| 7 | Volume key This key is located to the left of the keypad. | Allows you  to increase or decrease the ring volume or the sound. Press up on the rocker key to increase the volume. Press down on the rocker key to decrease the volume. When you adjust the volume, the LED bar lights white to show the volume increase or decrease. |

| Item | Accessibility Feature | Description |
|---|---|---|
| 1 | LED bar | Indicates your phone's status: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 2 | Tactile-discernible buttons and functions, including a nib on
                                                					 Key 5 | Allow you to easily locate your phone's keys. For example, Key 5 has a nib, which you can use to locate other key positions. |

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Phone information . |
| Step 3 | (Optional) Press Show detail to view the active load information. |
| Step 4 | Press Exit . |

| Step 1 | Press Report . |
|---|---|
| Step 2 | Scroll and
                                             			 select the item that closely matches your problem. |
| Step 3 | Press the Select softkey to send the information to your system administrator. |

| Step 1 | Select Settings > Phone information > Report . |
|---|---|
| Step 2 | Enter the date and time that you experienced the problem in the Date of problem and Time of problem fields. |
| Step 3 | Select Problem description . |
| Step 4 | Select a description from the displayed list, then press Submit . |