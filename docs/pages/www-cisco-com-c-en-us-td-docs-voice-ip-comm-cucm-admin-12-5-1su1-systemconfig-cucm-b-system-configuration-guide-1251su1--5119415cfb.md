---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-systemconfig-cucm-b-system-configuration-guide-1251su1--5119415cfb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/systemConfig/cucm_b_system-configuration-guide-1251su1/cucm_b_system-configuration-guide-1251su1_restructured_chapter_0100011.html
retrieved_at: 2026-08-16T17:49:08.949808+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Configure Global Dial Plan Replication

## Chapter: Configure Global Dial Plan Replication

# Configure Global Dial Plan Replication

## Global Dial Plan Replication Overview

Global Dial Plan Replication makes it easy to set up an intercluster VoIP network with video calling that uses either URI
                              dialing, enterprise numbers or E.164 numbers for dialing.

Global Dial Plan Replication leverages the Cisco Intercluster Lookup Service by replicating global dial plan data elements
                              to the remote clusters in an ILS network. Each cluster in the ILS network learns the Global Dial Plan elements of the other
                              clusters, along with the route string for the home cluster.

### Advertised Globally via ILS

Global Dial Plan Replication advertises the following dial plan elements to the ILS network, replicating this data in remote
                              clusters:

Directory URIs —In the local cluster, provision email-style directory URIs (e.g. alice@cisco.com). URI dialing provides a user-centric method
                                    of placing calls. Global Dial Plan Replication lets you advertise the local catalog of directory URIs to the other clusters
                                    in the ILS network to enable intercluster URI dialing.

Enterprise and E.164 Alternate Numbers —Alternate numbers are aliases of the original extension that are created by applying a mask with prepend digit instructions
                                    to the original directory number. Alternate numbers can be dialed from anywhere within an ILS network. There are two types
                                    of alternate numbers. You can provision alternate numbers in the local cluster and then either advertise each numbers to the
                                    ILS network or configure advertised number patterns that summarize a range of alternate numbers, and advertise the pattern
                                    to the ILS network.

Advertised patterns —Advertised patterns summarize a range of enterprise alternate numbers or +E.164 alternate numbers. You can replicate the
                                    pattern throughout an ILS network, rather than individual alternate numbers in order to save database space in the remote
                                    cluster. Advertised patterns are only used from remote clusters in the ILS network—you cannot use these patterns to route
                                    local calls.

PSTN failover numbers —This option lets you assign the Enterprise Alternate Number or E.164 Alternate Number as a PSTN failover number. If call
                                    routing to a global dial plan element fails via VoIP channels, the failover number provides an alternate routing method. In
                                    the remote cluster, you must configure route patterns that route the PSTN failover to an appropriate gateway.

Route string —Each cluster has a route string that gets replicated with along with the global dial plan catalog. The route string identifies
                                    the home cluster for a directory URI or alternate number. For intercluster calling, you must configure SIP route patterns
                                    in each remote cluster that route the route string back to its home cluster.

Learned Global Dial Plan Data —To ensure that replicated data reaches all clusters in the ILS network, each cluster replicates its locally provisioned global
                                    dial plan data, along with catalogs that were learned from other clusters.

Imported Global Dial Plan Data — If you are interoperating Cisco Unified Communications Manager with a Cisco TelePresence Video Communications Server, or
                                    a third-party call control system, export global dial plan data from the other system to a csv file, and then import that
                                    csv file into a hub cluster in the ILS network. Global Dial Plan Replication replicates the imported catalog to other clusters
                                    in the ILS network, allowing you to place calls to directory URIs and alternate numbers that are registered to the other system.

### Sample Global Dial Plan Mapping

The following example shows sample Global Dial Plan data elements that map to phone extension 4001. Assuming call routing
                              is configured correctly, dialing any of these numbers will ring extension 4001.

Enterprise Alternate Number—A number mask of 5XXXX applied to extension 4001 creates an enterprise alternate number of 54001.

E164 Alternate Number—A number mask of 1972555XXXX applied to extension 4001 creates an +E.164 alternate number of 19725554001.

PSTN Failover—Assign the enterprise alternate Number or +E.164 alternate number as the PSTN failover and route the call to
                                    an appropriate gateway.

Advertised Pattern—The pattern 54XXX can be used to summarize all Enterprise Alternate Numbers in the 54000-54999 range. You
                                    can create patterns for Enteprise and +E.164 alternate numbers.

Directory URIs— alice@cisco.com

### URI Dialing

URI dialing is a subfeature of Global Dial Plan Replication that allows callers to place calls using directory URIs as the
                                 dial string. A directory URI is an alphanumeric text string that looks like an email addresses (for example, alice@cisco.com ).

Although the URI resembles an email address, a directory URI is not a routable entity by itself. For local calling, calls
                                 to directory URIs can be routed so long as the directory URI is in a partition that is within the caller's calling search
                                 space. For intercluster calls, the system pulls the cluster route string that was replicated with Global Dial Plan Replication
                                 and tries to match a SIP route pattern to the route string.

#### Directory URI Types

There are two types of directory URIs, with the type being determined by how you provision the directory URI:

User-based URIs—The directory URI is assigned to a user in End User Configuration . All of these URIs get assigned automatically to the local directory URI partition, which is a local nondeletable partition.
                                       If the user also has a primary extension, the URI also appears in Directory Number Configuration as the Primary URI for that extension.

Line-based URIs—Up to five additional directory URIs can be assigned directly to a directory number in the Directory Number Configuration window. For these URIs, you can assign any local partition.

#### Directory URI
                              	 Format

Directory URIs are alphanumeric strings that consist of a user and a host address separated by the @ symbol.

Cisco Unified Communications Manager supports the following formats for directory URIs:

user@domain (for example, joe@cisco.com)

user@ip_address (for example, joe@10.10.10.1)

The system supports the following formats in the user portion of a directory URI (the portion before the @ symbol):

Accepted characters are a-z, A-Z, 0-9, !, $, %, &, *, _, +, ~, -, =, , ?, , ‘, ,, ., /, ( and ) .

The user portion has a maximum length of 47 characters.

Cisco Unified Communications Manager automatically applies percent encoding to the following characters when the directory
                                          URI is saved in the database:

# % ^ ` { } | \ : ” < > [ ] \ ‘ and spaces.

The user portion of a directory URI is case sensitive by default. You can edit the user portion to be case insensitive by
                                                editing the URI Lookup Policy enterprise parameter.

Cisco Unified
                                    		  Communications Manager supports the following formats in the host portion of a
                                    		  directory URI (the portion after the @ symbol):

Supports IPv4
                                          				addresses or fully qualified domain names.

Accepted
                                          				characters are alphanumeric characters, hyphens (-), and dots (.).

The host
                                          				portion cannot start or end with a hyphen (-).

The host
                                          				portion cannot have two dots in a row.

The host
                                          				portion has a minimum length of two characters.

The host
                                          				portion is not case sensitive.

Within Cisco Unified Communications Manager Administration , when you use Bulk Administration to import a CSV file that contains directory URIs with embedded double quotes and commas,
                                                you must enclose the entire directory URI in double quotes (").

#### Call Forward to URI

Call-forwarding to URIs won't be possible from physical phones.

Call-forward to a URI can only be configured through applications if that URI is already in the Unified Communications Manager database. If the URI is not in the database, then the application will error out "Call Forward Setting Failed /n Failed to
                                       forward calls to: New Number" while trying to configure call-forward.

Call-forward can be configured for any URI, whether the URI exists in the database or not through the Unified Communications
                                       Manager Administration page.

You can configure call-forwards on the Cisco Unified Communications Self Care Portal > End User Page to any URI, regardless of whether it exists in the database. The 'Percent Encoding' must be used when entering these
                                       characters # % ^ ` { } | \ : ? < > [ ] \ ‘ . For example, %3A is used for mentioning : and %20 is used for mentioning space.

You must provide " mobile%3A%2012345@cisco.com " under the Call-Forward section of the Cisco Unified Communications Self Care Portal > End User page, if you need to forward calls to the URI " mobile: 12345@cisco.com ".

### Call Routing for Global Dial Plan Replication

For intracluster calling, Global Dial Plan Data is routed via partitions and calling search spaces. For calls to a local directory
                                 URI, enterprise alternate number or E.164 alternate number to work, the URI or number must be present in a partition that
                                 is in the calling search space that the calling party is using.

Intercluster calling uses the cluster route strings that Global Dial Plan Replication advertises to send the call to the called
                                 party's home cluster. When a caller places a call to a directory URI or alternate number that is homed in another cluster,
                                 the system pulls the associated route string, matches a SIP route pattern for the route string, and sends the call to the
                                 destination that the SIP route pattern specifies. For this to work, you must configure SIP route patterns in your remote clusters
                                 to route the route string back to its home cluster.

If call routing fails, the system can also use the associated PSTN failover number. However, you will need to configure route
                                 patterns in the remote cluster so that PSTN failover calls can be sent to the appropriate gateway.

## Global Dial Plan Replication Prerequisites

You must:

Configure the Cisco Intercluster Lookup Service (ILS)

Plan how you are going to deploy your global dial plan:

Will you deploy URI dialing by provisioning directory URIs for your users? You can use Global Dial Plan Replication to replicate
                                          directory URIs across the ILS network.

Will you deploy alternate number dialing? Will you use enterprise alternate numbers or E.164 alternate numbers? Which will
                                          you use as the PSTN failover?

If you are deploying alternate numbers, plan your numbering plan. For large networks, you can save on database space and bandwidth
                                          by advertising number patterns to the ILS network rather than individual alternate numbers.

## Global Dial Plan Replication Configuration Task Flow

Step 1

Enable ILS Support for Global Dial Plan Replication

Enable support for Global Dial Plan Replication in the local cluster.

Step 2

Configure SIP Profiles

Configure SIP settings that support Global Dial Plan Replication and URI Dialing.

Step 3

Configure SIP Trunks for URI Dialing

For URI dialing, configure whether the system inserts a directory URI, directory number, or blended address in  Contact headers.

Step 4

Configure SIP Route Patterns

For intercluster routing, configure SIP route patterns in each cluster that route the learned route strings back to their
                                          home clusters.

Step 5

Set Database Limits for Learned Data

Set the upper limit for the amount of data that ILS can write to the local database.

Step 6

Assign Partitions for Learned Numbers and Patterns

Assign route partitions for enterprise alternate numbers, +E.164 alternate numbers, and learned number patterns.

Step 7

Set Up Advertised Pattern for Alternate Numbers

Optional. Advertise a number pattern that summarizes a range of enterprise or +E.164 alternate numbers.

Step 8

Block a Learned Pattern

Optional. Configure a pattern that blocks calls to a specific number or number pattern. This configuration is applied locally,
                                          and is not replicated to the ILS network.

Step 9

Import Global Dial Plan Data

Optional. If you are interoperating with a Cisco TelePresence Video Communications Server or third-party call control system,
                                          import a catalog of directory URIs, +E.164 Numbers and PSTN failover numbers from the other system into a hub cluster in the
                                          ILS network.

Step 10

Provision Global Dial Plan Data

Assign directory URIs, enterprise alternate numbers, and +E.164 alternate numbers to a directory number.

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

### Configure SIP Profiles

Step 1

In Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Click Find and select an existing SIP Profile.

Step 3

From the Dial String Interpretation drop-down, configure the policy the system uses to determine whether to route calls as directory URIs or as directory numbers:

- Always treat all dial strings as URI addresses

- Phone number consists of characters 0–9, A–D, *, and + (others treated as URI addresses).

- Phone number consists of characters 0-9, *, and + (others treated as URI addresses)—This is the default option.

Step 4

Check the Use Fully Qualified Domain Name in SIP Requests check box.

Step 5

Optional. Under Trunk-Specific Configuration , check the Send ILS Learned Destination Route String check box if you want to be able to route intercluster calls across a Cisco Unified Border Element.

Step 6

Click Save .

### Configure SIP
                           	 Trunks for URI Dialing

If you are deploying URI dialing, configure the contact header addressing policy for the SIP trunks in your network. Cisco Unified Communications Manager can insert a directory number, directory URI, or a blended address that includes both the directory number and directory
                                 URI in the SIP identity headers for outgoing SIP messages.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Click Find and select an existing SIP trunk.

Step 3

In the Outbound Calls area, select one of the following from the Calling and Connected Party Info Format drop-down list:

- Deliver DN only in connected party —In outgoing SIP messages, Unified Communications Manager inserts the calling party’s directory number in the SIP contact
                                             header information. This is the default setting.

- Deliver URI only in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts the sending party’s directory URI in the SIP contact header.
                                             If a directory URI is not available, Unified Communications Manager inserts the directory number instead.

- Deliver URI and DN in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts a blended address that includes the calling party's directory
                                             URI and directory number in the SIP contact headers. If a directory URI is not available, Unified Communications Manager includes
                                             the directory number only.

Step 4

Click Save .

### Configure SIP Route Patterns

Step 1

From Cisco Unified CM Administration, choose Call Routing > SIP Route Pattern .

Step 2

Click Add New .

Step 3

From the Pattern Usage drop-down, select Domain Routing .

Step 4

Depending on whether you are deploying IPv4 or IPv6, enter the route string in the IPv4 Address or IPv6 Address text box.

Step 5

Under SIP Trunk/Route List , select a SIP trunk or route list that leads to the next- hop cluster for the route back to the route string's home cluster.

Step 6

Complete the remaining fields in the SIP Route Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 7

Click Save .

Step 8

Create SIP route patterns for each learned route string.

Step 9

Repeat these tasks for each cluster in the ILS network.

If the SIP Route Pattern name contains dashes, you must ensure that there are no numerical digits between dashes. However,
                                             you can use a combination of letters and numbers or letters only, if there is more than one dash. Examples of right and wrong
                                             SIP Route Patterns are listed in the following:

Correct Patterns:

abc-1d-efg.xyz.com

123-abc-456.xyz.com

Incorrect Patterns :

abc-123-def.xyz.com

1bc-2-3ef.xyz.com

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

### Provision Global Dial Plan Data

Step 1

From Cisco Unified CM Administration, choose Call Routing > Directory Number .

Step 2

Do either of the following:

- Click Find and select an existing directory number for which you want to add global dial plan data.

- Click Add New to create a new directory number.

Step 3

If you are creating a new number, enter the Directory Number and click Save .

Step 4

To add an enterprise alternate number click the the Add an Enterprise Alternate Number button and do the following:

Enter a Number Mask . For example, 5XXXX as an alternate number for 4001. The resulting enterprise alternate number (54001) displays in the Alternate Number field.

Check the Add to Local Route Partition check box to add to a local route partition.

From the Route Partition drop-down, select the partition.

Check Advertise Globally via ILS if you want this alternate number to be advertised to the ILS network.

Step 5

To add an +E.164 Alternate Number, click the Add an +E.164 Alternate Number and do the following:

Enter a Number Mask . For example, 1972555XXXX as an alternate number for extension 4001. The resulting +E.164 alternate number (19725554001)
                                                displays in the Alternate Number field.

Check the Add to Local Route Partition check box to add to a local route partition.

From the Route Partition drop-down, select the partition.

Check Advertise Globally via ILS if you want this alternate number to be advertised to the ILS network.

Step 6

In the Directory URIs section, add directory URIs to this directory number:

In the URI field, enter the directory URI. For example, alice@cisco.com.

From the Partition drop-down, assign the directory URI to a local partition.

Check the Advertise Globally via ILS check box to include this directory URI in advertised catalogs.

Click Add Row to add additional directory URIs. You can add up to five directory URIs.

Step 7

In the Advertised Failover Number field, select either the Enterprise Alternate Number or +E.164 Alternate Number as a PSTN failover.

Step 8

Configure the remaining fields in the Directory Number Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 9

Click Save .

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

## Global Dial Plan Replication Interactions and Restrictions

The following table summarizes some of the feature interactions for Global Dial Plan Replication and URI dialing.

Feature

Interactions and Restrictions

Export Directory URIs and +E.164 Patterns

You can also export all directory URIs and +E.164 number patterns that were configured in the local cluster, and export them
                                          to a csv file that you can import into another system.

In Cisco Unified CM Administration, choose Bulk Adminstration > Directory URIs and Patterns > Export Local Directory URIs and Patterns .

Click one of the following radio buttons to define the domain name that you want to attach to the export file:

Organizational Top Level Domain —Click this radio button to use the value of the Organizational Top Level Domain enterprise parameter for the export file
                                                      domain name.

Route String Domain —Click this radio button to use the value of the Route String field, as configured in ILS Configuration, for the export file
                                                      domain name.

User Defined Domain —Click this radio button to create a customized domain name to attach to the export file. If you choose this option, enter
                                                      the domain name in the Domain Name text box.

Click the Export Local Directory URIs and Patterns button.

Save the CSV file to a local drive

Partitioning with URI Dialing

Partitioning with directory URIs depends on how you provision the directory URI.

For user-based directory URIs that are assigned to an end user in End User Configuration , the local nondeletable Directory URI partition is assigned to the URI automatically. You cannot assign another partition,
                                                but you can use an administrator-managed partition as an alias for the local Directory URI partition by configuring the Directory URI Alias Partition enterprise parameter.

For line-based directory URIs where the URI is assigned directly to a directory number in Directory Number Configuration , you can assign each URI to a local partition separately.

If you are using tools like LDAP sync and Bulk Administration to provision directory URIs:

Directory URIs that are provisioned via an LDAP sync are user-based and get assigned to the user in End User Configuration . These URIs are assigned to the local Directory URI partition. If the user has a primary extension, the URI also appears
                                                in Directory Number Configuration as the Primary URI. However, the assigned partition is the Directory URI partition.

For directory URIs that are provisioned via Bulk Administration, it depends on how your updates are applied. For example,
                                                if you use the bat.xlt spreadsheet to create a csv import file, the user will be a user-based URI if you use the Users or Update Users tabs on the spreadsheet to add the directory URI. However, if you add the directory URI via the Line Fields options that appear when you click Create File Format , you can assign the URI to a directory number and assign a local partition to the URI directly.

Directory URI Case Sensitivity

By default, the user portion of a directory URI (the portion before the @) is case sensitive. You can make the user portion
                                          case insensitive by editing the URI Lookup Policy enterprise parameter.

Calling Search Space

To be dialable, directory URIs, enterprise alternate numbers, and +E.164 alternate numbers must be in a partition that is
                                          available in the calling party's calling search space.

Digit Transformations with URI dialing

If you use digit transformations, and you are deploying intercluster URI dialing, apply digit transformations against either
                                          the phone configuration or against the device pool that the phone uses.

For individual phones, apply the transformation to the Calling Party Transformation CSS field in the Remote Number section.

For device pools, you can apply the transformation against the Calling Party Transformation CSS field under Device Mobility Related Information .

| Note | Directory URIs can be assigned to a directory number or to an end user. Directory URIs that are associated to an end user
                                             will also associate to the user's primary extension (a directory number) and will ring the primary extension, provided it
                                             is assigned. |
|---|---|

| Note | The user portion of a directory URI is case sensitive by default. You can edit the user portion to be case insensitive by
                                                editing the URI Lookup Policy enterprise parameter. When you apply percent encoding, the digit length of the directory URI increases. For example, if you input joe smith#@cisco.com
                                             (20 characters) as a directory URI, Unified Communications Manager stores the directory URI in the database as joe%20smith%23@cisco.com (24 characters). Due to database restrictions, the Directory URI field has a maximum length of 254 characters. |
|---|---|

| Note | Within Cisco Unified Communications Manager Administration , when you use Bulk Administration to import a CSV file that contains directory URIs with embedded double quotes and commas,
                                                you must enclose the entire directory URI in double quotes ("). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable ILS Support for Global Dial Plan Replication | Enable support for Global Dial Plan Replication in the local cluster. |
| Step 2 | Configure SIP Profiles | Configure SIP settings that support Global Dial Plan Replication and URI Dialing. |
| Step 3 | Configure SIP Trunks for URI Dialing | For URI dialing, configure whether the system inserts a directory URI, directory number, or blended address in  Contact headers. |
| Step 4 | Configure SIP Route Patterns | For intercluster routing, configure SIP route patterns in each cluster that route the learned route strings back to their
                                          home clusters. |
| Step 5 | Set Database Limits for Learned Data | Set the upper limit for the amount of data that ILS can write to the local database. |
| Step 6 | Assign Partitions for Learned Numbers and Patterns | Assign route partitions for enterprise alternate numbers, +E.164 alternate numbers, and learned number patterns. |
| Step 7 | Set Up Advertised Pattern for Alternate Numbers | Optional. Advertise a number pattern that summarizes a range of enterprise or +E.164 alternate numbers. |
| Step 8 | Block a Learned Pattern | Optional. Configure a pattern that blocks calls to a specific number or number pattern. This configuration is applied locally,
                                          and is not replicated to the ILS network. |
| Step 9 | Import Global Dial Plan Data | Optional. If you are interoperating with a Cisco TelePresence Video Communications Server or third-party call control system,
                                          import a catalog of directory URIs, +E.164 Numbers and PSTN failover numbers from the other system into a hub cluster in the
                                          ILS network. |
| Step 10 | Provision Global Dial Plan Data | Assign directory URIs, enterprise alternate numbers, and +E.164 alternate numbers to a directory number. Note For multiple users, use an LDAP directory sync or Bulk Administration to assign global dial plan data for a large number of
                                                   users in a single operation. Refer to the Provisioning Users section of this guide. | Note | For multiple users, use an LDAP directory sync or Bulk Administration to assign global dial plan data for a large number of
                                                   users in a single operation. Refer to the Provisioning Users section of this guide. |
| Note | For multiple users, use an LDAP directory sync or Bulk Administration to assign global dial plan data for a large number of
                                                   users in a single operation. Refer to the Provisioning Users section of this guide. |

| Note | For multiple users, use an LDAP directory sync or Bulk Administration to assign global dial plan data for a large number of
                                                   users in a single operation. Refer to the Provisioning Users section of this guide. |
|---|---|

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

| Step 1 | In Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Click Find and select an existing SIP Profile. |
| Step 3 | From the Dial String Interpretation drop-down, configure the policy the system uses to determine whether to route calls as directory URIs or as directory numbers: Always treat all dial strings as URI addresses Phone number consists of characters 0–9, A–D, *, and + (others treated as URI addresses). Phone number consists of characters 0-9, *, and + (others treated as URI addresses)—This is the default option. |
| Step 4 | Check the Use Fully Qualified Domain Name in SIP Requests check box. |
| Step 5 | Optional. Under Trunk-Specific Configuration , check the Send ILS Learned Destination Route String check box if you want to be able to route intercluster calls across a Cisco Unified Border Element. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Click Find and select an existing SIP trunk. |
| Step 3 | In the Outbound Calls area, select one of the following from the Calling and Connected Party Info Format drop-down list: Deliver DN only in connected party —In outgoing SIP messages, Unified Communications Manager inserts the calling party’s directory number in the SIP contact
                                             header information. This is the default setting. Deliver URI only in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts the sending party’s directory URI in the SIP contact header.
                                             If a directory URI is not available, Unified Communications Manager inserts the directory number instead. Deliver URI and DN in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts a blended address that includes the calling party's directory
                                             URI and directory number in the SIP contact headers. If a directory URI is not available, Unified Communications Manager includes
                                             the directory number only. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > SIP Route Pattern . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Pattern Usage drop-down, select Domain Routing . |
| Step 4 | Depending on whether you are deploying IPv4 or IPv6, enter the route string in the IPv4 Address or IPv6 Address text box. |
| Step 5 | Under SIP Trunk/Route List , select a SIP trunk or route list that leads to the next- hop cluster for the route back to the route string's home cluster. |
| Step 6 | Complete the remaining fields in the SIP Route Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 7 | Click Save . |
| Step 8 | Create SIP route patterns for each learned route string. |
| Step 9 | Repeat these tasks for each cluster in the ILS network. |

| Note | If the SIP Route Pattern name contains dashes, you must ensure that there are no numerical digits between dashes. However,
                                             you can use a combination of letters and numbers or letters only, if there is more than one dash. Examples of right and wrong
                                             SIP Route Patterns are listed in the following: Correct Patterns: abc-1d-efg.xyz.com 123-abc-456.xyz.com Incorrect Patterns : abc-123-def.xyz.com 1bc-2-3ef.xyz.com |
|---|---|

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

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Global Dial Plan Replication > Block Learned Numbers and Patterns . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: Click Find and select an existing blocking rule to edit. Click Add New to create a new blocking rule. |
| Step 3 | In the Pattern field, enter the pattern or number that you want to block. For example, 206XXXXXXX can be used to block calls to 2065551212. |
| Step 4 | If you want to block calls based on the dial string prefix, enter the Prefix . |
| Step 5 | If you want to block calls from being sent to a specific cluster, enter the Cluster ID of the cluster. |
| Step 6 | From the Pattern Type drop-down list, select how you want to apply the blocking rule: Any —Choose this option if the blocking rule applies to both enterprise number patterns and +E.164 patterns. Enterprise Pattern —Choose this option if the blocking rule applies to enterprise number patterns only. +E.164 Pattern —Choose this option if the blocking rule applies to +E.164 number patterns only. |
| Step 7 | Click Save . |

| Note | If you have a large number of users, configure universal line templates and apply them with provisioning tools such as LDAP
                                          sync or Bulk Administration to provision global dial plan data for a large number of users in a single operation. See the
                                          Provisioning Users section of this book. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Directory Number . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing directory number for which you want to add global dial plan data. Click Add New to create a new directory number. |
| Step 3 | If you are creating a new number, enter the Directory Number and click Save . |
| Step 4 | To add an enterprise alternate number click the the Add an Enterprise Alternate Number button and do the following: Enter a Number Mask . For example, 5XXXX as an alternate number for 4001. The resulting enterprise alternate number (54001) displays in the Alternate Number field. Check the Add to Local Route Partition check box to add to a local route partition. From the Route Partition drop-down, select the partition. Check Advertise Globally via ILS if you want this alternate number to be advertised to the ILS network. Note If you configure an advertised pattern where the enterprise alternate number or +E.164 alternate number falls within the range
                                                            of the pattern, then you don't need to advertise the alternate numbers individually. | Note | If you configure an advertised pattern where the enterprise alternate number or +E.164 alternate number falls within the range
                                                            of the pattern, then you don't need to advertise the alternate numbers individually. |
| Note | If you configure an advertised pattern where the enterprise alternate number or +E.164 alternate number falls within the range
                                                            of the pattern, then you don't need to advertise the alternate numbers individually. |
| Step 5 | To add an +E.164 Alternate Number, click the Add an +E.164 Alternate Number and do the following: Enter a Number Mask . For example, 1972555XXXX as an alternate number for extension 4001. The resulting +E.164 alternate number (19725554001)
                                                displays in the Alternate Number field. Check the Add to Local Route Partition check box to add to a local route partition. From the Route Partition drop-down, select the partition. Check Advertise Globally via ILS if you want this alternate number to be advertised to the ILS network. |
| Step 6 | In the Directory URIs section, add directory URIs to this directory number: In the URI field, enter the directory URI. For example, alice@cisco.com. From the Partition drop-down, assign the directory URI to a local partition. Check the Advertise Globally via ILS check box to include this directory URI in advertised catalogs. Click Add Row to add additional directory URIs. You can add up to five directory URIs. |
| Step 7 | In the Advertised Failover Number field, select either the Enterprise Alternate Number or +E.164 Alternate Number as a PSTN failover. |
| Step 8 | Configure the remaining fields in the Directory Number Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 9 | Click Save . |

| Note | If you configure an advertised pattern where the enterprise alternate number or +E.164 alternate number falls within the range
                                                            of the pattern, then you don't need to advertise the alternate numbers individually. |
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

| Feature | Interactions and Restrictions |
|---|---|
| Export Directory URIs and +E.164 Patterns | You can also export all directory URIs and +E.164 number patterns that were configured in the local cluster, and export them
                                          to a csv file that you can import into another system. In Cisco Unified CM Administration, choose Bulk Adminstration > Directory URIs and Patterns > Export Local Directory URIs and Patterns . Click one of the following radio buttons to define the domain name that you want to attach to the export file: Organizational Top Level Domain —Click this radio button to use the value of the Organizational Top Level Domain enterprise parameter for the export file
                                                      domain name. Route String Domain —Click this radio button to use the value of the Route String field, as configured in ILS Configuration, for the export file
                                                      domain name. User Defined Domain —Click this radio button to create a customized domain name to attach to the export file. If you choose this option, enter
                                                      the domain name in the Domain Name text box. Click the Export Local Directory URIs and Patterns button. Save the CSV file to a local drive |
| Partitioning with URI Dialing | Partitioning with directory URIs depends on how you provision the directory URI. For user-based directory URIs that are assigned to an end user in End User Configuration , the local nondeletable Directory URI partition is assigned to the URI automatically. You cannot assign another partition,
                                                but you can use an administrator-managed partition as an alias for the local Directory URI partition by configuring the Directory URI Alias Partition enterprise parameter. For line-based directory URIs where the URI is assigned directly to a directory number in Directory Number Configuration , you can assign each URI to a local partition separately. If you are using tools like LDAP sync and Bulk Administration to provision directory URIs: Directory URIs that are provisioned via an LDAP sync are user-based and get assigned to the user in End User Configuration . These URIs are assigned to the local Directory URI partition. If the user has a primary extension, the URI also appears
                                                in Directory Number Configuration as the Primary URI. However, the assigned partition is the Directory URI partition. For directory URIs that are provisioned via Bulk Administration, it depends on how your updates are applied. For example,
                                                if you use the bat.xlt spreadsheet to create a csv import file, the user will be a user-based URI if you use the Users or Update Users tabs on the spreadsheet to add the directory URI. However, if you add the directory URI via the Line Fields options that appear when you click Create File Format , you can assign the URI to a directory number and assign a local partition to the URI directly. |
| Directory URI Case Sensitivity | By default, the user portion of a directory URI (the portion before the @) is case sensitive. You can make the user portion
                                          case insensitive by editing the URI Lookup Policy enterprise parameter. |
| Calling Search Space | To be dialable, directory URIs, enterprise alternate numbers, and +E.164 alternate numbers must be in a partition that is
                                          available in the calling party's calling search space. |
| Digit Transformations with URI dialing | If you use digit transformations, and you are deploying intercluster URI dialing, apply digit transformations against either
                                          the phone configuration or against the device pool that the phone uses. For individual phones, apply the transformation to the Calling Party Transformation CSS field in the Remote Number section. For device pools, you can apply the transformation against the Calling Party Transformation CSS field under Device Mobility Related Information . Note For roaming devices, the device pool setting overrides the phone configuration even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. | Note | For roaming devices, the device pool setting overrides the phone configuration even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. |
| Note | For roaming devices, the device pool setting overrides the phone configuration even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. |

| Note | For roaming devices, the device pool setting overrides the phone configuration even if the Use Device Pool Calling Party Transformation CSS check box is unchecked in the Phone Configuration window. |
|---|---|