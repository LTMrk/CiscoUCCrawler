  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN - 63945 - Memory on Some SX300 Cards Might Have an Out of Specification Component - Replace on Failure
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63945.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/639/fn63945.html)


Updated:January 18, 2019
Document ID:FN63945
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
|  1.0   |  11-Jul-16   |  Initial Release   |  
|  10.0   |  13-Oct-17   |  Migration to new field notice system   |  
|  10.1   |  18-Jan-19   |  Fixed Broken Image Links   |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
|  UCSC-F-FIO-1000PS=   |   |  
|  UCSC-F-FIO-1300PS=   |   |  
|  UCSC-F-FIO-2600PS=   |   |  
|  UCSC-F-FIO-1000PS   |   |  
|  UCSC-F-FIO-1300PS   |   |  
|  UCSC-F-FIO-2600PS   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf34445](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf34445)  | There were no defects filed with this field notice at the time of publication.  |  
### Problem Description
A very small number of PCIe flash storage cards were manufactured with an out of specification component that can cause the system to have performance issues. It is recommended that customers who are impacted by this issue replace their server cards. There is no risk to customer data.
### Background
A component of the PCIe memory card was not within specifications. There is no risk to customer data.
If the part fails:
  * The card might draw greater than two amps on the PCIe bus, but will not exceed three amps. In a worst case scenario, the card's thermal protection would initiate a shutdown which will protect the card and the system.
  * The card might prematurely trigger a power throttling event that would limit the performance of the card.


### Problem Symptom
There are two potential symptoms:
  * The card's thermal protection could initiate a shutdown in order to protect the card and the system.
  * The card might trigger a power throttling event that would limit the performance of the card.


### Workaround/Solution
It is recommended that customers replace their cards if they have been shipped these cards.
In order to identify if you are impacted, retrieve the serial number of the card and then check in the Serial Number Validation Tool in order to determine if the card is impacted. Only those that are impacted should be replaced.
If the unit is affected, contact the Technical Assistance Center (TAC) in order to request a Return Material Authorization (RMA) for a replacement card.
### How To Identify Affected Products
  1. Log in to the Cisco Integrated Management Controller for the server(s) that contains potentially affected FusionIO card(s).
  2. Click **Launch KVM Console** in order to open a KVM session.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63945_nmuy921547509817126.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63945_nmuy921547509817126.png "Related image, diagram or screenshot.")  
  

  3. Enter the **fio-status** command. [![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63945_nmuyac1547509829122.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63945_nmuyac1547509829122.png "Related image, diagram or screenshot.")  
  

  4. Confirm whether the listed Product Number is one of these strings. If it is not one of these character strings, the unit is not affected.  
  
PFIO1000MPS  
PFIO1300MPS  
PFIO2600MPS  

  5. Note the serial number and enter it into the [Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63945) for this Field Notice in order to determine if affected.
  6. If the unit is affected, contact the TAC in order to request an RMA for a replacement card.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m4-rack-server/model.html)
  * [UCS C240 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m4-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63945.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63945.html)
