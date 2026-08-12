  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Expressway Series](https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-field-notices-list.html)


# Field Notice: FN74362 - Cisco Expressway: Impact on Secure Communication due to Upcoming Changes to TLS Certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting May 2026 - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74362.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74362.html)


Updated:June 1, 2026
Document ID:FN74362
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Critical
**Impact Rating:**
Critical
**First Published:**
2026-Jan-30
**Last Published:**
2026-Jun-01
**Revision:**
1.2
**Cisco Bug IDs:**
  * [CSCwr73373](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwr73373)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Expressway Core and Edge  | X14  | X14.0.0, X14.0.1, X14.0.10, X14.0.11, X14.0.2, X14.0.3, X14.0.4, X14.0.5, X14.0.6, X14.0.7, X14.0.8, X14.0.9, X14.2.0, X14.2.1, X14.2.2, X14.2.5, X14.2.6, X14.2.7, X14.3.0, X14.3.1, X14.3.2, X14.3.3, X14.3.4, X14.3.5, X14.3.6, X14.3.7  | All releases are affected. See the Workaround/Solution section for additional details.  |  
| Expressway Core and Edge  | X15  | X15.0.0, X15.0.1, X15.0.2, X15.0.3, X15.2.0, X15.2.1, X15.2.2, X15.2.3, X15.2.4, X15.2.4., X15.3.0, X15.3.1, X15.3.2  | All releases are affected. See the Workaround/Solution section for additional details.  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwr73373](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwr73373)  | Support for separate server and client Certificate for Expressway  |  
  

### Problem Description
  

Effective March 2027, the Chrome Root Program Policy will restrict root certificate authority (CA) certificates that are included in the Chrome Root Store, phasing out multi-purpose roots to align all public-key infrastructure (PKI) hierarchies to serve only TLS server authentication use cases.
This constraint includes root CAs that assert an Extended Key Usage (EKU) only for server authentication (id-kp-serverAuth). As a result, certificates issued by a public root CA with only Server Authentication EKU will not be valid for client authentication in mutual TLS (mTLS) setups.
**Note** : The effective date of the Chrome Root Program Policy is subject to change. For the most up-to-date information, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/).
  

### Background
  

To meet the Chrome Root Program Policy requirement, effective March 2027, public root CAs that are part of the Chrome Root Store will be restricted to Server Authentication EKU only, effectively sunsetting the Client Authentication EKU from the store. This date might change, and timelines will be decided by the CAs.
Certificates must include only Server Authentication EKU to maintain trust from the Google Chrome browser. Including the Client Authentication EKU in these certificates will be prohibited.
Although certain public root CAs continue to issue certificates containing the Client Authentication EKU, they will eventually be removed from the Chrome Root Store.
Certificates that are used for mTLS connections in Cisco Expressway are expected to include both Server and Client Authentication EKUs. Customers could choose to have these certificates from public CA providers.
Server Authentication EKU-only certificates that are provided by public root CAs can break certificate validity, leading to potential authentication issues in Cisco Expressway and affecting proper functionality.
For more details, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/).
  

### Problem Symptom
  

Cisco Expressway can be affected by potential authentication issues and impacted functionality due to broken certificate validity that is caused by using Server Authentication EKU-only certificates provided by public root CAs. The public CA-signed certificate with Client Authentication EKU that is currently used for mTLS connections in Cisco Expressway is the **Expressway Certificate**.
This certificate is used for different mTLS connections, as shown in the following examples:
  * SIP B2B call over mTLS (Expressway E becomes client or server on mTLS connection, depending on session-initiated site).
  * SIP IMP Federation over mTLS (Expressway E becomes client or server on mTLS connection, depending on session-initiated site).
  * UC Traversal Zone (Expressway C presents Client Authentication EKU).
  * Traversal Zone with mTLS configuration (Expressway C presents Client Authentication EKU).
  * SIP Neighbor Zone with mTLS configuration (Expressway becomes client or server on mTLS connection, depending on session-initiated site), including Cisco Unified Communications Manager (Unified CM), Cisco Unity, Cisco Unified Border Element (CUBE), and Cisco Meeting Server (CMS).
  * Connection to Cisco Cloud (Mobile and Remote Access (MRA) Onboarding, with Expressway initiating the connection to Cisco Cloud and presenting Client Authentication EKU).

  

### Workaround/Solution
  

Before considering workaround and solution options, audit current certificates. Prepare an inventory of all public TLS certificates to identify which certificates contain the Client Authentication EKU. It is recommended that customers take a backup of their Cisco Expressway instance or manually copy the signed certificate and Private key.
**Workaround**
Administrators can choose from one of the following workaround options.
> **Option 1: Switch to public root CAs that provide combined EKU certificates.**
> Some public root CAs, such as DigiCert and IdenTrust, issue certificates with combined EKU types (server and client certificates) from an alternative root, which may not be included in the Chrome Root Store. Coordinate with the CA provider to check the availability of such certificates, and, before deploying them, ensure that both the server presenting the certificate and the clients consuming it trust the corresponding root CA.
> The following table, which shows examples of public root CAs and EKU types, is not an exhaustive list and is for illustrative purposes only.  
> | **CA Vendor**  | **EKU Type**  | **Root CA**  | **Issuing/Sub CA**  |  
> | --- | --- | --- | --- |  
> | IdenTrust  | clientAuth + serverAuth  | IdenTrust Public Sector Root CA 1  | IdenTrust Public Sector Server CA 1  |  
> | IdenTrust  | clientAuth  | IdenTrust Public Sector Root CA 1  | TrustID RSA ClientAuth CA 2  |  
> | IdenTrust  | serverAuth (browser trusted)  | IdenTrust Commercial Root CA 1  | HydrantID Server CA O1  |  
> | DigiCert  | clientAuth + serverAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID CA G2  |  
> | DigiCert  | clientAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID Client CA G2  |  
> | DigiCert  | serverAuth (browser trusted)  | DigiCert Global Root G2  | DigiCert Global G2 TLS RSA SHA256  |  
> **Option 2: Renew current certificates to extend validity.**
> Certificates that were issued by public root CAs before the sunsetting of Client Authentication EKU and that have both Server and Client Authentication EKU will continue to be honored until their term expires. However, it is best to renew combined EKU certificates before policy sunsetting occurs.
> To maximize certificate validity, renew certificates before March 15, 2026, when public CAs will reduce maximum validity to 200 days. Note that CA policies vary. Some may implement this change earlier, reducing validity to 200 and 100 days. Work with CA providers to find the appropriate date and path.
> **For customers using Let's Encrypt Certificates:** Currently, Expressway uses a **classic** ACME profile and cannot be modified by users. This **classic** ACME profile is presently used for requesting certificates that include both Server and Client Authentication EKUs. **Starting February 11, 2026** , certificate requests using this profile will no longer include the Client Authentication EKU in certificates generated by Let's Encrypt.
>   * **Note:** Customers that are using Let's Encrypt certificates with the **classic** ACME profile should renew before February 11, 2026, ideally as close to that date as possible to maximize validity. For more information, see [Ending TLS Client Authentication Certificate Support in 2026 - Let's Encrypt.](https://letsencrypt.org/2025/05/14/ending-tls-client-authentication)
>   * Customers should also disable the ACME automated scheduler to prevent certificates from being automatically renewed after February 11, 2026. This action will help avoid certificates being inadvertently overwritten with versions that contain only the Server Authentication EKU.
> 

> **Note:** Some public CAs have stopped issuing combined EKU certificates and may not provide one by default. To generate a certificate with a combined EKU, work with public CAs, which may provide special profiles.
> The following image shows the Client Authentication EKU depreciation timeline, which is subject to change. For the most recent information, check with the specific CA.
> [![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74362_78bcffd8878d87104dc14047cebb3570.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74362_78bcffd8878d87104dc14047cebb3570.png "Related image, diagram or screenshot.")
> After the solution becomes available, upgrade servers. For more information, see the **Solution** section of this Field Notice. Follow the steps in the relevant Cisco Expressway Admin Guide to manage Expressway certificates:
>   * [Cisco Expressway Certificate Creation and Use Deployment Guide (X14.0)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/cert_creation_use/exwy_b_cisco-expressway-certificate-creation-and-use-deployment-guide-x14-0.pdf)
>   * [Cisco Expressway Certificate Creation and Use Deployment Guide (X15.0)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/cert-creation-use/exwy_b_cisco-expressway-certificate-creation-and-use-deployment-guide-x150.pdf)
> 

> **Option 3: Evaluate and Migrate to Alternatives (for Expressway C only; not applicable for Expressway E).**
> Evaluate the feasibility of transitioning to a private PKI and then set up a private CA to issue single certificates with combined EKUs.
> Before issuing or deploying a certificate, ensure that both the server presenting the certificate and all clients consuming it trust the corresponding root CA.
### **Solution**
The following product enhancements will be implemented in the fixed release that is described in the table in this section:
  * **Segregation****of client and server certificates:** This will enable support for two separate certificates on the same interface (such as Expressway certificates with distinct Server Authentication EKU and Client Authentication EKU) to facilitate mTLS connections.
  * **Options for administrators to disable Client Authentication EKU check:** This will allow Cisco Expressway to ignore EKU from remote peers (client) that are requesting a connection with Server Authentication EKU-only certificates. In the absence of a Client Authentication EKU certificate, this option will also allow Expressway to (re)use the Server Authentication EKU-only certificate as a Client certificate. **Note:** The remote peer will also have to support a similar **Ignore Client Authentication EKU** model.


To segregate server and client certificates or to use the **Ignore EKU** option, upgrade to a fixed release as shown in the following table:  
| Product  | Affected Release   | Fixed Release  | Purpose of Fix  |  
| --- | --- | --- | --- |  
| Cisco Expressway  |  X14.x Release Train: All releases X15.x Release Train: Earlier than X15.4  |  X15.4 This release allows additional upload of ServerAuth EKU-only signed certificate on Expressway E and certificate verification adjustment for MRA SIP signal between Expressway E and Expressway C.  |  To accommodate certificates with ServerAuth EKU only and to enable MRA registrations.  |  
| Cisco Expressway  |  X14.x Release Train: All releases X15.x Release Train: Earlier than X15.5  |  X15.5 This release provides UI enhancement for segregating client and server certificates and provides options to administrators to disable EKU checking.  | To meet global Google Chrome Root Program requirements.  |  
**Note:** Both Cisco Expressway E and Expressway C must be upgraded to the same version.
  

### Additional Information
  

The following field notices address other Cisco Collaboration products that are affected by this issue:
  * [FN74345: Cisco Calling On-Premises products](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
  * [FN74350: Cisco Unified Border Element (CUBE)](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)


For more information about this issue, see the following:
  * [Public CA certificate changes impacting Dedicated Instance](https://help.webex.com/en-us/article/zo55dl/Public-CA-certificate-changes-impacting-Dedicated-Instance)
  * [Blog: Changes to TLS clientAuth Certificates - Ensuring You're Not Impacted](https://blogs.cisco.com/security/changes-to-tls-clientauth-certificates)
  * [Certificate EKU Changes: Actions Cisco On-premises Collaboration Customers MUST TAK NOW](https://blog.webex.com/collaboration/certificate-eku-changes-actions-cisco-premises-collaboration-customers-must-take-now/)

  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.2  | Added blog and article links for more details. Updated information about the dates when the Chrome Root Program Policy is scheduled to go into effect.  | Problem Description, Background, Problem Symptom, Workaround/Solution, Additional Information  | 2026-JUN-01  |  
| 1.1  | Updated information to explain that public CA servers will stop issuing Client Authentication EKU certifications from May 2026.  | Background  | 2026-FEB-03  |  
| 1.0  | Initial Release  | —  | 2026-JAN-30  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74362.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)
