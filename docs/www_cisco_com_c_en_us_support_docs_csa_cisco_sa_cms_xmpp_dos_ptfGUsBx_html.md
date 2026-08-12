  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Meeting Server Extensible Messaging and Presence Protocol Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html) to Save Content 
Print
### Available Languages
Updated:May 3, 2020
Document ID:1588541856816469
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Meeting Server Extensible Messaging and Presence Protocol Denial of Service Vulnerability
Medium
Advisory ID: 
cisco-sa-cms-xmpp-dos-ptfGUsBx
First Published:
2020 February 19 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvk42193](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvk42193)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)
CVE-2020-3160
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)
CVSS Score:
[ Base 5.3](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L/E:X/RL:X/RC:X
CVE-2020-3160
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cms-xmpp-dos-ptfGUsBx/csaf/cisco-sa-cms-xmpp-dos-ptfGUsBx.json)
Email 
## 
Summary 
  * A vulnerability in the Extensible Messaging and Presence Protocol (XMPP) feature of Cisco Meeting Server software could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition for users of XMPP conferencing applications. Other applications and processes are unaffected.
The vulnerability is due to improper input validation of XMPP packets. An attacker could exploit this vulnerability by sending crafted XMPP packets to an affected device. An exploit could allow the attacker to cause process crashes and a DoS condition for XMPP conferencing applications.
Cisco has released software updates that address the vulnerability described in this advisory. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cms-xmpp-dos-ptfGUsBx>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected Cisco Meeting Server deployments that are running a software release earlier than Release 2.8 and that have the XMPP feature enabled.
See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
**Note:** XMPP is not enabled by default.
### Determine the Status of XMPP for Cisco Meeting Server Deployments
Administrators can determine whether the XMPP feature is enabled on a device by using the **xmpp status** command in the device CLI, as shown in the following example:
> 
```
cms> xmpp status  
> **Enabled**                 : **true**  
> Clustered               : false
.
.
.

```

##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html#vp) section of this advisory are known to be affected by this vulnerability.


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories and Alerts page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, Cisco Meeting Server software releases 2.8 and later contained the fix for this vulnerability.
See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.


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
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cms-xmpp-dos-ptfGUsBx>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2020-February-19  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cms-xmpp-dos-ptfGUsBx.html "Back to Top")
