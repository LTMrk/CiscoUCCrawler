---
doc_id: sec-cloudapps-cisco-com-security-center-resources-understanding-terminology-html-0105b2bb9e
source_url: https://sec.cloudapps.cisco.com/security/center/resources/understanding-terminology.html
retrieved_at: 2026-09-01T14:09:55.151203+00:00
---

Home / Cisco Security

Understanding Terminology in Cisco Security Advisories

# Understanding Terminology in Cisco Security Advisories

Introduction Background Knowledge Exploitability Metrics Attack Vector Attack Complexity Privileges Required User Interaction Scope Impact Metrics Confidentiality Integrity Availability Reading and Understanding Sections of a Security Advisory Summary Affected Products Workarounds and Mitigations Fixed Software Exploitation and Public Announcements Source A Methodology for Organizing Vulnerability Details Conclusion Glossary of Terms Additional Resources

## Introduction

The Cisco Product Security Incident Response Team (PSIRT) manages the receipt, investigation, and public disclosure of security vulnerability information that is related to Cisco products and networks. Cisco Security Advisories (SAs) provide detailed information about security issues that directly involve Cisco products and that also require an upgrade, fix, or other customer action. Cisco SAs use a common set of terms across all of the advisories that describe the characteristics of vulnerabilities. Characteristics such as whether the vulnerability is remotely exploitable, the software versions are affected, patches are available, and any other actions that can be taken to minimize the impact of the vulnerability.

This document defines the terms used in Cisco SAs. The SAs represent the severity of a vulnerability to help customers understand how these vulnerability characteristics might impact risk to their individual network environments. A vulnerability that is assigned a severity of Critical in the SA may represent a low overall risk if there are no affected devices in the network environment. Therefore, understanding the advisories is the first step in facilitating effective communication about the vulnerability with system owners who will be deploying software updates and top-level executives who are concerned about risk.

Understanding SAs and communicating risk to stakeholders can become a daunting task unless it can be done at scale. Therefore, this document will show via the Cisco PSIRT openVuln API how to gather and organize large sets of vulnerability information that is relevant to a specific need.

Cisco SAs provide the severity of an individual vulnerability. The complete assessment of risk must be done by someone with institutional knowledge and, therefore, is not within the scope of this document. However, network operators and those with institutional knowledge of the assets being evaluated can use the CVSSv3 Environmental Metrics along with the Base Score Metrics found in the Cisco SAs to form a more complete picture of the overall risk to their organization.

## Background Knowledge

The Common Vulnerability Scoring System (CVSSv3) provides an open framework for communicating the characteristics and impacts of Information Technology vulnerabilities. Cisco leverages this framework to evaluate the severity of a vulnerability and also to describe  vulnerabilities in a standard way. Cisco uses both  CVSSv3 scoring and a proprietary Security Impact Rating in  Cisco Security Advisories. Using this information, customers can have a basis for deciding how the vulnerability impacts the risk to any specific deployment scenario.

CVSSv3 uses three categories of metrics to score the severity of a vulnerability from 0 to 10, where 10 is the highest possible vulnerability score. The three metric categories include:

- Base Score Metrics

- Temporal Score Metrics

- Environmental Score Metrics

This document will focus mostly on the Base Score Metrics because these metrics constitute the bulk of the evaluation of severity in a new vulnerability announced via  Cisco Security Advisories.

The base score metrics can be seen in Figure 1.

Figure 1. Base Score Metrics

Understanding the Base Score Metrics is critical for the understanding of Cisco SAs; therefore, a brief description of these metrics would be helpful here. The base metrics represent the intrinsic characteristics that will not change over time or within a specific deployment scenario. Rarely, Cisco PSIRT will update an existing SA because there are newly discovered intrinsic characteristics of an existing vulnerability. Keep in mind while reading the metrics below that a CVSS Base score of 10 is the highest score and a score of 0 is the lowest score. Base Score Metrics have two categories: Exploitability Metrics and Impact Metrics.

## Exploitability Metrics

Exploitability Metrics describe the thing (software, hardware, etc.) that is vulnerable and generically can be described in Cisco SAs as the vulnerable product . Cisco SAs  provide details about the impacted platforms or software versions, or both, and for this reason the phrase vulnerable product is generally used. When Cisco PSIRT scores a vulnerability, it is scored with the assumption that the vulnerable product is already configured in such a way as to be vulnerable. Any configuration changes or infrastructure that can be described as a workaround or a mitigation are described in the SA as well, but do not impact the base score.

### Attack Vector

The Attack Vector (AV) describes the shortest distance of the attacker relative to the vulnerable product. The Physical attack vector would score a different severity than a Network attack vector because the number of attackers who are physically proximate to a vulnerable product is usually a smaller number than the number of possible attackers who can reach a vulnerable product over a network. With all other metrics being the same, the actual overall vulnerability score could be higher or lower depending on the other metrics being evaluated.

### Attack Complexity

The Attack Complexity is described as High if conditions beyond the control of an attacker need to be in place in order for the attack to succeed. For example, a single HTTP packet causing a web service to crash would score as a Low complexity. If the same device in a different scenario can be crashed with the same packet, however, in this new scenario 100 TCP connections need to  be established for the packet to cause a crash, the complexity could be described as High.

### Privileges Required

The metric values of High, Low, and None reflect the privileges required by an attacker to exploit the vulnerability. The higher the privileges required, the lower the overall severity.

### User Interaction

If a user other than the attacker is needed to exploit the vulnerability, the user interaction is described as Required. If no interaction is needed, the overall score will be higher than if another user is needed.

### Scope

When a vulnerability in one product can expose upstream or downstream resources to the impact of a successful exploit of the vulnerability, the scope is considered Changed. A practical example of this is when a successfully exploited vulnerability in BGP on one device exposes the BGP peers to complete or partial instability. Therefore, a scope of Changed will have a severity score higher than a scope of Unchanged.

## Impact Metrics

Impact Metrics represent the effects of a worst-case scenario on the impacted product. Although the scenario is worst-case, at the same time the outcome must reflect a reasonable and predictable outcome. In other words, if a reasonable and predictable worst-case outcome in a specific vulnerability is read access to a filesystem, that read access will be scored differently than a worst-case scenario of read and write access to a filesystem. The categories below should make this clear.

### Confidentiality

When a successfully exploited vulnerability discloses restricted information, the disclosure can be None, Low, or High depending on the scope of the disclosure. An example of a Low scored Confidentiality metric would be the exposure of an administrator username and password that has a highly improbable likelihood of ever being used. Likewise, an example of a High score would be the exposure of an administrator username and password used on the external interface of home routers.

### Integrity

Integrity refers to the ability to change data and thereby impact the trustworthiness and veracity of the impacted product. For example, if a successfully exploited vulnerability caused the ability to modify logs on the impacted product and the modification resulted in serious consequences such as logging all usernames and passwords in cleartext, the Integrity metric would be High.

### Availability

Confidentiality and Integrity describe the probable loss of data in a product. Availability describes if the product is still available after a successful exploit of the vulnerability. For example, if a single malicious email attachment causes a mail server to go completely offline, the Availability metric will be High.

## Reading and Understanding Sections of a Security Advisory

The beginning section of the Security Advisory contains the Security Advisory title, the Cisco bug IDs, the Security Impact Rating (SIR), and the CVSS base score. The Title will contain the product impacted and a short description of the vulnerability. The SIR is not labeled as such but is found inside the colored circle in the header of the document. Figure 2 shows the Security Advisory header with the SIR.

Figure 2. Security Advisory Header with Security Impact Rating (SIR)

The values of a SIR in a Security Advisory can be Critical, High, Medium and Low. The following table shows the mapping between the SIR and the CVSSv3 base score:

Figure 3. Mapping Between SIR and CVSS

Occasionally, Cisco PSIRT will apply a SIR that is higher or lower than the CVSS score would indicate. A SIR that is higher than the equivalent CVSS score happens when circumstances are such that the ease of exploitation or the wide adoption of a technology warrant a higher level of awareness.

### Summary Section

The Summary section of the Security Advisory contains details about the Exploitability Metrics and the Impact Metrics covered above. Again, we will use the vulnerability CVE-2019-15992 as an example. In Figure 4 below, the metrics are called out in red to illustrate where the metrics can be found in a readable format.

Figure 4. Summary Section of a Security Advisory

### Affected Products

The Affected Products section informs the reader of the versions of a product that are impacted by the vulnerability, the versions not impacted, or both. It will also contain any  relevant context for the reader that may help them understand the severity of a vulnerability. The Affected Products section  may also contain ways to identify whether a product has a vulnerable configuration. Common identification methods include:

- Product versions that are vulnerable

- Product versions that are not vulnerable

- Specific CLI commands that will generate output indicating if a product is vulnerable

### Workarounds and Mitigations

When a vulnerability has a workaround, it will be listed in this section with any specific configuration commands needed. A workaround is considered as such only if it is something that:

- Can be done locally on the vulnerable device AND

- Eliminates the vulnerability

A workaround is not a fix. If a workaround is mistakenly removed manually or via automation, it will once again expose the attack surface outlined in the advisory. Therefore, software updates are the preferred method of resolution.

Mitigations will also be in this section of the Security Advisory. Mitigations are actions that can be taken to minimize the attack surface, or reduce the damage resulting from a successful exploitation of a vulnerability. For example, if a product has a vulnerable management GUI, controlling access by allowing only a single management IP address to use the GUI could be a practical mitigation. Again, using a fixed version of hardware or software is the preferred method of resolving a vulnerability.

### Fixed Software

If a fixed software release is available, this section  shows the fixed release versions, how to find the fixed versions, and  any related support documentation for the product.

### Exploitation and Public Announcements

If a vulnerability is actively being exploited, this section  provides the scope of the exploitation and the context of the exploitation.

### Source

This section  details how Cisco became aware of the vulnerability. Common scenarios include Cisco internal teams finding the vulnerability, resolution of support cases by the Cisco Technical Assistance Center (TAC), customers finding the issue, or  external security researchers finding vulnerabilities.

## A Methodology for Organizing Vulnerability Details

System owners are commonly presented with frequent security advisories and need a way of importing and organizing large amounts vulnerability data so that effective risk triage can take place. The properties below are some of the most fundamental data points needed from Cisco SAs:

- The CVSS Base Score

- The Security Impact Rating (SIR)

- The Summary section of the security advisory

- The first fixed release of code

A common scenario for system owners is when they have a stable version of an operating system and need to know what vulnerabilities impact that version of code. They need to triage vulnerabilities by CVSS Base Score, SIR, or both. Because system owners understand the specifics of their environment, reading the Summary section of the advisory will most likely be enough information to rule in or rule out a remediation effort.

Using the scenario above, the following is an example of using the Cisco PSIRT openVuln API to gather all vulnerabilities in IOS-XE version 16.6.3 that have a SIR of Medium, High, or Critical. The CVSS Base score, the vulnerability Summary, and the first fixed release of code is pulled from the API and placed into a .CSV file along with the publication URL in case more details are needed.

```
(py3-vulnapi) Jermysmac:$ openVulnQuery --ios_xe 16.6.3 --fields summary first_fixed publication_url cvss_base_score sir  --csv iosxe1663.csv --conf creds.json
```

The output below shows six lines of output from a file containing 45 vulnerabilities.

Figure 5. Cisco openVuln API

As you can see, the Cisco PSIRT openVuln API can quickly gather large amounts of relevant vulnerabilities and organize them for risk triage and communicating severity to other stakeholders. Machine-consumable formats are also available. To get started with the openVuln API,  see the DevNet documentation .

## Conclusion

Cisco Security Advisories contain information about specific software and hardware vulnerabilities, the Cisco product versions affected, and any software updates that will fix the vulnerability. Software updates are the preferred method of resolution; however, workarounds and mitigations are a viable alternative when considering the resources required to update hardware and software. Customers can use the Security Impact Rating, the summary description of the vulnerability, CVSS Base Score, and institutional knowledge of the assets to assess risk and prioritize the operational resources used to update software and hardware.

When the vulnerability information needs to be consumed at scale, the Cisco PSIRT openVuln API can be used to effectively manage specific data points that are relevant for any given scenario or environment.

## Glossary of Terms

unauthenticated attack : An attack that does not require authentication to the vulnerable device prior to carrying out the attack. This metric does not gauge the strength or complexity of the authentication process, only that an attacker is not required to provide credentials before an exploit may occur.

authenticated attack : An attack where credentials that exist must be provided prior to the attack. These credentials can be of any strength or complexity and exist either locally on the vulnerable device or on a remote authentication database.

network attack : An attack that must be bound to the network stack, and one or more layer 3 hops must separate the source of the attack and the destination of the attack. A network attack could originate from any routable origin, including networks internal and external to an organization. Proper access controls will mitigate but not completely prevent the attack.

adjacent attack : An attack that originates from the same layer 2 domain as the victim device. Examples of local networks include Bluetooth, 802.1x, and IEEE 802.11.

local attack : An attack on a vulnerability that is not bound to the network stack and the attacker’s path is via read/write/execute capabilities. Additionally, the attacker exploits the vulnerability by accessing the target system locally (e.g., keyboard, console), or remotely (e.g., SSH); or the attacker relies on User Interaction by another person to perform actions required to exploit the vulnerability (e.g., using social engineering techniques to trick a legitimate user into opening a malicious document). Examples of locally exploitable vulnerabilities are peripheral attacks such as USB Direct Memory Attacks (DMA), and local privilege escalations.

physical attack : An attack that requires the attacker to interact physically with the vulnerable device to successfully attack the device.

denial of service : When a vulnerable system or service is effectively unavailable to users of the system. Examples include an unexpected (crafted) packet causing a system to crash. If a device is performing under conditions that are beyond the upper threshold of the product specifications and the product becomes unavailable and then goes back to normal operating conditions when within specification, Cisco does not consider this a denial of service vulnerability. Therefore, these types of denial of service attacks are not in Cisco Security Advisories.

crafted packet : A packet that has been specifically created or altered after creation by human action. By definition, a crafted packet should not be seen during the normal operation of a network.

malformed packet : A packet that cannot be processed according to specification. These packets are usually discarded. An example of a malformed packet is an IGMP null payload packet that is less than 28 bytes long. A normal IGMP packet consists of a 20-byte IP header and an 8-byte IGMP body.

command injection : An attack where arbitrary commands are sent to the host operating system via a vulnerable application. For example, if a web interface on a router accepts user supplied data (forms, cookies, HTTP headers etc.) and passes it to a system shell. Command injection attacks are mostly due to insufficient input validation.

static credentials : Also called hard-coded credentials and can be any of the following:

- plaintext passwords

- hashed passwords

- authorized keys

- PEM formatted key files

- default credentials still enabled in a fully functional system

Static credentials can be used for inbound authentication or outbound communication to external components such as database replication or encryption of internal data. Static credentials are usually high risk because they allow an attacker to bypass standard authentication mechanisms and usage can also be difficult to detect.

privilege escalation : Occurs when privileges are attained beyond what is intended by a system or system administrator. Generally speaking, vulnerabilities that allow privilege escalation allow regular, authenticated users to obtain a privilege or privileges that are usually reserved for administrators or System accounts.

cross-site request forgery : An attack where a victim is tricked into performing actions in an application that the victim is using. For example, if an administrator of a vulnerable application receives a link (via text or email) from an attacker which, when executed, causes a compromise of the application. Examples of a compromise can be a new administrative user created or another configuration change that furthers the attacker’s goals.

SQL injection : These attacks happen when SQL commands are inserted into an application and sent to the SQL database. The intent of the attack can be to reveal database information or cause a denial of service.

container escape : Containers are applications or processes that have their own namespaces. Namespaces may include routing tables, authentication sources and other resources managed by different tenants in a multiple container environment. Important for this definition is the concept of an attacker compromising one container and then expanding the footprint of the attack. For example, an attacker could install a custom container which in turn gains root access on a physical machine or cluster of machines belonging to other tenants.

access control list (ACL) : Access control lists, or ACLs, are filtering mechanisms present on many network devices. ACLs may be in a Cisco SA workaround section. ACLs permit or deny network traffic based on the Layer 3 or Layer 4 characteristics of the packet. For example, the following ACL excerpt from a Cisco IOS device denies telnet traffic on TCP port 23, but allows SSH traffic on TCP port 22.

access-list 100 deny tcp any any eq 23 access-list 100 permit tcp any any eq 22

Once created, ACLs used for traffic filtering are applied to network interfaces in either the inbound or outbound direction.

infrastructure access control list : A technique through which ACLs are applied around the outside of a network. iACLs may be in a Cisco SA workaround section when applicable. Infrastructure ACLs aim to filter incoming network traffic that is targeted to the network itself while allowing all other traffic to travel across the network.

control plane policing (CoPP) : A security feature on Cisco IOS devices that permits, denies, or rate limits network traffic to a network device. CoPP filters traffic to a network device, but not through it. In the context of security advisories, CoPP allows us to deny certain, potentially malicious, traffic on a network device without applying an ACL to all interfaces on the device. This single point of application coupled with the characteristic that it only affects traffic to the device makes CoPP a viable mitigation when the device itself has a vulnerability.

## Additional Resources

Cisco Security Advisories

https://sec.cloudapps.cisco.com/security/center/publicationListing.x

Risk Triage for Security Vulnerability Announcements

https://sec.cloudapps.cisco.com/security/center/resources/vulnerability_risk_triage.html

CVSS Usage Within Cisco

https://sec.cloudapps.cisco.com/security/center/resources/cvss.html

CVSSv3.1 Specification Guide

https://www.first.org/cvss/v3.1/specification-document

CVSSv3.1 Calculator

https://www.first.org/cvss/calculator/3.1

Cisco PSIRT Vulnerability Policy

https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html

Cisco PSIRT openVuln API

https://developer.cisco.com/docs/psirt/#!overview

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top