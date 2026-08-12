  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Communications Products Remote Code Execution Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html) to Save Content 
Print
### Available Languages
Updated:April 7, 2021
Document ID:1617813172187176
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Unified Communications Products Remote Code Execution Vulnerability
High
Advisory ID: 
cisco-sa-cucm-rce-pqVYwyb
First Published:
2021 April 7 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvu56491](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu56491)
[CSCvv35203](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv35203)
[CSCvv41616](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv41616)
[ More... ](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html) ,[CSCvu56491](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu56491),[CSCvv35203](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv35203),[CSCvv41616](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv41616),[CSCvv59434](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv59434)
CVE-2021-1362
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)
CWE-94
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)
CVSS Score:
[ Base 8.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:X/RL:X/RC:X
CVE-2021-1362
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)
CWE-94
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-rce-pqVYwyb/csaf/cisco-sa-cucm-rce-pqVYwyb.json)
Email 
## 
Summary 
  * A vulnerability in the SOAP API endpoint of Cisco Unified Communications Manager, Cisco Unified Communications Manager Session Management Edition, Cisco Unified Communications Manager IM & Presence Service, Cisco Unity Connection, and Cisco Prime License Manager could allow an authenticated, remote attacker to execute arbitrary code on an affected device.
This vulnerability is due to improper sanitization of user-supplied input. An attacker could exploit this vulnerability by sending a SOAP API request with crafted parameters to an affected device. A successful exploit could allow the attacker to execute arbitrary code with _root_ privileges on the underlying Linux operating system of the affected device.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-rce-pqVYwyb>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects the following Cisco products if they are running a vulnerable software release:
    * Unified Communications Manager (Unified CM)
    * Unified Communications Manager Session Management Edition (Unified CM SME)
    * Unified Communications Manager IM & Presence Service (Unified CM IM&P)
    * Unity Connection
    * Prime License Manager
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html#fs) section of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect Cisco Emergency Responder.


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * Cisco has released free software updates that address the vulnerability described in this advisory. Customers may only install and expect support for software versions and feature sets for which they have purchased a license. By installing, downloading, accessing, or otherwise using such software upgrades, customers agree to follow the terms of the Cisco software license:  
<https://www.cisco.com/c/en/us/products/end-user-license-agreement.html>
Additionally, customers may only download software for which they have a valid license, procured from Cisco directly, or through a Cisco authorized reseller or partner. In most cases this will be a maintenance upgrade to software that was previously purchased. Free security software updates do not entitle customers to a new software license, additional software feature sets, or major revision upgrades.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Customers Without Service Contracts
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the Cisco TAC: <https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html>
Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
### Fixed Releases
In the following tables, the left column lists Cisco software releases. The right column indicates whether a release is affected by the vulnerability described in this advisory and the first release that includes the fix for this vulnerability. Customers are advised to upgrade to an appropriate fixed software release as indicated in this section.
**Unified CM and Unified CM SME:**[**CSCvu56491**](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu56491)  
| Cisco Unified CM and Unified CM SME Releases  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 10.5(2)  | None planned  |  
| 11.0(1)  | Migrate to 11.5(1)SU9  |  
| 11.5(1)  | 11.5(1)SU9  |  
| 12.0(1)  | Migrate to 12.5(1)SU4  |  
| 12.5(1)  | 12.5(1)SU4  |  
**Unified CM IM &P: **[**CSCvv41616**](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv41616)  
| Cisco Unified CM IM&P Releases  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 10.5(2)  | None planned  |  
| 11.0(1)  | Migrate to 11.5(1)SU9  |  
| 11.5(1)  | 11.5(1)SU9  |  
| 12.0(1)  | Migrate to 12.5(1)SU4  |  
| 12.5(1)  | 12.5(1)SU4  |  
**Unity Connection:**[**CSCvv35203**](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv35203)  
| Cisco Unity Connection Releases  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 10.5(2)  | None planned  |  
| 11.0(1)  | Migrate to 11.5(1)SU9  |  
| 11.5(1)  | 11.5(1)SU9  |  
| 12.0(1)  | Migrate to 12.5(1)SU4  |  
| 12.5(1)  | 12.5(1)SU4  |  
**Prime License Manager:**[**CSCvv59434**](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv59434)  
| Cisco Prime License Manager Releases  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 10.5(2)  | None planned  |  
| 11.0(1)  | Migrate to 11.5(1)SU9  |  
| 11.5(1)  | 11.5(1)SU9  |  


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * Cisco would like to thank Christopher Schneider of State Farm Information Security for reporting this vulnerability.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-rce-pqVYwyb>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2021-APR-07  |  
Show Less


* * *
## 
Legal Disclaimer 
  * THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
A standalone copy or paraphrase of the text of this document that omits the distribution URL is an uncontrolled copy and may lack important information or contain factual errors. The information in this document is intended for end users of Cisco products.


## 
Feedback 
  * [Leave additional feedback](javascript:openNewWindow\(\);)


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-rce-pqVYwyb.html "Back to Top")
