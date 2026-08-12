  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Multiple Cisco Products SNORT HTTP Detection Engine File Policy Bypass Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html) to Save Content 
Print
### Available Languages
Updated:October 21, 2020
Document ID:1603297690745993
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Multiple Cisco Products SNORT HTTP Detection Engine File Policy Bypass Vulnerability
Medium
Advisory ID: 
cisco-sa-ftd-bypass-3eCfd24j
First Published:
2020 October 21 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvm69545](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvm69545)
[CSCvq96573](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvq96573)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)
CVE-2020-3299
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)
CWE-693
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)
CVSS Score:
[ Base 5.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:N/E:X/RL:X/RC:X
CVE-2020-3299
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)
CWE-693
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-bypass-3eCfd24j/csaf/cisco-sa-ftd-bypass-3eCfd24j.json)
Email 
## 
Summary 
  * Multiple Cisco products are affected by a vulnerability in the Snort detection engine that could allow an unauthenticated, remote attacker to bypass a configured File Policy for HTTP.
The vulnerability is due to incorrect detection of modified HTTP packets used in chunked responses. An attacker could exploit this vulnerability by sending crafted HTTP packets through an affected device. A successful exploit could allow the attacker to bypass a configured File Policy for HTTP packets and deliver a malicious payload.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability. 
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-bypass-3eCfd24j>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected the following Cisco products if they were running a vulnerable release of Cisco software:
    * 1000 Series Integrated Services Routers (ISRs)
    * 3000 Series Industrial Security Appliances (ISAs)
    * 4000 Series Integrated Services Routers (ISRs)
    * Cloud Services Router 1000V
    * Firepower Threat Defense (FTD) Software
    * Integrated Services Virtual Router (ISRv)
    * Meraki MX Series Security Appliances1
    1. See [Products Confirmed Not Vulnerable](https://tvce.cisco.com/security/aims/PublicationPreview.aspx?ID=72315&Version=1&Revision=8#nvp) section in this advisory for exceptions.
This vulnerability also affects the open-source Snort project version prior to 2.9.13.1. For more information, see the [Snort website](https://www.snort.org/).
For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * Adaptive Security Appliance (ASA) Software
    * Firepower Management Center (FMC) Software
    * Meraki MX64 Security Appliances
    * Meraki MX64W Security Appliances
    * Meraki vMX100 Virtual Appliances
    * Meraki Z1 Appliances
    * Meraki Z3 Series Appliances


## 
Workarounds 
  * There are no workarounds that address this vulnerability. Please contact TAC for mitigations.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
**Fixed Releases**
At the time of publication, the release information in the following table(s) was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerability described in this advisory and which release included the fix for this vulnerability.
**Cisco FTD Software**  
| Cisco FTD Software Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 6.01  | 6.3.0.1  |  
| 6.0.11  | 6.3.0.1  |  
| 6.1.0  | 6.3.0.1  |  
| 6.2.0  | 6.3.0.1  |  
| 6.2.1  | 6.3.0.1  |  
| 6.2.2  | 6.3.0.1  |  
| 6.2.3  | 6.3.0.1  |  
| 6.3.0  | 6.3.0.1  |  
| 6.4.0  | Not vulnerable.  |  
| 6.5.0  | Not vulnerable.  |  
| 6.6.0  | Not vulnerable.  |  
1. Cisco FMC and FTD Software releases 6.0.1 and earlier, as well as releases 6.2.0 and 6.2.1, have reached end of software maintenance. Customers are advised to migrate to a supported release that includes the fix for this vulnerability.
To upgrade to a fixed release of Cisco FTD Software, do one of the following:
    * For devices that are managed by using Cisco Firepower Management Center (FMC), use the FMC interface to install the upgrade. After installation is complete, reapply the access control policy.
    * For devices that are managed by using Cisco Firepower Device Manager (FDM), use the FDM interface to install the upgrade. After installation is complete, reapply the access control policy.
**Cisco UTD Snort IPS Engine Software for IOS XE**  
| UTD SNORT IPS Engine IOS XE Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 16.9  | 16.9.5  |  
| 16.12  | 16.12.2  |  
| 17.1  | Not vulnerable.  |  
| 17.2  | Not vulnerable.  |  
See the Details section in the bug IDs [CSCvq96573](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvq96573) for the most complete and current information.
**Cisco UTD Engine Software for IOS XE SD-WAN**  
| UTD Engine IOS XE SD-WAN Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 16.10  | 16.10.3b  |  
| 16.12  | 16.12.1d  |  
| 17.2  | Not vulnerable.  |  
See the Details section in the bug IDs [CSCvq96573](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvq96573) for the most complete and current information.
**Meraki MX Series Security Appliances**  
| Meraki MX Series Security Appliance Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| MX 14  | MX 14.53  |  
| MX 15  | MX 15.33 (beta)  |  
**Open Source SNORT**
This is fixed in the open-source Snort project version 2.9.13.1 and later. For more information, see the [Snort website](https://www.snort.org/).


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
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-bypass-3eCfd24j>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2020-OCT-21  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ftd-bypass-3eCfd24j.html "Back to Top")
