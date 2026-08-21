---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-config-esrst-html-29c597398e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/config_esrst.html
retrieved_at: 2026-08-21T23:38:05.146195+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Configuring E-SRST Site Provisioning

## Chapter: Configuring E-SRST Site Provisioning

## Configuring E-SRST Site Provisioning

When enabled on a site, the Cisco Unified SRST Manager E-SRST functionality provides automated remote site provisioning of the following advanced telephony features in survivable mode by gathering the information from Cisco Unified Communications Manager:

- After-hours

- Call pickup and group pickup

- Call routing restrictions (local and long distance, and time of day)

- Class of restrictions

- Dial Plan

- Hunt groups

- Phones and extensions (speed dials, lines, softkeys)

- Pick-up groups

Note Cisco Unified SRST Manager software does not support provisioning Media Gateway Control Protocol (MGCP) dial plan. Cisco has removed the support for this feature due to the complexity of and differences between dial plans across the globe. These complexities and differences must be analyzed by a Cisco engineering team member to understand whether the Cisco Unified SRST Manager dial plan logic can meet customer requirements. If you are interested in automatic dial plan provisioning, contact srstmgr@cisco.com. The Cisco engineering team member requires a copy of your Cisco Unified Communications Manager dial plan (.tar file) for analysis. After analysis, a private build of the Cisco Unified SRST Manager with the dial plan provisioning feature enabled will be delivered.

This section describes the high-level tasks required to configure a site to support E-SRST. Enabling E-SRST requires configuration on Cisco Unified SRST Manager, the Cisco Unified Communications Manager central call agent, and on the CUCME call agent at the branch site. Most of the configuration on Cisco Unified SRST Manager is handled using the GUI.

This procedure assumes that the security certificates have been installed on Cisco Unified SRST Manager. For more information, see About Security for Cisco Unified SRST Manager .

## Using E-SRST to Pull an Advanced Telephony Configuration from CUCM to the Branch Site

This section describes the high-level configuration tasks required to pull advanced telephony configuration information from Cisco Unified Communications Manager to the remote site.

### Initial Configuration Using the Cisco Unified SRST Manager GUI

Before you can configure Cisco Unified SRST Manager to support E-SRST on branch sites, you must first perform the following high-level tasks using the GUI:

1. Configure the Cisco Unified SRST Manager initial values using the setup wizard. For more information, see Using the Setup Wizard .

2. Add the central call agent using the Central Call Agent wizard. For more information, see Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information .

3. Retrieve the Cisco Unified SRST sites. For more information, see Viewing the Cisco Unified SRST References .

### Preparing the Central Cisco Unified Communications Manager Call Agent for E-SRST Provisioning

This section assumes that the advanced telephony features have already been configured on Cisco Unified Communications Manager. For more information, see the Cisco Unified Communications Manager documentation at http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html .

To configure Cisco Unified Communications Manager to prepare for E-SRST provisioning, perform the following steps on Cisco Unified Communications Manager.

Step 1 Configure the Cisco Unified SRST references on Cisco Unified Communications Manager with the following:

- Site name

- Port number for CUCME

- IP address of the router

Step 2 Create a device pool in Cisco Unified Communications Manager that has the SRST reference. Collect the following information:

- Device pool name

- Cisco Unified SRST reference, which must match the site name

- Devices and phones. For each phone that you want to be registered for survivable mode, set the device pool to match the device pool configured in the previous step.

Step 3 Configure the advanced telephony configuration on Cisco Unified Communications Manager that will be downloaded to the branch site using E-SRST provisioning.

Cisco Unified SRST Manager supports selected Cisco Unified Communications Manager features to be downloaded using E-SRST site provisioning, and operates in survivable fallback mode. Table 3 lists the supported features and instructions for preparing for the E-SRST site provisioning.

Table 3 Cisco Unified Communications Manager Advanced Telephony Features Supported in Cisco Unified SRST Manager

Calling search space (CSS) and partitions

Cisco Unified SRST Manager converts the CSS and partitions into cor lists on the branch routers.

Calling search space and partitions on CUCM are typically used to apply restrictions on calling, such as internal, local, national, and international calling restrictions. Cisco Unified SRST Manager applies the configured restrictions using cor lists on the branch routers.

Call pickup and group pickup

Hunt groups

1. Select the Hunt Pilot setting.

2. Select Hunt Pilot .

3. Select Hunt List .

4. Select Device Settings --> Softkey Templates .

Assign this template to all ephones. In fallback mode, these templates are translated into an ephone template, and assigned to the ephones as well. As a result, the same softkey templates that appear in normal connected mode will appear in fallback mode.

Table 4 lists the softkey states and keys that E-SRST provisioning supports.

Table 4 Softkeys Supported for E-SRST Provisioning

Alerting

Endcall

Connected

Endcall, HLog, Hold, Join, Park, RmLstC, Select, TrnsfVM, Trnsfer

Hold

Join, Newcall, Resume, Select

Idle

Cfwdall, Dnd, Gpickup, Hlog, Join, Newcall, Pickup, Redial, RmLstC

Remote-in-use

Cbarge, Newcall

Ringing

Answer, Dnd, Hlog

Seized

CallBack, Cfwdall, Endcall, Gpickup, Hlog, Pickup, Redial

### Configuring the Cisco Unified Communications Manager Express Branch Call Agent to Prepare for E-SRST Provisioning

The E-SRST solution requires that Cisco Unified Communications Manager Express (CUCME) be configured in Cisco Unified SRST fallback mode. For more information, see the Cisco Unified Communications Manager Express Administrator Guide .

The Cisco Unified Communications Manager Express site must also be configured with additional CLI commands to ensure that Cisco Unified SRST Manager can contact the Cisco Unified Communications Manager Express site. This enables Cisco Unified SRST Manager to transfer configuration information from the Cisco Unified Communications Manager to the branch site.

The communication between Cisco Unified SRST Manager and Cisco Unified Communications Manager Express can use local authentication or HTTPS authentication. The following sections describe the procedures for preparing CUCME:

### Configuring Communication with CUCME by Local Authentication

Perform the following procedure in CUCME to configure communication between Cisco Unified SRST Manager and CUCME using local authentication:

Procedure for Using Local Authentication

Step 1 Configure the user telnet name and password for the interface that connects back to Cisco Unified SRST Manager.

username name privilege 15 password password

Note Privilege 15 is required for Cisco Unified SRST Manager to push the configurations to the branch site.

Step 2 Enter the line terminal configuration and enter line configuration mode.

line vty 0 4

Step 3 Enable local password checking at login.

login local

Step 4 Define which protocol to use to connect to the branch call agent.

- If TLS is not enabled on Cisco Unified SRST Manager, enter the following command:

transport input telnet

- If TLS is enabled on Cisco Unified SRST Manager, enter the following command:

transport input ssh

Step 5 Enable the IP HTTP server using the following command:

ip http server

Step 6 Set the IP HTTP authentication to the local setting using the following command:

ip http authentication local

Step 7 Enable or disable the HTTPS secure server, depending on whether TLS is enabled on the Cisco Unified SRST Manager:

- If TLS is enabled on Cisco Unified SRST Manager, enter the following command:

ip http secure-server

- If TLS is disabled on Cisco Unified SRST Manager, enter the following command:

no ip http secure-server

If TLS is disabled on Cisco Unified SRST Manager, this setting is required for the Cisco Unified Communications Manager voice configuration to be downloaded to the branch router.

Step 8 Set the IP HTTP flash (include the colon “:” at the end of the command).

ip http path flash:

Step 9 Set the IP HTTP timeout policy using the following command:

ip http timeout policy

### Configuring Communication with CUCME by HTTPS Authentication

Perform the following procedure in CUCME to configure communication between Cisco Unified SRST Manager and CUCME using HTTPS authentication:

Procedure for Using HTTPS Authentication

Step 1 Configure the user telnet name and password for the interface that connects back to Cisco Unified SRST Manager.

username name privilege 15 password password

Note Privilege 15 is required for Cisco Unified SRST Manager to push the configurations to the branch site.

Step 2 Enter the line terminal configuration and enter line configuration mode.

line vty 0 4

Step 3 Enable AAA login authentication.

login authentication https

Step 4 Define ssh as the connection protocol for connecting to the branch call agent.

transport input ssh

Step 5 Enter the following commands individually to configure AAA authentication.

aaa new-model

aaa authentication login https group tacacs+

aaa authorization exec https group tacacs+ if-authenticated

aaa session-id common

ip tacacs source-interface GigabitEthernet0/1

tacacs server ACS

address ipv4 100.100.100.200

key cisco123

single-connection

Step 6 Enable the IP HTTP server using the following command:

ip http server

Step 7 Set IP HTTP AAA authentication.

ip http authentication aaa login-authentication https

ip http authentication aaa exec-authorization https

Step 8 Enable the HTTPS secure server with TLS enabled on the Cisco Unified SRST Manager.

ip http secure-server

Step 9 Set the IP HTTP flash (include the colon “:” at the end of the command).

ip http path flash:

Step 10 Set the IP HTTP timeout policy using the following command:

ip http timeout policy

### Enabling E-SRST Provisioning on the Site Using the Cisco Unified SRST Manager GUI

You must enable E-SRST provisioning using the Cisco Unified SRST Manager GUI for each branch site that will download Cisco Unified Communications Manager telephony configuration during the provisioning process. You can either perform on-demand site provisioning for the site, or configure Cisco Unified SRST Manager to perform scheduled provisioning on the site.

For information, see Viewing and Provisioning Sites .

### Verifying the Updated Configuration on the Branch Call Agent Router

After the E-SRST provisioning is complete, the dial plan and ephone configuration settings configured on the central call agent should be propagated to the branch call agent router. Verify that the updated settings are configured on the site by viewing the dial peer and ephone configuration settings.

| Cisco Unified Communications Manager Advanced Telephony Configuration | Instructions for Preparing the Cisco Unified Communications Manager Feature for E-SRST Site Provisioning |
|---|---|
| Calling search space (CSS) and partitions | Cisco Unified SRST Manager converts the CSS and partitions into cor lists on the branch routers. Calling search space and partitions on CUCM are typically used to apply restrictions on calling, such as internal, local, national, and international calling restrictions. Cisco Unified SRST Manager applies the configured restrictions using cor lists on the branch routers. |
| Call pickup and group pickup |  |
| Hunt groups | 1. Select the Hunt Pilot setting. 2. Select Hunt Pilot . 3. Select Hunt List . 4. Select Device Settings --> Softkey Templates . Assign this template to all ephones. In fallback mode, these templates are translated into an ephone template, and assigned to the ephones as well. As a result, the same softkey templates that appear in normal connected mode will appear in fallback mode. |

| Phone States | Softkey |
|---|---|
| Alerting | Endcall |
| Connected | Endcall, HLog, Hold, Join, Park, RmLstC, Select, TrnsfVM, Trnsfer |
| Hold | Join, Newcall, Resume, Select |
| Idle | Cfwdall, Dnd, Gpickup, Hlog, Join, Newcall, Pickup, Redial, RmLstC |
| Remote-in-use | Cbarge, Newcall |
| Ringing | Answer, Dnd, Hlog |
| Seized | CallBack, Cfwdall, Endcall, Gpickup, Hlog, Pickup, Redial |