---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-operation-guide-chcs-b-hcs-smart-licensing-operational-318046b860
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/Operation_Guide/chcs_b_hcs-smart-licensing-operational-guide/chcs_b_hcs-smart-licensing-operational-guide_chapter_0100.html
retrieved_at: 2026-09-01T20:56:13.770510+00:00
---

Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

# Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

Updated: April 23, 2020

Chapter: Deployment Scenarios

## Chapter: Deployment Scenarios

- Deployment Scenarios

- Scenario: To Migrate On-Premise UC with Dual License Entitlement to HCS

- Scenario: To Migrate Flex Hosted (EA/NU) License

# Deployment Scenarios

## Scenario: To Migrate On-Premise UC with Dual License Entitlement to HCS

Use this workflow to migrate from Dual Entitelment On-premise Unified Communication applications to HCS 12.5 Smart Licensing:

Action

Description

Log in to Cisco Commerce(CCW) and order HCS license.

For more information about operational licenses, see Configuring Operational Licenses

Create a smart account and virtual account

Create a Smart Account in CSSM or Satellite . You can also get access to an existing smart account.

Create Virtual Account

For more information about the one time setup activities, see Initial One Time Setup in CSSM for Smart Licensing and Initial One Time Setup in CSSM on-prem for Smart Licensing

Setup Transport Mode

Setup the transport mode in HCM-F to connect HCM-F and UC applications to CSSM.

Provision smart account in HCM-F

Provision the credentials and Smart Account with HCM-F.

HCM-F extracts smart account, local account, and virtual account-related information from CSSM and Satellite .

Creates product registration token to register UC Applications in CSSM and Satellite .

Provide the transport mode in HCM-F to connect HCM-F and UC applications to CSSM and Satellite.

You can autoregister the clusters to ordered virtual account using HCM-F.

Activate Smart Licensing for Clusters (Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder)

You can assign and unassign clusters to CSSM and Satellite using HCM-F.

If autoregistration is enabled, the clusters are automatically assigned to the ordered virtual account. You do not have to
                                       manually assign the clusters.

For any failed cluster registration, refer to the Cluster Summary page.

Service Inventory and HLM report generated

HCM-F generates the reports to view the licenses from CSSM and Satellite at virtual account-level, or customer-level. For more information on reports, see Smart Licensing Reports

Licensing Dashboard

HCM-F provides a view of the licenses at virtual account-level and customer-level.

HCM-F sync with CSSM and Satellite

HCM-F provides on-demand and automatic sync to CSSM and Satellite . You can trigger the sync from HCM-F, then HCM-F pulls the virtual account and smart account details from CSSM or Satellite and refresh the tokens, if needed.

You can sync smart accounts and virtual accounts either manually or automatically. HCM-F periodically syncs with CSSM and Satellite every 8 24 hours.

For more information on manual sync, see Perform Manual Sync in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide .

## Scenario: To Migrate Flex Hosted (EA/NU) License

Action

Description

Log in to Cisco Commerce(CCW) and order HCS licenses.

For more information about operational licenses, see Configuring Operational Licenses

Create a smart account and virtual account

Create a Smart Account in CSSM or Satellite . You can also get access to an existing smart account.

Create Virtual Account

For more information about the one time setup activities, see Initial One Time Setup in CSSM for Smart Licensing and Initial One Time Setup in CSSM on-prem for Smart Licensing

Upgrade HCM-F to 12.5 version

Provision the Smart account with client credentials that includes Client ID and Client Secret in HCM-F. For more information,
                                       see HCM-F 12.5 Upgrade Guidelines

Setup Transport Mode

Setup the transport mode in HCM-F to connect HCM-F and UC applications to CSSM.

Provision smart account in HCM-F

Provision the credentials and Smart Account with HCM-F.

HCM-F extracts smart account, local account, and virtual account-related information from CSSM and Satellite .

Creates product registration token to register UC Applications in CSSM and Satellite .

Provide the transport mode in HCM-F to connect HCM-F and UC applications to CSSM and Satellite.

You can autoregister the clusters to ordered virtual account using HCM-F.

Activate Smart Licensing for Clusters (Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder)

You can assign and unassign clusters to CSSM and Satellite using HCM-F.

If autoregistration is enabled, the clusters are automatically assigned to the ordered virtual account. You do not have to
                                       manually assign the clusters.

Cluster Sumary

For any failed cluster registration, refer to the Cluster Summary page.

Service Inventory and HLM report generated

HCM-F generates the reports to view the licenses from CSSM and Satellite at virtual account-level, or customer-level. For more information on reports, see Smart Licensing Reports

Licensing Dashboard

HCM-F provides a view of the licenses at virtual account-level and customer-level.

HCM-F sync with CSSM and Satellite

HCM-F provides on-demand and automatic sync to CSSM and Satellite . You can trigger the sync from HCM-F, then HCM-F pulls the virtual account and smart account details from CSSM or Satellite and refresh the tokens, if needed.

You can sync smart accounts and virtual accounts either manually or automatically. HCM-F periodically syncs with CSSM and Satellite every 8 24 hours.

For more information on manual sync, see Perform Manual Sync in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide .

| Action | Description |
|---|---|
| Log in to Cisco Commerce(CCW) and order HCS license. | For more information about operational licenses, see Configuring Operational Licenses |
| Create a smart account and virtual account | Create a Smart Account in CSSM or Satellite . You can also get access to an existing smart account. Create Virtual Account For more information about the one time setup activities, see Initial One Time Setup in CSSM for Smart Licensing and Initial One Time Setup in CSSM on-prem for Smart Licensing |
| Setup Transport Mode | Setup the transport mode in HCM-F to connect HCM-F and UC applications to CSSM. For more information, see Set Transport Mode . |
| Provision smart account in HCM-F | Provision the credentials and Smart Account with HCM-F. HCM-F extracts smart account, local account, and virtual account-related information from CSSM and Satellite . Creates product registration token to register UC Applications in CSSM and Satellite . Provide the transport mode in HCM-F to connect HCM-F and UC applications to CSSM and Satellite. For more information, see Provisioning Workflow for Smart Licensing Note You can autoregister the clusters to ordered virtual account using HCM-F. | Note | You can autoregister the clusters to ordered virtual account using HCM-F. |
| Note | You can autoregister the clusters to ordered virtual account using HCM-F. |
| Activate Smart Licensing for Clusters (Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder) | You can assign and unassign clusters to CSSM and Satellite using HCM-F. If autoregistration is enabled, the clusters are automatically assigned to the ordered virtual account. You do not have to
                                       manually assign the clusters. For any failed cluster registration, refer to the Cluster Summary page. |
| Service Inventory and HLM report generated | HCM-F generates the reports to view the licenses from CSSM and Satellite at virtual account-level, or customer-level. For more information on reports, see Smart Licensing Reports |
| Licensing Dashboard | HCM-F provides a view of the licenses at virtual account-level and customer-level. |
| HCM-F sync with CSSM and Satellite | HCM-F provides on-demand and automatic sync to CSSM and Satellite . You can trigger the sync from HCM-F, then HCM-F pulls the virtual account and smart account details from CSSM or Satellite and refresh the tokens, if needed. You can sync smart accounts and virtual accounts either manually or automatically. HCM-F periodically syncs with CSSM and Satellite every 8 24 hours. For more information on manual sync, see Perform Manual Sync in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . |

| Note | You can autoregister the clusters to ordered virtual account using HCM-F. |
|---|---|

| Action | Description |
|---|---|
| Log in to Cisco Commerce(CCW) and order HCS licenses. | For more information about operational licenses, see Configuring Operational Licenses |
| Create a smart account and virtual account | Create a Smart Account in CSSM or Satellite . You can also get access to an existing smart account. Create Virtual Account For more information about the one time setup activities, see Initial One Time Setup in CSSM for Smart Licensing and Initial One Time Setup in CSSM on-prem for Smart Licensing |
| Upgrade HCM-F to 12.5 version | Provision the Smart account with client credentials that includes Client ID and Client Secret in HCM-F. For more information,
                                       see HCM-F 12.5 Upgrade Guidelines |
| Setup Transport Mode | Setup the transport mode in HCM-F to connect HCM-F and UC applications to CSSM. For more information, see Set Transport Mode . |
| Provision smart account in HCM-F | Provision the credentials and Smart Account with HCM-F. HCM-F extracts smart account, local account, and virtual account-related information from CSSM and Satellite . Creates product registration token to register UC Applications in CSSM and Satellite . Provide the transport mode in HCM-F to connect HCM-F and UC applications to CSSM and Satellite. For more information, see Provisioning Workflow for Smart Licensing Note You can autoregister the clusters to ordered virtual account using HCM-F. | Note | You can autoregister the clusters to ordered virtual account using HCM-F. |
| Note | You can autoregister the clusters to ordered virtual account using HCM-F. |
| Activate Smart Licensing for Clusters (Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder) | You can assign and unassign clusters to CSSM and Satellite using HCM-F. If autoregistration is enabled, the clusters are automatically assigned to the ordered virtual account. You do not have to
                                       manually assign the clusters. |
| Cluster Sumary | For any failed cluster registration, refer to the Cluster Summary page. |
| Service Inventory and HLM report generated | HCM-F generates the reports to view the licenses from CSSM and Satellite at virtual account-level, or customer-level. For more information on reports, see Smart Licensing Reports |
| Licensing Dashboard | HCM-F provides a view of the licenses at virtual account-level and customer-level. |
| HCM-F sync with CSSM and Satellite | HCM-F provides on-demand and automatic sync to CSSM and Satellite . You can trigger the sync from HCM-F, then HCM-F pulls the virtual account and smart account details from CSSM or Satellite and refresh the tokens, if needed. You can sync smart accounts and virtual accounts either manually or automatically. HCM-F periodically syncs with CSSM and Satellite every 8 24 hours. For more information on manual sync, see Perform Manual Sync in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . |

| Note | You can autoregister the clusters to ordered virtual account using HCM-F. |
|---|---|