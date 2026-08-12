  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Communications Products Command Injection Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html) to Save Content 
Print
### Available Languages
Updated:June 4, 2025
Document ID:1749052824106167
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Unified Communications Products Command Injection Vulnerability
Medium
Advisory ID: 
cisco-sa-vos-command-inject-65s2UCYy
First Published:
2025 June 4 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwk24029](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk24029)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)
CVE-2025-20278
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)
CWE-77
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)
CVSS Score:
[ Base 6.0](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N/E:X/RL:X/RC:X
CVE-2025-20278
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)
CWE-77
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vos-command-inject-65s2UCYy/csaf/cisco-sa-vos-command-inject-65s2UCYy.json)
Email 
## 
Summary 
  * A vulnerability in the CLI of multiple Cisco Unified Communications products could allow an authenticated, local attacker to execute arbitrary commands on the underlying operating system of an affected device as the _root_ user.
This vulnerability is due to improper validation of user-supplied command arguments. An attacker could exploit this vulnerability by executing crafted commands on the CLI of an affected device. A successful exploit could allow the attacker to execute arbitrary commands on the underlying operating system of an affected device as the _root_ user. To exploit this vulnerability, the attacker must have valid administrative credentials.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vos-command-inject-65s2UCYy>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected the following Cisco products if they were running a vulnerable software release:
    * Customer Collaboration Platform (CCP)
    * Finesse
    * Unified Communications Manager (Unified CM)
    * Unified Communications Manager IM & Presence Service (Unified CM IM&P)
    * Unified Communications Manager Session Management Edition (Unified CM SME)
    * Unified Contact Center Express (Unified CCX)
    * Unified Intelligence Center
    * Unity Connection
    * Virtualized Voice Browser
For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html#vp) section of this advisory are known to be affected by this vulnerability.


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the release information in the following tables was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerability that is described in this advisory and which release included the fix for this vulnerability.  
| Cisco CCP Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 15.0  | Migrate to a fixed release.  |  
| 15.0  | 15.0(1)  |  
| Cisco Finesse Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 12.6  | Migrate to a fixed release.  |  
| 12.6  | 12.6(2)ES6  |  
| 15.0  | 15.0(1)  |  
| Cisco Unified CM and Unified CM SME Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 15.0  | Migrate to a fixed release.  |  
| 15.0  | 15SU2  |  
| Cisco Unified CM IM&P Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 15.0  | Migrate to a fixed release.  |  
| 15.0  | 15SU2  |  
| Cisco Unified CCX Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 15.0  | Migrate to a fixed release.  |  
| 15.0  | 15.0(1)  |  
| Cisco Unified Intelligence Center Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 12.6  | Migrate to a fixed release.  |  
| 12.6  | 12.6(2)ES04  |  
| 15.0  | 15.0(1)  |  
| Cisco Unity Connection Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 15.0  | Migrate to a fixed release.  |  
| 15.0  | 15SU2  |  
| Cisco Virtualized Voice Browser Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 12.6  | Migrate to a fixed release.  |  
| 12.6  | 12.6(2)ES06  |  
| 15.0  | 15.0(1)  |  
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * Cisco would like to thank Antonin B., Jean-Michel Huguet, and Jorge Escabias from NATO Cyber Security Centre (NCSC) for reporting this vulnerability.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vos-command-inject-65s2UCYy>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2025-JUN-04  |  
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
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vos-command-inject-65s2UCYy.html "Back to Top")
