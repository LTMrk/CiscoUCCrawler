---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-c2938290d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_cvp-device-configuration-api_15_0_1.html
retrieved_at: 2026-08-21T16:45:58.090763+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: CVP Device Configuration API

## Chapter: CVP Device Configuration API

- CVP Device Configuration API

- CVP Device Configuration API

# CVP Device Configuration API

## CVP Device Configuration API

Use the GET API to get the device configuration information of the CVP Call Server for the specified remote site. If no remote
                           site is specified, it will retrieve the information for the main site.

### URL

### Operations

get : Gets the device configuration information of the CVP Call Server for the specified remote site using the URL: https://<server>:<serverport>/unifiedconfig/config/deviceconfig/<site_name>/cvpserver .

update : Updates the configuration details for CVP devices.

If the configuration types (ICM, SIP, IVR, VXML, Infra , Media Server ) are set as empty, the configuration related to the respective configuration type gets deleted.

### Parameters

ICM

vruConnectionPort: Required. The port number on which the ICM Service listens for a TCP connection from the ICM PIM. It can
                                          be any valid TCP/IP connection port.

maximumLengthDNIS maxDNISLength : Required. The maximum length of an incoming Dialed Number Identification Service (DNIS). The range is 1 - 99999.

enableTrunkUtilization: Default value is false.

maxGatewayPorts: Maximum number of ports that a gateway supports. This is available only if enableTrunkUtilization is true.
                                          The range is 1 - 1500.

gateways: The list of gateways available for trunk reporting. This is available only if enableTrunkUtilization is true.

gateway: The gateway available for trunk reporting.

refURL: The MachineInventory reference URL of the gateway machine.

trunkGroupId: The Trunk Group ID of the gateway.

enableSecureVRU: To enable secure communication between ICM and VRU PIM. Default value is false.

SIP

enableOutboundProxy: Use a Cisco Unified SIP Server Group.

proxyHost: The SIP Server Group name of type External. This is available only if useOutboundProxy is true.

outboundProxyPort: Port on which the SIP service sends requests to the outbound proxy server. This is available only if useOutboundProxy
                                          is true. The range is 1-65535.

useSrv: Use DNS SRV for outbound proxy lookup.

useLocalSrv: Select to resolve the SRV domain name with a local configuration file instead of a DNS Server. Values can be
                                          enabled/disabled.

outgoingTransport: Transport type for outgoing SIP requests. It can be TCP/UDP.

incomingPort: Required. Port on which the SIP Service listens for incoming SIP requests. The range is 1-65535.

sigDigits: The range is 1-20.

useErrorRefer: Default is false.

toneDuration: Required. Default is 100.

commaDuration: Required. Default is 100.

sipHeaders: It can have a maximum length of 255 characters.

sipHeader

name

value

incomingSecurePort: Required. Default is 5061.

incomingSecureTransport: Default is TLS.

outgoingSecureTransport: Default is TLS.

supportedTLSVersions: Default is TLSv1.2. Values are TLS1.0, TLSv1.1, and TLSv1.2.

secureCiphers: Default is TLS_RSA_WITH_AES_128_CBC_SHA.

IVR

generateHttpsURL: Default is yes. Values can be true/false or yes/no.

useBackupMediaServers, useBackupASRTTSServers: If you select Yes (default) and a media server is unavailable, the gateway
                                          attempts to connect to the backup Media Server. Values can be true/false or yes/no.

useMediaServerHostNames: If you select No (default), the IP address is used for the XML Server and Media Server. If you select
                                          Yes, the hostnames are used rather than IP addresses. Values can be true/false or yes/no.

CallTimeout: Required. The number of seconds the IVR Service waits for a response from the SIP Service before timing out.
                                          This setting should be longer than the longest prompt, transfer or digit collection at a Voice Browser. If the timeout is
                                          reached, the call is canceled but no other calls are affected. The only downside to making the number arbitrarily large is
                                          that if calls are being stranded, they will not be removed from the IVR Service until this timeout is reached. Default is
                                          7200. It can be 6 seconds or higher.

VXML

enableReporting: Indicates whether or not the Unified CVP VXML Server sends data to the Reporting Server. If disabled, no
                                          data is sent to the Reporting Server, and reports do not contain any VXML application data. Value can be enabled/disabled.

reportingDetail: Indicates whether VXML application details are reported. Value can be enabled/disabled.

inclusiveFilters: List of applications, element types, element names, and element fields, and ECC variables to include in
                                          reporting data. Range is a semicolon-separated list of text strings. A wildcard character (*) is allowed within each element
                                          in the list.

exclusiveFilters: List of applications, element types, element names, and element fields, and ECC variables to exclude from
                                          reporting data. Range is a semicolon-separated list of text strings. A wildcard character (*) is allowed within each element
                                          in the list.

Infrastructure

maxLogFileSize: Required. Maximum number of threads allocated in the thread pool, which can be shared by all services running
                                          as part of a CVP Web Application. Range can be 100-1000.

maxLogDirectorySize: Required. Maximum number of megabytes to allocate for disk storage for log files. Note Modifying the
                                          value to a setting that is below the default value might cause logs to be rolled over quickly. Consequently, log entries might
                                          be lost, which can affect troubleshooting. Range is 500 - 500000. The log folder size divided by the log file size must be
                                          less than 5000.

syslogServer: Hostname or IP address of Primary Syslog Server to send syslog events from a CVP Application. It can be a valid
                                          IP address or hostname.

syslogServerPort: Port number of Primary Syslog Server. The range is 1-65535.

syslogBackupServer: Hostname or IP address of the Primary Backup Syslog Server to send syslog events from a CVP Application
                                          when the Syslog Server cannot be reached. It can be a valid IP address or hostname.

syslogBackupServerPort: Port number of Primary Backup Syslog Server. The range is 1-65535.

syslogSecondaryServer: Hostname or IP address of the Secondary Syslog Server to send syslog events from a CVP Application
                                          when the Syslog Server cannot be reached. It can be a valid IP address or hostname.

syslogSecondaryServerPort: Port number of Secondary Syslog Server. The range is 1-65535.

syslogSecondaryBackupServer: Hostname or IP address of the Secondary Backup Syslog Server to send syslog events from a CVP
                                          Application when the Syslog Server cannot be reached. It can be a valid IP address or hostname.

syslogSecondaryBackupServerPort: Port number of Secondary Backup Syslog Server. The range is 1-65535.

Media Server Properties

defaultMediaServer: To set the default Media Server for all the available CVP Servers in the specified site. Provide IP address
                                          of the Media Server.

You must configure atleast one Media Server.

Default Media Server must be one of the configured Media Servers.

### Example Get Response

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<CVP>
 <icm>
   <enableSecureVRU>false</enableSecureVRU>
   <enableTrunkUtilization>false</enableTrunkUtilization> 
   <gateways/>
   <maxDNISLength>10</maxDNISLength> 
   <maxGatewayPorts>700</maxGatewayPorts>
   <vruConnectionPort>5000</vruConnectionPort>
 </icm>
 <infrastructure>
   <maxLogDirectorySize>20000</maxLogDirectorySize>
   <maxLogFileSize>100</maxLogFileSize>
   <syslogBackupServer/>
   <syslogBackupServerPort>514</syslogBackupServerPort>
   <syslogSecondaryBackupServer/>
   <syslogSecondaryBackupServerPort>514</syslogSecondaryBackupServerPort>
   <syslogSecondaryServer/>
   <syslogSecondaryServerPort>514</syslogSecondaryServerPort>
   <syslogServer/>
   <syslogServerPort>514</syslogServerPort>
 </infrastructure>
 <ivr>
   <callTimeout>7200</callTimeout>
   <useBackupMediaServers>true</useBackupMediaServers>
   <useMediaServerHostNames>false</useMediaServerHostNames>
   <useSecurityForMediaFetches>false</useSecurityForMediaFetches>
 </ivr>
<mediaServer>
   <defaultMediaServer>10.10.10.100</defaultMediaServer>
   
</mediaServer>
<sip>
  <commaDuration>100</commaDuration>
  <enableOutboundProxy>false</enableOutboundProxy>
  <incomingPort>5060</incomingPort>
  <incomingSecurePort>5061</incomingSecurePort>
  <outboundProxyPort>5060</outboundProxyPort>
  <outgoingTransport>TCP</outgoingTransport>
  <secureCiphers>TLS_RSA_WITH_AES_128_CBC_SHA</secureCiphers>
  <sigDigits>0</sigDigits>
  <sipHeaders>
   <sipHeader>
     <name>n1</name>
     <value>v1</value>
   </sipHeader>
  <sipHeader>
     <name>n1</name>
     <value>v1</value>
  </sipHeader>
 </sipHeaders>
 <supportedTLSVersion>TLSv1.2</supportedTLSVersion>
 <toneDuration>100</toneDuration>
 <useErrorRefer>true</useErrorRefer>
 <useLocalSrv>true</useLocalSrv>
 <useSrv>true</useSrv>
</sip>
<vxml>
  <enableAppDetailsReporting>false</enableAppDetailsReporting>
  <enableReporting>true</enableReporting>
</vxml>
</CVP>
```

| Note | You must configure atleast one Media Server. Default Media Server must be one of the configured Media Servers. |
|---|---|