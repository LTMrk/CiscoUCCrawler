  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 7800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-field-notices-list.html)


# Field Notice: FN - 70546 - Webex Calling (formerly Spark Call) Does Not Work With HW V15 or Later 8811/8841/8851/8861 and HW V20 or Later 7821/7841/7861 IP Phones - Replace on Failure
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70546.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/705/fn70546.html)


Updated:August 18, 2023
Document ID:FN70546
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 2.1  | 17-Aug-23  | Updated Problem Description and Workaround/Solution Section  |  
| 2.0  | 31-Aug-21  | Changed the Title from Workaround Provided to Product Migration Required and Added the 78XX Phones as Products Affected  |  
| 1.2  | 30-Jul-20  | Remove TAA SKUS from Phone Chart in Workaround / Solution Section  |  
| 1.1  | 22-Jul-20  | Updated the Workaround/Solution Section  |  
| 1.0  | 27-Apr-20  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CP-8851-K9=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-8861-K9=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-8841-K9=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-8811-K9=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-8811-K9++=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-8841-K9++=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-8851-K9++=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-8861-K9++=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-7821-K9=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-7841-K9=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-7861-K9=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-7861-K9++=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-7821-K9++=  | MPP Replacement (Order by 2021-09-15)  |  
| CP-7841-K9++=  | MPP Replacement (Order by 2021-09-15)  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvs58194](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvs58194)  | 88x1 phones HW V15 and later do not work with Webex Calling (Spark Calling)  |  
### Problem Description
Customers should no longer order voice-only enterprise phone SKUs for use with Webex Calling (formerly Spark Call) as this product does not work with HW V15 or later 8811/8841/8851/8861 and HW V20 or later 7821/7841/7861 Cisco IP Phones. Customers are encouraged to migrate to other Webex Calling services as advised in the End-of-Life Announcement [EOL13394](https://www.cisco.com/c/en/us/products/collateral/conferencing/webex-meeting-center/eos-eol-notice-c51-744405.html). 
### Background
Cisco is now shipping later hardware versions for these IP Phones with the minimum required IP telephony firmware version as specified.
  * Cisco 8811/8841/8851/8861 IP Phones with HW V15 or later require minimum 12.6 firmware version installed.
  * Cisco 7821/7841/7861 IP Phones with HW V20 or later require minimum 14.0 firmware version installed. The Cisco 7811 IP Phone hardware version remains the same and is not impacted.


Webex Calling (formerly Spark Call) only supports IP telephony firmware versions up to 12.0.
When Webex Calling (formerly Spark Call) customers attempt to provision a Cisco IP Phone with a hardware version higher than 12.0, the phone cannot be downgraded which prevents it from running the supported Webex Calling firmware load.
See the [Cisco IP Phone 8800 Series Compatibility Matrix](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/compatibility/p881_b_phone-8800-series-compatibility.html) for more information on Cisco IP Phone 8800 Series compatibility requirements.
### Problem Symptom
The problem symptoms are:
  * A Cisco IP Phone with a later hardware version, specified in the Background section, will not load the IP telephony firmware version required for Webex Calling (formerly Spark Call).
  * A Cisco IP Phone with a later hardware version, specified in the Background section, remains on the preinstalled Enterprise IP telephony firmware version.


### Workaround/Solution
We recommend a replacement for this issue as no workaround is available.
Customers who confirm they are affected using the "How to Identify Affected Products" section, and who have a valid service contract, should use the normal Return Material Authorization (RMA) process to request a replacement.
### How To Identify Affected Products
In order to confirm that the Cisco IP Phone received is an affected later hardware version, verify that the packaging contains a label with this text, "SW must be 12.6 or later" (for 8811/8841/8851/8861) or “SW must be 14.0 or later” (for 7821/7841/7861). See Image 1.
  1. If you have already unboxed the phone and opened the packaging, look for one of these labels on the back of the phone. See Image 2. 
    1. A label with this text, "SW must be 12.6 or later" (for 8811/8841/8851/8861) or “SW must be 14.0 or later” (for 7821/7841/7861).
    2. A barcode that contains the PID VID label. For example, “PID VID: CP-88X1-K9 V15” or “PID VID CP-7841-K9= V20”.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70546img8.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70546img8.jpg "Related image, diagram or screenshot.")


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70546.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70546.html)
