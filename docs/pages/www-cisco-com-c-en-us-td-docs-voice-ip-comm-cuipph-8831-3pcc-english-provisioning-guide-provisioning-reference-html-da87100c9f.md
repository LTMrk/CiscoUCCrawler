---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-provisioning-guide-provisioning-reference-html-da87100c9f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/provisioning-guide/Provisioning/Reference.html
retrieved_at: 2026-08-21T02:10:21.341794+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Provisioning Guide, Release 9.3(3)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Provisioning Guide, Release 9.3(3)

Updated: October 9, 2014

Chapter: Provisioning Parameters

## Chapter: Provisioning Parameters

## Provisioning Parameters

This chapter describes the provisioning parameters that can be used in configuration profile scripts. It includes the following sections:

## Configuration Profile Parameters

The following table defines the function and usage of each parameter in the Configuration Profile Parameters section under the Provisioning tab.

Provision_Enable

Controls all resync actions independently of firmware upgrade actions. Set to Yes to enable remote provisioning.

The default value is Yes.

Resync_On_Reset

Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades.

The default value is Yes.

Resync_At

The hour and minutes (HHmm) that the device resynchronizes with the provisioning server.

The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value, the Resync_Periodic parameter is ignored.

Resync_At_Random_Delay

Prevents an overload of the provisioning server when a large number of devices power-on simultaneously.

To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay = (Resync_At_Random_Delay + 30)/60 minutes.

The input value in seconds is converted to minutes, rounding up to the next minute to calculate the final random_delay interval.

This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes). If the parameter value is set to less than 600, the default value is used.

Resync_Periodic

The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only after the first successful sync with the server.

Set this parameter to zero to disable periodic resynchronization.

The default value is 3600 seconds.

Forced_Resync_Delay

Maximum delay (in seconds) the IP Telephony deviceATA waits before performing a resynchronization.

The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in succession without interruption.

The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of the counter. Resync events are delayed until this counter decrements to zero.

The default value is 14,400 seconds.

Resync_From_SIP

Enables a resync to be triggered via a SIP NOTIFY message.

The default value is Yes.

Resync_After_Upgrade_Attempt

Triggers a resync after every firmware upgrade attempt.

The default value is Yes.

Resync_Trigger_1, Resync_Trigger_2

Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE.

The default value is (empty).

Log_Request_Msg

This parameter contains the message that is sent to the syslog server at the start of a resync attempt.

The default value is $PN $MAC – Requesting resync $SCHEME://$SERVIP:$PORT$PATH.

Log_Success_Msg

The syslog message that is issued upon successful completion of a resync attempt.

The default value is $PN $MAC – Successful resync $SCHEME://$SERVIP:$PORT$PATH -- $ERR.

Log_Failure_Msg

The syslog message that is issued after a failed resync attempt.

The default value is $PN $MAC – Resync failed: $ERR.

## Firmware Upgrade Parameters

The following table defines the function and usage of each parameter in the Firmware Upgrade section of the Provisioning tab.

Upgrade_Enable

Enables firmware upgrade operations independently of resync actions.

The default value is Yes.

Upgrade_Error_Retry_Delay

The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next firmware upgrade attempt occurs when this timer counts down to zero.

The default value is 3600 seconds.

Upgrade_Rule

This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated firmware URLs.

The default value is (empty).

Log_Request_Msg

The syslog message that is issued at the start of a firmware upgrade attempt.

The default value is $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH.

Log_Success_Msg

The syslog message that is issued after a firmware upgrade attempt completes successfully.

The default value is $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR.

Log_Failure_Msg

The syslog message that is issued after a failed firmware upgrade attempt.

The default value is $PN $MAC -- Upgrade failed: $ERR.

## General Purpose Parameters

The following table defines the function and usage of each parameter in the General Purpose Parameters section of the Provisioning tab.

GPP_SA, GPP_SB, GPP_SC, GPP_SD

Special purpose provisioning parameters, designed to hold encryption keys and passwords. To ensure the integrity of the encryption mechanism, these parameters must be kept secret. Therefore these parameters are not displayed on the device configuration web page, and they are not included in the configuration report sent in response to a SIP NOTIFY command.

Note that these parameters are not available on the SPA500 Series phones.

The default value is (empty).

GPP_A through GPP_P

General purpose provisioning parameters. These parameters can be used as variables in provisioning and upgrade rules. They are referenced by prepending the variable name with a ‘$’ character, such as $GPP_A.

The default value is (empty).

## Macro Expansion Variables

Certain macro variables are recognized within the following provisioning parameters:

- Profile_Rule

- Profile_Rule_*

- Resync_Trigger_*

- Upgrade_Rule

- Log_*

- GPP_* (under specific conditions)

Within these parameters, syntax types, such as $NAME or $(NAME), are recognized and expanded.

Macro variable substrings can be specified with the notation $(NAME:p) and $(NAME:p:q), where p and q are non-negative integers (available in revision 2.0.11 and above). The resulting macro expansion is the substring starting at character offset p, with length q (or else till end-of-string if q is not specified). For example, if GPP_A contains ABCDEF, then $(A:2) expands to CDEF, and $(A:2:3) expands to CDE.

An unrecognized name is not translated, and the $NAME or $(NAME) form remains unchanged in the parameter value after expansion.

$

The form $$ expands to a single $ character.

A through P

Replaced by the contents of the general purpose parameters GPP_A through GPP_P.

MA

MAC address using lower case hex digits, for example, 000e08aabbcc.

MAU

MAC address using upper case hex digits, for example 000E08AABBCC.

MAC

MAC address using lower case hex digits, and colons to separate hex digit pairs, for example 00:0e:08:aa:bb:cc.

PN

Product Name, for example CP-8831-3PCC.

PSN

Product Series Number, for example 514.

SN

Serial Number string, for example 88012BA01234.

CCERT

SSL Client Certificate status: Installed or Not Installed.

IP

IP address of the IP Telephony device within its local subnet, for example 192.168.1.100.

EXTIP

External IP of the IP Telephony device, as seen on the Internet, for example 66.43.16.52.

SWVER

Software version string, for example 7.5.1(a).

HWVER

Hardware version string, for example 2.0.1

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

Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts.

ISCUST

Value=1 if unit is customized, 0 otherwise; customization status viewable on WebUI Info page.

SA through SD

Replaced by the contents of the parameters GPP_SA through GPP_SD, which are for secure key string.

## Internal Error Codes

The IP Telephony device defines a number of internal error codes (X00–X99) to facilitate configuration in providing finer control over the behavior of the unit under certain error conditions.

X00

Transport layer (or ICMP) error when sending a SIP request.

X20

SIP request times out while waiting for a response.

X40

General SIP protocol error (for example, unacceptable codec in SDP in 200 and ACK messages, or times out while waiting for ACK).

X60

Dialed number invalid according to given dial plan.

| Parameter Name | Description and Default Value |
|---|---|
| Provision_Enable | Controls all resync actions independently of firmware upgrade actions. Set to Yes to enable remote provisioning. The default value is Yes. |
| Resync_On_Reset | Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades. The default value is Yes. |
| Resync_At | The hour and minutes (HHmm) that the device resynchronizes with the provisioning server. The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value, the Resync_Periodic parameter is ignored. |
| Resync_At_Random_Delay | Prevents an overload of the provisioning server when a large number of devices power-on simultaneously. To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay = (Resync_At_Random_Delay + 30)/60 minutes. The input value in seconds is converted to minutes, rounding up to the next minute to calculate the final random_delay interval. This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes). If the parameter value is set to less than 600, the default value is used. |
| Resync_Periodic | The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only after the first successful sync with the server. Set this parameter to zero to disable periodic resynchronization. The default value is 3600 seconds. |
| Forced_Resync_Delay | Maximum delay (in seconds) the IP Telephony deviceATA waits before performing a resynchronization. The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in succession without interruption. The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of the counter. Resync events are delayed until this counter decrements to zero. The default value is 14,400 seconds. |
| Resync_From_SIP | Enables a resync to be triggered via a SIP NOTIFY message. The default value is Yes. |
| Resync_After_Upgrade_Attempt | Triggers a resync after every firmware upgrade attempt. The default value is Yes. |
| Resync_Trigger_1, Resync_Trigger_2 | Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE. The default value is (empty). |
| Log_Request_Msg | This parameter contains the message that is sent to the syslog server at the start of a resync attempt. The default value is $PN $MAC – Requesting resync $SCHEME://$SERVIP:$PORT$PATH. |
| Log_Success_Msg | The syslog message that is issued upon successful completion of a resync attempt. The default value is $PN $MAC – Successful resync $SCHEME://$SERVIP:$PORT$PATH -- $ERR. |
| Log_Failure_Msg | The syslog message that is issued after a failed resync attempt. The default value is $PN $MAC – Resync failed: $ERR. |

| Parameter Name | Description and Default Value |
|---|---|
| Upgrade_Enable | Enables firmware upgrade operations independently of resync actions. The default value is Yes. |
| Upgrade_Error_Retry_Delay | The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next firmware upgrade attempt occurs when this timer counts down to zero. The default value is 3600 seconds. |
| Upgrade_Rule | This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated firmware URLs. The default value is (empty). |
| Log_Request_Msg | The syslog message that is issued at the start of a firmware upgrade attempt. The default value is $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH. |
| Log_Success_Msg | The syslog message that is issued after a firmware upgrade attempt completes successfully. The default value is $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR. |
| Log_Failure_Msg | The syslog message that is issued after a failed firmware upgrade attempt. The default value is $PN $MAC -- Upgrade failed: $ERR. |

| Parameter Name | Description and Default Value |
|---|---|
| GPP_SA, GPP_SB, GPP_SC, GPP_SD | Special purpose provisioning parameters, designed to hold encryption keys and passwords. To ensure the integrity of the encryption mechanism, these parameters must be kept secret. Therefore these parameters are not displayed on the device configuration web page, and they are not included in the configuration report sent in response to a SIP NOTIFY command. Note that these parameters are not available on the SPA500 Series phones. The default value is (empty). |
| GPP_A through GPP_P | General purpose provisioning parameters. These parameters can be used as variables in provisioning and upgrade rules. They are referenced by prepending the variable name with a ‘$’ character, such as $GPP_A. The default value is (empty). |

| Parameter Name | Description and Default Value |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by the contents of the general purpose parameters GPP_A through GPP_P. |
| MA | MAC address using lower case hex digits, for example, 000e08aabbcc. |
| MAU | MAC address using upper case hex digits, for example 000E08AABBCC. |
| MAC | MAC address using lower case hex digits, and colons to separate hex digit pairs, for example 00:0e:08:aa:bb:cc. |
| PN | Product Name, for example CP-8831-3PCC. |
| PSN | Product Series Number, for example 514. |
| SN | Serial Number string, for example 88012BA01234. |
| CCERT | SSL Client Certificate status: Installed or Not Installed. |
| IP | IP address of the IP Telephony device within its local subnet, for example 192.168.1.100. |
| EXTIP | External IP of the IP Telephony device, as seen on the Internet, for example 66.43.16.52. |
| SWVER | Software version string, for example 7.5.1(a). |
| HWVER | Hardware version string, for example 2.0.1 |
| SCHEME | File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL. |
| SERV | Request target server host name, as obtained after parsing resync or upgrade URL. |
| SERVIP | Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup. |
| PORT | Request target UDP/TCP port, as obtained after parsing resync or upgrade URL. |
| PATH | Request target file path, as obtained after parsing resync or upgrade URL. |
| ERR | Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts. |
| ISCUST | Value=1 if unit is customized, 0 otherwise; customization status viewable on WebUI Info page. |
| SA through SD | Replaced by the contents of the parameters GPP_SA through GPP_SD, which are for secure key string. |

| Parameter Name | Description and Default Value |
|---|---|
| X00 | Transport layer (or ICMP) error when sending a SIP request. |
| X20 | SIP request times out while waiting for a response. |
| X40 | General SIP protocol error (for example, unacceptable codec in SDP in 200 and ACK messages, or times out while waiting for ACK). |
| X60 | Dialed number invalid according to given dial plan. |