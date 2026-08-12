  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Meeting Server Session Fixation Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html) to Save Content 
Print
### Available Languages
Updated:June 20, 2018
Document ID:1529512508087618
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://tools.cisco.com/security/center/images/cisco-alert.svg)](https://tools.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory
# Cisco Meeting Server Session Fixation Vulnerability
Medium
Advisory ID: 
cisco-sa-20180620-cms-sf
First Published:
2018 June 20 16:00 GMT
Version 1.0: 
[Final](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvi23787](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvi23787)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)
CVE-2018-0359
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)
CWE-384
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)
CVSS Score:
[ Base 4.0](https://tools.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)[![](https://tools.cisco.com/security/center/images/blue-square.png)](https://tools.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N/E:X/RL:X/RC:X
CVE-2018-0359
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)
CWE-384
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html)
[ Download CVRF ](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180620-cms-sf/cvrf/cisco-sa-20180620-cms-sf_cvrf.xml)
Download PDF 
Email 
## 
Summary 
  * A vulnerability in the session identification management functionality of the web-based management interface for Cisco Meeting Server could allow an unauthenticated, local attacker to hijack a valid user session identifier.
The vulnerability exists because the affected application does not assign a new session identifier to a user session when a user authenticates to the application. An attacker could exploit this vulnerability by using a hijacked session identifier to connect to the application through the web-based management interface. A successful exploit could allow the attacker to hijack an authenticated user's browser session.
There are no workarounds that address this vulnerability.  
  
This advisory is available at the following link:  
<https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180620-cms-sf>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects Cisco Meeting Server. For information about affected software releases, consult the Cisco bug ID(s) at the top of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html#vp) section of this advisory are known to be affected by this vulnerability.
No other Cisco products are currently known to be affected by this vulnerability.


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * For information about fixed software releases, consult the Cisco bug ID(s) at the top of this advisory.
When considering software upgrades, customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories and Alerts page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory. 


## 
Source 
  * This vulnerability was found during the resolution of a Cisco TAC support case.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
URL 
  * <https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180620-cms-sf>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2018-June-20  |  
Show Less


* * *
## 
Legal Disclaimer 
  * THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
A standalone copy or paraphrase of the text of this document that omits the distribution URL is an uncontrolled copy and may lack important information or contain factual errors. The information in this document is intended for end users of Cisco products.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180620-cms-sf.html "Back to Top")
