---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-smtp-configuration-html-1eed122d25
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_smtp_configuration.html
retrieved_at: 2026-08-17T03:50:15.577066+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for SMTP Configuration

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for SMTP Configuration

# Cisco Unity Connection Provisioning Interface (CUPI) API for SMTP Configuration

Cisco Unity Connection 14SU2 and later, supports secure SMTP client communication over port 25 and 587 using authentication
                        support. Administrator can use this API to update or fetch the SMTP configuration. Unity Connection can act as both server
                        or client depending upon the requirement.

## Cisco Unity Connection Provisioning Interface (CUPI) API -- SMTP Server Configuration

Administrator can configure port 25 or port 587 for inbound SMTP communications over STARTTLS.

### Listing SMTP Server Configuration

The request can be used to fetch the SMTP server side configuration present currently on the system.

```
GET https://<connection-server>/vmrest/smtpserver/serverconfigs
```

The following is the response from the above *GET* request and the actual response will depend upon the current SMTP server
                              configuration.

```
<SmtpServerConfiguration>
    <Port>587</Port>
    <domainName>ucbu-aricent-vm234.cisco.com</domainName>
    <maxNumberConnections>20</maxNumberConnections>
    <smtpClientThreads>2</smtpClientThreads>
    <maxMessageSizeKb>10000</maxMessageSizeKb>
    <maxNumberMessagesSession>10</maxNumberMessagesSession>
    <maxNumberRecipients>15000</maxNumberRecipients>
    <retryDeliveryTimeoutMin>240</retryDeliveryTimeoutMin>
    <allowConnectionsFromUntrustedIpAddresses>true</allowConnectionsFromUntrustedIpAddresses>
    <requireAuthenticationFromUntrustedIpAddresses>true</requireAuthenticationFromUntrustedIpAddresses>
    <requireTlsFromUntrustedIpAddresses>1</requireTlsFromUntrustedIpAddresses>
</SmtpServerConfiguration>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/smtpserver/serverconfigs
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the current SMTP server
                              configuration:

```
{
         "Port": "587",
         "domainName": "ucbu-aricent-vm234.cisco.com",
         "maxNumberConnections": "20",
         "smtpClientThreads": "2",
         "maxMessageSizeKb": "10000",
         "maxNumberMessagesSession": "10",
         "maxNumberRecipients": "15000",
         "retryDeliveryTimeoutMin": "240",
         "allowConnectionsFromUntrustedIpAddresses": "true",
         "requireAuthenticationFromUntrustedIpAddresses": "true",
         "requireTlsFromUntrustedIpAddresses": "1"
 }
```

```
Response Code: 200
```

### Updating SMTP Server Configuration

The following is an example of the PUT request that update the configuration of SMTP Server.

```
PUT https://<connection-server>/vmrest/smtpserver/serverconfigs
```

```
<SmtpServerConfiguration>
    <Port>25</Port>
    <domainName>ucbu-aricent-vm234.cisco.com</domainName>
    <maxNumberConnections>20</maxNumberConnections>
    <smtpClientThreads>2</smtpClientThreads>
    <maxMessageSizeKb>10000</maxMessageSizeKb>
    <maxNumberMessagesSession>10</maxNumberMessagesSession>
    <maxNumberRecipients>15000</maxNumberRecipients>
    <retryDeliveryTimeoutMin>240</retryDeliveryTimeoutMin>
    <allowConnectionsFromUntrustedIpAddresses>true</allowConnectionsFromUntrustedIpAddresses>
    <requireAuthenticationFromUntrustedIpAddresses>true</requireAuthenticationFromUntrustedIpAddresses>
    <requireTlsFromUntrustedIpAddresses>1</requireTlsFromUntrustedIpAddresses>
</SmtpServerConfiguration>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 200
```

JSON Example

```
PUT https://<connection-server>/vmrest/smtpserver/serverconfigs
Accept: application/json
Connection: keep_alive
Request Body:{
         "Port": "25",
         "domainName": "ucbu-aricent-vm234.cisco.com",
         "maxNumberConnections": "20",
         "smtpClientThreads": "2",
         "maxMessageSizeKb": "10000",
         "maxNumberMessagesSession": "10",
         "maxNumberRecipients": "15000",
         "retryDeliveryTimeoutMin": "240",
         "allowConnectionsFromUntrustedIpAddresses": "true",
         "requireAuthenticationFromUntrustedIpAddresses": "true",
         "requireTlsFromUntrustedIpAddresses": "1"
      }
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 200
```

### Explaination of Data Fields

The following table explain the data fields:

25

587

Specifies the maximum number of SMTP clients that can be connected to the Unity Connection SMTP server at one time for sending
                                             messages.

Possible values can be between 0 - 50.

Default setting: 20 Unity Connections.

Specifies the maximum number of outgoing connections that the Unity Connection SMTP server can have open with other SMTP servers
                                             at one time.

Possible values can be between 0 - 10.

Default setting: 2 connections.

Specifies the maximum size of message that clients can send to Unity Connection using SMTP.

Possible values can be between 0 - 50000 Kilobytes.

Default setting: 10,000 kilobytes (approximately 10 megabytes).

Specifies the maximum number of messages that a client can send to Unity Connection in a single SMTP session.

Possible values can be between 0 - 100.

Default setting: 10 messages.

Specifies the maximum number of recipients allowed for a single message that is sent by a client to Unity Connection using
                                             SMTP.

Possible values can be between 0 - 50000

Default setting: 15,000 recipients.

Specifies the time interval in minutes to have Unity Connection periodically retries the delivery of SMTP messages that have
                                             failed because of issues that may be temporary (for example, the remote SMTP server is not responding). If the timeout has
                                             passed without success, Unity Connection sends a non-delivery receipt to the sender.

Default setting: 0 minutes (Unity Connection immediately sends a non-delivery receipt to the sender and does not retry delivery
                                             of failed SMTP messages).

A flag indicating whether the Unity Connection enable or disable the SMTP connections from clients or servers whose IP addresses
                                             do not match any address pattern that is configured on the IP Address Access List .

Possible values:

false

true

Default setting: false

A flag indicating whether the Unity Connection requires authentication for SMTP connections from clients or servers whose
                                             IP addresses do not match any address pattern that is configured on the IP Address Access List .

Possible values:

false : Unity Connection allows clients to connect without authenticating.

true : Unity Connection require authentication from clients for connections.

This option is unavailable when the Allow Connections from Untrusted IP Addresses field is disabled.

Specifies how Unity Connection handles Transport Layer Security (TLS) with a client or server that attempts to connect from
                                             an IP address that does not match any address pattern configured on the IP Address Access List .

Possible values:

0 : Unity Connection does not offer TLS as an option for SMTP sessions initiated by clients or servers with untrusted IP addresses.

1 : Clients or servers connecting from untrusted IP addresses must use TLS to initiate SMTP sessions with the Unity Connection
                                                   server.

2 : Clients or servers connecting from untrusted IP addresses can use TLS to initiate SMTP sessions with the Unity Connection
                                                   server, but are not required to do so.

This option is unavailable when the Allow Connections from Untrusted IP Addresses field is disabled.

## Cisco Unity Connection Provisioning Interface (CUPI) API -- SMTP Client Configuration

Administrator can configure port 25 or port 587 for outbound SMTP communications over STARTTLS.

### Listing SMTP Client Configuration

The request can be used to fetch the SMTP client side configuration present currently on the system.

```
GET https://<connection-server>/vmrest/smtpclient/clientconfigs
```

The following is the response from the above *GET* request and the actual response will depend upon the the current SMTP client
                              configuration:

```
<SmtpClientConfiguration>
    <smtpSmartHost>outbound.cisco.com</smtpSmartHost>
    <isClientSecure>true</isClientSecure>
    <smtpPort>25</smtpPort>
    <isAuthEnabled>true</isAuthEnabled>
    <smtpUsername>Admin</smtpUsername>
    <smtpPassword></smtpPassword>
</SmtpClientConfiguration>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/smtpclient/clientconfigs
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the current SMTP client
                              configuration.

```
{
         "smtpSmartHost": "outbound.cisco.com",
         "isClientSecure": "true",
         "smtpPort": "25",
         "isAuthEnabled": "true",
         "smtpUsername": "Admin",
         "smtpPassword": "",
}
```

```
Response Code: 200
```

### Updating SMTP Client Configuration

The following is an example of the PUT request that update the configuration of SMTP Client.

```
PUT https://<connection-server>/vmrest/smtpclient/clientconfigs
```

```
<SmtpClientConfiguration>
    <smtpSmartHost>outbound.cisco.com</smtpSmartHost>
    <isClientSecure>true</isClientSecure>
    <smtpPort>25</smtpPort>
    <isAuthEnabled>true</isAuthEnabled>
    <smtpUsername>Admin</smtpUsername>
    <smtpPassword>smtp</smtpPassword>
</SmtpClientConfiguration>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/smtpclient/clientconfigs
Accept: application/json
Connection: keep_alive
Request Body:{
        "smtpSmartHost": "outbound.cisco.com",
         "isClientSecure": "true",
         "smtpPort": "587",
         "isAuthEnabled": "false",
         "smtpUsername" : "Admin" 
         "smtpPassword" : "smtp"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                              by you:

```
Response Code: 204
```

### Explaination of Data Fields

The following table explain the data fields:

A flag indicating whether the SMTP communication on Unity Connection is secure or non secure.

Possible values:

false

true

Default setting: false

If IsClientSecure checkbox is not checked, Unity Connection will initiate request towards Smart Host over port 25 without using STARTTLS. It
                                                         is non secure mode of communication. If it is checked, then Unity Connection will initiate request towards Smart Host over
                                                         port 587 using STARTTLS. It is secure mode of communication.

25

587

Possible values:

false

true

Default setting: false

| GET https://<connection-server>/vmrest/smtpserver/serverconfigs |
|---|

| <SmtpServerConfiguration>
    <Port>587</Port>
    <domainName>ucbu-aricent-vm234.cisco.com</domainName>
    <maxNumberConnections>20</maxNumberConnections>
    <smtpClientThreads>2</smtpClientThreads>
    <maxMessageSizeKb>10000</maxMessageSizeKb>
    <maxNumberMessagesSession>10</maxNumberMessagesSession>
    <maxNumberRecipients>15000</maxNumberRecipients>
    <retryDeliveryTimeoutMin>240</retryDeliveryTimeoutMin>
    <allowConnectionsFromUntrustedIpAddresses>true</allowConnectionsFromUntrustedIpAddresses>
    <requireAuthenticationFromUntrustedIpAddresses>true</requireAuthenticationFromUntrustedIpAddresses>
    <requireTlsFromUntrustedIpAddresses>1</requireTlsFromUntrustedIpAddresses>
</SmtpServerConfiguration> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/smtpserver/serverconfigs
Accept: application/json
Connection: keep_alive |
|---|

| {
         "Port": "587",
         "domainName": "ucbu-aricent-vm234.cisco.com",
         "maxNumberConnections": "20",
         "smtpClientThreads": "2",
         "maxMessageSizeKb": "10000",
         "maxNumberMessagesSession": "10",
         "maxNumberRecipients": "15000",
         "retryDeliveryTimeoutMin": "240",
         "allowConnectionsFromUntrustedIpAddresses": "true",
         "requireAuthenticationFromUntrustedIpAddresses": "true",
         "requireTlsFromUntrustedIpAddresses": "1"
 } |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/smtpserver/serverconfigs |
|---|

| PUT https://<connection-server>/vmrest/smtpserver/serverconfigs
Accept: application/json
Connection: keep_alive
Request Body:{
         "Port": "25",
         "domainName": "ucbu-aricent-vm234.cisco.com",
         "maxNumberConnections": "20",
         "smtpClientThreads": "2",
         "maxMessageSizeKb": "10000",
         "maxNumberMessagesSession": "10",
         "maxNumberRecipients": "15000",
         "retryDeliveryTimeoutMin": "240",
         "allowConnectionsFromUntrustedIpAddresses": "true",
         "requireAuthenticationFromUntrustedIpAddresses": "true",
         "requireTlsFromUntrustedIpAddresses": "1"
      } |
|---|

| Response Code: 200 |
|---|

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| Port | Integer | Read/Write | Specifies the port that Unity Connection uses to support secure/non-secure SMTP client communication. Possible values: 25 587 Default Value : 25 |
| DomainName | String | Read/Write | Specifies the domain name that Unity Connection uses to route messages between digitally networked Unity Connection servers
                                          and to construct the SMTP address of the sender on outgoing SMTP messages. |
| MaxNumberConnections | Integer | Read/Write | Specifies the maximum number of SMTP clients that can be connected to the Unity Connection SMTP server at one time for sending
                                             messages. Possible values can be between 0 - 50. Default setting: 20 Unity Connections. |
| SmtpClientThreads | Integer | Read/Write | Specifies the maximum number of outgoing connections that the Unity Connection SMTP server can have open with other SMTP servers
                                             at one time. Possible values can be between 0 - 10. Default setting: 2 connections. |
| MaxMessageSizeKb | Integer | Read/Write | Specifies the maximum size of message that clients can send to Unity Connection using SMTP. Possible values can be between 0 - 50000 Kilobytes. Default setting: 10,000 kilobytes (approximately 10 megabytes). |
| MaxNumberMessagesSession | Integer | Read/Write | Specifies the maximum number of messages that a client can send to Unity Connection in a single SMTP session. Possible values can be between 0 - 100. Default setting: 10 messages. |
| MaxNumberRecipients | Integer | Read/Write | Specifies the maximum number of recipients allowed for a single message that is sent by a client to Unity Connection using
                                             SMTP. Possible values can be between 0 - 50000 Default setting: 15,000 recipients. |
| RetryDeliveryTimeoutMin | Integer | Read/Write | Specifies the time interval in minutes to have Unity Connection periodically retries the delivery of SMTP messages that have
                                             failed because of issues that may be temporary (for example, the remote SMTP server is not responding). If the timeout has
                                             passed without success, Unity Connection sends a non-delivery receipt to the sender. Default setting: 0 minutes (Unity Connection immediately sends a non-delivery receipt to the sender and does not retry delivery
                                             of failed SMTP messages). |
| AllowConnectionsFromUntrustedIpAddresses | Boolean | Read/Write | A flag indicating whether the Unity Connection enable or disable the SMTP connections from clients or servers whose IP addresses
                                             do not match any address pattern that is configured on the IP Address Access List . Possible values: false true Default setting: false |
| RequireAuthenticationFromUntrustedIpAddresses | Boolean | Read/Write | A flag indicating whether the Unity Connection requires authentication for SMTP connections from clients or servers whose
                                             IP addresses do not match any address pattern that is configured on the IP Address Access List . Possible values: false : Unity Connection allows clients to connect without authenticating. true : Unity Connection require authentication from clients for connections. This option is unavailable when the Allow Connections from Untrusted IP Addresses field is disabled. |
| RequireTlsFromUntrustedIpAddresses | Integer | Read/Write | Specifies how Unity Connection handles Transport Layer Security (TLS) with a client or server that attempts to connect from
                                             an IP address that does not match any address pattern configured on the IP Address Access List . Possible values: 0 : Unity Connection does not offer TLS as an option for SMTP sessions initiated by clients or servers with untrusted IP addresses. 1 : Clients or servers connecting from untrusted IP addresses must use TLS to initiate SMTP sessions with the Unity Connection
                                                   server. 2 : Clients or servers connecting from untrusted IP addresses can use TLS to initiate SMTP sessions with the Unity Connection
                                                   server, but are not required to do so. This option is unavailable when the Allow Connections from Untrusted IP Addresses field is disabled. |

| GET https://<connection-server>/vmrest/smtpclient/clientconfigs |
|---|

| <SmtpClientConfiguration>
    <smtpSmartHost>outbound.cisco.com</smtpSmartHost>
    <isClientSecure>true</isClientSecure>
    <smtpPort>25</smtpPort>
    <isAuthEnabled>true</isAuthEnabled>
    <smtpUsername>Admin</smtpUsername>
    <smtpPassword></smtpPassword>
</SmtpClientConfiguration> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/smtpclient/clientconfigs
Accept: application/json
Connection: keep_alive |
|---|

| {
         "smtpSmartHost": "outbound.cisco.com",
         "isClientSecure": "true",
         "smtpPort": "25",
         "isAuthEnabled": "true",
         "smtpUsername": "Admin",
         "smtpPassword": "",
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/smtpclient/clientconfigs |
|---|

| PUT https://<connection-server>/vmrest/smtpclient/clientconfigs
Accept: application/json
Connection: keep_alive
Request Body:{
        "smtpSmartHost": "outbound.cisco.com",
         "isClientSecure": "true",
         "smtpPort": "587",
         "isAuthEnabled": "false",
         "smtpUsername" : "Admin" 
         "smtpPassword" : "smtp"
} |
|---|

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| SMTPSmartHost | String | Read/Write | Specifies the IP address or fully qualified domain name of the SMTP smart host through which Cisco Unity Connection relays
                                          SMTP messages. |
| IsClientSecure | Boolean | Read/Write | A flag indicating whether the SMTP communication on Unity Connection is secure or non secure. Possible values: false true Default setting: false Note If IsClientSecure checkbox is not checked, Unity Connection will initiate request towards Smart Host over port 25 without using STARTTLS. It
                                                         is non secure mode of communication. If it is checked, then Unity Connection will initiate request towards Smart Host over
                                                         port 587 using STARTTLS. It is secure mode of communication. | Note | If IsClientSecure checkbox is not checked, Unity Connection will initiate request towards Smart Host over port 25 without using STARTTLS. It
                                                         is non secure mode of communication. If it is checked, then Unity Connection will initiate request towards Smart Host over
                                                         port 587 using STARTTLS. It is secure mode of communication. |
| Note | If IsClientSecure checkbox is not checked, Unity Connection will initiate request towards Smart Host over port 25 without using STARTTLS. It
                                                         is non secure mode of communication. If it is checked, then Unity Connection will initiate request towards Smart Host over
                                                         port 587 using STARTTLS. It is secure mode of communication. |
| SMTPPort | Integer | Read/Write | Unity Connection will communicate to external SMTP servers on below ports. 25 587 |
| isAuthEnabled | Boolean | Read/Write | A flag indicating whether the SMTP communication is password protected or not. Possible values: false true Default setting: false |
| smtpUsername | String | Read/Write | Username of Smart Host. |
| smtpPassword | String | Only Write | Password of Smart Host. |

| Note | If IsClientSecure checkbox is not checked, Unity Connection will initiate request towards Smart Host over port 25 without using STARTTLS. It
                                                         is non secure mode of communication. If it is checked, then Unity Connection will initiate request towards Smart Host over
                                                         port 587 using STARTTLS. It is secure mode of communication. |
|---|---|