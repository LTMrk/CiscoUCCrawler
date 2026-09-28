---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-1-cjab-b-param-reference-for-jabber141-cjab-b-parameter-reference--d345a0c61f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_1/cjab_b_param-reference-for-jabber141/cjab_b_parameter-reference-guide-jabber-129_chapter_010.html
retrieved_at: 2026-08-21T21:16:31.805311+00:00
---

Parameters Reference Guide for Cisco Jabber 14.1

# Parameters Reference Guide for Cisco Jabber 14.1

Updated: March 4, 2022

Chapter: Jabber Client Configuration

## Chapter: Jabber Client Configuration

# Jabber Client Configuration

## Jabber Client Configuration Methods

You can configure Jabber client configuration parameters by either:

using Unified CM Administration inteface

creating the configuraiton file using an XML editor.

For more information the Client Configuration Workflow section of the latest release of the On-Premises Deployment for Cisco Jabber or Cloud and Hybrid Deployments for Cisco Jabber .

## Configuration File
                        	 Structure

You create client
                              		  configuration files in an XML format that contains the following elements

### XML
                              		  Declaration

```
<?xml version="1.0" encoding="utf-8"?>
```

### Root
                              		  Element

```
<?xml version="1.0" encoding="utf-8"?>
<config version="1.0">
</config>
```

### Group
                              		  Elements

Group elements
                              		  contain configuration parameters and values. You must nest group elements
                              		  within the root element.

### XML Structure

```
<Client>
  < parameter > value </ parameter >
</Client>
<Directory>
  < parameter > value </ parameter >
</Directory>
<Options>
  < parameter > value </ parameter >
</Options>
<Phone>
  < parameter > value </ parameter >
</Phone>
<Policies>
  < parameter > value </ parameter >
</Policies>
<Presence>
  < parameter > value </ parameter >
</Presence>
<Voicemail>
  < parameter > value </ parameter >
</Voicemail>
```

## Example
                        	 Configuration

The following is
                              		  an example of a configuration file used in an on-premises deployment for all
                              		  clients:

```
<?xml version="1.0" encoding="utf-8"?>
<config version="1.0">
 <Client>
  <PrtLogServerUrl>http:// server_name : port / path / prt_script.php </ PrtLogServerUrl >
  <jabber-plugin-config>
   <browser-plugin>
    <page refresh="true" preload="true">
     <tooltip>Cisco</tooltip>
     <icon>http://www.cisco.com/web/fw/i/logo.gif</icon>
     <url>www.cisco.com</url>
    </page>
   </browser-plugin>
  </jabber-plugin-config>
  </Client>
  <Options>
    <Set_Status_Inactive_Timeout>20</Set_Status_Inactive_Timeout>
    <StartCallWithVideo>false</StartCallWithVideo>
  </Options>
  <Policies>
    <Disallowed_File_Transfer_Types>.exe;.msi</Disallowed_File_Transfer_Types>
  </Policies>
<Directory>
    <PrimaryServerName>dir.example.com</PrimaryServerName>
    <SearchBase1>ou=staff,dc=example,dc=com</SearchBase1>
    <ConnectionUsername>ad_jabber_access@eample.com</ConnectionUsername>
    <ConnectionPassword>Jabber</ConnectionPassword>
    <PhotoUriSubstitutionEnabled>True</PhotoUriSubstitutionEnabled>
    <PhotoUriSubstitutionToken>sAMAccountName</PhotoUriSubstitutionToken>
    <PhotoUriWithToken>http://example.com/phto/sAMAccountName.jpg</PhotoUriWithToken>
  </Directory>
</config>
```