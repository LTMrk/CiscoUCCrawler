---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-cucm-b-feature-configuration-guide-for-cisco1251su2-cuc-bacdbe7fc4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_010101.html
retrieved_at: 2026-08-16T17:10:59.935084+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Hotline

## Chapter: Hotline

# Hotline

## Hotline Overview

The Hotline feature extends the Private Line Automatic Ringdown (PLAR) feature, which allows you to configure a phone so that
                              when the user goes off hook (or the NewCall softkey or Line Key gets pressed), the phone immediately dials a preconfigured
                              number. The phone user cannot dial any other number from a phone that is configured for PLAR

Hotline adds the following additional restrictions and administrator controls for phones that use PLAR:

Hotline devices (devices configured to use hotline) that receive calls will receive calls only from other hotline devices,
                                    and will reject non-hotline callers.

You can configure a Hotline phone to call only, receive only, or both call and receive.

You can restrict the features available on a Hotline phone by applying a softkey template to the phone.

Analog hotline
                                    				phones ignore inbound hookflash signals.

### Route Class
                              		  Signaling

Hotline uses route
                              		  class signaling to allow Hotline phones to receive calls only from other
                              		  Hotline phones. A route class is a DSN code that identifies the class of
                              		  traffic for a call. The route class informs downstream devices about special
                              		  routing or termination requirements. A Hotline phone can only accept calls from a Hotline phone with
                              		  the same route class.

### Call
                              		  Screening

Hotline also
                              		  provides Configurable Call Screening based on caller ID. Configurable Call
                              		  Screening allows a receiving Hotline phone to screen calls based on caller ID
                              		  information and allow only callers in a screening list to connect.

## System Requirements for Hotline

The following hotline system requirements exist for Unified Communications Manager :

Unified Communications Manager 8.0(1) or higher on each server in the cluster

MGCP gateway POTS phones (FXS).

SCCP gateway POTS phones (FXS).

Tip

Cisco Feature Navigator allows you to determine which Cisco IOS and Catalyst OS software images support a specific software
                                          release, feature set, or platform. To access Cisco Feature Navigator, go to http://cfn.cloudapps.cisco.com/ITDIT/CFN/ .

You do not need a Cisco.com account to access Cisco Feature
                                          			 Navigator.

## Hotline
                        	 Configuration Task Flow

Step 1

Generate a Phone Feature List

Step 2

Create Custom Softkey Template

Step 3

Configure Hotline on Phones

Step 4

Configure Route Class Signaling Task Flow

Configure
                                          				route class signaling to support the Hotline feature.

Step 5

Configure Hotline to Call Only or Receive Only Task Flow

Step 6

Configure Call Screening with a Calling Search Space

### Create Custom
                           	 Softkey Template

When
                                 		  configuring Hotline, you can customize a softkey template to display only those
                                 		  features that you want to make available to a Hotline phone.

Unified Communications Manager includes standard softkey templates for call processing and applications. When creating custom softkey templates, copy the
                                 standard templates and make modifications as required.

#### Before you begin

Generate a Phone Feature List

Step 1

Choose Device > Device
                                                				  Settings > Softkey Template .

Step 2

Click Add
                                             				New .

Step 3

From the
                                          			 drop-down list, select a softkey template and click Copy to create a new template.

Step 4

In the Softkey Template Name field, enter a unique name to
                                          			 identify the softkey template.

Step 5

Enter a
                                          			 description that describes the use of the template. The description can include
                                          			 up to 50 characters in any language, but it cannot include double-quotes ("),
                                          			 percentage sign (%), ampersand (&), backslash (\), or angle brackets
                                          			 (<>).

Step 6

To designate
                                          			 this softkey template as the standard softkey template, check the Default Softkey Template check box.

If you
                                                         				  designate a softkey template as the default softkey template, you will not be
                                                         				  able to delete this softkey template unless you first remove the default
                                                         				  designation.

Step 7

Click Save .

The softkey
                                             				template gets copied, and the Softkey Template Configuration window redisplays.

Step 8

(Optional) Click the Add
                                             				Application button.

Step 9

Configure the positions of the softkeys on the Cisco Unified IP Phone LCD screen.

Step 10

To save your
                                          			 configuration, click Save .

### Configure Hotline
                           	 on Phones

Use this procedure to enable the phone as a Hotline device.

#### Before you begin

Optional. If you want to create a custom softkey template to display only those features that you want to make available to
                                 a Hotline phone, see Create Custom Softkey Template .

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the
                                          			 phone that you want to enable as a Hotline device.

Step 3

Check the Hotline Device check box.

Step 4

If you have
                                          			 created a custom softkey template specifically for the Hotline phone, from the Softkey Template drop-down list, choose the softkey template.

Step 5

Click Save .

### Configure Route Class Signaling Task Flow

Perform this task flow to configure route class signaling  for Hotline calls.

Step 1

Enable Route Class Signaling in the Cluster

Set the route class signaling clusterwide defaults for trunks and gateways to enabled.

The settings for individual trunks and gateways override the clusterwide defaults. If you use this service parameter to enable
                                                         route class signaling across the cluster, route class signaling can still be disabled on an individual trunk or gateway.

Step 2

Enable Route Class Signaling on Trunks

Enable route class signaling on an individual trunk.

Step 3

Enable Route Class Signaling on Gateways

Enable route class signaling on an MGCP T1/CAS or MGCP PRI gateway.

Step 4

Configure Signaling Labels for the Hotline Route Class

Configure SIP signaling labels for Hotline route classes.

Step 5

Configure the Route Class on Hotline Route Patterns

Configure the route class on the route patterns that are routing your Hotline calls.

Step 6

Configure the Route Class on Hotline Translation Patterns

Optional . If you use translation patterns on your Hotline calls, configure the route class on your translation patterns.

#### Enable Route Class
                              	 Signaling in the Cluster

When you set the Route Class Trunk Signaling Enabled service parameter to True , the default route class signaling setting for all trunks or gateways  in the cluster that support route class signaling
                                    is set to enabled.

The settings for individual trunks and gateways override the clusterwide defaults. If you use this service parameter to enable
                                                route class signaling across the cluster, route class signaling can still be disabled on an individual trunk or gateway.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

Set the Route Class Trunk Signaling Enabled service parameter to True .

Step 3

Click Save .

##### What to do next

Use the following procedures to configure route class signaling on individual trunks or gateways.

Enable Route Class Signaling on Trunks

Enable Route Class Signaling on Gateways

#### Enable Route Class Signaling on Trunks

Use this  procedure to enable  route class signaling on an individual trunk. The configuration for individual trunks overrides
                                    the clusterwide service parameter setting.

##### Before you begin

Follow the Enable Route Class Signaling in the Cluster procedure to use a clusterwide service parameter to configure the default route class signaling settings for all trunks in
                                    the cluster.

Step 1

From Cisco Unified CM Administration, choose Device > Trunks .

Step 2

Click Find and select the SIP trunk on which you want to enable route class signaling.

Step 3

From the Route Class Signaling Enabled drop-down list box, choose one of the following options:

- Default —This trunk uses the setting from the Route Class Signaling Enabled service parameter.

- Off —Route class signaling is disabled for this trunk.

- On —Route class signaling is enabled for this trunk.

Step 4

Click Save .

#### Enable Route Class Signaling on Gateways

Use  this procedure to enable route class signaling on an individual MGCP PRI or MGCP T1/CAS gateway. The configuration for
                                    individual gateways overrides the clusterwide service parameter setting.

##### Before you begin

Follow the Enable Route Class Signaling in the Cluster procedure to use a clusterwide service parameter to set the default route class signaling setting for gateways in the cluster.

Perform the Enable Route Class Signaling on Trunks procedure to configure route class signaling for individual trunks.

Step 1

From Cisco Unified CM Administration, choose Device > Gateways .

Step 2

Click Find and select the gateway on which you want to configure route class signaling.

Step 3

From the Route Class Signaling Enabled drop-down list box, choose one of the following options:

- Default —This gateway uses the setting from the clusterwide Route Class Signaling Enabled service parameter.

- Off —Route class signaling is disabled on this gateway.

- On —Route class signaling is enabled on this gateway.

Step 4

If you want to encode voice route class for voice  calls, check the Encode Voice Route Class check box.

Step 5

Click Save .

#### Configure Signaling Labels for the Hotline Route Class

You must configure a SIP signaling label value for the Hotline route class that you want to use.

##### Before you begin

Enable route class signaling on your trunks and gateways. For details, see Enable Route Class Signaling in the Cluster .

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server on which
                                             			 the CallManager service is running.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Click Advanced .

Step 5

In the SIP Route Class Naming Authority service parameter field, enter a value to represent the naming authority and context for the labels used in SIP signaling
                                             to represent route class. The default value is cisco.com .

Step 6

In the SIP Hotline Voice Route Class Label service parameter field, enter a label to represent the Hotline Voice route class. The default value is hotline .

Step 7

In the SIP Hotline Data Route Class Label service parameter field, enter a lable to represent the Hotline Data route class. The default value is ccdata .

Step 8

Click Save .

#### Configure the Route Class on Hotline Route
                              	 Patterns

This procedure describes call routing instructions that are specific to Hotline devices. For more information on how to
                                    configure route patterns and translation patterns in your network, see the System Configuration Guide for Cisco Unified Communications Manager .

For each route pattern that you expect to route a Hotline call, you must set the route class for that route pattern to Hotline Voice or Hotline Data .

##### Before you begin

Configure Signaling Labels for the Hotline Route Class

Before you perform this procedure, it is expected that your network call routing is set up with route patterns.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Patterns .

Step 2

Click Find to display a list of route patterns in your network.

Step 3

For each T1/CAS  route pattern that is used to route a Hotline call:

From the Find and List Route Patterns window, select the
                                                   			 route pattern.

From the Route Class drop-down list box, choose either Hotline Voice or Hotline Data as the route class for this route
                                                   			 pattern.

Click Save .

#### Configure the
                              	 Route Class on Hotline Translation Patterns

##### Before you begin

Before you perform
                                    		  this procedure, it is expected that you have set up network call routing with
                                    		  route patterns and translation patterns.

Perform the Configure the Route Class on Hotline Route Patterns procedure.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Translation Pattern .

Step 2

Click Find to display the translation patterns in your
                                             			 cluster.

Step 3

For each
                                             			 translation pattern that you want to use on a Hotline number, perform the
                                             			 following steps:

From the Route Class drop-down list box, select either Hotline Voice or Hotline Data .

Click Save .

### Configure Hotline to Call Only or Receive Only Task Flow

The configuration example in this task flow describes how to set up a Hotline phone to either place calls only or receive
                                 calls only.

Step 1

Configure Partitions for Hotline Call Only Receive Only

Create two partitions: one should be empty and the other will be assigned to a new CSS.

Step 2

Configure Calling Search Space for Hotline Call Only Receive Only

Create a new calling search space and assign one of the new partitions to this CSS. This CSS will contain no other partition.

Step 3

Perform one of the following procedures:

- Configure Call Only on Hotline Phone

- Configure Receive Only on Hotline Phone

If you want to configure call only, assign the empty partition to the phone line. If you want to configure receive only, assign
                                             the new CSS to the phone.

#### Configure Partitions for Hotline Call Only Receive Only

If you want to configure a Hotline phone to either place calls only, or to receive calls only you must create two partitions.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partitions .

Step 2

Click Add New .

Step 3

Create a new partition.

Step 4

Enter a unique name and description for the partition. For example, IsolatedPartition .

This partition will not be assigned to any CSS.

Step 5

Click Save

Step 6

Repeat steps 2-5 and create a second partition. For example, EmptyPartition .

This partition will not be assigned to any phone line, but it will be assigned to the NoRouteCSS.

#### Configure Calling Search Space for Hotline Call Only Receive Only

You must create a calling search and assign one of the two partitions that you've created to the calling search space.

##### Before you begin

Configure Partitions for Hotline Call Only Receive Only

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

Click Add New .

Step 3

Enter a Name and Description for the calling search space.

Step 4

From the Available Partitions list box, use the arrows to select  the EmptyPartition partition.

Make sure that the partition is assigned to only this calling search space and to no phone lines.

Step 5

Click Save

##### What to do next

Perform one of the following procedures:

Configure Call Only on Hotline Phone

Configure Receive Only on Hotline Phone

#### Configure Call Only on Hotline Phone

If you have set up your partitions and calling search spaces, perform these steps to configure the Hotline phone to place
                                    calls only.

##### Before you begin

Configure Calling Search Space for Hotline Call Only Receive Only

Step 1

From Cisco Unified CM Administration, choose Call Routing > Phone .

Step 2

Click Find and select the Hotline phone.

Step 3

From the left navigation pane, click the phone line.

Step 4

From the Route Partition drop-down list, select the empty partition that you created.

Step 5

Click Save .

#### Configure Receive Only on Hotline Phone

If you have created your calling search space and partitions already, perform these steps to configure the Hotline phone to
                                    receive calls only.

##### Before you begin

Configure Calling Search Space for Hotline Call Only Receive Only

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the Hotline phone.

Step 3

From the Calling Search Space drop-down list, select the new CSS that you created in the previous procedure.

Step 4

Click Save .

### Configure Call
                           	 Screening with a Calling Search Space

Configure call
                                 		  screening for any intraswitched (line to line) Hotline calls by assigning a unique CSS where the Hotline phones that are
                                 in the partitions are only those Hotline phones that you want to be able to call each other.

Step 1

Configure Partitions for Hotline Call Screening

Create any new partitions for your Hotline phone lines.

Step 2

Create Calling Search Space for Hotline Call Screening

Create a new CSS for the screening list. The CSS must include partitions with only those Hotline numbers that you want to
                                             allow.

Step 3

Configure Hotline Phones for Call Screening

Assign the new CSS and partition to the Hotline phone.

#### Configure Partitions for Hotline Call Screening

To configure call screening in Hotline phones using a calling search space, you must set up partitions where the only Hotline
                                    numbers are those that you want to allow.

Perform the following procedure if you need to create a new partition for your Hotline call screening list.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

Click Add
                                                				New to create a new partition.

Step 3

In
                                             			 the Partition
                                                				Name, Description field, enter a name for the partition that is
                                             			 unique to the route plan.

Step 4

Enter a
                                             			 comma (,) after the partition name and enter a description of the partition on
                                             			 the same line.

Step 5

To create
                                             			 multiple partitions, use one line for each partition entry.

Step 6

From the Time
                                                				Schedule drop-down list, choose a time schedule to associate with
                                             			 this partition.

Step 7

Select one
                                             			 of the following radio buttons to configure the Time
                                                				Zone :

- Originating
                                                   				  Device —When you select this radio button, the system compares the
                                                				time zone of the calling device to the Time Schedule to determine whether the partition is
                                                				available is available to receive an incoming call.

- Specific Time
                                                   				  Zone —After you select this radio button, choose a time zone from
                                                				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                                				available is available to receive an incoming call.

Step 8

Click Save .

#### Create Calling Search Space for Hotline Call Screening

Perform the following procedure to create a new calling search space for the Hotline phones in the  call screening list. Make
                                    sure that the only Hotline numbers in the partitions that you select for this CSS are those Hotline numbers that you want
                                    to allow in the call screening list. No Hotline numbers that you want to screen out should be included in the partitions for
                                    this CSS.

##### Before you begin

Configure Partitions for Hotline Call Screening

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

Click Add New .

Step 3

In the Name field, enter a name.

Ensure that
                                                				each calling search space name is unique to the system. The name can include up
                                                				to 50 alphanumeric characters and can contain any combination of spaces,
                                                				periods (.), hyphens (-), and underscore characters (_).

Step 4

In the Description field, enter a description.

The
                                                				description can include up to 50 characters in any language, but it cannot
                                                				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                                				(\), or angle brackets (<>).

Step 5

From the Available Partitions drop-down list, perform one of
                                             			 the following steps:

- For a single partition,
                                                				select that partition.

- For multiple partitions,
                                                				hold down the Control (CTRL) key, then select the appropriate
                                                				partitions.

Step 6

Select the
                                             			 down arrow between the boxes to move the partitions to the Selected Partitions field.

Step 7

(Optional) Change the priority of selected partitions by using the arrow keys to the right
                                             			 of the Selected Partitions box.

Step 8

Click Save .

#### Configure Hotline Phones for Call Screening

If you have already configured calling search spaces and partitions for Hotline call screening, perform this procedure to
                                    assign the calling search spaces and partitions to your Hotline phones.

##### Before you begin

Create Calling Search Space for Hotline Call Screening

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the Hotline phone.

Step 3

From the Calling Search Space drop-down list, select the new calling search space that you created for the Hotline call screening list.

Step 4

Click Save .

Step 5

From the left navigation pane, click the phone line that you want to use for Hotline calls.

Step 6

From the Route Partition drop-down list, select a partition that is included in the calling search space that you set up.

Step 7

Click Save .

## Hotline Troubleshooting

The following table  provides troubleshooting information for cases where hotline calls do not dial correctly.

Problem

Solution

Dial tone

Check PLAR configuration.

Reorder tone or VCA (intracluster call)

Check PLAR configuration.

Verify that the phones on both ends are configured as hotline phones.

Reorder tone or VCA (intercluster or TDM call)

Check PLAR configuration.

Verify that the phones on both ends are configured as hotline phones.

Verify that route class signalling is enabled on trunks.

Check the configuration of route class translations on CAS gateways.

The following table provides troubleshooting information for cases where call screening based on caller ID does not work.

Problem

Solution

Call not allowed

Check Caller ID.

Add pattern to screen CSS.

Call allowed

Remove pattern from screen CSS.

| Tip | Cisco Feature Navigator allows you to determine which Cisco IOS and Catalyst OS software images support a specific software
                                          release, feature set, or platform. To access Cisco Feature Navigator, go to http://cfn.cloudapps.cisco.com/ITDIT/CFN/ . You do not need a Cisco.com account to access Cisco Feature
                                          			 Navigator. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Log in to
                                       			 Cisco Unified Reporting and run a phone feature list report to determine which
                                       			 phones support Hotline. |
| Step 2 | Create Custom Softkey Template | Optional. If
                                       			 you want to restrict features on a Hotline phone, create a softkey template
                                       			 that allows only the features that you want. |
| Step 3 | Configure Hotline on Phones | Enable the
                                       			 phone as a Hotline device. |
| Step 4 | Configure Route Class Signaling Task Flow | Configure
                                          				route class signaling to support the Hotline feature. |
| Step 5 | Configure Hotline to Call Only or Receive Only Task Flow | Optional . If you want to restrict a Hotline phone to either originating calls only or terminating calls only, configure call and receive
                                       settings. |
| Step 6 | Configure Call Screening with a Calling Search Space | Optional . Use calling search spaces and partitions to configure a call screening list for your Hotline phones. |

| Step 1 | Choose Device > Device
                                                				  Settings > Softkey Template . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | From the
                                          			 drop-down list, select a softkey template and click Copy to create a new template. |
| Step 4 | In the Softkey Template Name field, enter a unique name to
                                          			 identify the softkey template. |
| Step 5 | Enter a
                                          			 description that describes the use of the template. The description can include
                                          			 up to 50 characters in any language, but it cannot include double-quotes ("),
                                          			 percentage sign (%), ampersand (&), backslash (\), or angle brackets
                                          			 (<>). |
| Step 6 | To designate
                                          			 this softkey template as the standard softkey template, check the Default Softkey Template check box. Note If you
                                                         				  designate a softkey template as the default softkey template, you will not be
                                                         				  able to delete this softkey template unless you first remove the default
                                                         				  designation. | Note | If you
                                                         				  designate a softkey template as the default softkey template, you will not be
                                                         				  able to delete this softkey template unless you first remove the default
                                                         				  designation. |
| Note | If you
                                                         				  designate a softkey template as the default softkey template, you will not be
                                                         				  able to delete this softkey template unless you first remove the default
                                                         				  designation. |
| Step 7 | Click Save . The softkey
                                             				template gets copied, and the Softkey Template Configuration window redisplays. |
| Step 8 | (Optional) Click the Add
                                             				Application button. |
| Step 9 | Configure the positions of the softkeys on the Cisco Unified IP Phone LCD screen. |
| Step 10 | To save your
                                          			 configuration, click Save . |

| Note | If you
                                                         				  designate a softkey template as the default softkey template, you will not be
                                                         				  able to delete this softkey template unless you first remove the default
                                                         				  designation. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the
                                          			 phone that you want to enable as a Hotline device. |
| Step 3 | Check the Hotline Device check box. |
| Step 4 | If you have
                                          			 created a custom softkey template specifically for the Hotline phone, from the Softkey Template drop-down list, choose the softkey template. |
| Step 5 | Click Save . Note You can also assign a softkey template to a Device Pool and
                                                      				then assign that Device Pool to the phone. | Note | You can also assign a softkey template to a Device Pool and
                                                      				then assign that Device Pool to the phone. |
| Note | You can also assign a softkey template to a Device Pool and
                                                      				then assign that Device Pool to the phone. |

| Note | You can also assign a softkey template to a Device Pool and
                                                      				then assign that Device Pool to the phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Route Class Signaling in the Cluster | Set the route class signaling clusterwide defaults for trunks and gateways to enabled. Note The settings for individual trunks and gateways override the clusterwide defaults. If you use this service parameter to enable
                                                         route class signaling across the cluster, route class signaling can still be disabled on an individual trunk or gateway. | Note | The settings for individual trunks and gateways override the clusterwide defaults. If you use this service parameter to enable
                                                         route class signaling across the cluster, route class signaling can still be disabled on an individual trunk or gateway. |
| Note | The settings for individual trunks and gateways override the clusterwide defaults. If you use this service parameter to enable
                                                         route class signaling across the cluster, route class signaling can still be disabled on an individual trunk or gateway. |
| Step 2 | Enable Route Class Signaling on Trunks | Enable route class signaling on an individual trunk. |
| Step 3 | Enable Route Class Signaling on Gateways | Enable route class signaling on an MGCP T1/CAS or MGCP PRI gateway. |
| Step 4 | Configure Signaling Labels for the Hotline Route Class | Configure SIP signaling labels for Hotline route classes. |
| Step 5 | Configure the Route Class on Hotline Route Patterns | Configure the route class on the route patterns that are routing your Hotline calls. |
| Step 6 | Configure the Route Class on Hotline Translation Patterns | Optional . If you use translation patterns on your Hotline calls, configure the route class on your translation patterns. |

| Note | The settings for individual trunks and gateways override the clusterwide defaults. If you use this service parameter to enable
                                                         route class signaling across the cluster, route class signaling can still be disabled on an individual trunk or gateway. |
|---|---|

| Note | The settings for individual trunks and gateways override the clusterwide defaults. If you use this service parameter to enable
                                                route class signaling across the cluster, route class signaling can still be disabled on an individual trunk or gateway. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | Set the Route Class Trunk Signaling Enabled service parameter to True . |
| Step 3 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunks . |
|---|---|
| Step 2 | Click Find and select the SIP trunk on which you want to enable route class signaling. |
| Step 3 | From the Route Class Signaling Enabled drop-down list box, choose one of the following options: Default —This trunk uses the setting from the Route Class Signaling Enabled service parameter. Off —Route class signaling is disabled for this trunk. On —Route class signaling is enabled for this trunk. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Gateways . |
|---|---|
| Step 2 | Click Find and select the gateway on which you want to configure route class signaling. |
| Step 3 | From the Route Class Signaling Enabled drop-down list box, choose one of the following options: Default —This gateway uses the setting from the clusterwide Route Class Signaling Enabled service parameter. Off —Route class signaling is disabled on this gateway. On —Route class signaling is enabled on this gateway. |
| Step 4 | If you want to encode voice route class for voice  calls, check the Encode Voice Route Class check box. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which
                                             			 the CallManager service is running. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Click Advanced . |
| Step 5 | In the SIP Route Class Naming Authority service parameter field, enter a value to represent the naming authority and context for the labels used in SIP signaling
                                             to represent route class. The default value is cisco.com . |
| Step 6 | In the SIP Hotline Voice Route Class Label service parameter field, enter a label to represent the Hotline Voice route class. The default value is hotline . |
| Step 7 | In the SIP Hotline Data Route Class Label service parameter field, enter a lable to represent the Hotline Data route class. The default value is ccdata . |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Patterns . |
|---|---|
| Step 2 | Click Find to display a list of route patterns in your network. |
| Step 3 | For each T1/CAS  route pattern that is used to route a Hotline call: From the Find and List Route Patterns window, select the
                                                   			 route pattern. From the Route Class drop-down list box, choose either Hotline Voice or Hotline Data as the route class for this route
                                                   			 pattern. Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Translation Pattern . |
|---|---|
| Step 2 | Click Find to display the translation patterns in your
                                             			 cluster. |
| Step 3 | For each
                                             			 translation pattern that you want to use on a Hotline number, perform the
                                             			 following steps: From the Route Class drop-down list box, select either Hotline Voice or Hotline Data . Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Partitions for Hotline Call Only Receive Only | Create two partitions: one should be empty and the other will be assigned to a new CSS. |
| Step 2 | Configure Calling Search Space for Hotline Call Only Receive Only | Create a new calling search space and assign one of the new partitions to this CSS. This CSS will contain no other partition. |
| Step 3 | Perform one of the following procedures: Configure Call Only on Hotline Phone Configure Receive Only on Hotline Phone | If you want to configure call only, assign the empty partition to the phone line. If you want to configure receive only, assign
                                             the new CSS to the phone. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partitions . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Create a new partition. |
| Step 4 | Enter a unique name and description for the partition. For example, IsolatedPartition . Note This partition will not be assigned to any CSS. | Note | This partition will not be assigned to any CSS. |
| Note | This partition will not be assigned to any CSS. |
| Step 5 | Click Save |
| Step 6 | Repeat steps 2-5 and create a second partition. For example, EmptyPartition . Note This partition will not be assigned to any phone line, but it will be assigned to the NoRouteCSS. | Note | This partition will not be assigned to any phone line, but it will be assigned to the NoRouteCSS. |
| Note | This partition will not be assigned to any phone line, but it will be assigned to the NoRouteCSS. |

| Note | This partition will not be assigned to any CSS. |
|---|---|

| Note | This partition will not be assigned to any phone line, but it will be assigned to the NoRouteCSS. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name and Description for the calling search space. |
| Step 4 | From the Available Partitions list box, use the arrows to select  the EmptyPartition partition. Note Make sure that the partition is assigned to only this calling search space and to no phone lines. | Note | Make sure that the partition is assigned to only this calling search space and to no phone lines. |
| Note | Make sure that the partition is assigned to only this calling search space and to no phone lines. |
| Step 5 | Click Save |

| Note | Make sure that the partition is assigned to only this calling search space and to no phone lines. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Phone . |
|---|---|
| Step 2 | Click Find and select the Hotline phone. |
| Step 3 | From the left navigation pane, click the phone line. The Directory Number Configuration window displays. |
| Step 4 | From the Route Partition drop-down list, select the empty partition that you created. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the Hotline phone. |
| Step 3 | From the Calling Search Space drop-down list, select the new CSS that you created in the previous procedure. |
| Step 4 | Click Save . |

| Note | You can
                                          				also configure call screening by creating translation patterns where each
                                          				pattern matches each number pattern that you want to either allow or screen. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Partitions for Hotline Call Screening | Create any new partitions for your Hotline phone lines. |
| Step 2 | Create Calling Search Space for Hotline Call Screening | Create a new CSS for the screening list. The CSS must include partitions with only those Hotline numbers that you want to
                                             allow. |
| Step 3 | Configure Hotline Phones for Call Screening | Assign the new CSS and partition to the Hotline phone. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | Click Add
                                                				New to create a new partition. |
| Step 3 | In
                                             			 the Partition
                                                				Name, Description field, enter a name for the partition that is
                                             			 unique to the route plan. Partition
                                             			 names can contain alphanumeric characters, as well as spaces, hyphens (-), and
                                             			 underscore characters (_). See the online help for guidelines about partition
                                             			 names. |
| Step 4 | Enter a
                                             			 comma (,) after the partition name and enter a description of the partition on
                                             			 the same line. The
                                             			 description can contain up to 50 characters in any language, but it cannot
                                             			 include double quotes ("), percentage sign (%), ampersand (&), backslash
                                             			 (\), angle brackets (<>), or square brackets ([ ]). If you do
                                             			 not enter a description, Cisco Unified Communications Manager automatically
                                             			 enters the partition name in this field. |
| Step 5 | To create
                                             			 multiple partitions, use one line for each partition entry. |
| Step 6 | From the Time
                                                				Schedule drop-down list, choose a time schedule to associate with
                                             			 this partition. The time
                                             			 schedule specifies when the partition is available to receive incoming calls.
                                             			 If you choose None , the partition remains active at all times. |
| Step 7 | Select one
                                             			 of the following radio buttons to configure the Time
                                                				Zone : Originating
                                                   				  Device —When you select this radio button, the system compares the
                                                				time zone of the calling device to the Time Schedule to determine whether the partition is
                                                				available is available to receive an incoming call. Specific Time
                                                   				  Zone —After you select this radio button, choose a time zone from
                                                				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                                				available is available to receive an incoming call. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter a name. Ensure that
                                                				each calling search space name is unique to the system. The name can include up
                                                				to 50 alphanumeric characters and can contain any combination of spaces,
                                                				periods (.), hyphens (-), and underscore characters (_). |
| Step 4 | In the Description field, enter a description. The
                                                				description can include up to 50 characters in any language, but it cannot
                                                				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                                				(\), or angle brackets (<>). |
| Step 5 | From the Available Partitions drop-down list, perform one of
                                             			 the following steps: For a single partition,
                                                				select that partition. For multiple partitions,
                                                				hold down the Control (CTRL) key, then select the appropriate
                                                				partitions. |
| Step 6 | Select the
                                             			 down arrow between the boxes to move the partitions to the Selected Partitions field. |
| Step 7 | (Optional) Change the priority of selected partitions by using the arrow keys to the right
                                             			 of the Selected Partitions box. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the Hotline phone. |
| Step 3 | From the Calling Search Space drop-down list, select the new calling search space that you created for the Hotline call screening list. |
| Step 4 | Click Save . |
| Step 5 | From the left navigation pane, click the phone line that you want to use for Hotline calls. The Directory Number Configuration window displays. |
| Step 6 | From the Route Partition drop-down list, select a partition that is included in the calling search space that you set up. |
| Step 7 | Click Save . |

| Problem | Solution |
|---|---|
| Dial tone | Check PLAR configuration. |
| Reorder tone or VCA (intracluster call) | Check PLAR configuration. Verify that the phones on both ends are configured as hotline phones. |
| Reorder tone or VCA (intercluster or TDM call) | Check PLAR configuration. Verify that the phones on both ends are configured as hotline phones. Verify that route class signalling is enabled on trunks. Check the configuration of route class translations on CAS gateways. |

| Problem | Solution |
|---|---|
| Call not allowed | Check Caller ID. Add pattern to screen CSS. |
| Call allowed | Remove pattern from screen CSS. |