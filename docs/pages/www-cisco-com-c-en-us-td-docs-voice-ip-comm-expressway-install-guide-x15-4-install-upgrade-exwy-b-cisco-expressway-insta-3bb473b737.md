---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-4-install-upgrade-exwy-b-cisco-expressway-insta-3bb473b737
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-4/install-upgrade/exwy_b_cisco-expressway-install-and-upgrade-guide-x154/exwy_m_configure-expressway-after-deployment.html
retrieved_at: 2026-08-16T22:07:16.397156+00:00
---

Cisco Expressway Install and Upgrade Guide (X15.4)

# Cisco Expressway Install and Upgrade Guide (X15.4)

Updated: April 3, 2026

Chapter: Configure Expressway after Deployment

## Chapter: Configure Expressway after Deployment

# Configure Expressway after Deployment

The chapter implies to all three hypervisors.

VMware vSphere ESXi

Nutanix AHV

Cisco NFVIS-for-UC

This chapter explains the method to configure Expressway after deployment.

## Configuring the Hypervisors

These instructions describe how to set the root and admin password over SSH if you entered an RSA SSH public key in the VM Properties page – used primarily for automated deployments - or using the Install Wizard.

### Set the Root and Admin Password Using the Install Wizard

Step 1

Select the VM guest and then select the Console tab.

Step 2

Enter and confirm your root and admin passwords. You will also be prompted to set any property you did not set in VMware.

These passwords should be unique; do not use the same password for admin and root accounts.

Step 3

Press Enter to apply the configuration.

Step 4

The Expressway will apply the configuration and reboot.

You should now be able to access the Expressway using a web browser.

You can now order your option keys; see Expressway Service Selection, Licenses, and Basic Configuration .

### Set the Root and Admin Password Using SSH

The vSphere client or OVF Tool (for install Expressway) provides an interface to set the root and admin password.

You can set the root and admin password using Secure Shell Protocol (SSH) on any one of the following ports.

Port 5022

Port 22

#### Port 5022

The Install Wizard starts an SSH daemon, listening on port 5022, to set the root and admin password.

Connect as user "wizard" using an SSH client on port 5022 (for example, ssh wizard@192.168.0.100 -p 5022 ).

Follow the prompt to set admin.password and root.password .

The Expressway will apply the configuration and reboot.

You should now be able to access the Expressway using a web browser.

You can now order your option keys; see Expressway Service Selection, Licenses, and Basic Configuration .

#### Port 22

The Install Wizard starts an SSH daemon, listening on port 22 (Standard SSH port), to set the root and admin password.

Connect as user "wizard" using an SSH client on port 22 (for example, ssh wizard@192.168.0.100 ).

Follow the prompt to set admin.password and root.password .

The Expressway will apply the configuration and reboot.

You should now be able to access the Expressway using a web browser.

You can now order your option keys; see Expressway Service Selection, Licenses, and Basic Configuration .

| Note | You can ignore any floppy read errors that appear, as they are not relevant to this deployment mode. |
|---|---|

| Step 1 | Select the VM guest and then select the Console tab. You are taken to Install Wizard. |
|---|---|
| Step 2 | Enter and confirm your root and admin passwords. You will also be prompted to set any property you did not set in VMware. Note These passwords should be unique; do not use the same password for admin and root accounts. Figure 1. Enter Root and Admin Password | Note | These passwords should be unique; do not use the same password for admin and root accounts. |
| Note | These passwords should be unique; do not use the same password for admin and root accounts. |
| Step 3 | Press Enter to apply the configuration. |
| Step 4 | The Expressway will apply the configuration and reboot. Figure 2. Configuration Applied |

| Note | These passwords should be unique; do not use the same password for admin and root accounts. |
|---|---|