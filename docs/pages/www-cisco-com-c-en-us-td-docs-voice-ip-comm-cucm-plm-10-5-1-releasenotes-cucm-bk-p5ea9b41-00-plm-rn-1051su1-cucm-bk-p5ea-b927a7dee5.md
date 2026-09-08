---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-1-releasenotes-cucm-bk-p5ea9b41-00-plm-rn-1051su1-cucm-bk-p5ea-b927a7dee5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_1/releasenotes/CUCM_BK_P5EA9B41_00_plm-rn-1051su1/CUCM_BK_P5EA9B41_00_plm-rn-1051su1_chapter_0100.html
retrieved_at: 2026-09-08T04:52:45.426492+00:00
---

Release Notes for Cisco Prime License Manager Release 10.5(1)SU1

# Release Notes for Cisco Prime License Manager Release 10.5(1)SU1

Updated: October 23, 2014

Chapter: New and Changed Information

## Chapter: New and Changed Information

- Credential Policy

- Custom Log-On	 Message

- Cisco Prime License Manager Removal

# New and Changed Information

## Credential Policy

It is the only account that can create or delete administrator accounts.

It is the only account that can modify the existing credential policy.

For more information, see the Cisco Prime License Manager User Guide, Release 10.5(1)SU1 : http:/​/​www.cisco.com/​c/​en/​us/​support/​cloud-systems-management/​prime-license-manager/​products-user-guide-list.html .

## Custom Log-On
	 Message

In a coresident
		  deployment, a custom log-on message created for Cisco Unified Communications
		  Manager is automatically displayed in the Cisco Prime License Manager login
		  window. The message is created through the Cisco Unified Operating System
		  Administration interface. For information about how to create or edit a custom
		  log-on message, see the Cisco Unified
			 Communications Operating System Administration Guide .

A standalone deployment does not support a custom log-on message.

## Cisco Prime License Manager Removal

In a coresident
		  deployment, you have the option to remove Cisco Prime License Manager if it is
		  not being used. For example, in a Cisco Unified Communications Manager cluster,
		  Cisco Prime License Manager is installed on publisher nodes and subscriber nodes. Since the Cisco Prime License Manager only needs to be active
		  on a single node to manage the licensing of all nodes, you may choose to remove
		  Cisco Prime License Manager from the nodes where it is inactive. 
		For more information, see the Cisco Prime License Manager User Guide, Release 10.5(1)SU1 .

To restore Cisco Prime License Manager after it has been removed, contact Cisco Technical Assistance Center (TAC).

| Note | A standalone deployment does not support a custom log-on message. |
|---|---|

| Note | To restore Cisco Prime License Manager after it has been removed, contact Cisco Technical Assistance Center (TAC). |
|---|---|