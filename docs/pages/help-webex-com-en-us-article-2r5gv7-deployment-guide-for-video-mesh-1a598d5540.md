---
doc_id: help-webex-com-en-us-article-2r5gv7-deployment-guide-for-video-mesh-1a598d5540
source_url: https://help.webex.com/en-us/article/2r5gv7/Deployment-Guide-for-Video-Mesh
retrieved_at: 2026-11-02T12:57:18.361830+00:00
---

### Video Mesh Deployment Task Flow

Before you begin

Prepare your environment

Choose a supported virtualization platform for your Video Mesh node and complete its prerequisites:

- VMware ESXi 7 or 8, managed through vSphere or vCenter

- Cisco NFVIS 26.2.1

- Nutanix AOS 7.5.x with Nutanix AHV 11.0.x managed through Prism Central.

Install and Configure Video Mesh Node Software

Use the procedure for your supported hypervisor to deploy a Video Mesh Node. You install the software on-premises which creates a node and then perform initial configuration, such as network settings. You'll register it to the cloud later.

Log in to the Video Mesh Node Console

Sign in to the console for the first time. The Video Mesh Node software has a default password. You need to change this value before you configure the node.

Set the Network Configuration of the Video Mesh Node in the Console

Use this procedure to configure the network settings for the Video Mesh Node if you didn't configure them when you set up the node on a virtual machine. You'll set a static IP address and change the FQDN/hostname and NTP servers. DHCP is not currently supported.

Use these steps to configure the external interface for a dual network interface (dual NIC) deployment:

- Set The External Network Interface of the Video Mesh Node

- Add Internal and External Routing Rules

After the node is back online and you verified the internal network configuration, you can configure the external network interface if you're deploying the Video Mesh Node in your network's DMZ so that you can isolate the enterprise (internal) traffic from the outside (external) traffic.

You can also make exceptions or overrides to the default routing rules.

Register the Video Mesh Node to the Webex Cloud

Use this procedure to register Video Mesh nodes to the Webex cloud and complete additional configuration. When you use Control Hub to register your node, you create a cluster to which the node is assigned. A cluster contains one or more media nodes that serve users in a specific geographic region. The registration steps also configure SIP call settings, set an upgrade schedule, and subscribe to email notifications.

Enable and verify Quality of Service (QoS) with the following tasks:

- Enable Quality of Service (QoS) for Video Mesh Node

- Verify Video Mesh Node Port Ranges With Reflector Tool in the Web Interface

Enable QoS if you want Video Mesh nodes to automatically mark SIP traffic (on-premises SIP registered endpoints) for both audio (EF) and video (AF41) separately with appropriate class of service and use well-known port ranges for specific media types. This change will let you create QoS policies and effectively remark return traffic from the cloud if desired.

Use the Reflector Tool steps to verify the correct ports are opened on your firewall.

Configure Video Mesh Node for Proxy Integration

Use this procedure to specify the type of proxy that you want to integrate with a Video Mesh. If you choose a transparent inspecting proxy, you can use the node's interface to upload and install the root certificate, check the proxy, and troubleshoot any potential issues.

Follow Integrate Video Mesh With Call Control Task Flow and choose one of the following, depending on your call control, security requirements, and whether you want to integrate Video Mesh with your call control environment:

- Configure Unified CM Secure TLS SIP Traffic Routing for Video Mesh (TLS)

- Configure Unified CM TCP SIP Traffic Routing for Video Mesh (TCP)

- Configure Expressway TCP SIP Traffic Routing for Video Mesh (TCP)

SIP devices don't support direct reachability, so you must use Unified CM or VCS Expressway configuration to establish a relationship between on-premises registered SIP devices and your Video Meshclusters.

You only need to trunk your Unified CM or VCS Expressway to Video Mesh Node, depending on your call control environment.

Exchange Certificate Chains Between Unified CM and Video Mesh Nodes

In this task, you download certificates from the Unified CM and Video Mesh interfaces and upload one to the other. This step establishes secure trust between the two products and, in conjunction with the secure trunk configuration, allows encrypted SIP traffic and SRTP media in your organization to land on Video Mesh nodes.

Enable Media Encryption for the Organization and Video Mesh Clusters

Use this procedure to turn on media encryption for your organization and individual Video Mesh clusters. This setting forces end-to-end TLS setup and you must have a secure TLS SIP trunk in place on your Unified CM that points to your Video Mesh nodes.

Enable Video Mesh for the Webex Site

To use optimized media to the Video Mesh Node for a Webex meeting to all the Webex app and devices to join, this configuration needs to be enabled for the Webex site. Enabling this setting links Video Mesh and meeting instances in the cloud together and allows cascades to occur from Video Mesh nodes. If this setting is not enabled, the Webex app and devices will not use the Video Mesh node for Webex meetings.

Assign Collaboration Meeting Rooms to Webex App Users

Verify the meeting experience on the secure endpoint

If you are using media encryption through the end-to-end TLS setup, use these steps to verify that the endpoints are securely registered and the correct meeting experience appears.

### Bulk Provisioning Script for Video Mesh

If you need to deploy many nodes in your Video Mesh deployment, the process is time-consuming. You can use the script at https://github.com/CiscoDevNet/webex-video-mesh-node-provisioning to deploy Video mesh nodes on VMWare ESXi servers quickly. Read through the readme file for instructions on using the script.

This procedure applies only to VMware deployments.

### Install and Configure Video Mesh Node Software

Use the procedure for your supported hypervisor to deploy a Video Mesh Node. You install the software on-premises which creates a node and then perform initial configuration, such as network settings. You'll register it to the cloud later.

Install and Configure Video Mesh on VMware

You must download the software package (OVA) from Control Hub ( https://admin.webex.com ), rather than using a previously downloaded version. This OVA is signed by Cisco certificates and can be downloaded after you sign in to Control Hub with your customer administrator credentials.

Before you begin

See System and Platform Requirements for Video Mesh Node Software for supported hardware platforms and specifications requirements for the Video Mesh Node.

Make sure you have these required items:

A computer with:

VMware vSphere client 7 or 8.

For a list of supported operating systems, refer to VMware documentation.

Video Mesh software OVA file downloaded.

Download the latest Video Mesh software from Control Hub, rather than using a previously downloaded version. You can also access the software from this link . (The file is approximately 1.5 GB.)

Older versions of the software package (OVA) will not be compatible with the latest Video Mesh upgrades. This can result in issues while upgrading the application. Make sure you download the latest version of the OVA file from this link .

A supported server with VMware ESXi or vCenter 7 or 8 installed and running

Disable virtual machine backups and live migration. Video Mesh Node clusters are realtime systems; any virtual machine pauses can make these systems unstable. (For maintenance activities on a Video Mesh Node, use maintenance mode from Control Hub.)

Using your computer, open the VMware vSphere client and sign in to the vCenter or ESXi system on the server.

Go to Actions > Deploy OVF Template .

On the Select an OVF tempate page, click Local File , then Choose Files . Navigate to where the videomesh.ova file is located, choose the file, and then click Next .

Each time you do a Video Mesh Node installation, we recommend that you redownload the OVA rather than using a previously downloaded version. If you try to deploy an old OVA, your Video Mesh Node may not work properly nor register to the cloud. An old OVA will also lead to potential issues during upgrades.

Make sure you download a new copy of the OVA from this link .

On the Select a name and folder page, enter a Virtual machine name for the Video Mesh Node (for example, "Video_Mesh_Node_1"), choose a location where the virtual machine node deployment can reside, and then click Next .

A validation check runs. After it finishes, the template details appear.

Verify the template details and then click Next .

On the Configuration page, choose the type of deployment configuration, and then click Next .

- VMNLite (default)

- VMNFull

The options are listed in the order of increasing resource requirements.

If you choose the VMNLite option, you'll need to repeat the steps to deploy the other instance(s) on the same host, and choose the same option each time. Co-residency of VMNLite and non-VMNLite instances has not been tested and is not supported.

On the Select storage page, ensure that the default disk format of Thick Provision Lazy Zeroed and VM storage policy of Datastore Default are selected and then click Next .

On the Select networks page, choose the network option from the list of entries to provide the desired connectivity to the VM.

- For Internal Interface  Network , choose the node's internal IP address.

- For External InterfaceNetwork , choose the external IP address that faces the public network. Ignore this option if you don't have a dual NIC deployment.

The inside interface (the default interface for traffic) is used for CLI, SIP trunks, SIP traffic and node management. The outside (external) interface is for HTTPS and websockets communication to the Webex cloud, along with the cascades traffic from the nodes to a meeting.

For a DMZ deployment, you can set up the Video Mesh node with the dual network interface (NIC). This deployment lets you separate the internal enterprise network traffic (used for interbox communication, cascades between nodes in a cluster, and to access the node's management interface) from the external cloud network traffic (used for connectivity to the outside world, Inter-Cluster cascades, and cascades to Webex). All nodes in a cluster must be in dual NIC mode; a mixture of single and dual NIC is not supported.

For an existing installation of Video Mesh Node software, you cannot upgrade from a single NIC to a dual NIC configuration. You must do a fresh install of Video Mesh Node in this case.

On the Customize template page, configure the following network settings:

To ensure a successful registration to the cloud, use only lowercase characters in the FQDN or hostname that you set for the Video Mesh Node. Capitalization is not supported at this time.

When using or configuring FQDN or hostname, you must also enter a valid and resolvable domain. The total length of the FQDN must not exceed 64 characters.

- IP Address — Enter the IP address for the internal interface of the node.

- Mask —Enter the subnet mask address in dot-decimal notation. For example, 255.255.255.0 .

- Gateway —Enter the gateway IP address. A gateway is a network node that serves as an access point to another network.

- DNS Servers —Enter a comma-separated list of DNS servers, which handle translating domain names to numeric IP addresses. (Up to 4 DNS entries are allowed.)

- NTP Servers —Enter your organization's NTP server or another external NTP server that can be used in your organization. You can also use a comma-separated list to enter multiple NTP servers.

The Video Mesh Node must have an internal IP address and resolvable DNS name. The node IP address must not belong to the IP address range reserved for Video Mesh Node internal use. The default reserved IP address range is 172.17.42.0–172.17.42.63, which can be configured later in the Diagnostic menu. This IP address range is for communication within the Video Mesh Node and between the software containers which hold the different components of the node—for example, SIP interface and media transcoding.

Deploy all the nodes on the same subnet or VLAN, so that all nodes in a cluster are reachable from wherever the clients reside in your network.

For a dual NIC DMZ deployment, you can set the external IP address in the node console, after you've saved the internal network configuration and rebooted the node later.

If preferred, you can skip the network setting configuration and follow the steps in Set the Network Configuration of the Video Mesh Node in the Console after you sign into the node.

On the Ready to Complete page, verify that all the settings that you entered match the guidelines in this procedure, and then click Finish .

After deployment of the OVA is complete, your Video Mesh Node appears in the list of VMs.

Right-click the Video Mesh Node VM, and then choose Power > Power On .

The Video Mesh Node software is installed as a guest on the VM Host. You are now ready to sign in to the console and configure the Video Mesh Node.

You may experience a delay of a few minutes before the node containers come up. A bridge firewall message appears on the console during first boot, during which you can't sign in.

What to do next

Log in to the Video Mesh Node Console

Install and configure Video Mesh on Cisco NFVIS

Use this procedure to upload the Video Mesh OVA to Cisco NFVIS and deploy a Video Mesh Node VM. After the VM starts, use the console, network configuration, and cloud registration procedures that follow this section.

Before you begin

See System and Platform Requirements for Video Mesh Node Software for supported hardware platforms and specifications requirements for the Video Mesh Node.

Make sure you have these required items:

A computer with:

- A web browser and network access to the Cisco NFVIS portal. Google Chrome is recommended.

Video Mesh software OVA file downloaded.

Download the latest Video Mesh software from Control Hub, rather than using a previously downloaded version. You can also access the software from this link . (The file is approximately 1.5 GB.)

Older versions of the software package (OVA) will not be compatible with the latest Video Mesh upgrades. This can result in issues while upgrading the application. Make sure you download the latest version of the OVA file from this link .

A supported server with Cisco NFVIS 26.2.1 installed and running, and sufficient resources.

- The NFVIS network for the node’s internal interface.

- The node’s IP address, subnet mask, and gateway.

- DNS and NTP server addresses.

- A lowercase hostname or FQDN that resolves through DNS.

Disable virtual machine backups and live migration. Video Mesh Node clusters are realtime systems; any virtual machine pauses can make these systems unstable. (For maintenance activities on a Video Mesh Node, use maintenance mode from Control Hub.)

Sign in to the Cisco NFVIS portal . Go to Configuration > Virtual Machine > Images > Image Repository .

Choose LOCAL , select the Video Mesh OVA file, and select the destination datastore. Verify the Image Name , set VM Workload Type to Calling and VM Type to ECP/VIDEO MESH , then select Upload File .

Wait for the image to reach ACTIVE in the Image Repository. Confirm that NFVIS created a profile for the uploaded image. An image still in CREATE is not ready for deployment.

Go to Configuration > Deploy . Under Select VM , choose ECP/VIDEO MESH , then select the Video Mesh icon.

Use Network Interfaces to connect the VM to the NFVIS network selected for its internal interface. Select the connection line and, in vNIC Details , set:

- Model : Virtio

- Driver Name : vhost

- Driver Queues : 8

For a dual-NIC deployment, use Network Interfaces to connect a second vNIC to the NFVIS network designated for the node’s external interface. Select the new connection line and set Model to Virtio , Driver Name to vhost , and Driver Queues to 8 . Verify and record which vNIC ID connects to the internal network and which connects to the external network.

Configure the external static IP address later in Set The External Network Interface of the Video Mesh Node . Use the same single-NIC or dual-NIC configuration for every node in a cluster.

Select the Video Mesh icon again. In Deployment Details , enter a unique VM name and select the image uploaded in step 2 and its matching profile.

Select the deployment disk and verify that the profile and NFVIS resource settings provide the dedicated CPU, memory, and storage required for the planned Video Mesh node size.

Select Deploy . Wait for the successful deployment notification, then go to Configuration > Virtual Machine > Manage . Refresh the status until the VM is Active .

Select Terminal for the new VM. Allow the first boot to finish and wait for the Video Mesh login prompt.

For a production VMNLite deployment, repeat the VM deployment steps to deploy a second identical VMNLite VM on the NFVIS host.

After the Video Mesh login prompt appears, wait 2-3 minutes for the node to complete its startup and the console to stabilize before continuing.

What to do next

Install and configure Video Mesh on Nutanix

Use this procedure to upload the Video Mesh OVA to Nutanix Prism Central and deploy a Video Mesh Node virtual machine. After the VM starts, use the console, network configuration, and cloud registration procedures that follow this section.

Before you begin

See System and Platform Requirements for Video Mesh Node Software for supported Nutanix platform and specification requirements for the Video Mesh Node.

Make sure you have these required items:

- A web browser and network access to Prism Central. Google Chrome is recommended.

- Access to Nutanix Controller VM (CVM).

Video Mesh software OVA file downloaded.

Download the latest Video Mesh software from Control Hub, rather than using a previously downloaded version. You can also access the software from this link . (The file is approximately 1.5 GB.)

Older versions of the software package (OVA) will not be compatible with the latest Video Mesh upgrades. This can result in issues while upgrading the application. Make sure you download the latest version of the OVA file from this link .

- A target Nutanix cluster with sufficient dedicated CPU, memory, and storage for the selected Video Mesh Node configuration.

- The Nutanix subnet or VLAN for the node’s internal interface.

- The node’s IP address, subnet mask, and gateway.

- DNS and NTP server addresses.

- A lowercase hostname or FQDN that resolves through DNS.

Disable virtual machine backups and live migration. Video Mesh Node clusters are realtime systems; any virtual machine pauses can make these systems unstable. (For maintenance activities on a Video Mesh Node, use maintenance mode from Control Hub.)

Sign in to Prism Central and go to Infrastructure > Compute > OVAs .

Select Upload OVA . Choose the downloaded Video Mesh OVA and target cluster. Give the upload a unique name that includes its version or upload date, then complete the upload.

In the OVA list, confirm that the upload succeeded and Disk Format shows VMDK .

Select the uploaded OVA and choose Deploy as VM .

Enter a unique VM name and select the target cluster. Verify that the VM’s CPU and memory match the planned VMNFull or VMNLite profiles.

For VMNFull (default profile):

- 2 vCPUs (35 cores per vCPU) (2 × 35 = 70 virtual CPU cores)

- 60 GB main memory.

For VMNLite:

- 23 vCPUs (1 core per vCPU)

- 20 GB main memory.

Click Next . The Resources wizard opens.

In the Resources > Disks table, verify that the attached disk has a capacity of 80 GB for a VMNFull or standard VMNLite node, or 250 GB for a VMNLite recording node.

Attach the correct subnet or VLAN using the Attach to Subnet option and set the network connection state to Connected .

If the wizard contains an empty or default network entry displaying No network found for VM network , remove that entry. The invalid entry can prevent the wizard from continuing even after the correct subnet has been attached.

For a dual-NIC deployment, select Attach to Subnet again and attach a second network interface to the subnet or VLAN designated for the node’s external interface. Set its Network Connection State to Connected . Before creating the VM, verify that two interfaces are present and record which subnet is attached to each interface.

Configure the external static IP address later in Set The External Network Interface of the Video Mesh Node . Use the same single-NIC or dual-NIC configuration for every node in a cluster.

Select UEFI as the BIOS mode and click Next . The Management wizard opens.

Leave Categories blank unless categories are required by the organization.

Select the appropriate time zone.

Select No Customization on the Guest Customization card and click Next .

Review the settings and select Create VM .

Find the new VM’s NIC MAC address in Prism Central. Alternatively, sign in to a Nutanix Controller VM (CVM) and run:

acli vm.nic_get "<VM name>"

From the CVM command line, run this command once for each NIC , using its MAC address::

acli vm.nic_update "<VM name>" "<MAC address>" queues=8

Go to Infrastructure > Compute > VMs . Select the new VM and choose Summary > Power Operations > Power On .

Select Launch Console . Allow the first boot to finish and wait for the Video Mesh login prompt. After it appears, allow another 2–3 minutes for startup to settle before continuing.

For a production VMNLite deployment, repeat the VM deployment steps for all three identical instances required by the selected configuration.

What to do next

### Log in to the Video Mesh Node Console

Sign in to the console for the first time. The Video Mesh Node software has a default password. You need to change this value before you configure the node.

Open the Video Mesh Node console using the step for your hypervisor:

- VMware ESXi/vSphere: In the VMware vSphere client, go to the Video Mesh Node VM and choose Console .

- Cisco NFVIS: In the NFVIS portal, go to Configuration > Virtual Machine > Manage , locate the Video Mesh Node VM, and choose Terminal .

- Nutanix AHV: In Prism Central, go to VMs , select the Video Mesh Node VM, and choose Launch Console .

The Video Mesh Node VM boots up and a login prompt appears. If the login prompt does not appear, press Enter . You may briefly see a message that indicates the system is being initialized.

Use the following default username and password to log in:

Login: admin

Password: ciscosystems

Because you are logging in to the Video Mesh Node for the first time, you must change the administrator passphrase (password).

For (current) password, enter the default password (from above),  and then press Enter .

For new password, enter a new passphrase, and then press Enter .

For retype new password, retype the new passphrase, and then press Enter .

A "Password successfully changed" message appears, and then the initial Video Mesh Node screen appears with a message about unauthorized access being prohibited.

Press Enter to load the main menu.

What to do next

Set the Network Configuration of the Video Mesh Node in the Console

### Set the Network Configuration of the Video Mesh Node in the Console

Use this procedure to configure the network settings for the Video Mesh Node if you didn't configure them when you set up the node on a virtual machine. You'll set a static IP address and change the FQDN/hostname and NTP servers. DHCP is not currently supported.

These steps are required if you didn't configure network settings at the time of OVA deployment.

The inside interface (the default interface for traffic) is used for CLI, SIP trunks, SIP traffic and node management. The outside (external) interface is for HTTPS and websockets communication to Webex, along with the cascades traffic from the nodes to Webex.

Open the node console interface using the step for your hypervisor, then sign in with the admin credentials:

- VMware ESXi/vSphere: In the VMware vSphere client, go to the Video Mesh Node VM and choose Console .

- Cisco NFVIS: In the NFVIS portal, go to Configuration > Virtual Machine > Manage , locate the Video Mesh Node VM, and select Terminal .

- Nutanix AHV: In Prism Central, go to VMs , select the Video Mesh Node VM, and choose Launch Console .

From the main menu of the Video Mesh Node console, choose option 2 Edit Configuration and then click Select .

Read the prompt that the calls will end on the Video Mesh Node, and then click Yes .

Click Static , enter the IP address for the internal interface, Mask , Gateway , and DNS values for your network.

The Video Mesh Node must have an internal IP address and resolvable DNS name. The node IP address must not belong to the IP address range reserved for Video Mesh Node internal use. The default reserved IP address range is 172.17.42.0–172.17.42.63, which can be configured in the Diagnostic menu. This IP address range is for communication within the Video Mesh Node and between the software containers which hold the different components of the node—for example, SIP interface and media transcoding.

Deploy all the nodes on the same subnet or VLAN, so that all nodes in a cluster are reachable from wherever the clients reside in your network.

For a dual NIC DMZ deployment, you can set the external IP address in the next procedure, after you've saved the internal network configuration and rebooted the node.

Enter your organization's NTP server or another external NTP server that can be used in your organization.

After you configure the NTP server and save network settings, you can follow the steps in Check Health of Video Mesh Node From Console to verify that the time is synchronizing correctly through the specified NTP servers.

If you configure more than one NTP servers, the poll interval for failover is 40 seconds.

(Optional) Change the hostname or domain, if required.

To ensure a successful registration to the cloud, use only lowercase characters in the hostname that you set for the Video Mesh Node. Capitalization is not supported at this time.

When using or configuring FQDN or hostname, you must also enter a valid and resolvable domain. The total length of the FQDN must not exceed 64 characters.

Click Save , and then click Save Changes & Reboot .

During the save, DNS validation is performed if you provided a domain. A warning is displayed if the FQDN (hostname and domain) is not resolvable using the DNS server addresses provided. You may choose to save by ignoring the Warning, but calls will not work until the FQDN can resolve to the DNS configured on the node. After the Video Mesh Node reboots, the network configuration changes take effect.

What to do next

Once the software image is installed and configured with the network settings (IP Address, DNS, NTP, and so on) and accessible on the enterprise network, you can move to the next step of securely registering it to the cloud. The IP address that is configured on the Video Mesh Node is accessible only from the enterprise network. From a security perspective, the node is hardened whereby only customer administrators can access the node interface to perform configuration.

Set The External Network Interface of the Video Mesh Node

### Set The External Network Interface of the Video Mesh Node

After the node is back online and you verified the internal network configuration, you can configure the external network interface if you're deploying the Video Mesh Node in your network's DMZ so that you can isolate the enterprise (internal) traffic from the outside (external) traffic.

From the main menu of the Video Mesh Node console, choose option 5 External IP Configuration and then click Select .

Click 1 Enable/Disable , then Select , and then Yes to enable the external IP address options on the node.

As you did with the initial network configuration, enter the IP Address (external), Mask , and Gateway values.

The Interface field shows the name of the external interface for the node.

Click Save and Restart .

The node once again reboots to enable the dual IP address, and then automatically configures the basic static routing rules. These rules determine that traffic to and from a private class IP address uses an internal interface; traffic to and from a public class IP address uses an external interface. Later, you can create your own routing rules—For example, if you need to configure an override and allow access to an external domain from the internal interface.

Under certain circumstances, the existing SSH connection may terminate. For organizations that use IP addresses from the public range , you must reestablish an SSH connection to the public IP address of the Video Mesh Node.

To validate the internal and external IP address configuration, from the main menu of the console, go to 4 Diagnostics , and then choose Ping .

In the ping field, enter a destination address that you want to test, such as an external destination or an internal IP address, and then click OK .

- Test an external destination (example, cisco.com); if successful, the results show that the destination was accessed from the external interface.

- Test an internal IP address; if successful, the results show that the address was accessed from the internal interface.

What to do next

Register the Video Mesh Node to the Webex Cloud

### Video Mesh Node APIs

Video Mesh Node APIs enable organization admins to manage password, internal & external network settings, maintenance mode and server certificates related to Video Mesh Nodes. These APIs can be invoked via any API tool like Postman, or you can create your own script to call them. The user needs to call the APIs using the appropriate endpoint (you can use either node IP or FQDN), method, body, headers, authorization, etc. to perform the desired action and get a suitable response, as per the information provided below.

VMN Administration APIs

Video Mesh Administration APIs enable organization admins to manage maintenance mode and admin account password of the Video Mesh Nodes.

##### Get the Maintenance Mode status

Retrieves the current maintenance mode status (Expected status: on, off, pending or requested).

[GET] https://<node_ip>/api/v1/external/maintenanceMode

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Success"
    },
    "result": {
        "isRegistered": true,
        "maintenanceMode": "pending/requested/on/off",
        "maintenanceModeLastUpdated": 1691135731847
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 401,
        "message": "login failed: incorrect password or username"
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 429,
        "message": "Too Many Requests"
    }
}
```

##### Enable or Disable Maintenance Mode

When you place a Video Mesh node into maintenance mode, it does a graceful shutdown of calling services (stops accepting new calls and waits up to 2 hours for existing calls to complete).

[PUT] https://<node_ip>/api/v1/external/maintenanceMode

Call this API only when there are no active calls.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body :

```
{
      "maintenanceMode": "on"
}
```

maintenanceMode - Status of Maintenance Mode to be set - "on" or "off".

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
        "status": {  
            "code": 200,
            "message": "Your request to enable/disable maintenance mode was successful."
    }
}
```

Sample Response 2:

```
{
      "status": {
          "code": 409,
          "message": "Maintenance Mode is already on/off"
    }
}
```

Sample Response 3 :

```
{
      "status": {
          "code": 400,
          "message": "Bad Request - wrong input"   
    }
}
```

##### Change admin password

Changes the admin user's password.

[PUT] https://<node_ip>/api/v1/external/password

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body:

```
{
  "newPassword": "new"
}
```

newPassword- The new password to be set for the 'admin' account of the Video Mesh Node.

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully set the new passphrase for user admin."
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 400,
        "message": "Enter a new passphrase that wasn't used for one of the previous 3 passphrases."
    }
}
```

VMN Network APIs

Video Mesh Network APIs enable organization admins to manage internal and external network settings.

##### Get External Network Configuration

Detects if the external network is enabled or disabled. If the external network is enabled, it also fetches the External IP Address, External Subnet Mask and the External Gateway.

[GET] https://<node_ip>/api/v1/external/externalNetwork

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully fetched external network configuration."
    },
    "result": {
        "ip": "1.1.1.1",
        "mask": "2.2.2.2",
        "gateway": "3.3.3.3"
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 200,
        "message": "External network not enabled."
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 500,
        "message": "Failed to get external network configuration."
    }
}
```

##### Edit External Network Configuration

Changes the External Network settings. This API can be used to either enable the external network along with setting or editing the External Network Interface with External IP Address, External Subnet Mask and External Gateway. It can also be used to disable the external network. After you make external network configuration changes, the node reboots to apply these changes.

[PUT] https://<node_ip>/api/v1/external/externalNetwork

You can configure this only for newly deployed Video Mesh Nodes, whose default admin password has changed. Do not use this API after registering the node to an organisation.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body:

Enabling external network:

```
{
  "externalNetworkEnabled": true,
  "externalIp": "1.1.1.1",
  "externalMask": "2.2.2.2",
  "externalGateway": "3.3.3.3"
}
```

Disabling external network:

```
{
  "externalNetworkEnabled": false
}
```

externalNetworkEnabled- Boolean value (true or false) to enable/disable External Network

externalIp - The External IP to be added

externalMask - The Netmask for the External Network

externalGateway - The Gateway for the External Network

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully saved the external network configuration. This node will reboot soon to apply the changes. Please wait for a minute and relogin to the node to verify that all changes were applied."
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 200,
        "message": "Successfully disabled the external network. This node will reboot soon to apply the changes. Please wait for a minute and relogin to the node to verify that all changes were applied."
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 400,
        "message": "One or more errors in the input: Value should be boolean for 'externalNetworkEnabled'"
    }
}
```

Sample Response 4:

```
{
    "status": {
        "code": 400,
        "message": "External network configuration has not changed; skipping save of the external network configuration."
    }
}
```

##### Get Internal Network details

Retrieves the internal network configuration details which includes Network Mode, IP Address, Subnet Mask, Gateway, DNS Caching details, DNS servers, NTP servers, Internal Interface MTU, Hostname and Domain.

[GET] https://<node_ip>/api/v1/external/internalNetwork

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully fetched internal network details"
    },
    "result": {
        "dhcp": false,
        "ip": "1.1.1.1",
        "mask": "2.2.2.2",
        "gateway": "3.3.3.3",
        "dnsCaching": false,
        "dnsServers": [
            "4.4.4.4",
            "5.5.5.5"
        ],
        "mtu": 1500,
        "ntpServers": [
            "6.6.6.6"
        ],
        "hostName": "test-vmn",
        "domain": ""
    }
}
```

Sample Response 2:

```
{
      "status": {
          "code": 500,
          "message": "Failed to get Network details."   
    }
}
```

Sample Response 3:

```
{
      "status": {
          "code": 500,
          "message": "Failed to get host details."   
    }
}
```

##### Edit DNS servers

Updates DNS Servers with new ones.

[PUT] https://<node_ip>/api/v1/external/internalNetwork/dns

Place the Node in Maintenance Mode before making this change. See Enable or Disable Maintenance Mode for more information on moving a node into maintenance mode.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body:

```
{
    "dnsServers": "1.1.1.1 2.2.2.2"
}
```

dnsServers - DNS servers to be updated. Multiple space-separated DNS servers are allowed.

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully saved DNS servers"
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 409,
        "message": "Requested DNS server(s) already exist."
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 424,
        "message": "Maintenance Mode is not enabled. Kindly enable Maintenance Mode and try again for this node."
    }
}
```

##### Edit NTP servers

Updates NTP servers with new ones.

[PUT] https://<node_ip>/api/v1/external/internalNetwork/ntp

Place the Node in Maintenance Mode before making this change. See Enable or Disable Maintenance Mode for more information on moving a node into maintenance mode.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body:

```
{
    "ntpServers": "1.1.1.1 2.2.2.2"
}
```

ntpServers - NTP servers to be updated. Multiple space-separated NTP servers are allowed.

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully saved the NTP servers."
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 409,
        "message": "Requested NTP server(s) already exist."
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 424,
        "message": "Maintenance Mode is not enabled. Kindly enable Maintenance Mode and try again for this node."
    }
}
```

##### Edit host name and domain

Updates the Hostname and Domain of the Video Mesh Node.

[PUT] https://<node_ip>/api/v1/external/internalNetwork/host

Place the Node in Maintenance Mode before making this change. The Node reboots to apply the change. See Enable or Disable Maintenance Mode for more information on moving a node into maintenance mode.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body:

```
{
    "hostName": "test-vmn",
    "domain": "abc.com"
}
```

hostName - The new hostname of the node.

domain - The new domain for the hostname of the node (optional).

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully saved the host FQDN. This node will reboot soon to apply the changes. Please wait for a minute and relogin to the node to verify that all changes were applied."
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 400,
        "message": "Unable to resolve FQDN"
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 409,
        "message": "Entered hostname and domain already set to same."
    }
}
```

##### Enable or Disable DNS Caching

Enables or Disables DNS Caching. Consider enabling caching if DNS checks often take over 750 ms to resolve, or if recommended by Cisco Support.

[PUT] https://<node_ip>/api/v1/external/internalNetwork/dnsCaching

Place the Node in Maintenance Mode before making this change. The Node reboots to apply the change. See Enable or Disable Maintenance Mode for more information on moving a node into maintenance mode.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body:

```
{
    "dnsCaching": true
}
```

dnsCaching - DNS Caching Configuration. Accepts Boolean value (true or false).

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully saved DNS settings changes. This node will reboot soon to apply the changes. Please wait for a minute and relogin to the node to verify that all changes were applied."
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 400,
        "message": "One or more errors in the input: 'dnsCaching' field value should be a boolean"
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 409,
        "message": "dnsCaching is already set to false"
    }
}
```

##### Edit Interface MTU

Changes the Maximum Transmission Unit (MTU) for the node's network interfaces from the default value of 1500. Values between 1280 and 9000 are allowed.

[PUT] https://<node_ip>/api/v1/external/internalNetwork/mtu

Place the Node in Maintenance Mode before making this change. The Node reboots to apply the change. See Enable or Disable Maintenance Mode for more information on moving a node into maintenance mode.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body:

```
{
    "internalInterfaceMtu": 1500
}
```

internalInterfaceMtu - Maximum Transmission Unit for the node's network interfaces. The value should be between 1280 and 9000.

Request Headers:

'Content-type': 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully saved the internal interface MTU settings. This node will reboot soon to apply the changes. Please wait for a minute and relogin to the node to verify that all changes were applied."
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 400,
        "message": "One or more errors in the input: 'internalInterfaceMtu' field value should be a number"
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 400,
        "message": "Please enter a number between 1280 and 9000."
    }
}
```

VMN Server Certificate APIs

Video Mesh Server Certificate APIs enable organization admins to create, update, download, and delete the certificates related to Video Mesh Nodes. For more information, see Exchange Certificate Chains Between Unified CM and Video Mesh Nodes .

##### Create the CSR certificate

Generates a CSR (Certificate Signing Request) certificate, and the private key, based on the details provided.

[POST] https://<node_ip>/api/v1/externalCertManager/generateCsr

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body :

```
{
    "csrInfo":
    {
         "commonName": "1.2.3.4",
         "emailAddress": "abc@xyz.com",
         "altNames": "1.1.1.1 2.2.2.2",
         "organization": "VMN",
         "organizationUnit": "IT",
         "locality": "BLR",
         "state": "KA",
         "country": "IN",
         "passphrase": "",
         "keyBitSize": 2048
    }
}
```

commonName - IP/FQDN of the Video Mesh Node given as common name. (mandatory)

emailAddress - User's Email Address. (optional)

altNames - Subject Alternative Name(s) (optional). Multiple space separated FQDNs are allowed. If provided, it must contain the common name. If altNames are not provided, it takes the commonName as the value of altNames.

organization - Organization/Company name. (optional)

organizationUnit - Organizational Unit or Department or Group Name, etc. (optional)

locality - City/Locality. (optional)

state - State/Province. (optional)

country - Country/Region. Two-letter abbreviation. Do not provide more than two letters. (optional)

passphrase - Private Key Passphrase. (optional)

keyBitSize - Private Key Bit Size. Accepted values are 2048, by default, or 4096. (optional)

Request Headers :

Content-Type: 'application/json'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully generated CSR"
    },
    "result": {
        "caCert": {},
        "caKey": {
            "fileName": "VideoMeshGeneratedPrivate.key",
            "localFileName": "CaPrivateKey.key",
            "fileLastModified": "Fri Jul 21 2023 08:12:25 GMT+0000 (Coordinated Universal Time)",
            "uploadDate": 1689927145422,
            "size": 1678,
            "type": "application/pkcs8",
            "modulus": "S4MP1EM0DULU2"
        },
        "certInstallRequestPending": false,
        "certInstallStarted": null,
        "certInstallCompleted": null,
        "isRegistered": true,
        "caCertsInstalled": false,
        "csr": {
            "keyBitsize": 2048,
            "commonName": "1.2.3.4",
            "organization": "VMN",
            "organizationUnit": "IT",
            "locality": "BLR",
            "state": "KA",
            "country": "IN",
            "emailAddress": "abc@xyz.com",
            "altNames": [
                "1.1.1.1",
                "2.2.2.2"
            ],
            "csrContent": "-----BEGIN CERTIFICATE REQUEST-----\nS4MP1E_C3RT_C0NT3NT\n-----END CERTIFICATE REQUEST-----"
        },
        "encryptedPassphrase": null
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 400,
        "message": "Private key already exists. Delete it before generating new CSR."
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 400,
        "message": "CSR certificate already exists. Delete it before generating new CSR."
    }
}
```

Sample Response 4:

```
{
    "status": {
        "code": 400,
        "message": "CSR certificate and private key already exist. Delete them before generating new CSR."
    }
}
```

Sample Response 5:

```
{
    "status": {
        "code": 400,
        "message": "There were one or more errors while generating the CSR: The \"Country\" field must contain exactly two A-Z characters."
    }
}
```

##### Download the CSR certificate

Downloads the generated CSR certificate.

[GET] https://<node_ip>/api/v1/externalCertManager/csr

You can also download the file through the Send and Download option.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
-----BEGIN CERTIFICATE REQUEST-----
S4MP1E_C3RT_C0NT3NT
-----END CERTIFICATE REQUEST-----
```

Sample Response 2:

```
{
    "status": {
        "code": 404,
        "message": "Could not download, CSR certificate does not exist."
    }
}
```

##### Download the private key

Downloads the private key generated along with the CSR certificate.

[GET] https://<node_ip>/api/v1/externalCertManager/key

You can also download the file through the Send and Download option.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
-----BEGIN RSA PRIVATE KEY-----
S4MP1E_PR1V4T3_K3Y
-----END RSA PRIVATE KEY-----
```

Sample Response 2:

```
{
    "status": {
        "code": 404,
        "message": "Could not download, private key does not exist."
    }
}
```

##### Delete the CSR certificate

Deletes the existing CSR certificate.

[DELETE] https://<node_ip>/api/v1/externalCertManager/csr

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully deleted the CSR certificate"
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 404,
        "message": "CSR certificate does not exist."
    }
}
```

##### Delete the private key

Deletes the existing private key.

[DELETE] https://<node_ip>/api/v1/externalCertManager/key

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully deleted the private key"
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 404,
        "message": "Private key does not exist."
    }
}
```

##### Install the CA signed certificate and private key

Uploads the provided CA signed certificate and the private key on the Video Mesh node and installs the certificate on the node.

[POST] https://<node_ip>/api/v1/externalCertManager/uploadInstallCaCert

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Body :

Use 'form-data' to upload the following files:

CA Signed Certificate (.crt) file with key as 'crtFile'.

Private Key (.key) file with key as 'keyFile'.

Request Headers :

Content-Type: 'multipart/form-data'

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully installed certificate and key. It might take a few seconds to reflect on the node."
    },
    "result": {
        "caCert": {
            "fileName": "videoMeshCsr.crt",
            "localFileName": "CaCert.crt",
            "fileLastModified": 1689931788598,
            "uploadDate": 1689931788605,
            "size": 1549,
            "type": "application/x-x509-ca-cert",
            "certStats": {
                "version": 0,
                "subject": {
                    "countryName": "IN",
                    "stateOrProvinceName": "KA",
                    "localityName": "BLR",
                    "organizationName": "VMN",
                    "organizationalUnitName": "IT",
                    "emailAddress": "abc@xyz.com",
                    "commonName": "1.2.3.4"
                },
                "issuer": {
                    "countryName": "AU",
                    "stateOrProvinceName": "Some-State",
                    "organizationName": "ABC"
                },
                "serial": "3X4MPL3",
                "notBefore": "2023-07-21T09:28:19.000Z",
                "notAfter": "2024-12-02T09:28:19.000Z",
                "signatureAlgorithm": "sha256WithRsaEncryption",
                "fingerPrint": "11:22:33:44:AA:BB:CC:DD",
                "publicKey": {
                    "algorithm": "rsaEncryption",
                    "e": 65537,
                    "n": "3X4MPL3",
                    "bitSize": 2048
                },
                "altNames": [],
                "extensions": {}
            }
        },
        "caKey": {
            "fileName": "VideoMeshGeneratedPrivate.key",
            "localFileName": "CaPrivateKey.key",
            "fileLastModified": 1689931788629,
            "uploadDate": 1689931788642,
            "size": 1678,
            "type": "application/pkcs8",
            "modulus": "S4MP1EM0DULU2"
        },
        "certInstallRequestPending": true,
        "certInstallStarted": null,
        "certInstallCompleted": null,
        "isRegistered": true,
        "caCertsInstalled": false,
        "csr": {
            "keyBitsize": 2048,
            "commonName": "1.2.3.4",
            "organization": "VMN",
            "organizationUnit": "IT",
            "locality": "BLR",
            "state": "KA",
            "country": "IN",
            "emailAddress": "abc@xyz.com",
            "altNames": [
                "1.1.1.1",
                "2.2.2.2"
            ],
            "csrContent": "-----BEGIN CERTIFICATE REQUEST-----\nS4MP1E_C3RT_C0NT3NT\n-----END CERTIFICATE REQUEST-----"
        },
        "encryptedPassphrase": null
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 400,
        "message": "Could not parse the certificate file. Make sure it is a properly formatted certificate and try again."
    }
}
```

Sample Response 3:

```
{
    "status": {
        "code": 400,
        "message": "Private Key does not match Certificate (different modulus)"
    }
}
```

Sample Response 4:

```
{
    "status": {
        "code": 202,
        "message": "Certificate and private key PENDING installation. It might take a few seconds to reflect on the node. If the node is in maintenance mode, it will get installed once it is disabled."
    }
}
```

##### Download the CA signed certificate

Downloads the CA signed certificate installed on the node.

[GET] https://<node_ip>/api/v1/externalCertManager/caCert

You can also download the file through the Send and Download option.

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
-----BEGIN CERTIFICATE-----
S4MP1E_C3RT_C0NT3NT
-----END CERTIFICATE-----
```

Sample Response 2:

```
{
    "status": {
        "code": 404,
        "message": "Could not download, CA certificate does not exist."
    }
}
```

##### Delete the CA signed certificate

Deletes the CA signed certificate installed on the node.

[DELETE] https://<node_ip>/api/v1/externalCertManager/caCert

Authorization : Basic Authentication utilizing the Video Mesh username (‘admin’) and the password.

Sample Responses :

Sample Response 1:

```
{
    "status": {
        "code": 200,
        "message": "Successfully deleted the CA certificate."
    }
}
```

Sample Response 2:

```
{
    "status": {
        "code": 404,
        "message": "CA certificate does not exist."
    }
}
```

Common API Responses

Listed below are some sample responses that you might encounter while using any of the APIs mentioned above.

Sample Response 1: Wrong Credentials provided in the Basic Authorization.

```
{
    "status": {
        "code": 401,
        "message": "login failed: incorrect password or username"
    }
}
```

Sample Response 2: VMN is not upgraded to the required version that supports these APIs.

```
{
    "status": {
        "code": 421,
        "message": "Misdirected Request 1:[undefined]"
    }
}
```

Sample Response 3: Wrong referer entered in the header (when header wasn't expected).

```
{
    "status": {
        "code": 421,
        "message": "Misdirected Request 2:[https://x.x.x.x/setup]"
    }
}
```

Sample Response 4: Rate limit exceeded, try after some time.

```
{
    "status": {
        "code": 429,
        "message": "Too Many Requests"
    }
}
```

### Add Internal and External Routing Rules

In a dual network interface (NIC) deployment, you can fine tune the routing for Video Mesh nodes by adding user-defined route rules for external and internal interfaces. The default routes are added to the nodes, but you can make exceptions—for example, external subnets or host addresses that need to be accessed through the internal interface, or internal subnets or host addresses that need to be accessed from the external interface. Perform the following steps as needed.

From the Video Mesh node interface, choose 5 External IP Configuration and then click Select .

Choose 3 Manage Routing Rules , and then click Select .

The first time you open this page, the default system routing rules appear in the list. By default, all internal traffic goes through the internal interface and external traffic through the external interface.

You can add manual overrides to these rules in the next steps.

Follow these steps as needed:

- Click Add external route , and then enter the internal subnet or host IP address to use for the external route.

- Click Add internal route , and then enter the external subnet or host IP address to use for the internal route.

As you add each rule, they appear in the routing rule list, categorized as user defined rules.

The default routes cannot be deleted, but you can delete any user-defined overrides that you configured.

Custom routing rules may create potential for conflicts with other routing. For example, you may define a rule that freezes your SSH connection to the Video Mesh Node interface. If this happens, do one of the following and then remove or modify the routing rule:

Open an SSH connection to the public IP address of the Video Mesh Node.

Access the Video Mesh Node through the VM console in your hypervisor’s management interface.

### Register the Video Mesh Node to the Webex Cloud

Use this procedure to register Video Mesh nodes to the Webex cloud and complete additional configuration. When you use Control Hub to register your node, you create a cluster to which the node is assigned. A cluster contains one or more media nodes that serve users in a specific geographic region. The registration steps also configure SIP call settings, set an upgrade schedule, and subscribe to email notifications.

Before you begin

Once you begin registration of a node, you must complete it within 60 minutes or you have to start over.

Ensure that any popup blockers in your browser are disabled or that you allow an exception for https://admin.webex.com .

For best results, deploy all nodes of a cluster in the same data center. See Clusters in Video Mesh for how they work and best practices.

From the host or machine where you're registering Video Mesh Nodes to the cloud, you must have connectivity to the Webex cloud and the Video Mesh IP addresses that are being registered (in a dual NIC environment, specifically the internal IP addresses of the Video Mesh Nodes).

Sign in to Control Hub .

You sign in to Control Hub using the admin credentials. The Control Hub admin functionality is available only to users who are defined as admins in Control Hub. See Customer Account Roles for more information.

Go to Services > Hybrid and choose one:

See Complete the Prerequisites for Video Mesh for more information.

- View all : Choose this option if you've already registered one or more Video Mesh Nodes, then click Add Resource .

Make sure you have installed and configured your Video Mesh Node. Click Yes, I'm ready to register... , then click Next .

In Create a new or select a cluster , choose one:

- For a new cluster, enter a name for the cluster to which you want to assign your Video Mesh Node.

- For an existing cluster, click the field, then choose an existing cluster to which to add the new node.

We recommend that you name a cluster based on where the nodes of the cluster are located geographically. For example, "San Francisco".

In Enter the FQDN or IP address , enter the fully qualified domain name (FQDN) or internal IP address of your Video Mesh Node and then click Next .

- If you use FQDN, enter a domain that can be resolved by DNS.

- If you use an IP address, enter the same internal IP address that you used to configure the node from the console.

An FQDN must resolve directly to the IP address or it is not usable. We perform the validation on FQDN to rule out any typo or configuration mismatch.

The dual network interface does not support specifying an FQDN for the external IP address. The FQDN can be added only on the screen where internal IP address is entered. That is what the FQDN must resolve to using the DNS servers that are specified on the same screen.

Under Upgrade Schedule , choose a time, frequency, and time zone.

The default is a daily upgrade schedule. You can change it to a weekly schedule on a specific day. When an upgrade is available, the Video Mesh Node software automatically upgrades during the time that you select.

When an upgrade is available, you can use Upgrade Now to start the upgrade before the next maintenance window or Postpone to defer it until the subsequent window.

Under Email Notifications , add administrator email addresses to subscribe to notifications about service alarms and software upgrades.

Your administrator email address is automatically added. You can remove it if you want.

Toggle the Video Quality setting on to enable 1080p 30fps video.

With this setting, SIP participants that join a meeting that is hosted in a Video Mesh Node can use 1080p 30fps video if they are all inside the corporate network and they're using a high definition-capable device. The setting applies to all clusters of nodes.

If this setting is off, the default is 720p.

For video resolutions supported by Webex App, see Video specifications for calls and meetings .

Read the information under Complete Registration , then click Go to Node to register the node to the Webex cloud.

A new browser tab opens to check the node. This step safelists the Video Mesh Node using the IP address of the node. During the registration process, Control Hub redirects you to the Video Mesh Node. The IP address must be safelisted, otherwise registration fails. The registration process must be completed from the enterprise network where the node is installed.

Check Allow Access to the Webex Video Mesh Node , then click Continue .

Click Allow .

Your account is validated, your Video Mesh Node is registered and the message Registration Complete is shown, indicating your Video Mesh Node is now registered to Webex.

The Video Mesh Node gets machine credentials based on your organization's entitlements. The generated machine credentials expire periodically and are refreshed.

Click the portal link or close the tab to go back to the Video Mesh page.

On the Video Mesh page, you now see the new cluster that contains the Video Mesh Node that you registered.

If you go to the cluster, you'll see the new Video Mesh Node, which initially shows a status of Registering . The node changes to Running when it is ready for use in your Webex organization.

Because the software is a container that contains services from the cloud infrastructure, it gets updates from the cloud to remain in sync with the cloud services. Required updates may install shortly after you register the node to the cloud. You can also change your automatic upgrade schedule. See Automatic Upgrades for Hybrid Services Resources for more information.

If you installed the demo image on the node that you registered, you'll see a demo mode yellow status alarm. This alarm is normal, but we recommend installing the full software image before the 90-day grace period expires for the demo image.

At this point, the Video Mesh Node is ready to communicate with Cisco cloud services over the secured channels using a token issued for authentication. The Video Mesh Node also communicates with Docker Hub (docker.com, docker.io). Docker is used by Video Mesh node to store containers for distribution to different Video Mesh nodes all over the world. Only Cisco has credentials to write to Docker Hub. The Video Mesh nodes can reach out to Docker Hub using read-only credentials to download the containers for upgrades.

Images are downloaded based on checksum, which is transmitted to the node as part of the provisioning data. See this document for more details on how docker pull works: https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#sharing-promotes-smaller-images

Things to keep in mind

Keep the following information in mind about Video Mesh Node and how it works once registered to your Webex organization:

When you deploy a new Video Mesh Node, the Webex App and Webex-registered device won't recognize the new node for up to 2 hours. The clients check for cluster reachability during startup, a network change, or cache expiration. You can wait for 2 hours or, as a workaround, restart your Webex App or reboot the Webex room or desk device. Afterwards, call activity is captured in the Video Mesh reports in Control Hub.

A Video Mesh Node registers to a single Webex organization; it is not a multitenant device.

To understand what uses Video Mesh Node and what doesn't, see the table in Clients and Devices that use Video Mesh Node .

The Video Mesh Node can connect to your Webex site or to another customer or partner's Webex site. For example, Site A deployed a Video Mesh Node cluster and registered it with the example1.webex.com domain. If users in Site A dial in to mymeeting@example1.webex.com, they use the Video Mesh Node and a cascade can be created. If the users in site A dial yourmeeting@example2.webex.com, the Site A users will use their local Video Mesh Node and connect to the meeting on Site B's Webex organization.

What to do next

To register additional nodes, repeat these steps.

If an upgrade is available, we recommend that you apply it as soon as possible. To upgrade, complete the following steps:

The provisioning data is pushed to the Webex cloud by the Cisco development team over secured channels. The provisioning data is signed. For the containers, the provisioning data contains name, checksum, version, and so on. Video Mesh Node also gets its provisioning data from the Webex cloud over secured channels.

Once Video Mesh Node gets its provisioning data, the node authenticates with read-only credentials and downloads the container with specific checksum and name and upgrades the system. Each container running on Video Mesh Node has an image name and checksum. These attributes are uploaded to the Webex cloud using secured channels.

### Enable Quality of Service (QoS) for Video Mesh Node

Before you begin

Make the necessary firewall port changes that are covered in the diagram and table. See Ports and Protocols Used by Video Mesh .

For Video Mesh nodes to be enabled for QoS, the nodes must be online. Nodes in maintenance mode or offline states are excluded when you enable this setting.

From the customer view in https://admin.webex.com , go to Services > Hybrid , click Edit settings on the Video Mesh
                    card.

Scroll to Quality of Service and click Enable .

When enabled, you get the large, discrete port range (determined by
                        on-premises call control configuration) that's used for audio and video for
                        on-premises SIP clients/endpoints and intracluster cascades with unique DSCP
                        markings:.

Audio: 52500–62999 DSCP EF (Expedited Forwarding)

Video/Content: 63000–65500 DSCP AF41

All SIP and cascade traffic from Video Mesh nodes is marked with EF for audio and AF41 for video. The discrete port ranges are used as source ports for cascade media to other Video Mesh nodes and cloud media nodes as well as source and destination ports for SIP client media. Webex App and cascade media continue to use the destination shared port of 5004 and 9000.

All Video Mesh return traffic (audio, video, content) from the shared
                            ports is marked with AF41. The audio traffic needs to be remarked to EF
                            in your network, based on the source port numbers.

A status message appears that shows which nodes are being enabled one-by-one
                        for the QoS port range. You can click review pending
                            nodes to see a list of nodes that are pending for QoS.
                        Enabling this setting can take up to 2 hours, depending on call traffic on
                        the nodes.

If QoS is not fully enabled in 2 hours, open a case with support for further investigation.

The nodes reboot and are updated with the new port range.

If you decide to disable the setting, you get the small, consolidate port range that's used for both audio and video (34000–34999). All traffic from Video Mesh nodes (SIP, cascades, cloud traffic, and so on) gets a single marking of AF41.

### Verify  Video Mesh Node Port Ranges With Reflector Tool in the Web Interface

The reflector tool (a combination of a server on the  Video Mesh node and client through a Python script) is used to verify whether the required TCP/UDP ports are open from  Video Mesh nodes.

Before you begin

Download a copy of the Reflector Tool Client (a Python script) from https://github.com/CiscoDevNet/webex-video-mesh-reflector-client .

For the script to work properly, ensure that you're running Python 2.7.10 or later in your environment.

Currently, this tool supports SIP endpoints to  Video Mesh nodes and intracluster verification.

From the customer view in https://admin.webex.com , enable maintenance node for the Video Mesh Node by following these instructions .

Wait for the node to show a 'Ready for maintenance' status in Control Hub.

Open the Webex Video Mesh node interface.

For instructions, see Manage Video Mesh Node From the Web Interface .

Scroll to Reflector Tool , and then start either the TCP Reflector Server or UDP Reflector Server , depending on what protocol you want to use.

Click Start Reflector Server , and then wait for the server to start successfully.

You'll see a notice when the server starts.

From a system (such as a PC) on a network that you want Video Mesh nodes to reach, run the script with the following command:

```
$ python <local_path_to_client_script>/reflectorClient.py --ip <ip address of the server> --protocol <tcp or udp>
```

At the end of the run, the client shows a success message if all the required ports are open:

The client shows a failed message if any required ports are not open:

Resolve any port issues on the firewall and then rerun the above steps.

Run the client with --help to get more details.

### Configure Video Mesh Node for Proxy Integration

Use this procedure to specify the type of proxy that you want to integrate with a Video Mesh. If you choose a transparent inspecting proxy or an explicit proxy, you can use the node's interface to upload and install the root certificate, check the proxy connection, and troubleshoot any potential issues.

Before you begin

See Proxy Support for Video Mesh for an overview of the supported proxy options.

Requirements for Proxy Support for Video Mesh

Enter the Video Mesh setup URL https://[IP or FQDN/setup] in a web browser, enter the admin credentials you set up for the node, and then click Sign In .

Go to Trust Store & Proxy , and then choose an option:

- No Proxy —The default option before you integrate a proxy. No certificate update is required.

- Transparent Non-Inspecting Proxy —Video Mesh nodes are not configured to use a specific proxy server address and should not require any changes to work with a non-inspecting proxy. No certificate update is required.

- Transparent Inspecting Proxy —Video Mesh nodes are not configured to use a specific proxy server address. No http(s) configuration changes are necessary on Video Mesh; however, the Video Mesh nodes need a root certificate so that they trust the proxy. Inspecting proxies are typically used by IT to enforce policies regarding which websites can be visited and types of content that are not permitted. This type of proxy decrypts all your traffic (even https).

Proxy IP/FQDN —Address that can be used to reach the proxy machine.

Proxy Port —A port number that the proxy uses to listen for proxied traffic.

Proxy Protocol —Choose http (Video Mesh tunnels its https traffic through the http proxy) or https (traffic from the Video Mesh node to the proxy uses the https protocol). Choose an option based on what your proxy server supports.

Choose from among the following authentication types, depending on your proxy environment:

Option

Usage

None

Choose for HTTP or HTTPS explicit proxies where there's no authentication method.

Basic

Available for HTTP or HTTPS explicit proxies.

Used for an HTTP user agent to provide a username and password when making a request, and uses Base64 encoding.

Digest

Available for HTTPS explicit proxies only.

Used to confirm the account before sending sensitive information, and applies a hash function on the user name and password before sending over the network.

NTLM

Available for HTTP explicit proxies only.

Like Digest, used to confirm the account before sending sensitive information. Uses Windows credentials instead of the username and password.

If you choose this option, enter the Active Directory domain that the proxy uses for authentication in the NTLM Domain field. Enter the name of the proxy workstation (also referred to as a workstation account or machine account) within the specified NTLM domain in the NTLM Workstation field.

Follow the next steps for a transparent inspecting or explicit proxy.

Click Upload a Root Certificate or End Entity Certificate , and then locate and choose the root certificate for the explicit or transparent inspecting proxy.

The certificate is uploaded but not yet installed because the node needs to be rebooted to install the certificate. Click the arrow by the certificate issuer name to get more details or click Delete if you made a mistake and want to reupload the file.

For transparent inspecting or explicit proxies, click Check Proxy Connection to test the network connectivity between the Video Mesh node and the proxy.

If the connection test fails, you'll see an error message that shows the reason and how you can correct the issue.

After the connection test passes, for explicit proxy, turn the toggle on to Route all port 443 https requests from this node through the explicit proxy . This setting requires 15 seconds to take effect.

Click Install All Certificates Into the Trust Store (﻿appears whenever a root certificate was added during proxy setup) or Reboot (appears if no root certificate was added), read the prompt, and then click Install if you're ready.

The node reboots within a few minutes.

After the node reboots, sign in again if needed, and then open the Overview page to check the connectivity checks to make sure they are all in green status.

The proxy connection check only tests a subdomain of webex.com. If there are connectivity problems, a common issue is that some of the cloud domains listed in the install instructions are being blocked at the proxy.

### Integrate Video Mesh With Call Control Task Flow

Configure SIP trunks to route SIP dial-in for Webex meetings on Video Mesh. SIP devices don't support direct reachability, so you must use Unified CM or VCS Expressway configuration to establish a relationship between on-premises SIP devices and your Video Mesh clusters.

Before you begin

See Deployment Models For Video Mesh and Cisco Unified Communications Manager to understand common deployment
                        examples.

Video Mesh supports either TCP or TLS between Unified CM and SIP signaling. SIP TLS is not supported for VCS Expressway.

In Unified CM, each SIP trunk can support up to 16 Video Mesh destinations (IP addresses).

In Unified CM, incoming ports on SIP trunk security profile can be default (Non Secure SIP Trunk Profile).

Video Mesh supports 2 route patterns: sitename.webex.com and meet.ciscospark.com . Other route patterns are unsupported.

Video Mesh supports 3 route patterns: webex.com (for short video addresses ), sitename.webex.com and meet.ciscospark.com . Other route patterns are unsupported.

When you use the short video address format ( meet@webex.com ), the
                            Video Mesh node always handles the call. The node handles the call even
                            if the call is to a site that doesn't have Video Mesh enabled.

Choose one of these options, depending on your call control environment and security requirements:

- Configure Unified CM Secure TLS SIP Traffic Routing for Video Mesh

- Configure Unified CM TCP SIP Traffic Routing for Video Mesh

- Configure Expressway TCP SIP Traffic Routing for Video Mesh (TCP only)

Configure Unified CM with Video Mesh, using either TLS encrypted or TCP SIP traffic. You can create a trunk routing policy that reflects cluster preferences, and is highly available and resilient to device failures. If you use Unified CM Session Management Edition (SME), configure trunks on the Unified CM SME and leaf systems so that inbound and outbound calls are evenly distributed across the Unified CM servers within the Session Management cluster.

Typically, each site will have a dedicated Unified CM cluster associated with it. These clusters will be connected through intercluster SIP trunks. Each cluster will have call-in trunks to the local site for the Video Mesh nodes.

You can also configure your deployment to handle failure or overflow conditions. This configuration helps if there's an outage or if the Video Mesh clusters reached capacity. If the SIP meeting or call cannot be established with a cluster, the meeting or call will overflow to the cloud.

Configure neighbor zones and search rules to route SIP dial-in and dial-out for Cisco Webex meetings to Video Mesh clusters. SIP devices registered to a VCS Control or Expressway-C don't support direct reachability, so you must use a TCP-based Expressway configuration to establishes a relationship between on-premises SIP devices and your Video Mesh clusters.

You can also configure your deployment to handle failure or overflow conditions. This configuration helps if there's an outage or if the Video Mesh clusters reached capacity. If the SIP meeting or call cannot be established with a cluster, the meeting or call will overflow to the cloud through the VCS Control/Expressway-C or an Expressway C/E pair.

#### Configure Unified CM Secure TLS SIP Traffic Routing for Video Mesh

Create a SIP profile for Video Mesh clusters:

From Cisco Unified CM Administration, go to Device > Device Settings > SIP Profile , and then click Find .

Choose Standard SIP Profile For Cisco VCS , and then click Copy .

Enter a name for the new profile—for example, Video Mesh SIP Profile .

Under Trunk Specific Configuration , set Early Offer support for voice and video calls to Best Effort (no MTP inserted) .

You can apply this setting to a new SIP trunk to the Webex cloud (routed by the external domain for the Webex site). The setting does not affect any existing SIP trunking or call routing.

Make sure that Enable OPTIONS Ping to monitor destination status for Trunks with Service Type is checked.

Leave all other fields with their default values and save your changes.

Add a new SIP trunk security profile for Video Mesh clusters:

From Cisco Unified CM Administration, choose System > Security > SIP Trunk Security Profile , and then click Add New .

Enter a meaningful name, such as Video Mesh Secure SIP Trunk Security Profile

Confirm these settings:

Field

Value

Device Security Mode

Encrypted

Incoming Transport Type

TLS

Outgoing Transport Type

TLS

X.509 Subject Name

Secure Certificate Subject or Subject Alternate Name

Enter the common name of the Video Mesh node certificate.

Incoming Port

5061

SIP V.150 Outbound SDP Offer Filtering

Use Default Filter

Leave all other fields with their default values and save your changes.

Add a new SIP trunk to point to your Video Mesh clusters:

- In a Unified CM-only deployment, add a single trunk.

- In an SME deployment, a trunk typically exists between Unified CM and SME. Add another trunk between SME and Video Mesh nodes. Both trunks must have the same settings specified below.

From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New .

Choose SIP Trunk for the trunk type; leave the other values and click Next .

Enter a meaningful name, such as Video_Mesh_SIP_Trunk_UCMtoVMN .

Check the SRTP Allowed check box

For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex.

Check Run On All Active Unified CM Nodes .

Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Video Mesh nodes.

Enter 5061 for the Destination Port .

For the SIP Trunk Security Profile , choose the Video Mesh Trunk Security Profile that you created earlier. (For example, Video Mesh Secure SIP Trunk Security Profile .)

For the SIP Profile , choose the Video Mesh SIP Profile that you created earlier. (For example, Video Mesh SIP Profile .)

Leave all other fields with their default values and save your changes.

A Video Mesh call or meeting might assign media to any node in a cluster, not just the node that terminates the SIP call.

Create a SIP trunk to point to an Expressway for Webex cloud failover.

You can use a SIP trunk already in place for an existing Unified CM and Expressway deployment. If you create another one, and you also run Mobile Remote Access (MRA) with those Expressways, you can break MRA.

From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New .

Choose SIP Trunk for the trunk type; leave the other values and click Next .

Enter a meaningful name, such as Video_Mesh_VCS_Trunk .

For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex.

Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Expressways. For the Port , enter 5060 .

For SIP Profile , choose Standard SIP Profile For Cisco VCS .

Create a new route group for calls to Video Mesh clusters:

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New .

Enter a meaningful name, such as Video Mesh Node Route Group .

Change the Distribution Algorithm to Top Down .

In the Route Group Member Information section, Find the Devices with name Video Mesh .

Add Video_Mesh_SIP_Trunk_UCMtoVMN by clicking Add to Route Group .

Save your changes.

For overflow to the cloud, create a new route group for calls to Expressway:

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New .

Enter a meaningful name, such as Video Mesh Expressway Route Group .

Change the Distribution Algorithm to Top Down .

In the Route Group Member Information section, Find the Devices with name Video Mesh .

Add Video_Mesh_VCS_Trunk by clicking Add to Route Group .

Save your changes.

Create a new route list for calls to Video Mesh clusters and Expressway:

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List , and then click Add New .

Enter a meaningful name, such as Video Mesh Node Route List .

Set the Cisco Unified Communications Manager Group to Default , or another value depending on your configuration.

Save your changes.

In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Route Group .

Leave the defaults for the other settings, and then save your changes.

In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Expressway Route Group .

Leave the defaults for the other settings, and then save your changes.

Create a SIP route pattern for the short video address dialing format for Webex meetings:

From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route Pattern for Webex Short URIs .

In the IPv4 pattern , enter webex.com as the domain.

For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List .

Leave all other fields with their default values and save your changes.

With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number.

Create a SIP route pattern for the Webex site:

From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route Pattern for Webex Sites .

In the IPv4 pattern , enter the Webex site for which you want optimized media—For example, examplesitename.webex.com .

For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List .

Leave all other fields with their default values and save your changes.

Create a SIP route pattern for Webex App meetings (backwards compatibility):

From Call Routing > SIP Route Pattern , click Add New , and then enter the name Video Mesh Route Pattern for Teams Meetings .

In the IPv4 pattern , enter the meet.ciscospark.com .

For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List .

Leave all other fields with their default values and save your changes.

#### Configure Unified CM TCP SIP Traffic Routing for Video Mesh

Create a SIP profile for Video Mesh clusters:

From Cisco Unified CM Administration, go to Device > Device Settings > SIP Profile , and then click Find .

Choose Standard SIP Profile For Cisco VCS , and then click Copy .

Enter a name for the new profile—for example, Video Mesh SIP Profile .

Under Trunk Specific Configuration , set Early Offer support for voice and video calls to Best Effort (no MTP inserted) .

You can apply this setting to a new SIP trunk to the Webex (routed by the external domain for the Webex site). The setting does not affect any existing SIP trunking or call routing.

Make sure that Enable OPTIONS Ping to monitor destination status for Trunks with Service Type is checked.

Leave all other fields with their default values and save your changes.

Add a new SIP trunk security profile for Video Mesh clusters:

From Cisco Unified CM Administration, choose System > Security > SIP Trunk Security Profile , and then click Add New .

Enter a meaningful name, such as Video Mesh Trunk Security Profile

Confirm these settings:

Field

Value

Device Security Mode

Non Secure

Incoming Transport Type

TCP+UDP

Outgoing Transport Type

TCP

Incoming Port

5060

SIP V.150 Outbound SDP Offer Filtering

Use Default Filter

Leave all other fields with their default values and save your changes.

Add a new SIP trunk to point to your Video Mesh clusters:

- In a Unified CM-only deployment, add a single trunk.

- In an SME deployment, a trunk typically exists between Unified CM and SME. Add another trunk between SME and Video Mesh nodes. Both trunks must have the same settings specified below.

From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New .

Choose SIP Trunk for the trunk type; leave the other values and click Next .

Enter a meaningful name, such as Video_Mesh_SIP_Trunk_UCMtoVMN .

For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex.

Check Run On All Active Unified CM Nodes .

Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Video Mesh nodes.

Enter 5060 for the Destination Port .

For the SIP Trunk Security Profile , choose the Video MeshTrunk Security Profile that you created earlier. (For example, Video Mesh Trunk Security Profile .)

For the SIP Profile , choose the Video Mesh SIP Profile that you created earlier. (For example, Video Mesh SIP Profile .)

Leave all other fields with their default values and save your changes.

A Video Mesh call or meeting might assign media to any node in a cluster, not just the node that terminates the SIP call.

Create a new SIP trunk to point to an Expressway.

You can use a SIP trunk already in place for an existing Unified CM and Expressway deployment. If you create another one, and you also run Mobile Remote Access (MRA) with those Expressways, you can break MRA.

From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New .

Choose SIP Trunk for the trunk type; leave the other values and click Next .

Enter a meaningful name, such as Video_Mesh_VCS_Trunk .

For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex.

Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Expressways. For the Port , enter 5060 .

For SIP Profile , choose Standard SIP Profile For Cisco VCS .

Create a new route group for calls to Video Mesh clusters:

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New .

Enter a meaningful name, such as Video Mesh Node Route Group .

Change the Distribution Algorithm to Top Down .

In the Route Group Member Information section, Find the Devices with name Video Mesh .

Add the Video_Mesh_SIP_Trunk_UCMtoVMN by clicking Add to Route Group .

Save your changes.

For overflow to the cloud, create a new route group for calls to Expressway:

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New .

Enter a meaningful name, such as Video Mesh Expressway Route Group .

Change the Distribution Algorithm to Top Down .

In the Route Group Member Information section, Find the Devices with name Video Mesh .

Add the Video_Mesh_VCS_Trunk by clicking Add to Route Group .

Save your changes.

Create a new route list for calls to Video Mesh clusters and Expressway:

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List , and then click Add New .

Enter a meaningful name, such as Video Mesh Node Route List .

Set the Cisco Unified Communications Manager Group to Default , or another value depending on your configuration.

Save your changes.

In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Route Group .

Leave the defaults for the other settings, and then save your changes.

In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Expressway Route Group .

Leave the defaults for the other settings, and then save your changes.

Create a SIP route pattern for the short video address dialing format for Webex meetings:

From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route
                                        Pattern for Webex Short URIs .

In the IPv4 pattern , enter webex.com as the domain.

For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List .

Leave all other fields with their default values and save your
                            changes.

With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number.

Create a SIP route pattern for the Webex site:

From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route
                                        Pattern for Webex Sites .

In the IPv4 pattern , enter the Webex site for which you want
                            optimized media—For example, examplesitename.webex.com ,
                            where examplesitename is the name of your actual Webex
                            site.

For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List .

Leave all other fields with their default values and save your
                            changes.

Create a SIP route pattern for Webex App meetings:

From Call Routing > SIP Route Pattern , click Add New , and then enter the name Video Mesh Route Pattern for Teams Meetings .

In the IPv4 pattern , enter the meet.ciscospark.com .

For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List .

Leave all other fields with their default values and save your changes.

#### Configure Expressway TCP SIP Traffic Routing for Video Mesh

Create a zone that points to Video Mesh clusters:

From VCS Control or Expressway-C, go to Configuration > Zones > Zones , and then click New .

Configure the following fields:

Field Name

Value

Name

Enter a name that easily identifies the zone—for example, WebexVideoMeshZone

Type

Neighbor

H.323

Mode

Off

SIP

Mode

On

Port

5060

Transport

TCP

Location

Look up peers by

Address

Peer [n] Address

Enter the IP addresses for each Video Mesh node.

Leave the other fields with their default settings, and then save your changes.

Create  dial patterns for Video Mesh clusters for Webex sites:

From Expressway-C, go to Configuration > Dial Plan > Search Rules , and then click New .

Configure the following fields for the Webex site search rule:

Field Name

Value

Rule Name

Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-YourSite

Priority

100 is the default. Ensure that this number is lower than the cloud fallback and B2B rules.

Protocol

SIP

Mode

Alias Pattern Match

Pattern Type

Regex

Pattern String

.*@(YourSite\.)?webex\.com.*

This pattern matches both yoursite.webex.com and webex.com (for short video addresses) formats. With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number.

Pattern Behavior

Leave

On Successful Match

Continue

Target

Choose the Video Mesh zone that you created—for example, WebexVideoMeshZone .

Leave the other fields with their default settings, and then save your changes.

Create a traversal client and zone pair that points to the cloud Expressway for failover:

See the Expressway Basic Configuration Guide for your release for steps to create the traversal client and zone pair.

Create a fallback search rule to the Traversal Client Zone that leads to the Expressway-E:

From Expressway-C, go to Configuration > Dial Plan > Search Rules , and then click New .

Configure the following fields:

Field Name

Value

Rule Name

Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-Failover

Priority

100 is the default. Ensure that the priority is lower by entering a number that is higher than the Video Mesh dial pattern and B2B rules.

Protocol

SIP

Mode

Any Alias

Pattern Behavior

Leave

On Successful Match

Continue

Target

Choose the Traversal Client Zone that leads to the Expressway-E.

Leave the other fields with their default settings, and then save your changes.

From Expressway-E, go to Configuration > Zones > Zones . Click New and add the Webex Zone.

In versions before X8.11, you created a new DNS zone for this purpose.

Create a dial pattern for the cloud Expressway:

From Expressway-E, go to Configuration > Dial Plan > Search Rules , and then click New .

Configure the following fields:

Field Name

Value

Rule Name

Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-toCloud

Priority

Enter a higher value than the rule for the local Video Mesh nodes. If the nodes are set to 100, set this value to 101 . You must also ensure that the value is lower than all B2B rules on your Expressway.

Protocol

SIP

Source

Named

Source Name

Choose the secure traversal server zone from Expressway-C—for example, WebexVideoMeshZone

Mode

Alias Pattern Match

Pattern Type

Regex

Pattern String

.*@(YourSite\.)?webex\.com.*

Pattern Behavior

Leave

On Successful Match

Stop

Target

Choose the Webex Zone or DNS zone.

For SIP devices registered to the Expressway-C, open the device IP address in a browser, go to Setup , scroll to SIP , and choose Standards from the Type drop-down.

### Exchange Certificate Chains Between Unified CM and Video Mesh Nodes

Complete a certificate exchange to establish two-way trust between the Unified CM and Video Mesh interfaces. With the secure trunk configuration, the certificates allow encrypted SIP traffic and SRTP media in your organization from trusted Unified CMs to land on trusted Video Mesh nodes.

In a clustered environment, you must install CA and server certificates on each node individually.

Before you begin

For security reasons, we recommend that you use a CA signed certificate on your Video Mesh nodes instead of the node's default self-signed certificate.

Open the Video Mesh node interface (IP address/setup, for example, https://192.0.2.0/setup ) in your browser and sign in with the node's admin credentials.

Go to Server Certificates and request and upload a certificate and key pair as needed:

(Optional) If you need a certificate issued from a certified provider, click Create a Certificate Signing Request . Fill out the required information (including the Subject Alternative Name(s) , which are FQDNs that must contain the common name, and then generate the request. Download the CSR to submit the request to the provider. (You can request multiple ones. They return the certificate authority (CA) signed certificate (the private key was already generated during the CSR creation step)

The common name is not a URL. It doesn’t include any protocol (for example http:// or https://), port number, or pathname. The commonName field in the X.509 certificate specification represents the common name. For https://www.example.com , the correct value is example.com .

The private key is already in place when you generate a CSR. If you don't use the CSR creation step, you must upload a private key.

When you have the certificate and key, click Upload a Server Certificate (.crt or .pem file) , choose the certificate file, then click Upload a Private Key (.key file) and enter a passphrase if you have one.

After you get the certificate, go to the first Video Mesh node in a cluster, click Install Server Certificate , read the prompt, click Install , then click OK .

A cloud-registered Video Mesh node gracefully shuts down, waiting up to 2 hours for any calls to end. The node then completes the certificate installation. A prompt appears when the server certificate installs. You can then reload the page to view the new certificate and key entry.

Click Download next to the certificate and key files to save a local copy.

Save the files somewhere that's easy to remember and leave the Video Mesh instance open in the browser tab.

Go to the next Video Mesh node in the cluster, fill in the passphrase, and then upload the private key file. Then click Upload a Server Certificate and then choose Install Server Certificate , read the prompt, click Install , then click OK .

Repeat these steps for any Video Mesh nodes in the same cluster.

In another browser tab, from Cisco Unified OS Administration, go to Security > Certificate Management . Enter your search criteria and click Find , then choose the filename of the certificate or Certificate Trust List (CTL) and click Download .

Save the Unified CM file somewhere that's easy to remember and leave Unified CM instance open in the browser tab.

Go back to the Video Mesh node interface tab, click Trust Store & Proxy , and then choose an option:

- If the Unified CM uses a CA certificate that's signed by a well-known organization, then the Video Mesh node trusts it automatically. The trust is based on the list of root certificates from the VMN node's host OS, which update periodically.

- If the Unified CM uses a CA certificate that's signed by an internal enterprise CA root certificate, add that root certificate to the node. That root certificate is available from within the enterprise, but might not be downloadable from Unified CM.

- Add both the ECDSA and RSA certificates that the Unified CM uses to serve external requests. These certificates can be self-signed or CA certificates.

- If you downloaded a single certificate, click Upload a Root Certificate or End Entity Certificate (.crt or .pem file) , and choose the CallManager.pem certificate file that you downloaded. Click Install All Certificates into the Trust Store , read the prompt, click Install , and then reboot the node.

- If you downloaded a certificate chain, upload the root CA certificate and intermediate CA certificate, and then click Install All Certificates into the Trust Store , read the prompt, and then click Install .

A cloud-registered Video Mesh node gracefully shuts down, waiting up to 2 hours for any calls to end. To install the CallManager.pem certificate, the node automatically reboots. When it comes back online, a prompt appears when the CallManager.pem certificate installs on the Video Mesh node. You can then reload the page to view the new certificate.

Go back to the Cisco Unified OS Administration tab and click Upload Certificate/Certificate Chain . Choose the certificate name from the Certificate Purpose drop-down list, browse to the file that you downloaded from the Video Mesh node interface, and then click Open .

To upload the file to the server, click Upload File .

If you're uploading a certificate chain, you must upload all certificates in the chain.

Restart the affected service after uploading the certificate. When the server comes back up, you can access the CCMAdmin or CCMUser GUI to verify that your newly added certificates are in use.

You can install and manage server certificates via APIs. For more information, see VMN Server Certificate APIs .

### Enable Media Encryption for the Organization and Video Mesh Clusters

Use this procedure to turn on media encryption for your organization and individual Video Mesh clusters. This setting forces an end-to-end TLS setup and you must have a secure TLS SIP trunk in place on your Unified CM that points to your Video Mesh nodes.

Settings

Result

Unified CM is configured with a secure trunk and this Video Mesh Control Hub setting is not enabled.

Calls fail.

Unified CM is not configured with a secure trunk and this Video Mesh Control Hub setting is enabled.

Calls won't fail but they fall back to non-secure mode.

Cisco endpoints must also be configured with a security profile and TLS negotiation for end-to-end encryption to work. Otherwise, calls overflow to the cloud from endpoints that are not configured with TLS. We recommend that you enable this feature only if all endpoints can be configured to use TLS.

Before you begin

Configure Unified CM Secure TLS SIP Traffic Routing for Video Mesh

Exchange Certificate Chains Between Unified CM and Video Mesh Nodes

From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click Edit Settings on the Video Mesh card.

Scroll to Media Encryption and toggle on the setting.

This setting makes encryption mandatory on all media channels that pass
                        through Video Mesh nodes in your organization. Note the preceding table and
                        caution note for situations where calls may fail and what's required for
                        end-to-end encryption to work.

Click Resources and repeat the following steps on each Video Mesh cluster that you want to enable for secure SIP traffic.

Select a Video Mesh cluster entry in the list, and then click Cluster settings .

Scroll to the SIP TLS Configuration card.

Under Trusted SIP sources , ﻿enter the Common Name (CN) or any FQDNs that are present in the Subject Alternative Name on the Unified CM certificate (typically the FQDN of the Unified CM).

These entries are identified as trusted SIP sources and are allowed to send secure SIP calls to Webex Video Mesh.

The Trusted SIP sources field will be greyed out unless Media Encryption is enabled for the organization, as detailed in the previous step.

### Enable Video Mesh for the Webex Site

To use optimized media to the Video Mesh Node for a Webex meeting to all the Webex app and devices to join, this configuration needs to be enabled for the Webex site. Enabling this setting links Video Mesh and meeting instances in the cloud together and allows cascades to occur from Video Mesh nodes. If this setting is not enabled, the Webex app and devices will not use the Video Mesh node for Webex meetings.

From the customer view in https://admin.webex.com , go to Services > Meetings , click the Webex site from the Meetings card, and then click Settings to access the the Webex site configuration options.

Access Common Settings by clicking on Service > Meeting > Site Settings . From Common Settings , click Cloud Collaboration Meeting Rooms (CMR) , choose Video Mesh for Media Resource Type , and then click Save at the bottom.

This setting links Video Mesh and meeting instances in the cloud together and allows cascades to occur from Video Mesh nodes. The setting should populate across your environment after 15 minutes. Webex meetings that start after this change is populated will pick up the new setting. If you leave this field set to Cloud (the default option), all meetings are hosted in the cloud and the Video Mesh node is not used.

### Assign Collaboration Meeting Rooms to Webex App Users

If you manage your site through Control Hub:

From the customer view in https://admin.webex.com , go to Users > Manage Users .

To assign to users in bulk, see this document .

Assign Webex Collaboration Meeting Rooms to users in your organization.

If you manage your site through Site Admin:

From Site Admin, go to User Management .

Edit the user account and check Collaboration Meeting Room.

To assign to users in bulk, see this document .

### Verify the meeting experience on the secure endpoint

Use these steps to verify that the endpoints are securely registered and the correct meeting experience appears.

Join a meeting from the secured endpoint.

Verify that the meeting roster list appears on the device.

This example shows how the meeting list looks on an endpoint with a touch panel:

During the meeting, access the Webex Conference information from Call Details .

Verify that Encryption section shows the Type as AES-128 and the Status as On .

| 1 | Install and Configure Video Mesh Node Software Use the procedure for your supported hypervisor to deploy a Video Mesh Node. You install the software on-premises which creates a node and then perform initial configuration, such as network settings. You'll register it to the cloud later. |
|---|---|
| 2 | Log in to the Video Mesh Node Console Sign in to the console for the first time. The Video Mesh Node software has a default password. You need to change this value before you configure the node. |
| 3 | Set the Network Configuration of the Video Mesh Node in the Console Use this procedure to configure the network settings for the Video Mesh Node if you didn't configure them when you set up the node on a virtual machine. You'll set a static IP address and change the FQDN/hostname and NTP servers. DHCP is not currently supported. |
| 4 | Use these steps to configure the external interface for a dual network interface (dual NIC) deployment: Set The External Network Interface of the Video Mesh Node Add Internal and External Routing Rules After the node is back online and you verified the internal network configuration, you can configure the external network interface if you're deploying the Video Mesh Node in your network's DMZ so that you can isolate the enterprise (internal) traffic from the outside (external) traffic. You can also make exceptions or overrides to the default routing rules. |
| 5 | Register the Video Mesh Node to the Webex Cloud Use this procedure to register Video Mesh nodes to the Webex cloud and complete additional configuration. When you use Control Hub to register your node, you create a cluster to which the node is assigned. A cluster contains one or more media nodes that serve users in a specific geographic region. The registration steps also configure SIP call settings, set an upgrade schedule, and subscribe to email notifications. |
| 6 | Enable and verify Quality of Service (QoS) with the following tasks: Enable Quality of Service (QoS) for Video Mesh Node Verify Video Mesh Node Port Ranges With Reflector Tool in the Web Interface Enable QoS if you want Video Mesh nodes to automatically mark SIP traffic (on-premises SIP registered endpoints) for both audio (EF) and video (AF41) separately with appropriate class of service and use well-known port ranges for specific media types. This change will let you create QoS policies and effectively remark return traffic from the cloud if desired. Use the Reflector Tool steps to verify the correct ports are opened on your firewall. |
| 7 | Configure Video Mesh Node for Proxy Integration Use this procedure to specify the type of proxy that you want to integrate with a Video Mesh. If you choose a transparent inspecting proxy, you can use the node's interface to upload and install the root certificate, check the proxy, and troubleshoot any potential issues. |
| 8 | Follow Integrate Video Mesh With Call Control Task Flow and choose one of the following, depending on your call control, security requirements, and whether you want to integrate Video Mesh with your call control environment: Configure Unified CM Secure TLS SIP Traffic Routing for Video Mesh (TLS) Configure Unified CM TCP SIP Traffic Routing for Video Mesh (TCP) Configure Expressway TCP SIP Traffic Routing for Video Mesh (TCP) SIP devices don't support direct reachability, so you must use Unified CM or VCS Expressway configuration to establish a relationship between on-premises registered SIP devices and your Video Meshclusters. You only need to trunk your Unified CM or VCS Expressway to Video Mesh Node, depending on your call control environment. |
| 9 | Exchange Certificate Chains Between Unified CM and Video Mesh Nodes In this task, you download certificates from the Unified CM and Video Mesh interfaces and upload one to the other. This step establishes secure trust between the two products and, in conjunction with the secure trunk configuration, allows encrypted SIP traffic and SRTP media in your organization to land on Video Mesh nodes. |
| 10 | Enable Media Encryption for the Organization and Video Mesh Clusters Use this procedure to turn on media encryption for your organization and individual Video Mesh clusters. This setting forces end-to-end TLS setup and you must have a secure TLS SIP trunk in place on your Unified CM that points to your Video Mesh nodes. |
| 11 | Enable Video Mesh for the Webex Site To use optimized media to the Video Mesh Node for a Webex meeting to all the Webex app and devices to join, this configuration needs to be enabled for the Webex site. Enabling this setting links Video Mesh and meeting instances in the cloud together and allows cascades to occur from Video Mesh nodes. If this setting is not enabled, the Webex app and devices will not use the Video Mesh node for Webex meetings. |
| 12 | Assign Collaboration Meeting Rooms to Webex App Users |
| 13 | Verify the meeting experience on the secure endpoint If you are using media encryption through the end-to-end TLS setup, use these steps to verify that the endpoints are securely registered and the correct meeting experience appears. |

| 1 | Using your computer, open the VMware vSphere client and sign in to the vCenter or ESXi system on the server. |
|---|---|
| 2 | Go to Actions > Deploy OVF Template . |
| 3 | On the Select an OVF tempate page, click Local File , then Choose Files . Navigate to where the videomesh.ova file is located, choose the file, and then click Next . Each time you do a Video Mesh Node installation, we recommend that you redownload the OVA rather than using a previously downloaded version. If you try to deploy an old OVA, your Video Mesh Node may not work properly nor register to the cloud. An old OVA will also lead to potential issues during upgrades. Make sure you download a new copy of the OVA from this link . |
| 4 | On the Select a name and folder page, enter a Virtual machine name for the Video Mesh Node (for example, "Video_Mesh_Node_1"), choose a location where the virtual machine node deployment can reside, and then click Next . A validation check runs. After it finishes, the template details appear. |
| 5 | Verify the template details and then click Next . |
| 6 | On the Configuration page, choose the type of deployment configuration, and then click Next . VMNLite (default) VMNFull The options are listed in the order of increasing resource requirements. If you choose the VMNLite option, you'll need to repeat the steps to deploy the other instance(s) on the same host, and choose the same option each time. Co-residency of VMNLite and non-VMNLite instances has not been tested and is not supported. |
| 7 | On the Select storage page, ensure that the default disk format of Thick Provision Lazy Zeroed and VM storage policy of Datastore Default are selected and then click Next . |
| 8 | On the Select networks page, choose the network option from the list of entries to provide the desired connectivity to the VM. For Internal Interface  Network , choose the node's internal IP address. For External InterfaceNetwork , choose the external IP address that faces the public network. Ignore this option if you don't have a dual NIC deployment. The inside interface (the default interface for traffic) is used for CLI, SIP trunks, SIP traffic and node management. The outside (external) interface is for HTTPS and websockets communication to the Webex cloud, along with the cascades traffic from the nodes to a meeting. For a DMZ deployment, you can set up the Video Mesh node with the dual network interface (NIC). This deployment lets you separate the internal enterprise network traffic (used for interbox communication, cascades between nodes in a cluster, and to access the node's management interface) from the external cloud network traffic (used for connectivity to the outside world, Inter-Cluster cascades, and cascades to Webex). All nodes in a cluster must be in dual NIC mode; a mixture of single and dual NIC is not supported. For an existing installation of Video Mesh Node software, you cannot upgrade from a single NIC to a dual NIC configuration. You must do a fresh install of Video Mesh Node in this case. |
| 9 | On the Customize template page, configure the following network settings: Hostname (Optional)—Enter the FQDN (hostname and domain) or a single word hostname for the node. To ensure a successful registration to the cloud, use only lowercase characters in the FQDN or hostname that you set for the Video Mesh Node. Capitalization is not supported at this time. When using or configuring FQDN or hostname, you must also enter a valid and resolvable domain. The total length of the FQDN must not exceed 64 characters. IP Address — Enter the IP address for the internal interface of the node. Mask —Enter the subnet mask address in dot-decimal notation. For example, 255.255.255.0 . Gateway —Enter the gateway IP address. A gateway is a network node that serves as an access point to another network. DNS Servers —Enter a comma-separated list of DNS servers, which handle translating domain names to numeric IP addresses. (Up to 4 DNS entries are allowed.) NTP Servers —Enter your organization's NTP server or another external NTP server that can be used in your organization. You can also use a comma-separated list to enter multiple NTP servers. The Video Mesh Node must have an internal IP address and resolvable DNS name. The node IP address must not belong to the IP address range reserved for Video Mesh Node internal use. The default reserved IP address range is 172.17.42.0–172.17.42.63, which can be configured later in the Diagnostic menu. This IP address range is for communication within the Video Mesh Node and between the software containers which hold the different components of the node—for example, SIP interface and media transcoding. Deploy all the nodes on the same subnet or VLAN, so that all nodes in a cluster are reachable from wherever the clients reside in your network. For a dual NIC DMZ deployment, you can set the external IP address in the node console, after you've saved the internal network configuration and rebooted the node later. If preferred, you can skip the network setting configuration and follow the steps in Set the Network Configuration of the Video Mesh Node in the Console after you sign into the node. |
| 10 | On the Ready to Complete page, verify that all the settings that you entered match the guidelines in this procedure, and then click Finish . After deployment of the OVA is complete, your Video Mesh Node appears in the list of VMs. |
| 11 | Right-click the Video Mesh Node VM, and then choose Power > Power On . The Video Mesh Node software is installed as a guest on the VM Host. You are now ready to sign in to the console and configure the Video Mesh Node. You may experience a delay of a few minutes before the node containers come up. A bridge firewall message appears on the console during first boot, during which you can't sign in. |

| 1 | Sign in to the Cisco NFVIS portal . Go to Configuration > Virtual Machine > Images > Image Repository . |
|---|---|
| 2 | Choose LOCAL , select the Video Mesh OVA file, and select the destination datastore. Verify the Image Name , set VM Workload Type to Calling and VM Type to ECP/VIDEO MESH , then select Upload File . |
| 3 | Wait for the image to reach ACTIVE in the Image Repository. Confirm that NFVIS created a profile for the uploaded image. An image still in CREATE is not ready for deployment. |
| 4 | Go to Configuration > Deploy . Under Select VM , choose ECP/VIDEO MESH , then select the Video Mesh icon. |
| 5 | Use Network Interfaces to connect the VM to the NFVIS network selected for its internal interface. Select the connection line and, in vNIC Details , set: Model : Virtio Driver Name : vhost Driver Queues : 8 |
| 6 | For a dual-NIC deployment, use Network Interfaces to connect a second vNIC to the NFVIS network designated for the node’s external interface. Select the new connection line and set Model to Virtio , Driver Name to vhost , and Driver Queues to 8 . Verify and record which vNIC ID connects to the internal network and which connects to the external network. Configure the external static IP address later in Set The External Network Interface of the Video Mesh Node . Use the same single-NIC or dual-NIC configuration for every node in a cluster. |
| 7 | Select the Video Mesh icon again. In Deployment Details , enter a unique VM name and select the image uploaded in step 2 and its matching profile. |
| 8 | Select the deployment disk and verify that the profile and NFVIS resource settings provide the dedicated CPU, memory, and storage required for the planned Video Mesh node size. |
| 9 | Select Deploy . Wait for the successful deployment notification, then go to Configuration > Virtual Machine > Manage . Refresh the status until the VM is Active . |
| 10 | Select Terminal for the new VM. Allow the first boot to finish and wait for the Video Mesh login prompt. For a production VMNLite deployment, repeat the VM deployment steps to deploy a second identical VMNLite VM on the NFVIS host. After the Video Mesh login prompt appears, wait 2-3 minutes for the node to complete its startup and the console to stabilize before continuing. |

| 1 | Sign in to Prism Central and go to Infrastructure > Compute > OVAs . |
|---|---|
| 2 | Select Upload OVA . Choose the downloaded Video Mesh OVA and target cluster. Give the upload a unique name that includes its version or upload date, then complete the upload. |
| 3 | In the OVA list, confirm that the upload succeeded and Disk Format shows VMDK . |
| 4 | Select the uploaded OVA and choose Deploy as VM . |
| 5 | Enter a unique VM name and select the target cluster. Verify that the VM’s CPU and memory match the planned VMNFull or VMNLite profiles. For VMNFull (default profile): 2 vCPUs (35 cores per vCPU) (2 × 35 = 70 virtual CPU cores) 60 GB main memory. For VMNLite: 23 vCPUs (1 core per vCPU) 20 GB main memory. |
| 6 | Click Next . The Resources wizard opens. |
| 7 | In the Resources > Disks table, verify that the attached disk has a capacity of 80 GB for a VMNFull or standard VMNLite node, or 250 GB for a VMNLite recording node. |
| 8 | Attach the correct subnet or VLAN using the Attach to Subnet option and set the network connection state to Connected . If the wizard contains an empty or default network entry displaying No network found for VM network , remove that entry. The invalid entry can prevent the wizard from continuing even after the correct subnet has been attached. |
| 9 | For a dual-NIC deployment, select Attach to Subnet again and attach a second network interface to the subnet or VLAN designated for the node’s external interface. Set its Network Connection State to Connected . Before creating the VM, verify that two interfaces are present and record which subnet is attached to each interface. Configure the external static IP address later in Set The External Network Interface of the Video Mesh Node . Use the same single-NIC or dual-NIC configuration for every node in a cluster. |
| 10 | Select UEFI as the BIOS mode and click Next . The Management wizard opens. |
| 11 | Leave Categories blank unless categories are required by the organization. |
| 12 | Select the appropriate time zone. |
| 13 | Select No Customization on the Guest Customization card and click Next . |
| 14 | Review the settings and select Create VM . |
| 15 | Find the new VM’s NIC MAC address in Prism Central. Alternatively, sign in to a Nutanix Controller VM (CVM) and run: acli vm.nic_get "<VM name>" |
| 16 | From the CVM command line, run this command once for each NIC , using its MAC address:: acli vm.nic_update "<VM name>" "<MAC address>" queues=8 |
| 17 | Go to Infrastructure > Compute > VMs . Select the new VM and choose Summary > Power Operations > Power On . |
| 18 | Select Launch Console . Allow the first boot to finish and wait for the Video Mesh login prompt. After it appears, allow another 2–3 minutes for startup to settle before continuing. For a production VMNLite deployment, repeat the VM deployment steps for all three identical instances required by the selected configuration. |

| 1 | Open the Video Mesh Node console using the step for your hypervisor: VMware ESXi/vSphere: In the VMware vSphere client, go to the Video Mesh Node VM and choose Console . Cisco NFVIS: In the NFVIS portal, go to Configuration > Virtual Machine > Manage , locate the Video Mesh Node VM, and choose Terminal . Nutanix AHV: In Prism Central, go to VMs , select the Video Mesh Node VM, and choose Launch Console . The Video Mesh Node VM boots up and a login prompt appears. If the login prompt does not appear, press Enter . You may briefly see a message that indicates the system is being initialized. |
|---|---|
| 2 | Use the following default username and password to log in: Login: admin Password: ciscosystems Because you are logging in to the Video Mesh Node for the first time, you must change the administrator passphrase (password). |
| 3 | For (current) password, enter the default password (from above),  and then press Enter . |
| 4 | For new password, enter a new passphrase, and then press Enter . |
| 5 | For retype new password, retype the new passphrase, and then press Enter . A "Password successfully changed" message appears, and then the initial Video Mesh Node screen appears with a message about unauthorized access being prohibited. |
| 6 | Press Enter to load the main menu. |

| 1 | Open the node console interface using the step for your hypervisor, then sign in with the admin credentials: VMware ESXi/vSphere: In the VMware vSphere client, go to the Video Mesh Node VM and choose Console . Cisco NFVIS: In the NFVIS portal, go to Configuration > Virtual Machine > Manage , locate the Video Mesh Node VM, and select Terminal . Nutanix AHV: In Prism Central, go to VMs , select the Video Mesh Node VM, and choose Launch Console . After first time setup of the network settings and if the Video Mesh is reachable, you can access the node interface through secure shell (SSH). |
|---|---|
| 2 | From the main menu of the Video Mesh Node console, choose option 2 Edit Configuration and then click Select . |
| 3 | Read the prompt that the calls will end on the Video Mesh Node, and then click Yes . |
| 4 | Click Static , enter the IP address for the internal interface, Mask , Gateway , and DNS values for your network. The Video Mesh Node must have an internal IP address and resolvable DNS name. The node IP address must not belong to the IP address range reserved for Video Mesh Node internal use. The default reserved IP address range is 172.17.42.0–172.17.42.63, which can be configured in the Diagnostic menu. This IP address range is for communication within the Video Mesh Node and between the software containers which hold the different components of the node—for example, SIP interface and media transcoding. Deploy all the nodes on the same subnet or VLAN, so that all nodes in a cluster are reachable from wherever the clients reside in your network. For a dual NIC DMZ deployment, you can set the external IP address in the next procedure, after you've saved the internal network configuration and rebooted the node. |
| 5 | Enter your organization's NTP server or another external NTP server that can be used in your organization. After you configure the NTP server and save network settings, you can follow the steps in Check Health of Video Mesh Node From Console to verify that the time is synchronizing correctly through the specified NTP servers. If you configure more than one NTP servers, the poll interval for failover is 40 seconds. |
| 6 | (Optional) Change the hostname or domain, if required. To ensure a successful registration to the cloud, use only lowercase characters in the hostname that you set for the Video Mesh Node. Capitalization is not supported at this time. When using or configuring FQDN or hostname, you must also enter a valid and resolvable domain. The total length of the FQDN must not exceed 64 characters. |
| 7 | Click Save , and then click Save Changes & Reboot . During the save, DNS validation is performed if you provided a domain. A warning is displayed if the FQDN (hostname and domain) is not resolvable using the DNS server addresses provided. You may choose to save by ignoring the Warning, but calls will not work until the FQDN can resolve to the DNS configured on the node. After the Video Mesh Node reboots, the network configuration changes take effect. |

| 1 | From the main menu of the Video Mesh Node console, choose option 5 External IP Configuration and then click Select . |
|---|---|
| 2 | Click 1 Enable/Disable , then Select , and then Yes to enable the external IP address options on the node. |
| 3 | As you did with the initial network configuration, enter the IP Address (external), Mask , and Gateway values. The Interface field shows the name of the external interface for the node. |
| 4 | Click Save and Restart . The node once again reboots to enable the dual IP address, and then automatically configures the basic static routing rules. These rules determine that traffic to and from a private class IP address uses an internal interface; traffic to and from a public class IP address uses an external interface. Later, you can create your own routing rules—For example, if you need to configure an override and allow access to an external domain from the internal interface. Under certain circumstances, the existing SSH connection may terminate. For organizations that use IP addresses from the public range , you must reestablish an SSH connection to the public IP address of the Video Mesh Node. |
| 5 | To validate the internal and external IP address configuration, from the main menu of the console, go to 4 Diagnostics , and then choose Ping . |
| 6 | In the ping field, enter a destination address that you want to test, such as an external destination or an internal IP address, and then click OK . Test an external destination (example, cisco.com); if successful, the results show that the destination was accessed from the external interface. Test an internal IP address; if successful, the results show that the address was accessed from the internal interface. |

| 1 | From the Video Mesh node interface, choose 5 External IP Configuration and then click Select . |
|---|---|
| 2 | Choose 3 Manage Routing Rules , and then click Select . The first time you open this page, the default system routing rules appear in the list. By default, all internal traffic goes through the internal interface and external traffic through the external interface. You can add manual overrides to these rules in the next steps. |
| 3 | Follow these steps as needed: Click Add external route , and then enter the internal subnet or host IP address to use for the external route. Click Add internal route , and then enter the external subnet or host IP address to use for the internal route. As you add each rule, they appear in the routing rule list, categorized as user defined rules. The default routes cannot be deleted, but you can delete any user-defined overrides that you configured. |

| 1 | Sign in to Control Hub . You sign in to Control Hub using the admin credentials. The Control Hub admin functionality is available only to users who are defined as admins in Control Hub. See Customer Account Roles for more information. |
|---|---|
| 2 | Go to Services > Hybrid and choose one: Set up : Choose this option if this is the first Video Mesh Node you're registering, then click Next . See Complete the Prerequisites for Video Mesh for more information. View all : Choose this option if you've already registered one or more Video Mesh Nodes, then click Add Resource . |
| 3 | Make sure you have installed and configured your Video Mesh Node. Click Yes, I'm ready to register... , then click Next . |
| 4 | In Create a new or select a cluster , choose one: For a new cluster, enter a name for the cluster to which you want to assign your Video Mesh Node. For an existing cluster, click the field, then choose an existing cluster to which to add the new node. We recommend that you name a cluster based on where the nodes of the cluster are located geographically. For example, "San Francisco". |
| 5 | In Enter the FQDN or IP address , enter the fully qualified domain name (FQDN) or internal IP address of your Video Mesh Node and then click Next . If you use FQDN, enter a domain that can be resolved by DNS. If you use an IP address, enter the same internal IP address that you used to configure the node from the console. An FQDN must resolve directly to the IP address or it is not usable. We perform the validation on FQDN to rule out any typo or configuration mismatch. The dual network interface does not support specifying an FQDN for the external IP address. The FQDN can be added only on the screen where internal IP address is entered. That is what the FQDN must resolve to using the DNS servers that are specified on the same screen. |
| 6 | Under Upgrade Schedule , choose a time, frequency, and time zone. The default is a daily upgrade schedule. You can change it to a weekly schedule on a specific day. When an upgrade is available, the Video Mesh Node software automatically upgrades during the time that you select. When an upgrade is available, you can use Upgrade Now to start the upgrade before the next maintenance window or Postpone to defer it until the subsequent window. |
| 7 | Under Email Notifications , add administrator email addresses to subscribe to notifications about service alarms and software upgrades. Your administrator email address is automatically added. You can remove it if you want. |
| 8 | Toggle the Video Quality setting on to enable 1080p 30fps video. With this setting, SIP participants that join a meeting that is hosted in a Video Mesh Node can use 1080p 30fps video if they are all inside the corporate network and they're using a high definition-capable device. The setting applies to all clusters of nodes. If this setting is off, the default is 720p. For video resolutions supported by Webex App, see Video specifications for calls and meetings . |
| 9 | Read the information under Complete Registration , then click Go to Node to register the node to the Webex cloud. A new browser tab opens to check the node. This step safelists the Video Mesh Node using the IP address of the node. During the registration process, Control Hub redirects you to the Video Mesh Node. The IP address must be safelisted, otherwise registration fails. The registration process must be completed from the enterprise network where the node is installed. |
| 10 | Check Allow Access to the Webex Video Mesh Node , then click Continue . |
| 11 | Click Allow . Your account is validated, your Video Mesh Node is registered and the message Registration Complete is shown, indicating your Video Mesh Node is now registered to Webex. The Video Mesh Node gets machine credentials based on your organization's entitlements. The generated machine credentials expire periodically and are refreshed. |
| 12 | Click the portal link or close the tab to go back to the Video Mesh page. On the Video Mesh page, you now see the new cluster that contains the Video Mesh Node that you registered. If you go to the cluster, you'll see the new Video Mesh Node, which initially shows a status of Registering . The node changes to Running when it is ready for use in your Webex organization. Because the software is a container that contains services from the cloud infrastructure, it gets updates from the cloud to remain in sync with the cloud services. Required updates may install shortly after you register the node to the cloud. You can also change your automatic upgrade schedule. See Automatic Upgrades for Hybrid Services Resources for more information. If you installed the demo image on the node that you registered, you'll see a demo mode yellow status alarm. This alarm is normal, but we recommend installing the full software image before the 90-day grace period expires for the demo image. At this point, the Video Mesh Node is ready to communicate with Cisco cloud services over the secured channels using a token issued for authentication. The Video Mesh Node also communicates with Docker Hub (docker.com, docker.io). Docker is used by Video Mesh node to store containers for distribution to different Video Mesh nodes all over the world. Only Cisco has credentials to write to Docker Hub. The Video Mesh nodes can reach out to Docker Hub using read-only credentials to download the containers for upgrades. Images are downloaded based on checksum, which is transmitted to the node as part of the provisioning data. See this document for more details on how docker pull works: https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#sharing-promotes-smaller-images |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid , click Edit settings on the Video Mesh
                    card. |
|---|---|
| 2 | Scroll to Quality of Service and click Enable . When enabled, you get the large, discrete port range (determined by
                        on-premises call control configuration) that's used for audio and video for
                        on-premises SIP clients/endpoints and intracluster cascades with unique DSCP
                        markings:. Audio: 52500–62999 DSCP EF (Expedited Forwarding) Video/Content: 63000–65500 DSCP AF41 All SIP and cascade traffic from Video Mesh nodes is marked with EF for audio and AF41 for video. The discrete port ranges are used as source ports for cascade media to other Video Mesh nodes and cloud media nodes as well as source and destination ports for SIP client media. Webex App and cascade media continue to use the destination shared port of 5004 and 9000. All Video Mesh return traffic (audio, video, content) from the shared
                            ports is marked with AF41. The audio traffic needs to be remarked to EF
                            in your network, based on the source port numbers. A status message appears that shows which nodes are being enabled one-by-one
                        for the QoS port range. You can click review pending
                            nodes to see a list of nodes that are pending for QoS.
                        Enabling this setting can take up to 2 hours, depending on call traffic on
                        the nodes. |
| 3 | If QoS is not fully enabled in 2 hours, open a case with support for further investigation. The nodes reboot and are updated with the new port range. |

| 1 | From the customer view in https://admin.webex.com , enable maintenance node for the Video Mesh Node by following these instructions . |
|---|---|
| 2 | Wait for the node to show a 'Ready for maintenance' status in Control Hub. |
| 3 | Open the Webex Video Mesh node interface. For instructions, see Manage Video Mesh Node From the Web Interface . |
| 4 | Scroll to Reflector Tool , and then start either the TCP Reflector Server or UDP Reflector Server , depending on what protocol you want to use. |
| 5 | Click Start Reflector Server , and then wait for the server to start successfully. You'll see a notice when the server starts. |
| 6 | From a system (such as a PC) on a network that you want Video Mesh nodes to reach, run the script with the following command: $ python <local_path_to_client_script>/reflectorClient.py --ip <ip address of the server> --protocol <tcp or udp> At the end of the run, the client shows a success message if all the required ports are open: The client shows a failed message if any required ports are not open: |
| 7 | Resolve any port issues on the firewall and then rerun the above steps. |
| 8 | Run the client with --help to get more details. |

| 1 | Enter the Video Mesh setup URL https://[IP or FQDN/setup] in a web browser, enter the admin credentials you set up for the node, and then click Sign In . |
|---|---|
| 2 | Go to Trust Store & Proxy , and then choose an option: No Proxy —The default option before you integrate a proxy. No certificate update is required. Transparent Non-Inspecting Proxy —Video Mesh nodes are not configured to use a specific proxy server address and should not require any changes to work with a non-inspecting proxy. No certificate update is required. Transparent Inspecting Proxy —Video Mesh nodes are not configured to use a specific proxy server address. No http(s) configuration changes are necessary on Video Mesh; however, the Video Mesh nodes need a root certificate so that they trust the proxy. Inspecting proxies are typically used by IT to enforce policies regarding which websites can be visited and types of content that are not permitted. This type of proxy decrypts all your traffic (even https). Explicit Proxy —With explicit proxy, you tell the client (Video Mesh nodes) which proxy server to use, and this option supports several authentication types. After you choose this option, you must enter the following information: Proxy IP/FQDN —Address that can be used to reach the proxy machine. Proxy Port —A port number that the proxy uses to listen for proxied traffic. Proxy Protocol —Choose http (Video Mesh tunnels its https traffic through the http proxy) or https (traffic from the Video Mesh node to the proxy uses the https protocol). Choose an option based on what your proxy server supports. Choose from among the following authentication types, depending on your proxy environment: Option Usage None Choose for HTTP or HTTPS explicit proxies where there's no authentication method. Basic Available for HTTP or HTTPS explicit proxies. Used for an HTTP user agent to provide a username and password when making a request, and uses Base64 encoding. Digest Available for HTTPS explicit proxies only. Used to confirm the account before sending sensitive information, and applies a hash function on the user name and password before sending over the network. NTLM Available for HTTP explicit proxies only. Like Digest, used to confirm the account before sending sensitive information. Uses Windows credentials instead of the username and password. If you choose this option, enter the Active Directory domain that the proxy uses for authentication in the NTLM Domain field. Enter the name of the proxy workstation (also referred to as a workstation account or machine account) within the specified NTLM domain in the NTLM Workstation field. Follow the next steps for a transparent inspecting or explicit proxy. | Option | Usage | None | Choose for HTTP or HTTPS explicit proxies where there's no authentication method. | Basic | Available for HTTP or HTTPS explicit proxies. Used for an HTTP user agent to provide a username and password when making a request, and uses Base64 encoding. | Digest | Available for HTTPS explicit proxies only. Used to confirm the account before sending sensitive information, and applies a hash function on the user name and password before sending over the network. | NTLM | Available for HTTP explicit proxies only. Like Digest, used to confirm the account before sending sensitive information. Uses Windows credentials instead of the username and password. If you choose this option, enter the Active Directory domain that the proxy uses for authentication in the NTLM Domain field. Enter the name of the proxy workstation (also referred to as a workstation account or machine account) within the specified NTLM domain in the NTLM Workstation field. |
| Option | Usage |
| None | Choose for HTTP or HTTPS explicit proxies where there's no authentication method. |
| Basic | Available for HTTP or HTTPS explicit proxies. Used for an HTTP user agent to provide a username and password when making a request, and uses Base64 encoding. |
| Digest | Available for HTTPS explicit proxies only. Used to confirm the account before sending sensitive information, and applies a hash function on the user name and password before sending over the network. |
| NTLM | Available for HTTP explicit proxies only. Like Digest, used to confirm the account before sending sensitive information. Uses Windows credentials instead of the username and password. If you choose this option, enter the Active Directory domain that the proxy uses for authentication in the NTLM Domain field. Enter the name of the proxy workstation (also referred to as a workstation account or machine account) within the specified NTLM domain in the NTLM Workstation field. |
| 3 | Click Upload a Root Certificate or End Entity Certificate , and then locate and choose the root certificate for the explicit or transparent inspecting proxy. The certificate is uploaded but not yet installed because the node needs to be rebooted to install the certificate. Click the arrow by the certificate issuer name to get more details or click Delete if you made a mistake and want to reupload the file. |
| 4 | For transparent inspecting or explicit proxies, click Check Proxy Connection to test the network connectivity between the Video Mesh node and the proxy. If the connection test fails, you'll see an error message that shows the reason and how you can correct the issue. |
| 5 | After the connection test passes, for explicit proxy, turn the toggle on to Route all port 443 https requests from this node through the explicit proxy . This setting requires 15 seconds to take effect. |
| 6 | Click Install All Certificates Into the Trust Store (﻿appears whenever a root certificate was added during proxy setup) or Reboot (appears if no root certificate was added), read the prompt, and then click Install if you're ready. The node reboots within a few minutes. |
| 7 | After the node reboots, sign in again if needed, and then open the Overview page to check the connectivity checks to make sure they are all in green status. The proxy connection check only tests a subdomain of webex.com. If there are connectivity problems, a common issue is that some of the cloud domains listed in the install instructions are being blocked at the proxy. |

| Option | Usage |
|---|---|
| None | Choose for HTTP or HTTPS explicit proxies where there's no authentication method. |
| Basic | Available for HTTP or HTTPS explicit proxies. Used for an HTTP user agent to provide a username and password when making a request, and uses Base64 encoding. |
| Digest | Available for HTTPS explicit proxies only. Used to confirm the account before sending sensitive information, and applies a hash function on the user name and password before sending over the network. |
| NTLM | Available for HTTP explicit proxies only. Like Digest, used to confirm the account before sending sensitive information. Uses Windows credentials instead of the username and password. If you choose this option, enter the Active Directory domain that the proxy uses for authentication in the NTLM Domain field. Enter the name of the proxy workstation (also referred to as a workstation account or machine account) within the specified NTLM domain in the NTLM Workstation field. |

| Choose one of these options, depending on your call control environment and security requirements: Configure Unified CM Secure TLS SIP Traffic Routing for Video Mesh Configure Unified CM TCP SIP Traffic Routing for Video Mesh Configure Expressway TCP SIP Traffic Routing for Video Mesh (TCP only) SIP Devices Registered to Unified CM (TLS or TCP) Configure Unified CM with Video Mesh, using either TLS encrypted or TCP SIP traffic. You can create a trunk routing policy that reflects cluster preferences, and is highly available and resilient to device failures. If you use Unified CM Session Management Edition (SME), configure trunks on the Unified CM SME and leaf systems so that inbound and outbound calls are evenly distributed across the Unified CM servers within the Session Management cluster. Typically, each site will have a dedicated Unified CM cluster associated with it. These clusters will be connected through intercluster SIP trunks. Each cluster will have call-in trunks to the local site for the Video Mesh nodes. You can also configure your deployment to handle failure or overflow conditions. This configuration helps if there's an outage or if the Video Mesh clusters reached capacity. If the SIP meeting or call cannot be established with a cluster, the meeting or call will overflow to the cloud. SIP Devices Registered to VCS or Expressway (TCP Only) Configure neighbor zones and search rules to route SIP dial-in and dial-out for Cisco Webex meetings to Video Mesh clusters. SIP devices registered to a VCS Control or Expressway-C don't support direct reachability, so you must use a TCP-based Expressway configuration to establishes a relationship between on-premises SIP devices and your Video Mesh clusters. You can also configure your deployment to handle failure or overflow conditions. This configuration helps if there's an outage or if the Video Mesh clusters reached capacity. If the SIP meeting or call cannot be established with a cluster, the meeting or call will overflow to the cloud through the VCS Control/Expressway-C or an Expressway C/E pair. |
|---|

| 1 | Create a SIP profile for Video Mesh clusters: From Cisco Unified CM Administration, go to Device > Device Settings > SIP Profile , and then click Find . Choose Standard SIP Profile For Cisco VCS , and then click Copy . Enter a name for the new profile—for example, Video Mesh SIP Profile . Under Trunk Specific Configuration , set Early Offer support for voice and video calls to Best Effort (no MTP inserted) . You can apply this setting to a new SIP trunk to the Webex cloud (routed by the external domain for the Webex site). The setting does not affect any existing SIP trunking or call routing. Make sure that Enable OPTIONS Ping to monitor destination status for Trunks with Service Type is checked. Leave all other fields with their default values and save your changes. |
|---|---|
| 2 | Add a new SIP trunk security profile for Video Mesh clusters: From Cisco Unified CM Administration, choose System > Security > SIP Trunk Security Profile , and then click Add New . Enter a meaningful name, such as Video Mesh Secure SIP Trunk Security Profile Confirm these settings: Field Value Device Security Mode Encrypted Incoming Transport Type TLS Outgoing Transport Type TLS X.509 Subject Name Secure Certificate Subject or Subject Alternate Name Enter the common name of the Video Mesh node certificate. Incoming Port 5061 SIP V.150 Outbound SDP Offer Filtering Use Default Filter Leave all other fields with their default values and save your changes. | Field | Value | Device Security Mode | Encrypted | Incoming Transport Type | TLS | Outgoing Transport Type | TLS | X.509 Subject Name Secure Certificate Subject or Subject Alternate Name | Enter the common name of the Video Mesh node certificate. | Incoming Port | 5061 | SIP V.150 Outbound SDP Offer Filtering | Use Default Filter |
| Field | Value |
| Device Security Mode | Encrypted |
| Incoming Transport Type | TLS |
| Outgoing Transport Type | TLS |
| X.509 Subject Name Secure Certificate Subject or Subject Alternate Name | Enter the common name of the Video Mesh node certificate. |
| Incoming Port | 5061 |
| SIP V.150 Outbound SDP Offer Filtering | Use Default Filter |
| 3 | Add a new SIP trunk to point to your Video Mesh clusters: In a Unified CM-only deployment, add a single trunk. In an SME deployment, a trunk typically exists between Unified CM and SME. Add another trunk between SME and Video Mesh nodes. Both trunks must have the same settings specified below. From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New . Choose SIP Trunk for the trunk type; leave the other values and click Next . Enter a meaningful name, such as Video_Mesh_SIP_Trunk_UCMtoVMN . Check the SRTP Allowed check box For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex. Check Run On All Active Unified CM Nodes . Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Video Mesh nodes. Enter 5061 for the Destination Port . For the SIP Trunk Security Profile , choose the Video Mesh Trunk Security Profile that you created earlier. (For example, Video Mesh Secure SIP Trunk Security Profile .) For the SIP Profile , choose the Video Mesh SIP Profile that you created earlier. (For example, Video Mesh SIP Profile .) Leave all other fields with their default values and save your changes. A Video Mesh call or meeting might assign media to any node in a cluster, not just the node that terminates the SIP call. |
| 4 | Create a SIP trunk to point to an Expressway for Webex cloud failover. You can use a SIP trunk already in place for an existing Unified CM and Expressway deployment. If you create another one, and you also run Mobile Remote Access (MRA) with those Expressways, you can break MRA. From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New . Choose SIP Trunk for the trunk type; leave the other values and click Next . Enter a meaningful name, such as Video_Mesh_VCS_Trunk . For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex. Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Expressways. For the Port , enter 5060 . For SIP Profile , choose Standard SIP Profile For Cisco VCS . |
| 5 | Create a new route group for calls to Video Mesh clusters: From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New . Enter a meaningful name, such as Video Mesh Node Route Group . Change the Distribution Algorithm to Top Down . In the Route Group Member Information section, Find the Devices with name Video Mesh . Add Video_Mesh_SIP_Trunk_UCMtoVMN by clicking Add to Route Group . Save your changes. |
| 6 | For overflow to the cloud, create a new route group for calls to Expressway: From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New . Enter a meaningful name, such as Video Mesh Expressway Route Group . Change the Distribution Algorithm to Top Down . In the Route Group Member Information section, Find the Devices with name Video Mesh . Add Video_Mesh_VCS_Trunk by clicking Add to Route Group . Save your changes. |
| 7 | Create a new route list for calls to Video Mesh clusters and Expressway: From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List , and then click Add New . Enter a meaningful name, such as Video Mesh Node Route List . Set the Cisco Unified Communications Manager Group to Default , or another value depending on your configuration. Save your changes. In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Route Group . Leave the defaults for the other settings, and then save your changes. In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Expressway Route Group . Leave the defaults for the other settings, and then save your changes. |
| 8 | Create a SIP route pattern for the short video address dialing format for Webex meetings: From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route Pattern for Webex Short URIs . In the IPv4 pattern , enter webex.com as the domain. For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List . Leave all other fields with their default values and save your changes. With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number. |
| 9 | Create a SIP route pattern for the Webex site: From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route Pattern for Webex Sites . In the IPv4 pattern , enter the Webex site for which you want optimized media—For example, examplesitename.webex.com . For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List . Leave all other fields with their default values and save your changes. |
| 10 | Create a SIP route pattern for Webex App meetings (backwards compatibility): From Call Routing > SIP Route Pattern , click Add New , and then enter the name Video Mesh Route Pattern for Teams Meetings . In the IPv4 pattern , enter the meet.ciscospark.com . For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List . Leave all other fields with their default values and save your changes. |

| Field | Value |
|---|---|
| Device Security Mode | Encrypted |
| Incoming Transport Type | TLS |
| Outgoing Transport Type | TLS |
| X.509 Subject Name Secure Certificate Subject or Subject Alternate Name | Enter the common name of the Video Mesh node certificate. |
| Incoming Port | 5061 |
| SIP V.150 Outbound SDP Offer Filtering | Use Default Filter |

| 1 | Create a SIP profile for Video Mesh clusters: From Cisco Unified CM Administration, go to Device > Device Settings > SIP Profile , and then click Find . Choose Standard SIP Profile For Cisco VCS , and then click Copy . Enter a name for the new profile—for example, Video Mesh SIP Profile . Under Trunk Specific Configuration , set Early Offer support for voice and video calls to Best Effort (no MTP inserted) . You can apply this setting to a new SIP trunk to the Webex (routed by the external domain for the Webex site). The setting does not affect any existing SIP trunking or call routing. Make sure that Enable OPTIONS Ping to monitor destination status for Trunks with Service Type is checked. Leave all other fields with their default values and save your changes. |
|---|---|
| 2 | Add a new SIP trunk security profile for Video Mesh clusters: From Cisco Unified CM Administration, choose System > Security > SIP Trunk Security Profile , and then click Add New . Enter a meaningful name, such as Video Mesh Trunk Security Profile Confirm these settings: Field Value Device Security Mode Non Secure Incoming Transport Type TCP+UDP Outgoing Transport Type TCP Incoming Port 5060 SIP V.150 Outbound SDP Offer Filtering Use Default Filter Leave all other fields with their default values and save your changes. | Field | Value | Device Security Mode | Non Secure | Incoming Transport Type | TCP+UDP | Outgoing Transport Type | TCP | Incoming Port | 5060 | SIP V.150 Outbound SDP Offer Filtering | Use Default Filter |
| Field | Value |
| Device Security Mode | Non Secure |
| Incoming Transport Type | TCP+UDP |
| Outgoing Transport Type | TCP |
| Incoming Port | 5060 |
| SIP V.150 Outbound SDP Offer Filtering | Use Default Filter |
| 3 | Add a new SIP trunk to point to your Video Mesh clusters: In a Unified CM-only deployment, add a single trunk. In an SME deployment, a trunk typically exists between Unified CM and SME. Add another trunk between SME and Video Mesh nodes. Both trunks must have the same settings specified below. From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New . Choose SIP Trunk for the trunk type; leave the other values and click Next . Enter a meaningful name, such as Video_Mesh_SIP_Trunk_UCMtoVMN . For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex. Check Run On All Active Unified CM Nodes . Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Video Mesh nodes. Enter 5060 for the Destination Port . For the SIP Trunk Security Profile , choose the Video MeshTrunk Security Profile that you created earlier. (For example, Video Mesh Trunk Security Profile .) For the SIP Profile , choose the Video Mesh SIP Profile that you created earlier. (For example, Video Mesh SIP Profile .) Leave all other fields with their default values and save your changes. A Video Mesh call or meeting might assign media to any node in a cluster, not just the node that terminates the SIP call. |
| 4 | Create a new SIP trunk to point to an Expressway. You can use a SIP trunk already in place for an existing Unified CM and Expressway deployment. If you create another one, and you also run Mobile Remote Access (MRA) with those Expressways, you can break MRA. From Cisco Unified CM Administration, choose Device > Trunk , and then click Add New . Choose SIP Trunk for the trunk type; leave the other values and click Next . Enter a meaningful name, such as Video_Mesh_VCS_Trunk . For Calling and Connecting Party Info Format , check Deliver URI and DN in connected party, if available . This setting enables blended identity. It allows the SIP trunk to transmit the enterprise-side party's directory URI to Webex. Under SIP Information - Destination , enter an IP address or fully qualified domain name (FQDN) for each of your Expressways. For the Port , enter 5060 . For SIP Profile , choose Standard SIP Profile For Cisco VCS . |
| 5 | Create a new route group for calls to Video Mesh clusters: From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New . Enter a meaningful name, such as Video Mesh Node Route Group . Change the Distribution Algorithm to Top Down . In the Route Group Member Information section, Find the Devices with name Video Mesh . Add the Video_Mesh_SIP_Trunk_UCMtoVMN by clicking Add to Route Group . Save your changes. |
| 6 | For overflow to the cloud, create a new route group for calls to Expressway: From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group , and then click Add New . Enter a meaningful name, such as Video Mesh Expressway Route Group . Change the Distribution Algorithm to Top Down . In the Route Group Member Information section, Find the Devices with name Video Mesh . Add the Video_Mesh_VCS_Trunk by clicking Add to Route Group . Save your changes. |
| 7 | Create a new route list for calls to Video Mesh clusters and Expressway: From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List , and then click Add New . Enter a meaningful name, such as Video Mesh Node Route List . Set the Cisco Unified Communications Manager Group to Default , or another value depending on your configuration. Save your changes. In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Route Group . Leave the defaults for the other settings, and then save your changes. In the Route List Member Information section, click Add Route Group , and then choose Video Mesh Expressway Route Group . Leave the defaults for the other settings, and then save your changes. |
| 8 | Create a SIP route pattern for the short video address dialing format for Webex meetings: From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route
                                        Pattern for Webex Short URIs . In the IPv4 pattern , enter webex.com as the domain. For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List . Leave all other fields with their default values and save your
                            changes. With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number. |
| 9 | Create a SIP route pattern for the Webex site: From Call Routing > SIP Route Pattern , click Add New and enter the name Video Mesh Route
                                        Pattern for Webex Sites . In the IPv4 pattern , enter the Webex site for which you want
                            optimized media—For example, examplesitename.webex.com ,
                            where examplesitename is the name of your actual Webex
                            site. For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List . Leave all other fields with their default values and save your
                            changes. |
| 10 | Create a SIP route pattern for Webex App meetings: From Call Routing > SIP Route Pattern , click Add New , and then enter the name Video Mesh Route Pattern for Teams Meetings . In the IPv4 pattern , enter the meet.ciscospark.com . For SIP Trunk/Route List , choose the Route List created for Video Mesh—For example, Video Mesh Route List . Leave all other fields with their default values and save your changes. |

| Field | Value |
|---|---|
| Device Security Mode | Non Secure |
| Incoming Transport Type | TCP+UDP |
| Outgoing Transport Type | TCP |
| Incoming Port | 5060 |
| SIP V.150 Outbound SDP Offer Filtering | Use Default Filter |

| 1 | Create a zone that points to Video Mesh clusters: From VCS Control or Expressway-C, go to Configuration > Zones > Zones , and then click New . Configure the following fields: Field Name Value Name Enter a name that easily identifies the zone—for example, WebexVideoMeshZone Type Neighbor H.323 Mode Off SIP Mode On Port 5060 Transport TCP Location Look up peers by Address Peer [n] Address Enter the IP addresses for each Video Mesh node. Leave the other fields with their default settings, and then save your changes. | Field Name | Value | Name | Enter a name that easily identifies the zone—for example, WebexVideoMeshZone | Type | Neighbor | H.323 | Mode | Off | SIP | Mode | On | Port | 5060 | Transport | TCP | Location | Look up peers by | Address | Peer [n] Address | Enter the IP addresses for each Video Mesh node. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field Name | Value |
| Name | Enter a name that easily identifies the zone—for example, WebexVideoMeshZone |
| Type | Neighbor |
| H.323 |
| Mode | Off |
| SIP |
| Mode | On |
| Port | 5060 |
| Transport | TCP |
| Location |
| Look up peers by | Address |
| Peer [n] Address | Enter the IP addresses for each Video Mesh node. |
| 2 | Create  dial patterns for Video Mesh clusters for Webex sites: From Expressway-C, go to Configuration > Dial Plan > Search Rules , and then click New . Configure the following fields for the Webex site search rule: Field Name Value Rule Name Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-YourSite Priority 100 is the default. Ensure that this number is lower than the cloud fallback and B2B rules. Protocol SIP Mode Alias Pattern Match Pattern Type Regex Pattern String .*@(YourSite\.)?webex\.com.* This pattern matches both yoursite.webex.com and webex.com (for short video addresses) formats. With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number. Pattern Behavior Leave On Successful Match Continue Target Choose the Video Mesh zone that you created—for example, WebexVideoMeshZone . Leave the other fields with their default settings, and then save your changes. | Field Name | Value | Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-YourSite | Priority | 100 is the default. Ensure that this number is lower than the cloud fallback and B2B rules. | Protocol | SIP | Mode | Alias Pattern Match | Pattern Type | Regex | Pattern String | .*@(YourSite\.)?webex\.com.* This pattern matches both yoursite.webex.com and webex.com (for short video addresses) formats. With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number. | Pattern Behavior | Leave | On Successful Match | Continue | Target | Choose the Video Mesh zone that you created—for example, WebexVideoMeshZone . |
| Field Name | Value |
| Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-YourSite |
| Priority | 100 is the default. Ensure that this number is lower than the cloud fallback and B2B rules. |
| Protocol | SIP |
| Mode | Alias Pattern Match |
| Pattern Type | Regex |
| Pattern String | .*@(YourSite\.)?webex\.com.* This pattern matches both yoursite.webex.com and webex.com (for short video addresses) formats. With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number. |
| Pattern Behavior | Leave |
| On Successful Match | Continue |
| Target | Choose the Video Mesh zone that you created—for example, WebexVideoMeshZone . |
| 3 | Create a traversal client and zone pair that points to the cloud Expressway for failover: See the Expressway Basic Configuration Guide for your release for steps to create the traversal client and zone pair. |
| 4 | Create a fallback search rule to the Traversal Client Zone that leads to the Expressway-E: From Expressway-C, go to Configuration > Dial Plan > Search Rules , and then click New . Configure the following fields: Field Name Value Rule Name Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-Failover Priority 100 is the default. Ensure that the priority is lower by entering a number that is higher than the Video Mesh dial pattern and B2B rules. Protocol SIP Mode Any Alias Pattern Behavior Leave On Successful Match Continue Target Choose the Traversal Client Zone that leads to the Expressway-E. Leave the other fields with their default settings, and then save your changes. | Field Name | Value | Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-Failover | Priority | 100 is the default. Ensure that the priority is lower by entering a number that is higher than the Video Mesh dial pattern and B2B rules. | Protocol | SIP | Mode | Any Alias | Pattern Behavior | Leave | On Successful Match | Continue | Target | Choose the Traversal Client Zone that leads to the Expressway-E. |
| Field Name | Value |
| Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-Failover |
| Priority | 100 is the default. Ensure that the priority is lower by entering a number that is higher than the Video Mesh dial pattern and B2B rules. |
| Protocol | SIP |
| Mode | Any Alias |
| Pattern Behavior | Leave |
| On Successful Match | Continue |
| Target | Choose the Traversal Client Zone that leads to the Expressway-E. |
| 5 | From Expressway-E, go to Configuration > Zones > Zones . Click New and add the Webex Zone. In versions before X8.11, you created a new DNS zone for this purpose. |
| 6 | Create a dial pattern for the cloud Expressway: From Expressway-E, go to Configuration > Dial Plan > Search Rules , and then click New . Configure the following fields: Field Name Value Rule Name Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-toCloud Priority Enter a higher value than the rule for the local Video Mesh nodes. If the nodes are set to 100, set this value to 101 . You must also ensure that the value is lower than all B2B rules on your Expressway. Protocol SIP Source Named Source Name Choose the secure traversal server zone from Expressway-C—for example, WebexVideoMeshZone Mode Alias Pattern Match Pattern Type Regex Pattern String .*@(YourSite\.)?webex\.com.* Pattern Behavior Leave On Successful Match Stop Target Choose the Webex Zone or DNS zone. | Field Name | Value | Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-toCloud | Priority | Enter a higher value than the rule for the local Video Mesh nodes. If the nodes are set to 100, set this value to 101 . You must also ensure that the value is lower than all B2B rules on your Expressway. | Protocol | SIP | Source | Named | Source Name | Choose the secure traversal server zone from Expressway-C—for example, WebexVideoMeshZone | Mode | Alias Pattern Match | Pattern Type | Regex | Pattern String | .*@(YourSite\.)?webex\.com.* | Pattern Behavior | Leave | On Successful Match | Stop | Target | Choose the Webex Zone or DNS zone. |
| Field Name | Value |
| Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-toCloud |
| Priority | Enter a higher value than the rule for the local Video Mesh nodes. If the nodes are set to 100, set this value to 101 . You must also ensure that the value is lower than all B2B rules on your Expressway. |
| Protocol | SIP |
| Source | Named |
| Source Name | Choose the secure traversal server zone from Expressway-C—for example, WebexVideoMeshZone |
| Mode | Alias Pattern Match |
| Pattern Type | Regex |
| Pattern String | .*@(YourSite\.)?webex\.com.* |
| Pattern Behavior | Leave |
| On Successful Match | Stop |
| Target | Choose the Webex Zone or DNS zone. |
| 7 | For SIP devices registered to the Expressway-C, open the device IP address in a browser, go to Setup , scroll to SIP , and choose Standards from the Type drop-down. |

| Field Name | Value |
|---|---|
| Name | Enter a name that easily identifies the zone—for example, WebexVideoMeshZone |
| Type | Neighbor |
| H.323 |
| Mode | Off |
| SIP |
| Mode | On |
| Port | 5060 |
| Transport | TCP |
| Location |
| Look up peers by | Address |
| Peer [n] Address | Enter the IP addresses for each Video Mesh node. |

| Field Name | Value |
|---|---|
| Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-YourSite |
| Priority | 100 is the default. Ensure that this number is lower than the cloud fallback and B2B rules. |
| Protocol | SIP |
| Mode | Alias Pattern Match |
| Pattern Type | Regex |
| Pattern String | .*@(YourSite\.)?webex\.com.* This pattern matches both yoursite.webex.com and webex.com (for short video addresses) formats. With the short video address dialing feature, users no longer have to remember the Webex site name to join a Webex meeting or event using a video system. They can join the meeting faster because they only need to know the meeting or event number. |
| Pattern Behavior | Leave |
| On Successful Match | Continue |
| Target | Choose the Video Mesh zone that you created—for example, WebexVideoMeshZone . |

| Field Name | Value |
|---|---|
| Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-Failover |
| Priority | 100 is the default. Ensure that the priority is lower by entering a number that is higher than the Video Mesh dial pattern and B2B rules. |
| Protocol | SIP |
| Mode | Any Alias |
| Pattern Behavior | Leave |
| On Successful Match | Continue |
| Target | Choose the Traversal Client Zone that leads to the Expressway-E. |

| Field Name | Value |
|---|---|
| Rule Name | Enter a rule name that easily identifies the search rule—for example, WebexVideoMesh-toCloud |
| Priority | Enter a higher value than the rule for the local Video Mesh nodes. If the nodes are set to 100, set this value to 101 . You must also ensure that the value is lower than all B2B rules on your Expressway. |
| Protocol | SIP |
| Source | Named |
| Source Name | Choose the secure traversal server zone from Expressway-C—for example, WebexVideoMeshZone |
| Mode | Alias Pattern Match |
| Pattern Type | Regex |
| Pattern String | .*@(YourSite\.)?webex\.com.* |
| Pattern Behavior | Leave |
| On Successful Match | Stop |
| Target | Choose the Webex Zone or DNS zone. |

| 1 | Open the Video Mesh node interface (IP address/setup, for example, https://192.0.2.0/setup ) in your browser and sign in with the node's admin credentials. |
|---|---|
| 2 | Go to Server Certificates and request and upload a certificate and key pair as needed: (Optional) If you need a certificate issued from a certified provider, click Create a Certificate Signing Request . Fill out the required information (including the Subject Alternative Name(s) , which are FQDNs that must contain the common name, and then generate the request. Download the CSR to submit the request to the provider. (You can request multiple ones. They return the certificate authority (CA) signed certificate (the private key was already generated during the CSR creation step) The common name is not a URL. It doesn’t include any protocol (for example http:// or https://), port number, or pathname. The commonName field in the X.509 certificate specification represents the common name. For https://www.example.com , the correct value is example.com . The private key is already in place when you generate a CSR. If you don't use the CSR creation step, you must upload a private key. When you have the certificate and key, click Upload a Server Certificate (.crt or .pem file) , choose the certificate file, then click Upload a Private Key (.key file) and enter a passphrase if you have one. After you get the certificate, go to the first Video Mesh node in a cluster, click Install Server Certificate , read the prompt, click Install , then click OK . A cloud-registered Video Mesh node gracefully shuts down, waiting up to 2 hours for any calls to end. The node then completes the certificate installation. A prompt appears when the server certificate installs. You can then reload the page to view the new certificate and key entry. Click Download next to the certificate and key files to save a local copy. Save the files somewhere that's easy to remember and leave the Video Mesh instance open in the browser tab. Go to the next Video Mesh node in the cluster, fill in the passphrase, and then upload the private key file. Then click Upload a Server Certificate and then choose Install Server Certificate , read the prompt, click Install , then click OK . Repeat these steps for any Video Mesh nodes in the same cluster. |
| 3 | In another browser tab, from Cisco Unified OS Administration, go to Security > Certificate Management . Enter your search criteria and click Find , then choose the filename of the certificate or Certificate Trust List (CTL) and click Download . Save the Unified CM file somewhere that's easy to remember and leave Unified CM instance open in the browser tab. |
| 4 | Go back to the Video Mesh node interface tab, click Trust Store & Proxy , and then choose an option: If the Unified CM uses a CA certificate that's signed by a well-known organization, then the Video Mesh node trusts it automatically. The trust is based on the list of root certificates from the VMN node's host OS, which update periodically. If the Unified CM uses a CA certificate that's signed by an internal enterprise CA root certificate, add that root certificate to the node. That root certificate is available from within the enterprise, but might not be downloadable from Unified CM. Add both the ECDSA and RSA certificates that the Unified CM uses to serve external requests. These certificates can be self-signed or CA certificates. If you downloaded a single certificate, click Upload a Root Certificate or End Entity Certificate (.crt or .pem file) , and choose the CallManager.pem certificate file that you downloaded. Click Install All Certificates into the Trust Store , read the prompt, click Install , and then reboot the node. If you downloaded a certificate chain, upload the root CA certificate and intermediate CA certificate, and then click Install All Certificates into the Trust Store , read the prompt, and then click Install . A cloud-registered Video Mesh node gracefully shuts down, waiting up to 2 hours for any calls to end. To install the CallManager.pem certificate, the node automatically reboots. When it comes back online, a prompt appears when the CallManager.pem certificate installs on the Video Mesh node. You can then reload the page to view the new certificate. |
| 5 | Go back to the Cisco Unified OS Administration tab and click Upload Certificate/Certificate Chain . Choose the certificate name from the Certificate Purpose drop-down list, browse to the file that you downloaded from the Video Mesh node interface, and then click Open . |
| 6 | To upload the file to the server, click Upload File . If you're uploading a certificate chain, you must upload all certificates in the chain. Restart the affected service after uploading the certificate. When the server comes back up, you can access the CCMAdmin or CCMUser GUI to verify that your newly added certificates are in use. You can install and manage server certificates via APIs. For more information, see VMN Server Certificate APIs . |

| Settings | Result |
|---|---|
| Unified CM is configured with a secure trunk and this Video Mesh Control Hub setting is not enabled. | Calls fail. |
| Unified CM is not configured with a secure trunk and this Video Mesh Control Hub setting is enabled. | Calls won't fail but they fall back to non-secure mode. |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click Edit Settings on the Video Mesh card. |
|---|---|
| 2 | Scroll to Media Encryption and toggle on the setting. This setting makes encryption mandatory on all media channels that pass
                        through Video Mesh nodes in your organization. Note the preceding table and
                        caution note for situations where calls may fail and what's required for
                        end-to-end encryption to work. |
| 3 | Click Resources and repeat the following steps on each Video Mesh cluster that you want to enable for secure SIP traffic. Select a Video Mesh cluster entry in the list, and then click Cluster settings . Scroll to the SIP TLS Configuration card. Under Trusted SIP sources , ﻿enter the Common Name (CN) or any FQDNs that are present in the Subject Alternative Name on the Unified CM certificate (typically the FQDN of the Unified CM). These entries are identified as trusted SIP sources and are allowed to send secure SIP calls to Webex Video Mesh. The Trusted SIP sources field will be greyed out unless Media Encryption is enabled for the organization, as detailed in the previous step. |

| 1 | From the customer view in https://admin.webex.com , go to Services > Meetings , click the Webex site from the Meetings card, and then click Settings to access the the Webex site configuration options. |
|---|---|
| 2 | Access Common Settings by clicking on Service > Meeting > Site Settings . From Common Settings , click Cloud Collaboration Meeting Rooms (CMR) , choose Video Mesh for Media Resource Type , and then click Save at the bottom. This setting links Video Mesh and meeting instances in the cloud together and allows cascades to occur from Video Mesh nodes. The setting should populate across your environment after 15 minutes. Webex meetings that start after this change is populated will pick up the new setting. If you leave this field set to Cloud (the default option), all meetings are hosted in the cloud and the Video Mesh node is not used. |

| 1 | Join a meeting from the secured endpoint. |
|---|---|
| 2 | Verify that the meeting roster list appears on the device. This example shows how the meeting list looks on an endpoint with a touch panel: |
| 3 | During the meeting, access the Webex Conference information from Call Details . |
| 4 | Verify that Encryption section shows the Type as AES-128 and the Status as On . |

## Figuras

![Example Deployment of Video Mesh with Distributed Unified CM](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/420001-430000/421001-422000/421007.jpg)

![Settings button represented by a cog icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/410001-420000/414001-415000/414887.jpg)

![Cloud collaboration meeting room options with the media resource type dropwdown expanded to select Video mesh](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/420001-430000/427001-428000/427242.jpg)

![Webex Conference meeting window displaying three participants](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/433001-434000/433504.jpg)

![Webex Conference secure endpoint meeting information displaying details and encryption box selected with Type AES-128 and Status as ON](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/433001-434000/433503.jpg)