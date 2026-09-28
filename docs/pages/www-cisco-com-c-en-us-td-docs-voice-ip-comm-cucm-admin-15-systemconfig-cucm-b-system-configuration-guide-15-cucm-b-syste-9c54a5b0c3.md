---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-systemconfig-cucm-b-system-configuration-guide-15-cucm-b-syste-9c54a5b0c3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15/cucm_b_system-configuration-guide-14_chapter_0100.html
retrieved_at: 2026-08-16T16:08:20.654698+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: August 7, 2026

Chapter: Configure Two Stacks (IPv4 and IPv6)

## Chapter: Configure Two Stacks (IPv4 and IPv6)

# Configure Two Stacks (IPv4 and IPv6)

## Two Stacks (IPv4 and IPv6) Overview

When your SIP network is configured for both IPv4 and IPv6 stacks, SIP devices can handle calls for each of the following
                              scenarios:

All
                                    devices in the call support IPv4 only

All
                                    devices in the call support IPv6 only

All
                                    devices in the call support both  IPv4 and IPv6 stacks. In this scenario, the
                                    system determines the IP address type by the configuration for the IP Addressing Mode Preference
                                       for Signaling setting for signaling events and the IP Addressing Mode Preference for Media enterprise parameter for media events.

One device supports IPv4 only and the other supports IPv6 only. In this scenario, Unified Communications Manager inserts an
                                    MTP into the call path to translate the signaling between the two addressing types.

For SIP devices and trunks, you can enable two-stack support by
                              configuring Alternate Network Address Types (ANAT). When ANAT is applied to a SIP device or trunk,
                              the SIP signaling that the device or trunk sends includes both an
                              IPv4 and IPv6 address,  if both are available. ANAT
                              allows the endpoint to interoperate seamlessly in both IPv4-only and IPv6-only
                              networks.

## Two Stacks (IPv4 and IPv6) Prerequisites

You must first configure Cisco Unified Communications Manager to support the IPv6 stack (IPv4 is enabled by default). This
                              includes setting IP addressing preferences for both media and signaling. For configuration details, see IPv6 Configuration Task Flow .

## Two Stacks (IPv4 and IPv6) Configuration Task Flow

Complete the following tasks to configure SIP devices and trunks to support both IPv4 and IPv6 addressing simultaneously.

Step 1

Configure ANAT for a SIP Profile

Configure a SIP Profile that supports both IPv4 and IPv6 stacks simultaneously.

Step 2

Apply ANAT to SIP Phone

Apply the ANAT-enabled SIP Profile to a SIP phone. This allows the SIP phone to support both IPv4 and IPv6 stacks simultaneously.

Step 3

Apply ANAT to a SIP Trunk

Apply  the ANAT-enabled SIP Profile to a SIP trunk. This allows the trunk to support both IPv4 and IPv6 stacks simultaneously.

Step 4

Restart Services

After configuring your system to support both IPv4 and IPv6 stacks simultaneously, restart essential services.

### Configure ANAT for a SIP Profile

Use this procedure to configure a SIP Profile that supports Alternate Network Address Types (ANAT). SIP devices and trunks
                                 that use this profile can interoperate seamlessly between IPv4-only and IPv6-only networks.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Do one of the following:

Click Add New to create a new SIP Profile.

Click Find and select an existing SIP Profile.

Step 3

Check the Enable ANAT check box.

Step 4

Complete the remaining fields in the SIP Profile Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

You must apply the SIP Profile to a SIP phone or SIP trunk to enable those devices to support both IPv4 and IPv6 stacks simultaneously.

### Apply ANAT to SIP Phone

Use this procedure to apply the Alternate Network Address Types (ANAT)
                                 configuration to a SIP phone. When ANAT is enabled, the phone
                                 can communicate with both IPv4-only and IPv6-only networks simultaneously.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select an existing phone.

Step 3

From the SIP Profile drop-down list box, select the SIP Profile
                                          on which you enabled ANAT.

Step 4

Complete the remaining fields in the Phone Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

### Apply ANAT to a SIP Trunk

Use this procedure to apply the Alternate Network Address Types configuration to an existing SIP trunk. This allows the SIP
                                 trunk to support both IPv4 and IPv6 stacks simultaneously.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Click Find and select an existing SIP trunk.

Step 3

From the SIP Profile drop-down list box, select the SIP Profile
                                          on which you enabled ANAT.

Step 4

Complete the remaining fields in the Trunk Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save

### Restart Services

After configuring your system to support both IPv4 and IPv6 stacks simultaneously, restart essential services.

Step 1

Log into Cisco Unified Serviceability and choose Tools > Control Center - Feature Services .

Step 2

Check the check box corresponding to each of the following services:

- Cisco CallManager

- Cisco CTIManager

- Cisco Certificate Authority Proxy Function

- Cisco IP Voice Media Streaming App

Step 3

Click Restart .

Step 4

Click OK .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure ANAT for a SIP Profile | Configure a SIP Profile that supports both IPv4 and IPv6 stacks simultaneously. |
| Step 2 | Apply ANAT to SIP Phone | Apply the ANAT-enabled SIP Profile to a SIP phone. This allows the SIP phone to support both IPv4 and IPv6 stacks simultaneously. |
| Step 3 | Apply ANAT to a SIP Trunk | Apply  the ANAT-enabled SIP Profile to a SIP trunk. This allows the trunk to support both IPv4 and IPv6 stacks simultaneously. |
| Step 4 | Restart Services | After configuring your system to support both IPv4 and IPv6 stacks simultaneously, restart essential services. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Do one of the following: Click Add New to create a new SIP Profile. Click Find and select an existing SIP Profile. |
| Step 3 | Check the Enable ANAT check box. |
| Step 4 | Complete the remaining fields in the SIP Profile Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . You must apply the SIP Profile to a SIP phone or SIP trunk to enable those devices to support both IPv4 and IPv6 stacks simultaneously. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select an existing phone. |
| Step 3 | From the SIP Profile drop-down list box, select the SIP Profile
                                          on which you enabled ANAT. |
| Step 4 | Complete the remaining fields in the Phone Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . |

| Note | For more information on SIP trunk configuration options, see Configure SIP Trunks . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Click Find and select an existing SIP trunk. |
| Step 3 | From the SIP Profile drop-down list box, select the SIP Profile
                                          on which you enabled ANAT. |
| Step 4 | Complete the remaining fields in the Trunk Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save |

| Step 1 | Log into Cisco Unified Serviceability and choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | Check the check box corresponding to each of the following services: Cisco CallManager Cisco CTIManager Cisco Certificate Authority Proxy Function Cisco IP Voice Media Streaming App |
| Step 3 | Click Restart . |
| Step 4 | Click OK . |