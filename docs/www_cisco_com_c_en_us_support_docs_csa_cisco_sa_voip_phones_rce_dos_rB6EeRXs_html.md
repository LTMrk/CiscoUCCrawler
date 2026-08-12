  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco IP Phones Web Server Remote Code Execution and Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html) to Save Content 
Print
### Available Languages
Updated:April 16, 2020
Document ID:1586967472212155
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco IP Phones Web Server Remote Code Execution and Denial of Service Vulnerability
Critical
Advisory ID: 
cisco-sa-voip-phones-rce-dos-rB6EeRXs
First Published:
2020 April 15 16:00 GMT
Last Updated: 
2020 April 16 15:57 GMT
Version 1.1: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCuz03016](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuz03016)
[CSCvs78272](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvs78272)
[CSCvs78441](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvs78441)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)
CVE-2020-3161
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)
CVSS Score:
[ Base 9.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:X/RL:X/RC:X
CVE-2020-3161
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voip-phones-rce-dos-rB6EeRXs/csaf/cisco-sa-voip-phones-rce-dos-rB6EeRXs.json)
Email 
## 
Summary 
  * A vulnerability in the web server for Cisco IP Phones could allow an unauthenticated, remote attacker to execute code with _root_ privileges or cause a reload of an affected IP phone, resulting in a denial of service (DoS) condition.
The vulnerability is due to a lack of proper input validation of HTTP requests. An attacker could exploit this vulnerability by sending a crafted HTTP request to the web server of a targeted device. A successful exploit could allow the attacker to remotely execute code with _root_ privileges or cause a reload of an affected IP phone, resulting in a DoS condition.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voip-phones-rce-dos-rB6EeRXs>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects the following Cisco products if they have web access enabled and are running a firmware release earlier than the first fixed release for that device:
    * IP Phone 7811, 7821, 7841, and 7861 Desktop Phones
    * IP Phone 8811, 8841, 8845, 8851, 8861, and 8865 Desktop Phones
    * Unified IP Conference Phone 8831
    * Wireless IP Phone 8821 and 8821-EX
**Note:** Web access is disabled by default. Administrators can check the web access configuration from Cisco Unified Communications Manager by choosing **Device > Phone > Select a Phone** and checking whether **Web Access** is set to _Enabled_ or _Disabled_. If it is set to _Disabled_ , the IP phone is not vulnerable.
For information about which Cisco firmware releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html#fs) section of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * ATA 190 Analog Telephone Adapter
    * ATA 191 Analog Telephone Adapter
    * ATA 192 Multiplatform Analog Telephone Adapter
    * IP Conference Phone 7832
    * IP Conference Phone 7832 with Multiplatform Firmware
    * IP Conference Phone 8832
    * IP Conference Phone 8832 with Multiplatform Firmware
    * IP DECT 6825 with Multiplatform Firmware
    * IP Phone 6821, 6841, 6851, 6861, and 6871 with Multiplatform Firmware
    * IP Phone 7811, 7821, 7841, and 7861 Desktop Phones with Multiplatform Firmware
    * IP Phone 8811, 8841, 8845, 8851, 8861, and 8865 Desktop Phones with Multiplatform Firmware
    * SPA112 2-Port Phone Adapter
    * SPA122 ATA with Router
    * SPA2102 Phone Adapter with Router
    * SPA232D Multi-Line DECT ATA
    * SPA3102 Voice Gateway with Router
    * SPA8000 8-Port IP Telephony Gateway
    * SPA8800 IP Telephony Gateway with 4 FXS and 4 FXO Ports
    * Small Business SPA300 Series IP Phones
    * Small Business SPA500 Series IP Phones
    * Unified IP Conference Phone 8831 for Third-Party Call Control
    * Unified IP Phone 6901 and 6911
    * Unified SIP Phone 3905


## 
Workarounds 
  * There are no workarounds that address this vulnerability.
However, if web access is not required, disabling it is considered a mitigation for this vulnerability. If web access is disabled, the phone is not vulnerable. For additional information, see the Web Access Disable chapter of the [Phone Hardening](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/11_0_1/secugd/CUCM_BK_C1A78C1D_00_cucm-security-guide-1101/phone_hardening.pdf) guide.
**Note:** Web access is disabled by default on Cisco IP phones.


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
Customers are advised to upgrade to an appropriate fixed firmware release as indicated in the following table:  
| Cisco IP Phone Model  | Cisco Bug ID  | First Fixed Release  |  
| --- | --- | --- |  
| IP Phone 7811, 7821, 7841, 7861 Desktop Phones  | [CSCuz03016](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuz03016)  | 11.7(1)  |  
| IP Phone 8811, 8841, 8845, 8851, 8861, 8865 Desktop Phones  | [CSCuz03016](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuz03016)  | 11.7(1)  |  
| Unified IP Conference Phone 8831   | [CSCvs78441](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvs78441)  | 10.3(1)SR6  |  
| Wireless IP Phone 8821, 8821-EX  | [CSCvs78272](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvs78272)  | 11.0(5)SR3   |  
To download the Cisco IP Phone firmware from the [Software Center](https://software.cisco.com/download/navigator.html) on [Cisco.com](https://www.cisco.com/), do the following:
    1. Click **Browse all**.
    2. Choose **Collaboration Endpoints > IP Phones**.
    3. Choose a specific product from the right pane of the product selector.
    4. Choose a release from the left pane of the product page.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is aware that proof-of-concept exploit code is available for the vulnerability described in this advisory.


## 
Source 
  * This vulnerability was found during internal security testing. Cisco would also like to thank Jacob Baines of Tenable for reporting this vulnerability.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Action Links for This Advisory 
  * [Snort Rule 53670](https://www.cisco.com/web/software/286321931/143310/sf-rules-2020-04-16-new.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voip-phones-rce-dos-rB6EeRXs>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.1  | Updated Exploitation and Public Announcements to indicate that there is public exploit code.  | Exploitation and Public Announcements  | Final  | 2020-APR-16  |  
| 1.0  | Initial public release.  | —  | Final  | 2020-APR-15  |  
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
Action Links for This Advisory 
  * [Snort Rule 53670](https://www.cisco.com/web/software/286321931/143310/sf-rules-2020-04-16-new.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-voip-phones-rce-dos-rB6EeRXs.html "Back to Top")
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
