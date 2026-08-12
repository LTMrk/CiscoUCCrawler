  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Emergency Responder](https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-field-notices-list.html)


# Field Notice: FN74345 - Cisco On-Premises Calling Products: Impact on Secure Communication Due to Upcoming Changes to TLS certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting May 2026 - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74345.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74345.html)


Updated:March 31, 2026
Document ID:FN74345
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Critical
**Impact Rating:**
Critical
**First Published:**
2026-Jan-30
**Last Published:**
2026-Mar-25
**Revision:**
1.2
**Cisco Bug IDs:**
  * [CSCws03463](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03463), 
  * [CSCws02424](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws02424), 
  * [CSCws03437](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03437), 
  * [CSCws03022](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03022)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Emergency Responder  | -  |   | All releases are affected.  |  
| Unified Communications Manager  | -  |   | All releases are affected including Session Management Edition  |  
| Unified Communications Manager IM and Presence Service  | -  |   | All releases are affected.  |  
| Unity Connection  | -  |   | All releases are affected.  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCws03463](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03463)  | Support for separate server and client Certificate for CUC  |  
| [CSCws02424](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws02424)  | Support for Separate Server and Client Certificate Support for CUCM  |  
| [CSCws03437](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03437)  | Support for Separate Server and Client Certificate Support for IM&P  |  
| [CSCws03022](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03022)  | Support for separate server and client Certificate for CER  |  
  

### Problem Description
  

Effective March 2027, the Chrome Root Program Policy will restrict root certificate authority (CA) certificates that are included in the Chrome Root Store, phasing out multi-purpose roots to align all public-key infrastructure (PKI) hierarchies to serve only TLS server authentication use cases.
This constraint includes root CAs that assert an Extended Key Usage (EKU) only for server authentication (id-kp-serverAuth). As a result, certificates issued by a public root CA with only Server Authentication EKU will not be valid for client authentication in mutual TLS (mTLS) setups.
**Note:** The effective date of the Chrome Root Program Policy is subject to change. For the most up-to-date information, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/). 
  

### Background
  

To meet the Chrome Root Program Policy requirement, effective March 2027, public root CAs that are part of Chrome Root Store will be restricted to Server Authentication EKU only, effectively sunsetting the Client Authentication EKU from the store. As a response, public CA servers will stop issuing Client Authentication EKU certifications before March 2027. This date might change, and timelines will be decided by the CAs.
Certificates must include only Server Authentication EKU to maintain trust from the Google Chrome browser. Including the Client Authentication EKU in these certificates will be prohibited.
Although certain public root CAs continue to issue certificates containing the Client Authentication EKU, they will eventually be removed from the Chrome Root Store.
Certificates that are used for mTLS connections in Cisco Unified Communication devices are expected to include both Server and Client Authentication EKUs. Customers could choose to have these certificates from public CA providers.
Server Authentication EKU-only certificates that are provided by public root CAs can break certificate validity, leading to potential authentication issues in Cisco Unified Communication devices and affecting proper functionality.
For more details, see the [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/).
  

### Problem Symptom
  

Cisco on-premises calling products can be affected by potential authentication issues and impacted functionality due to broken certificate validity that is caused by using Server Authentication-only certificates provided by public root CAs.
The following list shows examples of certificates that are used for mTLS connections in these Cisco on-premises calling products:
  * Unified Communication Manager/Session Management Edition (Unified CM/Unified CM SME): Tomcat, TVS, Call Manager, and IPSec
  * Unified Communication Manager IM & Presence Service (Unified CM IM&P), formerly Cisco Unified Presence (CUP): cup-xmpp-s2s
  * Emergency Responder: Tomcat
  * Unity Connection: Tomcat


The following list shows examples of certificates that are used for different mTLS connections:
  * Tomcat: Connections with external servers like Lightweight Directory Access Protocol (LDAP), filebeat, logslash server, and SIP Oauth over MRA
  * Call Manager: SIP Trunk connections and internode/intercluster connections
  * TVS: Online-CAPF (Certificate Authority Proxy Function) connection
  * IPSec: IPSec connections with other Cisco Unified CM nodes and Gateways
  * CUP: Secure SIP connections with Cisco Unified CM and third party clients
  * CUP-XMPP-S2S: Extensible Messaging and Presence Protocol (XMPP) federation

  

### Workaround/Solution
  

Before considering workaround and solution options, audit current certificates. Prepare an inventory of all public TLS certificates to identify which certificates contain the Client Authentication EKU.
**Workaround**
Administrators can choose from one of the following workaround options.
> **Option 1: Switch to public root CAs that provide combined EKU certificates.**
> Some public root CAs, such as DigiCert and IdenTrust, issue certificates with combined EKU types (server and client certificates) from an alternative root, which may not be included in the Chrome Root Store. Coordinate with the CA provider to check the availability of such certificates, and, before deploying them, ensure that both the server presenting the certificate and the clients consuming it trust the corresponding root CA.
> This approach alleviates the need to upgrade server software to mitigate sunsetting of Client Authentication EKU that is enforced by the Chrome Root Program Policy.
> The following table, which shows examples of public root CAs and EKU types, is not an exhaustive list and is for illustrative purposes only.  
> | CA Vendor  | EKU Type  | Root CA  | Issuing/Sub CA  |  
> | --- | --- | --- | --- |  
> | IdenTrust  | clientAuth + serverAuth   | IdenTrust Public Sector Root CA 1  | IdenTrust Public Sector Server CA 1  |  
> | IdenTrust  | clientAuth  | IdenTrust Public Sector Root CA 1  | TrustID RSA ClientAuth CA 2  |  
> | IdenTrust  | serverAuth (browser trusted)  | IdenTrust Commercial Root CA 1  | HydrantID Server CA O1  |  
> | DigiCert  | clientAuth + serverAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID CA G2  |  
> | DigiCert  | clientAuth  | DigiCert Assured ID Root G2  | DigiCert Assured ID Client CA G2  |  
> | DigiCert  | serverAuth (browser trusted)  | DigiCert Global Root G2  | DigiCert Global G2 TLS RSA SHA256  |  
> **Option 2: Renew current certificates to extend validity.**
> Certificates that were issued by public root CAs before the sunsetting of Client Authentication EKU and that have both Server and Client Authentication EKU will continue to be honored until their term expires. However, it is best to renew combined EKU certificates before policy sunsetting occurs.
> To maximize certificate validity, renew certificates before March 15, 2026, when public CAs will reduce maximum validity to 200 days. Note that CA policies vary. Some may implement this change earlier, reducing validity to 200 and 100 days. Work with CA providers to find the appropriate date and path.
> **Note:** Some public CAs have stopped issuing combined EKU certificates and may not provide one by default. To generate a certificate with a combined EKU, work with public CAs, which may provide special profiles.
> Upgrade servers after the solution mentioned in this field notice is available.
> The following image shows the Client Authentication EKU depreciation timeline, which is subject to change. For the most recent information, check with the specific CA.
> [![EKU Sunsetting Chart March 2026.png](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74345_e7052dd897c84f10f30f74c71153af9b.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74345_e7052dd897c84f10f30f74c71153af9b.png "EKU Sunsetting Chart March 2026.png")
> To manage certificates for Cisco Collaboration products, see the steps in the following guides: 
>   * [Cisco Unified Communication Manager Certificate Regeneration](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/adminGd/cucm_b_administration-guide-15/cucm_b_test-adminguide_chapter_01111.html#CUCM_TK_U8A8E8DA_00)
>   * [Cisco Emergency Responder 15 Certificate Management](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/15/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-15/cer0_b_cisco-emergency-responder-administration-guide-1401_appendix_010001.html#CER0_RF_C610A8DA_00)
>   * [Cisco Emergency Responder 14 Certificate Management](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/14su2/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-14su2/cer0_b_cisco-emergency-responder-administration-guide-1401_chapter_0111.html#concept_CFD893C1425A15DF2EF4C4972F3D8BBC)
>   * [Cisco Unity Connection 15 Security Administration](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx/b_15cucosagx_chapter_0101.html#ID-2301-0000001a)
>   * [Cisco Unity Connection 14 Security Administration](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx/b_14cucosagx_chapter_0101.html#:~:text=Login%20to%20Cisco%20Unified%20Communications%20Operating%20System%20Administration%20window.&text=Generate%20a%20CSR%20on%20the,Generating%20a%20Certificate%20Signing%20Request%E2%80%9D%20.&text=Download%20the%20CSR%20to%20your,Downloading%20a%20Certificate%20Signing%20Request%E2%80%9D.&text=Use%20the%20CSR%20to%20obtain,CA%20Certificates%E2%80%9D%20for%20additional%20notes.&text=Obtain%20the%20CA%20root%20certificate,CA%20Certificates%E2%80%9D%20for%20additional%20notes.&text=Upload%20the%20CA%20root%20certificate,the%20%E2%80%9CUpload%20Trust%20Certificate%E2%80%9D%20.&text=Upload%20the%20application%20certificate%20to,the%20%E2%80%9CUpload%20Application%20Certificate%E2%80%9D%20.&text=Restart%20the%20services%20that%20are,the%20Connection%20Conversation%20Manager%20service.)
> 

> **Option 3: Evaluate and Migrate to Alternatives**
> Evaluate the feasibility of transitioning to a private PKI and then set up a private CA to issue single certificates with combined EKUs.
> Before issuing or deploying a certificate, ensure that both the server presenting the certificate and all clients consuming it trust the corresponding root CA. Using this approach will alleviate the need to upgrade server software to mitigate sunsetting of Client Authentication EKU that is enforced by the Chrome Root Program Policy.
**Solution**
The following product enhancements will be implemented in the fixed release that is described in the table in this section:
  * **Segregation of client and server certificates:** This will enable support for two separate certificates on the same interface, such as Tomcat server certificates (with Server Authentication EKU) and Tomcat client certificate (with Client Authentication EKU) to facilitate mTLS connections. Customers must arrange for Client Authentication EKU certificates from either private PKI or alternate root CAs.


  * **Options for administrators to disable Client Authentication EKU checks:** This will allow on-premises calling products to ignore EKU from remote peers (client) that are requesting a connection with Server Authentication EKU-only certificate. This option will also allow on-premises calling products to (re)use the Server Authentication EKU-only certificate as a client certificate. **Note:** The remote peer will also have to support a similar **Ignore Client Authentication EKU** model.


To segregate server and client certificates or to use the **Ignore EKU** option, upgrade to a fixed release as shown in the following table:  
| Product  | Affected Release  | Fixed Release  |  
| --- | --- | --- |  
| Emergency Responder  
Unified CM  
Unified CM IM&P  
Unified CM SME  
Unity Connection   
Unity Connection Survivable Remote Site Voicemail (SRSV)  | 14  
14 SU1  
14 SU2  
14 SU3  
14 SU4  
15  
15 SU1  
15 SU2  
15 SU3a  
15 SU4  | 15 SU5 (future release Q4CY26)  |  
  

### Additional Information
  

The following field notices address other Cisco Collaboration products that are affected by this issue:
  * [FN74362: Cisco Expressway](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74362.html)
  * [FN74350: Cisco Unified Border Element (CUBE)](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html)


For more information about this issue, see the following:
  * [Public CA certificate changes impacting Dedicated Instance](https://help.webex.com/en-us/article/zo55dl/Public-CA-certificate-changes-impacting-Dedicated-Instance "Public CA certificate changes impacting Dedicated Instance")
  * [Blog: Changes to TLS clientAuth Certificates - Ensuring You’re Not Impacted](https://blogs.cisco.com/security/changes-to-tls-clientauth-certificates)
  * [Certificate EKU Changes: Actions Cisco On-premises Collaboration Customers MUST TAKE NOW](https://blog.webex.com/collaboration/certificate-eku-changes-actions-cisco-premises-collaboration-customers-must-take-now/ "Certificate EKU Changes: Actions Cisco On-premises Collaboration Customers MUST TAKE NOW")  
  


  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.2  | Added blog and article links for more details. Updated information about the dates when the Chrome Root Program Policy is scheduled to go into effect.  | Problem Description, Background, Workaround/Solution, Additional Information  | 2026-MAR-25  |  
| 1.1  | Updated information to explain that public CA servers will stop issuing Client Authentication EKU certifications from May 2026.  | Background  | 2026-FEB-03  |  
| 1.0  | Initial Release  | —  | 2026-JAN-30  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Emergency Responder 14](https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder-14/model.html)
  * [Emergency Responder 15](https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder-15/model.html)
  * [Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Unified Communications Manager IM and Presence Service 15](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-15/model.html)
  * [Unified Communications Manager IM and Presence Service Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-version-14/model.html)
  * [Unified Communications Manager Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-14/model.html)
  * [Unified Communications Manager Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-15/model.html)
  * [Unity Connection Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-14/model.html)
  * [Unity Connection Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-15/model.html)

+ Show All 9 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74345.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
