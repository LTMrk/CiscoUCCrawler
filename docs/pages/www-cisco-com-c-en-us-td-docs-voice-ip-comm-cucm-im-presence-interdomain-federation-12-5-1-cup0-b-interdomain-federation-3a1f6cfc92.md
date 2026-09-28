---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-interdomain-federation-12-5-1-cup0-b-interdomain-federation-3a1f6cfc92
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/interdomain_federation/12_5_1/cup0_b_interdomain-federation-1251/cup0_b_interdomain-federation-1251_chapter_010000.html
retrieved_at: 2026-08-16T17:22:41.127306+00:00
---

Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

# Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

Updated: January 22, 2024

Chapter: Serviceability Configuration for Federation

## Chapter: Serviceability Configuration for Federation

# Serviceability Configuration for Federation

This section provides information on Serviceability Configuration for Federation.

## Use of Logging for Federation

This section explains the Use of Logging for Federation.

### Location of Log Files for SIP Federation

The following log files are applicable for SIP federation:

sip-cm-3_0000000X.log located in /var/log/active/epas/trace/xcp/log

esp0000000X.log located in /var/log/active/epas/trace/esp/sdi

You can also capture these logs from RTMT.

### Location of Log File for XMPP Federation

The following log file  applies to XMPP federation:

xmpp-cm-4_0000000X.log located in /var/log/active/epas/trace/xcp/log

You can also capture logs from RTMT.

### Turn On Logging for Federation

Step 1

Log on to the Cisco Unified
                                             				  IM and
                                             			 Presence Serviceability user interface. Choose Trace > Configuration .

Step 2

From the Server drop-down list, chose the IM and Presence Service server, and click Go .

Step 3

from the Service Group list box, choose IM and
                                             			 Presence Services , and click Go .

Step 4

Perform one of the following steps:

For SIP federation, choose the Cisco XCP SIP Federation
                                                				  Connection Manager service from the Service drop-down list, and click Go .

For XMPP federation, choose the Cisco XCP XMPP Federation
                                                				  Connection Manager service from the Service drop-down list, and click Go .

Step 5

Click Trace On .

Choose the Debug Trace Level in the Trace Filter Settings. If you
                                             				want to enable Debug level on the traces choose Debug for Debug Trace Level.

## How to Restart the Cisco XCP Router

This section provides information on How to Restart the Cisco XCP Router.

### Cisco XCP Router

If you make any configuration changes for SIP or XMPP federation configuration, you must restart the Cisco XCP Router on the IM and Presence Service . If you restart the Cisco XCP Router, the IM and Presence Service automatically restarts all active XCP services.

Note that you must restart the Cisco XCP Router, not turn off and turn on the Cisco XCP Router. If you turn off the Cisco
                                 XCP Router, rather than restart this service, the IM and Presence Service stops all other XCP services. Subsequently when you then turn on the XCP router, the IM and Presence Service does not automatically turn on the other XCP services; you need to manually turn on the other XCP services.

### Restart Cisco XCP Router

Step 1

Log in to the Cisco Unified
                                             				  IM and
                                             			 Presence Serviceability user interface. Choose Tools > Control Center
                                                				  - Network Services .

Step 2

From the Server drop-down list, choose  the server.

Step 3

Click Go .

Step 4

In the IM and Presence Service area, click the radio button next to the Cisco XCP Router service.

Step 5

Click Restart .

Step 6

Click OK when a message indicates that restarting
                                          			 may take a while.

| Step 1 | Log on to the Cisco Unified
                                             				  IM and
                                             			 Presence Serviceability user interface. Choose Trace > Configuration . |
|---|---|
| Step 2 | From the Server drop-down list, chose the IM and Presence Service server, and click Go . |
| Step 3 | from the Service Group list box, choose IM and
                                             			 Presence Services , and click Go . |
| Step 4 | Perform one of the following steps: For SIP federation, choose the Cisco XCP SIP Federation
                                                				  Connection Manager service from the Service drop-down list, and click Go . For XMPP federation, choose the Cisco XCP XMPP Federation
                                                				  Connection Manager service from the Service drop-down list, and click Go . |
| Step 5 | Click Trace On . Choose the Debug Trace Level in the Trace Filter Settings. If you
                                             				want to enable Debug level on the traces choose Debug for Debug Trace Level. |

| Step 1 | Log in to the Cisco Unified
                                             				  IM and
                                             			 Presence Serviceability user interface. Choose Tools > Control Center
                                                				  - Network Services . |
|---|---|
| Step 2 | From the Server drop-down list, choose  the server. |
| Step 3 | Click Go . |
| Step 4 | In the IM and Presence Service area, click the radio button next to the Cisco XCP Router service. |
| Step 5 | Click Restart . |
| Step 6 | Click OK when a message indicates that restarting
                                          			 may take a while. |