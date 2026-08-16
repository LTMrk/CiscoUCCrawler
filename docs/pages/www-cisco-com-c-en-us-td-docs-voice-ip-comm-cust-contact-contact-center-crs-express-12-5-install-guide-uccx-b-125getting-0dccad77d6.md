---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-0dccad77d6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_01001.html
retrieved_at: 2026-08-16T21:15:38.285333+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: How to Deploy the Sample Script BasicQ.aef

## Chapter: How to Deploy the Sample Script BasicQ.aef

# How to Deploy the Sample Script BasicQ.aef

## How Unified CCX
                        	 Scripts Work in a Unified CCE System

In a
                              		  Unified CCE system, the Unified CCX system uses the ICM subsystem, which
                              		  manages call distribution across sites and call-processing environments.

The Unified
                              		  CCX system is a queue and call-control point within the Enterprise system that the Unified ICME
                              		  system manages. The Unified ICME system manages the queuing and call control.

Cisco User
                              		  to User (UU) scripts, which the BasicQ.aef script is, do not handle complete
                              		  calls, but provides different call-handling instructions to be executed
                              		  sequentially by the Unified CCX server. For example, VRU scripts may play a
                              		  prompt or acquire dual tone multi-frequency (DTMF) values.

The
                              		  following example ICM VRU script runs two different Unified CCX scripts, CollectDigits and BasicQ , that
                              		  provide two different call-handling steps in the ICM VRU script.

ICM VRU
                              		  scripts run when the Unified ICME system sends a Run VRU Script request to the
                              		  Unified CCX system using a Run External Script node in an ICM script. However,
                              		  before the Unified ICME system can run a VRU script, you must have configured
                              		  the Unified CCX script that the VRU script is to run, uploaded it to the
                              		  Unified CCX Repository, and mapped it to the ICM VRU script.

For related
                              		  Unified CCX Contact Center documentation, see Cisco Unified Contact Center Express Documentation .

For related
                              		  Unified CCE documentation, see Cisco Unified Contact Center Enterprise
                                    				Documentation .

### See Also

Cisco Unified Contact Center
                                 			 Express Scripting Series: Volume 1, Getting Started Developing Scripts

Cisco Unified Contact Center
                                 			 Express Scripting Series: Volume 2, Editor Step Reference

Cisco Unified Contact Center
                                 			 Express Scripting Series: Volume 3, Expression Language Reference

Cisco Unified Contact Center
                                 			 Express Administration Guide

Cisco Unified Contact Center
                                 			 Express Installation and Upgrade Guide

Cisco Unified Contact Center
                                 			 Enterprise Installation and Configuration Guide

## BasicQ.aef Script Example

The Unified CCX BasicQ script, BasicQ.aef, is a default
                              		  Unified CCX script for a Unified CCE environment that Cisco provides for the queue treatment part of an enterprise call flow. The script plays several
                              		  prompts, (and puts the call on hold), looping through the prompts until an
                              		  agent phone becomes free and the Unified ICME system can route the call to the
                              		  agent. This script has no variables defined.

The Unified CCX system accepts the call with the Accept step.
                              		  Next, it plays the ICMStayOnline.wav file using the Play Prompt step, then puts
                              		  the call on hold for 30 seconds using the Call Hold and Delay steps. The script
                              		  uses the Call UnHold step to take the call off hold, plays the
                              		  ICMWait4NextAvail.wav file, and then puts the call back on hold for another 60
                              		  seconds. This sequence repeats until a cancel and then a connect are sent to
                              		  connect the call through the Unified ICME system to an available agent or the
                              		  call is released.

The figure below shows an example ICM VRU script. The diagram
                              		  illustrates how the example script calls the Unified CCX BasicQ.aef script as a
                              		  function in the ICM script.

## Configure
                        	 BasicQ.aef

For instructions on configuring Unified IP IVR, see the Cisco Unified Contact Center Express Administration and Operations Guide at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html .

For instructions on installing and configuring Unified ICME for use in a Unified CCE environment, see the Cisco Unified Contact Center Enterprise Install and Upgrade Guides .

To
                              		  configure the BasicQ.aef script, do the following.

Configure a port
                                       			 group and a trigger for ICM translation routing.

Go to the Unified
                                             				  CCX Administration CM Telephony Call Control Group Configuration web
                                          				page by selecting Subsystems > CM
                                                					 Telephony .

Upload the
                                       			 Unified CCX BasicQ script.

Go to the Unified
                                             				  CCX Administration Script Management web page by selecting Application > Script
                                                					 Management and then click Upload new
                                             				  Scripts .

Create the
                                       			 Unified CCX application, BasicQ.

Go to the Unified
                                             				  CCX Administration Application Configuration web page by selecting Applications > Application
                                                					 Management and then click Add a
                                             				  New Application .

Add the BasicQ
                                       			 ICM VRU script.

Go to the Unified
                                             				  CCX Administration ICM Configuration web page by selecting Subsystems > ICM . Then click ICM
                                             				  VRU Scripts and next click Add a new VRU
                                             				  Script .

Select the
                                          				BasicQ.aef script and enter BasicQ for the name.

Configure the
                                       			 BasicQ VRU script in the Unified ICME system.

Go to the Network VRU
                                             				Script List dialog box by selecting from the ICM Configuration Manager
                                                				  Tools > List Tools > Network VRU Script
                                                				  List .

Click Retrieve and then Add .

Make sure that
                                          				the VRU Script Name you enter in the Unified ICME system matches the VRU Script
                                          				Name configured on the Unified IP IVR system and the Enterprise Name matches
                                          				the name of the script called in the Run VRU Script call in the ICM Script
                                          				Editor.

## Test Your
                        	 Deployment

Select the
                              		  target number for your Unified IP IVR system and two phone numbers and an agent
                              		  number in your system.

The
                              		  following is example configuration data:

- Dial Number (DN): 3000

- Telephones: 9501 and 9502

- Agent Number: 24

Using your
                              		  own data or the preceding example data, verify the following sequence of events
                              		  for your system:

A caller dials
                                       			 3000 from phone 9501.

The caller
                                       			 listens to Unified IP IVR play BasicQ music. BasicQ is the name of the VRU
                                       			 script.

Agent 24 logs in
                                       			 to phone 9502 using Cisco Finesse Desktop.

The state for
                                       			 Agents 24 changes to the ready state.

The IP IVR music
                                       			 stops.

Agent 24 gets a
                                       			 screen pop on the Agent Desktop along with a phone ring.

The caller can
                                       			 then hang up or the Agent can drop the call through Cisco Finesse Desktop software.

| Step 1 | Configure a port
                                       			 group and a trigger for ICM translation routing. Go to the Unified
                                             				  CCX Administration CM Telephony Call Control Group Configuration web
                                          				page by selecting Subsystems > CM
                                                					 Telephony . |
|---|---|
| Step 2 | Upload the
                                       			 Unified CCX BasicQ script. Go to the Unified
                                             				  CCX Administration Script Management web page by selecting Application > Script
                                                					 Management and then click Upload new
                                             				  Scripts . |
| Step 3 | Create the
                                       			 Unified CCX application, BasicQ. Go to the Unified
                                             				  CCX Administration Application Configuration web page by selecting Applications > Application
                                                					 Management and then click Add a
                                             				  New Application . |
| Step 4 | Add the BasicQ
                                       			 ICM VRU script. Go to the Unified
                                             				  CCX Administration ICM Configuration web page by selecting Subsystems > ICM . Then click ICM
                                             				  VRU Scripts and next click Add a new VRU
                                             				  Script . Select the
                                          				BasicQ.aef script and enter BasicQ for the name. |
| Step 5 | Configure the
                                       			 BasicQ VRU script in the Unified ICME system. Go to the Network VRU
                                             				Script List dialog box by selecting from the ICM Configuration Manager
                                                				  Tools > List Tools > Network VRU Script
                                                				  List . Click Retrieve and then Add . Make sure that
                                          				the VRU Script Name you enter in the Unified ICME system matches the VRU Script
                                          				Name configured on the Unified IP IVR system and the Enterprise Name matches
                                          				the name of the script called in the Run VRU Script call in the ICM Script
                                          				Editor. |

| Step 1 | A caller dials
                                       			 3000 from phone 9501. |
|---|---|
| Step 2 | The caller
                                       			 listens to Unified IP IVR play BasicQ music. BasicQ is the name of the VRU
                                       			 script. |
| Step 3 | Agent 24 logs in
                                       			 to phone 9502 using Cisco Finesse Desktop. |
| Step 4 | The state for
                                       			 Agents 24 changes to the ready state. |
| Step 5 | The IP IVR music
                                       			 stops. |
| Step 6 | Agent 24 gets a
                                       			 screen pop on the Agent Desktop along with a phone ring. |
| Step 7 | The caller can
                                       			 then hang up or the Agent can drop the call through Cisco Finesse Desktop software. |