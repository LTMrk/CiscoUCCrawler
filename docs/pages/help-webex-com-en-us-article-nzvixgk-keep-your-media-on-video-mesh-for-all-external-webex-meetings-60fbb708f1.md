---
doc_id: help-webex-com-en-us-article-nzvixgk-keep-your-media-on-video-mesh-for-all-external-webex-meetings-60fbb708f1
source_url: https://help.webex.com/en-us/article/nzvixgk/Keep-your-media-on-Video-Mesh-for-all-external-Webex-meetings
retrieved_at: 2026-11-02T13:04:06.744795+00:00
---

## Use your Video Mesh for all external Webex meetings

In previous releases, you controlled the use of Video Mesh for meetings only for your internal sites. For meetings that are hosted on external Webex sites, those sites controlled if Video Mesh could cascade to Webex. If an external site didn't allow Video Mesh cascades, your media always used the Webex cloud nodes.

With the Prefer Video Mesh for All External Webex Meetings setting, if your Webex site has available Video Mesh nodes, your media runs through those nodes for meetings on external sites. This table summarizes the behavior for your participants joining Webex meetings:

This setting is off by default, which maintains the behavior from previous releases. In those releases, your Video Mesh didn’t cascade to Webex and your participants joined through the Webex cloud nodes.

In the customer view in https://admin.webex.com , go to Services > Hybrid and click Show all on the Video Mesh card.

Select your Video Mesh cluster in the list and click Edit settings .

Scroll to Prefer Video Mesh for All External Webex Meetings and enable the setting.

Save your change.

| Setting is... | Meeting on internal Webex site with Video Mesh cascades enabled | Meeting on internal Webex site with Video Mesh cascades disabled | Meeting on external Webex site with Video Mesh cascades enabled | Meeting on external Webex site with Video Mesh cascades disabled |
|---|---|---|---|---|
| Enabled | Media uses your Video Mesh nodes. | Media uses cloud nodes. | Media uses your Video Mesh nodes. | Media uses your Video Mesh nodes. |
| Disabled | Media uses your Video Mesh nodes. | Media uses cloud nodes. | Media uses your Video Mesh nodes. | Media uses cloud nodes. |

| 1 | In the customer view in https://admin.webex.com , go to Services > Hybrid and click Show all on the Video Mesh card. |
|---|---|
| 2 | Select your Video Mesh cluster in the list and click Edit settings . |
| 3 | Scroll to Prefer Video Mesh for All External Webex Meetings and enable the setting. |
| 4 | Save your change. |