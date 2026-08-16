---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-cucm-b-feature-configuration-guide-for-cisco1251su2-cuc-b944d371ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_01000010.html
retrieved_at: 2026-08-16T17:16:27.273311+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Configure SIP Normalization and Transparency

## Chapter: Configure SIP Normalization and Transparency

# Configure SIP Normalization and Transparency

## SIP Normalization and Transparency Overview

SIP normalization and transparency is an optional feature that handles SIP interoperability issues between Unified Communications
                           Manager and endpoints, service providers, PBXs, or gateways that implement SIP differently. To configure SIP normalization
                           and transparency, apply a customized LUA script to a SIP trunk or SIP line. Unified Communications Manager applies the script
                           to the SIP messaging that passes through the SIP trunks or SIP lines.

Upon installation, Unified Communications Manager contains default normalization and transparency scripts that you can assign
                           to the SIP trunks and SIP profiles in your system. You can also create and import your own customized scripts.

### SIP Normalization

SIP normalization scripts modify incoming and outgoing SIP messages. For example, if you are interoperating Unified Communications
                              Manager with a Cisco TelePresence Video Communications Server, apply the vcs-interop script to the SIP trunk that connects the two. The script resolves the differences in the SIP messaging so that the two products
                              can communicate.

You can apply a normalization script to any SIP trunk connection, regardless of which protocol is being used by the endpoint
                              that connects to that SIP trunk.

### SIP  Transparency

SIP transparency scripts enable Unified Communications Manager to transparently pass SIP information, such as proprietary
                              headers, from one call leg to the other. For transparency to work, both call legs must be SIP.

Another feature of SIP transparency is REFER transparency, which allows Unified Communications Manager to pass on REFER requests
                              without acting on them. You can use REFER transparency in call center environments where a centralized agent may answer a
                              call and then transfer the call to an agent who resides in the same geographical area as the caller. REFER transparency allows
                              the centralized Unified Communications Manager to drop the call and shift call control to the new agent.

### Default Scripts
                           	 for SIP Normalization and Transparency

Upon installation, Cisco Unified Communications Manager contains the following default scripts for SIP Normalization and Transparency.
                              You can apply these scripts to a SIP trunk or SIP profile, but you cannot edit these scripts. If none of these scripts meet
                              your needs, you can create your own scripts:

cisco-meeting-server-interop —Provides interoperability between Cisco Unified Communications Manager and Cisco Meeting Server (CMS).

cisco-telepresence-conductor-interop —Provides interoperability for endpoints that are registered to TelePresence Conductor.

cisco-telepresence-mcu-ts-direct-interop —Provides interoperability between Cisco Unified Communications Manager and either Cisco TelePresence MCU or Cisco TelePresence
                                    Server.

diversion-counter —Provides capability to adjust the diversion counter.

HCS-PCV-PAI passthrough —Provides Cisco HCS platform integration with Enterprise IMS.

refer-passthrough —Removes Cisco Unified Communications Manager from the call due to a blind transfer between SIP trunks.

vcs-interop —Provides interoperability for endpoints that are registered to the Cisco TelePresence Video Communications Server.

## SIP Normalization and Transparency Prerequisites

Cisco Unified Communications Manager provides default scripts for SIP Normalization and Transparency. Make sure to review
                                 the existing scripts and system settings to verify whether they meet your needs. For information on the available default
                                 scripts, see Default Scripts for SIP Normalization and Transparency .

Make sure that you understand your deployment's SIP requirements in addition to the SIP requirements for any third-party products.
                                 For information on Cisco Unified Communications Manager's implementation of SIP, review the SIP Line Messaging Guide for Cisco Unified Communications Manager (Standard Edition) at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-programming-reference-guides-list.html .

If you plan to develop customized SIP Normalization scripts, review the Developer Guide for SIP Normalization and Transparency at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-programming-reference-guides-list.html .

## SIP Normalization and Transparency Configuration Task Flow

Step 1

Create New SIP Normalization and Transparency Scripts

Optional. If none of the preinstalled scripts meet your needs, use this procedure to configure a customized script. You can
                                          create your new script in the SIP Normalization Script Configuration window or you can import a customized script.

Step 2

Apply Normalization or Transparency Script to SIP Trunk

In the Trunk Configuration window, apply a script directly to a SIP trunk. Cisco Unified Communications Manager applies the
                                          script to all the SIP messaging that passes through the trunk

Step 3

Apply Normalization or Transparency to SIP Devices

If you want to apply a normalization or transparency script to a SIP line, apply  a script to the SIP profile that is associated
                                          to that SIP line. Cisco Unified Communications Manager applies the script to all SIP messaging that uses that SIP profile.

### Create New SIP
                           	 Normalization and Transparency Scripts

If the default
                                 		  normalization and transparency scripts do not meet your needs, use this
                                 		  procedure to create a new LUA script. You can either write the new script in
                                 		  Cisco Unified Communications Manager or import a file into the system.

Tip

If the script
                                             			 that you want to create closely resembles a default script, open the default
                                             			 script in the SIP
                                                				Normalization Script Configuration window and copy the Contents text box. Create a new script and paste the
                                             			 contents into the Contents text box. You can then edit the content in
                                             			 the new script.

The memory utilization of the SIP Normalization Script is based on each trunk and not on each script.

Step 1

In Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > SIP Normalization Script .

Step 2

Click Add
                                             				New .

Step 3

Enter a Name and Description for your script.

Step 4

If you are
                                          			 writing a new script, edit the script in the Contents text box.

Step 5

Optional. If
                                          			 you have an external file that you want to import, do the following

Click Import
                                                   					 File .

Browse to
                                                				  locate the file and select the file.

Click Import File .

Step 6

Complete the
                                          			 fields in the SIP
                                             				Normalization Script Configuration window. For help with the fields
                                          			 and their contents, refer to the online help.

Step 7

Click Save .

#### What to do next

Assign the script
                                 		  to a SIP profile or SIP trunk:

Apply Normalization or Transparency to SIP Devices

Apply Normalization or Transparency Script to SIP Trunk

### Apply Normalization or Transparency Script to SIP Trunk

Use this procedure to apply a SIP normalization or transparency script to a SIP trunk. Cisco Unified Communications Manager
                                 applies the script to all SIP messaging that passes through the trunk.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Click Find and select the trunk to which you want to apply a script.

Step 3

From the Normalization Script drop-down list, choose the script that you want to apply to the trunk.

Step 4

(Optional) If you want to normalize specific parameters within the SIP messaging, do the following:

Enter the Parameter Name that you want to normalize, and the Parameter Value for the value that you want to apply to the parameter. For example, you could enter a Location parameter and North Carolina as the value.

To add additional parameters, click the (+) to create additional lines where you can enter additional parameters and values.

Step 5

(Optional) If you want to produce SDI traces against the script, check the Enable Trace check box.

Step 6

Click Save .

### Apply Normalization or Transparency to SIP Devices

You can apply a customized SIP Normalization and Transparency script, or a customized SDP Transparency Profile to a SIP phone
                                 by applying the script to the SIP Profile that is used by that device.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Click Find and select the SIP profile to which you want to apply a script.

Step 3

In the SDP Information area, from the SDP Transparency Profile drop-down list, choose a profile.

Step 4

From the Normalization Script drop-down list, choose the script that you want to apply to the trunk.

Step 5

(Optional) If you want to normalize specific parameters within the SIP messaging, do the following:

Enter the Parameter Name that you want to normalize, and the Parameter Value for the value that you want to apply to the parameter. For example, you could enter a Location parameter and North Carolina as the value.

To add additional parameters, click the (+) to create additional lines where you can enter additional parameters and values.

Step 6

(Optional) If you want to produce SDI traces against the script, check the Enable Trace check box.

Step 7

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create New SIP Normalization and Transparency Scripts | Optional. If none of the preinstalled scripts meet your needs, use this procedure to configure a customized script. You can
                                          create your new script in the SIP Normalization Script Configuration window or you can import a customized script. |
| Step 2 | Apply Normalization or Transparency Script to SIP Trunk | In the Trunk Configuration window, apply a script directly to a SIP trunk. Cisco Unified Communications Manager applies the
                                          script to all the SIP messaging that passes through the trunk |
| Step 3 | Apply Normalization or Transparency to SIP Devices | If you want to apply a normalization or transparency script to a SIP line, apply  a script to the SIP profile that is associated
                                          to that SIP line. Cisco Unified Communications Manager applies the script to all SIP messaging that uses that SIP profile. |

| Tip | If the script
                                             			 that you want to create closely resembles a default script, open the default
                                             			 script in the SIP
                                                				Normalization Script Configuration window and copy the Contents text box. Create a new script and paste the
                                             			 contents into the Contents text box. You can then edit the content in
                                             			 the new script. |
|---|---|

| Note | The memory utilization of the SIP Normalization Script is based on each trunk and not on each script. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > SIP Normalization Script . |
|---|---|
| Step 2 | Click Add
                                             				New . The SIP
                                          			 Normalization Script Configuration window appears. |
| Step 3 | Enter a Name and Description for your script. |
| Step 4 | If you are
                                          			 writing a new script, edit the script in the Contents text box. |
| Step 5 | Optional. If
                                          			 you have an external file that you want to import, do the following Click Import
                                                   					 File . Browse to
                                                				  locate the file and select the file. Click Import File . The SIP
                                                   					 Normalization Script Configuration window displays the contents of
                                                				  the imported file in the Contents text box. |
| Step 6 | Complete the
                                          			 fields in the SIP
                                             				Normalization Script Configuration window. For help with the fields
                                          			 and their contents, refer to the online help. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Click Find and select the trunk to which you want to apply a script. |
| Step 3 | From the Normalization Script drop-down list, choose the script that you want to apply to the trunk. |
| Step 4 | (Optional) If you want to normalize specific parameters within the SIP messaging, do the following: Enter the Parameter Name that you want to normalize, and the Parameter Value for the value that you want to apply to the parameter. For example, you could enter a Location parameter and North Carolina as the value. To add additional parameters, click the (+) to create additional lines where you can enter additional parameters and values. |
| Step 5 | (Optional) If you want to produce SDI traces against the script, check the Enable Trace check box. Note Cisco recommends that you enable tracing while debugging your scripts. | Note | Cisco recommends that you enable tracing while debugging your scripts. |
| Note | Cisco recommends that you enable tracing while debugging your scripts. |
| Step 6 | Click Save . |

| Note | Cisco recommends that you enable tracing while debugging your scripts. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Click Find and select the SIP profile to which you want to apply a script. |
| Step 3 | In the SDP Information area, from the SDP Transparency Profile drop-down list, choose a profile. |
| Step 4 | From the Normalization Script drop-down list, choose the script that you want to apply to the trunk. |
| Step 5 | (Optional) If you want to normalize specific parameters within the SIP messaging, do the following: Enter the Parameter Name that you want to normalize, and the Parameter Value for the value that you want to apply to the parameter. For example, you could enter a Location parameter and North Carolina as the value. To add additional parameters, click the (+) to create additional lines where you can enter additional parameters and values. |
| Step 6 | (Optional) If you want to produce SDI traces against the script, check the Enable Trace check box. Note Cisco recommends that you enable tracing while debugging your scripts. | Note | Cisco recommends that you enable tracing while debugging your scripts. |
| Note | Cisco recommends that you enable tracing while debugging your scripts. |
| Step 7 | Click Save . |

| Note | Cisco recommends that you enable tracing while debugging your scripts. |
|---|---|