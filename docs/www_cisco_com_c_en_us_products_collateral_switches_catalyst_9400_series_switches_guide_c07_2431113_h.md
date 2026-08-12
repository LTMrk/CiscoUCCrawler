  * [Skip to content](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


# Cisco ThousandEyes Enterprise Agent Deployment Guide on Catalyst 9000 Switching Platforms
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.pdf) (4.1 MB)   
View with Adobe Reader on a variety of devices


Updated:October 23, 2024
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Contact Cisco
  * Contact Cisco
  * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)
  * Call Sales: [ 1-800-553-6387 ](tel:18005536387)   
US/CAN | 5am-5pm PT 
  * [Product / Technical Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.pdf) (4.1 MB)   
View with Adobe Reader on a variety of devices


Updated:October 23, 2024
#### Table of Contents
![Open Search](https://www.cisco.com/content/dam/eotToc/search-white_28x28.png)
![Close Search](https://www.cisco.com/content/dam/eotToc/close_11x11.png)
#### Table of Contents
  * [Introduction](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#Introduction "Introduction")
  * [Catalyst 9000 application hosting framework](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#Catalyst9000applicationhostingframework "Catalyst9000applicationhostingframework")
  * [Requirements for the ThousandEyes Enterprise Agent on the Catalyst 9000 platform](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#RequirementsfortheThousandEyesEnterpriseAgentontheCatalyst9000platform "RequirementsfortheThousandEyesEnterpriseAgentontheCatalyst9000platform")
  * [Installation and configuration procedure](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#Installationandconfigurationprocedure "Installationandconfigurationprocedure")
  * [Cisco Catalyst Center](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#CiscoCatalystCenter "CiscoCatalystCenter")
  * [Cisco IOS XE CLI](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#CiscoIOSXECLI "CiscoIOSXECLI")
  * [WebUI](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#WebUI "WebUI")
  * [YANG models](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#YANGmodels "YANGmodels")
  * [Performing tests from the ThousandEyes account](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#PerformingtestsfromtheThousandEyesaccount "PerformingtestsfromtheThousandEyesaccount")
  * [Troubleshooting](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#Troubleshooting "Troubleshooting")
  * [Conclusion](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#Conclusion "Conclusion")
  * [Useful references](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.html#Usefulreferences "Usefulreferences")


Introduction
Many organizations are heavily dependent on business-critical applications hosted in private and public clouds as Software as a Service (SaaS) over the internet. While SaaS-based productivity and collaboration tools have been game-changing, meeting network SLAs and ensuring consistent performance of business-critical SaaS applications have become a concern for enterprises. 
End-to-end visibility into the network is required to understand why SaaS performance is degrading or to troubleshoot the root cause of outages. However, traditional tools such as NetFlow, Simple Network Management Protocol (SNMP), and Packet Capture (PCAP) cannot provide visibility into devices managed by service providers or SaaS providers. 
Cisco® ThousandEyes is a digital experience monitoring platform to see, understand, and improve digital experiences over any network. ThousandEyes offers global vantage points from which users can run a variety of tests to gain more insights and to monitor the performance of their business-critical applications or the network itself. 
ThousandEyes has three type of agents:
●**Enterprise Agent:** A lightweight software-based agent, easily installed on your own network, that provides visibility within the enterprise campus, data centers, virtual private clouds/virtual networks, and branches. It also supports active monitoring, SNMP-based monitoring, and topological mapping of internal network devices. 
●**Cloud Agent:** A globally distributed agent installed and managed by ThousandEyes in 200+ cities to give users access to performance data from local transit providers and last-mile ISPs to simulate end-user performance. 
●**Endpoint Agent:** A lightweight service installed on end-user laptops and desktops that provides proactive and real-time monitoring of application experience and network connectivity. 
Generally, on an enterprise campus, the network operator must deploy ThousandEyes Enterprise Agents across the network, including campus and branch locations, to measure network and application performance between the campus and branches, SaaS, and cloud infrastructure (Figure 1). 
The ThousandEyes Enterprise Agent integrated on Cisco Catalyst® 9300 and 9400 Series switches helps the network operator minimize deployment time across multiple locations without requiring any additional hardware, as well as providing ongoing insight into the status of network SLAs. 
[![Typical ThousandEyes deployment and use cases in an enterprise campus network](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_0.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_0.png "Typical ThousandEyes deployment and use cases in an enterprise campus network")
Figure 1. 
Typical ThousandEyes deployment and use cases in an enterprise campus network
This document describes the installation, configuration, and operation of the ThousandEyes Enterprise Agent on Cisco Catalyst 9300 and 9400 Series platforms using the Cisco application hosting framework.
Catalyst 9000 application hosting framework
Application hosting on the Cisco Catalyst 9000 switching platform enables data processing closer to the source in a distributed manner. It is used by enterprises to host a new breed of security, network monitoring/troubleshooting, and data analytics tools while removing the need for expensive compute nodes, as having an application hosted on the switch gives developers easy and efficient access to live network traffic as well as to the rich telemetry supported by the infrastructure. 
Figure 2 shows a high-level view of the system architecture of application hosting on Catalyst 9000 switching platforms. 
[![Cisco Catalyst 9000 application hosting framework](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_1.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_1.png "Cisco Catalyst 9000 application hosting framework")
Figure 2. 
Cisco Catalyst 9000 application hosting framework
Requirements for the ThousandEyes Enterprise Agent on the Catalyst 9000 platform
●One or more Cisco Catalyst 9300 or 9400 Series switches
●Cisco IOS® XE 17.3.3 (on the Catalyst 9300) or 17.5.1 (on the Catalyst 9400) or later
●Cisco Catalyst and Cisco DNA Advantage licenses 
●ThousandEyes account
●IP reachability to ThousandEyes (direct, Network Address Translation [NAT], or proxy)
●Cisco Catalyst Center (version 2.2.2.x and above) (optional)
●SSD (optional)*
* An SSD is not required starting with Cisco IOS XE 17.3.3 (on the Catalyst 9300) and Cisco IOS XE 17.5.1 (on the Catalyst 9400) for non-browser tests. 
Installation and configuration procedure
The ThousandEyes Enterprise Agent can be downloaded from your ThousandEyes account (Figure 3). There are two Catalyst 9000 Docker versions: Embed Docker version (approximately > 200 MB file size), which doesn’t currently have browser tests (page load and transaction), and Full Docker version (approximately > 1.2 GB file size). The Embed Docker version can be used on the Catalyst 9300 and 9400 Series switches without an SSD drive. 
To download the ThousandEyes Enterprise Agent Docker application, log in to your ThousandEyes account and follow the path below: 
Cloud and Enterprise Agents -> Agent Settings -> Enterprise Agents -> Add New Enterprise Agent -> Cisco Application Hosting
[![ThousandEyes Enterprise Agent images and account group token](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_2.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_2.png "ThousandEyes Enterprise Agent images and account group token")
Figure 3. 
ThousandEyes Enterprise Agent images and account group token
**Note:** The Cisco signed Embed ThousandEyes Enterprise Agent can be hosted in the flash memory of the switch starting with Cisco IOS XE Release 17.3.3 on the Catalyst 9300 Series and with Cisco IOS XE Release 17.5.1 on the Catalyst 9400 Series. 
Catalyst 9300 and 9400 Series switches shipping after April 2021 will have the ThousandEyes Enterprise Agent (Embed version) already preloaded in the flash:Apps folder.
There are multiple options for deploying the ThousandEyes Enterprise Agent on the Catalyst 9000 platform. 
●Cisco Catalyst Center 
●Web User Interface (WebUI) 
●Cisco IOS XE Command-Line Interface (CLI) 
●YANG model 
Cisco Catalyst Center
Beginning with Cisco Catalyst Center Release 1.3.1.2, Cisco is providing a centralized user interface for deploying and managing the entire lifecycle of the applications, in addition to the CLI and WebUI management. Cisco Catalyst Center provides consistent workflows for managing multiple Catalyst 9000 switches through the “Application Hosting” workflow. 
Cisco Catalyst Center is the preferred automation platform for enterprise, since it can minimize the time taken to deploy these agents across multiple locations, helps ensure consistency in deployment, and helps ensure the security of the compute resources throughout the easy-to-use workflow. 
With its intuitive user interface, Cisco Catalyst Center (Release 2.2.2.x) makes it easy to deploy the ThousandEyes Enterprise Agent. The network operator can upload the Enterprise Agent to Cisco Catalyst Center and add required IP configurations and Docker run options (ThousandEyes account token, proxy info, etc.), as shown in Figures 4 and 5.
[![Cisco Catalyst Center application hosting workflow](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_3.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_3.png "Cisco Catalyst Center application hosting workflow")
Figure 4. 
Cisco Catalyst Center application hosting workflow
[![Cisco Catalyst Center application hosting device selection](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_4.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_4.png "Cisco Catalyst Center application hosting device selection")
Figure 5. 
Cisco Catalyst Center application hosting device selection
Cisco Catalyst Center can manage the entire application lifecycle on multiple Catalyst 9000 switches at the same time with one click (Figure 6). 
[![Cisco Catalyst Center application hosting lifecycle management](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_5.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_5.png "Cisco Catalyst Center application hosting lifecycle management")
Figure 6. 
Cisco Catalyst Center application hosting lifecycle management
Cisco IOS XE CLI
Step 1: Copy the application to the flash or SSD drive.  
|  C9K#dir flash: | i .tar 253960 -rw- 178872320 Mar 27 2021 00:03:32 +00:00 thousandeyes-enterprise-agent-3.0.cat9k.tar   |  
| --- |  
Step 2: Enable “iox” for the application hosting feature.
Configure Cisco IOx in the Catalyst 9000 switch to enable the application hosting framework.  
|  C9K#conf t C9K(config)1#iox C9K(config)1#exit  |  
| --- |  
Verify that the switch is configured to run Cisco IOx with the following show command:  
|  C9K#show iox IOx Infrastructure Summary: --------------------------- IOx service (CAF) 1.11.0.5 : Running IOx service (HA) : Running  IOx service (IOxman) : Running  IOx service (Sec storage) : Not Running  Libvirtd 1.3.4 : Running Dockerd 18.03.0 : Running Application DB Sync Info : Available  Sync Status : Disabled  |  
| --- |  
Step 3: Configure the AppGigabitEthernet port  
|  interface AppGigabitEthernet1/0/1 switchport trunk allowed vlan <vlan-id> switchport mode trunk  |  
| --- |  
AppGigabitEthernet is an internal hardware data port that is hardware-switched to the front-panel data ports. The AppGigabitEthernet port can be configured as a trunk port and allow a specific VLAN for application traffic. In the application hosting infrastructure, the user can define multiple virtual networks (eth0, eth1,…) based on application requirements (Figure 7).
[![Cisco Catalyst 9000 application hosting architecture](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_6.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_6.png "Cisco Catalyst 9000 application hosting architecture")
Figure 7. 
Cisco Catalyst 9000 application hosting architecture
Step 4: Configure applications based on the deployment models
The application’s network configuration and Docker run-option requirements are covered in this step. The ThousandEyes account token is available in your ThousandEyes account, as shown in Figure 3.
4.1. Assign a static IP address for the Enterprise Agent
Set up a static IP address in the application’s configuration:  
|  Configuration snippet: C9K#conf t Enter configuration commands, one per line. End with CNTL/Z. C9K(config)#app-hosting appid <app-name> C9K(config-app-hosting)# app-vnic AppGigabitEthernet trunk C9K(config-config-app-hosting-trunk)# vlan <vlan-id> guest-interface 0 C9K(config-config-app-hosting-vlan-access-ip)# guest-ipaddress x.x.x.x netmask x.x.x.x C9K(config-config-app-hosting-vlan-access-ip)# app-default-gateway x.x.x.x guest-interface 0 C9K(config-app-hosting)# app-resource docker C9K(config-app-hosting-docker)# prepend-pkg-opts C9K(config-app-hosting-docker)# run-opts 1 "-e TEAGENT_ACCOUNT_TOKEN=xxxxxxxxxx" C9K(config-app-hosting-docker)# name-server0 x.x.x C9K(config-app-hosting)# start C9K(config-app-hosting)#end Configuration Example: app-hosting appid teyes app-vnic AppGigabitEthernet trunk vlan 14 guest-interface 0 guest-ipaddress 14.0.0.113 netmask 255.255.255.0 app-default-gateway 14.0.0.1 guest-interface 0 app-resource docker prepend-pkg-opts run-opts 1 "-e TEAGENT_ACCOUNT_TOKEN=xxxxxxxxxx" name-server0 14.0.0.1 start  |  
| --- |  
4.2. Assign a dynamic IP address assignment for the Enterprise Agent
For networks that use Dynamic Host Configuration Protocol (DHCP), configure an IP address in the application’s configuration:  
|  Configuration snippet: C9K#conf t Enter configuration commands, one per line. End with CNTL/Z. C9K(config)#app-hosting appid <app-name> C9K(config-app-hosting)# app-vnic AppGigabitEthernet trunk C9K(config-config-app-hosting-trunk)# vlan <vlan-id> guest-interface 0 C9K(config-app-hosting)# app-resource docker C9K(config-app-hosting-docker)# prepend-pkg-opts C9K(config-app-hosting-docker)# run-opts 1 "-e TEAGENT_ACCOUNT_TOKEN=xxxxxxxxxx" C9K(config-app-hosting-docker)# name-server0 x.x.x C9K(config-app-hosting)# start C9K(config-app-hosting)#end Configuration Example: app-hosting appid teyes app-vnic AppGigabitEthernet trunk vlan 14 guest-interface 0 app-resource docker prepend-pkg-opts run-opts 1 "-e TEAGENT_ACCOUNT_TOKEN=xxxxxxxxxx" name-server0 14.0.0.1 start  |  
| --- |  
4.3. Using a proxy setting in the Enterprise Agent
This section shows how to add proxy information in an application’s configuration. Proxy information is required for networks that don’t have direct IP reachability to ThousandEyes. The proxy setting can be used in both the static and DHCP configurations mentioned in sections 4.1 and 4.2.  
|  Configuration snippet: C9K#conf t Enter configuration commands, one per line. End with CNTL/Z. C9K(config)#app-hosting appid <app-name> C9K(config-app-hosting)# app-vnic AppGigabitEthernet trunk C9K(config-config-app-hosting-trunk)# vlan <vlan-id> guest-interface 0 C9K(config-app-hosting)# app-resource docker C9K(config-app-hosting-docker)# prepend-pkg-opts C9K(config-app-hosting-docker)# run-opts 1 "-e TEAGENT_ACCOUNT_TOKEN=xxxxxxxxxx" run-opts 2 "-e TEAGENT_PROXY_TYPE=STATIC" run-opts 3 "-e TEAGENT_PROXY_LOCATION='proxy-info.xyz.com:80'" C9K(config-app-hosting-docker)# name-server0 x.x.x.x C9K(config-app-hosting)# start C9K(config-app-hosting)#end Configuration Example: app-hosting appid teyes app-vnic AppGigabitEthernet trunk vlan 14 guest-interface 0 app-resource docker prepend-pkg-opts run-opts 1 "-e TEAGENT_ACCOUNT_TOKEN=xxxxxxxxxx" run-opts 2 "-e TEAGENT_PROXY_TYPE=STATIC" run-opts 3 "-e TEAGENT_PROXY_LOCATION='proxy-info.xyz.com:80'" name-server0 14.0.0.1 start  |  
| --- |  
Step 5: Install and start the ThousandEyes Enterprise Agent
The application is now ready to be deployed. The command below is required to deploy the Enterprise Agent on the Catalyst 9300 or 9400 Series switching platforms.  
|  C9K#app-hosting install appid teyes package flash:  thousandeyes-enterprise-agent-3.0.cat9k.tar Installing package 'flash:thousandeyes-enterprise-agent-3.0.cat9k.tar' for 'teyes'. Use 'show app-hosting list' for progress. C9K#show app-hosting list  App id State --------------------------------------------------------- teyes RUNNING C9K#show app-hosting detail appid teyes  App id : teyes Owner : iox State : RUNNING Application Type : docker Name : thousandeyes/enterprise-agent Version : 3.0 Description :  Path : flash:thousandeyes-enterprise-agent-3.0.cat9k.tar URL Path :  Activated profile name : custom Resource reservation Memory : 500 MB Disk : 1 MB CPU : 1850 units VCPU : 1 Attached devices Type Name Alias --------------------------------------------- serial/shell iox_console_shell serial0 serial/aux iox_console_aux serial1 serial/syslog iox_syslog serial2 serial/trace iox_trace serial3 Network interfaces --------------------------------------- eth0: MAC address : 52:54:dd:e3:db:15 Network name : mgmt-bridge-v14  |  
| --- |  
WebUI
The network operator can use the Catalyst 9300 or 9400 Series WebUI to deploy the ThousandEyes Enterprise Agent on the switch. The operator can upload the ThousandEyes Docker app as shown in Figure 8. This is an alternative way to deploy the Enterprise Agent on a single switch and then repeat the steps on every switch on which you plan to deploy the Enterprise Agent.
[![Cisco IOx Local Manager on WebUI](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_7.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_7.png "Cisco IOx Local Manager on WebUI")
Figure 8. 
Cisco IOx Local Manager on WebUI
The network operator can also select the IP configuration of the app as well as specifying Docker run options (account token, proxy information, etc.), as shown in Figure 9. Then activate the application to reserve CPU, memory, and disk space for it.
[![Cisco IOx Local Manager application configuration](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_8.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_8.png "Cisco IOx Local Manager application configuration")
Figure 9. 
Cisco IOx Local Manager application configuration
The application is now successfully deployed and running, as shown in Figure 10. The network operator can manage the entire lifecycle of the application using the WebUI.
[![Cisco IOx Local Manager application management](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_9.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_9.png "Cisco IOx Local Manager application management")
Figure 10. 
Cisco IOx Local Manager application management
YANG models
Starting with Cisco IOS XE Release 16.12.1, Cisco is also offering YANG models for hosting applications on Catalyst 9000 switching platforms, in addition to Cisco Catalyst Center automation for application deployment. With the configuration below and operational YANG models, the network operator can use customized automation for Enterprise Agent deployment. 
[Cisco-IOS-XE-app-hosting-cfg.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/16121/Cisco-IOS-XE-app-hosting-cfg.yang)
[Cisco-IOS-XE-app-hosting-oper.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/16121/Cisco-IOS-XE-app-hosting-oper.yang)
Performing tests from the ThousandEyes account
Once the ThousandEyes Enterprise Agent is successfully deployed, the network operator can log in to the ThousandEyes dashboard and perform required network and application performance testing to discover the root causes of network and application outages (Figure 11). 
[![ThousandEyes Cloud and Enterprise Agent test settings](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_10.png)](https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9400-series-switches/guide-c07-2431113.docx/_jcr_content/renditions/guide-c07-2431113_10.png "ThousandEyes Cloud and Enterprise Agent test settings")
Figure 11. 
ThousandEyes Cloud and Enterprise Agent test settings
Troubleshooting
The network operator may log in to the application console to collect a required application log for troubleshooting. The commands below show how to access the log via the Cisco IOS XE CLI. For WebUI and Cisco Catalyst Center, the network operator can get the logs easily within the application hosting user interface.  
|  C9K#app-hosting connect appid <app-name> session  # # cd /var/log/agent # ls te-agent.log te-agent-sanity.log # cat te-agent.log 2021-03-28 19:46:30.683 DEBUG [cdc90a40] [te.agent.AptPackageInterface] {} Initialized APT package interface 2021-03-28 19:46:30.683 INFO [cdc90a40] [te.agent.main] {} Agent version 1.103.0 starting. Max core size is 0 and max open files is 1024 2021-03-28 19:46:30.683 DEBUG [cdc90a40] [te.agent.db] {} Vacuuming database 2021-03-28 19:46:30.685 INFO [cdc90a40] [te.agent.db] {} Found version 0, expected version 50 2021-03-28 19:46:30.720 INFO [cdc62700] [te.probe.ServerTaskExecutor] {} ProbeTaskExecutor started with 2 threads. 2021-03-28 19:46:30.721 INFO [c7fff700] [te.probe.ProbeTaskExecutor.bandwidth] {} ProbeTaskExecutor started with 1 threads. 2021-03-28 19:46:30.721 INFO [c77fe700] [te.probe.ProbeTaskExecutor.realtime] {} ProbeTaskExecutor started with 1 threads. 2021-03-28 19:46:30.721 INFO [c6ffd700] [te.probe.ProbeTaskExecutor.throughput] {} ProbeTaskExecutor started with 1 threads. 2021-03-28 19:46:30.722 DEBUG [cdc90a40] [te.agent.DnssecTaskProceessor] {} Agent is not running bind 2021-03-28 19:46:30.722 DEBUG [cdc90a40] [te.snmp.RequestDispatcher] {} Initialised SNMP++ session 2021-03-28 19:46:30.722 DEBUG [cdc90a40] [te.snmp.RequestDispatcher] {} Initialised SNMP++ session 2021-03-28 19:46:30.722 DEBUG [cdc90a40] [te.snmp.RequestDispatcher] {} Initialised SNMP++ session 2021-03-28 19:46:30.722 INFO [cdc90a40] [te.agent.main] {} Agent starting up 2021-03-28 19:46:30.723 INFO [cdc90a40] [te.agent.main] {} No agent id found, attempting to obtain one 2021-03-28 19:46:30.723 INFO [cdc90a40] [te.agent.ClusterMasterAdapter] {} Attempting to get agent id from sc1.thousandeyes.com 2021-03-28 19:46:31.058 INFO [cdc90a40] [te.agent.main] {} Found id 231626 2021-03-28 19:46:31.059 INFO [cdc90a40] [te.agent.ClusterMasterAdapter] {} Attempting to get controller assignment from sc1.thousandeyes.com 2021-03-28 19:46:31.087 INFO [cdc90a40] [te.agent.ClusterMasterAdapter] {} sc1.thousandeyes.com told us we should talk to controller c1.thousandeyes.com # exit  |  
| --- |  
The network operator can also export the log file to the flash of the switch as follows:  
|  C9K#app-hosting move system techsupport to flash: Successfully moved tech support to flash:/tech_support_2021-03-28_19.55.24.tar.gz  |  
| --- |  
Conclusion
Enterprises with SLAs for their network can now deploy the Cisco signed version of the ThousandEyes Enterprise Agent on Catalyst 9300 and 9400 Series switching platforms without using additional hardware for compute resources. Network operators can easily install the Enterprise Agents through the different methods described in this guide with minimal time and effort across different campus locations. Moreover, Cisco is providing a certain number of ThousandEyes units per Cisco DNA Advantage license for Catalyst 9300 and 9400 Series switches. These ThousandEyes units can be used toward network and application tests to gain visibility into applications, visualize paths, and detect anomalies in the network.
Useful references
Catalyst 9000 Application Hosting white paper:   
<https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9300-series-switches/white-paper-c87-742415.pdf>
General information about application hosting on Catalyst 9000 switching platforms:   
<https://developer.cisco.com/docs/app-hosting/#!application-hosting-in-the-enterprise>
ThousandEyes Enterprise Docker Agent Networking:   
<https://docs.thousandeyes.com/product-documentation/global-vantage-points/enterprise-agents/configuring/enterprise-agent-on-docker-advanced-networking>
### Our experts recommend
  * [Support for Precision Time Protocol on Cisco Catalyst Switches FAQ](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.html "Support for Precision Time Protocol on Cisco Catalyst Switches FAQ")


### Learn more
