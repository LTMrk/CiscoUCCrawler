---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-5-exwy-b-mra-expressway-deployment-guide-exwy-b--2445c6c2a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-5/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_01001.html
retrieved_at: 2026-08-16T15:36:20.664710+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

Updated: May 1, 2019

Chapter: Unified CM Configuration

## Chapter: Unified CM Configuration

# Unified CM Configuration

## SIP Trunks Between Unified CM and Expressway-C

Expressway deployments for Mobile and Remote Access do not require SIP trunk connections between Unified CM and Expressway-C. Note that the automatically generated neighbor zones between Expressway-C and each discovered Unified CM node are not SIP trunks.

However, you may still configure a SIP trunk if required. (For example, to enable B2B callers or endpoints registered to Expressway
                              to call endpoints registered to Unified CM .)

If a SIP trunk is configured, you must ensure that it uses a different listening port on Unified CM from that used for SIP line registrations to Unified CM . An alarm is raised on Expressway-C if a conflict is detected.

The ports used for SIP trunks are configured on both Unified CM and Expressway.

See the Cisco TelePresence Cisco Unified Communications Manager with Expressway (SIP Trunk) Deployment Guide for more information about configuring a SIP trunk.

See Configure Cisco Unified Communications Manager for OAuth with Refresh for information about OAuth-based authorization on SIP trunks.

### Configure Line Registration Listening Ports on Unified CM

There are two ports that are used for line registrations to Unified CM :

SIP Phone Port : the TCP port.

SIP Phone Secure Port : the TLS port.

Access System > Cisco Unified CM .

Set the SIP Phone Port to 5060 .

Set the SIP Phone Secure Port to 5061 .

### Configure SIP Trunk Listening Ports on Unified CM

Go to System > Security > SIP Trunk Security Profile and select the profile used for the SIP trunk.

If this profile is used for connections from other devices, you may want to create a separate security profile for the SIP
                                             trunk connection to Expressway.

Configure the Incoming Port to be different from that used for line registrations.

Click Save and then click Apply Config .

### Configure SIP Trunk Listening Ports on Expressway

Go to Configuration > Zones > Zones and select the Unified CM neighbor zone used for the SIP trunk.

(Note that the automatically generated neighbor zones between Expressway-C and each discovered Unified CM node for line side communications are non-configurable.)

Configure the SIP Port to the same value as the Incoming Port configured on Unified CM .

Click Save .

## Unified Communications Services Deployment Partitions

A deployment is an abstract boundary used to enclose a domain and one or more Unified Communications service providers (such
                              as Unified CM , Cisco Unity Connection , and IM and Presence Service nodes). The purpose of multiple deployments is to partition the Unified Communications services available to Mobile and Remote
                              Access (MRA) users. So different subsets of MRA users can access different sets of services over the same Expressway pair.

We recommend that you do not exceed ten deployments.

Deployments and their associated domains and services are configured on the Expressway-C.

One primary deployment (called "Default deployment" unless you rename it) automatically encloses all domains and services
                              until you create and populate additional deployments. This primary deployment cannot be deleted, even if it is renamed or
                              has no members.

To partition the services that you provide through Mobile and Remote Access, create as many deployments as you need. Associate
                              a different domain with each one, and then associate the required Unified Communications resources with each deployment.

You cannot associate one domain with more than one deployment. Similarly, each Unified Communications node may only be associated
                              with one deployment.

### Example

Consider an implementation of two sets of Unified Communications infrastructure to provide a live MRA environment and a staging
                              environment, respectively. This implementation might also require an isolated environment for sensitive communications, as
                              a third set.

### Create a New Deployment

Log in to the Expressway-C.

Go to Configuration > Unified Communications > Deployments and click New .

Give the deployment a name and click Create deployment .

The new deployment is listed on the Deployments page and is available to select when editing domains or UC services.

### Associate a Domain with a Deployment

Go to Configuration > Domains .

The domains and their associated services are listed here. The deployment column shows where the listed domains are associated.

Click the domain name, or create a new domain.

In the Deployment field, select the deployment which will enclose this domain.

Click Save .

### Associate a Unified CM or Other Server/Service with the Deployment

Go to Configuration > Unified Communications and select one of the following entries:

- Unified CM servers

- IM and Presence Service nodes

- Unity Connection servers

Any previously discovered service nodes of the selected type are listed here. The deployment column shows where the listed
                                             nodes are associated.

If the list is not properly populated, see Discover Unified Communications Servers and Services for Mobile and Remote Access .

Click the server / service node name.

In the Deployment field, select which deployment will enclose this server / service node.

Click Save.

When you save this change, the Expressway-C refreshes the connection to the node, which may temporarily disrupt the service
                                             to the connected users.

Repeat for any other Unified Communications services that will belong to the deployment.

| Step 1 | Access System > Cisco Unified CM . |
|---|---|
| Step 2 | Set the SIP Phone Port to 5060 . |
| Step 3 | Set the SIP Phone Secure Port to 5061 . |

| Step 1 | Go to System > Security > SIP Trunk Security Profile and select the profile used for the SIP trunk. If this profile is used for connections from other devices, you may want to create a separate security profile for the SIP
                                             trunk connection to Expressway. |
|---|---|
| Step 2 | Configure the Incoming Port to be different from that used for line registrations. |
| Step 3 | Click Save and then click Apply Config . |

| Step 1 | Go to Configuration > Zones > Zones and select the Unified CM neighbor zone used for the SIP trunk. (Note that the automatically generated neighbor zones between Expressway-C and each discovered Unified CM node for line side communications are non-configurable.) |
|---|---|
| Step 2 | Configure the SIP Port to the same value as the Incoming Port configured on Unified CM . |
| Step 3 | Click Save . |

| Step 1 | Log in to the Expressway-C. |
|---|---|
| Step 2 | Go to Configuration > Unified Communications > Deployments and click New . |
| Step 3 | Give the deployment a name and click Create deployment . The new deployment is listed on the Deployments page and is available to select when editing domains or UC services. |

| Step 1 | Go to Configuration > Domains . The domains and their associated services are listed here. The deployment column shows where the listed domains are associated. |
|---|---|
| Step 2 | Click the domain name, or create a new domain. |
| Step 3 | In the Deployment field, select the deployment which will enclose this domain. |
| Step 4 | Click Save . |

| Step 1 | Go to Configuration > Unified Communications and select one of the following entries: Unified CM servers IM and Presence Service nodes Unity Connection servers Any previously discovered service nodes of the selected type are listed here. The deployment column shows where the listed
                                             nodes are associated. If the list is not properly populated, see Discover Unified Communications Servers and Services for Mobile and Remote Access . |
|---|---|
| Step 2 | Click the server / service node name. |
| Step 3 | In the Deployment field, select which deployment will enclose this server / service node. |
| Step 4 | Click Save. When you save this change, the Expressway-C refreshes the connection to the node, which may temporarily disrupt the service
                                             to the connected users. |
| Step 5 | Repeat for any other Unified Communications services that will belong to the deployment. |