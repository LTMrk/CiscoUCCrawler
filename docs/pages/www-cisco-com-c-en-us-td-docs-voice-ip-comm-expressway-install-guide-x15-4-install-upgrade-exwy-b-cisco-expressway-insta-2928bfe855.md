---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-4-install-upgrade-exwy-b-cisco-expressway-insta-2928bfe855
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-4/install-upgrade/exwy_b_cisco-expressway-install-and-upgrade-guide-x154/exwy_m_hardware-references.html
retrieved_at: 2026-08-16T22:07:28.723927+00:00
---

Cisco Expressway Install and Upgrade Guide (X15.4)

# Cisco Expressway Install and Upgrade Guide (X15.4)

Updated: April 3, 2026

Chapter: Hardware References

## Chapter: Hardware References

# Hardware References

## Serial Interface

A VM Expressway has no physical serial interface; the serial interface is accessible through the console tab of the VM guest.

You can use CTRL+ALT to exit from the Console window (this is identified in the bottom right corner of the vSphereClient window).

## Ethernet Interfaces (NICs)

In VM Expressway the LAN interfaces are Virtual NICs. Appropriate drivers are set up as VM Expressway is installed; configuration
                              of IP addresses is carried out through the standard Expressway interface.

VM Expressway allocates 3 virtual NICs:

The first is used for the standard LAN 1 interface.

The second is used if Dual Network interfaces are enabled (LAN 2).

The third is reserved for future use.

## ESXi specific - Allocating a Virtual NIC to a Physical NIC Interface

Step 1

Ensure that the physical NIC on the VM host is connected and operational.

Step 2

Set up or check that there are Virtual Switches (vNetwork Distributed Switches) for each physical NIC. (Select the host on
                                       which the VM Expressway will run, select the Configuration tab and select Networking .)

Step 3

Ensure that there is at least one Virtual Machine Port Group (with associated VLAN IDs) set up for each physical NIC.

To add a new Virtual Machine Port Group, click Properties on the appropriate Virtual Switch or vNetwork Distributed Switch.

Follow the network wizard.

Step 4

Note the name of a Virtual Machine Port Group connecting to the required NIC.

Step 5

Select the VM guest; right click it and select Edit settings…

Step 6

Select the required network adaptor (Network adaptor 1 = LAN 1, Network adaptor 2 = LAN 2).

Step 7

Select the appropriate Network label (Virtual Machine Port Group) to associate the Expressway LAN interface with the required
                                       physical NIC.

Step 8

After a few seconds the Expressway will be able to communicate over the physical interface.

| Step 1 | Ensure that the physical NIC on the VM host is connected and operational. |
|---|---|
| Step 2 | Set up or check that there are Virtual Switches (vNetwork Distributed Switches) for each physical NIC. (Select the host on
                                       which the VM Expressway will run, select the Configuration tab and select Networking .) |
| Step 3 | Ensure that there is at least one Virtual Machine Port Group (with associated VLAN IDs) set up for each physical NIC. To add a new Virtual Machine Port Group, click Properties on the appropriate Virtual Switch or vNetwork Distributed Switch. Follow the network wizard. |
| Step 4 | Note the name of a Virtual Machine Port Group connecting to the required NIC. |
| Step 5 | Select the VM guest; right click it and select Edit settings… Figure 1. Edit Settings |
| Step 6 | Select the required network adaptor (Network adaptor 1 = LAN 1, Network adaptor 2 = LAN 2). Figure 2. Select Network Adaptor |
| Step 7 | Select the appropriate Network label (Virtual Machine Port Group) to associate the Expressway LAN interface with the required
                                       physical NIC. |
| Step 8 | After a few seconds the Expressway will be able to communicate over the physical interface. |