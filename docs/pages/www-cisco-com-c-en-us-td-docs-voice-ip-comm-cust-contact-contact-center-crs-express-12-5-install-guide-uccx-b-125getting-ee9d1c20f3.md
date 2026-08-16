---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-ee9d1c20f3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_011.html
retrieved_at: 2026-08-16T21:15:01.146938+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Basic Call and Contact Flow Concepts

## Chapter: Basic Call and Contact Flow Concepts

# Basic Call and Contact Flow Concepts

## Relationships Between Tasks, Sessions, Contacts, and Channels

When installing and configuring Unified IP IVR, you must
                              		  understand the concepts, call flows, and configuration dependencies explained
                              		  in this section:

Task : The Unified CCX receives the incoming call/contact signal on
                                    				a Trigger , which is then assigned an Application . The application can be a
                                    				workflow application, a CM Telephony application, (and in a Unified CCE system)
                                    				an ICM Translation Routing application or an ICM Post-Routing application. When
                                    				the Unified CCX accepts the contact, the application starts an application
                                    				task. The application task in turn invokes an instance of a script associated
                                    				with the application.

Session : A session tracks Contacts as they move around the system.
                                    				This enables information to be shared among contacts that are related to the
                                    				same session.

When a contact is received (inbound) or initiated (outbound), the
                                    				Unified CCX checks to see if an existing session already exists with that
                                    				contact's Implementation ID. The Implementation ID is the Unified CM Global
                                    				CallID plus the Unified CM node (GCID/<node>). If a session already
                                    				exists for the contact, the Unified CCX associates it with that session. If
                                    				there is no session for the contact, the Unified CCX automatically creates one.

After the contact ends, the session remains idle in memory for a
                                    				default period of 30 minutes before being automatically deleted.

Contact . A contact can be a Call , an HTTP request , or an email . A
                                    				contact carries attributes such as creation time, state, language, and so on.

Channel . Each type of contact can have various channel types
                                    				associated with it. Channels are allocated and associated with contacts as
                                    				needed and are used to support performing actions on contacts.

Different types of channels are allocated based on the type of
                                    				contact and the type of dialogue that needs to be supported between the Unified
                                    				CCX and the Contact. For example, a CM Telephony call that is presented to
                                    				Unified CCX will be connected to a CTI Port. To support the call control event
                                    				transfer, a Call Control channel is allocated.

If the Trigger is associated to a Primary and or Secondary
                                    				Dialogue Group, depending on the type, a Media Channel or an MRCP channel will
                                    				be allocated.

If an application is triggered by an HTTP Trigger, an HTTP Control
                                    				Channel will be allocated.

## Frequently Asked Questions about CM Telephony Call Flow Outside Unified CCE

When deploying your system, you should understand the following about call flows and the Unified CM configuration dependencies
                              that can impact call flow:

How is a call presented to the Unified CCX system?

Through the Caller, and then the CTI Route Point. An incoming call is given to the Unified CCX system on a Trigger , which is also called a CTI Route Point . The trigger signals the Unified CCX system through CM Telephony that there is an incoming call.

Unified CCX rejects the call if the Max Session limit has been hit for the Trigger or the Application to which the trigger is assigned.

If there are available sessions, based on the Call Control Group assigned to the trigger, Unified CCX searches for an available CTI Port to receive the call. If it finds an available port,
                                    it sends a request to Unified CM through CM Telephony/CTI requesting that the caller be rerouted from the CTI Route Point
                                    to the CTI Port.

The calling party is a GW (for a call from the PSTN) or an IP Phone (for an internal call into the system).

How does the Unified CCX system determine which CTI Port to use?

A Unified CCX Application requires a Trigger . The trigger type determines whether or not a port will be required.

If an application is started by dialing a phone number, it must have a CM Telephony Trigger .

If an application is started by entering a URL, it must have an HTTP Trigger .

If an application is triggered by calling a CM Telephony Trigger:

The Unified CCX system looks for an available CTI Port in the CM Telephony Call Control Group assigned to the Trigger.

Unified CCX then requests the Unified CM to Redirect the caller to the desired CTI Port .

The call is presented to the CTI Port.

Unified CCX accepts the call on the CTI Port, the call rings on the CTI Port, and a Unified CCX script decides how to handle
                                                   the call.

Why does the CM Telephony Trigger need to have Primary and or Secondary Dialogue Groups assigned to it?

For the Unified CCX system to establish a media connection to a caller, Unified CCX must allocate a Media Channel for that call. When Unified CCX accepts a call on a CTI Port, it looks for an available Media Channel in the Primary Dialog Group . If there are none available, it will look for an available channel in the Secondary Dialogue Group .

What are the Unified CCX script call control choices?

The call control step choices are:

Accept . Answers the call and establishes a media connection. This is based on the Primary and Secondary Dialogue Groups assigned
                                    to the Trigger. It can be either CMT (Cisco Media Termination) or ASR (Automatic Speech Recognition).

Reject . Rejects the call and returns it to Unified CM without answering it.

Terminate . Disconnects the Contact.

Redirect . Requests that Unified CM reroute the caller to another destination.

How are Redirects done?

When Unified CCX requests that a caller be rerouted from a CTI Route Point to a CTI Port.

When a Unified CCX script executes a Call Redirect step

In Unified CCE, when a Unified ICME system sends a Connect request to the Unified CCX system to send a queued call to a destination label.

Once the Unified CCX system requests a Redirect and Unified CM accepts it, the redirecting CTI Port is released and returned
                                             to the idle port list.

## HTTP Contact Flow Outside of Unified CCE

When an HTTP request is presented to Unified CCX:

The HTTP trigger is assigned to an application.

When the URL trigger is hit, an application task is started.

The application is assigned to a script and the script starts.

An HTTP control channel is allocated.

The script performs steps on the triggering contact.

Possible step choices are:

Get HTTP contact information . Obtain Header Information, Parameters, Cookies and Environment Attributes and assign them to local variables.

Send a response . Send a Document Object as a response to the calling browser.

Send a JSP reply . Send a response to the calling browser based on a JSP template. This step allows for the mapping of local variables to keywords
                                    in the template.

HTTP redirect . Allows a calling browser to be redirected to a different URL.

## Summary of Unified IP IVR Contact Flow Outside of Unified CCE

The figure below shows a simplified block diagram of a
                              		  contact flow outside of Unified CCE.

The following are the steps a call or contact takes within a
                              		  Unified IP IVR system with Unified CM but without Unified CCE:

The caller dials the desired phone number or enters a Web address.

Unified CCX receives the contact signal at the phone number
                                    				trigger point or the Web address trigger point.

Unified CCX determines which CTI port to take the contact on and
                                    				sends a Redirect Request to CTI in the Unified CM to send the contact to the
                                    				port:

If the contact is a call, then the Unified CCX system looks
                                          					 for a CTI port in the CM Telephony Call Control Group assigned to the trigger
                                          					 (the phone number).

If the contact is a Web connection, then the Unified CCX
                                          					 system looks for a CTI port in the HTTP Control Group assigned to the trigger
                                          					 (the URL).

Unified CM sends the contact to the specified CTI port.

The caller is presented to Unified CCX on the CTI port.

Unified CCX accepts the call.

Unified CCX starts an application that executes a CCX script.

The script determines how to handle the call:

The Unified CCX script can Redirect the call (for example, when
                                    				no agents are available). Or, the Unified CCX script can answer the call with
                                    				the Accept step.

If the Unified CCX script answers the call and the trigger has
                                    				been assigned a Dialog Group, Unified CCX establishes a media connection with
                                    				the caller.

## Important Unified CM Configuration Dependencies

Unified CM is a software ACD that distributes calls. The
                              		  Unified IP IVR software tells Unified CM how to distribute calls. For both
                              		  products to work together correctly, you should therefore understand how calls
                              		  are set up when you configure the Unified CM devices.

You should be aware of the following:

Repository Datastore . The IDs resides on the Unified CCX server in
                                    				the MSDE or SQL2K database. It holds the prompts, grammars, documents, and
                                    				scripts used by the system.

CTI Ports and Route Points . When configuring Unified CCX in the
                                    				Unified CCX Administration web page, you must enter the information that
                                    				Unified CCX uses to configure CTI Ports and Route Points in Unified CM.

CM Telephony User . When configuring Unified CCX, you define a CM
                                    				Telephony User Prefix that is used to create the CM Telephony User in the
                                    				Unified CM.

Redirects . Redirects are performed when a call comes and the call
                                    				is sent from the route point to the designated CTI port (in this case, the
                                    				redirect takes place internally as part of the protocol), when a Unified CCX
                                    				script executes a call Redirect step, or when a Unified ICME system sends a
                                    				Connect request to the Unified CCX system to send a queued call to a
                                    				destination label.

When the Redirect is performed, if the Unified CM destination is
                                    				available, the call is immediately sent to the Unified CM and released from the
                                    				CTI Port.

Destination . A Redirect will fail if the destination is not
                                    				available.

Redirect Calling Search Space . Unlike the redirect that the Route
                                    				Point does to the CTI Port (which is not configurable), the CSS used for a
                                    				redirect for a call that is already established on a CTI Port is indeed
                                    				controlled by the Redirect Calling Search Space parameter in the Call Control
                                    				Group config.

Calling Search Space . Calling search spaces (CSS) determine the
                                    				partitions that calling devices, including IP phones, SIP phones, and gateways,
                                    				can search when attempting to complete a call. A collection of partitions are
                                    				searched to determine how a dialed number must be routed. The CSS for the
                                    				device and the CSS for the directory number get used together. The directory
                                    				number CSS takes precedence over the device CSS.

See Cisco Unified Communications Manager Maintain and Operate
                                          				  Guides for more information.

Device Regions . Regions determine the maximum bandwidth codec
                                    				that is allowed for calls both intra- and inter-region, not the codec itself.
                                    				In the case of the Unified CCX servers CTI Ports, if the connection to calling
                                    				or called device cannot be made at the Unified CCX servers installed bandwidth,
                                    				then a Transcoder channel must be available.

If you install Unified CCX with the default codec (G.711), your region configuration must allow calls into the region assigned
                                                to the CTI Ports at G.711. Otherwise, calls across the WAN are forced to G.729 in the region configuration, which causes the
                                                call to fail if there are no hardware transcoding resources properly configured and available.

See Regions Configuration for more information.

Device Locations . In the event that one or more of the devices
                                    				are in a location, if sufficient bandwidth is not available, the requested
                                    				call-control operation will fail.

See Location Configuration for more information.

Media Connections . Media connections to the Unified CCX system are
                                    				either all G.711 or all G.729. This means that the Unified CM region
                                    				configuration must allow for connections between devices and the Unified CCX
                                    				server CTI Ports with the appropriate Codec. If not, then Transcoder channels
                                    				MUST be configured and available. You do this at the appropriate matching Codec
                                    				at Unified CCX installation time.

Connection path device (Codec) . When you create a region, you
                                    				specify the codec that can be used for calls between devices within that
                                    				region, and between that region and other regions. The system uses regions also
                                    				for applications that only support a specific codec; for example, an
                                    				application that only uses G.711.

## How Calls Go through the Unified CCE System

### Call Flow Control

The Unified ICME system is a major component of the Unified
                                 		  CCE system. Unified ICME provides a central control system that directs calls
                                 		  to various human and automated systems, such as Integrated Voice Response
                                 		  (IVRs) units [also called Voice Response Units (VRUs)] and Automatic Call
                                 		  Distribution (ACD) systems.

Unified CCX scripts can direct calls based on various
                                 		  criteria, such as time of day or the availability of subsystems. When used with
                                 		  Unified ICME in a Translation Routing or Post Routing Application, the Unified
                                 		  IP IVR system does not make decisions as to what script to run. Instead,
                                 		  Unified ICME controls the call treatment by issuing RUN_VRU_SCRIPT commands to
                                 		  Unified IP IVR system. These RUN_VRU_SCRIPT commands tell Unified IP IVR which
                                 		  Unified CCX script to run.

ICM scripts use four different commands to interact with the
                                 		  Unified IP IVR system:

Connect - To connect the call. The Unified ICME
                                       				system sends the connect message with a label to instruct the Unified IP IVR
                                       				system where to direct the call.

Release - To hang up a call.

RUN_VRU_SCRIPT - To run an ICM VRU script on
                                       				the Unified IP IVR system.

Cancel - To cancel the ICM VRU script currently
                                       				running.

### Two Ways of Configuring Unified IP IVR with Unified ICME

When integrated in a Unified CCE environment, Unified CCX can be used in two different ways depending on the call flow.

You can define your Applications as either post-routing or translation-routing applications.

Post Routing . If the calls will first traverse through the Unified IP IVR and then through Unified CCE, it is considered a Post-Routing
                                       scenario. In this type of call flow, Unified CCE is notified of the call by Unified CCX. The ICM script will not start until
                                       Unified CCX requests instructions from Unified CCE after the Unified CCX Initial Script ends (if one is configured).

An example would be when a caller is prompted by Unified CCX for some information that is intended for subsequent delivery
                                       to a Unified CCE Agent.

Translation Routing . If Unified CCE first has control of the call and it needs to flow through the Unified IP IVR, it is considered a Translation-Routing
                                       scenario. In this type of call flow, the call is under Unified CCE script control when arriving at Unified CCX.

Examples of this call flow are when you have to queue a caller or if you use the Unified IP IVR for menu based (CED) routing.

The Unified ICME system and the Unified CCX system together form the Unified CCE system. In a Unified CCE environment, the
                                             Unified ICME software is the primary controller of all calls. The Unified CCE queuing is done through the Unified CM and Unified CCX software. The agent assigned by the
                                             software to handle a call can be defined in either the Unified CM database or the Unified ICME database.

### Post-routed Call Flow Scenario

This scenario represents a call that is queued in the
                                 		  Unified IP IVR system through Post Routing until an agent becomes available.

In a post-routed call flow:

The caller dials the desired phone number (an application Trigger
                                       				that is a Unified CCX Route Point).

The trigger is linked to a Post-Routing application with a default
                                       				Unified CCX script.

The call is presented to the Unified CCX system.

The Unified CCX system looks for a CTI port in the CM
                                             					 Telephony Call Control Group assigned to the trigger (the phone number).

The Unified CCX system determines which CTI Port to take the
                                             					 call on and sends a redirect request to Unified CM through the CM Telephony
                                             					 protocol.

If no ports are free, the caller hears a "fast busy"
                                             					 until there is a free port to take the call.

Unified CM sends the caller to the specified CTI Port.

The caller is presented to the Unified CCX system on the CTI
                                             					 Port.

The default Unified CCX script linked to the application is
                                             					 run.

The Unified CCX script then determines what to do next:

In most post-routing cases, the script will welcome the caller
                                             					 and collect some information from the caller to be sent over to the Unified
                                             					 ICME system.

The script maps this data using the Set Unified ICME data
                                             					 step.

The script ends with the End step.

Since this is a post-routing application, once the End step is
                                       				reached, the Unified CCX system requests instruction from the Unified ICME
                                       				system.

This instruction is a route request with the VRU peripheral as the
                                       				routing client and the Unified CCX Route Point as the DN.

The Unified ICME system will have an ICM script configured to run
                                       				for this routing client DN. After it is notified of the call, the Unified ICME
                                       				system runs the ICM script.

The ICM script will determine how to handle the call and will
                                       				instruct the Unified CCX system accordingly.

ICM scripts are composed of many different call-handling steps,
                                       				including the following four commands it can send to the Unified CCX
                                       				system-connect, Release, Run VRU Script, and Cancel.

The Unified CCX system responds to the commands from the Unified
                                       				ICME system until the Unified ICME system signals that the call is complete.

For example, the ICM script could send a Run VRU Script request to
                                       				the Unified IP IVR system, instructing the Unified IP IVR system to run a
                                       				script that plays music and thanks the caller for their patience. When an agent
                                       				becomes available, the Unified ICME system sends a Cancel request and the
                                       				Unified IP IVR system stops running the current script.

The Unified ICME system then sends a Connect command with a Normal
                                       				label that indicates the extension of the free agent. The Unified CCX system
                                       				then checks the VRU Script Name variable to determine if it needs to run a
                                       				PreConnect script. The Unified CCX system routes the call to the agent
                                       				indicated in the Normal label.

### Translation-Routed Call Flow Scenario

This scenario represents a call that is queued in the Unified IP IVR through Translation Routing until an agent becomes available.

In a translation-route call flow:

The caller dials the desired phone number (an application Trigger that is a Unified ICME Route Point).

The call is presented to the Unified ICME system.

An ICM script is started. Based on the ICM script logic, the caller is queued for a group of agents. If none are available,
                                       the caller is queued in the Unified IP IVR as follows:

The caller is translation routed to the Unified IP IVR by the PG (the ICM Peripheral Gateway) sending a redirect request to
                                             CTI through CM Telephony. The destination is a Unified CCX Translation Route Point (Trigger).

The Unified ICME system sends along with the call additional information associated with the call, including a reserved DNIS
                                             value, a trunk group, a label for the PG, and instructions for further processing.

The call is presented to the Unified CCX system on the trigger.

The Unified CCX system looks for a CTI port in the CM Telephony Call Control Group assigned to the trigger (the phone number).

The Unified CCX system determines which CTI Port to take the call on and sends a redirect request to through CM Telephony.

The Unified CM sends the caller to the specified CTI Port.

The caller is presented to the Unified CCX system on the CTI Port.

The Unified CCX system accepts the call, starts a session with the ICM PG, and sends a REQUEST_INSTRUCTION request.

The ICM script then determines what to do next. In most cases, it sends a RUN_VRU_SCRIPT request to the Unified CCX system.

The Unified CCX system maps the requested VRU script name to a Unified CCX Script based on the VRU Script configuration in
                                       the Unified CCX system.

The Unified CCX script then determines how to handle the call. A call can either be redirected or answered with the accept
                                       step.

If the Unified CCX script answers the call, and the trigger has been assigned a Dialogue Group, it establishes a media connection
                                       with the caller. At this point the Unified CCX system can interact with the caller as desired.

When the script ends, it sends a RUN_SCRIPT_ RESULT message back to the Unified ICME system. The ICM script determines what
                                       to do next. Typically another RUN_SCRIPT_REQUEST events is sent. This continues until an agent becomes available to take the
                                       call.

Once an agent becomes available, the Unified ICME system sends a CANCEL message to the Unified CCX system.

The Unified CCX system terminates the running script.

The Unified ICME system then sends a CONNECT message that includes the Agent's extension as the Label.

The Unified CCX system then redirects the caller to the agent's extension.

### ICM Subsystem

The ICM subsystem of the Unified CCX system allows Unified IP IVR to interact with the ICM system. The ICM subsystem of Unified
                              CCX uses a proprietary protocol to communicate with the ICM PG.

When using the ICM subsystem, you should understand:

### Service Control interface

The Service Control interface allows the Unified ICME system to provide call-processing instructions to the Unified IP IVR
                                 system. It also provides the Unified ICME system with event reports indicating changes in call state.

The Service Control Interface is enabled from the Unified CCX ICM subsystem configuration web page.

### Labels

The Service Control interface supports four label types:

Normal

The Normal label is a character string that encodes the instructions for routing the call. It contains either a directory
                                       number to which the Unified IP IVR system should route the call or the name of a .wav file representing an announcement.

If you configure the Unified IP IVR system to send an announcement, the Unified IP IVR system plays the .wav file, pauses
                                       for two seconds, and repeats the .wav file followed by the two second pause three additional times. Then it pauses 8 seconds
                                       and plays a fast busy signal until the caller hangs up.

Busy

The Busy label indicates that the caller should receive a busy treatment. Unless you set up a Busy label port group to handle
                                       the call, the Unified IP IVR system generates a simulated busy signal from a .wav file until the caller hangs up.

Ring No Answer

The Ring No Answer (RNA) label indicates that the caller should receive an RNA treatment. Unless you set up a Ring No Answer
                                       label port group to handle the call, the Unified IP IVR system generates a simulated ringing sound from a .wav file until
                                       the caller hangs up.

Default

The Default label indicates that the Unified IP IVR system should run the default script.

### VRU Scripts

The scripts that control Unified IP IVR calls have a VRU Script name in the Unified ICME system that must be properly mapped
                                 to a Unified CCX script name (.aef file) in the Unified CCX system. This mapping is done from the Unified CCX ICM subsystem
                                 configuration web page.

### Expanded Call Variables

Data is passed back and forth between the Unified ICME system and the Unified CCX scripts using Expanded Call Variables . There are 10 default variables available, but others can be configured. Since these variables are used globally throughout
                                 the system, they are considered to be premium and should only be used when necessary. Expanded Call Variables are configured
                                 both in the Unified ICME system and in the Unified CCX system. In the Unified CCX system, they are configured from the Unified
                                 CCX ICM subsystem configuration web page.

### Script Parameter
                           	 Separators

One
                                 		  function that can prove useful is the ability to use the Unified ICME
                                 		  RUN_SCRIPT node with a name that includes parameter separators. The Parameter
                                 		  Separator is defined from the Unified CCX ICM subsystem configuration web page.
                                 		  By default it is the | (pipe) symbol.

One
                                 		  example of its usefulness is if you have one main script. Within that script,
                                 		  you can have multiple branches that would execute based on the value of a
                                 		  parameter that is passed by the Unified ICME system.

Example

Configuration data:

Cisco Unified
                                       				CCX Script name = testscript.aef

VRU Script name
                                       				= testscript ICM VRU Scripts

Run VRU Script
                                       				node in Unified ICME = testscript|100

Get ICM
                                 		  Data step in script testscript.aef:

Field Name: VRU
                                       				Script Name

Token Index: 1

Decoding Type:
                                       				String

Local Variable:
                                       				param1 (of type string)

In the
                                 		  preceding example of a script parameter separator, the script variable param1 will contain the first parameter (after the |)
                                 		  In this case, that would be 100. This example allows the variable param1 to be tested and for the script to take the
                                 		  desired branch based on its value. The benefit is that only one VRU Script
                                 		  needs to be defined in the Unified CCX system, and you do not have to use any
                                 		  other variables as parameters to determine which branch to take in the script.

When you use
                                             			 parameter separators in Unified CCX, the Unified ICME script name must include
                                             			 the parameter as part of its name. If you want to pass a different parameter
                                             			 like "testscript|200" then you need to configure another VRU script
                                             			 on the Unified ICME system and name it testscript|200.

For more
                                 		  information on script parameters, see the Cisco Unified Contact
                                          				  Center Express Editor Step Reference Guide and the Cisco Unified Contact
                                          				  Center Express Getting Started with Scripts .

## Debugging Problems in the Unified IP IVR System

The SS_TEL or SS_SIP (Telephony subsystems) debug traces can be used to debug the CM Telephony aspect of a call.

When debugging Unified ICME problems in the Unified IP IVR system, turn on the ICM related debugs. The Unified CCX LIB_ICM
                              (ICM library) and the SS_ICM (ICM subsystem) show the Unified ICME events messaging. Use the Cisco Unified Contact Center Express Solutions Servicing and Troubleshooting Guide for instructions on how to interpret the messages and how to use Trace.

## Important Unified
                        	 ICME Configuration Dependencies

When
                              		  configuring your Unified IP IVR system in an Unified CCE environment, you need
                              		  to be aware of the following:

The DNs ( Dialed Numbers ) of the
                                    				Route Points, that is, the triggers that you configure in the Unified CCX
                                    				system are used in the Unified ICME system as Translation
                                       				  Route DNIS '. As such, it is critical that these DNs match the Translation
                                    				Route DNIS’ you configure in ICM. If you fail to do this, Translation Routing
                                    				will not work and calls will be dropped.

For example, if
                                    				your Translation Route DNIS pool has DNIS’ 5000, 5001, 5002, and 5003 in it,
                                    				then you must create four Route Points, each with one of those numbers as the
                                    				DN of the Route Point.

TRRoutePoint1 – DN 5000

TRRoutePoint2 – DN 5001

TRRoutePoint3 – DN 5002

TRRoutePoint4 – DN 5003

The CTI port
                                       				  group number IDs in Unified CCX must have the same numbers as the peripheral trunk group numbers in the Unified ICME
                                    				system.

It is imperative
                                    				that the script
                                       				  name referenced in your Unified ICME Run External Script node matches what
                                    				is configured in the VRU Script List configuration in the ICM Subsystem on
                                    				Unified CCX.

In order to
                                 				eliminate any confusion, name the Unified CCX script exactly the same in all
                                 				places.

Consider the
                                 				example BasicQ.aef script provided with your Unified CCX
                                 				server. Obviously, this is the script name by which Unified CCX will know the
                                 				script. However, you can refer to this script in a Run External Script node in
                                 				Unified ICME by whatever name you want. The VRU Script List configuration in
                                 				Unified CCX Application Administration application is where you couple the ICM
                                 				External Script name with the Unified CCX script name.

The VRU Script
                                    				Name column on the left is the name that Unified ICME will refer to when
                                    				calling the script and the Script column on the right is the file name of the
                                    				Unified CCX script you want to run when Unified ICME calls the script mentioned
                                    				in the VRU Script Name column.

As you can
                                    				imagine, if you refer to these scripts by different names in Unified ICME and
                                    				Unified CCX, it can become confusing when it comes time to troubleshoot. Thus
                                    				keep these names exactly the same. This way there is no ambiguity as to what
                                    				script you are referring to.

The VRU
                                       				  connection port numbers in Unified CCX must be the same as the VRU
                                       				  connection port numbers in the Unified ICME system.

Any enterprise ECC (Expanded Call Context) variables must
                                    				be defined on both sides of the system (in Unified IP IVR and in Unified ICME
                                    				software).

| Warning | If you install Unified CCX with the default codec (G.711), your region configuration must allow calls into the region assigned
                                                to the CTI Ports at G.711. Otherwise, calls across the WAN are forced to G.729 in the region configuration, which causes the
                                                call to fail if there are no hardware transcoding resources properly configured and available. |
|---|---|

| Note | The Unified ICME system and the Unified CCX system together form the Unified CCE system. In a Unified CCE environment, the
                                             Unified ICME software is the primary controller of all calls. The Unified CCE queuing is done through the Unified CM and Unified CCX software. The agent assigned by the
                                             software to handle a call can be defined in either the Unified CM database or the Unified ICME database. |
|---|---|

| Note | When you use
                                             			 parameter separators in Unified CCX, the Unified ICME script name must include
                                             			 the parameter as part of its name. If you want to pass a different parameter
                                             			 like "testscript\|200" then you need to configure another VRU script
                                             			 on the Unified ICME system and name it testscript\|200. |
|---|---|---|---|