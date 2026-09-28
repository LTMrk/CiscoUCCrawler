---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-provisioning-pa2d-b-mpp-7800-provisioning-guide-pa2d-ec74d9a780
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/provisioning/pa2d_b_mpp-7800-provisioning-guide/pa2d_b_mpp-7800-provisioning-guide_chapter_0100.html
retrieved_at: 2026-08-21T02:22:49.574400+00:00
---

Cisco IP Phone 7800 Series and Cisco IP Conference Phone 7832 Multiplatform Phones Provisioning Guide

# Cisco IP Phone 7800 Series and Cisco IP Conference Phone 7832 Multiplatform Phones Provisioning Guide

Updated: December 20, 2017

Chapter: Provisioning Parameters

## Chapter: Provisioning Parameters

# Provisioning Parameters

## Provisioning Parameters Overview

This chapter describes the provisioning parameters that can be used in configuration profile scripts.

## Configuration Profile Parameters

The following table defines the function and usage of each parameter in the Configuration Profile Parameters section under the Provisioning tab.

Parameter Name

Description and Default Value

Provision Enable

Controls all resync actions independently of firmware upgrade actions. Set to Yes to enable remote provisioning.

The default value is Yes.

Resync On Reset

Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades.

The default value is Yes.

Resync Random Delay

A random delay following the boot-up sequence before performing the reset, specified in seconds. In a pool of IP Telephony
                                          devices that are scheduled to simultaneously power up, this introduces a spread in the times at which each unit sends a resync
                                          request to the provisioning server. This feature can be useful in a large residential deployment, in the case of a regional
                                          power failure.

The value for this field must be an integer ranging between 0 and 65535.

The default value is 2.

Resync At (HHmm)

The time (HHmm) that the device resynchronizes with the provisioning server.

The value for this field must be a four-digit number ranging from 0000 to 2400 to indicate the time in HHmm format. For example,
                                          0959 indicates 09:59.

The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value,
                                          the Resync Periodic parameter is ignored.

Resync At Random Delay

Prevents an overload of the provisioning server when a large number of devices power-on simultaneously.

To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours
                                          and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay =
                                          (Resync At Random Delay + 30)/60 minutes, the input value in seconds is converted to minutes, rounding up to the next minute
                                          to calculate the final random_delay interval.

The valid value ranges between 0 and 65535.

This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes).

Resync Periodic

The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only
                                          after the first successful sync with the server.

The valid formats are as follows:

An integer

Example: An input of 3000 indicates that the next resync occurs in 3000 seconds.

Multiple integers

Example: An input of 600,1200,300 indicates that the first resync occurs in 600 seconds, the second resync occurs in 1200 seconds after the first one, and
                                                the third resync occurs in 300 seconds after the second one.

A time range

Example, an input of 2400+30 indicates that the next resync occurs in between 2400 and 2430 seconds after a successful resync.

Set this parameter to zero to disable periodic resynchronization.

The default value is 3600 seconds.

Resync Error Retry Delay

If a resync operation fails because the IP Telephony device was unable to retrieve a profile from the server, or the downloaded
                                          file is corrupt, or an internal error occurs, the device tries to resync again after a time specified in seconds.

The valid formats are as follows:

An integer

Example: An input of 300 indicates that the next retry for resync occurs in 300 seconds.

Multiple integers

Example: An input of 600,1200,300 indicates that the first retry occurs in 600 seconds after the failure, the second retry occurs in 1200 seconds after the
                                                failure of the first retry, and the third retry occurs in 300 seconds after the failure of the second retry.

A time range

Example, an input of 2400+30 indicates that the next retry occurs in between 2400 and 2430 seconds after a resync failure.

If the delay is set to 0, the device does not try to resync again following a failed resync attempt.

Forced Resync Delay

Maximum delay (in seconds) the phone waits before performing a resynchronization.

The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable
                                          to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in
                                          succession without interruption.

The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of
                                          the counter. Resync events are delayed until this counter decrements to zero.

The valid value ranges between 0 and 65535.

The default value is 14,400 seconds.

Resync From SIP

Enables a resync to be triggered via a SIP NOTIFY message.

The default value is Yes.

Resync After Upgrade Attempt

Enables or disables the resync operation after any upgrade occurs. If Yes is selected, sync is triggered.

The default value is Yes.

Resync Trigger 1, Resync Trigger 2

Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE.

The default value is (empty).

Resync Fails On FNF

A resync is considered unsuccessful if a requested profile is not received from the server. This can be overridden by this
                                          parameter. When it is set to no , the device accepts a file-not-found response from the server as a successful resync.

The default value is Yes.

Profile Rule

Profile Rule B

Profile Rule C

Profile Rule D

Each profile rule informs the phone of a source from which to obtain a profile (configuration file). During every resync operation,
                                          the phone applies all the profiles in sequence.

Default: /$PSN.xml

If you are applying AES-256-CBC encryption to the configuration files, specify the encryption key with the --key keyword as follows:

[--key <encryption key>]

You can enclose the encryption key in double-quotes (") optionally.

DHCP Option To Use

DHCP options, delimited by commas, used to retrieve firmware and profiles.

The default value is 66,160,159,150,60,43,125.

Log Request Msg

This parameter contains the message that is sent to the syslog server at the start of a resync attempt.

The default value is $PN $MAC –Requesting % $SCHEME://$SERVIP:$PORT$PATH .

Log Success Msg

The syslog message that is issued upon successful completion of a resync attempt.

The default value is $PN $MAC –Successful Resync % $SCHEME://$SERVIP:$PORT$PATH -- $ERR .

Log Failure Msg

The syslog message that is issued after a failed resync attempt.

The default value is $PN $MAC -- Resync failed: $ERR .

User Configurable Resync

Allows a user to resync the phone from the IP phone screen.

The default value is Yes.

## Firmware Upgrade Parameters

The following table defines the function and usage of each parameter in the Firmware Upgrade section of the Provisioning tab.

Parameter Name

Description and Default Value

Upgrade Enable

Enables firmware upgrade operations independently of resync actions.

The default value is Yes.

Upgrade Error Retry Delay

The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer
                                          that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next
                                          firmware upgrade attempt occurs when this timer counts down to zero.

The default value is 3600 seconds.

Upgrade Rule

A firmware upgrade script that defines upgrade conditions and associated firmware URLs. It uses the same syntax as Profile
                                          Rule.

Use the following format to enter the upgrade rule:

<tftp|http|https>://<ip address>/image/<load name>

For example:

tftp://192.168.1.5/image/sip78xx.11-0-1MPP-BN.loads

If no protocol is specified, TFTP is assumed. If no server-name is specified, the host that requests the URL is used as the
                                          server name. Isf no port is specified, the default port is used (69 for TFTP, 80 for HTTP, or 443 for HTTPS).

The default value is blank.

Log Upgrade Request Msg

Syslog message issued at the start of a firmware upgrade attempt.

Default: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH

Log Upgrade Success Msg

Syslog message issued after a firmware upgrade attempt completes successfully.

The default value is $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR

Log Upgrade Failure Msg

Syslog message issued after a failed firmware upgrade attempt.

The default value is $PN $MAC -- Upgrade failed: $ERR

Peer Firmware Sharing

Enables or disables the Peer Firmware Sharing feature. Select Yes or No to enable or to disable the feature.

Default: Yes

Peer Firmware Sharing Log Server

Indicates the IP address and the port to which the UDP message is sent.

For example: 10.98.76.123:514 where, 10.98.76.123 is the IP address and 514 is the port number.

## General Purpose Parameters

The following table defines the function and usage of each parameter in the General Purpose Parameters section of the Provisioning tab.

Parameter Name

Description and Default Value

GPP A - GPP P

Encryption keys.

URLs.

Multistage provisioning status information.

Post request templates.

Parameter name alias maps.

Partial string values, eventually combined into complete parameter values.

The default value is blank.

## Macro Expansion Variables

Certain macro variables are recognized within the following provisioning parameters:

Profile_Rule

Profile_Rule_*

Resync_Trigger_*

Upgrade_Rule

Log_*

GPP_* (under specific conditions)

Within these parameters, syntax types, such as $NAME or $(NAME), are recognized and expanded.

Macro variable substrings can be specified with the notation $(NAME:p) and $(NAME:p:q), where p and q are non-negative integers
                              (available in revision 2.0.11 and above). The resulting macro expansion is the substring starting at character offset p, with
                              length q (or else till end-of-string if q is not specified). For example, if GPP_A contains ABCDEF, then $(A:2) expands to
                              CDEF, and $(A:2:3) expands to CDE.

An unrecognized name is not translated, and the $NAME or $(NAME) form remains unchanged in the parameter value after expansion.

Parameter Name

Description and Default Value

$

The form $$ expands to a single $ character.

A through P

Replaced by the contents of the general purpose parameters GPP_A through GPP_P.

SA through SD

$SA through $SD are recognized as arguments to the optional resync URL qualifier, --key.

MA

MAC address using lower case hex digits, for example, 000e08aabbcc.

MAU

MAC address using upper case hex digits, for example 000E08AABBCC.

MAC

MAC address using lower case hex digits, and colons to separate hex digit pairs. For example 00:0e:08:aa:bb:cc.

PN

Product Name. For example, CP-7832-3PCC.

PSN

Product Series Number. For example, V03.

SN

Serial Number string. for example 88012BA01234.

CCERT

SSL Client Certificate status: Installed or Not Installed.

IP

IP address of the phone within its local subnet. For example 192.168.1.100.

EXTIP

External IP of the phone, as seen on the Internet. For example 66.43.16.52.

SWVER

Software version string. For example, sip78xx.11-0-1MPP.

HWVER

Hardware version string. For example, 2.0.1

PRVST

Provisioning State (a numeric string):

-1 = explicit resync request

0 = power-up resync

1 = periodic resync

2 = resync failed, retry attempt

UPGST

Upgrade State (a numeric string):

1 = first upgrade attempt

2 = upgrade failed, retry attempt

UPGERR

Result message (ERR) of previous upgrade attempt; for example http_get failed.

PRVTMR

Seconds since last resync attempt.

UPGTMR

Seconds since last upgrade attempt.

REGTMR1

Seconds since Line 1 lost registration with SIP server.

REGTMR2

Seconds since Line 2 lost registration with SIP server.

UPGCOND

Legacy macro name.

SCHEME

File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL.

SERV

Request target server host name, as obtained after parsing resync or upgrade URL.

SERVIP

Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup.

PORT

Request target UDP/TCP port, as obtained after parsing resync or upgrade URL.

PATH

Request target file path, as obtained after parsing resync or upgrade URL.

ERR

Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the
                                          UPGERR variable in the case of upgrade attempts.

UIDn

The contents of the Line n UserID configuration parameter.

EMS

Extension Mobility Status

MUID

Extension Mobility User ID

MPWD

Extension Mobility Password

## Internal Error Codes

The phone defines a number of internal error codes (X00–X99) to facilitate configuration in providing finer control over the
                              behavior of the unit under certain error conditions.

Parameter Name

Description and Default Value

X00

Transport layer (or ICMP) error when sending a SIP request.

X20

SIP request times out while waiting for a response.

X40

General SIP protocol error (for example, unacceptable codec in SDP in 200 and ACK messages, or times out while waiting for
                                          ACK).

X60

Dialed number invalid according to given dial plan.

| Parameter Name | Description and Default Value |
|---|---|
| Provision Enable | Controls all resync actions independently of firmware upgrade actions. Set to Yes to enable remote provisioning. The default value is Yes. |
| Resync On Reset | Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades. The default value is Yes. |
| Resync Random Delay | A random delay following the boot-up sequence before performing the reset, specified in seconds. In a pool of IP Telephony
                                          devices that are scheduled to simultaneously power up, this introduces a spread in the times at which each unit sends a resync
                                          request to the provisioning server. This feature can be useful in a large residential deployment, in the case of a regional
                                          power failure. The value for this field must be an integer ranging between 0 and 65535. The default value is 2. |
| Resync At (HHmm) | The time (HHmm) that the device resynchronizes with the provisioning server. The value for this field must be a four-digit number ranging from 0000 to 2400 to indicate the time in HHmm format. For example,
                                          0959 indicates 09:59. The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value,
                                          the Resync Periodic parameter is ignored. |
| Resync At Random Delay | Prevents an overload of the provisioning server when a large number of devices power-on simultaneously. To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours
                                          and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay =
                                          (Resync At Random Delay + 30)/60 minutes, the input value in seconds is converted to minutes, rounding up to the next minute
                                          to calculate the final random_delay interval. The valid value ranges between 0 and 65535. This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes). |
| Resync Periodic | The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only
                                          after the first successful sync with the server. The valid formats are as follows: An integer Example: An input of 3000 indicates that the next resync occurs in 3000 seconds. Multiple integers Example: An input of 600,1200,300 indicates that the first resync occurs in 600 seconds, the second resync occurs in 1200 seconds after the first one, and
                                                the third resync occurs in 300 seconds after the second one. A time range Example, an input of 2400+30 indicates that the next resync occurs in between 2400 and 2430 seconds after a successful resync. Set this parameter to zero to disable periodic resynchronization. The default value is 3600 seconds. |
| Resync Error Retry Delay | If a resync operation fails because the IP Telephony device was unable to retrieve a profile from the server, or the downloaded
                                          file is corrupt, or an internal error occurs, the device tries to resync again after a time specified in seconds. The valid formats are as follows: An integer Example: An input of 300 indicates that the next retry for resync occurs in 300 seconds. Multiple integers Example: An input of 600,1200,300 indicates that the first retry occurs in 600 seconds after the failure, the second retry occurs in 1200 seconds after the
                                                failure of the first retry, and the third retry occurs in 300 seconds after the failure of the second retry. A time range Example, an input of 2400+30 indicates that the next retry occurs in between 2400 and 2430 seconds after a resync failure. If the delay is set to 0, the device does not try to resync again following a failed resync attempt. |
| Forced Resync Delay | Maximum delay (in seconds) the phone waits before performing a resynchronization. The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable
                                          to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in
                                          succession without interruption. The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of
                                          the counter. Resync events are delayed until this counter decrements to zero. The valid value ranges between 0 and 65535. The default value is 14,400 seconds. |
| Resync From SIP | Enables a resync to be triggered via a SIP NOTIFY message. The default value is Yes. |
| Resync After Upgrade Attempt | Enables or disables the resync operation after any upgrade occurs. If Yes is selected, sync is triggered. The default value is Yes. |
| Resync Trigger 1, Resync Trigger 2 | Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE. The default value is (empty). |
| Resync Fails On FNF | A resync is considered unsuccessful if a requested profile is not received from the server. This can be overridden by this
                                          parameter. When it is set to no , the device accepts a file-not-found response from the server as a successful resync. The default value is Yes. |
| Profile Rule Profile Rule B Profile Rule C Profile Rule D | Each profile rule informs the phone of a source from which to obtain a profile (configuration file). During every resync operation,
                                          the phone applies all the profiles in sequence. Default: /$PSN.xml If you are applying AES-256-CBC encryption to the configuration files, specify the encryption key with the --key keyword as follows: [--key <encryption key>] You can enclose the encryption key in double-quotes (") optionally. |
| DHCP Option To Use | DHCP options, delimited by commas, used to retrieve firmware and profiles. The default value is 66,160,159,150,60,43,125. |
| Log Request Msg | This parameter contains the message that is sent to the syslog server at the start of a resync attempt. The default value is $PN $MAC –Requesting % $SCHEME://$SERVIP:$PORT$PATH . |
| Log Success Msg | The syslog message that is issued upon successful completion of a resync attempt. The default value is $PN $MAC –Successful Resync % $SCHEME://$SERVIP:$PORT$PATH -- $ERR . |
| Log Failure Msg | The syslog message that is issued after a failed resync attempt. The default value is $PN $MAC -- Resync failed: $ERR . |
| User Configurable Resync | Allows a user to resync the phone from the IP phone screen. The default value is Yes. |

| Parameter Name | Description and Default Value |
|---|---|
| Upgrade Enable | Enables firmware upgrade operations independently of resync actions. The default value is Yes. |
| Upgrade Error Retry Delay | The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer
                                          that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next
                                          firmware upgrade attempt occurs when this timer counts down to zero. The default value is 3600 seconds. |
| Upgrade Rule | A firmware upgrade script that defines upgrade conditions and associated firmware URLs. It uses the same syntax as Profile
                                          Rule. Use the following format to enter the upgrade rule: <tftp\|http\|https>://<ip address>/image/<load name> For example: tftp://192.168.1.5/image/sip78xx.11-0-1MPP-BN.loads If no protocol is specified, TFTP is assumed. If no server-name is specified, the host that requests the URL is used as the
                                          server name. Isf no port is specified, the default port is used (69 for TFTP, 80 for HTTP, or 443 for HTTPS). The default value is blank. |
| Log Upgrade Request Msg | Syslog message issued at the start of a firmware upgrade attempt. Default: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH |
| Log Upgrade Success Msg | Syslog message issued after a firmware upgrade attempt completes successfully. The default value is $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR |
| Log Upgrade Failure Msg | Syslog message issued after a failed firmware upgrade attempt. The default value is $PN $MAC -- Upgrade failed: $ERR |
| Peer Firmware Sharing | Enables or disables the Peer Firmware Sharing feature. Select Yes or No to enable or to disable the feature. Default: Yes |
| Peer Firmware Sharing Log Server | Indicates the IP address and the port to which the UDP message is sent. For example: 10.98.76.123:514 where, 10.98.76.123 is the IP address and 514 is the port number. |

| Parameter Name | Description and Default Value |
|---|---|
| GPP A - GPP P | The general purpose parameters GPP_* are used as free string registers when configuring the phones to interact with a particular
                                          provisioning server solution. They can be configured to contain diverse values, including the following: Encryption keys. URLs. Multistage provisioning status information. Post request templates. Parameter name alias maps. Partial string values, eventually combined into complete parameter values. The default value is blank. |

| Parameter Name | Description and Default Value |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by the contents of the general purpose parameters GPP_A through GPP_P. |
| SA through SD | Replaced by special purpose parameters GPP_SA through GPP_SD. These parameters hold keys or passwords used in provisioning. Note $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. | Note | $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. |
| Note | $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. |
| MA | MAC address using lower case hex digits, for example, 000e08aabbcc. |
| MAU | MAC address using upper case hex digits, for example 000E08AABBCC. |
| MAC | MAC address using lower case hex digits, and colons to separate hex digit pairs. For example 00:0e:08:aa:bb:cc. |
| PN | Product Name. For example, CP-7832-3PCC. |
| PSN | Product Series Number. For example, V03. |
| SN | Serial Number string. for example 88012BA01234. |
| CCERT | SSL Client Certificate status: Installed or Not Installed. |
| IP | IP address of the phone within its local subnet. For example 192.168.1.100. |
| EXTIP | External IP of the phone, as seen on the Internet. For example 66.43.16.52. |
| SWVER | Software version string. For example, sip78xx.11-0-1MPP. |
| HWVER | Hardware version string. For example, 2.0.1 |
| PRVST | Provisioning State (a numeric string): -1 = explicit resync request 0 = power-up resync 1 = periodic resync 2 = resync failed, retry attempt |
| UPGST | Upgrade State (a numeric string): 1 = first upgrade attempt 2 = upgrade failed, retry attempt |
| UPGERR | Result message (ERR) of previous upgrade attempt; for example http_get failed. |
| PRVTMR | Seconds since last resync attempt. |
| UPGTMR | Seconds since last upgrade attempt. |
| REGTMR1 | Seconds since Line 1 lost registration with SIP server. |
| REGTMR2 | Seconds since Line 2 lost registration with SIP server. |
| UPGCOND | Legacy macro name. |
| SCHEME | File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL. |
| SERV | Request target server host name, as obtained after parsing resync or upgrade URL. |
| SERVIP | Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup. |
| PORT | Request target UDP/TCP port, as obtained after parsing resync or upgrade URL. |
| PATH | Request target file path, as obtained after parsing resync or upgrade URL. |
| ERR | Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the
                                          UPGERR variable in the case of upgrade attempts. |
| UIDn | The contents of the Line n UserID configuration parameter. |
| EMS | Extension Mobility Status |
| MUID | Extension Mobility User ID |
| MPWD | Extension Mobility Password |

| Note | $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. |
|---|---|

| Parameter Name | Description and Default Value |
|---|---|
| X00 | Transport layer (or ICMP) error when sending a SIP request. |
| X20 | SIP request times out while waiting for a response. |
| X40 | General SIP protocol error (for example, unacceptable codec in SDP in 200 and ACK messages, or times out while waiting for
                                          ACK). |
| X60 | Dialed number invalid according to given dial plan. |