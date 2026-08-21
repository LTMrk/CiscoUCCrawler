---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-managed-services-12-5-1-cucm-b-managed-services-guide-1251-cucm-b-manag-3ddf64686b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/managed_services/12_5_1/cucm_b_managed-services-guide-1251/cucm_b_managed-services-guide-1251_chapter_0100.html
retrieved_at: 2026-08-21T08:59:47.753209+00:00
---

Managed Services Guide for Cisco Unified Communications Manager and IM and Presence Service

# Managed Services Guide for Cisco Unified Communications Manager and IM and Presence Service

Updated: January 22, 2019

Chapter: Cisco Unified Real-Time Monitoring Tool Tracing PerfMon Counters and Alerts

## Chapter: Cisco Unified Real-Time Monitoring Tool Tracing PerfMon Counters and Alerts

# Cisco Unified Real-Time Monitoring Tool Tracing PerfMon Counters and Alerts

This chapter briefly describes the Cisco Unified Communications Real-Time Monitoring Tool (RTMT) tracing capabilities, perfmon
                        objects and counters, and alerts.

## Cisco Unified Real-Time Monitoring

The RTMT runs as a client-side application and uses HTTPS and TCP to monitor system performance, device status, device discovery,
                              CTI applications, and voice messaging ports. RTMT can connect directly to devices by using HTTPS to troubleshoot system issues.
                              Cisco Unified RTMT performs the following tasks:

Monitor a set of predefined management objects that monitor the health of the system.

Generate various alerts, in the form of e-mails, for objects when values go over/below user-configured thresholds.

Collect and view traces in various default viewers that exist in RTMT.

Translate Q931 messages.

View syslog messages in SysLog Viewer.

Work with performance-monitoring counters.

In addition to SNMP traps, Cisco Unified RTMT can monitor and parse syslog messages that are provided by the hardware vendors,
                              and then send these alerts to RTMT Alert Central. You can configure RTMT to notify the Unified Communications Manager system administrator when the alerts occur. The notifications can occur by using e-mail or Epage or both.

Be aware the RTMT is best used for a single cluster. For large and enterprise networks that have multiple clusters deployed,
                                          Cisco recommends using Cisco Unified Operations Manager. For details about Cisco Unified Operations Manager, go to http://www.cisco.com/en/US/products/ps6535/index.htm .

## Performance Monitoring in RTMT

Unified Communications Manager updates performance counters (called PerfMon counters). The counters contain simple, useful information about the system
                              and devices on the system, such as number of registered phones, number of active calls, number of available conference bridge
                              resources, and voice messaging port usage.

You can monitor the performance of the components of the system and the components for the application on the system by choosing
                              the counters for any object. The counters for each object display when the folder expands.

For Unified Communications Manager , the Cisco CallManager object contains most of the Unified Communications Manager performance counters, and these counters have only one instance. The instance-based counters that belong to the other objects
                              can have zero or more instances. For example, if two phones are registered to Unified Communications Manager , two instances of each counter that belong to the Cisco phones object exist.

You can log perfmon counters locally on the computer and use the performance log viewer in RTMT to display the perfmon CSV
                              log files that you collected or the Real-time Information Server Data Collection (RISDC) perfmon logs.

RTMT provides alert notifications for troubleshooting performance. It also periodically polls performance counters to display
                              data for that counter. Performance monitoring allows you to perform the following tasks:

Monitor performance counters including all the Unified Communications Manager servers in a cluster (if applicable), TFTP servers, and database servers.

Continuously monitor a set of preconfigured objects and receive notification in the form of an e-mail message.

Associate counter threshold settings to alert notification. An e-mail or popup message provides notification to the administrator.

Save and restore settings, such as counters that get monitored, threshold settings, and alert notifications, for customized
                                    troubleshooting tasks.

Display up to six perfmon counters in one chart for performance comparisons.

### PerfMon Alert Notifications

The alert notifications keep you updated on system and Unified Communications Manager issues. You can use the parameters that are already contained in RTMT or configure your own. The following table lists the
                                 available settings and describes each. The Threshold, Value Calculated As, Duration, Frequency, and Schedule panes of RTMT
                                 contain the settings.

Setting

Description

Threshold Pane

Trigger alert when Over and Under conditions get met

Check the box and enter the value that applies.

- Over—Check this box to configure a maximum threshold that must be met before an alert notification is activated. In the Over
                                                value field, enter a value. For example, enter a value that equals the number of calls in progress.

Value Calculated As Pane

Absolute, Delta, Delta Percentage

Click the radio button that applies.

- Absolute—Choose Absolute to display the data at its current status. These counter values are cumulative.

- Delta—Choose Delta to display the difference between the current counter value and the previous counter value.

- Delta Percentage—Choose Delta Percentage to display the counter performance changes in percentage.

Duration Pane

Trigger alert only when value constantly...; Trigger alert immediately

- Trigger alert only when value constantly...—If you want the alert notification only when the value is constantly below or
                                                over threshold for a desired number of seconds, click this radio button and enter seconds after which you want the alert to
                                                be sent.

- Trigger alert immediately—If you want the alert notification to be sent immediately, click this radio button.

Frequency Pane

Trigger alert on every poll; trigger up to...

Click the radio button that applies.

For example, if the calls in progress continue to go over or under the threshold, the system does not send another alert notification.
                                                   When the threshold is normal (between 50 and 100 calls in progress), the system deactivates the alert notification; however,
                                                   if the threshold goes over or under the threshold value again, the system reactivates alert notification.

- Trigger up to...—If you want the alert notification to activate at certain intervals, click this radio button and enter the
                                                number of alerts that you want sent and the number of minutes within which you want them sent.

Schedule Pane

24-hours daily; start/stop

Click the radio button that applies:

- 24-hours daily—If you want the alert to be triggered 24 hours a day, click this radio button.

- Start/Stop—If you want the alert notification activated within a specific time frame, click the radio button and enter a start
                                                time and a stop time. If the check box is checked, enter the start and stop times of the daily task. For example, you can
                                                configure the counter to be checked every day from 9:00 am to 5:00 pm or from 9:00 pm to 9:00 am.

If you require an e-mail notifications, check the Enable E-mail box.

You can also use data sampling in RTMT. The perfmon counters that display in the RTMT Perfmon Monitoring pane have green dots
                                 that represent samples of data over time. You can configure the number of samples to collect and the number of data points
                                 to show in the chart. The following table lists and describes the parameters.

Parameter

Description

Absolute

Because some counter values are accumulative, choose Absolute to display the data at its current status.

Delta

Choose Delta to display the difference between the current counter value and the previous counter value.

Delta Percentage

Choose Delta Percentage to display the counter performance changes in percentage.

### PerfMon Objects and Counters for Cisco Unified Communications Manager

This section provides information on Unified Communications Manager PerfMon objects and counters.

#### Cisco Analog Access

The Cisco Analog Access object provides information about registered Cisco Analog Access gateways. The following table contains
                                    information about Cisco Analog Access counters.

Counters

Counter Description

OutboundBusyAttempts

This counter represents the total number of times that Unified Communications Manager attempts a call through the analog access gateway when all ports were busy.

PortsActive

This counter represents the number of ports that are currently in use (active). A port appears active when a call is in progress
                                                on that port.

PortsOutOfService

This counter represents the number of ports that are currently out of service. Counter applies only to loop-start and ground-start
                                                trunks.

#### Cisco Annunciator Device

The Cisco Annunciator Device object provides information about registered Cisco annunciator devices. The following table contains
                                    information about Cisco Annunciator counters.

Counters

Counter Description

OutOfResources

This counter represents the total number of times that Unified Communications Manager attempted to allocate an annunciator resource from an annunciator device and failed; for example, because all resources were
                                                already in use.

ResourceActive

This counter represents the total number of annunciator resources that are currently active (in use) for an annunciator device.

ResourceAvailable

This counter represents the total number of resources that are not active and are still available to be used at the current
                                                time for the annunciator device.

ResourceTotal

This counter represents the total number of annunciator resources that are configured for an annunciator device.

#### Cisco
                              	 CallManager

The Cisco CallManager object provides information about calls, applications, and devices that are registered with the Unified Communications Manager . The following table contains information about Cisco CallManager counters.

Counters

Counter
                                                					 Description

AnnunciatorOutOfResources

This counter represents the total number of times that Unified Communications Manager attempted to allocate an annunciator resource from those that are registered to a Unified Communications Manager when none were available.

AnnunciatorResourceActive

This counter represents the total number of annunciator resources that are currently in use on all annunciator devices that
                                                are registered with a Unified Communications Manager .

AnnunciatorResourceAvailable

This counter
                                                					 represents the total number of annunciator resources that are not active and
                                                					 are currently available.

AnnunciatorResourceTotal

This counter represents the total number of annunciator resources that are provided by all annunciator devices that are currently
                                                registered with Unified Communications Manager .

AuthenticatedCallsActive

This counter represents the number of authenticated calls that are currently active (in use) on Unified Communications Manager . An authenticated call designates one in which all the endpoints that are participating in the call are authenticated. An
                                                authenticated phone uses the Transport Layer Security (TLS) authenticated Skinny protocol signaling with Unified Communications Manager .

AuthenticatedCallsCompleted

This counter represents the number of authenticated calls that connected and subsequently disconnected through Unified Communications Manager . An authenticated call designates one in which all the endpoints that are participating in the call are authenticated. An
                                                authenticated phone uses the TLS authenticated Skinny protocol signaling with Unified Communications Manager .

AuthenticatedPartiallyRegisteredPhone

This counter
                                                					 represents the number of partially registered, authenticated SIP phones.

AuthenticatedRegisteredPhones

This counter represents the total number of authenticated phones that are registered to Unified Communications Manager . An authenticated phone uses the TLS authenticated Skinny protocol signaling with Unified Communications Manager .

BRIChannelsActive

This counter represents the number of BRI voice channels that are currently in an active call on this Unified Communications Manager .

BRISpansInService

This counter
                                                					 represents the number of BRI spans that are currently available for use.

CallManagerHeartBeat

This counter represents the heartbeat of Unified Communications Manager . This incremental count indicates that Cisco Unified Communications Manager is up and running. If the count does not increment, that indicates that Unified Communications Manager is down.

CallsActive

This counter represents the number of voice or video streaming connections that are currently in use (active); in other words,
                                                the number of calls that actually have a voice path that is connected on Unified Communications Manager .

CallsAttempted

This counter
                                                					 represents the total number of attempted calls. An attempted call occurs any
                                                					 time that a phone goes off hook and back on hook, regardless of whether any
                                                					 digits were dialed, or whether it connected to a destination. The system
                                                					 considers some call attempts during feature operations (such as transfer and
                                                					 conference) to be attempted calls.

CallsCompleted

This counter represents the number of calls that were actually connected (a voice path or video stream was established) through Unified Communications Manager . This number increases when the call terminates.

CallsInProgress

This counter represents the number of voice or video calls that are currently in progress on Unified Communications Manager , including all active calls.

When a
                                                					 phone that is registered with Skinny Client Control Protocol (SCCP) goes off
                                                					 hook, the CallsInProgress progress counter increments until it goes back on
                                                					 hook.

For Cisco Unified IP
                                                   						Phone s 7940, and 7960 that register with SIP, the CallsInProgress
                                                					 counter increments when the dial softkey is pressed.

For all
                                                					 other phones that are running SIP, the CallsInProgress counter increments when
                                                					 the first digit is pressed.

When all
                                                					 voice or video calls that are in progress are connected, the number of
                                                					 CallsInProgress represents the number of CallsActive. The counter decreases by
                                                					 one when a phone goes back on hook.

CM_MediaTermPointsRequestsThrottled

This counter represents the total number of media termination point (MTP) resource requests that have been denied due to throttling
                                                (a resource from this MTP was not allocated because, as specified by the Cisco CallManager service parameter, MTP and Transcoder
                                                Resource Throttling Percentage, the MTP was being utilized beyond the configured throttle percentage). This counter increments
                                                each time a request for an MTP on this Unified Communications Manager node is requested and denied due to MTP throttling and reflects a running total since the start of the Cisco CallManager
                                                service.

CM_TranscoderRequestsThrottled

This counter represents the total number of transcoder resource requests that have been denied due to throttling (a resource
                                                from this transcoder was not allocated because, as specified by the Cisco CallManager service parameter MTP and Transcoder
                                                Resource Throttling Percentage, the transcoder was being utilized beyond the configured throttle percentage). This counter
                                                increments each time a request for a transcoder on this Unified Communications Manager node is requested and denied due to transcoder throttling and reflects a running total since the start of the Cisco CallManager
                                                service

EncryptedCallsActive

This counter represents the number of encrypted calls that are currently active (in use) on this Unified Communications Manager . An encrypted call represents one in which all the endpoints that are participating in the call are encrypted.

EncryptedCallsCompleted

This counter represents the number of encrypted calls that were connected and subsequently disconnected through this Unified Communications Manager . An encrypted call represents one in which all the endpoints that are participating in the call are encrypted.

EncryptedPartiallyRegisteredPhones

This
                                                					 counter represents the number of partially registered, encrypted SIP phones.

EncryptedRegisteredPhones

This counter represents the total number of encrypted phones that are registered on this Unified Communications Manager .

FXOPortsActive

This counter represents the number of FXO ports that are currently in use (active) on a Unified Communications Manager .

FXOPortsInService

This
                                                					 counter represents the number of FXO ports that are currently available for use
                                                					 in the system.

FXSPortsActive

This counter represents the number of FXS ports that are currently in use (active) on a Unified Communications Manager .

FXSPortsInService

This
                                                					 counter represents the number of FXS ports that are currently available for use
                                                					 in the system.

HuntListsInService

This counter represents the number of hunt lists that are currently in service on Unified Communications Manager .

HWConferenceActive

This counter represents the total number of hardware conference resources that are provided by all hardware conference bridge
                                                devices that are currently registered with Unified Communications Manager .

HWConferenceCompleted

This counter represents the total number of conferences that used a hardware conference bridge (hardware-based conference
                                                devices such as Cisco Catalyst 6000, Cisco Catalyst 4000, Cisco VG200, Cisco series 26xx and 36xx) that is allocated from Unified Communications Manager and that have completed, which means that the conference bridge has been allocated and released. A conference activates when
                                                the first call connects to the bridge. The conference completes when the last call disconnects from the bridge.

HWConferenceOutOfResources

This counter represents the total number of times that Unified Communications Manager attempted to allocate a hardware conference resource from those that are registered to a Unified Communications Manager when none was available.

HWConferenceResourceActive

This counter represents the total number of conference resources that are in use on all hardware conference devices (such
                                                as Cisco Catalyst 6000, Catalyst 4000, Cisco VG200, Cisco series 26xx and 36xx) that are registered with Unified Communications Manager . System considers conference to be active when one or more calls are connected to a bridge.

HWConferenceResourceAvailable

This counter represents the number of hardware conference resources that are not in use and that are available to be allocated
                                                on all hardware conference devices (such as Cisco Catalyst 6000, Cisco Catalyst 4000, Cisco VG200, Cisco series 26xx and 36xx)
                                                that are allocated from Unified Communications Manager and that have been completed, which means that the conference bridge has been allocated and released. A conference activates
                                                when the first call connects to the bridge. The conference completes when the last call disconnects from the bridge.

HWConferenceResourceTotal

This counter represents the number of active conferences on all hardware conference devices that are registered with Unified Communications Manager .

InitializationState

This counter represents the current initialization state of Unified Communications Manager . Unified Communications Manager includes the following initialization state values:

1-Database; 2-Regions; 3-Locations; 4-QoS Policy; 5-Time Of Day;
                                                					 6-AAR Neighborhoods; 7-Digit Analysis; 8-Route Plan; 9-Call Control; 10-RSVP
                                                					 Session Manager; 11-Supplementary Services; 12-Directory; 13-SDL Link;
                                                					 14-Device; 100-Initialization Complete.

Not all
                                                					 states display when this counter is used. This does not indicate that an error
                                                					 occurred; it simply indicates that the state(s) initialized and completed
                                                					 within the refresh period of the performance monitor.

LocationOutOfResources

This
                                                					 counter represents the total number of times that a call through Locations
                                                					 failed due to the lack of bandwidth.

MOHMulticastResourceActive

This counter represents the total number of multicast MOH resources that are currently in use (active) on all MOH servers
                                                that are registered with a Unified Communications Manager .

MOHMulticastResourceAvailable

This counter represents the total number of active multicast MOH connections that are not being used on all MOH servers that
                                                are registered with a Unified Communications Manager .

MOHOutOfResources

This counter represents the total number of times that the Media Resource Manager attempted to allocate an MOH resource when
                                                all available resources on all MOH servers that are registered with a Unified Communications Manager were already active.

MOHTotalMulticastResources

This counter represents the total number of multicast MOH resources or connections that are provided by all MOH servers that
                                                are currently registered with a Unified Communications Manager .

MOHTotalUnicastResources

This counter represents the total number of unicast MOH resources or streams that are provided by all MOH servers that are
                                                currently registered with Unified Communications Manager . Each MOH unicast resource uses one stream.

MOHUnicastResourceActive

This counter represents the total number of unicast MOH resources that are currently in use (active) on all MOH servers that
                                                are registered with Unified Communications Manager . Each MOH unicast resource uses one stream.

MOHUnicastResourceAvailable

This counter represents the total number of unicast MOH resources that are currently available on all MOH servers that are
                                                registered with Unified Communications Manager . Each MOH unicast resource uses one stream.

MTPOutOfResources

This counter represents the total number of times that Unified Communications Manager attempted but failed to allocate an MTP resource from one MTP device that is registered with Unified Communications Manager . This also means that no transcoders were available to act as MTPs.

MTPResourceActive

This counter represents the total number of MTP resources that are currently in use (active) on all MTP devices that are registered
                                                with a Unified Communications Manager . Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call.

MTPResourceAvailable

This counter represents the total number of MTP resources that are not in use and are available to be allocated on all MTP
                                                devices that are registered with Unified Communications Manager . Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call.

MTPResourceTotal

This counter represents the total number of media termination point (MTP) resources that are provided by all MTP devices that
                                                are currently registered with Unified Communications Manager .

MTP_RequestsThrottled

This
                                                					 counter represents the total number of media termination point (MTP) resource
                                                					 requests that have been denied due to throttling (a resource from this MTP was
                                                					 not allocated because, as specified by the Cisco CallManager service parameter
                                                					 MTP and Transcoder Resource Throttling Percentage, the MTP was being utilized
                                                					 beyond the configured throttle percentage). This counter increments each time a
                                                					 resource is requested from this MTP and is denied due to throttling. This
                                                					 counter reflects a running total since the MTP device registered with the Cisco
                                                					 CallManager service.

PartiallyRegisteredPhone

This
                                                					 counter represents the number of partially registered phones that are running
                                                					 SIP.

PRIChannelsActive

This counter represents the number of PRI voice channels that are in an active call on a Unified Communications Manager .

PRISpansInService

This
                                                					 counter represents the number of PRI spans that are currently available for
                                                					 use.

RegisteredAnalogAccess

This
                                                					 counter represents the number of registered Cisco analog access gateways that
                                                					 are registered with system. The count does not include the number of Cisco
                                                					 analog access ports.

RegisteredHardwarePhones

This
                                                					 counter represents the number of Cisco hardware IP phones (for example, Cisco Unified IP
                                                   						Phone s 7960, 7940, and so on) that are currently registered in
                                                					 the system.

RegisteredMGCPGateway

This
                                                					 counter represents the number of MGCP gateways that are currently registered in
                                                					 the system.

RegisteredOtherStationDevices

This
                                                					 counter represents the number of station devices other than Cisco hardware IP
                                                					 phones that are currently registered in the system (for example,
                                                					 Cisco IP SoftPhone, CTI port, CTI route point, Cisco voice-mail port).

SIPLineServerAuthorizationChallenges

This counter represents the number of authentication challenges for incoming SIP requests that the Unified Communications Manager server issued to phones that are running SIP. An authentication challenge occurs when a phone that is running SIP with Digest
                                                Authentication enabled sends a SIP line request to Unified Communications Manager .

SIPLineServerAuthorizationFailures

This counter represents the number of authentication challenge failures for incoming SIP requests from SIP phones to the Unified Communications Manager server. An authentication failure occurs when a SIP phone with Digest Authentication enabled sends a SIP line request with
                                                bad credentials to Unified Communications Manager .

SIPTrunkAuthorization

This counter represents the number of application-level authorization checks for incoming SIP requests that Unified Communications Manager has issued to SIP trunks. An application-level authorization check occurs when Unified Communications Manager compares an incoming SIP request to the application-level settings on the SIP Trunk Security Profile Configuration window
                                                in Cisco Unified Communications Manager Administration .

SIPTrunkAuthorizationFailures

This counter represents the number of application-level authorization failures for incoming SIP requests that have occurred
                                                on Unified Communications Manager SIP trunks. An application-level authorization failure occurs when Unified Communications Manager compares an incoming SIP request to the application-level authorization settings on the SIP Trunk Security Profile Configuration
                                                window in Cisco Unified Communications Manager Administration and finds that authorization for one or more of the SIP features on that window is not allowed.

SIPTrunkServerAuthenticationChallenges

This counter represents the number of authentication challenges for incoming SIP requests that Unified Communications Manager issued to SIP trunks. An authentication challenge occurs when a SIP trunk with Digest Authentication enabled sends a SIP
                                                request to Unified Communications Manager .

SIPTrunkServerAuthenticationFailures

This counter represents the number of authentication challenge failures that occurred for incoming SIP requests from SIP trunks
                                                to Unified Communications Manager . An authentication failure occurs when a SIP trunk with Digest Authentication enabled sends a SIP request with bad credentials
                                                to Unified Communications Manager .

SWConferenceActive

This counter represents the number of active conferences on all software conference devices that are registered with Unified Communications Manager .

SWConferenceCompleted

This counter represents the total number of conferences that used a software conference bridge that was allocated from a Unified Communications Manager and that have been completed, which means that the conference bridge has been allocated and released. A conference activates
                                                when the first call connects to the bridge. The conference completes when the last call disconnects from the bridge.

SWConferenceOutOfResources

This counter represents the total number of times that Unified Communications Manager attempted to allocate a software conference resource from those that are registered to Unified Communications Manager when none was available. Counter includes failed attempts to add a new participant to an existing conference.

SWConferenceResourceActive

This counter represents the total number of conference resources that are in use on all software conference devices that are
                                                registered with Unified Communications Manager . The system considers a conference to be active when one or more calls connect to a bridge. One resource equals one stream.

SWConferenceResourceAvailable

This counter represents the number of new software-based conferences that can be started at the same time, for Unified Communications Manager . You must have a minimum of three streams available for each new conference. One resource equals one stream

SWConferenceResourceTotal

This counter represents the total number of software conference resources that are provided by all software conference bridge
                                                devices that are currently registered with Unified Communications Manager .

SystemCallsAttempted

This
                                                					 counter represents the total number of server-originated calls and attempted
                                                					 calls to the Unity message waiting indicator (MWI).

T1ChannelsActive

This counter represents the number of T1 CAS voice channels that are in an active call on a Unified Communications Manager .

T1SpansInService

This
                                                					 counter represents the number of T1 CAS spans that are currently available for
                                                					 use.

TLSConnectedSIPTrunks

This
                                                					 counter represents the number of SIP trunks that are configured and connected
                                                					 via Transport Layer Security (TLS).

TLSConnectedWSM

This
                                                					 counter represents the number of WSM Connectors that are configured and
                                                					 connected to Motorola WSM via Transport Layer Security (TLS).

TranscoderOutOfResources

This counter represents the total number of times that Unified Communications Manager attempted to allocate a transcoder resource from a transcoder device that is registered to a Unified Communications Manager when none was available.

TranscoderResourceActive

This counter represents the total number of transcoders that are in use on all transcoder devices that are registered with Unified Communications Manager . A transcoder in use represents one transcoder resource that has been allocated for use in a call. Each transcoder resource
                                                uses two streams.

TranscoderResourceAvailable

This counter represents the total number of transcoders that are not in use and that are available to be allocated on all
                                                transcoder devices that are registered with Unified Communications Manager . Each transcoder resource uses two streams.

TranscoderResourceTotal

This counter represents the total number of transcoder resources that are provided by all transcoder devices that are currently
                                                registered with Unified Communications Manager .

VCBConferenceActive

This counter represents the total number of active video conferences on all video conference bridge devices that are registered
                                                with Unified Communications Manager .

VCBConferenceAvailable

This counter represents the total number of new video conferences on all video conference bridge devices that are registered
                                                with Unified Communications Manager .

VCBConferenceCompleted

This counter represents the total number of video conferences that used a video conference bridge that are allocated from Unified Communications Manager and that have been completed, which means that the conference bridge has been allocated and released. A conference activates
                                                when the first call connects to the bridge. The conference completes when the last call disconnects from the bridge.

VCBConferenceTotal

This counter represents the total number of video conferences that are supported on all video conference bridge devices that
                                                are registered with Unified Communications Manager .

VCBOutOfConferences

This counter represents the total number of times that Unified Communications Manager attempted to allocate a video conference resource from those that are registered to Unified Communications Manager when none was available.

VCBOutOfResources

This
                                                					 counter represents the total number of failed new video conference requests. A
                                                					 conference request can fail because, for example, the configured number of
                                                					 conferences is already in use.

VCBResourceActive

This counter represents the total number of video conference resources that are currently in use on all video conference devices
                                                that are registered with Unified Communications Manager .

VCBResourceAvailable

This
                                                					 counter represents the total number of video conference resources that are not
                                                					 active and are currently available.

VCBResourceTotal

This counter represents the total number of video conference resources that are provided by all video conference bridge devices
                                                that are currently registered with Unified Communications Manager .

VideoCallsActive

This counter represents the number of active video calls with active video streaming connections on all video conference bridge
                                                devices that are registered with Unified Communications Manager .

VideoCallsCompleted

This
                                                					 counter represents the number of video calls that were actually connected with
                                                					 video streams and then released.

VideoOutOfResources

This counter represents the total number of times that Unified Communications Manager attempted to allocate a video-streaming resource from one of the video conference bridge devices that is registered to Unified Communications Manager when none was available.

XCODE_RequestsThrottled

This
                                                					 counter represents the total number of transcoder resource requests that have
                                                					 been denied due to throttling (a resource from this transcoder was not
                                                					 allocated because, as specified by the Cisco CallManager service parameter MTP
                                                					 and Transcoder Resource Throttling Percentage, the transcoder was being
                                                					 utilized beyond the configured throttle percentage). This counter increments
                                                					 each time a resource is requested from this transcoder and is denied due to
                                                					 throttling. This counter reflects a running total since the transcoder device
                                                					 registered with the Cisco CallManager service.

#### Cisco CallManager External Call Control

The Cisco CallManager External Call Control feature provides information about the counters that are added to support the
                                    External Call Control feature. The following table contains information about the External Call Control counters.

Counters

Counter Description

Unified Communications Manager Object

ExternalCallControlEnabledCallsAttempted

This counter specifies the total number of calls to devices that have the External Call Control feature enabled. This is a
                                                cumulative count of all calls to intercept-enabled patterns or DNs since the last restart of the Cisco CallManager service.

ExternalCallControlEnabledCallsCompleted

This counter specifies the total number of calls that were connected to a device that had the External Call Control feature
                                                enabled. This is a cumulative count of all calls to intercept-enabled patterns or DNs since the last restart of the Cisco
                                                CallManager service.

ExternalCallControlEnabledFailureTreatmentApplied

This counter specifies the total number of calls that were cleared or routed based on failure treatments (such as Allow or
                                                Deny) that are defined in the External Call Control profile.

External Call Control Objects

PDPServersTotal

This counter defines the total number of PDP servers in all External Call Control Profiles configured in Cisco Unified Communications Manager Administration. This counter increments when a new PDP server is added and decrements when a PDP server is removed.

PDPServersInService

This counter defines the total number of in-service (active) PDP servers.

PDPServersOutOfService

This counter defines the total number of times that PDP servers have transitioned from in-service to out-of-service. This
                                                is a cumulative count of out-of-service PDP servers since the last restart of the Cisco CallManager service.

ConnectionsActiveToPDPServer

This counter specifies the total number of connections that Unified Communications Manager has established (currently active) with PDP servers.

ConnectionsLostToPDPServer

This counter specifies the total number of times that active connections between Unified Communications Manager and the PDP servers were disconnected. This is a cumulative count since the last restart of the Cisco CallManager service.

#### Cisco CallManager SAF

The Cisco SAF Client object provides information about SAF counters that are specific to each node. The following table contains
                                    information about Cisco  SAF Client object counters.

Counters

Counter Description

SAFConnectionsSucceeded (range from 0 to 2)

Total number of SAF client connections currently active on this Unified Communications Manager node.

SAFFConnectionsFailed (range from 0 to 2)

Total number of SAF client connections that failed on the Unified Communications Manager node. A failed connection is a connection that did not register with the SAF Forwarder.

A Unified Communications Manager node restart causes a counter reset.

See Real-Time Monitoring Tool Guide for more information.

#### Cisco CallManager System Performance

The Cisco CallManager System Performance object provides system performance information about Unified Communications Manager . The following table contains information about Cisco CallManager system performance counters.

Counters

Counter Description

AverageExpectedDelay

This counter represents the current average expected delay before any incoming message gets handled.

CallsRejectedDueToICTThrottling

This counter represents the total number of calls that were rejected since the start of Cisco CallManager service due to Intercluster
                                                Trunk (ICT) call throttling. When the threshold limit of 140 calls per 5 seconds is met, the ICT will start throttling (rejecting)
                                                new calls. One cause for ICT call throttling occurs when calls across an ICT enter a route loop condition.

CallThrottlingGenericCounter3

This counter represents a generic counter that is used for call-throttling purpose.

CodeRedEntryExit

This counter indicates whether Unified Communications Manager has entered or exited a Code state (call-throttling mode). Valid values include 0 (Exit) and 1 (Entry).

CodeYellowEntryExit

This counter indicates whether  has entered or exited a Code Unified Communications Manager Yellow state (call-throttling mode). Valid values include 0 (Exit) and 1 (Entry).

EngineeringCounter1

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

EngineeringCounter2

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

EngineeringCounter3

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

EngineeringCounter4

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

EngineeringCounter5

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

EngineeringCounter6

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

EngineeringCounter7

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

EngineeringCounter8

Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes.

QueueSignalsPresent 1-High

This counter indicates the number of high-priority signals in the Unified Communications Manager queue. High-priority signals include timeout events, internal Unified Communications Manager keepalives, certain gatekeeper events, and internal process creation, among other events. A large number of high-priority
                                                events will cause degraded performance on Unified Communications Manager and result in slow call connection or loss of dial tone. Use this counter in conjunction with the QueueSignalsProcessed 1-High
                                                counter to determine the processing delay on Unified Communications Manager .

QueueSignalsPresent 2-Normal

This counter indicates the number of normal-priority signals in the Unified Communications Manager queue. Normal-priority signals include call-processing functions, key presses, on-hook and off-hook notifications, among
                                                other events. A large number of normal-priority events will cause degraded performance on Unified Communications Manager , sometimes resulting in delayed dial tone, slow call connection, or loss of dial tone. Use this counter in conjunction with
                                                the QueueSignalsProcessed 2-Normal counter to determine the call-processing delay on Unified Communications Manager . Remember that high-priority signals must complete before normal-priority signals begin to process, so check the high-priority
                                                counters as well to get an accurate picture of the potential delay.

QueueSignalsPresent 3-Low

This counter indicates the number of low-priority signals in the Unified Communications Manager queue. Low-priority signals include station device registration (except the initial station registration request message),
                                                among other events. A large number of signals in this queue could result in delayed device registration, among other events.

QueueSignalsPresent 4-Lowest

This counter indicates the number of lowest priority signals in the Unified Communications Manager queue. Lowest priority signals include the initial station registration request message during device registration, among
                                                other events. A large number of signals in this queue could result in delayed device registration, among other events.

QueueSignalsProcessed 1-High

This counter indicates the number of high-priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 1-High counter to determine
                                                the processing delay on this queue.

QueueSignalsProcessed 2-Normal

This counter indicates the number of normal-priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 2-Normal counter to determine
                                                the processing delay on this queue. Remember that high-priority signals get processed before normal-priority signals.

QueueSignalsProcessed 3-Low

This counter indicates the number of low-priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 3-Low counter to determine
                                                the processing delay on this queue. The number of signals processed gives an indication of how much device registration activity
                                                is being processed in this time interval.

QueueSignalsProcessed 4-Lowest

This counter indicates the number of lowest priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 4-Lowest counter to determine
                                                the processing delay on this queue. The number of signals that are processed gives an indication of how many devices began
                                                the Unified Communications Manager registration process in this time interval.

QueueSignalsProcessed Total

This counter provides a sum total of all queue signals that Unified Communications Manager processes for each 1-second interval for all queue levels: high, normal, low, and lowest.

SkinnyDevicesThrottled

This counter represents the total number of Skinny devices that are being throttled. A Skinny device gets throttled (asked
                                                to shut down and reregister) when the total number of events that the Skinny device generated exceeds the configured maximum
                                                threshold value (default value specifies 2000 events) within a 5-second interval.

ThrottlingSampleActivity

This counter indicates how many samples, out of the configured sample size, have non-zero averageExpectedDelay values. This
                                                counter gets reset when any sample has an averageExpectedDelay value of zero. This process repeats for each batch of samples.
                                                A batch represents the configured sample size.

TotalCodeYellowEntry

This counter indicates the number of times that Unified Communications Manager call processing enters the code yellow state. This counter remains cumulative from the start of the Unified Communications Manager process.

#### Cisco CTIManager

The Cisco CTI Manager object provides information about Cisco CTI Manager. The following table contains information about
                                    Cisco CTIManager counters.

Counters

Counter Description

CcmLinkActive

This counter represents the total number of active Unified Communications Manager links. CTI Manager maintains links to all active servers in a cluster, if applicable.

CTIConnectionActive

This counter represents the total number of CTI clients that are currently connected to the CTIManager. This counter increases
                                                by one when a new connection is established and decreases by one when a connection is released. The CTIManager service parameter
                                                MaxCTIConnections determines the maximum number of active connections.

DevicesOpen

This counter represents the total number of devices that are configured in Unified Communications Manager that CTI applications control and/or monitor. Devices include hardware IP phones, CTI ports, CTI route points, and so on.

LinesOpen

This counter represents the total number of lines that are configured in Unified Communications Manager that control and/or monitor CTI applications.

QbeVersion

This counter represents the version number of the Quick Buffer Encoding (QBE) interface that the CTIManager uses.

#### Cisco Dual-Mode Mobility

The Cisco Dual-Mode Mobility object provides information about the dual-mode mobility application on Unified Communications Manager . The following table contains information about Cisco Dual-Mode Mobility counters.

Counters

Counter Description

CallsAnchored

This counter represents the number of calls that are placed or received on dual-mode phones that are anchored in Unified Communications Manager . The counter increments when a call is received from or placed to a dual-mode phone. The counter increments twice if a dual-mode
                                                phone calls another dual-mode phone.

DMMSRegistered

This counter represents the number of Dual-mode Mobile Station (DMMS) subscribers that are registered in the wireless LAN
                                                (WLAN).

FollowMeAborted

This counter represents the number of failed follow-me operations.

FollowMeAttempted

This counter represents the number of follow-me operations that Unified Communications Manager attempted. The counter increments when a SIP 302 - Moved Temporarily message is received from the Wireless Service Manager
                                                (WSM) and Unified Communications Manager redirects the call to the DMMS in WLAN.

FollowMeCompleted

This counter represents the number of follow-me operations that were successfully completed. The counter increments when the
                                                DMMS in WLAN answers the call and the media (voice path) successfully gets established with the calling device.

FollowMeInProgress

This counter represents the number of follow-me operations that are currently in progress. The counter increments when a follow-me
                                                is attempted, and it decrements when the follow-me operation aborts or completes.

H1HandOutAttempted

This counter represents the number of H1 hand-out operations that dual-mode phones attempt. The counter increments when Unified Communications Manager processes a call to the H1 number from a DMMS.

H1HandOutCompleted

This counter represents the number of successfully completed H1 hand-out operations. The counter increments when the DMMS
                                                in WLAN successfully reestablishes a media (voice path).

H2HandOutCompleted

This counter represents the number of successfully completed H2 hand-out operations. The counter increments when the DMMS
                                                in WLAN successfully reestablishes a media (voice path).

H2HandOutsAttempted

This counter represents the number of H2 hand-out operations that dual-mode phones attempt. The counter increments when Unified Communications Manager receives a call to the H2 number from a DMMS.

HandInAborted

This counter represents the number of hand-in operations that failed.

HandInAttempted

This counter represents the number of hand-in operations that dual-mode phones attempt.

HandInCompleted

This counter represents the number of successfully completed hand-in operations. The counter increments when the DMMS in WLAN
                                                successfully reestablishes a media (voice path).

HandInInProgress

This counter represents the number of hand-in operations that are currently in progress. The counter increments when a hand-in
                                                is attempted, and the counter decrements when the hand-in is aborted or completed.

HandOutAborted

This counter represents the number of hand-out operations that failed.

HandOutInProgress

This counter represents the number of H1 and H2 hand-out operations that are currently in progress. The counter increments
                                                when a H1 or H2 hand-out is attempted, and it decrements when the hand-out is aborted or completed.

#### Cisco Extension Mobility

The Cisco Extension Mobility object provides information about the extension mobility application. The following table contains information about Cisco Extension
                                    Mobility counters.

Counters

Counter Description

RequestsHandled

This counter represents the total number of HTTP requests that the extension mobility application handled since the last restart
                                                of the Cisco CallManager service. A typical login would constitute two HTTP requests: one to query the initial login state
                                                of the device and another to log in the user on a device. Similarly, a typical logout also results in two HTTP requests.

RequestsInProgress

This counter represents the number of HTTP requests that the extension mobility application currently is handling. A typical
                                                login would constitute two HTTP requests: one to query the initial login state of the device and another to log in the user
                                                on a device. Similarly, a typical logout also results in two HTTP requests.

RequestsThrottled

This counter represents the total number of Login/Logout Requests that failed due to throttling.

LoginsSuccessful

This counter represents the total number of successful login requests that were completed through Extension Mobility Service.

LogoutsSuccessful

This counter represents the total number of successful logout requests that were completed through Extension Mobility Service

Total Login/LogoutRequestsAttempted

This counter represents the total number of Login and Logout requests that were attempted through this Extension Mobility
                                                Service. This number includes both successful and unsuccessful attempts.

Total Number of EMCC Messages

This represents the total number of messages related to EMCC Requests that came from remote clusters.

Number of Remote Devices

This represents the total number of devices from other clusters that are currently using a EMCC Base Device (EMCC Logged in).

Number of Unknown Remote Users

This represents the total number of users who were not found in any of the remote cluster during inter-cluster extension mobility
                                                login.

Active Inter-cluster Sessions

This represents the total number of inter cluster Extension Mobility requests that are currently in progress.

Total Number of Remote Users

This represents the total number of users from other cluster who use a local device of this cluster and have logged into a
                                                remote cluster.

EMCC Check User Requests Handled

This represents the total number of EMCC check user requests that came from remote clusters.

#### Cisco Feature Control Policy

The Cisco Feature Control Policy feature provides information about the two new counters for TFTP. The following table contains
                                    information about Cisco Feature Control Policy feature counters.

Counters

Counter Description

BuildFeaturePolicyCount

Indicates the number of built FCP files

FeaturePolicyChangeNotifications

Indicates the number of sent FCP change notifications

#### Cisco Gatekeeper

The Cisco Gatekeeper object provides information about registered Cisco gatekeeper devices. The following table contains information
                                    about Cisco gatekeeper device counters.

Counters

Counter Description

ACFsReceived

This counter represents the total number of RAS Admission Confirm messages that are received from the configured gatekeeper
                                                and its alternate gatekeepers.

ARQsAttempted

This counter represents the total number of RAS Admission Request messages that are attempted by using the configured gatekeeper
                                                and its alternate gatekeepers.

RasRetries

This counter represents the number of retries due to loss or delay of all RAS acknowledgement messages on the configured gatekeeper
                                                and its alternate gatekeepers.

VideoOutOfResources

This counter represents the total number of video-stream requests to the configured gatekeeper or its alternate gatekeepers
                                                that failed, most likely due to lack of bandwidth.

#### Cisco H.323

The Cisco H.323 object provides information about registered Cisco H.323 devices. The following table contains information
                                    about Cisco H.323 device counters.

Counters

Counter Description

CallsActive

This counter represents the number of streaming connections that are currently active (in use) on the configured H.323 device;
                                                in other words, the number of calls that actually have a voice path that is connected.

CallsAttempted

This counter represents the total number of calls that have been attempted on a device, including both successful and unsuccessful
                                                call attempts.

CallsCompleted

This counter represents the total number of successful calls that were made from a device.

CallsInProgress

This counter represents the number of calls that are currently in progress on a device.

CallsRejectedDueToICTCallThrottling

This counter represents the total number of calls that are rejected due to Intercluster Trunk (ICT) call throttling since
                                                the start of the Cisco CallManager service. When the system reaches a threshold limit of 140 calls per 5 seconds, ICT will
                                                start throttling (rejecting) new calls. One cause for ICT call throttling occurs when calls across an ICT enter a route loop
                                                condition.

VideoCallsActive

This counter represents the number of video calls with video streaming connections that are currently active (in use) on all
                                                H.323 trunks that are registered with a Unified Communications Manager ; in other words, the number of calls that actually have video-streaming connections on a Unified Communications Manager .

VideoCallsCompleted

This counter represents the number of video calls that were actually connected with video streams for all H.323 trunks that
                                                were registered with a Unified Communications Manager . This number increases when the call terminates.

#### Cisco Hunt Lists

The Cisco Hunt Lists object provides information about the hunt lists that are defined in Cisco Unified Communications Manager Administration. The following table contains information about Cisco hunt list counters.

Counters

Counter Description

CallsAbandoned

This counter represents the number of abandoned calls that occurred through a hunt list. An abandoned call represents one
                                                in which a caller hangs up before the call is answered.

CallsActive

This counter represents the number of calls that are currently active (in use) that occurred through a hunt list. An active
                                                call represents one that gets distributed and answered, and to which a voice path connects.

CallsBusyAttempts

This counter represents the number of times that calls through a hunt list were attempted when all members of the line and/or
                                                route groups were busy.

CallsInProgress

This counter represents the number of calls that are currently in progress through a hunt list. A call in progress represents
                                                one that the call distributor is attempting to extend to a member of a line or route group and that has not yet been answered.
                                                Examples of a hunt list member include a line, a station device, a trunk device, or a port/channel of a trunk device.

CallsRingNoAnswer

This counter represents the total number of calls through a hunt list that rang but that called parties did not answer.

HuntListInService

This counter specifies whether the particular hunt list is currently in service. A value of 0 indicates that the hunt list
                                                is out of service; a value of 1 indicates that the hunt list is in service. Reasons that a hunt list could be out of service
                                                include the hunt list is not running on a primary Unified Communications Manager based on its Unified Communications Manager Group or the hunt list has been disabled in Cisco Unified Communications Manager Administration.

MembersAvailable

This counter represents the total number of available or idle members of line and route groups that belong to an in-service
                                                hunt list. An available member currently handles a call and will accept a new call. An idle member does not handle any call
                                                and will accept a new call. A hunt list member can comprise a route group, line group, or a combination. A member of a line
                                                group represents a directory number of a line on an IP phone or a voice-mail port. A member of a route group represents a
                                                station gateway, a trunk gateway, or port/channel of a trunk gateway.

#### Cisco HW Conference Bridge Device

The Cisco HW Conference Bridge Device object provides information about registered Cisco hardware conference bridge devices.
                                    The following table contains information about Cisco hardware conference bridge device counters.

Counters

Counter Description

HWConferenceActive

This counter represents the number of conferences that are currently active (in use) on a HW conference bridge device. One
                                                resource represents one stream.

HWConferenceCompleted

This counter represents the total number of conferences that have been allocated and released on a HW conference device. A
                                                conference starts when the first call connects to the bridge. The conference completes when the last call disconnects from
                                                the bridge.

OutOfResources

This counter represents the total number of times that an attempt was made to allocate a conference resource from a HW conference
                                                device and failed, for example, because all resources were already in use.

ResourceActive

This counter represents the number of resources that are currently in use (active) for this HW conference device. One resource
                                                represents one stream.

ResourceAvailable

This counter represents the total number of resources that are not active and are still available to be used now for a HW
                                                conference device. One resource represents one stream.

ResourceTotal

This counter represents the total number of resources for a HW conference bridge device. This counter equals the sum of the
                                                counters ResourceAvailable and ResourceActive. One resource represents one stream.

#### Cisco IP Manager Assistant

The Cisco IP Manager Assistant (IPMA) Service object provides information about the Cisco Unified Communications Manager Assistant application. The following table contains information on Cisco IPMA counters.

Counters

Counter Description

AssistantsActive

This counter represents the number of assistant consoles that are currently active. An active assistant console exists when
                                                an assistant is logged in from the assistant console desktop application.

LinesOpen

This counter represents the number of phone lines that the Cisco Unified Communications Manager Assistant application opened. An open phone line exists when the application assumes line control from CTI.

ManagersActive

This counter represents the current number of managers that the Cisco IPMA is servicing.

SessionsCurrent

This counter represents the total number of managers assistants that are currently using the Cisco Unified Communications Manager Assistant application. Each manager and each assistant constitute an active session; so, for one manager/assistant pair, this counter
                                                would reflect two sessions.

#### Cisco Lines

The Cisco Lines object represents the number of Cisco lines (directory numbers) that can dial and connect to a device. Lines
                                    represent all directory numbers that terminate on an endpoint. The directory number that is assigned to it identifies the
                                    line. The Cisco Lines object does not include directory numbers that include wildcards such as a pattern for a Digital or
                                    Analog Access gateway.

The Active counter represents the state of the line, either active or not active. A zero indicates that the line is not in
                                    use. When the number is greater than zero, this indicates that the line is active, and the number represents the number of
                                    calls that are currently in progress on that line. If more than one call is active, this indicates that the call is on hold
                                    either because of being placed on hold specifically (user hold) or because of a network hold operation (for example, a transfer
                                    is in progress, and it is on transfer hold). This applies to all directory numbers that are assigned to any device.

#### Cisco Locations

The Cisco Location object provides information about locations that are defined in Unified Communications Manager . The following table contains information on Cisco location counters.

Counters

Counter Description

BandwidthAvailable

This counter represents the current bandwidth in a given location. A value of 0 indicates that no bandwidth is available.

BandwidthMaximum

This counter represents the maximum bandwidth that is available in a given location. A value of 0 indicates that infinite
                                                bandwidth is available.

CallsInProgress

This counter represents the number of calls that are currently in progress on a particular Unified Communications Manager .

OutOfResources

This counter represents the total number of times that a call on a particular Unified Communications Manager through the location failed due to lack of bandwidth.

RSVP AudioReservationErrorCounts

This counter represents the number of RSVP reservation errors in the audio stream.

RSVP MandatoryConnectionsInProgress

This counter represents the number of connections with mandatory RSVP that are in progress.

RSVP OptionalConnectionsInProgress

This counter represents the number of connections with optional RSVP that are in progress.

RSVP TotalCallsFailed

This counter represents the total number of failed calls due to a RSVP reservation failure.

RSVP VideoCallsFailed

This counter represents the number of video calls that failed due to a RSVP reservation failure.

RSVP VideoReservationErrorCounts

This counter represents the number of RSVP reservation errors in the video stream

VideoBandwidthAvailable

This counter represents the bandwidth that is currently available for video in the location where the person who initiated
                                                the video conference resides. A value of 0 indicates that no bandwidth is available.

VideoBandwidthMaximum

This counter represents the maximum bandwidth that is available for video in the location where the person who initiated the
                                                video conference resides. A value of 0 indicates that no bandwidth is allocated for video.

VideoOutOfResources

This counter represents the total number of failed video-stream requests (most likely due to lack of bandwidth) in the location
                                                where the person who initiated the video conference resides.

#### Cisco Media Streaming Application

The Cisco IP Voice Media Streaming Application object provides information about the registered MTPs, MOH servers, conference
                                    bridge servers, and annunciators. The following table contains information on Cisco IP Voice Media Streaming Application counters.

One object exists for each Unified Communications Manager in the Unified Communications Manager group that is associated with the device pool that the annunciator device is configured to use.

Counter

Counter Description

ANNConnectionsLost

This counter represents the total number of times since the last restart of the Cisco IP Voice Media Streaming Application
                                                that a Unified Communications Manager connection was lost.

ANNConnectionState

For each Unified Communications Manager that is associated with an annunciator, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails).

ANNConnectionsTotal

This counter represents the total number of annunciator instances that have been started since the Cisco IP Voice Media Streaming
                                                Application service started.

ANNInstancesActive

This counter represents the number of actively playing (currently in use) announcements.

ANNStreamsActive

This counter represents the total number of currently active simplex (one direction) streams for all connections. Each stream
                                                direction counts as one stream. One internal stream provides the audio input and another output stream to the endpoint device.

ANNStreamsAvailable

This counter represents the remaining number of streams that are allocated for the annunciator device that are available for
                                                use. This counter starts as 2 multiplied by the number of configured connections (defined in the Cisco IP Voice Media Streaming
                                                App service parameter for the Annunciator, Call Count) and is reduced by one for each active stream that started.

ANNStreamsTotal

This counter represents the total number of simplex (one direction) streams that connected to the annunciator device since
                                                the Cisco IP Voice Media Streaming Application service started.

CFBConferencesActive

This counter represents the number of active (currently in use) conferences.

CFBConferencesTotal

This counter represents the total number of conferences that started since the Cisco IP Voice Media Streaming Application
                                                service started.

CFBConnectionsLost

This counter represents the total number of times since the last restart of the Cisco IP Voice Media Streaming Application
                                                that a Unified Communications Manager connection was lost.

CFBConnectionState

For each Unified Communications Manager that is associated with a SW Conference Bridge, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails).

CFBStreamsActive

This counter represents the total number of currently active simplex (one direction) streams for all conferences. Each stream
                                                direction counts as one stream. In a three-party conference, the number of active streams equals 6.

CFBStreamsAvailable

This counter represents the remaining number of streams that are allocated for the conference bridge that are available for
                                                use. This counter starts as 2 multiplied by the number of configured connections (defined in the Cisco IP Voice Media Streaming
                                                App service parameter for Conference Bridge, Call Count) and is reduced by one for each active stream that started.

CFBStreamsTotal

This counter represents the total number of simplex (one direction) streams that connected to the conference bridge since
                                                the Cisco IP Voice Media Streaming Application service started.

MOHAudioSourcesActive

This counter represents the number of active (currently in use) audio sources for this MOH server. Be aware that some of these
                                                audio sources may not be actively streaming audio data if no devices are listening. The exception exists for multicast audio
                                                sources, which will always be streaming audio.

When an audio source is in use, even after the listener has disconnected, this counter will always have one input stream for
                                                each configured MOH codec. For unicast streams, the stream may exist in a suspended state where no audio data is received
                                                until a device connects to listen to the stream. Each MOH multicast resource uses one stream for each audio source and codec
                                                combination. For example, if the default audio source is configured for multicast, G.711 mu-law and wideband codecs, then
                                                two streams get used (default audio source + G.711 mu-law and default audio source + wideband).

MOHConnectionsLost

This counter represents the total number of times since the last restart of the Cisco IP Voice Media Streaming Application
                                                that a Unified Communications Manager connection was lost.

MOHConnectionState

For each Unified Communications Manager that is associated with an MOH, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails).

MOHStreamsActive

This counter represents the total number of active (currently in use) simplex (one direction) streams for all connections.
                                                One output stream exists for each device that is listening to a unicast audio source, and one input stream exists for each
                                                active audio source, multiplied by the number of MOH codecs.

When an audio source has been used once, it will always have one input stream for each configured MOH codec. For unicast streams,
                                                the stream may exist in a suspended state where no audio data is received until a device connects to listen to the stream.
                                                Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, then two streams get used (default audio source + G.711
                                                mu-law and default audio source + wideband).

MOHStreamsAvailable

This counter represents the remaining number of streams that are allocated for the MOH device that are available for use.
                                                This counter starts as 408 plus the number of configured half-duplex unicast connections and is reduced by 1 for each active
                                                stream that started. The counter gets reduced by 2 for each multicast audio source, multiplied by the number of MOH codecs
                                                that are configured. The counter gets reduced by 1 for each unicast audio source, multiplied by the number of MOH codecs that
                                                are configured.

MOHStreamsTotal

This counter represents the total number of simplex (one direction) streams that have connected to the MOH server since the
                                                Cisco IP Voice Media Streaming Application service started.

MTPConnectionsLost

This counter represents the total number of times since the last restart of the Cisco IP Voice Streaming Application that
                                                a Unified Communications Manager connection was lost.

MTPConnectionState

For each Unified Communications Manager that is associated with an MTP, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails).

MTPConnectionsTotal

This counter represents the total number of MTP instances that have been started since the Cisco IP Voice Media Streaming
                                                Application service started.

MTPInstancesActive

This counter represents the number of active (currently in use) instances of MTP.

MTPStreamsActive

This counter represents the total number of currently active simplex (one direction) streams for all connections. Each stream
                                                direction counts as one stream.

MTPStreamsAvailable

This counter represents the remaining number of streams that are allocated for the MTP device that are available for use.
                                                This counter starts as 2 multiplied by the number of configured connections (defined in the Cisco IP Voice Media Streaming
                                                App service parameter for MTP, Call Count) and is reduced by one for each active stream that started.

MTPStreamsTotal

This counter represents the total number of simplex (one direction) streams that connected to the MTP device since the Cisco
                                                IP Voice Media Streaming Application service started.

#### Cisco MGCP BRI Device

The Cisco Media Gateway Control Protocol (MGCP) Foreign Exchange Office (FXO) Device object provides information about registered
                                    Cisco MGCP BRI devices. The following table contains information on Cisco MGCP BRI device counters.

Counters

Counter Description

CallsCompleted

This counter represents the total number of successful calls that were made from this MGCP Basic Rate Interface (BRI) device

Channel 1 Status

This counter represents the status of the indicated B-Channel that is associated with the MGCP BRI device. Possible values:
                                                0 (Unknown) indicates the status of the channel could not be determined; 1 (Out of service) indicates that this channel is
                                                not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates an
                                                active call on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-channel or for use
                                                as a Synch-Channel for BRI.

Channel 2 Status

This counter represents the status of the indicated B-Channel that is associated with the MGCP BRI device. Possible values:
                                                0 (Unknown) indicates the status of the channel could not be determined; 1 (Out of service) indicates that this channel is
                                                not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates an
                                                active call on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-channel or for use
                                                as a Synch-Channel for BRI.

DatalinkInService

This counter represents the state of the Data Link (D-Channel) on the corresponding digital access gateway. This value will
                                                get set to 1 (one) if the Data Link is up (in service) or 0 (zero) if the Data Link is down (out of service).

OutboundBusyAttempts

This counter represents the total number of times that a call through this MGCP BRI device was attempted when no voice channels
                                                were available.

#### Cisco MGCP FXO Device

The Cisco Media Gateway Control Protocol (MGCP) Foreign Exchange Office (FXO) Device object provides information about registered
                                    Cisco MGCP FXO devices. The following table contains information on Cisco MGCP FXO device counters.

Counters

Counter Description

CallsCompleted

This counter represents the total number of successful calls that were made from the port on an MGCP FXO device.

OutboundBusyAttempts

This counter represents the total number of times that a call through the port on this MGCP FXO device was attempted when
                                                no voice channels were available.

PortStatus

This counter represents the status of the FXO port that is associated with this MGCP FXO device.

#### Cisco MGCP FXS Device

The Cisco MGCP Foreign Exchange Station (FXS) Device object provides information about registered Cisco MGCP FXS devices.
                                    One instance of this object gets created for each port on a Cisco Catalyst 6000 24 port FXS Analog Interface Module gateway.
                                    For example, a fully configured Catalyst 6000 Analog Interface Module would represent 24 separate instances of this object.
                                    The following table contains information on Cisco MGCP FXS device counters.

Counters

Counter Description

CallsCompleted

This counter represents the total number of successful calls that were made from this port on the MGCP FXS device.

OutboundBusyAttempts

This counter represents the total number of times that a call through this port on the MGCP FXS device was attempted when
                                                no voice channels were available.

PortStatus

This counter represents the status of the FXS port that is associated with a MGCP FXS device.

#### Cisco MGCP Gateways

The Cisco MGCP Gateways object provides information about registered MGCP gateways. The following table contains information
                                    on Cisco MGCP gateway counters.

Counters

Counter Description

BRIChannelsActive

This counter represents the number of BRI voice channels that are currently active in a call in the gateway

BRISpansInService

This counter represents the number of BRI spans that are currently available for use in the gateway.

FXOPortsActive

This counter represents the number of FXO ports that are currently active in a call in the gateway.

FXOPortsInService

This counter represents the number of FXO ports that are currently available for use in the gateway.

FXSPortsActive

This counter represents the number of FXS ports that are currently active in a call in the gateway.

FXSPortsInService

This counter represents the number of FXS ports that are currently available for use in the gateway.

PRIChannelsActive

This counter represents the number of PRI voice channels that are currently active in a call in the gateway.

PRISpansInService

This counter represents the number of PRI spans that are currently available for use in the gateway.

T1ChannelsActive

This counter represents the number of T1 CAS voice channels that are currently active in a call in the gateway.

T1SpansInService

This counter represents the number of T1 CAS spans that are currently available for use in the gateway.

#### Cisco MGCP PRI Device

The Cisco MGCP Primary Rate Interface (PRI) Device object provides information about registered Cisco MGCP PRI devices. The
                                    following table contains information on Cisco MGCP PRI device counters.

Counters

Counter Description

CallsActive

This counter represents the number of calls that are currently active (in use) on this MGCP PRI device.

CallsCompleted

This counter represents the total number of successful calls that were made from this MGCP PRI device.

Channel 1 Status through Channel 15 Status (consecutively numbered)

This counter represents the status of the indicated B-Channel that is associated with a MGCP PRI device. Possible values:
                                                0 (Unknown) indicates that the status of the channel could not be determined; 1 (Out of service) indicates that this channel
                                                is not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates
                                                that an active call exists on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-Channel
                                                or for use as a Synch-Channel for E-1.

Channel 16 Status

This counter represents the status of the indicated B-Channel that is associated with a MGCP PRI Device. Possible values:
                                                0-Unknown, 1-Out of service, 2-Idle, 3-Busy, 4-Reserved, for an E1 PRI Interface, this channel is reserved for use as a D-Channel.

Channel 17 Status through Channel 31 Status (consecutively numbered)

This counter represents the status of the indicated B-Channel that is associated with the MGCP PRI Device. 0-Unknown, 1-Out
                                                of service, 2-Idle, 3-Busy, 4-Reserved.

DatalinkInService

This counter represents the state of the Data Link (D-Channel) on the corresponding digital access gateway. This value will
                                                get set to 1 (one) if the Data Link is up (in service) or 0 (zero) if the Data Link is down (out of service).

OutboundBusyAttempts

This counter represents the total number of times that a call through an MGCP PRI device was attempted when no voice channels
                                                were available.

#### Cisco MGCP T1 CAS Device

The Cisco MGCP T1 Channel Associated Signaling (CAS) Device object provides information about registered Cisco MGCP T1 CAS
                                    devices. The following table contains information on Cisco MGCP TI CAS device counters.

Counters

Counter Description

CallsActive

This counter represents the number of calls that are currently active (in use) on this MGCP T1 CAS device.

CallsCompleted

This counter represents the total number of successful calls that were made from this MGCP T1 CAS device.

Channel 1 Status through Channel 24 Status (consecutively numbered)

This counter represents the status of the indicated B-Channel that is associated with an MGCP T1 CAS device. Possible values:
                                                0 (Unknown) indicates the status of the channel could not be determined; 1 (Out of service) indicates that this channel is
                                                not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates that
                                                an active call exists on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-Channel or
                                                for use as a Synch-Channel for E-1.

OutboundBusyAttempts

This counter represents the total number of times that a call through the MGCP T1 CAS device was attempted when no voice channels
                                                were available.

#### Cisco Mobility Manager

The Cisco Mobility Manager object provides information on registered Cisco Unified Mobility Manager devices. The following table contains information on Cisco Unified Mobility Manager device counters.

Counters

Counter Description

MobileCallsAnchored

This counter represents the total number of paths that are associated with single-mode/dual-mode phone call that is currently
                                                anchored on a Unified Communications Manager . Call anchoring occurs when a call enters an enterprise gateway and connects to a mobility application that then uses redirection
                                                to send the call back out an enterprise gateway. For example, this counter increments twice for a dual-mode phone-to-dual-mode
                                                phone call: once for the originating call and once for the terminating call. When the call terminates, this counter decrements
                                                accordingly.

MobilityHandinsAborted

This counter represents the total number of aborted handins.

MobileHandinsCompleted

This counter represents the total number of handins that were completed by dual-mode phones. A completed handin occurs when
                                                the call successfully connects in the enterprise network and the phone moves from WAN to WLAN.

MobilityHandinsFailed

This counter represents the total number of handins (calls on mobile devices that move from cellular to the wireless network)
                                                that failed.

MobilityHandoutsAborted

This counter represents the total number of aborted handouts.

MobileHandoutsCompleted

This counter represents the total number of handouts (calls on mobile devices that move from the enterprise WLAN network to
                                                the cellular network) that were completed. A completed handout occurs when the call successfully connects.

MobileHandoutsFailed

This counter represents the total number of handouts (calls on mobile devices that move from cellular to the wireless network)
                                                that failed.

MobilityFollowMeCallsAttempted

This counter represents the total number of follow-me calls that were attempted.

MobilityFollowMeCallsIgnoredDueToAnswerTooSoon

This counter represents the total number of follow-me calls that were ignored before the AnswerTooSoon timer went off.

MobilityIVRCallsAttempted

This counter represents the total number of attempted IVR calls.

MobilityIVRCallsFailed

This counter represents the total number of failed IVR calls.

MobilityIVRCallsSucceeded

This counter represents the total number of successful IVR calls.

MobilitySCCPDualModeRegistered

This counter represents the total number of dual-mode SCCP devices that are registered.

MobilitySIPDualModeRegistered

This counter represents the total number of dual-mode SIP devices that are registered.

#### Cisco Music On Hold (MOH) Device

The Cisco Music On Hold (MOH) Device object provides information about registered Cisco MOH devices. The following table contains
                                    information on Cisco MOH device counters.

Counters

Counter Description

MOHHighestActiveResources

This counter represents the largest number of simultaneously active MOH connections for an MOH server. This number includes
                                                both multicast and unicast connections.

MOHMulticastResourceActive

This counter represents the number of currently active multicast connections to multicast addresses that are served by an
                                                MOH server.

Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, two streams get used (default audio source + G.711 mu-law
                                                and default audio source + wideband).

MOHMulticastResourceAvailable

This counter represents the number of multicast MOH connections to multicast addresses that are served by an MOH server that
                                                are not active and are still available to be used now for the MOH server.

Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, two streams get used (default audio source + G.711 mu-law
                                                and default audio source + wideband).

MOHOutOfResources

This counter represents the total number of times that the Media Resource Manager attempted to allocate an MOH resource when
                                                all available resources on all MOH servers that are registered with a Unified Communications Manager were already active.

MOHTotalMulticastResources

This counter represents the total number of multicast MOH connections that are allowed to multicast addresses that are served
                                                by an MOH server.

Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, two streams get used (default audio source + G.711 mu-law
                                                and default audio source + wideband).

MOHTotalUnicastResources

This counter represents the total number of unicast MOH connections that are allowed by an MOH server.

Each MOH unicast resource uses one stream.

MOHUnicastResourceActive

This counter represents the number of active unicast MOH connections to an MOH server.

Each MOH unicast resource uses one stream.

MOHUnicastResourceAvailable

This counter represents the number of unicast MOH connections that are not active and are still available to be used now for
                                                an MOH server.

Each MOH unicast resource uses one stream.

#### Cisco MTP Device

The Cisco Media Termination Point (MTP) Device object provides information about registered Cisco MTP devices. The following
                                    table contains information on Cisco MTP device counters.

Counters

Counter Description

OutOfResources

This counter represents the total number of times that an attempt was made to allocate an MTP resource from an MTP device
                                                and failed; for example, because all resources were already in use.

ResourceActive

This counter represents the number of MTP resources that are currently in use (active) for an MTP device.

Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call.

ResourceAvailable

This counter represents the total number of MTP resources that are not active and are still available to be used now for an
                                                MTP device.

Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call.

ResourceTotal

This counter represents the total number of MTP resources that an MTP device provides. This counter equals the sum of the
                                                counters ResourceAvailable and ResourceActive.

#### Cisco Phones

The Cisco Phones object provides information about the number of registered Cisco Unified IP Phone s, including both hardware-based and other station devices.

The CallsAttempted counter represents the number of calls that have been attempted from this phone. This number increases
                                    each time that the phone goes off hook and on hook.

#### Cisco Presence Feature

The Cisco Presence object provides information about presence subscriptions, such as statistics that are related to the speed
                                    dial or call list Busy Lamp Field (BLF) subscriptions. The following table contains information on Cisco Presence feature.

Counters

Counter Description

ActiveCallListAndTrunkSubscriptions

This counter represents the active presence subscriptions for the call list feature as well as presence subscriptions through
                                                SIP trunk.

ActiveSubscriptions

This counter represents all active incoming and outgoing presence subscriptions.

CallListAndTrunkSubscriptionsThrottled

This counter represents the cumulative number of rejected call list and trunk side presence subscriptions due to throttling
                                                for the call list feature.

IncomingLineSideSubscriptions

This counter represents the cumulative number of presence subscriptions that were received on the line side.

IncomingTrunkSideSubscriptions

This counter represents the cumulative number of presence subscriptions that were received on the trunk side.

OutgoingTrunkSideSubscriptions

This counter represents the cumulative number of presence subscriptions that were sent on the trunk side.

#### Cisco QSIG Feature

The Cisco QSIG Feature object provides information regarding the operation of various QSIG features, such as call diversion
                                    and path replacement. The following table contains information on the Cisco QSIG feature counters.

Counters

Counter Description

CallForwardByRerouteCompleted

This counter represents the number of successful calls that has been forwarded by rerouting. Call forward by rerouting enables
                                                the path for a forwarded call to be optimized (minimizes the number of B-Channels in use) from the originator perspective.
                                                This counter gets reset when the Cisco CallManager service parameter Call Forward by Reroute Enabled is enabled or disabled,
                                                or when the Cisco CallManager service restarts.

PathReplacementCompleted

This counter represents the number of successful path replacements that have occurred. Path replacement in a QSIG network
                                                optimizes the path between two edge PINX (PBXs) that are involved in a call. This counter resets when the Cisco CallManager
                                                service parameter Path Replacement Enabled is enabled or disabled, or when the Cisco CallManager service restarts.

#### Cisco Signaling Performance

The Cisco Signaling Performance object provides call-signaling data on transport communications on Unified Communications Manager . The following table contains information on the Cisco Signaling Performance counter.

Counters

Counter Description

UDPPacketsThrottled

This counter represents the total number of incoming UDP packets that were throttled (dropped) because they exceeded the threshold
                                                for the number of incoming packets per second that is allowed from a single IP address. Configure the threshold via the SIP
                                                Station UDP Port Throttle Threshold and SIP Trunk UDP Port Throttle Threshold service parameters in Cisco Unified Communications Manager Administration . This counter increments for every throttled UDP packet that was received since the last restart of the Cisco CallManager
                                                Service.

#### Cisco SIP

The Cisco Session Initiation Protocol (SIP) object provides information about configured SIP devices. The following table
                                    contains information on the Cisco SIP counters.

Counters

Counter Description

CallsActive

This counter represents the number of calls that are currently active (in use) on this SIP device.

CallsAttempted

This counter represents the number of calls that have been attempted on this SIP device, including both successful and unsuccessful
                                                call attempts.

CallsCompleted

This counter represents the number of calls that were actually connected (a voice path was established) from a SIP device.
                                                This number increases when the call terminates.

CallsInProgress

This counter represents the number of calls that are currently in progress on a SIP device, including all active calls. When
                                                all calls that are in progress are connected, the number of CallsInProgress equals the number of CallsActive.

VideoCallsActive

This counter represents the number of video calls with streaming video connections that are currently active (in use) on this
                                                SIP device.

VideoCallsCompleted

This counter represents the number of video calls that were actually connected with video streams for this SIP device. This
                                                number increments when the call terminates.

#### Cisco SIP Normalization

The Cisco SIP Normalization performance object contains counters that allow you to monitor aspects of the normalization script,
                                    including initialization errors, runtime errors, and script status. Each device that has an associated script causes a new
                                    instance of these counters to be created. The following table contains information on the Cisco SIP Normalization counters..

Display Name

Description

DeviceResetAutomatically

This counter indicates the number of times that Unified Communications Manager automatically resets the device (SIP trunk). The device reset is based on the values that are specified in the Script Execution
                                                Error Recovery Action and System Resource Error Recovery Action fields on the SIP Normalization Script Configuration window
                                                in Cisco Unified Communications Manager Administration . When the device (SIP trunk) is reset due to script errors, the counter value increments. This count restarts when the device
                                                is reset manually.

DeviceResetManually

This counter indicates the number of times that the device (SIP trunk) is reset manually in Cisco Unified Communications Manager Administration or by other methods, such as AXL. When the device associated with a script is reset due to configuration changes, the counter
                                                value increments.

The counter restarts in the following situations:

- The SIP trunk is deleted.

- The script on the trunk gets changed or deleted.

- Unified Communications Manager restarts.

ErrorExecution

This counter represents the number of execution errors that occurred while the script executed. Execution errors can occur
                                                while a message handler executes. Execution errors can be caused by resource errors, an argument mismatch in a function call,
                                                and so on.

When an execution error occurs, Unified Communications Manager performs the following actions:

- Automatically restores the message to the original content before applying additional error handling actions.

- Increments the value of the counter.

- Takes appropriate action based on the configuration of the Script Execution Error Recovery Action and System Resource Error
                                                   Recovery Action fields in Cisco Unified Communications Manager Administration .

Check the SIPNormalizationScriptError alarm for details, including the line number in the script that failed. Correct the
                                                script problem, upload the corrected script as needed, and reset the trunk. This counter increments every time an execution
                                                error occurs. This counter provides a count from the most recent trunk reset that involved a script configuration change.
                                                (A device reset alone does not restart the count; the script configuration must also change before the reset occurs.)

If the counter continues to increment after you fix the script problem, examine the script again.

ErrorInit

This counter represents the number of times a script error occurred after the script successfully loaded into memory, but
                                                failed to initialize in Unified Communications Manager . A script can fail to initialize due to resource errors, an argument mismatch in a function call, the expected table was
                                                not returned, and so on.

Check the SIPNormalizationScriptError alarm for details, including the line number in the script that failed. Correct the
                                                script problem, upload the corrected script as needed, and reset the trunk. This counter increments every time an initialization
                                                error occurs. This counter provides a count from the most recent trunk reset that was accompanied by a script configuration
                                                change. (A device reset alone does not restart the count; the script configuration must also change before the reset occurs.)
                                                If the counter continues to increment after you fix the script problem, examine the script again. When the error occurs during
                                                initialization, Unified Communications Manager automatically disables the script.

ErrorInternal

This counter indicates the number of internal errors that occurred while the script executed. Internal errors are very rare.
                                                If the value in this counter is higher than zero, a defect exists in the system that is not related to the script content
                                                or execution. Collect SDI traces and contact the Technical Assistance Center (TAC).

ErrorLoad

This counter represents the number of times a script error occurred when the script loaded into memory in Unified Communications Manager . A script can fail to load due to memory issues or syntax errors.

Check the SIPNormalizationScriptError alarm for details. Check the script syntax for errors, upload the corrected script as
                                                needed, and reset the trunk. This counter increments every time a load error occurs. This counter provides a count from the
                                                most recent trunk reset that was accompanied by a script configuration change. (A device reset alone will not restart the
                                                count; the script configuration must also change before the reset occurs.) If the counter continues to increment even after
                                                you fix the script problem, examine the script again.

ErrorResource

This counter indicates whether the script encountered a resource error.

Two kinds of resource errors exist: exceeding the value in the Memory Threshold field and exceeding the value in the Lua Instruction
                                                Threshold field. (Both fields display on the SIP Normalization Script Configuration window in Cisco Unified Communications Manager Administration .) If either condition occurs, Unified Communications Manager immediately closes the script and issues the SIPNormalizationScriptError alarm.

If a resource error occurs while the script loads or initializes, the script is disabled. If a resource error occurs during
                                                execution, the configured system resource error recovery action is taken. (The setting of the System Resource Error Recovery
                                                Action field on the SIP Normalization Script Configuration window in Cisco Unified Communications Manager Administration defines this action.)

MemoryUsage

This counter specifies the amount of memory, in bytes, that the script consumes. This counter increases and decreases to match
                                                the amount of memory that the script uses. This count gets cleared when the script closes (because a closed script does not
                                                consume memory) and restarts when the script opens (gets enabled). A high number in this counter indicates a resource problem.
                                                Check the MemoryUsagePercentage counter and the SIPNormalizationResourceWarning alarm, which occur when the resource consumption
                                                exceeds an internally set threshold.

MemoryUsagePercentage

This counter specifies the percentage of the total amount of memory that the script consumes.

The value in this counter is derived by dividing the value in the MemoryUsage counter by the value in the Memory Threshold
                                                field (in the SIP Normalization Script Configuration window) and multiplying the result by 100 to arrive at a percentage.

This counter increases and decreases in accordance with the MemoryUsage counter. This count gets cleared when the script closes
                                                (because closed scripts do not consume memory) and restarts when the script opens (gets enabled). When this counter reaches
                                                the internally controlled resource threshold, the SIPNormalizationResourceWarning alarm is issued.

MessageRollback

This counter indicates the number of times that the system automatically rolled back a message. The system rolls back the
                                                message by using the error handling that is specified in the Script Execution Error Recovery Action field in the SIP Normalization
                                                Script Configuration window in Cisco Unified Communications Manager Administration.

When an execution error occurs, Unified Communications Manager automatically restores the message to the original content before applying additional error handling actions. If error handling
                                                specifies Rollback only, no further action is taken beyond rolling back to the original message before the normalization attempt.
                                                For the other possible Script Execution Error Recovery Actions, message rollback always occurs first, followed by the specified
                                                action, such as disabling the script, resetting the script automatically, or resetting the trunk automatically.

msgAddContentBody

This counter represents the number of times that the script added a content body to the message. If you are using the msg:addContentBody
                                                API in the script, this counter increases each time that the msg:addContentBody API executes successfully. If the counter
                                                behavior is not as expected, examine the script logic for errors.

msgAddHeader

This counter represents the number of times that the script added a SIP header to the message. If you are using the msg:addHeader
                                                API in the script, this counter increases each time that the msg:addHeader API executes successfully. If the counter behavior
                                                is not as expected, examine the script logic for errors.

msgAddHeaderUriParameter

This counter represents the number of times that the script added a SIP header URI parameter to a SIP header in the message.
                                                If you are using the msg:addHeaderUriParameter API in the script, this counter increases each time that the msg:addHeaderUriParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

msgAddHeaderValueParameter

This counter represents the number of times that the script added a SIP header value parameter to a SIP header in the message.
                                                If you are using the msg:addHeaderValueParameter API in the script, this counter increases each time that the msg:addHeaderValueParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

msgApplyNumberMask

This counter represents the number of times that the script applied a number mask to a SIP header in the message. If you are
                                                using the msg:applyNumberMask API in the script, this counter increases each time that the msg:applyNumberMask API executes
                                                successfully. If the counter behavior is not as expected, examine the script logic for errors.

msgBlock

This counter represents the number of times that the script blocked a message. If you are using the msg:block API in the script,
                                                this counter increases each time that the msg:block API executes successfully. If the counter behavior is not as expected,
                                                examine the script logic for errors.

msgConvertDiversionToHI

This counter represents the number of times that the script converted Diversion headers into History-Info headers in the message.
                                                If you are using the msg:convertDiversionToHI API in the script, this counter increases each time that the msg:convertDiversionToHI
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

msgConvertHIToDiversion

This counter represents the number of times that the script converted Diversion headers into History-Info headers in the message.
                                                If you are using the msg:convertDiversionToHI API in the script, this counter increases each time that the msg:convertDiversionToHI
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

msgModifyHeader

This counter represents the number of times that the script modified a SIP header in the message. If you are using the msg:modifyHeader
                                                API in the script, this counter increases each time that the msg:modifyHeader API executes successfully. If the counter behavior
                                                is not as expected, examine the script logic for errors.

msgRemoveContentBody

This counter represents the number of times that the script removed a content body from the message. If you are using the
                                                msg:removeContentBody API in the script, this counter increases each time that the msg:removeContentBody API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors.

msgRemoveHeader

This counter represents the number of times that the script removed a SIP header from the message. If you are using the msg:removeHeader
                                                API in the script, this counter increases each time that the msg:removeHeader API executes successfully. If the counter behavior
                                                is not as expected, examine the script logic for errors.

msgRemoveHeaderValue

This counter represents the number of times that the script removed a SIP header value from the message. If you are using
                                                the msg:removeHeaderValue API in the script, this counter increases each time that the msg:removeHeaderValue API executes
                                                successfully. If the counter behavior is not as expected, examine the script logic for errors.

msgSetRequestUri

This counter represents the number of times that the script modified the request URI in the message. If you are using the
                                                msg:setRequestUri API in the script, this counter increases each time that the msg:setRequestUri API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors.

msgSetResponseCode

This counter represents the number of times that the script modified the response code and/or response phrase in the message.
                                                If you are using the msg:setResponseCode API in the script, this counter increases each time that the msg:setResponseCode
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

msgSetSdp

This counter represents the number of times that the script set the SDP in the message. If you are using the msg:setSdp API
                                                in the script, this counter increases each time that the msg:setSdp API executes successfully. If the counter behavior is
                                                not as expected, examine the script logic for errors.

ptAddContentBody

This counter represents the number of times that the script added a content body to the PassThrough (pt) object. If you are
                                                using the pt:addContentBody API in the script, this counter increases each time that the pt:addContentBody API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors.

ptAddHeader

This counter represents the number of times that the script added a SIP header to the PassThrough (pt) object. If you are
                                                using the pt:addHeader API in the script, this counter increases each time that the pt:addHeader API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors.

ptAddHeaderUriParameter

This counter represents the number of times that the script added a SIP header URI parameter to the PassThrough (pt) object.
                                                If you are using the pt:addHeaderUriParameter API in the script, this counter increases each time that the pt:addHeaderUriParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

ptAddHeaderValueParameter

This counter represents the number of times that the script added a SIP header value parameter to the PassThrough (pt) object.
                                                If you are using the pt:addHeaderValueParameter API in the script, this counter increases each time that the pt:addHeaderValueParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

ptAddRequestUriParameter

This counter represents the number of times that the script added a request URI parameter to the PassThrough (pt) object.
                                                If you are using the pt:addRequestUriParameter API in the script, this counter increases each time that the pt:addRequestUriParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors.

ScriptActive

This counter indicates whether the script is currently active (running on the trunk). The following values display for the
                                                counter:

- 0—Indicates that the script is closed (disabled).

- 1—Indicates that the script is open and operational.

To open the script that should be running on this trunk, perform the following actions:

Check for any alarms that might indicate why the script is not open.

Correct any errors.

Upload a new script if necessary.

Reset the trunk.

ScriptClosed

This counter indicates the number of times that Unified Communications Manager has closed the script.

When the script is closed, it is not enabled on this device.

Unified Communications Manager closes the script under one of the following conditions:

- The device was reset manually.

- The device was reset automatically (due to an error).

- The device was deleted.

This count restarts when the SIP trunk is reset after a change to the script configuration and when Unified Communications Manager restarts.

ScriptDisabledAutomatically

This counter indicates the number of times that the system automatically disabled the script. The values that are specified
                                                in the Script Execution Error Recovery Action and System Resource Error Recovery Action fields in the SIP Normalization Script
                                                Configuration window in Cisco Unified Communications Manager Administration determine whether the script is disabled. The
                                                script also gets disabled as a result of script error conditions that are encountered during loading and initialization. This
                                                counter provides a count from the most recent manual device reset that involved a script configuration change (a device reset
                                                alone does not restart the count; the script must also have changed before the reset occurs). This counter increments every
                                                time Unified Communications Manager automatically disables a script due to script errors.

If the number in this counter is higher than expected, perform the following actions:

- Check for SIPNormalizationScriptError alarm and SIPNormalizationAutoResetDisabled alarm.

- Check for any resource-related alarms and counters in RTMT to determine whether a resource issue is occurring.

- Check for any unexpected SIP normalization events in the SDI trace files.

ScriptOpened

This counter indicates the number of times that the Unified Communications Manager attempted to open the script. For the a script to open, it must load into memory in Unified Communications Manager , initialize, and be operational. A number greater than one in this counter means that Unified Communications Manager has made more than one attempt to open the script on this SIP trunk, either for an expected reason or due to an error during
                                                loading or initialization. The error can occur due to execution errors or resource errors or invalid syntax in the script.
                                                Expect this counter to be greater than one if any of these counters increment: DeviceResetManually, DeviceResetAutomatically,
                                                or ScriptResetAutomatically. The DeviceResetManually counter increments when an expected event, such as a maintenance window
                                                on the SIP trunk, causes the script to close.

If the number in this counter is high for an unexpected reason, perform the following actions:

- Check for alarms, such as the SIPNormalizationScriptClosed, SIPNormalizationScriptError, or SIPNormalizationResourceWarning.

- Check resource-related alarms and counters in RTMT to determine whether a resource issue is occurring.

- Check for any unexpected SIP normalization events in the SDI trace files.

This count restarts when the SIP trunk resets after a script configuration change and when Unified Communications Manager restarts.

ScriptResetAutomatically

This counter indicates the number of times that the system automatically reset the script. The script resets based on the
                                                values that are specified in the Script Execution Error Recovery Action and System Resource Error Recovery Action fields in
                                                the SIP Normalization Script Configuration window in Cisco Unified Communications Manager Administration. This counter specifies
                                                a count of the number of automatic script resets after the last manual device reset; this counter increments every time the Unified Communications Manager automatically resets a script due to script errors.

If the number in this counter is higher than expected, perform the following actions:

- Check for a SIPNormalizationScriptError alarm.

- Check for any resource-related alarms and counters in RTMT to determine whether a resource issue is occurring.

- Check for any unexpected SIP normalization events in the SDI trace files.

#### Cisco SIP Stack

The Cisco SIP Stack object provides information about Session Initiation Protocol (SIP) stack statistics that are generated
                                    or used by SIP devices such as SIP Proxy, SIP Redirect Server, SIP Registrar, and SIP User Agent. The following table contains
                                    information on Cisco SIP Stack counters.

Counters

Counter Description

AckIns

This counter represents the total number of ACK requests that the SIP device received.

AckOuts

This counter represents the total number of ACK requests that the SIP device sent.

ByeIns

This counter represents the total number of BYE requests that the SIP device received. This number includes retransmission.

ByeOuts

This counter represents the total number of BYE requests that the SIP device sent. This number includes retransmission.

CancelIns

This counter represents the total number of CANCEL requests that the SIP device received. This number includes retransmission.

CancelOuts

This counter represents the total number of CANCEL requests that the SIP device sent. This number includes retransmission.

CCBsAllocated

This counter represents the number of Call Control Blocks (CCB) that are currently in use by the SIP stack. Each active SIP
                                                dialog uses one CCB.

GlobalFailedClassIns

This counter represents the total number of 6xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses indicates that a SIP device, that is providing a client function, received a failure response message.
                                                Generally, the responses indicate that a server had definitive information on a particular called party and not just the particular
                                                instance in the Request-URI.

GlobalFailedClassOuts

This counter represents the total number of 6xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses indicates that a SIP device, that is providing a server function, received a failure response message.
                                                Generally, the responses indicate that a server had definitive information on a particular called party and not just the particular
                                                instance in the Request-URI.

InfoClassIns

This counter represents the total number of 1xx class SIP responses that the SIP device received. This includes retransmission.
                                                This class of responses provides information on the progress of a SIP request.

InfoClassOuts

This counter represents the total number of 1xx class SIP responses that the SIP device sent. This includes retransmission.
                                                This class of responses provides information on the progress of processing a SIP request.

InfoIns

This counter represents the total number of INFO requests that the SIP device has received. This number includes retransmission.

InfoOuts

This counter represents the total number of INFO requests that the SIP device has sent. This number includes retransmission.

InviteIns

This counter represents the total number of INVITE requests that the SIP device received. This number includes retransmission.

InviteOuts

This counter represents the total number of INVITE requests that the SIP device sent. This number includes retransmission.

NotifyIns

This counter represents the total number of NOTIFY requests that the SIP device received. This number includes retransmission.

NotifyOuts

This counter represents the total number of NOTIFY requests that the SIP device sent. This number includes retransmission.

OptionsIns

This counter represents the total number of OPTIONS requests that the SIP device received. This number includes retransmission.

OptionsOuts

This counter represents the total number of OPTIONS requests that the SIP device sent. This number includes retransmission.

PRAckIns

This counter represents the total number of PRACK requests that the SIP device received. This number includes retransmission.

PRAckOuts

This counter represents the total number of PRACK requests that the SIP device sent. This number includes retransmission.

PublishIns

This counter represents the total number of PUBLISH requests that the SIP device received. This number includes retransmissions.

PublishOuts

This counter represents the total number of PUBLISH requests that the SIP device sent. This number includes retransmission

RedirClassIns

This counter represents the total number of 3xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses provides information about redirections to addresses where the callee may be reachable.

RedirClassOuts

This counter represents the total number of 3xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses provides information about redirections to addresses where the callee may be reachable.

ReferIns

This counter represents the total number of REFER requests that the SIP device received. This number includes retransmission.

ReferOuts

This counter represents the total number of REFER requests that the SIP device sent. This number includes retransmission.

RegisterIns

This counter represents the total number of REGISTER requests that the SIP device received. This number includes retransmission.

RegisterOuts

This counter represents the total number of REGISTER requests that the SIP device sent. This number includes retransmission.

RequestsFailedClassIns

This counter represents the total number of 4xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses indicates a request failure by a SIP device that is providing a client function.

RequestsFailedClassOuts

This counter represents the total number of 4xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses indicates a request failure by a SIP device that is providing a server function.

RetryByes

This counter represents the total number of BYE retries that the SIP device sent. To determine the number of first BYE attempts,
                                                subtract the value of this counter from the value of the sipStatsByeOuts counter.

RetryCancels

This counter represents the total number of CANCEL retries that the SIP device sent. To determine the number of first CANCEL
                                                attempts, subtract the value of this counter from the value of the sipStatsCancelOuts counter.

RetryInfo

This counter represents the total number of INFO retries that the SIP device sent. To determine the number of first INFO attempts,
                                                subtract the value of this counter from the value of the sipStatsInfoOuts counter.

RetryInvites

This counter represents the total number of INVITE retries that the SIP device sent. To determine the number of first INVITE
                                                attempts, subtract the value of this counter from the value of the sipStatsInviteOuts counter.

RetryNotify

This counter represents the total number of NOTIFY retries that the SIP device sent. To determine the number of first NOTIFY
                                                attempts, subtract the value of this counter from the value of the sipStatsNotifyOuts counter.

RetryPRAck

This counter represents the total number of PRACK retries that the SIP device sent. To determine the number of first PRACK
                                                attempts, subtract the value of this counter from the value of the sipStatsPRAckOuts counter.

RetryPublish

This counter represents the total number of PUBLISH retries that the SIP device sent. To determine the number of first PUBLISH
                                                attempts, subtract the value of this counter from the value of the sipStatsPublishOuts counter.

RetryRefer

This counter represents the total number of REFER retries that the SIP device sent. To determine the number of first REFER
                                                attempts, subtract the value of this counter from the value of the sipStatsReferOuts counter.

RetryRegisters

This counter represents the total number of REGISTER retries that the SIP device sent. To determine the number of first REGISTER
                                                attempts, subtract the value of this counter from the value of the sipStatsRegisterOuts counter.

RetryRel1xx

This counter represents the total number of Reliable 1xx retries that the SIP device sent.

RetryRequestsOut

This counter represents the total number of Request retries that the SIP device sent.

RetryResponsesFinal

This counter represents the total number of Final Response retries that the SIP device sent.

RetryResponsesNonFinal

This counter represents the total number of non-Final Response retries that the SIP device sent.

RetrySubscribe

This counter represents the total number of SUBSCRIBE retries that the SIP device sent. To determine the number of first SUBSCRIBE
                                                attempts, subtract the value of this counter from the value of the sipStatsSubscribeOuts counter.

RetryUpdate

This counter represents the total number of UPDATE retries that the SIP device sent. To determine the number of first UPDATE
                                                attempts, subtract the value of this counter from the value of the sipStatsUpdateOuts counter.

SCBsAllocated

This counter represents the number of Subscription Control Blocks (SCB) that are currently in use by the SIP stack. Each subscription
                                                uses one SCB.

ServerFailedClassIns

This counter represents the total number of 5xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses indicates that failure responses were received by a SIP device that is providing a client function.

ServerFailedClassOuts

This counter represents the total number of 5xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses indicates that failure responses were received by a SIP device that is providing a server function.

SIPGenericCounter1

Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes.

SIPGenericCounter2

Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes.

SIPGenericCounter3

Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes.

SIPGenericCounter4

Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes.

SIPHandlerSDLQueueSignalsPresent

This counter represents the number of SDL signals that are currently on the four SDL priority queues of the SIPHandler component.
                                                The SIPHandler component contains the SIP stack.

StatusCode1xxIns

This counter represents the total number of 1xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 1xx responses:

- 100 Trying

- 180 Ringing

- 181 Call is being forwarded

- 182 Queued

- 183 Session Progress

StatusCode1xxOuts

This counter represents the total number of 1xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 1xx responses:

- 100 Trying

- 180 Ringing

- 181 Call is being forwarded

- 182 Queued

- 183 Session Progress

StatusCode2xxIns

This counter represents the total number of 2xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 2xx responses:

- 200 OK

- 202 Success Accepted

StatusCode2xxOuts

This counter represents the total number of 2xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 2xx responses:

- 200 OK

- 202 Success Accepted

StatusCode3xxins

This counter represents the total number of 3xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 3xx responses:

- 300 Multiple Choices

- 301 Moved Permanently

- 302 Moved Temporarily

- 303 Incompatible Bandwidth Units

- 305 Use Proxy

- 380 Alternative Service

StatusCode302Outs

This counter represents the total number of 302 Moved Temporarily response messages, including retransmission, that the SIP
                                                device sent.

StatusCode4xxIns

This counter represents the total number of 4xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 4xx responses:

- 400 Bad Request

- 401 Unauthorized

- 402 Payment Required

- 403 Forbidden

- 404 Not Found

- 405 Method Not Allowed

- 406 Not Acceptable

- 407 Proxy Authentication Required

- 408 Request Timeout

- 409 Conflict

- 410 Gone

- 413 Request Entity Too Large

- 414 Request-URI Too Long

- 415 Unsupported Media Type

- 416 Unsupported URI Scheme

- 417 Unknown Resource Priority

- 420 Bad Extension

- 422 Session Expires Value Too Small

- 423 Interval Too Brief

- 480 Temporarily Unavailable

- 481 Call/Transaction Does Not Exist

- 482 Loop Detected

- 483 Too Many Hops

- 484 Address Incomplete

- 485 Ambiguous

- 486 Busy Here

- 487 Request Terminated

- 488 Not Acceptable Here

- 489 Bad Subscription Event

- 491 Request Pending

StatusCode4xxOuts

This counter represents the total number of 4xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 4xx responses:

- 400 Bad Request

- 401 Unauthorized

- 402 Payment Required

- 403 Forbidden

- 404 Not Found

- 405 Method Not Allowed

- 406 Not Acceptable

- 407 Proxy Authentication Required

- 408 Request Timeout

- 409 Conflict

- 410 Gone

- 413 Request Entity Too Large

- 414 Request-URI Too Long

- 415 Unsupported Media Type

- 416 Unsupported URI Scheme

- 417 Unknown Resource Priority

- 420 Bad Extension

- 422 Session Expires Value Too Small

- 423 Interval Too Brief

- 480 Temporarily Unavailable

- 481 Call/Transaction Does Not Exist

- 482 Loop Detected

- 483 Too Many Hops

- 484 Address Incomplete

- 485 Ambiguous

- 486 Busy Here

- 487 Request Terminated

- 488 Not Acceptable Here

- 489 Bad Subscription Event

- 491 Request Pending

StatusCode5xxIns

This counter represents the total number of 5xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 5xx responses:

- 500 Server Internal Error

- 501 Not Implemented

- 502 Bad Gateway

- 503 Service Unavailable

- 504 Server Timeout

- 505 Version Not Supported

- 580 Precondition Failed

StatusCode5xxOuts

This counter represents the total number of 5xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 5xx responses:

- 500 Server Internal Error

- 501 Not Implemented

- 502 Bad Gateway

- 503 Service Unavailable

- 504 Server Timeout

- 505 Version Not Supported

- 580 Precondition Failed

StatusCode6xxIns

This counter represents the total number of 6xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 6xx responses:

- 600 Busy Everywhere

- 603 Decline

- 604 Does Not Exist Anywhere

- 606 Not Acceptable

StatusCode6xxOuts

This counter represents the total number of 6xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 6xx responses:

- 600 Busy Everywhere

- 603 Decline

- 604 Does Not Exist Anywhere

- 606 Not Acceptable

SubscribeIns

This counter represents the total number of SUBSCRIBE requests that the SIP device received. This number includes retransmission.

SubscribeOuts

This counter represents the total number of SUBSCRIBE requests that the SIP device sent. This number includes retransmission.

SuccessClassIns

This counter represents the total number of 2xx class SIP responses that the SIP device received. This includes retransmission.
                                                This class of responses provides information on the successful completion of a SIP request.

SuccessClassOuts

This counter represents the total number of 2xx class SIP responses that the SIP device sent. This includes retransmission.
                                                This class of responses provides information on the successful completion of a SIP request.

SummaryRequestsIn

This counter represents the total number of SIP request messages that the SIP device received. This number includes retransmissions.

SummaryRequestsOut

This counter represents the total number of SIP request messages that the device sent. This number includes messages that
                                                originate on the device and messages that are being relayed by the device. When a particular message gets sent more than once,
                                                each transmission gets counted separately; for example, a message that is re-sent as a retransmission or as a result of forking.

SummaryResponsesIn

This counter represents the total number of SIP response messages that the SIP device received. This number includes retransmission.

SummaryResponsesOut

This counter represents the total number of SIP response messages that the SIP device sent (originated and relayed). This
                                                number includes retransmission.

UpdateIns

This counter represents the total number of UPDATE requests that the SIP device received. This number includes retransmission.

UpdateOuts

This counter represents the total number of UPDATE requests that the SIP device sent. This number includes retransmission.

#### Cisco SIP Station

The Cisco SIP Station object provides information about SIP line-side devices. The following table contains information on
                                    the Cisco SIP Station counters.

Counters

Counter Description

ConfigMismatchesPersistent

This counter represents the number of times that a phone that is running SIP was persistently unable to register due to a
                                                configuration version mismatch between the TFTP server and Unified Communications Manager since the last restart of the Unified Communications Manager . This counter increments each time that Unified Communications Manager cannot resolve the mismatch and manual intervention is required (such as a configuration update or device reset).

ConfigMismatchesTemporary

This counter represents the number of times that a phone that is running SIP was temporarily unable to register due to a configuration
                                                version mismatch between the TFTP server and Unified Communications Manager since the last restart of the Cisco CallManager service. This counter increments each time Unified Communications Manager can resolve the mismatch automatically.

DBTimeouts

This counter represents the number of new registrations that failed because a timeout occurred while the system was attempting
                                                to retrieve the device configuration from the database.

NewRegAccepted

This counter represents the total number of new REGISTRATION requests that have been removed from the NewRegistration queue
                                                and processed since the last restart of the Cisco CallManager service.

NewRegQueueSize

This counter represents the number of REGISTRATION requests that are currently on the NewRegistration queue. The system places
                                                REGISTRATION requests that are received from devices that are not currently registered on this queue before they are processed.

NewRegRejected

This counter represents the total number of new REGISTRATION requests that were rejected with a 486 Busy Here response and
                                                not placed on the NewRegistration queue since the last restart of the Cisco CallManager service. The system rejects REGISTRATION
                                                requests if the NewRegistration queue exceeds a programmed size.

TokensAccepted

This counter represents the total number of token requests that have been granted since the last Unified Communications Manager restart. Unified Communications Manager grants tokens as long as the number of outstanding tokens remains below the number that is specified in the Cisco CallManager
                                                service parameter Maximum Phone Fallback Queue Depth.

TokensOutstanding

This counter represents the number of devices that have been granted a token but have not yet registered. The system requires
                                                that devices that are reconnecting to a higher priority Unified Communications Manager server be granted a token before registering. Tokens protect Unified Communications Manager from being overloaded with registration requests when it comes back online after a failover situation.

TokensRejected

This counter represents the total number of token requests that have been rejected since the last Unified Communications Manager restart. Unified Communications Manager will reject token request if the number of outstanding tokens is greater than the number that is specified in the Cisco CallManager
                                                service parameter Maximum Phone Fallback Queue Depth.

#### Cisco SW Conf Bridge Device

The Cisco SW Conference Bridge Device object provides information about registered Cisco software conference bridge devices.
                                    The following table contains information on the Cisco software conference bridge device counters.

Counters

Counter Description

OutOfResources

This counter represents the total number of times that an attempt was made to allocate a conference resource from a SW conference
                                                device and failed because all resources were already in use.

ResourceActive

This counter represents the number of resources that are currently in use (active) for a SW conference device. One resource
                                                represents one stream.

ResourceAvailable

This counter represents the total number of resources that are not active and are still available to be used now for a SW
                                                conference device. One resource represents one stream.

ResourceTotal

This counter represents the total number of conference resources that a SW conference device provides. One resource represents
                                                one stream.This counter equals the sum of the ResourceAvailable and ResourceActive counters.

SWConferenceActive

This counter represents the number of software-based conferences that are currently active (in use) on a SW conference device.

SWConferenceCompleted

This counter represents the total number of conferences that have been allocated and released on a SW conference device. A
                                                conference starts when the first call connects to the bridge. The conference completes when the last call disconnects from
                                                the bridge.

#### Cisco TFTP Server

The Cisco Trivial File Transfer Protocol (TFTP) Server object provides information about the Cisco TFTP server. The following
                                    table contains information on Cisco TFTP server counters.

Counters

Counter Description

BuildAbortCount

This counter represents the number of times that the build process aborted when it received a Build all request. This counter
                                                increases when building of device/unit/softkey/dial rules gets aborted as a result of group level change notifications.

BuildCount

This counter represents the number of times since the TFTP service started that the TFTP server has built all the configuration
                                                files in response to a database change notification that affects all devices. This counter increases by one every time the
                                                TFTP server performs a new build of all the configuration files.

BuildDeviceCount

This counter represents the number of devices that were processed in the last build of all the configuration files. This counter
                                                also updates while processing device change notifications. The counter increases when a new device is added and decreases
                                                when an existing device is deleted.

BuildDialruleCount

This counter represents the number of dial rules that were processed in the last build of the configuration files. This counter
                                                also updates while processing dial rule change notifications. The counter increases when a new dial rule is added and decreases
                                                when an existing dial rule is deleted.

BuildDuration

This counter represents the time in seconds that it took to build the last configuration files.

BuildSignCount

This counter represents the number of security-enabled phone devices for which the configuration file was digitally signed
                                                with the Unified Communications Manager server key in the last build of all the configuration files. This counter also updates while processing security-enabled
                                                phone device change notifications.

BuildSoftKeyCount

This counter represents the number of softkeys that were processed in the last build of the configuration files. This counter
                                                increments when a new softkey is added and decrements when an existing softkey is deleted.

BuildUnitCount

This counter represents the number of gateways that were processed in the last build of all the configuration files. This
                                                counter also updates while processing unit change notifications. The counter increases when a new gateway is added and decreases
                                                when an existing gateway is deleted.

ChangeNotifications

This counter represents the total number of all the Unified Communications Manager database change notifications that the TFTP server received. Each time that a device configuration is updated in Cisco Unified Communications Manager Administration , the TFTP server gets sent a database change notification to rebuild the XML file for the updated device.

DeviceChangeNotifications

This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete configuration files for devices.

DialruleChangeNotifications

This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete configuration files for dial rules.

EncryptCount

This counter represents the number of configuration files that were encrypted. This counter gets updated each time a configuration
                                                file is successfully encrypted

GKFoundCount

This counter represents the number of GK files that were found in the cache. This counter gets updated each time a GK file
                                                is found in the cache

GKNotFoundCount

This counter represents the number of GK files that were not found in the cache. This counter gets updated each time a request
                                                to get a GK file results in the cache not finding it

HeartBeat

This counter represents the heartbeat of the TFTP server. This incremental count indicates that the TFTP server is up and
                                                running. If the count does not increase, this means that the TFTP server is down.

HttpConnectRequests

This counter represents the number of clients that are currently requesting the HTTP GET file request.

HttpRequests

This counter represents the total number of file requests (such as requests for XML configuration files, phone firmware files,
                                                audio files, and so on.) that the HTTP server handled. This counter represents the sum total of the following counters since
                                                the HTTP service started: RequestsProcessed, RequestsNotFound, RequestsOverflow, RequestsAborted, and RequestsInProgress.

HttpRequestsAborted

This counter represents the total number of HTTP requests that the HTTP server. canceled (aborted) unexpectedly. Requests
                                                could get aborted if the requesting device cannot be reached (for instance, the device lost power) or if the file transfer
                                                was interrupted due to network connectivity problems.

HttpRequestsNotFound

This counter represents the total number of HTTP requests where the requested file was not found. When the HTTP server does
                                                not find the requested file, a message gets sent to the requesting device.

HttpRequestsOverflow

This counter represents the total number of HTTP requests that were rejected when the maximum number of allowable client connections
                                                was reached. The requests may have arrived while the TFTP server was building the configuration files or because of some other
                                                resource limitation. The Cisco TFTP advanced service parameter, Maximum Serving Count, sets the maximum number of allowable
                                                connections.

HttpRequestsProcessed

This counter represents the total number of HTTP requests that the HTTP server. successfully processed.

HttpServedFromDisk

This counters represents the number of requests that the HTTP server completed with the files that are on disk and not cached
                                                in memory.

LDFoundCount

This counter represents the number of LD files that were found in the cache. This counter gets updated each time that a LD
                                                file is found in cache memory.

LDNotFoundCount

This counter represents the number of LD files that were not found in cache memory. This counter gets updated each time that
                                                a request to get an LD file results in the cache not finding it.

MaxServingCount

This counter represents the maximum number of client connections that the TFTP can serve simultaneously. The Cisco TFTP advanced
                                                service parameter, Maximum Serving Count, sets this value.

Requests

This counter represents the total number of file requests (such as requests for XML configuration files, phone firmware files,
                                                audio files, and so on.) that the TFTP server handles. This counter represents the sum total of the following counters since
                                                the TFTP service started: RequestsProcessed, RequestsNotFound, RequestsOverflow, RequestsAborted, and RequestsInProgress.

RequestsAborted

This counter represents the total number of TFTP requests that the TFTP server canceled (aborted) unexpectedly. Requests could
                                                get aborted if the requesting device cannot be reached (for instance, the device lost power) or if the file transfer was interrupted
                                                due to network connectivity problems.

RequestsInProgress

This counter represents the number of file requests that the TFTP server currently is processing. This counter increases for
                                                each new file request and decreases for each file request that completes. This counter indicates the current load of the TFTP
                                                server.

RequestsNotFound

This counter represents the total number of TFTP requests for which the requested file was not found. When the TFTP server
                                                does not find the requested file, a message gets sent to the requesting device. If this counter increments in a cluster that
                                                is configured as secure, this event usually indicates an error condition. If, however, the cluster is configured as non-secure,
                                                it is normal for the CTL file to be absent (not found), which results in a message being sent to the requesting device and
                                                a corresponding increment in this counter. For non-secure clusters, this normal occurrence does not represent an error condition.

RequestsOverflow

This counter represents the total number of TFTP requests that were rejected because the maximum number of allowable client
                                                connections was exceeded, because requests arrived while the TFTP server was building the configuration files, or because
                                                of some other resource limitation. The Cisco TFTP advanced service parameter, Maximum Serving Count, sets the maximum number
                                                of allowable connections.

RequestsProcessed

This counter represents the total number of TFTP requests that the TFTP server successfully processed.

SegmentsAcknowledged

This counter represents the total number of data segments that the client devices acknowledged. Files get sent to the requesting
                                                device in data segments of 512 bytes, and for each 512-byte segment, the device sends the TFTP server an acknowledgment message.
                                                Each additional data segment gets sent upon receipt of the acknowledgment for the previous data segment until the complete
                                                file successfully gets transmitted to the requesting device.

SegmentsFromDisk

This counter represents the number of data segments that the TFTP server reads from the files on disk, while serving files.

SegmentSent

This counter represents the total number of data segments that the TFTP server sent. Files get sent to the requesting device
                                                in data segments of 512 bytes.

SEPFoundCount

This counter represents the number of SEP files that were successfully found in the cache. This counter gets updated each
                                                time that a SEP file is found in the cache.

SEPNotFoundCount

This counter represents the number of SEP files that were not found in the cache. This counter gets updated each time that
                                                a request to get a SEP file produces a not found in cache memory result.

SIPFoundCount

This counter represents the number of SIP files that were successfully found in the cache. This counter gets updated each
                                                time that a SIP file is found in the cache

SIPNotFoundCount

This counter represents the number of SIP files that were not found in the cache. This counter gets updated each time that
                                                a request to get a SIP file produces a not found in cache memory result.

SoftkeyChangeNotifications

This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete configuration files for softkeys.

UnitChangeNotifications

This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete gateway-related configuration files.

#### Cisco Transcode Device

The Cisco Transcode Device object provides information about registered Cisco transcoding devices. The following table contains
                                    information on Cisco transcoder device counters.

Counters

Counter Description

OutOfResources

This counter represents the total number of times that an attempt was made to allocate a transcoder resource from a transcoder
                                                device and failed; for example, because all resources were already in use.

ResourceActive

This counter represents the number of transcoder resources that are currently in use (active) for a transcoder device.

Each transcoder resource uses two streams.

ResourceAvailable

This counter represents the total number of resources that are not active and are still available to be used now for a transcoder
                                                device.

Each transcoder resource uses two streams.

ResourceTotal

This counter represents the total number of transcoder resources that a transcoder device provided. This counter equals the
                                                sum of the ResourceActive and ResourceAvailable counters.

#### Cisco Video Conference Bridge

The Cisco Video Conference Bridge object provides information about registered Cisco video conference bridge devices. The
                                    following table contains information on Cisco video conference bridge device counters.

Counters

Counter Description

ConferencesActive

This counter represents the total number of video conferences that are currently active (in use) on a video conference bridge
                                                device. The system specifies a conference as active when the first call connects to the bridge.

ConferencesAvailable

This counter represents the number of video conferences that are not active and are still available on a video conference
                                                device.

ConferencesCompleted

This counter represents the total number of video conferences that have been allocated and released on a video conference
                                                device. A conference starts when the first call connects to the bridge. The conference completes when the last call disconnects
                                                from the bridge.

ConferencesTotal

This counter represents the total number of video conferences that are configured for a video conference device.

OutOfConferences

This counter represents the total number of times that an attempt was made to initiate a video conference from a video conference
                                                device and failed because the device already had the maximum number of active conferences that is allowed (as specified by
                                                the TotalConferences counter).

OutOfResources

This counter represents the total number of times that an attempt was made to allocate a conference resource from a video
                                                conference device and failed, for example, because all resources were already in use.

ResourceActive

This counter represents the total number of resources that are currently active (in use) on a video conference bridge device.
                                                One resource gets used per participant.

ResourceAvailable

This counter represents the total number of resources that are not active and are still available on a device to handle additional
                                                participants for a video conference bridge device.

ResourceTotal

This counter represents the total number of resources that are configured on a video conference bridge device. One resource
                                                gets used per participant.

#### Cisco Web Dialer

The Cisco Web Dialer object provides information about the Cisco Web Dialer application and the Redirector servlet. The following table contains information on the Cisco Web Dialer counters.

Counters

Counter Description

CallsCompleted

This counter represents the number of Make Call and End Call requests that the Cisco Web Dialer application successfully completed.

CallsFailed

This counter represents the number of Make Call and End Call requests that were unsuccessful.

RedirectorSessionsHandled

This counter represents the total number of HTTP sessions that the Redirector servlet handled since the last service startup.

RedirectorSessionsInProgress

This counter represents the number of HTTP sessions that are currently being serviced by the Redirector servlet.

RequestsCompleted

This counter represents the number of Make Call and End Call requests that the Web Dialer servlet successfully completed.

RequestsFailed

This counter represents the number of Make Call and End Call requests that failed.

SessionsHandled

This counter represents the total number of CTI sessions that the Cisco Web Dialer servlet handled since the last service startup.

SessionsInProgress

This counter represents the number of CTI sessions that the Cisco Web Dialer servlet is currently servicing.

#### Cisco WSM Connector

The WSM object provides information on WSMConnectors that are configured on Unified Communications Manager . Each WSMConnector represents a physical Motorola WSM device. The following table contains information on the Cisco WSM Connector
                                    counters.

Counters

Counter Description

CallsActive

This counter represents the number of calls that are currently active (in use) on the WSMConnector device.

CallsAttempted

This counter represents the number of calls that have been attempted on the WSMConnector device, including both successful
                                                and unsuccessful call attempts.

CallsCompleted

This counter represents the number of calls that are connected (a voice path was established) through the WSMConnector device.
                                                The counter increments when the call terminates.

CallsInProgress

This counter represents the number of calls that are currently in progress on the WSMConnector device. This includes all active
                                                calls. When the number of CallsInProgress equals the number of CallsActive, this indicates that all calls are connected.

DMMSRegistered

This counter represents the number of DMMS subscribers that are registered to the WSM.

### PerfMon Objects and Counters for System

This section provides information on Unified Communications Manager System PerfMon objects and counters.

#### Cisco Tomcat Connector

The Tomcat Hypertext Transport Protocol (HTTP)/HTTP Secure (HTTPS) Connector object provides information about Tomcat connectors.
                                    A Tomcat HTTP connector represents an endpoint that receives requests and sends responses. The connector handles HTTP/HTTPS
                                    requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related web pages are accessed. The Secure Socket Layer (SSL) status of the URLs for web applications provides the basis
                                    for the instance name for each Tomcat HTTP Connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. The following table contains information on the Tomcat HTTP connector counters.

Counters

Counter Description

Errors

This counter represents the total number of HTTP errors (for example, 401 Unauthorized) that the connector encountered. A
                                                Tomcat HTTP connector represents an endpoint that receives requests and sends responses. The connector handles HTTP/HTTPS
                                                requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL.

MBytesReceived

This counter represents the amount of data that the connector received. A Tomcat HTTP connector represents an endpoint that
                                                receives requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS responses that occur
                                                when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL.

MBytesSent

This counter represents the amount of data that the connector sent. A Tomcat HTTP connector represents an endpoint that receives
                                                requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL.

Requests

This counter represents the total number of request that the connector handled. A Tomcat HTTP connector represents an endpoint
                                                that receives requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS responses that
                                                occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL.

ThreadsTotal

This counter represents the current total number of request processing threads, including available and in-use threads, for
                                                the connector. A Tomcat HTTP connector represents an endpoint that receives requests and sends responses. The connector handles
                                                HTTP/HTTPS requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL.

ThreadsMax

This counter represents the maximum number of request processing threads for the connector. Each incoming request on a Unified Communications Manager related window requires a thread for the duration of that request. If more simultaneous requests are received than the currently
                                                available request processing threads can handle, additional threads will get created up to the configured maximum shown in
                                                this counter. If still more simultaneous requests are received, they accumulate within the server socket that the connector
                                                created, up to an internally specified maximum number. Any further simultaneous requests will receive connection refused messages
                                                until resources are available to process them.

A Tomcat HTTP connector represents an endpoint that receives requests and sends responses. The connector handles HTTP/HTTPS
                                                requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL.

ThreadsBusy

This counter represents the current number of busy/in-use request processing threads for the connector. A Tomcat Connector
                                                represents an endpoint that receives requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS
                                                responses that occur when web pages that are related to Unified Communications Manager are accessed. The Secure Sockets Layer (SSL) status of the URLs for the web application provides the basis for the instance
                                                name for each Tomcat connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL.

#### Cisco Tomcat JVM

The Cisco Tomcat Java Virtual Machine (JVM) object provides information about the Tomcat JVM, which represents, among other
                                    things, a pool of common resource memory that Unified Communications Manager related web applications such as Cisco Unified Communications Manager Administration , Cisco Unified Serviceability , Cisco Unity Connection Administration , and more use. The following table contains information on the Tomcat JVM counters.

Counters

Counter Description

KBytesMemoryFree

This counter represents the amount of free dynamic memory block (heap memory) in the Tomcat Java Virtual Machine. The dynamic
                                                memory block stores all objects that Tomcat and its web applications, such as Cisco Unified Communications Manager Administration , Cisco Unified Serviceability , and Cisco Unity Connection create. When the amount of free dynamic memory is low, more memory gets automatically allocated,
                                                and total memory size (represented by the KbytesMemoryTotal counter) increases but only up to the maximum (represented by
                                                the KbytesMemoryMax counter). You can determine the amount of memory in use by subtracting KBytesMemoryFree from KbytesMemoryTotal.

KBytesMemoryMax

This counter represents the amount of free dynamic memory block (heap memory) in the Tomcat Java Virtual Machine. The dynamic
                                                memory block stores all objects that Tomcat and its web applications, such as Cisco Unified Communications Manager Administration , Cisco Unified Serviceability , and Cisco Unity Connection Administration , create.

KBytesMemoryTotal

This counter represents the current total dynamic memory block size, including free and in-use memory, of Tomcat Java Virtual
                                                Machine. The dynamic memory block stores all objects that Tomcat and its web applications, such as Cisco Unified Communications Manager Administration , Cisco Unified Serviceability , and Cisco Unity Connection Administration , create.

#### Cisco Tomcat Web Application

The Cisco Tomcat Web Application object provides information about how to run Unified Communications Manager web applications. The URLs for the web application provide basis for the instance name for each Tomcat Web Application. For
                                    example, Cisco Unified Communications Manager Administration ( https://<IP Address>:8443/ccmadmin ) gets identified by ccmadmin, Cisco Unified Serviceability gets identified by ccmservice, Unified Communications Manager User Options gets identified by ccmuser, Cisco Unity Connection Administration ( https://<IP Address>:8443/cuadmin ) gets identified by cuadmin, and URLs that do not have an extension, such as https://<IP Address>:8443 or http://<IP Address>:8080 ), get identified by _root. The following table contains information on the Tomcat Web Application counters.

Counters

Counter Description

Errors

This counter represents the total number of HTTP errors (for example, 401 Unauthorized) that a Unified Communications Manager related web application encountered. The URLs for the web application provide the basis instance name for each Tomcat Web
                                                Application. For example, Cisco Unified Communications Manager Administration ( https://<IP Address>:8443/ccmadmin ) gets identified by ccmadmin, Cisco Unified Serviceability gets identified by ccmservice, Unified Communications Manager User Options gets identified by ccmuser, Cisco Unity Connection Administration ( https://<IP Address>:8443/cuadmin ) gets identified by cuadmin, and URLs that do not have an extension, such as https://<IP Address>:8443 or http://<IP Address>:8080 ), get identified by _root.

Requests

This counter represents the total number of requests that the web application handles. Each time that a web application is
                                                accessed, its Requests counter increments accordingly. The URLs for the web application provide the basis instance name for
                                                each Tomcat Web Application. For example, Cisco Unified Communications Manager Administration ( https://<IP Address>:8443/ccmadmin ) gets identified by ccmadmin, Cisco Unified Serviceability gets identified by ccmservice, Unified Communications Manager User Options gets identified by ccmuser, Cisco Unity Connection Administration ( https://<IP Address>:8443/cuadmin ) gets identified by cuadmin, and URLs that do not have an extension, such as https://<IP Address>:8443 or http://<IP Address>:8080 ), get identified by _root.

SessionsActive

This counter represents the number of sessions that the web application currently has active (in use). The URLs for the web
                                                application provide the basis instance name for each Tomcat Web Application. For example, Cisco Unified Communications Manager Administration ( https://<IP Address>:8443/ccmadmin ) gets identified by ccmadmin, Cisco Unified Serviceability gets identified by ccmservice, Unified Communications Manager User Options gets identified by ccmuser, Cisco Unity Connection Administration ( https://<IP Address>:8443/cuadmin ) gets identified by cuadmin, and URLs that do not have an extension, such as https://<IP Address>:8443 or http://<IP Address>:8080 ), get identified by _root.

#### Database Change Notification Client

The Database Change Notification Client object provides information on change notification clients. The following table contains
                                    information on the Database Change Notification Client counters.

Counters

Counter Descriptions

MessagesProcessed

This counter represents the number of database change notifications that have been processed. This counter refreshes every
                                                15 seconds.

MessagesProcessing

This counter represents the number of change notification messages that are currently being processed or are waiting to be
                                                processed in the change notification queue for this client. This counter refreshes every 15 seconds.

QueueHeadPointer

This counter represents the head pointer to the change notification queue. The head pointer acts as the starting point in
                                                the change notification queue. To determine the number of notifications in the queue, subtract the head pointer value from
                                                the tail pointer value. By default, this counter refreshes every 15 seconds.

QueueMax

This counter represents the largest number of change notification messages that will be processed for this client. This counter
                                                remains cumulative since the last restart of the Cisco Database Layer Monitor service.

QueueTailPointer

This counter represents the tail pointer to the change notification queue. The tail pointer represents the ending point in
                                                the change notification queue. To determine the number of notifications in the queue, subtract the head pointer value from
                                                the tail pointer value. By default, this counter refreshes every 15 seconds

TablesSubscribed

This counter represents the number of tables in which this client has subscribed.

#### Database Change Notification Server

The Database Change Notification Server object provides information on different change-notification-related statistics. The
                                    following table contains information on the Database Change Notification Server counters.

Counter

Counter Descriptions

Clients

This counter represents the number of change notification clients (services/servlets) that have subscribed for change notification.

Queue Delay

This counter provides the number of seconds that the change notification process has messages to process but is not processing
                                                them. This condition is true if:

- Either Change Notification Requests Queued in Database (QueuedRequestsInDB) and Change Notification Requests Queued in Memory
                                                   (QueuedRequestsInMemory) are non-zero, or

- The Latest Change Notification Messages Processed count is not changing.

This condition gets checked every 15 seconds.

QueuedRequestsInDB

This counter represents the number of change notification records that are in the DBCNQueue (Database Change Notification
                                                Queue) table via direct TCP/IP connection (not queued in shared memory). This counter refreshes every 15 seconds.

QueuedRequestsInMemory

This counter represents the number of change notification requests that are queued in shared memory.

#### Database Change Notification Subscription

The Database Change Notification Subscription object displays the names of tables where the client will receive Change Notifications.

The SubscribedTable object displays the table with the service or servlet that will receive change notifications. Because
                                    the counter does not increment, this display occurs for informational purposes only.

#### Database Local DSN

The Database Local Data Source Name (DSN) object and LocalDSN counter provide the DSN information for the local machine. The
                                    following table contains information on the Database local DSN.

Counters

Counter Descriptions

CcmDbSpace_Used

This counter represents the amount of Ccm DbSpace that is being consumed

CcmtempDbSpace_Used

This counter represents the amount of Ccmtemp DbSpace that is being consumed.

CNDbSpace_Used

This counter represents the percentage of CN dbspace consumed.

LocalDSN

This counter represents the data source name (DSN) that is being referenced from the local machine.

SharedMemory_Free

This counter represents total shared memory that is free.

SharedMemory_Used

This counter total shared memory that is used.

RootDbSpace_Used

This counter represents the amount of RootDbSpace that is being consumed.

#### DB User Host Information Counters

The DB User Host Information object provides information on DB User Host. The DB:User:Host Instance object displays the number
                                    of connections that are present for each instance of DB:User:Host.

#### Enterprise Replication DBSpace Monitors

The enterprise replication DBSpace monitors object displays the usage of various ER DbSpaces. The following table contains
                                    information on the enterprise replication DB monitors.

Counters

Counter Descriptions

ERDbSpace_Used

This counter represents the amount of enterprise replication DbSpace that was consumed.

ERSBDbSpace_Used

This counter represents the amount of ERDbSpace that was consumed.

#### Enterprise Replication Perfmon Counters

The Enterprise Replication Perfmon Counter object provides information on the various replication counters. The ServerName:ReplicationQueueDepth
                                    counter displays the server name followed by the replication queue depth.

#### IP

The IP object provides information on the IP statistics on your system. The following table contains information on the IP
                                    counters.

Counters

Counter Descriptions

Frag Creates

This counter represents the number of IP datagrams fragments that have been generated at this entity.

Frag Fails

This counter represents the number of IP datagrams that were discarded at this entity because the datagrams could not be fragmented,
                                                such as datagrams where the Do not Fragment flag was set.

Frag OKs

This counter represents the number of IP datagrams that were successfully fragmented at this entity.

In Delivers

This counter represents the number of input datagrams that were delivered to IP user protocols. This includes Internet Control
                                                Message Protocol (ICMP).

In Discards

This counter represents the number of discarded input IP datagrams when no problems were encountered. Lack of buffer space
                                                provides one possible reason. This counter does not include any datagrams that were discarded while they were awaiting reassembly.

In HdrErrors

This counter represents the number of discarded input datagrams that had header errors. This includes bad checksums, version
                                                number mismatch, other format errors, time-to-live exceeded, and other errors that were discovered in processing IP options.

In Receives

This counter represents the number of input datagrams that were received from all network interfaces. This counter includes
                                                datagrams that were received with errors

In UnknownProtos

This counter represents the number of locally addressed datagrams that were received successfully but discarded because of
                                                an unknown or unsupported protocol.

InOut Requests

This counter represents the number of incoming IP datagrams that were received and the number of outgoing IP datagrams that
                                                were sent.

Out Discards

This counter represents the number of output IP datagrams that were not transmitted and were discarded. Lack of buffer space
                                                provides one possible reason.

Out Requests

This counter represents the total number of IP datagrams that local IP protocols, including ICMP, supply to IP in requests
                                                transmission. This counter does not include any datagrams that were counted in ForwDatagrams.

Reasm Fails

This counter represents the number of IP reassembly failures that the IP reassembly algorithm detected, including time outs,
                                                errors, and so on. This counter does not represent the discarded IP fragments because some algorithms, such as the algorithm
                                                in RFC 815, can lose track of the number of fragments because it combines them as they are received.

Reasm OKs

This counter represents the number of IP datagrams that were successfully reassembled.

Reasm Reqds

This counter represents the number of IP fragments that were received that required reassembly at this entity.

#### Memory

The memory object provides information about the usage of physical memory and swap memory on the server. The following table
                                    contains information on memory counters.

Counters

Counter Descriptions

% Mem Used

This counter displays the system physical memory utilization as a percentage. The value of this counter equals (Total KBytes
                                                - Free KBytes - Buffers KBytes - Cached KBytes + Shared KBytes) / Total KBytes, which also corresponds to the Used KBytes/Total
                                                KBytes.

% Page Usage

This counter represents the percentage of active pages.

% VM Used

This counter displays the system virtual memory utilization as a percentage. The value of this counter equals (Total KBytes
                                                - Free KBytes - Buffers KBytes - Cached KBytes + Shared KBytes + Used Swap KBytes) / (Total KBytes + Total Swap KBytes), which
                                                also corresponds to Used VM KBytes/Total VM KBytes.

Buffers KBytes

This counter represents the capacity of buffers in your system in kilobytes.

Cached KBytes

This counter represents the amount of cached memory in kilobytes.

Free KBytes

This counter represents the total amount of memory that is available in your system in kilobytes.

Free Swap KBytes

This counter represents the amount of free swap space that is available in your system in kilobytes.

Faults Per Sec

This counter represents the number of page faults (both major and minor) that the system made per second (post 2.5 kernels
                                                only). This does not necessarily represent a count of page faults that generate I/O because some page faults can get resolved
                                                without I/O.

Low Total

This counter represents the total low (non-paged) memory for kernel.

Low Free

This counter represents the total free low (non-paged) memory for kernel.

Major Faults Per Sec

This counter represents the number of major faults that the system has made per second that have required loading a memory
                                                page from disk (post 2.5 kernels only).

Pages

This counter represents the number of pages that the system paged in from the disk plus the number of pages that the system
                                                paged out to the disk.

Pages Input

This counter represents the number of pages that the system paged in from the disk.

Pages Input Per Sec

This counter represents the total number of kilobytes that the system paged in from the disk per second.

Pages Output

This counter represents the number of pages that the system paged out to the disk.

Pages Output Per Sec

This counter represents the total number of kilobytes that the system paged out to the disk per second.

Shared KBytes

This counter represents the amount of shared memory in your system in kilobytes.

Total KBytes

This counter represents the total amount of memory in your system in kilobytes.

Total Swap KBytes

This counter represents the total amount of swap space in your system in kilobytes.

Total VM KBytes

This counter represents the total amount of system physical and memory and swap space (Total Kbytes + Total Swap Kbytes) that
                                                is in use in your system in kilobytes.

Used KBytes

This counter represents the amount of system physical memory that is in use in kilobytes. The value of the Used KBytes counter
                                                equals Total KBytes minus Free KBytes minus Buffers KBytes minus Cached KBytes plus Shared KBytes. In a Linux environment,
                                                the Used KBytes value that displays in the top or free command output equals the difference of Total KBytes and Free KBytes
                                                and also includes the sum of Buffers KBytes and Cached KBytes.

Used Swap KBytes

This counter represents the amount of swap space that is in use on your system in kilobytes.

Used VM KBytes

This counter represents the system physical memory and the amount of swap space that is in use on your system in kilobytes.
                                                The value equals Total KBytes - Free KBytes - Buffers KBytes - Cached KBytes + Shared KBytes + Used Swap KBytes. This corresponds
                                                to Used Mem KBytes + Used Swap KBytes.

#### Network Interface

The network interface object provides information about the network interfaces on the system. The following table contains
                                    information on network interface counters.

Counters

Counter Descriptions

Rx Bytes

This counter represents the number of bytes, including framing characters, that were received on the interface.

Rx Dropped

This counter represents the number of inbound packets that were chosen to be discarded even though no errors had been detected.
                                                This prevents the packet from being delivered to a higher layer protocol. Discarding packets to free up buffer space provides
                                                one reason.

Rx Errors

This counter represents the number of inbound packets (packet-oriented interfaces) and the number of inbound transmission
                                                units (character-oriented or fixed-length interfaces) that contained errors that prevented them from being deliverable to
                                                a higher layer protocol.

Rx Multicast

This counter represents the number of multicast packets that were received on this interface.

Rx Packets

This counter represents the number of packets that this sublayer delivered to a higher sublayer. This does not include the
                                                packets that were addressed to a multicast or broadcast address at this sublayer.

Total Bytes

This counter represents the total number of received (Rx) bytes and transmitted (Tx) bytes.

Total Packets

This counter represents the total number of Rx packets and Tx packets.

Tx Bytes

This counter represents the total number of octets, including framing characters, that were transmitted out from the interface.

Tx Dropped

This counter represents the number of outbound packets that were chosen to be discarded even though no errors were detected.
                                                This action prevents the packet from being delivered to a higher layer protocol. Discarding a packet to free up buffer space
                                                represents one reason.

Tx Errors

This counter represents the number of outbound packets (packet-oriented interfaces) and the number of outbound transmission
                                                units (character-oriented or fixed-length interfaces) that could not be transmitted because of errors.

Tx Packets

This counter represents the total number of packets that the higher level protocols requested for transmission, including
                                                those that were discarded or not sent. This does not include packets that were addressed to a multicast or broadcast address
                                                at this sublayer.

Tx QueueLen

This counter represents the length of the output packet queue (in packets).

#### Number of Replicates Created and State of Replication

The Number of Replicates Created and State of Replication object provides real-time replication information for the system.
                                    The following table contains information on replication counters.

Counters

Counter Descriptions

Number of Replicates Created

This counter displays the number of replicates that were created by Informix for the DB tables. This counter displays information
                                                during Replication Setup.

Replicate_State

This counter represents the state of replication. The following list provides possible values:

- 0—Initializing. The counter equals 0 when the server is not defined or when the server is defined but the template has not
                                                   completed.

- 1—Replication setup script fired from this node. Cisco recommends that you run utils dbreplication status on the CLI to determine
                                                   the location and cause of the failure.

- 2—Good Replication.

- 3—Bad Replication. A counter value of 3 indicates replication in the cluster is bad. It does not mean that replication failed
                                                   on a particular server in the cluster. Cisco recommends that you run utils dbreplication status on the CLI to determine the
                                                   location and cause of the failure.

- 4—Replication setup did not succeed.

#### Partition

The partition object provides information about the file system and its usage in the system. The following table contains
                                    information on partition counters. Be aware that these counters are available for the spare partition, if present.

Counters

Counter Descriptions

% CPU Time

This counter represents the percentage of CPU time that is dedicated to handling I/O requests that were issued to the disk.
                                                This counter is no longer valid when the counter value equals -1.

% Used

This counter represents the percentage of disk space that is in use on this file system.

% Wait in Read

Not Used. The Await Read Time counter replaces this counter. This counter is no longer valid when the counter value equals
                                                -1.

% Wait in Write

Not Used. The Await Write Time counter replaces this counter.This counter is no longer valid when the counter value equals
                                                -1.

Await Read Time

This counter represents the average time, measured in milliseconds, for Read requests that are issued to the device to be
                                                served. This counter is no longer valid when the counter value equals -1.

Await Time

This counter represents the average time, measured in milliseconds, for I/O requests that were issued to the device to be
                                                served. This includes the time that the requests spent in queue and the time that was spent servicing them.This counter is
                                                no longer valid when the counter value equals -1.

Await Write Time

This counter represents the average time, measured in milliseconds, for write requests that are issued to the device to be
                                                served. This counter is no longer valid when the counter value equals -1.

Queue Length

This counter represents the average queue length for the requests that were issued to the disk.This counter is no longer valid
                                                when the counter value equals -1.

Read Bytes Per Sec

This counter represents the amount of data in bytes per second that was read from the disk.

Total Mbytes

This counter represents the amount of total disk space in megabytes that is on this file system.

Used Mbytes

This counter represents the amount of disk space in megabytes that is in use on this file system.

Write Bytes Per Sec

This counter represents the amount of data that was written to the disk in bytes per second.

#### Process

The process object provides information about the processes that are running on the system. The following table contains information
                                    on process counters.

Counters

Counter Descriptions

% CPU Time

This counter, which is expressed as a percentage of total CPU time, represents the tasks share of the elapsed CPU time since
                                                the last update.

% MemoryUsage

This counter represents the percentage of physical memory that a task is currently using.

Data Stack Size

This counter represents the stack size for task memory status.

Nice

This counter represents the nice value of the task. A negative nice value indicates that the process has a higher priority
                                                while a positive nice value indicates that the process has a lower priority. If the nice value equals zero, do not adjust
                                                the priority when you are determining the dispatchability of a task.

Page Fault Count

This counter represents the number of major page faults that a task encountered that required the data to be loaded into memory.

PID

This counter displays the task-unique process ID. The ID periodically wraps, but the value will never equal zero.

Process Status

This counter displays the process status:

- 0—Running

- 1—Sleeping

- 2—Uninterruptible disk sleep

- 3—Zombie

- 4—Stopped

- 5— Paging

- 6—Unknown

Shared Memory Size

This counter displays the amount of shared memory (KB) that a task is using. Other processes could potentially share the same
                                                memory.

STime

This counter displays the system time (STime), measured in jiffies, that this process has scheduled in kernel mode. A jiffy
                                                corresponds to a unit of CPU time and gets used as a base of measurement. One second comprises 100 jiffies.

Thread Count

This counter displays the number of threads that are currently grouped with a task. A negative value (-1) indicates that this
                                                counter is currently not available. This happens when thread statistics (which includes all performance counters in the Thread
                                                object as well as the Thread Count counter in the Process object) are turned off because the system total processes and threads
                                                exceeded the default threshold value.

Total CPU Time Used

This counter displays the total CPU time in jiffies that the task used in user mode and kernel mode since the start of the
                                                task. A jiffy corresponds to a unit of CPU time and gets used as a base of measurement. One second comprises 100 jiffies.

UTime

This counter displays the time, measured in jiffies, that a task has scheduled in user mode.

VmData

This counter displays the virtual memory usage of the heap for the task in kilobytes (KB).

VmRSS

This counter displays the virtual memory (Vm) resident set size (RSS) that is currently in physical memory in kilobytes (KB).
                                                This includes the code, data, and stack.

VmSize

This counter displays the total virtual memory usage for a task in kilobytes (KB). It includes all code, data, shared libraries,
                                                and pages that have been swapped out: Virtual Image = swapped size + resident size.

Wchan

This counter displays the channel (system call) in which the process is waiting.

#### Processor

The processor object provides information on different processor time usage in percentages. The following table contains information
                                    on processor counters.

Counters

Counter Descriptions

% CPU Time

This counter displays the processors share of the elapsed CPU time, excluding idle time, since the last update. This share
                                                gets expressed as a percentage of total CPU time.

Idle Percentage

This counter displays the percentage of time that the processor is in the idle state and did not have an outstanding disk
                                                I/O request.

IOwait Percentage

This counter represents the percentage of time that the processor is in the idle state while the system had an outstanding
                                                disk I/O request.

Irq Percentage

This counter represents the percentage of time that the processor spends executing the interrupt request that is assigned
                                                to devices, including the time that the processor spends sending a signal to the computer.

Nice Percentage

This counter displays the percentage of time that the processor spends executing at the user level with nice priority.

Softirq Percentage

This counter represents the percentage of time that the processor spends executing the soft IRQ and deferring task switching
                                                to get better CPU performance.

System Percentage

This counter displays the percentage of time that the processor is executing processes in system (kernel) level.

User Percentage

This counter displays the percentage of time that the processor is executing normal processes in user (application) level.

#### System

The System object provides information on file descriptors on your system. The following table contains information on system
                                    counters.

Counters

Counter Descriptions

Allocated FDs

This counter represents the total number of allocated file descriptors.

Being Used FDs

This counter represents the number of file descriptors that are currently in use in the system.

Freed FDs

This counter represents the total number of allocated file descriptors on the system that are freed.

Max FDs

This counter represents the maximum number of file descriptors that are allowed on the system.

Total CPU Time

This counter represents the total time in jiffies that the system has been up and running.

Total Processes

This counter represents the total number of processes on the system.

Total Threads

This counter represents the total number of threads on the system.

#### TCP

The TCP object provides information on the TCP statistics on your system. The following table contains information on the
                                    TCP counters.

Counters

Counter Description

Active Opens

This counter displays the number of times that the TCP connections made a direct transition to the SYN-SENT state from the
                                                CLOSED state.

Attempt Fails

This counter displays the number of times that the TCP connections have made a direct transition to the CLOSED state from
                                                either the SYN-RCVD state or the SYN-RCVD state, plus the number of times TCP connections have made a direct transition to
                                                the LISTEN state from the SYS-RCVD state.

Curr Estab

This counter displays the number of TCP connections where the current state is either ESTABLISHED or CLOSE- WAIT.

Estab Resets

This counter displays the number of times that the TCP connections have made a direct transition to the CLOSED state from
                                                either the ESTABLISHED state or the CLOSE-WAIT state.

In Segs

This counter displays the total number of segments that were received, including those received in error. This count only
                                                includes segments that are received on currently established connections.

InOut Segs

This counter displays the total number of segments that were sent and the total number of segments that were received.

Out Segs

This counter displays the total number of segments that were sent. This count only includes segments that are sent on currently
                                                established connections, but excludes retransmitted octets.

Passive Opens

This counter displays the number of times that TCP connections have made a direct transition to the SYN-RCVD state from the
                                                LISTEN state.

RetransSegs

This counter displays the total number of segments that were retransmitted because the segment contains one or more previously
                                                transmitted octets.

#### Thread

The Thread object provides a list of running threads on your system. The following table contains information on the Thread
                                    counters.

Counters

Counter Description

% CPU Time

This counter displays the thread share of the elapsed CPU time since the last update. This counter expresses the share as
                                                a percentage of the total CPU time.

PID

This counter displays the threads leader process ID.

## Cisco Intercompany Media Engine Performance Objects and Alerts

This section provides information on new performance objects, and alerts for both the Unified Communications Manager server and the Cisco Intercompany Media Engine server.

### Cisco Intercompany Media Engine Server Objects

#### Performance Objects

The following performance objects are available on the Cisco Intercompany Media Engine server to support the Cisco Intercompany Media Engine feature.

#### IME Configuration Manager

The IME Configuration Manager object provides information about the IME distributed cache certificate. The following table
                                    contains information on the Cisco IME configuration counters.

Counters

Counter Description

DaysUntilCertExpiry

This counter indicates the number of days that remain until the IME distributed cache certificate expires. You must replace
                                                the certificate before it expires.

When the value of this counter falls below 14, an alert gets generated once every day until the value exceeds 14.

#### IME Server

The IME Server object provides information about the Cisco IME server. The following table contains information on the Cisco
                                    IME Server counters.

Counters

Counter Description

BlockedValidationOrigTLSLimit

This counter indicates the total number of blocked validations that occurred because the TLSValidationThreshold was reached.

BlockedValidationTermTLSLimit

This counter indicates the total number of blocked validations that occurred because the TLSValidationThreshold was reached.

ClientsRegistered

This counter indicates the number of Cisco IME clients that are currently connected to the Cisco IME server.

IMEDistributedCacheHealth

The counter indicates the health of the IME distributed cache. The following values may display:

An alert gets generated once every hour until the value changes from red status.

- 1 (yellow)—Indicates that the Cisco IME network is experiencing minor issues, such as connectivity between bootstrap servers
                                                   or other Cisco IME network issues. (Check the Cisco IME alarms to determine network issues.)

- 2 (green)—Indicates that the Cisco IME is functioning normally and is considered healthy.

IMEDistributedCacheNodeCount

The counter is an integer that indicates an approximation of the total number of nodes in the IME distributed cache. Since
                                                each physical Cisco IME server hosts multiple nodes, this counter does not directly indicate the number of physical Cisco
                                                IME servers that participate in the IME distributed cache. This counter can provide an indication of the health of the IME
                                                distributed cache; for example, a problem may exist with the IME distributed cache if an expected value displays on one day
                                                (for example, 300), but then on the next day, the value drops dramatically (for example, to 10 or 2).

IMEDistributedCacheQuota

Indicates the number of individual DIDs that can be written into the IME Distributed Cache, by Cisco Unified CMs attached
                                                to this IME server. This number is determined by the overall configuration of the IME Distributed Cache, and the IME license
                                                installed on the IME server.

IMEDistributedCacheQuotaUsed

Indicates the total number of unique DID numbers that have been configured, to be published via enrolled patterns for Intercompany
                                                Media Services, by Cisco Unified CMs currently attached to this IME server.

IMEDistributedCacheReads

This counter indicates the total number of reads that the Cisco IME server has attempted into the IME distributed cache. This
                                                number serves as an indicator of whether the Cisco IME server is functional; that is, whether the server is interacting with
                                                other nodes.

IMEDistributedCacheStoredData

This counter indicates the amount of IME distributed cache storage, measured in bytes, that this Cisco IME server provides.

IMEDistributedCacheStores

This counter indicates the total number of stores (published numbers) that the Cisco IME server has attempted into the IME
                                                distributed cache. This number serves as an indicator of whether the Cisco IME server is functional.

InternetBandwidthRecv

This counter measures the amount of downlink Internet bandwidth, in Kbits/s, that the Cisco IME server is consuming.

InternetBandwidthSend

This counter measures the amount of uplink Internet bandwidth that the Cisco IME server in Kbits/s is consuming.

TerminatingVCRs

This counter indicates the total Cisco IME voice call records (VCRs) that are stored on the Cisco IME server after receiving
                                                calls. You can use these records for validating learned routes.

ValidationAttempts

This counter indicates the total number of attempts that the Cisco IME server has made at performing a validation because
                                                the dialed number was found in the Cisco IME network. This counter provides an overall indication of system usage.

ValidationsAwaitingConfirmation

This counter indicates the total number of destination phone numbers that have been validated, but that are awaiting further
                                                calls to improve the security of the system. If you use a higher level of security for learning new routes, the Cisco IME
                                                server requires multiple successful validations for a route before that route is available for calls over IP. This counter
                                                tracks the number of successful validations that have not resulted in available IP routes.

ValidationsPending

This counter, which is an integer, indicates the number of scheduled validation attempts to retrieve a learned route. This
                                                value indicates the backlog of work for the Cisco IME service on the Cisco IME server.

An alert gets generated when the value rises either above the high watermark or falls below the low watermark. After the high
                                                watermark is reached, an alert gets sent immediately and then once an hour until the value falls below the high watermark.
                                                When the high watermark is reached, the Cisco IME service cannot clear the backlog of work prior to the expiration of data;
                                                this situation causes records to drop, and validation may not occur. To reduce the workload, add more Cisco IME servers that
                                                can share the workload.

ValidationsBlocked

This counter indicates the number of times that the Cisco IME service rejected a validation attempt because the calling party
                                                was not trusted; that is, the party was on a blacklist or not on a whitelist. This value provides an indication of the number
                                                of cases where a VoIP calls cannot happen in the future because of the blocked validation.

#### IME Server System Performance

The Cisco IME System Performance object provides information about performance on the Cisco IME server. The following table
                                    contains information on the Cisco IME server system performance counters.

Counters

Counter Description

QueueSignalsPresent 1-High

This counter indicates the number of high-priority signals in the queue on the Cisco IME server. High-priority signals include
                                                timeout events, internal KeepAlive messages, internal process creation, and so on. A large number of high-priority events
                                                causes degraded performance of the Cisco IME service and results in slower or failed validations. Use this counter in conjunction
                                                with the QueueSignalsProcessed 1-High counter to determine the processing delay on the Cisco IME server.

QueueSignalsPresent 2-Normal

This counter indicates the number of normal-priority signals in the queue on the Cisco IME server. Normal-priority signals
                                                include call validations, IME distributed cache operations such as stores and reads, and so on. A large number of normal-priority
                                                events causes degraded performance of the Cisco IME service and may result in slower or failed validations or disruption to
                                                IME distributed cache connectivity. Use this counter in conjunction with the QueueSignalsProcessed 2-Normal counter to determine
                                                the processing delay on the Cisco IME server.

Since high-priority signal must complete before normal priority signals begin to process, check the high-priority counters
                                                to accurately understand why a delay occurs.

QueueSignalsPresent 3-Low

This counter indicates the number of low-priority signals in the queue on the Cisco IME server. Low-priority signals include
                                                IME distributed cache signaling and other events. A large number of signals in this queue may disrupt IME distributed cache
                                                connectivity or other events.

QueueSignalsPresent 4-Lowest

This counter indicates the number of lowest-priority signals in the queue on the Cisco IME server. A large number of signals
                                                in this queue may disrupt IME distributed cache connectivity and other events.

QueueSignalsProcessed 1-High

This counter indicates the number of high-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 1-High counter to determine the processing delay for this queue.

QueueSignalsProcessed 2-Normal

This counter indicates the number of normal-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 1-High counter to determine the processing delay for this queue.
                                                High-priority signals are processed before normal-priority signals.

QueueSignalsProcessed 3-Low

This counter indicates the number of low-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 3-Low counter to determine the processing delay for this queue.

QueueSignalsProcessed 4-Lowest

This counter indicates the number of lowest-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 4-Lowest counter to determine the processing delay for this queue.

QueueSignalsProcessed Total

This counter provides a total of all queue signals that the Cisco IME service processes for each one-second period for all
                                                queue levels: high, normal, low, and lowest.

### Cisco Intercompany Media Engine Server Alerts

The following alerts are available on the Cisco Intercompany Media Engine server to support the Cisco Intercompany Media Engine feature. For descriptions and default configuration settings, refer to the Cisco Intercompany Media Engine Installation and Configuration Guide .

BannedFromNetwork

IMEDistributedCacheCertificateExpiring

IMEDistributedCacheFailure

IMESdlLinkOutOfService

InvalidCertificate

InvalidCredentials

MessageOfTheDay

SWUpdateRequired

TicketPasswordChanged

ValidationsPendingExceeded

CriticalAuditEventGenerated

### Cisco Unified Communications Manager Server Objects

The following performance objects are available on the Unified Communications Manager server to support Cisco Intercompany Media Engine .

#### IME Client

The IME Client object provides information about the Cisco IME client on the Unified Communications Manager server. contains information on the Cisco IME client counters.

Counters

Counter Description

CallsAccepted

This counter indicates the number of Cisco IME calls that the Unified Communications Manager received successfully and that the called party answered, resulting in an IP call.

CallsAttempted

This counter indicates the number of calls that the Unified Communications Manager received through Cisco IME. This number includes accepted calls, failed calls, and busy, no-answer calls. The counter increments
                                                each time that Unified Communications Manager receives a call through Cisco IME.

CallsReceived

This counter indicates the number of calls that Unified Communications Manager receives through Cisco IME. This number includes accepted calls, failed calls, and busy, no-answer calls. The counter increments
                                                on call initiation.

CallsSetup

This counter indicates the number of Cisco IME calls that Unified Communications Manager placed successfully and that the remote party answered, resulting in an IP call.

DomainsUnique

This counter indicates the number of unique domain names of peer enterprises that the Cisco IME client discovered. The counter
                                                serves as an indicator of overall system usage.

FallbackCallsFailed

This counter indicates the total number of failed fallback attempts.

FallbackCallsSuccessful

This counter indicates the total number of Cisco IME calls that have fallen back to the PSTN mid-call due to a quality problem.
                                                The counter includes calls initiated and calls received by this Unified Communications Manager .

IMESetupsFailed

This counter indicates the total number of call attempts for which a Cisco IME route was available but that were set up through
                                                the PSTN due to a failure to connect to the target over the IP network.

RoutesLearned

This counter indicates the total number of distinct phone numbers that the Cisco IME has learned and that are present as routes
                                                in the Unified Communications Manager routing tables. If this number grows too large, the server may exceed the per-cluster limit, and you may need to add additional
                                                servers to your cluster.

RoutesPublished

This counter indicates the total number of DIDs that were published successfully into the IME distributed cache across all
                                                Cisco IME client instances. The counter provides a dynamic measurement that gives you an indication of your own provisioned
                                                usage and a sense of how successful the system has been in storing the DIDs in the network.

RoutesRejected

This counter indicates the number of learned routes that were rejected because the administrator blacklisted the number or
                                                domain. This counter provides an indication of the number of cases where a VoIP call cannot happen in the future because of
                                                the blocked validation.

VCRUploadRequests

This counter indicates the number of voice call record (VCR) upload requests that the Unified Communications Manager has sent to the Cisco IME server to be stored in the IME distributed cache.

#### IME Client Instance

The IME Client Instance object provides information about the Cisco IME client instance on the Unified Communications Manager server. The following table contains information on the Cisco IME client instance counters.

Counters

Counter Description

IMEServiceStatus

This counter indicates the overall health of the connection to the Cisco IME services for a particular Cisco IME client instance
                                                ( Unified Communications Manager ). The following values may display for the counter:

0—Indicates an unknown state (which may mean that the Cisco IME service is not active).

If the value specifies 0, an alert gets generated once per hour while the connection remains in the unknown state.

1—Indicates a healthy state; that is, the Cisco IME service is active, and the Unified Communications Manager has successfully established a connection to its primary and backup servers for the Cisco IME client instance, if configured.

2—Indicates an unhealthy state; that is, the Cisco IME service is active, but the Unified Communications Manager has not successfully established a connection to its primary and backup servers for the Cisco IME client instance, if configured.

### Cisco Unified Communications Manager Server Alerts

The following alerts are available on the Unified Communications Manager server to support Cisco Intercompany Media Engine . For descriptions and default configuration settings, refer to the Cisco Intercompany Media Engine Installation and Configuration Guide .

IMEDistributedCacheInactive

IMEOverQuota

IMEQualityAlert

InsufficientFallbackIdentifiers

IMEServiceStatus

InvalidCredentials

TCPSetupToIMEFailed

TLSConnectionToIMEFailed

| Note | Be aware the RTMT is best used for a single cluster. For large and enterprise networks that have multiple clusters deployed,
                                          Cisco recommends using Cisco Unified Operations Manager. For details about Cisco Unified Operations Manager, go to http://www.cisco.com/en/US/products/ps6535/index.htm . |
|---|---|

| Setting | Description |
|---|---|
| Threshold Pane |
| Trigger alert when Over and Under conditions get met | Check the box and enter the value that applies. Over—Check this box to configure a maximum threshold that must be met before an alert notification is activated. In the Over
                                                value field, enter a value. For example, enter a value that equals the number of calls in progress. Under—Check this box to configure a minimum threshold that must be met before an alert notification is activated. In the Under
                                                value field, enter a value. For example, enter a value that equals the number of calls in progress. Tip Use these boxes in conjunction with the Frequency and Schedule configuration parameters. | Tip | Use these boxes in conjunction with the Frequency and Schedule configuration parameters. |
| Tip | Use these boxes in conjunction with the Frequency and Schedule configuration parameters. |
| Value Calculated As Pane |
| Absolute, Delta, Delta Percentage | Click the radio button that applies. Absolute—Choose Absolute to display the data at its current status. These counter values are cumulative. Delta—Choose Delta to display the difference between the current counter value and the previous counter value. Delta Percentage—Choose Delta Percentage to display the counter performance changes in percentage. |
| Duration Pane |
| Trigger alert only when value constantly...; Trigger alert immediately | Trigger alert only when value constantly...—If you want the alert notification only when the value is constantly below or
                                                over threshold for a desired number of seconds, click this radio button and enter seconds after which you want the alert to
                                                be sent. Trigger alert immediately—If you want the alert notification to be sent immediately, click this radio button. |
| Frequency Pane |
| Trigger alert on every poll; trigger up to... | Click the radio button that applies. Trigger alert on every poll—If you want the alert notification to activate on every poll when the threshold is met, click
                                                this radio button. For example, if the calls in progress continue to go over or under the threshold, the system does not send another alert notification.
                                                   When the threshold is normal (between 50 and 100 calls in progress), the system deactivates the alert notification; however,
                                                   if the threshold goes over or under the threshold value again, the system reactivates alert notification. Trigger up to...—If you want the alert notification to activate at certain intervals, click this radio button and enter the
                                                number of alerts that you want sent and the number of minutes within which you want them sent. |
| Schedule Pane |
| 24-hours daily; start/stop | Click the radio button that applies: 24-hours daily—If you want the alert to be triggered 24 hours a day, click this radio button. Start/Stop—If you want the alert notification activated within a specific time frame, click the radio button and enter a start
                                                time and a stop time. If the check box is checked, enter the start and stop times of the daily task. For example, you can
                                                configure the counter to be checked every day from 9:00 am to 5:00 pm or from 9:00 pm to 9:00 am. |

| Tip | Use these boxes in conjunction with the Frequency and Schedule configuration parameters. |
|---|---|

| Note | If you require an e-mail notifications, check the Enable E-mail box. |
|---|---|

| Parameter | Description |
|---|---|
| Absolute | Because some counter values are accumulative, choose Absolute to display the data at its current status. |
| Delta | Choose Delta to display the difference between the current counter value and the previous counter value. |
| Delta Percentage | Choose Delta Percentage to display the counter performance changes in percentage. |

| Counters | Counter Description |
|---|---|
| OutboundBusyAttempts | This counter represents the total number of times that Unified Communications Manager attempts a call through the analog access gateway when all ports were busy. |
| PortsActive | This counter represents the number of ports that are currently in use (active). A port appears active when a call is in progress
                                                on that port. |
| PortsOutOfService | This counter represents the number of ports that are currently out of service. Counter applies only to loop-start and ground-start
                                                trunks. |

| Counters | Counter Description |
|---|---|
| OutOfResources | This counter represents the total number of times that Unified Communications Manager attempted to allocate an annunciator resource from an annunciator device and failed; for example, because all resources were
                                                already in use. |
| ResourceActive | This counter represents the total number of annunciator resources that are currently active (in use) for an annunciator device. |
| ResourceAvailable | This counter represents the total number of resources that are not active and are still available to be used at the current
                                                time for the annunciator device. |
| ResourceTotal | This counter represents the total number of annunciator resources that are configured for an annunciator device. |

| Counters | Counter
                                                					 Description |
|---|---|
| AnnunciatorOutOfResources | This counter represents the total number of times that Unified Communications Manager attempted to allocate an annunciator resource from those that are registered to a Unified Communications Manager when none were available. |
| AnnunciatorResourceActive | This counter represents the total number of annunciator resources that are currently in use on all annunciator devices that
                                                are registered with a Unified Communications Manager . |
| AnnunciatorResourceAvailable | This counter
                                                					 represents the total number of annunciator resources that are not active and
                                                					 are currently available. |
| AnnunciatorResourceTotal | This counter represents the total number of annunciator resources that are provided by all annunciator devices that are currently
                                                registered with Unified Communications Manager . |
| AuthenticatedCallsActive | This counter represents the number of authenticated calls that are currently active (in use) on Unified Communications Manager . An authenticated call designates one in which all the endpoints that are participating in the call are authenticated. An
                                                authenticated phone uses the Transport Layer Security (TLS) authenticated Skinny protocol signaling with Unified Communications Manager . |
| AuthenticatedCallsCompleted | This counter represents the number of authenticated calls that connected and subsequently disconnected through Unified Communications Manager . An authenticated call designates one in which all the endpoints that are participating in the call are authenticated. An
                                                authenticated phone uses the TLS authenticated Skinny protocol signaling with Unified Communications Manager . |
| AuthenticatedPartiallyRegisteredPhone | This counter
                                                					 represents the number of partially registered, authenticated SIP phones. |
| AuthenticatedRegisteredPhones | This counter represents the total number of authenticated phones that are registered to Unified Communications Manager . An authenticated phone uses the TLS authenticated Skinny protocol signaling with Unified Communications Manager . |
| BRIChannelsActive | This counter represents the number of BRI voice channels that are currently in an active call on this Unified Communications Manager . |
| BRISpansInService | This counter
                                                					 represents the number of BRI spans that are currently available for use. |
| CallManagerHeartBeat | This counter represents the heartbeat of Unified Communications Manager . This incremental count indicates that Cisco Unified Communications Manager is up and running. If the count does not increment, that indicates that Unified Communications Manager is down. |
| CallsActive | This counter represents the number of voice or video streaming connections that are currently in use (active); in other words,
                                                the number of calls that actually have a voice path that is connected on Unified Communications Manager . |
| CallsAttempted | This counter
                                                					 represents the total number of attempted calls. An attempted call occurs any
                                                					 time that a phone goes off hook and back on hook, regardless of whether any
                                                					 digits were dialed, or whether it connected to a destination. The system
                                                					 considers some call attempts during feature operations (such as transfer and
                                                					 conference) to be attempted calls. |
| CallsCompleted | This counter represents the number of calls that were actually connected (a voice path or video stream was established) through Unified Communications Manager . This number increases when the call terminates. |
| CallsInProgress | This counter represents the number of voice or video calls that are currently in progress on Unified Communications Manager , including all active calls. When a
                                                					 phone that is registered with Skinny Client Control Protocol (SCCP) goes off
                                                					 hook, the CallsInProgress progress counter increments until it goes back on
                                                					 hook. For Cisco Unified IP
                                                   						Phone s 7940, and 7960 that register with SIP, the CallsInProgress
                                                					 counter increments when the dial softkey is pressed. For all
                                                					 other phones that are running SIP, the CallsInProgress counter increments when
                                                					 the first digit is pressed. When all
                                                					 voice or video calls that are in progress are connected, the number of
                                                					 CallsInProgress represents the number of CallsActive. The counter decreases by
                                                					 one when a phone goes back on hook. |
| CM_MediaTermPointsRequestsThrottled | This counter represents the total number of media termination point (MTP) resource requests that have been denied due to throttling
                                                (a resource from this MTP was not allocated because, as specified by the Cisco CallManager service parameter, MTP and Transcoder
                                                Resource Throttling Percentage, the MTP was being utilized beyond the configured throttle percentage). This counter increments
                                                each time a request for an MTP on this Unified Communications Manager node is requested and denied due to MTP throttling and reflects a running total since the start of the Cisco CallManager
                                                service. |
| CM_TranscoderRequestsThrottled | This counter represents the total number of transcoder resource requests that have been denied due to throttling (a resource
                                                from this transcoder was not allocated because, as specified by the Cisco CallManager service parameter MTP and Transcoder
                                                Resource Throttling Percentage, the transcoder was being utilized beyond the configured throttle percentage). This counter
                                                increments each time a request for a transcoder on this Unified Communications Manager node is requested and denied due to transcoder throttling and reflects a running total since the start of the Cisco CallManager
                                                service |
| EncryptedCallsActive | This counter represents the number of encrypted calls that are currently active (in use) on this Unified Communications Manager . An encrypted call represents one in which all the endpoints that are participating in the call are encrypted. |
| EncryptedCallsCompleted | This counter represents the number of encrypted calls that were connected and subsequently disconnected through this Unified Communications Manager . An encrypted call represents one in which all the endpoints that are participating in the call are encrypted. |
| EncryptedPartiallyRegisteredPhones | This
                                                					 counter represents the number of partially registered, encrypted SIP phones. |
| EncryptedRegisteredPhones | This counter represents the total number of encrypted phones that are registered on this Unified Communications Manager . |
| FXOPortsActive | This counter represents the number of FXO ports that are currently in use (active) on a Unified Communications Manager . |
| FXOPortsInService | This
                                                					 counter represents the number of FXO ports that are currently available for use
                                                					 in the system. |
| FXSPortsActive | This counter represents the number of FXS ports that are currently in use (active) on a Unified Communications Manager . |
| FXSPortsInService | This
                                                					 counter represents the number of FXS ports that are currently available for use
                                                					 in the system. |
| HuntListsInService | This counter represents the number of hunt lists that are currently in service on Unified Communications Manager . |
| HWConferenceActive | This counter represents the total number of hardware conference resources that are provided by all hardware conference bridge
                                                devices that are currently registered with Unified Communications Manager . |
| HWConferenceCompleted | This counter represents the total number of conferences that used a hardware conference bridge (hardware-based conference
                                                devices such as Cisco Catalyst 6000, Cisco Catalyst 4000, Cisco VG200, Cisco series 26xx and 36xx) that is allocated from Unified Communications Manager and that have completed, which means that the conference bridge has been allocated and released. A conference activates when
                                                the first call connects to the bridge. The conference completes when the last call disconnects from the bridge. |
| HWConferenceOutOfResources | This counter represents the total number of times that Unified Communications Manager attempted to allocate a hardware conference resource from those that are registered to a Unified Communications Manager when none was available. |
| HWConferenceResourceActive | This counter represents the total number of conference resources that are in use on all hardware conference devices (such
                                                as Cisco Catalyst 6000, Catalyst 4000, Cisco VG200, Cisco series 26xx and 36xx) that are registered with Unified Communications Manager . System considers conference to be active when one or more calls are connected to a bridge. |
| HWConferenceResourceAvailable | This counter represents the number of hardware conference resources that are not in use and that are available to be allocated
                                                on all hardware conference devices (such as Cisco Catalyst 6000, Cisco Catalyst 4000, Cisco VG200, Cisco series 26xx and 36xx)
                                                that are allocated from Unified Communications Manager and that have been completed, which means that the conference bridge has been allocated and released. A conference activates
                                                when the first call connects to the bridge. The conference completes when the last call disconnects from the bridge. |
| HWConferenceResourceTotal | This counter represents the number of active conferences on all hardware conference devices that are registered with Unified Communications Manager . |
| InitializationState | This counter represents the current initialization state of Unified Communications Manager . Unified Communications Manager includes the following initialization state values: 1-Database; 2-Regions; 3-Locations; 4-QoS Policy; 5-Time Of Day;
                                                					 6-AAR Neighborhoods; 7-Digit Analysis; 8-Route Plan; 9-Call Control; 10-RSVP
                                                					 Session Manager; 11-Supplementary Services; 12-Directory; 13-SDL Link;
                                                					 14-Device; 100-Initialization Complete. Not all
                                                					 states display when this counter is used. This does not indicate that an error
                                                					 occurred; it simply indicates that the state(s) initialized and completed
                                                					 within the refresh period of the performance monitor. |
| LocationOutOfResources | This
                                                					 counter represents the total number of times that a call through Locations
                                                					 failed due to the lack of bandwidth. |
| MOHMulticastResourceActive | This counter represents the total number of multicast MOH resources that are currently in use (active) on all MOH servers
                                                that are registered with a Unified Communications Manager . |
| MOHMulticastResourceAvailable | This counter represents the total number of active multicast MOH connections that are not being used on all MOH servers that
                                                are registered with a Unified Communications Manager . |
| MOHOutOfResources | This counter represents the total number of times that the Media Resource Manager attempted to allocate an MOH resource when
                                                all available resources on all MOH servers that are registered with a Unified Communications Manager were already active. |
| MOHTotalMulticastResources | This counter represents the total number of multicast MOH resources or connections that are provided by all MOH servers that
                                                are currently registered with a Unified Communications Manager . |
| MOHTotalUnicastResources | This counter represents the total number of unicast MOH resources or streams that are provided by all MOH servers that are
                                                currently registered with Unified Communications Manager . Each MOH unicast resource uses one stream. |
| MOHUnicastResourceActive | This counter represents the total number of unicast MOH resources that are currently in use (active) on all MOH servers that
                                                are registered with Unified Communications Manager . Each MOH unicast resource uses one stream. |
| MOHUnicastResourceAvailable | This counter represents the total number of unicast MOH resources that are currently available on all MOH servers that are
                                                registered with Unified Communications Manager . Each MOH unicast resource uses one stream. |
| MTPOutOfResources | This counter represents the total number of times that Unified Communications Manager attempted but failed to allocate an MTP resource from one MTP device that is registered with Unified Communications Manager . This also means that no transcoders were available to act as MTPs. |
| MTPResourceActive | This counter represents the total number of MTP resources that are currently in use (active) on all MTP devices that are registered
                                                with a Unified Communications Manager . Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call. |
| MTPResourceAvailable | This counter represents the total number of MTP resources that are not in use and are available to be allocated on all MTP
                                                devices that are registered with Unified Communications Manager . Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call. |
| MTPResourceTotal | This counter represents the total number of media termination point (MTP) resources that are provided by all MTP devices that
                                                are currently registered with Unified Communications Manager . |
| MTP_RequestsThrottled | This
                                                					 counter represents the total number of media termination point (MTP) resource
                                                					 requests that have been denied due to throttling (a resource from this MTP was
                                                					 not allocated because, as specified by the Cisco CallManager service parameter
                                                					 MTP and Transcoder Resource Throttling Percentage, the MTP was being utilized
                                                					 beyond the configured throttle percentage). This counter increments each time a
                                                					 resource is requested from this MTP and is denied due to throttling. This
                                                					 counter reflects a running total since the MTP device registered with the Cisco
                                                					 CallManager service. |
| PartiallyRegisteredPhone | This
                                                					 counter represents the number of partially registered phones that are running
                                                					 SIP. |
| PRIChannelsActive | This counter represents the number of PRI voice channels that are in an active call on a Unified Communications Manager . |
| PRISpansInService | This
                                                					 counter represents the number of PRI spans that are currently available for
                                                					 use. |
| RegisteredAnalogAccess | This
                                                					 counter represents the number of registered Cisco analog access gateways that
                                                					 are registered with system. The count does not include the number of Cisco
                                                					 analog access ports. |
| RegisteredHardwarePhones | This
                                                					 counter represents the number of Cisco hardware IP phones (for example, Cisco Unified IP
                                                   						Phone s 7960, 7940, and so on) that are currently registered in
                                                					 the system. |
| RegisteredMGCPGateway | This
                                                					 counter represents the number of MGCP gateways that are currently registered in
                                                					 the system. |
| RegisteredOtherStationDevices | This
                                                					 counter represents the number of station devices other than Cisco hardware IP
                                                					 phones that are currently registered in the system (for example,
                                                					 Cisco IP SoftPhone, CTI port, CTI route point, Cisco voice-mail port). |
| SIPLineServerAuthorizationChallenges | This counter represents the number of authentication challenges for incoming SIP requests that the Unified Communications Manager server issued to phones that are running SIP. An authentication challenge occurs when a phone that is running SIP with Digest
                                                Authentication enabled sends a SIP line request to Unified Communications Manager . |
| SIPLineServerAuthorizationFailures | This counter represents the number of authentication challenge failures for incoming SIP requests from SIP phones to the Unified Communications Manager server. An authentication failure occurs when a SIP phone with Digest Authentication enabled sends a SIP line request with
                                                bad credentials to Unified Communications Manager . |
| SIPTrunkAuthorization | This counter represents the number of application-level authorization checks for incoming SIP requests that Unified Communications Manager has issued to SIP trunks. An application-level authorization check occurs when Unified Communications Manager compares an incoming SIP request to the application-level settings on the SIP Trunk Security Profile Configuration window
                                                in Cisco Unified Communications Manager Administration . |
| SIPTrunkAuthorizationFailures | This counter represents the number of application-level authorization failures for incoming SIP requests that have occurred
                                                on Unified Communications Manager SIP trunks. An application-level authorization failure occurs when Unified Communications Manager compares an incoming SIP request to the application-level authorization settings on the SIP Trunk Security Profile Configuration
                                                window in Cisco Unified Communications Manager Administration and finds that authorization for one or more of the SIP features on that window is not allowed. |
| SIPTrunkServerAuthenticationChallenges | This counter represents the number of authentication challenges for incoming SIP requests that Unified Communications Manager issued to SIP trunks. An authentication challenge occurs when a SIP trunk with Digest Authentication enabled sends a SIP
                                                request to Unified Communications Manager . |
| SIPTrunkServerAuthenticationFailures | This counter represents the number of authentication challenge failures that occurred for incoming SIP requests from SIP trunks
                                                to Unified Communications Manager . An authentication failure occurs when a SIP trunk with Digest Authentication enabled sends a SIP request with bad credentials
                                                to Unified Communications Manager . |
| SWConferenceActive | This counter represents the number of active conferences on all software conference devices that are registered with Unified Communications Manager . |
| SWConferenceCompleted | This counter represents the total number of conferences that used a software conference bridge that was allocated from a Unified Communications Manager and that have been completed, which means that the conference bridge has been allocated and released. A conference activates
                                                when the first call connects to the bridge. The conference completes when the last call disconnects from the bridge. |
| SWConferenceOutOfResources | This counter represents the total number of times that Unified Communications Manager attempted to allocate a software conference resource from those that are registered to Unified Communications Manager when none was available. Counter includes failed attempts to add a new participant to an existing conference. |
| SWConferenceResourceActive | This counter represents the total number of conference resources that are in use on all software conference devices that are
                                                registered with Unified Communications Manager . The system considers a conference to be active when one or more calls connect to a bridge. One resource equals one stream. |
| SWConferenceResourceAvailable | This counter represents the number of new software-based conferences that can be started at the same time, for Unified Communications Manager . You must have a minimum of three streams available for each new conference. One resource equals one stream |
| SWConferenceResourceTotal | This counter represents the total number of software conference resources that are provided by all software conference bridge
                                                devices that are currently registered with Unified Communications Manager . |
| SystemCallsAttempted | This
                                                					 counter represents the total number of server-originated calls and attempted
                                                					 calls to the Unity message waiting indicator (MWI). |
| T1ChannelsActive | This counter represents the number of T1 CAS voice channels that are in an active call on a Unified Communications Manager . |
| T1SpansInService | This
                                                					 counter represents the number of T1 CAS spans that are currently available for
                                                					 use. |
| TLSConnectedSIPTrunks | This
                                                					 counter represents the number of SIP trunks that are configured and connected
                                                					 via Transport Layer Security (TLS). |
| TLSConnectedWSM | This
                                                					 counter represents the number of WSM Connectors that are configured and
                                                					 connected to Motorola WSM via Transport Layer Security (TLS). |
| TranscoderOutOfResources | This counter represents the total number of times that Unified Communications Manager attempted to allocate a transcoder resource from a transcoder device that is registered to a Unified Communications Manager when none was available. |
| TranscoderResourceActive | This counter represents the total number of transcoders that are in use on all transcoder devices that are registered with Unified Communications Manager . A transcoder in use represents one transcoder resource that has been allocated for use in a call. Each transcoder resource
                                                uses two streams. |
| TranscoderResourceAvailable | This counter represents the total number of transcoders that are not in use and that are available to be allocated on all
                                                transcoder devices that are registered with Unified Communications Manager . Each transcoder resource uses two streams. |
| TranscoderResourceTotal | This counter represents the total number of transcoder resources that are provided by all transcoder devices that are currently
                                                registered with Unified Communications Manager . |
| VCBConferenceActive | This counter represents the total number of active video conferences on all video conference bridge devices that are registered
                                                with Unified Communications Manager . |
| VCBConferenceAvailable | This counter represents the total number of new video conferences on all video conference bridge devices that are registered
                                                with Unified Communications Manager . |
| VCBConferenceCompleted | This counter represents the total number of video conferences that used a video conference bridge that are allocated from Unified Communications Manager and that have been completed, which means that the conference bridge has been allocated and released. A conference activates
                                                when the first call connects to the bridge. The conference completes when the last call disconnects from the bridge. |
| VCBConferenceTotal | This counter represents the total number of video conferences that are supported on all video conference bridge devices that
                                                are registered with Unified Communications Manager . |
| VCBOutOfConferences | This counter represents the total number of times that Unified Communications Manager attempted to allocate a video conference resource from those that are registered to Unified Communications Manager when none was available. |
| VCBOutOfResources | This
                                                					 counter represents the total number of failed new video conference requests. A
                                                					 conference request can fail because, for example, the configured number of
                                                					 conferences is already in use. |
| VCBResourceActive | This counter represents the total number of video conference resources that are currently in use on all video conference devices
                                                that are registered with Unified Communications Manager . |
| VCBResourceAvailable | This
                                                					 counter represents the total number of video conference resources that are not
                                                					 active and are currently available. |
| VCBResourceTotal | This counter represents the total number of video conference resources that are provided by all video conference bridge devices
                                                that are currently registered with Unified Communications Manager . |
| VideoCallsActive | This counter represents the number of active video calls with active video streaming connections on all video conference bridge
                                                devices that are registered with Unified Communications Manager . |
| VideoCallsCompleted | This
                                                					 counter represents the number of video calls that were actually connected with
                                                					 video streams and then released. |
| VideoOutOfResources | This counter represents the total number of times that Unified Communications Manager attempted to allocate a video-streaming resource from one of the video conference bridge devices that is registered to Unified Communications Manager when none was available. |
| XCODE_RequestsThrottled | This
                                                					 counter represents the total number of transcoder resource requests that have
                                                					 been denied due to throttling (a resource from this transcoder was not
                                                					 allocated because, as specified by the Cisco CallManager service parameter MTP
                                                					 and Transcoder Resource Throttling Percentage, the transcoder was being
                                                					 utilized beyond the configured throttle percentage). This counter increments
                                                					 each time a resource is requested from this transcoder and is denied due to
                                                					 throttling. This counter reflects a running total since the transcoder device
                                                					 registered with the Cisco CallManager service. |

| Counters | Counter Description |
|---|---|
| Unified Communications Manager Object |
| ExternalCallControlEnabledCallsAttempted | This counter specifies the total number of calls to devices that have the External Call Control feature enabled. This is a
                                                cumulative count of all calls to intercept-enabled patterns or DNs since the last restart of the Cisco CallManager service. |
| ExternalCallControlEnabledCallsCompleted | This counter specifies the total number of calls that were connected to a device that had the External Call Control feature
                                                enabled. This is a cumulative count of all calls to intercept-enabled patterns or DNs since the last restart of the Cisco
                                                CallManager service. |
| ExternalCallControlEnabledFailureTreatmentApplied | This counter specifies the total number of calls that were cleared or routed based on failure treatments (such as Allow or
                                                Deny) that are defined in the External Call Control profile. |
| External Call Control Objects |
| PDPServersTotal | This counter defines the total number of PDP servers in all External Call Control Profiles configured in Cisco Unified Communications Manager Administration. This counter increments when a new PDP server is added and decrements when a PDP server is removed. |
| PDPServersInService | This counter defines the total number of in-service (active) PDP servers. |
| PDPServersOutOfService | This counter defines the total number of times that PDP servers have transitioned from in-service to out-of-service. This
                                                is a cumulative count of out-of-service PDP servers since the last restart of the Cisco CallManager service. |
| ConnectionsActiveToPDPServer | This counter specifies the total number of connections that Unified Communications Manager has established (currently active) with PDP servers. |
| ConnectionsLostToPDPServer | This counter specifies the total number of times that active connections between Unified Communications Manager and the PDP servers were disconnected. This is a cumulative count since the last restart of the Cisco CallManager service. |

| Counters | Counter Description |
|---|---|
| SAFConnectionsSucceeded (range from 0 to 2) | Total number of SAF client connections currently active on this Unified Communications Manager node. |
| SAFFConnectionsFailed (range from 0 to 2) | Total number of SAF client connections that failed on the Unified Communications Manager node. A failed connection is a connection that did not register with the SAF Forwarder. |

| Note | A Unified Communications Manager node restart causes a counter reset. |
|---|---|

| Counters | Counter Description |
|---|---|
| AverageExpectedDelay | This counter represents the current average expected delay before any incoming message gets handled. |
| CallsRejectedDueToICTThrottling | This counter represents the total number of calls that were rejected since the start of Cisco CallManager service due to Intercluster
                                                Trunk (ICT) call throttling. When the threshold limit of 140 calls per 5 seconds is met, the ICT will start throttling (rejecting)
                                                new calls. One cause for ICT call throttling occurs when calls across an ICT enter a route loop condition. |
| CallThrottlingGenericCounter3 | This counter represents a generic counter that is used for call-throttling purpose. |
| CodeRedEntryExit | This counter indicates whether Unified Communications Manager has entered or exited a Code state (call-throttling mode). Valid values include 0 (Exit) and 1 (Entry). |
| CodeYellowEntryExit | This counter indicates whether  has entered or exited a Code Unified Communications Manager Yellow state (call-throttling mode). Valid values include 0 (Exit) and 1 (Entry). |
| EngineeringCounter1 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| EngineeringCounter2 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| EngineeringCounter3 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| EngineeringCounter4 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| EngineeringCounter5 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| EngineeringCounter6 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| EngineeringCounter7 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| EngineeringCounter8 | Do not use this counter unless directed by a Cisco Engineering Special build. Cisco uses information in this counter for diagnostic
                                                purposes. |
| QueueSignalsPresent 1-High | This counter indicates the number of high-priority signals in the Unified Communications Manager queue. High-priority signals include timeout events, internal Unified Communications Manager keepalives, certain gatekeeper events, and internal process creation, among other events. A large number of high-priority
                                                events will cause degraded performance on Unified Communications Manager and result in slow call connection or loss of dial tone. Use this counter in conjunction with the QueueSignalsProcessed 1-High
                                                counter to determine the processing delay on Unified Communications Manager . |
| QueueSignalsPresent 2-Normal | This counter indicates the number of normal-priority signals in the Unified Communications Manager queue. Normal-priority signals include call-processing functions, key presses, on-hook and off-hook notifications, among
                                                other events. A large number of normal-priority events will cause degraded performance on Unified Communications Manager , sometimes resulting in delayed dial tone, slow call connection, or loss of dial tone. Use this counter in conjunction with
                                                the QueueSignalsProcessed 2-Normal counter to determine the call-processing delay on Unified Communications Manager . Remember that high-priority signals must complete before normal-priority signals begin to process, so check the high-priority
                                                counters as well to get an accurate picture of the potential delay. |
| QueueSignalsPresent 3-Low | This counter indicates the number of low-priority signals in the Unified Communications Manager queue. Low-priority signals include station device registration (except the initial station registration request message),
                                                among other events. A large number of signals in this queue could result in delayed device registration, among other events. |
| QueueSignalsPresent 4-Lowest | This counter indicates the number of lowest priority signals in the Unified Communications Manager queue. Lowest priority signals include the initial station registration request message during device registration, among
                                                other events. A large number of signals in this queue could result in delayed device registration, among other events. |
| QueueSignalsProcessed 1-High | This counter indicates the number of high-priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 1-High counter to determine
                                                the processing delay on this queue. |
| QueueSignalsProcessed 2-Normal | This counter indicates the number of normal-priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 2-Normal counter to determine
                                                the processing delay on this queue. Remember that high-priority signals get processed before normal-priority signals. |
| QueueSignalsProcessed 3-Low | This counter indicates the number of low-priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 3-Low counter to determine
                                                the processing delay on this queue. The number of signals processed gives an indication of how much device registration activity
                                                is being processed in this time interval. |
| QueueSignalsProcessed 4-Lowest | This counter indicates the number of lowest priority signals that Unified Communications Manager processes for each 1-second interval. Use this counter in conjunction with the QueueSignalsPresent 4-Lowest counter to determine
                                                the processing delay on this queue. The number of signals that are processed gives an indication of how many devices began
                                                the Unified Communications Manager registration process in this time interval. |
| QueueSignalsProcessed Total | This counter provides a sum total of all queue signals that Unified Communications Manager processes for each 1-second interval for all queue levels: high, normal, low, and lowest. |
| SkinnyDevicesThrottled | This counter represents the total number of Skinny devices that are being throttled. A Skinny device gets throttled (asked
                                                to shut down and reregister) when the total number of events that the Skinny device generated exceeds the configured maximum
                                                threshold value (default value specifies 2000 events) within a 5-second interval. |
| ThrottlingSampleActivity | This counter indicates how many samples, out of the configured sample size, have non-zero averageExpectedDelay values. This
                                                counter gets reset when any sample has an averageExpectedDelay value of zero. This process repeats for each batch of samples.
                                                A batch represents the configured sample size. |
| TotalCodeYellowEntry | This counter indicates the number of times that Unified Communications Manager call processing enters the code yellow state. This counter remains cumulative from the start of the Unified Communications Manager process. |

| Counters | Counter Description |
|---|---|
| CcmLinkActive | This counter represents the total number of active Unified Communications Manager links. CTI Manager maintains links to all active servers in a cluster, if applicable. |
| CTIConnectionActive | This counter represents the total number of CTI clients that are currently connected to the CTIManager. This counter increases
                                                by one when a new connection is established and decreases by one when a connection is released. The CTIManager service parameter
                                                MaxCTIConnections determines the maximum number of active connections. |
| DevicesOpen | This counter represents the total number of devices that are configured in Unified Communications Manager that CTI applications control and/or monitor. Devices include hardware IP phones, CTI ports, CTI route points, and so on. |
| LinesOpen | This counter represents the total number of lines that are configured in Unified Communications Manager that control and/or monitor CTI applications. |
| QbeVersion | This counter represents the version number of the Quick Buffer Encoding (QBE) interface that the CTIManager uses. |

| Counters | Counter Description |
|---|---|
| CallsAnchored | This counter represents the number of calls that are placed or received on dual-mode phones that are anchored in Unified Communications Manager . The counter increments when a call is received from or placed to a dual-mode phone. The counter increments twice if a dual-mode
                                                phone calls another dual-mode phone. |
| DMMSRegistered | This counter represents the number of Dual-mode Mobile Station (DMMS) subscribers that are registered in the wireless LAN
                                                (WLAN). |
| FollowMeAborted | This counter represents the number of failed follow-me operations. |
| FollowMeAttempted | This counter represents the number of follow-me operations that Unified Communications Manager attempted. The counter increments when a SIP 302 - Moved Temporarily message is received from the Wireless Service Manager
                                                (WSM) and Unified Communications Manager redirects the call to the DMMS in WLAN. |
| FollowMeCompleted | This counter represents the number of follow-me operations that were successfully completed. The counter increments when the
                                                DMMS in WLAN answers the call and the media (voice path) successfully gets established with the calling device. |
| FollowMeInProgress | This counter represents the number of follow-me operations that are currently in progress. The counter increments when a follow-me
                                                is attempted, and it decrements when the follow-me operation aborts or completes. |
| H1HandOutAttempted | This counter represents the number of H1 hand-out operations that dual-mode phones attempt. The counter increments when Unified Communications Manager processes a call to the H1 number from a DMMS. |
| H1HandOutCompleted | This counter represents the number of successfully completed H1 hand-out operations. The counter increments when the DMMS
                                                in WLAN successfully reestablishes a media (voice path). |
| H2HandOutCompleted | This counter represents the number of successfully completed H2 hand-out operations. The counter increments when the DMMS
                                                in WLAN successfully reestablishes a media (voice path). |
| H2HandOutsAttempted | This counter represents the number of H2 hand-out operations that dual-mode phones attempt. The counter increments when Unified Communications Manager receives a call to the H2 number from a DMMS. |
| HandInAborted | This counter represents the number of hand-in operations that failed. |
| HandInAttempted | This counter represents the number of hand-in operations that dual-mode phones attempt. |
| HandInCompleted | This counter represents the number of successfully completed hand-in operations. The counter increments when the DMMS in WLAN
                                                successfully reestablishes a media (voice path). |
| HandInInProgress | This counter represents the number of hand-in operations that are currently in progress. The counter increments when a hand-in
                                                is attempted, and the counter decrements when the hand-in is aborted or completed. |
| HandOutAborted | This counter represents the number of hand-out operations that failed. |
| HandOutInProgress | This counter represents the number of H1 and H2 hand-out operations that are currently in progress. The counter increments
                                                when a H1 or H2 hand-out is attempted, and it decrements when the hand-out is aborted or completed. |

| Counters | Counter Description |
|---|---|
| RequestsHandled | This counter represents the total number of HTTP requests that the extension mobility application handled since the last restart
                                                of the Cisco CallManager service. A typical login would constitute two HTTP requests: one to query the initial login state
                                                of the device and another to log in the user on a device. Similarly, a typical logout also results in two HTTP requests. |
| RequestsInProgress | This counter represents the number of HTTP requests that the extension mobility application currently is handling. A typical
                                                login would constitute two HTTP requests: one to query the initial login state of the device and another to log in the user
                                                on a device. Similarly, a typical logout also results in two HTTP requests. |
| RequestsThrottled | This counter represents the total number of Login/Logout Requests that failed due to throttling. |
| LoginsSuccessful | This counter represents the total number of successful login requests that were completed through Extension Mobility Service. |
| LogoutsSuccessful | This counter represents the total number of successful logout requests that were completed through Extension Mobility Service |
| Total Login/LogoutRequestsAttempted | This counter represents the total number of Login and Logout requests that were attempted through this Extension Mobility
                                                Service. This number includes both successful and unsuccessful attempts. |
| Total Number of EMCC Messages | This represents the total number of messages related to EMCC Requests that came from remote clusters. |
| Number of Remote Devices | This represents the total number of devices from other clusters that are currently using a EMCC Base Device (EMCC Logged in). |
| Number of Unknown Remote Users | This represents the total number of users who were not found in any of the remote cluster during inter-cluster extension mobility
                                                login. |
| Active Inter-cluster Sessions | This represents the total number of inter cluster Extension Mobility requests that are currently in progress. |
| Total Number of Remote Users | This represents the total number of users from other cluster who use a local device of this cluster and have logged into a
                                                remote cluster. |
| EMCC Check User Requests Handled | This represents the total number of EMCC check user requests that came from remote clusters. |

| Counters | Counter Description |
|---|---|
| BuildFeaturePolicyCount | Indicates the number of built FCP files |
| FeaturePolicyChangeNotifications | Indicates the number of sent FCP change notifications |

| Counters | Counter Description |
|---|---|
| ACFsReceived | This counter represents the total number of RAS Admission Confirm messages that are received from the configured gatekeeper
                                                and its alternate gatekeepers. |
| ARQsAttempted | This counter represents the total number of RAS Admission Request messages that are attempted by using the configured gatekeeper
                                                and its alternate gatekeepers. |
| RasRetries | This counter represents the number of retries due to loss or delay of all RAS acknowledgement messages on the configured gatekeeper
                                                and its alternate gatekeepers. |
| VideoOutOfResources | This counter represents the total number of video-stream requests to the configured gatekeeper or its alternate gatekeepers
                                                that failed, most likely due to lack of bandwidth. |

| Counters | Counter Description |
|---|---|
| CallsActive | This counter represents the number of streaming connections that are currently active (in use) on the configured H.323 device;
                                                in other words, the number of calls that actually have a voice path that is connected. |
| CallsAttempted | This counter represents the total number of calls that have been attempted on a device, including both successful and unsuccessful
                                                call attempts. |
| CallsCompleted | This counter represents the total number of successful calls that were made from a device. |
| CallsInProgress | This counter represents the number of calls that are currently in progress on a device. |
| CallsRejectedDueToICTCallThrottling | This counter represents the total number of calls that are rejected due to Intercluster Trunk (ICT) call throttling since
                                                the start of the Cisco CallManager service. When the system reaches a threshold limit of 140 calls per 5 seconds, ICT will
                                                start throttling (rejecting) new calls. One cause for ICT call throttling occurs when calls across an ICT enter a route loop
                                                condition. |
| VideoCallsActive | This counter represents the number of video calls with video streaming connections that are currently active (in use) on all
                                                H.323 trunks that are registered with a Unified Communications Manager ; in other words, the number of calls that actually have video-streaming connections on a Unified Communications Manager . |
| VideoCallsCompleted | This counter represents the number of video calls that were actually connected with video streams for all H.323 trunks that
                                                were registered with a Unified Communications Manager . This number increases when the call terminates. |

| Counters | Counter Description |
|---|---|
| CallsAbandoned | This counter represents the number of abandoned calls that occurred through a hunt list. An abandoned call represents one
                                                in which a caller hangs up before the call is answered. |
| CallsActive | This counter represents the number of calls that are currently active (in use) that occurred through a hunt list. An active
                                                call represents one that gets distributed and answered, and to which a voice path connects. |
| CallsBusyAttempts | This counter represents the number of times that calls through a hunt list were attempted when all members of the line and/or
                                                route groups were busy. |
| CallsInProgress | This counter represents the number of calls that are currently in progress through a hunt list. A call in progress represents
                                                one that the call distributor is attempting to extend to a member of a line or route group and that has not yet been answered.
                                                Examples of a hunt list member include a line, a station device, a trunk device, or a port/channel of a trunk device. |
| CallsRingNoAnswer | This counter represents the total number of calls through a hunt list that rang but that called parties did not answer. |
| HuntListInService | This counter specifies whether the particular hunt list is currently in service. A value of 0 indicates that the hunt list
                                                is out of service; a value of 1 indicates that the hunt list is in service. Reasons that a hunt list could be out of service
                                                include the hunt list is not running on a primary Unified Communications Manager based on its Unified Communications Manager Group or the hunt list has been disabled in Cisco Unified Communications Manager Administration. |
| MembersAvailable | This counter represents the total number of available or idle members of line and route groups that belong to an in-service
                                                hunt list. An available member currently handles a call and will accept a new call. An idle member does not handle any call
                                                and will accept a new call. A hunt list member can comprise a route group, line group, or a combination. A member of a line
                                                group represents a directory number of a line on an IP phone or a voice-mail port. A member of a route group represents a
                                                station gateway, a trunk gateway, or port/channel of a trunk gateway. |

| Counters | Counter Description |
|---|---|
| HWConferenceActive | This counter represents the number of conferences that are currently active (in use) on a HW conference bridge device. One
                                                resource represents one stream. |
| HWConferenceCompleted | This counter represents the total number of conferences that have been allocated and released on a HW conference device. A
                                                conference starts when the first call connects to the bridge. The conference completes when the last call disconnects from
                                                the bridge. |
| OutOfResources | This counter represents the total number of times that an attempt was made to allocate a conference resource from a HW conference
                                                device and failed, for example, because all resources were already in use. |
| ResourceActive | This counter represents the number of resources that are currently in use (active) for this HW conference device. One resource
                                                represents one stream. |
| ResourceAvailable | This counter represents the total number of resources that are not active and are still available to be used now for a HW
                                                conference device. One resource represents one stream. |
| ResourceTotal | This counter represents the total number of resources for a HW conference bridge device. This counter equals the sum of the
                                                counters ResourceAvailable and ResourceActive. One resource represents one stream. |

| Counters | Counter Description |
|---|---|
| AssistantsActive | This counter represents the number of assistant consoles that are currently active. An active assistant console exists when
                                                an assistant is logged in from the assistant console desktop application. |
| LinesOpen | This counter represents the number of phone lines that the Cisco Unified Communications Manager Assistant application opened. An open phone line exists when the application assumes line control from CTI. |
| ManagersActive | This counter represents the current number of managers that the Cisco IPMA is servicing. |
| SessionsCurrent | This counter represents the total number of managers assistants that are currently using the Cisco Unified Communications Manager Assistant application. Each manager and each assistant constitute an active session; so, for one manager/assistant pair, this counter
                                                would reflect two sessions. |

| Counters | Counter Description |
|---|---|
| BandwidthAvailable | This counter represents the current bandwidth in a given location. A value of 0 indicates that no bandwidth is available. |
| BandwidthMaximum | This counter represents the maximum bandwidth that is available in a given location. A value of 0 indicates that infinite
                                                bandwidth is available. |
| CallsInProgress | This counter represents the number of calls that are currently in progress on a particular Unified Communications Manager . |
| OutOfResources | This counter represents the total number of times that a call on a particular Unified Communications Manager through the location failed due to lack of bandwidth. |
| RSVP AudioReservationErrorCounts | This counter represents the number of RSVP reservation errors in the audio stream. |
| RSVP MandatoryConnectionsInProgress | This counter represents the number of connections with mandatory RSVP that are in progress. |
| RSVP OptionalConnectionsInProgress | This counter represents the number of connections with optional RSVP that are in progress. |
| RSVP TotalCallsFailed | This counter represents the total number of failed calls due to a RSVP reservation failure. |
| RSVP VideoCallsFailed | This counter represents the number of video calls that failed due to a RSVP reservation failure. |
| RSVP VideoReservationErrorCounts | This counter represents the number of RSVP reservation errors in the video stream |
| VideoBandwidthAvailable | This counter represents the bandwidth that is currently available for video in the location where the person who initiated
                                                the video conference resides. A value of 0 indicates that no bandwidth is available. |
| VideoBandwidthMaximum | This counter represents the maximum bandwidth that is available for video in the location where the person who initiated the
                                                video conference resides. A value of 0 indicates that no bandwidth is allocated for video. |
| VideoOutOfResources | This counter represents the total number of failed video-stream requests (most likely due to lack of bandwidth) in the location
                                                where the person who initiated the video conference resides. |

| Note | One object exists for each Unified Communications Manager in the Unified Communications Manager group that is associated with the device pool that the annunciator device is configured to use. |
|---|---|

| Counter | Counter Description |
|---|---|
| ANNConnectionsLost | This counter represents the total number of times since the last restart of the Cisco IP Voice Media Streaming Application
                                                that a Unified Communications Manager connection was lost. |
| ANNConnectionState | For each Unified Communications Manager that is associated with an annunciator, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails). |
| ANNConnectionsTotal | This counter represents the total number of annunciator instances that have been started since the Cisco IP Voice Media Streaming
                                                Application service started. |
| ANNInstancesActive | This counter represents the number of actively playing (currently in use) announcements. |
| ANNStreamsActive | This counter represents the total number of currently active simplex (one direction) streams for all connections. Each stream
                                                direction counts as one stream. One internal stream provides the audio input and another output stream to the endpoint device. |
| ANNStreamsAvailable | This counter represents the remaining number of streams that are allocated for the annunciator device that are available for
                                                use. This counter starts as 2 multiplied by the number of configured connections (defined in the Cisco IP Voice Media Streaming
                                                App service parameter for the Annunciator, Call Count) and is reduced by one for each active stream that started. |
| ANNStreamsTotal | This counter represents the total number of simplex (one direction) streams that connected to the annunciator device since
                                                the Cisco IP Voice Media Streaming Application service started. |
| CFBConferencesActive | This counter represents the number of active (currently in use) conferences. |
| CFBConferencesTotal | This counter represents the total number of conferences that started since the Cisco IP Voice Media Streaming Application
                                                service started. |
| CFBConnectionsLost | This counter represents the total number of times since the last restart of the Cisco IP Voice Media Streaming Application
                                                that a Unified Communications Manager connection was lost. |
| CFBConnectionState | For each Unified Communications Manager that is associated with a SW Conference Bridge, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails). |
| CFBStreamsActive | This counter represents the total number of currently active simplex (one direction) streams for all conferences. Each stream
                                                direction counts as one stream. In a three-party conference, the number of active streams equals 6. |
| CFBStreamsAvailable | This counter represents the remaining number of streams that are allocated for the conference bridge that are available for
                                                use. This counter starts as 2 multiplied by the number of configured connections (defined in the Cisco IP Voice Media Streaming
                                                App service parameter for Conference Bridge, Call Count) and is reduced by one for each active stream that started. |
| CFBStreamsTotal | This counter represents the total number of simplex (one direction) streams that connected to the conference bridge since
                                                the Cisco IP Voice Media Streaming Application service started. |
| MOHAudioSourcesActive | This counter represents the number of active (currently in use) audio sources for this MOH server. Be aware that some of these
                                                audio sources may not be actively streaming audio data if no devices are listening. The exception exists for multicast audio
                                                sources, which will always be streaming audio. When an audio source is in use, even after the listener has disconnected, this counter will always have one input stream for
                                                each configured MOH codec. For unicast streams, the stream may exist in a suspended state where no audio data is received
                                                until a device connects to listen to the stream. Each MOH multicast resource uses one stream for each audio source and codec
                                                combination. For example, if the default audio source is configured for multicast, G.711 mu-law and wideband codecs, then
                                                two streams get used (default audio source + G.711 mu-law and default audio source + wideband). |
| MOHConnectionsLost | This counter represents the total number of times since the last restart of the Cisco IP Voice Media Streaming Application
                                                that a Unified Communications Manager connection was lost. |
| MOHConnectionState | For each Unified Communications Manager that is associated with an MOH, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails). |
| MOHStreamsActive | This counter represents the total number of active (currently in use) simplex (one direction) streams for all connections.
                                                One output stream exists for each device that is listening to a unicast audio source, and one input stream exists for each
                                                active audio source, multiplied by the number of MOH codecs. When an audio source has been used once, it will always have one input stream for each configured MOH codec. For unicast streams,
                                                the stream may exist in a suspended state where no audio data is received until a device connects to listen to the stream.
                                                Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, then two streams get used (default audio source + G.711
                                                mu-law and default audio source + wideband). |
| MOHStreamsAvailable | This counter represents the remaining number of streams that are allocated for the MOH device that are available for use.
                                                This counter starts as 408 plus the number of configured half-duplex unicast connections and is reduced by 1 for each active
                                                stream that started. The counter gets reduced by 2 for each multicast audio source, multiplied by the number of MOH codecs
                                                that are configured. The counter gets reduced by 1 for each unicast audio source, multiplied by the number of MOH codecs that
                                                are configured. |
| MOHStreamsTotal | This counter represents the total number of simplex (one direction) streams that have connected to the MOH server since the
                                                Cisco IP Voice Media Streaming Application service started. |
| MTPConnectionsLost | This counter represents the total number of times since the last restart of the Cisco IP Voice Streaming Application that
                                                a Unified Communications Manager connection was lost. |
| MTPConnectionState | For each Unified Communications Manager that is associated with an MTP, this counter represents the current registration state to Unified Communications Manager ; 0 indicates no registration to Unified Communications Manager ; 1 indicates registration to the primary Unified Communications Manager ; 2 indicates connection to the secondary Unified Communications Manager (connected to Unified Communications Manager but not registered until the primary Unified Communications Manager connection fails). |
| MTPConnectionsTotal | This counter represents the total number of MTP instances that have been started since the Cisco IP Voice Media Streaming
                                                Application service started. |
| MTPInstancesActive | This counter represents the number of active (currently in use) instances of MTP. |
| MTPStreamsActive | This counter represents the total number of currently active simplex (one direction) streams for all connections. Each stream
                                                direction counts as one stream. |
| MTPStreamsAvailable | This counter represents the remaining number of streams that are allocated for the MTP device that are available for use.
                                                This counter starts as 2 multiplied by the number of configured connections (defined in the Cisco IP Voice Media Streaming
                                                App service parameter for MTP, Call Count) and is reduced by one for each active stream that started. |
| MTPStreamsTotal | This counter represents the total number of simplex (one direction) streams that connected to the MTP device since the Cisco
                                                IP Voice Media Streaming Application service started. |

| Counters | Counter Description |
|---|---|
| CallsCompleted | This counter represents the total number of successful calls that were made from this MGCP Basic Rate Interface (BRI) device |
| Channel 1 Status | This counter represents the status of the indicated B-Channel that is associated with the MGCP BRI device. Possible values:
                                                0 (Unknown) indicates the status of the channel could not be determined; 1 (Out of service) indicates that this channel is
                                                not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates an
                                                active call on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-channel or for use
                                                as a Synch-Channel for BRI. |
| Channel 2 Status | This counter represents the status of the indicated B-Channel that is associated with the MGCP BRI device. Possible values:
                                                0 (Unknown) indicates the status of the channel could not be determined; 1 (Out of service) indicates that this channel is
                                                not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates an
                                                active call on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-channel or for use
                                                as a Synch-Channel for BRI. |
| DatalinkInService | This counter represents the state of the Data Link (D-Channel) on the corresponding digital access gateway. This value will
                                                get set to 1 (one) if the Data Link is up (in service) or 0 (zero) if the Data Link is down (out of service). |
| OutboundBusyAttempts | This counter represents the total number of times that a call through this MGCP BRI device was attempted when no voice channels
                                                were available. |

| Counters | Counter Description |
|---|---|
| CallsCompleted | This counter represents the total number of successful calls that were made from the port on an MGCP FXO device. |
| OutboundBusyAttempts | This counter represents the total number of times that a call through the port on this MGCP FXO device was attempted when
                                                no voice channels were available. |
| PortStatus | This counter represents the status of the FXO port that is associated with this MGCP FXO device. |

| Counters | Counter Description |
|---|---|
| CallsCompleted | This counter represents the total number of successful calls that were made from this port on the MGCP FXS device. |
| OutboundBusyAttempts | This counter represents the total number of times that a call through this port on the MGCP FXS device was attempted when
                                                no voice channels were available. |
| PortStatus | This counter represents the status of the FXS port that is associated with a MGCP FXS device. |

| Counters | Counter Description |
|---|---|
| BRIChannelsActive | This counter represents the number of BRI voice channels that are currently active in a call in the gateway |
| BRISpansInService | This counter represents the number of BRI spans that are currently available for use in the gateway. |
| FXOPortsActive | This counter represents the number of FXO ports that are currently active in a call in the gateway. |
| FXOPortsInService | This counter represents the number of FXO ports that are currently available for use in the gateway. |
| FXSPortsActive | This counter represents the number of FXS ports that are currently active in a call in the gateway. |
| FXSPortsInService | This counter represents the number of FXS ports that are currently available for use in the gateway. |
| PRIChannelsActive | This counter represents the number of PRI voice channels that are currently active in a call in the gateway. |
| PRISpansInService | This counter represents the number of PRI spans that are currently available for use in the gateway. |
| T1ChannelsActive | This counter represents the number of T1 CAS voice channels that are currently active in a call in the gateway. |
| T1SpansInService | This counter represents the number of T1 CAS spans that are currently available for use in the gateway. |

| Counters | Counter Description |
|---|---|
| CallsActive | This counter represents the number of calls that are currently active (in use) on this MGCP PRI device. |
| CallsCompleted | This counter represents the total number of successful calls that were made from this MGCP PRI device. |
| Channel 1 Status through Channel 15 Status (consecutively numbered) | This counter represents the status of the indicated B-Channel that is associated with a MGCP PRI device. Possible values:
                                                0 (Unknown) indicates that the status of the channel could not be determined; 1 (Out of service) indicates that this channel
                                                is not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates
                                                that an active call exists on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-Channel
                                                or for use as a Synch-Channel for E-1. |
| Channel 16 Status | This counter represents the status of the indicated B-Channel that is associated with a MGCP PRI Device. Possible values:
                                                0-Unknown, 1-Out of service, 2-Idle, 3-Busy, 4-Reserved, for an E1 PRI Interface, this channel is reserved for use as a D-Channel. |
| Channel 17 Status through Channel 31 Status (consecutively numbered) | This counter represents the status of the indicated B-Channel that is associated with the MGCP PRI Device. 0-Unknown, 1-Out
                                                of service, 2-Idle, 3-Busy, 4-Reserved. |
| DatalinkInService | This counter represents the state of the Data Link (D-Channel) on the corresponding digital access gateway. This value will
                                                get set to 1 (one) if the Data Link is up (in service) or 0 (zero) if the Data Link is down (out of service). |
| OutboundBusyAttempts | This counter represents the total number of times that a call through an MGCP PRI device was attempted when no voice channels
                                                were available. |

| Counters | Counter Description |
|---|---|
| CallsActive | This counter represents the number of calls that are currently active (in use) on this MGCP T1 CAS device. |
| CallsCompleted | This counter represents the total number of successful calls that were made from this MGCP T1 CAS device. |
| Channel 1 Status through Channel 24 Status (consecutively numbered) | This counter represents the status of the indicated B-Channel that is associated with an MGCP T1 CAS device. Possible values:
                                                0 (Unknown) indicates the status of the channel could not be determined; 1 (Out of service) indicates that this channel is
                                                not available for use; 2 (Idle) indicates that this channel has no active call and is ready for use; 3 (Busy) indicates that
                                                an active call exists on this channel; 4 (Reserved) indicates that this channel has been reserved for use as a D-Channel or
                                                for use as a Synch-Channel for E-1. |
| OutboundBusyAttempts | This counter represents the total number of times that a call through the MGCP T1 CAS device was attempted when no voice channels
                                                were available. |

| Counters | Counter Description |
|---|---|
| MobileCallsAnchored | This counter represents the total number of paths that are associated with single-mode/dual-mode phone call that is currently
                                                anchored on a Unified Communications Manager . Call anchoring occurs when a call enters an enterprise gateway and connects to a mobility application that then uses redirection
                                                to send the call back out an enterprise gateway. For example, this counter increments twice for a dual-mode phone-to-dual-mode
                                                phone call: once for the originating call and once for the terminating call. When the call terminates, this counter decrements
                                                accordingly. |
| MobilityHandinsAborted | This counter represents the total number of aborted handins. |
| MobileHandinsCompleted | This counter represents the total number of handins that were completed by dual-mode phones. A completed handin occurs when
                                                the call successfully connects in the enterprise network and the phone moves from WAN to WLAN. |
| MobilityHandinsFailed | This counter represents the total number of handins (calls on mobile devices that move from cellular to the wireless network)
                                                that failed. |
| MobilityHandoutsAborted | This counter represents the total number of aborted handouts. |
| MobileHandoutsCompleted | This counter represents the total number of handouts (calls on mobile devices that move from the enterprise WLAN network to
                                                the cellular network) that were completed. A completed handout occurs when the call successfully connects. |
| MobileHandoutsFailed | This counter represents the total number of handouts (calls on mobile devices that move from cellular to the wireless network)
                                                that failed. |
| MobilityFollowMeCallsAttempted | This counter represents the total number of follow-me calls that were attempted. |
| MobilityFollowMeCallsIgnoredDueToAnswerTooSoon | This counter represents the total number of follow-me calls that were ignored before the AnswerTooSoon timer went off. |
| MobilityIVRCallsAttempted | This counter represents the total number of attempted IVR calls. |
| MobilityIVRCallsFailed | This counter represents the total number of failed IVR calls. |
| MobilityIVRCallsSucceeded | This counter represents the total number of successful IVR calls. |
| MobilitySCCPDualModeRegistered | This counter represents the total number of dual-mode SCCP devices that are registered. |
| MobilitySIPDualModeRegistered | This counter represents the total number of dual-mode SIP devices that are registered. |

| Counters | Counter Description |
|---|---|
| MOHHighestActiveResources | This counter represents the largest number of simultaneously active MOH connections for an MOH server. This number includes
                                                both multicast and unicast connections. |
| MOHMulticastResourceActive | This counter represents the number of currently active multicast connections to multicast addresses that are served by an
                                                MOH server. Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, two streams get used (default audio source + G.711 mu-law
                                                and default audio source + wideband). |
| MOHMulticastResourceAvailable | This counter represents the number of multicast MOH connections to multicast addresses that are served by an MOH server that
                                                are not active and are still available to be used now for the MOH server. Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, two streams get used (default audio source + G.711 mu-law
                                                and default audio source + wideband). |
| MOHOutOfResources | This counter represents the total number of times that the Media Resource Manager attempted to allocate an MOH resource when
                                                all available resources on all MOH servers that are registered with a Unified Communications Manager were already active. |
| MOHTotalMulticastResources | This counter represents the total number of multicast MOH connections that are allowed to multicast addresses that are served
                                                by an MOH server. Each MOH multicast resource uses one stream for each audio source and codec combination. For example, if the default audio
                                                source is configured for multicast, G.711 mu-law and wideband codecs, two streams get used (default audio source + G.711 mu-law
                                                and default audio source + wideband). |
| MOHTotalUnicastResources | This counter represents the total number of unicast MOH connections that are allowed by an MOH server. Each MOH unicast resource uses one stream. |
| MOHUnicastResourceActive | This counter represents the number of active unicast MOH connections to an MOH server. Each MOH unicast resource uses one stream. |
| MOHUnicastResourceAvailable | This counter represents the number of unicast MOH connections that are not active and are still available to be used now for
                                                an MOH server. Each MOH unicast resource uses one stream. |

| Counters | Counter Description |
|---|---|
| OutOfResources | This counter represents the total number of times that an attempt was made to allocate an MTP resource from an MTP device
                                                and failed; for example, because all resources were already in use. |
| ResourceActive | This counter represents the number of MTP resources that are currently in use (active) for an MTP device. Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call. |
| ResourceAvailable | This counter represents the total number of MTP resources that are not active and are still available to be used now for an
                                                MTP device. Each MTP resource uses two streams. An MTP in use represents one MTP resource that has been allocated for use in a call. |
| ResourceTotal | This counter represents the total number of MTP resources that an MTP device provides. This counter equals the sum of the
                                                counters ResourceAvailable and ResourceActive. |

| Counters | Counter Description |
|---|---|
| ActiveCallListAndTrunkSubscriptions | This counter represents the active presence subscriptions for the call list feature as well as presence subscriptions through
                                                SIP trunk. |
| ActiveSubscriptions | This counter represents all active incoming and outgoing presence subscriptions. |
| CallListAndTrunkSubscriptionsThrottled | This counter represents the cumulative number of rejected call list and trunk side presence subscriptions due to throttling
                                                for the call list feature. |
| IncomingLineSideSubscriptions | This counter represents the cumulative number of presence subscriptions that were received on the line side. |
| IncomingTrunkSideSubscriptions | This counter represents the cumulative number of presence subscriptions that were received on the trunk side. |
| OutgoingTrunkSideSubscriptions | This counter represents the cumulative number of presence subscriptions that were sent on the trunk side. |

| Counters | Counter Description |
|---|---|
| CallForwardByRerouteCompleted | This counter represents the number of successful calls that has been forwarded by rerouting. Call forward by rerouting enables
                                                the path for a forwarded call to be optimized (minimizes the number of B-Channels in use) from the originator perspective.
                                                This counter gets reset when the Cisco CallManager service parameter Call Forward by Reroute Enabled is enabled or disabled,
                                                or when the Cisco CallManager service restarts. |
| PathReplacementCompleted | This counter represents the number of successful path replacements that have occurred. Path replacement in a QSIG network
                                                optimizes the path between two edge PINX (PBXs) that are involved in a call. This counter resets when the Cisco CallManager
                                                service parameter Path Replacement Enabled is enabled or disabled, or when the Cisco CallManager service restarts. |

| Counters | Counter Description |
|---|---|
| UDPPacketsThrottled | This counter represents the total number of incoming UDP packets that were throttled (dropped) because they exceeded the threshold
                                                for the number of incoming packets per second that is allowed from a single IP address. Configure the threshold via the SIP
                                                Station UDP Port Throttle Threshold and SIP Trunk UDP Port Throttle Threshold service parameters in Cisco Unified Communications Manager Administration . This counter increments for every throttled UDP packet that was received since the last restart of the Cisco CallManager
                                                Service. |

| Counters | Counter Description |
|---|---|
| CallsActive | This counter represents the number of calls that are currently active (in use) on this SIP device. |
| CallsAttempted | This counter represents the number of calls that have been attempted on this SIP device, including both successful and unsuccessful
                                                call attempts. |
| CallsCompleted | This counter represents the number of calls that were actually connected (a voice path was established) from a SIP device.
                                                This number increases when the call terminates. |
| CallsInProgress | This counter represents the number of calls that are currently in progress on a SIP device, including all active calls. When
                                                all calls that are in progress are connected, the number of CallsInProgress equals the number of CallsActive. |
| VideoCallsActive | This counter represents the number of video calls with streaming video connections that are currently active (in use) on this
                                                SIP device. |
| VideoCallsCompleted | This counter represents the number of video calls that were actually connected with video streams for this SIP device. This
                                                number increments when the call terminates. |

| Display Name | Description |
|---|---|
| DeviceResetAutomatically | This counter indicates the number of times that Unified Communications Manager automatically resets the device (SIP trunk). The device reset is based on the values that are specified in the Script Execution
                                                Error Recovery Action and System Resource Error Recovery Action fields on the SIP Normalization Script Configuration window
                                                in Cisco Unified Communications Manager Administration . When the device (SIP trunk) is reset due to script errors, the counter value increments. This count restarts when the device
                                                is reset manually. |
| DeviceResetManually | This counter indicates the number of times that the device (SIP trunk) is reset manually in Cisco Unified Communications Manager Administration or by other methods, such as AXL. When the device associated with a script is reset due to configuration changes, the counter
                                                value increments. The counter restarts in the following situations: The SIP trunk is deleted. The script on the trunk gets changed or deleted. Unified Communications Manager restarts. |
| ErrorExecution | This counter represents the number of execution errors that occurred while the script executed. Execution errors can occur
                                                while a message handler executes. Execution errors can be caused by resource errors, an argument mismatch in a function call,
                                                and so on. When an execution error occurs, Unified Communications Manager performs the following actions: Automatically restores the message to the original content before applying additional error handling actions. Increments the value of the counter. Takes appropriate action based on the configuration of the Script Execution Error Recovery Action and System Resource Error
                                                   Recovery Action fields in Cisco Unified Communications Manager Administration . Check the SIPNormalizationScriptError alarm for details, including the line number in the script that failed. Correct the
                                                script problem, upload the corrected script as needed, and reset the trunk. This counter increments every time an execution
                                                error occurs. This counter provides a count from the most recent trunk reset that involved a script configuration change.
                                                (A device reset alone does not restart the count; the script configuration must also change before the reset occurs.) If the counter continues to increment after you fix the script problem, examine the script again. |
| ErrorInit | This counter represents the number of times a script error occurred after the script successfully loaded into memory, but
                                                failed to initialize in Unified Communications Manager . A script can fail to initialize due to resource errors, an argument mismatch in a function call, the expected table was
                                                not returned, and so on. Check the SIPNormalizationScriptError alarm for details, including the line number in the script that failed. Correct the
                                                script problem, upload the corrected script as needed, and reset the trunk. This counter increments every time an initialization
                                                error occurs. This counter provides a count from the most recent trunk reset that was accompanied by a script configuration
                                                change. (A device reset alone does not restart the count; the script configuration must also change before the reset occurs.)
                                                If the counter continues to increment after you fix the script problem, examine the script again. When the error occurs during
                                                initialization, Unified Communications Manager automatically disables the script. |
| ErrorInternal | This counter indicates the number of internal errors that occurred while the script executed. Internal errors are very rare.
                                                If the value in this counter is higher than zero, a defect exists in the system that is not related to the script content
                                                or execution. Collect SDI traces and contact the Technical Assistance Center (TAC). |
| ErrorLoad | This counter represents the number of times a script error occurred when the script loaded into memory in Unified Communications Manager . A script can fail to load due to memory issues or syntax errors. Check the SIPNormalizationScriptError alarm for details. Check the script syntax for errors, upload the corrected script as
                                                needed, and reset the trunk. This counter increments every time a load error occurs. This counter provides a count from the
                                                most recent trunk reset that was accompanied by a script configuration change. (A device reset alone will not restart the
                                                count; the script configuration must also change before the reset occurs.) If the counter continues to increment even after
                                                you fix the script problem, examine the script again. |
| ErrorResource | This counter indicates whether the script encountered a resource error. Two kinds of resource errors exist: exceeding the value in the Memory Threshold field and exceeding the value in the Lua Instruction
                                                Threshold field. (Both fields display on the SIP Normalization Script Configuration window in Cisco Unified Communications Manager Administration .) If either condition occurs, Unified Communications Manager immediately closes the script and issues the SIPNormalizationScriptError alarm. If a resource error occurs while the script loads or initializes, the script is disabled. If a resource error occurs during
                                                execution, the configured system resource error recovery action is taken. (The setting of the System Resource Error Recovery
                                                Action field on the SIP Normalization Script Configuration window in Cisco Unified Communications Manager Administration defines this action.) |
| MemoryUsage | This counter specifies the amount of memory, in bytes, that the script consumes. This counter increases and decreases to match
                                                the amount of memory that the script uses. This count gets cleared when the script closes (because a closed script does not
                                                consume memory) and restarts when the script opens (gets enabled). A high number in this counter indicates a resource problem.
                                                Check the MemoryUsagePercentage counter and the SIPNormalizationResourceWarning alarm, which occur when the resource consumption
                                                exceeds an internally set threshold. |
| MemoryUsagePercentage | This counter specifies the percentage of the total amount of memory that the script consumes. The value in this counter is derived by dividing the value in the MemoryUsage counter by the value in the Memory Threshold
                                                field (in the SIP Normalization Script Configuration window) and multiplying the result by 100 to arrive at a percentage. This counter increases and decreases in accordance with the MemoryUsage counter. This count gets cleared when the script closes
                                                (because closed scripts do not consume memory) and restarts when the script opens (gets enabled). When this counter reaches
                                                the internally controlled resource threshold, the SIPNormalizationResourceWarning alarm is issued. |
| MessageRollback | This counter indicates the number of times that the system automatically rolled back a message. The system rolls back the
                                                message by using the error handling that is specified in the Script Execution Error Recovery Action field in the SIP Normalization
                                                Script Configuration window in Cisco Unified Communications Manager Administration. When an execution error occurs, Unified Communications Manager automatically restores the message to the original content before applying additional error handling actions. If error handling
                                                specifies Rollback only, no further action is taken beyond rolling back to the original message before the normalization attempt.
                                                For the other possible Script Execution Error Recovery Actions, message rollback always occurs first, followed by the specified
                                                action, such as disabling the script, resetting the script automatically, or resetting the trunk automatically. |
| msgAddContentBody | This counter represents the number of times that the script added a content body to the message. If you are using the msg:addContentBody
                                                API in the script, this counter increases each time that the msg:addContentBody API executes successfully. If the counter
                                                behavior is not as expected, examine the script logic for errors. |
| msgAddHeader | This counter represents the number of times that the script added a SIP header to the message. If you are using the msg:addHeader
                                                API in the script, this counter increases each time that the msg:addHeader API executes successfully. If the counter behavior
                                                is not as expected, examine the script logic for errors. |
| msgAddHeaderUriParameter | This counter represents the number of times that the script added a SIP header URI parameter to a SIP header in the message.
                                                If you are using the msg:addHeaderUriParameter API in the script, this counter increases each time that the msg:addHeaderUriParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| msgAddHeaderValueParameter | This counter represents the number of times that the script added a SIP header value parameter to a SIP header in the message.
                                                If you are using the msg:addHeaderValueParameter API in the script, this counter increases each time that the msg:addHeaderValueParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| msgApplyNumberMask | This counter represents the number of times that the script applied a number mask to a SIP header in the message. If you are
                                                using the msg:applyNumberMask API in the script, this counter increases each time that the msg:applyNumberMask API executes
                                                successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| msgBlock | This counter represents the number of times that the script blocked a message. If you are using the msg:block API in the script,
                                                this counter increases each time that the msg:block API executes successfully. If the counter behavior is not as expected,
                                                examine the script logic for errors. |
| msgConvertDiversionToHI | This counter represents the number of times that the script converted Diversion headers into History-Info headers in the message.
                                                If you are using the msg:convertDiversionToHI API in the script, this counter increases each time that the msg:convertDiversionToHI
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| msgConvertHIToDiversion | This counter represents the number of times that the script converted Diversion headers into History-Info headers in the message.
                                                If you are using the msg:convertDiversionToHI API in the script, this counter increases each time that the msg:convertDiversionToHI
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| msgModifyHeader | This counter represents the number of times that the script modified a SIP header in the message. If you are using the msg:modifyHeader
                                                API in the script, this counter increases each time that the msg:modifyHeader API executes successfully. If the counter behavior
                                                is not as expected, examine the script logic for errors. |
| msgRemoveContentBody | This counter represents the number of times that the script removed a content body from the message. If you are using the
                                                msg:removeContentBody API in the script, this counter increases each time that the msg:removeContentBody API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors. |
| msgRemoveHeader | This counter represents the number of times that the script removed a SIP header from the message. If you are using the msg:removeHeader
                                                API in the script, this counter increases each time that the msg:removeHeader API executes successfully. If the counter behavior
                                                is not as expected, examine the script logic for errors. |
| msgRemoveHeaderValue | This counter represents the number of times that the script removed a SIP header value from the message. If you are using
                                                the msg:removeHeaderValue API in the script, this counter increases each time that the msg:removeHeaderValue API executes
                                                successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| msgSetRequestUri | This counter represents the number of times that the script modified the request URI in the message. If you are using the
                                                msg:setRequestUri API in the script, this counter increases each time that the msg:setRequestUri API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors. |
| msgSetResponseCode | This counter represents the number of times that the script modified the response code and/or response phrase in the message.
                                                If you are using the msg:setResponseCode API in the script, this counter increases each time that the msg:setResponseCode
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| msgSetSdp | This counter represents the number of times that the script set the SDP in the message. If you are using the msg:setSdp API
                                                in the script, this counter increases each time that the msg:setSdp API executes successfully. If the counter behavior is
                                                not as expected, examine the script logic for errors. |
| ptAddContentBody | This counter represents the number of times that the script added a content body to the PassThrough (pt) object. If you are
                                                using the pt:addContentBody API in the script, this counter increases each time that the pt:addContentBody API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors. |
| ptAddHeader | This counter represents the number of times that the script added a SIP header to the PassThrough (pt) object. If you are
                                                using the pt:addHeader API in the script, this counter increases each time that the pt:addHeader API executes successfully.
                                                If the counter behavior is not as expected, examine the script logic for errors. |
| ptAddHeaderUriParameter | This counter represents the number of times that the script added a SIP header URI parameter to the PassThrough (pt) object.
                                                If you are using the pt:addHeaderUriParameter API in the script, this counter increases each time that the pt:addHeaderUriParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| ptAddHeaderValueParameter | This counter represents the number of times that the script added a SIP header value parameter to the PassThrough (pt) object.
                                                If you are using the pt:addHeaderValueParameter API in the script, this counter increases each time that the pt:addHeaderValueParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| ptAddRequestUriParameter | This counter represents the number of times that the script added a request URI parameter to the PassThrough (pt) object.
                                                If you are using the pt:addRequestUriParameter API in the script, this counter increases each time that the pt:addRequestUriParameter
                                                API executes successfully. If the counter behavior is not as expected, examine the script logic for errors. |
| ScriptActive | This counter indicates whether the script is currently active (running on the trunk). The following values display for the
                                                counter: 0—Indicates that the script is closed (disabled). 1—Indicates that the script is open and operational. To open the script that should be running on this trunk, perform the following actions: Check for any alarms that might indicate why the script is not open. Correct any errors. Upload a new script if necessary. Reset the trunk. |
| ScriptClosed | This counter indicates the number of times that Unified Communications Manager has closed the script. When the script is closed, it is not enabled on this device. Unified Communications Manager closes the script under one of the following conditions: The device was reset manually. The device was reset automatically (due to an error). The device was deleted. This count restarts when the SIP trunk is reset after a change to the script configuration and when Unified Communications Manager restarts. |
| ScriptDisabledAutomatically | This counter indicates the number of times that the system automatically disabled the script. The values that are specified
                                                in the Script Execution Error Recovery Action and System Resource Error Recovery Action fields in the SIP Normalization Script
                                                Configuration window in Cisco Unified Communications Manager Administration determine whether the script is disabled. The
                                                script also gets disabled as a result of script error conditions that are encountered during loading and initialization. This
                                                counter provides a count from the most recent manual device reset that involved a script configuration change (a device reset
                                                alone does not restart the count; the script must also have changed before the reset occurs). This counter increments every
                                                time Unified Communications Manager automatically disables a script due to script errors. If the number in this counter is higher than expected, perform the following actions: Check for SIPNormalizationScriptError alarm and SIPNormalizationAutoResetDisabled alarm. Check for any resource-related alarms and counters in RTMT to determine whether a resource issue is occurring. Check for any unexpected SIP normalization events in the SDI trace files. |
| ScriptOpened | This counter indicates the number of times that the Unified Communications Manager attempted to open the script. For the a script to open, it must load into memory in Unified Communications Manager , initialize, and be operational. A number greater than one in this counter means that Unified Communications Manager has made more than one attempt to open the script on this SIP trunk, either for an expected reason or due to an error during
                                                loading or initialization. The error can occur due to execution errors or resource errors or invalid syntax in the script.
                                                Expect this counter to be greater than one if any of these counters increment: DeviceResetManually, DeviceResetAutomatically,
                                                or ScriptResetAutomatically. The DeviceResetManually counter increments when an expected event, such as a maintenance window
                                                on the SIP trunk, causes the script to close. If the number in this counter is high for an unexpected reason, perform the following actions: Check for alarms, such as the SIPNormalizationScriptClosed, SIPNormalizationScriptError, or SIPNormalizationResourceWarning. Check resource-related alarms and counters in RTMT to determine whether a resource issue is occurring. Check for any unexpected SIP normalization events in the SDI trace files. This count restarts when the SIP trunk resets after a script configuration change and when Unified Communications Manager restarts. |
| ScriptResetAutomatically | This counter indicates the number of times that the system automatically reset the script. The script resets based on the
                                                values that are specified in the Script Execution Error Recovery Action and System Resource Error Recovery Action fields in
                                                the SIP Normalization Script Configuration window in Cisco Unified Communications Manager Administration. This counter specifies
                                                a count of the number of automatic script resets after the last manual device reset; this counter increments every time the Unified Communications Manager automatically resets a script due to script errors. If the number in this counter is higher than expected, perform the following actions: Check for a SIPNormalizationScriptError alarm. Check for any resource-related alarms and counters in RTMT to determine whether a resource issue is occurring. Check for any unexpected SIP normalization events in the SDI trace files. |

| Counters | Counter Description |
|---|---|
| AckIns | This counter represents the total number of ACK requests that the SIP device received. |
| AckOuts | This counter represents the total number of ACK requests that the SIP device sent. |
| ByeIns | This counter represents the total number of BYE requests that the SIP device received. This number includes retransmission. |
| ByeOuts | This counter represents the total number of BYE requests that the SIP device sent. This number includes retransmission. |
| CancelIns | This counter represents the total number of CANCEL requests that the SIP device received. This number includes retransmission. |
| CancelOuts | This counter represents the total number of CANCEL requests that the SIP device sent. This number includes retransmission. |
| CCBsAllocated | This counter represents the number of Call Control Blocks (CCB) that are currently in use by the SIP stack. Each active SIP
                                                dialog uses one CCB. |
| GlobalFailedClassIns | This counter represents the total number of 6xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses indicates that a SIP device, that is providing a client function, received a failure response message.
                                                Generally, the responses indicate that a server had definitive information on a particular called party and not just the particular
                                                instance in the Request-URI. |
| GlobalFailedClassOuts | This counter represents the total number of 6xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses indicates that a SIP device, that is providing a server function, received a failure response message.
                                                Generally, the responses indicate that a server had definitive information on a particular called party and not just the particular
                                                instance in the Request-URI. |
| InfoClassIns | This counter represents the total number of 1xx class SIP responses that the SIP device received. This includes retransmission.
                                                This class of responses provides information on the progress of a SIP request. |
| InfoClassOuts | This counter represents the total number of 1xx class SIP responses that the SIP device sent. This includes retransmission.
                                                This class of responses provides information on the progress of processing a SIP request. |
| InfoIns | This counter represents the total number of INFO requests that the SIP device has received. This number includes retransmission. |
| InfoOuts | This counter represents the total number of INFO requests that the SIP device has sent. This number includes retransmission. |
| InviteIns | This counter represents the total number of INVITE requests that the SIP device received. This number includes retransmission. |
| InviteOuts | This counter represents the total number of INVITE requests that the SIP device sent. This number includes retransmission. |
| NotifyIns | This counter represents the total number of NOTIFY requests that the SIP device received. This number includes retransmission. |
| NotifyOuts | This counter represents the total number of NOTIFY requests that the SIP device sent. This number includes retransmission. |
| OptionsIns | This counter represents the total number of OPTIONS requests that the SIP device received. This number includes retransmission. |
| OptionsOuts | This counter represents the total number of OPTIONS requests that the SIP device sent. This number includes retransmission. |
| PRAckIns | This counter represents the total number of PRACK requests that the SIP device received. This number includes retransmission. |
| PRAckOuts | This counter represents the total number of PRACK requests that the SIP device sent. This number includes retransmission. |
| PublishIns | This counter represents the total number of PUBLISH requests that the SIP device received. This number includes retransmissions. |
| PublishOuts | This counter represents the total number of PUBLISH requests that the SIP device sent. This number includes retransmission |
| RedirClassIns | This counter represents the total number of 3xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses provides information about redirections to addresses where the callee may be reachable. |
| RedirClassOuts | This counter represents the total number of 3xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses provides information about redirections to addresses where the callee may be reachable. |
| ReferIns | This counter represents the total number of REFER requests that the SIP device received. This number includes retransmission. |
| ReferOuts | This counter represents the total number of REFER requests that the SIP device sent. This number includes retransmission. |
| RegisterIns | This counter represents the total number of REGISTER requests that the SIP device received. This number includes retransmission. |
| RegisterOuts | This counter represents the total number of REGISTER requests that the SIP device sent. This number includes retransmission. |
| RequestsFailedClassIns | This counter represents the total number of 4xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses indicates a request failure by a SIP device that is providing a client function. |
| RequestsFailedClassOuts | This counter represents the total number of 4xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses indicates a request failure by a SIP device that is providing a server function. |
| RetryByes | This counter represents the total number of BYE retries that the SIP device sent. To determine the number of first BYE attempts,
                                                subtract the value of this counter from the value of the sipStatsByeOuts counter. |
| RetryCancels | This counter represents the total number of CANCEL retries that the SIP device sent. To determine the number of first CANCEL
                                                attempts, subtract the value of this counter from the value of the sipStatsCancelOuts counter. |
| RetryInfo | This counter represents the total number of INFO retries that the SIP device sent. To determine the number of first INFO attempts,
                                                subtract the value of this counter from the value of the sipStatsInfoOuts counter. |
| RetryInvites | This counter represents the total number of INVITE retries that the SIP device sent. To determine the number of first INVITE
                                                attempts, subtract the value of this counter from the value of the sipStatsInviteOuts counter. |
| RetryNotify | This counter represents the total number of NOTIFY retries that the SIP device sent. To determine the number of first NOTIFY
                                                attempts, subtract the value of this counter from the value of the sipStatsNotifyOuts counter. |
| RetryPRAck | This counter represents the total number of PRACK retries that the SIP device sent. To determine the number of first PRACK
                                                attempts, subtract the value of this counter from the value of the sipStatsPRAckOuts counter. |
| RetryPublish | This counter represents the total number of PUBLISH retries that the SIP device sent. To determine the number of first PUBLISH
                                                attempts, subtract the value of this counter from the value of the sipStatsPublishOuts counter. |
| RetryRefer | This counter represents the total number of REFER retries that the SIP device sent. To determine the number of first REFER
                                                attempts, subtract the value of this counter from the value of the sipStatsReferOuts counter. |
| RetryRegisters | This counter represents the total number of REGISTER retries that the SIP device sent. To determine the number of first REGISTER
                                                attempts, subtract the value of this counter from the value of the sipStatsRegisterOuts counter. |
| RetryRel1xx | This counter represents the total number of Reliable 1xx retries that the SIP device sent. |
| RetryRequestsOut | This counter represents the total number of Request retries that the SIP device sent. |
| RetryResponsesFinal | This counter represents the total number of Final Response retries that the SIP device sent. |
| RetryResponsesNonFinal | This counter represents the total number of non-Final Response retries that the SIP device sent. |
| RetrySubscribe | This counter represents the total number of SUBSCRIBE retries that the SIP device sent. To determine the number of first SUBSCRIBE
                                                attempts, subtract the value of this counter from the value of the sipStatsSubscribeOuts counter. |
| RetryUpdate | This counter represents the total number of UPDATE retries that the SIP device sent. To determine the number of first UPDATE
                                                attempts, subtract the value of this counter from the value of the sipStatsUpdateOuts counter. |
| SCBsAllocated | This counter represents the number of Subscription Control Blocks (SCB) that are currently in use by the SIP stack. Each subscription
                                                uses one SCB. |
| ServerFailedClassIns | This counter represents the total number of 5xx class SIP responses that the SIP device received. This number includes retransmission.
                                                This class of responses indicates that failure responses were received by a SIP device that is providing a client function. |
| ServerFailedClassOuts | This counter represents the total number of 5xx class SIP responses that the SIP device sent. This number includes retransmission.
                                                This class of responses indicates that failure responses were received by a SIP device that is providing a server function. |
| SIPGenericCounter1 | Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes. |
| SIPGenericCounter2 | Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes. |
| SIPGenericCounter3 | Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes. |
| SIPGenericCounter4 | Do not use this counter unless directed to do so by a Cisco Engineering Special build. Cisco uses information in this counter
                                                for diagnostic purposes. |
| SIPHandlerSDLQueueSignalsPresent | This counter represents the number of SDL signals that are currently on the four SDL priority queues of the SIPHandler component.
                                                The SIPHandler component contains the SIP stack. |
| StatusCode1xxIns | This counter represents the total number of 1xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 1xx responses: 100 Trying 180 Ringing 181 Call is being forwarded 182 Queued 183 Session Progress |
| StatusCode1xxOuts | This counter represents the total number of 1xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 1xx responses: 100 Trying 180 Ringing 181 Call is being forwarded 182 Queued 183 Session Progress |
| StatusCode2xxIns | This counter represents the total number of 2xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 2xx responses: 200 OK 202 Success Accepted |
| StatusCode2xxOuts | This counter represents the total number of 2xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 2xx responses: 200 OK 202 Success Accepted |
| StatusCode3xxins | This counter represents the total number of 3xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 3xx responses: 300 Multiple Choices 301 Moved Permanently 302 Moved Temporarily 303 Incompatible Bandwidth Units 305 Use Proxy 380 Alternative Service |
| StatusCode302Outs | This counter represents the total number of 302 Moved Temporarily response messages, including retransmission, that the SIP
                                                device sent. |
| StatusCode4xxIns | This counter represents the total number of 4xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 4xx responses: 400 Bad Request 401 Unauthorized 402 Payment Required 403 Forbidden 404 Not Found 405 Method Not Allowed 406 Not Acceptable 407 Proxy Authentication Required 408 Request Timeout 409 Conflict 410 Gone 413 Request Entity Too Large 414 Request-URI Too Long 415 Unsupported Media Type 416 Unsupported URI Scheme 417 Unknown Resource Priority 420 Bad Extension 422 Session Expires Value Too Small 423 Interval Too Brief 480 Temporarily Unavailable 481 Call/Transaction Does Not Exist 482 Loop Detected 483 Too Many Hops 484 Address Incomplete 485 Ambiguous 486 Busy Here 487 Request Terminated 488 Not Acceptable Here 489 Bad Subscription Event 491 Request Pending |
| StatusCode4xxOuts | This counter represents the total number of 4xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 4xx responses: 400 Bad Request 401 Unauthorized 402 Payment Required 403 Forbidden 404 Not Found 405 Method Not Allowed 406 Not Acceptable 407 Proxy Authentication Required 408 Request Timeout 409 Conflict 410 Gone 413 Request Entity Too Large 414 Request-URI Too Long 415 Unsupported Media Type 416 Unsupported URI Scheme 417 Unknown Resource Priority 420 Bad Extension 422 Session Expires Value Too Small 423 Interval Too Brief 480 Temporarily Unavailable 481 Call/Transaction Does Not Exist 482 Loop Detected 483 Too Many Hops 484 Address Incomplete 485 Ambiguous 486 Busy Here 487 Request Terminated 488 Not Acceptable Here 489 Bad Subscription Event 491 Request Pending |
| StatusCode5xxIns | This counter represents the total number of 5xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 5xx responses: 500 Server Internal Error 501 Not Implemented 502 Bad Gateway 503 Service Unavailable 504 Server Timeout 505 Version Not Supported 580 Precondition Failed |
| StatusCode5xxOuts | This counter represents the total number of 5xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 5xx responses: 500 Server Internal Error 501 Not Implemented 502 Bad Gateway 503 Service Unavailable 504 Server Timeout 505 Version Not Supported 580 Precondition Failed |
| StatusCode6xxIns | This counter represents the total number of 6xx response messages, including retransmission, that the SIP device received.
                                                This count includes the following 6xx responses: 600 Busy Everywhere 603 Decline 604 Does Not Exist Anywhere 606 Not Acceptable |
| StatusCode6xxOuts | This counter represents the total number of 6xx response messages, including retransmission, that the SIP device sent. This
                                                count includes the following 6xx responses: 600 Busy Everywhere 603 Decline 604 Does Not Exist Anywhere 606 Not Acceptable |
| SubscribeIns | This counter represents the total number of SUBSCRIBE requests that the SIP device received. This number includes retransmission. |
| SubscribeOuts | This counter represents the total number of SUBSCRIBE requests that the SIP device sent. This number includes retransmission. |
| SuccessClassIns | This counter represents the total number of 2xx class SIP responses that the SIP device received. This includes retransmission.
                                                This class of responses provides information on the successful completion of a SIP request. |
| SuccessClassOuts | This counter represents the total number of 2xx class SIP responses that the SIP device sent. This includes retransmission.
                                                This class of responses provides information on the successful completion of a SIP request. |
| SummaryRequestsIn | This counter represents the total number of SIP request messages that the SIP device received. This number includes retransmissions. |
| SummaryRequestsOut | This counter represents the total number of SIP request messages that the device sent. This number includes messages that
                                                originate on the device and messages that are being relayed by the device. When a particular message gets sent more than once,
                                                each transmission gets counted separately; for example, a message that is re-sent as a retransmission or as a result of forking. |
| SummaryResponsesIn | This counter represents the total number of SIP response messages that the SIP device received. This number includes retransmission. |
| SummaryResponsesOut | This counter represents the total number of SIP response messages that the SIP device sent (originated and relayed). This
                                                number includes retransmission. |
| UpdateIns | This counter represents the total number of UPDATE requests that the SIP device received. This number includes retransmission. |
| UpdateOuts | This counter represents the total number of UPDATE requests that the SIP device sent. This number includes retransmission. |

| Counters | Counter Description |
|---|---|
| ConfigMismatchesPersistent | This counter represents the number of times that a phone that is running SIP was persistently unable to register due to a
                                                configuration version mismatch between the TFTP server and Unified Communications Manager since the last restart of the Unified Communications Manager . This counter increments each time that Unified Communications Manager cannot resolve the mismatch and manual intervention is required (such as a configuration update or device reset). |
| ConfigMismatchesTemporary | This counter represents the number of times that a phone that is running SIP was temporarily unable to register due to a configuration
                                                version mismatch between the TFTP server and Unified Communications Manager since the last restart of the Cisco CallManager service. This counter increments each time Unified Communications Manager can resolve the mismatch automatically. |
| DBTimeouts | This counter represents the number of new registrations that failed because a timeout occurred while the system was attempting
                                                to retrieve the device configuration from the database. |
| NewRegAccepted | This counter represents the total number of new REGISTRATION requests that have been removed from the NewRegistration queue
                                                and processed since the last restart of the Cisco CallManager service. |
| NewRegQueueSize | This counter represents the number of REGISTRATION requests that are currently on the NewRegistration queue. The system places
                                                REGISTRATION requests that are received from devices that are not currently registered on this queue before they are processed. |
| NewRegRejected | This counter represents the total number of new REGISTRATION requests that were rejected with a 486 Busy Here response and
                                                not placed on the NewRegistration queue since the last restart of the Cisco CallManager service. The system rejects REGISTRATION
                                                requests if the NewRegistration queue exceeds a programmed size. |
| TokensAccepted | This counter represents the total number of token requests that have been granted since the last Unified Communications Manager restart. Unified Communications Manager grants tokens as long as the number of outstanding tokens remains below the number that is specified in the Cisco CallManager
                                                service parameter Maximum Phone Fallback Queue Depth. |
| TokensOutstanding | This counter represents the number of devices that have been granted a token but have not yet registered. The system requires
                                                that devices that are reconnecting to a higher priority Unified Communications Manager server be granted a token before registering. Tokens protect Unified Communications Manager from being overloaded with registration requests when it comes back online after a failover situation. |
| TokensRejected | This counter represents the total number of token requests that have been rejected since the last Unified Communications Manager restart. Unified Communications Manager will reject token request if the number of outstanding tokens is greater than the number that is specified in the Cisco CallManager
                                                service parameter Maximum Phone Fallback Queue Depth. |

| Counters | Counter Description |
|---|---|
| OutOfResources | This counter represents the total number of times that an attempt was made to allocate a conference resource from a SW conference
                                                device and failed because all resources were already in use. |
| ResourceActive | This counter represents the number of resources that are currently in use (active) for a SW conference device. One resource
                                                represents one stream. |
| ResourceAvailable | This counter represents the total number of resources that are not active and are still available to be used now for a SW
                                                conference device. One resource represents one stream. |
| ResourceTotal | This counter represents the total number of conference resources that a SW conference device provides. One resource represents
                                                one stream.This counter equals the sum of the ResourceAvailable and ResourceActive counters. |
| SWConferenceActive | This counter represents the number of software-based conferences that are currently active (in use) on a SW conference device. |
| SWConferenceCompleted | This counter represents the total number of conferences that have been allocated and released on a SW conference device. A
                                                conference starts when the first call connects to the bridge. The conference completes when the last call disconnects from
                                                the bridge. |

| Counters | Counter Description |
|---|---|
| BuildAbortCount | This counter represents the number of times that the build process aborted when it received a Build all request. This counter
                                                increases when building of device/unit/softkey/dial rules gets aborted as a result of group level change notifications. |
| BuildCount | This counter represents the number of times since the TFTP service started that the TFTP server has built all the configuration
                                                files in response to a database change notification that affects all devices. This counter increases by one every time the
                                                TFTP server performs a new build of all the configuration files. |
| BuildDeviceCount | This counter represents the number of devices that were processed in the last build of all the configuration files. This counter
                                                also updates while processing device change notifications. The counter increases when a new device is added and decreases
                                                when an existing device is deleted. |
| BuildDialruleCount | This counter represents the number of dial rules that were processed in the last build of the configuration files. This counter
                                                also updates while processing dial rule change notifications. The counter increases when a new dial rule is added and decreases
                                                when an existing dial rule is deleted. |
| BuildDuration | This counter represents the time in seconds that it took to build the last configuration files. |
| BuildSignCount | This counter represents the number of security-enabled phone devices for which the configuration file was digitally signed
                                                with the Unified Communications Manager server key in the last build of all the configuration files. This counter also updates while processing security-enabled
                                                phone device change notifications. |
| BuildSoftKeyCount | This counter represents the number of softkeys that were processed in the last build of the configuration files. This counter
                                                increments when a new softkey is added and decrements when an existing softkey is deleted. |
| BuildUnitCount | This counter represents the number of gateways that were processed in the last build of all the configuration files. This
                                                counter also updates while processing unit change notifications. The counter increases when a new gateway is added and decreases
                                                when an existing gateway is deleted. |
| ChangeNotifications | This counter represents the total number of all the Unified Communications Manager database change notifications that the TFTP server received. Each time that a device configuration is updated in Cisco Unified Communications Manager Administration , the TFTP server gets sent a database change notification to rebuild the XML file for the updated device. |
| DeviceChangeNotifications | This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete configuration files for devices. |
| DialruleChangeNotifications | This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete configuration files for dial rules. |
| EncryptCount | This counter represents the number of configuration files that were encrypted. This counter gets updated each time a configuration
                                                file is successfully encrypted |
| GKFoundCount | This counter represents the number of GK files that were found in the cache. This counter gets updated each time a GK file
                                                is found in the cache |
| GKNotFoundCount | This counter represents the number of GK files that were not found in the cache. This counter gets updated each time a request
                                                to get a GK file results in the cache not finding it |
| HeartBeat | This counter represents the heartbeat of the TFTP server. This incremental count indicates that the TFTP server is up and
                                                running. If the count does not increase, this means that the TFTP server is down. |
| HttpConnectRequests | This counter represents the number of clients that are currently requesting the HTTP GET file request. |
| HttpRequests | This counter represents the total number of file requests (such as requests for XML configuration files, phone firmware files,
                                                audio files, and so on.) that the HTTP server handled. This counter represents the sum total of the following counters since
                                                the HTTP service started: RequestsProcessed, RequestsNotFound, RequestsOverflow, RequestsAborted, and RequestsInProgress. |
| HttpRequestsAborted | This counter represents the total number of HTTP requests that the HTTP server. canceled (aborted) unexpectedly. Requests
                                                could get aborted if the requesting device cannot be reached (for instance, the device lost power) or if the file transfer
                                                was interrupted due to network connectivity problems. |
| HttpRequestsNotFound | This counter represents the total number of HTTP requests where the requested file was not found. When the HTTP server does
                                                not find the requested file, a message gets sent to the requesting device. |
| HttpRequestsOverflow | This counter represents the total number of HTTP requests that were rejected when the maximum number of allowable client connections
                                                was reached. The requests may have arrived while the TFTP server was building the configuration files or because of some other
                                                resource limitation. The Cisco TFTP advanced service parameter, Maximum Serving Count, sets the maximum number of allowable
                                                connections. |
| HttpRequestsProcessed | This counter represents the total number of HTTP requests that the HTTP server. successfully processed. |
| HttpServedFromDisk | This counters represents the number of requests that the HTTP server completed with the files that are on disk and not cached
                                                in memory. |
| LDFoundCount | This counter represents the number of LD files that were found in the cache. This counter gets updated each time that a LD
                                                file is found in cache memory. |
| LDNotFoundCount | This counter represents the number of LD files that were not found in cache memory. This counter gets updated each time that
                                                a request to get an LD file results in the cache not finding it. |
| MaxServingCount | This counter represents the maximum number of client connections that the TFTP can serve simultaneously. The Cisco TFTP advanced
                                                service parameter, Maximum Serving Count, sets this value. |
| Requests | This counter represents the total number of file requests (such as requests for XML configuration files, phone firmware files,
                                                audio files, and so on.) that the TFTP server handles. This counter represents the sum total of the following counters since
                                                the TFTP service started: RequestsProcessed, RequestsNotFound, RequestsOverflow, RequestsAborted, and RequestsInProgress. |
| RequestsAborted | This counter represents the total number of TFTP requests that the TFTP server canceled (aborted) unexpectedly. Requests could
                                                get aborted if the requesting device cannot be reached (for instance, the device lost power) or if the file transfer was interrupted
                                                due to network connectivity problems. |
| RequestsInProgress | This counter represents the number of file requests that the TFTP server currently is processing. This counter increases for
                                                each new file request and decreases for each file request that completes. This counter indicates the current load of the TFTP
                                                server. |
| RequestsNotFound | This counter represents the total number of TFTP requests for which the requested file was not found. When the TFTP server
                                                does not find the requested file, a message gets sent to the requesting device. If this counter increments in a cluster that
                                                is configured as secure, this event usually indicates an error condition. If, however, the cluster is configured as non-secure,
                                                it is normal for the CTL file to be absent (not found), which results in a message being sent to the requesting device and
                                                a corresponding increment in this counter. For non-secure clusters, this normal occurrence does not represent an error condition. |
| RequestsOverflow | This counter represents the total number of TFTP requests that were rejected because the maximum number of allowable client
                                                connections was exceeded, because requests arrived while the TFTP server was building the configuration files, or because
                                                of some other resource limitation. The Cisco TFTP advanced service parameter, Maximum Serving Count, sets the maximum number
                                                of allowable connections. |
| RequestsProcessed | This counter represents the total number of TFTP requests that the TFTP server successfully processed. |
| SegmentsAcknowledged | This counter represents the total number of data segments that the client devices acknowledged. Files get sent to the requesting
                                                device in data segments of 512 bytes, and for each 512-byte segment, the device sends the TFTP server an acknowledgment message.
                                                Each additional data segment gets sent upon receipt of the acknowledgment for the previous data segment until the complete
                                                file successfully gets transmitted to the requesting device. |
| SegmentsFromDisk | This counter represents the number of data segments that the TFTP server reads from the files on disk, while serving files. |
| SegmentSent | This counter represents the total number of data segments that the TFTP server sent. Files get sent to the requesting device
                                                in data segments of 512 bytes. |
| SEPFoundCount | This counter represents the number of SEP files that were successfully found in the cache. This counter gets updated each
                                                time that a SEP file is found in the cache. |
| SEPNotFoundCount | This counter represents the number of SEP files that were not found in the cache. This counter gets updated each time that
                                                a request to get a SEP file produces a not found in cache memory result. |
| SIPFoundCount | This counter represents the number of SIP files that were successfully found in the cache. This counter gets updated each
                                                time that a SIP file is found in the cache |
| SIPNotFoundCount | This counter represents the number of SIP files that were not found in the cache. This counter gets updated each time that
                                                a request to get a SIP file produces a not found in cache memory result. |
| SoftkeyChangeNotifications | This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete configuration files for softkeys. |
| UnitChangeNotifications | This counter represents the number of times that the TFTP server received database change notification to create, update,
                                                or delete gateway-related configuration files. |

| Counters | Counter Description |
|---|---|
| OutOfResources | This counter represents the total number of times that an attempt was made to allocate a transcoder resource from a transcoder
                                                device and failed; for example, because all resources were already in use. |
| ResourceActive | This counter represents the number of transcoder resources that are currently in use (active) for a transcoder device. Each transcoder resource uses two streams. |
| ResourceAvailable | This counter represents the total number of resources that are not active and are still available to be used now for a transcoder
                                                device. Each transcoder resource uses two streams. |
| ResourceTotal | This counter represents the total number of transcoder resources that a transcoder device provided. This counter equals the
                                                sum of the ResourceActive and ResourceAvailable counters. |

| Counters | Counter Description |
|---|---|
| ConferencesActive | This counter represents the total number of video conferences that are currently active (in use) on a video conference bridge
                                                device. The system specifies a conference as active when the first call connects to the bridge. |
| ConferencesAvailable | This counter represents the number of video conferences that are not active and are still available on a video conference
                                                device. |
| ConferencesCompleted | This counter represents the total number of video conferences that have been allocated and released on a video conference
                                                device. A conference starts when the first call connects to the bridge. The conference completes when the last call disconnects
                                                from the bridge. |
| ConferencesTotal | This counter represents the total number of video conferences that are configured for a video conference device. |
| OutOfConferences | This counter represents the total number of times that an attempt was made to initiate a video conference from a video conference
                                                device and failed because the device already had the maximum number of active conferences that is allowed (as specified by
                                                the TotalConferences counter). |
| OutOfResources | This counter represents the total number of times that an attempt was made to allocate a conference resource from a video
                                                conference device and failed, for example, because all resources were already in use. |
| ResourceActive | This counter represents the total number of resources that are currently active (in use) on a video conference bridge device.
                                                One resource gets used per participant. |
| ResourceAvailable | This counter represents the total number of resources that are not active and are still available on a device to handle additional
                                                participants for a video conference bridge device. |
| ResourceTotal | This counter represents the total number of resources that are configured on a video conference bridge device. One resource
                                                gets used per participant. |

| Counters | Counter Description |
|---|---|
| CallsCompleted | This counter represents the number of Make Call and End Call requests that the Cisco Web Dialer application successfully completed. |
| CallsFailed | This counter represents the number of Make Call and End Call requests that were unsuccessful. |
| RedirectorSessionsHandled | This counter represents the total number of HTTP sessions that the Redirector servlet handled since the last service startup. |
| RedirectorSessionsInProgress | This counter represents the number of HTTP sessions that are currently being serviced by the Redirector servlet. |
| RequestsCompleted | This counter represents the number of Make Call and End Call requests that the Web Dialer servlet successfully completed. |
| RequestsFailed | This counter represents the number of Make Call and End Call requests that failed. |
| SessionsHandled | This counter represents the total number of CTI sessions that the Cisco Web Dialer servlet handled since the last service startup. |
| SessionsInProgress | This counter represents the number of CTI sessions that the Cisco Web Dialer servlet is currently servicing. |

| Counters | Counter Description |
|---|---|
| CallsActive | This counter represents the number of calls that are currently active (in use) on the WSMConnector device. |
| CallsAttempted | This counter represents the number of calls that have been attempted on the WSMConnector device, including both successful
                                                and unsuccessful call attempts. |
| CallsCompleted | This counter represents the number of calls that are connected (a voice path was established) through the WSMConnector device.
                                                The counter increments when the call terminates. |
| CallsInProgress | This counter represents the number of calls that are currently in progress on the WSMConnector device. This includes all active
                                                calls. When the number of CallsInProgress equals the number of CallsActive, this indicates that all calls are connected. |
| DMMSRegistered | This counter represents the number of DMMS subscribers that are registered to the WSM. |

| Counters | Counter Description |
|---|---|
| Errors | This counter represents the total number of HTTP errors (for example, 401 Unauthorized) that the connector encountered. A
                                                Tomcat HTTP connector represents an endpoint that receives requests and sends responses. The connector handles HTTP/HTTPS
                                                requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. |
| MBytesReceived | This counter represents the amount of data that the connector received. A Tomcat HTTP connector represents an endpoint that
                                                receives requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS responses that occur
                                                when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. |
| MBytesSent | This counter represents the amount of data that the connector sent. A Tomcat HTTP connector represents an endpoint that receives
                                                requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. |
| Requests | This counter represents the total number of request that the connector handled. A Tomcat HTTP connector represents an endpoint
                                                that receives requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS responses that
                                                occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. |
| ThreadsTotal | This counter represents the current total number of request processing threads, including available and in-use threads, for
                                                the connector. A Tomcat HTTP connector represents an endpoint that receives requests and sends responses. The connector handles
                                                HTTP/HTTPS requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. |
| ThreadsMax | This counter represents the maximum number of request processing threads for the connector. Each incoming request on a Unified Communications Manager related window requires a thread for the duration of that request. If more simultaneous requests are received than the currently
                                                available request processing threads can handle, additional threads will get created up to the configured maximum shown in
                                                this counter. If still more simultaneous requests are received, they accumulate within the server socket that the connector
                                                created, up to an internally specified maximum number. Any further simultaneous requests will receive connection refused messages
                                                until resources are available to process them. A Tomcat HTTP connector represents an endpoint that receives requests and sends responses. The connector handles HTTP/HTTPS
                                                requests and sends HTTP/HTTPS responses that occur when Unified Communications Manager related windows are accessed. The Secure Socket Layer (SSL) status of the URLs for the web application provides basis for
                                                the instance name for each Tomcat HTTP connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. |
| ThreadsBusy | This counter represents the current number of busy/in-use request processing threads for the connector. A Tomcat Connector
                                                represents an endpoint that receives requests and sends responses. The connector handles HTTP/HTTPS requests and sends HTTP/HTTPS
                                                responses that occur when web pages that are related to Unified Communications Manager are accessed. The Secure Sockets Layer (SSL) status of the URLs for the web application provides the basis for the instance
                                                name for each Tomcat connector. For example, https://<IP Address>:8443 for SSL or http://<IP Address>:8080 for non-SSL. |

| Counters | Counter Description |
|---|---|
| KBytesMemoryFree | This counter represents the amount of free dynamic memory block (heap memory) in the Tomcat Java Virtual Machine. The dynamic
                                                memory block stores all objects that Tomcat and its web applications, such as Cisco Unified Communications Manager Administration , Cisco Unified Serviceability , and Cisco Unity Connection create. When the amount of free dynamic memory is low, more memory gets automatically allocated,
                                                and total memory size (represented by the KbytesMemoryTotal counter) increases but only up to the maximum (represented by
                                                the KbytesMemoryMax counter). You can determine the amount of memory in use by subtracting KBytesMemoryFree from KbytesMemoryTotal. |
| KBytesMemoryMax | This counter represents the amount of free dynamic memory block (heap memory) in the Tomcat Java Virtual Machine. The dynamic
                                                memory block stores all objects that Tomcat and its web applications, such as Cisco Unified Communications Manager Administration , Cisco Unified Serviceability , and Cisco Unity Connection Administration , create. |
| KBytesMemoryTotal | This counter represents the current total dynamic memory block size, including free and in-use memory, of Tomcat Java Virtual
                                                Machine. The dynamic memory block stores all objects that Tomcat and its web applications, such as Cisco Unified Communications Manager Administration , Cisco Unified Serviceability , and Cisco Unity Connection Administration , create. |

| Counters | Counter Description |
|---|---|
| Errors | This counter represents the total number of HTTP errors (for example, 401 Unauthorized) that a Unified Communications Manager related web application encountered. The URLs for the web application provide the basis instance name for each Tomcat Web
                                                Application. For example, Cisco Unified Communications Manager Administration ( https://<IP Address>:8443/ccmadmin ) gets identified by ccmadmin, Cisco Unified Serviceability gets identified by ccmservice, Unified Communications Manager User Options gets identified by ccmuser, Cisco Unity Connection Administration ( https://<IP Address>:8443/cuadmin ) gets identified by cuadmin, and URLs that do not have an extension, such as https://<IP Address>:8443 or http://<IP Address>:8080 ), get identified by _root. |
| Requests | This counter represents the total number of requests that the web application handles. Each time that a web application is
                                                accessed, its Requests counter increments accordingly. The URLs for the web application provide the basis instance name for
                                                each Tomcat Web Application. For example, Cisco Unified Communications Manager Administration ( https://<IP Address>:8443/ccmadmin ) gets identified by ccmadmin, Cisco Unified Serviceability gets identified by ccmservice, Unified Communications Manager User Options gets identified by ccmuser, Cisco Unity Connection Administration ( https://<IP Address>:8443/cuadmin ) gets identified by cuadmin, and URLs that do not have an extension, such as https://<IP Address>:8443 or http://<IP Address>:8080 ), get identified by _root. |
| SessionsActive | This counter represents the number of sessions that the web application currently has active (in use). The URLs for the web
                                                application provide the basis instance name for each Tomcat Web Application. For example, Cisco Unified Communications Manager Administration ( https://<IP Address>:8443/ccmadmin ) gets identified by ccmadmin, Cisco Unified Serviceability gets identified by ccmservice, Unified Communications Manager User Options gets identified by ccmuser, Cisco Unity Connection Administration ( https://<IP Address>:8443/cuadmin ) gets identified by cuadmin, and URLs that do not have an extension, such as https://<IP Address>:8443 or http://<IP Address>:8080 ), get identified by _root. |

| Counters | Counter Descriptions |
|---|---|
| MessagesProcessed | This counter represents the number of database change notifications that have been processed. This counter refreshes every
                                                15 seconds. |
| MessagesProcessing | This counter represents the number of change notification messages that are currently being processed or are waiting to be
                                                processed in the change notification queue for this client. This counter refreshes every 15 seconds. |
| QueueHeadPointer | This counter represents the head pointer to the change notification queue. The head pointer acts as the starting point in
                                                the change notification queue. To determine the number of notifications in the queue, subtract the head pointer value from
                                                the tail pointer value. By default, this counter refreshes every 15 seconds. |
| QueueMax | This counter represents the largest number of change notification messages that will be processed for this client. This counter
                                                remains cumulative since the last restart of the Cisco Database Layer Monitor service. |
| QueueTailPointer | This counter represents the tail pointer to the change notification queue. The tail pointer represents the ending point in
                                                the change notification queue. To determine the number of notifications in the queue, subtract the head pointer value from
                                                the tail pointer value. By default, this counter refreshes every 15 seconds |
| TablesSubscribed | This counter represents the number of tables in which this client has subscribed. |

| Counter | Counter Descriptions |
|---|---|
| Clients | This counter represents the number of change notification clients (services/servlets) that have subscribed for change notification. |
| Queue Delay | This counter provides the number of seconds that the change notification process has messages to process but is not processing
                                                them. This condition is true if: Either Change Notification Requests Queued in Database (QueuedRequestsInDB) and Change Notification Requests Queued in Memory
                                                   (QueuedRequestsInMemory) are non-zero, or The Latest Change Notification Messages Processed count is not changing. This condition gets checked every 15 seconds. |
| QueuedRequestsInDB | This counter represents the number of change notification records that are in the DBCNQueue (Database Change Notification
                                                Queue) table via direct TCP/IP connection (not queued in shared memory). This counter refreshes every 15 seconds. |
| QueuedRequestsInMemory | This counter represents the number of change notification requests that are queued in shared memory. |

| Counters | Counter Descriptions |
|---|---|
| CcmDbSpace_Used | This counter represents the amount of Ccm DbSpace that is being consumed |
| CcmtempDbSpace_Used | This counter represents the amount of Ccmtemp DbSpace that is being consumed. |
| CNDbSpace_Used | This counter represents the percentage of CN dbspace consumed. |
| LocalDSN | This counter represents the data source name (DSN) that is being referenced from the local machine. |
| SharedMemory_Free | This counter represents total shared memory that is free. |
| SharedMemory_Used | This counter total shared memory that is used. |
| RootDbSpace_Used | This counter represents the amount of RootDbSpace that is being consumed. |

| Counters | Counter Descriptions |
|---|---|
| ERDbSpace_Used | This counter represents the amount of enterprise replication DbSpace that was consumed. |
| ERSBDbSpace_Used | This counter represents the amount of ERDbSpace that was consumed. |

| Counters | Counter Descriptions |
|---|---|
| Frag Creates | This counter represents the number of IP datagrams fragments that have been generated at this entity. |
| Frag Fails | This counter represents the number of IP datagrams that were discarded at this entity because the datagrams could not be fragmented,
                                                such as datagrams where the Do not Fragment flag was set. |
| Frag OKs | This counter represents the number of IP datagrams that were successfully fragmented at this entity. |
| In Delivers | This counter represents the number of input datagrams that were delivered to IP user protocols. This includes Internet Control
                                                Message Protocol (ICMP). |
| In Discards | This counter represents the number of discarded input IP datagrams when no problems were encountered. Lack of buffer space
                                                provides one possible reason. This counter does not include any datagrams that were discarded while they were awaiting reassembly. |
| In HdrErrors | This counter represents the number of discarded input datagrams that had header errors. This includes bad checksums, version
                                                number mismatch, other format errors, time-to-live exceeded, and other errors that were discovered in processing IP options. |
| In Receives | This counter represents the number of input datagrams that were received from all network interfaces. This counter includes
                                                datagrams that were received with errors |
| In UnknownProtos | This counter represents the number of locally addressed datagrams that were received successfully but discarded because of
                                                an unknown or unsupported protocol. |
| InOut Requests | This counter represents the number of incoming IP datagrams that were received and the number of outgoing IP datagrams that
                                                were sent. |
| Out Discards | This counter represents the number of output IP datagrams that were not transmitted and were discarded. Lack of buffer space
                                                provides one possible reason. |
| Out Requests | This counter represents the total number of IP datagrams that local IP protocols, including ICMP, supply to IP in requests
                                                transmission. This counter does not include any datagrams that were counted in ForwDatagrams. |
| Reasm Fails | This counter represents the number of IP reassembly failures that the IP reassembly algorithm detected, including time outs,
                                                errors, and so on. This counter does not represent the discarded IP fragments because some algorithms, such as the algorithm
                                                in RFC 815, can lose track of the number of fragments because it combines them as they are received. |
| Reasm OKs | This counter represents the number of IP datagrams that were successfully reassembled. |
| Reasm Reqds | This counter represents the number of IP fragments that were received that required reassembly at this entity. |

| Counters | Counter Descriptions |
|---|---|
| % Mem Used | This counter displays the system physical memory utilization as a percentage. The value of this counter equals (Total KBytes
                                                - Free KBytes - Buffers KBytes - Cached KBytes + Shared KBytes) / Total KBytes, which also corresponds to the Used KBytes/Total
                                                KBytes. |
| % Page Usage | This counter represents the percentage of active pages. |
| % VM Used | This counter displays the system virtual memory utilization as a percentage. The value of this counter equals (Total KBytes
                                                - Free KBytes - Buffers KBytes - Cached KBytes + Shared KBytes + Used Swap KBytes) / (Total KBytes + Total Swap KBytes), which
                                                also corresponds to Used VM KBytes/Total VM KBytes. |
| Buffers KBytes | This counter represents the capacity of buffers in your system in kilobytes. |
| Cached KBytes | This counter represents the amount of cached memory in kilobytes. |
| Free KBytes | This counter represents the total amount of memory that is available in your system in kilobytes. |
| Free Swap KBytes | This counter represents the amount of free swap space that is available in your system in kilobytes. |
| Faults Per Sec | This counter represents the number of page faults (both major and minor) that the system made per second (post 2.5 kernels
                                                only). This does not necessarily represent a count of page faults that generate I/O because some page faults can get resolved
                                                without I/O. |
| Low Total | This counter represents the total low (non-paged) memory for kernel. |
| Low Free | This counter represents the total free low (non-paged) memory for kernel. |
| Major Faults Per Sec | This counter represents the number of major faults that the system has made per second that have required loading a memory
                                                page from disk (post 2.5 kernels only). |
| Pages | This counter represents the number of pages that the system paged in from the disk plus the number of pages that the system
                                                paged out to the disk. |
| Pages Input | This counter represents the number of pages that the system paged in from the disk. |
| Pages Input Per Sec | This counter represents the total number of kilobytes that the system paged in from the disk per second. |
| Pages Output | This counter represents the number of pages that the system paged out to the disk. |
| Pages Output Per Sec | This counter represents the total number of kilobytes that the system paged out to the disk per second. |
| Shared KBytes | This counter represents the amount of shared memory in your system in kilobytes. |
| Total KBytes | This counter represents the total amount of memory in your system in kilobytes. |
| Total Swap KBytes | This counter represents the total amount of swap space in your system in kilobytes. |
| Total VM KBytes | This counter represents the total amount of system physical and memory and swap space (Total Kbytes + Total Swap Kbytes) that
                                                is in use in your system in kilobytes. |
| Used KBytes | This counter represents the amount of system physical memory that is in use in kilobytes. The value of the Used KBytes counter
                                                equals Total KBytes minus Free KBytes minus Buffers KBytes minus Cached KBytes plus Shared KBytes. In a Linux environment,
                                                the Used KBytes value that displays in the top or free command output equals the difference of Total KBytes and Free KBytes
                                                and also includes the sum of Buffers KBytes and Cached KBytes. |
| Used Swap KBytes | This counter represents the amount of swap space that is in use on your system in kilobytes. |
| Used VM KBytes | This counter represents the system physical memory and the amount of swap space that is in use on your system in kilobytes.
                                                The value equals Total KBytes - Free KBytes - Buffers KBytes - Cached KBytes + Shared KBytes + Used Swap KBytes. This corresponds
                                                to Used Mem KBytes + Used Swap KBytes. |

| Counters | Counter Descriptions |
|---|---|
| Rx Bytes | This counter represents the number of bytes, including framing characters, that were received on the interface. |
| Rx Dropped | This counter represents the number of inbound packets that were chosen to be discarded even though no errors had been detected.
                                                This prevents the packet from being delivered to a higher layer protocol. Discarding packets to free up buffer space provides
                                                one reason. |
| Rx Errors | This counter represents the number of inbound packets (packet-oriented interfaces) and the number of inbound transmission
                                                units (character-oriented or fixed-length interfaces) that contained errors that prevented them from being deliverable to
                                                a higher layer protocol. |
| Rx Multicast | This counter represents the number of multicast packets that were received on this interface. |
| Rx Packets | This counter represents the number of packets that this sublayer delivered to a higher sublayer. This does not include the
                                                packets that were addressed to a multicast or broadcast address at this sublayer. |
| Total Bytes | This counter represents the total number of received (Rx) bytes and transmitted (Tx) bytes. |
| Total Packets | This counter represents the total number of Rx packets and Tx packets. |
| Tx Bytes | This counter represents the total number of octets, including framing characters, that were transmitted out from the interface. |
| Tx Dropped | This counter represents the number of outbound packets that were chosen to be discarded even though no errors were detected.
                                                This action prevents the packet from being delivered to a higher layer protocol. Discarding a packet to free up buffer space
                                                represents one reason. |
| Tx Errors | This counter represents the number of outbound packets (packet-oriented interfaces) and the number of outbound transmission
                                                units (character-oriented or fixed-length interfaces) that could not be transmitted because of errors. |
| Tx Packets | This counter represents the total number of packets that the higher level protocols requested for transmission, including
                                                those that were discarded or not sent. This does not include packets that were addressed to a multicast or broadcast address
                                                at this sublayer. |
| Tx QueueLen | This counter represents the length of the output packet queue (in packets). |

| Counters | Counter Descriptions |
|---|---|
| Number of Replicates Created | This counter displays the number of replicates that were created by Informix for the DB tables. This counter displays information
                                                during Replication Setup. |
| Replicate_State | This counter represents the state of replication. The following list provides possible values: 0—Initializing. The counter equals 0 when the server is not defined or when the server is defined but the template has not
                                                   completed. 1—Replication setup script fired from this node. Cisco recommends that you run utils dbreplication status on the CLI to determine
                                                   the location and cause of the failure. 2—Good Replication. 3—Bad Replication. A counter value of 3 indicates replication in the cluster is bad. It does not mean that replication failed
                                                   on a particular server in the cluster. Cisco recommends that you run utils dbreplication status on the CLI to determine the
                                                   location and cause of the failure. 4—Replication setup did not succeed. |

| Counters | Counter Descriptions |
|---|---|
| % CPU Time | This counter represents the percentage of CPU time that is dedicated to handling I/O requests that were issued to the disk.
                                                This counter is no longer valid when the counter value equals -1. |
| % Used | This counter represents the percentage of disk space that is in use on this file system. |
| % Wait in Read | Not Used. The Await Read Time counter replaces this counter. This counter is no longer valid when the counter value equals
                                                -1. |
| % Wait in Write | Not Used. The Await Write Time counter replaces this counter.This counter is no longer valid when the counter value equals
                                                -1. |
| Await Read Time | This counter represents the average time, measured in milliseconds, for Read requests that are issued to the device to be
                                                served. This counter is no longer valid when the counter value equals -1. |
| Await Time | This counter represents the average time, measured in milliseconds, for I/O requests that were issued to the device to be
                                                served. This includes the time that the requests spent in queue and the time that was spent servicing them.This counter is
                                                no longer valid when the counter value equals -1. |
| Await Write Time | This counter represents the average time, measured in milliseconds, for write requests that are issued to the device to be
                                                served. This counter is no longer valid when the counter value equals -1. |
| Queue Length | This counter represents the average queue length for the requests that were issued to the disk.This counter is no longer valid
                                                when the counter value equals -1. |
| Read Bytes Per Sec | This counter represents the amount of data in bytes per second that was read from the disk. |
| Total Mbytes | This counter represents the amount of total disk space in megabytes that is on this file system. |
| Used Mbytes | This counter represents the amount of disk space in megabytes that is in use on this file system. |
| Write Bytes Per Sec | This counter represents the amount of data that was written to the disk in bytes per second. |

| Counters | Counter Descriptions |
|---|---|
| % CPU Time | This counter, which is expressed as a percentage of total CPU time, represents the tasks share of the elapsed CPU time since
                                                the last update. |
| % MemoryUsage | This counter represents the percentage of physical memory that a task is currently using. |
| Data Stack Size | This counter represents the stack size for task memory status. |
| Nice | This counter represents the nice value of the task. A negative nice value indicates that the process has a higher priority
                                                while a positive nice value indicates that the process has a lower priority. If the nice value equals zero, do not adjust
                                                the priority when you are determining the dispatchability of a task. |
| Page Fault Count | This counter represents the number of major page faults that a task encountered that required the data to be loaded into memory. |
| PID | This counter displays the task-unique process ID. The ID periodically wraps, but the value will never equal zero. |
| Process Status | This counter displays the process status: 0—Running 1—Sleeping 2—Uninterruptible disk sleep 3—Zombie 4—Stopped 5— Paging 6—Unknown |
| Shared Memory Size | This counter displays the amount of shared memory (KB) that a task is using. Other processes could potentially share the same
                                                memory. |
| STime | This counter displays the system time (STime), measured in jiffies, that this process has scheduled in kernel mode. A jiffy
                                                corresponds to a unit of CPU time and gets used as a base of measurement. One second comprises 100 jiffies. |
| Thread Count | This counter displays the number of threads that are currently grouped with a task. A negative value (-1) indicates that this
                                                counter is currently not available. This happens when thread statistics (which includes all performance counters in the Thread
                                                object as well as the Thread Count counter in the Process object) are turned off because the system total processes and threads
                                                exceeded the default threshold value. |
| Total CPU Time Used | This counter displays the total CPU time in jiffies that the task used in user mode and kernel mode since the start of the
                                                task. A jiffy corresponds to a unit of CPU time and gets used as a base of measurement. One second comprises 100 jiffies. |
| UTime | This counter displays the time, measured in jiffies, that a task has scheduled in user mode. |
| VmData | This counter displays the virtual memory usage of the heap for the task in kilobytes (KB). |
| VmRSS | This counter displays the virtual memory (Vm) resident set size (RSS) that is currently in physical memory in kilobytes (KB).
                                                This includes the code, data, and stack. |
| VmSize | This counter displays the total virtual memory usage for a task in kilobytes (KB). It includes all code, data, shared libraries,
                                                and pages that have been swapped out: Virtual Image = swapped size + resident size. |
| Wchan | This counter displays the channel (system call) in which the process is waiting. |

| Counters | Counter Descriptions |
|---|---|
| % CPU Time | This counter displays the processors share of the elapsed CPU time, excluding idle time, since the last update. This share
                                                gets expressed as a percentage of total CPU time. |
| Idle Percentage | This counter displays the percentage of time that the processor is in the idle state and did not have an outstanding disk
                                                I/O request. |
| IOwait Percentage | This counter represents the percentage of time that the processor is in the idle state while the system had an outstanding
                                                disk I/O request. |
| Irq Percentage | This counter represents the percentage of time that the processor spends executing the interrupt request that is assigned
                                                to devices, including the time that the processor spends sending a signal to the computer. |
| Nice Percentage | This counter displays the percentage of time that the processor spends executing at the user level with nice priority. |
| Softirq Percentage | This counter represents the percentage of time that the processor spends executing the soft IRQ and deferring task switching
                                                to get better CPU performance. |
| System Percentage | This counter displays the percentage of time that the processor is executing processes in system (kernel) level. |
| User Percentage | This counter displays the percentage of time that the processor is executing normal processes in user (application) level. |

| Counters | Counter Descriptions |
|---|---|
| Allocated FDs | This counter represents the total number of allocated file descriptors. |
| Being Used FDs | This counter represents the number of file descriptors that are currently in use in the system. |
| Freed FDs | This counter represents the total number of allocated file descriptors on the system that are freed. |
| Max FDs | This counter represents the maximum number of file descriptors that are allowed on the system. |
| Total CPU Time | This counter represents the total time in jiffies that the system has been up and running. |
| Total Processes | This counter represents the total number of processes on the system. |
| Total Threads | This counter represents the total number of threads on the system. |

| Counters | Counter Description |
|---|---|
| Active Opens | This counter displays the number of times that the TCP connections made a direct transition to the SYN-SENT state from the
                                                CLOSED state. |
| Attempt Fails | This counter displays the number of times that the TCP connections have made a direct transition to the CLOSED state from
                                                either the SYN-RCVD state or the SYN-RCVD state, plus the number of times TCP connections have made a direct transition to
                                                the LISTEN state from the SYS-RCVD state. |
| Curr Estab | This counter displays the number of TCP connections where the current state is either ESTABLISHED or CLOSE- WAIT. |
| Estab Resets | This counter displays the number of times that the TCP connections have made a direct transition to the CLOSED state from
                                                either the ESTABLISHED state or the CLOSE-WAIT state. |
| In Segs | This counter displays the total number of segments that were received, including those received in error. This count only
                                                includes segments that are received on currently established connections. |
| InOut Segs | This counter displays the total number of segments that were sent and the total number of segments that were received. |
| Out Segs | This counter displays the total number of segments that were sent. This count only includes segments that are sent on currently
                                                established connections, but excludes retransmitted octets. |
| Passive Opens | This counter displays the number of times that TCP connections have made a direct transition to the SYN-RCVD state from the
                                                LISTEN state. |
| RetransSegs | This counter displays the total number of segments that were retransmitted because the segment contains one or more previously
                                                transmitted octets. |

| Counters | Counter Description |
|---|---|
| % CPU Time | This counter displays the thread share of the elapsed CPU time since the last update. This counter expresses the share as
                                                a percentage of the total CPU time. |
| PID | This counter displays the threads leader process ID. |

| Counters | Counter Description |
|---|---|
| DaysUntilCertExpiry | This counter indicates the number of days that remain until the IME distributed cache certificate expires. You must replace
                                                the certificate before it expires. When the value of this counter falls below 14, an alert gets generated once every day until the value exceeds 14. |

| Counters | Counter Description |
|---|---|
| BlockedValidationOrigTLSLimit | This counter indicates the total number of blocked validations that occurred because the TLSValidationThreshold was reached. |
| BlockedValidationTermTLSLimit | This counter indicates the total number of blocked validations that occurred because the TLSValidationThreshold was reached. |
| ClientsRegistered | This counter indicates the number of Cisco IME clients that are currently connected to the Cisco IME server. |
| IMEDistributedCacheHealth | The counter indicates the health of the IME distributed cache. The following values may display: 0 (red)—Warns that the IME distributed cache is not functioning properly; for example, the Cisco IME cannot resolve issues
                                                   after the network has been partitioned In this case, validation attempts might fail. For example, the Cisco IME service is
                                                   not connected to the network and is unable to reach the bootstrap servers. An alert gets generated once every hour until the value changes from red status. 1 (yellow)—Indicates that the Cisco IME network is experiencing minor issues, such as connectivity between bootstrap servers
                                                   or other Cisco IME network issues. (Check the Cisco IME alarms to determine network issues.) 2 (green)—Indicates that the Cisco IME is functioning normally and is considered healthy. |
| IMEDistributedCacheNodeCount | The counter is an integer that indicates an approximation of the total number of nodes in the IME distributed cache. Since
                                                each physical Cisco IME server hosts multiple nodes, this counter does not directly indicate the number of physical Cisco
                                                IME servers that participate in the IME distributed cache. This counter can provide an indication of the health of the IME
                                                distributed cache; for example, a problem may exist with the IME distributed cache if an expected value displays on one day
                                                (for example, 300), but then on the next day, the value drops dramatically (for example, to 10 or 2). |
| IMEDistributedCacheQuota | Indicates the number of individual DIDs that can be written into the IME Distributed Cache, by Cisco Unified CMs attached
                                                to this IME server. This number is determined by the overall configuration of the IME Distributed Cache, and the IME license
                                                installed on the IME server. |
| IMEDistributedCacheQuotaUsed | Indicates the total number of unique DID numbers that have been configured, to be published via enrolled patterns for Intercompany
                                                Media Services, by Cisco Unified CMs currently attached to this IME server. |
| IMEDistributedCacheReads | This counter indicates the total number of reads that the Cisco IME server has attempted into the IME distributed cache. This
                                                number serves as an indicator of whether the Cisco IME server is functional; that is, whether the server is interacting with
                                                other nodes. |
| IMEDistributedCacheStoredData | This counter indicates the amount of IME distributed cache storage, measured in bytes, that this Cisco IME server provides. |
| IMEDistributedCacheStores | This counter indicates the total number of stores (published numbers) that the Cisco IME server has attempted into the IME
                                                distributed cache. This number serves as an indicator of whether the Cisco IME server is functional. |
| InternetBandwidthRecv | This counter measures the amount of downlink Internet bandwidth, in Kbits/s, that the Cisco IME server is consuming. |
| InternetBandwidthSend | This counter measures the amount of uplink Internet bandwidth that the Cisco IME server in Kbits/s is consuming. |
| TerminatingVCRs | This counter indicates the total Cisco IME voice call records (VCRs) that are stored on the Cisco IME server after receiving
                                                calls. You can use these records for validating learned routes. |
| ValidationAttempts | This counter indicates the total number of attempts that the Cisco IME server has made at performing a validation because
                                                the dialed number was found in the Cisco IME network. This counter provides an overall indication of system usage. |
| ValidationsAwaitingConfirmation | This counter indicates the total number of destination phone numbers that have been validated, but that are awaiting further
                                                calls to improve the security of the system. If you use a higher level of security for learning new routes, the Cisco IME
                                                server requires multiple successful validations for a route before that route is available for calls over IP. This counter
                                                tracks the number of successful validations that have not resulted in available IP routes. |
| ValidationsPending | This counter, which is an integer, indicates the number of scheduled validation attempts to retrieve a learned route. This
                                                value indicates the backlog of work for the Cisco IME service on the Cisco IME server. An alert gets generated when the value rises either above the high watermark or falls below the low watermark. After the high
                                                watermark is reached, an alert gets sent immediately and then once an hour until the value falls below the high watermark.
                                                When the high watermark is reached, the Cisco IME service cannot clear the backlog of work prior to the expiration of data;
                                                this situation causes records to drop, and validation may not occur. To reduce the workload, add more Cisco IME servers that
                                                can share the workload. |
| ValidationsBlocked | This counter indicates the number of times that the Cisco IME service rejected a validation attempt because the calling party
                                                was not trusted; that is, the party was on a blacklist or not on a whitelist. This value provides an indication of the number
                                                of cases where a VoIP calls cannot happen in the future because of the blocked validation. |

| Counters | Counter Description |
|---|---|
| QueueSignalsPresent 1-High | This counter indicates the number of high-priority signals in the queue on the Cisco IME server. High-priority signals include
                                                timeout events, internal KeepAlive messages, internal process creation, and so on. A large number of high-priority events
                                                causes degraded performance of the Cisco IME service and results in slower or failed validations. Use this counter in conjunction
                                                with the QueueSignalsProcessed 1-High counter to determine the processing delay on the Cisco IME server. |
| QueueSignalsPresent 2-Normal | This counter indicates the number of normal-priority signals in the queue on the Cisco IME server. Normal-priority signals
                                                include call validations, IME distributed cache operations such as stores and reads, and so on. A large number of normal-priority
                                                events causes degraded performance of the Cisco IME service and may result in slower or failed validations or disruption to
                                                IME distributed cache connectivity. Use this counter in conjunction with the QueueSignalsProcessed 2-Normal counter to determine
                                                the processing delay on the Cisco IME server. Since high-priority signal must complete before normal priority signals begin to process, check the high-priority counters
                                                to accurately understand why a delay occurs. |
| QueueSignalsPresent 3-Low | This counter indicates the number of low-priority signals in the queue on the Cisco IME server. Low-priority signals include
                                                IME distributed cache signaling and other events. A large number of signals in this queue may disrupt IME distributed cache
                                                connectivity or other events. |
| QueueSignalsPresent 4-Lowest | This counter indicates the number of lowest-priority signals in the queue on the Cisco IME server. A large number of signals
                                                in this queue may disrupt IME distributed cache connectivity and other events. |
| QueueSignalsProcessed 1-High | This counter indicates the number of high-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 1-High counter to determine the processing delay for this queue. |
| QueueSignalsProcessed 2-Normal | This counter indicates the number of normal-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 1-High counter to determine the processing delay for this queue.
                                                High-priority signals are processed before normal-priority signals. |
| QueueSignalsProcessed 3-Low | This counter indicates the number of low-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 3-Low counter to determine the processing delay for this queue. |
| QueueSignalsProcessed 4-Lowest | This counter indicates the number of lowest-priority signals that the Cisco IME service processes for each one-second interval.
                                                Use this counter in conjunction with the QueueSignalsPresent 4-Lowest counter to determine the processing delay for this queue. |
| QueueSignalsProcessed Total | This counter provides a total of all queue signals that the Cisco IME service processes for each one-second period for all
                                                queue levels: high, normal, low, and lowest. |

| Counters | Counter Description |
|---|---|
| CallsAccepted | This counter indicates the number of Cisco IME calls that the Unified Communications Manager received successfully and that the called party answered, resulting in an IP call. |
| CallsAttempted | This counter indicates the number of calls that the Unified Communications Manager received through Cisco IME. This number includes accepted calls, failed calls, and busy, no-answer calls. The counter increments
                                                each time that Unified Communications Manager receives a call through Cisco IME. |
| CallsReceived | This counter indicates the number of calls that Unified Communications Manager receives through Cisco IME. This number includes accepted calls, failed calls, and busy, no-answer calls. The counter increments
                                                on call initiation. |
| CallsSetup | This counter indicates the number of Cisco IME calls that Unified Communications Manager placed successfully and that the remote party answered, resulting in an IP call. |
| DomainsUnique | This counter indicates the number of unique domain names of peer enterprises that the Cisco IME client discovered. The counter
                                                serves as an indicator of overall system usage. |
| FallbackCallsFailed | This counter indicates the total number of failed fallback attempts. |
| FallbackCallsSuccessful | This counter indicates the total number of Cisco IME calls that have fallen back to the PSTN mid-call due to a quality problem.
                                                The counter includes calls initiated and calls received by this Unified Communications Manager . |
| IMESetupsFailed | This counter indicates the total number of call attempts for which a Cisco IME route was available but that were set up through
                                                the PSTN due to a failure to connect to the target over the IP network. |
| RoutesLearned | This counter indicates the total number of distinct phone numbers that the Cisco IME has learned and that are present as routes
                                                in the Unified Communications Manager routing tables. If this number grows too large, the server may exceed the per-cluster limit, and you may need to add additional
                                                servers to your cluster. |
| RoutesPublished | This counter indicates the total number of DIDs that were published successfully into the IME distributed cache across all
                                                Cisco IME client instances. The counter provides a dynamic measurement that gives you an indication of your own provisioned
                                                usage and a sense of how successful the system has been in storing the DIDs in the network. |
| RoutesRejected | This counter indicates the number of learned routes that were rejected because the administrator blacklisted the number or
                                                domain. This counter provides an indication of the number of cases where a VoIP call cannot happen in the future because of
                                                the blocked validation. |
| VCRUploadRequests | This counter indicates the number of voice call record (VCR) upload requests that the Unified Communications Manager has sent to the Cisco IME server to be stored in the IME distributed cache. |

| Counters | Counter Description |
|---|---|
| IMEServiceStatus | This counter indicates the overall health of the connection to the Cisco IME services for a particular Cisco IME client instance
                                                ( Unified Communications Manager ). The following values may display for the counter: 0—Indicates an unknown state (which may mean that the Cisco IME service is not active). If the value specifies 0, an alert gets generated once per hour while the connection remains in the unknown state. 1—Indicates a healthy state; that is, the Cisco IME service is active, and the Unified Communications Manager has successfully established a connection to its primary and backup servers for the Cisco IME client instance, if configured. 2—Indicates an unhealthy state; that is, the Cisco IME service is active, but the Unified Communications Manager has not successfully established a connection to its primary and backup servers for the Cisco IME client instance, if configured. |