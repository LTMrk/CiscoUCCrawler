---
doc_id: developer-cisco-com-site-webdialer-learn-sample-apps-soap-hello-world-202a9e2dcc
source_url: https://developer.cisco.com/site/webdialer/learn/sample-apps/soap-hello-world/
retrieved_at: 2026-09-01T17:49:57.433177+00:00
---

# SOAP Sample App

The Cisco WebDialer SOAP API gives you more flexibility when developing applications for user
                    specific needs. The SOAP interface of Cisco WebDialer lets you be creative with your application
                    design to build a better user experience. For example, if you would like to list your employees by
                    name, or maybe offer a search dialog box that searches for users by name, you could use the
                    getPrimaryLine API to return the employee’s phone number or extension.

The following example uses the getPrimaryLine API to retrieve a user’s phone
                    extension. It takes two input parameters (user and password), and returns a string (the user’s
                    extension).

There are only a few things you need to know to make this API call work:

- The name/IP address of your Cisco Unified Communications Manager (Unified CM) server that is
                        hosting your Cisco WebDialer service.

- The username and password of the user whose extension you want to retrieve.

- The format of the SOAP message you are going to construct and send to the Cisco WebDialer
                        service.

- The format of the SOAP message you will receive as a response to your request.

The steps you will perform are:

- Determine which server you are going to send the getPrimaryLine request to.

- Determine the username and password needed to use the getPrimaryLine credential request
                        fields.

- Load up the parameters into a well-formed SOAP envelope

- Send the SOAP request off to the server you identified in Step 1

- Retrieve and parse the SOAP response you will receive, extracting the getPrimaryLineReturn value
                        as your user’s primary line string.

That’s it!

Steps 1, 2, and 3 will result in a SOAP request ready to send that will look like
                    this:

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

<? xml version = "1.0" encoding = "UTF-8" ?>

< soapenv:Envelope xmlns:xsi = " http://www.w3.org/2001/XMLSchema-instance " xmlns:xsd = " http://www.w3.org/2001/XMLSchema " xmlns:soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns:urn = "urn:WD70" >

< soapenv:Header />

< soapenv:Body >

< urn:getPrimaryLine soapenv:encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " >

< in0 xsi:type = "urn:Credential" >

< userID xsi:type = "xsd:string" >bill</ userID >

< password xsi:type = "xsd:string" >123</ password >

</ in0 >

</ urn:getPrimaryLine >

</ soapenv:Body >

</ soapenv:Envelope >

Step 4 is where you will make the call to Unified CM in the following format:

https://<server>:8443/webdialer/services/WebdialerSoapService70

where <server> specifies the IP address of the Unified CM running the Cisco WebDialer
                    service.

Step 5 results in the SOAP response you’ve been waiting for, bringing you the
                    primary extension of the user you identified in your request:

1

2

3

4

5

6

7

8

<? xml version = "1.0" encoding = "UTF-8" ?>

< soapenv:Envelope xmlns:soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns:xsd = " http://www.w3.org/2001/XMLSchema " xmlns:xsi = " http://www.w3.org/2001/XMLSchema-instance " >

< soapenv:Body >

< ns1:getPrimaryLineResponse soapenv:encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xmlns:ns1 = "urn:WD70" >

< getPrimaryLineReturn xsi:type = "soapenc:string" xmlns:soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " >1002</ getPrimaryLineReturn >

</ ns1:getPrimaryLineResponse >

</ soapenv:Body >

</ soapenv:Envelope >

Now just extract the value of getPrimaryLineReturn , and you’re done!

You can follow these 5 steps using any language that allows you to construct SOAP envelopes and send
                    them via https.

| 1 2 3 4 5 6 7 8 9 10 11 12 | <? xml version = "1.0" encoding = "UTF-8" ?> < soapenv:Envelope xmlns:xsi = " http://www.w3.org/2001/XMLSchema-instance " xmlns:xsd = " http://www.w3.org/2001/XMLSchema " xmlns:soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns:urn = "urn:WD70" > < soapenv:Header /> < soapenv:Body > < urn:getPrimaryLine soapenv:encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " > < in0 xsi:type = "urn:Credential" > < userID xsi:type = "xsd:string" >bill</ userID > < password xsi:type = "xsd:string" >123</ password > </ in0 > </ urn:getPrimaryLine > </ soapenv:Body > </ soapenv:Envelope > |
|---|---|

| 1 2 3 4 5 6 7 8 | <? xml version = "1.0" encoding = "UTF-8" ?> < soapenv:Envelope xmlns:soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns:xsd = " http://www.w3.org/2001/XMLSchema " xmlns:xsi = " http://www.w3.org/2001/XMLSchema-instance " > < soapenv:Body > < ns1:getPrimaryLineResponse soapenv:encodingStyle = " http://schemas.xmlsoap.org/soap/encoding/ " xmlns:ns1 = "urn:WD70" > < getPrimaryLineReturn xsi:type = "soapenc:string" xmlns:soapenc = " http://schemas.xmlsoap.org/soap/encoding/ " >1002</ getPrimaryLineReturn > </ ns1:getPrimaryLineResponse > </ soapenv:Body > </ soapenv:Envelope > |
|---|---|