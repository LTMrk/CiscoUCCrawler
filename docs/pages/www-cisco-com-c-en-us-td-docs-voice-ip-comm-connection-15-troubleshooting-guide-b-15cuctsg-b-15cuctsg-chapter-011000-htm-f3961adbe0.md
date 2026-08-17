---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-011000-htm-f3961adbe0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_011000.html
retrieved_at: 2026-08-17T02:40:01.444347+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting Reports

## Chapter: Troubleshooting Reports

# Troubleshooting Reports

Troubleshooting Reports

## Overview

When no data appears in the reports that you generate, use the
                           		following task list to determine the cause and to resolve the problem:

Confirm that the Unity Connection Reports Data Harvester service
                                 			 is running. See the “Confirm
                                    				Connection Reports Data Harvester Service is Running” section on
                                    				page 25-1 .

Adjust the report data collection cycle. See the “Adjusting
                                    				Report Data Collection Cycle” section on page 25-2 .

Use traces to troubleshoot reports. For detailed instructions on
                                 			 enabling the applicable traces and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting section.

For information about the available reports and how to generate reports, see the “ Using Reports ” chapter of the Administration Guide for Cisco Unity Connection Serviceability Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html .

## Confirming
                        	 Connection Reports Data Harvester Service is Running

Step 1

In Cisco Unity Connection Serviceability, expand Tools menu,
                                       			 select Service Management .

Step 2

On the Control Center – Feature Services page, under Optional
                                       			 Services, locate the Connection Reports Data Harvester service.

Step 3

Confirm that the activate status for the Connection Reports Data
                                       			 Harvester service is Activated . If the activate status is Deactivated,
                                       			 select Activate .

Step 4

Confirm that the service status for the Connection Reports Data
                                       			 Harvester service is Started . If the service status is Stopped, select Start .

Step 5

Confirm that the running time for the Connection Reports Data
                                       			 Harvester service is greater than 00:00:00. If the running time is 00:00:00,
                                       			 turn off the Connection Reports Data Harvester service, then repeat Step 3 and Step 4 .

## Adjusting Report
                        	 Data Collection Cycle

Step 1

If the
                                          				value of the Data Collection Cycle field is too high, the data may not have
                                          				been collected yet for the report because the time between each cycle of
                                          				collecting data is too long.

Step 2

In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Reports .

Step 3

On the Report Configuration page, in the Minutes Between Data
                                       			 Collection Cycles field, enter the time (in minutes) that you want between each
                                       			 cycle of collecting data for the reports. The default is 30 minutes.

Step 4

Select Save .

| Step 1 | In Cisco Unity Connection Serviceability, expand Tools menu,
                                       			 select Service Management . |
|---|---|
| Step 2 | On the Control Center – Feature Services page, under Optional
                                       			 Services, locate the Connection Reports Data Harvester service. |
| Step 3 | Confirm that the activate status for the Connection Reports Data
                                       			 Harvester service is Activated . If the activate status is Deactivated,
                                       			 select Activate . |
| Step 4 | Confirm that the service status for the Connection Reports Data
                                       			 Harvester service is Started . If the service status is Stopped, select Start . |
| Step 5 | Confirm that the running time for the Connection Reports Data
                                       			 Harvester service is greater than 00:00:00. If the running time is 00:00:00,
                                       			 turn off the Connection Reports Data Harvester service, then repeat Step 3 and Step 4 . |

| Step 1 | If the
                                          				value of the Data Collection Cycle field is too high, the data may not have
                                          				been collected yet for the report because the time between each cycle of
                                          				collecting data is too long. |
|---|---|
| Step 2 | In Cisco Unity Connection Administration, expand System Settings , then select Advanced > Reports . |
| Step 3 | On the Report Configuration page, in the Minutes Between Data
                                       			 Collection Cycles field, enter the time (in minutes) that you want between each
                                       			 cycle of collecting data for the reports. The default is 30 minutes. |
| Step 4 | Select Save . |