---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su3-cucm-b-security-guide-1251su3-cucm-m-security-troubl-6bf4d8c58d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU3/cucm_b_security_guide_1251SU3/cucm_m_security-troubleshooting-overview.html
retrieved_at: 2026-08-21T08:36:38.327981+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: March 22, 2024

Chapter: Security Troubleshooting Overview

## Chapter: Security Troubleshooting Overview

# Security Troubleshooting Overview

## Remote Access

Remote access provides you with the ability to establish Terminal Services (remote port 3389), HTTP (remote port 80), and
                           Telnet (remote port 23) sessions to all the necessary equipment.

Caution

When you are setting up dial-in, do not use login:cisco or password:cisco because they constitute a vulnerability to the system.

You may resolve many issues very quickly by allowing the TAC engineer remote access to the devices through one of the following
                           methods:

Equipment with public IP address.

Dial-in access—In decreasing order of preference: analog modem, Integrated Services Digital Network (ISDN) modem, virtual
                                 private network (VPN).

Network Address Translation (NAT)—IOS and private Internet exchange (PIX) to allow access to equipment with private IP addresses.

Ensure that firewalls do not obstruct IOS traffic and PIX traffic during engineer intervention and that all necessary services,
                           such as Terminal Services, start on the servers.

TAC handles all access information with the utmost discretion, and no changes will get made to the system without customer
                                       consent.

## Cisco Secure Telnet

Cisco Secure Telnet offers Cisco Service Engineers (CSE) transparent firewall access to Unified Communications Manager servers on your site.

Cisco Secure Telnet works by enabling a Telnet client inside the Cisco Systems firewall to connect to a Telnet daemon behind
                           your firewall. This secure connection allows remote monitoring and maintenance of your Unified Communications Manager servers without requiring firewall modifications.

Cisco accesses your network only with your permission. You must provide a network administrator at your site to help initiate
                                       the process.

### Firewall Protection

Virtually all internal networks use firewall applications to restrict outside access to internal host systems. These applications
                              protect your network by restricting IP connections between the network and the public Internet.

Firewalls work by automatically blocking TCP/IP connections that are initiated from the outside, unless the software is reconfigured
                              to allow such access.

Corporate networks normally permit communication with the public Internet but only if connections directed to outside hosts
                              originate from inside the firewall.

### Cisco Secure Telnet Design

Cisco Secure Telnet takes advantage of the fact that Telnet connections can easily be initiated from behind a firewall. Using
                              an external proxy machine, the system relays TCP/IP communications from behind your firewall to a host behind another firewall
                              at the Cisco Technical Assistance Center (TAC).

Using this relay server maintains the integrity of both firewalls while secure communication between the shielded remote systems
                              get supported.

### Cisco Secure Telnet Structure

The external relay server establishes the connection between your network and Cisco Systems by building a Telnet tunnel. This
                              enables you to transmit the IP address and password identifier of your Unified Communications Manager server to your CSE.

The password comprises a text string upon which your administrator and the CSE mutually agree.

Your administrator starts the process by initiating the Telnet tunnel, which establishes a TCP connection from inside your
                              firewall out to the relay server on the public Internet. The Telnet tunnel then establishes another connection to your local
                              Telnet server, creating a two-way link between the entities.

The Telnet client at the Cisco TAC runs in compliance with systems that run on Windows NT and Windows 2000 or with UNIX operating
                                          systems.

After the Cisco Communications Manager at your site accepts the password, the Telnet client that is running at the Cisco TAC
                              connects to the Telnet daemon that is running behind your firewall. The resulting transparent connection allows the same access
                              as if the machine were being used locally.

After the Telnet connection is stable, the CSE can implement all remote serviceability functionality to perform maintenance,
                              diagnostic, and troubleshooting tasks on your Unified Communications Manager server.

You can view the commands that the CSE sends and the responses that your Unified Communications Manager server issues, but the commands and responses may not always be completely formatted.

## Set up a Remote Account

Configure a remote account in the Unified Communications Manager so that Cisco support can temporarily gain access to your
                              system for troubleshooting purposes.

Step 1

From Cisco Unified Operating System Administration, choose Services > Remote Support .

Step 2

In the Account Name field, enter a name for the remote account.

Step 3

In the Account Duration field, enter the account duration in days.

Step 4

Click Save .

Step 5

Contact Cisco support to provide them with the remote support account name and pass phrase.

| Caution | When you are setting up dial-in, do not use login:cisco or password:cisco because they constitute a vulnerability to the system. |
|---|---|

| Note | TAC handles all access information with the utmost discretion, and no changes will get made to the system without customer
                                       consent. |
|---|---|

| Note | Cisco accesses your network only with your permission. You must provide a network administrator at your site to help initiate
                                       the process. |
|---|---|

| Note | The password comprises a text string upon which your administrator and the CSE mutually agree. |
|---|---|

| Note | The Telnet client at the Cisco TAC runs in compliance with systems that run on Windows NT and Windows 2000 or with UNIX operating
                                          systems. |
|---|---|

| Step 1 | From Cisco Unified Operating System Administration, choose Services > Remote Support . |
|---|---|
| Step 2 | In the Account Name field, enter a name for the remote account. |
| Step 3 | In the Account Duration field, enter the account duration in days. |
| Step 4 | Click Save . The system generates an encrypted pass phrase. |
| Step 5 | Contact Cisco support to provide them with the remote support account name and pass phrase. |