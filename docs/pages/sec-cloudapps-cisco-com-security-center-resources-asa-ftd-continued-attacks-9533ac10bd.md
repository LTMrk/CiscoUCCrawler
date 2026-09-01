---
doc_id: sec-cloudapps-cisco-com-security-center-resources-asa-ftd-continued-attacks-9533ac10bd
source_url: https://sec.cloudapps.cisco.com/security/center/resources/asa_ftd_continued_attacks
retrieved_at: 2026-09-01T14:08:40.147354+00:00
---

Home / Cisco Security

Cisco Event Response: Continued Attacks Against Cisco Firewalls

# Cisco Event Response: Continued Attacks Against Cisco Firewalls

Version 2.3 First Published: September 25, 2025 Last Updated: April 24, 2026

Update: On April 23, 2026, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) issued an update to V1: Emergency Directive (ED) 25-03: Identify and Mitigate Potential Compromise of Cisco Devices related to Cisco Secure Firewall Adaptive Security Appliance (ASA) and Cisco Secure Firewall Threat Defense (FTD) products.

According to the update, the ArcaneDoor threat actor has developed a previously unknown persistence mechanism that is preserved across upgrading to the fixed releases that were published in September 2025. This persistence mechanism resides in the Cisco Firepower eXtensible Operating System (FXOS) Software base operating system for Cisco Secure Firewall ASA Software and Cisco Secure FTD Software installations on the affected hardware platforms.

The ArcaneDoor threat actor has also broadened its attack radius beyond the previously targeted Cisco Adaptive Security Appliance (ASA) 5500-X Series devices running Cisco Secure Firewall ASA Software to any device running either Cisco Secure Firewall ASA Software or Cisco Secure Firewall Threat Defense (FTD) Software.

For more information, see the Continued Evolution of Persistence Mechanism Against Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Informational advisory.

Update: On November 5, 2025, Cisco became aware of a new attack variant against devices running Cisco Secure ASA Software or Cisco Secure FTD Software releases that are affected by CVE-2025-20333 and CVE-2025-20362. This attack can cause unpatched devices to unexpectedly reload, leading to denial of service (DoS) conditions. Cisco strongly recommends that all customers upgrade to the fixed software releases that are listed in the Fixed Releases section of this page.

## Summary

In May 2025, Cisco was engaged by multiple government agencies that provide incident response services to government organizations to support the investigation of attacks that were targeting certain Cisco Adaptive Security Appliance (ASA) 5500-X Series devices that were running Cisco Secure Firewall ASA Software with VPN web services enabled to implant malware, execute commands, and potentially exfiltrate data from the compromised devices.

Cisco dedicated a specialized, full-time team to this investigation, working closely with a limited set of affected customers. Our response involved providing instrumented images with enhanced detection capabilities, assisting customers with the analysis of packet captures from compromised environments, and conducting in-depth analysis of firmware extracted from infected devices. These collaborative and technical efforts enabled our teams to ultimately identify the underlying memory corruption bug in the product software.

Attackers were observed to have exploited multiple zero-day vulnerabilities and employed advanced evasion techniques such as disabling logging, intercepting CLI commands, and intentionally crashing devices to prevent diagnostic analysis. The complexity and sophistication of this incident required an extensive, multi-disciplinary response across Cisco’s engineering and security teams.

Cisco assesses with high confidence that this new activity is related to the same threat actor as the ArcaneDoor attack campaign that Cisco reported in early 2024.

While the vulnerable software is supported across other hardware platforms with different underlying architectures as well as in devices that are running Cisco Secure Firewall Threat Defense (FTD) Software, Cisco has no evidence that these platforms have been successfully compromised.

Cisco strongly recommends that customers follow the guidance provided to determine exposure and courses of action.

## Persistence Capability

During our forensic analysis of confirmed compromised devices, in some cases, Cisco has observed the threat actor modifying ROMMON to allow for persistence across reboots and software upgrades.

These modifications have been observed only on Cisco ASA 5500-X Series platforms that were released prior to the development of Secure Boot and Trust Anchor technologies; no CVE will be assigned to the lack of Secure Boot and Trust Anchor technology support on these platforms. Cisco has not observed successful compromise, malware implantation, or the existence of a persistence mechanism on platforms that support Secure Boot and Trust Anchors.

## Affected Cisco ASA 5500-X Series Models

The following Cisco ASA 5500-X Series models that are running Cisco ASA Software releases 9.12 or 9.14 with VPN web services enabled, which do not support Secure Boot and Trust Anchor technologies, have been observed to be successfully compromised in this campaign:

- 5512-X and 5515-X – Last Date of Support: August 31, 2022

- 5525-X, 5545-X, and 5555-X – Last Date of Support: September 30, 2025

- 5585-X – Last Date of Support: May 31, 2023

The following Cisco ASA 5500-X Series models, as well as all Cisco Firepower and Cisco Secure Firewall models, support Secure Boot and Trust Anchors:

- 5506-X, 5506H-X, 5506W-X, 5508-X, and 5516-X – Last Date of Support: August 31, 2026

No successful exploitation of these vulnerabilities and no modifications of ROMMON have been observed on these models. They are included here due to the impending end of support.

## Detecting this Attack

For information about detecting this attack, see Detection Guide for Continued Attacks against Cisco Firewalls by the Threat Actor behind ArcaneDoor . For further analysis to determine if there is potentially malicious activity, open a Cisco Technical Assistance Center (TAC) case.

## Recommended Actions

Step 1: Determine Device Model and Software Release

Refer to the tables provided in the Fixed Releases section of this page to determine if the software that is running on your device is affected by these vulnerabilities.

If you are running vulnerable software, proceed to Step 2.

Step 2: Assess the Device Configuration

Use the guidance provided in the security advisories listed in the Details section of this page to determine whether VPN web services are enabled on your device.

If VPN web services are enabled on your device, proceed to Step 3. If VPN web services are not enabled, your device is not affected by this vulnerability. Cisco still recommends that you upgrade to a fixed release.

Step 3: Remediate the Vulnerabilities

Option 1: Upgrade (recommended, long-term solution)

Cisco strongly recommends that customers upgrade to a fixed release to resolve the vulnerabilities and prevent subsequent exploitation.

If the device is vulnerable but cannot be upgraded due to end of life or support status, Cisco strongly recommends that the device be migrated to supported hardware and software.

Option 2: Mitigate (temporary solution only)

The risk can also be mitigated by disabling all SSL/TLS-based VPN web services. This includes disabling IKEv2 client services that facilitate the update of client endpoint software and profiles as well as disabling all SSL VPN services.

Disable IKEv2 Client Services

Disabling IKEv2 client-services will prevent VPN clients from receiving VPN client software and profile updates from the device, but IKEv2 IPsec VPN functionality will be retained otherwise.

Cisco Secure Firewall ASA Software

Disable IKEv2 client services by repeating the crypto ikev2 enable < interface_name > command in global configuration mode for every interface on which IKEv2 client services are enabled, as shown in the following example:

```
firewall# show running-config crypto ikev2 | include client-services crypto ikev2 enable outside client-services port 443 firewall# conf t firewall(config)# crypto ikev2 enable outside INFO: Client services disabled firewall(config)#
```

Cisco Secure FTD Software managed by Cisco Secure Firewall Management Center (FMC)

To disable IKEv2 client services, complete the following steps in the Cisco Secure FMC:

- Choose Devices > VPN > Remote Access .

- For each existing Remote Access VPN Policy do the following:

- Click the Edit icon.

- Open to the Advanced tab.

- Choose IPsec > Crypto Maps .

- For each crypto map listed do the following:

- Click the Edit icon.

- Uncheck Enable Client Services to disable IKEv2 client services.

- Click OK .

- Click Save .

- Deploy your changes.

Cisco Secure FTD Software managed by Cisco Secure Firewall Device Manager (FDM)

Cisco Secure FTD Software managed by Cisco Secure FDM does not support remote access IKEv2 IPsec VPN services.

Disable all SSL VPN Services

Important: All remote access SSL VPN features will cease to function after following this procedure.

Cisco Secure Firewall ASA Software

To disable all SSL VPN services, run the no webvpn command in global configuration mode, as shown in the following example:

```
firewall# conf t firewall(config)# no webvpn WARNING: Disabling webvpn removes proxy-bypass settings. Do not overwrite the configuration file if you want to keep existing proxy-bypass commands. firewall(config)#
```

Cisco Secure FTD Software managed by Cisco Secure FMC

To disable all SSL VPN services, complete the following steps in the Cisco Secure FMC:

- Choose Devices > VPN > Remote Access .

- For each existing Remote Access VPN Policy do the following:

- Click the Edit icon.

- Open the Access Interface tab.

- For each interface listed do the following:

- Click the Edit icon.

- Uncheck Enable SSL to fully disable SSL VPN services.

- Click OK .

- Click Save .

- Deploy your changes

Cisco Secure FTD Software managed by Cisco Secure FDM

To disable all SSL VPN services, complete the following steps in the Cisco Secure FDM:

- Choose Device > Remote Access VPN > View Configuration .

- For all Remote Access VPN Connection Profiles listed, click the trash icon in the Actions column and confirm with OK .

- Deploy your changes.

Step 4: Recover Potentially Compromised Devices

For Cisco ASA 5500-X Series devices that do not support Secure Boot (5512-X, 5515-X, 5525-X, 5545-X, and 5555-X), booting a fixed release will automatically check ROMMON and remove the persistence mechanism that was observed in this attack campaign if it is detected. When the persistence mechanism is detected and removed, a file called firmware_update.log is written to disk0: (or appended to if the file exists) and the device is rebooted to load a clean system immediately afterwards.

In cases of suspected or confirmed compromise on any Cisco firewall device, all configuration elements of the device should be considered untrusted. Cisco recommends that all configurations – especially local passwords, certificates, and keys – be replaced after the upgrade to a fixed release. This is best achieved by resetting the device to factory defaults after the upgrade to a fixed release and then reconfiguring the device from scratch with new passwords, and re-generated certificates and keys.

If the file firmware_update.log is found on disk0: after upgrade to a fixed release, customers should open a case with the Cisco TAC with the output of the show tech-support command and the content of the firmware_update.log file.

Resetting a Device to Factory Defaults

Cisco Secure Firewall ASA Software

To reset a device that is running Cisco Secure Firewall ASA Software to factory default, use the configure factory-default command in global configuration mode. If the configure factory-default command should not be supported, use the commands write erase and then reload instead.

Cisco Secure FTD Software

To reset a device that is running Cisco Secure FTD Software, follow the guidance in the following documents:

- Reimage a Secure FTD for 1000, 2100, and 3100 Series

- Perform a Complete Reimage for FXOS in Firepower 4100 and 9300 Series

Cisco Secure FTD Virtual devices must be re-deployed.

## Current Status

The software updates that are identified in the advisories in the following table address bugs that, when chained together, could allow an unauthenticated, remote attacker to gain full control of an affected device. The evidence collected strongly indicates that CVE-2025-20333 and CVE-2025-20362 were used by the attacker in the current attack campaign.

The persistence capability observed does not affect devices that support Secure Boot technology. Cisco assesses with high confidence that upgrading to a fixed software release will break the threat actor's attack chain and strongly recommends that all customers upgrade to fixed software releases.

## Details

On September 25, 2025, Cisco released the following Security Advisories that address weaknesses that were leveraged in these attacks:

## Fixed Releases

In the following tables, the left column lists Cisco software releases. The middle columns indicate the first fixed release for each vulnerability. The right column indicates the first fixed release for all vulnerabilities in the advisories that are listed on this page. Customers are advised to upgrade to an appropriate fixed software release as indicated in this section.

Notes:

- The fixed release for Cisco Secure ASA Software Release 9.12 is 9.12.4.72. It is available from the Cisco Software Download Center .

- The fixed release for Cisco Secure ASA Software Release 9.14 is 9.14.4.28. It is available from the Cisco Software Download Center .

1. A code change prior to CSCwq79815 removed the endpoints that were affected by this vulnerability. However, Cisco has also patched CSCwq79815 in addition for defensive posture, the fixed releases in this table should be considered as the confirmed first fixed release for CVE-2025-20333 for each code train.

2. Cisco Secure FTD Release 7.4.3 also contains the fixes for the ArcaneDoor campaign, but it is not required to install Release 7.4.3 on top of Release 7.4.2.4 to fix these vulnerabilities.

## Additional Information

For more information about detecting this attack, see Detection Guide for Continued Attacks against Cisco Firewalls by the Threat Actor behind ArcaneDoor . For further analysis if potentially malicious activity is identified, open a Cisco TAC case.

The Snort rule for CVE-2025-20333 is 65340 and the Snort rule for CVE-2025-20362 is 46897 .

All customers are advised to upgrade to a fixed software release.

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Cisco Security Advisory | CVE ID | Security Impact Rating | CVSS Base Score |
|---|---|---|---|
| Cisco Secure Firewall Adaptive Security Appliance Software and Secure Firewall Threat Defense Software VPN Web Server Remote Code Execution Vulnerability | CVE-2025-20333 | Critical | 9.9 |
| Cisco Secure Firewall Adaptive Security Appliance, Secure Firewall Threat Defense Software, IOS Software, IOS XE Software and IOS XR Software HTTP Server Remote Code Execution Vulnerability | CVE-2025-20363 | Critical | 9 |
| Cisco Secure Firewall Adaptive Security Appliance Software and Secure Firewall Threat Defense Software VPN Web Server Unauthorized Access Vulnerability | CVE-2025-20362 | Medium | 6.5 |

| Cisco ASA Software Release | First Fixed Release for CVE-2025-20333 1 Critical | First Fixed Release for CVE-2025-20363 Critical | First Fixed Release for CVE-2025-20362 Medium | First Fixed Release for all of These Vulnerabilities |
|---|---|---|---|---|
| 9.16 | 9.16.4.85 | 9.16.4.84 | 9.16.4.85 | 9.16.4.85 |
| 9.17 | 9.17.1.45 | Migrate to a fixed release. | Migrate to a fixed release. | Migrate to a fixed release. |
| 9.18 | 9.18.4.47 | 9.18.4.57 | 9.18.4.67 | 9.18.4.67 |
| 9.19 | 9.19.1.37 | 9.19.1.42 | Migrate to a fixed release. | Migrate to a fixed release. |
| 9.20 | 9.20.3.7 | 9.20.3.16 | 9.20.4.10 | 9.20.4.10 |
| 9.22 | 9.22.1.3 | 9.22.2 | 9.22.2.14 | 9.22.2.14 |
| 9.23 | Not vulnerable. | 9.23.1.3 | 9.23.1.19 | 9.23.1.19 |

| Cisco FTD Software Release | First Fixed Release for CVE-2025-20333 1 Critical | First Fixed Release for CVE-2025-20363 Critical | First Fixed Release for CVE-2025-20362 Medium | First Fixed Release for all of These Vulnerabilities |
|---|---|---|---|---|
| 7.0 | 7.0.8.1 | 7.0.8 | 7.0.8.1 | 7.0.8.1 |
| 7.1 | Migrate to a fixed release. | Migrate to a fixed release. | Migrate to a fixed release. | Migrate to a fixed release. |
| 7.2 | 7.2.9 | 7.2.10 | 7.2.10.2 | 7.2.10.2 |
| 7.3 | Migrate to a fixed release. | Migrate to a fixed release. | Migrate to a fixed release. | Migrate to a fixed release. |
| 7.4 2 | 7.4.2.4 | 7.4.2.3 | 7.4.2.4 | 7.4.2.4 |
| 7.6 | 7.6.1 | 7.6.1 | 7.6.2.1 | 7.6.2.1 |
| 7.7 | Not vulnerable. | 7.7.10 | 7.7.10.1 | 7.7.10.1 |