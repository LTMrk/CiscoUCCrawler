---
doc_id: sec-cloudapps-cisco-com-security-center-resources-asa-ftd-attacks-event-response-a09daf6b9a
source_url: https://sec.cloudapps.cisco.com/security/center/resources/asa_ftd_attacks_event_response
retrieved_at: 2026-09-01T14:08:52.994590+00:00
---

Home / Cisco Security

Cisco Event Response: Attacks Against Cisco Firewall Platforms

# Cisco Event Response: Attacks Against Cisco Firewall Platforms

# Summary

In early 2024, the Cisco Product Security Incident Response Team (PSIRT) became aware of attacks that were targeting certain devices that were running Cisco Adaptive Security Appliance (ASA) Software or Cisco Firepower Threat Defense (FTD) Software to implant malware, execute commands, and potentially exfiltrate data from the compromised devices.

This attack campaign has been named ArcaneDoor. Although Cisco has not yet identified the initial attack vector, the software updates that are identified in the advisories in the following table  address software weaknesses that could allow an attacker to implant malware and obtain persistence on an affected device. Of these software weaknesses, CVE-2024-20353 and CVE-2024-20359 were used by the attacker in this attack campaign.

Cisco strongly recommends that all customers upgrade to fixed software versions.

IMPORTANT: For customers seeking a 7.2 train fixed version of code, please upgrade to 7.2.5.2 or 7.2.7; this guidance has changed due to a bug in 7.2.6. Refer to this Upgrade TechNote for further guidance.

# Details

On April 24, 2024, Cisco released the following Cisco ASA and FTD Software Security Advisories that address weaknesses that were leveraged in these attacks:

# Additional Information

For more information on the ArcaneDoor campaign, see the Cisco Talos Threat Advisory ArcaneDoor: New espionage-focused campaign targets perimeter network devices .

All customers are advised to upgrade to a fixed software release.

Customers  can use the Cisco  Support Assistant to verify the integrity of their Cisco ASA or FTD  devices.

Notes:

- If the device is deployed in Cisco FTD mode, run the system support diagnostic-cli command and then the enable command first.

- If the device is deployed in multi-context mode, log in to the admin context and change to the system context first.

Back to Top

| Cisco Security Advisory | CVE ID | Security Impact Rating | CVSS Base Score |
|---|---|---|---|
| Cisco Adaptive Security Appliance and Firepower Threat Defense Software Web Services Denial of Service Vulnerability | CVE-2024-20353 | High | 8.6 |
| Cisco Adaptive Security Appliance and Firepower Threat Defense Software Persistent Local Code Execution Vulnerability | CVE-2024-20359 | High | 6.0 |
| Cisco Adaptive Security Appliance and Firepower Threat Defense Software Command Injection Vulnerability | CVE-2024-20358 | Medium | 6.0 |