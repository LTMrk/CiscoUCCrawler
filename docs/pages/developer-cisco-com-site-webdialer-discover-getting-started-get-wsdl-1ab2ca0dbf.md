---
doc_id: developer-cisco-com-site-webdialer-discover-getting-started-get-wsdl-1ab2ca0dbf
source_url: https://developer.cisco.com/site/webdialer/discover/getting-started/get-wsdl/
retrieved_at: 2026-08-25T21:11:54.968926+00:00
---

# Get the WebDialer WSDL

The WebDialer WSDL is included with each implementation of Cisco Unified Communications Manager (Unified
                CM).

Cisco WebDialer WSDL

Follow these steps to get the WSDL for WebDialer:

- Copy the address below into your browser.

- https://<server>/webdialer/wsdl/wd70.wsdl

- Replace "<server>" with the Unified CM node (typically a Publisher node) or IP
                    address and your secured port.

- Once the WSDL is accessed you may wish to copy it into a text document and save it for review or
                    testing purposes.

Cisco WebDialer Service

Accessing the WebDialer API from your application or with a testing tool (like SOAP UI) is going to
                require sending a request to the Cisco WebDialer node where the Cisco WebDialer Service is running.

The most current Cisco WebDialer Service is included with Unified CM and can be accessed by your
                application here:

https://<server>/webdialer/services/WebdialerSoapService70.

Replace "<server>" with the Unified CM node name (typically a Publisher node) or IP
                address and your secured port number.

In order to access the Cisco WebDialer Service be sure that all required services are turned on. See
                Authentication.