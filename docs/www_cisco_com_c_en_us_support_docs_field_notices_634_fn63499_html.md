  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN - 63499 - Disk Drive Contamination Causes Premature Failure - Replace on Failure
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/634/fn63499.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/634/fn63499.html)


Updated:May 21, 2018
Document ID:FN63499
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
|  1.0   |  21-Aug-12   |  Initial Release   |  
|  10.0   |  13-Oct-17   |  Migration to new field notice system   |  
|  11.0   |  21-Feb-18   |  Move FN to Fix on Fail   |  
|  11.1   |  21-May-18   |  Fixed Broken Image Links   |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
|  A03-D300GA2   |   |  
|  A03-D300GA2=   |   |  
|  A03-D600GA2   |   |  
|  A03-D600GA2=   |   |  
|  UCS-HDD900GI2F106   |   |  
|  UCS-HDD900GI2F106=   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf34445](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf34445)  | There were no defects filed with this field notice at the time of publication.  |  
### Problem Description
Certain hard disk drives have the possibility of premature failure due to contamination, which is the result of a defective top cover seal. Affected drives can be identified by the serial number and were shipped by Cisco between April 3, 2012 through June 1, 2012.
### Background
A high failure rate of hard disk drives was detected during Ongoing Reliability Testing at the manufacturer's facility, and root cause was determined to be the seal on the top cover. The defective seal causes contamination of the read/write heads, and can result in eventual degraded Bit Error Rate or complete failure of the drive. There is a 50% chance of drive failure within the first 500 hours of operation. The drive manufacturer has taken the corrective action to replace the disk drive top cover gasket Form In Place Gasket material from 3M 4302 heat cured epoxy to Huntsman TX-09 UV cured acrylate.
Drives in operation beyond the first 500 hours of operation should perform normally and not have premature failure.
### Problem Symptom
Symptoms exhibited by affected hard disk drives include increased read/write errors or complete failure.
### Workaround/Solution
Drives in operation beyond the first 500 hours of operation should perform normally and not have premature failure. If a drive fails or experiences a large number of errors, it should be replaced with a standard Return Material Authorization (RMA).
### How To Identify Affected Products
Affected hard disk drives are identified by the serial number, and are applicable for use in Cisco UCS B-Series Blade Servers and UCS C-Series Rack Servers. If you use hard disk drives in the list of affected products at the top of this Field Notice, you can retrieve the serial number from your drive and use the [Field Notice 63499 Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63499) in order to confirm whether the unit is on the list of affected units.
**Check the HDD Serial Number on UCS B-Series Blade Servers**
**Note** : This method also applies to UCS C-Series Rack Servers that use integrated UCS Manager (UCSM).
  1. Log in to UCSM.
  2. Choose **Chassis > Server > Inventory > Storage**.
  3. Note the serial number for each hard disk drive that matches a Product ID noted in the Products Affected section at the top of this Field Notice. If the displayed serial number is longer than 8 alphanumeric digits, note only the first 8 digits. See this example: 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/634/fn63499_m6ichx.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/634/fn63499_m6ichx.png "Related image, diagram or screenshot.")
  4. If desired, the CLI can also be used to capture hard disk drive serial numbers. See this CLI example: 
```
UCSexample1 /chassis/server/raid-controller # **sh local-disk detail expand**

Local Disk: 
ID: 1 
Block Size: 512 
Blocks: 1758174768 
Size (MB): 858483 
Technology: Hdd 
Operability: Operable 
Presence: Equipped 
Product Name: 900GB 6Gb SAS 10K RPM 2.5 in. HDD/hot plug/drive sled mounted 
PID: UCS-HDD900GI2F106 
VID: V01 
Vendor: SEAGATE 
Vendor Description: Seagate Technology LLC 
Serial: 6XS23BLZ 
HW Rev: 0 

ID: 2 
Block Size: 512 
Blocks: 1758174768 
Size (MB): 858483 
Technology: Hdd 
Operability: Operable 
Presence: Equipped 
Product Name: 900GB 6Gb SAS 10K RPM 2.5 in. HDD/hot plug/drive sled mounted 
PID: UCS-HDD900GI2F106 
VID: V01 
Vendor: SEAGATE 
Vendor Description: Seagate Technology LLC 
Serial: 6XS23BV90000M236L2X7 
HW Rev: 0
```

  5. After you collect serial numbers from potentially affected hard drives, check whether they are affected with the [Field Notice 63499 Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63499).


**Check the HDD Serial Number on UCS C-Series Rack Servers**
  1. Log in to Cisco Integrated Management Controller (CIMC).
  2. Choose **Inventory > Storage > Physical Drive Info**.
  3. For C-Series CIMC users, the manufacturer model number is displayed in the Product ID field instead of the orderable Product ID. See this table in order to identify affected model numbers:  
  
| Manufacturer Model  | Product ID  | Product Description  |  
| --- | --- | --- |  
| ST9300605SS  | A03-D300GA2  | 300GB 6Gb SAS 10K RPM SFF HDD/hot plug/drive sled mounted  |  
| ST9600205SS  | A03-D600GA2  | 600GB 6Gb SAS 10K RPM SFF HDD/hot plug/drive sled mounted  |  
| ST9900805SS  | UCS-HDD900GI2F106  | 900GB 6Gb SAS 10K RPM SFF HDD/hot plug/drive sled mounted  |  
  

  4. Note the serial numbers of any hard disk drive(s) which have a Model/Product ID listed in the table. See this example: 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/634/fn63499_m70qke.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/634/fn63499_m70qke.png "Related image, diagram or screenshot.")
  5. After you collect the serial numbers from potentially affected hard drives, check whether they are affected with the [Field Notice 63499 Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63499).


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m4-rack-server/model.html)
  * [UCS C240 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m4-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/634/fn63499.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63499.html)
