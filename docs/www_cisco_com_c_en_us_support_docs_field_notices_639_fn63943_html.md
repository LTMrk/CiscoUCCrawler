  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack-Mount UCS-Managed Server Software](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-mount-ucs-managed-server-software/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-mount-ucs-managed-server-software/products-field-notices-list.html)


# Field Notice: FN - 63943 - Memory Leak in UCS-C Cisco Integrated Management Controller (CIMC) Might Cause Memory Exhaustion for Systems with Extended Up-Times - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63943.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/639/fn63943.html)


Updated:October 13, 2017
Document ID:FN63943
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
|  1.0   |  18-Aug-16   |  Initial Release   |  
|  10.0   |  13-Oct-17   |  Migration to new field notice system   |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
|  C260-BASE-2646   |   |  
|  R460-4640810   |   |  
|  UCSC-C22-M3L   |   |  
|  UCSC-C22-M3S   |   |  
|  UCSC-C220-M3L   |   |  
|  UCSC-C220-M3S   |   |  
|  UCSC-C220-M4L   |   |  
|  UCSC-C220-M4S   |   |  
|  UCSC-C24-M3L   |   |  
|  UCSC-C24-M3S   |   |  
|  UCSC-C24-M3S2   |   |  
|  UCSC-C240-M3L   |   |  
|  UCSC-C240-M3S   |   |  
|  UCSC-C240-M4L   |   |  
|  UCSC-C240-M4S   |   |  
|  UCSC-C240-M4S2   |   |  
|  UCSC-C240-M4SX   |   |  
|  UCSC-C240-SNEBS   |   |  
|  UCSC-C3160   |   |  
|  UCSC-C420-M3   |   |  
|  UCSC-C460-M4   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCun88303 ](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCun88303)  | CIMC Memory Leak : Can't SSH/HTTP to CIMC  |  
| [CSCus63934](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus63934)  | CIMC memory leak observed in C-series managed by UCS Manager  |  
### Problem Description
A memory leak in the Cisco Integrated Management Controller (CIMC) software might cause systems with extended up-times to run out of memory.
### Background
A memory leak has been discovered during storage operations. The leak is slow, and users that run Cisco UCS C-Series servers (standalone) or the Cisco Unified Computing System Manager (UCSM) with C-Series integration might discover that memory becomes exhausted. When memory becomes exhausted, communication is lost with the CIMC.
**Note** : The B-Series chassis are not impacted. 
### Problem Symptom
Most customers will first notice this issue when the communication with the CIMC is affected. The disruption in CIMC communication indicates that there is a problem. Customers can then act before the Operating System (OS) (business) is impacted.
### Workaround/Solution
Until the software is released that corrects this issue, Cisco recommends that users monitor the free memory of their CIMC and plan a reload if the memory nears exhaustion. In order to avoid this issue, Cisco recommends that users upgrade their systems as shown in the tables that follow.
For C-Series Standalone Software (CIMC):   
| Version  | Approximate FCS Date  |  
| --- | --- |  
| 1.4(x)   | not impacted  |  
| 1.5(1x)  | Not Planned; upgrade to 1.5(3h) or later  |  
| 1.5(2x)  | Not Planned; upgrade to 1.5(3h) or later  |  
| 1.5(3h)   | cisco.com planned end of June 2015  |  
| 1.5(4g)   | cisco.com April 20, 2105  |  
| 1.5(6x)   | Not Planned Upgrade to 1.5(7f) when released  |  
| 1.5(7f)   | cisco.com planned: mid July  |  
|   |   |  
| 2.0(1c)   | Not Planned; Upgrade to 2.0(3i) or later  |  
| 2.0(2x)   | Not Planned; Upgrade to 2.0(3i) or later  |  
| 2.0(3i)   | cisco.com: March 13, 2015  |  
| 2.0(4c)   | cisco.com : May 15, 2015  |  
| 2.0(6d)   | cisco.com : June 6, 2015  |  
For UCSM Software:   
| Version  | Approximate FCS Date  |  
| --- | --- |  
|   |   |  
| 2.1(3h)   | End of June   |  
|   |   |  
| 2.2(1h)   | Mid June   |  
| 2.2(3f)   | cisco.com March 5, 2015  |  
| 2.2(5a)   | cisco.com June 5, 2015   |  
|   |   |  
| 3.0(1)   | Not Planned; upgrade to 3.0(2) or later  |  
| 3.0(2d)   | End of June  |  
  

**Note** : Refer to the [Cisco UCS C-Series Rack-Mount Server BIOS Upgrade Guide](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/bios/b_Upgrading_BIOS_Firmware.html) for information about how to upgrade the UCS C-Series servers.
**Note** : Refer to the [Cisco UCS C-Series Rack Servers](http://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/tsd-products-support-series-home.html) web page for information about the UCS C-Series software releases.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m4-rack-server/model.html)
  * [UCS C240 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m4-rack-server/model.html)
  * [UCS C-Series Rack-Mount UCS-Managed Server Software](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-mount-ucs-managed-server-software/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63943.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63943.html)
