---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1262-maint-0cbffeed33
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1262/maintain_and_operate/guide/cuic_b_1262-admin-console-user-guide/cuic_m_1261-command-line-interface.html
retrieved_at: 2026-08-21T04:40:35.389590+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

Updated: April 28, 2023

Chapter: Command Line
	 Interface

## Chapter: Command Line
	 Interface

# Command Line
                     	 Interface

The Command Line
                        		Interface (CLI) provides a set of commands applicable to the operating system,
                        		to the Unified Intelligence Center database ( cuic_data ) and to the
                        		system database ( ccm_<version> ).

These commands allow
                        		basic maintenance and failure recovery and also enable some system
                        		administration when the Unified Intelligence Center operations console is
                        		unavailable.

You can access the CLI
                        		directly, using the monitor and keyboard at the server console:

Enter the ID for
                              			 the System Administration user (the one created during install).

When prompted,
                              			 enter the password for the System Administration user.

In addition to the CLI
                        		commands listed in this chapter, you can also enter:

help - to display the
                              			 list of all supported commands. For example, to display help for a specific
                              			 command, type help
                                 				delete dns and press Enter.

quit - to close the CLI.

In the command syntax
                        		descriptions:

bold is used for the base
                        		command.

italics are used for
                        		mandatory parameters, when the syntax includes them.

[ ] brackets are used
                        		for options, when the syntax includes them.

## Unset Command

### unset cuic properties

Use this command to remove the translation of host-to-ip setting.

### Command Syntax

unset cuic properties host-to-ip hostname

### unset ipsec

Use these commands to disable ipsec policies.

### Command Syntax

unset ipsec policy_group [ group | all ]

### Command Syntax

unset ipsec policy_name [policy_group] [policy_name]

### unset network dns

### Command Syntax

unset network dns options [options]

OPTIONS:

[timeout] sets the wait time before the system considers a DNS query
                              		failed to the default.

[attempts] sets the number of DNS attempts to make before failing to the
                              		default.

[rotate] sets the method for selecting a nameserver to the default. This
                              		affects how loads are distributed across nameservers.

### Command Syntax

unset ipv6 [policy_group] [policy_name]

### unset_host-to-ip

Use this command to
                              		remove any host-to-ip configurations that were defined with the command set cuic properties .

Running this command
                              		removes the node-specific override for the IP address of the Unified CCE
                              		databases and reverts to the default for the Unified CCE databases as
                              		configured in the Data Sources page.

### Command
                                 			 Syntax

unset_host-to-ip

## Utils Command

### utils auditd

These commands display enable, disable, and show the status of the
                              		audit daemon.

When enabled, auditd log files for the system are retrievable through
                              		RTMT. The auditd system monitors for specific security sensitive system calls
                              		at the OS kernel level and provides a record-keeping trail for such activities
                              		as file permission changes, failures to manipulate files due to permission
                              		settings, and changes to the system time and name.

### Command Syntax

utils auditd disable

utils auditd enable

utils auditd status

### utils core

These commands display information for core files.

### Command Syntax

utils core analyze core_file_name

PARAMETER core_file_name .

### Command Syntax

utils core list

### utils create report

These commands create a system report. If you specify hardware, the
                              		report contains disk array, remote console, diagnostic, and environmental data.

If you specify platform, the system collects the platform configuration
                              		files and copies them to a common log location.

As these reports take time to complete, the system prompts for a
                              		confirmation.

### Command Syntax

utils create report hardware

utils create report platform

### utils cuic

#### utils cuic
                              	 cpudiagnostics

This command is to monitor cuic tomcat process continuously and report
                                 		the CPU usage per thread. It uses a combination of top and jstack commands to
                                 		find out CPU usage at thread level and merge the results into the standard
                                 		jstack output.

### Command Syntax

utils cuic cpudiagnostics enable <max_cpu>

This command is to enable cpu diagnostic process.

PARAMETERS:

Max CPU usage at which to log thread details, max_cpu should be between
                                 		50 to 90. Default value is "50"

### Command Syntax

utils cuic cpudiagnostics disable

This command line is to disable the cpudiagnostics process.

#### utils cuic
                              	 mbeans

### Command Syntax

utils cuic mbeans [_c] [_e] [_i <val>] [_l <val>] [_n] [_o
                                       				  <val>] [_p <val>] [_u <val>] [_v <val>] [_x
                                       				  <val>]

PARAMETERS:

_e,__exitonfailure With this flag, terminal exits for any Exception

_i,__input <val> Input script file. There can only be one input
                                 		file. Default value is "stdin"

_l,__url <val> Location of MBean service. It can be
                                 		<host>:<port> or full service URL.

_n,__noninteract Non interactive mode. Use this mode if input doesn't
                                 		come from human or jmxterm is embedded

_o,__output <val> Comma separated output list, file and/or
                                 		stdout. Default value is "stdout".

_p,__password <val> Password for user/password authentication

_u,__user <val> User name for user/password authentication

_v,__verbose <val> Verbose level, could be silent|brief|verbose.
                                 		Default value is "brief".

_x,__execute <val> Executes a command (a connection must be
                                 		opened first with _l)

#### utils cuic
                              	 nmon

### Command Syntax

utils cuic nmon start s [seconds] c [count]

PARAMETERS:

s specifies the time interval (in seconds) between each
                                 		collection.

c specifies the number of collections that you want to
                                 		invoke. Each collection takes up about one Kilobyte of disk space.

### Command Syntax

utils cuic nmon stop

#### utils cuic purge

This command runs a manual purge of the
                                 cuic database tables. You might do this if you receive an alert that the
                                 database is nearing capacity and you do not want to wait for the daily
                                 automatic purge.

The tables purged
                                 are:

CuicDataSetInfo

CuicDataSet

CuicReportDefinitionFilter

CuicReportDefinitionFilterField

CuicReportDefinitionFilterParameter

CuicCollection

CuicCollectionValue

This command prompts for the password of the administration user. When
                                 the password is confirmed, the purge runs
                                 immediately.

#### utils cuic restorepub

This command restores security files like keypassfile and
                                 cuickeystore files from
                                 subscriber to publisher in the same cluster.

### Command Syntax

utils cuic restorepub

PARAMETERS:

No optional parameters.

#### utils cuic cors

Important

After you make changes to the CORS status, allowed origins list, exposed header, or allowed header, restart Cisco Intelligence
                                             Center Reporting Service for the changes to take effect. All CLIs are node-specific and must be run on all nodes in the cluster.

### Command Syntax

utils cuic cors enable

This command enables Cross Origin Resource Sharing (CORS) support in Unified Intelligence Center.

For Unified Intelligence Centre gadgets (Live Data and Historical) to load in Cisco Finesse, ensure to:

Enable CORS using the utils cuic cors enable command.

Set the Finesse host URL in the utils cuic cors allowed_origin add URLs command.

Examples:

https://<finesse-FQDN>

https://<finesse-FQDN>:port

### Command Syntax

utils cuic cors disable

This command disables CORS support in Unified Intelligence Center.

### Command Syntax

utils cuic cors status

This command displays the current CORS status in Unified Intelligence Center.

### Command Syntax

utils cuic cors allowed_origin list

This command displays the list of allowed URLs that can make CORS requests to Unified Intelligence Center.

### Command Syntax

utils cuic cors allowed_origin add <URL1,URL2,URL3>

Parameter: Comma-separated list of URLs (without spaces) that has to be added to the allowed origins list.

The URL format: http[s]://<hostname>[:port]

This command adds the given set of comma-separated URLs to the allowed origins list.

### Command Syntax

utils cuic cors allowed_origin delete

This command prompts for a choice to delete a particular allowed origin URL or all the allowed origin URLs.

1. http://google.com

2. http://www.cisco.com

a: all

q: quit

Select the index of origin to be deleted [1-2 or a,q]

### Command Syntax

utils cuic cors allowed_headers list

This command lists all the configured allowed headers for CORS. This list is used to validate incoming requests to CUIC.

### Command Syntax

utils cuic cors allowed_headers add <header1,header2,header3>

Parameter : Comma-separated list of headers (without spaces) that have to be added to the allowed headers list.

This command adds one or multiple allowed headers for CORS. You can add multiple headers using a comma-separated string.

### Command Syntax

utils cuic cors allowed_headers delete

This command prompts for a choice to delete a particular custom allowed header or all the custom allowed headers.

1: header1

2: header2

a: all

q: quit

Select the index of allowed header to be deleted [1-2 or a, q]: 1

### Command Syntax

utils cuic cors exposed_headers list

This command lists the response headers available for a client.

### Command Syntax

utils cuic cors exposed_headers add <header1,header2,header3>

Parameter: Comma-separated list of headers (without spaces) that have to be added to the exposed headers list.

This command adds one or multiple exposed headers for CORS. You can add multiple headers using a comma-separated string.

### Command Syntax

utils cuic cors exposed_headers delete

This command prompts for a choice to delete a particular custom exposed header or all the custom exposed headers.

1: header1

2: header2

a: all

q: quit

Select the index of exposed header to be deleted [1-2 or a, q]: 1

### Command Syntax

utils cuic cors private-network-access status

This command displays the status of the private network access for CORS in Cisco Unified Intelligence Center. If the status
                                    is True, you have private network access.

### Command Syntax

utils cuic cors private-network-access enable

This command enables the private network access for CORS in Cisco Unified Intelligence Center. To enable private network access,
                                    run the command on all nodes of CUIC and restart the Intelligence Center Reporting Service.

### Command syntax

utils cuic cors private-network-access disable

This command disables the private network access for CORS in Cisco Unified Intelligence Center. To disable private network
                                    access, run the command on all nodes of CUIC and restart the Intelligence Center Reporting Service.

#### utils cuic session

##### utils cuic session list

This command lists the current Cisco Unified Intelligence Center sessions.

### Command Syntax

utils cuic session list

Options

No parameters

Example

```
admin:utils cuic session list
Command run successfully
Session ID details saved to file.
To view file, type "file view activelog cuic-session.out"
To SFTP file, type "file get activelog cuic-session.out"
```

##### utils cuic session delete

This command deletes the Cisco Unified Intelligence Center sessions based on the username that you pass to this command.

### Command Syntax

utils cuic session delete <username 1,username 2>

Parameter

Usernames are names of the currently logged in users of the current Cisco Unified Intelligence Center sessions.

To get the current usernames , you must first run the utils cuic session list command and then run file view activelog cuic-session.out command.

Example

```
admin:utils cuic session delete CUIC\administrator Session Deleted successfully
```

### utils cuic cluster show

This command shows the current cluster mode enabled on this node and the other member details.

### Command Syntax

utils cuic cluster show

### utils cuic cluster
                           	 mode

This command is used
                              		to switch the CUIC cluster join configuration from Multicast to TCP/IP and vice
                              		versa.

After changing the cluster mode in all the nodes, restart “Intelligence Center Reporting Service ” in all the nodes starting
                                          from the publisher sequentially.

### Command
                              		  Syntax

utils cuic cluster mode

### utils cuic cluster refresh

This command refreshes the cluster node information only when run in the TCP/IP mode and must be run when there is an addition
                              or deletion of nodes to the CUIC cluster.

### Command Syntax

utils cuic cluster refresh

### utils cuic logging

The utils cuic logging commands update or display the configuration only on the nodes on which the commands are run. To change the logging configuration
                              on each node in the cluster, you must run the command separately on each node.

#### utils cuic logging config set

This command sets the value for log file configuration.

### Command Syntax

utils cuic logging config set [config-name] [config-value]

Options

[config-name] - mandatory log file configuration name

Valid configuration names are max-file-size , max-file-count , syslog-primary-host and syslog-secondary-host . The maximum limit of max-file-size and max-file-count is 50 MB and 50 respectively.

Only one [config-name] option can be set at a time.

[config-value] - mandatory log file configuration value.  For syslog-primary-host and syslog-secondary-host configuration names, the configuration values are the primary syslog server hostname and the secondary syslog server hostname,
                                       respectively.

#### utils cuic logging config show

This command prints the current log configuration for the given configuration name.

### Command Syntax

utils cuic logging config show [config-name]

Options

[config-name] - mandatory log file configuration
                                 name

Valid configuration names are max-file-size , max-file-count , syslog-primary-host and syslog-secondary-host .

Only one [config-name] option can be printed at a time.

#### utils cuic logging config clear

This command clears the log file configuration for the primary and secondary syslog servers.

### Command Syntax

utils cuic logging config clear [config-name]

Options

[config-name] - mandatory log file configuration name

Valid configuration names are syslog-primary-host and syslog-secondary-host .

Only one [config-name] option can be cleared at a time.

#### utils cuic logging list

This command lists the module and the logging level for the specified module. If a module name is
                                 specified, the logging level is displayed only for that module.

### Command Syntax

utils cuic logging list [module-name]

Options

[module-name] - optional

Possible module names for which, the log levels can be printed are as follows:

REPORT, REPORTENGINE, REPORTDEFINITION, SCHEDULER, DASHBOARD, AUTHORIZATION,
                                    AUTHENTICATION, VALUELISTCOLLECTION, SECURITY, CUICUI, DATASOURCE,
                                    CUICCONFIG

#### utils cuic logging reset

This command resets any modifications done to the logging configuration to the default value. For
                                 all the modules, the default value is Info .

### Command Syntax

utils cuic logging reset

Options

No parameters

#### utils cuic logging update

This command updates the log level for the given module name.

### Command Syntax

utils cuic logging update [module-name] [log-level]

Options

[module-name] - mandatory

Possible module names are as follows:

REPORT, REPORTENGINE, REPORTDEFINITION, SCHEDULER, DASHBOARD,
                                          AUTHORIZATION, AUTHENTICATION, VALUELISTCOLLECTION, SECURITY, CUICUI,
                                          DATASOURCE, CUICCONFIG

[log-level] - mandatory

New log level for the module. Valid log-level values are as follows:

ERROR, WARN, INFO, DEBUG

### utils cuic user
                           	 make-admin

This command
                              		provides all the roles to the new user and copies all the permission from the
                              		administrator to the user.

### Command
                              		  Syntax

utils cuic user make-admin

PARAMETERS:

domain\username

domain\username
                              		should be the complete username, including the prefix, as listed in CUIC User
                              		List page.

### utils oamp show logging-level

This command prints the current log configuration for the OAMP module name.

### Command Syntax

utils oamp show logging-level [module-name]

Options

[module-name] - mandatory

Following are the possible module names:

```
USERS_CONFIG, DEVICES_CONFIG, SERVER_CONFIG, CLUSTER_CONFIG, TOOLS_CONFIG, GENERIC
```

### utils oamp update logging-level

This command modifies the logging-level of the OAMP module.

### Command Syntax

utils oamp update logging-level [module-name] [log-level]

Options

[module-name] - mandatory

Following are the possible module names:

```
USERS_CONFIG, DEVICES_CONFIG, SERVER_CONFIG, CLUSTER_CONFIG, TOOLS_CONFIG, GENERIC
```

[log-level] - mandatory

Following are the valid log-level values:

```
ERROR, WARN, INFO, DEBUG
```

### utils dbreplication

#### utils dbreplication clusterreset

This command is used to reset replication on an entire cluster.

Caution

Before executing this command, run the command utils dbreplication stop on all Member nodes and then on the publisher (the Controller node).

### Command Syntax

utils dbreplication
                                       				  clusterreset

#### utils dbreplication dropadmindb

This command is used to drop the Informix syscdr database on any server
                                 		in the cluster.

Caution

### Command Syntax

utils dbreplication dropadmindb

#### utils dbreplication rebuild

This command is used to set up database replication across the cluster. This command can only be run from the publisher. This
                                 command will run the following commands on the specified nodes:

utils dbreplication stop

utils dbreplication dropadmindb or dropadmindbforce

utils dbreplication reset

### Command Syntax

utils dbreplication rebuild { [nodename] | | all }

#### utils dbreplication repair

This command repairs mismatched data on a named node or between nodes.
                                 		It does not repair replication setup.

### Command Syntax

utils dbreplication repair nodename

utils dbreplication repair all

#### utils dbreplication reset

This command is used to reset replication.

Caution

Before running this command, you must run utils dbreplication stop . If resetting all, stop replication on all nodes first. If resetting <nodename>, stop replication on that node first.

### Command Syntax

utils dbreplication reset all

utils dbreplication reset
                                       				  nodename

#### utils dbreplication runtimestate

This command is used to monitor progress of the database replication
                                 		process and provides replication state in the cluster.

### Command Syntax

utils dbreplication runtimestate nodename

OPTION: [nodename} limits the status to that of the node indicated.

#### utils dbreplication setrepltimeout

Use this command to increase the default timeout for replication setup
                                 		on large clusters.

The default timeout is 5 minutes, thus all subscribers requesting
                                 		replication within 5 minutes will be on the broadcast list and will be
                                 		replicated.

### Command Syntax

utils dbreplication setrepltimeout nteger value of new timeout in seconds

PARAMETER: integer value of new timeout in seconds must be between 300 and
                                 		3600 seconds.

#### utils dbreplication status

Use this command to view status of database replication after setup is
                                 		complete. To monitor status during setup, use RTMT.

### Command Syntax

utils dbreplication status

#### utils dbreplication stop

This command is used to stop the automatic setup of database replication
                                 		and to stop the ongoing setup of replication.

Run this command on each node where replication needs to be stopped.

Run on all Member nodes first and then on the publisher (the Controller
                                 		node).

Run this command with no parameters to run the stop operation on the local node only.

On the publisher, run this command as stop all or stop nodename to run the stop operation on all nodes or on a named node.

### Command Syntax

utils dbreplication stop all

utils dbreplication stop
                                       				  nodename

### utils diagnose

Use these commands for various diagnostic functions.

### Command Syntax

utils diagnose fix

### Command Syntax

utils diagnose list

### Command Syntax

utils diagnose module module name

### Command Syntax

utils diagnose test

### Command Syntax

utils diagnose version

### utils disaster_recovery

#### utils disaster_recovery backup

This command invokes a backup and makes the tar file on the network drive or
                                 		the tape.

### Command Syntax

utils disaster_recovery backup
                                       				  network <featurelist> <path> <servername> <userid >

PARAMETERS:

featurelist indicates the comma-separated feature list to back
                                 		up. Use the command utils disaster_recovery show_registration to display the list of registered features.

path indicates the path to save back up files.

servername is the server ip/hostname where the backup file is to
                                 		be stored.

userid is the user id used to connect to the remote machine.

utils disaster_recovery backup tape <featurelist> <tapeid>

PARAMETERS:

featurelist indicates a comma-separated feature list to back up.

tapeid indicates the tape ID to back up the files. Use the
                                 		command utils disaster_recovery show_tapeid to display the list of tape IDs.

#### utils disaster_recovery cancel_backup

This command cancels an ongoing backup.

### Command Syntax

utils disaster_recovery cancel_backup confirm

confirm is mandatory and prompts you to enter Yes/Y to continue or any other key to stop.

#### utils
                              	 disaster_recovery device

### Command Syntax

utils disaster_recovery device add
                                       				  network devicename path server_namei/ip_address username
                                       				  [Number_of_backups]

This command adds the backup network device.

PARAMETERS :

devicename : Specifies the name of the backup device to be
                                 		added (mandatory).

path : Specifies the path to retrieve the backup device (mandatory).

server_namei/ip_address : Specifies the hostname or IP
                                 		address of the server where the backup file is stored (mandatory).

username : Specifies the userid required to connect to the
                                 		remote location.

Number_of_backups : Specifies the number of backups to
                                 		store on the Network Directory (default 2). This parameter is optional.

### Command Syntax

utils disaster_recovery device delete device_name \*

This command deletes the specified device.

PARAMETERS :

device_name : Name of the device to be deleted .

* : Deletes all existing devices except for the ones associated to a
                                 		schedule

### Command Syntax

utils disaster_recovery device
                                       				  list

Displays the device name, device type, and device path for all the
                                 		backup devices.

#### utils
                              	 disaster_recovery estimate_tar_size

### Command
                                    			 Syntax

utils disaster_recovery estimate_tar_size featurelist

PARAMETERS:

featurelist indicates the comma separated feature list to backup. Use utils disaster_recovery show_registration <servername> to display the list of registered
                                 		features.

#### utils
                              	 disaster_recovery history

This command displays the history of previous backups and restores.

### Command Syntax

utils disaster_recovery history [operation]

operation specifies backup and restore.

#### utils
                              	 disaster_recovery jschLogs

### Command Syntax

utils disaster_recovery jschLogs operation

PARAMETERS:

operation name of operation like Enable\Disable.

#### utils
                              	 disaster_recovery prepare

This command prepares for backup and restore from publisher and
                                 		subscriber.

### Command Syntax

utils disaster_recovery prepare
                                       				  restore

### Command Syntax

utils disaster_recovery prepare restore
                                       				  pub_from_sub

#### utils disaster_recovery restore

These commands invoke a restore.

### Command Syntax

utils disaster_recovery restore
                                       				  network <restore_server> <tarfilename> <path> <servername> <userid>

PARAMETERS:

restore_server is the hostname of the server to be restored.

tarfilename is the tar file name to be restored.

path is the mandatory path that retrieves the backup tar file from this
                                 		location.

servername is the server ip\hostname from which to retrieve
                                 		backup tar file.

userid is the user id used to connect to the  remote machine.

### Command Syntax

utils disaster_recovery restore tape <server><tarfilename>
                                       				  <tapeid>

PARAMETERS

server is the hostname of the server to be restored.

tarfilename is the tar file name to be restored.

tapeid is the tape ID used to restore files from the tape device. Use the
                                 		command utils disaster_recovery show_tapeid to display the list of tape
                                 		IDs.

#### utils disaster_recovery show_backupfiles

These commands retrieve information about backup files.

### Command Syntax

utils disaster_recovery show_backupfiles
                                       				  network <path> <servername> <userid>

PARAMETERS:

path indicates the location of the backup file.

servername is the server ip/hostname where the backup file has
                                 		been stored.

userid is the user id used to connect to the remote machine.

### Command Syntax

utils disaster_recovery show_backupfiles
                                       				  tape tapeid

PARAMETER: tapeid is the ID of the tape device.

#### utils disaster_recovery show_registration

This command shows all the registered features and components on a given
                                 		server.

### Command Syntax

utils disaster_recovery
                                       				  show_registration

#### utils disaster_recovery show_tapeid

This command shows the list of tape IDs.

### Command Syntax

utils disaster_recovery
                                       				  show_tapeid

#### utils disaster_recovery status

This command shows the status of the ongoing backup or restore operation.

### Command Syntax

utils disaster_recovery status operation

PARAMETER operation is the name of the operation: backup or restore.

### utils firewall

These commands perform various actions pertaining to the firewall.

### Command Syntax

utils firewall disable [time]

utils firewall enable

utils firewall list

utils firewall status

OPTION: [time} is the duration in seconds for which the firewall is to
                              		be disabled.

#### utils firewall
                              	 ipv4

These commands perform various actions pertaining to the firewall ipv4.

### Command Syntax

utils firewall debug [off \\ time]

PARAMETERS:

This command turns IPv4 firewall debugging on or off. If you do not
                                 		enter a time parameter, this command turns on debugging for 5 minutes.

off Turns off the IPv4 firewall debugging. If you do not
                                 		enter the time parameter, this command disables the firewall for 5 minutes.

- Minutes: 0-1440m

- Hours: 0-23h

- Hours and minutes: 0-23h
                                       		  0-60m

### Command Syntax

utils firewall disable [time]

disable Turns off the IPv4 firewall. If you do not enter
                                 		the time parameter, this command disables the firewall for 5 minutes.

### Command Syntax

utils firewall enable [time]

enable Turns on the IPv4 firewall.

### Command Syntax

utils firewall list

This commands displays the current configuration of the IPv4 firewall.

### Command Syntax

utils firewall status

This command displays the current status of the IPv4 firewall.

#### utils firewall
                              	 ipv6

These commands perform various actions pertaining to the firewall ipv6.

### Command Syntax

utils firewall debug [off \\ time]

PARAMETERS:

This command turns IPv6 firewall debugging on or off. If you do not
                                 		enter a time parameter, this command turns on debugging for 5 minutes.

off Turns off the IPv6 firewall debugging. If you do not
                                 		enter the time parameter, this command disables the firewall for 5 minutes.

- Minutes: 0-1440m

- Hours: 0-23h

- Hours and minutes: 0-23h
                                       		  0-60m

### Command Syntax

utils firewall disable [time]

disable Turns off the IPv6 firewall. If you do not enter
                                 		the time parameter, this command disables the firewall for 5 minutes.

### Command Syntax

utils firewall enable [time]

enable Turns on the IPv6 firewall.

### Command Syntax

utils firewall list

This commands displays the current configuration of the IPv6 firewall.

### Command Syntax

utils firewall status

This command displays the current status of the IPv6 firewall.

### utils import
                           	 config

This command takes
                              		data from the platformConfig.xml file on the virtual floppy drive and modifies
                              		the system to match the configuration file. The system will reboot after the
                              		command successfully completes.

### Command
                                 			 Syntax

utils import config

PARAMETERS: None

REQUIREMENTS:

Command privilege
                              		level: 1

Allowed during
                              		upgrade: Yes

USAGE GUIDELINES

To run this command on a VMware deployment that has been cloned (copied) from a template:

Power on the VM.

Use the Answer File Generator (AFG) tool. For more information, see https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html .

Insert the Config.xml file into a virtual floppy instance. For more information, see https://kb.vmware.com/s/article/1739 .

Mount the .flp
                                    			 file in the floppy drive of the new VM.

Log in to the CLI of the VM (using console or SSH) and run the utils importconfig command. The command cycles through all
                                    of the data found in the xml file and if data is found that is different than what is currently set on the VM, it modifies
                                    the VM to match the new data.

The system reboots
                                    			 with the new identity.

### utils iostat

This command provides the iostat output for the given number of
                              		iterations and interval.

### Command Syntax

utils iostat [options]

OPTIONS:

[interval] indicates the interval in seconds. Mandatory if iterations is
                              		also used.

[iterations] indicates the number of iostat iterations to be performed.
                              		Mandatory if interval is also used.

[filename] redirects the output to a file.

### utils iothrottle

These commands enable, disable, or show status of I/O throttling
                              		enhancements.

### Command Syntax

utils iothrottle disable

utils iothrottle enable

utils iothrottle status

### utils
                           	 netdump

This command enables, disable and displays status of the netdump.

### Command Syntax

utils netdump enable

### Command Syntax

utils netdump disable

### Command Syntax

utils netdump status

#### utils netdump client

These commands configure the netdump client.

### Command Syntax

utils netdump start ip-address-of-netdump-server

PARAMETER ip-address-of-netdump-server specifies the IP address of the netdump server to which the client
                                 		will send diagnostic information.

### Command Syntax

utils netdump status

### Command Syntax

utils netdump status

### utils network

#### utils network arp

This command lists, sets, or deletes Address Resolution Protocol (ARP)
                                 		table entries.

### Command Syntax

utils network arp delete host

host represents the host name or IP address of the host to delete
                                 		from the table.

### Command Syntax

utils network arp list [options]

OPTIONS:

[host host] is the host and host name to list.

[page] displays the output one page at a time.

[numeric] displays hosts as dotted IP addresses.

### Command Syntax

utils network arp set <host> <address>

<host> is the name or dotted IP address of the host to add
                                 		to the table.

<address> is the hardware address (MAC) of the host to be
                                 		added.

#### utils network capture

This command captures IP packets on the ethernet interface.

### Command Syntax

utils network capture [options]

OPTIONS:

[page] pauses output.

[numeric] show hosts as dotted IP addresses.

[file fname] outputs the information to a file saved in
                                 		platform/cli/fname.cap.

[count num] indicates a count of the number of packets to capture.

[size bytes] indicates a count of the number of packets to capture.
                                 		Note: The maximum count for the screen is 1000; for a file it is 100000.

[src addr] indicates the source address of the packet as a host name or
                                 		IPV4 address.

[dest addr] indicate the destination address of the packet as a host
                                 		name or IPV4 address.

[port num] indicates the port number of the packet (either src or dest).

[host protocol] indicates the host address of the packet as a host name
                                 		or IPV4 address. This option will display all packets to and from that address.
                                 		Note: If "host" is provided, do not provide "src" or "dest".

#### utils network connectivity

This command is valid only on a subscriber (Member) node. It tests the
                                 		network connectivity from this system to the publisher node (the Controller
                                 		node).

### Command Syntax

utils network connectivity

#### utils network host

This command resolves a hostname to an address, or an address to a
                                 		hostname. This command looks for the host locally first. If it cannot resolve
                                 		it locally, and DNS is configured, then it does a DNS lookup.

### Command Syntax

utils network host name

PARAMETER name is the name of the host or address to resolve.

#### utils network ping

This command sends one or more ping packets to a remote destination.

### Command Syntax

utils network ping dest [count]

PARAMETER dest is the dotted IP or host name of the destination.

OPTION [count] is the optional count value (default is 4).

#### utils network tracert

This command traces IP packets to a remote destination.

### Command Syntax

utils network tracert dest

PARAMETER dest is the dotted IP or host name of the destination.

#### utils network
                              	 ipv6

### Command Syntax

utils network ipv6 host {host_name \ ipv6_address}

This command does an IPv6 host lookup (or IPv6 address lookup) for the
                                 		specified host name or IPv6 address.

host_name Specifies the name of the server.

ipv6_address Specifies the IPv6 address of the server.

### Command Syntax

utils network ipv6 traceroute { ipv6-address \ address}

This command does an IPv6 host lookup (or IPv6 address lookup) for the
                                 		specified host name or IPv6 address.

hostname Specifies the host name that you want to trace.

ipv6-address Specifies IPv6 address that you want to trace.

### Command Syntax

utils network ipv6 ping destination [count]

This command allows you to ping an IPv6 address or hostname.

destination Specifies a valid IPv6 address or host name
                                 		that you want to ping. .

count Specifies the number of times to ping the external
                                 		server. The default count equals 4.

### utils ntp

This command displays the NTP status or configuration.

### Command Syntax

utils ntp status

utils ntp config

### Command Syntax

utils ntp restart

### Command Syntax

utils ntp server add s1 [
                                    				  s1| s2| s3| s4| s5 ] [norestart]

The command adds a maximum of five specified NTP servers.

PARAMETERS:

s1... Specifies the NTP servers.

norestart Causes the NTP service to not restart after you
                              		add the servers.

### Command Syntax

utils ntp server delete

This command deletes NTP servers that are configured.

The following warning message, changing this setting will invalidate the software licence is not applicable to Cisco Unified Intelligence Center and can be ignored.

### Command Syntax

utils ntp server list

This command lists all NTP servers.

### Command Syntax

utils ntp start

This command starts the NTP service if it is not already running.

You can not stop the NTP service from the command line interface. Use
                                          		  this command when the utils ntp status command returns stopped.

### utils raid disk maintenance

Use these commands to maintain the RAID disk. They are needed only on servers using RAID software.

### Command Syntax

utils raid disk maintenance disable

### Command Syntax

utils raid disk maintenance enable

### Command Syntax

utils raid disk maintenance status

### utils remote_account

These commands create, enable, disable, and show the status of a remote
                              		account.

A remote account generates a pass phrase that allows Cisco Systems
                              		support personnel to get access to the system for the specified life of the
                              		account. You can have only one remote account that is enabled at a time.

### Command Syntax

utils remote_account create <account> <life>

account is the account name.

life indicates the life of the account in days.

utils remote_account disable

utils remote_account enable

utils remote_account status

### utils_reset

These commands reset user names and passwords.

### Command Syntax

utils
                                    				  reset_application_ui_administrator_name

This command prompts for the new name.

Make sure to do the following while running this command:

Run this command only when replication is running.

Wait for 10 to 15 minutes to ensure that the user name is reset
                                    			 across all nodes.

Restart the Cisco Unified Intelligence Center application on all
                                    			 nodes to complete the process.

Warning

If you log in to the Cisco Unified Intelligence Center application without completing these steps you will lose all administrator
                                          privileges.

### Command Syntax

utils
                                    				  reset_application_ui_administrator_password

### utils
                           	 restore_application_ui_administrator_account

This command restores the administrator account information in the
                              		application.

### Command Syntax

utils
                                    				  restore_application_ui_administrator_account

### utils service

#### utils service list

This command retrieves status for all services.

### Command Syntax

utils service list [page]

OPTION [page] pauses after each page.

#### utils service restart

This command restarts a service.

### Command Syntax

utils service restart serv

PARAMETER serv is the name of the service to restart.

#### utils service start

This command starts a service.

### Command Syntax

utils service start serv

PARAMETER serv is the name of the service to start.

#### utils service stop

This command stops a service.

### Command Syntax

utils service stop serv

PARAMETER serv is the name of the service to stop.

### utils snmp

#### utils snmp get

This command gets the SNMP data for the specified MIB OID.

### Command Syntax

utils snmp get <version>

PARAMETERS:

version is 1 or 2c.

Enter the community string: <Community string>

Enter the ip address of the Server : <IP address of the server>

The Object ID (OID) <Object ID>

Enter parameter as "file" to log the output to a file. [nofile] < name of the text file>

Press Enter to display the results on screen without saving any text files.

#### utils snmp test

This snmp test sends sample alarms to local syslog, remote syslog and
                                 		snmp trap.

### Command Syntax

utils snmp test

#### utils snmp walk

This command is used to walk the SNMP MIB starting with the specified
                                 		OID.

### Command Syntax

utils snmp walk <version>

PARAMETERS:

version is 1 or 2c.

Enter the community string: <Community string>

Enter the ip address of the Server : <IP address of the server>

The Object ID (OID) : <Object ID>

Enter parameter as "file" to log the output to a file. [nofile] <name of the text file>

Press Enter to display the results on screen without
                                 saving any text files.

#### utils snmp configure

##### utils snmp config
                                 	 1/2c community-string

This interactive command adds, deletes, lists or updates a community
                                    		string.

utils snmp config 1/2c community-string { add | | delete | | list | | update }

PARAMETERS:

add Adds a new community string.

delete Deletes a community string.

list Lists all community strings.

update Updates a community string.

##### utils snmp config
                                 	 1/2c inform

This interactive command adds, deletes, lists or updates inform
                                    		notification destinations.

utils snmp config 1/2c inform { add | | delete | | list | | update }

PARAMETERS:

add Adds a notification destination.

delete Deletes a notification destination.

Lists Lists all notification destination.

Update Updates all notification destination.

##### utils snmp config
                                 	 1/2c trap

This interactive command affects trap notifications.

utils snmp config 1/2c trap { add | delete | list | update }

PARAMETERS:

add Adds a new v1/2c trap notification destination
                                    		associated with a configured v1/2c community string.

delete Deletes the configuration information for an
                                    		existing v1/2c trap notification destination.

List Lists the v1/2c trap notifications currently
                                    		configured.

update Updates configuration information for an
                                    		existing v1/2c trap notification destination.

##### utils snmp config
                                 	 3 inform

This interactive command affects the v3 inform notification.

utils snmp config 3 inform { add | | delete | | list | | update }

PARAMETERS:

add Adds a new v3 inform notification destination
                                    		associated with a configured v3 username.

delete Deletes the configuration information for an
                                    		existing v3 inform notification destination.

list Lists the v3 inform notifications currently
                                    		configured.

update Updates configuration information for an
                                    		existing v3 inform notification destination.

##### utils snmp config
                                 	 mib2

This interactive command affects the Mib2 configuration information.

utils snmp config mib2 { add | | delete | | list | | update }

PARAMETERS:

add Adds the Mib2 configuration information.

delete Deletes the Mib2 configuration information.

list Lists the Mib2 configuration information.

update Updates the Mib2 configuration information.

##### utils snmp config
                                 	 3 trap

This interactive command affects trap notifications.

utils snmp config 3 trap { add | | delete | | list | | update }

PARAMETERS:

add Adds a new v3 trap notification destination
                                    		associated with a configured v3 username.

delete Deletes the configuration information for an
                                    		existing v 3 trap notification destination.

list Lists the v3 trap notifications currently
                                    		configured.

update Updates configuration information for an
                                    		existing v3 trap notification destination.

##### utils snmp config
                                 	 3 user

This interactive command affects v3 user configuration.

utils snmp config 3 user { add | | delete | | list | | update }

PARAMETERS:

add Adds a new v3 user with the v3 authentication and
                                    		privacy passwords.

delete Deletes the configuration information for an
                                    		existing v3 user.

list Lists the v3 users currently configured.

update Updates configuration information for an
                                    		existing v3 user.

### utils soap realtimeservice test

This soap test runs a number of test cases on the remote server as specified by a parameter of remote-ip, remote-https-user,
                              or remote-https-password.

### Command Syntax

utils soap realtimeservice test <remote-ip> <remote-https-user> <remote-https-password>

PARAMETERS: (At least one parameter is required.)

remote-ip = remote ip address of the machine under test

remote-https-user = remote http user who has role to access soap api

remote-https-password = remote http users password

### utils system

These commands perform system
                              operations.

#### utils system restart

This command restarts the server after presenting a confirmation (yes |
                                 		no) message.

### Command Syntax

utils system restart

#### utils system shutdown

This command shuts the server down after presenting a confirmation (yes
                                 		| no) message.

### Command Syntax

utils system shutdown

#### utils system
                              	 switch-version

This command switches
                                 		to the other installed version on the server after presenting a confirmation
                                 		(yes | no) message. Note that if you switch back to an earlier version, any
                                 		services or functionality available only in the later version are removed.

### Command
                                    			 Syntax

utils system switch-version

#### utils system upgrade

This command allows you to upgrade the server.

### Command Syntax

utils system upgrade <cancel> <status> <initiate>

PARAMETERS:

cancel cancels the active upgrade.

status gets the status of the upgrade.

initiate starts an upgrade. Specify the required inputs as the
                                 		upgrade proceeds.

### utils vmtools

#### utils vmtools
                              	 refresh

This command refreshes the version of the currently installed VMware
                                    		  tools on the virtual machine to the same version as that of the ESXi host.

### Command Syntax

utils vmtools refresh

The VMware Tools ISO is not mounted in the CD/DVD
                                       			 drive.

Please ensure that you have selected Guest -> Install/Upgrade VMware
                                       			 Tools -> Interactive Tools Upgrade by right-clicking on the VM from your VI
                                       			 client.

After you perform the above step, run the command again utils vmtools refresh

VMware Tools are out-of-date. Proceeding with tools
                                       			 upgrade.

*** W A R N I N G ***

Running this command will update your current
                                       			 version of VMware Tools to the latest version prescribed by the ESXi host on
                                       			 which this VM is running. The tools install will cause your system to reboot
                                       			 twice. Continue (y/n)? Y Starting VMware Tools upgrade
                                       			 ...

Uninstalling VMware Tools 8.6.0-425873...... Done

Restarting system to complete tools
                                       		upgrade...

*** W A R N I N G ***

Restart could take up to 5 minutes... Stopping Service Manager

## Show Commands

### show account

This command lists all accounts except the primary admin account.

### Command Syntax

show account

### show accountlocking

This command shows the current account locking settings.

### Command Syntax

show accountlocking

### show cert

These commands show certificate information about the selected
                              		certificate type.

### Command Syntax

show cert list type

PARAMETER type is mandatory and can be own or trust .

show cert own name

show cert trust name

PARAMETER name must be a valid certificate name.

### show cli

Run this command to show if pagination of the current CLI session is on
                              		or off.

### Command Syntax

show cli pagination

Run this command to show the CLI session timeout. The CLI session
                              		timeout is set to 30 minutes for new CLI sessions.

### Command Syntax

show cli session timeout

### show
                           	 cuic-properties

These commands show
                              		information about Unified Intelligence Center properties.

### Command Syntax

show cuic properties allow-external-links

This command shows the value on or off , depending on the current value set for the allow-external-links property.

### Command Syntax

show cuic properties dashboard-customwidget-enabled

### Command
                                 			 Syntax

show cuic properties host-to-ip

### Command Syntax

show cuic properties http-cache

### Command Syntax

show cuic properties max-large-schedule

### Command Syntax

show cuic properties purge-retention

### Command
                                 			 Syntax

show cuic properties purge-time

### Command
                                 			 Syntax

show cuic properties session-timeout

### Command Syntax

show cuic properties user-audit-logging

### Command Syntax

show cuic properties report-query-timeout

This command shows the time limit, in seconds, that is set for a report query  execution to timeout.

### show cuic component-status

These commands show the status of the Unified Intelligence Center components.

### Command Syntax

show cuic component-status subsystem [options]

PARAMETER subsystem is mandatory.

OPTIONS:

[CuicStatus] shows the status of cuic web engine and the DB replication.

[DBReplStatus] shows the status of database replication on this node.

[DBStatus] shows the database status.

### show diskusage

These commands show disk usage of the given directory as well as the
                              		usage of the disk partition the directory exists on.

### Command Syntax

show diskusage activelog [options]

show diskusage common [options]

show diskusage inactivelog [options]

show diskusage install [options]

show diskusage tftp [options]

show diskusage tmp [options]

OPTIONS:

[file fname] outputs the information to a file saved in
                              		platform/cli/fname.

[directory] show only directory sizes.

[sort] sorts output by sizes in 1024 byte blocks.

### show environment

These commands retrieve the current reading of the various fan,
                              		power-supply, or temperature sensors.

### Command Syntax

show environment fans

show environment power-supply

show environment temperatures

### show hardware

This command retrieves some basic platform hardware information.

### Command Syntax

show hardware

### show ipsec

Use these commands to display ipsec policies.

### Command Syntax

show ipsec information [ policy_group ] [ policy-name ]

### Command Syntax

show ipsec policy_group

### Command Syntax

show ipsec policy_name

### Command Syntax

show ipsec status

### show logins

This command shows the last number of platform admin logins. The default
                              		is to show 20 logins.

### Command Syntax

show logins last n

OPTION:

[last n] specifies a number of logins to show. Entering the command with
                              		no option shows 20 logins. Specifying a value of 0 will display all previously
                              		saved logins.

### show memory

These commands displays information about the server memory.

### Command Syntax

show memory count

show memory module module
                                    				  number

show memory module ALL

show memory size

### show myself

This command shows information about the current account: machine name,
                              		account name, admin privilege level, output setting and logging setting. Use
                              		the commands set
                                 		  commandcount and set
                                 		  logging to modify current account settings.

### Command Syntax

show myself

### show network

#### show network all

This command retrieves all basic platform network information.

### Command Syntax

show network all [options]

OPTIONS:

[detail] displays more detail.

[page] pauses the output .

[search srchtxt] looks for srchtxt in the output. This is a
                                 		case-insensitive search.

#### show network
                              	 cluster

This command shows
                                 		the nodes that are part of the network cluster.

### Command
                                    			 Syntax

show network cluster

#### show network dhcp eth0 status

This command displays the DHCP status on eth0.

### Command Syntax

show network dhcp eth0 status [options]

#### show network failover

This command shows network fault tolerance information.

### Command Syntax

show network failover [options]

OPTIONS:

[detail] displays more detail.

[page] pauses the output.

#### show network ip_conntrack

This command retrieves the current utilization of ip_conntrack.

### Command Syntax

show network ip_conntrack [options]

#### show network
                              	 ipprefs

These commands display the network ports and their status.

### Command Syntax

show network all

show network enabled

show network public

#### show network ipv6

This command shows
                                 		the IPv6 network settings.

### Command
                                    			 Syntax

show network ipv6 settings

### Command
                                    			 Syntax

show network ipv6 route [options]

OPTIONS:

optional.

detail.

#### show network max_ip_conntrack

This command retrieves ip_conntrack_max information.

### Command Syntax

show network all

#### show network
                              	 ntp

This command displays security option configured on /etc/ntp.conf file.

### Command Syntax

show network ntp option

#### show network route

This command retrieves some basic platform network route information.

### Command Syntax

show network route [options]

OPTIONS:

[detail] displays more detail.

[search srchtxt] looks for srchtxt in the output. This is a
                                 		case-insensitive search.

#### show network status

This command retrieves some basic platform network status information.

### Command Syntax

show network status [options]

OPTIONS:

[detail] displays additional information.

[listen] displays only listening sockets.

[process] displays the process ID and name of the program to which each
                                 		socket belongs.

[all ] displays both listening and non-listening sockets.

[nodes] displays numerical addresses without any DNS information.

[search sext] searches for the "sext" in the output. This is a
                                 		case-insensitive search.

### show open

#### show open files

These commands show open files.

### Command Syntax

show open files all

### Command Syntax

show open files process ProcessID1, ProcessID2

PARAMETER Processid must be a valid process id. You can enter a
                                 		comma-delimited list of processes.

### Command Syntax

show open files regex "regex"

PARAMETER "regex" is the regular expression to match and must be enclosed in
                                 		quotation marks.

#### show open ports

These two commands show open ports.

### Command Syntax

show open ports all

### Command Syntax

show open ports regex "string"

### show packages

These commands retrieve the version number of one or more packages on
                              		the active or inactive side.

### Command Syntax

show packages active pkg [page]

show packages inactive pkg [page]

PARAMETER pkg must be a valid package name.

OPTION:

[page] pauses the display.

### show password

Use these commands to configure password rules.

### Command Syntax

show password age maximum | days minimum | days

show password complexity character minimum-length

### Command Syntax

show password expiry maximum-age minimum-age user

### Command Syntax

show password history number

### show perf

#### show perf counterhelp

This command lists the explaining text for a particular perfmon counter.

### Command Syntax

show perf counterhelp <class-name> <counter-name>

PARAMETERS:

class-name is the perf class name that contains the perf counter.

counter-name is the perf counter name to view.

#### show perf list

These four commands show various perfmon information.

### Command Syntax

show perf list categories

### Command Syntax

show perf list classes [options]

### Command Syntax

show perf list counters class-name [options]

### Command Syntax

show perf list instances class-name [options]

PARAMETER class-name is the name of the perfmon class.

OPTIONS:

[cat category] shows perfmon classes for a particular category.

[detail] shows detailed information.

#### show perf query

These four commands show various perfmon queries.

### Command Syntax

show perf query class class-name

Most Unified Intelligence Center counters display with this command. For example show perf query class SchedulerInfo shows the SchedulerIntervalLength , SchedulerJobsCompletedCount , SchedulerJobsFailedCount , SchedulerJobsRunningCount , and SchedulerState .

### Command Syntax

show perf query counter class-name <counter-name, counter-name...>

### Command Syntax

show perf query instance <class-name> <instance-name, instance-name...>

### Command Syntax

show perf query path path-spec, path-spec

class-name is the name of the perfmon class. Accepts a
                                 		comma-delimited list of up to five class-names. If class-name contains white
                                 		space, enclose it in double quotes.

counter-name is the counter name to view. You can query a maximum of five
                                 		comma-delimited counter-names. If the name contains white space, enclose it in
                                 		double quotes.

instance-name is the instance name to view. You can query a
                                 		maximum of five comma-delimited instance-names. If the name contains white
                                 		space, enclose it in double quotes.

path-spec is the perfmon query path to view. You can query a
                                 		maximum of five, comma-delimited path-specs.

### show process

These commands show process
                              information.

#### show process list

This command is used to get the list of all the processes, and critical
                                 		information about each one of them. This command also displays visually the
                                 		child-parent relationship between these processes.

### Command Syntax

show process list [options]

OPTIONS:

[file] - optional file-name for the output.

[detail] - optional detailed output.

#### show process load

This command shows the current load on the system including the number "num" of processes using the most cpu or memory or
                                 time.

### Command Syntax

show process load [options]

OPTIONS:

[cont] - the command will repeat continuously.

[clear] - the screen will clear before displaying output.

[noidle] - the command will ignore the idle/zombie processes.

[num XX] - configure the number of processes to be displayed (using most
                                 		cpu) XX is the number of processes: default is 10 processes; minimum value is 1;
                                 		use 'all' for all processes.

[thread] - show threads.

[cpu]- sort output by CPU usage.

[memory] - sort output by memory.

[usage time] - sort output by time usage.

[page] - pause output.

#### show process name

This command is used get the details of processes that share the same
                                 		name. This also displays parent-child relationship.

### Command Syntax

show process name process-name [file-filename]

PARAMETER process-name must be a valid process name.

OPTION [file file-name] is the file-name for the output.

#### show process open-fd

This command is used to list the open file descriptors for a comma
                                 		separated list of process Ids.

### Command Syntax

show process open-fd p1, p2, p3 [file]

PARAMETER p1 is the process ID. You can enter a comma-separated string of
                                 		process IDs.

OPTION [file] is the file-name for the output.

#### show process search

This command lets you search some particular patterns in the output of
                                 		the operating system specific process listing.

### Command Syntax

show process search regexp [file]

PARAMETER regexp specifies the regular expression.

OPTION [file] is the file-name for the output.

#### show process
                              	 user

This command displays the user and more details on the process used,
                                 		including the virtual memory used and others.

### Command Syntax

show process user user-name [options]

user-name is mandatory.

OPTION :

[file] is the file-name for the output.

[vm] is the virtual memory of the process.

[detail] show process's page fault, virtual memory, start time and
                                 		others.

[cont] to repeat the command continuously.

#### show process using-most

These commands show the processes using the most cpu or the most memory.

### Command Syntax

show process using-most cpu [options]

show process using-most memory [options]

OPTIONS:

[file] - the file-name for the output.

[number] - The number of processes. The default is 5.

### show registry

This command displays the contents of the registry.

### Command Syntax

show registry <system> <component name> page

PARAMETERS:

system represents the registry system name.

component represents the registry component name.

OPTION: [page] displays one page at a time.

### show smtp

This command shows the SMTP server.

### Command Syntax

show smtp

### show stats io

This command shows system input/output statistics of the machine.

### Command Syntax

show stats io [options]

OPTIONS:

[kilo ] display statistics in kilobytes.

[detail] displays detailed statistics of every available device on the
                              		system. This option overrides the [kilo] option.

[page] pauses the output.

[file fname] outputs to a file. The file is saved in
                              		platform/cli/fname.txt. The fname must not contain the " character.

### show status

This command retrieves basic platform status.

### Command Syntax

show status

### show tech

#### show tech activesql

This command shows the active queries to the database taken in the last
                                 		one minute.

### Command Syntax

show tech activesql

#### show tech all

This command displays all of the different show tech xxx commands and
                                 		may produce a large output of data.

### Command Syntax

show tech all [options]

OPTIONS:

[page] displays one line at a time.

[file fname] outputs to a file saved in platform/cli/fname.txt.

#### show cuic tech

These commands display information about the Unified Intelligence Center database.

### Command Syntax

show cuic tech procedures

This command shows the procedures in use for the Unified Intelligence Center database.

### Command Syntax

show cuic tech systables

This command displays the name of all tables in the Unified Intelligence Center database.

### Command Syntax

show cuic tech table <tablename>

This command shows the contents of a table on the Unified Intelligence Center database.

PARAMETER tablename is mandatory and must be the name of a table in the Unified Intelligence Center database.

### Command Syntax

show cuic tech triggers

This command displays Unified Intelligence Center table names and the triggers associated
                                 		with those tables.

#### show tech database

These commands show database information.

### Command Syntax

show tech database dump [options]

This command dumps the database so that you can send it for debugging.

OPTIONS:

[ccm] - operating system database. This is the default. If you do not
                                 		include the cuic option, this command shows the operating system database.

[cuic] - Unified Intelligence Center database.

### Command Syntax

show tech database sessions

This command redirects the session and SQL information of present
                                 		session IDs to a CSV file.

#### show tech dberrorcode

This command shows the explanation for a particular database errorcode.

### Command Syntax

show tech dberrorcode errorcode

PARAMETER errorcode is mandatory. Enter the code for the error you are
                                 		investigating.

#### show tech dbintegrity

This command checks database server specified disk structures for
                                 		inconsistencies and displays output in a file.

### Command Syntax

show tech dbintegrity

#### show tech dbinuse

This command displays the database in use.

### Command Syntax

show tech dbinuse

#### show cuic tech dbschema

This command displays the database schema in a CSV file.

### Command Syntax

show cuic tech dbschema [options]

OPTIONS:

[ccm] - operating system database. This is the default. If you do not
                                 		include the cuic option, this command shows the operating system schema.

[cuic] - Unified Intelligence Center database.

#### show tech dbstateinfo

This command shows the database state information and outputs it to a
                                 		file.

### Command Syntax

show tech dbstateinfo

#### show tech dumpCSVandXML

This command collects csv and xml files into a single tar file.

### Command Syntax

show tech dumpCSVandXML

#### show tech network

These commands shows network aspects of the system.

### Command Syntax

show tech network all [options]

show tech network hosts [options]

show tech network interfaces [options]

show tech network resolv [options]

show tech network routes [options]

show tech network sockets [options]

OPTIONS:

[page] displays one line at a time.

[search txt] searches the output for txt *. Case insensitive search.

[file fname] outputs to a file saved in platform/cli/fname.txt.

[numeric] displays ports in numeric format.

#### show tech notify

This command displays the database change notify monitor.

### Command Syntax

show tech notify [search pattern]

OPTION [search pattern] is a string that needs to be searched in the
                                 		command output.

#### show tech params

These commands display the database parameters.

### Command Syntax

show tech params all

### Command Syntax

show tech params enterprise

### Command Syntax

show tech params service

#### show cuic tech procedures

This command displays the stored procedures in use for the database.

### Command Syntax

show cuic tech procedures [options]

OPTIONS:

[ccm] - operating system database. This is the default. If you do not
                                 		include the cuic option, this command shows the procedures in use for the
                                 		operating system database.

[cuic] - Unified Intelligence Center database.

#### show tech repltimeout

This command shows the replication timeout setting.

### Command Syntax

show tech repltimeout

#### show tech sqlhistory

This command collects sqlhistory statements into a single file (*.out)
                                 		and directs you to the location of that file.

### Command Syntax

show tech sqlhistory

#### show cuic tech systables

This command displays the name of all tables in the database.

### Command Syntax

show cuic tech systables [options]

OPTIONS:

[ccm] - operating system database. This is the default. If you do not
                                 		include the cuic option, this command shows the tables in the operating system
                                 		database.

[cuic] - Unified Intelligence Center database.

#### show tech system

These commands show various aspects of the system.

### Command Syntax

show tech system all [options]

show tech system bus [options]

show tech system hardware [options]

show tech system host [options]

show tech system kernel

show tech system software

show tech system tools

OPTIONS:

[page] displays one line at a time.

[file fname] outputs to a file are saved in platform/cli/fname.txt.

#### show cuic tech table

This command redirects the contents of the specified database table
                                 		into a file.

### Command Syntax

show cuic tech table [options]

This command shows the contents of a table on the operating system
                                 		database.

PARAMETER tablename must be the name of a table in the database.

OPTIONS:

[ccm] - operating system database. This is the default. If you do not
                                 		include the cuic option, this command shows only tables in the operating
                                 		system database.

[cuic] - Unified Intelligence Center database.

This example shows the cuicversion table from the cuic database: show cuic tech table cuicversion cuic .

#### show cuic tech triggers

This command displays table names and triggers associated with those
                                 		tables.

### Command Syntax

show cuic tech triggers [options]

OPTIONS:

[ccm] - operating system database. This is the default. If you do not
                                 		include the cuic option, this command shows the table name and triggers
                                 		associated with the operating system database.

[cuic] - Unified Intelligence Center database.

#### show tech version

This command displays the version of all RPMs (RedHat Package Manager)
                                 		installed on the system.

### Command Syntax

show tech version

### show timezone

These commands display the currently-configured timezone or list of all
                              		zones.

### Command Syntax

show timezone config

### Command Syntax

show timezone list

### show tls server cert_type

This command displays the configured certificate type used by the server for TLS connections.

Command syntax

show tls server cert_type

```
admin:show tls server cert_type
The server certificate type is set to ECDSA

Command successful
```

### show ups status

This command communicates with an attached Uninterruptible Power Supply
                              		and displays status.

### Command Syntax

show ups status

### show version

This command displays the software version on the active or inactive
                              		side.

### Command Syntax

show version [ active | inactive ]

The indicator to the active or inactive partition is required.

### show web-security

This command displays web security information.

### Command Syntax

show web-security

### show workingdir

This command displays the current working directories for the activelog
                              		and inactivelog.

### Command Syntax

show workingdir

## Set Commands

### set account

### Command Syntax

set account name

PARAMETER name specifies the name of the admin account.

### Command Syntax

set account enable

### set accountlocking

Use these commands to control the administrator accounts.

### Command Syntax

set accountlocking { enable | disable | unlocktime }

PARAMETER enable enables account locking.

PARAMETER disable disables account locking.

PARAMETER unlocktime used to configure the unlock time for admin
                              		accounts in seconds. Acceptable values are equal to or greater than 300 seconds
                              		but less than 3600 seconds (60 mins).

### set cert

This command regenerates the certificate for the unit name. See also show cert .

### Command Syntax

set cert bulk { unit | all }

### Command Syntax

set cert import { unit | all }

### Command Syntax

set cert regen unit name

PARAMETERS:

unit and unit name specifies the name of the unit.

### set cli

Run this command to set the pagination of the current CLI session.

### Command Syntax

set cli pagination name

PARAMETER on or off

Run this command to set the CLI session timeout minutes. Minutes are
                              		mandatory. The number of minutes after which sessions are declared to be
                              		invalid; range is 5 to 99999.

### Command Syntax

set cli session timeout minutes

### set commandcount

These commands change the CLI command prompt, so it displays or hides the number of CLI commands run in the current session.

### Command Syntax

set commandcount enable

set commandcount disable

### set cuic
                           	 properties

Use these commands to set values for the Unified Intelligence Center properties.

### Command Syntax

set cuic properties allow-external-links

PARAMETER <on|off>

This command sets the allow-external-links property to on or off . By setting the value to on or off , you can enable or disable the external links in Unified Intelligence Center dashboard respectively. By default, the value
                                 is set to off .

After the upgrade, the external links in the Unified Intelligence Center dashboard will be disabled.

If enabled, the contents from external links are rendered within the HTML iFrame in the dashboard. This will include the frame-src* directive in the Content Security Policy of the Unified Intelligence Center web pages.

### Command Syntax

set cuic properties dashboard-customwidget-enabled

PARAMETER <on|off>

This command sets the dashboard-customwidget-enabled property to on or off . By setting the value to on or off , you can enable or disable the Custom Widget feature in Dashboards respectively. By default, the value is set to off .

Enabling the custom widget configuration can lead to injection vulnerabilities.

### Command Syntax

set cuic properties host-to-ip

PARAMETER <host> <ip-address>

This command sets the IP to be used for the data source host name that is specified while configuring the Unified Intelligence
                              Center data source. This command allows for scalability and overrides the default Historical or Real-time database server
                              that is defined in the Data Sources interface.

For <host> , enter the value for the host DNS name for the server, as displayed on the Data Sources interface.

The hostname is case-sensitive. Enter the hostname exactly as entered on the Data Sources interface.

For <ip-address> , enter the IP address of the server for the
                              		Historical or Real-time database.

You must restart the Unified Intelligence Center Reporting Services
                                          		  for the change to take effect.

### Command Syntax

set cuic properties max-large-schedule

PARAMETER # of large schedules

This command sets the limit for maximum number of large schedules that you can create. The valid range is 1-6 large schedules.
                              The default value is 1.

You must restart the Unified Intelligence Center Reporting Services for the change to take effect

### Command Syntax

set cuic properties purge-time

PARAMETER 1 <HH:MM > <AM/PM>

PARAMETER 2 <Interval (in minutes)>

This command sets the time of day when the Unified Intelligence Center
                              		database will be purged and the duration (in minutes) after which the purge
                              		operation should be rerun. The default purge time is 12:00 AM and the default
                              		purge interval is 60 minutes.

For <HH:MM> and <AM/PM> specify the time of the day when you want the purge
                              		job to run for the first time.

For <Interval (in minutes)> , specify the interval in minutes
                              		after which you want the purge job to rerun.

After you run this command with the correct parameters, the system
                              		displays a message as follows:

```
Next purge is scheduled to run after <x> hours <y> minutes.
Value has been successfully set.
```

Following are the various categories of data that the system purges when you use these CLI commands:

Cached report data - Data in this category is purged based on
                                    			 the time specified using the set cuic properties purge-time command. Note that
                                    			 the purge time is calculated based on the time when the filter used to run the
                                    			 report was last used or refreshed.

Audit trail - All audit trail data that is older than a month
                                    			 are purged during the last purge operation of the day.

Cached scheduled report data - The set cuic properties purge-retention CLI command
                                    			 applies only to this category.

Each rerun that the system performs using this command, results in the
                              		purging of the cached report data. Other categories are purged only during the
                              		last purge run of the day.

If you restart the Unified Intelligence Center server after the purge start time, the system discontinues the current purge
                              cycle until the same purge start time on the next day.

For example, if you have set to run the purge job at 11.45 AM on a day with a rerun interval of 1 hour and the Unified Intelligence
                              Center server was restarted at 2 PM, the following happens with respect to the purge runs and reruns:

Purge job runs typically at 11.45 AM, 12.45 PM., and 1.45 PM.

After the restart at 2 PM, the system checks for the purge start time and since the purge start time is set as 11.45 AM, the
                                    next purge run happens only at 11.45 AM on the next day.

To have continuous rerun even after the system restarts, you must set
                              		the purge start time and interval again using the set cuic properties purge-time CLI command.

### Command Syntax

set cuic properties purge-retention

PARAMETER #number of days

This command sets the number of days that data in the Unified Intelligence Center database is retained before it gets purged.
                              The default is one day and the maximum permissible value is 31 days.

### Command Syntax

set cuic properties session-timeout

PARAMETER #numberofSeconds

This command sets the Session Timeout for the Unified Intelligence Center Reporting web application. The valid range is 1,800-14,400
                              seconds. The default is 14,400 seconds (4 hours).

You must restart the Unified Intelligence Center Reporting Services for the change to take effect.

### Command Syntax

set cuic properties http-cache

PARAMETER <on|off>

This command sets the http-cache property to on or off . By setting the value to on or off , you can enable and disable the HTTP cache control. By default, the value is set to on.

### Command Syntax

set cuic properties user-audit-logging

PARAMETER <on|off>

This command sets the user-audit-logging property to on or off . By setting the value to on or off , you can enable or disable the user audit logging. By default, the value is set to off .

### Command Syntax

set cuic properties report-query-timeout

PARAMETER number of seconds

Range: 180-3600 seconds

This command sets the report query execution timeout value. The command is applicable when you run the report using the interface
                                 and does not apply to scheduled reports.

Example

```
set cuic properties report-query-timeout 250
WARNING : Do not change it to a higher value, as it may cause performance issue.

cuic.query.timeout has been updated
This command requires a restart of Intelligence Center service.
Ensure that this command is run on all nodes in the cluster.
```

### set ipsec

Use these commands to enable ipsec policies.

### Command Syntax

set ipsec policy_group { group | all }

### Command Syntax

set ipsec policy_name [policy_group] [policy_name]

### set logging

These commands allow you to enable or disable logging.

### Command Syntax

set logging enable

set logging disable

### set network

#### set network cluster publisher

Caution

### Command Syntax

set network cluster publisher
                                       				  hostname

### Command Syntax

set network cluster publisher
                                       				  ip

#### set network dhcp eth0

These commands set the ethernet interface to disable dhcp (if enabled) or to use dhcp (if not already enabled). Entering this
                                 command prompts for verification and, if run, causes the system to restart.

### Command Syntax

set network dhcp eth0 enable

set network dhcp eth0 disable

#### set network dns options

This command allows you to set the dns options.

### Command Syntax

set network dns options [options]

OPTIONS:

[timeout xx] sets the DNS request timeout in seconds.

[attempts xx] sets the number of times to attempt a DNS request before
                                 		quitting.

[rotate] causes the system to rotate among the configured DNS servers,
                                 		distributing the load.

#### set network dns {primary | secondary}

These commands set the IP address for the primary or secondary DNS server. Entering this command prompts for verification
                                 and, if run, causes a loss of network connectivity.

### Command Syntax

set network dns primary addr

set network dns secondary addr

PARAMETER addr specifies the address of the server.

#### set network domain

This command sets the domain name for the system. Entering this command prompts for verification and, if run, causes a loss
                                 of network connectivity.

### Command Syntax

set network domain name

PARAMETER name specifies the name of the domain.

#### set network failover

These commands enable and disable Network Fault Tolerance on the Media Convergence Server network interface card. Entering
                                 the command prompts for verification and, if run, causes the system to restart.

### Command Syntax

set network failover ena op

set network failover dis op

PARAMETER op indicates the operation.

#### set network gateway

This command enables you to configure the IP address of the network gateway. Entering this command prompts for verification
                                 and, if run, causes the system to restart.

### Command Syntax

set network gateway addr

PARAMETER addr specifies the address of the gateway.

#### set network hostname

This command sets the network hostname and then causes a restart of the
                                 		system The hostname must follow the rules for ARPANET host names. The hostname
                                 		must start with an alphabet, end with an alphanumeric, and may contain any
                                 		alphanumeric characters or hyphens in between. The hostname must be 63
                                 		characters or less.

### Command Syntax

set network hostname [ name ] addr

PARAMETER name specifies the network hostname.

#### set network IP
                              	 eth0

This command sets
                                 		the IP address for Ethernet interface 0.

The system asks whether you want to continue to run this command. If you continue, this command causes the system to restart.

### Command
                                 		  Syntax

set network ip eth0 <ipaddr> <mask> <gateway>

PARAMETERS:

ipaddr is the IP
                                 		address.

mask is the mask.

gateway is the gateway.

#### set network
                              	 ipv6

These commands are
                                 		used for configuring the IPv6 feature on the machine.

### Command
                                    			 Syntax

set network ip dhcp action reboot

### Command
                                    			 Syntax

set network ip service action reboot reboot

### Command
                                    			 Syntax

set network ipv6 static_address addr mask

PARAMETERS:

Action is mandatory can
                                 		have either of these values: {enable |
                                    		  disable}

mask is the mask.

Reboot . Reboot after
                                 		making these changes.

addr is the IP address.

mask is the mask.

#### set network max_ip_conntrack

This command sets the maximum value for ip_conntract_max.

### Command Syntax

set network max_ip_conntrack ip_conntrack_max

PARAMETER ip_conntrack_max indicates the maximum value.

#### set network mtu

This command sets the maximum MTU value. The valid range is 500-1500.

### Command Syntax

set network mtu size

PARAMETER size must be 1500 for all servers in the cluster.

#### set network nic eth0

This command sets the properties of the Ethernet Interface 0. It asks if
                                 		you want to continue. If you continue, this command causes a temporary loss of
                                 		network connections while the NIC is reset.

### Command Syntax

set network nic etho0 auto [ en | dis ] speed [ 10 | 100 ] duplex [ half | full ]

PARAMETERS: At least one is mandatory. Each parameter takes options
                                 		indicated.

auto specifies whether auto negotiation gets enabled or disabled.

speed specifies the speed of the Ethernet connection: 10 or 100
                                 		Mbps.

duplex specifies half-duplex or full-duplex.

#### set network pmtud

This command enables or disables Path MTU Discovery.

The system asks whether you want to continue to run this command. If you continue, the system temporarily loses network connectivity.

### Command Syntax

set network pmtud state { enable | disable }

PARAMETER state {enable | disable}

#### set network restore

This command restarts the networking on this host. If confirmed, this
                                 		command causes a temporary loss of network connectivity.

Caution

### Command Syntax

set network restore <ethernet port> <ip-address> <network-mask> <gateway>

PARAMETERS:

ethernet-port is the Ethernet port (for example, eth0).

ip-address is the IP address of the host.

network-mask is the network mask.

gateway is the Gateway IP address.

#### set network status eth0

This command sets the state of the ethernet interface eth0 to up or
                                 		down.

Caution

### Command Syntax

set network status eth0 state { up | down }

PARAMETER state {up | down} to set the status up or down is required.

### set password

Use these commands to configure password rules.

### Command Syntax

set password age maximum | days minimum | days

set password complexity character minimum-length

set password system bootloader encryptHash

set password change-at-login enable\disable

Use this commands to enable or disable password complexity rules.

### Command Syntax

set password expiry maximum-age minimum-age

set password history number

set password inactivity { enable | disable | period (days) }

Use these commands to enable the operating system password inactivity to the default value of 10 days, to disable password
                              inactivity, or set the number of days.

### Command Syntax

set password user admin security

These commands allow you to change the system administrator and security passwords.

The system prompts you for the old and new passwords and checks the password for strength.

PARAMETERS:

character takes {enable | disable}

When enabled, passwords need to meet these guidelines:

Have at least one lower-case character.

Have at least one uppercase, one digit and one special character.

Contain no characters that are adjacent on the keyboard.

Have not been used as any of the previous ten passwords. The admin user password can be changed only once in 24 hours.

Cannot have been changed in the past 24 hours.

minimum-length

When enabled, modify the value of minimum password length for Unified CM OS accounts. Acceptable values should be equal to
                              or greater than 6. Use this command only after enabling the character complexity of passwords.

maximum days - Sets the value of the maximum age for the admin accounts in days. Acceptable values should be equal to or greater than
                              10 days but less than 3650 days (10 years).

minimum days - Sets the minimum password age for the admin accounts in days.

maximum-age - Takes {enable | disable) .

Enabling the maximum age sets the value of maximum password age to 3650 days (10 yrs) for CUCM OS admin accounts.

minimum-age - Takes {enable | disable) .

number - The number of passwords to maintain in history. Default is 10. Maximum is 20. Enter 0 to disable.

admin - Sets the admin password.

security - Sets the security password.

### set smtp

This command sets the SMTP server hostname.

### Command Syntax

set smtp host

PARAMETER host indicates the hostname for the smtp server.

### set cuic syslog

This command sets the syslog as enabled or disabled.

### Command Syntax

set cuic syslog { enable | disable }

### set timezone

This command changes or sets the timezone. You must restart the system
                              		after you change the timezone.

### Command Syntax

set timezone zone

PARAMETER zone indicates the timezone.

Enter the appropriate string or zone index id to uniquely identify the
                              		timezone.

To see a list of valid timezones, use the show timezone command.

Be aware that the timezone name is case-sensitive.

### set tls server cert_type

Use this command to set the server certificate type to either RSA or ECDSA ciphers for TLS connections. The certificate set
                                 to the specified type is then presented for the cipher negotiations on all incoming TLS communications.

Command syntax

set tls server cert_type  [option]

Option

ecdsa—Sets the certificate type to ECDSA.

rsa—Sets the certificate type to RSA.

Example

```
admin:set tls server cert_type rsa

Configuring the server to use RSA certificates for all inbound connections.

Do you want to continue (y/n) ? y
Yes entered
Configuring the server to use RSA ciphers for inbound connections.

Successfully configured the server to use RSA certificate for all inbound connections.

********************************************************
A system reboot will occur for the changes to take effect.
It is highly recommended that you perform a system backup
after the system reboot.
Ensure all the nodes in the cluster are running on the same
certificate type by running the 'set' command
********************************************************

Broadcast message from root@uccxfirstnode (Mon Jul 5 10:31:04 2021):

The system is going down for reboot in 1 Minute

Broadcast message from root@uccxfirstnode (Mon 2021-07-05 10:31:05 IST):

The system is going down for reboot at Mon 2021-07-05 10:32:04 IST!
```

### set tls min-version

This command allows you to set the minimum TLS version in the server or client that can be used for inbound or outbound SSL
                              connections respectively. You must restart the system for the changes to take effect.

When you upgrade the TLS minimum version from TLSv1.0 to TLSv1.1 or TLSv1.2, reinstall the Cisco Unified Real-Time Monitoring
                                                Tool.

In a multi-node CUIC deployment, run this CLI command on all the nodes of the cluster starting from the publisher. Restart
                                                all the nodes after executing the CLI command.

### Command Syntax

set tls [server | client] min-version <1.0|1.1|1.2>

### set web-security

This command sets the web security certificate information for the
                              		operating system.

### Command Syntax

set web-security <orgunit> <orgname> <locality> <state> < country> [hostname]

PARAMETERS: (First five parameters are mandatory.)

orgunit is the organizational unit.

orgname is the organizational name.

locality is the location of the organization.

state is the state of the organization.

country is the country of the organization.

hostname is the alternate hostname. This parameter is optional.

For more information about  setting the alternative host name, see https://supportforums.cisco.com/docs/DOC-6119 .

### set workingdir

These commands set the CLI working directory for activelog or
                              		inactivelog.

### Command Syntax

set workingdir activelog directory

set workingdir inactivelog directory

PARAMETER directory must be a valid sub-directory of the activelog or
                              		inactivelog.

## Run Commands

### run loadxml

This command can be run on the publisher (the Controller node) as a
                              		workaround when service parameters or product specific information does not
                              		appear on the administration screen.

Running this command might necessitate a restart of some services.

### Command Syntax

run loadxml

### run cuic sql

This runs a SQL command to query and select from the database and table.

### Command Syntax

run cuic sql sql statement [options]

PARAMETER sql statement specifies the SQL command to run. For example, select * from
                              		tablename.

OPTIONS:

[ccm] - operating system database. This is the default. If you do not
                              		include the cuic option, this command runs a sql statement from the system
                              		database.

[cuic] - Unified Intelligence Center database. For example, select * from cuic:tablename

You can run only one sql_statement at a time. But in the sql_statement
                              		you can use multiple tables. For example: Select * from cuic:cuicreport, cuic_data:cuicreportdefinition .

### run
                           	 loadcsv

This command runs on the publisher, to install product csv's on the
                              		server. It is necessary to run this command on the publisher only.

Running this command might necessitate a restart of some services.

### Command Syntax

run loadcsv

## file
                        	 commands

File commands that include activelog list a livedata directory. For Packaged CCE deployments only, this directory contains logs for the Live Data reporting components.

### file check

This command checks whether any files or directories have been added,
                              		removed, or changed in size since the last fresh installation or upgrade. The
                              		results display after the check.

### Command Syntax

file check [detection-size-kb]

OPTION: [detection-size-kb] specifies the minimum file size change that
                              		is required for the command to display the file as changed. The default is
                              		100Kb.

### file delete

These commands delete one or more specified files.

### Command Syntax

file delete activelog file-spec [options]

file delete inactivelog file-spec [options]

file delete install file-spec [options]

PARAMETERS:

file-spec specifies the path and filename of the file(s) to
                              		delete.

OPTIONS:

[detail] displays a listing of deleted files with the date and time.

[noconfirm] deletes files without asking you to confirm each deletion.

Caution

### file dump

These commands dump the contents of the indicated files to the screen,
                              		one page at a time.

### Command Syntax

file dump activelog file-spec [options]

file dump inactivelog file-spec [options]

file dump install file-spec [options]

file dump sftpdetails file-spec [options]

PARAMETER file-spec specifies the path and filename of the
                              		file(s) to dump.

OPTIONS:

[detail] displays listing with the date and time.

[hex] displays output in hexadecimal.

### file get

These commands get (transfer) the specified file to another system by
                              		using SFTP. After the command identifies the specified files, you are prompted
                              		to enter an SFTP host, username, and password.

### Command Syntax

file get activelog file-spec [options]

file get inactivelog file-spec [options]

file get install file-spec [options]

file get partBsalog file-spec [options]

file get salog file-spec [options]

PARAMETER file-spec specifies the path and filename of the
                              		file(s) to transfer.

OPTIONS:

[abstime] is absolute time period, specified as hh:mm:MM/DD/YY.

[reltime] is relative time period, specified as minutes | hours | days |
                              		weeks | months value.

[match] matches a particular string in the filename, specified as string
                              		value.

[recurs] gets all files, including subdirectories.

### file list

These commands list the log files in an available log directory.

### Command Syntax

file list activelog file-spec [options]

file list inactivelog file-spec [options]

file list install file-spec [options]

file list partBsalog file-spec [options]

file list salog file-spec [options]

PARAMETER file-spec specifies the path to the directory to list.

OPTIONS:

[page] displays the output one screen at a time.

[reverse] reverses sort direction.

[detail] displays a long listing with date and time.

[date] sorts by date.

[size] sorts by file size.

### file search

These commands search the content of a log and display the matching
                              		lines one page at a time.

### Command Syntax

file search activelog file-spec [options]

file search inactivelog file-spec [options]

file search install file-spec [options]

PARAMETERS:

file-spec represents the path to the file(s) to search.

reg-exp represents a regular expression.

OPTIONS:

[reltime] only search files that were modified within relative time.

[abstime] only search files that were modified within specific time
                              		range.

[ignorecase] ignores case distinctions.

[recurs] searches for the pattern recursively through subdirectories.

### file tail

These commands tail (print the last few lines) of a log file.

### Command Syntax

file tail activelog file-spec [options]

file tail inactivelog file-spec [options]

file tail install file-spec [options]

PARAMETER file-spec specifies the path to the file to tail.

OPTIONS:

[detail] displays a long listing with date and time.

[hex] displays hexadecimal listing.

[lines] specifies number of lines to display.

### file view

These commands display the contents of the logging files specified.

### Command Syntax

file view activelog file-spec

file view inactivelog file-spec

file view install file-spec

file view system-management-log

PARAMETER file-spec specifies the path to the file to view.

## Delete Commands

### delete account

This command allows you to delete an administrator account.

### Command Syntax

delete account name

PARAMETER name specifies the name of the admin account.

### delete dns

This command deletes the specified DNS server from the system and
                              		results in loss of network connectivity.

### Command Syntax

delete dns addr

PARAMETER addr specifies the IP address name of the domain name server.

### delete ipsec

These commands allow you to delete IPSec policies. You can delete a
                              		pokcy with a given policy name and group.

### Command Syntax

delete ipsec policy_group [ group | all ]

### Command Syntax

delete ipsec policy_name [policy_group] [policy_name]

PARAMETERS:

policy_group

policy_name

### delete process

This command allows you to delete a particular process.

### Command Syntax

delete process pid [ options ]

PARAMETER pid specifies the process ID number.

OPTIONS:

[force] stops the process.

[terminate] terminates the process.

[crash] crashes the process with a crash dump.

### delete smtp

This command deletes the SMTP host.

### Command Syntax

delete smtp

## Use CLI

If you choose to configure Unified Intelligence Center with Live Data using CLI commands, refer chapter 4 on Live Data Installation in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Certain CLI commands are useful for specific inquiries.

| Note | Without any option, this command opens an interactive command line based console. With a given input file, commands in file
                                             are run and process ends after file is processed. The execute option may be used to run a command directly, without opening
                                             the interactive command line. If the command requires an open connection, it must be opened with _l. Quotes may be used to
                                             group words in the command and any dashed arguments use underscore instead. |
|---|---|

| Important | After you make changes to the CORS status, allowed origins list, exposed header, or allowed header, restart Cisco Intelligence
                                             Center Reporting Service for the changes to take effect. All CLIs are node-specific and must be run on all nodes in the cluster. |
|---|---|

| Note | For Unified Intelligence Centre gadgets (Live Data and Historical) to load in Cisco Finesse, ensure to: Enable CORS using the utils cuic cors enable command. Set the Finesse host URL in the utils cuic cors allowed_origin add URLs command. Examples: https://<finesse-FQDN> https://<finesse-FQDN>:port For Live Data gadgets, in addition to the above settings, ensure to enable CORS using the utils live-data cors enable command and set the Finesse host URL in the utils live-data cors allowed_origin add URLs command. For more information, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|

| Note | The member details are available only in the TCP/IP mode. The member details displayed are of the configured members and does
                                       not represent the cluster in real-time. |
|---|---|

| Note | After changing the cluster mode in all the nodes, restart “Intelligence Center Reporting Service ” in all the nodes starting
                                          from the publisher sequentially. |
|---|---|

| Caution | Before executing this command, run the command utils dbreplication stop on all Member nodes and then on the publisher (the Controller node). |
|---|---|

| Caution | Run this command only if the command utils dbreplication reset or utils dbreplication clusterreset fails and replication
                                          		cannot be restarted. |
|---|---|

| Caution | Run this command only when replication setup has
                                          		failed after an install or upgrade. |
|---|---|

| Note | If the platformConfig.xml file contains a new IP address for the publisher, refer to the section Change Cluster IP Address for Publisher Server Defined by IP Address in Chapter 3 and perform Step1 on all subscriber nodes before running this CLI from the publisher node. |
|---|---|

| Note | If the platformConfig.xml file contains a new IP address for the subscriber, refer to the section Change Cluster IP Address for Subscriber Servers Defined by IP Address in Chapter 3 and perform Step 1 to Step 4 on the publisher node before running this CLI from the subscriber nodes. |
|---|---|

| Note | The following warning message, changing this setting will invalidate the software licence is not applicable to Cisco Unified Intelligence Center and can be ignored. |
|---|---|

| Note | You can not stop the NTP service from the command line interface. Use
                                          		  this command when the utils ntp status command returns stopped. |
|---|---|

| Warning | If you log in to the Cisco Unified Intelligence Center application without completing these steps you will lose all administrator
                                          privileges. |
|---|---|

| Note | It is important to shut down using this CLI command. Do not shut down
                                          		by pressing the power button on the server. |
|---|---|

| Note | If either parameters contain white space, then both should be in
                                          		quotation marks. For example, show perf counterhelp "Cisco Phones" "CallsAttempted". |
|---|---|

| Note | Only one of cpu, memory or time may be specified. |
|---|---|

| Note | After the upgrade, the external links in the Unified Intelligence Center dashboard will be disabled. If enabled, the contents from external links are rendered within the HTML iFrame in the dashboard. This will include the frame-src* directive in the Content Security Policy of the Unified Intelligence Center web pages. |
|---|---|

| Note | Enabling the custom widget configuration can lead to injection vulnerabilities. |
|---|---|

| Note | The hostname is case-sensitive. Enter the hostname exactly as entered on the Data Sources interface. |
|---|---|

| Note | You must restart the Unified Intelligence Center Reporting Services
                                          		  for the change to take effect. |
|---|---|

| Note | You must restart the Unified Intelligence Center Reporting Services for the change to take effect |
|---|---|

| Note | Cached scheduled report data - The set cuic properties purge-retention CLI command applies only to this category. |
|---|---|

| Note | You must restart the Unified Intelligence Center Reporting Services for the change to take effect. |
|---|---|

| Caution | These commands are not supported for Unified Intelligence Center. |
|---|---|

| Caution | Only use this command when all other CLI 'set network
                                          		...' commands have failed to restore network connectivity to an Ethernet port.
                                          		This command removes all previous Ethernet and Network Fault Tolerance
                                          		settings. The specified Ethernet port is configured with a minimal static IP
                                          		address configuration. It is imperative that the original Ethernet port
                                          		settings be reconfigured AFTER this command using other CLI 'set network ...'
                                          		commands. |
|---|---|

| Caution | Only use this command when all other CLI 'set network
                                          		...' commands have failed to restore network connectivity to an Ethernet port.
                                          		This command erases all previous Ethernet and Network Fault Tolerance settings.
                                          		The specified Ethernet port is configured with a minimal static IP address
                                          		configuration. It's imperative that the original Ethernet port settings be
                                          		reconfigured AFTER this command using other CLI 'set network ...' commands. |
|---|---|

| Note | When you upgrade the TLS minimum version from TLSv1.0 to TLSv1.1 or TLSv1.2, reinstall the Cisco Unified Real-Time Monitoring
                                                Tool. In a multi-node CUIC deployment, run this CLI command on all the nodes of the cluster starting from the publisher. Restart
                                                all the nodes after executing the CLI command. |
|---|---|

| Note | File commands that include activelog list a livedata directory. For Packaged CCE deployments only, this directory contains logs for the Live Data reporting components. |
|---|---|

| Note | This command is system-intensive. Run it at off-hours. |
|---|---|

| Caution | You cannot recover a deleted file, except possibly by
                                       		using the Disaster Recovery System. |
|---|---|

| Note | If you choose to configure Unified Intelligence Center with Live Data using CLI commands, refer chapter 4 on Live Data Installation in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|