---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-d5d40cd9ff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0100011.html
retrieved_at: 2026-08-16T17:31:49.282774+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Service Profile

## Chapter: Configure Service Profile

# Configure Service Profile

## Service Profile Overview

A Service Profile allows you to create a profile that comprises common Unified Communications (UC) Services settings.  You
                              can then apply the service profile to an end user in order to assign the UC services configuration settings in the Service
                              Profile to that end user. You can configure different service profiles for different groups of users in your company so that
                              each group of users has the appropriate services configured for their job.

A Service Profile comprises configuration settings for the following UC services:

Voicemail

Mailstore

Conferencing

Directory

IM and Presence

CTI

Video conferencing services

Jabber Client Configuration (jabber-config.xml)

### Applying Service Profiles to End Users

You can use the following methods to apply a service profile to an end user:

For LDAP Synchronized Users—If you have imported end users from an LDAP directory, you can assign the service profile to a
                                    feature group template and then apply that feature group template to your end users

For Active Local Users (i.e. non-LDAP users)—In End User Configuration, you can assign a service profile for an individual
                                    end user. You can also use the Bulk Administration Tool to assign a service profiles for many end users at once. For details,
                                    see the Bulk Administration Guide for Cisco Unified Communications Manager .

## Service Profile Configuration Task Flow

Step 1

Configure any of the following Unified Communications (UC) services that you want to assign to this service profile:

Configure the UC services settings that you want to set up for your service profiles.

Step 2

Configure a Service Profile

Configure the user's service profile to point to the UC services that you want to apply to this service profile.

### Add Voicemail Service

Add a voicemail service to your system. You can add multiple voicemail services and then select which service you want to
                                 add to your service profiles.

Step 1

From Cisco Unified CM Administration choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list box, choose Voicemail .

Step 4

From the Product Type drop-down list box, choose Unity or Unity Connection .

Step 5

Enter a Name for the voicemail service.

Step 6

Enter a Description that helps you distinguish between services.

Step 7

In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the voicemail service.

Step 8

In the Port field, enter a port to connect to the voicemail service. The default port is 443.

Step 9

In the Protocol field, enter the protocol that will be used to route voicemail messages. The available options are HTTP and HTTPS .

Step 10

Click Save .

#### What to do next

Add Mailstore Service

### Add Mailstore Service

Add a mailstore service to your system. Cisco Jabber clients use the mailstore service for visual voicemail functionality.

Cisco Unity creates subscriber mailboxes for message storage on the Microsoft Exchange server.

Cisco Unity Connection usually provides a mailstore service, and hosts the mailstore service on the same server.

#### Before you begin

Add Voicemail Service

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list box, choose Mailstore .

Step 4

Enter a Name for the mailstore service.

Step 5

Enter a Description for the mailstore service.

Step 6

In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name for the server that hosts the mailstore service.

Step 7

In the Port field, specify a port between 1–65535 that matches the available port on the mailstore service. number between 1 - 65535.
                                          The default mailstore port is 143.

Step 8

In the Protocol field, enter the protocol that will be used to route voicemail messages: TCP (default), TLS, UDP, or SSL.

Step 9

Click Save .

#### What to do next

Add Conferencing Service

### Add Conferencing Service

Add a conferencing service to your system.

#### Before you begin

Add Mailstore Service

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list, choose Conferencing .

Step 4

From the Product Type drop-down list, choose the product that you want to use for conferencing:

- MeetingPlace Classic

- MettingPlace Express

- Webex (Conferencing)

Step 5

Enter a Name for the conferencing service.

Step 6

Enter a Description for the conferencing service.

Step 7

In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the conferencing service.

Step 8

In the Port field, enter a port value that matches the available port on the conferencing service. The recommended values are:

- 80 (default setting)—Use this port for HTTP

- 443—Use this port for HTTPS

Step 9

From the Protocol drop-down list, choose the Protocol to use when endpoints contact this service:

- HTTP

- HTTPS

Step 10

Click Save .

#### What to do next

Add Directory Service

### Add Directory Service

Add a directory service to your system if you want to point Cisco Unified Communications Manager towards an external LDAP
                                 directory for directory lookups.

#### Before you begin

Add Conferencing Service

Step 1

From Cisco Unified CM Administration, choose USer Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list box, choose Directory .

Step 4

From the Product Type field, choose either of the following:

- Directory—Choose this option if you want your clients to use UDS to connect to the Cisco Unified Communications Manager database
                                             for directory lookups.

- Enhanced Directory—Choose this option if you want your clients to connect to an external LDAP directory for directory lookups.

Step 5

Enter a Name for the directory service.

Step 6

Enter a Description for the directory service.

Step 7

In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the directory service that
                                          you want your clients to use for directory lookups.

If you are using an external LDAP directory for directory lookups, enter the hostname, IP address, or fully qualified domain
                                                         name of the  LDAP directory.

Step 8

In the Port field, enter a port number that matches the available port on the directory service. The default port value is 389. In addition,
                                          ports 636, 3628, 3629 can connect to an external LDAP directory.

Step 9

In the Protocol field, enter the protocol that will be used to route  communications between the directory service and endpoints. The available
                                          options are:

- TCP (default setting)

- UDP

- TLS

Step 10

Click Save .

#### What to do next

Add IM and Presence Service

### Add IM and Presence Service

Add an IM and Presence service to your system.

#### Before you begin

Add Directory Service

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list box, choose IM and Presence.

Step 4

From the Product Type drop-down list box, choose one of the following options:

- Unified CM (IM and Presence)

- WeEx (IM and Presence)

Step 5

Enter a Name for the IM and Presence service.

Step 6

Enter a Description for the IM and Presence service.

Step 7

In the Hostname/IP Address field, enter the hostname, IP address, or DNS SRV for the server that hosts the IM and Presence service.

Tip

Cisco recommends DNS SRV to help the client find the correct IM and Presence service for the user.

Step 8

Click Save .

#### What to do next

Add CTI Service

### Add CTI Service

Add a CTI service to your system.

#### Before you begin

Add IM and Presence Service

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list box, choose CTI .

Step 4

Enter a Name for the CTI service.

Step 5

Enter a Description for the CTI service.

Step 6

In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name for the server that hosts the CTI service.

Step 7

In the Port field, enter the port number of the CTI service. The default port is 2748.

Step 8

Click Save .

#### What to do next

Add Video Conference Scheduling Service

### Add Video Conference Scheduling Service

Add a video conference scheduling service that provides a portal to the TelePresence Management System for video conference
                                 scheduling.

#### Before you begin

Add CTI Service

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

Enter a Name for the service.

Step 4

Enter a Description for the service.

Step 5

In the IP Address/Hostname field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the video conferencing scheduling
                                          service.

Step 6

In the Port field, enter a port number that matches the available port on the video conference scheduling service. The available ports
                                          are:

- 80 (default) or 8080—use these ports for HTTP

- 443 or 8443—use these ports for HTTPS

Step 7

From the Protocol drop-down list box, choose one of the following protocols for communications with the video conference scheduling service:

- HTTP

- HTTPS

Step 8

In the Portal URL field, enter a URL that points to the TelePresence Management System.

Step 9

Click Save .

#### What to do next

Configure a Service Profile

### Add Jabber Client Configuration Service

Step 1

From Cisco Unified CM Administration user interface, choose User Management > User Settings > UC Service .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down list box, choose Jabber Client Configuration (jabber-config.xml) .

Step 4

Enter a Name for the Jabber Client Configuration (jabber-config.xml) service.

Step 5

Enter a Description for the Jabber Client Configuration (jabber-config.xml) service.

Step 6

In the Jabber Configuration Parameters section, choose the required Jabber configuration parameters and values.

Step 7

Click Save .

### Configure UC Services

Use this procedure to configure the UC service connections that your users will use. You can configure connections for the
                                 following UC services:

Voicemail

Mailstore

Conferencing

Directory

IM and Presence Service

CTI

Video Conferencing Scheduling Portal

Jabber Client Configuration (jabber-config.xml)

The fields may vary depending on which UC service you configure.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > UC Services .

Step 2

Click Add New .

Step 3

From the UC Service Type drop-down, select the UC service that you want to configure and click Next .

Step 4

Select the Product Type .

Step 5

Enter a Name for the service.

Step 6

Enter the Hostname or IP address for the server where the service is homed.

Step 7

Complete the Port and Protocol information.

Step 8

Configure the remaining fields. For help with the fields and their settings, refer to the online help. The field options vary
                                          depending on which UC service you are deploying.

Step 9

Click Save .

Step 10

Repeat this procedure until you have provisioned all the UC services that you need.

If you want the service to be located on multiple servers, configure different UC service connections that point to different
                                                         servers. For example, with the IM and Presence Service Centralized Deployment, it is recommended to configure multiple IM
                                                         and Presence UC services that point to different IM and Presence nodes. After you have configured all your UC connections,
                                                         you can add them to a Service Profile.

### Configure a Service Profile

Configure a Service Profile that include the UC Services that you want to assign to end users who use the profile.

#### Before you begin

You must set up your Unified Communications (UC) services before you can add them to a service profile.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile .

Step 2

Click Add New .

Step 3

Enter a Name for the chosen Service Profile Configuration.

Step 4

Enter a Description for the chosen Service Profile Configuration.

Step 5

For each UC service that you want to be a part of this profile, assign the Primary , Secondary , and Tertiary connections for that service.

Step 6

Complete the remaining fields in the Service Profile Configuration window. For detailed field descriptions, see the online help.

Step 7

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure any of the following Unified Communications (UC) services that you want to assign to this service profile: | Configure the UC services settings that you want to set up for your service profiles. |
| Step 2 | Configure a Service Profile | Configure the user's service profile to point to the UC services that you want to apply to this service profile. |

| Step 1 | From Cisco Unified CM Administration choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list box, choose Voicemail . |
| Step 4 | From the Product Type drop-down list box, choose Unity or Unity Connection . |
| Step 5 | Enter a Name for the voicemail service. |
| Step 6 | Enter a Description that helps you distinguish between services. |
| Step 7 | In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the voicemail service. |
| Step 8 | In the Port field, enter a port to connect to the voicemail service. The default port is 443. |
| Step 9 | In the Protocol field, enter the protocol that will be used to route voicemail messages. The available options are HTTP and HTTPS . Note Cisco recommends that you use HTTPS as the voicemail transport protocol for Cisco Unity and Cisco Unity Connection servers.
                                                      Only change to HTTP if your network configuration does not support HTTPS. | Note | Cisco recommends that you use HTTPS as the voicemail transport protocol for Cisco Unity and Cisco Unity Connection servers.
                                                      Only change to HTTP if your network configuration does not support HTTPS. |
| Note | Cisco recommends that you use HTTPS as the voicemail transport protocol for Cisco Unity and Cisco Unity Connection servers.
                                                      Only change to HTTP if your network configuration does not support HTTPS. |
| Step 10 | Click Save . |

| Note | Cisco recommends that you use HTTPS as the voicemail transport protocol for Cisco Unity and Cisco Unity Connection servers.
                                                      Only change to HTTP if your network configuration does not support HTTPS. |
|---|---|

| Note | Cisco Unity creates subscriber mailboxes for message storage on the Microsoft Exchange server. Cisco Unity Connection usually provides a mailstore service, and hosts the mailstore service on the same server. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list box, choose Mailstore . |
| Step 4 | Enter a Name for the mailstore service. |
| Step 5 | Enter a Description for the mailstore service. |
| Step 6 | In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name for the server that hosts the mailstore service. |
| Step 7 | In the Port field, specify a port between 1–65535 that matches the available port on the mailstore service. number between 1 - 65535.
                                          The default mailstore port is 143. Note For secure voice messaging with Cisco Unity connection, use 7993. | Note | For secure voice messaging with Cisco Unity connection, use 7993. |
| Note | For secure voice messaging with Cisco Unity connection, use 7993. |
| Step 8 | In the Protocol field, enter the protocol that will be used to route voicemail messages: TCP (default), TLS, UDP, or SSL. Note For secure messaging with Cisco Unity Connection, use TLS. | Note | For secure messaging with Cisco Unity Connection, use TLS. |
| Note | For secure messaging with Cisco Unity Connection, use TLS. |
| Step 9 | Click Save . |

| Note | For secure voice messaging with Cisco Unity connection, use 7993. |
|---|---|

| Note | For secure messaging with Cisco Unity Connection, use TLS. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list, choose Conferencing . |
| Step 4 | From the Product Type drop-down list, choose the product that you want to use for conferencing: MeetingPlace Classic MettingPlace Express Webex (Conferencing) |
| Step 5 | Enter a Name for the conferencing service. |
| Step 6 | Enter a Description for the conferencing service. |
| Step 7 | In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the conferencing service. |
| Step 8 | In the Port field, enter a port value that matches the available port on the conferencing service. The recommended values are: 80 (default setting)—Use this port for HTTP 443—Use this port for HTTPS |
| Step 9 | From the Protocol drop-down list, choose the Protocol to use when endpoints contact this service: HTTP HTTPS |
| Step 10 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose USer Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list box, choose Directory . |
| Step 4 | From the Product Type field, choose either of the following: Directory—Choose this option if you want your clients to use UDS to connect to the Cisco Unified Communications Manager database
                                             for directory lookups. Enhanced Directory—Choose this option if you want your clients to connect to an external LDAP directory for directory lookups. |
| Step 5 | Enter a Name for the directory service. |
| Step 6 | Enter a Description for the directory service. |
| Step 7 | In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the directory service that
                                          you want your clients to use for directory lookups. Note If you are using an external LDAP directory for directory lookups, enter the hostname, IP address, or fully qualified domain
                                                         name of the  LDAP directory. | Note | If you are using an external LDAP directory for directory lookups, enter the hostname, IP address, or fully qualified domain
                                                         name of the  LDAP directory. |
| Note | If you are using an external LDAP directory for directory lookups, enter the hostname, IP address, or fully qualified domain
                                                         name of the  LDAP directory. |
| Step 8 | In the Port field, enter a port number that matches the available port on the directory service. The default port value is 389. In addition,
                                          ports 636, 3628, 3629 can connect to an external LDAP directory. |
| Step 9 | In the Protocol field, enter the protocol that will be used to route  communications between the directory service and endpoints. The available
                                          options are: TCP (default setting) UDP TLS |
| Step 10 | Click Save . |

| Note | If you are using an external LDAP directory for directory lookups, enter the hostname, IP address, or fully qualified domain
                                                         name of the  LDAP directory. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list box, choose IM and Presence. |
| Step 4 | From the Product Type drop-down list box, choose one of the following options: Unified CM (IM and Presence) WeEx (IM and Presence) |
| Step 5 | Enter a Name for the IM and Presence service. |
| Step 6 | Enter a Description for the IM and Presence service. |
| Step 7 | In the Hostname/IP Address field, enter the hostname, IP address, or DNS SRV for the server that hosts the IM and Presence service. Tip Cisco recommends DNS SRV to help the client find the correct IM and Presence service for the user. | Tip | Cisco recommends DNS SRV to help the client find the correct IM and Presence service for the user. |
| Tip | Cisco recommends DNS SRV to help the client find the correct IM and Presence service for the user. |
| Step 8 | Click Save . |

| Tip | Cisco recommends DNS SRV to help the client find the correct IM and Presence service for the user. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list box, choose CTI . |
| Step 4 | Enter a Name for the CTI service. |
| Step 5 | Enter a Description for the CTI service. |
| Step 6 | In the Hostname/IP Address field, enter the hostname, IP address, or fully qualified domain name for the server that hosts the CTI service. |
| Step 7 | In the Port field, enter the port number of the CTI service. The default port is 2748. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the service. |
| Step 4 | Enter a Description for the service. |
| Step 5 | In the IP Address/Hostname field, enter the hostname, IP address, or fully qualified domain name of the server that hosts the video conferencing scheduling
                                          service. |
| Step 6 | In the Port field, enter a port number that matches the available port on the video conference scheduling service. The available ports
                                          are: 80 (default) or 8080—use these ports for HTTP 443 or 8443—use these ports for HTTPS |
| Step 7 | From the Protocol drop-down list box, choose one of the following protocols for communications with the video conference scheduling service: HTTP HTTPS |
| Step 8 | In the Portal URL field, enter a URL that points to the TelePresence Management System. |
| Step 9 | Click Save . |

| Step 1 | From Cisco Unified CM Administration user interface, choose User Management > User Settings > UC Service . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down list box, choose Jabber Client Configuration (jabber-config.xml) . |
| Step 4 | Enter a Name for the Jabber Client Configuration (jabber-config.xml) service. |
| Step 5 | Enter a Description for the Jabber Client Configuration (jabber-config.xml) service. |
| Step 6 | In the Jabber Configuration Parameters section, choose the required Jabber configuration parameters and values. |
| Step 7 | Click Save . |

| Note | The fields may vary depending on which UC service you configure. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > UC Services . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the UC Service Type drop-down, select the UC service that you want to configure and click Next . |
| Step 4 | Select the Product Type . |
| Step 5 | Enter a Name for the service. |
| Step 6 | Enter the Hostname or IP address for the server where the service is homed. |
| Step 7 | Complete the Port and Protocol information. |
| Step 8 | Configure the remaining fields. For help with the fields and their settings, refer to the online help. The field options vary
                                          depending on which UC service you are deploying. |
| Step 9 | Click Save . |
| Step 10 | Repeat this procedure until you have provisioned all the UC services that you need. Note If you want the service to be located on multiple servers, configure different UC service connections that point to different
                                                         servers. For example, with the IM and Presence Service Centralized Deployment, it is recommended to configure multiple IM
                                                         and Presence UC services that point to different IM and Presence nodes. After you have configured all your UC connections,
                                                         you can add them to a Service Profile. | Note | If you want the service to be located on multiple servers, configure different UC service connections that point to different
                                                         servers. For example, with the IM and Presence Service Centralized Deployment, it is recommended to configure multiple IM
                                                         and Presence UC services that point to different IM and Presence nodes. After you have configured all your UC connections,
                                                         you can add them to a Service Profile. |
| Note | If you want the service to be located on multiple servers, configure different UC service connections that point to different
                                                         servers. For example, with the IM and Presence Service Centralized Deployment, it is recommended to configure multiple IM
                                                         and Presence UC services that point to different IM and Presence nodes. After you have configured all your UC connections,
                                                         you can add them to a Service Profile. |

| Note | If you want the service to be located on multiple servers, configure different UC service connections that point to different
                                                         servers. For example, with the IM and Presence Service Centralized Deployment, it is recommended to configure multiple IM
                                                         and Presence UC services that point to different IM and Presence nodes. After you have configured all your UC connections,
                                                         you can add them to a Service Profile. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the chosen Service Profile Configuration. |
| Step 4 | Enter a Description for the chosen Service Profile Configuration. |
| Step 5 | For each UC service that you want to be a part of this profile, assign the Primary , Secondary , and Tertiary connections for that service. |
| Step 6 | Complete the remaining fields in the Service Profile Configuration window. For detailed field descriptions, see the online help. |
| Step 7 | Click Save . |