  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Contact Center Enterprise Web-Based Management Interface Cross-Site Scripting Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html) to Save Content 
Print
### Available Languages
Updated:June 22, 2016
Document ID:1466627875335859
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://tools.cisco.com/security/center/images/cisco-alert.svg)](https://tools.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory
# Cisco Unified Contact Center Enterprise Web-Based Management Interface Cross-Site Scripting Vulnerability
Medium
Advisory ID: 
cisco-sa-20160622-ucce
First Published:
2016 June 22 13:30 GMT
Version 1.0: 
[Final](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCux59474](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCux59474)
[CSCux59650](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCux59650)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)
CVE-2016-1439
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)
CWE-79
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)
CVSS Score:
[ Base 4.3, Temporal 3.7](https://tools.cisco.com/security/center/cvssCalculator.x?version=2.0&vector=AV:N/AC:M/Au:N/C:N/I:P/A:N/E:U/RL:U/RC:C)[![](https://tools.cisco.com/security/center/images/blue-square.png)](https://tools.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
AV:N/AC:M/Au:N/C:N/I:P/A:N/E:U/RL:U/RC:C
CVE-2016-1439
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)
CWE-79
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html)
[ Download CVRF ](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20160622-ucce/cvrf/cisco-sa-20160622-ucce_cvrf.xml)
Download PDF 
Email 
## 
Summary 
  * A vulnerability in the HTTP web-based management interface of Cisco Unified Contact Center Enterprise Software could allow an unauthenticated, remote attacker to conduct a cross-site scripting (XSS) attack against a user of the web interface of an affected system.  
  
The vulnerability is due to insufficient input validation of a user-supplied value. An attacker could exploit this vulnerability by persuading a user to click a specific link.  
  
Cisco has not released software updates that address this vulnerability. Workarounds that address this vulnerability are not available.   
  
This advisory is available at the following link: <http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20160622-ucce>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects all releases of Cisco Unified Contact Center Enterprise Software.
##  Products Confirmed Not Vulnerable 
No other Cisco products are currently known to be affected by this vulnerability.


## 
Workarounds 
  * For additional information about cross-site scripting attacks and the methods used to exploit these vulnerabilities, see the Cisco Applied Mitigation Bulletin [Understanding Cross-Site Scripting (XSS) Threat Vectors](https://tools.cisco.com/security/center/content/CiscoAppliedMitigationBulletin/cisco-amb-20060922-understanding-xss).


## 
Fixed Software 
  * Cisco provides information about fixed software in Cisco bugs, which are accessible through the [Cisco Bug Search Tool](https://bst.cloudapps.cisco.com/bugsearch/bug/BUGID).  
  
When considering software upgrades, customers are advised to consult the Cisco Security Advisories and Responses archive at <http://www.cisco.com/go/psirt> and review subsequent advisories to determine exposure and a complete upgrade solution.  
  
In all cases, customers should ensure that the devices to upgrade contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
URL 
  * <http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20160622-ucce>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2016-June-22  |  
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


[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20160622-ucce.html "Back to Top")
