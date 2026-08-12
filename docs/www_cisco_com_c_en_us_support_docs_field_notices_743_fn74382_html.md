  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified IP Interactive Voice Response (IVR)](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-ip-interactive-voice-response-ivr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-ip-interactive-voice-response-ivr/products-field-notices-list.html)


# Field Notice: FN74382 - Cisco Unified Contact Center Products: Impact on Secure Communication Due to Upcoming Changes to TLS certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting March 2027 - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74382.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74382.html)


Updated:May 13, 2026
Document ID:FN74382
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Critical
**Impact Rating:**
Critical
**First Published:**
2026-Mar-30
**Last Published:**
2026-May-13
**Revision:**
2.0
**Cisco Bug IDs:**
  * [CSCwt38851](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38851), 
  * [CSCwt23909](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt23909), 
  * [CSCwt23908](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt23908), 
  * [CSCwt38849](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38849), 
  * [CSCwt38846](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38846), 
  * [CSCwt38841](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38841), 
  * [CSCwt79317](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt79317)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Cisco Customer Voice Portal Software Releases  | 12  | 12.5(1), 12.6(2)  | All releases are affected.  |  
| Cisco Customer Voice Portal Software Releases  | 15  | 15.0(1)  | All releases are affected.  |  
| Cisco Virtualized Voice Browser Software Releases  | 12  | 12.5(1), 12.6(1), 12.6(2)  | All releases are affected.  |  
| Cisco Virtualized Voice Browser Software Releases  | 15  | 15.0(1)  | All releases are affected.  |  
| Finesse Software  | 12  | 12.5(1), 12.6(1), 12.6(2)  | All releases are affected.  |  
| Finesse Software  | 15  | 15.0(1)  | All releases are affected.  |  
| Packaged Contact Center Enterprise Virtual Machine Templates  | 12  | 12.5(1), 12.6(1), 12.6(2)  | All releases are affected.  |  
| Packaged Contact Center Enterprise Virtual Machine Templates  | 15  | 15.0(1)  | All releases are affected.  |  
| Unified Contact Center Enterprise Virtual Machine Templates  | 12  | 12.5(1), 12.6(1), 12.6(2)  | All releases are affected.  
All releases are affected.  |  
| Unified Contact Center Enterprise Virtual Machine Templates  | 15  | 15.0(1)  | All releases are affected.  |  
| Unified Contact Center Express Software  | 12  | 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3  | All releases are affected including Customer Collaboration Platform and Unified IP Interactive Voice Response (IP IVR)  |  
| Unified Contact Center Express Software  | 15  | 15.0(1)  | All releases are affected including Customer Collaboration Platform and Unified IP Interactive Voice Response (IP IVR)  |  
| Unified Intelligence Center Software  | 12  | 12.5(1), 12.6(1), 12.6(2)  | All releases are affected.  |  
| Unified Intelligence Center Software  | 15  | 15.0(1)  | All releases are affected.  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwt38851](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38851)  | Support for Separate Server and Client Certificate Support for CUIC  |  
| [CSCwt23909](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt23909)  | Support for Separate Server and Client Certificate Support for PCCE  |  
| [CSCwt23908](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt23908)  | Support for Separate Server and Client Certificate Support for UCCE  |  
| [CSCwt38849](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38849)  | Support for Separate Server and Client Certificate Support for Finesse  |  
| [CSCwt38846](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38846)  | Support for Separate Server and Client Certificate Support for Virtual VoiceBrowser  |  
| [CSCwt38841](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt38841)  | Support for Separate Server and Client Certificate Support for Cloud Connect  |  
| [CSCwt79317](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt79317)  | Implement EKU policy change in CCX  |  
  

### Problem Description
  

Effective March 2027, the Chrome Root Program Policy will restrict root certificate authority (CA) certificates that are included in the Chrome Root Store, phasing out multi-purpose roots to align all public-key infrastructure (PKI) hierarchies to serve only TLS server authentication use cases.
This constraint includes root CAs that assert an Extended Key Usage (EKU) only for server authentication (id-kp-serverAuth). As a result, certificates issued by a public root CA with only Server Authentication EKU will not be valid for client authentication in mutual TLS (mTLS) setups.
**Note:** The effective date of the Chrome Root Program Policy is subject to change. For the most up-to-date information, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/).
  

### Background
  

To meet the Chrome Root Program Policy requirement, effective March 2027, public root CAs that are part of Chrome Root Store will be restricted to Server Authentication EKU only, effectively sunsetting the Client Authentication EKU from the store. As a response, public CA servers will stop issuing Client Authentication EKU certifications before March 2027. This date might change, and timelines will be decided by the CAs.
Certificates must include only Server Authentication EKU to maintain trust from the Google Chrome browser. Including the Client Authentication EKU in these certificates will be prohibited.
Although certain public root CAs continue to issue certificates containing the Client Authentication EKU, they will eventually be removed from the Chrome Root Store.
Certificates that are used for mTLS connections in Cisco Unified Contact Center products are expected to include both Server and Client Authentication EKUs. Customers could choose to have these certificates from public CA providers.
Server Authentication EKU-only certificates that are provided by public root CAs can break certificate validity, leading to potential authentication issues in Cisco Unified Contact Center products and affecting proper functionality.
For more details, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/).
  

### Problem Symptom
  

Cisco Unified Contact Center products can be affected by potential authentication issues and impacted functionality due to broken certificate validity that is caused by using Server Authentication-only certificates provided by public root CAs.
  

### Workaround/Solution
  

Before considering workaround and solution options, audit current certificates. Prepare an inventory of all public TLS certificates to identify which certificates contain the Client Authentication EKU. 
**Workaround**
Administrators can choose from one of the following workaround options.
> **Option 1: Switch to public root CAs that provide combined EKU certificates**
> Some public root CAs, such as DigiCert and IdenTrust, issue certificates with combined EKU types (server and client certificates) from an alternative root, which may not be included in the Chrome Root Store. Coordinate with the CA provider to check the availability of such certificates, and, before deploying them, ensure that both the server presenting the certificate and the clients consuming it trust the corresponding root CA.
> This approach alleviates the need to upgrade server software to mitigate sunsetting of Client Authentication EKU enforced by the Chrome Root Program Policy.
> The following table, which shows examples of public root CAs and EKU types, is not an exhaustive list and is for illustrative purposes only.  
> | CA Vendor  | EKU Type  | Root CA  | Issuing/Sub CA  |  
> | --- | --- | --- | --- |  
> | IdenTrust  | clientAuth + serverAuth  | IdenTrust Public Sector Root CA 1  | IdenTrust Public Sector Server CA 1  |  
> | IdenTrust  | clientAuth  | IdenTrust Public Sector Root CA 1  | TrustID RSA ClientAuth CA 2  |  
> | IdenTrust  | serverAuth (browser trusted)  | IdenTrust Commercial Root CA 1  | HydrantID Server CA O1  |  
> | DigiCert  | clientAuth + serverAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID CA G2  |  
> | DigiCert  | clientAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID Client CA G2  |  
> | DigiCert  | serverAuth (browser trusted)  | DigiCert Global Root G2  | DigiCert Global G2 TLS RSA SHA256  |  
> **Option 2: Renew current certificates to extend validity**
> Certificates that were issued by public root CAs before the sunsetting of Client Authentication EKU and that have both Server and Client Authentication EKU will continue to be honored until their term expires. However, it is best to renew combined EKU certificates before policy sunsetting occurs.
> To maximize certificate validity, renew certificates before March 15, 2026, when public CAs will reduce maximum validity to 200 days. Note that CA policies vary. Some may implement this change earlier, reducing validity to 200 and 100 days. Work with CA providers to find the appropriate date and path.
> Note: Some Public CAs have stopped issuing combined EKU certificates and may not provide one by default. To generate a certificate with a combined EKU, work with public CAs, which may provide special profiles. 
> Upgrade servers after the solution mentioned in this field notice is available.
> The following image shows the Client Authentication EKU depreciation timeline, which is subject to change. For the most recent information, check with the specific CA:
> [![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74382_379aa114970c4f10f30f74c71153af0b.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74382_379aa114970c4f10f30f74c71153af0b.png "Related image, diagram or screenshot.")
> **Option 3: Evaluate and Migrate to Alternatives.**
> Evaluate the feasibility of transitioning to a private PKI and then set up a private CA to issue single certificates with combined EKUs.
> Before issuing or deploying a certificate, ensure that both the server presenting the certificate and all clients consuming it trust the corresponding root CA. Using this approach will alleviate the need to upgrade server software to mitigate sunsetting of Client Authentication EKU that is enforced by the Chrome Root Program Policy.
**Solution**
The following product enhancements will be implemented in the fixed release that is described in the table in this section:
  * **Segregation of client and server certificates:** This will enable support for two separate certificates on the same interface, such as Tomcat server certificates (with Server Authentication EKU) and Tomcat client certificates (with Client Authentication EKU) to facilitate mTLS connections. Customers must arrange for Client Authentication EKU certificates from either private PKI or alternate root CAs.
  * **Options for administrators to disable Client Authentication EKU checks:** This will allow Cisco Unified Contact Center products to ignore EKU from remote peers (clients) that are requesting a connection with Server Authentication EKU-only certificates. This option will also allow Cisco Unified Contact Center products to (re)use the Server Authentication EKU-only certificate as a client certificate. **Note:** The remote peer will also have to support a similar Ignore Client Authentication EKU model.


To segregate server and client certificates or to use the Ignore EKU option, upgrade to a fixed release as shown in the following table:  
| Affected Cisco Product  | Affected Releases  | First Fixed Release  |  
| --- | --- | --- |  
|  Customer Collaboration Platform (CCP)  
Finesse  
Packaged Contact Center Enterprise (CCE)  
Unified CCE  
Unified Contact Center Express (CCX)  
Unified Customer Voice Portal (CVP)  
Unified IP Interactive Voice Response (IP IVR)  
Unified Intelligence Center  
Virtualized Voice Browser  |  12.5(1), 12.6(1), 12.6(2), 15.0(1), 15.0(1)SU1  | 15.0(1)SU2 (future release Q4CY26)  |  
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 2.0  | Added two affected products: Cisco Unified Contact Center Express (CCX) and Cisco Customer Collaboration Platform (CCP).  | Products Affected, Workaround/Solution, Defect Information  | 2026-MAY-13  |  
| 1.0  | Initial Release  | —  | 2026-MAR-30  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Field Notice: FN74345 - Cisco On-Premises Calling Products: Impact on Secure Communication Due to Upcoming Changes to TLS certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting May 2026 - Workaround Provided](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
  * [Field Notice: FN74362 - Cisco Expressway: Impact on Secure Communication due to Upcoming Changes to TLS Certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting May 2026 - Workaround Provided](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Packaged Contact Center Enterprise 12.5(1)](https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-12-5-1/model.html)
  * [Packaged Contact Center Enterprise 12.5(2)](https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-12-5-2/model.html)
  * [Packaged Contact Center Enterprise 12.6(1)](https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-12-6-1/model.html)
  * [Packaged Contact Center Enterprise 12.6(2)](https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-12-6-2/model.html)
  * [Packaged Contact Center Enterprise 15.0(1)](https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-15-0-1/model.html)
  * [Unified Contact Center Enterprise 12.5(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-enterprise-12-5-1/model.html)
  * [Unified Contact Center Enterprise 12.5(2)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-enterprise-12-5-2/model.html)
  * [Unified Contact Center Enterprise 12.6(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-enterprise-12-6-1/model.html)
  * [Unified Contact Center Enterprise 12.6(2)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-enterprise-12-6-2/model.html)
  * [Unified Contact Center Enterprise 15.0(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-enterprise-15-0-1/model.html)
  * [Unified Contact Center Express 12.5(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-express-12-5-1/model.html)
  * [Unified Contact Center Express 15.0(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-express-15-0/model.html)
  * [Unified Customer Voice Portal 12.5(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-customer-voice-portal-12-5-1/model.html)
  * [Unified Customer Voice Portal 12.6(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-customer-voice-portal-12-6-1/model.html)
  * [Unified Customer Voice Portal 12.6(2)](https://www.cisco.com/c/en/us/support/contact-center/unified-customer-voice-portal-12-6-2/model.html)
  * [Unified Customer Voice Portal 15.0(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-customer-voice-portal-15-0-1/model.html)
  * [Unified Intelligence Center 12.5(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-intelligence-center-12-5-1/model.html)
  * [Unified Intelligence Center 12.6(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-intelligence-center-12-6-1/model.html)
  * [Unified Intelligence Center 12.6(2)](https://www.cisco.com/c/en/us/support/contact-center/unified-intelligence-center-12-6-2/model.html)
  * [Unified Intelligence Center 15.0(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-intelligence-center-15-0-1/model.html)

+ Show All 20 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74382.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)
