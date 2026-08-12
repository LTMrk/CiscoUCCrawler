  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Multiple Cisco Products Snort Memory Leak Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html) to Save Content 
Print
### Available Languages
Updated:October 29, 2021
Document ID:1635352141985320
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Multiple Cisco Products Snort Memory Leak Denial of Service Vulnerability
Medium
Advisory ID: 
cisco-sa-snort-dos-s2R7W9UU
First Published:
2021 October 27 16:00 GMT
Last Updated: 
2021 October 29 14:07 GMT
Version 1.1: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvt57503](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt57503)
[CSCvx29001](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx29001)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)
CVE-2021-40114
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)
CWE-770
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)
CVSS Score:
[ Base 6.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:N/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:N/A:H/E:X/RL:X/RC:X
CVE-2021-40114
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)
CWE-770
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-s2R7W9UU/csaf/cisco-sa-snort-dos-s2R7W9UU.json)
Email 
## 
Summary 
  * Multiple Cisco products are affected by a vulnerability in the way the Snort detection engine processes ICMP traffic that could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition on an affected device.
The vulnerability is due to improper memory resource management while the Snort detection engine is processing ICMP packets. An attacker could exploit this vulnerability by sending a series of ICMP packets through an affected device. A successful exploit could allow the attacker to exhaust resources on the affected device, causing the device to reload.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-s2R7W9UU>
This advisory is part of the October 2021 release of the Cisco ASA, FTD, and FMC Security Advisory Bundled publication. For a complete list of the advisories and links to them, see [Cisco Event Response: October 2021 Cisco ASA, FMC, and FTD Software Security Advisory Bundled Publication](https://sec.cloudapps.cisco.com/security/center/viewErp.x?alertId=ERP-74773).


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected all open source Snort project releases earlier than Release 2.9.18. For more information on open source Snort, see the [Snort website](https://www.snort.org/).
### Impact to Cisco Products
At the time of publication, this vulnerability affected the following Cisco products if they were running a vulnerable release of Cisco Software:
    * Firepower Threat Defense (FTD) Software - All platforms
At the time of publication, this vulnerability affected the following Cisco products if they were running a release earlier than the first fixed release of Cisco Unified Threat Defense (UTD) Snort Intrusion Prevention System (IPS) Engine for Cisco IOS XE Software or Cisco UTD Engine for Cisco IOS XE SD-WAN Software.
**Note** : UTD is not installed on these devices by default: 
    * 1000 Series Integrated Services Routers (ISRs)
    * 4000 Series Integrated Services Routers (ISRs)
    * Catalyst 8000V Edge Software
    * Catalyst 8200 Series Edge Platforms
    * Catalyst 8300 Series Edge Platforms
    * Cloud Services Routers 1000V Series
    * Integrated Services Virtual Routers (ISRv)
For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * Adaptive Security Appliance (ASA) Software
    * Catalyst 8500 Series Edge Platforms
    * Catalyst 8500L Series Edge Platforms
    * Firepower Management Center (FMC) Software
    * Meraki Security Appliances


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the release information in the following table(s) was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerability described in this advisory and which release included the fix for this vulnerability.
**Cisco FTD Software**  
| FTD Software Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 6.2.2 and earlier1  | Migrate to a fixed release.  |  
| 6.2.3  | Migrate to a fixed release.  |  
| 6.3.01  | Migrate to a fixed release.  |  
| 6.4.0  | 6.4.0.12  |  
| 6.5.01  | Migrate to a fixed release.  |  
| 6.6.0  | 6.6.3  |  
| 6.7.0  | 6.7.0.2  |  
| 7.0.0  | Not vulnerable.  |  
1. Cisco FMC and FTD Software releases 6.2.2 and earlier, as well as releases 6.3.0 and 6.5.0, have reached [end of software maintenance](https://www.cisco.com/c/en/us/products/eos-eol-listing.html). Customers are advised to migrate to a supported release that includes the fix for this vulnerability.
For instructions on upgrading your FTD device, see [Cisco Firepower Management Center Upgrade Guide](https://www.cisco.com/c/en/us/td/docs/security/firepower/upgrade/fpmc-upgrade-guide/getting_started.html).
**Cisco UTD Software**  
| UTD Software Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 16.12  | 16.12.6  |  
| 17.3  | 17.3.4a  |  
| 17.4  | 17.4.2  |  
| 17.5  | Not vulnerable.  |  
| 17.6  | Not vulnerable.  |  
| 17.7  | Not vulnerable.  |  
**Snort Software Release**  
| Snort Major Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 2.x  | 2.9.18  |  
| 3.x  | Not vulnerable.  |  
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * This vulnerability was found by Santosh Krishnamurthy of Cisco during internal security testing.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
  * [Cisco Event Response: October 2021 Cisco ASA, FMC, and FTD Software Security Advisory Bundled Publication](https://sec.cloudapps.cisco.com/security/center/viewErp.x?alertId=ERP-74773)


## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-s2R7W9UU>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.1  | Updated the Source section.  | Source  | Final  | 2021-OCT-29  |  
| 1.0  | Initial public release.  | —  | Final  | 2021-OCT-27  |  
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
  * [Cisco Event Response: October 2021 Cisco ASA, FMC, and FTD Software Security Advisory Bundled Publication](https://sec.cloudapps.cisco.com/security/center/viewErp.x?alertId=ERP-74773)


[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-s2R7W9UU.html "Back to Top")
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
