---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-maintenance-guide-pcce-b-featur-2b8e9cd668
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/maintenance/guide/pcce_b_features-guide-1262/pcce_b_features-guide-1261_chapter_010001.html
retrieved_at: 2026-08-21T12:29:42.723892+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: November 15, 2024

Chapter: Whisper Announcement

## Chapter: Whisper Announcement

# Whisper Announcement

## Capabilities

Whisper Announcement plays a brief, prerecorded message to an agent just before the agent connects with each caller. The announcement
                           plays only to the agent; the caller hears ringing (based on existing ring tone patterns) while the announcement plays.

The content of the announcement can contain information about the caller that helps prepare the agent to handle the call.
                           The information can include caller language preference, choices the caller made from a menu (Sales, Service), customer status
                           (Platinum, Gold, Regular), and so on.

After Whisper Announcement is enabled, the played announcements are specified in the call routing scripts. The determination
                           of which announcement to play is controlled in the script and is based on various inputs, such as the dialed number, a customer
                           ID look up in your customer database, or selections you made from a VRU menu.

Whisper Announcement is supported for blended outbound agents when they receive inbound calls.

### Functional Limitations

Whisper Announcement is subject to these limitations:

Announcements do not play for outbound calls made by an agent. The announcement plays for inbound calls only.

For Whisper Announcement to work with agent-to-agent calls, use the SendToVRU node before you transfer the call  to the agent.
                                    Transfer the call to Unified CVP before you transfer the call to another agent. Then, Unified CVP can control the call and
                                    play the announcement, regardless of which node transfers the call to Unified CVP.

CVP Refer Transfers do not support Whisper Announcement.

Whisper Announcement supports Silent Monitoring with this exception: For Unified Communications Manager-based Silent Monitoring,
                                    supervisors cannot hear the announcements themselves. The supervisor desktop dims the Silent Monitor button while an announcement
                                    plays.

Only one announcement can play for each call. While an announcement plays, you cannot put the call on hold, transfer, or conference;
                                    release the call; or request supervisor assistance. These features become available again after the announcement completes.

The codec settings for Whisper Announcement recording and the agent's phone must match.  For example, if Whisper Announcement
                                    is recorded in G.711 ALAW, the phone must also be at G.711 ALAW.  If Whisper Announcement is recorded in G.729, the phone
                                    must support or connect using G.729.

Forking happens in Gateway in NBR only when a caller is connected to the agent (with two-way audio). Whisper announcement
                                    is played only with one way audio with agent (before connecting to the caller).

In an IPv6-enabled environment, Whisper Announcement might require extra Media Termination Points (MTPs).

## Deployment
                        	 Tasks

The following
                           		list shows the high-level tasks that are required to deploy Whisper
                           		Announcement. Individual steps are covered in more detail in later sections.

Example scripts that
                           		enable Whisper Announcement are installed with your system. For information
                           		about these scripts and how to access them, see Whisper Announcement Sample Scripts .

### Create Whisper
                           	 Announcement Audio Files

You must
                              		create audio files for each different Whisper Announcement you want to use on
                              		your system; for example, "Sales, English" or "Soporte Técnico en
                                 		  Español." Create the files using the recording tool of your choice.

When
                              		recording your files, follow these rules:

The media files
                                    			 must be in wave (.wav) format. Your wave files must match Unified CVP encoding
                                    			 and format requirements (G729, CCITT G.711 A-Law and U-law 8 kHz, 8 bit, mono).

To avoid cutting
                                    			 off files when they are played, make sure they do not exceed the Whisper
                                    			 Announcement play limit (15 seconds).

Test your audio
                                    			 files. Ensure that they are not cut off and that they are consistent in volume
                                    			 and tone.

To reduce the
                                    			 likelihood of scripting errors, decide ahead of time on a file-naming
                                    			 convention that is easy for you and others to remember. For example,
                                    			 en_sales.wav, sp_support.wav.

### Deploy Whisper
                           	 Announcement Audio Files to Media Server

```
http://<media_server>/<locale_directory>/<application_directory>/<file_name>.
```

For example, if:

The script node
                                    			 that defines the media server has a value of http://myserver.mydomain.com and

The script node
                                    			 that defines the audio file to play has a value of en_sales.wav

Then the HTTP request
                              		for the file is automatically constructed as

```
http://myserver.mydomain.com/en-us/app/en_sales.wav
```

If you store
                              		your files in a different locale and application directory, your routing
                              		scripts must include variable nodes that define those alternate locations. Make
                              		note of the directories in which you place your files and communicate the
                              		locations to your script authors.

Make sure
                              		that the directories in which you deploy your files have the appropriate
                              		permissions to allow Read access.

CVP with the
                                 		  Streaming Audio (Helix) and Whisper Announcement

You must set the user.microapp.media_server variable, to point to the whisper announcement .wav file, for the CVP Whisper Announcement feature to work while Streaming
                              Audio feature (using Helix) is also on. This is achieved by setting the Call.WhisperAnnouncement variable to the complete URL of the whisper announcement wav file. The Call.WhisperAnnouncement variable should be put in using the http://<VXMLserverip>:7000/CVP/audio/XXX.wav URL format.

### Configure Whisper
                           	 Service Dialed Numbers

For Whisper
                              		Announcement, Unified CVP uses two different dialed numbers when transferring a
                              		call to an agent:

The first number
                                    			 calls the ringtone service that the caller hears while the whisper plays to the
                                    			 agent. The CVP default for this number is 91919191.

The second number
                                    			 calls the whisper itself. The Unified CVP default for this number is
                                    			 9191919100.

Whisper
                                                				Announcement dialed number is always an extension of the Ringtone dialed number
                                                				with an extra two zeros at the end.

For Whisper
                              		Announcement to work, your dial plan must include both of these numbers. The
                              		easiest way to ensure coverage is through the use of wild cards such as 9191*.

### Add Whisper Announcement to Routing Scripts

To enable Whisper Announcements, use the Script Editor to modify your  routing scripts as follows:

Specify the WhisperAnnouncement call variable

Specify the Unified CVP media server and location of whisper audio files

Specify other required variables

For more information, see Whisper Announcement Sample Scripts .

#### Specify WhisperAnnouncement Call Variable

To include Whisper Announcement in a script, insert a Set Variable node that references the WhisperAnnouncement call variable.
                                 The WhisperAnnouncement variable causes a whisper to play and specifies the audio file it should use. Typically, you use a
                                 single whisper prompt for a single call type. As a result, you use only one WhisperAnnouncement set node for each script.
                                 However, as needed, you can set the variable at multiple places in your scripts to allow different announcements to play for
                                 different endpoints. For example, for skills-based routing, you can specify the variable at each decision point used to select
                                 a particular skill group or Precision Queue.

Only one Whisper Announcement can play for each call. If a script references and sets the WhisperAnnouncement variable more
                                             than once in a single path through a script, the last value to be set is the one that plays.

Use these settings in the Set Variable node for Whisper Announcement:

Object Type: Call.

Variable: Must use the WhisperAnnouncement variable.

Value: Specify the filename of the whisper file. For example: "my_whisper.wav" or "my_whisper" .

Specify the filename only, not its path.

You must enclose the filename in quotation marks.

The filename is not case sensitive.

The filename cannot include spaces or characters that require URL encoding.

The .wav extension is optional. If you omit it, Unified CVP adds it automatically in the HTTP request.

#### Specify Unified CVP Media Server Information

Ensure that your call routing scripts can access the Whisper Announcement audio files  that you stored on a CVP media server.
                                 If you configure a default media server, and you store the audio files on the default server, you may not have to add any
                                 additional nodes to the scripts.   For more information, see . To test the access, see Test Whisper Announcement File Path .

#### Test Whisper
                              	 Announcement File Path

To test the
                                 		path to the whisper file that you defined in you script variables, enter the
                                 		complete URL into a browser. The .wav file should play. For example:

If your script
                                       			 includes: default media server + default locale + default application directory
                                       			 + whisper.wav, then the path is "http://<default_media_server>/en-us/app/whisper.wav"

If your script
                                       			 includes: http://my_server.my_domain.com + default locale + "app/wav_files" + whisper.wav, then the path is "http://my_server.my_domain.com/en-us/app/wav_files/whisper.wav"

#### Other Script
                              	 Settings That Are Required for Whisper Announcement

These
                                 		additional settings are required for Whisper Announcement to work:

Enable Target
                                       			 Requery on all script nodes that follow the WhisperAnnouncement variable and
                                       			 target an agent. These include Queue (to Skill Group or Precision Queue), Queue
                                       			 Agent, Route Select, and Select. If Target Requery is not enabled, the Whisper
                                       			 Announcement does not play.

When you run an agent transfer or a conference script, use a
                                       			 SendToVRU or a Run Script Request node before you target an agent.

### Fail-Safe Timeout for Whisper Announcement in Unified CCE

Unified CVP sends one message to Unified CCE each time a Whisper Announcement begins and a second message when the announcement ends. The time stamps from these messages
                                 are used to calculate Whisper Announcement data in Unified CCE reports.

If Unified CVP fails to send a Whisper Announcement end message to Unified CCE , the following occurs:

- Unified CCE cannot accurately calculate the whisper length, thus skewing report data.

- The agent cannot control
                                    			 the call (for example, put it on hold or transfer it) because these controls
                                    			 are disabled while a Whisper Announcement is playing.

To prevent this, Unified CCE has a Whisper Announcement timeout value . This value is 20 seconds and represents the maximum Whisper Announcement play time that Unified CCE uses to calculate its report data.

The value was chosen based on the default Whisper Announcement play time (specified in Unified CVP) of 15 seconds. The extra
                                 5 seconds in the Unified CCE fail-safe timeout is a buffer against latency. While the value is configurable in Unified CCE , changing the value is not supported in Unified CCE .

### Whisper Announcement Sample Scripts

Unified CCE includes sample routing scripts that demonstrate Whisper Announcement. You can use them as learning tools and as models for
                              your own Whisper Announcement scripts. They are the following:

WA.ICMS —This script plays a Whisper Announcement.

WA_AG.ICMS— This script plays both a Whisper Announcement and an Agent Greeting to play on the same call flow.

The script files are located in the c:\icm\bin directory. In Unified CCE Script Editor, they are installed to the application root directory.

To use these scripts you must have a default media server  configured in Unified CVP, and have the Whisper file stored in
                                          the default location on the media server. For that reason, they do not include variables that specify the media server, locale,
                                          or application directories.

#### WA.ICMS Script

This script sets up a Whisper Announcement by setting the Whisper Announcement variable to the desired wave file and then
                                 queuing the call to a skill group or Precision Queue. After an agent is selected from the skill group or Precision Queue and
                                 the call routed to the agent, the whisper plays to the agent.

#### WA_AG.ICMS Script

This script causes both a Whisper Announcement and an Agent Greeting to play.

#### Import Sample Whisper Announcement Scripts

To view or use the sample Whisper Announcement scripts, you must first import them into Unified CCE Script Editor. Follow this procedure to import the scripts:

Step 1

Open Script Editor.

Step 2

Select File > Import Script and select the first of the two scripts to import.

In addition to importing the script, Script Editor tries to map imported objects. Some objects that are referenced in the
                                                sample scripts, such as the external Network VRU scripts or the skill groups or Precision Queues, do not map successfully.
                                                You must create these maps manually or change these references to point to existing Network VRU scripts, skill groups, and
                                                Precision Queues in your system.

Step 3

Repeat steps 2 and 3 for the remaining script.

## Administration and Usage

### Whisper Announcement
                           	 Audio File

You store and serve your Whisper
                              		Announcement audio files from the Cisco Unified Contact Center Enterprise
                              		(Unified CCE) media server. This feature supports only the wave ( .wav ) file type.
                              		The maximum play time for a Whisper Announcement is subject to a timeout.
                              		Playback terminates at the timeout regardless of the actual length of the audio
                              		file. The timeout is 15 seconds. In practice, you may want your messages to be
                              		much shorter than that, 5 seconds or less, to shorten your call-handling time.

#### While a Whisper Announcement Is Playing

Only one Whisper Announcement can play for each call. While a Whisper Announcement is playing, you cannot put the call on
                                 hold, transfer, conference, or release the call, or request supervisor assistance. These features become available again after
                                 the whisper is complete.

#### Whisper Announcement with Transfers and Conference Calls

When an agent transfers or initiates a conference call to another agent, the second agent hears an announcement if the second
                                 agent's number supports Whisper Announcement. In the case of consultative transfers or conferences, while the whisper plays,
                                 the caller hears whatever generally plays during hold. The first agent hears ringing. In the case of blind transfers, the
                                 caller hears ringing while the whisper announcement plays.

#### Reporting and Serviceability

Whisper time is not specifically broken out in Unified CCE reports. In agent, skill group, and Precision Queue reports, the period during which the announcement plays is reported as
                                 Reserved agent state time. In the Termination Call Detail records, it is treated as Ring Time.

Serviceability for Whisper Announcement includes system events to indicate reasons for Whisper Announcement failures and counters
                                 to track the number of failed whisper events.

##### Whisper Announcement in Agent Desktop Software

No configuration is needed to integrate Whisper Announcement with agent desktop software. While a whisper is playing, software
                                    on the agent desktop shows the call in the Ring state. Desk phones show the call in the Talking state.

##### Using Agent Greeting with Whisper Announcement

You can use Agent Greeting along with the Whisper Announcement feature. Consider the following when you use them together:

On the call, the Whisper Announcement always plays first before the greeting.

To shorten your call-handling time, you may want to use shorter whispers and greetings than you might if you were using either
                                          feature by itself. A long whisper followed by a long greeting means a long wait before an agent handles a call.

Usually, agents that use Whisper Announcement handle different types of calls: for example,  "English, Gold Member, Activate
                                          Card, Spanish, Gold Member, Report Lost Card, English, Platinum Member, Account Inquiry." Ensure the greetings your agents
                                          record are generic enough to cover the range of customer calls they handle.

| Note | Whisper
                                                				Announcement dialed number is always an extension of the Ringtone dialed number
                                                				with an extra two zeros at the end. |
|---|---|

| Note | Only one Whisper Announcement can play for each call. If a script references and sets the WhisperAnnouncement variable more
                                             than once in a single path through a script, the last value to be set is the one that plays. |
|---|---|

| Note | To use these scripts you must have a default media server  configured in Unified CVP, and have the Whisper file stored in
                                          the default location on the media server. For that reason, they do not include variables that specify the media server, locale,
                                          or application directories. |
|---|---|

| Step 1 | Open Script Editor. |
|---|---|
| Step 2 | Select File > Import Script and select the first of the two scripts to import. In addition to importing the script, Script Editor tries to map imported objects. Some objects that are referenced in the
                                                sample scripts, such as the external Network VRU scripts or the skill groups or Precision Queues, do not map successfully.
                                                You must create these maps manually or change these references to point to existing Network VRU scripts, skill groups, and
                                                Precision Queues in your system. |
| Step 3 | Repeat steps 2 and 3 for the remaining script. |