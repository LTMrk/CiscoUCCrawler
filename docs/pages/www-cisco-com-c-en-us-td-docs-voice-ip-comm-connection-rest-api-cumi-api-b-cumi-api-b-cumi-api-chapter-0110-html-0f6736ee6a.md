---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-0110-html-0f6736ee6a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_0110.html
retrieved_at: 2026-08-21T08:06:31.671033+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface CUMI API -- Scaling Applications Using Notifications

## Chapter: Cisco Unity Connection Messaging
	 Interface CUMI API -- Scaling Applications Using Notifications

# Cisco Unity Connection Messaging
                     	 Interface CUMI API -- Scaling Applications Using Notifications

## About
                        	 Notifications

Cisco Unity
                           		Connection Provides two types of Notifications

COMET
                                 			 Notifications. Available through the CUMI. It is a subscription to an
                                 			 individual mailbox's events.

Bulk
                                 			 Notification via the CUNI. The subscriptions can be created for multiple
                                 			 mailboxes at the same time.

## Scalability

Cisco has tested the notification
                           		APIs under load to provide guidance on how they can be scaled. It is advised
                           		that development teams created solutions using these APIs validate their
                           		appliactions as the numbers can change based on the hardware performance as
                           		well as other loads on the system.

### Test
                              	 Hardware

The results are based on tests
                              		done on a 20,000 user OVA Virtual machine.

### Test
                              	 Results

CUMI COMET notifications only

, a single server performs acceptably with up to 10,000 users.

CUNI Notifications only

, a single server performs acceptably with up to 6000 users. Each
                              		individual subscription is for 500 users or lesser.

Combined CUMI COMET and CUNI Notifications

, a single server performs acceptably with up to 5000 users. Each
                              		individual CUNI subscription is for 500 users or lesser.