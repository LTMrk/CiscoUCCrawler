---
doc_id: developer-cisco-com-site-curri-learn-how-to-read-call-routing-request-17d16ccc03
source_url: https://developer.cisco.com/site/curri/learn/how-to/read-call-routing-request/
retrieved_at: 2026-09-07T14:10:24.520786+00:00
---

# Read Call Routing Request

Unified CM sends the eXtensible Access Control Markup Language (XACML) based routing request over
                    HTTP or HTTPS using the POST method. The XACML requests comply with XACML v2.0 standard.

It contains the following information about the call:

- Calling number

- Transformed calling number *

- Called number or dialed digits

- Transformed called number *

- Type of the triggering point

* The number that Unified CM plans to convert (transform) the calling and called number to.

In reference dial plans, the transformed value is usually the globalized number of the calling and
                    called party

Format

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

44

45

POST
                                                    < Request-URI > HTTP/1.1

Host:
                                                    < Route-Server >:< port >

Accept:
                                                    */*

Content-type:
                                                    text/xml; charset=ISO-8859-1

methodName:
                                                    < string >

User-Agent:
                                                    CiscoUCM-HttpClient/1.0

Connection:Keep-Alive

Content-Length:
                                                    < length >

< request xmlns = "urn:oasis:names:tc:xacml:2.0:context:schema:os" >

< subject subjectcategory = "urn:oasis:names:tc:xacml:1.0:subject-category:access-subject" >

< attribute attributeid = "urn:oasis:names:tc:xacml:1.0:subject:role-id" datatype = " http://www.w3.org/2001/XMLSchema #string" issuer = "requestor" >

< attributevalue >[string]</ attributevalue >

</ attribute >

< attribute attributeid = "urn:Cisco:uc:1.0:callingnumber" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >[number]</ attributevalue >

</ attribute >

< attribute attributeid = "urn:Cisco:uc:1.0:callednumber" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >[number]</ attributevalue >

</ attribute >

< attribute attributeid = "urn:Cisco:uc:1.0:transformedcgpn" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >[number]</ attributevalue >

</ attribute >

< attribute attributeid = "urn:Cisco:uc:1.0:transformedcdpn" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >[number]</ attributevalue >

</ attribute >

</ subject >

< resource >

< attribute attributeid = "urn:oasis:names:tc:xacml:1.0:resource:resource-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" >

< attributevalue >[string]</ attributevalue >

</ attribute >

</ resource >

< action >

< attribute attributeid = "urn:oasis:names:tc:xacml:1.0:action:action-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" >

< attributevalue >[URI]</ attributevalue >

</ attribute >

</ action >

< environment >

< attribute attributeid = "urn:Cisco:uc:1.0:triggerpointtype" datatype = " http://www.w3.org/2001/XMLSchema #string" >

< attributevalue >[string]</ attributevalue >

</ attribute >

</ environment >

</ request >

Learn how to Generate
                    Call Routing Response .

## Call Routing Response

Learn More

## Documentation

Developer Guide

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 | POST
                                                    < Request-URI > HTTP/1.1 Host:
                                                    < Route-Server >:< port > Accept:
                                                    */* Content-type:
                                                    text/xml; charset=ISO-8859-1 methodName:
                                                    < string > User-Agent:
                                                    CiscoUCM-HttpClient/1.0 Connection:Keep-Alive Content-Length:
                                                    < length > < request xmlns = "urn:oasis:names:tc:xacml:2.0:context:schema:os" > < subject subjectcategory = "urn:oasis:names:tc:xacml:1.0:subject-category:access-subject" > < attribute attributeid = "urn:oasis:names:tc:xacml:1.0:subject:role-id" datatype = " http://www.w3.org/2001/XMLSchema #string" issuer = "requestor" > < attributevalue >[string]</ attributevalue > </ attribute > < attribute attributeid = "urn:Cisco:uc:1.0:callingnumber" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >[number]</ attributevalue > </ attribute > < attribute attributeid = "urn:Cisco:uc:1.0:callednumber" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >[number]</ attributevalue > </ attribute > < attribute attributeid = "urn:Cisco:uc:1.0:transformedcgpn" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >[number]</ attributevalue > </ attribute > < attribute attributeid = "urn:Cisco:uc:1.0:transformedcdpn" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >[number]</ attributevalue > </ attribute > </ subject > < resource > < attribute attributeid = "urn:oasis:names:tc:xacml:1.0:resource:resource-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" > < attributevalue >[string]</ attributevalue > </ attribute > </ resource > < action > < attribute attributeid = "urn:oasis:names:tc:xacml:1.0:action:action-id" datatype = " http://www.w3.org/2001/XMLSchema #anyURI" > < attributevalue >[URI]</ attributevalue > </ attribute > </ action > < environment > < attribute attributeid = "urn:Cisco:uc:1.0:triggerpointtype" datatype = " http://www.w3.org/2001/XMLSchema #string" > < attributevalue >[string]</ attributevalue > </ attribute > </ environment > </ request > |
|---|---|