---
doc_id: sec-cloudapps-cisco-com-security-center-resources-principles-secure-operations-c36411306b
source_url: https://sec.cloudapps.cisco.com/security/center/resources/principles_secure_operations
retrieved_at: 2026-09-01T14:09:34.525544+00:00
---

Home / Cisco Security

Principles of Secure Operations

# Principles of Secure Operations

Updated: June 11, 2026

### Contents

Introduction Prerequisites Cisco Security Advisories and Responses Secure Boot and Image Verification Securing the Management Plane Disabling Unused Services Setting the EXEC Timeout Value Using Management Interfaces Limiting Access to the Network with Infrastructure ACLs Filtering ICMP Packets Filtering IP Fragments Securing Interactive Management Sessions Encrypting Management Sessions Securing the Console Port, Auxiliary Port, and Connectivity Management Processor Controlling vty Lines Displaying Warning Banners Using AAA Authentication using TACACS+, RADIUS, and LDAP TACACS+ over TLS 1.3 Authentication Fallback TACACS+ Command Authorization Accounting Redundant AAA Servers Configuring Strong Passwords Recommendations for Creating Strong Passwords Password Security Basics Securing SNMP SNMP Version 3 SNMP Community Strings SNMP Community Strings with ACLs iACLs Performing Configuration Management Logging Best Practices Send Logs to a Central Location Assign Logging Level Do Not Log to Console or Monitor Sessions Log to the Log File Configure Logging Source Interface Configure Logging Time Stamps Securing the Control Plane IP ICMP Redirect Messages ICMP Unreachable Messages Proxy Address Resolution Protocol NTP Limiting the Effect of Control-Plane Traffic on the CPU Securing the Data Plane Limiting the Effect of Data-Plane Traffic on the CPU Disabling IP Source Routing Disabling ICMP Redirect Messages Disabling or Limiting IP Directed Broadcasts Filtering ICMP Packets Filtering IP Fragments Using IP Source Guard Using Port Security Traffic Identification and Traceback NetFlow Classification ACLs Access Control with VLAN Maps and PACLs Access Control with VLAN Maps Access Control with MAC Address ACLs Conclusion Appendix OS-Specific Guide Links References Revision History

# Introduction

This document contains information to help administrators secure, or harden, Cisco devices running NX-OS, IOS XE, or IOS XR Software to increase the overall security posture of a network. The document is organized according to the three planes into which functions of a network device can be categorized:

- Management plane: The management plane contains the logical group of all traffic that supports provisioning, maintenance, and monitoring functions for the Cisco device and the network. Traffic in this group includes SSH, Secure Copy Protocol (SCP), Simple Network Management Protocol (SNMP), syslog, TACACS+, RADIUS, NetFlow, and Cisco Discovery Protocol (CDP). Management plane traffic is always destined for the local Cisco device.

- Control plane: The control plane of a network device processes the traffic that is important for maintaining the functions of the network infrastructure. The control plane consists of applications and protocols between network devices, including Border Gateway Protocol (BGP) and Interior Gateway Protocols (IGPs) such as EIGRP and OSPF, as well as DNS.

- Data plane: The data plane forwards data through a network device. The data plane does not include traffic that is sent to the local Cisco device.

Although most of this document is devoted to the secure configuration of Cisco devices, configurations alone do not completely secure a network. The operating procedures in use on the network contribute as much to security as the configuration of the underlying devices.

This document contains operation recommendations that network administrators are advised to implement. However, note that this document focuses on critical areas of network operations and is not comprehensive.

## Prerequisites

Engineers and administrators should possess a Cisco Certified Network Associate (CCNA)-level knowledge of the basic configuration options available. Configuration examples and more advanced topics are covered in the following guides:

- Cisco IOS XE Software Hardening Guide

- Cisco IOS XR Software Hardening Guide

- Cisco NX-OS Software Hardening Guide

## Cisco Security Advisories and Responses

The Cisco Product Security Incident Response Team (PSIRT) creates and maintains publications, commonly referred to as security advisories, for security-related concerns in Cisco products. Security advisories are available at http://www.cisco.com/go/psirt . For additional information about security-related communications, see the Cisco Security Vulnerability Policy .

Being aware of Cisco security advisories and responses is essential to maintaining a secure network. In addition, administrators must obtain knowledge of a vulnerability prior to evaluating its threat to a network. For assistance with this evaluation process, refer to Risk Triage for Security Vulnerability Announcements .

## Secure Boot and Image Verification

Administrators should ensure they are using a legitimate copy of software by verifying digital signatures before installing. Cisco Secure Boot will ensure that images not matching the digital signatures cannot be installed.

# Securing the Management Plane

The management plane consists of functions that achieve the management goals of the network. These goals include interactive management sessions using SSHv2 and statistics-gathering with tools and protocols such as SNMPv3, NetFlow, and gRPC Network Management Interface (gNMI). When considering the security of a network device, make sure that the management plane is protected. If a security incident undermines the functions of the management plane, recovering or stabilizing the network will be a challenge.

The management plane is used to access, configure, and manage a device, in addition to monitoring its operations and the network on which it is deployed. The management plane receives and sends traffic to support the operations of the following functions:

- FTP (Do not use)

- HTTP (Do not use)

- HTTPS

- NetFlow

- NTP

- RADIUS

- Rlogin (Do not use)

- SCP

- Secure LDAP

- SFTP

- SNMPv1, v2, and v3 (Do not use v1 or v2)

- SSHv2 (Do not use v1)

- Syslog

- TACACS+

- TACACS+ over TLS 1.3

- Telnet (Do not use)

- TFTP (Do not use)

Use secure protocols whenever possible. For example, use SSHv2 instead of Telnet so that both authentication data and management information are encrypted. To secure file transfer protocols when configuration data is moved or copied among the devices in a network environment, use SCP instead of TFTP or FTP.

Both the management and control planes of a device must be secured because the operation of these planes directly affects the overall operation of the device. Take steps to help ensure the survival of the management and control planes during security incidents. If one of these planes is exploited, all planes can be compromised.

## Disabling Unused Services

As a general security best practice, disable any unnecessary services. Each operating system will have different default settings for what is enabled and disabled. System admins should be aware of the default settings for each operating system in use.

SSHv2 and SNMPv3 are essential services for running and managing a network. If needed, they can be individually disabled.

Telnet should be disabled. Cisco recommends using SSHv2 instead of Telnet for security reasons.

Cisco Discovery Protocol (CDP) is a network protocol that is used to discover other devices enabled for CDP for neighbor adjacency and to map a network topology. It can be used by network management systems or during troubleshooting. CDP can be exploited by malicious users for reconnaissance and network mapping, so it should be disabled if it is not required.

Link Layer Discovery Protocol (LLDP) is an IEEE protocol defined in the IEEE 802.1AB standard. LLDP is similar to CDP, but it allows interoperability between devices not supported by CDP. Like CDP, LLDP has the potential to be exploited by malicious users for reconnaissance and network mapping, so it should be disabled if it is not needed.

## Setting the EXEC Timeout Value

Setting an EXEC timeout value is highly recommended. The default value for the operating system may be longer than the company's security policy allows.

## Using Management Interfaces

The management plane of a device can be accessed in-band or out-of-band on a physical or logical management interface. Ideally, both in-band and out-of-band management access exists to provide redundancy so that the management plane can be accessed in the event of a network outage.

One of the most common interfaces used for in-band access to a device is the loopback interface. Loopback interfaces are logical and are therefore always up, whereas physical interfaces can change state, making the interface potentially inaccessible.

Add a loopback interface as a management interface to each device. This interface should be used exclusively for the management plane. This approach allows administrators to apply policies throughout the network for the management plane. After the loopback interface is configured on a device, it can be used by management plane protocols such as SSHv2, SNMP, and syslog to send and receive traffic.

## Limiting Access to the Network with Infrastructure ACLs

Infrastructure access control lists (iACLs) are one of the most critical security controls that can be implemented in networks. They prevent unauthorized direct communication to network devices. iACLs use the idea that all network traffic simply traverses the network and is not destined for the network itself.

The key to an iACL is its construction. iACLs are built on the premise of permitting connections among trusted hosts or networks that require communication with network infrastructure devices according to established security policies and configurations. This required communication typically consists of management- and control-plane traffic. Common examples of these types of connections are external BGP (eBGP), SSHv2, and SNMP. After the required connections have been permitted, all other traffic to the infrastructure is explicitly denied.

All transit traffic that crosses the network and is not destined for infrastructure devices is then explicitly permitted. This permission typically occurs through a transit access control list (tACL), which is discussed later in this document.

iACLs protect both the management and control planes. The implementation of iACLs can be made easier through the use of distinct addressing for network infrastructure devices. For more information about the security implications of IP addressing, see the Cisco white paper A Security-Oriented Approach to IP Addressing .

For the strongest protection of infrastructure devices, deployed iACLs should be applied in the ingress direction on all interfaces for which an IP address has been configured, including interfaces that connect to other organizations, remote access segments, user segments, and segments in data centers. Note that an iACL cannot provide complete protection against vulnerabilities when the attack originates from a trusted source address.

## Filtering ICMP Packets

The ICMP was designed as an IP control protocol. As such, the messages it conveys can have far-reaching ramifications for TCP and IP in general. Although the network troubleshooting tools ping and traceroute use ICMP, external ICMP connectivity is rarely needed for the proper operation of a network.

## Filtering IP Fragments

The filtering of fragmented IP packets can pose a challenge to infrastructure and security devices alike. This challenge exists because the Layer 4 information that is used to filter TCP and UDP packets is present only in the initial fragment.

Due to the nonintuitive nature of fragment handling, many access control lists (ACLs) inadvertently permit IP fragments, and attackers use fragmentation in attempts to evade intrusion detection systems. For these reasons, IP fragments are often used in attacks, and so they must be explicitly filtered at the top of any configured iACLs.

## Securing Interactive Management Sessions

Management sessions for devices allow administrators to view and collect information about a device and its operations. If this information is disclosed to a malicious user, the device can be attacked, compromised, and commandeered to perform additional attacks. Anyone with privileged access to a device could get full administrative control of that device. Securing management sessions is imperative to prevent information disclosure and unauthorized access.

### Encrypting Management Sessions

Because information can be disclosed during an interactive management session, this traffic must be encrypted so that a malicious user cannot gain access to the data being transmitted. Encrypting the traffic allows for a secure remote access connection to the device. If the traffic for a management session is sent over the network in clear text, an attacker can obtain sensitive information about the device and the network.

Use SSHv2 to establish an encrypted and secure remote access management connection to a device.

### Securing the Console Port, Auxiliary Port, and Connectivity Management Processor

In Cisco devices, console and auxiliary (AUX) ports are asynchronous lines that can be used for local and remote access to a device. Console ports on Cisco devices have special privileges that allow an administrator to perform the password recovery procedure. To perform password recovery, an unauthenticated attacker would need to have access to the console port and the capability to interrupt power to the device or to cause the device to fail.

Any method used to access the console port of a device must be secured with a security level that is equal to the security that is enforced for privileged access to a device. The configuration of authentication, authorization, and accounting (AAA) authentication methods and policies for the login mechanism will automatically apply to the console, AUX port, and virtual tty (vty) access methods.

The AUX port (also called com1), when available, cannot be explicitly disabled. Therefore, AAA must be properly configured globally on the platform to secure the AUX port as well. In addition, it is highly recommended that physical security measures be applied to restrict physical access to the AUX port.

### Controlling vty Lines

Interactive management sessions in Cisco devices use a vty. A vty line is used for all remote network connections supported by the device, regardless of protocol (SSHv2, SCP, and Telnet are examples). To help ensure that a device can be accessed through a local or remote management session, proper controls must be enforced on vty lines. Cisco devices have a limited number of vty lines. When all vty lines are in use, new management sessions cannot be established, creating a denial of service (DoS) condition for access to the device.

The simplest form of access control for the vty of a device is the use of authentication on all lines, regardless of the location of the device within the network.

Authentication can be enforced using the local user database or through AAA. The use of a AAA broker, such as Cisco Identity Services Engine (ISE), is recommended for authenticated access to a device.

## Displaying Warning Banners

In some legal jurisdictions, malicious users cannot be prosecuted or legally monitored unless they have been notified that they are not permitted to use the system. One way to provide this notification is to put it in a banner message that is configured to display before login.

Legal notification requirements are complex and vary by jurisdiction and situation and should be discussed with legal counsel. Even within jurisdictions, legal opinions can differ. Created in cooperation with counsel, a banner can provide some or all the following information:

- Notice that the system is to be logged in to or used only by specifically authorized personnel, and information about who can authorize use

- Notice that any unauthorized use of the system is unlawful and can be subject to civil and criminal penalties

- Notice that any use of the system can be logged or monitored without further notice, and that the resulting logs can be used as evidence in court

- Specific notices required by local laws

From a security (rather than legal) point of view, a login banner should not contain any specific information about the router's name, model, software, or ownership. This information can be abused by malicious users.

## Using AAA

The AAA framework is vital to securing network devices. It provides a highly configurable environment that can be tailored to the needs of the network. The AAA framework provides authentication of management sessions, the capability to limit users to specific administrator-defined commands, and the option of logging all commands entered by all users.

### Authentication Using TACACS+, RADIUS, and LDAP

TACACS+ is an authentication protocol that Cisco devices can use for authentication of management users against a remote AAA server.

TACACS+ authentication, or more generally AAA authentication, provides the capability to centralize authentication information and authorization policies. It also enables effective centralized accounting of AAA-related transactions for improved auditability.

RADIUS is a protocol like TACACS+. However, RADIUS encrypts only the password sent across the network. In contrast, TACACS+ obfuscates the entire TCP payload, including the username and password. Refer to the Compare TACACS+ and RADIUS TechNote for a more detailed comparison of these two protocols.

Newer releases of Cisco devices support TACACS+ over TLS 1.3, RADIUS over TLS, and RADIUS over DTLS for secure communication.

If supported, Type-6 key encryption is highly recommended over the default Type-7 when using RADIUS and TACACS keys. Using Type-6 TACACS or RADIUS key requires master key configuration.

### TACACS+ over TLS 1.3

TACACS versions earlier than TACACS+ over TLS 1.3 use MD5 for data obfuscation and are therefore considered obsolete. Cisco strongly recommends that customers implement the updated TACACS+ over TLS 1.3 feature, which securely encrypts TACACS+ traffic.

This feature requires support from both the network device and the AAA server. It is supported in Cisco ISE Release 3.4 Patch 2.

### Authentication Fallback

If all configured AAA servers become unavailable, then a Cisco device can rely on secondary authentication methods. Configuration options include the use of local or no authentication if all configured TACACS+ servers are unavailable. Do not use the None option, which in effect would fall back to no authentication if the AAA servers were unreachable. This fallback would potentially allow a DoS attack on the AAA servers to eliminate authentication on the network devices.

Instead, authentication fallback should be set to use the local database when AAA servers are unreachable. This approach allows a locally defined user to be created for one or more network administrators. If TACACS+ were to become completely unavailable, each administrator could use a local username and password. Although this action does enhance the accountability of network administrators during TACACS+ outages, it can increase the administrative overhead because local user accounts on all network devices must be maintained.

Disabling fallback to local authentication can lock the Cisco device, forcing a system admin to perform a password recovery to gain access. To prevent being locked out of the device, Cisco recommends disabling fallback to local authentication for either the default login or the console login, not both.

### TACACS+ Command Authorization

Command authorization with TACACS+ and AAA provides a mechanism that permits or denies each command that is entered by an administrative user. When the user enters an EXEC or configuration command, Cisco devices send the command to the configured AAA server, which uses its configured policies to permit or deny the command for that user.

### Accounting

When configured, AAA command accounting sends information about each EXEC or configuration command that is entered back to the configured TACACS+ and RADIUS servers. The information sent to the TACACS+ servers includes the command executed, the date it was executed, and the username of the user entering the command.

### Redundant AAA Servers

The AAA servers should be redundant and deployed in a fault-tolerant manner. This approach helps ensure that interactive management access, such as SSHv2 access, is possible if an AAA server is unavailable.

When designing or implementing a redundant AAA server solution, keep these considerations in mind:

- Availability of AAA servers during potential network failures

- Geographically dispersed placement of AAA servers

- Load on individual AAA servers during steady-state and failure conditions

- Network latency between network access servers and AAA servers

- AAA server databases synchronization

## Configuring Strong Passwords

Passwords are a primary mechanism for controlling access to resources and devices.  As a security best practice, passwords should be managed with a TACACS+ or RADIUS authentication server. However, note that a locally configured username and password for privileged access is still needed in the event of a TACACS+ or RADIUS service failure. Moreover, a device may also have other password information such as a Network Time Protocol (NTP) key, SNMP community string, or routing protocol key present within its configuration.

### Recommendations for Creating Strong Passwords

Never write passwords down, on paper or online. Instead, create passwords that one can remember easily, but no one can guess easily. One way to do this is to create a password that is based on a song title, affirmation, or other phrase. For example, the phrase could be "this may be one way to remember" and the password could be "TmB1w2R!" or "Tmb1W>r~" or some other variation.

Note: Do not use either of those examples as passwords.

Note: Using a company-approved password manager to store passwords is highly recommended.

Characteristics of a Strong Password

Strong passwords have the following characteristics:

- Contain both upper- and lowercase characters (e.g., a-z, A-Z)

- Contain numerals and punctuation as well as letters (e.g., 0-9, !@#$%^&*()_+|~ =\`{}[]: ;'<>?,./)

- Are at least 15 alphanumeric characters long

- Are not a word in any language, and are not slang, dialect, or jargon

- Are not based on personal information, such as the names of family members

Characteristics of a Weak Password

A poor, weak password has the following characteristics:

- Contains fewer than 15 characters

- Is a word found in a dictionary (English or foreign)

- The name of family, pet, friend, coworker, or fantasy character

- A computing term or name, such as a command, site, company, model, or application

- Is a birthday or another kind of personal information, such as an address or telephone number

- Is a predictable letter pattern or number pattern, such as aaabbb, qwerty, zyxwvuts, or 123321

- Any of the above, spelled backward

- Any of the above, preceded or followed by a digit, such as secret1 or 1secret

### Password Security Basics

Never reveal a password.

In addition, you must:

- Never talk about a password in front of others.

- Never hint at the format of a password (such as "my family name").

- Never share a password with family members.

- Never use characters from outside the standard ASCII character set. Some symbols, such the pound sterling symbol (£), are known to cause login problems on some systems.

## Securing SNMP

Several methods can be used to secure the deployment of SNMP in Cisco devices. SNMP must be properly secured to protect the confidentiality, integrity, and availability of both the network data and the network devices through which this data transits. SNMP provides a wealth of information about the health of network devices. This information should be protected from malicious users who want to use this data for attacks against the network.

### SNMP Version 3

SNMP Version 3 (SNMPv3) is defined by RFC3410, RFC3411, RFC3412, RFC3413, RFC3414, and RFC3415 and is an interoperable standards-based protocol for network management. SNMPv3 provides secure access to devices by authenticating and optionally encrypting packets over the network. Where supported, SNMPv3 can be used to add another layer of security when deploying SNMP.

SNMPv3 consists of three primary configuration options:

- no auth does not require any authentication or any encryption of SNMP packets.

- auth requires authentication of the SNMP packet without encryption.

- priv requires both authentication and encryption (privacy) of each SNMP packet.

When priv is used, administrators should use AED-356 or higher. DES or 3DES are now considered deprecated and insecure.

An authoritative engine ID must exist to use the SNMPv3 security mechanism's authentication or authentication and encryption to handle SNMP packets. By default, the engine ID is generated locally.

Note that if the engine ID is changed, all SNMP user accounts must be reconfigured.

### SNMP Community Strings

Community strings are passwords that are applied to a Cisco device to restrict access (both read-only and read-write access) to the SNMP data on the device. These community strings, as with all passwords, should be carefully chosen to help ensure that they are strong. Community strings should be changed at regular intervals and in accordance with network security policies. For example, the strings should be changed when a network administrator changes roles or leaves the company.

Refer to the Recommendations for Creating Strong Passwords section of this document for more information about the selection and generation of strong passwords.

### SNMP Community Strings with ACLs

In addition to the community string, an ACL should be applied that further restricts SNMP access to a selected group of source IP addresses.

### iACLs

iACLs can be deployed to help ensure that only end hosts with trusted IP addresses can send SNMP traffic to a device. An iACL should contain a policy that denies unauthorized SNMP packets on UDP port 161.

## Performing Configuration Management

Configuration management is a process by which configuration changes are proposed, reviewed, approved, and deployed. Within the context of a device configuration, two additional aspects of configuration management are critical: configuration archival and security.

Engineers and administrators can use configuration archives to roll back changes that are made to network devices. In the context of security, configuration archives can also be used to determine what security changes were made and when these changes occurred. In conjunction with AAA log data, this information can assist in security auditing of network devices.

The configuration of a device contains many sensitive details, including usernames, passwords, and the contents of ACLs. The repository used to archive device configurations must be secured. Insecure access to this information can undermine the security of the entire network.

# Logging Best Practices

To understand existing, emerging, and historic events related to security incidents, an organization must have a unified strategy for event logging and correlation. This strategy must use logging information from all network devices and use prepackaged and customizable correlation capabilities.

After implementing centralized logging, an organization must develop a structured approach to log analysis and incident tracking. Depending on the needs of the organization, this approach can range from a simple, diligent review of log data to an advanced rule- and role-based analysis of multiple factors using correlated data.

Event logging provides visibility into the operation of a Cisco device and the network in which it is deployed. Cisco devices include several flexible logging options that can help an organization achieve its network management and visibility goals.

The following sections provide some basic logging best practices that can help an administrator use logging successfully while reducing the impact of logging on a Cisco device.

## Send Logs to a Central Location

System admins should send logging information to a remote syslog server. This helps admins to more effectively correlate and audit network and security events across network devices. Note that syslog messages are transmitted unreliably by UDP and in clear text. For this reason, any protections that a network uses for management traffic (for example, encryption and out-of-band access) should be extended to include syslog traffic.

## Assign Logging Level

Each internal system software component of a Cisco device that can log using the syslog facility can be assigned a severity level ranging from level 0, Emergencies, through level 7, Debug. The severity level determines the level, granularity, and frequency of messages generated for that component. Unless specifically required, avoid logging at level 7 because it produces an elevated CPU load on the device that can lead to device and network instability.

## Do Not Log to Console or Monitor Sessions

With Cisco devices, system admins can send log messages to monitor sessions or to the console. However, doing so can elevate the CPU load of a Cisco device and therefore is not recommended. Furthermore, system admins are advised to send logging information to the local log buffer or the local log file.

Use the global configuration commands to disable logging to the console and to monitor sessions. If logging output is required for troubleshooting purposes, system admins should enable it only temporarily to monitor for vty sessions and avoid using it on the console. Be sure to disable logging to monitor sessions after troubleshooting is completed.

## Log to the Log File

Software for Cisco devices supports the use of a local log buffer in the form of a log file so that an administrator can view locally generated log messages. The use of buffered logging to the log file is highly recommended instead of logging to either the console or monitor sessions.

There are two configuration options that are relevant when configuring buffered logging: the logging buffer size and the message severity levels stored in the buffer. The size of the log file and the severity levels of messages sent to the log file can be configured.

## Configure Logging Source Interface

To provide an increased level of consistency when collecting and reviewing log messages, system admins should statically configure a logging source interface using the logging source-interface interface command. Statically configuring a logging source interface helps ensure that the same IP address appears in all logging messages that are sent from an individual device. For added stability, system admins should use a loopback interface as the logging source.

## Configure Logging Time Stamps

The configuration of logging time stamps helps administrators correlate events across network devices. It is important to implement a correct and consistent logging time-stamp configuration to help ensure that administrators can correlate logging data. Logging time stamps should be configured to include millisecond precision.

# Securing the Control Plane

Control-plane functions consist of the protocols and processes that communicate between network devices to move data from the source to the destination. These include routing protocols, such as BGP, and other protocols like ICMP.

It is important that events in the management and data planes do not adversely affect the control plane. If a data plane event such as a DoS attack affects the control plane, the entire network can become unstable. Protecting the control plane of a network device is critical because the control plane helps ensure that the management and data planes are maintained and operational. If the control plane were to become unstable during a security incident, it can be impossible to recover the stability of the network.

In many cases, disabling the reception and transmission of certain types of messages on an interface can reduce the CPU load that is required to process unneeded packets.

## IP ICMP Redirect Messages

An ICMP redirect message can be generated by a router when a packet is received and transmitted on the same interface. In this situation, the router forwards the packet and sends an ICMP redirect message back to the sender of the original packet. This behavior allows the sender to bypass the router and forward future packets directly to the destination (or to a router closer to the destination). In a properly functioning IP network, a router sends redirect messages only to hosts on its own local subnets. In other words, ICMP redirect messages should never go beyond a Layer 3 boundary.

There are two types of ICMP redirect messages: redirect messages for a host address and redirect messages for an entire subnet. A malicious user can exploit the capability of the router to send ICMP redirect messages by continually sending packets to the router, forcing the router to respond with ICMP redirect messages, resulting in adverse impact on the CPU and on the performance of the router.

## ICMP Unreachable Messages

Filtering with an interface access list elicits the transmission of ICMP unreachable messages back to the source of the filtered traffic. Generating these messages can increase CPU utilization on the device. Administrators can disable ICMP unreachable message generation on Cisco devices.

Note that the default behavior of ICMP unreachable messages may vary depending on the hardware platform and whether the device interface is in Layer 2 mode or Layer 3 mode. Users are encouraged to test specific ICMP unreachable message behavior in their environments.

## Proxy Address Resolution Protocol

Proxy Address Resolution Protocol (ARP) is the technique in which one device, usually a router, answers ARP requests that are intended for another device. By "faking" its identity, the router accepts responsibility for routing packets to the real destination. Proxy ARP can help machines on a subnet reach remote subnets without the need to configure routing or a default gateway. Proxy ARP is defined in RFC 1027.

There are several disadvantages to using proxy ARP. Proxy ARP can result in an increase in the amount of ARP traffic on the network segment and resource exhaustion and machine-in-the-middle attacks. Proxy ARP presents a resource exhaustion attack vector because each proxied ARP request consumes a small amount of memory. An attacker could attempt to exhaust memory unnecessarily by sending many ARP requests.

Machine-in-the-middle attacks enable a host on the network to spoof the MAC address of the router, causing unsuspecting hosts to send traffic to the attacker. Proxy ARP can be disabled on Cisco devices.

## NTP

NTP is not an especially dangerous service, but any unneeded service can represent an attack vector. If NTP is used, explicitly configure a trusted time source and use proper authentication. Accurate and reliable time can be very useful for logging purposes, such as for forensic investigations of potential attacks.

Configuring NTP authentication assures that NTP messages are exchanged between trusted NTP peers. Enable authentication for NTP, if possible. Additionally, for precision and redundancy purposes, configure multiple NTP server time sources on the Cisco device acting as an NTP client.

## Limiting the Effect of Control-Plane Traffic on the CPU

Protection of the control plane is critical. Because application performance and end-user experience can suffer without the presence of data and management traffic, the survivability of the control plane helps ensure that the other two planes are maintained and operational.

To properly protect the control plane of the Cisco device, system admins must understand the types of traffic that are process-switched by the CPU. Process-switched traffic normally consists of two types of traffic. The first type of traffic is directed to the Cisco device and must be handled directly by the device's CPU.

The second type of traffic is data-plane traffic with a destination beyond the Cisco device that requires special processing by the CPU. This type of behavior tends to be platform specific and dependent on the specific hardware implementation of the specific Cisco platform. Some platforms handle more types of data-plane traffic in hardware, thereby requiring less CPU-based intervention. Regardless of the hardware handling capabilities, system admins should understand potential sources of control-plane traffic that could affect the system's CPU.

# Securing the Data Plane

Although the data plane is responsible for moving data from the source to the destination, the data plane is the least important of the three planes within the context of security. For this reason, when securing a network device, system admins should prioritize protecting the management and control planes over the data plane. However, within the data plane itself, there are many features and configuration options that can help secure traffic.

Most data plane traffic flows across the network as determined by the routing configuration. However, IP network functions are available to alter the path of packets across the network. Features such as IP options—specifically, the source routing option—can create security challenges.

## Limiting the Effect of Data-Plane Traffic on the CPU

The primary purpose of routers and switches is to forward packets and frames through the device to final destinations. These packets, which transit the devices that are deployed throughout the network, can affect the CPU operations of a device. The data plane, which consists of traffic transiting the network device, should be secured to help ensure the operation of the management and control planes. If transit traffic can cause a device to process switch traffic, the control plane of a device can be affected, which may disrupt operations.

## Disabling IP Source Routing

IP source routing uses the Loose Source Route and Record Route options in tandem, or the Strict Source Route along with the Record Route option, to enable the source of the IP datagram to specify the network path that a packet takes. This function can be used in attempts to route traffic around security controls in the network. For this reason, IP source routing should be disabled.

## Disabling ICMP Redirect Messages

ICMP redirect messages are used to inform a network device of a better path to an IP destination. Some Cisco devices send a redirect message if they receive a packet that must be routed through the interface from which it was received.

In some situations, an attacker may be able to cause the Cisco device to send many ICMP redirect messages, resulting in an elevated CPU load. For this reason, the transmission of ICMP redirect messages should be disabled.

## Disabling or Limiting IP Directed Broadcasts

IP directed broadcasts make it possible to send an IP broadcast packet to a remote IP subnet. After the packet reaches the remote network, the forwarding IP device sends the packet as a Layer 2 broadcast to all stations on the subnet. This directed broadcast function has been used as an amplification and reflection aid in several attacks, including the Smurf attack.

Cisco recommends disabling this function. Some Cisco operating systems have this function disabled by default.

## Filtering ICMP Packets

ICMP was designed as a control protocol for IP. As such, the messages it conveys can have far-reaching ramifications on the TCP and IP protocols in general. ICMP is used by the network troubleshooting tools ping and traceroute , as well as by path maximum transmission unit (MTU) discovery. However, external ICMP connectivity is rarely needed for the proper operation of a network.

## Filtering IP Fragments

The filtering of fragmented IP packets can pose a challenge to security devices. Because of the nonintuitive nature of fragment handling, IP fragments are often inadvertently permitted by ACLs. Attackers often use fragmentation to evade intrusion detection systems. For these reasons, IP fragments should be explicitly filtered at the top of any configured tACLs.

## Using IP Source Guard

IP source guard is an effective means of spoofing prevention that can be used if the system administrators have control over Layer 2 interfaces. IP source guard uses information from Dynamic Host Configuration Protocol (DHCP) snooping to dynamically configure a port ACL (PACL) on the Layer 2 interface, denying any traffic from IP addresses that are not associated in the IP source binding table.

IP source guard can be applied to Layer 2 interfaces that belong to VLANs that are enabled for DHCP snooping.

## Using Port Security

Port security is used to mitigate MAC address spoofing at the access interface. Port security can use dynamically learned (sticky) MAC addresses to facilitate the initial configuration. After port security has determined a MAC address violation, it can use one of four violation modes: protect, restrict, shutdown, and shutdown VLAN. In instances in which a port provides access only for a single workstation using standard protocols, a maximum value of 1 may be sufficient. Protocols that use virtual MAC addresses such as Hot Standby Router Protocol (HSRP) do not function when the maximum value is set to 1.

## Traffic Identification and Traceback

At times, administrators may need to quickly identify and trace back network traffic, especially during incident response or poor network performance. NetFlow and classification ACLs are the two primary mechanisms for accomplishing this using Cisco devices.

### NetFlow

NetFlow can provide visibility into all traffic on the network. Additionally, NetFlow can be implemented with collectors that can provide long-term trending and automated analysis.

NetFlow enables engineers and administrators to monitor traffic flows throughout the network. Originally intended to export traffic information to network management applications, NetFlow can also be used to show flow information (that is, source and destination interfaces, IP addresses, and ports) on a router. This capability allows administrators to see traffic traversing the network in real time or to capture the information for reference. Regardless of whether flow information is exported to a remote collector or viewed live, administrators should configure network devices for NetFlow so that it can be used in various capacities (including proactive and reactive scenarios) if needed.

NetFlow identifies anomalous and security-related network activity by tracking network flows. NetFlow data can be viewed and analyzed using the CLI, or the data can be exported to a commercial or freeware NetFlow collector for aggregation and analysis. NetFlow collectors, through long-term trending, can provide network behavior and usage analysis. NetFlow functions by performing analysis on specific attributes within IP packets and creating flows. NetFlow Version 5 is the most commonly used version of NetFlow; however, Version 9 is more extensible. NetFlow flows can be created using sampled traffic data in high-volume environments.

More information about this feature is available at http://www.cisco.com/go/netflow (registered Cisco customers only).

### Classification ACLs

Classification ACLs provide visibility into traffic that traverses an interface. They are a component of ACLs and require planning to identify specific traffic and manual intervention during analysis.

Classification ACLs do not alter the security policy of a network and are typically constructed to classify individual protocols, source addresses, or destinations. For example, an access control entry that permits all traffic could be separated into specific protocols or ports. This more detailed classification of traffic into specific access control entries can help provide an understanding of the network traffic because each traffic category has its own hit counter. An administrator can also separate the implicit deny response at the end of an ACL into granular access control entries to help identify the types of denied traffic.

## Access Control with VLAN Maps and PACLs

VLAN ACLS (VACLs), also called VLAN maps, and port ACLs (PACLs) provide the capability to enforce access control on nonrouted traffic that is closer to endpoint devices than ACLs that are applied to routed interfaces.

### Access Control with VLAN Maps

VLAN maps that apply to all packets that enter the VLAN can be used to enforce access control for intra-VLAN traffic. This control is not possible using ACLs on routed interfaces. For example, a VLAN map can be used to prevent hosts that are contained within the same VLAN from communicating with each other, thereby reducing opportunities for local attackers or worms to exploit a host on the same network segment. To prevent packets from using a VLAN map, administrators can create an ACL that matches the traffic and, in the VLAN map, set the action to drop. After a VLAN map is configured, all packets that enter the LAN are sequentially evaluated against the configured VLAN map. VLAN access maps support IPv4 and MAC address access lists. However, they do not support logging or IPv6 ACLs.

### Access Control with MAC Address ACLs

MAC packet classification allows a system admin to control whether a MAC ACL that is on a Layer 2 interface applies to all traffic entering the interface, including IP traffic, or to non-IP traffic only.

A system admin can enable or disable MAC packet classification only on Layer 2 interfaces.

# Conclusion

This document has provided a broad overview of the methods that can be used to secure a Cisco NX-OS, IOS XE, or IOS XR system device. In this overview, the protection of the management, control, and data planes were discussed. By securing individual devices, system administrators increase the overall security of the networks that they manage.

# Appendix

## OS-Specific Guide Links

- Cisco IOS XE Software Hardening Guide

- Cisco IOS XR Software Hardening Guide

- Cisco NX-OS Software Hardening Guide

## References

# Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Updated Date | Comments |
|---|---|
| 11-Jun-2026 | First published. |