---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-0-ce1200-exwy-b-cisco-expressway-ce1200-applian-5afc078d3f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-0/CE1200/exwy_b_cisco-expressway-ce1200-appliance-installation-guide-x14-0/exwy_m_appendix-troubleshooting.html
retrieved_at: 2026-08-16T22:17:08.059036+00:00
---

Cisco Expressway CE1200 Appliance Installation Guide (X14.0)

# Cisco Expressway CE1200 Appliance Installation Guide (X14.0)

Updated: April 14, 2021

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Locating LEDs and Components

The panel layouts for this appliance are described in:

Front Panel Layout

Rear Panel Layout

## Definitions of LED States

The various LED states are defined in the Cisco UCS C220 M5 Server Installation and
                           			Service Guide at https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/hw/C220M5/install/C220M5.html

## Reset from the Internal Recovery Partition (IRP)

The Cisco Expressway CE1200 appliance comes pre-installed with an SD card that you can
                           			use to complete a reinstall of your configuration. You must reset the SD card and enable
                           			the virtual drive before proceeding with the reinstall using the KVM console in the
                           			Cisco Integrated Management Controller (CIMC). Once the reset is complete, make sure
                           			that you disable the virtual drive again.

### Before you begin

You need to set up and access the CIMC, as described in Run the Install Wizard .

### Task 1: Reset the SD Card and Enable the Virtual Drive

Log in to the CIMC.

Click the menu arrow in the top left corner and navigate to Storage > Cisco FlexFlash .

Under the General tab, click Activate/Reset
                                             						FlexFlash Controller and click ok in the
                                          					popup window that appears. The reset ensures your FlexFlash Controller is in the
                                          					correct state.

Click the Virtual Drives tab.

Check the Hypervisor checkbox.

Click Enable Virtual Drive and confirm that you would
                                          					like to enable the virtual drive.

### Task 2: IRP Reinstall Using the KVM Console

Launch the KVM Console using the icon in the CIMC.

Power up the CE1200 and, when prompted, press F2 to enter setup .

Select Boot Options and ensure that the CiscoVD
                                             						Hypervisor is visible as one of the options.

When prompted, press F6 to enter the Boot
                                             						Menu .

Select CiscoVD Hypervisor as the boot option.

When prompted, type y and press Enter to
                                          					proceed with the reinstall.

Type b to reboot.

During this reboot we recommend disabling the virtual drive (although you can
                                             						also do it later as described in Task 3 below). To disable the virtual drive
                                             						now:

Press F2 to enter boot Setup.

Under Boot options select CiscoVD
                                                      									Hypervisor and disable it.

Press F10 to save and exit.

While the system reboots, return to the Virtual Drive
                                                      									info tab—in the CIMC interface under Storage—and
                                                   								check the Hypervisor checkbox. Click Disable .

After the reboot completes, connect using serial to complete the reset. You
                                          					will see the factory installation wizard.

You can optionally apply any option keys for the appliance (such as room or
                                          					desktop registrations). If you choose not to at this stage, they can be applied
                                          					later through the Expressway web UI or CLI.

When prompted, press Enter to shutdown the system.

The factory installation wizard phase is complete.

Power on the appliance, and follow the steps in Run the Install Wizard to
                                          					complete the customer installation wizard.

### Task 3: Disable the Virtual Drive After the Reinstall

Access the CIMC interface.

Go to Storage > Virtual Drive info tab.

Check the Hypervisor checkbox, then press Disable .

## Lag During Boot up Due to Power Characterization Check

Log in to the CIMC (see Connecting Using CIMC Serial Over
                                          						LAN ).

Click the menu arrow in the top-left corner.

Go to Chassis > Power management > Power Cap Configuration .

Click Disable Power Characterization .

Click Save Changes .

| Step 1 | Log in to the CIMC. |
|---|---|
| Step 2 | Click the menu arrow in the top left corner and navigate to Storage > Cisco FlexFlash . |
| Step 3 | Under the General tab, click Activate/Reset
                                             						FlexFlash Controller and click ok in the
                                          					popup window that appears. The reset ensures your FlexFlash Controller is in the
                                          					correct state. |
| Step 4 | Click the Virtual Drives tab. |
| Step 5 | Check the Hypervisor checkbox. |
| Step 6 | Click Enable Virtual Drive and confirm that you would
                                          					like to enable the virtual drive. |

| Step 1 | Launch the KVM Console using the icon in the CIMC. |
|---|---|
| Step 2 | Power up the CE1200 and, when prompted, press F2 to enter setup . |
| Step 3 | Select Boot Options and ensure that the CiscoVD
                                             						Hypervisor is visible as one of the options. |
| Step 4 | When prompted, press F6 to enter the Boot
                                             						Menu . |
| Step 5 | Select CiscoVD Hypervisor as the boot option. |
| Step 6 | When prompted, type y and press Enter to
                                          					proceed with the reinstall. |
| Step 7 | Type b to reboot. During this reboot we recommend disabling the virtual drive (although you can
                                             						also do it later as described in Task 3 below). To disable the virtual drive
                                             						now: Press F2 to enter boot Setup. Under Boot options select CiscoVD
                                                      									Hypervisor and disable it. Press F10 to save and exit. While the system reboots, return to the Virtual Drive
                                                      									info tab—in the CIMC interface under Storage—and
                                                   								check the Hypervisor checkbox. Click Disable . |
| Step 8 | After the reboot completes, connect using serial to complete the reset. You
                                          					will see the factory installation wizard. |
| Step 9 | You can optionally apply any option keys for the appliance (such as room or
                                          					desktop registrations). If you choose not to at this stage, they can be applied
                                          					later through the Expressway web UI or CLI. |
| Step 10 | When prompted, press Enter to shutdown the system. The factory installation wizard phase is complete. |
| Step 11 | Power on the appliance, and follow the steps in Run the Install Wizard to
                                          					complete the customer installation wizard. |

| Step 1 | Access the CIMC interface. |
|---|---|
| Step 2 | Go to Storage > Virtual Drive info tab. |
| Step 3 | Check the Hypervisor checkbox, then press Disable . |

| Step 1 | Log in to the CIMC (see Connecting Using CIMC Serial Over
                                          						LAN ). |
|---|---|
| Step 2 | Click the menu arrow in the top-left corner. |
| Step 3 | Go to Chassis > Power management > Power Cap Configuration . |
| Step 4 | Click Disable Power Characterization . |
| Step 5 | Click Save Changes . |