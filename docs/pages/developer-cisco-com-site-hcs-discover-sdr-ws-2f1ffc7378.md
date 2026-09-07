---
doc_id: developer-cisco-com-site-hcs-discover-sdr-ws-2f1ffc7378
source_url: https://developer.cisco.com/site/hcs/discover/sdr-ws/
retrieved_at: 2026-09-07T14:15:30.326400+00:00
---

# Shared Data Repository Web Service

The Shared Data Repository Web Service API, you can view and modify (Create, Read, Update, Delete) data in the Shared Data Repository. You can use the SDR Web Service to manage customers, clusters, applications and other entities .

You can find the details for working with the Shared Data Repository Web Service in the

- Developer Guide for Cisco Hosted Collaboration Mediation Fulfillment 9.1(1) .

Here are the basic steps for getting started with the Shared Data Repository Web Service.

## Get the WSDL

The Shared Data Repository Web Service WSDL is available at: https://your-hcs-box.example.com:8443/HCSWebServiceInterface/SharedDataRepositoryWebService?wsdl

## Authentication

The Shared Data Repository APIs use HTTP Basic Authentication. You should use the HCS Admin username and password to authenticate the API calls.

Because the Fulfillment APIs use HTTPS, you will need to enable SSL support in your application. Depending on the specific technology used by your application, you may need to manually install the HCS certificate into a local trust store for your application.

## Shared Data Repository Data Model

The following diagram shows the relationships between the most important entities in the Shared Data Repository logical data model and the hierarchical nature of the data model. The diagram is intended to give an overview of the organization of the database and provide context for each of the entities available in the NBI.

The following entities comprise the main sections of the data model:

- Service Provider: This entity represents the company in which Cisco HCS is deployed. The service provider entity can have only a single instance. The attributes that are associated with the service provider can be synced from Cisco Unified Communications Domain Manager if the CUCDMSync service is running and configured in Cisco HCM-F.

- Data Center: This hierarchy represents the data centers in the Cisco HCS deployment. There can be any number of data centers. Each data center can have zero or more UCS Managers and vCenters. The UCS Managers and vCenters each have a hierarchy of entities as shown in the diagram. Note the linkage between Blade and ESXiHost. This linkage is important for Service Assurance to perform fault correlation.

- Customer: This hierarchy represents the configuration of each customer deployed in the system. Each customer has one or more clusters and associated applications.

- Management Network: This hierarchy represents the management network for the service provider, which contains the domain managers that are used for provisioning and service assurance.

- Network Address and Credential: These entities are associated with a number of different types of entities such as vCenter, cluster applications, and management applications.

## Sample Application

Check out the Fulfillment API Sample Application that uses the Shared Data Repository Web Service

Visit the HCS Developer Forums to ask questions and interact with other developers.

Forums