---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-010011--5bf2121366
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_010011.html
retrieved_at: 2026-08-17T02:29:39.654007+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

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

## SpeechView
                        	 Services are Not Working

If the SpeechView services are not working on Unity Connection,
                           		confirm whether the Unity Connection is registered with CSSM or satellite and
                           		the required licenses for SpeechView are obtained on Unity Connection.