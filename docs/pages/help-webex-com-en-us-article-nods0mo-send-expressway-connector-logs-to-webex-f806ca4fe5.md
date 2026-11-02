---
doc_id: help-webex-com-en-us-article-nods0mo-send-expressway-connector-logs-to-webex-f806ca4fe5
source_url: https://help.webex.com/en-us/article/nods0mo/Send-Expressway-connector-logs-to-Webex
retrieved_at: 2026-11-02T13:14:19.443311+00:00
---

Before you begin

To see this logging option, you must have a supported version of Expressway with Hybrid Services enabled. See this document for more information.

The Expressway must have port access for HTTPS or secure web sockets outbound to TCP port 443 (secure) for the Webex storage URLs. Find the Webex storage URLs and other network requirements here .

On an Expressway-C node or cluster, go to Applications > Hybrid Services > Connector Logging , and then click Send .

In the dialogue box that appears, click OK . To search for specific logs:

- Use Generated Search Key for a cluster.

- Use Serial Number for a node.

A notification of the Generated Search Key for the logs appears and the logs are uploaded to the cloud.

Choose one:

- If you want to open a new ticket at this point, open Control Hub at https://admin.webex.com , click your username, and then choose Feedback . Provide the generated search key or serial number to support.

- If you're already working with support, provide them with the generated search key or serial number.

If there's a network issue, you'll see an error appear in the Expressway interface. In a cluster scenario, even if there's a network issue from the main node, the logs send from the other remote nodes but not from the node on which the command was initiated.

| 1 | On an Expressway-C node or cluster, go to Applications > Hybrid Services > Connector Logging , and then click Send . |
|---|---|
| 2 | In the dialogue box that appears, click OK . To search for specific logs: Use Generated Search Key for a cluster. Use Serial Number for a node. A notification of the Generated Search Key for the logs appears and the logs are uploaded to the cloud. |
| 3 | Choose one: If you want to open a new ticket at this point, open Control Hub at https://admin.webex.com , click your username, and then choose Feedback . Provide the generated search key or serial number to support. If you're already working with support, provide them with the generated search key or serial number. |