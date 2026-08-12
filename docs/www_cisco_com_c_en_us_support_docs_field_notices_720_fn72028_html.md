  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Conferencing](https://www.cisco.com/c/en/us/support/conferencing/category.html)
  * [Cisco Meeting Server](https://www.cisco.com/c/en/us/support/conferencing/meeting-server/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/conferencing/meeting-server/products-field-notices-list.html)


# Field Notice: FN - 72028 - UCS 6324 and 6332 Fabric Interconnects Might Become Unresponsive After 3.2 Years of Operation - BIOS/Firmware Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/720/fn72028.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/720/fn72028.html)


Updated:June 1, 2021
Document ID:FN72028
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 02-Feb-21  | Initial Release  |  
| 1.1  | 16-Feb-21  | Updated the Problem Symptom, Workaround/Solution, and How to Identify Affected Products Sections  |  
| 2.0  | 22-Apr-21  | Updated the Products Affected, Defect Information, Problem Description, Problem Symptom, Workaround/Solution, and How to Identify Affected Products Sections  |  
| 2.1  | 01-Jun-21  | Add information on how to use serial numbers to identify units that may potentially be impacted (still requires secondary validation)  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| UCS-FI-M-6324=   |   |  
| UCS-FI-M-6324   |   |  
| CIT3-FI-M-6324   |   |  
| UCS-FI-6332   |   |  
| UCS-FI-6332=   | Part Alternate   |  
| UCS-FI-6332-U   |   |  
| HX-FI-6332   |   |  
| UCS-MAFI-6332   |   |  
| HX-UC-FI6332   |   |  
| HX-D-FI6332   |   |  
| UCS-R2F-FI-6332   |   |  
| UCS-FI-6332-16UP=   | Part Alternate   |  
| UCS-FI-6332-16UP-U   |   |  
| UCS-FI-6332-16UP   |   |  
| HX-FI-6332-16UP   |   |  
| UCS-NL-FI6332-16UP   |   |  
| HX-NL-FI6332-16UP   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvw51222](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvw51222)  | UCS-FI-M-6324 - 500IT SSD hangs after 3.2 years power on hours  |  
| [CSCvw93034](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvw93034)  | UCS-FI-6332 - 500IT SSD hangs after 3.2 years power on hours  |  
### Problem Description
Because of a flaw in the Solid State Drive (SSD) firmware, the SSD will no longer respond after approximately 3.2 years of operation. A power-cycle of the system will allow the drive to operate for another six weeks before it again ceases to respond.
### Background
After 28,224 hours (~3.2 years) of accumulated Power On Hours (POHs), a memory buffer overrun condition occurs that triggers the firmware event. This causes the drive to become unresponsive until the drive is power-cycled. No data loss will occur when the memory buffer overrun firmware event occurs. A power-cycle restores normal operation of the drive. The drive continues to operate normally for 1008 additional accumulated POHs (6 weeks), at which time the drive will become unresponsive again. Another power-cycle of the drive will re-initiate the 1008 hour window.
### Problem Symptom
UCS-FI-M-6324, UCS-FI-6332, and UCS-FI-6332-16UP with certain SSD models installed will reboot or management processes will crash after 28,224 POHs (~3.2 years).
Depending on the management process that crashes, the system might reboot or Unified Computing System (UCS) Manager might become inaccessible. The SSD's firmware must be reset in order to make it operational again, but from there on the same condition will occur every six weeks of additional POHs.
In order to reset the SSD firmware, pull and reinsert the power cables in order to manually power-cycle the Fabric Interconnect (FI).
### Workaround/Solution
**Workaround**
Manually power-cycle the system in order to temporarily recover from this problem. However, this failure will reappear after 1008 hours (six weeks) of operation. In order to reset the SSD firmware, pull and reinsert the power cables in order to manually power-cycle the FI. A simple reboot of the FI will not cause the SSD firmware to reset.
**Solution**
In order to prevent this issue and corresponding disruption to the network and operations, Cisco recommends to upgrade the SSD firmware proactively before the uptime reaches 28,224 POHs. Refer to the **How to Identify Affected Products** section and follow the firmware upgrade procedure accordingly.
If the system has already been impacted, the SSD firmware upgrade will permanently resolve this defect and prevent future recurrence.
There are two options to upgrade the firmware:
  * Upgrade to the [UCS Infrastructure and UCS Manager Software release](https://software.cisco.com/download/home/283612660/type/283655658) that incorporates the fix for this defect as follows: 
**UCS-FI-M-6324**
    * [Release 4.0(4l) and later](https://software.cisco.com/download/home/283612660/type/283655658/release/4.0\(4l\))
    * [Release 4.1(2c) and later](http://https://software.cisco.com/download/home/283612660/type/283655658/release/4.1\(2c\))
    * [Release 4.1(3b) and later](https://software.cisco.com/download/home/283612660/type/283655658/release/4.1\(3b\))
**UCS-FI-6332 and UCS-FI-6332-16UP**
    * [Release 4.0(4l) and later](https://software.cisco.com/download/home/283612660/type/283655658/release/4.0\(4l\))
    * [Release 4.1(2c) and later](https://software.cisco.com/download/home/283612660/type/283655658/release/4.1\(2c\))
    * [Release 4.1(3c) and later](https://software.cisco.com/download/home/283612660/type/283655658/release/4.1\(3c\))  

  * Raise a Technical Assistance Center (TAC) request to have TAC perform the firmware upgrade for the SSD manually. This can be done without a FI reboot.


See [Cisco UCS Manager Firmware Management Guide, Release 4.1](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Firmware-Mgmt/4-1/b_UCSM_GUI_Firmware_Management_Guide_4-1/b_UCSM_GUI_Firmware_Management_Guide_4-1_chapter_011.html) for instructions on how to upgrade your firmware.
### How To Identify Affected Products
**Via Intersight**
Fabric interconnects that have been claimed in [Intersight](https://intersight.com/) with [Advantage Licensing](https://www.intersight.com/help/getting_started#licensing_requirements) will benefit from the ability to view affected devices directly within Intersight. Users can click the advisories button in the top right corner, select ‘View All’ at the bottom of the list, navigate to Field Notices and view any affected devices. An example of the Field Notice in Intersight is below:
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72028img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72028img1.jpg "Related image, diagram or screenshot.")
**UCS-FI-M6324**
The SSD installed in the FI and its firmware version can be determined from the Cisco NX-OS CLI. If the SSD model is Micron_M500IT* and the firmware version is NOT CZ03.00 or later, then a firmware upgrade is required.
SSH to the FI VIP and enter these commands:

```
**connect nxos a
show system internal file /proc/scsi/scsi
exit
connect nxos b
show system internal file /proc/scsi/scsi**
```

```
MINI-FI-B(nxos)# **show system internal file /proc/scsi/scsi**
Attached devices:
Host: scsi4 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: Micron_M500IT_MT Rev: CZ01
  Type:   Direct-Access                    ANSI  SCSI revision: 05
```

**Note:** On the first boot after an upgrade, the `**show system internal file /proc/scsi/scsi**`command still shows the old firmware. This file is only updated during the boot process. A second reboot is required after the upgrade process to use this method.
**UCS-FI-6332 and UCS-FI-6332-16UP**
The SSD installed in the FI and its firmware version can be determined from the Cisco NX-OS CLI. If the SSD model is Micron_M500IT* and the firmware version is NOT MC03 or MU05 or later, then a firmware upgrade is required.
SSH to the FI VIP and enter these commands:

```
**connect nxos a
show system internal file /proc/scsi/scsi
exit
connect nxos b
show system internal file /proc/scsi/scsi**
```

```
3GFI-FI-B(nxos)# **show system internal file /proc/scsi/scsi**
Attached devices:
Host: scsi4 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: Micron_M500IT_MT Rev: MC02
  Type:   Direct-Access                    ANSI  SCSI revision: 05
```

**Note:** On the first boot after an upgrade, the `**show system internal file /proc/scsi/scsi**`command will still show the old firmware. This file is only updated during the boot process. A second reboot is required after the upgrade process in order to use this method.
**Current POHs Check**
If you currently run firmware that is later than Version 3.1(3a) or 3.2(1d), then the current POH count can be reviewed from a technical support file. See [Visual Guide to Collect UCS Tech Support Files - B, C and S Series](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-infrastructure-ucs-manager-software/211587-Visual-Guide-to-collect-UCS-Tech-Support.html) for more information.
  1. Check the “var/sysmgr/sam_logs/smartctllog.<timestamp>" file for each FI and search for "Power_On_Hours". The "Raw_Value" is the number of POHs at the time the file was generated. Here is an example with Raw_Value underlined: 
```
9 Power_On_Hours     0x0012  100  100  000  Old_age  Always   -   _51074_
```

  2. This file is typically generated weekly. In order to calculate the actual POHs for the drive, take the Raw_Value number in the file and add the number of hours since the file was generated. The date the file was generated is in the filename, as well as at the top of the file as shown in this example: 
```
Local Time is:    Fri Apr  9 01:57:40 2021 EDT
```



**SSD Update Verification**
UCS-FI-M-6324 - If the SSD model is Micron_M500IT* and the firmware version is CZ03 or later, the firmware has been successfully upgraded.
UCS-FI-6332 and UCS-FI-6332-16UP - If the SSD model is Micron_M500IT* and the firmware version is MC03 or MU05 or later, the firmware has been successfully upgraded.
  * If you manually updated the SSD firmware via TAC assistance, the running SSD firmware can be verified immediately after an upgrade with this command: 
```
**smartctl -a /dev/sda**
```

  * If you upgraded via a UCS Infrastructure and UCS Manager Software Release, the running SSD firmware can be confirmed seven days after an upgrade. A UCS Manager technical support file will include an updated "smartctl" log file which will display the firmware version that is currently in use. 
    1. See [Visual Guide to Collect UCS Tech Support Files - B, C and S Series](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-infrastructure-ucs-manager-software/211587-Visual-Guide-to-collect-UCS-Tech-Support.html) for information on how to collect a UCS Manager technical support file seven or more days after an upgrade.
    2. Check the file “var/sysmgr/sam_logs/smartctllog.<timestamp>" file for each FI and verify the firmware version.
**Note:** On the first boot after an upgrade, the `**show system internal file /proc/scsi/scsi**`command still shows the old firmware. This file is only updated during the boot process. A second reboot is required after the upgrade process in order to use this method.


### Serial Number Validation
The Cisco Support Assistant (CSA) can help verify whether a device is impacted by the issue that is described in this Field Notice. To check the device, either enter the serial number in the CSA on the right side of this page or click the following URL: <https://cs.co/FNSNV>.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/720/fn72028.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72028.html)
