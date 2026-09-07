---
doc_id: developer-cisco-com-site-user-data-services-learn-how-to-uds-hello-world-aca233a649
source_url: https://developer.cisco.com/site/user-data-services/learn/how-to/uds-hello-world/
retrieved_at: 2026-09-07T14:09:54.493172+00:00
---

# UDS "Hello World"

To get started with using UDS, lets look at an API request for a simple example.

An API request consists of an HTTP method and a URI. The HTTP method designates the type of activity to perform. Operations use standard HTTP methods to retrieve, update, create, and delete resources or data. The URI identifies the resource or resources that the request targets, and can include various parameters to further refine the operation.

Most API requests require that an HTTP Accept header be included. In addition, PUT and POST requests require an HTTP Content-Type header. The Accept and Content-type header can specify xml.

To invoke an API operation, you send an HTTP request from any client that supports the creation of such a request to a Cisco Unified Communications Manager (CUCM) server.

Example Scenario: We want to get a user's settings and preferences.

For this task, we need to make 1 REST API request to the server. Visit explore the UDS APIs to see exactly how this is done.

To get the list of servers in XML format, make a HTTP GET request with the Accept header set to "application/xml".  You'll receive a response in XML format similar to the following:

Request GET https://{host}:8443/cucm-uds/user/{userId} Accept: application/xml

# Request

# Response

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

46

47

48

49

< user version = "{version}" uri = "https:­//{host}:8443/cucm-uds/user/{userId}" >

< id >{userPkid}</ id >

< userName >{userId}</ userName >

< firstName >firstName</ firstName >

< lastName >lastName</ lastName >

< middleName >middleName</ middleName >

< nickName >nickName</ nickName >

< phoneNumber >8134567</ phoneNumber >

< homeNumber >8134455</ homeNumber >

< mobileNumber >8131111</ mobileNumber >

< mobileConnect >true|false</ mobileConnect >

< userLocale uri = "https:­//{host}:8443/cucm-uds/installedLocales" value = "0" appliesToAllDevices = "true|false" >English, United States</ userLocale >

< email >someone@example.com</ email >

< directoryUri >someone@example.com</ directoryUri >

< msUri >someone@example.com</ msUri >

< department >department</ department >

< manager >manager</ manager >

< title >title</ title >

< pager >8137777</ pager >

< primaryExtension uri = "https:­//{host}:8443/cucm-uds/user/{userId}/userExtension/{extensionPkid}" >

< description >extensionDescription</ description >

< directoryNumber >81134953</ directoryNumber >

< callForwardAllDestination >

< sendToVoiceMailPilotNumber >true|false</ sendToVoiceMailPilotNumber >

< destination >4352134</ destination >

</ callForwardAllDestination >

< messageWaitingVisualAlert >true|false</ messageWaitingVisualAlert >

< messageWaitingVisualAlertPreference appliesToAllLineAppearances = "true|false" value = "" >Use System Default</ messageWaitingVisualAlertPreference >

< messageWaitingAudibleAlertPreference appliesToAllLineAppearances = "true|false" value = "1" >On</ messageWaitingAudibleAlertPreference >

< onACallRingPreference appliesToAllLineAppearances = "true|false" value = "0" >Use System Default</ onACallRingPreference >

< notOnACallRingPreference appliesToAllLineAppearances = "true|false" value = "0" >Use System Default</ notOnACallRingPrefence >

< voiceMailPilotNumber >5555</ voiceMailPilotNumber >

< label appliesToAllLineAppearances = "true|false" >label</ label >

< logMissedCalls appliesToAllLineAppearances = "true|false" >true|false</ logMissedCalls >

</ primaryExtension >

< accountType useLdapAuth = "true|false" >ldap|local</ accountType >

< homeCluster enableCalendarPresence = "true|false" enableImAndPresence = "true|false" >true|false</ homeCluster >

< devices uri = "https:­//{host}:8443/cucm-uds/user/{userId}/devices" />

< credentials uri = "https:­//{host}:8443/cucm-uds/user/{userId}/credentials" />

< userExtensions uri = "https:­//{host}:8443/cucm-uds/user/{userId}/userExtensions" />

< enableDoNotDisturb appliesToAllDevices = "true|false" >true|false</ enableDoNotDisturb >

< callForwardAllDestination appliesToAllExtensions = "true|false" >

< sendToVoiceMailPilotNumber >true|false</ sendToVoiceMailPilotNumber >

< destination >43521</ destination >

</ callForwardAllDestination >

< speedDials uri = "https:­//{host}:8443/cucm-uds/user/{userId}/speedDials" />

< serviceProfile uri = "http:­//{host}:6970/SPDefault.cnf.xml" />

</ user >

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 | < user version = "{version}" uri = "https:­//{host}:8443/cucm-uds/user/{userId}" > < id >{userPkid}</ id > < userName >{userId}</ userName > < firstName >firstName</ firstName > < lastName >lastName</ lastName > < middleName >middleName</ middleName > < nickName >nickName</ nickName > < phoneNumber >8134567</ phoneNumber > < homeNumber >8134455</ homeNumber > < mobileNumber >8131111</ mobileNumber > < mobileConnect >true\|false</ mobileConnect > < userLocale uri = "https:­//{host}:8443/cucm-uds/installedLocales" value = "0" appliesToAllDevices = "true\|false" >English, United States</ userLocale > < email >someone@example.com</ email > < directoryUri >someone@example.com</ directoryUri > < msUri >someone@example.com</ msUri > < department >department</ department > < manager >manager</ manager > < title >title</ title > < pager >8137777</ pager > < primaryExtension uri = "https:­//{host}:8443/cucm-uds/user/{userId}/userExtension/{extensionPkid}" > < description >extensionDescription</ description > < directoryNumber >81134953</ directoryNumber > < callForwardAllDestination > < sendToVoiceMailPilotNumber >true\|false</ sendToVoiceMailPilotNumber > < destination >4352134</ destination > </ callForwardAllDestination > < messageWaitingVisualAlert >true\|false</ messageWaitingVisualAlert > < messageWaitingVisualAlertPreference appliesToAllLineAppearances = "true\|false" value = "" >Use System Default</ messageWaitingVisualAlertPreference > < messageWaitingAudibleAlertPreference appliesToAllLineAppearances = "true\|false" value = "1" >On</ messageWaitingAudibleAlertPreference > < onACallRingPreference appliesToAllLineAppearances = "true\|false" value = "0" >Use System Default</ onACallRingPreference > < notOnACallRingPreference appliesToAllLineAppearances = "true\|false" value = "0" >Use System Default</ notOnACallRingPrefence > < voiceMailPilotNumber >5555</ voiceMailPilotNumber > < label appliesToAllLineAppearances = "true\|false" >label</ label > < logMissedCalls appliesToAllLineAppearances = "true\|false" >true\|false</ logMissedCalls > </ primaryExtension > < accountType useLdapAuth = "true\|false" >ldap\|local</ accountType > < homeCluster enableCalendarPresence = "true\|false" enableImAndPresence = "true\|false" >true\|false</ homeCluster > < devices uri = "https:­//{host}:8443/cucm-uds/user/{userId}/devices" /> < credentials uri = "https:­//{host}:8443/cucm-uds/user/{userId}/credentials" /> < userExtensions uri = "https:­//{host}:8443/cucm-uds/user/{userId}/userExtensions" /> < enableDoNotDisturb appliesToAllDevices = "true\|false" >true\|false</ enableDoNotDisturb > < callForwardAllDestination appliesToAllExtensions = "true\|false" > < sendToVoiceMailPilotNumber >true\|false</ sendToVoiceMailPilotNumber > < destination >43521</ destination > </ callForwardAllDestination > < speedDials uri = "https:­//{host}:8443/cucm-uds/user/{userId}/speedDials" /> < serviceProfile uri = "http:­//{host}:6970/SPDefault.cnf.xml" /> </ user > |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|