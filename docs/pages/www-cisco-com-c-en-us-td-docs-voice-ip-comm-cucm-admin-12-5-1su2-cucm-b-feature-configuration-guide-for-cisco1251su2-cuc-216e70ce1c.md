---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-cucm-b-feature-configuration-guide-for-cisco1251su2-cuc-216e70ce1c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_0101011.html
retrieved_at: 2026-08-16T17:12:33.956910+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Private Line Automatic Ringdown

## Chapter: Private Line Automatic Ringdown

# Private Line Automatic Ringdown

## Private Line
                        	 Automatic Ringdown Overview

The Private Line
                              		  Automatic Ringdown (PLAR) feature configures a phone so that when the user goes
                              		  off hook (or the NewCall softkey or line key gets pressed), the phone
                              		  immediately dials a preconfigured number. The phone user cannot dial any other
                              		  number from the phone line that gets configured for PLAR.

PLAR works with
                              		  features such as Barge, cBarge, or single button Barge. If you use PLAR with a
                              		  feature, you must configure the feature as described in the feature
                              		  documentation, and you must configure the PLAR destination, which is a
                              		  directory number that is used specifically for PLAR.

## Private Line
                        	 Automatic Ringdown Configuration Task Flow for SCCP Phones

Perform the
                              		  following tasks to configure Private Line Automatic Ringdown (PLAR) on SCCP
                              		  phones.

Step 1

Create Partition

Create a
                                          				partition for the PLAR destination. The only directory number that you can
                                          				assign to this partition is the PLAR destination.

Step 2

Assign Partitions to Calling Search Spaces

Assign the
                                          				partition to a unique CSS, and a CSS that includes the PLAR destination device.

Step 3

Assign Partition to the Private Line Automatic Ringdown Destination

Step 4

Configure Translation Pattern for Private Line Automatic Ringdown on Phones

### Create
                           	 Partition

Create a new
                                 		  partition for the Private Line Automatic Ringdown (PLAR) destination. For the
                                 		  feature to work, only the null translation pattern that you configure for PLAR
                                 		  can be assigned to this partition.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

Click Add
                                             				New .

Step 3

In the Name field, enter a partition name and a description
                                          			 separated by a comma.

Step 4

Click Save .

### Assign Partitions
                           	 to Calling Search Spaces

For Private Line Automatic Ringdown (PLAR) on SCCP phones, you must configure two calling search spaces (CSS):

The first CSS should include the new partition for the null translation pattern as well as a partition that routes to the
                                       destination phone.

The second CSS should include only the new partition for the null translation pattern.

#### Before you begin

Create Partition

Step 1

From Cisco Unified CM Administration, choose Call Control > Class of Control > Calling Search Space .

Step 2

Click Find and select the calling search space for the
                                          			 PLAR destination device.

Step 3

Use the arrows
                                          			 to move both of the following partitions to the Selected Partitions list box: the new partition that
                                          			 you created for the null translation pattern and a partition that routes to the
                                          			 destination device.

Step 4

Click Save .

Step 5

Click Add
                                             				New .

Step 6

Enter a name
                                          			 and description for the calling search space.

Step 7

Use the arrows
                                          			 to move the new partition to the Selected Partitions list box.

Step 8

Click Save .

### Assign Partition
                           	 to the Private Line Automatic Ringdown Destination

When configuring
                                 		  Private Line Automatic Ringdown (PLAR) on SCCP phones, assign a null partition
                                 		  to the directory number that you want to use as the PLAR destination.

Each PLAR
                                             			 destination directory number must have its own unique partition. Do not add any
                                             			 other directory numbers to the null partition that you created for the PLAR
                                             			 destination.

#### Before you begin

Assign Partitions to Calling Search Spaces

Step 1

In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Directory Number .

Step 2

Click Find and select the directory number that you want
                                          			 to use as the PLAR destination.

Step 3

In the Route
                                             				Partition field, select a partition that you created for your PLAR
                                          			 destination.

Step 4

In the Calling Search Space drop-down list, select the CSS that includes both the null partition and the destination device.

Step 5

Click Save .

### Configure
                           	 Translation Pattern for Private Line Automatic Ringdown on Phones

To configure
                                 		  Private Line Automatic Ringdown (PLAR) on phones, configure a null translation
                                 		  pattern and assign the PLAR destination number to that translation pattern.

#### Before you begin

Assign Partition to the Private Line Automatic Ringdown Destination

Step 1

In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Translation Pattern .

Step 2

Click Add
                                             				New to create a new translation pattern.

Step 3

Leave the Translation Pattern field empty.

Step 4

From the Partition drop-down list, select the new partition that you created for the null translation pattern.

Step 5

From the Calling Search Space drop-down list, select a calling search space that includes both the new partition and the partition for the PLAR destination
                                          device.

Step 6

In the Called
                                             				Party Transformation Mask field, enter the PLAR destination
                                          			 directory number.

Step 7

Click Save .

## Private Line
                        	 Automatic Ringdown Configuration Task Flow for SIP Phones

Perform these
                              		  tasks to configure Private Line Automatic Ringdown (PLAR) on SIP Phones.

Step 1

Create SIP Dial Rule for Private Line Automatic Ringdown

Create a SIP
                                          				dial rule for PLAR.

Step 2

Assign Private Line Automatic Ringdown Dial Rule to SIP Phone

Assign the
                                          				PLAR dial rule to the phone.

### Create SIP Dial
                           	 Rule for Private Line Automatic Ringdown

To configure
                                 		  Private Line Automatic Ringdown (PLAR) on SIP phones, you must configure a SIP
                                 		  dial rule for your PLAR destination number.

Step 1

In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Class of Control > SIP Dial
                                                				  Rules .

Step 2

Click Add
                                             				New .

Step 3

From the Dial Pattern drop-down list, choose 7940_7960_OTHER .

Step 4

Click Next .

Step 5

Enter a name
                                          			 and description for the dial rule.

Step 6

Click Next .

Step 7

In the Pattern field, enter a pattern that matches the PLAR
                                          			 destination number and click Add
                                             				PLAR .

Step 8

Click Save .

### Assign Private Line Automatic Ringdown Dial Rule to SIP Phone

You can configure Private Line Automatic Ringdown (PLAR) on SIP phones by
                                 		  assigning a PLAR-enabled SIP Dial Rule to the
                                 		  phone.

#### Before you begin

Create SIP Dial Rule for Private Line Automatic Ringdown

Step 1

In Cisco
                                          			 Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone on which you want to configure PLAR.

Step 3

From the SIP Dial Rules drop-down list, choose the dial rule that you created for PLAR.

Step 4

Click Save .

## Private Line Automatic Ringdown Troubleshooting

### Troubleshooting Private Line Automatic Ringdown on SCCP
                              		  Phones

Symptom

Solution

The phone goes off hook and the user hears a fast busy
                                          					 (reorder) tone.

Make sure that the CSS that is assigned to the PLAR
                                          					 translation pattern contains the partition of the PLAR destination.

The phone goes off hook and receives dial tone.

Make sure that the CSS that is assigned to the phone contains
                                          					 the partition of the null PLAR translation pattern.

### Troubleshooting Private Line Automatic Ringdown on SIP
                              		  Phones

Symptom

Solution

The phone goes off hook and the user hears fast busy (reorder)
                                          					 tone.

Make sure that the CSS of the SIP phone can reach the PLAR
                                          					 destination.

The phone goes off hook and receives a dial tone.

Make sure that the SIP Dial Rule has been created and is
                                          					 assigned to the phone.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create Partition | Create a
                                          				partition for the PLAR destination. The only directory number that you can
                                          				assign to this partition is the PLAR destination. |
| Step 2 | Assign Partitions to Calling Search Spaces | Assign the
                                          				partition to a unique CSS, and a CSS that includes the PLAR destination device. |
| Step 3 | Assign Partition to the Private Line Automatic Ringdown Destination | Assign the
                                       			 null partition and a CSS to your PLAR destination directory number. |
| Step 4 | Configure Translation Pattern for Private Line Automatic Ringdown on Phones | Create a null
                                       			 translation pattern and assign it to your PLAR destination directory number. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | In the Name field, enter a partition name and a description
                                          			 separated by a comma. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Control > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Find and select the calling search space for the
                                          			 PLAR destination device. |
| Step 3 | Use the arrows
                                          			 to move both of the following partitions to the Selected Partitions list box: the new partition that
                                          			 you created for the null translation pattern and a partition that routes to the
                                          			 destination device. |
| Step 4 | Click Save . |
| Step 5 | Click Add
                                             				New . |
| Step 6 | Enter a name
                                          			 and description for the calling search space. |
| Step 7 | Use the arrows
                                          			 to move the new partition to the Selected Partitions list box. |
| Step 8 | Click Save . |

| Note | Each PLAR
                                             			 destination directory number must have its own unique partition. Do not add any
                                             			 other directory numbers to the null partition that you created for the PLAR
                                             			 destination. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Directory Number . |
|---|---|
| Step 2 | Click Find and select the directory number that you want
                                          			 to use as the PLAR destination. |
| Step 3 | In the Route
                                             				Partition field, select a partition that you created for your PLAR
                                          			 destination. |
| Step 4 | In the Calling Search Space drop-down list, select the CSS that includes both the null partition and the destination device. |
| Step 5 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Translation Pattern . |
|---|---|
| Step 2 | Click Add
                                             				New to create a new translation pattern. |
| Step 3 | Leave the Translation Pattern field empty. |
| Step 4 | From the Partition drop-down list, select the new partition that you created for the null translation pattern. |
| Step 5 | From the Calling Search Space drop-down list, select a calling search space that includes both the new partition and the partition for the PLAR destination
                                          device. |
| Step 6 | In the Called
                                             				Party Transformation Mask field, enter the PLAR destination
                                          			 directory number. |
| Step 7 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create SIP Dial Rule for Private Line Automatic Ringdown | Create a SIP
                                          				dial rule for PLAR. |
| Step 2 | Assign Private Line Automatic Ringdown Dial Rule to SIP Phone | Assign the
                                          				PLAR dial rule to the phone. |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Class of Control > SIP Dial
                                                				  Rules . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | From the Dial Pattern drop-down list, choose 7940_7960_OTHER . |
| Step 4 | Click Next . |
| Step 5 | Enter a name
                                          			 and description for the dial rule. |
| Step 6 | Click Next . |
| Step 7 | In the Pattern field, enter a pattern that matches the PLAR
                                          			 destination number and click Add
                                             				PLAR . |
| Step 8 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone on which you want to configure PLAR. |
| Step 3 | From the SIP Dial Rules drop-down list, choose the dial rule that you created for PLAR. |
| Step 4 | Click Save . |

| Symptom | Solution |
|---|---|
| The phone goes off hook and the user hears a fast busy
                                          					 (reorder) tone. | Make sure that the CSS that is assigned to the PLAR
                                          					 translation pattern contains the partition of the PLAR destination. |
| The phone goes off hook and receives dial tone. | Make sure that the CSS that is assigned to the phone contains
                                          					 the partition of the null PLAR translation pattern. |

| Symptom | Solution |
|---|---|
| The phone goes off hook and the user hears fast busy (reorder)
                                          					 tone. | Make sure that the CSS of the SIP phone can reach the PLAR
                                          					 destination. |
| The phone goes off hook and receives a dial tone. | Make sure that the SIP Dial Rule has been created and is
                                          					 assigned to the phone. |