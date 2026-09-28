---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-installatio-3c8a3607e6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/installation/guide/ucce_b_install_upgrade_guide_1262/ucce_m_1251_split_generic-pg-cucm-vrupg.html
retrieved_at: 2026-08-16T20:00:35.519195+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: Split Generic PG to CUCM PG and VRU PG

## Chapter: Split Generic PG to CUCM PG and VRU PG

# Split Generic PG to CUCM PG and VRU PG

## Convert Generic PG to CUCM PG and VRU PG in PG Explorer

Step 1

In the Configuration Manager window, expand Tools > Explorer Tools .

Step 2

Open PG Explorer .

Step 3

Click Add PG and then enter the following values in the Logical Controller pane:

In the Name field, enter VRU_PG .

For Client type , choose VRU .

Step 4

Delete the peripheral that was automatically created in the previous step.

Step 5

Click Save .

Step 6

Drag the VRU peripheral from the Generic PG to the VRU PG.

A message appears asking if you are sure you want to move the peripheral to a different PG. Click Yes to confirm.

Step 7

Rename the Generic PG to CUCM PG and change the Client type to CUCM .

Step 8

Click Save .

Make sure to record the Logical Controller ID of the new VRU PG. You need to enter it when you install the PG.

## Install VRU PG

Step 1

Add a new VRU PG alongside the Generic PG on both Side A and Side B VMs of the Generic PG machine. On the VRU PG, choose Start > All Programs > Unified CCE Tools > Peripheral Gateway Setup .

Step 2

In the Instance Component section, click Add .

Step 3

Click Peripheral Gateway .

Step 4

In the Peripheral Gateways Properties dialog, do the following:

Check the Production Mode check box.

Check the Auto start at system start up check box.

Check the Duplexed Peripheral Gateway check box.

From the PG Node Properties ID drop-down list, select PG3 .

Select the appropriate side (Side A or Side B).

In the Client Type Selection section, add VRU to the Selected Types.

Click Next .

Step 5

In the Peripheral Gateway Managers section of the Peripheral Gateway Component Properties dialog box, click Add .

Step 6

Select VRU and PIM1 and click OK . Enter the VRU PIM details.

Step 7

In the Logical controller ID field, enter the Logical controller ID of the VRU PG that you created previously in PG Explorer.

Step 8

In the Device Management Protocols Properties dialog box, do the following:

For Side A PG:

Select Side A preferred .

For Side A properties, select CallRouter is local .

For Side B properties, select CallRouter is remote (WAN) .

For Side B PG:

Select Side B preferred .

For Side A properties, select CallRouter is remote (WAN) .

For Side B properties, select CallRouter is local .

For both sides:

Accept the default in the Usable Bandwidth (kbps) field.

Accept the default in the Heartbeat Interval (100ms) field.

Click Next .

Step 9

In the Peripheral Gateway Network Interfaces dialog box, complete the interface fields:

Enter the Private and Visible network interface hostnames. For the PG, use the same hostnames for private and private high.
                                             For the router, enter the hostname of the Unified CCE Rogger Side A for the Router visible A and Router visible A high interfaces.
                                             Enter the hostname of the Unified CCE Rogger Side B for the Router visible B and Router visible B high interfaces.

For the Side A PG, in the Private Interfaces section, click QoS . Check Enable QoS and click OK .

For both the Side A and Side B PGs, in the Visible Interfaces section, click QoS . Check Enable QoS and click OK .

Click Next .

Step 10

In the Check Setup Information dialog box, click Next .

Step 11

In the Setup Complete dialog box, click Finish .

## Convert Generic PG to CUCM PG using Peripheral Gateway Setup

Step 1

Open Peripheral Gateway Setup.

Step 2

Select PG.

Step 3

Click Edit .

Step 4

In the Client Type Selection section, remove VRU .

Step 5

Click Next .

Step 6

In the Peripheral Gateway Component Properties dialog box, remove the VRU PIMs that were used for connecting to VRU and click Next .

Step 7

In the Device Management Protocol Properties dialog box, click Next .

Step 8

In the Check Setup Information dialog box, click Next .

Step 9

Check the Yes, start the Unified ICM/CC Node Manager check box and click Finish .

| Step 1 | In the Configuration Manager window, expand Tools > Explorer Tools . |
|---|---|
| Step 2 | Open PG Explorer . |
| Step 3 | Click Add PG and then enter the following values in the Logical Controller pane: In the Name field, enter VRU_PG . For Client type , choose VRU . |
| Step 4 | Delete the peripheral that was automatically created in the previous step. |
| Step 5 | Click Save . |
| Step 6 | Drag the VRU peripheral from the Generic PG to the VRU PG. A message appears asking if you are sure you want to move the peripheral to a different PG. Click Yes to confirm. |
| Step 7 | Rename the Generic PG to CUCM PG and change the Client type to CUCM . |
| Step 8 | Click Save . Note Make sure to record the Logical Controller ID of the new VRU PG. You need to enter it when you install the PG. | Note | Make sure to record the Logical Controller ID of the new VRU PG. You need to enter it when you install the PG. |
| Note | Make sure to record the Logical Controller ID of the new VRU PG. You need to enter it when you install the PG. |

| Note | Make sure to record the Logical Controller ID of the new VRU PG. You need to enter it when you install the PG. |
|---|---|

| Step 1 | Add a new VRU PG alongside the Generic PG on both Side A and Side B VMs of the Generic PG machine. On the VRU PG, choose Start > All Programs > Unified CCE Tools > Peripheral Gateway Setup . |
|---|---|
| Step 2 | In the Instance Component section, click Add . |
| Step 3 | Click Peripheral Gateway . |
| Step 4 | In the Peripheral Gateways Properties dialog, do the following: Check the Production Mode check box. Check the Auto start at system start up check box. Check the Duplexed Peripheral Gateway check box. From the PG Node Properties ID drop-down list, select PG3 . Select the appropriate side (Side A or Side B). In the Client Type Selection section, add VRU to the Selected Types. Click Next . |
| Step 5 | In the Peripheral Gateway Managers section of the Peripheral Gateway Component Properties dialog box, click Add . |
| Step 6 | Select VRU and PIM1 and click OK . Enter the VRU PIM details. |
| Step 7 | In the Logical controller ID field, enter the Logical controller ID of the VRU PG that you created previously in PG Explorer. |
| Step 8 | In the Device Management Protocols Properties dialog box, do the following: For Side A PG: Select Side A preferred . For Side A properties, select CallRouter is local . For Side B properties, select CallRouter is remote (WAN) . For Side B PG: Select Side B preferred . For Side A properties, select CallRouter is remote (WAN) . For Side B properties, select CallRouter is local . For both sides: Accept the default in the Usable Bandwidth (kbps) field. Accept the default in the Heartbeat Interval (100ms) field. Click Next . |
| Step 9 | In the Peripheral Gateway Network Interfaces dialog box, complete the interface fields: Enter the Private and Visible network interface hostnames. For the PG, use the same hostnames for private and private high.
                                             For the router, enter the hostname of the Unified CCE Rogger Side A for the Router visible A and Router visible A high interfaces.
                                             Enter the hostname of the Unified CCE Rogger Side B for the Router visible B and Router visible B high interfaces. For the Side A PG, in the Private Interfaces section, click QoS . Check Enable QoS and click OK . For both the Side A and Side B PGs, in the Visible Interfaces section, click QoS . Check Enable QoS and click OK . Click Next . |
| Step 10 | In the Check Setup Information dialog box, click Next . |
| Step 11 | In the Setup Complete dialog box, click Finish . |

| Step 1 | Open Peripheral Gateway Setup. |
|---|---|
| Step 2 | Select PG. |
| Step 3 | Click Edit . |
| Step 4 | In the Client Type Selection section, remove VRU . |
| Step 5 | Click Next . |
| Step 6 | In the Peripheral Gateway Component Properties dialog box, remove the VRU PIMs that were used for connecting to VRU and click Next . |
| Step 7 | In the Device Management Protocol Properties dialog box, click Next . |
| Step 8 | In the Check Setup Information dialog box, click Next . |
| Step 9 | Check the Yes, start the Unified ICM/CC Node Manager check box and click Finish . |