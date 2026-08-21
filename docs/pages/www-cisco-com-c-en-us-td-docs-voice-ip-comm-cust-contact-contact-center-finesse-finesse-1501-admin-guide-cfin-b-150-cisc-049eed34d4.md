---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-admin-guide-cfin-b-150-cisc-049eed34d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/admin/guide/cfin_b_150_cisco-finesse-administration-guide/cfin_m_150_manage-connected-agents.html
retrieved_at: 2026-08-21T12:04:52.191326+00:00
---

Cisco Finesse Administration Guide, Release 15.0(1)

# Cisco Finesse Administration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Manage Connected Agents

## Chapter: Manage Connected Agents

- Manage Connected Agents

- Connected Agents

# Manage Connected Agents

## Connected Agents

Use the Connected Agents gadget on the Connected Agents tab to view the list of agents currently signed in to Cisco Finesse

### Actions on the Connected Agents Gadget

You can use this gadget to determine which agents are signed in to the Publisher Side or the Subscriber Side. You can use
                              this gadget also to filter the client types and identify the client type through which an agent has logged in. The client
                              types can be Finesse Desktop, Finesse IP Phone, and Custom Desktop.

The list of signed-in agents is displayed in the form of a table, the Connected Agents table.

You can search the Connected Agents table for certain entries, sort the table, or refresh the table to view the latest data.
                              The number of agents signed in to the Publisher Side and the Subscriber Side are displayed in the gadget (above the table).

The columns of the Connected Agents table are displayed below:

Column

Explanation

Agent Name

The first and last name of an agent.

Username

The Agent ID or username required to sign in to Cisco Finesse.

Extension

The extension number of the agent.

Team

The team the agent belongs to.

Connected Time

The total duration (in hh:mm:ss) for which the agent has been logged in.

Connected Side

Publisher/Subscriber/Both Sides.

Finesse Host

The Finesse host through which the agent is connected.

Search : Searches for the entered text across all columns of the Connected Agents table.

Sort : Sorts the column values of the Connected Agents table in ascending or descending order.

Filter : Filters agents connected to Both Sides, the Publisher side, or the Subscriber side.

The default selection for this drop-down box is Both Sides.

Refresh : Refreshes the Connected Agents table. When the Refresh button is clicked, a new REST API call is made to both the publisher
                                    and subscriber servers to get the latest information about the signed-in agents.

The time at which the agent information was last fetched from the server is displayed beside the Refresh button (For example,
                                    Updated 45 minutes ago).

The Connected Agents gadget may display an error message stating that Connected Agents are not listed due to network error. Check the logs for more details . This error can occur for various reasons, including when the Finesse subscriber node is unavailable or undeployed.

| Column | Explanation |
|---|---|
| Agent Name | The first and last name of an agent. |
| Username | The Agent ID or username required to sign in to Cisco Finesse. |
| Extension | The extension number of the agent. |
| Team | The team the agent belongs to. |
| Connected Time | The total duration (in hh:mm:ss) for which the agent has been logged in. |
| Connected Side | Publisher/Subscriber/Both Sides. |
| Finesse Host | The Finesse host through which the agent is connected. |

| Note | The Connected Agents gadget may display an error message stating that Connected Agents are not listed due to network error. Check the logs for more details . This error can occur for various reasons, including when the Finesse subscriber node is unavailable or undeployed. |
|---|---|