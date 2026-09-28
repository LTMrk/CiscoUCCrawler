---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-010011-htm-482a5c25d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_010011.html
retrieved_at: 2026-08-17T02:39:35.732359+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting Licensing

## Chapter: Troubleshooting Licensing

# Troubleshooting Licensing

Troubleshooting Licensing

## Troubleshooting
                        	 Cisco Smart Software Licensing

This chapter explains various problems that may occur while using Cisco
                           		Smart Software Licensing in Unity connection with the resolution. To use Smart
                           		Licensing in Cisco Unity Connection, you must register the product with Cisco
                           		Smart Software Manager (CSSM) or Cisco Smart Software Manager satellite.

Following issues may occur while configuring or using Cisco Smart
                           		Software Licensing in Unity Connection:

Registration, Reregistration, Renew Authorization, Renew
                                       				Registration or Deregistration Failed with "Communication Timeout - Will
                                       				Reattempt Automatically" error message.

If you get the "Communication Timeout - Will Reattempt
                                    			 Automatically" error message while performing the Registration, Reregistration,
                                    			 Renew Authorization, Renew Registration or Deregistration, verify the
                                    			 following:

- Make sure you have
                                          				entered a valid URL or proxy server on Transport Settings window to communicate
                                          				with CSSM or satellite.

- Make sure "Connection
                                          				Smart License Manager Server" service is up and running.

- Make sure the CSSM
                                          				server is reachable.

Registration or Reregistration Failed with "The Product Instance
                                       				Registration Token you entered is invalid or has expired. Ensure that you have
                                       				pasted the entire token and that the token has not expired." error message.

If you get the "The Product Instance Registration Token you entered
                                    			 is invalid or has expired. Ensure that you have pasted the entire token and
                                    			 that the token has not expired." error message while registering or
                                    			 reregistering the Unity Connection with CSSM or satellite, verify the
                                    			 following:

- Make sure you have
                                          				entered a valid token to register the product with CSSM or satellite.

When you reregister the Unity Connection with CSSM or satellite
                                             				  using wrong or expired token, the reregistration failed and the previous state
                                             				  of the product is changed. In this case, a warning sign with "The last attempt
                                             				  to renew Smart Software Licensing registration failed for the following reason:
                                             				  The Product Instance Registration Token you entered is invalid or has expired.
                                             				  Ensure that you have pasted the entire token and that the token has not
                                             				  expired." error message appears in the Registration Status and License
                                             				  Authorization Status field on the Licenses page of Cisco Unity Connection
                                             				  Administration.

To resolve this issue, you must perform the Renew Registration Now and Renew Authorization Now actions on the Licenses page to get back the Unity Connection
                                             				  in the previous state.

Restart of Connection Smart License Manager Server after switching from Call Home to Smart Transport failed with the following
                                       message:

"Transport mode is successfully updated to Smart Transport. Restart the Connection Smart License Manager Server service on
                                       all the nodes in the cluster to establish connection with Smart Transport."

After you click the Switch button, the Connection Smart License Manager Server service will attempt to restart automatically.
                                    If the service does not restart automatically, an alert message will appear. If you receive an alert, you will have to restart
                                    the Connection Smart License Manager Server service on all Unity Connection server nodes to establish the connection with
                                    Smart Transport. To restart the service, contact Cisco TAC.

## SpeechView
                        	 Services are Not Working

If the SpeechView services are not working on Unity Connection,
                           		confirm whether the Unity Connection is registered with CSSM or satellite and
                           		the required licenses for SpeechView are obtained on Unity Connection.