---
doc_id: developer-cisco-com-site-curri-learn-how-to-configure-external-call-control-profile-79d76652e2
source_url: https://developer.cisco.com/site/curri/learn/how-to/configure-external-call-control-profile/
retrieved_at: 2026-09-07T14:10:19.936342+00:00
---

# Configure External Call Control Profile

### System Requirements for External Call Control

The following system requirements exist for External Call Control:

- Cisco Unified Communications Manager 8.0(2) (or higher)

- Cisco Unified Routing Rules XML Interface, which provides the route decisions and obligation for the calls

### What is an External Call Control Profile?

The External Call Control Profile (ECCP) is how you link your application with Unified CM.

Configuring an ECCP adds your application's URL to the Unified CM database. The ECCP can then be added to Trigger Points in Unified CM.

In Cisco Unified CM Administration, specify the following information in the "External Call Control Profile Configuration" window :

- Name of the External Call Control Profile (ECCP)

- URI of the web service (Route Server) application

- permits configuration of two URIs,  for redundancy (active & standby) and for load balancing

- supports HTTP or HTTPS

- Timeout value for call routing response

- Diversion rerouting calling search space (for call diversion)

- Call treatment on failures

This image shows a External Call Control Profile Configuration window.

### What is Trigger Point?

It is the point in Unified CM's routing logic at which Unified CM issues a Route Request.

- Translation Pattern trigger points are available in Unified CM 8.0(1) and later.

- Route Patterns and Directory Numbers are trigger points in Unified CM 10.0 and later.

### Enable ECCP in Translation Pattern Trigger point

### Enable ECCP in Route Pattern Trigger Point (In Unified CM 10.0 and later)

### Enable ECCP in Directory Number Trigger Point (In Unified CM 10.0 and later)

Understand Unified CM's Call Routing Request .

## Call Routing Request

Learn More

## Documentation

Developer Guide