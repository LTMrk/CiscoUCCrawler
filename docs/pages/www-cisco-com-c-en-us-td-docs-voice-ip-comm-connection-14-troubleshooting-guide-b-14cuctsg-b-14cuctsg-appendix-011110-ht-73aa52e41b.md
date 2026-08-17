---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-appendix-011110-ht-73aa52e41b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_appendix_011110.html
retrieved_at: 2026-08-17T02:18:35.746482+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting
	 Tenant Partitioning

## Chapter: Troubleshooting
	 Tenant Partitioning

# Troubleshooting
                     	 Tenant Partitioning

Troubleshooting Problems
                           		  While Configuring Tenant Partitioning

This section covers
                        		the problems that you might face while configuring tenant partitioning.

Getting Error Message "COS
                           		  is referenced by at least one user or user template" while Deleting a
                           		  Tenant

While deleting a
                        		tenant you may get this error message "COS is referenced by at least one user
                        		or user template". This error may occur for any other objects that are
                        		associated with the tenant. This error occurs if the objects mapped to a tenant
                        		like class of service are associated with users belonging to other tenants.

## Troubleshooting
                        	 Issues while Deleting Tenant

Step 1

Get object IDs of the class
                                       			 of service objects associated with the tenant using the URI:
                                       			 https://<connection-server>/vmrest/tenants/<TenantObjectId>/coses

Get the list of user
                                          				templates associated with the class of service object ID using the URI:
                                          				https://<connection-server>/vmrest/usertemplates?query=(CosObjectId%20is%20<CosObjectId>)

Here, replace <CosObjectId> with the COS Object Id that
                                          				belongs to the tenant.

To get the list of user templates that belongs to the tenant, use
                                          				the URI below:

https://<connection-server>/vmrest/usertemplates?query=(CosObjectId%20is%20<CosObjectId>%26PartitionObjectId%20is%20<PartitionObjectId>)

Step 2

Comparing results of the GET
                                       			 operations would provide list of user templates that are associated with the
                                       			 tenant's class of service but are not a part of tenant's partition. You can
                                       			 correct this by changing the class of service association for these user
                                       			 templates.

Step 3

Get the list of users
                                       			 associated with the class of service Object ID using the URI:

https://<connection-server/vmrest/users?query=(CosObjectId%20is%20<CosObjectId>)

Here, replace <CosObjectId> with the class of service Object
                                          				ID that belongs to the tenant. Now, to get the list of users that belongs to
                                          				the tenant, use the URI below:

https://<connection-server>/vmrest/users?query=(CosObjectId%20is%20<CosObjectId>%26PartitionObjectId%20is%20<PartitionObjectId>)

Step 4

Comparing results of both the GET operations provide with the list
                                       			 of users that are associated with the tenant's class of service objects but are
                                       			 not a part of tenant's partition. You can correct this by changing the class of
                                       			 service association for these users.

Step 5

Repeat Step 2 to Step 3 for all the class of service object IDs.

Step 6

Repeat Step 1 to Step 3 for other objects associated with a
                                       			 tenant.

## Users of One
                        	 Tenant are Able to Send Messages to Users of Other Tenants

If the users of one tenant are able
                           		to send messages to users of other tenants through the Web Inbox, touchtone, or
                           		voice recognition conversation, do the following:

- Check the tenant's search
                              		  space as it may contain partition(s) belonging to other tenants.

- Run an HTTP GET request on
                              		  the URI below to get Search Space Object ID for the tenant:
                              		  https://<connection-server>/vmrest/searchspacesmembers?query=(PartitionObjectId%20is%20<TenantPartitionObjectId>)

https://<connection-server>/vmrest/searchspacesmembers?query=(SearchSpaceObjectId%20is%20<TenantSearchSpaceObjectId>)

- Correct this by changing the
                              		  association.

## Able to Hear the
                        	 Opening Greeting Without being Asked for the PIN

If you are able to hear the opening
                           		greeting without being asked for the PIN, do the following;

- Open Port Status Monitor and
                              		  dial the pilot number.

- On Port Status Monitor and
                              		  check if the calls are going directly to the opening greeting.

GET
                                 			 https://<connection-server>/vmrest/routingrules?query=(SearchSpaceObjectId%20is%20<TenantSearchSpaceObjectId>)

To correct the routing rule order, see the CUPI APIs documentation for
                           		Routing Rules API.

http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Provisioning_Interface_%28CUPI%29_API_--_Routing_Rules

## Getting Option to
                        	 Select Users from Other Partitions in Directory Result

- Check Search Scope for the
                              		  directory handler that belongs to the tenant.

- If the value of SearchScope
                              		  field is set to zero then it means that the Search Scope is set to entire
                              		  server. Set the search scope value to 6 to resolve the issue.

- There is a possibility that
                              		  the SearchScope field is set to search-space of some other tenant. Set the
                              		  search scope to search space of respective tenant to resolve the issue.

### Debugging
                           	 Steps

https://<connection
                                    			 server>/vmrest/handlers/directoryhandlers?query=(PartitionObjectId%20is%20<TenantPartitionObjectId>)

If the value of SearchScope field is set to zero then it means that
                                    			 the Search Scope is set to entire server. Set the search scope value to 6 to
                                    			 resolve the issue.

- Enable Micro Traces for
                                 		  General Method returns and Parameter values(01), Data access(02), Named
                                 		  property access(03) level ConvSub logs and Named props access(11), CDL
                                 		  Access(12), MIU Access(13) and Search Space(04) level CDE logs from Cisco Unity
                                 		  Connection Serviceability.

- For all the aliases that you
                                 		  hear over the call, there may be an entry in the diag_ CuCsMgr_*.uc log files.

From the above URI search space object ID of a tenant is
                                          				  obtained and it can be used to find the associated partitions with the URI
                                          				  below.

- To get the search space:
                                       				GET
                                       				https://<connection-server>/vmrest/searchspaces/<searchspace-objectid>/searchspacemembers?query=(SearchSpaceObjectId%20is%20<SearchSpaceObjectId>

https://<connection
                                    			 server>/vmrest/handlers/directoryhandlers/<directoryhandler-objectid>

Check the search scope object ID, it should be same as that of the
                                    			 tenant.

## Tenant Creation
                        	 Fails with an Error Message "Non-Tenant users exist on Unity
                        	 Connection"

When a tenant creation API fails on
                           		a freshly installed system, do the following:

Try to create tenant in Unity Connection that is having users of any
                           		other partition, the following error displays:

"Invalid parameter. Parameter = [Non-Tenant users exists on Unity
                           		Connection.Cannot proceed with Tenant creation.], Value = [tbl_user]"

## Troubleshooting
                        	 Problems While Integrating with Call Manager

See the following sections:

### Hearing the Fast
                           	 Busy Tone on Dialing the Pilot Number

You may hear the fast busy tone
                              		while dialing the pilot number in the following two cases:

- Ports are busy or locked

- Ports required reset

Do the following:

- Check on Cisco Unity
                                 		  Connection Administration if any ports require a reset.

- In case you find any port
                                 		  group that requires a reset then login to Cisco Unity Connection Administration
                                 		  and go to the Port Groups page.

- If for any port group, value
                                 		  for the Needs Reset field is Yes, then reset the port group.

- Check if ports are busy
                                       				or number of incoming calls is significantly high in peak hours only or all the
                                       				time. Based on the tenant's requirement there might be a need to add additional
                                       				ports.

- Check Unity Connection
                                       				phone system: Check ports in Use Counter using the Real-Time Monitoring Tool
                                       				(RTMT) to see if ports are busy.

- The ports may be marked
                                       				busy even if the ports are locked.

- To verify, check using
                                       				the RTMT if the port frees up after a call ends and it answers other incoming
                                       				calls.

- Check the CUC Phone
                                       				System: Check the Ports Locked counter for any locked ports. You can reset the
                                       				port to resolve the port lock issue.

The Ports locked counter in RTMT can be checked in the CUC Phone System
                              		counter.

### Hearing the Error
                           	 Message - "The system is temporarily unable to complete your call" on Dialing
                           	 the Pilot Number

To Resolve Issues When there
                                    			 are No Appropriate Routing Rules in Unity Connection

Step 1

Enable Threads(11) and
                                          			 Ports(13) level Micro Traces for Arbiter on Cisco Unity Connection
                                          			 Serviceability. Check the diag_CuCsMgr_*.uc log file for the phone system:

where "PhoneSystem_1" is the name of the phone system

Step 2

For details on how to view
                                          			 diagnostic traces, see the Using Diagnostic Traces for Troubleshooting section.

Step 3

In case, no routing rules
                                          			 exist for the tenant, you can add them using the POST operation on the routing
                                          			 rules API. To identify that which type of routing rules (direct or forward)
                                          			 need to be added, you can use the Port Status Monitor.

If the Port Status Monitor displays that the call does not contain
                                             				a redirecting ID and value for the Reason field is direct, then Direct Routing
                                             				Rule is added else add the Forward Routing Rule.

Step 4

If routing rule condition has been removed or is missing from a
                                          			 routing rule on Unity Connection then the routing rule that comes later in the
                                          			 list, is never reached. To check or to investigate the issue:

- Check if tenant's
                                                				  phone system is added as a routing rule condition in the routing rules for that
                                                				  tenant. For more information refer to the Routing Rule Condition APIs available
                                                				  at http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_APIs.

- Enable the Micro
                                                				  Traces for Routing Rules and "Thread (11) and Ports(13)" for Arbiter on Cisco
                                                				  Unity Connection Serviceability and check the logs for any errors or issues.

- Check the phone system
                                                				  configuration like phone system, port groups, ports and SIP security profile
                                                				  for Unity Connection. You can check the following:

- Verify that the port
                                                				  number specified in SIP Trunk profile on Cisco Unified Communications Manager
                                                				  and the Port Group on Unity Connection are same.

- Verify that SIP Trunk
                                                				  Security Profile on Cisco Unified Communications Manager has the correct
                                                				  incoming port number.

- Verify the Cisco
                                                				  Unified Communications Manager IP address or hostname specified in port group
                                                				  on Unity Connection.

## Troubleshooting
                        	 Problems with Migration

See the following sections:

### "Mailbox could not
                           	 be loaded" Error Shows Up

If the error "Mailbox could not be
                              		loaded" shows up for one or more subscribers on Web Inbox after migrating data
                              		from a multi-tenant Unity Connection to another multi-tenant Unity Connection,
                              		do the following:

Check if the setting required for mailbox access may be lost during
                              		migration. To enable it back, do the following:

https://<connection-server>/vmrest/users?query=(Alias%20is%20<UserAlias>

https://<connection-server>/vmrest/coses/<CosObjectId>

### SMTP Proxy Address
                           	 Not Updated on Unity Connection for One or More Subscribers After
                           	 Migration

- Look for the errors or
                                 		  warnings in the log files after migration at the following location:
                                 		  <COBRASInstallationDirectory>/logs

https://<connection-server>/vmrest/smtpproxyaddresses?query=(SmtpAddress%20is%20<SmtpProxyAddress>)

Here, <SmtpProxyAddress> is the field for which the update
                                    			 failed.

https://<connection-server>/vmrest/users?query=(ObjectId%20is%20<UserObjectId>)

https://<connection-server>/vmrest/smtpproxyaddresses

### Hearing a Wrong
                           	 Post Greeting Recording for Users Belonging to a Tenant

If you are hearing a wrong post
                              		greeting recording for users belonging to a tenant, do the following:

- Check if the post greeting
                                 		  recording with the same name already exists in the Unity Connection.

- Look for the errors or
                                 		  warnings in the log files after migration at the following location:
                                 		  <COBRASInstallationDirectory>/logs

- Administrator can pick the
                                 		  missing recording from the backup of the destination Unity Connection, or else
                                 		  re-recording needs to be done.

### Getting Incorrect
                           	 Time for Incoming or Outgoing Messages

In COBRAS migration, for any
                              		subscriber if timezone in the source Unity Connection is set to system default
                              		timezone then after migration in the destination Unity Connection, it would be
                              		set to the timezone that the tenant was created with.

To set it right, do the following:

https://<connection-server>/vmrest/users?query=(Alias%20is%20<UserAlias>)

https://<connection-server>/vmrest/users/<UserObjectId>

### Get Incorrect
                           	 Language for the Incoming or Outgoing Users

In COBRAS migration, for any
                              		subscriber if language in the source Unity Connection is set to system default
                              		language then after migration, in the destination Unity Connection, it would be
                              		set to the language that the tenant was created with.

To set it right, do the following:

https://<connection-server>/vmrest/users?query=(Alias%20is%20<UserAlias>)

https://<connection-server>/vmrest/users/<UserObjectId>

| Step 1 | Get object IDs of the class
                                       			 of service objects associated with the tenant using the URI:
                                       			 https://<connection-server>/vmrest/tenants/<TenantObjectId>/coses Get the list of user
                                          				templates associated with the class of service object ID using the URI:
                                          				https://<connection-server>/vmrest/usertemplates?query=(CosObjectId%20is%20<CosObjectId>) Here, replace <CosObjectId> with the COS Object Id that
                                          				belongs to the tenant. To get the list of user templates that belongs to the tenant, use
                                          				the URI below: https://<connection-server>/vmrest/usertemplates?query=(CosObjectId%20is%20<CosObjectId>%26PartitionObjectId%20is%20<PartitionObjectId>) |
|---|---|
| Step 2 | Comparing results of the GET
                                       			 operations would provide list of user templates that are associated with the
                                       			 tenant's class of service but are not a part of tenant's partition. You can
                                       			 correct this by changing the class of service association for these user
                                       			 templates. |
| Step 3 | Get the list of users
                                       			 associated with the class of service Object ID using the URI: https://<connection-server/vmrest/users?query=(CosObjectId%20is%20<CosObjectId>) Here, replace <CosObjectId> with the class of service Object
                                          				ID that belongs to the tenant. Now, to get the list of users that belongs to
                                          				the tenant, use the URI below: https://<connection-server>/vmrest/users?query=(CosObjectId%20is%20<CosObjectId>%26PartitionObjectId%20is%20<PartitionObjectId>) |
| Step 4 | Comparing results of both the GET operations provide with the list
                                       			 of users that are associated with the tenant's class of service objects but are
                                       			 not a part of tenant's partition. You can correct this by changing the class of
                                       			 service association for these users. |
| Step 5 | Repeat Step 2 to Step 3 for all the class of service object IDs. |
| Step 6 | Repeat Step 1 to Step 3 for other objects associated with a
                                       			 tenant. |

| Step 1 | Enable Threads(11) and
                                          			 Ports(13) level Micro Traces for Arbiter on Cisco Unity Connection
                                          			 Serviceability. Check the diag_CuCsMgr_*.uc log file for the phone system: 'Failed to find routing rule=<PhoneSystem_1>' where "PhoneSystem_1" is the name of the phone system |
|---|---|
| Step 2 | For details on how to view
                                          			 diagnostic traces, see the Using Diagnostic Traces for Troubleshooting section. |
| Step 3 | In case, no routing rules
                                          			 exist for the tenant, you can add them using the POST operation on the routing
                                          			 rules API. To identify that which type of routing rules (direct or forward)
                                          			 need to be added, you can use the Port Status Monitor. If the Port Status Monitor displays that the call does not contain
                                             				a redirecting ID and value for the Reason field is direct, then Direct Routing
                                             				Rule is added else add the Forward Routing Rule. |
| Step 4 | If routing rule condition has been removed or is missing from a
                                          			 routing rule on Unity Connection then the routing rule that comes later in the
                                          			 list, is never reached. To check or to investigate the issue: Check if tenant's
                                                				  phone system is added as a routing rule condition in the routing rules for that
                                                				  tenant. For more information refer to the Routing Rule Condition APIs available
                                                				  at http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_APIs. Enable the Micro
                                                				  Traces for Routing Rules and "Thread (11) and Ports(13)" for Arbiter on Cisco
                                                				  Unity Connection Serviceability and check the logs for any errors or issues. Check the phone system
                                                				  configuration like phone system, port groups, ports and SIP security profile
                                                				  for Unity Connection. You can check the following: Verify that the port
                                                				  number specified in SIP Trunk profile on Cisco Unified Communications Manager
                                                				  and the Port Group on Unity Connection are same. Verify that SIP Trunk
                                                				  Security Profile on Cisco Unified Communications Manager has the correct
                                                				  incoming port number. Verify the Cisco
                                                				  Unified Communications Manager IP address or hostname specified in port group
                                                				  on Unity Connection. |