  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN - 63737 - UCS C-Series Rack Servers - 1 TB SATA HDD Crash - Replace on Failure
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/637/fn63737.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/637/fn63737.html)


Updated:February 4, 2019
Document ID:FN63737
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
|  1.0   |  29-Jan-16   |  Initial Release   |  
|  10.0   |  13-Oct-17   |  Migration to new field notice system   |  
|  10.1   |  04-Feb-19   |  Fixed Broken Image Links   |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
|  A03-D1TBSATA=   |   |  
|  A03-D1TBSATA   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf34445](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf34445)  | There were no defects filed with this field notice at the time of publication.  |  
### Problem Description
It is possible that 1 TB Hard Disk Drives (HDD) in a Unified Computing System (UCS) C-Series Rack Server could fail. Initially customers might observe data errors and/or eventually the HDD will not function.
### Background
Cisco's UCS C-Series Rack Servers with 1 TB HDDs from one vendor (bounded by a serial number range) could fail at a higher than expected rate. This is due to a quality issue with the internal crash stop that shortens the HDD operational lifespan.
The A03-D1TBSATA HDD is hot swappable, so Cisco recommends to hot swap the drives in order to eliminate any issues due to this HDD failure. The steps to complete this hot swap are:
  1. Stop all I/Os to the drive.
  2. Slightly pull the drive from the system connector.
  3. Let the drive sit in the system for 30 seconds while the spindle motor spins down and the heads park.
  4. Remove the drive from the system and install the replacement.


If you are not able to hot swap HDDs, the entire server must be powered down. This should only be performed when the replacement drive is ready to install (for example, mounting brackets).
Tests suggest that there will not be an issue with UCS C-Series Rack Servers that run at normal operations between 35 C and 50 C.
In summary:
  * Any crash stop affected drive (identified by serial number) that is powered down runs the risk that it will not come back up. If you do not have to, do not power down drives.
  * If you have to power down a drive, you will be less likely to exhibit an unlatch DNR the warmer it is and with a smaller amount of time powered off. This has been very successful at a temperature of 35 C or higher.


### Problem Symptom
Cisco was informed by it's supplier, Seagate, that Seagate's supplier of the crash stops used in the 1 TB disk drives had a marginal lot of crash stops that were too "sticky". This causes the actuator to fail on occasion.
### Workaround/Solution
The A03-D1TBSATA HDD is hot swappable, so Cisco recommends to hot swap the drives in order to eliminate any issues due to this HDD failure. The steps to complete this hot swap are:
  1. Stop all I/Os to the drive.
  2. Slightly pull the drive from the system connector.
  3. Let the drive sit in the system for 30 seconds while the spindle motor spins down and the heads park.
  4. Remove the drive from the system and install the replacement.


If you are unable to hot swap HDDs, the entire server must be powered down. This should only be performed when the replacement drive is ready to install (for example, mounting brackets).
See the How to Identify Affected Products section in order to determine if you have an affected HDD.
### How To Identify Affected Products
Affected hard disk drives are identified by serial number, and can be used in Cisco UCS B-Series Blade Servers and UCS C-Series Rack Servers. If you have the affected drive installed on a Cisco UCS server, you can retrieve the serial number from your drive and use the [FN 63737 Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63737) link in order to confirm whether the unit is on the list of affected units.
**Check the HDD Serial Number on UCS B-Series Blade Servers**
**Note:** This method also applies to UCS C-Series Rack Servers that use integrated UCS Manager (UCSM) management.
  1. Log in to the UCSM.
  2. Choose **Chassis > Server > Inventory > Storage**.
  3. Note the serial number for each hard disk drive that matches a Product ID (PID) noted in the Products Affected section of this Field Notice. If the displayed serial number is longer than 8 alphanumeric digits, note only the first 8 digits. See this example: 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/637/fn63737_n1941b1548804890043.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/637/fn63737_n1941b1548804890043.png "Related image, diagram or screenshot.")
  4. If desired, the CLI can also be used to capture hard disk drive serial numbers. See this example: 
```
show local-disk detail expand
```

[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/637/fn63737_n1942z1548804907384.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/637/fn63737_n1942z1548804907384.png "Related image, diagram or screenshot.")
  5. After you collect the serial numbers from potentially affected hard drives, use the [FN 63737 Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63737) in order to determine if the HDDs are affected.


**Check the HDD Serial Number on UCS C-Series Rack Servers**
  1. Log in to the Cisco Integrated Management Controller (CIMC).
  2. Choose **Inventory > Storage > Physical Drive Info**.
  3. For C-Series CIMC users, the manufacturer model number is displayed in the Product ID field instead of the orderable Product ID. The model number of the affected drive is **ST91000640NS**. An example is shown here: 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/637/fn63737_n1943e1548804929401.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/637/fn63737_n1943e1548804929401.png "Related image, diagram or screenshot.")
  4. If desired, the CLI can also be used to capture hard disk drive information. See this CLI example: 
```
test-system /chassis/storageadapter # **scope physical-drive 12**
test-system /chassis/storageadapter/physical-drive # **show detail**
Physical Drive Number 12:
Controller: SAS
Health: Good
Status: Unconfigured Good
Manufacturer: ATA
Model: ST91000640NS
Predictive Failure Count: 0
Drive Firmware: CC02
Coerced Size: 952720 MB
Type: HDD
test-system /chassis/storageadapter/physical-drive # **show inquiry-data**
Physical Drive Number 12:
Controller: SAS
Info Valid: Yes
Info Invalid Cause: 
Vendor: ATA
Product ID: ST91000640NS
Drive Firmware: CC02
Drive Serial Number: 9XG2K0YP
```

  5. Note the serial numbers of any HDDs that have a Model/Product ID of **ST91000640NS**.
  6. After you collect the serial numbers from potentially affected hard drives, use the [FN 63737 Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63737) in order to determine if the HDDs are affected.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m4-rack-server/model.html)
  * [UCS C240 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m4-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/637/fn63737.html)
