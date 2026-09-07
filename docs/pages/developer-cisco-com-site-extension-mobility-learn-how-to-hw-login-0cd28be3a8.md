---
doc_id: developer-cisco-com-site-extension-mobility-learn-how-to-hw-login-0cd28be3a8
source_url: https://developer.cisco.com/site/extension-mobility/learn/how-to/hw-login/
retrieved_at: 2026-09-07T14:15:15.751105+00:00
---

# "Hello World" Login

The Login operation logs in a single user using the specified device profile. The following example logs in userID "john" to device SEP003094C25B15 using the user-associated device profile UserDevProf:

When creating the request body, it is recommended to first build in XML format and then encode the XML before sending to the CUCM server. The first part of the example shows the XML unencoded and the second part of the example shows the XML encoded.

# Request

POST /emservice/EMServiceServlet Content-Type: application/x-www-form-urlencoded Unencoded

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

< request >

< appinfo >

< appid >appid</ appid >

< appcertificate >apppasswd</ appcertificate >

</ appinfo >

< login >

< devicename >SEP003094C25B15</ devicename >

< userid >john</ userid >

< deviceprofile >UserDevProf</ deviceprofile >

< exclusiveduration >

< time >60</ time >

</ exclusiveduration >

</ login >

</ request >

Encoded

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

xml=%3Crequest%3E

%3CappInfo%3E

%3CappID%3Eappid%3C/appID%3E

%3CappCertificate%3Eapppasswd%3C/appCertificate%3E

%3C/appInfo%3E

%3Clogin%3E

%3CdeviceName%3ESEP003094C25B15%3C/deviceName%3E

%3CuserID%3Ejohn%3C/userID%3E

%3CdeviceProfile%3EUserDevProf%3C/deviceProfile%3E

%3CexclusiveDuration%3E

%3Ctime%3E60%3C/time%3E

%3C/exclusiveDuration%3E

%3C/login%3E

%3C/request%3E

# Success Response

?

1

2

3

< response >

< success />

</ response >

## Login Request

View a sample logout request

Learn More

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | < request > < appinfo > < appid >appid</ appid > < appcertificate >apppasswd</ appcertificate > </ appinfo > < login > < devicename >SEP003094C25B15</ devicename > < userid >john</ userid > < deviceprofile >UserDevProf</ deviceprofile > < exclusiveduration > < time >60</ time > </ exclusiveduration > </ login > </ request > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | xml=%3Crequest%3E %3CappInfo%3E %3CappID%3Eappid%3C/appID%3E %3CappCertificate%3Eapppasswd%3C/appCertificate%3E %3C/appInfo%3E %3Clogin%3E %3CdeviceName%3ESEP003094C25B15%3C/deviceName%3E %3CuserID%3Ejohn%3C/userID%3E %3CdeviceProfile%3EUserDevProf%3C/deviceProfile%3E %3CexclusiveDuration%3E %3Ctime%3E60%3C/time%3E %3C/exclusiveDuration%3E %3C/login%3E %3C/request%3E |
|---|---|

| 1 2 3 | < response > < success /> </ response > |
|---|---|