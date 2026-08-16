---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-3-1-ce1300-exwy-b-cisco-expressway-ce1300-appli-444ffe20d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-3-1/CE1300/exwy_b_cisco-expressway-ce1300-appliance-installation-guide-x1431/exwy_m_run-the-install-wizard.html
retrieved_at: 2026-08-16T22:10:19.017504+00:00
---

Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

# Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

Updated: October 15, 2024

Chapter: Run the Install Wizard

## Chapter: Run the Install Wizard

- Run the Install Wizard

- Install Wizard Process

# Run the Install Wizard

After the system boots up the terminal emulator program on the PC displays Cisco Expressway startup information. After approximately
                        four minutes the Install Wizard is displayed.

If the Cisco Expressway was already on when you connected and you do not see the Install Wizard, press Ctrl+D to access it. If you encounter issues or enter incorrect information during the wizard, you can press Ctrl+D to restart it.

This chapter explains the following:

## Install Wizard Process

Follow the prompts in the Install Wizard to specify the following:

IPv4, IPv6, or both.

LAN 1 IPv4 subnet mask of the Cisco Expressway (if you select IPv4).

IP address of the Expressway default gateway.

Password for root user account.

Password for admin user account.

Whether to enable the Expressway web UI (recommended).

If you plan to deploy the appliance as an Expressway-E then you must enable the web UI. It's not possible to configure the
                                    appliance as an Expressway-E through the CLI.

Whether to allow SSH access to the Cisco Expressway CLI.

Timezone. The default is UTC. You can search and replace with your desired zone in the wizard. Or you can change it later
                                          through the System > Time page in the web user interface.

Wait for the wizard to finish and the Installation wizard complete message to appear.

Press Enter to continue.

The system applies the specified settings and continues to boot.

After the boot completes, the Expressway is ready to use.

The system services restart after the wizard completes. This is expected behavior.

You can now access the Expressway user interface using the IP address assigned to the LAN1 Ethernet port (see next section).

| Note | The system services restart after the wizard completes. This is expected behavior. |
|---|---|