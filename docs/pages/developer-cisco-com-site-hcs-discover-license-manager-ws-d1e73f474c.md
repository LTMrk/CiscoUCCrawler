---
doc_id: developer-cisco-com-site-hcs-discover-license-manager-ws-d1e73f474c
source_url: https://developer.cisco.com/site/hcs/discover/license-manager-ws/
retrieved_at: 2026-09-08T03:51:40.457749+00:00
---

# License Manager Web Service

HCS License Manager Web Service provides an interface to allow the HCM-F administrator to perform license management tasks such as setting the global deployment mode, creating or deleting an ELM, assigning a customer/UC cluster to an ELM, unassigning a customer/UC Cluster from an ELM, updating the assigned cluster's platform credential, and retrieving the license relationship among ELMs, customers, and UC clusters.

You can find the details for working with the License Manager Web Service in the

- Developer Guide for Cisco Hosted Collaboration Mediation Fulfillment 9.1(1) .

- HCS WebServices Interface JavaDoc

Here are the basic steps for getting started with the Shared Data Repository Web Service.

## Get the WSDL

The License Manager Web Service WSDL is available at: https://your-hcs-box.example.com:8443/HCSWebServiceInterface/HCSLicenseManagerWebService?wsdl

## Authentication

The Service Inventory APIs use HTTP Basic Authentication. You should use the HCS Admin username and password to authenticate the API calls.

Because the Service Inventory APIs use HTTPS, you will need to enable SSL support in your application. Depending on the specific technology used by your application, you may need to manually install the HCS certificate into a local trust store for your application.

## Sample Application

Check out the Fulfillment API Sample Application that uses the Shared Data Repository Web Service

Subscribe to receive the latest news and updates

Subscribe