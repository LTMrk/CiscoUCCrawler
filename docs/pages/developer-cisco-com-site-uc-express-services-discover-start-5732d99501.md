---
doc_id: developer-cisco-com-site-uc-express-services-discover-start-5732d99501
source_url: https://developer.cisco.com/site/uc-express-services/discover/start/
retrieved_at: 2026-08-25T21:11:00.001371+00:00
---

Note: This site is no longer being maintained. Latest documents are available at Cisco Unified Communications Manager Express.

## How Do I Get Started

The UC Express Services SDK is intended for developers who are developing voice applications on Cisco Unified CME. Developers who are already familiar with the JTAPI development environment for CUCM will find the UC Express Services SDK for CME to be based on very similar command formats.

The developer must have knowledge or experience in the following areas:

- Cisco IOS software

- Java programming

The developer can download the UC Express Services SDK here .

PREREQUISITES

Applications Server

- JAR files for UC Express Services SDK: cme_sdk_x.y.z.jar, where x.y.z is the version number.

- Java version 6 must be installed and included in the application.

- All SDK JAR files must be in the CLASS PATH ( For more details please refer to the Quick Start Guide )

Cisco Unified CME Router

- Cisco IOS Release 15.0(1)XA ( CME 8.0 ) or beyond

- Cisco Unified CME 8.x must be configured on the Cisco router. For configuration information, see the Cisco Unified CME Administrator Guide here

- XML interface must be manually configured in Cisco Unified CME. See the "Configuring XML Interface" module in the Cisco Unified CME Administrator Guide here .

PREPARING THE ENVIRONMENT

To prepare the developer's environment for developing applications using the UC Express Services SDK, perform the following steps:

- 1. Import all java source files into each source directory.

- 2. Include all JAR files into the CLASS PATH.

- CME_SDK_0_1_x.jar

- caffeine-stack-3.1.2.152.jar

- cme.xml.sdk.jaxb.jar

- concurrent-1.3.4.jar

- jain-sip-1.0.jar

- log4j-1.2.8.jar

- trove-1.0.2.jar

Please Refer to the UC Express Services SDK Quick Start Guide for Sample Configuration.