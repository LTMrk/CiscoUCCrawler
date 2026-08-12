  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-field-notices-list.html)


# Field Notice: FN - 72366 - CP-8831: QuoVadis Root CA 2 Decommission Might Cause SIP and HTTPS Handshakes to Fail - Product Migration Required
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72366.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/723/fn72366.html)


Updated:March 1, 2022
Document ID:FN72366
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 01-Mar-22  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CP-8831-3PCC-K9=   |   |  
| CP-8831-BASE-3PCC   |   |  
| CP-8831-BASE-3PCCR   |   |  
| CP-8831-3PCC-R-K9=   |   |  
| CP-8831-3PB-S-JP=   | Part Alternate   |  
| CP-8831-3PB-S-LA   |   |  
| CP-8831-3P-LA-K9=   |   |  
| CP-8831-3PB-S-BR=   | Part Alternate   |  
| CP-8831-3PD-EU-K9=   |   |  
| CP-8831-3PB-S-TW   |   |  
| CP-8831-3PB-S-EU=   |   |  
| CP-8831-3P-J-K9=   |   |  
| CP-8831-3PB-S-TW=   |   |  
| CP-8831-3PD-TW-K9=   |   |  
| CP-8831-3P-TW-K9=   |   |  
| CP-8831-3PB-S-EU   |   |  
| CP-8831-3PB-S-LA=   | Part Alternate   |  
| CP-8831-3PB-S-JP   |   |  
| CP-8831-3PD-J-K9=   |   |  
| CP-8831-3PD-K9=   |   |  
| CP-8831-3PB-S-BR   |   |  
| CP-8831-3PB-S-JP=   |   |  
| CP-8831-3P-BR-K9=   | Part Alternate   |  
| CP-8831-3PD-LA-K9=   |   |  
| CP-8831-3P-EU-K9=   |   |  
| CP-8831-BASE-3PCC=   |   |  
| CP-8831-3PD-BR-K9=   |   |  
| CP-8831-3PB-S-JP   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvx00523](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx00523)  | QuoVadis root CA decommission on 3pcc-beignet  |  
### Problem Description
For affected versions of the CP-8831 series phone, some Secure Sockets Layer (SSL) certificates issued from the QuoVadis root certificate authority (CA) trust chain before March 31, 2021 cannot be renewed from this CA. Once those certificates expire on devices or are removed from the Cisco cloud servers, functions such as Session Initiation Protocol (SIP) and HTTPS connections will fail to establish.
### Background
The QuoVadis Root CA 2 Public Key Infrastructure (PKI) used by CP-8831 series phones to issue SSL certificates is subject to an industry-wide issue that affects revocation abilities. Due to this issue, no new QuoVadis Root CA 2 certificates will be issued or renewed by Cisco after March 31, 2021. This affects certificate renewals on devices, Cisco cloud servers, and third-party services.
Certificates issued before the QuoVadis Root CA 2 was decommissioned will continue to be valid. However, the certificates will not renew when they expire on either the device or the Cisco cloud server. This will cause functions such as SIP and HTTPS connections to fail to establish.
### Problem Symptom
Expiration of the QuoVadis Root CA 2 certificates affects SIP or HTTPS communications and will cause handshakes to fail. Phones might not be provisioned and/or negotiate SIP security, and other security related features (not SIP related) might not work.
### Workaround/Solution
Cisco has migrated from the QuoVadis Root CA 2 to the IdenTrust Commercial Root CA 1 for SSL certificates.
Unfortunately there is no workaround and no software upgrade available due to the end of software support (see [EOL notice 12400](https://www.cisco.com/c/en/us/products/collateral/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/eos-eol-notice-c51-742916.html)). Cisco recommends migration to a device that is supported. The Cisco account team or reseller can help to understand what kind of options are available.
### For More Information
Cisco has created a web page to provide customers and partners with additional information on this issue. Consult the [QuoVadis Root CA 2 Decommission page](https://tools.cisco.com/security/center/resources/Q-CA-Root-Change) for a full list of products affected, associated Field Notices, and frequently asked questions.
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72366.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72366.html)
