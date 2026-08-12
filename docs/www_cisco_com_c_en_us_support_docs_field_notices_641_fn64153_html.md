  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Video](https://www.cisco.com/c/en/us/support/video/category.html)
  * [Cisco cBR Series Converged Broadband Routers](https://www.cisco.com/c/en/us/support/video/cbr-series-converged-broadband-routers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/video/cbr-series-converged-broadband-routers/products-field-notices-list.html)


# Field Notice: FN - 64153 - ASR1000 - Inaccurate Power Supply Unit Status - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/641/fn64153.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/641/fn64153.html)


Updated:May 27, 2020
Document ID:FN64153
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 07-Jul-16  | Initial Release  |  
| 10.0  | 16-Oct-17  | Migration to new field notice system  |  
| 11  | 13-Nov-17  | Content in FN is incorrect and needs to be updated  |  
| 12  | 27-May-20  | Updated the Products Affected Section  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | IOSXE  | 3  | 3.10.7S, 3.16.1aS, 3.16.2bS, 3.16.2S, 3.17.0S, 3.17.1S  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCux37457](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCux37457)  | Power supply status stuck on either "ps, fail" or "ok"  |  
### Problem Description
The Power Supply Unit (PSU) failure events might not be accurately captured in the **show platform** command after boot up.
### Background
After system bootup, the PSU status can be viewed with the **show platform** command.
On all ASR1000 chassis that use Cisco IOS-XE images 3.10.7, 3.16.1a, 3.16.2, 3.16.2b, 3.17.0, and 3.17.1, the PSU status might be inaccurately displayed in these scenarios:
  * Scenario 1 - After bootup the PSU is connected and functions properly, but the **show platform** command might display as 'ps,fail'.
  * Scenario 2 - If the PSU fails or if the power cable is unplugged from the PSU, the **show platform** command might display as 'ok'.


### Problem Symptom
After bootup, the **show platform** command might incorrectly display 'ps,fail' or 'ok' with Cisco IOS-XE images 3.10.7, 3.16.1a, 3.16.2, 3.16.2b, 3.17.0 and 3.17.1
### Workaround/Solution
It is not required to create a Return Material Authorization (RMA) for the PSU. In order to fix this issue, upgrade to either of these images:
  * Cisco IOS-XE 3.16.3
  * Cisco IOS-XE 3.17.2


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4321 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4321-integrated-services-router/model.html)
  * [4331 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4331-integrated-services-router-isr/model.html)
  * [4351 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4351-integrated-services-router/model.html)
  * [4431 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4441-x-integrated-services-router-isr/model.html)
  * [4451-X Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4451-x-integrated-services-router-isr/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/641/fn64153.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64153.html)
