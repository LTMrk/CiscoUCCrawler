---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-4590fd4af5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_011010.html
retrieved_at: 2026-08-16T17:31:11.102741+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Global Dial Plan Replication

## Chapter: Configure Global Dial Plan Replication

# Configure Global Dial Plan Replication

## Global Dial Plan
                        	 Replication Overview

Use global dial plan
                           		replication to create a global dial plan that spans across the Intercluster
                           		Lookup Service (ILS) network. When you enable Global Dial Plan Replication, you
                           		configure the dial plan component on one cluster, and ILS replicates that
                           		information throughout the ILS network.

When you enable Global Dial Plan Replication, each cluster in an ILS network advertises its global dial plan data, including
                           the global dial plan data that was configured locally and any data that was learned from other clusters, to the ILS network.
                           Global dial plan data includes the following:

Directory universal resource indicators (URIs)

Alternate numbers

Advertised patterns

PSTN failover

Route strings

Learned Global Dial Plan Data

Imported Global Dial Plan Data

### Directory
                              		  URIs

ILS advertises the full catalog of locally configured directory URIs when you choose Advertise Globally via ILS option. See the URI Dialing Overview for more information on how to configure URI dialing.

### Alternate
                              		  Numbers

Alternate numbers allow you to configure globally routable numbers that can be dialed from anywhere within an ILS network.
                              Cisco Unified Communications Manager allows you to create two types of alternate numbers:

Enterprise alternate numbers

+E.164 alternate numbers

### Advertised
                              		  Patterns

Advertised
                              		  patterns allow you to create summarized routing instructions for a range of
                              		  enterprise alternate numbers or +E.164 alternate numbers and replicate that
                              		  pattern throughout an ILS network so that all clusters within the ILS network
                              		  know the pattern. Advertised patterns prevent you from individually configuring
                              		  routing information for each alternate number. Advertised patterns are never
                              		  used by the local cluster on which they are configured; they are only used by
                              		  remote clusters that learn the pattern through ILS. You can also configure
                              		  Public Switched Telephone Network(PSTN) failover information for patterns that
                              		  are advertised by ILS.

### PSTN
                              		  Failovers

Unified Communications Manager uses a PSTN failover number to reroute only those calls that are placed to patterns, alternate numbers, or directory URIs
                              that were learned through ILS. Communications Manager does not reroute calls to the PSTN failover number for calls that are placed to locally configured patterns, alternate numbers,
                              and directory URIs.

When you enable Global Dial Plan Replication, you can configure ILS to replicate a PSTN failover rule for learned directory
                              URIs, learned numbers, and learned patterns. If the dial string for an outgoing call matches a learned pattern, learned alternate
                              number, or learned directory URI, and Unified Communications Manager cannot route the call over a SIP trunk, Unified Communications Manager uses the calling party's Automatic Alternate Routing (AAR) CSS to reroute the call to the associated PSTN failover number.

### Route
                              		  Strings

ILS advertises the local route string to the ILS network. Each global dial plan data element associates to a route string
                              that identifies the home cluster for that element. Remote clusters use the route string with a SIP route pattern to route
                              to the various clusters in an ILS network. When a user in a remote cluster dials a directory URI or alternate number that
                              was learned through ILS, Unified Communications Manager matches the associated route string to a SIP route pattern, and routes the call to the trunk that is specified by the SIP
                              route pattern.

When a user
                              		  assigns route string to a cluster, ILS associates that route string to all the
                              		  global dial plan data that is local to that cluster (including locally
                              		  configured directory URIs, alternate numbers, advertised patterns, and PSTN
                              		  failover information).

If the SIP Route Pattern name contains dashes, you must ensure that there are no numerical digits between dashes. However,
                                          you can use a combination of letters and numbers or letters only, if there are more than one dash.

Examples of right and wrong SIP Route Patterns are listed in the following:

Correct Patterns:

abc-1d-efg.xyz.com

123-abc-456.xyz.com

Incorrect Patterns :

abc-123-def.xyz.com

1bc-2-3ef.xyz.com

### Learned Global
                              		  Dial Plan Data

Unified Communications Manager stores in the local database all global dial plan data that is learned through ILS. In addition to replicating locally configured
                              data, ILS advertises all global dial plan data that the local cluster has learned from other clusters in the ILS network.
                              This ensures that all advertised data reaches each cluster in the ILS network. Learned global dial plan data includes learned
                              directory URIs, learned alternate numbers, learned patterns, learned PSTN failover rules, and learned route strings.

In Cisco Unified CM Administration, you can view the following types of learned global dial plan data:

Learned Alternate Numbers

Learned Enterprise and +E.164 Patterns

Learned Directory URIs

### Imported
                              		  Global Dial Plan Data

Unified Communications Manager allows you to import global dial plan data from a CSV file into any hub cluster in an ILS network. ILS replicates the imported
                              global dial plan data throughout the ILS network that allows you to interoperate Unified Communications Manager with a Cisco TelePresence Video Communications Server or a third-party call control system. Imported global dial plan data
                              includes directory URIs, +E.164 patterns, and PSTN failover rules that were imported manually from a CSV file

Imported data includes only global dial plan data that is imported manually into Unified Communications Manager . Imported global dial plan data does not include data that was learned through ILS.

## Global Dial Plan
                        	 Replication Prerequisites

Follow the procedures to set up an ILS network in the ILS Configuration Task Flow .

## Global Dial Plan
                        	 Replication Task Flow

Step 1

Enable ILS Support for Global Dial Plan Replication .

Step 2

Set Up Alternate Number .

(Optional) If
                                          				you want to set up alternate numbers that you can dial between clusters,
                                          				configure alternate number replication.

Step 3

Set Up Advertised Pattern for Alternate Numbers .

Step 4

Set Up PSTN Failover .

Step 5

Assign Partitions for Learned Numbers and Patterns .

(Optional)
                                          				Assign route partitions to the alternate numbers and patterns that the local
                                          				cluster learns through ILS.

Step 6

Block a Learned Pattern .

Step 7

Set Database Limits for Learned Data .

Step 8

Import Global Dial Plan Data .

(Optional) If you want your ILS network to interoperate with a Cisco TelePresence Video Communication Server or third-party
                                          call control system, import directory URI catalogs from a CSV file for the other system into any hub cluster in the ILS network.

### What to do next

If you want to dial directory universal resource indicators (URIs) across clusters, set up URI dialing in the local cluster.
                              For details, see the URI Dialing Overview .

### Enable ILS Support
                           	 for Global Dial Plan Replication

To enable ILS
                                 		  support for Global Dial Plan Replication in the local cluster, follow this
                                 		  procedure:

Step 1

Log in to the Cisco
                                             				Unified Communications Manager publisher node.

Step 2

From Cisco
                                          			 Unified CM Administration, choose Advanced
                                                				  Features > ILS Configuration .

Step 3

Check the Exchange Global Dial Plan Replication Data with Remote Clusters check box.

Step 4

In the Advertised Route String text box, enter a route
                                          			 string for the local cluster.

Step 5

Click Save .

### Set Up Alternate
                           	 Number

Create an
                                 		  enterprise alternate number or +E.164 alternate number and associate the
                                 		  alternate number with a directory number. When you dial the alternate number,
                                 		  the phone that is registered to the associated directory number, rings.

Each alternate
                                             			 number that you set up must associate with a single directory number. However,
                                             			 that directory number can associate to both an enterprise alternate number and
                                             			 a +E.164 alternate number at the same time.

#### Before you begin

Enable ILS Support for Global Dial Plan Replication .

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Directory Number .

Step 2

From the Find
                                             				and List Directory Numbers window, find and select the directory
                                          			 number to which you want to associate the alternate number.

Step 3

From the Directory Number Configuration window, click one of
                                          			 the following options depending on the type of alternate number that you want
                                          			 to assign:

Add Enterprise Alternate
                                                   					 Number .

Add +E.164 Alternate
                                                   					 Number .

Step 4

In the Number
                                             				Mask field, enter the number mask that you want to apply to the
                                          			 directory number.

The Alternate Number field displays how the alternate
                                             				number appears after Cisco
                                                				  Unified Communications Manager applies the number mask.

Step 5

(Optional) If
                                          			 you want to enable local routing for the alternate number, perform the
                                          			 following steps:

Check the Add to Local Route Partition check box.

From the Route Partition drop-down list, choose a route
                                                				  partition that is assigned to a local calling search space.

Step 6

(Optional) If
                                          			 you want to use a number pattern to set up intercluster routing for this
                                          			 alternate number, click Save .

Step 7

(Optional) If
                                          			 you want to set up intercluster routing for this alternate number, check the Advertise Globally via ILS check box for this
                                          			 alternate number.

Step 8

(Optional) If
                                          			 you want to assign a PSTN failover number to this alternate number, from the PSTN
                                             				failover drop-down list, assign a number as the PSTN failover.

Step 9

Click Save .

#### What to do next

Set Up Advertised Pattern for Alternate Numbers .

### Set Up Advertised
                           	 Pattern for Alternate Numbers

Use advertised patterns to summarize a range of Enterprise alternate numbers or E.164 alternate numbers. You can advertise
                                 the pattern to the ILS network to enable intercluster calling to numbers that match the pattern.

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan Replication > Advertised
                                                				  Patterns .

Step 2

From the Find and List Advertised Patterns window, do either of the following:

- Click Find and select an existing pattern.

- Click Add New to create a new pattern.

Step 3

In the Pattern field, enter the number pattern. For example, 54XXX summarizes a range of numbers between 54000 - 54999.

Step 4

In the Pattern Type field, select the pattern type: Enterprise Number Pattern or E.164 Number Pattern .

Step 5

From the radio buttons, select whether you want to apply a PSTN Failover.

- Don't use PSTN Failover

- Use Pattern as PSTN Failover

- Apply Strip Digits and Prepend Digits to Pattern and Use for PSTN Failover —If you choose this option, enter the digits in the PSTN Failover Strip Digits and PSTN Failover Prepend Digits fields.

Step 6

Click Save .

### Set Up PSTN
                           	 Failover

Perform the
                                 		  following procedure to assign a PSTN failover number for directory URIs or
                                 		  alternate numbers and advertise that PSTN failover number to the ILS network.
                                 		  Remote clusters can use the PSTN failover number for calls to learned directory
                                 		  URIs or learned alternate numbers.

#### Before you begin

Set Up Advertised Pattern for Alternate Numbers .

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Directory Number .

Step 2

From the Find
                                             				and List Directory Numbers window, find and select the directory
                                          			 number that is associated to the directory URI or alternate number for which
                                          			 you want to assign a PSTN failover number.

Step 3

(Optional) If
                                          			 the alternate number that you want to use as the PSTN failover does not exist,
                                          			 in the Directory Number Configuration window, choose one of
                                          			 the following options depending on the type of alternate number that you want
                                          			 to assign:

Add Enterprise Alternate
                                                   					 Number .

Add +E.164 Alternate
                                                   					 Number .

Step 4

In the PSTN
                                             				Failover drop-down list, choose the alternate number that you want
                                          			 to use as the PSTN failover.

Step 5

Click Save .

Cisco Unified
                                                				  Communications Manager associates that PSTN failover number to that
                                             				directory number. Global Dial Plan Replication advertises that number to the
                                             				ILS network as the PSTN failover number for all the directory URIs and
                                             				alternate numbers that are associated to that directory number.

#### What to do next

Assign Partitions for Learned Numbers and Patterns .

### Assign Partitions for Learned Numbers and Patterns

You must assign learned numbers and learned patterns to a partition. You can define your own partitions or use the predefined
                                 default partitions. Unified Communications Manager is installed with the following predefined partitions for learned alternate numbers and number patterns:

Global Learned Enterprise Numbers.

Global Learned E.164 Numbers.

Global Learned Enterprise Patterns.

Global Learned E.164 Patterns.

You cannot
                                             			 assign a learned number or learned pattern to a NULL partition.

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan Replication > Partitions for Learned
                                                				  Numbers and Patterns .

Step 2

Configure the fields in the Partitions for Learned Numbers and Patterns window. For more information on the fields and their configuration options, see the system Online Help.

Step 3

Click Save .

### Block a Learned
                           	 Pattern

Complete this optional task if you want to set up a blocking rule that prevents the local cluster from routing calls to specific
                                 enterprise alternate numbers, +E.164 alternate numbers, or number patterns that were learned through the ILS.

Before routing a call to a learned number or learned pattern, ILS checks to see if a local blocking rule matches the dial
                                 string. If the blocking rule matches, Unified Communications Manager does not route the call.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Global Dial Plan Replication > Block Learned Numbers and Patterns .

Step 2

Perform one of
                                          			 the following tasks:

- Click Find and select an existing blocking rule to edit.

- Click Add New to create a new blocking rule.

Step 3

In the Pattern field, enter the pattern or number that you want to block. For example, 206XXXXXXX can be used to block calls to 2065551212.

Step 4

If you want to block calls based on the dial string prefix, enter the Prefix .

Step 5

If you want to block calls from being sent to a specific cluster, enter the Cluster ID of the cluster.

Step 6

From the Pattern Type drop-down list, select how you want to apply the blocking rule:

- Any —Choose this option if the blocking rule applies to both enterprise number patterns and +E.164 patterns.

- Enterprise Pattern —Choose this option if the blocking rule applies to enterprise number patterns only.

- +E.164 Pattern —Choose this option if the blocking rule applies to +E.164 number patterns only.

Step 7

Click Save .

### Set Database
                           	 Limits for Learned Data

Set a database limit to determine the number of learned objects that Unified Communications Manager can write to the local
                                 database.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

Choose the Server where you want to configure the parameter.

Step 3

From the Service drop-down list, choose Cisco Intercluster Lookup Service (Active) . If the service does not appear as active, ensure that the service is activated in Cisco Unified Serviceability.

Step 4

Under Clusterwide Parameters (ILS) section, set an upper limit for the ILS Max Number of Learned Objects in Database service parameter.

Step 5

Click Save .

This service parameter determines the maximum number of entries that Unified Communications Manager can write to the database for data that is learned through ILS. The default value of the service parameter is 100,000 while
                                             the maximum value of the service parameter is 1,000,000.

If you reduce the service parameter to a value that is lower than the current number of ILS-learned entries that are saved
                                             in the database, Unified Communications Manager does not write additional ILS learned objects to the database. However, the existing database entries remain.

### Import Global Dial
                           	 Plan Data

#### Before you begin

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan RepIication > Imported Global Dial Plan
                                                				  Catalog .

Step 2

From the Find
                                             				and List Imported Global Dial Plan Catalogs window, perform one of
                                          			 the following tasks:

- Click Find and select an existing catalog from the resulting list.

- Click Add New to add a new catalog.

Step 3

From the Imported Global Dial Plan Catalog Settings window, in
                                          			 the Name field, enter a unique name to identify the
                                          			 catalog that you want to import.

Step 4

(Optional) In the Description field, enter a description of the catalog.

Step 5

In the Route
                                             				String field, create a route string for the system from which you
                                          			 are importing the catalog.

Step 6

Click Save .

Step 7

From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files .

- Click Add New .

- Click Browse and select the CSV file for the catalog that you want to import.

Step 8

In the Select
                                             				the Target drop-down list, select Imported Directory URIs and Patterns .

Step 9

In the Select
                                             				Transaction Type drop-down list, select Insert
                                             				Imported Directory URIs and Patterns .

Step 10

Click Save .

Step 11

From Cisco Unified CM Administration, choose Bulk Administration > Directory URIs and Patterns > Insert Imported Directory URIs and Patterns .

Step 12

In the File
                                             				Name drop-down list, choose the CSV file that contains the catalog
                                          			 that you want to import.

Step 13

In the Imported Directory URI Catalog drop-down list,
                                          			 choose the catalog that you named in the Imported Global Dial Plan Catalog window.

Step 14

In the Job
                                             				Description text box, enter a name for the job that you are about
                                          			 to run.

Step 15

Perform one of
                                          			 the following steps:

- If you want to run the job
                                             				now, select the Run
                                                				  Immediately option, and click Submit .

- If you want to schedule the
                                             				job to run at a specified time, select the Run
                                                				  Later radio button and click Submit .

| Note | If the SIP Route Pattern name contains dashes, you must ensure that there are no numerical digits between dashes. However,
                                          you can use a combination of letters and numbers or letters only, if there are more than one dash. Examples of right and wrong SIP Route Patterns are listed in the following: Correct Patterns: abc-1d-efg.xyz.com 123-abc-456.xyz.com Incorrect Patterns : abc-123-def.xyz.com 1bc-2-3ef.xyz.com |
|---|---|

| Note | Imported data includes only global dial plan data that is imported manually into Unified Communications Manager . Imported global dial plan data does not include data that was learned through ILS. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable ILS Support for Global Dial Plan Replication . | Enable ILS
                                       			 support for Global Dial Plan Replication to share dial plan information between
                                       			 participating ILS-enabled clusters. |
| Step 2 | Set Up Alternate Number . | (Optional) If
                                          				you want to set up alternate numbers that you can dial between clusters,
                                          				configure alternate number replication. |
| Step 3 | Set Up Advertised Pattern for Alternate Numbers . | (Optional) If
                                       			 you want to summarize your alternate numbers with a pattern, set up an
                                       			 advertised pattern, and assign a PSTN failover rule for the pattern. |
| Step 4 | Set Up PSTN Failover . | (Optional) If
                                       			 you want to set up a PSTN failover number for specific directory URIs or
                                       			 alternate numbers, assign an alternate number as the PSTN failover number for
                                       			 all the directory URIs and alternate numbers that are associated to a specific
                                       			 directory number. |
| Step 5 | Assign Partitions for Learned Numbers and Patterns . | (Optional)
                                          				Assign route partitions to the alternate numbers and patterns that the local
                                          				cluster learns through ILS. |
| Step 6 | Block a Learned Pattern . | (Optional) To prevent a local Unified Communications Manager cluster from routing calls to a learned alternate number or learned alternate number pattern, you can configure a local blocking
                                       rule on that cluster. |
| Step 7 | Set Database Limits for Learned Data . | Set a database limit to determine the number of learned objects that Unified Communications Manager can write to the local database. |
| Step 8 | Import Global Dial Plan Data . | (Optional) If you want your ILS network to interoperate with a Cisco TelePresence Video Communication Server or third-party
                                          call control system, import directory URI catalogs from a CSV file for the other system into any hub cluster in the ILS network. |

| Step 1 | Log in to the Cisco
                                             				Unified Communications Manager publisher node. |
|---|---|
| Step 2 | From Cisco
                                          			 Unified CM Administration, choose Advanced
                                                				  Features > ILS Configuration . |
| Step 3 | Check the Exchange Global Dial Plan Replication Data with Remote Clusters check box. |
| Step 4 | In the Advertised Route String text box, enter a route
                                          			 string for the local cluster. |
| Step 5 | Click Save . |

| Note | Each alternate
                                             			 number that you set up must associate with a single directory number. However,
                                             			 that directory number can associate to both an enterprise alternate number and
                                             			 a +E.164 alternate number at the same time. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Directory Number . |
|---|---|
| Step 2 | From the Find
                                             				and List Directory Numbers window, find and select the directory
                                          			 number to which you want to associate the alternate number. |
| Step 3 | From the Directory Number Configuration window, click one of
                                          			 the following options depending on the type of alternate number that you want
                                          			 to assign: Add Enterprise Alternate
                                                   					 Number . Add +E.164 Alternate
                                                   					 Number . |
| Step 4 | In the Number
                                             				Mask field, enter the number mask that you want to apply to the
                                          			 directory number. The Alternate Number field displays how the alternate
                                             				number appears after Cisco
                                                				  Unified Communications Manager applies the number mask. |
| Step 5 | (Optional) If
                                          			 you want to enable local routing for the alternate number, perform the
                                          			 following steps: Check the Add to Local Route Partition check box. From the Route Partition drop-down list, choose a route
                                                				  partition that is assigned to a local calling search space. |
| Step 6 | (Optional) If
                                          			 you want to use a number pattern to set up intercluster routing for this
                                          			 alternate number, click Save . |
| Step 7 | (Optional) If
                                          			 you want to set up intercluster routing for this alternate number, check the Advertise Globally via ILS check box for this
                                          			 alternate number. |
| Step 8 | (Optional) If
                                          			 you want to assign a PSTN failover number to this alternate number, from the PSTN
                                             				failover drop-down list, assign a number as the PSTN failover. |
| Step 9 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan Replication > Advertised
                                                				  Patterns . |
|---|---|
| Step 2 | From the Find and List Advertised Patterns window, do either of the following: Click Find and select an existing pattern. Click Add New to create a new pattern. |
| Step 3 | In the Pattern field, enter the number pattern. For example, 54XXX summarizes a range of numbers between 54000 - 54999. |
| Step 4 | In the Pattern Type field, select the pattern type: Enterprise Number Pattern or E.164 Number Pattern . |
| Step 5 | From the radio buttons, select whether you want to apply a PSTN Failover. Don't use PSTN Failover Use Pattern as PSTN Failover Apply Strip Digits and Prepend Digits to Pattern and Use for PSTN Failover —If you choose this option, enter the digits in the PSTN Failover Strip Digits and PSTN Failover Prepend Digits fields. |
| Step 6 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Directory Number . |
|---|---|
| Step 2 | From the Find
                                             				and List Directory Numbers window, find and select the directory
                                          			 number that is associated to the directory URI or alternate number for which
                                          			 you want to assign a PSTN failover number. The
                                          			 appears. |
| Step 3 | (Optional) If
                                          			 the alternate number that you want to use as the PSTN failover does not exist,
                                          			 in the Directory Number Configuration window, choose one of
                                          			 the following options depending on the type of alternate number that you want
                                          			 to assign: Add Enterprise Alternate
                                                   					 Number . Add +E.164 Alternate
                                                   					 Number . |
| Step 4 | In the PSTN
                                             				Failover drop-down list, choose the alternate number that you want
                                          			 to use as the PSTN failover. |
| Step 5 | Click Save . Cisco Unified
                                                				  Communications Manager associates that PSTN failover number to that
                                             				directory number. Global Dial Plan Replication advertises that number to the
                                             				ILS network as the PSTN failover number for all the directory URIs and
                                             				alternate numbers that are associated to that directory number. |

| Note | You cannot
                                             			 assign a learned number or learned pattern to a NULL partition. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan Replication > Partitions for Learned
                                                				  Numbers and Patterns . |
|---|---|
| Step 2 | Configure the fields in the Partitions for Learned Numbers and Patterns window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 3 | Click Save . Note The route partition must also exist in the calling search space that is used by the calling party in order for calls to be
                                                      placed to numbers in the partition. | Note | The route partition must also exist in the calling search space that is used by the calling party in order for calls to be
                                                      placed to numbers in the partition. |
| Note | The route partition must also exist in the calling search space that is used by the calling party in order for calls to be
                                                      placed to numbers in the partition. |

| Note | The route partition must also exist in the calling search space that is used by the calling party in order for calls to be
                                                      placed to numbers in the partition. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Global Dial Plan Replication > Block Learned Numbers and Patterns . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: Click Find and select an existing blocking rule to edit. Click Add New to create a new blocking rule. |
| Step 3 | In the Pattern field, enter the pattern or number that you want to block. For example, 206XXXXXXX can be used to block calls to 2065551212. |
| Step 4 | If you want to block calls based on the dial string prefix, enter the Prefix . |
| Step 5 | If you want to block calls from being sent to a specific cluster, enter the Cluster ID of the cluster. |
| Step 6 | From the Pattern Type drop-down list, select how you want to apply the blocking rule: Any —Choose this option if the blocking rule applies to both enterprise number patterns and +E.164 patterns. Enterprise Pattern —Choose this option if the blocking rule applies to enterprise number patterns only. +E.164 Pattern —Choose this option if the blocking rule applies to +E.164 number patterns only. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | Choose the Server where you want to configure the parameter. |
| Step 3 | From the Service drop-down list, choose Cisco Intercluster Lookup Service (Active) . If the service does not appear as active, ensure that the service is activated in Cisco Unified Serviceability. |
| Step 4 | Under Clusterwide Parameters (ILS) section, set an upper limit for the ILS Max Number of Learned Objects in Database service parameter. |
| Step 5 | Click Save . |

| Note | This service parameter determines the maximum number of entries that Unified Communications Manager can write to the database for data that is learned through ILS. The default value of the service parameter is 100,000 while
                                             the maximum value of the service parameter is 1,000,000. If you reduce the service parameter to a value that is lower than the current number of ILS-learned entries that are saved
                                             in the database, Unified Communications Manager does not write additional ILS learned objects to the database. However, the existing database entries remain. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan RepIication > Imported Global Dial Plan
                                                				  Catalog . |
|---|---|
| Step 2 | From the Find
                                             				and List Imported Global Dial Plan Catalogs window, perform one of
                                          			 the following tasks: Click Find and select an existing catalog from the resulting list. Click Add New to add a new catalog. |
| Step 3 | From the Imported Global Dial Plan Catalog Settings window, in
                                          			 the Name field, enter a unique name to identify the
                                          			 catalog that you want to import. |
| Step 4 | (Optional) In the Description field, enter a description of the catalog. |
| Step 5 | In the Route
                                             				String field, create a route string for the system from which you
                                          			 are importing the catalog. Note Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. | Note | Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. |
| Note | Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. |
| Step 6 | Click Save . |
| Step 7 | From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files . Click Add New . Click Browse and select the CSV file for the catalog that you want to import. Note Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). | Note | Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). |
| Note | Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). |
| Step 8 | In the Select
                                             				the Target drop-down list, select Imported Directory URIs and Patterns . |
| Step 9 | In the Select
                                             				Transaction Type drop-down list, select Insert
                                             				Imported Directory URIs and Patterns . |
| Step 10 | Click Save . |
| Step 11 | From Cisco Unified CM Administration, choose Bulk Administration > Directory URIs and Patterns > Insert Imported Directory URIs and Patterns . |
| Step 12 | In the File
                                             				Name drop-down list, choose the CSV file that contains the catalog
                                          			 that you want to import. |
| Step 13 | In the Imported Directory URI Catalog drop-down list,
                                          			 choose the catalog that you named in the Imported Global Dial Plan Catalog window. |
| Step 14 | In the Job
                                             				Description text box, enter a name for the job that you are about
                                          			 to run. |
| Step 15 | Perform one of
                                          			 the following steps: If you want to run the job
                                             				now, select the Run
                                                				  Immediately option, and click Submit . If you want to schedule the
                                             				job to run at a specified time, select the Run
                                                				  Later radio button and click Submit . Note If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. Cisco Unified Communications Manager saves all imported +E.164 patterns to the Global Learned +E.164 Patterns partition. | Note | If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. |
| Note | If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. |

| Note | Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. |
|---|---|

| Note | Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). |
|---|---|

| Note | If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. |
|---|---|

| Note | You can also export all locally configured directory URIs, +E.164 number patterns, and their associated PSTN failover rules
                                          to a CSV file that you can import into the other call control system. Refer to the menus at Bulk Administration > Directory URIs and Patterns > Export Local Directory URIs and Patterns for details. |
|---|---|