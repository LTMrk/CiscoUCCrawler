---
doc_id: developer-cisco-com-site-im-and-presence-documents-developer-cookbook-v10-5-edb8f041c5
source_url: https://developer.cisco.com/site/im-and-presence/documents/developer-cookbook-v10-5/
retrieved_at: 2026-09-01T17:46:09.887616+00:00
---

# IM and Presence Developer Cookbook 10.5(0)

# Introduction

Presence exchange and user preference information (for example, presence rules and contact list) on Cisco
                Unified CM IM and Presence have been made available to Third Party Applications through two web
                services, the Presence Web Service and the Client Configuration Web Service.

The Presence Web Service provides the functionality to manage user presence on a Cisco Unified CM IM and
                Presence server. Users can set their own presence states and receive notifications of changes to the
                presence states of their contacts. The client application registers a HTTP endpoint and sets up a
                subscription for presence notifications.

The Client Configuration Web Service is an interface that allows client applications to manage user
                preference information on Cisco Unified CM IM and Presence. The Client Configuration Web Service
                provides the functionality to provision information such as contacts, contact groups, presence rules,
                access control lists, and calendaring options.

Both these interfaces are described in detail in the Developer Guide for Cisco Unified CM IM and
                Presence. This document describes what methods are in the API, and the contents of method requests and
                responses.

Note: The term Third Party Interface is used throughout this document and
                refers to the combined functionality provided by both web services, the Presence Web Service and the
                Client Configuration Web Service.

A Reference Application is provided with the web services to demonstrate the functionality opened up by
                the web services. The objective of the Reference Application is not to be of production quality, but to
                aid developer understanding of how best to use the interfaces. The Reference Application also provides a
                method for testing that the web services have been correctly set up and are fully operational.

This document describes the functionality of the Reference Application and outlines how it is built and
                configured. It also describes implementation, includes source code examples, and provides guidelines on
                using the web services.

Note: The Presence Web Service can also be accessed over REST. Cisco sees REST as being
                the interface mechanism of choice in the future. This functionality is an early adopter REST interface
                and future development and enhancements in the interface mean that compatibility with previous releases
                of the API is not guaranteed.

## WSDL Definitions

The WSDL definition of the SOAP-based web services can be found (on a Cisco Unified CM IM and Presence
                server) at:

Presence Web Service (HTTP): http://<cup-hostname>:8082/presence-service/soap?wsdl

Presence Web Service (HTTPS): https://<cup-hostname>:8083/presence-service/soap?wsdl

Client Configuration Web Service (HTTPS) IPv4: https://<cup-hostname>:8443/EPASSoap/service/v70?wsdl

The Client Configuration WSDL uses two .xsd files. These files are located at:

- https://cup-hostname:8443/EPASSoap/presence-rules.xsd - https://cup-hostname:8443/EPASSoap/ epas-soap-interface.xsd

Client Configuration Web Service (HTTPS) (IPv6 support added in Cisco Unified CM IM and Presence
                    10.5): (https://[cup-V6 address]:443/EPASSoap/service/v70?wsdl

The Client Configuration WSDL uses two .xsd files. These files are located at:

- (https://[cup-V6 address]:443/EPASSoap/presence-rules.xsd - (https://[cup-V6 address]:443EPASSoap/ epas-soap-interface.xsd

Note: The WSDL will only load in Mozilla Firefox (non-version specific) or Microsoft
                Internet Explorer v7.X and later.

## Terminology

- Send SOAP messages

- Receive and process SOAP messages

- Create implementation client stub classes using WSDL

### References

AJAX Programming http://en.wikipedia.org/wiki/Ajax_(programming )

Apache Struts http://struts.apache.org/

Axis http://ws.apache.org/axis2/index.html

Eclipse Development Platform http://www.eclipse.org/

Jakarta Commons HTTP Client library http://hc.apache.org/httpclient-3.x/

RFC 3863 - Presence Information Data Format (PIDF)

RFC4480 - RPID: Rich Presence Extensions to the Presence Information Data Format (PIDF)

# Installing the Reference Application

This section describes how to install and configure the Reference Application. The Reference Application
                is delivered as a J2EE Web Application. The configuration information for the Reference Application is
                stored in a web.xml file.

The Reference Application can be downloaded as an Eclipse Project. This download includes a WAR file
                (refApp.war file) in the build\ear folder. If you have not been provided with this file, contact your
                Cisco representative.

## Requirements

This section assumes that you are running Apache Tomcat version 6.X and have Java2SE version 6. To
                download this software, go to http://tomcat.apache.org .

This section also assumes that you have created an application user for the Reference Application on
                Cisco Unified Communications Manager or Cisco Unified CM IM and Presence server, and that you have added
                your end users to the Cisco Unified CM IM and Presence server.

For Cisco Unified CM IM and Presence releases before 10.0.1, the application user is created in the Cisco
                Unified CM IM and Presence Administration GUI via User Management > Application User >
                    New .

For Cisco Unified CM IM and Presence releases 10.0.1 and later, the application user is created in the
                Cisco Unified Communications Manager Administration GUI via User Management > Application
                    User > New .

Note: The Application User must be added to the Admin-3rd Party API Group for use with the 3rd Party API.

## Copying the WAR File

Procedure:

- Copy the refApp.war file into the <CATALINA_HOME>\webapps folder, where CATALINA_HOME is the
                    Tomcat installation directory.

- Start and stop Tomcat. The following directory is created: <CATALINA_HOME>\webapps\refApp

- Edit the servlet parameters in the <CATALINA_HOME>\webapps\refApp\WEB-INF\web.xml file as
                    described in Configuring the Web XML File .

- Restart Tomcat.

## Configuring the Web XML File

On application startup, certain servlets are invoked to configure the Reference Application. You must
                define parameters for these servlets during installation. The servlets are configured in the web.xml
                file.

##### securityConfig Servlet

The securityConfig servlet is used to define the security configuration for the Reference Application.
                The configuration parameters are described in the following table.

##### axisConfig Servlet

The axisConfig servlet is used to point the Reference Application to the REST services on Cisco Unified
                CM IM and Presence. The configuration parameters are described in the following table. The parameters cup_presence_path and cup_config_soap_path must be defined as part of the Reference
                Application installation. The remaining parameter values can remain as the default values.

##### axisConfig parameters

action field in the Content Type header

```
Content-Type: application/soap+xml;
charset=UTF-8;
action="urn:cisco:epas:soap/login";
```

Note: SOAP 1.2 messages have an action field in the Content Type header. Refer to the
                right hand panel for an example. Disabling the parameters cup_config_disablesoapaction and cup_presence_disablesoapaction removes the action from the header.

##### restConfig Servlet

The restConfig servlet is used to point the Reference Application to the REST-based Presence Web Service.
                The configuration parameters are described in the following table. The cup_rest_presence_path and
                cup_configsoap_path parameters must be defined as part of the Reference Application installation.

restConfig parameters

##### genericConfig Servlet

The genericConfig servlet has configuration parameters common to both the REST and SOAP interfaces. The
                relevant parameters are described in the following table.

- com.cisco.cup.webservices.refapp.handler.rest.RestHandlerFactory

- com.cisco.cup.webservices.refapp.handler.axis.AxisHandlerFactory

### Verify Installation

To verify that the Reference Application has installed correctly, go to http://localhost: /refApp in your browser, assuming the Reference Application is installed on your local machine. The login page
                for the Reference Application is displayed.

### Debugging

To help debug any Reference Application installation problems, check the log file(s) in <CATALINA_HOME>\bin\logs\refApp.log*.

## Security Configuration

- Downloading the Certificates

- Create a Keystore and Import the
                    Certificates

- Configure the Reference
                    Application to Use the Keystore

This section describes how to configure the Reference Application to use secure transport (TLS v1)
                between the Application server and the Cisco Unified CM IM and Presence server. The process involves
                downloading certificates from Cisco Unified CM IM and Presence and creating a keystore for the
                certificates. The following figure shows the connections between the Application server, hosting the
                Reference Application, and the Cisco Unified CM IM and Presence server.

Note: The security procedures described in this section must be repeated for any Cisco
                Unified CM IM and Presence server that you wish to connect to the Reference Application.

### Downloading the Certificates

The following certificates need to be downloaded from the Cisco Unified CM IM and Presence server:

- Presence Interface (cup.der)

- Configuration Interface (tomcat.der)

Procedure:

Create the local directory, for example if using Windows, create C:\certs.

Login to the Cisco Unified CM IM and Presence Operating System Administration using your
                    administrator username and password.

Navigate to Security > Certificate Management .

Click Find . The list of certificates is displayed.

Click on the link cup.der and click Download .

Save the certificate cup.der to the local directory C:\certs.

Navigate back to the Certificate Find/List page, click on the link tomcat.der and click Download .

Save the certificate tomcat.der to the local directory C:\certs.

### Create a Keystore and Import the Certificates

A Java keystore is used to store trusted certificates for a Java application. A Java keystore for the
                Reference Application must be set up.

Procedure:

On the Application server (where the Reference Application is installed), a Java Runtime
                    Environment should be installed for the J2EE container used. Ensure that the java bin directory is
                    in the path environment variable. Run the command keytool from the command
                    prompt/shell and a list of commands print out as help information.

Open a command prompt/shell on the Application server, navigate to c:\certs, and run the
                    following command using the parameter definitions in the import keytool parameter descriptions table below: keytool -import -alias cup -file cup.der -keystore c:\certs\refapp.keystore -storepass
                        ciscoRefApp

When asked if you want to trust the certificate, enter Yes .

From the command prompt/shell on the Application server, run the following command, using the
                    parameter definitions in the import keytool parameter
                        descriptions table below: keytool -import -alias tomcat -file tomcat.der -keystore C:\certs\refapp.keystore -storepass
                        ciscoRefApp

When prompted to trust the certificate, enter Yes .

To ensure that the certificates have been imported (from the C:\certs\ directory), print out the
                    contents of the Java keystore using the command: keytool -list -keystore refapp.keystore -storepass ciscoRefApp

Note: When running the keytool –import command, a new Java
                keystore will be created with the specified filename and password if this keystore does not already
                exist.

### Configure the Reference Application to Use
                the Keystore

This section describes how to configure the Reference Application to use the newly created Java
                keystore.

Procedure:

Open the <TOMCAT_HOME>\webapps\refApp\WEB-INF\web.xml file for the Reference
                    Application.

Edit the java_keystore_file property so that it contains the full path to the Java keystore
                    created in the previous section.

Edit the java_keystore_password property so that it contains the password used when creating the
                    Java keystore in the previous section.

Ensure the URLs configured in the following web.xml properties have a https:// prefix and use the ports listed below:

axisConfig Servlet

restConfig Servlet

Below are example values for a Cisco Unified CM IM and Presence server with hostname cupserver:

- Restart Tomcat to ensure that all properties are updated.

- To verify that the certificates were downloaded correctly and the Reference Application is using
                    HTTPS, check the refApp.log in the Tomcat/logs folder for the following:

- 200 OK message from https://<IP>:8443/EPASSoapDev/service

- 200 OK message from https://<IPv6>:443/EPASSoapDev/service

- 200 OK message from https://<IP>:8083/presence-service/soap

- 200 OK message from https://<IP>:8083/presence-service

# Using the Reference Application GUI

This section describes the functions that are available using the Reference Application GUI. There are
                two sets of screens available in the Reference Application:

- User Presence Application

- Eventing Tutorial

To access the Reference Application GUI, in your browser go to http://localhost: /refApp , assuming the Reference Application is installed on the local machine. The login page for the
                Reference Application is displayed.

User Presence Application

These screens use a subset of the Client Configuration Web Service functionality in conjunction with the
                Presence Web Service. The following operations can be performed:

- Maintain a contact list

- View presence of your contacts

- Set a user’s presence

- View the devices a contact is using (an example of rich presence)

- Block other users from seeing your presence

Eventing Tutorial

These screens provide a tutorial on using the presence notification feature provided by the Presence Web
                Service. It walks the user through setting up and tearing down subscriptions, and viewing notifications
                associated with a subscription.

You select the set of screens you wish to view at login. From the login screen select the screen set,
                enter your user ID, and press the login button.

## Viewing Presence

On logging in to the User Presence Application, you are presented with a management screen that allows
                you to set your presence state and manage your contact list.

You can set your own presence by selecting a presence state from the drop down menu. The following
                presence states are possible:

- Available

- Busy (translated to Away on the server)

- DND (Do Not Disturb)

- Away

- Unavailable

- Vacation (translated to Away on the server)

When users log in, their presence states are automatically set to Available. When users log out, their
                presence states are set to Unavailable.

You can also view the presence state of your contacts from the management screen. An icon displayed to
                the right of the contact name indicates the presence state. The color code for showing presence is:

- Green - Available

- Red - Away, DND

- Grey - Unavailable

If the presence state is none of the above, the presence icon displayed is a grey question mark.

## Managing Groups

You can manage your contact groups by clicking on the My Groups link on the Presence
                Management screen.

The following group management functions are available:

- Modify a group name – In the Select Group drop-down menu, select the group
                    you wish to modify. Enter a new group name and press the Modify button.

- Delete a group – In the Select Group drop-down menu, select the group you
                    wish to delete. Press the Delete button.

## Managing Contacts

You can manage the contacts in a group by clicking on the group name link, for example General in Group under Manage Contacts . The following
                contact management functions are available:

- Add a Contact - In the Select Contact drop-down menu, select New .
                    Enter a User ID , Domain , and Nickname , and press
                    the Add option. This contact (user) is provisioned in Cisco Unified CM IM and
                    Presence.

- Modify a contact - In the Select Contact drop-down menu, select the contact you
                    wish to modify. You cannot modify the User ID or the Domain associated with a contact. The NickName of the contact can be changed, and the
                    contact can be moved to a new or existing group using the Group dropdown. To move
                    the contact to a new Group, select the Other option in the Group
                        drop down.

- Delete a Contact - In the Select Contact drop-down menu, select the contact you
                    wish to delete. Press the Delete button.

The following screen shows the user moving the contact devtest1 to a New Group – Friends. This is
                done by selecting Other in the Group dropdown and then updating the New Group text field.

## Viewing a Contact’s Presence Details

You can view more information on a contact’s presence by clicking on a contact name. This screen
                demonstrates retrieving Rich Presence in PIDF format from Cisco Unified CM IM and Presence. The
                following presence information is available for a contact:

- The overall presence state of the contact.

- The device(s) the contact is using.

- The privacy status defined for the contact. This facility allows you to block the contact from
                    viewing your presence state.

## Using the Eventing Tutorial

This tutorial demonstrates to a developer the steps involved in setting up the presence notification
                feature offered by the Presence Web Service.

On logging in to the Eventing Tutorial, you are presented with the notification tutorial screen. This
                screen allows you to perform the following functions:

- Register the endpoint that is configured in the web.xml file. The end point ID is then displayed on
                    the screen.

- Subscribe to the presence of some or all of the contact list. You can only subscribe to the presence
                    of contacts that have been added to the Cisco Unified CM IM and Presence database.

- Remove contact(s) from the subscription.

- Unregister an endpoint.

All presence notifications for a subscription are shown in the Notifications text area.
                To generate a notification, log in to another instance of the Reference Application as one of the
                contacts in the subscription. When a subscription is created, a presence notification is immediately
                generated by Cisco Unified CM IM and Presence.

All of the requests on this screen, with the exception of logout, are serviced by the com.cisco.cup.webservices.refapp.action.EventingAction class.

# Building the Reference Application

The Reference Application is available as an Eclipse Project. This section describes the content of the
                Project and provides information on building the Reference Application.

See Appendix 3 for information on importing the Reference Application into
                Eclipse.

The Project contains the following items:

## data-src Folder

The data-src folder contains the following packages:

## build Folder

The build folder contains two ant scripts:

- build.xml

- deploy.xml

The WAR file for the Reference Application is located in the build\ear\refApp.war.

## web folder

The web folder contains the following subfolders:

## clientstubs Folder

The clientstubs folder contains the following files:

The WSDL definition for the Client Configuration Web Service is found at:

https://cup:8443/EPASSoap/service?wsdl

The WSDL definition for the Presence Web Service is found at

https://cup:8083/presence-service/soap?wsdl

Note: It is recommended that you always get the latest WSDL from the above URLs for any
                application development.

## Build.xml Script

The build.xml script, located in the build folder, contains the following targets of note: the all target, the stubs target, and the doc tag.

The default tag, all , builds the application into a RefApp.war file, and places it in the
                build/ear folder. The stubs target is used to generate axis client stubs for interacting with
                the Third Party web services soap interfaces. This target calls the generateClientStubs.sh script in the
                clientstubs folder, which creates two jars (client-config.jar and presence.jar) in the lib directory.

Axis2 provides several options when it comes to mapping WSDL to objects when generating clients. The
                model used in the Reference Application is XMLBeans which has a powerful schema compiler. However, be
                aware that it generates a huge number of files. The stub generation build files are included only as an
                example and require an Axis2 installation.

Note: Generating stubs has only been tested on a Linux platform.

The doc tag generates the Javadoc documentation associated with the Reference Application.

In addition, another Ant file, deploy.xml, can be used to deploy the Reference Application to a Tomcat
                Server. To run this an environment variable, TOMCAT_HOME, needs to be set. The Ant script simply copies
                the RefApp.war to a webapps folder in Tomcat.

# Reference Application Structure

## Architecture

An overview of the Reference Application architecture is outlined in the following image. The Reference
                Application is written as a Web Application following a three-tiered-architecture.

The Presentation Layer (web application) is written using HTML. The HTML pages are generated by JSPs.
                JavaScript and AJAX are embedded in the HTML pages to make UI behavior more dynamic.

The Middle Tier contains the Reference Application business logic. There are two layers to the middle
                tier, a set of Struts action classes that service HTTP requests from Reference Application clients, and
                a set of handler classes that interact with the Third Party Web Services on Cisco Unified CM IM and
                Presence. As mentioned previously there are two implementations of the handler layer, REST and Axis
                SOAP. These layers make calls to the REST and SOAP Web Services provided by Cisco Unified CM IM and
                Presence.

There are two interfaces exposed on Cisco Unified CM IM and Presence, a SOAP interface which provides
                Presence and Configuration services and a REST interface, which provides Presence capabilities
                only.

Note: The Presentation Layer (web application) has been tested on Mozilla Firefox 2 and
                Internet Explorer 6.0. The Reference Application is deployed as a WAR file to a Servlet Engine, such as
                Tomcat. The Java code that makes up the Reference Application uses JDK 5.0.

## Web Application

The JSPs that make up the Reference Application User Interface are described in the following table. The
                JSP files are located in the web/pages folder in the Eclipse project, with the exception of index.jsp
                (the welcome page) which is in the web folder.

Tiles are used to control the parts of HTML pages where a JSP will write. Tiles are configured using the
                Web-Inf/tiles-def.xml page.

### Getting Presence Updates

The process for directing a presence update to a user’s screen is described, and illustrated
                below. Cisco Unified CM IM and Presence notifications are detailed later in the document, but this
                section gives an overview of the process on the client side.

- The contactList JSP and eventing JSP use AJAX to poll the Reference Application for server updates.

- The contactList.jsp updates the buddy list tree every 5 seconds (see the triggerPull(5) call) by an
                    Ajax call to getTreePresence in the PresenceAction.

- Cisco Unified CM IM and Presence sends a PresenceNotification to the Third Party Application.

- NotifyAction handles the notification by putting the presence update in a SubscriptionCache.

- The UI makes a call to the getTreePresence method on the PresenceAction over Ajax. The
                    PresenceAction checks the cache for updates and returns an XML snippet for any updates to the
                    UI.

- The UI uses Javascript to change the color code of a contact in the tree to reflect the change.

## Action Classes

The Reference Application uses Apache Struts, an open-source framework for creating Java Web
                Applications. To see how HTTP Requests are forwarded to the correct struts action, refer to the
                Web-Inf/struts-config.xml file.

Submitting a HTML form in the Reference Application results in a call to one of the struts action classes
                in the com.cisco.cup.webservices.refapp.action package. The Action classes are quite
                lightweight, typically performing the following functions:

- Converting form variables to handler parameters

- Calling the appropriate handler

- Storing any information returned from the handler in the request or session

- Forwarding to next screen

The Action classes and the functionality they illustrate are described in the following table.

## Cisco Unified CM IM and Presence Handlers

The Cisco Unified CM IM and Presence Handlers are the classes that interact with Cisco Unified CM IM and
                Presence. The interfaces that Cisco Unified CM IM and Presence Handlers must implement are at:

com.cisco.cup.webservices.refapp.handler

The following table lists the Cisco Unified CM IM and Presence handler classes and interfaces, and
                indicates whether they use configuration or presence information from Cisco Unified CM IM and Presence.
                There are currently two implementations of the handler interfaces, one for Axis and one for REST.

The two implementations of the handler interfaces are:

An Axis Soap implementation at com.cisco.cup.webservices.refapp.handler.axis which make
                    calls to the Third Party Interfaces over SOAP. This package has implementation of all the handler
                    interfaces (both Configuration and Presence).

A REST implementation at com.cisco.cup.webservices.refapp.handler.rest that extends the SOAP implementation. This
                    package has separate implementations of the HandlerFactory, PresenceHandler, and ApplicationHandlers
                    making calls to the RESTful Presence Interface. The REST Implementation still needs to use SOAP to
                    interact with the Client Configuration Web Service, but uses REST to exchange presence data.

### Example: ContactAction Class

The ContactAction class is a good example of an action class interacting with Cisco Unified CM IM and
                Presence handlers. It is called by the Reference Application GUI when any contact information needs to
                be maintained. To access the contact functionality on Cisco Unified CM IM and Presence, the
                ContactAction class uses a ContactHandler implementation, as illustrated in the following image.

There are two steps in getting a ContactHandler:

- Call the HandlerGeneratorFactory to get the HandlerFactory being used. In the image, an
                    AxisHandlerFactory is returned.

- Get the required Handler by calling the appropriate method in the HandlerFactory. In the image,
                    calling getContactHandler returns an AxisContactHandler object.

ContactAction class

```
CupContext context = endUser.getCupContext();

HandlerFactory handlerFactory =  HandlerFactoryGenerator.getHandlerFactory().

ContactHandler contacthandler = handlerFactory.getContactHandler(context);

List <ContactGroup> contactList = contacthandler.getContactList();
```

The action class then calls the appropriate method on the ContactHandler, which will result in a SOAP
                call (over Axis stubs) to Cisco Unified CM IM and Presence. See the right hand panel for a code snippet
                for fetching a contact list.

# Implementation Information

## System Startup

The application web.xml is configured to run the init method of the servlets that appear in the
                com.cisco.cup.webservices.refapp.config package at system startup. The init functionality of each
                servlet, and the order in which they run, is as follows:

SecurityConfigServlet reads the keystore information.

AxisConfigServlet points the Reference Application to the SOAP interfaces on Cisco
                    Unified CM IM and Presence.

RestConfigSerlvet points the Reference Application to the REST interface on Cisco
                    Unified CM IM and Presence.

GenericConfigServlet loads other configurations parameters such as the Application User
                    name and password, the callback URL, and what handler implementation is being used by the Reference
                    Application.

The GenericConfigServlet also has the lines, shown in the right hand panel, in its init method.

```
HandlerFactoryGenerator.getHandlerFactory()

.login(APPLICATION_USERNAME, APPLICATION_PASSWORD, true, true);

if (cupContext != null)
{
    ApplicationUser.getInstance().setCupContext(cupContext);
    ApplicationUser.getInstance().setUserID(APPLICATION_USERNAME);
}

CupEndPoint.getInstance().register();
```

This code snippet sets up two important singletons within the Reference Application:

- The application user that is logged into Cisco Unified CM IM and Presence. This object will in turn
                    be used to log in end users to Cisco Unified CM IM and Presence.

- An endpoint which will be used to receive presence notifications from Cisco Unified CM IM and
                    Presence.

## Login/Logout

As noted in the previous section, on startup the Reference Application creates an application user and
                logs the application user in to Cisco Unified CM IM and Presence. Once an application user’s
                credentials (user name and password) are verified by Cisco Unified CM IM and Presence, the application
                user can log in end users to Cisco Unified CM IM and Presence.

As the Reference Application uses only one application user, the class com.cisco.cup.webservices.refapp.endpoint.ApplicationUser ,
                which models the Application User, is a singleton.

Session ID passed in SOAP header

```
<soapenv:Header> <session-key xmlns= "urn:cisco:cup:tpi:soap" > beb3bb70-1be2-4d73-90f8-e8b3929af58c </session-key> </soapenv:Header>
```

When a user (application user or end user) logs onto Cisco Unified CM IM and Presence via the Third Party
                Interface, they are granted a session ID. This session ID must be passed back in all subsequent calls to
                the interface. In SOAP requests the session ID is passed in the SOAP header as shown in the right hand
                panel.

REST inteface with session ID passed as a request header

```
Presence-Session-Key: beb3bb70-1be2-4d73-90f8-e8b3929af58c
```

With the REST interface, the session ID is passed as a request header as shown in the right hand
                panel.

Thus all handlers must be passed a session ID (contained in CUPContext) to enable them to communicate
                with Cisco Unified CM IM and Presence. Logging out involves passing the session key back to Cisco
                Unified CM IM and Presence, where all the resources associated with the session will be destroyed.

A user can be logged in/logged out over REST or SOAP interfaces. Both the RestHandlerFactory and the
                AxisHandlerFactory have login/logout methods. The login methods for either interface are similar. For
                example when logging in an end user, the end user’s id and the application user’s session
                key are passed to Cisco Unified CM IM and Presence for both interfaces. Cisco Unified CM IM and Presence
                acknowledges a successful login by returning a session ID. This session ID is used to create a
                CUPContext object which is then passed as a parameter to all Handler objects. The Handlers need the
                CUPContext so they can extract the session ID when communicating with Cisco Unified CM IM and
                Presence.

In summary the HandlerFactories logs an application user in to Cisco Unified CM IM and Presence with a
                user name and password combination. End users are logged in with their user name and the application
                user’s session ID. A successful login results in the creation of CupContext objects which are
                stored with the EndUser in the HTTP Session object.

### Multi-node

Cisco Unified CM IM and Presence can be distributed across a series of clusters. The following image
                shows a deployment with two sub clusters, each with two Cisco Unified CM IM and Presence nodes. End User
                1 is configured to have Node 1a as its primary node, while End User 2 has Node 2b as its primary node.
                Both end users are logged on to a Third Party Application which has an associated application user.

The key points to note are:

- The application user is not tied to any sub-cluster or any node in a sub-cluster. It can log in an
                    end user to any node.

- End User 1 has Node 1a as its primary node. For logging on to the Third Party Application (TPA), the
                    TPA will use the application user to log the end user onto Node 1a.

- Once an end user is logged on to a node, all end user requests will be routed to that node, with the
                    end user’s session key.

- The TPA will maintain a record of what nodes an end user is logged into. In the event of a user’s
                    primary node failing, the TPA will forward end user requests to the user’s backup server.

### Context Objects

These are the extensions of the CupContext class for REST and Axis:

- com.cisco.cup.webservices.refapp.handler.axis.AxisCupContext

- com.cisco.cup.webservices.refapp.handler.rest.RestCupContext with RestCupContext extending
                    AxisCupContext

There are two service stub objects in the class AxisCupContext, which are used to invoke SOAP API
                methods. The stub objects are generated from the WSDL as part of the client stub generation. There is
                one stub object generated for each service element defined in the WSDL, configStub and presenceStub.
                There is a default constructor for each that uses the relevant service endpoint defined in the WSDL.
                However, in the Reference Application, the instances of the stub objects are created using the
                constructor that take an endpoint URL as the argument (the endpoints are passed to the
                AxisCupContext constructor).

A number of client options can be set for the stubs. In the AxisCupContext constructor the following
                client options are set:

HTTP Chunking is turned off on the PresenceSoapServiceStub. This is required to call the Presence
                    Interface web service.

REUSE_HTTP_CLIENT is used to configure Axis to re-use one instance of the HTTPClient object for
                    each stub.

The SOAP version to be used is set.

Setting of action fields in the Content Type Header is disabled.

The HTTP Header Connection : Keep-Alive is added to the stub properties to request a
                    persistent connection from the server.

As the REST handlers don’t use SOAP to engage with the Presence Web Service, the RestCupContext
                doesn’t initialize the PresenceStub. Instead the object HTTPClient is created, which is used for
                fire requests at the REST Interface.

RestCupContext uses HTTPClient objects created by the class
                com.cisco.cup.webservice.refApp.ssl.ConnectionManager.

Note: The HTTP client objects are set up to allow concurrent requests.

The ConnectionManager registers a custom Protocol Socket Factory for handling HTTPS requests. This
                ensures HTTPS requests will always use the TLSv1 protocol as required by the Presence Web Service. The
                custom Protocol Socket Factory that is registered is the AuthSSLProtocolSocketFactory class which can be
                obtained as part of the HTTPClient contrib package.

## Handler Internals

To illustrate the contents of Handler objects, a REST and an Axis example of the registerEndPoint method
                is provided in this section. This method is used as part of the Presence Eventing model, this model is discussed in detail in the section Event
                    Notifications .

### registerEndPoint - Axis Example

registerEndPoint - Axis Example

```
public int registerEndPoint(String url,
        int endPointID,
        int expiration) throws HandlerException

{
    int result = 0;
    // Using the Generated classes
    RegisterEndPoint regEPointObj = RegisterEndPoint.Factory.newInstance();
    regEPointObj.setUrl(url);
    regEPointObj.setEndPointID(endPointID);
    regEPointObj.setExpiration(expiration);
    //set up RegisterEndPointDocument used in the SOAP request
    RegisterEndPointDocument regEPointReq =     RegisterEndPointDocument.Factory.newInstance();
    regEPointReq.setRegisterEndPoint(regEPointObj);
    RegisterEndPointResponseDocument regEPointResp = null;
    try
    {
        AxisCupContext context = getAxisCupContext();
        // invoke the web service
        regEPointResp = context.getPresenceStub().registerEndPoint
        (
                regEPointReq,
                context getPresenceSessionKeyDocument()
        );
    }
    catch(RemoteException re)
    {
        throw new HandlerException(re);
    }
    if(regEPointResp!= null)
    {
        result = regEPointResp.getRegisterEndPointResponse()
        .getEndPointID();
    }
return result;

}
```

This section describes the registerEndPoint method for Axis, AxisApplicationHandler.registerEndPoint() .
                The AxisHandler is passed an AxisCupContext in its constructor. The handler gets a stub from the context
                object in order to invoke a registerEndPoint request on the Third Party SOAP Interface. The method
                builds the parameters needed by the stub method and is an example of using the classes generated during
                the WSDL generation exercise. The RegisterEndPoint and RegisterEndPointDocument classes, for example,
                were generated (by axis) from the WSDL and can be found in the lib/presence.jar file.

### registerEndPoint - REST Example

registerEndPoint - REST Example

```
POST /presence-service/endpoints HTTP/1.1
Presence-Session-Key: {app-user-session-key} <?xml version="1.0" ?> <endpoint> <url> {callback-url} </url> <expiration> {expiration} </expiration> </endpoint>
```

This section describes the registerEndPoint method for REST, RestApplicationHandler.registerEndPoint() .
                The purpose of this method is to create a HTTP request in the format below and send the request to the
                REST Interface of the Presence Web Service on Cisco Unified CM IM and Presence.

HTTP response from which the endpoint is read

```
HTTP/1.1 201 CREATED
Location: http://{hostname}/presence-service/endpoints/{endpointId}
```

Cisco Unified CM IM and Presence will respond with a HTTP response, in the format shown in the right hand
                panel, from which the endpoint is read.

code with embedded comments

```
// If it is a new endpoint, use a PostMethod. Otherwise, use PutMethod. Refer to the interface definition as to what HTTP Method should be used.
if(endPointID == 0)
{
    method = new PostMethod(uri);
} else

{
    method = new *PutMethod*(uri + "/" + endPointID);
}

// The Session ID is passed as a HTTP Header
RestUtils.*addSessionKeyHeader*(method, restCupContext.getSessionId());
// Build the Request Body
String request =
    " < ?xml version=\"1.0\"?\>\n" +
    " <endpoint> \n" +
    " <url> " + callbackUrl + " </url> \n" +
    " <expiration> " + expiration + " </expiration> \n" +
    " </endpoint> ";
    RequestEntity entity = new StringRequestEntity(request, "text/xml", "UTF-8");
// Configure the form parameters
method.setRequestEntity(entity);
// Execute the method on the HttpClient object on the RestCupContext
int statusCode = restCupContext.getPresenceHttpClient().executeMethod(method);
if (statusCode != HttpStatus.SC_CREATED)
{
    log.log(LEVEL.Error, "registerEndPoint Method failed: " + method.getStatusLine());
    throw new HandlerException("Error Registering REST End Point");
}

Header locationHeader = method.getResponseHeader("Location");
// Extract the EndPoint ID and return
return RestUtils.getResourceIDAsInt(locationHeader.getValue());
```

The method uses the Jakarta Commons HTTP Client library ( http://hc.apache.org/httpclient-3.x/ )
                to create and send the HTTP requests. DOM Parsers are used to formulate the body of the POST method and
                to parse the returned response. See the embedded comments in the code in the right hand panel to
                understand the method contents.

Note:

- The call to the REST Interface on the Presence Web Service will have a Session ID set as a HTTP
                    header.

- Different HTTP methods are used depending on the service being invoked in the Presence Web Service.
                    Please refer to the Developer Guide for Cisco Unified CM IM and Presence for a description
                    of the methods and parameters that are used for each call to the Presence Web Service.

- Data can be passed to the Presence Web Service in the URI, as a HTTP header or in the XML message
                    body.

- The example above returned an end point in the message body.

## Event Notifications

The sequence flow in the following figure shows the methods used in the Presence Web Service to exchange
                presence data, using the eventing model.

On start up, the Reference Application registers an endpoint with Cisco Unified CM IM and
                    Presence and is passed back an endPointID. This endPointID is stored in the CupEndPoint class and is
                    made available to the Reference Application when a subscription is created.

The Reference Application sets up a subscription and is returned a subscription ID. When a
                    subscription is created, the endpoint is one of the parameters passed to Cisco Unified CM IM and
                    Presence, along with the contacts whose presence will be watched by the subscription.

When Cisco Unified CM IM and Presence needs to notify the Reference Application of an event, it
                    sends an HTTP notification to the Reference Application specifying the subscriptionID and the
                    eventType.

This alerts the Reference Application that an event of the specified type has occurred and that
                    it should retrieve it.

The Reference Application calls the appropriate method to retrieve the event.

A client application should respond to a notification of type PRESENCE_NOTIFICATION by calling
                getSubscribedPresence on the Presence Web Service.

The client application can call the unsubscribe and unregisterEndPoint methods to terminate the
                subscription and to unregister the end point respectively.

### Expiration

An important point concerns the prevention of endpoint registrations from timing out. An expiration (or
                Time-To-Live) is passed as a parameter to Cisco Unified CM IM and Presence for endpoint registration.
                This parameter reflects how long the endpoint is registered with Cisco Unified CM IM and Presence.

The expiration interval for endpoint registration can be refreshed by invoking the registerEndPoint
                method on the Presence Web Service and passing in the endpointID and the updated expiration
                interval.

This is done in the Reference Application by a TimerTask in the CupEndPoint class.

### Endpoints

In order to use the Event notification feature of the Presence Web Service, the Reference Application
                must expose an endpoint to Cisco Unified CM IM and Presence. This endpoint is used by Cisco Unified CM
                IM and Presence to send event notifications. The management of this end point is performed by the class com.cisco.cup.webservices.refapp.endpoint.CupEndPoint

This class has methods for registering and unregistering endpoints. It also prevents the endpoint
                registration from expiring. Registering an endpoint involves sending a call back URL and an expiration
                interval to Cisco Unified CM IM and Presence. The Reference Application is configured to use the
                following action class to handle incoming notifications: com.cisco.cup.webservices.refapp.action.NotifyAction

The CupEndPoint, a singleton, is set up in conjunction with the ApplicationUser at system startup. As can
                be seen from the CupEndPoint class, an ApplicationHandler is used to set up and tear down endpoints.
                There are REST and Axis implementations of the ApplicationHandler.

### Subscriptions

subscribe method signature

```
public int subscribe(List <ContactURI> contactList,
                    EventType eventType, int expiration,
                    int endPointID, int subscriptionID)
throws HandlerException
```

In addition to setting up endpoints the ApplicationHandler also manages subscriptions through its
                subscribe and unsubscribe methods. See the subscribe method signature in the right hand panel:

This method takes in an ad-hoc list of contact URI, an eventtype (the only supported eventtype is
                PRESENCE_NOTIFICATION), an expiration interval (in seconds), an endpointID, and a subscriptionID. The
                endPointID is retrieved from the CupEndPoint singleton. There are two possible ways of using the
                subscriptionID parameter. You can pass in a subscriptionID value of zero which instructs Cisco Unified
                CM IM and Presence to create a new subscription. The subscribe method will return the ID of the new
                subscription. To add contacts to an existing subscription, pass in the relevant subscriptionID value and
                the additional contacts.

An important point concerns the prevention of subscriptions from timing out. An expiration (or
                Time-To-Live) is passed as a parameter to Cisco Unified CM IM and Presence for a subscription. This
                parameter reflects how long the subscription is valid for with Cisco Unified CM IM and Presence.

The expiration interval for a subscription can be refreshed by invoking the subscribe method on the
                Presence Web Service and passing in the subscriptionID, the endpointID, and the updated expiration
                interval.

This is done in the Reference Application by a TimerTask in the SubscriptionCache class.

The unsubscribe method takes in a list of contacts to be removed from a subscription with the given
                subscriptionID. To remove all contacts from a subscription, set the unsubscribeAll flag to true or list
                all contacts to be removed from the subscription in the contactsList parameter.

unsubscribe method

```
public void unsubscribe(List <ContactURI> contactList,
                        int subscriptionID, boolean unsubscribeAll)
throws HandlerException
```

The unsubscribe method is as shown in the right hand panel.

### NotifyAction

When a presence event of interest to a subscription takes place on Cisco Unified CM IM and Presence,
                Cisco Unified CM IM and Presence sends a notification back to the appropriate endPoint. The NotifyAction
                class is configured to be the Reference Application’s endPoint. As this notification (or call
                back) is over an unsecure link, the notify message will not contain any security sensitive data. It will
                however include the ID of the subscription associated with the event. The NotifyAction then calls
                getSubscribedPresence on the PresenceHandler, which calls the Presence Web Service over a secure link to
                get the actual presence change.

getSubscribedPresence

```
public MultiUserPresence getSubscribedPresence(int subscriptionID,
                            PresenceType presenceType)
throws HandlerException;
```

getSubscribedPresence is defined as shown in the right hand panel.

There are two types of Presence_Type, BASIC_PRESENCE and RICH_PRESENCE. Passing in BASIC_PRESENCE will
                see a string, such as AVAILABLE and BUSY, being returned, while specifying RICH_PRESENCE will see a PIDF
                document being returned.

The PIDF document defines the end user’s overall reachability, and the status of each device
                associated with the end user. For detailed information on the content of a PIDF and sample PIDF
                documents, refer to Appendix 2 .

The presence data is then cached on the WebServer for retrieval by a Reference Application client.

The endpoint package contains a SubscriptionCache for caching details on a subscription. Some of the
                details cached include:

- The logged in End User who created the subscription.

- The contacts associated with the subscription.

- Any presence event associated with the subscription.

Typically the NotifyAction will place presence event data for an end user in the subscription cache. The
                PresenceAction, which is being continually polled by Reference Application clients, checks if there are
                any events in the cache associated with the end user and returns any updates to the client.

## Polling for Presence

The Presence Web Service provides a PolledPresence (or Snapshot) mechanism for providing presence
                information to a Third Party Application. This polling functionality can be seen in the REST and Axis
                implementations of the getPolledPresence method in the PresenceHandler interface.

getPolledPresence method

```
public MultiUserPresence getPolledPresence(List <ContactURI> contactList, PresenceType presenceType) throws HandlerException;
```

The getPolledPresence method is defined as shown in the right hand panel.

This interface is defined as taking an ad-hoc list of contacts and a Presence Type. There are two types
                of Presence_Type, BASIC_PRESENCE and RICH_PRESENCE. Passing in BASIC_PRESENCE will see a string such as
                AVAILABLE or BUSY being returned, while specifying RICH_PRESENCE will see a PIDF document being
                returned.

Note: This mechanism bypasses the eventing model to get presence. A Third Party
                Application could continually use getPolledPresence to get presence updates. This alternative to
                eventing, while easier to implement, increases network traffic and increases the load on Cisco Unified
                CM IM and Presence. The Presence Web Service is throttled to prevent an overload on Cisco Unified CM IM
                and Presence.

### Setting Presence

The Presence Handler interface also has a method for allowing end users to set their presence states on
                Cisco Unified CM IM and Presence. The setPresence interface is shown in the right hand panel.

setting presence

```
public void setPresence(SingleUserPresence presenceInfo, int expiration)
throws HandlerException;
```

The presenceInfo parameter contains the presence information. The expiration value specifies how long
                this presence information is valid. Subsequent calls to setPresence are needed to maintain a presence
                state after the expiration time. The SingleUserPresence class can hold Rich Presence and Basic
                Presence. The setPresence method handles passing both rich and basic presence to the Third Party
                Interface. The setPresence method is on:

com.cisco.cup.webservices.refapp.handler.axis.AxisPresenceHandler

Note: Rich Presence is represented as a PIDF document. An example is included in Appendix 2 . Refer to this section for a description of the contents of a PIDF
                document.

Note: The Reference Application only has a use case for setting SIMPLE Presence, for
                example passing down a String Representation (including AVAILABLE and BUSY).

The following table lists the presence states on Cisco Unified CM IM and Presence and provides a
                definition for each state.

## Presence Override

Presence override is the concept of setting your presence state to override any other presence events.
                For example, you might be at your desk, but have set your presence to DND, in an override state. This
                means all other device initiated presence events (for example, going on/off hook) will be overridden by
                the original DND presence event. Override is represented as a boolean on the SingleUserPresence
                class.

Note: A state of Available can ONLY be set with override set to false. A state of DND
                can ONLY be set with override set to true.

## Error Handling

This is applicable to the SOAP Interface only.

When the Presence Web Service on Cisco Unified CM IM and Presence encounters an error condition, it
                generates a Fault. This results in an AxisFault being thrown in the Axis Handler Layer of the Reference
                Application. A definition of the AxisFault class is as follows:

http://ws.apache.org/axis/java/apiDocs/org/apache/axis/AxisFault.html

The Reference Application has a very basic exception (fault) handling procedure in that all exceptions
                are just written to the log\refApp.log file under the Tomcat Installation directory. The
                AxisSoapFaultUtils class contains an example of how to parse a SOAP fault.

Appendix 1 lists the errors that can be generated by the SOAP-based Presence
                Web Service. Each error has a code, a message, and a recommended fix. The errors covered in the Appendix
                are only returned by the Presence SOAP Interface.

# Third Party API FAQ

Note: In this section the term Third Party Interface refers to the web services
                that open up both Presence exchange and user preference information (such as presence rules and contact
                list) on Cisco Unified CM IM and Presence, the Presence Web Service, and the Client Configuration Web
                Service.

What Interfaces make up the Third Party API?

The Third Party API consists of a Client Configuration Interface and a Presence Interface. Both
                interfaces are available as Web Services, though the Presence Interface can also be accessed over REST.
                The Presence and Client Configuration interfaces run on different components on Cisco Unified CM IM and
                Presence and are available on different ports.

Why does interacting with the API involve using two certificates? What TLS Versions are
                supported?

As mentioned above the Third Party API is split across two Cisco Unified CM IM and Presence components.
                Interacting with SIP Proxy requires one certificate, and calling the Tomcat Config Servlet requires
                another certificate. These certificates are downloaded via the Cisco Unified CM IM and Presence
                Operating System GUI. TLSv1 is supported.

What versions of SOAP are supported by the Third Party API?

The Presence Interface supports SOAP V1.1 and V1.2. The Configuration Interface supports V1.2 only.

Can the Third Party API be accessed over HTTP?

The Presence Interface is available over HTTP. The Client Configuration Interface cannot be accessed over
                HTTP.

What is the difference between Rich and BASIC Presence?

Rich Presence is in a PIDF format (for a sample PIDF, refer to Appendix 2 ) and
                contains information beyond an end user’s basic presence state. Rich presence contains an end
                user’s “overall reachability” status and the status of each device associated with
                the end user. The Reference Application, for example, shows retrieving device information over PIDF.
                Basic Presence involves sending one of the seven basic presence states in a string format, such as
                Available and Busy. The basic presence states are defined in presence
                    state definitions table.

How do I read a PIDF document?

The PIDF document is made up of a persona section and a tuple section per device associated with the end
                user. The persona section identifies the end user and defines the end user’s overall
                reachability. The tuple section identifies an associated end user device and contains information on the
                status of the device. Note that the status of a device can either be open or closed. For more detailed
                information on the content of the PIDF, refer to Appendix 2 .

What is the purpose of the override flag when setting Presence?

When setting presence, a presence status and an override flag are passed to Cisco Unified CM IM and
                Presence. Setting override to true sets an end user’s overall reachability and overrides the
                presence of an end user’s devices. When an end user sets their presence to DND (DND must have an
                associated override of true), their presence will still be DND, even if they go on a call. Normally
                going on a call would see Call Manager publishing a BUSY Event to Cisco Unified CM IM and Presence. The
                event will be ignored if the user’s presence is a DND state, because of the override session.
                When using the override flag for rich presence, the tuple ID should be set to pws-override or
                pws-persistent.

How does setPresence with override set to false affect my overall presence
                status?

Presence rules for a user dictate how setPresence requests are handled by Cisco Unified CM IM
                and Presence when override is false.

The user is actually setting their presence for a particular client and the presence rules decide how
                that change affects their overall status.

With default presence rules, setting the status of a user to Available, Away, Busy, or Vacation on
                a PWS client will also update the overall status for a user. But, this is not guaranteed
                for Unavailable.

An overall status for a user will only be set to Unavailable when they are unavailable on
                all their clients.

Note: A presence rule for a user may be modified to change this default behavior.

How do I set up an Application User?

An application user is set up using the user management option in the Cisco Unified CM IM and Presence
                Administration GUI. When setting the application user, keep a note of the user name and password as you
                will need these values for configuring the web.xml file in the Reference Application.

Why must HTTP Chunking be disabled when using the Presence Interface?

Presence Interface is rendered by a GSOAP Web Service stack which has a requirement that HTTP chunking be
                disabled.

What are the presence eventing models, and why would I use one over the other?

There are two presence eventing models supported, polling and eventing. Polling is easier to implement on
                the client, but may cause increased network traffic and load on the Cisco Unified CM IM and Presence.
                This is the method to use for getting a quick presence snapshot. However, to monitor a user’s
                presence over time, the eventing model is more efficient and will give presence updates in real time as
                distinct from having a polling interval lag.

What are the issues around maintaining an endpoint?

When an endpoint is created, an endpointID is returned by Cisco Unified CM IM and Presence which is used
                to manage the endpoint. When an endpoint is created, an expiration interval must be passed as a
                parameter. This timeout is absolute and is NOT an inactivity timeout, meaning the timer starts as soon
                as the endpoint is created. The interval can be refreshed by calling registerEndPoint (via SOAP or REST)
                and passing the new expiration interval and the endpointID.

What are the issues around maintaining a subscription?

When a subscription is created, a subscriptionID is returned by Cisco Unified CM IM and Presence. An
                application can add contacts to the subscription by passing the additional contacts, the endpointID, and
                the subscriptionID to the subscribe call. As with endpoints, the expiration interval on a subscription
                is absolute. The subscription can be refreshed by invoking the subscribe call and passing the
                subscriptionID, the endpointID, and the updated expiration interval.

What are the defaults expiration values around setting up subscriptions and
                endpoints?

Both expiration values have a maximum expiration time of twenty-four hours. If the expiration time is
                non-zero, the interval must be at least one hour or the request will be rejected. An expiration time of
                zero is an error case for RegisterEndPoint. But for subscribe, you can pass an expiration value of zero
                when adding contacts to an existing subscription, without refreshing the subscription’s
                expiration time.

If I am using the Presence Web Service and the Client Configuration Web Service, do I need to
                log in separately to both interfaces?

No, if your application intends to use both interfaces, you should just log in over the Presence Web
                Service interface. The session key returned may be used in requests to both the Presence Web Service and
                Client Configuration Web Service. If the application is just using Client Configuration Web Service,
                then it can use the Client Configuration Web Service login method.

What happens when the Primary (Cisco Unified CM IM and Presence) Node I am logged into
                fails?

When an Application/End user is logged in, the login response includes the IP address of a backup server.
                In the event of a primary failure, any User can login to the backup server, the presence
                resources such as endpoints and subscriptions will have to be recreated on the backup server. This
                requires calling the registerEndPoint method and the subscribe method to set up endpoints and
                subscriptions

Is viewing presence of Federated users through the Presence Web Service supported?

Yes, for Cisco Unified CM IM and Presence to Cisco Unified CM IM and Presence federation. However, for
                Cisco Unified CM IM and Presence to Microsoft OCS federation, BASIC presence is not supported. RICH
                presence must be retrieved to view a federated OCS user’s presence.

I am getting errors trying to generate stubs with the Client Configuration WSDL due to missing
                types. What can I do?

Make sure presence-rules.xsd and the epas-soap-interface.xsd files are in the same directory as the
                Client Configuration. Then (in a .NET environment) run the command wsdl.exe <service.wsdl>
                    presence-rules.xsd epas-soap-interface.xsd .

The xsd files are located at:

- https://cup-hostname:8443/EPASSoap/presence-rules.xsd

- https://cup-hostname:8443/EPASSoap/ epas-soap-interface.xsd

I am having problems connecting to the Presence Service using CXF Soap Stack using HTTPS. What is
                the issue?

The Proxy Component that runs the Presence Web Service only accepts connection requests using TLSv1. CXF
                version 2.0.5+ does not support TLSv1. CXF will use SSLV2, even for connection setup requests, leading
                to the connection being rejected by the Cisco Unified CM IM and Presence.

What ports are the Presence and Client Configuration Web Services available on by
                default?

The Presence Web Service is available on port 8082 (HTTP) and 8083 (HTTPS). The Client Configuration Web
                Service is available on 8443 for IPv4 and 443 for IPv6 (HTTPS) only.

What is the format of a presence notification (callback) generated by Cisco Unified CM IM and
                Presence?

http://<Call Back Address>?id=10&eventType=PRESENCE_NOTIFICATION

The Call Back Address is passed as the URL parameter to the registerEndPoint method. Note that Cisco
                Unified CM IM and Presence sets two parameters in the call back. The id (subscription id) for which a
                present event has occurred and the eventType. The client application would typically then call
                getSubscribedPresence passing in the subscription id to get the Presence update.

I am getting an invalid session key response when I attempt to log out of the Presence Web
                Service using a Cisco Unified Personal Communicator session key with the logout method. What is the
                issue?

The Presence Web Service can only log in or log out any third party user. It is unable to log in or log
                out a Cisco Unified Personal Communicator or Cisco Unified Mobile Communicator user. This is applicable
                to both SOAP and REST.

Note that the Client Configuration Web Service can distinguish between a third party user and an
                application user. Therefore it is possible to log in and log out a third party user, a Cisco Unified
                Personal Communicator user and a Cisco Unified Mobile Communicator user from the Client Configuration
                Web Service.

When using the Third Party API over HTTPS, what is the best connection handling
                approach?

We recommend that you reuse a secure connection when interacting with Cisco Unified CM IM and Presence
                due to the CPU overhead used to create these secure connections. The Reference Application provides an
                example for doing this with the Keep-Alive Http Header. Using this header Cisco Unified CM IM and
                Presence maintains a secure connection for several hours even if there is no activity on the
                connection.

# Appendix 1

## Error Codes

The error codes for the Presence Web Service are defined below:

# Appendix 2

## PIDF Documents

Rich presence for an end user is sent in a PIDF document. The PIDF contains the following
                information:

- The end user’s overall presence state or reachability.

- The status of each device associated with the end user.

Each device associated with an end user reports its status and reachability to Cisco Unified CM IM and
                Presence. Using this device status information and the presence rules defined, Cisco Unified CM IM and
                Presence determines an overall presence state for the end user, also known as overall reachability. The
                overall reachability, and the status of each device associated with the end user, form the rich presence
                information that is defined for an end user in the PIDF document.

The PIDF document contains a person section, that defines the end user’s overall reachability, and
                a tuple section for each device associated with the end user. The tuple identifies the device type and
                contains information on the status of the device. Note that the status of a device can either be open or
                closed. A definition of the elements in the PIDF is provided in the PIDF
                    element definitions table.

Each time the client application sets basic presence, the Presence Web Service generates a PIDF document
                (on behalf of the client). This PIDF document contains the end user’s overall reachability and a
                tuple entry for the Presence Web Service. This is illustrated in the Sample
                    PIDF where the tuple ID is cisco-pws which represents the
                Presence Web Service. When the client application sets rich presence, a PIDF document is built by the
                client and passed to the Third Party API. It is up to the client to ensure that the PIDF is well formed.
                The client can set the overall reachability and the set the tuple to whatever they wish. They are not
                tied to using the cisco-pws tuple.

The override flag allows the client application to override the overall reachability state and set an end
                user’s overall presence state directly on Cisco Unified CM IM and Presence. Note that if the
                override flag is set to true, the tuple entry for the Presence Web Service will have the tuple id value pws-override .

When rich presence is retrieved, multiple tuple entries may be present in the PIDF for each end user
                device. See section Sample PIDF for a sample PIDF document showing multiple
                tuple entries.

## Sample PIDF

Presence setting of available

```
<presence xmlns= "urn:ietf:params:xml:ns:pidf" entity= "sip:brmaguir@cisco.com" > <person xmlns= "urn:cisco:params:xml:ns:pidf:rpid" id= "brmaguir" > <activities> <available /> <phone-status> unavailable </phone-status> <im-status> available </im-status> </activities> </person> <display-name xmlns= "urn:ietf:params:xml:ns:pidf:cipid" > Brendan Maguire </display-name> <tuple id= "cisco-upc" > <contact priority= "0.6" > sip:brmaguir@cisco.com </contact> <note xml:lang= "en" /> <sc:servcaps xmlns:sc= "urn:ietf:params:xml:ns:pidf:servcaps" > <sc:video> false </sc:video> <sc:audio> false </sc:audio> <sc:text> true </sc:text> <sc:type> text/plain </sc:type> <sc:type> application/x-cisco-cupc+xml </sc:type> </sc:servcaps> <user-input> active </user-input> <status> <basic> open </basic> </status> </tuple> </presence>
```

An example in the right hand panel shows a PIDF document with a Presence setting of available .

PIDF with multiple tuple entries

```
<presence xmlns= "urn:ietf:params:xml:ns:pidf" entity= "sip:brmaguir@cisco.com" > <person xmlns= "urn:cisco:params:xml:ns:pidf:rpid" id= "brmaguir" > <activities> <user-input> idle </user-input> <available /> <phone-status> unavailable </phone-status> <im-status> available </im-status> </activities> </person> <display-name xmlns= "urn:ietf:params:xml:ns:pidf:cipid" > Brendan Maguire </display-name> <tuple xmlns= "urn:cisco:params:xml:ns:pidf" id= "cisco-upc" > <contact priority= "0.6" > sip:brmaguir@cisco.com </contact> <note xml:lang= "en" /> <sc:servcaps xmlns:sc= "urn:ietf:params:xml:ns:pidf:servcaps" > <sc:video> false </sc:video> <sc:audio> false </sc:audio> <sc:text> true </sc:text> <sc:type> text/plain </sc:type> <sc:type> application/x-cisco-cupc+xml </sc:type> </sc:servcaps> <user-input> idle </user-input> <status> <basic> open </basic> </status> </tuple> <tuple xmlns= "urn:ietf:params:xml:ns:pidf" id= "Jabbercup7" > <status> <basic> open </basic> </status> <servcaps xmlns= "urn:ietf:params:xml:ns:pidf:servcaps" > <type> text/plain </type> <type> application/x-cisco-cupc+xml </type> <text> true </text> </servcaps> </tuple> </presence>
```

An example in the right hand panel shows a PIDF with multiple tuple entries.

# Appendix 3

## Importing the Eclipse Project

This section describes how to import the Reference Application into Eclipse.

- Download the Presence Web Service Reference Application. Contact your Cisco representative for the
                    location to download the application. The filename for the Reference Application will be in the
                    following format: cup_tpi_referenceApplication_<REF_APP_VERSION>.zip . Save
                    this file to your local disk.

- Open Eclipse to your local workspace.

- Go to File > Import .

- Select the import source as Existing Projects into Workspace and click Next .

- Choose Select archive file and browse to the location where you saved the Reference
                    Application .zip file. Ensure the ReferenceApp Project is selected in the projects window.

- Click Finish to start importing the project into the workspace.

Note: It may take approximately 10 minutes to import the project due to the large number
                of generated client stub classes and javadocs.

Note: When imported, the project may show HTML validation errors due to the nature of
                some jsp files and javadocs. If this is the case you can disable HTML validation by right clicking on
                the ReferenceApp project and selecting Properties > Validation . Then choose Override
                    validation preferences and uncheck the required validators from the Build column.

## Rebuild the Eclipse Project

To remove any validation errors that Eclipse may have been showing, you will need to Clean the Project
                ( Project > Clean ) and rebuild it ( Project > Build All ) within
                Eclipse.

The pre-build Web Archive file (.WAR ) file is located in the folder build\ear\refApp.war. The
                recommended way to build the Project is using the supplied Ant script. The procedure is described
                below.

- Right click on build.xml in the build folder and choose Run
                    As > Ant Build .

- To deploy the war file, copy the .WAR file from build\ear to your J2EE webapps
                    folder on Tomcat.

- Alternatively you can use the deploy.xml Ant script to deploy the .WAR file
                    (Windows only). To use this, right click on deploy.xml in the build folder and choose Run As > Ant Script .

| Name | Description |
|---|---|
| Application User | An application user is a logical entity that represents a Third Party Application that can log
                        in to Cisco Unified CM IM and Presence. The primary functionality associated with an application
                        user is the ability to log end users in to Cisco Unified CM IM and Presence. Setting up the
                        Reference Application involves configuring an application user. An application user is created
                        under the User Management option in the Cisco Unified CM IM and Presence Administration GUI. |
| Axis | Axis is a Java-based implementation of both the client and server sides of the Web services
                        specification. The Reference App uses Axis2 to: Send SOAP messages Receive and process SOAP messages Create implementation client stub classes using WSDL The Reference Application uses an Axis2 client library to interact with the Third Party
                        Interface. As the Third Party Interface has two elements, with the Presence and Configuration
                        interfaces served on different ports, the Reference Application must interact with two end
                        points. |
| Client Configuration Web Service | The Client Configuration Web Service is an interface to Cisco Unified CM IM and Presence that
                        allows client applications to manage user preference information such as contacts, contact
                        groups, access control lists, and calendaring options. This web service is available via a SOAP
                        interface. |
| CUP Handler | The CUP Handler is the layer of code (in the Reference Application) which communicates with
                        Cisco Unified CM IM and Presence. There are two Handler implementations available within the
                        Reference Application - a REST implementation, which sends HTTP Requests to Cisco Unified CM IM
                        and Presence, and an Axis SOAP implementation. |
| Endpoint | The Reference Application has an endpoint, which Cisco Unified CM IM and Presence uses to send
                        presence notifications back to the Reference Application. Any application using the sub/notify
                        feature of Cisco Unified CM IM and Presence must provide such an end point. |
| Presence Web Service | The Presence Web Service is an open interface that allows client applications to share user
                        presence information with Cisco Unified CM IM and Presence. This interface is used by developers
                        to build client applications that can send and receive updates to a user’s presence
                        state. The web service is available via a SOAP interface and a REST (HTTP/XML) interface. |
| REST | REST (Representational State Transfer) can be seen as a lightweight alternative to SOAP. REST
                        relies on accessing resources by using different URIs and putting the XML data in the message
                        body. |

| Parameter Name | Parameter Description |
|---|---|
| java_keystore_file | The full path to the Java keystore (including the keystore filename) that contains trusted
                        certificates for establishing TLS connections between the Reference Application and the Cisco
                        Unified CM IM and Presence server. The path should include the keystore filename. |
| java_keystore_password | The password to access the Java keystore. |

| Parameter Name | Parameter Description |
|---|---|
| cup_presence_path | The endpoint where the SOAP-based Presence Web Service is hosted. The CUP_HOSTNAME value should
                        be set to the IP address of the Cisco Unified CM IM Presence server |
| cup_config_soap_path | The endpoint where the SOAP-based Client Configuration Web Service is hosted. |
| cup_config_soapversion | The SOAP version used to connect to the Client Configuration Web Service on the Cisco Unified CM
                        IM and Presence server. Only SOAP 1.2 is supported. The syntax is V1_2. |
| cup_presence_soapversion | The SOAP version used to connect to the Presence Web Service on the Cisco Unified CM IM Presence
                        server. SOAP 1.1 and 1.2 are supported. The syntax is V1_1 or V1_2. |
| cup_config_disablesoapaction | This parameter disables the soap action header when connecting to the Client Configuration Web
                        Service. The valid values are true and false . |
| cup_presence_disablesoapaction | This parameter disables the soap action header when connecting to the Presence Web Service. The
                        valid values are true and false . |

| Parameter Name | Parameter Description |
|---|---|
| cup_rest_presence_path | The URL where the REST-based Presence Web Service is hosted. The CUP_HOSTNAME should be set to
                        the IPv4/IPv6 address of the Cisco Unified CM IM Presence server. |
| cup_configsoap_path | The endpoint where the REST-based Client Configuration Web Service is hosted. The CUP_HOSTNAME
                        should be set to the IPv4/IPv6 address of the Cisco Unified CM IM and Presence server. |

| Parameter Name | Parameter Description |
|---|---|
| Application_username | The username of the application user. |
| Application_password | The password of the application user. |
| callback_url | The URL on which the Reference Application will receive notifications from Cisco Unified CM IM
                        and Presence. Set the REFAPP_WEBSERVER_HOSTNAME value to the address of the machine that the
                        Reference Application is running on. This address can be both IPv4 or IPv6. |
| handler_factory_classpath | The location of handler class to use when communicating with Cisco Unified CM IM and Presence.
                        There are two possible settings for the REST and Axis SOAP implementations of the Handler
                        Interface respectively: com.cisco.cup.webservices.refapp.handler.rest.RestHandlerFactory com.cisco.cup.webservices.refapp.handler.axis.AxisHandlerFactory |

| Parameter Name | Parameter Description |
|---|---|
| alias | The name that is used to identify the certificate in the keystore. |
| file | The path to the certificate file that was downloaded from Cisco Unified CM IM and Presence |
| keystore | The path to the Reference Application keystore. It can be located in a folder of your choice on
                        your local disk. |
| storepass | The password used to access the keystore. |

| URL | Port |
|---|---|
| cup_presence_path | port : 8083 |
| cup_configsoap_path (IPv4) | port : 8443 |
| cup_configsoap_path (IPv6) | port : 443 |

| URL | Port |
|---|---|
| cup_rest_presence_path | port : 8083 |
| cup_configsoap_path (IPv4) | port : 8443 |
| cup_configsoap_path (IPv6) | port : 443 |

| Server | URL |
|---|---|
| cup_presence_path | https://cupserver:8083/presence-service/soap |
| cup_configsoap_path | https://cupserver-ipv4:8443/EPASSoap/service |
| cup_configsoap_path | https://cupserver-ipv6:443/EPASSoap/service |
| cup_rest_presence_path | https://cupserver:8083/presence-service |
| cup_configsoap_path | https://cupserver-ipv4:8443/EPASSoap/service |
| cup_configsoap_path | https://cupserver-ipv6:443/EPASSoap/service |

| Item | Description |
|---|---|
| data-src | Contains all the Reference Application source code. |
| build | Contains build scripts used to build the Reference Application. The WAR files are located in
                        build\ear. |
| web | Contains the jsp and JavaScript files that make up the Web Application. In addition the Java
                        libraries used by the Reference Application are stored in here at WEB-INF\LIB |
| clientStubs | WSDL and client stubs for the Third Party SOAP Interface. |
| docs | Javadocs describing the Reference Application source code. |

| Package | Description |
|---|---|
| com.cisco.cup.webservices.refapp.action | The struts action classes and associated forms that service the UI. |
| com.cisco.cup.webservices.refapp.config | Four servlets that run at system start-up, and configure the Reference Application based on the
                        web.xml file. |
| com.cisco.cup.webservices.refapp.endpoint | Classes used to manage and cache subscription information. |
| com.cisco.cup.webservices.refapp.handler | The handler classes that interact with the Cisco Unified CM IM and Presence Third Party
                        Interfaces. |
| com.cisco.cup.webservices.refapp.log | RefApp logger. The RefApp uses log4j to write to <CATALINA_HOME>\logs\refApp.log* log
                        files. |
| com.cisco.cup.webservices.refapp.ssl | Classes for setting up the TLS Connections with Cisco Unified CM IM and Presence. |

| Package | Description |
|---|---|
| images | Contains the gifs used to represent presence in the contacts tree. |
| pages | Contains the JSP files used to generate the HTML/Javascript that make up the Reference
                        Application UI. |
| tiles | Contains the Template.jsp which dictates where a JSP is placed on screen. |
| WEB-INF | Contains the tag libraries used by the Reference Application. The struts-config.xml is
                        used to configure struts, tiles-defs.xml manages the tiles set up, and web.xml configures the Reference Application itself. The build process bundles all these files in
                        RefApp.war. |
| (lib) | Contains jar file needed by the Reference Application. These jars include the Axis2, struts, and
                        xml handling binaries. Other jar of note is the axis-struts.jar created during the stubs process
                        above. All the jars in the lib directory are put in the RefApp.war file. |

| File | Description |
|---|---|
| client-configuration.wsdl | Contains the interface definition for the Client Configuration Web Service. |
| presence.wsdl | Contains the interface definition for the Presence Web Service. |
| presence-rules.xsd | Contains the schema definition of a PresenceRule. It is used by the client-configuration.wsdl
                        file. |
| Epas-soap-interface.xsd | Contains type used by the client-configuration.wsdl. |
| generateClientStubs.sh | Shows how to generate axis client stubs from the WSDL definitions. Running the file has the
                        effect of creating two jars – client-config.jar and presence.jar (one for each WSDL file)
                        and placing them in the lib directory. This script only runs on a Unix/Linux platform. |

| Name | Screen | Description |
|---|---|---|
| index.jsp | Login Page | This JSP manages user login authorization and application type selection. Submitting the login
                        form calls the LoginAction class. |
| eventing.jsp | Eventing Tutorial | This JSP demonstrates how to register endpoints and set up a subscription for event
                        notifications. All form submission is handled by the EventingAction class. This JSP uses Ajax to
                        poll the Reference Application for event notifications. |
| contact.jsp | Contact Page | This JSP displays rich presence and manages the functionality for blocking a user’s
                        presence. This JSP interacts with the UserAction class. |
| contactList.jsp | Contact Tree | This JSP receives contact information that it uses to draw the contact tree. This JSP uses Ajax
                        to poll for presence updates. Polling and setting of presence results in calls to Presence
                        Action. |
| contacts-Maintainence.jsp | Manage Contacts Screen | This JSP interacts with ContactAction class for adding/updating/deleting contacts. |
| group-Maintainence.jsp | Manage Groups Screen | This JSP Interacts with GroupAction class for adding/updating/deleting contacts. |
| errorPage.jsp | Error Page | This JSP will be displayed if an exception is thrown by any other JSP page |
| presence.jsp |  | This JSP carries Ajax call back information for the contact tree. |
| notification.jsp |  | This JSP carries Ajax call back information for the eventing screen. |

| Action | Functionality |
|---|---|
| EventingAction | Provides examples on using the event methods, for example on setting up and tearing down,
                        registering subscriptions and endpoints. |
| ContactAction | Add/modify/delete a contact |
| GroupAction | Add/modify/delete a group |
| LoginAction | Log an end user in to Cisco Unified CM IM and Presence |
| LogoutAction | Log an end user out of Cisco Unified CM IM and Presence. |
| NotifyAction | Handling a presence notification |
| PresenceAction | Setting a user’s presence, and retrieving cached presence. |
| UserAction | Getting (polled) rich presence of a contact, and blocking a contact from seeing a user’s
                        presence. Code for parsing PIDF to get Device and Privacy Information. |

| Class | Purpose | Type |
|---|---|---|
| HandlerFactoryGenerator | This class determines which HandlerFactory implementation (Axis or REST) is used. | NA |
| HandlerFactory | This class is the gateway to handler logic, acting as a Factory for creating handler objects.
                        There are two implementation of this factory, one for returning Axis Handlers, another for
                        returning REST Handlers. In addition, the login/logout functionality is available here. | Presence |
| ACLHandler | This class determines the methods that can be carried out on a Rule ACL. | Configuration |
| CalendarHandler | This class is used to access the calendaring logic available on Cisco Unified CM IM and
                        Presence. | Configuration |
| ContactHandler | This class allows for managing the contacts on Cisco Unified CM IM and Presence. | Configuration |
| CupContext | This class represents a user session with Cisco Unified CM IM and Presence. | NA |
| GroupHandler | This class allows for the managing of groups on Cisco Unified CM IM and Presence. | Configuration |
| PresenceHandler | This class allows for getting and setting of Presence. | Presence |
| ApplicationHandler | This class interacts with the Subscribe/Notify capabilities of the Presence Web Service. | Presence |
| PresenceRulesHandler | This class determines the methods for getting and setting presence rules. | Configuration |

| Presence State | Definition |
|---|---|
| Available | The user is available. |
| Away | The user has logged in, but presence is set to AWAY. |
| Do Not Disturb (DND) | The user has logged in, but Presence is set to DND. |
| Unavailable | This state is returned when a user is not logged in to Cisco Unified CM IM and Presence through
                        any UPC client (or the Presence Web Service). |
| Unknown | This state is returned when Cisco Unified CM IM and Presence is asked for the presence of a user
                        that is not known. |

| Error Code | Error Message | Error Fix | SOAP HTTP Status Code | REST HTTP Status Code |
|---|---|---|---|---|
| 100 | Session key not present in request | A session key is required to authenticate the request. It is obtained by logging
                        in. | 200 OK | 401 Unauthorized |
| 101 | Invalid session key | Ensure the user is logged in or try logging in the user again. | 200 OK | 401 Unauthorized |
| 102 | Unable to parse XML request | Ensure that the XML in the request is well formed and the required data is
                        provided. | 200 OK | 400 Bad Request |
| 103 | The XML root element is invalid | Ensure that the XML root element corresponds to the root element expected for this
                        type of request. | 200 OK | 400 Bad Request |
| 110 | The presence type is not valid | Presence type must be either BASIC_PRESENCE or RICH_PRESENCE. | 200 OK | 400 Bad Request |
| 111 | The password is not valid | The password must not be empty. | 200 OK | 400 Bad Request |
| 112 | The login type is not valid | Follow the required format for either application user login or end user login. | 200 OK | 400 Bad Request |
| 113 | The username is not valid | The username must not be empty. | 200 OK | 404 Not Found |
| 114 | Failed to login user | Ensure the login data is valid. | 200 OK | 400 Bad Request |
| 115 | Basic presence parameter specified is either null or empty | Specify a basic presence status. | 200 OK | 400 Bad Request |
| 120 | Failed to set presence data | Ensure the presence data is valid. | 200 OK | 400 Bad Request |
| 121 | User’s presence status cannot be set to AVAILABLE in override mode. | To set the presence status to AVAILABLE, the override flag must be false. | 200 OK | 400 Bad Request |
| 122 | User’s presence status cannot be set to DND in non-override mode | To set the presence status to DND, the override flag must be true. | 200 OK | 400 Bad Request |
| 123 | Endpoint URL specified in endpoint registration update | Only expiry times are updated in endpoint registration. Ensure that the endpoint
                        URL field is empty. | 200 OK | 400 Bad Request |
| 124 | An invalid contact URI was provided | Ensure that all contact URIs are correctly formatted. | 200 OK | 400 Bad Request |
| 125 | An invalid override parameter was provided | Ensure that the override parameter is specified as either true or false (case
                        sensitive). | 200 OK | 400 Bad Request |
| 130 | The endpoint URL is null or empty | An endpoint URL is required when registering an endpoint. | 200 OK | 400 Bad Request |
| 131 | The expiry value must be between 3600 and 86400 seconds | The value must not be less than 3600 or greater than 86400 seconds. | 200 OK | 400 Bad Request |
| 132 | The endpoint id does not exist | Ensure the value is not less than 0 or that the endpoint was not previously
                        unregistered. | 200 OK | 400 Bad Request |
| 133 | The subscription id does not exist | Ensure the value is not less than 0 or that the id was not previously
                        unsubscribed. | 200 OK | 400 Bad Request |
| 134 | The subscription type is not valid | Subscription was expecting to receive a type of PRESENCE_
                        NOTIFICATION. | 200 OK | 400 Bad Request |
| 135 | The number of contacts must be between 0 and 5000. | Ensure that the number of contacts is greater than 0 but not greater than 5000. | 200 OK | 400 Bad Request |
| 136 | You do not have permission to access this endpoint | Ensure the session key associated with this endpoint is used. | 200 OK | 400 Bad Request |
| 137 | You do not have permission to access this subscription | Ensure the session key associated with this subscription is used. | 200 OK | 400 Bad Request |
| 138 | There are no free endpoints available | Unregister any unused endpoints. | 200 OK | 400 Bad Request |
| 139 | There are no free subscriptions available | Unsubscribe from any unused subscriptions. | 200 OK | 400 Bad Request |
| 140 | You must be an end user to perform this task | Log in as end user. | 200 OK | 400 Bad Request |
| 141 | You must be an application user to perform this task | Log in as application user. | 200 OK | 400 Bad Request |
| 142 | The endpoint URL contains spaces | The endpoint URL is invalid. Remove any spaces. | 200 OK | 400 Bad Request |
| 143 | A null or empty contact was provided | Ensure that all contacts are valid. | 200 OK | 400 Bad Request |
| 144 | At least one of the contacts provided is not part of the subscription | Ensure that all contacts are valid and exist as part of this subscription. | 200 OK | 400 Bad Request |
| 145 | No expiry value or contacts provided | An expiry value or a list of contacts must be specified. | 200 OK | 400 Bad Request |
| 146 | No contact list provided | A list of contacts must be specified. | 200 OK | 400 Bad Request |
| 147 | Invalid element in contact list | Ensure the contact list consists of valid elements. | 200 OK | 400 Bad Request |
| 148 | Invalid contact attribute | Specify a valid contact attribute. | 200 OK | 400 Bad Request |
| 150 | Could not read the message body of the http request | Ensure the http body is correctly formed. | 200 OK | 400 Bad Request |
| 160 | User is already logged in | Log the user out from their session or enable the force option when logging in. | 200 OK | 409 Conflict |
| 161 | Invalid override tuple-id specified in rich presence document | To set override or persistent presence, the tuple-id must be ‘pws-override’
                        or ‘pws-persistent’. | 200 OK | 400 Bad Request |
| 162 | Invalid source element in rich presence document | Place a ‘Presence Web Service’ source element in the device tuple. | 200 OK | 400 Bad Request |
| 200 | Server error occurred | Consult the application server logs. | 200 OK | 500 Internal
                        Server
                        Error |
| 201 | Failed to unregister endpoint | Consult the application server logs. | 200 OK | 500 Internal Server Error |
| 202 | Failed to subscribe to contact’s presence | Consult the application server logs. | 200 OK | 500 Internal Server Error |
| 203 | Failed to unsubscribe to contact’s presence | Consult the application server logs. | 200 OK | 500 Internal Server Error |
| 204 | Failed to set contact’s presence status | Consult the application server logs. | 200 OK | 500 Internal Server Error |
| 205 | Failed to logout user | Consult the application server logs | 200 OK | 500 Internal Server Error |
| 206 | Failed to acquire endpointID | Consult the application server logs | 200 OK | 500 Internal Server Error |
| 207 | Failed to acquire subscriptionID | Consult the application server logs | 200 OK | 500 Internal Server Error |
| 208 | Failed to login user | Consult the application server logs | 200 OK | 500 Internal Server Error |
| 209 | Failed to register endpoint | Consult the application server logs | 200 OK | 500 Internal Server Error |
| 210 | Max CPU utilization reached | Wait before sending another request | 503 Service Unavailable | 503 Service Unavailable |
| 211 | No free SIP Subscriptions available | Reduce the number of contacts being viewed to reduce the number of underlying SIP
                        subscriptions | 200 OK | 503 Service Unavailable |
| 212 | Max number of requests per second reached | Wait before sending another request | 503 Service Unavailable | 503 Service Unavailable |

| Element | Definition |
|---|---|
| <person> | This element contains information on the overall reachability of the contact. |
| <tuple id> | This element identifies the device. |
| <contact> | This element identifies the contact SIP address. |
| <audio> | This element is used to indicate whether the class of service of audio (for example, phone) is
                        available. The value of true in this field is used to indicate
                        that the state being published is that of a phone device. Note
                        that it is possible for multiple classes of services to be published from the same device. |
| <text> | This element is used to indicate whether the class of service of text (for example, IM) is
                        available. The value of true in this field is used to indicate
                        that the state being published is that of an IM device. Note
                        that it is possible for multiple classes of services to be published from the same device. |
| <video> | This element is used to indicate whether the class of service of video is available. Note that
                        it is possible for multiple classes of services to be published from the same device. |
| <user-input> | This element is used to indicate activity on a device (for example voice, keyboard, pointing
                        device) |
| <model> | This element contains model information for the device. |
| <status> | This element indicates the status of the device. This value is either open or closed . |