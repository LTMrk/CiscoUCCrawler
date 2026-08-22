---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-hardware-installation-b-vg410-hardware-intallation-guide-m-installing-0d9c9b2eb4
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/hardware-installation/b-vg410-hardware-intallation-guide/m-installing-the-cisco-vg410-voice-gateway.html
retrieved_at: 2026-08-22T01:13:48.470388+00:00
---

Cisco VG410 Voice Gateway Hardware Installation Guide

# Cisco VG410 Voice Gateway Hardware Installation Guide

Updated: October 27, 2023

Chapter: Installing the Cisco VG410 Voice Gateway

## Chapter: Installing the Cisco VG410 Voice Gateway

# Installing the Cisco VG410 Voice Gateway

This chapter provides the prerequisites and the procedure for installing the Cisco VG410 Voice Gateway in an equipment rack.

## Prerequisites for the Installation

Before installing the device, read the safety warnings and gather the required tools and equipment. For more information about
                           the required tools and equipment, see the Tools and Equipment section in this hardware installation guide.

### Safety Recommendations

Statement 407— Japanese Safety Instruction

You are strongly advised to read the safety instruction before using the product.

https://www.cisco.com/web/JP/techdoc/pldoc/pldoc.html

When installing the product, use the provided or designated connection cables/power cables/AC adapters.

〈製品使用 における 安全上 の 注意〉

www.cisco.com/web/JP/techdoc/index.html

接 続ケーブル 、電源 コードセット 、 AC アダプタ 、 バッテリなどの 部品 は 、必 ず 添付品 または

指定品 をご 使用 ください 。添付品 ・ 指定品以外 をご 使用 になると 故障 や 動作不良、火災 の

原因 となります 。 また 、電源 コードセットは 弊社 が 指定 する 製品以外 の 電 気 機器 には 使用

Warning

Statement
                                             1024— Ground Conductor

This equipment must be grounded. To reduce the risk of
                                          electric shock, never defeat the ground conductor or
                                          operate the equipment in the absence of a suitably
                                          installed ground conductor. Contact the appropriate
                                          electrical inspection authority or an electrician if
                                          you are uncertain that suitable grounding is
                                          available.

Warning

Statement
                                             1046— Installing or Replacing the Unit

To reduce risk of electric shock, when installing or replacing the unit, the ground
                                          connection must always be made first and disconnected last.

If your unit has modules, secure them with the provided screws.

Warning

Statement 338— Prevent Accidental  Discharge

To prevent accidental discharge in the event of a power line cross, route on-premise wiring away from power cables and off-premise
                                          wiring, or use a grounded shield to separate the on-premise wiring from the power cables and off-premise wiring.  A power
                                          line cross is an event, such as a lightning strike, that causes a power surge.  Off-premise wiring is designed to withstand
                                          power line crosses.  On-premise wiring is protected from power line crosses by a device that provides overcurrent and overvoltage
                                          protection.  Nevertheless, if the on-premise wiring is in close proximity to or not shielded from, the off-premise wiring
                                          or power cable during a lightning strike or power surge, the on-premise wiring can carry a dangerous discharge to the attached
                                          interface, equipment, or nearby personnel.

## Unpack the Device

Do not unpack the device until you are ready to install it. If the final installation site will not be ready for some time,
                           keep the chassis in its shipping container to prevent accidental damage. When you are ready to install the chassis, proceed
                           with unpacking it.

The chassis, accessory kit, publications, and any optional equipment you ordered may be shipped in more than one container.
                           When you unpack the containers, check the packing list to ensure that you received all of the items on the list.

If anything appears damaged, or if you encounter problems when installing or configuring your system, contact a customer service
                           representative.

## Mounting the Voice Gateway in Rack

You can install the Cisco VG410 Voice Gateway in 19-inch (48.26-cm) Electronic Industries Alliance (EIA) racks. You can also mount the voice gateway in a 600-mm ETSI rack.
                              You can mount the voice gateway in the following ways:

Front mounting : Brackets attached at the front of the chassis with the front panel facing forward. Brackets can be attached so that mounting
                                    surface can be co-planar with the front of the chassis or recessed 1.0".

Back mounting : Brackets attached at the back of the chassis (PSU and fanside) with the back panel facing forward.

Mid-mount : By reversing the orientation of the brackets, mid-mounting of the chassis can be achieved with either orientation.

Perform the following steps to mount the device on the rack:

Step 1

Attach the mounting brackets to the chassis as shown in the following images, using the screws provided.

Caution

Do not over-torque the screws. The recommended torque is 15 to 18 inch-lb (1.7 to 2.0 N-m)

Step 2

Attach the second bracket to the opposite side of the chassis. Use a number-2 Phillips screwdriver to install the number-6
                                       bracket screws.

Attention

Your chassis installation must allow unrestricted airflow for chassis cooling.

Step 3

Use the screws provided with the rack to install the chassis in the rack. For the 19-inch EIA brackets, start the lower pair
                                       of screws first, and rest the brackets on the lower screws while you insert the upper pair of screws.

See the following images that show the mounting positions from the I/O side, mid mount, and from the power socket side, respectively.

The screw slots in the brackets are spaced to line up with every second pair of screw holes in the rack. When the correct
                                          screw holes are used, the small threaded holes in the brackets line up with unused screw holes in the rack. If the small holes
                                          do not line up with the rack holes, you must raise or lower the brackets to the next rack hole. See the following image that
                                          shows a front mounted orientation in rack, for more clarity.

Warning

Statement
                                                         					1006— Chassis Warning for Rack-Mounting and Servicing

To prevent bodily injury when mounting or servicing this unit in a rack, you must
                                                      				take special precautions to ensure that the system remains stable. The following
                                                      				guidelines are provided to ensure your safety:

This unit should be mounted at the bottom of the rack if it is the only unit
                                                            						in the rack.

When mounting this unit in a partially filled rack, load the rack from the
                                                            						bottom to the top with the heaviest component at the bottom of the rack.

If the rack is provided with stabilizing devices, install the stabilizers
                                                            						before mounting or servicing the unit in the rack.

Warning

Statement 1047— Overheating Prevention

To reduce the risk of fire or bodily injury, do not operate the unit in an area that exceeds the maximum recommended ambient
                                                      temperature of: 40 degrees C.

## Setting the Chassis on a Desktop

After unpacking your device, you can place it on a desktop, bench top, or a shelf. However, be aware of the following before
                           you set your chassis on a desktop:

Do not place anything on top of the router that weighs more than 10 pounds (4.5 kg), and do not stack the gateway hardware
                                 on a desktop. Excessive distributed weight of more than 10 pounds, or pound point load of 10 pounds on top could damage the
                                 chassis.

To prevent airflow restriction, allow clearance around the ventilation openings to be at least 1 inch (2.54cms). Statement
                                 1076.

After you install the voice gateway, you must connect the chassis to a reliable earth ground.

The following images indicate the location of the feet for the chassis and the application of the foot.

Here, 1 indicates the position of the feet.

## Chassis Grounding

Before you connect the power or turn on the power to your chassis, you must provide an adequate chassis ground (earth) connection
                              for the chassis. To install the ground connection for your router, perform the following steps:

### Before you begin

After you install the voice gateway, you must connect the chassis to a reliable earth ground. You must install the ground
                              wire in accordance with local electrical safety standards.

You will need the following tools and supplies to connect the system ground to the chassis:

A size 10 AWG (4 mm2) or larger copper wire

An appropriate user-supplied ring terminal with an inner diameter of 1/4 in. (5–7 mm).

A Philips screwdriver

Step 1

Use the wire stripper to strip one end of the ground wire to the required length for the ground lug or terminal.

For the ground lug, you’d require approximately 0.75 inch (20 mm)

For user-provided ring terminal, use length as required

Step 2

Insert the wire into the open end of the grounding lug.

Step 3

Use the crimping tool to carefully crimp the wire receptacle around the wire. This step is required to ensure a proper mechanical
                                       connection.

Step 4

Locate the chassis ground connector on the side of your chassis.

Step 5

Insert the two screws through the holes in the grounding lug. Use the two screws with captive locking washers provided.

Step 6

Use the Number 2 Phillips screwdriver to carefully tighten the screws until the grounding lug is held firmly to the chassis.
                                       Do not over tighten the screws.

Step 7

Connect the opposite end of the grounding wire to the appropriate grounding point at your site to ensure an adequate chassis
                                       ground.

| Note | Statement 407— Japanese Safety Instruction You are strongly advised to read the safety instruction before using the product. https://www.cisco.com/web/JP/techdoc/pldoc/pldoc.html When installing the product, use the provided or designated connection cables/power cables/AC adapters. 〈製品使用 における 安全上 の 注意〉 www.cisco.com/web/JP/techdoc/index.html 接 続ケーブル 、電源 コードセット 、 AC アダプタ 、 バッテリなどの 部品 は 、必 ず 添付品 または 指定品 をご 使用 ください 。添付品 ・ 指定品以外 をご 使用 になると 故障 や 動作不良、火災 の 原因 となります 。 また 、電源 コードセットは 弊社 が 指定 する 製品以外 の 電 気 機器 には 使用 できないためご注意ください。 |
|---|---|

| Warning | Statement
                                             1024— Ground Conductor This equipment must be grounded. To reduce the risk of
                                          electric shock, never defeat the ground conductor or
                                          operate the equipment in the absence of a suitably
                                          installed ground conductor. Contact the appropriate
                                          electrical inspection authority or an electrician if
                                          you are uncertain that suitable grounding is
                                          available. |
|---|---|

| Warning | Statement
                                             1046— Installing or Replacing the Unit To reduce risk of electric shock, when installing or replacing the unit, the ground
                                          connection must always be made first and disconnected last. If your unit has modules, secure them with the provided screws. |
|---|---|

| Warning | Statement 338— Prevent Accidental  Discharge To prevent accidental discharge in the event of a power line cross, route on-premise wiring away from power cables and off-premise
                                          wiring, or use a grounded shield to separate the on-premise wiring from the power cables and off-premise wiring.  A power
                                          line cross is an event, such as a lightning strike, that causes a power surge.  Off-premise wiring is designed to withstand
                                          power line crosses.  On-premise wiring is protected from power line crosses by a device that provides overcurrent and overvoltage
                                          protection.  Nevertheless, if the on-premise wiring is in close proximity to or not shielded from, the off-premise wiring
                                          or power cable during a lightning strike or power surge, the on-premise wiring can carry a dangerous discharge to the attached
                                          interface, equipment, or nearby personnel. |
|---|---|

| Step 1 | Attach the mounting brackets to the chassis as shown in the following images, using the screws provided. Caution Do not over-torque the screws. The recommended torque is 15 to 18 inch-lb (1.7 to 2.0 N-m) Figure 1. Attach the Mounting Brackets | Caution | Do not over-torque the screws. The recommended torque is 15 to 18 inch-lb (1.7 to 2.0 N-m) |
|---|---|---|---|
| Caution | Do not over-torque the screws. The recommended torque is 15 to 18 inch-lb (1.7 to 2.0 N-m) |
| Step 2 | Attach the second bracket to the opposite side of the chassis. Use a number-2 Phillips screwdriver to install the number-6
                                       bracket screws. Attention Your chassis installation must allow unrestricted airflow for chassis cooling. | Attention | Your chassis installation must allow unrestricted airflow for chassis cooling. |
| Attention | Your chassis installation must allow unrestricted airflow for chassis cooling. |
| Step 3 | Use the screws provided with the rack to install the chassis in the rack. For the 19-inch EIA brackets, start the lower pair
                                       of screws first, and rest the brackets on the lower screws while you insert the upper pair of screws. See the following images that show the mounting positions from the I/O side, mid mount, and from the power socket side, respectively. Figure 2. I/O Side Mounting Figure 3. Mid mounting Figure 4. Power Socket Side Mounting The screw slots in the brackets are spaced to line up with every second pair of screw holes in the rack. When the correct
                                          screw holes are used, the small threaded holes in the brackets line up with unused screw holes in the rack. If the small holes
                                          do not line up with the rack holes, you must raise or lower the brackets to the next rack hole. See the following image that
                                          shows a front mounted orientation in rack, for more clarity. Figure 5. Front Mounted in Rack Warning Statement
                                                         					1006— Chassis Warning for Rack-Mounting and Servicing To prevent bodily injury when mounting or servicing this unit in a rack, you must
                                                      				take special precautions to ensure that the system remains stable. The following
                                                      				guidelines are provided to ensure your safety: This unit should be mounted at the bottom of the rack if it is the only unit
                                                            						in the rack. When mounting this unit in a partially filled rack, load the rack from the
                                                            						bottom to the top with the heaviest component at the bottom of the rack. If the rack is provided with stabilizing devices, install the stabilizers
                                                            						before mounting or servicing the unit in the rack. Warning Statement 1047— Overheating Prevention To reduce the risk of fire or bodily injury, do not operate the unit in an area that exceeds the maximum recommended ambient
                                                      temperature of: 40 degrees C. | Warning | Statement
                                                         					1006— Chassis Warning for Rack-Mounting and Servicing To prevent bodily injury when mounting or servicing this unit in a rack, you must
                                                      				take special precautions to ensure that the system remains stable. The following
                                                      				guidelines are provided to ensure your safety: This unit should be mounted at the bottom of the rack if it is the only unit
                                                            						in the rack. When mounting this unit in a partially filled rack, load the rack from the
                                                            						bottom to the top with the heaviest component at the bottom of the rack. If the rack is provided with stabilizing devices, install the stabilizers
                                                            						before mounting or servicing the unit in the rack. | Warning | Statement 1047— Overheating Prevention To reduce the risk of fire or bodily injury, do not operate the unit in an area that exceeds the maximum recommended ambient
                                                      temperature of: 40 degrees C. |
| Warning | Statement
                                                         					1006— Chassis Warning for Rack-Mounting and Servicing To prevent bodily injury when mounting or servicing this unit in a rack, you must
                                                      				take special precautions to ensure that the system remains stable. The following
                                                      				guidelines are provided to ensure your safety: This unit should be mounted at the bottom of the rack if it is the only unit
                                                            						in the rack. When mounting this unit in a partially filled rack, load the rack from the
                                                            						bottom to the top with the heaviest component at the bottom of the rack. If the rack is provided with stabilizing devices, install the stabilizers
                                                            						before mounting or servicing the unit in the rack. |
| Warning | Statement 1047— Overheating Prevention To reduce the risk of fire or bodily injury, do not operate the unit in an area that exceeds the maximum recommended ambient
                                                      temperature of: 40 degrees C. |

| Caution | Do not over-torque the screws. The recommended torque is 15 to 18 inch-lb (1.7 to 2.0 N-m) |
|---|---|

| Attention | Your chassis installation must allow unrestricted airflow for chassis cooling. |
|---|---|

| Warning | Statement
                                                         					1006— Chassis Warning for Rack-Mounting and Servicing To prevent bodily injury when mounting or servicing this unit in a rack, you must
                                                      				take special precautions to ensure that the system remains stable. The following
                                                      				guidelines are provided to ensure your safety: This unit should be mounted at the bottom of the rack if it is the only unit
                                                            						in the rack. When mounting this unit in a partially filled rack, load the rack from the
                                                            						bottom to the top with the heaviest component at the bottom of the rack. If the rack is provided with stabilizing devices, install the stabilizers
                                                            						before mounting or servicing the unit in the rack. |
|---|---|

| Warning | Statement 1047— Overheating Prevention To reduce the risk of fire or bodily injury, do not operate the unit in an area that exceeds the maximum recommended ambient
                                                      temperature of: 40 degrees C. |
|---|---|

| Step 1 | Use the wire stripper to strip one end of the ground wire to the required length for the ground lug or terminal. For the ground lug, you’d require approximately 0.75 inch (20 mm) For user-provided ring terminal, use length as required |
|---|---|
| Step 2 | Insert the wire into the open end of the grounding lug. |
| Step 3 | Use the crimping tool to carefully crimp the wire receptacle around the wire. This step is required to ensure a proper mechanical
                                       connection. |
| Step 4 | Locate the chassis ground connector on the side of your chassis. |
| Step 5 | Insert the two screws through the holes in the grounding lug. Use the two screws with captive locking washers provided. |
| Step 6 | Use the Number 2 Phillips screwdriver to carefully tighten the screws until the grounding lug is held firmly to the chassis.
                                       Do not over tighten the screws. |
| Step 7 | Connect the opposite end of the grounding wire to the appropriate grounding point at your site to ensure an adequate chassis
                                       ground. Figure 8. Chassis Grounding |