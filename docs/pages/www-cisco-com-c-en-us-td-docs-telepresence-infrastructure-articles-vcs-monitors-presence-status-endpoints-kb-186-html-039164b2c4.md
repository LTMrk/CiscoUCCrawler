---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-infrastructure-articles-vcs-monitors-presence-status-endpoints-kb-186-html-039164b2c4
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/infrastructure/articles/vcs_monitors_presence_status_endpoints_kb_186.html
retrieved_at: 2026-08-21T12:30:42.644638+00:00
---

Cisco TelePresence Video Communication Server (VCS) How the Cisco VCS monitors the Presence status of endpoints

# Cisco TelePresence Video Communication Server (VCS)

## How the Cisco VCS monitors the Presence status of endpoints

### How the Cisco TelePresence Video Communication Server (Cisco VCS) monitors the Presence status of endpoints

When the Cisco VCS is sent a registration , de-registration , in-call or call-ended message by the endpoint, the Cisco VCS Presence User Agent (PUA) updates the endpoint's presence status immediately.

However, there are two situations when changes are not updated immediately:

- If the endpoint goes offline without first reporting a status change to the Cisco VCS (for example, if it is powered down or unplugged), the PUA will only change the endpoint's status to off-line when it fails to receive the next registration refresh from the endpoint.

- If the PUA is enabled after the endpoint has already registered, it will only report the endpoint as on-line when it receives the next registration refresh from the endpoint.

The frequency of registration refreshes is configured by the Cisco VCS as follows:

- For SIP endpoints, by the Registration expire delta setting ( VCS configuration > Protocols > SIP > Configuration ). The default is 60 seconds.

- For H.323 endpoints, by the Time to live setting ( VCS configuration > Protocols > H.323 ). The default is 30 minutes.

You can change either or both of these settings to reduce the time taken for the PUA to update the endpoint's status.

#### This article applies to the following products:

- Cisco Video Communication Server

|  | How the Cisco TelePresence Video Communication Server (Cisco VCS) monitors the Presence status of endpoints When the Cisco VCS is sent a registration , de-registration , in-call or call-ended message by the endpoint, the Cisco VCS Presence User Agent (PUA) updates the endpoint's presence status immediately. However, there are two situations when changes are not updated immediately: If the endpoint goes offline without first reporting a status change to the Cisco VCS (for example, if it is powered down or unplugged), the PUA will only change the endpoint's status to off-line when it fails to receive the next registration refresh from the endpoint. If the PUA is enabled after the endpoint has already registered, it will only report the endpoint as on-line when it receives the next registration refresh from the endpoint. The frequency of registration refreshes is configured by the Cisco VCS as follows: For SIP endpoints, by the Registration expire delta setting ( VCS configuration > Protocols > SIP > Configuration ). The default is 60 seconds. For H.323 endpoints, by the Time to live setting ( VCS configuration > Protocols > H.323 ). The default is 30 minutes. You can change either or both of these settings to reduce the time taken for the PUA to update the endpoint's status. This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_186 | How the Cisco TelePresence Video Communication Server (Cisco VCS) monitors the Presence status of endpoints When the Cisco VCS is sent a registration , de-registration , in-call or call-ended message by the endpoint, the Cisco VCS Presence User Agent (PUA) updates the endpoint's presence status immediately. However, there are two situations when changes are not updated immediately: If the endpoint goes offline without first reporting a status change to the Cisco VCS (for example, if it is powered down or unplugged), the PUA will only change the endpoint's status to off-line when it fails to receive the next registration refresh from the endpoint. If the PUA is enabled after the endpoint has already registered, it will only report the endpoint as on-line when it receives the next registration refresh from the endpoint. The frequency of registration refreshes is configured by the Cisco VCS as follows: For SIP endpoints, by the Registration expire delta setting ( VCS configuration > Protocols > SIP > Configuration ). The default is 60 seconds. For H.323 endpoints, by the Time to live setting ( VCS configuration > Protocols > H.323 ). The default is 30 minutes. You can change either or both of these settings to reduce the time taken for the PUA to update the endpoint's status. This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_186 | June 16th, 2011 | TAA_KB_186 |  |
|---|---|---|---|---|---|
| How the Cisco TelePresence Video Communication Server (Cisco VCS) monitors the Presence status of endpoints When the Cisco VCS is sent a registration , de-registration , in-call or call-ended message by the endpoint, the Cisco VCS Presence User Agent (PUA) updates the endpoint's presence status immediately. However, there are two situations when changes are not updated immediately: If the endpoint goes offline without first reporting a status change to the Cisco VCS (for example, if it is powered down or unplugged), the PUA will only change the endpoint's status to off-line when it fails to receive the next registration refresh from the endpoint. If the PUA is enabled after the endpoint has already registered, it will only report the endpoint as on-line when it receives the next registration refresh from the endpoint. The frequency of registration refreshes is configured by the Cisco VCS as follows: For SIP endpoints, by the Registration expire delta setting ( VCS configuration > Protocols > SIP > Configuration ). The default is 60 seconds. For H.323 endpoints, by the Time to live setting ( VCS configuration > Protocols > H.323 ). The default is 30 minutes. You can change either or both of these settings to reduce the time taken for the PUA to update the endpoint's status. This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_186 | June 16th, 2011 | TAA_KB_186 |  |
| June 16th, 2011 | TAA_KB_186 |

| How the Cisco TelePresence Video Communication Server (Cisco VCS) monitors the Presence status of endpoints When the Cisco VCS is sent a registration , de-registration , in-call or call-ended message by the endpoint, the Cisco VCS Presence User Agent (PUA) updates the endpoint's presence status immediately. However, there are two situations when changes are not updated immediately: If the endpoint goes offline without first reporting a status change to the Cisco VCS (for example, if it is powered down or unplugged), the PUA will only change the endpoint's status to off-line when it fails to receive the next registration refresh from the endpoint. If the PUA is enabled after the endpoint has already registered, it will only report the endpoint as on-line when it receives the next registration refresh from the endpoint. The frequency of registration refreshes is configured by the Cisco VCS as follows: For SIP endpoints, by the Registration expire delta setting ( VCS configuration > Protocols > SIP > Configuration ). The default is 60 seconds. For H.323 endpoints, by the Time to live setting ( VCS configuration > Protocols > H.323 ). The default is 30 minutes. You can change either or both of these settings to reduce the time taken for the PUA to update the endpoint's status. This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_186 | June 16th, 2011 | TAA_KB_186 |  |
|---|---|---|---|
| June 16th, 2011 | TAA_KB_186 |

| June 16th, 2011 | TAA_KB_186 |
|---|---|