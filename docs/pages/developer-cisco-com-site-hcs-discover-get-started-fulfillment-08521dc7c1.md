---
doc_id: developer-cisco-com-site-hcs-discover-get-started-fulfillment-08521dc7c1
source_url: https://developer.cisco.com/site/hcs/discover/get-started/fulfillment/
retrieved_at: 2026-09-07T14:15:35.226211+00:00
---

# HCS Fulfillment APIs

The HCS Fulfillment APIs provide APIs to provision and manage the resources and services in an HCS deployment. The Fulfillment APIs are grouped by function.

Shared Data Repository API

Using the Shared Data Repository Web Service API, you can view and modify (Create, Read, Update, Delete) data in Shared Data Repository. You can use the SDR Web Service to manage customers, clusters, applications and other entities .

Fulfillment Web Service API

Using the Fulfillment Web Services, you can perform fulfillment-related tasks, such as triggering manual syncs, starting manual syncs, restarting jobs, and non-CRUD Shared Data Repository operations. The Fulfillment Web Service also includes the automated provisioning feature to automatically size and provision HCS applications .

Service Inventory Web Service API

The Service Inventory Web Service provides an interface for scheduling, configuring, and executing the generation of service inventory billing reports . This web service allows you to retrieve, process, and generate service inventory reports in a Cisco common format.

HCS License Manager Web Service API

HCS License Manager Web Service provides an interface to allow the HCM-F administrator to perform license management tasks such as setting the global deployment mode, creating or deleting an ELM, assigning a customer/UC cluster to an ELM, unassigning a customer/UC Cluster from an ELM, updating the assigned cluster's platform credential, and retrieving the license relationship among ELMs, customers, and UC clusters.

Platform Administrative Web Services

The Platform Administrative Web Services (PAWS) API provides methods to manage and schedule backups and upgrades

## Authentication

All of the Fulfillment APIs use HTTP Basic Authentication. You should use the HCS Admin username and password to authenticate the API calls.

Because the Fulfillment APIs use HTTPS, you will need to enable SSL support in your application. Depending on the specific technology used by your application, you may need to manually install the HCS certificate into a local trust store for your application.

## Developer Resources

- Developer Guide for Cisco Hosted Collaboration Mediation Fulfillment 9.1(1)

- Cisco Hosted Collaboration Solution (HCS) Support page

- HCS Fulfillment API Sample Client Application

Visit the HCS Developer Forums to ask questions and interact with other developers.

Forums