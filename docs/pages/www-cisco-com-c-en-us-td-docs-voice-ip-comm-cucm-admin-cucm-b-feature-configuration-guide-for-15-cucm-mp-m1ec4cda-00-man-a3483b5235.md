---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-mp-m1ec4cda-00-man-a3483b5235
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_mp_m1ec4cda_00_manager-assistant-12-0.html
retrieved_at: 2026-08-16T16:03:21.816309+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Manager Assistant

## Chapter: Manager Assistant

# Manager Assistant

## Cisco Unified
                        	 Communications Manager Assistant Overview

The Unified Communications Manager Assistant feature is a plug-in that an assistant can use to handle calls on behalf of a manager, intercept manager calls,
                              and route them appropriately.

Manager Assistant supports up to 3500 managers and 3500 assistants. To accommodate this number of users, you can configure
                              up to three Manager Assistant applications in one Unified Communications Manager cluster and assign managers and assistants to each instance of the application.

Manager Assistant
                              		  supports shared line support and proxy line support.

### Manager
                              		  Assistant Architecture

The Manager
                              		  Assistant architecture comprises the following:

Cisco IP Manager Assistant service —After you install Unified Communications Manager , activate this service from the Cisco Unified Serviceability interface.

Assistant Console
                                       				  interface —Allows assistants to access the Manager Assistant features on
                                    				their computer to handle calls for managers. The Manager Assistant handles
                                    				calls for an assistant and for as many as 33 managers.

Cisco Unified IP Phone interface: Managers and assistants use softkeys and the Cisco Unified IP Phone Services button to access the Manager Assistant features.

For more information, see chapter Manager Assistant, in Feature Configuration Guide for Cisco Unified Communications Manager .

### Manager
                              		  Assistant Database Access Architecture

The database
                              		  stores all Manager Assistant configuration information. When the manager or
                              		  assistant logs in, the Cisco IP Manager Assistant service retrieves all data
                              		  that is related to the manager or assistant from the database and stores it in
                              		  memory. The database includes two interfaces:

Manager interface —The manager phone makes available the manager features except Manager Configuration. Manager Assistant automatically logs
                                    in a manager in to the Cisco IP Manager Assistant service when the Cisco IP Manager Assistant service starts.

Assistant interface —The assistant accesses the Manager Assistant features by using the Assistant Console application and the Cisco Unified IP Phone . The Assistant Console, an application, provides call-control functions such as answer, divert, transfer, and hold. The assistant
                                    uses the Assistant Console to log in and log out, to set up assistant preferences, and to display the Manager Configuration window that is used to configure manager preferences.

For more information, see chapter Manager Assistant, in Feature Configuration Guide for Cisco Unified Communications Manager .

### Softkeys

Manager
                              		  Assistant  supports the following softkeys:

Redirect

Transfer to VoiceMail

Do Not Disturb

Manager Assistant
                              		  supports the following softkey templates:

Standard
                                    				Manager—Supports manager for proxy mode

Standard
                                    				Shared Mode Manager—Supports manager for shared mode

Standard
                                    				Assistant—Supports assistant in proxy or shared mode

Standard User—The
                                    		  system makes call-processing (such as Hold and Dial) softkeys available with
                                    		  the Standard User template.

### Manager Assistant
                           	 Shared Line Overview

When you configure
                                 		  Manager Assistant in shared line mode, the manager and assistant share a
                                 		  directory number, for example, 8001. The assistant handles calls for a manager
                                 		  on the shared directory number. When a manager receives a call on 8001, both
                                 		  the manager phone and the assistant phone ring.

The Manager
                                 		  Assistant features that do not apply to shared line mode include Default
                                 		  Assistant Selection, Assistant Watch, Call Filtering, and Divert All Calls. An
                                 		  assistant cannot see or access these features on the Assistant Console
                                 		  application.

### Manager Assistant
                           	 Proxy Line Overview

When you configure
                                 		  Manager Assistant in proxy line mode, the assistant handles calls for a manager using a proxy
                                 		  number. The proxy number is not the directory number for the manager, but is an
                                 		  alternate number chosen by the system that an assistant uses to handle manager
                                 		  calls. In proxy line mode, a manager and an assistant have access to all
                                 		  features that are available in Manager Assistant, which include Default
                                 		  Assistant Selection, Assistant Watch, Call Filtering, and Divert All Calls.

## Manager Assistant
                        	 Prerequisites

The user must install JRE on a 32 or 64-bit Windows platform before the user upgrades the Manager Assistant client to a newer
                                    version for Releases 11.5(1)SU9, 12.0(1)SU4, and 14 onwards.

Important

For the Windows 11 platform, the user must install JRE 1.8 on the 64-bit Windows platform before the user upgrades the Manager
                                    Assistant client to a newer version for Release 15SU2 and later.

Manager
                                    				Assistant supports the following browsers and platform:

Unified Communications Manager Assistant Administration and the Assistant Console are supported on Internet Explorer 11 with
                                          Windows 10 and 11 (64 bit), Firefox with Windows 10 and 11 (64 bit) or later, and Safari with MacOS (10.x) or later.

On a computer running Windows 10 and 11 or Apple MAC OS X, you can open one of the browsers specified above.

To display Manager Assistant features in other
                                    				languages, install the locale installer before you configure the Manager
                                    				Assistant.

The Assistant Console application is supported on computers that run Windows 10 and 11 , Windows 2019, and Windows 2022.

You must configure the phones and users, and associated the devices to the users. In
                                    				addition, for shared line appearances between managers and assistants, you must
                                    				configure the same directory number on the manager primary line and
                                    				assistant secondary line.

To add managers and assistants in bulk, install the Cisco Unified Communications Manager Bulk Administration Tool. For more
                                    information, see the Bulk Administration Guide .

## Manager Assistant
                        	 Task Flow for Proxy Lines

### Before you begin

Review Manager Assistant Prerequisites .

Step 1

Run the Cisco Unified CM Assistant Configuration Wizard

Step 2

Configure Manager And Assign Assistant For Proxy Line

Step 3

Configure Assistant Line Appearances for Proxy Line

Step 4

Install Assistant Console Plugin

Step 5

Configure
                                       			 the manager and Assistant Console applications.

### Run the Cisco
                           	 Unified CM Assistant Configuration Wizard

You can run the Cisco Unified CM Assistant Configuration Wizard to automatically create partitions, calling search spaces,
                                 and route points. The wizard also creates Bulk Administration Tool (BAT) templates for the manager phones, the assistant phones,
                                 and all other user phones. You can use the BAT templates to configure the managers, assistants, and all other users. For more
                                 information about BAT, see Bulk Administration Guide for Cisco Unified Communications Manager .

#### Before you begin

Ensure that the configuration wizard runs on the same server (the Unified Communications Manager server) as the Bulk Administration Tool.

Step 1

From Cisco Unified CM Administration, choose Application > Cisco Unified CM Assistant Configuration Wizard .

Step 2

Click Next to begin the Cisco Unified CM Assistant
                                          			 Configuration wizard process.

Step 3

In the Partition for Managers window, enter a name, provide
                                          			 a description, and then click Next . Alternatively, you can accept the default
                                          			 partition name and description.

Step 4

In the Partition for CTI Route Point window, enter a name,
                                          			 provide a description, and then click Next . Alternatively, you can accept the default CTI
                                          			 route point name.

Step 5

In the Partition for All Users window, enter a name, provide
                                          			 a description and then click Next . Alternatively, you can accept the default
                                          			 partition name and description for all users.

Step 6

In the Intercom Partition window, enter a name, provide a
                                          			 description, and then click Next . Alternatively, you can accept the default
                                          			 intercom partition name.

Step 7

In the Assistant Calling Search Space window, enter a name,
                                          			 and provide a description. Alternatively, you can use the default calling
                                          			 search space name and description.

Step 8

Click Next .

Step 9

In the Everyone Calling Search Space window, enter a name,
                                          			 and provide a description. Alternatively, you can accept the default calling
                                          			 search space name and description for everyone.

Step 10

Click Next .

Manager
                                             				Assistant requires that the existing calling search spaces add the prefix Generated_Route Point and Generated_Everyone partitions. The Available Calling Search
                                             				Spaces and Selected Calling Search Spaces boxes automatically list these
                                             				partitions. Use the up and down arrows to move partitions from one box to the
                                             				other.

Step 11

Click Next .

Step 12

In the CTI
                                             				Route Point window, enter a name in the CTI route point name field;
                                          			 otherwise, use the default CTI route point name.

Step 13

From the
                                          			 drop-down list, choose the appropriate device pool.

Step 14

Enter a route
                                          			 point directory number; otherwise, use the default route point directory
                                          			 number.

Step 15

From the
                                          			 drop-down list, choose the appropriate numbering plan and then click Next .

Step 16

In the Phone
                                             				Services window, enter the primary phone service name; otherwise,
                                          			 use the default Phone Service name.

Step 17

From the
                                          			 drop-down list, choose the primary Cisco
                                             				Unified Communications Manager Assistant server or enter a server
                                          			 name or IP address.

Step 18

Enter the
                                          			 secondary phone service name; otherwise, use the default phone service name.

Step 19

From the
                                          			 drop-down list, choose the secondary Cisco
                                             				Unified Communications Manager Assistant server or enter a server
                                          			 name or IP address and then click Next .

Step 20

Click Finish .

Any errors
                                             				that the configuration wizard generates is sent to a trace file. Access this
                                             				file by using the following CLI command: file get activelog tomcat/logs/ccmadmin/log4j

#### What to do next

The Cisco Unified CM Assistant Configuration Wizard only creates the Cisco IP Manager Assistant service parameters. You must
                                 enter the remaining service parameters manually. For service parameter information, see Manager Assistant Service Parameters for Proxy Line .

#### Manager Assistant
                              	 Service Parameters for Proxy Line

From Cisco Unified CM Administration, choose System > Service Parameters . Choose the server on which the Cisco IP Manager Assistant service is active and click ? for detailed descriptions.

Setting

Description

Cisco IP
                                                   						Manager Assistant (Active) Parameters

CTIManager (Primary) IP Address

This
                                                					 parameter specifies the IP address of the primary CTIManager that this Cisco
                                                					 IPMA server uses to process calls.

No default
                                                					 value.

CTIManager (Backup) IP Address

This
                                                					 parameter specifies the IP address of the backup CTIManager that this Cisco
                                                					 IPMA server uses to process calls when primary CTIManager is down.

No default
                                                					 value.

Route
                                                					 Point Device Name for Proxy Mode

This
                                                					 parameter specifies the device name of the CTI route point that this Cisco IPMA
                                                					 server uses to intercept all calls to managers' primary lines for intelligent
                                                					 call routing.

Cisco
                                                					 recommends that you use same CTI route point device for all servers running the
                                                					 IPMA service. You must configure the CTI route point device name if any manager
                                                					 or assistant will be configured to use proxy mode.

CAPF
                                                					 Profile Instance Id for Secure Connection to CTIManager

This
                                                					 service parameter specifies the Instance ID of the Application CAPF Profile for
                                                					 the application user IPMASecureSysUser that this Manager Assistant will
                                                					 use to open a secure connection to CTIManager.

Configure this parameter if CTIManager Connection Security Flag is enabled.

Clusterwide Parameters
                                                   						(Parameters that apply to all servers)

Important

Cisco IPMA
                                                					 Server (Primary) IP Address

This
                                                					 parameter specifies the IP address of the primary Cisco IPMA server.

No default
                                                					 value.

Cisco
                                                					 IPMA Server (Backup) IP Address

This
                                                					 parameter specifies the IP address of the backup Cisco IPMA server. The backup
                                                					 server provides IPMA service when the primary IPMA server fails.

No default
                                                					 value.

Cisco
                                                					 IPMA Server Port

This
                                                					 parameter specifies the TCP/IP port on the Cisco IPMA servers to which the IPMA
                                                					 Assistant Consoles will open socket connections. You may change the parameter
                                                					 if a port conflict exists.

Default
                                                					 value: 2912

Cisco
                                                					 IPMA Assistant Console Heartbeat Interval

This
                                                					 parameter specifies the interval, in seconds, at which the Cisco IPMA server
                                                					 sends keepalive messages (commonly referred to as heartbeat) to the IPMA
                                                					 Assistant Consoles. The IPMA Assistant Consoles initiate failover when they
                                                					 fail to receive heartbeat from the server before the time that is specified in
                                                					 this parameter expires.

Default
                                                					 value: 30 seconds

Cisco
                                                					 IPMA Assistant Console Request Timeout

This
                                                					 parameter specifies the time, in seconds, that the IPMA Assistant Consoles wait
                                                					 to receive a response from the Cisco IPMA server.

Default
                                                					 value: 30 seconds

Cisco
                                                					 IPMA RNA Forward Calls

This
                                                					 parameter determines whether Cisco IPMA Ring No Answer (RNA) forwarding is
                                                					 enabled. Valid values are True (Cisco IPMA forwards unanswered calls to next
                                                					 available assistant) or False (Cisco IPMA does not forward calls).

This parameter works in conjunction with the Cisco IPMA RNA Timeout parameter; calls
                                                					 are forwarded after the time that is specified in the Cisco IPMA RNA Timeout parameter. If a
                                                					 voicemail profile is specified for the line, unanswered calls that cannot be
                                                					 forwarded to an assistant are sent to voicemail when this timer expires.

Default
                                                					 value: False

Alpha
                                                					 Numeric UserID

This
                                                					 parameter determines whether Cisco IPMA Assistant Phone uses an alphanumeric
                                                					 user ID or a numeric user ID.

Default
                                                					 value: True

Cisco IPMA
                                                					 RNA Timeout

This
                                                					 parameter specifies the time, in seconds, that the Cisco IPMA server waits
                                                					 before forwarding an unanswered call to the next available assistant. This
                                                					 parameter works in conjunction with the Cisco IPMA RNA Forward Calls parameter; forwarding
                                                					 occurs only if the Cisco IPMA RNA Forward Calls parameter is set to True .

Default
                                                					 value: 10 seconds

CTIManager Connection Security Flag

This
                                                					 parameter determines whether security for the Cisco IP Manager Assistant
                                                					 service CTIManager connection is enabled. If it is enabled, Cisco IPMA opens a
                                                					 secure connection to CTIManager using the CAPF profile that is configured for
                                                					 the instance ID (as specified in the CAPF Profile Instance ID for Secure Connection to
                                                   						CTIManager service parameter) for the application user IPMASecureSysUser .

Default
                                                					 value: Non Secure

To
                                                					 enable security, you must select an instance ID in the CAPF Profile Instance ID for Secure Connection to
                                                   						CTIManager service parameter.

Redirect
                                                					 call to Manager upon failure to reach Assistant

This
                                                					 parameter determines whether the Cisco Unified IP Manager Assistant application
                                                					 redirects the call back to the intended manager if the call fails to reach the
                                                					 selected proxy assistant.

Default
                                                					 value: False

Advanced Clusterwide
                                                   						parameters

Important

Enable
                                                					 Multiple Active Mode

This
                                                					 parameter determines whether multiple instances of the Cisco IP Manager
                                                					 Assistant service must be run for scalability. If it is enabled, Cisco IPMA can
                                                					 run on the other nodes as configured in the Pool 2 and Pool 3 parameters.

To
                                                					 enable multiple active mode, you must enter the IP addresses of the nodes on
                                                					 which you want to run the additional instances of Cisco IPMA. Configure the
                                                					 Cisco IP Manager Assistant service parameters on those nodes.

Default
                                                					 value: False

Pool 2:
                                                					 Cisco IPMA Server (Primary) IP Address

If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 primary Cisco IPMA server of the second instance of Cisco IPMA.

Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node.

Pool 2:
                                                					 Cisco IPMA Server (Backup) IP Address

If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 backup Cisco IPMA server of the second instance of Cisco IPMA. The backup
                                                					 server provides IPMA service when the primary IPMA server fails.

Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node.

Pool 3:
                                                					 Cisco IPMA Server (Primary) IP Address

If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 primary Cisco IPMA server of the third instance of Cisco IPMA.

Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node.

Pool 3:
                                                					 Cisco IPMA Server (Backup) IP Address

If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 primary Cisco IPMA server of the third instance of Cisco IPMA. The backup
                                                					 server provides IPMA service when the primary IPMA server fails.

Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node.

Clusterwide Parameters
                                                   						(Softkey Templates)

Important

Assistant Softkey Template

This parameter specifies the assistant softkey template that
                                                					 is assigned to assistant devices during Automatic Configuration. The value that
                                                					 is specified in this parameter is used when the Automatic Configuration check box is
                                                					 checked on the Cisco IPMA Assistant Configuration page.

Manager
                                                					 Softkey Template for Proxy Mode

This
                                                					 parameter specifies the manager softkey template for proxy mode that is
                                                					 assigned to manager devices during Automatic Configuration. This parameter
                                                					 applies only for managers that use proxy mode.

Clusterwide Parameters
                                                   						(IPMA Device Configuration Defaults for Proxy Mode)

Manager
                                                					 Partition

This
                                                					 parameter defines the partition that is assigned to manager lines that IPMA
                                                					 handles on manager devices during Automatic Configuration. Make sure the
                                                					 partition you want to use has already been added to Cisco Unified CM
                                                					 Administration. If the Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers that use
                                                					 proxy mode.

All User
                                                					 Partition

This
                                                					 parameter specifies the partition that is configured on all proxy lines and the
                                                					 intercom line on assistant devices, as well as the intercom line on manager
                                                					 devices, during Automatic Configuration. Make sure the partition you want to
                                                					 use has already been added to Cisco Unified CM Administration. If the Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or
                                                					 assistants that use proxy mode.

IPMA
                                                					 Calling Search Space

This
                                                					 parameter specifies the calling search space that is configured for manager
                                                					 lines on manager devices that IPMA handles and the intercom line, as well as
                                                					 the assistant intercom line on assistant devices during Automatic
                                                					 Configuration. Make sure the calling search space you want to use has already
                                                					 been added to Cisco Unified CM Administration. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or
                                                					 assistants that use proxy mode.

Manager
                                                					 Calling Search Space

This
                                                					 parameter defines the manager calling search space that is configured on proxy
                                                					 lines on assistant devices during Automatic Configuration. This calling search
                                                					 space must be a calling search space that already exists in the system. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for assistants that use
                                                					 proxy mode.

Cisco
                                                					 IPMA Primary Phone Service

This
                                                					 parameter defines the IP phone service to which manager/assistant devices will
                                                					 be subscribed during Automatic Configuration. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or assistants
                                                					 that use proxy mode.

Cisco
                                                					 IPMA Secondary Phone Service

This
                                                					 parameter defines the secondary IP phone service to which manager or assistant
                                                					 devices will be subscribed during Automatic Configuration. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or assistants
                                                					 that use proxy mode.

Clusterwide Parameters
                                                   						(Proxy Directory Number Range for Proxy Mode)

Starting
                                                					 Directory Number

This
                                                					 parameter specifies the starting directory number that is used as the starting
                                                					 number for automatic generation of proxy directory numbers during IPMA
                                                					 assistant configuration. After an auto-generated proxy line number is used for
                                                					 an assistant, the next number will be generated for the next assistant, and so
                                                					 on. This parameter applies only for assistants that use proxy mode.

Ending
                                                					 Directory Number

This
                                                					 parameter specifies the ending directory number for automatic generation of
                                                					 proxy directory numbers during IPMA assistant configuration. Configuration will
                                                					 stop at this number. This parameter applies only for assistants that use proxy
                                                					 mode.

Clusterwide Parameters
                                                   						(Proxy Directory Number Range for Proxy Mode)

Number
                                                					 of Characters to be Stripped from Manager DN

This
                                                					 parameter specifies the number of characters to be stripped from the manager
                                                					 directory number (DN) in the process of generating the proxy DN. Generating a
                                                					 proxy DN may involve stripping some number of digits and adding a prefix.
                                                					 Digits are stripped starting from the left. This parameter applies only for
                                                					 assistants that use proxy mode.

Prefix
                                                					 for Manager DN

This
                                                					 parameter specifies the prefix to be added to a manager DN in the process of
                                                					 generating the proxy DN. Generating a proxy DN may involve some stripping of
                                                					 digits and adding a prefix. This parameter applies only for assistants that use
                                                					 proxy mode.

### Configure Manager
                           	 And Assign Assistant For Proxy Line

For information about configuring a new user and associating a device to the user, see Administration Guide for Cisco Unified Communications Manager .

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Click Find .

Step 3

From the Related Links drop-down list, choose Manager Configuration and click Go .

Tip

Step 4

From the Device
                                             				Name/Profile drop-down list, choose the device name or device
                                          			 profile to associate a device name or device profile with a manager. For more
                                          			 information about Extension Mobility with Manager Assistant, see Manager Assistant Interactions .

Step 5

From the Intercom Line drop-down list, choose the intercom
                                          			 line appearance for the manager, if applicable.

Step 6

From the Assistant Pool drop-down list, choose the
                                          			 appropriate pool number (1 to 3).

Step 7

From the Available Lines selection box, choose a line that
                                          			 you want Manager Assistant to control and click the down arrow to make the line
                                          			 display in the Selected Lines selection box. Configure up to five Manager
                                          			 Assistant—controlled lines.

Tip

Step 8

Check the Automatic Configuration check box to automatically
                                          			 configure the softkey template, subscribe to the Manager Assistant phone
                                          			 service, calling search space, and partition for Manager Assistant—Controlled
                                          			 selected lines and intercom line; and Auto Answer with Speakerphone for
                                          			 intercom line for the manager phone based on the Cisco IP Manager Assistant
                                          			 service parameters.

Step 9

Click Save .

### Configure
                           	 Assistant Line Appearances for Proxy Line

A proxy line specifies a phone line that appears on the assistant Cisco Unified IP Phone . Manager Assistant uses proxy lines to manage calls that are intended for a manager. The administrators can manually configure
                                 a line on the assistant phone to serve as the proxy line, or you can enable the Automatic Configuration check box to generate a DN and to add the line to the assistant phone.

Make sure that you configure manager information and assign an assistant to the manager before you configure assistant information
                                                   for an assistant.

If you want to automatically configure proxy line on the assistant phone, configure the service parameters in Proxy Directory Number Range and Proxy Directory Number Prefix sections.

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Click Find .

Step 3

Click on the
                                          			 user name to display user information for the chosen assistant

Step 4

From the Related Links drop-down list, choose Assistant Configuration and click Go .

Step 5

From the Device
                                             				Name drop-down list, choose the device name to associate with the
                                          			 assistant.

Step 6

From the Intercom Line drop-down list, choose the incoming
                                          			 intercom line appearance for the assistant.

Step 7

From the Primary Line drop-down list, choose the primary line
                                          			 for the assistant.

Step 8

To associate
                                          			 the manager line to the assistant line, perform the following steps from the
                                          			 Manager Association to Assistant Line selection box:

From the Available Lines drop-down list, choose the assistant
                                                				  line that will be associated with the manager line.

From the Manager Names drop-down list, choose the
                                                				  preconfigured manager name for whom this proxy line will apply.

From the Manager Lines drop-down list, choose the manager
                                                				  line for which this proxy line will apply.

Step 9

Click Save .

## Manager Assistant
                        	 Task Flow for Shared Lines

### Before you begin

Review Manager Assistant Prerequisites .

Step 1

Configure Partitions for Manager Assistant Shared Line Support

Step 2

Configure Calling Search Spaces for Manager Assistant Shared Line Support

Step 3

Configure Cisco IP Manager Assistant Service Parameters

Step 4

Configure intercom settings.

Step 5

Configure Multiple Manager Assistant Pool

Step 6

Configure Secure TLS Connection to CTI

- Configure IPMASecureSysUser Application User

- Configure CAPF Profile

- Configure Cisco WebDialer Web Service

Follow these procedures if your system is running in mixed mode.

Step 7

Configure CTI Route Point

Step 8

Configure IP Phone Services for Manager and Assistant

Step 9

Configure Phone Button Templates for Manager, Assistant, and Everyone

Step 10

Configure Manager and Assign Assistant for Shared Line Mode

Step 11

Configure Assistant Line Appearances for Shared Line

Step 12

Install Assistant Console Plugin

Step 13

Configure
                                       			 the manager and assistant console applications.

### Configure
                           	 Partitions for Manager Assistant Shared Line Support

You must create
                                 		  three partitions: Generated_Everyone, Generated_Managers, and
                                 		  Generated_Route_Point.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

Click Add
                                             				New to create a new partition.

Step 3

In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan.

Step 4

Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line.

Step 5

To create
                                          			 multiple partitions, use one line for each partition entry.

Step 6

From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition.

Step 7

Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone :

- Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

- Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

Step 8

Click Save .

#### Partition Name Guidelines for Manager Assistant Shared Line Support

The list of partitions in a calling search space is limited to a maximum of 1024 characters. This means that the maximum number
                                    of partitions in a CSS varies depending on the length of the partition names. Use the following table to determine the maximum
                                    number of partitions that you can add to a calling search space if partition names are of fixed length.

Partition
                                                					 Name Length

Maximum
                                                					 Number of Partitions

2 characters

340

3 characters

256

4 characters

204

5 characters

172

...

...

10
                                                					 characters

92

15
                                                					 characters

64

### Configure  Calling
                           	 Search Spaces for Manager Assistant Shared Line Support

A calling
                                 		  search space is an ordered list of route partitions that are typically
                                 		  assigned to devices. Calling search spaces determine the partitions that
                                 		  calling devices can search when they are attempting to complete a call.

You must create
                                 		  two calling search spaces: Generated_CSS_I_E and Generated_CSS_M_E.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

Click Add New .

Step 3

In the Name field, enter a name.

Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_).

Step 4

In the Description field, enter a description.

The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>).

Step 5

From the Available Partitions drop-down list, perform one of
                                          			 the following steps:

- For a single partition,
                                             				select that partition.

- For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions.

Step 6

Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field.

Step 7

(Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box.

Step 8

Click Save .

### Configure Cisco IP
                           	 Manager Assistant Service Parameters

Configure Cisco IP
                                 		  Manager Assistant service parameters if you want to use the Manager Assistant
                                 		  automatic configuration for managers and assistants. You must specify the
                                 		  cluster-wide parameters once for all Cisco IP Manager Assistant services and
                                 		  general parameters for each Cisco IP Manager Assistant service that is
                                 		  installed.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server on which
                                          			 the Cisco IP Manager Assistant service is active.

Step 3

From the Service drop-down list, choose Cisco
                                             				IP Manager Assistant service.

Step 4

Configure the Cisco
                                             				IP Manager Assistant Parameters , Clusterwide Parameters (Parameters that apply to all
                                             				servers) , and Clusterwide Parameters (Softkey Templates) .

click ? for detailed descriptions.

Step 5

Click Save .

### Configure Intercom Settings

Step 1

Configure an Intercom Partition

Step 2

Configure an Intercom Calling Search Space

Step 3

Configure an Intercom Directory Number

Step 4

Configure an Intercom Translation Pattern

#### Configure an
                              	 Intercom Partition

Step 1

From Cisco Unified CM Administration, choose Call Routing > Intercom > Intercom Route Partition .

The Find and List Intercom Partitions window appears.

Step 2

Click Add New .

An Add New Intercom Partition window appears.

Step 3

Under the Intercom Partition Information section, in the Name box, enter the name and description of the
                                             			 intercom partition that you want to add.

To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                            can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                            partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description.

Step 4

Click Save .

Step 5

Locate the
                                             			 partition that you want to configure.

Step 6

Configure the
                                             			 fields in the Intercom Partition Configuration field area. See the online help
                                             			 for more information about the fields and their configuration options.

Step 7

Click Save .

The Intercom Partition
                                                   				  Configuration window appears.

Step 8

Enter the
                                             			 appropriate settings. For detailed information about the Intercom Partition
                                             			 Configuration parameters, see online help.

Step 9

Click Save .

Step 10

Click Apply
                                                				Config .

#### Configure an
                              	 Intercom Calling Search Space

Step 1

In the menu
                                             			 bar, choose Call
                                                   				  Routing > Intercom > Intercom Calling Search
                                                   				  Space .

Step 2

Click the Add New .

Step 3

Configure the fields in the Intercom Calling Search Space field area. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

#### Configure an
                              	 Intercom Directory Number

Step 1

Choose Call
                                                   				  Routing > Intercom > Intercom Directory
                                                   				  Number .

The Find
                                                   				  and List Intercom Directory Numbers window is displayed.

Step 2

To locate a
                                             			 specific intercom directory number, enter search criteria and click Find.

Step 3

Perform one of
                                             			 the followings tasks:

To add an intercom directory number, click Add New .

To update
                                                   				  an intercom directory number, click the intercom directory number to update.

The Intercom Directory Number Configuration window
                                                				displayed.

Step 4

Configure the fields in the Intercom Directory Number Configuration field area. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

Step 6

Click Apply
                                                				Config .

Step 7

Click Reset
                                                				Phone .

Step 8

Restart
                                             			 devices.

During the
                                                				restart, the system may drop calls on gateways.

#### Configure an
                              	 Intercom Translation Pattern

Step 1

Choose Call
                                                   				  Routing > Intercom > Intercom Translation
                                                   				  Pattern .

The Find
                                                   				  and List Intercom Translation Patterns window appears.

Step 2

Perform one of
                                             			 the followings tasks:

To copy an existing intercom translation pattern, locate the partition to configure, click Copy eside the intercom translation pattern to copy.

To add a new intercom translation pattern, click the Add New .

Step 3

Configure the fields in the Intercom Translation Pattern Configuration field area. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

Ensure that
                                                				the intercom translation pattern that uses the selected partition, route
                                                				filter, and numbering plan combination is unique. if you receive an error that
                                                				indicates duplicate entries, check the route pattern or hunt pilot, translation
                                                				pattern, directory number, call park number, call pickup number, or meet-me
                                                				number configuration windows.

The Intercom Translation
                                                   				  Pattern Configuration window displays the newly configured intercom
                                                				translation pattern.

##### What to do next

Refer to the Manager Assistant Task Flow for Shared Lines to determine the next task to complete.

### Configure Multiple
                           	 Manager Assistant Pool

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server on which
                                          			 the Cisco IP Manager Assistant service is active.

Step 3

From the Service drop-down list, choose the Cisco
                                             				IP Manager Assistant service.

Step 4

Click Advanced .

Step 5

Configure the
                                          			 following parameters to add multiple manager assistant pools in Clusterwide Parameters (Parameters that apply to all
                                             				servers) :

Enable Multiple Active
                                                   					 Mode —The default is False. When this parameter is set to True, the
                                                				  administrator can configure up to 7000 managers and assistants by using
                                                				  multiple pools.

Pool 2: Cisco IPMA Server
                                                   					 (Primary) IP Address —No default. The administrator must manually
                                                				  enter this IP address. Administrator can assign up to 2500 managers and
                                                				  assistants to this address.

Pool 2: Cisco IPMA Server
                                                   					 (Backup) IP Address —No default. The administrator must manually
                                                				  enter this IP address.

Pool 3: Cisco IPMA Server
                                                   					 (Primary) IP Address —No default. The administrator must manually
                                                				  enter this IP address and can assign up to 2500 managers and assistants to this
                                                				  address.

Pool 3: Cisco IPMA Server
                                                   					 (Backup) IP Address —No default. The administrator must manually
                                                				  enter this IP address.

Step 6

Click Save .

#### What to do next

Refer to the Manager Assistant Task Flow for Shared Lines to determine the next task to complete.

### Configure Secure
                           	 TLS Connection to CTI for Manager Assistant

Manager Assistant uses WDSecureSysUser application user credentials to establish a secure TLS connection to CTI to make calls.

To configure the WDSecureSysUser application user to establish a secure TLS connection, complete the following tasks.

#### Before you begin

Install and configure the Cisco CTL Client.

For more information about CTL Client, see Security Guide for Cisco Unified Communications Manager .

Verify that the Cluster Security Mode in the Enterprise Parameters Configuration window is 1 (mixed mode). Operating the system in mixed mode impacts other security functions in your system. If your system is not currently
                                       running in mixed mode, do not switch to mixed mode until you understand these interactions. For more information, see Security Guide for Cisco Unified Communications Manager .

Verify that the Cluster SIPOAuth Mode field in the Enterprise Parameters Configuration window is set to Enabled .

Activate the Cisco Certificate Authority Proxy Function (CAPF) service on the first node.

Step 1

Configure IPMASecureSysUser Application User

Step 2

Configure CAPF Profile

Configure Certificate Authority Proxy Function (CAPF) Profile for the IPMASecureSysUser Application User.

Step 3

Configure Cisco WebDialer Web Service

Configure service parameters for the Cisco IP Manager Assistant service.

#### Configure
                              	 IPMASecureSysUser Application User

Use this procedure
                                    		  to configure IPMASecureSysUser application user.

Step 1

From Cisco Unified CM Administration, choose User Management > Application User .

Step 2

Click Find .

Step 3

From the Find
                                                				and List Application Users Application window, choose WDSecureSysUser .

Step 4

Configure the
                                             			 fields in the Application User Configuration window and click Save .

#### Configure CAPF Profile

Certificate
                                    		  Authority Proxy Function (CAPF) is a component that performs tasks to issue and
                                    		  authenticate security certificates. When you create an application user CAPF
                                    		  profile, the profile uses the configuration details to open secure connections
                                    		  for the application.

Step 1

From Cisco Unified CM Administration, choose User Management > Application User CAPF Profile .

Step 2

Perform one of
                                             			 the following tasks:

- Click Add New in the Find window, to add a new CAPF profile.

- Click Copy for that record in the Copy column, to copy an existing profile, and locate the appropriate profile.

Step 3

Configure or
                                             			 update the relevant CAPF profile fields. See the Related Topics section
                                             			 information about the fields and their configuration options.

Step 4

Click Save .

Step 5

Repeat the
                                             			 procedure for each application and end user that you want to use security.

##### CAPF Profile
                                 	 Settings

Setting

Description

Application User

From the drop-down list, choose the application user for the
                                                   						CAPF operation. This setting displays configured application users.

This setting does not appear in the End User CAPF Profile window.

End User ID

From the drop-down list, choose the end user for the CAPF
                                                   						operation. This setting displays configured end users.

This setting does not appear in the Application User CAPF Profile window.

Instance ID

Enter 1 to 128 alphanumeric characters (a-z, A-Z, 0-9). The
                                                   						Instance ID identifies the user for the certificate operation.

You can configure multiple connections (instances) of an
                                                   						application. To secure the connection between the application and CTIManager,
                                                   						ensure that each instance that runs on the application PC (for end users) or
                                                   						server (for application users) has a unique certificate.

This field relates to the CAPF Profile Instance ID for Secure
                                                   						Connection to CTIManager service parameter that supports web services and
                                                   						applications.

Certificate Operation

From the drop-down list, choose one of the following options:

No Pending Operation —This message is displayed when no certificate operation is occurring. (default setting)

Install/Upgrade —This option installs a new certificate or upgrades an existing locally significant certificate for the application.

Authentication Mode

The authentication mode for the Install/Upgrade certificate
                                                   						operation specifies By Authentication String, which means CAPF installs,
                                                   						upgrades, or troubleshoots a locally significant certificate only when the user
                                                   						or administrator enters the CAPF authentication string in the JTAPI/TSP Preferences window.

Authentication String

To create your own authentication string, enter a unique string.

Each string must contain 4 to 10 digits.

To install or upgrade a locally significant certificate, the
                                                   						administrator must enter the authentication string in the JTAPI/TSP preferences
                                                   						GUI on the applicationPC. This string supports one-time use only; after you
                                                   						use the string for the instance, you cannot use it again.

Generate String

To automatically generate an authentication string, click this
                                                   						button. The 4- to10-digit authentication string appears in the Authentication String field.

Key Size (bits)

From the drop-down list, choose the key size for the
                                                   						certificate. The default setting is 1024. The other option for key size is 512.

Key generation, which is set at low priority, allows the
                                                   						application to function while the action occurs. Key generation may take up to
                                                   						30 or more minutes.

Operation Completes by

This field, which supports all certificate operations, specifies
                                                   						the date and time by which you must complete the operation.

The values that are displayed apply for the first node.

Use this setting with the CAPF Operation Expires in (days) enterprise parameter, which specifies the default number of days in which the
                                                   						certificate operation must be completed. You can update this parameter at any
                                                   						time.

Certificate Operation Status

This field displays the progress of the certificate operation,
                                                   						such as pending, failed, or successful.

You cannot change the information that is displayed in this
                                                   						field.

#### Configure Cisco WebDialer
                                 		Web Service

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server on which
                                             			 the Cisco WebDialer Web service is active.

Step 3

From the Service drop-down list, choose the Cisco WebDialer Web service.

Step 4

Navigate to
                                             			 and update the CTIManager Connection Security Flag and CAPF Profile Instance ID
                                             			 for Secure Connection to CTIManager parameters.

To view
                                                				parameter descriptions, click the parameter name link.

CTIManager
                                                            				  supports IPv4 and IPv6 addresses.

Step 5

Click Save .

Step 6

Repeat the
                                             			 procedure on each server on which the service is active.

##### What to do next

Refer to the Manager Assistant Task Flow for Shared Lines to determine the next task to complete.

### Configure CTI
                           	 Route Point

Step 1

From Cisco Unified CM Administration, choose Device > CTI Route Point .

Step 2

Click Add
                                             				New .

Step 3

In the Device
                                             				Name field, enter the device name.

Step 4

From the Device
                                             				Pool drop-down list, choose Default .

Step 5

From the Calling Search Space drop-down list, choose Generated_CSS_M_E .

Step 6

Check the Use
                                             				Device Pool Calling Party Transformation CSS check box.

Step 7

Click Save .

Step 8

From the
                                          			 Association area, click Line
                                             				[1] - Add a new DN .

Step 9

Enter a
                                          			 directory number in the Directory Number field.

Step 10

From the Route
                                             				Partition drop-down list, choose Generated_Route_Point .

Step 11

Click Save .

### Configure IP Phone
                           	 Services for Manager and Assistant

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Services .

Step 2

Click Add
                                             				New .

Step 3

For each supported phone for managers and assistants, enter the required fields and click Save . See Cisco IP Phone Services Configuration Fields for more information about the fields and their configuration options.

#### Cisco IP Phone
                              	 Services Configuration Fields

Field

Description

Service Information

Service
                                                						Name

Enter
                                                						the name of the service. If the service is not marked as an enterprise
                                                						subscription, the service name will display in areas where you can subscribe to
                                                						a service, for example, under Cisco Unified Communications Self Care Portal.

Enter up
                                                						to 128 characters for the service name.

For Java
                                                						MIDlet services, the service name must exactly match the name that is defined
                                                						in the Java Application Descriptor (JAD) file.

ASCII
                                                						Service Name

Enter
                                                						the name of the service to display if the phone cannot display Unicode.

Service
                                                						Description

Enter a
                                                						description of the content that the service provides. The description can
                                                						include up to 50 characters in any language, but it cannot include double
                                                						quotation marks (") or single quotation marks (').

Service
                                                						URL

Enter the URL of the server where the IP phone services application is located. Make sure that this server remains independent
                                                of the servers in your Unified Communications Manager cluster. Do not specify a Unified Communications Manager server or any server that is associated with Unified Communications Manager (such as a TFTP server or directory database publisher server).

For the services to be available, the phones in the Unified Communications Manager cluster must have network connectivity to the server.

For
                                                						Cisco-signed Java MIDlets, enter the location where the JAD file can be
                                                						downloaded; for example, a web server or the back-end application server to
                                                						which the Java MIDlet communicates.

For
                                                						Cisco-provided default services, the service URL is displayed as Application:Cisco/<name of service> by
                                                						default; for example, Application:Cisco/CorporateDirectory . If you
                                                						modify the service URL for Cisco-provided default services, verify that you
                                                						configured both for the Service Provisioning setting, which displays in the Phone , Enterprise Parameter , and Common Phone Profile Configuration windows. For
                                                						example, you use a custom corporate directory, so you change Application:Cisco/CorporateDirectory to the
                                                						external service URL for your custom directory; in this case, change the Service Provisioning value  to Both .

Secure-Service URL

Enter the secure URL of the server where the Cisco Unified IP Phone services application is located. Make sure that this server remains independent of the servers in your Unified Communications Manager cluster. Do not specify a Unified Communications Manager server or any server that is associated with Unified Communications Manager (such as a TFTP server or publisher database server).

For the services to be available, the phones in the Unified Communications Manager cluster must have network connectivity to the server.

Service
                                                						Category

Choose a
                                                						service application type (XML or Java MIDlet).

If you
                                                						choose Java MIDlet, when the phone receives the updated configuration file, the
                                                						phone retrieves the Cisco-signed MIDlet application (JAD and JAR) from the
                                                						specified Service URL and installs the application.

Service
                                                						Type

Choose
                                                						whether the service is provisioned to the Services, Directories, or Messages
                                                						button or option on the phone; that is, if the phone has these buttons or
                                                						options. To determine whether your phone supports these buttons or options, see
                                                						the Cisco Unified IP Phone Administration Guide that supports
                                                						your phone model.

Service
                                                						Vendor

Allows you to specify the vendor or manufacturer for the service. This field is optional for XML applications, but it is required
                                                for Cisco-signed Java MIDlets.

For
                                                						Cisco-signed Java MIDlets, the value that you enter in this field must exactly
                                                						match the vendor that is defined in the MIDlet JAD file.

This
                                                						field displays as blank for Cisco-provided default services.

You can
                                                						enter up to 64 characters.

Service
                                                						Version

Enter
                                                						the version number for the application.

For XML
                                                						applications, this field is optional and is informational only. For
                                                						Cisco-signed Java MIDlets, consider the following information:

If
                                                      							 you enter a version, the service version must exactly match the version that is
                                                      							 defined in the JAD file. If you enter a version, the phone attempts to upgrade
                                                      							 or downgrade the MIDlet if the version is different than what is installed on
                                                      							 the phone.

If the field is blank, the version gets retrieved from the Service URL . Leaving the field blank ensures that the phone attempts to download the JAD file every time that the phone reregisters to Unified Communications Manager as well as every time that the Cisco-signed Java MIDlet is launched; this ensures that the phone always runs the latest version
                                                      of the Cisco-signed Java MIDlet without you having to manually update the Service Version field.

This
                                                						field displays as blank for Cisco-provided default services.

You can
                                                						enter numbers and periods in this field (up to 16 ASCII characters).

Enable

Allows you to enable or disable the service without removing the configuration from Cisco Unified CM Administration (and without removing the service from the database).

Uncheck
                                                						the check box to remove the service from the phone configuration file and the
                                                						phone.

Service Parameter
                                                   						  Information

Parameters

Lists the service parameters that apply to this IP phone service. Use the following buttons to configure service parameters
                                                for this pane:

New
                                                         							 Parameter —Click this button to display the Configure Cisco Unified
                                                         								IP Phone Service Parameter window, where you configure a new service
                                                      							 parameter for this IP phone service.

Edit
                                                         							 Parameter —Highlight a service parameter that is displayed in the Parameters pane, then click this button to display
                                                      							 the Configure Cisco Unified
                                                         								IP Phone Service Parameter window, where you can edit the selected
                                                      							 service parameter for this IP phone service.

Delete Parameter —Highlight a service parameter that is displayed
                                                      							 in the Parameters pane, then click this button to delete a
                                                      							 service parameter for this IP phone service. A popup window asks you to confirm
                                                      							 deletion.

### Configure Phone
                           	 Button Templates for Manager, Assistant, and Everyone

The procedures in this section describe how to configure phone  button for manager and assistant.

Step 1

Configure a Phone Button Template for Manager Assistant

Perform this step to assign manage and assistant button features to line or speed dial keys.

Step 2

Associate a Manager Assistant Button Template with a Phone

Perform this step to configure the manager and assistant button for a phone.

#### Configure a Phone
                              	 Button Template for Manager Assistant

Use this procedure
                                    		  to configure a phone button template for the Manager Assistant feature.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template .

Step 2

Click Find to display list of supported phone templates.

Step 3

Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step.

Select a default template for the model of phone and click Copy .

In the Phone Button Template Information field, enter a new name for the template.

Click Save .

Step 4

Perform the following steps if you want to add phone buttons to an existing template.

Click Find and enter the search criteria.

Choose an existing template.

Step 5

From the Line drop-down list, choose 
                                             			 feature that you want  to add to the template.

Step 6

Click Save .

Step 7

Perform one
                                             			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them.

#### Associate a
                              	 Manager Assistant Button Template with a Phone

##### Before you begin

Configure a Phone Button Template for Manager Assistant

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find to display the list of configured phones.

Step 3

Choose the
                                             			 phone to which you want to add the phone button template.

Step 4

In the Phone
                                                				Button Template drop-down list, choose the phone button template
                                             			 that contains the new feature button.

Step 5

Click Save .

### Configure Manager
                           	 and Assign Assistant for Shared Line Mode

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Click Find .

Step 3

From the Related Links drop-down list, choose Manager Configuration and click Go .

Step 4

Check the Automatic Configuration check box to automatically
                                          			 configure the softkey template and Auto Answer with Speakerphone for intercom
                                          			 line for the manager phone based on the Cisco IP Manager Assistant service
                                          			 parameters.

Step 5

Check Uses
                                             				Shared Lines check box.

Step 6

From the Device
                                             				Name/Profile drop-down list, choose the device name or device
                                          			 profile to associate a device name or device profile with a manager.

See the
                                             				related topics for more information about Extension Mobility with Manager
                                             				Assistant.

Step 7

From the Intercom Line drop-down list, choose the intercom
                                          			 line appearance for the manager, if applicable.

Step 8

From the Assistant Pool drop-down list, choose the
                                          			 appropriate pool number (1 to 3).

Step 9

Choose the
                                          			 name of the assistant from the Available Assistants selection box and move it
                                          			 to the Associated Assistants selection box by clicking the down arrow to assign
                                          			 an assistant to the manager.

Step 10

Choose the
                                          			 appropriate line from the Available Lines list box and move it to the Selected
                                          			 Lines list box by clicking the down arrow to configure the Manager Assistant
                                          			 controlled lines.

Step 11

Click Save .

### Configure
                           	 Assistant Line Appearances for Shared Line

Administrators can set up one or more lines with a shared line appearance. The Unified Communications Manager system considers a directory number to be a shared line if it appears on more than one device in the same partition.

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Click Find .

Step 3

Click on the
                                          			 username to display user information for the chosen assistant.

Step 4

From the Related Links drop-down list, choose Assistant Configuration and click Go .

Step 5

From the Device Name drop-down list, choose the device name
                                          			 to associate with the assistant.

Step 6

From the Intercom Line drop-down list, choose the incoming
                                          			 intercom line appearance for the assistant.

Step 7

From the Primary Line drop-down list, choose the primary line
                                          			 for the assistant.

To view
                                                				  existing manager configuration information, highlight the manager name in the Associated Managers list and click View Details .

To
                                                				  return to the Assistant Configuration window, highlight the
                                                				  assistant name and click View Details link in the Manager Configuration window.

Step 8

To associate
                                          			 the manager line to the assistant line, perform the following steps from the
                                          			 Manager Association to Assistant Line selection box:

From the Available Lines drop-down list, choose the assistant
                                                				  line that will be associated with the manager line.

From the Manager Names drop-down list, choose the
                                                				  preconfigured manager name for whom this proxy line will apply.

From the Manager Lines drop-down list, choose the manager
                                                				  line for which this proxy line will apply.

Step 9

Click Save .

### Install Assistant
                           	 Console Plugin

Step 1

From Cisco Unified CM Administration, choose Application > Plugins .

Step 2

Click Find .

Step 3

Click on the Download link for Cisco Unified CM Assistant Console
                                          			 and save the executable to a location.

Step 4

Run the
                                          			 executable file.

Step 5

In the Introduction window, click Next .

Step 6

In the License
                                             				Agreement window, click Next .

Step 7

Choose a
                                          			 location where you want the application to install and click Next .

Step 8

In the Pre-installation Summary window, review the summary
                                          			 and click Install .

Step 9

After the
                                          			 installation is complete, click Finish .

Step 10

Provide the
                                          			 assistant the username and password that is required to log in to the console.

Step 11

To launch the
                                          			 Assistant Console, click the desktop icon or choose Cisco Unified
                                                				  Communications Manager Assistant > Assistant Console from the Start...Programs menu.

Step 12

The Advanced tab in the Cisco
                                             				Unified Communications Manager Assistant Settings window allows you
                                          			 to enable trace for the Assistant Console.

Step 13

Provide the assistant with the port number and the IP address or hostname of the Unified Communications Manager server on which the Cisco IP Manager Assistant service is active. The first time that the assistant logs in to the console,
                                          the assistant must enter the information in the Cisco Unified Communications Manager Assistant Server Port and the Cisco Unified Communications Manager Assistant Server Hostname or IP Address fields.

## Manager Assistant
                        	 Interactions

Feature

Interaction

Bulk
                                          						Administration Tool

You can
                                          						use the Bulk Administration Tool to add many users (managers and assistants) at
                                          						once instead of adding users individually.

The Bulk Administration Tool templates that the Cisco Unified CM Assistant Configuration Wizard creates for Cisco Unified IP Phones support only the Unified Communications Manager intercom lines.

For more information, see the Bulk Administration Guide for Cisco Unified Communications Manager .

Calling
                                          						Party Normalization

Manager
                                          						Assistant automatically supports localized and globalized calls if you
                                          						configure the Calling Party Normalization feature. Manager Assistant can
                                          						display localized calling party numbers on the user interfaces. In addition,
                                          						for an incoming call to the manager, Manager Assistant can display localized
                                          						and globalized calling party numbers when filter pattern matching occurs.

Extension Mobility

You can
                                          						simultaneously use Manager Assistant with the Cisco Extension Mobility feature.
                                          						When you log in to the Cisco Unified IP Phone using Extension Mobility, the
                                          						Cisco IP Manager Assistant service is automatically enabled on that phone. You
                                          						can then access the Manager Assistant features.

For
                                          						more information about Cisco Extension Mobility, see Extension Mobility Overview .

Internet
                                          						Protocol Version 6 (IPv6)

Manager
                                          						Assistant does not support IPv6, so you cannot use phones with an IP Addressing
                                          						Mode of IPv6 Only with Manager Assistant. To use Manager Assistant with the
                                          						phone, ensure that you configure the phone with an IP Addressing Mode of IPv4
                                          						Only or IPv4 and IPv6.

Reporting tools

Manager Assistant provides statistical information in the CDR
                                          						Analysis and Reporting (CAR) tool and provides a summary of changes to
                                          						configurations in a change log.

The
                                          						administrator can view a summary of changes that are made to the Manager or
                                          						Assistant Configurations in Unified CM AssistantChangeLog*.txt. A manager can
                                          						change defaults by accessing the Manager Configuration from a URL. An assistant
                                          						can change the manager defaults from the Assistant Console. For information
                                          						about the URL and Manager Configuration, see the Cisco Unified Communications Manager Assistant User
                                             						  Guide .

When
                                          						the manager or assistant makes changes, the changes are sent to a log file
                                          						called ipma_changeLogxxx.log . The log file resides on the server
                                          						that runs the Cisco IP Manager Assistant service. Use the following command to
                                          						obtain the log file: file get activelog
                                             						  tomcat/logs/ipma/log4j/

For
                                          						more information about downloading the log file, see the Cisco Unified Real -Time Monitoring Tool Administration
                                             						  Guide .

CDR
                                          						Analysis and Reporting

Manager Assistant supports call-completion statistics and inventory reporting for managers and assistants. The CAR tool supports
                                          call-completion statistics. Cisco Unified Serviceability supports inventory reporting.

For
                                          						more information, see the following guides:

Cisco Unified
                                                   								Serviceability Administration Guide

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager

Multilevel Precedence and Preemption (MLPP)

The
                                          						following points describe the interactions between Manager Assistant with
                                          						shared line support and MLPP:

The
                                                							 system preserves call precedence in the handling of calls by Manager Assistant.
                                                							 For example, when an assistant diverts a call, the system preserves the
                                                							 precedence of the call.

Filtering of precedence calls occurs in the same manner as all
                                                							 other calls. The precedence of a call will not affect whether a call is
                                                							 filtered.

Because Manager Assistant does not have information about the
                                                							 precedence of a call, it does not provide any additional indication of the
                                                							 precedence of a call on the Assistant Console.

Intercom

Manager
                                          						Assistant supports the following two types of intercom:

Manager Assistant intercom (used with Cisco Unified IP Phones
                                                							 7940 and 7960). You can configure this intercom feature using the DN
                                                							 configuration and end user (manager and assistant) configuration windows.

Unified Communications Manager intercom (used with Cisco Unified IP Phones 7940 and 7960). You can configure this intercom feature using the intercom partition,
                                                intercom calling search space, intercom directory number, intercom translation pattern, DN, and end user (manager and assistant)
                                                configuration windows.

Message Waiting Indicator

The
                                          						Message Waiting Indicator feature interacts with proxy line support only.

The
                                          						Message Waiting Indicator (MWI) on and off numbers should have the partition of
                                          						the manager line in their calling search space. The partition can exist in any
                                          						order of priority within each calling search space.

Time-of-Day Routing

The
                                          						Time-of-Day feature interacts with proxy line support only.

Time-of-Day routing routes calls to different locations based on
                                          						the time that the call gets made; for example, during business hours, calls get
                                          						routed to a manager office, and after hours, the calls go directly to voicemail
                                          						service.

For more information about Time-of-Day Routing, see the System Configuration Guide for Cisco Unified Communications Manager .

## Manager Assistant
                        	 Restrictions

Feature

Restriction

Assistant
                                       					 Console Application

To install
                                       					 the Assistant Console application on a computer with Microsoft Internet
                                       					 Explorer 7 (or later), install the Microsoft Java Virtual Machine (JVM) before
                                       					 the Assistant Console installation.

Call
                                       					 Management features

The
                                       					 Assistant Console does not support hunt groups or queues, recording and
                                       					 monitoring, one-touch Call Pickup, and On-Hook transfer (the ability to
                                       					 transfer a call by pressing the Transfer softkey and going on hook to complete
                                       					 the transfer).

Cisco IP
                                       					 Phones

Manager
                                       					 Assistant supports SIP on Cisco Unified IP Phones 7900 Series, except for Cisco
                                       					 Unified IP Phones 7940 and 7960.

Manager
                                       					 Assistant supports up to 3500 managers and 3500 assistants by configuring
                                       					 multiple Cisco IP Manager Assistant servers (pools). When you enable multiple
                                       					 pools, the manager and all configured assistants for that manager should belong
                                       					 to the same pool.

Cisco Unified IP Phones 7960 and 7940 support only the Unified Communications Manager Assistant Intercom lines feature. Cisco Unified IP Phones 7900 (except 7940 and 7960) support only the Unified Communications Manager Intercom feature.

One manager can have up to ten assigned assistants and one assistant can support up to 33 managers (if each manager has one Unified Communications Manager –controlled line).

Only one assistant at a time can assist a manager.

Manager Assistant supports up to 3500 managers and 3500 assistants per Unified Communications Manager cluster.

Intercom

After an upgrade, Manager Assistant users that use the incoming intercom line do not get upgraded automatically to the Unified Communications Manager Intercom feature.

The system does not support calls between the Unified Communications Manager Intercom feature and regular lines (which may be configured as Manager Assistant Intercom lines).

Single
                                       					 Sign-On

Manager
                                       					 Assistant is not supported in the Single Sign-On environment.

Speed
                                       					 Dial

Cisco
                                       					 Unified IP Phones 7940, 7942, and 7945 support only two lines or speed-dial
                                       					 buttons.

## Cisco Unified
                        	 Communications Manager Assistant Troubleshooting

This section
                              		  describes the troubleshooting tools for Manager Assistant and the client
                              		  desktop, and troubleshooting information for Manager Assistant.

Tool
                                          						Description

Location

Cisco
                                          						Unified CM Assistant server trace files

The
                                          						trace files reside on the server that runs the Cisco IP Manager Assistant
                                          						service.

You can
                                          						download these files from the server using one of the following methods:

Use
                                                							 the CLI command file get activelog tomcat/logs/ipma/log4j .

Use
                                                							 the trace collection features in the Cisco Unified Real-Time Monitoring Tool
                                                							 (RTMT). For more information, see the Cisco Unified Real-Time Monitoring Tool Administration
                                                   								Guide .

You can
                                          						enable debug tracing by choosing Cisco Unified
                                                							 Serviceability > Trace > Configuration .

Cisco
                                          						IPMA client trace files

$INSTALL_DIR\logs\ACLog*.txt on the client desktop, in the
                                          						same location where the Unified CM Assistant assistant console resides.

To
                                          						enable debug tracing, go to the Settings dialog box in the Assistant Console. In the Advanced panel, check the Enable Trace check box.

Cisco
                                          						IPMA client install trace files

$INSTALL_DIR\InstallLog.txt on the client desktop, in the
                                          						same location where the Assistant Console resides.

Cisco
                                          						IPMA Client AutoUpdater trace files

$INSTALL_DIR\UpdatedLog.txt on the client desktop, in the
                                          						same location where the Unified CM Assistant Console resides.

Install
                                          						directory

By
                                          						default— C:\Program Files\Cisco\Unified Communications Manager Assistant
                                             						  Console\

### Calling Party Gets
                           	 Reorder Tone

#### Problem

Calling party gets
                                 		  a reorder tone or a message:

#### Possible
                                 		  Cause

The calling search
                                 		  space of the calling line may not be configured correctly.

#### Solution

Check the calling search space of the line. For more information about configuration, see the System Configuration Guide for Cisco Unified Communications Manager .

You can also use
                                 		  the Cisco Dialed Number Analyzer service to check for flaws in the calling
                                 		  search space. For more information, see the Cisco Unified
                                    			 Communications Manager Dialed Number Analyzer Guide .

### Calls Do Not Get
                           	 Routed When Filtering Is On or Off

#### Problem

Calls are not
                                 		  routed properly.

#### Possible Cause
                                 		  1

Cisco CTI Manager
                                 		  service may have stopped.

#### Solution
                                 		  1

Restart the Cisco
                                 		  CTI Manager and Cisco IP Manager Assistant services from Cisco Unified
                                       				Serviceability > Tools > Control Center—Feature Services .

#### Possible Cause
                                 		  2

The Unified Communications Manager Assistant route point was not configured properly.

#### Solution
                                 		  2

Use wildcards to match the directory number of the Unified Communications Manager Assistant CTI route point and the primary directory numbers of all managers that are configured for Unified Communications Manager Assistant.

#### Possible Cause
                                 		  3

The status window on the manager phone displays the message Filtering Down . This message can indicate that Unified Communications Manager Assistant CTI route point may be deleted or may not be in service.

#### Solution
                                 		  3

Use the following
                                 		  procedure to configure the CTI route point and restart the Cisco IP Manager
                                 		  Assistant service:

From Cisco
                                       				Unified CM Administration, choose Device > CTI Route
                                             					 Point .

Find the route point, or add a new route point. For more information about configuration, see the System Configuration Guide for Cisco Unified Communications Manager .

Restart the
                                       				Cisco CTI Manager and Cisco IP Manager Assistant services from Cisco Unified
                                             					 Serviceability > Tools > Control Center—Feature Services .

### Cisco IP Manager
                           	 Assistant Service Unreachable

#### Problem

After you open the
                                 		  Assistant Console, the following message is displayed:

#### Possible Cause
                                 		  1

Cisco IP Manager
                                 		  Assistant service may have stopped.

#### Solution
                                 		  1

Restart the Unified Communications Manager Assistant from Cisco Unified Serviceability > Tools > Control Center—Feature Services .

#### Possible Cause
                                 		  2

The server address for the primary and secondary Unified Communications Manager Assistant servers may be configured as DNS names, but the DNS names are not configured in the DNS server.

#### Solution
                                 		  2

Use the following
                                 		  procedure to replace the DNS name.

From Cisco Unified CM Administration, choose System > Server .

Replace the
                                       				DNS name of the server with the corresponding IP address.

Restart the Unified Communications Manager Assistant from Cisco Unified Serviceability > Tools > Control Center—Feature Services .

#### Possible Cause
                                 		  3

The Cisco CTI
                                 		  Manager service may have stopped.

#### Solution
                                 		  3

Restart the Unified Communications Manager Assistant from Cisco Unified Serviceability > Tools > Control Center—Feature Services .

#### Possible Cause 4

The Unified Communications Manager Assistant service might be configured to open a CTI connection in secure mode, but the security configuration may not be
                                 complete.

If this scenario occurs, the following message is displayed in the alarm viewer or in the Unified Communications Manager Assistant service logs:

#### Solution
                                 		  4

Check the security
                                 		  configuration in the service parameters of Cisco IP Manager Assistant service.

Restart the Unified Communications Manager Assistant from Cisco Unified Serviceability > Tools > Control Center—Feature Services .

### Cannot Initialize
                           	 Cisco IP Manager Assistant Service

#### Problem

The Cisco IP
                                 		  Manager Assistant service cannot open a connection to CTI Manager, and the
                                 		  following message is displayed:

#### Possible
                                 		  Cause

The Cisco IP
                                 		  Manager Assistant service cannot open a connection to CTIManager. You can see
                                 		  the message in the alarm viewer or in the Unified CM Assistant service logs.

#### Solution

Restart the Cisco
                                 		  CTI Manager and Cisco IP Manager Assistant services from Cisco Unified
                                       				Serviceability > Tools > Control Center—Feature Services .

### Assistant Console
                           	 Installation from Web Fails

#### Problem

Assistant Console
                                 		  installation from the web fails. The following message is displayed:

#### Possible
                                 		  Cause

Using the Sun Java plug-in virtual machine instead of the Microsoft JVM with the standard Unified Communications Manager Assistant Console install causes failures.

#### Solution

The administrator
                                 		  directs the user to the following URL, which is a JSP page that supports the
                                 		  Sun Java plug-in:

### HTTP Status
                           	 503—This Application Is Not Currently Available

#### Problem

http://<server-name>:8443/ma/Install/IPMAConsoleInstall.jsp displays the following error message:

#### Possible
                                 		  Cause

Cisco IP Manager
                                 		  Assistant service has not been activated or is not running.

#### Solution

Ensure that the
                                 		  Cisco IP Manager Assistant service has been activated by checking the
                                 		  activation status of the service from Cisco Unified
                                       				Serviceability > Tools > Service Activation .

If the Cisco IP Manager Assistant service has already been activated, restart the Unified Communications Manager Assistant from Cisco Unified Serviceability > Tools > Control Center—Feature Services .

### Manager Is Logged
                           	 Out While the Service Is Still Running

#### Problem

Although the manager is logged out of Unified Communications Manager Assistant, the service still runs. The display on the manager IP phone disappears. Calls do not get routed, although filtering
                                 is On. To verify that the manager is logged out, view the application log using the Cisco Unified Real-Time Monitoring Tool.
                                 Look for a warning from the Cisco Java Applications that indicates that the Cisco IP Manager Assistant service logged out.

#### Possible
                                 		  Cause

The manager
                                 		  pressed the softkeys more than four times per second (maximum limit allowed).

#### Solution

The Unified Communications Manager administrator must update the manager configuration. Perform the following procedure to correct the problem:

From Cisco Unified CM Administration, choose User Management > End User .

The Find
                                          				  and List Users window is displayed.

Enter the
                                       				manager name in the search field and click Find .

From the
                                       				search results list, choose the manager that you want to update.

The End
                                          				  User Configuration window is displayed.

From the Related Links drop-down list, choose Cisco IPMA Manager and click Go .

Make the
                                       				necessary changes to the manager configuration and click Update .

### Manager Cannot
                           	 Intercept Calls That Are Ringing on the Assistant Proxy Line

#### Problem

The manager cannot
                                 		  intercept the calls that are ringing on the assistant proxy line.

#### Possible
                                 		  Cause

The calling search
                                 		  space of the proxy line is not configured properly.

#### Solution

Check the calling
                                 		  search space of the proxy line for the assistant phone. Perform the following
                                 		  procedure to correct the problem:

From Cisco Unified CM Administration, choose Device > Phone .

The Find
                                          				  and List Phones search window is displayed.

Click the
                                       				assistant phone.

The Phone
                                          				  Configuration window is displayed.

Verify the
                                       				calling search space configuration for the phone and for the directory number
                                       				(line) and update as appropriate.

### No Page Found
                           	 Error

#### Problem

http://<server-name>:8443/ma/Install/IPMAConsoleInstall.jsp displays the following error message:

#### Possible Cause
                                 		  1

Network problems.

#### Solution
                                 		  1

Ensure that the
                                 		  client has connectivity to the server. Ping the server name that is specified
                                 		  in the URL and verify that it is reachable.

#### Possible Cause
                                 		  2

Misspelled URL.

#### Solution
                                 		  2

Because URLs are
                                 		  case sensitive, ensure that the URL matches exactly with the URL in the
                                 		  instructions.

### System Error -
                           	 Contact System Administrator

#### Problem

After you open the
                                 		  Assistant Console, the following message is displayed:

#### Possible Cause
                                 		  1

You may have upgraded the Unified Communications Manager . The system does not upgrade the Assistant Console automatically when you upgrade the Unified Communications Manager .

#### Solution
                                 		  1

Uninstall the
                                 		  console by choosing Start
                                    			 > Programs > Cisco Unified Communications Manager Assistant >
                                    			 Uninstall Assistant Console and reinstall the console from URL https://<server-name>:8443/ma/Install/IPMAConsoleInstall.jsp .

#### Possible Cause
                                 		  2

The user is not
                                 		  configured correctly in the database.

#### Solution
                                 		  2

Ensure that the user ID and the password are run as a Unified Communications Manager user through Cisco Unified CM Administration.

#### Possible Cause
                                 		  3

When you deleted a
                                 		  manager from an assistant, Cisco Unified CM Administration left a blank line
                                 		  for the assistant.

#### Solution
                                 		  3

From the Assistant
                                    			 Configuration window, reassign the proxy lines.

### Unable to Call
                           	 Manager When Cisco IP Manager Assistant Service is Down

#### Problem

Calls do not get
                                 		  routed properly to managers when Cisco IP Manager Assistant service goes down.

#### Possible
                                 		  Cause

The Unified Communications Manager Assistant CTI route point does not have Call Forward No Answer enabled.

#### Solution

Perform the following procedure to properly configure the Unified Communications Manager Assistant route point.

From Cisco
                                       				Unified CM Administration, choose Device > CTI Route
                                             					 Point .

The Find
                                          				  and List CTI Route Point search window is displayed.

Click Find .

A list of
                                       				configured CTI route points is displayed.

Choose the Unified Communications Manager Assistant CTI route point that you want to update.

In the CTI
                                          				  Route Point Configuration window, click the line to update from the Association area.

In the Call
                                          				  Forward and Pickup Settings section, check the Forward No Answer Internal and the Forward No Answer External check box and
                                       				enter the CTI route point DN in the Coverage/Destination field (for example, CFNA as
                                       				1xxx for the route point DN 1xxx).

In the Calling Search Space drop-down list, choose CSS-M-E (or appropriate calling search
                                       				space).

Click Update .

### User
                           	 Authentication Fails

#### Problem

User
                                 		  authentication fails when you sign in using the login window from the Assistant
                                 		  Console.

#### Possible
                                 		  Cause

The following
                                 		  probable causes can apply:

Incorrect
                                       				management of the user in the database

Incorrect
                                       				management of the user as an assistant or a manager

#### Solution

Ensure that the user ID and the password are ran as a Unified Communications Manager user through Cisco Unified CM Administration.

You must run the user as an assistant or a manager by associating the Unified Communications Manager Assistant user information, which you access through Cisco Unified CM Administration under User Management > End User .

| Note | Managers also have access to Unified Communications Manager features such as Do Not Disturb and Immediate Divert. |
|---|---|

| Important | Before you perform the upgrade, ensure that you uninstall the Cisco Unified Communications Manager Assistant client that is
                                             currently installed on your machine. This is applicable from Releases 12.0(1)SU4 and 14 onwards. |
|---|---|

| Note | To run IPMA plug-in on Windows 11 for Unified Communications Manager Release 15SU1 and earlier versions, you should install
                                                   the IPMA Release 15 version plug-in to any of these supported OS platforms: Windows 10, Windows 2019, and Windows 2022. You
                                                   must then copy the installed version of the IPMA plug-in to Windows 11 and then launch IMPA. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Run the Cisco Unified CM Assistant Configuration Wizard |  |
| Step 2 | Configure Manager And Assign Assistant For Proxy Line |  |
| Step 3 | Configure Assistant Line Appearances for Proxy Line |  |
| Step 4 | Install Assistant Console Plugin | The assistant accesses the Unified Communications Manager Assistant features by using the Assistant Console application and the Cisco Unified IP Phone. The Assistant Console provides
                                       call-control functions such as answer, divert, transfer, and hold. |
| Step 5 | Configure
                                       			 the manager and Assistant Console applications. | See Cisco Unified Communications Manager Assistant User Guide for Cisco Unified Communications Manager . |

| Step 1 | From Cisco Unified CM Administration, choose Application > Cisco Unified CM Assistant Configuration Wizard . |
|---|---|
| Step 2 | Click Next to begin the Cisco Unified CM Assistant
                                          			 Configuration wizard process. |
| Step 3 | In the Partition for Managers window, enter a name, provide
                                          			 a description, and then click Next . Alternatively, you can accept the default
                                          			 partition name and description. |
| Step 4 | In the Partition for CTI Route Point window, enter a name,
                                          			 provide a description, and then click Next . Alternatively, you can accept the default CTI
                                          			 route point name. |
| Step 5 | In the Partition for All Users window, enter a name, provide
                                          			 a description and then click Next . Alternatively, you can accept the default
                                          			 partition name and description for all users. |
| Step 6 | In the Intercom Partition window, enter a name, provide a
                                          			 description, and then click Next . Alternatively, you can accept the default
                                          			 intercom partition name. |
| Step 7 | In the Assistant Calling Search Space window, enter a name,
                                          			 and provide a description. Alternatively, you can use the default calling
                                          			 search space name and description. The
                                          			 Available Partitions and Selected Partitions boxes under the Route Partitions
                                          			 for this Calling Search Space automatically list Partitions for the Assistant
                                          			 Calling Search Space. You can accept the default values or you can choose the
                                          			 applicable partition from the Available Partitions box. Use the up and down
                                          			 arrows to move partitions from one box to the other. |
| Step 8 | Click Next . |
| Step 9 | In the Everyone Calling Search Space window, enter a name,
                                          			 and provide a description. Alternatively, you can accept the default calling
                                          			 search space name and description for everyone. The
                                          			 Available Partitions and Selected Partitions boxes under the Route Partitions
                                          			 for this Calling Search Space automatically list Partitions for the Assistant
                                          			 Calling Search Space. You can accept the default values or you can choose the
                                          			 applicable partition from the Available Partitions box. Use the up and down
                                          			 arrows to move partitions from one box to the other. |
| Step 10 | Click Next . If you
                                          			 have existing calling search spaces that are configured on the system, the Existing Calling Search Spaces window is displayed;
                                          			 otherwise, proceed to the next step. Manager
                                             				Assistant requires that the existing calling search spaces add the prefix Generated_Route Point and Generated_Everyone partitions. The Available Calling Search
                                             				Spaces and Selected Calling Search Spaces boxes automatically list these
                                             				partitions. Use the up and down arrows to move partitions from one box to the
                                             				other. Note The prefix
                                                      				that is added to the existing calling search spaces may change if the
                                                      				administrator has changed the names of the partitions. | Note | The prefix
                                                      				that is added to the existing calling search spaces may change if the
                                                      				administrator has changed the names of the partitions. |
| Note | The prefix
                                                      				that is added to the existing calling search spaces may change if the
                                                      				administrator has changed the names of the partitions. |
| Step 11 | Click Next . |
| Step 12 | In the CTI
                                             				Route Point window, enter a name in the CTI route point name field;
                                          			 otherwise, use the default CTI route point name. |
| Step 13 | From the
                                          			 drop-down list, choose the appropriate device pool. |
| Step 14 | Enter a route
                                          			 point directory number; otherwise, use the default route point directory
                                          			 number. |
| Step 15 | From the
                                          			 drop-down list, choose the appropriate numbering plan and then click Next . |
| Step 16 | In the Phone
                                             				Services window, enter the primary phone service name; otherwise,
                                          			 use the default Phone Service name. |
| Step 17 | From the
                                          			 drop-down list, choose the primary Cisco
                                             				Unified Communications Manager Assistant server or enter a server
                                          			 name or IP address. |
| Step 18 | Enter the
                                          			 secondary phone service name; otherwise, use the default phone service name. |
| Step 19 | From the
                                          			 drop-down list, choose the secondary Cisco
                                             				Unified Communications Manager Assistant server or enter a server
                                          			 name or IP address and then click Next . The Confirmation window is displayed. It provides all the
                                          			 information that you chose. If the information is not correct, you can cancel
                                          			 the configuration process or return to the previous configuration windows. |
| Step 20 | Click Finish . Upon
                                          			 completion, a final status window is displayed. Any errors
                                             				that the configuration wizard generates is sent to a trace file. Access this
                                             				file by using the following CLI command: file get activelog tomcat/logs/ccmadmin/log4j |

| Note | The prefix
                                                      				that is added to the existing calling search spaces may change if the
                                                      				administrator has changed the names of the partitions. |
|---|---|

| Setting | Description |
|---|---|
| Cisco IP
                                                   						Manager Assistant (Active) Parameters |
| CTIManager (Primary) IP Address | This
                                                					 parameter specifies the IP address of the primary CTIManager that this Cisco
                                                					 IPMA server uses to process calls. No default
                                                					 value. |
| CTIManager (Backup) IP Address | This
                                                					 parameter specifies the IP address of the backup CTIManager that this Cisco
                                                					 IPMA server uses to process calls when primary CTIManager is down. No default
                                                					 value. |
| Route
                                                					 Point Device Name for Proxy Mode | This
                                                					 parameter specifies the device name of the CTI route point that this Cisco IPMA
                                                					 server uses to intercept all calls to managers' primary lines for intelligent
                                                					 call routing. Cisco
                                                					 recommends that you use same CTI route point device for all servers running the
                                                					 IPMA service. You must configure the CTI route point device name if any manager
                                                					 or assistant will be configured to use proxy mode. |
| CAPF
                                                					 Profile Instance Id for Secure Connection to CTIManager | This
                                                					 service parameter specifies the Instance ID of the Application CAPF Profile for
                                                					 the application user IPMASecureSysUser that this Manager Assistant will
                                                					 use to open a secure connection to CTIManager. Configure this parameter if CTIManager Connection Security Flag is enabled. |
| Clusterwide Parameters
                                                   						(Parameters that apply to all servers) Important Click Advanced to view the hidden parameters. | Important | Click Advanced to view the hidden parameters. |
| Important | Click Advanced to view the hidden parameters. |
| Cisco IPMA
                                                					 Server (Primary) IP Address | This
                                                					 parameter specifies the IP address of the primary Cisco IPMA server. No default
                                                					 value. |
| Cisco
                                                					 IPMA Server (Backup) IP Address | This
                                                					 parameter specifies the IP address of the backup Cisco IPMA server. The backup
                                                					 server provides IPMA service when the primary IPMA server fails. No default
                                                					 value. |
| Cisco
                                                					 IPMA Server Port | This
                                                					 parameter specifies the TCP/IP port on the Cisco IPMA servers to which the IPMA
                                                					 Assistant Consoles will open socket connections. You may change the parameter
                                                					 if a port conflict exists. Default
                                                					 value: 2912 |
| Cisco
                                                					 IPMA Assistant Console Heartbeat Interval | This
                                                					 parameter specifies the interval, in seconds, at which the Cisco IPMA server
                                                					 sends keepalive messages (commonly referred to as heartbeat) to the IPMA
                                                					 Assistant Consoles. The IPMA Assistant Consoles initiate failover when they
                                                					 fail to receive heartbeat from the server before the time that is specified in
                                                					 this parameter expires. Default
                                                					 value: 30 seconds |
| Cisco
                                                					 IPMA Assistant Console Request Timeout | This
                                                					 parameter specifies the time, in seconds, that the IPMA Assistant Consoles wait
                                                					 to receive a response from the Cisco IPMA server. Default
                                                					 value: 30 seconds |
| Cisco
                                                					 IPMA RNA Forward Calls | This
                                                					 parameter determines whether Cisco IPMA Ring No Answer (RNA) forwarding is
                                                					 enabled. Valid values are True (Cisco IPMA forwards unanswered calls to next
                                                					 available assistant) or False (Cisco IPMA does not forward calls). This parameter works in conjunction with the Cisco IPMA RNA Timeout parameter; calls
                                                					 are forwarded after the time that is specified in the Cisco IPMA RNA Timeout parameter. If a
                                                					 voicemail profile is specified for the line, unanswered calls that cannot be
                                                					 forwarded to an assistant are sent to voicemail when this timer expires. Default
                                                					 value: False |
| Alpha
                                                					 Numeric UserID | This
                                                					 parameter determines whether Cisco IPMA Assistant Phone uses an alphanumeric
                                                					 user ID or a numeric user ID. Default
                                                					 value: True |
| Cisco IPMA
                                                					 RNA Timeout | This
                                                					 parameter specifies the time, in seconds, that the Cisco IPMA server waits
                                                					 before forwarding an unanswered call to the next available assistant. This
                                                					 parameter works in conjunction with the Cisco IPMA RNA Forward Calls parameter; forwarding
                                                					 occurs only if the Cisco IPMA RNA Forward Calls parameter is set to True . Default
                                                					 value: 10 seconds |
| CTIManager Connection Security Flag | This
                                                					 parameter determines whether security for the Cisco IP Manager Assistant
                                                					 service CTIManager connection is enabled. If it is enabled, Cisco IPMA opens a
                                                					 secure connection to CTIManager using the CAPF profile that is configured for
                                                					 the instance ID (as specified in the CAPF Profile Instance ID for Secure Connection to
                                                   						CTIManager service parameter) for the application user IPMASecureSysUser . Default
                                                					 value: Non Secure To
                                                					 enable security, you must select an instance ID in the CAPF Profile Instance ID for Secure Connection to
                                                   						CTIManager service parameter. |
| Redirect
                                                					 call to Manager upon failure to reach Assistant | This
                                                					 parameter determines whether the Cisco Unified IP Manager Assistant application
                                                					 redirects the call back to the intended manager if the call fails to reach the
                                                					 selected proxy assistant. Default
                                                					 value: False |
| Advanced Clusterwide
                                                   						parameters Important Configure unique IP addresses for each pool so that the same
                                                         					 Cisco IPMA server IP address does not appear in more than one pool. | Important | Configure unique IP addresses for each pool so that the same
                                                         					 Cisco IPMA server IP address does not appear in more than one pool. |
| Important | Configure unique IP addresses for each pool so that the same
                                                         					 Cisco IPMA server IP address does not appear in more than one pool. |
| Enable
                                                					 Multiple Active Mode | This
                                                					 parameter determines whether multiple instances of the Cisco IP Manager
                                                					 Assistant service must be run for scalability. If it is enabled, Cisco IPMA can
                                                					 run on the other nodes as configured in the Pool 2 and Pool 3 parameters. To
                                                					 enable multiple active mode, you must enter the IP addresses of the nodes on
                                                					 which you want to run the additional instances of Cisco IPMA. Configure the
                                                					 Cisco IP Manager Assistant service parameters on those nodes. Default
                                                					 value: False |
| Pool 2:
                                                					 Cisco IPMA Server (Primary) IP Address | If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 primary Cisco IPMA server of the second instance of Cisco IPMA. Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node. |
| Pool 2:
                                                					 Cisco IPMA Server (Backup) IP Address | If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 backup Cisco IPMA server of the second instance of Cisco IPMA. The backup
                                                					 server provides IPMA service when the primary IPMA server fails. Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node. |
| Pool 3:
                                                					 Cisco IPMA Server (Primary) IP Address | If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 primary Cisco IPMA server of the third instance of Cisco IPMA. Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node. |
| Pool 3:
                                                					 Cisco IPMA Server (Backup) IP Address | If
                                                					 multiple active mode is enabled, this parameter specifies the IP address of the
                                                					 primary Cisco IPMA server of the third instance of Cisco IPMA. The backup
                                                					 server provides IPMA service when the primary IPMA server fails. Configure the Cisco IP Manager Assistant service parameters on
                                                					 this node. |
| Clusterwide Parameters
                                                   						(Softkey Templates) Important Configure these parameters if you want to use the Manager
                                                         					 Assistant automatic configuration for managers and assistants. | Important | Configure these parameters if you want to use the Manager
                                                         					 Assistant automatic configuration for managers and assistants. |
| Important | Configure these parameters if you want to use the Manager
                                                         					 Assistant automatic configuration for managers and assistants. |
| Assistant Softkey Template | This parameter specifies the assistant softkey template that
                                                					 is assigned to assistant devices during Automatic Configuration. The value that
                                                					 is specified in this parameter is used when the Automatic Configuration check box is
                                                					 checked on the Cisco IPMA Assistant Configuration page. |
| Manager
                                                					 Softkey Template for Proxy Mode | This
                                                					 parameter specifies the manager softkey template for proxy mode that is
                                                					 assigned to manager devices during Automatic Configuration. This parameter
                                                					 applies only for managers that use proxy mode. |
| Clusterwide Parameters
                                                   						(IPMA Device Configuration Defaults for Proxy Mode) |
| Manager
                                                					 Partition | This
                                                					 parameter defines the partition that is assigned to manager lines that IPMA
                                                					 handles on manager devices during Automatic Configuration. Make sure the
                                                					 partition you want to use has already been added to Cisco Unified CM
                                                					 Administration. If the Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers that use
                                                					 proxy mode. |
| All User
                                                					 Partition | This
                                                					 parameter specifies the partition that is configured on all proxy lines and the
                                                					 intercom line on assistant devices, as well as the intercom line on manager
                                                					 devices, during Automatic Configuration. Make sure the partition you want to
                                                					 use has already been added to Cisco Unified CM Administration. If the Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or
                                                					 assistants that use proxy mode. |
| IPMA
                                                					 Calling Search Space | This
                                                					 parameter specifies the calling search space that is configured for manager
                                                					 lines on manager devices that IPMA handles and the intercom line, as well as
                                                					 the assistant intercom line on assistant devices during Automatic
                                                					 Configuration. Make sure the calling search space you want to use has already
                                                					 been added to Cisco Unified CM Administration. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or
                                                					 assistants that use proxy mode. |
| Manager
                                                					 Calling Search Space | This
                                                					 parameter defines the manager calling search space that is configured on proxy
                                                					 lines on assistant devices during Automatic Configuration. This calling search
                                                					 space must be a calling search space that already exists in the system. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for assistants that use
                                                					 proxy mode. |
| Cisco
                                                					 IPMA Primary Phone Service | This
                                                					 parameter defines the IP phone service to which manager/assistant devices will
                                                					 be subscribed during Automatic Configuration. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or assistants
                                                					 that use proxy mode. |
| Cisco
                                                					 IPMA Secondary Phone Service | This
                                                					 parameter defines the secondary IP phone service to which manager or assistant
                                                					 devices will be subscribed during Automatic Configuration. If Cisco IPMA Configuration Wizard is run, it
                                                					 will populate this value. This parameter applies only for managers or assistants
                                                					 that use proxy mode. |
| Clusterwide Parameters
                                                   						(Proxy Directory Number Range for Proxy Mode) |
| Starting
                                                					 Directory Number | This
                                                					 parameter specifies the starting directory number that is used as the starting
                                                					 number for automatic generation of proxy directory numbers during IPMA
                                                					 assistant configuration. After an auto-generated proxy line number is used for
                                                					 an assistant, the next number will be generated for the next assistant, and so
                                                					 on. This parameter applies only for assistants that use proxy mode. |
| Ending
                                                					 Directory Number | This
                                                					 parameter specifies the ending directory number for automatic generation of
                                                					 proxy directory numbers during IPMA assistant configuration. Configuration will
                                                					 stop at this number. This parameter applies only for assistants that use proxy
                                                					 mode. |
| Clusterwide Parameters
                                                   						(Proxy Directory Number Range for Proxy Mode) |
| Number
                                                					 of Characters to be Stripped from Manager DN | This
                                                					 parameter specifies the number of characters to be stripped from the manager
                                                					 directory number (DN) in the process of generating the proxy DN. Generating a
                                                					 proxy DN may involve stripping some number of digits and adding a prefix.
                                                					 Digits are stripped starting from the left. This parameter applies only for
                                                					 assistants that use proxy mode. |
| Prefix
                                                					 for Manager DN | This
                                                					 parameter specifies the prefix to be added to a manager DN in the process of
                                                					 generating the proxy DN. Generating a proxy DN may involve some stripping of
                                                					 digits and adding a prefix. This parameter applies only for assistants that use
                                                					 proxy mode. |

| Important | Click Advanced to view the hidden parameters. |
|---|---|

| Important | Configure unique IP addresses for each pool so that the same
                                                         					 Cisco IPMA server IP address does not appear in more than one pool. |
|---|---|

| Important | Configure these parameters if you want to use the Manager
                                                         					 Assistant automatic configuration for managers and assistants. |
|---|---|

| Note | Make sure you
                                          		  configure manager information before you configure assistant information for an
                                          		  assistant. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Click Find . The search result displays all the end users that are configured in Unified Communications Manager . |
| Step 3 | From the Related Links drop-down list, choose Manager Configuration and click Go . Tip To view existing assistant configuration information, click the
                                                      				assistant name in the Associated Assistants list and click View
                                                         				  Details . The Cisco Unified CM Assistant - Assistant Configuration window is displayed. To return to the manager configuration information, click
                                                      				the manager name in the Associated Managers list and click View
                                                         				  Details . The Cisco
                                             				Unified CM Assistant - Manager Configuration window is displayed. | Tip | To view existing assistant configuration information, click the
                                                      				assistant name in the Associated Assistants list and click View
                                                         				  Details . The Cisco Unified CM Assistant - Assistant Configuration window is displayed. To return to the manager configuration information, click
                                                      				the manager name in the Associated Managers list and click View
                                                         				  Details . |
| Tip | To view existing assistant configuration information, click the
                                                      				assistant name in the Associated Assistants list and click View
                                                         				  Details . The Cisco Unified CM Assistant - Assistant Configuration window is displayed. To return to the manager configuration information, click
                                                      				the manager name in the Associated Managers list and click View
                                                         				  Details . |
| Step 4 | From the Device
                                             				Name/Profile drop-down list, choose the device name or device
                                          			 profile to associate a device name or device profile with a manager. For more
                                          			 information about Extension Mobility with Manager Assistant, see Manager Assistant Interactions . Note If the
                                                      				manager telecommutes, click the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. After you choose
                                                      				a device profile, the manager must log in to the phone by using extension
                                                      				mobility before accessing Manager Assistant. | Note | If the
                                                      				manager telecommutes, click the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. After you choose
                                                      				a device profile, the manager must log in to the phone by using extension
                                                      				mobility before accessing Manager Assistant. |
| Note | If the
                                                      				manager telecommutes, click the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. After you choose
                                                      				a device profile, the manager must log in to the phone by using extension
                                                      				mobility before accessing Manager Assistant. |
| Step 5 | From the Intercom Line drop-down list, choose the intercom
                                          			 line appearance for the manager, if applicable. Note The chosen intercom line applies to the Manager Assistant and Unified Communications Manager intercom features. | Note | The chosen intercom line applies to the Manager Assistant and Unified Communications Manager intercom features. |
| Note | The chosen intercom line applies to the Manager Assistant and Unified Communications Manager intercom features. |
| Step 6 | From the Assistant Pool drop-down list, choose the
                                          			 appropriate pool number (1 to 3). |
| Step 7 | From the Available Lines selection box, choose a line that
                                          			 you want Manager Assistant to control and click the down arrow to make the line
                                          			 display in the Selected Lines selection box. Configure up to five Manager
                                          			 Assistant—controlled lines. Tip To remove a line from the Selected Lines selection box and from
                                                      				Manager Assistant control, click the up arrow. | Tip | To remove a line from the Selected Lines selection box and from
                                                      				Manager Assistant control, click the up arrow. |
| Tip | To remove a line from the Selected Lines selection box and from
                                                      				Manager Assistant control, click the up arrow. |
| Step 8 | Check the Automatic Configuration check box to automatically
                                          			 configure the softkey template, subscribe to the Manager Assistant phone
                                          			 service, calling search space, and partition for Manager Assistant—Controlled
                                          			 selected lines and intercom line; and Auto Answer with Speakerphone for
                                          			 intercom line for the manager phone based on the Cisco IP Manager Assistant
                                          			 service parameters. Note Automatic
                                                      				Configuration for intercom applies only when using the Manager Assistant
                                                      				intercom feature for the Cisco Unified IP Phones 7940 and 7960. | Note | Automatic
                                                      				Configuration for intercom applies only when using the Manager Assistant
                                                      				intercom feature for the Cisco Unified IP Phones 7940 and 7960. |
| Note | Automatic
                                                      				Configuration for intercom applies only when using the Manager Assistant
                                                      				intercom feature for the Cisco Unified IP Phones 7940 and 7960. |
| Step 9 | Click Save . If you
                                          			 checked the Automatic Configuration check box and the service
                                          			 parameters are invalid, a message displays. Ensure that the service parameters
                                          			 are valid. Upon successful completion of the automatic configuration, the
                                          			 manager device resets. If you configured a device profile, the manager must log
                                          			 out and log in to the device for settings to take effect. |

| Tip | To view existing assistant configuration information, click the
                                                      				assistant name in the Associated Assistants list and click View
                                                         				  Details . The Cisco Unified CM Assistant - Assistant Configuration window is displayed. To return to the manager configuration information, click
                                                      				the manager name in the Associated Managers list and click View
                                                         				  Details . |
|---|---|

| Note | If the
                                                      				manager telecommutes, click the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. After you choose
                                                      				a device profile, the manager must log in to the phone by using extension
                                                      				mobility before accessing Manager Assistant. |
|---|---|

| Note | The chosen intercom line applies to the Manager Assistant and Unified Communications Manager intercom features. |
|---|---|

| Tip | To remove a line from the Selected Lines selection box and from
                                                      				Manager Assistant control, click the up arrow. |
|---|---|

| Note | Automatic
                                                      				Configuration for intercom applies only when using the Manager Assistant
                                                      				intercom feature for the Cisco Unified IP Phones 7940 and 7960. |
|---|---|

| Note | Make sure that you configure manager information and assign an assistant to the manager before you configure assistant information
                                                   for an assistant. If you want to automatically configure proxy line on the assistant phone, configure the service parameters in Proxy Directory Number Range and Proxy Directory Number Prefix sections. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Click on the
                                          			 user name to display user information for the chosen assistant The End
                                             				User Configuration window is displayed. |
| Step 4 | From the Related Links drop-down list, choose Assistant Configuration and click Go . Note The system
                                                      				automatically sets the softkey template and intercom line on the basis of the
                                                      				Cisco IP Manager Assistant service parameter settings when the Automatic Configuration check box is checked. In
                                                      				addition, the system also sets Auto Answer with Speakerphone for intercom line. The Assistant Configuration window is displayed. | Note | The system
                                                      				automatically sets the softkey template and intercom line on the basis of the
                                                      				Cisco IP Manager Assistant service parameter settings when the Automatic Configuration check box is checked. In
                                                      				addition, the system also sets Auto Answer with Speakerphone for intercom line. |
| Note | The system
                                                      				automatically sets the softkey template and intercom line on the basis of the
                                                      				Cisco IP Manager Assistant service parameter settings when the Automatic Configuration check box is checked. In
                                                      				addition, the system also sets Auto Answer with Speakerphone for intercom line. |
| Step 5 | From the Device
                                             				Name drop-down list, choose the device name to associate with the
                                          			 assistant. |
| Step 6 | From the Intercom Line drop-down list, choose the incoming
                                          			 intercom line appearance for the assistant. |
| Step 7 | From the Primary Line drop-down list, choose the primary line
                                          			 for the assistant. |
| Step 8 | To associate
                                          			 the manager line to the assistant line, perform the following steps from the
                                          			 Manager Association to Assistant Line selection box: From the Available Lines drop-down list, choose the assistant
                                                				  line that will be associated with the manager line. From the Manager Names drop-down list, choose the
                                                				  preconfigured manager name for whom this proxy line will apply. From the Manager Lines drop-down list, choose the manager
                                                				  line for which this proxy line will apply. |
| Step 9 | Click Save . The
                                          			 update takes effect immediately. If you chose Automatic Configuration , the assistant device
                                          			 automatically resets. |

| Note | The system
                                                      				automatically sets the softkey template and intercom line on the basis of the
                                                      				Cisco IP Manager Assistant service parameter settings when the Automatic Configuration check box is checked. In
                                                      				addition, the system also sets Auto Answer with Speakerphone for intercom line. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Partitions for Manager Assistant Shared Line Support | Configure
                                       			 a partition for lines that is used by Manager Assistant. |
| Step 2 | Configure Calling Search Spaces for Manager Assistant Shared Line Support | Configure
                                       			 calling search spaces for manager and assistant lines. |
| Step 3 | Configure Cisco IP Manager Assistant Service Parameters | Configure
                                       			 these parameters to use automatic configuration for managers and assistants. |
| Step 4 | Configure intercom settings. |  |
| Step 5 | Configure Multiple Manager Assistant Pool | Configure multiple pools if you need to support a large number of managers and assistants. You can configure up to three active
                                       Cisco IP Manager Assistant servers, with each managing up to 2500 pairs of managers and assistants. |
| Step 6 | Configure Secure TLS Connection to CTI Configure IPMASecureSysUser Application User Configure CAPF Profile Configure Cisco WebDialer Web Service | Follow these procedures if your system is running in mixed mode. |
| Step 7 | Configure CTI Route Point | Cisco Unified Communications Manager Assistant requires creation of CTI route point to intercept and route calls from managers. |
| Step 8 | Configure IP Phone Services for Manager and Assistant |  |
| Step 9 | Configure Phone Button Templates for Manager, Assistant, and Everyone |  |
| Step 10 | Configure Manager and Assign Assistant for Shared Line Mode |  |
| Step 11 | Configure Assistant Line Appearances for Shared Line |  |
| Step 12 | Install Assistant Console Plugin | The assistant accesses the Cisco Unified Communications Manager Assistant features by using the Assistant Console application and the Cisco Unified IP Phone . The Assistant Console provides call-control functions such as answer, divert, transfer, and hold. |
| Step 13 | Configure
                                       			 the manager and assistant console applications. | See Cisco Unified Communications Manager Assistant User Guide for Cisco Unified Communications Manager . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | Click Add
                                             				New to create a new partition. |
| Step 3 | In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan. Partition
                                          			 names can contain alphanumeric characters, as well as spaces, hyphens (-), and
                                          			 underscore characters (_). See the online help for guidelines about partition
                                          			 names. |
| Step 4 | Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line. The
                                          			 description can contain up to 50 characters in any language, but it cannot
                                          			 include double quotes ("), percentage sign (%), ampersand (&), backslash
                                          			 (\), angle brackets (<>), or square brackets ([ ]). If you do
                                          			 not enter a description, Cisco Unified Communications Manager automatically
                                          			 enters the partition name in this field. |
| Step 5 | To create
                                          			 multiple partitions, use one line for each partition entry. |
| Step 6 | From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition. The time
                                          			 schedule specifies when the partition is available to receive incoming calls.
                                          			 If you choose None , the partition remains active at all times. |
| Step 7 | Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone : Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. |
| Step 8 | Click Save . |

| Partition
                                                					 Name Length | Maximum
                                                					 Number of Partitions |
|---|---|
| 2 characters | 340 |
| 3 characters | 256 |
| 4 characters | 204 |
| 5 characters | 172 |
| ... | ... |
| 10
                                                					 characters | 92 |
| 15
                                                					 characters | 64 |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter a name. Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_). |
| Step 4 | In the Description field, enter a description. The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>). |
| Step 5 | From the Available Partitions drop-down list, perform one of
                                          			 the following steps: For a single partition,
                                             				select that partition. For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions. |
| Step 6 | Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field. |
| Step 7 | (Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which
                                          			 the Cisco IP Manager Assistant service is active. |
| Step 3 | From the Service drop-down list, choose Cisco
                                             				IP Manager Assistant service. The Service
                                             				Parameter Configuration window, which lists the parameters, is
                                          			 displayed. |
| Step 4 | Configure the Cisco
                                             				IP Manager Assistant Parameters , Clusterwide Parameters (Parameters that apply to all
                                             				servers) , and Clusterwide Parameters (Softkey Templates) . click ? for detailed descriptions. |
| Step 5 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure an Intercom Partition |  |
| Step 2 | Configure an Intercom Calling Search Space |  |
| Step 3 | Configure an Intercom Directory Number |  |
| Step 4 | Configure an Intercom Translation Pattern |  |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Intercom > Intercom Route Partition . The Find and List Intercom Partitions window appears. |
|---|---|
| Step 2 | Click Add New . An Add New Intercom Partition window appears. |
| Step 3 | Under the Intercom Partition Information section, in the Name box, enter the name and description of the
                                             			 intercom partition that you want to add. Note To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                            can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                            partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. | Note | To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                            can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                            partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. |
| Note | To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                            can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                            partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. |
| Step 4 | Click Save . |
| Step 5 | Locate the
                                             			 partition that you want to configure. Intercom Partition Configuration window is displayed |
| Step 6 | Configure the
                                             			 fields in the Intercom Partition Configuration field area. See the online help
                                             			 for more information about the fields and their configuration options. |
| Step 7 | Click Save . The Intercom Partition
                                                   				  Configuration window appears. |
| Step 8 | Enter the
                                             			 appropriate settings. For detailed information about the Intercom Partition
                                             			 Configuration parameters, see online help. |
| Step 9 | Click Save . |
| Step 10 | Click Apply
                                                				Config . |

| Note | To enter multiple partitions, use one line for each partition entry. You can enter up to 75 partitions; the names and descriptions
                                                            can have up to a total of 1475 characters. The partition name cannot exceed 50 characters. Use a comma (,) to separate the
                                                            partition name and description on each line. If a description is not entered, Unified Communications Manager uses the partition name as the description. |
|---|---|

| Step 1 | In the menu
                                             			 bar, choose Call
                                                   				  Routing > Intercom > Intercom Calling Search
                                                   				  Space . |
|---|---|
| Step 2 | Click the Add New . |
| Step 3 | Configure the fields in the Intercom Calling Search Space field area. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . |

| Step 1 | Choose Call
                                                   				  Routing > Intercom > Intercom Directory
                                                   				  Number . The Find
                                                   				  and List Intercom Directory Numbers window is displayed. |
|---|---|
| Step 2 | To locate a
                                             			 specific intercom directory number, enter search criteria and click Find. A list
                                             			 of intercom directory numbers that match the search criteria displayed. |
| Step 3 | Perform one of
                                             			 the followings tasks: To add an intercom directory number, click Add New . To update
                                                   				  an intercom directory number, click the intercom directory number to update. The Intercom Directory Number Configuration window
                                                				displayed. |
| Step 4 | Configure the fields in the Intercom Directory Number Configuration field area. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                                				Config . |
| Step 7 | Click Reset
                                                				Phone . |
| Step 8 | Restart
                                             			 devices. During the
                                                				restart, the system may drop calls on gateways. |

| Step 1 | Choose Call
                                                   				  Routing > Intercom > Intercom Translation
                                                   				  Pattern . The Find
                                                   				  and List Intercom Translation Patterns window appears. |
|---|---|
| Step 2 | Perform one of
                                             			 the followings tasks: To copy an existing intercom translation pattern, locate the partition to configure, click Copy eside the intercom translation pattern to copy. To add a new intercom translation pattern, click the Add New . |
| Step 3 | Configure the fields in the Intercom Translation Pattern Configuration field area. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . Ensure that
                                                				the intercom translation pattern that uses the selected partition, route
                                                				filter, and numbering plan combination is unique. if you receive an error that
                                                				indicates duplicate entries, check the route pattern or hunt pilot, translation
                                                				pattern, directory number, call park number, call pickup number, or meet-me
                                                				number configuration windows. The Intercom Translation
                                                   				  Pattern Configuration window displays the newly configured intercom
                                                				translation pattern. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which
                                          			 the Cisco IP Manager Assistant service is active. |
| Step 3 | From the Service drop-down list, choose the Cisco
                                             				IP Manager Assistant service. The Service
                                             				Parameter Configuration window, which lists the parameters, is
                                          			 displayed. |
| Step 4 | Click Advanced . The
                                          			 advanced parameters for Clusterwide Parameters (Parameters that apply to all
                                             				servers) are displayed. |
| Step 5 | Configure the
                                          			 following parameters to add multiple manager assistant pools in Clusterwide Parameters (Parameters that apply to all
                                             				servers) : Enable Multiple Active
                                                   					 Mode —The default is False. When this parameter is set to True, the
                                                				  administrator can configure up to 7000 managers and assistants by using
                                                				  multiple pools. Pool 2: Cisco IPMA Server
                                                   					 (Primary) IP Address —No default. The administrator must manually
                                                				  enter this IP address. Administrator can assign up to 2500 managers and
                                                				  assistants to this address. Pool 2: Cisco IPMA Server
                                                   					 (Backup) IP Address —No default. The administrator must manually
                                                				  enter this IP address. Pool 3: Cisco IPMA Server
                                                   					 (Primary) IP Address —No default. The administrator must manually
                                                				  enter this IP address and can assign up to 2500 managers and assistants to this
                                                				  address. Pool 3: Cisco IPMA Server
                                                   					 (Backup) IP Address —No default. The administrator must manually
                                                				  enter this IP address. click ? for detailed descriptions. |
| Step 6 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IPMASecureSysUser Application User | Configure IPMASecureSysUser Application User. |
| Step 2 | Configure CAPF Profile | Configure Certificate Authority Proxy Function (CAPF) Profile for the IPMASecureSysUser Application User. |
| Step 3 | Configure Cisco WebDialer Web Service | Configure service parameters for the Cisco IP Manager Assistant service. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > Application User . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | From the Find
                                                				and List Application Users Application window, choose WDSecureSysUser . |
| Step 4 | Configure the
                                             			 fields in the Application User Configuration window and click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > Application User CAPF Profile . |
|---|---|
| Step 2 | Perform one of
                                             			 the following tasks: Click Add New in the Find window, to add a new CAPF profile. Click Copy for that record in the Copy column, to copy an existing profile, and locate the appropriate profile. To update an
                                             			 existing entry, locate and display the appropriate profile. |
| Step 3 | Configure or
                                             			 update the relevant CAPF profile fields. See the Related Topics section
                                             			 information about the fields and their configuration options. |
| Step 4 | Click Save . |
| Step 5 | Repeat the
                                             			 procedure for each application and end user that you want to use security. |

| Setting | Description |
|---|---|
| Application User | From the drop-down list, choose the application user for the
                                                   						CAPF operation. This setting displays configured application users. This setting does not appear in the End User CAPF Profile window. |
| End User ID | From the drop-down list, choose the end user for the CAPF
                                                   						operation. This setting displays configured end users. This setting does not appear in the Application User CAPF Profile window. |
| Instance ID | Enter 1 to 128 alphanumeric characters (a-z, A-Z, 0-9). The
                                                   						Instance ID identifies the user for the certificate operation. You can configure multiple connections (instances) of an
                                                   						application. To secure the connection between the application and CTIManager,
                                                   						ensure that each instance that runs on the application PC (for end users) or
                                                   						server (for application users) has a unique certificate. This field relates to the CAPF Profile Instance ID for Secure
                                                   						Connection to CTIManager service parameter that supports web services and
                                                   						applications. |
| Certificate Operation | From the drop-down list, choose one of the following options: No Pending Operation —This message is displayed when no certificate operation is occurring. (default setting) Install/Upgrade —This option installs a new certificate or upgrades an existing locally significant certificate for the application. |
| Authentication Mode | The authentication mode for the Install/Upgrade certificate
                                                   						operation specifies By Authentication String, which means CAPF installs,
                                                   						upgrades, or troubleshoots a locally significant certificate only when the user
                                                   						or administrator enters the CAPF authentication string in the JTAPI/TSP Preferences window. |
| Authentication String | To create your own authentication string, enter a unique string. Each string must contain 4 to 10 digits. To install or upgrade a locally significant certificate, the
                                                   						administrator must enter the authentication string in the JTAPI/TSP preferences
                                                   						GUI on the applicationPC. This string supports one-time use only; after you
                                                   						use the string for the instance, you cannot use it again. |
| Generate String | To automatically generate an authentication string, click this
                                                   						button. The 4- to10-digit authentication string appears in the Authentication String field. |
| Key Size (bits) | From the drop-down list, choose the key size for the
                                                   						certificate. The default setting is 1024. The other option for key size is 512. Key generation, which is set at low priority, allows the
                                                   						application to function while the action occurs. Key generation may take up to
                                                   						30 or more minutes. |
| Operation Completes by | This field, which supports all certificate operations, specifies
                                                   						the date and time by which you must complete the operation. The values that are displayed apply for the first node. Use this setting with the CAPF Operation Expires in (days) enterprise parameter, which specifies the default number of days in which the
                                                   						certificate operation must be completed. You can update this parameter at any
                                                   						time. |
| Certificate Operation Status | This field displays the progress of the certificate operation,
                                                   						such as pending, failed, or successful. You cannot change the information that is displayed in this
                                                   						field. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which
                                             			 the Cisco WebDialer Web service is active. |
| Step 3 | From the Service drop-down list, choose the Cisco WebDialer Web service. A list
                                             			 of parameters appears. |
| Step 4 | Navigate to
                                             			 and update the CTIManager Connection Security Flag and CAPF Profile Instance ID
                                             			 for Secure Connection to CTIManager parameters. To view
                                                				parameter descriptions, click the parameter name link. Note CTIManager
                                                            				  supports IPv4 and IPv6 addresses. | Note | CTIManager
                                                            				  supports IPv4 and IPv6 addresses. |
| Note | CTIManager
                                                            				  supports IPv4 and IPv6 addresses. |
| Step 5 | Click Save . |
| Step 6 | Repeat the
                                             			 procedure on each server on which the service is active. |

| Note | CTIManager
                                                            				  supports IPv4 and IPv6 addresses. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > CTI Route Point . |
|---|---|
| Step 2 | Click Add
                                             				New . The CTI
                                             				Route Point Configuration window is displayed. |
| Step 3 | In the Device
                                             				Name field, enter the device name. |
| Step 4 | From the Device
                                             				Pool drop-down list, choose Default . |
| Step 5 | From the Calling Search Space drop-down list, choose Generated_CSS_M_E . |
| Step 6 | Check the Use
                                             				Device Pool Calling Party Transformation CSS check box. |
| Step 7 | Click Save . Add successful status message is displayed. |
| Step 8 | From the
                                          			 Association area, click Line
                                             				[1] - Add a new DN . The Directory Number Configuration window is displayed. |
| Step 9 | Enter a
                                          			 directory number in the Directory Number field. |
| Step 10 | From the Route
                                             				Partition drop-down list, choose Generated_Route_Point . |
| Step 11 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Services . |
|---|---|
| Step 2 | Click Add
                                             				New . The IP
                                             				Phone Services Configuration window is displayed. |
| Step 3 | For each supported phone for managers and assistants, enter the required fields and click Save . See Cisco IP Phone Services Configuration Fields for more information about the fields and their configuration options. The Update successful message is displayed. |

| Field | Description |
|---|---|
| Service Information |
| Service
                                                						Name | Enter
                                                						the name of the service. If the service is not marked as an enterprise
                                                						subscription, the service name will display in areas where you can subscribe to
                                                						a service, for example, under Cisco Unified Communications Self Care Portal. Enter up
                                                						to 128 characters for the service name. For Java
                                                						MIDlet services, the service name must exactly match the name that is defined
                                                						in the Java Application Descriptor (JAD) file. Note Unified Communications Manager allows you to create two or more IP phone services with identical names. Cisco recommends that you do not do so unless most
                                                         or all phone users are advanced, or unless an administrator always configures the IP phone services. Be aware that if AXL
                                                         or any third-party tool accesses the list of IP phone services for configuration, you must use unique names for IP phone services. Note When
                                                         						the service URL points to an external customized URL, you cannot localize the
                                                         						service name according to the device locale of the phone. The service name gets
                                                         						displayed in English alphabets only. | Note | Unified Communications Manager allows you to create two or more IP phone services with identical names. Cisco recommends that you do not do so unless most
                                                         or all phone users are advanced, or unless an administrator always configures the IP phone services. Be aware that if AXL
                                                         or any third-party tool accesses the list of IP phone services for configuration, you must use unique names for IP phone services. | Note | When
                                                         						the service URL points to an external customized URL, you cannot localize the
                                                         						service name according to the device locale of the phone. The service name gets
                                                         						displayed in English alphabets only. |
| Note | Unified Communications Manager allows you to create two or more IP phone services with identical names. Cisco recommends that you do not do so unless most
                                                         or all phone users are advanced, or unless an administrator always configures the IP phone services. Be aware that if AXL
                                                         or any third-party tool accesses the list of IP phone services for configuration, you must use unique names for IP phone services. |
| Note | When
                                                         						the service URL points to an external customized URL, you cannot localize the
                                                         						service name according to the device locale of the phone. The service name gets
                                                         						displayed in English alphabets only. |
| ASCII
                                                						Service Name | Enter
                                                						the name of the service to display if the phone cannot display Unicode. |
| Service
                                                						Description | Enter a
                                                						description of the content that the service provides. The description can
                                                						include up to 50 characters in any language, but it cannot include double
                                                						quotation marks (") or single quotation marks ('). |
| Service
                                                						URL | Enter the URL of the server where the IP phone services application is located. Make sure that this server remains independent
                                                of the servers in your Unified Communications Manager cluster. Do not specify a Unified Communications Manager server or any server that is associated with Unified Communications Manager (such as a TFTP server or directory database publisher server). For the services to be available, the phones in the Unified Communications Manager cluster must have network connectivity to the server. For
                                                						Cisco-signed Java MIDlets, enter the location where the JAD file can be
                                                						downloaded; for example, a web server or the back-end application server to
                                                						which the Java MIDlet communicates. For
                                                						Cisco-provided default services, the service URL is displayed as Application:Cisco/<name of service> by
                                                						default; for example, Application:Cisco/CorporateDirectory . If you
                                                						modify the service URL for Cisco-provided default services, verify that you
                                                						configured both for the Service Provisioning setting, which displays in the Phone , Enterprise Parameter , and Common Phone Profile Configuration windows. For
                                                						example, you use a custom corporate directory, so you change Application:Cisco/CorporateDirectory to the
                                                						external service URL for your custom directory; in this case, change the Service Provisioning value  to Both . |
| Secure-Service URL | Enter the secure URL of the server where the Cisco Unified IP Phone services application is located. Make sure that this server remains independent of the servers in your Unified Communications Manager cluster. Do not specify a Unified Communications Manager server or any server that is associated with Unified Communications Manager (such as a TFTP server or publisher database server). For the services to be available, the phones in the Unified Communications Manager cluster must have network connectivity to the server. Note If
                                                         						you do not provide a Secure-Service URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. | Note | If
                                                         						you do not provide a Secure-Service URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Note | If
                                                         						you do not provide a Secure-Service URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
| Service
                                                						Category | Choose a
                                                						service application type (XML or Java MIDlet). If you
                                                						choose Java MIDlet, when the phone receives the updated configuration file, the
                                                						phone retrieves the Cisco-signed MIDlet application (JAD and JAR) from the
                                                						specified Service URL and installs the application. |
| Service
                                                						Type | Choose
                                                						whether the service is provisioned to the Services, Directories, or Messages
                                                						button or option on the phone; that is, if the phone has these buttons or
                                                						options. To determine whether your phone supports these buttons or options, see
                                                						the Cisco Unified IP Phone Administration Guide that supports
                                                						your phone model. |
| Service
                                                						Vendor | Allows you to specify the vendor or manufacturer for the service. This field is optional for XML applications, but it is required
                                                for Cisco-signed Java MIDlets. For
                                                						Cisco-signed Java MIDlets, the value that you enter in this field must exactly
                                                						match the vendor that is defined in the MIDlet JAD file. This
                                                						field displays as blank for Cisco-provided default services. You can
                                                						enter up to 64 characters. |
| Service
                                                						Version | Enter
                                                						the version number for the application. For XML
                                                						applications, this field is optional and is informational only. For
                                                						Cisco-signed Java MIDlets, consider the following information: If
                                                      							 you enter a version, the service version must exactly match the version that is
                                                      							 defined in the JAD file. If you enter a version, the phone attempts to upgrade
                                                      							 or downgrade the MIDlet if the version is different than what is installed on
                                                      							 the phone. If the field is blank, the version gets retrieved from the Service URL . Leaving the field blank ensures that the phone attempts to download the JAD file every time that the phone reregisters to Unified Communications Manager as well as every time that the Cisco-signed Java MIDlet is launched; this ensures that the phone always runs the latest version
                                                      of the Cisco-signed Java MIDlet without you having to manually update the Service Version field. This
                                                						field displays as blank for Cisco-provided default services. You can
                                                						enter numbers and periods in this field (up to 16 ASCII characters). |
| Enable | Allows you to enable or disable the service without removing the configuration from Cisco Unified CM Administration (and without removing the service from the database). Uncheck
                                                						the check box to remove the service from the phone configuration file and the
                                                						phone. |
| Service Parameter
                                                   						  Information |
| Parameters | Lists the service parameters that apply to this IP phone service. Use the following buttons to configure service parameters
                                                for this pane: New
                                                         							 Parameter —Click this button to display the Configure Cisco Unified
                                                         								IP Phone Service Parameter window, where you configure a new service
                                                      							 parameter for this IP phone service. Edit
                                                         							 Parameter —Highlight a service parameter that is displayed in the Parameters pane, then click this button to display
                                                      							 the Configure Cisco Unified
                                                         								IP Phone Service Parameter window, where you can edit the selected
                                                      							 service parameter for this IP phone service. Delete Parameter —Highlight a service parameter that is displayed
                                                      							 in the Parameters pane, then click this button to delete a
                                                      							 service parameter for this IP phone service. A popup window asks you to confirm
                                                      							 deletion. |

| Note | Unified Communications Manager allows you to create two or more IP phone services with identical names. Cisco recommends that you do not do so unless most
                                                         or all phone users are advanced, or unless an administrator always configures the IP phone services. Be aware that if AXL
                                                         or any third-party tool accesses the list of IP phone services for configuration, you must use unique names for IP phone services. |
|---|---|

| Note | When
                                                         						the service URL points to an external customized URL, you cannot localize the
                                                         						service name according to the device locale of the phone. The service name gets
                                                         						displayed in English alphabets only. |
|---|---|

| Note | If
                                                         						you do not provide a Secure-Service URL, the device uses the nonsecure URL. If
                                                         						you provide both a secure URL and a nonsecure URL, the device chooses the
                                                         						appropriate URL, based on its capabilities. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Phone Button Template for Manager Assistant | Perform this step to assign manage and assistant button features to line or speed dial keys. |
| Step 2 | Associate a Manager Assistant Button Template with a Phone | Perform this step to configure the manager and assistant button for a phone. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| Step 2 | Click Find to display list of supported phone templates. |
| Step 3 | Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step. Select a default template for the model of phone and click Copy . In the Phone Button Template Information field, enter a new name for the template. Click Save . |
| Step 4 | Perform the following steps if you want to add phone buttons to an existing template. Click Find and enter the search criteria. Choose an existing template. |
| Step 5 | From the Line drop-down list, choose 
                                             			 feature that you want  to add to the template. |
| Step 6 | Click Save . |
| Step 7 | Perform one
                                             			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find to display the list of configured phones. |
| Step 3 | Choose the
                                             			 phone to which you want to add the phone button template. |
| Step 4 | In the Phone
                                                				Button Template drop-down list, choose the phone button template
                                             			 that contains the new feature button. |
| Step 5 | Click Save . A
                                             			 dialog box is displayed with a message to press Reset to update the phone settings. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Click Find . The search result displays all the end users that are configured in Unified Communications Manager . |
| Step 3 | From the Related Links drop-down list, choose Manager Configuration and click Go . |
| Step 4 | Check the Automatic Configuration check box to automatically
                                          			 configure the softkey template and Auto Answer with Speakerphone for intercom
                                          			 line for the manager phone based on the Cisco IP Manager Assistant service
                                          			 parameters. Note Automatic Configuration for intercom applies only when the Unified Communications Manager Assistant intercom feature is used for the Cisco Unified IP Phones 7940 and 7960. | Note | Automatic Configuration for intercom applies only when the Unified Communications Manager Assistant intercom feature is used for the Cisco Unified IP Phones 7940 and 7960. |
| Note | Automatic Configuration for intercom applies only when the Unified Communications Manager Assistant intercom feature is used for the Cisco Unified IP Phones 7940 and 7960. |
| Step 5 | Check Uses
                                             				Shared Lines check box. |
| Step 6 | From the Device
                                             				Name/Profile drop-down list, choose the device name or device
                                          			 profile to associate a device name or device profile with a manager. Note If the
                                                      				manager telecommutes, check the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. When device
                                                      				profile is chosen, the manager must log in to the phone by using Cisco
                                                      				Extension Mobility before accessing Manager Assistant. See the
                                             				related topics for more information about Extension Mobility with Manager
                                             				Assistant. | Note | If the
                                                      				manager telecommutes, check the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. When device
                                                      				profile is chosen, the manager must log in to the phone by using Cisco
                                                      				Extension Mobility before accessing Manager Assistant. |
| Note | If the
                                                      				manager telecommutes, check the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. When device
                                                      				profile is chosen, the manager must log in to the phone by using Cisco
                                                      				Extension Mobility before accessing Manager Assistant. |
| Step 7 | From the Intercom Line drop-down list, choose the intercom
                                          			 line appearance for the manager, if applicable. The chosen intercom line applies to the Manager Assistant and Unified Communications Manager intercom features. |
| Step 8 | From the Assistant Pool drop-down list, choose the
                                          			 appropriate pool number (1 to 3). |
| Step 9 | Choose the
                                          			 name of the assistant from the Available Assistants selection box and move it
                                          			 to the Associated Assistants selection box by clicking the down arrow to assign
                                          			 an assistant to the manager. You can go to
                                          			 the Assistant Configuration window by highlighting the
                                          			 assistant name and clicking the View
                                             				Details link. |
| Step 10 | Choose the
                                          			 appropriate line from the Available Lines list box and move it to the Selected
                                          			 Lines list box by clicking the down arrow to configure the Manager Assistant
                                          			 controlled lines. Make
                                          			 sure that the controlled line is always the shared line DN. |
| Step 11 | Click Save . If you
                                          			 checked the Automatic Configuration check box and the service
                                          			 parameters are invalid, a message is displayed. Ensure that the service
                                          			 parameters are valid. After successful completion of the automatic
                                          			 configuration, the manager device resets. If you configured a device profile,
                                          			 the manager must log out and log in to the device for the changes to take
                                          			 effect. |

| Note | Automatic Configuration for intercom applies only when the Unified Communications Manager Assistant intercom feature is used for the Cisco Unified IP Phones 7940 and 7960. |
|---|---|

| Note | If the
                                                      				manager telecommutes, check the Mobile Manager check box and optionally choose a
                                                      				device profile from the Device Name/Profile drop-down list. When device
                                                      				profile is chosen, the manager must log in to the phone by using Cisco
                                                      				Extension Mobility before accessing Manager Assistant. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Click Find . The search result displays all the end users that are configured in Unified Communications Manager . |
| Step 3 | Click on the
                                          			 username to display user information for the chosen assistant. The End
                                             				User Configuration window is displayed. |
| Step 4 | From the Related Links drop-down list, choose Assistant Configuration and click Go . The Assistant Configuration window is displayed. The
                                          			 system automatically sets the softkey template and intercom line on the basis
                                          			 of the Cisco IP Manager Assistant service parameter settings when you check the Automatic Configuration check box. In addition, the
                                          			 system also sets Auto Answer with Speakerphone for intercom line. |
| Step 5 | From the Device Name drop-down list, choose the device name
                                          			 to associate with the assistant. |
| Step 6 | From the Intercom Line drop-down list, choose the incoming
                                          			 intercom line appearance for the assistant. |
| Step 7 | From the Primary Line drop-down list, choose the primary line
                                          			 for the assistant. To view
                                                				  existing manager configuration information, highlight the manager name in the Associated Managers list and click View Details . The Manager Configuration window is displayed. To
                                                				  return to the Assistant Configuration window, highlight the
                                                				  assistant name and click View Details link in the Manager Configuration window. In the Associated Manager selection list box, the name of
                                          			 the previously configured manager is displayed. |
| Step 8 | To associate
                                          			 the manager line to the assistant line, perform the following steps from the
                                          			 Manager Association to Assistant Line selection box: From the Available Lines drop-down list, choose the assistant
                                                				  line that will be associated with the manager line. From the Manager Names drop-down list, choose the
                                                				  preconfigured manager name for whom this proxy line will apply. From the Manager Lines drop-down list, choose the manager
                                                				  line for which this proxy line will apply. |
| Step 9 | Click Save . The
                                          			 update takes effect immediately. If you chose Automatic Configuration , the assistant device
                                          			 automatically resets. |

| Step 1 | From Cisco Unified CM Administration, choose Application > Plugins . The Find and List Plugins window is displayed. |
|---|---|
| Step 2 | Click Find . A list
                                          			 of installable application plug-ins is displayed. |
| Step 3 | Click on the Download link for Cisco Unified CM Assistant Console
                                          			 and save the executable to a location. |
| Step 4 | Run the
                                          			 executable file. Note If you install the application on a Windows Vista PC, a security window may be displayed. Allow the installation to continue. The Cisco
                                             				Unified CallManager Assistant Console installation wizard is
                                          			 displayed. | Note | If you install the application on a Windows Vista PC, a security window may be displayed. Allow the installation to continue. |
| Note | If you install the application on a Windows Vista PC, a security window may be displayed. Allow the installation to continue. |
| Step 5 | In the Introduction window, click Next . |
| Step 6 | In the License
                                             				Agreement window, click Next . |
| Step 7 | Choose a
                                          			 location where you want the application to install and click Next . Note By default,
                                                      				the application installs in C:\Program Files\Cisco\ Unified CallManager Assistant
                                                         				  Console . | Note | By default,
                                                      				the application installs in C:\Program Files\Cisco\ Unified CallManager Assistant
                                                         				  Console . |
| Note | By default,
                                                      				the application installs in C:\Program Files\Cisco\ Unified CallManager Assistant
                                                         				  Console . |
| Step 8 | In the Pre-installation Summary window, review the summary
                                          			 and click Install . The
                                          			 installation begins. |
| Step 9 | After the
                                          			 installation is complete, click Finish . |
| Step 10 | Provide the
                                          			 assistant the username and password that is required to log in to the console. |
| Step 11 | To launch the
                                          			 Assistant Console, click the desktop icon or choose Cisco Unified
                                                				  Communications Manager Assistant > Assistant Console from the Start...Programs menu. |
| Step 12 | The Advanced tab in the Cisco
                                             				Unified Communications Manager Assistant Settings window allows you
                                          			 to enable trace for the Assistant Console. |
| Step 13 | Provide the assistant with the port number and the IP address or hostname of the Unified Communications Manager server on which the Cisco IP Manager Assistant service is active. The first time that the assistant logs in to the console,
                                          the assistant must enter the information in the Cisco Unified Communications Manager Assistant Server Port and the Cisco Unified Communications Manager Assistant Server Hostname or IP Address fields. |

| Note | If you install the application on a Windows Vista PC, a security window may be displayed. Allow the installation to continue. |
|---|---|

| Note | By default,
                                                      				the application installs in C:\Program Files\Cisco\ Unified CallManager Assistant
                                                         				  Console . |
|---|---|

| Feature | Interaction |
|---|---|
| Bulk
                                          						Administration Tool | You can
                                          						use the Bulk Administration Tool to add many users (managers and assistants) at
                                          						once instead of adding users individually. The Bulk Administration Tool templates that the Cisco Unified CM Assistant Configuration Wizard creates for Cisco Unified IP Phones support only the Unified Communications Manager intercom lines. For more information, see the Bulk Administration Guide for Cisco Unified Communications Manager . |
| Calling
                                          						Party Normalization | Manager
                                          						Assistant automatically supports localized and globalized calls if you
                                          						configure the Calling Party Normalization feature. Manager Assistant can
                                          						display localized calling party numbers on the user interfaces. In addition,
                                          						for an incoming call to the manager, Manager Assistant can display localized
                                          						and globalized calling party numbers when filter pattern matching occurs. |
| Extension Mobility | You can
                                          						simultaneously use Manager Assistant with the Cisco Extension Mobility feature.
                                          						When you log in to the Cisco Unified IP Phone using Extension Mobility, the
                                          						Cisco IP Manager Assistant service is automatically enabled on that phone. You
                                          						can then access the Manager Assistant features. For
                                          						more information about Cisco Extension Mobility, see Extension Mobility Overview . |
| Internet
                                          						Protocol Version 6 (IPv6) | Manager
                                          						Assistant does not support IPv6, so you cannot use phones with an IP Addressing
                                          						Mode of IPv6 Only with Manager Assistant. To use Manager Assistant with the
                                          						phone, ensure that you configure the phone with an IP Addressing Mode of IPv4
                                          						Only or IPv4 and IPv6. |
| Reporting tools | Manager Assistant provides statistical information in the CDR
                                          						Analysis and Reporting (CAR) tool and provides a summary of changes to
                                          						configurations in a change log. The
                                          						administrator can view a summary of changes that are made to the Manager or
                                          						Assistant Configurations in Unified CM AssistantChangeLog*.txt. A manager can
                                          						change defaults by accessing the Manager Configuration from a URL. An assistant
                                          						can change the manager defaults from the Assistant Console. For information
                                          						about the URL and Manager Configuration, see the Cisco Unified Communications Manager Assistant User
                                             						  Guide . When
                                          						the manager or assistant makes changes, the changes are sent to a log file
                                          						called ipma_changeLogxxx.log . The log file resides on the server
                                          						that runs the Cisco IP Manager Assistant service. Use the following command to
                                          						obtain the log file: file get activelog
                                             						  tomcat/logs/ipma/log4j/ For
                                          						more information about downloading the log file, see the Cisco Unified Real -Time Monitoring Tool Administration
                                             						  Guide . |
| CDR
                                          						Analysis and Reporting | Manager Assistant supports call-completion statistics and inventory reporting for managers and assistants. The CAR tool supports
                                          call-completion statistics. Cisco Unified Serviceability supports inventory reporting. For
                                          						more information, see the following guides: Cisco Unified
                                                   								Serviceability Administration Guide Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager |
| Multilevel Precedence and Preemption (MLPP) | The
                                          						following points describe the interactions between Manager Assistant with
                                          						shared line support and MLPP: The
                                                							 system preserves call precedence in the handling of calls by Manager Assistant.
                                                							 For example, when an assistant diverts a call, the system preserves the
                                                							 precedence of the call. Filtering of precedence calls occurs in the same manner as all
                                                							 other calls. The precedence of a call will not affect whether a call is
                                                							 filtered. Because Manager Assistant does not have information about the
                                                							 precedence of a call, it does not provide any additional indication of the
                                                							 precedence of a call on the Assistant Console. |
| Intercom | Manager
                                          						Assistant supports the following two types of intercom: Manager Assistant intercom (used with Cisco Unified IP Phones
                                                							 7940 and 7960). You can configure this intercom feature using the DN
                                                							 configuration and end user (manager and assistant) configuration windows. Unified Communications Manager intercom (used with Cisco Unified IP Phones 7940 and 7960). You can configure this intercom feature using the intercom partition,
                                                intercom calling search space, intercom directory number, intercom translation pattern, DN, and end user (manager and assistant)
                                                configuration windows. |
| Message Waiting Indicator | The
                                          						Message Waiting Indicator feature interacts with proxy line support only. The
                                          						Message Waiting Indicator (MWI) on and off numbers should have the partition of
                                          						the manager line in their calling search space. The partition can exist in any
                                          						order of priority within each calling search space. |
| Time-of-Day Routing | The
                                          						Time-of-Day feature interacts with proxy line support only. Time-of-Day routing routes calls to different locations based on
                                          						the time that the call gets made; for example, during business hours, calls get
                                          						routed to a manager office, and after hours, the calls go directly to voicemail
                                          						service. For more information about Time-of-Day Routing, see the System Configuration Guide for Cisco Unified Communications Manager . |

| Feature | Restriction |
|---|---|
| Assistant
                                       					 Console Application | To install
                                       					 the Assistant Console application on a computer with Microsoft Internet
                                       					 Explorer 7 (or later), install the Microsoft Java Virtual Machine (JVM) before
                                       					 the Assistant Console installation. |
| Call
                                       					 Management features | The
                                       					 Assistant Console does not support hunt groups or queues, recording and
                                       					 monitoring, one-touch Call Pickup, and On-Hook transfer (the ability to
                                       					 transfer a call by pressing the Transfer softkey and going on hook to complete
                                       					 the transfer). |
| Cisco IP
                                       					 Phones | Manager
                                       					 Assistant supports SIP on Cisco Unified IP Phones 7900 Series, except for Cisco
                                       					 Unified IP Phones 7940 and 7960. Manager
                                       					 Assistant supports up to 3500 managers and 3500 assistants by configuring
                                       					 multiple Cisco IP Manager Assistant servers (pools). When you enable multiple
                                       					 pools, the manager and all configured assistants for that manager should belong
                                       					 to the same pool. Cisco Unified IP Phones 7960 and 7940 support only the Unified Communications Manager Assistant Intercom lines feature. Cisco Unified IP Phones 7900 (except 7940 and 7960) support only the Unified Communications Manager Intercom feature. One manager can have up to ten assigned assistants and one assistant can support up to 33 managers (if each manager has one Unified Communications Manager –controlled line). Only one assistant at a time can assist a manager. Manager Assistant supports up to 3500 managers and 3500 assistants per Unified Communications Manager cluster. |
| Intercom | After an upgrade, Manager Assistant users that use the incoming intercom line do not get upgraded automatically to the Unified Communications Manager Intercom feature. The system does not support calls between the Unified Communications Manager Intercom feature and regular lines (which may be configured as Manager Assistant Intercom lines). |
| Single
                                       					 Sign-On | Manager
                                       					 Assistant is not supported in the Single Sign-On environment. |
| Speed
                                       					 Dial | Cisco
                                       					 Unified IP Phones 7940, 7942, and 7945 support only two lines or speed-dial
                                       					 buttons. |

| Tool
                                          						Description | Location |
|---|---|
| Cisco
                                          						Unified CM Assistant server trace files | The
                                          						trace files reside on the server that runs the Cisco IP Manager Assistant
                                          						service. You can
                                          						download these files from the server using one of the following methods: Use
                                                							 the CLI command file get activelog tomcat/logs/ipma/log4j . Use
                                                							 the trace collection features in the Cisco Unified Real-Time Monitoring Tool
                                                							 (RTMT). For more information, see the Cisco Unified Real-Time Monitoring Tool Administration
                                                   								Guide . You can
                                          						enable debug tracing by choosing Cisco Unified
                                                							 Serviceability > Trace > Configuration . |
| Cisco
                                          						IPMA client trace files | $INSTALL_DIR\logs\ACLog*.txt on the client desktop, in the
                                          						same location where the Unified CM Assistant assistant console resides. To
                                          						enable debug tracing, go to the Settings dialog box in the Assistant Console. In the Advanced panel, check the Enable Trace check box. Note This
                                                   						check box enables only debug tracing. Error tracing always remains On. | Note | This
                                                   						check box enables only debug tracing. Error tracing always remains On. |
| Note | This
                                                   						check box enables only debug tracing. Error tracing always remains On. |
| Cisco
                                          						IPMA client install trace files | $INSTALL_DIR\InstallLog.txt on the client desktop, in the
                                          						same location where the Assistant Console resides. |
| Cisco
                                          						IPMA Client AutoUpdater trace files | $INSTALL_DIR\UpdatedLog.txt on the client desktop, in the
                                          						same location where the Unified CM Assistant Console resides. |
| Install
                                          						directory | By
                                          						default— C:\Program Files\Cisco\Unified Communications Manager Assistant
                                             						  Console\ |

| Note | This
                                                   						check box enables only debug tracing. Error tracing always remains On. |
|---|---|