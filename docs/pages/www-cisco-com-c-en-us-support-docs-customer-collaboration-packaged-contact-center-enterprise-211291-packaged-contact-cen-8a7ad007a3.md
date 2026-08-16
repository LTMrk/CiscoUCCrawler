---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-packaged-contact-center-enterprise-211291-packaged-contact-cen-8a7ad007a3
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/packaged-contact-center-enterprise/211291-Packaged-Contact-Center-Enterprise-PCCE.html
retrieved_at: 2026-08-16T19:22:32.599836+00:00
---

Packaged Contact Center Enterprise (PCCE) 11.5 Deployment Errors On VM Hosts Screen

# Packaged Contact Center Enterprise (PCCE) 11.5 Deployment Errors On VM Hosts Screen

Updated: May 25, 2017

Document ID: 211291

Contents

## Contents

## Introduction

This document describes how to troubleshoot and fix invalid datastores issue on VM Hosts screen during PCCE deployment.

## Prerequisites

Cisco recommends that you have knowledge of these topics:

- PCCE

- U nified Computing System ( UCS)

- RAID Configuration

## Components Used

PCCE 11.5

Hardware - UCS 240 M4SX

RAID Configuration Utility

## Problem

To setup PCCE 11.5 deployment, you need to log in to webadmin page from AW/HDS server. On the VM hosts screen, PCCE asks for ESXi host credentials.  After you enter credentials and click next, ESXi credentials are verified. Afer verification, ESXi queries and compares current hardware configurations.

If the hardware configuration is invalid, PCCE webadmin returns error message "Invalid Host- Error reason-Invalid Datastores: Must match expected configuration."

On C240 M4SX server, R edundant Array Of Independent Disks ( RAID) manuall configuration is not necessary. The disk array configuration for this server was set up to match the requirement of PCCE.

Verify the settings as follows:

- Virtual Drive Info: RAID 5 with 5 (Physical Disks) * 4 (Virtual Drives/Datastores)

- Stripe Size: 128KB

- Write Policy: Write Back with BBU

- Read Policy: Read Ahead Always

Scenario1

Scenario2

## Solution

Scenario1

Error on screen says there is a mismatch with expected datastore configuration. PCCE 11.5 requires 4 datastores to be configured with specific size mentioned as below. However, in scenario 1, there are only 3 datastores configured.

Datastore1 - Min:1104 GB and Max:1108 GB

Datastore2 - Min:1104 GB and Max:1115 GB

Datastore3 - Min:1104 GB and Max:1108 GB

Datastore4 - Min:1104 GB and Max:1108 GB

VMValidation logs show 3 data stores.

Found HD(s) (GB): [VMDatastoreData[ sizeInGB=271 , name=local-irvtcmvmhprd00], VMDatastoreData[ sizeInGB=2227 , name=datastore01-irvtcmvmhprd00], VMDatastoreData[ sizeInGB=2506 , name=datastore02-irvtcmvmhprd00]]

Verify your RAID configuration with RAID config Validator Utility>PackagedCCEraidConfigValidator-11.5.zip.

https://software.cisco.com/download/release.html?mdfid=284360381&softwareid=284416107&release=11.5(1... >

Then, run this command java -jar PackagedCCEraidConfigValidator-10.5.jar <IP Address of the Side A server> <username> <password>.

For example: C:\Users\Administrator\Desktop>java -jar PackagedCCEraidConfigValidator-10.5.jar xx.xx.xxx.xxx userName password

From RAID config. validate output, we see wrong number of Datastores were configured.

IOS profile C240M4 matches C240M4.2.0.8b.0.080620151546; checking data stores. Actual number of data stores found = 3 Expected number of data stores = 4 Wrong number of data stores found BIOS profile C240M4 matches C240M4.2.0.8b.0.080620151546; checking data stores. Actual number of data stores found = 3 Expected number of data stores = 4 Wrong number of data stores found BIOS profile C240M4 matches C240M4.2.0.8b.0.080620151546; checking data stores. Actual number of data stores found = 3 Expected number of data stores = 4 Wrong number of data stores found BIOS profile C240M4 matches C240M4.2.0.8b.0.080620151546; checking data stores. Actual number of data stores found = 3 Expected number of data stores = 4 Wrong number of data stores found XXX *** Validation Complete -- RAID Configuration is Invalid *** XXX

Reconfigure the RAID with these steps:

Ensure that you have following settings in your environment: 1. The UCS C240 M4 SX server is a brand new one with only RAID configured with some level. There is no data. Any existing data will be lost. 2. No changes were made to the Adapter Settings under Adapter Settings in the webBIOS screen.

All the RAID configuration is done with LSI MegaRAID WEBBIOS CU(Configuration Utility). We use this procedure to create  RAID configurations on LSI MegaRAID SAS controllers.

Step 1. Power on the UCS server. Ensure Quiet Boot was disabled in BIOS. Step 2. When you see LSI MegaRAID SAS BIOS screen, press Control+H to enter the MegaRAID BIOS configuration utility. The Controller Selection window appears. Step 3. You see a screen with the details of the SAS Controller(s). Step 4. Select the RAID controller which you want to work with. Usually, there is only one listed. Step 5. Select Start . Step 6. You land up at the webBIOS page. This screen lists Physical Drives and Virtual Drives. In the new server there must not be any Virtual Devices ideally. Step 7. We need to delete/clear existing/previous configuration. In the menu list to the left, select Configuration Wizard. Step 8. The WebBIOS Configuration Method window opens. Select the Clear Configuration radio button. Step 9. Click Next . Step 10. Click Yes for the message This is a Destructive Operation!. Step 11. You must not see any Virtual Drives post Step 11. Step 12. Verify that all Physical Drives are in good condition. Step 13. Select Configuration wizard and then select New Configuration radio button in the WebBIOS Configuration Method window. Click Yes for the message This is a Destructive Operation!. Step 14. Select Custom/Manual Configuration. Step 15. You see DG Definition screen shows Physical Drives and Disk Groups. You see a Disk Group DG0. Step 16. Select the first five drives. [Control to select multiple]. Step 17. Click on the Add to Array button.

Note : If you need to undo the changes, click Reclaim.

Step 18. Click on the Accept DG button to add the drives to the Disk Group DG0. Step 19. Select the next five drives. Step 20. Click on the Add to Array button. Step 21. Click on the Accept to DG button to add the drives to the Disk Group DG1. Step 22. Similarly add fives drives to DG2 and DG3. Step 23. You must now have 4 Disk Groups. Step 24. Click Next on the DG Definition Screen. Step 25. The Span Definition screen is displayed. Step 26. Select DG0 on the left side and click Add to SPAN. The DG should be now under the SPAN side. Step 27. Click Next . This leads to the VD Definition screen. You see a VD0 under DG0. Step 28. Configure Virtual Drive (DV). a) For RAID Level, select RAID 5. b) For Stripe Size,select 128KB. c) For Read Policy, select read ahead = always. d) For Write Policy, select write back with bbu. e) Click Update Size to finalize the RAID volume and to determine the size of the resulting volume. It comes to  TB. f) Click Accept to accept the virtual drive definition, VD0. g) Click Next . h) Click back to add the second RAID5 array. Step 29. Select Disk Group 1. Click on Add to span. Click on Next . Follow the instructions in Step 29. Step 30. Repeat this for the other two Disk Groups. Step 31. Click Yes at the BBU warning screen. Step 32. Click Next at the Virtual Live Definition screen to indicate that you have finished defining virtual drives. Step 33. Click Accept at the Configuration Preview screen to accept the RAID configuration. Step 34. Click Yes to save the Configuration. Step 35. Click on Yes to start the drive configuration. Step 36. When finished click Home . Click on Exit in the Menu options in the left pane.

This completes RAID 5 configuration on UCS C240 M4 SX server.

Verifications With Cisco Integrated Management Controller, ensure following settings are configured correctly: 1) Virtual Drive Info: RAID 5 with 5 (Physical Disks) * 4 (Virtual Drives/Datastores) 2) Stripe Size: 128KB 3) Write Policy: Write Back with BBU 4) Read Policy: Read Ahead Always

Scenario 2

For scenario 2, you see 4 data stores were configured. However, the size of data store is not what PCCE expects. It shows doubled the size than expected.

Run RAID config validator utility to see what exactly the cause is. Here is the output:

2017-01-26 13:29:46,423 [main] INFO - BIOS profile C240M4 matches C240M4.2.0.10c.0.032320160820; checking data stores.

2017-01-26 13:29:46,427 [main] INFO - Actual number of data stores found = 4

2017-01-26 13:29:46,427 [main] ERROR - Misconfigured datastores.

2017-01-26 13:29:46,427 [main] INFO - Actual Data Store Size - 2224GB

2017-01-26 13:29:46,427 [main] INFO - Actual Data Store Size - 2231GB

2017-01-26 13:29:46,427 [main] INFO - Actual Data Store Size - 2231GB

2017-01-26 13:29:46,427 [main] INFO - Actual Data Store Size - 2231GB

2017-01-26 13:29:46,427 [main] INFO - Expected Data Store must be between 1104GB and 1108GB

2017-01-26 13:29:46,427 [main] INFO - Expected Data Store must be between 1111GB and 1115GB

2017-01-26 13:29:46,427 [main] INFO - Expected Data Store must be between 1111GB and 1115GB

2017-01-26 13:29:46,427 [main] INFO - Expected Data Store must be between 1111GB and 1115GB

2017-01-26 13:29:46,427 [main] INFO - XXX *** Validation Complete -- RAID Configuration is Invalid *** XXX

Why does it show 2224 GB?

C240 M4SX TRC#1 comes with 20 physical disks each with 300GB of capacity. Refer link - http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtua...

So, based on above datastore requirements, each data store will be of 1200GB (1.2 TB). However, what we see is 2400GB (2.4 TB). Refer this RAID calculator.

http://www.raid-calculator.com/default.aspx

HDD in C240 M4SX TRC#1 came with doubled the capacity of its actual size. PCCE is very restrict with the validation rule as it was tested with defined hardware specifications.

Contact your ordering team to verify ordering guide and order the correct hardware.

References

http://docwiki.cisco.com/wiki/Virtualization_for_Cisco_Packaged_CCE

http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtua...

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_11_5_1/inst...

### Revision History

1.0

24-May-2017

Initial Release

### Contributed by Cisco Engineers

Mayur Vyas

Cisco TAC Engineer

### This Document Applies to These Products

- Packaged Contact Center Enterprise

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-May-2017 | Initial Release |