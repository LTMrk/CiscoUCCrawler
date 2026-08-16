---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-f5d589dad1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_01101.html
retrieved_at: 2026-08-16T21:15:09.378669+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Unified IP IVR Installation and Configuration

## Chapter: Unified IP IVR Installation and Configuration

# Unified IP IVR Installation and Configuration

## Cisco IP IVR
                        	 Installation

To install
                              		  Unified IP IVR, you must install Unified CCX and select the Unified IP IVR
                              		  product package during the installation.

The Unified
                              		  CCX installation procedure contains two steps:

Installation : Loads the
                                    				Unified CCX software onto your system. At this time, you select the deployment
                                    				type (Unified CM) and a language.

Server Setup : After you
                                    				install Unified CCX, you use the Unified CCX Administration web application to
                                    				perform the initial system setup.

Server Setup : Enables the
                                    				specific Unified CCX components that will run on a particular server. Also
                                    				determines if a server will function as a standby server for high availability.
                                    				This procedure is done for each Unified CCX node in a cluster, including the
                                    				one on which you perform the cluster setup.

Once these
                              		  installation and setup procedures are done, you will have access to the
                              		  complete set of Unified CCX Administration features that are licensed for your
                              		  Unified CCX product.

For installation instructions, including the planning of your Unified IP IVR installation, a pre-installation check list,
                              and an installation and setup check list, see the Cisco Unified Contact
                                       				  Center Express Install and Upgrade Guide at the Install and Upgrade Guides .

## Unified IP IVR
                        	 Configuration

After you
                              		  install and perform the initial set up of Unified IP IVR, use the Unified CCX
                              		  Administration web interface to perform a variety of additional set up and
                              		  configuration tasks.

These tasks
                              		  include:

Configuring
                                    				Unified CCX to work with Unified CM

Configuring the
                                    				required subsystems

Configuring
                                    				Unified CCX for Unified IP IVR

You can
                              		  access the Unified CCX Administration web interface from a server on which
                              		  Unified CCX is installed or from a client system with access to your network.

From a web
                              		  browser on any computer in your network, enter the following URL: http://servername/AppAdmin where servername is the host name or IP address of the
                              		  Unified CCX node.

For detailed instructions about configuring Unified CCX and Unified IP IVR, see the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . The procedure locations referenced in the table are found in the administration guide.

See the https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_series_home.html for the latest Unified CCX documentation.

## Unified IP IVR Configuration Checklist

Do the following tasks in the given order.

Task

Purpose and Notes

Configuration Location

Procedure Location

1. Configure the JTAPI subsystem on Unified CCX.

The Unified CCX Engine uses the JTAPI subsystem to send and
                                          					 receive calls from Unified CM.

JTAPI Configuration web page

From the Unified CCX Administration web page menu bar, select Subsystems > JTAPI . Then select JTAPI provider in the option list on the
                                          					 left.

Configuring a JTAPI Provider section in the Cisco Unified Contact Center Express Administration and Operations Guide .

For the JTAPI Provider configuration, select the IP
                                          					 address(es) or hostname(s) of one of the Available CTI Manager machines.
                                          					 The Available CTI Managers list box lists all the available
                                          				  CTI Managers that are in the Unified CM cluster.

The primary provider is the first value in the list of
                                          					 selected CTI managers in the cluster, and the secondary provider is the second
                                          					 (also the last) value in the list of CTI selected managers in the cluster.

There cannot be more than two selected CTI Managers for JTAPI
                                          					 Provider Configuration.

The User Prefix is used by Unified CCX to create the
                                          					 Application User in Unified CM that controls the Route Points and CTI Ports.

Make sure the users (<User prefix> +"_"+,nodeid) are NOT
                                          					 defined in Unified CM.

On clicking OK , JTAPI users are created in the Unified CM.
                                          					 Depending on how many Unified CCX engines are enabled in the cluster, those
                                          					 many JTAPI users are created.

In an IP IVR system installed independently of Unified CCX,
                                          					 you do not need to configure the RmCm subsystem.

That configuration is shown here only to show you what you
                                          					 would have to configure next if your IP IVR system were installed as a part of
                                          					 Unified CCX.

2. Provision a JTAPI Call Control Group.

The Unified CCX system uses JTAPI call control groups to pool
                                          					 together a series of CTI ports, which the system uses to serve calls as they
                                          					 arrive at the Unified CCX server.

Unified CCX automatically adds the needed CTI ports port
                                          					 assignments and the specified call control groups to the Unified CM database
                                          					 when you click Update .

JTAPI Call Control Group Configuration web page

From the Unified CCX Administration web page menu
                                          					 bar, select Subsystems > JTAPI . Then select JTAPI
                                             					 Call Control Group in the option list on the left.

Provisioning JTAPI Call Control Groups section in the Cisco Unified Contact Center Administration and Operations Guide .

3. Check to make sure the JTAPI information in Unified CCX and
                                          					 Unified CM is synchronized. If it is not synchronized, resynchronize it.

Makes sure the JTAPI configuration data entered in Unified CM
                                          					 through Unified CCX is synchronized with the JTAPI configuration data in
                                          					 Unified CM for every server in both the Unified CM cluster and the Unified CCX
                                          					 cluster.

The check and Synchronize option generates a report describing
                                          					 the status of JTAPI information (JTAPI Users, Port Groups, and Triggers).

The JTAPI Resynchronize dialog box

From the Unified CCX Administration web page menu
                                          					 bar, select Subsystems > JTAPI . Then select Resynchronize in the option list on the
                                          					 left.

Provisioning JTAPI Call Control Group s section in the Cisco Unified Contact Center Express Administration and Operations Guide .

4. Provision the Cisco Media Termination Subsystem.

Specifies the media you need for your system.

The Unified CCX server uses the Real-Time Transport Protocol
                                          					 (RTP) to send and receive media packets over the IP network. To ensure that the
                                          					 Unified CCX can communicate with your Cisco Unified Communications system, you
                                          					 need to configure the RTP ports that the Unified CCX Engine will use to send
                                          					 and receive RTP data.

Cisco Media Termination Dialog Group
                                             						Configuration web page

From the Unified CCX Administration web page menu
                                          					 bar, select Subsystems > Cisco Media and then in
                                          					 the upper, right corner of the window, click the Add a New CMT Dialog Control Group link.

Provisioning the Cisco Media Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide .

You can choose different types of media, from a simple type of
                                          					 media capable of supporting prompts and DTMF (Cisco Media Termination) to a
                                          					 more complex and rich type of media capable of supporting speech recognition.
                                          					 It is even possible to provision calls without media.

Because of the media capabilities, you must provision media
                                          					 manually. Each call requires both a CTI port and a media channel for the system
                                          					 to be backward compatible or to support media interactions.

Media resources are licensed and sold as IVR ports so you can
                                          					 provision more channels than you are licensed for and, at run-time, licensing
                                          					 will be enforced to prevent the system accepting calls, as this would violate
                                          					 your licensing agreements.

5. Provision and configure any other Unified CCX subsystems
                                          					 that you will use.

Expands the functionality of your Unified IP IVR system.

This task includes the following three tasks and depends on
                                          					 whether or not you have bought licenses for subsystems and have installed them
                                          					 when you installed Unified CCX.

Provisioning ASR and TTS section in the Cisco Unified Contact Center Express Administration and Operations Guide .

5.1 Provision an MRCP Automated Speech Recognition (ASR)
                                          					 subsystem. (optional)

Allows users to navigate through a menu of options by speaking
                                          					 instead of pressing keys on a touch-tone telephone.

MRCP ASR Configuration web page

In the Unified CCX Administration web page,
                                          					 select Subsystems > MRCP ASR .

The MRCP ASR software is optional and requires a vendor
                                          					 license.

The License is the number of MRCP ASR port licenses purchased
                                          					 from the ASR vendor. For the currently supported MRCP ASR vendors, see the
                                          					 current Unified CCX Compatibility Matrix .

To configure an MRCP ASR server or a dialog group, click the MRCP ASR Servers or MRCP ASR Dialog Groups respectively in
                                          					 the column on the left of the web page.

The Unified CCX system uses the Media subsystem of the Unified
                                          					 CCX Engine to configure Cisco Media Termination (CMT) dialog groups that can be
                                          					 used to handle simple Dual-Tone Multi-Frequency (DTMF) based dialog
                                          					 interactions with customers. A dialog group is a pool of dialog channels in
                                          					 which each channel is used to perform dialog interactions with a caller.

This step involves the configuration of your:

- MRCP ASR Providers

- MRCP ASR Servers

- MRCP ASR Dialog
                                             						Groups

5.2 Provision an MRCP Text-to-Speech (TTS) subsystem.
                                          					 (optional)

Converts text (UNICODE) into spoken words in order to provide
                                          					 a user with information or to prompt a user to respond to an action.

MRCP TTS Configuration web page

In the Unified CCX Administration web page,
                                          					 select Subsystems > MRCP TTS , click Add MRCP TTS Provider , link, fill in the
                                          					 information required and click Add.

Provisioning ASR and TTS section in the Cisco Unified Contact Center Express Administration and Operations Guide .

The MRCP TTS software is optional and requires a vendor
                                          					 license. For the currently supported MRCP TTS vendors, see the current Unified CCX Compatibility Matrix .

To configure an MRCP TTS server or default gender, click on
                                          					 the MRCP TTS Servers or the MRCP TTS Default Genders in the column
                                          					 on the left of the web page.

This step involves the configuration of your:

- MRCP TTS Providers

- MRCP TTS Servers

- MRCP TTS Default
                                             						Genders

5.3 Provision the HTTP subsystem. (optional)

Enables Unified IP IVR applications to respond to requests
                                          					 from a variety of web clients, including computers and IP phones.

If you are not using HTTP applications, you do not need to
                                          					 provision the HTTP subsystem.

HTTP Trigger Configuration web page

From the Unified CCX Administration menu bar, choose Subsystems > HTTP , and click the Add a New HTTP Trigger link, fill in the
                                          					 information required and click Add .

Provisioning the HTTP Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide .

5.4 Provision the database subsystem. (optional)

Enables Unified CCX applications to interact with database
                                          					 servers in order to make database information accessible to contacts.

For example, if you want customers to be able to dial in to
                                          					 automatically get account information, you would need this subsystem.

The database subsystem is optional.

If you are not using Unified CCX applications that require
                                          					 access to databases, you do not need to provision the Database subsystem.

The ODBC Data Source Administrator window and
                                          					 the Enterprise Database Subsystem Configuration web page

This involves two procedures:

- On the script
                                             						server, select Start > Programs > Administrative Tools > Data Sources (ODBC) .

- From the Unified
                                             						CCX Administration menu bar, select Subsystems > Database ,

- and in the Database Subsystem Configuration web
                                             						page, click Add a New Datasource .

Provisioning the Database Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide .

5.5 Provision the email subsystem. (optional)

Communicates with your email server and enables your Unified
                                          					 IP IVR applications to create and send email.

From the Unified CCX Administration menu bar, select Subsystems > eMail .

Provisioning the eMail Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide .

The email subsystem is optional.

If you are not using email applications, you do not need to
                                          					 provision the eMail subsystem.

Once you configure email functionality, the Unified CCX
                                          					 scripts created with the email steps will function correctly.

The email configuration identifies the default email address
                                          					 and server to be used for sending email (including e-pages and faxes) and for
                                          					 receiving acknowledgments:

- A Mail Server is a
                                             						fully-qualified email server name. For example: server.domain.com)

- An eMail Address
                                             						is an existing fully qualified email address for the administrative account.
                                             						For Example:administrator@domain.com

6. Start the Application Engine

The Application Engine is the execution vehicle for Unified
                                          					 IP IVR scripts.

The application engine runs when you install Unified CCX.
                                          					 However, you need to restart the engine after you configure your subsystems.

Unified CCX Control Center web page

From Unified CCX Administration menu bar, select System > Control Center . Then
                                          					 click Component Activation . Finally, on the
                                          					 Component Activation page, select all your components and click Update.

Starting, Stopping, and Restarting Unified CCX Services section in the Cisco Unified Contact Center Express Administration and Operations Guide .

7. Install and configure the applications that you will use
                                          					 with Unified CCX (as needed).

Enable the Unified IP IVR applications you want.

This task is subdivided into 5 tasks summarized in the
                                          					 following Unified CCX Application Configuration Check List .

See Unified IP IVR Application Configuration Checklist .

For instructions for how to use a specific web page, from the
                                          					 menu bar, select Help > For this
                                                						  page .

## Unified IP IVR
                        	 Application Configuration Checklist

Unified IP
                              		  IVR applications require Unified IP IVR scripts. For instructions on creating
                              		  and editing scripts see the Cisco Unified Contact Center Express Script
                              		  Developer Series documentation at the Cisco Unified Contact Center
                                 			 Express End-User Guides for the latest Unified CCX documentation .

To
                              		  configure your applications for Unified IP IVR, do the following tasks in the
                              		  given order.

Task

Purpose and
                                          					 Notes

Configuration Location

Procedure
                                          					 Location

1. If
                                          					 needed, edit the script that your Unified CCX application will use.

To customize
                                          					 the script for your needs.

By double
                                          					 clicking on an uploaded script listed in the Unified CCX Script Management page, you can open the
                                          					 script with the Unified CCX Editor.

Unified CCX
                                          					 Script Editor (for creating or editing scripts) and Unified CCX Administration
                                          					 web pages

Managing Scripts, Prompts,
                                             						Grammars, and Documents section in the Cisco Unified Contact Center Express Administration and Operations Guide .

See also the
                                          					 Unified CCX Script Developer Series documentation:

- Volume 1, Getting Started with Cisco Unified CCX Scripting

- Volume 2, Cisco Unified CCX Editor Reference

- Volume 3, Cisco Unified CCX Expression Language Reference

These three
                                          					 PDF documents contain the same information that is in the Unified CCX Editor
                                          					 online help, only in PDF format, rather than HTML format.

If you are
                                          					 customizing the Cisco Unified CM AutoAttendant, you should see the
                                          					 customization procedure in the .
                                          					 You can access this guide through the Unified CM documentation web
                                             						page .

2. If
                                          					 needed, create or customize any prompts that your Unified CCX script will use.

Through
                                          					 Unified CCX Administration Media Configuration, you can modify the prompts that
                                          					 your script uses. You can also upload spoken names for each person in the
                                          					 organization, so callers receive spoken names rather than, for example,
                                          					 spelled-out names when the automated attendant is asking the caller to confirm
                                          					 which party they want.

Unified CCX Prompt
                                             						Management web page

From the
                                          					 menu bar in the Unified CCX Administration web page, select Applications > Prompt
                                                						  Management .

Managing Scripts, Prompts,
                                             						Grammars, and Documents section in the Cisco Unified Contact Center Express Administration and Operations Guide .

Some notes
                                          					 on Prompts

- The Cisco Unified CM
                                             						AutoAttendant, for example, comes with a prerecorded, generic welcome prompt.
                                             						You should record your own welcome prompt to customize your automated attendant
                                             						for the specific role that it is to fulfill for your organization.

- You can use any sound
                                             						recording software to record your prompts if the software can save the prompt
                                             						in the required file format. You can record a different welcome prompt for each
                                             						instance of your script application that you create.

- You can record your prompts
                                             						by using Microsoft Sound Recorder. Save each prompt as a .wav file in CCITT
                                             						(mu-law) 8-kHz, 8-bit, mono format. You must have a microphone and speakers on
                                             						your system to use the software.

3. Upload
                                          					 the script.

To put the
                                          					 needed scripts in the Unified CCX repository so that they are available for use
                                          					 in a Unified CCX application.

Unified CCX Script Management web page

From the
                                          					 Unified CCX Administration menu bar, select Applications > Script
                                                						  Management .

In the Script Management page, click Upload New Scripts . Then in the Explorer User Prompt dialog box, type in the script
                                          					 name in expression format.

Uploading a Script section in the Cisco Unified Contact Center Express Administration and Operations Guide .

If you have
                                          					 questions when on a Unified CCX Administration web page, from the menu bar,
                                          					 select the Help > For this
                                                						  page .

4. Upload
                                          					 any prompts needed for the script.

For
                                          					 customized or language specific prompts

Unified CCX Prompt
                                             						Management web page

From the
                                          					 Unified CCX Administration menu bar, select Applications > Prompt
                                                						  Management .

Then in
                                          					 the Prompt Management page, click Upload New Prompts .

Uploading prompts section in the Cisco Unified Contact Center Express Administration and Operations Guide .

5. Add the
                                          					 application.

To perform
                                          					 a telephony task through Unified CCX, you need a Unified CCX application.

Adding an
                                          					 application involves giving it a name, assigning it a script, and defining any
                                          					 application variables.

An example
                                          					 application that comes with Unified IP IVR is the Cisco
                                             						Unified CM AutoAttendant .

The script
                                          					 for the Cisco Unified CM AutoAttendant is aa.aef.

Unified CCX Application
                                             						Configuration web page

From the Unified CCX Administration web page menu bar, select Applications > Application
                                                						  Management and then in the upper, right corner of the
                                          					 window, click the Add New Application link.

Next,
                                          					 Under Application Type, select Cisco Script Application and click Next.

Configure a Cisco Script
                                             						Application section in the Cisco Unified Contact Center Express Administration and Operations Guide .

6. Give
                                          					 the application a name and assign the script to the application.

To make
                                          					 the application available for use.

Unified CCX Script
                                             						Application web page

Configure a Cisco Script
                                             						Application section in the Cisco Unified Contact Center Express Administration and Operations Guide .

7.
                                          					 Customize the application parameters.

If you are
                                          					 using a Cisco supplied script, you might also want to customize the application
                                          					 prompts. For example, you can record and upload your own prompts as previously
                                          					 explained in this check list.

On the
                                          					 Application page, if there are variables, you can customize the application by
                                          					 the definitions (values) you give the variables. The variables are the
                                          					 parameters you specify on the application web page in the Unified CCX
                                          					 Administration tool.

Unified CCX Cisco Script
                                             						Application web page

Configure a Cisco Script
                                             						Application section in the Cisco Unified Contact Center Express Administration and Operations Guide .

8. Add the
                                          					 Application Trigger.

Enable the
                                          					 application to respond to JTAPI calls and/or HTTP requests.

When you
                                          					 configure JTAPI triggers, you need to specify the CTI Route Point attributes
                                          					 used by the trigger. For example, device pool, location, and voice mail
                                          					 profile.

Unified CCX Add Application Triggers web page

See the
                                          					 online help for that web page. Also see Add
                                             						Application Triggers section in the Cisco Unified Contact Center Express Administration and Operations Guide .

Some
                                          					 Configuration Specifics

From
                                                						  the Unified CCX Administration web page, select Applications > Application
                                                      								Management .

In the Application Configuration web page, Click the name of your new
                                                						  application.

In the Cisco Script Application web page for your new
                                                						  application, the Add New Trigger link.

In the
                                                						  pop-up window, select the trigger type and click Next .

Enter
                                                						  the trigger phone number or web address and the other configuration information
                                                						  that you need.

9. Test
                                          					 the application.

Make sure
                                          					 the application works.

Before the
                                          					 Unified IP IVR system can receive calls, the Unified CCX engine must be
                                          					 running.

From one
                                          					 of your phones, phone the number specified by the trigger. Or if you have an
                                          					 HTTP trigger, from your computer, email the specified web address.

Your
                                          					 application specific documentation.

| Task | Purpose and Notes | Configuration Location | Procedure Location |
|---|---|---|---|
| 1. Configure the JTAPI subsystem on Unified CCX. | The Unified CCX Engine uses the JTAPI subsystem to send and
                                          					 receive calls from Unified CM. | JTAPI Configuration web page From the Unified CCX Administration web page menu bar, select Subsystems > JTAPI . Then select JTAPI provider in the option list on the
                                          					 left. | Configuring a JTAPI Provider section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| For the JTAPI Provider configuration, select the IP
                                          					 address(es) or hostname(s) of one of the Available CTI Manager machines.
                                          					 The Available CTI Managers list box lists all the available
                                          				  CTI Managers that are in the Unified CM cluster. The primary provider is the first value in the list of
                                          					 selected CTI managers in the cluster, and the secondary provider is the second
                                          					 (also the last) value in the list of CTI selected managers in the cluster. There cannot be more than two selected CTI Managers for JTAPI
                                          					 Provider Configuration. The User Prefix is used by Unified CCX to create the
                                          					 Application User in Unified CM that controls the Route Points and CTI Ports. Make sure the users (<User prefix> +"_"+,nodeid) are NOT
                                          					 defined in Unified CM. On clicking OK , JTAPI users are created in the Unified CM.
                                          					 Depending on how many Unified CCX engines are enabled in the cluster, those
                                          					 many JTAPI users are created. In an IP IVR system installed independently of Unified CCX,
                                          					 you do not need to configure the RmCm subsystem. That configuration is shown here only to show you what you
                                          					 would have to configure next if your IP IVR system were installed as a part of
                                          					 Unified CCX. |
| 2. Provision a JTAPI Call Control Group. | The Unified CCX system uses JTAPI call control groups to pool
                                          					 together a series of CTI ports, which the system uses to serve calls as they
                                          					 arrive at the Unified CCX server. Unified CCX automatically adds the needed CTI ports port
                                          					 assignments and the specified call control groups to the Unified CM database
                                          					 when you click Update . | JTAPI Call Control Group Configuration web page From the Unified CCX Administration web page menu
                                          					 bar, select Subsystems > JTAPI . Then select JTAPI
                                             					 Call Control Group in the option list on the left. | Provisioning JTAPI Call Control Groups section in the Cisco Unified Contact Center Administration and Operations Guide . |
| 3. Check to make sure the JTAPI information in Unified CCX and
                                          					 Unified CM is synchronized. If it is not synchronized, resynchronize it. | Makes sure the JTAPI configuration data entered in Unified CM
                                          					 through Unified CCX is synchronized with the JTAPI configuration data in
                                          					 Unified CM for every server in both the Unified CM cluster and the Unified CCX
                                          					 cluster. The check and Synchronize option generates a report describing
                                          					 the status of JTAPI information (JTAPI Users, Port Groups, and Triggers). | The JTAPI Resynchronize dialog box From the Unified CCX Administration web page menu
                                          					 bar, select Subsystems > JTAPI . Then select Resynchronize in the option list on the
                                          					 left. | Provisioning JTAPI Call Control Group s section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 4. Provision the Cisco Media Termination Subsystem. | Specifies the media you need for your system. The Unified CCX server uses the Real-Time Transport Protocol
                                          					 (RTP) to send and receive media packets over the IP network. To ensure that the
                                          					 Unified CCX can communicate with your Cisco Unified Communications system, you
                                          					 need to configure the RTP ports that the Unified CCX Engine will use to send
                                          					 and receive RTP data. | Cisco Media Termination Dialog Group
                                             						Configuration web page From the Unified CCX Administration web page menu
                                          					 bar, select Subsystems > Cisco Media and then in
                                          					 the upper, right corner of the window, click the Add a New CMT Dialog Control Group link. | Provisioning the Cisco Media Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| You can choose different types of media, from a simple type of
                                          					 media capable of supporting prompts and DTMF (Cisco Media Termination) to a
                                          					 more complex and rich type of media capable of supporting speech recognition.
                                          					 It is even possible to provision calls without media. Because of the media capabilities, you must provision media
                                          					 manually. Each call requires both a CTI port and a media channel for the system
                                          					 to be backward compatible or to support media interactions. Media resources are licensed and sold as IVR ports so you can
                                          					 provision more channels than you are licensed for and, at run-time, licensing
                                          					 will be enforced to prevent the system accepting calls, as this would violate
                                          					 your licensing agreements. |
| 5. Provision and configure any other Unified CCX subsystems
                                          					 that you will use. | Expands the functionality of your Unified IP IVR system. | This task includes the following three tasks and depends on
                                          					 whether or not you have bought licenses for subsystems and have installed them
                                          					 when you installed Unified CCX. | Provisioning ASR and TTS section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 5.1 Provision an MRCP Automated Speech Recognition (ASR)
                                          					 subsystem. (optional) | Allows users to navigate through a menu of options by speaking
                                          					 instead of pressing keys on a touch-tone telephone. | MRCP ASR Configuration web page In the Unified CCX Administration web page,
                                          					 select Subsystems > MRCP ASR . |
| The MRCP ASR software is optional and requires a vendor
                                          					 license. The License is the number of MRCP ASR port licenses purchased
                                          					 from the ASR vendor. For the currently supported MRCP ASR vendors, see the
                                          					 current Unified CCX Compatibility Matrix . To configure an MRCP ASR server or a dialog group, click the MRCP ASR Servers or MRCP ASR Dialog Groups respectively in
                                          					 the column on the left of the web page. The Unified CCX system uses the Media subsystem of the Unified
                                          					 CCX Engine to configure Cisco Media Termination (CMT) dialog groups that can be
                                          					 used to handle simple Dual-Tone Multi-Frequency (DTMF) based dialog
                                          					 interactions with customers. A dialog group is a pool of dialog channels in
                                          					 which each channel is used to perform dialog interactions with a caller. This step involves the configuration of your: MRCP ASR Providers MRCP ASR Servers MRCP ASR Dialog
                                             						Groups |
| 5.2 Provision an MRCP Text-to-Speech (TTS) subsystem.
                                          					 (optional) | Converts text (UNICODE) into spoken words in order to provide
                                          					 a user with information or to prompt a user to respond to an action. | MRCP TTS Configuration web page In the Unified CCX Administration web page,
                                          					 select Subsystems > MRCP TTS , click Add MRCP TTS Provider , link, fill in the
                                          					 information required and click Add. | Provisioning ASR and TTS section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| The MRCP TTS software is optional and requires a vendor
                                          					 license. For the currently supported MRCP TTS vendors, see the current Unified CCX Compatibility Matrix . To configure an MRCP TTS server or default gender, click on
                                          					 the MRCP TTS Servers or the MRCP TTS Default Genders in the column
                                          					 on the left of the web page. This step involves the configuration of your: MRCP TTS Providers MRCP TTS Servers MRCP TTS Default
                                             						Genders |
| 5.3 Provision the HTTP subsystem. (optional) | Enables Unified IP IVR applications to respond to requests
                                          					 from a variety of web clients, including computers and IP phones. If you are not using HTTP applications, you do not need to
                                          					 provision the HTTP subsystem. | HTTP Trigger Configuration web page From the Unified CCX Administration menu bar, choose Subsystems > HTTP , and click the Add a New HTTP Trigger link, fill in the
                                          					 information required and click Add . | Provisioning the HTTP Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 5.4 Provision the database subsystem. (optional) | Enables Unified CCX applications to interact with database
                                          					 servers in order to make database information accessible to contacts. For example, if you want customers to be able to dial in to
                                          					 automatically get account information, you would need this subsystem. The database subsystem is optional. If you are not using Unified CCX applications that require
                                          					 access to databases, you do not need to provision the Database subsystem. | The ODBC Data Source Administrator window and
                                          					 the Enterprise Database Subsystem Configuration web page This involves two procedures: On the script
                                             						server, select Start > Programs > Administrative Tools > Data Sources (ODBC) . From the Unified
                                             						CCX Administration menu bar, select Subsystems > Database , and in the Database Subsystem Configuration web
                                             						page, click Add a New Datasource . | Provisioning the Database Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 5.5 Provision the email subsystem. (optional) | Communicates with your email server and enables your Unified
                                          					 IP IVR applications to create and send email. | From the Unified CCX Administration menu bar, select Subsystems > eMail . | Provisioning the eMail Subsystem section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| The email subsystem is optional. If you are not using email applications, you do not need to
                                          					 provision the eMail subsystem. Once you configure email functionality, the Unified CCX
                                          					 scripts created with the email steps will function correctly. The email configuration identifies the default email address
                                          					 and server to be used for sending email (including e-pages and faxes) and for
                                          					 receiving acknowledgments: A Mail Server is a
                                             						fully-qualified email server name. For example: server.domain.com) An eMail Address
                                             						is an existing fully qualified email address for the administrative account.
                                             						For Example:administrator@domain.com |
| 6. Start the Application Engine | The Application Engine is the execution vehicle for Unified
                                          					 IP IVR scripts. The application engine runs when you install Unified CCX.
                                          					 However, you need to restart the engine after you configure your subsystems. | Unified CCX Control Center web page From Unified CCX Administration menu bar, select System > Control Center . Then
                                          					 click Component Activation . Finally, on the
                                          					 Component Activation page, select all your components and click Update. | Starting, Stopping, and Restarting Unified CCX Services section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 7. Install and configure the applications that you will use
                                          					 with Unified CCX (as needed). | Enable the Unified IP IVR applications you want. | This task is subdivided into 5 tasks summarized in the
                                          					 following Unified CCX Application Configuration Check List . | See Unified IP IVR Application Configuration Checklist . For instructions for how to use a specific web page, from the
                                          					 menu bar, select Help > For this
                                                						  page . |

| Task | Purpose and
                                          					 Notes | Configuration Location | Procedure
                                          					 Location |
|---|---|---|---|
| 1. If
                                          					 needed, edit the script that your Unified CCX application will use. | To customize
                                          					 the script for your needs. By double
                                          					 clicking on an uploaded script listed in the Unified CCX Script Management page, you can open the
                                          					 script with the Unified CCX Editor. | Unified CCX
                                          					 Script Editor (for creating or editing scripts) and Unified CCX Administration
                                          					 web pages | Managing Scripts, Prompts,
                                             						Grammars, and Documents section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| See also the
                                          					 Unified CCX Script Developer Series documentation: Volume 1, Getting Started with Cisco Unified CCX Scripting Volume 2, Cisco Unified CCX Editor Reference Volume 3, Cisco Unified CCX Expression Language Reference These three
                                          					 PDF documents contain the same information that is in the Unified CCX Editor
                                          					 online help, only in PDF format, rather than HTML format. If you are
                                          					 customizing the Cisco Unified CM AutoAttendant, you should see the
                                          					 customization procedure in the .
                                          					 You can access this guide through the Unified CM documentation web
                                             						page . |
| 2. If
                                          					 needed, create or customize any prompts that your Unified CCX script will use. | Through
                                          					 Unified CCX Administration Media Configuration, you can modify the prompts that
                                          					 your script uses. You can also upload spoken names for each person in the
                                          					 organization, so callers receive spoken names rather than, for example,
                                          					 spelled-out names when the automated attendant is asking the caller to confirm
                                          					 which party they want. | Unified CCX Prompt
                                             						Management web page From the
                                          					 menu bar in the Unified CCX Administration web page, select Applications > Prompt
                                                						  Management . | Managing Scripts, Prompts,
                                             						Grammars, and Documents section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| Some notes
                                          					 on Prompts The Cisco Unified CM
                                             						AutoAttendant, for example, comes with a prerecorded, generic welcome prompt.
                                             						You should record your own welcome prompt to customize your automated attendant
                                             						for the specific role that it is to fulfill for your organization. You can use any sound
                                             						recording software to record your prompts if the software can save the prompt
                                             						in the required file format. You can record a different welcome prompt for each
                                             						instance of your script application that you create. You can record your prompts
                                             						by using Microsoft Sound Recorder. Save each prompt as a .wav file in CCITT
                                             						(mu-law) 8-kHz, 8-bit, mono format. You must have a microphone and speakers on
                                             						your system to use the software. |
| 3. Upload
                                          					 the script. | To put the
                                          					 needed scripts in the Unified CCX repository so that they are available for use
                                          					 in a Unified CCX application. | Unified CCX Script Management web page From the
                                          					 Unified CCX Administration menu bar, select Applications > Script
                                                						  Management . In the Script Management page, click Upload New Scripts . Then in the Explorer User Prompt dialog box, type in the script
                                          					 name in expression format. | Uploading a Script section in the Cisco Unified Contact Center Express Administration and Operations Guide . If you have
                                          					 questions when on a Unified CCX Administration web page, from the menu bar,
                                          					 select the Help > For this
                                                						  page . |
| 4. Upload
                                          					 any prompts needed for the script. | For
                                          					 customized or language specific prompts | Unified CCX Prompt
                                             						Management web page From the
                                          					 Unified CCX Administration menu bar, select Applications > Prompt
                                                						  Management . Then in
                                          					 the Prompt Management page, click Upload New Prompts . | Uploading prompts section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 5. Add the
                                          					 application. | To perform
                                          					 a telephony task through Unified CCX, you need a Unified CCX application. Adding an
                                          					 application involves giving it a name, assigning it a script, and defining any
                                          					 application variables. An example
                                          					 application that comes with Unified IP IVR is the Cisco
                                             						Unified CM AutoAttendant . The script
                                          					 for the Cisco Unified CM AutoAttendant is aa.aef. | Unified CCX Application
                                             						Configuration web page From the Unified CCX Administration web page menu bar, select Applications > Application
                                                						  Management and then in the upper, right corner of the
                                          					 window, click the Add New Application link. Next,
                                          					 Under Application Type, select Cisco Script Application and click Next. | Configure a Cisco Script
                                             						Application section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 6. Give
                                          					 the application a name and assign the script to the application. | To make
                                          					 the application available for use. | Unified CCX Script
                                             						Application web page | Configure a Cisco Script
                                             						Application section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 7.
                                          					 Customize the application parameters. If you are
                                          					 using a Cisco supplied script, you might also want to customize the application
                                          					 prompts. For example, you can record and upload your own prompts as previously
                                          					 explained in this check list. | On the
                                          					 Application page, if there are variables, you can customize the application by
                                          					 the definitions (values) you give the variables. The variables are the
                                          					 parameters you specify on the application web page in the Unified CCX
                                          					 Administration tool. | Unified CCX Cisco Script
                                             						Application web page | Configure a Cisco Script
                                             						Application section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| 8. Add the
                                          					 Application Trigger. | Enable the
                                          					 application to respond to JTAPI calls and/or HTTP requests. When you
                                          					 configure JTAPI triggers, you need to specify the CTI Route Point attributes
                                          					 used by the trigger. For example, device pool, location, and voice mail
                                          					 profile. | Unified CCX Add Application Triggers web page | See the
                                          					 online help for that web page. Also see Add
                                             						Application Triggers section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
| Some
                                          					 Configuration Specifics From
                                                						  the Unified CCX Administration web page, select Applications > Application
                                                      								Management . In the Application Configuration web page, Click the name of your new
                                                						  application. In the Cisco Script Application web page for your new
                                                						  application, the Add New Trigger link. In the
                                                						  pop-up window, select the trigger type and click Next . Enter
                                                						  the trigger phone number or web address and the other configuration information
                                                						  that you need. |
| 9. Test
                                          					 the application. | Make sure
                                          					 the application works. Before the
                                          					 Unified IP IVR system can receive calls, the Unified CCX engine must be
                                          					 running. | From one
                                          					 of your phones, phone the number specified by the trigger. Or if you have an
                                          					 HTTP trigger, from your computer, email the specified web address. | Your
                                          					 application specific documentation. |