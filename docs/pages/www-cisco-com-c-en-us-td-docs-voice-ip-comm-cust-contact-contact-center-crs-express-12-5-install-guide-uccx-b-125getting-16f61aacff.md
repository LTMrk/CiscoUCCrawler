---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-16f61aacff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_0111.html
retrieved_at: 2026-08-16T21:15:29.932371+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Install and Configure Unified IP IVR for Unified CCE

## Chapter: Install and Configure Unified IP IVR for Unified CCE

# Install and Configure Unified IP IVR for Unified CCE

## Unified IP IVR in a Unified CCE System

In a Unified CCE system, you can use Unified IP IVR to extract and parse web-based content and present the data to customers
                              using a telephony or an HTTP interface.

Unified IP IVR communicates with Unified ICME software by way of the Service Control Interface (SCI) protocol.

## Unified IP IVR for Unified CCE Installation

The procedure for installing Unified IP IVR for an Unified CCE system is the same as that for installing Unified IP IVR outside
                              of an Unified CCE system.

## Check List for
                        	 Configuring Unified IP IVR in a Unified CCE System

After
                              		  installation, in addition to the configuration tasks described in Unified IP IVR Configuration Checklist ,
                              		  complete the tasks described in the following table to configure Unified IP IVR
                              		  for use in a Unified CCE environment. These tasks should be performed in the
                              		  order listed.

Task

Purpose

Configuration Location

Procedure
                                          					 Location

1. Configure
                                          					 the ICM subsystem.

Allows the
                                          					 Unified IP IVR system to interact with Unified ICME software. Unified ICME
                                          					 software provides a central control system that directs calls to various human
                                          					 and automated systems.

You must
                                          					 enable the Service
                                             						Control Interface to use the ICM subsystem.

The VRU
                                          					 Connection Port is the same number configured in the VRU Peripheral Interface
                                          					 Manager (PIM) on the Unified ICME system. This is the TCP/IP socket number to
                                          					 use for receiving messages from the Unified ICME system.

Unified CCX ICM
                                             						Configuration web page

In the
                                          					 Unified CCX Administration web page, select Subsystems > ICM .

Provisioning
                                          					 the ICM Subsystem sect ion in the Cisco Unified Contact Center Express Administration and Operations Guide .

2. Create
                                          					 and upload Unified CCX VRU scripts.

Unified CCE
                                          					 uses Unified ICME Voice Response Unit (VRU) scripts to handle interactions with
                                          					 contacts. These scripts are loaded as applications on the Unified CCX Engine.

Unified CCX
                                             						ICM Configuration web page

After you
                                          					 create the script, in the Unified CCX Administration web page, select Subsystems > ICM . Then click Add a New VRU
                                             						Script .

Configuring ICM VRU Scripts section in the Cisco Unified Contact Center Express Administration and Operations Guide .

For creating
                                          					 VRU scripts, see the Cisco
                                             						ICM/IP Contact Center Enterprise Edition Scripting and Media Routing
                                             						Guide .

The script
                                          					 you configure in this step is the Unified CCX script to associate with the ICM
                                          					 VRU script. You can select the script from the drop-down list or click the Edit
                                          					 button to specify a new script.

The VRU
                                          					 Script Name configured in this step must be the name of the VRU Script from the
                                          					 Property window of the Run VRU Script call. In other words, the Unified CCX
                                          					 file name configured here and the ICM VRU script file name must have the same
                                          					 name.

All scripts
                                          					 under the \default directory are listed in the drop-down list of the Script
                                          					 field in the Cisco Script Application Configuration page.

To specify a
                                          					 new script, click Edit , enter the script name in the dialog box, and
                                          					 click OK . The User Prompt dialog box closes, and the name
                                          					 you entered appears in the Script field.

If you enter
                                          					 the script name as a file URL, enter the value with double backslashes (\\).
                                          					 For example, file: //c:\\temp\\aa.aef .

The
                                          					 Application Name is the filename of the script in the Unified CCX repository to
                                          					 run for this VRU Script Name. For example, SCRIPT[BasicQ.aef].

A script
                                          					 name is displayed only as an Expression starting in Unified CCX 4.5. The
                                          					 expression formats for different types of script are as follows:

- SCRIPT[aa.aef] for
                                             						User scripts

- SSCRIPT[aa.aef] for
                                             						System scripts

- SCRIPT[FILE[C:\\Windows\aa.aef]] for File scripts

- SCRIPT[URL[http://localhost/aa.aef]] for URL-based scripts

3. Configure
                                          					 Unified IP IVR for ICM Translation Routing.

In
                                          					 translation routing, Unified ICME software receives the call, instead of the
                                          					 Unified IP IVR system, but then Unified ICME software routes the call to the
                                          					 Unified IP IVR for queuing.

Unified CCX ICM Translation
                                             						Routing web page

In Unified
                                          					 CCX Administration, select Applications > Application
                                                						  Management . Then click Add a New Application , select ICM Translation
                                             						Routing and click Next .

Configure
                                             						an ICM Translation-Routing Application section in the Cisco Unified Contact Center Express Administration and Operations Guide .

You must
                                          					 configure Cisco Unified ICME translation-routing applications when the Cisco IP
                                          					 IVR is used as a queue point in an contact center solution.

Translation routing happens when a call is transferred from one
                                          					 peripheral to another. For example, the call could be transferred from a
                                          					 peripheral gateway to an IP IVR.

4.
                                          					 Configure Unified IP IVR for ICM Post Routing.

In a
                                          					 Unified ICME post routing situation, the Unified CM receives the call and
                                          					 controls it.

In this
                                          					 case, Unified IP IVR receives the call directly from the Unified CM and then
                                          					 requests instructions from the Unified ICME system.

Unified CCX ICM
                                             						Post-Routing web page

In Unified
                                          					 CCX Administration, select Applications > Application
                                                						  Management . Then click Add a New Application , select ICM Post Routing and click Next .

Configure an ICM
                                             						Post-Routing Application section in the Cisco Unified Contact Center Express Administration and Operations Guide .

If the
                                          					 agent is configured in the Unified ICME system, Unified CCX gets the routing
                                          					 information for the call from the Unified ICME system, and post routes it to
                                          					 the Unified ICME agent when that agent becomes available.

This
                                          					 situation happens when any phone numbers that are configured in Unified CM as
                                          					 triggers are dialed.

You do not
                                          					 have to configure both ICM post routing and ICM translation routing unless your
                                          					 configuration requires it.

## Important Unified IP IVR Dependency Check List

Before you install Unified ICME, list the values for all the Unified IP IVR configurations listed in the following table.
                              You will need these for your Unified ICME configuration.

Unified CCX route points, group IDs, connection ports, and IVR script names must be the same as the corresponding Unified
                              ICME route points, trunk group numbers, connection ports, ICM VRU script, and enterprise ECC variable names.

The following table lists the configuration dependencies between Unified IP IVR and Unified ICME in a Unified CCE deployment.
                              The items in the left column must be the same as the corresponding items in the right column.

Unified IP IVR Configuration

Unified ICME Configuration

Unified CCX Route Points (DNIS and label for the translation route in the Unified ICME Configuration that maps the route point
                                          in Unified CCX)

ICM Translation Routing Route Points (DNIS and label)

CTI Port Group IDs

ICM peripheral trunk group numbers

VRU connection port

VRU connection port in the Unified ICME system

Unified CCX script names

ICM VRU Script names

Unified CCX enterprise ECC (Extended Call Context) variable names

ICM enterprise ECC variable names

| Task | Purpose | Configuration Location | Procedure
                                          					 Location |
|---|---|---|---|
| 1. Configure
                                          					 the ICM subsystem. | Allows the
                                          					 Unified IP IVR system to interact with Unified ICME software. Unified ICME
                                          					 software provides a central control system that directs calls to various human
                                          					 and automated systems. You must
                                          					 enable the Service
                                             						Control Interface to use the ICM subsystem. The VRU
                                          					 Connection Port is the same number configured in the VRU Peripheral Interface
                                          					 Manager (PIM) on the Unified ICME system. This is the TCP/IP socket number to
                                          					 use for receiving messages from the Unified ICME system. | Unified CCX ICM
                                             						Configuration web page In the
                                          					 Unified CCX Administration web page, select Subsystems > ICM . | Provisioning
                                          					 the ICM Subsystem sect ion in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 2. Create
                                          					 and upload Unified CCX VRU scripts. | Unified CCE
                                          					 uses Unified ICME Voice Response Unit (VRU) scripts to handle interactions with
                                          					 contacts. These scripts are loaded as applications on the Unified CCX Engine. | Unified CCX
                                             						ICM Configuration web page After you
                                          					 create the script, in the Unified CCX Administration web page, select Subsystems > ICM . Then click Add a New VRU
                                             						Script . | Configuring ICM VRU Scripts section in the Cisco Unified Contact Center Express Administration and Operations Guide . For creating
                                          					 VRU scripts, see the Cisco
                                             						ICM/IP Contact Center Enterprise Edition Scripting and Media Routing
                                             						Guide . |
| The script
                                          					 you configure in this step is the Unified CCX script to associate with the ICM
                                          					 VRU script. You can select the script from the drop-down list or click the Edit
                                          					 button to specify a new script. The VRU
                                          					 Script Name configured in this step must be the name of the VRU Script from the
                                          					 Property window of the Run VRU Script call. In other words, the Unified CCX
                                          					 file name configured here and the ICM VRU script file name must have the same
                                          					 name. All scripts
                                          					 under the \default directory are listed in the drop-down list of the Script
                                          					 field in the Cisco Script Application Configuration page. To specify a
                                          					 new script, click Edit , enter the script name in the dialog box, and
                                          					 click OK . The User Prompt dialog box closes, and the name
                                          					 you entered appears in the Script field. If you enter
                                          					 the script name as a file URL, enter the value with double backslashes (\\).
                                          					 For example, file: //c:\\temp\\aa.aef . The
                                          					 Application Name is the filename of the script in the Unified CCX repository to
                                          					 run for this VRU Script Name. For example, SCRIPT[BasicQ.aef]. A script
                                          					 name is displayed only as an Expression starting in Unified CCX 4.5. The
                                          					 expression formats for different types of script are as follows: SCRIPT[aa.aef] for
                                             						User scripts SSCRIPT[aa.aef] for
                                             						System scripts SCRIPT[FILE[C:\\Windows\aa.aef]] for File scripts SCRIPT[URL[http://localhost/aa.aef]] for URL-based scripts |
| 3. Configure
                                          					 Unified IP IVR for ICM Translation Routing. | In
                                          					 translation routing, Unified ICME software receives the call, instead of the
                                          					 Unified IP IVR system, but then Unified ICME software routes the call to the
                                          					 Unified IP IVR for queuing. | Unified CCX ICM Translation
                                             						Routing web page In Unified
                                          					 CCX Administration, select Applications > Application
                                                						  Management . Then click Add a New Application , select ICM Translation
                                             						Routing and click Next . | Configure
                                             						an ICM Translation-Routing Application section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| You must
                                          					 configure Cisco Unified ICME translation-routing applications when the Cisco IP
                                          					 IVR is used as a queue point in an contact center solution. Translation routing happens when a call is transferred from one
                                          					 peripheral to another. For example, the call could be transferred from a
                                          					 peripheral gateway to an IP IVR. |
| 4.
                                          					 Configure Unified IP IVR for ICM Post Routing. | In a
                                          					 Unified ICME post routing situation, the Unified CM receives the call and
                                          					 controls it. In this
                                          					 case, Unified IP IVR receives the call directly from the Unified CM and then
                                          					 requests instructions from the Unified ICME system. | Unified CCX ICM
                                             						Post-Routing web page In Unified
                                          					 CCX Administration, select Applications > Application
                                                						  Management . Then click Add a New Application , select ICM Post Routing and click Next . | Configure an ICM
                                             						Post-Routing Application section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| If the
                                          					 agent is configured in the Unified ICME system, Unified CCX gets the routing
                                          					 information for the call from the Unified ICME system, and post routes it to
                                          					 the Unified ICME agent when that agent becomes available. This
                                          					 situation happens when any phone numbers that are configured in Unified CM as
                                          					 triggers are dialed. You do not
                                          					 have to configure both ICM post routing and ICM translation routing unless your
                                          					 configuration requires it. |

| Unified IP IVR Configuration | Unified ICME Configuration |
|---|---|
| Unified CCX Route Points (DNIS and label for the translation route in the Unified ICME Configuration that maps the route point
                                          in Unified CCX) | ICM Translation Routing Route Points (DNIS and label) |
| CTI Port Group IDs | ICM peripheral trunk group numbers |
| VRU connection port | VRU connection port in the Unified ICME system |
| Unified CCX script names | ICM VRU Script names |
| Unified CCX enterprise ECC (Extended Call Context) variable names | ICM enterprise ECC variable names |