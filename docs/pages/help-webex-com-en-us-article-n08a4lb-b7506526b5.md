---
doc_id: help-webex-com-en-us-article-n08a4lb-b7506526b5
source_url: https://help.webex.com/en-us/article/n08a4lb
retrieved_at: 2026-11-02T13:12:44.302371+00:00
---

## Configure call center agent phone

You can enable a phone with Automatic Call Distribution (ACD) features. This phone acts as
        a call center agent's phone and can be used to trace a customer call, to escalate any
        customer call to a supervisor in emergency, to categorize contact numbers using disposition
        codes, and to view customer call details.

Access the phone administration web page.

Select Voice > Ext(n) , where (n) is the number of an extension to
          share.

Navigate to the ACD Settings section, set up call center agent phone.

For more information about the parameters, see Parameters for Automatic Call Distribution (ACD) .

### Parameters for Automatic Call Distribution (ACD)

Broadsoft ACD

Enables the phone for Automatic Call Distribution (ACD).

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Broadsoft_ACD_n_ ua="na">Yes</Broadsoft_ACD_n_>
```

In the phone web page, select Yes to enable this feature and select No to disable it.

Options: Yes and No

Default: No

Call Information Enable

Enables the phone to display details of a call center call.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: No

Disposition Code Enable

Enables the user to add a disposition code.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: No

Trace Enable

Enables the user to trace the last incoming call.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: No

Emergency Escalation Enable

Enables the user to escalate a call to a supervisor in case of emergency.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: No

Queue Status Notification Enable

Displays the call center status and the agent status.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Queue_Status_Notification_Enable_n_
          ua="na">Yes</Queue_Status_Notification_Enable_n_>
```

In the phone web page, select Yes to enable this feature. Select No to disable it.

Options: Yes and No

Default: No

ACD Status

Control whether to sync/set the Agent status from/to the server after the device powers up.

For more information, see Restore ACD status .

Auto Available After Sign-In

Sets the agent status to Available automatically when the user signs into the phone as a call center agent.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Auto_Available_After_Sign-In_n_
        ua="na">Yes</Auto_Available_After_Sign-In_n_>
```

In the phone web page, select Yes to enable this feature and select No to disable it.

Options: Yes and No

Default: No

Unavailable Reason Code Enable

Displays the ACD unavailable reason code edit box in phone LCD.

Perform one of the following:

```
<Unavailable_Reason_Code_Enable_n_ ua="na">Yes</Unavailable_Reason_Code_Enable_n_>
```

- In the phone web page, select Yes to enable this feature.

- Select No to disable it.

Options: Yes and No

Default: Yes

## Restore ACD status

You can enable the phone to automatically set the ACD status to the last local value in one
        of the following situations:

Phone is powered on.

Phone status is changed to “Registered” from “Unregistered” or “Registration failed”
            status.

Registration destination server IP address is changed when failover happens, a fallback
            happens, or a DNS response is changed.

Access the phone administration web page.

Navigate to the ACD Settings section, set BraodSoft ACD to Yes .

From ACD Status parameter, select one of the options:

Sync From Local : Select this option to restore the last local status as ACD
                status when the phone boots up, status is changed to "Registered" from
                "Unregistered" or "Registration failed", or registration destination ip address is
                changed due to failover, fallback or DNS response is changed.

When the intial ACD status is configured to sync from local, and the last local
                status is unavailable with a reason code, after the phone boots up, the reason code
                will not be restored.

- Sync From Server : Select this option to get ACD intial status from the
              server. This is the default value.

You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format:

```
<ACD_Status_n_ ua="na">Sync From Local</ACD_Status_n_>
```

where n = 1 to 16

Click Submit All Changes .

## Control unavailable menu text

You can control if your user wants to hide the Unavailable menu text box of the Set agent status screen on the phone

Access the phone administration web page.

Navigate to the ACD Settings section, set the Unavailable Reason Code
            Enable parameter to No to hide the Unavailable text box on the
          phone.

To display the text box, select Yes . This is the default value.

You
            can configure this parameter in the phone configuration XML file (cfg.xml) by entering a
            string in this format:

Click Submit All Changes .

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext(n) , where (n) is the number of an extension to
          share. |
| 3 | Navigate to the ACD Settings section, set up call center agent phone. For more information about the parameters, see Parameters for Automatic Call Distribution (ACD) . |

| Parameter | Description |
|---|---|
| Broadsoft ACD | Enables the phone for Automatic Call Distribution (ACD). Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Broadsoft_ACD_n_ ua="na">Yes</Broadsoft_ACD_n_> In the phone web page, select Yes to enable this feature and select No to disable it. Options: Yes and No Default: No |
| Call Information Enable | Enables the phone to display details of a call center call. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Call_Information_Enable_n_ ua="na">Yes</Call_Information_Enable_n_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: No |
| Disposition Code Enable | Enables the user to add a disposition code. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Disposition_Code_Enable_n_ ua="na">Yes</Disposition_Code_Enable_n_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: No |
| Trace Enable | Enables the user to trace the last incoming call. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Trace_Enable_n_ ua="na">Yes</Trace_Enable_n_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: No |
| Emergency Escalation Enable | Enables the user to escalate a call to a supervisor in case of emergency. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Emergency_Escalation_Enable_n_ ua="na">Yes</Emergency_Escalation_Enable_n_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: No |
| Queue Status Notification Enable | Displays the call center status and the agent status. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Queue_Status_Notification_Enable_n_
          ua="na">Yes</Queue_Status_Notification_Enable_n_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: No |
| ACD Status | Control whether to sync/set the Agent status from/to the server after the device powers up. For more information, see Restore ACD status . |
| Auto Available After Sign-In | Sets the agent status to Available automatically when the user signs into the phone as a call center agent. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Auto_Available_After_Sign-In_n_
        ua="na">Yes</Auto_Available_After_Sign-In_n_> In the phone web page, select Yes to enable this feature and select No to disable it. Options: Yes and No Default: No |
| Unavailable Reason Code Enable | Displays the ACD unavailable reason code edit box in phone LCD. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Unavailable_Reason_Code_Enable_n_ ua="na">Yes</Unavailable_Reason_Code_Enable_n_> In the phone web page, select Yes to enable this feature. Select No to disable it. Options: Yes and No Default: Yes |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Navigate to the ACD Settings section, set BraodSoft ACD to Yes . |
| 3 | From ACD Status parameter, select one of the options: Sync From Local : Select this option to restore the last local status as ACD
                status when the phone boots up, status is changed to "Registered" from
                "Unregistered" or "Registration failed", or registration destination ip address is
                changed due to failover, fallback or DNS response is changed. When the intial ACD status is configured to sync from local, and the last local
                status is unavailable with a reason code, after the phone boots up, the reason code
                will not be restored. Sync From Server : Select this option to get ACD intial status from the
              server. This is the default value. You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format: <ACD_Status_n_ ua="na">Sync From Local</ACD_Status_n_> where n = 1 to 16 |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Navigate to the ACD Settings section, set the Unavailable Reason Code
            Enable parameter to No to hide the Unavailable text box on the
          phone. To display the text box, select Yes . This is the default value. You
            can configure this parameter in the phone configuration XML file (cfg.xml) by entering a
            string in this format: <Unavailable_Reason_Code_Enable_1_
              ua="na"> Yes </Unavailable_Reason_Code_Enable_1_> |
| 3 | Click Submit All Changes . |