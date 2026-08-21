---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-paging-server-216176-change-network-settings-in-informacast-w--ab4db9c172
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/paging-server/216176-change-network-settings-in-informacast-w.html
retrieved_at: 2026-08-21T12:40:11.490263+00:00
---

Change Network Settings in Informacast with GUI and Console

# Change Network Settings in Informacast with GUI and Console

### Download Options

Updated: October 14, 2019

Document ID: 216176

Contents

## Contents

## Introduction

This document describes how to change and troubleshoot the network settings in Cisco Basic Paging (InformaCast) with the Graphical User Interface (GUI) and the console.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Basic Paging

- Linux

### Components Used

The information in this document is based on this software version:

- Informacast basic Paging version 11.0.5 – 11.3

The information in this document was created from the devices in a specific lab environment. All the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

You can use method 1 or 2 to change the IP address, mask, DNS and gateway for the Singlewire server.

Warning : If you plan to switch between Basic and Advanced InformaCast and you change your IP address, you need to redeploy the InformaCast OVA.

Warning : If you have applications currently licensed, changing your IP address may cause yo u to require new license(s).

Note : InformaCast SIP certificates are regenerated whenever InformaCast is installed or its IP address is changed, so if you use Transport Layer Security (TLS) protocol with SIP, you need to install the InformaCast SIP certificate on all Cisco Unified Communications Managers (CUCM) in your InformaCast environment.

### Method 1. GUI

Step 1. In order to configure the network settings with the GUI open a web browser, enter the IP address of the InformaCast Virtual Appliance ( https://<informacast_IP>:10000 ) and press the Enter key. The Singlewire start page appears.

Step 2. Click on the Access Application Management Tools with Control Center link. A separate tab/window opens to the Control Center menu page as shown in the image.

Step 3. Enter your credentials and click on the Login button. By default, your username is admin and your password is changeMe . The Webmin homepage appears as shown in the image.

Step 4. In order to change the IP address follow these steps, navigate to System > Bootup and Shutdown .

Step 5. From the list of services select singlewireInformaCast as shown in the image.

Step 6. In order to stop the Informacast service click on Stop Now and wait until the service stops with all its children processes as shown in the image.

Step 7. Return to the main menu and navigate to Networking > Network Configuration . The network configuration options are as shown in the image.

Step 8. Select Network Interfaces and click on eth0 .

Step 9. Edit the eth0 interface with the new IP address and click on Save . At this point, it is expected to lose the connectivity to the server. In order to log in back to the server, use the new IP address.

Step 10. In order to edit the bootup interface, navigate to Networking > Network Configuration , click on the Activated at Boot tab and edit the IP address, the netmask and the broadcast IP as shown in the image.

Step 11. In order to start the singlewireInformaCast again, navigate to System > Bootup and Shutdown .

Step 12. From the list of services, select singlewireInformacast and click on Start Now . It can take several minutes for the service to start.

Step 13. In order to change the DNS and hostname, navigate to System > Bootup and Shutdown .

Step 14. From the list of services select singlewireInformaCast as shown in the image.

Step 15. Click on Stop Now and wait until the service stops with all its children processes as shown in the image.

Step 16. In order to return to the main menu, navigate to Networking > Netowrk Configuration .

Step 17. Select Hostname and DNS Client .

Step 18. Edit your DNS entries and click on Save .

Step 19. Return to the list of services under System > Bootup and Shutdown .

Step 20. Select singlewireInformaCast and click on Start Now . It can take several minutes for the service to start.

Step 21. Give the service several minutes to come back online.

Step 22. In order to change the Gateway, navigate to Network configuration > Routing and gateways and edit the settings as shown in the image. Click on Save .

### Method 2. Console

In order to change the IP addres, mask, DNS and gateway of the InformaCast server with the console follow this procedure:

Step 1. Open and log into the vSphere client.

Step 2. Select your virtual machine from your inventory (by default, this is Singlewire InformaCast VM).

Step 3. Click on Open Console . The Singlewire InformaCast VM console window appears as shown in the image.

Step 4. Press Alt + F2 in the Singlewire InformaCast VM console window. The Singlewire InformaCast VM console window refreshes.

Step 5. Enter admin at the singlewire login prompt and press Enter key.

Step 6. Enter your OS password at the Password prompt and press the Enter key. The Singlewire InformaCast VM console window refreshes as shown in the image.

Step 7. In order to confirm the current configuration use the command cat /etc/network/interfaces as shown in the image.

Step 8. In order to change the current IP of the Informacast server, enter the change-ip-address command and press the Enter key as shown in the image.

Step 9. Then, enter Y and press the Enter key.

Step 10. Enter a routable IP address on your network that is not currently in use and press the Enter key.

Step 11. Enter a valid netmask for that IP address and press the Enter key.

Step 12. Enter the default gateway for your specified IP address and press the Enter key.

Step 13. Enter the IP address(es) of a DNS server(s) on your network and press the Enter key to get an output as shown in the image.

Step 14. Enter Y and press the Enter key. The script to change the network parameters and regenerate the Secure Sockets Layer ( SSL) certificates starts automatically as shown in the image.

Step 15. The message Change IP address process completed successfully indicates that the change was applied. Send a ping to the new IP address to confirm reachability.

Step 16. In order to confirm that the change was taken correctly run the command cat /etc/network/interfaces as shown in the image.

If you configure the new IP address with a previously used IP, the change fails with the error " No changes were made to your system. Try running this command again or contact Singlewire support for assistance " as shown in the image.

In this case, change the server IP to a new one (never used) and repeat the process an additional time with the desired IP and gateway.

Warning : If you change the InformaCast IP address via SSH instead of Console the next message displays " If you are running this command over ssh, changing your IP address will result in your connection being dropped Singlewire recommends running this command from the console ".

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

In order to confirm if the server uses static or dynamic IP run the command cat /etc/network/interfaces as shown in the image.

Other useful command that you can use is /sbin/ifconfig eth0 as shown in the image.

In order to troubleshoot multicast, network settings and other issues, collect logs from Informacast server as follows.

Step 1. Open the informacast IP in a web browser, https://<informacast_IP> and select Informacast .

Step 2. Use your credentials to log in as shown in the image.

Step 3. Navigate to Help > Support .

Step 4. The Documentation and Tools menu shows up. It can vary for each Informacast version as shown in the image.

In order to troubleshoot multicast issues click on Informacast Logs Directory and collect the Performance Logs and Summary Logs .

Step 5. In order to troubleshoot network settings, you are required to get the messages logs . Connect via SSH to the server with admin credentials and run the next command.

tar -zcf messages.tgz /var/log/* /usr/local/singlewire/SwiftStart/server/jetty/webapps/SwiftStart/WEB-INF/data/* /etc/network/interfaces

Step 6. The comand line shows many permission denied messages, however the traces are collected and saved in compressed .tgz files as shown in the image.

Step 7. In order to confirm that the messages.tgz was generated use the command ls -la as shown in the image.

Step 8. In order to export the messages.tgz file to an external SFTP server use the command sftp <user>@<sftp_ip_address> . Enter your SFTP credentials and once connected type put messages.tgz to export the file as shown in the image.

Step 9. If you have a TAC case open use the link https://cway.cisco.com/csc/ in order to attach the messages.tgz to your service request.

Step 10. The daemon.log file can help you to figure it out the root cause of the issue.

## Related Information

InformaCast Virtual Appliance Basic Paging: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cucm/cisco_paging_server/11_0_5/CiscoPagingServerInstallandUserGuide_1105.pdf

### Contributed by Cisco Engineers

Victor Gutierrez Luna

Cisco TAC

### Customers Also Viewed

- Configure CUCM Integration with Paging Server (InformaCast)

- Configure and Troubleshoot Informacast

### This Document Applies to These Products

- Paging Server

- Unified Communications Manager (CallManager)