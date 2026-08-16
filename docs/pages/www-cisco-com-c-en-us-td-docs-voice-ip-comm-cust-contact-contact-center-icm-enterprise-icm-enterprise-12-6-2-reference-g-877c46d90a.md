---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-reference-g-877c46d90a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/reference/guide/ucce_b_acd-supplement-guide-for-avaya-12_6_2/ucce_m_cvlan_tsapi_migration-12_5.html
retrieved_at: 2026-08-16T19:45:57.784976+00:00
---

Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(2)

# Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.6(2)

Updated: April 28, 2023

Chapter: CVLAN to TSAPI Migration

## Chapter: CVLAN to TSAPI Migration

# CVLAN to TSAPI Migration

## Migration Overview

12.6(1) is the last supported release in the 12.6 release train for the Unified ICM peripheral gateway integration with Avaya Communications Manager using the ECS PIM / CVLAN
                           interface peripheral gateway. Migrate your existing Avaya PGs from the CVLAN interface to the TSAPI interface. However, you
                           are not required to reconfigure the skill groups, services, PGs, and agents for the Avaya PGs that you are planning to migrate.

## Important Considerations for Migration

Consider the following before you migrate your Avaya PGs to the TSAPI interface:

Ensure that you download the TSAPI client from the Avaya Support website or from the Avaya DevConnect website.

Install the downloaded TSAPI client before you start the peripheral gateway service. For instructions about installing TSAPI
                                 client, see the Installing TSAPI Client section.

Use the same interface type that is TSAPI for all the PIMs under the peripheral gateway.

Secured TSAPI links are not supported.

By default, TAESPIM supports up to a maximum of ten-digit agent extension.

TAESPIM can process the Universal Call Identifier (UCID) that is received from the switch when certain events such as service
                                 initiated, delivered, and so on, are triggered. The UCID is stored in the CallReferenceID column of the Termination_Call_Details
                                 table and is also added as Peripheral Variable 7.

To avoid reporting the UCID in the Peripheral Variable, set the value of the DisableUCIDinPV attribute to 1. You must create the DWORD registry under the PIM dynamic registry hive.

Let us take a conference call scenario as an example to see how Avaya reports the UCID and also how the UCID numbering model
                                 and the Computer-Supported Telecommunications Applications (CSTA) event call ID are arrived.

Customer A calls an agent B.

1000

1

Agent B initiates a conference call to consult with the supervisor C.

1001

2

Agent B completes the conference call with the supervisor C and continues the call with the customer A.

1001

1

In this scenario, the call model for the CSTA event call ID is 1-2-2 and the call model for UCID is 1-2-1.

As other parties are added to the conference call and new calls are created, the original UCID 1 continues to survive and
                                 appears in all the conference event. Therefore, the UCID 1 is included in all legs of a conference call to tie them all together.

## Migrating CVLAN Interface to TSAPI Interface

To migrate your existing Avaya PGs to the TSAPI interface:

Step 1

Create TSAPI links on the Application Enablement Services (AES) server. See the Follow the procedure to establish the TSAPI link: section in Setting up the TSAPI Links on AES Server .

Step 2

Create a CTI user in AES. The TSAPI PG uses this CTI user to connect to the AES server over TSAPI. See the Add CTI User in AES section in Setting up the TSAPI Links on AES Server .

Step 3

In the PIM Configuration UI, switch the Interface Type option from CVLAN to TSAPI and enter the required details to finish the setup. See PIM Configuration .

Step 4

Ensure that you have set up the peer side of the PG to use the TSAPI interface.

Step 5

Configure all post-route VDNs as dialed numbers in the Unified ICM configuration. This is to register the TSAPI PIM as the
                                       routing server for these VDNs. The PIM sends the route registration request to AES server for these dialed numbers.

The Avaya PIM automatically sends the registration request for Translation Route Dialed Number Identification Service (DNIS)
                                                      numbers, configured in Unified ICM via the Translation Route Explorer tool. They should not be configured as Dialed Numbers in Unified ICM to prevent route registration errors that can impact call processing.

## Trace Bits to Troubleshoot TSAPI PG Issues

Use the trace bits in the TAESPIM procmon interface to troubleshoot TSAPI PG issues. To enable the trace bits, from the diagnostic
                           framework, set the debug level to 3. The following is the list of trace bits:

Trace Bits

Description

monitor_unsolicited_msgs

Prints all the monitoring-related unsolicited events.

monitor_request_msgs

Prints all the monitor requests.

monitor_resp_msgs

Prints the successful confirmation or the universal failure of all the monitor requests from the switch.

value_query_request_msgs

Prints all the value query requests towards the switch.

value_query_resp_msgs

Prints the successful confirmation or the universal failure of all the value query requests.

tsapi_msgs

This is a high-level trace command that you must use along with the other trace commands at the TSAPILib-level.

tsapi_internal_msgs

Prints all the traces that are related to the interaction between the TSAPILib and the Avaya Client library.

```
PG2B-pim1 Trace: [TSAPILIB] Succesfully connected to TSAPI Server [AVAYA#ACM6ENV1#CSTA#AESENV2]
```

| Note | To avoid reporting the UCID in the Peripheral Variable, set the value of the DisableUCIDinPV attribute to 1. You must create the DWORD registry under the PIM dynamic registry hive. |
|---|---|

| Conference Call | CSTA Event Call ID | UCID |
|---|---|---|
| Customer A calls an agent B. | 1000 | 1 |
| Agent B initiates a conference call to consult with the supervisor C. | 1001 | 2 |
| Agent B completes the conference call with the supervisor C and continues the call with the customer A. | 1001 | 1 |

| Step 1 | Create TSAPI links on the Application Enablement Services (AES) server. See the Follow the procedure to establish the TSAPI link: section in Setting up the TSAPI Links on AES Server . |
|---|---|
| Step 2 | Create a CTI user in AES. The TSAPI PG uses this CTI user to connect to the AES server over TSAPI. See the Add CTI User in AES section in Setting up the TSAPI Links on AES Server . |
| Step 3 | In the PIM Configuration UI, switch the Interface Type option from CVLAN to TSAPI and enter the required details to finish the setup. See PIM Configuration . |
| Step 4 | Ensure that you have set up the peer side of the PG to use the TSAPI interface. |
| Step 5 | Configure all post-route VDNs as dialed numbers in the Unified ICM configuration. This is to register the TSAPI PIM as the
                                       routing server for these VDNs. The PIM sends the route registration request to AES server for these dialed numbers. Note The Avaya PIM automatically sends the registration request for Translation Route Dialed Number Identification Service (DNIS)
                                                      numbers, configured in Unified ICM via the Translation Route Explorer tool. They should not be configured as Dialed Numbers in Unified ICM to prevent route registration errors that can impact call processing. | Note | The Avaya PIM automatically sends the registration request for Translation Route Dialed Number Identification Service (DNIS)
                                                      numbers, configured in Unified ICM via the Translation Route Explorer tool. They should not be configured as Dialed Numbers in Unified ICM to prevent route registration errors that can impact call processing. |
| Note | The Avaya PIM automatically sends the registration request for Translation Route Dialed Number Identification Service (DNIS)
                                                      numbers, configured in Unified ICM via the Translation Route Explorer tool. They should not be configured as Dialed Numbers in Unified ICM to prevent route registration errors that can impact call processing. |

| Note | The Avaya PIM automatically sends the registration request for Translation Route Dialed Number Identification Service (DNIS)
                                                      numbers, configured in Unified ICM via the Translation Route Explorer tool. They should not be configured as Dialed Numbers in Unified ICM to prevent route registration errors that can impact call processing. |
|---|---|

| Trace Bits | Description |
|---|---|
| monitor_unsolicited_msgs | Prints all the monitoring-related unsolicited events. |
| monitor_request_msgs | Prints all the monitor requests. |
| monitor_resp_msgs | Prints the successful confirmation or the universal failure of all the monitor requests from the switch. |
| value_query_request_msgs | Prints all the value query requests towards the switch. |
| value_query_resp_msgs | Prints the successful confirmation or the universal failure of all the value query requests. |
| tsapi_msgs | This is a high-level trace command that you must use along with the other trace commands at the TSAPILib-level. |
| tsapi_internal_msgs | Prints all the traces that are related to the interaction between the TSAPILib and the Avaya Client library. |

| Note | All the TSAPI library-level traces are prefixed with [TSAPILIB] in the PIM logs. For example: PG2B-pim1 Trace: [TSAPILIB] Succesfully connected to TSAPI Server [AVAYA#ACM6ENV1#CSTA#AESENV2] |
|---|---|