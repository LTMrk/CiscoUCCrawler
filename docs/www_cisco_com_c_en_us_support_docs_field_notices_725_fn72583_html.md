  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/products-field-notices-list.html)


# Field Notice: FN - 72583 - Unable to Downgrade Cisco Multiplatform IP Conference Phone 8832 to Pre-12.0.2 Version - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72583.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72583.html)


Updated:May 30, 2023
Document ID:FN72583
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 23-May-23  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CP-8832-3PCC-K9  | HW V08  |  
| CP-8832-3PC-EU-K9  | HW V08  |  
| CP-8832-3PC-J-K9  | HW V08  |  
| CP-8832-3PC-LA-K9  | HW V08  |  
| CP-8832-3PC-NR-K9  | HW V08  |  
| CP-8832-K9  | HW V08 Mfg Date 2-17-2023 and later.  |  
| CP-8832-NR-K9  | HW V08 Mfg Date: 11-29-2022 and later or Mfg Date: 2-15-2023 and later.  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwe94938](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwe94938)  | Unable to Downgrade 8832 to Pre-12.0.2 Version  |  
### Problem Description
Downgrading a Cisco IP Conference Phone 8832 Multiplatform Phone (MPP) to a release earlier than firmware version 12.0.2 results in a failure.
### Background
Later versions of the Cisco IP Conference Phone 8832 MPP have internal hardware changes. These changes require a minimum firmware version of 12.0.2.
### Problem Symptom
The user or administrator will not be able to downgrade a Cisco IP Conference Phone 8832 MPP to a release earlier than version 12.0.2.
A message similar to this entry might be present in the logs:

```
ERR (14128:14128) img-pfs-HWCOMPAT compatibility check fails for upgrade for CP-8832
```

### Workaround/Solution
If the hardware matches the model and hardware version listed in the "How to Identify Affected Products" section, keep the firmware at MPP firmware version 12.0.2 or later.
### How To Identify Affected Products
These models are known to have updated hardware:
  * CP-8832-3PCC-K9
  * CP-8832-3PC-EU-K9
  * CP-8832-3PC-J-K9
  * CP-8832-3PC-LA-K9
  * CP-8832-3PC-NR-K9
  * CP-8832-K9 phones manufactured on or after February 17, 2023
  * CP-8832-NR-K9 phones with: 
    * Serial numbers that start with FCH* and manufactured on or after November 29, 2022
    * Serial numbers that start with FVH* and manufactured on or after February 15, 2023


The updated MPP 8832 devices affected by this notice will have hardware Version ID (VID) of 8 (VID=V08) or later. The VID is located after the Product ID (PID) on the label located at the bottom of the phone. For example, "PID VID: CP-8832-3PCC-K9 V08" will be affected.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72583.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72583.html)
