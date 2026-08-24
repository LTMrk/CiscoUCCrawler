---
doc_id: ciscodevnet-finesse-sample-code-notificationserviceclientsample-readme-md
source_url: https://github.com/CiscoDevNet/finesse-sample-code/blob/master/NotificationServiceClientSample/README.md
repo: CiscoDevNet/finesse-sample-code
ruta: NotificationServiceClientSample/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:26.028097+00:00
---

# finesse-sample-code — NotificationServiceClientSample/README.md

Repositorio: CiscoDevNet/finesse-sample-code
Descripcion del repositorio: Sample Gadgets and code for use with Finesse

# Cisco Finesse - Notification Service Client Sample
The notification service client sample presents a Java program that has the step by step process to connect to the Cisco Finesse Notification Service and receive the Finesse notifications (XML events). The example program implements the logic to connect to the Finesse Notification Service using the OpenSource XMPP client library [Smack](https://www.igniterealtime.org/projects/smack/) to connect and receive Finesse notifications. Other [Java XMPP libraries](http://xmpp.org/software/libraries.html) are also available. This code has been tested with Finesse 15.0 and Smack 4.3.4.

This sample contains the following files:

    _readme.txt
    jxmpp-core-0.6.4.jar
    jxmpp-jid-0.6.4.jar
    jxmpp-util-cache-0.6.4.jar
    minidns-core-0.3.4.jar
    SampleNotificationService.pdf
    SampleXMPPClient.java
    smack-core-4.3.4.jar
    smack-extensions-4.3.4.jar
    smack-im-4.3.4.jar
    smack-java7-4.3.4.jar
    smack-resolver-javax-4.3.4.jar
    smack-sasl-javax-4.3.4.jar
    smack-tcp-4.3.4.jar
    xpp3-1.1.4c.jar

## Requirements
1. The sample gadget and the Finesse JavaScript library requires a deployment that includes Cisco Finesse. If you do not have a system that includes Cisco Finesse, you can reserve a [DevNet sandbox](https://developer.cisco.com/docs/finesse/#!sandbox) for developing your gadget.
1. [XMPP Library](http://xmpp.org/software/libraries.html): [Smack](https://www.igniterealtime.org/projects/smack/) is the XMPP library used to connect to the Notification Service to receive events.

 * smack-core-4.3.4.jar - Smack core components.
 * smack-tcp-4.3.4.jar - Smack for standard XMPP connections over TCP.
 * smack-extensions-4.3.4.jar - Smack extensions. Classes and methods that implement support for the various XMPP XEPs (Multi-User Chat, PubSub, …) and other XMPP extensions.
 * smack-sasl-javax-4.3.4.jar - SASL with javax.security.sasl Use javax.security.sasl for SASL.
 * smack-resolver-javax-4.3.4.jar - DNS SRV with Java7 Use javax.naming for DNS SRV lookups. The javax.naming API is availabe in JavaSE since Java7.
 * smack-java7-4.3.4.jar - Smack for Java7 (or higher). This is a pseudo-artifact that pulls all the required dependencies to run Smack on Java 7 (or higher) JVMs. Usually you want to add additional dependencies to smack-tcp, smack-extensions and smack-experimental.
 * smack-im-4.3.4.jar - Smack IM. Classes and methods for XMPP-IM (RFC 6121): Roster, Chat and other functionality.
 * jxmpp-core-0.6.4.jar - JXMPP core components.
 * jxmpp-jid-0.6.4.jar - JID classes from JXMPP.
 * jxmpp-util-cache-0.6.4.jar - A minimalistic and efficient bounded LRU Cache with optional expiration.
 * minidns-core-0.3.4.jar - MiniDNS' core classes and functionality.
 * xpp3-1.1.4c.jar - MXP1 is a stable XmlPull parsing engine that is based on ideas from XPP and in particular XPP2 but completely revised and rewritten to take the best advantage of latest JIT JVMs such as Hotspot in JDK 1.4+.


## Usage
In order to run this Finesse Java program, follow the **SampleNotificationService.pdf** documentation for how to modify the program for your Finesse environment.

1. Change the following variables in the Java program for your Finesse environment:
 * hostname
 * username
 * password
1. Compile the sample java program using the following command:
`javac -cp ":/<path>/jxmpp-core-0.6.4.jar:/<path>/jxmpp-jid-
0.6.4.jar:/<path>/jxmpp-util-cache-0.6.4.jar:/<path>/minidns-core-
0.3.4.jar:/<path>/smack-core-4.3.4.jar:/<path>/smack-extensions-
4.3.4.jar:/<path>/smack-im-4.3.4.jar:/<path>/smack-java7-4.3.4.jar:/<path>/smack-
resolver-javax-4.3.4.jar:/<path>/smack-sasl-javax-4.3.4.jar:/<path>/smack-tcp-
4.3.4.jar:/<path>/xpp3-1.1.4c.jar" /<path>/SampleXMPPClient.java`
1. Run the program using the following command:
`java -cp ":/<path>/jxmpp-core-0.6.4.jar:/<path>/jxmpp-jid-0.6.4.jar:/<path>/jxmpp-
util-cache-0.6.4.jar:/<path>/minidns-core-0.3.4.jar:/<path>/smack-core-
4.3.4.jar:/<path>/smack-extensions-4.3.4.jar:/<path>/smack-im-
4.3.4.jar:/<path>/smack-java7-4.3.4.jar:/<path>/smack-resolver-javax-
4.3.4.jar:/<path>/smack-sasl-javax-4.3.4.jar:/<path>/smack-tcp-
4.3.4.jar:/<path>/xpp3-1.1.4c.jar" /<path>/SampleXMPPClient`

Note: These commands work for Mac and Linux OS. In case of windows, use ‘;’ instead of ‘:’.

## Additional Information
##### Finesse REST API
Documentation for the Finesse REST API can be found in the [Finesse Developer Guide](https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide).

## Disclaimer
This sample code is only a sample and is **NOT guaranteed to be bug free and production quality**.

The sample code is meant to:
- Serve as an example of the step by step process of connecting to the Finesse Notification Service and receive Finesse notifications.
- Provided as a guide for a developer to see how to use a Java XMPP library to receive the Finesse notifications.s

## Support Notice
[Support](https://developer.cisco.com/site/support) for the sample code is provided on a "best effort" basis via DevNet. Like any custom deployment, it is the responsibility of the partner and/or customer to ensure that the customization works correctly and this includes ensuring that the sample code is properly integrated into 3rd party applications.

Cisco Systems, Inc.<br>
[http://www.cisco.com](http://www.cisco.com)<br>
[http://developer.cisco.com/site/finesse](http://developer.cisco.com/site/finesse)

---
> Fuente: https://github.com/CiscoDevNet/finesse-sample-code/blob/master/NotificationServiceClientSample/README.md (licencia MIT)
