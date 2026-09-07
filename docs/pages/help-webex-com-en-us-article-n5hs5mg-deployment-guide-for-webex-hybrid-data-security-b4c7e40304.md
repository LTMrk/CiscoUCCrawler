---
doc_id: help-webex-com-en-us-article-n5hs5mg-deployment-guide-for-webex-hybrid-data-security-b4c7e40304
source_url: https://help.webex.com/en-us/article/n5hs5mg/Deployment-guide-for-Webex-Hybrid-Data-Security
retrieved_at: 2026-09-07T10:36:19.048086+00:00
---

### Hybrid Data Security Deployment Task Flow

Before you begin

Download Installation Files

Download the OVA file to your local machine for later use.

Create a Configuration ISO for the HDS Hosts

Use the HDS Setup Tool to create an ISO configuration file for the Hybrid Data Security nodes.

Install the HDS Host OVA

Create a virtual machine from the OVA file and perform initial configuration,
                        such as network settings.

The option to configure network settings during OVA deployment has been tested with ESXi 7.0 and 8.0. The option may not be available in earlier versions.

Set up the Hybrid Data Security VM

Sign in to the VM console and set the sign-in credentials. Configure the
                        network settings for the node if you didn't configure them at the time of
                        OVA deployment.

Upload and Mount the HDS Configuration ISO

Configure the VM from the ISO configuration file that you created with the
                        HDS Setup Tool.

Configure the HDS Node for Proxy Integration

If the network environment requires proxy configuration, specify the type of proxy that you will use for the node, and add the proxy certificate to the trust store if needed.

Register the First Node in the Cluster

Register the VM with the Cisco Webex cloud as a Hybrid Data Security node.

Create and Register More Nodes

Complete the cluster setup.

Until you start a trial, your nodes generate an alarm indicating that your service is not yet activated.

### Download Installation Files

Sign in to https://admin.webex.com , and then click Services .

In the Hybrid Services section, find the Hybrid Data Security card, and then click Set up .

If
                                                  the card is disabled or you don’t see it, contact
                                                  your account team or your partner organization.
                                                  Give them your account number and ask to enable
                                                  your organization for Hybrid Data Security. To find the account number, click the gear at
                                                  the top right, next to your organization name.

You can also download the OVA at any time from
                                                  the Help section on the Settings page. On the Hybrid Data Security card, click Edit
                                                  settings to open the page. Then, click Download Hybrid Data Security
                                                  software in the Help section.

Older versions of the software package (OVA) will not be compatible with the latest Hybrid Data Security upgrades. This can result in issues while upgrading the application. Make sure you download the latest version of the OVA file.

Select No to indicate
                                                  that you haven’t set up the node yet, and then
                                                  click Next .

The OVA file automatically begins to
                                                  download. Save the file to a location on your
                                                  machine.

Optionally, click Open Deployment
                                                  Guide to check if there’s a later
                                                  version of this guide available.

### Create a Configuration ISO for the HDS Hosts

The Hybrid Data Security setup process creates an ISO file. You then use the ISO to configure your Hybrid Data Security host.

Before you begin

The HDS Setup tool runs as a Docker container on a local machine. To access it, run Docker on that machine. The setup process requires the credentials of a Control Hub account with full administrator rights for your organization.

If you do not have a Docker Desktop license, you can use Podman Desktop to run the HDS Setup tool for steps 1 to 5 in the procedure below. See Run HDS Setup tool using Podman Desktop for details.

If the HDS Setup tool runs behind a proxy in your environment, provide the proxy settings (server, port, credentials) through Docker environment variables when bringing up the Docker container in step 5 . This table gives some possible environment variables:

Description

Variable

HTTP Proxy without authentication

GLOBAL_AGENT_HTTP_PROXY=http://SERVER_IP:PORT

HTTPS Proxy without authentication

GLOBAL_AGENT_HTTPS_PROXY=http://SERVER_IP:PORT

HTTP Proxy with authentication

GLOBAL_AGENT_HTTP_PROXY=http://USERNAME:PASSWORD@SERVER_IP:PORT

HTTPS Proxy with authentication

GLOBAL_AGENT_HTTPS_PROXY=http://USERNAME:PASSWORD@SERVER_IP:PORT

The configuration ISO file that you generate contains the master key encrypting the PostgreSQL or Microsoft SQL Server database. You need the latest copy of this file anytime you make configuration changes, like these:

Database credentials

Certificate updates

Changes to authorization policy

If you plan to encrypt database connections, set up your PostgreSQL or SQL Server deployment for TLS.

At your machine's command line, enter the appropriate command for your environment:

In regular environments:

```
docker rmi ciscocitg/hds-setup:stable
```

In FedRAMP environments:

```
docker rmi ciscocitg/hds-setup-fedramp:stable
```

This step cleans up previous HDS setup tool images. If there are no previous images, it returns an error which you can ignore.

To sign in to the Docker image registry, enter the following:

```
docker login -u hdscustomersro
```

At the password prompt, enter this hash:

```
dckr_pat_aDP6V4KkrvpBwaQf6m6ROkvKUIo
```

Download the latest stable image for your environment:

In regular environments:

```
docker pull ciscocitg/hds-setup:stable
```

In FedRAMP environments:

```
docker pull ciscocitg/hds-setup-fedramp:stable
```

When the pull completes, enter the appropriate command for your environment:

In regular environments without a proxy:

```
docker run -p 8080:8080 --rm -it ciscocitg/hds-setup:stable
```

In regular environments with an HTTP proxy:

```
docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTP_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup:stable
```

In regular environments with an HTTPS proxy:

```
docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTPS_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup:stable
```

In FedRAMP environments without a proxy:

```
docker run -p 8080:8080 --rm -it ciscocitg/hds-setup-fedramp:stable
```

In FedRAMP environments with an HTTP proxy:

```
docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTP_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup-fedramp:stable
```

In FedRAMP environments with an HTTPS proxy:

```
docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTPS_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup-fedramp:stable
```

When the container is running, you see "Express server listening on port
                        8080."

The Setup tool does not support connecting to localhost through http://localhost:8080 . Use http://127.0.0.1:8080 to connect to localhost.

Use a web browser to go to the localhost, http://127.0.0.1:8080 , and enter customer admin username for Control Hub at the prompt.

The tool uses this first entry of the username to set the proper environment for that account. The tool then displays the standard sign-in prompt.

When prompted, enter your Control Hub customer admin sign-in credentials, and then click Log in to allow access to the required services for Hybrid Data Security.

On the Setup Tool overview page, click Get Started .

On the ISO Import page, you have these options:

- No —If you’re creating your first HDS node, you don't have an ISO file to upload.

- Yes —If you already created HDS nodes, then you select your ISO file in the browse and upload it.

Check that your X.509 certificate meets the requirements in X.509 Certificate Requirements .

- If you never uploaded a certificate before, upload the X.509 certificate, enter the password, and click Continue .

- If your certificate is OK, click Continue .

- If your certificate has expired or you want to replace it, select No for Continue using HDS certificate chain and private key from previous ISO? . Upload a new X.509 certificate, enter the password, and click Continue .

Enter the database address and account for HDS to access your key datastore:

Select your Database Type ( PostgreSQL or Microsoft SQL Server ).

If you choose Microsoft SQL Server , you get an Authentication Type field.

( Microsoft SQL Server only) Select your Authentication Type :

Basic Authentication : You need a local SQL Server account name in the Username field.

Windows Authentication : You need a Windows account in the format username@DOMAIN in the Username field.

Enter the database server address in the form <hostname>:<port> or <IP-address>:<port> .

Example:

You can use an IP address for basic authentication, if the nodes can't use DNS to resolve the hostname.

If you are using Windows authentication, you must enter a Fully Qualified Domain Name in the format dbhost.example.org:1433

Enter the Database Name .

Enter the Username and Password of a user with all privileges on the key storage database.

Select a TLS Database Connection Mode :

Mode

Description

Prefer TLS (default option)

HDS nodes don’t require TLS to connect to the database server. If you enable TLS on the database server, the nodes attempt an encrypted connection.

Require TLS

HDS nodes connect only if the database server can negotiate TLS.

Require TLS and verify certificate signer

This mode isn’t applicable for SQL Server databases.

HDS nodes connect only if the database server can negotiate TLS.

After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection.

Use the Database root certificate control below the drop-down to upload the root certificate for this option.

Require TLS and verify certificate signer and hostname

HDS nodes connect only if the database server can negotiate TLS.

After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection.

The nodes also verify that the hostname in the server certificate matches the hostname in the Database host and port field. The names must match exactly, or the node drops the connection.

Use the Database root certificate control below the drop-down to upload the root certificate for this option.

When you upload the root certificate (if necessary) and click Continue , the HDS Setup Tool tests the TLS connection to the database server. The tool also verifies the certificate signer and hostname, if applicable. If a test fails, the tool shows an error message describing the problem. You can choose whether to ignore the error and continue with the setup. (Because of connectivity differences, the HDS nodes might be able to establish the TLS connection even if the HDS Setup Tool machine can't successfully test it.)

On the System Logs page, configure your Syslogd server:

Enter the syslog server URL.

If the server isn’t DNS-resolvable from the nodes for your HDS cluster, use an IP address in the URL.

Example:

If you set up your server to use TLS encryption, check Is your server configured for TLS negotiation/handshake?

If you check this check box, make sure you enter a TCP URL such as tcp://10.92.43.23:514 , and upload the syslog root certificate.

From the Choose syslog record termination drop-down, choose the appropriate setting for your ISO file: Choose  or  Newline is used for Graylog and Rsyslog TCP

Null byte -- \x00

Newline -- \n —Select this choice for Graylog and Rsyslog TCP.

Click Continue .

(Optional) You can change the default value for some database connection parameters in Advanced Settings . Generally, this parameter is the only one that you might want to change:

```
app_datasource_connection_pool_maxSize: 10
```

Click Continue on the Reset Service Accounts Password screen.

Service account passwords have a nine-month lifespan. Use this screen when your passwords are nearing expiry or you want to reset them to invalidate previous ISO files.

Click Download ISO File . Save the file in a location that's easy to find.

Make a backup copy of the ISO file on your local system.

Keep the backup copy secure. This file contains a master encryption key for the database contents. Restrict access to only those Hybrid Data Security administrators who should make configuration changes.

To shut down the Setup tool, type CTRL+C .

What to do next

Back up the configuration ISO file. You need it to create more nodes for recovery, or to make configuration changes. If you lose all copies of the ISO file, you've also lost the master key. Recovering the keys from your PostgreSQL or Microsoft SQL Server database isn't possible.

We never have a copy of this key and can't help if you lose it.

### Install the HDS Host OVA

Use the VMware vSphere client on your computer to log into the ESXi virtual host.

Select File > Deploy OVF Template .

In the wizard, specify the location of the OVA file that you downloaded earlier, and then click Next .

On the Select a name and folder page, enter a Virtual machine name for the node (for example, "HDS_Node_1"), choose a location where the virtual machine node deployment can reside, and then click Next .

On the Select a compute resource page, choose the destination compute resource, and then click Next .

A validation check runs. After it finishes, the template details appear.

Verify the template details and then click Next .

If you are asked to choose the resource configuration on the Configuration page, click 4 CPU and then click Next .

On the Select storage page, click Next to accept the default disk format and VM storage policy.

On the Select networks page, choose the network option from the list of entries to provide the desired connectivity to the VM.

On the Customize template page, configure the following network settings:

You do not need to set the domain to match the domain that you used to obtain the X.509 certificate.

To ensure a successful registration to the cloud, use only lowercase characters in the FQDN or hostname that you set for the node. Capitalization is not supported at this time.

The total length of the FQDN must not exceed 64 characters.

Your node should have an internal IP address and DNS name. DHCP is not supported.

- Mask —Enter the subnet mask address in dot-decimal notation. For example, 255.255.255.0 .

- Gateway —Enter the gateway IP address. A gateway is a network node that serves as an access point to another network.

- DNS Servers —Enter a comma-separated list of DNS servers, which handle translating domain names to numeric IP addresses. (Up to 4 DNS entries are allowed.)

- NTP Servers —Enter your organization's NTP server or another external NTP server that can be used in your organization. The default NTP servers may not work for all enterprises. You can also use a comma-separated list to enter multiple NTP servers.

Deploy all the nodes on the same subnet or VLAN, so that all nodes in a cluster are reachable from clients in your network for administrative purposes.

If preferred, you can skip the network setting configuration and follow the steps in Set up the Hybrid Data Security VM to configure the settings from the node console.

The option to configure network settings during OVA deployment has been tested with ESXi 7.0 and 8.0. The option may not be available in earlier versions.

Right-click the node VM, and then choose Power > Power On .

The Hybrid Data Security software is installed as a guest on the VM Host. You are now ready to sign in to the console and configure the node.

Troubleshooting Tips

You may experience a delay of a few minutes before the node containers come up. A bridge firewall message appears on the console during first boot, during which you can't sign in.

### Set up the Hybrid Data Security VM

Use this procedure to sign in to the Hybrid Data Security node VM console for the first time and set the sign-in credentials. You can also use the console to configure the network settings for the node if you didn't configure them at the time of OVA deployment.

In the VMware vSphere client, select your Hybrid Data Security node VM and select the Console tab.

The VM boots up and a login prompt appears. If the login prompt does not display, press Enter .

Use the following default login and password to sign in and change the credentials:

Login: admin

Password: ciscosystems

Since you are signing in to your VM for the first time, you are required to change the administrator password.

If you already configured the network settings in Install the HDS Host OVA , skip the rest of this procedure. Otherwise, in the main menu, select the Edit Configuration option.

Set up a static configuration with IP address, Mask, Gateway and DNS information. Your node should have an internal IP address and DNS name. DHCP is not supported.

(Optional) Change the hostname, domain or NTP server(s), if needed to match your network policy.

You do not need to set the domain to match the domain that you used to obtain the X.509 certificate.

Save the network configuration and reboot the VM so that the changes take effect.

### Upload and Mount the HDS Configuration ISO

Before you begin

Because the ISO file holds the master key, it should only be exposed on a "need to know" basis, for access by the Hybrid Data Security VMs and any administrators who might need to make changes. Make sure that only those administrators can access the datastore.

Upload the ISO file from your computer:

In the VMware vSphere client's left navigation pane, click on the ESXi server.

On the Configuration tab's Hardware list, click Storage .

In the Datastores list, right-click on the datastore for your VMs and click Browse Datastore .

Click on the Upload Files icon, and then click Upload File .

Browse to the location where you downloaded the ISO file on your computer and click Open .

Click Yes to accept the upload/download operation warning, and close the datastore dialog.

Mount the ISO file:

In the VMware vSphere client's left navigation pane, right-click on the VM and click Edit Settings .

Click OK to accept the restricted edit options warning.

Click CD/DVD Drive 1 , select the option to mount from a datastore ISO file, and browse to the location where you uploaded the configuration ISO file.

Check Connected and Connect at power on .

Save your changes and reboot the virtual machine.

What to do next

If your IT policy requires, you can optionally unmount the ISO file after all your
                nodes pick up the configuration changes. See (Optional) Unmount ISO After HDS Configuration for details.

### Configure the HDS Node for Proxy Integration

If the network environment requires a proxy, use this procedure to specify the type of proxy that you want to integrate with Hybrid Data Security. If you choose a transparent inspecting proxy or an HTTPS explicit proxy, you can use the node's interface to upload and install the root certificate. You can also check the proxy connection from the interface, and troubleshoot any potential issues.

Before you begin

See Proxy Support for an overview of the supported proxy options.

Proxy Server Requirements

Enter the HDS node setup URL https://[HDS Node IP or FQDN]/setup in a web browser, enter the admin credentials that you set up for the node, and then click Sign In .

Go to Trust Store & Proxy , and then choose an option:

- No Proxy —The default option before you integrate a proxy. No certificate update is required.

- Transparent Non-Inspecting Proxy —Nodes are not configured to use a specific proxy server address and should not require any changes to work with a non-inspecting proxy. No certificate update is required.

- Transparent Inspecting Proxy —Nodes are not configured to use a specific proxy server address. No HTTPS configuration changes are necessary on the Hybrid Data Security deployment, however, the HDS nodes need a root certificate so that they trust the proxy. Inspecting proxies are typically used by IT to enforce policies on which websites can be visited and which types of content are not permitted. This type of proxy decrypts all your traffic (even HTTPS).

Proxy IP/FQDN —Address that can be used to reach the proxy machine.

Proxy Port —A port number that the proxy uses to listen for proxied traffic.

Proxy Protocol —Choose http (views and controls all requests that are received from the client) or https (provides a channel to the server and the client receives and validates the server's certificate). Choose an option based on what your proxy server supports.

Authentication Type —Choose from among the following authentication types:

None —No further authentication is required.

Available for HTTP or HTTPS proxies.

Basic —Used for an HTTP User Agent to provide a user name and password when making a request. Uses Base64 encoding.

Available for HTTP or HTTPS proxies.

If you choose this option, you must also enter the user name and password.

Digest —Used to confirm the account before sending sensitive information. Applies a hash function on the user name and password before sending over the network.

Available for HTTPS proxies only.

If you choose this option, you must also enter the user name and password.

Follow the next steps for a transparent inspecting proxy, an HTTP explicit proxy with Basic authentication, or an HTTPS explicit proxy.

Click Upload a Root Certificate or End Entity Certificate , and then navigate to a choose the root certificate for the proxy.

The certificate is uploaded but not yet installed because you must reboot the node to install the certificate. Click the chevron arrow by the certificate issuer name to get more details or click Delete if you made a mistake and want to reupload the file.

Click Check Proxy Connection to test the network connectivity between the node and the proxy.

If the connection test fails, you'll see an error message that shows the reason and how you can correct the issue.

If you see a message saying that external DNS resolution was not successful, the node was unable to reach the DNS server. This condition is expected in many explicit proxy configurations. You can continue with the setup, and the node will function in Blocked External DNS Resolution mode. If you think this is an error, complete these steps, and then see Turn off Blocked External DNS Resolution Mode .

After the connection test passes, for explicit proxy set to https only, turn the toggle on to Route all port 443/444 https requests from this node through the explicit proxy . This setting requires 15 seconds to take effect.

Click Install All Certificates Into the Trust Store (﻿appears for an HTTPS explicit proxy or a transparent inspecting proxy) or Reboot (appears for an HTTP explicit proxy), read the prompt, and then click Install if you're ready.

The node reboots within a few minutes.

After the node reboots, sign in again if needed, and then open the Overview page to check the connectivity checks to make sure they are all in green status.

The proxy connection check only tests a subdomain of webex.com. If there are connectivity problems, a common issue is that some of the cloud domains listed in the install instructions are being blocked at the proxy.

### Register the First Node in the Cluster

When you register your first node, you create a cluster to which the node is assigned. A cluster contains one or more nodes deployed to provide redundancy.

Before you begin

Once you begin registration of a node, you must complete it within 60 minutes or you have to start over.

Ensure that any pop-up blockers in your browser are disabled or that you allow an exception for admin.webex.com.

Sign in to https://admin.webex.com .

From the menu on the left side of the screen, select Services .

In the Hybrid Services section, find Hybrid Data Security and click Set up .

The Register Hybrid Data Security Node page appears.

Select Yes to indicate that you have set up the node and are ready to register it, and then click Next .

In the first field, enter a name for the cluster to which you want to assign your Hybrid Data Security node.

We recommend that you name a cluster based on where the nodes of the cluster are located geographically. Examples: "San Francisco" or "New York" or "Dallas"

In the second field, enter the internal IP address or fully qualified domain name (FQDN) of your node and click Next .

This IP address or FQDN should match the IP address or hostname and domain that you used in Set up the Hybrid Data Security VM .

A message appears indicating you can register your node to the Webex.

Click Go to Node .

Click Continue in the warning message.

After a few moments, you are redirected to the node connectivity tests for Webex services. If all tests are successful, the Allow Access to Hybrid Data Security Node page appears. There, you confirm that you want to give permissions to your Webex organization to access your node.

Check the Allow Access to Your Hybrid Data Security Node checkbox, and then click Continue .

Your account is validated and the "Registration Complete" message indicates that your node is now registered to the Webex cloud.

Click the link or close the tab to go back to the Control Hub
                    Hybrid Data Security page.

On the Hybrid Data Security page, the new cluster containing the node that you registered is displayed. The node will automatically download the latest software from the cloud.

### Create and Register More Nodes

At this time, the backup VMs that you created in Complete the Prerequisites for Hybrid Data Security are standby hosts which are only used in the event of disaster recovery; they are not registered with the system until then. For details, see Disaster Recovery using Standby Data Center .

Before you begin

Once you begin registration of a node, you must complete it within 60 minutes or you have to start over.

Ensure that any pop-up blockers in your browser are disabled or that you allow an exception for admin.webex.com.

Create a new virtual machine from the OVA, repeating the steps in Install the HDS Host OVA .

Set up the initial configuration on the new VM, repeating the steps in Set up the Hybrid Data Security VM .

On the new VM, repeat the steps in Upload and Mount the HDS Configuration ISO .

If you are setting up a proxy for your deployment, repeat the steps in Configure the HDS Node for Proxy Integration as needed for the new node.

Register the node.

In https://admin.webex.com , select Services from the menu on the left side of the screen.

In the Hybrid Services section, find the Hybrid Data Security card and click Resources .

The Hybrid Data Security Resources page appears.

Click Add Resource .

In the first field, select the name of your existing cluster.

In the second field, enter the internal IP address or fully qualified domain name (FQDN) of your node and click Next .

A message appears indicating you can register your node to the Webex cloud.

Click Go to Node .

After a few moments, you are redirected to the node connectivity tests for Webex services. If all tests are successful, the Allow Access to Hybrid Data Security Node page appears. There, you confirm that you want to give permissions to your organization to access your node.

Check the Allow Access to Your Hybrid Data Security Node checkbox, and then click Continue .

Your account is validated and the "Registration Complete" message indicates that your node is now registered to the Webex cloud.

Click the link or close the tab to go back to the Control Hub
                            Hybrid Data Security page.

Your node is registered. Note that until you start a trial, your nodes generate an alarm indicating that your service is not yet activated.

What to do next

| 1 | Download Installation Files Download the OVA file to your local machine for later use. |
|---|---|
| 2 | Create a Configuration ISO for the HDS Hosts Use the HDS Setup Tool to create an ISO configuration file for the Hybrid Data Security nodes. |
| 3 | Install the HDS Host OVA Create a virtual machine from the OVA file and perform initial configuration,
                        such as network settings. The option to configure network settings during OVA deployment has been tested with ESXi 7.0 and 8.0. The option may not be available in earlier versions. |
| 4 | Set up the Hybrid Data Security VM Sign in to the VM console and set the sign-in credentials. Configure the
                        network settings for the node if you didn't configure them at the time of
                        OVA deployment. |
| 5 | Upload and Mount the HDS Configuration ISO Configure the VM from the ISO configuration file that you created with the
                        HDS Setup Tool. |
| 6 | Configure the HDS Node for Proxy Integration If the network environment requires proxy configuration, specify the type of proxy that you will use for the node, and add the proxy certificate to the trust store if needed. |
| 7 | Register the First Node in the Cluster Register the VM with the Cisco Webex cloud as a Hybrid Data Security node. |
| 8 | Create and Register More Nodes Complete the cluster setup. |
| 9 | Until you start a trial, your nodes generate an alarm indicating that your service is not yet activated. |

| 1 | Sign in to https://admin.webex.com , and then click Services . |
|---|---|
| 2 | In the Hybrid Services section, find the Hybrid Data Security card, and then click Set up . If
                                                  the card is disabled or you don’t see it, contact
                                                  your account team or your partner organization.
                                                  Give them your account number and ask to enable
                                                  your organization for Hybrid Data Security. To find the account number, click the gear at
                                                  the top right, next to your organization name. You can also download the OVA at any time from
                                                  the Help section on the Settings page. On the Hybrid Data Security card, click Edit
                                                  settings to open the page. Then, click Download Hybrid Data Security
                                                  software in the Help section. Older versions of the software package (OVA) will not be compatible with the latest Hybrid Data Security upgrades. This can result in issues while upgrading the application. Make sure you download the latest version of the OVA file. |
| 3 | Select No to indicate
                                                  that you haven’t set up the node yet, and then
                                                  click Next . The OVA file automatically begins to
                                                  download. Save the file to a location on your
                                                  machine. |
| 4 | Optionally, click Open Deployment
                                                  Guide to check if there’s a later
                                                  version of this guide available. |

| Description | Variable |
|---|---|
| HTTP Proxy without authentication | GLOBAL_AGENT_HTTP_PROXY=http://SERVER_IP:PORT |
| HTTPS Proxy without authentication | GLOBAL_AGENT_HTTPS_PROXY=http://SERVER_IP:PORT |
| HTTP Proxy with authentication | GLOBAL_AGENT_HTTP_PROXY=http://USERNAME:PASSWORD@SERVER_IP:PORT |
| HTTPS Proxy with authentication | GLOBAL_AGENT_HTTPS_PROXY=http://USERNAME:PASSWORD@SERVER_IP:PORT |

| 1 | At your machine's command line, enter the appropriate command for your environment: In regular environments: docker rmi ciscocitg/hds-setup:stable In FedRAMP environments: docker rmi ciscocitg/hds-setup-fedramp:stable This step cleans up previous HDS setup tool images. If there are no previous images, it returns an error which you can ignore. |
|---|---|
| 2 | To sign in to the Docker image registry, enter the following: docker login -u hdscustomersro |
| 3 | At the password prompt, enter this hash: dckr_pat_aDP6V4KkrvpBwaQf6m6ROkvKUIo |
| 4 | Download the latest stable image for your environment: In regular environments: docker pull ciscocitg/hds-setup:stable In FedRAMP environments: docker pull ciscocitg/hds-setup-fedramp:stable |
| 5 | When the pull completes, enter the appropriate command for your environment: In regular environments without a proxy: docker run -p 8080:8080 --rm -it ciscocitg/hds-setup:stable In regular environments with an HTTP proxy: docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTP_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup:stable In regular environments with an HTTPS proxy: docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTPS_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup:stable In FedRAMP environments without a proxy: docker run -p 8080:8080 --rm -it ciscocitg/hds-setup-fedramp:stable In FedRAMP environments with an HTTP proxy: docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTP_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup-fedramp:stable In FedRAMP environments with an HTTPS proxy: docker run -p 8080:8080 --rm -it -e GLOBAL_AGENT_HTTPS_PROXY=http://SERVER_IP:PORT ciscocitg/hds-setup-fedramp:stable When the container is running, you see "Express server listening on port
                        8080." |
| 6 | The Setup tool does not support connecting to localhost through http://localhost:8080 . Use http://127.0.0.1:8080 to connect to localhost. Use a web browser to go to the localhost, http://127.0.0.1:8080 , and enter customer admin username for Control Hub at the prompt. The tool uses this first entry of the username to set the proper environment for that account. The tool then displays the standard sign-in prompt. |
| 7 | When prompted, enter your Control Hub customer admin sign-in credentials, and then click Log in to allow access to the required services for Hybrid Data Security. |
| 8 | On the Setup Tool overview page, click Get Started . |
| 9 | On the ISO Import page, you have these options: No —If you’re creating your first HDS node, you don't have an ISO file to upload. Yes —If you already created HDS nodes, then you select your ISO file in the browse and upload it. |
| 10 | Check that your X.509 certificate meets the requirements in X.509 Certificate Requirements . If you never uploaded a certificate before, upload the X.509 certificate, enter the password, and click Continue . If your certificate is OK, click Continue . If your certificate has expired or you want to replace it, select No for Continue using HDS certificate chain and private key from previous ISO? . Upload a new X.509 certificate, enter the password, and click Continue . |
| 11 | Enter the database address and account for HDS to access your key datastore: Select your Database Type ( PostgreSQL or Microsoft SQL Server ). If you choose Microsoft SQL Server , you get an Authentication Type field. ( Microsoft SQL Server only) Select your Authentication Type : Basic Authentication : You need a local SQL Server account name in the Username field. Windows Authentication : You need a Windows account in the format username@DOMAIN in the Username field. Enter the database server address in the form <hostname>:<port> or <IP-address>:<port> . Example: dbhost.example.org:1433 or 198.51.100.17:1433 You can use an IP address for basic authentication, if the nodes can't use DNS to resolve the hostname. If you are using Windows authentication, you must enter a Fully Qualified Domain Name in the format dbhost.example.org:1433 Enter the Database Name . Enter the Username and Password of a user with all privileges on the key storage database. |
| 12 | Select a TLS Database Connection Mode : Mode Description Prefer TLS (default option) HDS nodes don’t require TLS to connect to the database server. If you enable TLS on the database server, the nodes attempt an encrypted connection. Require TLS HDS nodes connect only if the database server can negotiate TLS. Require TLS and verify certificate signer This mode isn’t applicable for SQL Server databases. HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. Require TLS and verify certificate signer and hostname HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. The nodes also verify that the hostname in the server certificate matches the hostname in the Database host and port field. The names must match exactly, or the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. When you upload the root certificate (if necessary) and click Continue , the HDS Setup Tool tests the TLS connection to the database server. The tool also verifies the certificate signer and hostname, if applicable. If a test fails, the tool shows an error message describing the problem. You can choose whether to ignore the error and continue with the setup. (Because of connectivity differences, the HDS nodes might be able to establish the TLS connection even if the HDS Setup Tool machine can't successfully test it.) | Mode | Description | Prefer TLS (default option) | HDS nodes don’t require TLS to connect to the database server. If you enable TLS on the database server, the nodes attempt an encrypted connection. | Require TLS | HDS nodes connect only if the database server can negotiate TLS. | Require TLS and verify certificate signer | This mode isn’t applicable for SQL Server databases. HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. | Require TLS and verify certificate signer and hostname | HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. The nodes also verify that the hostname in the server certificate matches the hostname in the Database host and port field. The names must match exactly, or the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. |
| Mode | Description |
| Prefer TLS (default option) | HDS nodes don’t require TLS to connect to the database server. If you enable TLS on the database server, the nodes attempt an encrypted connection. |
| Require TLS | HDS nodes connect only if the database server can negotiate TLS. |
| Require TLS and verify certificate signer | This mode isn’t applicable for SQL Server databases. HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. |
| Require TLS and verify certificate signer and hostname | HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. The nodes also verify that the hostname in the server certificate matches the hostname in the Database host and port field. The names must match exactly, or the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. |
| 13 | On the System Logs page, configure your Syslogd server: Enter the syslog server URL. If the server isn’t DNS-resolvable from the nodes for your HDS cluster, use an IP address in the URL. Example: udp://10.92.43.23:514 indicates logging to Syslogd host 10.92.43.23 on UDP port 514. If you set up your server to use TLS encryption, check Is your server configured for TLS negotiation/handshake? If you check this check box, make sure you enter a TCP URL such as tcp://10.92.43.23:514 , and upload the syslog root certificate. From the Choose syslog record termination drop-down, choose the appropriate setting for your ISO file: Choose  or  Newline is used for Graylog and Rsyslog TCP Null byte -- \x00 Newline -- \n —Select this choice for Graylog and Rsyslog TCP. Click Continue . |
| 14 | (Optional) You can change the default value for some database connection parameters in Advanced Settings . Generally, this parameter is the only one that you might want to change: app_datasource_connection_pool_maxSize: 10 |
| 15 | Click Continue on the Reset Service Accounts Password screen. Service account passwords have a nine-month lifespan. Use this screen when your passwords are nearing expiry or you want to reset them to invalidate previous ISO files. |
| 16 | Click Download ISO File . Save the file in a location that's easy to find. |
| 17 | Make a backup copy of the ISO file on your local system. Keep the backup copy secure. This file contains a master encryption key for the database contents. Restrict access to only those Hybrid Data Security administrators who should make configuration changes. |
| 18 | To shut down the Setup tool, type CTRL+C . |

| Mode | Description |
|---|---|
| Prefer TLS (default option) | HDS nodes don’t require TLS to connect to the database server. If you enable TLS on the database server, the nodes attempt an encrypted connection. |
| Require TLS | HDS nodes connect only if the database server can negotiate TLS. |
| Require TLS and verify certificate signer | This mode isn’t applicable for SQL Server databases. HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. |
| Require TLS and verify certificate signer and hostname | HDS nodes connect only if the database server can negotiate TLS. After establishing a TLS connection, the node compares the signer of the certificate from the database server to the certificate authority in the Database root certificate . If they don't match, the node drops the connection. The nodes also verify that the hostname in the server certificate matches the hostname in the Database host and port field. The names must match exactly, or the node drops the connection. Use the Database root certificate control below the drop-down to upload the root certificate for this option. |

| 1 | Use the VMware vSphere client on your computer to log into the ESXi virtual host. |
|---|---|
| 2 | Select File > Deploy OVF Template . |
| 3 | In the wizard, specify the location of the OVA file that you downloaded earlier, and then click Next . |
| 4 | On the Select a name and folder page, enter a Virtual machine name for the node (for example, "HDS_Node_1"), choose a location where the virtual machine node deployment can reside, and then click Next . |
| 5 | On the Select a compute resource page, choose the destination compute resource, and then click Next . A validation check runs. After it finishes, the template details appear. |
| 6 | Verify the template details and then click Next . |
| 7 | If you are asked to choose the resource configuration on the Configuration page, click 4 CPU and then click Next . |
| 8 | On the Select storage page, click Next to accept the default disk format and VM storage policy. |
| 9 | On the Select networks page, choose the network option from the list of entries to provide the desired connectivity to the VM. |
| 10 | On the Customize template page, configure the following network settings: Hostname —Enter the FQDN (hostname and domain) or a single word hostname for the node. You do not need to set the domain to match the domain that you used to obtain the X.509 certificate. To ensure a successful registration to the cloud, use only lowercase characters in the FQDN or hostname that you set for the node. Capitalization is not supported at this time. The total length of the FQDN must not exceed 64 characters. IP Address — Enter the IP address for the internal interface of the node. Your node should have an internal IP address and DNS name. DHCP is not supported. Mask —Enter the subnet mask address in dot-decimal notation. For example, 255.255.255.0 . Gateway —Enter the gateway IP address. A gateway is a network node that serves as an access point to another network. DNS Servers —Enter a comma-separated list of DNS servers, which handle translating domain names to numeric IP addresses. (Up to 4 DNS entries are allowed.) NTP Servers —Enter your organization's NTP server or another external NTP server that can be used in your organization. The default NTP servers may not work for all enterprises. You can also use a comma-separated list to enter multiple NTP servers. Deploy all the nodes on the same subnet or VLAN, so that all nodes in a cluster are reachable from clients in your network for administrative purposes. If preferred, you can skip the network setting configuration and follow the steps in Set up the Hybrid Data Security VM to configure the settings from the node console. The option to configure network settings during OVA deployment has been tested with ESXi 7.0 and 8.0. The option may not be available in earlier versions. |
| 11 | Right-click the node VM, and then choose Power > Power On . The Hybrid Data Security software is installed as a guest on the VM Host. You are now ready to sign in to the console and configure the node. Troubleshooting Tips You may experience a delay of a few minutes before the node containers come up. A bridge firewall message appears on the console during first boot, during which you can't sign in. |

| 1 | In the VMware vSphere client, select your Hybrid Data Security node VM and select the Console tab. The VM boots up and a login prompt appears. If the login prompt does not display, press Enter . |
|---|---|
| 2 | Use the following default login and password to sign in and change the credentials: Login: admin Password: ciscosystems Since you are signing in to your VM for the first time, you are required to change the administrator password. |
| 3 | If you already configured the network settings in Install the HDS Host OVA , skip the rest of this procedure. Otherwise, in the main menu, select the Edit Configuration option. |
| 4 | Set up a static configuration with IP address, Mask, Gateway and DNS information. Your node should have an internal IP address and DNS name. DHCP is not supported. |
| 5 | (Optional) Change the hostname, domain or NTP server(s), if needed to match your network policy. You do not need to set the domain to match the domain that you used to obtain the X.509 certificate. |
| 6 | Save the network configuration and reboot the VM so that the changes take effect. |

| 1 | Upload the ISO file from your computer: In the VMware vSphere client's left navigation pane, click on the ESXi server. On the Configuration tab's Hardware list, click Storage . In the Datastores list, right-click on the datastore for your VMs and click Browse Datastore . Click on the Upload Files icon, and then click Upload File . Browse to the location where you downloaded the ISO file on your computer and click Open . Click Yes to accept the upload/download operation warning, and close the datastore dialog. |
|---|---|
| 2 | Mount the ISO file: In the VMware vSphere client's left navigation pane, right-click on the VM and click Edit Settings . Click OK to accept the restricted edit options warning. Click CD/DVD Drive 1 , select the option to mount from a datastore ISO file, and browse to the location where you uploaded the configuration ISO file. Check Connected and Connect at power on . Save your changes and reboot the virtual machine. |

| 1 | Enter the HDS node setup URL https://[HDS Node IP or FQDN]/setup in a web browser, enter the admin credentials that you set up for the node, and then click Sign In . |
|---|---|
| 2 | Go to Trust Store & Proxy , and then choose an option: No Proxy —The default option before you integrate a proxy. No certificate update is required. Transparent Non-Inspecting Proxy —Nodes are not configured to use a specific proxy server address and should not require any changes to work with a non-inspecting proxy. No certificate update is required. Transparent Inspecting Proxy —Nodes are not configured to use a specific proxy server address. No HTTPS configuration changes are necessary on the Hybrid Data Security deployment, however, the HDS nodes need a root certificate so that they trust the proxy. Inspecting proxies are typically used by IT to enforce policies on which websites can be visited and which types of content are not permitted. This type of proxy decrypts all your traffic (even HTTPS). Explicit Proxy —With explicit proxy, you tell the client (HDS nodes) which proxy server to use, and this option supports several authentication types. After you choose this option, you must enter the following information: Proxy IP/FQDN —Address that can be used to reach the proxy machine. Proxy Port —A port number that the proxy uses to listen for proxied traffic. Proxy Protocol —Choose http (views and controls all requests that are received from the client) or https (provides a channel to the server and the client receives and validates the server's certificate). Choose an option based on what your proxy server supports. Authentication Type —Choose from among the following authentication types: None —No further authentication is required. Available for HTTP or HTTPS proxies. Basic —Used for an HTTP User Agent to provide a user name and password when making a request. Uses Base64 encoding. Available for HTTP or HTTPS proxies. If you choose this option, you must also enter the user name and password. Digest —Used to confirm the account before sending sensitive information. Applies a hash function on the user name and password before sending over the network. Available for HTTPS proxies only. If you choose this option, you must also enter the user name and password. Follow the next steps for a transparent inspecting proxy, an HTTP explicit proxy with Basic authentication, or an HTTPS explicit proxy. |
| 3 | Click Upload a Root Certificate or End Entity Certificate , and then navigate to a choose the root certificate for the proxy. The certificate is uploaded but not yet installed because you must reboot the node to install the certificate. Click the chevron arrow by the certificate issuer name to get more details or click Delete if you made a mistake and want to reupload the file. |
| 4 | Click Check Proxy Connection to test the network connectivity between the node and the proxy. If the connection test fails, you'll see an error message that shows the reason and how you can correct the issue. If you see a message saying that external DNS resolution was not successful, the node was unable to reach the DNS server. This condition is expected in many explicit proxy configurations. You can continue with the setup, and the node will function in Blocked External DNS Resolution mode. If you think this is an error, complete these steps, and then see Turn off Blocked External DNS Resolution Mode . |
| 5 | After the connection test passes, for explicit proxy set to https only, turn the toggle on to Route all port 443/444 https requests from this node through the explicit proxy . This setting requires 15 seconds to take effect. |
| 6 | Click Install All Certificates Into the Trust Store (﻿appears for an HTTPS explicit proxy or a transparent inspecting proxy) or Reboot (appears for an HTTP explicit proxy), read the prompt, and then click Install if you're ready. The node reboots within a few minutes. |
| 7 | After the node reboots, sign in again if needed, and then open the Overview page to check the connectivity checks to make sure they are all in green status. The proxy connection check only tests a subdomain of webex.com. If there are connectivity problems, a common issue is that some of the cloud domains listed in the install instructions are being blocked at the proxy. |

| 1 | Sign in to https://admin.webex.com . |
|---|---|
| 2 | From the menu on the left side of the screen, select Services . |
| 3 | In the Hybrid Services section, find Hybrid Data Security and click Set up . The Register Hybrid Data Security Node page appears. |
| 4 | Select Yes to indicate that you have set up the node and are ready to register it, and then click Next . |
| 5 | In the first field, enter a name for the cluster to which you want to assign your Hybrid Data Security node. We recommend that you name a cluster based on where the nodes of the cluster are located geographically. Examples: "San Francisco" or "New York" or "Dallas" |
| 6 | In the second field, enter the internal IP address or fully qualified domain name (FQDN) of your node and click Next . This IP address or FQDN should match the IP address or hostname and domain that you used in Set up the Hybrid Data Security VM . A message appears indicating you can register your node to the Webex. |
| 7 | Click Go to Node . |
| 8 | Click Continue in the warning message. After a few moments, you are redirected to the node connectivity tests for Webex services. If all tests are successful, the Allow Access to Hybrid Data Security Node page appears. There, you confirm that you want to give permissions to your Webex organization to access your node. |
| 9 | Check the Allow Access to Your Hybrid Data Security Node checkbox, and then click Continue . Your account is validated and the "Registration Complete" message indicates that your node is now registered to the Webex cloud. |
| 10 | Click the link or close the tab to go back to the Control Hub
                    Hybrid Data Security page. On the Hybrid Data Security page, the new cluster containing the node that you registered is displayed. The node will automatically download the latest software from the cloud. |

| 1 | Create a new virtual machine from the OVA, repeating the steps in Install the HDS Host OVA . |
|---|---|
| 2 | Set up the initial configuration on the new VM, repeating the steps in Set up the Hybrid Data Security VM . |
| 3 | On the new VM, repeat the steps in Upload and Mount the HDS Configuration ISO . |
| 4 | If you are setting up a proxy for your deployment, repeat the steps in Configure the HDS Node for Proxy Integration as needed for the new node. |
| 5 | Register the node. In https://admin.webex.com , select Services from the menu on the left side of the screen. In the Hybrid Services section, find the Hybrid Data Security card and click Resources . The Hybrid Data Security Resources page appears. Click Add Resource . In the first field, select the name of your existing cluster. In the second field, enter the internal IP address or fully qualified domain name (FQDN) of your node and click Next . A message appears indicating you can register your node to the Webex cloud. Click Go to Node . After a few moments, you are redirected to the node connectivity tests for Webex services. If all tests are successful, the Allow Access to Hybrid Data Security Node page appears. There, you confirm that you want to give permissions to your organization to access your node. Check the Allow Access to Your Hybrid Data Security Node checkbox, and then click Continue . Your account is validated and the "Registration Complete" message indicates that your node is now registered to the Webex cloud. Click the link or close the tab to go back to the Control Hub
                            Hybrid Data Security page. Your node is registered. Note that until you start a trial, your nodes generate an alarm indicating that your service is not yet activated. |