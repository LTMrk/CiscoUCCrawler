---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-exwy-b-cisco-expressway-on-virtual-machine-exwy-b-v-66f5af37a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/exwy_b_cisco-expressway-on-virtual-machine/exwy_b_vm-install-guide_chapter_011.html
retrieved_at: 2026-08-21T18:07:43.538708+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X12.7)

# Cisco Expressway on Virtual Machine Installation Guide (X12.7)

Updated: April 8, 2020

Chapter: Installing a Virtual Machine

## Chapter: Installing a Virtual Machine

# Installing a Virtual Machine

## Installation Process

This process guides you through installing the Expressway VM using vCenter or vSphere client. Before you start the installation,
                           make sure all the system requirements are in place, as detailed in System Requirements .

## Configuring the VM Host

### Before you begin

Ensure that the VM host is configured with a valid NTP server – the same NTP server that will be specified in Expressway.

Select the host.

Go to the Configuration tab.

Select Time configuration .

Select Properties .

If the date and time were red on the previous page, set the date and time manually to the current time.

Click Options .

Select NTP Settings .

Click Add .

Enter the IP address of the NTP server.

Click OK .

Select the Restart NTP service to apply changes check box.

Click OK .

Click OK .

### What to do next

The following section describes how to deploy the ova to host using vCenter. If you are using vSphere, skip this section and
                              go to Deploying OVA to Standalone ESXi Host .

## Deploying OVA to Host Managed by vCenter

These instructions represent a typical installation. The Deploy OVF Template wizard dynamically changes to reflect host configuration.

If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments):

Using a web browser, go to https:///folder supplying any required credentials (typically the same username and password as used to log into vCenter ).

Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore.

Right click on the .ova file and select Copy Link Location .

(If the .ova file is not preloaded on the datastore, you can select and upload it in the following steps.)

Log in to vCenter to access the ESXi Host.

Select File > Deploy OVF Template.

On the Source page, identify where the .ova file is located, and then click Next .

If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that vCenter can access the web server.

If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file.

On the OVF Template Details page, check that the Publisher certificate is valid and click Next .

On the End User License Agreement page:

Read the EULA.

If you accept the EULA, click Accept then Next .

On the Name and Location page enter a Name for this Expressway VM guest, for example " Virtual_ Expressway " and click Next .

When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base.

On the Deployment Configuration page, select the appropriately sized deployment:

Select Small , Medium or Large depending on the capabilities of the VMware host.

The default is Medium. See System Requirements for details about resource requirements. If the VMware host has insufficient resources, the virtual Expressway will fail
                                                to power on / boot.

Click Next .

On the Host / Cluster page, select where you want to run the virtual Expressway and click Next .

On the Resource Pool page, select where you want to run the virtual Expressway and click Next .

On the Storage page, select the location onto which the virtual Expressway will be deployed and click Next .

On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next .

On the Network Mapping page, select the network mapping that applies to your infrastructure (the default is VM Network ) and then click Next .

In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters.

On the Properties page, configure the network properties of the virtual Expressway and click Next .

The properties you can set include the Expressway's IPv4 and IPv6 settings, option to enable DMI, and configure DMI Address
                                          and DMI Netmask, System, hostname and domain, up to five NTP servers, and up to five DNS servers. For automated deployments
                                          you can also enter an RSA SSH public key to securely set the root and admin passwords via SSH. If you do not enter a public
                                          key, you must set the passwords during the Install Wizard process.

The hostname and domain name must contain only ASCII characters

On the Ready to Complete page:

Confirm the deployment settings.

Select the Power on after deployment check box.

Click Finish .

The installation process will begin and a progress bar will be displayed.

The Expressway ova is now deployed as a Guest on the VM Host.

## Configuring the VM Guest (vCenter)

These instructions describe how to set the root and admin password over SSH if you entered an RSA SSH public key in the VM Properties page – used primarily for automated deployments - or using the Install Wizard.

### Set the Root and Admin Password Using the Install Wizard

Select the VM guest and then select the Console tab.

Enter and confirm your root and admin passwords. You will also be prompted to set any properties you did not set in VMware.

These passwords should be unique; do not use the same password for admin and root accounts.

Press Enter to apply the configuration.

The Expressway will apply the configuration and reboot.

You should now be able to access the Expressway using a web browser.

You can now order your option keys; see Expressway Service Selection, Licenses, and Basic Configuration .

### Set the Root and Admin Password Using SSH

The Install Wizard starts an SSH daemon, listening on port 5022, so you can set the root and admin password.

Connect as user "wizard" using an SSH client on port 5022 (for example: ssh wizard@10.0.0.1 -p 5022 ).

Follow the prompt to set admin.password and root.password .

The Expressway will apply the configuration and reboot.

You should now be able to access the Expressway using a web browser.

You can now order your option keys; see Expressway Service Selection, Licenses, and Basic Configuration .

## Deploying OVA to Standalone ESXi Host

If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments):

Using a web browser, go to https://<VMwareHost>/folder supplying any required credentials (typically the same username and password as used to log into the vSphere client).

Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore.

Right click on the .ova file and select Copy Link Location .

(If the .ova file is not preloaded on the datastore, you can select and upload it in the following steps.)

Log in to the vSphere client to access the ESXi Host.

Select File > Deploy OVF Template .

On the Source page, identify where the .ova file is located, and then click Next .

If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that the vSphere client can access the web server.

- If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file. Figure 17. Browse .ova File

On the OVF Template Details page, check that the Publisher certificate is valid and click Next .

On the End User License Agreement page:

Read the EULA

If you accept the EULA, click Accept then Next .

On the Name and Location page enter a Name for this Expressway VM guest, for example "Virtual_Expressway" and click Next .

When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base

On the Deployment Configuration page, select the appropriately sized deployment:

Select Small , Medium or Large depending on the capabilities of the VMware host.

The default is Medium . See System Requirements for details about resource requirements. If theVMware host has insufficient resources, the virtual Expressway will fail to
                                                power on / boot.

Click Next .

On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next .

On the Ready to Complete page:

Confirm the deployment settings.

Select the Power on after deployment check box.

Click Finish .

The installation process will begin and a progress bar will be displayed.

## Configuring the VM Guest (ESXi Host)

If you encounter issues or enter incorrect information during the wizard you can press Ctrl+D to restart.

The pre-X8.9 default passwords of the admin and root accounts are well known. You must use strong passwords for these accounts.
                                                If your new system is on X8.9 or later, you must supply non-default passwords.

The pre-X8.9 default passwords of the admin and root accounts are well known. You must use strong passwords for these accounts.
                                                If your new system is on X8.9 or later, you must supply non-default passwords.

The default timezone is UTC but you can search for your desired timezone. You can also change it later in the web interface
                                                by going to System > Time .

The default values support tab completion.

Select the VM guest and then select the Console tab.

The VM guest will take some time to boot, create its second hard disk partition and then reboot to the Install Wizard.

Follow the prompts given by the Install Wizard to specify the following:

Whether you want to use IPv4, IPv6 or Both.

The LAN 1 IPv4 subnet mask of the Expressway (if you have selected IPv4).

The IP address of the default gateway of the Expressway.

The root password. Should be unique, do not use the same password as for admin account.

The admin password. Should be unique, do not use the same password as for root account.

Whether you want to enable the web UI.

Whether you want to use SSH to administer the Expressway.

The timezone.

After the wizard is finished the following message will appear:

Installation wizard complete

Press Enter to continue the boot and apply the configuration.

Press Enter .

After it has applied the configuration and rebooted, the Expressway is ready to use. You should now be able to access the
                                       Expressway using a web browser.

### What to do next

You can now manage the Expressway licensing and basic configuration; see Expressway Service Selection, Licenses, and Basic Configuration .

## Automating the Deployment Process

We recommend deploying an Expressway VMWare OVA in an automated manner. To do this:

Deploy the VM using VMWare’s OVFTool:

```
Ovftool –acceptAllEulas -ds=<vsphere datastore> --powerOn –noSSLVerify 
--name=<name of VM> --prop:ip4.address=<ip address> --prop:ip4.gateway=<gateway> 
--prop:ip4.netmask=<subnet mask> --prop.dmi.enable=<enable> 
--prop.dmi.ip4.address=<dmi ipv4 address> --prop.dmi.ip4.netmask=<dmi ipv4 netmask> 
--prop.dmi.ip6.address=<dmi ipv6 address> --prop:default.dns=1.1.1.1 -nw=<vsphere network> 
--X:waitForIp --prop:ssh.public.key=’<public ssh key>’ <OVA file>
```

For more details of the command syntax, including examples, see the OVFTool User’s Guide .

Configure the root and admin passwords using ssh on port 5022. Refer the section Set the Root and Admin Password Using SSH .

There are multiple ways to automate the deployment, for example, you can use Python Paramiko SSH library command:

| Step 1 | Select the host. |
|---|---|
| Step 2 | Go to the Configuration tab. |
| Step 3 | Select Time configuration . |
| Step 4 | Select Properties . If the date and time were red on the previous page, set the date and time manually to the current time. |
| Step 5 | Click Options . |
| Step 6 | Select NTP Settings . |
| Step 7 | Click Add . |
| Step 8 | Enter the IP address of the NTP server. |
| Step 9 | Click OK . |
| Step 10 | Select the Restart NTP service to apply changes check box. |
| Step 11 | Click OK . |
| Step 12 | Click OK . |

| Step 1 | If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments): Using a web browser, go to https:///folder supplying any required credentials (typically the same username and password as used to log into vCenter ). Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore. Right click on the .ova file and select Copy Link Location . (If the .ova file is not preloaded on the datastore, you can select and upload it in the following steps.) |
|---|---|
| Step 2 | Log in to vCenter to access the ESXi Host. |
| Step 3 | Select File > Deploy OVF Template. Figure 1. Deploy OVF Template |
| Step 4 | On the Source page, identify where the .ova file is located, and then click Next . If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that vCenter can access the web server. If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file. Figure 2. Browse .ova file |
| Step 5 | On the OVF Template Details page, check that the Publisher certificate is valid and click Next . |
| Step 6 | On the End User License Agreement page: Read the EULA. If you accept the EULA, click Accept then Next . |
| Step 7 | On the Name and Location page enter a Name for this Expressway VM guest, for example " Virtual_ Expressway " and click Next . Important When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. Figure 3. Name and Location | Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. |
| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. |
| Step 8 | On the Deployment Configuration page, select the appropriately sized deployment: Select Small , Medium or Large depending on the capabilities of the VMware host. The default is Medium. See System Requirements for details about resource requirements. If the VMware host has insufficient resources, the virtual Expressway will fail
                                                to power on / boot. Click Next . Figure 4. Select Deployment Size |
| Step 9 | On the Host / Cluster page, select where you want to run the virtual Expressway and click Next . Figure 5. Select Host or Cluster |
| Step 10 | On the Resource Pool page, select where you want to run the virtual Expressway and click Next . Figure 6. Select Resource Pool |
| Step 11 | On the Storage page, select the location onto which the virtual Expressway will be deployed and click Next . Figure 7. Select Destination Storage |
| Step 12 | On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next . Figure 8. Select Disk Format |
| Step 13 | On the Network Mapping page, select the network mapping that applies to your infrastructure (the default is VM Network ) and then click Next . Important In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. Figure 9. Select Network Mapping | Important | In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. |
| Important | In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. |
| Step 14 | On the Properties page, configure the network properties of the virtual Expressway and click Next . The properties you can set include the Expressway's IPv4 and IPv6 settings, option to enable DMI, and configure DMI Address
                                          and DMI Netmask, System, hostname and domain, up to five NTP servers, and up to five DNS servers. For automated deployments
                                          you can also enter an RSA SSH public key to securely set the root and admin passwords via SSH. If you do not enter a public
                                          key, you must set the passwords during the Install Wizard process. Important The hostname and domain name must contain only ASCII characters Figure 10. Configure Network Properties | Important | The hostname and domain name must contain only ASCII characters |
| Important | The hostname and domain name must contain only ASCII characters |
| Step 15 | On the Ready to Complete page: Confirm the deployment settings. Select the Power on after deployment check box. Click Finish . The installation process will begin and a progress bar will be displayed. |

| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. |
|---|---|

| Important | In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. |
|---|---|

| Important | The hostname and domain name must contain only ASCII characters |
|---|---|

| Note | You can ignore any floppy read errors that appear, as they are not relevant to this deployment mode. |
|---|---|

| Step 1 | Select the VM guest and then select the Console tab. You are taken to the Install Wizard. |
|---|---|
| Step 2 | Enter and confirm your root and admin passwords. You will also be prompted to set any properties you did not set in VMware. Note These passwords should be unique; do not use the same password for admin and root accounts. Figure 11. Enter Root and Admin Password | Note | These passwords should be unique; do not use the same password for admin and root accounts. |
| Note | These passwords should be unique; do not use the same password for admin and root accounts. |
| Step 3 | Press Enter to apply the configuration. |
| Step 4 | The Expressway will apply the configuration and reboot. Figure 12. Configuration Applied |

| Note | These passwords should be unique; do not use the same password for admin and root accounts. |
|---|---|

| Step 1 | The Install Wizard starts an SSH daemon, listening on port 5022, so you can set the root and admin password. |
|---|---|
| Step 2 | Connect as user "wizard" using an SSH client on port 5022 (for example: ssh wizard@10.0.0.1 -p 5022 ). Figure 13. Connect as User "wizard" |
| Step 3 | Follow the prompt to set admin.password and root.password . Figure 14. Set Admin and Root Password |
| Step 4 | The Expressway will apply the configuration and reboot. |

| Note | The desktop vSphere Client is not available from vSphere 6.5 and later. |
|---|---|

| Step 1 | If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments): Using a web browser, go to https://<VMwareHost>/folder supplying any required credentials (typically the same username and password as used to log into the vSphere client). Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore. Right click on the .ova file and select Copy Link Location . (If the .ova file is not preloaded on the datastore, you can select and upload it in the following steps.) |
|---|---|
| Step 2 | Log in to the vSphere client to access the ESXi Host. |
| Step 3 | Select File > Deploy OVF Template . Figure 16. Deploy OVF Template |
| Step 4 | On the Source page, identify where the .ova file is located, and then click Next . If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that the vSphere client can access the web server. If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file. Figure 17. Browse .ova File |
| Step 5 | On the OVF Template Details page, check that the Publisher certificate is valid and click Next . |
| Step 6 | On the End User License Agreement page: Read the EULA If you accept the EULA, click Accept then Next . |
| Step 7 | On the Name and Location page enter a Name for this Expressway VM guest, for example "Virtual_Expressway" and click Next . Important When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base Figure 18. Name and Location | Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base |
| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base |
| Step 8 | On the Deployment Configuration page, select the appropriately sized deployment: Select Small , Medium or Large depending on the capabilities of the VMware host. The default is Medium . See System Requirements for details about resource requirements. If theVMware host has insufficient resources, the virtual Expressway will fail to
                                                power on / boot. Click Next . Figure 19. Deployment Configuration |
| Step 9 | On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next . Thin Provision is not supported as VM performance may degrade during resizing of a partition. Figure 20. Disk Format |
| Step 10 | On the Ready to Complete page: Confirm the deployment settings. Select the Power on after deployment check box. Click Finish . The installation process will begin and a progress bar will be displayed. |

| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base |
|---|---|

| Note | If you encounter issues or enter incorrect information during the wizard you can press Ctrl+D to restart. The pre-X8.9 default passwords of the admin and root accounts are well known. You must use strong passwords for these accounts.
                                                If your new system is on X8.9 or later, you must supply non-default passwords. The pre-X8.9 default passwords of the admin and root accounts are well known. You must use strong passwords for these accounts.
                                                If your new system is on X8.9 or later, you must supply non-default passwords. The default timezone is UTC but you can search for your desired timezone. You can also change it later in the web interface
                                                by going to System > Time . The default values support tab completion. |
|---|---|

| Step 1 | Select the VM guest and then select the Console tab. The VM guest will take some time to boot, create its second hard disk partition and then reboot to the Install Wizard. |
|---|---|
| Step 2 | Follow the prompts given by the Install Wizard to specify the following: Whether you want to use IPv4, IPv6 or Both. The LAN 1 IPv4 subnet mask of the Expressway (if you have selected IPv4). The IP address of the default gateway of the Expressway. The root password. Should be unique, do not use the same password as for admin account. The admin password. Should be unique, do not use the same password as for root account. Whether you want to enable the web UI. Whether you want to use SSH to administer the Expressway. The timezone. |
| Step 3 | After the wizard is finished the following message will appear: Installation wizard complete Press Enter to continue the boot and apply the configuration. Press Enter . |
| Step 4 | After it has applied the configuration and rebooted, the Expressway is ready to use. You should now be able to access the
                                       Expressway using a web browser. |

| Step 1 | Deploy the VM using VMWare’s OVFTool: Ovftool –acceptAllEulas -ds=<vsphere datastore> --powerOn –noSSLVerify 
--name=<name of VM> --prop:ip4.address=<ip address> --prop:ip4.gateway=<gateway> 
--prop:ip4.netmask=<subnet mask> --prop.dmi.enable=<enable> 
--prop.dmi.ip4.address=<dmi ipv4 address> --prop.dmi.ip4.netmask=<dmi ipv4 netmask> 
--prop.dmi.ip6.address=<dmi ipv6 address> --prop:default.dns=1.1.1.1 -nw=<vsphere network> 
--X:waitForIp --prop:ssh.public.key=’<public ssh key>’ <OVA file> For more details of the command syntax, including examples, see the OVFTool User’s Guide . |
|---|---|
| Step 2 | Configure the root and admin passwords using ssh on port 5022. Refer the section Set the Root and Admin Password Using SSH . |
| Step 3 | There are multiple ways to automate the deployment, for example, you can use Python Paramiko SSH library command: {{command = '{"admin.password": "x", "root.password": “x”}\n’}} |