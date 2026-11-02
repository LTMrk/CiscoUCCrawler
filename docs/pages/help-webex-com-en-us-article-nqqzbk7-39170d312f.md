---
doc_id: help-webex-com-en-us-article-nqqzbk7-39170d312f
source_url: https://help.webex.com/en-us/article/nqqzbk7
retrieved_at: 2026-11-02T13:01:16.107716+00:00
---

## Configure SIP Trunk Security Profile for Trunk to Local Gateway

In cases where Local Gateway and PSTN gateway reside on the same device, Unified CM must be enabled to differentiate between two different traffic types (calls from Webex and from the PSTN) that are originating from the same device and apply differentiated class of service to these call types. This differentiated call treatment is achieved by provisioning two trunks between Unified CM and the combined local gateway and PSTN gateway device which requires different SIP listening ports for the two trunks.

Create a dedicated SIP Trunk Security Profile for the Local Gateway trunk with the following settings:

## Configure SIP Profile for the Local Gateway Trunk

Create a dedicated SIP Profile for the Local Gateway trunk with the following settings:

## Create a Calling Search Space for Calls From Webex

Create a calling search space for calls originating from Webex with the following settings:

DN (+E.164 directory numbers)

ESN (abbreviated inter-site dialling)

PSTNInternational (PSTN access)

onNetRemote (GDPR learned destinations)

The last partition onNetRemote is only used in a multi-cluster environment where routing information is exchanged between Unified CM clusters using Intercluster Lookup Service (ILS) or Global Dialplan Replication (GDPR).

## Configure a SIP Trunk To and From Webex

Create a SIP trunk for the calls to and from Webex via the Local Gateway with the following settings:

## Configure Route Group for Webex

Create a route group with the following settings:

## Configure Route List for Webex

Create a route list with the following settings:

## Create a Partition for Webex Destinations

Create a partition for the Webex destinations with the following settings:

What to do next

## What to do next

Make sure to add this partition to all calling search spaces that should have access to Webex destinations. You must add this partition specifically to the calling search space that is used as the inbound calling search space on PSTN trunks, so that calls from the PSTN to Webex can be routed.

## Configure Route Patterns for Webex Destinations

Configure route patterns for each DID range on Webex with the following settings:

## Configure Abbreviated Intersite Dialing Normalization for Webex

If abbreviated inter-site dialing is required to Webex, then configure dialing normalization patterns for each ESN range on Webex with the following settings:

| Create a dedicated SIP Trunk Security Profile for the Local Gateway trunk with the following settings: Setting Value Name Unique Name, such as Webex Description Meaningful description, such as Webex SIP Trunk Security Profile Incoming Port Needs to match port used in local gateway config for traffic to/from Webex: 5065 | Setting | Value |  | Name | Unique Name, such as Webex | Description | Meaningful description, such as Webex SIP Trunk Security Profile | Incoming Port | Needs to match port used in local gateway config for traffic to/from Webex: 5065 |
|---|---|---|---|---|---|---|---|---|---|
| Setting | Value |
|  |
| Name | Unique Name, such as Webex |
| Description | Meaningful description, such as Webex SIP Trunk Security Profile |
| Incoming Port | Needs to match port used in local gateway config for traffic to/from Webex: 5065 |

| Setting | Value |
|---|---|
|  |
| Name | Unique Name, such as Webex |
| Description | Meaningful description, such as Webex SIP Trunk Security Profile |
| Incoming Port | Needs to match port used in local gateway config for traffic to/from Webex: 5065 |

| Create a dedicated SIP Profile for the Local Gateway trunk with the following settings: Setting Value Name Unique Name, such as Webex Description Meaningful description, such as Webex SIP Profile Enable OPTIONS Ping to monitor destination status for Trunks with Service Type “None (Default)” Checked | Setting | Value |  | Name | Unique Name, such as Webex | Description | Meaningful description, such as Webex SIP Profile | Enable OPTIONS Ping to monitor destination status for Trunks with Service Type “None (Default)” | Checked |
|---|---|---|---|---|---|---|---|---|---|
| Setting | Value |
|  |
| Name | Unique Name, such as Webex |
| Description | Meaningful description, such as Webex SIP Profile |
| Enable OPTIONS Ping to monitor destination status for Trunks with Service Type “None (Default)” | Checked |

| Setting | Value |
|---|---|
|  |
| Name | Unique Name, such as Webex |
| Description | Meaningful description, such as Webex SIP Profile |
| Enable OPTIONS Ping to monitor destination status for Trunks with Service Type “None (Default)” | Checked |

| Create a calling search space for calls originating from Webex with the following settings: Setting Value Name Unique Name, such as Webex Description Meaningful description, such as Webex Calling Search Space Selected Partitions DN (+E.164 directory numbers) ESN (abbreviated inter-site dialling) PSTNInternational (PSTN access) onNetRemote (GDPR learned destinations) The last partition onNetRemote is only used in a multi-cluster environment where routing information is exchanged between Unified CM clusters using Intercluster Lookup Service (ILS) or Global Dialplan Replication (GDPR). | Setting | Value |  | Name | Unique Name, such as Webex | Description | Meaningful description, such as Webex Calling Search Space | Selected Partitions | DN (+E.164 directory numbers) ESN (abbreviated inter-site dialling) PSTNInternational (PSTN access) onNetRemote (GDPR learned destinations) |  | The last partition onNetRemote is only used in a multi-cluster environment where routing information is exchanged between Unified CM clusters using Intercluster Lookup Service (ILS) or Global Dialplan Replication (GDPR). |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Setting | Value |
|  |
| Name | Unique Name, such as Webex |
| Description | Meaningful description, such as Webex Calling Search Space |
| Selected Partitions | DN (+E.164 directory numbers) ESN (abbreviated inter-site dialling) PSTNInternational (PSTN access) onNetRemote (GDPR learned destinations) |
|  | The last partition onNetRemote is only used in a multi-cluster environment where routing information is exchanged between Unified CM clusters using Intercluster Lookup Service (ILS) or Global Dialplan Replication (GDPR). |

| Setting | Value |
|---|---|
|  |
| Name | Unique Name, such as Webex |
| Description | Meaningful description, such as Webex Calling Search Space |
| Selected Partitions | DN (+E.164 directory numbers) ESN (abbreviated inter-site dialling) PSTNInternational (PSTN access) onNetRemote (GDPR learned destinations) |

|  | The last partition onNetRemote is only used in a multi-cluster environment where routing information is exchanged between Unified CM clusters using Intercluster Lookup Service (ILS) or Global Dialplan Replication (GDPR). |
|---|---|

| Create a SIP trunk for the calls to and from Webex via the Local Gateway with the following settings: Setting Value Device Information DeviceName A unique name, such as Webex Description Meaningful description, such as Webex SIP Trunk Run On All Active Unified CM Nodes Checked Inbound Calls Calling Search Space The previously defined calling search space: Webex AAR Calling Search Space A calling search space with only access to PSTN route patterns: PSTNReroute SIP Information Destination Address IP address of the Local Gateway CUBE Destination Port 5060 SIP Trunk Security Profile Previously defined: Webex SIP Profile Previously defined: Webex | Setting | Value | Device Information | DeviceName | A unique name, such as Webex | Description | Meaningful description, such as Webex SIP Trunk | Run On All Active Unified CM Nodes | Checked | Inbound Calls | Calling Search Space | The previously defined calling search space: Webex | AAR Calling Search Space | A calling search space with only access to PSTN route patterns: PSTNReroute | SIP Information | Destination Address | IP address of the Local Gateway CUBE | Destination Port | 5060 | SIP Trunk Security Profile | Previously defined: Webex | SIP Profile | Previously defined: Webex |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Setting | Value |
| Device Information |
| DeviceName | A unique name, such as Webex |
| Description | Meaningful description, such as Webex SIP Trunk |
| Run On All Active Unified CM Nodes | Checked |
| Inbound Calls |
| Calling Search Space | The previously defined calling search space: Webex |
| AAR Calling Search Space | A calling search space with only access to PSTN route patterns: PSTNReroute |
| SIP Information |
| Destination Address | IP address of the Local Gateway CUBE |
| Destination Port | 5060 |
| SIP Trunk Security Profile | Previously defined: Webex |
| SIP Profile | Previously defined: Webex |

| Setting | Value |
|---|---|
| Device Information |
| DeviceName | A unique name, such as Webex |
| Description | Meaningful description, such as Webex SIP Trunk |
| Run On All Active Unified CM Nodes | Checked |
| Inbound Calls |
| Calling Search Space | The previously defined calling search space: Webex |
| AAR Calling Search Space | A calling search space with only access to PSTN route patterns: PSTNReroute |
| SIP Information |
| Destination Address | IP address of the Local Gateway CUBE |
| Destination Port | 5060 |
| SIP Trunk Security Profile | Previously defined: Webex |
| SIP Profile | Previously defined: Webex |

| Create a route group with the following settings: Setting Value Route Group Information Route Group Name A unique name, such as Webex Selected Devices The previously configured SIP trunk: Webex | Setting | Value | Route Group Information | Route Group Name | A unique name, such as Webex | Selected Devices | The previously configured SIP trunk: Webex |
|---|---|---|---|---|---|---|---|
| Setting | Value |
| Route Group Information |
| Route Group Name | A unique name, such as Webex |
| Selected Devices | The previously configured SIP trunk: Webex |

| Setting | Value |
|---|---|
| Route Group Information |
| Route Group Name | A unique name, such as Webex |
| Selected Devices | The previously configured SIP trunk: Webex |

| Create a route list with the following settings: Setting Value Route List Information Name A unique name, such as RL_Webex Description Meaningful description, such as Route list for Webex Run On All Active Unified CM Nodes Checked Route List Member Information Selected Groups Only the previously defined route group: Webex | Setting | Value | Route List Information | Name | A unique name, such as RL_Webex | Description | Meaningful description, such as Route list for Webex | Run On All Active Unified CM Nodes | Checked | Route List Member Information | Selected Groups | Only the previously defined route group: Webex |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Setting | Value |
| Route List Information |
| Name | A unique name, such as RL_Webex |
| Description | Meaningful description, such as Route list for Webex |
| Run On All Active Unified CM Nodes | Checked |
| Route List Member Information |
| Selected Groups | Only the previously defined route group: Webex |

| Setting | Value |
|---|---|
| Route List Information |
| Name | A unique name, such as RL_Webex |
| Description | Meaningful description, such as Route list for Webex |
| Run On All Active Unified CM Nodes | Checked |
| Route List Member Information |
| Selected Groups | Only the previously defined route group: Webex |

| Create a partition for the Webex destinations with the following settings: Setting Value Route List Information Name Unique name, such as Webex Description Meaningful description, such as Webex Partition | Setting | Value | Route List Information | Name | Unique name, such as Webex | Description | Meaningful description, such as Webex Partition |
|---|---|---|---|---|---|---|---|
| Setting | Value |
| Route List Information |
| Name | Unique name, such as Webex |
| Description | Meaningful description, such as Webex Partition |

| Setting | Value |
|---|---|
| Route List Information |
| Name | Unique name, such as Webex |
| Description | Meaningful description, such as Webex Partition |

| Configure route patterns for each DID range on Webex with the following settings: Setting Value Route Pattern Full +E.164 pattern for the DID range in Webex with the leading “\”. For example: \+140855501XX Route Partition Webex Gateway/Route List RL_Webex Urgent Priority Checked | Setting | Value |  | Route Pattern | Full +E.164 pattern for the DID range in Webex with the leading “\”. For example: \+140855501XX | Route Partition | Webex | Gateway/Route List | RL_Webex | Urgent Priority | Checked |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Setting | Value |
|  |
| Route Pattern | Full +E.164 pattern for the DID range in Webex with the leading “\”. For example: \+140855501XX |
| Route Partition | Webex |
| Gateway/Route List | RL_Webex |
| Urgent Priority | Checked |

| Setting | Value |
|---|---|
|  |
| Route Pattern | Full +E.164 pattern for the DID range in Webex with the leading “\”. For example: \+140855501XX |
| Route Partition | Webex |
| Gateway/Route List | RL_Webex |
| Urgent Priority | Checked |

| If abbreviated inter-site dialing is required to Webex, then configure dialing normalization patterns for each ESN range on Webex with the following settings: Setting Value Translation Pattern ESN pattern for the ESN range in Webex. For example: 80121XX Partition Webex Description Meaningful description, such as Webex Normalization Pattern Use Originator's Calling Search Space Checked Urgent Priority Checked Do Not Wait For Interdigit Timeout On Subsequent Hops Checked Called Party Transformation Mask Mask to normalize the number to +E.164. For example: + 140855501XX | Setting | Value |  | Translation Pattern | ESN pattern for the ESN range in Webex. For example: 80121XX | Partition | Webex | Description | Meaningful description, such as Webex Normalization Pattern | Use Originator's Calling Search Space | Checked | Urgent Priority | Checked | Do Not Wait For Interdigit Timeout On Subsequent Hops | Checked | Called Party Transformation Mask | Mask to normalize the number to +E.164. For example: + 140855501XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Setting | Value |
|  |
| Translation Pattern | ESN pattern for the ESN range in Webex. For example: 80121XX |
| Partition | Webex |
| Description | Meaningful description, such as Webex Normalization Pattern |
| Use Originator's Calling Search Space | Checked |
| Urgent Priority | Checked |
| Do Not Wait For Interdigit Timeout On Subsequent Hops | Checked |
| Called Party Transformation Mask | Mask to normalize the number to +E.164. For example: + 140855501XX |

| Setting | Value |
|---|---|
|  |
| Translation Pattern | ESN pattern for the ESN range in Webex. For example: 80121XX |
| Partition | Webex |
| Description | Meaningful description, such as Webex Normalization Pattern |
| Use Originator's Calling Search Space | Checked |
| Urgent Priority | Checked |
| Do Not Wait For Interdigit Timeout On Subsequent Hops | Checked |
| Called Party Transformation Mask | Mask to normalize the number to +E.164. For example: + 140855501XX |