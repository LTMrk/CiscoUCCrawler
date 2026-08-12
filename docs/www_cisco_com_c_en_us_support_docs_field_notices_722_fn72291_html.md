  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unity Connection](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-field-notices-list.html)


# Field Notice: FN - 72291 - Cisco Unity Connection: QuoVadis Root CA 2 Decommission Might Affect Smart Licensing Functionality - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72291.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/722/fn72291.html)


Updated:August 18, 2022
Document ID:FN72291
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 3.0  | 18-Aug-22  | Updated the Workaround/Solution section and added the Additional Information section  |  
| 2.1  | 24-Feb-22  | Updated the Problem Description, Background, Problem Symptom, and Workaround/Solution Sections  |  
| 2.0  | 03-Feb-22  | Updated the Problem Symptom Section  |  
| 1.0  | 07-Jan-22  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Unity Connection Updates  | 12.0  | 12.0(1)SU1, 12.0(1)SU2, 12.0(1)SU3, 12.0(1)SU4, 12.0(1)SU5  | Includes 12.0(1)  |  
| NON-IOS  | Unity Connection Updates  | 12.5  | 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4  |   |  
| NON-IOS  | Unity Connection Updates  | 14  | 14  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvx40739](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx40739)  | QuoVadis root CA decommission on Cisco Unity Connection  |  
### Problem Description
For affected versions of the Cisco Unity Connection (CUC) software, some Secure Sockets Layer (SSL) certificates issued from the QuoVadis root certificate authority (CA) trust chain before March 31, 2021, cannot be renewed from this CA. Once those certificates expire on devices or are removed from the Cisco cloud servers, functions such as Smart Licensing will fail to establish secure connections to Cisco and might not operate properly.
### Background
The QuoVadis Root CA 2 Public Key Infrastructure (PKI) used by CUC software to issue SSL certificates is subject to an industry-wide issue that affects revocation abilities. Due to this issue, no new QuoVadis Root CA 2 certificates will be issued or renewed by Cisco after March 31, 2021. This affects certificate renewals on devices, Cisco cloud servers, and third-party services.
Certificates issued before the QuoVadis Root CA 2 was decommissioned will continue to be valid. However, the certificates will not renew when they expire on either the device or the Cisco cloud server. This will cause functions such as Smart Licensing to fail to establish secure connections to Cisco cloud servers.
This table shows a summary of the QuoVadis Root CA 2 certificate expiration dates for affected Cisco services.  
| Cisco Cloud Server  | QuoVadis Certificate Expiration Date  | Affected Services  |  
| --- | --- | --- |  
| tools.cisco.com  | February 5, 2022  |  Smart Licensing  |  
| smartreceiver.cisco.com  | January 26, 2023  | Smart Licensing  |  
### Problem Symptom
Expiration of the QuoVadis Root CA 2 certificates affects these services with the associated symptoms.  
| Affected Services  | Symptoms for Affected Services  |  
| --- | --- |  
| Smart Licensing  | Failure to connect to the server (Details are provided in this section)  |  
For CUC, affected versions will be unable to connect to the Smart Licensing services hosted by Cisco. Smart licenses might fail entitlement and reflect an Out of Compliance status.
The features that use Smart Licensing will continue to function for 90 days after the last successful secure connection. Some Smart Licensing symptoms are:
  * The CUC server will indicate the last attempt to renew license authorization has failed to communicate with the Smart Licensing server. 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img1.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img2.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img2.jpg "Related image, diagram or screenshot.")
  * The CUC server will show the "Authorization Expired" state if there is no communication with the Smart Licensing server within 90 days. 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img3.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img3.jpg "Related image, diagram or screenshot.")
  * The CUC server will then show the "Out of Compliance" state if there is no communication with the Smart Licensing server and administrators will be unable to provision users until the certification is renewed with IdenTrust. 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img4.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img4.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img5.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/722/fn72291img5.jpg "Related image, diagram or screenshot.")


**Note:** Offline licensing, such as Permanent License Reservation (PLR) and Specific License Reservation (SLR), is not affected by the certificate change on the Smart Licensing server.
For additional information, refer to the [Cisco Smart Licensing Guide](https://www.cisco.com/c/en/us/buy/licensing/licensing-guide.html) and the Managing Licenses chapter of the Install, Upgrade, and Maintenance Guide for your specific version of CUC software.
### Workaround/Solution
Cisco has migrated from the QuoVadis Root CA 2 to the IdenTrust Commercial Root CA 1 for SSL certificates. Cisco recommends these two options to add the new IdenTrust Commercial Root CA 1 certificate to the CUC.
  * Software Upgrade
  * Manual Certificate Update


**Software Upgrade**
For CUC-based devices, upgrade to one of the CUC software versions shown in the table in order to resolve the root CA certificate issue for affected platforms.  
| Release Version  | Fixed Version  |  
| --- | --- |  
|  CUC 12.0(1) 12.0(1)SU1, 12.0(1)SU2, 12.0(1)SU3, 12.0(1)SU4, 12.0(1)SU5 CUC 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4  | CUC 12.5.1 SU5 or later  |  
| CUC 14.0  | CUC 14 SU1 or later  |  
If the CUC version is 12.5.1 SU5 or 14 SU1 or later, no action is needed as the new certificate is provided natively.
**Manual Certificate Update**
For all other CUC 12.0, 12.5, and 14 versions, Cisco recommends to install the COP file on the CUC Publisher to add the new IdenTrust Commercial Root CA 1 certificate to CUC.
  1. Follow the directions in the [Cisco Unity Connection COP File for SLM CDETS CSCvx40739](https://www.cisco.com/web/software/286319537/139787/ciscocm.cuc.slm_quovadis_rootCA_decommission_v1.1.k4.cop-Readme.pdf) document.
  2. Download the [COP file v1.1.k4](https://software.cisco.com/download/home/286313379/type/286319537/release/COP-Files). 
     * The COP file version has changed from v1.0.k4 to v 1.1.k4 due to the Cisco bug ID [CSCwb50904](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb50904). If you installed ciscocm.slm_quovadis_rootCA_decommission_v1.0.k4.cop.sha512 and you are still not able to get Smart License Manager to connect, it is recommended to install the latest version of the COP file (ciscocm.slm_quovadis_rootCA_decommission_v1.1.k4.cop.sha512). See the v1.1 COP file readme for additional information.
     * If you installed ciscocm.slm_quovadis_rootCA_decommission_v1.0.k4.cop.sha512 and everything works as expected, no further action is required.


**Note** : Existing certificates issued from the HydrantID SSL ICA G3 do not need replacement. They are normal certificates issued from the current SSL certificate service and can be used until expiration.
### Additional Information
Cisco has created a web page to provide customers and partners with additional information on this issue. Consult the [QuoVadis Root CA 2 Decommission page](https://tools.cisco.com/security/center/resources/Q-CA-Root-Change) for a full list of products affected, associated Field Notices, and frequently asked questions.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unity Connection Version 12.x](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-12-x/model.html)
  * [Unity Connection Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-14/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72291.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72291.html)
