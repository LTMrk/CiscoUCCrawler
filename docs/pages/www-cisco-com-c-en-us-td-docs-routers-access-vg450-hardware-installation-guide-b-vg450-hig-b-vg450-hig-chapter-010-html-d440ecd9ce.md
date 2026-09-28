---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg450-hardware-installation-guide-b-vg450-hig-b-vg450-hig-chapter-010-html-d440ecd9ce
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg450/hardware/installation/guide/b_Vg450_hig/b_Vg450_hig_chapter_010.html
retrieved_at: 2026-08-22T01:15:35.130567+00:00
---

Cisco VG450 Voice Gateway Hardware Installation Guide

# Cisco VG450 Voice Gateway Hardware Installation Guide

Updated: October 15, 2018

Chapter: Installing the Cisco VG450 Voice Gateway

## Chapter: Installing the Cisco VG450 Voice Gateway

# Installing the Cisco VG450 Voice Gateway

Tip

While you do this installation, record your progress and site information. See the suggested format in the Installation Checklist .

Warning

Only trained and qualified personnel should be allowed to install, replace, or service this equipment. Statement 1030

Warning

Read the installation instructions before connecting the system to the power source. Statement 1004

This chapter contains the procedures for installing your Cisco VG450 Voice Gateway and consists of the following sections:

## Safety Recommendations

The following information is included to alert you to safety recommendations and best practices when working with this equipment.

### Maintaining Safety with Electricity

Follow these guidelines when working on equipment powered by electricity.

Warning

High leakage current—earth connection essential before connecting to system power supply. Statement 342

Warning

When installing the product, please use the provided or designated connection cables/power cables/AC adaptors/batteries.
                                          Using any other cables/adaptors could cause a malfunction or a fire. Electrical Appliance and Material Safety Law prohibits
                                          the use of UL-certified cables (that have the "UL" or "CSA" shown on the cord), not regulated with the subject law by showing
                                          "PSE" on the cord, for any other electrical devices than products designated by CISCO. Statement 371

Warning

This product relies on the building's installation for short-circuit (overcurrent) protection. Ensure that the protective
                                          device is rated not greater than 15A minimum, 60VDC, 35A minimum, 60VDC, 45A minimum, 60VDC, or 50A minimum, 60VDC for the
                                          Circuit Breaker. Statement 1005

Warning

This equipment has been designed for connection to TN and IT power systems. Statement 1007

Warning

Class 1 laser product. Statement 1008

Warning

Avoid using or servicing any equipment that has outdoor connections during an electrical storm. There may be a risk of electric
                                          shock from lightning. Statement 1088

Warning

This equipment must be grounded. Never defeat the ground conductor or operate the equipment in the absence of a suitably
                                          installed ground conductor. Contact the appropriate electrical inspection authority or an electrician if you are uncertain
                                          that suitable grounding is available. Statement 1024

Warning

This unit might have more than one power supply connection. All connections must be removed to de-energize the unit. Statement
                                          1028

Warning

Blank faceplates and cover panels serve three important functions: they prevent exposure to hazardous voltages and currents
                                          inside the chassis; they contain electromagnetic interference (EMI) that might disrupt other equipment; and they direct the
                                          flow of cooling air through the chassis. Do not operate the system unless all cards, faceplates, front covers, and rear covers
                                          are in place. Statement 1029

Warning

To prevent personal injury or damage to the chassis, never attempt to lift or tilt the chassis using the handles on modules
                                          (such as power supplies, fans, or cards); these types of handles are not designed to support the weight of the unit. Statement
                                          1032

Warning

Do not use this product near water; for example, near a bathtub, wash bowl, kitchen sink or laundry tub, in a wet basement,
                                          or near a swimming pool. Statement 1035

Warning

Never install telephone jacks in wet locations unless the jack is specifically designed for wet locations. Statement 1036

Warning

Never touch uninsulated telephone wires or terminals unless the telephone line has been disconnected at the network interface.
                                          Statement 1037

Warning

Avoid using a telephone (other than a cordless type) during an electrical storm. There may be a remote risk of electric shock
                                          from lightning. Statement 1038

Warning

To report a gas leak, do not use a telephone in the vicinity of the leak. Statement 1039

Warning

Before opening the unit, disconnect the telephone-network cables to avoid contact with telephone-network voltages. Statement
                                          1041

Warning

This equipment contains a ring signal generator (ringer), which is a source of hazardous voltage. Do not touch the RJ-11
                                          (phone) port wires (conductors), the conductors of a cable connected to the RJ-11 port, or the associated circuit-board when
                                          the ringer is active. The ringer is activated by an incoming call. Statement 1042

Warning

Installation of the equipment must comply with local and national electrical codes. Statement 1074

Warning

Pluggable optical modules comply with IEC 60825-1 Ed. 3 and 21 CFR 1040.10 and 1040.11 with or without exception for conformance
                                          with IEC 60825-1 Ed. 3 as described in Laser Notice No. 56, dated May 8, 2019.

### General Safety Practices

Follow these guidelines to ensure personal safety and to protect the equipment:

- Keep the chassis area clear and dust-free during and after installation.

- Put the removed chassis cover in a safe place.

- Keep tools away from walk areas where you and others could fall over them.

- Do not wear loose clothing that could get caught in the chassis.

- Wear safety glasses if you are working under any conditions that might be hazardous to your eyes.

### Safety Tips

Use these tips as safety guidelines when installing or working around this equipment:

- Locate the emergency Power-off switch for the room in which you are working. Then, if an electrical accident occurs, you can
                                 act quickly to turn off the power.

- Disconnect all power before installing or removing a chassis.

- Do not work alone if potentially hazardous conditions exist.

- Never assume that power is disconnected from a circuit. Always check.

- Look carefully for possible hazards in your work area, such as moist floors, ungrounded power extension cables, and missing
                                 safety grounds.

- Use caution; do not become a victim yourself.

- Turn off power to the system.

- If possible, send another person to get medical aid. Otherwise, assess the condition of the victim and then call for help.

- Determine if the person needs rescue breathing or external cardiac compressions; then take appropriate action.

### Preventing Electrostatic Discharge Damage

Electrostatic discharge (ESD) can damage equipment and impair electrical circuitry. ESD occurs when electronic components
                              are improperly handled; it can result in complete or intermittent failures.

Always follow ESD-prevention procedures when removing and replacing components.

- Ensure that the chassis is electrically connected to earth ground.

- Wear an ESD-preventive wrist strap, ensuring that it makes good skin contact.

- Connect the clip to the ESD-strap connection jack (to the left of the power switch on the rear of the chassis) or to an unpainted
                                 chassis frame surface.

Caution

For safety, periodically check the resistance value of the antistatic strap, which should be between 1 and 10 megohm (Mohm).

## Unpacking and Inspection

Do not unpack the Cisco VG450 until you are ready to install it. If the installation site is not ready, keep the chassis in
                           its shipping container to prevent accidental damage.

The Cisco VG450, cables, printed publications, and any optional equipment you ordered might be shipped in more than one container.
                           When you unpack each shipping container, check the packing list to ensure that you received all the following items:

Cisco VG450 Voice Gateway

Power cord, 6-foot (1.8-meter)

RJ-45-to-DB-25 adapter cable (labeled Console)

RJ-45-to-DB-9 adapter cable (labeled Auxiliary)

Rack-mounting brackets for 19-inch rack (one pair) with screws for attaching to chassis

Grounding lug and fasteners

Inspect all items for shipping damage. If anything appears damaged, or if you encounter problems when installing or configuring
                           your system, contact a customer service representative.

## Install the Cisco VG450 Voice Gateway

Caution

To prevent damage to the chassis, never attempt to lift or tilt the chassis by holding it by the plastic panel on the front.
                                       Always hold the chassis by the sides of the metal body.

You can install the Cisco VG450 Voice Gateway in one of the following ways:

### Setting the Chassis on a Desktop

You can place the router on a desktop, bench top, or shelf.

Caution

Do not place anything on top of the router that weighs more than 10 pounds (4.5 kg), and do not stack the gateway hardware
                                          on a desktop. Excessive distributed weight of more than 10 pounds, or pound point load of 10 pounds on top could damage the
                                          chassis.

Warning

To prevent airflow restriction, allow clearance around the ventilation openings to be at least 1 inch (2.54cms). Statement
                                          1076.

After you install the voice gateway, you must connect the chassis to a reliable earth ground. For the chassis ground connection
                              procedures, see the Chassis Grounding section.

### Mount Cisco VG450 Voice Gateway Chassis in Rack

Warning

To prevent bodily injury when mounting or servicing this unit in a rack, you must take special precautions to ensure that
                                          the system remains stable. The following guidelines are provided to ensure your safety:

This unit should be mounted at the bottom of the rack if it is the only unit in the rack.

When mounting this unit in a partially filled rack, load the rack from the bottom to the top with the heaviest component at
                                                the bottom of the rack.

If the rack is provided with stabilizing devices, install the stabilizers before mounting or servicing the unit in the rack.
                                                Statement 1006.

You can install the Cisco VG450 Voice Gateway in 19-inch (48.26-cm) EIA and 23-inch (58.42-cm) Southwestern Bell Corporation
                              (SBC) racks. You can also mount the voice gateway in a 600-mm ETSI rack. Use the standard brackets shipped with the hardware
                              for mounting the chassis in a 19-inch EIA rack; you can order optional larger brackets for mounting the chassis in a 23-inch
                              SBC rack.

You can mount the voice gateway in the following ways:

Center-front mounting: Brackets attached in the center front of the chassis with only the front panel facing forward.

Center-back mounting: Brackets attached in the center back of the chassis with only the back panel facing forward.

Front mounting: Brackets attached at the front of the chassis with the front panel facing forward.

Back mounting: Brackets attached at the back of the chassis with the back panel facing forward.

Attach the mounting brackets to the chassis as shown in the following images, using the screws provided.

Caution

Do not over-torque the screws. The recommended torque is 15 to 18 inch-lb (1.7 to 2.0 N-m).

Attach the second bracket to the opposite side of the chassis. Use a number-2 Phillips screwdriver to install the number-8
                                    bracket screws.

Caution

Your chassis installation must allow unrestricted airflow for chassis cooling.

1

Screws

4

23-inch SBC brackets

3

19-inch EIA brackets

4

19-inch EIA brackets

Use the screws provided with the rack to install the chassis in the rack. For both the 19-inch EIA brackets and the 23-inch
                                    SBC brackets, start the lower pair of screws first, and rest the brackets on the lower screws while you insert the upper pair
                                    of screws.

Tip

The screw slots in the brackets are spaced to line up with every second pair of screw holes in the rack. When the correct
                                                screw holes are used, the small, threaded holes in the brackets line up with unused screw holes in the rack. If the small
                                                holes do not line up with the rack holes, you must raise or lower the brackets to the next rack hole.

The following image shows a typical installation with back mounting

1

Mounting Screws (4)

After you install the voice gateway, you must connect the chassis to a reliable earth ground. For the chassis ground connection
                              procedures, see the Chassis Grounding section.

## Chassis Grounding

Warning

To reduce the risk of electric shock, the chassis of this equipment needs to be connected to permanent earth ground during
                                          normal use. Statement 445

Use a size 10 AWG (4 mm2) or larger copper wire and an appropriate user-supplied ring terminal with an inner diameter of
                              1/4 in. (5–7 mm).

To install the ground connection for your router, perform the
                              		  following steps:

### SUMMARY STEPS

- Strip one end of the ground wire to the length required for the ring terminal.

- Crimp the ground wire to the ring terminal, using a crimp tool of the appropriate size.

- Attach the ground lug or ring terminal to the chassis as shown in the following image. Use one of the screws provided. Tighten
                              the screws to a torque of 8 to 10 in-lb (0.9 to 1.1 N-m).

- Connect the other end of the ground wire to a known reliable earth ground point at your site.

### DETAILED STEPS

Step 1

Strip one end of the ground wire to the length required for the ring terminal.

Step 2

Crimp the ground wire to the ring terminal, using a crimp tool of the appropriate size.

Step 3

Attach the ground lug or ring terminal to the chassis as shown in the following image. Use one of the screws provided. Tighten
                                       the screws to a torque of 8 to 10 in-lb (0.9 to 1.1 N-m).

Step 4

Connect the other end of the ground wire to a known reliable earth ground point at your site.

## Power-On Procedure

Perform this procedure to power on your Cisco VG450 Voice Gateway, and verify that it goes through its initialization and
                              self-test. When this is finished, the Cisco VG450 Voice Gateway is ready to configure.

Warning

This unit might have more than one power supply connection. All connections must be removed to de-energize the unit. Statement
                                          1028

Warning

Installation of the equipment must comply with local and national electrical codes. Statement 1074

To power on the Cisco VG450 Voice Gateway, perform the following:

Step 1

Power on your terminal or PC, and configure it for 9600 bps, 8 data bits, 1 stop bit, and no parity.

Step 2

Move the Cisco VG450 Voice Gateway power switch to the ON position.

The green LED next to the auxiliary port come on and the fan starts to operate. If this does not happen, see the Troublehooting section in this guide.

The following message is displayed at the end of the boot-up messages:

### Example:

```
--- System Configuration Dialog ---
Would you like to enter the initial configuration dialog? [yes/no]:
```

Step 3

Enter no to proceed with manual configuration using the CLI:

### Example:

```
Would you like to enter the initial configuration dialog? [yes/no]: no Would you like to terminate autoinstall? [yes]
```

Step 4

Press Return to terminate autoinstall and continue with manual configuration.

Several messages are displayed, ending with a line similar to the following:

### Example:

```
... Copyright (c) 1986-2003 by cisco Systems, Inc.
Compiled < date > < time > by < person >
```

Step 5

Press Return to bring up the Router> prompt:

### Example:

```
... flashfs[4]: Initialization complete.
Router>
```

Step 6

Enter privileged EXEC mode:

### Example:

```
Router> enable Router#
```

Step 7

Continue with the Troubleshooting section.

| Tip | While you do this installation, record your progress and site information. See the suggested format in the Installation Checklist . |
|---|---|

| Warning | Only trained and qualified personnel should be allowed to install, replace, or service this equipment. Statement 1030 |
|---|---|

| Warning | Read the installation instructions before connecting the system to the power source. Statement 1004 This chapter contains the procedures for installing your Cisco VG450 Voice Gateway and consists of the following sections: |
|---|---|

| Warning | High leakage current—earth connection essential before connecting to system power supply. Statement 342 |
|---|---|

| Warning | When installing the product, please use the provided or designated connection cables/power cables/AC adaptors/batteries.
                                          Using any other cables/adaptors could cause a malfunction or a fire. Electrical Appliance and Material Safety Law prohibits
                                          the use of UL-certified cables (that have the "UL" or "CSA" shown on the cord), not regulated with the subject law by showing
                                          "PSE" on the cord, for any other electrical devices than products designated by CISCO. Statement 371 |
|---|---|

| Warning | This product relies on the building's installation for short-circuit (overcurrent) protection. Ensure that the protective
                                          device is rated not greater than 15A minimum, 60VDC, 35A minimum, 60VDC, 45A minimum, 60VDC, or 50A minimum, 60VDC for the
                                          Circuit Breaker. Statement 1005 |
|---|---|

| Warning | This equipment has been designed for connection to TN and IT power systems. Statement 1007 |
|---|---|

| Warning | Class 1 laser product. Statement 1008 |
|---|---|

| Warning | Avoid using or servicing any equipment that has outdoor connections during an electrical storm. There may be a risk of electric
                                          shock from lightning. Statement 1088 |
|---|---|

| Warning | This equipment must be grounded. Never defeat the ground conductor or operate the equipment in the absence of a suitably
                                          installed ground conductor. Contact the appropriate electrical inspection authority or an electrician if you are uncertain
                                          that suitable grounding is available. Statement 1024 |
|---|---|

| Warning | This unit might have more than one power supply connection. All connections must be removed to de-energize the unit. Statement
                                          1028 |
|---|---|

| Warning | Blank faceplates and cover panels serve three important functions: they prevent exposure to hazardous voltages and currents
                                          inside the chassis; they contain electromagnetic interference (EMI) that might disrupt other equipment; and they direct the
                                          flow of cooling air through the chassis. Do not operate the system unless all cards, faceplates, front covers, and rear covers
                                          are in place. Statement 1029 |
|---|---|

| Warning | To prevent personal injury or damage to the chassis, never attempt to lift or tilt the chassis using the handles on modules
                                          (such as power supplies, fans, or cards); these types of handles are not designed to support the weight of the unit. Statement
                                          1032 |
|---|---|

| Warning | Do not use this product near water; for example, near a bathtub, wash bowl, kitchen sink or laundry tub, in a wet basement,
                                          or near a swimming pool. Statement 1035 |
|---|---|

| Warning | Never install telephone jacks in wet locations unless the jack is specifically designed for wet locations. Statement 1036 |
|---|---|

| Warning | Never touch uninsulated telephone wires or terminals unless the telephone line has been disconnected at the network interface.
                                          Statement 1037 |
|---|---|

| Warning | Avoid using a telephone (other than a cordless type) during an electrical storm. There may be a remote risk of electric shock
                                          from lightning. Statement 1038 |
|---|---|

| Warning | To report a gas leak, do not use a telephone in the vicinity of the leak. Statement 1039 |
|---|---|

| Warning | Before opening the unit, disconnect the telephone-network cables to avoid contact with telephone-network voltages. Statement
                                          1041 |
|---|---|

| Warning | This equipment contains a ring signal generator (ringer), which is a source of hazardous voltage. Do not touch the RJ-11
                                          (phone) port wires (conductors), the conductors of a cable connected to the RJ-11 port, or the associated circuit-board when
                                          the ringer is active. The ringer is activated by an incoming call. Statement 1042 |
|---|---|

| Warning | Installation of the equipment must comply with local and national electrical codes. Statement 1074 |
|---|---|

| Warning | Pluggable optical modules comply with IEC 60825-1 Ed. 3 and 21 CFR 1040.10 and 1040.11 with or without exception for conformance
                                          with IEC 60825-1 Ed. 3 as described in Laser Notice No. 56, dated May 8, 2019. |
|---|---|

| Caution | For safety, periodically check the resistance value of the antistatic strap, which should be between 1 and 10 megohm (Mohm). |
|---|---|

| Caution | To prevent damage to the chassis, never attempt to lift or tilt the chassis by holding it by the plastic panel on the front.
                                       Always hold the chassis by the sides of the metal body. |
|---|---|

| Note | Do not set the chassis in an area where the high acoustic noise can
                                       		be an issue. |
|---|---|

| Caution | Do not place anything on top of the router that weighs more than 10 pounds (4.5 kg), and do not stack the gateway hardware
                                          on a desktop. Excessive distributed weight of more than 10 pounds, or pound point load of 10 pounds on top could damage the
                                          chassis. |
|---|---|

| Warning | To prevent airflow restriction, allow clearance around the ventilation openings to be at least 1 inch (2.54cms). Statement
                                          1076. |
|---|---|

| Warning | To prevent bodily injury when mounting or servicing this unit in a rack, you must take special precautions to ensure that
                                          the system remains stable. The following guidelines are provided to ensure your safety: This unit should be mounted at the bottom of the rack if it is the only unit in the rack. When mounting this unit in a partially filled rack, load the rack from the bottom to the top with the heaviest component at
                                                the bottom of the rack. If the rack is provided with stabilizing devices, install the stabilizers before mounting or servicing the unit in the rack.
                                                Statement 1006. |
|---|---|

| Caution | Do not over-torque the screws. The recommended torque is 15 to 18 inch-lb (1.7 to 2.0 N-m). |
|---|---|

| Caution | Your chassis installation must allow unrestricted airflow for chassis cooling. |
|---|---|

| 1 | Screws | 4 | 23-inch SBC brackets |
|---|---|---|---|
| 3 | 19-inch EIA brackets | 4 | 19-inch EIA brackets |

| Tip | The screw slots in the brackets are spaced to line up with every second pair of screw holes in the rack. When the correct
                                                screw holes are used, the small, threaded holes in the brackets line up with unused screw holes in the rack. If the small
                                                holes do not line up with the rack holes, you must raise or lower the brackets to the next rack hole. |
|---|---|

| 1 | Mounting Screws (4) |
|---|---|

| Warning | To reduce the risk of electric shock, the chassis of this equipment needs to be connected to permanent earth ground during
                                          normal use. Statement 445 |
|---|---|

| Step 1 | Strip one end of the ground wire to the length required for the ring terminal. |
|---|---|
| Step 2 | Crimp the ground wire to the ring terminal, using a crimp tool of the appropriate size. |
| Step 3 | Attach the ground lug or ring terminal to the chassis as shown in the following image. Use one of the screws provided. Tighten
                                       the screws to a torque of 8 to 10 in-lb (0.9 to 1.1 N-m). Figure 4. Chassis Ground Connection on the Router |
| Step 4 | Connect the other end of the ground wire to a known reliable earth ground point at your site. |

| Warning | This unit might have more than one power supply connection. All connections must be removed to de-energize the unit. Statement
                                          1028 |
|---|---|

| Warning | Installation of the equipment must comply with local and national electrical codes. Statement 1074 |
|---|---|

| Step 1 | Power on your terminal or PC, and configure it for 9600 bps, 8 data bits, 1 stop bit, and no parity. |
|---|---|
| Step 2 | Move the Cisco VG450 Voice Gateway power switch to the ON position. The green LED next to the auxiliary port come on and the fan starts to operate. If this does not happen, see the Troublehooting section in this guide. The following message is displayed at the end of the boot-up messages: Example: --- System Configuration Dialog ---
Would you like to enter the initial configuration dialog? [yes/no]: |
| Step 3 | Enter no to proceed with manual configuration using the CLI: Example: Would you like to enter the initial configuration dialog? [yes/no]: no Would you like to terminate autoinstall? [yes] |
| Step 4 | Press Return to terminate autoinstall and continue with manual configuration. Several messages are displayed, ending with a line similar to the following: Example: ... Copyright (c) 1986-2003 by cisco Systems, Inc.
Compiled < date > < time > by < person > |
| Step 5 | Press Return to bring up the Router> prompt: Example: ... flashfs[4]: Initialization complete.
Router> |
| Step 6 | Enter privileged EXEC mode: Example: Router> enable Router# |
| Step 7 | Continue with the Troubleshooting section. Note If the rommon 1> prompt appears, your system has booted in ROM monitor mode. For information on the ROM monitor, refer to
                                                   the router rebooting and ROM monitor information in the Cisco IOS Configuration Fundamentals Configuration Guide for your Cisco IOS software release. | Note | If the rommon 1> prompt appears, your system has booted in ROM monitor mode. For information on the ROM monitor, refer to
                                                   the router rebooting and ROM monitor information in the Cisco IOS Configuration Fundamentals Configuration Guide for your Cisco IOS software release. |
| Note | If the rommon 1> prompt appears, your system has booted in ROM monitor mode. For information on the ROM monitor, refer to
                                                   the router rebooting and ROM monitor information in the Cisco IOS Configuration Fundamentals Configuration Guide for your Cisco IOS software release. |

| Note | If the rommon 1> prompt appears, your system has booted in ROM monitor mode. For information on the ROM monitor, refer to
                                                   the router rebooting and ROM monitor information in the Cisco IOS Configuration Fundamentals Configuration Guide for your Cisco IOS software release. |
|---|---|