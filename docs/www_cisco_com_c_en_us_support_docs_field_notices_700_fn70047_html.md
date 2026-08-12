  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-field-notices-list.html)


# Field Notice: FN - 70047 - CP-8821 - IP Phone Displays "MIC not installed" Error Message - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/700/fn70047.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/700/fn70047.html)


Updated:November 30, 2017
Document ID:FN70047
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 30-Nov-17  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| NON-IOS  | SIP v.11  | 11.0(3)SR3, 11.0(2)SR2, 11.0(3)SR5, 11.0(3), 11.0(2), 11.0(3)SR2, 11.0(1), 11.0(3)SR1  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCve44412](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve44412)  | Concurrent access to secure storage causes MMC errors  |  
| [CSCvg68954](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvg68954)  | Request to remove "MIC not installed" home screen message logic regardless of LSC status  |  
### Problem Description
The CP-8821 IP Phone displays the "MIC not installed" error message.
### Background
The Manufacturer Installed Certificate (MIC) can be used for wireless authentication (for example, Extensible Authentication Protocol (EAP) - Transport Layer Security (TLS)) as well as other security features/interfaces:
  * Cisco Unified Communications Manager (CUCM) Encrypted/Authenticated device security mode
  * HTTPS
  * Secure Shell (SSH)


The "MIC not installed" error message is displayed on the CP-8821 and is covered in Cisco bug IDs [CSCve44412](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve44412) and [CSCvg68954](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvg68954).
The “MIC not installed” message will only show on the home screen either indefinitely (without a Locally Significant Certificate (LSC)) or for 10 seconds after power on (with LSC) with loads earlier than Release 11.0(3)SR6. However, a message will be logged to Status Messages for all loads.
### Problem Symptom
The "MIC not installed" error message is displayed on the CP-8821 IP Phone.
### Workaround/Solution
In order to troubleshoot the 8821 IP Phone when it displays "MIC not installed", complete these steps.
**Step 1. Confirm the Error Message**
Verify that the phone displays the "MIC not installed" error message on the screen as shown in this image:
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/700/fn70047_1.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/700/fn70047_1.png "Related image, diagram or screenshot.")
If the error has disappeared, choose **Settings > Admin settings > Status > Status messages** in order to verify it is present as a status message.
**Step 2. Restore Functionality**
If not required for wireless authentication, the MIC can be replaced with an LSC with the use of CUCM Certificate Authority Proxy Function (CAPF) so the phone operates normally. [Install an LSC on the phone](http://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200934-Install-an-LSC-on-a-Phone-with-CUCM-Clus.html) once the error message is confirmed and test once more. Ensure **By Null String** or **By Authentication String** is selected for the Authentication Mode in order for the LSC to be installed successfully despite the fact that the MIC is not present.
In Release 11.0(3)SR3.2, the "MIC not installed" message in the status bar is suppressed when the LSC is installed on the phone. The message is displayed for the first 10 seconds after power on. For earlier loads an LSC can be installed on the phone and function, but the “MIC not installed” message continues to be displayed on the phone’s status bar.
**Step 3. Prevent New Occurrences**
Upgrade all Cisco 8821 phones to Release 11.0(3)SR3.2 or later as soon as possible, as the issue has been fixed from this version onwards. For devices that have already displayed this error message, an upgrade will not recover the MIC. The code that contains the fix for Cisco bug ID [CSCvc65418](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc65418/?reffering_site=dumpcr) (resolved through the fix of Cisco bug ID [CSCve44412](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve44412/?reffering_site=dumpcr)) prevents disappearance of the MIC in the first place.
For further assistance or if the MIC is required for wireless authentication on an affected phone, contact the [Cisco Technical Assistance Center](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) for a Return Material Authorization (RMA).
**Note** : Cisco recommends that you use the latest 8821 firmware release available on Cisco.com.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/700/fn70047.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70047.html)
