  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligent-contact-management-enterprise/products-field-notices-list.html)


# Field Notice: FN - 72306 - Unified Contact Center Enterprise (UCCE)/Packaged Contact Center Enterprise (PCCE) and Unified Customer Voice Portal (CVP): QuoVadis Root CA 2 Decommission Might Affect Smart Licensing - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72306.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/723/fn72306.html)


Updated:March 29, 2022
Document ID:FN72306
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.1  | 29-Mar-22  | Updated the Products Affected, Defect Information, Problem Description, Background, Problem Symptom, and Workaround/Solution Sections and Added the Additional Information Section  |  
| 1.0  | 22-Feb-22  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Cisco Customer Voice Portal Software Releases  | CVP Ver 12  | 12.5(1), 12.6(1)  | CVP  |  
| NON-IOS  | Cisco Unified Intelligent Contact Management Software Releases  | ICM Ver 12  | 12.5(1), 12.6(1)  | UCCE/PCCE  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwb04917](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb04917)  | ICM: Smart License - Registration & Authorization fails with "Communication send error"  |  
| [CSCwb04933](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb04933)  | CVP: Smart License - Registration & Authorization fails with "Communication send error"  |  
### Problem Description
For affected versions of the Cisco Unified Contact Center Enterprise (UCCE)/Packaged Contact Center Enterprise (PCCE) and Unified Customer Voice Portal (CVP) software, some Secure Sockets Layer (SSL) certificates issued from the QuoVadis root certificate authority (CA) trust chain before March 31, 2021 cannot be renewed from this CA. Once those certificates expire on devices or are removed from the Cisco cloud servers, functions such as Smart Licensing will fail to establish secure connections to Cisco and might not operate properly.
### Background
The QuoVadis Root CA 2 Public Key Infrastructure (PKI) used by UCCE/PCCE and Unified CVP software to issue SSL certificates is subject to an industry-wide issue that affects revocation abilities. Due to this issue, no new QuoVadis Root CA 2 certificates will be issued or renewed by Cisco after March 31, 2021. This affects certificate renewals on devices, Cisco cloud servers, and third-party services.
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
For UCCE/PCCE and Unified CVP devices, affected devices will be unable to connect to the Smart Licensing services hosted by Cisco. Smart licenses might fail entitlement and reflect an Out of Compliance status.
The features that use Smart Licensing will continue to function for one year after the last successful secure connection. Some Smart Licensing symptoms are:
  * The device might indicate a failure to communicate with the Smart Licensing server within 30 days from the last successful connection.
  * The device will show the "Authorization Expired" state if there is no communication with the Smart Licensing server within 90 days.
  * The device will show the "Unregistered" state if there is no communication with the Smart Licensing server after one year and the licensed features usage become suspended.


**Note:** Offline licensing, such as Permanent License Reservation (PLR) and Specific License Reservation (SLR), is not affected by the certificate change on the Smart Licensing server.
For additional information, refer to the [Cisco Smart Licensing Guide](https://www.cisco.com/c/en/us/buy/licensing/licensing-guide.html) and the Administration/Installation and Upgrade Guide for UCCE/PCCE and Unified CVP:
  * [Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/administration/guide/ucce_b_administration-guide-for-cisco-unified_1261/ucce_b_administration-guide-for-cisco-unified_1261_chapter_0100.html)
  * [Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5/ucce_b_administration-guide-for-cisco-unified12_5_chapter_01111.html)
  * [Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/installandupgrade/guide/ccvp_b_1261-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-unified-cvp-licensing.html)
  * [Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/installation/guide/ccvp_b_install_and_upgrade_12-5/ccvp_b_install_and_upgrade_12-5_chapter_01000.html)


For devices managed by UCCE/PCCE and Unified CVP, navigate to `**smart licensing status**`in order to view the licensing status:
  * UCCE/PCCE - Log in to CCEAdmin and choose **Infrastructure Settings > License Management > Smart Licensing Status > License Authorization Status**.
  * Unified CVP - Log in to CVP NOAMP and choose **License Management > Smart Licensing Status > License Authorization Status**.


UCCE/PCCE and Unified CVP will be authorized with this error message:

```
**The last attempt to renew license authorization failed......**

```

The error message is shown in this image:
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/FN723061648582716932.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/FN723061648582716932.png "Related image, diagram or screenshot.")
### Workaround/Solution
Cisco has migrated from the QuoVadis Root CA 2 to the IdenTrust Commercial Root CA 1 for SSL certificates. Cisco recommends to add the new IdenTrust Commercial Root CA 1 certificate to UCCE/PCCE and Unified CVP.
**Software Downloads**
  * [UCCE/PCCE/Unified CVP 12.6.x](https://software.cisco.com/download/home/268439622/type/284420243/release/12.6\(1\))
  * [UCCE/PCCE/Unified CVP 12.5.x](https://software.cisco.com/download/home/268439622/type/284420243/release/12.5\(1\)), choose **"QuoVadis to IdenTrust migration for Smart Agent" can get from QuoVadis_IdenTrust_Migration**


**ICM Logger A Server**
In order to add the new IdenTrust Commercial Root CA 1 certificate, complete these steps:
  1. Make a backup of the folder <_icm_install_drive_ >:\icm\\.sl_truststore\\.
  2. Stop the Cisco Tomcat service.
  3. Remove the "call_home_ca" file present in the path "<_icm_install_drive_ >:\icm\\.sl_truststore\".
  4. Copy the downloaded "call_home_ca" file and place it in the path "<_icm_install_drive_ >:\icm\\.sl_truststore\".
  5. Start the Cisco Tomcat service and wait for five minutes.
  6. Re-attempt to "Renew Authorization" for Smart Licensing.


**Unified CVP Call Server**
In order to add the new IdenTrust Commercial Root CA 1 certificate, complete these steps:
  1. Make a backup of the folder <_cvp_install_drive_ >:\Cisco\CVP\conf\\.sltruststore\\.
  2. Stop the Unified CVP WebServicesManager (WSM) service.
  3. Remove the "call_home_ca" file present in the path "<_cvp_install_drive_ >:\Cisco\CVP\conf\\.sltruststore\".
  4. Copy the downloaded "call_home_ca" file and place it in the path "<_cvp_install_drive_ >:\Cisco\CVP\conf\\.sltruststore\".
  5. Start the Unified CVP WSM service and wait for five minutes.
  6. Re-attempt to "Renew Authorization" for Smart Licensing.


### Additional Information
Cisco has created a web page to provide customers and partners with additional information on this issue. Consult the [QuoVadis Root CA 2 Decommission page](https://tools.cisco.com/security/center/resources/Q-CA-Root-Change) for a full list of products affected, associated Field Notices, and frequently asked questions.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)
  * [Unified Customer Voice Portal](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72306.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72306.html)
