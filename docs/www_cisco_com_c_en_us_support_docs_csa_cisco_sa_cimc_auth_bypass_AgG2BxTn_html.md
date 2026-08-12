  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Integrated Management Controller Authentication Bypass Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html) to Save Content 
Print
### Available Languages
Updated:April 1, 2026
Document ID:1775069892371251
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Integrated Management Controller Authentication Bypass Vulnerability
Critical
Advisory ID: 
cisco-sa-cimc-auth-bypass-AgG2BxTn
First Published:
2026 April 1 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwq55648](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq55648)
[CSCwq55659](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq55659)
[CSCwq68912](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq68912)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
CVE-2026-20093
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
CVSS Score:
[ Base 9.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:X/RL:X/RC:X
CVE-2026-20093
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-auth-bypass-AgG2BxTn/csaf/cisco-sa-cimc-auth-bypass-AgG2BxTn.json)
Email 
## 
Summary 
  * A vulnerability in the change password functionality of Cisco Integrated Management Controller (IMC) could allow an unauthenticated, remote attacker to bypass authentication and gain access to the system as  _Admin_.
This vulnerability is due to incorrect handling of password change requests. An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device. A successful exploit could allow the attacker to bypass authentication, alter the passwords of any user on the system, including an  _Admin_ user, and gain access to the system as that user.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-auth-bypass-AgG2BxTn>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects the following Cisco products if they are running a vulnerable release of Cisco IMC, regardless of device configuration:
    * 5000 Series Enterprise Network Compute Systems (ENCS) ([CSCwq55648](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq55648))
    * Catalyst 8300 Series Edge uCPE ([CSCwq68912](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq68912))
    * UCS C-Series M5 and M6 Rack Servers in standalone mode ([CSCwq55659](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq55659))
    * UCS E-Series Servers M3 ([CSCwq55648](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq55648))
    * UCS E-Series Servers M6 ([CSCwq68912](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq68912))
Cisco appliances that are based on a preconfigured version of one of the Cisco UCS C-Series Servers that are in the preceding list are also affected by this vulnerability if they expose access to the Cisco IMC UI. This includes the following Cisco products:
    * Application Policy Infrastructure Controller (APIC) Servers
    * Business Edition 6000 and 7000 Appliances
    * Catalyst Center Appliances
    * Cisco Telemetry Broker Appliances
    * Cloud Services Platform (CSP) 5000 Series
    * Common Services Platform Collector (CSPC) Appliances
    * Connected Mobile Experiences (CMX) Appliances
    * Connected Safety and Security UCS Platform Series Servers
    * Cyber Vision Center Appliances
    * Expressway Series Appliances
    * HyperFlex Edge Nodes
    * HyperFlex Nodes in HyperFlex Datacenter without Fabric Interconnect (DC-No-FI) deployment mode
    * IEC6400 Edge Compute Appliances
    * IOS XRv 9000 Appliances
    * Meeting Server 1000 Appliances
    * Nexus Dashboard Appliances
    * Prime Infrastructure Appliances
    * Prime Network Registrar Jumpstart Appliances
    * Secure Endpoint Private Cloud Appliances
    * Secure Firewall Management Center Appliances
    * Secure Malware Analytics Appliances
    * Secure Network Analytics Appliances
    * Secure Network Server Appliances
    * Secure Workload Servers
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html#fs) section of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has determined that this vulnerability does not affect the following Cisco products:
    * UCS B-Series Blade Servers
    * UCS C-Series M7 and M8 Rack Servers in standalone mode
    * UCS C-Series Rack Servers with Fabric Interconnects in UCS Manager or Intersight Managed Mode (IMM)
    * UCS S-Series Storage Servers
    * UCS X-Series Modular System
    * Unified Edge


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * Cisco considers any workarounds and mitigations (if applicable) to be temporary solutions until an upgrade to a fixed software release is available. To fully remediate these vulnerabilities and avoid future exposure as described in this advisory, Cisco strongly recommends that customers upgrade to the fixed software indicated in this advisory.
### Fixed Releases
In the following tables, the left column lists Cisco software releases. The right column indicates whether a release is affected by the vulnerability that is described in this advisory and the first release that includes the fix for this vulnerability. Customers are advised to upgrade to an appropriate [fixed software release](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) as indicated in this section.
**5000 Series ENCS and Catalyst 8300 Series Edge uCPE**
**Note:** Upgrading Cisco IMC on Cisco 5000 Series ENCS and Cisco Catalyst 8300 Series Edge uCPE requires upgrading Cisco Enterprise NFV Infrastructure Software (NFVIS) on the platforms. Cisco IMC is upgraded as part of the firmware auto-upgrade process.  
| Cisco NFVIS Release  | First Fixed Release for Cisco 5000 Series ENCS  |  
| --- | --- |  
| 4.15 and earlier  | 4.15.5  |  
| Cisco NFVIS Release  | First Fixed Release for Cisco Catalyst 8300 Series Edge uCPE  |  
| --- | --- |  
| 4.16 and earlier  | Migrate to a fixed release.  |  
| 4.18  | 4.18.3 (Apr 2026)  |  
| 26.1  | Not vulnerable.  |  
**UCS C-Series M5 Rack Server**  
| Cisco IMC Release  | First Fixed Release  |  
| --- | --- |  
| 4.2 and earlier  | Migrate to a fixed release.  |  
| 4.3  | 4.3(2.260007)  |  
**UCS C-Series M6 Rack Server**  
| Cisco IMC Release  | First Fixed Release  |  
| --- | --- |  
| 4.2 and earlier  | Migrate to a fixed release.  |  
| 4.3  | 4.3(6.260017)  |  
| 6.0  | 6.0(1.250174)  |  
**UCS E-Series M3**  
| Cisco IMC Release  | First Fixed Release  |  
| --- | --- |  
| 3.2 and earlier  | 3.2.17  |  
**UCS E-Series M6**  
| Cisco IMC Release  | First Fixed Release  |  
| --- | --- |  
| 4.15 and earlier  | 4.15.3  |  
**Note:** For Cisco appliances that are based on a preconfigured version of a Cisco UCS C-Series Server, administrators can perform a direct upgrade of Cisco IMC to one of the fixed releases mentioned in the preceding tables. For instructions, see the [Cisco Host Upgrade Utility (HUU) User Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/lomug/4-2/b_cisco-host-upgrade-utility-user-guide-4-2/m_upgrading-the-firmware.html). The exceptions are the appliances that are listed in the following table. For these appliances, follow the instructions in the Remediation column:  
| Cisco Hardware Platform  | First Fixed Cisco IMC Release  | Remediation  |  
| --- | --- | --- |  
| Cisco Telemetry Broker Appliances  | 6.0(1.250192) (M6)  | Apply the firmware update [m6-tb2300-ctb-firmware-6.0-1.250192.iso](https://www.cisco.com/c/dam/en/us/td/docs/security/Telemetry_Broker/Release-Notes/m6-tb2300-ctb-firmware-6_0-1_250192_iso_DV_1_0.pdf).  |  
| IEC6400 Edge Compute Appliances  | 4.3(6.260017) (M6)  | Apply the HUU upgrade using [IEC6400-HUU-4.3.6.img](https://software.cisco.com/download/home/286331621/type/286331613/release/HUU%204.3.6).  |  
| Secure Endpoint Private Cloud Appliances  | 4.3(2.260007) (M5)  
4.3(6.260017) (M6)  | Upgrade to Release 4.2.5 or later, then follow the steps in the [TechNote](https://www.cisco.com/c/en/us/support/docs/security/secure-endpoint-private-cloud/222008-cisco-secure-endpoint-private-cloud-firm.html).  |  
| Secure Firewall Management Center Appliances  | 4.3(2.260007) (M5)  
4.3(6.260017) (M6)  | Apply [Hotfix FX](https://www.cisco.com/c/en/us/td/docs/security/secure-firewall/release-notes/threat-defense/hotfix/threat-defense-release-notes-hotfix.html#Cisco_Reference.dita_e5a104de-579f-48b7-adb6-0a72dc5183b7).  |  
| Secure Malware Analytics Appliances  | 4.3(2.260007) (M5)  
4.3(6.260017) (M6)  | Update the firmware using the [Out-of-Band Firmware Update ISO](https://www.cisco.com/c/en/us/td/docs/security/secure-malware-analytics/admin-guide/v2-19/secure-malware-analytics-guide/m_oob-update-firmware.html) procedure.  |  
| Secure Network Analytics Appliances  | 4.3(2.260007) (M5)  
6.0(1.250192) (M6)  | For M5, install [patch-common-SNA-FIRMWARE-20260210-M5-REL.iso](https://www.cisco.com/c/dam/en/us/td/docs/security/stealthwatch/cimc_bios/7_5_3_M5_CIMC_firmware_4_3_2_260007_readme_DV_1_0.pdf).  
For M6, install [patch-common-SNA-FIRMWARE-20260210-M6-REL.iso](https://www.cisco.com/c/dam/en/us/td/docs/security/stealthwatch/cimc_bios/7_5_3_M6_CIMC_firmware_6_0_1_250192_readme_DV_1_0.pdf).  |  
| Secure Network Server Appliances  | 4.3(2.260007) (M5)  
4.3(6.260017) (M6)  
6.0(1.250174) (M6)  | Apply the BIOS and HUU upgrade as documented in the Firmware Upgrade Guide for [Cisco Secure Network Server 3600 Series](https://www.cisco.com/c/en/us/td/docs/security/ise/sns3600hig/sns-36xx-firmware-4-x-xx_upgrade_guide.html#Cisco_Concept.dita_3e2c957e-62e6-4b2d-9f76-96ad121f29e1) or [Cisco Secure Network Server 3700 Series](https://www.cisco.com/c/en/us/td/docs/security/ise/sns3700hig/sns-37xx-firmware-4-x-xx_upgrade_guide.html#r_overview).  |  
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * Cisco would like to thank the security researcher jyh for reporting this vulnerability.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-auth-bypass-AgG2BxTn>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2026-APR-01  |  
Show Less


* * *
## 
Legal Disclaimer 
  * ### SOFTWARE DOWNLOADS AND TECHNICAL SUPPORT
The [Cisco Support and Downloads](https://www.cisco.com/c/en/us/support/index.html) page on Cisco.com provides information about licensing and downloads. This page can also display customer device support coverage for customers who use the My Devices tool. Please note that customers may download only software that was procured from Cisco directly or through a Cisco authorized reseller or partner and for which the license is still valid.
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html). Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult [the advisories](https://www.cisco.com/go/psirt) for the relevant Cisco products to determine exposure and a complete upgrade solution. In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) or their contracted maintenance providers.
### LEGAL DISCLAIMER DETAILS
CISCO DOES NOT MAKE ANY EXPRESS OR IMPLIED GUARANTEES OR WARRANTIES OF ANY KIND, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. WITHOUT LIMITING THE GENERALITY OF THE FOREGOING, CISCO DOES NOT GUARANTEE THE ACCURACY OR COMPLETENESS OF THIS INFORMATION. THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
Copies or summaries of the information contained in this Security Advisory may lack important information or contain factual errors. Customers are advised to visit the [Cisco Security Advisories](https://www.cisco.com/go/psirt) page for the most recent version of this Security Advisory. The Cisco Product Security Incident Response Team (PSIRT) assesses only the affected and fixed release information that is documented in this advisory. See the [Cisco Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) for more information.


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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html "Back to Top")
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
