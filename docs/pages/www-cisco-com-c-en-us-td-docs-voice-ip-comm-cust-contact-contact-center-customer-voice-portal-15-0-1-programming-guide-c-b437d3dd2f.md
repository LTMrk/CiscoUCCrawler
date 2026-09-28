---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-programming-guide-c-b437d3dd2f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/programming/guide/ccvp_b_1501-programming-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio/ccvp_b_1261-programming-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio_chapter_01001.html
retrieved_at: 2026-08-21T17:14:07.549933+00:00
---

Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio, Release 15.0(1)

# Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio, Release 15.0(1)

Updated: April 1, 2025

Chapter: Application Start Classes

## Chapter: Application Start Classes

- Application Start Classes

- Remote Execution

# Application Start Classes

## Application Start Classes

Application start classes are unlike most components in that they are not related to a call session. Application start classes
                           are instead associated with a particular application and are run when the application itself is initialized or updated. Currently,
                           only the Java API can construct code to run when an application starts.

An application can define in its application settings any number of application start classes. VXML Server will run the classes
                           sequentially in the order they appear in the application’s settings. By conforming to this order, a developer can create an
                           application start class that stores information that can then be referenced by subsequent start of application classes.

The application settings can specify that an error on a particular application start class will cancel the application’s deployment.
                           This is an optional attribute and by default the system will not allow an error in one of these classes to stop the application
                           deployment. If set, an error encountered in the class will stop the application from being deployed, an error message will
                           appear in the application server console, and an error event will be thrown to be logged by any error loggers. This attribute
                           is provided should an application require its application start class to run without error for calls the application to succeed.

There are four situations where the application start class is run:

The application server is launched. VXML Server is configured to begin initializing applications once it is loaded by the
                                 application server. This process triggers each application’s start classes to be run.

The VXML Server web application is restarted. Most application servers provide the ability to restart just a certain web application
                                 running within it rather than restarting the entire application server. The act of restarting the web application that defines
                                 the VXML Server will prompt it to start the application loading process just like an application server restart.

An application is deployed after the VXML Server has started. Using the deployment administration scripts, an application
                                 can be deployed while the system is actively handling calls to other applications. When the application is loaded, the application
                                 start classes will be run.

An application is updated. The process of updating an application prompts VXML Server to create a new instance of the application
                                 in memory, while keeping the old instance in memory long enough for all existing callers to complete their calls. The new
                                 application must initialize itself, including calling all application start classes.

An application start class only has access to the Global API, which allows for the creation of global and application data.
                           It does not have access to the Session API because it is not run within a call session and is associated only with an application,
                           not a call.

The main purpose for an application start class would be to prepare information that would then be used by call-specific components,
                           especially if the setup process takes a long time to run. For example, if an application has elements that are written to
                           access a backend database or mainframe system, they could initiate connections to that system each time they need to. This,
                           however, would incur overhead in initiating the connection each time. An alternative would be to write an application start
                           class that will open up the connection to the database or mainframe and perform all necessary setup. The class could take
                           as long as necessary to run because the application is being initialized and is not actively taking calls. The application
                           start class could then store the connection in application data that the elements could then access when needed. This solution
                           incurs overhead at the best time, during application initialization, and eliminates it at the worst time, during a call.

The application start class action is built by implementing the Unified CVP class StartApplicationInterface found in the com.audium.server.proxy package. It contains a single method named onStartApplication that is the method to run for the application start class. This method receives a single argument, an instance of ApplicationStartAPI . This class belongs to the Global API and is used to access and create application data and global data (see the User Guide for Cisco Unified CVP VXML Server and Unified Call Studio for details on application and global data). The method does not have a return value. It is expected that should an unrecoverable
                           error occur, the application start class will throw an AudiumException .

### Remote Execution

For remote execution of the Application Start Classes, the following syntax for URI is to be used:

For HTTP and RPC call: remote://system/?classurl=<fully_qualified_java_class_path>

For example: remote://system/?classurl=com.cisco.cvp.callstudio.Action.TestStartApplicationClass

remote://system indicates that the configurations will be fetched from the Remote Url Settings property tab which is application-specific.

If a direct remote server URI is provided, then that IP:Port will be used and not fetched from the Remote Url Settings property tab.

For example: http://<IP>:<Port>/<target_path>/?classurl=<fully_qualified_java_class_path>

| Note | If a direct remote server URI is provided, then that IP:Port will be used and not fetched from the Remote Url Settings property tab. For example: http://<IP>:<Port>/<target_path>/?classurl=<fully_qualified_java_class_path> |
|---|---|