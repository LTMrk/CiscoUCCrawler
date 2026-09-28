---
doc_id: developer-cisco-com-site-cer-discover-overview-1aec7cc686
source_url: https://developer.cisco.com/site/cer/discover/overview/
retrieved_at: 2026-08-25T21:03:45.409427+00:00
---

# CER Overview

Cisco Emergency Responder (CER) is an emergency communication system that helps you respond to a crisis quickly and efficiently. It also maintains a record of the emergency calls that your system receives so that you can access this information later.

CER augments the conventional E9-1-1 support available in the Cisco Unified Communications Manager and provides a 5-key function that exceeds the E9-1-1 capabilities in the conventional voice network:

- Emergency Responder automatically tracks the location of users, and eliminates the need for manual ALI record updates. It overcomes the limitation of a single move per user, per day, in a conventional E9-1-1 network.

- It routes calls to 911 (or any other configured number) to the appropriate gateway based on the current location of the caller.

- It ensures that the emergency operator (PSAP) gets the correct location information of the 911 caller, even if the user frequently moves between different sites.

- It alerts on-site emergency response personnel (for example, a security desk) that a 911 call is in progress. The alert information includes phone number and the current location of the 911 caller.  This information is delivered via email, pager, telephone call, and an auto-refreshing alert webpage.

Note:  Alerts via SNMP, 911 call monitor/barge-in (post-Bravo CallManager feature) will be included in the future.

- It creates an audit log for the E9-1-1 system configuration change to facilitate change management and reduce system down-time due to configuration errors. It records a history log of all the 911 calls to facilitate capacity planning, abuse monitoring, and also document emergency incidents.

For more information, refer to admin and user guides which can be downloaded from internet.

CER exposes APIs for authentication, phone discovery and managing the server. The APIs use HTTP Basic Authentication method. The request must include the API access credentials in the Authorization header, and the password must be sent in MD5 encrypted format. The user credentials can only perform GET operations on the REST API resources.

As an example, the authentication request must be sent in below format

http://{CER-IP}/cerappservices/export/authenticate/status/{user-name}/{MD5-encrypted-password}