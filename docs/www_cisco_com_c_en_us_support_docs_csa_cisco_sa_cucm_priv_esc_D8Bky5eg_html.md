  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Communications Products Privilege Escalation Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html) to Save Content 
Print
### Available Languages
Updated:August 30, 2023
Document ID:1693412660855528
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Unified Communications Products Privilege Escalation Vulnerability
Medium
Advisory ID: 
cisco-sa-cucm-priv-esc-D8Bky5eg
First Published:
2023 August 30 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwh29940](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh29940)
[CSCwh30442](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh30442)
[CSCwh30455](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh30455)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)
CVE-2023-20266
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)
CWE-347
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)
CVSS Score:
[ Base 6.5](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N/E:X/RL:X/RC:X
CVE-2023-20266
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)
CWE-347
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-priv-esc-D8Bky5eg/csaf/cisco-sa-cucm-priv-esc-D8Bky5eg.json)
Email 
## 
Summary 
  * A vulnerability in Cisco Emergency Responder, Cisco Unified Communications Manager (Unified CM), Cisco Unified Communications Manager Session Management Edition (Unified CM SME), and Cisco Unity Connection could allow an authenticated, remote attacker to elevate privileges to _root_ on an affected device.
This vulnerability exists because the application does not properly restrict the files that are being used for upgrades. An attacker could exploit this vulnerability by providing a crafted upgrade file. A successful exploit could allow the attacker to elevate privileges to _root_. To exploit this vulnerability, the attacker must have valid platform administrator credentials on an affected device.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-priv-esc-D8Bky5eg>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected the following Cisco products:
    * Emergency Responder
    * Unified CM
    * Unified CM SME
    * Unity Connection
For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * Finesse
    * Hosted Collaboration Mediation Fulfillment (HCM-F)
    * Packaged Contact Center Enterprise (Packaged CCE)
    * Prime Collaboration Deployment
    * Prime License Manager (PLM)
    * SocialMiner
    * Unified Communications Manager IM & Presence Service (Unified CM IM&P)
    * Unified Contact Center Domain Manager (Unified CCDM)
    * Unified Contact Center Express (Unified CCX)
    * Unified Contact Center Management Portal (Unified CCMP)
    * Unified Intelligence Center
    * Virtualized Voice Browser


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the release information in the following tables was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information. Only the specific releases listed are affected by this vulnerability.   
| Cisco Emergency Responder Release   | Vulnerable Releases  | First Fixed Release  |  
| --- | --- | --- |  
| Earlier than 12.5(1)  | Not vulnerable  | Not vulnerable  |  
| 12.5(1)  | 12.5.1SU4  
12.5.1SU8a  | Apply patch file ciscocm.ADD_SIGNED_FILTER.k4.cop.sha512 or upgrade to 12.5.1SU5, 12.5.1SU6, 12.5.1SU7, or 12.5.1SU8b  |  
| 14  | 14SU3  | Apply patch file ciscocm.ADD_SIGNED_FILTER.k4.cop.sha512 or upgrade to 14SU3a  |  
| Cisco Unified CM and Unified CM SME Release  | Vulnerable Releases  | First Fixed Release  |  
| --- | --- | --- |  
| Earlier than 12.5(1)  | Not vulnerable  | Not vulnerable  |  
| 12.5(1)  | 12.5.1SU8  | Apply patch file ciscocm.ADD_SIGNED_FILTER.k4.cop.sha512 or upgrade to 12.5.1SU8a  |  
| 14  | Not vulnerable  | Not vulnerable  |  
| Cisco Unity Connection Release  | Vulnerable Releases  | First Fixed Release  |  
| --- | --- | --- |  
| Earlier than 12.5(1)  | Not vulnerable  | Not vulnerable  |  
| 12.5(1)  | 12.5.1SU6   
12.5.1SU7  
12.5.1SU8  | Apply patch file ciscocm.ADD_SIGNED_FILTER.k4.cop.sha512 or upgrade to 12.5.1SU8a  |  
| 14  | 14SU2  
14SU3  | Apply patch file ciscocm.ADD_SIGNED_FILTER.k4.cop.sha512 or upgrade to 14SU3a  |  
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * This vulnerability was found during internal security testing.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-priv-esc-D8Bky5eg>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2023-AUG-30  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-priv-esc-D8Bky5eg.html "Back to Top")
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
