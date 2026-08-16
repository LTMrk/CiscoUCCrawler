---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-cucm-b-feature-configuration-guide-for-cisco14su2-cucm-b-fe-8a95fbd2a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/cucm_b_feature-configuration-guide-for-cisco14su2/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_01000100.html
retrieved_at: 2026-08-16T16:26:51.338535+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: May 7, 2026

Chapter: Configure SDP Transparency Profiles

## Chapter: Configure SDP Transparency Profiles

# Configure SDP Transparency Profiles

## SDP Transparency Profile Overview

SDP Transparency Profiles contain a set of rules for declarative SDP attributes that allow the system to pass through declarative
                              attributes that are not natively supported by Unified Communications Manager from the ingress to the egress call leg. Without
                              an SDP transparency profile, Unified Communications Manager drops non-supported SDP attributes.

You can configure SDP transparency profiles with multiple rules and apply them to SIP devices via the SIP profile. In order
                              for the SDP transparency profile to be applied, both call legs must be SIP. You can configure the following types of rules
                              for SDP attributes:

Property—If a rule is configured for a property attribute, Unified Communications Manager passes through the SDP attribute
                                    unless the attribute has a value.

- Any Value—If a rule is configured for any value, the SDP attribute gets passed through so long as it has a value that consists
                                 of at least one non-white space character.

- Value From List—If a rule is configured using this option, the SDP attribute gets passed through so long as it matches one
                                 of the specified values. You can configure up to five possible values

## SDP Transparency Profile Restrictions

The following restrictions apply to SDP transparency profiles. If any of these situations occur on the egress call leg, Cisco
                              Unified Communications Manager will not pass through the declarative SDP attribute:

One or more Media Termination Points (MTPs) or Trusted Relay Points (TRPs) that do not support passthrough are allocated

The Media Termination Point Required check box is checked for the SIP trunk

A transcoder is being used

RSVP is being used

The ingress call leg is using Delayed Offer while the egress call leg is using Early Offer

The media line has been rejected (port=0)

Either call leg is using a protocol other than SIP

## SDP Transparency Profile Prerequisites

If you plan to deploy any third-party SIP products, make sure that you understand how the products implement the Session Description
                           Protocol (SDP).

## Configure SDP Transparency Profile

Configure a customized SDP Transparency Profile with a set of rules for declarative SDP attributes that are not natively supported
                              by Cisco Unified Communications Manager.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > SDP Transparency Profile .

Step 2

Click Add New .

Step 3

Enter a Name and Description .

Step 4

In the Attribute Information pane, create the rules for the SDP attributes that you want to pass through:

- To pass through a property attribute, enter the attribute in the Name text box (for example, a=recvonly) and from the Type drop-down list, select Property .

- To pass through a value attribute, enter the attribute in the Name text box (for example, a=rtpmap), and select Any Value from the Type drop-down list box.

- To pass through a value attribute with any of up to five values, enter the attribute in the Name field (for example, a=rtpmap) and select Any Value from the Type drop-down list. In the resulting Value text box, enter the value of the attribute. You can click + to add up to five possible values for this attribute.

Step 5

Click the (+) to create new lines where you can enter additional SDP attributes for this transparency profile.

Step 6

Click Save .

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > SDP Transparency Profile . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name and Description . |
| Step 4 | In the Attribute Information pane, create the rules for the SDP attributes that you want to pass through: To pass through a property attribute, enter the attribute in the Name text box (for example, a=recvonly) and from the Type drop-down list, select Property . To pass through a value attribute, enter the attribute in the Name text box (for example, a=rtpmap), and select Any Value from the Type drop-down list box. To pass through a value attribute with any of up to five values, enter the attribute in the Name field (for example, a=rtpmap) and select Any Value from the Type drop-down list. In the resulting Value text box, enter the value of the attribute. You can click + to add up to five possible values for this attribute. |
| Step 5 | Click the (+) to create new lines where you can enter additional SDP attributes for this transparency profile. |
| Step 6 | Click Save . Note You must apply this profile to a SIP Profile so that the devices that use the SIP Profile can use the SDP Transparency Profile. | Note | You must apply this profile to a SIP Profile so that the devices that use the SIP Profile can use the SDP Transparency Profile. |
| Note | You must apply this profile to a SIP Profile so that the devices that use the SIP Profile can use the SDP Transparency Profile. |

| Note | You must apply this profile to a SIP Profile so that the devices that use the SIP Profile can use the SDP Transparency Profile. |
|---|---|