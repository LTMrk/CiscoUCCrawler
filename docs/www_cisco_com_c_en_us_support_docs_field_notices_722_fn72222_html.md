  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 7800 Series with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/products-field-notices-list.html)


# Field Notice: FN - 72222 - End of CDA/EDOS Support for Earlier Firmware - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72222.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/722/fn72222.html)


Updated:June 9, 2022
Document ID:FN72222
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.2  | 09-Jun-22  | Updated the Workaround/Solution Section  |  
| 1.1  | 27-Apr-22  | Updated the Problem Description, Background, Problem Symptom, and Workaround/Solution Sections  |  
| 1.0  | 07-Mar-22  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| ATA191-3PW-K9   |   |  
| ATA192-3PW-K9   |   |  
| CP-6851-3PCC-K9=   |   |  
| CP-7811-3PCC-K9=   |   |  
| CP-7821-3PCC-K9=   |   |  
| CP-7832-3PCC-K9=   |   |  
| CP-7841-3PCC-K9=   |   |  
| CP-7861-3PCC-K9=   |   |  
| CP-8811-3PCC-K9=   |   |  
| CP-8841-3PCC-K9=   |   |  
| CP-8845-3PCC-K9=   |   |  
| CP-8851-3PCC-K9=   |   |  
| CP-8861-3PCC-K9=   |   |  
| CP-8865-3PCC-K9=   |   |  
| SPA122-RC   |   |  
| SPA112-RC   |   |  
| CP-6841-3PCC-K9=   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwa56866](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwa56866)  | End of support for redirection service (CDA / EDOS) on old firmware that use webapps.cisco.com  |  
### Problem Description
Cisco announced the end of support for the redirection service (Customer Device Activation (CDA) / Enablement Data Orchestration System (EDOS)) on earlier firmware that uses the webapps.cisco.com sever, effective December 1, 2022. The phones and Analog Telephone Adapters (ATAs) that are currently sold with the latest firmware version are NOT impacted. The phones and ATAs already deployed in the field that run earlier firmware versions are also not impacted, except for the redirection function. Certain Cisco phones, Multiplatform Phones (MPPs), ATA191/192, and Cisco SPA112/122 ATAs still in the box with the earlier firmware are impacted.
This will take effect immediately on Cisco SPA112/122 and December 1, 2022 for other affected devices. This field notice details the devices and firmware impacted, as well as workarounds.
### Background
The products affected are listed in this table.  
| Product Name  | Firmware Version  |  
| --- | --- |  
| SPA112/122  | Earlier than 1.4.1 SR3  |  
|  MPP 6841/6851 7832/7811/7821/7841/7861 8811/8841/8851/8861 8845/8865  |  11.1.1 and earlier 11.1.1 MSR1-1 11.1.2  |  
|  ATA191/192  |  Earlier than 11.1.0 MSR2  |  
This field notice lists the base Product IDs (PIDs), but pertains to all PIDs of the same model. See the Products Affected section for further details.
### Problem Symptom
Affected platforms with earlier firmware versions will no longer be able to use the redirection service (CDA / EDOS).
After December 1, 2022, cloud provisioning via legacy CDA services on webapps.cisco.com will not work.
### Workaround/Solution
**Prior to December 1, 2022**
The SPA112-RC and SPA122-RC will require an upgrade to the latest firmware prior to installation.
While MPPs and ATA191/ATA192 endpoints can be deployed with earlier firmware, it is recommended to upgrade to the latest firmware version. Then, at the time of installation, perform a factory reset on the device in order to retrigger EDOS activation.
The suggested firmware versions, listed by product, are in this table.  
| Product Name  | Firmware Version  |  
| --- | --- |  
| SPA112-RC/SPA122-RC  | 1.4.1 SR5  |  
| MPP  | 11.3.6 and later  |  
| ATA19x  | 11.2.1 and later  |  
**December 1, 2022 and Later**
The SPA112-RC and SPA122-RC endpoints can be configured manually.
For the MPPs and ATA191/192 MPP endpoints, there are two options:
  * Configure the endpoints manually.
  * Upgrade to the latest firmware available and factory reset the device during installation in order to retrigger EDOS activation.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72222.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72222.html)
