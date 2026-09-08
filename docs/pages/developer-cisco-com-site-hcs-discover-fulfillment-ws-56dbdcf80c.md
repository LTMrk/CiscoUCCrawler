---
doc_id: developer-cisco-com-site-hcs-discover-fulfillment-ws-56dbdcf80c
source_url: https://developer.cisco.com/site/hcs/discover/fulfillment-ws/
retrieved_at: 2026-09-08T03:51:32.142465+00:00
---

# Fulfillment Web Service

Using the Fulfillment Web Services, you can perform fulfillment-related tasks, such as triggering manual syncs, starting manual syncs, restarting jobs, and non-CRUD Shared Data Repository operations.

The Fulfillment Web Service also includes the automated provisioning feature to automatically size and provision HCS applications .

You can find the details for working with the Fulfillment Web Service in the

- Developer Guide for Cisco Hosted Collaboration Mediation Fulfillment 9.1(1) .

- Fulfillment API Reference .

Here are the basic steps for getting started with the Fufillment Web Service

## Get the WSDL

The Fulfillment Web Service WSDL is available at: https://your-hcs-box.example.com:8443/HCSWebServiceInterface/Fulfillment WebService?wsdl

## Authentication

The Fulfillment APIs use HTTP Basic Authentication. You should use the HCS Admin username and password to authenticate the API calls.

Because the Fulfillment APIs use HTTPS, you will need to enable SSL support in your application. Depending on the specific technology used by your application, you may need to manually install the HCS certificate into a local trust store for your application.

## Infrastructure Platform Automation

Infrastructure Platform Automation (IPA) automates the UC application provisioning steps for on-boarding customers using an XML configuration file that is loaded in Infrastructure Manager within the HCM-F interface.

The installAndProvisionHCSApplications API of the HCS Fulfillment Web Service provides programmatic access to this feature.

You can find out more information about the IPA feature in:

- the How-To...Use Infrastructure Platform Automation article

- the Infrastructure Platform Automation chapter of the Cisco HCS Customer Provisioning and Administration 9.0(1) Guide

## Sample Application

Check out the Fulfillment API Sample Application that uses the Shared Data Repository Web Service

Subscribe to receive the latest news and updates

Subscribe