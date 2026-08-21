---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--d0bc3df9aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_scripting-and-media-routing-guide_12_5/ucce_b_scripting-and-media-routing-guide_12_5_chapter_01100.html
retrieved_at: 2026-08-21T12:03:57.938824+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

Updated: May 26, 2022

Chapter: Utility Nodes

## Chapter: Utility Nodes

# Utility Nodes

## Start Node

The Start node marks the beginning of a script. The Script Editor
                              automatically inserts the Start node when you create a new script; a script
                              must have one and only one Start node.

You do not define any properties for the Start node. However, you can add
                              comments and connection labels:

## Comment Node

Use the Comment node (in the General tab of the Palette) to include a
                              block comment in a script. A block comment provides general documentation
                              for a script or section of a script:

For example, you might add a comment describing the purpose of the script.

You can move and resize the comment box within the script.

## Line Connector Node

Use the Line Connector node (in the General tab of the Palette) to make
                              routing and administrative scripts clear and understandable.

A script can be difficult to understand and the call flow hard
                              to follow if:

The connecting lines between nodes are too long.

The connecting lines go in different directions.

The connecting lines run over other nodes and other connection
                                    lines.

The Line Connector node allows you to break and reconnect lines using one
                              or more of its multiple input connections and single output connection. Any
                              request coming into this node (on any one of the multiple inputs) goes to
                              the single output connection of the line connector node.

For the Line Connector node, you define the connection labels:

| Note | If you choose the Auto-Size Height option, you cannot adjust the height of
                                       the comment. |
|---|---|