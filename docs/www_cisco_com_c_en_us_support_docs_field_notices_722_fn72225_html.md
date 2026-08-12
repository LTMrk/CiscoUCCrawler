  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN - 72225 - SSD Timeouts Might Cause IO Operations to Halt and Lead to Premature Failure of the Drive - BIOS/Firmware Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72225.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/722/fn72225.html)


Updated:September 28, 2021
Document ID:FN72225
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 21-Sep-21  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| UCS-SD38TK1X-EV   |   |  
| UCS-SD38TK1X-EV=   | Part Alternate   |  
| UCS-SD76TK1X-EV   |   |  
| UCS-SD76TK1X-EV=   | Part Alternate   |  
| UCS-SD15TK1X-EV   |   |  
| UCS-SD15TK1X-EV=   | Part Alternate   |  
| UCS-SD38TKB1X-EV   |   |  
| UCS-SD38TKB1X-EV=   | Part Alternate   |  
| UCS-SD76TKB1X-EV   |   |  
| UCS-SD76TKB1X-EV=   | Part Alternate   |  
| UCS-SD15TKB1X-EV   |   |  
| UCS-SD15TKB1X-EV=   | Part Alternate   |  
| UCS-SD32TK3X-EP   |   |  
| UCS-SD32TKB3X-EP   |   |  
| UCS-SD32TK3X-EP=   | Part Alternate   |  
| UCS-SD32TKB3X-EP=   | Part Alternate   |  
| HX-SD15TK1X-EV   |   |  
| HX-SD15TK1X-EV=   |   |  
| HX-SD15TKB1X-EV   |   |  
| HX-SD15TKB1X-EV=   |   |  
| HX-SD32TK3X-EP   |   |  
| HX-SD32TK3X-EP=   |   |  
| HX-SD32TKB3X-EP   |   |  
| HX-SD32TKB3X-EP=   |   |  
| HX-SD38TK1X-EV   |   |  
| HX-SD38TK1X-EV=   |   |  
| HX-SD38TKB1X-EV   |   |  
| HX-SD38TKB1X-EV=   |   |  
| HX-SD76TK1X-EV   |   |  
| HX-SD76TK1X-EV=   |   |  
| HX-SD76TKB1X-EV   |   |  
| HX-SD76TKB1X-EV=   |   |  
| APIC-SD38TK1X-EV   |   |  
| APIC-SD38TK1X-EV=   |   |  
| UCSX-SD15TK1X-EV   |   |  
| UCSX-SD15TK1X-EV=   |   |  
| UCSX-SD32TK3X-EP   |   |  
| UCSX-SD32TK3X-EP=   |   |  
| UCSX-SD38TK1X-EV   |   |  
| UCSX-SD38TK1X-EV=   |   |  
| UCSX-SD76TK1X-EV   |   |  
| UCSX-SD76TK1X-EV=   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvy52309](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvy52309)  | SSD Timeout - Drive goes to failure mode and stop current operation  |  
### Problem Description
Certain Solid State Drive (SSD) models might detect a Logical Block Address (LBA) mismatch condition and halt the drive IO operation. The drive will no longer be recoverable if this condition occurs.
### Background
Certain high capacity SSD models are composed of 512Gb Flash memory chips. When reading the data from this Flash memory chip, the impacted drive firmware mistakenly drops one bit of the physical data address, which causes an internal mismatch condition. Because user-data stored in the Flash memory is protected by the LBA seeded cyclic redundancy check (CRC), the drive correctly detects the address mismatch and stops drive operation.
### Problem Symptom
The drive will experience sudden unexpected failure and will not recover by a power cycle.
### Workaround/Solution
This issue is fixed in the drive firmware 0103 and later. Customers should upgrade to these software bundles (or later), which contain the fixed drive firmware.  
| Platform  | Release  |  
| --- | --- |  
| UCS B-Series Blade Server Software  |  [UCS Infrastructure and UCS Manager Software - Release 4.1(3e)](https://software.cisco.com/download/home/283612660/type/283655658/release/4.1\(3e\)) or [UCS B-Series Blade Server Software - Release 4.2(1f)](https://software.cisco.com/download/home/283853163/type/283655681/release/4.2\(1f\))  |  
| UCS C-Series Rack-Mount UCS-Managed Server Software  |  [Release 4.1(3e)](https://software.cisco.com/download/home/283862063/type/283655681/release/4.1\(3e\)) or [Release 4.2(1f)](https://software.cisco.com/download/home/283862063/type/283655681/release/4.2\(1f\))  |  
| UCS C220 M5 Rack Server Software  | [Release 4.1(3d)](https://software.cisco.com/download/home/286318809/type/283850974/release/4.1\(3d\))  |  
| UCS C240 M5 Rack Server Software  | [Release 4.1(3d)](https://software.cisco.com/download/home/286318800/type/283850974/release/4.1\(3d\))  |  
| UCS C240 M6 Rack Server Software  | [Release 4.2(1b)](https://software.cisco.com/download/home/286329285/type/283850974/release/4.2\(1b\))  |  
| UCS C220 M6 Rack Server Software  | [Release 4.2(1b)](https://software.cisco.com/download/home/286329281/type/283850974/release/4.2\(1b\))  |  
For more details on how to use the Host Update Utility (HUU) to update disk drive firmware, see [Cisco UCS C-Series Rack Servers End-User Guides](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-user-guide-list.html).
For more details on how to upgrade the disk firmware using Cisco UCS Manager, see [Cisco UCS Manager Firmware Management Guides](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-manager/products-installation-guides-list.html).
**Note:** By default, a Host Firmware Package (HFP) will exclude Local Disk firmware. In order to ensure that you can manually modify your HFP to include the Local Disk firmware, uncheck the **Local Disk** check box in the Excluded Components section.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img1.jpg "Related image, diagram or screenshot.")
### How To Identify Affected Products
This issue only impacts the drive Product IDs (PIDs) mentioned in the Products Affected section. Of these impacted PIDs, only those drives that run firmware version 0102 are affected. Drives which match the PIDs in the Products Affected section and have the 0103 and later firmware versions are fixed and do not require an update. Drives which do not match the the PIDs in the Products Affected section are not impacted, even though their firmware version might appear to be an earlier version.
There are several ways to identify the PID and firmware based on the preferred management utility.
**UCS Manager Managed Servers**
The most direct method to quickly gather all drive details from Unified Computing System Manager (UCS Manager) managed servers is to use the Managed Object Browser (MOB) built in to the UCS Manager. Input your IP address into the query and open the link in a browser. Note that in this example, the drive does not match the PID in the Products Affected section and is therefore not impacted.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img2.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img2.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img3.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img3.jpg "Related image, diagram or screenshot.")
In order to directly view individual server drive models and firmware, navigate to the UCS Manager Virtual IP (VIP) page in your browser. In the Navigation Pane (left-hand side), choose **Equipment > Rack Mount > Servers** or **Equipment > Chassis > Servers**. In the Action Pane (middle of the screen), click the **Inventory > Storage > Disks** tabs. Here you can double-click each individual disk to view more details, which includes Model and Firmware. In this example, the drive PID matches an entry in the Products Affected section and the firmware version 0102. This is an impacted drive.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img33.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img33.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img38.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img38.jpg "Related image, diagram or screenshot.")
**Standalone Rack Servers (Cisco IMC Managed)**
For Cisco IMC Managed servers, navigate to the Cisco IMC IP. In order to view the PIDs of the installed drives, navigate to the **Compute** page. Click the **PID Catalog > HDD**tabs. Verify the Product ID against the Products Affected table.
In order to view the firmware running on any potentially impacted HDDs, navigate to the **Storage** page and choose the appropriate storage controller. Click the **Physical Drive Info** tab and check the individual **Physical Drives** check boxes. As the PID is listed in the Products Affected section and the firmware is 0102, this is an impacted drive.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img39.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img39.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img42.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72225img42.png "Related image, diagram or screenshot.")
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M5 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m5-rack-server/model.html)
  * [UCS C220 M6 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m6-rack-server/model.html)
  * [UCS C240 M5 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m5-rack-server/model.html)
  * [UCS C240 M6 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m6-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72225.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72225.html)
