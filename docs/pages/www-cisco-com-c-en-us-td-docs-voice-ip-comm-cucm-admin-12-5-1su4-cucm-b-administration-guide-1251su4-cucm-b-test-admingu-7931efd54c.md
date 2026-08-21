---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-administration-guide-1251su4-cucm-b-test-admingu-7931efd54c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_administration-guide-1251su4/cucm_b_test-adminguide_chapter_011110.html
retrieved_at: 2026-08-21T16:02:25.087797+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: April 8, 2025

Chapter: IP Address and Hostname Changes

## Chapter: IP Address and Hostname Changes

# IP Address and Hostname Changes

## Change IP Address
                        	 and Hostname Task List

The following table lists the tasks to perform to change the IP address and hostname for Unified Communications Manager and IM and Presence Service nodes.

Item

Task

1

Perform
                                          					 the pre-change tasks and system health checks.

2

Change the
                                          					 IP address or hostname for the node using either the Command Line Interface
                                          					 (CLI) or the Unified Operating System GUI.

For IM and Presence Service nodes, observe the following conditions:

Change the IP address and hostname for the database publisher node before you change any subscriber nodes.

You can change the IP address and hostname for all subscriber nodes simultaneously or one at a time.

3

Perform
                                          					 the post-change tasks.

## Change IP Address or Hostname Through OS Admin GUI

You can use Cisco Unified Operating System Administration to change the IP address or hostname for publisher and subscriber
                              nodes that are defined by a hostname in your deployment. Unless otherwise stated, each step in this procedure applies to both
                              publisher and subscriber nodes on Unified Communications Manager and IM and Presence Service clusters.

Changing the hostname through set network hostname command triggers an automatically self-signed certificate regeneration. This causes all devices in the cluster to reset so
                              that they can download an updated ITL file. If your cluster is using CA-signed certificates, you need to have them re-signed.

Changing only the IP address using the set network hostname command causes all devices in the cluster to reset so that they can download an updated ITL file. Certificates are not updated.

Caution

Through Cisco Unified Operating System Administration, we recommend that you change only one of these settings at a time.
                                                To change both the IP address and hostname at the same time, use the CLI command set network hostname .

If the Unified Communications Manager cluster security is operating in mixed mode, secure connections to this node will fail after changing the hostname, or IP
                                                address until you run the CTL client and update the CTL file or run utils ctl update CTLFile if you used the tokenless CTL feature.

### Before you begin

Perform the
                              		  pre-change tasks and system health checks on your deployment.

Step 1

From Cisco
                                       			 Unified Operating System Administration, select Settings > IP > Ethernet

Step 2

Change the
                                       			 hostname, IP address, and if necessary, the default gateway.

Step 3

Click Save .

Changing the hostname triggers an automatically self-signed certificate regeneration and causes all devices in the cluster
                                          to reset so they can download an updated ITL file. Changing the hostname does not trigger the ITL recovery certificates regeneration.

### What to do next

Perform all
                              		  applicable post-change tasks to ensure that your changes are properly
                              		  implemented in your deployment.

Do not proceed
                                          			 if the new hostname does not resolve to the correct IP address.

If your cluster is using CA-signed certificates, you need to have them re-signed.

Run the CTL Client to
                              		  update the CTL file if you used that process to put your cluster into mixed
                              		  mode. If you used the tokenless CTL feature, then run the CLI command utils ctl
                                 			 update CTLFile

## Change IP Address or Hostname Through Unified CM Administration GUI

You can use Cisco Unified CM Administration to change the IP address or hostname, which is defined in the database, for the
                              publisher and subscriber nodes. Doing this ensures that the hostname entries are uniform with the system-defined hostname
                              or IP values.

Changing the IP address or hostname triggers an automatically self-signed certificate regeneration. This causes all devices in the cluster to reset
                              so that they can download an updated ITL file. If your cluster is using CA-signed certificates, you must have them re-signed.

Caution

A change of the hostname or IP address requires the system services to be restarted. Hence, refrain from making this change
                                                during normal operating hours.

Through Cisco Unified CM Administration, we recommend that you change only one of these settings at a time. To change both
                                                the IP address and hostname at the same time, use the CLI command set network hostname .

If the Unified Communications Manager cluster security is operating in mixed mode, secure connections to this node will fail after changing the hostname, or IP
                                                address until you run the CTL client and update the CTL file or run utils ctl update CTLFile if you used the tokenless CTL feature.

If the hostname or IP address that is defined on the Cisco Unified OS Administration and Cisco Unified CM Administration pages
                                                do not match, the applications are unable to fetch the correct phone status. Also, due to certificate mismatch, TLS handshake
                                                fails. Hence, ensure that the IP address and hostname entries in both the Cisco Unified OS Administration and the Cisco Unified
                                                CM Administration pages are alike.

### Before you begin

Perform the prechange tasks and system health checks on your deployment.

Step 1

From Cisco Unified CM Administration, choose System > Server .

The Find and List Servers window appears.

Step 2

To get a list of all servers, click Find .

Step 3

From the list, click the server for which you want to modify the hostname.

Step 4

In the Host Name/IP Address* field, enter the new host name or the IP address and click Save .

Step 5

Using the Admin CLI GUI, reboot the node using the utils system restart CLI command.

## Change IP Address or Hostname Through CLI

You can use the CLI to change the IP address or hostname for publisher and subscriber nodes that are defined by a hostname
                              in your deployment. Unless otherwise stated, each step in this procedure applies to both publisher and subscriber nodes on
                              Cisco Unified Communication Manager and IM and Presence Service clusters.

Changing the hostname triggers an automatically self-signed certificate regeneration. This causes all devices in the cluster
                              to reset so that they can download an updated ITL file. If your cluster is using CA-signed certificates, you must have them
                              re-signed. Changing the hostname does not trigger the ITL recovery certificates regeneration.

Caution

If the Cisco Unified Communications Manager cluster security is operating in mixed mode, secure connections to this node will
                                          fail after changing the hostname, or IP address until you run the CTL client and update the CTL file or run utils ctl update CTLFile if you used the tokenless CTL feature.

### Before you begin

Perform the
                              		  pre-change tasks and system health checks on your deployment.

Step 1

Log in to the CLI of the node that you want to change.

Step 2

Enter set network
                                             				  hostname .

Step 3

Follow the
                                       			 prompts to change the hostname, IP address, or default gateway.

Enter the
                                             				  new hostname and press Enter .

Enter yes if you
                                             				  also want to change the IP address; otherwise, go to Step 4.

Enter the
                                             				  new IP address.

Enter the
                                             				  subnet mask.

Enter the
                                             				  address of the gateway.

Step 4

Verify that
                                       			 all your input is correct and enter yes to start
                                       			 the process.

### What to do next

Perform all
                              		  applicable post-change tasks to ensure that your changes are properly
                              		  implemented in your deployment.

Do not proceed
                                          			 if the new hostname does not resolve to the correct IP address.

If your cluster is using CA-signed certificates, you must have them re-signed.

Run the CTL Client to update the CTL file if you used that process to put your cluster into mixed mode. If you used the tokenless
                              CTL feature, then run the CLI command utils ctl update CTLFile

### Example CLI Output
                           	 for Set Network Hostname

```
admin:set network hostname 

ctrl-c: To quit the input.

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
       all CUCM Certificates including any third party
       signed Certificates that have been uploaded. 
    
Enter the hostname:: newHostname

Would you like to change the network ip address at this time [yes]:: 

Warning: Do not close this window until command finishes.

    

ctrl-c: To quit the input.

           ***   W A R N I N G   ***
=======================================================
 Note: Please verify that the new ip address is unique 
       across the cluster.
=======================================================
    
Enter the ip address:: 10.10.10.28
Enter the ip subnet mask:: 255.255.255.0
Enter the ip address of the gateway:: 10.10.10.1
Hostname:       newHostname				
IP Address:     10.10.10.28
IP Subnet Mask: 255.255.255.0
Gateway:        10.10.10.1

Do you want to continue [yes/no]? yes 

calling 1 of 5 component notification script: ahostname_callback.sh		
Info(0): Processnode query returned =
name       
========== 
bldr-vcm18 
updating server table from:'oldHostname', to: 'newHostname'
Rows: 1
updating database, please wait 90 seconds
updating database, please wait 60 seconds
updating database, please wait 30 seconds
Going to trigger /usr/local/cm/bin/dbl updatefiles --remote=newHostname,oldHostname 
calling 2 of 5 component notification script: clm_notify_hostname.sh		notification
Verifying update across cluster nodes...
platformConfig.xml is up-to-date: bldr-vcm21

cluster update successfull
calling 3 of 5 component notification script: drf_notify_hostname_change.py 	
calling 4 of 5 component notification script: regenerate_all_certs.sh		
calling 5 of 5 component notification script: update_idsenv.sh 		
calling 1 of 2 component notification script: ahostname_callback.sh 		
Info(0): Processnode query returned =
name 
==== 
Going to trigger /usr/local/cm/bin/dbl updatefiles --remote=10.10.10.28,10.67.142.24
calling 2 of 2 component notification script: clm_notify_hostname.sh		 
Verifying update across cluster nodes...
Shutting down interface eth0:
```

## Change IP Address
                        	 Only

You can change the
                              		  IP address of a node
                              		  by using the CLI.

If the node is defined by hostname or FQDN, you must update only the DNS before you make the change (if DNS is used).

For IM and Presence Service :

Change and
                                                				  verify the IM and Presence database publisher node first.

You can change the IM and Presence
                                                   				  Service subscriber nodes simultaneously or one at a time.

### Before you begin

Perform the
                              		  pre-change tasks and system health checks on your deployment.

Step 1

Log in to the CLI of the node that you want to change.

Step 2

Enter set network ip eth0 new-ip_address new_netmask new_gateway to change the IP address of the node.

where new_ip_address specifies the new server IP address, new_netmask specifies the new server network mask and new_gateway specifies the gateway address.

The following output displays:

```
admin:set network ip eth0 10.53.57.101 255.255.255.224 10.53.56.1 

WARNING: Changing this setting will invalidate software license 
on this server. The license will have to be re-hosted. 

Continue (y/n)?
```

Step 3

Verify the
                                       			 output of the CLI command. Enter yes , and then
                                       			 press Enter to start the process.

### What to do next

Perform all
                              		  applicable post-change tasks to ensure that your changes are properly
                              		  implemented in your deployment.

### Example Output for Set Network IP Address

```
admin:set network ip eth0 10.77.30.34 255.255.255.0 10.77.30.1

           ***   W A R N I N G   ***

This command will restart system services
=======================================================
 Note: Please verify that the new ip address is unique
       across the cluster and, if DNS services are
       utilized, any DNS configuration is completed
       before proceeding.
=======================================================

Continue (y/n)?y
calling 1 of 6 component notification script: acluster_healthcheck.sh
calling 2 of 6 component notification script: adns_verify.sh
No Primary DNS server defined
No Secondary DNS server defined
calling 3 of 6 component notification script: aetc_hosts_verify.sh
calling 4 of 6 component notification script: afupdateip.sh
calling 5 of 6 component notification script: ahostname_callback.sh
Info(0): Processnode query returned using 10.77.30.33:
name
====
calling 6 of 6 component notification script: clm_notify_hostname.sh
```

## Change DNS IP Address Using CLI

You can use CLI to change the DNS IP Address for publisher and subscriber nodes in your deployment. This procedure applies
                              to both publisher and subscriber nodes on Unified Communications Manager and IM and Presence Service clusters.

### Before you begin

Step 1

Log in to the CLI of the node that you want to change.

Step 2

Enter set network dns primary/secondary <new IP address of the DNS>

The following ouput displays:

```
admin:set network dns primary/secondary <new IP address of DNS>
*** W A R N I N G ***
This will cause the system to temporarily lose network connectivity
```

Step 3

Verify the output of the CLI command. Enter Yes and then press Enter to start the process.

| Item | Task |
|---|---|
| 1 | Perform
                                          					 the pre-change tasks and system health checks. |
| 2 | Change the
                                          					 IP address or hostname for the node using either the Command Line Interface
                                          					 (CLI) or the Unified Operating System GUI. For IM and Presence Service nodes, observe the following conditions: Change the IP address and hostname for the database publisher node before you change any subscriber nodes. You can change the IP address and hostname for all subscriber nodes simultaneously or one at a time. Note After you change the IP address or hostname of an IM and Presence Service node, you must change the Destination Address value for the SIP publish trunk on Unified Communications Manager . See the post-change task list. | Note | After you change the IP address or hostname of an IM and Presence Service node, you must change the Destination Address value for the SIP publish trunk on Unified Communications Manager . See the post-change task list. |
| Note | After you change the IP address or hostname of an IM and Presence Service node, you must change the Destination Address value for the SIP publish trunk on Unified Communications Manager . See the post-change task list. |
| 3 | Perform
                                          					 the post-change tasks. |

| Note | After you change the IP address or hostname of an IM and Presence Service node, you must change the Destination Address value for the SIP publish trunk on Unified Communications Manager . See the post-change task list. |
|---|---|

| Note | Changing the hostname does not trigger the ITL recovery certificates regeneration. |
|---|---|

| Caution | Through Cisco Unified Operating System Administration, we recommend that you change only one of these settings at a time.
                                                To change both the IP address and hostname at the same time, use the CLI command set network hostname . If the Unified Communications Manager cluster security is operating in mixed mode, secure connections to this node will fail after changing the hostname, or IP
                                                address until you run the CTL client and update the CTL file or run utils ctl update CTLFile if you used the tokenless CTL feature. |
|---|---|

| Note | In case you must change the vNIC from vcenter, use the CLI command set network hostname . |
|---|---|

| Step 1 | From Cisco
                                       			 Unified Operating System Administration, select Settings > IP > Ethernet |
|---|---|
| Step 2 | Change the
                                       			 hostname, IP address, and if necessary, the default gateway. |
| Step 3 | Click Save . Node services
                                       			 automatically restart with the new changes. Restarting services ensures the
                                       			 proper update and service-restart sequence for the changes to take effect. Changing the hostname triggers an automatically self-signed certificate regeneration and causes all devices in the cluster
                                          to reset so they can download an updated ITL file. Changing the hostname does not trigger the ITL recovery certificates regeneration. |

| Note | Do not proceed
                                          			 if the new hostname does not resolve to the correct IP address. |
|---|---|

| Caution | A change of the hostname or IP address requires the system services to be restarted. Hence, refrain from making this change
                                                during normal operating hours. Through Cisco Unified CM Administration, we recommend that you change only one of these settings at a time. To change both
                                                the IP address and hostname at the same time, use the CLI command set network hostname . If the Unified Communications Manager cluster security is operating in mixed mode, secure connections to this node will fail after changing the hostname, or IP
                                                address until you run the CTL client and update the CTL file or run utils ctl update CTLFile if you used the tokenless CTL feature. If the hostname or IP address that is defined on the Cisco Unified OS Administration and Cisco Unified CM Administration pages
                                                do not match, the applications are unable to fetch the correct phone status. Also, due to certificate mismatch, TLS handshake
                                                fails. Hence, ensure that the IP address and hostname entries in both the Cisco Unified OS Administration and the Cisco Unified
                                                CM Administration pages are alike. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Server . The Find and List Servers window appears. |
|---|---|
| Step 2 | To get a list of all servers, click Find . |
| Step 3 | From the list, click the server for which you want to modify the hostname. |
| Step 4 | In the Host Name/IP Address* field, enter the new host name or the IP address and click Save . |
| Step 5 | Using the Admin CLI GUI, reboot the node using the utils system restart CLI command. |

| Caution | If the Cisco Unified Communications Manager cluster security is operating in mixed mode, secure connections to this node will
                                          fail after changing the hostname, or IP address until you run the CTL client and update the CTL file or run utils ctl update CTLFile if you used the tokenless CTL feature. |
|---|---|

| Step 1 | Log in to the CLI of the node that you want to change. |
|---|---|
| Step 2 | Enter set network
                                             				  hostname . |
| Step 3 | Follow the
                                       			 prompts to change the hostname, IP address, or default gateway. Enter the
                                             				  new hostname and press Enter . Enter yes if you
                                             				  also want to change the IP address; otherwise, go to Step 4. Enter the
                                             				  new IP address. Enter the
                                             				  subnet mask. Enter the
                                             				  address of the gateway. |
| Step 4 | Verify that
                                       			 all your input is correct and enter yes to start
                                       			 the process. |

| Note | Do not proceed
                                          			 if the new hostname does not resolve to the correct IP address. |
|---|---|

| Note | In case you need to change the vNIC from vcenter, update the vNIC after the step calling 4 of 5 component notification script: regenerate_all_certs.sh as displayed in the following output. |
|---|---|

| Note | For IM and Presence Service : Change and
                                                				  verify the IM and Presence database publisher node first. You can change the IM and Presence
                                                   				  Service subscriber nodes simultaneously or one at a time. |
|---|---|

| Step 1 | Log in to the CLI of the node that you want to change. |
|---|---|
| Step 2 | Enter set network ip eth0 new-ip_address new_netmask new_gateway to change the IP address of the node. Note Changing IP address only with the set network ip eth0 command does not trigger Certificate Regeneration. where new_ip_address specifies the new server IP address, new_netmask specifies the new server network mask and new_gateway specifies the gateway address. The following output displays: admin:set network ip eth0 10.53.57.101 255.255.255.224 10.53.56.1 

WARNING: Changing this setting will invalidate software license 
on this server. The license will have to be re-hosted. 

Continue (y/n)? | Note | Changing IP address only with the set network ip eth0 command does not trigger Certificate Regeneration. |
| Note | Changing IP address only with the set network ip eth0 command does not trigger Certificate Regeneration. |
| Step 3 | Verify the
                                       			 output of the CLI command. Enter yes , and then
                                       			 press Enter to start the process. |

| Note | Changing IP address only with the set network ip eth0 command does not trigger Certificate Regeneration. |
|---|---|

| Note | In case you need to change the vNIC from vcenter, update the vNIC after the step calling 3 of 6 component notification script: aetc_hosts_verify.sh as displayed in the following output. |
|---|---|

| Step 1 | Log in to the CLI of the node that you want to change. |
|---|---|
| Step 2 | Enter set network dns primary/secondary <new IP address of the DNS> Note If you change the IP address for the DNS servers, you must reboot the server through the utils system restart CLI command. The following ouput displays: admin:set network dns primary/secondary <new IP address of DNS>
*** W A R N I N G ***
This will cause the system to temporarily lose network connectivity | Note | If you change the IP address for the DNS servers, you must reboot the server through the utils system restart CLI command. |
| Note | If you change the IP address for the DNS servers, you must reboot the server through the utils system restart CLI command. |
| Step 3 | Verify the output of the CLI command. Enter Yes and then press Enter to start the process. |

| Note | If you change the IP address for the DNS servers, you must reboot the server through the utils system restart CLI command. |
|---|---|