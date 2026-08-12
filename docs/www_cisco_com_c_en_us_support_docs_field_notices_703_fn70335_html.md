  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco 4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-field-notices-list.html)


# Field Notice: FN - 70335 - ISR-WAAS-200 Deployed on an ISR-4321 Router with Cisco IOS XE Release 16.7 or Earlier Might Experience High Memory Utilization - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70335.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/703/fn70335.html)


Updated:December 12, 2018
Document ID:FN70335
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 12-Dec-18  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Wide Area Application Services (WAAS) Software  | 6.2  | 6.2.3c, 6.2.3d, 6.2.3e  | This problem is specific to ISR-4321 with Cisco IOS Software Release 16.x and ISR-WAAS-200 deployed with 4GB RAM.  |  
| NON-IOS  | Wide Area Application Services (WAAS) Software  | 6.4  | 6.4.1, 6.4.1a, 6.4.1b, 6.4.3  | This problem is specific to ISR-4321 with Cisco IOS Software Release 16.x and ISR-WAAS-200 deployed with 4GB RAM.  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf02875](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf02875)  | Reducing the memory utilized by ISR-WAAS-200  |  
### Problem Description
ISR-WAAS-200 software deployed on an ISR-4321 router installed with Cisco IOS® XE Software Release 16.7 or earlier might experience high memory utilization.
This issue is specific to ISR-WAAS-200 software when deployed in the combination listed in this table.  
| Router  | Cisco IOS XE Software Release  | ISR-WAAS-200 Version  | Impact  |  
| --- | --- | --- | --- |  
| ISR-4321  | 16.7 or earlier  | 6.2.3c, 6.2.3d, 6.2.3e, 6.4.1, 6.4.1a, 6.4.1b, 6.4.3  | The router might experience high memory utilization.  |  
### Background
ISR-WAAS software is a specific implementation of Virtual WAAS, which runs Cisco IOS XE software, on a Cisco ISR 4000 Series router.
Due to RAM allocation changes in the ISR-WAAS software, the router might experience high memory utilization.
### Problem Symptom
The ISR-WAAS-200 software, when deployed on an ISR-4321 router as per the combination mentioned in the Problem Description section, might display either or both of these warning messages:
`Router#**show logging**  
   
 PLATFORM-4-ELEMENT_WARNINGSIP0: smand: RP/0: Used Memory value 93% exceeds warning level 88%  
   
 PLATFORM-3-ELEMENT_CRITICAL: SIP0: smand: RP/0: Used Memory value 94% exceeds critical level 93%`
### Workaround/Solution
In order to avoid high memory utilization, Cisco recommends that you upgrade to Cisco IOS XE Software Release 16.8 or later and redeploy ISR-WAAS software with Version 6.4.1c.  
| Router  | Cisco IOS XE Software Release  | ISR-WAAS Version  | Action  |  
| --- | --- | --- | --- |  
| ISR-4321  | 16.8 or later  | 6.4.1c  | Redeploy WAAS with Version 6.4.1c  |  
**Note:** The ISR-WAAS software version can now be downgraded to any of the supported versions (which include impacted versions), after ISR-WAAS Version 6.4.1c is redeployed as suggested in the table. This can still consume less memory.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70335.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70335.html)
