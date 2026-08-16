---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-messageservice-cmgt-b-spark-hybrid-m-0bd6544a51
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/messageservice/cmgt_b_spark-hybrid-message-deployment-guide/cmgt_b_spark-hybrid-message-deployment-guide_chapter_011.html
retrieved_at: 2026-08-16T15:38:00.578724+00:00
---

Deployment Guide for Hybrid Message

# Deployment Guide for Hybrid Message

Updated: October 4, 2018

Chapter: Manage Hybrid Message Service

## Chapter: Manage Hybrid Message Service

# Manage Hybrid Message Service

## Hybrid Message Status on Expressway

Each Expressway connector host enables part of your Hybrid Message deployment and shows status information about that part only. This is useful if you already know that a specific Expressway
                              is affected by, or responsible for, an issue.

If you are looking for a more general overview of your service status, open your Hybrid Message deployment in Control Hub .

The status information page is at Applications > Hybrid Services > Message Service > Message Service Status . The information shown there falls into the following categories:

Connectivity to Webex

User and usage stats

Connections to IM and Presence Service infrastructure

The status page and this reference topic are ordered by the level of impact that the status item will have on your service.

### Connectivity to Webex

If this status is anything other than "Operational", then there is a problem between this Expressway and Webex . It could be a problem with the Expressway (check Status > Alarms ), the service (check status.webex.com ), or the network between them (check the proxy if you have one, check firewalls allow outbound HTTPS connections, use network
                              diagnostic tools to establish if routes exist).

### Message Service User Totals (this Expressway)

This part of the status page is about the total user populations known to this Expressway cluster. The numbers are common
                              across this connector host cluster, because all nodes in the cluster share the Hybrid Message configuration (where you entered the publisher address and account details).

Users from connected IM and Presence clusters is the count of users that the connector gathers from the directly connected IM and Presence Service infrastructure. These users are "homed" on (or "local" to) the IM and Presence clusters whose publishers' details you entered
                              on this Expressway cluster's primary node.

We need to distinguish this number because, when the connector makes AXL queries to those publishers, the publishers return
                              all the users they know about. This includes 'intercluster' users, which the queried publishers know about because ICSA (Intercluster
                              Sync Agent) is working across multiple IM and Presence clusters.

This number is the theoretical maximum of users that you could have using the service through this connector host cluster.
                              In practice, you would probably enable a smaller subset of these, as part of a migration plan.

Users from all IM and Presence clusters (ICSA) is the count of users known to all IM and Presence clusters that are synchronized (by ICSA) with the publishers you added
                              to the connector configuration. The number includes the count of local users (the previous number in this section). So, when
                              you read the two numbers, you can think of them as, for example, 300 of 1000, if 300 users are homed on the directly connected IM and Presence clusters and 1000 are synchronized between multiple
                              IM and Presence clusters.

You can use the relationship between these numbers to help validate or troubleshoot your Message Service deployment. For example,
                              if you know you should have 1000 synchronized users but the total is less, you may have an intercluster sync agent problem.
                              If you only have one cluster, or if all the IM and Presence publishers are configured on this connector, then the two numbers
                              should be the same. If both numbers are 0, it could indicate an AXL query problem or a message connector configuration problem.

Users Enabled for Hybrid Message Service is the number of Hybrid Message -enabled users that Webex has assigned to this particular Expressway cluster. It is typically smaller than Users from connected IM and Presence clusters .

When you grant the message service to your users in Control Hub , the cloud communicates with the connector hosts to determine which connectors know about those users. The cloud then assigns
                              those users to those connectors in a balanced way.

Active Message Service Users is the count of enabled users that are currently using the Hybrid Message . Users are considered Active if, within the 72 hours leading up to now, they have used Webex App to read or write messages to or from Cisco Jabber. It is also shown as a percentage of Users Enabled for Hybrid Message Service.

Users not Active for 72 Hours or more is the count of enabled users that are not currently using the Hybrid Message . Within the rolling 72 hour period up to now, these users did not use Webex App to read or write messages to or from Jabber. The connector uses this characteristic to improve performance, by deleting any
                              sessions that are held by inactive users. In typical usage across your deployment, you can expect there to be some inactive
                              users (holiday etc.) but the number should typically be lower than the Active users. It is also shown as a percentage of Users
                              Enabled for Hybrid Message Service.

### Message Service Status (IM and Presence Nodes)

This section of the page is about the connector's relationships with directly connected IM and Presence nodes.

For each IM and Presence publisher (the address you entered during configuration) there is at least one discovered node (itself)
                              and there may be up to six in total.

The following status information is shown for each node in each IM and Presence Service cluster:

Node Version is the IM and Presence Service software version, as reported by the particular node.

Node Status should be "Operational". The "Outage" status indicates a problem with that IM and Presence Service node, or the connection to it.

Certificate validation is either On or Off, depending on the choice you made when you connected to this node's publisher. If it's On (default),
                                    then the Expressway must be able to validate the certificate presented by this node, or the Hybrid Message will not work.

Message Service Users from this Node is the count of Hybrid Message -enabled users who are assigned to this connector and are homed on this IM and Presence Service node. Each IM and Presence Service node that is listed on this status page contributes a portion to the total count of Users Enabled for Message Service, shown
                                    near the top of the page.

Active Message Service Users is the count of enabled users that are currently using the Hybrid Message , and are homed on this IM and Presence Service node. Each IM and Presence Service node that is listed on this status page contributes a portion to the total count of Active Message Service Users, shown near
                                    the top of the page.

Users not Active for 72 Hours or more is the count of enabled users that are not currently using the Hybrid Message , and are homed on this IM and Presence Service node. Each IM and Presence Service node that is listed on this status page contributes a portion to the total count of Users not Active for 72 Hours or more,
                                    shown near the top of the page.

## High Availability and Failover

### Controlled Outages of Message Connector Nodes

Before you start maintenance on an Expressway node that is hosting Message Connector, you should move the node into maintenance mode in Control Hub . This enables Cisco Webex to move the users off that node and onto the remaining nodes in the cluster, so that you can do
                              your maintenance.

Cisco Webex does not recognize the Expressway's own maintenance mode. If you take an Expressway out of service in this way,
                              it looks like an uncontrolled outage of that connector to Cisco Webex.

### High Availability Setting on Presence Redundancy Groups

The Message Service connector is aware of the high availability setting. It can respond to manual or automatic failover and
                              fallback events on the IM and Presence nodes.

If you change the group's high availability setting (either on or off) while the group's nodes are participating in Message
                              Service, then you must restart the connector on the associated Expressway.

See https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/200958-IM-and-Presence-Server-High-Availability.html for more on the IM and Presence configuration.

### Controlled Outages of IM and Presence Service Nodes

Before you start maintenance on an IM and Presence Service node, you should manually failover the sessions from that node
                              to the other node in the Presence Redundancy Group.

When you manually fail over one of the IM and Presence nodes in a Presence Redundancy Group, the user sessions from the source
                              node migrate to the other node. The Expressway's Message Service status page reports "Outage" status for the source node,
                              but shows users still assigned to that node.

The Message Connector is rate limited when creating new sessions on the target IM and Presence Service node. The connector
                              could take up to 15 minutes to start transitioning users to the other node, and then progresses at a rate that does not overwhelm
                              the target node. For example, with 5,000 user sessions failing over, you can expect to wait approximately 30 minutes for the
                              service to stabilize after the start of the controlled outage.

Wait until the transition process is complete, then you can do your maintenance on the IM and Presence Service node. Finally,
                              you can manually fallback the sessions to the original node. You can expect a similar wait for the fallback to complete.

### Uncontrolled Outages

The Hybrid Message Service automatically responds to an unexpected failure of an IM and Presence Service node.

As with the controlled outage, the Message Connector is rate limited when creating new sessions on the remaining IM and Presence
                              Service node. The connector could take up to 15 minutes to start transitioning users to the other node, and then progresses
                              at a rate that does not overwhelm the target node. For example, with 5,000 user sessions failing over, you can expect to wait
                              approximately 30 minutes for the service to stabilize after an unexpected failure of one of the IM and Presence nodes.

The service is not robust to other uncontrolled outages, including but not limited to:

Unexpected failure of an Expressway.

Unexpected failure of Message Connector.

Unexpected failure of the IM and Presence services that Hybrid Message Service depends on, including XCP, AXL, and the Presence
                                    Engine.

## Refresh Connections to Unified CM IM and Presence Nodes

The Message Connector uses AXL calls to the IM and Presence publisher to discover the nodes in that cluster. This is a static
                              arrangement and the Message Connector does not dynamically adapt when you change the IM and Presence cluster. For example,
                              when you add or remove nodes.

The Message Connector cannot discover IM and Presence nodes when the AXL service is not running on the nodes. So, if there
                              has been some kind of failure in your deployment, the nodes may not be back up before the Message Connector starts, or the
                              AXL service may not have restarted.

When the Message Connector has not discovered some of the IM and Presence nodes, you can restart the Message Connector to
                              force a rediscovery.

Sign in to the primary peer of the Message Connector Expressway cluster, and go to Applications > Hybrid Services > Connector Management .

Click Message Connector .

Choose Disabled from the Active drop-down list.

Click Save .

The connector stops.

Choose Enabled from the Active drop-down list.

Click Save .

The connector starts and the status changes to Running .

## Troubleshooting Hybrid Message

### Webex Status

If all users are affected, the first thing you should check is whether the Hybrid Message is operational:

Browse to https://status.ciscospark.com/

Expand Webex Hybrid Services > Message Service to read the status.

If the Hybrid Message status is not Operational, we are trying to fix it.

### Service Activation

Sign in to https://admin.webex.com

Does your organization have the Hybrid Message card?

### User Activation

Check Control Hub for user activation problems:

Sign in to https://admin.webex.com

Click Users and find the users you're interested in.

You can sort the list by Status .

Click a username to open that user's configuration.

If there is no Message Service link, you need to onboard the user for Hybrid Message .

Click Message Service .

The slider should be on (to the right position). If it is not, slide it to on and save: the user status goes Pending for a
                                    few seconds and then Active.

If the user status is Error, review the message. Also, click See history to get more information about what is preventing this user's activation.

Correct the problem preventing activation, then come back to the user and click Reactivate User .

If the user status is still not Active, you should raise a case.

### Connector Status

If Hybrid Message is not working for all users, or a large subset, you should check the message connector status on Expressway:

Sign in to the primary peer of the cluster you registered and configured for Hybrid Message .

Go to Applications > Hybrid Services > Connector Management .

Is Management Connector running?

Is message connector running?

Go to Applications > Hybrid Services > Message Service > Message Service Status

Review the page for any errors between the Expressway and the configured IM and Presence Service nodes.

Status should be Operational . There should be users assigned on-premises and subscribed to the cloud. If people are using Hybrid Message , then there should be some percentage of users with active sessions.

Check the IM and Presence Service node configuration on the Expressway:

On the Expressway, go to Applications > Hybrid Services > Message Service > Message Service Configuration .

Check the listed nodes. Are any of the status entries not Active ?

There is a known issue where the software version of the IM and Presence node is not correctly synchronized on the Expressway
                                                after the IM and Presence node is upgraded. This is a purely cosmetic issue as the Message Connector does not use the version
                                                information for any purpose. You can synchronize the IM and Presence version by restarting the Message Connector. We intend
                                                to resolve this issue in a future Message Connector release.

Delete any affected nodes.

Recreate the nodes you deleted. Each time, make sure to correctly enter the address, username, and password, and then save
                                    the configuration.

If the status does not improve, perhaps there is a configuration or connectivity issue on the IM and Presence Service nodes.

### IM and Presence Service Checks

Are the users you are investigating homed on the same IM and Presence Service cluster that is being used with Hybrid Message ?

Does the Message Connector account have the AXL role? Are the username and password of that account the same as what you entered on the Message Connector ?

Users are in Error state in Control Hub, with 'duplicate Mail ID' errors: These users are probably homed on more than one
                                    IM and Presence cluster. This situation could be a result of the way you import users to IM and Presence from Active Directory.
                                    Users should not be homed on multiple IM and Presence clusters. Run the IM And Presence troubleshooter to check for and correct
                                    any duplicate user accounts.

Are the IM and Presence Service nodes running the Cisco AXL Web Service? Go to Cisco Unified IM and Presence Serviceability > Tools > Service Activation to check.

### Per User Checks

If one or two users are affected, try the following checks:

Is the user entitled for Hybrid Message ?

Did the user activation fail the first time? Open the user in Control Hub, open the Hybrid Message Service, and click Reactivate User .

Does the user have an email address (mailid) in IM and Presence administration?

Does the user's email address in IM and Presence match what is in Control Hub ?

Is there a new 'duplicate' Webex user named after the user's Jabber ID (JID)? This could result from searching for a JID in
                                    Webex. When you search for a JID, Webex may create a new space based on the JID, even though there is already an account based
                                    on the same user's email address.

Did you use Directory Connector to import/synchronize users? Check that the LDAP attribute that you mapped to cloud UID contains the user's email address.

For example, if you choose to map UserPrincipalName to cloud UID , then in Active Directory the UserPrincipalName attribute must contain the user's email address.

Are the users correctly entitled in Cisco Webex? The 'Jabber only' users in your organization must be entitled to use the
                                    Message Free service with Webex, even though they are not using Webex, to ensure that they get messages sent via Webex by
                                    Message Service users.

To avoid getting into this situation, we recommend that you assign the Message Free entitlement to all users. You can do this
                                    by configuring an Automatic License Assignment Template in Control Hub before you import users .

If you already have many users in Control Hub who do not have the correct entitlement, you can resolve the situation by exporting all users to a CSV file , and then reimporting all the users from the CSV file. This works because importing users by CSV automatically applies the
                                    Message Free entitlement. Importing users with Hybrid Directory Service does not automatically apply this entitlement unless
                                    you use an automatic license assignment template.

For a small number of affected users, you may prefer to manually apply their entitlement - especially if you have a diverse
                                    set of entitlements in your user population.

Are Message Service users losing messages in Jabber? When a Message Service user hides their status in Webex (the Show status setting is unchecked), then that user's presence is reflected as "Away" in Jabber. However, the Message Service continues
                                    working for that user, and processes their messages from IM and Presence up to Webex. If the user is only using Jabber, but
                                    is not actually using the client while the messages are coming in, the message may not ever appear in Jabber as it does not
                                    persist messages. This could be mitigated by enabling offline storage in IM and Presence, but we recommend that users affected
                                    like this should check the Show status setting in Webex. They could also use Webex which persists the messages.

### Hybrid Services Log

The Expressway's Experimental menu is not supported or documented.

You can read what the message connector is logging by reviewing the Hybrid Services Log on the Expressway:

Manually enter the URL for the /setaccess page, e.g. https:// <IPAddressOrFQDN> /setaccess

Enter the value qwertsys in the Access password field then click Enable access .

The Experimental menu is visible now.

Click Experimental > Hybrid Services Log > Hybrid Services Log .

Investigate the log for error conditions.

If you are having a repeatable or persistent problem, you should raise a case. You may be advised to change the log levels
                                    or take a diagnostic log to send to Cisco ( Maintenance > Diagnostics ).

### Proxy Server Updates

Whenever proxy settings are updated on Applications > Hybrid Services > Connector Proxy during runtime, a restart of hybrid services is required.

| Step 1 | Sign in to the primary peer of the Message Connector Expressway cluster, and go to Applications > Hybrid Services > Connector Management . |
|---|---|
| Step 2 | Click Message Connector . |
| Step 3 | Choose Disabled from the Active drop-down list. |
| Step 4 | Click Save . The connector stops. |
| Step 5 | Choose Enabled from the Active drop-down list. |
| Step 6 | Click Save . The connector starts and the status changes to Running . |

| Note | There is a known issue where the software version of the IM and Presence node is not correctly synchronized on the Expressway
                                                after the IM and Presence node is upgraded. This is a purely cosmetic issue as the Message Connector does not use the version
                                                information for any purpose. You can synchronize the IM and Presence version by restarting the Message Connector. We intend
                                                to resolve this issue in a future Message Connector release. |
|---|---|

| Note | The Expressway's Experimental menu is not supported or documented. |
|---|---|