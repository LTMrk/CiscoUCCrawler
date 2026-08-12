  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco IP Phone 8800 Series Cross-Site Request Forgery Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html) to Save Content 
Print
### Available Languages
Updated:March 20, 2019
Document ID:1553100138405593
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco IP Phone 8800 Series Cross-Site Request Forgery Vulnerability
High
Advisory ID: 
cisco-sa-20190320-ip-phone-csrf
First Published:
2019 March 20 16:00 GMT
Last Updated: 
2019 March 22 19:30 GMT
Version 1.1: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvn56221](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvn56221)
[CSCvo57629](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvo57629)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)
CVE-2019-1764
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)
CWE-352
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)
CVSS Score:
[ Base 8.1](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:H/E:X/RL:X/RC:X
CVE-2019-1764
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)
CWE-352
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20190320-ip-phone-csrf/csaf/cisco-sa-20190320-ip-phone-csrf.json)
Email 
## 
Summary 
  * A vulnerability in the web-based management interface of Session Initiation Protocol (SIP) Software for Cisco IP Phone 8800 Series could allow an unauthenticated, remote attacker to conduct a cross-site request forgery (CSRF) attack. 
The vulnerability is due to insufficient CSRF protections for the web-based management interface of an affected device. An attacker could exploit this vulnerability by persuading an authenticated user of the interface to follow a crafted link. A successful exploit could allow the attacker to perform arbitrary actions on a targeted device via a web browser and with the privileges of the user.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.  
  
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20190320-ip-phone-csrf>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects Cisco IP Phone Series products running SIP Software prior to the following releases and with the web service feature enabled:
    * 11.0(5) for Wireless IP Phone 8821 and 8821-EX
    * 12.5(1)SR1 for the IP Conference Phone 8832 and the rest of the IP Phone 8800 Series
**Note:** The web service feature is disabled in SIP Software by default.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that IP phones running Multiplatform Firmware are not affected by this vulnerability. 
Cisco has confirmed that the following IP phones are not affected by this vulnerability:
    * Cisco IP Phone 7800 Series
    * Cisco IP Conference Phone 8831
    * Cisco IP Conference Phone 7832


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
Cisco fixed this vulnerability in the following SIP Software releases:
    * 11.0(5) (future release) for Cisco Wireless IP Phone 8821 and 8821-EX
    * 12.5(1)SR1 for the IP Conference Phone 8832 and the rest of the IP Phone 8800 Series
Customers can download the SIP Software from the [Software Center](https://software.cisco.com/download/home) on Cisco.com by doing the following:
    1. Click **Browse all**.
    2. Choose **Collaboration Endpoints > IP Phones > IP Phone 8800 Series > [Model] > Session Initiation Protocol (SIP) Software**.
    3. Access releases by using the left pane of the Session Initiation Protocol (SIP) Software page.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory. 


## 
Source 
  * Cisco would like to thank David Gullasch of modzero AG for reporting this vulnerability.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20190320-ip-phone-csrf>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.1  | Added the web service feature to the bulleted list introduction in Vulnerable Products. Updated first item in bulleted list in Vulnerable Products and Fixed Releases. Added note to Vulnerable Products.  | Vulnerable Products and Fixed Releases  | Final  | 2019-March-22  |  
| 1.0  | Initial public release.  | —  | Final  | 2019-March-20  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190320-ip-phone-csrf.html "Back to Top")
