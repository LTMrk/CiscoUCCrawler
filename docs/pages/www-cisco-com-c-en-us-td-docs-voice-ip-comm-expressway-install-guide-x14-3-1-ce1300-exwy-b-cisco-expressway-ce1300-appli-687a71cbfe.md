---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-3-1-ce1300-exwy-b-cisco-expressway-ce1300-appli-687a71cbfe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-3-1/CE1300/exwy_b_cisco-expressway-ce1300-appliance-installation-guide-x1431/exwy_m_install-the-appliance.html
retrieved_at: 2026-08-16T22:10:11.031089+00:00
---

Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

# Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

Updated: October 15, 2024

Chapter: Install the Appliance

## Chapter: Install the Appliance

# Install the Appliance

This chapter explains the following:

## Task 1: Install into a Rack

For details about how to install the appliance into the rack, see the Cisco UCS C220 M6S Server Installation and Service Guide .

## Task 2: Insert the SFP Network Connection Modules

The CE1300 ships with two 10 Gb fiber SFP modules and two 1 Gb copper SFPs.

Caution

To avoid compatibility issues, the following restrictions apply to SFP modules.

Only use the SFPs supplied with the appliance. (Note that SFP modules from M4-based Expressways should not be reused in this
                                    appliance.)

Do not mix SFPs. Either insert two 10 Gb fiber SFPs or two 1 Gb copper SFPs.

The following requirements also apply to the SFPs:

Insert them only into the designated SFP ports on the PCIe 01 card. The leftmost SFP port corresponds to LAN1 on the Expressway
                                    user interface.

Although SFPs support auto-negotiation for speed and duplex, they only negotiate one speed—to the stated speed of the SFP
                                    and full duplex. This means you must connect them to a switch port that supports the stated speed and full duplex:

10 Gb full duplex for fiber SFPs

1 Gb full duplex for copper SFPs

If you are installing the CE1300 in an environment that only supports 100 Mb, such as an older DMZ implementation, you need
                                    a switch to handle the speed negotiation from 1 Gb to 100 Mb.

### Medium Appliances With 1 Gbps NIC - Demultiplexing Ports

If you upgrade a Medium appliance with a 1 Gbps NIC to X8.10 or later, Cisco VCS automatically converts the system to a Large
                              system. As a result, Cisco VCS Expressway listens for multiplexed RTP/RTCP traffic on the default demultiplexing ports for
                              Large systems (36000 to 36011) instead of on the demultiplexing ports that are configured for Medium systems. In this case,
                              the Cisco VCS Expressway drops the calls because ports 36000 to 36011 are not open on the firewall. From X8.11.4, you can
                              manually change the system size back to Medium through the System > Administration settings page (select Medium from the Deployment Configuration list).

## Task 3: Connect and Power On

Step 1

First connect designated power cords to the appliance, and then connect them to a grounded AC power outlet. See Cisco UCS C220 M6 SFF Rack Server Spec Sheet for power specifications.

Step 2

When you plug in the CE1300 appliance for the first time, leave it in standby mode for 5 minutes before pressing the power
                                       button. This time allows the onboard CIMC to boot, ready the self-test, perform a hardware check, and prepare the power characterization
                                       test. Failure to wait enough time will postpone the power characterization test until the next boot.

Step 3

To power on the appliance (the power button is at the top of the control panel on the right-hand side of the unit's front
                                       face). The system performs a self-test, and the appliance automatically restarts. This restart is expected behavior.

Step 4

The first boot takes approximately 5 minutes due to the initial power characterization test. Any subsequent boot of the system
                                       takes approximately 2 minutes. The power characterization test displays the message Performing Platform Characterization … when running.

Step 5

If the power characterization test runs on subsequent bootups, causing a lag in the boot time, it is important that you disable it . It is especially important to disable the test in a clustered environment to avoid issues. See the Appendix 1: Troubleshooting , for more information.

## Task 4: Verify Power Status

Check the Power Status LED on the front of the appliance:

Off. No AC power is present in the appliance.

Amber. Appliance is in standby power mode. Power is supplied only to the CIMC and some motherboard functions.

Green. Appliance is in main power mode. Power is supplied to all server components.

### Monitoring power consumption

The CIMC has a power monitoring utility that you can use to track power consumption.

| Caution | To avoid compatibility issues, the following restrictions apply to SFP modules. |
|---|---|

| Step 1 | First connect designated power cords to the appliance, and then connect them to a grounded AC power outlet. See Cisco UCS C220 M6 SFF Rack Server Spec Sheet for power specifications. |
|---|---|
| Step 2 | When you plug in the CE1300 appliance for the first time, leave it in standby mode for 5 minutes before pressing the power
                                       button. This time allows the onboard CIMC to boot, ready the self-test, perform a hardware check, and prepare the power characterization
                                       test. Failure to wait enough time will postpone the power characterization test until the next boot. |
| Step 3 | To power on the appliance (the power button is at the top of the control panel on the right-hand side of the unit's front
                                       face). The system performs a self-test, and the appliance automatically restarts. This restart is expected behavior. |
| Step 4 | The first boot takes approximately 5 minutes due to the initial power characterization test. Any subsequent boot of the system
                                       takes approximately 2 minutes. The power characterization test displays the message Performing Platform Characterization … when running. |
| Step 5 | If the power characterization test runs on subsequent bootups, causing a lag in the boot time, it is important that you disable it . It is especially important to disable the test in a clustered environment to avoid issues. See the Appendix 1: Troubleshooting , for more information. |