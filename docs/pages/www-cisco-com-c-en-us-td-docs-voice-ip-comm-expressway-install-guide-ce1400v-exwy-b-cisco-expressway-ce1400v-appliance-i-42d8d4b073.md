---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-ce1400v-exwy-b-cisco-expressway-ce1400v-appliance-i-42d8d4b073
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/CE1400V/exwy_b_cisco-expressway-ce1400v-appliance-installation-guide/exwy_m_install-the-appliance.html
retrieved_at: 2026-08-16T22:09:33.063968+00:00
---

Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

# Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

Updated: September 1, 2025

Chapter: Install the Appliance

## Chapter: Install the Appliance

# Install the Appliance

This chapter explains the following:

## Task 1: Install into a Rack

For details about how to install the appliance into the rack, see the Cisco UCS C220 M7 Server Installation and Service Guide .

## Task 2: Insert the SFP Network Connection Modules

The CE1400V ships with a pair of four-port SFP+ NICs. An SFP+ transceiver is required on each NIC port that will connect to
                              your network. Either SFP-10G-SR for fiber, or GLC-TE for copper.

Caution

To avoid compatibility issues, the following restrictions apply to SFP modules.

Only use the Cisco SFP-10G-SR or GLC-TE SFP+ transceivers.

SFP modules from M4-based Expressways should not be reused in this appliance.

Do not mix SFP+ transceivers. Either use all fiber or all copper.

The following requirements also apply to the SFPs:

Although SFPs support auto-negotiation for speed and duplex, they only negotiate one speed—to the stated speed of the SFP
                                    and full duplex. This means you must connect them to a switch port that supports the stated speed and full duplex:

10 Gb full duplex for fiber SFPs

1 Gb full duplex for copper SFPs

If you are installing the CE1400V in an environment that only supports 100 Mb, such as an older DMZ implementation, you need
                                    a switch to handle the speed negotiation from 1 Gb to 100 Mb.

## Task 3: Connect and Power On

Step 1

First connect designated power cords to the appliance and then connect them to a grounded AC power outlet. See Cisco UCS C220 M7 SFF Rack Server Spec Sheet for power specifications.

Step 2

When you plug in the CE1400V appliance for the first time, leave it in standby mode for 5 minutes before pressing the power
                                       button. This time allows the onboard CIMC to boot, prepare the self-test, perform a hardware check, and prepare the power
                                       characterization test. Failure to wait enough time will postpone the power characterization test until the next boot.

Step 3

To power on the appliance (the power button is at the top of the control panel on the right-hand side of the unit's front
                                       face). The system performs a self-test, and the appliance automatically restarts. This restart is expected behavior.

Step 4

The first boot takes approximately 5 minutes due to the initial power characterization test. Any subsequent boot of the system
                                       takes approximately 2 minutes. The power characterization test displays the message Performing Platform Characterization … when running.

Step 5

If the power characterization test runs on subsequent bootups, causing a lag in the boot time, it is important that you disable it . It is especially important to disable the test in a clustered environment to avoid issues.

### What to do next

## Task 4: Verify Power Status

Check the Power Status LED on the front of the appliance:

Off. No AC power is present in the appliance.

Amber. Appliance is in standby power mode. Power is supplied only to the CIMC and some motherboard functions.

Green. Appliance is in main power mode. Power is supplied to all server components.

### Monitoring power consumption

The CIMC has a power monitoring utility that you can use to track power consumption.

| Caution | To avoid compatibility issues, the following restrictions apply to SFP modules. |
|---|---|

| Note | SFP modules from M4-based Expressways should not be reused in this appliance. |
|---|---|

| Step 1 | First connect designated power cords to the appliance and then connect them to a grounded AC power outlet. See Cisco UCS C220 M7 SFF Rack Server Spec Sheet for power specifications. |
|---|---|
| Step 2 | When you plug in the CE1400V appliance for the first time, leave it in standby mode for 5 minutes before pressing the power
                                       button. This time allows the onboard CIMC to boot, prepare the self-test, perform a hardware check, and prepare the power
                                       characterization test. Failure to wait enough time will postpone the power characterization test until the next boot. |
| Step 3 | To power on the appliance (the power button is at the top of the control panel on the right-hand side of the unit's front
                                       face). The system performs a self-test, and the appliance automatically restarts. This restart is expected behavior. |
| Step 4 | The first boot takes approximately 5 minutes due to the initial power characterization test. Any subsequent boot of the system
                                       takes approximately 2 minutes. The power characterization test displays the message Performing Platform Characterization … when running. |
| Step 5 | If the power characterization test runs on subsequent bootups, causing a lag in the boot time, it is important that you disable it . It is especially important to disable the test in a clustered environment to avoid issues. |