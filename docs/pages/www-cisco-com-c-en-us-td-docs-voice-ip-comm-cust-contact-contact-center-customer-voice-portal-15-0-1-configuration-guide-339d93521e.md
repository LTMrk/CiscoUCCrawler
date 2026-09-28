---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-339d93521e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_150-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1501_remote-custom-api-server-configuration.html
retrieved_at: 2026-08-21T02:58:28.709371+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: March 5, 2025

Chapter: Remote Custom API Server Configuration

## Chapter: Remote Custom API Server Configuration

# Remote Custom API Server Configuration

## Overview

Remote execution of custom code facilitates the execution of custom code and libraries in the remote server outside VXML Server.
                           This feature allows the separation of core IVR application (business logic) and extended business logic (custom code not shipped
                           with the Call Studio application) and operates on a distinct instance that is not shared by Call or VXML Server. This improves
                           system stability and performance because the fundamental services are functioning exclusively for their respective applications.
                           This in turn provides the sufficient resources and reduces the application instability caused by excessive resource utilization.
                           A component is introduced in Call Studio to facilitate the communication and separation between external applications and
                           core applications.

The table below provides the list of elements and whether those elements have the remote execution option or not. For more
                           information on the configuration details, see the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio .

Element Type

Element Name

Remote Execution Option

Audio

Audio

No

Custom_Audio

Yes

Call Control

Transfer

No

Cisco

ReqICMLabel

No

Callback

Callback_Add

No

Callback_Disconnect_Caller

Callback_Enter_Queue

Callback_Get_Status

Callback_Reconnect

Callback_Set_Queue_Defaults

Callback_Update_Status

Calback_Validate

Callback_Wait

Callback_Ready

Commerce

Currency

No

Currency_with_confirm

Context

Application_Modifier

No

Date & Time

Date

No

Date_With_Confirm

Time

Time_With_Confirm

Form

Form

No

Custom Form

Yes

Form_With_Confirm

No

Custom Form_With_Confirm

Yes

Integration

Database

Yes

FTP_Client

No

REST_Client

No

Math

Counter

No

Math

Set Value

Yes

Menu

Yes_No_Menu

No

Custom Yes_No_Menu

Yes

2_Option_Menu

No

Custom 2_Option_Menu

Yes

3_Option_Menu

No

Custom 3_Option_Menu

Yes

4_Option_Menu

No

Custom 4_Option_Menu

Yes

5_Option_Menu

No

Custom 5_Option_Menu

Yes

5_Option_Menu

No

Custom 4_Option_Menu

Yes

6_Option_Menu

No

Custom 6_Option_Menu

Yes

7_Option_Menu

No

Custom 7_Option_Menu

Yes

8_Option_Menu

No

Custom 8_Option_Menu

Yes

9_Option_Menu

No

Custom 9_Option_Menu

Yes

Notification

Alert

No

Email

Number Capture

Digits

No

Custom Digits

Yes

Digits_With_Confirm

No

Custom Digits_With_Confirm

Yes

Number

No

Custom Custom Number

Yes

Number_With_Confirm

No

Custom Number_With_Confirm

Yes

Phone

No

Custom Phone

Yes

Phone_With_Confirm

No

Custom Phone_With_Confirm

Yes

Record

Record

No

Record_With_Confirm

Video

Video Connect

No

Virtual Agent

Dialogflow

No

DialogflowCX

DialogflowIntent

DialogflowParam

Transcribe

VirtualAgentVoice

Wxm

WxM_PCS

No

Say it Smart Plugin

Say it Smart Plugin

Yes

Logger

Remote Custom Logger

Yes

## Installation and Configurations

### Set Up Remote Server

#### Before you begin

Step 1

In the Remote Server VM, install OpenJDK 17 (version 17.0.13 or higher). .

Download OpenJDK at: https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=416&field_operating_system_target_id=436&field_architecture_target_id=All&field_java_package_target_id=All .

Step 2

Configure the JAVA_HOME environment variable under System Variables , with the respective Java installed path. For example, the path may be C:\Program Files\OpenLogic\jdk-17.0.xx.xxx-hotspot .

Step 3

Install Apache Tomcat 9 (version 9.0. 90 or higher).

Download Tomcat at: https://tomcat.apache.org/download-90.cgi .

Step 4

Stop the Tomcat server.

Step 5

Copy the customapis.war file to the webapps folder of Tomcat (for example, C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps ).

The spring boot SDK customapis.war file is located at %CVP_HOME%\util\remoteexecution folder of the VXML Server. To run the customapis.war file, you need Apache Tomcat as the web server.

Step 6

Start the Tomcat server. A folder named customapis is created in %Apache Software Foundation%\Tomcat 9.0\webapps .

Templates for web.xml and server.xml are bundled in the customapis folder in the following locations:

\customapis\WEB-INF\classes\tomcatConfig\conf\web.xml

\customapis\WEB-INF\classes\tomcatConfig\conf\server.xml

Use these files only as a reference and configure them properly according to your requirements.

The existing web.xml and server.xml files are available at the following locations:

%Apache Software Foundation%\Tomcat 9.0\conf\server.xml

%Apache Software Foundation%\Tomcat 9.0\conf\web.xml

You can replace or modify the above files.

### Running Custom Code Using Remote Server

Step 1

Bundle all the custom code that you want to run remotely in a .jar file.

Step 2

Copy the .jar file and all the dependencies to the %Apache Software Foundation%\webapps\customapis\WEB-INF\lib folder.

Step 3

Restart the Tomcat server.

The HTTP port listens at 8080 and the gRPC port listens at 8090 .

You can change the port for gRPC in the application.properties file located at %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes .

```
#server.grpc.port =8090
```

You can change the port for HTTP in the server.xml file located at %Apache Software Foundation%\Tomcat 9.0\conf .

Name of the property:

```
<Connector port="8080" protocol="HTTP/1.1"
connectionTimeout="20000"
redirectPort="8443"
maxParameterCount="1000"
 />
```

For secure connection, configure the port 8080 in the server.xml file. For more information, see Enable Security over HTTP (Self-Signed Certificate) .

To confirm if the application is running, check the spring boot starter logs in the cvp.log file located in the %Apache Software Foundation%\logs folder.

Step 4

Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running.

Step 5

To check if the gRPC server is up and running, run the command netstat -a | findstr 8090 .

Step 6

Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application.

Step 7

Restart the VXML Server for the changes to be effective.

Step 8

To run the loggers remotely, see the Loggers chapter in the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio .

Step 9

In a failure scenario:

Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog .

To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog .

### Remote Server Application Properties

The following table lists the properties in the application.properties file that is located at %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes .

Property Name

Usage

loggerPath = C:\\<any folder>\\CustomLogger

Specifies the path for running the application loggers in the remote server.

server.grpc.port = 8090

server.grpc.keyStorePath = C:\\Program Files\\OpenLogic\\jdk-17.0.xxx-hotspot\\jre\\lib\\security\\cacerts

Specifies the port and keystore path configured for gRPC.

server.grpc.keyStoreType = JCEKS

Specifies the KeyStoreType for gRPC connection.

server.grpc.keyAlgorithm = SunX509

Specifies the key algorithm used.

server.grpc.transport = TLS

Specifies the incoming secure protocol.

server.grpc.outgoing.secure.Transport = TLS

Specifies the outgoing secure protocol.

server.grpcciphers = TLS_RSA_WITH_AES_128_CBC_SHA

Colon (;) seperated secure ciphers, for example TLS_RSA_WITH_AES_128_CBC_SHA.

server.grpctlsv1dot2Enabled = true

Secure TLS versions flags, for example TLSv1.

server.grpc.protocol = TLS

Specifies the secure protocol used.

server.grpc.useClientAuth = true

Specifies whether a client certificate is needed or not.

server.grpc.enableRemoteAuthentication = false

Specifies whether gRPC authentication is needed or not.

server.grpc.maxAllowedRequests = 1000

Specifies the maximum allowed calls at a time.

restapi.security.enabled = false

Specifies whether HTTP authentication is needed or not.

#### Heartbeat Settings in VXML Server

The heartbeat mechanism monitors each remote endpoint URL, be it HTTP or RPC.

For the End point heartbeat control following properties have been added in the vxml.properties .

These three properties have been added in the %CVP_HOME%\conf\vxml.properties .

VXML.EndpointHeartbeatEnabled = true

VXML.EndpointPingInterval = 30000

VXML.EndpointMaxPingFailure = 1

After you update the vxml.properties file, restart the VXML Server.

#### Configuring HTTP Proxy Settings in VXML Server

To configure HTTP proxy settings in VXML Server, perform the following steps:

Step 1

Open Windows Registry Editor (regedit) in the VXML Server.

Step 2

Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java\Options .

Step 3

Add the following entries:

Dhttps.proxyHost=<proxy-server hostname or fqdn or IP>

Dhttps.proxyPort=<port>

Step 4

Restart the Unified CVP VXML Server from Windows services.

#### Firewall Port Settings

To allow remote execution of custom code, add the following ports to the firewall exclusion list:

HTTP port - 8080

gRPC port - 8090

### Run the Launcher Script

A launcher script file helps you execute commands inside the docker container. The launcher script accepts commands, options,
                              and other arguments to modify its behavior.

On the windows host, after downloading the customapis-docker-windows-<version>.zip installer, you will find a launcher.bat file. To run the launcher script from the C:/Cisco/customapis directory, use the following command:

```
launcher.bat <parameter>
```

On the linux host, after downloading the customapis-docker-linux-<version>.zip installer, you will find a launcher.sh file. To run the launcher script from the /usr/local/customapis directory, use the following command:

```
launcher.sh <parameter>
```

Parameter

Action

create

Creates a directory structure

load

Loads the docker image and run the docker container

run

Run the docker container

stop

Stops the existing docker container

status

Displays the status of running docker container

### Running Custom Code Using Remote Server on Windows

Complete the following procedures to run the custom code using remote server on the windows host.

#### Load Docker image and Container on Windows Host

Follow the below steps to load the docker image and run the docker container on the windows host machine.

Step 1

Download or copy the customapis-windows-docker-<version>.zip installer zip file on the windows host.

Step 2

Create the following directory structure on the host: C:\Cisco\customapis

Step 3

Extract the archive (.zip) to the following location: C:\Cisco\customapis , where you need the Installer to be running from.

Step 4

Open the PowerShell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis .

Step 5

Use the launcher.bat file to initiate creation of external mounted folders by providing the create parameter by running the following command:

PS .\launcher.bat create

After you run the command, external mount folder gets created at location: C:\Cisco\customapis

Step 6

Bundle all the custom code that you want to run remotely in .jar file.

Step 7

Copy the .jar files and all the dependency jars to the C:\Cisco\customapis\external\lib folder.

Step 8

Use the launcher.bat file to load the container by providing the load parameter by running the following command:

```
PS .\launcher.bat load
```

Step 9

Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running.

Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command:

```
PS .\launcher.bat status
```

Step 10

Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application.

Step 11

Restart the VXML Server for the changes to be effective.

Step 12

In a failure scenario:

Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog .

To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog .

Check Remote Windows Host docker container logs: C:\Cisco\customapis\cvpLogs\cvp.log .

Check Tomcat logs: C:\Cisco\customapis\tomcatLogs

#### Configure Secure and Authenticate Calls for Docker Container on Windows Host

Follow the below steps to configure secure call and authenticate calls for docker containers on the windows host machine.

The configuration of secure and authenticated setup is a one-time activity and not required for subsequent Docker releases.

If the Windows system reboots or Docker restarts, you need to start the Docker container again by running the launcher.bat file with the run parameter.

Step 1

Bundle all the custom code that you want to run remotely in .jar file.

Step 2

Copy the .jar files and all the dependency jars to the C:\Cisco\customapis\external\lib folder.

Step 3

Open the Powershell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis .

Step 4

Use the launcher.bat file to start the container by providing the run parameter by running the following command:

```
PS .\launcher.bat run
```

Step 5

Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running.

Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command:

```
PS .\launcher.bat status
```

Step 6

Perform steps a to c of the Create Credentials for Authentication in Remote Server and Create Keystore Password for Remote Server procedures respectively.

Step 7

Use the following command in PoweShell application to get the <container_id> :

```
PS &$Env:DOCKER_HOME\docker ps
```

Step 8

Use the following command in PowerShell application to open the command prompt of running docker container:

```
PS &$Env:DOCKER_HOME\docker exec -it <container_id>  cmd.exe
```

Step 9

Use the following command in the command prompt of the docker container and perform steps 1 to 3 of the Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC procedure:

```
%JAVA_HOME%\bin\keytool -genkey -keyalg RSA -alias customcode_certificate -keystore C:\Users\ContainerAdministrator\external\security\cacerts -storetype JCEKS -keysize 2048
```

After adding the certificate, close the command prompt terminal of the docker container.

If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) .

Step 10

Use the launcher.bat file to stop the container by providing the stop parameter by running the following command:

```
PS .\launcher.bat stop
```

Step 11

Modify the application.properties file and server.xml file to configure these files with proper values for a secure and authenticated gRPC and HTTP call as provided in the section External Mounted Folders or Files Usage and Location .

Step 12

Perform steps 3 to 5 of this procedure again to start the container and view the status of the container.

Step 13

Perform steps 1 to 6 of the Import Self-Signed Certificate of Remote Server in VXML Server for HTTP or gRPC procedure to add the remote server certificate in VXML Server.

Step 14

Perform steps 1 to 7 of the Enable Secure Connection in Call Studio and VXML Server to configure the applications on Call studio and VXML Server procedure to configure the applications on Call studio and VXML Server for a secure and authenticated call.

Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios .

Step 15

In a failure scenario:

Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog .

To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog .

Check Remote Windows Host docker container logs: C:\Cisco\customapis\cvpLogs\cvp.log .

Check Tomcat logs: C:\Cisco\customapis\tomcatLogs .

### Running Custom Code Using Remote Server on Linux

Complete the following procedures to run the custom code using remote server on the Linux host.

#### Load Docker Image and Container on Linux Host

Follow the below steps to load the docker image and run the docker container on the linux host machine.

Step 1

Download or copy the customapis-docker-linux-<version>.zip installer zip on the linux host.

Step 2

Create the following directory structure on the host: /usr/local/customapis

Step 3

Run the following command to extract the archive (.zip) to the location: /usr/local/customapis , where you need the Installer to be running from:

```
$ unzip customapis-docker-linux-<version>.zip
```

Step 4

Run the following command to provide permission to the launcher.sh file:

```
$ chmod +x launcher.sh
```

Ensure that you have permissions to directory location: /usr/local/customapis

Step 5

Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

Step 6

Use the launcher.sh file to initiate creation of external mounted folders by providing the create parameter by running the following command:

```
$ ./launcher.sh create
```

After you run the command, external mount folder gets created at location: /usr/local/customapis

Step 7

Bundle all the custom code that you want to run remotely in .jar file.

Step 8

Copy the .jar files and all the dependency jars to the /usr/local/customapis/external/lib folder.

Step 9

Use the launcher.sh file to load the container by providing the load parameter by running the following command:

```
$ ./launcher.sh load
```

Step 10

Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running.

Use the launcher.sh file to view the status of the container by providing the status parameter by running the following command:

```
$ ./launcher.sh status
```

Step 11

Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application.

Step 12

Restart the VXML Server for the changes to be effective.

Step 13

In a failure scenario:

Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog .

To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog .

Check Remote Linux Host docker container logs: /usr/local/customapis/logs/cvp.log .

#### Configure Secure and Authenticate Calls for Docker Container on Linux Host

Follow the below steps to configure secure call and authenticate calls for docker containers on the linux host machine.

The configuration of secure and authenticated setup is a one-time activity and does not need to be repeated for subsequent
                                                Docker releases.

If the Linux system reboots or Docker restarts, you need to start the Docker container again by running the launcher.sh file with the run parameter.

Step 1

Bundle all the custom code that you want to run remotely in .jar file.

Step 2

Copy the .jar files and all the dependency jars to the /usr/local/customapis/external/lib folder.

Step 3

Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

Step 4

Use the launcher.sh file to start the container by providing the run parameter by running the following command:

```
$ ./launcher.sh run
```

Step 5

Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running.

Use the launcher.sh file to view the status of the container by providing the status parameter by running the following command:

```
$ ./launcher.sh status
```

Step 6

Perform steps a to c of the Create Credentials for Authentication in Remote Server and Create Keystore Password for Remote Server procedures respectively.

Step 7

Use the following command to get the <container_id> :

```
$ docker ps
```

Step 8

Use the following command to open the command prompt for running docker container:

```
$ docker exec -it <container_id> /bin/sh
```

Step 9

Use the following command in the command prompt of the docker container and perform steps 1 to 3 of the Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC procedure:

```
$JAVA_HOME/bin/keytool -genkey -keyalg RSA -alias customcode_certificate -keystore /usr/local/customapis/external/security/cacerts -storetype JCEKS -keysize 2048
```

If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) .

Step 10

Use the launcher.sh file to stop the container by providing the stop parameter by running the following command:

```
$ ./launcher.sh stop
```

Step 11

Modify the application.properties file and server.xml file to configure these files with proper values for a secure and authenticated gRPC and HTTP call as provided in the section External Mounted Folders or Files Usage and Location .

Step 12

Perform steps 3 to 5 of this procedure again to start the container and view the status of the container.

Step 13

Perform steps 1 to 6 of the Import Self-Signed Certificate of Remote Server in VXML Server for HTTP or gRPC procedure to add the remote server certificate in VXML Server.

Step 14

Perform steps 1 to 7 of the Enable Secure Connection in Call Studio and VXML Server to configure the applications on Call studio and VXML Server procedure for a secure and authenticated call.

Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios .

Step 15

In a failure scenario:

Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog .

To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog .

Check Remote Linux Host docker container logs: /usr/local/customapis/logs/cvp.log .

Check Tomcat logs: /usr/local/customapis/logs .

### External Mounted Folders or Files Usage and Location

The following table lists various configuration files and log files being used and their usages for running the docker container
                              with proper config values.

Ensure to restart the container after modifying the files for the changes to take effect.

File and Location

Usage

.jar file and dependencies

Linux : /usr/local/customapis/external/lib

Windows : C:\Cisco\customapis\external\lib

Bundles all the custom code that you want to run remotely in a .jar file.

Copy the .jar file and all the dependencies to the C:\Cisco\customapis\external\lib folder (Windows) and /usr/local/customapis/external/lib folder (Linux)

.class files

Linux : /usr/local/customapis/external/classes

Windows : C:\Cisco\customapis\external\classes

application.properties

Linux : /usr/local/customapis/external/conf/application.properties

Windows : C:\Cisco\customapis\external\conf\application.properties

For grpc Authentication, set the server.grpc.enableRemoteAuthentication flag to true .

For grpc Secure:

set the server.grpc.secure flag to true .

(For Windows) set the server.grpc.keyStorePath to C:/Users/ContainerAdministrator/external/security/cacerts .

For http authentication, set the restapi.security.enabled flag to true .

server.xml

Linux : /usr/local/customapis/external/conf/tomcatConfig/conf/server.xml

Windows : C:\Cisco\customapis\external\conf\tomcatConfig\conf\server.xml

For http Secure Connection, replace the existing connector <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" /> with the following:

```
<Connector SSLEnabled="true" acceptCount="1500" ciphers="TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256" clientAuth="false" disableUploadTimeout="true" enableLookups="false" executor="tomcatThreadPool" keyAlias="customcode_certificate" keystoreFile="C:\Users\ContainerAdministrator\external\security\cacerts" keystorePass="changeit" keystoreType="JCEKS" maxHttpHeaderSize="8192" port="8080" protocol="org.apache.coyote.http11.Http11NioProtocol"
scheme="https" secure="true" sslImplementationName="org.apache.tomcat.util.net.jsse.JSSEImplementation" sslProtocol="TLS" sslEnabledProtocols="TLSv1.2"/>
```

Ensure that you add the following parameters to the connector according to the configurations done for your remote server:

keyAlias

keystoreFile

keystorePass

port

log4j2.xml

Linux : /usr/local/customapis/external/conf/conf/log4j2.xml

Windows : C:\Cisco\customapis\external\conf\log4j2.xml

For enhanced logging, ensure that you change the level of logging from info to debug as shown below:

```
<Logger name="com.cisco.cvp.customapi" level="debug"
additivity="false">
<AppenderRef ref="LogToFile" />
</Logger>
```

setenv.bat

Linux : /usr/local/customapis/external/conf/setenv.bat

Windows : C:\Cisco\customapis\external\conf\setenv.bat

For setting user defined variables for the tomcat service, you can modify the setenv.bat file according to requirement.

A pre-configured setenv.bat has already been added to the specific location.

context.xml

Linux : /usr/local/customapis/external/conf/context.xml

Windows : C:\Cisco\customapis\external\conf\tomcatConfig\conf\context.xml

For adding resource, you can modify the context.xml according to your requirement.

Tomcat logs:

Linux : /usr/local/customapis/logs/

Windows : C:\Cisco\customapis\tomcatLogs

Remote server logs:

Linux : /usr/local/customapis/logs/cvp.log

Windows : C:\Cisco\customapis\cvpLogs\cvp.log

For debugging, tomcat catalina logs and remote server logs are available here.

docker-compose.yaml

Linux : /usr/local/customapis/docker-compose.yaml

Windows : C:\Cisco\customapis\docker-compose.yaml

For modifying the memory limit and CPU usage specified for the container, use the docker-compose.yaml file.

### Upgrade Subsequent Docker Released Images (Windows)

Step 1

Open the PowerShell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis .

Step 2

Use the launcher.bat file to stop the container by providing the stop parameter by running the following command:

```
PS .\launcher.bat stop
```

Step 3

Download or copy the customapis-windows-docker-<version>.zip installer zip file on the windows host.

Step 4

Extract the archive (.zip) to the following location and replace the existing files if necessary: C:\Cisco\customapis , where you need the Installer to be running from.

Step 5

Use the launcher.bat file to load the container by providing the load parameter by running the following command:

```
PS .\launcher.bat load
```

Step 6

Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running.

Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command:

```
PS .\launcher.bat status
```

Step 7

Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application.

Step 8

Restart the VXML Server for the changes to be effective.

Step 9

In a failure scenario:

Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog .

To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog .

Check Remote Server or Windows Host docker container logs:

C:\Cisco\customapis\cvpLogs\cvp.log

Check Tomcat logs:

C:\Cisco\customapis\tomcatLogs

### Upgrade Subsequent Docker Released Images (Linux)

Step 1

Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

Step 2

Use the launcher.sh file to stop the container by providing the stop parameter by running the following command:

```
$ ./launcher.sh stop
```

Step 3

Download or copy the customapis-docker-linux-<version>.zip installer zip on the linux host.

Step 4

Create the following directory structure on the host: /usr/local/customapis

Step 5

Run the following command to extract the archive (.zip) to the location and replace the existing files if necessary: /usr/local/customapis , where you need the Installer to be running from:

```
$ unzip customapis-docker-linux-<version>.zip
```

Step 6

Run the following command to provide permission to the launcher.sh file:

```
$ chmod +x launcher.sh
```

Ensure that you have permissions to directory location: /usr/local/customapis

Step 7

Use the launcher.sh file to load the container by providing the load parameter by running the following command:

```
$ ./launcher.sh load
```

Step 8

Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running.

Use the launcher.sh file to view the status of the container by providing the status parameter by running the following command:

```
$ ./launcher.sh status
```

Step 9

Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application.

Step 10

Restart the VXML Server for the changes to be effective.

Step 11

In a failure scenario:

Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog .

To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog .

Check Remote Server or Linux Host docker container logs:

/usr/local/customapis/logs/cvp.log

Check Tomcat logs:

/usr/local/customapis/logs

### Remote Execution of Custom Logger

Follow the steps to enable remote execution of custom logger on Windows or Linux host:

#### Before you begin

For changes specific to the VXML Server, see the Remote Execution of Custom Logger section of the Loggers chapter in the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio .

Ensure that you run the launcher script. Refer to the section Run the Launcher Script for more information.

Step 1

Use the launcher.bat file (Windows) or launcher.sh file (Linux) stop the container by providing the stop parameter by running the following command:

Windows :

```
PS .\launcher.bat stop
```

Linux :

```
$ ./launcher.sh stop
```

Step 2

Provide the existing path in the application.properties file of the remote server for the loggerPath .

For example:

Linux : loggerPath= /usr/local/customapis/external/CustomLogger

Windows : loggerPath= C:/Users/ContainerAdministrator/external/Customlogger

Step 3

Copy the VXMLServer\applications\<applicationName>\data folder to the loggerPath in the remote server machine.

For example:

Linux : loggerPath= /usr/local/customapis/external/CustomLogger

Windows : loggerPath= C:/Users/ContainerAdministrator/external/Customlogger

Step 4

Copy the VXMLServer\dtds folder to the loggerPath in the remote server machine. The logger folder must contain both /applications and /dtds folders.

Step 5

Use the launcher.bat file (Windows) or launcher.sh file (Linux) to run the container by providing the run parameter by running the following command:

Windows : PS .\launcher.bat run

Linux : $ ./launcher.sh run

Step 6

Load the custom logger instances of the remote windows host machine using the cvp.log file located at /usr/local/customapis/logs/cvp.log (Linux) or C:\Cisco\customapis\cvpLogs\cvp.log (Windows).

### Generate CA-signed Certificate for Remote Server (Docker)

If you already have a CA-signed certificate for the host, follow the steps below. If not, generate a self-signed certificate
                                          using the procedure in Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC and sign it with the relevant Certificate Authority (CA).

#### Import CA-signed Certificate for Remote Server (Docker)

Step 1

To import the root certificate issued by the Certificate Authority, follow the below steps:

Copy the root.pem file in the following external directory location:

Windows Docker : C:\Cisco\customapis\external\security\root.pem

Linux Docker : /usr/local/customapis/external/security/root.pem

Access the Docker container by running the following command:

Windows Docker : PS &$Env:DOCKER_HOME\docker exec -it <container_id> cmd.exe

Linux Docker : $ docker exec -it <container_id> /bin/sh

Run the following command to import the root certificate into a Java KeyStore (JKS):

```
%JAVA_HOME%\bin\keytool -storetype JCEKS -keystore C:\Cisco\customapis\external\security\cacerts -import -v -trustcacerts -alias root -file C:\Cisco\customapis\external\security\root.pem
```

```
$JAVA_HOME/bin/keytool -storetype JCEKS -keystore /usr/local/customapis/external/security/cacerts -import -v -trustcacerts -alias root -file /usr/local/customapis/external/security/root.pem
```

Step 2

To import the CA-signed certificate to the remote server, follow the below steps:

Copy the host.pem file in the following external directory location:

Windows Docker : C:\Cisco\customapis\external\security\root.pem

Linux Docker : /usr/local/customapis/external/security/root.pem

Access the Docker container by running the following command:

Windows Docker : PS &$Env:DOCKER_HOME\docker exec -it <container_id> cmd.exe

Linux Docker : $ docker exec -it <container_id> /bin/sh

Run the following command to import the root certificate into a Java KeyStore (JKS):

```
%JAVA_HOME%\bin\keytool -storetype JCEKS -keystore C:\Cisco\customapis\external\security\cacerts -import -v -trustcacerts -alias customcode_certificate -file C:\Cisco\customapis\external\security\host.pem
```

```
$JAVA_HOME/bin/keytool -storetype JCEKS -keystore /usr/local/customapis/external/security/cacerts -import -v -trustcacerts -alias customcode_certificate -file /usr/local/customapis/external/security/host.pem
```

## Security Configuration

This section covers the steps which need to be configured for enabling a secure connection between the remote server and VXML
                           Server.

### Authentication for Remote Server

#### Create Credentials for Authentication in Remote Server

##### Before you begin

In a REST client, for example Postman, enter the following details to create credentials:

In the POST request, add the URL http://<remote_machine_IP>:8080/customapis/actionapi/add-user-credentials .

In the above URL, replace remote server, IP address, and port as needed.

In Request Body , add userid and secret as key-value. Make sure the provided userid and secret to be non-null values.

In the Headers tab, you must enable Content-Type as application/x-www-form-urlencoded .

After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously.

#### Enable gRPC Authentication in Remote Server

Step 1

Log in to the remote server machine.

Step 2

Navigate to %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes .

Step 3

Open the application.properties file and set the server.grpc.enableRemoteAuthentication flag to true.

Step 4

Restart Apache Tomcat Server.

#### Enable HTTP Authentication in Remote Server

Step 1

Log in to the remote server machine.

Step 2

Navigate to %Apache Software Foundation%\Tomcat9.0\webapps\customapis\WEB-INF\classes .

Step 3

Open the application.properties file and set the restapi.security.enabled flag to true.

Step 4

Restart Apache Tomcat Server.

### Secure Connection Setup Between Remote Server and VXML Server

#### Create Keystore Password for Remote Server

##### Before you begin

In a REST client, for example Postman, enter the following details to create credentials:

In the POST request, add the URL http://<remote_machine_IP>:8080/customapis/actionapi/add-keystore-password .

In the above URL, replace remote server, IP address, and port as required.

In Request Body , add keyStorePassword as the key-value . Ensure that the provided keyStorePassword is a non-null value.

In the Headers tab, you must enable Content-Type as application/x-www-form-urlencoded .

After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously.

#### Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC

##### Before you begin

It is recommended to change the default keystore password (which is usually 'changeit'). To change the password, run the command: %JAVA_HOME%\jdk-17.0.xx-hotspot\jre\bin>keytool -storepasswd -new <newpassword> -keystore ..\lib\security\cacerts -storetype
                                       JCEKS -storepass <defaultpassword>

Step 1

Open the command prompt and execute the following command in cmd.exe with proper alias: %JAVA_HOME%\jdk-17.0.xx-hotspot\jre\bin>keytool -genkey -keyalg RSA -alias customcode_certificate -keystore ..\lib\security\cacerts
                                                -storetype JCEKS -keysize 2048

Step 2

Once you execute the command, answer the questions.

For example:

```
Enter keystore password: *************
What is your first and last name? [Unknown]:  CustomRemoteServer----------------→ The CN should same as the FQDN of the machine What is the name of your organizational unit?
  [Unknown]:  CCBU
What is the name of your organization?
  [Unknown]:  CISCO
What is the name of your City or Locality?
  [Unknown]:  KA
What is the name of your State or Province?
  [Unknown]:  BLR
What is the two-letter country code for this unit?
  [Unknown]:  IN
Is CN= CustomRemoteServer , OU=CCBU, O=CISCO, L=KA, ST=BLR, C=IN correct?
  [no]:  yes
Enter key password for <customcode_certificate>
        (RETURN if same as keystore password):
done
```

Step 3

Now, you can import the self-signed certificate.

#### Generate CA-signed Certificate for Remote Server HTTP or gRPC

If you already have a CA-signed certificate for the host, follow the steps below. If not, generate a self-signed certificate
                                             using the procedure in Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC and sign it with the relevant Certificate Authority (CA).

##### Import CA-signed Certificate for Remote Server

Step 1

To import the root certificate issued by the Certificate Authority, follow the below steps:

Copy the root.pem file in the following location: %JAVA_HOME%\lib\security

Go to directory location %JAVA_HOME%\jre\bin .

Open the command prompt and execute the following command in cmd.exe with proper alias:

```
keytool.exe -storetype JCEKS -keystore ..\lib\security\cacerts -import -v -trustcacerts -alias root -file ..\lib\security\root.pem
```

Step 2

To import the CA-signed certificate to the remote server, follow the below steps:

Copy the host.pem file in the following location: %JAVA_HOME%\lib\security

Go to directory location: %JAVA_HOME%\jre\bin .

Open the command prompt and execute the following command in cmd.exe with proper alias:

```
keytool.exe -storetype JCEKS -keystore ..\lib\security\cacerts -import -v -trustcacerts -alias customcode_certificate -file ..\lib\security\host.pem
```

#### Generate Remote Server ECDSA Certificate with Open SSL

##### Before you begin

The Remote Server enables a variant of the Digital Signature Algorithm that are known as an Elliptic Curve Digital Signature
                                    Algorithm (ECDSA). Remote Server supports either ECDSA or RSA. RSA remains the default cryptography algorithm. However, looking
                                    at the requirements, we can enable or disable ECDSA.

For disabling ECDSA, you must delete the existing ECDSA aliases and generate RSA certificates again.

Step 1

Download OpenSSL (64-bit) and install on your remote computer.

Step 2

Add OpenSSL bin path to the Windows environment path variable.

For example, path=C:\Program Files\OpenSSL-Win64\bin

Step 3

Go to C:\Cisco\CVP\conf\security

Step 4

From the command prompt, run the following command to generate the private keys for the remote server: openssl ecparam -name prime256v1 -genkey -noout -out remoteserver-private-key.pem

Step 5

Run the following command to generate the self-signed certificates for the remote server: openssl req -new -key remoteserver-private-key.pem -x509 -nodes -days 365 -out remoteserver-cert.pem

Step 6

Enter the values for the following fields when prompted:

```
Country Name (2 letter code) []: < >
State or Province Name (full name) []: < >
Locality Name (for example, city) []: < >
Organization Name (for example, company) []: < >
Organizational Unit Name (for example, section) []: < >
Common Name (for example, server FQDN or your name) []: < >
Email Address []: < >
Please enter the following extra attributes to be sent with your certificate request:
A challenge password []: < >
An optional company name []: < >
```

Enter a period (.) to leave the following fields blank:

Common Name

Email Address

Challenge password

An optional company name

You can generate a certificate after entering all the details.

Step 7

Run the following command to append the keys and certificates in one file: cat remoteserver-private-key.pem remoteserver-cert.pem > remoteserver-certificate-private.pem

Step 8

Run the following command to export the certificates to the Remote server: openssl pkcs12 -export -inkey remoteserver-private-key.pem -in remoteserver-certificate-private.pem -out cert_remoteserver.p12
                                                -name remoteserver_certificate

```
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

Step 9

Go to C:\Cisco\CVP\conf\security and run the following command to delete the existing RSA certificates for the remote server: C:\Cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias remoteserver-certificate -storepass <CVP
                                                keystore password>

Step 10

Run the following command to import the ECDSA certificates to the keystore: C:\Cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_remoteserver.p12 -srcstoretype PKCS12 -destkeystore
                                                .keystore -deststoretype JCEKS -alias remoteserver_certificate Importing keystore cert_remoteserver.p12 to .keystore...

```
Enter destination keystore password:
Enter source keystore password:
[Storing.keystore]
```

Step 11

Restart the remote server.

Step 12

In the new browser tab, type the following and download the certificates: https://<remote ip>:8080

#### Enable Security over gRPC (Self-Signed Certificate) in Remote Server

Step 1

Log in to the remote server machine.

Step 2

Make sure the the self-signed certificate for the remote server machine is generated.

Step 3

Navigate to the %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes directory.

Step 4

Launch the application.properties file and set the server.grpc.secure flag to true.

Step 5

Provide the .keystore path for the server.grpc.keyStorePath flag.

For example: C:\\Program Files\\OpenLogic\\jdk-17.0.11-hotspot\\jre\\lib\\security\\cacerts (make sure that keystore exists in that machine).

Step 6

Restart the Remote Apache Tomcat server.

#### Enable Security over HTTP (Self-Signed Certificate) in Remote Server

Step 1

Log in to the remote server machine.

Step 2

Ensure that the self-signed certificate for the remote server machine is generated.

Step 3

Navigate to the %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes directory.

Step 4

Open the application.properties file, set the restapi.security.enabled flag to true, and save the file.

Step 5

Navigate to the %Apache Software Foundation%\Tomcat 9.0\conf directory.

Step 6

Open the server.xml file and provide the connector with the port number, and mention the respective keystore password.

For Example :

```
<Connector SSLEnabled="true" acceptCount="1500"
ciphers="TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256" 
clientAuth="false" disableUploadTimeout="true" enableLookups="false" executor="tomcatThreadPool" keyAlias="customcode_certificate"
keystoreFile="C:\Program Files\Java\jre1.8.0_271\lib\security\cacerts" keystorePass="changeit" keystoreType="JCEKS" maxHttpHeaderSize="8192"
port="8080" protocol="org.apache.coyote.http11.Http11NioProtocol" scheme="https" secure="true" 
sslImplementationName="org.apache.tomcat.util.net.jsse.JSSEImplementation" sslProtocol="TLS" sslEnabledProtocols="TLSv1.2"/>
```

Step 7

Save the server.xml file and restart the remote Apache Tomcat server.

#### (Optional) Enabling Mutual TLS for gRPC and HTTP in Remote Server

Step 1

Import the certificate for VXML Server in the RemoteServer java keystore .

Step 2

For gRPC, in the application.properties file, available at %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes , change the following property to true:

```
server.grpc.useClientAuth = true
```

Step 3

For HTTP, in the server.xml file, available at %Apache Software Foundation%\Tomcat 9.0\conf\server.xml , change the following property to true:

```
“clientAuth" flag = true
```

Step 4

Restart the Apache Tomcat server.

### Secure Connection Set Up for  VXML Server

#### Enable Secure Connection in Call Studio and VXML Server

##### Before you begin

Step 1

Go to the Call Studio application.

Step 2

Right-click on the application, which needs to be in secure connection, and select Properties .

Step 3

In the Call Studio Properties tab, click Remote URL Settings .

Step 4

Choose HTTP or RPC as required

Step 5

Click the Secure Connection checkbox to provide a secure connection.

You must provide FQDN for HTTP and gRPC connection type in the address field for secure connection.

Step 6

For FQDN, add <IP><space><FQDN(hostname)> in the %drivers%\etc\hosts file in the VXML Server.

Step 7

Save and deploy the application. Restart the VXML Server.

For example: All the applications utilizing a port on the VXML Server for gRPC must be re-deployed with the same secure or
                                                            non-secure configurations if the port is used for both secure and non-secure calls.

When several remote servers or load end points are added for load balancing, all of those servers must have the same secure
                                                            or non-secure configurations when used simultaneously. This is because all the added servers have the same remote URL settings.

Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios .

#### Import Self-Signed Certificate of Remote Server in VXML Server for HTTP or gRPC

Step 1

Launch the URL https://<remote_server_IP>:8090/ to download the certificate.

Step 2

Upload the certificate in the %CVP_HOME%\conf\security folder where the VXML Server is hosted.

Step 3

Import the certificate using the following command: %CVP_HOME%\jdk-8.0.372.07-hotspot\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype
                                                JCEKS -alias <any_alias> -file %CVP_HOME%\conf\security\<FQDN_remote_server.cer> %CVP_HOME%\jdk-17.0.11-hotspot\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype
                                                JCEKS -alias <any_alias> -file %CVP_HOME%\conf\security\<FQDN_remote_server.cer>

Where, <FQDN_remote_server.cer> is the certificate downloaded in step 1, which is named after the FQDN of remote server.

Use FQDN instead of IP address for a secure gRPC connection. The common name (CN) of the certificate should be same as the
                                                            address mentioned in the studio settings.

Step 4

Enter the keystore password when prompted.

Run the DecryptKeystoreUtil.bat file located at %CVP_HOME%\bin to view the keystore password.

Step 5

Make sure that the connection type in the Call Studio application is changed to HTTP or gRPC accordingly. Also, ensure the Secure Connection checkbox is enabled.

Step 6

Save and deploy the Call Studio application and restart the VXML Server.

## Monitoring and Serviceability

Spring boot provides enhanced serviceability and has a set of APIs for monitoring and serviceability.

HTTP port listens at 8080 and gRPC port listens at 8090 .

Spring Boot Starter Actuator : http://<remote_IP>:<Port>/customapis/actuator . This API provides monitoring facilities around the services:

beans : http://<IP>:<Port>/customapis/actuator/beans

health-path : http://<IP>:<Port>/customapis/actuator/health/{*path}

health : http://<IP>:<Port>/customapis/actuator/health

info : http://<IP>:<Port>/customapis/actuator/info

shutdown : http://<IP>:<Port>/customapis/actuator/shutdown

loggers : http://<IP>:<Port>/customapis/actuator/loggers

loggers-name : http://<IP>:<Port>/customapis/actuator/loggers/{name}

heapdump : http://<IP>:<Port>/customapis/actuator/heapdump

thread dump : http://<IP>:<Port>/customapis/actuator/threaddump

Prometheus : http://<IP>:<Port>/customapis/actuator/prometheus

metrics-requiredMetricName : http://<IP>:<Port>/customapis/actuator/metrics/{requiredMetricName}

metrics : http://<IP>:<Port>/customapis/actuator/metrics

scheduled tasks : http://<IP>:<Port>/customapis/actuator/scheduledtasks

To check the health of the application, access the URL: http://remote_ip:8080/customapis/actuator/health . The UP status denotes that the application is running.

To check the memory used by the application, access the URL: http://remote_ip:8080/customapis/actuator/metrics/jvm.memory.used .

To check the CPU usage, access the URL: http://remote_ip:8080/customapis/actuator/metrics/process.cpu.usage .

To check the current number of live threads, access the URL: http://remote_ip:8080/customapis/actuator/metrics/jvm.threads.live .

To analyze the state of all the threads of an application at a given time, access the URL: http://remote_ip:8080/customapis/actuator/threaddump .

A heap dump is a snapshot of all the objects that are in memory in the JVM at a certain moment. It is useful for troubleshooting
                              memory-leak problems and optimising memory usage in Java applications.

To download the heap dump, access the URL: http://remote_ip:8080/customapis/actuator/heapdump .

### HTTP and gRPC Statistics

To know the statistics of HTTP and gRPC, use the following actuator URL:

/prometheus : http://remote_ip:8080/customapis/actuator/prometheus .

#### HTTP Statistics

HTTP statistics shows the summary of the requests handled along with type, status, and other attributes.

Example

```
# TYPE http_server_requests_seconds summary
http_server_requests_seconds_count{exception="None",method="GET",outcome="SUCCESS",status="200",uri="/actuator",} 1.0
http_server_requests_seconds_sum{exception="None",method="GET",outcome="SUCCESS",status="200",uri="/actuator",} 1.095763557
```

#### gRPC Statistics

gRPC statistics mentioned below represents the total count of gRPC requests handled with attributes. It shows that there is
                                 one bidirectional streaming request (BIDI_STREAMING) for the RemoteVoiceService method of com.audium.core.protobuf.RemoteExecutionService and the response code is "OK".

Example

```
# HELP grpc_server_handled_total Total number of RPCs completed on the server, regardless of success or failure.
# TYPE grpc_server_handled_total counter
grpc_server_handled_total{grpc_type="BIDI_STREAMING",grpc_service="com.audium.core.protobuf.RemoteExecutionService",
grpc_method="RemoteVoiceService",code="OK",grpc_code="OK",} 1.0
```

### VXML Server Statistics

Use the following URL for gRPC registry collection statistics: http://<IP/hostname of VXML Server>:7000/CVP/Server?stats=true .

### SNMP and Syslog Alerts

The Remote Server application displays SNMP and Syslog alerts when it encounters an exception or error. The alerts contain
                                 messages along with the stack trace for monitoring and serviceability of the application.

Following is the sample syslog and SMNP alerts displayed when the class name is not valid.

Syslog Alert

```
98: IP: Oct 05 2023 10:45:40.726 -0700: %com.cisco.ccbu.infra.serviceability.ServiceabilityManager_VXML-3-VXML_SERVER_SYSTEM_ERROR:  In application TestSNMP encountered SYSTEM_ERROR_EVENT with message: 'com.cisco.cvp.customaction' is not a valid action element class. 
<011 = Level: ERR - error conditions (3)>
```

SNMP Alert

```
Trap OID - 1.3.6.1.4.1.9.9.590 In application TestSNMP encountered SYSTEM_ERROR_EVENT with message: 'com.cisco.cvp.customaction' is not a valid action element class.
SNMP    880    trap iso.3.6.1.4.1.9.9.590
```

Similar messages are logged for other scenarios encountered after SNMP and Syslog are properly configured for the VXML Server
                                 used.

### Create User Credentials for Monitoring in Remote Server

Before you begin:

Ensure that before you activate authentication on the remote server, you must create credentials for it. Use the add-user-credentials API to both create and update these credentials. You can now create multiple users for monitoring purposes.

In a REST client, for example Postman, enter the following details to create credentials:

In the POST request, add the URL http://<remote_machine_IP>:8080/customapis/actionapi/add-user-credentials .

In the above URL, replace remote server, IP address, and port as needed.

In Request Body, add userid and secret as key-value. Make sure the provided userid and secret to be non-null values.

In Request Body, add admin as key and value as true. (true is for monitoring credentials and false for normal user credentials)

In the Headers tab, you must enable Content-Type as application/x-www-form-urlencoded .

The above credentials can be used for monitoring .

After creating the user credentials for multiple users, modify the Auth flag in the application.properties file and restart the Tomcat server.

For Docker, follow the below steps:

Stop the container by running the launcher.bat file with the stop parameter. Refer to the Run the Launcher Script section for more information.

```
PS .\launcher.bat stop
```

Start the container by running the launcher.bat file with the run parameter. Refer to the Run the Launcher Script section for more information.

```
PS .\launcher.bat run
```

### Remote Server Load Balance Status

A REST endpoint has been implemented to check the load balance status of all the gRPC and HTTP endpoint.

To check for the status of the remote server load balance, use the following URL: https://<VXML_Server_IP>:7443/CVP/Server?lbstatus=true . This API provides monitoring facilities around the services.

### Logging

#### VXML Server Configuration for Remote Server

For enhanced VXML logging for custom code, make the required configuration in the VXML Server.

In the log4j_vxml.xml file located at %CVP_HOME%\conf\ , navigate to the logger section and add the following AsyncLogger tag.

```
<AsyncLogger name="com.cisco.cvp.callserver" level="info" additivity="false">

    <AppenderRef ref="rootUniversalAppender" />

</AsyncLogger>

<AsyncLogger name="io.grpc" level="info" additivity="false">

    <AppenderRef ref="rootUniversalAppender" />

</AsyncLogger>

<AsyncLogger name="com.cisco.cvp.ivr" level="info" additivity="false">

    <AppenderRef ref="rootUniversalAppender" />

</AsyncLogger>
```

You can set the level to debug or info according to the requirement of logging level.

The log files monitored are:

%CVP_HOME%\logs\VXML\CVP <timestamp>.log

%CVP_HOME%\logs\VXML\ERROR <timestamp>.log

To monitor the health of RPC end point status , check the logs in the VXML\CVP <timestamp>.log file.

Sample Log

```
RpcEndPoint-6-com.cisco.cvp.callserver.grpc.endpoint.RpcEndPoint:  status of healthcheckgrpc.health.v1.HealthCheckResponse.ServingStatus.SERVINGEndPoint=
url=<FQDN>/<IP>:8090, statusUrl=cvv, key=<FQDN>:8090:null, status=true
```

#### Remote Server Configuration for Logging

In the log4j2.xml file located at %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes , change the level of logging from info to debug for enhanced logging.

```
<Logger name="com.cisco.cvp.customapi" level="debug"
additivity="false">
<AppenderRef ref="LogToFile" />
</Logger>
```

Log file monitored: %Apache Software Foundation%\Tomcat 9.0\logs\cvp.log .

| Element Type | Element Name | Remote Execution Option |
|---|---|---|
| Audio | Audio | No |
| Custom_Audio | Yes |
| Call Control | Transfer | No |
| Cisco | ReqICMLabel | No |
| Callback | Callback_Add | No |
| Callback_Disconnect_Caller |
| Callback_Enter_Queue |
| Callback_Get_Status |
| Callback_Reconnect |
| Callback_Set_Queue_Defaults |
| Callback_Update_Status |
| Calback_Validate |
| Callback_Wait |
| Callback_Ready |
| Commerce | Currency | No |
| Currency_with_confirm |
| Context | Application_Modifier | No |
| Date & Time | Date | No |
| Date_With_Confirm |
| Time |
| Time_With_Confirm |
| Form | Form | No |
| Custom Form | Yes |
| Form_With_Confirm | No |
| Custom Form_With_Confirm | Yes |
| Integration | Database | Yes |
| FTP_Client | No |
| REST_Client | No |
| Math | Counter | No |
| Math |
| Set Value | Yes |
| Menu | Yes_No_Menu | No |
| Custom Yes_No_Menu | Yes |
| 2_Option_Menu | No |
| Custom 2_Option_Menu | Yes |
| 3_Option_Menu | No |
| Custom 3_Option_Menu | Yes |
| 4_Option_Menu | No |
| Custom 4_Option_Menu | Yes |
| 5_Option_Menu | No |
| Custom 5_Option_Menu | Yes |
| 5_Option_Menu | No |
| Custom 4_Option_Menu | Yes |
| 6_Option_Menu | No |
| Custom 6_Option_Menu | Yes |
| 7_Option_Menu | No |
| Custom 7_Option_Menu | Yes |
| 8_Option_Menu | No |
| Custom 8_Option_Menu | Yes |
| 9_Option_Menu | No |
| Custom 9_Option_Menu | Yes |
| Notification | Alert | No |
| Email |
| Number Capture | Digits | No |
| Custom Digits | Yes |
| Digits_With_Confirm | No |
| Custom Digits_With_Confirm | Yes |
| Number | No |
| Custom Custom Number | Yes |
| Number_With_Confirm | No |
| Custom Number_With_Confirm | Yes |
| Phone | No |
| Custom Phone | Yes |
| Phone_With_Confirm | No |
| Custom Phone_With_Confirm | Yes |
| Record | Record | No |
| Record_With_Confirm |
| Video | Video Connect | No |
| Virtual Agent | Dialogflow | No |
| DialogflowCX |
| DialogflowIntent |
| DialogflowParam |
| Transcribe |
| VirtualAgentVoice |
| Wxm | WxM_PCS | No |
| Say it Smart Plugin | Say it Smart Plugin | Yes |
| Logger | Remote Custom Logger | Yes |

| Step 1 | In the Remote Server VM, install OpenJDK 17 (version 17.0.13 or higher). . Download OpenJDK at: https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=416&field_operating_system_target_id=436&field_architecture_target_id=All&field_java_package_target_id=All . |
|---|---|
| Step 2 | Configure the JAVA_HOME environment variable under System Variables , with the respective Java installed path. For example, the path may be C:\Program Files\OpenLogic\jdk-17.0.xx.xxx-hotspot . |
| Step 3 | Install Apache Tomcat 9 (version 9.0. 90 or higher). Download Tomcat at: https://tomcat.apache.org/download-90.cgi . |
| Step 4 | Stop the Tomcat server. |
| Step 5 | Copy the customapis.war file to the webapps folder of Tomcat (for example, C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps ). Note The spring boot SDK customapis.war file is located at %CVP_HOME%\util\remoteexecution folder of the VXML Server. To run the customapis.war file, you need Apache Tomcat as the web server. | Note | The spring boot SDK customapis.war file is located at %CVP_HOME%\util\remoteexecution folder of the VXML Server. To run the customapis.war file, you need Apache Tomcat as the web server. |
| Note | The spring boot SDK customapis.war file is located at %CVP_HOME%\util\remoteexecution folder of the VXML Server. To run the customapis.war file, you need Apache Tomcat as the web server. |
| Step 6 | Start the Tomcat server. A folder named customapis is created in %Apache Software Foundation%\Tomcat 9.0\webapps . Templates for web.xml and server.xml are bundled in the customapis folder in the following locations: \customapis\WEB-INF\classes\tomcatConfig\conf\web.xml \customapis\WEB-INF\classes\tomcatConfig\conf\server.xml Use these files only as a reference and configure them properly according to your requirements. The existing web.xml and server.xml files are available at the following locations: %Apache Software Foundation%\Tomcat 9.0\conf\server.xml %Apache Software Foundation%\Tomcat 9.0\conf\web.xml You can replace or modify the above files. |

| Note | The spring boot SDK customapis.war file is located at %CVP_HOME%\util\remoteexecution folder of the VXML Server. To run the customapis.war file, you need Apache Tomcat as the web server. |
|---|---|

| Step 1 | Bundle all the custom code that you want to run remotely in a .jar file. |
|---|---|
| Step 2 | Copy the .jar file and all the dependencies to the %Apache Software Foundation%\webapps\customapis\WEB-INF\lib folder. |
| Step 3 | Restart the Tomcat server. The HTTP port listens at 8080 and the gRPC port listens at 8090 . You can change the port for gRPC in the application.properties file located at %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes . Name of the property: #server.grpc.port =8090 You can change the port for HTTP in the server.xml file located at %Apache Software Foundation%\Tomcat 9.0\conf . Name of the property: <Connector port="8080" protocol="HTTP/1.1"
connectionTimeout="20000"
redirectPort="8443"
maxParameterCount="1000"
 /> For secure connection, configure the port 8080 in the server.xml file. For more information, see Enable Security over HTTP (Self-Signed Certificate) . Note To confirm if the application is running, check the spring boot starter logs in the cvp.log file located in the %Apache Software Foundation%\logs folder. | Note | To confirm if the application is running, check the spring boot starter logs in the cvp.log file located in the %Apache Software Foundation%\logs folder. |
| Note | To confirm if the application is running, check the spring boot starter logs in the cvp.log file located in the %Apache Software Foundation%\logs folder. |
| Step 4 | Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running. |
| Step 5 | To check if the gRPC server is up and running, run the command netstat -a \| findstr 8090 . |
| Step 6 | Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application. |
| Step 7 | Restart the VXML Server for the changes to be effective. |
| Step 8 | To run the loggers remotely, see the Loggers chapter in the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio . |
| Step 9 | In a failure scenario: Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog . To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog . |

| Note | To confirm if the application is running, check the spring boot starter logs in the cvp.log file located in the %Apache Software Foundation%\logs folder. |
|---|---|

| Property Name | Usage |
|---|---|
| loggerPath = C:\\<any folder>\\CustomLogger | Specifies the path for running the application loggers in the remote server. |
| server.grpc.port = 8090 server.grpc.keyStorePath = C:\\Program Files\\OpenLogic\\jdk-17.0.xxx-hotspot\\jre\\lib\\security\\cacerts | Specifies the port and keystore path configured for gRPC. |
| server.grpc.keyStoreType = JCEKS | Specifies the KeyStoreType for gRPC connection. |
| server.grpc.keyAlgorithm = SunX509 | Specifies the key algorithm used. |
| server.grpc.transport = TLS | Specifies the incoming secure protocol. |
| server.grpc.outgoing.secure.Transport = TLS | Specifies the outgoing secure protocol. |
| server.grpcciphers = TLS_RSA_WITH_AES_128_CBC_SHA | Colon (;) seperated secure ciphers, for example TLS_RSA_WITH_AES_128_CBC_SHA. |
| server.grpctlsv1dot2Enabled = true | Secure TLS versions flags, for example TLSv1. |
| server.grpc.protocol = TLS | Specifies the secure protocol used. |
| server.grpc.useClientAuth = true | Specifies whether a client certificate is needed or not. |
| server.grpc.enableRemoteAuthentication = false | Specifies whether gRPC authentication is needed or not. |
| server.grpc.maxAllowedRequests = 1000 | Specifies the maximum allowed calls at a time. |
| restapi.security.enabled = false | Specifies whether HTTP authentication is needed or not. |

| Step 1 | Open Windows Registry Editor (regedit) in the VXML Server. |
|---|---|
| Step 2 | Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java\Options . |
| Step 3 | Add the following entries: Dhttps.proxyHost=<proxy-server hostname or fqdn or IP> Dhttps.proxyPort=<port> |
| Step 4 | Restart the Unified CVP VXML Server from Windows services. |

| Parameter | Action |
|---|---|
| create | Creates a directory structure |
| load | Loads the docker image and run the docker container |
| run | Run the docker container |
| stop | Stops the existing docker container |
| status | Displays the status of running docker container |

| Step 1 | Download or copy the customapis-windows-docker-<version>.zip installer zip file on the windows host. |
|---|---|
| Step 2 | Create the following directory structure on the host: C:\Cisco\customapis |
| Step 3 | Extract the archive (.zip) to the following location: C:\Cisco\customapis , where you need the Installer to be running from. |
| Step 4 | Open the PowerShell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. Note All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . | Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
| Step 5 | Use the launcher.bat file to initiate creation of external mounted folders by providing the create parameter by running the following command: PS .\launcher.bat create After you run the command, external mount folder gets created at location: C:\Cisco\customapis |
| Step 6 | Bundle all the custom code that you want to run remotely in .jar file. |
| Step 7 | Copy the .jar files and all the dependency jars to the C:\Cisco\customapis\external\lib folder. |
| Step 8 | Use the launcher.bat file to load the container by providing the load parameter by running the following command: PS .\launcher.bat load |
| Step 9 | Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running. Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command: PS .\launcher.bat status |
| Step 10 | Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application. |
| Step 11 | Restart the VXML Server for the changes to be effective. |
| Step 12 | In a failure scenario: Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog . To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog . Check Remote Windows Host docker container logs: C:\Cisco\customapis\cvpLogs\cvp.log . Check Tomcat logs: C:\Cisco\customapis\tomcatLogs |

| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
|---|---|

| Note | The configuration of secure and authenticated setup is a one-time activity and not required for subsequent Docker releases. |
|---|---|

| Note | If the Windows system reboots or Docker restarts, you need to start the Docker container again by running the launcher.bat file with the run parameter. |
|---|---|

| Step 1 | Bundle all the custom code that you want to run remotely in .jar file. |
|---|---|
| Step 2 | Copy the .jar files and all the dependency jars to the C:\Cisco\customapis\external\lib folder. |
| Step 3 | Open the Powershell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. Note All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . | Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
| Step 4 | Use the launcher.bat file to start the container by providing the run parameter by running the following command: PS .\launcher.bat run |
| Step 5 | Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running. Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command: PS .\launcher.bat status |
| Step 6 | Perform steps a to c of the Create Credentials for Authentication in Remote Server and Create Keystore Password for Remote Server procedures respectively. |
| Step 7 | Use the following command in PoweShell application to get the <container_id> : PS &$Env:DOCKER_HOME\docker ps |
| Step 8 | Use the following command in PowerShell application to open the command prompt of running docker container: PS &$Env:DOCKER_HOME\docker exec -it <container_id>  cmd.exe |
| Step 9 | Use the following command in the command prompt of the docker container and perform steps 1 to 3 of the Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC procedure: %JAVA_HOME%\bin\keytool -genkey -keyalg RSA -alias customcode_certificate -keystore C:\Users\ContainerAdministrator\external\security\cacerts -storetype JCEKS -keysize 2048 After adding the certificate, close the command prompt terminal of the docker container. Note If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . | Note | If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . |
| Note | If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . |
| Step 10 | Use the launcher.bat file to stop the container by providing the stop parameter by running the following command: PS .\launcher.bat stop |
| Step 11 | Modify the application.properties file and server.xml file to configure these files with proper values for a secure and authenticated gRPC and HTTP call as provided in the section External Mounted Folders or Files Usage and Location . |
| Step 12 | Perform steps 3 to 5 of this procedure again to start the container and view the status of the container. |
| Step 13 | Perform steps 1 to 6 of the Import Self-Signed Certificate of Remote Server in VXML Server for HTTP or gRPC procedure to add the remote server certificate in VXML Server. |
| Step 14 | Perform steps 1 to 7 of the Enable Secure Connection in Call Studio and VXML Server to configure the applications on Call studio and VXML Server procedure to configure the applications on Call studio and VXML Server for a secure and authenticated call. Note Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . | Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
| Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
| Step 15 | In a failure scenario: Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog . To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog . Check Remote Windows Host docker container logs: C:\Cisco\customapis\cvpLogs\cvp.log . Check Tomcat logs: C:\Cisco\customapis\tomcatLogs . |

| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
|---|---|

| Note | If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . |
|---|---|

| Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
|---|---|

| Step 1 | Download or copy the customapis-docker-linux-<version>.zip installer zip on the linux host. |
|---|---|
| Step 2 | Create the following directory structure on the host: /usr/local/customapis |
| Step 3 | Run the following command to extract the archive (.zip) to the location: /usr/local/customapis , where you need the Installer to be running from: $ unzip customapis-docker-linux-<version>.zip |
| Step 4 | Run the following command to provide permission to the launcher.sh file: $ chmod +x launcher.sh Note Ensure that you have permissions to directory location: /usr/local/customapis | Note | Ensure that you have permissions to directory location: /usr/local/customapis |
| Note | Ensure that you have permissions to directory location: /usr/local/customapis |
| Step 5 | Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. |
| Step 6 | Use the launcher.sh file to initiate creation of external mounted folders by providing the create parameter by running the following command: $ ./launcher.sh create After you run the command, external mount folder gets created at location: /usr/local/customapis |
| Step 7 | Bundle all the custom code that you want to run remotely in .jar file. |
| Step 8 | Copy the .jar files and all the dependency jars to the /usr/local/customapis/external/lib folder. |
| Step 9 | Use the launcher.sh file to load the container by providing the load parameter by running the following command: $ ./launcher.sh load |
| Step 10 | Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running. Use the launcher.sh file to view the status of the container by providing the status parameter by running the following command: $ ./launcher.sh status |
| Step 11 | Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application. |
| Step 12 | Restart the VXML Server for the changes to be effective. |
| Step 13 | In a failure scenario: Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog . To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog . Check Remote Linux Host docker container logs: /usr/local/customapis/logs/cvp.log . |

| Note | Ensure that you have permissions to directory location: /usr/local/customapis |
|---|---|

| Note | The configuration of secure and authenticated setup is a one-time activity and does not need to be repeated for subsequent
                                                Docker releases. |
|---|---|

| Note | If the Linux system reboots or Docker restarts, you need to start the Docker container again by running the launcher.sh file with the run parameter. |
|---|---|

| Step 1 | Bundle all the custom code that you want to run remotely in .jar file. |
|---|---|
| Step 2 | Copy the .jar files and all the dependency jars to the /usr/local/customapis/external/lib folder. |
| Step 3 | Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. |
| Step 4 | Use the launcher.sh file to start the container by providing the run parameter by running the following command: $ ./launcher.sh run |
| Step 5 | Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running. Use the launcher.sh file to view the status of the container by providing the status parameter by running the following command: $ ./launcher.sh status |
| Step 6 | Perform steps a to c of the Create Credentials for Authentication in Remote Server and Create Keystore Password for Remote Server procedures respectively. |
| Step 7 | Use the following command to get the <container_id> : $ docker ps |
| Step 8 | Use the following command to open the command prompt for running docker container: $ docker exec -it <container_id> /bin/sh |
| Step 9 | Use the following command in the command prompt of the docker container and perform steps 1 to 3 of the Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC procedure: $JAVA_HOME/bin/keytool -genkey -keyalg RSA -alias customcode_certificate -keystore /usr/local/customapis/external/security/cacerts -storetype JCEKS -keysize 2048 Note If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . | Note | If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . |
| Note | If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . |
| Step 10 | Use the launcher.sh file to stop the container by providing the stop parameter by running the following command: $ ./launcher.sh stop |
| Step 11 | Modify the application.properties file and server.xml file to configure these files with proper values for a secure and authenticated gRPC and HTTP call as provided in the section External Mounted Folders or Files Usage and Location . |
| Step 12 | Perform steps 3 to 5 of this procedure again to start the container and view the status of the container. |
| Step 13 | Perform steps 1 to 6 of the Import Self-Signed Certificate of Remote Server in VXML Server for HTTP or gRPC procedure to add the remote server certificate in VXML Server. |
| Step 14 | Perform steps 1 to 7 of the Enable Secure Connection in Call Studio and VXML Server to configure the applications on Call studio and VXML Server procedure for a secure and authenticated call. Note Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . | Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
| Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
| Step 15 | In a failure scenario: Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog . To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog . Check Remote Linux Host docker container logs: /usr/local/customapis/logs/cvp.log . Check Tomcat logs: /usr/local/customapis/logs . |

| Note | If you already have a CA-signed certificate for the host, refer to the steps in the section Import CA-signed Certificate for Remote Server (Docker) . |
|---|---|

| Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
|---|---|

| Note | Ensure to restart the container after modifying the files for the changes to take effect. |
|---|---|

| File and Location | Usage |
|---|---|
| .jar file and dependencies Linux : /usr/local/customapis/external/lib Windows : C:\Cisco\customapis\external\lib | Bundles all the custom code that you want to run remotely in a .jar file. Copy the .jar file and all the dependencies to the C:\Cisco\customapis\external\lib folder (Windows) and /usr/local/customapis/external/lib folder (Linux) |
| .class files Linux : /usr/local/customapis/external/classes Windows : C:\Cisco\customapis\external\classes | Keeps all external classes in the folder location |
| application.properties Linux : /usr/local/customapis/external/conf/application.properties Windows : C:\Cisco\customapis\external\conf\application.properties | For grpc Authentication, set the server.grpc.enableRemoteAuthentication flag to true . For grpc Secure: set the server.grpc.secure flag to true . (For Windows) set the server.grpc.keyStorePath to C:/Users/ContainerAdministrator/external/security/cacerts . For http authentication, set the restapi.security.enabled flag to true . |
| server.xml Linux : /usr/local/customapis/external/conf/tomcatConfig/conf/server.xml Windows : C:\Cisco\customapis\external\conf\tomcatConfig\conf\server.xml | For http Secure Connection, replace the existing connector <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" /> with the following: <Connector SSLEnabled="true" acceptCount="1500" ciphers="TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256" clientAuth="false" disableUploadTimeout="true" enableLookups="false" executor="tomcatThreadPool" keyAlias="customcode_certificate" keystoreFile="C:\Users\ContainerAdministrator\external\security\cacerts" keystorePass="changeit" keystoreType="JCEKS" maxHttpHeaderSize="8192" port="8080" protocol="org.apache.coyote.http11.Http11NioProtocol"
scheme="https" secure="true" sslImplementationName="org.apache.tomcat.util.net.jsse.JSSEImplementation" sslProtocol="TLS" sslEnabledProtocols="TLSv1.2"/> Note Ensure that you add the following parameters to the connector according to the configurations done for your remote server: keyAlias keystoreFile keystorePass port | Note | Ensure that you add the following parameters to the connector according to the configurations done for your remote server: keyAlias keystoreFile keystorePass port |
| Note | Ensure that you add the following parameters to the connector according to the configurations done for your remote server: keyAlias keystoreFile keystorePass port |
| log4j2.xml Linux : /usr/local/customapis/external/conf/conf/log4j2.xml Windows : C:\Cisco\customapis\external\conf\log4j2.xml | For enhanced logging, ensure that you change the level of logging from info to debug as shown below: <Logger name="com.cisco.cvp.customapi" level="debug"
additivity="false">
<AppenderRef ref="LogToFile" />
</Logger> |
| setenv.bat Linux : /usr/local/customapis/external/conf/setenv.bat Windows : C:\Cisco\customapis\external\conf\setenv.bat | For setting user defined variables for the tomcat service, you can modify the setenv.bat file according to requirement. A pre-configured setenv.bat has already been added to the specific location. |
| context.xml Linux : /usr/local/customapis/external/conf/context.xml Windows : C:\Cisco\customapis\external\conf\tomcatConfig\conf\context.xml | For adding resource, you can modify the context.xml according to your requirement. |
| Tomcat logs: Linux : /usr/local/customapis/logs/ Windows : C:\Cisco\customapis\tomcatLogs Remote server logs: Linux : /usr/local/customapis/logs/cvp.log Windows : C:\Cisco\customapis\cvpLogs\cvp.log | For debugging, tomcat catalina logs and remote server logs are available here. |
| docker-compose.yaml Linux : /usr/local/customapis/docker-compose.yaml Windows : C:\Cisco\customapis\docker-compose.yaml | For modifying the memory limit and CPU usage specified for the container, use the docker-compose.yaml file. |

| Note | Ensure that you add the following parameters to the connector according to the configurations done for your remote server: keyAlias keystoreFile keystorePass port |
|---|---|

| Step 1 | Open the PowerShell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. Note All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . | Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
|---|---|---|---|
| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
| Step 2 | Use the launcher.bat file to stop the container by providing the stop parameter by running the following command: PS .\launcher.bat stop |
| Step 3 | Download or copy the customapis-windows-docker-<version>.zip installer zip file on the windows host. |
| Step 4 | Extract the archive (.zip) to the following location and replace the existing files if necessary: C:\Cisco\customapis , where you need the Installer to be running from. |
| Step 5 | Use the launcher.bat file to load the container by providing the load parameter by running the following command: PS .\launcher.bat load |
| Step 6 | Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running. Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command: PS .\launcher.bat status |
| Step 7 | Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application. |
| Step 8 | Restart the VXML Server for the changes to be effective. |
| Step 9 | In a failure scenario: Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog . To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog . Check Remote Server or Windows Host docker container logs: C:\Cisco\customapis\cvpLogs\cvp.log Check Tomcat logs: C:\Cisco\customapis\tomcatLogs |

| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
|---|---|

| Step 1 | Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. |
|---|---|
| Step 2 | Use the launcher.sh file to stop the container by providing the stop parameter by running the following command: $ ./launcher.sh stop |
| Step 3 | Download or copy the customapis-docker-linux-<version>.zip installer zip on the linux host. |
| Step 4 | Create the following directory structure on the host: /usr/local/customapis |
| Step 5 | Run the following command to extract the archive (.zip) to the location and replace the existing files if necessary: /usr/local/customapis , where you need the Installer to be running from: $ unzip customapis-docker-linux-<version>.zip |
| Step 6 | Run the following command to provide permission to the launcher.sh file: $ chmod +x launcher.sh Note Ensure that you have permissions to directory location: /usr/local/customapis | Note | Ensure that you have permissions to directory location: /usr/local/customapis |
| Note | Ensure that you have permissions to directory location: /usr/local/customapis |
| Step 7 | Use the launcher.sh file to load the container by providing the load parameter by running the following command: $ ./launcher.sh load |
| Step 8 | Check the status of the application at: http://remote_ip:8080/customapis/actuator/health . UP status denotes that the application is running. Use the launcher.sh file to view the status of the container by providing the status parameter by running the following command: $ ./launcher.sh status |
| Step 9 | Configure the dynamic configuration and remote execution URLs for the Call Studio application in the Remote URL Settings tab and redeploy the application. |
| Step 10 | Restart the VXML Server for the changes to be effective. |
| Step 11 | In a failure scenario: Check the error logs in VXML Server: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ErrorLog . To check the lifecycle of an element, check the activity log: %CVP_HOME%\VXMLServer\applications\{App name}\logs\ActivityLog . Check Remote Server or Linux Host docker container logs: /usr/local/customapis/logs/cvp.log Check Tomcat logs: /usr/local/customapis/logs |

| Note | Ensure that you have permissions to directory location: /usr/local/customapis |
|---|---|

| Step 1 | Use the launcher.bat file (Windows) or launcher.sh file (Linux) stop the container by providing the stop parameter by running the following command: Windows : PS .\launcher.bat stop Linux : $ ./launcher.sh stop |
|---|---|
| Step 2 | Provide the existing path in the application.properties file of the remote server for the loggerPath . For example: Linux : loggerPath= /usr/local/customapis/external/CustomLogger Windows : loggerPath= C:/Users/ContainerAdministrator/external/Customlogger |
| Step 3 | Copy the VXMLServer\applications\<applicationName>\data folder to the loggerPath in the remote server machine. For example: Linux : loggerPath= /usr/local/customapis/external/CustomLogger Windows : loggerPath= C:/Users/ContainerAdministrator/external/Customlogger |
| Step 4 | Copy the VXMLServer\dtds folder to the loggerPath in the remote server machine. The logger folder must contain both /applications and /dtds folders. |
| Step 5 | Use the launcher.bat file (Windows) or launcher.sh file (Linux) to run the container by providing the run parameter by running the following command: Windows : PS .\launcher.bat run Linux : $ ./launcher.sh run |
| Step 6 | Load the custom logger instances of the remote windows host machine using the cvp.log file located at /usr/local/customapis/logs/cvp.log (Linux) or C:\Cisco\customapis\cvpLogs\cvp.log (Windows). |

| Note | If you already have a CA-signed certificate for the host, follow the steps below. If not, generate a self-signed certificate
                                          using the procedure in Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC and sign it with the relevant Certificate Authority (CA). |
|---|---|

| Step 1 | To import the root certificate issued by the Certificate Authority, follow the below steps: Copy the root.pem file in the following external directory location: Windows Docker : C:\Cisco\customapis\external\security\root.pem Linux Docker : /usr/local/customapis/external/security/root.pem Access the Docker container by running the following command: Windows Docker : PS &$Env:DOCKER_HOME\docker exec -it <container_id> cmd.exe Linux Docker : $ docker exec -it <container_id> /bin/sh Run the following command to import the root certificate into a Java KeyStore (JKS): Windows Docker : %JAVA_HOME%\bin\keytool -storetype JCEKS -keystore C:\Cisco\customapis\external\security\cacerts -import -v -trustcacerts -alias root -file C:\Cisco\customapis\external\security\root.pem Linux Docker : $JAVA_HOME/bin/keytool -storetype JCEKS -keystore /usr/local/customapis/external/security/cacerts -import -v -trustcacerts -alias root -file /usr/local/customapis/external/security/root.pem |
|---|---|
| Step 2 | To import the CA-signed certificate to the remote server, follow the below steps: Copy the host.pem file in the following external directory location: Windows Docker : C:\Cisco\customapis\external\security\root.pem Linux Docker : /usr/local/customapis/external/security/root.pem Access the Docker container by running the following command: Windows Docker : PS &$Env:DOCKER_HOME\docker exec -it <container_id> cmd.exe Linux Docker : $ docker exec -it <container_id> /bin/sh Run the following command to import the root certificate into a Java KeyStore (JKS): Windows Docker : %JAVA_HOME%\bin\keytool -storetype JCEKS -keystore C:\Cisco\customapis\external\security\cacerts -import -v -trustcacerts -alias customcode_certificate -file C:\Cisco\customapis\external\security\host.pem Linux Docker : $JAVA_HOME/bin/keytool -storetype JCEKS -keystore /usr/local/customapis/external/security/cacerts -import -v -trustcacerts -alias customcode_certificate -file /usr/local/customapis/external/security/host.pem |

| In a REST client, for example Postman, enter the following details to create credentials: In the POST request, add the URL http://<remote_machine_IP>:8080/customapis/actionapi/add-user-credentials . In the above URL, replace remote server, IP address, and port as needed. In Request Body , add userid and secret as key-value. Make sure the provided userid and secret to be non-null values. In the Headers tab, you must enable Content-Type as application/x-www-form-urlencoded . Note After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. | Note | After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. |
|---|---|---|
| Note | After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. |

| Note | After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. |
|---|---|

| Step 1 | Log in to the remote server machine. |
|---|---|
| Step 2 | Navigate to %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes . |
| Step 3 | Open the application.properties file and set the server.grpc.enableRemoteAuthentication flag to true. |
| Step 4 | Restart Apache Tomcat Server. |

| Step 1 | Log in to the remote server machine. |
|---|---|
| Step 2 | Navigate to %Apache Software Foundation%\Tomcat9.0\webapps\customapis\WEB-INF\classes . |
| Step 3 | Open the application.properties file and set the restapi.security.enabled flag to true. |
| Step 4 | Restart Apache Tomcat Server. |

| In a REST client, for example Postman, enter the following details to create credentials: In the POST request, add the URL http://<remote_machine_IP>:8080/customapis/actionapi/add-keystore-password . In the above URL, replace remote server, IP address, and port as required. In Request Body , add keyStorePassword as the key-value . Ensure that the provided keyStorePassword is a non-null value. In the Headers tab, you must enable Content-Type as application/x-www-form-urlencoded . Note After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. | Note | After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. |
|---|---|---|
| Note | After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. |

| Note | After authentication is enabled, you must change the credentials. Use basic authentication if the credentials were updated
                                                            in the same POST request and the username and password were changed previously. |
|---|---|

| Step 1 | Open the command prompt and execute the following command in cmd.exe with proper alias: %JAVA_HOME%\jdk-17.0.xx-hotspot\jre\bin>keytool -genkey -keyalg RSA -alias customcode_certificate -keystore ..\lib\security\cacerts
                                                -storetype JCEKS -keysize 2048 |
|---|---|
| Step 2 | Once you execute the command, answer the questions. For example: Enter keystore password: *************
What is your first and last name? [Unknown]:  CustomRemoteServer----------------→ The CN should same as the FQDN of the machine What is the name of your organizational unit?
  [Unknown]:  CCBU
What is the name of your organization?
  [Unknown]:  CISCO
What is the name of your City or Locality?
  [Unknown]:  KA
What is the name of your State or Province?
  [Unknown]:  BLR
What is the two-letter country code for this unit?
  [Unknown]:  IN
Is CN= CustomRemoteServer , OU=CCBU, O=CISCO, L=KA, ST=BLR, C=IN correct?
  [no]:  yes
Enter key password for <customcode_certificate>
        (RETURN if same as keystore password):
done |
| Step 3 | Now, you can import the self-signed certificate. |

| Note | If you already have a CA-signed certificate for the host, follow the steps below. If not, generate a self-signed certificate
                                             using the procedure in Generate Self-Signed Certificate for Remote Custom Server HTTP or gRPC and sign it with the relevant Certificate Authority (CA). |
|---|---|

| Step 1 | To import the root certificate issued by the Certificate Authority, follow the below steps: Copy the root.pem file in the following location: %JAVA_HOME%\lib\security Go to directory location %JAVA_HOME%\jre\bin . Open the command prompt and execute the following command in cmd.exe with proper alias: keytool.exe -storetype JCEKS -keystore ..\lib\security\cacerts -import -v -trustcacerts -alias root -file ..\lib\security\root.pem |
|---|---|
| Step 2 | To import the CA-signed certificate to the remote server, follow the below steps: Copy the host.pem file in the following location: %JAVA_HOME%\lib\security Go to directory location: %JAVA_HOME%\jre\bin . Open the command prompt and execute the following command in cmd.exe with proper alias: keytool.exe -storetype JCEKS -keystore ..\lib\security\cacerts -import -v -trustcacerts -alias customcode_certificate -file ..\lib\security\host.pem |

| Step 1 | Download OpenSSL (64-bit) and install on your remote computer. |
|---|---|
| Step 2 | Add OpenSSL bin path to the Windows environment path variable. For example, path=C:\Program Files\OpenSSL-Win64\bin |
| Step 3 | Go to C:\Cisco\CVP\conf\security |
| Step 4 | From the command prompt, run the following command to generate the private keys for the remote server: openssl ecparam -name prime256v1 -genkey -noout -out remoteserver-private-key.pem |
| Step 5 | Run the following command to generate the self-signed certificates for the remote server: openssl req -new -key remoteserver-private-key.pem -x509 -nodes -days 365 -out remoteserver-cert.pem |
| Step 6 | Enter the values for the following fields when prompted: Country Name (2 letter code) []: < >
State or Province Name (full name) []: < >
Locality Name (for example, city) []: < >
Organization Name (for example, company) []: < >
Organizational Unit Name (for example, section) []: < >
Common Name (for example, server FQDN or your name) []: < >
Email Address []: < >
Please enter the following extra attributes to be sent with your certificate request:
A challenge password []: < >
An optional company name []: < > Note Enter a period (.) to leave the following fields blank: Common Name Email Address Challenge password An optional company name You can generate a certificate after entering all the details. | Note | Enter a period (.) to leave the following fields blank: Common Name Email Address Challenge password An optional company name You can generate a certificate after entering all the details. |
| Note | Enter a period (.) to leave the following fields blank: Common Name Email Address Challenge password An optional company name You can generate a certificate after entering all the details. |
| Step 7 | Run the following command to append the keys and certificates in one file: cat remoteserver-private-key.pem remoteserver-cert.pem > remoteserver-certificate-private.pem |
| Step 8 | Run the following command to export the certificates to the Remote server: openssl pkcs12 -export -inkey remoteserver-private-key.pem -in remoteserver-certificate-private.pem -out cert_remoteserver.p12
                                                -name remoteserver_certificate Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> |
| Step 9 | Go to C:\Cisco\CVP\conf\security and run the following command to delete the existing RSA certificates for the remote server: C:\Cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias remoteserver-certificate -storepass <CVP
                                                keystore password> |
| Step 10 | Run the following command to import the ECDSA certificates to the keystore: C:\Cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_remoteserver.p12 -srcstoretype PKCS12 -destkeystore
                                                .keystore -deststoretype JCEKS -alias remoteserver_certificate Importing keystore cert_remoteserver.p12 to .keystore... Enter destination keystore password:
Enter source keystore password:
[Storing.keystore] |
| Step 11 | Restart the remote server. |
| Step 12 | In the new browser tab, type the following and download the certificates: https://<remote ip>:8080 |

| Note | Enter a period (.) to leave the following fields blank: Common Name Email Address Challenge password An optional company name You can generate a certificate after entering all the details. |
|---|---|

| Step 1 | Log in to the remote server machine. |
|---|---|
| Step 2 | Make sure the the self-signed certificate for the remote server machine is generated. |
| Step 3 | Navigate to the %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes directory. |
| Step 4 | Launch the application.properties file and set the server.grpc.secure flag to true. |
| Step 5 | Provide the .keystore path for the server.grpc.keyStorePath flag. For example: C:\\Program Files\\OpenLogic\\jdk-17.0.11-hotspot\\jre\\lib\\security\\cacerts (make sure that keystore exists in that machine). |
| Step 6 | Restart the Remote Apache Tomcat server. |

| Step 1 | Log in to the remote server machine. |
|---|---|
| Step 2 | Ensure that the self-signed certificate for the remote server machine is generated. |
| Step 3 | Navigate to the %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes directory. |
| Step 4 | Open the application.properties file, set the restapi.security.enabled flag to true, and save the file. |
| Step 5 | Navigate to the %Apache Software Foundation%\Tomcat 9.0\conf directory. |
| Step 6 | Open the server.xml file and provide the connector with the port number, and mention the respective keystore password. For Example : <Connector SSLEnabled="true" acceptCount="1500"
ciphers="TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256" 
clientAuth="false" disableUploadTimeout="true" enableLookups="false" executor="tomcatThreadPool" keyAlias="customcode_certificate"
keystoreFile="C:\Program Files\Java\jre1.8.0_271\lib\security\cacerts" keystorePass="changeit" keystoreType="JCEKS" maxHttpHeaderSize="8192"
port="8080" protocol="org.apache.coyote.http11.Http11NioProtocol" scheme="https" secure="true" 
sslImplementationName="org.apache.tomcat.util.net.jsse.JSSEImplementation" sslProtocol="TLS" sslEnabledProtocols="TLSv1.2"/> |
| Step 7 | Save the server.xml file and restart the remote Apache Tomcat server. |

| Step 1 | Import the certificate for VXML Server in the RemoteServer java keystore . |
|---|---|
| Step 2 | For gRPC, in the application.properties file, available at %Apache Software Foundation%\Tomcat 9.0\webapps\customapis\WEB-INF\classes , change the following property to true: server.grpc.useClientAuth = true |
| Step 3 | For HTTP, in the server.xml file, available at %Apache Software Foundation%\Tomcat 9.0\conf\server.xml , change the following property to true: “clientAuth" flag = true |
| Step 4 | Restart the Apache Tomcat server. |

| Step 1 | Go to the Call Studio application. |
|---|---|
| Step 2 | Right-click on the application, which needs to be in secure connection, and select Properties . |
| Step 3 | In the Call Studio Properties tab, click Remote URL Settings . |
| Step 4 | Choose HTTP or RPC as required |
| Step 5 | Click the Secure Connection checkbox to provide a secure connection. Note You must provide FQDN for HTTP and gRPC connection type in the address field for secure connection. | Note | You must provide FQDN for HTTP and gRPC connection type in the address field for secure connection. |
| Note | You must provide FQDN for HTTP and gRPC connection type in the address field for secure connection. |
| Step 6 | For FQDN, add <IP><space><FQDN(hostname)> in the %drivers%\etc\hosts file in the VXML Server. |
| Step 7 | Save and deploy the application. Restart the VXML Server. Note The same port cannot be used simultaneously in several applications as secure and non-secure ports. For example: All the applications utilizing a port on the VXML Server for gRPC must be re-deployed with the same secure or
                                                            non-secure configurations if the port is used for both secure and non-secure calls. Note When several remote servers or load end points are added for load balancing, all of those servers must have the same secure
                                                            or non-secure configurations when used simultaneously. This is because all the added servers have the same remote URL settings. Note Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . | Note | The same port cannot be used simultaneously in several applications as secure and non-secure ports. For example: All the applications utilizing a port on the VXML Server for gRPC must be re-deployed with the same secure or
                                                            non-secure configurations if the port is used for both secure and non-secure calls. | Note | When several remote servers or load end points are added for load balancing, all of those servers must have the same secure
                                                            or non-secure configurations when used simultaneously. This is because all the added servers have the same remote URL settings. | Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
| Note | The same port cannot be used simultaneously in several applications as secure and non-secure ports. For example: All the applications utilizing a port on the VXML Server for gRPC must be re-deployed with the same secure or
                                                            non-secure configurations if the port is used for both secure and non-secure calls. |
| Note | When several remote servers or load end points are added for load balancing, all of those servers must have the same secure
                                                            or non-secure configurations when used simultaneously. This is because all the added servers have the same remote URL settings. |
| Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |

| Note | You must provide FQDN for HTTP and gRPC connection type in the address field for secure connection. |
|---|---|

| Note | The same port cannot be used simultaneously in several applications as secure and non-secure ports. For example: All the applications utilizing a port on the VXML Server for gRPC must be re-deployed with the same secure or
                                                            non-secure configurations if the port is used for both secure and non-secure calls. |
|---|---|

| Note | When several remote servers or load end points are added for load balancing, all of those servers must have the same secure
                                                            or non-secure configurations when used simultaneously. This is because all the added servers have the same remote URL settings. |
|---|---|

| Note | Refer to the Remote Execution section of the Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studios . |
|---|---|

| Step 1 | Launch the URL https://<remote_server_IP>:8090/ to download the certificate. |
|---|---|
| Step 2 | Upload the certificate in the %CVP_HOME%\conf\security folder where the VXML Server is hosted. |
| Step 3 | Import the certificate using the following command: %CVP_HOME%\jdk-8.0.372.07-hotspot\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype
                                                JCEKS -alias <any_alias> -file %CVP_HOME%\conf\security\<FQDN_remote_server.cer> %CVP_HOME%\jdk-17.0.11-hotspot\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype
                                                JCEKS -alias <any_alias> -file %CVP_HOME%\conf\security\<FQDN_remote_server.cer> Where, <FQDN_remote_server.cer> is the certificate downloaded in step 1, which is named after the FQDN of remote server. Note Use FQDN instead of IP address for a secure gRPC connection. The common name (CN) of the certificate should be same as the
                                                            address mentioned in the studio settings. | Note | Use FQDN instead of IP address for a secure gRPC connection. The common name (CN) of the certificate should be same as the
                                                            address mentioned in the studio settings. |
| Note | Use FQDN instead of IP address for a secure gRPC connection. The common name (CN) of the certificate should be same as the
                                                            address mentioned in the studio settings. |
| Step 4 | Enter the keystore password when prompted. Run the DecryptKeystoreUtil.bat file located at %CVP_HOME%\bin to view the keystore password. |
| Step 5 | Make sure that the connection type in the Call Studio application is changed to HTTP or gRPC accordingly. Also, ensure the Secure Connection checkbox is enabled. |
| Step 6 | Save and deploy the Call Studio application and restart the VXML Server. |

| Note | Use FQDN instead of IP address for a secure gRPC connection. The common name (CN) of the certificate should be same as the
                                                            address mentioned in the studio settings. |
|---|---|

| Note | The above credentials can be used for monitoring . |
|---|---|

| Note | After creating the user credentials for multiple users, modify the Auth flag in the application.properties file and restart the Tomcat server. |
|---|---|

| Note | For Docker, follow the below steps: Stop the container by running the launcher.bat file with the stop parameter. Refer to the Run the Launcher Script section for more information. PS .\launcher.bat stop Start the container by running the launcher.bat file with the run parameter. Refer to the Run the Launcher Script section for more information. PS .\launcher.bat run |
|---|---|