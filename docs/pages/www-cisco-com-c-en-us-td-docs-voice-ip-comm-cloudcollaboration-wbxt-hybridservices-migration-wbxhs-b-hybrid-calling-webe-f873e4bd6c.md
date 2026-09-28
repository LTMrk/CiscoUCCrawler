---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-hybridservices-migration-wbxhs-b-hybrid-calling-webe-f873e4bd6c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/hybridservices/migration/wbxhs_b_hybrid-calling-webex-domain-migration-guide/wbxhs_b_migrate-call-service-to-webex_chapter_010.html
retrieved_at: 2026-08-20T23:59:46.672369+00:00
---

Migrate Cisco Spark Hybrid Call Service Organization to the Cisco Webex Domain

# Migrate Cisco Spark Hybrid Call Service Organization to the Cisco Webex Domain

## Results

Updated: March 7, 2019

Chapter: Migrate Your Organization

## Chapter: Migrate Your Organization

# Migrate Your Organization

## Migrate Hybrid Call Service to Webex SIP Addresses Task Flow

Follow these tasks to migrate your Hybrid Call Service organization to SIP addresses that use the Webex domain. The tasks
                              walk you through the necessary configuration on your premises (Expressway pair and Unified CM) and the cloud and intermediary
                              side (Control Hub, Expressway connector host) and how to verify that the migration is successful.

If you don't have Hybrid Call Service, that means you have a cloud organization. You can ignore this document and use the
                                          steps in Change Your Webex SIP Address instead.

### Before you begin

Make sure your Expressways and Unified CMs are on a supported release, as documented in the Requirements for Hybrid Call Service in the deployment guide. For example, this task flow assumes a minimum of X8.11.4 or later for the Expressway traversal pair.

Create a New SIP Route Pattern on Unified CM Clusters

This migration task assumes you followed the deployment steps in Configure Cisco Unified Communications Manager Settings for Hybrid Call Service . You'll create a new SIP route pattern for the new routing domain for Cisco Webex. You must keep the existing SIP route pattern
                                          for *.ciscospark.com .

Create New Outbound Search Rules on Expressway-C Clusters

This migration task assumes that you followed the deployment steps in Configure the Expressway-C for Hybrid Call Service . In this context, outbound means from your premises towards Cisco Webex.

You could be using one or more Expressway-C clusters with Hybrid Call Service. Each of those could be connected to one or
                                          more Unified CM clusters. Each Expressway-C cluster has a neighbor zone to each associated Unified CM cluster. Each Expressway-C
                                          cluster has a traversal zones relationship with a corresponding Expressway-E cluster.

Create New Webex Zones on Expressway-E Clusters

You have one or more Expressway-E clusters in your Hybrid Call Service deployment. Each of them has a DNS zone, configured
                                          to look up the Cisco Spark SIP hosts based on the pattern *.ciscospark.com. We’re going to create a new Webex zone, adjacent
                                          to the existing DNS zone, on each Expressway-E cluster.

Create Search Rules Between Traversal Server Zone and Webex Zone

This migration task assumes you followed the deployment steps in Create Inbound and Outbound Search Rules in the deployment guide. Search rules define how the Expressway routes calls (to destination zones) in specific call scenarios.
                                          When a search rule is matched, the destination alias can be modified according to the conditions defined in the search rule.
                                          Add these new search rules on Expressway-E to:

Prioritize the Webex domain routing over the Spark routing.

Identify calls from the Cisco Webex cloud and route down the traversal zone to Expressway-C.

Identify calls from Cisco Unified Communications Manager and route through the Webex Zone to Cisco Webex.

Add CPL Rule on Expressway-E

This migration task assumes you followed the deployment steps in Configure Call Processing Language Rules on Expressway-E . This task applies to your Hybrid Call Service deployment if you have an existing CPL (Call Processing Language) rule on
                                          Expressway-E, to protect your traversal pair from toll fraud.

We will add a rule because the new domain is another potential source of fraudulent call attempts.

Migrate Users and Devices in Workspaces to Webex SIP Addresses

After you finish the appropriate on-premises configuration steps, complete
                                          the Hybrid Call Service steps in Cisco Webex Control Hub ( https://admin.webex.com ) and the Call Connector. You'll perform steps to bring over all of your
                                          users and workspaces to the Webex-branded SIP addresses and mirror this
                                          configuration as the new remote destination on the Cisco Spark-RDs in
                                          Unified CM.

### Create a New SIP Route Pattern on Unified CM Clusters

This migration task assumes you followed the deployment steps in Configure Cisco Unified Communications Manager Settings for Hybrid Call Service . You'll create a new SIP route pattern for the new routing domain for Cisco Webex . You must keep the existing SIP route pattern for *.ciscospark.com .

For each Unified CM cluster in your Hybrid Call Service deployment, sign in to the publisher node, and from Cisco Unified
                                          CM Administration, go to Call Routing > SIP Route Pattern , and then create a new route pattern with the following settings:

Field Name

Value

IPv4 Pattern

*.webex.com

Pattern Usage

Domain Routing

Description

Routing to Cisco Webex

SIP Trunk/Route List

Choose the trunk you created for Hybrid Call Service— Hybrid_Calling_SIP_Trunk (for example)

Save your changes.

You now have at least two route patterns from each Unified CM cluster that both route on the same trunk to an Expressway-C
                                             cluster. The patterns are *.ciscospark.com and *.webex.com . Leave the *.ciscospark.com route pattern in place until we (Cisco) officially announce its removal.

### Create New Outbound Search Rules on Expressway-C Clusters

This migration task assumes that you followed the deployment steps in Configure the Expressway-C for Hybrid Call Service . In this context, outbound means from your premises towards Cisco Webex.

You could be using one or more Expressway-C clusters with Hybrid Call Service. Each of those could be connected to one or
                                 more Unified CM clusters. Each Expressway-C cluster has a neighbor zone to each associated Unified CM cluster. Each Expressway-C
                                 cluster has a traversal zones relationship with a corresponding Expressway-E cluster.

There are existing rules on the Expressway-C clusters to route calls from the Unified CM neighbour zones to the traversal
                                 client zone. In this task, we’re going to clone all those rules and change the pattern on each. So, for each Expressway-C
                                 cluster in your Hybrid Call Service deployment:

Sign in to the primary peer, and go to Configuration > Dial plan > Search rules .

Order the list by the Target column so you can easily find all the rules that point to the traversal client zone.

For each rule that is sourced from a Unified CM neighbour zone and targets the traversal client zone:

Click Clone . You get a new create search rule page with details completed as per your original search rule.

Add the text “NEW PATTERN” or similar to the end of the rule name. This should help you preserve the new rules when you clean up later. Also, you cannot
                                                have duplicate rule names.

Decrease the Priority a small amount, for example, by 5.

Change the Pattern string field:

From

.+@.+\.(room|call)\.ciscospark\.com.*

To

.+@.+\.(calls|rooms|meetup)\.webex\.com.*

The new pattern matches your new SIP URIs. For example, SIP URIs will
                                                   change from user@example.call.ciscospark.com to user@example.calls.webex.com , or from workspace@example.room.ciscospark.com to workspace@example.rooms.webex.com .

Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs.

Click Create search rule .

Repeat until you’ve cloned all the Hybrid Call Service-related rules on this Expressway-C primary peer.

The Expressway-C search rules list should look something like this when you’re finished:

Repeat until you’ve cloned the Hybrid Call Service-related rules on all Expressway-C primary peers in your deployment.

### Create New Webex Zones on Expressway-E Clusters

You have one or more Expressway-E clusters in your Hybrid Call Service deployment. Each of them has a DNS zone, configured
                                 to look up the Cisco Spark SIP hosts based on the pattern *.ciscospark.com. We’re going to create a new Webex zone, adjacent
                                 to the existing DNS zone, on each Expressway-E cluster.

On each Expressway-E cluster in your Hybrid Call Service deployment, Sign in to the primary peer, and go to Configuration > Zones > Zones .

Click New .

You don't need to enter a name for this zone, it is created for you.

In the Type field, select Webex .

Click Create zone .

The "Webex Zone" is now in the zones list. The zone settings are fixed. You cannot edit this zone or create any more instances
                                             of this type on this Expressway-E primary peer.

Repeat on all other Expressway-E primary peers in your Hybrid Call Service deployment.

### Create Search Rules Between Traversal Server Zone and Webex Zone

This migration task assumes you followed the deployment steps in Create Inbound and Outbound Search Rules in the deployment guide. Search rules define how the Expressway routes calls (to destination zones) in specific call scenarios.
                                 When a search rule is matched, the destination alias can be modified according to the conditions defined in the search rule.
                                 Add these new search rules on Expressway-E to:

Prioritize the Webex domain routing over the Spark routing.

Identify calls from the Cisco Webex cloud and route down the traversal zone to Expressway-C.

Identify calls from Cisco Unified Communications Manager and route through the Webex Zone to Cisco Webex.

For each Expressway-E cluster in your Hybrid Call Service deployment, sign in to the primary peer, and go to Configuration > Dial plan > Search rules .

There should be one rule outbound to the existing, Hybrid Call Service-related DNS zone and one rule inbound from that zone,
                                             for example:

Clone and modify the outbound rule as follows:

Click Clone in the same row as the outbound rule. You get a new create search rule page with details completed as per your original search
                                                rule.

Add the text “NEW PATTERN” or similar to the end of the rule name.

Decrease the Priority a small amount, for example by 5.

This forces the Expressway-Es to attempt routing the new Webex rules first. If the new routing rules don't work, Expressway-Es
                                                   will fall back on the original Spark rules.

Change the Pattern string field as follows:

From

.+@.+\.ciscospark\.com.*

To

.+@.+\.(calls|rooms|meetup).webex\.com.*

The new pattern matches your new SIP URIs. For example, SIP URIs will
                                                   change from user@example.call.ciscospark.com to user@example.calls.webex.com , or from workspace@example.room.ciscospark.com to workspace@example.rooms.webex.com .

Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs.

Leave the Source name field set to the traversal server zone.

Change the Target field to Webex Zone .

Click Create search rule .

Clone and modify the inbound rule as follows:

Click Clone in the same row as the inbound rule. You get a new create search rule page with details completed as per your original search
                                                rule.

Add the text “ FROM WEBEX ZONE ” or similar to the end of the rule name.

Change the Source name field to Webex Zone .

Leave the Target field set to the traversal server zone.

Click Create search rule .

You should now have one inbound rule and one outbound rule for each of the two Hybrid Call Service-related zones. For example:

If necessary, repeat the procedure on your other Expressway-E clusters.

### Add CPL Rule on Expressway-E

This migration task assumes you followed the deployment steps in Configure Call Processing Language Rules on Expressway-E . This task applies to your Hybrid Call Service deployment if you have an existing CPL (Call Processing Language) rule on
                                 Expressway-E, to protect your traversal pair from toll fraud.

We will add a rule because the new domain is another potential source of fraudulent call attempts.

Sign in to the Expressway-E and go to Configuration > Call Policy > Rules .

There should already be a rule to reject calls from unauthenticated callers whose addresses match .*@example\.call\.ciscospark\.com.* , where example is your company's subdomain.

Click New and configure the new rule as follows:

Field

Setting

Source type

From address

Rule applies to

Unauthenticated callers

Source pattern

.*@example\.calls\.webex\.com.* , where example is your company's subdomain.

Destination pattern

.*

Action

Reject

Click Add to save this new rule.

### Migrate Users and Devices in Workspaces to Webex SIP Addresses

After you finish the appropriate on-premises configuration steps, complete the Hybrid
                                 Call Service steps in Cisco Webex Control Hub ( https://admin.webex.com ) and the Call Connector. You'll perform steps to bring over all of your users and
                                 workspaces to the Webex-branded SIP addresses and mirror this configuration as the
                                 new remote destination on the Cisco Spark-RDs in Unified CM. The following is a
                                 high-level overview of the steps:

Disabling and reenabling Call Service Connect for the org —This step
                                       requires a number of substeps. You'll first toggle off Call Service Connect
                                       for your organization, which effectively converts you to a cloud calling
                                       organization. You then edit your organization SIP domain which kicks off the
                                       SIP address change to the Webex domain, which runs as a background task in
                                       Control Hub. When completed and you've verified that the SIP addresses
                                       updated for users and workspaces, you toggle Call Service Connect back on
                                       for your organization.

SIP Address Change —This step uses the SIP address mechanism that is
                                       built into Control Hub. When you're a cloud calling organization (in this
                                       case, when you temporarily disable Call Service Connect), you can edit your
                                       subdomain, and this step kicks off the migration of your SIP addresses for
                                       users and workspaces to the Webex domain.

Call Connector Updates —The call connectors pick up the SIP address change as the new remote destination to pass down to Cisco Spark-RDs on each
                                       Unified CM cluster. The expected behavior is covered in the procedure steps.

Verification of New Addresses —Throughout the procedure, there are checks and balances to help you verify the migration on the Control Hub and premises
                                       side of things.

#### Before you begin

Complete the on-premises migration steps on your Unified CM and Expressway environments. If the on-premises configuration
                                 is not completed correctly, the users will be in error state for Hybrid Call Service.

From the customer view in https://admin.webex.com , deactivate Hybrid Call Service Connect for your organization by going to Organization Services , choosing Edit settings on the Hybrid
                                          Call card, scrolling to Call Service Connect , and then clicking Deactivate .

As soon as the service is deactivated, Hybrid Call Service calls will not
                                             route. This step is required to temporarily convert you to a cloud calling
                                             organization, which allows you to modify the SIP addresses for calling.
                                             After you see that Call Service Connect is disabled for the organization,
                                             you can proceed with the steps.

Go to Settings , scroll to SIP Address for Cisco Webex Calling , click Edit Subdomain , leave the same value or enter a new value as needed, click Check Availability , click Save and then click OK .

This step triggers the migration process that converts the domains from Cisco Spark to Webex. You'll see a background task
                                             notification at the top of your Control Hub instance. You can click on the notification to see the status of the SIP address changes.

Secondary SIP addresses with ciscospark.com remain if you don't change the subdomain value. If you do change the subdomain
                                             value, the ciscospark.com SIP address is not preserved.

If any users or workspaces produce an error in the results, you can try
                                                         these steps to address the issue:

Redo the preceding step to trigger the migration process again—you should see a Rerun button.

If specific users or workspaces continue to produce errors, try
                                                               to edit the user or workspace in Control Hub without making any
                                                               changes and then click Save .

If you rerun the migration step and still see users and
                                                               workspaces in error state, export the CSV file, open a case with the Cisco TAC , and
                                                               attach the CSV file to your case.

After the SIP address background task is completed and there are no errors, use Cisco Webex Control Hub to verify that the SIP addresses appear correctly for users and
                                          Workspaces:

Where to Verify in Control Hub

Expected Result

Users

Go to Users , click any user, click Calling , and then you'll see
                                                         the primary and backup SIP address entries.

Workspaces

Go to Workspaces , click any
                                                         workspace to open the overview pane, and then under Calling you'll see the
                                                         primary and backup SIP address entries.

After you verify that the SIP addresses converted correctly to a Webex
                                             domain, you can reenable your organization with Hybrid Call Service
                                             Connect.

From the customer view in https://admin.webex.com , reactivate Hybrid Call Service Connect for your organization by going to Services > Hybrid , choosing Edit settings on the Hybrid
                                          Call card, scrolling to Call Service Connect , and then clicking Activate .

After all the user and Workspace SIP addresses are changed on the cloud side
                                             and your organization is reenabled for Hybrid Call Service Connect, the Call
                                             Connector on Expressway needs to pick up on these changes and replicate them
                                             on the premises side. On Unified CM, the new Webex SIP addresses become the
                                             remote destination for each Cisco Spark-RD that is tied to a user or
                                             workspace account.

To synchronize these changes, choose an option:

Wait for the daily user activation status validation, which occurs between 7 am and 11 am Universal Time Coordinated (UTC).
                                                   The changes are picked up through the Call Connector after this validation period.

Restart each Call Connector by following these steps in the deployment guide . In a multicluster deployment, restarting the connector on the primary node automatically restarts the other connectors in
                                                   the cluster. The changes are picked up after the connector comes back online.

As mentioned in the deployment guide, restarting the Call Connector creates extra load on Unified CM publishers. Consider
                                                               restarting the Call Connector during off-peak hours; during busy hours, a restart may cause service issues.

Verify that the Cisco Spark-RDs are still listed: from Cisco Unified CM Administration, go to Device > Phone , and search on Cisco Spark Remote Device as the Device Type .

Verify that the remote destinations were created correctly: From Cisco Unified CM Administration, go to Device > Remote Destination , choose CTI Remote Device/Cisco Spark Remote Device from the Find destination where drop down, and then click Find .

The results show each Cisco Spark Remote Device (Cisco Spark-RDs) in your
                                             deployment and the remote destination (under Destination
                                                Number . Your Cisco Spark-RDs have a remote destination
                                             subdomain calls.webex.com for users and rooms.webex.com for devices in a workspace.

Make test calls to verify that call behavior is as expected (for example, an
                                          incoming call rings both a Hybrid Call Service user's desk phone and Webex app.

See the Test the Softphone Functionality for Hybrid Call
                                                Service procedure in the deployment guide for more
                                             information.

Things to Keep in Mind

After the change is made in Control Hub, the new Webex SIP addresses are set
                                       as the primary address for users and workspaces. At this point, calls from
                                       cloud to enterprise begin to use the new *.webex.com SIP addresses.

Old SIP addresses (*.ciscospark.com) are not removed. This ensures that calls toward the Cisco Webex cloud still work when
                                       when users dial the old SIP addresses.

Because the on-premises Cisco Spark-RD is configured with the old *.ciscospark.com value, outbound calls will not anchor to
                                       the user’s home cluster. Depending on customer routing rules, calls may fail for a brief period of time.

For example, a user's SIP address is webex.com but the manual Cisco Spark-RD remote destination address is still ciscospark.com
                                       until the nightly discovery connector restarts updates the Cisco Spark-RD with the new webex.com address. If you migrate this
                                       at 9 am but wait for nightly discovery to update the Cisco Spark-RD, then calls from this user may not work properly.

| Note | If you don't have Hybrid Call Service, that means you have a cloud organization. You can ignore this document and use the
                                          steps in Change Your Webex SIP Address instead. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create a New SIP Route Pattern on Unified CM Clusters | This migration task assumes you followed the deployment steps in Configure Cisco Unified Communications Manager Settings for Hybrid Call Service . You'll create a new SIP route pattern for the new routing domain for Cisco Webex. You must keep the existing SIP route pattern
                                          for *.ciscospark.com . |
| Step 2 | Create New Outbound Search Rules on Expressway-C Clusters | This migration task assumes that you followed the deployment steps in Configure the Expressway-C for Hybrid Call Service . In this context, outbound means from your premises towards Cisco Webex. You could be using one or more Expressway-C clusters with Hybrid Call Service. Each of those could be connected to one or
                                          more Unified CM clusters. Each Expressway-C cluster has a neighbor zone to each associated Unified CM cluster. Each Expressway-C
                                          cluster has a traversal zones relationship with a corresponding Expressway-E cluster. |
| Step 3 | Create New Webex Zones on Expressway-E Clusters | You have one or more Expressway-E clusters in your Hybrid Call Service deployment. Each of them has a DNS zone, configured
                                          to look up the Cisco Spark SIP hosts based on the pattern *.ciscospark.com. We’re going to create a new Webex zone, adjacent
                                          to the existing DNS zone, on each Expressway-E cluster. |
| Step 4 | Create Search Rules Between Traversal Server Zone and Webex Zone | This migration task assumes you followed the deployment steps in Create Inbound and Outbound Search Rules in the deployment guide. Search rules define how the Expressway routes calls (to destination zones) in specific call scenarios.
                                          When a search rule is matched, the destination alias can be modified according to the conditions defined in the search rule.
                                          Add these new search rules on Expressway-E to: Prioritize the Webex domain routing over the Spark routing. Identify calls from the Cisco Webex cloud and route down the traversal zone to Expressway-C. Identify calls from Cisco Unified Communications Manager and route through the Webex Zone to Cisco Webex. |
| Step 5 | Add CPL Rule on Expressway-E | This migration task assumes you followed the deployment steps in Configure Call Processing Language Rules on Expressway-E . This task applies to your Hybrid Call Service deployment if you have an existing CPL (Call Processing Language) rule on
                                          Expressway-E, to protect your traversal pair from toll fraud. We will add a rule because the new domain is another potential source of fraudulent call attempts. |
| Step 6 | Migrate Users and Devices in Workspaces to Webex SIP Addresses | After you finish the appropriate on-premises configuration steps, complete
                                          the Hybrid Call Service steps in Cisco Webex Control Hub ( https://admin.webex.com ) and the Call Connector. You'll perform steps to bring over all of your
                                          users and workspaces to the Webex-branded SIP addresses and mirror this
                                          configuration as the new remote destination on the Cisco Spark-RDs in
                                          Unified CM. |

| Step 1 | For each Unified CM cluster in your Hybrid Call Service deployment, sign in to the publisher node, and from Cisco Unified
                                          CM Administration, go to Call Routing > SIP Route Pattern , and then create a new route pattern with the following settings: Field Name Value IPv4 Pattern *.webex.com Pattern Usage Domain Routing Description Routing to Cisco Webex SIP Trunk/Route List Choose the trunk you created for Hybrid Call Service— Hybrid_Calling_SIP_Trunk (for example) | Field Name | Value | IPv4 Pattern | *.webex.com | Pattern Usage | Domain Routing | Description | Routing to Cisco Webex | SIP Trunk/Route List | Choose the trunk you created for Hybrid Call Service— Hybrid_Calling_SIP_Trunk (for example) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Field Name | Value |
| IPv4 Pattern | *.webex.com |
| Pattern Usage | Domain Routing |
| Description | Routing to Cisco Webex |
| SIP Trunk/Route List | Choose the trunk you created for Hybrid Call Service— Hybrid_Calling_SIP_Trunk (for example) |
| Step 2 | Save your changes. You now have at least two route patterns from each Unified CM cluster that both route on the same trunk to an Expressway-C
                                             cluster. The patterns are *.ciscospark.com and *.webex.com . Leave the *.ciscospark.com route pattern in place until we (Cisco) officially announce its removal. |

| Field Name | Value |
|---|---|
| IPv4 Pattern | *.webex.com |
| Pattern Usage | Domain Routing |
| Description | Routing to Cisco Webex |
| SIP Trunk/Route List | Choose the trunk you created for Hybrid Call Service— Hybrid_Calling_SIP_Trunk (for example) |

| Step 1 | Sign in to the primary peer, and go to Configuration > Dial plan > Search rules . |
|---|---|
| Step 2 | Order the list by the Target column so you can easily find all the rules that point to the traversal client zone. |
| Step 3 | For each rule that is sourced from a Unified CM neighbour zone and targets the traversal client zone: Click Clone . You get a new create search rule page with details completed as per your original search rule. Add the text “NEW PATTERN” or similar to the end of the rule name. This should help you preserve the new rules when you clean up later. Also, you cannot
                                                have duplicate rule names. Decrease the Priority a small amount, for example, by 5. This forces the Expressway-Cs to attempt routing the new Webex rules first. If the new routing rules don't work yet, Expressway-Cs
                                                will fall back on the original Spark rules. Change the Pattern string field: From .+@.+\.(room\|call)\.ciscospark\.com.* To .+@.+\.(calls\|rooms\|meetup)\.webex\.com.* The new pattern matches your new SIP URIs. For example, SIP URIs will
                                                   change from user@example.call.ciscospark.com to user@example.calls.webex.com , or from workspace@example.room.ciscospark.com to workspace@example.rooms.webex.com . Note Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. Click Create search rule . | From | .+@.+\.(room\|call)\.ciscospark\.com.* | To | .+@.+\.(calls\|rooms\|meetup)\.webex\.com.* | Note | Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. |
| From | .+@.+\.(room\|call)\.ciscospark\.com.* |
| To | .+@.+\.(calls\|rooms\|meetup)\.webex\.com.* |
| Note | Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. |
| Step 4 | Repeat until you’ve cloned all the Hybrid Call Service-related rules on this Expressway-C primary peer. The Expressway-C search rules list should look something like this when you’re finished: |
| Step 5 | Repeat until you’ve cloned the Hybrid Call Service-related rules on all Expressway-C primary peers in your deployment. |

| From | .+@.+\.(room\|call)\.ciscospark\.com.* |
|---|---|---|
| To | .+@.+\.(calls\|rooms\|meetup)\.webex\.com.* |

| Note | Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. |
|---|---|

| Step 1 | On each Expressway-E cluster in your Hybrid Call Service deployment, Sign in to the primary peer, and go to Configuration > Zones > Zones . |
|---|---|
| Step 2 | Click New . You don't need to enter a name for this zone, it is created for you. |
| Step 3 | In the Type field, select Webex . |
| Step 4 | Click Create zone . The "Webex Zone" is now in the zones list. The zone settings are fixed. You cannot edit this zone or create any more instances
                                             of this type on this Expressway-E primary peer. |
| Step 5 | Repeat on all other Expressway-E primary peers in your Hybrid Call Service deployment. |

| Step 1 | For each Expressway-E cluster in your Hybrid Call Service deployment, sign in to the primary peer, and go to Configuration > Dial plan > Search rules . There should be one rule outbound to the existing, Hybrid Call Service-related DNS zone and one rule inbound from that zone,
                                             for example: |
|---|---|
| Step 2 | Clone and modify the outbound rule as follows: Click Clone in the same row as the outbound rule. You get a new create search rule page with details completed as per your original search
                                                rule. Add the text “NEW PATTERN” or similar to the end of the rule name. Decrease the Priority a small amount, for example by 5. This forces the Expressway-Es to attempt routing the new Webex rules first. If the new routing rules don't work, Expressway-Es
                                                   will fall back on the original Spark rules. Change the Pattern string field as follows: From .+@.+\.ciscospark\.com.* To .+@.+\.(calls\|rooms\|meetup).webex\.com.* The new pattern matches your new SIP URIs. For example, SIP URIs will
                                                   change from user@example.call.ciscospark.com to user@example.calls.webex.com , or from workspace@example.room.ciscospark.com to workspace@example.rooms.webex.com . Note Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. Leave the Source name field set to the traversal server zone. Change the Target field to Webex Zone . Click Create search rule . | From | .+@.+\.ciscospark\.com.* | To | .+@.+\.(calls\|rooms\|meetup).webex\.com.* | Note | Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. |
| From | .+@.+\.ciscospark\.com.* |
| To | .+@.+\.(calls\|rooms\|meetup).webex\.com.* |
| Note | Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. |
| Step 3 | Clone and modify the inbound rule as follows: Click Clone in the same row as the inbound rule. You get a new create search rule page with details completed as per your original search
                                                rule. Add the text “ FROM WEBEX ZONE ” or similar to the end of the rule name. Change the Source name field to Webex Zone . Leave the Target field set to the traversal server zone. Click Create search rule . You should now have one inbound rule and one outbound rule for each of the two Hybrid Call Service-related zones. For example: |
| Step 4 | If necessary, repeat the procedure on your other Expressway-E clusters. |

| From | .+@.+\.ciscospark\.com.* |
|---|---|
| To | .+@.+\.(calls\|rooms\|meetup).webex\.com.* |

| Note | Use the pattern checker ( Maintenance > Tools > Check pattern ) to test the new pattern you enter against one or more of your new format URIs. |
|---|---|

| Step 1 | Sign in to the Expressway-E and go to Configuration > Call Policy > Rules . There should already be a rule to reject calls from unauthenticated callers whose addresses match .*@example\.call\.ciscospark\.com.* , where example is your company's subdomain. |
|---|---|
| Step 2 | Click New and configure the new rule as follows: Field Setting Source type From address Rule applies to Unauthenticated callers Source pattern .*@example\.calls\.webex\.com.* , where example is your company's subdomain. Destination pattern .* Action Reject | Field | Setting | Source type | From address | Rule applies to | Unauthenticated callers | Source pattern | .*@example\.calls\.webex\.com.* , where example is your company's subdomain. | Destination pattern | .* | Action | Reject |
| Field | Setting |
| Source type | From address |
| Rule applies to | Unauthenticated callers |
| Source pattern | .*@example\.calls\.webex\.com.* , where example is your company's subdomain. |
| Destination pattern | .* |
| Action | Reject |
| Step 3 | Click Add to save this new rule. |

| Field | Setting |
|---|---|
| Source type | From address |
| Rule applies to | Unauthenticated callers |
| Source pattern | .*@example\.calls\.webex\.com.* , where example is your company's subdomain. |
| Destination pattern | .* |
| Action | Reject |

| Step 1 | From the customer view in https://admin.webex.com , deactivate Hybrid Call Service Connect for your organization by going to Organization Services , choosing Edit settings on the Hybrid
                                          Call card, scrolling to Call Service Connect , and then clicking Deactivate . As soon as the service is deactivated, Hybrid Call Service calls will not
                                             route. This step is required to temporarily convert you to a cloud calling
                                             organization, which allows you to modify the SIP addresses for calling.
                                             After you see that Call Service Connect is disabled for the organization,
                                             you can proceed with the steps. |
|---|---|
| Step 2 | Go to Settings , scroll to SIP Address for Cisco Webex Calling , click Edit Subdomain , leave the same value or enter a new value as needed, click Check Availability , click Save and then click OK . This step triggers the migration process that converts the domains from Cisco Spark to Webex. You'll see a background task
                                             notification at the top of your Control Hub instance. You can click on the notification to see the status of the SIP address changes. Secondary SIP addresses with ciscospark.com remain if you don't change the subdomain value. If you do change the subdomain
                                             value, the ciscospark.com SIP address is not preserved. Note If any users or workspaces produce an error in the results, you can try
                                                         these steps to address the issue: Redo the preceding step to trigger the migration process again—you should see a Rerun button. If specific users or workspaces continue to produce errors, try
                                                               to edit the user or workspace in Control Hub without making any
                                                               changes and then click Save . If you rerun the migration step and still see users and
                                                               workspaces in error state, export the CSV file, open a case with the Cisco TAC , and
                                                               attach the CSV file to your case. | Note | If any users or workspaces produce an error in the results, you can try
                                                         these steps to address the issue: Redo the preceding step to trigger the migration process again—you should see a Rerun button. If specific users or workspaces continue to produce errors, try
                                                               to edit the user or workspace in Control Hub without making any
                                                               changes and then click Save . If you rerun the migration step and still see users and
                                                               workspaces in error state, export the CSV file, open a case with the Cisco TAC , and
                                                               attach the CSV file to your case. |
| Note | If any users or workspaces produce an error in the results, you can try
                                                         these steps to address the issue: Redo the preceding step to trigger the migration process again—you should see a Rerun button. If specific users or workspaces continue to produce errors, try
                                                               to edit the user or workspace in Control Hub without making any
                                                               changes and then click Save . If you rerun the migration step and still see users and
                                                               workspaces in error state, export the CSV file, open a case with the Cisco TAC , and
                                                               attach the CSV file to your case. |
| Step 3 | After the SIP address background task is completed and there are no errors, use Cisco Webex Control Hub to verify that the SIP addresses appear correctly for users and
                                          Workspaces: Where to Verify in Control Hub Expected Result Users Go to Users , click any user, click Calling , and then you'll see
                                                         the primary and backup SIP address entries. Workspaces Go to Workspaces , click any
                                                         workspace to open the overview pane, and then under Calling you'll see the
                                                         primary and backup SIP address entries. After you verify that the SIP addresses converted correctly to a Webex
                                             domain, you can reenable your organization with Hybrid Call Service
                                             Connect. | Where to Verify in Control Hub | Expected Result | Users | Go to Users , click any user, click Calling , and then you'll see
                                                         the primary and backup SIP address entries. |  | Workspaces | Go to Workspaces , click any
                                                         workspace to open the overview pane, and then under Calling you'll see the
                                                         primary and backup SIP address entries. |  |
| Where to Verify in Control Hub | Expected Result |
| Users |
| Go to Users , click any user, click Calling , and then you'll see
                                                         the primary and backup SIP address entries. |  |
| Workspaces |
| Go to Workspaces , click any
                                                         workspace to open the overview pane, and then under Calling you'll see the
                                                         primary and backup SIP address entries. |  |
| Step 4 | From the customer view in https://admin.webex.com , reactivate Hybrid Call Service Connect for your organization by going to Services > Hybrid , choosing Edit settings on the Hybrid
                                          Call card, scrolling to Call Service Connect , and then clicking Activate . After all the user and Workspace SIP addresses are changed on the cloud side
                                             and your organization is reenabled for Hybrid Call Service Connect, the Call
                                             Connector on Expressway needs to pick up on these changes and replicate them
                                             on the premises side. On Unified CM, the new Webex SIP addresses become the
                                             remote destination for each Cisco Spark-RD that is tied to a user or
                                             workspace account. |
| Step 5 | To synchronize these changes, choose an option: Wait for the daily user activation status validation, which occurs between 7 am and 11 am Universal Time Coordinated (UTC).
                                                   The changes are picked up through the Call Connector after this validation period. Restart each Call Connector by following these steps in the deployment guide . In a multicluster deployment, restarting the connector on the primary node automatically restarts the other connectors in
                                                   the cluster. The changes are picked up after the connector comes back online. Caution As mentioned in the deployment guide, restarting the Call Connector creates extra load on Unified CM publishers. Consider
                                                               restarting the Call Connector during off-peak hours; during busy hours, a restart may cause service issues. | Caution | As mentioned in the deployment guide, restarting the Call Connector creates extra load on Unified CM publishers. Consider
                                                               restarting the Call Connector during off-peak hours; during busy hours, a restart may cause service issues. |
| Caution | As mentioned in the deployment guide, restarting the Call Connector creates extra load on Unified CM publishers. Consider
                                                               restarting the Call Connector during off-peak hours; during busy hours, a restart may cause service issues. |
| Step 6 | Verify that the Cisco Spark-RDs are still listed: from Cisco Unified CM Administration, go to Device > Phone , and search on Cisco Spark Remote Device as the Device Type . |
| Step 7 | Verify that the remote destinations were created correctly: From Cisco Unified CM Administration, go to Device > Remote Destination , choose CTI Remote Device/Cisco Spark Remote Device from the Find destination where drop down, and then click Find . The results show each Cisco Spark Remote Device (Cisco Spark-RDs) in your
                                             deployment and the remote destination (under Destination
                                                Number . Your Cisco Spark-RDs have a remote destination
                                             subdomain calls.webex.com for users and rooms.webex.com for devices in a workspace. |
| Step 8 | Make test calls to verify that call behavior is as expected (for example, an
                                          incoming call rings both a Hybrid Call Service user's desk phone and Webex app. See the Test the Softphone Functionality for Hybrid Call
                                                Service procedure in the deployment guide for more
                                             information. |

| Note | If any users or workspaces produce an error in the results, you can try
                                                         these steps to address the issue: Redo the preceding step to trigger the migration process again—you should see a Rerun button. If specific users or workspaces continue to produce errors, try
                                                               to edit the user or workspace in Control Hub without making any
                                                               changes and then click Save . If you rerun the migration step and still see users and
                                                               workspaces in error state, export the CSV file, open a case with the Cisco TAC , and
                                                               attach the CSV file to your case. |
|---|---|

| Where to Verify in Control Hub | Expected Result |
|---|---|
| Users |
| Go to Users , click any user, click Calling , and then you'll see
                                                         the primary and backup SIP address entries. |  |
| Workspaces |
| Go to Workspaces , click any
                                                         workspace to open the overview pane, and then under Calling you'll see the
                                                         primary and backup SIP address entries. |  |

| Caution | As mentioned in the deployment guide, restarting the Call Connector creates extra load on Unified CM publishers. Consider
                                                               restarting the Call Connector during off-peak hours; during busy hours, a restart may cause service issues. |
|---|---|