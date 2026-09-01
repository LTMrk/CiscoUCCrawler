---
doc_id: developer-cisco-com-site-extension-mobility-learn-sample-apps-2b63b6d8d1
source_url: https://developer.cisco.com/site/extension-mobility/learn/sample-apps/
retrieved_at: 2026-09-01T17:45:12.326465+00:00
---

Download the Code

# Sample App

## Introduction

This sample application demonstrates how to create an Extension Mobility web service consumer client. The following article walks through how to setup your Java project and run the sample app. This sample application logs in an end user to a device.

## Before You begin

To complete this exercise, you will need access to the following tools.

- Eclipse

- Access to a Cisco Unified Communications Manager installation

- Application user's username and password for Cisco Unified Communications Manager

- End user's username for Cisco Unified Communications Manager

- The name of a device associated to the end user and registered with Cisco Unified Communications Manager

- The name of the user-associated device profile

- Java 6

## Create a Java Project in Eclipse

We will create a new Java in Eclipse.

- In Eclipse go to, File | New | Java Project

- Give your project a name. For this sample, we will use EM .

- In the package explorer, you should see your new project, and there should be a src folder inside of your new project.

We will create code in the next section that calls the Extension Mobility login API.

## EMAPISample.java

- Click on the src folder, and choose New | Package

- Name the new package com.cisco.extensionmobility

- Right Click on the com.cisco.extensionmobility package and choose New | Class

- Name the new class EMAPISample.java

- Put the code from attached EMAPISample.java into your class

Calling the Extension Mobility API (EMAPI) login API

The following code in EMAPISample.java connects to the EMAPI service and makes the login request. You can use a similar pattern for calling any of the EMAPIs.

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

import
                                                    java.io.*;

import
                                                    java.net.*;

import
                                                    java.net.URLEncoder;

public
                                                    class EMAPISample {

public
                                                    static void main(String[] args) throws Exception {

//E/M API
                                                    service URL on Unified CM host host.com

//Note
                                                    this sample assumes the certificate for the host with subject

//name
                                                    'cucm-host.com' has been imported into the Java
                                                    keystore

//To test
                                                    with insecure connection use the URL as http://cucm-host.com:8080/emservice/EMServiceServlet

URL url
                                                    = new URL(" https://cucm-host.com:8443/emservice/EMServiceServlet ");

//Create
                                                    a java.net URLConnection object to make the HTTP request

URLConnection
                                                    conn = url.openConnection();

//setDoOutput=true
                                                    causes the URLConnection to perform a POST operation

conn.setDoOutput(true);

//The
                                                    request body will be in HTTP form encoded format

conn.setRequestProperty("Content-Type","application/x-www-form-urlencoded");

//Build
                                                    a string containing the contents of the E/M API XML request - here
                                                    'login'

String
                                                    EMRequest = "< request >< appinfo >< appid >testUser</ appid >< appcertificate >testPassword</ appcertificate ></ appinfo >";

EMRequest
                                                    += "< login >< devicename >SEP003094C25B15</ devicename >< userid >johndoe</ userid >< deviceprofile >UserDevProf</ deviceprofile >";

EMRequest
                                                    += "< exclusiveduration >< time >60</ time ></ exclusiveduration ></ login ></ request >";

//URL
                                                    encode/escape the request

EMRequest
                                                    = URLEncoder.encode(EMRequest,"UTF-8");

//Build
                                                    the complete HTTP form request body

EMRequest
                                                    = "xml="+EMRequest;

//Create
                                                    an OutputStreamWriter for the URLConnection object and make the
                                                    request

OutputStreamWriter
                                                    writer = new OutputStreamWriter(conn.getOutputStream());

writer.write(EMRequest);

writer.flush();

//Read
                                                    the response

BufferedReader
                                                    reader = new BufferedReader(new
                                                    InputStreamReader(conn.getInputStream()));

//Output
                                                    the response to the console

String
                                                    line;

while
                                                    ((line = reader.readLine()) != null) {

System.out.println(line);

}

//Cleanup
                                                    the stream objects

writer.close();

reader.close();

}

}

## Running the Sample Project

After you have added the code to EMAPISample.java in your project, you are ready to run the sample and connect to your Cisco Unified CM. You will need to replace the following information in the code above:

- The IP address or hostname for your Cisco Unified CM

- The application user's user id and password .

- The end user's user id .

- The device name for a phone registered with the Cisco Unified CM.

- The user-associated device profile name

Adding the Cisco Unified CM SSL certificate to your keystore

EMAPI uses HTTPS, so you need to install the UC applications SSL certificate into your local keystore in order to run the sample app.

Download the Cisco Unified CM SSL Certificate

You can download the certificate from the UC manager using your browser. Here are the steps to do so using Firefox.

- In Firefox, go to https://<cucm-host>:8443

- Login with the Unified CM admin credentials.

- Click on the lock.

- Click more information .

- Click View Certificate

- Click Details

- Click Export .

- Save the certificate into a known place on your local machine

Add the certificate to your java keystore

You can run the following command from the command line to add the certificate file to your local keystore.

?

1

2

$
                                                    JAVA_HOME/bin/keytool -import -alias < some descriptive
                                                    name> -file < certificate file>
                                                    -keystore < path to keystore>

For Windows/Linux The keystore is located here: C:/Java/jre/lib/security/cacerts

For Mac OS The keystore is located here: $JAVA_HOME/lib/security/jssecacerts and JAVA_HOME is located here: /System/Library/Frameworks/JavaVM.framework/Versions/<your version>/Home

Run the Sample Project

If you encounter issues running the sample project, you may want to examine the Extension Mobility logs from Cisco Unified Communications Manager.

## Next Steps

- You can expand the sample and experiment by calling additional Extension Mobility APIs.

## Login Request

View a sample login request

Learn More

Visit the Extension Mobility API Developer Forums to ask questions and interact with other
                    developers.

Forums

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 | import
                                                    java.io.*; import
                                                    java.net.*; import
                                                    java.net.URLEncoder; public
                                                    class EMAPISample { public
                                                    static void main(String[] args) throws Exception { //E/M API
                                                    service URL on Unified CM host host.com //Note
                                                    this sample assumes the certificate for the host with subject //name
                                                    'cucm-host.com' has been imported into the Java
                                                    keystore //To test
                                                    with insecure connection use the URL as http://cucm-host.com:8080/emservice/EMServiceServlet URL url
                                                    = new URL(" https://cucm-host.com:8443/emservice/EMServiceServlet "); //Create
                                                    a java.net URLConnection object to make the HTTP request URLConnection
                                                    conn = url.openConnection(); //setDoOutput=true
                                                    causes the URLConnection to perform a POST operation conn.setDoOutput(true); //The
                                                    request body will be in HTTP form encoded format conn.setRequestProperty("Content-Type","application/x-www-form-urlencoded"); //Build
                                                    a string containing the contents of the E/M API XML request - here
                                                    'login' String
                                                    EMRequest = "< request >< appinfo >< appid >testUser</ appid >< appcertificate >testPassword</ appcertificate ></ appinfo >"; EMRequest
                                                    += "< login >< devicename >SEP003094C25B15</ devicename >< userid >johndoe</ userid >< deviceprofile >UserDevProf</ deviceprofile >"; EMRequest
                                                    += "< exclusiveduration >< time >60</ time ></ exclusiveduration ></ login ></ request >"; //URL
                                                    encode/escape the request EMRequest
                                                    = URLEncoder.encode(EMRequest,"UTF-8"); //Build
                                                    the complete HTTP form request body EMRequest
                                                    = "xml="+EMRequest; //Create
                                                    an OutputStreamWriter for the URLConnection object and make the
                                                    request OutputStreamWriter
                                                    writer = new OutputStreamWriter(conn.getOutputStream()); writer.write(EMRequest); writer.flush(); //Read
                                                    the response BufferedReader
                                                    reader = new BufferedReader(new
                                                    InputStreamReader(conn.getInputStream())); //Output
                                                    the response to the console String
                                                    line; while
                                                    ((line = reader.readLine()) != null) { System.out.println(line); } //Cleanup
                                                    the stream objects writer.close(); reader.close(); } } |
|---|---|

| 1 2 | $
                                                    JAVA_HOME/bin/keytool -import -alias < some descriptive
                                                    name> -file < certificate file>
                                                    -keystore < path to keystore> |
|---|---|