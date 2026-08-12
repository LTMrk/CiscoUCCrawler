  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Expressway Series, Cisco TelePresence Video Communication Server, and Cisco TelePresence Conductor REST API Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html) to Save Content 
Print
### Available Languages
Updated:October 18, 2017
Document ID:1508344933610231
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://tools.cisco.com/security/center/images/cisco-alert.svg)](https://tools.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory
# Cisco Expressway Series, Cisco TelePresence Video Communication Server, and Cisco TelePresence Conductor REST API Denial of Service Vulnerability
Medium
Advisory ID: 
cisco-sa-20171018-expressway-tp-vcs
First Published:
2017 October 18 16:00 GMT
Last Updated: 
2017 October 30 19:00 GMT
Version 1.1: 
[Final](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCve77571](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve77571)
[CSCvg44278](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvg44278)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)
CVE-2017-12287
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)
CWE-399
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)
CVSS Score:
[ Base 4.3](https://tools.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L)[![](https://tools.cisco.com/security/center/images/blue-square.png)](https://tools.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L/E:X/RL:X/RC:X
CVE-2017-12287
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)
CWE-399
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html)
[ Download CVRF ](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171018-expressway-tp-vcs/cvrf/cisco-sa-20171018-expressway-tp-vcs_cvrf.xml)
Download PDF 
Email 
## 
Summary 
  * A vulnerability in the cluster database (CDB) management component of Cisco Expressway Series Software, Cisco TelePresence Video Communication Server (VCS) Software, and Cisco TelePresence Conductor Software could allow an authenticated, remote attacker to cause the CDB process on an affected system to restart unexpectedly, resulting in a temporary denial of service (DoS) condition.  
  
The vulnerability is due to incomplete input validation of URL requests by the REST API of the affected software. An attacker could exploit this vulnerability by sending a crafted URL to the REST API of the affected software on an affected system. A successful exploit could allow the attacker to cause the CDB process on the affected system to restart unexpectedly, resulting in a temporary DoS condition.  
  
There are no workarounds that address this vulnerability.  
  
This advisory is available at the following link:  
<https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171018-expressway-tp-vcs>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects Cisco Expressway Series Software, Cisco TelePresence Video Communication Server (VCS) Software, and Cisco TelePresence Conductor Software.  
  
For information about affected software releases, consult the Cisco bug ID(s) at the top of this advisory.
##  Products Confirmed Not Vulnerable 
No other Cisco products are currently known to be affected by this vulnerability.


## 
Indicators of Compromise 
  * Exploitation of this vulnerability will cause the CDB process to restart. When the process restarts, the following system alarm will be generated:  

> 
```
An unexpected software error was detected in ClusterDB: unknown reason
```

Contact the Cisco Technical Assistance Center (TAC) to determine whether the system has been compromised by exploitation of this vulnerability.


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
  * This vulnerability was found during internal security testing.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
URL 
  * <https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171018-expressway-tp-vcs>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.1  | Added Cisco TelePresence Conductor to advisory.  | Affected Products  | Final  | 2017-October-30  |  
| 1.0  | Initial public release.  | —  | Final  | 2017-October-18  |  
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


[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20171018-expressway-tp-vcs.html "Back to Top")
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
