---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-cucm-sccp-b-15cucintcucmskinny-b-14cucintcucmskinn-6dc39c9331
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/cucm_sccp/b_15cucintcucmskinny/b_14cucintcucmskinny_chapter_0101.html
retrieved_at: 2026-08-16T18:29:11.451712+00:00
---

Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 15

# Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Changing the Number of Voice Messaging Ports

## Chapter: Changing the Number of Voice Messaging Ports

# Changing the Number of Voice Messaging Ports

## Changing the Number of Voice Messaging Ports

### Introduction

To change
                              		the number of voice messaging ports in Cisco Unified Communications Manager and
                              		in Cisco Unity Connection for an existing integration, use Cisco Voice Mail
                              		Port Wizard.

See the following:

To add voice mail ports in Cisco Unified CM Administration
                                    			 through the Cisco Voice Mail Port Wizard, see the Adding Voice Messaging Ports procedure in
                                    			 the chapter for the applicable version of Cisco Unified CM.

To remove voice mail ports in Cisco Unified CM Administration
                                    			 through the Cisco Voice Mail Port Wizard, see the Help on Cisco Unified CM
                                    			 Administration.

#### Adding Voice
                              	 Messaging Ports

The following task list describes the process for Adding Voice
                                    		  Messaging Ports in Cisco Unity Connection Administration

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations and select Port .

The maximum number of voice messaging ports that can be added in
                                                            				  Unity Connection depends on the OVA template of the virtual machine.

Step 2

On the Search Ports page, under Port Search Results, select Add New .

Step 3

On the New Port page, enter the applicable settings and select Save .

Make sure that there are an appropriate number of ports set to
                                                				answer calls and an appropriate number of ports set to dial out. Otherwise, the
                                                				integration does not function correctly. For details, see to the " Planning
                                                   				  the Voice Messaging Ports " chapter.

Step 4

If you are not using Cisco Unified CM authentication and
                                             			 encryption, skip to Step 10 .

If you are using Cisco Unified CM authentication and encryption,
                                                				in Cisco Unity Connection Administration, expand Telephony Integrations > Security , and then select Root Certificate .

Confirm that you have set up the TFTP server on the Edit Servers
                                                				page for the port group to which voice messaging ports belong. Otherwise, the
                                                				integration does not function correctly with Cisco Unified CM authentication
                                                				and encryption.

Step 5

On the View Root Certificate page, Right-select to Save the Certificate as a File link,
                                             			 and select Save Target As .

Step 6

In the Save As dialog box, browse to the location where you want
                                             			 to save the Unity Connection root certificate as a file.

Step 7

For Cisco Unified CM 5.x and later, in the File Name field,
                                             			 confirm that the extension is .pem (rather than .htm), and select Save .

Step 8

In the Download Complete dialog box, select Close .

Step 9

Upload the Unity Connection root certificate to all Cisco
                                             			 Unified CM servers in this Cisco Unified CM phone system integration by doing
                                             			 the following substeps.

Caution

On the Cisco Unified CM server, sign in to Cisco Unified
                                                   				  Operating System Administration.

In Cisco Unified Operating System Administration, on the
                                                   				  Security menu, select Certificate Management .

On the Certificate List page, select Upload Certificate .

On the Upload Certificate page, in the Certificate Name
                                                   				  drop-down box, select CallManager-trust .

In the Root Certificate field, enter Cisco Unity Connection Root Certificate .

To the right of the Upload File field, select Browse .

In the Choose File dialog box, browse to the Cisco Unity
                                                   				  Connection root certificate that you saved in Step 7 .

Follow the on-screen instructions.

Repeat Step 9a. through Step
                                                      					 9h. on all remaining Cisco Unified CM servers in the Cisco Unified CM
                                                   				  cluster.

In Cisco Unity Connection Administration, in the Related Links
                                                   				  drop-down list, select Check Telephony Configuration and select Go to confirm the Unity Connection to the Cisco Unified CM
                                                   				  servers.

If the test is not successful, the Task Results list displays
                                                      					 one or more messages with troubleshooting steps. After correcting the problems,
                                                      					 test the Unity Connection again.

In the Task Results window, select Close .

Step 10

Sign out of Cisco Unity Connection Administration.

#### Deleting Voice Messaging Ports

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Telephony Integrations > and select > Port .

Step 2

In the Search Port page, under Port Search
                                             			 Results, check the check boxes next to the voice messaging ports that you want
                                             			 to delete.

Step 3

Select Delete Selected .

Step 4

For the remaining voice messaging ports in
                                             			 the port group, change the settings as necessary so that there are an
                                             			 appropriate number of voice messaging ports set to answer calls and an
                                             			 appropriate number of voice messaging ports set to dial out.

Step 5

In Cisco Unity Connection Administration, in
                                             			 the Related Links drop-down list, select Check Telephony
                                                				Configuration and select Go to confirm the phone
                                             			 system integration settings.

If the test is not successful, the Task
                                                				Execution Results displays one or more messages with troubleshooting steps.
                                                				After correcting the problems, test the Unity Connection again.

Step 6

In the Task Execution Results window, select Close and sign out of
                                             			 Cisco Unity Connection Administration.

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Port . Note The maximum number of voice messaging ports that can be added in
                                                            				  Unity Connection depends on the OVA template of the virtual machine. | Note | The maximum number of voice messaging ports that can be added in
                                                            				  Unity Connection depends on the OVA template of the virtual machine. |
|---|---|---|---|
| Note | The maximum number of voice messaging ports that can be added in
                                                            				  Unity Connection depends on the OVA template of the virtual machine. |
| Step 2 | On the Search Ports page, under Port Search Results, select Add New . |
| Step 3 | On the New Port page, enter the applicable settings and select Save . Make sure that there are an appropriate number of ports set to
                                                				answer calls and an appropriate number of ports set to dial out. Otherwise, the
                                                				integration does not function correctly. For details, see to the " Planning
                                                   				  the Voice Messaging Ports " chapter. |
| Step 4 | If you are not using Cisco Unified CM authentication and
                                             			 encryption, skip to Step 10 . If you are using Cisco Unified CM authentication and encryption,
                                                				in Cisco Unity Connection Administration, expand Telephony Integrations > Security , and then select Root Certificate . Confirm that you have set up the TFTP server on the Edit Servers
                                                				page for the port group to which voice messaging ports belong. Otherwise, the
                                                				integration does not function correctly with Cisco Unified CM authentication
                                                				and encryption. |
| Step 5 | On the View Root Certificate page, Right-select to Save the Certificate as a File link,
                                             			 and select Save Target As . |
| Step 6 | In the Save As dialog box, browse to the location where you want
                                             			 to save the Unity Connection root certificate as a file. |
| Step 7 | For Cisco Unified CM 5.x and later, in the File Name field,
                                             			 confirm that the extension is .pem (rather than .htm), and select Save . |
| Step 8 | In the Download Complete dialog box, select Close . |
| Step 9 | Upload the Unity Connection root certificate to all Cisco
                                             			 Unified CM servers in this Cisco Unified CM phone system integration by doing
                                             			 the following substeps. Caution The Unity Connection system clock must be
                                                         				synchronized with the Cisco Unified CM system clock for Cisco Unified CM
                                                         				authentication to function immediately. Otherwise, Cisco Unified CM does not
                                                         				let the Cisco Unity Connection voice messaging ports register until the Cisco
                                                         				Unified CM system clock has passed the time stamp in the Unity Connection
                                                         				device certificates. On the Cisco Unified CM server, sign in to Cisco Unified
                                                   				  Operating System Administration. In Cisco Unified Operating System Administration, on the
                                                   				  Security menu, select Certificate Management . On the Certificate List page, select Upload Certificate . On the Upload Certificate page, in the Certificate Name
                                                   				  drop-down box, select CallManager-trust . In the Root Certificate field, enter Cisco Unity Connection Root Certificate . To the right of the Upload File field, select Browse . In the Choose File dialog box, browse to the Cisco Unity
                                                   				  Connection root certificate that you saved in Step 7 . Follow the on-screen instructions. Repeat Step 9a. through Step
                                                      					 9h. on all remaining Cisco Unified CM servers in the Cisco Unified CM
                                                   				  cluster. In Cisco Unity Connection Administration, in the Related Links
                                                   				  drop-down list, select Check Telephony Configuration and select Go to confirm the Unity Connection to the Cisco Unified CM
                                                   				  servers. If the test is not successful, the Task Results list displays
                                                      					 one or more messages with troubleshooting steps. After correcting the problems,
                                                      					 test the Unity Connection again. In the Task Results window, select Close . | Caution | The Unity Connection system clock must be
                                                         				synchronized with the Cisco Unified CM system clock for Cisco Unified CM
                                                         				authentication to function immediately. Otherwise, Cisco Unified CM does not
                                                         				let the Cisco Unity Connection voice messaging ports register until the Cisco
                                                         				Unified CM system clock has passed the time stamp in the Unity Connection
                                                         				device certificates. |
| Caution | The Unity Connection system clock must be
                                                         				synchronized with the Cisco Unified CM system clock for Cisco Unified CM
                                                         				authentication to function immediately. Otherwise, Cisco Unified CM does not
                                                         				let the Cisco Unity Connection voice messaging ports register until the Cisco
                                                         				Unified CM system clock has passed the time stamp in the Unity Connection
                                                         				device certificates. |
| Step 10 | Sign out of Cisco Unity Connection Administration. |

| Note | The maximum number of voice messaging ports that can be added in
                                                            				  Unity Connection depends on the OVA template of the virtual machine. |
|---|---|

| Caution | The Unity Connection system clock must be
                                                         				synchronized with the Cisco Unified CM system clock for Cisco Unified CM
                                                         				authentication to function immediately. Otherwise, Cisco Unified CM does not
                                                         				let the Cisco Unity Connection voice messaging ports register until the Cisco
                                                         				Unified CM system clock has passed the time stamp in the Unity Connection
                                                         				device certificates. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Telephony Integrations > and select > Port . |
|---|---|
| Step 2 | In the Search Port page, under Port Search
                                             			 Results, check the check boxes next to the voice messaging ports that you want
                                             			 to delete. |
| Step 3 | Select Delete Selected . |
| Step 4 | For the remaining voice messaging ports in
                                             			 the port group, change the settings as necessary so that there are an
                                             			 appropriate number of voice messaging ports set to answer calls and an
                                             			 appropriate number of voice messaging ports set to dial out. |
| Step 5 | In Cisco Unity Connection Administration, in
                                             			 the Related Links drop-down list, select Check Telephony
                                                				Configuration and select Go to confirm the phone
                                             			 system integration settings. If the test is not successful, the Task
                                                				Execution Results displays one or more messages with troubleshooting steps.
                                                				After correcting the problems, test the Unity Connection again. |
| Step 6 | In the Task Execution Results window, select Close and sign out of
                                             			 Cisco Unity Connection Administration. |