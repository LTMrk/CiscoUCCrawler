---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg350-hardware-installation-guide-vg350-hig-vg350higinst-html-452d587ad0
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg350/hardware/installation/guide/vg350_hig/vg350higinst.html
retrieved_at: 2026-08-22T01:14:36.320301+00:00
---

Cisco VG350 Voice Gateway Hardware Installation Guide

# Cisco VG350 Voice Gateway Hardware Installation Guide

Updated: March 27, 2014

Chapter: Installing the Cisco VG350 Voice Gateway

## Chapter: Installing the Cisco VG350 Voice Gateway

This chapter contains the procedures for installing your Cisco VG350 Voice Gateway and consists of the following sections:

Tip While you do this installation, record your progress and site information. See the suggested format in the “Keeping Track–Checklist” section .

Warning	Only trained and qualified personnel should be allowed to install, replace, or service this equipment. Statement 1030

Warning	Read the installation instructions before connecting the system to the power source. Statement 1004

## Safety Recommendations

The following information is included to alert you to safety recommendations and best practices when working with this equipment.

### Maintaining Safety with Electricity

Follow these guidelines when working on equipment powered by electricity.

Warning	High leakage current—earth connection essential before connecting to system power supply. Statement 342

Warning	When installing the product, please use the provided or designated connection cables/power cables/AC adaptors/batteries.  Using any other cables/adaptors could cause a malfunction or a fire. Electrical Appliance and Material Safety Law prohibits the use of UL-certified cables (that have the "UL" or "CSA" shown on the cord), not regulated with the subject law by showing "PSE" on the cord, for any other electrical devices than products designated by CISCO. Statement 371

Warning	This product relies on the building's installation for short-circuit (overcurrent) protection. Ensure that the protective device is rated not greater than 15A minimum, 60VDC, 35A minimum, 60VDC, 45A minimum, 60VDC, or 50A minimum, 60VDC for the Circuit Breaker. Statement 1005

Warning	This equipment has been designed for connection to TN and IT power systems.Statement 1007

Warning	Class 1 laser product. Statement 1008

Warning	There is the danger of explosion if the battery is replaced incorrectly. Replace the battery only with the same or equivalent type recommended by the manufacturer. Dispose of used batteries according to the manufacturer's instructions. Statement 1015

Warning Do not work on the system or connect or disconnect cables during periods of lightning activity. Statement 1001

Warning	To avoid electric shock, do not connect safety extra-low voltage (SELV) circuits to telephone-network voltage (TNV) circuits. LAN ports contain SELV circuits, and WAN ports contain TNV circuits. Some LAN and WAN ports both use RJ-45 connectors. Use caution when connecting cables. Statement 1021

Warning	This equipment must be grounded. Never defeat the ground conductor or operate the equipment in the absence of a suitably installed ground conductor. Contact the appropriate electrical inspection authority or an electrician if you are uncertain that suitable grounding is available. Statement 1024

Warning	This unit might have more than one power supply connection. All connections must be removed to de-energize the unit.Statement 1028

Warning Blank faceplates and cover panels serve three important functions: they prevent exposure to hazardous voltages and currents inside the chassis; they contain electromagnetic interference (EMI) that might disrupt other equipment; and they direct the flow of cooling air through the chassis. Do not operate the system unless all cards, faceplates, front covers, and rear covers are in place. Statement 1029

Warning	To prevent personal injury or damage to the chassis, never attempt to lift or tilt the chassis using the handles on modules (such as power supplies, fans, or cards); these types of handles are not designed to support the weight of the unit. Statement 1032

Warning	Do not use this product near water; for example, near a bathtub, wash bowl, kitchen sink or laundry tub, in a wet basement, or near a swimming pool. Statement 1035

Warning	Never install telephone jacks in wet locations unless the jack is specifically designed for wet locations. Statement 1036

Warning	Never touch uninsulated telephone wires or terminals unless the telephone line has been disconnected at the network interface. Statement 1037

Warning	Avoid using a telephone (other than a cordless type) during an electrical storm. There may be a remote risk of electric shock from lightning. Statement 1038

Warning	To report a gas leak, do not use a telephone in the vicinity of the leak. Statement 1039

Warning	Before opening the unit, disconnect the telephone-network cables to avoid contact with telephone-network voltages. Statement 1041

Warning	This equipment contains a ring signal generator (ringer), which is a source of hazardous voltage. Do not touch the RJ-11 (phone) port wires (conductors), the conductors of a cable connected to the RJ-11 port, or the associated circuit-board when the ringer is active. The ringer is activated by an incoming call. Statement 1042

Warning	For diverging beams, viewing the laser output with certain optical instruments within a distance of 100 mm may harm your eyes. For collimated beams, viewing the laser output with certain optical instruments designed for use at a distance may harm your eyes. Statement 1054

Warning	Installation of the equipment must comply with local and national electrical codes. Statement 1074

### General Safety Practices

Follow these guidelines to ensure personal safety and to protect the equipment:

- Keep the chassis area clear and dust-free during and after installation.

- Put the removed chassis cover in a safe place.

- Keep tools away from walk areas where you and others could fall over them.

- Do not wear loose clothing that could get caught in the chassis.

- Wear safety glasses if you are working under any conditions that might be hazardous to your eyes.

Warning	This equipment must be installed and maintained by service personnel as defined by AS/NZS 3260. Incorrectly connecting this equipment to a general-purpose outlet could be hazardous. The telecommunications lines must be disconnected 1) before unplugging the main power connector or 2) while the housing is open, or both. Statement 1043

### Safety Tips

Use these tips as safety guidelines when installing or working around this equipment:

- Locate the emergency Power-off switch for the room in which you are working. Then, if an electrical accident occurs, you can act quickly to turn off the power.

- Disconnect all power before installing or removing a chassis.

- Do not work alone if potentially hazardous conditions exist.

- Never assume that power is disconnected from a circuit. Always check.

- Look carefully for possible hazards in your work area, such as moist floors, ungrounded power extension cables, and missing safety grounds.

- If an electrical accident occurs, proceed as follows:

– Use caution; do not become a victim yourself.

– Turn off power to the system.

– If possible, send another person to get medical aid. Otherwise, assess the condition of the victim and then call for help.

– Determine if the person needs rescue breathing or external cardiac compressions; then take appropriate action.

### Preventing Electrostatic Discharge Damage

Electrostatic discharge ( ESD) can damage equipment and impair electrical circuitry. ESD occurs when electronic components are improperly handled; it can result in complete or intermittent failures.

Always follow ESD-prevention procedures when removing and replacing components.

- Ensure that the chassis is electrically connected to earth ground.

- Wear an ESD-preventive wrist strap, ensuring that it makes good skin contact.

- Connect the clip to the ESD-strap connection jack (to the left of the power switch on the rear of the chassis) or to an unpainted chassis frame surface.

## Site Log

We recommend that you maintain a Site Log to record all actions relevant to the system. Site Log entries might include the following:

- Installation—Print a copy of the Installation Checklist and insert it into the Site Log.

- Upgrades and maintenance—Use the Site Log to record ongoing maintenance and expansion history. Update the Site Log to reflect the following:

– Configuration changes

– Maintenance schedules, requirements, and procedures performed

– Comments, notes, and problems

– Changes and updates to Cisco IOS software

## Keeping Track–Checklist

We recommend that you use an installation checklist and maintain a Site Log.

### Installation Checklist

The Installation Checklist (see Figure 4-1 ) lists the tasks for installing a Cisco VG350 Voice Gateway. Print a copy of this checklist and mark the entries as you complete each task. For each Cisco VG350 Voice Gateway, include a copy of the checklist in your Site Log.

Figure 4-1 Installation Checklist

Installation Checklist for site ______________________________________________

Cisco VG name/serial number _____________________________________________

Task

Verified by

Date

Background information placed in Site Log

Environmental specifications verified

Site power voltages verified

Installation site prepower check completed

Required tools available

Additional equipment available

Cisco VG received

Quick start guide received

Regulatory compliance and safety information received

Information packet, warranty card, and Cisco.com card received

Software version verified

Rack, desktop, or wall-mounting of chassis completed

Initial electrical connections established

ASCII terminal attached to console port

Modem attached to console port (for remote configuration)

Signal distance limits verified

Startup sequence steps completed

Initial operation verified

## Mounting Tools and Equipment

Obtain the following tools and parts to install a Cisco VG350 Voice Gateway:

- Standard flat-blade screwdriver as required for attaching brackets to rack or wall

- Phillips screwdriver for attaching brackets to a Cisco VG350 Voice Gateway

- Mounting brackets and screws for 24-inch rack, if required:

– Four telco machine screws, for installing the chassis in a rack (use the screw size required by the rack)

- Screws and anchors for wall-mounting, if required

– Eight wood screws or other fasteners, for installing the chassis on a wall. An additional starter screw can be used to facilitate wall-mounting.

- ESD-preventive wrist strap

In addition, you might need the following external equipment:

- Console terminal or PC with terminal emulation software

- PC running terminal emulation software for administrative access

- Modem for remote access

- Analog voice RJ-21 cable

- Ethernet switch

- Modem for remote configuration

## Unpacking and Inspection

Do not unpack the Cisco VG350 until you are ready to install it. If the installation site is not ready, keep the chassis in its shipping container to prevent accidental damage.

The Cisco VG350, cables, printed publications, and any optional equipment you ordered might be shipped in more than one container. When you unpack each shipping container, check the packing list to ensure that you received all the following items:

- Cisco VG350 Voice Gateway

- Power cord, 6-foot (1.8-meter)

- RJ-45-to-DB-25 adapter cable (labeled Console)

- RJ-45-to-DB-9 adapter cable (labeled Auxiliary)

- Rack-mounting brackets for 19-inch rack (one pair) with screws for attaching to chassis

- Chassis guard for wall-mounting applications

- Grounding lug and fasteners

- Read Me First for Cisco VG350 Voice Gateway

Inspect all items for shipping damage. If anything appears damaged, or if you encounter problems when installing or configuring your system, contact a customer service representative. (See the “Obtaining Documentation” section .)

| Task | Verified by | Date |
|---|---|---|
| Background information placed in Site Log |  |  |
| Environmental specifications verified |  |  |
| Site power voltages verified |  |  |
| Installation site prepower check completed |  |  |
| Required tools available |  |  |
| Additional equipment available |  |  |
| Cisco VG received |  |  |
| Quick start guide received |  |  |
| Regulatory compliance and safety information received |  |  |
| Information packet, warranty card, and Cisco.com card received |  |  |
| Software version verified |  |  |
| Rack, desktop, or wall-mounting of chassis completed |  |  |
| Initial electrical connections established |  |  |
| ASCII terminal attached to console port |  |  |
| Modem attached to console port (for remote configuration) |  |  |
| Signal distance limits verified |  |  |
| Startup sequence steps completed |  |  |
| Initial operation verified |  |  |