---
doc_id: developer-cisco-com-site-hcs-discover-service-inventory-ws-13a520a193
source_url: https://developer.cisco.com/site/hcs/discover/service-inventory-ws/
retrieved_at: 2026-09-08T03:51:36.318625+00:00
---

# Service Inventory Web Service

The Service Inventory Web Service provides an interface for scheduling, configuring, and executing the generation of service inventory billing reports . This web service allows you to retrieve, process, and generate service inventory reports in a Cisco common format.

You can find the details for working with the Service Inventory Web Service in the

- Developer Guide for Cisco Hosted Collaboration Mediation Fulfillment 9.1(1) .

- Service Inventory API Reference

Here are the basic steps for getting started with the Service Inventory Web Service.

- Get the WSDL

- Learn how to Authenticate

- Checkout the sample application

## Get the WSDL

The Service Inventory Web Service WSDL is available at: https://your-hcs-box.example.com:8443/HCSWebServiceInterface/ServiceInventoryWebService?wsdl

## Authentication

The Service Inventory APIs use HTTP Basic Authentication. You should use the HCS Admin username and password to authenticate the API calls.

Because the Service Inventory APIs use HTTPS, you will need to enable SSL support in your application. Depending on the specific technology used by your application, you may need to manually install the HCS certificate into a local trust store for your application.

## Sample Application

Check out the Fulfillment API Sample Application that uses the Shared Data Repository Web Service.

Visit the HCS Developer Forums to ask questions and interact with other developers.

Forums