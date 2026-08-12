  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-field-notices-list.html)


# Field Notice: FN - 63999 - Cisco IP Conference Station 8831 Series Locally Significant Certificate (LSC) Issue - Software Upgrade Required
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63999.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/639/fn63999.html)


Updated:September 28, 2015
Document ID:FN63999
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Field Notice: FN - 63999 - Cisco IP Conference Station 8831 Series Locally Significant Certificate (LSC) Issue - Software Upgrade Required
### NOTICE: 
### THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME. 
### Revision History  
| Revision  | Date  | Comment  |  
| --- | --- | --- |  
| 1.1  | 28-SEP-2015  | Updated the Problem Description and Problem Symptoms Sections  |  
| 1.0  | 20-AUG-2015  | Initial Public Release  |  
### Products Affected  
| Products Affected  |  
| --- |  
| 8831 - CP-8831-BR-K9 (=)  |  
| 8831 - CP-8831-DC-BR-K9 (=)  |  
| 8831 - CP-8831-DC-EU-K9 (=)  |  
| 8831 - CP-8831-DC-J-K9 (=)  |  
| 8831 - CP-8831-DC-K9 (=)  |  
| 8831 - CP-8831-DC-LA-K9 (=)  |  
| 8831 - CP-8831-DC-TW-K9 (=)  |  
| 8831 - CP-8831-EU-K9 (=)  |  
| 8831 - CP-8831-J-K9 (=)  |  
| 8831 - CP-8831-K9 (=)  |  
| 8831 - CP-8831-K9++ (=)  |  
| 8831 - CP-8831-LA-K9 (=)  |  
| 8831 - CP-8831-TW-K9 (=)  |  
### Problem Description
The Locally Significant Certificates (LSCs) that are installed on the Cisco 8831 Series IP phones are no longer detected when a phone is upgraded from Version 9-3-3-5 to Version 10-3-1-16. 
### Background
It might appear that the phone LSC is lost after an upgrade from Version 9-3-3 to Version 10-3-1-16 or later. The LSC is neither removed nor deleted, but it is not detected by the new software.
### Problem Symptoms
There can be multiple symptoms when this issue is encountered, which include:
  * Your phone might not work.   
  

  * The phone User Interface (UI) might display the _phone is registering_ message after the upgrade, but the phone does not register.   
  

  * The phone UI might display the _network unavailable_ message after the upgrade, but the phone cannot obtain an IP address.   
  

  * The phone security settings show _LSC not installed_.


If this problem exists on your network, all 8831's will show the same or similar symptoms after the upgrade.
If, after the upgrade, any 8831's on the same network register successfully and others do not, there is most likely another problem that happens not related to this field notice. It will depend on the security profile of the endpoints. A non-secure 8831 will register without an LSC, where a secure 8831 will not register.
### Workaround/Solution
In order to maintain the original LSC files, you must complete these steps in order to upgrade the software:
  1. Upgrade from software Version 9-3-3-5 to Version [9-3-3-TO-10-3-1v2](https://software.cisco.com/download/release.html?mdfid=284738433&flowid=46257&softwareid=282074288&release=10.3\(1\)&relind=AVAILABLE&rellifecycle=&reltype=latest).  
  

  2. Upgrade from software Version 9-3-3-TO-10-3-1v2 to Version [10-3-1-16](https://software.cisco.com/download/release.html?mdfid=284738433&flowid=46257&softwareid=282074288&release=10.3\(1\)&relind=AVAILABLE&rellifecycle=&reltype=latest).


If you desire to install the LSC but have not yet installed it, you must upgrade to Version 10.3.1 before the LSC is installed.
**Note** : If you do not use (and have no plans to use) the LSC, you are not affected by this issue.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods: 
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63999.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63999.html)
