---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-configuration-guide-pcce-b-admi-cbf0aa6537
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/configuration/guide/pcce_b_admin-and-config-guide_12_5/pcce_b_admin-and-config-guide_12_5_appendix_010011.html
retrieved_at: 2026-08-21T04:45:28.858725+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

Updated: June 11, 2024

Chapter: Reference

## Chapter: Reference

# Reference

## Certificates for Live Data

### Certificates and Secure Communications

For secure Cisco Finesse, Cisco Unified Intelligence Center, AWDB, and Live Data server-to-server communication, perform any of the following:

Use the self-signed certificates provided with Live Data.

When using self-signed certificates, agents must accept the Live Data certificates in the Finesse desktop when they sign in
                                                before they can use the Live Data gadget.

Obtain and install a Certification Authority (CA) certificate from a third-party vendor.

Produce a Certification Authority (CA) certificate internally.

After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                          them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki .

For information about adding a certificate, see Insert a new tomcat-trust certificate .

### Self-Signed Certificates and Third-Party CA Certificates

For secure Cisco Finesse, Cisco Unified Intelligence Center, AWDB, and Live Data server-to-server communication, you must set up security certificates (Applicable for both Self-Signed and Third-Party
                              CA Certificates):

For Cisco Finesse and Cisco Unified Intelligence Center servers to communicate with the Live Data server, you must to import
                                    the Live Data certificates and Cisco Unified Intelligence Center certificates into Cisco Finesse, and the Live Data certificates
                                    into Cisco Unified Intelligence Center.

For Live Data servers to communicate with AWDB servers, you must import AWDB certificates into Live Data.

For Live Data servers to communicate with Cisco Unified Intelligence Center servers, you must import Cisco Unified Intelligence
                                    Center servers certificates into Live Data.

On Server

Import Certificates From

Finesse

Live Data and Cisco Unified Intelligence Center

Live Data

AW Database

Cisco Unified Intelligence Center

Cisco Unified Intelligence Center

Live Data

#### Export Self-Signed
                              	 Live Data Certificates

Live Data
                                    		  installation includes the generation of self-signed certificates. If you choose
                                    		  to work with these self-signed certificates (rather than producing your own CA
                                    		  certificate or obtaining a CA certificate from a third-party certificate
                                    		  vendor), you must first export the certificates from Live Data and Cisco
                                    		  Unified Intelligence Center, as described in this procedure. You must export
                                    		  from both Side A and Side B of the Live Data and Cisco Unified Intelligence
                                    		  Center servers. You must then import the certificates into Finesse, importing
                                    		  both Side A and Side B certificates into each side of the Finesse servers.

As is the case
                                    		  when using other self-signed certificates, agents must accept the Live Data
                                    		  certificates in the Finesse desktop when they sign in before they can use the
                                    		  Live Data gadget.

Step 1

Sign in to Cisco Unified Operating System Administration on Cisco Unified Intelligence Center (https:// hostname of Cisco Unified Intelligence Center server /cmplatform).

Step 2

From the Security menu, select Certificate Management .

Step 3

Click Find .

Step 4

Do one of the
                                             			 following:

If the tomcat certificate for your server is on the list, click the certificate to select it. (Ensure that the certificate
                                                      you select includes the hostname for the server.)

If you are using self-signed certificate, do the following:

Click Generate New .

When the certificate generation is complete, restart the Cisco Tomcat service and the Cisco Live Data NGNIX service.

Restart this procedure.

Step 5

Download the certificate and save the file to your desktop.

Be sure to perform these steps for both Side A and Side B.

Step 6

After you have downloaded the certificates from Cisco Unified Intelligence Center, sign in to Cisco Unified Operating System
                                             Administration on the Live Data server (http://hostname of LiveData server/cmplatform), and repeat steps 2 to 5. This is applicable
                                             only for Standalone LiveData.

##### What to do next

You must now
                                    		  import the Live Data and Cisco Unified Intelligence Center certificates into
                                    		  the Finesse servers.

#### Import  Self-Signed Live Data Certificates

To import the certificates into the Finesse servers, use  the following procedure.

Step 1

Sign in to
                                             			 Cisco Unified Operating System Administration on the Finesse server using the following URL:

http s :// FQDN of Finesse server :8443/cmplatform

Step 2

From the Security menu, select Certificate Management .

Step 3

Click Upload
                                                				Certificate .

Step 4

From the Certificate Name drop-down list, select tomcat-trust .

Step 5

Click Browse and browse to the location of the Cisco
                                             					Unified Intelligence Center certificate ().

Step 6

Select the file, and click Upload
                                                				File .

Step 7

After you have uploaded the Cisco Unified Intelligence Center certificate repeat steps 3 to 6 for Live Data certificates.This
                                             is applicable only for standalone Live Data.

Step 8

After you upload both the certificates, restart Cisco Finesse Tomcat on the Finesse server.

##### What to do next

Be sure to perform these steps for both Side A and Side B.

#### Obtain and Upload Third-party CA Certificate

You can use a Certification Authority (CA) certificate provided by a third-party vendor to establish an HTTPS connection between
                                    the Live Data, Cisco Finesse, Cisco Unified Intelligence Center servers, and Cloud Connect servers.

To use third-party CA certificates:

From the Cisco Unified Operating System Administrator of Live Data, Cisco Finesse, Cisco Unified Intelligence Center, and Cloud Connect servers, generate and download a Certificate
                                          Signing Requests (CSR).

Obtain root and application certificates from the third-party vendor.

Upload the appropriate certificates to the Live Data, Unified Intelligence Center, Cisco Finesse, and Cloud Connect servers.

Follow the instructions provided in the Unified CCE Solution: Procedure to Obtain and Upload Third-Party CA certificates (Version 11.x) technical note at https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise-1101/200286-Unified-CCE-Solution-Procedure-to-Obtai.html .

## Change Java Truststore Password

Step 1

Log in to the Windows machine.

Step 2

Run the following command:

Important

```
cd % CCE_JAVA_HOME %\bin
```

Step 3

Change the truststore password by running the following command:

```
keytool.exe -storepasswd -keystore ..\lib\security\cacerts Enter keystore password:  <old-password>
New keystore password:  <new-password>
Re-enter new keystore password:  <new-password>
```

## Graceful Shutdown of Call Server or Reporting Server

As a local administrator, you can use the following procedure to gracefully shut down the Call Server or Reporting Server
                              services from the CLI.

Step 1

Log in to the CVP Call Server box.

Step 2

Go to <CVP-INSTALLED-LOCATION>\Cisco\CVP\bin\ServiceController .

Step 3

Run the service-controller.bat file.

Step 4

Enter the administrator credentials, service name, and IP address details at the prompt:

```
CALLSERVER-IP-ADDRESS: <IP-Address of the Call Server> CALLSERVER-USERNAME: <Username of the Call Server> CALLSERVER-PASSWORD: <Password of the Call Server> SERVICE-NAME: <Choose the Service name which you need to shutdown gracefully(callserver/reportingserver)>
REPORTINGSERVER-IP-ADDRESS: <IP-Address of the REPORTING SERVER>
```

To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running.

If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server.

## Unified CVP Statistics

### Call Server

#### Unified CCE Service Call Statistics

The ICM Service call statistics include data on calls currently being processed by the ICM service, new calls received during
                                    a specified interval, and total calls processed since start time.

The following table describes ICM Service call statistics.

Statistic

Description

Realtime Statistics

Active Calls

The current number of calls being serviced by the Unified ICM Server for a Unified CVP Call Server. This value represents
                                                a count of calls currently being serviced by the ICM for the Unified CVP Call Server for follow-on routing to a Contact Center
                                                agent.

Active SIP Call Legs

The Unified ICM Server can accept Voice over IP (VoIP) calls that originate using the Session Initiation Protocol (SIP). Active
                                                SIP Call Legs indicates the current number of calls received by the Unified ICM Server from the Unified CVP Call Server using
                                                the SIP protocol.

Active VRU Call Legs

The current number of calls receiving Voice Response Unit (VRU) treatment from the Unified ICM Server. The VRU treatment includes
                                                playing pre-recorded messages, asking for Caller Entered Digits (CED), or Speech Recognition Techniques to understand the
                                                customer request.

Active ICM Lookup Requests

Calls originating from an external Unified CVP VXML Server need call routing instructions from the Unified ICM Server. Active
                                                Lookup Requests indicates the current number of external Unified CVP VXML Server call routing requests sent to the ICM Server.

Active Basic Service Video Calls Offered

The current number of simultaneous basic service video calls
                                                					 being processed by the ICM service where video capability was offered.

Active Basic Service Video Calls Accepted

The current number of simultaneous calls that were accepted as
                                                					 basic service video calls and are being processed by the ICM service.

Interval Statistics

Start Time

The time at which the current interval has begun.

Duration Elapsed

The amount of time that has elapsed since the start time in
                                                					 the current interval.

Interval Duration

The interval at which statistics are collected. The default
                                                					 value is 30 minutes.

New Calls

The number of new calls received by the Intelligent Contact
                                                					 Management (ICM) application for follow-on Voice Response Unit (VRU) treatment
                                                					 and routing to a Contact Center agent during the current interval.

SIP Call Legs

The Intelligent Contact Management (ICM) application has the
                                                					 ability to accept Voice over IP (VoIP) calls that originate via the Session
                                                					 Initiation Protocol (SIP). Interval SIP Call Legs is an
                                                					 interval specific snapshot metric indicating the number of calls received by
                                                					 the ICM application via SIP during the current interval.

VRU Call Legs

The number of calls receiving Voice Response Unit (VRU)
                                                					 treatment from the Intelligent Contact Management (ICM) application. The VRU
                                                					 treatment includes playing pre-recorded messages, asking for Caller Entered
                                                					 Digits (CED), or speech recognition techniques to understand the customer
                                                					 request during the current interval.

ICM Lookup Requests

Calls originating in an external Unified CVP VXML Server need
                                                					 call routing instructions from the Intelligent Contact Management (ICM)
                                                					 application. Interval Lookup Requests is an interval specific metric indicating
                                                					 the number of external Unified CVP VXML Server call routing requests sent to
                                                					 the ICM application during the current interval.

Basic Service Video Calls Offered

The number of offered basic service video calls processed by
                                                					 the ICM service during the current interval.

Basic Service Video Calls Accepted

The number of basic service video calls accepted and processed
                                                					 by the ICM service during the current interval.

Aggregate Statistics

Start Time

The time the service started collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the service start
                                                					 time.

Total Calls

The total number of new calls received by the ICM application for follow-on VRU
                                                					 treatment and routing to a Contact Center agent since system start time.

Total SIP Call Legs

The ICM application has the
                                                					 ability to accept VoIP calls that originate via the SIP. Total SIP Switch Legs is a metric
                                                					 indicating the total number of calls received by the ICM application via SIP
                                                					 since system start time.

Total VRU Call Legs

The total number of calls that have received VRU treatment from the ICM application
                                                					 since system start time. The VRU treatment includes playing pre-recorded
                                                					 messages, asking for CED or Speech Recognition
                                                					 Techniques to understand the customer request.

Total ICM Lookup Requests

Calls originating in an external Unified CVP VXML Server need
                                                					 call routing instructions from the ICM application. Total Lookup Requests is a metric indicating the total number of
                                                					 external Unified CVP VXML Server call routing requests sent to the ICM
                                                					 application since system start time.

Total Basic Service Video Calls Offered

The total number of newly offered basic service video calls
                                                					 processed by the ICM service since system start time.

Total Basic Service Video Calls Accepted

The total number of new basic service video calls accepted and
                                                					 processed by the ICM service since system start time.

#### SIP Service Call Statistics

The SIP service call statistics include data on calls currently being processed by the SIP service, new calls received during
                                    a specified interval, and total calls processed since the SIP service started.

The following table describes the SIP Service call statistics.

Statistic

Description

Realtime Statistics

Active Calls

A real time snapshot metric indicating the count of the number of current calls being handled by the SIP service.

Total Call Legs

The total number of SIP call legs being handled by the SIP service. A call leg is also known as a SIP dialog. The metric includes
                                                incoming, outgoing, and ringtone type call legs. For each active call in the SIP service, there will be an incoming call leg,
                                                and an outgoing call leg to the destination of the transfer label.

Active Basic Service Video Calls Offered

The number of basic service video calls in progress where video capability was offered.

Active Basic Service Video Calls Answered

The number of basic service video calls in progress where video capability was answered.

Interval Statistics

Start Time

The time the system started collecting statistics for the current interval.

Duration Elapsed

The amount of time that has elapsed since the start time in the current interval.

Interval Duration

The interval at which statistics are collected. The default value is 30 minutes.

New Calls

The number of SIP Invite messages received by Unified CVP in the current interval. It includes the failed calls as well as
                                                calls rejected due to the SIP service being out of service.

Connects Received

The number of CONNECT messages received by SIP service in order to perform a call Transfer, in the last statistics aggregation
                                                interval. Connects Received includes the regular Unified CVP transfers as well as Refer transfers. Any label coming from the
                                                ICM service is considered a CONNECT message, whether it is a label to send to the VRU or a label to transfer to an agent.

Avg Latency Connect to Answer

The period of time between the CONNECT from ICM and when the call is answered. The metric includes the average latency computation
                                                for all the calls that have been answered in the last statistics aggregation interval.

Failed SIP Transfers (Pre-Dialog)

The total number of failed SIP transfers since system start time. When Unified CVP attempts to make a transfer to the first
                                                destination of the call, it sends the initial INVITE request to set up the caller with the ICM routed destination label. The
                                                metric does not include rejections due to the SIP Service not running. The metric includes failed transfers that were made
                                                after a label was returned from the ICM Server in a CONNECT message.

Failed SIP Transfers (Post-Dialog)

The number of failed re-invite requests on either the inbound or outbound legs of the call during the interval. After a SIP
                                                dialog is established, re-INVITE messages are used to perform transfers. Re-invite requests can originate from the endpoints
                                                or else be initiated by a Unified CVP transfer from the Unified ICME script. This counter includes failures for both kinds
                                                of re-invite requests.

Basic Service Video Calls Offered

The number of basic service video calls offered in the current interval.

Basic Service Video Calls Answered

The number of basic service video calls answered in the current interval.

Whisper Announce Answered

The number of calls for which whisper announcement was successful during the interval.

Whisper Announce Failed

The number of calls for which whisper announcement was failed during the interval.

Agent Greeting Answered

The number of calls for which agent greeting was successful during the interval.

Agent Greeting Failed

The number of calls for which agent greeting was failed during the interval.

Aggregate Statistics

Start Time

The time the service started collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the service start time.

Total New Calls

The number of SIP Invite messages received by Unified CVP since system start time. It includes the failed calls as well as
                                                calls rejected due to the SIP service being out of service.

Connects Received

The number of CONNECT messages received by SIP service in order to perform a Unified CVP Transfer, since system start time.
                                                Connects Received includes the regular Unified CVP transfers as well as Refer transfers. Any label coming from the ICM service
                                                is considered a CONNECT message, whether it is a label to send to the VRU or a label to transfer to an agent.

Avg Latency Connect to Answer

The period of time between the CONNECT from ICM and when the call is answered. The metric includes the average latency computation
                                                for all the calls that have been answered since system start up time.

Failed SIP Transfers (Pre-Dialog)

The total number of failed transfers on the first CVP transfer since system start time. A SIP dialog is established after
                                                the first CVP transfer is completed. The metric does not include rejections due to SIP being out of service. The metric includes
                                                failed transfers that were made after a label was returned from the ICM in a CONNECT message.

Failed SIP Transfers (Post-Dialog)

The number of failed re-invite requests on either the inbound or outbound legs of the call since start time. After a SIP dialog
                                                is established, re-INVITE messages are used to perform transfers. Re-invite requests can originate from the endpoints or else
                                                be initiated by a Unified CVP transfer from the Unified ICME script. This counter includes failures for both kinds of re-invite
                                                requests.

Total Basic Service Video Calls Offered

The total number of basic service video calls offered since system start time.

Total Basic Service Video Calls Answered

The total number of basic service video calls answered since system start time.

Total Whisper Announce Answered

The total number of call for which whisper announce was successful since the system start time.

Total Whisper Announce Failed

The total number of calls for which whisper announce failed since the system start time.

Total Agent Greeting Answered

The total number of calls for which agent greeting was successful since the system start time.

Total Agent Greeting Failed

The total number of calls for which agent greeting failed since the system start time.

#### Infrastructure Statistics

Unified CVP infrastructure statistics displays realtime, interval, and aggregate data (including Java Virtual Machine (JVM)
                                    and threadpool realtime statistics).

The following table describes infrastructure statistics.

Statistic

Description

Realtime Statistics

Ports Available

The number of ports available for the processing of new calls. Exactly one port license is used per call, independent of the
                                                call's traversal through the individual call server services.

Current Port Usage

The number of port usage currently in use on the call server. Exactly one port usage is used per call, independent of the
                                                call's traversal of the individual call server services.

Current Port Usage State

The threshold level of port usage. There are four levels: safe, warning, critical, and failure.

Interval

Start Time

The time the system started collecting statistics for the current interval.

Duration Elapsed

The amount of time that has elapsed since the start time in the current interval.

Interval Duration

The interval at which statistics are collected. The default value is 30 minutes.

Total New Port Usage Requests

The number of port usage checkout requests made in the current interval. For each port license checkout request, whether it
                                                checks out a new port license or not, this metric is increased by one.

Average Port Usage Requests/Minute

The average number of port usage checkout requests made per minute in the current interval. This metric is calculated by dividing
                                                the port license requests metric by the number of minutes elapsed in the current interval.

Maximum Port Usage

The maximum number of ports used during this time interval.

Aggregate Statistics

Start Time

The time the service started collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the service start time.

Total New Port Usage Requests

The number of port checkout requests made since the system was started. For each port checkout request, whether it checks
                                                out a new port or not, this metric is increased by one.

Average Port Usage Requests/Minute

The average number of port checkout requests made per minute since the system was started. This metric is calculated by dividing
                                                the aggregate port license requests metric by the number of minutes elapsed since the system was started.

Peak Port Usage

The peak number of simultaneous ports used since the start of the system. When a port checkout occurs, this metric is set
                                                to the current ports in use metric if that value is greater than this metric's current peak value.

Total Denied Port Usage Requests

The number of port checkout requests that were denied since the start of the system. The only reason a port checkout request
                                                would be denied is if the number of port licenses checked out at the time of the request is equal to the total number of ports
                                                available. When a port checkout is denied, the call does not receive regular treatment (the caller may hear a busy tone or
                                                an error message).

The following table describes thread pool system statistics. The thread pool is a cache of threads, used by Unified CVP components
                                    only, for processing of relatively short tasks. Using a thread pool eliminates the waste of resources encountered when rapidly
                                    creating and destroying threads for these types of tasks.

Statistic

Description

Realtime Statistics

Idle Threads

The number of idle threads waiting for some work.

Active Threads

The number of running thread pool threads currently processing some work.

Core Pool Size

The number of thread pool threads that are never destroyed, regardless of their idle period.

Maximum Pool Size

The maximum number of thread pool threads that can exist simultaneously.

Largest Pool Size

The peak number of thread pool threads simultaneously tasks with some work to process.

The following table describes Java Virtual Machine statistics.

Statistic

Description

Realtime Statistics

Peak Memory Usage

The greatest amount of memory used by the Java Virtual machine since startup. The number reported is in megabytes and indicates
                                                the peak amount of memory ever used simultaneously by this Java Virtual Machine.

Current Memory Usage

The current number of megabytes of memory used by the Java Virtual Machine.

Total Memory

The total amount of memory in megabytes available to the Java Virtual Machine. The number reported is in megabytes and indicates
                                                the how much of the system memory is available for use by the Java Virtual Machine.

Available Memory

The amount of available memory in the Java Virtual Machine. The number reported is in megabytes and indicates how much of
                                                the current system memory claimed by the Java Virtual Machine is not currently being used.

Threads in Use

The number of threads currently in use in the Java Virtual Machine. This number includes all of the Unified CVP  and thread
                                                pool threads, as well as those threads created by the Web Application Server running within the same JVM.

Peak Threads in Use

The greatest amount of threads ever used simultaneously in the Java Virtual Machine since startup. The peak number of threads
                                                ever used by the Java Virtual Machine includes all Unified CVP  and thread pool threads, as well as threads created by the
                                                Web Application Server running within the same JVM.

Uptime

The length of time that the Java Virtual Machine has been running. This time is measured in hh:mm:ss and shows the amount
                                                of elapsed time since the Java Virtual Machine process began executing.

### VXML Server

#### Unified CVP VXML
                              	 Server Statistics

The Unified CVP VXML Server Statistics displays realtime, interval, and aggregate Unified CVP VXML Server statistics.

To view VXML Statistics, at least one deployed Unified CVP VXML Server application must be configured with the CVPDataFeed
                                          logger.

The following table
                                    		  describes the statistics reported by the Unified CVP VXML Server.

Statistic

Description

Port Usage
                                                   						Statistics

Total Ports

The total number of licensed ports for this Unified CVP VXML  server.

Port Usage Expiration Date

The date when the licensed ports expires for this Unified CVP VXML  server.

Available Ports

The number of port licenses available for this Unified CVP VXML  server.

Total Concurrent Callers

The number of callers currently interacting with this Unified CVP VXML  server.

Real Time Statistics

Active
                                                					 Sessions

The number
                                                					 of current sessions being handled by the Unified CVP VXML Server.

Active ICM
                                                					 Lookup Requests

The number
                                                					 of current ICM requests being handled by the Unified CVP VXML Server.

Interval Statistics

Start Time

The time at
                                                					 which the current interval begins.

Duration
                                                					 Elapsed

The amount
                                                					 of time that has elapsed since the start time in the current interval.

Interval
                                                					 Duration

The interval
                                                					 at which statistics are collected. The default value is 30 minutes.

Sessions

The total
                                                					 number of sessions in the Unified CVP VXML Server in the current interval.

Reporting
                                                					 Events

The number of events sent to the Unified CVP Reporting Server from the Unified CVP VXML Server in the current interval.

ICM Lookup
                                                					 Requests

The number
                                                					 of requests from the Unified CVP VXML Server to the ICM Service in the current
                                                					 interval.

ICM Lookup
                                                					 Responses

The number
                                                					 of responses to both failed and successful ICM Lookup Requests that the ICM
                                                					 Service has sent to the Unified CVP VXML Server in the current interval. In the
                                                					 case that multiple response messages are sent back to the Unified CVP VXML
                                                					 Server to a single request, this metric will increment per response message
                                                					 from the ICM Service.

ICM Lookup
                                                					 Successes

The number of successful requests from the Unified CVP VXML Server to the ICM Service in the current interval.

ICM Lookup
                                                					 Failures

The number
                                                					 of requests from the Unified CVP VXML Server to the ICM Service in the current
                                                					 interval. This metric will be incremented in the case an ICM failed message was
                                                					 received or in the case the Unified CVP VXML Server generates the failed
                                                					 message.

Aggregate Statistics

Start Time

The time at
                                                					 which the current interval has begun.

Duration
                                                					 Elapsed

The
                                                					 amount of time that has elapsed since the start time in the current interval.

Total
                                                					 Sessions

The total
                                                					 number of sessions in the Unified CVP VXML Server since startup.

Total
                                                					 Reporting Events

The total
                                                					 number of reporting events sent from the Unified CVP VXML Server since startup.

Total ICM
                                                					 Lookup Requests

The total
                                                					 number of requests from the Unified CVP VXML Server to the ICM Service. For
                                                					 each ICM lookup request, whether the request succeeded or failed, this metric
                                                					 will be increased by one.

Total ICM
                                                					 Lookup Responses

The total
                                                					 number of responses the ICM Service has sent to the Unified CVP VXML Server
                                                					 since startup. For each ICM lookup response, whether the response is to a
                                                					 succeeded or failed request, this metric will be increased by one. In the case
                                                					 that multiple response messages are sent back to the Unified CVP VXML Server to
                                                					 a single request, this metric will increment per response message from the ICM
                                                					 Service.

Total ICM Lookup Successes

The total
                                                					 number of requests from the Unified CVP VXML Server to the ICM Service since
                                                					 startup. For each ICM lookup request that succeeded, this metric will be
                                                					 increased by one.

Total ICM
                                                					 Lookup Failures

The total
                                                					 number of requests from the Unified CVP VXML Server to the ICM Service since
                                                					 startup. For each ICM lookup request that failed, this metric will be increased
                                                					 by one. This metric will be incremented if an ICM failed message was received
                                                					 or if the Unified CVP VXML Server generates a failed message.

SMS Statistics

Total Outbound SMS

Total number of SMS sent by VXML server. This will be increased by 1 once the SMS is sent.

Outbound SMS Successful

Total number of SMS sent successfully to the carrier. This will be increased by 1 once the SMS is posted to the carrier successfully

Outbound SMS Failed

Total number of SMS sent from CVP but not posted to the carrier. This will be increased by 1 whenever the SMS posting to
                                                the carrier is unsuccessful.

#### Infrastructure Statistics

To view further details about infrastructure statistics, see section Infrastructure Statistics .

#### IVR Service Call Statistics

The IVR service call statistics include data on calls currently being
                                    		  processed by the IVR service, new calls received during a specified interval,
                                    		  and total calls processed since the IVR service started.

The following table describes the IVR Service call statistics.

Statistic

Description

Realtime Call Statistics

Active Calls

The number of active calls being serviced by the IVR service.

Active HTTP Requests

The number of active HTTP requests being serviced by the IVR
                                                					 service.

Interval Statistics

Start Time

The time the system started collecting statistics for the
                                                					 current interval.

Duration Elapsed

The amount of time that has elapsed since the start time in
                                                					 the current interval.

Interval Duration

The interval at which statistics are collected. The default
                                                					 value is 30 minutes.

Peak Active Calls

Maximum number of active calls handled by the IVR service at
                                                					 the same time during this interval.

New Calls

New Calls is a metric that counts the number of New Call requests received from the IOS Gateway Service. A New Call includes
                                                the Switch leg of the call and the IVR leg of the call.

Calls Finished

A Call is a metric that represents the Switch leg of the CVP
                                                					 call and the IVR leg of the CVP call. When both legs of the call are finished,
                                                					 this metric increases. Calls Finished is a metric that counts the number of
                                                					 CVP Calls that have finished during this interval.

Average Call Latency

The average amount of time in milliseconds it took the IVR
                                                					 Service to process a New Call or Call Result Request during this interval.

Maximum Call Latency

The maximum amount of time in milliseconds it has taken for
                                                					 the IVR Service to complete the processing of a New Call Request or a Request
                                                					 Instruction Request during this time interval.

Minimum Call Latency

The minimum amount of time in milliseconds it took for the IVR
                                                					 Service to complete the processing of a New Call Request or a Request
                                                					 Instruction Request during this time interval.

Peak Active HTTP Requests

Active HTTP Requests is a metric that indicates the current
                                                					 number of simultaneous HTTP requests being processed by the IVR Service. Peak
                                                					 Active Requests is a metric that represents the maximum simultaneous HTTP
                                                					 requests being processed by the IVR Service during this time interval.

Total HTTP Requests

The total number of HTTP Requests received from a client by
                                                					 the IVR Service during this time interval.

Average HTTP Requests/second

The average number of HTTP Requests the IVR Service receives
                                                					 per second during this time interval.

Peak Active HTTP Requests/second

HTTP Requests per Second is a metric that represents the
                                                					 number of HTTP Requests the IVR Service receives each second from all clients.
                                                					 Peak HTTP Requests per Second is the maximum number of HTTP Requests that were
                                                					 processed by the IVR Service in any given second. This is also known as high
                                                					 water marking.

Aggregate Statistics

Start Time

The time the service started collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the service start
                                                					 time.

Total New Calls

New Calls is a metric that counts the number of New Call
                                                					 requests received from the IOS Gateway Service. A New Call
                                                					 includes the Switch leg of the call and the IVR leg of the call. Total New
                                                					 Calls is a metric that represents the total number of new calls received by the
                                                					 IVR Service since system startup.

Peak Active Calls

The maximum number of simultaneous calls processed by the IVR
                                                					 Service since the service started.

Total HTTP Requests

Total HTTP Requests is a metric that represents the total
                                                					 number of HTTP Requests received from all clients. This metric is the total
                                                					 number of HTTP Requests received by the IVR Service since system startup.

Peak Active HTTP Requests

Active HTTP Requests is a metric that indicates the current
                                                					 number of simultaneous HTTP requests processed by the IVR Service. Maximum
                                                					 number of active HTTP requests processed at the same time since the IVR service
                                                					 started. This is also known as high water marking.

## Unified CVP Reporting Statistics

### Reporting Statistics

Unified CVP Reporting Server statistics include the total number of events received from the IVR, SIP, and VXML services.

The following table describes the Unified CVP Reporting Server statistics.

Statistic

Description

Interval Statistics

Start Time

The time the system started collecting statistics for the
                                             					 current interval.

Duration Elapsed

The amount of time that has elapsed since the start time in
                                             					 the current interval.

Interval Duration

The interval at which statistics are collected. The default
                                             					 value is 30 minutes.

VXML Events Received

The total number of reporting events received from the VXML
                                             					 Service during this interval. For each reporting event received from the VXML
                                             					 Service, this metric will be increased by one.

SIP Events Received

The total number of reporting events received from the SIP
                                             					 Service during this interval. For each reporting event received from the SIP
                                             					 Service, this metric will be increased by one.

IVR Events Received

The total number of reporting events received from the IVR
                                             					 service in the interval. For each reporting event received from the IVR
                                             					 service, this metric will be increased by one.

Database Writes

The total number of writes to the database made by the Unified CVP Reporting Server during the interval. For each write to
                                             the database by the Unified CVP Reporting Server, this metric will be increased by one.

Aggregate Statistics

Start Time

The time the service started collecting statistics.

Duration Elapsed

The amount of time that has elapsed since the service start
                                             					 time.

VXML Events Received

The total number of reporting events received from the VXML
                                             					 Service since the service started. For each reporting event received from the
                                             					 VXML Service, this metric will be increased by one.

SIP Events Received

The total number of reporting events received from the SIP
                                             					 Service since the service started. For each reporting event received from the
                                             					 SIP Service, this metric will be increased by one.

IVR Events Received

The total number of reporting events received from the IVR
                                             					 Service since the service started. For each reporting event received from the
                                             					 IVR Service, this metric will be increased by one.

Database Writes

The total number of writes to the database made by the Unified CVP Reporting Server since startup. For each write to the database
                                             by the Unified CVP Reporting Server, this metric will be increased by one.

### Infrastructure Statistics

To view further details about infrastructure statistics, see section Infrastructure Statistics .

| Note | When using self-signed certificates, agents must accept the Live Data certificates in the Finesse desktop when they sign in
                                                before they can use the Live Data gadget. |
|---|---|

| Note | After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                          them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki . For information about adding a certificate, see Insert a new tomcat-trust certificate . |
|---|---|

| On Server | Import Certificates From |
|---|---|
| Finesse | Live Data and Cisco Unified Intelligence Center |
| Live Data | AW Database Cisco Unified Intelligence Center |
| Cisco Unified Intelligence Center | Live Data |

| Step 1 | Sign in to Cisco Unified Operating System Administration on Cisco Unified Intelligence Center (https:// hostname of Cisco Unified Intelligence Center server /cmplatform). |
|---|---|
| Step 2 | From the Security menu, select Certificate Management . |
| Step 3 | Click Find . |
| Step 4 | Do one of the
                                             			 following: If the tomcat certificate for your server is on the list, click the certificate to select it. (Ensure that the certificate
                                                      you select includes the hostname for the server.) If you are using self-signed certificate, do the following: Click Generate New . When the certificate generation is complete, restart the Cisco Tomcat service and the Cisco Live Data NGNIX service. Restart this procedure. |
| Step 5 | Download the certificate and save the file to your desktop. Be sure to perform these steps for both Side A and Side B. |
| Step 6 | After you have downloaded the certificates from Cisco Unified Intelligence Center, sign in to Cisco Unified Operating System
                                             Administration on the Live Data server (http://hostname of LiveData server/cmplatform), and repeat steps 2 to 5. This is applicable
                                             only for Standalone LiveData. |

| Step 1 | Sign in to
                                             			 Cisco Unified Operating System Administration on the Finesse server using the following URL: http s :// FQDN of Finesse server :8443/cmplatform |
|---|---|
| Step 2 | From the Security menu, select Certificate Management . |
| Step 3 | Click Upload
                                                				Certificate . |
| Step 4 | From the Certificate Name drop-down list, select tomcat-trust . |
| Step 5 | Click Browse and browse to the location of the Cisco
                                             					Unified Intelligence Center certificate (). |
| Step 6 | Select the file, and click Upload
                                                				File . |
| Step 7 | After you have uploaded the Cisco Unified Intelligence Center certificate repeat steps 3 to 6 for Live Data certificates.This
                                             is applicable only for standalone Live Data. |
| Step 8 | After you upload both the certificates, restart Cisco Finesse Tomcat on the Finesse server. |

| Step 1 | Log in to the Windows machine. |
|---|---|
| Step 2 | Run the following command: Important If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. cd % CCE_JAVA_HOME %\bin | Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
| Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
| Step 3 | Change the truststore password by running the following command: keytool.exe -storepasswd -keystore ..\lib\security\cacerts Enter keystore password:  <old-password>
New keystore password:  <new-password>
Re-enter new keystore password:  <new-password> |

| Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
|---|---|

| Step 1 | Log in to the CVP Call Server box. |
|---|---|
| Step 2 | Go to <CVP-INSTALLED-LOCATION>\Cisco\CVP\bin\ServiceController . |
| Step 3 | Run the service-controller.bat file. |
| Step 4 | Enter the administrator credentials, service name, and IP address details at the prompt: CALLSERVER-IP-ADDRESS: <IP-Address of the Call Server> CALLSERVER-USERNAME: <Username of the Call Server> CALLSERVER-PASSWORD: <Password of the Call Server> SERVICE-NAME: <Choose the Service name which you need to shutdown gracefully(callserver/reportingserver)>
REPORTINGSERVER-IP-ADDRESS: <IP-Address of the REPORTING SERVER> Note To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. | Note | To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. |
| Note | To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. |

| Note | To shut down the Reporting Server gracefully, ensure that the CVP Call Server is up and running. If you have selected the reportingserver service, then be sure to provide the IP address of the Reporting Server. |
|---|---|

| Statistic | Description |
|---|---|
| Realtime Statistics |
| Active Calls | The current number of calls being serviced by the Unified ICM Server for a Unified CVP Call Server. This value represents
                                                a count of calls currently being serviced by the ICM for the Unified CVP Call Server for follow-on routing to a Contact Center
                                                agent. |
| Active SIP Call Legs | The Unified ICM Server can accept Voice over IP (VoIP) calls that originate using the Session Initiation Protocol (SIP). Active
                                                SIP Call Legs indicates the current number of calls received by the Unified ICM Server from the Unified CVP Call Server using
                                                the SIP protocol. |
| Active VRU Call Legs | The current number of calls receiving Voice Response Unit (VRU) treatment from the Unified ICM Server. The VRU treatment includes
                                                playing pre-recorded messages, asking for Caller Entered Digits (CED), or Speech Recognition Techniques to understand the
                                                customer request. |
| Active ICM Lookup Requests | Calls originating from an external Unified CVP VXML Server need call routing instructions from the Unified ICM Server. Active
                                                Lookup Requests indicates the current number of external Unified CVP VXML Server call routing requests sent to the ICM Server. |
| Active Basic Service Video Calls Offered | The current number of simultaneous basic service video calls
                                                					 being processed by the ICM service where video capability was offered. |
| Active Basic Service Video Calls Accepted | The current number of simultaneous calls that were accepted as
                                                					 basic service video calls and are being processed by the ICM service. |
| Interval Statistics |
| Start Time | The time at which the current interval has begun. |
| Duration Elapsed | The amount of time that has elapsed since the start time in
                                                					 the current interval. |
| Interval Duration | The interval at which statistics are collected. The default
                                                					 value is 30 minutes. |
| New Calls | The number of new calls received by the Intelligent Contact
                                                					 Management (ICM) application for follow-on Voice Response Unit (VRU) treatment
                                                					 and routing to a Contact Center agent during the current interval. |
| SIP Call Legs | The Intelligent Contact Management (ICM) application has the
                                                					 ability to accept Voice over IP (VoIP) calls that originate via the Session
                                                					 Initiation Protocol (SIP). Interval SIP Call Legs is an
                                                					 interval specific snapshot metric indicating the number of calls received by
                                                					 the ICM application via SIP during the current interval. |
| VRU Call Legs | The number of calls receiving Voice Response Unit (VRU)
                                                					 treatment from the Intelligent Contact Management (ICM) application. The VRU
                                                					 treatment includes playing pre-recorded messages, asking for Caller Entered
                                                					 Digits (CED), or speech recognition techniques to understand the customer
                                                					 request during the current interval. |
| ICM Lookup Requests | Calls originating in an external Unified CVP VXML Server need
                                                					 call routing instructions from the Intelligent Contact Management (ICM)
                                                					 application. Interval Lookup Requests is an interval specific metric indicating
                                                					 the number of external Unified CVP VXML Server call routing requests sent to
                                                					 the ICM application during the current interval. |
| Basic Service Video Calls Offered | The number of offered basic service video calls processed by
                                                					 the ICM service during the current interval. |
| Basic Service Video Calls Accepted | The number of basic service video calls accepted and processed
                                                					 by the ICM service during the current interval. |
| Aggregate Statistics |
| Start Time | The time the service started collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the service start
                                                					 time. |
| Total Calls | The total number of new calls received by the ICM application for follow-on VRU
                                                					 treatment and routing to a Contact Center agent since system start time. |
| Total SIP Call Legs | The ICM application has the
                                                					 ability to accept VoIP calls that originate via the SIP. Total SIP Switch Legs is a metric
                                                					 indicating the total number of calls received by the ICM application via SIP
                                                					 since system start time. |
| Total VRU Call Legs | The total number of calls that have received VRU treatment from the ICM application
                                                					 since system start time. The VRU treatment includes playing pre-recorded
                                                					 messages, asking for CED or Speech Recognition
                                                					 Techniques to understand the customer request. |
| Total ICM Lookup Requests | Calls originating in an external Unified CVP VXML Server need
                                                					 call routing instructions from the ICM application. Total Lookup Requests is a metric indicating the total number of
                                                					 external Unified CVP VXML Server call routing requests sent to the ICM
                                                					 application since system start time. |
| Total Basic Service Video Calls Offered | The total number of newly offered basic service video calls
                                                					 processed by the ICM service since system start time. |
| Total Basic Service Video Calls Accepted | The total number of new basic service video calls accepted and
                                                					 processed by the ICM service since system start time. |

| Statistic | Description |
|---|---|
| Realtime Statistics |
| Active Calls | A real time snapshot metric indicating the count of the number of current calls being handled by the SIP service. |
| Total Call Legs | The total number of SIP call legs being handled by the SIP service. A call leg is also known as a SIP dialog. The metric includes
                                                incoming, outgoing, and ringtone type call legs. For each active call in the SIP service, there will be an incoming call leg,
                                                and an outgoing call leg to the destination of the transfer label. |
| Active Basic Service Video Calls Offered | The number of basic service video calls in progress where video capability was offered. |
| Active Basic Service Video Calls Answered | The number of basic service video calls in progress where video capability was answered. |
| Interval Statistics |
| Start Time | The time the system started collecting statistics for the current interval. |
| Duration Elapsed | The amount of time that has elapsed since the start time in the current interval. |
| Interval Duration | The interval at which statistics are collected. The default value is 30 minutes. |
| New Calls | The number of SIP Invite messages received by Unified CVP in the current interval. It includes the failed calls as well as
                                                calls rejected due to the SIP service being out of service. |
| Connects Received | The number of CONNECT messages received by SIP service in order to perform a call Transfer, in the last statistics aggregation
                                                interval. Connects Received includes the regular Unified CVP transfers as well as Refer transfers. Any label coming from the
                                                ICM service is considered a CONNECT message, whether it is a label to send to the VRU or a label to transfer to an agent. |
| Avg Latency Connect to Answer | The period of time between the CONNECT from ICM and when the call is answered. The metric includes the average latency computation
                                                for all the calls that have been answered in the last statistics aggregation interval. |
| Failed SIP Transfers (Pre-Dialog) | The total number of failed SIP transfers since system start time. When Unified CVP attempts to make a transfer to the first
                                                destination of the call, it sends the initial INVITE request to set up the caller with the ICM routed destination label. The
                                                metric does not include rejections due to the SIP Service not running. The metric includes failed transfers that were made
                                                after a label was returned from the ICM Server in a CONNECT message. |
| Failed SIP Transfers (Post-Dialog) | The number of failed re-invite requests on either the inbound or outbound legs of the call during the interval. After a SIP
                                                dialog is established, re-INVITE messages are used to perform transfers. Re-invite requests can originate from the endpoints
                                                or else be initiated by a Unified CVP transfer from the Unified ICME script. This counter includes failures for both kinds
                                                of re-invite requests. |
| Basic Service Video Calls Offered | The number of basic service video calls offered in the current interval. |
| Basic Service Video Calls Answered | The number of basic service video calls answered in the current interval. |
| Whisper Announce Answered | The number of calls for which whisper announcement was successful during the interval. |
| Whisper Announce Failed | The number of calls for which whisper announcement was failed during the interval. |
| Agent Greeting Answered | The number of calls for which agent greeting was successful during the interval. |
| Agent Greeting Failed | The number of calls for which agent greeting was failed during the interval. |
| Aggregate Statistics |
| Start Time | The time the service started collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the service start time. |
| Total New Calls | The number of SIP Invite messages received by Unified CVP since system start time. It includes the failed calls as well as
                                                calls rejected due to the SIP service being out of service. |
| Connects Received | The number of CONNECT messages received by SIP service in order to perform a Unified CVP Transfer, since system start time.
                                                Connects Received includes the regular Unified CVP transfers as well as Refer transfers. Any label coming from the ICM service
                                                is considered a CONNECT message, whether it is a label to send to the VRU or a label to transfer to an agent. |
| Avg Latency Connect to Answer | The period of time between the CONNECT from ICM and when the call is answered. The metric includes the average latency computation
                                                for all the calls that have been answered since system start up time. |
| Failed SIP Transfers (Pre-Dialog) | The total number of failed transfers on the first CVP transfer since system start time. A SIP dialog is established after
                                                the first CVP transfer is completed. The metric does not include rejections due to SIP being out of service. The metric includes
                                                failed transfers that were made after a label was returned from the ICM in a CONNECT message. |
| Failed SIP Transfers (Post-Dialog) | The number of failed re-invite requests on either the inbound or outbound legs of the call since start time. After a SIP dialog
                                                is established, re-INVITE messages are used to perform transfers. Re-invite requests can originate from the endpoints or else
                                                be initiated by a Unified CVP transfer from the Unified ICME script. This counter includes failures for both kinds of re-invite
                                                requests. |
| Total Basic Service Video Calls Offered | The total number of basic service video calls offered since system start time. |
| Total Basic Service Video Calls Answered | The total number of basic service video calls answered since system start time. |
| Total Whisper Announce Answered | The total number of call for which whisper announce was successful since the system start time. |
| Total Whisper Announce Failed | The total number of calls for which whisper announce failed since the system start time. |
| Total Agent Greeting Answered | The total number of calls for which agent greeting was successful since the system start time. |
| Total Agent Greeting Failed | The total number of calls for which agent greeting failed since the system start time. |

| Statistic | Description |
|---|---|
| Realtime Statistics |
| Ports Available | The number of ports available for the processing of new calls. Exactly one port license is used per call, independent of the
                                                call's traversal through the individual call server services. |
| Current Port Usage | The number of port usage currently in use on the call server. Exactly one port usage is used per call, independent of the
                                                call's traversal of the individual call server services. |
| Current Port Usage State | The threshold level of port usage. There are four levels: safe, warning, critical, and failure. |
| Interval |
| Start Time | The time the system started collecting statistics for the current interval. |
| Duration Elapsed | The amount of time that has elapsed since the start time in the current interval. |
| Interval Duration | The interval at which statistics are collected. The default value is 30 minutes. |
| Total New Port Usage Requests | The number of port usage checkout requests made in the current interval. For each port license checkout request, whether it
                                                checks out a new port license or not, this metric is increased by one. |
| Average Port Usage Requests/Minute | The average number of port usage checkout requests made per minute in the current interval. This metric is calculated by dividing
                                                the port license requests metric by the number of minutes elapsed in the current interval. |
| Maximum Port Usage | The maximum number of ports used during this time interval. |
| Aggregate Statistics |
| Start Time | The time the service started collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the service start time. |
| Total New Port Usage Requests | The number of port checkout requests made since the system was started. For each port checkout request, whether it checks
                                                out a new port or not, this metric is increased by one. |
| Average Port Usage Requests/Minute | The average number of port checkout requests made per minute since the system was started. This metric is calculated by dividing
                                                the aggregate port license requests metric by the number of minutes elapsed since the system was started. |
| Peak Port Usage | The peak number of simultaneous ports used since the start of the system. When a port checkout occurs, this metric is set
                                                to the current ports in use metric if that value is greater than this metric's current peak value. |
| Total Denied Port Usage Requests | The number of port checkout requests that were denied since the start of the system. The only reason a port checkout request
                                                would be denied is if the number of port licenses checked out at the time of the request is equal to the total number of ports
                                                available. When a port checkout is denied, the call does not receive regular treatment (the caller may hear a busy tone or
                                                an error message). |

| Statistic | Description |
|---|---|
| Realtime Statistics |
| Idle Threads | The number of idle threads waiting for some work. |
| Active Threads | The number of running thread pool threads currently processing some work. |
| Core Pool Size | The number of thread pool threads that are never destroyed, regardless of their idle period. |
| Maximum Pool Size | The maximum number of thread pool threads that can exist simultaneously. |
| Largest Pool Size | The peak number of thread pool threads simultaneously tasks with some work to process. |

| Statistic | Description |
|---|---|
| Realtime Statistics |
| Peak Memory Usage | The greatest amount of memory used by the Java Virtual machine since startup. The number reported is in megabytes and indicates
                                                the peak amount of memory ever used simultaneously by this Java Virtual Machine. |
| Current Memory Usage | The current number of megabytes of memory used by the Java Virtual Machine. |
| Total Memory | The total amount of memory in megabytes available to the Java Virtual Machine. The number reported is in megabytes and indicates
                                                the how much of the system memory is available for use by the Java Virtual Machine. |
| Available Memory | The amount of available memory in the Java Virtual Machine. The number reported is in megabytes and indicates how much of
                                                the current system memory claimed by the Java Virtual Machine is not currently being used. |
| Threads in Use | The number of threads currently in use in the Java Virtual Machine. This number includes all of the Unified CVP  and thread
                                                pool threads, as well as those threads created by the Web Application Server running within the same JVM. |
| Peak Threads in Use | The greatest amount of threads ever used simultaneously in the Java Virtual Machine since startup. The peak number of threads
                                                ever used by the Java Virtual Machine includes all Unified CVP  and thread pool threads, as well as threads created by the
                                                Web Application Server running within the same JVM. |
| Uptime | The length of time that the Java Virtual Machine has been running. This time is measured in hh:mm:ss and shows the amount
                                                of elapsed time since the Java Virtual Machine process began executing. |

| Statistic | Description |
|---|---|
| Port Usage
                                                   						Statistics |
| Total Ports | The total number of licensed ports for this Unified CVP VXML  server. |
| Port Usage Expiration Date | The date when the licensed ports expires for this Unified CVP VXML  server. |
| Available Ports | The number of port licenses available for this Unified CVP VXML  server. |
| Total Concurrent Callers | The number of callers currently interacting with this Unified CVP VXML  server. |
| Real Time Statistics |
| Active
                                                					 Sessions | The number
                                                					 of current sessions being handled by the Unified CVP VXML Server. |
| Active ICM
                                                					 Lookup Requests | The number
                                                					 of current ICM requests being handled by the Unified CVP VXML Server. |
| Interval Statistics |
| Start Time | The time at
                                                					 which the current interval begins. |
| Duration
                                                					 Elapsed | The amount
                                                					 of time that has elapsed since the start time in the current interval. |
| Interval
                                                					 Duration | The interval
                                                					 at which statistics are collected. The default value is 30 minutes. |
| Sessions | The total
                                                					 number of sessions in the Unified CVP VXML Server in the current interval. |
| Reporting
                                                					 Events | The number of events sent to the Unified CVP Reporting Server from the Unified CVP VXML Server in the current interval. |
| ICM Lookup
                                                					 Requests | The number
                                                					 of requests from the Unified CVP VXML Server to the ICM Service in the current
                                                					 interval. |
| ICM Lookup
                                                					 Responses | The number
                                                					 of responses to both failed and successful ICM Lookup Requests that the ICM
                                                					 Service has sent to the Unified CVP VXML Server in the current interval. In the
                                                					 case that multiple response messages are sent back to the Unified CVP VXML
                                                					 Server to a single request, this metric will increment per response message
                                                					 from the ICM Service. |
| ICM Lookup
                                                					 Successes | The number of successful requests from the Unified CVP VXML Server to the ICM Service in the current interval. |
| ICM Lookup
                                                					 Failures | The number
                                                					 of requests from the Unified CVP VXML Server to the ICM Service in the current
                                                					 interval. This metric will be incremented in the case an ICM failed message was
                                                					 received or in the case the Unified CVP VXML Server generates the failed
                                                					 message. |
| Aggregate Statistics |
| Start Time | The time at
                                                					 which the current interval has begun. |
| Duration
                                                					 Elapsed | The
                                                					 amount of time that has elapsed since the start time in the current interval. |
| Total
                                                					 Sessions | The total
                                                					 number of sessions in the Unified CVP VXML Server since startup. |
| Total
                                                					 Reporting Events | The total
                                                					 number of reporting events sent from the Unified CVP VXML Server since startup. |
| Total ICM
                                                					 Lookup Requests | The total
                                                					 number of requests from the Unified CVP VXML Server to the ICM Service. For
                                                					 each ICM lookup request, whether the request succeeded or failed, this metric
                                                					 will be increased by one. |
| Total ICM
                                                					 Lookup Responses | The total
                                                					 number of responses the ICM Service has sent to the Unified CVP VXML Server
                                                					 since startup. For each ICM lookup response, whether the response is to a
                                                					 succeeded or failed request, this metric will be increased by one. In the case
                                                					 that multiple response messages are sent back to the Unified CVP VXML Server to
                                                					 a single request, this metric will increment per response message from the ICM
                                                					 Service. |
| Total ICM Lookup Successes | The total
                                                					 number of requests from the Unified CVP VXML Server to the ICM Service since
                                                					 startup. For each ICM lookup request that succeeded, this metric will be
                                                					 increased by one. |
| Total ICM
                                                					 Lookup Failures | The total
                                                					 number of requests from the Unified CVP VXML Server to the ICM Service since
                                                					 startup. For each ICM lookup request that failed, this metric will be increased
                                                					 by one. This metric will be incremented if an ICM failed message was received
                                                					 or if the Unified CVP VXML Server generates a failed message. |
| SMS Statistics |
| Total Outbound SMS | Total number of SMS sent by VXML server. This will be increased by 1 once the SMS is sent. |
| Outbound SMS Successful | Total number of SMS sent successfully to the carrier. This will be increased by 1 once the SMS is posted to the carrier successfully |
| Outbound SMS Failed | Total number of SMS sent from CVP but not posted to the carrier. This will be increased by 1 whenever the SMS posting to
                                                the carrier is unsuccessful. |

| Statistic | Description |
|---|---|
| Realtime Call Statistics |
| Active Calls | The number of active calls being serviced by the IVR service. |
| Active HTTP Requests | The number of active HTTP requests being serviced by the IVR
                                                					 service. |
| Interval Statistics |
| Start Time | The time the system started collecting statistics for the
                                                					 current interval. |
| Duration Elapsed | The amount of time that has elapsed since the start time in
                                                					 the current interval. |
| Interval Duration | The interval at which statistics are collected. The default
                                                					 value is 30 minutes. |
| Peak Active Calls | Maximum number of active calls handled by the IVR service at
                                                					 the same time during this interval. |
| New Calls | New Calls is a metric that counts the number of New Call requests received from the IOS Gateway Service. A New Call includes
                                                the Switch leg of the call and the IVR leg of the call. |
| Calls Finished | A Call is a metric that represents the Switch leg of the CVP
                                                					 call and the IVR leg of the CVP call. When both legs of the call are finished,
                                                					 this metric increases. Calls Finished is a metric that counts the number of
                                                					 CVP Calls that have finished during this interval. |
| Average Call Latency | The average amount of time in milliseconds it took the IVR
                                                					 Service to process a New Call or Call Result Request during this interval. |
| Maximum Call Latency | The maximum amount of time in milliseconds it has taken for
                                                					 the IVR Service to complete the processing of a New Call Request or a Request
                                                					 Instruction Request during this time interval. |
| Minimum Call Latency | The minimum amount of time in milliseconds it took for the IVR
                                                					 Service to complete the processing of a New Call Request or a Request
                                                					 Instruction Request during this time interval. |
| Peak Active HTTP Requests | Active HTTP Requests is a metric that indicates the current
                                                					 number of simultaneous HTTP requests being processed by the IVR Service. Peak
                                                					 Active Requests is a metric that represents the maximum simultaneous HTTP
                                                					 requests being processed by the IVR Service during this time interval. |
| Total HTTP Requests | The total number of HTTP Requests received from a client by
                                                					 the IVR Service during this time interval. |
| Average HTTP Requests/second | The average number of HTTP Requests the IVR Service receives
                                                					 per second during this time interval. |
| Peak Active HTTP Requests/second | HTTP Requests per Second is a metric that represents the
                                                					 number of HTTP Requests the IVR Service receives each second from all clients.
                                                					 Peak HTTP Requests per Second is the maximum number of HTTP Requests that were
                                                					 processed by the IVR Service in any given second. This is also known as high
                                                					 water marking. |
| Aggregate Statistics |
| Start Time | The time the service started collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the service start
                                                					 time. |
| Total New Calls | New Calls is a metric that counts the number of New Call
                                                					 requests received from the IOS Gateway Service. A New Call
                                                					 includes the Switch leg of the call and the IVR leg of the call. Total New
                                                					 Calls is a metric that represents the total number of new calls received by the
                                                					 IVR Service since system startup. |
| Peak Active Calls | The maximum number of simultaneous calls processed by the IVR
                                                					 Service since the service started. |
| Total HTTP Requests | Total HTTP Requests is a metric that represents the total
                                                					 number of HTTP Requests received from all clients. This metric is the total
                                                					 number of HTTP Requests received by the IVR Service since system startup. |
| Peak Active HTTP Requests | Active HTTP Requests is a metric that indicates the current
                                                					 number of simultaneous HTTP requests processed by the IVR Service. Maximum
                                                					 number of active HTTP requests processed at the same time since the IVR service
                                                					 started. This is also known as high water marking. |

| Statistic | Description |
|---|---|
| Interval Statistics |
| Start Time | The time the system started collecting statistics for the
                                             					 current interval. |
| Duration Elapsed | The amount of time that has elapsed since the start time in
                                             					 the current interval. |
| Interval Duration | The interval at which statistics are collected. The default
                                             					 value is 30 minutes. |
| VXML Events Received | The total number of reporting events received from the VXML
                                             					 Service during this interval. For each reporting event received from the VXML
                                             					 Service, this metric will be increased by one. |
| SIP Events Received | The total number of reporting events received from the SIP
                                             					 Service during this interval. For each reporting event received from the SIP
                                             					 Service, this metric will be increased by one. |
| IVR Events Received | The total number of reporting events received from the IVR
                                             					 service in the interval. For each reporting event received from the IVR
                                             					 service, this metric will be increased by one. |
| Database Writes | The total number of writes to the database made by the Unified CVP Reporting Server during the interval. For each write to
                                             the database by the Unified CVP Reporting Server, this metric will be increased by one. |
| Aggregate Statistics |
| Start Time | The time the service started collecting statistics. |
| Duration Elapsed | The amount of time that has elapsed since the service start
                                             					 time. |
| VXML Events Received | The total number of reporting events received from the VXML
                                             					 Service since the service started. For each reporting event received from the
                                             					 VXML Service, this metric will be increased by one. |
| SIP Events Received | The total number of reporting events received from the SIP
                                             					 Service since the service started. For each reporting event received from the
                                             					 SIP Service, this metric will be increased by one. |
| IVR Events Received | The total number of reporting events received from the IVR
                                             					 Service since the service started. For each reporting event received from the
                                             					 IVR Service, this metric will be increased by one. |
| Database Writes | The total number of writes to the database made by the Unified CVP Reporting Server since startup. For each write to the database
                                             by the Unified CVP Reporting Server, this metric will be increased by one. |