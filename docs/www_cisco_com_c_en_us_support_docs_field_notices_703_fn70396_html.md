  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Enterprise Chat and Email](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-field-notices-list.html)


# Field Notice: FN - 70396 - Java Applet Certificate Expiry - Cisco Enterprise Chat and Email (ECE) - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70396.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/703/fn70396.html)


Updated:February 4, 2020
Document ID:FN70396
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 29-Mar-19  | Initial Release  |  
| 1.1  | 04-Feb-20  | Updated the Workaround/Solution Section  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Enterprise Chat and Email  | 12  | 12.0(1)  |   |  
| NON-IOS  | Enterprise Chat and Email  | 11  | 11.5(1), 11.6(1)  | Version 11.5(1) customers are advised to upgrade to Version 11.6(1) and the latest ES7  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvo88067](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvo88067)  | JAVA Certificate Expiry  |  
### Problem Description
All versions of the Enterprise Chat and Email (ECE) applications use Java Runtime Environment (JRE) to perform specific functions within the application user interface. This field notice provides information to Cisco customers about the Java applet security certificate expiration planned for 2019-04-01.
### Background
The certificate used to sign the Java applet used by the application will expire soon. Cisco wants to inform its customers about the Java applet security certificate expiration planned for 2019-04-01.
### Problem Symptom
The workflow diagram editor Java applet will not load on ECE Versions 11.5(1), 11.6(1), and 12.0(1).
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/703/fn70396img11553694969340.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/703/fn70396img11553694969340.png "Related image, diagram or screenshot.")
### Workaround/Solution
Complete these steps:
  1. Download the update for your ECE version from the Software Download page: 
     * [ECE 11.6 ES7](https://software.cisco.com/download/home/286311237/type/286310764/release/11.6\(1\)_ES7) or later
     * [ECE 12.0 ES1](https://software.cisco.com/download/home/286311237/type/286310764/release/12.0\(1\)_ES1) or later
  2. In order to apply the fix, complete the instructions in the ReadMe file.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Enterprise Chat and Email](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html)
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70396.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70396.html)
