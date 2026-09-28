---
doc_id: developer-cisco-com-site-curri-learn-how-to-curri-hello-world-79f4b80676
source_url: https://developer.cisco.com/site/curri/learn/how-to/curri-hello-world/
retrieved_at: 2026-09-07T14:10:10.953327+00:00
---

# CURRI Hello World

To get started with CURRI, let us look at a simple call routing example.

Here we see how a call would be managed by Unified CM using the Cisco Unified Routing Rules
                    Interface (CURRI) API.

- Let us assume that the administrator has configured an External Call Control Profile "ECC
                        profile to RS1 & RS2" and enabled it at the translation pattern 5XXXX. You can see how
                        to do that here .

- User A with directory number 9725550101 calls user B by dialing 50102. Cisco Unified CM is
                        configured to allow five digit dialing for internal calls. The dialed number, 50102, is
                        transformed into +19725550102 on the translation pattern 5XXXX.

- When Unified CM detects that dialed pattern has an ECCP associated with it, it pauses
                        processing of the call and issues a call routing request to the URL specified in the ECCP.

An example of the call routing request can be seen below:

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

32

33

34

35

36

37

38

39

40

41

42

43

POST
                                                    /pdp/AuthorizationEndPoint HTTP/1.1

Host:
                                                    10.89.81.55:8080

Accept:
                                                    */*

Content-type:
                                                    text/xml; charset=ISO-8859-1

methodName:
                                                    isRoleAccessAllowed

User-Agent:
                                                    CiscoUCM-HttpClient/1.0

Connection:Keep-Alive

Content-Length:
                                                    1704

< request xmlns = "urn:oasis:names:tc:xacml:2.0:context:schema:os" >

< subject subjectcategory = "urn:oasis:names:tc:xacml:1.0:subject-category:access-subject" >

< attribute attributeid = "urn:oasis:names:tc:xacml:1.0:subject:role-id" datatype = " http://www.w3.org/2001/XMLSchema #string" >
                                                        Issuer="requestor">

< attributevalue >CISCO:UC:UCMPolicy</ attributevalue >

</ attribute >

< attribute attributeid = "urn:Cisco:uc:1.0:callingnumber" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >9725550101</ attributevalue >

</ attribute >

;
                                                      < attribute attributeid = "urn:Cisco:uc:1.0:callednumber" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >50102</ attributevalue >

</ attribute >

< attribute attributeid = "urn:Cisco:uc:1.0:transformedcgpn" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >+19725550101</ attributevalue >

</ attribute >

< attribute attributeid = "urn:Cisco:uc:1.0:transformedcdpn" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >+19725550102</ attributevalue >

</ attribute >

</ subject >

< resource >

< attribute attributeid = "urn:oasis:names:tc:xacml:1.0:resource:resource-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" >

< attributevalue >CISCO:UC:VoiceOrVideoCall</ attributevalue >

</ attribute >

</ resource >

< action >

< attribute attributeid = "urn:oasis:names:tc:xacml:1.0:action:action-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" >

< attributevalue >any</ attributevalue >

</ attribute >

</ action >

< environment >

< attribute attributeid = "urn:Cisco:uc:1.0:triggerpointtype" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >translationpattern</ attributevalue >

</ attribute >

</ environment >

</ request >

To learn more about call routing request, visit Read Call Routing
                    Request .

4. In response to the request, the Route Server provides a directive - permit with a simple
                    continue.

An example of the call routing response can be seen below:

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

HTTP/1.1
                                                    200 OK

Server:
                                                    Apache-Coyote/1.1

Connection:
                                                    Keep-Alive

Keep-Alive:
                                                    timeout = 1000 max = 100

Transfer-Encoding:
                                                    chunked

Date: Mon,
                                                    08 Jun 2009 16:50:21 GMT

< response >

< result >

< decision >Permit</ decision >

< obligations >

< obligation fulfillon = "Permit" obligationid = "continue.simple" >

< attributeassignment attributeid = "Policy:continue.simple" >

< attributevalue datatype = " http://www.w3.org/2001/XMLSchema #string" >

< cixml version = "1.0" >

< continue ></ continue >

</ cixml >

</ attributevalue >

</ attributeassignment >

</ obligation >

</ obligations >

</ result >

</ response >

To learn more about call routing response, visit Generate Call
                    Routing Response .

5. Unified CM routes the call according to the directive. In this example, the call continues to
                    9725550102.

## Configure External Call Control Profile

Learn More

## Documentation

Developer Guide

## Sample App

Check out the CURRI Sample App

Sample App

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 | POST
                                                    /pdp/AuthorizationEndPoint HTTP/1.1 Host:
                                                    10.89.81.55:8080 Accept:
                                                    */* Content-type:
                                                    text/xml; charset=ISO-8859-1 methodName:
                                                    isRoleAccessAllowed User-Agent:
                                                    CiscoUCM-HttpClient/1.0 Connection:Keep-Alive Content-Length:
                                                    1704 < request xmlns = "urn:oasis:names:tc:xacml:2.0:context:schema:os" > < subject subjectcategory = "urn:oasis:names:tc:xacml:1.0:subject-category:access-subject" > < attribute attributeid = "urn:oasis:names:tc:xacml:1.0:subject:role-id" datatype = " http://www.w3.org/2001/XMLSchema #string" >
                                                        Issuer="requestor"> < attributevalue >CISCO:UC:UCMPolicy</ attributevalue > </ attribute > < attribute attributeid = "urn:Cisco:uc:1.0:callingnumber" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >9725550101</ attributevalue > </ attribute > ;
                                                      < attribute attributeid = "urn:Cisco:uc:1.0:callednumber" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >50102</ attributevalue > </ attribute > < attribute attributeid = "urn:Cisco:uc:1.0:transformedcgpn" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >+19725550101</ attributevalue > </ attribute > < attribute attributeid = "urn:Cisco:uc:1.0:transformedcdpn" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >+19725550102</ attributevalue > </ attribute > </ subject > < resource > < attribute attributeid = "urn:oasis:names:tc:xacml:1.0:resource:resource-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" > < attributevalue >CISCO:UC:VoiceOrVideoCall</ attributevalue > </ attribute > </ resource > < action > < attribute attributeid = "urn:oasis:names:tc:xacml:1.0:action:action-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" > < attributevalue >any</ attributevalue > </ attribute > </ action > < environment > < attribute attributeid = "urn:Cisco:uc:1.0:triggerpointtype" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >translationpattern</ attributevalue > </ attribute > </ environment > </ request > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 | HTTP/1.1
                                                    200 OK Server:
                                                    Apache-Coyote/1.1 Connection:
                                                    Keep-Alive Keep-Alive:
                                                    timeout = 1000 max = 100 Transfer-Encoding:
                                                    chunked Date: Mon,
                                                    08 Jun 2009 16:50:21 GMT < response > < result > < decision >Permit</ decision > < obligations > < obligation fulfillon = "Permit" obligationid = "continue.simple" > < attributeassignment attributeid = "Policy:continue.simple" > < attributevalue datatype = " http://www.w3.org/2001/XMLSchema #string" > < cixml version = "1.0" > < continue ></ continue > </ cixml > </ attributevalue > </ attributeassignment > </ obligation > </ obligations > </ result > </ response > |
|---|---|