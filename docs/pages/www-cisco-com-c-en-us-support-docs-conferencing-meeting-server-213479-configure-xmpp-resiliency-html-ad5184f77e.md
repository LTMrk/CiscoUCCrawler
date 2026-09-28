---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-213479-configure-xmpp-resiliency-html-ad5184f77e
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/213479-configure-xmpp-resiliency.html
retrieved_at: 2026-08-16T18:59:30.490380+00:00
---

Configure XMPP Resiliency

# Configure XMPP Resiliency

Updated: July 11, 2018

Document ID: 213479

Contents

## Contents

## Introduction

This document describes how to setup Extensible Messaging and Presence Protocol (XMPP) Resiliency on Cisco Meeting Server (CMS).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Database clustering must be setup before XMPP Resiliency. This is the link to setup Database Clustering

https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/210530-Configure-Cisco-Meeting-Server-Call-Brid.html

- Callbridge component must be configured on CMS

- Cisco recommends that you have at least 3 XMPP nodes to be able to setup XMPP resiliency

- When setup is in Resilient mode, the XMPP servers within a deployment are loaded with the same configuration

- Understanding of certificates self-signed, Certificate Authority (CA)-Signed

- Domain Name Server (DNS) required

- Required a Local certificate Authority or Public Certificate Authority to generate certificates

Note : Using self-signed certificates are not recommended for production environment

### Components Used

This document is not restricted to specific software and hardware versions.

- CMS

- PuTTY Secure Shell (SSH) terminal emulation software for Mainboard Management Processor (MMP)

- A web browser such as Firefox, Chrome

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Network Diagram

This image shows the exchange of XMPP messages and routing traffic.

### Configuration

This example of XMPP resiliency deployment uses three XMPP servers, and configures it for the first time.

Note : If XMPP resiliency is previously deployed then it is recommended to reset all servers.

XMPP servers uses keep-alive messages to monitor each other and to elect a Leader. XMPP messages can be sent to any server. As shown in the preceeding image, messages are forwarded to the Leader XMPP server. The XMPP servers continue to monitor each other, if the Leader fails then a new Leader is elected and the other XMPP servers forward traffic to the new Leader.

Step 1. Generate Certificates for XMPP Component.

Generate CSR and then you this command to generate corresponding certificate through Local Certificate Authority/ Public certifcate Authority as required

pki csr  <key/cert basename>

Step 2. Use the above CSR and generate certificate using local certificate authority. You can use VCS Certificate guide to generate certificates using Microsoft Certificate Authority, Appendix 5 page 32

https://www.cisco.com/c/dam/en/us/td/docs/telepresence/infrastructure/vcs/config_guide/X8-8/Cisco-VCS-Certificate-Creation-and-Use-Deployment-Guide-X8-8.pdf

Upload the certificate on all 3 nodes using WINSCP/SFTP server. To check if certificates being uploaded use a command on MMP/SSH

command: pki list

Note : In lab, one certificate is used for all 3 XMPP nodes.

Step 3. Configure CMS to use XMPP component.

```
cb1> xmpp domain tptac9.com
cb1>xmpp listen a
cb1>xmpp certs abhiall.key abhiall.cer certall.cer
 
*certall.cer= CA certificate
```

Tip : If your CA provides a certificate bundle then include the bundle as a separate file to the certificate. A certificate bundle is a single file (with an extension of .pem , .cer or .crt ) holding a copy of the Root CA’s certificate and all intermediate certificates in the chain. The certificates need to be in sequence with the certificate of the Root CA being last in the certificate bundle. External clients (for example web browsers and XMPP clients) require the certificate and certificate bundle to be presented by the XMPP server respectively, when setting up a secure connection.

When bundle of certificates is required. The above command would be

```
cb1> xmpp certs abhiall.key abhiall.cer certallbundle.cer
 
certallbundle.cer= CA certificate + Intermediate CA + Intermediate CA1 + Intermediate CA2 +.... + Intermediate CAn +  Root CA
 
where n is an integer
```

When using 3 certificates for 3 respective XMPP nodes. Please ensure to bundle the certificates

```
xmppserver1.crt + xmppserver2.crt + xmppserver3.crt= xmpp-cluster-bundle.crt
```

A single certificate abhiall.cer is used in the document.

Please refer to this guide to know more details on certificates

https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Deployment_Guide/Version-2-2/Certificate-Guidelines-Scalable-and-Resilient-Deployments-2-2.pdf

Step 4. Upload certificates through SFTP to all CMS, which runs XMPP component.

cb1>> xmpp cluster trust xmpp-cluster-bundle.crt

In lab xmpp cluster trust abhiall.cer

cb1>>xmpp cluster trust abhiall.cer

Step 5. Add Call Bridges to XMPP server.

cb1> xmpp callbridge add cb1

A secret is generated, this configures the XMPP server to allow connections with the Call Bridge named cb1 .

Note : The domain, Call Bridge name and secret is generated, you need this information later when you configure the Call Bridge access to the XMPP server (so that the Call Bridge presents the authentication details to the XMPP server)

The above command is used to add other Call Bridges to the same xmpp node.

cb1> xmpp callbridge add cb2

cb1> xmpp callbridge add cb3

Note :Each call bridge must have a unique name . If you have not already noted the details for the Call Bridges that you have added to the XMPP server, then use the command: xmpp callbridge list

cb1> xmpp disable

This disable the XMPP server node

Step 6. Enable XMPP cluster.

cb1> xmpp cluster enable

Initialize the XMPP cluster on this node. This command creates a 1 node xmpp cluster , the other nodes (xmpp servers) are joined to this cluster.

cb1> xmpp cluster initialize

Re-enable this node

cb1>xmpp enable

Step 7. Add Call Bridges to second XMPP node and join it to a Cluster.

Add each Call Bridge to this node. This requires the Call Bridge to be added using the same Call Bridge name and secret from the first XMPP server node. This is achieved through this command

cb2>> xmpp callbridge add-secret cb1

Enter call bridge secret

To check secret please run the command xmpp call bridge list . It lists all the secret generated on the first node.

After you add all the Call Bridges secret to the second node.

```
cb2>> xmpp disable
cb2>> xmpp cluster enable
cb2>> xmpp enable
cb2>> xmpp cluster join <cluster>
```

Cluster: is the IP address or domain name of the first node

Step 8. Add Call Bridges to third XMPP node and join it to a Cluster.

Add each Call Bridge to this node. This requires the Call Bridge to be added using the same Call Bridge name and secret from the first XMPP server node. This is achieved using the command

cb3>> xmpp callbridge add-secret cb1

Enter call bridge secret

Now to check secret. You can run the command xmpp callbridge list . The command list all the secret generated on the first node

After all the Call Bridge secrets are added to this node perform these steps.

```
cb3>> xmpp disable
cb3>> xmpp cluster enable
cb3>> xmpp enable
cb3>> xmpp cluster join <cluster>
```

Cluster: is the IP address or domain name of the first node

Step 9. Configure each Call Bridge with the authentication details of the XMPP servers in the cluster. This enables the Call Bridges to access the XMPP servers.

Navigate to Webadmin > Configuration > General and enter these:

- Add unique Call Bridge name, no domain part is required.

- Enter domain for XMPP server domain tptac9.com

- Server address of the XMPP server. Set this field if you want this Call Bridge to only use a co-located XMPP server, or you don’t have DNS configured. Usage of the co-located XMPP server reduces latency.

- Leave this field empty to allow this Call Bridge to failover between XMPP servers, this requires the DNS entries to be setup.

If you plan to use Domain Name Server (DNS) to connect between Call Bridges and XMPP servers, you also need to set up a DNS SRV record for the xmpp cluster to resolve to the DNS A record of each of the XMPP servers in the cluster. The format of the DNS SRV record is: _xmpp-component._tcp.

```
_xmpp-component._tcp.example.com. 86400 IN SRV 0 0 5222 xmppserver1.example.com,  _xmpp-component._tcp.example.com. 86400 IN SRV 0 0 5223 xmppserver2.example.com, _xmpp-component._tcp.example.com. 86400 IN SRV 0 0 5223 xmppserver3.example.com.
```

The example above specifies port 5223 (use another port if 5223 is already used).

the shared secret used for the respective Call Bridge. For example in the above screenshots

Cb1 secret is

Callbridge: cb1

Domain: tptac9.com

Secret: kvgP1SRzWVabhiPVAb1

Similarly for cb2 and cb3, repeat these steps for all 3 Call Bridges cb1,cb2 and cb3 .

After you perform these steps, please check the status of the cluster on all three Call Bridges

## Verify

Run cb1>>  xmpp cluster status , this command to get a report on the live state of the xmpp cluster. If the cluster fails, then this command  returns the statistics of the xmpp server, which runs on this Meeting Server only. Use this command to try and help diagnose connectivity problems.

This image shows the nodes, one as a Leader 10.106.81.30 and the rest two as Follower.

Similarly, check the status on rest of the two nodes.

On Second node

On Third node

## Troubleshoot

XMPP resiliency has been setup successfully. There could be issues which might come across when using xmpp resiliency.

Scenario 1. Checked for DNS configuration, the errors in the screenshots points to the DNS issues.

If these errors are seen, check the  configuration for SRV records.

In XMPP resiliency, the XMPP server that a Call Bridge connects to is controlled via DNS. This choice is based on the DNS priority and weight given. A Call Bridge only connects to one XMPP server at a time. There is no requirement for all Call Bridges to connect to the same XMPP server since all traffic is forwarded to the master. If a network problem results in the Call Bridge losing connection to the XMPP server, the Call Bridge attempts to reconnect to another XMPP server. The Call Bridge must be configured to any XMPP server it can connect to.

In order to enable client connections, use of the WebRTC Client, an _xmpp-client._tcp record is required. On a typical deployment, it resolves to port 5222 . Inside, the LAN, if the core server is directly routable, it can resolve to the XMPP service, that runs on the core server.

For example: _xmpp-client._tcp.tptac9.com can have these SRV records:

_xmpp-client._tcp. tptac9.com 86400 IN SRV 10 50 5222 cb1. tptac9.com

advice on setting up DNS records for the XMPP server nodes. For, XMPP resiliency you require DNS to connect between Call Bridges and XMPP servers you will also need to set up a DNS SRV record for the xmpp cluster to resolve to the DNS A record of each of the XMPP servers in the cluster. The format of the DNS SRV record is: _xmpp-component._tcp.tptac9.com

As per the setup discussed for 3 xmpp servers, the record which resolves to all three servers are shown

_xmpp-component._tcp.tptac9.com. 86400 IN SRV 0 0 5223 cb1.tptac9.com

_xmpp-component._tcp.tptac9.com. 86400 IN SRV 0 0 5223 cb2.tptac9.com

_xmpp-component._tcp.tptac9.com. 86400 IN SRV 0 0 5223 cb3.tptac9.com

The example specifies the port 5223, any other port can also be used if 5223 is already being used. However, ensure the used port must be opened.

Scenario 2. When CMS status page shows authentication failure.

The authentication failure is mostly seen when either the shared secret is not entered or entered incorrectly. Please ensure that shared secret is entered, if forgot and do not have it handy. Please SSH to the server and run this command: xmpp callbridge list

The document describes the xmpp resiliency setup. Hence, run the command on all 3 servers to ensure the generated secrets are same across all servers. As the images shows, it can seen on server cb1 , the shared secret used is same as what is being reflected for cb3 . After you check on other servers, it is conclude that the entered secret for cb1 is incorrect.

Scenario 3. In xmpp cluster status duplicate entries of XMPP nodes.

This output shows the duplicate entry of the node 10.61.7.91:5222

```
cb1> xmpp cluster status State: LEADER
List of peers 10.61.7.91:5222
 
10.61.7.91:5222 10.59.103.71:5222
10.59.103.70:5222 (Leader)
```

Caution : It is recommend to remove xmpp nodes from the cluster before resetting them. If XMPP reset is performed on a node while it is still in the cluster and then re-join the node to the existing XMPP cluster, it creates a duplicate entry of that node when checked the status through xmpp cluster status.

This can cause issues in a resilient setup. A defect has been raised

https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvi67717

Please check page 94 of the below guide

https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Deployment_Guide/Version-2-3/Cisco-Meeting-Server-2-3-Scalable-and-Resilient-Deployments.pdf

### Contributed by Cisco Engineers

Abhishek Pal

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server