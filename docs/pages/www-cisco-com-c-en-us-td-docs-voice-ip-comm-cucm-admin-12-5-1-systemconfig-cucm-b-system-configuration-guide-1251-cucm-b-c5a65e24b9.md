---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-c5a65e24b9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_010111.html
retrieved_at: 2026-08-16T17:30:58.403351+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Transformation Patterns

## Chapter: Configure Transformation Patterns

# Configure Transformation Patterns

## Transformation
                        	 Pattern Overview

Transformation
                              		  patterns determine how the system manipulates the digits that were dialed in an
                              		  incoming or outgoing call. You can configure transformation patterns when you
                              		  need to change the calling or called number before the system sends it to the
                              		  phone or the PSTN.

You can use
                              		  transformation patterns to discard digits, prefix digits, add a calling party
                              		  transformation mask, and control the presentation of the calling party number.

You can:

Hit a Calling Party Transformation Pattern with a Called Party Transformation CSS.

Hit a Called Party Transformation Pattern with a Calling Party Transformation CSS.

## Transformation Pattern Configuration Task Flow

Step 1

Configure Calling Party Transformation Patterns

Use this procedure to transform the calling number. For example, you can configure a transformation pattern that replaces
                                          a caller's extension
                                          with the office's main number when calling the PSTN.

Step 2

Configure Called Party Transformation Patterns

Use this procedure to transform the called number. For example, you can configure a transformation pattern that retains only
                                          the last five
                                          digits of a call dialed as a ten-digit number.

Step 3

Configure Transformation Profiles

Optional : Perform this procedure only if you are using Cisco Intercompany Media Engine (Cisco IME).  You must configure a transformation
                                          profile to convert dialed numbers into the E.164 format.

### Configure Calling Party Transformation Patterns

Use this procedure to transform the calling number. For example, you can configure a transformation pattern that replaces
                                 a caller's extension
                                 with the office's main number when calling the PSTN.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Calling Party Transformation Pattern .

Step 2

Choose one of the following options:

- Click Add New to add a new calling party transformation pattern.

- Click Find and select an existing pattern.

Step 3

From the Pattern field, enter the pattern that you want to match to the calling party number.

For Outboud Calls:

The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone).

While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask.

Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA.

Step 4

Complete the remaining fields in the Calling Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

### Configure Called Party Transformation Patterns

Use this procedure to transform the called number. For example, you can configure a transformation pattern that retains only
                                 the last five
                                 digits of a call dialed as a ten-digit number.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Called Party Transformation Pattern .

Step 2

Choose one of the following options:

- Click Add New , to add a new called party transformation pattern.

- Click Find and select an existing pattern.

Step 3

From the Pattern field, enter the pattern that you want to match to the called number.

Step 4

Complete the remaining fields in the Called Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

### Configure Transformation Profiles

Perform this procedure only if you are using  Cisco Intercompany Media Engine (Cisco IME). You must configure a transformation
                                 profile to convert dialed numbers into the E.164 format. The  E.164 format  includes the international "+" prefix; for example,
                                 "+14085551212".

Step 1

From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Profile .

Step 2

Choose one of the following options:

- Click Add New , to add a new transformation profile.

- Click Find and choose a pattern from the resulting list, to modify the settings for an existing transformation profile.

Step 3

Configure the fields in the Transformation Profile Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Calling Party Transformation Patterns | Use this procedure to transform the calling number. For example, you can configure a transformation pattern that replaces
                                          a caller's extension
                                          with the office's main number when calling the PSTN. |
| Step 2 | Configure Called Party Transformation Patterns | Use this procedure to transform the called number. For example, you can configure a transformation pattern that retains only
                                          the last five
                                          digits of a call dialed as a ten-digit number. |
| Step 3 | Configure Transformation Profiles | Optional : Perform this procedure only if you are using Cisco Intercompany Media Engine (Cisco IME).  You must configure a transformation
                                          profile to convert dialed numbers into the E.164 format. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Calling Party Transformation Pattern . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New to add a new calling party transformation pattern. Click Find and select an existing pattern. |
| Step 3 | From the Pattern field, enter the pattern that you want to match to the calling party number. Note For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. | Note | For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. |
| Note | For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. |
| Step 4 | Complete the remaining fields in the Calling Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |

| Note | For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Called Party Transformation Pattern . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New , to add a new called party transformation pattern. Click Find and select an existing pattern. |
| Step 3 | From the Pattern field, enter the pattern that you want to match to the called number. |
| Step 4 | Complete the remaining fields in the Called Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Profile . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New , to add a new transformation profile. Click Find and choose a pattern from the resulting list, to modify the settings for an existing transformation profile. The Transformation Profile Configuration window appears. |
| Step 3 | Configure the fields in the Transformation Profile Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |