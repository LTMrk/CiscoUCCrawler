---
doc_id: developer-cisco-com-site-sxml-learn-soap-ui-tutorial-88d24b59f9
source_url: https://developer.cisco.com/site/sxml/learn/soap-ui-tutorial/
retrieved_at: 2026-09-01T17:49:21.934671+00:00
---

# How to Execute Serviceability Requests with SoapUI

SoapUI is an open source, cross-platform web service testing application, https://www.soapui.org/

This example uses the selectCMDeviceExt method of the RisPort70 API. This method allows clients to
                perform Cisco Unified Communications Manager (Unified CM) device-related queries. The method returns a
                snapshot of real-time device registration status from each Cisco Unified CM node. The data includes
                registration status, IP address, model info, and CTI application connections to the device. This request
                consolidates device records across nodes, returning only the device info for the latest
                registration.

### Setup

Initial setup to test with SoapUI:

- Download and install SoapUI.

- Download the WSDL to the local system or have this URL available, where <ServerName> is the
                    server name of Cisco Unified CM: https://<ServerName>:8443/realtimeservice2/services/RISService70?wsdl.

### Test

Follow these steps to test an API with SoapUI:

- Select File > New Soap Project

- Enter the Project Name

- For Initial WSDL , select one of the following methods to enter the information:

- Select Browse and navigate to the location where the WSDL was previously saved.

- Enter the URL of the WSDL in the dialog box.

The image below shows the New SOAP Project with the parameters filled in:

- Ensure the Create Requests checkbox is enabled. Select OK.

A Progress box displays the status of loading the WSDL.

The Navigator is populated with the Project Name , for example Serviceability Test,
                    and the methods available in the chosen WSDL. In this example the RisPort70 WSDL includes
                    SelectCmDevice, SelectCmDeviceExt, and SelectCtiItem.

- Expand SelectCmDeviceExt and a SOAP request Request 1 is created
                    for selectCmDeviceExt.

- Double click Request 1. The SelectCmDeviceExt request XML populates the Request 1
                    left panel.

- Select Auth (Authentication and Security-related settings) in the lower left corner
                    of the Request 1 window.

- From the Authorization drop down box, select Add New Authorization. The Add
                    Authorization box is displayed.

- Select Basic in the Type box and click OK.

- Enter Username and Password in the Authorization dialog box. Username is an application user registered in Cisco Unified CM.

- Click the Auth button to close the Authorization dialog box.

- If the URL for the Cisco Unified CM node needs to be edited, select the dropdown box to the right of
                    the URL.

- Fill in the fields in the XML request by replacing or removing ?.

- To execute the request, click the green arrow (Submit request to specified endpoint URL) in the
                    upper left corner of the XML request panel.

The SelectCmDeviceExt response is displayed in the right panel of the Request 1 window.

A closer view of the right hand panel of the response:

Cisco Unified Communications Manager (Unified CM) and Serviceability version tested: 10.0