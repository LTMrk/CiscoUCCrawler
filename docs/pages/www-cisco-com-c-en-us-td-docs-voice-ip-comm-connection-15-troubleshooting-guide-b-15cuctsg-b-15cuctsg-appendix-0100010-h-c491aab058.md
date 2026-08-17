---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-appendix-0100010-h-c491aab058
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_appendix_0100010.html
retrieved_at: 2026-08-17T02:40:39.573862+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting
	 SNMP

## Chapter: Troubleshooting
	 SNMP

# Troubleshooting
                     	 SNMP

Cisco Unity Connection supports
                        		Simple Network Management Protocol (SNMP) to provide standard network
                        		management. Unity Connection SNMP uses the SNMP Master Agent service in Cisco
                        		Unified Serviceability and the Unity Connection SNMP Agent service in Cisco
                        		Unity Connection Serviceability.

## Problems with
                        	 SNMP

Use the troubleshooting information
                           		in this section if you experience problems with SNMP.

SNMP Master Agent Service Not Running

The SNMP Master Agent service in Cisco Unified Serviceability runs as
                           		the master agent. Do the following procedure to confirm that the service is
                           		running.

### To Confirm That
                           	 the SNMP Master Agent Service Is Running

Step 1

In Cisco Unified
                                          			 Serviceability, on the Tools menu, select Control Center - Network Services .

Step 2

On the Control Center -
                                          			 Network Services page, under Platform Services, confirm that the status of the
                                          			 SNMP Master Agent service is Started .

Step 3

If the status is not Started,
                                          			 select SNMP Master Agent and select Restart .

### Connection SNMP Agent Service Not Running

The Connection SNMP Agent service in Cisco Unity Connection
                                 		  Serviceability runs as a subagent. Do the following procedure to confirm that
                                 		  the service is running.

To Confirm That the Unity Connection SNMP Agent Service Is Running

Step 1

In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Service Management .

Step 2

On the Control Center - Feature Services page, under Base
                                          			 Services, confirm that the Connection SNMP Agent service status is Started . If the service status is Stopped, select Start .

### SNMP Community
                           	 String Configured Incorrectly

The SNMP community
                                 		  string must be configured for SNMP to function correctly. Do the following
                                 		  procedure to confirm that the SNMP community string is configured correctly.

To Confirm That the SNMP
                                    			 Community String Is Configured Correctly

Step 1

In Cisco
                                          			 Unified Serviceability, on the SNMP menu, select V1/V2 > Community String .

Step 2

On the SNMP
                                          			 Community String Configuration page, select Find .

Step 3

If an SNMP community string appears, select the name. If there is
                                          			 no SNMP community string, select Add New .

Step 4

Enter any applicable settings and verify the settings.

Step 5

Select Save .

Step 6

When prompted that the SNMP Master Agent service is restarted,
                                          			 select OK .

## Using Traces to
                        	 Troubleshoot SNMP Issues

You can use traces to troubleshoot
                           		SNMP issues. For detailed instructions on enabling the applicable traces and
                           		viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting

| Note | Unity Connection SNMP supports CISCO-UNITY-MIB from Cisco Unity. |
|---|---|

| Step 1 | In Cisco Unified
                                          			 Serviceability, on the Tools menu, select Control Center - Network Services . |
|---|---|
| Step 2 | On the Control Center -
                                          			 Network Services page, under Platform Services, confirm that the status of the
                                          			 SNMP Master Agent service is Started . |
| Step 3 | If the status is not Started,
                                          			 select SNMP Master Agent and select Restart . |

| Step 1 | In Cisco Unity Connection Serviceability, on the Tools menu,
                                          			 select Service Management . |
|---|---|
| Step 2 | On the Control Center - Feature Services page, under Base
                                          			 Services, confirm that the Connection SNMP Agent service status is Started . If the service status is Stopped, select Start . |

| Step 1 | In Cisco
                                          			 Unified Serviceability, on the SNMP menu, select V1/V2 > Community String . |
|---|---|
| Step 2 | On the SNMP
                                          			 Community String Configuration page, select Find . |
| Step 3 | If an SNMP community string appears, select the name. If there is
                                          			 no SNMP community string, select Add New . |
| Step 4 | Enter any applicable settings and verify the settings. |
| Step 5 | Select Save . |
| Step 6 | When prompted that the SNMP Master Agent service is restarted,
                                          			 select OK . |