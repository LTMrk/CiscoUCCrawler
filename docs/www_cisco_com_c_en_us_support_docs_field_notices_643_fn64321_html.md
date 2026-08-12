  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco 4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-field-notices-list.html)


# Field Notice: FN - 64321 - Network Interface Module Functionality Issue with Cisco IOS Releases Earlier than IOS-XE 16.5 - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/643/fn64321.html) to Save Content 
Print
### Available Languages
Updated:July 17, 2017
Document ID:FN64321
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 14-Jul-17  | Initial Release  |  
| 10.0  | 19-Dec-17  | Migration to new field notice system  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| NIM-2FXS/4FXOP  |   |  
| NIM-2FXS/4FXOP=  |   |  
| NIM-2FXSP  |   |  
| NIM-2FXSP=  |   |  
| NIM-4FXSP  |   |  
| NIM-4FXSP=  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf34445](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf34445)  | There were no defects filed with this field notice at the time of publication.  |  
### Problem Description
On select Cisco 4000 Series Integrated Services Routers (ISR 4000s), the Foreign Exchange Station Network Interface Modules (FXS NIMs) NIM-2FXSP, NIM-4FXSP, and NIM-2FXS/4FXOP will not function properly if they run Cisco IOS® Software Releases earlier than Cisco IOS XE 16.5.
### Background
A hardware component that was introduced into the manufacturing process for the FXS NIMs that are compatible with ISR 4000s requires Cisco IOS Software Release IOS XE 16.5 or later in order to operate properly. Affected units are identified by the suffix "**P** " at the end of the Product Identifier (PID).
### Problem Symptom
The new hardware revision will not be recognized with Cisco IOS Software Releases earlier than Cisco IOS XE 16.5. The impacted FXS NIMs that run a Cisco IOS Software Release earlier than Cisco IOS XE 16.5 will exhibit this behavior:
  * The NIM modules boot up, as verified by the **show platform** command.
  * The output of the **show voice port summary** command does not show any analog ports.


Here is an example:
[![](https://www-tac.cisco.com/Support_Library/field_alerts/fn64321_ormvsb.png)](https://www-tac.cisco.com/Support_Library/field_alerts/fn64321_ormvsb.png "Related image, diagram or screenshot.")  

### Workaround/Solution
Use Cisco IOS XE Release 16.5 or later so that the impacted FXS NIMs operate properly. **Note** : The FXS NIMs can be identified as described in the _How to Identify Hardware Levels_ section. Enter the **show version** command in order to identify the Cisco IOS XE version, as highlighted in blue in this example: [![](https://www-tac.cisco.com/Support_Library/field_alerts/fn64321_osvw4v.png)](https://www-tac.cisco.com/Support_Library/field_alerts/fn64321_osvw4v.png "Related image, diagram or screenshot.")  
  

### How To Identify Affected Products
The impacted FXS NIMs have a suffix "**P** " at the end of the PID. The impacted FXS NIM PIDs are:
  * NIM-2FXS**P**
  * NIM-4FXS**P**
  * NIM-2FXS/4FXO**P**


You can enter the **show platform** command in order to verify the PIDs, as shown here:
[![](https://www-tac.cisco.com/Support_Library/field_alerts/fn64321_os7qxd.png)](https://www-tac.cisco.com/Support_Library/field_alerts/fn64321_os7qxd.png "Related image, diagram or screenshot.")  
  

### Additional Information
Here is some additional information about the issue that is described in this FN:
  * The Cisco IOS Software Release Cisco IOS XE 16.5 or later is compatible with both the old and new hardware.
  * Platforms with old and new components are completely interoperable.
  * There is no change in features or any other functionality.
  * Older modules (NIM-2FXS, NIM-4FXS, and NIM-2FXS/4FXO) will continue to work with supported versions of Cisco IOS XE releases, as mentioned in [Cisco 4000 Series Integrated Services Routers - Interfaces and Modules](http://www.cisco.com/c/en/us/products/routers/4000-series-integrated-services-routers-isr/relevant-interfaces-and-modules.html#voice-interface-cards).


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/643/fn64321.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64321.html)
