  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 6800 Series with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/products-field-notices-list.html)


# Field Notice: FN - 72302 - Cisco IP Phones Might Fail to Operate Correctly Due to a New Manufacturer Installed Certificate - Configuration Change Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72302.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/723/fn72302.html)


Updated:June 7, 2023
Document ID:FN72302
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.3  | 07-Jun-23  | Updated the Products Affected Section  |  
| 1.2  | 23-Dec-22  | Updated the Workaround/Solution Section  |  
| 1.1  | 19-Jul-22  | Updated the Products Affected, Problem Description, Problem Symptom, and Workaround/Solution Sections  |  
| 1.0  | 07-Apr-22  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CP-6851-3PCC-K9=  |   |  
| CP-6841-3PCC-K9=  |   |  
| CP-6821-3PCC-K9=  |   |  
| CP-7861-3PCC-K9=  |   |  
| CP-7841-3PCC-K9=  |   |  
| CP-7821-3PCC-K9=  |   |  
| CP-7811-3PCC-K9=  |   |  
| CP-7832-3PCC-K9=  |   |  
| CP-6871-3PCC-K9=  |   |  
| CP-6861-3PW-K9  |   |  
| CP-8811-3PCC-K9=  |   |  
| CP-8811-3PCC-K9++=  |   |  
| CP-8811-3PC-RC-K9=  |   |  
| CP-8851-3PCC-K9=  |   |  
| CP-8861-3PCC-K9=  |   |  
| CP-8841-3PCC-K9=  |   |  
| CP-8865-3PCC-K9=  |   |  
| CP-8845-3PCC-K9=  |   |  
| CP-8832-3PCC-K9=  |   |  
| ATA192-3PW-K9  |   |  
| ATA191-3PW-K9  |   |  
| CP-7811-K9=  | Manufacturing Date: 3/2022 and later  |  
| CP-7821-K9=  | Manufacturing Date: 4/2022 and later  |  
| CP-7841-K9=  | Manufacturing Date: 2/2022 and later  |  
| CP-7861-K9=  | Manufacturing Date: 3/2022 and later  |  
| CP-8811-A-K9=  | Manufacturing Date: 4/2022 and later  |  
| CP-8811-K9++=  | Manufacturing Date: 5/2022 and later  |  
| CP-8811-K9=  | Manufacturing Date: 2/2022 and later  |  
| CP-8811-W-K9=  | Manufacturing Date: 3/2022 and later  |  
| CP-8811-NC-K9=  | Manufacturing Date: 5/2022 and later  |  
| CP-8841-K9++=  | Manufacturing Date: 5/2022 and later  |  
| CP-8841-K9=  | Manufacturing Date: 5/2021 and later  |  
| CP-8841-W-K9=  | Manufacturing Date: 2/2022 and later  |  
| CP-8841-NC-K9=  | Manufacturing Date: 5/2022 and later  |  
| CP-8851-A-K9=  | Manufacturing Date: 1/2022 and later  |  
| CP-8851-K9++=  | Manufacturing Date: 4/2022 and later  |  
| CP-8851-K9=  | Manufacturing Date: 5/2021 and later  |  
| CP-8851-W-K9=  | Manufacturing Date: 2/2022 and later  |  
| CP-8851-NC-K9=  | Manufacturing Date: 4/2022 and later  |  
| CP-8851NR-K9++=  | Manufacturing Date: 4/2022 and later  |  
| CP-8851NR-K9=  | Manufacturing Date: 2/2022 and later  |  
| CP-8861-A-K9=  | Manufacturing Date: 1/2022 and later  |  
| CP-8861-K9++=  | Manufacturing Date: 3/2022 and later  |  
| CP-8861-K9=  | Manufacturing Date: 5/2021 and later  |  
| CP-8861-NC-K9=  | Manufacturing Date: 3/2022 and later  |  
| CP-8861-W-K9=  | Manufacturing Date: 1/2022 and later  |  
| CP-8811-K9++=  | Manufacturing Date: 5/2022 and later  |  
| CP-8811-NC-K9=  | Manufacturing Date: 5/2022 and later  |  
| CP-7832-K9=  | Manufacturing Date: 11/22/2022  |  
| CP-7832-W-K9=  | Manufacturing Date: 11/22/2022  |  
| CP-7832-K9++=  | Manufacturing Date: 2/10/2023  |  
| CP-8832-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-W-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-W-K9=  | Manufacturing Date: 8/3/2022  |  
| CP-8832-NR-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-NR-K9=  | Manufacturing Date: 8/3/2022  |  
| CP-8832-K9++  | Manufacturing Date: 2/1/2023  |  
| CP-8832-K9++=  | Manufacturing Date: 2/1/2023  |  
| CP-8832-NR-K9++  | Manufacturing Date: 2/1/2023  |  
| CP-8832-NR-K9++=  | Manufacturing Date: 2/1/2023  |  
| CP-8832-EU-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-EU-K9=  | Manufacturing Date: 8/3/2022  |  
| CP-8832-EU-W-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-EU-W-K9=  | Manufacturing Date: 8/3/2022  |  
| CP-8832-J-W-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-J-W-K9=  | Manufacturing Date: 8/3/2022  |  
| CP-8832-LA-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-LA-K9=  | Manufacturing Date: 8/3/2022  |  
| CP-8832-LA-W-K9  | Manufacturing Date: 8/3/2022  |  
| CP-8832-LA-W-K9=  | Manufacturing Date: 8/3/2022  |  
| CP-8845-K9=  | Manufacturing Date: 10/20/2022  |  
| CP-8845-W-K9=  | Manufacturing Date: 10/26/2022  |  
| CP-8845-K9++=  | Manufacturing Date: 1/27/2023  |  
| CP-8845-A-K9=  | Manufacturing Date: 11/9/2022  |  
| CP-8845-NC-K9=  | Manufacturing Date: 1/27/2023  |  
| CP-8865-K9=  | Manufacturing Date: 10/20/2022  |  
| CP-8865-W-K9=  | Manufacturing Date: 10/26/2022  |  
| CP-8865-K9++=  | Manufacturing Date: 1/27/2023  |  
| CP-8865NR-K9=  | Manufacturing Date: 10/20/2022  |  
| CP-8865NR-K9++=  | Manufacturing Date: 1/27/2023  |  
| CP-8865-A-K9=  | Manufacturing Date: 11/9/2022  |  
| CP-8865-NC-K9=  | Manufacturing Date: 1/27/2023  |  
| ATA191-K9  | Manufacturing Date: 11/4/2022  |  
| CP-8875-L-K9=  | Manufacturing Date: from shipping  |  
| CP-8875-K9=  | Manufacturing Date: from shipping  |  
| CP-8875NR-K9=  | Manufacturing Date: from shipping  |  
| CP-8875NR-K9++=  | Manufacturing Date: from shipping  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwb15715](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb15715)  | MPP/Enterprise Phones and ATA: Shipping with MIC certificate issued by new Cisco Manufacturing CA  |  
### Problem Description
Multiplatform Phones (MPPs), Analog Telephone Adapters (ATAs), and Enterprise Phones will fail to operate if a new Certificate Authority (CA) is not added in the server trust list. Newly manufactured MPPs, ATAs, and Enterprise Phones will ship with a Cisco Manufacturing CA III or Cisco Manufacturing HA SUDI CA issued device certificate. If the new CA is not added in the server trust list, secure network deployment will fail to operate.
### Background
If the new CA is not added in the server trust list, secure network deployment will fail to operate. An administrator must install the new CA in order to ensure secure device communication and operation.
This field notice lists the base Product IDs (PIDs), but pertains to all PIDs of the same model. See the Products Affected section for further details.
### Problem Symptom
Secure network deployment will fail to operate on affected MPP and Enterprise devices.
### Workaround/Solution
An administrator must install the new CA information in order to ensure secure device communication and operation.
For the affected MPP, ATA, and Enterprise Phone, service providers and administrators need to add the necessary files, based on the device type, to the trusted root certificate bundle they use to validate the phones' device certificate against.
**MPP and ATA**
The certificate (CER) and Privacy Enhanced Mail (PEM) file links are included here:
  * [Cisco Manufacturing CA III (cmca3) - CER](http://www.cisco.com/security/pki/certs/cmca3.cer) / [Cisco Manufacturing CA III (cmca3) - PEM](http://www.cisco.com/security/pki/certs/cmca3.pem)
  * [Cisco Basic Assurance Root CA 2099 (cbarc2099) - CER](http://www.cisco.com/security/pki/certs/cbarc2099.cer) / [Cisco Basic Assurance Root CA 2099 (cbarc2099) - PEM](http://www.cisco.com/security/pki/certs/cbarc2099.pem)
  * [Cisco Manufacturing HA SUDI CA - CER](https://www.cisco.com/security/pki/certs/hasudi.cer) / [Cisco Manufacturing HA SUDI CA - PEM](https://www.cisco.com/security/pki/certs/hasudi.pem)
  * [Cisco Root CA 2099 (crca2099) - CER](https://www.cisco.com/security/pki/certs/crca2099.cer) / [Cisco Root CA 2099 (crca2099) - PEM](https://www.cisco.com/security/pki/certs/crca2099.pem)


**Enterprise Phone**
The CER and PEM file links are included here:
  * [Cisco Manufacturing CA III (cmca3) - CER](http://www.cisco.com/security/pki/certs/cmca3.cer) / [Cisco Manufacturing CA III (cmca3) - PEM](http://www.cisco.com/security/pki/certs/cmca3.pem)
  * [Cisco Basic Assurance Root CA 2099 (cbarc2099) - CER](http://www.cisco.com/security/pki/certs/cbarc2099.cer) / [Cisco Basic Assurance Root CA 2099 (cbarc2099) - PEM](http://www.cisco.com/security/pki/certs/cbarc2099.pem)


For the Cisco Unified Communictions Manager (UCM) version equal to or later than 11.5 SU9, 12.5 SU4, and 14, the new CA is natively installed, therefore it will not be affected. For the process of CA installation on Cisco UCM and Identity Services Engine (ISE), refer to:
  * [Administration Guide for Cisco Unified Communications Manager, Release 12.5(1) - Upload the Certificate or Certificate Chain](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/admin/cucm_b_administration-guide-1251/cucm_b_administration-guide-1251_chapter_01111.html#CUCM_TK_UACB16F8_00)
  * [Import and Export Certificates in ISE - Import the Certificate in ISE](https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine/215927-how-to-import-and-export-certificate-fro.html#anc3)


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html)
