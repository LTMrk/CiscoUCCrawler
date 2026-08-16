---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-all-models-xsi-9-1-1-cuip-bk-p82b3b16-00-phones-services-application--14baed18e3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes1_chapter_01000.html
retrieved_at: 2026-08-16T18:02:01.415010+00:00
---

Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

# Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

Updated: August 6, 2026

Chapter: Cisco IP Phone Services Software Development Kit (SDK)

## Chapter: Cisco IP Phone Services Software Development Kit (SDK)

# Cisco IP Phone Services Software Development Kit (SDK)

## SDK Overview

The Cisco IP Phone Services Software Development Kit (SDK) contains everything that you require
                           to create XML applications, including necessary documentation
                           and sample applications. Contact Cisco DevNet to obtain the SDK
                           at:

https://developer.cisco.com/site/ip-phone-services/documentation/

## SDK Components

The SDK contains the following components.

### Documentation

Cisco IP Services Development Notes (PDF format)

Cisco URL Proxy Guide (Rich Text Format)

Cisco LDAP Programming Guide (Microsoft Word format)

Cisco CIP Image Release Notes (Microsoft Word format)

Cisco IP Applications Samples (Microsoft Word format)

### Development Tools

Cip.8bi: Adobe Photoshop plug-in that allows .cip extensions to be viewed and saved.

Cip2Gif.exe: DOS-based program that converts .cip files to .gif.

Gif2Cip.exe: DOS-based program that converts .gif files to .cip.

ImageViewer.exe: Windows application that displays .cip graphic files.

Cisco CIPImage: used for converting images to and from CIP images (automatically installed)

Cisco URL Proxy: Proxy server that is needed to use the sample services (automatically installed).

Cisco LDAP Search: Service that is installed to do LDAP searches (automatically installed).

Microsoft XML Parser (MXSML) 3.0: Used for parsing XML data (automatically installed)

Cisco Unified IP Phone Services ASP/Javascript Library (automatically installed)

Cisco Unified IP Phone Services Java Library: Used by the JSP apps (manually installed; see JSP Install readme)

CallManager Simulator: Used for developing Phone Services without a Cisco Unified Communications Manager server

Cisco Unified IP Phone XML Schema (.xsd) file: Used with an XML editor to validate XML syntax

### Sample Services

Weather forecast lookup for any city (ASP)

Currency Exchange Rates and Converter (ASP)

UPS Rates & tracking (ASP)

World Clock (ASP)

Measurement conversions (ASP)

US White pages/Yellow Pages search (ASP)

Calendar (ASP)

Stock Ticker (ASP)

Stock Chart (ASP)

Push2Phone (ASP and JSP)

Click2Dial (ASP and JSP)

IdleURL (ASP) - Not supported on Cisco Unified IP Phones 7905G and 7912G

MConference (JSP)

Hootie (ASP)

InterCom (ASP)

JPEGViewer (ASP)

Logo (ASP)

Clock (ASP)

Personal Service (ASP)

WaterMark (ASP)

Extension Mobility Controller (JSP)

Speed Dials (JSP)

Group MWI (JSP)

AutoDialer (JSP)

PhotoDirectory (JSP)

CallerInfo (JSP)

PushAuthenticate (ASP)

ScreenShot (ASP)

Integrating RS-232 devices with IP Telephony Applications (OtherApps)

PNGViewer (ASP)

Keyboard (ASP)

MultiDirectory (ASP)

Phone Push Step and Subsystem (Cisco Unified Contact Center Express / CRS)

## Sample Services Requirements

The following list contains the items that are required for the sample services to work properly:

Microsoft IIS 4.0 or later (for ASP sample services)

Sun J2SE 1.4.2 or later and Tomcat 4.0 or later (for JSP sample services)

Internet Connection to external websites like Yahoo.com, Cnn.com etc.

Cisco Unified Communications Manager 4.1(2) or later.

PhoneOS 2.1(1) or later (Only for Cisco Video Phone 8875 and Cisco Desk Phone 9800 Series)

Cisco IP Phones or Wireless Phones that supports XML services

The setup program installs a CiscoServices web project to c:\CiscoIpServices directory. The sample services are copied to
                              c:\CiscoIpServices\Services subdirectory, and IIS and WSH example codes are provided. The web server already senses these
                              services and you do not require further administration. You can view or edit all the source code with any text editor. For
                              additional documentation, go to this directory: c:\CiscoIpServices\Documentation. Find tools to help develop services in c:\CiscoIpServices\Tools.