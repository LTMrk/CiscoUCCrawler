---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-1f99577200
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_0101.html
retrieved_at: 2026-08-25T21:46:16.447001+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Configure a Service Profile

## Chapter: Configure a Service Profile

- Activate and Start	 Essential Services

- Create a Service	 Profile

# Configure a Service Profile

## Activate and Start
	 Essential Services

Essential services
		  enable communication between servers and provide capabilities to the client.

- Cisco SIP Proxy

- Cisco Sync Agent

- Cisco XCP Authentication
					 Service

- Cisco XCP Connection
					 Manager

- Cisco XCP Text Conference
					 Manager

- Cisco Presence
					 Engine

## Create a Service
	 Profile

You create a service
		  profile that contains the configuration settings for the services you add on 
		  Cisco Unified Communications Manager.
		  You add the service profile to the end user configuration for your users. The
		  client can then retrieve settings for available services from the service
		  profile.

Activate and Start Essential Services

The Find
				  and List Service Profiles window opens.

The Service Profile Configuration window opens.

- Specify a
				  unique name for the service profile in the Name field.

- Select Make
					 this the default service profile for the system , if appropriate.

For phone mode, in the IM and Presence Profile section ensure
				  that the Primary field has <None> selected.

| Step 1 | Open the Cisco
				Unified IM and Presence Serviceability interface. |
|---|---|
| Step 2 | Select Tools > Control Center - Feature
				  Services . |
| Step 3 | Select the
			 appropriate server from the Server drop-down list. |
| Step 4 | Ensure the
			 following services are started and activated: Cisco SIP Proxy Cisco Sync Agent Cisco XCP Authentication
					 Service Cisco XCP Connection
					 Manager Cisco XCP Text Conference
					 Manager Cisco Presence
					 Engine |
| Step 5 | Select Tools > Control Center - Network
				  Services . |
| Step 6 | Select the
			 appropriate server from the Server drop-down list. |
| Step 7 | Ensure Cisco
				XCP Router Service is running. |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > User Settings > Service
				  Profile . The Find
				  and List Service Profiles window opens. |
| Step 3 | Select Add
				New . The Service Profile Configuration window opens. |
| Step 4 | Enter settings
			 on the Service
				Profile Configuration window as follows: Specify a
				  unique name for the service profile in the Name field. Select Make
					 this the default service profile for the system , if appropriate. Note For phone mode, in the IM and Presence Profile section ensure
				  that the Primary field has <None> selected. | Note | For phone mode, in the IM and Presence Profile section ensure
				  that the Primary field has <None> selected. |
| Note | For phone mode, in the IM and Presence Profile section ensure
				  that the Primary field has <None> selected. |
| Step 5 | Select Save . |

| Note | For phone mode, in the IM and Presence Profile section ensure
				  that the Primary field has <None> selected. |
|---|---|