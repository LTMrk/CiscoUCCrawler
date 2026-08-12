  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified Customer Voice Portal](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-field-notices-list.html)


# Field Notice: FN - 70374 - Cisco Contact Center Enterprise Agreement (CC EA) Unified Customer Voice Portal (CVP) License Expiration - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70374.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/703/fn70374.html)


Updated:February 21, 2019
Document ID:FN70374
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 21-Feb-19  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Unified Contact Center Enterprise Virtual Machine Templates  | 11  | 11.0, 11.5  |   |  
| NON-IOS  | Unified Contact Center Enterprise Virtual Machine Templates  | 10  | 10.5  |   |  
| NON-IOS  | Cisco Customer Voice Portal Software Releases  | CVP Version 11  | 11.0(1)  |   |  
| NON-IOS  | Cisco Customer Voice Portal Software Releases  | CVP Version 10  | 10.5(1)  |   |  
| NON-IOS  | Cisco Customer Voice Portal Software Releases  | CVP Ver 11  | 11.5(1)  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvo35148](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvo35148)  | Cisco Contact Center Enterprise Agreement (CC EA) CVP License Expiration  |  
### Problem Description
The Contact Center Enterprise Agreement (CC EA) licenses for Cisco Unified Customer Voice Portal (CVP) can expire before the end of a customer's CC EA term.
**Note:** This issue affects only customers who have a CC EA license. Other customers are not affected.
**CVP licenses affected:** Releases 10.5, 11.0, and 11.5
### Background
CVP licenses for CC EAs should be issued without expiration dates. However, some licenses were issued _with_ an expiration date. The issue affects licenses for these CVP releases:
  * **Release 10.5:** License expiration date is December 31, 2018.
  * **Release 11.0:** License expiration date is December 1, 2019.
  * **Release 11.5:** License expiration date is December 1, 2019.


**Note:** Licenses for CVP Release 11.6 or later are _not_ affected.
### Problem Symptom
An expired license on a CVP server triggers a graceful shutdown that causes inbound phone numbers to ring busy. The problem begins on the date that the CVP license expires.
### Workaround/Solution
You can download a new permanent license for your current CVP release from the EA Workspace portal, and then apply the new license to the CVP server.
**Alternative:** Upgrade to CVP Release 11.6 or later.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)
  * [Unified Customer Voice Portal](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70374.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70374.html)
