---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-3-1-ce1300-exwy-b-cisco-expressway-ce1300-appli-c4181c3aa7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-3-1/CE1300/exwy_b_cisco-expressway-ce1300-appliance-installation-guide-x1431/exwy_m_troubleshooting.html
retrieved_at: 2026-08-16T22:10:31.699466+00:00
---

Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

# Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

Updated: October 15, 2024

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

This chapter explains the following:

## Locating LEDs and Components

The panel layouts for this appliance are described in:

Front Panel Layout

Rear Panel Layout

## Definitions of LED States

The various LED states are defined in the Cisco UCS C220 M6S Server Installation and Service Guide .

## Reset from the Internal Recovery Partition (IRP)

The Cisco Expressway CE1300 appliance comes pre-installed with an M.2 device that you can use to reinstall of your appliance
                              to factory state.

### Before you begin

You need to set up and access the CIMC, as described in Run the Install Wizard .

### Task: IRP Reinstall Using the KVM Console

Step 1

Launch the KVM Console using the icon in the CIMC.

Step 2

Power up the CE1300 and, when prompted, press F6 to enter the boot menu .

Step 3

Select USER: Built-in EFI Shell as the boot option.

The EFI shell will load and, after 5 seconds will launch the startup.nsh by default, which will load the recovery image.

Step 4

When prompted, type y to press Enter to proceed with the reinstall.

The login prompt may interfere with entering y , press Enter to bypass the prompt and press y again and enter to launch the reimage.

Step 5

After the reboot completes, connect using serial to complete the reset. You will see the factory installation wizard.

Step 6

You can optionally apply any option keys for the appliance (such as room or desktop registrations). If you choose not to at
                                          this stage, they can be applied later through the Expressway web UI or CLI.

Step 7

When prompted, press Enter to shutdown the system.

The factory installation wizard phase is complete.

Step 8

Power on the appliance, and follow the steps in Run the Install Wizard to complete the customer installation wizard.

## Lag During Boot up Due to Power Characterization Check

Step 1

Log in to the CIMC (see Connecting Using CIMC Serial Over LAN ).

Step 2

Click the menu arrow in the top-left corner.

Step 3

Go to Chassis > Power management > Power Cap Configuration .

Step 4

Click Disable Power Characterization .

Step 5

Click Save Changes .

| Step 1 | Launch the KVM Console using the icon in the CIMC. |
|---|---|
| Step 2 | Power up the CE1300 and, when prompted, press F6 to enter the boot menu . |
| Step 3 | Select USER: Built-in EFI Shell as the boot option. The EFI shell will load and, after 5 seconds will launch the startup.nsh by default, which will load the recovery image. |
| Step 4 | When prompted, type y to press Enter to proceed with the reinstall. The login prompt may interfere with entering y , press Enter to bypass the prompt and press y again and enter to launch the reimage. |
| Step 5 | After the reboot completes, connect using serial to complete the reset. You will see the factory installation wizard. |
| Step 6 | You can optionally apply any option keys for the appliance (such as room or desktop registrations). If you choose not to at
                                          this stage, they can be applied later through the Expressway web UI or CLI. |
| Step 7 | When prompted, press Enter to shutdown the system. The factory installation wizard phase is complete. |
| Step 8 | Power on the appliance, and follow the steps in Run the Install Wizard to complete the customer installation wizard. |

| Step 1 | Log in to the CIMC (see Connecting Using CIMC Serial Over LAN ). |
|---|---|
| Step 2 | Click the menu arrow in the top-left corner. |
| Step 3 | Go to Chassis > Power management > Power Cap Configuration . |
| Step 4 | Click Disable Power Characterization . |
| Step 5 | Click Save Changes . |