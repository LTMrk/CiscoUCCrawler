---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-installation-guide-vvb-b-inst-412cc2b29a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/installation/guide/vvb_b_install-and-upgrade-guide-12-5/vvb_b_install-and-upgrade-guide-12-5_chapter_011.html
retrieved_at: 2026-08-21T16:27:47.838263+00:00
---

Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

# Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

Updated: August 24, 2023

Chapter: Cisco VVB Installation on KVM

## Chapter: Cisco VVB Installation on KVM

- Cisco VVB Installation on KVM

- Install Cisco VVB on KVM

# Cisco VVB Installation on KVM

## Install Cisco VVB on KVM

### Before you begin

Download Cisco VVB OVA template from CCO. Read the OVA's readme file before you create a virtual machine using the OVA.

For hardware requirements, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html .

Step 1

Copy the OVA image from FTP/TFTP server to the router by running:

copy ftp harddisk

### Example:

```
router# copy ftp harddisk: Address or name of remote host [10.10.10.10]?
Source filename [ag2.xml]? VVB_12_5_1_ISR4K.ova
Destination filename [VVB_12_5_1_ISR4K.ova]?
Accessing ftp://10.10.10.10/VVB_12_5_1_ISR4K.ova...
Loading VVB_12_5_1_ISR4K.ova !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[OK - -1055619072/4096 bytes]
```

Step 2

Install the package by running:

virtual-service install name <name> package <uri:.ova>

The package name is case-sensitive.

### Example:

```
router# virtual-service install name vvb package harddisk:VV router# virtual-service install name vvb package harddisk:VVB-12-5-1-ISR4K.ova Installing package 'harddisk:/VVB-12-5-1-ISR4K.ova' for virtual-service 'vvb'. 
Once the install has finished, the VM may be activated. 
Use 'show virtual-service list' for progress.
router# show virtual-service list System busy installing virtual-service 'vvb'. The request may take several minutes... 
Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 12.5(1) 15 
Virtual Service List: 
Name 		Status 		Package Name
 ------------------------------------------------------------------------------ 
vvb 			Installing 		VVB-12-5-1-ISR4K.ova

router#show virtual-service list
Virtual Service List:

Name                    Status             Package Name
------------------------------------------------------------------------------
vvb                     Installed          VVB-12-5-1-ISR4K.ova
```

Step 3

Configure VirtualPortGroup Interface by running:

interface VirtualPortGroup <interface number>

ip unnumbered <interface type> <interface number>

### Example:

```
router# config t Enter configuration commands, one per line.  End with CNTL/Z.
router(config)# interface VirtualPortGroup1 router(config-if)# ip unnumbered GigabitEthernet0/0/0 router(config-if)# end router# show ip int brief | sec VirtualPortGroup1 VirtualPortGroup1      10.10.10.58    YES unset  up        up
```

The virtual-service name is case-sensitive and must match the name given in Step 2.

The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet.

This VirtualPortGroup1 interface acts as the default gateway for the VM.

Step 4

Configure the service by running:

virtual-service <name>

### Example:

```
1. Get into the virtual-service config mode by running:
conf t
<enter>

2. Assign VirtualPortGroup Interface as gateway to connect to guest virtual-service/VM
router# config t router(config)# virtual-service vvb router(config-virt-serv)# vnic gateway VirtualPortGroup1 router(config-virt-serv-vnic)# guest ip address 10.10.10.59 router(config-virt-serv-vnic)#
router(config-virt-serv-vnic)#!!! 10.00.00.000 will be the IP of the VM!!!
router(config-virt-serv-vnic)# exit vnic gateway VirtualPortGroup <interface number><enter>
```

The virtual-service name is case-sensitive and must match the name given in Step 2.

The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet.

Step 5

Add the static IP route for the guest VM instance by running:

ip route <VM IP address> <subnet mask> <VirtualPortGroup Interface>

### Example:

```
router# config t Enter configuration commands, one per line.  End with CNTL/Z.
router(config)# ip route 10.10.10.10 255.255.255.0 VirtualPortGroup1 router(config)#!!!! 10.10.10.10 will be Guest/VM  IP !!!!!!!
```

This is to make sure that the assigned VirtualPortGroup interface is the gateway for only this specific IP address in the
                                                      network.

Step 6

Activate the service by running:

activate

### Example:

```
router# config t Enter configuration commands, one per line.  End with CNTL/Z.
router(config)# virtual-service vvb router(config-virt-serv)# activate % Activating virtual-service 'vvb', this might take a few minutes. Use 'show virtual-service list' 
for progress.
router(config-virt-serv)# end router# show virtual-service list System busy activating virtual-service 'vvb'. The request may take several minutes...
Virtual Service List:
Name                    Status             Package Name
------------------------------------------------------------------------------
vvb                     Activating         VVB_12_5_1_ISR4K.ova
 
router# show virtual-service list Virtual Service List:
Name                    Status             Package Name
------------------------------------------------------------------------------
vvb                     Activated          VVB_12_5_1_ISR4K.ova
```

The virtual-service name is case-sensitive and must match the name given in Step 2.

Step 7

Connect to the virtual service console by running:

virtual-service connect name <name> console

### Example:

```
router# virtual-service connect name vvb console Connected to appliance. Exit using ^c^c^c
Cisco Virtualized Voice Browser <11.x.x>
vvbkvm login:

Default credentials: administrator/C!sco123
```

This may take 2-3 minutes to connect to the console.

Step 8

Change the hostname and the IP address by running:

set network hostname

### Example:

```
Host name Change: 

Login to administrator 
admin: set network hostname ctrl-c: To quit the input. 
         ***   W A R N I N G   *** 
Do not close this window without first canceling the command. 
This command will automatically restart system services. 
The command should not be issued during normal operating 
hours. 
======================================================= 
 Note: Please verify that the new hostname is a unique 
       name across the cluster and, if DNS services are 
       utilized, any DNS configuration is completed 
       before proceeding. 
======================================================= 
Security Warning : This operation will regenerate 
       all UCCX Certificates including any third party 
       signed Certificates that have been uploaded. 
Enter the hostname: vvbkvm Would you like to change the network ip address at this time [yes]: yes Warning: Do not close this window until command finishes. 
ctrl-c: To quit the input.

           ***   W A R N I N G   ***
=======================================================
 Note: Please verify that the new ip address is unique
       across the cluster.
=======================================================

Enter the ip address:: 10.78.0.00 Enter the ip subnet mask:: 255.255.255.0 Enter the ip address of the gateway:: 10.78.0.1 Hostname: vvbkvm IP Address: 10.78.0.00 Subnet Mask: 255.255.255.0 Gateway: 10.78.0.1 Do you want to continue [yes/no]? yes calling 1 of 8 component notification script: acluster_healthcheck.sh 
calling 2 of 8 component notification script: adpuccx_IP_HostName_change.sh 
calling 3 of 8 component notification script: ahostname_callback.sh 
Info(0): Processnode query returned using kvmvvb: 
name 
====== 
kvmvvb 
updating server table from:'kvmvvb', to: 'vvbkvm' 
Rows: 1 
updating database, please wait 90 seconds 
updating database, please wait 60 seconds 
updating database, please wait 30 seconds 
calling 4 of 8 component notification script: drf_notify_hostname_change.py 
calling 5 of 8 component notification script: hosts_mgr.sh 
calling 6 of 8 component notification script: idsLocalPrefsUpdateFile.sh 
Going to trigger /usr/bin/python /usr/local/cm/lib/dblupdatefiles-plugin.py -f=vvbkvm,kvmvvb 
calling 7 of 8 component notification script: regenerate_all_certs.sh 
calling 8 of 8 component notification script: update_idsenv.sh 
System services will restart in 1 minute
admin: utils system restart
```

Changing the hostname fails if the hostname includes any of these wildcard characters: “.”, “_” , “@”, “!”,”#”, “$”, “%”

Engine takes around 5 minutes to be in service after the server comes back up.

API and configuration services take around 10 minutes to be in service.

Step 9

Validate Cisco VVB services.

Log in to VVB administrator using appadmin credentials.

Go to Cisco VVB serviceability.

Check if the services are up and running.

| Step 1 | Copy the OVA image from FTP/TFTP server to the router by running: copy ftp harddisk Example: router# copy ftp harddisk: Address or name of remote host [10.10.10.10]?
Source filename [ag2.xml]? VVB_12_5_1_ISR4K.ova
Destination filename [VVB_12_5_1_ISR4K.ova]?
Accessing ftp://10.10.10.10/VVB_12_5_1_ISR4K.ova...
Loading VVB_12_5_1_ISR4K.ova !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[OK - -1055619072/4096 bytes] |
|---|---|
| Step 2 | Install the package by running: virtual-service install name <name> package <uri:.ova> Note The package name is case-sensitive. Example: router# virtual-service install name vvb package harddisk:VV router# virtual-service install name vvb package harddisk:VVB-12-5-1-ISR4K.ova Installing package 'harddisk:/VVB-12-5-1-ISR4K.ova' for virtual-service 'vvb'. 
Once the install has finished, the VM may be activated. 
Use 'show virtual-service list' for progress.
router# show virtual-service list System busy installing virtual-service 'vvb'. The request may take several minutes... 
Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 12.5(1) 15 
Virtual Service List: 
Name 		Status 		Package Name
 ------------------------------------------------------------------------------ 
vvb 			Installing 		VVB-12-5-1-ISR4K.ova

router#show virtual-service list
Virtual Service List:

Name                    Status             Package Name
------------------------------------------------------------------------------
vvb                     Installed          VVB-12-5-1-ISR4K.ova | Note | The package name is case-sensitive. |
| Note | The package name is case-sensitive. |
| Step 3 | Configure VirtualPortGroup Interface by running: interface VirtualPortGroup <interface number> ip unnumbered <interface type> <interface number> Example: router# config t Enter configuration commands, one per line.  End with CNTL/Z.
router(config)# interface VirtualPortGroup1 router(config-if)# ip unnumbered GigabitEthernet0/0/0 router(config-if)# end router# show ip int brief \| sec VirtualPortGroup1 VirtualPortGroup1      10.10.10.58    YES unset  up        up Note The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. This VirtualPortGroup1 interface acts as the default gateway for the VM. | Note | The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. This VirtualPortGroup1 interface acts as the default gateway for the VM. |
| Note | The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. This VirtualPortGroup1 interface acts as the default gateway for the VM. |
| Step 4 | Configure the service by running: virtual-service <name> Example: 1. Get into the virtual-service config mode by running:
conf t
<enter>

2. Assign VirtualPortGroup Interface as gateway to connect to guest virtual-service/VM
router# config t router(config)# virtual-service vvb router(config-virt-serv)# vnic gateway VirtualPortGroup1 router(config-virt-serv-vnic)# guest ip address 10.10.10.59 router(config-virt-serv-vnic)#
router(config-virt-serv-vnic)#!!! 10.00.00.000 will be the IP of the VM!!!
router(config-virt-serv-vnic)# exit vnic gateway VirtualPortGroup <interface number><enter> Note The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. | Note | The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. |
| Note | The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. |
| Step 5 | Add the static IP route for the guest VM instance by running: ip route <VM IP address> <subnet mask> <VirtualPortGroup Interface> Example: router# config t Enter configuration commands, one per line.  End with CNTL/Z.
router(config)# ip route 10.10.10.10 255.255.255.0 VirtualPortGroup1 router(config)#!!!! 10.10.10.10 will be Guest/VM  IP !!!!!!! Note This is to make sure that the assigned VirtualPortGroup interface is the gateway for only this specific IP address in the
                                                      network. | Note | This is to make sure that the assigned VirtualPortGroup interface is the gateway for only this specific IP address in the
                                                      network. |
| Note | This is to make sure that the assigned VirtualPortGroup interface is the gateway for only this specific IP address in the
                                                      network. |
| Step 6 | Activate the service by running: activate Example: router# config t Enter configuration commands, one per line.  End with CNTL/Z.
router(config)# virtual-service vvb router(config-virt-serv)# activate % Activating virtual-service 'vvb', this might take a few minutes. Use 'show virtual-service list' 
for progress.
router(config-virt-serv)# end router# show virtual-service list System busy activating virtual-service 'vvb'. The request may take several minutes...
Virtual Service List:
Name                    Status             Package Name
------------------------------------------------------------------------------
vvb                     Activating         VVB_12_5_1_ISR4K.ova
 
router# show virtual-service list Virtual Service List:
Name                    Status             Package Name
------------------------------------------------------------------------------
vvb                     Activated          VVB_12_5_1_ISR4K.ova Note The virtual-service name is case-sensitive and must match the name given in Step 2. | Note | The virtual-service name is case-sensitive and must match the name given in Step 2. |
| Note | The virtual-service name is case-sensitive and must match the name given in Step 2. |
| Step 7 | Connect to the virtual service console by running: virtual-service connect name <name> console Example: router# virtual-service connect name vvb console Connected to appliance. Exit using ^c^c^c
Cisco Virtualized Voice Browser <11.x.x>
vvbkvm login:

Default credentials: administrator/C!sco123 Note This may take 2-3 minutes to connect to the console. | Note | This may take 2-3 minutes to connect to the console. |
| Note | This may take 2-3 minutes to connect to the console. |
| Step 8 | Change the hostname and the IP address by running: set network hostname Example: Host name Change: 

Login to administrator 
admin: set network hostname ctrl-c: To quit the input. 
         ***   W A R N I N G   *** 
Do not close this window without first canceling the command. 
This command will automatically restart system services. 
The command should not be issued during normal operating 
hours. 
======================================================= 
 Note: Please verify that the new hostname is a unique 
       name across the cluster and, if DNS services are 
       utilized, any DNS configuration is completed 
       before proceeding. 
======================================================= 
Security Warning : This operation will regenerate 
       all UCCX Certificates including any third party 
       signed Certificates that have been uploaded. 
Enter the hostname: vvbkvm Would you like to change the network ip address at this time [yes]: yes Warning: Do not close this window until command finishes. 
ctrl-c: To quit the input.

           ***   W A R N I N G   ***
=======================================================
 Note: Please verify that the new ip address is unique
       across the cluster.
=======================================================

Enter the ip address:: 10.78.0.00 Enter the ip subnet mask:: 255.255.255.0 Enter the ip address of the gateway:: 10.78.0.1 Hostname: vvbkvm IP Address: 10.78.0.00 Subnet Mask: 255.255.255.0 Gateway: 10.78.0.1 Do you want to continue [yes/no]? yes calling 1 of 8 component notification script: acluster_healthcheck.sh 
calling 2 of 8 component notification script: adpuccx_IP_HostName_change.sh 
calling 3 of 8 component notification script: ahostname_callback.sh 
Info(0): Processnode query returned using kvmvvb: 
name 
====== 
kvmvvb 
updating server table from:'kvmvvb', to: 'vvbkvm' 
Rows: 1 
updating database, please wait 90 seconds 
updating database, please wait 60 seconds 
updating database, please wait 30 seconds 
calling 4 of 8 component notification script: drf_notify_hostname_change.py 
calling 5 of 8 component notification script: hosts_mgr.sh 
calling 6 of 8 component notification script: idsLocalPrefsUpdateFile.sh 
Going to trigger /usr/bin/python /usr/local/cm/lib/dblupdatefiles-plugin.py -f=vvbkvm,kvmvvb 
calling 7 of 8 component notification script: regenerate_all_certs.sh 
calling 8 of 8 component notification script: update_idsenv.sh 
System services will restart in 1 minute
admin: utils system restart Note Changing the hostname fails if the hostname includes any of these wildcard characters: “.”, “_” , “@”, “!”,”#”, “$”, “%” Engine takes around 5 minutes to be in service after the server comes back up. API and configuration services take around 10 minutes to be in service. | Note | Changing the hostname fails if the hostname includes any of these wildcard characters: “.”, “_” , “@”, “!”,”#”, “$”, “%” Engine takes around 5 minutes to be in service after the server comes back up. API and configuration services take around 10 minutes to be in service. |
| Note | Changing the hostname fails if the hostname includes any of these wildcard characters: “.”, “_” , “@”, “!”,”#”, “$”, “%” Engine takes around 5 minutes to be in service after the server comes back up. API and configuration services take around 10 minutes to be in service. |
| Step 9 | Validate Cisco VVB services. Log in to VVB administrator using appadmin credentials. Go to Cisco VVB serviceability. Check if the services are up and running. |

| Note | The package name is case-sensitive. |
|---|---|

| Note | The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. This VirtualPortGroup1 interface acts as the default gateway for the VM. |
|---|---|

| Note | The virtual-service name is case-sensitive and must match the name given in Step 2. The IP address of the router/VirtualPortGroup Interface and the guest/VM must be on the same subnet. |
|---|---|

| Note | This is to make sure that the assigned VirtualPortGroup interface is the gateway for only this specific IP address in the
                                                      network. |
|---|---|

| Note | The virtual-service name is case-sensitive and must match the name given in Step 2. |
|---|---|

| Note | This may take 2-3 minutes to connect to the console. |
|---|---|

| Note | Changing the hostname fails if the hostname includes any of these wildcard characters: “.”, “_” , “@”, “!”,”#”, “$”, “%” Engine takes around 5 minutes to be in service after the server comes back up. API and configuration services take around 10 minutes to be in service. |
|---|---|