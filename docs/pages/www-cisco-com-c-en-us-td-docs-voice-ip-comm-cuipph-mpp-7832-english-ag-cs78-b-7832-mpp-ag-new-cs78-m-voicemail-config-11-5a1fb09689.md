---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7832-english-ag-cs78-b-7832-mpp-ag-new-cs78-m-voicemail-config-11-5a1fb09689
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7832/english/AG/cs78_b_7832-mpp-ag_new/cs78_m_voicemail-config-1135.html
retrieved_at: 2026-08-21T23:25:35.935200+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide for Release 11.3(1) and Later

# Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide for Release 11.3(1) and Later

Updated: September 16, 2021

Chapter: Voicemail Configuration

## Chapter: Voicemail Configuration

# Voicemail Configuration

## Configure Voicemail

You can configure the internal or external phone number or URL for the voicemail system. If you use an external voicemail
                              service, the number must include any digits required to dial out and any required area code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Phone .

In the General section, enter the Voice Mail Number that is a phone number or URL to check the voicemail.

```
<Voice_Mail_Number ua="na">123</Voice_Mail_Number>
```

Default: Empty

Click Submit All Changes .

### Configure Voicemail for An Extension

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Ext(n) , where (n) is the number of an extension.

In the Call Feature Settings section, configure the parameters Voice Mail Server , Voice Mail Subscribe Interval (optional), and Voice Mail Enable as described in Parameters for Voicemail Server .

Click Submit All Changes .

The phone reboots.

#### Parameters for Voicemail Server

The following table describes the Call Feature Settings for Voicemail.

Parameter

Description

Voice Mail Server

Identifies the SpecVM server for the phone, generally the IP address, and port number of the VM server.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

```
<Voice_Mail_Server_1_ ua="na"></Voice_Mail_Server_1_>
```

In the phone web page, enter the IP address of the voicemail server.

Default: Empty

Voice Mail Subscribe Interval

The expiration time, in seconds, of a subscription to a voicemail server.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

```
<Voice_Mail_Subscribe_Interval_1_ ua="na">86400</Voice_Mail_Subscribe_Interval_1_>
```

In the phone web page, enter an appropriate value.

Allowed values: An integer from 0 through 86400

If the value is set to 0, then the phone uses the default value instead.

Default: 86400

Voice Mail Enable

Enables or disables the subscription to the voicemail server for the specific extension.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

```
<Voice_Mail_Enable_1_ ua="na">Yes</Voice_Mail_Enable_1_>
```

In the phone web interface, set this field to Yes or No to enable or disable the function.

Allowed values: Yes and No

Default: Yes

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the General section, enter the Voice Mail Number that is a phone number or URL to check the voicemail. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Voice_Mail_Number ua="na">123</Voice_Mail_Number> Default: Empty |
| Step 3 | Click Submit All Changes . The phone reboots. |

| Step 1 | Select Voice > Ext(n) , where (n) is the number of an extension. |
|---|---|
| Step 2 | In the Call Feature Settings section, configure the parameters Voice Mail Server , Voice Mail Subscribe Interval (optional), and Voice Mail Enable as described in Parameters for Voicemail Server . |
| Step 3 | Click Submit All Changes . The phone reboots. |

| Parameter | Description |
|---|---|
| Voice Mail Server | Identifies the SpecVM server for the phone, generally the IP address, and port number of the VM server. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Voice_Mail_Server_1_ ua="na"></Voice_Mail_Server_1_> In the phone web page, enter the IP address of the voicemail server. Default: Empty |
| Voice Mail Subscribe Interval | The expiration time, in seconds, of a subscription to a voicemail server. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Voice_Mail_Subscribe_Interval_1_ ua="na">86400</Voice_Mail_Subscribe_Interval_1_> In the phone web page, enter an appropriate value. Allowed values: An integer from 0 through 86400 If the value is set to 0, then the phone uses the default value instead. Default: 86400 |
| Voice Mail Enable | Enables or disables the subscription to the voicemail server for the specific extension. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Voice_Mail_Enable_1_ ua="na">Yes</Voice_Mail_Enable_1_> In the phone web interface, set this field to Yes or No to enable or disable the function. Allowed values: Yes and No Default: Yes |