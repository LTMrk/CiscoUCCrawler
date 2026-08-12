  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Communications Manager IM&P Service, Cisco TelePresence VCS, and Cisco Expressway Series Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html) to Save Content 
Print
### Available Languages
Updated:June 5, 2019
Document ID:1559752642583706
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Unified Communications Manager IM&P Service, Cisco TelePresence VCS, and Cisco Expressway Series Denial of Service Vulnerability
High
Advisory ID: 
cisco-sa-20190605-cucm-imp-dos
First Published:
2019 June 5 16:00 GMT
Last Updated: 
2019 June 24 13:49 GMT
Version 1.1: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvn00361](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvn00361)
[CSCvp51956](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvp51956)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)
CVE-2019-1845
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)
CVSS Score:
[ Base 8.6](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:H/E:X/RL:X/RC:X
CVE-2019-1845
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20190605-cucm-imp-dos/csaf/cisco-sa-20190605-cucm-imp-dos.json)
Email 
## 
Summary 
  * A vulnerability in the authentication service of the Cisco Unified Communications Manager IM and Presence (Unified CM IM&P) Service, Cisco TelePresence Video Communication Server (VCS), and Cisco Expressway Series could allow an unauthenticated, remote attacker to cause a service outage for users attempting to authenticate, resulting in a denial of service (DoS) condition.
The vulnerability is due to insufficient controls for specific memory operations. An attacker could exploit this vulnerability by sending a malformed Extensible Messaging and Presence Protocol (XMPP) authentication request to an affected system. A successful exploit could allow the attacker to cause an unexpected restart of the authentication service, preventing users from successfully authenticating. Exploitation of this vulnerability does not impact users who were authenticated prior to an attack.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20190605-cucm-imp-dos>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects the Cisco following products if they are running a vulnerable release:
    * Expressway Series configured for Mobile and Remote Access with IM&P Service (Releases X8.1 to X12.5.2)
    * TelePresence VCS configured for Mobile and Remote Access with IM&P Service (Releases X8.1 to X12.5.2)
    * Unified Communications Manager IM&P Service (multiple releases)
For information about which releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html#fs) section of this advisory.
To determine whether Mobile and Remote Access with IM&P Service is configured on Cisco Expressway Series or Cisco TelePresence VCS, administrators can log in to the web-based management interface, choose **Status > Unified Communications Status**, and check the value of the **IM and Presence Service** entry. A product is vulnerable if the **IM and Presence Service** entry is present and its value is **Configured**.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect Cisco WebEx Messenger.


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * Cisco has released free software updates that address the vulnerability described in this advisory. Customers may only install and expect support for software versions and feature sets for which they have purchased a license. By installing, downloading, accessing, or otherwise using such software upgrades, customers agree to follow the terms of the Cisco software license:   
<https://www.cisco.com/c/en/us/products/end-user-license-agreement.html>
Additionally, customers may only download software for which they have a valid license, procured from Cisco directly, or through a Cisco authorized reseller or partner. In most cases this will be a maintenance upgrade to software that was previously purchased. Free security software updates do not entitle customers to a new software license, additional software feature sets, or major revision upgrades.
When considering software upgrades, customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories and Alerts page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Customers Without Service Contracts
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the Cisco TAC:  
<https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html>
Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
### Fixed Releases
For Cisco Expressway Series and Cisco TelePresence VCS, Cisco fixed this vulnerability in Releases X12.5.3 and later.
For Cisco Unified Communications Manager IM&P, customers are advised to upgrade to an appropriate [fixed software release](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) as indicated in the following table:   
|  Cisco Unified CM IM&P Service Major Release  | First Fixed Release  |  
| --- | --- |  
|  10.5(2) and previous releases  
 |  11.5(1) SU6 or 12.5(1)  |  
|  11.0(1)  |  11.5(1) SU6  
 |  
|  11.5(1)  |  11.5(1) SU6  
 |  
|  12.0(1)  |  12.5(1)  
 |  
|  12.5(1)  |  Not vulnerable  
 |  


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory. 


## 
Source 
  * This vulnerability was found during internal security testing. 


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Action Links for This Advisory 
  * [Snort Rule 50320](https://www.cisco.com/web/software/286321931/143310/sf-rules-2019-06-06-new.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20190605-cucm-imp-dos>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.1  | Updated the list of Vulnerable Software Releases and related fixes.  | Fixed Software  | Final  | 2019-June-24  |  
| 1.0  | Initial public release.  | —  | Final  | 2019-June-05  |  
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
  * [Snort Rule 50320](https://www.cisco.com/web/software/286321931/143310/sf-rules-2019-06-06-new.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190605-cucm-imp-dos.html "Back to Top")
