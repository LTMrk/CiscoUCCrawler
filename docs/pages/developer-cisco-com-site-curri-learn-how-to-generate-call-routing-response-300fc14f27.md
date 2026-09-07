---
doc_id: developer-cisco-com-site-curri-learn-how-to-generate-call-routing-response-300fc14f27
source_url: https://developer.cisco.com/site/curri/learn/how-to/generate-call-routing-response/
retrieved_at: 2026-09-07T14:14:46.701092+00:00
---

# Generate Call Routing Response

The Route Server evaluates the request sent by Unified CM and returns call handling instructions as
                    a Decision and Obligation. This XACML response is returned as the body of a 200 OK message.

### Decision

The XACML response includes one of the following policy decsions:

- Permit : Call is allowed.

- Deny : Call is denied.

- Indeterminate : No call routing route is determined. Follows the call treatment
                        on failure configuration.

- Not Applicable : No call routing route is determined. Follows the call treatment
                        on failure configuration.

### Obligation

The XACML may contain a call instruction XML (CIXML) obligation attribute that gives additional
                    instructions for Unified CM to route the call or apply other special treatments. Example for
                    obligations include directives to play a particular greeting before connecting a call and diverting
                    a call to a different extension than the one that was dialed.

The following are the formats for the various call routing obligations (directives):

- Continue – Routes normally to current destination

Examples include directives to play a particular greeting before connecting a call and modifying the
                    calling /called number before connecting a call.

- Divert – Routes to diverted destination specified

Examples include diverting a call to a different extension than the one that was dialed and
                    providing a reason for the call to be diverted.

- Reject – Rejects the call.

Example includes directives to play a particular announcement when the rejecting the call.

The CIXML obligation must be consistent with the policy decision. If it is not, then Unified CM
                    obeys the policy decision and not the obligation. For example, an obligation set to divert the call
                    is ignored if the policy decision is to deny that call.

To learn more about the CIXML Obligation format and parameters, refer to the CURRI Developer Guide .

### Format

The following is the call routing response format:

?

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

HTTP/1.1
                                                    200 OK

Server:
                                                    < product >

Connection:Keep-Alive

Keep-Alive:
                                                    timeout = < timeout value = "" >
                                                    max = < count >

Location:
                                                    < new-url >

Date:
                                                    < date >

Content-Length:
                                                    < length >

< response >

< result resourceid = "[name
                                                    of resource]" >

< decision >[decision
                                                    value]</ decision >

< status >

< statuscode value = "[status
                                                        code]" >

< statusmessage >[status message]</ statusmessage >

< statusdetail >[status details]</ statusdetail >

</ statuscode ></ status >

< obligations >

[other obligations]

< obligation fulfillon = "[fulfill
                                                        on value]" obligationid = "urn:cisco:cepm:3.3:xacml:policy-attribute" >

< attributeassignment attributeid = "[name
                                                        of attribute]" >

< attributevalue datatype = " http://www.w3.org/2001/XMLSchema #string" >

< cixml version="1.0>

[routing directive[sub-element]]

</ cixml >

</ attributevalue >

</ attributeassignment >

</ obligation >

</ obligations >

</ result >

</ response >

Learn How to Monitor
                    Performance .

## Monitor Performance

Learn More

## Documentation

Developer Guide

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | HTTP/1.1
                                                    200 OK Server:
                                                    < product > Connection:Keep-Alive Keep-Alive:
                                                    timeout = < timeout value = "" >
                                                    max = < count > Location:
                                                    < new-url > Date:
                                                    < date > Content-Length:
                                                    < length > < response > < result resourceid = "[name
                                                    of resource]" > < decision >[decision
                                                    value]</ decision > < status > < statuscode value = "[status
                                                        code]" > < statusmessage >[status message]</ statusmessage > < statusdetail >[status details]</ statusdetail > </ statuscode ></ status > < obligations > [other obligations] < obligation fulfillon = "[fulfill
                                                        on value]" obligationid = "urn:cisco:cepm:3.3:xacml:policy-attribute" > < attributeassignment attributeid = "[name
                                                        of attribute]" > < attributevalue datatype = " http://www.w3.org/2001/XMLSchema #string" > < cixml version="1.0> [routing directive[sub-element]] </ cixml > </ attributevalue > </ attributeassignment > </ obligation > </ obligations > </ result > </ response > |
|---|---|

| Note: Cisco Unified CM expects the CIXML obligation to be an
                                    encoded version of XML. The < and > characters
                                    have to be escaped as &lt; and &gt; respectively. |
|---|