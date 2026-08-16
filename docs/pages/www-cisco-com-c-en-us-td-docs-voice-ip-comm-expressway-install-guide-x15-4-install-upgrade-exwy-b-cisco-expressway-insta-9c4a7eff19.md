---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-4-install-upgrade-exwy-b-cisco-expressway-insta-9c4a7eff19
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-4/install-upgrade/exwy_b_cisco-expressway-install-and-upgrade-guide-x154/exwy_m_vmware-vsphere-esxi.html
retrieved_at: 2026-08-16T22:07:03.782406+00:00
---

Cisco Expressway Install and Upgrade Guide (X15.4)

# Cisco Expressway Install and Upgrade Guide (X15.4)

Updated: April 3, 2026

Chapter: VMware vSphere ESXi

## Chapter: VMware vSphere ESXi

# VMware vSphere ESXi

## Installing the Expressway VM using vCenter or vSphere Client

### Installation Process

This process guides you through installing Expressway VM using vCenter or vSphere client. Before you start the installation,
                              make sure all the system requirements are in place, as detailed in the chapter, System Requirements .

### Configuring the VM Host

#### Before you begin

Ensure that the VM host is configured with a valid NTP server – the same NTP server that will be specified in Expressway.

Step 1

Select the host.

Step 2

Go to the Configuration tab.

Step 3

Select Time configuration .

Step 4

Select Properties .

If the date and time were red on the previous page, set the date and time manually to the current time.

Step 5

Click Options .

Step 6

Select NTP Settings .

Step 7

Click Add .

Step 8

Enter the IP address of the NTP server.

Step 9

Click OK .

Step 10

Select the Restart NTP service to apply changes check box.

Step 11

Click OK .

Step 12

Click OK .

#### What to do next

The following section describes how to deploy the ova to host using vCenter. If you are using vSphere, skip this section and
                                 go to Deploying OVA to Standalone ESXi Host .

## Deploying OVA to Host Managed by vCenter

These instructions represent a typical installation. The Deploy OVF Template wizard dynamically changes to reflect host configuration.

Step 1

If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments):

Using a web browser, go to https:///folder supplying any required credentials (typically the same username and password as used to log into vCenter).

Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore.

Right click on the .ova file and select Copy Link Location .

(If the .ova file is not preloaded onto the datastore, you can select and upload it in the following steps.)

Step 2

Log in to vCenter to access the ESXi Host.

Step 3

Select File > Deploy OVF Template.

Step 4

On the Source page, identify where the .ova file is located, and then click Next .

If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that vCenter can access the web server.

If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file.

Step 5

On the OVF Template Details page, check that the Publisher certificate is valid and click Next .

Step 6

On the End User License Agreement page:

Read the EULA.

If you accept the EULA, click Accept . Click Next .

Step 7

On the Name and Location page enter a Name for this Expressway VM guest, for example " Virtual_ Expressway " and click Next .

Important

When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base.

Step 8

On the Deployment Configuration page, select the appropriately sized deployment:

Select Small , Medium or Large depending on the capabilities of the VMware host.

The default is Medium. See System Requirements for details about resource requirements. If the VMware host has insufficient resources, the virtual Expressway will fail
                                                to power on / boot.

Click Next .

Step 9

On the Host / Cluster page, select where you want to run the virtual Expressway and click Next .

Step 10

On the Resource Pool page, select where you want to run the virtual Expressway and click Next .

Step 11

On the Storage page, select the location onto which the virtual Expressway will be deployed and click Next .

Step 12

On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next .

Step 13

On the Network Mapping page, select the network mapping that applies to your infrastructure (the default is VM Network ) and then click Next .

Important

In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters.

Step 14

On the Properties page, configure the network properties of the virtual Expressway and click Next .

The properties you can set include Expressway's IPv4 and IPv6 settings, the timezone, hostname and domain, up to five NTP
                                          servers, and up to five DNS servers. For automated deployments you can also enter an RSA SSH public key to securely set the
                                          root and admin passwords via SSH. If you do not enter a public key, you must set the passwords during the Install Wizard process.

Important

The hostname and domain name must contain only ASCII characters.

Step 15

On the Ready to Complete page:

Confirm the deployment settings.

Select the Power on after deployment check box.

Click Finish .

The installation process will begin, and a progress bar will be displayed.

The Expressway OVA is now deployed as a Guest on the VM Host.

## Configuring the VM Guest to Standalone ESXi Host

If you encounter issues or enter incorrect information during the wizard you can press Ctrl+D to restart.

The pre-X8.9 default passwords of the admin and root accounts are well known. You must use strong passwords for these accounts.
                                                If your new system is on X8.9 or later, you must supply non-default passwords.

The pre-X8.9 default passwords of the admin and root accounts are well known. You must use strong passwords for these accounts.
                                                If your new system is on X8.9 or later, you must supply non-default passwords.

The default timezone is UTC but you can search for your desired timezone. You can also change it later in the web interface
                                                by going to System > Time .

The default values support tab completion.

Step 1

Select the VM guest and then select the Console tab.

The VM guest will take some time to boot, create its second hard disk partition and then reboot to the Install Wizard.

Step 2

Follow the prompts given by the Install Wizard to specify the following:

Whether you want to use IPv4, IPv6 or Both.

The LAN 1 IPv4 subnet mask of the Expressway (if you have selected IPv4).

The IP address of the default gateway of the Expressway.

The root password. Should be unique, do not use the same password as for admin account.

The admin password. Should be unique, do not use the same password as for root account.

Whether you want to enable the web UI.

Whether you want to use SSH to administer the Expressway.

The timezone.

Step 3

After the wizard is finished the following message will appear:

Installation wizard complete

Press Enter to continue the boot and apply the configuration.

Press Enter .

Step 4

After it has applied the configuration and rebooted, the Expressway is ready to use. You should now be able to access the
                                       Expressway using a web browser.

### What to do next

You can now manage the Expressway licensing and basic configuration; see Expressway Service Selection, Licenses, and Basic Configuration .

## Deploying OVA to Standalone ESXi Host

### Before you begin

Important

When deploying an OVF template in vSphere, the IPv4 address fields are mandatory and must be populated even if the "Enable
                                          IPv4" option is not enabled.

Step 1

If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments):

Using a web browser, go to https://<VMwareHost>/folder supplying any required credentials (typically the same username and password as used to log into the vSphere client).

Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore.

Right click on the .ova file and select Copy Link Location .

(If the .ova file is not preloaded onto the datastore, you can select and upload it in the following steps.)

Step 2

Log in to the vSphere client to access the ESXi Host.

Step 3

Select File > Deploy OVF Template .

Step 4

On the Source page, identify where the .ova file is located, and then click Next .

If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that the vSphere client can access the web server.

- If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file. Figure 2. Browse .ova File

Step 5

On the OVF Template Details page, check that the Publisher certificate is valid and click Next .

Step 6

On the End User License Agreement page:

Read the EULA

If you accept the EULA, click Accept . Click Next .

Step 7

On the Name and Location page enter a Name for this Expressway VM guest, for example "Virtual_Expressway" and click Next .

Important

When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base

Step 8

On the Deployment Configuration page, select the appropriately sized deployment:

Select Small , Medium or Large depending on the capabilities of  the VMware host.

The default is Medium . See System Requirements for details about resource requirements. If the VMware host has insufficient resources, the virtual Expressway will fail
                                                to power on / boot.

Click Next .

Step 9

On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next .

Step 10

On the Ready to Complete page:

Confirm the deployment settings.

Select the Power on after deployment check box.

Click Finish .

The installation process will begin, and a progress bar will be displayed.

## Automating the Deployment Process

We recommend deploying an Expressway VMware OVA in an automated manner. To do this:

Step 1

Deploy the VM using VMware’s OVFTool:

```
Ovftool –acceptAllEulas -ds=<vsphere datastore> --powerOn –noSSLVerify 
--name=<name of VM> --prop:ip4.address=<ip address> --prop:ip4.gateway=<gateway> 
--prop:ip4.netmask=<subnet mask> --prop.dmi.enable=<enable> 
--prop.dmi.ip4.address=<dmi ipv4 address> --prop.dmi.ip4.netmask=<dmi ipv4 netmask> 
--prop.dmi.ip6.address=<dmi ipv6 address> --prop:default.dns=1.1.1.1 -nw=<vsphere network> 
--X:waitForIp --prop:ssh.public.key=’<public ssh key>’ <OVA file>
```

For more details of the command syntax, including examples, see the OVFTool User’s Guide .

Step 2

Configure the root and admin passwords using ssh on port 5022 or port 22. See the section Set the Root and Admin Password Using SSH .

This property --prop:ssh.use.standard.port=True can be used to install wizard to listen on port 22. Otherwise, the install wizard listens on port 5022.

Step 3

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

| Step 1 | If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments): Using a web browser, go to https:///folder supplying any required credentials (typically the same username and password as used to log into vCenter). Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore. Right click on the .ova file and select Copy Link Location . (If the .ova file is not preloaded onto the datastore, you can select and upload it in the following steps.) |
|---|---|
| Step 2 | Log in to vCenter to access the ESXi Host. |
| Step 3 | Select File > Deploy OVF Template. |
| Step 4 | On the Source page, identify where the .ova file is located, and then click Next . If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that vCenter can access the web server. If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file. |
| Step 5 | On the OVF Template Details page, check that the Publisher certificate is valid and click Next . |
| Step 6 | On the End User License Agreement page: Read the EULA. If you accept the EULA, click Accept . Click Next . |
| Step 7 | On the Name and Location page enter a Name for this Expressway VM guest, for example " Virtual_ Expressway " and click Next . Important When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. | Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. |
| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. |
| Step 8 | On the Deployment Configuration page, select the appropriately sized deployment: Select Small , Medium or Large depending on the capabilities of the VMware host. The default is Medium. See System Requirements for details about resource requirements. If the VMware host has insufficient resources, the virtual Expressway will fail
                                                to power on / boot. Click Next . |
| Step 9 | On the Host / Cluster page, select where you want to run the virtual Expressway and click Next . |
| Step 10 | On the Resource Pool page, select where you want to run the virtual Expressway and click Next . |
| Step 11 | On the Storage page, select the location onto which the virtual Expressway will be deployed and click Next . |
| Step 12 | On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next . |
| Step 13 | On the Network Mapping page, select the network mapping that applies to your infrastructure (the default is VM Network ) and then click Next . Important In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. | Important | In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. |
| Important | In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. |
| Step 14 | On the Properties page, configure the network properties of the virtual Expressway and click Next . The properties you can set include Expressway's IPv4 and IPv6 settings, the timezone, hostname and domain, up to five NTP
                                          servers, and up to five DNS servers. For automated deployments you can also enter an RSA SSH public key to securely set the
                                          root and admin passwords via SSH. If you do not enter a public key, you must set the passwords during the Install Wizard process. Important The hostname and domain name must contain only ASCII characters. | Important | The hostname and domain name must contain only ASCII characters. |
| Important | The hostname and domain name must contain only ASCII characters. |
| Step 15 | On the Ready to Complete page: Confirm the deployment settings. Select the Power on after deployment check box. Click Finish . The installation process will begin, and a progress bar will be displayed. |

| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base. |
|---|---|

| Important | In Expressway versions 12.5.3 and earlier, the network name must contain only ASCII characters. From 12.5.4 release, network
                                                      name can also contain non-ASCII characters. |
|---|---|

| Important | The hostname and domain name must contain only ASCII characters. |
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

| Note | The desktop vSphere Client is not available from vSphere 6.5 and later. |
|---|---|

| Important | When deploying an OVF template in vSphere, the IPv4 address fields are mandatory and must be populated even if the "Enable
                                          IPv4" option is not enabled. |
|---|---|

| Step 1 | If the .ova file is already preloaded onto the ESXi Host datastore (for example, in Cisco Business Edition 6000 deployments): Using a web browser, go to https://<VMwareHost>/folder supplying any required credentials (typically the same username and password as used to log into the vSphere client). Navigate through the index of datacenters to find the .ova file you want to deploy from the datastore. Right click on the .ova file and select Copy Link Location . (If the .ova file is not preloaded onto the datastore, you can select and upload it in the following steps.) |
|---|---|
| Step 2 | Log in to the vSphere client to access the ESXi Host. |
| Step 3 | Select File > Deploy OVF Template . Figure 1. Deploy OVF Template |
| Step 4 | On the Source page, identify where the .ova file is located, and then click Next . If the .ova file is already preloaded onto the ESXi Host datastore, paste the URL you copied from step 1 above. You may have
                                             to re-enter username and password credentials so that the vSphere client can access the web server. If the .ova file is not preloaded on the datastore, Browse to the location of the .ova file. Figure 2. Browse .ova File |
| Step 5 | On the OVF Template Details page, check that the Publisher certificate is valid and click Next . |
| Step 6 | On the End User License Agreement page: Read the EULA If you accept the EULA, click Accept . Click Next . |
| Step 7 | On the Name and Location page enter a Name for this Expressway VM guest, for example "Virtual_Expressway" and click Next . Important When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base Figure 3. Name and Location | Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base |
| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base |
| Step 8 | On the Deployment Configuration page, select the appropriately sized deployment: Select Small , Medium or Large depending on the capabilities of  the VMware host. The default is Medium . See System Requirements for details about resource requirements. If the VMware host has insufficient resources, the virtual Expressway will fail
                                                to power on / boot. Click Next . Figure 4. Deployment Configuration |
| Step 9 | On the Disk Format page, ensure that the default disk format of Thick Provision Lazy Zeroed is selected and then click Next . Thin Provision is not supported as VM performance may degrade during resizing of a partition. Figure 5. Disk Format |
| Step 10 | On the Ready to Complete page: Confirm the deployment settings. Select the Power on after deployment check box. Click Finish . The installation process will begin, and a progress bar will be displayed. |

| Important | When deploying a VM to ESXi version 6.0 or later, you must not use a backslash or forward slash in the VM name as the characters
                                                      are unsupported and it can cause errors during the deployment. You must remove the slash from the default name of Cisco Expressway/VCS
                                                      Base |
|---|---|

| Step 1 | Deploy the VM using VMware’s OVFTool: Ovftool –acceptAllEulas -ds=<vsphere datastore> --powerOn –noSSLVerify 
--name=<name of VM> --prop:ip4.address=<ip address> --prop:ip4.gateway=<gateway> 
--prop:ip4.netmask=<subnet mask> --prop.dmi.enable=<enable> 
--prop.dmi.ip4.address=<dmi ipv4 address> --prop.dmi.ip4.netmask=<dmi ipv4 netmask> 
--prop.dmi.ip6.address=<dmi ipv6 address> --prop:default.dns=1.1.1.1 -nw=<vsphere network> 
--X:waitForIp --prop:ssh.public.key=’<public ssh key>’ <OVA file> For more details of the command syntax, including examples, see the OVFTool User’s Guide . |
|---|---|
| Step 2 | Configure the root and admin passwords using ssh on port 5022 or port 22. See the section Set the Root and Admin Password Using SSH . Note This property --prop:ssh.use.standard.port=True can be used to install wizard to listen on port 22. Otherwise, the install wizard listens on port 5022. | Note | This property --prop:ssh.use.standard.port=True can be used to install wizard to listen on port 22. Otherwise, the install wizard listens on port 5022. |
| Note | This property --prop:ssh.use.standard.port=True can be used to install wizard to listen on port 22. Otherwise, the install wizard listens on port 5022. |
| Step 3 | There are multiple ways to automate the deployment, for example, you can use Python Paramiko SSH library command: {{command = '{"admin.password": "x", "root.password": “x”}\n’}} |

| Note | This property --prop:ssh.use.standard.port=True can be used to install wizard to listen on port 22. Otherwise, the install wizard listens on port 5022. |
|---|---|