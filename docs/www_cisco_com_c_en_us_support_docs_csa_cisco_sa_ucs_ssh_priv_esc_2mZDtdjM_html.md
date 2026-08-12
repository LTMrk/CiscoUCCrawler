  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Integrated Management Controller Privilege Escalation Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html) to Save Content 
Print
### Available Languages
Updated:June 4, 2025
Document ID:1749052815600164
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Integrated Management Controller Privilege Escalation Vulnerability
High
Advisory ID: 
cisco-sa-ucs-ssh-priv-esc-2mZDtdjM
First Published:
2025 June 4 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwc06871](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc06871)
[CSCwk24502](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk24502)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)
CVE-2025-20261
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)
CWE-923
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)
CVSS Score:
[ Base 8.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:X/RL:X/RC:X
CVE-2025-20261
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)
CWE-923
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM/csaf/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.json)
Email 
## 
Summary 
  * A vulnerability in the SSH connection handling of Cisco Integrated Management Controller (IMC) for Cisco UCS B-Series, UCS C-Series, UCS S-Series, and UCS X-Series Servers could allow an authenticated, remote attacker to access internal services with elevated privileges.
This vulnerability is due to insufficient restrictions on access to internal services. An attacker with a valid user account could exploit this vulnerability by using crafted syntax when connecting to the Cisco IMC of an affected device through SSH. A successful exploit could allow the attacker to access internal services with elevated privileges, which may allow unauthorized modifications to the system, including the possibility of creating new administrator accounts on the affected device.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability, but a mitigation is available.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects the following Cisco products if they are running a vulnerable software release and they accept incoming SSH connections to the Cisco IMC:
    * UCS B-Series Blade Servers ([CSCwk24502](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk24502))
    * UCS C-Series Rack Servers ([CSCwc06871](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc06871))
    * UCS S-Series Storage Servers ([CSCwc06871](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc06871))
    * UCS X-Series Modular System ([CSCwk24502](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk24502))
**Note:** Cisco UCS C-Series and UCS S-Series Servers in standalone mode accept incoming SSH connections by default. For additional details, see the _Configuring SSH_ section of the [Cisco UCS C-Series Integrated Management Controller GUI Configuration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/gui/config/guide/4_3/b_cisco_ucs_c-series_gui_configuration_guide_43/b_Cisco_UCS_C-series_GUI_Configuration_Guide_41_chapter_01101.html#task_083E4199DCF1404486FC1C6F958CBE8C). Cisco UCS B-Series, Managed UCS C-Series, Managed UCS S-Series, and UCS X-Series Servers accept incoming SSH connections only if a Serial over LAN (SoL) policy is enabled on the associated Service Profile. For additional details, see the _Serial over LAN Policy Settings_ section of the [Cisco UCS Manager Server Management Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-manager/GUI-User-Guides/Server-Mgmt/4-3/b_cisco_ucs_manager_server_mgmt_guide_4_3/m_server-related_policy_configuration.html#d21614e28464a1635).
Cisco appliances that are based on a preconfigured version of a Cisco UCS C-Series Server are also affected by this vulnerability if they expose SSH access to the Cisco IMC. At the time of publication, this included the following Cisco products:
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
    * Secure Firewall Management Center Appliances, formerly Firepower Management Center
    * Secure Malware Analytics Appliances
    * Secure Network Analytics Appliances
    * Secure Network Server Appliances
    * Secure Workload Servers
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html#fs) section of this advisory.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * 5000 Series Enterprise Network Compute Systems (ENCS)
    * Catalyst 8300 Series Edge uCPE
    * UCS E-Series Servers


## 
Workarounds 
  * There are no workarounds that address this vulnerability. However, there is a mitigation. 
If it is not required, SSH access to the Cisco IMC of an affected device may be disabled.
For Cisco UCS C-Series and UCS S-Series Servers in standalone mode, choose **Admin** > **Communication Services** on the Cisco IMC web UI and uncheck the **SSH Enabled** option.
For Cisco UCS B-Series, Managed UCS C-Series, Managed UCS S-Series, and UCS X-Series Servers, disable the Serial over LAN (SoL) policy on the associated Service Profile (SoL access is disabled by default). From the **Servers** section of the Cisco UCS Manager web UI, do the following:
    1. Choose the **Service Profile** in question.
    2. Click the **Change Serial over LAN Policy** link under **Actions** in the **Policies** tab.
    3. Choose the **No Serial over LAN Policy** option.
    4. Click **OK**.
Alternatively, edit the applied **Serial Over LAN Policy** under **Policies** > **Serial Over LAN Policies** and change the **Serial over LAN State** property from **Enable** to **Disable**. This would disable SoL access for all the Service Profiles that are using the SoL policy in question.
While this mitigation has been deployed and was proven successful in a test environment, customers should determine the applicability and effectiveness in their own environment and under their own use conditions. Customers should be aware that any workaround or mitigation that is implemented may negatively impact the functionality or performance of their network based on intrinsic customer deployment scenarios and limitations. Customers should not deploy any workarounds or mitigations before first evaluating the applicability to their own environment and any impact to such environment.


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
In the following tables, the left column lists Cisco software releases. The right column indicates whether a release is affected by the vulnerability that is described in this advisory and the first release that includes the fix for this vulnerability.
**UCS B-Series and X-Series Servers in UCS Manager Mode**  
| Cisco UCS Server Software Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 4.1  | Migrate to a fixed release.  |  
| 4.1  | 4.1(3n)  |  
| 4.2  | 4.2(3k)  |  
| 4.3  | 4.3(4c)  |  
**UCS B-Series Servers in Intersight Managed Mode**  
| Cisco Intersight Server Firmware Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 4.2  | Migrate to a fixed release.  |  
| 4.2  | 4.2(3i)  |  
| 5.1  | Migrate to a fixed release.  |  
| 5.2  | 5.2(2.240073)  |  
| 5.3  | Not vulnerable.  |  
| 5.4  | Not vulnerable.  |  
**UCS X-Series Servers in Intersight Managed Mode**  
| Cisco Intersight Server Firmware Release  | First Fixed Release  |  
| --- | --- |  
| 5.0  | 5.0(4f)  |  
| 5.1  | Migrate to a fixed release.  |  
| 5.2  | 5.2(2.240073)  |  
| 5.3  | Not vulnerable.  |  
| 5.4  | Not vulnerable.  |  
**UCS C-Series and S-Series Servers in Standalone Mode or Intersight Managed Mode  
**  
| Cisco UCS Server Software Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 4.2  | Migrate to a fixed release.  |  
| 4.2  | 4.2(2f), 4.2(3b)  |  
| 4.3  | Not vulnerable.  |  
**UCS C-Series and S-Series Servers in UCS Manager Mode  
**  
| Cisco UCS Server Software Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 4.2  | Migrate to a fixed release.  |  
| 4.2  | 4.2(2c), 4.2(3b)  |  
| 4.3  | Not vulnerable.  |  
**Note:** For Cisco appliances that are based on a preconfigured version of a Cisco UCS C-Series Server, administrators can perform a direct upgrade of the Cisco IMC software to one of the fixed releases as indicated in the preceding tables. For instructions, see the [Cisco Host Upgrade Utility User Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/lomug/4-2/b_cisco-host-upgrade-utility-user-guide-4-2/m_upgrading-the-firmware.html). The exceptions are the appliances that are listed in the following table. For these appliances, follow the instructions in the **Remediation** column:  
| Cisco Hardware Platform  | Remediation  |  
| --- | --- |  
| Cisco Telemetry Broker Appliance  | Apply the firmware update [m6-tb2300-ctb-firmware-4.3-2.240009.iso](https://www.cisco.com/c/dam/en/us/td/docs/security/Telemetry_Broker/Release-Notes/m6-tb2300-ctb-firmware-4_3-2_240009_iso_DV_1_0.pdf) or later.  |  
| IEC6400 Edge Compute Appliances  | Apply the HUU upgrade using IEC6400-HUU-4.2.3j.img.  |  
| Secure Endpoint Private Cloud Appliances  | Follow the steps documented in the [TechNote](https://www.cisco.com/c/en/us/support/docs/security/secure-endpoint-private-cloud/222008-cisco-secure-endpoint-private-cloud-firm.html).  |  
| Secure Firewall Management Center Appliances  | Apply Hotfix [EN](https://www.cisco.com/c/en/us/td/docs/security/firepower/hotfix/Firepower_Hotfix_Release_Notes/available-hotfixes.html#Cisco_Reference.dita_e5a104de-579f-48b7-adb6-0a72dc5183b7) or later.  |  
| Secure Malware Analytics Appliances  | Upgrade to release 2.19.4 or later and follow the [Updating Firmware Procedure](https://www.cisco.com/c/en/us/td/docs/security/secure-malware-analytics/admin-guide/v2-19/secure-malware-analytics-guide/m_update-firmware.html#about-updating-firmware).  |  
| Secure Network Analytics Appliances  | Install Update Patch [patch-common-SNA-FIRMWARE-20240305-v2-01.swu](https://www.cisco.com/c/dam/en/us/td/docs/security/stealthwatch/cimc_bios/7_4_1_M5_CIMC_firmware_4_3_2_240009_readme_DV_1_0.pdf) or later.  |  
| Secure Network Server Appliances  | Apply the BIOS and HUU upgrade as documented in the Firmware Upgrade Guide for [Cisco SNS 3700 Series](https://www.cisco.com/c/en/us/td/docs/security/ise/sns3700hig/sns-37xx-firmware-4-x-xx_upgrade_guide.html#r_overview) or [Cisco SNS 3600 Series](https://www.cisco.com/c/en/us/td/docs/security/ise/sns3600hig/sns-36xx-firmware-4-x-xx_upgrade_guide.html#Cisco_Concept.dita_3e2c957e-62e6-4b2d-9f76-96ad121f29e1).  |  
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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2025-JUN-04  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM.html "Back to Top")
