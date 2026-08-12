  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Communications Manager Static SSH Credentials Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html) to Save Content 
Print
### Available Languages
Updated:July 2, 2025
Document ID:1751472267455216
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Unified Communications Manager Static SSH Credentials Vulnerability
Critical
Advisory ID: 
cisco-sa-cucm-ssh-m4UBdpE7
First Published:
2025 July 2 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwp27755](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwp27755)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)
CVE-2025-20309
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)
CWE-798
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)
CVSS Score:
[ Base 10.0](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:X/RL:X/RC:X
CVE-2025-20309
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)
CWE-798
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssh-m4UBdpE7/csaf/cisco-sa-cucm-ssh-m4UBdpE7.json)
Email 
## 
Summary 
  * A vulnerability in Cisco Unified Communications Manager (Unified CM) and Cisco Unified Communications Manager Session Management Edition (Unified CM SME) could allow an unauthenticated, remote attacker to log in to an affected device using the _root_ account, which has default, static credentials that cannot be changed or deleted.
This vulnerability is due to the presence of static user credentials for the _root_ account that are reserved for use during development. An attacker could exploit this vulnerability by using the account to log in to an affected system. A successful exploit could allow the attacker to log in to the affected system and execute arbitrary commands as the _root_ user.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssh-m4UBdpE7>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects Cisco Unified CM and Unified CM SME Engineering Special (ES) releases 15.0.1.13010-1 through 15.0.1.13017-1, regardless of device configuration.
**Note:** ES releases are limited fix releases that are distributed only by the Cisco Technical Assistance Center (TAC).
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html#fs) section of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html#vp) section of this advisory are known to be affected by this vulnerability.


## 
Indicators of Compromise 
  * The [Cisco Security Indicators of Compromise Reference Guide](https://sec.cloudapps.cisco.com/security/center/resources/iocs.html "Cisco Security Indicators of Compromise Reference Guide") lists commonly observed IoCs, which can help identify devices that may have been impacted by the vulnerability disclosed in this Cisco security advisory.
Successful exploitation would result in a log entry to /var/log/active/syslog/secure for the _root_ user with _root_ permissions. Logging of this event is enabled by default.
To retrieve the logs, run the following command from the CLI:
> 
```
cucm1# file get activelog syslog/secure
```

If a log entry both includes **sshd** and shows a successful SSH login by the user _root_ , it is an IoC, as shown in the following example:
> 
```
Apr 6 10:38:43 cucm1 authpriv 6 systemd: pam_unix(systemd-user:session): session opened for user root by (uid=0)  
> Apr 6 10:38:43 cucm1 authpriv 6 **sshd**: pam_unix(sshd:session): session opened for user **root** by (uid=0)
```



## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * Cisco has released [free software updates](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#ssu) that address the vulnerability described in this advisory. Customers with service contracts that entitle them to regular software updates should obtain security fixes through their usual update channels.
Customers may only install and expect support for software versions and feature sets for which they have purchased a license. By installing, downloading, accessing, or otherwise using such software upgrades, customers agree to follow the terms of the Cisco software license:  
<https://www.cisco.com/c/en/us/products/end-user-license-agreement.html>
Additionally, customers may only download software for which they have a valid license, procured from Cisco directly, or through a Cisco authorized reseller or partner. In most cases this will be a maintenance upgrade to software that was previously purchased. Free security software updates do not entitle customers to a new software license, additional software feature sets, or major revision upgrades.
The [Cisco Support and Downloads page](https://www.cisco.com/c/en/us/support/index.html) on Cisco.com provides information about licensing and downloads. This page can also display customer device support coverage for customers who use the My Devices tool.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Customers Without Service Contracts
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the Cisco TAC: <https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html>
Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
### Fixed Releases
In the following table, the left column lists Cisco software releases. The right column indicates whether a release is affected by the vulnerability that is described in this advisory and the first release that includes the fix for this vulnerability. Customers are advised to upgrade to an appropriate [fixed software release](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) as indicated in this section.  
| Cisco Unified CM and Unified CM SME Release  | First Fixed Release  |  
| --- | --- |  
| 12.5  | Not vulnerable  |  
| 14  | Not vulnerable  |  
| 15.0.1.13010-1 through 15.0.1.13017-11  | 15SU3 (Jul 2025) or apply patch file:  
[ciscocm.CSCwp27755_D0247-1.cop.sha512](https://software.cisco.com/download/home/286331940/type/286319173/release/COP-Files)  |  
1. Only the listed set of ES releases is vulnerable. No Service Updates (SUs) for any releases are affected.
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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssh-m4UBdpE7>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2025-JUL-02  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssh-m4UBdpE7.html "Back to Top")
