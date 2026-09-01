---
doc_id: sec-cloudapps-cisco-com-security-center-resources-cisco-catalyst-sd-wan-hardeningguide-57d557b79b
source_url: https://sec.cloudapps.cisco.com/security/center/resources/Cisco-Catalyst-SD-WAN-HardeningGuide
retrieved_at: 2026-09-01T14:10:03.437631+00:00
---

Home / Cisco Security

Cisco Catalyst SD-WAN Hardening Guide

# Cisco Catalyst SD-WAN Hardening Guide

### Contents

## Introduction

This document addresses security hardening for Cisco Catalyst SD-WAN – specifically the SD-WAN control components in the fabric, and WAN edge device hardening issues specific to Cisco Catalyst SD-WAN. For security hardening of WAN edge devices, see the Cisco IOS XE Software Hardening Guide .

The aim is to do the following:

- Lock down access to the SD-WAN Control Components to prevent unauthorized connections.

- Among users with legitimate access, limit access to settings and configuration options to provide each user with only the access that they require for their role.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software releases or hardware versions.
The SD-WAN Control Components that are referenced in this document are presented using a default (cleared) configuration. If your network is live, ensure that you understand the potential impact of any changes.

## Terminology

SD-WAN Control Components include:

- SD-WAN Manager

- SD-WAN Controller

- SD-WAN Validator

## Network Perimeter Controls

Implement a defense-in-depth architecture that integrates network segmentation with granular access control lists (ACLs) and firewall policies to strictly limit network reachability to your SD-WAN control components. These perimeter controls act as the first line of defense against unauthorized access.

### Cisco-Hosted Deployment

To secure your Cisco SD-WAN Cloud Pro fabric, you must explicitly add trusted IPs, ports, and protocols to an allow list using the Cisco Catalyst SD-WAN Portal. To do so, complete the following steps:

- Log in to the Cisco Catalyst SD-WAN Portal.

- Choose your fabric from the List View .

- Navigate to Inbound Rules and click Add Inbound Rule .

- Define the Rule Type (SSH, HTTPS, or Custom), Port range , and Source IP or prefix . Do not use the ALL rule for the source IP, source prefix, or port range.

- Enter a description

- Click Add Rule .

Notes:

- When you configure inbound rules from the Cisco Catalyst SD-WAN Portal, the portal automatically translates these inputs into cloud-native security group rules (for example, AWS Security Groups or Azure Network Security Groups) on the underlying infrastructure. This ensures that traffic is filtered at the boundary before it ever reaches your SD-WAN components.

- Rules apply uniformly to all SD-WAN Manager, Validator, and Controller components in the fabric.

- There is a maximum of 200 rules allowed per fabric.

- Edge devices do not need to be added to an allow list. Provided that their serial numbers are authorized within Cisco SD-WAN Manager, these devices establish connectivity through secure, mutually authenticated (D)TLS tunnels.

For more information, see Specify the allowed list of IP addresses for managing control component access .

You may implement additional restrictions beyond the rules created from the Cisco Catalyst SD-WAN Portal by applying Localized Policy feature templates directly to the VPN 512 (Management) interface from the SD-WAN Manager. This enables granular control and further restricts access to a specific subset of your allowlisted IP ranges.

For more information, see Configure Localized Policy Using Cisco SD-WAN Manager .

### Self-Hosted Deployment

For self-hosted deployments, you must secure SD-WAN Control Components by implementing perimeter security controls, including ACLs and firewall policies, appropriate for the environment where the SD-WAN Control Components are deployed.

Maintain separation of the Control Plane (Transport) from the Management Plane. Deploy the VPN 0 (Transport) interfaces of SD-WAN Validator, SD-WAN Controller, and SD-WAN Manager into a DMZ segment behind a perimeter firewall. A best practice is to use 1:1 NAT on a firewall. The SD-WAN Control Components should have private IPs, and the firewall translates them to public IPs.

Deploy the VPN 512 (Management) interfaces into a strictly isolated internal management VLAN. A best practice is to never route VPN 512 traffic through the DMZ or the public internet. It should remain entirely out of band (OOB).

Secure Administrative Access

Direct access to management interfaces from user subnets or the internet increases the attack surface. Administrators should not access SD-WAN Manager directly from their workstations. Therefore, determine if your environment can use hardened jump hosts for secure admin access. A best practice is to enforce multi-factor authentication (MFA) to log in to a jump host through the corporate VPN of choice (for example, Cisco AnyConnect) that terminates at the network perimeter, then routes to the jump host. Do not expose administrative interfaces (for example, ports 443, 22, 830) of SD-WAN components directly to the internet.

Firewall Allow List (Ports and Protocols)

Configure the perimeter firewall to allow only the minimum necessary traffic.

For the SD-WAN Validator and SD-WAN Manager, allow UDP port 12346.

To ensure successful initial orchestration when using automated provisioning (for example, ZTP/PnP) or if edge devices use dynamic public IP addresses, allow traffic from any source. However, if edge devices are manually provisioned with known static public IPs, restrict the source to those specific IP blocks to further harden the perimeter.

For SD-WAN Controllers and the SD-WAN Manager, allow traffic destined to UDP port 12346 (Datagram Transport Layer Security (DTLS)) and TCP port 23456 (Transport Layer Security (TLS)) from edge device IPs. Be aware that edge devices may use port hopping, cycling through ports UDP 12346+n, 12366+n, 12386+n, 12406+n, and 12426+n (where n=0-19 represents the configured offset). This traffic carries the encrypted tunnels that are required for Overlay Management Protocol (OMP) and Bidirectional Forwarding Detection (BFD). Note that the destination ports, UDP port 12346 (DTLS) and TCP port 23456 (TLS), are the default base ports for Core 0.

SD-WAN Managers and SD-WAN Controllers with multiple cores use a distinct port for each additional core, incrementing the base port by 100. For example, Core 1 uses UDP 12446 and TCP 23556, Core 2 uses UDP 12546 and TCP 23656, and so on. Configure the firewall to allow these specific port increments based on the number of cores assigned to your instances.

If a NAT gateway is present in the underlay, source ports from edge devices may be randomized, requiring you to permit a broader range of source ports beyond the standard port hopping values.

Depending on your deployment architecture, DNS may be needed if you are using a DNS server to resolve hostnames and the server is reachable natively through the VPN 0 transport. You may need DNS to resolve the SD-WAN Validator or NTP server name. DNS uses UDP port 53, NTP uses UDP port 123.

To secure remote administrative access that is destined for the VPN 512 (Management) interface, configure the following firewall allow-list rules:

- SSH (TCP 22): Allow strictly from a jump host or an authorized management subnet to all SD-WAN components for CLI access.

- HTTPS (TCP 443): Allow strictly from a jump host or authorized management subnet to the SD-WAN Manager for web UI access.

- NETCONF (TCP 830): Allow strictly from the SD-WAN Manager IP address to the SD-WAN Controllers and Validators to facilitate configuration operations.

For more information, see the Cisco Catalyst SD-WAN Design Guide .

## Role-Based Access Control

Role-based access control (RBAC) is a security feature that enables you to configure permissions for each SD-WAN Manager user to view or modify settings and features, according to the roll assigned to the user. Instead of assigning privileges directly to individual users, RBAC assigns roles that define the privileges that a user has within the system.

User: Entity that performs different actions in SD-WAN Manager. A user has an assigned role.

Role: Defines the feature permissions (write, read, or deny) authorized for users with the role. Write enables changes, read enables only viewing, and deny means that a user can neither view nor change a feature.

Scope: Defines the set of objects (sites, devices, or templates) on which a user can perform actions.

### RBAC Roles

Cisco Catalyst SD-WAN includes the following default roles.

Note: Only netadmin users can view the running and local configuration. Users who are associated with a predefined operator role do not have access to the running and local configurations. The predefined role operator has only read access for the template configuration. If you need only a subset of admin user privileges, then you need to create a new role with the selected features from the features list with both read and write access and associate the role with the custom user.

For complete information about RBAC, see Role Based Access Control .

### Best Practices

Determine which settings and features each user will need to be able to monitor, and which they need to be able to configure. Assign a role to the user in accordance with their requirements. Do not provide a user more access privileges than they require.

## Access to SD-WAN Manager: Web Server Certificates

SD-WAN Manager is the main portal for managing Cisco Catalyst SD-WAN. It is an intuitive graphical interface that runs in a web browser. SD-WAN Manager uses certificate authentication to ensure a secure connection with your browser. This requires you to generate a certificate signing request, get it signed by a root certificate authority, and then install it.

For procedures and more information, see Web Server Certificate for Cisco SD-WAN Manager .

### Best Practices

By default, SD-WAN Manager uses a self-signed certificate for the web UI. Replace it with a certificate signed by your Enterprise Root CA or a trusted Public CA to ensure browser trust.

## Strong Passwords

SD-WAN Control Components enforce password policy rules to ensure the use of strong passwords. Password policies can be enabled and configured to require passwords that meet specific criteria for security levels such as medium or high security. Passwords must meet length, character type, and complexity requirements to be accepted.

### Password Examples

Here are examples of strong passwords based on the medium and high security password criteria:

Medium security password example:

- Length: Between eight and 32 characters.

- Includes at least one lowercase letter, one uppercase letter, one numeric character, and one special character.

- Does not reuse any of the last five passwords.

- Does not contain the full name or username.

Example: Ex@mple1

High security password example:

- Length: Between 15 and 32 characters.

- Includes at least one lowercase letter, one uppercase letter, one numeric character, and one special character.

- Does not reuse any of the last five passwords.

- Does not contain the full name or username.

- Has at least eight characters changed from the old password.

Example: Str0ng!Passw0rd2026#

These examples meet the specified criteria for medium and high security passwords respectively, ensuring complexity and uniqueness to enhance security.

For more information, see Configure Hardened Passwords .

### Password Management

- Change passwords regularly and use different passwords for different accounts.

- Enable multifactor authentication whenever possible to enhance security. For configuring Duo multifactor authentication, see Configure Duo Multifactor Authentication .

- Limit consecutive password attempts to prevent brute force attacks by making accounts lock after multiple failed attempts. For account lockout policies and reset procedures, see Configure Account Lockout .

- If locked out, wait for automatic unlock or contact an administrator for reset or unlock. For instructions for resetting locked users, see Reset a Locked User .

- Manage user roles and groups to control access and reset or unlock accounts as needed. For more information, see Role Based Access Control .

- Store passwords securely using encryption methods such as type 6 encryption in configuration groups. For more information, see Type 6 Passwords on Cisco IOS XE SD-WAN Routers .

- Replace the default configuration database credentials with a unique username and a strong, complex password to prevent unauthorized database access. For more information, see Update Configuration Database Login .

### Single Sign On (SSO) and Duo Multi-Factor Authentication (MFA)

In addition to strong passwords, enable single sign on or multifactor authentication whenever possible to enhance security. For configuring Duo multifactor authentication, see Configure Duo Multifactor Authentication . Use the following guidelines:

- SSO for Self-Hosted Deployments: SD-WAN Manager supports both on-premise and cloud-based Identity Providers (IdP). Ensure that the Management interface is permitted to reach your specific IdP through appropriate firewall or proxy configurations. For more information, see Configure Single Sign-On .

- SSO for Cisco-Hosted Deployments: For Cisco SD-WAN Cloud Pro fabric, you can configure IdP directly through the Cisco Catalyst SD-WAN Portal, which simplifies the integration of external IdPs (such as Okta or Azure AD) with your hosted overlay fabric. For more information, see Configure an Identity Provider for the Cisco Catalyst SD-WAN Portal .

- Native Duo MFA: If you prefer to enforce authentication controls directly at the application level, you can utilize the native Duo MFA feature integrated within SD-WAN Manager. For more information, see Configure Duo Multifactor Authentication .

## Control Plane Security

The control plane of a network defines the network topology and how to direct packets. The Cisco Catalyst SD-WAN control plane was designed with network and device security in mind, operating on a Zero Trust model where no device is trusted implicitly. All control plane traffic is encapsulated within authenticated and encrypted DTLS or TLS tunnels. Furthermore, to adhere to rigorous security standards, FIPS mode is enabled by default on SD-WAN control components starting with release 20.15.1.

### Security Protocols: DTLS and TLS

Control plane security relies on two security protocols that are derived from Secure Sockets Layer (SSL): the Datagram Transport Layer Security (DTLS) protocol and the Transport Layer Security (TLS) protocol. The SD-WAN Controller, which is the centralized brain of the Cisco Catalyst SD-WAN solution, establishes and maintains DTLS or TLS connections to all devices in the fabric:

- Routers

- SD-WAN Validator

- SD-WAN Manager

- Other SD-WAN Controllers

These connections carry control plane traffic. DTLS or TLS provides secure communication between devices in the network, using the Advanced Encryption Standard (AES-256) encryption algorithm to encrypt all the control traffic sent over the connections.

### Authentication

To perform authentication, network devices exchange digital certificates, which are either installed by the software or hard coded into the hardware, depending on the device. They identify each device and allow the devices themselves to automatically determine which ones belong in the network and which are imposters.

### Integrity

DTLS or TLS connections use AES-256-GCM, an authenticated encryption with associated data (AEAD) that provides encryption and integrity, which ensures that all the control and data traffic sent over the connections has not been tampered with.

### Best Practices

DTLS

Configure DTLS data encryption for SD-WAN Manager connections. The DTLS protocol is a standards-track IETF protocol that can encrypt both control and data packets based on TLS.

For more information, see Configure DTLS in Cisco SD-WAN Manager .

SNMP

Use only SNMPv3 – not SNMPv1 or SNMPv2. Enable authentication for SNMPv2.

For information about configuring SNMPv3 using a configuration group, see Configure SNMP using a Configuration Group . You can choose security level, authentication protocol, authentication password, etc.

## Data Plane Security

Data plane security relies on control plane security as its foundation to be able to trust the reliability of route information and other info derived from the control plane.

Within the data plane itself, security features address authentication, encryption, and data integrity.

### Authentication and Key Exchange for SD-WAN Fabric

In Cisco Catalyst SD-WAN, authentication involves key exchange: This can be (a) traditional key exchange, where an SD-WAN Controller sends IPsec encryption keys to each edge device, or (b) by pairwise key exchange, where an SD-WAN Controller sends Diffie-Hellman public values to the edge devices, and they generate pairwise IPsec encryption keys using Elliptic-curve Diffie-Hellman (ECDH) and a P-384 curve.

By default, IPsec tunnel connections use an enhanced version of the Encapsulating Security Payload (ESP) protocol for authentication on IPsec tunnels.

For more information, see IPsec Pairwise Keys .

### Encryption and Integrity (Enhanced ESP)

By default, overlay tunnels use an Enhanced Encapsulating Security Payload (ESP) protocol.

- Encryption: Data encryption is performed using the AES-GCM-256 cipher.

- Integrity: Unlike standard ESP, this enhanced version checks the integrity of the outer IP and UDP headers, providing protection like the Authentication Header (AH) protocol.

- Anti-Replay: The scheme implements protection against replay attacks, where an attacker attempts to duplicate and retransmit encrypted packets.

Edge devices exchange their supported integrity and encryption capabilities through Transport Locator (TLOC) properties. If two peers advertise different types, they negotiate to use the strongest common method.

### Data Plane Security for Third-Party Tunnels (IKE/Ipsec)

This section applies to standard IPsec tunnels that are established between Cisco Catalyst SD-WAN devices and non-SD-WAN endpoints, like Cloud Security Providers, Zscaler, etc. These connections use standard Internet Key Exchange (IKE).

To ensure the security of third-party connections, Cisco Catalyst SD-WAN enforces strict cryptographic standards for IKE negotiations.

- Beginning with Cisco IOS XE Software for Catalyst SD-WAN Release 17.11.1a, support for weak Diffie-Hellman (DH) groups has been removed to align with modern security hardening standards. DH Groups 1, 2, and 5 are no longer supported.

- When configuring IKE/IPsec templates for third-party peers, ensure that the remote end supports modern DH groups (for example, Group 14, 15, 16) to establish session keys and provide Perfect Forward Secrecy.

For more information, see Configure IPsec Tunnel Parameters.

### Best Practices

Configure Allowed Authentication Types

By default, the IPsec tunnel connections in Cisco Catalyst SD-WAN fabric use an enhanced version of the Encapsulating Security Payload (ESP) protocol for authentication. You can modify the integrity type to use any of these:

- esp: Encapsulating Security Payload (ESP) encryption and integrity checking on the ESP header.

- ip-udp-esp: ESP encryption, and in addition to the integrity checks on the ESP header and the payload, this option also checks the outer IP and UDP headers.

- ip-udp-esp-no-id: Similar to ip-udp-esp but ignores the ID field of the outer IP header. This option can be helpful when Cisco Catalyst SD-WAN is working with non-Cisco devices or with providers that use IPv6 core networks.

- none: Turns integrity checking off on IPSec packets. This option is not recommended.

For more information, see Configure Allowed Authentication Types .

Change The Rekeying Timer

Before devices can exchange data traffic, they set up a secure authenticated communications channel between them. The devices use IPSec tunnels between them as the channel, and the AES-256 cipher to perform encryption.

Each device generates a new AES key for its data path periodically. By default, a key is valid for 86400 seconds (24 hours), and the timer range is 10 seconds through 1209600 seconds (14 days).  Retaining the default rekey interval is recommended. However, if you choose to modify this value, you must ensure the rekeying time is at least twice the value of the Overlay Management Protocol (OMP) graceful restart timer.

## Session Timeouts for Cisco Catalyst SD-WAN Manager

Session timeouts refer to the automatic termination of Cisco Catalyst SD-WAN Manager web-based user sessions or CLI-based user sessions after a specified period of inactivity. This security feature helps prevent unauthorized access by ensuring that sessions do not remain open indefinitely when a user is inactive.

In Cisco Catalyst SD-WAN Manager, session timeouts are configurable settings that control how long a user session remains active before it is automatically logged out due to inactivity or maximum session duration. These timeouts enhance security by reducing the risk of unauthorized access through unattended sessions.

### Types of Session Timeouts for Cisco Catalyst SD-WAN Manager

Client session timeout: You can set a client session timeout in Cisco Catalyst SD-WAN Manager. When a timeout is set, such as no keyboard or keystroke activity, the client is automatically logged out of the system. For more information, see Set a Client Session Timeout in Cisco SD-WAN Manager.

Server session timeout: You can configure the server session timeout in Cisco Catalyst SD-WAN Manager. It indicates how long the server should keep a session running before it expires due to inactivity. The default server session timeout is 30 minutes. For more information, see Set the Server Session Timeout in Cisco SD-WAN Manager .

CLI session inactivity: You can configure the CLI session timeout on SD-WAN control components. The CLI idle timeout indicates how long the system should maintain an open SSH or console session before terminating it due to inactivity. The default CLI timeout is 1800 seconds (30 minutes). To set the session timeout, complete the following steps:

- Log in to the CLI of the device using SSH.

- At the operational prompt, type config to enter configuration mode.

- Type system to enter the system configuration hierarchy.

- Type idle-timeout followed by the number of minutes (for example, idle-timeout 10 for 600 seconds).

- Type commit to validate and apply the changes to the active configuration.

- Type end to exit configuration mode and return to the operational prompt.

- To verify the change, log out of the current session and log back in using SSH. Then, run the show cli command in operational mode. The idle-timeout value should now reflect the updated configuration.

For more information, see Cisco Catalyst SD-WAN Command Reference .

### Best Practices

Configure all session limits in accordance with your internal policies or relevant regulatory frameworks.

For client and session timeouts, configure the shortest amount of time possible.

For CLI session inactivity, configure the shortest amount of time that supports your workflow:

- Session lifetime: You can specify how long to keep your session active by setting the session lifetime in minutes. A session lifetime indicates the amount of time for which a session can be active. If you keep a session active without letting it expire, you will be logged out of the session in 24 hours, which is the default session timeout value. For more information, see Set a Session Lifetime in Cisco SD-WAN Manager .

- Maximum sessions per user: You can configure the maximum number of concurrent login sessions for each configured user role. This maximum value applies to all users assigned to that role. For more information, see Set the maximum sessions per user role .

Configure your maximum sessions value as low as possible without impacting business operations.

## Logging

Logging in Cisco Catalyst SD-WAN refers to collecting, storing, and analyzing recordable messages that are generated by SD-WAN components, including system events, operational messages, alarms, audit trails, and access control log entries. These logs help with troubleshooting, monitoring, auditing, and compliance across the SD-WAN infrastructure.

Logging includes:

- Syslog messages from devices

- Events and alarms from the overlay network

- Audit trails of configuration and admin actions

- ACL/security logs from policy enforcement

Note: Audit logs, ACL logs, and syslogs are aggregated in Cisco Catalyst SD-WAN Manager to provide a comprehensive security audit trail.

For more details about how syslog messages are generated and used by SD-WAN components, see Alarms, Events, and Logs .

### Logging in SD-WAN Control Components

Cisco Catalyst SD-WAN devices generate logs specific to the platform that help with operations, security, and troubleshooting.

WAN Edge Devices

Devices generate system logs locally in the /var/log directory and can forward these logs securely to remote servers using syslog over UDP, TCP, or TLS. These logs help monitor device health, troubleshoot issues, and support security auditing. Cisco Catalyst SD-WAN Manager allows you to configure and view these logs to maintain network visibility and control. For more information, see System Logging, Configure System Logging Using CLI .

Cisco Catalyst SD-WAN Manager

Cisco Catalyst SD-WAN Manager logs various events including administrative actions, configuration changes, system operations, and internal services. These logs are stored on the Cisco Catalyst SD-WAN Manager host under the directory /var/log/nms . The logs help monitor system activity, troubleshooting issues, and auditing changes within the SD-WAN environment. For more information, see Cisco SD-WAN Manager Logs .

SD-WAN Controller and SD-WAN Validator

Cisco Catalyst SD‑WAN Manager, Controller, and Validator generate system and control‑plane logs locally under /var/log to support troubleshooting, monitoring, and auditing of control connections and orchestration. The most important logs are:

```
/var/log/vsyslog
```

Main SD‑WAN control‑plane log (vBond state changes, control‑connection up/down, auth failures, security events).

```
/var/log/messages
```

Combined system log (OS + SD‑WAN notifications).

```
auth.log
```

Authentication and login audit trail.

```
/var/log/vconfd
```

Management‑plane errors and config validation issues.

```
kern.log
```

Kernel/hardware warnings and boot‑time kernel events.

```
runit.log
```

Service startup/boot orchestration (which services started, phase transitions, System Ready timing).

```
/var/log/vdebug
```

Deep debug/boot diagnostics (very verbose).

These logs can be forwarded to a remote syslog server using UDP, TCP, or TLS. For secure transport always prefer TLS.

### Types of Logging

Cisco Catalyst SD-WAN supports various types of logging to address different operational, security, and monitoring needs. These logging types help administrators track system behavior, security events, configuration changes, and network traffic for effective management and troubleshooting.

System Logging (syslog)

System logging captures standard operating logs from system services, daemons, and Cisco Catalyst SD-WAN processes on devices. This includes kernel, authentication, process, and consolidated messages such as auth.log and messages.log . For more information, see System Logging .

Audit Logging

Audit Logging tracks administrative actions like configuration changes, template attach/detach events, and login activity within SD-WAN Manager, providing accountability and change tracking. For more information, see Audit Logging .

ACL Logging

ACL records match against ACL rules on WAN Edge devices. For more information, see ACL Log .

Alarms and Events Logging

Alarms and events capture high-level alerts and state changes for system components, such as device status changes, TLOC state, and control connection failures, helping in proactive monitoring. For more information, see Alarms and Events .

Firewall High-Speed Logging

Firewall high-speed logging (HSL) provides high-speed logging from the zone-based firewall feature, exporting session records in NetFlow v9 format with minimal packet processing impact, suitable for detailed traffic analysis. For more information, see Firewall High-Speed Logging .

### Best Practices

Configure retention periods to align with your organization's security policies and regulatory compliance mandates. To do so, complete the following steps:

- Log in to your Cisco Catalyst SD-WAN Manager.

- Run the API call https://your-vmanage-ip/dataservice/management/elasticsearch/index/size/estimate in a browser or REST client to retrieve the storage projections for your fabric.

- Locate the audit section in the JSON response to find the specific storage requirements. For example, the output might indicate 2 GB is needed for 90 days and 8 GB is needed for one year.

- Choose Administration > Settings > Statistics Database Configuration .

- Update the Audit Logs storage limit to the specific value retrieved from the API (for example, enter 2 GB for 90-day retention or 8 GB for one-year retention).

- Click Save to commit the storage expansion.

Note: Periodically review storage allocations because network growth increases log volume and reduces the configured retention duration. A 5GB allocation that covers one year of logs today might cover only six months of logs next year if your log volume doubles. Allocate storage capacity above the value that is returned by the JSON output (for example, a 20 percent buffer) to accommodate future network growth and fluctuations in log volume.

## Access to SD-WAN Control Components and Devices: SSH Configuration

The Secure Shell (SSH) protocol provides secure remote access connection to network devices. It provides encrypted command-line access for configuration, monitoring, and troubleshooting.

About SSH Configuration:

- SSH authentication on WAN edge devices supports RSA keys with sizes from 2048 to 4096 bits (1024 and 8192 are not supported).

- A maximum of two SSH keys per user is allowed.

- Public keys are stored in the  home directory of the user under ~/.ssh/authorized_keys .

- The authentication order can be configured to try local, RADIUS, and TACACS+ servers in a preferred sequence.

- Role-based access control is implemented using Authentication, Authorization, and Accounting (AAA) to manage user permissions.

- Weak SSH encryption algorithms, such as SHA-1, AES-128, and AES-192, can be disabled on Cisco Catalyst SD-WAN Manager to enhance security compliance. See Information About Disabling Weak SSH Encryption Algorithms on Cisco SD-WAN Manager .

- SSH access to Cisco Catalyst SD-WAN Manager requires enabling SSH authentication using AAA templates that are pushed through feature templates.

For more information about SSH configuration and authentication setup on WAN edge devices and Cisco Catalyst SD-WAN Manager, see Configure SSH Authentication .

Using SSH to access SD-WAN Control Components and WAN edge devices:

- SSH is used to securely access network components, including Cisco Catalyst SD-WAN Manager, SD-WAN Controllers, SD-WAN Validators, and WAN edge devices for command-line management and troubleshooting.

- Cisco Catalyst SD-WAN Manager provides an SSH terminal tool in the GUI to open SSH sessions to devices. Ensure that SSH access to edge devices from the Cisco Catalyst SD-WAN Manager is allowed. For more information, see SSH Terminal .

- In a multitenant Cisco Catalyst SD-WAN deployment, provider and tenant roles have different SSH access privileges with the provider able to manage and access shared components and the tenant limited to their scoped devices and views. For more information, see User Roles in Multitenant Environment .

- When SD-WAN Control Components establish control connections with each device in the network, they use an encryption algorithm that each device supports. For more information, see SSH Encryption Algorithms .

### Best Practices

- Restrict SSH to management networks and bastion hosts only. Never expose controllers directly to the Internet.

- Use key‑based authentication only. Avoid passwords and shared accounts.

- Rotate per‑admin keys regularly and remove them immediately on offboarding or incident response.

- Keep private keys only on admin/jump hosts. Never copy private keys onto SD-WAN Validator or SD-WAN Controller.

- Configure authentication order intentionally (for example, TACACS/RADIUS first, local last).

- Disable weak SSH algorithms after all devices are on compatible releases.

- Centralize logging and audit SSH sessions. Alert on unexpected access.

- Use Cisco Catalyst SD‑WAN Manager templates to manage SSH and AAA consistently at scale.

## References

Control Plane Security Overview - DTLS and TLS Infrastructure

### Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Role | Configurable | Description |
|---|---|---|
| basic | No | This is the basic default role built into SD-WAN Manager. To create a new role that can be modified, copy the basic role and then modify it for your requirements. |
| operator | Yes | This role can be used for any user or privilege level. It is designed to include users who have permission only to view information. |
| netadmin | No | By default, this role includes the admin user. You can add other users to this role. Users with this role are permitted to perform all operations on the device. |
| network_operations | No | Users in this role can perform all non-security-policy operations on devices and can view security policy information. They can apply policies to a device, revoke applied policies, and edit device templates. For example, these users can create or modify template configurations, manage disaster recovery, and create non-security policies such as an application-aware routing policy or Cflowd policy. |
| security_operations | No | Users with this role can perform all security operations on the device and can view non-security-policy information. These users require network_operations users to intervene on day-0 to deploy a security policy on a device and on day-N to remove a deployed security policy. But after a security policy is deployed on a device, security_operations users can modify the security policy without needing the network_operations users to intervene. For example, these users can manage umbrella keys, licensing, IPS signatures auto update, TLS/SSL proxy settings, and so on. |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.1 | 09-Feb-2026 | Updated the Strong Passwords section. |
| 1.0 | 06-Feb-2026 | Initial Release |