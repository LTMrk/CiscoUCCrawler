---
doc_id: help-webex-com-en-us-article-nsxxojf-5b7e89786f
source_url: https://help.webex.com/en-us/article/nsxxojf
retrieved_at: 2026-11-02T13:07:00.634377+00:00
---

## Provisioning parameter types

This section describes the provisioning parameters broadly organized according to function.

### General purpose parameters

The general-purpose parameters GPP_* ( Admin Login > advanced > Voice > Provisioning ) are used as free string registers when configuring the phone to interact with a particular provisioning server solution. The GPP_* parameters are empty by default. They can be configured to contain diverse values, including the following:

Encryption keys

URLs

Multistage provisioning status information.

Post request templates

Parameter name alias maps

Partial string values, eventually combined into complete parameter values.

The GPP_* parameters are available for macro expansion within other provisioning parameters. For this purpose, single-letter uppercase macro names (A through P) suffice to identify the contents of GPP_A through GPP_P. Also, the two-letter uppercase macro names SA through SD identify GPP_SA through GPP_SD as a special case when used as arguments of the following URL options:

key , uid , and pwd

These parameters can be used as variables in provisioning and upgrade rules. They are referenced by prefixing the variable name with a ‘$’ character, such as $GPP_A.

### Enable parameters

The Provision_Enable and Upgrade_Enable parameters control all profile resync and firmware upgrade operations. These parameters control resyncs and upgrades independently of each other. These parameters also control resync and upgrade URL commands that are issued through the administration web server. Both of these parameters are set to Yes by default.

The Resync_From_SIP parameter controls requests for resync operations. A SIP NOTIFY event is sent from the service provider proxy server to the phone. If enabled, the proxy can request a resync. To do so, the proxy sends a SIP NOTIFY message that contains the Event: resync header to the device.

The device challenges the request with a 401 response (authorization refused for used credentials). The device expects an authenticated subsequent request before it honors the resync request from the proxy. The Event: reboot_now and Event: restart_now headers perform cold and warm restarts, respectively, which are also challenged.

The two remaining enables are Resync_On_Reset and Resync_After_Upgrade_Attempt. These parameters determine whether the device performs a resync operation after power-up software reboots and after each upgrade attempt.

When Resync_On_Reset is enabled, the device introduces a random delay that follows the boot-up sequence before the reset is performed. The delay is a random time up to the value that the Resync_Random_Delay (in seconds) specifies. In a pool of phones that power up simultaneously, this delay spreads out the start times of the resync requests from each unit. This feature can be useful in a large residential deployment, in the case of a regional power failure.

### Triggers

The phone allows you to resync at specific intervals or at a specific time.

#### Resync at specific intervals

The phone is designed to resync with the provisioning server periodically. The resync interval is configured in Resync_Periodic (seconds). If this value is left empty, the device does not resync periodically.

The resync typically takes place when the voice lines are idle. If a voice line is active when a resync is due, the phone delays the resync procedure until the line becomes idle again. A resync can cause configuration parameter values to change.

A resync operation can fail because the phone is unable to retrieve a profile from the server, the downloaded file is corrupt, or an internal error occurred. The device tries to resync again after a time that is specified in Resync_Error_Retry_Delay (seconds). If Resync_Error_Retry_Delay is set to 0, the device does not try to resync again after a failed resync attempt.

If an upgrade fails, a retry is performed after Upgrade_Error_Retry_Delay seconds.

Two configurable parameters are available to conditionally trigger a resync: Resync_Trigger_1 and Resync_Trigger_2. Each parameter can be programmed with a conditional expression that undergoes macro expansion. When the resync interval expires (time for the next resync) the triggers, if set, will prevent resync unless one or more triggers evaluates to true.

The following example condition triggers a resync. In the example, the last phone upgrade attempt has elapsed more than 5 minutes (300 seconds), and at least 10 minutes (600 seconds) have elapsed since the last resync attempt.

```
$UPGTMR gt 300 and $PRVTMR ge 600
```

#### Resync at a specific time

The Resync_At parameter allows the phone to resync at a specific time. This parameter uses the 24-hour format (hhmm) to specify the time.

The Resync_At_Random_Delay parameter allows the phone to resync at an unspecified delay in time. This parameter uses a positive integer format to specify the time.

Flooding the server with resync requests from multiple phones that are set to resync at the same time should be avoided. To do so, the phone triggers the resync up to 10 minutes after the specified time.

For example, if you set the resync time to 1000 (10 a.m.), the phone triggers the resync anytime between 10:00 a.m. and 10:10 a.m.

By default, this feature is disabled. If the Resync_At parameter is provisioned, the Resync_Periodic parameter is ignored.

### Configurable schedules

You can configure schedules for periodic resyncs, and you can specify the retry intervals for resync and upgrade failures by using these provisioning parameters:

Resync_Periodic

Resync_Error_Retry_Delay

Upgrade_Error_Retry_Delay

Each parameter accepts a single delay value (seconds). The new extended syntax allows for a comma-separated list of consecutive delay elements. The last element in the sequence is implicitly repeated forever.

Optionally, you can use a plus sign to specify another numeric value that appends a random extra delay.

#### Example 1

In this example, the phone periodically resyncs every 2 hours. If a resync failure occurs, the device retries at these intervals: 30 minutes, 1 hour, 2 hours, 4 hours. The device continues to try at 4-hour intervals until it resyncs successfully.

```
Resync_Periodic=7200
Resync_Error_Retry_Delay=1800,3600,7200,14400
```

#### Example 2

In this example, the device periodically resyncs every hour (plus an extra random delay of up to 10 minutes). In the case of a resync failure, the device retries at these intervals: 30 minutes (plus up to 5 minutes). 1 hour (plus up to 10 minutes), 2 hours (plus up to 15 minutes). The device continues to try at 2-hour intervals (plus up to 15 minutes) until it successfully resyncs.

```
Resync_Periodic=3600+600
Resync_Error_Retry_Delay=1800+300,3600+600,7200+900
```

#### Example 3

In this example, if a remote upgrade attempt fails, the device retries the upgrade in 30 minutes, then again after one more hour, then in two hours. If the upgrade still fails, the device retries every four to five hours until the upgrade succeeds.

```
Upgrade_Error_Retry_Delay  =  1800,3600,7200,14400+3600
```

### Profile rules

The phone provides multiple remote configuration profile parameters (Profile_Rule*). Thus, each resync operation can retrieve multiple files that different servers manage.

In the simplest scenario, the device resyncs periodically to a single profile on a central server, which updates all pertinent internal parameters. Alternatively, the profile can be split between different files. One file is common for all the phones in a deployment. A separate, unique file is provided for each account. Encryption keys and certificate information can be supplied by still another profile, stored on a separate server.

Whenever a resync operation is due, the phone evaluates the four Profile_Rule* parameters in sequence:

Profile_Rule

Profile_Rule_B

Profile_Rule_C

Profile_Rule_D

Each evaluation can result in a profile retrieval from a remote provisioning server, with a possible update of some number of internal parameters. If an evaluation fails, the resync sequence is interrupted, and is retried again from the beginning specified by the Resync_Error_Retry_Delay parameter (seconds). If all evaluations succeed, the device waits for the second specified by the Resync_Periodic parameter and then performs another resync.

The contents of each Profile_Rule* parameter consist of a set of alternatives. The alternatives are separated by the | (pipe) character. Each alternative consists of a conditional expression, an assignment expression, a profile URL, and any associated URL options. All these components are optional within each alternative. The following are the valid combinations, and the order in which they must appear, if present:

```
[ conditional-expr ] [ assignment-expr ] [[ options ] URL ]
```

Within each Profile_Rule* parameter, all alternatives except the last one must provide a conditional expression. This expression is evaluated and is processed as follows:

Conditions are evaluated from left to right, until one is found that evaluates as true (or until one alternative is found with no conditional expression).

Any accompanying assignment expression is evaluated, if present.

If a URL is specified as part of that alternative, an attempt is made to download the profile that is located at the specified URL. The system attempts to update the internal parameters accordingly.

If all alternatives have conditional expressions and none evaluates to true (or if the whole profile rule is empty), the entire Profile_Rule* parameter is skipped. The next profile rule parameter in the sequence is evaluated.

#### Example 1

This example resyncs unconditionally to the profile at the specified URL, and performs an HTTP GET request to the remote provisioning server:

```
http://remote.server.com/cisco/$MA.cfg
```

#### Example 2

In this example, the device resyncs to two different URLs, depending on the registration state of Line 1. In case of lost registration, the device performs an HTTP POST to a CGI script. The device sends the contents of the macro expanded GPP_A, which may provide additional information on the device state:

```
($PRVTMR ge 600)? http://p.tel.com/has-reg.cfg
| [--post a] http://p.tel.com/lost-reg?
```

#### Example 3

In this example, the device resyncs to the same server. The device provides additional information if a certificate is not installed in the unit (for legacy pre-2.0 units):

```
(“$CCERT” eq “Installed”)? https://p.tel.com/config?
| https://p.tel.com/config?cisco$MAU
```

#### Example 4

In this example, Line 1 is disabled until GPP_A is set equal to Provisioned through the first URL. Afterwards, it resyncs to the second URL:

```
(“$A” ne “Provisioned”)? (Line_Enable_1_ = “No”;)! https://p.tel.com/init-prov
| https://p.tel.com/configs
```

#### Example 5

In this example, the profile that the server returns is assumed to contain XML element tags. These tags must be remapped to proper parameter names by the aliases map stored in GPP_B:

```
[--alias b] https://p.tel.com/account/$PN$MA.xml
```

A resync is typically considered unsuccessful if a requested profile is not received from the server. The Resync_Fails_On_FNF parameter can override this default behavior. If Resync_Fails_On_FNF is set to No, the device accepts a file-not-found response from the server as a successful resync. The default value for Resync_Fails_On_FNF is Yes.

### Upgrade rule

Upgrade rule is to tell the device to activate to a new load and from where to get the load, if necessary. If the load is already on the device, it won’t try to get the load. So, validity of the load location doesn’t matter when the desired load is in the inactive partition.

The Upgrade_Rule specifies a firmware load which, if different from the current load, will be downloaded and applied unless limited by a conditional expression or Upgrade_Enable is set to No .

The phone provides one configurable remote upgrade parameter, Upgrade_Rule. This parameter accepts syntax similar to the profile rule parameters. URL options aren’t supported for upgrades, but conditional expressions and assignment expressions can be used. If conditional expressions are used, the parameter can be populated with multiple alternatives, separated by the | character. The syntax for each alternative is as follows:

```
[ conditional-expr ] [ assignment-expr ] URL
```

As in the case of Profile_Rule* parameters, the Upgrade_Rule parameter evaluates each alternative until a conditional expression is satisfied or an alternative has no conditional expression. The accompanying assignment expression is evaluated, if specified. Then, an upgrade to the specified URL is attempted.

If the Upgrade_Rule contains a URL without a conditional expression, the device upgrades to the firmware image that the URL specifies. After macro expansion and evaluation of the rule, the device doesn’t reattempt to upgrade until the rule is modified, or the effective combination of scheme + server + port + filepath is changed.

To attempt a firmware upgrade, the device disables audio at the start of the procedure and reboots at the end of the procedure. The device automatically begins an upgrade that is driven by the contents of Upgrade_Rule only if all voice lines are currently inactive.

For example,

```
https://10.73.10.223/firmware/PHONEOS-8875.1-0-1-0001-1.loads
```

In this example, the Upgrade_Rule upgrades the firmware to the image that is stored at the indicated URL.

Here’s another example:

```
(“$F” ne “beta-customer”)? http://p.tel.com/firmware/PHONEOS-8875.1-0-1-0001-1.loads
| http://p.tel.com/firmware/PHONEOS-8875.1-0-1-0001-1.loads
```

This example directs the unit to load one of two images, based on the contents of a general-purpose parameter, GPP_F.

## Provisioning parameters

You can find the provisioning parameters on the Provisioning tab in the phone web page.

### Configuration profile parameters

The following table defines the function and usage of each parameter in the Configuration Profile Parameters section under the Provisioning tab.

Parameter name

Description and default value

Provision Enable

Controls all resync actions independently of firmware upgrade actions. Set to Yes to enable remote provisioning.

The default value is Yes.

Resync On Reset

Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades.

The default value is Yes.

Resync Random Delay

A random delay following the boot-up sequence before performing the reset, specified in seconds. In a pool of IP Telephony devices that are scheduled to simultaneously power up, this introduces a spread in the times at which each unit sends a resync request to the provisioning server. This feature can be useful in a large residential deployment, in the case of a regional power failure.

The value for this field must be an integer ranging between 0 and 65535.

The default value is 2.

Resync At (HHmm)

The time (HHmm) that the device resynchronizes with the provisioning server.

The value for this field must be a four-digit number ranging from 0000 to 2400 to indicate the time in HHmm format. For example, 0959 indicates 09:59.

The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value, the Resync Periodic parameter is ignored.

Resync At Random Delay

Prevents an overload of the provisioning server when a large number of devices power-on simultaneously.

To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay = (Resync At Random Delay + 30)/60 minutes, the input value in seconds is converted to minutes, rounding up to the next minute to calculate the final random_delay interval.

The valid value ranges between 600 and 65535.

If the value is less than 600, the random delay internal is between 0 and 600.

The default value is 600 seconds (10 minutes).

Resync Periodic

The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only after the first successful sync with the server.

The valid formats are as follows:

An integer

Example: An input of 3000 indicates that the next resync occurs in 3000 seconds.

Multiple integers

Example: An input of 600,1200,300 indicates that the first resync occurs in 600 seconds, the second resync occurs in 1200 seconds after the first one, and the third resync occurs in 300 seconds after the second one.

A time range

Example, an input of 2400+30 indicates that the next resync occurs in between 2400 and 2430 seconds after a successful resync.

Set this parameter to zero to disable periodic resynchronization.

The default value is 3600 seconds.

Resync Error Retry Delay

If a resync operation fails because the IP Telephony device was unable to retrieve a profile from the server, or the downloaded file is corrupt, or an internal error occurs, the device tries to resync again after a time specified in seconds.

The valid formats are as follows:

An integer

Example: An input of 300 indicates that the next retry for resync occurs in 300 seconds.

Multiple integers

Example: An input of 600,1200,300 indicates that the first retry occurs in 600 seconds after the failure, the second retry occurs in 1200 seconds after the failure of the first retry, and the third retry occurs in 300 seconds after the failure of the second retry.

A time range

Example, an input of 2400+30 indicates that the next retry occurs in between 2400 and 2430 seconds after a resync failure.

If the delay is set to 0, the device does not try to resync again following a failed resync attempt.

Forced Resync Delay

Maximum delay (in seconds) the phone waits before performing a resynchronization.

The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in succession without interruption.

The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of the counter. Resync events are delayed until this counter decrements to zero.

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

A resync is considered unsuccessful if a requested profile is not received from the server. This can be overridden by this parameter. When it is set to no , the device accepts a file-not-found response from the server as a successful resync.

The default value is Yes.

Profile Rule

Profile Rule B

Profile Rule C

Profile Rule D

Each profile rule informs the phone of a source from which to obtain a profile (configuration file). During every resync operation, the phone applies all the profiles in sequence.

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

### Firmware upgrade parameters

The following table defines the function and usage of each parameter in the Firmware Upgrade section of the Provisioning tab.

Parameter name

Description and default value

Upgrade Enable

Enables firmware upgrade operations independently of resync actions.

The default value is Yes.

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Upgrade_Enable ua="na">Yes</Upgrade_Enable>

- In the phone administration web page , set this field to Yes or No.

Upgrade Error Retry Delay

The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next firmware upgrade attempt occurs when this timer counts down to zero.

The default value is 3600 seconds.

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Upgrade_Error_Retry_Delay ua="na">3600</Upgrade_Error_Retry_Delay>

- In the phone administration web page , set the value.

Upgrade Rule

A firmware upgrade script that defines upgrade conditions and associated firmware URLs. It uses the same syntax as Profile Rule.

Use the following format to enter the upgrade rule:

```
<tftp|http|https>://<ip address><:port>/<path>/<load name>
```

For example:

```
tftp://192.168.1.5/firmware/PHONEOS-8875.1-0-1-0001-1.loads
```

```
http://10.74.16.242/PHONEOS.3-0-1-0001-213.loads
```

If no protocol is specified, TFTP is assumed. If no server-name is specified, the host that requests the URL is used as the server name. If no port is specified, the default port is used (69 for TFTP, 80 for HTTP, or 443 for HTTPS).

The default value is blank.

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Upgrade_Rule ua="na">http://10.74.16.242/PHONEOS.3-0-1-0001-213.loads</Upgrade_Rule>

- In the phone administration web page , enter the path where the load file is stored.

Log Upgrade Request Msg

Syslog message issued at the start of a firmware upgrade attempt.

Default: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Log_Upgrade_Request_Msg ua="na">$PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH</Log_Upgrade_Request_Msg>

- In the phone administration web page , customize the parameter as needed.

Log Upgrade Success Msg

Syslog message issued after a firmware upgrade attempt completes successfully.

The default value is $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Log_Upgrade_Success_Msg ua="na">$PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR</Log_Upgrade_Success_Msg>

- In the phone administration web page , customize the parameter as needed.

Log Upgrade Failure Msg

Syslog message issued after a failed firmware upgrade attempt.

The default value is $PN $MAC -- Upgrade failed: $ERR

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Log_Upgrade_Failure_Msg ua="na">$PN $MAC -- Upgrade failed: $ERR</Log_Upgrade_Failure_Msg>

- In the phone administration web page , customize the parameter as needed.

Peer Firmware Sharing

Enables or disables the Peer Firmware Sharing (PFS) feature. Select Yes or No to enable or to disable the feature.

Default: Yes

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Peer_Firmware_Sharing ua="na">Yes</Peer_Firmware_Sharing>

- In the phone administration web page , set this field to Yes or No.

Peer Firmware Sharing Log Server

Indicates the IP address and the port to which the UDP message is sent.

For example: 10.98.76.123:514 where, 10.98.76.123 is the IP address and 514 is the port number.

Configure this parameter with one of the methods:

In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Peer_Firmware_Sharing_Log_Server ua="na">10.98.76.123:514</Peer_Firmware_Sharing_Log_Server>

- In the phone administration web page , enter the log server address.

### General purpose parameters

The following table defines the function and usage of each parameter in the General Purpose Parameters section of the Provisioning tab.

Parameter name

Description and default value

GPP A - GPP P

The general purpose parameters GPP_* are used as free string registers when configuring the phones to interact with a particular provisioning server solution. They can be configured to contain diverse values, including the following:

Encryption keys.

URLs.

Multistage provisioning status information.

Post request templates.

Parameter name alias maps.

Partial string values, eventually combined into complete parameter values.

The default value is blank.

### Macro expansion variables

Certain macro variables are recognized within the following provisioning parameters:

Profile_Rule

Profile_Rule_*

Resync_Trigger_*

Upgrade_Rule

Log_*

GPP_* (under specific conditions)

Within these parameters, syntax types, such as $NAME or $(NAME), are recognized and expanded.

Macro variable substrings can be specified with the notation $(NAME:p) and $(NAME:p:q), where p and q are non-negative integers (available in revision 2.0.11 and above). The resulting macro expansion is the substring starting at character offset p, with length q (or else till end-of-string if q is not specified). For example, if GPP_A contains ABCDEF, then $(A:2) expands to CDEF, and $(A:2:3) expands to CDE.

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

Product Name. For example, CP-8875, DP-9851, DP-9871.

PSN

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

PHONEOS.3-1-1-0104-37

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

Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts.

UIDn

The contents of the Line n UserID configuration parameter.

EMS

Extension Mobility Status

MUID

Extension Mobility User ID

MPWD

Extension Mobility Password

### Internal error codes

The phone defines a number of internal error codes (X00–X99) to facilitate configuration in providing finer control over the behavior of the unit under certain error conditions.

Parameter name

Description and default value

X00

Transport layer (or ICMP) error when sending a SIP request.

X20

SIP request times out while waiting for a response.

X40

General SIP protocol error (for example, unacceptable codec in SDP in 200 and ACK messages, or times out while waiting for ACK).

X60

Dialed number invalid according to given dial plan.

| Parameter name | Description and default value |
|---|---|
| Provision Enable | Controls all resync actions independently of firmware upgrade actions. Set to Yes to enable remote provisioning. The default value is Yes. |
| Resync On Reset | Triggers a resync after every reboot except for reboots caused by parameter updates and firmware upgrades. The default value is Yes. |
| Resync Random Delay | A random delay following the boot-up sequence before performing the reset, specified in seconds. In a pool of IP Telephony devices that are scheduled to simultaneously power up, this introduces a spread in the times at which each unit sends a resync request to the provisioning server. This feature can be useful in a large residential deployment, in the case of a regional power failure. The value for this field must be an integer ranging between 0 and 65535. The default value is 2. |
| Resync At (HHmm) | The time (HHmm) that the device resynchronizes with the provisioning server. The value for this field must be a four-digit number ranging from 0000 to 2400 to indicate the time in HHmm format. For example, 0959 indicates 09:59. The default value is empty. If the value is invalid, the parameter is ignored. If this parameter is set with a valid value, the Resync Periodic parameter is ignored. |
| Resync At Random Delay | Prevents an overload of the provisioning server when a large number of devices power-on simultaneously. To avoid flooding resync requests to the server from multiple phones, the phone resynchronizes in the range between the hours and minutes, and the hours and minutes plus the random delay (hhmm, hhmm+random_delay). For example, if the random delay = (Resync At Random Delay + 30)/60 minutes, the input value in seconds is converted to minutes, rounding up to the next minute to calculate the final random_delay interval. The valid value ranges between 600 and 65535. If the value is less than 600, the random delay internal is between 0 and 600. The default value is 600 seconds (10 minutes). |
| Resync Periodic | The time interval between periodic resynchronizes with the provisioning server. The associated resync timer is active only after the first successful sync with the server. The valid formats are as follows: An integer Example: An input of 3000 indicates that the next resync occurs in 3000 seconds. Multiple integers Example: An input of 600,1200,300 indicates that the first resync occurs in 600 seconds, the second resync occurs in 1200 seconds after the first one, and the third resync occurs in 300 seconds after the second one. A time range Example, an input of 2400+30 indicates that the next resync occurs in between 2400 and 2430 seconds after a successful resync. Set this parameter to zero to disable periodic resynchronization. The default value is 3600 seconds. |
| Resync Error Retry Delay | If a resync operation fails because the IP Telephony device was unable to retrieve a profile from the server, or the downloaded file is corrupt, or an internal error occurs, the device tries to resync again after a time specified in seconds. The valid formats are as follows: An integer Example: An input of 300 indicates that the next retry for resync occurs in 300 seconds. Multiple integers Example: An input of 600,1200,300 indicates that the first retry occurs in 600 seconds after the failure, the second retry occurs in 1200 seconds after the failure of the first retry, and the third retry occurs in 300 seconds after the failure of the second retry. A time range Example, an input of 2400+30 indicates that the next retry occurs in between 2400 and 2430 seconds after a resync failure. If the delay is set to 0, the device does not try to resync again following a failed resync attempt. |
| Forced Resync Delay | Maximum delay (in seconds) the phone waits before performing a resynchronization. The device does not resync while one of its phone lines is active. Because a resync can take several seconds, it is desirable to wait until the device has been idle for an extended period before resynchronizing. This allows a user to make calls in succession without interruption. The device has a timer that begins counting down when all of its lines become idle. This parameter is the initial value of the counter. Resync events are delayed until this counter decrements to zero. The valid value ranges between 0 and 65535. The default value is 14,400 seconds. |
| Resync From SIP | Enables a resync to be triggered via a SIP NOTIFY message. The default value is Yes. |
| Resync After Upgrade Attempt | Enables or disables the resync operation after any upgrade occurs. If Yes is selected, sync is triggered. The default value is Yes. |
| Resync Trigger 1, Resync Trigger 2 | Configurable resync trigger conditions. A resync is triggered when the logic equation in these parameters evaluates to TRUE. The default value is (empty). |
| Resync Fails On FNF | A resync is considered unsuccessful if a requested profile is not received from the server. This can be overridden by this parameter. When it is set to no , the device accepts a file-not-found response from the server as a successful resync. The default value is Yes. |
| Profile Rule Profile Rule B Profile Rule C Profile Rule D | Each profile rule informs the phone of a source from which to obtain a profile (configuration file). During every resync operation, the phone applies all the profiles in sequence. Default: /$PSN.xml If you are applying AES-256-CBC encryption to the configuration files, specify the encryption key with the --key keyword as follows: [--key <encryption key>] You can enclose the encryption key in double-quotes (") optionally. |
| DHCP Option To Use | DHCP options, delimited by commas, used to retrieve firmware and profiles. The default value is 66,160,159,150,60,43,125. |
| Log Request Msg | This parameter contains the message that is sent to the syslog server at the start of a resync attempt. The default value is $PN $MAC –Requesting % $SCHEME://$SERVIP:$PORT$PATH . |
| Log Success Msg | The syslog message that is issued upon successful completion of a resync attempt. The default value is $PN $MAC –Successful Resync % $SCHEME://$SERVIP:$PORT$PATH -- $ERR . |
| Log Failure Msg | The syslog message that is issued after a failed resync attempt. The default value is $PN $MAC -- Resync failed: $ERR . |
| User Configurable Resync | Allows a user to resync the phone from the IP phone screen. The default value is Yes. |

| Parameter name | Description and default value |
|---|---|
| Upgrade Enable | Enables firmware upgrade operations independently of resync actions. The default value is Yes. Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Upgrade_Enable ua="na">Yes</Upgrade_Enable> In the phone administration web page , set this field to Yes or No. |
| Upgrade Error Retry Delay | The upgrade retry interval (in seconds) applied in case of upgrade failure. The device has a firmware upgrade error timer that activates after a failed firmware upgrade attempt. The timer is initialized with the value in this parameter. The next firmware upgrade attempt occurs when this timer counts down to zero. The default value is 3600 seconds. Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Upgrade_Error_Retry_Delay ua="na">3600</Upgrade_Error_Retry_Delay> In the phone administration web page , set the value. |
| Upgrade Rule | A firmware upgrade script that defines upgrade conditions and associated firmware URLs. It uses the same syntax as Profile Rule. Use the following format to enter the upgrade rule: <tftp\|http\|https>://<ip address><:port>/<path>/<load name> For example: tftp://192.168.1.5/firmware/PHONEOS-8875.1-0-1-0001-1.loads http://10.74.16.242/PHONEOS.3-0-1-0001-213.loads If no protocol is specified, TFTP is assumed. If no server-name is specified, the host that requests the URL is used as the server name. If no port is specified, the default port is used (69 for TFTP, 80 for HTTP, or 443 for HTTPS). The default value is blank. Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Upgrade_Rule ua="na">http://10.74.16.242/PHONEOS.3-0-1-0001-213.loads</Upgrade_Rule> In the phone administration web page , enter the path where the load file is stored. |
| Log Upgrade Request Msg | Syslog message issued at the start of a firmware upgrade attempt. Default: $PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Log_Upgrade_Request_Msg ua="na">$PN $MAC -- Requesting upgrade $SCHEME://$SERVIP:$PORT$PATH</Log_Upgrade_Request_Msg> In the phone administration web page , customize the parameter as needed. |
| Log Upgrade Success Msg | Syslog message issued after a firmware upgrade attempt completes successfully. The default value is $PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Log_Upgrade_Success_Msg ua="na">$PN $MAC -- Successful upgrade $SCHEME://$SERVIP:$PORT$PATH -- $ERR</Log_Upgrade_Success_Msg> In the phone administration web page , customize the parameter as needed. |
| Log Upgrade Failure Msg | Syslog message issued after a failed firmware upgrade attempt. The default value is $PN $MAC -- Upgrade failed: $ERR Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Log_Upgrade_Failure_Msg ua="na">$PN $MAC -- Upgrade failed: $ERR</Log_Upgrade_Failure_Msg> In the phone administration web page , customize the parameter as needed. |
| Peer Firmware Sharing | Enables or disables the Peer Firmware Sharing (PFS) feature. Select Yes or No to enable or to disable the feature. Default: Yes Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Peer_Firmware_Sharing ua="na">Yes</Peer_Firmware_Sharing> In the phone administration web page , set this field to Yes or No. |
| Peer Firmware Sharing Log Server | Indicates the IP address and the port to which the UDP message is sent. For example: 10.98.76.123:514 where, 10.98.76.123 is the IP address and 514 is the port number. Configure this parameter with one of the methods: In the phone configuration file with XML(cfg.xml) , enter a string in this format: <Peer_Firmware_Sharing_Log_Server ua="na">10.98.76.123:514</Peer_Firmware_Sharing_Log_Server> In the phone administration web page , enter the log server address. |

| Parameter name | Description and default value |
|---|---|
| GPP A - GPP P | The general purpose parameters GPP_* are used as free string registers when configuring the phones to interact with a particular provisioning server solution. They can be configured to contain diverse values, including the following: Encryption keys. URLs. Multistage provisioning status information. Post request templates. Parameter name alias maps. Partial string values, eventually combined into complete parameter values. The default value is blank. |

| Parameter Name | Description and Default Value |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by the contents of the general purpose parameters GPP_A through GPP_P. |
| SA through SD | Replaced by special purpose parameters GPP_SA through GPP_SD. These parameters hold keys or passwords used in provisioning. $SA through $SD are recognized as arguments to the optional resync URL qualifier, --key. |
| MA | MAC address using lower case hex digits, for example, 000e08aabbcc. |
| MAU | MAC address using upper case hex digits, for example 000E08AABBCC. |
| MAC | MAC address using lower case hex digits, and colons to separate hex digit pairs. For example 00:0e:08:aa:bb:cc. |
| PN | Product Name. For example, CP-8875, DP-9851, DP-9871. |
| PSN | Product Series Number. For example, V03. |
| SN | Serial Number string. for example 88012BA01234. |
| CCERT | SSL Client Certificate status: Installed or Not Installed. |
| IP | IP address of the phone within its local subnet. For example 192.168.1.100. |
| EXTIP | External IP of the phone, as seen on the Internet. For example 66.43.16.52. |
| SWVER | Software version string. For example, PHONEOS.3-1-1-0104-37 |
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
| ERR | Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts. |
| UIDn | The contents of the Line n UserID configuration parameter. |
| EMS | Extension Mobility Status |
| MUID | Extension Mobility User ID |
| MPWD | Extension Mobility Password |

| Parameter name | Description and default value |
|---|---|
| X00 | Transport layer (or ICMP) error when sending a SIP request. |
| X20 | SIP request times out while waiting for a response. |
| X40 | General SIP protocol error (for example, unacceptable codec in SDP in 200 and ACK messages, or times out while waiting for ACK). |
| X60 | Dialed number invalid according to given dial plan. |