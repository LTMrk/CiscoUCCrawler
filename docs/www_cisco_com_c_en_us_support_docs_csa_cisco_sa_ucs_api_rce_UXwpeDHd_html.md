  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Integrated Management Controller Multiple Remote Code Execution Vulnerabilities
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html) to Save Content 
Print
### Available Languages
Updated:November 18, 2020
Document ID:1605716445280787
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Integrated Management Controller Multiple Remote Code Execution Vulnerabilities
Critical
Advisory ID: 
cisco-sa-ucs-api-rce-UXwpeDHd
First Published:
2020 November 18 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvu21215](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu21215)
[CSCvu21222](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu21222)
[CSCvu22429](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu22429)
[ More... ](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html) ,[CSCvu21215](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu21215),[CSCvu21222](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu21222),[CSCvu22429](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu22429),[CSCvu80203](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu80203)
CVE-2020-3470
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)
CWE-119
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)
CVSS Score:
[ Base 9.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:X/RL:X/RC:X
CVE-2020-3470
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)
CWE-119
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-api-rce-UXwpeDHd/csaf/cisco-sa-ucs-api-rce-UXwpeDHd.json)
Email 
## 
Summary 
  * Multiple vulnerabilities in the API subsystem of Cisco Integrated Management Controller (IMC) could allow an unauthenticated, remote attacker to execute arbitrary code with _root_ privileges.
The vulnerabilities are due to improper boundary checks for certain user-supplied input. An attacker could exploit these vulnerabilities by sending a crafted HTTP request to the API subsystem of an affected system. When this request is processed, an exploitable buffer overflow condition may occur. A successful exploit could allow the attacker to execute arbitrary code with _root_ privileges on the underlying operating system (OS).
Cisco has released software updates that address these vulnerabilities. There are no workarounds that address these vulnerabilities.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-api-rce-UXwpeDHd>


## 
Affected Products 
  * ##  Vulnerable Products 
These vulnerabilities affect the following Cisco products if they are running a vulnerable release of Cisco IMC:
    * 5000 Series Enterprise Network Compute System (ENCS) Platforms
    * UCS C-Series Rack Servers in standalone mode
    * UCS E-Series Servers
    * UCS S-Series Servers in standalone mode
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html#fs) section of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html#vp) section of this advisory are known to be affected by these vulnerabilities.
Cisco has confirmed that these vulnerabilities do not affect Cisco UCS B-Series Servers, or Cisco FI-Attached C-Series and S-Series Servers managed by Cisco UCS Manager.


## 
Workarounds 
  * There are no workarounds to address this vulnerability.
However, administrators can disable the Cisco IMC web-management interface to mitigate the impact of these vulnerabilities. For example, the following commands show how to perform the configuration change on a UCS C-Series Server:
> 
```
xxxxxx-bmc# **scope http** 
xxxxxx-bmc /http # 
xxxxxx-bmc /http # **set enabled no**
SSH is in enabled state. Disabling HTTP service
Warning: setting "enabled" to "no" will disconnect all 
 existing http connections and will disable login via WebUI.
xxxxxx-bmc /http *# **commit**
xxxxxx-bmc /http # show detail
HTTP Settings:
    HTTP Port: 80
    HTTPS Port: 443
    Timeout: 1800
    Max Sessions: 4
    Active Sessions: 0
    Enabled: **no**
    HTTP Redirected: yes
xxxxxx-bmc /http # exit
```



## 
Fixed Software 
  * Cisco has released free software updates that address the vulnerability described in this advisory. Customers may only install and expect support for software versions and feature sets for which they have purchased a license. By installing, downloading, accessing, or otherwise using such software upgrades, customers agree to follow the terms of the Cisco software license: <https://www.cisco.com/c/en/us/products/end-user-license-agreement.html>
Additionally, customers may only download software for which they have a valid license, procured from Cisco directly, or through a Cisco authorized reseller or partner. In most cases this will be a maintenance upgrade to software that was previously purchased. Free security software updates do not entitle customers to a new software license, additional software feature sets, or major revision upgrades.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories and Alerts page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Customers Without Service Contracts
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the Cisco TAC: <https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html>
Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
### Fixed Releases
Customers are advised to upgrade to an appropriate release as indicated in the following tables:
**Cisco UCS C-Series Rack Servers**  
| M3 Servers  | Affected Firmware Release  | First Fixed Firmware Release  |  
| --- | --- | --- |  
| 3.0  | 3.0(1c) to 3.0(4q)  | 3.0(4r)  |  
| M4 Servers  | Affected Firmware Release  | First Fixed Firmware Release  |  
| --- | --- | --- |  
| 3.0  | 3.0(1c) to 3.0(4q)  | 3.0(4r)  |  
| 4.0  | 4.0(1a) to 4.0(2l)  | 4.0(2n)  |  
| 4.1  | 4.1(1c) to 4.1(1f)  | 4.1(1g)  |  
| M5 Servers  | Affected Firmware Release  | First Fixed Firmware Release  |  
| --- | --- | --- |  
| 3.1  | All releases  | Migrate to a fixed release.  |  
| 4.0  | 4.0(1a) to 4.0(4l)  | 4.0(4m)  |  
| 4.1  | 4.1(1c) to 4.1(1f)  | 4.1(1g)  |  
**Cisco UCS E-Series** _  
_
Cisco fixed these vulnerabilities in Cisco IMC for E-Series Servers releases 3.2.11.3 and later.
**Cisco UCS S-Series _  
_**  
| Server - S3160  | Affected Firmware Release  | First Fixed Firmware Release  |  
| --- | --- | --- |  
| 3.0  | 3.0(1c) to 3.0(4q)  | 3.0(4r)  |  
| Server - S3260  | Affected Firmware Release  | First Fixed Firmware Release  |  
| --- | --- | --- |  
| 3.1  | All releases  | Migrate to a fixed release.  |  
| 4.0  | 4.0(1a) to 4.0(4l)  | 4.0(4m)  |  
| 4.1  | 4.1(1c) to 4.1(1f)  | 4.1(1g)  |  
**Cisco 5000 Series ENCS Platforms** _  
_
Cisco fixed these vulnerabilities in Cisco Enterprise NFV Infrastructure Software (NFVIS) for Cisco 5000 Series ENCS Platforms releases 4.4.1 and later.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerabilities that are described in this advisory.


## 
Source 
  * Cisco would like to thank Nikita Abramov of Positive Technologies for reporting these vulnerabilities.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-api-rce-UXwpeDHd>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2020-NOV-18  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-api-rce-UXwpeDHd.html "Back to Top")
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
