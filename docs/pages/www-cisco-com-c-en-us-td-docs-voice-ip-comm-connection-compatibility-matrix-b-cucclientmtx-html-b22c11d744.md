---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-compatibility-matrix-b-cucclientmtx-html-b22c11d744
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html
retrieved_at: 2026-08-16T18:48:44.134651+00:00
---

Compatibility Matrix for Cisco Unity Connection

# Compatibility Matrix for Cisco Unity Connection

### Download Options

Updated: December 18, 2023

# Compatibility
            	 Matrix for Cisco Unity Connection

This document describes different
               		combinations of the softwares, such as operating systems and web browsers to
               		access voicemails using various client applications. It also provides the
               		information on different version combination for SCCP, SIP, and video
               		integration of Cisco Unity Connection with Cisco Unified Communications
               		Manager.

## Client
               	 Compatibility Matrix for Cisco Unity Connetion

This section
                  		describes the various combinations of operating systems, client applications,
                  		and web browsers installed on user workstations to access Cisco Unity
                  		Connection web tools and client applications in all versions of Unity
                  		Connection and Cisco Business Edition 6000/ 7000.

- For user workstation and
                                 			 administrator workstation requirements in Unity Connection, see the applicable
                                 			 version of System
                                    				Requirements for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-guides-list.html .

- For user workstation and
                                 			 administrator workstation requirements in Cisco Business Edition 6000 at http://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/products-installation-guides-list.html .

### Matrices for Unity Connection 15 and Cisco Business Edition 6000/7000

This section provides the compatibility matrices of the different operating systems of Unity Connection 15 and Cisco Business
                     Edition 6000/7000 with the following web applications or clients:

- Cisco ViewMail for Microsoft Outlook

- Web Inbox

- Mini Web Inbox

- IMAP Clients

- Messaging Assistant and Personal Call Transfer Rules

- Cisco Unity Connection Administration

#### Browser Support for Unity Connection 15

Consider the following points with reference to different Unity Connection applications:

Web Inbox

- Cisco Unity Connection uses Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in WebInbox.

- In Internet Explorer, the message Only secure content is displayed , arises when you visit a website that contains mixed content i.e. encrypted https and non-encrypted http on the same web
                                 page. On this message window when you select the Show all content button, auto refresh works fine.

- In Firefox, when you select the security shield in the web address bar and select Disable protection mode , auto refresh works fine.

- In Chrome, when you select the security shield in the web address bar and select Load unsafe script , auto refresh works fine.

Mini Web Inbox

- Cisco Unity Connection uses Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in Mini Web Inbox.

- Make sure the trusted certificate of the certification authority is added to the Trusted Root Store on the user workstations
                           in order to access the notifications via email and the voice message via Mini Web Inbox. For more information on how to configure
                           the trusted certificate on Unity Connection, see the " Securing the Connection between Cisco Unity Connection, Cisco Unified Communications Manager, and IP Phones " chapter of Security Guide for Cisco Unity Connection, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15ucsecx.html .

- Make sure to perform the steps to configure the HTML notification on user workstation. For more information on how to configure
                           the HTML notifications, see the " Configuring Unity Connection for HTML-based Message Notification " section of the "Configuring an Email Account to Access Cisco Unity Connection Voice Messages" chapter of the User Workstation Setup Guide for Cisco Unity Connection, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user_setup/guide/b_15cucuwsx.html .

For more information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco Unity Connection Mini Web Inbox Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/quick_start/guide/b_15cucqsgminiinbox.html .

#### Supported Version Combinations of Operating Systems, Web Browsers, IMAP Clients and ViewMail Applications

Supported Operating System

Supported Browser

IMAP Clients

ViewMail Application (Compatibility with version - 15)

Windows 11

(32-bit and 64-bit)

Professional

Enterprise

118

118 ESR

Chrome

117

Edge 1

117

118

118 ESR

117

117

2019

2016

2013

115

115 ESR

Outlook Desktop Application 3

2019 4

2016

2013

Windows 10 5

(32-bit and 64-bit)

Professional

Enterprise

118

118 ESR

Chrome

117

Edge 6

117

118

118 ESR

117

117

2019

2016

2013

115

115 ESR

Outlook Desktop Application 8

2019 9

2016

2013

Mac OS X 13 ( macOS Ventura)

Safari

17

Safari 9

17

Outlook

2016

Apple Mail

14

Thunderbird

115

115 ESR

Not Supported

1 For successful audio recording through Windows computer on Edge browser, make sure the trusted certificate of the certification
                           authority is added to the Trusted Root Store of the browser.

2 Firefox does not display any pop-up for muted microphone. Make sure to unmute the microphone while recording with Media Player
                           using computer device.

3 The desktop version of outlook is integrated with either Exchange or Office 365 account in backend.

4 “Inline Forward and Reply” functionality for Outlook 2013 and above, is not supported with ViewMail for Outlook.

5 Windows 10 in the Desktop Mode.

6 For successful audio recording through Windows computer on Edge browser, make sure the trusted certificate of the certification
                           authority is added to the Trusted Root Store of the browser.

7 Firefox does not display any pop-up for muted microphone. Make sure to unmute the microphone while recording with Media Player
                           using computer device.

8 The desktop version of outlook is integrated with either Exchange or Office 365 account in backend.

9 “Inline Forward and Reply” functionality for Outlook 2013 and above, is not supported with ViewMail for Outlook.

#### Supported Version Combinations of Cisco Unity Connection 15, Cisco Unified CM, Cisco Unified CM Session Manager Edition and
                     Cisco Unified CM Express

15, 14, 12.5(1)

### Matrices for Unity Connection 14 and Cisco Business Edition 6000/7000

This section provides the compatibility matrices of the different operating systems of Unity Connection 14 and Cisco Business
                     Edition 6000/7000 with the following web applications or clients:

- Cisco ViewMail for Microsoft Outlook

- Web Inbox

- Mini Web Inbox

- IMAP Clients

- Messaging Assistant and Personal Call Transfer Rules

- Cisco Unity Connection Administration

#### Browser Support for Unity Connection 14

Consider the following points with reference to different Unity Connection applications:

Web Inbox

- Cisco Unity Connection uses Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in WebInbox.

- In Internet Explorer, the message Only secure content is displayed , arises when you visit a website that contains mixed content i.e. encrypted https and non-encrypted http on the same web
                                 page. On this message window when you select the Show all content button, auto refresh works fine.

- In Firefox, when you select the security shield in the web address bar and select Disable protection mode , auto refresh works fine.

- In Chrome, when you select the security shield in the web address bar and select Load unsafe script , auto refresh works fine.

- Cisco Unity Connection uses Web Real-Time Communication (Web RTC) to record voice messages using HTML5 in Mini Web Inbox.

- Make sure the trusted certificate of the certification authority is added to the Trusted Root Store on the user workstations
                              in order to access the notifications via email and the voice message via Mini Web Inbox. For more information on how to configure
                              the trusted certificate on Unity Connection, see the " Securing the Connection between Cisco Unity Connection, Cisco Unified Communications Manager, and IP Phones " chapter of Security Guide for Cisco Unity Connection, Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/security/guide/b_14cucsecx.html .

- Make sure to perform the steps to configure the HTML notification on user workstation. For more information on how to configure
                              the HTML notifications, see the " Configuring Unity Connection for HTML-based Message Notification " section of the "Configuring an Email Account to Access Cisco Unity Connection Voice Messages" chapter of the User Workstation Setup Guide for Cisco Unity Connection, Release 14 available at

For more information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco Unity Connection Mini Web Inbox Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/quick_start/guide/b_14cucqsgminiinbox.html ..

#### Supported Version Combinations of Operating Systems, Web Browsers, IMAP Clients and ViewMail Applications

Supported Operating System

Supported Browser

IMAP Clients

ViewMail Application (Compatibility with version - 14)

ViewMail Application (Compatibility with version - 12.5(3))

Windows 10 10

(32-bit and 64-bit)

Professional

Enterprise

83

83 ESR

Chrome

87

Edge 11

87

83

83 ESR

Internet Explorer

- 11 13

87

87

2019

2016

2013

78

78 ESR

Outlook Desktop Application 14

2019 15

2016

2013

Outlook Desktop Application 5

2019 6

2016

2013

Windows 8.1 16

(32-bit and 64-bit)

Standard

Professional

Enterprise

Firefox

83

83 ESR

Chrome

87

Firefox 3

83

83 ESR

11 4

Chrome

87

Outlook

2019

2016

2013

78

78 ESR

Outlook Desktop Application 5

2019 6

2016

2013

Outlook Desktop Application 5

2019 6

2016

2013

Windows 7

(32-bit and 64-bit)

Standard

Professional

Enterprise

Firefox

83

83 ESR

Chrome

87

Firefox 3

83

83 ESR

Internet Explorer

11 4

Chrome

87

Outlook

2019

2016

2013

Thunderbird

78

78 ESR

Not Supported

Not Supported

Mac OS X 11.0.1 ( macOS Big Sur)

Firefox 17

83

83 ESR

Safari

14

Chrome

87

83

83 ESR

Safari 18

14

Chrome

87

Outlook

2016

Apple Mail

14

Thunderbird

78

78 ESR

Not Supported

Not Supported

Mac OS X 10.15 ( macOS Catalina)

Firefox 10

83

83 ESR

Safari

14

Chrome

87

83

83 ESR

Safari 9

14

Chrome

87

Outlook

2016

Apple Mail

14

Thunderbird

78

78 ESR

Not Supported

Not Supported

10 Windows 10 in the Desktop Mode.

11 For successful audio recording through Windows computer on Edge browser, make sure the trusted certificate of the certification
                              authority is added to the Trusted Root Store of the browser.

12 Firefox does not display any pop-up for muted microphone. Make sure to unmute the microphone while recording with Media Player
                              using computer device.

13 On IE11 browser, recording and playback in Media Player gets reset when you change the volume.

14 The desktop version of outlook is integrated with either Exchange or Office 365 account in backend.

15 “Inline Forward and Reply” functionality for Outlook 2013 and above, is not supported with ViewMail for Outlook.

16 Windows 8.1 in the Desktop Mode.

17 On Mac OS X, computer record and play is not available on Safari and Firefox for Web Inbox and Mini Web Inbox. Only telephone
                              record and play is available.

18 On Mac OS X, Media Player does not support computer as recording device with Safari. For playback using computer device, go
                              to Safari > Preferences > Websites > AutoPlay and make sure that "Allow All Auto Play" option is selected under "When visiting
                              other websites " drop down list.

#### Supported Version Combinations of Cisco Unity Connection 14, Cisco Unified CM, Cisco Unified CM Session Manager Edition and
                     Cisco Unified CM Express

14, 12.5(1), 12.0(1), 11.5(1)

### Matrices for Unity
                  	 Connection 12.x and Cisco Business Edition 6000/7000

This section provides the compatibility matrices of the different
                     		operating systems of Unity Connection 12.x and Cisco Business Edition 6000/7000
                     		with the following web applications or clients:

- Cisco ViewMail for Microsoft
                        		  Outlook

- Web Inbox

- Mini Web Inbox

- IMAP Clients

- Messaging Assistant and
                        		  Personal Call Transfer Rules

- Cisco Unity Connection
                        		  Administration

#### Browser Support for Unity Connection 12.x

Consider the following points with reference to different Unity Connection applications:

Web Inbox

- Cisco Unity Connection uses Flash Player for recording voice messages through Web Inbox. However, Adobe has announced end
                           of life for Flash Player. Hence Cisco Unity Connection 12.5(1) Service Update 3 and later, replaces the Flash Player with
                           Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in WebInbox.

- In Internet Explorer, the message Only secure content is displayed , arises when you visit a website that contains mixed content i.e. encrypted https and non-encrypted http on the same web
                                 page. On this message window when you select the Show all content button, auto refresh works fine.

- In Firefox, when you select the security shield in the web address bar and select Disable protection mode , auto refresh works fine.

- In Chrome, when you select the security shield in the web address bar and select Load unsafe script , auto refresh works fine.

Mini Web Inbox

- Cisco Unity Connection uses Flash Player for recording voice messages through Mini Web Inbox. However, Adobe has announced
                           end of life for Flash Player. Hence Cisco Unity Connection 12.5(1) Service Update 3 and later, replaces the Flash Player with
                           Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in Mini Web Inbox.

- Make sure the trusted certificate of the certification authority is added to the Trusted Root Store on the user workstations
                           in order to access the notifications via email and the voice message via Mini Web Inbox. For more information on how to configure
                           the trusted certificate on Unity Connection, see the " Securing the Connection between Cisco Unity Connection, Cisco Unified Communications Manager, and IP Phones " chapter of the Security Guide for Cisco Unity Connection, Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/b_12xcucsecx.html .

- Make sure to perform the steps to configure the HTML notification on user workstation. For more information on how to configure
                           the HTML notifications, see the " Configuring Unity Connection for HTML-based Message Notification " section of the "Configuring an Email Account to Access Cisco Unity Connection Voice Messages" chapter of the User Workstation Setup Guide for Cisco Unity Connection, Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user_setup/guide/b_12xcucuwsx.html .

For more information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco Unity Connection Mini Web Inbox available
                                 at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/quick_start/guide/b_12xcucqsgminiinbox.html .

Cisco Unity Connection Administration , Messaging Assistant and Personal Call Transfer Rule

With Unity Connection 12.0(1) SU2 and later, Media Player also supports the computer device along with phone to provide the
                              functionality of play, record, upload and download.

#### Supported Version
                     	 Combinations of Operating Systems, Web Browsers, IMAP Clients and ViewMail
                     	 Applications

Supported Operating System

Supported Browser

IMAP Clients

ViewMail Application (Compatibility with version - 12.5(3))

ViewMail Application (Compatibility with version - 12.5(2))

Windows 10 19

(32-bit and 64-bit)

Professional

Enterprise

61

61 ESR

Chrome

68

Edge 20

42

61

61 ESR

Internet Explorer

- 11 22

68

42

2016

2013

2010

IBM Notes

9 23

60

60 ESR

Outlook Desktop Application 24

2019 25

2016

2013

Outlook Desktop Application 15

2019 16

2016

2013

Windows 8.1 26

(32-bit and 64-bit)

Standard

Professional

Enterprise

Firefox

61

61 ESR

Chrome

68

Firefox 12

61

61 ESR

11 13

Chrome

68

Outlook

2016

2013

2010

IBM Notes

9 14

60

60 ESR

Outlook Desktop Application 15

2019 16

2016

2013

Outlook Desktop Application 15

2019 16

2016

2013

Windows 7

(32-bit and 64-bit)

Standard

Professional

Enterprise

Firefox

61

61 ESR

Chrome

68

Firefox 12

61

61 ESR

Internet Explorer

11 13

Chrome

68

Outlook

2016

2013

2010

IBM Notes

9 14

Thunderbird

60

60 ESR

Not Supported

Outlook Desktop Application 15

2019 16

2016

2013

Mac OS X 10.13 ( macOS High Sierra )

Firefox 27

60

60 ESR

Safari

12

Chrome

68

60

60 ESR

Safari 28

12

Chrome

68

Outlook

2016

Apple Mail

11.5

Thunderbird

52

52 ESR

Not Supported

Not Supported

Mac OS X 10.12 (macOS Sierra)

Firefox 9

60

60 ESR

Safari

10

Chrome

68

Firefox 12

60

60 ESR

Safari 19

10

Chrome

68

Outlook

2016

Apple Mail

10.3

Thunderbird

60

60 ESR

Not Supported

Not Supported

Mac OS X 10.11 (EI Capitan)

Firefox 9

60

60 ESR

Safari

10

Chrome

68

Firefox 12

60

60 ESR

Safari 19

10

Chrome

68

Outlook

2016

Apple Mail

10.3

Thunderbird

60

60 ESR

Not Supported

Not Supported

19 Windows 10 in the Desktop Mode.

20 For successful audio recording through Windows computer on Edge browser, make sure the trusted certificate of the certification
                              authority is added to the Trusted Root Store of the browser.

21 Firefox does not display any pop-up for muted microphone. Make sure to unmute the microphone while recording with Media Player
                              using computer device.

22 On IE11 browser, recording and playback in Media Player gets reset when you change the volume.

23 IBM Notes 9 with Fix Pack 9 is supported in Unity Connection.

24 The desktop version of outlook is integrated with either Exchange or Office 365 account in backend.

25 “Inline Forward and Reply” functionality for Outlook 2013 and above, is not supported with ViewMail for Outlook.

26 Windows 8.1 in the Desktop Mode.

27 On Mac OS X, computer record and play is not available on Safari and Firefox for Web Inbox and Mini Web Inbox. Only telephone
                              record and play is available.

28 On Mac OS X, Media Player does not support computer as recording device with Safari. For playback using computer device, go
                              to Safari > Preferences > Websites > AutoPlay and make sure that "Allow All Auto Play" option is selected under "When visiting
                              other websites " drop down list.

#### Supported Version Combinations of Cisco Unity Connection 12.x, Cisco Unified CM, Cisco Unified CM Session Manager Edition
                     and Cisco Unified CM Express

12.5(1), 12.0(1), 11.5(1)

#### Supported Version Combinations of Operating Systems and Web Browsers for Unity Connection 12.5(1) SU3

Supported Operating System

Supported Browser for Web Inbox and Mini Web Inbox

(64-bit)

Enterprise

Edge

44

Chrome

81

Firefox

73

(64-bit)

Enterprise

Edge

44

Chrome

81

Firefox

73

Mac OS X 10.12.6

Edge

44

Chrome

81

Firefox

73

Safari

12

### Unity Connection Prior Versions

For information on compatibility matrix of Unity Connection versions 10.x and 11.x, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx_older.html

### IMAP Solution
                  	 Support Statement

Cisco supports the server-side portion of the IMAP solution only; Cisco
                     		neither provides nor supports IMAP client software. All major IMAP client
                     		software release versions must be qualified by Cisco in order to be supported;
                     		any minor, maintenance or hot fix releases are automatically supported unless
                     		otherwise stated.

Cisco provides all testing, qualification, and configuration
                     		documentation of IMAP client software as a courtesy. For IMAP client support,
                     		contact the software vendor or the designated IMAP client software support
                     		channel for your organization.

### Third Party
                  	 Plugins Support with Cisco ViewMail for Microsoft Outlook Statement

Cisco does not claim any compliance to third party proprietary plug-ins
                     		with Cisco ViewMail for Microsoft Outlook. However, Cisco provides support for
                     		Cisco plugins software with Cisco ViewMail for Microsoft Outlook.

For issues with any third-party products contact the third-party vendor
                     		for support.

## SCCP Compatibility
               	 Matrix

This section
                  		describes the supported version combinations of Unity Connection and Cisco
                  		Unified CM or Cisco Unified CM Express for SCCP integration.

The supported
                           		version combinations are determined by testing. While other combinations may
                           		provide acceptable results to customers, Cisco must test or approve these
                           		combinations before they will be supported.

Cisco Unified CM
                  		support patch (sp) releases have the same compatibility as the base release. In
                  		addition, rereleased versions—for example, 8.x(xa) rereleased as 8.x(xb)—are
                  		assumed to have the same compatibility unless noted.

Unity Connection
                  		service releases (SR) have the same compatibility as the base release.

### Supported Version Combinations for Cisco Unity Connection,Cisco Unified Communications Manager and Cisco Unified Communications
                  Manager Express

### Supported Version
                  	 Combinations of Cisco Unity Connection SRSV and Cisco Unified SRST

MWI is not
                                 		  supported in Cisco Unified SRST mode. For more information on MWI, see the
                                 		  “ Configuring Message Waiting Indication (Cisco Unified SCCP SRST
                                    			 Routers) ” section of the “Integrating Voice Mail with Cisco Unified
                                 		  SRST” chapter of the Cisco Unified SCCP and SIP SRST System Administrator Guide
                                 		  (All Versions) guide at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/
                                    			 SCCP_and_SIP_SRST_Admin_Guide.html .

## SIP Trunk
               	 Compatibility Matrix

This section describes the supported version combinations for Unity
                  		Connection and Cisco Unified Communications Manager, for Unity Connection and
                  		Cisco Unified Communications Manager Session Manager Edition, and for Unity
                  		Connection and Cisco Unified Communications Manager Express when they are
                  		integrated through a SIP trunk.

The supported version combinations are determined by testing. While
                              		  other combinations may provide acceptable results to customers, Cisco must test
                              		  or approve these combinations before they will be supported. Cisco Business
                              		  Edition 6000/7000 is supported for SIP trunk integrations with Unity
                              		  Connection.

Cisco Unified CM support patch (sp) releases have the same compatibility
                  		as the base release. In addition, rereleased versions—for example, 7.x(xa)
                  		rereleased as 7.x(xb)—are assumed to have the same compatibility unless noted.

Unity Connection service releases (SR) have the same compatibility as
                  		the base release.

### Supported Version Combinations of Cisco Unity Connection, Cisco Unified CM,Cisco Unified CM Session Manager Edition and Cisco
                  Unified CM Express

### Supported Version
                  	 Combinations of Cisco Unity Connection SRSV and Cisco Unified SRST

## Video
               	 Compatibility Matrix

Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                              feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html

In Unity Connection 10.0(1) and
                  		later, to record or play video greetings, you need to integrate video
                  		endpoints, Cisco Unified CM, and Cisco MediaSense. This section describes the
                  		supported version combinations to configure the video greetings feature.

### Supported Version
                  	 Combinations for Video Endpoints with SIP

While using Video Messaging on Cisco Jabber, you may experience
                                    			 some inconsistent behavior with Jabber user interface.

### Supported Version
                  	 Combinations for Video Endpoints with SCCP

### Supported Version Combinations of Unity Connection, Cisco MediaSense and Cisco Unified Communications Manager

29 For successful functioning of collaboration features, Cisco Unity Connection and Cisco Unified Communications Manager versions
                        should be same.

## IMAP Solution
               	 Support Statement

Cisco supports the server-side portion of the IMAP solution only; Cisco
                  		neither provides nor supports IMAP client software. All major IMAP client
                  		software release versions must be qualified by Cisco in order to be supported;
                  		any minor, maintenance or hot fix releases are automatically supported unless
                  		otherwise stated.

Cisco provides all testing, qualification, and configuration
                  		documentation of IMAP client software as a courtesy. For IMAP client support,
                  		contact the software vendor or the designated IMAP client software support
                  		channel for your organization.

## Third Party
               	 Plugins Support with Cisco ViewMail for Microsoft Outlook Statement

Cisco does not claim any compliance to third party proprietary plug-ins
                  		with Cisco ViewMail for Microsoft Outlook. However, Cisco provides support for
                  		Cisco plugins software with Cisco ViewMail for Microsoft Outlook.

For issues with any third-party products contact the third-party vendor
                  		for support.

| Note | For user workstation and
                                 			 administrator workstation requirements in Unity Connection, see the applicable
                                 			 version of System
                                    				Requirements for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-guides-list.html . For user workstation and
                                 			 administrator workstation requirements in Cisco Business Edition 6000 at http://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/products-installation-guides-list.html . |
|---|---|

| Note | For more information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco Unity Connection Mini Web Inbox Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/quick_start/guide/b_15cucqsgminiinbox.html . |
|---|---|

| Supported Operating System | Supported Browser | IMAP Clients | ViewMail Application (Compatibility with version - 15) |
|---|---|---|---|
| Web Inbox and Mini Web Inbox | Cisco Unity Connection Administration, Messaging Assistant and Personal Call Transfer Rules |
| Windows 11 (32-bit and 64-bit) Professional Enterprise | Firefox 118 118 ESR Chrome 117 Edge 1 117 | Firefox 2 118 118 ESR Chrome 117 Edge 117 | Outlook 2019 2016 2013 Thunderbird 115 115 ESR | Outlook Desktop Application 3 2019 4 2016 2013 |
| Windows 10 5 (32-bit and 64-bit) Professional Enterprise | Firefox 118 118 ESR Chrome 117 Edge 6 117 | Firefox 7 118 118 ESR Chrome 117 Edge 117 | Outlook 2019 2016 2013 Thunderbird 115 115 ESR | Outlook Desktop Application 8 2019 9 2016 2013 |
| Mac OS X 13 ( macOS Ventura) | Safari 17 | Safari 9 17 | Outlook 2016 Apple Mail 14 Thunderbird 115 115 ESR | Not Supported |

| Cisco Unity Connection | Cisco Unified CM/ Cisco Unified CM Session Manager Edition/ Cisco Unified CM Express |
|---|---|
| 15 | 15, 14, 12.5(1) |

| Note | For more information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco Unity Connection Mini Web Inbox Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/quick_start/guide/b_14cucqsgminiinbox.html .. |
|---|---|

| Supported Operating System | Supported Browser | IMAP Clients | ViewMail Application (Compatibility with version - 14) | ViewMail Application (Compatibility with version - 12.5(3)) |
|---|---|---|---|---|
| Web Inbox and Mini Web Inbox | Cisco Unity Connection Administration, Messaging Assistant and Personal Call Transfer Rules |
| Windows 10 10 (32-bit and 64-bit) Professional Enterprise | Firefox 83 83 ESR Chrome 87 Edge 11 87 | Firefox 12 83 83 ESR Internet Explorer 11 13 Chrome 87 Edge 87 | Outlook 2019 2016 2013 Thunderbird 78 78 ESR | Outlook Desktop Application 14 2019 15 2016 2013 | Outlook Desktop Application 5 2019 6 2016 2013 |
| Windows 8.1 16 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 83 83 ESR Chrome 87 | Firefox 3 83 83 ESR Internet Explorer 11 4 Chrome 87 | Outlook 2019 2016 2013 Thunderbird 78 78 ESR | Outlook Desktop Application 5 2019 6 2016 2013 | Outlook Desktop Application 5 2019 6 2016 2013 |
| Windows 7 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 83 83 ESR Chrome 87 | Firefox 3 83 83 ESR Internet Explorer 11 4 Chrome 87 | Outlook 2019 2016 2013 Thunderbird 78 78 ESR | Not Supported | Not Supported |
| Mac OS X 11.0.1 ( macOS Big Sur) | Firefox 17 83 83 ESR Safari 14 Chrome 87 | Firefox 3 83 83 ESR Safari 18 14 Chrome 87 | Outlook 2016 Apple Mail 14 Thunderbird 78 78 ESR | Not Supported | Not Supported |
| Mac OS X 10.15 ( macOS Catalina) | Firefox 10 83 83 ESR Safari 14 Chrome 87 | Firefox 3 83 83 ESR Safari 9 14 Chrome 87 | Outlook 2016 Apple Mail 14 Thunderbird 78 78 ESR | Not Supported | Not Supported |

| Cisco Unity Connection | Cisco Unified CM/ Cisco Unified CM Session Manager Edition/ Cisco Unified CM Express |
|---|---|
| 14 | 14, 12.5(1), 12.0(1), 11.5(1) |

| Note | For more information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco Unity Connection Mini Web Inbox available
                                 at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/quick_start/guide/b_12xcucqsgminiinbox.html . |
|---|---|

| Supported Operating System | Supported Browser | IMAP Clients | ViewMail Application (Compatibility with version - 12.5(3)) | ViewMail Application (Compatibility with version - 12.5(2)) |
|---|---|---|---|---|
| Web Inbox and Mini Web Inbox | Cisco Unity Connection Administration, Messaging Assistant and Personal Call Transfer Rules |
| Windows 10 19 (32-bit and 64-bit) Professional Enterprise | Firefox 61 61 ESR Chrome 68 Edge 20 42 | Firefox 21 61 61 ESR Internet Explorer 11 22 Chrome 68 Edge 42 | Outlook 2016 2013 2010 IBM Notes 9 23 Thunderbird 60 60 ESR | Outlook Desktop Application 24 2019 25 2016 2013 | Outlook Desktop Application 15 2019 16 2016 2013 |
| Windows 8.1 26 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 61 61 ESR Chrome 68 | Firefox 12 61 61 ESR Internet Explorer 11 13 Chrome 68 | Outlook 2016 2013 2010 IBM Notes 9 14 Thunderbird 60 60 ESR | Outlook Desktop Application 15 2019 16 2016 2013 | Outlook Desktop Application 15 2019 16 2016 2013 |
| Windows 7 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 61 61 ESR Chrome 68 | Firefox 12 61 61 ESR Internet Explorer 11 13 Chrome 68 | Outlook 2016 2013 2010 IBM Notes 9 14 Thunderbird 60 60 ESR | Not Supported | Outlook Desktop Application 15 2019 16 2016 2013 |
| Mac OS X 10.13 ( macOS High Sierra ) | Firefox 27 60 60 ESR Safari 12 Chrome 68 | Firefox 12 60 60 ESR Safari 28 12 Chrome 68 | Outlook 2016 Apple Mail 11.5 Thunderbird 52 52 ESR | Not Supported | Not Supported |
| Mac OS X 10.12 (macOS Sierra) | Firefox 9 60 60 ESR Safari 10 Chrome 68 | Firefox 12 60 60 ESR Safari 19 10 Chrome 68 | Outlook 2016 Apple Mail 10.3 Thunderbird 60 60 ESR | Not Supported | Not Supported |
| Mac OS X 10.11 (EI Capitan) | Firefox 9 60 60 ESR Safari 10 Chrome 68 | Firefox 12 60 60 ESR Safari 19 10 Chrome 68 | Outlook 2016 Apple Mail 10.3 Thunderbird 60 60 ESR | Not Supported | Not Supported |

| Cisco Unity Connection | Cisco Unified CM/ Cisco Unified CM Session Manager Edition/ Cisco Unified CM Express |
|---|---|
| 12.5 | 12.5(1), 12.0(1), 11.5(1) |

| Supported Operating System | Supported Browser for Web Inbox and Mini Web Inbox |
|---|---|
| Window 10 (64-bit) Enterprise | Edge 44 Chrome 81 Firefox 73 |
| Windows 7 (64-bit) Enterprise | Edge 44 Chrome 81 Firefox 73 |
| Mac OS X 10.12.6 | Edge 44 Chrome 81 Firefox 73 Safari 12 |

| Note | The supported
                           		version combinations are determined by testing. While other combinations may
                           		provide acceptable results to customers, Cisco must test or approve these
                           		combinations before they will be supported. |
|---|---|

| Cisco Unity Connection | Cisco Unified CM/Cisco Unified CM Express |
|---|---|
| 12.0(1) | 12.0(1),11.5(1), 10.5(2) |
| 11.5(1) | 11.5(1), 10.5(2) |
| 10.5(2) | 10.5(2) |

| Cisco Unity Connection SRSV | Cisco Unified SRST/CME-SRST | Cisco Unified E-SRST |
|---|---|---|
| 9.1(1) and later | 8.6 and higher | 8.6 and higher |

| Note | MWI is not
                                 		  supported in Cisco Unified SRST mode. For more information on MWI, see the
                                 		  “ Configuring Message Waiting Indication (Cisco Unified SCCP SRST
                                    			 Routers) ” section of the “Integrating Voice Mail with Cisco Unified
                                 		  SRST” chapter of the Cisco Unified SCCP and SIP SRST System Administrator Guide
                                 		  (All Versions) guide at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/
                                    			 SCCP_and_SIP_SRST_Admin_Guide.html . |
|---|---|

| Note | The supported version combinations are determined by testing. While
                              		  other combinations may provide acceptable results to customers, Cisco must test
                              		  or approve these combinations before they will be supported. Cisco Business
                              		  Edition 6000/7000 is supported for SIP trunk integrations with Unity
                              		  Connection. |
|---|---|

| Cisco Unity Connection | Cisco Unified CM/ Cisco Unified CM Session Manager Edition/ Cisco Unified CM Express |
|---|---|
| 12.0(1) | 12.0(1), 11.5(1), 10.5(2) |
| 11.5(1) | 11.5(1), 10.5(2) |
| 10.5(2) | 10.5(2) |

| Cisco Unity Connection SRSV | Cisco Unified SRST/CME-SRST | Cisco Unified E-SRST |
|---|---|---|
| 9.1(1) and later | 8.6 and higher | 8.6 and higher |

| Note | Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                              feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html |
|---|---|

| Video EndPoints | Supported Software |
|---|---|
| 8865 | Phone Load: sip8845_65.14-2-1-0101-26 |
| 8861 | Phone Load: sip88xx.14-2-1-0101-26 |
| 8851 | Phone Load: sip88xx.14-2-1-0101-26 |
| 8845 | Phone Load: sip8845_65.14-2-1-0101-26 |
| 8832 | Phone Load: sip8832.14-2-1-0101-26 |
| 7861 | Phone Load: sip78xx.14-2-1-0101-26 |
| 7841 | Phone Load: sip78xx.11-0-1-11dev |
| DX80 | Phone Load: sipdx80.ce-9.15.3.22-8ebef840687-2021-06-16 |

| Note | While using Video Messaging on Cisco Jabber, you may experience
                                    			 some inconsistent behavior with Jabber user interface. |
|---|---|

| Video Enabled EndPoints | Software Supported |
|---|---|
| 8945 | Phone Load: SCCP.9.3.4.17 and later |
| 7975 | Phone Load: SCCP.75.9-3-1SR2-1S and later |
| 7945 | Phone Load: SCCP4.5.9-3-1SR2-1S and later |
| 6945 | Phone Load: SCCP9-3-1-3 and later |
| 6941 | Phone Load: 9-3-3-2 and later |
| 6921 | Phone Load: SCCP9.2.1.0 and later |

| Cisco Unity Connection | Cisco MediaSense | Cisco Unified Communications Manager |
|---|---|---|
| 10.5(2) and later 29 | 11.5(1) | 10.x and later |