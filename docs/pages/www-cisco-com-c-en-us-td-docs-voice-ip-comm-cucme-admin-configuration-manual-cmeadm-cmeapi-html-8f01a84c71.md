---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeapi-html-8f01a84c71
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeapi.html
retrieved_at: 2026-08-21T07:25:38.281534+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Configure the XML API

## Chapter: Configure the XML API

# Configure the XML API

This chapter describes the eXtensible Markup Language (XML) Application
                        		Programming Interface (API) support available in Cisco Unified Communications
                        		Manager Express (Cisco Unified CME).

## Information About XML API

### XML API Definition

An XML API provides an interface to Cisco Unified CME that allows an
                              		external network management system (NMS) to configure and monitor
                              		Cisco Unified CME operations.

### XML API Provision Using IXI

In previous versions of Cisco Unified CME, the XML interface provided
                              		configuration and monitoring functions using the HTTP port. The XML interface
                              		ran under the HTTP server process, simultaneously parsing incoming XML requests
                              		on demand and processing them.

In Cisco Unified CME 4.0 and later versions, the XML interface is
                              		provided through the Cisco IOS XML Infrastructure (IXI), in which the parser
                              		and transport layers are separated from the application. This modularity
                              		provides scalability and enables future XML support to be developed. In
                              		Cisco Unified CME 4.0 and later versions, all Cisco Unified CME features have
                              		XML support.

### XML API for Cisco Unified CME

The eXtensible Markup Language (XML) Application Programming Interface
                              		(API) is supported in Cisco Unified Communications Manager Express
                              		(Cisco Unified CME) 8.5 and later versions.

### Target
                           	 Audience

TCP/IP Protocol

Hypertext
                                       			 Transport Protocol

Socket
                                       			 programming

XML

In addition, users
                              		of this programming guide must have a firm grasp of XML Schema, which is used
                              		to define the AXL requests, responses, and errors. For more information on XML
                              		Schema, see XML Schema Part 0: Primer Second Edition .

### Prerequisites

For
                                    			 Cisco Unified CME: XML API must be configured in Cisco Unified CME. For
                                    			 configuration information, see Configure the XML API of the Cisco Unified CME Administrator Guide .

### Information on XML
                           	 API for Cisco Unified CME

The XML API support
                              		in Cisco Unified CME provides a mechanism for inserting, retrieving, updating,
                              		and removing data from the Cisco router using XML.

Request methods are
                              		XML structures that are passed to the XML server in Cisco Unified CME and
                              		Cisco Unified SRST applications using HTTP POST. The XML server receives the
                              		XML structures and executes the request. If the request completes successfully,
                              		then the appropriate XML response is returned.

Querying for
                                          		  multiple entities in a single request can fail because of the XML buffer size
                                          		  limitation. Because of this limitation, the application must adjust its
                                          		  granularity to query one entity per request.

Table 1 lists the request and response methods for the XML API along with the purpose
                              		and parameters for each method.

Description

Request

Parameter

Response

System

Execute
                                             					 configuration commands

ISexecCLI

command

ISexecCLIResult

Save
                                             					 router configuration to nvram

ISSaveConfig

—

ISSaveConfigResult

SCCP

Get system
                                             					 status for Cisco Unified CME or Cisco Unified SRST.

ISgetGlobal

—

ISGlobal

Get status
                                             					 of an IP phone

ISgetDevice

Any
                                             					 combination of the following:

ISDevID

ISDevName

ISKeyword:

all

allTag

available

ISDevices

Get
                                             					 configuration of a phone template

ISgetDeviceTemplate

Any
                                             					 combination of the following:

ISDevTemplateID

ISKeyword:

all

allTag

available

ISDeviceTemplates

Get
                                             					 configuration of an extension

ISgetExtension

Any
                                             					 combination of the following:

ISExtID

ISExtNumber

ISKeyword:

all

allTag

available

ISExtensions

Get
                                             					 configuration of an extension template

ISgetExtensionTemplate

Any
                                             					 combination of the following:

ISExtTemplateID

ISKeyword:

all

allTag

available

ISExtensionTemplates

Get user
                                             					 information

ISgetUser

ISuserID

ISuser

Get user
                                             					 profile information

ISgetuserProfile

Any
                                             					 combination of the following:

ISUserProfileID

ISuserID

ISKeyword:

all

allTag

available

ISUserProfiles

Get
                                             					 configuration for utility directory

ISgetUtilityDirectory

—

ISUtilityDirectory

SIP

Get
                                             					 system status for a Cisco Unified CME running SIP

ISgetVoiceRegGlobal

—

ISSipGlobal

Get
                                             					 status of an IP phone

ISgetSipDevice

Any
                                             					 combination of the following:

ISPoolID

ISPoolName

ISKeyword:

all

allTag

available

ISSipDevices

Get
                                             					 configuration of an extension

ISgetSipExtension

Any
                                             					 combination of the following:

ISVoiceRegDNID

ISVoiceRegNumber

ISKeyword:

all

allTag

available

ISSipExtensions

Get
                                             					 status of a session server

ISgetSessionServer

Any
                                             					 combination of the following:

ISSessionServerID

ISSessionServerName

ISKeyword:

all

allTag

available

ISSessionServers

Get
                                             					 status of voice hunt groups

ISgetVoiceHuntGroup

ISVoiceHuntGroupID

ISKeyword:

all

allTag

available

ISVoiceHuntGroups

Get
                                             					 configuration for Presence

ISgetPresenceGlobal

—

ISPresenceGlobal

### Examples for XML
                           	 API Methods

This section
                                 		  contains examples for the following XML API methods:

System

ISexecCLI

ISSaveConfig

SCCP IP Phones

SIP IP
                                    			 Phones

#### ISexecCLI

Use ISexecCLI to execute a list of Cisco IOS commands on the Cisco
                                    		  router. The request must include the CLI parameter with the Cisco IOS command
                                    		  string for each command to be executed.

##### Request

```
<SOAP-ENV:Envelope>
<SOAP-ENV:Body>
<axl>
<request xsi:type="ISexecCLI">
<ISexecCLI>
<CLI>ephone 4</CLI>
<CLI>mac-address 000D.BC80.EB51</CLI>
<CLI>type 7960</CLI>
<CLI>button  1:1</CLI>
</ISexecCLI>
</request>
</axl>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

##### Response

The value of “0” for ISexecCLIResponse in the following example is the
                                    		  response when the request is completed successfully.

```
<SOAP-ENV:Envelope >
<SOAP-ENV:Body>
<axl >
<response xsi:type="ISexecCLIResponse" >
<ISexecCLIResponse>0</ISexecCLIResponse>
<ISexecCLIError></ISexecCLIError>
</response>
</axl>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

The following example shows the response when the request fails. The
                                    		  value of ISexecCLIResponse identifies which line number in the request failed.
                                    		  Any subsequent commands in the list of commands are not executed. All preceding
                                    		  commands in the list were executed.

```
<SOAP-ENV:Envelope >
<SOAP-ENV:Body>
<axl >
<response xsi:type="ISexecCLIResponse" >
<ISexecCLIResponse>4</ISexecCLIResponse>
<ISexecCLIError> invalid input dn parameter for button 1</ISexecCLIError>
</response>
</axl>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

#### ISSaveConfig

Use ISSaveConfig to save the running configuration on a router to the
                                    		  startup configuration on the same router.

##### Request

```
<request>
<ISSaveConfig />
</request>
```

##### Response

The following example shows that the ISSaveConfig request was
                                    		  successfully completed.

```
<response xsi:type=" ISSaveConfig">
<ISSaveConfigResult>success</ISSaveConfigResult>
</request>
```

The following example shows the response when the request fails.

```
<response xsi:type=" ISSaveConfig">
<ISSaveConfigResult>fail</ISSaveConfigResult>
</request>
```

The following example shows that response when the request is delayed,
                                    		  typically because there is another terminal session connected to
                                    		  Cisco Unified CME. The running configuration will be saved later by a
                                    		  background process after all other terminal sessions are disconnected.

```
<response xsi:type=" ISSaveConfig">
<ISSaveConfigResult>delay</ISSaveConfigResult>
</request>
```

#### ISgetGlobal

Use ISgetGlobal to
                                    		  retrieve system configuration and status information for the Cisco Unified CME
                                    		  system.

##### Request

```
<request xsi:type=”ISgetGlobal”>
<ISgetGlobal></ISgetGlobal>
</request>
```

##### Response

```
<response>
<ISGlobal>
<ISAddress>10.4.188.90</ISAddress> 
<ISMode>ITS</ISMode> 
<ISVersion>7.2</ISVersion> 
<ISDeviceRegistered>0</ISDeviceRegistered> 
<ISPeakDeviceRegistered>1</ISPeakDeviceRegistered> 
<ISPeakDeviceRegisteredTime>9470</ISPeakDeviceRegisteredTime> 
<ISKeepAliveInterval>30</ISKeepAliveInterval> 
<ISConfiguredDevice>32</ISConfiguredDevice> 
<ISConfiguredExtension>74</ISConfiguredExtension> 
<ISServiceEngine>0.0.0.0</ISServiceEngine> 
<ISName>ngm-2800</ISName> 
<ISPortNumber>2000</ISPortNumber> 
<ISMaxConference>8</ISMaxConference>
<ISMaxRedirect>10</ISMaxRedirect> 
<ISMaxEphone>48</ISMaxEphone>
<ISMaxDN>180</ISMaxDN>
<ISVoiceMail>6050</ISVoiceMail> 
<ISUrlServices>
<ISUrlService>
<ISUrlType>EPHONE_URL_INFO</ISUrlType> 
<ISUrlLink>http://1.4.188.101/localdir</ISUrlLink> 
</ISUrlService>
<ISUrlService>
<ISUrlType>EPHONE_URL_DIRECTOREIES</ISUrlType> 
<ISUrlLink>http://1.4.188.101/localdir</ISUrlLink> 
</ISUrlService>
<ISUrlService>
<ISUrlType>EPHONE_URL_MESSAGES</ISUrlType> 
<ISUrlLink>http://1.4.188.101/localdir</ISUrlLink>
</ISUrlService>
<ISUrlService>
<ISUrlType>EPHONE_URL_SERVICES</ISUrlType> 
<ISUrlLink>http://1.4.188.101/localdir</ISUrlLink> 
</ISUrlService>
<ISUrlService>
<ISUrlType>EPHONE_URL_PROXYSERV</ISUrlType> 
<ISUrlLink>http://1.4.188.101/localdir</ISUrlLink> 
</ISUrlService>
<ISUrlService>
<ISUrlType>EPHONE_URL_IDLE</ISUrlType> 
<ISUrlLink>ttp://1.4.188.101/localdir</ISUrlLink> 
</ISUrlService>
<ISUrlService>
<ISUrlType>EPHONE_URL_AUTH</ISUrlType> 
<ISUrlLink>http://1.4.188.101/localdir</ISUrlLink> 
</ISUrlService>
</ISUrlServices>
<global-after-hours>
<block_list>
<block_item>
<pattern_id>1</pattern_id> 
<blocking_pattern>1234</blocking_pattern> 
<blocking_option /> 
</block_item>
<block_item>
<pattern_id>2</pattern_id> 
<blocking_pattern>2345</blocking_pattern> 
<blocking_option>7-24</blocking_option> 
</block_item>
</block_list>
<date_list>
<date_item>
<month>Nov</month> 
<day_of_month>12</day_of_month> 
<start_time>12:00</start_time> 
<stop_time>13:00</stop_time> 
</date_item>
</date_list>
<day_list>
<day_item>
<day_of_week>Mon</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>13:00</stop_time> 
</day_item>
</day_list>
<after-hours_login>
<http>true</http> 
</after-hours_login>
<override-code>2222</override-code> 
<pstn-prefix_list>
<pstn-prefix_item>
<index>1</index> 
<pstn-prefix>22</pstn-prefix> 
</pstn-prefix_item>
</pstn-prefix_list>
</global-after-hours>
<application_name>calling</application_name> 
<auth_credential_list>
<credential_item>
<index>1</index> 
<user>test</user> 
<password>test</password> 
</credential_item>
</auth_credential_list>
<auto>
<assign_list>
<assign_item>
<group_id>1</group_id> 
<start_tag>70</start_tag> 
<stop_tag>93</stop_tag> 
<type>anl</type> 
<cfw /> 
<timeout>0</timeout> 
</assign_item>
<assign_item>
<group_id>2</group_id>
<start_tag>1</start_tag> 
<stop_tag>20</stop_tag> 
<cfw>1234</cfw> 
<timeout>80</timeout> 
</assign_item>
</assign_list>
</auto>
<auto-reg-ephone>true</auto-reg-ephone> 
<bulk-speed-dial_list>
<bulk-speed-dial_item>
<list>1</list> 
<url /> 
</bulk-speed-dial_item>
</bulk-speed-dial_list>
<prefix>123<prefix> 
<global-call-forward>
<pattern_list>
<pattern_item>
<index>2</index> 
<pattern>.T</pattern> 
</pattern_item>
</pattern_list>
<callfwd_system>
<redirecting-expanded>false</redirecting-expanded> 
</callfwd_system>
</global-call-forward>
<call-park>
<select>
<no-auto-match>true</no-auto-match> 
</select>
<application_system>true</application_system> 
<redirect_system>true</redirect_system> 
</call-park>
<caller-id>
<block_code>*1</block_code> 
<name-only>true</name-only> 
</caller-id>
<calling-number>
<initiator>true</initiator> 
<local>false</local> 
<secondary>false</secondary> 
</calling-number>
<cnf-file>
<location>
<TFTP>flash:/its/</TFTP> 
<flash>true</flash> 
</location>
<option>perphonetype</option> 
</cnf-file>
<default_codec>Unknown</default_codec> 
<conference>
<hardware>true</hardware> 
</conference>
<date-format>mm-dd-yy</date-format> 
<device-security-mode>none</device-security-mode> 
<dialplan-pattern_list>
<dialplan-pattern_item>
<index>1</index> 
<pattern>1234</pattern> 
<extension-length>4</extension-length> 
<extension-pattern /> 
<demote>false</demote> 
<no-reg>false</no-reg> 
</dialplan-pattern_item>
<dialplan-pattern_item>
<index>2</index> 
<pattern>1233</pattern> 
<extension-length>4</extension-length> 
<extension-pattern /> 
<demote>true</demote> 
<no-reg>false</no-reg> 
</dialplan-pattern_item>
<dialplan-pattern_item>
<index>3</index> 
<pattern>1232</pattern> 
<extension-length>4</extension-length> 
<extension-pattern>1111</extension-pattern> 
<demote>false</demote> 
<no-reg>false</no-reg> 
</dialplan-pattern_item>
<dialplan-pattern_item>
<index>4</index> 
<pattern>1231</pattern> 
<extension-length>4</extension-length> 
<extension-pattern /> 
<demote>false</demote> 
<no-reg>true</no-reg> 
</dialplan-pattern_item>
</dialplan-pattern_list>
<directory>
<entry_list>
<entry_item>
<tag>1</tag> 
<number>1234</number> 
<name>directory</name> 
</entry_item>
</entry_list>
<option>last-name-first</option> 
</directory>
<dn-webedit>false</dn-webedit> 
<em>
<external>true</external> 
<keep-history>true</keep-history> 
<logout>12:00 00:-1 -1:-1</logout> 
</em>
<ephone-reg>true</ephone-reg> 
<extension-assigner>
<tag-type>provision-tag</tag-type> 
</extension-assigner>
<fac>
<standard>true</standard> 
<custom_list>
<custom_item>
<fac_string>callfwd all</fac_string> 
<fac_list>**1</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>callfwd cancel</fac_string> 
<fac_list>**2</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>pickup local</fac_string> 
<fac_list>**3</fac_list> 
<alias>0</alias> 
<alias_map />
</custom_item>
<custom_item>
<fac_string>pickup group</fac_string> 
<fac_list>**4</fac_list> 
<alias>0</alias>
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>pickup direct</fac_string> 
<fac_list>**5</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>park</fac_string> 
<fac_list>**6</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>dnd</fac_string> 
<fac_list>**7</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>redial</fac_string> 
<fac_list>**8</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>voicemail</fac_string> 
<fac_list>**9</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>ephone-hunt join</fac_string> 
<fac_list>*3</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>ephone-hunt cancel</fac_string> 
<fac_list>#3</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>ephone-hunt hlog</fac_string> 
<fac_list>*4</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>ephone-hunt hlog-phone</fac_string> 
<fac_list>*5</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>trnsfvm</fac_string> 
<fac_list>*6</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>dpark-retrieval</fac_string>
<fac_list>*0</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
<custom_item>
<fac_string>cancel call waiting</fac_string> 
<fac_list>*1</fac_list> 
<alias>0</alias> 
<alias_map /> 
</custom_item>
</custom_list>
</fac>
<fxo>
<hook-flash>true</hook-flash> 
</fxo>
<hunt-group>
<logout>HLog</logout> 
<report>
<url_info>
<prefix>tftp://223.255.254.253/ngm/huntgp/2800/data</prefix> 
<hg_suffix>
<low>-1</low> 
<high>0</high> 
</hg_suffix>
</url_info>
<delay>0</delay> 
<duration>24</duration> 
<internal>
<duration>5</duration>
<hg_suffix>
<low>1</low>
<high>5</high> 
</hg_suffix>
</internal>
</report>
</hunt-group>
<internal-call>
<moh-group>-1</moh-group> 
</internal-call>
<ip>
<qos>
<dscp_list>
<dscp_item>
<index>0</index> 
<af11>media</af11> 
</dscp_item>
<dscp_item>
<index>1</index> 
<af12>signal</af12> 
</dscp_item>
<dscp_item>
<index>2</index> 
<af13>video</af13> 
</dscp_item>
<dscp_item>
<index>3</index> 
<af21>service</af21> 
</dscp_item>
<dscp_item>
<index>4</index> 
<af22>media</af22> 
</dscp_item>
<dscp_item>
<index>5</index> 
<af23>media</af23>
</dscp_item>
<dscp_item>
<index>6</index>
<af31>media</af31> 
</dscp_item>
<dscp_item>
<index>7</index> 
<af32>media</af32> 
</dscp_item>
<dscp_item>
<index>8</index> 
<af33>media</af33> 
</dscp_item>
<dscp_item>
<index>9</index> 
<af41>media</af41> 
</dscp_item>
<dscp_item>
<index>10</index> 
<af42>media</af42> 
</dscp_item>
<dscp_item>
<index>11</index> 
<af43>media</af43>
</dscp_item>
<dscp_item>
<index>12</index> 
<cs1>media</cs1> 
</dscp_item>
<dscp_item>
<index>13</index> 
<cs2>media</cs2> 
</dscp_item>
<dscp_item>
<index>14</index> 
<cs3>media</cs3> 
</dscp_item>
<dscp_item>
<index>15</index> 
<cs4>media</cs4> 
</dscp_item>
<dscp_item>
<index>16</index> 
<cs5>media</cs5> 
</dscp_item>
<dscp_item>
<index>17</index> 
<cs6>media</cs6> 
</dscp_item>
<dscp_item>
<index>18</index> 
<cs7>media</cs7> 
</dscp_item>
<dscp_item>
<index>19</index> 
<default>media</default> 
</dscp_item>
<dscp_item>
<index>20</index> 
<ef>media</ef> 
</dscp_item>
</dscp_list>
</qos>
<source-address>
<primary>10.4.188.90</primary> 
<port>2000</port> 
<secondary>1.4.188.90</secondary> 
<rehome>0</rehome> 
<strict-match>true</strict-match> 
</source-address>
</ip>
<keepalive>
<timeout>30</timeout> 
<aux_timeout>30</aux_timeout> 
</keepalive>
<live-record>999</live-record> 
<load_list>
<phone_7914>hehe</phone_7914> 
<phone_7915-12>hehe</phone_7915-12> 
<phone_7915-24>hehe</phone_7915-24> 
<phone_7916-12>hehe</phone_7916-12> 
<phone_7916-24>hehe</phone_7916-24> 
<phone_12SP>hehe</phone_12SP> 
<phone_7902>hehe</phone_7902> 
<phone_7906>hehe</phone_7906> 
<phone_7910>hehe</phone_7910> 
<phone_7911>SCCP11.9-0-1FT6-4DEV</phone_7911> 
<phone_7912>hehe</phone_7912> 
<phone_7920>hehe</phone_7920>
<phone_7921>hehe</phone_7921> 
<phone_7925>hehe</phone_7925> 
<phone_7931>hehe</phone_7931> 
<phone_7935>hehe</phone_7935> 
<phone_7936>hehe</phone_7936> 
<phone_7937>hehe</phone_7937> 
<phone_7960-7940>P00308000501</phone_7960-7940> 
<phone_7941>hehe</phone_7941> 
<phone_7941GE>hehe</phone_7941GE> 
<phone_7942>hehe</phone_7942> 
<phone_7961>SCCP41.8-4-2-38S</phone_7961> 
<phone_7962>hehe</phone_7962> 
<phone_7965>hehe</phone_7965> 
<phone_7970>hehe</phone_7970> 
<phone_7971>hehe</phone_7971> 
<phone_7975>hehe</phone_7975> 
<phone_7985>hehe</phone_7985> 
<phone_ata>hehe</phone_ata> 
<phone_6921>hehe</phone_6921> 
<phone_6941>hehe</phone_6941> 
<phone_6961>hehe</phone_6961> 
</load_list>
<load-cfg-file_list>
<load-cfg-file_item>
<cfg_file>flash:its/vrf1/XMLDefaultCIPC.cnf.xml</cfg_file> 
<alias>cnf.xml</alias> 
<sign>false</sign> 
</load-cfg-file_item>
</load-cfg-file_list>
<log>
<table >
<max-size>150</max-size> 
<retain-timer>15</retain-timer> 
</table>
</log>
<login>
<timeout>60</timeout> 
<clear>24:0</clear> 
</login>
<max-conferences>
<count>8</count>
<gain>-6</gain> 
</max-conferences>
<max-dn>
<count>180</count> 
<global_preference>0</global_preference> 
<no-reg>secondary</no-reg> 
</max-dn>
<max-ephones>48</max-ephones> 
<max-redirect>10</max-redirect> 
<modem>
<passthrough>
<payload-type>100</payload-type> 
</passthrough>
<relay_sse>
<payload-type>118</payload-type> 
</relay_sse>
<relay_sprt>
<payload-type>120</payload-type> 
</relay_sprt>
</modem>
<moh_file>flash:music-on-hold.au</moh_file> 
<moh-file-buffer>10000</moh-file-buffer> 
<multicast>
<moh_ipaddr>239.10.10.10</moh_ipaddr> 
<port>2000</port> 
<route_list>
<route_item>
<index>1</index> 
<route>10.10.10.10</route> 
</route_item>
</route_list>
</multicast>
<mwi-server>
<prefix /> 
<reg-e164>true</reg-e164> 
<relay>true</relay> 
</mwi-server>
<network-locale_list>
<network-locale_item>
<index>0</index> 
<locale>US</locale> 
</network-locale_item>
<network-locale_item>
<index>1</index> 
<locale>US</locale> 
</network-locale_item>
<network-locale_item>
<index>2</index> 
<locale>US</locale> 
</network-locale_item>
<network-locale_item>
<index>3</index> 
<locale>US</locale> 
</network-locale_item>
<network-locale_item>
<index>4</index>
<locale>US</locale> 
</network-locale_item>
</network-locale_list>
<night-service>
<option>everyday</option> 
<code>*234</code> 
<date_list>
<date_item>
<index>1</index>
<month>Jan</month> 
<day_of_month>1</day_of_month> 
<start_time>12:00</start_time> 
<stop_time>14:00</stop_time> 
</date_item>
</date_list>
<day_list>
<day_item>
<index>1</index> 
<day_of_week>Sun</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</day_item>
<day_item>
<index>2</index> 
<day_of_week>Mon</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</day_item>
<day_item>
<index>3</index> 
<day_of_week>Tue</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</day_item>
<day_item>
<index>4</index> 
<day_of_week>Wed</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</day_item>
<day_item>
<index>5</index> 
<day_of_week>Thu</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</day_item>
<day_item>
<index>6</index> 
<day_of_week>Fri</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</day_item>
<day_item>
<index>7</index> 
<day_of_week>Sat</day_of_week> 
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</day_item>
</day_list>
<everyday>
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time> 
</everyday>
<weekday>
<start_time>12:00</start_time>
<stop_time>16:00</stop_time> 
</weekday>
<weekend>
<start_time>12:00</start_time> 
<stop_time>16:00</stop_time>
</weekend>
</night-service>
<pin>1234</pin> 
<pin_override>true</pin_override> 
<privacy>true</privacy> 
<privacy-on-hold>false</privacy-on-hold> 
<protocol>
<mode>dual-stack</mode> 
<preference>ipv4</preference> 
</protocol>
<sdspfarm>
<conference_options>
<mute-on>124</mute-on> 
<mute-off>234</mute-off> 
<hardware>false</hardware> 
</conference_options>
<units>4</units> 
<tag_list>
<tag_item>
<tag>1</tag> 
<device>mtp-conf</device> 
</tag_item>
</tag_list>
<transcode>
<sessions>4</sessions> 
</transcode>
<unregister>
<force>1</force>
</unregister>
</sdspfarm>
<secondary-dialtone>4567</secondary-dialtone> 
<secure-signaling>
<trustpoint /> 
</secure-signaling>
<server-security-mode /> 
<service>
<local-directory>true</local-directory> 
<local-directory_authenticate>false</local-directory_authenticate> 
<dss>false</dss> 
<dnis>
<overlay>false</overlay> 
<dir-lookup>false</dir-lookup> 
</dnis>
<directed-pickup>true</directed-pickup> 
<directed-pickup_gpickup>false</directed-pickup_gpickup> 
<phone_list>
<phone_item>
<index>1</index> 
<phone_params>displayOnTime</phone_params> 
<phone_text>time.xml</phone_text> 
</phone_item>
</phone_list>
</service>
<ssh>
<userid>ngm</userid> 
<password>ngm</password> 
</ssh>
<standby>
<user>ngm</user> 
<password>ngm</password>
</standby>
<system_message>LITTLE TWIN STARS (2800)</system_message> 
<tftp-server-credentials>
<trustpoint /> 
</tftp-server-credentials>
<time-format>12</time-format> 
<time-webedit>false</time-webedit> 
<time-zone>0</time-zone> 
<timeouts>
<busy_timeout>10</busy_timeout>
<interdigit_timeout>10</interdigit_timeout>
<ringing_timeout>180</ringing_timeout> 
<transfer-recall_timeout>0</transfer-recall_timeout> 
<night-service-bell_timeout>12</night-service-bell_timeout> 
</timeouts>
<transfer-digit-collect>new-call</transfer-digit-collect> 
<transfer-pattern_list>
<transfer-pattern_item>
<index>1</index> 
<pattern>....</pattern> 
<blind>false</blind> 
</transfer-pattern_item>
<transfer-pattern_item>
<index>2</index> 
<pattern>.T</pattern> 
<blind>false</blind> 
</transfer-pattern_item>
</transfer-pattern_list>
<transfer-system>
<type>full-consult</type> 
<dss>false</dss> 
</transfer-system>
<trunk_optimization_pre_connect>false</trunk_optimization_pre_connect> 
<url_list>
<information>
<url>http://1.4.188.101/localdir</url> 
</information>
<directories>
<url>http://1.4.188.101/localdir</url> 
</directories>
<messages>
<url>http://1.4.188.101/localdir</url> 
</messages>
<services>
<url>http://1.4.188.101/localdir</url> 
<name /> 
</services>
<proxy_server>
<url>http://1.4.188.101/localdir</url> 
</proxy_server>
<idle>
<url>http://1.4.188.101/localdir</url> 
<idle_timeout>90</idle_timeout> 
</idle>
<authentication>
<url>http://1.4.188.101/localdir</url> 
<user /> 
<password /> 
</authentication>
</url_list>
<user-locale_list>
<user-locale_item>
<index>0</index> 
<locale>US</locale> 
<package>en</package> 
<load > 
</user-locale_item>
<user-locale_item>
<index>1</index> 
<locale>US</locale> 
<package>en</package> 
<load /> 
</user-locale_item>
<user-locale_item>
<index>2</index> 
<locale>US</locale> 
<package>en</package> 
<load /> 
</user-locale_item>
<user-locale_item>
<index>3</index> 
<locale>US</locale> 
<package>en</package>
<load /> 
</user-locale_item>
<user-locale_item>
<index>4</index> 
<locale>US</locale> 
<package>en</package> 
<load /> 
</user-locale_item>
</user-locale_list>
<video>
<maximum>
<bit-rate>10000000</bit-rate> 
</maximum>
</video>
<voicemail>6050</voicemail> 
<web>
<system_admin>
<name>Admin</name> 
<secret>-1</secret> 
<password /> 
</system_admin>
<customer_admin>
<name>ngm</name> 
<secret>5</secret> 
<password>$1$.nfD$zn3h3bp/4grULFS87ZHHV/</password> 
</customer_admin>
<customize>
<load /> 
</customize>
</web>
<xml>
<user>cisco</user> 
<password>cisco</password>
<level>0</level>
</xml>
</ISGlobal>
</response>
```

#### ISgetDevice

Use ISgetDevice to retrieve configuration and status information for
                                    		  IP phones.

Use any combination of the following parameters in the request message
                                    		  to specific one or more SCCP phones:

ISDevID with the ephone tag number of SCCP phone to be queried.

ISDevName with the MAC address of SCCP phone to be queried.

ISKeyword with one of the following options:

all—All configured SCCP phones

allTag—Ephone tag numbers for all SCCP phones configured

available—Next available ephone tag number to be configured

##### Request:

```
<request xsi:type="ISgetDevice">
<ISgetDevice>
<ISDevID>1</ISDevID>
<ISDevName>SEP0012DA8AC43D</ISDevName>
<ISDevName>allKeyphone</ISDevName>
</ISgetDevice>
</request>
```

##### Response

```
<response>
<ISDevices>
<ISDevice>
<ISDevID>1</ISDevID> 
<ISDevName>SEP0016C7C7AF9D</ISDevName> 
<ISDevType>Others</ISDevType> 
<ISconfigDevType>7911</ISconfigDevType> 
<ISDevUsername>test</ISDevUsername> 
<ISDevLineButtons>
<ISDevLineButton>
<ISDevLineButtonID>1</ISDevLineButtonID> 
<ISDevLineButtonMode>MONITOR_RING</ISDevLineButtonMode> 
</ISDevLineButton>
</ISDevLineButtons>
<after-hours_exempt>false</after-hours_exempt> 
<after-hours_login>
<http>false</http> 
</after-hours_login>
<block-blind-xf-fallback>false</block-blind-xf-fallback>
<capf-ip-in-cnf>false</capf-ip-in-cnf> 
<codec>
<codec_name>g711ulaw</codec_name> 
<dspfarm-assist>false</dspfarm-assist> 
</codec>
<adhoc_conference>
<add-mode>
<creator>true</creator> 
</add-mode>
<admin>true</admin> 
<drop-mode>
<creator>false</creator> 
<local>false</local> 
</drop-mode>
</adhoc_conference>
<fastdial_list>
<fastdial_item>
<fastdial>1</fastdial> 
<fastdial_number>1234</fastdial_number>
<fastdial_name>home LINE</fastdial_name> 
</fastdial_item>
</fastdial_list>
<feature-button_list>
<feature-button_item>
<feature-button>1</feature-button> 
<feature_type>Dnd</feature_type> 
</feature-button_item>
<feature-button_item>
<feature-button>2</feature-button> 
<feature_type>Flash</feature_type> 
</feature-button_item>
</feature-button_list>
<keep-conference>
<hangup>true</hangup> 
<drop-last>false</drop-last> 
<endcall>true</endcall> 
<local-only>true</local-only> 
</keep-conference>
<keypad-normalize>false</keypad-normalize>
<keyphone>false</keyphone> 
<mtp>true</mtp> 
<multicast-moh>true</multicast-moh> 
<night-service_bell>true</night-service_bell> 
<privacy /> 
<privacy-button>false</privacy-button> 
<transfer-park>
<blocked>false</blocked> 
</transfer-park>
<transfer-pattern>
<blocked>false</blocked>
</transfer-pattern>
<busy-trigger-per-button>0</busy-trigger-per-button> 
<emergency-resp_location>0</emergency-resp_location> 
<max-calls-per-button>0</max-calls-per-button> 
<nte-end-digit-delay>0</nte-end-digit-delay> 
<keepalive>
<timeout>30</timeout>
<aux_timeout>30</aux_timeout> 
</keepalive>
<lpcor>
<type>none</type> 
</lpcor>
<exclude-services>
<em_service>true</em_service> 
<directory_service>false</directory_service> 
<myphoneapp_service>false</myphoneapp_service> 
</exclude-services>
<park>
<reservation-group>park</reservation-group>
</park>
<paging-dn>
<dn>0</dn> 
<mode>multicast</mode>
</paging-dn>
<speed-dial_list>
<speed-dial_item>
<index>1</index> 
<phone_number>1234</phone_number> 
<label>home</label> 
</speed-dial_item>
</speed-dial_list>
<ssh>
<userid>ngm</userid> 
<password>ngm</password> 
</ssh>
<phone_type>
<name>7911</name> 
<addon_list>
<addon_item>
<addon>1</addon> 
<addon_type>7914</addon_type> 
</addon_item>
</addon_list>
</phone_type>
<auto-line>
<mode>normal</mode> 
<auto_select_line>0</auto_select_line> 
</auto-line>
<blf-speed-dial_list>
<blf-speed-dial_item>
<index>1</index> 
<phone_number>1234</phone_number> 
<label>blfsd</label> 
</blf-speed-dial_item>
<device>true</device> 
</blf-speed-dial_list>
<bulk-speed-dial_list>
<bulk-speed-dial_item>
<list>1</list> 
<url />
</bulk-speed-dial_item>
</bulk-speed-dial_list>
<capf-auth-str>7777</capf-auth-str> 
<description>ephoneOne</description> 
<device-security-mode>none</device-security-mode> 
<dnd>
<feature-ring>true</feature-ring> 
</dnd>
<ephone-template>1</ephone-template> 
<headset>
<auto-answer>
<line_list>
<line>1</line> 
</line_list>
</auto-answer>
</headset>
<logout-profile>0</logout-profile> 
<display_all_missed_calls>true</display_all_missed_calls> 
<mwi-line>1</mwi-line> 
<offhook-guard-timer>0</offhook-guard-timer> 
<phone-ui>
<snr>true</snr> 
<speeddial-fastdial>true</speeddial-fastdial> 
</phone-ui>
<pin>1234</pin> 
<presence>
<call-list>true</call-list> 
</presence>
<provision-tag>1</provision-tag> 
<username>test</username> 
<password>test</password> 
<video_enable>true</video_enable> 
<vm-device-id>SEP0016C7C7AF9D</vm-device-id> 
<ISDevAddr>
<Xipv4Address>0.0.0.0</Xipv4Address> 
</ISDevAddr>
<ISPhoneLineList>
<ExtMapStatus>
<LineId>1</LineId> 
<ExtId>176</ExtId> 
<ExtNumber>6176</ExtNumber> 
<ExtStatus>false</ExtStatus> 
<LineState>idle</LineState> 
</ExtMapStatus>
</ISPhoneLineList>
<ISKeyPhone>false</ISKeyPhone> 
<SNRui>true</SNRui> 
<ISLogoutProfileID>0</ISLogoutProfileID> 
<ISUserProfileID>0</ISUserProfileID> 
<ISTapiClientAddr>
<Xipv4Address /> 
</ISTapiClientAddr>
<ISDevStatus>unregistered</ISDevStatus> 
<ISDevLastStatus>deceased</ISDevLastStatus> 
<ISDevChangeTime>4040</ISDevChangeTime> 
<ISDevKeepAlives>0</ISDevKeepAlives> 
<ISDevTapiCStatus /> 
<ISTapiCLastStatus /> 
<ISTapiCChangeTime /> 
<ISTapiCKeepAlive /> 
<ISDevDND>no</ISDevDND> 
</ISDevice>
</ISDevices>
</response>
```

#### ISgetDeviceTemplate

Use ISgetDeviceTemplate to retrieve configuration and status
                                    		  information for IP phone templates.

Use any combination of the following parameters in the request message
                                    		  to specify one or more phone templates:

ISDevTemplateID with phone template tag number to be queried.

ISKeyword with one of the following options:

all—All configured phone templates

allTag—Phone template tag numbers for all configured phone
                                                					 templates

available—Next available phone template tag number to be
                                                					 configured

##### Request

```
<request>
<ISgetDeviceTemplate>
<ISgetDevTemplateID>1</ISgetDevTemplateID> 
<ISgetDeviceTemplate>
</request>
```

##### Response

```
<response>
<ISDeviceTemplates>
<ISDeviceTemplate>
<ISDevTemplateID>1<ISDevTemplateID> 
<after-hours>
<block_list>
<block_item>
<pattern_id>1<pattern_id> 
<blocking_pattern>1234<blocking_pattern> 
<blocking_option>7-24<blocking_option> 
<block_item>
<block_list>
<date_list>
<date_item>
<month>Jan<month> 
<day_of_month>1<day_of_month> 
<start_time>12:00<start_time> 
<stop_time>14:00<stop_time> 
<date_item>
<date_list>
<day_list>
<day_item>
<day_of_week>Mon<day_of_week> 
<start_time>12:00<start_time> 
<stop_time>14:00<stop_time> 
<day_item>
<day_list>
<exempt>true<exempt> 
<after-hours_login>
<http>true<http> 
<after-hours_login>
<override-code>1234<override-code> 
<after-hours>
<block-blind-xf-fallback>false<block-blind-xf-fallback> 
<button-layout_phone_7931>0<button-layout_phone_7931> 
<button-layout_list>
<button-layout_item>
<button-layout>1,9<button-layout> 
<button-type>line<button-type> 
<button-layout_item>
<button-layout_item>
<button-layout>4-5,7<button-layout> 
<button-type>speed-dial<button-type> 
<button-layout_item>
<button-layout_item>
<button-layout>2-3<button-layout> 
<button-type>feature<button-type> 
<button-layout_item>
<button-layout_item>
<button-layout>11<button-layout> 
<button-type>url<button-type> 
<button-layout_item>
<button-layout_list>
<capf-ip-in-cnf>false<capf-ip-in-cnf> 
<codec>
<codec_name>g711ulaw<codec_name> 
<dspfarm-assist>false<dspfarm-assist> 
<codec>
<adhoc_conference>
<add-mode>
<creator>false<creator> 
<add-mode>
<admin>false<admin> 
<drop-mode>
<creator>false<creator> 
<local>false<local> 
<drop-mode>
<adhoc_conference>
<fastdial_list>
<fastdial_item>
<fastdial>1<fastdial> 
<fastdial_number>1234<fastdial_number> 
<fastdial_name>office<fastdial_name> 
<fastdial_item>
<fastdial_list>
<feature-button_list>
<feature-button_item>
<feature-button>1<feature-button> 
<feature_type>HLog<feature_type> 
<feature-button_item>
<feature-button_item>
<feature-button>2<feature-button> 
<feature_type>Park<feature_type> 
<feature-button_item>
<feature-button_item>
<feature-button>3<feature-button> 
<feature_type>Privacy<feature_type> 
<feature-button_item>
<feature-button_list>
<url-button_list>
<url-button_item>
<url-button>1<url-button> 
<url-button_type>em<url-button_type> 
<url-button_item>
<url-button_item>
<url-button>3<url-button> 
<url-button_type>myphoneapp<url-button_type> 
<url-button_item>
<url-button_item>
<url-button>6<url-button> 
<url-button_type>service<url-button_type> 
<url-button_url>hello<url-button_url> 
<url-button_name>helloworld<url-button_name> 
<url-button_item>
<url-button_list>
<features_blocked>Pickup Park GPickup<features_blocked> 
<keep-conference>
<hangup>false<hangup> 
<drop-last>false<drop-last> 
<endcall>false<endcall> 
<local-only>false<local-only> 
<keep-conference>
<keypad-normalize>false<keypad-normalize> 
<keyphone>false<keyphone> 
<mlpp>
<indication>true<indication> 
<preemption>true<preemption> 
<max_priority>-1<max_priority> 
<mlpp>
<mtp>false<mtp> 
<multicast-moh>true<multicast-moh> 
<night-service_bell>false<night-service_bell> 
<privacy > 
<privacy-button>false<privacy-button> 
<phone_service>
<param_list>
<param_item>
<param>displayOnTime<param> 
<text>170<text> 
<param_item>
<param_list>
<phone_service>
<softkeys>
<alerting_keys > 
<connected_keys > 
<hold_keys > 
<idle_keys > 
<remote-in-use_keys>CBarge Newcall<remote-in-use_keys> 
<ringing_keys > 
<seized_keys > 
<softkeys>
<transfer-park>
<blocked>false<blocked> 
<transfer-park>
<transfer-pattern>
<blocked>false<blocked> 
<transfer-pattern>
<busy-trigger-per-button>0<busy-trigger-per-button> 
<emergency-resp_location>0<emergency-resp_location> 
<max-calls-per-button>0<max-calls-per-button> 
<network_locale>0<network_locale>
<nte-end-digit-delay>0<nte-end-digit-delay> 
<transfer_max-length>0<transfer_max-length> 
<user_locale>0<user_locale> 
<keepalive>
<timeout>30<timeout> 
<aux_timeout>30<aux_timeout> 
<keepalive>
<lpcor>
<type>none<type> 
<lpcor>
<exclude-services>
<em_service>false<em_service> 
<directory_service>true<directory_service> 
<myphoneapp_service>true<myphoneapp_service> 
<exclude-services>
<park>
<reservation-group>1234<reservation-group> 
<park>
<paging-dn>
<dn>0<dn> 
<mode>multicast<mode> 
<paging-dn>
<speed-dial_list>
<speed-dial_item>
<index>1<index> 
<phone_number>1234<phone_number> 
<label>play<label> 
<speed-dial_item>
<speed-dial_list>
<ssh>
<userid>test<userid> 
<password>test<password> 
<ssh>
<phone_type>
<name>7960<name> 
<addon_list>
<addon_item>
<addon>1<addon> 
<addon_type>7914<addon_type> 
<addon_item>
<addon_list>
<phone_type>
<url_services_list>
<url_services_item>
<services_id>1<services_id> 
<url>http<url> 
<name>HTTP<name> 
<url_services_item>
<url_services_list>
<ISDeviceTemplate>
<ISDeviceTemplates>
<response>
```

#### ISgetExtension

Use ISgetExtension to retrieve configuration and status information
                                    		  for extension numbers.

Use any combination of the following parameters in the request message
                                    		  to specify one or more extensions:

ISExtID with the extension ID number to be queried.

ISExtNumber with the extension number to be queried.

ISKeyword with one of the following options:

all—Displays details of all extension numbers configured

allTag—Displays a list of all extension ID numbers configured

available—Next available extension ID number to be configured

##### Request

```
<request>
<ISExtension>
<ISVExtID>1</ISExtID> 
<ISExtNumber>1</ISExtNumber>
</ISExtension>
</request>
```

##### Response

```
<response>
<ISExtensions>
<ISExtension>
<ISExtID>1</ISExtID> 
<ISExtNumber>6001</ISExtNumber> 
<ISExtSecNumber>6111</ISExtSecNumber> 
<ISExtType>normal</ISExtType> 
<ISExtStatus>up</ISExtStatus> 
<ISExtChangeTime>3122733</ISExtChangeTime> 
<ISExtUsage>0</ISExtUsage> 
<ISExtHomeAddress>0.0.0.0</ISExtHomeAddress> 
<ISExtMultiLines>0</ISExtMultiLines> 
<ISExtPortName>EFXS 50/0/1</ISExtPortName> 
<ISExtLineMode>DUAL_LINE</ISExtLineMode> 
<ISExtCallStatus>IDLE</ISExtCallStatus> 
<Mobility>false</Mobility> 
<SNRnumber>1111</SNRnumber> 
<SNRdelay>10</SNRdelay> 
<SNRtimeout>5</SNRtimeout> 
<SNRnoanNumber /> 
<ISAllowWatch>true</ISAllowWatch> 
<ISSessionServerIDs>
<ISSessionServerID>1</ISSessionServerID> 
</ISSessionServerIDs>
<firstName /> 
<lastName>ephoneDnOne</lastName> 
<callForwardAll>1234</callForwardAll> 
<ISDevList>
<ISDeviceID>8</ISDeviceID> 
</ISDevList>
<allow>
<watch>true</watch> 
</allow>
<call-forward>
<all>
<number>1234</number> 
</all>
<busy>
<number>9000</number> 
<option>secondary</option> 
<dialplan-pattern>false</dialplan-pattern> 
</busy>
<max-length>
<number /> 
</max-length>
<night-service-activated>
<number>2323</number> 
</night-service-activated>
<noan>
<number>1234</number> 
<timeout>80</timeout> 
<dialplan-pattern>true</dialplan-pattern> 
<option /> 
</noan>
</call-forward>
<call-waiting>
<cw_beep>
<accept>true</accept> 
<generate>true</generate> 
</cw_beep>
<cw_ring>true</cw_ring> 
</call-waiting>
<corlist>
<incoming /> 
<outgoing /> 
</corlist>
<cti>
<notify>true</notify> 
<watch>true</watch> 
</cti>
<description>ephoneDnOne</description> 
<hold-alert>
<timeout>15</timeout> 
<mode>idle</mode> 
<ring-silent-dn>true</ring-silent-dn> 
</hold-alert>
<huntstop>
<channel>8</channel> 
</huntstop>
<moh-group>0</moh-group> 
<mwi>
<type>qsig</type> 
<mode /> 
</mwi>
<mwi-type>both</mwi-type> 
<pickup-group /> 
<transfer-recall_timeout>0</transfer-recall_timeout> 
<translate>
<called>1</called> 
<calling>2</calling> 
</translate>
<translation-profile>
<incoming>in</incoming> 
<outgoing>out</outgoing> 
</translation-profile>
<application>
<name>calling</name> 
<out-bound>calling</out-bound> 
</application>
<port-caller-id>
<block>false</block> 
<local>false</local> 
<transfer_passthrough>false</transfer_passthrough> 
</port-caller-id>
<conference_dn>
<mode /> 
<unlocked>false</unlocked> 
</conference_dn>
<ephone-dn-template>0</ephone-dn-template> 
<ephone-hunt_login>true</ephone-hunt_login> 
<feed>
<ip_addr>0.0.0.0</ip_addr> 
<port>0</port> 
<route>0.0.0.0</route> 
<out-call /> 
</feed>
<fwd-local-calls>true</fwd-local-calls> 
<intercom>
<dn-plar /> 
<barge-in>false</barge-in> 
<label /> 
<no-mute>true</no-mute> 
<ptt>false</ptt> 
<no-auto-answer>true</no-auto-answer> 
</intercom>
<label /> 
<loopback-dn>
<dn>0</dn> 
<auto-con>false</auto-con> 
<loopback-codec /> 
<forward>0</forward> 
<prefix /> 
<retry>0</retry> 
<strip>0</strip> 
<suffix /> 
</loopback-dn>
<mailbox-selection>
<last-redirect-num>false</last-redirect-num> 
</mailbox-selection>
<moh>
<ip_addr>0.0.0.0</ip_addr> 
<port>0</port> 
<route>0.0.0.0</route> 
<out-call /> 
</moh>
<name>ephoneDnOne</name> 
<night-service_bell>false</night-service_bell> 
<telephony_number>
<primary>6001</primary> 
<secondary>6111</secondary> 
<no-reg>true</no-reg> 
<no-reg_option /> 
</telephony_number>
<paging>
<group /> 
<ip_addr>0.0.0.0</ip_addr> 
<port>0</port> 
</paging>
<park-slot>
<directed>false</directed> 
<reserved-for /> 
<reservation-group /> 
<timeout>0</timeout> 
<limit>0</limit> 
<notify /> 
<only>false</only> 
<transfer_destination /> 
<recall>true</recall> 
<alternate /> 
<retry>0</retry> 
<retry_limit>0</retry_limit> 
</park-slot>
<pickup-call>
<any-group>false</any-group> 
</pickup-call>
<dn_preference>
<order>0</order> 
<secondary>9</secondary> 
</dn_preference>
<queueing-dn>
<mode /> 
<timeout>180</timeout> 
<transfer_number /> 
</queueing-dn>
<ring>
<type>external</type> 
<line>primary</line> 
</ring>
<session-server>
<server>1</server> 
</session-server>
<snr_info>
<value>1111</value> 
<delay>10</delay> 
<timeout>5</timeout> 
<cfwd-noan /> 
</snr_info>
<transfer-mode /> 
<trunk>
<number /> 
<timeout>3</timeout> 
<transfer-timeout>0</transfer-timeout> 
<monitor-port /> 
</trunk>
<whisper-intercom>
<speed-dial /> 
<label /> 
</whisper-intercom>
</ISExtension>
</ISExtensions>
</response>
```

#### ISgetExtensionTemplate

Use the ISgetExtensionTemplates to retrieve configuration and status
                                    		  information for extension templates.

Use any combination of the following parameters in the request message
                                    		  to specify one or more extensions:

ISExtTemplateID with the extension template ID number to be
                                          				queried.

ISKeyword with one of the following options:

all—Displays details of all configured extension templates

allTag—Displays a list of all configured extension template ID
                                                					 numbers

available—Next available extension template ID number to be
                                                					 configured

##### Request

```
<request>
<ISExtensionTemplates>
<ISExtensionTemplateID>1</ISExtensionTemplateID>
</ISgetExtensionTemplate>
</request>
```

##### Response

```
<response>
<ISExtensionTemplates>
<ISExtensionTemplate>
<ISExtTemplateID>1</ISExtTemplateID> 
<allow>
<watch>false</watch> 
</allow>
<call-forward>
<all>
<number>1234</number> 
</all>
<busy>
<number>3456</number> 
<option>primary</option> 
<dialplan-pattern>false</dialplan-pattern> 
</busy>
<max-length>
<number>4</number> 
</max-length>
<night-service-activated>
<number>7777</number> 
</night-service-activated>
<noan>
<number>9999</number> 
<timeout>80</timeout> 
<dialplan-pattern>false</dialplan-pattern> 
<option>secondary<option> 
</noan>
</call-forward>
<call-waiting>
<cw_beep>
<accept>true</accept> 
<generate>true</generate> 
</cw_beep>
<cw_ring>true</cw_ring> 
</call-waiting>
<caller-id_blocked>true</caller-id_blocked> 
<corlist>
<incoming /> 
<outgoing /> 
</corlist>
<cti>
<notify>false</notify> 
<watch>false</watch> 
</cti>
<description>ephoneDnTemplate</description> 
</hold-alert>
<timeout>15</timeout> 
<mode>idle</mode> 
<ring-silent-dn>true</ring-silent-dn> 
</hold-alert>
<huntstop>
<channel>8</channel> 
</huntstop>
<moh-group>0</moh-group> 
<mwi>
<type>sip</type> 
<mode>on-off</mode> 
</mwi>
<mwi-type>both</mwi-type> 
<pickup-group>1</pickup-group> 
<transfer-recall_timeout>400</transfer-recall_timeout> 
<translate>
<called>1</called> 
<calling>0</calling> 
</translate>
<translation-profile>
<incoming>1</incoming> 
<outgoing>1</outgoing> 
</translation-profile>
</ISExtensionTemplate>
</ISExtensionTemplates>
</response>
```

#### ISgetUser

Use ISgetUser to retrieve information for a particular user in
                                    		  Cisco Unified CME. The request must include the ISuserID parameter with a user
                                    		  name that is configured in Cisco Unified CME. If the request contains a valid
                                    		  ISuserID, the response includes the user-name tag number (ISuserTag) and type
                                    		  for this user.

The value for ISuserType corresponds to how a username is configured
                                    		  in Cisco Unified CME, as follows:

0—INVALID_CME_USER

1—EPHONE_USER

2—LOGOUT_PROFILE_USER

3—USER_PROFILE_USER

If the request contains an invalid ISuserID, the value for ISuserTag
                                    		  and ISuserType will both be “0.”

##### Request

```
<request>
<ISgetUser>
<ISuserID>a</ISuserID> 
</ISgetUser>
</request>
```

##### Response

```
<response>
<ISuser>
<ISuserID>a</ISuserID> 
<ISuserType>3</ISuserType> 
<ISuserTag>1</ISuserTag> 
</ISuser>
</response>
```

#### ISgetUserProfile

Use the ISgetUserProfile to retrieve the status and configuration
                                    		  information for a specific user profile.

Use any combination of the following:

ISUserProfileID with the user profile ID of a specific user.

ISuserID with user ID of a specific user.

ISKeyword with one of the following options:

all—Displays details of all configured user profiles.

allTag—Displays a list of all configured user profile IDs.

available—Next available user profile.

##### Request

```
<request>
<ISgetUserProfile>
<ISUserProfileID>1</ISUserProfileID> 
</ISgetUserProfile>
</request>
```

##### Response

```
<response>
<ISUserProfiles>
<ISUserProfile>
<ISUserProfileID>1</ISUserProfileID> 
<ISuserID>a</ISuserID> 
<ISpassword>a</ISpassword> 
<ISuserPin>12</ISuserPin> 
<ISPrivacyButton>no</ISPrivacyButton> 
<ISuserMaxIdleTime>0</ISuserMaxIdleTime> 
<SpeedDials>
<SpeedDial>
<SpeedDialIndex>1</SpeedDialIndex> 
<SpeedDialNumber>901</SpeedDialNumber> 
<SpeedDialLabel /> 
<SpeedDialBLF>no</SpeedDialBLF> 
</SpeedDial>
<SpeedDial>
<SpeedDialIndex>2</SpeedDialIndex> 
<SpeedDialNumber>902</SpeedDialNumber> 
<SpeedDialLabel /> 
<SpeedDialBLF>no</SpeedDialBLF> 
</SpeedDial>
<SpeedDial>
<SpeedDialIndex>3</SpeedDialIndex> 
<SpeedDialNumber>2002</SpeedDialNumber> 
<SpeedDialLabel>2002Label</SpeedDialLabel> 
<SpeedDialBLF>no</SpeedDialBLF> 
</SpeedDial>
<SpeedDial>
<SpeedDialIndex>5</SpeedDialIndex> 
<SpeedDialNumber>2004</SpeedDialNumber> 
<SpeedDialLabel>2004</SpeedDialLabel> 
<SpeedDialBLF>yes</SpeedDialBLF> 
</SpeedDial>
</SpeedDials>
<UserNumbers>
<UserNumber>
<ISExtNumber>2003</ISExtNumber> 
<ISExtMode>NORMAL</ISExtMode> 
<ISExtOverlayGroup>0</ISExtOverlayGroup> 
<ISExtCombo>no</ISExtCombo> 
</UserNumber>
<UserNumber>
<ISExtNumber>201</ISExtNumber> 
<ISExtMode>NORMAL</ISExtMode> 
<ISExtOverlayGroup>0</ISExtOverlayGroup> 
<ISExtCombo>no</ISExtCombo> 
</UserNumber>
<UserNumber>
<ISExtNumber>202</ISExtNumber> 
<ISExtMode>NORMAL</ISExtMode> 
<ISExtOverlayGroup>0</ISExtOverlayGroup> 
<ISExtCombo>no</ISExtCombo> 
</UserNumber>
</UserNumbers>
<ISuserCurrentPhone>
<CurrentPhoneType>Unknown</CurrentPhoneType> 
<CurrentPhoneID>0</CurrentPhoneID> 
</ISuserCurrentPhone>
</ISUserProfile>
</ISUserProfiles>
</response>
```

#### ISgetUtilityDirectory

Use the ISgetUtilityDirectory to retrieve status and configuration
                                    		  information for directory information.

##### Request

```
<request>
<ISgetUtilityDirectory>
</ISgetUtilityDirectory>
</request>
```

##### Response

```
<response>
<ISUtilityDirectory>
<ISDirectoryEntry>
<ISDirectoryTag>1</ISDirectoryTag> 
<ISDirectoryNumber>12345</ISDirectoryNumber> 
<firstName>first</firstName> 
<lastName>last</lastName> 
</ISDirectoryEntry>
<ISDirectoryEntry>
<ISDirectoryTag>2</ISDirectoryTag> 
<ISDirectoryNumber>67890</ISDirectoryNumber> 
<firstName>first2</firstName> 
<lastName>last 2</lastName> 
</ISDirectoryEntry>
</ISUtilityDirectory>
</response>
```

#### ISgetVoiceRegGlobal

Use the ISgetVoiceRegGlobal to retrieve status and configuration
                                    		  information of global parameters for SIP,

##### Request

```
<request>
<ISgetVoiceRegGlobal>
</ISgetVoiceRegGlobal>
</request>
```

##### Response

```
<response>
<ISSipGlobal>
<ISAddress>10.10.10.1</ISAddress> 
<ISMode>cme</ISMode> 
<ISVersion>7.1</ISVersion> 
<ISAuthModes>
<ISAuthMode>ood_refer</ISAuthMode> 
<ISAuthMode>presence</ISAuthMode> 
</ISAuthModes>
<ISPortNumber>5060</ISPortNumber> 
<ISMaxPool>10</ISMaxPool> 
<ISMaxDN>100</ISMaxDN> 
<ISMaxRedirect>5</ISMaxRedirect> 
</ISSipGlobal>
</response>
```

#### ISgetSipDevice

For SIP phones, use any combination of the following parameters in the
                                    		  request message to specify one or more SIP phones:

ISPoolID with the voice register pool tag number of SIP phone to
                                          				be queried.

ISPoolName with the voice register pool name of the SIP phone to
                                          				be queried.

ISKeyword with one of the following options:

all—All configured SIP phones

allTag—Voice register pool tag numbers for all configured SIP
                                                					 phones

available—Next available phone tag number to be configured

##### Request

```
<request>
<ISgetSipDevice>
<ISPoolID>1</ISPoolID> 
</ISgetSipDevice>
</request>
```

##### Response

```
<response>
<ISSipDevices>
<ISSipDevice>
<ISPoolID>1</ISPoolID> 
<ISDevMac>0013.1978.3CA5</ISDevMac> 
<ISSessionServerID>0</ISSessionServerID> 
<ISDevAddr>
<Xipv4Address>0</Xipv4Address> 
</ISDevAddr>
<ISSipPhoneLineList>
<ExtMapStatus>
<LineId>1</LineId> 
<ExtId>1</ExtId> 
<ExtNumber>901</ExtNumber> 
<LineState>idle</LineState> 
</ExtMapStatus>
<ExtMapStatus>
<LineId>2</LineId> 
<ExtId>2</ExtId> 
<ExtNumber>902</ExtNumber> 
<LineState>idle</LineState> 
</ExtMapStatus>
</ISSipPhoneLineList>
<ISPoolMaxRegistration>42</ISPoolMaxRegistration> 
<ISPoolDtmfRelay>rtp-nte</ISPoolDtmfRelay> 
<ISDevCodec>g729r8</ISDevCodec> 
</ISSipDevice>
</ISSipDevices>
</response>
```

#### ISgetSipExtension

Use ISgetSipExtension to retrieve configuration and status information
                                    		  for extension numbers.

Use any combination of the following parameters in the request message
                                    		  to specify one or more extensions:

ISVoiceRegDNID with the extension ID number to be queried.

ISVoiceRegNumber with the extension number to be queried.

ISKeyword with one of the following options:

all—Displays details of all configured extension numbers

allTag—Displays a list of all configured extension ID numbers

available—Next available extension ID number to be configured

##### Request

```
<request>
<ISgetSipExtension>
<ISVoiceRegDNID>1</ISVoiceRegDNID> 
</ISgetSipExtension>
</request>
```

##### Response

```
<response>
<ISSipExtensions>
<ISSipExtension>
<ISVoiceRegDNID>1</ISVoiceRegDNID> 
<ISExtNumber>901</ISExtNumber> 
<ISSessionServerIDs>
<ISSessionServerID>1</ISSessionServerID> 
<ISSessionServerID>2</ISSessionServerID> 
</ISSessionServerIDs>
<ISAllowWatch>true</ISAllowWatch> 
<firstName>Henry</firstName> 
<lastName>Mann</lastName> 
<ISSipDevList>
<ISPoolID>1</ISPoolID> 
<ISPoolID>2</ISPoolID> 
</ISSipDevList>
</ISSipExtension>
</ISSipExtensions>
</response>
```

#### ISgetSessionServer

Use ISgetSessionServer to retrieve configuration information for
                                    		  session servers in Cisco Unified CME.

Use any combination of the following parameters in the request message
                                    		  to specify one or more session servers:

ISSessionServerID with the session server tag number.

ISSessionserverName with session server name.

ISKeyword with one of the following keywords:

all—All configured session servers

allTag—Session server tag numbers for all configured session
                                                					 servers

available—Next available session server tag number to be
                                                					 configured

##### Request

```
<request>
<ISgetSessionServer>
<ISSessionServerID>1</ISSessionServerID>
</ISgetSessionServer>
</request>
```

##### Response

```
<response>
<ISSessionServers>
<ISSessionServer>
<ISSessionServerID>1</ISSessionServerID> 
<ISSessionRegisterID>SS1</ISSessionRegisterID> 
<ISSessionKeepAlives>60</ISSessionKeepAlives> 
</ISSessionServer>
</ISSessionServers>
</response>
```

#### ISgetVoiceHuntGroup

Use the ISgetVoiceHuntGroupID to retrieve status and configuration
                                    		  information for voice hunt groups.

Use any combination of the following parameters in the request message
                                    		  to specify one or more voice hunt groups:

ISVoiceHuntGroupID with the voice hunt group ID number.

ISKeyword with one of the following keywords:

all—All configured voice hunt groups

allTag—Voice hunt group ID numbers for all configured voice
                                                					 hunt groups

available—Next available voice hunt group ID number to be
                                                					 configured

##### Request

```
<request>
<ISgetVoiceHuntGroup>
<ISVoiceHuntGroupID>1</ISVoiceHuntGroupID> 
</ISgetVoiceHuntGroup>
</request>
```

##### Response

```
<response>
<ISVoiceHuntGroups>
<ISVoiceHuntGroup>
<ISVoiceHuntGroupID>1</ISVoiceHuntGroupID> 
<ISVoiceHuntGroupType>longest-idle</ISVoiceHuntGroupType> 
<ISVoiceHuntGroupPilotNumber>200</ISVoiceHuntGroupPilotNumber> 
<ISVoiceHuntGroupPilotPeerTag>200</ISVoiceHuntGroupPilotPeerTag> 
<ISVoiceHuntGroupPilotPreference>0</ISVoiceHuntGroupPilotPreference> 
<ISVoiceHuntGroupSecPilotNumber /> 
<ISVoiceHuntGroupSecPilotPeerTag>-1</ISVoiceHuntGroupSecPilotPeerTag> 
<ISVoiceHuntGroupSecPilotPreference>0</ISVoiceHuntGroupSecPilotPreference> 
<ISVoiceHuntGroupListSize>2</ISVoiceHuntGroupListSize> 
<ISVoiceHuntGroupListNums>
<ISVoiceHuntGroupListNum>201</ISVoiceHuntGroupListNum> 
<ISVoiceHuntGroupListNum>202</ISVoiceHuntGroupListNum> 
</ISVoiceHuntGroupListNums>
<ISVoiceHuntGroupFinalNum /> 
<ISVoiceHuntGroupTimeout>180</ISVoiceHuntGroupTimeout> 
<ISVoiceHuntGroupHops>2</ISVoiceHuntGroupHops> 
</ISVoiceHuntGroup>
</ISVoiceHuntGroups>
</response>
```

#### ISgetPresenceGlobal

Use ISgetPresenceGlobal to retrieve configuration information and
                                    		  status for the presence engine in Cisco Unified CME.

##### Request

```
<request>
<ISgetPresenceGlobal /> 
</request>
```

##### Response

```
<response>
<ISPresenceGlobal>
<ISPresenceEnable>true</ISPresenceEnable> 
<ISMode>cme</ISMode> 
<ISAllowSub>true</ISAllowSub> 
<ISAllowWatch>true</ISAllowWatch> 
<ISMaxSubAllow>100</ISMaxSubAllow> 
<ISSipUaPresenceStatus>false</ISSipUaPresenceStatus> 
</ISPresenceGlobal>
</response>
```

## Configure XML
                        	 API

The following
                                       		  Cisco IOS commands that were previously used with the XML interface are no
                                       		  longer valid: log password , xmltest , xmlschema ,
                                       		  and xmlthread .

### Define XML
                           	 Transport Parameters

To define the XML
                                 		  transport method and associated parameters, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- ip http server

- ixi transport http

- response size fragment-size

- request outstanding number

- request timeout seconds

- no shutdown

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ip http server

#### Example:

```
Router(config)# ip http server
```

Enables the
                                             				Cisco web browser user interface on the local Cisco Unified CME router.

Step 4

ixi transport http

#### Example:

```
Router(config)# ixi transport http
```

Specifies the
                                             				XML transport method and enters XML-transport configuration mode.

http —HTTP transport.

Step 5

response size fragment-size

#### Example:

```
Router(conf-xml-trans)# response size 8
```

Sets the
                                             				response buffer size.

fragment-size —Size of fragment in the response
                                                   					 buffer, in kilobytes. Range is constrained by the transport type and platform.
                                                   					 See the CLI help for the valid range of values.

Step 6

request outstanding number

#### Example:

```
Router(conf-xml-trans)# request outstanding 2
```

Sets the
                                             				maximum number of outstanding requests allowed for the transport type.

number —Number of requests. Range is constrained by
                                                   					 the transport type and platform. See the CLI help for the valid range of
                                                   					 values.

Step 7

request timeout seconds

#### Example:

```
Router(conf-xml-trans)# request timeout 30
```

Sets the
                                             				number of seconds to wait, while processing a request, before timing out.

seconds —Number of seconds. Range is 0 to 60.

Step 8

no shutdown

#### Example:

```
Router(conf-xml-trans)# no shutdown
```

Enables HTTP
                                             				transport.

Step 9

end

#### Example:

```
Router(config-xml-app)# end
```

Returns to
                                             				privileged EXEC mode.

### Define XML
                           	 Application Parameters

To set a response
                                 		  timeout for communication with the XML application that overrides the setting
                                 		  in transport configuration mode, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- ixi application cme

- response timeout { -1 | seconds }

- no shutdown

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ixi application cme

#### Example:

```
Router(config)# ixi application cme
```

Enters
                                             				XML-application configuration mode for configuring Cisco IOS XML infrastructure
                                             				parameters for the Cisco Unified CME application.

This command
                                                         				  defines URL of Cisco Unified CME XML server as http://<routerIPaddress>/ios_xml_app/cme .

Step 4

response timeout { -1 | seconds }

#### Example:

```
Router(config-xml-app)# response timeout 30
```

Sets a timeout
                                             				for responding to the XML application and overwrites the IXI transport level
                                             				timeout.

-1 —No application-specific timeout is specified.
                                                   					 This is the default.

seconds —Length of timeout, in seconds. Range is
                                                   					 0 to 60.

Step 5

no shutdown

#### Example:

```
Router(conf-xml-app)# no shutdown
```

Enables XML
                                             				communication with the application.

Step 6

end

#### Example:

```
Router(config-xml-app)# end
```

Returns to
                                             				privileged EXEC mode.

### Define
                           	 Authentication for XML Access

To authenticate
                                 		  users for XML access, perform the following steps:

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- xml user user-name password password
                                       				  privilege-level

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

xml user user-name password password
                                                				  privilege-level

#### Example:

```
Router(config-telephony)# xml user user23 password 3Rs92uzQ 15
```

Defines an
                                             				authorized user.

user-name —Unique alphanumeric string that is
                                                   					 authorized user name. Maximum length of string is 19 characters.

password —Alphanumeric string to use for access.
                                                   					 Maximum length of string is 19 characters.

privilege-level —Level of access to Cisco IOS
                                                   					 commands to be granted to this user. Only the commands with the same or a lower
                                                   					 level can be executed via XML. Range is 0 (lowest) to 15 (highest).

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Define XML Event
                           	 Table Parameters

The XML event
                                 		  table is an internal buffer that stores captured and time-stamped events, such
                                 		  as phones registering and unregistering and extension status. One event equals
                                 		  one entry in the table. To set the maximum number of events or entries that can
                                 		  be stored in the XML event table and the length of time that events are
                                 		  retained before they are deleted from the table, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- log table max-size number

- log table retain-timer minutes

- end

- show fb-its-log

- clear telephony-service xml-event-log

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)#
```

Enters
                                             				telephony-service configuration mode.

Step 4

log table max-size number

#### Example:

```
Router(config-telephony)# log table max-size 100
```

Sets the
                                             				number of entries in the XML event table.

number —Number of entries. Range is 0 to 1000.
                                                   					 Default is 150.

Step 5

log table retain-timer minutes

#### Example:

```
Router(config-telephony)# log table retain-timer 30
```

Sets the
                                             				number of minutes to retain entries in the event table before they are deleted.

minutes —Number of minutes. Range is 2 to 500.
                                                   					 Default is 15.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

Step 7

show fb-its-log

#### Example:

```
Router# show fb-its-log
```

Displays the
                                             				event logs.

Step 8

clear telephony-service xml-event-log

#### Example:

```
Router# clear telephony-service xml-event-log
```

Clears XML
                                             				event logs.

### Troubleshooting the XML Interface

Use the debug cme-xml command to view debug
                                    			 messages for the Cisco Unified CME XML interface.

## Configuration Examples for XML API

### Example for XML Transport Parameters

The following example selects HTTP as the XML transport method:

```
ip http server 
ixi transport http
 response size 8
 request outstanding 2
 request timeout 30
 no shutdown
```

### Example for XML Application Parameters

The following example sets the application response timeout to 30
                                 		  seconds.

```
ixi application cme
 response timeout 30
 no shutdown
```

### Example for XML Authentication

The following example selects HTTP as the XML transport method. It
                                 		  allows access for user23 with the password 3Rs92uzQ, and sets up access list 99
                                 		  that accepts requests from the IP address 192.168.146.72.

```
ixi transport http
		ip http server 
		!
		telephony-service
		xml user user23 password 3Rs92uzQ 15
```

### Example for XML Event Table

The following example sets the maximum number of entries in the XML
                                 		  event table to 100 and the number of minutes to retain entries at 30:

```
telephony-service
		 log table max-size 100
		 log table retain-timer 30
```

## Where to Go
                        	 Next

For developer information on the XML API, see XML Provisioning Guide for Cisco
                              		  CME/SRST .

## Feature
                        	 Information for XML API

The following table provides release information about the feature or
                           		features described in this module. This table lists only the software release
                           		that introduced support for a given feature in a given software release train.
                           		Unless noted otherwise, subsequent releases of that software release train also
                           		support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn . An account on
                           		Cisco.com is not required.

Feature Name

Cisco Unified CME Version

Feature Information

Call Blocking Based on Date and Time

4.0

The XML API was modified and is now provided through the Cisco IOS XML infrastructure. It supports all Cisco Unified CME features.

3.0

The XML API was introduced.

12.6

The log password , xmltest , xmlschema , and xmlthread commands were deprecated.

| Note | Querying for
                                          		  multiple entities in a single request can fail because of the XML buffer size
                                          		  limitation. Because of this limitation, the application must adjust its
                                          		  granularity to query one entity per request. |
|---|---|

| Description | Request | Parameter | Response |
|---|---|---|---|
| System |
| Execute
                                             					 configuration commands | ISexecCLI | command | ISexecCLIResult |
| Save
                                             					 router configuration to nvram | ISSaveConfig | — | ISSaveConfigResult |
| SCCP |
| Get system
                                             					 status for Cisco Unified CME or Cisco Unified SRST. | ISgetGlobal | — | ISGlobal |
| Get status
                                             					 of an IP phone | ISgetDevice | Any
                                             					 combination of the following: ISDevID ISDevName ISKeyword: all allTag available | ISDevices |
| Get
                                             					 configuration of a phone template | ISgetDeviceTemplate | Any
                                             					 combination of the following: ISDevTemplateID ISKeyword: all allTag available | ISDeviceTemplates |
| Get
                                             					 configuration of an extension | ISgetExtension | Any
                                             					 combination of the following: ISExtID ISExtNumber ISKeyword: all allTag available | ISExtensions |
| Get
                                             					 configuration of an extension template | ISgetExtensionTemplate | Any
                                             					 combination of the following: ISExtTemplateID ISKeyword: all allTag available | ISExtensionTemplates |
| Get user
                                             					 information | ISgetUser | ISuserID | ISuser |
| Get user
                                             					 profile information | ISgetuserProfile | Any
                                             					 combination of the following: ISUserProfileID ISuserID ISKeyword: all allTag available | ISUserProfiles |
| Get
                                             					 configuration for utility directory | ISgetUtilityDirectory | — | ISUtilityDirectory |
| SIP |
| Get
                                             					 system status for a Cisco Unified CME running SIP | ISgetVoiceRegGlobal | — | ISSipGlobal |
| Get
                                             					 status of an IP phone | ISgetSipDevice | Any
                                             					 combination of the following: ISPoolID ISPoolName ISKeyword: all allTag available | ISSipDevices |
| Get
                                             					 configuration of an extension | ISgetSipExtension | Any
                                             					 combination of the following: ISVoiceRegDNID ISVoiceRegNumber ISKeyword: all allTag available | ISSipExtensions |
| Get
                                             					 status of a session server | ISgetSessionServer | Any
                                             					 combination of the following: ISSessionServerID ISSessionServerName ISKeyword: all allTag available | ISSessionServers |
| Get
                                             					 status of voice hunt groups | ISgetVoiceHuntGroup | ISVoiceHuntGroupID ISKeyword: all allTag available | ISVoiceHuntGroups |
| Get
                                             					 configuration for Presence | ISgetPresenceGlobal | — | ISPresenceGlobal |

| Note | The following
                                       		  Cisco IOS commands that were previously used with the XML interface are no
                                       		  longer valid: log password , xmltest , xmlschema ,
                                       		  and xmlthread . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ip http server Example: Router(config)# ip http server | Enables the
                                             				Cisco web browser user interface on the local Cisco Unified CME router. |
| Step 4 | ixi transport http Example: Router(config)# ixi transport http | Specifies the
                                             				XML transport method and enters XML-transport configuration mode. http —HTTP transport. |
| Step 5 | response size fragment-size Example: Router(conf-xml-trans)# response size 8 | Sets the
                                             				response buffer size. fragment-size —Size of fragment in the response
                                                   					 buffer, in kilobytes. Range is constrained by the transport type and platform.
                                                   					 See the CLI help for the valid range of values. |
| Step 6 | request outstanding number Example: Router(conf-xml-trans)# request outstanding 2 | Sets the
                                             				maximum number of outstanding requests allowed for the transport type. number —Number of requests. Range is constrained by
                                                   					 the transport type and platform. See the CLI help for the valid range of
                                                   					 values. |
| Step 7 | request timeout seconds Example: Router(conf-xml-trans)# request timeout 30 | Sets the
                                             				number of seconds to wait, while processing a request, before timing out. seconds —Number of seconds. Range is 0 to 60. |
| Step 8 | no shutdown Example: Router(conf-xml-trans)# no shutdown | Enables HTTP
                                             				transport. |
| Step 9 | end Example: Router(config-xml-app)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ixi application cme Example: Router(config)# ixi application cme | Enters
                                             				XML-application configuration mode for configuring Cisco IOS XML infrastructure
                                             				parameters for the Cisco Unified CME application. Note This command
                                                         				  defines URL of Cisco Unified CME XML server as http://<routerIPaddress>/ios_xml_app/cme . | Note | This command
                                                         				  defines URL of Cisco Unified CME XML server as http://<routerIPaddress>/ios_xml_app/cme . |
| Note | This command
                                                         				  defines URL of Cisco Unified CME XML server as http://<routerIPaddress>/ios_xml_app/cme . |
| Step 4 | response timeout { -1 \| seconds } Example: Router(config-xml-app)# response timeout 30 | Sets a timeout
                                             				for responding to the XML application and overwrites the IXI transport level
                                             				timeout. -1 —No application-specific timeout is specified.
                                                   					 This is the default. seconds —Length of timeout, in seconds. Range is
                                                   					 0 to 60. |
| Step 5 | no shutdown Example: Router(conf-xml-app)# no shutdown | Enables XML
                                             				communication with the application. |
| Step 6 | end Example: Router(config-xml-app)# end | Returns to
                                             				privileged EXEC mode. |

| Note | This command
                                                         				  defines URL of Cisco Unified CME XML server as http://<routerIPaddress>/ios_xml_app/cme . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | xml user user-name password password
                                                				  privilege-level Example: Router(config-telephony)# xml user user23 password 3Rs92uzQ 15 | Defines an
                                             				authorized user. user-name —Unique alphanumeric string that is
                                                   					 authorized user name. Maximum length of string is 19 characters. password —Alphanumeric string to use for access.
                                                   					 Maximum length of string is 19 characters. privilege-level —Level of access to Cisco IOS
                                                   					 commands to be granted to this user. Only the commands with the same or a lower
                                                   					 level can be executed via XML. Range is 0 (lowest) to 15 (highest). |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# | Enters
                                             				telephony-service configuration mode. |
| Step 4 | log table max-size number Example: Router(config-telephony)# log table max-size 100 | Sets the
                                             				number of entries in the XML event table. number —Number of entries. Range is 0 to 1000.
                                                   					 Default is 150. |
| Step 5 | log table retain-timer minutes Example: Router(config-telephony)# log table retain-timer 30 | Sets the
                                             				number of minutes to retain entries in the event table before they are deleted. minutes —Number of minutes. Range is 2 to 500.
                                                   					 Default is 15. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |
| Step 7 | show fb-its-log Example: Router# show fb-its-log | Displays the
                                             				event logs. |
| Step 8 | clear telephony-service xml-event-log Example: Router# clear telephony-service xml-event-log | Clears XML
                                             				event logs. |

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| Call Blocking Based on Date and Time | 4.0 | The XML API was modified and is now provided through the Cisco IOS XML infrastructure. It supports all Cisco Unified CME features. |
| 3.0 | The XML API was introduced. |
| 12.6 | The log password , xmltest , xmlschema , and xmlthread commands were deprecated. |