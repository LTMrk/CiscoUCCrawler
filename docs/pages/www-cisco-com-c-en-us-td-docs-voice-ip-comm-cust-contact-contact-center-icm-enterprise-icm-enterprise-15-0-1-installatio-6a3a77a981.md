---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-6a3a77a981
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_150_install_upgrade_guide/cli_commands_during_installation_and_upgrade.html
retrieved_at: 2026-08-16T19:57:23.527937+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: CLI Commands

## Chapter: CLI Commands

# CLI Commands

## Live Data CLI Commands

### Supported Character Set for Live Data Installation CLI Commands

When working with
                                 		  the CLI (and not exclusively for Live Data), you can use plain alphanumeric
                                 		  characters [0-9] [A-Z] [a-z] and the following additional characters:

". " (dot)

"!" (exclamation mark)

"@" (at sign)

"#" (number
                                       				sign)

"$" (dollar)

"%" (percent)

"^" (caret)

"*" (star)

"_"
                                       				(underscore)

"+" (plus
                                       				sign)

"=" (equal
                                       				sign)

"~" (tilde)

":" (colon)

"(" and ")"
                                       				(open and close parentheses)

"{" and "}"
                                       				(open and close brackets)

"[" and "]"
                                       				(open and close square brackets)

Spaces are used as
                                 		  input separators. Most special characters carry specific meaning to the Cisco Voice Operating System (VOS)
                                 		  command console (for example, "\", "|", and so on). Characters above standard
                                 		  ASCII are mostly ignored.

### Privilege Levels
                           	 for Live Data Commands

The Live Data CLI
                                 		  commands support the following privilege levels:

Ordinary

Advanced

Each Live Data
                                 		  command has a required privilege level related to the sensitivity of data it
                                 		  exposes or its ability to severely affect the operation of the application. The
                                 		  privilege level for each command is the minimum level required; a user with a
                                 		  higher privilege level also has access to the command.

The Cisco Voice
                                 		  Operating System (VOS) also supports a higher privilege level for the
                                 		  administrative user; this user is configured at installation. When the
                                 		  administrative user creates other users (with the set account name command),
                                 		  the administrative user sets each newly created user's privilege level. (For
                                 		  more information about the set account command, see the Administration Console User Guide for Cisco Unified Intelligence
                                    			 Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html . )

### Live Data AW DB Access

The Live Data AW
                                 		  DB access commands allow you to configure and display CCE AW DB (real-time
                                 		  distributor) access for the Contact Center Enterprise Live Data Product
                                 		  Deployment Selection. 
                                 		By default, the set and show commands also test the connection from Live Data to the primary or secondary AW database, check
                                 to see if the configured user has appropriate AW DB access, and report the results.

#### set live-data
                              	 aw-access

Required Minimum Privilege Level: Advanced

Use this command
                                    		  to set the access information to the primary or secondary CCE AW.   The command also automatically tests the connection
                                    from Live Data to the primary or secondary AW, checks to see if the configured user has appropriate AW DB access, and reports
                                    the results.

You can use the optional skip-test parameter if you do not want the test performed. No  checking is done to see if the configured
                                    user has appropriate AW DB access, and no results are reported.

### Command
                                    			 Syntax

set live-data aw-access {primary | secondary} addr port db user [skip-test]

##### Command Default

When you run this command, it prompts you to specify the login password (maximum 128 characters) to use for authentication
                                    with AW database access.

#### unset live-data
                              	 aw-access

Required Minimum Privilege Level: Advanced

Use this command to unset the access information to the primary or secondary CCE
                                    		  AW DB.

### Command Syntax

unset live-data aw-access
                                       				  {primary | secondary}

There is a single, required parameter with two possible values.

#### show live-data
                              	 aw-access

Required Minimum Privilege Level: Ordinary

Use this command
                                    		  to display the primary and secondary CCE AW DB access information and test the connection from Live Data to each AW DB,
                                    check to see if the configured user (on each node) has appropriate AW DB access, and report the results.

You can use the optional skip-test parameter if you do not want the test performed. No  checking is done to see if the configured
                                    user (on each node) has appropriate AW DB access, and no results are reported.

### Command
                                    			 Syntax

show live-data aw-access [skip-test]

Shows the configured primary and secondary CCE AW DB access information. There are no
                                    		  required parameters.

### Live Data Cluster Configuration

Use the following commands to set, unset, or show Live Data cluster configuration information.

#### set live-data secondary

Required Minimum Privilege Level: Advanced

Use this command to register the Live Data secondary node.

### Command Syntax

set live-data secondary name

#### unset live-data secondary

Required Minimum Privilege Level: Advanced

Use this command to unset Live Data secondary node configuration.

unset live-data secondary

There are no required parameters.

#### show live-data secondary

Required Minimum Privilege Level: Ordinary

Use this command to show Live Data secondary node configuration information.

show live-data secondary

There are no required parameters.

### Live Data Reporting Configuration

#### set live-data
                              	 reporting-interval

Required Minimum Privilege Level: Advanced

Use this command
                                    		  to set the Live Data reporting interval in minutes. The reporting interval is
                                    		  the duration of time for which values are aggregated and reported for the To
                                       			 Interval fields.

### Command
                                    			 Syntax

set live-data reporting-interval reporting-interval-in-minutes

When you set the
                                    		  Live Data reporting interval, restart the publisher and then the subscriber.
                                    		  Restart the inactive node and then the active node by using the utils system
                                       			 restart command. (For more information about the command, refer to the Administration Console User Guide for Cisco Unified Intelligence
                                       			 Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .)

If you restart
                                    		  only the publisher and not the subscriber, the new reporting interval takes
                                    		  effect only on the publisher; likewise, if you restart the subscriber but not
                                    		  the publisher, only the subscriber uses the newly set reporting interval.

When the publisher
                                    		  and the subscriber restart, use the show live-data reporting-interval command
                                    		  to validate the new interval.

#### show live-data reporting-interval

Required Minimum Privilege Level: Ordinary

Use this command
                                    		  to show the configured  and current reporting interval for both the Live Data publisher and subscriber.

### Command Syntax

show live-data reporting-interval

#### unset live-data
                              	 reporting-interval

Required Minimum Privilege Level: Advanced

Use this command
                                    		  to reset the Live Data reporting interval to the default value (which is five
                                    		  minutes).

### Command
                                    			 Syntax

unset live-data reporting-interval

When you reset the
                                    		  Live Data reporting interval, restart the publisher and then the subscriber.
                                    		  Restart the inactive node and then the active node by using the utils system
                                       			 restart command. (For more information about the command, refer to the Administration Console User Guide for Cisco Unified Intelligence
                                       			 Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .)

If you restart
                                    		  only the publisher and not the subscriber, the reset interval takes effect only
                                    		  on the publisher; likewise, if you restart the subscriber but not the
                                    		  publisher, only the subscriber uses the reset reporting interval.

When the publisher
                                    		  and the subscriber restart, use the show live-data reporting-interval command
                                    		  to validate the new interval.

### Live Data Services Registration

#### set live-data cuic-datasource

Required Minimum Privilege Level: Advanced

Use this command
                                    		  to create or update the Live Data data source in Cisco Unified Intelligence Center.

You can run the command from either the Side A or Side B (not both) Live Data node;  and you must run it once for each of
                                    the Cisco Unified Intelligence Center Publisher nodes. The AW Distributor and Cisco Unified Intelligence Center Publisher
                                    must be in service.

You can use this command after you:

Set the AW DB connection information on the same node where you want to run this command.

Configure Live Data endpoints in the Machine Service table.

You must run this command when there is a change in machine service inventory table. The changes can occur when,

Recreating the node in Unified CCE Inventory

Restoring AW database using EDMT

Running the set livedata machine-services CLI command (for 4K and above)

### Command Syntax

set live-data cuic-datasource cuic-addr cuic-port cuic-user

##### Command Default

When you run this command, it prompts you to specify the password to use for authentication with Cisco Unified Intelligence
                                    Center.

#### show live-data cuic-datasource

Required Minimum Privilege Level: Ordinary

Use this command
                                    		  to list the Live Data  data source configuration in Cisco Unified Intelligence Center.

You can use this command after you:

Set the AW DB connection information on the same node where you want to run this command.

Configure Live Data endpoints in the Machine Service table.

### Command Syntax

show live-data cuic-datasource cuic-addr cuic-port cuic-user

##### Command Default

When you run this command, it prompts you to specify the password to use for authentication with Cisco Unified Intelligence
                                    Center.

#### unset live-data cuic-datasource

Required Minimum Privilege Level: Advanced

Use this command
                                    		  to delete the existing Live Data data source. Ensure that there are no existing reports or report templates that reference
                                    the Live Data data source before you run the command; otherwise, the command fails.

After you run this command successfully, you can no longer generate Live Data reports.

You can use this command after you:

Set the AW DB connection information on the same node where you want to run this command.

Configure Live Data endpoints in the Machine Service table.

### Command Syntax

unset live-data cuic-datasource cuic-addr cuic-port cuic-user

##### Command Default

When you run this command, it prompts you to specify the password to use for authentication with Cisco Unified Intelligence
                                    Center.

#### set live-data
                              	 machine-services

This command is not valid for coresident deployments. If you have a coresident deployment, use the System Inventory in the
                                                Unified CCE Administration tool.

Required Minimum Privilege Level: Advanced

Use this command
                                    		  to set or update the Machine Service table with the latest information from
                                    		  Live Data services (publisher and subscriber).

You must run the set live-data cuic-datasource CLI command after running the set live-data machine-services command.

### Command
                                    			 Syntax

set live-data machine-services awdb-user

##### Command Default

When you run this command, it prompts you to specify the login password to use for authentication with AW database access.

#### show live-data machine-services

Required Minimum Privilege Level: Ordinary

Use this command to display Live Data entries in the Machine Services table.

### Command Syntax

show live-data machine-services [awdb-user]

##### Command Default

When you run this command, it prompts you to specify the login password to use for authentication with AW database access.

#### set live-data network-buffer

Required Minimum Privilege Level: Advanced

Use this command to set the network buffer size for the Live Data VM.

During peak load on Live Data, the VMXNET3 adapter is reset due to which the Live Data service is disconnected from other
                                                components. To avoid this disconnection, use the set live-data network-buffer command to increase the buffer size for the Live Data VM. The recommended value for both receive (rx) and transmit (tx) buffers
                                                is 4096 bytes, which is also the maximum allowed value. For more information about handling high traffic bursts, refer to
                                                the VMware KB article at https://kb.vmware.com/s/article/2039495 .

### Command Syntax

set live-data network-buffer [options] [size]

OPTIONS:

[tx] sets the custom network-buffer tx size.

[rx] sets the custom network-buffer rx size.

SIZE:

[size] sets the buffer size in bytes.

#### show live-data network-buffer

Required Minimum Privilege Level: Ordinary

Use this command to view the network buffer size for the Live Data VM.

### Command Syntax

show live-data network-buffer [options]

OPTIONS:

[tx] shows the custom network-buffer tx size.

[rx] shows the custom network-buffer rx size.

#### unset live-data network-buffer

Required Minimum Privilege Level: Advanced

Use this command to reset to the default network buffer size for the Live Data VM.

### Command Syntax

unset live-data network-buffer [options]

OPTIONS:

[tx] resets the custom network-buffer tx size to the default value of 512 bytes.

[rx] resets the custom network-buffer rx size to the default value of 1024 bytes.

### Live Data CORS Configuration

Live Data CORS commands allow you to configure CORS and hence allow web applications running on different origins to communicate
                                 with Live Data.

Ensure that the CORS update commands are run on all the live data nodes in the cluster.

After you make changes to the CORS status, allowed origins, allowed headers, or exposed headers, restart the Cisco Web Proxy Service .

#### utils live-data cors status

##### Required Minimum Privilege Level: Ordinary

Use this command to query the Live Data CORS status.

### Command Syntax

utils live-data cors status

There are no required parameters.

#### utils live-data cors enable

##### Required Minimum Privilege Level: Advanced

Use this command to enable CORS in Live Data.

### Command Syntax

utils live-data cors enable

There are no required parameters.

For Unified Intelligence Centre gadgets (Live Data) to load in Cisco Finesse, ensure to:

Enable CORS using utils cuic cors enable and utils live-data cors enable commands.

Set the Finesse host URL in utils cuic cors allowed_origin add URLs and utils live-data cors allowed_origin add URLs commands.

Examples:

https://<finesse-FQDN>

https://<finesse-FQDN>:port

#### utils live-data cors disable

##### Required Minimum Privilege Level: Advanced

Use this command to disable CORS in Live Data.

### Command Syntax

utils live-data cors disable

There are no required parameters.

#### utils live-data cors allowed_origin list

##### Required Minimum Privilege Level: Ordinary

Use this command to display the list of allowed URLS that can make CORS request to Live Data.

### Command Syntax

utils live-data cors allowed_origin list

There are no required parameters.

#### utils live-data cors allowed_origin add

##### Required Minimum Privilege Level: Advanced

Use this command to add the given list of URLs to the allowed origin list.

### Command Syntax

utils live-data cors allowed_origin add URLs

URLs

Comma separated list of URLs (without spaces) that has to be added to the allowed origins list. The URL should be of the format: http[s]://<hostname>[:port]

#### utils live-data cors allowed_origin delete

##### Required Minimum Privilege Level: Advanced

Use this command to delete a particular URL entry or all the URL entries from the allowed origins list.

### Command Syntax

utils live-data cors allowed_origin delete

There are no required parameters. This command will prompt for a choice to delete a particular entry or all URL entries from
                                    allowed origins list.

##### Example

Utils live-data cors allowed_origin delete

1. https://cisco.com

2. https://google.com

a: all

q: quit

#### utils live-data cors allowed_headers list

##### Required Minimum Privilege Level: Ordinary

Use this command to display the list of allowed headers that the client can use to make CORS request to Live Data.

### Command Syntax

utils live-data cors allowed_headers list

There are no required parameters.

#### utils live-data cors allowed_headers add

##### Required Minimum Privilege Level: Advanced

Use this command to add the given list of headers to the allowed header list.

### Command Syntax

utils live-data cors allowed_headers add headers

headers

Comma separated list of headers (without spaces) that has to be added to the allowed headers list.

#### utils live-data cors allowed_headers delete

##### Required Minimum Privilege Level: Advanced

Use this command to delete a particular header entry or all the header entries from the allowed headers list. The header names
                                    are case-insensitive and any duplicate header name will be ignored.

### Command Syntax

utils live-data cors allowed_headers delete

There are no required parameters. This command will prompt for a choice to delete a particular entry or all the header entries
                                    from the allowed headers list.

##### Example

Utils live-data cors allowed_headers delete

1. Header1

2. Header2

a: all

q: quit

#### utils live-data cors exposed_headers list

##### Required Minimum Privilege Level: Oridnary

This command displays the list of exposed headers that the client can expect from Live Data when it makes CORS request to
                                    Live Data .

### Command Syntax

utils live-data cors exposed_headers list

There are no required parameters.

#### utils live-data cors exposed_headers add headers

##### Required Minimum Privilege Level: Oridnary

This command adds given list of headers to the exposed header list.

### Command Syntax

utils live-data cors exposed_headers add headers

headers

Comma separated list of headers that has to be added to the exposed headers list.

#### utils live-data cors exposed_headers delete

##### Required Minimum Privilege Level: Oridnary

This command deletes a particular header entry or all the header entries from the exposed headers list. The header names are
                                    case-insensitive, any duplicate header name will be ignored.

### Command Syntax

utils live-data cors exposed_headers delete

There are no required parameters. This command will prompt for a choice to delete a particular entry or all header entries
                                    from exposed headers list.

##### Example

Utils live-data cors exposed_headers delete.

Header1

Header2

a: all

q: quit

## Transport Layer Security CLI Commands

These CLI commands are only for VOS systems. They are not available for VMs running Windows Server.

### TLS Server Minimum Version

#### set tls server min-version

##### Command Syntax

Use this command to set the current TLS server minimum version for inbound connections. Supported TLS version values are 1.0,
                                    1.1, and 1.2.

set tls server min-version <version>

<version> in above command can be the supported TLS version 1.2, 1.1, or 1.0.

Warning will be displayed, if the administrator is trying to lower the currently configured TLS version.

Set the TLS server version on each node of the cluster seperately.

TLS server version will take effect only after restarting the system.

#### show tls server min-version

Use this command to display the current TLS server minimum version set for inbound connections.

### Command Syntax

show tls server min-version

### TLS Client Minimum Version

#### set tls client min-version

##### Command Syntax

Use this command to set the current TLS minimum version for outbound connections.

set tls client min-version 1.2

#### show tls client min-version

Use this command to display the current TLS minimum version for outbound connections.

### Command Syntax

show tls client min-version

## Cloud Connect CLI Command

### set cloudconnect subscriber

Required Minimum Privilege Level: Advanced

#### Command Default

Use this command to configure the cloud connect subscriber node in the cluster. The command verifies if the hostname is valid
                                 or not. Ensure to run this command only from publisher node.

### Command Syntax

set cloudconnect subscriber [ name ]

When you run this command, it configures the Cloud Connect subscriber node in the cluster.

### show cloudconnect subscriber

Required Minimum Privilege Level: Ordinary

#### Command Default

Use this command to display the Cloud Connect subscriber node details.

### Command Syntax

show cloudconnect subscriber

When you run this command, it displays the Cloud Connect subscriber node details.

### unset cloudconnect subscriber

Required Minimum Privilege Level: Advanced

#### Command Default

Use this command to remove the Cloud Connect subscriber node configuration from the cluster. Ensure to run this commend only
                                 from publisher node.

### Command Syntax

unset cloudconnect subscriber

When you run this command, it remove the Cloud Connect subscriber node configuration from the cluster.

### set cloudconnect digitalrouting config

Required Minimum Privilege Level: Advanced

Use this command to update the digitalrouting service configuration details.

### Command Syntax

set cloudconnect digitalrouting config

#### Command Default

When you run this command, the current digitalrouting service configuration details is fetched and is displayed. You are prompted
                                 to enter new configuration details. The current configuration details are displayed within [ ] . You can enter the new configuration details or retain the existing configuration. Depending on the config API response,
                                 either the success or the error response is displayed.

Example:

```
admin:set cloudconnect digitalrouting config
Fetching existing configuration...
Enter the Config details to be saved:
MR Server SSL Enabled [false]: true
The config details updated successfully.
```

### show cloudconnect digitalrouting config

#### Command Default

Required Minimum Privilege Level: Advanced

Use this command to display the digital routing configuration details.

### Command Syntax

show cloudconnect digitalrouting config

When you run this command, the DigitalRouting configuration details are displayed.

### show cloudconnect digitalrouting status

#### Command Default

Required Minimum Privilege Level: Advanced

Use this command to display status for cluster nodes and components in digitalrouting.

### Command Syntax

show cloudconnect digitalrouting status

When you run this command, the cluster nodes and the component status details are displayed.

### utils cloudconnect reinit services

Required Minimum Privilege Level: Advanced

#### Command Default

Use this command to reinitialize Cloud Connect services.

### Command Syntax

utils cloudconnect reinit services

This command stops all the Micro services(Containers) that are running on Cloud Connect, removes the services, and recreates
                                 them with new configuration.

The changes to the timezone take effect on the Cloud Connect services only after you run this command successfully.

### utils cloudconnect reset client-secret

Required Minimum Privilege Level: Advanced

#### Command Default

Use this command to reset your Cloud Connect client credentials via CLI.

### Command Syntax

utils cloudconnect reset client-secret

Administrators can reset their Cloud Connect client credentials by entering this command in the CLI. The possible responses
                                 to running this command are:

Successful Reset

```
Do you really want to reset client secret (yes/no)?: yes

Resetting client secret ....

Client Secret updated successfully.

admin:
```

Reset Aborted

```
Do you really want to reset client secret (yes/no)?: no

Client secret reset aborted !.

admin:
```

Reset failed due to API error

```
Do you really want to reset client secret (yes/no)?: yes

Resetting client secret ....

Unable to update client secret. Details: API Request failed. Response Code: 500
```

If you encounter this error, check the logs to resolve the issue.

### utils cloudconnect authlock status

Required Minimum Privilege Level: Advanced

### Command Syntax

utils cloudconnect authlock status <container name>

#### Command Default

After multiple failed attempts to enter credentials incorrectly, the IP address of a user or terminal will be locked.

To view the list of locked IP addresses in a specific container, use the status command.

Possible responses for running these commands include:

Response to Successful Status Command

```
admin: utils cloudconnect authlock status featureflagmgmt
[
 {
    "client_ip":"192.1.1.1",
    "status":"Active"
 }
]
admin:
```

Response when Status Command Fails

```
admin: utils cloudconnect authlock status featureflagmgmt

AuthLock show failed for featureflagmgmt with exception: Connection refused (Connection refused)

admin:
```

### utils cloudconnect authlock reset

Required Minimum Privilege Level: Advanced

### Command Syntax

utils cloudconnect authlock reset <container name> <IP address>

#### Command Default

After multiple failed attempts to enter credentials incorrectly, the IP address of a user or terminal will be locked.

To view the list of locked IP addresses in a specific container, use the status command in the previous section.

Once you've identified the relevant IP addresses and container name, run the reset command to unlock the IP addresses of users
                                 who have been locked out from each container. Upon successful execution of this command, the user or IP address will be immediately
                                 restored access.

Possible responses for running these commands include:

Response to a Successful Reset Command

```
admin: utils cloudconnect authlock reset featureflagmgmt 192.1.1.1

Auth lock reset is successful for featureflagmgmt

admin:
```

Response when Reset Command Fails

```
admin: utils cloudconnect authlock reset featureflagmgmt 192.1.1.1

AuthLock reset failed for featureflagmgmt with exception: Connection refused (Connection refused)

admin:
```

### utils cloudconnect reset client-secret

Required Minimum Privilege Level: Advanced

#### Command Default

Use this command to reset your Cloud Connect client credentials via CLI.

### Command Syntax

utils cloudconnect reset client-secret

Administrators can reset their Cloud Connect client credentials by entering this command in the CLI. The possible responses
                                 to running this command are:

Successful Reset

```
Do you really want to reset client secret (yes/no)?: yes

Resetting client secret ....

Client Secret updated successfully.

admin:
```

Reset Aborted

```
Do you really want to reset client secret (yes/no)?: no

Client secret reset aborted !.

admin:
```

Reset failed due to API error

```
Do you really want to reset client secret (yes/no)?: yes

Resetting client secret ....

Unable to update client secret. Details: API Request failed. Response Code: 500
```

If you encounter this error, check the logs to resolve the issue.

### utils cloudconnect reset client-secret

Required Minimum Privilege Level: Advanced

#### Command Default

Use this command to reset your Cloud Connect client credentials via CLI.

### Command Syntax

utils cloudconnect reset client-secret

Administrators can reset their Cloud Connect client credentials by entering this command in the CLI. The possible responses
                                 to running this command are:

Successful Reset

```
Do you really want to reset client secret (yes/no)?: yes

Resetting client secret ....

Client Secret updated successfully.

admin:
```

Reset Aborted

```
Do you really want to reset client secret (yes/no)?: no

Client secret reset aborted !.

admin:
```

Reset failed due to API error

```
Do you really want to reset client secret (yes/no)?: yes

Resetting client secret ....

Unable to update client secret. Details: API Request failed. Response Code: 500
```

If you encounter this error, check the logs to resolve the issue.

### utils cloudconnect authlock status

Required Minimum Privilege Level: Advanced

### Command Syntax

utils cloudconnect authlock status <container name>

#### Command Default

After multiple failed attempts to enter credentials incorrectly, the IP address of a user or terminal will be locked.

To view the list of locked IP addresses in a specific container, use the status command.

Possible responses for running these commands include:

Response to Successful Status Command

```
admin: utils cloudconnect authlock status featureflagmgmt
[
 {
    "client_ip":"192.1.1.1",
    "status":"Active"
 }
]
admin:
```

Response when Status Command Fails

```
admin: utils cloudconnect authlock status featureflagmgmt

AuthLock show failed for featureflagmgmt with exception: Connection refused (Connection refused)

admin:
```

### utils cloudconnect authlock reset

Required Minimum Privilege Level: Advanced

### Command Syntax

utils cloudconnect authlock reset <container name> <IP address>

#### Command Default

After multiple failed attempts to enter credentials incorrectly, the IP address of a user or terminal will be locked.

To view the list of locked IP addresses in a specific container, use the status command in the previous section.

Once you've identified the relevant IP addresses and container name, run the reset command to unlock the IP addresses of users
                                 who have been locked out from each container. Upon successful execution of this command, the user or IP address will be immediately
                                 restored access.

Possible responses for running these commands include:

Response to a Successful Reset Command

```
admin: utils cloudconnect authlock reset featureflagmgmt 192.1.1.1

Auth lock reset is successful for featureflagmgmt

admin:
```

Response when Reset Command Fails

```
admin: utils cloudconnect authlock reset featureflagmgmt 192.1.1.1

AuthLock reset failed for featureflagmgmt with exception: Connection refused (Connection refused)

admin:
```

### Commands to enable Beta Features

Starting from release 15.0(1), Contact Center Enterprise offers several Beta Features listed in the Beta Features section
                              of the Release Notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

Beta refers to the stage in the product lifecycle where select customers are invited to evaluate and provide feedback on features
                              that have not yet reached GA.

Beta features are not enabled by default and are "out of the box". To join Beta testing or enable these features, email the
                              Product Management team at cce-pm-team@cisco.com .

Administrators must ensure the following IP addresses are added to the Allow List to complete the configuration:

23.235.32.0/20, 43.249.72.0/22, 103.244.50.0/24, 103.245.222.0/23, 103.245.224.0/24, 104.156.80.0/20, 140.248.64.0/18, 140.248.128.0/17,
                                          146.75.0.0/17, 151.101.0.0/16, 157.52.64.0/18, 167.82.0.0/17, 167.82.128.0/20, 167.82.160.0/20, 167.82.224.0/20, 172.111.64.0/18,
                                          185.31.16.0/22, 199.27.72.0/21, and 199.232.0.0/16

For more details, see:

https://api.fastly.com/public-ip-list

https://our-ips.split.io/

https://help.split.io/hc/en-us/articles/360006954331-How-do-I-allow-Split-to-work-in-my-environment

#### set cloudconnect featureflagmgmt config

Required Minimum Privilege Level: Advanced

##### Command Default

### Command Syntax

set cloudconnect featureflagmgmt config <tenant> <SDK Key> <Environment>

Administrators can use this command to set up the following configurations:

Tenant : Unique tenant name (organization ID in Webex CCE deployments)

SDK Key

Environment

Contact your Cisco account team for the values of SDK Key and Environment .

The values can be retrieved using the APIs listed in the Internal Cloud Connect API Endpoints topic in the Other Security Considerations chapter of the Security Guide for Cisco Unified  Contact Center Enterprise, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html. .

An example when the command is successful is as follows:

```
set cloudconnect featureflagmgmt config
Fetching existing configuration...
Enter the FeatureFlag Config details to be saved:
FeatureFlag Tenant [orgA]:
FeatureFlag SDK Key [art57h5]:
FeatureFlag Environment [QA-ABC]:
The config details updated successfully.
```

#### set cloudconnect featureflagmgmt pollingInterval

Required Minimum Privilege Level: Advanced

##### Command Default

### Command Syntax

set cloudconnect featureflagmgmt <pollingInterval>

Administrators can use this command to set a valid polling interval at which Cloud Connect can poll for updates.

An example when the command is successful is as follows:

```
set cloudconnect featureflagmgmt pollingInterval
Fetching existing configuration...
Enter the FeatureFlag Polling Interval details to be saved:
FeatureFlag Polling Interval [10]:
The polling interval details updated successfully.
```

#### show cloudconnect featureflagmgmt config

Required Minimum Privilege Level: Advanced

##### Command Default

### Command Syntax

show cloudconnect featureflagmgmt config

This command displays all the configured values, including Tenant Name, SDK Key, Environment, and Polling Interval. You can
                                    use this to command to verify the values you configured using the above two CLI commands.

An example when the command is successful is as follows:

```
show cloudconnect featureflagmgmt config
Fetching existing configuration...
FeatureFlag Tenant: orgA
FeatureFlag SDK Key: art57h5
FeatureFlag Polling Interval: 10
FeatureFlag Environment: QA-ABC
FeatureFlag LastUpdatedTimestamp: 1745296111111
```

#### show cloudconnect featureflagmgmt status

Required Minimum Privilege Level: Advanced

##### Command Default

### Command Syntax

show cloudconnect featureflagmgmt status

Administrators can use this command to check the connection status of the service.

An example when the command shows an inactive connection status is as follows:

```
show cloudconnect featureflagmgmt status
{
  "status": "INACTIVE",
  "cluster": {
    "nodes": [
      {
        "address": "cconnect.hostname",
        "status": "MemberReachable",
        "statusSince": 1745296111111,
        "statusURL": "https://cconnect.hostname:8445/featureflagmgmt/v1/status"
      },
      {
        "address": "cconnect.hostname",
        "status": "MemberReachable",
        "statusSince": 1745296111111,
        "statusURL": "https://cconnect.hostname:8445/featureflagmgmt/v1/status"
      }
    ]
  },
  "peerSync": true
}
```

If the command shows that the service is not active, check the configuration and apply proxy settings if needed using the
                                                CCE Administration Console.

### CLI Commands for Cache Service

The following CLIs are available to view or modify configuration and logging for the cache service module:

#### View Current Configuration

show cloudconnect cache-service config

Command Default

Use this command to view the current configuration in the application.properties file and display all current key or value pairs:

Command Syntax

```
show cloudconnect cache-service config
```

When you run this command, it displays the cache service configurations.

#### View Current Log Level

show cloudconnect cache-service log

Command Default

Use this command to check the current log level configured in log4j.xml file:

Command Syntax

```
show cloudconnect cache-service log
```

When you run this command, it displays the current log level configured in log4j.xml file.

#### Modify Configuration Properties

set cloudconnect cache-service config

Command Default

Use this command to modify the configuration by updating a specific key/value pair in the application.properties file:

Command Syntax

```
set cloudconnect cache-service config [key] [value]
```

When you run this command, it displays the modified configuration for the specific key/value pair in the application.properties file.

#### Modify Log Level

set cloudconnect cache-service log

Command Default

Use this command to modify the current log level configured in log4j.xml file:

Command Syntax

```
set cloudconnect cache-service log [level]
```

When you run this command, it displays the modified log level configured in log4j.xml file.

#### Set RSA securitykeys

utils cloudconnect cache-service set securitykeys

Command Default

Use this command to create the RSA keys in current node:

Command Syntax

```
utils cloudconnect cache-service set securitykeys
```

When you run this command, it creates the RSA keys in current node.

#### Synchronize RSA securitykeys in Target Nodes

utils cloudconnect cache-service sync certificates

Command Default

Use this command to synchronize the RSA keys in target node:

Command Syntax

```
utils cloudconnect cache-service sync certificates
```

When you run this command, it synchronizes the RSA keys in the target node and then provide [Target IP Address]

#### Modify Configuration Properties (JWT)

Command Default

Use this command to modify the configuration by dynamically updating specific key/value pair in the application.properties file:

Command Syntax

```
set cloudconnect cache-service config [app.security.jwt.enabled] [true]
```

When you run this command, it displays the modified configuration for specific key/value pair, dynamically updated in the application.properties file.

#### Modify Configuration Properties for JWT Token Expiry Time

Command Default

Use this command to modify the configuration for JWT token expiry time by updating specific key/value pair in the application.properties file:

Command Syntax

```
set cloudconnect cache-service config [app.security.jwt.enabled] [time in milliseconds]
```

When you run this command, it displays the modified configuration for for JWT token expiry time by updating specific key/value
                                 pair, dynamically updated in the application.properties file.

Command Default

Use this curl command to get the JWT token issuance API for cache service:

Use the curl command through Postman for proper handling of requests and responses.

Command Syntax

```
curl --location 'https:// <FQDN> :8445/cache-service/api/auth/token' 

 --header 'Authorization: Basic <basic auth token> '
```

Only the basic auth credentials needs to be used (for examples, VOS admin credentials)

When you run this command, it displays the JWT role, username and token. Copy only the token and use it with 'bearer' keyword
                                 in request header for subsequent requests.

```
{
"role": "APP_USER",
"username": "Admin",
"token": " <basic auth token> "
}
```

Ensure that you restart the cache service module after modifying configuration file using the following commands:

Verify the configuration:

show cloudconnect cache-service config

Restart the service:

```
utils cloudconnect stop cache-service

utils cloudconnect start cache-service
```

## Cisco Identity Service OKTA IdP Configuration

### utils ids set_property IS_IdP_OKTA true

Required Minimum Privilege Level: Advanced

Use this command to set OKTA as the Identity Provider.

Command Syntax

utils ids set_property IS_IdP_OKTA true

OKTA is set as the Identity Provider.

### utils ids set_property IS_IdP_OKTA false

Required Minimum Privilege Level: Advanced

Use this command to unset OKTA as the Identity Provider.

Command Syntax

utils ids set_property IS_IdP_OKTA false

OKTA is removed as the Identity Provider.

### utils ids show_property IS_IdP_OKTA

Required Minimum Privilege Level: Ordinary

Use this command to show whether OKTA is set as the Identity Provider.

Command Syntax

utils ids show_property IS_IdP_OKTA

Displays one of the following:

The value of property 'IS_IdP_OKTA' is 'true'.

The value of property 'IS_IdP_OKTA' is 'false'.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Note | You must run this command when there is a change in machine service inventory table. The changes can occur when, Recreating the node in Unified CCE Inventory Restoring AW database using EDMT Running the set livedata machine-services CLI command (for 4K and above) |
|---|---|

| Note | This command is not valid for coresident deployments. If you have a coresident deployment, use the System Inventory in the
                                                Unified CCE Administration tool. |
|---|---|

| Note | You must run the set live-data cuic-datasource CLI command after running the set live-data machine-services command. |
|---|---|

| Note | During peak load on Live Data, the VMXNET3 adapter is reset due to which the Live Data service is disconnected from other
                                                components. To avoid this disconnection, use the set live-data network-buffer command to increase the buffer size for the Live Data VM. The recommended value for both receive (rx) and transmit (tx) buffers
                                                is 4096 bytes, which is also the maximum allowed value. For more information about handling high traffic bursts, refer to
                                                the VMware KB article at https://kb.vmware.com/s/article/2039495 . |
|---|---|

| Note | Ensure that the CORS update commands are run on all the live data nodes in the cluster. After you make changes to the CORS status, allowed origins, allowed headers, or exposed headers, restart the Cisco Web Proxy Service . |
|---|---|

| Note | For Unified Intelligence Centre gadgets (Live Data) to load in Cisco Finesse, ensure to: Enable CORS using utils cuic cors enable and utils live-data cors enable commands. Set the Finesse host URL in utils cuic cors allowed_origin add URLs and utils live-data cors allowed_origin add URLs commands. Examples: https://<finesse-FQDN> https://<finesse-FQDN>:port |
|---|---|

| Note | These CLI commands are only for VOS systems. They are not available for VMs running Windows Server. |
|---|---|

| Note | <version> in above command can be the supported TLS version 1.2, 1.1, or 1.0. Warning will be displayed, if the administrator is trying to lower the currently configured TLS version. Set the TLS server version on each node of the cluster seperately. TLS server version will take effect only after restarting the system. |
|---|---|

| Note | The changes to the timezone take effect on the Cloud Connect services only after you run this command successfully. |
|---|---|

| Note | If you encounter this error, check the logs to resolve the issue. |
|---|---|

| Note | If you encounter this error, check the logs to resolve the issue. |
|---|---|

| Note | If you encounter this error, check the logs to resolve the issue. |
|---|---|

| Note | Administrators must ensure the following IP addresses are added to the Allow List to complete the configuration: 23.235.32.0/20, 43.249.72.0/22, 103.244.50.0/24, 103.245.222.0/23, 103.245.224.0/24, 104.156.80.0/20, 140.248.64.0/18, 140.248.128.0/17,
                                          146.75.0.0/17, 151.101.0.0/16, 157.52.64.0/18, 167.82.0.0/17, 167.82.128.0/20, 167.82.160.0/20, 167.82.224.0/20, 172.111.64.0/18,
                                          185.31.16.0/22, 199.27.72.0/21, and 199.232.0.0/16 For more details, see: https://api.fastly.com/public-ip-list https://our-ips.split.io/ https://help.split.io/hc/en-us/articles/360006954331-How-do-I-allow-Split-to-work-in-my-environment |
|---|---|

| Note | Contact your Cisco account team for the values of SDK Key and Environment . |
|---|---|

| Note | If the command shows that the service is not active, check the configuration and apply proxy settings if needed using the
                                                CCE Administration Console. |
|---|---|

| Note | Use the curl command through Postman for proper handling of requests and responses. |
|---|---|

| Note | Only the basic auth credentials needs to be used (for examples, VOS admin credentials) |
|---|---|

| Note | Ensure that you restart the cache service module after modifying configuration file using the following commands: Verify the configuration: show cloudconnect cache-service config Restart the service: utils cloudconnect stop cache-service

utils cloudconnect start cache-service |
|---|---|