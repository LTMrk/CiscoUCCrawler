---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-wireless-ip-phone-8821-212534-cisco-8821-microphone-troublesh-069b485deb
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/wireless-ip-phone-8821/212534-cisco-8821-microphone-troubleshooting.html
retrieved_at: 2026-08-17T01:16:13.880687+00:00
---

Cisco 8821 Wireless Phone Troubleshooting

# Cisco 8821 Wireless Phone Troubleshooting

### Download Options

Updated: April 8, 2020

Document ID: 212534

Contents

## Contents

## Introduction

This article describes how to confirm the functionality of different components of the Cisco 8821 wireless phone.

## Microphone Audio

( CSCve15706 )

Certain phone covers or cases have been found to cause or contribute to microphone failures with the Cisco 8821 phone. Please discontinue using phone covers or cases to prevent damage to the microphone.  External documentation can be found here - Cisco Wireless IP Phone 8821 Support for Third-Party Cases and Covers.

There may be a need to confirm the functionality of the Cisco 8821 wireless phone microphone while investigating a one way or no way audio situation.

#### For phones running firmware versions 11.0(5) and later

The 11.0(5) release includes Audio Diagnostics support to help triage current hardware to determine if the microphone, handset speaker, or handsfree speaker are faulty or not.

Step 1. Audio Diagnostics can be accessed at Settings > Admin settings > Diagnostics > Audio .

Step 2. Press the audio path button (left side of the phone) to toggle between handsfree speaker, handset speaker, etc.

Step 3. Speak into the microphone and the audio should be heard from the output selected in Step 2.

#### For phones running firmware versions prior to 11.0(5)

The Cisco 8821 wireless phone has configurable side tone that can be used to confirm the functionality of the microphone.  Sidetone is sound received from the microphone being played out of the earpiece or headset port.  This is done to mimic normal speech where a person's ear will hear what they are saying while speaking.  This is useful for adjusting spoken volume levels.

To use the sidetone feature on the 8821 phone follow these steps:

Step 1. On the 8821 IP phone, navigate to Settings > Phone settings > Sounds > Headset sidetone.

Step 2. Set the value to High .

Step 3. Ensure the speaker phone is Off (no speaker icon next to the wireless signal indicator).

Note : This procedure can only be used in conjunction with the 8821 IP Phone earpiece. Speaker phone or the use of a headset is not supported.

Step 4. Place a call to or from the 8821 phone, answer it, and mute the phone that is not being tested for microphone functionality.

Step 5. Tap and/or scrape the area near the microphone on the 8821.  The microphone is located on the bottom to the left of the charging plate.  There is a small hole indicating the microphone location.

Step 6. Check if the tap sound can be heard from the phone's earpiece.

### Verification

- If sound can be heard on the earpiece during the test the microphone is functional.

- If no sound is heard the microphone is not functional and will need to be replaced through an RMA. Please use the RMA Failure Code Microphone Failure .

## Phone Will Not Power On (Boot)

( CSCvg06985 ). Fixed in 11.0(4) on 10/30/2018.

There may be a need to confirm the functionality of the battery in an 8821 wireless phone that will not power on and/or boot up.

Step 1. Swap out the battery in the phone that will not power on with another known working and charged battery and see if the phone will power on.

Step 2. Test the battery from the phone that will not power on in another 8821 phone to see if the battery is functional.

Step 3. Connect the 8821 to an AC Power Supply , USB cable on a computer , or Desktop charger and see if the 8821 powers on.

Step 4. Note if there are any indications of power such as (white screen, Cisco boot logo, LED) while attempting power up with known working battery.

Step 5. Note the firmware load the phone is or should be using from the Cisco Unified Communications Manager (CUCM).

### Verification

- If the phone powers on with a known good battery and the original battery from the non-powering on 8821 does not work in another 8821 phone, the battery is not functional.  New batteries can be ordered using the part number CP-BATT-8821= . Please use the RMA Failure Code HW Fail - Power.

- If the phone powers on when connected to a power source open a service request with the Cisco Technical Assistance Center (TAC) for further troubleshooting.

- If the metal charging plate on the bottom of the phone has fallen off, the phone will need to be replaced through an RMA (see CSCve17188 , next). Please use the RMA Failure Code Field Notice Alert (FN70135).

- If the phone fails to power on using a known good battery or while connected to a power source, the phone is not functional and will need to be replaced through an RMA. Please use the RMA Failure Code HW Fail - Power.

## Phone Will Not Charge

( CSCve17188 ). The problem was in Manufacturing between June 2016 to April 2017. The fix is in place for any phone with an SN of FCH2203DFZP or later.

There may be a need to identify the cause of an 8821 phone not changing.

Step 1. Try to charge another 8821 phone using the same power source ( AC Power Supply , USB cable on a computer , or Desktop charger ).

Step 2. Swap out the power source for another AC power supply, another USB port or cable, or another

Step 3. Confirm the metal charging plate on the bottom of the phone that the magnetic power cable connects to is attached to the 8821 phone ( CSCve17188 ).

Step 4. Swap out the battery for a known good battery and try to chage the phone by connecting it to a power source.

Step 5. Note any change in the LED status on the top of the phone or on the display of the phone itself.

### Verification

- If another 8821 phone charges using the same power source and the non-charging 8821 will not charge after changing the battery for a known good battery when connected to the same power source, the phone will need to be replaced through an RMA. Please use the RMA Failure Code HW Fail - Power.

- If no phones charge when connected to a particular power source but will charge when connected to a different power source, the power source is likely faulty.

- If the 8821 phone charges only when the battery is changed with a known good battery, the battery is likely bad and will need to be replaced (part number CP-BATT-8821= ). Please use the RMA Failure Code HW Fail - Power.

- If the metal charging plate is missing, the phone cannot be changed and the phone will need to be replaced through an RMA. Please use the RMA Failure Code Field Notice Alert (FN70135).

## MIC (Manufacturer Installed Certificate) Not Installed

( CSCvc65418 )

The 8821 wireless phone may display a "MIC not installed" message on the phone's screen and/or in the phone's status message log.  The Manufacturer Installed Certificate (MIC) can be used for the following:

- Wireless authentication with Extensible Authentication Protocol (EAP) - Transport Layer Security (TLS)

- Cisco Unified Communications Manager (CUCM) Encrypted/Authenticated device security mode

- HTTPS access to the phone's web page

- Secure Shell (SSH) to the phone

Step 1. Check the bottom of the display for a message that says "MIC not installed" either during the first 10 seconds of the phone turning on or persistently displayed.

Step 2. Check the phone's status messages ( Settings > Admin settings > Status > Status messages ) for a line that says "MIC not installed".

### Verification

The the message "MIC not installed" is seen on the phone's screen and/or in the Status Messages, the phone has lost the MIC.  If the MIC is needed for one of the functions listed above, the phone will need to be replaced through an RMA.  All functions other than wireless authentication using EAP-TLS with the MIC can work by installing a Locally Installed Certificate (LSC) .  If an LSC can be used there is no need to replace the phone, it will function normally with an LSC in place of a MIC.