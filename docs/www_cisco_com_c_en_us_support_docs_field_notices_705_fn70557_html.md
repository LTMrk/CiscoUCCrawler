  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified IP Interactive Voice Response (IVR)](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-ip-interactive-voice-response-ivr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-ip-interactive-voice-response-ivr/products-field-notices-list.html)


# Field Notice: FN - 70557 - Unified Contact Center Express (UCCX) and Customer Collaboration Portal (CCP): QuoVadis Root CA 2 Decommission Might Affect Smart Licensing - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70557.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/705/fn70557.html)


Updated:June 8, 2022
Document ID:FN70557
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.3  | 08-Jun-22  | Updated the Products Affected and Workaround/Solution Sections  |  
| 1.2  | 29-Mar-22  | Updated the Products Affected, Defect Information, Problem Description, Background, Problem Symptom, and Workaround/Solution Sections and Added the Additional Information Section  |  
| 1.1  | 22-Feb-22  | Updated the Problem Description, Background, Problem Symptom, and Workaround/Solution Sections  |  
| 1.0  | 18-Mar-21  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Unified Contact Center Express Software  | Unified CCX 12  | 12.5(1), 12.5(1)SU1, 12.5(1)SU2  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvx00534](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx00534)  | QuoVadis root CA decommission on cra  |  
| [CSCvx00533](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx00533)  | QuoVadis root CA decommission on cra  |  
| [CSCwa92591](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwa92591)  | Smart Licensing "Communication send error" due to certificate update  |  
| [CSCvx00529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx00529)  | QuoVadis root CA decommission on ccp  |  
### Problem Description
For affected versions of the Unified Contact Center Express (UCCX) software and Customer Collaboration Portal (CCP), some Secure Sockets Layer (SSL) certificates issued from the QuoVadis root certificate authority (CA) trust chain before March 31, 2021 cannot be renewed from this CA. Once those certificates expire on devices or are removed from the Cisco cloud servers, functions such as Smart Licensing will fail to establish secure connections to Cisco and might not operate properly.
### Background
The QuoVadis Root CA 2 Public Key Infrastructure (PKI) used by UCCX and CCP software to issue SSL certificates is subject to an industry-wide issue that affects revocation abilities. Due to this issue, no new QuoVadis Root CA 2 certificates will be issued or renewed by Cisco after March 31, 2021. This affects certificate renewals on devices, Cisco cloud servers, and third-party services.
Certificates issued before the QuoVadis Root CA 2 was decommissioned will continue to be valid. However, the certificates will not renew when they expire on either the device or the Cisco cloud server. This will cause functions such as Smart Licensing to fail to establish secure connections to Cisco cloud servers.
This table shows a summary of the QuoVadis Root CA 2 certificate expiration dates for affected Cisco services.  
| Cisco Cloud Server  | QuoVadis Certificate Expiration Date  | Affected Services  |  
| --- | --- | --- |  
| tools.cisco.com  | February 5, 2022  | 
  * Smart Licensing

 |  
| smartreceiver.cisco.com  | January 26, 2023  | 
  * Smart Licensing

 |  
### Problem Symptom
Expiration of the QuoVadis Root CA 2 certificates affects these services with the associated symptoms.  
| Affected Services  | Symptoms for Affected Services  |  
| --- | --- |  
| Smart Licensing  | Failure to connect to the server (Details are provided in this section)  |  
For UCCX and CCP devices, affected devices will be unable to connect to the Smart Licensing services hosted by Cisco. Smart licenses might fail entitlement and reflect an Out of Compliance status.
The features that use Smart Licensing will continue to function for one year after the last successful secure connection. Some Smart Licensing symptoms are:
  * The device might indicate a failure to communicate with the Smart Licensing server within 30 days from the last successful connection.
  * The device will show the "Authorization Expired" state if there is no communication with the Smart Licensing server within 90 days.
  * The device will show the "Unregistered" state if there is no communication with the Smart Licensing server after one year and the licensed features usage become suspended.


**Note:** Offline licensing, such as Permanent License Reservation (PLR) and Specific License Reservation (SLR), is not affected by the certificate change on the Smart Licensing server.
For additional information, refer to the [Cisco Smart Licensing Guide](https://www.cisco.com/c/en/us/buy/licensing/licensing-guide.html).
### Workaround/Solution
Cisco has migrated from the QuoVadis Root CA 2 to the IdenTrust Commercial Root CA 1 for SSL certificates. Cisco recommends to perform a software upgrade to add the new IdenTrust Commercial Root CA 1 certificate to UCCX and CCP.
**Workaround**
**Software Upgrade**
For UCCX-based devices, upgrade UCCX software versions shown in the table in order to resolve the root CA certificate issue for affected platforms.  
| Release Version  | Fixed Version  |  
| --- | --- |  
| UCCX 12.5(X)  | 12.5(1) SU2ES01 or later  |  
For CCP, the changes from CVOS (Cisco bug ID CSCvx00534) have been added to CCP as part of Cisco bug ID CSCvx00529. No action is required on the CCP server.  
| Release Version  | Fixed Version  |  
| --- | --- |  
| CCP 12.5(X)  | CCP 12.5(1) SU1 or later  |  
### Additional Information
Cisco has created a web page to provide customers and partners with additional information on this issue. Consult the [QuoVadis Root CA 2 Decommission page](https://tools.cisco.com/security/center/resources/Q-CA-Root-Change) for a full list of products affected, associated Field Notices, and frequently asked questions.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Express 12.5(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-express-12-5-1/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70557.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70557.html)
