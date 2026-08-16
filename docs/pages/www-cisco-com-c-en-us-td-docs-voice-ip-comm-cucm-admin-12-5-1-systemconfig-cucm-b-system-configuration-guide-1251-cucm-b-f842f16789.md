---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-f842f16789
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01000011.html
retrieved_at: 2026-08-16T17:36:24.461260+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Register Devices Overview

## Chapter: Register Devices Overview

- Register Devices Overview

- About Registering Devices

- Registering Devices

# Register Devices Overview

## About Registering Devices

The chapters in this section describe the tasks that you perform to register new endpoint devices and to  set up proxy TFTP
                              servers for your endpoints and gateway devices.

You can choose to register new phones manually or use autoregistration. To register more than 100 phones, use the Bulk Administration
                              Tool (BAT). For more information, see Cisco Unified Communications Manager Bulk Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

You cannot create new settings using BAT, but you can configure phone parameters when you use the BAT to register phones.
                                          Make sure that phone settings such as device pool, location, calling search space, button template, and softkey templates
                                          have already been configured using Cisco Unified Communications Manager Administration .

## Registering Devices

Complete the following task flows to register devices for your system.

Step 1

TFTP Server Configuration Task Flow

Configure the proxy Trivial File Transfer Protocol (TFTP) server that provides the configuration files for endpoints in your
                                          network.

Step 2

(Optional) Update Device Defaults Task Flow

Modify the device load, device pool, and the phone button template values that are applied to endpoints when they register.

Step 3

Configure Autoregistration Task Flow

Enable autoregistration for your network. Because of the inherent security risk of allowing devices to register automatically
                                          on the network, we recommend that you disable autoregistration as soon as you have registered your new endpoints.

Step 4

Manual Device Registration Task Flow

Manually register an IP phone and assign a new directory number.

Step 5

Self-Provisioning Configuration Task Flow

Optional. If you want your end users to be able to provision their own phones without the aid of an administrator, configure
                                          self-provisioning.

| Note | You cannot create new settings using BAT, but you can configure phone parameters when you use the BAT to register phones.
                                          Make sure that phone settings such as device pool, location, calling search space, button template, and softkey templates
                                          have already been configured using Cisco Unified Communications Manager Administration . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | TFTP Server Configuration Task Flow | Configure the proxy Trivial File Transfer Protocol (TFTP) server that provides the configuration files for endpoints in your
                                          network. |
| Step 2 | (Optional) Update Device Defaults Task Flow | (Optional) Modify the device load, device pool, and the phone button template values that are applied to endpoints when they register. |
| Step 3 | Configure Autoregistration Task Flow | Enable autoregistration for your network. Because of the inherent security risk of allowing devices to register automatically
                                          on the network, we recommend that you disable autoregistration as soon as you have registered your new endpoints. |
| Step 4 | Manual Device Registration Task Flow | Manually register an IP phone and assign a new directory number. |
| Step 5 | Self-Provisioning Configuration Task Flow | Optional. If you want your end users to be able to provision their own phones without the aid of an administrator, configure
                                          self-provisioning. |