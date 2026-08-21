---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-infrastructure-articles-mcu-tms-configure-work-together-kb-288-html-3b2459067a
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/infrastructure/articles/mcu_tms_configure_work_together_kb_288.html
retrieved_at: 2026-08-21T06:28:59.638918+00:00
---

Cisco TelePresence Management Suite (TMS) Configuring Cisco TMS and an MCU to work together

# Cisco TelePresence Management Suite (TMS)

## Configuring Cisco TMS and an MCU to work together

### How do I configure Cisco TelePresence Management Suite (Cisco TMS) and a Cisco TelePresence MCU to work together?

Follow these instructions.

#### Preparing a Cisco TelePresence MCU for adding to Cisco TMS

- In Network > Services ensure the SNMP port is enabled and set to port 161.

- In Network > SNMP ensure the RO, RW and Trap community are set to public, private and public respectively.

- In Settings > H.323 ensure that H.323 gatekeeper usage is set to Required and that you have specified a suitable service prefix (see Numeric IDs in Cisco TMS below).

- If required, configure your MCU's SIP Settings. Go to Settings > SIP and set SIP registrar usage to Enabled and check Allow numeric ID registration for conferences .

- In Network > Port A , configure a host name for your MCU. (If Cisco TMS is to manage your MCU using port B, then configure the host name in Network > Port B ).

#### Adding an MCU to Cisco TelePresence Management Suite (Cisco TMS)

- In Cisco TMS go to Systems > Navigator and click Add systems .

- Enter the IP address or DNS name of the Cisco TelePresence MCU.

- If required, enter a username and password by clicking on Advanced settings and completing the fields.

- Click Next .

- Cisco TMS should find your system. If you see a message that an incorrect password has been supplied, select Edit system and enter/re-enter the username and password. Click Save .

- You should be returned to a screen indicating that your system has been added. Click Finish adding systems .

#### Numeric IDs in Cisco TMS

For H.323, we recommend that you configure the Cisco TelePresence MCU to use a service prefix before adding the system to Cisco TMS.

When Cisco TMS creates a conference on an MCU it assigns a numeric ID to that conference. Where there is more than one MCU, Cisco TMS might assign the same numeric ID to more than one conference (on different MCUs); however, by specifying a unique Prefix for MCU registrations for each MCU ( Settings > H.323 ), it is possible to ensure that registrations and connections do not fail.

Alternatively, change the numeric IDs that Cisco TMS uses when creating conferences. To do this:

- Go to Systems and select the MCU in the left-hand pane.

- Click Settings and then Extended settings .

- For First meeting id specify the first numeric ID to be used on this MCU.

- Specify the Meeting id step .

- Click Save .

The number of meeting IDs that could potentially be used by Cisco TMS is equal to the port count of the MCU; for example, for a 4520 there are 40 video ports and 40 audio ports and therefore a maximum 80 meeting IDs. These should not overlap with those of other MCUs unless a service prefix has been specified.

Sometimes Cisco TMS will report that a gatekeeper registration from the MCU has failed, even though the MCU reports that all gatekeeper registrations have been successful.

#### Using Cisco TMS with SIP

For SIP it is recommended that you follow the above procedure of ensuring meeting IDs do not conflict between MCUs because service prefixes are not supported in SIP. It is also recommended that conference SIP registration is enabled. To do this:

- In Cisco TMS, go to Systems and select the MCU in the left hand pane.

- Click Settings and then Extended settings .

- For Conference sip registration , select On .

- Click Save .

#### This article applies to the following products:

- Cisco TelePresence MCU 4200 / MSE 8420

- Cisco TelePresence MCU 4500

- Cisco TelePresence MSE 8510 blade

- Cisco TelePresence Management Suite

|  | How do I configure Cisco TelePresence Management Suite (Cisco TMS) and a Cisco TelePresence MCU to work together? Follow these instructions. Preparing a Cisco TelePresence MCU for adding to Cisco TMS In Network > Services ensure the SNMP port is enabled and set to port 161. In Network > SNMP ensure the RO, RW and Trap community are set to public, private and public respectively. In Settings > H.323 ensure that H.323 gatekeeper usage is set to Required and that you have specified a suitable service prefix (see Numeric IDs in Cisco TMS below). If required, configure your MCU's SIP Settings. Go to Settings > SIP and set SIP registrar usage to Enabled and check Allow numeric ID registration for conferences . In Network > Port A , configure a host name for your MCU. (If Cisco TMS is to manage your MCU using port B, then configure the host name in Network > Port B ). Adding an MCU to Cisco TelePresence Management Suite (Cisco TMS) In Cisco TMS go to Systems > Navigator and click Add systems . Enter the IP address or DNS name of the Cisco TelePresence MCU. If required, enter a username and password by clicking on Advanced settings and completing the fields. Click Next . Cisco TMS should find your system. If you see a message that an incorrect password has been supplied, select Edit system and enter/re-enter the username and password. Click Save . You should be returned to a screen indicating that your system has been added. Click Finish adding systems . Numeric IDs in Cisco TMS For H.323, we recommend that you configure the Cisco TelePresence MCU to use a service prefix before adding the system to Cisco TMS. When Cisco TMS creates a conference on an MCU it assigns a numeric ID to that conference. Where there is more than one MCU, Cisco TMS might assign the same numeric ID to more than one conference (on different MCUs); however, by specifying a unique Prefix for MCU registrations for each MCU ( Settings > H.323 ), it is possible to ensure that registrations and connections do not fail. Alternatively, change the numeric IDs that Cisco TMS uses when creating conferences. To do this: Go to Systems and select the MCU in the left-hand pane. Click Settings and then Extended settings . For First meeting id specify the first numeric ID to be used on this MCU. Specify the Meeting id step . Click Save . The number of meeting IDs that could potentially be used by Cisco TMS is equal to the port count of the MCU; for example, for a 4520 there are 40 video ports and 40 audio ports and therefore a maximum 80 meeting IDs. These should not overlap with those of other MCUs unless a service prefix has been specified. Sometimes Cisco TMS will report that a gatekeeper registration from the MCU has failed, even though the MCU reports that all gatekeeper registrations have been successful. Using Cisco TMS with SIP For SIP it is recommended that you follow the above procedure of ensuring meeting IDs do not conflict between MCUs because service prefixes are not supported in SIP. It is also recommended that conference SIP registration is enabled. To do this: In Cisco TMS, go to Systems and select the MCU in the left hand pane. Click Settings and then Extended settings . For Conference sip registration , select On . Click Save . This article applies to the following products: Cisco TelePresence MCU 4200 / MSE 8420 Cisco TelePresence MCU 4500 Cisco TelePresence MSE 8510 blade Cisco TelePresence Management Suite May 3rd, 2011 TAA_KB_288 | How do I configure Cisco TelePresence Management Suite (Cisco TMS) and a Cisco TelePresence MCU to work together? Follow these instructions. Preparing a Cisco TelePresence MCU for adding to Cisco TMS In Network > Services ensure the SNMP port is enabled and set to port 161. In Network > SNMP ensure the RO, RW and Trap community are set to public, private and public respectively. In Settings > H.323 ensure that H.323 gatekeeper usage is set to Required and that you have specified a suitable service prefix (see Numeric IDs in Cisco TMS below). If required, configure your MCU's SIP Settings. Go to Settings > SIP and set SIP registrar usage to Enabled and check Allow numeric ID registration for conferences . In Network > Port A , configure a host name for your MCU. (If Cisco TMS is to manage your MCU using port B, then configure the host name in Network > Port B ). Adding an MCU to Cisco TelePresence Management Suite (Cisco TMS) In Cisco TMS go to Systems > Navigator and click Add systems . Enter the IP address or DNS name of the Cisco TelePresence MCU. If required, enter a username and password by clicking on Advanced settings and completing the fields. Click Next . Cisco TMS should find your system. If you see a message that an incorrect password has been supplied, select Edit system and enter/re-enter the username and password. Click Save . You should be returned to a screen indicating that your system has been added. Click Finish adding systems . Numeric IDs in Cisco TMS For H.323, we recommend that you configure the Cisco TelePresence MCU to use a service prefix before adding the system to Cisco TMS. When Cisco TMS creates a conference on an MCU it assigns a numeric ID to that conference. Where there is more than one MCU, Cisco TMS might assign the same numeric ID to more than one conference (on different MCUs); however, by specifying a unique Prefix for MCU registrations for each MCU ( Settings > H.323 ), it is possible to ensure that registrations and connections do not fail. Alternatively, change the numeric IDs that Cisco TMS uses when creating conferences. To do this: Go to Systems and select the MCU in the left-hand pane. Click Settings and then Extended settings . For First meeting id specify the first numeric ID to be used on this MCU. Specify the Meeting id step . Click Save . The number of meeting IDs that could potentially be used by Cisco TMS is equal to the port count of the MCU; for example, for a 4520 there are 40 video ports and 40 audio ports and therefore a maximum 80 meeting IDs. These should not overlap with those of other MCUs unless a service prefix has been specified. Sometimes Cisco TMS will report that a gatekeeper registration from the MCU has failed, even though the MCU reports that all gatekeeper registrations have been successful. Using Cisco TMS with SIP For SIP it is recommended that you follow the above procedure of ensuring meeting IDs do not conflict between MCUs because service prefixes are not supported in SIP. It is also recommended that conference SIP registration is enabled. To do this: In Cisco TMS, go to Systems and select the MCU in the left hand pane. Click Settings and then Extended settings . For Conference sip registration , select On . Click Save . This article applies to the following products: Cisco TelePresence MCU 4200 / MSE 8420 Cisco TelePresence MCU 4500 Cisco TelePresence MSE 8510 blade Cisco TelePresence Management Suite May 3rd, 2011 TAA_KB_288 | May 3rd, 2011 | TAA_KB_288 |  |
|---|---|---|---|---|---|
| How do I configure Cisco TelePresence Management Suite (Cisco TMS) and a Cisco TelePresence MCU to work together? Follow these instructions. Preparing a Cisco TelePresence MCU for adding to Cisco TMS In Network > Services ensure the SNMP port is enabled and set to port 161. In Network > SNMP ensure the RO, RW and Trap community are set to public, private and public respectively. In Settings > H.323 ensure that H.323 gatekeeper usage is set to Required and that you have specified a suitable service prefix (see Numeric IDs in Cisco TMS below). If required, configure your MCU's SIP Settings. Go to Settings > SIP and set SIP registrar usage to Enabled and check Allow numeric ID registration for conferences . In Network > Port A , configure a host name for your MCU. (If Cisco TMS is to manage your MCU using port B, then configure the host name in Network > Port B ). Adding an MCU to Cisco TelePresence Management Suite (Cisco TMS) In Cisco TMS go to Systems > Navigator and click Add systems . Enter the IP address or DNS name of the Cisco TelePresence MCU. If required, enter a username and password by clicking on Advanced settings and completing the fields. Click Next . Cisco TMS should find your system. If you see a message that an incorrect password has been supplied, select Edit system and enter/re-enter the username and password. Click Save . You should be returned to a screen indicating that your system has been added. Click Finish adding systems . Numeric IDs in Cisco TMS For H.323, we recommend that you configure the Cisco TelePresence MCU to use a service prefix before adding the system to Cisco TMS. When Cisco TMS creates a conference on an MCU it assigns a numeric ID to that conference. Where there is more than one MCU, Cisco TMS might assign the same numeric ID to more than one conference (on different MCUs); however, by specifying a unique Prefix for MCU registrations for each MCU ( Settings > H.323 ), it is possible to ensure that registrations and connections do not fail. Alternatively, change the numeric IDs that Cisco TMS uses when creating conferences. To do this: Go to Systems and select the MCU in the left-hand pane. Click Settings and then Extended settings . For First meeting id specify the first numeric ID to be used on this MCU. Specify the Meeting id step . Click Save . The number of meeting IDs that could potentially be used by Cisco TMS is equal to the port count of the MCU; for example, for a 4520 there are 40 video ports and 40 audio ports and therefore a maximum 80 meeting IDs. These should not overlap with those of other MCUs unless a service prefix has been specified. Sometimes Cisco TMS will report that a gatekeeper registration from the MCU has failed, even though the MCU reports that all gatekeeper registrations have been successful. Using Cisco TMS with SIP For SIP it is recommended that you follow the above procedure of ensuring meeting IDs do not conflict between MCUs because service prefixes are not supported in SIP. It is also recommended that conference SIP registration is enabled. To do this: In Cisco TMS, go to Systems and select the MCU in the left hand pane. Click Settings and then Extended settings . For Conference sip registration , select On . Click Save . This article applies to the following products: Cisco TelePresence MCU 4200 / MSE 8420 Cisco TelePresence MCU 4500 Cisco TelePresence MSE 8510 blade Cisco TelePresence Management Suite May 3rd, 2011 TAA_KB_288 | May 3rd, 2011 | TAA_KB_288 |  |
| May 3rd, 2011 | TAA_KB_288 |

| How do I configure Cisco TelePresence Management Suite (Cisco TMS) and a Cisco TelePresence MCU to work together? Follow these instructions. Preparing a Cisco TelePresence MCU for adding to Cisco TMS In Network > Services ensure the SNMP port is enabled and set to port 161. In Network > SNMP ensure the RO, RW and Trap community are set to public, private and public respectively. In Settings > H.323 ensure that H.323 gatekeeper usage is set to Required and that you have specified a suitable service prefix (see Numeric IDs in Cisco TMS below). If required, configure your MCU's SIP Settings. Go to Settings > SIP and set SIP registrar usage to Enabled and check Allow numeric ID registration for conferences . In Network > Port A , configure a host name for your MCU. (If Cisco TMS is to manage your MCU using port B, then configure the host name in Network > Port B ). Adding an MCU to Cisco TelePresence Management Suite (Cisco TMS) In Cisco TMS go to Systems > Navigator and click Add systems . Enter the IP address or DNS name of the Cisco TelePresence MCU. If required, enter a username and password by clicking on Advanced settings and completing the fields. Click Next . Cisco TMS should find your system. If you see a message that an incorrect password has been supplied, select Edit system and enter/re-enter the username and password. Click Save . You should be returned to a screen indicating that your system has been added. Click Finish adding systems . Numeric IDs in Cisco TMS For H.323, we recommend that you configure the Cisco TelePresence MCU to use a service prefix before adding the system to Cisco TMS. When Cisco TMS creates a conference on an MCU it assigns a numeric ID to that conference. Where there is more than one MCU, Cisco TMS might assign the same numeric ID to more than one conference (on different MCUs); however, by specifying a unique Prefix for MCU registrations for each MCU ( Settings > H.323 ), it is possible to ensure that registrations and connections do not fail. Alternatively, change the numeric IDs that Cisco TMS uses when creating conferences. To do this: Go to Systems and select the MCU in the left-hand pane. Click Settings and then Extended settings . For First meeting id specify the first numeric ID to be used on this MCU. Specify the Meeting id step . Click Save . The number of meeting IDs that could potentially be used by Cisco TMS is equal to the port count of the MCU; for example, for a 4520 there are 40 video ports and 40 audio ports and therefore a maximum 80 meeting IDs. These should not overlap with those of other MCUs unless a service prefix has been specified. Sometimes Cisco TMS will report that a gatekeeper registration from the MCU has failed, even though the MCU reports that all gatekeeper registrations have been successful. Using Cisco TMS with SIP For SIP it is recommended that you follow the above procedure of ensuring meeting IDs do not conflict between MCUs because service prefixes are not supported in SIP. It is also recommended that conference SIP registration is enabled. To do this: In Cisco TMS, go to Systems and select the MCU in the left hand pane. Click Settings and then Extended settings . For Conference sip registration , select On . Click Save . This article applies to the following products: Cisco TelePresence MCU 4200 / MSE 8420 Cisco TelePresence MCU 4500 Cisco TelePresence MSE 8510 blade Cisco TelePresence Management Suite May 3rd, 2011 TAA_KB_288 | May 3rd, 2011 | TAA_KB_288 |  |
|---|---|---|---|
| May 3rd, 2011 | TAA_KB_288 |

| May 3rd, 2011 | TAA_KB_288 |
|---|---|