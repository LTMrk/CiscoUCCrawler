---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-6-2-installandupgrade-guide-vvb-619547c45c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb_12_6_2/installandupgrade/guide/vvb_b_install-and-upgrade-guide-12-62/vvb_b_install-and-upgrade-guide-12-5_chapter_0100.html
retrieved_at: 2026-08-21T16:25:54.730352+00:00
---

Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 12.6(2)

# Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 12.6(2)

Updated: August 24, 2023

Chapter: Cisco VVB Uninstallation on KVM

## Chapter: Cisco VVB Uninstallation on KVM

- Cisco VVB Uninstallation on KVM

- Uninstall Cisco VVB on KVM

# Cisco VVB Uninstallation on KVM

## Cisco VVB Uninstallation on KVM

### Uninstall Cisco VVB on KVM

Step 1

Deactivate virtual-service from the virtual-service config mode by running:

no activate

#### Example:

```
router# configure Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
router(config)#
router(config)# virtual-service vvb router(config-virt-serv)# no activate router(config-virt-serv)# ^Z router# show virtual-service list Virtual Service List:

Name                    Status             Package Name
------------------------------------------------------------------------------ vvb                Deactivating            VVB_12_5_1_ISR4K.ova Name                    Status             Package Name
------------------------------------------------------------------------------ vvb                Deactivated             VVB_12_5_1_ISR4K.ova
```

This can take around 5-10 minutes.

Step 2

In the privileged EXEC mode, run:

virtual-service uninstall name <name>

#### Example:

```
router# virtual-service uninstall name vvb
```

The virtual-service name is case-sensitive and must match the name given in Step 2 of the preceding procedure.

Step 3

To verify the VVB instance was successfully deactivated/uninstalled, run:

show log

#### Example:

```
router# show log ------------------------------------------------------------------------------ show log *Aug  1 08:51:48.845: %VIRT_SERVICE-5-ACTIVATION_STATE: Successfully deactivated virtual service vvb
*Aug  1 08:52:45.418: %VIRT_SERVICE-5-INSTALL_STATE: Successfully uninstalled virtual service vvb
```

show virtual-service list

#### Example:

```
router# show virtual-service list Virtual Service List:
```

The output of the command must be empty.

| Step 1 | Deactivate virtual-service from the virtual-service config mode by running: no activate Example: router# configure Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
router(config)#
router(config)# virtual-service vvb router(config-virt-serv)# no activate router(config-virt-serv)# ^Z router# show virtual-service list Virtual Service List:

Name                    Status             Package Name
------------------------------------------------------------------------------ vvb                Deactivating            VVB_12_5_1_ISR4K.ova Name                    Status             Package Name
------------------------------------------------------------------------------ vvb                Deactivated             VVB_12_5_1_ISR4K.ova Note This can take around 5-10 minutes. | Note | This can take around 5-10 minutes. |
|---|---|---|---|
| Note | This can take around 5-10 minutes. |
| Step 2 | In the privileged EXEC mode, run: virtual-service uninstall name <name> Example: router# virtual-service uninstall name vvb Note The virtual-service name is case-sensitive and must match the name given in Step 2 of the preceding procedure. | Note | The virtual-service name is case-sensitive and must match the name given in Step 2 of the preceding procedure. |
| Note | The virtual-service name is case-sensitive and must match the name given in Step 2 of the preceding procedure. |
| Step 3 | To verify the VVB instance was successfully deactivated/uninstalled, run: show log Example: router# show log ------------------------------------------------------------------------------ show log *Aug  1 08:51:48.845: %VIRT_SERVICE-5-ACTIVATION_STATE: Successfully deactivated virtual service vvb
*Aug  1 08:52:45.418: %VIRT_SERVICE-5-INSTALL_STATE: Successfully uninstalled virtual service vvb show virtual-service list Example: router# show virtual-service list Virtual Service List: Note The output of the command must be empty. | Note | The output of the command must be empty. |
| Note | The output of the command must be empty. |

| Note | This can take around 5-10 minutes. |
|---|---|

| Note | The virtual-service name is case-sensitive and must match the name given in Step 2 of the preceding procedure. |
|---|---|

| Note | The output of the command must be empty. |
|---|---|