---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-6-operations-ccvp-b-1261-operati-456d10ec5e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_6/operations/ccvp_b_1261-operations-guide-for-cisco-virtualized-voice-browser/ccvp_b_1252-operations-guide-for-cisco-virtualized-voice-browser_appendix_010.html
retrieved_at: 2026-08-21T16:31:06.858708+00:00
---

Operations Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

# Operations Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

Find Matches in This Book

## Results

Updated: May 12, 2021

Chapter: Command Line
	 Interface

## Chapter: Command Line
	 Interface

# Command Line
                     	 Interface

Cisco VVB provides a
                           		  command line interface as an alternative to the web administration page to
                           		  configure and troubleshoot the system.

## Show Commands

Custom values are set on the VVB servers by the VoiceBrowser.properties and SIPSubsystem.properties properties files. The following commands may reset the custom values to their default values:

```
show vvb cache *
show vvb call *
show vvb mrcp *
show vvb http client response timeout
```

### show vvb version

This
                              		command displays the Cisco VVB versions on
                              		the active partition and the inactive partition. The inactive version is
                              		displayed only if the inactive partition is available.

Command syntax

show vvb version

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show vvb version 
 Active VVB Version: 11.0.0.95000-245
 Inactive VVB Version: NA
Command successful.
```

### show vvb components

This
                              		command displays the various components in Cisco VVB for which
                              		tracing can be turned on or off from CLI commands. This command is useful when
                              		you need the list of components to modify the trace settings of Cisco VVB .

Command syntax

show vvb components

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show vvb components
Various components are as follows -

 AppAdmin
 Engine
```

### show vvb subcomponents

This
                              		command displays the various subcomponents in specific Cisco VVB component.
                              		This command is useful when you need the list of subcomponents to modify the
                              		trace settings of Cisco VVB .

Command syntax

show vvb subcomponents component [options]

Options

APP_MGR

ARCHIVE_MGR

BOOTSTRAP_MGR

CFG_MGR

CHANNEL_MGR
                                             				  and so on

page —Displays the
                                    			 output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show vvb subcomponents Engine
```

### show vvb trace
                           	 levels

This
                              		command displays the names and trace levels of the various Cisco VVB components
                              		and subcomponents. 
                              		 If the optional component is specified, then the trace
                              		settings of all the subcomponents of the specified component are displayed. If
                              		both the optional component and subcomponent are specified, then the trace
                              		settings of the specified subcomponent of the specified component are
                              		displayed.

Command syntax

show vvb trace levels
                                 		  [options]

Options

Component —Displays the
                                    			 trace levels of all the subcomponents of this component

Sub-component —Displays
                                    			 the trace levels of this subcomponent for the specified component. The trace
                                    			 levels can be displayed only if the component was specified

page —Displays the
                                    			 output one page at a time

file —Stores the output
                                    			 to a file instead of showing it on the console. The name of the file is
                                    			 displayed after the completion of the command

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show vvb trace levels Engine SS_VB Trace settings for component "Engine" and module 'SS_VB' are
  ALARM = true
  DEBUGGING = false
  XDEBUGGING1 = false
  XDEBUGGING2 = false
  XDEBUGGING3 = false
  XDEBUGGING4 = false
  XDEBUGGING5 = false

 Command successful.
```

### show vvb trace file
                           	 size

This
                              		command shows the trace file size for the specified component.

Command syntax

show vvb trace file size [component]

Options

component—(Mandatory) Component such as Engine

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: Yes

Example

```
admin: show vvb trace file size Engine
Trace file size for Engine is 3000000 bytes.

Command Successful.
```

### show vvb trace file
                           	 count

This
                              		commands shows the trace file count for the specified component, which is the
                              		maximum number of trace files. The new file overwrites the older files.

Command syntax

show vvb trace file count
                                 		  [component]

Options

component —(Mandatory)
                              		Component such as Engine

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: Yes

Example

```
admin: show vvb trace file count Engine
Trace file count for Engine is 300.

Command Successful.
```

### show vvb cache
                           	 browser_cache_size

This
                              		command shows the currently allocated browser cache size in KB.

Command syntax

show vvb cache
                                 		  browser_cache_size

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show vvb cache browser_cache_size   
  2048000 KB
 Command successful.
```

### show vvb cache
                           	 dom_cache_capacity

This command shows the DOM cache capacity.

Command syntax

show vvb cache dom_cache_capacity

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show vvb cache dom_cache_capacity  
  64 entries
 Command successful.
```

### show vvb cache
                           	 enable_browser_cache

This command shows if the browser cache is enabled where True is enabled and False is disabled.

Command syntax

show vvb cache enable_browser_cache

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show vvb cache enable_browser_cache  
  true
 Command successful.
```

### show vvb cache
                           	 enable_browser_cache_trace

This command shows if the browser cache trace is enabled.

Command syntax

show vvb cache enable_browser_cache_trace

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show vvb cache enable_browser_cache_trace  
  false
 Command successful.
```

### show vvb cache
                           	 extensions

This
                              		command shows the extensions used for Cisco VVB.

Command syntax

show vvb cache
                                 		  extensions

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show vvb cache extensions
  jsp
  ircgi
  nohead
  testingExt
 Command successful.
```

### show vvb cache
                           	 max_file_size

This command shows the maximum cache size of a resource. If the size of the resource exceeds this limit, the resource will
                              not be added to the cache.

Command syntax

show vvb cache
                                 		  max_file_size

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show vvb cache max_file_size
 2048 KB

 Command successful.
```

### show vvb cache
                           	 cache_entries

This command shows all or selected entries that are cached.

Command syntax

show vvb cache
                                    			 cache_entries <start_index> <end_index>

Options

<start_index> -
                                 		  (Optional) Provide start index entry number.

<end_index> -
                                 		  (Optional) Provide end index entry number.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example 1

```
admin:show vvb cache cache_entries
Total Cache size: 2048000 KB
Total Cache size used: 66 KB
MaxFileSize: 2048 KB
Total number of Cache Entries: 1
Number of Entries retrieved: 1
EntryType       Size(Bytes)     Cache Entry
----------------------------------------------------------------------
File            68192           http://10.78.0.112:7000/CVP/audio/3min.wav
 Command successful.
```

Example 2

```
admin:show vvb cache cache_entries 1 2
Total Cache size: 2048000 KB
Total Cache size used: 66 KB
MaxFileSize: 2048 KB
Total number of Cache Entries: 1
Number of Entries retrieved: 1
EntryType       Size(Bytes)     Cache Entry
----------------------------------------------------------------------
File            68192           http://10.78.0.112:7000/CVP/audio/3min.wav
 Command successful.
```

### show vvb cache
                           	 cache_entry <URL>

This
                                 		  command shows details, such as size and age, of a cache entry.

Command syntax

show vvb cache cache_entry
                                    			 <URL>

Options

URL - (Mandatory)
                                 		  Provide cache entry URL.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb cache cache_entry http://10.11.12.13:7000/CVP/audio/
																																																					helloworld_audio.wav
EntryType               : File
Cache Entry             : http://10.11.12.13:7000/CVP/audio/helloworld_
																																																												audio.wav
Size                    : 68192 Bytes
Age                     : 09 minutes:19 seconds
FreshTime               : 0
CreationTime            : 23/06/2015 15:40:59
Stale flag              : true
 Command successful.
```

### show vvb call
                           	 active voice summary

This
                                 		  command shows active voice call summary.

Command syntax

show vvb call active voice
                                    			 summary

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb call active voice summary
        Total Concurrent Calls = 1
        Total CPS = 0.1
          Ringtone CPS = 0.0
          Whisper CPS = 0.0
          Agent Greeting CPS = 0.0
          Others CPS = 0.1

 Command successful.
```

### show vvb call ccb
                           	 disconnect-timeout

This
                                 		  command displays timer value used by CCB to wait for disconnect command
                                 		  response from Ingress Gateway.

Command syntax

show vvb call ccb
                                    			 disconnect-timeout

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb call ccb disconnect-timeout
disconnect-timeout: 7 seconds

 Command successful.
```

### show vvb call ccb
                           	 intercept-timeout

This
                                 		  command displays timer value used by CCB to wait for intercept command response
                                 		  from Ingress Gateway.

Command syntax

show vvb call ccb
                                    			 intercept-timeout

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb call ccb intercept-timeout
intercept-timeout: 4 seconds

 Command successful.
```

### show vvb call ccb
                           	 reconnect-timeout

This
                                 		  command displays timer value used by CCB to wait for reconnect command response
                                 		  from Ingress Gateway.

Command syntax

show vvb call ccb
                                    			 reconnect-timeout

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb call ccb reconnect-timeout
reconnect-timeout: 70 seconds

 Command successful.
```

### show vvb call app
                           	 ringtone-timeout

This
                                 		  command shows the maximum duration that is set to play tone for the caller.

Command syntax

show vvb call app
                                    			 ringtone-timeout

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb call app ringtone-timeout
ringtone-timeout:100 seconds 
  Command successful.
```

### show vvb call app
                           	 whisper-timeout

This
                                 		  command shows the maximum duration that is set to play tone for the agent.

Command syntax

show vvb call app
                                    			 whisper-timeout [Value]

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb call app whisper-timeout
whisper-timeout:12 seconds 
  Command successful.
```

### show vvb call app dtmf-payload

This command shows the value of DTMF payload.

Command syntax

show vvb call app dtmf-payload

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb call app dtmf-payload
dtmf-payload:100 
  Command successful.
```

### show vvb mrcp asr
                           	 all

This
                                 		  command shows the number of sessions that are currently running on all ASR
                                 		  hosts.

Command syntax

show vvb mrcp asr all

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb mrcp asr all
10.11.12.13	: Concurrent = 0     , Aggregate [Success = 0  , Failure = 0 ]
11.12.13.14	: Concurrent = 0     , Aggregate [Success = 0  , Failure = 0 ]
   Total    : Concurrent = 0     , Aggregate [Success = 0    Failure = 0 ]
 Command successful.
```

### show vvb mrcp tts
                           	 all

This
                                 		  command shows the number of sessions that are currently running on all TTS
                                 		  hosts.

Command syntax

show vvb mrcp tts all

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb mrcp tts all
10.11.12.13	: Concurrent = 0     , Aggregate [Success = 0  , Failure = 0 ]
11.12.13.14	: Concurrent = 0     , Aggregate [Success = 0  , Failure = 0 ]
   Total    : Concurrent = 0     , Aggregate [Success = 0  , Failure = 0 ]
 Command successful.
```

### show vvb mrcp asr
                           	 host

This
                                 		  command shows the number of sessions that are currently running on a particular
                                 		  ASR host.

Command syntax

show vvb mrcp asr host
                                    			 <hostname>

Parameters

<hostname> —Provide ASR server IP address or hostname.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb mrcp asr host 10.11.12.13 
ASR Statistics : 10.11.12.13 
  Concurrent Sessions = 2
  Aggregate Statistics :
       Successful Setups = 6
       Unsuccessful Setups = 0
 Command successful.
```

### show vvb mrcp tts
                           	 host

This
                                 		  command shows the number of sessions that are currently running on a particular
                                 		  TTS host.

Command syntax

show vvb mrcp tts host
                                    			 <hostname>

Parameters

<hostname> —Provide TTS server IP address or hostname.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb mrcp tts host 11.12.13.14
11.12.13.14	 : Concurrent = 0  , Aggregate [Success = 0  , Failure = 0 ]
 Command successful.
```

### show vvb
                           	 host-to-ip

Shows the user
                                 		  entries from /etc/hosts file.

Command syntax

show vvb
                                       				host-to-ip

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb host-to-ip

IPAddress      HostName
10.11.12.13 vb250.cisco.com vb250

# 2016-06-14 12:57:02.99 10.11.12.14 vb100 mediaserver1
10.11.12.14 vb100

# 2016-06-14 12:57:09.899 10.11.12.15 vb100 mediaserver2
10.11.12.15 vb100

# 2016-06-14 12:58:18.197 10.11.12.17 vb100 "This is testing"
10.11.12.17 vb100

Command successful.
```

### show vvb http
                           	 client response timeout

Shows the http
                                 		  client response timeout details.

Command syntax

show vvb http
                                       				client response timeout

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

```
admin:show vvb http client response timeout
http fetch timeout:15 seconds
 Command successful.
```

### show speechserver httpsProxy host

This command shows the proxy host of the Speech Server.

Command
                                    Syntax :

Example :

```
admin:show speechserver httpsProxy host
abc.cisco.com
Command successful.
```

### show vvb https strict_hostname_verifier

This command shows the strict_hostname_verifier for VVB. Hostname verifier is used while establishing TLS connection.

Command Syntax :

Example :

```
admin:show vvb https strict_hostname_verifier
true
Command successful.
```

### show speechserver httpsProxy port

This command shows the proxy port of the Speech Server.

Command Syntax :

Example :

```
admin:show speechserver httpsProxy port
80
Command successful.
```

### show vvb sip controlTransport

This command shows the SIP control transport mode.

Command syntax

show vvb sip controlTransport

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb vvb sip controlTransport
controlTransport: TCP
Command successful.
```

### show vvb sip optionsTransport

This command shows the SIP option transport mode.

Command syntax

show vvb sip optionsTransport

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb sip optionsTransport
optionsTransport: TCP
  Command successful.
```

### show vvb http client submit_badfetch_error

This command shows the boolean value to indicate whether submitting bad fetch (404) error to VXML server is enabled.

Command syntax

show vvb http client submit_badfetch_error

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:show vvb http client submit_badfetch_error
true
```

## Set Commands

### set vvb trace
                           	 defaults

This
                              		command sets the default trace levels for all components and subcomponents in Cisco VVB . If the
                              		optional component is specified, it sets the default trace levels only for all
                              		the subcomponents of the specified component. If both the optional component
                              		and subcomponent are specified, it sets the default trace levels only for the
                              		specified subcomponent under the component.

Command syntax

set vvb trace defaults
                                 		  [component] [subcomponent]

Options

Component —(Mandatory)
                                    			 Sets the default trace levels for all the subcomponents of this component. The
                                    			 various components are Engine and AppAdmin .

Sub-component —(Optional) Sets the default trace levels for
                                    			 this subcomponent for the specified component. This trace level can be
                                    			 specified only if the component was specified preceding it.

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set vvb trace defaults Engine SS_HTTP
Default traces restored successfully for the module.
```

### set vvb trace file size
                           	 component size

This
                              		command sets the trace file size for the specified component.

Command syntax

set vvb trace file size
                                 		  [component] [size]

Parameters

component —(Mandatory)
                              		The component such as Engine

size —(Mandatory)
                              		Specifies the file size in bytes

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set vvb trace file size engine 3145728
Trace file size for engine is set to 3145728 bytes.
```

### set vvb trace file count
                           	 component no-of-files

This
                              		command sets the trace file count for the specified component, that is the
                              		maximum number of trace files after which older files will start getting
                              		overwritten.

Command syntax

set vvb trace file count
                                 		  [component] [no-of-files]

Arguments

component —(Mandatory)
                                    			 The component such as Engine .

no-of-files —(Mandatory)
                                    			 Specifies the number of files after which older files will get overwritten.

Requirements

Level
                              		privilege—1

Command
                              		privilege level—1

Allowed
                              		during upgrade—No

Example

```
admin:set vvb trace file count engine 300
Trace file count for engine is set to 300
```

### set vvb trace
                           	 enable

Enables the specified logging level for the sub-component in the component mentioned in the command. The user can enter multiple
                              levels of logging by separating them by commas.

After the completion of the command, a message is displayed showing the current log trace settings enabled.

Restart the Cisco VVB services for the trace changes to take effect.

Command syntax

set vvb trace enable [component] [sub-component] [level]

Options

component —(Mandatory) The component such as Engine

sub-component —(Mandatory) The subcomponent within the component such as SS_SIP within the Engine component.

Level —(Mandatory) The logging level which will be enabled. Tracing levels are Debugging, XDebugging1, XDebugging2, XDebugging2,
                              XDebugging3, XDebugging4 and XDebugging5.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example 1

```
admin:set vvb trace enable engine SS_VB debugging
 Trace for engine :SS_VB:debugging is enabled.
 Command successful.
```

Example 2

```
admin:set vvb trace enable engine SS_SIP XDEBUGGING1,XDEBUGGING2
Trace for engine :SS_SIP:XDEBUGGING1 is enabled
Trace for engine :SS_SIP:XDEBUGGING2 is enabled
Command successful.
```

### set vvb trace
                           	 disable

Disables the specified logging level for the subcomponent in the component mentioned in the command. The user can enter multiple
                              levels of logging by separating them by commas. You cannot use this command to turn off Alarm tracing.

After the completion of the command, a message is displayed showing the current log trace settings enabled.

Restart the Cisco VVB services for the trace changes to take effect.

Command syntax

set vvb trace disable [component] [sub-component] [level]

Options

Component —The component such as Engine .

Sub-component —The subcomponent within the component such as SS_SIP within the Engine component.

Level —(Mandatory) The logging level which will be disabled. Tracing levels are Debugging, XDebugging1, XDebugging2, XDebugging2,
                              XDebugging3, XDebugging4 and XDebugging5. The tracing levels will also be available as part of the help of the command.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example 1

```
admin:set vvb trace disable engine SS_VB debugging
 Trace for engine :SS_VB:debugging is disabled.
 Command successful.
```

Example 2

```
set vvb trace disable engine SS_SIP XDEBUGGING1,XDEBUGGING2
Trace for engine :SS_SIP:XDEBUGGING1 is disabled
Trace for engine :SS_SIP:XDEBUGGING2 is disabled
Command successful.
```

### set password user
                           	 security

This command changes the security/SFTP password on Cisco Virtualized Voice Browser . In addition to changing the security password, it also changes the passwords of the internal Cisco Virtualized Voice Browser users.

Command syntax

set password user
                                 		  security

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set password user security   
Please enter the old password: ******
Please enter the new password: ******
Reenter new password to confirm: ******
WARNING:
Please make sure that the security password on the publisher is changed first.
The security password needs to be the same on all cluster nodes,
including the application server, therefore the security password on all nodes
need to be changed.

After changing the security password on a cluster node, please restart that node.

Continue (y/n)?y

Please wait...

Command successful.
```

### set vvb cache
                           	 enable_browser_cache

This command enables or disables the browser cache where True is enabled and False is disabled.

Command syntax

set vvb cache enable_browser_cache [Option]

Parameters

Boolean —(Mandatory) Enter boolean value true or false.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:set vvb cache enable_browser_cache false 
 Command successful.
```

### set vvb cache
                           	 browser_cache_size

This
                              		command sets the cache size in KB. Setting cache size to 0 disables the cache.
                              		Disabling cache does not add new entries to the cache. However, existing cache
                              		entries can be reused until they are expired.

Command syntax

set vvb cache
                                 		  browser_cache_size [size_in_KB]

Requirements

size_in_KB —Cache Size in KB

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set vvb cache browser_cache_size 1000

 Command successful.
```

If this command is issued while browser cache is disabled
                                          		  (enable_browser_cache = false), a warning message like this will be shown on
                                          		  console: 'Please note that browser cache is currently disabled, so this
                                          		  operation will take effect once caching is enabled again.'

### set vvb cache
                           	 enable_browser_cache_trace

This
                              		command enables or disables the browser cache trace.

Command syntax

set vvb cache
                                 		  enable_browser_cache_trace [Option]

Parameters

Boolean —(Mandatory) Enter boolean value true or false.

Requirements

Level privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set vvb cache enable_browser_cache_trace true
  Command successful.
```

If this command is issued while browser cache is disabled
                                          		  (enable_browser_cache = false), a warning message like this will be shown on
                                          		  console: 'Please note that browser cache is currently disabled, so this
                                          		  operation will take effect once caching is enabled again.'

### set vvb cache
                           	 extensions

This
                              		command is used to create new extensions.

Command syntax

set vvb cache extensions
                                 		  [Name]

Parameters

Name —(Mandatory) Enter the extension name.

Requirements

Level privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set vvb cache extensions newExtension
 Command successful.
```

If this command is issued while browser cache is disabled
                                          		  (enable_browser_cache = false), a warning message like this will be shown on
                                          		  console: 'Please note that browser cache is currently disabled, so this
                                          		  operation will take effect once caching is enabled again.'

### set vvb cache
                           	 max_file_size

This command sets the cache size in KB. Setting cache size to 0 disables the cache. That means that new entries will not be
                              added to the cache; however, existing cache entries will be reused until they are expired.

If .wav files larger than the max file size are fetched, it could impact audio quality. Therefore, it is recommended to increase
                                                the max file size accordingly.

The maximum size of a file that can be cached is 28MB. However, Cisco recommends setting this value to 2MB to avoid initial
                                                file download latency and filling up of the disk space.

Command syntax

set vvb cache
                                 		  browser_cache_size [size_in_KB]

Options

size_in_KB —Cache Size in KB

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set vvb cache browser_cache_size 1000

 Command successful.
```

If this command is issued while browser cache is disabled (enable_browser_cache = false), a warning message like this will
                                          be shown on console: 'Please note that browser cache is currently disabled, so this operation takes effect once caching is
                                          enabled again.'

### set vvb cache
                           	 browser_cache_reset

This command
                                 		  resets the following browser cache related properties to their default values:
                                 		  enable_browser_cache, browser_cache_size, max_file_size, extensions,
                                 		  enable_browser_cache_trace.

Command Syntax

set vvb cache
                                    			 browser_cache_reset

Requirements

Level privilege: 1

Command privilege
                                 		  level: 1

Allowed during
                                 		  upgrade: No

Example

```
admin:set vvb cache browser_cache_reset
  Command successful.
```

### set vvb cache
                           	 stale_cache_entry <URL>

This
                                 		  command marks stale for the given cache entry URL. The stale cache entry
                                 		  resource gets downloaded only for the first instance after it is marked as
                                 		  stale.

Command syntax

set vvb cache
                                    			 stale_cache_entry <URL>

Options

URL - Provide cache
                                 		  entry URL that you like to stale.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb cache stale_cache_entry <URL>   
 Command successful.
```

### set vvb cache
                           	 stale_cache_entries

This command marks stale for all http cache entries. The stale cache entries get downloaded only for the first instance after
                                 it is marked as stale.

Command syntax

set vvb cache
                                    			 stale_cache_entries

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb cache stale_cache_entries   
 Command successful.
```

### set vvb cache stale_tts_cache_entries

This command marks stale for all tts cache entries. The stale cache entries get downloaded only for the first instance after
                                 it is marked as stale.

Command syntax

set vvb cache stale_tts_cache_entries

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:set vvb cache stale_tts_cache_entries   
 Command successful.
```

### set vvb call ccb
                           	 disconnect-timeout

This
                                 		  command sets how long the Courtesy Call Back (CCB) waits for disconnect command
                                 		  response from Ingress Gateway.

Command syntax

set vvb call ccb
                                    			 disconnect-timeout [Value]

Options

Value - Provide value
                                 		  between 4-8 seconds. Default value is set to 4 seconds.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb call ccb disconnect-timeout 5

 Command successful.
```

### set vvb call ccb
                           	 intercept-timeout

This
                                 		  command sets how long the CCB waits for intercept command response from Ingress
                                 		  Gateway.

Command syntax

set vvb call ccb
                                    			 intercept-timeout [Value]

Options

Value - Provide value
                                 		  between 2-8 seconds. Default value is set to 2 seconds.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb call ccb intercept-timeout 5

 Command successful.
```

### set vvb call ccb
                           	 reconnect-timeout

This
                                 		  command sets how long the CCB waits for reconnect command response from Ingress
                                 		  Gateway.

Command syntax

set vvb call ccb
                                    			 reconnect-timeout [Value]

Options

Value - Provide value
                                 		  between 60-180 seconds. Default value is set to 120 seconds.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb call ccb reconnect-timeout 120

 Command successful.
```

### set vvb call app
                           	 ringtone-timeout

This
                                 		  command sets the maximum duration to play tone for the caller.

Command syntax

set vvb call app
                                    			 ringtone-timeout [Value]

Options

Value - Provide value
                                 		  between 30 - 180 seconds. Default value is set to 120 seconds.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb call app ringtone-timeout 100
  Command successful.
```

### set vvb call app
                           	 whisper-timeout

This
                                 		  command sets the maximum duration to play tone for the agent.

Command syntax

set vvb call app
                                    			 whisper-timeout [Value]

Options

Value - Provide value
                                 		  between 10 - 20 seconds. Default value is set to 15 seconds.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb call app whisper-timeout 13 
  Command successful.
```

### set vvb call app dtmf-payload

This command sets the default DTMF payload to be either 100 or 101.

Command syntax

set vvb call app dtmf-payload [Value]

Options

Value - 100 or 101 (default)

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb call app dtmf-payload 100 
  Command successful.
```

### set vvb mrcp asr
                           	 count clear

This
                                 		  command clears all the counts that were recorded from the ASR hosts.

Command syntax

set vvb mrcp asr count
                                    			 clear

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb mrcp asr count clear
ASR reset successfully
 Command successful.
```

### set vvb mrcp tts
                           	 count clear

This
                                 		  command clears all the counts that were recorded from the TTS hosts.

Command syntax

set vvb mrcp tts count
                                    			 clear

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb mrcp asr count clear
ASR reset successfully
 Command successful.
```

### set vvb http
                           	 client response timeout default

This command is used to configure the number of seconds for which the HTTP client waits for a server response to default value.
                                 The default value is 10 seconds.

Command syntax

set vvb http client response timeout default

Requirements

Level privilege: 1

Command privilege level: 1

```
admin:set vvb http client response timeout default
 Command successful.
admin:

admin:show vvb http client response timeout
http fetch timeout:10 seconds
 Command successful.
```

### set vvb http
                           	 client response timeout [seconds]

This
                                 		  command is used to configure the number of seconds for which the HTTP client
                                 		  waits for a server response.

Command syntax

set vvb http client
                                    			 response timeout [ seconds ]

Seconds: specifies
                                 		  the timeout. HTTP client waits for a response from the server after making a
                                 		  request.

Range is from 5 to
                                 		  30. The default is 10.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

```
admin:set vvb http client response timeout value 15
 Command successful.
```

### set speechserver httpsProxy Host

This command sets the proxy host for the Speech Server. It also asks for credentials, if required.

Command Syntax :

```
set speechserver httpsProxy host <hostname/ip>
Does proxy require Crendentials? [Y/N] y
Enter UserName: username
Enter Password: ****
```

Example :

```
admin:set speechserver httpsProxy host abc.com
Does proxy require Crendentials? [Y/N] y
Enter UserName: username
Enter Password: ****
Command successful.
```

You must stop and start Speech Server for the values to be reflected.

Syntax for stopping Speech Server : utils service stop Cisco Speech Server

Syntax for starting Speech Server : utils service start Cisco Speech Server

### set speechserver httpsProxy nonProxyHosts

This command sets the nonProxyHosts for the Speech Server. The traffic will not go via proxy to these hosts.

Command Syntax :

Example :

```
admin:set speechserver httpsProxy nonProxyHosts <list of nonProxyHosts separated by commas>
 Command successful.
```

The parameter can be a single host or mutiple hosts separated by commas.

You must stop and start Speech Server for the values to be reflected.

Syntax for stopping Speech Server : utils service stop Cisco Speech Server

Syntax for starting Speech Server : utils service start Cisco Speech Server

### set speechserver httpsProxy port

This command sets the proxy port for the Speech Server.

Command Syntax :

Example :

```
admin:set speechserver httpsProxy port 80
 Command successful.
```

You must stop and start Speech Server for the values to be reflected.

Syntax for stopping Speech Server : utils service stop Cisco Speech Server

Syntax for starting Speech Server : utils service start Cisco Speech Server

### set vvb sip controlTransport

This command sets the SIP control transport mode.

Command syntax

set vvb sip controlTransport [Value]

Options

Value - tcp/udp (case insensitive)

System is set with the default value TCP. It should not be changed unless explicitely required.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb sip controlTransport TCP 
  Command successful.
```

Cisco VVB Engine restart is required for changes to take affect.

### set vvb sip optionsTransport

This command sets the SIP option transport mode.

Command syntax

set vvb sip optionsTransport [Value]

Options

Value - tcp/udp (case insensitive)

Default value is UDP. It should not be changed unless explicitely required.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb sip optionsTransport TCP
  Command successful.
```

Cisco VVB Engine restart is required for changes to take affect.

### set vvb http client submit_badfetch_error

This command enables/disables the submitting of bad fetch (404) error to the VXML server.

Command syntax

set vvb http client submit_badfetch_error [Option]

Parameters

Boolean —(Mandatory) Enter boolean value true or false.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example

```
admin:set vvb http client submit_badfetch_error false
  Command successful.
```

## Unset Commands

### unset speechserver httpsProxy host

This command unsets the proxy host for the Speech Server.

Command Syntax :

Example :

```
admin:unset speechserver httpsProxy host
Command successful.
```

You must stop and start Speech Server for the values to be reflected.

Syntax for stopping Speech Server : utils service stop Cisco Speech Server

Syntax for starting Speech Server : utils service start Cisco Speech Server

### unset speechserver httpsProxy port

This command unsets the proxy port for the Speech Server.

Command Syntax :

Example :

```
admin:unset speechserver httpsProxy port
Command successful.
```

You must stop and start Speech Server for the values to be reflected.

Syntax for stopping Speech Server : utils service stop Cisco Speech Server

Syntax for starting Speech Server : utils service start Cisco Speech Server

### unset speechserver httpsProxy nonProxyHosts

This command unsets the nonProxy host for the Speech Server.

Command Syntax :

Example :

```
admin:unset speechserver httpsProxy nonProxyHosts
Command successful.
```

You must stop and start Speech Server for the values to be reflected.

Syntax for stopping Speech Server : utils service stop Cisco Speech Server

Syntax for starting Speech Server : utils service start Cisco Speech Server

## Utils Commands

### utils
                           	 remote_account

This
                              		command allows you to enable, disable, create, and check the status of a remote
                              		account.

Command Syntax

utils
                                    			 remote_account status

utils
                                    			 remote_account enable

utils
                                    			 remote_account disable

utils
                                    			 remote_account create username life

Arguments

username —Specifies the
                                    			 name of the remote account. The username can contain only lowercase characters
                                    			 and must be more than six characters long.

life —Specifies the life
                                    			 of the account in days. After the specified number of days, the account
                                    			 expires.

Usage Guidelines

A remote
                              		account generates a pass phrase that allows Cisco support personnel to access
                              		the system for the specified life of the account. You can have only one remote
                              		account that is enabled at a time.

Example

```
admin:utils remote_account status
Remote Support
Status         : disabled
Decode Version : 2
```

### utils system
                           	 upgrade

This
                              		command allows you to install upgrades and Cisco Option Package (COP) files
                              		from both local and remote directories.

Command syntax

utils system upgrade
                                 		  [Options]

Options

initiate —Starts a new
                              		upgrade wizard or assumes control of an existing upgrade wizard. The wizard
                              		prompts you for the location of the upgrade file for Cisco VVB .

status —Displays status
                              		of the upgrade

cancel —Stops the
                              		upgrade process

Example

```
admin:utils system upgrade initiate

Warning: Do not close this window without first canceling the upgrade.

Source:

 1) Remote Filesystem via SFTP
 2) Remote Filesystem via FTP
 3) Local DVD/CD
 q) quit

Please select an option (1 - 3 or "q" ):
```

### utils vvb
                           	 switch-version db-check

This command allows you to check whether the database was corrupted after an unsuccessful switch version due to a restart
                              in the middle of a switch version attempt. The command displays the status of last switch version. If there is a database
                              backup available that can be restored, it prints the time stamp of the backup and displays the CLI command utils vvb switch-version
                              db-recover to recover from this backup.

Command Syntax

utils vvb switch-version db-check

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils vvb switch-version db-check
vvb DB was found to be corrupted.
Last switch version was aborted at 05/29/2012 16:18:07
05/29/2012 16:18:07|root:Switch Version 9.0.1.10000-41 to 9.0.10000-42
Aborted
There is a VVB backup with timestamp 2012-05-29 16:16:19.000000000 +0530
that was taken during a prior switch version.
!!!WARNING!!! IF YOU CHOOSE TO RECOVER FROM THIS BACKUP, ANY CHANGES DONE
TO THE DATABASE AFTER THE TIMESTAMP OF THIS BACKUP WILL BE LOST.
You can run the CLI command "utils vvb switch-version db-recover" to
restore the DB from this backup.
```

### utils vvb
                           	 switch-version db-recover

This command first checks whether the database was corrupted after an
                              		unsuccessful switch version due to the restart in the middle of a switch
                              		version attempt. The command displays the status of the last switch version. If
                              		there is a database backup available that can be restored, it prints the time
                              		stamp of the backup and offer an option to restore the database from this
                              		backup. If the restore option is chosen, the command completes after restoring
                              		the database from this backup and bringing up all the services.

Command Syntax

utils vvb switch-version db-recover

Requirements

Level privilege: 1

Command privilege:1

Allowed during upgrade: No

Example

```
admin:utils vvb switch-version db-recover
VVB DB was found to be corrupted.
Last switch version was aborted at 05/29/2012 16:18:07
05/29/2012 16:18:07|root:Switch Version 9.0.1.10000-42 Aborted
There is a VVB DB backup with timestamp 2012-05-29 16:16:19:000000000
+530 that was taken during a prior switch version.
!!!WARNING!!! IF YOU CHOOSE TO RECOVER FROM THIS BACKUP, ANY CHANGES DONE
TO THE DATABASE AFTER THE TIMESTAMP OF THIS BACKUP WILL BE LOST.
Are you sure you want to continue?
Continue (y/n)?y
This operation may take a few minutes to complete. Please wait
```

### utils vvb
                           	 security_filter enable

Run this command to enable Cisco VVB administration security filter
                              		settings.

Command syntax

utils vvb security_filter enable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
utils vvb security_filter enable

admin:utils vvb security_filter enable
The status of security filter is: enabled
Please restart Cisco VVB service using
'utils service restart Cisco Tomcat' for changes to take effect.
```

### utils vvb
                           	 security_filter disable

Run this command to disable Cisco VVB administration security filter
                              		settings.

Command syntax

utils vvb security_filter disable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils vvb security_filter disable
The status of security filter is: disabled
Please restart Cisco VVB service using
'utils service restart Cisco Tomcat' for changes to take effect.
```

### utils vvb
                           	 security_filter status

Run this command to check the status of Cisco VVB administration
                              		security filter flag.

Command syntax

utils vvb security_filter status

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils vvb security_filter status
vvb security filter is :enabled
```

### utils service
                           	 list

This command shows all the services running on Cisco VVB server.

Command syntax

utils service list

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils service list
Requesting service status, please wait...
Service Manager is running
Getting list of all services
>> Return code = 0
Cisco AMC Service[STARTED]
Cisco Audit Event Service[STARTED]
Cisco CDP[STARTED]
Cisco CDP Agent[STARTED]
Cisco Certificate Change Notification[STARTED]
Cisco Certificate Expiry Monitor[STARTED]
Cisco RIS Data Collector[STARTED]
Cisco RTMT Reporter Servlet[STARTED] Cisco Speechserver[STARTED] Cisco Syslog Agent[STARTED]
Cisco Tomcat[STARTED]
Cisco Tomcat Stats Servlet[STARTED]
Cisco Trace Collection Service[STARTED]
Cisco Trace Collection Servlet[STARTED]
Administration[STARTED]
CVD Dependent Webapp[STARTED]
Cluster View Daemon[STARTED]
Configuration API[STARTED]
Database[STARTED]
Engine[STARTED]
Perfmon Counter Service[STARTED]
SNMP Java Adapter[STARTED]
Serviceability[STARTED]
Voice Subagent[STARTED]
WebServices[STARTED]
Cisco Unified Serviceability RTMT[STARTED]
Host Resources Agent[STARTED]
MIB2 Agent[STARTED]
Platform Administrative Web Service[STARTED]
Platform Communication Web Service[STARTED]
SNMP Master Agent[STARTED]
SOAP -Log Collection APIs[STARTED]
SOAP -Performance Monitoring APIs[STARTED]
SOAP -Real-Time Service APIs[STARTED]
System Application Agent[STARTED]
Cisco DirSync[STOPPED]  Service Not Activated
Cisco Serviceability Reporter[STOPPED]  Service Not Activated
Primary Node =true
Command successful
```

### utils vvb add
                           	 host-to-ip

This command adds
                                 		  the entries from /etc/hosts.

Command Syntax

utils vvb add
                                       				host-to-ip

Requirements

Level privilege: 0

Level privilege: 0

Allowed during
                                 		  upgrade: No

Example

```
admin:utils vvb add host-to-ip vb111 10.11.12.13 mediaserver111

Command successful.
```

### utils vvb delete
                           	 host-to-ip

This command
                                 		  deletes the entries from /etc/hosts.

Command Syntax

utils vvb delete
                                 		  host-to-ip

Requirements

Level privilege: 0

Command privilege
                                 		  level: 0

Allowed during
                                 		  upgrade: No

Example

```
admin:utils vvb delete host-to-ip vb111 10.11.12.13

Command successful.
```

### utils vvb restore
                           	 host-to-ip

Restores the entries in the hosts file, which are removed after the
                                 		  system reboot/restated.

Command Syntax

utils vvb restore host-to-ip

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: No

Example

```
admin:utils vvb restore host-to-ip
Copying the temp file
Copying the temp file success

Command successful.
```

### utils vvb restart

This command is used to restart the Virtualized Voice Browser when required and has two options:

utils vvb restart forceful: This command when run restarts the Virtualized Voice Browser forcefully even though calls are running.

utils vvb restart graceful: This command when run does not restart the Virtualized Voice Browser when the calls are running but restarts only when the
                                       calls are over.

Command Syntax

utils vvb restart

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: No

Example

```
utils vvb restart forceful
Do you really want to restart ?
Enter (yes/no)? yes
Appliance is being Restarted ...
Warning: Restart could take up to 5 minutes.
Stopping Service Manager...

Broadcast message from admin@vb11162
        (unknown) at 15:07 ...

The system is going down for reboot NOW!
```

```
utils vvb restart graceful
Do you really want to restart ?

Enter (yes/no)? yes
Appliance is being Restarted ...
Warning: Restart could take up to 5 minutes.
Stopping Service Manager...

Service Manager shutting down services... Please Wait
Broadcast message from admin@vb11162
        (unknown) at 15:18 ...

The system is going down for reboot NOW!
```

### utils vvb shutdown

This command is used to shutdown the Virtualized Voice Browser when required and has two options:

utils vvb shutdown forceful: This command when run restarts the Virtualized Voice Browser forcefully even though calls are running.

utils vvb shutdown graceful: This command when run does not restart the Virtualized Voice Browser when the calls are running but restarts only when the
                                       calls are over.

Command Syntax

utils vvb shutdown

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: No

Example

```
utils vvb shutdown forceful

Do you really want to shutdown ?

Enter (yes/no)? yes

Appliance is being Powered - Off ...
Warning: Shutdown could take up to 5 minutes.
Stopping Service Manager...
```

```
utils vvb shutdown graceful

Do you really want to shutdown ?

Enter (yes/no)? yes

Appliance is being Powered - Off ...
Warning: Shutdown could take up to 5 minutes.
Stopping Service Manager...
```

## File
                        	 Commands

File commands help
                           		in creating custom files that are stored in a specific directory in Cisco VVB Filesystem.

### file vvb list
                           	 prompt_file

This command lists
                              		prompt files created for various locales.

Command syntax

file vvb list prompt_file
                                 		  file_spec [options]

Arguments

file-spec —(Mandatory)
                              		The file to view. File-spec can contain asterisks (*) as wildcard.

Options

page —Pauses output

detail —Shows detailed
                              		listing

reverse —Reverses sort
                              		order

date —Sorts by date

size —Sorts by size

Requirements

Level privilege: 0

Command privilege
                              		level: 1

Allowed during
                              		upgrade: No

Example

```
admin:file vvb list prompt_file system/default/vb detail
no such file or directory can be found
admin:file vvb list prompt_file system/G711_ULAW/default/vb detail
09 May,2017 22:07:43       32,110  ringback.wav
dir count = 0, file count = 1
```

## Platform CLI
                        	 Commands

This section lists all the platform CLI commands. For syntax of each command and detailed descriptions see Command Line Interface Guide for Cisco Unified Communications Solutions guide.

There are other commands exposed by platform CLI, which may or may not be applicable for Cisco VVB. Running these commands
                                       can affect the usual system behavior of Cisco VVB.

### Platform Show
                           	 Commands

The platform show
                              		commands supported by Cisco VVB are:

show account

show
                                    			 accountlocking

show cli

show date

show diskusage

show hardware

show login

show media
                                    			 stream

show myself

show network *

show open *

show password *

show process *

show registry *

show risdb

show sessions max limit

show stats io

show status

show tech

show timezone

show tls client min-version

show tls server min-version

### Platform Set
                           	 Commands

The platform set
                              		commands supported by Cisco VVB are:

set cli

set commandcount

set date

set logging

set password
                                    			 user admin

set timezone

set webapp
                                    			 session timeout

set tls server cert_type

set tls client min-version

set tls server min-version

set network hostname

set network ip eth0 <ip_address> <netmask> <default gateway>

### Platform Utils
                           	 Commands

The platform utils
                              		commands supported by Cisco VVB are:

utils auditd *

utils iostat

utils iothrottle

utils network
                                    			 capture

utils network
                                    			 ping

utils
                                    			 reset_application_ui_administrator_password

utils service *

### Platform Files
                           	 Commands

The platform file
                              		commands supported by Cisco VVB are:

file delete *

file dump *

file get *

file list *

file search *

file tail

file view

unset network *

delete process

### Platform File Get Commands

This section lists the Platform file get commands for Speech Server service.

#### Get Speech Server Logs

Run the following command to get the Speech Server logs.

file get activelog /speechserver/logs/SpeechServer

#### Gets Speech Server Configuration Logs

Run the following command to get the Speech Server configuration logs.

file get activelog /speechserver/logs/SpeechConfig

| Note | The pound "#"
                                             			 sign, that is prefixed for size, indicates the entry is staled. |
|---|---|

| Note | If this command is issued while browser cache is disabled
                                          		  (enable_browser_cache = false), a warning message like this will be shown on
                                          		  console: 'Please note that browser cache is currently disabled, so this
                                          		  operation will take effect once caching is enabled again.' |
|---|---|

| Note | If this command is issued while browser cache is disabled
                                          		  (enable_browser_cache = false), a warning message like this will be shown on
                                          		  console: 'Please note that browser cache is currently disabled, so this
                                          		  operation will take effect once caching is enabled again.' |
|---|---|

| Note | If this command is issued while browser cache is disabled
                                          		  (enable_browser_cache = false), a warning message like this will be shown on
                                          		  console: 'Please note that browser cache is currently disabled, so this
                                          		  operation will take effect once caching is enabled again.' |
|---|---|

| Note | If .wav files larger than the max file size are fetched, it could impact audio quality. Therefore, it is recommended to increase
                                                the max file size accordingly. The maximum size of a file that can be cached is 28MB. However, Cisco recommends setting this value to 2MB to avoid initial
                                                file download latency and filling up of the disk space. |
|---|---|

| Note | If this command is issued while browser cache is disabled (enable_browser_cache = false), a warning message like this will
                                          be shown on console: 'Please note that browser cache is currently disabled, so this operation takes effect once caching is
                                          enabled again.' |
|---|---|

| Note | You must stop and start Speech Server for the values to be reflected. Syntax for stopping Speech Server : utils service stop Cisco Speech Server Syntax for starting Speech Server : utils service start Cisco Speech Server |
|---|---|

| Note | The parameter can be a single host or mutiple hosts separated by commas. You must stop and start Speech Server for the values to be reflected. Syntax for stopping Speech Server : utils service stop Cisco Speech Server Syntax for starting Speech Server : utils service start Cisco Speech Server |
|---|---|

| Note | You must stop and start Speech Server for the values to be reflected. Syntax for stopping Speech Server : utils service stop Cisco Speech Server Syntax for starting Speech Server : utils service start Cisco Speech Server |
|---|---|

| Note | Cisco VVB Engine restart is required for changes to take affect. |
|---|---|

| Note | Cisco VVB Engine restart is required for changes to take affect. |
|---|---|

| Note | You must stop and start Speech Server for the values to be reflected. Syntax for stopping Speech Server : utils service stop Cisco Speech Server Syntax for starting Speech Server : utils service start Cisco Speech Server |
|---|---|

| Note | You must stop and start Speech Server for the values to be reflected. Syntax for stopping Speech Server : utils service stop Cisco Speech Server Syntax for starting Speech Server : utils service start Cisco Speech Server |
|---|---|

| Note | You must stop and start Speech Server for the values to be reflected. Syntax for stopping Speech Server : utils service stop Cisco Speech Server Syntax for starting Speech Server : utils service start Cisco Speech Server |
|---|---|

| Note | There are other commands exposed by platform CLI, which may or may not be applicable for Cisco VVB. Running these commands
                                       can affect the usual system behavior of Cisco VVB. |
|---|---|