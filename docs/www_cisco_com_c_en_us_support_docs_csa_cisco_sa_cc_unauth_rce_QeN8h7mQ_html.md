  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Contact Center Express Remote Code Execution Vulnerabilities
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html) to Save Content 
Print
### Available Languages
Updated:November 13, 2025
Document ID:1762358979012183
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Unified Contact Center Express Remote Code Execution Vulnerabilities
Critical
Advisory ID: 
cisco-sa-cc-unauth-rce-QeN8h7mQ
First Published:
2025 November 5 16:00 GMT
Last Updated: 
2025 November 13 12:48 GMT
Version 1.1: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwq36528](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq36528)
[CSCwq36573](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq36573)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)
CVE-2025-20354
CVE-2025-20358
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)
CWE-306
CWE-434
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)
CVSS Score:
[ Base 9.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:X/RL:X/RC:X
CVE-2025-20354
CVE-2025-20358
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)
CWE-306
CWE-434
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cc-unauth-rce-QeN8h7mQ/csaf/cisco-sa-cc-unauth-rce-QeN8h7mQ.json)
Email 
## 
Summary 
  * Multiple vulnerabilities in the Java Remote Method Invocation (RMI) process of Cisco Unified Contact Center Express (Unified CCX) could allow an unauthenticated, remote attacker to upload arbitrary files, bypass authentication, execute arbitrary commands, and elevate privileges to _root_.
For more information about these vulnerabilities, see the [Details](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html#details) section of this advisory.
Cisco has released software updates that address these vulnerabilities. There are no workarounds that address these vulnerabilities.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cc-unauth-rce-QeN8h7mQ>


## 
Affected Products 
  * ##  Vulnerable Products 
These vulnerabilities affect Cisco Unified CCX, regardless of device configuration.
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html#fs) section of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html#vp) section of this advisory are known to be affected by these vulnerabilities.
Cisco has confirmed that these vulnerabilities do not affect the following Cisco products:
    * Packaged Contact Center Enterprise (Packaged CCE)
    * Unified Contact Center Enterprise (Unified CCE)


## 
Details 
  * The vulnerabilities are not dependent on one another. Exploitation of one of the vulnerabilities is not required to exploit the other vulnerability.
Details about the vulnerabilities are as follows:
**CVE-2025-20354: Cisco Unified CCX Remote Code Execution Vulnerability**
A vulnerability in the Java Remote Method Invocation (RMI) process of Cisco Unified CCX could allow an unauthenticated, remote attacker to upload arbitrary files and execute arbitrary commands with _root_ permissions on an affected system.
This vulnerability is due to improper authentication mechanisms that are associated to specific Cisco Unified CCX features. An attacker could exploit this vulnerability by uploading a crafted file to an affected system through the Java RMI process. A successful exploit could allow the attacker to execute arbitrary commands on the underlying operating system and elevate privileges to _root_.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
Bug ID(s): [CSCwq36528](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq36528)  
CVE ID: CVE-2025-20354  
Security Impact Rating (SIR): Critical  
CVSS Base Score: 9.8  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
**CVE-2025-20358: Cisco Unified CCX Editor Authentication Bypass Vulnerability**
A vulnerability in the Contact Center Express (CCX) Editor application of Cisco Unified CCX could allow an unauthenticated, remote attacker to bypass authentication and obtain administrative permissions pertaining to script creation and execution.
This vulnerability is due to improper authentication mechanisms in the communication between the CCX Editor and an affected Unified CCX server. An attacker could exploit this vulnerability by redirecting the authentication flow to a malicious server and tricking the CCX Editor into believing the authentication was successful. A successful exploit could allow the attacker to create and execute arbitrary scripts on the underlying operating system of an affected Unified CCX server, as an internal non-_root_ user account.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
Bug ID(s): [CSCwq36573](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq36573)  
CVE ID: CVE-2025-20358  
Security Impact Rating (SIR): Critical  
CVSS Base Score: 9.4  
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L


## 
Workarounds 
  * There are no workarounds that address these vulnerabilities.


## 
Fixed Software 
  * Cisco considers any workarounds and mitigations to be temporary solutions until an upgrade to a fixed software release is available. To fully remediate these vulnerabilities and avoid future exposure as described in this advisory, Cisco strongly recommends that customers upgrade to the fixed software indicated in this advisory.
### Fixed Releases
In the following table, the left column lists Cisco software releases. The right column indicates whether a release is affected by the vulnerabilities that are described in this advisory and the first release that includes the fix for these vulnerabilities. Customers are advised to upgrade to an appropriate [fixed software release](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) as indicated in this section.  
| Cisco Unified CCX Release  | First Fixed Release  |  
| --- | --- |  
| 12.5 SU3 and earlier  | 12.5 SU3 ES07  |  
| 15.0  | 15.0 ES01  |  
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerabilities that are described in this advisory.


## 
Source 
  * Cisco would like to thank the security researcher Jahmel Harris of NATO Cyber Security Centre (NCSC) for reporting these vulnerabilities.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cc-unauth-rce-QeN8h7mQ>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.1  | Updated affiliation of researcher.  | Source  | Final  | 2025-NOV-13  |  
| 1.0  | Initial public release.  | —  | Final  | 2025-NOV-05  |  
Show Less


* * *
## 
Legal Disclaimer 
  * ### SOFTWARE DOWNLOADS AND TECHNICAL SUPPORT
The [Cisco Support and Downloads](https://www.cisco.com/c/en/us/support/index.html) page on Cisco.com provides information about licensing and downloads. This page can also display customer device support coverage for customers who use the My Devices tool. Please note that customers may download only software that was procured from Cisco directly or through a Cisco authorized reseller or partner and for which the license is still valid.
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html). Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult [the advisories](https://www.cisco.com/go/psirt) for the relevant Cisco products to determine exposure and a complete upgrade solution. In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) or their contracted maintenance providers.
### LEGAL DISCLAIMER DETAILS
CISCO DOES NOT MAKE ANY EXPRESS OR IMPLIED GUARANTEES OR WARRANTIES OF ANY KIND, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. WITHOUT LIMITING THE GENERALITY OF THE FOREGOING, CISCO DOES NOT GUARANTEE THE ACCURACY OR COMPLETENESS OF THIS INFORMATION. THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
Copies or summaries of the information contained in this Security Advisory may lack important information or contain factual errors. Customers are advised to visit the [Cisco Security Advisories](https://www.cisco.com/go/psirt) page for the most recent version of this Security Advisory. The Cisco Product Security Incident Response Team (PSIRT) assesses only the affected and fixed release information that is documented in this advisory. See the [Cisco Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) for more information.


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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cc-unauth-rce-QeN8h7mQ.html "Back to Top")
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
