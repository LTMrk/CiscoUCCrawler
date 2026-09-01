---
doc_id: developer-cisco-com-site-sxml-discover-overview-risport-25d67ee4be
source_url: https://developer.cisco.com/site/sxml/discover/overview/risport/
retrieved_at: 2026-09-01T17:48:52.738776+00:00
---

# RisPort Overview

The RisPort (Real-Time Information Port) service provides an API for querying the current connection
                status of phones, devices, and applications connected to Cisco Unified Communications Manager (Cisco
                Unified CM). Details provided by RisPort include last known connection and registration state, IP
                address, and model information. The API provides queries for single device or application instances, and
                wildcard queries which return the status of multiple devices at once.

The RisPort API allows clients to:

- Query Cisco Unified CM for the status and details of phones and other telephony devices

- Query Cisco Unified CM for the status and details of CTI applications

### Use Cases

RisPort allows applications to retrieve the registration state of a device and current IP address of a
                device or application. This information is useful in scenarios such as:

- A notification and alert application which obtains the IP address of a set of phones from RisPort in
                    order to send an on-screen push notification via the IP Phone Services API

- A system health and monitoring application which periodically checks the registration status of
                    critical phone devices or CTI applications via RisPort in order to alert administrators of
                    connection failures.

### How It Works

RisPort is a standards-based SOAP interface, with available WSDL schema definition. The application sends
                a SOAP request with the application user’s credentials to the RisPort web service on Cisco
                Unified CM. The web service processes the request and returns a SOAP response to the application.

### Additional Information

RisPort device queries are based on:

- Specific device and application parameters, such as device name, IP address, directory number,
                    device type, or device class.

- Wildcard searches, for example, where devices are requested using an asterisk, “*”, or
                    a specific list of search criteria, such as device names.

The limit on devices in a query response is 1000. If a query gathers information on more than 1000
                devices, the response is limited to 1000 devices. If information on exactly 1000 devices is returned, an
                additional query is needed to determine if exactly 1000 devices are available or the results have been
                truncated. Refer to [Scalability and Performance](link) for more details.

RisPort service provides two methods to retrieve device information: SelectCmDevice and
                SelectCmDeviceExt. For both methods, either set NodeName to the particular node from which to retrieve
                information or set NodeName to blank to retrieve information from all nodes in a cluster.

When NodeName in the RisPort request is blank:

- SelectCmDevice returns information for all devices in the cluster. If a device is registered on more
                    than one node, multiple results for the same device are returned. Receiving old status for a device
                    is possible.

- SelectCmDeviceExt consolidates status across nodes and eliminates duplicate information, if needed.
                    One entry per device with the latest status is returned from SelectCmDeviceExt.

SelectCmDevice and SelectCmDeviceExt provide a snapshot of device status. For an application needing
                device status updates, use RisPort to poll for updates. The StateInfo feature can be used.

For applications which periodically query RisPort for status on a set of phones, the RisPort service
                provides a StateInfo feature which tracks and returns results only for devices that have changed status
                since the last query.

If an application previously used SelectCmDevice or SelectCmDeviceExt and you are unsure if the response
                information has changed, use the StateInfo element to determine if the response information has changed.
                Add the StateInfo element data included in the previous response into the SelectCmDevice or
                SelectCmDeviceExt request. The response includes a Boolean value for the NoChange element.

- If the value for NoChange is true, then the response remains unchanged.

- If the value for NoChange is false, then the response has changed and your application should make a
                    new SelectCmDevice request.

RisPort queries return the current connection status of phones, devices, and applications connected to
                Cisco Unified CM. The connection status and other information is reset when RisPort services are
                stopped. After Cisco Unified CM is restarted, devices need to register again. Only information on
                devices that have registered since the most recent start of Cisco Unified CM is returned with a RisPort
                query.

### Product Related Documentation

Learn more about Cisco Unified CM: