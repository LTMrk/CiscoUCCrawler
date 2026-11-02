---
doc_id: help-webex-com-en-us-article-ntypdwb-c645c2b53f
source_url: https://help.webex.com/en-us/article/ntypdwb
retrieved_at: 2026-11-02T13:05:57.483288+00:00
---

## Overview

XML Services Interface (XSI) is a protocol that allows communication between applications and the phone system. You can add your own XSI services to your phone using the supported XML objects and URIs.

After subscribing the phone to the services, users can access all the configured services on the phone by navigating to Settings > Network and service > Cisco XML services .  Cisco XML services is the default name. You can also change the name. To provide an easy access for users, you can add the XML applications to softkeys or line keys.

The supported features are:

- Messages (images and text)

- Paging

### Supported XML objects

CiscoIPPhoneMenu

CiscoIPPhoneText

CiscoIPPhoneInput

CiscoIPPhoneDirectory

CiscoIPPhoneImage

CiscoIPPhoneImageFile

CiscoIPPhoneIconMenu

CiscoIPPhoneIconFileMenu

CiscoIPPhoneStatus (except 9811 and 9841)

CiscoIPPhoneStatusFile (except 9811 and 9841)

CiscoIPPhoneExecute

### Supported URIs

Device

Dial

EditDail

Init

Key

Play (ringtones only)

Softkey

For more details about the XSI service configuration, see Cisco Unified IP Phone Services Application Development Notes .

## Configure a phone to connect to an XML service

Access the phone administration web page.

Select Voice > Phone .

In the XML Service section, configure the XML Application Service Name and XML Application Service URL parameters as defined in Parameters for XML services .

(Optional) To add authentication for accessing the application service, configure theses fields: XML User Name , XML Password , CISCO XML EXE Enable , and CISCO XML EXE Auth Mode .

Click Save All Changes .

## Parameters for XML services

The following table defines the function and usage of the XML application parameters in the XML Service section under the Voice > Phone tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file (cfg.xml) with XML code to configure a parameter.

Parameter

Default and options

Description

XML Application Service Name

Default: Empty

Name of the XML application. The name displays on the phone as a web application choice.

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<XML_Application_Service_Name
ua="na">XML APP Name</XML_Application_Service_Name>
```

XML Application Service URL

Default: Empty

The URL where the XML application is located.

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<XML_Application_Service_URL
ua="na">https://server.com/path/app.xml</XML_Application_Service_URL>
```

Macro variables are supported in XML URLs. For the valid macro variables, see Macro variables supported in XML URLs .

Only HTTP or HTTPs protocols are supported in the URL.

XML User Name

Default: Empty

XML service username for authentication purposes.

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<XML_User_Name ua="na">username</XML_User_Name>
```

XML Password

Default: Empty

XML service password for the specified XML User Name.

The password you entered in this field shows in the configuration file (cfg.xml) as the following:

CISCO XML EXE Enable

Default: No

Options: Yes, No

Specifies whether authentication is required to access the XML application server.

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<CISCO_XML_EXE_Enable ua="na">Yes</CISCO_XML_EXE_Enable>
```

CISCO XML EXE Auth Mode

Default: Local Credential

Options: Trusted, Local Credential, Remote Credential

Specifies the authentication mode for Cisco XML EXE.

Trusted—No authentication is performed regardless of the local credential.

Local Credential—Authentication is based on the digest authentication using the local credential, if set. If the local credential is not set, then no authentication is performed.

- Remote Credential—Authentication is based on the digest authentication using the remote credential as set in the XML application on the web page (to access an XML application server).

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<CISCO_XML_EXE_Auth_Mode ua="na">Local Credential</CISCO_XML_EXE_Auth_Mode>
```

## Add an XML application to a softkey

Add the frequently used applications to softkeys for users to access the service easily.

Before you begin

The XML Application Service has been properly configured.

Access the phone administration web page.

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format:

```
<Programmable_Softkey_Enable ua="na">Yes</Programmable_Softkey_Enable>
```

In the Programmable Softkeys section, edit the available fields of PSK1 to PSK16 in this format:

where url is the link where the XML application is stored; nme is the display name of the application on the phone screen.

Example fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu

You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format:

<PSK_n ua="na">fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu <configuration code> </PSK_n>

where n is the softkey number.

Click Save All Changes .

## Add an XML application to a line key

Add the frequently used applications to line keys for users to access the services easily.

Before you begin

The XML Application Service has been properly configured.

Access the phone administration web page.

Select Voice > Phone .

Select a line key.

Set the Extension parameter to Disabled to disable the extension.

If the Direct PLK Configuration feature is disabled, you must disable the extension to add an extended function to the line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK configuration .

In the Extended Function parameter, enter a string in this format:

where url is the link where the XML application is stored; nme is the display name of the application on the phone screen.

Example fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu

You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format:

<Extended_Function_n_ ua="na">fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu <configuration code> </Extended_Function_n_>

where n is the extension number.

Click Save All Changes .

## Macro variables supported in XML URLs

You can use macro variables in XML URLs. The following macro variables are supported:

User ID—UID1, UID2 to UIDn

Display name—DISPLAYNAME1, DISPLAYNAME2 to DISPLAYNAMEn

Auth ID—AUTHID1, AUTHID2 to AUTHIDn

Proxy—PROXY1, PROXY2 to PROXYn

MAC Address using lowercase hex digits—MA

Product Name—PN

Product Series Number—PSN

Serial Number—SERIAL_NUMBER

$SA through $SD are recognized as arguments to the optional resync URL
                    qualifier, --key.

SWVER

Software version string. For example,

PHONEOS.3-2-1-0104-37

HWVER

Hardware version string. For example, 2.0.1

PRVST

Provisioning State (a numeric string):

-1 = explicit resync request

0 = power-up resync

1 = periodic resync

2 = resync failed, retry attempt

UPGST

Upgrade State (a numeric string):

1 = first upgrade attempt

2 = upgrade failed, retry attempt

UPGERR

Result message (ERR) of previous upgrade attempt; for example http_get failed.

PRVTMR

Seconds since last resync attempt.

UPGTMR

Seconds since last upgrade attempt.

REGTMR1

Seconds since Line 1 lost registration with SIP server.

REGTMR2

Seconds since Line 2 lost registration with SIP server.

UPGCOND

Legacy macro name.

SCHEME

File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL.

SERV

Request target server host name, as obtained after parsing resync or upgrade URL.

SERVIP

Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup.

PORT

Request target UDP/TCP port, as obtained after parsing resync or upgrade URL.

PATH

Request target file path, as obtained after parsing resync or upgrade URL.

ERR

Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts.

UIDn

The contents of the Line n UserID configuration parameter.

If unit is customized, value=1, otherwise 0.

Customization status is viewable on Web UI Info page.

Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first call found is provided.

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the XML Service section, configure the XML Application Service Name and XML Application Service URL parameters as defined in Parameters for XML services . |
| 4 | (Optional) To add authentication for accessing the application service, configure theses fields: XML User Name , XML Password , CISCO XML EXE Enable , and CISCO XML EXE Auth Mode . |
| 5 | Click Save All Changes . |

| Parameter | Default and options | Description |
|---|---|---|
| XML Application Service Name | Default: Empty | Name of the XML application. The name displays on the phone as a web application choice. You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <XML_Application_Service_Name
ua="na">XML APP Name</XML_Application_Service_Name> |
| XML Application Service URL | Default: Empty | The URL where the XML application is located. You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <XML_Application_Service_URL
ua="na">https://server.com/path/app.xml</XML_Application_Service_URL> Macro variables are supported in XML URLs. For the valid macro variables, see Macro variables supported in XML URLs . Only HTTP or HTTPs protocols are supported in the URL. |
| XML User Name | Default: Empty | XML service username for authentication purposes. You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <XML_User_Name ua="na">username</XML_User_Name> |
| XML Password | Default: Empty | XML service password for the specified XML User Name. The password you entered in this field shows in the configuration file (cfg.xml) as the following: |
| CISCO XML EXE Enable | Default: No Options: Yes, No | Specifies whether authentication is required to access the XML application server. You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <CISCO_XML_EXE_Enable ua="na">Yes</CISCO_XML_EXE_Enable> |
| CISCO XML EXE Auth Mode | Default: Local Credential Options: Trusted, Local Credential, Remote Credential | Specifies the authentication mode for Cisco XML EXE. Trusted—No authentication is performed regardless of the local credential. Local Credential—Authentication is based on the digest authentication using the local credential, if set. If the local credential is not set, then no authentication is performed. Remote Credential—Authentication is based on the digest authentication using the remote credential as set in the XML application on the web page (to access an XML application server). You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <CISCO_XML_EXE_Auth_Mode ua="na">Local Credential</CISCO_XML_EXE_Auth_Mode> |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format: <Programmable_Softkey_Enable ua="na">Yes</Programmable_Softkey_Enable> |
| 4 | In the Programmable Softkeys section, edit the available fields of PSK1 to PSK16 in this format: fnc=xml;url= <xml_app_path> ;nme= <app_name> where url is the link where the XML application is stored; nme is the display name of the application on the phone screen. Example fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format: <PSK_n ua="na">fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu <configuration code> </PSK_n> where n is the softkey number. |
| 5 | Click Save All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Select a line key. |
| 4 | Set the Extension parameter to Disabled to disable the extension. If the Direct PLK Configuration feature is disabled, you must disable the extension to add an extended function to the line key. If the feature is enabled, you can skip this step. For details, see Enable Direct PLK configuration . |
| 5 | In the Extended Function parameter, enter a string in this format: fnc=xml;url= <xml_app_path> ;nme= <app_name> where url is the link where the XML application is stored; nme is the display name of the application on the phone screen. Example fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu You can also configure this parameter in the configuration file (cfg.xml). Enter a string in this format: <Extended_Function_n_ ua="na">fnc=xml;url=http://10.77.21.37/xmlapp/menu.xml;nme=Menu <configuration code> </Extended_Function_n_> where n is the extension number. |
| 6 | Click Save All Changes . |

| Macro Name | Macro Expansion |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by general-purpose parameters GPP_A through GPP_P. |
| SA through SD | Replaced by special purpose parameters GPP_SA through GPP_SD. These parameters
                hold keys or passwords used in provisioning. $SA through $SD are recognized as arguments to the optional resync URL
                    qualifier, --key. |
| MA | MAC address using lowercase hex digits (000e08aabbcc). |
| MAU | MAC address using uppercase hex digits (000E08AABBCC). |
| MAC | MAC address using lowercase hex digits with a colon to separate hex digit pairs (00:0e:08:aa:bb:cc). |
| PN | Product Name; for example, Video Phone 8875, Desk Phone 9851. |
| PSN | Product Series Number; for example, 8875, 9841, 9861 |
| SN | Serial Number string; for example, 88012BA01234. |
| CCERT | SSL Client Certificate status, installed or not installed. |
| IP | IP address of the phone within its local subnet; for example, 192.168.1.100. |
| EXTIP | External IP of the phone, as seen on the internet; for example, 66.43.16.52. |
| SWVER | Software version string. For example, PHONEOS.3-2-1-0104-37 |
| HWVER | Hardware version string. For example, 2.0.1 |
| PRVST | Provisioning State (a numeric string): -1 = explicit resync request 0 = power-up resync 1 = periodic resync 2 = resync failed, retry attempt |
| UPGST | Upgrade State (a numeric string): 1 = first upgrade attempt 2 = upgrade failed, retry attempt |
| UPGERR | Result message (ERR) of previous upgrade attempt; for example http_get failed. |
| PRVTMR | Seconds since last resync attempt. |
| UPGTMR | Seconds since last upgrade attempt. |
| REGTMR1 | Seconds since Line 1 lost registration with SIP server. |
| REGTMR2 | Seconds since Line 2 lost registration with SIP server. |
| UPGCOND | Legacy macro name. |
| SCHEME | File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL. |
| SERV | Request target server host name, as obtained after parsing resync or upgrade URL. |
| SERVIP | Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup. |
| PORT | Request target UDP/TCP port, as obtained after parsing resync or upgrade URL. |
| PATH | Request target file path, as obtained after parsing resync or upgrade URL. |
| ERR | Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts. |
| UIDn | The contents of the Line n UserID configuration parameter. |
| ISCUST | If unit is customized, value=1, otherwise 0. Customization status is viewable on Web UI Info page. |
| INCOMINGNAME | Name associated with first connected, ringing, or inbound call. |
| REMOTENUMBER | Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first call found is provided. |
| DISPLAYNAMEn | The contents of the Line N Display Name configuration parameter. |
| AUTHIDn | The contents of the Line N auth ID configuration parameter. |