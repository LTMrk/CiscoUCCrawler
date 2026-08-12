  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Integrated Management Controller Virtual Keyboard Video Monitor Stored Cross-Site Scripting Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html) to Save Content 
Print
### Available Languages
Updated:August 27, 2025
Document ID:1756313105958402
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Integrated Management Controller Virtual Keyboard Video Monitor Stored Cross-Site Scripting Vulnerability
Medium
Advisory ID: 
cisco-sa-ucs-kvmsxss-6h7AnUyk
First Published:
2025 August 27 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwm57433](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm57433)
[CSCwn43958](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwn43958)
[CSCwo77420](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo77420)
[ More... ](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html) ,[CSCwm57433](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm57433),[CSCwn43958](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwn43958),[CSCwo77420](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo77420),[CSCwq34766](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq34766)
CVE-2025-20342
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)
CWE-80
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)
CVSS Score:
[ Base 5.4](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N/E:X/RL:X/RC:X
CVE-2025-20342
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)
CWE-80
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-kvmsxss-6h7AnUyk/csaf/cisco-sa-ucs-kvmsxss-6h7AnUyk.json)
Email 
## 
Summary 
  * A vulnerability in the Virtual Keyboard Video Monitor (vKVM) connection handling of Cisco Integrated Management Controller (IMC) could allow an authenticated, remote attacker with low privileges to conduct a stored cross-site scripting (XSS) attack against a user of the interface.
This vulnerability is due to insufficient validation of user-supplied input by the web-based management interface of an affected system. An attacker could exploit this vulnerability by injecting malicious code into a specific data field in the interface. A successful exploit could allow the attacker to execute arbitrary script code in the context of the affected interface or access sensitive, browser-based information. To exploit this vulnerability, the attacker must have valid user credentials with privileges that allow for vKVM access on the affected device.
**Note:** The affected vKVM client is also included in Cisco UCS Manager.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-kvmsxss-6h7AnUyk>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected the following Cisco products if they were running a vulnerable software release, regardless of device configuration:
    * Catalyst 8300 Series Edge uCPE ([CSCwo77420](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo77420))
    * Cisco UCS Manager Software ([CSCwq34766](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwq34766))
    * UCS B-Series Blade Servers ([CSCwm57433](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm57433))
    * UCS C-Series M6, M7, and M8 Rack Servers ([CSCwn43958](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwn43958))
    * UCS E-Series Servers M6 ([CSCwo77420](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo77420))
    * UCS X-Series Modular System ([CSCwm57433](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm57433))
Cisco appliances that are based on a preconfigured version of one of the Cisco UCS C-Series Servers that are in the preceding list were also affected by this vulnerability if they exposed access to the Cisco IMC UI. At the time of publication, this included the following Cisco products:
    * Application Policy Infrastructure Controller (APIC) Servers
    * Business Edition 6000 and 7000 Appliances
    * Catalyst Center Appliances, formerly DNA Center
    * Cisco Telemetry Broker Appliance
    * Cloud Services Platform (CSP) 5000 Series
    * Common Services Platform Collector (CSPC) Appliances
    * Connected Mobile Experiences (CMX) Appliances
    * Connected Safety and Security UCS Platform Series Servers
    * Cyber Vision Center Appliances
    * Expressway Series Appliances
    * HyperFlex Edge Nodes
    * HyperFlex Nodes
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
For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html#fs) section of this advisory. See the Details section in the bug IDs at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * 5000 Series Enterprise Network Compute Systems (ENCS)
    * UCS C-Series M5
    * UCS E-Series Servers M3 
    * UCS S-Series Storage Servers


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the release information in the following tables was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerability that is described in this advisory and which release included the fix for this vulnerability.
**Catalyst 8300 Series Edge uCPE**
**Note:** Cisco IMC on Cisco Catalyst 8300 Series Edge uCPE is included in Cisco Enterprise NFV Infrastructure Software (NFVIS). Cisco IMC is upgraded as part of the firmware auto-upgrade process in NFVIS.  
| Cisco NFVIS Release  | First Fixed Release  |  
| --- | --- |  
| 4.18 and earlier  | 4.18.1  |  
**UCS Manager Software**  
| Cisco UCS Manager Software Release  | First Fixed Release  |  
| --- | --- |  
| 4.1 and earlier  | Migrate to a fixed release.  |  
| 4.2  | 4.2(3p)  |  
| 4.3  | 4.3(6a)  |  
| 6.0  | Not vulnerable.  |  
**UCS B-Series and X-Series Servers in UCS Manager Mode**  
| Cisco UCS Server Software Release  | First Fixed Release  |  
| --- | --- |  
| 4.1 and earlier  | Migrate to a fixed release.  |  
| 4.2  | 4.2(3o)  |  
| 4.3  | 4.3(5c)  |  
| 6.0  | Not vulnerable.  |  
**UCS B-Series Servers in Intersight Managed Mode**  
| Cisco Intersight Server Firmware Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 4.2  | Migrate to a fixed release.  |  
| 4.2  | 4.2(3l)  |  
| 5.1  | Migrate to a fixed release.  |  
| 5.2  | Migrate to a fixed release.  |  
| 5.3  | 5.3(0.250001)  |  
| 5.4  | Not vulnerable.  |  
| 6.0  | Not vulnerable.  |  
**UCS X-Series Servers in Intersight Managed Mode**  
| Cisco Intersight Server Firmware Release  | First Fixed Release  |  
| --- | --- |  
| 5.0  | 5.0(4i)  |  
| 5.1  | Migrate to a fixed release.  |  
| 5.2  | Migrate to a fixed release.  |  
| 5.3  | 5.3(0.250001)  |  
| 5.4  | Not vulnerable.  |  
| 6.0  | Not vulnerable.  |  
**UCS C-Series Servers in Standalone Mode or Intersight Managed Mode  
**  
| Cisco UCS Server Software Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 4.2  | Migrate to a fixed release.  |  
| 4.2  | 4.2(3o)  |  
| 4.3  | 4.3(5.250001)  |  
| 6.0  | Not vulnerable.  |  
**UCS C-Series Servers in UCS Manager Mode  
**  
| Cisco UCS Server Software Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 4.2  | Migrate to a fixed release.  |  
| 4.2  | 4.2(3o)  |  
| 4.3  | 4.3(5c)  |  
| 6.0  | Not vulnerable.  |  
**UCS E-Series M6 Server**  
| Cisco UCS Server Software Release  | First Fixed Release  |  
| --- | --- |  
| 4.15 and earlier  | 4.15.2  |  
**Note:** For Cisco appliances that are based on a preconfigured version of a Cisco UCS C-Series Server, administrators can perform a direct upgrade of the Cisco IMC software to one of the fixed releases as indicated in the preceding tables. For instructions, see the [Cisco Host Upgrade Utility User Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/lomug/4-2/b_cisco-host-upgrade-utility-user-guide-4-2/m_upgrading-the-firmware.html). The exceptions are the appliances that are listed in the following table. For these appliances, follow the instructions in the **Remediation** column:  
| Cisco Hardware Platform  | First Fixed Cisco IMC Release  | Remediation  |  
| --- | --- | --- |  
| Cisco Telemetry Broker Appliance  | 4.3(5.250030)  | Apply the firmware update [m6-tb2300-ctb-firmware-4.3-5.250030.iso](https://www.cisco.com/c/dam/en/us/td/docs/security/Telemetry_Broker/Release-Notes/m6-tb2300-ctb-firmware-4_3-5_250030_iso_DV_1_0.pdf).  |  
| IEC6400 Edge Compute Appliances  | 4.3(5.250033)  | Apply the HUU upgrade using IEC6400-HUU-4.3.5.img.  |  
| Secure Endpoint Private Cloud Appliances  | 4.3(6.250053)  | Upgrade to version 4.2.5 or later and then follow the steps documented in the [TechNote](https://www.cisco.com/c/en/us/support/docs/security/secure-endpoint-private-cloud/222008-cisco-secure-endpoint-private-cloud-firm.html).  |  
| Secure Firewall Management Center Appliances  | 4.3(6.250053)  | Apply [Hotfix l](https://www.cisco.com/c/en/us/td/docs/security/secure-firewall/release-notes/threat-defense/hotfix/threat-defense-release-notes-hotfix.html#Cisco_Reference.dita_e5a104de-579f-48b7-adb6-0a72dc5183b7).  |  
| Secure Malware Analytics Appliances  | 4.3(6.250053)  | Update the firmware using the [Out-of-Band Firmware Update ISO](https://www.cisco.com/c/en/us/td/docs/security/secure-malware-analytics/admin-guide/v2-19/secure-malware-analytics-guide/m_oob-update-firmware.html) procedure.  |  
| Secure Network Analytics Appliances  | 4.3(5.250030)  | Install update [patch-common-SNA-FIRMWARE-20250403-v2-01.swu](https://www.cisco.com/c/dam/en/us/td/docs/security/stealthwatch/cimc_bios/7_5_3_M6_CIMC_firmware_4_3_5_250030_readme_DV_1_0.pdf).  |  
| Secure Network Server Appliances  | 4.3(5.250001)  | Apply the BIOS and HUU upgrade as documented in the Firmware Upgrade Guide for [Cisco SNS 3700 Series](https://www.cisco.com/c/en/us/td/docs/security/ise/sns3700hig/sns-37xx-firmware-4-x-xx_upgrade_guide.html#r_overview).  |  
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
  * [Cross-Site Scripting](https://owasp.org/www-community/attacks/xss/)


## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-kvmsxss-6h7AnUyk>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2025-AUG-27  |  
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
  * [Cross-Site Scripting](https://owasp.org/www-community/attacks/xss/)


[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-kvmsxss-6h7AnUyk.html "Back to Top")
