---
doc_id: developer-cisco-com-site-curri-help-faqs-793779cec4
source_url: https://developer.cisco.com/site/curri/help/faqs/
retrieved_at: 2026-08-25T21:04:55.265801+00:00
---

# CURRI FAQs

### Getting Started

### Technical Questions

### Getting Started

What can CURRI do?

- Enhance dial plans in ways that can't be achieved natively

- Block incoming calls based on calling number

- Route incoming calls based on calling number

- Combine with data from other applications to route calls

What are the basic requirements for a CURRI Web Application?

- Support HTTP 1.1 for persistent connection

- Support Thread pool for multiple persistent connections

- Support HTTP KeepAlive header

- Support HTTP HEAD method for KeepAlive from Cisco Unified CM

- Support Call Routing request as specified in the CURRI Developers Guide

- Support HTTP POST method for XACML Call Routing Request

- Respond with Call Routing Response as specified in the CURRI Developers Guide

How are Unified CM/Route Server connections maintained?

- Unified CM maintains persistent connections to Route servers, to reduce delay in call setup time.

- All nodes (Publisher and all Subscribers) in a Unified CM cluster, establish a connection to the route server for parallel queries at high call rate.

- The connection is always enabled on all cluster nodes that have the CallManager service enabled. The Route server should be configured to expect Route Requests from all nodes.

- URIs in External Call Control determine if HTTP or HTTPS connections are established

What should I note while configuring Unified CM to perform Route Requests?

- Specify the port number of the Route Request server in Unified CM

- Configure Route Request (web) server to hide the complexity of the application's URI :

Do: "http://server/myapp/routingrequest"

Don't: "http://server/myapp/routing/curri.asp/request/"

- Make sure the application responds to the Keep-Alive requests from Unified CM (HEAD Requests)

- Turn on Media Streaming service if custom announcements are to be played

back to top

### Technical questions

What happens if Obligation is not consistent with route decision?

When an Obligation is not consistent with a Route decision, Unified CM obeys the route decision but ignores the obligation

What happens when you modify an existing ECCP in Unified CM 8.x?

Modifying an existing ECCP does not trigger a profile reload in Unified CM 8.x. The following behavior will be observed:

- Calls will still route to the external routing application

- Responses will be ignored by Unified CM

- ECCP will treat each request as a routing "failure"

- Will route based on "Call Treatment on Failure" setting

A workaround is to restart Cisco CallManager Services.

Note: In Unified CM 9.0 and later, the defect is resolved. When modifying an existing ECCP, Unified CM will correctly trigger a profile reload.

Can the calling name and called name be modified through Routing rules API?

Yes. Starting from Unified CM 10.0, the calling name and called name can be modified through Routing rules API

How can I play custom announcements?

An announcement specified by an [id] will be played to the caller when the "greeting identification=[id]" is sent in the obligations of the Call Route Response. Unified CM has a set of pre-recorded announcements for all supported locales. You can add desired custom announcements to Unified CM. Remember to turn on the Media Streaming service, if you want custom announcements.

When and how is Failure Treatment applied by Unified CM?

Unified CM applies failure treatment in the following situations:

- Unified CM fails to establish connections to the Route Server

- Unified CM cannot parse the response for the route decision or call routing directive

- Unified CM receives 4xx or 5xx HTTP response status codes from Route Server

- Unified CM times out waiting for a response

Failure treatment is specified in the External Call Control profile. The treatment is either "Allow Calls" or "Block Calls":

- If the failure treatment is "Allow Calls", the call is routed to the current destination, as if a permit decision with a continue directive is received.

- If the failure treatment is "Block Calls", the call will be cleared, as if a deny decision with a reject directive is received.

When a failure occurs, an alarm will be logged

back to top

Visit the CURRI Developer Forums to ask questions and interact with other developers.

Forums

We've put together a whole load of hints, tips, code samples and code snippets to help you benefit from CURRI.

Learn more