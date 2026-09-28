---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmesystm-html-bf777fc2c5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmesystm.html
retrieved_at: 2026-08-21T07:22:12.025858+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: System-Level Parameters

## Chapter: System-Level Parameters

# System-Level Parameters

## Prerequisites for System-Level Parameters

- To directly connect Cisco Unified IP phones that are running Session Initiation Protocol (SIP) in Cisco Unified CME, Cisco CME
                              3.4 or a later version must be installed on the router. For installation information, see Install and Upgrade Cisco Unified CME Software .

- Cisco Unified CME must be configured to work with your IP network. For configuration information, see Network Parameters .

## Information About Configuring System-Level Parameters

### Bulk Registration
                           	 Support for SIP Phones

Cisco Unified CME
                              		8.6 enhances the bulk registration feature for Cisco Unified SIP IP phones by
                              		optimizing the two main transactions involved in bulk registration process and
                              		minimizing the number of required messages to be sent to the phones. The bulk
                              		registration process involves the following two main transactions:

Register—Register transaction handles per line REGISTER messages
                                    			 coming to Cisco Unified CME and provisions phone DNs by creating dialpeers and
                                    			 various phone data structures.

Phone Status
                                    			 Update—Phone status update transaction sends back device information using
                                    			 REFER and NOTIFY messages.

In Cisco Unified CME
                              		8.6, the bulk registration process consists of only one REGISTER message per
                              		phone instead of one REGISTER message per phone per line, thus reducing any
                              		negative impact on your router’s performance. For information on configuring
                              		bulk registration, see Configure Bulk Registration for SIP IP Phones .

The show voice register
                                    			 pool command displays the registration method a phone uses: per
                              		line, bulk-in progress, or bulk-completed. The per line option indicates that
                              		the phone is using the per line registration process. The bulk-in progress
                              		option indicates that the phone is using the bulk registration process but the
                              		registration process is not complete yet. The bulk-completed option indicates
                              		that the phone is registered using the bulk registration process and the
                              		registration process is complete. For information on verifying the phone
                              		registration process, see Verify Phone Registration Type and Status .

In earlier versions
                              		of Cisco Unified CME, the registration process was very lengthy and several SIP
                              		messages were exchanged between the end points and Cisco Unified CME to
                              		properly provision the phone.

Table 1 lists the number of messages
                              		required to register an eight-button Cisco Unified SIP IP phone, where all of
                              		the eight buttons can be configurd as a shared line with message waiting
                              		indicator (MWI) notification enabled, to Cisco Unified CME.

Transactions

Method

Messages Per
                                          				  Transaction

Number of
                                          				  Transactions

Total number
                                          				  of messages (per line)

Total number
                                          				  of messages (bulk)

Register

REGISTER

2

8

24

3

Phone Status
                                          				  Update

REFER
                                          				  remotecc

NOTIFY (mwi,
                                          				  service-control)

2

2

3

8

6

16

2

Subscription

SUBSCRIBE
                                          				  (sharedline)

4

8

32

32

Total

78

37

You can see from the
                              		preceding table that more than 70 messages are required to register one
                              		8-button IP phone. If there is a simultaneous registration of more phones, the
                              		amount of messages can be overwhelming and can have a negative impact on the
                              		performance of the router.

With the enhanced
                              		bulk registration process, the two main transactions (Register and Phone Status
                              		Update) are optimized to minimize the number of messages required to complete
                              		the phone registration process. Table 1 shows that the total number
                              		of messages required for bulk registration is only 37.

#### Register Transaction

The following is an example of the REGISTER message:

```
REGISTER sip:28.18.88.1 SIP/2.0
```

```
Via: SIP/2.0/TCP 28.18.88.33:44332;branch=z9hG4bK53f227fc
```

```
From: <sip:6010@28.18.88.1>;tag=001b2a893698027db8ea0454-26b9fb0c
```

```
To: <sip:6010@28.18.88.1>
```

```
Call-ID: 001b2a89-3698011e-280209a4-567e339c@28.18.88.33
```

```
Max-Forwards: 70
```

```
Date: Wed, 03 Mar 2010 01:18:34 GMT
```

```
CSeq: 240 REGISTER
```

```
User-Agent: Cisco-CP7970G/8.4.0
```

```
Contact: <sip:6010@28.18.88.33:44332;transport=tcp > ;+sip.instance="<urn:uuid:00000000-0000-0000-0000-001b2a893698 >
 ";+u.sip!model.ccm.cisco.com="30006"
```

```
Supported: replaces,join,norefersub,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,
X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-3.0.0,X-cisco-xsi-7.0.1
```

```
Reason: SIP;cause=200;text="cisco-alarm:23 Name=SEP001B2A893698 Load=SIP70.8-4-2-30S Last=reset-restart"
```

```
Expires: 3600
```

```
Content-Type: multipart/mixed; boundary=uniqueBoundary
```

```
Mime-Version: 1.0
```

```
Content-Length: 982
```

```
--uniqueBoundary
```

```
Content-Type: application/x-cisco-remotecc-request+xml
```

```
Content-Disposition: session;handling=optional
```

```
>
```

```
< x-cisco-remotecc-request >
```

```
<bulkregisterreq >
```

```
< contact all="true" >
```

```
< register >  < /register >
```

```
< /contact >
```

```
< /bulkregisterreq >
```

```
< /x-cisco-remotecc-request >
```

```
--uniqueBoundary
```

```
Content-Type: application/x-cisco-remotecc-request+xml
```

```
Content-Disposition: session;handling=optional
```

```
>
```

```
< x-cisco-remotecc-request >
```

```
< optionsind >
```

```
< combine max="6" >
```

```
< remotecc >
```

```
< status >  < /status >
```

```
< /remotecc >
```

```
< service-control >  < /service-control >
```

```
< /combine >
```

```
< dialog usage="hook status" >
```

```
< unot >  < /unot >
```

```
< sub >  < /sub >
```

```
< /dialog >
```

```
< dialog usage="shared line" >
```

```
< unot >  < /unot >
```

```
< sub >  < /sub >
```

```
< /dialog >
```

```
< presence usage="blf speed dial" >
```

```
< unot >  < /unot >
```

```
< sub >  < /sub >
```

```
< /presence >
```

```
< joinreq >  < /joinreq >
```

```
< /optionsind >
```

```
< /x-cisco-remotecc-request >
```

```
--uniqueBoundary--
```

The following is an example of a response to the preceding REGISTER
                                    		  message:

```
SIP/2.0 200 OK
```

```
Date: Wed, 03 Mar 2010 01:18:41 GMT
```

```
From:  < sip:6010@28.18.88.1 > ;tag=001b2a893698027db8ea0454-26b9fb0c
```

```
Content-Length: 603
```

```
To:  < sip:6010@28.18.88.1 > ;tag=E2556C-6C1
```

```
Contact:  < sip:6010@28.18.88.33:44332;transport=tcp > ;expires=3600;x-cisco-newreg
```

```
Expires:  3600
```

```
Content-Type: multipart/mixed;boundary=uniqueBoundary
```

```
Call-ID: 001b2a89-3698011e-280209a4-567e339c@28.18.88.33
```

```
Via: SIP/2.0/TCP 28.18.88.33:44332;branch=z9hG4bK53f227fc
```

```
Server: Cisco-SIPGateway/IOS-12.x
```

```
CSeq: 240 REGISTER
```

```
Mime-Version: 1.0
```

```
>  < x-cisco-remotecc-response >  < response >  < code > 200 < /code >  < optionsind >  < combine max="6" >  < remotecc >
  < status/ >  < /remotecc >  < service-control/ >  < /combine >  < dialog usage="shared line" >  < sub/ >  < /dialog >  
< presence usage="blf speed dial" >  < sub/ >  < /presence >  < /optionsind >  < /response >  < /x-cisco-remotecc-response >
```

#### Phone Status Update Transaction

Cisco Unified IP phones use the option indication to negotiate supported options with Cisco Unified CME via remotecc request.
                                 Cisco Unified CME selects an option or options that it wishes to support and return it in the response. Cisco Unified CME
                                 ignores items (elements, attributes, and values) that it fails to understand. A new phone option, combine, is defined to optimize
                                 phone status update. This option combines remotecc status information (cfwdall, privacy, dnd, bulk mwi) and service-control.
                                 The following is an example of a combined status update:

```
<optionsind>
<combine max="5">
<remotecc><status/></remotecc>
<service-control/>
</combine>
</optionsind>
```

The following is another example of a combined status update:

```
<optionsind>
<combine max="4">
<remotecc><status/></remotecc>
<service-control/>
</combine>
</optionsind>
```

To minimize the data size, Cisco Unified CME and the phone agree ahead of time on a default value to apply updates. Therefore,
                                 during initial registration, Cisco Unified CME will not send the value if it matches the agreed upon default. Table 1 captures the existing status information and applicable default value.

Status

Default

Initialization

CallForwardAll Update

No default

Always send regardless of the value

Privacyrequest

Disabled

Only send if the value is not equal to the default

DnDupdate

Disabled

Only send if value is not equal to the default

Bulkupdate (MWI)

No default

Always send regardless of value

During bulk registration, Cisco Unified CME uses a single REFER message to send combined phone status update message for phone
                                 status updates such as cfwdallupdate, privacyrequet, DnDupdate, and Bulkupdate (MWI) instead of sending phone status in individual
                                 NOTIFY or REFER message to the phone. The following is an example of the single REFER message sent by Cisco Unified CME to
                                 the phone:

```
REFER sip:6010@28.18.88.33:44332 SIP/2.0
Content-Id: <1483336>
From: <sip:28.18.88.1>;tag=E256D4-2316
Timestamp: 1267579121
Content-Length: 934
User-Agent: Cisco-SIPGateway/IOS-12.x
Require: norefersub
Refer-To: cid:1483336
To: <sip:6010@28.18.88.33>
Contact: <sip:28.18.88.1:5060>
Referred-By: <sip:28.18.88.1>
Content-Type: multipart/mixed;boundary=uniqueBoundary
Call-ID: 89CBE590-259911DF-80589501-4E753388@28.18.88.1
Via: SIP/2.0/UDP 28.18.88.1:5060;branch=z9hG4bKA22639
CSeq: 101 REFER
Max-Forwards: 70
Mime-Version: 1.0
 
 --uniqueBoundary
 Content-Type: application/x-cisco-remotecc-request+xml
 
<x-cisco-remotecc-request>
<cfwdallupdate><fwdaddress></fwdaddress><tovoicemail>off</tovoicemail></cfwdallupdate></x-cisco-remotecc-request>
 

--uniqueBoundary
Content-Type: application/x-cisco-remotecc-request+xml

 

<x-cisco-remotecc-request>
<privacyreq><status>true</status></privacyreq>
</x-cisco-remotecc-request>
--uniqueBoundary
Content-Type: application/x-cisco-remotecc-request+xml
 

<x-cisco-remotecc-request>
<bulkupdate>
<contact all="true"><mwi>no</mwi></contact>
<contact line=" 1"><mwi>yes</mwi></contact>
<contact line=" 3"><mwi>yes</mwi></contact>
</bulkupdate>
</x-cisco-remotecc-request>
 

--uniqueBoundary
Content-Type: text/plain
action=check-version
RegisterCallId={001b2a89-3698011e-280209a4-567e339c@28.18.88.33}
ConfigVersionStamp={0106514225374329}
DialplanVersionStamp={}
SoftkeyVersionStamp={0106514225374329} 

--uniqueBoundary--
```

### DSCP

Differentiated Services Code Point (DSCP) packet marking is used to
                              		specify the class of service for each packet. Cisco Unified IP Phones get their
                              		DSCP information from the configuration file that is downloaded to the device.

In earlier versions of Cisco Unified CME, the DSCP value is predefined.
                              		In Cisco Unified CME 7.1 and later versions, you can configure the DSCP value
                              		for different types of network traffic. Cisco Unified CME downloads the
                              		configured DSCP value to SCCP and SIP phones in their configuration files and
                              		all control messages and flow-through RTP streams are marked with the
                              		configured DSCP value. This allows you to set different DSCP values, for
                              		example, for video streams and audio streams.

For configuration information, see Set Up Cisco Unified CME for SCCP Phones or Set Up Cisco Unified CME for SIP Phones .

### Maximum Ephones in Cisco Unified CME 4.3 and Later Versions

In Cisco Unified CME 4.3 and later versions, the max-ephones command is enhanced to set the maximum number of SCCP
                              		phones that can register to Cisco Unified CME, without limiting the number that
                              		can be configured. In previous versions of Cisco Unified CME, the max-ephones command defined the maximum number
                              		of phones that could be both configured and registered.

This enhancement expands the maximum number of phones that can be
                              		configured to 1000. The maximum number of phones that can register to
                              		Cisco Unified CME has not changed; it is dependent on the number of phones
                              		supported by the hardware platform and is limited by the max-ephones command.

This enhancement supports features, such as Extension Assigner, that
                              		require you to configure more phones than can register. For example, if you set
                              		the max-ephones command to 50 and configure 100 ephones, only 50 phones
                              		can register to Cisco Unified CME, one at a time in random order. The remaining
                              		50 phones cannot register and an error message displays for each rejected
                              		phone. This enhancement also allows you to assign ephone tags that match the
                              		extension number of the phone, for extensions up to 1000.

If you reduce the value of the max-ephones command, currently registered phones are not forced to
                              		unregister until a reboot. If the number of registered phones, however, is
                              		already equal to or more than the max-ephones value, no additional phones can
                              		register to Cisco Unified CME. If you increase the value of the max-ephones command, the previously rejected ephones are able to
                              		register immediately until the new limit is reached.

### Network Time Protocol for SIP Phones

Although SIP phones can synchronize to a Cisco Unified CME router, the router can lose its clock after a reboot causing phones
                              to display the wrong time. SIP phones registered to a Cisco Unified CME router can synchronize to a Network Time Protocol
                              (NTP) server. Synchronizing to an NTP server ensures that SIP phones maintain the correct time. For configuration information,
                              see Set Network Time Protocol for SIP Phones .

### Per-Phone
                           	 Configuration Files

In Cisco Unified CME
                              		4.0 and later versions, you can use an external TFTP server to off load the
                              		TFTP server function on the Cisco Unified CME router. Using flash memory or
                              		slot 0 memory on the Cisco Unified CME router allows you to use different
                              		configuration files for each phone type or for each phone, permitting you to
                              		specify different user locales and network locales for different phones. Before
                              		Cisco Unified CME 4.0, you could specify only a single default user and network
                              		locale for a Cisco Unified CME system.

You can specify one
                              		of the following four locations to store configuration files:

- System—This is the default.
                                 		  When system:/its is the storage location, there is only one default
                                 		  configuration file for all phones in the system. All phones, therefore, use the
                                 		  same user locale and network locale. User-defined locales are not supported.

- Flash or slot 0—When flash
                                 		  memory or slot 0 memory on the router is the storage location, you can create
                                 		  additional configuration files to apply per phone type or per individual phone.
                                 		  Up to five user and network locales can be used in these configuration files.

- TFTP—When an external TFTP server is
                                 		  the storage location, you can create additional configuration files that can be
                                 		  applied per phone type or per individual phone. Up to five user and network
                                 		  locales can be used in these configuration files.

You can then specify
                              		one of the following ways to create configuration files:

- Per system—This is the default. All
                                 		  phones use a single configuration file. The default user and network locale in
                                 		  a single configuration file are applied to all phones in the Cisco Unified CME
                                 		  system. Multiple locales and user-defined locales are not supported.

- Per phone
                                 		  type—This setting creates separate configuration files for each phone type. For
                                 		  example, all Cisco Unified IP Phone 7960s use XMLDefault7960.cnf.xml, and all
                                 		  Cisco Unified IP Phone 7905s use XMLDefault7905.cnf.xml. All phones of the same
                                 		  type use the same configuration file, which is generated using the default user
                                 		  and network locale. This option is not supported if you store the configuration
                                 		  files in the system:/its location.

- Per phone—This
                                 		  setting creates a separate configuration file for each phone by MAC address.
                                 		  For example, a Cisco Unified IP Phone 7960 with the MAC address 123.456.789
                                 		  creates the per-phone configuration file SEP123456789.cnf.xml. The
                                 		  configuration file for a phone is generated with the default user and network
                                 		  locale unless a different user and network locale is applied to the phone using
                                 		  an ephone template. This option is not supported if you store the configuration
                                 		  files in the system:/its location.

For configuration
                              		information, see Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

#### HFS Download Support for IP Phone Firmware and Configuration
                              	 Files

Legacy IP phones access the TFTP server to download firmware and
                                 		configuration files but Cisco Unified CME 8.8 enhances download support for SIP
                                 		phone firmware, scripts, midlets, and configuration files using the HTTP
                                 		File-Fetch Server (HFS) infrastructure.

In Cisco Unified CME 8.8 and later versions, SIP phones use an HTTP
                                 		server as the primary download service when it is configured and access a TFTP
                                 		server as a secondary or fallback option when the HTTP server fails.

The following scenario shows a successful download sequence using an
                                 		HTTP server:

An IP phone initiates TCP connection to port 6970. A connection is
                                 		established and an internal request for a file is sent to the HTTP server. The
                                 		phone receives the HTTP response status code of 200, signifying that the
                                 		download is successful.

The following scenario shows a download sequence that begins with an IP
                                 		phone using an HTTP server to download files and ends with a TFTP server as a
                                 		fallback option when the initial download attempt fails:

An IP phone initiates TCP connection to port 6970 but is unable to
                                 		establish a connection. The phone contacts the TFTP server and sends an
                                 		internal request for a file. The file is successfully downloaded from the TFTP
                                 		server.

The following scenario shows how a download sequence that starts with an
                                 		HTTP server does not always fall back to the TFTP server when the initial
                                 		download attempt fails:

An IP phone initiates TCP connection to port 6970. A connection is
                                 		established and an internal request for a file is sent to the HTTP server. The
                                 		phone receives the HTTP response status code of 404, signifying that the file
                                 		requested could not be found. Because the file cannot be found, the request is
                                 		not sent to the TFTP server.

For more information on Phone Firmware Files, see Install and Upgrade Cisco Unified CME Software .

For more information on Per-Phone Configuration Files, see Per-Phone Configuration Files .

For more information on Configuration Files for Phones in Cisco Unified CME, see Generate Configuration Files for Phones .

##### Enable HFS
                                 	 Service

To enable the HFS
                                    		download service, the underlying HTTP server must be enabled first because the
                                    		HFS infrastructure is built on top of an existing IOS HTTP server.

```
Router(config)# ip http server
```

This HFS
                                    		infrastructure enables multiple HTTP services to co-exist. The HFS download
                                    		service runs on custom port 6970 but can also share default port 80 with other
                                    		services. Other HTTP services run on other non-standard ports like 1234.

```
Router(config)# ip http server Router(config)# ip http port 1234
```

The HFS download
                                    		service starts when the following is configured in telephony-service
                                    		configuration mode.

For the default
                                    		port:

```
Router(config-telephony)# hfs enable
```

For the custom port:

```
Router(config-telephony)# hfs enable port 6970
```

In the following
                                    		example, port 6970 is configured as the IP HTTP port. When the HFS port is
                                    		configured with the same value, an error message is displayed to show that the
                                    		port is already in use.

```
Router (config)# ip http port 6970 . . Router (config)# telephony-service Router (config-telephony)# hfs enable port 6970
```

Error Message Invalid port number or port in use by other application

Explanation The HFS port number is already in use by the underlying IP HTTP
                                    		server.

Recommended Action Use an HFS port that is different from the underlying IP HTTP port.

For configuration
                                    		information, see Enable HFS Download Service for SIP Phones .

##### File Binding and Fetching

File binding and fetching using the HTTP server can be classified into
                                    		two:

Explicit binding – The create profile command triggers the system to generate the configuration and firmware files and store them in RAM or a flash memory. The
                                          system asks the new internal application programming interfaces (APIs) implemented by the HFS download service to bind the
                                          filename and alias that an IP phone wants to access to their corresponding URL.

Loose binding – The HFS download service enables the Cisco Unified CME system to configure a home path from where any requested
                                          firmware file that has no explicit binding can be searched and fetched. The files can be stored on any device (such as flash
                                          memory or NVRAM) under a root directory or a suitable subdirectory.

No matter how the system is configured, if there is no explicit binding, the files will go to the home path.

An advantage of the HFS service over the TFTP service is that only the absolute path where the firmware files are located
                                          needs to be configured in telephony-service configuration mode.

For example:

```
Router(config-telephony)# hfs home-path flash:/cme/loads/
```

In contrast, the TFTP service requires that each file be explicitly bound to its URL using the following tftp-server command:

```
tftp-server flash: SCCP70.8-3-3-14S.loads
```

The method is inefficient because this step must be repeated for each file that needs to be fetched using the TFTP server.

For information on verifying HFS file bindings, see Example for Verifying the HFS File Bindings of Cisco Unified SIP IP Phone Configuration and Firmware Files .

For information on how to configure the home path, see Configure HFS Home Path for SIP Phone Firmware Files .

##### Locale Installer

Installing and configuring locale files in Cisco Unified CME when using
                                    		an HTTP server is the same as when using a TFTP server.

For configuration information, see Use the Locale Installer in Cisco Unified CME 7.0(1) and Later Versions .

##### Security Recommendations

Like any access interface, the HFS download service can open router
                                    		files that should only be accessed by authorized persons. Security issues are
                                    		made more severe by the fact that the HFS download service is HTTP based,
                                    		enabling anyone with a simple web browser to access sensitive files, such as
                                    		configuration or image files, by entering a random string of words.

However, the HFS security problem is restricted to the loose binding
                                    		operation, where the administrator provides an HFS home path in which the phone
                                    		firmware and other related files are stored.

In the case where a unique directory path (where only the phone firmware
                                    		files are stored) is used as the HFS home path

```
(config-telephony)# hfs home-path flash:/cme/loads/
```

only those files that are in flash:/cme/loads/ can be accessed.

But when it is the root directory path that is used as the HFS home path

```
(config-telephony)# hfs home-path flash:/
```

there is a risk of making configuration files and system images, which
                                    		are stored in the root directory shared with the phone firmware files,
                                    		accessible to unauthorized persons.

The following are two recommendations on how to make firmware files
                                    		inaccessible to unauthorized persons:

Create a unique directory, which is not shared by any other application or used for any other purpose, fpr IP phone firmware
                                          files. Using a root directory as the HFS home path is not recommended.

Use the ip http access-class command to specify the access list that should be used to restrict access to the HTTP server. Before the HTTP server accepts
                                          a connection, it checks the access list. If the check fails, the HTTP server does not accept the request for a connection.

### Redundant Cisco
                           	 Unified CME Router for SCCP Phones

A second
                              		Cisco Unified CME router can be configured to provide call-control services if
                              		the primary Cisco Unified CME router fails. The secondary Cisco Unified CME
                              		router provides uninterrupted services until the primary router becomes
                              		operational again.

When a phone
                              		registers to the primary router, it receives a configuration file from the
                              		primary router. Along with other information, the configuration file contains
                              		the IP addresses of the primary and secondary Cisco Unified CME routers. The
                              		phone uses these addresses to initiate a keepalive (KA) message to each router.
                              		The phone sends a KA message after every KA interval (30 seconds by default) to
                              		the router with which it is registered and after every two KA intervals (60
                              		seconds by default) to the other router. The KA interval can be adjusted.

If the primary
                              		router fails, a phone will not receive an acknowledgment (ACK) to its KA
                              		message to the primary router. If the phone does not get an ACK from the
                              		primary router for three consecutive KAs, it registers with the secondary
                              		Cisco Unified CME router.

During the time that
                              		the phone is registered to the secondary router, it keeps sending a KA probe to
                              		the primary router to see if it has come back up, now every 60 seconds by
                              		default or two times the normal KA interval. After the primary
                              		Cisco Unified CME router returns to normal operation, the phone starts
                              		receiving ACKs for its probes. After the phone receives ACKs from the primary
                              		router for three consecutive probes, it switches back to the primary router and
                              		re-registers with it. The re-registration of phones with the primary router is
                              		also called rehoming.

The physical setup
                              		for redundant Cisco Unified CME routers is as follows. The FXO line from the
                              		PSTN is split using a splitter. From the splitter, one line goes to the primary
                              		Cisco Unified CME router and the other line goes to the secondary
                              		Cisco Unified CME router. When a call comes in on the FXO line, it is presented
                              		to both the primary and secondary Cisco Unified CME routers. The primary router
                              		is configured by default to answer the call immediately. The secondary
                              		Cisco Unified CME router is configured to answer the call after three rings. If
                              		the primary router is operational, it answers the call immediately and changes
                              		the call state so that the secondary router does not try to answer it. If the
                              		primary router is unavailable and does not answer the call, the secondary
                              		router sees the new call coming in and answers after three rings.

The secondary
                              		Cisco Unified CME router should be connected in some way on the LAN, either
                              		through the same switch or through another switch that may or may not be
                              		connected to the primary Cisco Unified CME router directly. As long as both
                              		routers and the phones are connected on the LAN with the appropriate
                              		configurations in place, the phones can register to whichever router is active.

Configure primary
                              		and secondary Cisco Unified CME routers identically, with the exception that
                              		the FXO voice port from the PSTN on the secondary router should be configured
                              		to answer after more rings than the primary router, as previously explained.
                              		The same command is used on both routers to specify the IP addresses of the
                              		primary and secondary routers.

For configuration
                              		information, see Configure Redundant Router for SCCP Phones .

Restriction

- Due to lack of High
                                             			 Availability support, Stateful Swtichover or preservation of active calls is
                                             			 not supported in the redundancy feature offered by Unified CME.

The physical setup for redundant Cisco Unified CME routers only
                                                				support Loop start signaling. The Ground start signaling is not supported.

### Redundant Cisco
                           	 Unified CME Router for SIP Phones

A secondary Cisco
                              		Unified CME router can be configured to provide call-control services if the
                              		primary Cisco Unified CME router fails. The secondary Cisco Unified CME router
                              		provides uninterrupted services until the primary router becomes operational
                              		again.

When a SIP phone
                              		registers to the primary router, it receives a configuration file from the
                              		primary router. Along with other information, the configuration file contains
                              		the IP addresses of the primary and secondary Cisco Unified CME routers. The
                              		phone uses these addresses to initiate a keepalive (KA) message to the
                              		secondary CME router. The phone sends a REGISTER message to the primary router
                              		for registration and a keepalive REGISTER message with Expires=0, to the
                              		secondary router during the keepalive interval (every 120 seconds by default).
                              		The keepalive interval can be configured (Range is 120 to 65535).

If primary router
                              		fails, a SIP phone (on registration refresh) will not receive a successful
                              		response for its REGISTER message. On unsuccessful response from primary
                              		router, phone registers with the secondary router. When the phone is registered
                              		to the secondary router, phone sends keepalive REGISTER (Expires=0) messages to
                              		the primary router.

After the primary
                              		Cisco Unified CME router returns to normal operation, the phone sends a
                              		"token-registration" to the primary router seeking permission to move
                              		registration of the phone from the standby secondary router to the primary
                              		router. To obtain a token, the SIP phones sends a Out-of-Dialog REFER message
                              		to the primary router for registration. The primary router accepts the token by
                              		responding with a 202 Accepted response. When the SIP phones receive the token
                              		(202 Accepted response) from the primary router, the phones will immediately
                              		de-register from the secondary router by sending a REGISTER message with
                              		Expires=0 for each line and registers back to the primary router. The
                              		re-registration of phones with the primary router is called rehoming.

No signaling or
                              		media preservation is done for any active calls on Unified CME. Hence during
                              		failover on primary CME, calls would remain in active state. But media would
                              		not be present for those calls. The SIP phones will not register to the
                              		secondary router until the active call is disconnected.

The secondary Cisco
                              		Unified CME router is connected directly to the same SIP trunk as the primary
                              		Cisco Unified CME router. As long as both routers and the phones are connected
                              		on the LAN with the appropriate configurations in place, the phones can
                              		register to whichever router is active. You should configure the primary and
                              		secondary Cisco Unified CME routers identically. The same command is used on
                              		both routers to specify the IP addresses of the primary and secondary routers.

For configuration
                              		information, see Configure Redundant Router for SIP Phones .

Restriction

Due to lack of High Availability support, Stateful Swtichover or preservation of active calls is not supported in the redundancy
                                                feature offered by Unified CME.

### Timeouts

The following system-level timeout parameters have default values that
                              		are generally adequate:

- Busy Timeout—Length of time
                                 		  that can elapse after a transferred call reaches a busy signal before the call
                                 		  is disconnected.

- Interdigit Timeout—Length of time that can elapse between the receipt of individual dialed digits before the dialing process
                                 times out and is terminated. If the timeout ends before the destination is identified, a tone sounds and the call ends. This
                                 value is important when using variable-length dial-peer destination patterns (dial plans).

- Ringing Timeout—Length of time a phone can ring with no answer before
                                 		  returning a disconnect code to the caller. This timeout is used only for
                                 		  extensions that do not have no-answer call forwarding enabled. The ringing
                                 		  timeout prevents hung calls received over interfaces, such as FXO, that do not
                                 		  have forward-disconnect supervision.

- Keepalive—Interval determines how often a message is sent between the
                                 		  router and Cisco Unified IP phones, over the session, to ensure that the
                                 		  keepalive timeout is not exceeded. If no other traffic is sent over the session
                                 		  during the interval, a keepalive message is sent.

For configuration information, see Modify Defaults for Timeouts for SCCP Phones .

### IPv6 Support for Cisco Unified CME SCCP Endpoints

Internet Protocol version 6 (IPv6), which is the latest version of the Internet Protocol (IP) that uses packets to exchange
                              data, voice, and video traffic over digital networks, increases the number of network address bits from 32 bits in IPv4 to
                              128 bits. IPv6 support in Cisco Unified CME allows the network to behave transparently in a dual-stack (IPv4 and IPv6) environment
                              and provides additional IP address space to SCCP phones and devices that are connected to the network. For information on
                              configuring DHCP for IPv6, see Network Parameters .

Before Cisco Unified CME 8.0, SCCP supported IPv4 addresses (4 bytes)
                              		only. With Cisco Unified CME 8.0, the SCCP version is upgraded to store IPv6
                              		address (16 bytes) also.

The following SCCP phones and devices are supported on IPv6: 7911, 7931, 7941G, 7941GE, 7961G, 7961GE, 7970G, 7971G, 7971G-GE,
                              7942, 7962, 7945, 7965, 7975, SCCP analogue gateway, Xcoder, and Hardware Conference devices. For more information on configuring
                              SCCP IP phones for IPv6 source address, see Configure IPv6 Source Address for SCCP IP Phones .

### Support for
                           	 IPv4-IPv6 (Dual-Stack)

Cisco Unified CME
                              		8.0 can interact with and support any SCCP devices that support IPv4 only or
                              		both IPv4 and IPv6 (dual-stack). In dual-stack mode, two IP addresses are
                              		assigned to an interface, one is an IPv4 address and the other is an IPv6
                              		address. Both IPv4 and IPv6 stacks are enabled on the voice gateways so that
                              		applications can interact with both versions of IP addresses. To support
                              		devices that use IPv4 only, IPv6 only, or both IPv4 and IPv6 (dual-stack)
                              		addresses, you must ensure that the Cisco Unified CME has both IPv4 address and
                              		IPv6 address enabled. For more information, see Configure IP Phones in IPv4, IPv6, or Dual Stack Mode .

### Media Flow Through and Flow Around

Media transport modes, such as flow around and flow through, are used to
                              		transport media packets across endpoints. Media flow around enables media
                              		packets to pass directly between the endpoints, without the intervention of the
                              		IP-IP Gateway (IPIPGW). Media flow through enables media packets to pass
                              		through the endpoints, without the intervention of the IPIPGW.

Table 1 lists media flow-through and flow-around scenarios between endpoints that support IPv4, IPv6, and dual- stack. When both
                              endpoints are IPv4 only or IPv6 only, the call flows around. When one endpoint is IPv4 and the other is IPv6, calls flow through.
                              When one endpoint is dual-stack and the other IPv4 or IPv6 the calls flow around. When both endpoints are dual-stack calls
                              flow around or follows the preference (preferred IP address version) selected by protocol mode in dual-stack.

IP Versions

IPv4 Only

IPv6 Only

Dual-Stack

IPv4 Only

Flow Around 1

Flow Through

Flow Around

IPv6 Only

Flow Through

Flow Around

Flow Around/IPv6

Dual-Stack

Flow Around/IPv4

Flow Around/IPv6

Flow Around/Preference

### Media Flow Around
                           	 Support for SIP-SIP Trunk Calls

Cisco Unified CME
                              		8.5 and later versions support the media flow around functionality for SIP to
                              		SIP trunk calls on Cisco Unified CME, allowing less consumption of resources on
                              		Cisco Unified CME.

The media flow
                              		around feature eliminates the need to terminate RTP and re-originate on
                              		Cisco Unified CME. This reduces media switching latency and increases the call
                              		handling capacity for a Cisco Unified CME SIP trunk.

Media flow around is
                              		supported in the following scenarios:

Single Number
                                    			 Reach (SNR) Push—If an SNR call on a SIP trunk is pushed over to a mobile user
                                    			 over another SIP trunk, the resulting connection is a SIP-SIP trunk call
                                    			 connection. If both SIP trunks are configured for media flow around, the media
                                    			 is allowed to flow around Cisco Unified CME for the resulting call.

Call Forward—If
                                    			 a SIP trunk call is forwarded over another SIP trunk and both the SIP trunks
                                    			 are configured for media flow around, media flows around Cisco Unified CME for
                                    			 the resulting SIP-SIP trunk call. Media flow around is supported for all types
                                    			 of call forwarding, such as call forward night-service, call forward all, call
                                    			 forward busy, and call forward no-answer.

Call Transfer—If
                                    			 a SIP trunk call is transferred over another SIP trunk and both SIP trunks are
                                    			 configured for media flow around, media flows around Cisco Unified CME for the
                                    			 resulting SIP-SIP trunk call. Media flow around is supported on both
                                    			 SIP-line-initiated call transfer and SCCP-line-initiated call transfers. It is
                                    			 supported for all types of call transfers, such as blind transfer, consult
                                    			 transfer, and full consult transfer.

Media is forced to
                              		flow through on different types of call flows including the SIP to SIP trunk
                              		call with asymmetric flow mode configurations or symmetric flow through
                              		configuration. In asymmetric flow mode configurations, one SIP leg is
                              		configured in the media flow around mode and another SIP leg is configured in
                              		the media flow through mode. In such cases, media is forced to flow through
                              		Cisco Unified CME.

Media is forced to
                              		flow through Cisco Unified CME for the following types of call flows:

Any calls
                                    			 involving a SIP endpoint, a SCCP endpoint, PSTN trunks (BRI/PRI/FXO), or FXO
                                    			 circuits.

SIP to SIP trunk
                                    			 call with either asymmetric flow mode configurations or symmetric flow through
                                    			 configurations.

SIP to SIP trunk
                                    			 call that requires transcoding services on Cisco Unified CME.

SIP to SIP trunk
                                    			 calls that require DTMF interworking with RFC2833 on one side, and SIP-Notify
                                    			 on the other side.

SNR pullback to
                                    			 SCCP— When an SNR call is pulled back from a mobile phone to the local SCCP SNR
                                    			 extension, the call is connected to the SCCP SNR extension. Media is required
                                    			 to flow through Cisco Unified CME because one of the calls is from a SCCP SNR
                                    			 extension, which is local to Cisco Unified CME.

In Cisco Unified CME
                              		8.5, the media flow around feature is turned on or turned off using the media command
                              		in voice service voip, dial-peer voip, and voice class media configuration
                              		modes. The configuration specified under voice class media configuration mode
                              		takes precedence over the configuration in dial-peer configuration mode. If the
                              		media configuration is not specified under voice class media or dial-peer
                              		configuration mode, then the global configuration specified under voice service
                              		voip takes precedence. For more information, see Enable Media Flow Mode on SIP Trunks .

### Overlap Dialing Support for SIP and SCCP IP Phones

Cisco Unified CME 8.5 and later versions support overlap dialing on SCCP
                              		and SIP IP phones such as 7942, 7945, 7962, 7965, 7970, 7971, and 7975.

In earlier versions of Cisco Unified CME, overlap dialing was not
                              		supported over PRI/BRI trunks for calls originating from SCCP or SIP IP phones.
                              		Dialing was always converted into enbloc dialing based on the dial-peer
                              		configuration and the dial-peer mapping application. Once dialpeer matching
                              		took place, no further dialing was possible and no overlap digit were sent over
                              		ISDN trunk, even though overlap dialing was supported over ISDN trunks.

SCCP IP phones currently support overlap dialing, but digits are
                              		converted to enbloc digits when it reaches Cisco Unified CME. Overlap dialing
                              		is supported on SIP IP phones using the KeyPad Markup Language (KPML) method.

With overlap dialing support, the dialed digits from the SIP or SCCP IP
                              		phones are passed across to the PRI/BRI trunks as overlap digits and not as
                              		enbloc digits, enabling overlap dialing on the PRI/BRI trunks as well.

For information on how to configure SCCP and SIP IP phones for overlap dialing, see Configure Overlap Dialing on SCCP IP Phones and Configure Overlap Dialing on SIP Phones .

### Unsolicited Notify
                           	 for Shared Line and Presence Events for Cisco Unified SIP IP Phones

Before Cisco Unified
                              		CME 9.0, a Cisco Unified SIP IP phone receives NOTIFY messages that convey
                              		shared line and presence events from the Cisco Unified CME only by subscribing
                              		to such events. To subscribe, the IP phone sends a SUBSCRIBE message to the
                              		Cisco Unified CME with the type of event for which it wants to be notified. The
                              		Cisco Unified CME sends a NOTIFY message to alert the subscribed IP phone or
                              		subscriber of event updates.

In Unsolicited
                              		Notify, the Cisco Unified CME acquires the required information from the router
                              		configuration to create the implicit subscription and adds subscribers without
                              		a subscription request from Cisco Unified SIP IP phones. The Cisco Unified CME
                              		sends out NOTIFY messages to the IP phones for shared line or presence updates.

In Cisco Unified CME
                              		9.0 and later versions, the Unsolicited Notify mechanism reduces network
                              		traffic particularly during Cisco Unified SIP IP phone registration using the
                              		bulk registration method. Through this registration method, the preferred
                              		notification method of the IP phone is embedded in the registration message.

The Unsolicited
                              		Notify mechanism supports backward compatibility with all existing Cisco
                              		Unified SIP IP phone features. This mechanism is also the defacto notify
                              		mechanism in newer IP phone and Cisco Unified CME features, such as SNR
                              		Mobility.

From the end-user
                              		perspective, the following are the only two discernible differences between the
                              		SUBSCRIBE/NOTIFY and the Unsolicited Notify mechanisms:

- show presence
                                    			 subscription and show
                                    			 shared-line commands display different subscription IDs for each mechanism.

- With the SUBSCRIBE/NOTIFY
                                 		  mechanism, a Cisco Unified SIP IP phone needs to refresh the Cisco Unified CME
                                 		  subscription. In Unsolicited Notify mode, the subscription is permanent and
                                 		  does not need a refresh as long as the IP phone remains registered.

Restriction

- Because Unsolicited Notify
                                             			 is negotiated during bulk registration, the mechanism is not available on Cisco
                                             			 Unified SIP IP phones that do not have bulk registration turned on or have
                                             			 firmware that do not support bulk registration.

- Cisco Unified CME cannot
                                             			 disable the Unsolicited Notify mechanism. The system complies with and cannot
                                             			 override the requests of Cisco Unified SIP IP phones.

- In the absence of Cisco Unified SIP IP
                                             			 phone subscription information to distinguish if a notification event is for
                                             			 line or device monitoring, local device monitoring is not supported in the
                                             			 Unsolicited Notify mode.

### Interface Support
                           	 for Unified CME and Unified SRST

Unified CME and
                              		Unified SRST routers have multiple interfaces that are used for signaling and
                              		data packet transfers. The two types of interfaces available on a Cisco router
                              		include the physical interface and the virtual interface. The types of physical
                              		interfaces available on a router depends on its interface processors or port
                              		adapters. Virtual interfaces are software-based interfaces that you create in
                              		the memory of the networking device using Cisco IOS commands. When you need to
                              		configure a virtual interface for connectivity, you can use the Loopback
                              		Interface for Unified CME and Unified SRST.

The following
                              		interfaces are supported on Unified CME and Unified SRST:

Gigabit Ethernet
                                    			 Interface (IEEE 802.3z) ( interface
                                          				  gigabitethernet )

Loopback
                                    			 Interface ( interface
                                          				  loopback )

Fast Ethernet
                                    			 Interface ( interface
                                          				  fastethernet )

The remaining Cisco
                              		IOS interfaces are not validated on Unified CME and Unified SRST. Hence,
                              		Unified CME and Unified SRST do not claim support for these interfaces. For
                              		more information on the Cisco IOS Interface commands, see Cisco IOS Interface and
                                 		  Hardware Component Command Reference .

For physical
                              		interfaces such as interface
                                    			 gigabitethernet and interface
                                    			 fastethernet , subinterfaces are supported. In a subinterface,
                              		virtual interfaces are created by dividing a physical interface into multiple
                              		logical interfaces. For Cisco routers, a subinterface uses the parent physical
                              		interface for sending and receiving data. Virtual interfaces (For example, interface
                                    			 loopback ) do not support subinterfaces.

A subinterface for interface
                                    			 gigabitethernet is configured as follows:

```
Router(config)#interface gigabitEthernet 0/0.1
Router(config-subif)#exit
Router(config)#exit
```

## Configure System-Level Parameters

### Configure IP Phones in IPv4, IPv6, or Dual Stack Mode

Restriction

Legacy IP phones are not supported.

Multicast MOH and multicast paging features are not supported on IPv6 only phones. If you want to receive paging calls on
                                                   IPv6 enabled phones, use the default multicast paging.

Primary and secondary CME need to be provisioned with the same network type.

MWI relay server must be in IPv4 network.

Presence server must be IPv4 only.

Video endpoints, such as CUVA and 7985, are not supported in IPv6

TAPI client is not supported in IPv6.

All HTTP based IPv6 services are not supported.

IOS TFTP server is not supported in IPv6.

If protocol mode is IPv4, you can only configure IPv4 as the source IP-address, if protocol mode is IPv6 you can only configure
                                                   IPv6 as the source IP address and if the protocol mode is dual-stack, you can configure both IPv4 and IPv6 source addresses.

#### Before you begin

Cisco Unified CME 8.0 or later version.

IPv6 CEF must be enabled for dual-stack configuration.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 }]}

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 }]}

#### Example:

```
Router(config-telephony)# protocol mode dual-stack preference ipv6
```

Allows SCCP phones to interact with phones on IPv6 voice gateways.
                                             				You can configure phones for IPv4 addresses, IPv6 address es, or for a
                                             				dual-stack mode

ipv4 —Allows you to set the protocol mode as an IPv4 address.

ipv6 —Allows you to set the protocol mode as an IPv6 address.

dual-stack— Allows you to set the protocol mode for both IPv4 and IPv6 addresses.

preference —Allows you to choose a preferred IP address family if protocol mode is dual-stack.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to privileged EXEC mode.

#### Example

```
telephony-service
protocol mode dual-stack preference ipv6
....
ip source-address 10.10.2.1 port 2000
ip source-address 2000:A0A:201:0:F:35FF:FF2C:697D
```

### Configure IPv6
                           	 Source Address for SCCP IP Phones

Restriction

- IPv6 option only appears if
                                                				protocol mode is in dual-stack or IPv6.

- Do not change the default
                                                				port number (2000) in the ip
                                                   				  source-address configuration command. If you change the port number, IPv6
                                                				CEF packet switching engine may not be able to handle the IPv6 SCCP phones and
                                                				various packet handling problems may occur.

#### Before you begin

Cisco Unified CME 8.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- ip
                                       				  source-address { ipv4 address | ipv6
                                       				  address } port port [ secondary { ipv4 address | ipv6
                                       				  address } [ rehome seconds ]]
                                 			 [ strict-match ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters the
                                             				telephony-service configuration mode.

Step 4

ip
                                                				  source-address { ipv4 address | ipv6
                                                				  address } port port [ secondary { ipv4 address | ipv6
                                                				  address } [ rehome seconds ]]
                                          			 [ strict-match ]

#### Example:

```
Router(config-telephony)# ip source-address 10.10.10.33 port 2000 ip source-address 2001:10:10:10::
```

Allows to
                                             				configure an IPv4 or IPv6 address as an IP source-address for phones to
                                             				communicate with a Cisco Unified CME router.

- ipv4 address —Allows phones to communicate with
                                                				  phones or voice gateways in an IPv4 network. ipv4 address can only be configured with an IPv4 address or a dual-stack mode.

- ipv6 address —Allows phones to communicate with
                                                				  phones or voice gateways in an IPv6 network. ipv6 address can only be configured with an IPv6 address or a dual-stack mode.

- (Optional) port port —TCP/IP
                                                				  port number to use for SCCP. Range is from 2000 to 9999. Default is 2000. For
                                                				  dual-stack, port is only configured with an IPv4 address.

- (Optional) secondary —Cisco Unified CME router with which
                                                				  phones can register if the primary Cisco Unified CME router fails.

- (Optional) rehome seconds —Used
                                                				  only by Cisco Unified IP phones that have registered with a Cisco Unified
                                                				  Survivable Remote Site Telephony (SRST) router. This keyword defines a delay
                                                				  that is used by phones to verify the stability of their primary SCCP controller
                                                				  (Cisco Unified Communication Manager or Cisco Unified CME) before the phones
                                                				  re-register with it. This parameter is ignored by phones unless they are
                                                				  registered to a secondary Cisco Unified SRST router. The range is from 0 to
                                                				  65535 seconds. The default is 120 seconds.

The use of
                                             				this parameter is a phone behavior and is subject to change, based on the phone
                                             				type and phone firmware version.

- (Optional) strict-match —
                                                				  Requires strict IP address checking for registration.

Step 5

end

#### Example:

```
outer(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify IPv6 and Dual-Stack Configuration

Step 1

The following example shows a list of success messages that are printed during Cisco IOS boot up. These messages confirm whether
                                          IPv6 has been enabled on interfaces (for example, EDSP0.1 to EDSP0.5) specific to exchanging RTP packets with SCCP endpoints.

#### Example:

```
Router#
00:00:33: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.1 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.2 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.3 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.4 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.5 added.
00:00:34: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to down
00:00:34: %LINK-3-UPDOWN: Interface ephone_dsp DN 1.1, changed state to up
00:00:34: %LINK-3-UPDOWN: Interface ephone_dsp DN 1.2, changed state to up 
.
```

Step 2

Use the show ephone socket command to verify if IPv4 only, IPv6 only, or dual-stack (IPv4/IPv6) is configured in Cisco Unified CME. In the following
                                          example, SCCP TCP listening socket (skinny_tcp_listen_socket fd) values 0 and 1 verify dual-stack configuration. When IPv6
                                          only is configured, the show ephone socket command displays SCCP TCP listening socket values as (-1) and (0). The listening socket is closed if the value is (-1). When
                                          IPv4 only is configured, the show ephone socket command displays SCCP TCP listening socket values as (0) and (-1).

#### Example:

```
Router# show ephone socket skinny_tcp_listen_socket fd = 0

skinny_tcp_listen_socket (ipv6) fd = 1

skinny_secure_tcp_listen_socket fd = -1

skinny_secure_tcp_listen_socket (ipv6) fd = -1

Phone 7,

skinny_sockets[15] fd = 16 [ipv6]

read_buffer 0x483C0BC4, read_offset 0, read_header N, read_length 0

resend_queue 0x47EC69EC, resend_offset 0, resend_flag N, resend_Q_depth 0

MTP 1,

skinny_sockets[16] fd = 17

read_buffer 0x483C1400, read_offset 0, read_header N, read_length 0

resend_queue 0x47EC6978, resend_offset 0, resend_flag N, resend_Q_depth 0

Phone 8,

skinny_sockets[17] fd = 18 [ipv6]

read_buffer 0x483C1C3C, read_offset 0, read_header N, read_length 0

resend_queue 0x47EC6904, resend_offset 0, resend_flag N, resend_Q_depth 0
```

Step 3

Use the show ephone summary command to verify the IPv6 or IPv4 addresses configured for ephones. The following example displays IPv6 and IPv4 addresses
                                          for different ephones:

#### Example:

```
Router# show ephone summary 
ephone-2[1] Mac:0016.46E0.796A TCP socket:[7] activeLine:0 whisperLine:0 REGISTERED

mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0 privacy:1 primary_dn: 1*

IPv6:2000:A0A:201:0:216:46FF:FEE0:796A* IP:10.10.10.12 7970 keepalive 599 music 0 1:1

sp1:2004

ephone-7[6] Mac:0013.19D1.F8A2 TCP socket:[6] activeLine:0 whisperLine:0 REGISTERED

mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0 privacy:0 primary_dn: 13*

IP:10.10.10.14 * Telecaster 7940 keepalive 2817 music 0 1:13 2:28
```

### Configure Bulk
                           	 Registration

To configure bulk
                                 		  registration for registering a block of phone numbers with an external
                                 		  registrar so that calls can be routed to Cisco Unified CME from a SIP network,
                                 		  perform the following steps.

Numbers that match
                                 		  the number pattern defined by using the bulk command
                                 		  can register with the external registrar. The block of numbers that is
                                 		  registered can include any phone that is attached to Cisco Unified CME or any
                                 		  analog phone that is directly attached to an FXS port on a Cisco Unified CME
                                 		  router.

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- mode cme

- bulk number

- exit

- sip-ua

- registrar { dns : address | ipv4 : destination-address } expires seconds [ tcp ] [ secondary ] no registrar [ secondary ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Step 4

mode cme

#### Example:

```
Router(config-register-global)# mode cme
```

Step 5

bulk number

#### Example:

```
Router(config-register-global)# bulk 408526....
```

number —Unique sequence of up to 32 characters,
                                                   					 including wild cards and patterns that represents E.164 numbers that will
                                                   					 register with a SIP proxy server.

Step 6

exit

#### Example:

```
Router(config-register-pool)# exit
```

Step 7

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Step 8

registrar { dns : address | ipv4 : destination-address } expires seconds [ tcp ] [ secondary ] no registrar [ secondary ]

#### Example:

```
Router(config-sip-ua)# registrar server ipv4:1.5.49.240
```

Step 9

end

#### Example:

```
Router(config-sip-ua)# end
```

#### Examples

The following
                                 		  example shows that all phone numbers that match the pattern “408555...” can
                                 		  register with a SIP proxy server (IP address 1.5.49.240):

```
voice register global
 mode cme
 bulk 408555….
sip-ua
 registrar ipv4:1.5.49.240
```

### Configure Bulk Registration for SIP IP Phones

#### Before you begin

- Cisco Unified CME 8.6 or a
                                    			 later version.

- Phone firmware 8.3 or a
                                    			 later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool tag

- session-transport { tcp | udp }

- number tag dn tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

voice register pool tag

#### Example:

```
Router(config)#voice register pool 20
```

Step 4

session-transport { tcp | udp }

#### Example:

```
Router(config-register-pool)#session-transport tcp
```

- tcp —TCP is
                                                				  used for bulk registration.

- udp —UDP is
                                                				  used for line registration.

Step 5

number tag dn tag

#### Example:

```
Router(config-register-pool)#number 1 dn 2
```

- dn dn-tag —Identifies the directory number
                                                				  for this SIP phone as defined by the voice register dn command.

Step 6

end

#### Example:

```
Router(config-register-pool)# end
```

#### Verify Phone Registration Type and Status

You can verify phone registration type and status using the show voice register pool command. The following example shows
                                    		  that the Cisco Unified IP phone 7970 used the bulk registration method and
                                    		  completed the registration process:

```
Router#sh voice register pool 20
```

```
Pool Tag 20
```

```
Config:
```

```
Mac address is 001B.2A89.3698
```

```
Type is 7970
```

```
Number list 1 : DN 20
```

```
Number list 2 : DN 2
```

```
Number list 3 : DN 24
```

```
Number list 4 : DN 4
```

```
Number list 5 : DN 6
```

```
Number list 6 : DN 7
```

```
Number list 7 : DN 17
```

```
Number list 8 : DN 23
```

```
Proxy Ip address is 0.0.0.0
```

```
Current Phone load version is Cisco-CP7970G/9.0.1
```

```
DTMF Relay is enabled, rtp-nte, sip-notify
```

```
Call Waiting is enabled
```

```
DnD is disabled
```

```
Video is disabled
```

```
Camera is disabled
```

```
Busy trigger per button value is 0
```

```
speed-dial blf 1 6779 label 6779_device
```

```
speed-dial blf 2 3555 label 3555_remote
```

```
speed-dial blf 3 6130 label 6130
```

```
speed-dial blf 4 3222 label 3222_remote_dev
```

```
fastdial 1 1234
```

```
keep-conference is enabled
```

```
username johndoe password cisco
```

```
template is 1
```

```
kpml signal is enabled
```

```
Lpcor Type is none
```

```
Transport type is tcp
```

```
service-control mechanism is supported
```

```
Registration method: bulk - completed
```

```
registration Call ID is 001b2a89-3698017e-68646967-126b902e@28.18.88.33
```

```
Privacy is configured:  init status: ON, current status: ON
```

```
Privacy button is enabled
```

```
active primary line is: 6010
```

### Set Up Cisco Unified CME for SCCP Phones

To identify filenames and the location of phone firmware for phone
                                 		  types to be connected, specify the port for phone registration, and specify the
                                 		  number of phones and directory numbers to be supported, perform the following
                                 		  steps.

Restriction

### SUMMARY STEPS

- enable

- configure terminal

- tftp-server device : filename

- telephony-service

- load phone-type firmware-file

- max-ephones max-phones

- max-dn max-directory - numbers [ preference preference-order ]
                                 			 [ no-reg primary | both ]

- ip source-address ip-address [ port port ] [ any-match | strict-match ]

- ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

tftp-server device : filename

#### Example:

```
Router(config)# tftp-server flash:P00307020300.bin
```

A separate tftp-server command is required for each phone type.

Required for Cisco Unified CME 7.0/4.3 and earlier versions.

Cisco Unified CME 7.0(1) and later versions: Required only if the location for cnf files is not flash or slot 0, such as system
                                                   memory or a TFTP server url. Use the complete filename, including the file suffix, for phone firmware versions later than
                                                   version 8.2(2) for all phone types.

Step 4

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Step 5

load phone-type firmware-file

#### Example:

```
Router(config-telephony)# load 7960-7940 P00307020300
```

A separate load command is required for each IP phone type.

firmware-file—Filename is case-sensitive.

Cisco Unified CME 7.0/4.3 and earlier versions: Do not use the .sbin or .loads file extension except for the Cisco ATA and
                                                         Cisco Unified IP Phone 7905 and 7912.

Cisco Unified CME 7.0(1) and later versions: Use the complete filename, including the file suffix, for phone firmware versions
                                                         later than version 8.2(2) for all phone types.

Step 6

max-ephones max-phones

#### Example:

```
Router(config-telephony)# max-ephones 24
```

Maximum number is platform and version-specific. Type ? for range.

In Cisco Unified CME 7.0/4.3 and later versions, the maximum number of phones that can register is different from the maximum
                                                   number of phones that can be configured. The maximum number of phones that can be configured is 1000.

In versions earlier than Cisco Unified CME 7.0/4.3, this command restricted the number of phones that could be configured
                                                   on the router.

Step 7

max-dn max-directory - numbers [ preference preference-order ]
                                          			 [ no-reg primary | both ]

#### Example:

```
Router(config-telephony)# max-dn 200 no-reg primary
```

Maximum number is platform and version-specific. Type ? for value.

Step 8

ip source-address ip-address [ port port ] [ any-match | strict-match ]

#### Example:

```
Router(config-telephony)# ip source-address 10.16.32.144
```

port port —(Optional) TCP/IP port number to use for SCCP. Range is 2000 to 9999. Default is 2000.

any-match —(Optional) Disables strict IP address checking for registration. This is the default.

strict-match —(Optional) Instructs the router to reject IP phone registration attempts if the IP server address used by the phone does
                                                   not exactly match the source address.

Step 9

ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

#### Example:

```
Router(config-telephony)# ip qos dscp af43 video
```

Step 10

end

#### Example:

```
Router(config-telephony)# end
```

#### Examples

The following example shows different DSCP settings for media, signaling, video, and services enabled with the ip qos dscp
                                 command:

```
telephony-service
load 7960-7940 P00308000500
max-ephones 100
max-dn 240
ip source-address 10.10.10.1 port 2000
ip qos dscp af11 media
ip qos dscp cs2 signal
ip qos dscp af43 video
ip qos dscp 25 service
cnf-file location flash:
.
.
```

### Set Date and Time Parameters for SCCP Phones

To specify the format of the date and time that appears on all SCCP
                                 		  phones in Cisco Unified CME, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- date-format { dd-mm-yy | mm-dd-yy | yy-dd-mm | yy-mm-dd }

- time-format { 12 | 24 }

- time-zone number

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

date-format { dd-mm-yy | mm-dd-yy | yy-dd-mm | yy-mm-dd }

#### Example:

```
Router(config-telephony)# date-format yy-mm-dd
```

(Optional) Sets the date format for phone display.

- Default: mm-dd-yy .

Step 5

time-format { 12 | 24 }

#### Example:

```
Router(config-telephony)# time-format 24
```

(Optional) Selects a 12-hour or 24-hour clock for the time display
                                             				format on phone display.

- Default: 12 .

Step 6

time-zone number

#### Example:

```
Router(config-telephony)# time-zone 2
```

Sets time zone for SCCP phones.

- Not required for Cisco Unified IP Phone 7902G, 7905G, 7912G,
                                                				  7920, 7921, 7935, 7936, 7940, 7960, or 7985G.

- Default: 5, Pacific Standard/Daylight Time (-480).

Step 7

end

#### Example:

```
Router(config-telephony)# end
```

Returns to privileged EXEC mode.

### Block Automatic
                           	 Registration for SCCP Phones

#### Before you begin

Cisco Unified CME
                                 		  4.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- no auto-reg-ephone

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Step 4

no auto-reg-ephone

#### Example:

```
Router(config-telephony)# no auto-reg-ephone
```

Default:
                                                   					 Enabled.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

### Define Per-Phone Configuration Files and Alternate Location for SCCP Phones

Restriction

TFTP does not support file deletion. When configuration files are updated, they overwrite any existing configuration files
                                                   with the same name. If you change the configuration file location, files are not deleted from the TFTP server.

Generating configuration files on flash memory or slot 0 memory can take up to a minute, depending on the number of files
                                                   being generated.

For smaller routers such as the Cisco 2600 series routers, you must manually enter the squeeze command to erase files after changing the configuration file location or entering any commands that trigger the deletion
                                                   of configuration files. Unless you use the squeeze command, the space used by the moved or deleted configuration files is not usable by other files.

If VRF Support on Cisco Unified CME is configured and the cnf-file location command is configured for system:, the per phone or per phone type file for an ephone in a VRF group is created in system:/its/vrf<group-tag>/ . The vrf directory is automatically created and appended to the TFTP path. No action is required on your part. Locale files
                                                   are still created in system:/its/.

If VRF Support on Cisco Unified CME is configured and the cnf-file location command is configured as flash: or slot0: , the per phone or per phone type file for an ephone in a VRF group is named flash:/its/vrf<group-tag>_<filename> or slot0:/its/vrf<group-tag>_filename> . The vrf directory is automatically created and appended to the TFTP path. No action is required on your part. The location
                                                   of the locale files is not changed.

To define a location other than system:/its for storing configuration
                                 		  files for per-phone and per-phone type configuration files, perform the
                                 		  following steps.

#### Before you begin

Cisco Unified CME 4.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- cnf-file location { flash: | slot0: | tftp tftp-url }

- cnf-file { perphonetype | perphone }

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

cnf-file location { flash: | slot0: | tftp tftp-url }

#### Example:

```
Router(config-telephony)# cnf-file location flash:
```

Specifies a location other than system:/its for storing phone
                                             				configuration files.

Required for per-phone or per-phone type configuration files.

Step 5

cnf-file { perphonetype | perphone }

#### Example:

```
Router(config-telephony)# cnf-file perphone
```

Specifies whether to use a separate file for each type of phone or
                                             				for each individual phone.

Required if you configured the cnf-file location command.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Returns to privileged EXEC mode.

#### Example

The following example selects flash memory as the configuration file
                                 		  storage location and per-phone as the type of configuration files that the
                                 		  system generates:

```
telephony-service
```

```
cnf-file location flash:
```

```
cnf-file perphone
```

#### What to do next

If you changed the configuration file storage location, use the option 150 ip command to update the address. See Change the TFTP Address on a DHCP Server .

### Modify Defaults for Timeouts for SCCP Phones

To configure values for system-level intervals for which default values are typically adequate, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- timeouts busy seconds

- timeouts interdigit seconds

- timeouts ringing seconds

- keepalive seconds

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

timeouts busy seconds

#### Example:

```
Router(config-telephony)# timeouts busy 20
```

(Optional) Sets the length of time after which calls that are transferred to busy destinations are disconnected.

seconds —Number of seconds. Range is 0 to 30. Default is 10.

Step 5

timeouts interdigit seconds

#### Example:

```
Router(config-telephony)# timeouts interdigit 30
```

(Optional) Configures the interdigit timeout value for all Cisco Unified IP phones attached to the router.

seconds —Number of seconds before the interdigit timer expires. Range is 2 to 120. Default is 10.

Step 6

timeouts ringing seconds

#### Example:

```
Router(config-telephony)# timeouts ringing 30
```

(Optional) Sets the duration, in seconds, for which the Cisco Unified CME system allows ringing to continue if a call is not
                                             answered. Range is 5 to 60000. Default is 180.

Step 7

keepalive seconds

#### Example:

```
Router(config-telephony)# keepalive 45
```

(Optional) Sets the time interval, in seconds, between keepalive
                                             				messages that are sent to the router by Cisco Unified IP phones.

The default is usually adequate. If the interval is set too large, it is possible for notification to be delayed when a system
                                                   goes down.

Range: 10 to 65535. Default: 0.

Step 8

end

#### Example:

```
Router(config-telephony)# end
```

Returns to privileged EXEC mode.

### Configure
                           	 Redundant Router for SCCP Phones

#### Before you begin

- Cisco Unified CME 4.0 or a
                                    			 later version.

- The secondary router‘s
                                    			 running configuration must be identical to that of the primary router.

- The physical configuration
                                    			 of the secondary router must be as described in Redundant Cisco Unified CME Router for SCCP Phones .

- Phones that use this
                                    			 feature must be configured with the type command, which guarantees that the appropriate phone configuration file will be
                                    			 present.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- ip source-address ip-address [ port port ] [ secondary ip-address [ rehome seconds ]] [ any-match | strict-match ]

- exit

- voice-port slot-number / port

- signal ground-start

- incoming alerting
                                    				ring-only

- ring number number

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

ip source-address ip-address [ port port ] [ secondary ip-address [ rehome seconds ]] [ any-match | strict-match ]

#### Example:

```
Router(config-telephony)# ip source-address 10.0.0.1 port 2000 secondary 10.2.2.25
```

Identifies the
                                             				IP address and port number that the primary Unified CME router uses for IP
                                             				phone registration.

- ip-address —Address of the primary Unified CME
                                                				  router.

- port port —(Optional) TCP/IP port number to use for
                                                				  SCCP. Range is 2000 to 9999. Default is 2000.

- secondary ip-address —Indicates a backup Unified CME router.

- rehome seconds —Not
                                                				  used by Unified CME. Used only by phones registered to Cisco Unified SRST.

- any-match —(Optional) Disables strict IP address
                                                				  checking for registration. This is the default.

- strict-match —(Optional) Router rejects IP phone
                                                				  registration attempts if the IP server address used by the phone does not
                                                				  exactly match the source address.

Step 5

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 6

voice-port slot-number / port

#### Example:

```
Router(config)# voice-port 2/0
```

Enters
                                             				voice-port configuration mode for the FXO voice port for DID calls from the
                                             				PSTN.

Step 7

signal ground-start

#### Example:

```
Router(config-voiceport)# signal ground-start
```

Specifies
                                             				ground-start signaling for a voice port.

Step 8

incoming alerting
                                             				ring-only

#### Example:

```
Router(config-voiceport)# incoming alerting ring-only
```

Instructs
                                             				the FXO ground-start voice port to detect incoming calls by detecting incoming
                                             				ring signals.

Step 9

ring number number

#### Example:

```
Router(config-voiceport)# ring number 3
```

(Required
                                             				only for the secondary router) Sets the maximum number of rings to be detected
                                             				before answering an incoming call over an FXO voice port.

number —Number of rings detected before answering
                                                   					 the call. Range is 1 to 10. Default is 1.

Step 10

end

#### Example:

```
Router(config-voiceport)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Redundant Router for SIP Phones

#### Before you begin

Cisco
                                       				Unified CME 11.6 or a later version.

Auto-register configuration is recommended only on the primary
                                       				router.

XML
                                       				interface for secondary backup router is configured. See Configure the XML Interface for the Secondary Backup Router .

It is
                                                   				  recommended to configure the XML interface for a seamless failover from primary
                                                   				  to secondary Cisco Unified CME. Else, there is delay in the phones getting
                                                   				  registered to secondary Cisco Unified CME due to mismatch in the configuration
                                                   				  version timestamp.

Ensure that
                                       				you configure version stamp synchronization on the primary router. See Configure Version Stamp Synchronization on the Primary Router .

It is
                                                   				  recommended to configure version stamp synchronization for a seamless failover
                                                   				  from primary to secondary Cisco Unified CME. Else, there is delay in the phones
                                                   				  getting registered to secondary Cisco Unified CME.

Restriction

Active calls
                                                   				  are not supported when switchover happens from primary router to the secondary
                                                   				  router.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- source-address ip-address [ port port ] [ secondary ip-address ]

- keepalive seconds

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode.

Step 4

source-address ip-address [ port port ] [ secondary ip-address ]

#### Example:

```
Router(config-register-global)# source-address 10.6.21.4 port 6000 secondary 10.6.50.6
```

Identifies the
                                             				IP address and port number that the Cisco Unified CME router uses for IP phone
                                             				registration.

- ip-address —Address of the primary
                                                				  Cisco Unified CME router.

- port port —(Optional) TCP/IP port number to use for SIP.
                                                				  Range is 2000 to 9999. Default is 5060 for SIP.

- secondary ip-address —Indicates a backup Cisco Unified CME
                                                				  router.

Step 5

keepalive seconds

#### Example:

```
Router(config-register-global)# keepalive 200
```

Sets the
                                             				length of the time interval between successive keepalive messages from the SIP
                                             				phones to Cisco Unified CME router. Default is 120 seconds.

Step 6

end

#### Example:

```
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Version
                           	 Stamp Synchronization on the Primary Router

To configure the
                                 		  primary router to enable automatic synchronization of 'version stamp' with
                                 		  secondary backup router, perform the following steps.

Tip

All
                                             			 phone-related configurations are tagged with a 'version stamp' that indicates
                                             			 when the last configuration change was made.

#### Before you begin

XML interface
                                       				for secondary backup router is configured. See Configure the XML Interface for the Secondary Backup Router .

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- standby
                                       				  username username password password

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Step 4

standby
                                                				  username username password password

#### Example:

```
Router(config-telephony)# standby username user23 password 3Rs92uzQ
```

Defines an
                                             				authorized user.

Same username and password that is defined in Configure the XML Interface for the Secondary Backup Router .

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure the XML
                           	 Interface for the Secondary Backup Router

To configure the
                                 		  secondary backup router to activate the XML interface required to receive
                                 		  "version stamp" configuration change information from the primary router,
                                 		  perform the following steps.

Restriction

Automatic
                                                   				  synchronization for new or replacement routers is not supported.

#### Before you begin

The XML interface, provided through the Cisco IOS XML Infrastructure (IXI), must be configured. See Configuring the XML API .

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- xml user user-name password password
                                       				  privilege-level

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Step 4

xml user user-name password password
                                                				  privilege-level

#### Example:

```
Router(config-telephony)# xml user user23 password 3Rs92uzQ 15
```

Defines an
                                             				authorized user.

user-name —Username of the authorized user.

password —Password to use for access.

privilege-level —Level of access to Cisco IOS
                                                   					 commands to be granted to this user. Only the commands with the same or a lower
                                                   					 level can be executed via XML. Range is 0 to 15.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Overlap Dialing on SCCP IP Phones

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- overlap-signal

- exit

- ephone phone-tag

- overlap-signal

- exit

- ephone-template template-tag

- overlap-signal

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

telephony-service

#### Example:

```
Router(config)telephony-service
```

Step 4

overlap-signal

#### Example:

```
Router(config-telephony)#overlap-signal
```

Step 5

exit

#### Example:

```
Router(config-telephony)#exit
```

Step 6

ephone phone-tag

#### Example:

```
Router(config)ephone 10
```

Step 7

overlap-signal

#### Example:

```
Router(config-ephone)overlap-signal
```

Step 8

exit

#### Example:

```
Router(config-ephone)exit
```

Step 9

ephone-template template-tag

#### Example:

```
Router(config)ephone-template 10
```

Step 10

overlap-signal

#### Example:

```
Router(config-ephone-template)#overlap-signal
```

Step 11

end

#### Example:

```
Router(config-ephone-template)# end
```

### Set Up Cisco Unified CME for SIP Phones

To identify filenames and location of phone firmware for phone types
                                 		  to be connected, to specify the port for phone registration, and to specify the
                                 		  number of phones and directory numbers to be supported, perform the following
                                 		  steps.

From Cisco IOS XE Amsterdam 17.2.1r onwards, cme-app mode was added for ISR4321 routers. This mode allows configuration of up to 200 phones for routers that are dedicated to
                                             CME use only. The cme or cme-app modes configure SIP phones and features for standalone call control use.

Restriction

SIP endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP trunks only.

Certain Cisco Unified IP phones, such as the Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE,
                                                   are supported only in Cisco Unified CME 4.1 and later versions.

DSCP requires Cisco Unified CME 7.1 or a later version. If DSCP is configured for the gateway interface using the service-policy command or for the dial peer using the ip qos dscp command, the value set with those commands takes precedence over the DSCP value configured in this procedure.

#### Before you begin

Cisco CME 3.4 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- mode [ cme | cme-app ]

- source-address ip-address [ port port ]

- load phone-type firmware-file

- tftp-path { flash : | slot0: | tftp:// url }

- max-pool max-phones

- max-dn max-directory-numbers

- authenticate [ all ][ realm string ]

- ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Step 4

mode [ cme | cme-app ]

#### Example:

```
Router(config-register-global)# mode cme
```

Step 5

source-address ip-address [ port port ]

#### Example:

```
Router(config-register-global)# source-address 10.6.21.4
```

port port —(Optional) TCP/IP port number. Range: 2000 to 9999. Default: 2000.

Step 6

load phone-type firmware-file

#### Example:

```
Router(config-register-global)# load 7960-7940 P0S3-07-3-00
```

A separate load command is required for each phone type.

Step 7

tftp-path { flash : | slot0: | tftp:// url }

#### Example:

```
Router(config-register-global)# tftp-path http://mycompany.com/files
```

Default: system memory (system:/cme/sipphone/).

Step 8

max-pool max-phones

#### Example:

```
Router(config-register-global)# max-pool 10
```

Version- and platform-dependent; type ? for range.

In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is maximum number supported by platform.

In Cisco Unified CME 7.0(1) and later versions: Default is 0.

Step 9

max-dn max-directory-numbers

#### Example:

```
Router(config-register-global)# max-dn 20
```

Required for Cisco Unified CME 7.0(1) and later versions.

In Cisco Unified CME 7.0(1) and later versions: Default is 0. Range is 1 to maximum number supported by platform. Type ? for range.

In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is 150 or maximum allowed on platform. Type ? for value.

Step 10

authenticate [ all ][ realm string ]

#### Example:

```
Router(config-register-global)# authenticate all realm company.com
```

Step 11

ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

#### Example:

```
Router(config-register-global)# ip qos dscp af43 video
```

Step 12

end

#### Example:

```
Router(config-register-global)# end
```

### Set Up Cisco Unified CME for SIP Phones

To identify filenames and location of phone firmware for phone types
                                 		  to be connected, to specify the port for phone registration, and to specify the
                                 		  number of phones and directory numbers to be supported, perform the following
                                 		  steps.

From Cisco IOS XE Amsterdam 17.2.1r onwards, cme-app mode was added for ISR4321 routers. This mode allows configuration of up to 200 phones for routers that are dedicated to
                                             CME use only. The cme or cme-app modes configure SIP phones and features for standalone call control use.

Restriction

SIP endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP trunks only.

Certain Cisco Unified IP phones, such as the Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE,
                                                   are supported only in Cisco Unified CME 4.1 and later versions.

DSCP requires Cisco Unified CME 7.1 or a later version. If DSCP is configured for the gateway interface using the service-policy command or for the dial peer using the ip qos dscp command, the value set with those commands takes precedence over the DSCP value configured in this procedure.

#### Before you begin

Cisco CME 3.4 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- mode [ cme | cme-app ]

- source-address ip-address [ port port ]

- load phone-type firmware-file

- tftp-path { flash : | slot0: | tftp:// url }

- max-pool max-phones

- max-dn max-directory-numbers

- authenticate [ all ][ realm string ]

- ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Step 4

mode [ cme | cme-app ]

#### Example:

```
Router(config-register-global)# mode cme
```

Step 5

source-address ip-address [ port port ]

#### Example:

```
Router(config-register-global)# source-address 10.6.21.4
```

port port —(Optional) TCP/IP port number. Range: 2000 to 9999. Default: 2000.

Step 6

load phone-type firmware-file

#### Example:

```
Router(config-register-global)# load 7960-7940 P0S3-07-3-00
```

A separate load command is required for each phone type.

Step 7

tftp-path { flash : | slot0: | tftp:// url }

#### Example:

```
Router(config-register-global)# tftp-path http://mycompany.com/files
```

Default: system memory (system:/cme/sipphone/).

Step 8

max-pool max-phones

#### Example:

```
Router(config-register-global)# max-pool 10
```

Version- and platform-dependent; type ? for range.

In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is maximum number supported by platform.

In Cisco Unified CME 7.0(1) and later versions: Default is 0.

Step 9

max-dn max-directory-numbers

#### Example:

```
Router(config-register-global)# max-dn 20
```

Required for Cisco Unified CME 7.0(1) and later versions.

In Cisco Unified CME 7.0(1) and later versions: Default is 0. Range is 1 to maximum number supported by platform. Type ? for range.

In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is 150 or maximum allowed on platform. Type ? for value.

Step 10

authenticate [ all ][ realm string ]

#### Example:

```
Router(config-register-global)# authenticate all realm company.com
```

Step 11

ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

#### Example:

```
Router(config-register-global)# ip qos dscp af43 video
```

Step 12

end

#### Example:

```
Router(config-register-global)# end
```

### Set Date and Time
                           	 Parameters for SIP Phones

#### Before you begin

Cisco CME
                                       				3.4 or a later version.

mode cme command is
                                       				enabled.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- timezone number

- date-format [ d/m/y | m/d/y | y-d-m | y/d/m | y/m/d | yy-m-d ]

- time-format { 12 | 24 }

- dst auto-adjust

- dst { start | stop } month [ day day-of-month | week week-number | day day-of-week] time hour:minutes

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

timezone number

#### Example:

```
Router(config-register-global)# timezone 8
```

Selects the
                                             				time zone used for SIP phones in Cisco Unified CME.

Default: 5 ,
                                                   					 Pacific Standard/Daylight Time. Type ? to
                                                   					 display a list of time zones.

Step 5

date-format [ d/m/y | m/d/y | y-d-m | y/d/m | y/m/d | yy-m-d ]

#### Example:

```
Router(config-register-global)# date-format yy-m-d
```

(Optional)
                                             				Selects the date display format on SIP phones in Cisco Unified CME.

Default: m/d/y .

Step 6

time-format { 12 | 24 }

#### Example:

```
Router(config-register-global)# time-format 24
```

(Optional)
                                             				Selects the time display format on SIP phones in Cisco Unified CME.

Default: 12 .

Step 7

dst auto-adjust

#### Example:

```
Router(config-register-global)# dst auto-adjust
```

(Optional)
                                             				Enables automatic adjustment of Daylight Saving Time on SIP phones in
                                             				Cisco Unified CME.

To
                                                   					 modify start and stop times for daylight savings time, use the dst command.

Step 8

dst { start | stop } month [ day day-of-month | week week-number | day day-of-week] time hour:minutes

#### Example:

```
Router(config-register-global)# dst start jan day 1 time 00:00
```

```
Router(config-register-global)# dst stop mar day 31 time 23:59
```

(Optional) Sets the time period for Daylight Saving Time on SIP phones in Cisco Unified CME.

Required if automatic adjustment of Daylight Saving Time is enabled by using the dst auto-adjust command.

Default is Start: First week of April, Sunday, 2:00 a.m. Stop: Last week of October, Sunday 2:00 a.m.

Step 9

end

#### Example:

```
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

### Set Network Time
                           	 Protocol for SIP Phones

To enable Network
                                 		  Time Protocol (NTP) for certain phones, such as the Cisco
                                 		  Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE,
                                 		  connected to Cisco Unified CME running SIP, perform the following steps.

#### Before you begin

- Cisco Unified CME 4.1 or a
                                    			 later version.

- The firmware load 8.2(1) or
                                    			 a later version is installed for SIP phones to download. For upgrade
                                    			 information, see Upgrade or Downgrade SIP Phone Firmware .

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- ntp-server ip-address [ mode { anycast | directedbroadcast | multicast | unicast }]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

- Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME environment.

Step 4

ntp-server ip-address [ mode { anycast | directedbroadcast | multicast | unicast }]

#### Example:

```
Router(config-register-global)# ntp-server 10.1.2.3
```

Synchronizes
                                             				clock on this router with the specified NTP server.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

### Enable HFS Download Service for SIP Phones

Restriction

- Only Cisco Unified 8951,
                                                				9951, and 9971 SIP IP Phones are supported.

- No IPv6 support for the
                                                				HFS download service.

#### Before you begin

Cisco Unified CME 8.8 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ip http server

- ip http port number

- voice register global

- mode cme

- load phone-type firmware-file

- create profile

- exit

- telephony-service

- hfs enable [ port port-number ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

ip http server

#### Example:

```
Router(config)# ip http server
```

Step 4

ip http port number

#### Example:

```
Router(config)# ip http port 60
```

Step 5

voice register global

#### Example:

```
Router(config)# voice register global
```

Step 6

mode cme

#### Example:

```
Router(config-register-global)# mode cme
```

Step 7

load phone-type firmware-file

#### Example:

```
Router(config-register-global)# load 3951 SIP51.9.2.1S
```

Step 8

create profile

#### Example:

```
Router(config-register-global)# create profile
```

Step 9

exit

#### Example:

```
Router(config-register-global)# exit
```

Step 10

telephony-service

#### Example:

```
Router (config)# telephony-service
```

Step 11

hfs enable [ port port-number ]

#### Example:

```
Router(config-telephony)# hfs enable port 5678
```

- port port-number —(Optional) Specifies the
                                                				  port where the HFS download service is enabled. Range is from 1024 to 65535.
                                                				  Port 80 is the default port. Port 6970 is the custom port.

Step 12

end

#### Example:

```
Router(config-telephonyl)# end
```

#### Troubleshooting HFS Download Service

The debug cme-hfs command can be used to troubleshoot an attempt to
                                 		download Cisco Unified SIP IP phone configuration and firmware files using the
                                 		HFS service.

### Configure HFS Home Path for SIP Phone Firmware Files

To configure a home path where any requested Cisco Unified SIP IP
                                 		  Phone firmware file that has no explicit binding can be searched and fetched
                                 		  using the HFS download service, perform the following steps.

Restriction

- Only Cisco 8951, 9951,
                                                				and 9971 SIP IP Phones are supported.

- No IPv6 support for the
                                                				HFS download service.

#### Before you begin

Cisco Unified CME 8.8 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ip http server

- ip http port number

- telephony-service

- hfs enable [ port port-number ]

- hfs home-path path

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

ip http server

#### Example:

```
Router(config)# ip http server
```

Step 4

ip http port number

#### Example:

```
Router(config)# ip http port 1234
```

Step 5

telephony-service

#### Example:

```
Router (config)# telephony-service
```

Step 6

hfs enable [ port port-number ]

#### Example:

```
Router(config-telephony)# hfs enable port 6970
```

Step 7

hfs home-path path

#### Example:

```
Router(config-telephony)# hfs home-path flash:/cme/loads/
```

Step 8

end

#### Example:

```
Router(config-telephony)# end
```

### Change
                           	 Session-Level Application for SIP Phones

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- application application-name

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Step 4

application application-name

#### Example:

```
Router(config-register-global)# application sipapp2
```

(Optional) Changes the default application for all dial peers
                                             				associated with the SIP phones in Cisco Unified CME to the specified
                                             				application.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

### Enable Media Flow
                           	 Mode on SIP Trunks

Restriction

- If any media service (like
                                                				transcoding and conferencing) is needed for SIP to SIP trunk call, at least one
                                                				of the SIP trunks must be placed in flow through mode.

- If media needs to flow
                                                				through Cisco Unified CME for voicemail calls, the SIP trunk going towards the
                                                				voicemail must be in flow through mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- media [ flow around | flow
                                       				  through ]

- exit

- dial-peer voice tag voip

- media {[ flow-around | flow-through ] forking }

- exit

- voice class media tag

- media {[ flow-around | flow-through ] forking }

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

- Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)#voice service voip
```

Enters voice service voip configuration mode.

Step 4

media [ flow around | flow
                                                				  through ]

#### Example:

```
Router(conf-voi-serv)#media flow-around
```

Enables global
                                             				media setting for VoIP calls.

- flow around —Allows the media to flow around the
                                                				  gateway.

- flow through —Allows the media to flow through the
                                                				  gateway.

Step 5

exit

#### Example:

```
Router(config-voi-ser)#exit
```

Exits voice
                                             				service voip configuration mode.

Step 6

dial-peer voice tag voip

#### Example:

```
Router(config)#dial-peer voice 222 voip
```

Enters
                                             				dial-peer configuration mode to define a VoIP dial peer for the voice-mail
                                             				system.

- tag —Defines the dial peer being configured. Range
                                                				  is 1 to 1073741823.

Step 7

media {[ flow-around | flow-through ] forking }

#### Example:

```
Router(config-dial-peer)#media flow-around
```

Enables media
                                             				settings for voice dial-peer.

- flow-around —Allows the media to flow around the
                                                				  gateway.

- flow-through —Allows the media to flow through the
                                                				  gateway.

- forking —Enables media forking.

Step 8

exit

#### Example:

```
Router(config-ephone)exit
```

Exits voip
                                             				dial-peer configuration mode.

Step 9

voice class media tag

#### Example:

```
Router(config)#voice class media 10
```

Enters voice
                                             				class media configuration mode.

- tag — Defines the voice class media tag being
                                                				  configured. Range is from 1 to 10000.

Step 10

media {[ flow-around | flow-through ] forking }

#### Example:

```
Router(config-class)#media flow-around
```

Enables media
                                             				settings for voice dial-peer.

- flow-around —Allows the media to flow around the
                                                				  gateway.

- flow-through —Allows the media to flow through the
                                                				  gateway.

- forking —Enables media forking.

Step 11

end

#### Example:

```
Router(config-class)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Overlap Dialing on SIP Phones

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- overlap-signal

- exit

- voice register pool pool-tag

- overlap-signal

- exit

- voice register template template tag

- overlap-signal

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Step 3

voice register global

#### Example:

```
Router(config)voice register global
```

Step 4

overlap-signal

#### Example:

```
Router(config-register-pool)overlap-signal
```

Step 5

exit

#### Example:

```
Router(config-register-pool)exit
```

Step 6

voice register pool pool-tag

#### Example:

```
Router(config)voice register pool 10
```

Step 7

overlap-signal

#### Example:

```
Router(config-register-global)overlap-signal
```

Step 8

exit

#### Example:

```
Router(config-register-global)exit
```

Step 9

voice register template template tag

#### Example:

```
Router(config)voice register template 5
```

- template-tag —Unique
                                                				  identifier for the ephone template that is being created. Range: 1 to 10.

Step 10

overlap-signal

#### Example:

```
Router(config-register-temp) overlap-signal
```

Step 11

end

#### Example:

```
Router(config-register-temp)# end
```

## Configuration Examples for System-Level Parameters

### Example for Bulk Registration Support for SIP Phones

The following example shows TCP and UDP configured for various phones.
                                 		  Notice that in Bulk Registration (TCP), only the primary directory number is
                                 		  displayed, while in Line Registration (UDP), all directory numbers are
                                 		  displayed.

```
Router# show sip-ua status registrar
```

```
Line          destination      expires(sec)  contact
```

```
transport     call-id
```

```
peer
```

```
============================================================
```

```
1001          21.1.1.138       112           21.1.1.138
```

```
TCP           239665429027943@21.1.1.138
```

```
40015
```

```
1009          21.1.1.138       118           21.1.1.138
```

```
UDP           239671730027945@21.1.1.138
```

```
40019
```

```
1010          21.1.1.138       118           21.1.1.138
```

```
UDP           239671745127945@21.1.1.138
```

```
40021
```

### Example for IPv6 Support on Cisco Unified CME

```
!
```

```
ip source-route
```

```
!
```

```
!ip cef
```

```
no ip dhcp use vrf connected
```

```
ip dhcp excluded-address 10.10.10.1 10.10.10.9
```

```
ip dhcp excluded-address 192.168.2.1
```

```
ipv6 unicast-routing
```

```
ipv6 cef
```

```
ntp server 223.255.254.254
```

```
multilink bundle-name authenticated
```

```
isdn switch-type primary-5ess
```

```
!
```

```
voice service voip
```

```
allow-connections h323 to h323
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
allow-connections sip to sip
```

```
fax protocol cisco
```

```
sip
```

```
registrar server expires max 1200 min 300
```

```
!
```

```
!
```

```
!
```

```
voice register dn  1
```

```
number 2016
```

```
allow watch
```

```
name SIP-7961GE
```

```
label SIP2016
```

```
!
```

```
voice register dn  2
```

```
number 2017
```

```
!
```

```
!
```

```
voice logout-profile 1
```

```
!
```

```
voice logout-profile 2
```

```
number 2001 type normal
```

```
speed-dial 1 2004 label "7960-1"
```

```
!
```

```
interface GigabitEthernet0/0
```

```
ip address 10.10.10.2 255.255.255.0
```

```
duplex auto
```

```
speed auto
```

```
ipv6 address 2000:A0A:201:0:F:35FF:FF2C:697D/64
```

```
ipv6 enable
```

```
interface GigabitEthernet0/1
```

```
ip address 40.10.30.1 255.255.255.0
```

```
shutdown
```

```
duplex auto
```

```
speed auto
```

```
ipv6 address 2000::1/64
```

```
ipv6 address 2000::2/64
```

```
ipv6 address 2000::A/64
```

```
ipv6 address 3000::1/64
```

```
ipv6 address 4000::1/64
```

```
ipv6 address 9000::1/64
```

```
ipv6 address F000::1/64
```

```
ipv6 enable
```

```
!
```

```
i!
```

```
!
```

```
!
```

```
ip http server
```

```
!
```

```
ipv6 route 2001:20:20:20::/64 2000:A0A:201:0:F:35FF:FF2C:5
```

```
ipv6 route 2001:50:50:50::/64 2000:A0A:201:0:F:35FF:FF2C:5
```

```
!
```

```
tftp-server flash:P00308000500.bin
```

```
tftp-server flash:P00308000500.loads
```

```
p-server flash:cvm70sccp.8-5-2FT1-18.sbn
```

```
!
```

```
!
```

```
voice-port 0/0/0:23
```

```
!
```

```
!
```

```
mgcp fax t38 ecm
```

```
!
```

```
sccp local GigabitEthernet0/0
```

```
sccp ccm 10.10.10.2 identifier 1 version 7.0
```

```
sccp ccm 2000:A0A:201:0:F:35FF:FF2C:697D identifier 2 version 7.0
```

```
sccp
```

```
!
```

```
!
```

```
gateway
```

```
timer receive-rtp 1200
```

```
!
```

```
sip-ua
```

```
protocol mode dual-stack preference ipv6
```

```
!
```

```
!
```

```
telephony-service
```

```
protocol mode dual-stack preference ipv6
```

```
sdspfarm conference mute-on 111 mute-off 222
```

```
sdspfarm units 2
```

```
sdspfarm transcode sessions 20
```

```
sdspfarm tag 1 xcoder
```

```
sdspfarm tag 2 conference
```

```
conference hardware
```

```
no auto-reg-ephone
```

```
em logout 0:0 0:0 0:0
```

```
max-ephones 52
```

```
max-dn 192
```

```
ip source-address 10.10.10.2 port 2000
```

```
ip source-address 2000:A0A:201:0:F:35FF:FF2C:697D
```

```
service phone settingsAccess 1
```

```
service phone spanTOPCPort 0
```

```
timeouts transfer-recall 15
```

```
system message MOTO-CME1
```

```
url directories http://10.10.10.2:80/localdirectory
```

```
cnf-file location flash:
```

```
cnf-file perphone
```

```
load 7914 S00103020003
```

```
load 7911 SCCP11.8-5-2FT1-18S
```

```
load 7970 SCCP70.8-5-2FT1-18S
```

```
time-zone 5
```

```
max-conferences 4 gain -6
```

```
call-forward pattern .T
```

```
web admin system name cisco password cisco
```

```
web admin customer name admin password admin
```

```
transfer-system full-consult
```

### Example for System-Level Parameters

The following example shows the system-level configuration for a
                                 		  Cisco Unified CME that can support up to 500 directory numbers on 100 phones.
                                 		  It sets up TFTP file sharing for phone firmware files for Cisco Unified IP
                                 		  Phones 7905, 7912, 7914, 7920, 7940, and 7960 and it loads those files.

```
tftp-server flash:ATA030100SCCP040211A.zup
```

```
! ATA 186/188 firmware
```

```
tftp-server flash:CP7902080001SCCP051117A.sbin
```

```
! 7902 firmware
```

```
tftp-server flash:CP7905080001SCCP051117A.sbin
```

```
! 7905 firmware
```

```
tftp-server flash:CP7912080001SCCP051117A.sbin
```

```
! 7912 firmware
```

```
tftp-server flash:cmterm_7920.4.0-02-00.bin
```

```
! 7914 firmware
```

```
tftp-server flash:P00503010100.bin
```

```
! 7920 firmware
```

```
tftp-server flash:S00104000100.sbn
```

```
! 7935 firmware
```

```
tftp-server flash:cmterm_7936.3-3-5-0.bin
```

```
! 7936 firmware
```

```
tftp-server flash:P0030702T023.bin
```

```
tftp-server flash:P0030702T023.loads
```

```
tftp-server flash:P0030702T023.sb2
```

```
! 7960/40 firmware
```

```
!
```

```
telephony-service
```

```
max-ephones 100
```

```
max-dn 500
```

```
load ata ATA030100SCCP040211A
```

```
load 7902 CP7902080001SCCP051117A
```

```
load 7905 CP7905080001SCCP051117A
```

```
load 7912 CP7912080001SCCP051117A
```

```
load 7914 S00104000100
```

```
load 7920 cmterm_7920.4.0-02-00
```

```
load 7935 P00503010100
```

```
load 7936 cmterm_7936.3-3-5-0
```

```
load 7960-7940 P0030702T023
```

```
ip source-address 10.16.32.144 port 2000
```

```
create cnf-files version-stamp Jan 01 2002 00:00:00
```

```
transfer-system full-consult
```

```
Cisco Unified IP Phone 7911, 7941, 7941-GE, 7961, 7961-GE, 7970, and 7971 require multiple files to be shared using TFTP. The following configuration example adds support for these phones.
```

```
tftp-server flash:SCCP11.7-2-1-0S.loads
```

```
tftp-server flash:term11.default.loads
```

```
tftp-server flash:apps11.1-0-0-72.sbn
```

```
tftp-server flash:cnu11.3-0-0-81.sbn
```

```
tftp-server flash:cvm11.7-2-0-66.sbn
```

```
tftp-server flash:dsp11.1-0-0-73.sbn
```

```
tftp-server flash:jar11.7-2-0-66.sbn
```

```
! 7911 firmware
```

```
!
```

```
tftp-server flash:TERM41.7-0-3-0S.loads
```

```
tftp-server flash:TERM41.DEFAULT.loads
```

```
tftp-server flash:TERM61.DEFAULT.loads
```

```
tftp-server flash:CVM41.2-0-2-26.sbn
```

```
tftp-server flash:cnu41.2-7-6-26.sbn
```

```
tftp-server flash:Jar41.2-9-2-26.sbn
```

```
! 7941/41-GE, 7961/61-GE firmware
```

```
!
```

```
tftp-server flash:TERM70.7-0-1-0s.LOADS
```

```
tftp-server flash:TERM70.DEFAULT.loads
```

```
tftp-server flash:TERM71.DEFAULT.loads
```

```
tftp-server flash:CVM70.2-0-2-26.sbn
```

```
tftp-server flash:cnu70.2-7-6-26.sbn
```

```
tftp-server flash:Jar70.2-9-2-26.sbn
```

```
! 7970/71 firmware
```

```
!
```

```
telephony-service
```

```
load 7911 SCCP11.7-2-1-0S
```

```
load 7941 TERM41.7-0-3-0S
```

```
load 7961 TERM41.7-0-3-0S
```

```
load 7941GE TERM41.7-0-3-0S
```

```
load 7961GE TERM41.7-0-3-0S
```

```
load 7970 TERM70.7-0-1-0s
```

```
load 7971 TERM70.7-0-1-0s
```

```
create cnf-files version-stamp Jan 01 2002 00:00:00
```

```
.
```

```
.
```

```
.
```

### Example for Blocking Automatic Registration

The following example shows how to disable automatic ephone
                                 		  registration, display a log of attempted registrations, and then clear the log:

```
Router(config)# telephony-service

Router(config-telephony)# no auto-reg-ephone

Router(config-telephony)# exit

Router(config)# exit

Router# show ephone attempted-registrations

Attempting Mac address:

Num Mac Address DateTime DeviceType

-----------------------------------------------------------------------------

1 C863.8475.5417 22:52:05 UTC Thu Apr 28 2005 SCCP Gateway (AN)

2 C863.8475.5408 22:52:05 UTC Thu Apr 28 2005 SCCP Gateway (AN)

.....

25 000D.28D7.7222 22:26:32 UTC Thu Apr 28 2005 Telecaster 7960

26 000D.BDB7.A9EA 22:25:59 UTC Thu Apr 28 2005 Telecaster 7960

...

47 C863.94A8.D40F 22:52:17 UTC Thu Apr 28 2005 SCCP Gateway (AN)

48 C863.94A8.D411 22:52:18 UTC Thu Apr 28 2005 SCCP Gateway (AN)

 

49 C863.94A8.D400 22:52:15 UTC Thu Apr 28 2005 SCCP Gateway (AN)

Router# clear telephony-service ephone-attempted-registrations
```

### Example for
                           	 Enabling the HFS Download Service for Cisco Unified SIP IP Phone

The following
                                 		  example shows how to enable the HFS download service:

```
Router(config)# ip http server
Router(config)# ip http port 1234
Router (config)# telephony-service
Router(config-telephony)# hfs enable port 65500
```

### Example for Configuring an HFS Home Path for Cisco Unified SIP IP
                           	 Phone Firmware Files

The following example shows how a new directory called phone-load can
                                 		  be created under the root directory of the flash memory and set as the hfs
                                 		  home-path:

```
cassini-c2801# mkdir flash:phone-loads Create directory filename [phone-loads]? Created dir flash:phone-loads cassini-c2801#sh flash: -#- --length-- -----date/time------ path 1     13932728 Mar 22 2007 15:57:38 +00:00 c2801-ipbase-mz.124-1c.bin 2     33510140 Sep 18 2010 01:21:56 +00:00 rootfs9951.9-0-3.sebn 3       143604 Sep 18 2010 01:22:20 +00:00 sboot9951.111909R1-9-0-3.sebn 4         1249 Sep 18 2010 01:22:40 +00:00 sip9951.9-0-3.loads 5        66996 Sep 18 2010 01:23:00 +00:00 skern9951.022809R2-9-0-3.sebn 6        10724 Sep 18 2010 00:59:48 +00:00 dkern9951.100609R2-9-0-3.sebn 7      1507064 Sep 18 2010 01:00:24 +00:00 kern9951.9-0-3.sebn 8            0 Jan 5 2011 02:03:46 +00:00 phone-loads 14819328 bytes available (49192960 bytes used) cassini-c2801#conf t Enter configuration commands, one per line.  End with CNTL/Z. cassini-c2801(config)#tele cassini-c2801(config)#telephony-service cassini-c2801(config-telephony)#hfs hom cassini-c2801(config-telephony)#hfs home-path flash:? WORD cassini-c2801(config-telephony)# hfs home-path flash:phone-loads cassini-c2801(config-telephony)#
```

### Example for Verifying the HFS File Bindings of Cisco Unified SIP IP
                           	 Phone Configuration and Firmware Files

The following is a sample output from the show voice register hfs command:

```
Router(config)# show voice register hfs Fetch Service Enabled = Y App enabled port = 6970 Use default port = N Registered session-id = 19 Default home path = flash:/ Ongoing fetches from home = 0 HTTP File Server Bindings No. of bindings = 11 No. of url table entries = 9
```

No. of alias table entries = 9

### Example for
                           	 Redundant Router for SCCP Phones

The following
                                 		  example is configured on the primary Cisco Unified CME router. It establishes
                                 		  the router at 10.5.2.78 as a secondary router. The voice port 3/0/0 is the FXO
                                 		  port for incoming calls from the PSTN. It is set to use ground-start signaling
                                 		  and to detect incoming calls by counting incoming ring signals.

```
telephony-service
```

```
ip source-address 10.0.0.1 port 2000 secondary 10.5.2.78
```

```
voice-port 3/0/0
```

```
signal ground-start
```

```
incoming alerting ring-only
```

The secondary
                                 		  Cisco Unified CME router is configured with the same commands, except that the
                                 		  ring number command is set to 3 instead of using the default of 1.

```
telephony-service
```

```
ip source-address 10.0.0.1 port 2000 secondary 10.5.2.78
```

```
voice-port 3/0/0
```

```
signal ground-start
```

```
incoming alerting ring-only
```

```
ring number 3
```

### Example for
                           	 Redundant Router for SIP Phones

The following
                                 		  example is configured on the primary Cisco Unified CME router. It establishes
                                 		  the router at 10.6.50.6 as a secondary router with keepalive value set to 200
                                 		  seconds.

For the synchronization to happen, additional configurations are
                                             			 needed. These configurations such as IXI, HTTP, and telephony-service are
                                             			 provided in the output.

```
voice register global
 source-address 10.6.21.4 port 6000 secondary 10.6.50.6
 keepalive 200

ip http server

ixi transport http
 response size 8
 no shutdown
 request outstanding 2
 request timeout 30

ixi application cme
 no shutdown
 response timeout -1

telephony-service
 ip source-address 10.6.21.4 secondary 10.6.50.6
 standby user cisco password cisco123
```

The secondary
                                 		  Cisco Unified CME router is configured with the same commands:

```
voice register global
 source-address 10.6.21.4 port 6000 secondary 10.6.50.6
 keepalive 200

ip http server

ixi transport http
 response size 8
 no shutdown
 request outstanding 2
 request timeout 30

ixi application cme
 no shutdown
 response timeout -1

telephony-service
 ip source-address 10.6.50.6
 xml user cisco password cisco123 15
```

### Example for Media Flow Around Mode for SIP Trunks

The following example shows media flow-around enabled in voice service voip, voice class media, and dial peer configuration
                                 modes:

```
Router# show running config

!

!

voice service voip

ip address trusted list

ipv4 20.20.20.1

media flow-around

allow-connections sip to sip

vpn-group 1

vpn-gateway 1 https://9.10.60.254/SSLVPNphone

vpn-trustpoint 1 trustpoint cme_cert root

vpn-hash-algorithm sha-1

vpn-profile 1

keepalive 50

auto-network-detect enable

host-id-check disable

vpn-profile 2

mtu 1300

authen-method both

password-persistent enable

host-id-check enable

vpn-profile 4

fail-connect-time 50

sip

!

voice class media 10

media flow-around

!

!

!

dspfarm profile 1 conference

codec g711ulaw

maximum sessions 2

associate application SCCP

!

dial-peer voice 222 voip

media flow-around

!

dial-peer voice 10 voip

media flow-around

!

dial-peer voice 101 voip

end
```

### Example for Configuring Overlap Dialing for SCCP IP Phones

The following example shows the overlap-signal command configured in
                                 		  telephony-service configuration mode, ephone template 10, and ephone 10:

```
The following example shows the overlap-signal command configured in telephony-service configuration mode, ephone template 10, and ephone 10:

Router# show running config

!

!

telephony-service

max-ephones 25

max-dn 15

load 7906 SCCP11.8-5-3S.loads

load 7911 SCCP11.8-5-3S.loads

load 7921 CP7921G-1.3.3.LOADS

load 7941 SCCP41.8-5-3S.loads

load 7942 SCCP42.8-5-3S.loads

load 7961 SCCP41.8-5-3S.loads

load 7962 SCCP42.8-5-3S.loads

max-conferences 12 gain -6

web admin system name cisco password cisco

transfer-system full-consult

create cnf-files version-stamp Jan 01 2002 00:00:00

overlap-signal

!

ephone-template 1

button-layout 1 line

button-layout 3-6 blf-speed-dial

!

ephone-template 9

feature-button 1 Endcall

feature-button 3 Mobility

!

!

ephone-template 10

feature-button 1 Park

feature-button 2 MeetMe

feature-button 3 CallBack

button-layout 1 line

button-layout 2-4 speed-dial

button-layout 5-6 blf-speed-dial

overlap-signal

!

ephone 10

device-security-mode none

mac-address 02EA.EAEA.0010

overlap-signal
```

### Example for Configuring Overlap Dialing for SIP IP Phones

The following example shows the overlap-signal configured in voice register global configuration mode and voice register pool 10:

```
Router# show running config

!

!

!

voice service voip

ip address trusted list

ipv4 20.20.20.1

media flow-around

allow-connections sip to sip

!

voice class media 10

media flow-around

!

!

voice register global

max-pool 10

overlap-signal

!

voice register pool 5

overlap-signal

!

!

!
```

## Where to Go Next

After configuring system-level parameters, you are ready to configure phones for making basic calls in Cisco Unified CME.

To use Extension Assigner to assign extension numbers to the phones in your Cisco Unified CME, see Create Phone Configurations Using Extension Assigner .

Otherwise, see Configure Phones to Make Basic Call .

## Feature
                        	 Information for System-Level Parameters

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Versions

Feature
                                          					 Information

Redundant Router for SIP Phones

11.6

Introduces redundant router support for SIP phones.

Unsolicited Notify for Shared Line and Presence Events for Cisco
                                          					 Unified SIP IP Phones

9.0

Allows the
                                          					 Unsolicited Notify mechanism to reduce network traffic during Cisco Unified SIP
                                          					 IP phone registration using the bulk registration method.

HFS
                                          					 Download Support for IP Phone Firmware and Configuration Files

8.8

Provides
                                          					 download support for SIP and SCCP IP phone firmware, scripts, midlets, and
                                          					 configuration files using the HTTP File-Fetch Server (HFS) infrastructure.

Bulk
                                          					 Registration

8.6/3.4

Introduces
                                          					 bulk registration support for SIP phones. Introduces bulk registration for
                                          					 registering a block of phone numbers with an external registrar.

Media Flow
                                          					 Around for SIP-SIP Trunks

8.5

Introduces
                                          					 the media flow around feature, which eliminates the need to terminate RTP and
                                          					 re-originate on Cisco Unified CME, reducing media switching latency and
                                          					 increasing the call handling capacity for Cisco Unified CME SIP trunk.

Overlap Dialing for SCCP and SIP Phones

8.5

Allows the dialed digits from the SIP or SCCP IP phones to pass across the PRI/BRI trunks as overlap digits and not as enbloc
                                          digits, enabling overlap dialing on the PRI/BRI trunks.

DSCP

7.1

Supports
                                          					 DSCP packet marking for Cisco Unified IP Phones to specify the class of service
                                          					 for each packet.

Maximum
                                          					 Ephones

7.0/4.3

The max-ephones command sets the maximum number of SCCP phones that can
                                          					 register to Cisco Unified CME, without limiting the number that can be
                                          					 configured. Maximum number of phones that can be configured is 1000.

Network
                                          					 Time Protocol for SIP Phones

4.1

Allows SIP
                                          					 phones to synchronize to an NTP server.

Blocking
                                          					 Automatic Registration

4.0

Blocks IP
                                          					 phones that are not explicitly configured in Cisco Unified CME from
                                          					 registering.

Per-Phone
                                          					 Configuration Files and Alternate Location

4.0

Defines a
                                          					 location other than system for storing configuration files and specifies the
                                          					 type of configuration files to generate.

Redundant
                                          					 Router for SCCP Phones

4.0

Introduces
                                          					 redundant router capability.

SIP phones
                                          					 in Cisco Unified CME

3.4

Introduces
                                          					 support for SIP endpoints directly connected to Cisco Unified CME.

| Note | The bulk
                                       		registration feature in Cisco Unified CME 8.6 optimizes line registration on
                                       		SIP phones and is a phone interop feature. The bulk registration feature is not
                                       		related to the bulk command
                                       		under voice register global configuration mode. |
|---|---|

| Transactions | Method | Messages Per
                                          				  Transaction | Number of
                                          				  Transactions | Total number
                                          				  of messages (per line) | Total number
                                          				  of messages (bulk) |
|---|---|---|---|---|---|
| Register | REGISTER | 2 | 8 | 24 | 3 |
| Phone Status
                                          				  Update | REFER
                                          				  remotecc NOTIFY (mwi,
                                          				  service-control) | 2 2 | 3 8 | 6 16 | 2 |
| Subscription | SUBSCRIBE
                                          				  (sharedline) | 4 | 8 | 32 | 32 |
| Total |  |  |  | 78 | 37 |

| Status | Default | Initialization |
|---|---|---|
| CallForwardAll Update | No default | Always send regardless of the value |
| Privacyrequest | Disabled | Only send if the value is not equal to the default |
| DnDupdate | Disabled | Only send if value is not equal to the default |
| Bulkupdate (MWI) | No default | Always send regardless of value |

| Note | Cisco Unified IP phones use the TCP for registration refresh. TCP socket has a default keepalive time out session of 60 minutes.
                                          If registration refresh to Cisco Unified CME does not takes place within an hour (60 minutes), the TCP connection will be
                                          removed. This will make the phones restart instead of refresh. To stop the phones from restarting, adjust the registrar expire
                                          timer under voice service voip or set the timer connection aging under sip-ua to a value greater than what the phone uses
                                          for registration refreshes. For example, if the phone does a registration refresh every 60 minutes, then setting up a timer
                                          connection aging to 100 minutes will guarantee that the TCP keeps the connection open. Or you can set the registrar expire
                                          maximum value to less than 3600. |
|---|---|

| Note | For Cisco Integrated Services Router 4351, you can set the
                                       		max-ephones value to 3925. For Cisco Integrated Services Router 4331, you can
                                       		set the max-ephones value to 2921. For Cisco Integrated Services Router 4321,
                                       		you can set the max-ephones value to 2901. For Cisco Integrated Services Router
                                       		4400 series, you can set the max-ephones value to 4451. |
|---|---|

| Note | When the storage
                                       		location you selected is flash memory and the file system type on this device
                                       		is Class B (LEFS), you must check the free space on the device periodically and
                                       		use the squeeze command to free the space used up by deleted files. Unless you use the squeeze command, the space used by the moved or deleted configuration files cannot be
                                       		used by other files. Rewriting flash memory space during the squeeze operation
                                       		may take several minutes. We recommend that you use this command during
                                       		scheduled maintenance periods or off-peak hours. |
|---|---|

| Note | When the HFS download service is not configured, SIP phones
                                          		automatically access the TFTP server. |
|---|---|

| Note | The configuration files are shared by the HTTP and TFTP servers.
                                          		However, the firmware files are different for each server. |
|---|---|

| Note | If the entered
                                             		custom HFS port clashes with the underlying IP HTTP port, an error message is
                                             		displayed and the command is disallowed. |
|---|---|

| Note | Because IP phones
                                             		are hardcoded to use port 6970 to connect to Cisco Unified CME, you must search
                                             		for other applications running on port 6970 and assign them with ports
                                             		different from 6970 to prevent a failure in connecting to Cisco Unified CME. |
|---|---|

| Restriction | Due to lack of High
                                             			 Availability support, Stateful Swtichover or preservation of active calls is
                                             			 not supported in the redundancy feature offered by Unified CME. The physical setup for redundant Cisco Unified CME routers only
                                                				support Loop start signaling. The Ground start signaling is not supported. |
|---|---|

| Restriction | Due to lack of High Availability support, Stateful Swtichover or preservation of active calls is not supported in the redundancy
                                                feature offered by Unified CME. |
|---|---|

| Note | You must disable Alternative Network Address Transport (ANAT)
                                       		globally for SIP lines if you have a Cisco Unified CME with a dual-stack SIP
                                       		trunk and enable ANAT at dial-peer level for the SIP trunk. |
|---|---|

| IP Versions | IPv4 Only | IPv6 Only | Dual-Stack |
|---|---|---|---|
| IPv4 Only | Flow Around 1 | Flow Through | Flow Around |
| IPv6 Only | Flow Through | Flow Around | Flow Around/IPv6 |
| Dual-Stack | Flow Around/IPv4 | Flow Around/IPv6 | Flow Around/Preference |

| Note | Configuring TCP
                                       		as the transport layer protocol under voice register pool configuration mode
                                       		enables bulk registration with negotiation for the Unsolicited Notify
                                       		mechanism. |
|---|---|

| Restriction | Because Unsolicited Notify
                                             			 is negotiated during bulk registration, the mechanism is not available on Cisco
                                             			 Unified SIP IP phones that do not have bulk registration turned on or have
                                             			 firmware that do not support bulk registration. Cisco Unified CME cannot
                                             			 disable the Unsolicited Notify mechanism. The system complies with and cannot
                                             			 override the requests of Cisco Unified SIP IP phones. In the absence of Cisco Unified SIP IP
                                             			 phone subscription information to distinguish if a notification event is for
                                             			 line or device monitoring, local device monitoring is not supported in the
                                             			 Unsolicited Notify mode. |
|---|---|

| Restriction | Legacy IP phones are not supported. Multicast MOH and multicast paging features are not supported on IPv6 only phones. If you want to receive paging calls on
                                                   IPv6 enabled phones, use the default multicast paging. Primary and secondary CME need to be provisioned with the same network type. MWI relay server must be in IPv4 network. Presence server must be IPv4 only. Video endpoints, such as CUVA and 7985, are not supported in IPv6 TAPI client is not supported in IPv6. All HTTP based IPv6 services are not supported. IOS TFTP server is not supported in IPv6. If protocol mode is IPv4, you can only configure IPv4 as the source IP-address, if protocol mode is IPv6 you can only configure
                                                   IPv6 as the source IP address and if the protocol mode is dual-stack, you can configure both IPv4 and IPv6 source addresses. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | protocol mode { ipv4 \| ipv6 \| dual-stack [ preference { ipv4 \| ipv6 }]} Example: Router(config-telephony)# protocol mode dual-stack preference ipv6 | Allows SCCP phones to interact with phones on IPv6 voice gateways.
                                             				You can configure phones for IPv4 addresses, IPv6 address es, or for a
                                             				dual-stack mode ipv4 —Allows you to set the protocol mode as an IPv4 address. ipv6 —Allows you to set the protocol mode as an IPv6 address. dual-stack— Allows you to set the protocol mode for both IPv4 and IPv6 addresses. preference —Allows you to choose a preferred IP address family if protocol mode is dual-stack. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to privileged EXEC mode. |

| Restriction | IPv6 option only appears if
                                                				protocol mode is in dual-stack or IPv6. Do not change the default
                                                				port number (2000) in the ip
                                                   				  source-address configuration command. If you change the port number, IPv6
                                                				CEF packet switching engine may not be able to handle the IPv6 SCCP phones and
                                                				various packet handling problems may occur. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters the
                                             				telephony-service configuration mode. |
| Step 4 | ip
                                                				  source-address { ipv4 address \| ipv6
                                                				  address } port port [ secondary { ipv4 address \| ipv6
                                                				  address } [ rehome seconds ]]
                                          			 [ strict-match ] Example: Router(config-telephony)# ip source-address 10.10.10.33 port 2000 ip source-address 2001:10:10:10:: | Allows to
                                             				configure an IPv4 or IPv6 address as an IP source-address for phones to
                                             				communicate with a Cisco Unified CME router. ipv4 address —Allows phones to communicate with
                                                				  phones or voice gateways in an IPv4 network. ipv4 address can only be configured with an IPv4 address or a dual-stack mode. ipv6 address —Allows phones to communicate with
                                                				  phones or voice gateways in an IPv6 network. ipv6 address can only be configured with an IPv6 address or a dual-stack mode. (Optional) port port —TCP/IP
                                                				  port number to use for SCCP. Range is from 2000 to 9999. Default is 2000. For
                                                				  dual-stack, port is only configured with an IPv4 address. (Optional) secondary —Cisco Unified CME router with which
                                                				  phones can register if the primary Cisco Unified CME router fails. (Optional) rehome seconds —Used
                                                				  only by Cisco Unified IP phones that have registered with a Cisco Unified
                                                				  Survivable Remote Site Telephony (SRST) router. This keyword defines a delay
                                                				  that is used by phones to verify the stability of their primary SCCP controller
                                                				  (Cisco Unified Communication Manager or Cisco Unified CME) before the phones
                                                				  re-register with it. This parameter is ignored by phones unless they are
                                                				  registered to a secondary Cisco Unified SRST router. The range is from 0 to
                                                				  65535 seconds. The default is 120 seconds. The use of
                                             				this parameter is a phone behavior and is subject to change, based on the phone
                                             				type and phone firmware version. (Optional) strict-match —
                                                				  Requires strict IP address checking for registration. |
| Step 5 | end Example: outer(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | The following example shows a list of success messages that are printed during Cisco IOS boot up. These messages confirm whether
                                          IPv6 has been enabled on interfaces (for example, EDSP0.1 to EDSP0.5) specific to exchanging RTP packets with SCCP endpoints. Example: Router#
00:00:33: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.1 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.2 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.3 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.4 added.
00:00:34: %EDSP-6-IPV6_ENABLED: IPv6 on interface EDSP0.5 added.
00:00:34: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to down
00:00:34: %LINK-3-UPDOWN: Interface ephone_dsp DN 1.1, changed state to up
00:00:34: %LINK-3-UPDOWN: Interface ephone_dsp DN 1.2, changed state to up 
. |
|---|---|
| Step 2 | Use the show ephone socket command to verify if IPv4 only, IPv6 only, or dual-stack (IPv4/IPv6) is configured in Cisco Unified CME. In the following
                                          example, SCCP TCP listening socket (skinny_tcp_listen_socket fd) values 0 and 1 verify dual-stack configuration. When IPv6
                                          only is configured, the show ephone socket command displays SCCP TCP listening socket values as (-1) and (0). The listening socket is closed if the value is (-1). When
                                          IPv4 only is configured, the show ephone socket command displays SCCP TCP listening socket values as (0) and (-1). Example: Router# show ephone socket skinny_tcp_listen_socket fd = 0

skinny_tcp_listen_socket (ipv6) fd = 1

skinny_secure_tcp_listen_socket fd = -1

skinny_secure_tcp_listen_socket (ipv6) fd = -1

Phone 7,

skinny_sockets[15] fd = 16 [ipv6]

read_buffer 0x483C0BC4, read_offset 0, read_header N, read_length 0

resend_queue 0x47EC69EC, resend_offset 0, resend_flag N, resend_Q_depth 0

MTP 1,

skinny_sockets[16] fd = 17

read_buffer 0x483C1400, read_offset 0, read_header N, read_length 0

resend_queue 0x47EC6978, resend_offset 0, resend_flag N, resend_Q_depth 0

Phone 8,

skinny_sockets[17] fd = 18 [ipv6]

read_buffer 0x483C1C3C, read_offset 0, read_header N, read_length 0

resend_queue 0x47EC6904, resend_offset 0, resend_flag N, resend_Q_depth 0 |
| Step 3 | Use the show ephone summary command to verify the IPv6 or IPv4 addresses configured for ephones. The following example displays IPv6 and IPv4 addresses
                                          for different ephones: Example: Router# show ephone summary 
ephone-2[1] Mac:0016.46E0.796A TCP socket:[7] activeLine:0 whisperLine:0 REGISTERED

mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0 privacy:1 primary_dn: 1*

IPv6:2000:A0A:201:0:216:46FF:FEE0:796A* IP:10.10.10.12 7970 keepalive 599 music 0 1:1

sp1:2004

ephone-7[6] Mac:0013.19D1.F8A2 TCP socket:[6] activeLine:0 whisperLine:0 REGISTERED

mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0 privacy:0 primary_dn: 13*

IP:10.10.10.14 * Telecaster 7940 keepalive 2817 music 0 1:13 2:28 |

| Note | Use the no reg command to specify that an individual directory number should not register with
                                          		  the external registrar. For configuration information, see Disable SIP Proxy Registration for a Directory Number . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                          			 privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                          			 configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                          			 register global configuration mode to set parameters for all supported SIP
                                          			 phones in Cisco Unified CME. |
| Step 4 | mode cme Example: Router(config-register-global)# mode cme | Enables mode
                                          			 for provisioning SIP phones in Cisco Unified CME. |
| Step 5 | bulk number Example: Router(config-register-global)# bulk 408526.... | Sets bulk
                                          			 registration for E.164 numbers that will register with a SIP proxy server. number —Unique sequence of up to 32 characters,
                                                   					 including wild cards and patterns that represents E.164 numbers that will
                                                   					 register with a SIP proxy server. |
| Step 6 | exit Example: Router(config-register-pool)# exit | Exits
                                          			 configuration mode to the next highest mode in the configuration mode
                                          			 hierarchy. |
| Step 7 | sip-ua Example: Router(config)# sip-ua | Enters SIP
                                          			 user agent (UA) configuration mode for configuring the user agent. |
| Step 8 | registrar { dns : address \| ipv4 : destination-address } expires seconds [ tcp ] [ secondary ] no registrar [ secondary ] Example: Router(config-sip-ua)# registrar server ipv4:1.5.49.240 | Enables SIP
                                          			 gateways to register E.164 numbers with a SIP proxy server. |
| Step 9 | end Example: Router(config-sip-ua)# end | Exits SIP UA
                                          			 configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool tag Example: Router(config)#voice register pool 20 | Enters voice register dn configuration mode to define a directory
                                          			 number for a SIP phone, intercom line, voice port, or an MWI. |
| Step 4 | session-transport { tcp \| udp } Example: Router(config-register-pool)#session-transport tcp | Specifies the transport layer protocol that a SIP phone uses to
                                          			 connect to Cisco Unified CME. tcp —TCP is
                                                				  used for bulk registration. udp —UDP is
                                                				  used for line registration. |
| Step 5 | number tag dn tag Example: Router(config-register-pool)#number 1 dn 2 | Associates a directory number with the SIP phone being
                                          			 configured. dn dn-tag —Identifies the directory number
                                                				  for this SIP phone as defined by the voice register dn command. |
| Step 6 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |

| Restriction | DSCP requires Cisco Unified CME 7.1 or a later version. If DSCP is configured for the gateway interface using the service-policy command or for the dial peer using the ip qos dscp command, the value set with those commands takes precedence over the DSCP
                                          value configured in this procedure. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | tftp-server device : filename Example: Router(config)# tftp-server flash:P00307020300.bin | (Optional) Creates TFTP bindings to permit IP phones served by
                                          			 the Cisco Unified CME router to access the specified file. A separate tftp-server command is required for each phone type. Required for Cisco Unified CME 7.0/4.3 and earlier versions. Cisco Unified CME 7.0(1) and later versions: Required only if the location for cnf files is not flash or slot 0, such as system
                                                   memory or a TFTP server url. Use the complete filename, including the file suffix, for phone firmware versions later than
                                                   version 8.2(2) for all phone types. |
| Step 4 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 5 | load phone-type firmware-file Example: Router(config-telephony)# load 7960-7940 P00307020300 | Identifies a Cisco Unified IP phone firmware file to be used by
                                          			 phones of the specified type when they register. A separate load command is required for each IP phone type. firmware-file—Filename is case-sensitive. Cisco Unified CME 7.0/4.3 and earlier versions: Do not use the .sbin or .loads file extension except for the Cisco ATA and
                                                         Cisco Unified IP Phone 7905 and 7912. Cisco Unified CME 7.0(1) and later versions: Use the complete filename, including the file suffix, for phone firmware versions
                                                         later than version 8.2(2) for all phone types. Note If you are loading a firmware file larger than 384 KB, you must
                                                      				first load a file for that phone type that is smaller than 384 KB and then load
                                                      				the larger file. | Note | If you are loading a firmware file larger than 384 KB, you must
                                                      				first load a file for that phone type that is smaller than 384 KB and then load
                                                      				the larger file. |
| Note | If you are loading a firmware file larger than 384 KB, you must
                                                      				first load a file for that phone type that is smaller than 384 KB and then load
                                                      				the larger file. |
| Step 6 | max-ephones max-phones Example: Router(config-telephony)# max-ephones 24 | Sets the maximum number of phones that can register to Cisco
                                          			 Unified CME. Maximum number is platform and version-specific. Type ? for range. In Cisco Unified CME 7.0/4.3 and later versions, the maximum number of phones that can register is different from the maximum
                                                   number of phones that can be configured. The maximum number of phones that can be configured is 1000. In versions earlier than Cisco Unified CME 7.0/4.3, this command restricted the number of phones that could be configured
                                                   on the router. |
| Step 7 | max-dn max-directory - numbers [ preference preference-order ]
                                          			 [ no-reg primary \| both ] Example: Router(config-telephony)# max-dn 200 no-reg primary | Limits number of directory numbers to be supported by this
                                          			 router. Maximum number is platform and version-specific. Type ? for value. |
| Step 8 | ip source-address ip-address [ port port ] [ any-match \| strict-match ] Example: Router(config-telephony)# ip source-address 10.16.32.144 | Identifies the IP address and port number that the Cisco Unified
                                          			 CME router uses for IP phone registration. port port —(Optional) TCP/IP port number to use for SCCP. Range is 2000 to 9999. Default is 2000. any-match —(Optional) Disables strict IP address checking for registration. This is the default. strict-match —(Optional) Instructs the router to reject IP phone registration attempts if the IP server address used by the phone does
                                                   not exactly match the source address. |
| Step 9 | ip qos dscp {{ number \| af \| cs \| default \| ef } { media \| service \| signaling \| video }} Example: Router(config-telephony)# ip qos dscp af43 video | Sets the DSCP priority levels for different types of traffic. |
| Step 10 | end Example: Router(config-telephony)# end | Returns to privileged EXEC mode. |

| Note | If you are loading a firmware file larger than 384 KB, you must
                                                      				first load a file for that phone type that is smaller than 384 KB and then load
                                                      				the larger file. |
|---|---|

| Note | For certain phones, such as the Cisco Unified IP Phones 7906, 7911, 7931, 7941, 7942, 7945, 7961, 7962, 7965, 7970, 7971,
                                          and 7975, you must configure the time-zone command to ensure that the correct time stamp appears on the phone display. This command is not required for Cisco Unified IP Phone
                                          7902G, 7905G, 7912G, 7920, 7921, 7935, 7936, 7940, 7960, or 7985G. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | date-format { dd-mm-yy \| mm-dd-yy \| yy-dd-mm \| yy-mm-dd } Example: Router(config-telephony)# date-format yy-mm-dd | (Optional) Sets the date format for phone display. Default: mm-dd-yy . |
| Step 5 | time-format { 12 \| 24 } Example: Router(config-telephony)# time-format 24 | (Optional) Selects a 12-hour or 24-hour clock for the time display
                                             				format on phone display. Default: 12 . |
| Step 6 | time-zone number Example: Router(config-telephony)# time-zone 2 | Sets time zone for SCCP phones. Not required for Cisco Unified IP Phone 7902G, 7905G, 7912G,
                                                				  7920, 7921, 7935, 7936, 7940, 7960, or 7985G. Default: 5, Pacific Standard/Daylight Time (-480). |
| Step 7 | end Example: Router(config-telephony)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                          			 privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                          			 configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                          			 telephony-service configuration mode. |
| Step 4 | no auto-reg-ephone Example: Router(config-telephony)# no auto-reg-ephone | Disables
                                          			 automatic registration of Cisco Unified IP phones that are running SCCP but are
                                          			 not explicitly configured in Cisco Unified CME. Default:
                                                   					 Enabled. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                          			 privileged EXEC mode. |

| Restriction | TFTP does not support file deletion. When configuration files are updated, they overwrite any existing configuration files
                                                   with the same name. If you change the configuration file location, files are not deleted from the TFTP server. Generating configuration files on flash memory or slot 0 memory can take up to a minute, depending on the number of files
                                                   being generated. For smaller routers such as the Cisco 2600 series routers, you must manually enter the squeeze command to erase files after changing the configuration file location or entering any commands that trigger the deletion
                                                   of configuration files. Unless you use the squeeze command, the space used by the moved or deleted configuration files is not usable by other files. If VRF Support on Cisco Unified CME is configured and the cnf-file location command is configured for system:, the per phone or per phone type file for an ephone in a VRF group is created in system:/its/vrf<group-tag>/ . The vrf directory is automatically created and appended to the TFTP path. No action is required on your part. Locale files
                                                   are still created in system:/its/. If VRF Support on Cisco Unified CME is configured and the cnf-file location command is configured as flash: or slot0: , the per phone or per phone type file for an ephone in a VRF group is named flash:/its/vrf<group-tag>_<filename> or slot0:/its/vrf<group-tag>_filename> . The vrf directory is automatically created and appended to the TFTP path. No action is required on your part. The location
                                                   of the locale files is not changed. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | cnf-file location { flash: \| slot0: \| tftp tftp-url } Example: Router(config-telephony)# cnf-file location flash: | Specifies a location other than system:/its for storing phone
                                             				configuration files. Required for per-phone or per-phone type configuration files. |
| Step 5 | cnf-file { perphonetype \| perphone } Example: Router(config-telephony)# cnf-file perphone | Specifies whether to use a separate file for each type of phone or
                                             				for each individual phone. Required if you configured the cnf-file location command. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | timeouts busy seconds Example: Router(config-telephony)# timeouts busy 20 | (Optional) Sets the length of time after which calls that are transferred to busy destinations are disconnected. seconds —Number of seconds. Range is 0 to 30. Default is 10. |
| Step 5 | timeouts interdigit seconds Example: Router(config-telephony)# timeouts interdigit 30 | (Optional) Configures the interdigit timeout value for all Cisco Unified IP phones attached to the router. seconds —Number of seconds before the interdigit timer expires. Range is 2 to 120. Default is 10. |
| Step 6 | timeouts ringing seconds Example: Router(config-telephony)# timeouts ringing 30 | (Optional) Sets the duration, in seconds, for which the Cisco Unified CME system allows ringing to continue if a call is not
                                             answered. Range is 5 to 60000. Default is 180. |
| Step 7 | keepalive seconds Example: Router(config-telephony)# keepalive 45 | (Optional) Sets the time interval, in seconds, between keepalive
                                             				messages that are sent to the router by Cisco Unified IP phones. The default is usually adequate. If the interval is set too large, it is possible for notification to be delayed when a system
                                                   goes down. Range: 10 to 65535. Default: 0. |
| Step 8 | end Example: Router(config-telephony)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | ip source-address ip-address [ port port ] [ secondary ip-address [ rehome seconds ]] [ any-match \| strict-match ] Example: Router(config-telephony)# ip source-address 10.0.0.1 port 2000 secondary 10.2.2.25 | Identifies the
                                             				IP address and port number that the primary Unified CME router uses for IP
                                             				phone registration. ip-address —Address of the primary Unified CME
                                                				  router. port port —(Optional) TCP/IP port number to use for
                                                				  SCCP. Range is 2000 to 9999. Default is 2000. secondary ip-address —Indicates a backup Unified CME router. rehome seconds —Not
                                                				  used by Unified CME. Used only by phones registered to Cisco Unified SRST. any-match —(Optional) Disables strict IP address
                                                				  checking for registration. This is the default. strict-match —(Optional) Router rejects IP phone
                                                				  registration attempts if the IP server address used by the phone does not
                                                				  exactly match the source address. |
| Step 5 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 6 | voice-port slot-number / port Example: Router(config)# voice-port 2/0 | Enters
                                             				voice-port configuration mode for the FXO voice port for DID calls from the
                                             				PSTN. |
| Step 7 | signal ground-start Example: Router(config-voiceport)# signal ground-start | Specifies
                                             				ground-start signaling for a voice port. |
| Step 8 | incoming alerting
                                             				ring-only Example: Router(config-voiceport)# incoming alerting ring-only | Instructs
                                             				the FXO ground-start voice port to detect incoming calls by detecting incoming
                                             				ring signals. |
| Step 9 | ring number number Example: Router(config-voiceport)# ring number 3 | (Required
                                             				only for the secondary router) Sets the maximum number of rings to be detected
                                             				before answering an incoming call over an FXO voice port. number —Number of rings detected before answering
                                                   					 the call. Range is 1 to 10. Default is 1. Note For an
                                                      				incoming FXO voice port on a secondary Cisco Unified CME router, set this value
                                                      				higher than is set on the primary router. We recommend setting this value to 3
                                                      				on the secondary router. | Note | For an
                                                      				incoming FXO voice port on a secondary Cisco Unified CME router, set this value
                                                      				higher than is set on the primary router. We recommend setting this value to 3
                                                      				on the secondary router. |
| Note | For an
                                                      				incoming FXO voice port on a secondary Cisco Unified CME router, set this value
                                                      				higher than is set on the primary router. We recommend setting this value to 3
                                                      				on the secondary router. |
| Step 10 | end Example: Router(config-voiceport)# end | Returns to
                                             				privileged EXEC mode. |

| Note | For an
                                                      				incoming FXO voice port on a secondary Cisco Unified CME router, set this value
                                                      				higher than is set on the primary router. We recommend setting this value to 3
                                                      				on the secondary router. |
|---|---|

| Note | It is
                                                   				  recommended to configure the XML interface for a seamless failover from primary
                                                   				  to secondary Cisco Unified CME. Else, there is delay in the phones getting
                                                   				  registered to secondary Cisco Unified CME due to mismatch in the configuration
                                                   				  version timestamp. |
|---|---|

| Note | It is
                                                   				  recommended to configure version stamp synchronization for a seamless failover
                                                   				  from primary to secondary Cisco Unified CME. Else, there is delay in the phones
                                                   				  getting registered to secondary Cisco Unified CME. |
|---|---|

| Restriction | Active calls
                                                   				  are not supported when switchover happens from primary router to the secondary
                                                   				  router. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode. |
| Step 4 | source-address ip-address [ port port ] [ secondary ip-address ] Example: Router(config-register-global)# source-address 10.6.21.4 port 6000 secondary 10.6.50.6 | Identifies the
                                             				IP address and port number that the Cisco Unified CME router uses for IP phone
                                             				registration. ip-address —Address of the primary
                                                				  Cisco Unified CME router. port port —(Optional) TCP/IP port number to use for SIP.
                                                				  Range is 2000 to 9999. Default is 5060 for SIP. secondary ip-address —Indicates a backup Cisco Unified CME
                                                				  router. |
| Step 5 | keepalive seconds Example: Router(config-register-global)# keepalive 200 | Sets the
                                             				length of the time interval between successive keepalive messages from the SIP
                                             				phones to Cisco Unified CME router. Default is 120 seconds. |
| Step 6 | end Example: Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

| Tip | All
                                             			 phone-related configurations are tagged with a 'version stamp' that indicates
                                             			 when the last configuration change was made. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                          			 telephony service configuration mode. |
| Step 4 | standby
                                                				  username username password password Example: Router(config-telephony)# standby username user23 password 3Rs92uzQ | Defines an
                                             				authorized user. Same username and password that is defined in Configure the XML Interface for the Secondary Backup Router . |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Automatic
                                                   				  synchronization for new or replacement routers is not supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                          			 telephony service configuration mode. |
| Step 4 | xml user user-name password password
                                                				  privilege-level Example: Router(config-telephony)# xml user user23 password 3Rs92uzQ 15 | Defines an
                                             				authorized user. user-name —Username of the authorized user. password —Password to use for access. privilege-level —Level of access to Cisco IOS
                                                   					 commands to be granted to this user. Only the commands with the same or a lower
                                                   					 level can be executed via XML. Range is 0 to 15. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)telephony-service | Enters telephony-service configuration mode. |
| Step 4 | overlap-signal Example: Router(config-telephony)#overlap-signal | Allows to configure overlap signaling support for SCCP IP phones. |
| Step 5 | exit Example: Router(config-telephony)#exit | Exits telephony-service configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)ephone 10 | Enters ephone configuration mode. |
| Step 7 | overlap-signal Example: Router(config-ephone)overlap-signal | Applies overlap signaling support for ephone. |
| Step 8 | exit Example: Router(config-ephone)exit | Exits ephone configuration mode. |
| Step 9 | ephone-template template-tag Example: Router(config)ephone-template 10 | Enters ephone-template configuration mode. |
| Step 10 | overlap-signal Example: Router(config-ephone-template)#overlap-signal | Applies overlap signaling support to ephone template. |
| Step 11 | end Example: Router(config-ephone-template)# end | Returns to privileged EXEC mode. |

| Note | If your Cisco Unified CME system supports SCCP and SIP phones, do
                                          		  not connect your SIP phones to your network until after you have verified the
                                          		  configuration profile for the SIP phone. |
|---|---|

| Note | From Cisco IOS XE Amsterdam 17.2.1r onwards, cme-app mode was added for ISR4321 routers. This mode allows configuration of up to 200 phones for routers that are dedicated to
                                             CME use only. The cme or cme-app modes configure SIP phones and features for standalone call control use. |
|---|---|

| Restriction | SIP endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP trunks only. Certain Cisco Unified IP phones, such as the Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE,
                                                   are supported only in Cisco Unified CME 4.1 and later versions. DSCP requires Cisco Unified CME 7.1 or a later version. If DSCP is configured for the gateway interface using the service-policy command or for the dial peer using the ip qos dscp command, the value set with those commands takes precedence over the DSCP value configured in this procedure. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set parameters
                                          			 for all supported SIP phones in Cisco Unified CME. |
| Step 4 | mode [ cme \| cme-app ] Example: Router(config-register-global)# mode cme | Enables mode for provisioning SIP phones in Cisco Unified CME. |
| Step 5 | source-address ip-address [ port port ] Example: Router(config-register-global)# source-address 10.6.21.4 | Enables the Cisco Unified CME router to receive messages from SIP
                                          			 phones through the specified IP address and port. port port —(Optional) TCP/IP port number. Range: 2000 to 9999. Default: 2000. |
| Step 6 | load phone-type firmware-file Example: Router(config-register-global)# load 7960-7940 P0S3-07-3-00 | Associates a phone type with a phone firmware file. A separate load command is required for each phone type. |
| Step 7 | tftp-path { flash : \| slot0: \| tftp:// url } Example: Router(config-register-global)# tftp-path http://mycompany.com/files | (Optional) Defines a location, other than system memory, from
                                          			 which the SIP phones will download configuration profile files. Default: system memory (system:/cme/sipphone/). |
| Step 8 | max-pool max-phones Example: Router(config-register-global)# max-pool 10 | Sets maximum number of SIP phones to be supported by the Cisco
                                          			 Unified CME router. Version- and platform-dependent; type ? for range. In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is maximum number supported by platform. In Cisco Unified CME 7.0(1) and later versions: Default is 0. |
| Step 9 | max-dn max-directory-numbers Example: Router(config-register-global)# max-dn 20 | (Optional) Sets maximum number of directory numbers for SIP
                                          			 phones to be supported by the Cisco Unified CME router. Required for Cisco Unified CME 7.0(1) and later versions. In Cisco Unified CME 7.0(1) and later versions: Default is 0. Range is 1 to maximum number supported by platform. Type ? for range. In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is 150 or maximum allowed on platform. Type ? for value. |
| Step 10 | authenticate [ all ][ realm string ] Example: Router(config-register-global)# authenticate all realm company.com | (Optional) Enables authentication for registration requests in
                                          			 which the MAC address of the SIP phone cannot be identified by using other
                                          			 methods. |
| Step 11 | ip qos dscp {{ number \| af \| cs \| default \| ef } { media \| service \| signaling \| video }} Example: Router(config-register-global)# ip qos dscp af43 video | Sets the DSCP priority levels for different types of traffic. |
| Step 12 | end Example: Router(config-register-global)# end | Exits voice register global configuration mode and enters
                                          			 privileged EXEC mode. |

| Note | If your Cisco Unified CME system supports SCCP and SIP phones, do
                                          		  not connect your SIP phones to your network until after you have verified the
                                          		  configuration profile for the SIP phone. |
|---|---|

| Note | From Cisco IOS XE Amsterdam 17.2.1r onwards, cme-app mode was added for ISR4321 routers. This mode allows configuration of up to 200 phones for routers that are dedicated to
                                             CME use only. The cme or cme-app modes configure SIP phones and features for standalone call control use. |
|---|---|

| Restriction | SIP endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP trunks only. Certain Cisco Unified IP phones, such as the Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE,
                                                   are supported only in Cisco Unified CME 4.1 and later versions. DSCP requires Cisco Unified CME 7.1 or a later version. If DSCP is configured for the gateway interface using the service-policy command or for the dial peer using the ip qos dscp command, the value set with those commands takes precedence over the DSCP value configured in this procedure. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set parameters
                                          			 for all supported SIP phones in Cisco Unified CME. |
| Step 4 | mode [ cme \| cme-app ] Example: Router(config-register-global)# mode cme | Enables mode for provisioning SIP phones in Cisco Unified CME. |
| Step 5 | source-address ip-address [ port port ] Example: Router(config-register-global)# source-address 10.6.21.4 | Enables the Cisco Unified CME router to receive messages from SIP
                                          			 phones through the specified IP address and port. port port —(Optional) TCP/IP port number. Range: 2000 to 9999. Default: 2000. |
| Step 6 | load phone-type firmware-file Example: Router(config-register-global)# load 7960-7940 P0S3-07-3-00 | Associates a phone type with a phone firmware file. A separate load command is required for each phone type. |
| Step 7 | tftp-path { flash : \| slot0: \| tftp:// url } Example: Router(config-register-global)# tftp-path http://mycompany.com/files | (Optional) Defines a location, other than system memory, from
                                          			 which the SIP phones will download configuration profile files. Default: system memory (system:/cme/sipphone/). |
| Step 8 | max-pool max-phones Example: Router(config-register-global)# max-pool 10 | Sets maximum number of SIP phones to be supported by the Cisco
                                          			 Unified CME router. Version- and platform-dependent; type ? for range. In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is maximum number supported by platform. In Cisco Unified CME 7.0(1) and later versions: Default is 0. |
| Step 9 | max-dn max-directory-numbers Example: Router(config-register-global)# max-dn 20 | (Optional) Sets maximum number of directory numbers for SIP
                                          			 phones to be supported by the Cisco Unified CME router. Required for Cisco Unified CME 7.0(1) and later versions. In Cisco Unified CME 7.0(1) and later versions: Default is 0. Range is 1 to maximum number supported by platform. Type ? for range. In Cisco CME 3.4 to Cisco Unified CME 7.0: Default is 150 or maximum allowed on platform. Type ? for value. |
| Step 10 | authenticate [ all ][ realm string ] Example: Router(config-register-global)# authenticate all realm company.com | (Optional) Enables authentication for registration requests in
                                          			 which the MAC address of the SIP phone cannot be identified by using other
                                          			 methods. |
| Step 11 | ip qos dscp {{ number \| af \| cs \| default \| ef } { media \| service \| signaling \| video }} Example: Router(config-register-global)# ip qos dscp af43 video | Sets the DSCP priority levels for different types of traffic. |
| Step 12 | end Example: Router(config-register-global)# end | Exits voice register global configuration mode and enters
                                          			 privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | timezone number Example: Router(config-register-global)# timezone 8 | Selects the
                                             				time zone used for SIP phones in Cisco Unified CME. Default: 5 ,
                                                   					 Pacific Standard/Daylight Time. Type ? to
                                                   					 display a list of time zones. |
| Step 5 | date-format [ d/m/y \| m/d/y \| y-d-m \| y/d/m \| y/m/d \| yy-m-d ] Example: Router(config-register-global)# date-format yy-m-d | (Optional)
                                             				Selects the date display format on SIP phones in Cisco Unified CME. Default: m/d/y . |
| Step 6 | time-format { 12 \| 24 } Example: Router(config-register-global)# time-format 24 | (Optional)
                                             				Selects the time display format on SIP phones in Cisco Unified CME. Default: 12 . |
| Step 7 | dst auto-adjust Example: Router(config-register-global)# dst auto-adjust | (Optional)
                                             				Enables automatic adjustment of Daylight Saving Time on SIP phones in
                                             				Cisco Unified CME. To
                                                   					 modify start and stop times for daylight savings time, use the dst command. |
| Step 8 | dst { start \| stop } month [ day day-of-month \| week week-number \| day day-of-week] time hour:minutes Example: Router(config-register-global)# dst start jan day 1 time 00:00 Router(config-register-global)# dst stop mar day 31 time 23:59 | (Optional) Sets the time period for Daylight Saving Time on SIP phones in Cisco Unified CME. Required if automatic adjustment of Daylight Saving Time is enabled by using the dst auto-adjust command. Default is Start: First week of April, Sunday, 2:00 a.m. Stop: Last week of October, Sunday 2:00 a.m. |
| Step 9 | end Example: Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME environment. |
| Step 4 | ntp-server ip-address [ mode { anycast \| directedbroadcast \| multicast \| unicast }] Example: Router(config-register-global)# ntp-server 10.1.2.3 | Synchronizes
                                             				clock on this router with the specified NTP server. |
| Step 5 | end Example: Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Only Cisco Unified 8951,
                                                				9951, and 9971 SIP IP Phones are supported. No IPv6 support for the
                                                				HFS download service. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ip http server Example: Router(config)# ip http server | Enables the underlying IOS HTTP server of the HFS infrastructure. |
| Step 4 | ip http port number Example: Router(config)# ip http port 60 | (Optional) Specifies the port where the HTTP service is run. |
| Step 5 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set global
                                          			 parameters for all supported Cisco SIP IP phones in a Cisco Unified CME. |
| Step 6 | mode cme Example: Router(config-register-global)# mode cme | Enables the mode for configuring SIP IP phones in a Cisco Unified
                                          			 CME system. |
| Step 7 | load phone-type firmware-file Example: Router(config-register-global)# load 3951 SIP51.9.2.1S | Associates a type of SIP IP phone with a phone firmware file. |
| Step 8 | create profile Example: Router(config-register-global)# create profile | Generates the configuration profile files required for SIP IP
                                          			 phones. |
| Step 9 | exit Example: Router(config-register-global)# exit | Exits voice register global configuration mode. |
| Step 10 | telephony-service Example: Router (config)# telephony-service | Enters telephony-service configuration mode for configuring Cisco
                                          			 Unified CME. |
| Step 11 | hfs enable [ port port-number ] Example: Router(config-telephony)# hfs enable port 5678 | Enables the HFS download service on a specified port. port port-number —(Optional) Specifies the
                                                				  port where the HFS download service is enabled. Range is from 1024 to 65535.
                                                				  Port 80 is the default port. Port 6970 is the custom port. Note If the entered custom HFS port clashes with the underlying IP
                                                      				HTTP port, an error message is displayed and the command is disallowed. | Note | If the entered custom HFS port clashes with the underlying IP
                                                      				HTTP port, an error message is displayed and the command is disallowed. |
| Note | If the entered custom HFS port clashes with the underlying IP
                                                      				HTTP port, an error message is displayed and the command is disallowed. |
| Step 12 | end Example: Router(config-telephonyl)# end | Exits to privileged EXEC mode. |

| Note | If the entered custom HFS port clashes with the underlying IP
                                                      				HTTP port, an error message is displayed and the command is disallowed. |
|---|---|

| Restriction | Only Cisco 8951, 9951,
                                                				and 9971 SIP IP Phones are supported. No IPv6 support for the
                                                				HFS download service. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ip http server Example: Router(config)# ip http server | Enables the underlying IOS HTTP server of the HFS infrastructure. |
| Step 4 | ip http port number Example: Router(config)# ip http port 1234 | Specifies the port where the HTTP service is run. |
| Step 5 | telephony-service Example: Router (config)# telephony-service | Enters telephony-service configuration mode for configuring Cisco
                                          			 Unified CME. |
| Step 6 | hfs enable [ port port-number ] Example: Router(config-telephony)# hfs enable port 6970 | Enables the HFS download service on a specified port. |
| Step 7 | hfs home-path path Example: Router(config-telephony)# hfs home-path flash:/cme/loads/ | Sets a home path directory for Cisco Unified SIP IP phone
                                          			 firmware files that can be searched and fetched using the HFS download service. Note The administrator must store the phone firmware files at the
                                                      				location set as the home path directory. | Note | The administrator must store the phone firmware files at the
                                                      				location set as the home path directory. |
| Note | The administrator must store the phone firmware files at the
                                                      				location set as the home path directory. |
| Step 8 | end Example: Router(config-telephony)# end | Exits to privileged EXEC mode. |

| Note | The administrator must store the phone firmware files at the
                                                      				location set as the home path directory. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                          			 privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                          			 configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                          			 register global configuration mode to set parameters for all supported SIP
                                          			 phones in Cisco Unified CME. |
| Step 4 | application application-name Example: Router(config-register-global)# application sipapp2 | (Optional) Changes the default application for all dial peers
                                             				associated with the SIP phones in Cisco Unified CME to the specified
                                             				application. Note This
                                                      				command can also be configured in voice register pool configuration mode. The
                                                      				value set in voice register pool configuration mode has priority over the value
                                                      				set in voice register global mode. | Note | This
                                                      				command can also be configured in voice register pool configuration mode. The
                                                      				value set in voice register pool configuration mode has priority over the value
                                                      				set in voice register global mode. |
| Note | This
                                                      				command can also be configured in voice register pool configuration mode. The
                                                      				value set in voice register pool configuration mode has priority over the value
                                                      				set in voice register global mode. |
| Step 5 | end Example: Router(config-register-global)# end | Exits voice
                                          			 register global configuration mode and enters privileged EXEC mode. |

| Note | This
                                                      				command can also be configured in voice register pool configuration mode. The
                                                      				value set in voice register pool configuration mode has priority over the value
                                                      				set in voice register global mode. |
|---|---|

| Restriction | If any media service (like
                                                				transcoding and conferencing) is needed for SIP to SIP trunk call, at least one
                                                				of the SIP trunks must be placed in flow through mode. If media needs to flow
                                                				through Cisco Unified CME for voicemail calls, the SIP trunk going towards the
                                                				voicemail must be in flow through mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Router(config)#voice service voip | Enters voice service voip configuration mode. |
| Step 4 | media [ flow around \| flow
                                                				  through ] Example: Router(conf-voi-serv)#media flow-around | Enables global
                                             				media setting for VoIP calls. flow around —Allows the media to flow around the
                                                				  gateway. flow through —Allows the media to flow through the
                                                				  gateway. |
| Step 5 | exit Example: Router(config-voi-ser)#exit | Exits voice
                                             				service voip configuration mode. |
| Step 6 | dial-peer voice tag voip Example: Router(config)#dial-peer voice 222 voip | Enters
                                             				dial-peer configuration mode to define a VoIP dial peer for the voice-mail
                                             				system. tag —Defines the dial peer being configured. Range
                                                				  is 1 to 1073741823. |
| Step 7 | media {[ flow-around \| flow-through ] forking } Example: Router(config-dial-peer)#media flow-around | Enables media
                                             				settings for voice dial-peer. flow-around —Allows the media to flow around the
                                                				  gateway. flow-through —Allows the media to flow through the
                                                				  gateway. forking —Enables media forking. |
| Step 8 | exit Example: Router(config-ephone)exit | Exits voip
                                             				dial-peer configuration mode. |
| Step 9 | voice class media tag Example: Router(config)#voice class media 10 | Enters voice
                                             				class media configuration mode. tag — Defines the voice class media tag being
                                                				  configured. Range is from 1 to 10000. |
| Step 10 | media {[ flow-around \| flow-through ] forking } Example: Router(config-class)#media flow-around | Enables media
                                             				settings for voice dial-peer. flow-around —Allows the media to flow around the
                                                				  gateway. flow-through —Allows the media to flow through the
                                                				  gateway. forking —Enables media forking. |
| Step 11 | end Example: Router(config-class)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register global Example: Router(config)voice register global | Enters voice register global configuration mode to set parameters
                                          			 for all supported SIP phones in Cisco Unified CME. |
| Step 4 | overlap-signal Example: Router(config-register-pool)overlap-signal | Allows to configure overlap signaling support for SIP IP phones. |
| Step 5 | exit Example: Router(config-register-pool)exit | Exits voice register pool configuration mode. |
| Step 6 | voice register pool pool-tag Example: Router(config)voice register pool 10 | Enters voice register pool configuration mode to set
                                          			 phone-specific parameters for a SIP phone. |
| Step 7 | overlap-signal Example: Router(config-register-global)overlap-signal | Enables overlap signaling support for voice register global. |
| Step 8 | exit Example: Router(config-register-global)exit | Exits voice register-template configuration mode. |
| Step 9 | voice register template template tag Example: Router(config)voice register template 5 | Enters voice register-template configuration mode to create an
                                          			 ephone template. template-tag —Unique
                                                				  identifier for the ephone template that is being created. Range: 1 to 10. |
| Step 10 | overlap-signal Example: Router(config-register-temp) overlap-signal | Applies overlap signaling support for voice register-template. |
| Step 11 | end Example: Router(config-register-temp)# end | Returns to privileged EXEC mode. |

| Note | For the synchronization to happen, additional configurations are
                                             			 needed. These configurations such as IXI, HTTP, and telephony-service are
                                             			 provided in the output. |
|---|---|

| Feature
                                          					 Name | Cisco Unified CME Versions | Feature
                                          					 Information |
|---|---|---|
| Redundant Router for SIP Phones | 11.6 | Introduces redundant router support for SIP phones. |
| Unsolicited Notify for Shared Line and Presence Events for Cisco
                                          					 Unified SIP IP Phones | 9.0 | Allows the
                                          					 Unsolicited Notify mechanism to reduce network traffic during Cisco Unified SIP
                                          					 IP phone registration using the bulk registration method. |
| HFS
                                          					 Download Support for IP Phone Firmware and Configuration Files | 8.8 | Provides
                                          					 download support for SIP and SCCP IP phone firmware, scripts, midlets, and
                                          					 configuration files using the HTTP File-Fetch Server (HFS) infrastructure. |
| Bulk
                                          					 Registration | 8.6/3.4 | Introduces
                                          					 bulk registration support for SIP phones. Introduces bulk registration for
                                          					 registering a block of phone numbers with an external registrar. |
| Media Flow
                                          					 Around for SIP-SIP Trunks | 8.5 | Introduces
                                          					 the media flow around feature, which eliminates the need to terminate RTP and
                                          					 re-originate on Cisco Unified CME, reducing media switching latency and
                                          					 increasing the call handling capacity for Cisco Unified CME SIP trunk. |
| Overlap Dialing for SCCP and SIP Phones | 8.5 | Allows the dialed digits from the SIP or SCCP IP phones to pass across the PRI/BRI trunks as overlap digits and not as enbloc
                                          digits, enabling overlap dialing on the PRI/BRI trunks. |
| DSCP | 7.1 | Supports
                                          					 DSCP packet marking for Cisco Unified IP Phones to specify the class of service
                                          					 for each packet. |
| Maximum
                                          					 Ephones | 7.0/4.3 | The max-ephones command sets the maximum number of SCCP phones that can
                                          					 register to Cisco Unified CME, without limiting the number that can be
                                          					 configured. Maximum number of phones that can be configured is 1000. |
| Network
                                          					 Time Protocol for SIP Phones | 4.1 | Allows SIP
                                          					 phones to synchronize to an NTP server. |
| Blocking
                                          					 Automatic Registration | 4.0 | Blocks IP
                                          					 phones that are not explicitly configured in Cisco Unified CME from
                                          					 registering. |
| Per-Phone
                                          					 Configuration Files and Alternate Location | 4.0 | Defines a
                                          					 location other than system for storing configuration files and specifies the
                                          					 type of configuration files to generate. |
| Redundant
                                          					 Router for SCCP Phones | 4.0 | Introduces
                                          					 redundant router capability. |
| SIP phones
                                          					 in Cisco Unified CME | 3.4 | Introduces
                                          					 support for SIP endpoints directly connected to Cisco Unified CME. |