---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--38b3197e10
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0100001.html
retrieved_at: 2026-08-16T16:37:24.552789+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Hold Reversion

## Chapter: Hold Reversion

# Hold Reversion

## Hold Reversion
                        	 Overview

When you place a
                              		  call on hold, the Hold Reversion feature alerts you when the held call exceeds
                              		  a configured time limit. When the configured time limit expires, an alert is
                              		  generated on your phone to remind you to handle the call.

The following
                              		  alerts are available:

- The Phone rings or beeps
                                 			 once

- The status line displays "Hold
                                    				Reversion"

- The LED next to the line
                                 			 button flashes continuously

- A vibrating handset icon
                                 			 displays

The type of
                                          			 alert that you receive depends on the capabilities of your phone.

To retrieve a
                              		  reverted call, you can:

- Pick up the handset

- Press the speaker button on
                                 			 the phone

- Press the headset button

- Select the line that is
                                 			 associated with the reverted call

- Press the Resume softkey

For details, see
                              		  the user guide for your particular phone model.

## Hold Reversion
                        	 Prerequisites

- Cisco CallManager service
                                 			 must be running on at least one node in the cluster

- Cisco CTIManager service
                                 			 must be running on at least one node in the cluster

- Cisco Database Layer
                                 			 Monitor service must be running on the same node as the Cisco CallManager
                                 			 service

- Cisco RIS Data Collector
                                 			 service must be running on the same node as the Cisco CallManager service

- Cisco Tftp service must be
                                 			 running on at least one node in the cluster

- Cisco Unified
                                 			 Communications Manager Locale Installer must be installed, if you want to use
                                 			 non-English phone locales or country-specific tones

## Hold Reversion
                        	 Configuration Task Flow

Perform the
                              		  following steps to configure Hold Reversion for your phones. This procedure
                              		  assumes that you have configured directory numbers for phones, or that you are
                              		  using auto-registration.

### Before you begin

If phone users
                                    				want the hold reversion messages to display in a language other than English,
                                    				or if you want the user to receive country-specific tones for calls, verify
                                    				that you have installed the locale installer.

Review Hold Reversion Prerequisites

Step 1

Generate a Phone Feature List

Run a phone
                                          				feature list report to determine which phones support the Hold Reversion
                                          				feature.

Step 2

Configure Call Focus Priority for Hold Reversion

Step 3

Perform one of
                                       			 the following procedures:

- Configure Hold Reversion Timer Defaults for Cluster

- Configure Hold Reversion Timer Settings for Phone

Configure the
                                          				Hold Reversion timer settings. You can configure the timer using a clusterwide
                                          				service parameter, or configure the settings on an individual phone line.

The settings
                                                      				  on an individual phone line override the clusterwide service parameter
                                                      				  settings.

### Configure Call
                           	 Focus Priority for Hold Reversion

As an
                                 		  administrator, you can prioritize incoming calls and reverted calls. By
                                 		  default, all incoming calls are handled before reverted calls, however you can
                                 		  change the call focus priority so that reverted calls take precedence.

#### Before you begin

Generate a Phone Feature List

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Device
                                                				  Pool and open the device pool that applies to your
                                          			 phones.

Step 2

In the Reverted Call Focus Priority field, choose one of
                                          			 the following options and click Save :

- Default —Incoming calls have priority over reverted
                                             				calls.

- Highest —Reverted calls have priority over incoming
                                             				calls.

Step 3

Click Save .

Step 4

Reset any
                                          			 devices in the Device Pool by performing the following steps:

Click Reset . The Device Reset window displays.

In the Device Reset window, click Reset .

#### What to do next

Perform one of the
                                 		  following procedures to configure Hold Reversion Timer Settings:

Configure Hold Reversion Timer Defaults for Cluster

Configure Hold Reversion Timer Settings for Phone

### Configure Hold Reversion Timer Defaults for Cluster

Perform this procedure to configure clusterwide service parameters that apply hold reversion timer default settings for all
                                 phones in  the cluster.

#### Before you begin

Configure Call Focus Priority for Hold Reversion

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server that is running the CallManager service.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Configure values for the following clusterwide service parameters:

- Hold Reversion
                                                				Duration —Enter a number from 0 to 1200 (inclusive) to specify the wait time in
                                             				seconds before Cisco Unified Communications Manager issues a reverted call
                                             				alert to the holding party phone. If you enter 0, Cisco Unified Communications
                                             				Manager does not issue reverted call alerts, unless it is configured on a phone
                                             				line.

- Hold Reversion Interval
                                                				Notification —Enter a number from 0 to 1200 (inclusive) to specify the wait time
                                             				in seconds before Cisco Unified Communications Manager sends periodic reminder
                                             				alerts to the holding party phone. If you enter 0, Cisco Unified Communications
                                             				Manager does not send periodic reminder alerts unless the timer is configured
                                             				on a phone line.

Step 5

Click Save .

### Configure Hold
                           	 Reversion Timer Settings for Phone

Perform this procedure to configure Hold Reversion timer settings for  a phone and phone line.

You can also configure
                                             		  Hold Reversion timer settings using a clusterwide service parameter. However, the settings on an individual phone line
                                             override the clusterwide service parameter setting.

#### Before you begin

Perform Configure Hold Reversion Timer Defaults for Cluster to configure Hold Reversion  clusterwide defaults.

Step 1

In Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone on which you want to configure Hold Reversion.

Step 3

In the Association pane on the left, click the phone line on which you want to configure Hold Reversion.

Step 4

Configure values for the following fields:

- Hold Reversion Ring
                                                				Duration —Enter a number from 0 to 1200 (inclusive) to specify the wait time in
                                             				seconds before Cisco Unified Communications Manager issues a reverted call
                                             				alert. If you enter 0, Cisco Unified Communications Manager does not issue
                                             				reverted call alerts to this DN. If you leave the field empty (the default
                                             				setting), Cisco Unified Communications Manager applies the setting from the Hold
                                             				Reversion Duration service parameter.

- Hold Reversion Ring
                                                				Interval Notification —Enter a number from 0 to 1200 (inclusive) to specify the
                                             				wait time in seconds before Cisco Unified Communications Manager sends periodic
                                             				reminder alerts. If you enter 0, Cisco Unified Communications Manager does not
                                             				send periodic reminder alerts to this DN. If you leave the field empty (the
                                             				default setting), Cisco Unified Communications Manager applies the setting from
                                             				the Hold Reversion Interval Notification service parameter.

Step 5

Click Save .

Step 6

Reset the phone by performing the following steps:

Click Reset . The Reset Device window displays.

Click Reset .

## Hold Reversion
                        	 Interactions

Feature

Interactions

Music on
                                          					 Hold

MOH is supported on a reverted call if MOH is
                                          					 configured for a normal held call.

Call Park

If hold
                                          					 reversion is invoked and the held party presses the Park softkey, the holding party still receives hold
                                          					 reversion alerts and can retrieve the call. When the holding party retrieves
                                          					 the call, the holding party receives MOH, if configured.

If the
                                          					 held party parks before the hold duration exceeds the configured time limit,
                                          					 the system suppresses all hold reversion alerts until the call is picked up or
                                          					 redirected.

MLPP

When a
                                          					 multilevel precedence and preemption (MLPP) call is put on hold and reverts,
                                          					 the MLPP call loses its preemption status, and the reverted call gets treated
                                          					 as a routine call.

After the
                                          					 call reverts, the system does not play a preemption ring. If a high precedence
                                          					 call becomes a reverted call, the system does not play a precedence tone.

CTI
                                          					 Applications

CTI
                                          					 applications can access hold reversion functionality when the feature is
                                          					 enabled for a line or the system. Cisco-provided applications such as Cisco
                                          					 Unified Communications Manager Assistant and attendant console provide hold
                                          					 reversion functionality using the CTI interface.

When hold
                                          					 reversion gets invoked, the CTI port receives event notification instead of the
                                          					 audible tone presented on Cisco Unified IP Phones. CTI ports and route points
                                          					 receive the event notification once only, whereas Cisco Unified IP Phones
                                          					 receive alerts at regular intervals.

See the
                                          					 following API documents for information about CTI requirements and interactions
                                          					 with hold reversion:

- Cisco Unified
                                                						  Communications JTAPI Developer Guide

- Cisco Unified
                                                						  Communications TAPI Developer Guide

Hold
                                          					 Reversion Interval for SCCP phones when interacting with SIP Phones

SCCP
                                          					 phones support a minimum Hold Reversion Notification Interval (HRNI) of 5
                                          					 seconds, whereas SIP phones support a minimum of 10 seconds. SCCP phones set
                                          					 for the minimum HRNI of 5 seconds may experience a Hold Reversion Notification
                                          					 ring delay of 10 seconds when handling calls involving SIP phones.

Shared
                                          					 Lines

If a
                                          					 Cisco Unified IP Phone that supports hold reversion shares a line with a phone
                                          					 device that does not support hold reversion, the hold reversion configuration
                                          					 settings display only for the line on the supporting device.

If a
                                          					 shared line device disables the feature, hold reversion gets disabled on all
                                          					 other devices that share the line.

Ring
                                          					 Settings

If the
                                          					 ring settings that are configured for the phone specify Disabled, the phone
                                          					 does not ring, flash, or beep for the hold reversion feature.

## Hold Reversion
                        	 Restrictions

Feature

Restriction

Cisco
                                       					 Extension Mobility and Cisco Web Dialer

Cisco
                                       					 Extension Mobility and Cisco Web Dialer features do not support the hold
                                       					 reversion feature.

SCCP
                                       					 phones

This
                                       					 feature does not support SCCP analog phone types, such as ATA 186, DPA-7610,
                                       					 and DPA-7630.

Only
                                       					 certain on-net phone devices that are running SCCP on a node can invoke the
                                       					 hold reversion feature.

Directory
                                       					 numbers

If a directory number is associated to a phone that does not support hold reversion, the feature settings do not display for
                                       that directory number in the Directory Number Configuration window.

Shared
                                       					 lines

If a Cisco Unified IP Phone that supports hold reversion shares a line with a phone device that does not support hold reversion, the hold reversion configuration
                                       settings display only for the line on the supporting device.

If a
                                       					 shared-line device disables this feature, hold reversion gets disabled on all
                                       					 other devices that share this line.

Ring
                                       					 settings

Hold reversion ring uses the ring settings that Cisco Unified Communications Manager Administration defines for that user (disable, flash only, ring once, ring, beep only) except that flash gets converted to flash once, and
                                       ring gets converted to ring once.

When an IP Phone call is on normal hold, the ring settings (Phone Idle) from the Call Manager is applied.

Maximum
                                       					 number of reverted calls

The
                                       					 maximum number of reverted calls on a line equals the maximum number of calls
                                       					 on your system.

CTI
                                       					 Applications

To enable
                                       					 this feature with CTI applications, ensure that the CTI application is
                                       					 certified to work with this feature and this release. Otherwise, the CTI
                                       					 application may fail because the hold reversion feature may affect existing CTI
                                       					 applications. This feature gets disabled by default. See the following API
                                       					 documents for information about CTI requirements:

Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager

Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager

Cisco
                                       					 Unified IP Phones

You cannot
                                       					 configure hold reversion settings for DNs that are associated with phones that
                                       					 do not support this feature. Only Cisco Unified IP Phones that support the hold
                                       					 reversion feature display the hold reversion timer settings in the Directory
                                       					 Number Configuration window.

When Hold
                                       					 Reversion is configured for the system, the phone must support the feature or
                                       					 the feature does not activate.

See Cisco Unified IP Phone administration guides for Cisco Unified IP Phone models that support hold reversion and this version of Unified Communications Manager for any phone restrictions with hold reversion.

| Note | The type of
                                          			 alert that you receive depends on the capabilities of your phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Run a phone
                                          				feature list report to determine which phones support the Hold Reversion
                                          				feature. |
| Step 2 | Configure Call Focus Priority for Hold Reversion | Configure the
                                       			 call focus priority setting against the device pool for your phones. |
| Step 3 | Perform one of
                                       			 the following procedures: Configure Hold Reversion Timer Defaults for Cluster Configure Hold Reversion Timer Settings for Phone | Configure the
                                          				Hold Reversion timer settings. You can configure the timer using a clusterwide
                                          				service parameter, or configure the settings on an individual phone line. Note The settings
                                                      				  on an individual phone line override the clusterwide service parameter
                                                      				  settings. | Note | The settings
                                                      				  on an individual phone line override the clusterwide service parameter
                                                      				  settings. |
| Note | The settings
                                                      				  on an individual phone line override the clusterwide service parameter
                                                      				  settings. |

| Note | The settings
                                                      				  on an individual phone line override the clusterwide service parameter
                                                      				  settings. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Device
                                                				  Pool and open the device pool that applies to your
                                          			 phones. |
|---|---|
| Step 2 | In the Reverted Call Focus Priority field, choose one of
                                          			 the following options and click Save : Default —Incoming calls have priority over reverted
                                             				calls. Highest —Reverted calls have priority over incoming
                                             				calls. |
| Step 3 | Click Save . |
| Step 4 | Reset any
                                          			 devices in the Device Pool by performing the following steps: Click Reset . The Device Reset window displays. In the Device Reset window, click Reset . |

| Note | When you configure the clusterwide service parameters, the configuration is applied as the default hold reversion setting
                                          for all phones in the cluster. However, the settings on an individual phone line can override the clusterwide defaults. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is running the CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Configure values for the following clusterwide service parameters: Hold Reversion
                                                				Duration —Enter a number from 0 to 1200 (inclusive) to specify the wait time in
                                             				seconds before Cisco Unified Communications Manager issues a reverted call
                                             				alert to the holding party phone. If you enter 0, Cisco Unified Communications
                                             				Manager does not issue reverted call alerts, unless it is configured on a phone
                                             				line. Hold Reversion Interval
                                                				Notification —Enter a number from 0 to 1200 (inclusive) to specify the wait time
                                             				in seconds before Cisco Unified Communications Manager sends periodic reminder
                                             				alerts to the holding party phone. If you enter 0, Cisco Unified Communications
                                             				Manager does not send periodic reminder alerts unless the timer is configured
                                             				on a phone line. |
| Step 5 | Click Save . |

| Note | You can also configure
                                             		  Hold Reversion timer settings using a clusterwide service parameter. However, the settings on an individual phone line
                                             override the clusterwide service parameter setting. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone on which you want to configure Hold Reversion. |
| Step 3 | In the Association pane on the left, click the phone line on which you want to configure Hold Reversion. |
| Step 4 | Configure values for the following fields: Hold Reversion Ring
                                                				Duration —Enter a number from 0 to 1200 (inclusive) to specify the wait time in
                                             				seconds before Cisco Unified Communications Manager issues a reverted call
                                             				alert. If you enter 0, Cisco Unified Communications Manager does not issue
                                             				reverted call alerts to this DN. If you leave the field empty (the default
                                             				setting), Cisco Unified Communications Manager applies the setting from the Hold
                                             				Reversion Duration service parameter. Hold Reversion Ring
                                                				Interval Notification —Enter a number from 0 to 1200 (inclusive) to specify the
                                             				wait time in seconds before Cisco Unified Communications Manager sends periodic
                                             				reminder alerts. If you enter 0, Cisco Unified Communications Manager does not
                                             				send periodic reminder alerts to this DN. If you leave the field empty (the
                                             				default setting), Cisco Unified Communications Manager applies the setting from
                                             				the Hold Reversion Interval Notification service parameter. |
| Step 5 | Click Save . |
| Step 6 | Reset the phone by performing the following steps: Click Reset . The Reset Device window displays. Click Reset . |

| Feature | Interactions |
|---|---|
| Music on
                                          					 Hold | MOH is supported on a reverted call if MOH is
                                          					 configured for a normal held call. |
| Call Park | If hold
                                          					 reversion is invoked and the held party presses the Park softkey, the holding party still receives hold
                                          					 reversion alerts and can retrieve the call. When the holding party retrieves
                                          					 the call, the holding party receives MOH, if configured. If the
                                          					 held party parks before the hold duration exceeds the configured time limit,
                                          					 the system suppresses all hold reversion alerts until the call is picked up or
                                          					 redirected. |
| MLPP | When a
                                          					 multilevel precedence and preemption (MLPP) call is put on hold and reverts,
                                          					 the MLPP call loses its preemption status, and the reverted call gets treated
                                          					 as a routine call. After the
                                          					 call reverts, the system does not play a preemption ring. If a high precedence
                                          					 call becomes a reverted call, the system does not play a precedence tone. |
| CTI
                                          					 Applications | CTI
                                          					 applications can access hold reversion functionality when the feature is
                                          					 enabled for a line or the system. Cisco-provided applications such as Cisco
                                          					 Unified Communications Manager Assistant and attendant console provide hold
                                          					 reversion functionality using the CTI interface. When hold
                                          					 reversion gets invoked, the CTI port receives event notification instead of the
                                          					 audible tone presented on Cisco Unified IP Phones. CTI ports and route points
                                          					 receive the event notification once only, whereas Cisco Unified IP Phones
                                          					 receive alerts at regular intervals. See the
                                          					 following API documents for information about CTI requirements and interactions
                                          					 with hold reversion: Cisco Unified
                                                						  Communications JTAPI Developer Guide Cisco Unified
                                                						  Communications TAPI Developer Guide |
| Hold
                                          					 Reversion Interval for SCCP phones when interacting with SIP Phones | SCCP
                                          					 phones support a minimum Hold Reversion Notification Interval (HRNI) of 5
                                          					 seconds, whereas SIP phones support a minimum of 10 seconds. SCCP phones set
                                          					 for the minimum HRNI of 5 seconds may experience a Hold Reversion Notification
                                          					 ring delay of 10 seconds when handling calls involving SIP phones. |
| Shared
                                          					 Lines | If a
                                          					 Cisco Unified IP Phone that supports hold reversion shares a line with a phone
                                          					 device that does not support hold reversion, the hold reversion configuration
                                          					 settings display only for the line on the supporting device. If a
                                          					 shared line device disables the feature, hold reversion gets disabled on all
                                          					 other devices that share the line. |
| Ring
                                          					 Settings | If the
                                          					 ring settings that are configured for the phone specify Disabled, the phone
                                          					 does not ring, flash, or beep for the hold reversion feature. |

| Feature | Restriction |
|---|---|
| Cisco
                                       					 Extension Mobility and Cisco Web Dialer | Cisco
                                       					 Extension Mobility and Cisco Web Dialer features do not support the hold
                                       					 reversion feature. |
| SCCP
                                       					 phones | This
                                       					 feature does not support SCCP analog phone types, such as ATA 186, DPA-7610,
                                       					 and DPA-7630. Only
                                       					 certain on-net phone devices that are running SCCP on a node can invoke the
                                       					 hold reversion feature. |
| Directory
                                       					 numbers | If a directory number is associated to a phone that does not support hold reversion, the feature settings do not display for
                                       that directory number in the Directory Number Configuration window. |
| Shared
                                       					 lines | If a Cisco Unified IP Phone that supports hold reversion shares a line with a phone device that does not support hold reversion, the hold reversion configuration
                                       settings display only for the line on the supporting device. If a
                                       					 shared-line device disables this feature, hold reversion gets disabled on all
                                       					 other devices that share this line. |
| Ring
                                       					 settings | Hold reversion ring uses the ring settings that Cisco Unified Communications Manager Administration defines for that user (disable, flash only, ring once, ring, beep only) except that flash gets converted to flash once, and
                                       ring gets converted to ring once. Note When an IP Phone call is on normal hold, the ring settings (Phone Idle) from the Call Manager is applied. | Note | When an IP Phone call is on normal hold, the ring settings (Phone Idle) from the Call Manager is applied. |
| Note | When an IP Phone call is on normal hold, the ring settings (Phone Idle) from the Call Manager is applied. |
| Maximum
                                       					 number of reverted calls | The
                                       					 maximum number of reverted calls on a line equals the maximum number of calls
                                       					 on your system. |
| CTI
                                       					 Applications | To enable
                                       					 this feature with CTI applications, ensure that the CTI application is
                                       					 certified to work with this feature and this release. Otherwise, the CTI
                                       					 application may fail because the hold reversion feature may affect existing CTI
                                       					 applications. This feature gets disabled by default. See the following API
                                       					 documents for information about CTI requirements: Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager |
| Cisco
                                       					 Unified IP Phones | You cannot
                                       					 configure hold reversion settings for DNs that are associated with phones that
                                       					 do not support this feature. Only Cisco Unified IP Phones that support the hold
                                       					 reversion feature display the hold reversion timer settings in the Directory
                                       					 Number Configuration window. When Hold
                                       					 Reversion is configured for the system, the phone must support the feature or
                                       					 the feature does not activate. See Cisco Unified IP Phone administration guides for Cisco Unified IP Phone models that support hold reversion and this version of Unified Communications Manager for any phone restrictions with hold reversion. |

| Note | When an IP Phone call is on normal hold, the ring settings (Phone Idle) from the Call Manager is applied. |
|---|---|