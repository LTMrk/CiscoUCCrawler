---
doc_id: sec-cloudapps-cisco-com-security-center-resources-firewall-best-practices-95c937758e
source_url: https://sec.cloudapps.cisco.com/security/center/resources/firewall_best_practices
retrieved_at: 2026-09-01T14:09:30.858206+00:00
---

Home / Cisco Security

Cisco Firewall Best Practices

# Cisco Firewall Best Practices

Introduction Prerequisites Components Used Conventions Principles of Secure Operations Cisco Firewalls as Security Devices Security Policies and Configuration Physical Security Monitor Cisco Security Advisories and Responses Leverage Authentication, Authorization, and Accounting. Centralize Log Collection and Monitoring Use Secure Protocols When Possible Gain Traffic Visibility with NetFlow Configuration Management Securing the Management Plane General Management Plane Hardening Securing Management Sessions Password Management Login Password Retry Lockout Disabling Password Recovery Disable Unused Services Network Time Protocol Session Timeout Using Management Interfaces Memory Threshold Notifications CPU Thresholding Notification ICMP Packet Filtering Securing Interactive Management Sessions Encrypting Management Sessions Console Port Control Management Sessions Control Management Sessions for Security Services Modules Set Management Session Quota Warning Banners Using Authentication, Authorization, and Accounting. TACACS+ Authentication Authentication Fallback TACACS+ Command Authorization TACACS+ Command Accounting Fortifying the Simple Network Management Protocol SNMP Community Strings SNMP MIBs SNMP Version 3 Logging Best Practices Send Logs to a Central Location Logging Level Disable Logging to Monitor Sessions and the Console Use Buffered Logging Configure Logging Time Stamps Software Configuration Management Show or Hide Invalid Usernames in Syslogs Securing the Control Plane General Control Plane Hardening ICMP Redirects ICMP Unreachables Limiting ICMP Responses Securing Routing Protocols Routing Protocol Authentication Securing the Data Plane General Data Plane Hardening Filtering Transit Traffic with Transit ACLs ACL Configuration Best Practices ACL Match Limits Security Levels Content and URL Filtering Content Filtering URL Filtering Modular Policy Framework Anti-Spoofing Protections Unicast Reverse Path Forwarding Antispoofing with Access Lists Inspection Enable Inspection for Nondefault Applications ACLs to Block Private and Bogon Addresses Denial of Service Protections Threat Detection Connection Limiting TCP Normalizer Botnet Protection Limiting the CPU Impact of Data Plane Traffic Traffic Identification and Traceback IPv6 Traffic Filtering High Availability Security Best Practices Checklist Management Plane Checks Control Plane Checks Data Plane Checks Conclusion Acknowledgments References

# Introduction

This document provides administrators and engineers guidance on securing Cisco firewall appliances, which increases the overall security of an end-to end architecture. The functions of network devices are structured around three planes: management, control, and data. This document is structured around security operations (best practices) and the three functional planes of a network. In addition, this document provides an overview of each included feature and references to related documentation. For the purposes of this document, all mentions of "Cisco firewall" refer explicitly to the Cisco ASA Adaptive Security Appliances, though the concepts may apply to other firewall and security devices.

The three functional planes of a network each provide different functionality that needs to be protected.

- Management plane: The management plane manages traffic that is sent to the Cisco firewall device and is composed of applications and protocols such as SSH and Simple Network Management Protocol (SNMP).

- Control plane: The control plane of a network device processes the traffic that is paramount to maintaining the functionality of the network infrastructure. The control plane consists of applications and protocols between network devices, which include the interior gateway protocols (IGPs) such as the Enhanced Interior Gateway Routing Protocol (EIGRP) and Open Shortest Path First (OSPF).

- Data plane: The data plane forwards data through a network device. The data plane does not include traffic that is sent to the local Cisco firewall device.

In addition to providing configuration details, this document serves primarily as a best practices guide. Therefore, security concepts will be recommended, although the exact configuration details may not be provided. The feature will be explained in a manner that allows the security practitioner and decision makers to determine whether the feature is required in a certain environment.

# Prerequisites

Engineers and administrators should possess a conceptual understanding of Cisco firewall product software and the basic configuration options available.

## Components Used

This document addresses the capabilities of Cisco ASA versions 8.x and later. Earlier releases of Cisco ASA Software may not include all features or capabilities outlined. Security practitioners who are using any Cisco firewall devices or ASA versions other than 8.x are advised to consult the release notes and documentation for the respective release regarding details and supported features.

Note: Some of the features referenced in this document may refer to, or show, examples of options that use strong encryption algorithms. Not all encryption algorithms may be available in all releases of Cisco firewall device software in all countries because of U.S. government export regulations.

## Conventions

Refer to Cisco Technical Tips Conventions for more information on document conventions. Some command line examples in this document are wrapped to enhance readability.

# Principles of Secure Operations

Secure network operations are a substantial topic. Although most of this document is devoted to the secure configuration of a Cisco firewall device, configurations alone do not completely secure a network. The operational procedures in use on the network contribute as much to security as the configuration of the underlying devices.

These topics contain operational recommendations that administrators and engineers are advised to implement. These topics highlight specific critical areas of network operations and are not comprehensive.

## Cisco Firewalls as Security Devices

Cisco firewalls provide advanced stateful firewall and VPN concentrator functionality in one device. In addition, some models offer an integrated intrusion prevention system (IPS) module or an integrated content security and control (CSC) module. Cisco firewall platforms include many advanced features, such as multiple security contexts (similar to virtualized firewalls), transparent (Layer 2) firewall, or routed (Layer 3) firewall operation, advanced inspection engines, IP Security (IPsec) VPN, SSL VPN, and clientless SSL VPN support. Cisco firewalls protect network segments from unauthorized access by users or miscreants while also enforcing security policies and posture.

When discussing the networks connected to a firewall, the outside network is typically defined as being in front of the firewall (an unsecured area), while the inside network is protected (by default) and resides behind the firewall-a trusted area, and a demilitarized zone ( DMZ) , while behind the firewall, allows limited access to outside (external) and inside (internal) users. Because Cisco ASA allows administrators and engineers to configure many interfaces with varied security policies, these interface terms/names are used only in a general sense.

There are key details that establish a firewall as a firewall and not a Layer 3 forwarding device. The Cisco firewall performs numerous intrinsic functions to ensure the security of an environment. These functions include, but are not limited to, the following:

- Stateful inspection

- Layer 2-7 protocol inspection (application protocol visibility)

- TCP normalizer functions

- Connection limits

These are key functions that differentiate a Cisco firewall from a standard Layer 3 device.

For further details see the Cisco ASA 5500 Series Configuration Guide .

## Security Policies and Configuration

Security policies are the top tier of formalized security documents. These high-level documents take into account a risk assessment, and subsequently offer general statements regarding the organization's assets and resources and the level of protection they should have. Furthermore, security policies do not provide detailed specifics on how to accomplish the stated goals. Those details are captured in the subsequent security standards, baselines, and procedure documents. A security policy determines the standards and rules that an environment/organization must adhere to. This policy also dictates which architecture solutions should be adopted for a given environment. The policy should be used as a high-level guide when pursuing firewall configuration details, including which traffic should be permitted to pass through the firewall to access another network and which traffic should not be permitted to pass.  Cisco ASA leverages the construct of "Security Levels" to allow (or deny) the flow of traffic from one interface to another. Each interface must have a security level assigned from 0 (lowest) to 100 (highest). For example, you should assign your most secure network, such as the inside host network, to level 100. While the outside network connected to the Internet can be level 0.

Other networks, such as DMZs can be in between. You can assign interfaces to the same security level. By default, Cisco ASA allows traffic to flow freely from a higher security level interface to a lower security level interface. For more details on Cisco ASA security levels, see the Security Levels section of this document. Administrators and engineers can apply actions to traffic to customize and/or adjust the firewall to adhere to stated security policies. Note: An organization's established security policies, and not product features, should be the key factor when determining configuration details. For further details, see the Cisco ASA 5500 Series Configuration Guide in addition to the Resources section of this document.

## Physical Security

The security of a device should begin with a progression up the Open Systems Interconnection (OSI) reference model, beginning with the physical layer. Though obvious, the details surrounding the physical security of a device are often overlooked. Physical security, as it applies to a firewall, refers to ensuring the device is placed in a physical location that is restricted to authorized personnel. Most often firewalls are installed in a restricted-access room; however, many levels of personnel have access to the room. Therefore, consider establishing and using role-based access control (RBAC). In this scenario, in addition to having the firewall placed in a restricted-access room, the firewall may also be housed in a locking rack/sector in the restricted room. Furthermore, environmental factors should also be verified because most Cisco firewalls have an operating temperature of 32 to 104 degrees F (0 to 40 degrees C). For details regarding the environmental factors and statistics, refer to the product data sheets for the respective firewall on the Cisco website .

## Monitor Cisco Security Advisories and Responses

The Cisco Product Security Incident Response Team (PSIRT) creates and maintains publications, commonly referred to as Cisco Security advisories, for security-related issues in Cisco products.  Security advisories are available at http://www.cisco.com/go/psirt .

Additional information about these communication vehicles is available in the Cisco Security Vulnerability Policy . To maintain a secure network, one must be aware of the Cisco advisories and responses that have been released. Moreover, one must have knowledge of a vulnerability before evaluating the threat it can pose to a network. Refer to Risk Triage for Security Vulnerability Announcements for assistance with this evaluation process.

## Leverage Authentication, Authorization, and Accounting

The authentication, authorization, and accounting (AAA) framework is vital to securing network devices. The AAA framework provides authentication of management sessions and can also limit users to specific, administrator-defined commands in addition to logging all commands entered by all users. See the Leverage Authentication, Authorization, and Accounting section of this document for more information about using AAA. Also, it is highly recommended that network administrators implement the principle of least privilege, in which every program and every user of the system should operate using the least set of privileges necessary to complete the job.

## Centralize Log Collection and Monitoring

To understand existing, emerging, and historic events related to security incidents, an organization needs a unified strategy for event logging and correlation. This strategy must employ logging from all network devices and use prepackaged and customizable correlation capabilities. After centralized logging is implemented, one must develop a structured approach to log analysis and incident tracking. Based on the needs of the organization, this approach can range from a simple, diligent review of log data to advanced rule-based analysis. See the Logging Best Practices section of this document for more information about implementing logging on Cisco firewall devices.

## Use Secure Protocols When Possible

Many protocols are used to carry sensitive network management data. One must use secure protocols whenever possible. A secure protocol choice includes using SSH instead of Telnet so that both authentication data and management information are encrypted. In addition, one must use secure file transfer protocols when copying configuration data. An example is the use of the Secure Copy Protocol (SCP) in place of FTP or TFTP. See the Securing Interactive Management Sessions section of this document for more information about the secure management of Cisco firewall devices.

## Gain Traffic Visibility with NetFlow

Cisco firewalls support NetFlow version 9 services. In particular, the Cisco ASA implementation of NetFlow Secure Event Logging (NSEL) is a stateful, IP flow tracking method that exports only records that indicate significant events in a flow. In stateful flow tracking, tracked flows go through a series of state changes. NSEL events are used to export data about flow status and are triggered by the event that caused the state change. The significant events that are tracked include flow-create, flow-teardown, and flow-denied (excluding flows that are denied by EtherType access control lists [ACLs]). Each NSEL record has an event ID and an extended event ID field, which describes the flow event. For details regarding NSEL on Cisco firewalls, refer to the NetFlow Implementation Guide .

## Configuration Management

Configuration management, also known as change management, is a process by which configuration changes are proposed, reviewed, approved, and deployed. In the context of a Cisco firewall device configuration, two additional aspects of configuration management are critical: configuration archiving and security. One can use configuration archives to roll back changes that are made to network devices. In a security context, configuration archives can also be used to determine which security changes were made and when these changes occurred. In conjunction with AAA log data, this information can assist in the security auditing of network devices. The configuration of a Cisco firewall device contains many sensitive details. Usernames, passwords, and the contents of ACLs are examples of this type of information. The repository used to archive Cisco firewall device configurations needs to be secured. Insecure access to this information can undermine the security of the entire network.

# Securing the Management Plane

The management plane consists of functions that achieve the management goals of the network. This includes interactive management sessions using SSH in addition to statistics gathering with SNMP or NetFlow. When considering the security of a network device, it is critical that the management plane be protected. If a security incident can undermine the functions of the management plane, the administrator may not be able to "recover" (stabilize) the network. The Management Plane sections of this document provide the security features and configurations available in Cisco ASA Software that help fortify the management plane.

## General Management Plane Hardening

The purpose of the management plane is to provide the capability to access, configure, and manage a device and to monitor its operations and the network on which it is deployed. The management plane receives and sends traffic for these functions. One must secure both the management plane and control plane of a device because operations of the control plane directly affect operations of the management plane. The following is a list of common protocols and tools used by the management plane:

- SNMP

- Telnet

- SSH

- FTP

- TFTP

- SCP

- TACACS+

- RADIUS

- NetFlow

- Network Time Protocol (NTP)

- Syslog

Steps must be taken to ensure the survival of the management and control planes during security incidents. If one of these planes is successfully exploited, all planes can be compromised. Moreover, exploitation can heavily impact the incident handling process, specifically regarding postmortem and lessons learned.

## Securing Management Sessions

### Password Management

Passwords control access to resources and devices when they are required for request authentication. When a request for access to a resource or device is received, the request is challenged for verification of the password and identity. Access can be granted, denied, or limited based on the result. As a security best practice, passwords must be managed with a TACACS+ or RADIUS authentication server. However, note that a locally configured password for privileged access will still be needed in the event of TACACS+ or RADIUS services failure. A device may also have other password information present in its configuration. Examples include an NTP key, SNMP community string, and failover or routing protocol keys. The enable password command is used to set the password that grants privileged administrative access to the Cisco firewall system. This command uses Message Digest 5 (MD5) for password hashing. This algorithm has had considerable public review and is not known to be reversible. However, the algorithm is subject to dictionary attacks, in which an attacker attempts various dictionary words in addition to other lists of candidate passwords to search for a match. For resilience against dictionary attacks, a salt value is added to the password before it is hashed and stored. As a general precaution, configuration files must be securely stored and shared only with trusted individuals. User passwords are also hashed using the MD5 algorithm after they have been concatenated with a salt value that provides resilience against dictionary attacks. Other Cisco firewall passwords (such as OSPF keys and VPN keys) are not encrypted on the firewall device by default, but the configured passwords will not be shown in the show running-configuration command output. Any Cisco firewall configuration file that contains passwords must be treated with care. Beginning with Cisco ASA version 8.3, the firewall can store plaintext passwords in an encrypted format. The encryption algorithm is the Advanced Encryption Standard (AES). The feature requires the definition of an encryption passphrase that is used to encrypt and decrypt the keys/passwords. Keys that can be encrypted include keys for routing protocol authentication, VPN, failover, AAA servers, logging, shared licenses, and more. Refer to the Configure the Master Passphrase section of the Cisco ASA Series General Operations CLI Configuration Guide for further information on the feature.

### Login Password Retry Lockout

The ASA allows an administrator to lock out a local user account after a configured number of unsuccessful login attempts. Once a user is locked out, the account is locked until the administrator unlocks it. An authorized user who is configured with privilege level 15 cannot be locked out with this feature. The number of users with privilege level 15 must be kept to a minimum.

Note that authorized users can lock themselves out of a device if the number of unsuccessful login attempts is reached. In addition, a malicious user can create a denial of service (DoS) condition with repeated attempts to authenticate with a valid username. This example shows how to enable the login password retry lockout feature:

```
!
aaa authentication telnet console LOCAL
aaa authentication ssh console LOCAL
aaa local authentication attempts max-fail 5
!
username <name> password UOeJAK2TCgmxctnA encrypted
!
```

Refer to the Configuring AAA for Network Access section of the Cisco ASA  Series General Operations CLI Configuration Guide for more information about this feature.

### Disable Unused Services

Being a security device, the Cisco firewall does not run many services (for example, bootp , finger , Cisco Discovery Protocol) by default. As a security best practice, any unnecessary services must be disabled. These unneeded services, especially those that use UDP, are infrequently used for legitimate purposes, but can also be used to launch DoS and other attacks that are otherwise prevented by packet filtering.

### Network Time Protocol

Network Time Protocol (NTP) is not an especially dangerous service, but any unneeded service can represent an attack vector. If NTP is used, it is important to explicitly configure a trusted time source and to use proper authentication. Accurate and reliable time is required for syslog purposes (for example, during forensic investigations of potential attacks) and for successful VPN connectivity when depending on certificates for Phase 1 authentication.

- NTP time zone: When configuring NTP, the time zone must be configured so that time stamps can be accurately correlated. There are usually two approaches to configuring the time zone for devices in a network with a global presence. One method is to configure all network devices with the Coordinated Universal Time (UTC) (or Greenwich Mean Time [GMT] if preferred). The other approach is to configure network devices with the local time zone. More information on this feature can be found in the Basic Settings section of the Cisco ASA General Operations CLI Configuration Guide.

- NTP authentication: Configuring NTP authentication provides assurance that NTP messages are exchanged between trusted NTP peers. Refer to the Basic Settings section of the Cisco ASA Series General Operations CLI Configuration Guide for more information on configuring NTP authentication.

### Session Timeout

To set the interval that the EXEC command interpreter waits for user input before it terminates a session, an administrator can use the < protocol > timeout global configuration command. The command must be used to log out sessions (Telnet, SSH, console) that are left idle. By default, sessions are disconnected after 5 minutes of inactivity. See the following example:

```
! ssh timeout <minutes>

telnet timeout <minutes>

console timeout <minutes> !
```

### Using Management Interfaces

The management plane of a device is accessed via in-band and out-of-band methods through physical and logical means. Ideally, both in-band and out-of-band management access exists for each network device so that the management plane can be accessed during network outages. Cisco firewalls define a specific interface as being the Management interface. This designation is defined by configuring the management-only command on the specific interface. By default the physically defined Management interface has this command defined. This interface is used for in-band access to a Cisco firewall. The Management interface can also be used for regular traffic when removing the management-only interface configuration command. It is recommended to use the Management interface of the ASA device exclusively as a management interface. This allows administrators and engineers to apply management traffic-based policies throughout the network. After the Management interface is configured on a Cisco firewall, it can be used by management plane protocols, such as SSH, SNMP, and syslog. Note that the Management interfaces on a Cisco firewall use the global routing table of the device; they do not use a separate routing table.

### Memory Threshold Notifications

The Memory Threshold Notification feature provides administrators and engineers with insight to mitigate low-memory conditions on a device. This feature enables a device to generate an SNMP notification when the memory pool buffer usage reaches a new peak. The following example will generate the memory-threshold trap toward the SNMP server when the system memory reaches 70 percent. Note: The default memory threshold is 70 percent.

```
! snmp-server enable traps memory-threshold

snmp-server host <int-name> <host-address> community <community-string> !
```

CPU Thresholding Notification

The CPU threshold notification feature allows administrators and engineers to detect, and be notified, when the CPU load on a device crosses the set threshold for a configured period of time. When the threshold is crossed, the device generates and sends an SNMP trap message. The following example will generate a CPU threshold trap toward the SNMP server when the CPU load is 75 percent or above for 30 minutes.

```
! snmp-server enable traps cpu-threshold

snmp cpu threshold rising 75% 30

snmp-server host <int-name> <host-address> community <community-string> !
```

Refer to the SNMP Chapter of the Cisco ASA Series General Operations CLI Configuration Guide for more information about this feature.

ICMP Packet Filtering

ICMP is designed as an IP control protocol. As such, the messages it conveys can have far-reaching ramifications to the TCP and IP protocols in general. While the network troubleshooting tools ping and traceroute use ICMP, external ICMP connectivity is rarely needed for the proper operation of a network. Cisco firewall software provides functionality to filter ICMP messages destined to itself by name or type and code. Cisco firewalls will, by default, allow pings to the firewalls' interfaces. The following example allows pings to a Cisco firewall interface from trusted management stations and blocks all other ICMP packets that are destined to the firewall:

```
icmp permit <trusted-management-stations-subnet> 
<trusted-management-stations-mask> echo <interface-name>
icmp deny any <interface-name>
```

### Securing Interactive Management Sessions

Management sessions destined to devices allow one to view and collect information about a device and its operations. If this information is disclosed to a malicious user, the device can become the target of an attack, compromised, and used to perform additional attacks. Anyone with privileged access to a device has the capability for full administrative control of that device. Securing management sessions is imperative to preventing information disclosure and unauthorized access.

It is not recommended to access the security appliance through an HTTP-based GUI session. The authentication credential information, such as the password, is sent as clear text. The HTTP server and client communication occurs only in clear text. Cisco recommends the use of HTTPS for secure GUI-based data communication.

It is not recommended to access the security appliance through a Telnet-based command-line interface (CLI) session. The authentication credential information, such as the password, is sent as clear text. The Telnet server and client communication occurs only in clear text. Cisco recommends the use of SSH for secure CLI data communication.

### Encrypting Management Sessions

Because information can be disclosed during an interactive management session, this traffic must be encrypted so a malicious user cannot access the data being transmitted. Encrypting the traffic allows a secure remote access connection to the device. If the traffic for a management session is sent over the network in clear text, an attacker can obtain sensitive information about the device and the network.

As previously stated, it is not recommended to access the security appliance through an HTTP or Telnet session because the authentication credential information is sent in clear text. By default, a Cisco firewall will not accept Telnet to its lowest trusted interface, as defined via the interface-configured security levels. Cisco recommends using SSH for more secure data communication. Reverse Telnet or reverse SSH is not possible on the Cisco firewall, meaning one cannot execute a reverse Telnet or initiate an SSH connection from the Cisco firewall. Cisco firewall software supports SSH version 2 (SSHv2), and HTTPS. HTTPS leverages SSL and Transport Layer Security (TLS) for authentication and data encryption of management sessions. In addition, IPsec can be used for encrypted and secure remote access connections to a Cisco firewall device, if supported, but IPsec adds additional CPU overhead to the device. Also, SSH must still be enforced as the transport even when IPsec is used. Cisco firewall software supports the SCP, which allows an encrypted and secure connection for copying device configurations or software images. SCP relies on SSH.

The following example configuration enables SSH on a Cisco ASA device:

```
! domain-name example.com ! crypto key generate rsa modulus 2048 ! ssh timeout 60
ssh version 2 !
```

The following is a configuration example for HTTPS services:

```
! crypto key generate rsa modulus 2048 ! http redirect <interface-name> !
```

Refer to the Management Access section of the Cisco ASA  Series General Operations Configuration Guide for more information about the Cisco firewall software SSH feature.

### Console Port

On Cisco firewall devices, the console port is an asynchronous line that can be used for local and remote access to a device. One must be aware that the console port on Cisco firewall devices has special privileges. In particular, these privileges allow an administrator to perform the password recovery procedure. To perform password recovery, an unauthenticated attacker would need access to the console port in addition to the ability to interrupt power to the device or cause the device to crash and reload. Any method used to access the console port of a device must be secured in a manner that is equal to the security that is enforced for privileged access to a device. Methods used to secure access must include the use of AAA, console timeouts, and modem passwords if a modem is attached to the console.

### Control Management Sessions

Cisco firewall interactive management sessions include console, Telnet, SSH, HTTP, and HTTPS. To ensure that a device can be accessed via a local or remote management session, proper controls must be enforced for the management protocols. Cisco firewall devices have a limited number of available management connections; the number of sessions available can be determined by using the show resource usage EXEC command. When all sessions are in use, new management sessions cannot be established, creating a DoS condition for access to the device.

The simplest form of access control to a device is through authenticated management sessions. Session access controls can be enforced by using the <ssh | telnet > < subnet > < mask > < interface name > commands. Furthermore, authentication can be enforced through the use of AAA, which is the recommended method for authenticated access to a device. AAA uses the local user database or the enable password in the case of Telnet and console sessions. The < ssh | telnet | console > timeout command must be used to log out sessions that are left idle. Refer to the Management Access section of the ASA Series General Operations CLI Configuration Guide for details regarding management access configuration.

### Set a Management Session Quota

You can establish a maximum number of simultaneous ASDM, SSH, and Telnet sessions that are allowed on the ASA device. If the maximum is reached, no additional sessions are allowed and a syslog message is generated. To prevent a system lockout, the management session quota mechanism cannot block a console session.

For example:

```
!
         quota management-session ssh3
         !
```

### Warning Banners

In some legal jurisdictions it may be improbable and/or illegal to monitor and prosecute malicious users unless they have been notified that they are not permitted to use or access a respective device or resource. One method to provide this notification is the banner message configuration on the Cisco firewall using the banner login command. Legal notification requirements are complex, vary by jurisdiction and situation, and should be discussed with legal counsel. Even within jurisdictions, legal opinions can differ. In cooperation with counsel, a banner can provide the following information:

- Notice that the system is to be logged into or used only by specifically authorized personnel

- Notice that any unauthorized use of the system is unlawful and can be subject to civil and criminal penalties

- Notice that any use of the system can be logged or monitored without further notice and that the resulting logs can be used as evidence in court

- Specific notices required by local laws

From a security point of view, a login banner should not contain any specific information about the device name, model, software, or ownership because this information can be abused by malicious users.

Refer to the Configuring a Login Banner section of the Cisco ASA Series General Operations CLI Configuration Guide for more information about Cisco firewall banners.

## Using Authentication, Authorization, and Accounting

The Authentication, Authorization, and Accounting (AAA) framework is critical to securing interactive access to network devices. The AAA framework provides a highly scalable architecture consisting of flexibility and granular configuration that can be tailored to the needs of the network.

### TACACS+ Authentication

TACACS+ is an authentication protocol that Cisco firewall devices can use for authentication of management users against a remote AAA server. These management users can access the firewall device via SSH, Telnet, HTTP, or HTTPS. TACACS+ authentication, or more generally AAA authentication, provides the ability to use individual user accounts for each administrator or engineer, employing the use of access controls. In removing the dependence on a single shared password, the security of the network is improved and accountability is strengthened. RADIUS is a protocol similar in purpose to TACACS+. However, it only encrypts the password sent across the network. In contrast, TACACS+ encrypts the entire TCP payload, including both the username and password. For this reason, TACACS+ is the preferred AAA server in Cisco network environments. Refer to the Cisco TACACS+ and RADIUS Comparison document for a more detailed comparison of these two protocols. TACACS+ authentication via Telnet can be enabled on a Cisco ASA device using a configuration similar to the following:

```
! aaa authentication ssh console <serv-name> ! aaa-server <serv-name> protocol tacacs+
aaa-server <serv-name> (<interface-name>) host
<ip-address-of-tacacs-server>
 <key> !
```

The previous configuration can be used as a starting point for an organization-specific AAA authentication template. Refer to the Configuring AAA Rules for Network Access section of the Cisco ASA  Series General Operations CLI Configuration Guide for more information about the configuration of AAA servers and server groups including support for Radius, TACACS+, LDAP, Kerberos, and RSA SecurID.

### Authentication Fallback

If the TACACS+ server becomes unavailable, a Cisco ASA device can rely on secondary authentication methods or protocols. Typical configurations include the use of local authentication if the TACACS+ server is unavailable. On Cisco ASA software releases that encrypt passwords for locally defined users, fallback to local authentication can be desirable. This allows a locally defined user to be created for one or more network administrators. If TACACS+ were to become completely unavailable, each administrator can use a local username and password. Although this approach does enhance the accountability of network administrators during TACACS+ outages, it significantly increases the administrative burden because local user accounts on all network devices must be maintained. The following configuration example builds on the previous TACACS+ authentication example to include fallback authentication to the local database:

```
! aaa authentication ssh console <serv-name> LOCAL ! aaa-server <serv-name> protocol tacacs+
aaa-server <serv-name> (<interface-name>) host
<ip-address-of-tacacs-server>
 <key> !
```

Refer to the Configuring Management Access section of the Cisco ASA 5500 Series Configuration Guide for more information on the use of fallback authentication with AAA.

### TACACS+ Command Authorization

AAA command authorization using TACACS+ provides a mechanism that permits or denies each command that is entered by an administrative user. When the user enters EXEC commands, the Cisco ASA sends each command to the configured AAA server. The AAA server then uses its configured policies to permit or deny the command or operation for that particular user. The following configuration can be added to the previous AAA authentication example to implement command authorization:

```
! aaa authorization exec <serv-name> <serv-name> ! aaa-server <serv-name> protocol tacacs+
aaa-server <serv-name> (<interface-name>) host
<ip-address-of-tacacs-server>
 <key> !
```

Refer to the Configuring Command Authorization section of the Cisco ASA  Series General Operations CLI Configuration Guide for more information about command authorization.

TACACS+ Command Accounting

When configured, AAA command accounting sends information about each EXEC command that is entered to the configured TACACS+ servers. The information sent to the TACACS+ server includes the command executed, the date it was executed, and the username of the user entering the command. Command accounting is not supported using RADIUS. The following example configuration enables AAA command accounting for EXEC commands entered at privilege levels zero, one, and 15. This configuration builds on previous examples that include configuration of the TACACS servers.

```
! aaa accounting ssh console <serv-name> ! aaa-server <serv-name> protocol tacacs+
aaa-server <serv-name> (<interface-name>) host
<ip-address-of-tacacs-server>
 <key> !
```

Refer to Configuring Management Access Accounting for more information regarding the configuration of AAA command accounting.

## Fortifying the Simple Network Management Protocol

SNMP is an application-layer protocol that facilitates the exchange of management information between network devices and is part of the TCP/IP protocol suite. Cisco ASA devices provide support for network monitoring using SNMP Versions 1, 2c, and 3, and support the use of all three versions simultaneously. The SNMP agent running on the ASA interface lets you monitor the network devices through network management systems (NMSes), such as HP OpenView. Cisco ASA devices support SNMP read-only access through issuance of a GET request. SNMP write access is not allowed, so you cannot make changes with SNMP. In addition, the SNMP SET request is not supported.

Note : SNMP can be configured over IPv6 transport so that an IPv6 host can perform SNMP queries and receive SNMP notifications from a device running IPv6 software.

It is critical that SNMP be properly secured to protect the confidentiality, integrity, and availability of both the network data and the network devices through which this data transits. SNMP provides one with a wealth of information on the health of network devices. This information should be protected from malicious users that want to use it to perform attacks against the network.

### SNMP Community Strings

Community strings are passwords that are applied to an ASA device to restrict access, both read-only and read-write access, to the SNMP data on the device. These community strings, as with all passwords, should be carefully chosen to ensure they are not trivial. Community strings should be changed at regular intervals and in accordance with network security policies. For example, the strings should be changed when a network administrator changes roles or leaves the company. These configuration lines configure a community string of COMM for SNMP version 1 (SNMPv1) and Community-based SNMP version 2 (SNMPv2c):

```
! snmp-server community COMM !
```

Note that the preceding community string examples have been chosen to clearly explain the use of these strings. For production environments, community strings should be chosen with caution and should consist of a series of alphabetical, numerical, and nonalphanumeric symbols. Refer to Use a Strong Password for more information on the selection of nontrivial passwords.

Refer to the Configuring SNMP section of the Cisco ASA Series General Operations CLI Configuration Guide for more information about this feature.

### SNMP MIBs

MIBs are either standard or enterprise specific. Standard MIBs are created by the IETF and documented in various RFCs. The firewall can support a variety of MIBs. Cisco ASA version 8.4 recently added more MIBs and traps to the wide range already supported. The administrator decides which MIB object ID (OID) to poll and which SNMP traps to enable to monitor the uninterrupted operation of the firewall device. A recommended minimum list of MIBs and traps to monitor that focus on device health, resources, and normal operation follows:

For a list of supported MIBs and traps for the Cisco ASA and ASA Services Module by release, see the following URL: https://www.cisco.com/c/en/us/td/docs/security/asa/asa917/configuration/general/asa-917-general-config/monitor-snmp.html

SNMP Version 3

SNMP version 3 (SNMPv3) is defined by RFC 3410 , RFC 3411 , RFC 3412 , RFC 3413 , RFC 3414 , RFC 3415 , and RFC 8096 and is an interoperable standards-based protocol for network management. SNMPv3 provides secure access to devices by authenticating and optionally encrypting packets over the network. SNMP Version 3 provides security enhancements that are not available in SNMP Version 1 or Version 2c. For SNMP Version 3, configuration must occur in the following order: group, user, host. You can now add up to 4000 hosts. The number of supported active polling destinations is 128. The limit on the message size that SNMP sends has been increased to 1472 bytes.

SNMP over IPV6 as  described in RFC 8096:

- ipv6InterfaceTable (OID: 1.3.6.1.2.1.4.30)—Contains per-interface IPv6-specific information.

- ipAddressPrefixTable (OID:1.3.6.1.2.1.4.32)—Includes all the prefixes learned by this entity.

- ipAddressTable (OID: 1.3.6.1.2.1.4.34)—Contains addressing information relevant to the entity's interfaces.

- ipNetToPhysicalTable (OID: 1.3.6.1.2.1.4.35)—Contains the mapping from IP addresses to physical  addresses.

Where supported, SNMPv3 can be used to add another layer of security when deploying SNMP. SNMPv3 consists of three primary configuration options:

- no auth : This mode does not require authentication or encryption of SNMP packets.

- auth : This mode requires authentication of the SNMP packet without encryption.

- priv : This mode requires both authentication and encryption (privacy) of each SNMP packet.

The SNMPv3 implementation in the Cisco ASA and ASA Services Module differs from the SNMPv3 implementation in Cisco IOS Software. The local-engine and remote-engine IDs are not configurable. There is no support for SNMP views. Only USM, VACM, FRAMEWORK, and TARGET MIBs are supported. If needed, SNMP users and groups should also be removed in the correct order.

The following command configures a Cisco ASA device for SNMPv3 with an SNMP server group AUTHGROUP and enables only authentication for this group by using the auth keyword:

```
! snmp-server group AUTHGROUP v3 auth !
```

The following command configures a Cisco ASA device for SNMPv3 with an SNMP server group PRIVGROUP and enables both authentication and encryption for this group by using the priv keyword:

```
! snmp-server group PRIVGROUP v3 priv !
```

The following command configures an SNMPv3 user snmpv3user1 with an MD5 authentication password of authpassword. User snmpv3user2 has an MD5 authentication password of authpassword and a Triple Data Encryption Standard (3DES) encryption password of privpassword :

```
! snmp-server user snmpv3user1 AUTHGROUP v3 auth md5 authpassword 
snmp-server user snmpv3user2 PRIVGROUP v3 auth md5 authpassword priv 3des privpassword !
```

Note that snmp-server user configuration commands are not displayed in the configuration output of the device as required by RFC 3414; therefore, the user password is not viewable from the configuration. The show snmp user command in the following example allows administrators to view the configured users:

```
ASA# show snmp-server user

User name: snmpv3user1
Engine ID: 80000009fe7e9bd7df37970104bb641ffb45ce1eb452604350
storage-type: nonvolatile active
Authentication Protocol: MD5
Privacy Protocol: None
Group-name: AUTHGROUP

User name: snmpv3user2
Engine ID: 80000009fe7e9bd7df37970104bb641ffb45ce1eb452604350
storage-type: nonvolatile active
Authentication Protocol: MD5
Privacy Protocol: 3DES
Group-name: PRIVGROUP
```

Refer to the SNMP section of the Cisco ASA Series General Operations CLI Configuration Guide for more information about this feature.

Logging Best Practices

Event logging provides visibility into the operation of a Cisco ASA device and the network where it is deployed. Cisco ASA Software provides several flexible logging options that can help achieve an organization's network management and visibility goals. These sections provide some basic logging best practices that can help an administrator use logging successfully while minimizing the impact of logging on a Cisco ASA device.

### Send Logs to a Central Location

Sending logging information to a remote syslog server allows administrators to correlate and audit network and security events across network devices more effectively. Note that, by default, syslog messages are transmitted unreliably by UDP and in clear text. For this reason, any protections that a network provides for management traffic (for example, encryption or out-of-band access) should be applied to syslog traffic as well. The following configuration example configures a Cisco ASA device to send logging information to a remote syslog server:

```
! logging host <name of interface> <hostname or ip-address of server> !
```

Refer to the Logging section of the Cisco ASA Series General Operations CLI Configuration Guide for more information about log correlation.

Smart Call Home (SCH) was introduced in Cisco ASA Software version 8.2.2. It offers proactive diagnostics and real-time alerts on the Cisco ASA and provides higher network availability and increased operational efficiency. SCH can also collect syslogs to the central portal page hosted on Cisco's servers. Note that SCH does not serve as a syslog collecting service because certain limitations apply. However, it can collect syslogs at higher levels (warning or error), and under certain conditions it can proactively open service requests and notify the administrators. Refer to Anonymous Reporting and Smart Call Home for more information about the SCH feature.

### Logging Level

Each log message that is generated by a Cisco ASA device is assigned one of eight severity levels that range from level 0, emergency, through level 7, debugging. Unless specifically required, it is advisable to avoid logging at level 7. This level produces an elevated CPU load on the device that can lead to device and network instability. The global configuration command logging trap level is used to specify which logging messages are sent to remote syslog servers. The specified level indicates the lowest severity message that is sent. For buffered logging, the logging buffered level command is used. The following configuration example limits log messages that are sent to remote syslog servers and the local log buffer to levels 0 (emergency) through 6 (information):

```
! logging trap 6
logging buffered 6 !
```

Refer to the Logging section of the Cisco ASA Series General Operations CLI Configuration Guide for more information.

### Disable Logging to Monitor Sessions and the Console

With Cisco ASA Software, it is possible to send log messages to monitor sessions and to the console. Monitor sessions are interactive management sessions in which the EXEC command terminal monitor has been issued. However, doing so can elevate the CPU load of a Cisco ASA device and therefore is not recommended. Instead, administrators are advised to send logging information to the local log buffer, which can be viewed using the show logging command. Use the global configuration commands no logging console and no logging monitor to disable logging to the console sessions and terminal lines. The following configuration example shows the use of these commands:

```
! no logging console
no logging monitor !
```

Refer to Logging section of the Cisco ASA Series General Operations CLI Configuration Guide for more information about global configuration commands.

### Use Buffered Logging

Cisco ASA software supports the use of a local log buffer so that an administrator can view locally generated log messages. The use of buffered logging is highly recommended versus logging to either the console or monitor sessions. There are two configuration options that are relevant when configuring buffered logging: the logging buffer size and the message severities that are stored in the buffer. The size of the logging buffer is configured with the global configuration command logging buffer-size . The lowest severity included in the buffer is configured using the logging buffered command. An administrator is able to view the contents of the logging buffer through the show logging EXEC command. The following configuration example includes the configuration of a logging buffer of 16,384 bytes and a severity of 6, information, indicating that messages at levels 0 (emergency) through 6 (information) are stored:

```
! logging buffer-size 16384
logging buffered 6 !
```

F or more information about buffered logging, see Logging .

### Configure Logging Time Stamps

The configuration of logging time stamps helps administrators and engineers correlate events across network devices. It is important to implement a correct and consistent logging time stamp configuration to enable correlation of logging data. Logging time stamps should be configured to include the date and time with millisecond precision and to include the time zone in use on the device.

The following example includes the configuration of logging time stamps with millisecond precision:

```
! logging timestamp !
```

Software Configuration Management

Administrators are encouraged to follow standard configuration management and logging procedures that will enable configuration rollback, configuration restoration, or misconfiguration tracking.

AAA accounting can be used to track configuration changes on a firewall. If syslogs are collected at a central location, level 5 syslog 111008 (%ASA-5-111008) will also provide a log of the commands executed on a device. In addition, if the firewall is managed through an external management tool, it should be able to provide configuration management logs. The Cisco Security Manager platform manages firewall devices and can provide change management and configuration change logging functionality. Among others, the Smart Call Home feature introduced in Cisco ASA Software version 8.2.2 can provide configuration management by taking periodic snapshots of the configuration and exporting it to the Smart Call Home portal. The configuration archive can then be used to replace or roll back the current running configuration. The following example will configure the Smart Call Home feature to send daily inventory and configuration updates that can later be retrieved by accessing the Smart Call Home portal at https://tools.cisco.com/sch/ . Note : This link requires login because the Smart Call Home feature is a registered service.

```
! service call-home
call-home
contact-email-addr customer@mail.server
profile CiscoSCH
destination address http https://tools.cisco.com/its/service/oddce/services/DDCEService
destination transport-method http
subscribe-to-alert-group inventory periodic monthly
subscribe-to-alert-group configuration periodic monthly !
```

Show or Hide Invalid Usernames in Syslogs

The default setting is to hide usernames when the username is invalid or if the validity is unknown.

Step 1 - Show invalid usernames

```
no logging hide username
```

Step 2 - Hide invalid usernames

```
logging hide username
```

F or more information about the Smart Call Home feature, see Anonymous Reporting and Smart Call Home .

# Securing the Control Plane

Control plane functions consist of the protocols and processes that communicate between network devices to move data from source to destination. These functions include routing protocols such as OSPF in addition to protocols such as ICMP.

It is important that events in the management and data planes do not adversely affect the control plane. If a data plane event such as a DoS attack impacts the control plane, the entire network can become unstable. The information that follows provides features and configurations that can help ensure the resilience of the control plane.

## General Control Plane Hardening

Protection of the control plane of a network device is critical because the control plane ensures that the management and data planes are maintained and operational. If the control plane becomes unstable during a security incident, it may not be possible for administrators and engineers to recover the stability of the network.

### ICMP Redirects

Because of the secure nature and operations of Cisco firewall platforms, the platforms do not support ICMP redirects. A Cisco firewall interface will drop any ICMP redirects it receives.

### ICMP Unreachables

Filtering with an interface access list elicits the transmission of ICMP unreachable messages back to the source of the filtered traffic. Generating these messages can increase CPU utilization on the device. Cisco firewalls can be configured to elicit or suppress ICMP unreachable messages. ICMP unreachables should be filtered to allow only known sources, for example those from management subnets.

The following example illustrates filtering ICMP unreachable messages to permit only messages to known sources sent to the mgmt interface:

! icmp permit host 10.0.0.1 unreachable mgmt !

To alleviate CPU utilization, ICMP unreachable messages are limited to one packet every second by default. ICMP unreachable message generation can be disabled using the global configuration command icmp deny any unreachable <interface> . ICMP unreachable rate limiting can be changed from the default using the icmp unreachable rate-limit rate burst-size size global configuration command.

For details on configuring ICMP unreachables, see icmp unreachable .

### Limiting ICMP Responses

ICMP responses are often used for troubleshooting and monitoring services. Because of the secure nature and operations of Cisco firewall platforms, ICMP responses from the firewall should be limited by filtering traffic to permit only what is necessary or expected. ICMP responses can also be limited by disabling ICMP responses on interfaces, specifically the outside or "untrusted" interface(s) at a minimum. By default Cisco firewalls permit ICMP traffic destined to an interface.

The following command syntax limits ICMP responses on the configure ("if name") interfaces:

! icmp {permit|deny} ip_address net_mask [icmp_type] if_name !

For details on configuring ICMP filtering, see Access Control .

## Securing Routing Protocols

# Routing Protocol Authentication

To enhance security, routing updates may be authenticated using a simple password or keys depending on the routing protocol being used. Use routing protocol authentication to prevent spoofing and routing attacks on firewalls. EIGRP route authentication provides MD5 authentication of routing updates from the EIGRP routing protocol. The MD5 keyed digest in each EIGRP packet prevents the introduction of unauthorized or false routing messages from unapproved sources.

To enable authentication of EIGRP packets and specify the authentication key (leveraging MD5), use the authentication mode eigrp and authentication key eigrp commands (in interface configuration mode) as follows:

! authentication mode eigrp [as-num] md5 ! authentication key eigrp [as-num]{0|8} [key] key-id [key-id] !

To enable authentication of Routing Information Protocol (RIP) version 2 packets and specify the authentication key, use the rip authentication mode and rip authentication key commands (in interface configuration mode) as follows:

! rip authentication mode {text | md5} ! Note: By default "text" authentication is used. We recommend the use of "MD5." rip authentication key {0|8} [key] key-id [key-id] !

To enable authentication of OSPF packets and specify the authentication key, use the ospf authentication and ospf authentication-key commands as follows:

! ospf authentication [key-chain | message-digest | null] ! Note: MD5 is the recommended configuration for ospf authentication, ! therefore the "message-digest" configuration option should be leveraged. ospf authentication key-chain [key] !

# Securing the Data Plane

The firewall data plane handles most of the traff i c that traverses the firewall. Data plane protection can prevent attacks for both the firewall and devices to which the firewall sends traffic.

## General Data Plane Hardening

Securing the control plane and management plane is essential, but all control plane and data plane traffic traverses through the data plane. Because the data plane is responsible for processing and forwarding traffic, protecting the firewall data plane plays an important part in firewall hardening and security. Any activated firewall feature may affect data plane traffic, so it is important to keep the firewall software version updated to the latest stable code that meets business requirements. It is also important to back up all firewall rulebase and configuration files regularly on a separate, accessible location. Backups can be used after a system failure and helps reduce total downtime. The Adaptive Security Algorithm ensures the secure use of applications and services. Some applications require special handling in the Adaptive Security Algorithm firewall application inspection function. These applications embed IP addressing information in the user data packet or open secondary channels on dynamically assigned ports.

Cisco ASA devices support application inspection through the Adaptive Security Algorithm function for basic, voice, video, and mobile network protocols. Ensure that the proper licensing levels are in place for a given inspection set.

## Filtering Transit Traffic with Transit ACLs

A host on one firewall interface can create any type of connection to a host on another interface of the same firewall as long as any required address translation can be made and relevant interface access lists permit it. When address translation methods are required and after they have been configured between pairs of firewall interfaces, the administrator must configure and apply access lists to the interfaces.

The steps required for placing an ACL on the firewall include configuring the ACL and binding it to a firewall interface. Any source and destination address specified in the ACL is relative to any address translation that occurs on the interface where the ACL is applied.

Each permit or deny statement in the ACL is referred to as an access control entry (ACE). ACEs can classify packets by inspecting Layer 2 through Layer 4 headers for a number of parameters, including the following:

- Layer 2 protocol information such as EtherTypes

- Layer 3 protocol information such as ICMP, TCP, or UDP

- Layer 3 header information such as source and destination IP addresses

- Layer 4 header information such as source and destination TCP or UDP ports

After an ACL has been properly configured, the administrator can apply it to an interface to filter traffic. The security appliance can filter packets in both the inbound and outbound direction on an interface. An ACL must be applied to each lower-security interface so that specific inbound connections are permitted. For information about security levels, refer to the Security Levels section of this document.

Note: In downloadable access lists from a RADIUS server, the per-user-override keyword can be added. This keyword allows any downloaded ACLs to override the ACL applied to the interface; the per-user downloaded ACLs are evaluated first, before the interface ACL.

After an access list has been applied inbound/outbound on an interface, all traffic entering/exiting that interface is subject to the ACL entries, and security-level rules defined previously are ignored. Only the first packet in the TCP or UDP flow is matched against the ACL entries. Once the packet is allowed, the flow is created in the Adaptive Security Algorithm connection table, and all further packets in the flow are permitted based on the connection entry, bypassing the ACL check. You can use the show conn command to view the connection table.

Note: ACLs are normally evaluated in the order in which they appear in the firewall configuration. As ACLs grow in length, the time needed to evaluate the ACEs in sequence can also increase.

It is important to configure and use an ACL to limit the types of traffic in a specific direction. When traffic is permitted by an ACL, connections are allowed to pass; when traffic is denied, all corresponding packets are dropped at the firewall. In addition, when an xlate entry is created for a new connection and the interface ACLs permit the initial traffic, the return traffic specific to that connection is also permitted because the firewall has built the proper xlate and conn entries for it.

To configure an ACL, use the following command:

access-list access_list_name [ line line_number ] [ extended ] { deny | permit } protocol source_address mask [ operator port ] dest_address mask [ operator port | icmp_type ] [ inactive ]

Note: Recompiling an ACL is a silent process, but it can burden an already loaded firewall CPU. Therefore, ACL changes should be made when traffic through the firewall is low.

### ACL Configuration Best Practices

This section lists some best practices to be followed for ACL configuration on firewalls. However, the list is not exhaustive and should serve as a guideline for firewall hardening.

To control access to an interface, use the access-group command in interface configuration mode. This rule determines whether there any ACLs are defined that are not applied to an interface.

The permit ip any any command is not recommended. Allowing access to all destinations provides access to all the hosts inside the perimeter, including the firewall itself, and to all Internet hosts. Traffic should be carefully filtered to meet the organization's requirements.

The permit icmp any any command is also not recommended. It is not secure to permit all ICMP traffic on firewalls, which would allow an attacker to exploit the network using ICMP attacks such as ping sweeps and ping floods. Traffic should be carefully filtered to meet the organization's requirements. Also, ICMP generally requires enabling icmp inspection because the ICMP inspection engine allows ICMP traffic to have a "session" so it can be inspected like TCP and UDP traffic. Without the ICMP inspection engine, we recommend that you do not allow ICMP through the ASA in an access list. Without stateful inspection, ICMP can be used to attack your network. The ICMP inspection engine ensures that there is only one response for each request, and that the sequence number is correct.

The best practice is to use ACLs to limit as much traffic as possible. Administrators are advised to create exact matches of host and network addresses rather than using the generic keyword any in access lists. Specifying the exact port numbers is recommended rather than opening all ports by not specifying anything in the ports field. Increased granularity increases security and also makes it easier to troubleshoot any malicious behavior.

It is a best practice to have an explicit deny statement at the end and log all the denied packets. The log keyword at the end of the individual ACL entries shows the ACL number and whether the packet was permitted or denied in addition to port-specific information. By default, logging message 106023 (default severity level 4, warning) is generated when a deny access list entry is matched with a traffic flow. One can log messages when specific ACEs permit or deny a traffic flow because the log keyword is added to the ACE. One can also log the rate at which traffic flows match specific access list entries. This can be useful to gauge the volume of attacks or exploits that are occurring over time. One can also set the logging severity level on a per-ACE basis if needed. Otherwise, severity level 6 is the default. Note: Although all ACLs contain an implicit deny statement, Cisco recommends use of an explicit deny statement, for example, deny ip any any . On most platforms, such statements maintain a count of the number of denied packets. This count can be displayed using the show access-list command.

ACL Match Limits

If the number of objects matched by the source address times the number matched by the destination address exceeds 10,000 then the connection is dropped. Configure your rules to prevent an excessive number of matches.

### Security Levels

The ability to configure security levels is a necessary firewall feature. A security-level value from 0 through 100 defines the trustworthiness of networks reachable through an interface. A value of 0 indicates the least trusted, and a value of 100 indicates the most trusted. Administrators are advised to correctly configure security levels for traffic traversal before ACLs are applied. The following are the key points:

- By default, all outbound traffic from higher-security-level interfaces to lower-security-level interfaces is allowed.

- By default, all inbound traffic from lower-security-level interfaces to higher-security-level interfaces is denied; to pass, this traffic needs to be allowed in an ACL applied inbound on the lower-security-level interface.

- Traffic between interfaces with the same security level is denied by default and can be allowed to pass by enabling the same security-traffic permit inter-interface command globally on the appliance.

- Traffic entering the appliance via one interface and exiting it via the same interface, known as a "U-turn," is denied by default and can be allowed to pass by enabling the same-security-traffic permit intra-interface command globally on the appliance.

The following command configures the security level:

hostname(config)# interface <interface_name> hostname(config-if)# security-level number

For more details regarding security levels, see Security Levels .

## Content and URL Filtering

Traditionally, firewalls filter data packets by analyzing Layer 3 and/or Layer 4 header information. Cisco firewalls can enhance this functionality by inspecting the content information in many Layer 7 protocols such as HTTP, HTTPS, and FTP. Based on an organization's security policy, the security appliance can either pass or drop the packets if they contain content not allowed in the network. Cisco firewalls support two types of application layer filtering: content filtering and URL filtering.

### Content Filtering

Cisco firewalls can differentiate friendly applets from untrusted applets. If a trusted website sends Java or ActiveX applets, the security appliance can forward them to the host requesting the connection. If the applets are sent from untrusted web servers, the security appliance can modify the content and remove the applets from the packets. This way, end users are not making decisions regarding which applet to accept or refuse. They can download any applets without taking extra precautions. The <OBJECT ID> and </OBJECT> HTML tags are used to insert ActiveX code into a web page. The security appliance searches for these tags for traffic that originated on a preconfigured port. If the security appliance finds these tags, it replaces them with the comment tags <!— and —>. When the browser receives the HTTP packets with <!— and —>, it ignores the actual content by assuming that the content contains the author's comments. A local content filtering server can be set up on the security appliance by using the filter command, followed by the name of the type of content to be removed. The following shows the complete command syntax:

filter activex|java|ftp|https|url [port or port range <start>[<end>]  local_ip local_mask foreign_ip foreign_mask

### URL Filtering

Cisco firewalls can delegate packet-filtering responsibilities to an external server. Administrators can define an external filtering server by using the url-server command. For example, the complete command syntax to specify a Websense server is:

url-server (if_name) vendor websense host local_ip  timeout [<seconds>] protocol [TCP|UDP] connections [num_conns] [version 1 |4]

To define a SmartFilter server, the command syntax is

url-server [ <(if_name) >] vendor {smartfilter | n2h2} host <local_ip> [port <number>] [ timeout <seconds>] [protocol TCP|UDP] [connections num_conns] ]

Note: Users may experience longer access times if the response from the filtering server is slow or delayed. This may happen if the filtering server is located at a remote location and the WAN link is slow. In addition, slow response times may also result if the URL server cannot keep up with the number of requests being sent to it. The url-server command does not verify whether a Websense or SmartFilter server is reachable from the security appliance. You can specify up to 16 filtering servers for redundancy. If the security appliance is not able to reach the first server in the list, it tries the second server from the list, and so on. In addition, Cisco ASA does not allow both SmartFilter and Websense servers to be defined at the same time. One must be deleted before the other is set up.

## Service Policies (Modular Policy Framework)

Service policies using Modular Policy Framework provide a consistent and flexible way to configure ASA features. For example, you can use a service policy to create a timeout configuration that is specific to a particular TCP application, as opposed to one that applies to all TCP applications. A service policy consists of multiple actions or rules applied to an interface or applied globally.

Service Policies are supported with these features:

- TCP and general connection settings

- Protocol inspection services

- Intrusion prevention services

- QoS services

- Policing (rate limiting)

The configuration of Service Policies consists of four tasks:

- Identify the Layer 3 and Layer 4 traffic to which you want to apply actions. See Service Policy for more information.

- (Application inspection only.) Define special actions for application inspection traffic. See Getting Started with Application Layer Protocol Inspection for more information.

- Apply actions to the Layer 3 and Layer 4 traffic. Refer to Configuring Service Policies for more information.

- Activate the actions on an interface. Refer to Configuring Service Policies for more information.

## Anti-Spoofing Protections

IP spoofing occurs when a potential intruder copies or falsifies a trusted source IP address. This is typically employed as an auxiliary technique for countless types of network-based attacks. Cisco firewalls contain several features to enhance the ability of the network to defend itself. Antispoofing is one such feature, which helps to protect an interface of the ASA by verifying that the source of network traffic is valid. This section discusses some antispoofing features.

### Unicast Reverse Path Forwarding

Network administrators can use Unicast Reverse Path Forwarding (uRPF) to help limit malicious traffic on a network. This security feature works by enabling a router to verify the reachability of the source address in packets being forwarded. This capability can limit the appearance of spoofed addresses on a network. If the source IP address is not valid, the packet is discarded. uRPF guards against IP spoofing by ensuring that all packets have a source IP address that matches the correct source interface according to the routing table. Normally, the security appliance examines only the destination address when determining where to forward the packet. uRPF instructs the security appliance to look also at the source address. For any traffic to be allowed through the security appliance, the security appliance routing table must include a route back to the source address. See RFC 2267 for more information. To enable uRPF, enter this command:

hostname(config)# ip verify reverse-path interface interface_name

uRPF works in two different modes: strict mode and loose mode. When administrators use uRPF in strict mode, the packet must be received on the interface that the security device would use to forward the return packet. uRPF in strict mode may drop legitimate traffic that is received on an interface that was not the firewall's choice for sending return traffic. Dropping this legitimate traffic could occur when asymmetric routing paths exist in the network. When administrators use uRPF in loose mode, the source address must appear in the routing table. Administrators can change this behavior using the allow-default option, which allows the use of the default route in the source verification process. In addition, a packet that contains a source address for which the return route points to the Null 0 interface will be dropped. An access list may also be specified that permits or denies certain source addresses in uRPF loose mode. Care must be taken to ensure that the appropriate uRPF mode (loose or strict) is configured during the deployment of this feature because it can drop legitimate traffic. Although asymmetric traffic flows may be a concern when deploying this feature, uRPF loose mode is a scalable option for networks that contain asymmetric routing paths.

Also be sure NOT to enable unicast RPF (ip verify reverse-path command) on the egress interface of a tunneled route, because this setting causes the session to fail.

### Antispoofing with Access Lists

RFC 2827 (BCP 38) describes uses of access lists as a current best practice to defeat IP source address spoofing. This RFC is a widespread resource, particularly for the Internet edge, because in such an environment the boundary between private and public addresses (in the sense of RFC 1918) is clearly demarcated. It is usually appropriate for an antispoofing access list to filter out all ICMP redirects regardless of source or destination address. These are just basic guidelines and can be further fine tuned with other filtering such as anti-bogon, which filters traffic that claims to be sourced from reserved addresses or from an IPv4 block that has yet to be allocated by the Internet Assigned Numbers Authority (IANA). In general, antispoofing filters are best deployed as input access lists; that is, packets must be filtered at the arriving interfaces, not at the interfaces through which they exit. The input access list also protects the firewall itself from spoofing attacks, whereas an output list protects only devices behind the firewall.

### Inspection

Cisco ASA supports application inspection through the Adaptive Security Algorithm function. Through the stateful application inspection used by the Adaptive Security Algorithm, the Cisco ASA tracks each connection that traverses the firewall and ensures that it is valid. The firewall, through stateful inspection, also monitors the state of the connection to compile information to place in a state table. With the use of the state table in addition to administrator-defined rules, filtering decisions are based on context that is established by packets previously passed through the firewall. The implementation of application inspections consists of these actions:

- Identify the traffic

- Apply inspections to the traffic

- Activate inspections on an interface

By default, the configuration includes a policy that matches all default application inspection traffic and applies certain inspections to the traffic on all interfaces (a global policy). Not all inspections are enabled by default. Only one global policy can be applied. If it is necessary to alter the global policy, one must either edit the default policy or disable it and apply a new one. (An interface policy overrides the global policy.) The default policy configuration includes these commands:

class-map inspection_default

match default-inspection-traffic

policy-map type inspect dns preset_dns_map

parameters

message-length maximum 512

policy-map global_policy

class inspection_default

inspect dns preset_dns_map

inspect ftp

inspect h323 h225

inspect h323 ras

inspect rsh

inspect rtsp

inspect esmtp

inspect sqlnet

inspect skinny

inspect sunrpc

inspect xdmcp

inspect sip

inspect netbios

inspect tftp

service-policy global_policy global

To disable global inspection for an application, use the no version of the inspect command.

### Enable Inspection for Nondefault Applications

Enhanced HTTP inspection is disabled by default. To enable HTTP application inspection or change the ports on which the security appliance listens, use the inspect http command in class configuration mode. Class configuration mode is accessible from policy map configuration mode. To remove the configuration, use the no form of this command. When used in conjunction with the http-map argument, the inspect http command protects against specific attacks and other threats that may be associated with HTTP traffic. Two of the basic checks of this engine ensure conformance to RFC 2616 and the use of RFC-defined methods only. Any HTTP flow that does not adhere to the basic checks is dropped by default. Many HTTP applications, even internal applications, do not conform. The action can be changed from dropped to logged, if required. For more information on using the http-map argument with the inspect http command, see HTTP Inspection .

For more information on  FTP and TFTP inspection filtering, see Inspection of Basic Internet Protocols .

To remove global inspection for the FTP application to which the Cisco ASA listens, administrators are advised to use the no inspect ftp command in class configuration mode. Two inspection engines that should be enabled during installation are ICMP and ICMP error inspection. The ICMP inspection engine allows ICMP traffic to be inspected in the same way as TCP and UDP traffic. Without the ICMP inspection engine, it is recommended not to allow ICMP through the Cisco ASA in an ACL. Without stateful inspection, ICMP can be used to attack a network. The ICMP inspection engine ensures that there is only one response for each request, and that the sequence number is correct.

Commands to enable ICMP inspection follow:

policy-map global_policy

class inspection_default

inspect icmp

inspect icmp error

For more details regarding ICMP inspection, see Inspection of Basic Internet Protocols .

### ACLs to Block Private and Bogon Addresses

Unallocated IP addresses, IP addresses for private internets as mentioned in RFC 1918 , and special use IP addresses as mentioned in RFC 3330 can be a problem when they are used to route packets on the Internet. These addresses can be used to source attacks that could make it difficult or impossible to trace back to the source. Filtering these addresses at your network boundary will provide another layer of security. The official list of unallocated bogon Internet addresses is maintained by Team Cymru .

## Denial of Service Protections

Antispoofing will ensure that DoS attacks are not launched from inside the network. Administrators are advised to follow this procedure to enable antispoofing on the inside interface to ensure DoS attacks are not inadvertently being launched from the inside the security appliance. Step 1: Identify the traffic to apply connection limits using a class map

ASA(config)# access list CONNS-ACL extended permit ip any 10.1.1.1 255.255.255.255 ASA(config)# class-map CONNS-MAP ASA(config-cmap)# match access-list CONNS-ACL

Step 2: Add a policy map to set the actions to take on the class map traffic

ASA(config)# policy-map CONNS-POLICY ASA(config-pmap)# class CONNS-MAP ! The following sets connection number limits ASA(config-pmap-c)# set connection {[conn-max n] [embryonic-conn-max n] [per-client-embryonic-max n] [per-client-max n] [random-sequence-number {enable | disable}]}

### Threat Detection

Cisco ASA supports the threat detection feature in software versions 8.0 and later. Using basic threat detection, the security appliance monitors the rate of dropped packets and security events caused by the following:

- Denial by access lists.

- Bad packet format, such as invalid-ip-header or invalid-tcp-hdr-length).

- Connection limits exceeded, both system-wide resource limits and limits set in the configuration.

- DoS attack detected, such as an invalid stateful packet inspection or stateful firewall check failure.

- Basic firewall checks failed. This option is a combined rate that includes all firewall-related packet drops in this bulleted list. It does not include non-firewall-related drops such as interface overload, packets failed at application inspection, and scanning attack detected.

- Suspicious ICMP packets detected.

- Packets failed application inspection.

- Interface overload.

- Scanning attack detected. This option monitors scanning attacks; for example, the first TCP packet is not a SYN packet or the TCP connection failed the three-way handshake. Full scanning threat detection takes this scanning attack rate information and acts on it by classifying hosts as attackers and automatically shunning them, for example. See Threat Detection for more information.

- Incomplete session detection, such as TCP SYN attack detected or no-data UDP session attack detected.

The types of commands are as follows:

- Embryonic (half-opened) connection: An embryonic connection is a TCP connection request that has not finished the necessary handshake between source and destination.

- Half-closed connection: A half closed connection is when the connection is closed only in one direction by sending FIN. However, the TCP session is still maintained by the peer.

- per-client-embryonic-max: This command sets the maximum number of simultaneous embryonic connections allowed per client, from 0 through 65535. The default is 0, which allows unlimited connections.

- per-client-max: This command sets the maximum number of simultaneous connections allowed per client, from 0 through 65535. The default is 0, which allows unlimited connections.

The show threat-detection rate command is used to identify potential attacks when the administrator is logged in to the security appliance.

ciscoasa# show threat-detection rate

Average(eps) Current(eps) Trigger Total events

10-min ACL drop: 0 0 0 16

1-hour ACL drop: 0 0 0 112

1-hour SYN attck: 5 0 2 21438

10-min Scanning: 0 0 29 193

1-hour Scanning: 106 0 10 384776

1-hour Bad pkts: 76 0 2 274690

10-min Firewall: 0 0 3 22

1-hour Firewall: 76 0 2 274844

10-min DoS attck: 0 0 0 6

1-hour DoS attck: 0 0 0 42

10-min Interface: 0 0 0 204

1-hour Interface: 88 0 0 318225

Refer to Threat Detection for more information on the configuration. When the security appliance detects a threat, it immediately sends a system log message (730100). Note: Basic threat detection affects performance only when there are drops or potential threats.

### Connection Limiting

If the embryonic connection limit is reached, the security appliance responds to every SYN packet sent to the server with a SYN+ACK and does not pass the SYN packet to the internal server. If the external device responds with an ACK packet, the security appliance knows it is a valid request (and not part of a potential SYN attack). The security appliance then establishes a connection with the server and joins the connections together. If the security appliance does not get an ACK back from the server, it aggressively times out that embryonic connection. Other options are to configure maximum connections, maximum embryonic connections, and TCP sequence randomization in the NAT configuration. If these settings are configured for the same traffic using both methods, the security appliance uses the lower limit. If TCP sequence randomization is disabled, the security appliance disables TCP sequence randomization. To set the maximum connections (both TCP and UDP), maximum embryonic connections, per-client-embryonic-max, or per-client-max, or to indicate whether to disable TCP sequence randomization, administrators can enter this command:

hostname(config-pmap-c)# set connection {[ conn-max number] [ embryonic-conn-max number] [ per-client-embryonic-max number] [ per-client-max number][ random-sequence-number { enable | disable }}

Recall that the per-client-max and per-client-embryonic-max is an integer from 0 through 65535 and the default is 0, which means no limit on connections. Administrators can enter this command all on one line (in any order) or enter each attribute as a separate command. The command is combined on one line in the running configuration. To set the timeout for connections, embryonic connections (half-opened), and half-closed connections, administrators can enter this command:

hostname(config-pmap-c)# set connection {[ embryonic hh[:mm[:ss]]]

[ half-closed hh[:mm[:ss]]] [ tcp hh[:mm[:ss]]]}

The embryonic hh[:mm[:ss] is a time from 0:0:5 through 1193:0:0. The default is 0:0:30. Administrators can also set this value to 0, which means the connection never times out. The half-closed hh[:mm[:ss] and tcp hh[:mm[:ss] values are a time from 0:5:0 through 1193:0:0. The default for half-closed is 0:10:0 and the default for tcp is 1:0:0. These values can also be set to 0, which means the connection never times out.

### TCP Normalizer

TCP normalization is a Layer 4 feature that consists of a series of checks that the firewall application performs at various stages of a flow, from initial connection setup to the closing of a connection. Many of the segment checks can be controlled by configuring one or more advanced TCP connection settings. The firewall application uses these TCP connection settings to decide which checks to perform and whether to discard a TCP segment based on the results of the checks. The firewall application discards segments that appear to be abnormal or malformed. This feature also checks for segments that have invalid or suspect conditions (for example, a SYN sent to the client from the server or a SYNACK sent to the server from the client) and takes appropriate actions based on the configured parameter settings. The firewall application uses TCP normalization to block certain types of network attacks (for example, insertion attacks and evasion attacks). Insertion attacks devise a scheme so that the inspection module accepts a packet that the end system rejects. Evasion attacks devise a scheme such that the inspection module rejects a packet while the end system accepts it. For more details regarding the TCP Normalizer feature, see TCP Normalization . The firewall application always discards segments when the following conditions exist:

- Bad segment checksum

- Bad TCP header or payload length

- Suspect TCP flags (for example, NULL, SYN/FIN, or FIN/URG)

The TCP normalization feature identifies abnormal packets that the Cisco ASA can act on when they are detected; for example, the adaptive security appliance can allow, drop, or clear the packets. TCP normalization helps protect the Cisco ASA from attacks. TCP normalization is always enabled, but administrators can customize how some features behave. The TCP normalizer includes nonconfigurable actions and configurable actions. Typically, nonconfigurable actions that drop or clear connections apply to packets that are always bad. Configurable actions may need to be customized depending on network needs. See the following guidelines for TCP normalization:

- The normalizer does not protect from SYN floods. Cisco ASA includes SYN flood protection in other ways.

- The normalizer always sees the SYN packet as the first packet in a flow unless Cisco ASA is in loose mode because of failover.

This feature uses the Modular Policy Framework so that customizing TCP normalization consists of identifying traffic, specifying the TCP normalization actions, and activating TCP normalization customization on an interface. See Service Policy for more information.

### Botnet Protection

A Botnet is a collection of autonomous software robots (bots), typically malicious in nature, that operate as a network of compromised computers. An originator, also known as a "bot herder," typically controls the bots and can launch them at will using command-and-control communication between the controller and the bots. Botnets have proven to be a malicious adversary to today's network environment and therefore must be curtailed with proper defense mechanisms. Cisco ASA 5500 Series Adaptive Security Appliances provide reputation-based control for an IP address or domain name. The Cisco ASA Botnet Traffic Filter is integrated into all Cisco ASA appliances and inspects traffic traversing the appliance to detect rogue traffic in the network. When internal clients are infected with malware and attempt to phone home across the network, the Botnet Traffic Filter alerts the system administrator of these attempts though the regular logging process for manual intervention. This is an effective way to combat botnets and other malware that shares the same phone-home communications pattern. The Botnet Traffic Filter feature does not automatically block botnet-related traffic. An administrator must manually configure ACLs to block malicious traffic. The Botnet Traffic Filter monitors all ports and performs a real-time lookup in its database of known botnet IP addresses and domain names. Based on this investigation, the Botnet Traffic Filter will determine whether a connection attempt is benign and should be allowed or whether it is a risk and should be tagged for mitigation. When the Botnet Traffic Filter feature is enabled, the Cisco ASA compares DNS A-records and CNAME records against the domain names in the database. This process is known as DNS snooping and is integrated with the current DNS inspection available on the ASA. When DNS snooping is enabled, the Cisco ASA builds a DNS reverse cache (DNSRC) for all the DNS replies received on interfaces where DNS snooping is enabled. For a comprehensive understanding and more details regarding Botnet mitigation leveraging the Botnet Traffic Filter option of the Cisco ASA, see Cisco ASA Botnet Traffic Filter Guide .

Cisco Trustsec for ASA

Cisco TrustSec provides access control that builds upon an existing identity-aware infrastructure to ensure data confidentiality between network devices and integrate security access services on one platform. In the Cisco TrustSec feature, enforcement devices use a combination of user attributes and endpoint attributes to make role-based and identity-based access control decisions. The availability and propagation of this information enables security across networks at the access, distribution, and core layers of the network.

Implementing Cisco TrustSec into your environment has the following advantages:

- Provides a growing mobile and complex workforce with appropriate and more secure access from any device.

- Lowers security risks by providing comprehensive visibility of who and what is connecting to the wired or wireless network.

- Offers exceptional control over activity of network users accessing physical or cloud-based IT resources.

- Reduces total cost of ownership through centralized, highly secure access policy management and scalable enforcement mechanisms.

For more information, see the following resources:

- Description of the Cisco TrustSec system and architecture for the enterprise. http://www.cisco.com/c/en/us/solutions/enterprise-networks/trustsec/index.html

- Instructions for deploying the Cisco TrustSec solution in the enterprise, including links to component design guides. http://www.cisco.com/c/en/us/solutions/enterprise/design-zone-security/landing_DesignZone_TrustSec.html

- An overview of the Cisco TrustSec solution when used with the ASA, switches, wireless LAN (WLAN) controllers, and routers. http://www.cisco.com/c/en/us/solutions/collateral/enterprise-networks/trustsec/solution_overview_c22-591771.pdf

- The Cisco TrustSec Platform Support Matrix, which lists the Cisco products that support the Cisco TrustSec solution. http://www.cisco.com/c/en/us/solutions/enterprise-networks/trustsec/trustsec_matrix.html

## Limiting the CPU Impact of Data Plane Traffic

It is key to understand the CPU impacts of the firewall. To achieve this, administrators must keep track of the health and stats of the firewall. It is important to note that sustained CPU spikes, that is, typically 80 percent or above, while passing "normal" traffic events requires a call to action and further design and scaling considerations. In addition, special consideration should be given in the occurrence of multiple context firewalls. In the case of multiple context firewalls, the performance (CPU) impacts of the firewall must be managed holistically (across all contexts). Use the show cpu usage context all command to view the CPU resources of all configured contexts of the firewall. To see the entire list of active firewall processes, administrators can use the show processes command. The primary available information follows:

- Process: Displays a descriptive name for the process, such as update_cpu_usage , that computes the values for the show cpu usage command

- Runtime: Lists the actual amount of time the CPU has spent on each process, in milliseconds. The runtime values begin at 0 when the firewall is first booted and accumulate until it is powered down or reloaded.

As a rule of thumb, the CPU utilization should stay below an average of 80 percent. The utilization may spike or temporarily peak at a greater value, as often seen in the outputs of the 5-second utilization field of the show cpu usage output. This is normal behavior because the CPU could be processing a periodic task or a short burst of traffic. Note that firewall logging and alerts should be enabled only when required because these functions impact the processor cycles and may lead to a degradation in firewall performance. It is also important to run features on the firewall only when absolutely necessary. Each application affects CPU cycles and therefore the throughput of the network. Limit the number of applications that run on the firewall to maximize CPU cycles and network throughput.

## Traffic Identification and Traceback

There are many ways to set up the appliance for packet filtering. The most common methods are as follows:

- Through traffic filtering using the CLI

Note : This method uses ACL configurations for traffic filtering through the box. For more details, see Access Lists and Access Rule s.

- Through traffic filtering using ASDM

Note : This method also uses ACL configurations for traffic filtering through the box. For more details, see Access Control Lists .

- To-the-box traffic filtering

Note : To-the-box traffic filtering most often applies to management plane traffic. For more details, see Cisco ASA Series General Operations CLI Configuration Guide .

- IP version 6 (IPv6) traffic filtering

Due to the unique nature of IPv6 filtering, this method will be discussed at length below.

### IPv6 Traffic Filtering

If IPv6 traffic is used in the network, an IPv6 ACL can be configured if desired to control the traffic passing through the security appliance. The IPv6 ACL can be defined by using the ipv6 access-list command followed by the name of the ACL. Like an extended ACL, the IPv6 ACL uses similar command options, as shown in the following syntax:

ipv6 access-list id [line line-num] {deny | permit} {protocol | object-group protocol_obj_grp_id} {source-ipv6-prefix/prefix-length | any | host source-ipv6address | object-group network_obj_grp_id} [operator {port [ port] | object-group service_obj_grp_id}] {destination-ipv6-prefix/prefix-length | any | host destination-ipv6-address | object-group network_obj_grp_id} [log [ [level] [interval secs] | disable | default]]

For more details regarding IPv6 traffic filtering, see Objects for Access Control .

## High Availability Security

The firewall offers a failover function that provides a safeguard mechanism in the event of a unit failure. When one unit fails, another immediately takes its place. The Security Appliance supports the following two types of failover setup. Both failover modes support stateful or stateless failover.

- Active/Standby Failover Mode: In this mode, only one unit (the primary, also called the Active unit) passes traffic, whereas the other unit is in a standby state. The Active/Standby failover is available in both single and multiple context modes. For more details, see Failover for High Availability .

- Active/Active Failover Mode: In this mode, either the primary or secondary may be the active device. The normal procedure is to connect to the active device during normal maintenance and testing. For more details, see Failover for High Availability .

High availability (HA) solutions should also be secured. As all information between the two firewalls in an HA configuration is sent (in clear text) over the failover/stateful failover link(s), the key to securing the Cisco firewall HA solution is to secure the communication with a failover key. Note specifically if the ASA is used to terminate VPN tunnels, unless using a failover key, the following information is sent in the clear: any usernames, passwords, and preshared keys used for establishing the tunnels. As stated in the Cisco ASA 5500 Configuration Guide, "Transmitting this sensitive data in clear text could pose a significant security risk. We recommend securing the failover communication with a failover key if you are using the ASA to terminate VPN tunnels." For more details on High Availability configurations,  see Failover for High Availability .

## Best Practices Checklist

### Management Plane Checks

Disable Console Logging - Firewall

Requirement

Severity

Comments

Disable Console Logging

Low

Best practice: Ensure console logging is disabled or set to critical. Although useful for troubleshooting from the console port, it is possible that excessive log messages on the console could make it impossible to manage the device, even from the console. Command: no logging console - or - logging console critical

Enable Logging - Firewall

Requirement

Severity

Comments

Enable Logging

Info

Best practice: Check if state of event logging on the firewall is enabled. Command: logging on | logging enable

Enable Logging Timestamp

Low

Best practice: Timestamps should be enabled for log messages, which will facilitate interpretation of the messages for troubleshooting and investigating network attacks. Ensure that the date/time is correctly set (if NTP is not configured) so that the timestamps provide the proper day/time of the log messages. If the timestamps are not shown in the log messages, it may not be possible to sense the order of events occurring in the network. Command: logging timestamp

Enable Logging to Buffer

Low

Best practice: Cisco devices can store log messages in memory. The buffered data is available only from an exec or enabled exec session, and it is cleared when the device reboots. This form of logging is useful, even though it does not offer enough long-term protection for the logs. Buffered logging keeps the log messages in RAM on the device. A logging buffer must be configured on the device, and this buffer is circular, meaning that when it fills up, the oldest log message is deleted to make room for the new message. If buffer logging is not enabled, it will not be possible to view the most recent log messages on the device for troubleshooting or monitoring purposes. Command: logging buffered <level>

Log Messages to a Syslog Server

Info

Best practice: Cisco devices can be configured to forward log messages to an external Syslog service. It is highly recommended that networks implement a logging structure based on a Syslog infrastructure. Proactive monitoring of firewall logs is an integral part of Security Admin duties. The firewall syslogs are useful for forensics, network troubleshooting, security evaluation, worm and virus attack mitigation, and so on. This is a scalable solution, which provides long-term storage capabilities and a central location for all device messages Command: logging host <interface-name> <ipAddress>

Secure Device Access - Firewall

Requirement

Severity

Comments

Restrict HTTP Access to Certain Addresses

Info

Best practice: To specify hosts that can access the HTTP server internal to the ASA. The addresses allowed to access the firewall using HTTP can be restricted. Any undefined IP address will not see the prompt at all. Command: http <ip-address> <net-mask> <interface name>

Restrict SSH Access to Certain Addresses

Medium

Best practice: The addresses allowed to access the firewall using SSH can be restricted. Any undefined IP address will not see the prompt at all. Command: ssh <ip-address> <net-mask> <interface name>

Restrict Telnet Access to Certain Addresses

Medium

Best practice: The addresses allowed to access the firewall using Telnet can be restricted. Any undefined IP address will not see the prompt at all. Command: telnet <ip-address> <net-mask> <interface name>

Set Enable Password

Info

Best practice: Set enable password to secure access to privilege level. Access to the privileged EXEC mode (enable mode) should be protected by requiring a password else user logged in to user mode can access enable mode. Command: enable password <password>

Set Password

Info

Best practice: To set the login password, use the passwd command in global configuration mode. You are prompted for the login password when you access the CLI as the default user using Telnet or SSH. After you enter the login password, you are in user EXEC mode. Command: passwd <password>

Set Suitable Console Timeout

Low

Best practice : For console connections the idle timeout must be configured to avoid undesirable open and unattended console connection to the firewall.

Command : console timeout

Set Suitable SSH Timeout

Low

Best practice: For ssh connections the idle timeout must be configured to avoid undesirable and unattended open ssh connections to the firewall. Command: ssh timeout <timeout in minutes>

Use Warning Banner Messages

Low

Best practice: Use of configurable, personalized login and failed-login banners is recommended. This feature lets you change the default message for login and failed-login. You can configure message banners that will be displayed when a user logs in to the system Command: banner <banner-message>

Secure Interactive Access Using AAA - Firewall

Requirement

Severity

Comments

Define AAA Server with Key

Medium

Best practice: An Authentication Authorization and Accounting Server (AAA) is recommended to store all the username / password and privilege levels in one single repository. AAA server should be configured with a key for authentication and encryption. Command: aaa-server TACACS+ <interface> host <ipAddress> <key>

Use AAA Accounting

Low

Best practice: When you configure the aaa accounting command, each command other than show commands entered by an administrator is recorded and sent to the accounting server or servers. Command: aaa accounting command EXAUTH LOCAL

Use AAA Authentication for Enable Mode

Medium

Best practice: Authenticates users who access privileged EXEC mode when they use the enable command. For authentication an external server may be used and also supports fallback to local database if external authentication server is down. Command: aaa authentication enable console RADIUS LOCAL

Use AAA Authentication for HTTP

Medium

Best practice: If aaa authentication http console command is not defined, you can gain access to the ASA (via ASDM) with no username and the ASA enable password (set with the enable password command). Command: aaa authentication http console RADIUS LOCAL

Use AAA Authentication for SSH

Info

Best practice: Before the firewall can authenticate a Telnet or SSH user, we must first configure access to the firewall using the telnet or ssh commands. These commands identify the IP addresses that are allowed to communicate with the firewall. Command: aaa authentication ssh console RADIUS LOCAL

Use AAA Authorization

Low

Best practice: The aaa authorization command specifies whether command execution at the CLI is subject to authorization. If you enable TACACS+ command authorization, and a user enters a command at the CLI, the ASA sends the command and username to the TACACS+ server to determine if the command is authorized. When configuring command authorization with a TACACS+ server, do not save your configuration until you are sure it works the way you want. If you get locked out because of a mistake, you can usually recover access by restarting the ASA. Command: aaa authorization command TACACS LOCAL

Use Local Login as Backup to AAA

Info

Best practice: While configuring external authentication it is advisable to keep the local database check as fallback option. Command: aaa authentication http console RADIUS LOCAL

Secure Management Protocols - Firewall

Requirement

Severity

Comments

Authenticate NTP Updates

Medium

Best practice: Network Time Protocol (NTP) is a UDP based protocol used to synchronize time clocks amongst network devices. NTP is especially useful to ensure that timestamps on log messages are consistent throughout the entire network. It is recommended to authenticate NTP updates so that time is synchronized with approved servers only. Command: ntp authentication-key <key-id> md5 <key>

Change Default Community String

High

Best practice: The default community string of "public" and "private" are well known. These should always be changed to more secure strings. Command: snmp-server community <non-default-string>

Define SNMP Server Host

Low

Best practice: SNMP is an application-layer communication protocol that allows ONS 15454 network devices to exchange management information among these systems and with other devices outside the network. SNMP is used in network management systems to monitor network-attached devices for conditions that warrant administrative attention. Command: snmp-server host

Disable SNMP if not used

Low

Best practice: SNMP Protocol should be disabled if not used in the network. If used, access to SNMP service should be protected using appropriate mechanisms like ACLs. Command: no snmp-server

Enable SNMP Trap Logging

Low

Best practice: SNMP traps are used to report an alert or other asynchronous event about a managed firewall. Command: snmp server enable traps

Use NTP to Synch Network Clocks

Medium

Best practice: Network Time Protocol (NTP) is a UDP based protocol used to synchronize time clocks amongst network devices. NTP is especially useful to ensure that timestamps on log messages are consistent throughout the entire network. Command: ntp server <ntp server name> source <interface>

### Control Plane Checks

Disable Unneeded Services - Firewall

Requirement

Severity

Comments

Check if Failover is used

Info

Best practice: This rule checks if failover is configured in the firewall devices Command: failover

Disable HTTP session replication

Info

Best practice: The replication of http session data to the failover firewall should be disabled unless the firewall is not expected to be under extreme load and the http session data is highly critical. Given the short duration of http sessions, low probably of firewall failure and the design of most applications, this is not likely to be needed. This rule checks only firewalls with failover configured. Command: no failover replication http

Disable Proxy ARPs

Low

Best practice: Proxy ARP allows a firewall to extend the network at layer 2 across multiple interfaces (i.e. LAN segments). Hence proxy ARP allows hosts from different segments to function as if they were on the same subnet, and is only safe when used between trusted LAN segments. Attackers can use the trusting nature of proxy ARP by spoofing a trusted host and intercepting packets. Because of this inherent security weakness, proxy ARP should be disabled on interfaces that do not require it, especially those interfaces that connect to untrusted networks. Command: sysopt noproxyarp <interface>

Limit ICMP responses on interfaces

Low

Best practice: Preferable to disable ICMP on outside interfaces at a minimum. The default (i.e. no ICMP control list is configured), is for the ASA to accept all ICMP traffic that terminates at any interface (including the outside interface). This will depend on the customer policy. Command: icmp permit <acl> <interface>

Medium

### Data Plane Checks

There are numerous techniques of securing the data plane in firewalls, which will be discussed in this section. Packet filtering, stateful inspection, proxies and application level inspection are one of the basic aspects of data plane security. It is never recommended to rely on one method of data plane security alone. It is best to use a combination of methods available as covered in this section.

Data Plane - Firewall

Requirement

Severity

Comments

Enable uRPF anti-spoofing

Info

Best practice: Anti-spoofing should be configured on all outside interfaces. This rule checks if uRFP is enabled on any one interface. Command: ip verify reverse-path interface <interface-name>

Enable dnsguard

Info

Best practice: Enforces one DNS response per query. Command: dns-guard

Configure Basic Threat Detection

Info

Best practice: Basic threat detection statistics is enabled by default. Command: threat-detection basic-threat

Configure objects for use in access-control-lists

Info

Reduce performance degradation during object lookup

Info

# Conclusion

The ability to understand device hardening at the core of security architecture design and implementation is essential to success. As the threat landscape continues to evolve, the reliance on risk analysis and management transcends the evolution and key components of a strong infrastructure. The firewall is an essential component of this infrastructure. Moreover, it is imperative that administrators and engineers understand the numerous aspects and barrage of concerns and activity that exist and must be acknowledged as part of a security policy to include the implementation of firewalls which are required to prevent such attacks in today's landscape.

# Acknowledgments

Original Authors :

Panos Kampanakis (pkampana[at]cisco[dot]com) is a member of the Applied Security Intelligence team in the Security Intelligence Operations organization.

Andrae Middleton (amiddlet[at]cisco[dot]com) is a Cisco Technical Marketing Engineer.

Revisions made February 2022 by the following members of the Applied Security Intelligence team in the Security & Trust Organization (S&TO).

Scott Bradley (sbradley@cisco.com)

Dan Maunz (damaunz@cisco.com)

Ryan Morrow (mor@cisco.com)

John Stuppi (jstuppi@cisco.com)

# References

Kaeo, Merike. Designing Network Security. Cisco Press.

Cisco ASA Series General Operations CLI Configuration Guide, 9.17 - https://www.cisco.com/c/en/us/td/docs/security/asa/asa917/configuration/general/asa-917-general-config.html

CLI Book 2: Cisco ASA Series Firewall CLI Configuration Guide, 9.17 - https://www.cisco.com/c/en/us/td/docs/security/asa/asa917/configuration/firewall/asa-917-firewall-config.html

ASDM Book 2: Cisco ASA Series Firewall ASDM Configuration Guide, 7.17 - https://www.cisco.com/c/en/us/td/docs/security/asa/asa917/asdm717/firewall/asdm-717-firewall-config.html

Duo for Cisco AnyConnect VPN with ASA or Firepower https://duo.com/docs/cisco

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| MIB | OIDs | Related Trap | Explanation |
|---|---|---|---|
| CISCO-PROCESS-MIB | cpmCPURisingThresholdValue | cpmCPURisingThreshold | CPU threshold |
| DISMAN-EVENT-MIB | mteHotValue | mteTriggerFired | Memory threshold |
| CISCO-ENTITY-SENSOR-EXT-MIB | ceSensorExtThresholdValue, entPhySensorValue, entPhySensorType | ceSensorExtThresholdNotification | Power supply failure, fan failure, CPU temperature |
| CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB | crlResourceLimitValueType, crlResourceLimitMax | clrResourceLimitReached | Connection limit |
| IF-MIB | ifIndex, ifOperStatus | linkup, linkdown | Interface up/down |

| Disable Console Logging - Firewall |
|---|
| Requirement | Severity | Comments |
| Disable Console Logging | Low | Low | Best practice: Ensure console logging is disabled or set to critical. Although useful for troubleshooting from the console port, it is possible that excessive log messages on the console could make it impossible to manage the device, even from the console. Command: no logging console - or - logging console critical |
| Low |

| Low |
|---|

| Enable Logging - Firewall |
|---|
| Requirement | Severity | Comments |
| Enable Logging | Info | Info | Best practice: Check if state of event logging on the firewall is enabled. Command: logging on \| logging enable |
| Info |
| Enable Logging Timestamp | Low | Low | Best practice: Timestamps should be enabled for log messages, which will facilitate interpretation of the messages for troubleshooting and investigating network attacks. Ensure that the date/time is correctly set (if NTP is not configured) so that the timestamps provide the proper day/time of the log messages. If the timestamps are not shown in the log messages, it may not be possible to sense the order of events occurring in the network. Command: logging timestamp |
| Low |
| Enable Logging to Buffer | Low | Low | Best practice: Cisco devices can store log messages in memory. The buffered data is available only from an exec or enabled exec session, and it is cleared when the device reboots. This form of logging is useful, even though it does not offer enough long-term protection for the logs. Buffered logging keeps the log messages in RAM on the device. A logging buffer must be configured on the device, and this buffer is circular, meaning that when it fills up, the oldest log message is deleted to make room for the new message. If buffer logging is not enabled, it will not be possible to view the most recent log messages on the device for troubleshooting or monitoring purposes. Command: logging buffered <level> |
| Low |
| Log Messages to a Syslog Server | Info | Info | Best practice: Cisco devices can be configured to forward log messages to an external Syslog service. It is highly recommended that networks implement a logging structure based on a Syslog infrastructure. Proactive monitoring of firewall logs is an integral part of Security Admin duties. The firewall syslogs are useful for forensics, network troubleshooting, security evaluation, worm and virus attack mitigation, and so on. This is a scalable solution, which provides long-term storage capabilities and a central location for all device messages Command: logging host <interface-name> <ipAddress> |
| Info |

| Info |
|---|

| Low |
|---|

| Low |
|---|

| Info |
|---|

| Secure Device Access - Firewall |
|---|
| Requirement | Severity | Comments |
| Restrict HTTP Access to Certain Addresses | Info | Info | Best practice: To specify hosts that can access the HTTP server internal to the ASA. The addresses allowed to access the firewall using HTTP can be restricted. Any undefined IP address will not see the prompt at all. Command: http <ip-address> <net-mask> <interface name> |
| Info |
| Restrict SSH Access to Certain Addresses | Medium | Medium | Best practice: The addresses allowed to access the firewall using SSH can be restricted. Any undefined IP address will not see the prompt at all. Command: ssh <ip-address> <net-mask> <interface name> |
| Medium |
| Restrict Telnet Access to Certain Addresses | Medium | Medium | Best practice: The addresses allowed to access the firewall using Telnet can be restricted. Any undefined IP address will not see the prompt at all. Command: telnet <ip-address> <net-mask> <interface name> |
| Medium |
| Set Enable Password | Info | Info | Best practice: Set enable password to secure access to privilege level. Access to the privileged EXEC mode (enable mode) should be protected by requiring a password else user logged in to user mode can access enable mode. Command: enable password <password> |
| Info |
| Set Password | Info | Info | Best practice: To set the login password, use the passwd command in global configuration mode. You are prompted for the login password when you access the CLI as the default user using Telnet or SSH. After you enter the login password, you are in user EXEC mode. Command: passwd <password> |
| Info |
| Set Suitable Console Timeout | Low | Low | Best practice : For console connections the idle timeout must be configured to avoid undesirable open and unattended console connection to the firewall. Command : console timeout |
| Low |
| Set Suitable SSH Timeout | Low | Low | Best practice: For ssh connections the idle timeout must be configured to avoid undesirable and unattended open ssh connections to the firewall. Command: ssh timeout <timeout in minutes> |
| Low |
| Use Warning Banner Messages | Low | Low | Best practice: Use of configurable, personalized login and failed-login banners is recommended. This feature lets you change the default message for login and failed-login. You can configure message banners that will be displayed when a user logs in to the system Command: banner <banner-message> |
| Low |

| Info |
|---|

| Medium |
|---|

| Medium |
|---|

| Info |
|---|

| Info |
|---|

| Low |
|---|

| Low |
|---|

| Low |
|---|

| Secure Interactive Access Using AAA - Firewall |
|---|
| Requirement | Severity | Comments |
| Define AAA Server with Key | Medium | Medium | Best practice: An Authentication Authorization and Accounting Server (AAA) is recommended to store all the username / password and privilege levels in one single repository. AAA server should be configured with a key for authentication and encryption. Command: aaa-server TACACS+ <interface> host <ipAddress> <key> |
| Medium |
| Use AAA Accounting | Low | Low | Best practice: When you configure the aaa accounting command, each command other than show commands entered by an administrator is recorded and sent to the accounting server or servers. Command: aaa accounting command EXAUTH LOCAL |
| Low |
| Use AAA Authentication for Enable Mode | Medium | Medium | Best practice: Authenticates users who access privileged EXEC mode when they use the enable command. For authentication an external server may be used and also supports fallback to local database if external authentication server is down. Command: aaa authentication enable console RADIUS LOCAL |
| Medium |
| Use AAA Authentication for HTTP | Medium | Medium | Best practice: If aaa authentication http console command is not defined, you can gain access to the ASA (via ASDM) with no username and the ASA enable password (set with the enable password command). Command: aaa authentication http console RADIUS LOCAL |
| Medium |
| Use AAA Authentication for SSH | Info | Info | Best practice: Before the firewall can authenticate a Telnet or SSH user, we must first configure access to the firewall using the telnet or ssh commands. These commands identify the IP addresses that are allowed to communicate with the firewall. Command: aaa authentication ssh console RADIUS LOCAL |
| Info |
| Use AAA Authorization | Low | Low | Best practice: The aaa authorization command specifies whether command execution at the CLI is subject to authorization. If you enable TACACS+ command authorization, and a user enters a command at the CLI, the ASA sends the command and username to the TACACS+ server to determine if the command is authorized. When configuring command authorization with a TACACS+ server, do not save your configuration until you are sure it works the way you want. If you get locked out because of a mistake, you can usually recover access by restarting the ASA. Command: aaa authorization command TACACS LOCAL |
| Low |
| Use Local Login as Backup to AAA | Info | Info | Best practice: While configuring external authentication it is advisable to keep the local database check as fallback option. Command: aaa authentication http console RADIUS LOCAL |
| Info |

| Medium |
|---|

| Low |
|---|

| Medium |
|---|

| Medium |
|---|

| Info |
|---|

| Low |
|---|

| Info |
|---|

| Secure Management Protocols - Firewall |
|---|
| Requirement | Severity | Comments |
| Authenticate NTP Updates | Medium | Medium | Best practice: Network Time Protocol (NTP) is a UDP based protocol used to synchronize time clocks amongst network devices. NTP is especially useful to ensure that timestamps on log messages are consistent throughout the entire network. It is recommended to authenticate NTP updates so that time is synchronized with approved servers only. Command: ntp authentication-key <key-id> md5 <key> |
| Medium |
| Change Default Community String | High | High | Best practice: The default community string of "public" and "private" are well known. These should always be changed to more secure strings. Command: snmp-server community <non-default-string> |
| High |
| Define SNMP Server Host | Low | Low | Best practice: SNMP is an application-layer communication protocol that allows ONS 15454 network devices to exchange management information among these systems and with other devices outside the network. SNMP is used in network management systems to monitor network-attached devices for conditions that warrant administrative attention. Command: snmp-server host |
| Low |
| Disable SNMP if not used | Low | Low | Best practice: SNMP Protocol should be disabled if not used in the network. If used, access to SNMP service should be protected using appropriate mechanisms like ACLs. Command: no snmp-server |
| Low |
| Enable SNMP Trap Logging | Low | Low | Best practice: SNMP traps are used to report an alert or other asynchronous event about a managed firewall. Command: snmp server enable traps |
| Low |
| Use NTP to Synch Network Clocks | Medium | Medium | Best practice: Network Time Protocol (NTP) is a UDP based protocol used to synchronize time clocks amongst network devices. NTP is especially useful to ensure that timestamps on log messages are consistent throughout the entire network. Command: ntp server <ntp server name> source <interface> |
| Medium |

| Medium |
|---|

| High |
|---|

| Low |
|---|

| Low |
|---|

| Low |
|---|

| Medium |
|---|

| Disable Unneeded Services - Firewall |
|---|
| Requirement | Severity | Comments |
| Check if Failover is used | Info | Info | Best practice: This rule checks if failover is configured in the firewall devices Command: failover |
| Info |
| Disable HTTP session replication | Info | Info | Best practice: The replication of http session data to the failover firewall should be disabled unless the firewall is not expected to be under extreme load and the http session data is highly critical. Given the short duration of http sessions, low probably of firewall failure and the design of most applications, this is not likely to be needed. This rule checks only firewalls with failover configured. Command: no failover replication http |
| Info |
| Disable Proxy ARPs | Low | Low | Best practice: Proxy ARP allows a firewall to extend the network at layer 2 across multiple interfaces (i.e. LAN segments). Hence proxy ARP allows hosts from different segments to function as if they were on the same subnet, and is only safe when used between trusted LAN segments. Attackers can use the trusting nature of proxy ARP by spoofing a trusted host and intercepting packets. Because of this inherent security weakness, proxy ARP should be disabled on interfaces that do not require it, especially those interfaces that connect to untrusted networks. Command: sysopt noproxyarp <interface> |
| Low |
| Limit ICMP responses on interfaces | Low | Low | Best practice: Preferable to disable ICMP on outside interfaces at a minimum. The default (i.e. no ICMP control list is configured), is for the ASA to accept all ICMP traffic that terminates at any interface (including the outside interface). This will depend on the customer policy. Command: icmp permit <acl> <interface> |
| Low |

| Info |
|---|

| Info |
|---|

| Low |
|---|

| Low |
|---|

| Control-Plane Access-List |
|---|
| Requirement | Severity | Comments |
| Use Control-Place Access list | Medium | Medium | Best practice : Access control rules for to-the-box management traffic (defined by such commands as http, ssh, or telnet) have higher precedence than an access list applied with the control-plane option. Therefore, such permitted management traffic will be allowed to come in even if explicitly denied by the to-the-box access list. Command : access-list <name> in interface <Interface name> control-plane |
| Medium |

| Medium |
|---|

| Data Plane - Firewall |
|---|
| Requirement | Severity | Comments |
| Enable uRPF anti-spoofing | Info | Info | Best practice: Anti-spoofing should be configured on all outside interfaces. This rule checks if uRFP is enabled on any one interface. Command: ip verify reverse-path interface <interface-name> |
| Info |
| Enable dnsguard | Info | Info | Best practice: Enforces one DNS response per query. Command: dns-guard |
| Info |
| Configure Basic Threat Detection | Info | Info | Best practice: Basic threat detection statistics is enabled by default. Command: threat-detection basic-threat |
| Info |
| Configure objects for use in access-control-lists | Info | Info | Best practice: Properly configure objects for primary use of access control.  Objects groups can include network, service, user, security, and time elements. Command: ip verify reverse-path interface <interface-name> |
| Info |
| Reduce performance degradation during object lookup | Info | Info | Best practice: Enable a threshold to help prevent performance degradation. When operating with a threshold, for each connection, both the source and destination IP addresses are matched against network objects. If the number of objects matched by the source address times the number matched by the destination address exceeds 10,000, the connection is dropped. Configure your rules to prevent an excessive number of matches. Command: object-group-search threshold |
| Info |

| Info |
|---|

| Info |
|---|

| Info |
|---|

| Info |
|---|

| Info |
|---|