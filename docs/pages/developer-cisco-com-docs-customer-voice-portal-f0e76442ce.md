---
doc_id: developer-cisco-com-docs-customer-voice-portal-f0e76442ce
source_url: https://developer.cisco.com/docs/customer-voice-portal/
retrieved_at: 2026-08-24T22:12:01.013808+00:00
---

# What is Customer Voice Portal?

Cisco Unified Customer Voice Portal (CVP) combines open-standards support for speech with intelligent application development and call control to deliver personalized self-service to callers, either as a standalone Interactive-Voice-Response (IVR) system or transparently integrated with a contact center.

Customers using the extensive out of the box features of Customer Voice Portal and Cisco Unified Call Studio can already create customized voice-portal/IVR applications with great flexibility and power without writing a line of code. However, for developers interested in extending the core CVP functionality to perform specific tasks, Cisco provides the following options:

- Custom Elements - create custom elements for Cisco Unified Call Studio using Java

- Customer Voice Portal (CVP) REST APIs - automate the deployment and management of CVP applications

- Cisco Virtualized Voice Browser (VVB) REST APIs - add VoiceXML browser services when used in conjunction with a VoiceXML server.

## What Are The Business Benefits?

- Provides incoming callers with automated, intelligent self-service using touch-tone input or speech recognition. Callers can access and modify their accounts, place orders, get status updates, retrieve information, and resolve problems, all without speaking to a live agent.

- Provides distributed call treatment with centralized application management, allowing calls to receive self-service and queuing at the most efficient (or desirable) location, while still enabling consistent branding and caller experience and easy application updates.

- The ability of Unified CVP to route calls across customer service sites enables resource virtualization, allowing businesses and organizations to lower their costs significantly by reducing the number of agents required to maintain a given service level.

# Custom Elements for Cisco Unified Call Studio

Customer Voice Portal customization capabilities enables the creation of custom elements for Cisco Unified Call Studio that look, act, and operate just like Cisco-provided elements. Customers can build a completely custom voice, action, or other functions in the self-service call flow. It allows users to create custom interfaces to other systems or even completely take control of the dynamic VoiceXML created by the software while retaining multi-platform compatibility. Additionally, custom Plug-ins can be created for complete control of the "Say It Smart" audio transformation technology to make custom mapping tables of abbreviations to full names, control read-back of currency, special account numbers, and more.

The custom elements for Cisco Unified Call Studio enables customers to:

- Make repetitive call flows and tasks easier to configure

- Create functions that are custom to their environment

- Create centralized, approved Elements for use by departments or subsidiaries, which fosters reuse in future voice applications

- Integrate logging capabilities with the existing management and logging facilities

- Integrate with IT and Web functionality that is already present in your business instead of rewriting business logic

- Leverage best-practices by building them into custom Elements

- Create a library of high-value enterprise-wide Elements for future reuse and enhancement

- Keep the same look and feel as Unified Call Studio

The custom Elements can only be built using Java, so the developer should possess a familiarity with the Java programming language. They should understand Java interfaces and abstract classes, extending classes and overriding methods, static variables and methods, Java collections, and compiling and deploying Java classes and JAR files. It does not require very complex Java coding, so knowing the basics of the Java language will be sufficient to start working with the custom Elements.

## CVP Custom Elements Architecture

# Customer Voice Portal REST APIs

Cisco Unified Customer Voice Portal provides REST based management APIs to address "Service Fulfillment" and "Service Assurance" type requirements, allowing programmatic control of CVP application script deployment, related media resource management (e.g. voice prompt or language specific audio files) and CVP server configurations.

Service fulfillment APIs are focused on the management of Media files on CVP Media servers, and VXML scripts on CVP VXML Servers. Service assurance APIs are targeted at the management of Simple Network Management Protocol (SNMP) and Syslog server configuration of CVP hosts.

- Built in best practices in dialog design to accelerate development and consistently deliver a high quality user interface.

- Pre-tested VoiceXML lets you reliably create powerful, platform independent applications.

- Support for leading speech recognition engines from Nuance and Scansoft allowing novice and advanced developers to easily create speech driven applications.

- Business rules and easy integration with back-end systems and third party applications deliver intelligent applications that extend existing enterprise investments through any phone.

- Complete customization allows you to create your own Elements and extend the library.

## Technical Overview

The CVP REST APIs are packaged with the CVP Operations Console (OAMP) as a web application running under the Web Services Manager (WSM) server. The REST APIs are automatically installed with OAMP installation. The Cisco CVP service "Cisco CVP WebServicesManager" that is part of OAMP is used for the management (Stop, Start and Restart) of the REST API Service. To manage media files on media servers and VXML files on VXML servers, respective media and VXML servers should be added and configured in OAMP under the Device Management section.

These APIs use the REST-based request-response model. HTTP requests are processed by the Web Service Manager (WSM) module within the CVP OAMP Server. Since the APIs are REST-based, they use the HTTP methods POST, PUT, GET, or DELETE, depending on the type of request.

CVP REST API requests can only be sent over secured connections (HTTPS). They support both JSON and XML as the data format for requests and responses.

### Authentication

The CVP REST APIs use Basic Authentication to authenticate the request. Only users that are administered by OAMP and have the ServiceabilityAdministrationUserRole role can use the REST APIs. Attempt to perform an operation by any other user will result in an error with an HTTP status code 401.

## CVP REST APIs Architecture

A brief description of the major components in the CVP REST API architecture can be found in the following table:

## Use Cases

The typical use of CVP REST APIs is the day two configuration management of CVP components. Here are some high-level use cases of the CVP REST APIs:

- Deploy new VXML applications in the CVP VXML server

- Access the details (current status of the application, the created date and time, last modified date and time, and last operation date and time, etc.) of a particular VXML application deployed in CVP

- Delete an existing deployed VXML application from CVP server

- Deploy a media file in CVP Media server

- Update an existing media file in CVP Media server

- Access the details (current status of the application, the created date and time, last modified date and time, and last operation date and time, etc.) of a particular media file deployed in CVP media server

- Delete an existing deployed media file from CVP Media Server

- Update existing syslog server details for CVP managed devices

- Get syslog server details of a CVP managed device

- Create/Update/Delete SNMP Configuration Entities (such as Community String, Users, Notification Destinations, etc.) in the specified devices

- Get details of a SNMP configuration entity

- Get a list of SNMP Configuration entities details.

# Virtualized Voice Browser (VVB) REST APIs

Cisco VVB provides VoiceXML browser services when used in conjunction with a VoiceXML server, such as the Cisco Unified CVP. The Cisco Unified CVP solution, including the Cisco VVB, extends automated self-service beyond the limits of traditional IVR systems and enterprise voice portal platforms.

Cisco VVB is a virtualized application which provides unmatched flexibility of deployment in both centralized data center or at the edge in a branch office. VVB enables ISR 4K series of access routers to be used in contact center deployments (Note: ISR 4K do not support VoiceXML browser function natively on the IOS).

The Cisco VVB provides following benefits:

- Better feature alignment with Cisco contact center solution lines.

- Solution based licensing: Voice browser entitlement clubbed with the U/PCCE, HCS CC solution agent license and CVP VXML port license.

- Support for hybrid deployments with IOS VB and VVB providing ease of migration.

- Facilitates self-service options by processing user commands through touchtone input or speech-recognition technologies.

- Provides multilingual support for Cisco VVB server prompts, for automated speech recognition (ASR) and text-to-speech (TTS) capabilities.

Virtualized Voice Browser Features:

- Media Handling (G.711 a / u law)

- SIP Support

- HTTPS Support

- CCB Support

- Template-Based Configuration Support

- Microapps

- VXML 2.0

- CVP Call studio Compliance

- ASR / TTS Server Compliance (MRCP v1)

- CVP Call Flows (Standalone and Comprehensive)

- Serviceability

- Administrator CLI Support

- Primary / Secondary VXML Server Support

- Whisper Agent and Agent Greeting / Agent Recording Support

- UCS-E Single wide and double wide blade support on 4451 router

- VMWare ESXi

Next

| Component Name | Description | Role |
|---|---|---|
| Application GUI | A REST client that is the user interface used by the administrator to set the day two configuration elements in CVP. | This is not a CVP component but is a gadget application that invokes the REST service. |
| CVP OAMP Server | Operations Console is occasionally referred to as the OAMP (Operate, Administer, Maintain, Provision). The Operations Console manages individual components through the Unified CVP Resource Manager, which is co-located with each managed Unified CVP component. As a part of the CVP operational console (OAMP server) component, CVP Web Services Manager (WSM) provides web services to external clients. Since information provided by WSM are privileged, it is necessary to authenticate client identities before providing privileged information. | Service Assurance and Service Fulfillment specific REST services are hosted in the WSM component of the CVP OAMP server. |
| CVP Media Server | The media server component is a simple web server, such as Microsoft IIS or Apache. Media files to play tones/music/announcements are stored in the media server. | Service Fulfillment specific REST based CRUD operations will be performed in the media files stored in the media server. |
| CVP VXML Server | VXML applications are deployed in the VXML server component. CVP VXML Server executes advanced IVR applications by exchanging VoiceXML pages with the VoiceXML gateway's built-in voice browser. | Service Fulfillment specific REST based CRUD operations will be performed in the VXML applications stored in the VXML server. Service Assurance specific REST based CRUD operations will be performed in the ‘Service Assurance Config Data’ kept in the VXML server. |
| CVP Call Server | The Call Server hosts a number of services including an IVR service, a SIP service, and an ICM service that interfaces with ICM. This server, as a main call control entity, acts as the heart of the CVP system. | Service Assurance specific REST based CRUD operations will be performed in the ‘Service Assurance Config Data’ kept in the call server. |
| CVP Reporting Server | The Reporting server enables users to integrate with Cisco Unified Intelligence Center (CUIC), enabling you to run user friendly custom reports in the CUIC environment. Cisco Unified Intelligence Center templates are shipped with all Unified CVP installations. These templates provide examples to report against Call, Application, Callback, and Trunk Grout Utilization structure. | Service Assurance specific REST based CRUD operations will be performed in the ‘Service Assurance Config Data’ kept in the reporting server. |

| Type of API | Use Cases |
|---|---|
| VXML APIs | These APIs can be used to: Deploy new VXML applications in the CVP VXML server Access the details (current status of the application, the created date and time, last modified date and time, and last operation date and time, etc.) of a particular VXML application deployed in CVP Delete an existing deployed VXML application from CVP server |
| Media APIs | These APIs can be used to: Deploy a media file in CVP Media server Update an existing media file in CVP Media server Access the details (current status of the application, the created date and time, last modified date and time, and last operation date and time, etc.) of a particular media file deployed in CVP media server Delete an existing deployed media file from CVP Media Server |
| Syslog APIs | Syslog APIs are provided to update and delete the syslog server details of already configured syslog server for existing CVP managed devices. The syslog details of the device will be delivered to the syslog server configured through syslog APIs. These APIs can be used to: Update existing syslog server details for CVP managed devices Get syslog server details of a CVP managed device |
| SNMP Configuration Entities API | SNMP Configuration Entities APIs allows users to update the SNMP community string entities for the CVP managed devices and can be used to: Create/Update/Delete SNMP Configuration Entities (such as Community String, Users, Notification Destinations, etc.) in the specified devices Get details of a SNMP configuration entity Get a list of SNMP Configuration entities details. |