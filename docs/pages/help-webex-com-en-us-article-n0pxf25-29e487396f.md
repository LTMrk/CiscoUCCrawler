---
doc_id: help-webex-com-en-us-article-n0pxf25-29e487396f
source_url: https://help.webex.com/en-us/article/n0pxf25
retrieved_at: 2026-11-02T13:06:10.883785+00:00
---

## Add dialog-based shared line appearance (SLA)

You can now enable dialog-based shared line, so that the phones in the shared line can
        subscribe to the dialog event package.

Access the phone administration web page.

Select Voice > SIP .

In the SIP Parameters section, set the Share Line
            Event Package Type parameter to Dialog to subscribe
          the phone to the dialog event package.

You can also set the parameter to Call-Info and the phone
            retains the legacy behavior.

Default value: Call-Info

You can also configure this parameter in the configuration file (cfg.xml) by entering a
            string in this format:

<Share_Line_Event_Package_Type ua="na">Dialog</Share_Line_Event_Package_Type>

Click Submit All Changes .

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > SIP . |
| 3 | In the SIP Parameters section, set the Share Line
            Event Package Type parameter to Dialog to subscribe
          the phone to the dialog event package. You can also set the parameter to Call-Info and the phone
            retains the legacy behavior. Default value: Call-Info You can also configure this parameter in the configuration file (cfg.xml) by entering a
            string in this format: <Share_Line_Event_Package_Type ua="na">Dialog</Share_Line_Event_Package_Type> |
| 4 | Click Submit All Changes . |