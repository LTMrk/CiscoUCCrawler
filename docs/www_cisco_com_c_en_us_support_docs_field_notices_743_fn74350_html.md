  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco Catalyst 8200 Series Edge Platforms](https://www.cisco.com/c/en/us/support/routers/catalyst-8200-series-edge-platforms/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/catalyst-8200-series-edge-platforms/products-field-notices-list.html)


# Field Notice: FN74350 - Cisco Unified Border Element: Impact on Secure Communication Due to Upcoming Changes to TLS Certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting May 2026 - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74350.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74350.html)


Updated:June 23, 2026
Document ID:FN74350
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Critical
**Impact Rating:**
Critical
**First Published:**
2026-Feb-03
**Last Published:**
2026-Jun-23
**Revision:**
2.0
**Cisco Bug IDs:**
  * [CSCws22989](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws22989)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Product Name  | Description  | Comments  |  
| --- | --- | --- |  
| ASR1001-X  | ^Cisco ASR1001-X Chassis, 6 built-in GE, Dual P/S, 8GB DRAM  |   |  
| ASR1002-X  | ^Cisco ASR1002-X Chassis, 6 built-in GE, Dual P/S, 4GB DRAM  |   |  
| ASR1004  | ^Cisco ASR1004 Chassis, Dual P/S  |   |  
| ASR1006  | ^Cisco ASR1006 Chassis, Dual P/S  |   |  
| ASR1006-X  | Cisco ASR1006-X Chassis  |   |  
| C8000V-PF  | C8000V Platform Selection for DNA Subscription  |   |  
| C8200-1N-4T  | Cisco Catalyst C8200-1N-4T Router  |   |  
| C8200L-1N-4T  | Cisco Catalyst 8200L with 1-NIM slot and 4x1G WAN ports  |   |  
| C8300-1N1S-4T2X  | Cisco Catalyst C8300-1N1S-4T2X Router  |   |  
| C8300-1N1S-6T  | Cisco Catalyst C8300-1N1S-6T Router  |   |  
| C8300-2N2S-4T2X  | Cisco Catalyst C8300-2N2S-4T2X Router  |   |  
| C8300-2N2S-6T  | Cisco Catalyst C8300-2N2S-6T Router  |   |  
| ISR1100-4G  | ISR1100 Series Router, 4 Eth LAN/WAN Ports, 4G RAM  |   |  
| ISR4321-AX/K9  | Cisco ISR 4321 AX Bundle w/APP, SEC lic  |   |  
| ISR4321/K9  | Cisco ISR 4321 (2GE,2NIM,4G FLASH,4G DRAM,IPB)  |   |  
| ISR4331/K9-WS  | Cisco ISR 4331(3GE,2NIM,1SM,4GFLASH,4G DRAM,IPB) REFURBISHED  |   |  
| ISR4351/K9  | Cisco ISR 4351 (3GE,3NIM,2SM,4G FLASH,4G DRAM,IPB)  |   |  
| ISR4431/K9  | Cisco ISR 4431 (4GE,3NIM,8G FLASH,4G DRAM,IPB)  |   |  
| ISR4451-X/K9  | Cisco ISR 4451 (4GE,3NIM,2SM,8G FLASH,4G DRAM)  |   |  
| ISR4461/K9  | Cisco ISR 4461 (2x10GE+4x1GE,3NIM,3SM,8G FLASH,4G DRAM)  |   |  
  
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| IOS XE Software  | 16  | 16.1.1  | All Software Releases in 16.x.y are affected  |  
| IOS XE Software  | 17  | 17.1.1  | All Software Releases in 17.x.y are affected  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCws22989](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws22989)  | Certificate Segregation for CUBE TLS Profile-Client Trustpoint Support  |  
  

### Problem Description
  

Effective March 2027, the Chrome Root Program Policy will restrict root certificate authority (CA) certificates that are included in the Chrome Root Store, phasing out multi-purpose roots to align all public-key infrastructure (PKI) hierarchies to serve only TLS server authentication use cases.
This constraint includes root CAs that assert an Extended Key Usage (EKU) only for server authentication (id-kp-serverAuth). As a result, certificates issued by a public root CA with only Server Authentication EKU will not be valid for client authentication in mutual TLS (mTLS) setups.
**Note:** The effective date of the Chrome Root Program Policy is subject to change. For the most up-to-date information, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/).
  

### Background
  

To meet the Chrome Root Program Policy requirement, effective March 2027, public root CAs that are part of Chrome Root Store will be restricted to Server Authentication EKU only, effectively sunsetting the Client Authentication EKU from the store. As a response, public CA servers will stop issuing Client Authentication EKU certifications before March 2027. This date might change, and timelines will be decided by the CAs.
Certificates must include only Server Authentication EKU to maintain trust from the Google Chrome browser. Including the Client Authentication EKU in these certificates will be prohibited.
Although certain public root CAs continue to issue certificates containing the Client Authentication EKU, they will eventually be removed from the Chrome Root Store.
Certificates that are used for mTLS connections in Cisco Unified Border Elements (CUBE) devices are expected to include both Server and Client Authentication EKUs. Customers could choose to have these certificates from public CA providers.
Server Authentication EKU-only certificates that are provided by public root CAs can break certificate validity, leading to potential authentication issues in Cisco Unified Border Elements (CUBE) devices and affecting proper functionality.
For more details, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/).
  

### Problem Symptom
  

Cisco Unified Border Elements (CUBE) products can be affected by potential authentication issues and impacted functionality due to broken certificate validity that is caused by using Server Authentication EKU-only certificates provided by public root CAs.
  

### Workaround/Solution
  

Before considering workaround and solution options, audit current certificates. Prepare an inventory of all public TLS certificates to identify which certificates contain the Client Authentication EKU.
**Note:** The Cisco Integrated Services Router (ISR) 4000 Series platform is not supported by Cisco IOS XE Release 26.1.1. Consequently, the workarounds and solutions detailed in this field notice are not applicable to these devices. For more information, see [End-of-Sale and End-of-Life Announcement for the Cisco ISR4200, ISR4300 and select ISR4400 Series Platform](https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/select-isr4k-series-platform-eol.html). 
**Workaround**
Administrators can choose from one of the following workaround options.
> **Option 1: Switch to public root CAs that provide combined EKU certificates**
> Some public root CAs, such as DigiCert and IdenTrust, issue certificates with combined EKU types (server and client certificates) from an alternative root, which may not be included in the Chrome Root Store. Coordinate with the CA provider to check the availability of such certificates, and, before deploying them, ensure that both the server presenting the certificate and the clients consuming it trust the corresponding root CA. 
> This approach alleviates the need to upgrade server software to mitigate sunsetting of Client Authentication EKU that is enforced by the Chrome Root Program Policy. 
> The following table, which shows examples of public root CAs and EKU types, is not an exhaustive list and is for illustrative purposes only.  
> | CA Vendor  | EKU Type  | Root CA  | Issuing/Sub CA  |  
> | --- | --- | --- | --- |  
> | IdenTrust  | clientAuth + serverAuth   | IdenTrust Public Sector Root CA 1  | IdenTrust Public Sector Server CA 1  |  
> | IdenTrust  | clientAuth  | IdenTrust Public Sector Root CA 1  | TrustID RSA clientAuth CA 2  |  
> | IdenTrust  | serverAuth (browser trusted)  | IdenTrust Commercial Root CA 1  | HydrantID Server CA O1  |  
> | DigiCert  | clientAuth + serverAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID CA G2  |  
> | DigiCert  | clientAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID Client CA G2  |  
> | DigiCert  | serverAuth (browser trusted)  | DigiCert Global Root G2  | DigiCert Global G2 TLS RSA SHA256  |  
> **Option 2: Renew current certificates to extend validity**
> Certificates that were issued by public root CAs before the sunsetting of Client Authentication EKU and that have both Server and Client Authentication EKU will continue to be honored until their term expires. However, it is best to renew combined EKU certificates before policy sunsetting occurs.
> To maximize certificate validity, renew certificates before March 15, 2026, when public CAs will reduce maximum validity to 200 days. Note that CA policies vary. Some may implement this change earlier, reducing validity to 200 and 100 days. Work with CA providers to find the appropriate date and path. 
> **Note:** Some Public CAs have stopped issuing combined EKU certificates and may not provide one by default. To generate a certificate with a combined EKU, work with public CAs, which may provide special profiles. 
> Upgrade your servers after the solution mentioned in this field notice is available.
> The following image shows the Client Authentication EKU depreciation timeline, which is subject to change. For the most recent information, check with the specific CA.
> [![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74350_bddf65d8970c4f10f30f74c71153af45.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74350_bddf65d8970c4f10f30f74c71153af45.png "Related image, diagram or screenshot.")
> To manage certificates for your CUBE product, see [Cisco Unified Border Element Configuration Guide Through Cisco IOS XE 17.5](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-cube-sip-tls.html).
> **Option 3: Evaluate and migrate to alternatives**
> Evaluate the feasibility of transitioning to a private PKI and then set up a private CA to issue single certificates with combined EKUs.
> Before issuing or deploying a certificate, ensure that both the server presenting the certificate and all clients consuming it trust the corresponding root CA. Using this approach will alleviate the need to upgrade server software to mitigate sunsetting of Client Authentication EKU that is enforced by the Chrome Root Program Policy.
> **Option 4: For Cisco IOS XE Software releases earlier than Release 26.1.1**
> For Cisco IOS XE Software releases earlier than Release 26.1.1, strict EKU validation is not enforced unless the **match eku client-auth** command is configured on the trustpoint or the **cc-mode** is enabled. Consequently, the system will accept certificates containing only the Server EKU attribute for both trustpoint installation and peer certificate authentication.
**Solution**
The following product enhancements will be implemented in the fixed release that is described in the table in this section: 
  * **Segregation of client and server certificates:** This will enable support for two separate certificates on the same interface, such as X509 server certificates (with Server Authentication EKU) and X509 client certificates (with Client Authentication EKU) to facilitate mTLS connections. Customers must arrange for Client Authentication EKU certificates from either private PKI or alternate Root CAs. 
  * **Options for administrators to disable Client Authentication EKU checks:** This will allow CUBE products to ignore EKU from the remote peers (client) that are requesting a connection with Server Authentication EKU-only certificates. This option will also allow CUBE products to (re)use the Server Authentication EKU-only certificate as a client certificate. **Note:** The remote peer will also have to support a similar **Ignore Client Authentication EKU** model.


To segregate server and client certificates or to use the **Ignore EKU** option, upgrade to the fixed release of Cisco IOS XE Software as shown in the following table:  
| Product  | Affected Cisco IOS XE Software Release   | First Fixed Release   |  
| --- | --- | --- |  
| CUBE  | Earlier than 26.1.1  | 26.1.1 (future release)  |  
  

### Additional Information
  

The following field notices address other Cisco Collaboration products that are affected by this issue:
  * [FN74362: Cisco Expressway](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)
  * [FN74345: Cisco Calling On-Premises Products](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)


For more information about this issue, see the following:
  * [Public CA certificate changes impacting Dedicated Instance](https://help.webex.com/en-us/article/zo55dl/Public-CA-certificate-changes-impacting-Dedicated-Instance)
  * [Blog: Changes to TLS clientAuth Certificates - Ensuring You’re Not Impacted](https://blogs.cisco.com/security/changes-to-tls-clientauth-certificates)
  * [Certificate EKU Changes: Actions Cisco On-premises Collaboration Customers MUST TAKE NOW](https://blog.webex.com/collaboration/certificate-eku-changes-actions-cisco-premises-collaboration-customers-must-take-now/)

  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 2.0  | Added one more workaround option.  | Workaround/Solution  | 2026-JUN-23  |  
| 1.1  | Added blog and article links for more details. Updated information about the dates when the Chrome Root Program Policy is scheduled to go into effect.  | Problem Description, Background, Workaround/Solution, Additional Information  | 2026-MAR-27  |  
| 1.0  | Initial Release  | —  | 2026-FEB-03  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4321 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4321-integrated-services-router/model.html)
  * [4331 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4331-integrated-services-router-isr/model.html)
  * [4351 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4351-integrated-services-router/model.html)
  * [4431 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4441-x-integrated-services-router-isr/model.html)
  * [4451-X Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4451-x-integrated-services-router-isr/model.html)
  * [4461 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4461-integrated-services-router/model.html)
  * [ASR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/asr-1000-series-ios-xe-sd-wan/model.html)
  * [ASR 9001 Router](https://www.cisco.com/c/en/us/support/routers/asr-9001-router/model.html)
  * [ISR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-1000-series-ios-xe-sd-wan/model.html)
  * [ISR 4000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-4000-series-ios-xe-sd-wan/model.html)

+ Show All 10 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)
