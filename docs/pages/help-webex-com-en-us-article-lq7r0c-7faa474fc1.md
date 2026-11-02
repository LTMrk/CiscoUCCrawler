---
doc_id: help-webex-com-en-us-article-lq7r0c-7faa474fc1
source_url: https://help.webex.com/en-us/article/lq7r0c
retrieved_at: 2026-11-02T13:16:23.972325+00:00
---

Applies to Expressway-based Hybrid Calendar Service and Hybrid Call Service, with clustered connector host Expressways.

If you are using an unclustered Expressway as a connector host, you can upgrade the Expressway using the standard Expressway upgrade procedure. You can find that in the release notes for your version at the Cisco Expressway Series Release Notes page .

If your connector host is a cluster of Expressway nodes, proceed as follows:

Sign in to Control Hub and find the connector host Expressways.

Put the primary node into Maintenance Mode.

See https://help.webex.com/article/nxep7tb for detail.

The users allocated to that connector host node are redistributed to other nodes in the cluster.

DO NOT use the Expressway's UI to enable maintenance mode, because the connectors ignore that configuration. When you correctly set maintenance mode, using Control Hub, then a banner on the Expressway's connector management page shows that Cloud Maintenance Mode is active.

Switch to the Expressway UI, and upgrade the node using the standard procedure for Expressway.

See the release notes for your version at the Cisco Expressway Series Release Notes page .

Return to Control Hub after the Expressway has finished its upgrade and has restarted.

You may see clustering alarms on Expressway or Control Hub. These should clear after you complete the upgrade across the cluster.

Return the primary node to normal service (disable maintenance mode using Control Hub).

Enable maintenance mode on a subordinate node in the same cluster.

Upgrade that node using the Expressway UI.

Return that node to service by disabling maintenance mode in Control Hub.

Continue in this pattern until the whole cluster is upgraded.

Clustering alarms should clear soon after all nodes are upgraded.

| 1 | Sign in to Control Hub and find the connector host Expressways. |
|---|---|
| 2 | Put the primary node into Maintenance Mode. See https://help.webex.com/article/nxep7tb for detail. The users allocated to that connector host node are redistributed to other nodes in the cluster. DO NOT use the Expressway's UI to enable maintenance mode, because the connectors ignore that configuration. When you correctly set maintenance mode, using Control Hub, then a banner on the Expressway's connector management page shows that Cloud Maintenance Mode is active. |
| 3 | Switch to the Expressway UI, and upgrade the node using the standard procedure for Expressway. See the release notes for your version at the Cisco Expressway Series Release Notes page . |
| 4 | Return to Control Hub after the Expressway has finished its upgrade and has restarted. You may see clustering alarms on Expressway or Control Hub. These should clear after you complete the upgrade across the cluster. |
| 5 | Return the primary node to normal service (disable maintenance mode using Control Hub). |
| 6 | Enable maintenance mode on a subordinate node in the same cluster. |
| 7 | Upgrade that node using the Expressway UI. |
| 8 | Return that node to service by disabling maintenance mode in Control Hub. |
| 9 | Continue in this pattern until the whole cluster is upgraded. Clustering alarms should clear soon after all nodes are upgraded. |