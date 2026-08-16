---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-0a26f6aeed
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_uccx-125admin-and-operations-guide/uccx_b_uccx-125admin-and-operations-guide_chapter_01011.html
retrieved_at: 2026-08-16T21:45:21.534095+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Unified CCX Reporting

## Chapter: Unified CCX Reporting

# Unified CCX Reporting

## Reporting Administration on Unified CCX

### Import of Stock
                           	 Reports

If you import stock reports from Unified Intelligence Center, run the CLI utils uccx synctocuic permission all command to reset the permissions of the user groups. For more information, see utils uccx synctocuic command in the Cisco Unified Contact Center Express Administration and Operations Guide .

Do not create a sub-category under the Stock category as the permissions for the Stock category is automatically reset at midnight.

You can now
                                          		  rename the Stock Reports folder name.

### Unified CCX
                           	 Historical Reports

Historical reports
                              		are the preconfigured reports in Unified Intelligence Center. These reports
                              		access past data from the historical data source to display information for the
                              		specified period of time.

#### Unified CCX
                              	 Historical Datastore

In a Unified
                                    		  CCX Cluster, there can be one or more Historical datastores.

Support for High
                                                			 Availability and remote servers is available only in multiple-server
                                                			 deployments.

The
                                    		  Historical Unified CCX Datastore can be co-located with the Unified CCX.

In a Unified CCX
                                                			 High Availability server with co-resident Cisco Unified Intelligence Center,
                                                			 Cisco Unified Intelligence Center will intelligently point to the appropriate
                                                			 datasource. This will require no manual configuration during failover or in
                                                			 island mode scenario. For more information about Historical datastore, see Cisco Unified Contact
                                                         				  Center Express Serviceability Administration Guide .

#### Historical Reporting Configuration

The Unified CCX Historical Reporting subsystem provides you with a way to
                                    				set up and manage the purging of the Historical Reporting databases.

Setting up Unified CCX for Historical Reporting consists of the following
                                    				tasks:

Configure Automatic Purging

##### Configure Database Server Limits

To limit the performance impact of historical reporting on a
                                       		  particular Unified CCX server, you can configure a maximum number of five
                                       		  client/scheduler database connections per server.

To do so, complete the following steps:

Step 1

From the Unified CCXAdministration menu bar, choose Tools > Historical
                                                      				  Reporting > Database Server
                                                      				  Configuration .

Field

Description

Server Name

The hostname or IP Address of the database server.

Maximum DB Connections for Report Clients Sessions

The maximum number of client and scheduler connections that can access the Historical Reports Database server.

Standalone Setup—1 to 8 instances

High Availability Setup—1 to 16 instances

Step 2

Enter a value in the Maximum DB Connections for Report Client
                                                   			 Sessions field next to a Server Name.

Step 3

Click Update .

The configuration changes take effect.

##### View Historical Reports

You can view historical reports through the Unified Intelligence Center.

Choose Tools > User
                                                      				  Management > Reporting Capability
                                                      				  View

The User Configuration web page opens.

#### Purge of Historical
                              	 Data

As the
                                    		  Unified CCX Engine runs, it collects information about the status and
                                    		  performance of the Unified CCX system. Historical information is stored in a
                                    		  database that can then be accessed to provide reports.

When the
                                    		  database approaches its maximum size, some or all of the data in it must be
                                    		  removed. Removing data from a database is called purging .

When the
                                    		  system purges data, it removes data from the db_cra database. It determines
                                    		  what information to purge based on the number of months you specify and on the
                                    		  current date. For example, if you instruct the system to purge data older than
                                    		  12 months, a purge on January 15 will purge data older than January 15 of the
                                    		  previous year.

When you purge
                                                			 data, you permanently delete it. If you want to keep data that will be purged,
                                                			 back up the database.

Unified CCX
                                    		  Administration provides the following features for purging historical reports
                                    		  from the database:

Daily comparison
                                          				of the size of the database to a user-specified maximum size

User-specified
                                          				time at which the system purges data

Automatic
                                          				purging of the database when it exceeds the user-specified maximum sizes

Automatic
                                          				purging of the database based on user-specified parameters

Manual purging
                                          				of the database

Caution

Not configuring
                                                			 the Purge parameters may make your database to be overloaded with large number
                                                			 of records. This leads to call data not being written to database.

##### Configure Automatic Purging

The Unified CCXEngine performs automatic purging each day at a preset time.

To help keep your system running most efficiently, schedule automatic purging to run when your system is least busy. By default,
                                       daily purges are scheduled to run at 01:00 a.m. (01:00 Hrs), but you can change this time.

The system bases its purging activities on a variety of parameters. You can change the default value for any parameter as
                                       needed.

The following section contains the procedure for setting the daily purge schedule and auto purge.

###### Configure Purge
                                    	 Schedule Configuration Parameters

You can
                                          		  change the time of day that the system assesses the need to purge data and the
                                          		  age of data to purge.

When data
                                          		  is purged, the Unified CCX sends a "Database
                                             			 purged" message. This message announces that a purge has taken place and
                                          		  includes an explanation of the purging activity. If the database is approaching
                                          		  its maximum size, then the Unified CCX sends the following message - "Database
                                             			 approaching maximum size" .

The system
                                          		  can send notifications through the following two methods:

- Syslog (system log)

- SNMP traps

To set the
                                          		  purge schedule configuration parameters, complete the following steps.

Step 1

From the Unified
                                                   			 CCXAdministration menu bar, choose Tools > HistoricalReporting > Purge Schedule
                                                         				  Configuration .

The Purge
                                                      				Schedule Configuration area opens. The following fields are displayed in the
                                                      				Purge Schedule Configuration area.

Field

Description

Purge Schedule

Daily
                                                                  							 purge at

Time
                                                                  							 of day for the daily purge along with the time zone. The time that appears here
                                                                  							 is based on the primary time zone, which is specified during initial setup of
                                                                  							 Unified CCX Administration.

In a
                                                                  							 High Availability over WAN deployment, the purge schedule will happen at the
                                                                  							 time zone of the primary node.

Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions.

Purge
                                                                  							 data older than

Data
                                                                  							 can persist for a number of months before being purged.

Purge run time

The
                                                                  							 total duration for which the purge process should run.

Auto Purge Configuration

Initiate automatic purge when database exceeds

Percentage of the maximum database size at which an automatic
                                                                  							 purge is initiated (as compared to the total available size).

Initiate automatic purge when extent size exceeds

Percentage of the maximum extents size of any table above which
                                                                  							 an automatic purge is initiated.

Auto
                                                                  							 purge data for the oldest

Age of
                                                                  							 data to be purged.

Step 2

From the
                                                   			 drop-down list in the Daily purge at field, choose a time of day at which the
                                                   			 system determines if purging is necessary.

Step 3

From the
                                                   			 drop-down list in the Purge data older than field, choose the required number
                                                   			 of months.

If the system
                                                      				determines that purging is necessary, it will purge both databases of data that
                                                      				is older than the number of months specified in this field.

Step 4

From the
                                                   			 drop-down list in the Purge run time field, specify the required number of
                                                   			 hours.

If the system
                                                      				determines that purging is necessary, it will purge both databases of data
                                                      				within the specified duration of time.

Step 5

From the
                                                   			 drop-down list in the Initiate automatic purge when database size exceeds
                                                   			 field, accept the default, or choose another number.

Step 6

From the
                                                   			 drop-down menu in the Auto purge data for the oldest field, accept the default
                                                   			 of 15 , or
                                                   			 choose another number.

Step 7

From the
                                                   			 drop-down list in the initiate automatic purge when extent size exceeds field,
                                                   			 accept the default , or choose another number.

Step 8

Click Update icon that displays in the tool bar in the
                                                   			 upper, left corner of the window or the Update button that displays at the bottom of the
                                                   			 window.

The new purge
                                                      				schedule configuration is added to the Unified CCX system.

##### Purge
                                 	 Manually

You can
                                       		  manually purge the databases at any time. This action will not affect the
                                       		  automatic purging schedule.

Support for High
                                                   			 Availability is available only in multiple-server deployments.

To manually
                                       		  purge historical data, complete the following steps.

Step 1

From the Unified
                                                			 CCXAdministration menu bar, choose Tools > HistoricalReporting > Purge
                                                      				  Now .

The
                                                   				Purge Now web page opens. The Purge data older than field is displayed in the
                                                   				Purge Now web page. You can specify this field in months and days.

Step 2

From the
                                                			 drop-down list in the Purge data older than N months field, keep the default (13 months) or
                                                			 specify the required number of months.

If the system
                                                   				determines that purging is necessary, it will purge both databases of data that
                                                   				is older than the number of months specified in this field.

The Initiate
                                                   				automatic purge when database exceeds field displays the current historical
                                                   				database size as compared to the total available size.

Step 3

From the
                                                			 drop-down list in the Purge data older than N days field, keep the default (15 days) or specify
                                                			 the required number of days.

If the system
                                                   				determines that purging is necessary, it will purge both databases of data that
                                                   				is older than the number of days specified in this field.

Step 4

From the
                                                			 drop-down list in the Purge run time, keep the default (7 hours) or specify the
                                                			 required number of hours.

If the system
                                                   				determines that purging is necessary, it will purge both databases of data
                                                   				within the specified duration of the time .

Step 5

Click Purge
                                                   				Now .

The database
                                                   				purge is initiated in the server and the Purge Now area refreshes.

#### Unified CCX to Unified Intelligence Center Synchronization

The Unified CCX to Unified Intelligence Center synchronization runs as part of daily purge at midnight.

The following updates occur during the synchronization:

Based on the user role (agent, supervisor, or reporting user) configured in Unified CCX, the corresponding user  in Unified
                                          Intelligence Center gets added to the respective group (agent, supervisor or reporting group). The groups have predefined
                                          permissions for folders, reports and report definitions. If you edit the permissions manually in Unified Intelligence Center,
                                          these changes are reset to the predefined settings during the daily purge.

Unified CCX sets the group association for its users based on the highest level role (reporting user, supervisor or agent)
                                          for the user. Any custom group associations that may have been done on Unified Intelligence Center is retained.

Users created directly in the co-resident Unified Intelligence Center are removed. However, users created in the standalone
                                          Unified Intelligence Center are retained.

Custom user groups remain unchanged unless they refer to agent, supervisor, and reporting groups and these groups get reset
                                          during the synchronization.

#### File Restore

Use the File Restore menu option to restore the database
                                 		records written to HR files when the database goes down.

### Unified CCX
                           	 Real-Time Reports

When the
                                 		  Unified CCX system is configured and functioning, you can run reports to
                                 		  monitor real-time activity using the Unified CCXAdministration web interface.

To access Real-Time
                                 		  Reporting tools, you must configure the DNS client on your local machine .

If your local machine is
                                 		  not in the domain where Unified CCX resides, enter the hostnames in the local
                                 		  host file for the machines that house Unified CCX nodes.

You must
                                 		  be logged into the Unified CCX Administration web interface to run Unified CCX
                                 		  real-time reports.

#### Available Unified CCX Real-Time
                              	 Reports

Unified CCX real-time
                                    		  reporting provides real-time reports you can use to monitor Unified CCX system
                                    		  activity. The following table briefly describes each of these reports.

Report

Description

Application Tasks

Provides information about currently active applications.

Application Tasks Summary

Provides a summary of specific application activity.

Applications

Provides a list of all applications loaded on the Unified CCX server.

Contacts Summary

Provides information for call contacts, email contacts, and HTTP contacts. Also provides the total number of contacts.

Calls made by the Outbound subsystem will not be displayed in the Contacts Summary Real-Time Report.

Contacts

Provides information about currently active contacts.

Chat CSQ Cisco Unified Contact Center Express Stats

Provides information about Chat CSQ activity. This report is available only if Unified CCX has been configured.

Chat Resource Cisco Unified Contact Center Express Stats

Provides information about Chat Unified CCX resources activity.

CSQ Cisco Unified Contact Center Express Stats

Provides information about CSQ activity. This report is available only if Unified CCX has been configured.

Data Source Usage

Provides information about configured data source names (DSNs).

Engine Tasks

Provides information about currently active Engine tasks.

Preview Outbound Campaign Cisco Unified Contact Center Express Stats

Provides information about real-time Unified CCX information for the Outbound preview dialer.

Outbound Campaign Stats

Provides real-time statistics on IVR and agent based progressive and predictive Outbound campaigns since the statistics were
                                                last reset.

This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX.

Overall Outbound Stats

Provides real-time statistics across all IVR and agent based progressive and predictive Outbound campaigns since the statistics
                                                were last reset.

This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX.

Overall Chat Cisco Unified Contact Center Express Stats

Provides information about Chat Unified CCX resources and contact information. This report is available only if Unified CCX
                                                has been configured.

Overall Cisco Unified Contact Center Express Stats

Provides information about Unified CCX resources and calls. This report is available only if Unified CCX has been configured.

Resource Cisco Unified Contact Center Express Stats

Provides information about Unified CCX resources activity.

Sessions

Provides information on all active sessions.

##### Related
                                    		  Topic

Report Menu

#### Open Real-Time
                              	 Reports

Real-Time
                                    		  reporting is available from the Unified CCX Administration web interface.

Real-Time Reporting requires the Java plug-in. If the Java plug-in is not already installed on the PC on which you are viewing
                                    the reports, the Unified CCX system automatically installs it when you choose Tools > Real Time Reporting Tool .

Use Mozilla Firefox and Internet Explorer for Real Time Reporting.

If you are using Mozilla Firefox, you must manually install the correct version of JRE to use real-time reports.

The
                                    		  Application Reporting web page is a stand-alone component of the Unified CCX Administration interface. It has its own menu bar, which replaces the Unified CCX Administration menu bar.

To open
                                    		  real-time reporting, complete the following steps.

Step 1

If you are
                                             			 running Real-Time Reporting for the first time on this system, log into Unified CCX Administration as an Administrator .

The system
                                                				prompts you to download the Java plug-in; follow the prompt instructions.

After you
                                                            				  perform the initial download of the Real-Time Reporting Java plug-in,
                                                            				  non-Administrative users can access Real-Time Reporting on this system.

Step 2

Choose Tools > Real-Time
                                                   				  Reporting from the Unified CCX Administration menu bar.

The
                                                				Application Reporting web page opens in a new window. The real-time reporting
                                                				tool requires a Java plug-in. If the plug-in is not installed on the machine
                                                				you are using, the Unified CCX system
                                                				prompts you to accept the automatic installation of the plug-in. If you do not
                                                				accept the installation, you cannot use real-time reporting.

#### Run
                              	 Reports

Open the
                                    		  real-time reporting tool from the Unified CCX Administration web interface to run reports.

To run a
                                    		  real-time report, complete the following steps.

Step 1

From the
                                             			 Application Reporting menu bar, choose Reports .

Step 2

From the
                                             			 Reports menu, choose the report to run.

The report
                                                				opens in the Application Reporting window.

#### View Detailed Subreports

You can view more detailed information for selected items in
                                    		  these four reports:

- Application Tasks report

- Contacts report

- Applications report

- Sessions report

To view detailed subreports, complete the following steps.

Step 1

Run the Application Tasks, Contacts, Applications, or Sessions
                                             			 report.

Step 2

Click a line in the report for which you want to view more
                                             			 detailed information. For example, click an email address in the Contacts
                                             			 report.

Step 3

From the Application Reporting menu bar, choose Views and click the subreport that you want to
                                             			 run.

You can also open a subreport by right-clicking the selected item
                                                				and choosing a subreport.

The subreport opens.

#### Print Reports

To facilitate printing, you can open a printable version of a
                                    		  report.

To print a report, complete the following steps.

Step 1

Run a report.

Step 2

From the Application Reporting menu, choose Tools > Open Printable
                                                   				  Report .

A printable version of the report opens in a separate window.

Step 3

Print the report using your browser print functionality.

#### Reset Report
                              	 Statistics

The Unified CCX system
                                    		  automatically resets all statistics each day at midnight. You can reset the
                                    		  accumulated statistics manually at any time. Resetting statistics does not
                                    		  reset active statistics, such as active contacts and active tasks.

To reset
                                    		  report statistics, complete the following steps.

Step 1

From the
                                             			 Application Reporting menu bar, choose Tools > Reset All
                                                   				  Stats .

The Reset
                                                				Stats dialog box opens for you to confirm the reset.

Step 2

Click Yes .

Accumulated
                                                				statistics are reset.

#### Clear Contact Option for Stuck Calls

You may sometimes see a Contact/Call as waiting in Real Time
                                    		  Reports in CSQ Stats, and even though there are available Agents in the queue,
                                    		  the call does not seem to get routed to these Agents. The waiting time for the
                                    		  Queued call accumulates and will not clear even if the user activates "Reset All Stats" option from the Real-Time Reporting menu.

To enable clearing such stuck call entries from the system,
                                    		  Unified CCX system provides the Clear Contact option. This has the ability to
                                    		  clear stuck calls in the system without requiring a restart of the engine.

#### Set Report
                              	 Options

You can
                                    		  set the following reporting options:

- Refresh interval

- Number of times that the Unified CCX Administration web interface should attempt to reconnect to the Unified CCX server

- Whether logged off users
                                       			 appear in reports

To set
                                    		  report options, complete the following steps.

Step 1

From the
                                             			 Application Reporting menu bar, choose Settings > Options .

The Options
                                                				dialog box opens.

Step 2

From the
                                             			 Polling Interval drop-down menu, choose the refresh rate in seconds.

Step 3

From the
                                             			 Server Connect Retry Count drop-down menu, choose the number of times that the Unified CCX Administration web interface should attempt to reconnect to the Unified CCX server.

Step 4

From the Show
                                             			 Logged Off Resources drop-down menu, choose whether logged-off agents appear in
                                             			 reports.

Step 5

Click Apply to apply the settings.

#### Set Report Appearance

You can select from three report appearances:

- Windows, which displays
                                       			 reports in colors based on your Windows settings

- Motif, which displays
                                       			 reports in purple and menu items in brown

- Metal, which displays
                                       			 reports in grey and menu items in black

To set the report appearance:

Choose Settings from the Application Reporting menu bar
                                             		  and click the appearance that you want.

#### Application
                              	 Reporting User Interface

Support for High
                                                			 Availability and remote servers is available only in multiple-server
                                                			 deployments.

When you
                                    		  choose Tools > Real-Time
                                          				Reporting from the Unified CCX Administration menu, the Application Reporting tool opens a web page
                                    		  in a new window.

The
                                    		  Application Reporting tool menu bar contains the following options:

Report —Choose this
                                          				option to display a list of the available top-level real-time reports.

Tools —Choose this
                                          				option to reset all the statistics and refresh connections.

Settings —Choose this
                                          				option to set the look and feel of the real-time Reporting client, set the
                                          				polling (refresh) interval times, and set the amount of times the server will
                                          				attempt to reconnect.

Help —Choose this option
                                          				to display system information and to access Unified CCX online help.

##### Report
                                 	 Menu

All real-time
                                                   			 reports display a Last Updated
                                                      				At field, which indicates the time of the snapshot. All summary reports
                                                   			 display both a start time (which indicates when the summary statistics started
                                                   			 being collected) and the current time. All real-time reports display a
                                                   			 Connected or Not Connected status for each node in the cluster.

The
                                       		  Report menu provides access to a variety of top-level reports. It contains the
                                       		  following menu options:

###### High Availability
                                    	 (HA) Setup

In an HA
                                          		  setup, real-time reports obtain data from both nodes in the cluster.

Support for High Availability and remote servers is available
                                                            				  only in multiple-server deployments.

In case of island mode where each node (on either side of the
                                                            				  network) assumes mastership and handles calls, the real-time reports may not
                                                            				  report accurate data.

Failover
                                          		  in a two-node cluster is available for Unified IP IVR reports as described in
                                          		  the following table.

Failover
                                                      						Scenario

Connection Status

Node 1
                                                      						Status

Node 2
                                                      						Status

Both
                                                      						nodes are up

Fully
                                                      						Connected

Node ID
                                                      						current/start-time

Node ID
                                                      						current/start-time

Node 1
                                                      						is up

Node 2
                                                      						is down

Partially Connected

Node ID
                                                      						current/start-time

Node ID
                                                      						Not Connected

Node 1
                                                      						is down

Node 2
                                                      						is up

Partially Connected

Node ID
                                                      						Not Connected

Node ID
                                                      						current/start-time

Both
                                                      						nodes are down

Not
                                                      						Connected

Node ID
                                                      						Not Connected

Node ID
                                                      						Not Connected

Unified
                                          		  CCX real-time reports obtain data only from the current master node—failover in
                                          		  a two-node cluster is available as described in the following table.

Failover
                                                      						Scenario

Connection Status

Node 1
                                                      						Status

Node 2
                                                      						Status

Both
                                                      						nodes are up Node 1 is master

Fully
                                                      						Connected

Node ID
                                                      						current/start-time

Node ID
                                                      						Not Connected

Node 1
                                                      						is master

Node 2
                                                      						is down

Fully
                                                      						Connected

Node ID
                                                      						current/start-time

Node ID
                                                      						Not Connected

Node 1
                                                      						is down

Node 2
                                                      						is master

Fully
                                                      						Connected

Node ID
                                                      						Not Connected

Node ID
                                                      						current/start-time

Both
                                                      						nodes are down

Not
                                                      						Connected

Node ID
                                                      						Not Connected

Node ID
                                                      						Not Connected

###### Contacts Summary
                                    	 Real-Time Report

Use the
                                          		  Contacts Summary report to view specific contact information for call contacts,
                                          		  email contacts, HTTP contacts, and total number of contacts.

To
                                          		  access the Contacts Summary real-time report, choose Reports > Contacts
                                                				Summary from the Application Reporting menu bar.

You display the
                                                      			 data on this report as numbers or percentages by clicking the Display
                                                      			 Value/Display % toggle button.

The
                                          		  following fields are displayed on the Contacts Summary report.

Field

Description

Active

Active
                                                      						contacts that are currently running.

Inbound

Number
                                                      						of inbound contacts since the statistics were last reset.

Outbound

Number
                                                      						of outbound contacts since the statistics were last reset.

Connected

Number
                                                      						of connected contacts since the statistics were last reset.

Provides
                                                      						a total for contacts that are connected to resources (for example, a call
                                                      						connected to an ACD agent).

Terminated

Number
                                                      						of terminated contacts since the statistics were last reset.

This row reports contacts that are ended generally by the application (for example, a caller stops responding and the application
                                                      terminates), indicating whether the contact was terminated:

Locally—On the local server.

Remotely—On a remote server in the cluster.

Use
                                                                  						  the + toggle button to access these statistics.

Rejected

Number of rejected contacts since the statistics were last reset.

This row reports contacts that are not accepted and processed (as a result, for example, of insufficient resources or the
                                                      rejection of the contact based on some customer-defined logic). Indicates the reason code for the reject:

Channels busy

No channel license

No trigger

Use the + toggle button to access these statistics.

Aborted

Number
                                                      						of aborted contacts since the statistics were last reset.

This row
                                                      						reports contacts improperly ended by a task associated with the application (as
                                                      						when, for example, the system generates an exception or can not invoke the
                                                      						application because of some error in the application) and includes the
                                                      						associated Java exception code.

Java
                                                                  						  exception codes are dynamic, as they can be generated from a variety of
                                                                  						  sources.

Use
                                                                  						  the + toggle button to access these statistics.

Handled

Number
                                                      						of handled contacts since the statistics were last reset.

This row
                                                      						reports contacts that are explicitly marked "Handled" by the application (typically when the application
                                                      						connects the contact to a Unified CCX agent).

Abandoned

Number
                                                      						of abandoned contacts since the statistics were last reset.

This row
                                                      						reports contacts that end without being marked "Handled" by the application.

###### Application Tasks
                                    	 Summary

Use the
                                          		  Application Tasks Summary report to display statistics that summarize the
                                          		  activity of specific applications.

To
                                          		  access the Application Tasks Summary real-time report, choose Reports > Application Tasks
                                                				Summary from the Application Reporting menu bar.

The
                                          		  following fields are displayed on the Application Tasks Summary report.

Field

Description

Application Name

Names of
                                                      						the applications that are running or have run.

Running

Currently running applications.

Completed

Applications that have stopped running.

Total

Number
                                                      						of times an application was invoked since the statistics were last reset.

DTMF VB
                                                      						and AA

Application names configured from the Unified CCX
                                                      						Administration.

Status

Displays
                                                      						the failover connection status. The possibilities are: Fully connected,
                                                      						Partially connected, and Not connected. See the following tables for detailed
                                                      						status information for Unified IP IVR and Unified CCX reports.

###### Application Tasks
                                    	 Real-Time Report

Use the
                                          		  Application Tasks real-time report to view information about currently active
                                          		  applications.

To
                                          		  access the Application Tasks report, choose Reports > Application
                                                				Tasks from the Application Reporting menu bar. The
                                          		  following fields are displayed on the Application Tasks report.

Field

Description

ID

Unique
                                                      						application task ID.

Node ID

Unique
                                                      						ID for a server in the cluster.

Application

Name of
                                                      						the application.

Start
                                                      						Time

Time
                                                      						when the application task started.

Duration

Length
                                                      						of time that the application has been active.

If this report
                                                      			 indicates that an application is running for an unusually long time, there may
                                                      			 be a problem with the application. The application script may not include error
                                                      			 handling that prevents infinite retries if a call is no longer present. If the
                                                      			 application does not receive a disconnect signal after a call, the application
                                                      			 repeatedly retries to locate the call, and causes the application to run for an
                                                      			 unusually long time. To prevent this problem, include the proper error handling
                                                      			 in the application script.

###### Engine Tasks
                                    	 Real-Time Report

Use the
                                          		  Engine Tasks real-time report to view information about currently active Engine
                                          		  tasks.

To
                                          		  access the Engine Tasks report, choose Reports > Engine
                                                				Tasks from the Application Reporting menu bar.

The
                                          		  following fields are displayed on the Engine Tasks report.

Field

Description

ID

Unique
                                                      						identifier of the engine task.

If the
                                                      						engine task is the main task running the application and the parent ID is
                                                      						empty, its identifier will match the Application Task Identifier.

Parent
                                                      						ID

Unique
                                                      						identifier for the parent of the engine task (if any).

Node ID

Unique
                                                      						identifier for a server in the cluster.

Server
                                                      						IP Address

IP
                                                      						address identifying the server in the cluster.

Script

Name of
                                                      						the script that is running the task (if the task is running a Unified CCX script).

Start
                                                      						Time

Time
                                                      						that the task started.

Duration

Length
                                                      						of time the task has been active.

###### Contacts
                                    	 Report

Use the
                                          		  Contacts real-time report to view information for all the active contacts for
                                          		  all servers across clusters .

Support for High
                                                      			 Availability and remote servers is available only in multiple-server
                                                      			 deployments.

To
                                          		  access the Contacts report, choose Reports > Contacts from the Application
                                          		  Reporting menu bar.

You can
                                          		  access detailed information about specific contacts listed on the Contacts web
                                          		  page by performing one of the following procedures:

Call Contacts Detailed Info Report

Email Detailed Info Report

HTTP Detailed Info Report

The
                                          		  following fields are displayed on the Contacts report.

Field

Description

ID

Unique
                                                      						identifier representing a contact.

Type

Type of
                                                      						contact: Unified CM Telephony call, Cisco agent call, or

Impl ID

Unique
                                                      						identifier provided by the particular type of contact. For example, for a call
                                                         						  contact, this identifier would represent the Unified CM global
                                                         						  call ID.

Node ID

Unique
                                                      						identifier for a server in the cluster.

Start
                                                      						Time

Time
                                                      						stamp when the contact was created.

Duration

Length
                                                      						of time that the contact is active.

Handled

If True,
                                                      						the contact is handled; if False, the contact is not handled.

Aborting

If True,
                                                      						the contact is aborted with a default treatment; if False, the contact is not
                                                      						aborted.

Application

Name of
                                                      						the application currently managing the contact.

Task

Unique
                                                      						identifier of the application task that is currently responsible for the
                                                      						contact.

Session

Unique
                                                      						identifier of the session currently managing the contact (if any).

The information
                                                      			 displayed is dependent on the type of contact selected. Depending on the type
                                                      			 of call, some fields may not be supported and will appear blank.

###### Call Contacts
                                       	 Detailed Info Report

Use the
                                             		  Call Contacts Detailed Info real-time report to view all information related to
                                             		  the call contact.

To
                                             		  access the Call Contacts Detailed Info report, right-click a specific call
                                             		  contact record on the Contacts report; information for that specific record
                                             		  displays.

The
                                             		  following fields are displayed on the Call Contacts Detailed Info report.

Field

Description

State

Current
                                                         						state of the contact.

Inbound

If True,
                                                         						this call was received by the Unified CCX server; if False,
                                                         						this call was placed as an outbound call by an application.

Language

The
                                                         						selected language context of the call.

Application ID

Unique
                                                         						identifier of the associated application.

Called
                                                         						Number

Called
                                                         						number for this call leg from the perspective of the called party.

Dialed
                                                         						Number

Dialed
                                                         						number for this call leg from the perspective of the calling party.

Calling
                                                         						Number

Calling
                                                         						number of the originator of this call.

ANI

Automatic number identification.

DNIS

Dialed
                                                         						number identification service.

CLID

Caller
                                                         						ID.

Arrival
                                                         						Type

Information on how the call contact arrived in the system.

Last
                                                         						Redirected Number

Number
                                                         						from which the last call diversion or transfer was invoked.

Original
                                                         						Called Number

Originally called number.

Original
                                                         						Dialed Number

Originally dialed number.

ANI
                                                         						Digits

Automatic Number Identification information indicator digit
                                                         						codes.

CED

Entered
                                                         						digits that were gathered by the network before the call was received.

###### Email Detailed
                                       	 Info Report

Use the
                                             		  Email Detailed Info real-time report to view all information related to the
                                             		  email contact.

To
                                             		  access the Email Detailed Info report, right-click a specific email contact
                                             		  record on the Contacts report; information for that specific record displays.

The
                                             		  following fields are displayed on the Email Detailed Info report.

Field

Description

State

Current
                                                         						state of the contact.

Inbound

If True,
                                                         						this email message was received by the Unified CCX server; if False,
                                                         						this email was created by an application.

Inbound email messages are not currently supported.

Language

Selected
                                                         						language context of the email message.

Application ID

Unique
                                                         						identifier of the associated application.

From

Sender
                                                         						of this email message.

To

All the
                                                         						recipients of this email message.

Subject

"Subject" field of this
                                                         						email message.

Attachments

List of
                                                         						all attachments (file names) associated with this email message.

###### HTTP Detailed Info
                                       	 Report

Use the
                                             		  HTTP Detailed Info real-time report to view all information related to the HTTP
                                             		  contact.

To
                                             		  access the HTTP Detailed Info report, right-click a specific HTTP contact
                                             		  record in the Contacts report; information for that specific record displays.

The
                                             		  following fields are displayed on the HTTP Detailed Info report.

Field

Description

State

Current
                                                         						state of the contact.

Inbound

If True,
                                                         						this HTTP request was received by the Unified CCX server; if False,
                                                         						this HTTP request was created by an application.

This
                                                                     						  information will always be reported as True, because the Unified CCX server does not
                                                                     						  currently track outbound HTTP requests in this way.

Language

Language
                                                         						currently associated with the HTTP request.

Application ID

Unique
                                                         						identifier of the associated application.

Authentication Type

Name of
                                                         						the authentication scheme used to protect the servlet; for example, "BASIC" or "SSL."

Character Encoding

Length,
                                                         						in bytes, of the request body, which is made available by the input stream, or
                                                         						-1 if the length is not known.

This
                                                                     						  length is the same as the value of the CGI 1 variable CONTENT_LENGTH.

Content
                                                         						Length

MIME
                                                         						type of the body of the request, or null if the type is not known.

This
                                                                     						  is the same as the value of the CGI variable CONTENT_TYPE.

Content
                                                         						Type

Type of
                                                         						HTTP contact request.

Request
                                                         						Language

Preferred language for client content (the language that the
                                                         						client accepts for its content), based on the Accept-Language header.

Path
                                                         						Info

Any
                                                         						extra path information associated with the URL the client sent when the HTTP
                                                         						request was made.

Protocol

Name and
                                                         						version of the protocol the request uses in the form: protocol/majorVersion.minorVersion ; for example,
                                                         						HTTP/1.1

This
                                                                     						  value is the same as the value of the CGI variable SERVER_PROTOCOL.

Remote
                                                         						Address

IP
                                                         						address of the client that sent the request

This
                                                                     						  value is the same as the value of the CGI variable REMOTE_ADDR.

Remote
                                                         						Host

Fully
                                                         						qualified name of the client that sent the request, or the IP address of the
                                                         						client, if the name cannot be determined

This
                                                                     						  value is the same as the value of the CGI variable REMOTE_HOST.

Remote
                                                         						User

Login
                                                         						of the user making this request, if the user has been authenticated.

Requested Session ID

HTTP
                                                         						session ID as specified by the client.

Request URL

Section of the URL of the HTTP request, from the protocol name
                                                         						up to the query string in the first line of the HTTP request.

###### Applications
                                    	 Report

Use the
                                          		  Applications real-time report to view all the applications loaded on the
                                          		  server.

To
                                          		  access the Applications report, choose Reports > Applications from the Application
                                          		  Reporting menu bar.

The
                                          		  following fields are displayed on the Applications report.

Field

Description

Name

Unique
                                                      						name of the currently loaded application.

ID

Application ID.

Type

Type of
                                                      						application that is currently running (for example, a Cisco Script
                                                      						Application).

Description

Description of the application as entered on the Unified CCX Administration web site.

Enabled

If True,
                                                      						the application is enabled; if False, the application is disabled.

Max.
                                                      						Sessions

Maximum
                                                      						number of simultaneous task instances that can run simultaneously on the Unified CCX server.

Valid

If True,
                                                      						the application is valid; if False, the application is invalid. 2

###### Sessions
                                    	 Report

Use the
                                          		  Sessions real-time report to view real-time information on all the active
                                          		  sessions.

To
                                          		  access the Sessions report, choose Reports > Sessions from the Application
                                          		  Reporting menu bar.

The
                                          		  following fields are displayed on the Sessions report.

Field

Description

ID

Session
                                                      						ID.

This
                                                                  						  identifier is guaranteed to remain unique for a period of 12 months.

Mapping
                                                      						ID

User- or
                                                      						system-defined identifier that maps to this session.

Node ID

Unique
                                                      						identifier for a server in the cluster.

Parent

Sessions
                                                      						that were created as a result of consult calls propagated in the system.

Creation
                                                      						Time

Creation
                                                      						time of the session.

State

Current
                                                      						state of the session.

When
                                                                  						  marked IDLE, the session is subject to being "garbage collected" by the system after a specified period of
                                                                  						  time. In addition, a session is IN_USE if it still has a contact associated or
                                                                  						  a child session.

Idle
                                                      						Time

Length
                                                      						of time that the session has been idle.

###### Data Source Usage Report

Use the Data Source Usage real-time report to view real-time
                                          		  information on all configured Data Source Names (DSNs).

To access the Data Source Usage report, choose Reports > Datasource
                                                				Usage from the Application Reporting menu bar.

The following fields are displayed on the Data Source Usage
                                          		  report.

Field

Description

Data Source Name

Name of the data source, as configured through the Unified
                                                      						CCXAdministration web interface.

Available Connections

Number of connections available.

Busy Connections

Number of busy connections.

Busy + available = Maximum number of connections
                                                                  						  configured.

Checkouts Granted

Number of times the database connections have been used up
                                                      						since the statistics were last reset.

Checkouts Denied

Number of times the Database connections have been denied
                                                      						since the statistics were last reset.

###### Overall Cisco
                                    	 Unified Contact Center Express Stats Report

Use the
                                          		  Overall Cisco Unified Contact Center Express Stats real-time report to view
                                          		  real-time Unified CCX resource and call information.

Unified CCX
                                                      			 reports contain information for calls that have been queued in one or more
                                                      			 CSQs. If a call is not queued (for example, the caller hangs up before being
                                                      			 queued), the reports do not display data for that call.

Unified
                                          		  CCX reports retrieve the following statistics:

Unified CCX
                                                				statistics from the current Master node.

Unified IP IVR
                                                				statistics from all nodes in the cluster.

To
                                          		  access the Overall Unified CCX Stats report, choose Reports > Overall Cisco Unified Contact Center Express
                                                				Stats from the Application Reporting menu bar.

Preview Outbound
                                                      			 durations are updated when the preview outbound call disconnects and all agents
                                                      			 (resources) involved in the call move out of the Work and Talking state.

The
                                          		  following fields are displayed on the Overall Cisco Unified Contact Center
                                          		  Express Stats report.

Field

Description

Resource Information

CSQs

Number
                                                      						of CSQs currently configured. If a CSQ is added or removed, this statistic
                                                      						reflects that change.

Logged-in Resources

Number
                                                      						of resources currently logged in.

Talking
                                                      						Resources

Number
                                                      						of resources currently talking.

This
                                                                  						  number includes resources in Talking, Work, and Reserved states.

Ready
                                                      						Resources

Number
                                                      						of resources currently ready.

Not
                                                      						Ready Resources

Number
                                                      						of resources currently not ready.

Call Information —
                                                         						  Inbound

Total
                                                      						Contacts

Number
                                                      						of total contacts that have arrived since the statistics were last reset. This
                                                      						includes contacts that are waiting, contacts connected to a resource, and
                                                      						contacts that have disconnected.

If a
                                                      						resource transfers to or conferences with a route point, this value increases.

Contacts
                                                      						Waiting

Number
                                                      						of contacts waiting to be connected to a resource.

A
                                                                  						  contact is shown as waiting until the call is answered by the agent. This means that, even if the phone is
                                                                  						  ringing at the agent, the contact will still show as waiting in RTR.

Oldest Contact in Queue

Displays the wait time for the oldest contact in the queue.

Contacts
                                                      						Handled

Number
                                                      						of contacts that have been handled by a resource.

Contacts
                                                      						Abandoned

Number
                                                      						of contacts that have arrived and disconnected before being connected to a
                                                      						resource.

Avg Talk
                                                      						Duration

Average
                                                      						duration (in seconds) that resources spend talking on Unified CCX contacts.
                                                      						Talk duration starts when a contact first connects to a resource and ends when
                                                      						the contact disconnects from the last resource to which it was connected.

Talk
                                                      						duration does not include hold time.

Avg
                                                      						Wait Duration

Average wait time (in seconds). It begins when the contact
                                                      						enters the system and ends when the contact stops waiting. Wait duration does
                                                      						not include hold time. The time a contact spends on a CTI port prior to getting
                                                      						queued is included in this report.

Longest Talk Duration

Longest talk duration (in seconds) of a contact. Talk duration
                                                      						does not include hold time.

Longest Wait Duration

Longest wait (in seconds) for a contact to be connected to a
                                                      						resource. Wait duration does not include hold time.

Call Information —
                                                         						  Preview Outbound

Active

Total
                                                      						number of preview outbound calls currently previewed or connected to agents.

Preview

Total
                                                      						number of preview outbound calls currently previewed but have not been
                                                      						accepted, rejected. or closed by the agents.

Connected

Total
                                                      						number of preview outbound calls currently connected to agents. When an agent
                                                      						conferences in other agents, the call is counted once towards the total number
                                                      						of connected calls.

Offered

Total
                                                      						number of preview outbound calls offered. A call is considered offered when it
                                                      						is presented to an agent. A contact that is presented to an agent,
                                                      						skipped/rejected by that agent, and then presented to the same agent or to
                                                      						another agent is counted twice towards the number of calls offered. Offered =
                                                      						Accepted + Rejected + Closed + Timed-out.

Accepted

Total
                                                      						number of preview outbound calls accepted. A call is considered accepted if an
                                                      						agent has clicked Accept when presented the call. A call that is presented to
                                                      						an agent, skipped/rejected by that agent, presented to another agent, and then
                                                      						accepted by that other agent is counted once towards the number of calls
                                                      						accepted.

Rejected

The
                                                      						number of preview outbound calls that were skipped or rejected by an agent.
                                                      						This means that the agent selected Reject, Skip, or Cancel Reservation. These
                                                      						contacts will be dialed again. If a contact is rejected by multiple agents,
                                                      						this field increments each time the contact is rejected.

The
                                                      						number Rejected is also incremented each time an agent drops the preview call
                                                      						while it is ringing at the customer’s contact.

Closed

The
                                                      						number of preview outbound contacts that were closed by agents. This means that
                                                      						the agent selected Skip-Close or Reject-close. These contacts will not be
                                                      						dialed again.

Timed-Out

Total
                                                      						number of preview outbound calls that timed out. A call is considered timed out
                                                      						when it is presented to an agent and not accepted, rejected, or closed within
                                                      						the allocated time. These contacts will be dialed again. If a contact timed out
                                                      						multiple agents, this field is incremented each time the contact is timed out
                                                      						for each agent.

Invalid Number

The
                                                      						number of preview outbound calls that were dialed to an invalid number. This
                                                      						means that the agent accepted the call (by clicking Accept), got connected to
                                                      						the customer, and selected the Invalid Number option from the contact
                                                      						Reclassification drop down. It also includes the number of preview outbound
                                                      						calls that failed at the network level.

The
                                                                  						  agent can manually reclassify the contact as Invalid Number while the customer
                                                                  						  contact is on the call or when the agent has gone into the Work state after the
                                                                  						  call.

Voice

The
                                                      						number of preview outbound calls that ended in successful customer contact.
                                                      						This means that an agent accepted the call (by clicking Accept) and selected a classification of Voice (default) or Do Not
                                                      						Call for this contact.

Answering Machine

The
                                                      						number of preview outbound calls that connected to an answering machine for
                                                      						this campaign. This means that the agent accepted the call (by clicking
                                                      						Accept), got connected to the answering machine and selected the Answering
                                                      						Machine option from the contact Reclassification drop down.

The
                                                                  						  agent can manually reclassify the contact as Answering Machine while the
                                                                  						  customer contact is on the call or when the agent has gone into the Work state
                                                                  						  after the call.

Requested Callback

The
                                                      						number of contacts marked for callback. This means that the agent accepted the
                                                      						call (by clicking Accept), got connected to the contact, the contact requested
                                                      						a callback, and the agent selected the CallBack option. A call that is accepted
                                                      						by an agent, marked for callback, later presented to and accepted by another
                                                      						agent (at the callback time), and marked for callback again is counted twice
                                                      						towards the number of callback calls.

Avg Outbound Talk Duration

The average time in HH:MM:SS (hours, minutes, seconds) that
                                                      						agents spend talking on outbound calls. The durations consider all calls that
                                                      						were Agent Accepted and classified as Voice. If a preview outbound call is
                                                      						transferred or conferenced to a route point, this average outbound talk
                                                      						duration does not include the talk time of agents who handle the call after it
                                                      						came through the route point. Instead, the talk time is included in the inbound
                                                      						talk duration.

Longest Outbound Talk Duration

The longest talk duration of a preview outbound call in
                                                      						HH:MM:SS (hours, minutes, seconds). The durations consider all calls that were
                                                      						Agent Accepted and classified as Voice.

###### CSQ Cisco Unified Contact Center Express Stats Report

Use the CSQ Cisco Unified Contact Center Express Stats
                                          		  real-time report to view real-time information.

Unified CCX reports contain information for calls that have been
                                                      			 queued in one or more CSQs. If a call is not queued, the reports do not display
                                                      			 data for that call. .

To access the CSQ Cisco Unified Contact Center Express Stats
                                          		  report, choose Reports > CSQ Cisco Unified
                                                				Contact Center Express Stats from the Application
                                          		  Reporting menu bar.

The following fields are displayed on the CSQ Cisco Unified
                                          		  Contact Center Express Stats report.

Field

Description

Name

Name of the CSQ.

Talking/Ready Resources/Not Ready Resources/Logged-In
                                                      						Resources

Number of resources who are in the talking, ready, and not
                                                      						ready states, and the number of resources logged in for this CSQ. Values for
                                                      						the four items are separated by colons. Values are displayed in the same order
                                                      						that the items appear in the column heading.

This number includes resources in Talking, Work, and
                                                                  						  Reserved states. If you are logged into the Unified CCX Administration web
                                                                  						  interface as a Supervisor and opening the Real-Time Reporting plug-in, you will
                                                                  						  be able see all the logged in agents from all the teams independent of team
                                                                  						  membership.

Total Contacts

Number of total contacts since the statistics were last
                                                      						reset for this CSQ.

Contacts Waiting

Number of contacts waiting to be connected to a resource in
                                                      						this CSQ.

This column also displays how long the oldest contact has
                                                      						been waiting.

Contacts [oldest contact in queue]

Duration of longest currently waiting contact.

Contacts Handled

Number of contacts that have been handled by this CSQ.

Contacts Abandoned

Number of contacts that have been abandoned by this CSQ.

Contacts Dequeued

Number of contacts that have been dequeued from this CSQ.

Avg Talk Duration

Average time (in seconds) agents in this CSQ spent talking
                                                      						to contacts.

Avg Wait Duration

Average wait time (in seconds). It begins when the call was queued (when you run the "Select Resource" step) and ends when the call reaches the agent. Wait duration does not include hold time.The time a contact spends on a CTI
                                                      port prior to getting queued is not included in this wait time.

Longest Talk Duration

Longest time (in seconds) agents in this CSQ spend talking
                                                      						to contacts.

Longest Wait Duration

Longest wait (in seconds) for a contact to be connected to a
                                                      						resource.

###### Preview Outbound
                                    	 Campaign Cisco Unified Contact Center Express Stats Report

Use the
                                          		  Preview Outbound Campaign Cisco Unified Contact Center Express Stats real-time
                                          		  report to view real-time Unified Contact CCX information for the Outbound
                                          		  preview dialer.

To
                                          		  access the Preview Outbound Campaign Cisco Unified Contact Center Express Stats
                                          		  report, choose Reports > Preview Outbound Campaign
                                                				Cisco Unified Contact Center Express Stats from the
                                          		  Application Reporting menu bar.

The
                                          		  following fields are displayed on the Preview Outbound Campaign Cisco Unified
                                          		  Contact Center Express Stats report.

Field

Description

Campaign

The name of the preview outbound campaign.

Status

The current activation state of the preview outbound campaign:

- Running: an active preview outbound campaign

- Stopped: an inactive preview outbound campaign

Active

Total number of outbound calls currently previewed by or connected to agents for this preview outbound campaign. Active Calls
                                                      = Previewed + Connected.

Preview

Total number of outbound calls currently previewed but have not been accepted, rejected or closed by the agents as part of
                                                      this preview outbound campaign.

Connected

Total number of outbound calls currently connected to agents for this preview outbound campaign. When an agent conferences
                                                      in other agents, the call is counted once towards the total number of connected calls.

Offered

Total number of outbound calls offered for this preview outbound campaign. A call is considered offered when it is presented
                                                      to an agent as part of this preview outbound campaign. A contact that is presented to an agent, rejected by that agent, and
                                                      then presented to the same agent or to another agent is counted twice towards the number of calls offered. Offered = Accepted
                                                      + Rejected + Closed + Timed-out.

Accepted

Total number of outbound calls accepted for this preview outbound campaign. A call is considered accepted if an agent has
                                                      clicked Accept when presented the call. A call that is presented to an agent, rejected by that agent, presented to another
                                                      agent, and then accepted by that other agent is counted once towards the number of calls accepted.

Rejected

The number of outbound calls that were rejected by an agent as part of this preview outbound campaign. This means that the
                                                      agent selected Reject or Cancel Reservation. These contacts will be dialed again. If a contact is rejected by multiple agents, this field increments
                                                      each time the contact is rejected.

The number Rejected is also incremented each time an agent drops the preview call while it is ringing at the customer contact.

Closed

The number of outbound contacts that were closed by agents as part of this preview outbound campaign. This means that the
                                                      agent selected Reject-close. These contacts will not be dialed again.

Timed-Out

Total number of outbound calls that timed out. A call is considered timed out when it is presented to an agent and not accepted,
                                                      rejected, or closed within the allocated time. These contacts will be dialed again. If a contact times out for multiple agents,
                                                      this field is incremented each time the contact is timed out for each agent.

Invalid Number

The number of outbound calls that were dialed to an invalid number for this preview outbound campaign. This means that the
                                                      agent accepted the call (by clicking Accept), got connected to the customer, and selected the "Invalid Number" option from the contact Reclassification drop down. It also includes the number of outbound calls that failed at the network
                                                      level.

The agent can manually reclassify the contact as Invalid Number while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call.

Voice

The number of outbound calls that ended in successful customer contact. This means that an agent accepted the call (by clicking
                                                      Accept) and selected a classification of Voice or Do Not Call for this contact.

Answering Machine

The number of outbound calls that connected to an answering machine for this preview outbound campaign. This means that the
                                                      agent accepted the call (by clicking Accept), got connected to the answering machine and selected the Answering Machine option
                                                      from the contact Reclassification drop down.

The agent can manually reclassify the contact as Answering Machine while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call.

Requested Callback

The number of contacts marked for callback for this preview outbound campaign. This means that the agent accepted the call
                                                      (by clicking Accept), got connected to the contact, the contact requested a callback, and the agent selected the CallBack
                                                      option. A call that is accepted by an agent, marked for callback, later presented to and accepted by another agent (at the
                                                      callback time), and marked for callback again is counted twice towards the number of callback calls.

Avg Talk Duration

The average time in HH:MM:SS (hours, minutes, seconds) that agents spend talking on outbound calls for this preview outbound
                                                      campaign. The durations consider all calls that were Agent Accepted and classified as Voice. If a call is transferred or conferenced
                                                      back to the route point, the preview outbound campaign talk duration does not handle the talk time of agents who handle the
                                                      call after it came through the route point.

Longest Talk Duration

The longest talk duration of an outbound call in HH:MM:SS (hours, minutes, seconds) for this preview outbound campaign. The
                                                      durations consider all calls that were Agent Accepted and classified as Voice.

###### Chat CSQ Cisco Unified Contact Center Express Stats Report

Use the Chat CSQ Cisco Unified Contact Center Express Stats real-time report to view real-time queue information. This report
                                          is available in Cisco Unified CCX Premium license package.

Unified CCX reports contain information for a chat contact that are queued with a specific CSQ. If a contact is not queued,
                                                      the reports do not display data for that chat contact.

To access the Chat CSQ Cisco Unified Contact Center Express Stats report, choose Reports > Chat CSQ Cisco Unified Contact Center Express Stats from the Application Reporting menu bar.

The following fields are displayed on the Chat CSQ Cisco Unified Contact Center Express Stats report.

Field

Description

Name

Name of the chat CSQ

Busy Resources/ Ready Resources/ Not Ready Resources/ Logged-In Resources

Number of resources who are in the Busy, Ready, and Not Ready states, and the number of agents logged in for this chat CSQ.
                                                      Values for the four items are separated by colons. Values are displayed in the same order that the items appear in the column
                                                      heading.

If you are logged in to the Unified CCX Administration web interface as a supervisor and you open the Real-Time Reporting
                                                                  plug-in, you can see all the logged-in agents from all the teams.

Total Contacts

Number of total contacts presented to this queue since last reset of statistics.

Contacts Waiting [Oldest Contact in Queue]

Number of contacts waiting in this queue with the duration of longest waiting contact in this queue.

Contacts Handled

Number of contacts that have been handled by this queue since last reset of statistics.

Contacts Abandoned

Number of contacts that have been abandoned in this queue since last reset of statistics.

Avg Contact Handling Duration

Average time (in HH:MM:SS) agents in this CSQ spent chatting with contacts.

Avg Wait Duration

Average wait time (in HH:MM:SS) a contact spent in queue waiting for an agent.

Longest Contact Handling Duration

Longest time (in HH:MM:SS) agents in this CSQ spent chatting with contacts.

Longest Wait Duration

Longest wait (in HH:MM:SS) for a contact to be connected to an agent.

###### Chat Resource
                                    	 Cisco Unified Contact Center Express Stats Report

Use the
                                          		  Chat Resource Cisco Unified Contact Center Express Stats real-time report to
                                          		  view real-time Unified CCX chat resource information. This report is available
                                          		  in Cisco Unified CCX Premium license package.

To access the Chat
                                          		  Resource Cisco Unified Contact Center Express Stats report, choose Reports
                                             			 > Chat Resource Cisco Unified Contact Center Express Stats from
                                          		  the Application Reporting menu bar.

The
                                          		  following fields are displayed on the Chat Resource Cisco Unified Contact
                                          		  Center Express Stats report:

Field

Description

Name
                                                      						(ID)

Unique
                                                      						identifier of the resource.

State

Current
                                                      						state of the resource.

Current Active Contacts

Number of active contacts that the agent is handling.

Duration
                                                      						in State

Length
                                                      						of time (in HH:MM:SS) the resource has remained in the current state.

Avg
                                                      						Resource Busy Duration

Average
                                                      						time the agent spent with contacts. The resource busy duration is the elapsed
                                                      						time between the resource accepting the contact and completing the chat by
                                                      						clicking End.

Longest
                                                      						Resource Busy Duration

Longest
                                                      						time the agent spent with a contact. The resource busy duration is the elapsed
                                                      						time between the resource accepting the contact and completing the chat by
                                                      						clicking End.

Contacts
                                                      						Presented

Number
                                                      						of contacts that have been presented to this resource.

Contacts
                                                      						Handled

Number
                                                      						of contacts that have been handled by this resource.

###### Overall Chat Cisco Unified Contact Center Express Stats Report

Use the Overall Chat Cisco Unified Contact Center Express Stats real-time report to view real-time Unified CCX resource and
                                          contact information. This report  is available in Cisco Unified CCX Premium license package.

Unified CCX reports contain information for contacts that have been queued in one or more CSQs. If a contact is not queued,
                                                      the reports do not display data for that contact.

To access the Overall Chat Unified CCX Stats report, choose Reports > Overall Chat Cisco Unified Contact Center Express Stats from the Application Reporting menu bar.

The following fields are displayed on the Overall Chat Cisco Unified Contact Center Express Stats report.

Field

Description

CSQs

Number of chat CSQs currently configured. If a chat CSQ is added or removed, this statistic reflects that change.

Logged-in Resources

Number of resources currently logged in.

Busy Resources

Number of resources currently busy.

Ready Resources

Number of resources currently ready.

Not Ready Resources

Number of resources currently not ready.

Total Contacts

Number of total contacts that have arrived since the statistics were last reset. This includes contacts that are waiting,
                                                      contacts connected to a resource, and contacts that have disconnected.

Contacts Waiting

Number of contacts waiting to be connected to a resource.

A contact is shown as waiting until the contact is answered by the agent.

Oldest Contact in Queue

Displays the wait time for the oldest contact in the queue.

Contacts Handled

Number of contacts that have been handled by a resource.

Contacts Abandoned

Number of contacts that are routed to the CSQ since midnight but are abandoned due to one of the following:

Customer ended the chat as the chat was not answered by an agent.

Customer chat was disconnected.

No agents were available.

All agents were busy.

Avg Contact Handling Duration

Average duration (in HH:MM:SS) that resources spent chatting on Unified CCX contacts. Chat duration starts when a contact
                                                      first connects to a resource and ends when the contact disconnects from the resource to which it was connected.

Avg Wait Duration

Average wait time (in HH:MM:SS). It begins when the contact enters the system and ends when either the contact is connected
                                                      with an agent or if contact was disconnected.

Longest Contact Handling Duration

Longest contact handling duration (in HH:MM:SS) of a contact.

Longest Wait Duration

Longest wait (in HH:MM:SS) for a contact to be connected to a resource.

###### Outbound Campaign
                                    	 Stats Report

If you
                                          		  have an Outbound license, use the Outbound Campaign Stats report to view
                                          		  real-time statistics on each IVR-based and agent-based progressive and
                                          		  predictive Outbound campaign configured in Unified CCX. This report will be
                                          		  available only if you have an Outbound license on top of Unified CCX premium
                                          		  license in your Unified CCX.

To
                                          		  access the Outbound Campaign Stats report, choose Reports > Outbound Campaign
                                                				Stats from the Application Reporting menu bar. The
                                          		  following fields are displayed on the Outbound Campaign Stats report.

The call related fields display the data from the time the
                                                      			 statistics were last reset.

Field

Description

Campaign
                                                      						Name

The name
                                                      						of the IVR-based or agent-based progressive or predictive campaign.

Status

The
                                                      						current activation state of the campaign:

- Running: an active
                                                         						  IVR-based or agent-based progressive or predictive campaign.

- Stopped: an inactive
                                                         						  IVR-based or agent-based progressive or predictive campaign.

Campaign
                                                      						Type

The
                                                      						dialer type of the campaign, which can be one of the following:

- IVR Progressive

- IVR Predictive

- Agent Progressive

- Agent Predictive

Attempted

The
                                                      						total number of attempted calls.

If there
                                                      						are no customer abandoned calls, then Attempted will be equal to sum of the
                                                      						following counters:

Voice + Answering Machine + Invalid Number + Fax/Modem + No
                                                      						Answer + Busy + Failed.

Voice

The
                                                      						total number of calls that are connected to live voice.

Whenever there is an exception while running some steps in an IVR script in case of IVR-based campaigns. For example, if there
                                                                           is any codec mismatch issue, there will be an exception in the Accept Step. In such cases, the same call will be marked in
                                                                           the following three categories voice, active, and system abandoned.

Whenever the call that is ringing on the agent's phone
                                                                           								fails in case of agent-based campaigns.

Answering Machine

The
                                                      						total number of calls that reached an answering machine.

Invalid
                                                      						Number

The
                                                      						total number of calls that reached an invalid number:

- A failed call when the
                                                         						  gateway returns an invalid or not found error.

Fax/Modem

The
                                                      						total number of calls that reached fax or modem.

No
                                                      						Answer

The
                                                      						total number of calls that were not answered within the time configured for the
                                                      						No Answer Ring Limit field in the Add New Campaign web page.

Busy

The
                                                      						total number of calls that reached a busy destination.

Failed

The
                                                      						total number of calls that failed due to any one of the following reasons:

- Dialer asked the Gateway to
                                                         						  cancel a call that was dialed out, but not connected.

- Gateway has declined the
                                                         						  call.

- Gateway failure or
                                                         						  configuration issues at the Gateway.

- Gateway is down.

Active

The
                                                      						total number of calls that were connected to IVR ports or agents.

All the
                                                      						voice calls that will be connected to Outbound IVR ports or agents will be
                                                      						marked as active. If you have selected Answering Machine Treatment or Abandoned
                                                      						Call Treatment as "Transfer to IVR," the answering machine calls and abandoned
                                                      						calls that are getting transferred to Outbound IVR ports will also be marked as
                                                      						active.

Customer
                                                      						Abandoned

The
                                                      						total number of calls that were disconnected by the customer or agent within
                                                      						the Abandoned Call Wait Time configured in Add New Campaign web page.

System
                                                      						Abandoned

The
                                                      						total number of calls that were abandoned due to any of the following reasons:

- Non-availability of ports
                                                         						  or agents.

- Any issues at system
                                                         						  level.

Abandon Rate (in %)

Abandon Rate = (System Abandoned/Voice)*100

If you have selected Answering Machine Treatment as "End Call"
                                                            				  for an IVR or agent based outbound campaign through Campaign Configuration web
                                                            				  page, then Voice = Active + System Abandoned.

If you have selected Answering Machine Treatment or Abandoned
                                                            				  Call Treatment as "Transfer to IVR" for an IVR or agent based outbound campaign
                                                            				  through Campaign Configuration web page, then Voice + Answering Machine =
                                                            				  Active + System Abandoned.

###### Overall Outbound
                                    	 Stats Report

If you
                                          		  have an Outbound license, you can use the Overall Outbound Stats report to view
                                          		  real-time statistics across all IVR-based and agent-based progressive and
                                          		  predictive campaigns since the statistics were last reset. This report will be
                                          		  available only if you have an Outbound license on top of Unified CCX premium
                                          		  license in your Unified CCX.

To
                                          		  access the Overall Outbound Stats report, choose Reports > Overall Outbound
                                                				Stats from the Application Reporting menu bar. The
                                          		  following fields are displayed on the Overall Outbound Stats report for all the
                                          		  configured IVR-based and agent-based Outbound campaigns.

The call related fields display the data from the time the
                                                      			 statistics were last reset.

Field

Description

Attempted

The
                                                      						total number of attempted Outbound calls.

Voice

The
                                                      						total number of Outbound calls that were connected to live voice.

Answering Machine

The
                                                      						total number of Outbound calls that reached answering machine.

Invalid
                                                      						Number

The
                                                      						total number of Outbound calls that reached an invalid number.

Fax/Modem

The
                                                      						total number of Outbound calls that reached fax or modem.

No
                                                      						Answer

The
                                                      						total number of Outbound calls that were not answered.

Busy

The
                                                      						total number of Outbound calls that reached a busy destination.

Failed

The
                                                      						total number of failed Outbound calls for all IVR and agent based Outbound
                                                      						campaigns.

Active

The
                                                      						total number of Outbound calls that were connected to Outbound IVR ports or
                                                      						agents.

Customer
                                                      						Abandoned

The
                                                      						total number of Outbound calls that were abandoned by the customer or
                                                      						disconnected by the agent.

System
                                                      						Abandoned

The
                                                      						total number of Outbound calls that were abandoned by the system.

###### Resource Cisco
                                    	 Unified Contact Center Express Stats Report

Use the
                                          		  Resource Cisco Unified Contact Center Express Stats real-time report to view
                                          		  real-time Unified Contact CCX agent information.

To
                                          		  access the Resource Cisco Unified Contact Center Express Stats report, choose Reports > Resource Cisco Unified
                                                				Contact Center Express Stats from the Application
                                          		  Reporting menu bar.

If multiple
                                                      			 lines are configured for an agent, only the calls on the agent's primary
                                                      			 extension are reported in Resource Cisco Unified Contact Center Express Stats
                                                      			 report.

The
                                          		  following fields are displayed on the Resource Cisco Unified Contact Center
                                          		  Express Stats report.

Field

Description

Name
                                                      						(ID)

Unique
                                                      						identifier of the agent.

State

Current
                                                      						state of the agent.

Duration
                                                      						in State

Amount
                                                      						of time (in seconds) the agent has remained in the current state.

Contacts
                                                      						Presented

Number
                                                      						of contacts presented to the agent.

Contacts
                                                      						Handled

Number
                                                      						of contacts handled by the agent.

Avg Talk
                                                      						Duration

Average
                                                      						time (in seconds) the agent spent in talking state.

Avg Hold
                                                      						Duration

Average
                                                      						time (in seconds) the agent keeps calls on hold.

Longest
                                                      						Talk Duration

Longest
                                                      						time (in seconds) the agent spent in talking state.

Longest
                                                      						Hold Duration

Longest
                                                      						time (in seconds) the agent keeps a call on hold.

Outbound
                                                      						Offered

Total
                                                      						number of preview outbound calls offered to the agent. A call is considered
                                                      						offered when it is presented to an agent. The number of calls offered is
                                                      						counted twice if a contact that is presented to an agent is skipped/rejected by
                                                      						that agent and then the contact is presented to the same agent or to another
                                                      						agent. Offered = Accepted + Rejected + Closed + Timed-out.

Outbound
                                                      						Accepted

Total
                                                      						number of outbound calls accepted by the agent. For transferred or conferenced
                                                      						outbound calls, the call is considered accepted if it is answered by the agent.

A
                                                      						preview outbound call is considered accepted if an agent has clicked Accept to
                                                      						accept the call and then the system places the call to the customer. The number
                                                      						of calls accepted is counted once if a call that is presented to an agent is
                                                      						skipped/rejected by that agent and then the call is presented to another agent
                                                      						who accepts the call.

A progressive or predictive outbound call is considered accepted if an agent has answered a live voice call that is presented
                                                      to the agent (if Agent AutoAnswer is disabled).

Outbound
                                                      						Rejected

The
                                                      						number of preview outbound calls skipped/rejected by the agent. This means that
                                                      						the agent selected Reject, Skip, or Cancel Reservation. These contacts will be
                                                      						dialed again.

The
                                                      						number of calls rejected is also incremented each time an agent drops the
                                                      						preview call while it is ringing at the customer’s contact.

Outbound
                                                      						Closed

The
                                                      						number of contacts closed by the agent for preview outbound. This means that
                                                      						the agent selected Skip-Close or Reject-close. These contacts will not be
                                                      						dialed again.

Outbound
                                                      						Timed-Out

Total
                                                      						number of preview outbound calls that timed out. A call is considered timed out
                                                      						when the call is presented to an agent but not accepted, rejected, or closed
                                                      						within the allocated time. These contacts will be dialed again. If a contact
                                                      						timed out for multiple agents, this field is incremented each time the contact
                                                      						is timed out for each agent.

Outbound
                                                      						Voice

The
                                                      						number of preview outbound calls that ended in successful customer contact for
                                                      						the agent. This means that the agent accepted the call (by clicking Accept) and selected a classification of Voice or Do Not Call for
                                                      						this contact.

Outbound
                                                      						Avg Talk Duration

The
                                                      						average time in HH:MM:SS (hours, minutes, seconds) that the agent spends in
                                                      						talking state for outbound calls. This talk duration also includes the time
                                                      						spent on outbound calls that were transferred or conferenced to a route point.

For
                                                      						preview outbound, the talk duration considers all calls that were Agent
                                                      						Accepted and classified as Voice.

Outbound Avg Hold Duration

The
                                                      						average time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                                      						holding an outbound call.

For
                                                      						preview outbound, the hold duration considers all calls that were Agent
                                                      						Accepted and classified as Voice.

Outbound Longest Talk Duration

The
                                                      						longest time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                                      						talking state for an outbound call .

For
                                                      						preview outbound, the talk duration considers all calls that were Agent
                                                      						Accepted and classified as Voice.

Outbound Longest Hold Duration

The
                                                      						longest time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                                      						holding an outbound call.

For
                                                      						preview outbound, the hold duration considers all calls that were Agent
                                                      						Accepted and classified as Voice.

###### Failover Behavior for Unified CCX Stats

All failovers, regardless of whether the Unified CCX Engine is restarted, will cause the Unified CCX stats to reset.

The Unified IP IVR stats do not reset in all cases if the Unified CCX Engine is not restarted on a node. However, the node
                                          loses its active server status. The Unified IP IVR stats on that node will not be reset.

##### Tools Menu

The
                                       		  Tools menu gives you access to the following Application Reporting tools:

Reset All Stats —Choose
                                             				this option to reset all statistics.

Open Printable
                                                				  Report —Choose this option to get a printable report of all currently active
                                             				contacts in the system.

Refresh
                                                				  Connections —Choose this option to refresh connections with the Unified
                                                				  CCX system.

Clear Contact —Choose
                                             				this option to clear contacts/calls that have been stuck in the system for a
                                             				long time.

###### Reset All
                                    	 Statistics

Use the
                                          		  Reset All Stats option to reset all statistics accumulated since the last time
                                          		  the statistics were reset. It will not reset active statistics, such as active
                                          		  contacts, tasks, and so on.

The Unified CCX
                                                      			 system automatically resets all statistics each day at midnight.

Choose Tools > Reset All
                                                         				  Statistics from the Application Reporting menu bar.

###### Open Printable Report

Use the option to get a printable report of all currently
                                          		  active contacts in the system.

To get a printable report:

Choose a real-time report from the Report menu option and then Tools > Open Printable
                                                         				  Report from the Application Reporting menu bar.

###### Refresh
                                    	 Connections

To
                                          		  refresh connections with the Unified
                                             			 CCX system:

Choose Tools > Refresh
                                                         				  Connections from the Application Reporting menu bar.

The Unified
                                                         				  CCX system
                                                      				refreshes all connections.

###### Clear Contact Menu

You can use the Clear Contact menu option to clear contacts
                                          		  in the following three situations:

###### Clear Stuck Calls from Sontacts Real-Time Report

To clear stuck calls or contacts from the Unified CCX
                                             		  system:

Step 1

Choose the contact from Reports > Contacts .

Step 2

From the Application Reporting menu bar, choose Tools > Clear
                                                            				  Contact . A Clear Call dialog box is displayed to warn
                                                      			 you. If you want to continue with the clear action, click No . To cancel the action, click Yes .

Step 3

Click No to proceed with the clear action. A Clear
                                                      			 Contact dialog box is displayed for you to confirm the action. You can click Yes to proceed or No to cancel.

Step 4

Click Yes . The Unified CCX system removes the
                                                      			 contact from all its queues.

###### Clear Stuck Calls from Overall Cisco Unified CCX Stats

To clear stuck calls/contacts from the Unified CCX system:

Step 1

Choose Reports > Overall Cisco
                                                            				  Unified Contact Center Express Stats .

Step 2

Choose the contact from Views and click Overall Waiting Contacts Info .

Please note that the Overall Waiting Contacts Info menu option
                                                                     				  displays only those calls that are queued in CSQs and not agent-based routing
                                                                     				  calls.

Step 3

From the Application Reporting menu bar, choose Tools and click Clear Contact . A Clear Call dialog box is
                                                      			 displayed to warn you. If you want to continue with the clear action, click No . To cancel the action, click Yes .

Step 4

Click No to proceed with the clear action. A Clear
                                                      			 Contact dialog box is displayed for you to confirm the action. You can click Yes to proceed or No to cancel.

Step 5

Click Yes . The Unified CCX system removes the
                                                      				contact from all its queues.

###### Clear Stuck Calls from CSQ Cisco Unified CCX Stats

To clear stuck calls or contacts from the Unified CCX
                                             		  system:

Step 1

Choose Reports > CSQ Cisco
                                                            				  Unified Contact Center Express Stats .

Step 2

Choose the contact from Views and click CSQ Waiting Contacts Info .

Step 3

From the Application Reporting menu bar, choose Tools > Clear
                                                            				  Contact . A Clear Call dialog box is displayed to warn
                                                      			 you. If you want to continue with the clear action, click No . To cancel the action, click Yes .

Step 4

Click No to proceed with the clear action. A Clear
                                                      			 Contact dialog box is displayed for you to confirm the action. You can click Yes to proceed or No to cancel.

Step 5

Click Yes . The Unified CCX system removes the
                                                      				contact from all its queues.

##### Views Menu

The
                                       		  Views menu allows you to access more detailed information for the following
                                       		  reports: The
                                          			 Application Tasks report, the Contacts report, the Applications report, the
                                          			 Sessions report, Overall Cisco Unified Contact Center Express Stats report, and
                                          			 the CSQ Cisco Unified Contact Center Express Stats report.

For some
                                                   			 reports, detailed information is also available by right-clicking a record in
                                                   			 that report.

The
                                       		  Views menu contains different options, depending on the report you have chosen.
                                       		  Possible options are:

Contacts by Application
                                                				  Task ID —Choose this option to view contacts according to Application Task
                                             				ID numbers.

Engine Tasks by Application
                                                				  Task ID —Choose this option to view Engine tasks according to Application
                                             				Task ID numbers.

Detailed Info —Choose
                                             				this option to view more detailed information on selected reports.

Application Tasks by
                                                				  Application Name —Choose this option to view application tasks by
                                             				application name.

Contacts by Session
                                                				  ID —Choose this option to view contacts by session ID.

Overall Waiting Contacts
                                                				  Info —Choose this option to view detailed information for the overall
                                             				waiting contacts. To clear stuck calls in this view, see Scenario 2 in Clear
                                                				  contact menu option.

CSQ Waiting Contacts
                                                				  Info —Choose this option to view detailed information for the CSQ waiting
                                             				contacts. To clear stuck calls in this view, see Scenario 3 in Clear
                                                				  contact menu option.

###### Application Tasks

You can obtain reports based on the application task ID associated with application tasks.

###### Contacts by Application Task ID

This report displays the same report as the Contact report
                                             		  with the exception that the Contacts by Application Task ID report has been
                                             		  filtered using only the contact currently being managed by the selected
                                             		  application task.

###### Engine Tasks by Application Task ID

This report displays the same report as the Engine Task
                                             		  reports except that the Engine Tasks by Application Task ID report has been
                                             		  filtered to display only the engine tasks that are associated with the
                                             		  application task.

###### Contacts

When you use the Views options with the Contacts report, the
                                          		  Views menu contains only the Detailed Info option.

The Detailed Info option provides various detailed
                                          		  information, depending on the type of contact selected. For example, if the
                                          		  contact is a call, the Calling Party number, the Called Number, and so on, are
                                          		  displayed for that particular call.

###### Applications

When you use the Views options with the Application reports,
                                          		  the Views menu contains only the Application Tasks by Application Name option.

The Application Task By Application Name report displays the
                                          		  same report as the Application Task report except that the Application Task By
                                          		  Application Name report is filtered using only the active application tasks
                                          		  associated with this application.

###### Sessions

You can obtain reports based on the session ID associated with a session.

###### Contacts by Session ID

This report displays the same report as the Contact report
                                             		  with the exception that the Contacts By Session ID report is filtered using
                                             		  only the contacts associated with the selected session.

###### Detailed Info

Detailed info displays the time the session was created and its current state.

##### Settings
                                 	 Menu

The
                                       		  Settings menu of the Application Reporting menu bar allows you to adjust
                                       		  various settings of the Real Time Reporting tool.

The
                                       		  Settings menu contains the following menu options:

Options —Choose this
                                             				option to set the polling (refresh) interval times and to set the amount of
                                             				times the server will attempt to reconnect.

Window —Choose this
                                             				option to display reports in colors based on your Windows settings.

Motif —Choose this
                                             				option to display reports in purple and menu items in brown.

Metal —Choose this
                                             				option to display reports in grey and menu items in black.

###### Options
                                    	 Menu

Choose Settings and click Options to access the Options dialog box. Use the
                                          		  Options dialog box to set the polling (refresh) interval time, set the number
                                          		  of times the server will attempt to reconnect , and specify whether
                                             			 logged off agents appear in reports .

The
                                          		  following fields are displayed in the Options dialog box.

Field

Description

Polling
                                                      						Interval

Time
                                                      						between two requests to the server for new statistics by the client.

Server
                                                      						Connect Retry Count

The
                                                      						number of times that the Unified CCXAdministration web interface should
                                                      						attempt to reconnect to the Unified CCX server.

If an
                                                                  						  error occurs, an Error dialog box opens to alert you that the server is not
                                                                  						  communicating with the web interface.

Show
                                                      						Logged Off Resources

Specifies whether logged off agents appear in reports.

Click Apply to submit configuration changes.

## Reporting Administration on Unified Intelligence Center

Unified Intelligence Center is the default reporting solution for Unified CCX. Unified
                           			Intelligence Center is a comprehensive, end-to-end reporting solution.

Live Data reports can only be run by agents, supervisors, and reporting users.

For more information, see the following guides:

Cisco Unified Contact
                                          				  Center Express Report User Guide

Cisco Unified Contact
                                          				  Center Express Report Developer Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_programming_reference_guides_list.html

Cisco Finesse

You can configure the Live Data reports that are to be displayed in the gadgets of the
                           			Cisco Finesse desktops.

## Start Unified
                        	 Intelligence Center

Step 1

Open a web browser.

Step 2

Access http://<host address> and click Cisco Unified Contact Center Express
                                          				Reporting .

Host address is the DNS name or IP address of the Unified CCX
                                                         					 node.

Step 3

Enter your username and password.

Step 4

Click Log In .

## Administrator
                        	 Overview

Access to the functions in the Unified Intelligence Center reporting
                           		application is controlled by the one or more users who have the user role of
                           		Security Administrator.

The initial, default Security Administrator is the user defined as the
                           		System Application User during the installation.

Security Administrators can:

Create and maintain users.

Assign User Roles—User roles are assigned to users to control access
                                 			 to drawers and what objects the user can create.

Assign users to User Groups.

Create and maintain user groups.

Assign Permissions—Whereas User Roles are associated with people,
                                 			 permissions are associated with objects (Dashboards, Reports, Report
                                 			 Definitions, Data Sources, Value Lists, and Collections).

Use the Run As feature to verify other users' permissions.

## Security
                        	 Overview

Unified Intelligence Center security offers multilayered and flexible functionality that allows a security administrator to
                           create a flat or a tiered structure of access to Unified Intelligence Center functions, based on the organization's needs.

A user's access to Unified Intelligence Center functions is based on:

Login authentication.

License type under which the user's organization runs Unified Intelligence Center. For example, organizations that use a Standard
                                 license cannot access the Report Definition functions.

User Role (a user can have one, some, or all seven User Roles).

User Groups in which user is a member.

For an object the user can access, the object-level permissions assigned by the person who created that object.

## User List

User List page opens from the Security drawer. If a user who does not have
                           		  the Security Administrator user role accesses this page, that user can see all the parameters except the  user roles.
                           The user cannot change his role or group membership.

When Security Administrators access this page, they can see all
                           		  existing users; can create users, modify or delete users, review or edit user
                           		  information, and 
                           		  use the Run As feature to work in Cisco Unified Intelligence Center as a user.

Field

Explanation

Only show currently active users

Check the check box to display users who are currently active.

Name Contains

Use this filter field to narrow the list of names or to move
                                       					 to a specific name.

User Name

The domain and user name (domain\name).

First Name

The user's first name.

Last Name

The user's last name.

You can perform the following actions on the user lists page:

Create —Opens the User Information page.

Edit —Select a user name and click Edit to edit the User Information page.

Delete —Select a user and click Delete to delete the user.

Run As —Select a user and click Run As to refresh the Cisco Unified Intelligence Center reporting interface.

Refresh —Refreshes the page to show any latest changes to the User List.

Page —Click the arrow to move to the next
                                 				page of the User List.

Help —Opens online help.

X —Closes the page.

## Create a User

To create a user, perform the following procedure:

Step 1

Navigate to Security > User List .

Step 2

Under the General Information tab, perform the following:

In the User Name field, enter the domain and user name (domain\name).

In the Alias field, enter the alias name for this user.

Check the User is active check box to enable the user to log in and remain active.

If the check box is unchecked, the user cannot log in.

In the First Name field, enter the first name of the user.

In the Last Name field, enter the last name.

In the Organization field, enter the company name or other descriptive text to be associated with the user, such as region or Line of Business.

In the Email field, enter the email address  of the user.

In the Phone field, enter a phone number for the user. This can be the user's personal phone number or an emergency contact.

In the Description field, enter the description of the user.

In the Time Zone field, choose the time zone that you want to use in the report from the drop-down list.

This time zone is also used for the user's scheduled reports and takes precedence over the time zone used by the report server.

If this field is left blank, the system uses the time zone of the report server.

For Start Day of the Week , perform the following:

Select Locale Based to select starting day of the week based on locale.

Select Custom Settings to choose one of the seven days of the week from the drop-down list.

Start Day Of The Week is used in Scheduled Report, Report Views, and Permalink.

In the Roles field, select and assign one or more roles for this user.

If the Security Administrator adds or changes User Roles, the change does not take effect until the user logs out and then
                                                logs in again.

In the Permissions field, choose the user's permission setting preference for My Group when creating new objects. My Group is the object owner's
                                             default group.

Settings for My Group configures whether other users who belong to this user's default group can write, or run the objects.
                                                            Higher level permissions persist and override other permissions.

Step 3

Under the Groups tab, you can determine which groups this user is a member of and how to add group membership(s) for a user.
                                       You can view the following:

My Group : This field shows the user's default group. The Security Administrator can change it. The group is represented as “My Group”
                                                for the user.

Available Groups : This list shows all the groups that have been created and that the user is not yet a member of. You can use arrows to move
                                                groups between columns.

Selected Groups : This column shows all the groups that the user is a member of. You can use arrows to move groups between columns.

By default, every user has AllUsers in their Selected Groups column. You cannot remove the AllUsers group from the Selected
                                                            Groups column.

## User Groups

User Groups page opens from the Security drawer. Use it to see the existing
                           		  groups, to create or delete groups, and to review or edit group information.

The following are the  two default groups created by the
                           		  system:

The AllUsers group is supplied by Unified Intelligence Center. All users belong to this group by default.

The Administrators group consists of administrators.

Field

Explanation

Name Contains

Use this filter field to narrow down the list of group names or to
                                       					 move to a specific name.

Name

Name of the group.

Full Name

The full name shows the child relationship of a group, as indicated by a dot separator.

For example, if the default group for Group3 is Group1, and
                                       					 Group1 is a top level group (does not have a parent), then the Full Name of
                                       					 Group1 is Group1 . The Full Name of Group 3 is Group1.Group3 .

Description

Description text of the group.

Yu can perform the following actions on the User Groups page:

Create —Opens the Group Information page.

Edit —Select the
                                 				group name and click Edit to open the Group Information page.

Delete —Select the
                                 				group name and click Delete.

Refresh —Refreshes the page to show any changes to the Group List.

Help —Opens online help.

X —Closes the page.

### Overview

User Groups are
                                 		  constructs that allow security administrators to partition Unified Intelligence
                                 		  Center functionality.

Creating User Groups
                                 		  expedites the process of provisioning users when multiple users need the same
                                 		  access to dashboards and reports, or when users require distinct permissions
                                 		  and features based on regional or organizational requirements.

User groups have no
                                 		  impact on how data is stored in the database. They are used only for assigning
                                 		  permissions to all the user members of the group through one operation instead
                                 		  of repeating the same operation for each user.

#### System-Defined
                                 		  All Users Group

All users are
                                 		  automatically a member of the system-defined All Users group.

All Users always appears on the User Groups window. The security administrator cannot delete it.

#### System-Defined
                                 		  Administrator User Group

The security
                                 		  administrator is automatically a member of the system-defined Administrators
                                 		  group and can add other security administrators to it.

Additional Security
                                 		  Administrators must be added to the Administrators group. Having the role does
                                 		  not automatically make them members of that group.

#### Customer-Defined
                                 		  User Groups

Security
                                 		  administrators can create any number of user groups and can add users to them.
                                 		  From those other user groups, one is designated as the user's Group (also
                                 		  called My Group ).

### Create a User Group

To create a user group, perform the following:

Step 1

Navigate to Security > User Groups .

Step 2

Under the General Information tab, perform the following:

In the Group Name field, enter the name of the group. This field is available only when you create a new group.

In the Description field, enter or modify text to describe this group

Step 3

Under the Groups tab, perform the following:

Default Group —From the drop-down list, enter the default group.

Available Groups —Lists the groups that were created and that are available for this group to become a child of. Click > or < to move just that group or groups.

Selected Groups —Lists the groups that this group is a child of. Click > or < to move just that group or groups.

Step 4

Under the Groups Members tab, perform the following:

Under Users tab:

Available Users —Lists all the users that were created and that are available to be children of this group. Click > or < to move just that group or groups.

Selected User Members —Lists the users that are currently children of this group. Click > or < to move just that group or groups.

Under Groups tab:

Available Groups —Lists all the groups that were created and that are available to be children of this group. Click > or < to move just that group or groups.

Selected Groups Members —Lists the groups that are currently children of this group.
                                                         Click > or < to move just that group or groups.

Step 5

Click Save to update new entry or changes to the fields.

Step 6

Click Cancel to cancel or close the page.

## Manage User
                        	 Permissions

Use this page to set
                           		extra permissions to Groups or to individual users.

User permissions
                           		page has the following tabs:

### About
                           	 Permissions

User Roles are
                                 		  associated with people and permissions are associated with objects. Unified
                                 		  Intelligence Center objects are Dashboards, Reports, Report Definitions, Data
                                 		  Sources, Categories, Value Lists, and Collections.

Permissions:

EXECUTE: When
                                       				the user has EXECUTE permissions for an object, that user can perform some
                                       				actions that depend on the object.

For example,
                                       				with EXECUTE permission, a user can run, print, and refresh a report, open and
                                       				refresh a dashboard and run a dashboard slide show, and see a Value List query.
                                       				EXECUTE permission includes the read permission.

WRITE: When the
                                       				user has WRITE permission for an object, that user can alter, rename or delete
                                       				the object. For example, With WRITE permission, you Save As, import, and export
                                       				reports; you can edit a data source and can delete a custom Value List. WRITE
                                       				permission also includes EXECUTE and read permission.

The following
                                       				rules are applicable for all category trees in Unified Intelligence Center —
                                       				Reports, Report Definitions, Dashboards.

To delete an
                                       				entity, you need WRITE permissions for the entity and the entity's parent
                                       				category.

To delete a
                                       				category, you need WRITE permissions for the category, the category's parent,
                                       				and all the categories and/or entities belonging to the category.

A user can only
                                       				Edit or Save an entity even if the immediate parent category has no WRITE
                                       				permissions.

A user can only
                                       				use the Save As feature if the entity has no WRITE permissions enabled.

Any category
                                       				owner within the Imported Report Definitions can delete a category if
                                       				the administrator provides explicit WRITE permissions on the Imported Report Definitions category.

Permissions are
                                 		  combined and the highest level prevails.

A user receives
                                 		  permission for an object from different sources. Permission can be inherited
                                 		  from the AllUsers group, the Default Group (My Group), or the permission
                                 		  assigned by the Security Administrator. Among all these permissions, the
                                 		  highest level permission is used when the user accesses the object.

### User Roles and
                           	 Permissions

Your User Role
                                 		  allows you to "open" the
                                 		  drawer that corresponds to that role. If you have EXECUTE permission, you can
                                 		  create objects for that drawer. For example, if you are a Dashboard Designer,
                                 		  you can create dashboards on the Available Dashboards page.

When you create an
                                 		  object, you are the owner of that
                                 		  object. You have WRITE permission for the object, and you can set the
                                 		  permissions for that object for users in your Group only.

If the object is
                                 		  still a work-in-progress and you do not want anyone to access it yet, you can
                                 		  make it "private" by
                                 		  leaving all permissions unchecked for both the All Users and the Groups.

When the object is
                                 		  ready, set your default Group (My Group) permissions to EXECUTE or even WRITE.
                                 		  For example, if you create a Dashboard for your Group and the dashboard has
                                 		  notes, you might want others in your Group to update the notes.

Even though you are a
                                 		  Dashboard Designer, if the Available Dashboards page contains dashboards
                                 		  created by (owned by) other Dashboard Designers, you may not be able to see
                                 		  those dashboards, based on your Group permissions and on the object-level
                                 		  permissions those owners have set for their dashboards.

### Assigned Group
                           	 Permissions

Step 1

Select the
                                          			 object type in the Permissions For panel. For Dashboard, Report or Report
                                          			 Definition type, you can select a category or an object within a category. For
                                          			 other object types, select an object from the list. All the groups that have
                                          			 already been assigned permissions for the object are displayed in the Group
                                          			 permissions for the selected item panel.

Step 2

Select a group
                                          			 in the All Groups panel. All user members of this group are displayed in the
                                          			 All Users for the selected group panel.

Step 3

Click Set
                                             				Permissions . Check the level you want for the group (Execute,
                                          			 Write), and click OK .

Step 4

The Group
                                             				Permissions for the selected item panel updates to include the
                                          			 group and its assigned permission you defined in Step
                                             				3 .

Field

Description

Permissions For panel (top left)

Click the
                                             					 drop-down list to select the objects for which you want to set permissions.
                                             					 Options are: Data Sources, Report Definitions, Reports, Dashboards, Value
                                             					 Lists, and Collections.

Selecting
                                             					 an object type refreshes the panel to show the list of items or categories for
                                             					 that object.

All Groups
                                             					 panel (top right)

This panel
                                             					 shows the available User Groups. Highlighting a user group refreshes the page
                                             					 to display an All Users for Selected Group panel that lists the member of the
                                             					 group.

All Users
                                             					 for the Selected Group panel (bottom right)

This panel
                                             					 shows all members in the group that is highlighted in the All Groups panel
                                             					 above.

Set
                                             					 Permissions button

Click this
                                             					 option to open a dialog box where you select the permission level for the
                                             					 selected object in the Permissions For panel and the selected group in the All
                                             					 Groups panel.

Group
                                             					 Permissions for the selected item

This panel
                                             					 shows the groups that have already been assigned permission for the selected
                                             					 object, and their permission level.

### Assigned User
                           	 Permissions

Step 1

Select the
                                          			 object type in the Permissions For panel. For Dashboard, Report, or Report
                                          			 Definition type, you can select a category or an object within a category. For
                                          			 other object types, select an object from the list. All the users that have
                                          			 already been assigned permission for the object are displayed in the User
                                          			 permissions for the selected item panel.

Step 2

Select a user
                                          			 name in the User List panel.

Step 3

Click Show
                                             				Groups to see the groups for which this user is a member.

Step 4

Click Set
                                             				Permissions , check the level you want for this user (Execute,
                                          			 Write), and click OK .

The All
                                                				  Permissions for the selected item panel refreshes to show the user
                                             				permissions you have added or changed for this user in steps 3 and 4.

Field

Description

Permissions For panel (top left)

Click the drop-down arrow to select the kinds of object for
                                                         							 which you want to set permissions. Options are Data Sources, Report
                                                         							 Definitions, Reports, Dashboards, Value Lists, Collections, and System
                                                         							 Collections.

Selecting an object type refreshes the panel to show the list of
                                                         							 items or categories for that object.

User
                                                         							 List panel (top right)

This
                                                         							 panel shows current users. Filter the list and select one or many user names.

Show
                                                         							 Groups button

Click this option to show the All Groups for the selected user
                                                         							 panel.

All
                                                         							 Groups for the selected User (bottom right)

This
                                                         							 panel shows all groups to which the highlighted username in the User List panel
                                                         							 above is a member.

Set
                                                         							 Permissions button

Click this option to open a dialog box where you select the
                                                         							 permission level for the object (Execute, Write).

All
                                                         							 Permissions for the selected item

This
                                                         							 panel shows users who have permission for the object, and the level of
                                                         							 permissions they have.

## Run As

Security Administrators can select a name on the User List page and
                              		  click Run As . This refreshes the Unified Intelligence Center web page
                              		  so that it reflects the interface that user has when logged in.

Use this tool to verify that the User Roles and permissions are
                              		  configured properly.

When you Run As another user, the top of the page shows both
                                                				  your Logged In identity and your Run As identity.

You cannot Run As yourself.

You can Run As one level of user. A Security Admin cannot Run As User A and, as User A, then Run As User B.

To leave Run As mode, click Stop Run As at the top of the page.

## Audit Trail Logging
                        	 in Cisco Unified Intelligence Center

Localization of
                                             				Audit Trail report is not supported.

### View Audit Trail
                           	 Logging in Unified Intelligence Center

Step 1

Log in to the
                                          			 Unified Intelligence Center Reporting Interface.

Step 2

Navigate to Reports > Stock > Intelligence Center
                                                				  Admin and click Audit
                                             				Trail . The system opens the Audit
                                             				Trail Report Filter window.

Step 3

Specify the
                                          			 required filter criteria and click Run . The system displays the Audit Trail report
                                          			 based on the filter criteria that you specified.

## Audit Trail
                        	 Report

Location : Reports > Stock > Intelligence Center Admin > Audit Trail .

Views : This report has
                              		  three grid views - Non-grouped, Groupby – EntityName, Groupby –Username.

Grouping : This report has
                              		  two grouped views - grouped and sorted by User and Entity Name. The third view
                              		  is un-grouped which is also the default view for this report.

Value List : CUIC Users,
                              		  CUIC Operations, CUIC Entity Types.

Database Schema Tables from which data is retrieved:

CUICAUDITLOG

CUICLOGEDENTITY

## Security
                        	 Considerations

If you make the user
                              		  a member of one or more other groups, make one of those groups the user's
                              		  default group, and set the permissions for the default group higher than those
                              		  of the AllUsers group.

Higher permissions
                              		  for the default group prevail over permissions in the AllUsers group.
                              		  Individual user permissions prevail over group permissions.

| Note | Do not create a sub-category under the Stock category as the permissions for the Stock category is automatically reset at midnight. You can now
                                          		  rename the Stock Reports folder name. |
|---|---|

| Note | Support for High
                                                			 Availability and remote servers is available only in multiple-server
                                                			 deployments. |
|---|---|

| Note | In a Unified CCX
                                                			 High Availability server with co-resident Cisco Unified Intelligence Center,
                                                			 Cisco Unified Intelligence Center will intelligently point to the appropriate
                                                			 datasource. This will require no manual configuration during failover or in
                                                			 island mode scenario. For more information about Historical datastore, see Cisco Unified Contact
                                                         				  Center Express Serviceability Administration Guide . |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Tools > Historical
                                                      				  Reporting > Database Server
                                                      				  Configuration . The Database Server Configuration web page opens with the following fields: Field Description Server Name The hostname or IP Address of the database server. Maximum DB Connections for Report Clients Sessions The maximum number of client and scheduler connections that can access the Historical Reports Database server. There is a limit of instances for the reporting client sessions and the scheduler sessions based on the load that can be run
                                                                  on each server. The following are the limits: Standalone Setup—1 to 8 instances High Availability Setup—1 to 16 instances | Field | Description | Server Name | The hostname or IP Address of the database server. | Maximum DB Connections for Report Clients Sessions | The maximum number of client and scheduler connections that can access the Historical Reports Database server. There is a limit of instances for the reporting client sessions and the scheduler sessions based on the load that can be run
                                                                  on each server. The following are the limits: Standalone Setup—1 to 8 instances High Availability Setup—1 to 16 instances |
|---|---|---|---|---|---|---|---|
| Field | Description |
| Server Name | The hostname or IP Address of the database server. |
| Maximum DB Connections for Report Clients Sessions | The maximum number of client and scheduler connections that can access the Historical Reports Database server. There is a limit of instances for the reporting client sessions and the scheduler sessions based on the load that can be run
                                                                  on each server. The following are the limits: Standalone Setup—1 to 8 instances High Availability Setup—1 to 16 instances |
| Step 2 | Enter a value in the Maximum DB Connections for Report Client
                                                   			 Sessions field next to a Server Name. |
| Step 3 | Click Update . The configuration changes take effect. |

| Field | Description |
|---|---|
| Server Name | The hostname or IP Address of the database server. |
| Maximum DB Connections for Report Clients Sessions | The maximum number of client and scheduler connections that can access the Historical Reports Database server. There is a limit of instances for the reporting client sessions and the scheduler sessions based on the load that can be run
                                                                  on each server. The following are the limits: Standalone Setup—1 to 8 instances High Availability Setup—1 to 16 instances |

| Choose Tools > User
                                                      				  Management > Reporting Capability
                                                      				  View The User Configuration web page opens. |
|---|

| Note | When you purge
                                                			 data, you permanently delete it. If you want to keep data that will be purged,
                                                			 back up the database. |
|---|---|

| Caution | Not configuring
                                                			 the Purge parameters may make your database to be overloaded with large number
                                                			 of records. This leads to call data not being written to database. |
|---|---|

| Step 1 | From the Unified
                                                   			 CCXAdministration menu bar, choose Tools > HistoricalReporting > Purge Schedule
                                                         				  Configuration . The Purge
                                                      				Schedule Configuration area opens. The following fields are displayed in the
                                                      				Purge Schedule Configuration area. Field Description Purge Schedule Daily
                                                                  							 purge at Time
                                                                  							 of day for the daily purge along with the time zone. The time that appears here
                                                                  							 is based on the primary time zone, which is specified during initial setup of
                                                                  							 Unified CCX Administration. In a
                                                                  							 High Availability over WAN deployment, the purge schedule will happen at the
                                                                  							 time zone of the primary node. Note Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. Purge
                                                                  							 data older than Data
                                                                  							 can persist for a number of months before being purged. Purge run time The
                                                                  							 total duration for which the purge process should run. Auto Purge Configuration Initiate automatic purge when database exceeds Percentage of the maximum database size at which an automatic
                                                                  							 purge is initiated (as compared to the total available size). Initiate automatic purge when extent size exceeds Percentage of the maximum extents size of any table above which
                                                                  							 an automatic purge is initiated. Auto
                                                                  							 purge data for the oldest Age of
                                                                  							 data to be purged. | Field | Description | Purge Schedule | Daily
                                                                  							 purge at | Time
                                                                  							 of day for the daily purge along with the time zone. The time that appears here
                                                                  							 is based on the primary time zone, which is specified during initial setup of
                                                                  							 Unified CCX Administration. In a
                                                                  							 High Availability over WAN deployment, the purge schedule will happen at the
                                                                  							 time zone of the primary node. Note Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. | Note | Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. | Purge
                                                                  							 data older than | Data
                                                                  							 can persist for a number of months before being purged. | Purge run time | The
                                                                  							 total duration for which the purge process should run. | Auto Purge Configuration |  | Initiate automatic purge when database exceeds | Percentage of the maximum database size at which an automatic
                                                                  							 purge is initiated (as compared to the total available size). | Initiate automatic purge when extent size exceeds | Percentage of the maximum extents size of any table above which
                                                                  							 an automatic purge is initiated. | Auto
                                                                  							 purge data for the oldest | Age of
                                                                  							 data to be purged. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Purge Schedule |
| Daily
                                                                  							 purge at | Time
                                                                  							 of day for the daily purge along with the time zone. The time that appears here
                                                                  							 is based on the primary time zone, which is specified during initial setup of
                                                                  							 Unified CCX Administration. In a
                                                                  							 High Availability over WAN deployment, the purge schedule will happen at the
                                                                  							 time zone of the primary node. Note Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. | Note | Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. |
| Note | Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. |
| Purge
                                                                  							 data older than | Data
                                                                  							 can persist for a number of months before being purged. |
| Purge run time | The
                                                                  							 total duration for which the purge process should run. |
| Auto Purge Configuration |  |
| Initiate automatic purge when database exceeds | Percentage of the maximum database size at which an automatic
                                                                  							 purge is initiated (as compared to the total available size). |
| Initiate automatic purge when extent size exceeds | Percentage of the maximum extents size of any table above which
                                                                  							 an automatic purge is initiated. |
| Auto
                                                                  							 purge data for the oldest | Age of
                                                                  							 data to be purged. |
| Step 2 | From the
                                                   			 drop-down list in the Daily purge at field, choose a time of day at which the
                                                   			 system determines if purging is necessary. |
| Step 3 | From the
                                                   			 drop-down list in the Purge data older than field, choose the required number
                                                   			 of months. If the system
                                                      				determines that purging is necessary, it will purge both databases of data that
                                                      				is older than the number of months specified in this field. |
| Step 4 | From the
                                                   			 drop-down list in the Purge run time field, specify the required number of
                                                   			 hours. If the system
                                                      				determines that purging is necessary, it will purge both databases of data
                                                      				within the specified duration of time. |
| Step 5 | From the
                                                   			 drop-down list in the Initiate automatic purge when database size exceeds
                                                   			 field, accept the default, or choose another number. |
| Step 6 | From the
                                                   			 drop-down menu in the Auto purge data for the oldest field, accept the default
                                                   			 of 15 , or
                                                   			 choose another number. |
| Step 7 | From the
                                                   			 drop-down list in the initiate automatic purge when extent size exceeds field,
                                                   			 accept the default , or choose another number. |
| Step 8 | Click Update icon that displays in the tool bar in the
                                                   			 upper, left corner of the window or the Update button that displays at the bottom of the
                                                   			 window. The new purge
                                                      				schedule configuration is added to the Unified CCX system. |

| Field | Description |
|---|---|
| Purge Schedule |
| Daily
                                                                  							 purge at | Time
                                                                  							 of day for the daily purge along with the time zone. The time that appears here
                                                                  							 is based on the primary time zone, which is specified during initial setup of
                                                                  							 Unified CCX Administration. In a
                                                                  							 High Availability over WAN deployment, the purge schedule will happen at the
                                                                  							 time zone of the primary node. Note Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. | Note | Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. |
| Note | Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. |
| Purge
                                                                  							 data older than | Data
                                                                  							 can persist for a number of months before being purged. |
| Purge run time | The
                                                                  							 total duration for which the purge process should run. |
| Auto Purge Configuration |  |
| Initiate automatic purge when database exceeds | Percentage of the maximum database size at which an automatic
                                                                  							 purge is initiated (as compared to the total available size). |
| Initiate automatic purge when extent size exceeds | Percentage of the maximum extents size of any table above which
                                                                  							 an automatic purge is initiated. |
| Auto
                                                                  							 purge data for the oldest | Age of
                                                                  							 data to be purged. |

| Note | Unified CCX to Unified Intelligence Center sync runs as part of
                                                                                 								  the purge. It synchronizes the users, teams and grants Live Data report
                                                                                 								  permissions. |
|---|---|

| Note | Support for High
                                                   			 Availability is available only in multiple-server deployments. |
|---|---|

| Step 1 | From the Unified
                                                			 CCXAdministration menu bar, choose Tools > HistoricalReporting > Purge
                                                      				  Now . The
                                                   				Purge Now web page opens. The Purge data older than field is displayed in the
                                                   				Purge Now web page. You can specify this field in months and days. |
|---|---|
| Step 2 | From the
                                                			 drop-down list in the Purge data older than N months field, keep the default (13 months) or
                                                			 specify the required number of months. If the system
                                                   				determines that purging is necessary, it will purge both databases of data that
                                                   				is older than the number of months specified in this field. The Initiate
                                                   				automatic purge when database exceeds field displays the current historical
                                                   				database size as compared to the total available size. |
| Step 3 | From the
                                                			 drop-down list in the Purge data older than N days field, keep the default (15 days) or specify
                                                			 the required number of days. If the system
                                                   				determines that purging is necessary, it will purge both databases of data that
                                                   				is older than the number of days specified in this field. |
| Step 4 | From the
                                                			 drop-down list in the Purge run time, keep the default (7 hours) or specify the
                                                			 required number of hours. If the system
                                                   				determines that purging is necessary, it will purge both databases of data
                                                   				within the specified duration of the time . |
| Step 5 | Click Purge
                                                   				Now . The database
                                                   				purge is initiated in the server and the Purge Now area refreshes. |

| Report | Description |
|---|---|
| Application Tasks | Provides information about currently active applications. |
| Application Tasks Summary | Provides a summary of specific application activity. |
| Applications | Provides a list of all applications loaded on the Unified CCX server. |
| Contacts Summary | Provides information for call contacts, email contacts, and HTTP contacts. Also provides the total number of contacts. Note Calls made by the Outbound subsystem will not be displayed in the Contacts Summary Real-Time Report. | Note | Calls made by the Outbound subsystem will not be displayed in the Contacts Summary Real-Time Report. |
| Note | Calls made by the Outbound subsystem will not be displayed in the Contacts Summary Real-Time Report. |
| Contacts | Provides information about currently active contacts. |
| Chat CSQ Cisco Unified Contact Center Express Stats | Provides information about Chat CSQ activity. This report is available only if Unified CCX has been configured. |
| Chat Resource Cisco Unified Contact Center Express Stats | Provides information about Chat Unified CCX resources activity. |
| CSQ Cisco Unified Contact Center Express Stats | Provides information about CSQ activity. This report is available only if Unified CCX has been configured. |
| Data Source Usage | Provides information about configured data source names (DSNs). |
| Engine Tasks | Provides information about currently active Engine tasks. |
| Preview Outbound Campaign Cisco Unified Contact Center Express Stats | Provides information about real-time Unified CCX information for the Outbound preview dialer. |
| Outbound Campaign Stats | Provides real-time statistics on IVR and agent based progressive and predictive Outbound campaigns since the statistics were
                                                last reset. Note This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. | Note | This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. |
| Note | This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. |
| Overall Outbound Stats | Provides real-time statistics across all IVR and agent based progressive and predictive Outbound campaigns since the statistics
                                                were last reset. Note This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. | Note | This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. |
| Note | This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. |
| Overall Chat Cisco Unified Contact Center Express Stats | Provides information about Chat Unified CCX resources and contact information. This report is available only if Unified CCX
                                                has been configured. |
| Overall Cisco Unified Contact Center Express Stats | Provides information about Unified CCX resources and calls. This report is available only if Unified CCX has been configured. |
| Resource Cisco Unified Contact Center Express Stats | Provides information about Unified CCX resources activity. |
| Sessions | Provides information on all active sessions. |

| Note | Calls made by the Outbound subsystem will not be displayed in the Contacts Summary Real-Time Report. |
|---|---|

| Note | This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. |
|---|---|

| Note | This report will be available only if you have an Outbound license on top of the Unified CCX premium license in your Unified
                                                            CCX. |
|---|---|

| Note | Use Mozilla Firefox and Internet Explorer for Real Time Reporting. If you are using Mozilla Firefox, you must manually install the correct version of JRE to use real-time reports. |
|---|---|

| Step 1 | If you are
                                             			 running Real-Time Reporting for the first time on this system, log into Unified CCX Administration as an Administrator . The system
                                                				prompts you to download the Java plug-in; follow the prompt instructions. Note After you
                                                            				  perform the initial download of the Real-Time Reporting Java plug-in,
                                                            				  non-Administrative users can access Real-Time Reporting on this system. | Note | After you
                                                            				  perform the initial download of the Real-Time Reporting Java plug-in,
                                                            				  non-Administrative users can access Real-Time Reporting on this system. |
|---|---|---|---|
| Note | After you
                                                            				  perform the initial download of the Real-Time Reporting Java plug-in,
                                                            				  non-Administrative users can access Real-Time Reporting on this system. |
| Step 2 | Choose Tools > Real-Time
                                                   				  Reporting from the Unified CCX Administration menu bar. The
                                                				Application Reporting web page opens in a new window. The real-time reporting
                                                				tool requires a Java plug-in. If the plug-in is not installed on the machine
                                                				you are using, the Unified CCX system
                                                				prompts you to accept the automatic installation of the plug-in. If you do not
                                                				accept the installation, you cannot use real-time reporting. |

| Note | After you
                                                            				  perform the initial download of the Real-Time Reporting Java plug-in,
                                                            				  non-Administrative users can access Real-Time Reporting on this system. |
|---|---|

| Step 1 | From the
                                             			 Application Reporting menu bar, choose Reports . |
|---|---|
| Step 2 | From the
                                             			 Reports menu, choose the report to run. The report
                                                				opens in the Application Reporting window. |

| Step 1 | Run the Application Tasks, Contacts, Applications, or Sessions
                                             			 report. |
|---|---|
| Step 2 | Click a line in the report for which you want to view more
                                             			 detailed information. For example, click an email address in the Contacts
                                             			 report. |
| Step 3 | From the Application Reporting menu bar, choose Views and click the subreport that you want to
                                             			 run. You can also open a subreport by right-clicking the selected item
                                                				and choosing a subreport. The subreport opens. |

| Step 1 | Run a report. |
|---|---|
| Step 2 | From the Application Reporting menu, choose Tools > Open Printable
                                                   				  Report . A printable version of the report opens in a separate window. |
| Step 3 | Print the report using your browser print functionality. |

| Step 1 | From the
                                             			 Application Reporting menu bar, choose Tools > Reset All
                                                   				  Stats . The Reset
                                                				Stats dialog box opens for you to confirm the reset. |
|---|---|
| Step 2 | Click Yes . Accumulated
                                                				statistics are reset. |

| Step 1 | From the
                                             			 Application Reporting menu bar, choose Settings > Options . The Options
                                                				dialog box opens. |
|---|---|
| Step 2 | From the
                                             			 Polling Interval drop-down menu, choose the refresh rate in seconds. |
| Step 3 | From the
                                             			 Server Connect Retry Count drop-down menu, choose the number of times that the Unified CCX Administration web interface should attempt to reconnect to the Unified CCX server. |
| Step 4 | From the Show
                                             			 Logged Off Resources drop-down menu, choose whether logged-off agents appear in
                                             			 reports. |
| Step 5 | Click Apply to apply the settings. |

| Choose Settings from the Application Reporting menu bar
                                             		  and click the appearance that you want. |
|---|

| Note | Support for High
                                                			 Availability and remote servers is available only in multiple-server
                                                			 deployments. |
|---|---|

| Note | All real-time
                                                   			 reports display a Last Updated
                                                      				At field, which indicates the time of the snapshot. All summary reports
                                                   			 display both a start time (which indicates when the summary statistics started
                                                   			 being collected) and the current time. All real-time reports display a
                                                   			 Connected or Not Connected status for each node in the cluster. |
|---|---|

| Note | Support for High Availability and remote servers is available
                                                            				  only in multiple-server deployments. In case of island mode where each node (on either side of the
                                                            				  network) assumes mastership and handles calls, the real-time reports may not
                                                            				  report accurate data. |
|---|---|

| Failover
                                                      						Scenario | Connection Status | Node 1
                                                      						Status | Node 2
                                                      						Status |
|---|---|---|---|
| Both
                                                      						nodes are up | Fully
                                                      						Connected | Node ID
                                                      						current/start-time | Node ID
                                                      						current/start-time |
| Node 1
                                                      						is up Node 2
                                                      						is down | Partially Connected | Node ID
                                                      						current/start-time | Node ID
                                                      						Not Connected |
| Node 1
                                                      						is down Node 2
                                                      						is up | Partially Connected | Node ID
                                                      						Not Connected | Node ID
                                                      						current/start-time |
| Both
                                                      						nodes are down | Not
                                                      						Connected | Node ID
                                                      						Not Connected | Node ID
                                                      						Not Connected |

| Failover
                                                      						Scenario | Connection Status | Node 1
                                                      						Status | Node 2
                                                      						Status |
|---|---|---|---|
| Both
                                                      						nodes are up Node 1 is master | Fully
                                                      						Connected | Node ID
                                                      						current/start-time | Node ID
                                                      						Not Connected |
| Node 1
                                                      						is master Node 2
                                                      						is down | Fully
                                                      						Connected | Node ID
                                                      						current/start-time | Node ID
                                                      						Not Connected |
| Node 1
                                                      						is down Node 2
                                                      						is master | Fully
                                                      						Connected | Node ID
                                                      						Not Connected | Node ID
                                                      						current/start-time |
| Both
                                                      						nodes are down | Not
                                                      						Connected | Node ID
                                                      						Not Connected | Node ID
                                                      						Not Connected |

| Note | You display the
                                                      			 data on this report as numbers or percentages by clicking the Display
                                                      			 Value/Display % toggle button. |
|---|---|

| Field | Description |
|---|---|
| Active | Active
                                                      						contacts that are currently running. |
| Inbound | Number
                                                      						of inbound contacts since the statistics were last reset. |
| Outbound | Number
                                                      						of outbound contacts since the statistics were last reset. |
| Connected | Number
                                                      						of connected contacts since the statistics were last reset. Provides
                                                      						a total for contacts that are connected to resources (for example, a call
                                                      						connected to an ACD agent). |
| Terminated | Number
                                                      						of terminated contacts since the statistics were last reset. This row reports contacts that are ended generally by the application (for example, a caller stops responding and the application
                                                      terminates), indicating whether the contact was terminated: Locally—On the local server. Remotely—On a remote server in the cluster. Note Use
                                                                  						  the + toggle button to access these statistics. | Note | Use
                                                                  						  the + toggle button to access these statistics. |
| Note | Use
                                                                  						  the + toggle button to access these statistics. |
| Rejected | Number of rejected contacts since the statistics were last reset. This row reports contacts that are not accepted and processed (as a result, for example, of insufficient resources or the
                                                      rejection of the contact based on some customer-defined logic). Indicates the reason code for the reject: Channels busy No channel license No trigger Use the + toggle button to access these statistics. |
| Aborted | Number
                                                      						of aborted contacts since the statistics were last reset. This row
                                                      						reports contacts improperly ended by a task associated with the application (as
                                                      						when, for example, the system generates an exception or can not invoke the
                                                      						application because of some error in the application) and includes the
                                                      						associated Java exception code. Note Java
                                                                  						  exception codes are dynamic, as they can be generated from a variety of
                                                                  						  sources. Note Use
                                                                  						  the + toggle button to access these statistics. | Note | Java
                                                                  						  exception codes are dynamic, as they can be generated from a variety of
                                                                  						  sources. | Note | Use
                                                                  						  the + toggle button to access these statistics. |
| Note | Java
                                                                  						  exception codes are dynamic, as they can be generated from a variety of
                                                                  						  sources. |
| Note | Use
                                                                  						  the + toggle button to access these statistics. |
| Handled | Number
                                                      						of handled contacts since the statistics were last reset. This row
                                                      						reports contacts that are explicitly marked "Handled" by the application (typically when the application
                                                      						connects the contact to a Unified CCX agent). |
| Abandoned | Number
                                                      						of abandoned contacts since the statistics were last reset. This row
                                                      						reports contacts that end without being marked "Handled" by the application. |

| Note | Use
                                                                  						  the + toggle button to access these statistics. |
|---|---|

| Note | Java
                                                                  						  exception codes are dynamic, as they can be generated from a variety of
                                                                  						  sources. |
|---|---|

| Note | Use
                                                                  						  the + toggle button to access these statistics. |
|---|---|

| Field | Description |
|---|---|
| Application Name | Names of
                                                      						the applications that are running or have run. |
| Running | Currently running applications. |
| Completed | Applications that have stopped running. |
| Total | Number
                                                      						of times an application was invoked since the statistics were last reset. |
| DTMF VB
                                                      						and AA | Application names configured from the Unified CCX
                                                      						Administration. |
| Status | Displays
                                                      						the failover connection status. The possibilities are: Fully connected,
                                                      						Partially connected, and Not connected. See the following tables for detailed
                                                      						status information for Unified IP IVR and Unified CCX reports. |

| Field | Description |
|---|---|
| ID | Unique
                                                      						application task ID. |
| Node ID | Unique
                                                      						ID for a server in the cluster. |
| Application | Name of
                                                      						the application. |
| Start
                                                      						Time | Time
                                                      						when the application task started. |
| Duration | Length
                                                      						of time that the application has been active. |

| Note | If this report
                                                      			 indicates that an application is running for an unusually long time, there may
                                                      			 be a problem with the application. The application script may not include error
                                                      			 handling that prevents infinite retries if a call is no longer present. If the
                                                      			 application does not receive a disconnect signal after a call, the application
                                                      			 repeatedly retries to locate the call, and causes the application to run for an
                                                      			 unusually long time. To prevent this problem, include the proper error handling
                                                      			 in the application script. |
|---|---|

| Field | Description |
|---|---|
| ID | Unique
                                                      						identifier of the engine task. If the
                                                      						engine task is the main task running the application and the parent ID is
                                                      						empty, its identifier will match the Application Task Identifier. |
| Parent
                                                      						ID | Unique
                                                      						identifier for the parent of the engine task (if any). |
| Node ID | Unique
                                                      						identifier for a server in the cluster. |
| Server
                                                      						IP Address | IP
                                                      						address identifying the server in the cluster. |
| Script | Name of
                                                      						the script that is running the task (if the task is running a Unified CCX script). |
| Start
                                                      						Time | Time
                                                      						that the task started. |
| Duration | Length
                                                      						of time the task has been active. |

| Note | Support for High
                                                      			 Availability and remote servers is available only in multiple-server
                                                      			 deployments. |
|---|---|

| Field | Description |
|---|---|
| ID | Unique
                                                      						identifier representing a contact. |
| Type | Type of
                                                      						contact: Unified CM Telephony call, Cisco agent call, or |
| Impl ID | Unique
                                                      						identifier provided by the particular type of contact. For example, for a call
                                                         						  contact, this identifier would represent the Unified CM global
                                                         						  call ID. |
| Node ID | Unique
                                                      						identifier for a server in the cluster. |
| Start
                                                      						Time | Time
                                                      						stamp when the contact was created. |
| Duration | Length
                                                      						of time that the contact is active. |
| Handled | If True,
                                                      						the contact is handled; if False, the contact is not handled. |
| Aborting | If True,
                                                      						the contact is aborted with a default treatment; if False, the contact is not
                                                      						aborted. |
| Application | Name of
                                                      						the application currently managing the contact. |
| Task | Unique
                                                      						identifier of the application task that is currently responsible for the
                                                      						contact. |
| Session | Unique
                                                      						identifier of the session currently managing the contact (if any). |

| Note | The information
                                                      			 displayed is dependent on the type of contact selected. Depending on the type
                                                      			 of call, some fields may not be supported and will appear blank. |
|---|---|

| Field | Description |
|---|---|
| State | Current
                                                         						state of the contact. |
| Inbound | If True,
                                                         						this call was received by the Unified CCX server; if False,
                                                         						this call was placed as an outbound call by an application. |
| Language | The
                                                         						selected language context of the call. |
| Application ID | Unique
                                                         						identifier of the associated application. |
| Called
                                                         						Number | Called
                                                         						number for this call leg from the perspective of the called party. |
| Dialed
                                                         						Number | Dialed
                                                         						number for this call leg from the perspective of the calling party. |
| Calling
                                                         						Number | Calling
                                                         						number of the originator of this call. |
| ANI | Automatic number identification. |
| DNIS | Dialed
                                                         						number identification service. |
| CLID | Caller
                                                         						ID. |
| Arrival
                                                         						Type | Information on how the call contact arrived in the system. |
| Last
                                                         						Redirected Number | Number
                                                         						from which the last call diversion or transfer was invoked. |
| Original
                                                         						Called Number | Originally called number. |
| Original
                                                         						Dialed Number | Originally dialed number. |
| ANI
                                                         						Digits | Automatic Number Identification information indicator digit
                                                         						codes. |
| CED | Entered
                                                         						digits that were gathered by the network before the call was received. |

| Field | Description |
|---|---|
| State | Current
                                                         						state of the contact. |
| Inbound | If True,
                                                         						this email message was received by the Unified CCX server; if False,
                                                         						this email was created by an application. Note Inbound email messages are not currently supported. | Note | Inbound email messages are not currently supported. |
| Note | Inbound email messages are not currently supported. |
| Language | Selected
                                                         						language context of the email message. |
| Application ID | Unique
                                                         						identifier of the associated application. |
| From | Sender
                                                         						of this email message. |
| To | All the
                                                         						recipients of this email message. |
| Subject | "Subject" field of this
                                                         						email message. |
| Attachments | List of
                                                         						all attachments (file names) associated with this email message. |

| Note | Inbound email messages are not currently supported. |
|---|---|

| Field | Description |
|---|---|
| State | Current
                                                         						state of the contact. |
| Inbound | If True,
                                                         						this HTTP request was received by the Unified CCX server; if False,
                                                         						this HTTP request was created by an application. Note This
                                                                     						  information will always be reported as True, because the Unified CCX server does not
                                                                     						  currently track outbound HTTP requests in this way. | Note | This
                                                                     						  information will always be reported as True, because the Unified CCX server does not
                                                                     						  currently track outbound HTTP requests in this way. |
| Note | This
                                                                     						  information will always be reported as True, because the Unified CCX server does not
                                                                     						  currently track outbound HTTP requests in this way. |
| Language | Language
                                                         						currently associated with the HTTP request. |
| Application ID | Unique
                                                         						identifier of the associated application. |
| Authentication Type | Name of
                                                         						the authentication scheme used to protect the servlet; for example, "BASIC" or "SSL." |
| Character Encoding | Length,
                                                         						in bytes, of the request body, which is made available by the input stream, or
                                                         						-1 if the length is not known. Note This
                                                                     						  length is the same as the value of the CGI 1 variable CONTENT_LENGTH. | Note | This
                                                                     						  length is the same as the value of the CGI 1 variable CONTENT_LENGTH. |
| Note | This
                                                                     						  length is the same as the value of the CGI 1 variable CONTENT_LENGTH. |
| Content
                                                         						Length | MIME
                                                         						type of the body of the request, or null if the type is not known. Note This
                                                                     						  is the same as the value of the CGI variable CONTENT_TYPE. | Note | This
                                                                     						  is the same as the value of the CGI variable CONTENT_TYPE. |
| Note | This
                                                                     						  is the same as the value of the CGI variable CONTENT_TYPE. |
| Content
                                                         						Type | Type of
                                                         						HTTP contact request. |
| Request
                                                         						Language | Preferred language for client content (the language that the
                                                         						client accepts for its content), based on the Accept-Language header. |
| Path
                                                         						Info | Any
                                                         						extra path information associated with the URL the client sent when the HTTP
                                                         						request was made. |
| Protocol | Name and
                                                         						version of the protocol the request uses in the form: protocol/majorVersion.minorVersion ; for example,
                                                         						HTTP/1.1 Note This
                                                                     						  value is the same as the value of the CGI variable SERVER_PROTOCOL. | Note | This
                                                                     						  value is the same as the value of the CGI variable SERVER_PROTOCOL. |
| Note | This
                                                                     						  value is the same as the value of the CGI variable SERVER_PROTOCOL. |
| Remote
                                                         						Address | IP
                                                         						address of the client that sent the request Note This
                                                                     						  value is the same as the value of the CGI variable REMOTE_ADDR. | Note | This
                                                                     						  value is the same as the value of the CGI variable REMOTE_ADDR. |
| Note | This
                                                                     						  value is the same as the value of the CGI variable REMOTE_ADDR. |
| Remote
                                                         						Host | Fully
                                                         						qualified name of the client that sent the request, or the IP address of the
                                                         						client, if the name cannot be determined Note This
                                                                     						  value is the same as the value of the CGI variable REMOTE_HOST. | Note | This
                                                                     						  value is the same as the value of the CGI variable REMOTE_HOST. |
| Note | This
                                                                     						  value is the same as the value of the CGI variable REMOTE_HOST. |
| Remote
                                                         						User | Login
                                                         						of the user making this request, if the user has been authenticated. |
| Requested Session ID | HTTP
                                                         						session ID as specified by the client. |
| Request URL | Section of the URL of the HTTP request, from the protocol name
                                                         						up to the query string in the first line of the HTTP request. |

| Note | This
                                                                     						  information will always be reported as True, because the Unified CCX server does not
                                                                     						  currently track outbound HTTP requests in this way. |
|---|---|

| Note | This
                                                                     						  length is the same as the value of the CGI 1 variable CONTENT_LENGTH. |
|---|---|

| Note | This
                                                                     						  is the same as the value of the CGI variable CONTENT_TYPE. |
|---|---|

| Note | This
                                                                     						  value is the same as the value of the CGI variable SERVER_PROTOCOL. |
|---|---|

| Note | This
                                                                     						  value is the same as the value of the CGI variable REMOTE_ADDR. |
|---|---|

| Note | This
                                                                     						  value is the same as the value of the CGI variable REMOTE_HOST. |
|---|---|

| Field | Description |
|---|---|
| Name | Unique
                                                      						name of the currently loaded application. |
| ID | Application ID. |
| Type | Type of
                                                      						application that is currently running (for example, a Cisco Script
                                                      						Application). |
| Description | Description of the application as entered on the Unified CCX Administration web site. |
| Enabled | If True,
                                                      						the application is enabled; if False, the application is disabled. |
| Max.
                                                      						Sessions | Maximum
                                                      						number of simultaneous task instances that can run simultaneously on the Unified CCX server. |
| Valid | If True,
                                                      						the application is valid; if False, the application is invalid. 2 |

| Field | Description |
|---|---|
| ID | Session
                                                      						ID. Note This
                                                                  						  identifier is guaranteed to remain unique for a period of 12 months. | Note | This
                                                                  						  identifier is guaranteed to remain unique for a period of 12 months. |
| Note | This
                                                                  						  identifier is guaranteed to remain unique for a period of 12 months. |
| Mapping
                                                      						ID | User- or
                                                      						system-defined identifier that maps to this session. |
| Node ID | Unique
                                                      						identifier for a server in the cluster. |
| Parent | Sessions
                                                      						that were created as a result of consult calls propagated in the system. |
| Creation
                                                      						Time | Creation
                                                      						time of the session. |
| State | Current
                                                      						state of the session. Note When
                                                                  						  marked IDLE, the session is subject to being "garbage collected" by the system after a specified period of
                                                                  						  time. In addition, a session is IN_USE if it still has a contact associated or
                                                                  						  a child session. | Note | When
                                                                  						  marked IDLE, the session is subject to being "garbage collected" by the system after a specified period of
                                                                  						  time. In addition, a session is IN_USE if it still has a contact associated or
                                                                  						  a child session. |
| Note | When
                                                                  						  marked IDLE, the session is subject to being "garbage collected" by the system after a specified period of
                                                                  						  time. In addition, a session is IN_USE if it still has a contact associated or
                                                                  						  a child session. |
| Idle
                                                      						Time | Length
                                                      						of time that the session has been idle. |

| Note | This
                                                                  						  identifier is guaranteed to remain unique for a period of 12 months. |
|---|---|

| Note | When
                                                                  						  marked IDLE, the session is subject to being "garbage collected" by the system after a specified period of
                                                                  						  time. In addition, a session is IN_USE if it still has a contact associated or
                                                                  						  a child session. |
|---|---|

| Field | Description |
|---|---|
| Data Source Name | Name of the data source, as configured through the Unified
                                                      						CCXAdministration web interface. |
| Available Connections | Number of connections available. |
| Busy Connections | Number of busy connections. Note Busy + available = Maximum number of connections
                                                                  						  configured. | Note | Busy + available = Maximum number of connections
                                                                  						  configured. |
| Note | Busy + available = Maximum number of connections
                                                                  						  configured. |
| Checkouts Granted | Number of times the database connections have been used up
                                                      						since the statistics were last reset. |
| Checkouts Denied | Number of times the Database connections have been denied
                                                      						since the statistics were last reset. |

| Note | Busy + available = Maximum number of connections
                                                                  						  configured. |
|---|---|

| Note | Unified CCX
                                                      			 reports contain information for calls that have been queued in one or more
                                                      			 CSQs. If a call is not queued (for example, the caller hangs up before being
                                                      			 queued), the reports do not display data for that call. |
|---|---|

| Note | Preview Outbound
                                                      			 durations are updated when the preview outbound call disconnects and all agents
                                                      			 (resources) involved in the call move out of the Work and Talking state. |
|---|---|

| Field | Description |
|---|---|
| Resource Information |
| CSQs | Number
                                                      						of CSQs currently configured. If a CSQ is added or removed, this statistic
                                                      						reflects that change. |
| Logged-in Resources | Number
                                                      						of resources currently logged in. |
| Talking
                                                      						Resources | Number
                                                      						of resources currently talking. Note This
                                                                  						  number includes resources in Talking, Work, and Reserved states. | Note | This
                                                                  						  number includes resources in Talking, Work, and Reserved states. |
| Note | This
                                                                  						  number includes resources in Talking, Work, and Reserved states. |
| Ready
                                                      						Resources | Number
                                                      						of resources currently ready. |
| Not
                                                      						Ready Resources | Number
                                                      						of resources currently not ready. |
| Call Information —
                                                         						  Inbound |
| Total
                                                      						Contacts | Number
                                                      						of total contacts that have arrived since the statistics were last reset. This
                                                      						includes contacts that are waiting, contacts connected to a resource, and
                                                      						contacts that have disconnected. If a
                                                      						resource transfers to or conferences with a route point, this value increases. |
| Contacts
                                                      						Waiting | Number
                                                      						of contacts waiting to be connected to a resource. Note A
                                                                  						  contact is shown as waiting until the call is answered by the agent. This means that, even if the phone is
                                                                  						  ringing at the agent, the contact will still show as waiting in RTR. | Note | A
                                                                  						  contact is shown as waiting until the call is answered by the agent. This means that, even if the phone is
                                                                  						  ringing at the agent, the contact will still show as waiting in RTR. |
| Note | A
                                                                  						  contact is shown as waiting until the call is answered by the agent. This means that, even if the phone is
                                                                  						  ringing at the agent, the contact will still show as waiting in RTR. |
| Oldest Contact in Queue | Displays the wait time for the oldest contact in the queue. |
| Contacts
                                                      						Handled | Number
                                                      						of contacts that have been handled by a resource. |
| Contacts
                                                      						Abandoned | Number
                                                      						of contacts that have arrived and disconnected before being connected to a
                                                      						resource. |
| Avg Talk
                                                      						Duration | Average
                                                      						duration (in seconds) that resources spend talking on Unified CCX contacts.
                                                      						Talk duration starts when a contact first connects to a resource and ends when
                                                      						the contact disconnects from the last resource to which it was connected. Talk
                                                      						duration does not include hold time. |
| Avg
                                                      						Wait Duration | Average wait time (in seconds). It begins when the contact
                                                      						enters the system and ends when the contact stops waiting. Wait duration does
                                                      						not include hold time. The time a contact spends on a CTI port prior to getting
                                                      						queued is included in this report. |
| Longest Talk Duration | Longest talk duration (in seconds) of a contact. Talk duration
                                                      						does not include hold time. |
| Longest Wait Duration | Longest wait (in seconds) for a contact to be connected to a
                                                      						resource. Wait duration does not include hold time. |
| Call Information —
                                                         						  Preview Outbound |
| Active | Total
                                                      						number of preview outbound calls currently previewed or connected to agents. |
| Preview | Total
                                                      						number of preview outbound calls currently previewed but have not been
                                                      						accepted, rejected. or closed by the agents. |
| Connected | Total
                                                      						number of preview outbound calls currently connected to agents. When an agent
                                                      						conferences in other agents, the call is counted once towards the total number
                                                      						of connected calls. |
| Offered | Total
                                                      						number of preview outbound calls offered. A call is considered offered when it
                                                      						is presented to an agent. A contact that is presented to an agent,
                                                      						skipped/rejected by that agent, and then presented to the same agent or to
                                                      						another agent is counted twice towards the number of calls offered. Offered =
                                                      						Accepted + Rejected + Closed + Timed-out. |
| Accepted | Total
                                                      						number of preview outbound calls accepted. A call is considered accepted if an
                                                      						agent has clicked Accept when presented the call. A call that is presented to
                                                      						an agent, skipped/rejected by that agent, presented to another agent, and then
                                                      						accepted by that other agent is counted once towards the number of calls
                                                      						accepted. |
| Rejected | The
                                                      						number of preview outbound calls that were skipped or rejected by an agent.
                                                      						This means that the agent selected Reject, Skip, or Cancel Reservation. These
                                                      						contacts will be dialed again. If a contact is rejected by multiple agents,
                                                      						this field increments each time the contact is rejected. The
                                                      						number Rejected is also incremented each time an agent drops the preview call
                                                      						while it is ringing at the customer’s contact. |
| Closed | The
                                                      						number of preview outbound contacts that were closed by agents. This means that
                                                      						the agent selected Skip-Close or Reject-close. These contacts will not be
                                                      						dialed again. |
| Timed-Out | Total
                                                      						number of preview outbound calls that timed out. A call is considered timed out
                                                      						when it is presented to an agent and not accepted, rejected, or closed within
                                                      						the allocated time. These contacts will be dialed again. If a contact timed out
                                                      						multiple agents, this field is incremented each time the contact is timed out
                                                      						for each agent. |
| Invalid Number | The
                                                      						number of preview outbound calls that were dialed to an invalid number. This
                                                      						means that the agent accepted the call (by clicking Accept), got connected to
                                                      						the customer, and selected the Invalid Number option from the contact
                                                      						Reclassification drop down. It also includes the number of preview outbound
                                                      						calls that failed at the network level. Note The
                                                                  						  agent can manually reclassify the contact as Invalid Number while the customer
                                                                  						  contact is on the call or when the agent has gone into the Work state after the
                                                                  						  call. | Note | The
                                                                  						  agent can manually reclassify the contact as Invalid Number while the customer
                                                                  						  contact is on the call or when the agent has gone into the Work state after the
                                                                  						  call. |
| Note | The
                                                                  						  agent can manually reclassify the contact as Invalid Number while the customer
                                                                  						  contact is on the call or when the agent has gone into the Work state after the
                                                                  						  call. |
| Voice | The
                                                      						number of preview outbound calls that ended in successful customer contact.
                                                      						This means that an agent accepted the call (by clicking Accept) and selected a classification of Voice (default) or Do Not
                                                      						Call for this contact. |
| Answering Machine | The
                                                      						number of preview outbound calls that connected to an answering machine for
                                                      						this campaign. This means that the agent accepted the call (by clicking
                                                      						Accept), got connected to the answering machine and selected the Answering
                                                      						Machine option from the contact Reclassification drop down. Note The
                                                                  						  agent can manually reclassify the contact as Answering Machine while the
                                                                  						  customer contact is on the call or when the agent has gone into the Work state
                                                                  						  after the call. | Note | The
                                                                  						  agent can manually reclassify the contact as Answering Machine while the
                                                                  						  customer contact is on the call or when the agent has gone into the Work state
                                                                  						  after the call. |
| Note | The
                                                                  						  agent can manually reclassify the contact as Answering Machine while the
                                                                  						  customer contact is on the call or when the agent has gone into the Work state
                                                                  						  after the call. |
| Requested Callback | The
                                                      						number of contacts marked for callback. This means that the agent accepted the
                                                      						call (by clicking Accept), got connected to the contact, the contact requested
                                                      						a callback, and the agent selected the CallBack option. A call that is accepted
                                                      						by an agent, marked for callback, later presented to and accepted by another
                                                      						agent (at the callback time), and marked for callback again is counted twice
                                                      						towards the number of callback calls. |
| Avg Outbound Talk Duration | The average time in HH:MM:SS (hours, minutes, seconds) that
                                                      						agents spend talking on outbound calls. The durations consider all calls that
                                                      						were Agent Accepted and classified as Voice. If a preview outbound call is
                                                      						transferred or conferenced to a route point, this average outbound talk
                                                      						duration does not include the talk time of agents who handle the call after it
                                                      						came through the route point. Instead, the talk time is included in the inbound
                                                      						talk duration. |
| Longest Outbound Talk Duration | The longest talk duration of a preview outbound call in
                                                      						HH:MM:SS (hours, minutes, seconds). The durations consider all calls that were
                                                      						Agent Accepted and classified as Voice. |

| Note | This
                                                                  						  number includes resources in Talking, Work, and Reserved states. |
|---|---|

| Note | A
                                                                  						  contact is shown as waiting until the call is answered by the agent. This means that, even if the phone is
                                                                  						  ringing at the agent, the contact will still show as waiting in RTR. |
|---|---|

| Note | The
                                                                  						  agent can manually reclassify the contact as Invalid Number while the customer
                                                                  						  contact is on the call or when the agent has gone into the Work state after the
                                                                  						  call. |
|---|---|

| Note | The
                                                                  						  agent can manually reclassify the contact as Answering Machine while the
                                                                  						  customer contact is on the call or when the agent has gone into the Work state
                                                                  						  after the call. |
|---|---|

| Note | Unified CCX reports contain information for calls that have been
                                                      			 queued in one or more CSQs. If a call is not queued, the reports do not display
                                                      			 data for that call. . |
|---|---|

| Field | Description |
|---|---|
| Name | Name of the CSQ. |
| Talking/Ready Resources/Not Ready Resources/Logged-In
                                                      						Resources | Number of resources who are in the talking, ready, and not
                                                      						ready states, and the number of resources logged in for this CSQ. Values for
                                                      						the four items are separated by colons. Values are displayed in the same order
                                                      						that the items appear in the column heading. Note This number includes resources in Talking, Work, and
                                                                  						  Reserved states. If you are logged into the Unified CCX Administration web
                                                                  						  interface as a Supervisor and opening the Real-Time Reporting plug-in, you will
                                                                  						  be able see all the logged in agents from all the teams independent of team
                                                                  						  membership. | Note | This number includes resources in Talking, Work, and
                                                                  						  Reserved states. If you are logged into the Unified CCX Administration web
                                                                  						  interface as a Supervisor and opening the Real-Time Reporting plug-in, you will
                                                                  						  be able see all the logged in agents from all the teams independent of team
                                                                  						  membership. |
| Note | This number includes resources in Talking, Work, and
                                                                  						  Reserved states. If you are logged into the Unified CCX Administration web
                                                                  						  interface as a Supervisor and opening the Real-Time Reporting plug-in, you will
                                                                  						  be able see all the logged in agents from all the teams independent of team
                                                                  						  membership. |
| Total Contacts | Number of total contacts since the statistics were last
                                                      						reset for this CSQ. |
| Contacts Waiting | Number of contacts waiting to be connected to a resource in
                                                      						this CSQ. This column also displays how long the oldest contact has
                                                      						been waiting. |
| Contacts [oldest contact in queue] | Duration of longest currently waiting contact. |
| Contacts Handled | Number of contacts that have been handled by this CSQ. |
| Contacts Abandoned | Number of contacts that have been abandoned by this CSQ. |
| Contacts Dequeued | Number of contacts that have been dequeued from this CSQ. |
| Avg Talk Duration | Average time (in seconds) agents in this CSQ spent talking
                                                      						to contacts. |
| Avg Wait Duration | Average wait time (in seconds). It begins when the call was queued (when you run the "Select Resource" step) and ends when the call reaches the agent. Wait duration does not include hold time.The time a contact spends on a CTI
                                                      port prior to getting queued is not included in this wait time. |
| Longest Talk Duration | Longest time (in seconds) agents in this CSQ spend talking
                                                      						to contacts. |
| Longest Wait Duration | Longest wait (in seconds) for a contact to be connected to a
                                                      						resource. |

| Note | This number includes resources in Talking, Work, and
                                                                  						  Reserved states. If you are logged into the Unified CCX Administration web
                                                                  						  interface as a Supervisor and opening the Real-Time Reporting plug-in, you will
                                                                  						  be able see all the logged in agents from all the teams independent of team
                                                                  						  membership. |
|---|---|

| Field | Description |
|---|---|
| Campaign | The name of the preview outbound campaign. |
| Status | The current activation state of the preview outbound campaign: Running: an active preview outbound campaign Stopped: an inactive preview outbound campaign |
| Active | Total number of outbound calls currently previewed by or connected to agents for this preview outbound campaign. Active Calls
                                                      = Previewed + Connected. |
| Preview | Total number of outbound calls currently previewed but have not been accepted, rejected or closed by the agents as part of
                                                      this preview outbound campaign. |
| Connected | Total number of outbound calls currently connected to agents for this preview outbound campaign. When an agent conferences
                                                      in other agents, the call is counted once towards the total number of connected calls. |
| Offered | Total number of outbound calls offered for this preview outbound campaign. A call is considered offered when it is presented
                                                      to an agent as part of this preview outbound campaign. A contact that is presented to an agent, rejected by that agent, and
                                                      then presented to the same agent or to another agent is counted twice towards the number of calls offered. Offered = Accepted
                                                      + Rejected + Closed + Timed-out. |
| Accepted | Total number of outbound calls accepted for this preview outbound campaign. A call is considered accepted if an agent has
                                                      clicked Accept when presented the call. A call that is presented to an agent, rejected by that agent, presented to another
                                                      agent, and then accepted by that other agent is counted once towards the number of calls accepted. |
| Rejected | The number of outbound calls that were rejected by an agent as part of this preview outbound campaign. This means that the
                                                      agent selected Reject or Cancel Reservation. These contacts will be dialed again. If a contact is rejected by multiple agents, this field increments
                                                      each time the contact is rejected. The number Rejected is also incremented each time an agent drops the preview call while it is ringing at the customer contact. |
| Closed | The number of outbound contacts that were closed by agents as part of this preview outbound campaign. This means that the
                                                      agent selected Reject-close. These contacts will not be dialed again. |
| Timed-Out | Total number of outbound calls that timed out. A call is considered timed out when it is presented to an agent and not accepted,
                                                      rejected, or closed within the allocated time. These contacts will be dialed again. If a contact times out for multiple agents,
                                                      this field is incremented each time the contact is timed out for each agent. |
| Invalid Number | The number of outbound calls that were dialed to an invalid number for this preview outbound campaign. This means that the
                                                      agent accepted the call (by clicking Accept), got connected to the customer, and selected the "Invalid Number" option from the contact Reclassification drop down. It also includes the number of outbound calls that failed at the network
                                                      level. Note The agent can manually reclassify the contact as Invalid Number while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. | Note | The agent can manually reclassify the contact as Invalid Number while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. |
| Note | The agent can manually reclassify the contact as Invalid Number while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. |
| Voice | The number of outbound calls that ended in successful customer contact. This means that an agent accepted the call (by clicking
                                                      Accept) and selected a classification of Voice or Do Not Call for this contact. |
| Answering Machine | The number of outbound calls that connected to an answering machine for this preview outbound campaign. This means that the
                                                      agent accepted the call (by clicking Accept), got connected to the answering machine and selected the Answering Machine option
                                                      from the contact Reclassification drop down. Note The agent can manually reclassify the contact as Answering Machine while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. | Note | The agent can manually reclassify the contact as Answering Machine while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. |
| Note | The agent can manually reclassify the contact as Answering Machine while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. |
| Requested Callback | The number of contacts marked for callback for this preview outbound campaign. This means that the agent accepted the call
                                                      (by clicking Accept), got connected to the contact, the contact requested a callback, and the agent selected the CallBack
                                                      option. A call that is accepted by an agent, marked for callback, later presented to and accepted by another agent (at the
                                                      callback time), and marked for callback again is counted twice towards the number of callback calls. |
| Avg Talk Duration | The average time in HH:MM:SS (hours, minutes, seconds) that agents spend talking on outbound calls for this preview outbound
                                                      campaign. The durations consider all calls that were Agent Accepted and classified as Voice. If a call is transferred or conferenced
                                                      back to the route point, the preview outbound campaign talk duration does not handle the talk time of agents who handle the
                                                      call after it came through the route point. |
| Longest Talk Duration | The longest talk duration of an outbound call in HH:MM:SS (hours, minutes, seconds) for this preview outbound campaign. The
                                                      durations consider all calls that were Agent Accepted and classified as Voice. |

| Note | The agent can manually reclassify the contact as Invalid Number while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. |
|---|---|

| Note | The agent can manually reclassify the contact as Answering Machine while the customer contact is on the call or when the agent
                                                                  has gone into the Work state after the call. |
|---|---|

| Note | Unified CCX reports contain information for a chat contact that are queued with a specific CSQ. If a contact is not queued,
                                                      the reports do not display data for that chat contact. |
|---|---|

| Field | Description |
|---|---|
| Name | Name of the chat CSQ |
| Busy Resources/ Ready Resources/ Not Ready Resources/ Logged-In Resources | Number of resources who are in the Busy, Ready, and Not Ready states, and the number of agents logged in for this chat CSQ.
                                                      Values for the four items are separated by colons. Values are displayed in the same order that the items appear in the column
                                                      heading. Note If you are logged in to the Unified CCX Administration web interface as a supervisor and you open the Real-Time Reporting
                                                                  plug-in, you can see all the logged-in agents from all the teams. | Note | If you are logged in to the Unified CCX Administration web interface as a supervisor and you open the Real-Time Reporting
                                                                  plug-in, you can see all the logged-in agents from all the teams. |
| Note | If you are logged in to the Unified CCX Administration web interface as a supervisor and you open the Real-Time Reporting
                                                                  plug-in, you can see all the logged-in agents from all the teams. |
| Total Contacts | Number of total contacts presented to this queue since last reset of statistics. |
| Contacts Waiting [Oldest Contact in Queue] | Number of contacts waiting in this queue with the duration of longest waiting contact in this queue. |
| Contacts Handled | Number of contacts that have been handled by this queue since last reset of statistics. |
| Contacts Abandoned | Number of contacts that have been abandoned in this queue since last reset of statistics. |
| Avg Contact Handling Duration | Average time (in HH:MM:SS) agents in this CSQ spent chatting with contacts. |
| Avg Wait Duration | Average wait time (in HH:MM:SS) a contact spent in queue waiting for an agent. |
| Longest Contact Handling Duration | Longest time (in HH:MM:SS) agents in this CSQ spent chatting with contacts. |
| Longest Wait Duration | Longest wait (in HH:MM:SS) for a contact to be connected to an agent. |

| Note | If you are logged in to the Unified CCX Administration web interface as a supervisor and you open the Real-Time Reporting
                                                                  plug-in, you can see all the logged-in agents from all the teams. |
|---|---|

| Field | Description |
|---|---|
| Name
                                                      						(ID) | Unique
                                                      						identifier of the resource. |
| State | Current
                                                      						state of the resource. |
| Current Active Contacts | Number of active contacts that the agent is handling. |
| Duration
                                                      						in State | Length
                                                      						of time (in HH:MM:SS) the resource has remained in the current state. |
| Avg
                                                      						Resource Busy Duration | Average
                                                      						time the agent spent with contacts. The resource busy duration is the elapsed
                                                      						time between the resource accepting the contact and completing the chat by
                                                      						clicking End. |
| Longest
                                                      						Resource Busy Duration | Longest
                                                      						time the agent spent with a contact. The resource busy duration is the elapsed
                                                      						time between the resource accepting the contact and completing the chat by
                                                      						clicking End. |
| Contacts
                                                      						Presented | Number
                                                      						of contacts that have been presented to this resource. |
| Contacts
                                                      						Handled | Number
                                                      						of contacts that have been handled by this resource. |

| Note | Unified CCX reports contain information for contacts that have been queued in one or more CSQs. If a contact is not queued,
                                                      the reports do not display data for that contact. |
|---|---|

| Field | Description |
|---|---|
| Resource Information |
| CSQs | Number of chat CSQs currently configured. If a chat CSQ is added or removed, this statistic reflects that change. |
| Logged-in Resources | Number of resources currently logged in. |
| Busy Resources | Number of resources currently busy. |
| Ready Resources | Number of resources currently ready. |
| Not Ready Resources | Number of resources currently not ready. |
| Contact Information |
| Total Contacts | Number of total contacts that have arrived since the statistics were last reset. This includes contacts that are waiting,
                                                      contacts connected to a resource, and contacts that have disconnected. |
| Contacts Waiting | Number of contacts waiting to be connected to a resource. Note A contact is shown as waiting until the contact is answered by the agent. | Note | A contact is shown as waiting until the contact is answered by the agent. |
| Note | A contact is shown as waiting until the contact is answered by the agent. |
| Oldest Contact in Queue | Displays the wait time for the oldest contact in the queue. |
| Contacts Handled | Number of contacts that have been handled by a resource. |
| Contacts Abandoned | Number of contacts that are routed to the CSQ since midnight but are abandoned due to one of the following: Customer ended the chat as the chat was not answered by an agent. Customer chat was disconnected. No agents were available. All agents were busy. |
| Avg Contact Handling Duration | Average duration (in HH:MM:SS) that resources spent chatting on Unified CCX contacts. Chat duration starts when a contact
                                                      first connects to a resource and ends when the contact disconnects from the resource to which it was connected. |
| Avg Wait Duration | Average wait time (in HH:MM:SS). It begins when the contact enters the system and ends when either the contact is connected
                                                      with an agent or if contact was disconnected. |
| Longest Contact Handling Duration | Longest contact handling duration (in HH:MM:SS) of a contact. |
| Longest Wait Duration | Longest wait (in HH:MM:SS) for a contact to be connected to a resource. |

| Note | A contact is shown as waiting until the contact is answered by the agent. |
|---|---|

| Note | The call related fields display the data from the time the
                                                      			 statistics were last reset. |
|---|---|

| Field | Description |
|---|---|
| Campaign
                                                      						Name | The name
                                                      						of the IVR-based or agent-based progressive or predictive campaign. |
| Status | The
                                                      						current activation state of the campaign: Running: an active
                                                         						  IVR-based or agent-based progressive or predictive campaign. Stopped: an inactive
                                                         						  IVR-based or agent-based progressive or predictive campaign. |
| Campaign
                                                      						Type | The
                                                      						dialer type of the campaign, which can be one of the following: IVR Progressive IVR Predictive Agent Progressive Agent Predictive |
| Attempted | The
                                                      						total number of attempted calls. If there
                                                      						are no customer abandoned calls, then Attempted will be equal to sum of the
                                                      						following counters: Voice + Answering Machine + Invalid Number + Fax/Modem + No
                                                      						Answer + Busy + Failed. |
| Voice | The
                                                      						total number of calls that are connected to live voice. Note The
                                                                  						  call will be marked as System Abandoned after it has been marked as Voice and
                                                                  						  Active due to any of the following reasons: Whenever there is an exception while running some steps in an IVR script in case of IVR-based campaigns. For example, if there
                                                                           is any codec mismatch issue, there will be an exception in the Accept Step. In such cases, the same call will be marked in
                                                                           the following three categories voice, active, and system abandoned. Whenever the call that is ringing on the agent's phone
                                                                           								fails in case of agent-based campaigns. | Note | The
                                                                  						  call will be marked as System Abandoned after it has been marked as Voice and
                                                                  						  Active due to any of the following reasons: Whenever there is an exception while running some steps in an IVR script in case of IVR-based campaigns. For example, if there
                                                                           is any codec mismatch issue, there will be an exception in the Accept Step. In such cases, the same call will be marked in
                                                                           the following three categories voice, active, and system abandoned. Whenever the call that is ringing on the agent's phone
                                                                           								fails in case of agent-based campaigns. |
| Note | The
                                                                  						  call will be marked as System Abandoned after it has been marked as Voice and
                                                                  						  Active due to any of the following reasons: Whenever there is an exception while running some steps in an IVR script in case of IVR-based campaigns. For example, if there
                                                                           is any codec mismatch issue, there will be an exception in the Accept Step. In such cases, the same call will be marked in
                                                                           the following three categories voice, active, and system abandoned. Whenever the call that is ringing on the agent's phone
                                                                           								fails in case of agent-based campaigns. |
| Answering Machine | The
                                                      						total number of calls that reached an answering machine. |
| Invalid
                                                      						Number | The
                                                      						total number of calls that reached an invalid number: A failed call when the
                                                         						  gateway returns an invalid or not found error. |
| Fax/Modem | The
                                                      						total number of calls that reached fax or modem. |
| No
                                                      						Answer | The
                                                      						total number of calls that were not answered within the time configured for the
                                                      						No Answer Ring Limit field in the Add New Campaign web page. |
| Busy | The
                                                      						total number of calls that reached a busy destination. |
| Failed | The
                                                      						total number of calls that failed due to any one of the following reasons: Dialer asked the Gateway to
                                                         						  cancel a call that was dialed out, but not connected. Gateway has declined the
                                                         						  call. Gateway failure or
                                                         						  configuration issues at the Gateway. Gateway is down. |
| Active | The
                                                      						total number of calls that were connected to IVR ports or agents. All the
                                                      						voice calls that will be connected to Outbound IVR ports or agents will be
                                                      						marked as active. If you have selected Answering Machine Treatment or Abandoned
                                                      						Call Treatment as "Transfer to IVR," the answering machine calls and abandoned
                                                      						calls that are getting transferred to Outbound IVR ports will also be marked as
                                                      						active. |
| Customer
                                                      						Abandoned | The
                                                      						total number of calls that were disconnected by the customer or agent within
                                                      						the Abandoned Call Wait Time configured in Add New Campaign web page. |
| System
                                                      						Abandoned | The
                                                      						total number of calls that were abandoned due to any of the following reasons: Non-availability of ports
                                                         						  or agents. Any issues at system
                                                         						  level. |
| Abandon Rate (in %) | Abandon Rate = (System Abandoned/Voice)*100 |

| Note | The
                                                                  						  call will be marked as System Abandoned after it has been marked as Voice and
                                                                  						  Active due to any of the following reasons: Whenever there is an exception while running some steps in an IVR script in case of IVR-based campaigns. For example, if there
                                                                           is any codec mismatch issue, there will be an exception in the Accept Step. In such cases, the same call will be marked in
                                                                           the following three categories voice, active, and system abandoned. Whenever the call that is ringing on the agent's phone
                                                                           								fails in case of agent-based campaigns. |
|---|---|

| Note | If you have selected Answering Machine Treatment as "End Call"
                                                            				  for an IVR or agent based outbound campaign through Campaign Configuration web
                                                            				  page, then Voice = Active + System Abandoned. If you have selected Answering Machine Treatment or Abandoned
                                                            				  Call Treatment as "Transfer to IVR" for an IVR or agent based outbound campaign
                                                            				  through Campaign Configuration web page, then Voice + Answering Machine =
                                                            				  Active + System Abandoned. |
|---|---|

| Note | The call related fields display the data from the time the
                                                      			 statistics were last reset. |
|---|---|

| Field | Description |
|---|---|
| Attempted | The
                                                      						total number of attempted Outbound calls. |
| Voice | The
                                                      						total number of Outbound calls that were connected to live voice. |
| Answering Machine | The
                                                      						total number of Outbound calls that reached answering machine. |
| Invalid
                                                      						Number | The
                                                      						total number of Outbound calls that reached an invalid number. |
| Fax/Modem | The
                                                      						total number of Outbound calls that reached fax or modem. |
| No
                                                      						Answer | The
                                                      						total number of Outbound calls that were not answered. |
| Busy | The
                                                      						total number of Outbound calls that reached a busy destination. |
| Failed | The
                                                      						total number of failed Outbound calls for all IVR and agent based Outbound
                                                      						campaigns. |
| Active | The
                                                      						total number of Outbound calls that were connected to Outbound IVR ports or
                                                      						agents. |
| Customer
                                                      						Abandoned | The
                                                      						total number of Outbound calls that were abandoned by the customer or
                                                      						disconnected by the agent. |
| System
                                                      						Abandoned | The
                                                      						total number of Outbound calls that were abandoned by the system. |

| Note | If multiple
                                                      			 lines are configured for an agent, only the calls on the agent's primary
                                                      			 extension are reported in Resource Cisco Unified Contact Center Express Stats
                                                      			 report. |
|---|---|

| Field | Description |
|---|---|
| Name
                                                      						(ID) | Unique
                                                      						identifier of the agent. |
| State | Current
                                                      						state of the agent. |
| Duration
                                                      						in State | Amount
                                                      						of time (in seconds) the agent has remained in the current state. |
| Contacts
                                                      						Presented | Number
                                                      						of contacts presented to the agent. |
| Contacts
                                                      						Handled | Number
                                                      						of contacts handled by the agent. |
| Avg Talk
                                                      						Duration | Average
                                                      						time (in seconds) the agent spent in talking state. |
| Avg Hold
                                                      						Duration | Average
                                                      						time (in seconds) the agent keeps calls on hold. |
| Longest
                                                      						Talk Duration | Longest
                                                      						time (in seconds) the agent spent in talking state. |
| Longest
                                                      						Hold Duration | Longest
                                                      						time (in seconds) the agent keeps a call on hold. |
| Outbound
                                                      						Offered | Total
                                                      						number of preview outbound calls offered to the agent. A call is considered
                                                      						offered when it is presented to an agent. The number of calls offered is
                                                      						counted twice if a contact that is presented to an agent is skipped/rejected by
                                                      						that agent and then the contact is presented to the same agent or to another
                                                      						agent. Offered = Accepted + Rejected + Closed + Timed-out. |
| Outbound
                                                      						Accepted | Total
                                                      						number of outbound calls accepted by the agent. For transferred or conferenced
                                                      						outbound calls, the call is considered accepted if it is answered by the agent. A
                                                      						preview outbound call is considered accepted if an agent has clicked Accept to
                                                      						accept the call and then the system places the call to the customer. The number
                                                      						of calls accepted is counted once if a call that is presented to an agent is
                                                      						skipped/rejected by that agent and then the call is presented to another agent
                                                      						who accepts the call. A progressive or predictive outbound call is considered accepted if an agent has answered a live voice call that is presented
                                                      to the agent (if Agent AutoAnswer is disabled). |
| Outbound
                                                      						Rejected | The
                                                      						number of preview outbound calls skipped/rejected by the agent. This means that
                                                      						the agent selected Reject, Skip, or Cancel Reservation. These contacts will be
                                                      						dialed again. The
                                                      						number of calls rejected is also incremented each time an agent drops the
                                                      						preview call while it is ringing at the customer’s contact. |
| Outbound
                                                      						Closed | The
                                                      						number of contacts closed by the agent for preview outbound. This means that
                                                      						the agent selected Skip-Close or Reject-close. These contacts will not be
                                                      						dialed again. |
| Outbound
                                                      						Timed-Out | Total
                                                      						number of preview outbound calls that timed out. A call is considered timed out
                                                      						when the call is presented to an agent but not accepted, rejected, or closed
                                                      						within the allocated time. These contacts will be dialed again. If a contact
                                                      						timed out for multiple agents, this field is incremented each time the contact
                                                      						is timed out for each agent. |
| Outbound
                                                      						Voice | The
                                                      						number of preview outbound calls that ended in successful customer contact for
                                                      						the agent. This means that the agent accepted the call (by clicking Accept) and selected a classification of Voice or Do Not Call for
                                                      						this contact. |
| Outbound
                                                      						Avg Talk Duration | The
                                                      						average time in HH:MM:SS (hours, minutes, seconds) that the agent spends in
                                                      						talking state for outbound calls. This talk duration also includes the time
                                                      						spent on outbound calls that were transferred or conferenced to a route point. For
                                                      						preview outbound, the talk duration considers all calls that were Agent
                                                      						Accepted and classified as Voice. |
| Outbound Avg Hold Duration | The
                                                      						average time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                                      						holding an outbound call. For
                                                      						preview outbound, the hold duration considers all calls that were Agent
                                                      						Accepted and classified as Voice. |
| Outbound Longest Talk Duration | The
                                                      						longest time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                                      						talking state for an outbound call . For
                                                      						preview outbound, the talk duration considers all calls that were Agent
                                                      						Accepted and classified as Voice. |
| Outbound Longest Hold Duration | The
                                                      						longest time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                                      						holding an outbound call. For
                                                      						preview outbound, the hold duration considers all calls that were Agent
                                                      						Accepted and classified as Voice. |

| Note | The Unified CCX
                                                      			 system automatically resets all statistics each day at midnight. |
|---|---|

| Choose Tools > Reset All
                                                         				  Statistics from the Application Reporting menu bar. |
|---|

| Choose a real-time report from the Report menu option and then Tools > Open Printable
                                                         				  Report from the Application Reporting menu bar. |
|---|

| Choose Tools > Refresh
                                                         				  Connections from the Application Reporting menu bar. The Unified
                                                         				  CCX system
                                                      				refreshes all connections. |
|---|

| Step 1 | Choose the contact from Reports > Contacts . |
|---|---|
| Step 2 | From the Application Reporting menu bar, choose Tools > Clear
                                                            				  Contact . A Clear Call dialog box is displayed to warn
                                                      			 you. If you want to continue with the clear action, click No . To cancel the action, click Yes . |
| Step 3 | Click No to proceed with the clear action. A Clear
                                                      			 Contact dialog box is displayed for you to confirm the action. You can click Yes to proceed or No to cancel. |
| Step 4 | Click Yes . The Unified CCX system removes the
                                                      			 contact from all its queues. |

| Step 1 | Choose Reports > Overall Cisco
                                                            				  Unified Contact Center Express Stats . |
|---|---|
| Step 2 | Choose the contact from Views and click Overall Waiting Contacts Info . Note Please note that the Overall Waiting Contacts Info menu option
                                                                     				  displays only those calls that are queued in CSQs and not agent-based routing
                                                                     				  calls. | Note | Please note that the Overall Waiting Contacts Info menu option
                                                                     				  displays only those calls that are queued in CSQs and not agent-based routing
                                                                     				  calls. |
| Note | Please note that the Overall Waiting Contacts Info menu option
                                                                     				  displays only those calls that are queued in CSQs and not agent-based routing
                                                                     				  calls. |
| Step 3 | From the Application Reporting menu bar, choose Tools and click Clear Contact . A Clear Call dialog box is
                                                      			 displayed to warn you. If you want to continue with the clear action, click No . To cancel the action, click Yes . |
| Step 4 | Click No to proceed with the clear action. A Clear
                                                      			 Contact dialog box is displayed for you to confirm the action. You can click Yes to proceed or No to cancel. |
| Step 5 | Click Yes . The Unified CCX system removes the
                                                      				contact from all its queues. |

| Note | Please note that the Overall Waiting Contacts Info menu option
                                                                     				  displays only those calls that are queued in CSQs and not agent-based routing
                                                                     				  calls. |
|---|---|

| Step 1 | Choose Reports > CSQ Cisco
                                                            				  Unified Contact Center Express Stats . |
|---|---|
| Step 2 | Choose the contact from Views and click CSQ Waiting Contacts Info . |
| Step 3 | From the Application Reporting menu bar, choose Tools > Clear
                                                            				  Contact . A Clear Call dialog box is displayed to warn
                                                      			 you. If you want to continue with the clear action, click No . To cancel the action, click Yes . |
| Step 4 | Click No to proceed with the clear action. A Clear
                                                      			 Contact dialog box is displayed for you to confirm the action. You can click Yes to proceed or No to cancel. |
| Step 5 | Click Yes . The Unified CCX system removes the
                                                      				contact from all its queues. |

| Note | For some
                                                   			 reports, detailed information is also available by right-clicking a record in
                                                   			 that report. |
|---|---|

| Field | Description |
|---|---|
| Polling
                                                      						Interval | Time
                                                      						between two requests to the server for new statistics by the client. |
| Server
                                                      						Connect Retry Count | The
                                                      						number of times that the Unified CCXAdministration web interface should
                                                      						attempt to reconnect to the Unified CCX server. Note If an
                                                                  						  error occurs, an Error dialog box opens to alert you that the server is not
                                                                  						  communicating with the web interface. | Note | If an
                                                                  						  error occurs, an Error dialog box opens to alert you that the server is not
                                                                  						  communicating with the web interface. |
| Note | If an
                                                                  						  error occurs, an Error dialog box opens to alert you that the server is not
                                                                  						  communicating with the web interface. |
| Show
                                                      						Logged Off Resources | Specifies whether logged off agents appear in reports. |

| Note | If an
                                                                  						  error occurs, an Error dialog box opens to alert you that the server is not
                                                                  						  communicating with the web interface. |
|---|---|

| Note | Do not access Unified Intelligence Center until you complete the post installation
                                    			tasks for Unified CCX. |
|---|---|

| Note | The maximum number of users who can
                                    			concurrently run Live Data reports is 42 . |
|---|---|

| Note | Historical Reporting Client (HRC) is not available from 10.0(1). |
|---|---|

| Step 1 | Open a web browser. |
|---|---|
| Step 2 | Access http://<host address> and click Cisco Unified Contact Center Express
                                          				Reporting . Note Host address is the DNS name or IP address of the Unified CCX
                                                         					 node. | Note | Host address is the DNS name or IP address of the Unified CCX
                                                         					 node. |
| Note | Host address is the DNS name or IP address of the Unified CCX
                                                         					 node. |
| Step 3 | Enter your username and password. |
| Step 4 | Click Log In . |

| Note | Host address is the DNS name or IP address of the Unified CCX
                                                         					 node. |
|---|---|

| Field | Explanation |
|---|---|
| Only show currently active users | Check the check box to display users who are currently active. |
| Name Contains | Use this filter field to narrow the list of names or to move
                                       					 to a specific name. |
| User Name | The domain and user name (domain\name). |
| First Name | The user's first name. |
| Last Name | The user's last name. |

| Step 1 | Navigate to Security > User List . |
|---|---|
| Step 2 | Under the General Information tab, perform the following: In the User Name field, enter the domain and user name (domain\name). In the Alias field, enter the alias name for this user. Check the User is active check box to enable the user to log in and remain active. Note If the check box is unchecked, the user cannot log in. In the First Name field, enter the first name of the user. In the Last Name field, enter the last name. In the Organization field, enter the company name or other descriptive text to be associated with the user, such as region or Line of Business. In the Email field, enter the email address  of the user. In the Phone field, enter a phone number for the user. This can be the user's personal phone number or an emergency contact. In the Description field, enter the description of the user. In the Time Zone field, choose the time zone that you want to use in the report from the drop-down list. This time zone is also used for the user's scheduled reports and takes precedence over the time zone used by the report server. Note If this field is left blank, the system uses the time zone of the report server. For Start Day of the Week , perform the following: Select Locale Based to select starting day of the week based on locale. Select Custom Settings to choose one of the seven days of the week from the drop-down list. Note Start Day Of The Week is used in Scheduled Report, Report Views, and Permalink. In the Roles field, select and assign one or more roles for this user. If the Security Administrator adds or changes User Roles, the change does not take effect until the user logs out and then
                                                logs in again. In the Permissions field, choose the user's permission setting preference for My Group when creating new objects. My Group is the object owner's
                                             default group. Note Settings for My Group configures whether other users who belong to this user's default group can write, or run the objects.
                                                            Higher level permissions persist and override other permissions. | Note | If the check box is unchecked, the user cannot log in. | Note | If this field is left blank, the system uses the time zone of the report server. | Note | Start Day Of The Week is used in Scheduled Report, Report Views, and Permalink. | Note | Settings for My Group configures whether other users who belong to this user's default group can write, or run the objects.
                                                            Higher level permissions persist and override other permissions. |
| Note | If the check box is unchecked, the user cannot log in. |
| Note | If this field is left blank, the system uses the time zone of the report server. |
| Note | Start Day Of The Week is used in Scheduled Report, Report Views, and Permalink. |
| Note | Settings for My Group configures whether other users who belong to this user's default group can write, or run the objects.
                                                            Higher level permissions persist and override other permissions. |
| Step 3 | Under the Groups tab, you can determine which groups this user is a member of and how to add group membership(s) for a user.
                                       You can view the following: My Group : This field shows the user's default group. The Security Administrator can change it. The group is represented as “My Group”
                                                for the user. Available Groups : This list shows all the groups that have been created and that the user is not yet a member of. You can use arrows to move
                                                groups between columns. Selected Groups : This column shows all the groups that the user is a member of. You can use arrows to move groups between columns. Note By default, every user has AllUsers in their Selected Groups column. You cannot remove the AllUsers group from the Selected
                                                            Groups column. | Note | By default, every user has AllUsers in their Selected Groups column. You cannot remove the AllUsers group from the Selected
                                                            Groups column. |
| Note | By default, every user has AllUsers in their Selected Groups column. You cannot remove the AllUsers group from the Selected
                                                            Groups column. |

| Note | If the check box is unchecked, the user cannot log in. |
|---|---|

| Note | If this field is left blank, the system uses the time zone of the report server. |
|---|---|

| Note | Start Day Of The Week is used in Scheduled Report, Report Views, and Permalink. |
|---|---|

| Note | Settings for My Group configures whether other users who belong to this user's default group can write, or run the objects.
                                                            Higher level permissions persist and override other permissions. |
|---|---|

| Note | By default, every user has AllUsers in their Selected Groups column. You cannot remove the AllUsers group from the Selected
                                                            Groups column. |
|---|---|

| Field | Explanation |
|---|---|
| Name Contains | Use this filter field to narrow down the list of group names or to
                                       					 move to a specific name. |
| Name | Name of the group. |
| Full Name | The full name shows the child relationship of a group, as indicated by a dot separator. For example, if the default group for Group3 is Group1, and
                                       					 Group1 is a top level group (does not have a parent), then the Full Name of
                                       					 Group1 is Group1 . The Full Name of Group 3 is Group1.Group3 . |
| Description | Description text of the group. |

| Step 1 | Navigate to Security > User Groups . |
|---|---|
| Step 2 | Under the General Information tab, perform the following: In the Group Name field, enter the name of the group. This field is available only when you create a new group. In the Description field, enter or modify text to describe this group |
| Step 3 | Under the Groups tab, perform the following: Default Group —From the drop-down list, enter the default group. Available Groups —Lists the groups that were created and that are available for this group to become a child of. Click > or < to move just that group or groups. Selected Groups —Lists the groups that this group is a child of. Click > or < to move just that group or groups. |
| Step 4 | Under the Groups Members tab, perform the following: Under Users tab: Available Users —Lists all the users that were created and that are available to be children of this group. Click > or < to move just that group or groups. Selected User Members —Lists the users that are currently children of this group. Click > or < to move just that group or groups. Under Groups tab: Available Groups —Lists all the groups that were created and that are available to be children of this group. Click > or < to move just that group or groups. Selected Groups Members —Lists the groups that are currently children of this group.
                                                         Click > or < to move just that group or groups. |
| Step 5 | Click Save to update new entry or changes to the fields. |
| Step 6 | Click Cancel to cancel or close the page. |

| Note | Permissions
                                                				set on categories are not recursive. For all entities under Dashboard, Report,
                                                				or Report Definition types, you need separate EXECUTE/WRITE permissions. |
|---|---|

| Note | If no check
                                                				boxes are selected when setting permission for an object, the user has no
                                                				access privileges to the object. |
|---|---|

| Step 1 | Select the
                                          			 object type in the Permissions For panel. For Dashboard, Report or Report
                                          			 Definition type, you can select a category or an object within a category. For
                                          			 other object types, select an object from the list. All the groups that have
                                          			 already been assigned permissions for the object are displayed in the Group
                                          			 permissions for the selected item panel. |
|---|---|
| Step 2 | Select a group
                                          			 in the All Groups panel. All user members of this group are displayed in the
                                          			 All Users for the selected group panel. |
| Step 3 | Click Set
                                             				Permissions . Check the level you want for the group (Execute,
                                          			 Write), and click OK . |
| Step 4 | The Group
                                             				Permissions for the selected item panel updates to include the
                                          			 group and its assigned permission you defined in Step
                                             				3 . |

| Note | If the Security
                                          		  Administrator adds or changes User Permissions, the change may not occur
                                          		  immediately. |
|---|---|

| Field | Description |
|---|---|
| Permissions For panel (top left) | Click the
                                             					 drop-down list to select the objects for which you want to set permissions.
                                             					 Options are: Data Sources, Report Definitions, Reports, Dashboards, Value
                                             					 Lists, and Collections. Selecting
                                             					 an object type refreshes the panel to show the list of items or categories for
                                             					 that object. |
| All Groups
                                             					 panel (top right) | This panel
                                             					 shows the available User Groups. Highlighting a user group refreshes the page
                                             					 to display an All Users for Selected Group panel that lists the member of the
                                             					 group. |
| All Users
                                             					 for the Selected Group panel (bottom right) | This panel
                                             					 shows all members in the group that is highlighted in the All Groups panel
                                             					 above. |
| Set
                                             					 Permissions button | Click this
                                             					 option to open a dialog box where you select the permission level for the
                                             					 selected object in the Permissions For panel and the selected group in the All
                                             					 Groups panel. |
| Group
                                             					 Permissions for the selected item | This panel
                                             					 shows the groups that have already been assigned permission for the selected
                                             					 object, and their permission level. |

| Step 1 | Select the
                                          			 object type in the Permissions For panel. For Dashboard, Report, or Report
                                          			 Definition type, you can select a category or an object within a category. For
                                          			 other object types, select an object from the list. All the users that have
                                          			 already been assigned permission for the object are displayed in the User
                                          			 permissions for the selected item panel. |
|---|---|
| Step 2 | Select a user
                                          			 name in the User List panel. |
| Step 3 | Click Show
                                             				Groups to see the groups for which this user is a member. |
| Step 4 | Click Set
                                             				Permissions , check the level you want for this user (Execute,
                                          			 Write), and click OK . The All
                                                				  Permissions for the selected item panel refreshes to show the user
                                             				permissions you have added or changed for this user in steps 3 and 4. Field Description Permissions For panel (top left) Click the drop-down arrow to select the kinds of object for
                                                         							 which you want to set permissions. Options are Data Sources, Report
                                                         							 Definitions, Reports, Dashboards, Value Lists, Collections, and System
                                                         							 Collections. Selecting an object type refreshes the panel to show the list of
                                                         							 items or categories for that object. User
                                                         							 List panel (top right) This
                                                         							 panel shows current users. Filter the list and select one or many user names. Show
                                                         							 Groups button Click this option to show the All Groups for the selected user
                                                         							 panel. All
                                                         							 Groups for the selected User (bottom right) This
                                                         							 panel shows all groups to which the highlighted username in the User List panel
                                                         							 above is a member. Set
                                                         							 Permissions button Click this option to open a dialog box where you select the
                                                         							 permission level for the object (Execute, Write). All
                                                         							 Permissions for the selected item This
                                                         							 panel shows users who have permission for the object, and the level of
                                                         							 permissions they have. Note You cannot
                                                      				change the permission for the owner of an object. The owner always has Write
                                                      				permission for the object. For example, if a user is the owner of Report 1,
                                                      				then that user has WRITE permission for Report 1, and no one else can change
                                                      				the permission to EXECUTE. | Field | Description | Permissions For panel (top left) | Click the drop-down arrow to select the kinds of object for
                                                         							 which you want to set permissions. Options are Data Sources, Report
                                                         							 Definitions, Reports, Dashboards, Value Lists, Collections, and System
                                                         							 Collections. Selecting an object type refreshes the panel to show the list of
                                                         							 items or categories for that object. | User
                                                         							 List panel (top right) | This
                                                         							 panel shows current users. Filter the list and select one or many user names. | Show
                                                         							 Groups button | Click this option to show the All Groups for the selected user
                                                         							 panel. | All
                                                         							 Groups for the selected User (bottom right) | This
                                                         							 panel shows all groups to which the highlighted username in the User List panel
                                                         							 above is a member. | Set
                                                         							 Permissions button | Click this option to open a dialog box where you select the
                                                         							 permission level for the object (Execute, Write). | All
                                                         							 Permissions for the selected item | This
                                                         							 panel shows users who have permission for the object, and the level of
                                                         							 permissions they have. | Note | You cannot
                                                      				change the permission for the owner of an object. The owner always has Write
                                                      				permission for the object. For example, if a user is the owner of Report 1,
                                                      				then that user has WRITE permission for Report 1, and no one else can change
                                                      				the permission to EXECUTE. |
| Field | Description |
| Permissions For panel (top left) | Click the drop-down arrow to select the kinds of object for
                                                         							 which you want to set permissions. Options are Data Sources, Report
                                                         							 Definitions, Reports, Dashboards, Value Lists, Collections, and System
                                                         							 Collections. Selecting an object type refreshes the panel to show the list of
                                                         							 items or categories for that object. |
| User
                                                         							 List panel (top right) | This
                                                         							 panel shows current users. Filter the list and select one or many user names. |
| Show
                                                         							 Groups button | Click this option to show the All Groups for the selected user
                                                         							 panel. |
| All
                                                         							 Groups for the selected User (bottom right) | This
                                                         							 panel shows all groups to which the highlighted username in the User List panel
                                                         							 above is a member. |
| Set
                                                         							 Permissions button | Click this option to open a dialog box where you select the
                                                         							 permission level for the object (Execute, Write). |
| All
                                                         							 Permissions for the selected item | This
                                                         							 panel shows users who have permission for the object, and the level of
                                                         							 permissions they have. |
| Note | You cannot
                                                      				change the permission for the owner of an object. The owner always has Write
                                                      				permission for the object. For example, if a user is the owner of Report 1,
                                                      				then that user has WRITE permission for Report 1, and no one else can change
                                                      				the permission to EXECUTE. |

| Field | Description |
|---|---|
| Permissions For panel (top left) | Click the drop-down arrow to select the kinds of object for
                                                         							 which you want to set permissions. Options are Data Sources, Report
                                                         							 Definitions, Reports, Dashboards, Value Lists, Collections, and System
                                                         							 Collections. Selecting an object type refreshes the panel to show the list of
                                                         							 items or categories for that object. |
| User
                                                         							 List panel (top right) | This
                                                         							 panel shows current users. Filter the list and select one or many user names. |
| Show
                                                         							 Groups button | Click this option to show the All Groups for the selected user
                                                         							 panel. |
| All
                                                         							 Groups for the selected User (bottom right) | This
                                                         							 panel shows all groups to which the highlighted username in the User List panel
                                                         							 above is a member. |
| Set
                                                         							 Permissions button | Click this option to open a dialog box where you select the
                                                         							 permission level for the object (Execute, Write). |
| All
                                                         							 Permissions for the selected item | This
                                                         							 panel shows users who have permission for the object, and the level of
                                                         							 permissions they have. |

| Note | You cannot
                                                      				change the permission for the owner of an object. The owner always has Write
                                                      				permission for the object. For example, if a user is the owner of Report 1,
                                                      				then that user has WRITE permission for Report 1, and no one else can change
                                                      				the permission to EXECUTE. |
|---|---|

| Note | When you Run As another user, the top of the page shows both
                                                				  your Logged In identity and your Run As identity. You cannot Run As yourself. You can Run As one level of user. A Security Admin cannot Run As User A and, as User A, then Run As User B. |
|---|---|

| Note | Localization of
                                             				Audit Trail report is not supported. |
|---|---|

| Step 1 | Log in to the
                                          			 Unified Intelligence Center Reporting Interface. |
|---|---|
| Step 2 | Navigate to Reports > Stock > Intelligence Center
                                                				  Admin and click Audit
                                             				Trail . The system opens the Audit
                                             				Trail Report Filter window. |
| Step 3 | Specify the
                                          			 required filter criteria and click Run . The system displays the Audit Trail report
                                          			 based on the filter criteria that you specified. |