---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-ce1400v-exwy-b-cisco-expressway-ce1400v-appliance-i-c3a2beebd8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/CE1400V/exwy_b_cisco-expressway-ce1400v-appliance-installation-guide/exwy_m_set-up-your-appliance.html
retrieved_at: 2026-08-16T22:09:37.426173+00:00
---

Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

# Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

Updated: September 1, 2025

Chapter: Set Up Your Appliance

## Chapter: Set Up Your Appliance

# Set Up Your Appliance

Review the following topics before you begin your installation.

## Installation of Virtualization and Application Software

This section describes the tasks that you must perform to install virtualization and application software on your appliance.

VMware vSphere ESXi software is required but not included or factory-preloaded. It must be customer-provided and manually
                                    installed/licensed. See the technical documentation at Broadcom.com for more information.

Expressway application files are not factory-preloaded; they are sold separately and must be manually installed/licensed.

See Physical Appliance Installation and Upgrade Guides

## Installation Task Flow

Perform the following tasks to install software on your appliance.

Step 1

Configure Cisco Integrated Management Controller

Configure CIMC for your appliance.

Step 2

Install and Configure Virtualization Software

Install and configure the VMware vSphere ESXi software on the appliance.

### Configure Cisco Integrated Management Controller

Cisco Integrated Management Controller (CIMC) is the management interface for the Cisco UCS appliance. CIMC runs within the
                                 appliance, allowing remote administration, configuration, and monitoring of the appliance through web or SSH command-line
                                 access.

Step 1

Power on and initiate the CIMC Setup

Power on the appliance and begin the basic Cisco Integrated Management Controller (CIMC) configuration.

Step 2

Complete the CIMC Configuration

Configure DNS and NTP settings in the CIMC interface.

#### Power on and initiate the CIMC Setup

Perform this procedure to power on the appliance and begin the basic Cisco Integrated Management Controller (CIMC) configuration.

##### Before you begin

Ensure that the appliance has been rack-mounted, connected to a power supply, which is connected to the data network, and
                                    that a monitor and keyboard are connected to the appliance.

Step 1

Verify that power is connected and that the power button LED is orange .

Step 2

Push the appliance power button and verify that it changes to green .

Step 3

Watch the boot process on the monitor.

Step 4

When the blue Cisco logo appears, press F8 to enter the CIMC configuration dialog.

The appearance of this screen may vary with appliance model and firmware version.

Step 5

When prompted, enter the username admin and create a new password.

Step 6

On the CIMC configuration screen, complete the following details:

- CIMC IP address

- Subnet mask

- Gateway IP address

Step 7

When complete, press F10 to save your changes and boot the system.

#### Complete the CIMC Configuration

Perform this procedure to configure DNS and NTP settings in the CIMC interface.

##### Before you begin

Step 1

In a web browser, enter the CIMC IP address and log in with the username admin and the password that you created in the previous task.

Step 2

From the left menu, select the Admin tab, and click Network .

Step 3

In the home page, select the Network Settings tab.

Step 4

From Common Properties , change the Hostname setting to the CIMC hostname.

Step 5

From IPv4 Properties , change Preferred DNS Server to the IP address that you have specified for the DNS server.

Step 6

In the home page, select the NTP Settings tab.

Step 7

Check the Enable NTP check box.

Step 8

In the Server 1 field, enter the NTP server IP address.

Step 9

Select Save Changes from the bottom-right corner of the page.

### Install and Configure Virtualization Software

After installation of the VMware vSphere ESXi, you must change the default administrator username and password. See technical
                                 documentation on Broadcom.com for details on how to set up the virtualization software.

#### Install and Customize Virtualization Software

Follow this procedure to customize the VMware vSphere ESXi to enable remote access from your PC using the VMware Embedded Host Client.

Step 1

When the hypervisor boots, the ESXi Direct Console User Interface displays on the monitor as shown in the following figure.
                                             The appearance of this screen may vary with appliance model and preload version.

Step 2

Press F2 to enter the System Customization menu as shown in the following figure.

Step 3

After logging in, you must change the default password, choose Configure Password to change the password.

If your applications are predeployed, skip to step 5 .

Step 4

To assign a static IP address, select the Configure Management Network menu, and follow the instructions on screen to change "IP Configuration" .

Step 5

Connect your PC to the data network and browse to the new hypervisor IP address.

#### Access and Configure Virtualization Software

If you want to use the ESXi host as your NTP Server, see the technical documentation at Broadcom.com for how to set up.

If you want to use a Cisco router as your NTP Server, see the technical documentation for your router model at Cisco.com for
                                    how to set up.

Some applications require the host to have a valid time reference.

##### Before you begin

Step 1

Browse to the "https://[ESXI-HOST-IP-Address]/ui/" to access VMware Embedded Host Client.

Step 2

Use the login credentials that you previously configured.

Step 3

A license for VMware vSphere ESXi software is required but is not included with, sold with, or factory loaded on these appliances.
                                             It must be customer-provided and manually applied. On power up ESXi enters its time-limited evaluation mode as described on
                                             Broadcom.com ESXi 7.0/8.0 technical documentation. After expiry of evaluation mode, virtual machines will not be able to power
                                             up. If you want to re upload or version-upgrade this license, follow these steps:

Locate your license document that has the license serial number you use on the appliance.

Navigate to Manage > License > Assign License .

Type in or copy or paste the license serial number from the license document.

Click Check License to validate the license key.

Step 4

Configure NTP settings:

Navigate to Manage > System > Time & date .

Click Edit settings to launch the Edit time configuration screen.

Check Manually configure the date and time on this host check box.

Update the Time.

Check the Use Network Time Protocol (enable NTP client) check box.

Select Start and stop with host from NTP service startup policy drop-down.

Type the IP address of the NTP server in NTP servers . If you want to add multiple NTP servers, type the IP address of NTP servers that are separated by commas.

Click Save .

Step 5

(Optional) Configure fault tolerance by using the NIC teaming feature in VMware:

Navigate to the Networking > Management Network .

Click Edit settings to launch Edit port group- Management Network .

In the Edit port group Management Network screen, enter the name, VLANID, and virtual switch details.

Expand NIC teaming, enter the required details.

Click Save to add the NIC that is connected to the data network.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Cisco Integrated Management Controller | Configure CIMC for your appliance. |
| Step 2 | Install and Configure Virtualization Software | Install and configure the VMware vSphere ESXi software on the appliance. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Power on and initiate the CIMC Setup | Power on the appliance and begin the basic Cisco Integrated Management Controller (CIMC) configuration. |
| Step 2 | Complete the CIMC Configuration | Configure DNS and NTP settings in the CIMC interface. |

| Step 1 | Verify that power is connected and that the power button LED is orange . |
|---|---|
| Step 2 | Push the appliance power button and verify that it changes to green . |
| Step 3 | Watch the boot process on the monitor. |
| Step 4 | When the blue Cisco logo appears, press F8 to enter the CIMC configuration dialog. Note The appearance of this screen may vary with appliance model and firmware version. Figure 1. Press F8 at the CIMC Boot Screen | Note | The appearance of this screen may vary with appliance model and firmware version. |
| Note | The appearance of this screen may vary with appliance model and firmware version. |
| Step 5 | When prompted, enter the username admin and create a new password. |
| Step 6 | On the CIMC configuration screen, complete the following details: CIMC IP address Subnet mask Gateway IP address Figure 2. Enter the CIMC IP Address Details |
| Step 7 | When complete, press F10 to save your changes and boot the system. |

| Note | The appearance of this screen may vary with appliance model and firmware version. |
|---|---|

| Step 1 | In a web browser, enter the CIMC IP address and log in with the username admin and the password that you created in the previous task. |
|---|---|
| Step 2 | From the left menu, select the Admin tab, and click Network . |
| Step 3 | In the home page, select the Network Settings tab. |
| Step 4 | From Common Properties , change the Hostname setting to the CIMC hostname. |
| Step 5 | From IPv4 Properties , change Preferred DNS Server to the IP address that you have specified for the DNS server. |
| Step 6 | In the home page, select the NTP Settings tab. |
| Step 7 | Check the Enable NTP check box. |
| Step 8 | In the Server 1 field, enter the NTP server IP address. |
| Step 9 | Select Save Changes from the bottom-right corner of the page. |

| Step 1 | When the hypervisor boots, the ESXi Direct Console User Interface displays on the monitor as shown in the following figure.
                                             The appearance of this screen may vary with appliance model and preload version. Figure 3. Console Screen After ESXi Loads |
|---|---|
| Step 2 | Press F2 to enter the System Customization menu as shown in the following figure. Figure 4. ESXi System Customization Menu. For the default username and password, see the technical documentation at Broadcom.com. |
| Step 3 | After logging in, you must change the default password, choose Configure Password to change the password. If your applications are predeployed, skip to step 5 . |
| Step 4 | To assign a static IP address, select the Configure Management Network menu, and follow the instructions on screen to change "IP Configuration" . Figure 5. Assign Static IP Address to ESXi Host |
| Step 5 | Connect your PC to the data network and browse to the new hypervisor IP address. Figure 6. Hypervisor Welcome Page |

| Note | Some applications require the host to have a valid time reference. |
|---|---|

| Step 1 | Browse to the "https://[ESXI-HOST-IP-Address]/ui/" to access VMware Embedded Host Client. Figure 7. Access Virtualization Software Using VMware Embedded Host Client |
|---|---|
| Step 2 | Use the login credentials that you previously configured. |
| Step 3 | A license for VMware vSphere ESXi software is required but is not included with, sold with, or factory loaded on these appliances.
                                             It must be customer-provided and manually applied. On power up ESXi enters its time-limited evaluation mode as described on
                                             Broadcom.com ESXi 7.0/8.0 technical documentation. After expiry of evaluation mode, virtual machines will not be able to power
                                             up. If you want to re upload or version-upgrade this license, follow these steps: Locate your license document that has the license serial number you use on the appliance. Navigate to Manage > License > Assign License . Type in or copy or paste the license serial number from the license document. Click Check License to validate the license key. |
| Step 4 | Configure NTP settings: Navigate to Manage > System > Time & date . Click Edit settings to launch the Edit time configuration screen. Check Manually configure the date and time on this host check box. Update the Time. Check the Use Network Time Protocol (enable NTP client) check box. Select Start and stop with host from NTP service startup policy drop-down. Type the IP address of the NTP server in NTP servers . If you want to add multiple NTP servers, type the IP address of NTP servers that are separated by commas. Click Save . |
| Step 5 | (Optional) Configure fault tolerance by using the NIC teaming feature in VMware: Navigate to the Networking > Management Network . Click Edit settings to launch Edit port group- Management Network . In the Edit port group Management Network screen, enter the name, VLANID, and virtual switch details. Expand NIC teaming, enter the required details. Click Save to add the NIC that is connected to the data network. |