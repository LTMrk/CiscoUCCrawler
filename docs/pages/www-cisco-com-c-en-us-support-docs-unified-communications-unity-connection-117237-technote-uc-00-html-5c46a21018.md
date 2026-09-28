---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-117237-technote-uc-00-html-5c46a21018
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/117237-technote-uc-00.html
retrieved_at: 2026-08-17T02:13:31.691087+00:00
---

Unity Connection SMTP Domain Name Change

# Unity Connection SMTP Domain Name Change

Updated: January 14, 2014

Document ID: 117237

Contents

## Contents

## Introduction

This document describes how to update the Simple Mail Transfer Protocol (SMTP) domain name in Connection Administration. This domain has an effect on Unified Messaging and Digital Networking.

Unity Connection has the ability to perform as an SMTP client as well as an SMTP server. By default, the SMTP domain name is set to the Fully Qualified Domain Name (FQDN - hostname with DNS domain name appended, if applicable) of the first node installed . In certain scenarios, it might be necessary to change the SMTP domain name from the default value. This might be required in order to ensure that each of the Connection Locations has a unique SMTP domain, and that this domain is not the same as the corporate e-mail domain.

If you have a current Digital Networking setup, in order to change the SMTP domain for a cluster you must remove it from the network. Complete these steps before you add it back to the Digital Network:

Check all remote locations in order to verify that the location (cluster) to be changed no longer appears in either of these lists:

- Connection Administration > Networking > Links > Intrasite Links

- Connection Administration > Networking > Links > Intersite Links

Once the location no longer appears in remote clusters, complete these steps in order to change the SMTP domain:

- Go to the Unity Connection Administration web page.

- Choose System Settings > SMTP Configuration > Server .

- Click Change SMTP Domain . Update the domain name and click Save .

- You will be prompted to restart these services: Connection Conversation Manager, Connection Message Transfer Agent, and Connection SMTP Server.

- If in a cluster, restart Connection Conversation Manager and Connection SMTP Server on both servers (Mail Transfer Agent [MTA] only runs on the Primary node).

As applicable, add back the Intrasite and Intersite links.

Note : Ensure the SMTP domain of Cisco Unity Connection is different from the corporate e-mail domain in order to avoid issues in message routing for Cisco Unity Connection.

## Related Information

- How Message Routing Works Through SMTP Domain Name

- Technical Support & Documentation - Cisco Systems