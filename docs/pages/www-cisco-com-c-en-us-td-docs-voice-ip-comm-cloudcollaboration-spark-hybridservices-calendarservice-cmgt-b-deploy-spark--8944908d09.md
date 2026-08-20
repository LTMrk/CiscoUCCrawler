---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--8944908d09
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_chapter_0101.html
retrieved_at: 2026-08-20T23:54:10.501235+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: October 17, 2023

Chapter: Deploy Hybrid Calendar for a Hybrid Exchange environment

## Chapter: Deploy Hybrid Calendar for a Hybrid Exchange environment

- Deploy Hybrid Calendar for a Hybrid Exchange environment

- Deploy Expressway calendar connector for a Hybrid Exchange environment

# Deploy Hybrid Calendar for a Hybrid Exchange environment

## Deploy Expressway calendar connector for a Hybrid Exchange environment

This chapter describes setting up the Calendar Connector on Expressway to handle both Office 365 and Microsoft Exchange in
                              a Hybrid Exchange deployment. With the release of the cloud-based service for Office 365 users, you can now choose whether
                              to deploy only the Expressway-based Calendar Connector, as described in this section, or a combination of the Calendar Connector
                              and the cloud-based service.

The cloud-based service can scale beyond the 1000 user limit for Office 365 users and is simpler to deploy and maintain. It
                              does not service Microsoft Exchange users. If you deploy it alongside the calendar connector, your Office 365 users automatically
                              move to the cloud-based service (unless they are in resource groups).

Before you decide which service to deploy for your Office 365 users, read the Prepare your environment chapter of the Office 365 with cloud-based Hybrid Calendar part of this guide, to understand the requirements for that option.

### Before you begin

Prepare your environment .

If your deployment meets all of the following criteria, you can use a simplified Exchange configuration, by following all
                                    of the steps in Deploy Expressway calendar connector for Microsoft Exchange , instead of this procedure.

Your Expressway-C connects to both the on-premises Exchange environment and the Office 365 cloud through the same proxy method
                                          (either neither connects through a proxy, or both do).

Your deployment met all of the conditions for using a simplified configuration with a single impersonation account (in Set up an impersonation account for Office 365 ).

If your deployment does not meet these criteria, follow all of the steps in this procedure to set up two separate Exchange
                                    configurations on the Expressway-C -- one for the on-premises mailboxes, and one for the Office 365 mailboxes.

Step 1

Deploy Expressway calendar connector for Microsoft Exchange by adding an Exchange configuration to Expressway.

- You must enable and configure auto discovery when you add the configuration—Select Use Active Directory to enable auto discovery. We do not support manually entered Exchange addresses in Exchange hybrid environments.

For the authentication type, you should check both NTLM and Basic authentication types. If one method fails, then the other method is used.

Step 2

Enable Hybrid Calendar for users who have mailboxes in on-premises Exchange.

Step 3

Start calendar connector and ensure that the activated users are subscribed.

Step 4

As a test, in a meeting invitation in Outlook, OWA, or your calendar client, add a space scheduling keyword (such as @webex:space
                                       or @meet) to the Location field; verify that this step creates a Webex App space for an activated user.

Step 5

Stop the calendar connector. Do not proceed until you see that it fully stopped.

Step 6

Deploy Expressway calendar connector with Office 365 by adding a new Exchange configuration to Expressway, for Office 365.

For the authentication type, you should check both NTLM and Basic authentication types. If one method fails, then the other method is used.

Step 7

Enable Hybrid Calendar for users who have mailboxes in Office 365.

Step 8

Start calendar connector and ensure that activated users in both on-premises and Office 365 are subscribed.

Step 9

As a test, in an Outlook invitation, add a space scheduling keyword to the Location field; verify that this step creates a Webex App space for both on-premises Exchange and Office 365 users.

Users with either on-premises Exchange or Office 365 mailboxes can now schedule meetings using the scheduling keywords.

| Step 1 | Deploy Expressway calendar connector for Microsoft Exchange by adding an Exchange configuration to Expressway. You must enable and configure auto discovery when you add the configuration—Select Use Active Directory to enable auto discovery. We do not support manually entered Exchange addresses in Exchange hybrid environments. For the authentication type, you should check both NTLM and Basic authentication types. If one method fails, then the other method is used. |
|---|---|
| Step 2 | Enable Hybrid Calendar for users who have mailboxes in on-premises Exchange. |
| Step 3 | Start calendar connector and ensure that the activated users are subscribed. |
| Step 4 | As a test, in a meeting invitation in Outlook, OWA, or your calendar client, add a space scheduling keyword (such as @webex:space
                                       or @meet) to the Location field; verify that this step creates a Webex App space for an activated user. |
| Step 5 | Stop the calendar connector. Do not proceed until you see that it fully stopped. |
| Step 6 | Deploy Expressway calendar connector with Office 365 by adding a new Exchange configuration to Expressway, for Office 365. For the authentication type, you should check both NTLM and Basic authentication types. If one method fails, then the other method is used. |
| Step 7 | Enable Hybrid Calendar for users who have mailboxes in Office 365. |
| Step 8 | Start calendar connector and ensure that activated users in both on-premises and Office 365 are subscribed. |
| Step 9 | As a test, in an Outlook invitation, add a space scheduling keyword to the Location field; verify that this step creates a Webex App space for both on-premises Exchange and Office 365 users. |