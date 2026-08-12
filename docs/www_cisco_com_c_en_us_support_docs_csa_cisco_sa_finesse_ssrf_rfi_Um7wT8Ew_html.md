  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Finesse Web-Based Management Interface Vulnerabilities
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html) to Save Content 
Print
### Available Languages
Updated:June 14, 2024
Document ID:1717604013798680
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Finesse Web-Based Management Interface Vulnerabilities
Medium
Advisory ID: 
cisco-sa-finesse-ssrf-rfi-Um7wT8Ew
First Published:
2024 June 5 16:00 GMT
Last Updated: 
2024 June 14 21:44 GMT
Version 1.2: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwh95276](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh95276)
[CSCwh95292](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh95292)
[CSCwk36966](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk36966)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)
CVE-2024-20404
CVE-2024-20405
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)
CWE-20
CWE-918
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)
CVSS Score:
[ Base 7.2](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N/E:X/RL:X/RC:X
CVE-2024-20404
CVE-2024-20405
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)
CWE-20
CWE-918
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew/csaf/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.json)
Email 
## 
Summary 
  * Multiple vulnerabilities in the web-based management interface of Cisco Finesse could allow an unauthenticated, remote attacker to perform a stored cross site-scripting (XSS) attack by exploiting a remote file inclusion (RFI) vulnerability or perform a server-side request forgery (SSRF) attack an affected system.
For more information about these vulnerabilities, see the [Details](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html#details) section of this advisory. 
Cisco has released software updates that address these vulnerabilities. There are no workarounds that address these vulnerabilities.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, these vulnerabilities affected Cisco Finesse in the default configuration.
The following Cisco products that may be bundled with Cisco Finesse are also affected by these vulnerabilities:
    * Packaged Contact Center Enterprise (Packaged CCE)
    * Unified Contact Center Enterprise (Unified CCE)
    * Unified Contact Center Express (Unified CCX)
    * Unified Intelligence Center
For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html#vp) section of this advisory are known to be affected by these vulnerabilities.


## 
Details 
  * The vulnerabilities are not dependent on one another. Exploitation of one of the vulnerabilities is not required to exploit the other vulnerability. In addition, a software release that is affected by one of the vulnerabilities may not be affected by the other vulnerability.
Details about the vulnerabilities are as follows:
**CVE-2024-20404: Cisco Finesse SSRF Vulnerability**
A vulnerability in the web-based management interface of Cisco Finesse could allow an unauthenticated, remote attacker to conduct an SSRF attack on an affected system.
This vulnerability is due to insufficient validation of user-supplied input for specific HTTP requests that are sent to an affected system. An attacker could exploit this vulnerability by sending a crafted HTTP request to the affected device. A successful exploit could allow the attacker to obtain limited sensitive information for services that are associated to the affected device.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
**Note:** The Security Impact Rating (SIR) is Medium due to the limited scope of information that is accessible to the attacker.
Bug ID(s): [CSCwh95292](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh95292), [CSCwk36966](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk36966)  
CVE ID: CVE-2024-20404  
Severity Impact Rating (SIR): Medium  
CVSS Base Score: 7.2  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N
**CVE-2024-20405: Cisco Finesse Stored XSS through RFI Vulnerability**
A vulnerability in the web-based management interface of Cisco Finesse could allow an unauthenticated, remote attacker to conduct a stored XSS attack by exploiting an RFI vulnerability. 
This vulnerability is due to insufficient validation of user-supplied input for specific HTTP requests that are sent to an affected device. An attacker could exploit this vulnerability by persuading a user to click a crafted link. A successful exploit could allow the attacker to execute arbitrary script code in the context of the affected interface or access sensitive information on the affected device.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
Bug ID(s): [CSCwh95276](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh95276), [CSCwk36966](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk36966)  
CVE ID: CVE-2024-20405  
Severity Impact Rating (SIR): Medium  
CVSS Base Score: 4.8  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:L/I:L/A:N


## 
Workarounds 
  * There are no workarounds that address these vulnerabilities.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the release information in the following tables was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerabilities that are described in this advisory and which release included the fix for these vulnerabilities.  
| Cisco Finesse Release  | First Fixed Release  |  
| --- | --- |  
| 11.6(1) ES11 and earlier  | Migrate to a fixed release.   |  
| 12.6(2) ES01 and earlier  | 12.6(2) ES03  |  
| Cisco Unified Contact Center Express Release  | First Fixed Release  |  
| --- | --- |  
| 12.0 and earlier  | Migrate to a fixed release.  |  
| 12.5(1) SU3 ES05 and earlier  | 12.5(1) SU3 ES06 (future release)  |  
**Note:** Cisco Packaged Contact Center Enterprise, Unified Contact Center Enterprise, and Unified Intelligence Center are upgraded autonomously.
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerabilities that are described in this advisory.


## 
Source 
  * Cisco would like to thank Abd El Rahman Ezzat for reporting these vulnerabilities.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
  * [Cross-Site Scripting](https://owasp.org/www-community/attacks/xss/)


## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.2  | Added CSCwk36966 to Details and Fixed Release sections and updated fixed release information.  | Header, Details, Fixed Releases  | Final  | 2024-JUN-14  |  
| 1.1  | Updated the source name.  | Source  | Final  | 2024-JUN-06  |  
| 1.0  | Initial public release.  | —  | Final  | 2024-JUN-05  |  
Show Complete History...


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
  * [Cross-Site Scripting](https://owasp.org/www-community/attacks/xss/)


[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-finesse-ssrf-rfi-Um7wT8Ew.html "Back to Top")
