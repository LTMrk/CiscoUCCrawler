---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-unified-ip-phone-7900-series-212061-how-to-make-a-cisco-ip-ph-e8c87373af
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/unified-ip-phone-7900-series/212061-How-To-Make-A-Cisco-IP-Phone-Console-Cab.html
retrieved_at: 2026-08-20T20:40:42.938070+00:00
---

How To Make A Cisco IP Phone Console Cable

# How To Make A Cisco IP Phone Console Cable

Updated: August 6, 2018

Document ID: 212061

Contents

## Contents

## Introduction

This document describes how to make a Cisco Console Cable (CCC) for Cisco IP Phones.

Many Cisco IP Phones have AUX ports on the back that are used to connect Key Expansion Modules (KEM). The RJ-11 port also serves as a serial console port to access the phone's terminal. The AUX port of a phone is as shown in the image.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco IP Phones

- Cables for IP networking

- Use CCC

### Components Used

This document is restricted to specific hardware versions.

These models support an RJ-11 serial port.

- 79XX

- 78XX

- 88XX except 8831

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Pinout Explanation

The standard RJ45 to DB9 flat CCC pinout is different than the pinout of the RJ11. The table and the two images here display the difference between the RJ45 and RJ11 pinout.

Console Cable RJ45

(color)

Console Cable RJ45

(pin)

Console Cable with red, orange, and green wires

connected to RJ45 pins 3, 4, and 6. Pins 3, 4, and 6

are highlighted for clerity.

Console Cable RJ45 side. Pins are counted with the clip down, from left to right.

Console Cable with red, orange, and green wires

connected to RJ11 pins 2, 3, and 4.

RJ11 pins are counted with the clip down, from left to

right. On a 4-wire RJ11 connector pins 1 and 6 are empty.

Note : It is possible the colors of the wires vary between versions of the CCC. Always verify the RJ45 pin number prior to cutting.

## Modify Cable

Obtain an RJ45 to DB9 flat CCC then convert the cable an RJ11 to DB9 phone console cable with the process outlined here. The image here shows the required cable.

Note :  The part ID for CCC is 72-3383-01 and they are sent with most Cisco devices.

Note : Review the section Pinout Explanation before you move forward.

The RJ11 cable as shown in the section Pinout Explanation is functional; however, with only 3 small wires that hold the clip to the cable it can easily break. In order to create a cable that is durable, the plastic sheath inside the plastic end before crimping. The image here shows the blue sheath inside the RJ11 clip.

Without modification, the flat console cable sheath is too wide to fit inside the RJ11 terminal clip. In order to fix this use a pair of scissors to trim the outside of the blue sheath. The detailed steps in this document describe how to properly trim the cable.

### Summary Steps

Step 1. Remove the RJ45 clip from the CCC

Step 2. Trim the blue sheath

Step 3. Remove unnecessary wires

Step 4. Trim the remaining wires

Step 5. Reduce the width of the blue sheath

Step 6. Connect and Crimp the RJ11 Clip

### Detailed Steps

#### Remove RJ45 Clip from CCC

The first step is to cut off the RJ45 terminal from the cable as shown in the image.

#### Trim Blue Sheath

Trim the wire sheath, leaving approximately 0.5 inch (12mm) of wire exposed as shown in the image.

#### Remove Unnecessary Wires

Remove the unnecessary wires. The remaining wires are red, orange, and green as shown in the image.

#### Trim Remaining Wires

Trim the ends of the red, orange, and green wires so they are approx 0.25in (6mm) long.  Make the cut as square as possible so that the three wires are exactly the same length as shown in the images.

#### Reduce Width Of Blue Sheath

Reduce the width of the sheath in order to allow the sheath access the RJ11 clip. This is done so the crimp is on the sheath, not the wires. Make the cut another 0.25in (6mm) down into the sheath as shown in the image.

#### Connect Crimp RJ11 Clip

The cable is ready and you need to attach the RJ11 connector and crimp it as shown in the image.

## Settings For Terminal Application

Modify the settings of your terminal application. The settings are outlined here with a screenshot from PuTTy as an example.

Baud: 115200

Flow Control: None

## Test Cable

At this point, the cable is complete and ready for testing. Plug the cable into the AUX port on the phone as shown in the images and confirm that you can connect to the terminal of the phone without issue.

Note :  The phone terminal image is from the document How To Custom-Make Cisco IP Phone Console Cable which covers another way to make a console cable for Cisco IP Phones.

## Related Information

- How to login to a Cisco IP Phone to set debug level

- Technical Support & Documentation - Cisco Systems

| Console Cable RJ45 (color) | Console Cable RJ45 (pin) | RJ11 Pin |
|---|---|---|
| red | 3 | 2 |
| orange | 4 | 3 |
| green | 6 | 4 |

|  |  |
|---|---|
| Console Cable with red, orange, and green wires connected to RJ45 pins 3, 4, and 6. Pins 3, 4, and 6 are highlighted for clerity. Console Cable RJ45 side. Pins are counted with the clip down, from left to right. | Console Cable with red, orange, and green wires connected to RJ11 pins 2, 3, and 4. RJ11 pins are counted with the clip down, from left to right. On a 4-wire RJ11 connector pins 1 and 6 are empty. |

|  |  |
|---|---|
| Before Trimming | After T rimming |