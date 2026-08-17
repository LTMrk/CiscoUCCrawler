---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-accessibilityfeatures-8831-cs38-b-conference-8831-accessibility-featu-daf2d2fde2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/AccessibilityFeatures/8831/cs38_b_conference-8831-accessibility-features.html
retrieved_at: 2026-08-17T01:12:45.994144+00:00
---

Cisco Unified IP Conference Phone 8831 Accessibility Features

# Cisco Unified IP Conference Phone 8831 Accessibility Features

### Download Options

Updated: August 9, 2017

First Published: August 9, 2017

# Accessibility Features

The Cisco Unified IP
                  		  Conference Phone 8831 and 8831NR provides accessibility features for the blind,
                  		  and the visually, hearing, and mobility impaired. Because many of these
                  		  features are standard, they can be used by users with disabilities without
                  		  requiring any special configuration.

The term phone support
                     			 pages refers to the web pages that users can access to set up certain
                  		  features. For Cisco Unified Communications Manager (Release 10.0 and later),
                  		  these pages are the Self Care Portal. For Cisco Unified Communications Manager
                  		  (Release 9.1 and earlier), these pages are the User Options web pages.

Cisco is committed
                  		  to designing and delivering accessible products and technologies to meet the
                  		  needs of your organization. You can find more information about Cisco and its
                  		  commitment to accessibility at this URL: http://www.cisco.com/go/accessibility

## Hearing Impaired Accessibility Features

Your conference phone comes with standard accessibility features that require little or no setup.

Item

Accessibility Feature

Description

1

Visual message-waiting indicator

When you have a message, a message is displayed on the phone screen. Your phone also provides an audible message-waiting indicator.

To change the audible voice-message indicator, sign in to the Self Care portal and access the message-indicator settings.
                                 You can change each setting to on or off.

Your administrator can also change your settings.

2

Visual notification of phone state

The phone screen displays the current state and the LED bar displays:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

3

Adjustable ringtone, pitch, and volume

Select Applications > Preferences to change the ringtone.

Adjust the volume level for the phone ring. When not in a call, press Volume to raise or lower the volume.

Your administrator can also change your settings.

## Vision-Impaired and Blind Accessibility Features

Your phone comes with standard accessibility features that require
                     little or no setup.

Item

Accessibility Feature

Description

1, 11

High-contrast visual and audible alert of incoming call

Alerts you to an incoming call. The LED flashes during incoming calls.

Colors indicate  your phone's status:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

2, 8, 10

Mute button

Use
                                 						  the Mute button to toggle the microphone
                                 						  on or off. When the microphone is muted, the button lights red. 
                                 						When you turn on Mute, your phone beeps once;  when you turn off
                                 						  Mute, your phone beeps twice.

3

Back-lit
                                 					 grayscale LCD screen with  adjustable contrast on the Cisco IP Phone

Allows you to adjust your phone screen's contrast.

4

Softkeys

- These are large buttons just below the LCD.

Provide access to special functions. The
                                 					 functions are displayed on the LCD.

5

Navigation Cluster (includes the  Navigation bar and the Select button)

- The Navigation cluster is located to the right of the keypad.

Use the Navigation bar to move up and
                                 					 down in the phone LCD. The Select button is in the center of the Navigation bar.

6

Standard
                                 					 12-key layout

Allows you to   use
                                 					 existing or familiar key positions. Key 5 has a nib.

7

Volume key

- This key is located to the left of the keypad.

Allows you  to increase
                                 					 or decrease the ring volume or the sound.

Press up on the rocker key to increase the volume. Press down
                                 					 on the rocker key to decrease the volume.

## Mobility-Impaired Accessibility Features

Your conference phone comes with standard accessibility features that require
                     little or no setup.

Item

Accessibility Feature

Description

1

LED

Indicates your phone's status:

Green, solid—Active call

Green, flashing—Incoming call

Green, pulsing—Held call

Red, solid—Muted call

2

Tactile-discernible buttons and functions, including a nib on
                                 					 Key 5

Allow you to easily locate your phone's keys. For example, Key 5 has a nib, which you can use to locate other key positions.

## Cisco Unified Communications Manager Accessibility Features

The following table provides information on the Cisco Unified Communications Manager (Cisco Unified CM) accessibility features.
                     For more information, see the user guide applicable to your phone.

Accessibility Feature

Description

Configuration Requirements

Programmable Line Key (PLK)

You can use the line buttons to initiate, answer, or switch to a call on a particular line. A limited number of features,
                                 such as speed dial, extension mobility, privacy, Busy Lamp Field (BLF) speed dial, Do Not Disturb (DND), and Service URLs,
                                 get assigned to these buttons.

The PLK feature expands the features that can be assigned to the line buttons to include those that softkeys normally control;
                                 for example New Call, Call Back, End Call, and Forward All. When these features are configured on the line buttons, they are
                                 always visible, so you can have a “hard” New Call key.

You can access features easily that may be assigned to softkeys normally, which can be too small and difficult to use.

Standard on all Cisco IP Phones; configuration is required.

Your administrator assigns PLKs to your phone.

Audible Message Waiting Indicator (AMWI)

Cisco Unified IP Phones can send a line-specific stutter dial tone when a voice message is waiting on the phone. You hear
                                 it only when using the line with the waiting messages. When you go off hook (on the line for which a voice message has been
                                 left), the stutter dial tone is heard.

You can change the audible voice-message indicator setting by logging in to your phone support pages, and changing the audible
                                 message-indicator setting to On or Off.

Standard on all Cisco IP Phones.

Configuration is required:

administrator

phone support pages

Do Not Disturb (Alert and Reject)

Your administrator configures the phone to turn on all audible and visual notifications, turn on ringer only, or to choose
                                 the type of alert a phone should play for incoming calls.

Standard on all Cisco IP Phones; configuration is required.

Busy Lamp Field

You can use the Busy Lamp Field (BLF) feature to monitor the call state of a directory number (DN) associated with a speed-dial
                                 button, call log, or directory listing on the phone.

In addition, you can use BLF pickup to monitor incoming calls on a directory number.

When the DN receives an incoming call, the system alerts the you so that you can then pick up the call.

Standard on all Cisco IP Phones; configuration is required.

Phone support pages:

User Options web pages (Cisco Unified CM 9.1 and earlier)

Self Care Portal (Cisco Unified CM 10.0 and later)

The Cisco IP Phone is a network device that enables you to do the following actions:

Share information with other network devices in your company, including your personal computer.

Use your computer to log in to your phone support pages, where you can subscribe to services, set up speed dial and call forwarding
                                       numbers, configure ring settings, and create a personal address book.

Standard on all Cisco IP Phones; configuration is required.

## Third-Party Accessibility Applications

Cisco works closely with partners to provide solutions that complement the accessibility and usability of Cisco products and
                     solutions. There are third-party applications such as real-time captioning on Cisco IP Phones, Text Telephones for the Deaf
                     (TDD/TTY), Real Time Text (RTT), hearing/voice carry over (HCO/VCO), audible caller ID, inline amplifiers for handsets for
                     louder call sound, "busy lights" , audio/visual emergency notifications through Cisco IP Phones (supporting users with disabilities), etc.

Here's a link to a presentation about all the accessibility features of Cisco Unified Communications products, and some third
                     party assistive technology which works with it:

http://www.cisco.com/c/dam/en_us/about/responsibility/accessibility/products/Accessibility_Innovation_Cisco_Unified_Communications.pdf

For more information about third-party applications, contact your administrator.

### This Document Applies to These Products

- IP Phone 8800 Series

| Item | Accessibility Feature | Description |
|---|---|---|
| 1 | Visual message-waiting indicator | When you have a message, a message is displayed on the phone screen. Your phone also provides an audible message-waiting indicator. To change the audible voice-message indicator, sign in to the Self Care portal and access the message-indicator settings.
                                 You can change each setting to on or off. Your administrator can also change your settings. |
| 2 | Visual notification of phone state | The phone screen displays the current state and the LED bar displays: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 3 | Adjustable ringtone, pitch, and volume | Select Applications > Preferences to change the ringtone. Adjust the volume level for the phone ring. When not in a call, press Volume to raise or lower the volume. Your administrator can also change your settings. |

| Item | Accessibility Feature | Description |
|---|---|---|
| 1, 11 | High-contrast visual and audible alert of incoming call | Alerts you to an incoming call. The LED flashes during incoming calls. Colors indicate  your phone's status: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 2, 8, 10 | Mute button | Use
                                 						  the Mute button to toggle the microphone
                                 						  on or off. When the microphone is muted, the button lights red. 
                                 						When you turn on Mute, your phone beeps once;  when you turn off
                                 						  Mute, your phone beeps twice. |
| 3 | Back-lit
                                 					 grayscale LCD screen with  adjustable contrast on the Cisco IP Phone | Allows you to adjust your phone screen's contrast. |
| 4 | Softkeys These are large buttons just below the LCD. | Provide access to special functions. The
                                 					 functions are displayed on the LCD. |
| 5 | Navigation Cluster (includes the  Navigation bar and the Select button) The Navigation cluster is located to the right of the keypad. | Use the Navigation bar to move up and
                                 					 down in the phone LCD. The Select button is in the center of the Navigation bar. |
| 6 | Standard
                                 					 12-key layout | Allows you to   use
                                 					 existing or familiar key positions. Key 5 has a nib. |
| 7 | Volume key This key is located to the left of the keypad. | Allows you  to increase
                                 					 or decrease the ring volume or the sound. Press up on the rocker key to increase the volume. Press down
                                 					 on the rocker key to decrease the volume. |

| Item | Accessibility Feature | Description |
|---|---|---|
| 1 | LED | Indicates your phone's status: Green, solid—Active call Green, flashing—Incoming call Green, pulsing—Held call Red, solid—Muted call |
| 2 | Tactile-discernible buttons and functions, including a nib on
                                 					 Key 5 | Allow you to easily locate your phone's keys. For example, Key 5 has a nib, which you can use to locate other key positions. |

| Accessibility Feature | Description | Configuration Requirements |
|---|---|---|
| Programmable Line Key (PLK) | You can use the line buttons to initiate, answer, or switch to a call on a particular line. A limited number of features,
                                 such as speed dial, extension mobility, privacy, Busy Lamp Field (BLF) speed dial, Do Not Disturb (DND), and Service URLs,
                                 get assigned to these buttons. The PLK feature expands the features that can be assigned to the line buttons to include those that softkeys normally control;
                                 for example New Call, Call Back, End Call, and Forward All. When these features are configured on the line buttons, they are
                                 always visible, so you can have a “hard” New Call key. You can access features easily that may be assigned to softkeys normally, which can be too small and difficult to use. | Standard on all Cisco IP Phones; configuration is required. Your administrator assigns PLKs to your phone. |
| Audible Message Waiting Indicator (AMWI) | Cisco Unified IP Phones can send a line-specific stutter dial tone when a voice message is waiting on the phone. You hear
                                 it only when using the line with the waiting messages. When you go off hook (on the line for which a voice message has been
                                 left), the stutter dial tone is heard. You can change the audible voice-message indicator setting by logging in to your phone support pages, and changing the audible
                                 message-indicator setting to On or Off. | Standard on all Cisco IP Phones. Configuration is required: administrator phone support pages |
| Do Not Disturb (Alert and Reject) | Your administrator configures the phone to turn on all audible and visual notifications, turn on ringer only, or to choose
                                 the type of alert a phone should play for incoming calls. | Standard on all Cisco IP Phones; configuration is required. |
| Busy Lamp Field | You can use the Busy Lamp Field (BLF) feature to monitor the call state of a directory number (DN) associated with a speed-dial
                                 button, call log, or directory listing on the phone. In addition, you can use BLF pickup to monitor incoming calls on a directory number. When the DN receives an incoming call, the system alerts the you so that you can then pick up the call. | Standard on all Cisco IP Phones; configuration is required. |
| Phone support pages: User Options web pages (Cisco Unified CM 9.1 and earlier) Self Care Portal (Cisco Unified CM 10.0 and later) | The Cisco IP Phone is a network device that enables you to do the following actions: Share information with other network devices in your company, including your personal computer. Use your computer to log in to your phone support pages, where you can subscribe to services, set up speed dial and call forwarding
                                       numbers, configure ring settings, and create a personal address book. | Standard on all Cisco IP Phones; configuration is required. |