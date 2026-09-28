---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-0-ce1200-exwy-b-cisco-expressway-ce1200-applian-13bbdc31ec
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-0/CE1200/exwy_b_cisco-expressway-ce1200-appliance-installation-guide-x14-0/exwy_m_access-the-expressway-user-interface.html
retrieved_at: 2026-08-16T22:17:03.482827+00:00
---

Cisco Expressway CE1200 Appliance Installation Guide (X14.0)

# Cisco Expressway CE1200 Appliance Installation Guide (X14.0)

Updated: April 14, 2021

Chapter: Access the Expressway User Interface

## Chapter: Access the Expressway User Interface

# Access the Expressway User Interface

## Access the Expressway User Interface

This section describes how to access the Expressway web and CLI user interfaces. The
                           			interfaces are enabled through the Install Wizard.

### Using the Web UI

To log into the web user interface:

Open a browser window and in the address line type one of the following:

IP address of the Cisco Expressway (for example, https://10.0.0.1 ). Enter the address as HTTPS.

FQDN of the Cisco Expressway (for example, https://mydomain.example.com ).

In the Login page, select Administrator
                                       						login .

Login with username admin and your system password.

The Expressway Overview page is displayed.

#### More information

Detailed information about configuring and managing Expressway, including each page
                                 				in the interface, is provided in the Expressway online help and in the Cisco Expressway Administrator Guide .

### Using the CLI

The command line interface is available over SSH and through the serial port by
                              			default:

Start an SSH session.

Enter the IP address or FQDN of the Cisco Expressway.

Log in with username admin and your system password.

A welcome message is displayed.

#### More information

The CLI commands for Expressway are detailed in the Cisco Expressway Administrator Guide .

### Next Steps

From the Expressway user interface, follow the steps described in the Cisco Expressway Basic Configuration Deployment
                                    					Guide to set up the Expressway. The process is briefly summarized here,
                                 				but please refer to the other guide for details before you continue:

The first time you log in, the Service Setup Wizard launches. The wizard is
                                          					used to select specific licensing requirements for a deployment, and if
                                          					necessary to change the default Expressway-C configuration to an
                                          					Expressway-E.

After the Service Setup Wizard, you go on to configure Expressway:

System configuration, including the System Name, DNS settings, server
                                                   								certificate, NTP servers, SIP domains).

Routing configuration, including transforms, search rules, and
                                                   								zones.

Endpoint registration.

System verification checks.

Maintenance and optional configuration tasks.

| Step 1 | The first time you log in, the Service Setup Wizard launches. The wizard is
                                          					used to select specific licensing requirements for a deployment, and if
                                          					necessary to change the default Expressway-C configuration to an
                                          					Expressway-E. |
|---|---|
| Step 2 | After the Service Setup Wizard, you go on to configure Expressway: System configuration, including the System Name, DNS settings, server
                                                   								certificate, NTP servers, SIP domains). Routing configuration, including transforms, search rules, and
                                                   								zones. Endpoint registration. System verification checks. Maintenance and optional configuration tasks. |