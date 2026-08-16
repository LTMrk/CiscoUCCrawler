---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-m-configure-confer-b7a33d55d6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_m_configure-conference-now.html
retrieved_at: 2026-08-16T16:03:42.425526+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Conference Now

## Chapter: Conference Now

# Conference Now

## Conference Now Overview

Conference Now provides a basic audio conferencing solution for small business customers that allows internal and external
                              callers to join a conference via a centralized IVR.

To host a meeting, configured users must configure a meeting PIN that they will need to enter, along with the meeting number,
                              when starting the meeting. The host provides the other meeting participants with the relevant meeting information, including
                              the time slot, meeting number (which is usually the host’s primary extension) and an optional access code for secure conferences.
                              At the designated time, the other participants can join the call by dialing the IVR, and entering the meeting information
                              at the prompts.

Administrators must configure end users with the ability to host Conference Now conferences. After the feature is configured,
                              meeting hosts can edit their meeting access code from within the Self-Care Portal.

## Conference Now Prerequisites

To use Conference Now you must make sure that the following media resources are configured, and are available to the devices
                              that will be initiating conferences.

Conference Bridge—For the best user experience, we recommend using a software-based Cisco IPVMS conference bridge. Using another
                                    conference bridge might not provide the conference party entry and exit tone.

Interactive Voice Response (IVR)

After you configure these resources, you can make them available to devices by configuring a media resource group list that
                              includes these resources and then associating that media resource group list to the device pools that will be used by your
                              devices, or to individual devices. For more information on configuring Conference Bridges, Interactive Voice Response, and
                              Media Resource Groups, see  "Configure Media Resources" section of the System Configuration Guide for Cisco Unified Communications Manager .

## Activate Cisco IP Voice Media Streaming

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server drop-down list, choose the Cisco Unified Communications Manager publisher node.

Step 3

If the Cisco IP Voice Media Streaming application is deactivated, check the corresponding check box and click Save .

## Configure Conference Now Settings

Step 1

From Cisco Unified CM Administration, choose Call Routing > Conference Now .

Step 2

In the Conference Now IVR Directory Number field, enter a DID (Direct Inward Dial) number for a Unified Communications Manager cluster to provide access for external callers.

Step 3

From the Route Partition drop-down list, select a partition.

Step 4

Complete the remaining fields in the Conference Now Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

### What to do next

Enable the feature for end users:

If you haven't yet synced your LDAP directory, add Conference Now to your LDAP sync, so that newly synced users will be able
                                    to host Conference Now meetings. See Enable Conference Now via LDAP .

To enable the feature for an existing end user, see Enable Conference Now for User .

## Enable Conference Now for User

You can also use Bulk Administration's Update Users feature to enable Conference Now for a large number of users via a csv
                                          file. You must ensure that the same settings as in the below task are configured. For more information, on how to use Update
                                          Users, see Bulk Administration Guide for Cisco Unified Communications Manager .

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Click Find and select the user for whom you want to add Conference Now.

Step 3

Under Conference Now , check the Enable End User to Host Conference Now check box.

Step 4

(Optional) For secure conferencing, enter an Attendees Access Code . Note that end users will be able to modify their access code setting within the Self-Care Portal.

Step 5

Complete any remaining fields within the End User Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 6

Click Save .

## Enable Conference Now via LDAP

Step 1

From Cisco Unified CM Administration, choose User Management > User Phone/Add > Feature Group Template .

Step 2

Do either of the following:

- Select Find and select an existing template.

- Click Add New to create a new template.

Step 3

From the drop-down list, select a Service Profile .

Step 4

From the drop-down list, select a User Profile .

Step 5

Check the Enable End User to Host Conference Now check box.

Step 6

Click Save .

### What to do next

Assign the template to an LDAP directory sync so that synced users will be configured for Conference Now. For more information
                              on configuring an LDAP sync, see the "Configure End Users" section of the System Configuration Guide for Cisco Unified Communications Manager .

Alternatively, you can add a new user with Conference Now functionality via the Quick User/Phone Add menu. You would need to add a new user that uses this feature group template in addition to assigning a primary extension.

## Conference Now
                        	 Interactions

Feature

Interactions

Mobility EFA (Enterprise Feature Access)

A mobility user dials an Enterprise Feature Access DID number from a remote destination. After the call is connected, the
                                          remote destination phone is used to send DTMF digits to Unified Communications Manager via the PSTN gateway.

The user PIN followed by the # key is first authenticated with Unified Communications Manager . After the user PIN authentication is successful, press 1 and the # key, to indicate a two-stage dialed call, followed by
                                          the desired phone number. If the dialed phone number is a Conference Now IVR Directory Number and the user is a meeting host,
                                          then the user must enter the PIN again.

Mobility MVA (Mobile Voice Access)

A call is directed to Unified Communications Manager through the enterprise PSTN H.323 or SIP gateway. The IVR prompts the user to enter the User ID, # key, PIN, # key, number
                                          1 (to make a Mobile Voice Access call) and then the desired phone number. If the phone number is a Conference Now IVR Directory
                                          Number and the user is a meeting host, then the user must enter the PIN again.

Users are not prompted for entering their PIN if they dial directly from their remote destination. However, if they dial
                                                      from a different phone to Mobile Voice Access Directory Number, then they are prompted to enter PIN before they can make the
                                                      call. If the users call Conference Now IVR Directory Number, they are prompted to enter the PIN again.

## Conference Now
                        	 Restrictions

The Conference Now feature has the following restrictions:

The host cannot mute attendees.

The attendee cannot mute the audio by entering DTMF digits.

The list of Conference Now participants is not supported.

Maximum number of participants in a conference is controlled by the existing CallManager service parameter "Maximum MeetMe
                                    Conference Unicast". It applies to both internal and external callers.

Maximum number of simultaneous Conference Now and MeetMe conference instances combined together is 100 per Unified Communications Manager CallManager node.

Video on hold is not supported.

The IPVMS software conference bridge only supports codec G.711 (ALaw & ULaw) and Wide Band 256k. If there is a codec mismatch
                                    between the calling device and the software conference bridge, a transcoder will be allocated.

Ensure that at least one of the following conditions are met to play the conference party entry and exit tone:

At least one conference participant is using the Cisco IP Phone.

IPVMS is the allocated software conference bridge.

When the sets up a Conference Bridge, the conference will continue with the remaining attendees irrespective whether the
                                    host is present or not. If the host wants to rejoin the conference, an announcement to enter the Attendee Access Code is played
                                    if it is configured by host. The host cannot schedule or mute attendees; therefore, the host status is no longer valid.

No audio announcement will play if the host is the first person to join the conference. However, when the host dials into
                                    Conference Now from an internal IP Phone, there is a visual display on the IP Phone showing "To Conference" .

| Note | Cisco recommends that you use IPVMS software-based conference bridges for Conference Now. If you use other conference bridges,
                                       the conference entry and exit tones may not play to participants. |
|---|---|

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down list, choose the Cisco Unified Communications Manager publisher node. |
| Step 3 | If the Cisco IP Voice Media Streaming application is deactivated, check the corresponding check box and click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Conference Now . |
|---|---|
| Step 2 | In the Conference Now IVR Directory Number field, enter a DID (Direct Inward Dial) number for a Unified Communications Manager cluster to provide access for external callers. |
| Step 3 | From the Route Partition drop-down list, select a partition. Note The combination of the number and the partition must be unique within a cluster. | Note | The combination of the number and the partition must be unique within a cluster. |
| Note | The combination of the number and the partition must be unique within a cluster. |
| Step 4 | Complete the remaining fields in the Conference Now Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |

| Note | The combination of the number and the partition must be unique within a cluster. |
|---|---|

| Note | You can also use Bulk Administration's Update Users feature to enable Conference Now for a large number of users via a csv
                                          file. You must ensure that the same settings as in the below task are configured. For more information, on how to use Update
                                          Users, see Bulk Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Click Find and select the user for whom you want to add Conference Now. |
| Step 3 | Under Conference Now , check the Enable End User to Host Conference Now check box. |
| Step 4 | (Optional) For secure conferencing, enter an Attendees Access Code . Note that end users will be able to modify their access code setting within the Self-Care Portal. Note If the user has a Self-Service User ID assigned, the Conference Now Meeting Number prepopulates with the value of the Self-Service User ID , which defaults to the user's primary extension. | Note | If the user has a Self-Service User ID assigned, the Conference Now Meeting Number prepopulates with the value of the Self-Service User ID , which defaults to the user's primary extension. |
| Note | If the user has a Self-Service User ID assigned, the Conference Now Meeting Number prepopulates with the value of the Self-Service User ID , which defaults to the user's primary extension. |
| Step 5 | Complete any remaining fields within the End User Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 6 | Click Save . |

| Note | If the user has a Self-Service User ID assigned, the Conference Now Meeting Number prepopulates with the value of the Self-Service User ID , which defaults to the user's primary extension. |
|---|---|

| Note | You cannot apply feature group template edits to an LDAP directory sync where the initial sync has already occurred. To apply
                                       these edits to an LDAP sync, the initial sync must not yet have occurred. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Phone/Add > Feature Group Template . |
|---|---|
| Step 2 | Do either of the following: Select Find and select an existing template. Click Add New to create a new template. |
| Step 3 | From the drop-down list, select a Service Profile . |
| Step 4 | From the drop-down list, select a User Profile . |
| Step 5 | Check the Enable End User to Host Conference Now check box. |
| Step 6 | Click Save . |

| Feature | Interactions |
|---|---|
| Mobility EFA (Enterprise Feature Access) | A mobility user dials an Enterprise Feature Access DID number from a remote destination. After the call is connected, the
                                          remote destination phone is used to send DTMF digits to Unified Communications Manager via the PSTN gateway. The user PIN followed by the # key is first authenticated with Unified Communications Manager . After the user PIN authentication is successful, press 1 and the # key, to indicate a two-stage dialed call, followed by
                                          the desired phone number. If the dialed phone number is a Conference Now IVR Directory Number and the user is a meeting host,
                                          then the user must enter the PIN again. |
| Mobility MVA (Mobile Voice Access) | A call is directed to Unified Communications Manager through the enterprise PSTN H.323 or SIP gateway. The IVR prompts the user to enter the User ID, # key, PIN, # key, number
                                          1 (to make a Mobile Voice Access call) and then the desired phone number. If the phone number is a Conference Now IVR Directory
                                          Number and the user is a meeting host, then the user must enter the PIN again. Note Users are not prompted for entering their PIN if they dial directly from their remote destination. However, if they dial
                                                      from a different phone to Mobile Voice Access Directory Number, then they are prompted to enter PIN before they can make the
                                                      call. If the users call Conference Now IVR Directory Number, they are prompted to enter the PIN again. | Note | Users are not prompted for entering their PIN if they dial directly from their remote destination. However, if they dial
                                                      from a different phone to Mobile Voice Access Directory Number, then they are prompted to enter PIN before they can make the
                                                      call. If the users call Conference Now IVR Directory Number, they are prompted to enter the PIN again. |
| Note | Users are not prompted for entering their PIN if they dial directly from their remote destination. However, if they dial
                                                      from a different phone to Mobile Voice Access Directory Number, then they are prompted to enter PIN before they can make the
                                                      call. If the users call Conference Now IVR Directory Number, they are prompted to enter the PIN again. |

| Note | Users are not prompted for entering their PIN if they dial directly from their remote destination. However, if they dial
                                                      from a different phone to Mobile Voice Access Directory Number, then they are prompted to enter PIN before they can make the
                                                      call. If the users call Conference Now IVR Directory Number, they are prompted to enter the PIN again. |
|---|---|

| Note | If the host joins the Conference Now from any external phone, then there will be no visual display on the phone. |
|---|---|