---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-interdomain-federation-12-5-1-cup0-b-interdomain-federation-e128812b04
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/interdomain_federation/12_5_1/cup0_b_interdomain-federation-1251/cup0_b_interdomain-federation-1251_chapter_010001.html
retrieved_at: 2026-08-16T17:22:45.166307+00:00
---

Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

# Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

Updated: January 22, 2024

Chapter: Federation Integration Verification

## Chapter: Federation Integration Verification

- Federation Integration Verification

- Verify SIP Federation Configuration

- Verify XMPP Federation Configuration

# Federation Integration Verification

This section describes the Federation Integration Verification.

## Verify SIP Federation Configuration

This procedure describes how to verify the configuration for a federated network between a IM and Presence Service enterprise deployment, and a Microsoft OCS enterprise deployment. Use this procedure as a guide for verifying the other types
                              of integrations if necessary.

If there are multiple local IM and Presence Service domains, re-run this procedure for a user in each local domain.

Step 1

Log on to the Cisco Jabber client or the third-party XMPP client.

Step 2

Log on to two federated Microsoft Office Communicator clients.

Step 3

Perform the following steps on the first Microsoft Office Communicator client:

Add the IM and Presence Service user as a contact.

A pop-up message displays on IM and Presence Service requesting that you accept or block or ignore the presence subscription of Microsoft Office Communicator user.

Check that the IM and Presence Service user and the Microsoft Office Communicator user are able to see each other's availability.

Step 4

Perform the following steps on the client of the IM and Presence Service client:

Add the second Microsoft Office Communicator user as a contact.

Check that you can see the availability of the Microsoft Office Communicator user.

A pop-up message should appear on the user client for the Microsoft Office Communicator user informing you that the Cisco Jabber user has been added as a contact.

Step 5

Toggle between the availability states on both the clients of the IM and Presence Service user and the Microsoft Office Communicator clients. Check that the availability state changes for the contacts on each client.

Step 6

Initiate an IM from the client of a IM and Presence Service user to a Microsoft Office Communicator user.

Step 7

Check that the IM window appears on Microsoft Office Communicator with the message from the IM and Presence Service user.

Step 8

Close both the IM window on the client of the IM and Presence Service user and IM window on the Microsoft Office Communicator client.

Step 9

Initiate an IM from Microsoft Office Communicator user to the IM and Presence Service user.

Step 10

Check that an IM window appears on the client of the IM and Presence Service user with the message from the Microsoft Office Communicator user.

Step 11

On the Cisco Jabber client, perform the following steps:

Block one of the Microsoft Office Communicator users.

Any third-party clients that do not support XEP-0016 - Privacy Lists, if you block from a third-party XMPP client, you only
                                                            block IM; users can still exchange availability status. To block server-side IM and availability, the user configures their
                                                            privacy settings from the IM and Presence Users Options interface, or from the Privacy configuration on Cisco Jabber .

Check that this Microsoft Office Communicator user now sees that the availability of the IM and Presence Service user as offline. The second Microsoft Office Communicator user should still be able to see availability status for the IM and Presence Service user.

On the client of the IM and Presence Service user, the blocked Microsoft Office Communicator user should still appear online, and you should be able to initiate an IM
                                             to the blocked Microsoft Office Communicator user.

Step 12

Block the IM and Presence Service user from the Microsoft Office Communicator client.

Step 13

Verify that the presence of the Microsoft Office Communicator user is no longer available on the client of the IM and Presence Service user.

## Verify XMPP Federation Configuration

This procedure describes how to verify the configuration for a federated network between an IM and Presence Service Release 9.0 enterprise deployment, and either a WebEx, an IBM Sametime, or another IM and Presence Service Release 9.0 enterprise deployment. The procedure below describes the procedure for an IM and Presence Service Release 9.0 and a WebEx deployment. Use this procedure as a guide to verify the other types of XMPP federations.

If there are multiple local IM and Presence Service domains, re-run this procedure for a user in each local domain.

Step 1

Log on to the Cisco Jabber client or the third-party XMPP client connected to the IM and Presence Service Release 9.0 server.

Step 2

Log on to two federated WebEx Connect clients.

Step 3

Perform the following steps on the first WebEx Connect client:

Add the IM and Presence Service user as a contact.

A pop-up message displays on client of the IM and Presence Service user requesting that you accept or block or ignore the presence subscription from the WebEx Connect user. Accept the subscription.

Check that the IM and Presence Service user and the WebEx Connect user are able to see each other's availability.

Step 4

Perform the following steps on the client of the IM and Presence Service user:

Add the second WebEx Connect user as a contact.

A pop-up should appear on the WebEx Connect client. Accept the subscription.

Check that you can see the availability of the WebEx Connect user.

Step 5

Toggle between the availability states on both the client of the IM and Presence Service user and the WebEx Connect client. Check that the availability state changes for the contacts on each client.

Step 6

Initiate an IM from the client of the IM and Presence Service user to a WebEx Connect contact.

Step 7

Check that the IM window displays on WebEx Connect client with the IM from the IM and Presence Service user.

Step 8

Close the IM window on both clients.

Step 9

Initiate an IM from the WebEx Connect user to the IM and Presence Service user.

Step 10

Check that an IM window displays on the client of the IM and Presence Service user with the IM from the WebEx Connect user.

Step 11

On the client of the IM and Presence Service user, perform the following steps:

Block one of WebEx Connect users.

If you block from a third-party XMPP client, you only block IM; users can still exchange availability status. To block server-side
                                                            IM and availability, the user configures their privacy settings from the IM and Presence Users Options interface, or from
                                                            the Privacy configuration on Cisco Jabber .

Check that this WebEx Connect user now sees that the availability of the IM and Presence Service user as offline. The second WebEx Connect user should still be able to see availability status for the IM and Presence Service user.

On the client of the IM and Presence Service user, the blocked WebEx Connect user should still appear as online, however you cannot send an IM to the blocked WebEx Connect
                                             user.

Step 12

Block the IM and Presence Service user from the WebEx Connect client.

Step 13

Verify that the availability of the WebEx Connect user is no longer available on the client of the IM and Presence Service user.

| Note | If there are multiple local IM and Presence Service domains, re-run this procedure for a user in each local domain. |
|---|---|

| Step 1 | Log on to the Cisco Jabber client or the third-party XMPP client. |
|---|---|
| Step 2 | Log on to two federated Microsoft Office Communicator clients. |
| Step 3 | Perform the following steps on the first Microsoft Office Communicator client: Add the IM and Presence Service user as a contact. A pop-up message displays on IM and Presence Service requesting that you accept or block or ignore the presence subscription of Microsoft Office Communicator user. Check that the IM and Presence Service user and the Microsoft Office Communicator user are able to see each other's availability. |
| Step 4 | Perform the following steps on the client of the IM and Presence Service client: Add the second Microsoft Office Communicator user as a contact. Check that you can see the availability of the Microsoft Office Communicator user. A pop-up message should appear on the user client for the Microsoft Office Communicator user informing you that the Cisco Jabber user has been added as a contact. |
| Step 5 | Toggle between the availability states on both the clients of the IM and Presence Service user and the Microsoft Office Communicator clients. Check that the availability state changes for the contacts on each client. |
| Step 6 | Initiate an IM from the client of a IM and Presence Service user to a Microsoft Office Communicator user. |
| Step 7 | Check that the IM window appears on Microsoft Office Communicator with the message from the IM and Presence Service user. |
| Step 8 | Close both the IM window on the client of the IM and Presence Service user and IM window on the Microsoft Office Communicator client. |
| Step 9 | Initiate an IM from Microsoft Office Communicator user to the IM and Presence Service user. |
| Step 10 | Check that an IM window appears on the client of the IM and Presence Service user with the message from the Microsoft Office Communicator user. |
| Step 11 | On the Cisco Jabber client, perform the following steps: Block one of the Microsoft Office Communicator users. Note Any third-party clients that do not support XEP-0016 - Privacy Lists, if you block from a third-party XMPP client, you only
                                                            block IM; users can still exchange availability status. To block server-side IM and availability, the user configures their
                                                            privacy settings from the IM and Presence Users Options interface, or from the Privacy configuration on Cisco Jabber . Check that this Microsoft Office Communicator user now sees that the availability of the IM and Presence Service user as offline. The second Microsoft Office Communicator user should still be able to see availability status for the IM and Presence Service user. On the client of the IM and Presence Service user, the blocked Microsoft Office Communicator user should still appear online, and you should be able to initiate an IM
                                             to the blocked Microsoft Office Communicator user. | Note | Any third-party clients that do not support XEP-0016 - Privacy Lists, if you block from a third-party XMPP client, you only
                                                            block IM; users can still exchange availability status. To block server-side IM and availability, the user configures their
                                                            privacy settings from the IM and Presence Users Options interface, or from the Privacy configuration on Cisco Jabber . |
| Note | Any third-party clients that do not support XEP-0016 - Privacy Lists, if you block from a third-party XMPP client, you only
                                                            block IM; users can still exchange availability status. To block server-side IM and availability, the user configures their
                                                            privacy settings from the IM and Presence Users Options interface, or from the Privacy configuration on Cisco Jabber . |
| Step 12 | Block the IM and Presence Service user from the Microsoft Office Communicator client. |
| Step 13 | Verify that the presence of the Microsoft Office Communicator user is no longer available on the client of the IM and Presence Service user. |

| Note | Any third-party clients that do not support XEP-0016 - Privacy Lists, if you block from a third-party XMPP client, you only
                                                            block IM; users can still exchange availability status. To block server-side IM and availability, the user configures their
                                                            privacy settings from the IM and Presence Users Options interface, or from the Privacy configuration on Cisco Jabber . |
|---|---|

| Note | If there are multiple local IM and Presence Service domains, re-run this procedure for a user in each local domain. |
|---|---|

| Step 1 | Log on to the Cisco Jabber client or the third-party XMPP client connected to the IM and Presence Service Release 9.0 server. |
|---|---|
| Step 2 | Log on to two federated WebEx Connect clients. |
| Step 3 | Perform the following steps on the first WebEx Connect client: Add the IM and Presence Service user as a contact. A pop-up message displays on client of the IM and Presence Service user requesting that you accept or block or ignore the presence subscription from the WebEx Connect user. Accept the subscription. Check that the IM and Presence Service user and the WebEx Connect user are able to see each other's availability. |
| Step 4 | Perform the following steps on the client of the IM and Presence Service user: Add the second WebEx Connect user as a contact. A pop-up should appear on the WebEx Connect client. Accept the subscription. Check that you can see the availability of the WebEx Connect user. |
| Step 5 | Toggle between the availability states on both the client of the IM and Presence Service user and the WebEx Connect client. Check that the availability state changes for the contacts on each client. |
| Step 6 | Initiate an IM from the client of the IM and Presence Service user to a WebEx Connect contact. |
| Step 7 | Check that the IM window displays on WebEx Connect client with the IM from the IM and Presence Service user. |
| Step 8 | Close the IM window on both clients. |
| Step 9 | Initiate an IM from the WebEx Connect user to the IM and Presence Service user. |
| Step 10 | Check that an IM window displays on the client of the IM and Presence Service user with the IM from the WebEx Connect user. |
| Step 11 | On the client of the IM and Presence Service user, perform the following steps: Block one of WebEx Connect users. Note If you block from a third-party XMPP client, you only block IM; users can still exchange availability status. To block server-side
                                                            IM and availability, the user configures their privacy settings from the IM and Presence Users Options interface, or from
                                                            the Privacy configuration on Cisco Jabber . Check that this WebEx Connect user now sees that the availability of the IM and Presence Service user as offline. The second WebEx Connect user should still be able to see availability status for the IM and Presence Service user. On the client of the IM and Presence Service user, the blocked WebEx Connect user should still appear as online, however you cannot send an IM to the blocked WebEx Connect
                                             user. | Note | If you block from a third-party XMPP client, you only block IM; users can still exchange availability status. To block server-side
                                                            IM and availability, the user configures their privacy settings from the IM and Presence Users Options interface, or from
                                                            the Privacy configuration on Cisco Jabber . |
| Note | If you block from a third-party XMPP client, you only block IM; users can still exchange availability status. To block server-side
                                                            IM and availability, the user configures their privacy settings from the IM and Presence Users Options interface, or from
                                                            the Privacy configuration on Cisco Jabber . |
| Step 12 | Block the IM and Presence Service user from the WebEx Connect client. |
| Step 13 | Verify that the availability of the WebEx Connect user is no longer available on the client of the IM and Presence Service user. |

| Note | If you block from a third-party XMPP client, you only block IM; users can still exchange availability status. To block server-side
                                                            IM and availability, the user configures their privacy settings from the IM and Presence Users Options interface, or from
                                                            the Privacy configuration on Cisco Jabber . |
|---|---|