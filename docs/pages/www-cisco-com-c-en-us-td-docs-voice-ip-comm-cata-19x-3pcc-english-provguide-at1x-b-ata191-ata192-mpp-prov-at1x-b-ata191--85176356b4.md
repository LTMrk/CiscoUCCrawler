---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-provguide-at1x-b-ata191-ata192-mpp-prov-at1x-b-ata191--85176356b4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/provguide/at1x_b_ata191-ata192-mpp-prov/at1x_b_ata191-ata192-mpp-prov_chapter_0100.html
retrieved_at: 2026-08-22T01:05:22.351538+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Provisioning Parameters

## Chapter: Provisioning Parameters

# Provisioning Parameters

## Configuration Parameters Overview

This chapter describes the provisioning parameters that can be used in configuration profile scripts.

## Configuration Profile Parameters

The following table defines the function and usage of each parameter in the Configuration Profile Parameters section under
                              the Provisioning tab.

Parameter Name

Description and Default Value

Provision_Enable

Controls all resync actions independently of firmware upgrade actions. Set to yes to enable remote provisioning.

The default value is Yes.

Resync_On_Reset

Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades.

The default value is Yes.

Resync_Random_Delay

Prevents an overload of the provisioning server when a large number of devices power-on simultaneously and attempt initial
                                          configuration. This delay is effective only on the initial configuration attempt, following a device power-on or reset.

The parameter is the maximum time interval that the device waits before making contact with the provisioning server. The actual
                                          delay is a pseudo-random number between zero and this value.

This parameter is in units of 20 seconds; the default value of 3 represents 60 seconds. This feature is disabled when this
                                          parameter is set to zero.

The default value is 2 (40 seconds).

Resync At

The hour and minutes (HHmm) that the device resyncs with the provisioning server.

The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value,
                                          the Resync_Periodic parameter is ignored.

Resync_At_Random_Delay

Prevents an overload of the provisioning server when a large number of devices power-on simultaneously.

To avoid flooding resync requests to the server from multiple phones, the phone resyncs in the range between the hours and
                                          minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay = (Resync_At_Random_Delay
                                          + 30)/60 minutes.

The input value in seconds is converted to minutes, rounding up to the next minute to calculate the final random_delay interval.

This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes). If the parameter
                                          value is set to less than 600, the default value is used.

Resync_Periodic

The time interval between periodic resyncs with the provisioning server. The associated resync timer is active only after
                                          the first successful sync with the server.

Set this parameter to zero to disable periodic resyncing.

The default value is 3600 seconds.

Resync_Error_Retry_Delay

Resync retry interval (in seconds) applied in case of resync failure.

The device has an error retry timer that activates if the previous attempt to sync with the provisioning server fails. The
                                          device waits to contact the server again until the timer counts down to zero.

This parameter is the value that is initially loaded into the error retry timer. If this parameter is set to zero, the device
                                          does not try to resync with the provisioning server following a failed attempt.

The default value is 3600 seconds.

Forced_Resync_Delay

Maximum delay (in seconds) the ATA waits before performing a resync. The device does not resync while one of its phone lines
                                          is active. Because a resync can take several seconds, it is desirable to wait until the device has been idle for an extended
                                          period before resyncing. This allows a user to make calls in succession without interruption.

The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of
                                          the counter. Resync events are delayed until this counter decrements to zero.

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

Resync_Fails_On_FNF

Determines whether a file-not-found response from the provisioning server constitutes a successful or a failed resync.

A failed resync activates the error resync timer.

The default value is Yes.

HTTPS_Name_Validate

Determines whether to check the Subject Alternative Name (SAN)  for the HTTPS provisioning. Set to yes to enable the SAN check.

The default value is Yes.

Profile_Rule

This parameter is a profile script that evaluates to the provisioning resync command. The command specifies the protocol (TFTP,
                                          HTTP, or HTTPS) and an associated URL.

If the command is not specified, TFTP is assumed, and the address of the TFTP server is obtained through DHCP option 66.

In the URL, either the IP address or the FQDN of the server can be specified. The file name can have macros, such as $MA,
                                          which expands to the device MAC address.

The default value is /ata$PSN.cfg.

Profile_Rule_B, Profile_Rule_C, Profile_Rule_D

Defines second, third, and fourth resync commands and associated profile URLs.

These profile scripts are executed sequentially after the primary Profile Rule resync operation has completed. If a resync
                                          is triggered and Profile Rule is blank, Profile Rule B, C, and D are still evaluated and executed.

The default value is (empty).

Log_Resync_Request_Msg

This parameter contains the message that is sent to the syslog server at the start of a resync attempt.

The default value is $PN $MAC –Requesting resync $SCHEME://$SERVIP:$PORT$PATH.

Log_Resync_Success_Msg

The syslog message that is issued upon successful completion of a resync attempt.

The default value is $PN $MAC –Successful resync $SCHEME://$SERVIP:$PORT$PATH -- $ERR.

Log_Resync_Failure_Msg

The syslog message that is issued after a failed resync attempt.

The default value is $PN $MAC – Resyncfailed: $ERR.

Report_Rule

The target URL to which configuration reports are sent. This parameter has the same syntax as the Profile_Rule parameter,
                                          and resolves to a TCP/IP command with an associated URL.

A configuration report is generated in response to an authenticated SIP NOTIFY message, with Event: report. The report is
                                          an XML file containing the name and value of all the device parameters.

This parameter may optionally contain an encryption key.

For example: [ --key $K ] tftp://ps.callhome.net/$MA/rep.xml.enc

## Firmware Upgrade Parameters

The following table defines the function and usage of each parameter in the Firmware Upgrade section of the Provisioning tab.

Parameter Name

Description and Default Value

Upgrade_Enable

Enables firmware upgrade operations independently of resync actions.

The default value is Yes.

Upgrade_Error_Retry_Delay

The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer
                                          that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next
                                          firmware upgrade attempt occurs when this timer counts down to zero.

The default value is 3600 seconds.

Downgrade_Rev_Limit

Enforces a lower limit on the acceptable version number during a firmware upgrade or downgrade. The device does not complete
                                          a firmware upgrade operation unless the firmware version is greater than or equal to this parameter.

The default value is (empty).

Upgrade_Rule

This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated
                                          firmware URLs.

The default value is (empty).

Log_Upgrade_Request_Msg

The syslog message that is issued at the start of a firmware upgrade attempt.

The default value is $PN $MAC – Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH.

Log_Upgrade_Success_Msg

The syslog message that is issued after a firmware upgrade attempt completes successfully.

The default value is $PN $MAC – Successful upgrade $SCHEME://$SERVIP:$PORT$PATH --$ERR.

Log_Upgrade_Failure_Msg

The syslog message that is issued after a failed firmware upgrade attempt.

The default value is $PN $MAC – Upgrade failed: $ERR.

## General Purpose Parameters

The following table defines the function and usage of each parameter in the General Purpose Parameters section of the Provisioning
                              tab.

Parameter Name

Description and Default Value

GPP_SA, GPP_SB, GPP_SC, GPP_SD

Special purpose provisioning parameters, designed to hold encryption keys and passwords. To ensure the integrity of the encryption
                                          mechanism, these parameters must be kept secret. Therefore these parameters are not displayed on the device configuration
                                          web page, and they are not included in the configuration report sent in response to a SIP NOTIFY command.

The default value is (empty).

GPP_A through GPP_P

General purpose provisioning parameters.

These parameters can be used as variables in provisioning and upgrade rules. They are referenced by prepending the variable
                                          name with a ‘$’ character, such as $A for GPP_A.

The default value is (empty).

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

Replaced by special purpose parameters GPP_SA through GPP_SD. These parameters hold keys or passwords used in provisioning.

$SA through $SD are recognized as arguments to the optional resync URL qualifier, --key.

MA

MAC address using lower case hex digits, for example, 000e08aabbcc.

MAU

MAC address using upper case hex digits, for example 000E08AABBCC.

MAC

MAC address using lower case hex digits, and colons to separate hex digit pairs. For example 00:0e:08:aa:bb:cc.

PN

Product name. For example, ATA191-MPP.

PSN

Product Series Number. For example, 191

SN

Serial Number string. for example 88012BA01234.

CCERT

SSL Client Certificate status: Installed or Not Installed.

IP

IP address of the phone within its local subnet. For example 192.168.1.100.

EXTIP

External IP of the phone, as seen on the Internet. For example 66.43.16.52.

SWVER

Software version string. For example,

Software version string. For example, 11-1-0MPP-19

HWVER

Hardware version string. For example, 4

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

ORIGTYPE

AUTHSTATUS

Controls whether the phone needs to request for a license.

```
ORIGTYPE
```

```
AUTHSTATUS
```

profile rule or upgrade rule macro expansion and conditional expression

transition authorization rule macro expansion

## Internal Error Codes

The ATA defines a number of internal error codes (X00–X99) to facilitate configuration in providing finer control over the
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
| Provision_Enable | Controls all resync actions independently of firmware upgrade actions. Set to yes to enable remote provisioning. The default value is Yes. |
| Resync_On_Reset | Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades. The default value is Yes. |
| Resync_Random_Delay | Prevents an overload of the provisioning server when a large number of devices power-on simultaneously and attempt initial
                                          configuration. This delay is effective only on the initial configuration attempt, following a device power-on or reset. The parameter is the maximum time interval that the device waits before making contact with the provisioning server. The actual
                                          delay is a pseudo-random number between zero and this value. This parameter is in units of 20 seconds; the default value of 3 represents 60 seconds. This feature is disabled when this
                                          parameter is set to zero. The default value is 2 (40 seconds). |
| Resync At | The hour and minutes (HHmm) that the device resyncs with the provisioning server. The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value,
                                          the Resync_Periodic parameter is ignored. |
| Resync_At_Random_Delay | Prevents an overload of the provisioning server when a large number of devices power-on simultaneously. To avoid flooding resync requests to the server from multiple phones, the phone resyncs in the range between the hours and
                                          minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay = (Resync_At_Random_Delay
                                          + 30)/60 minutes. The input value in seconds is converted to minutes, rounding up to the next minute to calculate the final random_delay interval. This feature is disabled when this parameter is set to zero. The default value is 600 seconds (10 minutes). If the parameter
                                          value is set to less than 600, the default value is used. |
| Resync_Periodic | The time interval between periodic resyncs with the provisioning server. The associated resync timer is active only after
                                          the first successful sync with the server. Set this parameter to zero to disable periodic resyncing. The default value is 3600 seconds. |
| Resync_Error_Retry_Delay | Resync retry interval (in seconds) applied in case of resync failure. The device has an error retry timer that activates if the previous attempt to sync with the provisioning server fails. The
                                          device waits to contact the server again until the timer counts down to zero. This parameter is the value that is initially loaded into the error retry timer. If this parameter is set to zero, the device
                                          does not try to resync with the provisioning server following a failed attempt. The default value is 3600 seconds. |
| Forced_Resync_Delay | Maximum delay (in seconds) the ATA waits before performing a resync. The device does not resync while one of its phone lines
                                          is active. Because a resync can take several seconds, it is desirable to wait until the device has been idle for an extended
                                          period before resyncing. This allows a user to make calls in succession without interruption. The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of
                                          the counter. Resync events are delayed until this counter decrements to zero. The default value is 14,400 seconds. |
| Resync_From_SIP | Enables a resync to be triggered via a SIP NOTIFY message. The default value is Yes. |
| Resync_After_Upgrade_Attempt | Triggers a resync after every firmware upgrade attempt. The default value is Yes. |
| Resync_Trigger_1, Resync_Trigger_2 | Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE. The default value is (empty). |
| Resync_Fails_On_FNF | Determines whether a file-not-found response from the provisioning server constitutes a successful or a failed resync. A failed resync activates the error resync timer. The default value is Yes. |
| HTTPS_Name_Validate | Determines whether to check the Subject Alternative Name (SAN)  for the HTTPS provisioning. Set to yes to enable the SAN check. The default value is Yes. |
| Profile_Rule | This parameter is a profile script that evaluates to the provisioning resync command. The command specifies the protocol (TFTP,
                                          HTTP, or HTTPS) and an associated URL. If the command is not specified, TFTP is assumed, and the address of the TFTP server is obtained through DHCP option 66. In the URL, either the IP address or the FQDN of the server can be specified. The file name can have macros, such as $MA,
                                          which expands to the device MAC address. The default value is /ata$PSN.cfg. |
| Profile_Rule_B, Profile_Rule_C, Profile_Rule_D | Defines second, third, and fourth resync commands and associated profile URLs. These profile scripts are executed sequentially after the primary Profile Rule resync operation has completed. If a resync
                                          is triggered and Profile Rule is blank, Profile Rule B, C, and D are still evaluated and executed. The default value is (empty). |
| Log_Resync_Request_Msg | This parameter contains the message that is sent to the syslog server at the start of a resync attempt. The default value is $PN $MAC –Requesting resync $SCHEME://$SERVIP:$PORT$PATH. |
| Log_Resync_Success_Msg | The syslog message that is issued upon successful completion of a resync attempt. The default value is $PN $MAC –Successful resync $SCHEME://$SERVIP:$PORT$PATH -- $ERR. |
| Log_Resync_Failure_Msg | The syslog message that is issued after a failed resync attempt. The default value is $PN $MAC – Resyncfailed: $ERR. |
| Report_Rule | The target URL to which configuration reports are sent. This parameter has the same syntax as the Profile_Rule parameter,
                                          and resolves to a TCP/IP command with an associated URL. A configuration report is generated in response to an authenticated SIP NOTIFY message, with Event: report. The report is
                                          an XML file containing the name and value of all the device parameters. This parameter may optionally contain an encryption key. For example: [ --key $K ] tftp://ps.callhome.net/$MA/rep.xml.enc |

| Parameter Name | Description and Default Value |
|---|---|
| Upgrade_Enable | Enables firmware upgrade operations independently of resync actions. The default value is Yes. |
| Upgrade_Error_Retry_Delay | The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer
                                          that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next
                                          firmware upgrade attempt occurs when this timer counts down to zero. The default value is 3600 seconds. |
| Downgrade_Rev_Limit | Enforces a lower limit on the acceptable version number during a firmware upgrade or downgrade. The device does not complete
                                          a firmware upgrade operation unless the firmware version is greater than or equal to this parameter. The default value is (empty). |
| Upgrade_Rule | This parameter is a firmware upgrade script with the same syntax as Profile_Rule. Defines upgrade conditions and associated
                                          firmware URLs. The default value is (empty). |
| Log_Upgrade_Request_Msg | The syslog message that is issued at the start of a firmware upgrade attempt. The default value is $PN $MAC – Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH. |
| Log_Upgrade_Success_Msg | The syslog message that is issued after a firmware upgrade attempt completes successfully. The default value is $PN $MAC – Successful upgrade $SCHEME://$SERVIP:$PORT$PATH --$ERR. |
| Log_Upgrade_Failure_Msg | The syslog message that is issued after a failed firmware upgrade attempt. The default value is $PN $MAC – Upgrade failed: $ERR. |

| Parameter Name | Description and Default Value |
|---|---|
| GPP_SA, GPP_SB, GPP_SC, GPP_SD | Special purpose provisioning parameters, designed to hold encryption keys and passwords. To ensure the integrity of the encryption
                                          mechanism, these parameters must be kept secret. Therefore these parameters are not displayed on the device configuration
                                          web page, and they are not included in the configuration report sent in response to a SIP NOTIFY command. The default value is (empty). |
| GPP_A through GPP_P | General purpose provisioning parameters. These parameters can be used as variables in provisioning and upgrade rules. They are referenced by prepending the variable
                                          name with a ‘$’ character, such as $A for GPP_A. The default value is (empty). |

| Parameter Name | Description and Default Value |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by the contents of the general purpose parameters GPP_A through GPP_P. |
| SA through SD | Replaced by special purpose parameters GPP_SA through GPP_SD. These parameters hold keys or passwords used in provisioning. Note $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. | Note | $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. |
| Note | $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. |
| MA | MAC address using lower case hex digits, for example, 000e08aabbcc. |
| MAU | MAC address using upper case hex digits, for example 000E08AABBCC. |
| MAC | MAC address using lower case hex digits, and colons to separate hex digit pairs. For example 00:0e:08:aa:bb:cc. |
| PN | Product name. For example, ATA191-MPP. |
| PSN | Product Series Number. For example, 191 |
| SN | Serial Number string. for example 88012BA01234. |
| CCERT | SSL Client Certificate status: Installed or Not Installed. |
| IP | IP address of the phone within its local subnet. For example 192.168.1.100. |
| EXTIP | External IP of the phone, as seen on the Internet. For example 66.43.16.52. |
| SWVER | Software version string. For example, Software version string. For example, 11-1-0MPP-19 |
| HWVER | Hardware version string. For example, 4 |
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
| ORIGTYPE AUTHSTATUS | Controls whether the phone needs to request for a license. Values for ORIGTYPE are: orig_ent, orig_mpp, none Values for AUTHSTATUS are: classic, wxc, none Add the variables in: profile rule or upgrade rule macro expansion and conditional expression transition authorization rule macro expansion |

| Note | $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. |
|---|---|

| Parameter Name | Description and Default Value |
|---|---|
| X00 | Transport layer (or ICMP) error when sending a SIP request. |
| X20 | SIP request times out while waiting for a response. |
| X40 | General SIP protocol error (for example, unacceptable codec in SDP in 200 and ACK messages, or times out while waiting for
                                          ACK). |
| X60 | Dialed number invalid according to given dial plan. |