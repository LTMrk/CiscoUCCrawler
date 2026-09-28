---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-aea019f269
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_features-guide-1261/ucce_m_agent_greeting-1261.html
retrieved_at: 2026-08-16T20:12:08.045106+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Agent Greeting

## Chapter: Agent Greeting

# Agent Greeting

## Capabilities

The Agent
                           		Greeting feature lets an agent record a message that plays automatically to
                           		callers when they connect to the agent. The greeting message can welcome the
                           		caller, identify the agent, and include other useful contextual information.
                           		With Agent Greeting, each caller can receive a clear, well-paced,
                           		language-appropriate, and enthusiastic introduction. Another benefit is that it
                           		saves the agent from having to repeat the same introductory phrase for each
                           		call. It also gives the agent a moment to review the desktop software screen
                           		popups while the greeting plays.

The process of
                           		recording a greeting is much the same as recording a message for voicemail.
                           		Depending on how the call center is set up, agents may be able to record
                           		different greetings that play for different types of callers. For example, agents can record an
                           		English greeting for English speakers or an Italian greeting for Italian
                           		speakers.

### Agent Greeting
                           	 Phone Requirements (for Local Agents Only)

Agent
                              		Greeting is available to agents and supervisors who use IP Phones with Built-In
                              		Bridge (BIB). These agents are typically located within a contact center.
                              		Phones used with Agent Greeting must meet these requirements:

The phones must
                                    			 have the BIB feature.

If you
                                                				disable BIB, the system attempts to use a conference bridge for Agent Greeting
                                                				call flow and raises a warning event.

In an IPv6-enabled environment, Agent Greeting may require extra Media Termination Points (MTPs).

See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for the list of supported Cisco Unified Call Center phone models.

### Agent Greeting Functional Limitations

Agent Greeting is subject to these limitations.

Agent Greeting does not support outbound calls made by an agent. The announcement plays for inbound calls only.

Only one Agent Greeting file plays per call.

Supervisors cannot listen to agent recorded greetings.

Agent Greetings do not play when the router selects the agent through a label node.

Agent Greeting supports Unified CM based Silent Monitoring with this exception: Supervisors cannot hear the greetings themselves.
                                    If a supervisor tries to start a silent monitoring session while a greeting is playing, a message displays stating that a
                                    greeting is playing and to try again shortly.

### Whisper Announcement
                           	 with Agent Greeting

You can use
                              		Agent Greeting with the Whisper Announcement feature. Here are some things to
                              		consider when using them together:

On the call, the
                                    			 Whisper Announcement always plays first.

To shorten your
                                    			 call-handling time, use shorter Whisper Announcements and Agent Greetings than
                                    			 if you were using either feature by itself. A long Whisper Announcement
                                    			 followed by a long Agent Greeting equals a long wait before an agent actively
                                    			 handles a call.

If you use a
                                    			 Whisper Announcement, your agents probably handle different types of calls: for
                                    			 example, "English-Gold
                                       				Member-Activate Card," "English-Gold
                                       				Member-Report Lost Card," "English-Platinum
                                       				Member-Account Inquiry." Therefore, you may want to ensure that greetings
                                    			 your agents record are generic enough to cover the range of call types.

For more information about Whisper Announcement, see Whisper Announcement

## Initial
                        	 Setup

This section is intended for system administrators responsible for installing and configuring Unified CCE . It describes the one-time tasks required to set up Agent Greeting.

### Configuration
                           	 Requirements

The following
                              		configuration components must be in place to deploy Agent Greeting.

Where

What

Unified Communications Manager

For
                                          					 phones that use Agent Greeting, you must set the Built-in-Bridge option to On
                                          					 or Default (if the value of Default is On). To verify, in Unified CM
                                          					 Administration, select Device > Phone > Built in Bridge .

Unified CCE

Agent Greeting is supported with Type 10 Network VRUs only. (Type 10 is required to allow CVP to control the call). If your
                                          current Unified CCE deployment is not configured for a Type 10 VRU, you must modify it accordingly.

Agent Greeting requires at minimum three expanded call variables.

user.microapp.ToExtVXML: This is used twice in an Agent Greeting record script: the first time is to queue the Unified CVP
                                                RecordAgentGreeting application; the second time is to tell the recording application where to save greeting files. Configure
                                                it as an array with size 3.

Use the Unified CCE Administration tool to ensure this variable includes these settings: Maximum Length - 100 and Enabled.

user.microapp.app_media_lib:This is required in Agent Greeting record and play scripts to specify the dedicated directory
                                                on the media server where your greeting audio files are stored. Maximum Length - 100 and Enabled.

user.microapp.input_type: This is required in Agent Greeting record scripts to limit the allowable input type to DTMF. Maximum
                                                Length - 100 and Enabled.

Unified CCE (optional variables, used to override defaults)

To make these variables available to your script authors, confirm that they are defined in the Unified CCE Administration tool. For instructions about defining ECC variables for CVP, see the Administration Guide for
                                                   				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

user.microapp.media_server: Use to identify the Unified CVP
                                                						  media server if it is other than the default.

user.microapp.locale: Use to specify the name of the locale
                                                						  directory on the media server if it is other than the default ( "en-us" ).

user.microapp.UseVXMLParams: Required in your record script if
                                                						  you include the user.microapp.media_server variable. It tells the external VXML
                                                						  recording script to use the name/value pair of the application that you pass in
                                                						  the user.microapp.ToExtVXML variable.

Unified CVP

Unified CVP Server must be installed and configured, as described in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Deploy Agent Greeting

### Agent Greeting Deployment Tasks

Step 1

Ensure that your system meets the baseline requirements for software, hardware, and configuration described in the System
                                          Requirements and Limitations section.

Step 2

Configure one or more servers to act as media servers. Configuration requirements include IIS and FTP.

Step 3

In Unified CVP, add media servers, configure FTP connection information, and deploy the media servers.

Step 4

Configure a Unified CVP media server, if you have not already done so. See Configure Media Server for Agent Greeting . .

Step 5

In Unified CVP, republish the VXML Gateway.tcl scripts with updated Agent Greeting support. See Republish the tcl scripts to VXML Gateway for Agent Greeting support.

Step 6

Set the cache size on the VXML Gateway. See Set Cache Size on VXML Gateway .

Step 7

Record the voice prompts to play to agents when they record a greeting and to deploy the audio files to your media server.
                                          See Create Voice Prompts for Recording Greetings .

Step 8

Configure call types to record and play agent greetings. See Configure Call Types .

Step 9

Configure dialed numbers to record and play agent greetings. See Configure Dialed Numbers .

Step 10

Schedule the Script .

Step 11

Define Network VRU Scripts for Agent Greeting .

Step 12

In Script Editor:

- To use the installed scripts to record and play agent greetings, see Import Example Agent Greeting Scripts .

- To create your own scripts, see Agent Greeting Scripts .

Step 13

Modify the Unified CCE call routing scripts to use Play Agent Greeting script .

#### Configure Media
                              	 Server for Agent Greeting

Agent Greeting uses
                                 		the Unified CVP media server. If you previously configured and deployed one or
                                 		more Unified CVP media servers for other features, you do not have to configure
                                 		any additional servers for Agent Greeting. You can optionally add additional
                                 		media servers.

Agent Greeting uses
                                 		the Unified CVP media server to store and serve the following types of files:

Prompt files,
                                       			 prepared by Administrators. These files supply the prompts that agents hear
                                       			 when they record their greetings. The Administrator must manually add the
                                       			 prompt files to all the media servers that their Agent Greeting scripts will
                                       			 query to retrieve those files.

Greeting files,
                                       			 recorded by agents. These files are the actual greetings that play to callers.
                                       			 They are recorded by individual agents. The system handles the storage of these
                                       			 files as follows:

A greeting file is named using the convention PersonID_AgentGreetingType . For more about AgentGreetingType , see Specify AgentGreetingType Call Variable .

When a
                                             				  greeting is first recorded, it is stored temporarily on the Unified CVP Server, where an agent can listen to it before
                                             confirming its use.

When the agent
                                             				  confirms the greeting, the file is transferred, using FTP, to all media servers
                                             				  that are deployed and are configured with FTP enabled. Make sure that an FTP server is installed and configured for
                                             the correct version of IIS on the media server.
                                             				  For instructions, consult your Microsoft documentation ( http://microsoft.com ).

To satisfy a
                                             				  request for the greeting to play to a caller, the greeting file is copied from
                                             				  the media server to the VXML Gateway, where it is cached. The cached copy is
                                             				  used to satisfy subsequent requests for the greeting. Content expires in the
                                             				  cache based on the cache timeout period defined on the media server.

The routing scripts
                                 		look for the prompt and greeting files either on the configured default Unified
                                 		CVP media server or on a specific server identified in the script. Some typical
                                 		scripting scenarios for retrieving files for Agent Greeting include:

All files are
                                       			 retrieved from the default server.

All files are
                                       			 retrieved from the default server if available; otherwise, a redundant server
                                       			 is queried.

For security, the
                                       			 prompt files are retrieved from one server and the greetings files are
                                       			 retrieved from a different server.

For load
                                       			 balancing, the greetings files are dispersed among several servers and
                                       			 retrieved based on tests in the script.

##### Media Server Hardware and Network Requirements

Ensure the server is accessible to CVP, Unified CCE, and your agent desktops.

##### Prepare a Media Server

Ensure that IIS is properly configured and running on the server. It must be listening on port 80.

Ensure the server is accessible to CVP, Unified CCE, and your agent desktops.

Perform the following steps:

On the taskbar, click Start , point to Administrative Tools , and then click Server Manager .

In the Server Manager hierarchy pane, expand Roles , and then click Web Server (IIS) .

In the Web Server (IIS) pane, scroll to the Role Services section, and then click Add Role Services .

On the Select Role Services page of the Add Role Services wizard, expand FTP Server .

To support ASP.NET membership or IIS Manager authentication for the FTP service, you need to select FTP Extensibility .

Click Next.

On the Confirm Installation Selections page, click Install.

On the Results page, click Close.

In the sites section, click Add FTP Site .  Provide a site name and path to the same location as the http directory c:\inetpub\wwwroot.

Select your desired binding method, specify to start automatically, select No SSL and click Next.

On the Authentication and Authorization section select the type of authentication required.  If using basic, note the name and password of the account.

Select the authorization; for anonymous select Anonymous users .

Set the read and write permissions.

Make note of your FTP connection information -- connection type, user name, password, and port number.

Make sure that the FTP and the IIS share the same root directory, because the recording application writes the file to the
                                          media server directory structure, and the greeting playback call uses IIS to fetch the file. The en-us/app directory should be under the same root directory for FTP and IIS.

Create a dedicated directory on the server to store your greeting files. This lets you specify a lower cache timeout of 5
                                          minutes for your agent greeting files that does not affect other more static files you may be serving from other directories.
                                          By default, the Record Greeting application posts the .wav file to the en-us/app directory under your web/ftp root directory. You may create a dedicated directory such as ag_gr under the en-us/app directory, and then indicate this in the Unified CCE script that invokes the recording application. Use the array for the
                                          ECC variable call.user.microapp.ToExtVXML to send the ftpPath parameter to the recording application. Make sure the ECC variable length is long enough, or it may get
                                          truncated and fail.

In IIS Manager, set the cache expiration for the dedicated directory to a value that allows re-recorded greetings to replace
                                          their predecessor in a reasonable amount of time, while minimizing requests for data to the media server from the VXML Gateway.
                                          The ideal value varies depending on the number of agents you support and how often they re-record their greetings. Two minutes
                                          may be a reasonable starting point.

Also find the site you are using, go to the agent greeting folder you created (ag_gr), and then select HTTP Response Headers .

Select Add , then Set Common Headers .

Select Expire Web Content and set your desired value.

After specifying the cache timeout, it is a good idea to clear the cache on the VXML Gateway. This ensures the gateway requests
                                                the latest files from the media server. You need only clear the gateway cache once. Open a command prompt on the CVP VXML
                                                Gateway, log into IOS, and enter the following commands:

my_server# conf t

my_server(config)# clear http client cache

my_server(config)# exit

my_server(config)# wr

The HTTP client response timeout setting on the gateway must be greater than the time it takes to complete the largest anticipated
                                                FTP file transfer. If an FTP file transfer takes longer than the configured duration in seconds for HTTP client response timeout,
                                                the FTP transfer completes correctly, but the call drops as soon as the configured timeout duration is met. To change the
                                                HTTP client response timeout setting, open a command prompt on the CVP VXML Gateway, log into IOS, and enter the following
                                                commands:

my_server# conf t

my_server(config)# http client response timeout <new value in seconds>

my_server(config)# exit

my_server(config)# wr

By default, the HTTP client response timeout value for CVP is 30 seconds.

##### How Greeting Files
                                 	 Are Recorded and Served

Following is
                                    		an illustration of how Greeting files are recorded and served, followed by a
                                    		step by step description.

An agent initiates
                                          			 a greeting recording session and records a greeting.

The VXML Gateway
                                          			 passes the recorded (but unsaved) greeting file to the VXML Server.

- The agent asks to listen to
                                       		  the greeting before saving it. The file is played from the VXML Server.

The agent saves
                                          			 the greeting. The file is named (based on the Person ID +
                                          			 AgentGreetingType) and stored on the media server.

Requests for the
                                          			 greeting file come in through the VXML Gateway. The VXML Gateway examines its
                                          			 web server cache for the file. If the file is present and not expired, the
                                          			 cached version is served. If the file is not present, or if its timestamp
                                          			 exceeds the cache expiration, the file is retrieved from the media server and
                                          			 cached again.

#### Add and Configure Media Servers in CVP

CVP automatically propagates  files that are added to one media server out to all media servers in the list that have  FTP
                                          enabled. To enable FTP on a media server, use the following procedure.

You can designate one media server as the default.  If a default media server is defined, requests for files are automatically
                                          sent to that server without your having to specify that server in your routing scripts.

Access the CVP Operations Console by typing https://<OAMP_server_IP>:9443/oamp .

At the CVP Operations Console,  select Device Management > Media Server .

Add a   server to the list of CVP media servers.

Select FTP Enabled .

Configure the credentials and port settings that will permit CVP to write files to the server using FTP.

Optionally, you can designate one of your media servers as the Default Media Server.

Click the Deploy button  to deploy the list of  media servers to your CVP Servers.

Note: If you deploy  the list of media servers and then designate a default, you must redeploy the list.

#### Republish the tcl
                              	 scripts to VXML Gateway

The .tcl
                                    		  script files that ship with Unified CVP include updates to support Agent
                                    		  Greeting. You must republish these updated files to your VXML Gateway.

Republishing scripts to the VXML Gateways is a standard task in CVP upgrades. You must republish the scripts before you can
                                    use Agent Greeting.

Step 1

In the Unified
                                             			 CVP Operation Console, select Bulk
                                                   				  Administration > File Transfer > Scripts and
                                                   				  Media .

Step 2

Set Device to
                                             			 Gateway.

Step 3

Select the
                                             			 gateways you want to update. Typically you would select all of them unless you
                                             			 have a specific reason not to.

Step 4

Select Default
                                                				Gateway Files .

Step 5

Click Transfer .

#### Set Cache Size on
                              	 VXML Gateway

To ensure
                                 		adequate performance, set the size of the cache on the VXML Gateway to the
                                 		maximum allowed. The maximum size is 100 megabytes; the default is 15
                                 		kilobytes. Failure to set the VXML Gateway cache to its maximum can result in
                                 		slowed performance to increased traffic to the media server.

Use the following
                                 		Cisco IOS commands on the VXML Gateway to reset the cache size:

```
conf t
http client cache memory pool 100000
exit
wr
```

For more information about configuring the cache size, see the Configuration Guide for
                                          				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

#### Create Voice
                              	 Prompts for Recording Greetings

You must
                                    		  create audio files for each of the voice prompts that agents hear as they
                                    		  record a greeting. The number of prompts you require can vary, but a typical
                                    		  set can consist of:

A welcome
                                          				followed by a prompt to select which greeting to work with (this assumes you
                                          				support multiple greetings per agent)

A prompt to
                                          				select whether they want to hear the current version, record a new one, or
                                          				return to the main menu

A prompt to
                                          				play if a current greeting is not found.

To create voice
                                    		  prompts for recording greetings:

Step 1

Create the
                                             			 files using the recording tool of your choice. When you record your files:

The media
                                                         					 files must be in .wav format. Your .wav files must match Unified CVP encoding and format
                                                         					 requirements (G.711, CCITT A-Law 8 kHz, 8 bit, mono).

Test your
                                                         					 audio files. Ensure that they are not clipped and that they are consistent in
                                                         					 volume and tone.

Step 2

After
                                             			 recording, deploy the files to your Unified CVP media server. The default
                                             			 deployment location is to the <web_server_root> \en-us\app directory.

Step 3

Note the names
                                             			 of the files and the location where you deployed them on the media server. Your
                                             			 script authors need this information for the Agent Greeting scripts.

##### Built-In Recording
                                 	 Prompts

The Unified
                                    		CVP Get Speech micro-application used to record Agent Greetings includes the
                                    		following built-in prompts:

A prompt that
                                          			 agents can use to play back what they recorded

A prompt to save
                                          			 the greeting, record it again, or return to the main menu

A prompt that confirms the save, with an option to end the call or return to the main menu

You can replace these .wav files with files of your own. For more information, see the Unified Customer Voice Portal Call Studio documentation at https://www.cisco.com/c/en/us/support/unified-communications/unified-call-studio/tsd-products-support-series-home.html .

##### Example Record Greeting Prompts

Unified CCE includes three example record greeting audio prompts. These are installed on each ICM server at <icm_root>\wav.
                                    These example files are referenced in the example recording script that are included with ICM. If you plan to deploy the example
                                    script, copy the audio prompts to the <web_server_root>en-us\app directory on your media server.

#### Configure Call
                              	 Types

To record and play
                                    		  agent greetings, create the following call types: RecordAgentGreeting and
                                    		  PlayAgentGreeting.

Step 1

From the
                                             			 Configuration Manager, select Tools > List Tools .

Step 2

Select Call Type List .

Step 3

Click Retrieve .

Step 4

Click Add .

Step 5

Create a call
                                             			 type to record agent greetings and use the name RecordAgentGreeting. 
                                             		  Then click Save .

Step 6

Create a call
                                             			 type to play agent greetings and use the name PlayAgentGreeting. 
                                             		  Then click Save .

#### Configure Dialed
                              	 Numbers

To record and play
                                    		  agent greetings, create the following dialed numbers: RecordAgentGreeting and
                                    		  PlayAgentGreeting.

Step 1

From the
                                             			 Configuration Manager, select Tools > List Tools .

Step 2

Select Dialed
                                                				  Number/Script Selector List .

Step 3

Click Retrieve .

Step 4

Click Add .

Step 5

On the Attributes tab, do the following:

Create a
                                                   			 dialed number to record agent greetings; use the name RecordAgentGreeting.
                                                   			 (The name must match exactly and is case-sensitive.) Set the Media routing domain to Cisco_Voice , and then click Save .

Create a
                                                   			 dialed number to play agent greetings; use the name PlayAgentGreeting.
                                                   			 (The name must match exactly and is case-sensitive.) Set the Media routing domain to Cisco_Voice , and then click Save .

Step 6

On the Dialed Number Mapping tab,  
                                             		  do the following:

Click Add and map the RecordAgentGreeting dialed number to its call type; click OK .

Click Add and map the PlayAgentGreeting dialed number and its call type; click OK .

#### Schedule the
                              	 Script

Step 1

In the Script
                                                				Editor , select Script > Call Type Manager .

Step 2

From the Call
                                             			 Type Manager screen, select the Schedules tab.

Step 3

From the Call
                                             			 type drop-down list, select the call type to associate with the script; for
                                             			 example, PlayAgentGreeting.

Step 4

Click Add and select the script you want from the Scripts
                                             			 box.

Step 5

Click OK twice to exit.

#### Define Network VRU
                              	 Scripts for Agent Greeting

For Agent
                                 		Greeting record and play scripts to interact with Unified CVP, Network VRU
                                 		scripts are required. The number of VRU scripts that you require and how you
                                 		configure them depends on how you choose to script Agent Greeting.

To create these scripts, use the Network VRU Script List Tool found in Configuration Manager.

The following
                                 		table lists an example set of Agent Greeting Network VRU scripts based on the
                                 		example Agent Greeting scripts that are included with the software.

If you require the
                                             		  following example VRU scripts, you must manually create them.

The Network VRU must be a Type10

The default timeout 180 is acceptable

Leave Overridable unchecked

VRU Script Name

(Y/N)

AgentGreeting

PM,-a

null

N

Causes a saved greeting audio file to play. The -a parameter automatically generates the file name by concatenating the Person ID with the AgentGreetingType variable value
                                             set in your routing scripts that target an agent.

GreetingMenu_1_to_9

M,press_1_thru_9_greeting,A

1-9

Y

During
                                             				a recording session, play an audio file that presents a voice menu prompting
                                             				the agent to press the number corresponding to the greeting he or she wants to
                                             				record. The 1-9 configuration parameter defines the range of
                                             				allowable keys. So this value also determines the number of concurrent
                                             				greetings agents can have. The A parameter specifies that the file is in the (default)
                                             				Application directory on the Unified CVP Server.

GreetingSubMenu

M,press1-press2-press3,A

1-3

Y

During
                                             				a recording session, play an audio file that prompts the agent to press 1 to
                                             				listen to a greeting, 2 to record, or 3 to go to the main menu.

Greeting_Not_Found

PM,no_greeting_recorded,A

Y

Y

During
                                             				a recording session, if an agent tries to play back a greeting that does not
                                             				exist, play the no_greeting_recorded audio file. The Y configuration parameter in this instance allows
                                             				barge-in (digit entry to interrupt media playback).

T10_GS_AUDIUM

GS,Server,V, FTP

,,,,,,,,,,Y

Y

This
                                             				starts the external VXML application that records the greeting. The VRU script
                                             				name must be specified exactly as shown and is case-sensitive.

The Y parameter in the eleventh position of the
                                             				Configuration Parameter is required. It allows the script to pass FTP
                                             				connection information to the VXML server. The VXML server then uses this
                                             				information to make an FTP connection to the media server when saving greeting
                                             				files.

GreetingReview

PM,-a,A

Y

Y

This script allows the agent to review the recorded greeting audio file.

For descriptions of VRU Script Name parameters and detailed instructions on creating Network VRU scripts for CVP micro-applications,
                                             see the Configuration and Administration Guide for Cisco Unified Customer Voice Portal.

#### Import Example
                              	 Agent Greeting Scripts

To view or use the
                                    		  example Agent Greeting scripts, you must first import them into Script Editor.
                                    		  To import the scripts:

Step 1

Launch Script
                                             			 Editor.

Step 2

Select File >
                                                				Import Script and select a script to import.

The scripts are located in the icm\bin directory on the Unified CCE AW-HDS-DDS.

When you
                                                            				  import the example scripts, Script Editor maps objects that are referenced in
                                                            				  the scripts. Some of the objects, such as the external Network VRU scripts,
                                                            				  skill groups, route to skill group, or precision queue, do not map
                                                            				  successfully. You must create these manually or change these references to
                                                            				  point to existing scripts, skill groups, and precision queues in your system.

##### What to do next

In addition to
                                    		  importing the scripts, you may need to modify the following items. For more
                                    		  information, see Agent Greeting Scripts .

If you do not
                                          				use a default media server, you must modify the media server specification.

If you do not
                                          				use the default values for application and locale ( en-us/app ), you
                                          				must modify the path name of greeting files.

Using the
                                          				Unified CCE Administration tool, enable all expanded call variables referenced
                                          				by the following sample scripts.

##### Agent Greeting
                                 	 Example Routing Scripts

The example
                                    		routing script files in the icm\bin directory include:

AG.ICMS— This script sets
                                          			 up an Agent Greeting by setting the greeting type to be used on the call and
                                          			 then queueing the call to a skill group or precision queue. Once an agent is
                                          			 selected from the skill group or precision queue and the call routed to the
                                          			 agent, the PAG.ICMS script is invoked. It requires that you define an
                                          			 AgentGreeting VRU script (described in Define Network VRU Scripts for Agent Greeting )
                                          			 and a skill group.

PAG.ICMS— This script causes an Agent Greeting to play. It is invoked by the PlayAgentGreeting dialed number that you configured earlier
                                          in the configuration process. This number must be associated with a call type that then runs the script. It requires that
                                          you define an AgentGreeting VRU script, described in Define Network VRU Scripts for Agent Greeting .

RECORD_AG.ICMS— This
                                          			 script lets agents record a greeting. It is called from the agent desktop when
                                          			 an agent clicks the Record Agent Greeting button. It prompts the agent to
                                          			 select which greeting to play or record. This script is invoked by the
                                          			 RecordAgentGreeting dialed number that you configured earlier in this
                                          			 configuration process. It requires that you define all five VRU scripts
                                          			 described in Define Network VRU Scripts for Agent Greeting .

WA_AG.ICMS— This script
                                          			 plays a Whisper Announcement and an Agent Greeting together on the same call
                                          			 flow. It requires that you define an AgentGreeting VRU script (described in Define Network VRU Scripts for Agent Greeting )
                                          			 and a skill group.

The PAG.ICMS and
                                                		  RECORD_AG.ICMS example scripts assume that a default media server is configured
                                                		  in Unified CVP, and the greeting files are stored in a dedicated directory
                                                		  named ag_gr directory. The WA_AG.ICMS script does not include a dedicated
                                                		  directory.

For greeting, the
                                                		  initial script sets up the call between caller and agent, and a different
                                                		  script plays the greeting to the agent after the caller is connected. If the
                                                		  initial Unified CCE script overrides the default media server with a SET node,
                                                		  the call context of expanded call variables is preserved on the greeting
                                                		  playback call as well, and the Default Media Server may be overridden. In this
                                                		  case, modify the greeting playback script to use a SET node with the correct
                                                		  media server.

#### Test Agent Greeting
                              	 File Path

When an agent records a greeting, the greeting file is saved with a system-generated name as follows:

The Person ID number is prepended to the starting string. For example, an agent with a Person ID of 5050 would have greeting
                                       files named 5050_1 or 5050_French.

The filename ends with the value of the Call.AgentGreetingType variable associated with the choice the agent made when recording
                                       the greeting. For example, if the agent selected the first option, and the Agent Greeting record script sets the first option
                                       to "1," then the greeting filename is appended with _1. As another example, if descriptive strings were implemented, and the
                                       first option is associated with the string "French," then the greeting filename is appended with _French.

The greeting file is saved in a directory whose path is determined by the following variables in the Agent Greeting record
                                 script:

A specific media server, or the default media server. (The file is later pushed to all FTP-enabled media servers.)

A specific application directory, or the default application directory.

A specific locale directory, or the default locale directory.

To test the
                                 		path you defined to the greeting file in your script variables, plug the
                                 		complete URL into a browser. The .wav file should play. For example:

If your script uses a default media server whose IP is 192.1.1.28 + the default locale + an application directory named greet + 5050_im1.wav , then the generated URL should be http://192.1.1.28/en-us/app/greet/5050_1.wav . Entering this URL into a browser should cause this agent’s greeting to play.

If your script includes: http://my_server.my_domain.com + the default locale + an application directory app/greet + 5050_1.wav , then the path should be http://my_server.my_domain.com/en-us/app/greet/5050_1.wav .

#### Modify the Unified CCE call routing scripts to use Play Agent Greeting script

For an Agent Greeting play script to run, you must add an AgentGreetingType Set Variable node to your existing Unified CCE call routing scripts: This variable's value is used to select the audio file to play for the greeting. Set the variable before
                                 the script node that queues the call to an agent (that is, the Queue [to Skill Group or Precision Queue], Queue Agent, Route
                                 Select, or Select node).

##### Specify
                                 	 AgentGreetingType Call Variable

To include
                                    		Agent Greeting in a script, insert a Set Variable node that references the
                                    		AgentGreetingType call variable. The AgentGreetingType variable causes a
                                    		greeting to play and specifies the audio file it should use. The variable value
                                    		corresponds to the name of the greeting type for the skill group or Precision
                                    		Queue. For example, if there is a skill group or Precision Queue for Sales
                                    		agents and if the greeting type for Sales is '5', then the variable value
                                    		should be 5.

You can use
                                    		a single greeting prompt throughout a single call type. As a result, use one
                                    		AgentGreetingType set node per script. However, as needed, you can set the
                                    		variable at multiple places in your scripts to allow different greetings to
                                    		play for different endpoints. For example, if you do skills-based routing, you
                                    		can specify the variable at each decision point used to select a particular
                                    		skill group or Precision Queue.

Only one greeting
                                                		  can play per call. If a script references and sets the AgentGreetingType
                                                		  variable more than once in any single path through a script, the last value to
                                                		  be set is the one that plays.

Use these
                                    		settings in the Set Variable node for Agent Greeting:

Object Type: Call.

Variable: Must use
                                          			 the AgentGreetingType variable.

Type: Must use the PersonID_AgentGreetingType type.

Value: Specify the
                                          			 value that corresponds to the greeting type you want to play. For example: "2" or "French"

You must
                                                				  enclose the value in quotes.

The value is
                                                				  not case-sensitive.

The value
                                                				  cannot include spaces or characters that require URL encoding.

##### Scripting Agent Greeting for Multiple Customers

In the out-of-box method for deploying Agent Greeting, Unified CCE uses the customer information from the built-in "PlayAgentGreeting" dialed number to choose the correct network VRU to play the greeting. If your deployment has multiple customers configured
                                    within your Unified CCE instance and you want to use Agent Greeting with all of them, you must configure things differently to work around customer
                                    associations.

###### Configure Custom Dialed Number for Agent Greeting Play

To play Agent Greetings for multiple customer instances, configure the built-in PlayAgentGreeting dialed number for each Unified
                                       CM routing client, but do not associate it with a specific customer. The Unified CM peripheral uses this number to initiate
                                       Agent Greeting play. If you want your greetings to be played from a different network VRU, use the TranslationRouteToVRU node
                                       in your routing scripts to explicitly choose the network VRU.

###### Configure Custom Dialed Number for Agent Greeting Record

To record Agent Greetings when you have multiple customers, you must create your own custom dialed number for recording. You
                                       may want to create different dialed numbers for different customers. As with Agent Greeting play, if you want to use different
                                       network VRUs to record Agent Greetings for different customers, use the TranslationRouteToVRU node in your routing script
                                       to explicitly select the network VRU.

Create your own custom button or have your agents enter the record dialed number using the dial pad on their desktops.

### Agent Greeting
                           	 Scripts

Agent
                              		Greeting requires two call routing scripts: one that agents can use to record
                              		greetings and one to play a greeting to callers. Examples of these scripts are
                              		included in your installation. This section describes the elements in the
                              		installed example scripts, including optional features and other modifications
                              		that you can make. To create scripts from scratch, use this section to
                              		understand the required elements in Agent Greeting scripts.

If you plan to use
                                          		  the installed example scripts out of the box, you can ignore this section.

#### Agent Greeting
                              	 Recording Script

The Agent
                                 		Greeting recording script is a dedicated routing script that allows agents to
                                 		record greetings. You can use the installed example scripts or create your own.

In the
                                 		example script shown here, the agent is first prompted to select one of nine
                                 		possible greeting types. After selecting a greeting type, the agent chooses
                                 		whether to 1) listen to the existing greeting for that type; 2) record a new
                                 		greeting for that type, or 3) return to the main menu. If the agent selects the
                                 		option to listen, the name of the application directory on the media server is
                                 		set and the external VRU script that plays the greeting is triggered. Then the
                                 		agent is returned to the main menu. If the agent selects the option to record,
                                 		the Unified CVP recording application is called. The recording application
                                 		contains its own built-in audio prompts that step the agent through the process
                                 		of recording and saving a greeting. At the end, the agent is returned to the
                                 		main menu.

There are
                                 		several other behaviors in the script to note. An agent may select to listen to
                                 		a greeting type for which no greeting exists. In that event, a VRU script that
                                 		plays an error message is called. Also, in two places in the script, the path
                                 		to the application directory is reset to the default. This is because (in this
                                 		example) that is where the files for the audio files reside. The only files
                                 		that reside outside of the default directory are the greetings themselves.

##### RecordAgentGreeting
                                 	 Micro-application

Unified CVP
                                    		includes a dedicated micro-application -- RecordAgentGreeting -- for recording
                                    		agent greetings. The application lets agents record, review, re-record, and
                                    		confirm the save of a greeting. It includes audio files to support each of
                                    		these functions. If an agent is not satisfied with a greeting, it can be
                                    		re-recorded up to three times. Upon confirmation of a save, the application
                                    		FTPs the saved file to the media server.

Built-in error checking includes checks for the data required to name the file ( Person ID + AgentGreetingType variable value), media server specification, valid menu selections made by the agent, and successful FTP of the greeting
                                    file.

##### Agent Greeting
                                 	 Record Script Nodes

Using the
                                    		example script as a reference, here are descriptions of the functions its nodes
                                    		perform.

Variable:Call:user.

microapp.input_type

Sets
                                                				the allowable input type to DTMF (touch tone).

RunExtScript:Press 1-9 to Select Greeting X

Runs
                                                				the VRU script that defines which digits are valid to select an
                                                				AgentGreetingType and plays a voice prompt describing the options.

Variable:Call:AgentGreetingType

Sets
                                                				the AgentGreetingType to the digit the agent pressed. This text is used in the
                                                				greeting wave file. It can be a simple numbering system or more descriptive
                                                				titles such as "English."

RunExtScript:

1 -
                                                				hear greeting X,

2 -
                                                				record greeting X,

3 -
                                                				return to menu

Runs
                                                				the VRU script that defines which digits are valid to select a desired action
                                                				and plays a voice prompt describing the options.

CED

Tells
                                                				the script how to handle the caller entered digits in response to the 1,2,3
                                                				external script.

Variable:Call: user.microapp.app_media_lib

Set three times:

Once to "app/ag_gr"

Twice to "" (an empty string; that is, the default)

Defines the path to the application directory on the Unified CVP
                                                				media server. Prior to playing the greeting file, it is set to the dedicated
                                                				greeting file directory (in this example, app/ag_gr ). After the greeting file plays, it is
                                                				reset to the default application directory where (in this example) the files
                                                				for voice prompts are stored. If the voice prompts were stored in the same
                                                				directory as the greeting files, there would be no need to reset the path.

RunExtScript: Play Recording

Runs
                                                				the VRU script that plays the selected Agent Greeting.

RunExtScript:Greeting Not Found

Runs
                                                				the VRU script that plays an error message if the Agent Greeting selected to
                                                				play does not exist.

Variable:

Call:user.microapp.

ToExtVXML[]

Array
                                                				Index: 2

Value: "ftpPath=< path_to_dedicated/ directory >"

For
                                                				example: "ftpPath=en-us/app/ag_gr"

Specifies the FTP information that the VXML server uses to write greeting files to the media server. The information must
                                                match the FTP information configured for the media server in the Unified CVP Operations Console.

The
                                                				value for array index must be 2.

The value consists of:

ftpPath= to set the path to the dedicated directory for agent greeting files.

The path must begin with the locale directory.

To view additional setting options, see CVP documentation .

Variable:

Call:user.microapp.

ToExtVXML[]

Array
                                                				Index: 0

Value: "application=RecordAgentGreeting"

Identifies the external Unified CVP micro-application
                                                				(RecordAgentGreeting) that is used to record the greeting.

The value for
                                                				array index must be 0.

RunExtScript: Run Default Recording Application

Runs the VRU script that launches the Get Speech micro-application on the VXML server.

##### Specify Media Server
                                 	 in Routing Scripts

When you configure
                                    		media servers in CVP, you can specify a default media server. The benefit to
                                    		specifying a default media server is that your scripts do not need a Set
                                    		Variable node to access the default media server. For this to work, you must
                                    		make sure that the files a script requests are stored on the default server.

If you do
                                    		not define a default media server, or if you define a default but the files
                                    		that your script requires are not stored on the default, then the script must
                                    		include a Set Variable node to identify a media server.

To specify a
                                    		media server that stores the files required by your script, use the following
                                    		settings in the Set Variable node:

Object Type: Call.

Variable: Must use
                                          			 the user.microapp.media_server expanded call variable.

Value: Specify the
                                          			 HTTP path to the server. For example: "http://myserver.mydomain.net." You must enclose the path in
                                          			 quotes.

Alternately you
                                          			 can specify an IP address in place of a hostname.

In scripts that invoke an external VXML application (as the Agent Greeting record script does), if you explicitly set a variable
                                       for the media server (user.microapp.media_server), then you must also set the following variables:

The path to the media server application directory (user.microapp.app_media_lib)

The CVP UseVXMLParams value to N.(user.microapp.UseVXMLParams)

See the
                                       		  following example.

##### Specify Greeting
                                 	 File Locale and Application Directories in Routing Scripts

CVP uses a default storage directory for media
                                       		  files: <web_server_root> /en-us/app . To take
                                       		  advantage of this, Unified CCE call routing scripts automatically add en-us/app to the server name when constructing HTTP
                                       		  requests for media files. For example:

If the script node that defines the media server has a value of "http://myserver.mydomain.com," and

The script node that defines which audio file to play has a value of "5050_1.wav" (for an agent with a Person ID of 5050), then

The HTTP request for the file is automatically constructed as http://myserver.mydomain.com/en-us/app/5050_1.wav

If your
                                       		  greeting audio files are stored in a different locale directory, you must add a
                                       		  Set Variable node to your script that identifies the locale directory. As you
                                       		  must store your greeting files in a dedicated subdirectory under the locale,
                                       		  you must always add a Set Variable node that identifies that directory.

Use these
                                       		  settings in the Set Variable node to specify your locale directory:

Object Type:
                                             				Call.

Variable: Must
                                             				use the user.microapp.locale expanded call variable.

Value: Specify
                                             				the directory name. For example: "pt-br" (Portuguese-Brazil). You must enclose the path in quotes.

Use these
                                       		  settings in the Set Variable node to specify your application directory:

Object Type:
                                             				Call.

Variable: Must
                                             				use the user.microapp.app_media_lib expanded call variable.

Value: Specify
                                             				the directory name. For example: to use a directory "greet" in
                                             				place of the default directory "app" , enter "greet" . To
                                             				use a sub-directory "greet" under "app" enter "app/greet" .
                                             				You must enclose the path in quotes.

##### Verify Length for Media Server Locale and Application Directory Variables

If you  include Set Variable nodes for the media server, locale, and/or application directories, make sure that the values
                                    you set for them do not exceed the Maximum Length settings for their corresponding expanded call variables.

For example, if you include a Set Variable node for the media server with a value of "http://mysubdomain.mydomain.co.uk" , the string is 33 characters long. Therefore, the Maximum Length setting for the user.microapp.media_server expanded call
                                    variable must be 33 or greater. Otherwise,  the server name is truncated in the HTTP request for the file and the file is
                                    not found.

To configure ECC variables, use the Unified CCE Configuration Manager. Select List Tools > Expanded Call Variables List .

#### Descriptive Agent
                              	 Greeting Type Strings

The previous Agent
                                 		Greeting record script example stores Agent Greeting Type values as numbers
                                 		(although in string format). But suppose you prefer more descriptive string
                                 		names. For example, "English," "French," and "Spanish." Or "Sales," "Billing," and "Tech Support."

Descriptive names can make it easier to understand at a glance what different numeric key selections in your scripts correspond
                                 to. Note that they also affect how greeting files are named (for example, for an agent whose Person ID is 5050, 5050_English.wav as opposed to 5050_1.wav ).

The following script
                                 		example is almost identical to the previous record script, except that it
                                 		includes four additional nodes (highlighted in green). They consist of an
                                 		additional CED node that maps the keys 1, 2, and 3 to language names. The Run
                                 		Ext Script node (in gray) was modified for the new options. The rest of the
                                 		script is the same with no other changes required. Note that your routing
                                 		scripts require a corresponding mapping of numeric keys to language names.

#### Agent Greeting Play
                              	 Script

The Agent
                                 		Greeting feature requires a dedicated routing script that causes the agent
                                 		greeting to play. This script is invoked by the PlayAgentGreeting dialed
                                 		number.

The Play
                                 		script must contain at least two and possibly four specific nodes, depending on
                                 		other factors.

You always
                                 		need the following nodes:

A Run External
                                       			 Script node that calls the VRU script that plays the greeting.

A Set Variable
                                       			 node that sets the directory path to your greeting files.

You may also
                                 		need to include in your scripts Set Variable nodes that:

Specify the Media
                                       			 Server: Unified CVP lets you specify a default media server. If you are not
                                       			 serving your audio files from the default media server, your scripts must
                                       			 include a variable that identifies the server where your audio files are
                                       			 stored.

The Locale
                                                      				  Directory set variable node is optional. It is needed only if you decide to use
                                                      				  a directory other than the default one.

Add a new Run External Script node with its backup media mapped to the agent greeting.

Add the Run External Script node between the failure path of the AgentGreeting Run External Script node and the End node.

Connect the Run External Script node's success path to the existing Release call node and failure path to the existing end
                                          node.

Adding the Run External Script node may add a short delay of one to two seconds to the call flow.

## Reporting

In agent,
                           		skill group, and precision queue reports, greeting time is not specifically
                           		broken out. The period during which the greeting plays is reported as talk
                           		time. Record time is counted as an internal call by the default skill group.

Calls that
                           		involve Agent Greeting consist of two call legs: the inbound call from the
                           		customer and the call to Unified CVP for the greeting. Both of these legs have
                           		the same RouterCallKeyDay and RouterCallKey values in the TCD and RCD tables in
                           		the database. You can use these values to link the two legs together for
                           		reporting purposes.

### Greeting Call
                           	 Statistics

To view
                              		greeting call statistics, create a separate call type and associate it with the
                              		routing script that plays agent greeting. New Cisco Unified Intelligence Center
                              		templates for the agent greeting call type are created based on the data in the
                              		existing Call_Type_Real_Time and Call_Type_Interval table in the database.

### Peripheral Call
                           	 Types for Agent Greeting

There are two
                              		peripheral call types specific to Agent Greeting that you can use to track and
                              		report on the feature.

Call Type 39: Play
                                    			 Agent Greeting. Route request to play an Agent Greeting.

Call Type 40:
                                    			 Record Agent Greeting. Agent call for recording an Agent Greeting.

Extra TCDs and RCDs are generated for the agent greeting call leg, and they can be linked to the first call leg by the same
                              RouterCallKeyDay and RouterCallKey.

## Serviceability

Serviceability for Agent Greeting includes SNMP events captured by your Network
                           		management software that indicate reasons for greeting failures and counters to
                           		track the number of failed greeting events.

When system components fail, Agent Greeting may be impacted. For example, if a requested greeting audio file cannot be found
                           for any reason, the call proceeds without the Agent Greeting.

| Note | If you
                                                				disable BIB, the system attempts to use a conference bridge for Agent Greeting
                                                				call flow and raises a warning event. |
|---|---|

| Where | What |
|---|---|
| Unified Communications Manager | For
                                          					 phones that use Agent Greeting, you must set the Built-in-Bridge option to On
                                          					 or Default (if the value of Default is On). To verify, in Unified CM
                                          					 Administration, select Device > Phone > Built in Bridge . |
| Unified CCE | Agent Greeting is supported with Type 10 Network VRUs only. (Type 10 is required to allow CVP to control the call). If your
                                          current Unified CCE deployment is not configured for a Type 10 VRU, you must modify it accordingly. Agent Greeting requires at minimum three expanded call variables. user.microapp.ToExtVXML: This is used twice in an Agent Greeting record script: the first time is to queue the Unified CVP
                                                RecordAgentGreeting application; the second time is to tell the recording application where to save greeting files. Configure
                                                it as an array with size 3. Use the Unified CCE Administration tool to ensure this variable includes these settings: Maximum Length - 100 and Enabled. user.microapp.app_media_lib:This is required in Agent Greeting record and play scripts to specify the dedicated directory
                                                on the media server where your greeting audio files are stored. Maximum Length - 100 and Enabled. user.microapp.input_type: This is required in Agent Greeting record scripts to limit the allowable input type to DTMF. Maximum
                                                Length - 100 and Enabled. No other ECC (Expanded Call Variable) are needed if you serve your files from the Unified CVP default media server, and your
                                       files are in the media server default locale directory ("< web_server_root >\en-us\app"). However, if you store your files in a location other than these defaults, you must use one or more of the ECC
                                       in the next row in your scripts. |
| Unified CCE (optional variables, used to override defaults) | To make these variables available to your script authors, confirm that they are defined in the Unified CCE Administration tool. For instructions about defining ECC variables for CVP, see the Administration Guide for
                                                   				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html . user.microapp.media_server: Use to identify the Unified CVP
                                                						  media server if it is other than the default. user.microapp.locale: Use to specify the name of the locale
                                                						  directory on the media server if it is other than the default ( "en-us" ). user.microapp.UseVXMLParams: Required in your record script if
                                                						  you include the user.microapp.media_server variable. It tells the external VXML
                                                						  recording script to use the name/value pair of the application that you pass in
                                                						  the user.microapp.ToExtVXML variable. |
| Unified CVP | Unified CVP Server must be installed and configured, as described in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |

| Step 1 | Ensure that your system meets the baseline requirements for software, hardware, and configuration described in the System
                                          Requirements and Limitations section. |
|---|---|
| Step 2 | Configure one or more servers to act as media servers. Configuration requirements include IIS and FTP. |
| Step 3 | In Unified CVP, add media servers, configure FTP connection information, and deploy the media servers. |
| Step 4 | Configure a Unified CVP media server, if you have not already done so. See Configure Media Server for Agent Greeting . . |
| Step 5 | In Unified CVP, republish the VXML Gateway.tcl scripts with updated Agent Greeting support. See Republish the tcl scripts to VXML Gateway for Agent Greeting support. |
| Step 6 | Set the cache size on the VXML Gateway. See Set Cache Size on VXML Gateway . |
| Step 7 | Record the voice prompts to play to agents when they record a greeting and to deploy the audio files to your media server.
                                          See Create Voice Prompts for Recording Greetings . |
| Step 8 | Configure call types to record and play agent greetings. See Configure Call Types . |
| Step 9 | Configure dialed numbers to record and play agent greetings. See Configure Dialed Numbers . |
| Step 10 | Schedule the Script . |
| Step 11 | Define Network VRU Scripts for Agent Greeting . |
| Step 12 | In Script Editor: To use the installed scripts to record and play agent greetings, see Import Example Agent Greeting Scripts . To create your own scripts, see Agent Greeting Scripts . |
| Step 13 | Modify the Unified CCE call routing scripts to use Play Agent Greeting script . |

| Note | To support ASP.NET membership or IIS Manager authentication for the FTP service, you need to select FTP Extensibility . |
|---|---|

| Note | Make note of your FTP connection information -- connection type, user name, password, and port number. |
|---|---|

| Note | After specifying the cache timeout, it is a good idea to clear the cache on the VXML Gateway. This ensures the gateway requests
                                                the latest files from the media server. You need only clear the gateway cache once. Open a command prompt on the CVP VXML
                                                Gateway, log into IOS, and enter the following commands: my_server# conf t my_server(config)# clear http client cache my_server(config)# exit my_server(config)# wr |
|---|---|

| Note | The HTTP client response timeout setting on the gateway must be greater than the time it takes to complete the largest anticipated
                                                FTP file transfer. If an FTP file transfer takes longer than the configured duration in seconds for HTTP client response timeout,
                                                the FTP transfer completes correctly, but the call drops as soon as the configured timeout duration is met. To change the
                                                HTTP client response timeout setting, open a command prompt on the CVP VXML Gateway, log into IOS, and enter the following
                                                commands: my_server# conf t my_server(config)# http client response timeout <new value in seconds> my_server(config)# exit my_server(config)# wr By default, the HTTP client response timeout value for CVP is 30 seconds. |
|---|---|

| Step 1 | In the Unified
                                             			 CVP Operation Console, select Bulk
                                                   				  Administration > File Transfer > Scripts and
                                                   				  Media . |
|---|---|
| Step 2 | Set Device to
                                             			 Gateway. |
| Step 3 | Select the
                                             			 gateways you want to update. Typically you would select all of them unless you
                                             			 have a specific reason not to. |
| Step 4 | Select Default
                                                				Gateway Files . |
| Step 5 | Click Transfer . |

| Step 1 | Create the
                                             			 files using the recording tool of your choice. When you record your files: The media
                                                         					 files must be in .wav format. Your .wav files must match Unified CVP encoding and format
                                                         					 requirements (G.711, CCITT A-Law 8 kHz, 8 bit, mono). Test your
                                                         					 audio files. Ensure that they are not clipped and that they are consistent in
                                                         					 volume and tone. |
|---|---|
| Step 2 | After
                                             			 recording, deploy the files to your Unified CVP media server. The default
                                             			 deployment location is to the <web_server_root> \en-us\app directory. |
| Step 3 | Note the names
                                             			 of the files and the location where you deployed them on the media server. Your
                                             			 script authors need this information for the Agent Greeting scripts. |

| Step 1 | From the
                                             			 Configuration Manager, select Tools > List Tools . |
|---|---|
| Step 2 | Select Call Type List . |
| Step 3 | Click Retrieve . |
| Step 4 | Click Add . |
| Step 5 | Create a call
                                             			 type to record agent greetings and use the name RecordAgentGreeting. 
                                             		  Then click Save . |
| Step 6 | Create a call
                                             			 type to play agent greetings and use the name PlayAgentGreeting. 
                                             		  Then click Save . |

| Step 1 | From the
                                             			 Configuration Manager, select Tools > List Tools . |
|---|---|
| Step 2 | Select Dialed
                                                				  Number/Script Selector List . |
| Step 3 | Click Retrieve . |
| Step 4 | Click Add . |
| Step 5 | On the Attributes tab, do the following: Create a
                                                   			 dialed number to record agent greetings; use the name RecordAgentGreeting.
                                                   			 (The name must match exactly and is case-sensitive.) Set the Media routing domain to Cisco_Voice , and then click Save . Create a
                                                   			 dialed number to play agent greetings; use the name PlayAgentGreeting.
                                                   			 (The name must match exactly and is case-sensitive.) Set the Media routing domain to Cisco_Voice , and then click Save . |
| Step 6 | On the Dialed Number Mapping tab,  
                                             		  do the following: Click Add and map the RecordAgentGreeting dialed number to its call type; click OK . Click Add and map the PlayAgentGreeting dialed number and its call type; click OK . |

| Step 1 | In the Script
                                                				Editor , select Script > Call Type Manager . |
|---|---|
| Step 2 | From the Call
                                             			 Type Manager screen, select the Schedules tab. |
| Step 3 | From the Call
                                             			 type drop-down list, select the call type to associate with the script; for
                                             			 example, PlayAgentGreeting. |
| Step 4 | Click Add and select the script you want from the Scripts
                                             			 box. |
| Step 5 | Click OK twice to exit. |

| Note | If you require the
                                             		  following example VRU scripts, you must manually create them. |
|---|---|

| Name / VRU Script Name | Configuration Parameter | Interruptible (Y/N) | What it does |
|---|---|---|---|
| AgentGreeting PM,-a | null | N | Causes a saved greeting audio file to play. The -a parameter automatically generates the file name by concatenating the Person ID with the AgentGreetingType variable value
                                             set in your routing scripts that target an agent. |
| GreetingMenu_1_to_9 M,press_1_thru_9_greeting,A | 1-9 | Y | During
                                             				a recording session, play an audio file that presents a voice menu prompting
                                             				the agent to press the number corresponding to the greeting he or she wants to
                                             				record. The 1-9 configuration parameter defines the range of
                                             				allowable keys. So this value also determines the number of concurrent
                                             				greetings agents can have. The A parameter specifies that the file is in the (default)
                                             				Application directory on the Unified CVP Server. |
| GreetingSubMenu M,press1-press2-press3,A | 1-3 | Y | During
                                             				a recording session, play an audio file that prompts the agent to press 1 to
                                             				listen to a greeting, 2 to record, or 3 to go to the main menu. |
| Greeting_Not_Found PM,no_greeting_recorded,A | Y | Y | During
                                             				a recording session, if an agent tries to play back a greeting that does not
                                             				exist, play the no_greeting_recorded audio file. The Y configuration parameter in this instance allows
                                             				barge-in (digit entry to interrupt media playback). |
| T10_GS_AUDIUM GS,Server,V, FTP | ,,,,,,,,,,Y | Y | This
                                             				starts the external VXML application that records the greeting. The VRU script
                                             				name must be specified exactly as shown and is case-sensitive. The Y parameter in the eleventh position of the
                                             				Configuration Parameter is required. It allows the script to pass FTP
                                             				connection information to the VXML server. The VXML server then uses this
                                             				information to make an FTP connection to the media server when saving greeting
                                             				files. |
| GreetingReview PM,-a,A | Y | Y | This script allows the agent to review the recorded greeting audio file. |

| Note | For descriptions of VRU Script Name parameters and detailed instructions on creating Network VRU scripts for CVP micro-applications,
                                             see the Configuration and Administration Guide for Cisco Unified Customer Voice Portal. |
|---|---|

| Step 1 | Launch Script
                                             			 Editor. |
|---|---|
| Step 2 | Select File >
                                                				Import Script and select a script to import. The scripts are located in the icm\bin directory on the Unified CCE AW-HDS-DDS. Note When you
                                                            				  import the example scripts, Script Editor maps objects that are referenced in
                                                            				  the scripts. Some of the objects, such as the external Network VRU scripts,
                                                            				  skill groups, route to skill group, or precision queue, do not map
                                                            				  successfully. You must create these manually or change these references to
                                                            				  point to existing scripts, skill groups, and precision queues in your system. | Note | When you
                                                            				  import the example scripts, Script Editor maps objects that are referenced in
                                                            				  the scripts. Some of the objects, such as the external Network VRU scripts,
                                                            				  skill groups, route to skill group, or precision queue, do not map
                                                            				  successfully. You must create these manually or change these references to
                                                            				  point to existing scripts, skill groups, and precision queues in your system. |
| Note | When you
                                                            				  import the example scripts, Script Editor maps objects that are referenced in
                                                            				  the scripts. Some of the objects, such as the external Network VRU scripts,
                                                            				  skill groups, route to skill group, or precision queue, do not map
                                                            				  successfully. You must create these manually or change these references to
                                                            				  point to existing scripts, skill groups, and precision queues in your system. |

| Note | When you
                                                            				  import the example scripts, Script Editor maps objects that are referenced in
                                                            				  the scripts. Some of the objects, such as the external Network VRU scripts,
                                                            				  skill groups, route to skill group, or precision queue, do not map
                                                            				  successfully. You must create these manually or change these references to
                                                            				  point to existing scripts, skill groups, and precision queues in your system. |
|---|---|

| Note | The PAG.ICMS and
                                                		  RECORD_AG.ICMS example scripts assume that a default media server is configured
                                                		  in Unified CVP, and the greeting files are stored in a dedicated directory
                                                		  named ag_gr directory. The WA_AG.ICMS script does not include a dedicated
                                                		  directory. |
|---|---|

| Note | For greeting, the
                                                		  initial script sets up the call between caller and agent, and a different
                                                		  script plays the greeting to the agent after the caller is connected. If the
                                                		  initial Unified CCE script overrides the default media server with a SET node,
                                                		  the call context of expanded call variables is preserved on the greeting
                                                		  playback call as well, and the Default Media Server may be overridden. In this
                                                		  case, modify the greeting playback script to use a SET node with the correct
                                                		  media server. |
|---|---|

| Note | Only one greeting
                                                		  can play per call. If a script references and sets the AgentGreetingType
                                                		  variable more than once in any single path through a script, the last value to
                                                		  be set is the one that plays. |
|---|---|

| Note | If you plan to use
                                          		  the installed example scripts out of the box, you can ignore this section. |
|---|---|

| Node | Value | What it does |
|---|---|---|
| Variable:Call:user. microapp.input_type | D | Sets
                                                				the allowable input type to DTMF (touch tone). |
| RunExtScript:Press 1-9 to Select Greeting X | M,press_1_thru_9_greeting,A | Runs
                                                				the VRU script that defines which digits are valid to select an
                                                				AgentGreetingType and plays a voice prompt describing the options. |
| Variable:Call:AgentGreetingType | Call. CallerEnteredDigits | Sets
                                                				the AgentGreetingType to the digit the agent pressed. This text is used in the
                                                				greeting wave file. It can be a simple numbering system or more descriptive
                                                				titles such as "English." |
| RunExtScript: 1 -
                                                				hear greeting X, 2 -
                                                				record greeting X, 3 -
                                                				return to menu | M,press1-press2-press3,A | Runs
                                                				the VRU script that defines which digits are valid to select a desired action
                                                				and plays a voice prompt describing the options. |
| CED | 1,2,3 | Tells
                                                				the script how to handle the caller entered digits in response to the 1,2,3
                                                				external script. |
| Variable:Call: user.microapp.app_media_lib | Set three times: Once to "app/ag_gr" Twice to "" (an empty string; that is, the default) | Defines the path to the application directory on the Unified CVP
                                                				media server. Prior to playing the greeting file, it is set to the dedicated
                                                				greeting file directory (in this example, app/ag_gr ). After the greeting file plays, it is
                                                				reset to the default application directory where (in this example) the files
                                                				for voice prompts are stored. If the voice prompts were stored in the same
                                                				directory as the greeting files, there would be no need to reset the path. |
| RunExtScript: Play Recording | PM,-a,A | Runs
                                                				the VRU script that plays the selected Agent Greeting. |
| RunExtScript:Greeting Not Found | PM,no_greeting_recorded,A | Runs
                                                				the VRU script that plays an error message if the Agent Greeting selected to
                                                				play does not exist. |
| Variable: Call:user.microapp. ToExtVXML[] | Array
                                                				Index: 2 Value: "ftpPath=< path_to_dedicated/ directory >" For
                                                				example: "ftpPath=en-us/app/ag_gr" | Specifies the FTP information that the VXML server uses to write greeting files to the media server. The information must
                                                match the FTP information configured for the media server in the Unified CVP Operations Console. The
                                                				value for array index must be 2. The value consists of: ftpPath= to set the path to the dedicated directory for agent greeting files. The path must begin with the locale directory. To view additional setting options, see CVP documentation . |
| Variable: Call:user.microapp. ToExtVXML[] | Array
                                                				Index: 0 Value: "application=RecordAgentGreeting" | Identifies the external Unified CVP micro-application
                                                				(RecordAgentGreeting) that is used to record the greeting. The value for
                                                				array index must be 0. |
| RunExtScript: Run Default Recording Application | GS,Server,V | Runs the VRU script that launches the Get Speech micro-application on the VXML server. |

| Note | The Locale
                                                      				  Directory set variable node is optional. It is needed only if you decide to use
                                                      				  a directory other than the default one. |
|---|---|

| Note | There is no
                                       		  counter for the number of failed agent greeting calls. |
|---|---|