---
doc_id: developer-cisco-com-site-sxml-discover-overview-service-control-6b026d69ac
source_url: https://developer.cisco.com/site/sxml/discover/overview/service-control/
retrieved_at: 2026-09-01T17:49:01.086214+00:00
---

# Control Center and Control Center Extended Overview

The Control Center and Control Center Extended services provide APIs to support remote control of Cisco
                Unified Communication Manager (Unified CM) service activation/deployment and deactivation/undeployment,
                and programmatically start, stop, or restart processes across the network.

### Use Cases

These services are useful in scenarios such as:

- Retrieving the status of a service to help troubleshoot issues

- Remotely starting and stopping a feature or network service, such as restarting the TFTP service
                    after deploying a new file to the TFTP server.

### How It Works

Control Center is a standards-based SOAP interface, with available WSDL schema definition. The
                application sends a SOAP request with the application user's credentials to the Control Center web
                service on Cisco Unified CM. The web service processes the request and returns a SOAP response to the
                application.

Control Center and Control Center Extended services allow operations only on the local node, which is
                specified by the NodeName element.

For each server in the cluster, clients are encouraged to send a getProductInformationList request to
                retrieve product information. Clients only need to send this request once during initialization. The
                information returned is used in Control Center and Control Center Extended operations.

### Additional Information

Only deployable services can be started, stopped, or restarted. To find out if a service is deployable
                use getProductInformationList, soapGetStaticServiceList, or getStaticServiceListExtended.

Some services require other dependent services to be started for the functionality to work correctly. To
                find out if a service has any dependencies use getProductInformationList, soapGetStaticServiceList, or
                getStaticSercieListExtended.

ControlCenterServicesEx is an extension to ControlCenterServices with some additional features
                supported.