---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-compatibility-matrix-b-cucclientmtx-older-html-4507755c67
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx_older.html
retrieved_at: 2026-08-17T02:41:56.821899+00:00
---

Compatibility Matrix for Cisco Unity Connection

# Compatibility Matrix for Cisco Unity Connection

### Download Options

Updated: December 18, 2023

First Published: December 18, 2023

Last Updated: December 18, 2023

# Compatibility
            	 Matrix for Cisco Unity Connection

This document describes different
               		combinations of the softwares, such as operating systems and web browsers to
               		access voicemails using various client applications. It also provides the
               		information on different version combination for SCCP, SIP, and video
               		integration of Cisco Unity Connection with Cisco Unified Communications
               		Manager.

## Matrices for Unity
               	 Connection 11.x and Cisco Business Edition 6000/7000

This section
                  		provides the compatibility matrices of the different operating systems of Unity
                  		Connection 11.x and Cisco Business Edition 6000/7000 with the following web
                  		applications or clients:

- Cisco ViewMail for
                     		  Microsoft Outlook

- Web Inbox

- Mini Web Inbox

- IMAP Clients

- Messaging Assistant and
                     		  Personal Call Transfer Rules

- Cisco Unity Connection
                     		  Administration

### Browser Support
                  	 for Unity Connection 11.x

Consider the
                     		following points with reference to different Unity Connection applications:

Web Inbox

- Cisco Unity Connection uses Flash Player for recording voice messages through Web Inbox. However, Adobe has announced end
                        of life for Flash Player. Hence Cisco Unity Connection 11.5(1) Service Update 8 and later, replaces the Flash Player with
                        Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in WebInbox.

- In Internet Explorer, the message Only secure content is displayed , arises when you visit a website that contains mixed content i.e. encrypted https and non-encrypted http on the same web
                              page. On this message window when you select the Show all content button, auto refresh works fine.

- In Firefox, when you select the security shield in the web address bar and select Disable protection mode , auto refresh works fine.

- In Chrome, when you select the security shield in the web address bar and select Load unsafe script , auto refresh works fine.

Mini Web Inbox

- Cisco Unity Connection uses Flash Player for recording voice messages through Mini Web Inbox. However, Adobe has announced
                        end of life for Flash Player. Hence Cisco Unity Connection 11.5(1) Service Update 8 and later, replaces the Flash Player with
                        Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in Mini Web Inbox.

- Make sure the trusted
                        		  certificate of the certification authority is added to the Trusted Root Store
                        		  on the user workstations in order to access the notifications via email and the
                        		  voice message via Mini Web Inbox. For more information on how to configure the
                        		  trusted certificate on Unity Connection, see the " Securing the Connection
                           			 between Cisco Unity Connection, Cisco Unified Communications Manager, and IP
                           			 Phones " chapter of the Security Guide for Cisco Unity Connection,
                        		  Release 11.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/security/b_11xcucsecx.html .

- Make sure to perform the
                        		  steps to configure the HTML notification on user workstation. For more
                        		  information on how to configure the HTML notifications, see the " Configuring Unity Connection
                           			 for HTML-based Message Notification " section of the "Configuring an
                        		  Email Account to Access Cisco Unity Connection Voice Messages" chapter of the
                        		  User Workstation Setup Guide for Cisco Unity Connection, Release 11.x,
                        		  available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/user_setup/guide/b_11xcucuwsx.html .

For more
                              		information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco
                              		Unity Connection Mini Web Inbox available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/quick_start/guide/b_11xcucqsgminiinbox.html .

Cisco Unity Connection
                        		  Administration , Messaging
                        		  Assistant and Personal Call
                        		  Transfer Rule

With Unity Connection 11.5(1) SU5 and later, Media Player also supports the computer device along with phone to provide the
                           functionality of play, record, upload and download. To see the compatibility of Media Player with different browsers, refer Supported Version Combinations of Operating Systems and Web Browsers for Unity Connection 11.5(1) SU5 ".

For supported versions of  IMAP client and ViewMail Application, refer Table 2

- With Unity Connection 11.5(1) and later, a new Media Player is introduced that provides the functionality of play, record,
                        upload and download using phone device. Media Player is compatible with all the browsers, given in the Table.

- For Unity Connection 11.0
                        		  (1) and earlier , it is recommended to use Java 8 update 79 with Cisco Unity
                        		  Connection Administration, Messaging Assistant and Personal Call Transfer
                        		  Rules.

### Supported Version
                  	 Combinations of Operating Systems, Web Browsers, IMAP Clients and ViewMail
                  	 Applications

ViewMail Application (Compatibility with version - 12.5(3))

ViewMail Application (Compatibility with version - 12.5(2))

(32-bit and 64-bit)

- Professional

- Enterprise

- 45

- 45 ESR

- 49

- 20

- 45

- 45 ESR

- 11

- 49 2

- 20 3

- 2016

- 2013 4

- 2010 5

- 2007

- 2012

- 9 7

- 38

- 38 ESR

Outlook Desktop Application 8

2019 9

2016 28

2013

Outlook Desktop Application 27

2019

2016 28

2013 28

(32-bit and 64-bit)

- Standard

- Professional

- Enterprise

- 45

- 45 ESR

- 49

- 45

- 45 ESR

- 11

- 49 21

- 2016

- 2013 23

- 2010 24

- 2007

- 2012

- 9 26

- 38

- 38 ESR

Same as above

(32-bit and 64-bit)

- Standard

- Professional

- Enterprise

- 45

- 45 ESR

- 49

- 45

- 45 ESR

- 11

- 49 21

- 2016

- 2013 23

- 2010 24

- 2007

- 2012

- 9 26

- 38

- 38 ESR

Not Supported

- 45

- 45 ESR

- 9

- 49

- 45

- 45 ESR

- 9

- 49 21

- 2011

- 9

- 45

- 45 ESR

Not Applicable

- 45

- 45 ESR

- 8

- 49

- 45

- 45 ESR

- 8

- 49 21

- 2011

- 8

- 45

- 45 ESR

Not Applicable

- 45

- 45 ESR

- 7

- 49

- 45

- 45 ESR

- 7

- 49 21

- 2011

- 7

- 45

- 45 ESR

Not Applicable

1 For successful audio recording through Windows computer on Edge browser, make sure the trusted certificate of the certification
                           authority is added to the Trusted Root Store of the browser.

2 Media Master for Unity Connection 11.0 (1) and earlier, is compatible only with chrome 42 and earlier versions that provide
                           the NPAPI plugin support. In Chrome Version 42, you need to perform the steps mentioned in " Configuring Chrome 42 section to continue using NPAPI plugins. Unity Connection supports new Media Player with chrome 45 and later versions.

3 Media Master for Unity Connection 11.0 (1) and earlier, is not compatible with Edge browser.

4 With Outlook 2013, it is mandatory to install KB2889859 using http://support2.microsoft.com/kb/2889859 . The delete operation may not work with Outlook 2013.

5 Outlook 2010 will stop working if you install KB2956203 update.

6 Lotus Notes is supported in the Online Mode only but the mark read operation from Web Inbox to Lotus Notes is not synchronized.
                           Also, the delete operation supports only the hard delete of messages in Lotus Notes.

7 Lotus Note 9 with Fix Pack 3 is supported in Unity Connection.

8 The desktop version of outlook is integrated with either Exchange or Office 365 account in backend.

9 “Inline Forward and Reply” functionality for Outlook 2013 and above, is not supported with ViewMail for Outlook.

10 Windows 8.1 in the Desktop Mode.

11 On Mac OS X, computer record and play is not available on Safari and Firefox for Web Inbox and Mini Web Inbox. Only telephone
                           record and play is available.

- It is recommended that
                                          				  for 32-bit browsers, the java version should be 32-bit only. 32 bit browser
                                          				  does not support 64 bit java version.

- The IMAP clients support
                                          				  both the IPv4 and IPv6 addresses. However, the IPv6 address works only when the
                                          				  Unity Connection platform is configured in Dual (IPv4/IPv6) mode.

### Configuring Chrome 42

To enable NPAPI in Chrome 42, do the following:

- Enter the following URL in the address bar: chrome://flags/#enable-npapi

- Click the Enable link under Enable NPAPI Mac, Windows section to enable NPAPI configuration option.

- Click the Relaunch Now button at the bottom of the configuration page.

### Supported Version Combinations of Operating Systems and Web Browsers for Unity Connection 11.5(1) SU5

Supported Operating System

Supported Browser for Web Inbox and Mini Web Inbox

Supported Browser for Cisco Unity Connection Administration, Messaging Assistant and Personal Call Transfer Rules

(32-bit and 64-bit)

Professional

Enterprise

Firefox

60

60 ESR

Chrome

67

Edge 12

40

Firefox 13

60

60 ESR

Chrome

67

Edge

40

(32-bit and 64-bit)

Standard

Professional

Enterprise

Firefox

60

60 ESR

Chrome

67

Firefox 32

60

60 ESR

Chrome

67

(32-bit and 64-bit)

Standard

Professional

Enterprise

Firefox

60

60 ESR

Chrome

67

Firefox 32

60

60 ESR

Chrome

67

Mac OS X 10.12 (Sierra)

Firefox 15

60

60 ESR

Safari

11

Chrome

67

Firefox 32

60

60 ESR

Safari 16

11

Chrome

67

Mac OS X 10.11 (El Capitan)

Firefox 34

60

60 ESR

Safari

11

Chrome

67

Firefox 32

60

60 ESR

Safari 35

11

Chrome

67

12 For successful audio recording through Windows computer on Edge browser, make sure the trusted certificate of the certification
                           authority is added to the Trusted Root Store of the browser.

13 Firefox does not display any pop-up for muted microphone. Make sure to unmute the microphone while recording with Media Player
                           using computer device.

14 Windows 8.1 in the Desktop Mode.

15 On Mac OS X, computer record and play is not available with Safari and Firefox for Web Inbox and Mini Web Inbox. Only telephone
                           record and play is available.

16 On Mac OS X, Media Player does not support computer as recording device with Safari. For playback using computer device, go
                           to Safari > Preferences > Websites > AutoPlay and make sure that "Allow All Auto Play" option is selected under "When visiting
                           other websites" drop down list.

### Supported Version Combinations of Operating Systems and Web Browsers for Unity Connection 11.5(1) SU8

Supported Operating System

Supported Browser for Web Inbox and Mini Web Inbox

(64-bit)

Enterprise

Edge

44

Chrome

81

Firefox 17

73

(64-bit)

Enterprise

Edge

44

Chrome

81

Firefox 36

73

Mac OS X 10.12.6

Edge

44

Chrome

81

Firefox 36

73

Safari

12

17 For successful audio recording through Windows computer on Firefox browser for version 73 and later, make sure to change
                           the Firefox configuration.On Firefox, open "about:config" , search navigator, set "media.navigator.permission.disabled" to
                           true, close all windows of Firefox and reopen it.

## Compatibility
               	 Matrix for Unity Connection 10.x and Cisco Business Edition 6000/7000

This section
                     		  provides the compatibility matrices of the different operating systems of Unity
                     		  Connection 10.x and Cisco Business Edition 6000/7000 with the following web
                     		  applications or clients:

- Cisco ViewMail for
                        			 Microsoft Outlook

- Web Inbox

- Mini Web Inbox

- IMAP Clients

- Messaging Assistant and
                        			 Personal Call Transfer Rules

- Cisco Unity Connection
                        			 Administration

### View Mail with
                  	 Unity Connection 10.x and Cisco Business Edition 6000/7000

(32-bit
                                    					 and 64-bit)

- Professional

- Enterprise

- 11.5(1)—Supported with Outlook 2016 18 19 , 2013 38 20 , 2010, and 2007.

(32-bit
                                    					 and 64-bit)

- Standard

- Professional

- Enterprise

- 11.5(1)—Supported with Outlook 2016 37 38 , 2013 38 39 , 2010, and 2007.

- 11.0(1)—Supported with Outlook 2013 38 39 , 2010, and 2007.

- 10.0(1)—Supported with Outlook 2013 38 39 , 2010, and 2007.

- 9.0(2)—Supported with Outlook 2013 38 , 2010, and 2007.

(32-bit
                                    					 and 64-bit)

- Standard

- Professional

- Enterprise

Same as above

(32-bit
                                    					 and 64-bit)

Same as above

18 “Click-to-Run with App virtualization” for Outlook 2016 is supported with ViewMail for Outlook.

19 “Inline Forward and Reply” functionality for outlook 2013 and above, is not supported with ViewMail for Outlook.

20 “Click-to-Run with App virtualization” for Outlook 2013 is supported with ViewMail for Outlook only if Outlook 2010 is already
                           installed on your system.

### Web Inbox with
                  	 Unity Connection 10.x and Cisco Business Edition 6000/7000

- With Windows using Internet
                                    				  Explorer, QuickTime 7.7.8 is supported..

- With Mac OS X, QuickTime
                                    				  7.7.3 is supported.

- Audio Recording on Computer
                                    				  - Adobe Flash Player 15 or higher is required to record the voice messages on
                                    				  Web Inbox.

- In Internet Explorer, the
                                       				  message Only
                                          					 secure content is displayed , arises when you visit a website that contains
                                       				  mixed content i.e. encrypted https and non-encrypted http on the same web page.
                                       				  On this message window when you select the Show all
                                          					 content button, auto refresh works fine.

- In Firefox, when you select
                                       				  the security shield in the web address bar and select Disable
                                          					 protection mode , auto refresh works fine.

- In Chrome, when you select
                                       				  the security shield in the web address bar and select Load
                                          					 unsafe script , auto refresh works fine.

(32-bit
                                    					 and 64-bit)

- Professional

- Enterprise

- 45

- 45 ESR

- 11

- 42

- 20

Windows 8.1

(32-bit and 64-bit)

- Standard

- Professional

- Enterprise

- 32

- 31 ESR

- 11

- 37

Windows 7

(32-bit and 64-bit)

- Professional

- Enterprise

- Ultimate

- 32

- 31 ESR

- 11

- 10

- 9

- 37

(32-bit and 64-bit)

- 32

- 31 ESR

- 9

- 37

- 32

- 31 ESR

- 7

- 37

- 32

- 31 ESR

- 6

- 37

- 32

- 31 ESR

- 6

- 37

- 32

- 31 ESR

- 37

- 10

21 Windows 8.1 in the Desktop Mode.

22 On Windows 7 and Windows Vista, using Internet Explorer 9 (64 bit), the play functionality is supported only via phone as
                           the Quick Time 64 bit plug-in is not available.

23 On Mac
                           					 OS X, computer record and play is not available in Safari and Firefox for Web
                           					 Inbox. Only telephone record and play is available.

It is
                                    			 recommended that for 32-bit browsers, the java version should be 32-bit only.
                                    			 32 bit browser does not support 64 bit java version.

### Mini Web Inbox
                  	 with Unity Connection 10.x

Ensure you have
                        		  performed the following steps:

Make sure the
                              				trusted certificate of the certification authority is added to the Trusted Root
                              				Store on the user workstations in order to access the notifications via email
                              				and the voice message via Mini Web Inbox. For more information on how to
                              				configure the trusted certificate on Unity Connection, see the " Securing Cisco Unity
                                 				  Connection Administration, Cisco PCA, and IMAP Email Client Access to Cisco
                                 				  Unity Connection " chapter of the Security
                                 				  Guide for Cisco Unity Connection, Release 10.x , available at http://www.cisco.com/c/en/us/td/docs/voice_ip_
                                 				  comm/connection/10x/security/guide/10xcucsecx.html .

- Make sure to perform the
                           			 steps to configure the HTML notification on user workstation. For more
                           			 information on how to configure the HTML notifications, see the " Configuring Unity Connection
                              				for HTML-based Message Notification " section of the "Configuring an
                           			 Email Account to Access Cisco Unity Connection Voice Messages" chapter of the User
                              				Workstation Setup Guide for Cisco Unity Connection, Release 10.x , available
                           			 at http://www.cisco.com/c/en/us/td/docs/voice_ip_
                              				comm/connection/10x/user_setup/guide/10xcucuwsx.html .

- With Windows using Internet
                                 				  Explorer, QuickTime 7.7.8 is supported.

- With Mac OS X, QuickTime
                                 				  7.7.3 is supported.

- For audio recording on
                           			 computer, Flash Player 15 or higher is required to record the voice messages on
                           			 Mini Web Inbox.

For more
                                 		  information on Mini Web Inbox, refer to the Quick Start
                                    			 Guide for the Cisco Unity Connection Mini Web Inbox available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/10x/quick_start/guide/b_10xcucqsgminiinbox.html .

The Table 5
                        		  describes the supported combinations of operating systems and web browsers
                        		  installed on workstation to access voice messages using Mini Web Inbox

- Professional

- Enterprise

- 45

- 45 ESR

- 11

- 42

- 20

- Standard

- Professional

- Enterprise

- 32

- 31 ESR

- 11

- 37

- Professional

- Enterprise

- Ultimate

- 32

- 31 ESR

- 11

- 10

- 9

- 37

- 32

- 31 ESR

- 9

- 37

- 32

- 31 ESR

- 7.0.6

- 37

- 32

- 31 ESR

- 6

- 37

- 32

- 31 ESR

- 6

- 37

- 32

- 31 ESR

- 37

24 Windows
                           					 8.1 in the Desktop Mode.

25 On
                           					 Windows 7 and Windows Vista, using Internet Explorer 9 (64 bit), the play
                           					 functionality is supported only via phone as the Quick Time 64 bit plug-in is
                           					 not available.

26 On Mac
                           					 OS X, computer record and play is not available in Safari and Firefox for Web
                           					 Inbox. Only telephone record and play is available.

It is
                                 		  recommended that for 32-bit browsers, the java version should be 32-bit only.
                                 		  32 bit browser does not support 64 bit java version.

### IMAP Clients with
                  	 Unity Connection 10.x and Cisco Business Edition 6000/7000

The Table 10
                        		  describes the supported combinations of operating systems and IMAP client
                        		  applications to access voice messages.

The IMAP
                                 		  clients support both the IPv4 and IPv6 addresses. However, the IPv6 address
                                 		  works only when the Unity Connection platform is configured in Dual (IPv4/IPv6)
                                 		  mode.

- Professional

- Enterprise

- 2016

- 2013 27

- 2010 28

- 2007

- 2012

- 9 30

- 38

- 38 ESR

(32-bit
                                    					 and 64-bit)

- Standard

- Professional

- Enterprise

- 2013 46

- 2010 47

- 2007

- 2012

- 9

- 8

- 31

- 31 ESR

- 1

(32-bit
                                    					 and 64-bit)

- Professional

- Enterprise

- Ultimate

- 2013 46

- 2010 47

- 2007

- 2012

- 2011

- 9

- 8

- 31

- 31 ESR

- 1

(32-bit
                                    					 and 64-bit)

- 2010 47

- 2007

- 2011

- 9

- 8

- 31

- 31 ESR

- 1

- 2011

- 7

- 9

- 31

- 31 ESR

- 1

- 2011

- 6

- 9

- 8

- 24

- 24 ESR

- 1

- 2011

- 5

- 9

- 8

- 24

- 24 ESR

- 1

- 2011

- 4

- 9

- 8

- 24

- 24 ESR

- 1

- 5.0

- 4.0

- 9

- 8

- 11

- 10

27 With Outlook 2013, it is mandatory to install KB2889859 using http://support2.microsoft.com/kb/2889859 .
                           								The delete operation may not work with Outlook 2013.

28 Outlook 2010 will stop working if you install KB2956203
                           								update.

29 Lotus Notes is supported in the Online Mode only but the mark
                           						  read operation from Web Inbox to Lotus Notes is not synchronized. Also, the
                           						  delete operation supports only the hard delete of messages in Lotus Notes.

30 Lotus Note 9 with Fix Pack 3 is Supported in Unity
                           								Connection.

31 Windows 8.1 in the Desktop
                           					 Mode.

### Messaging
                  	 Assistant and Personal Call Transfer Rules Web Tools with Unity Connection 10.x
                  	 and Cisco Business Edition 6000/7000

- Professional

- Enterprise

- 45

- 45 ESR

- 11

- 42 32

- 20 33

(32-bit
                                    					 and 64-bit)

- Standard

- Professional

- Enterprise

- 32

- 31 ESR

- 11

- 37

(32-bit
                                    					 and 64-bit)

- Professional

- Enterprise

- Ultimate

- 32

- 31 ESR

- 11

- 10

- 9

- 37

(32-bit
                                    					 and 64-bit)

- 32

- 31 ESR

- 9

- 37

- 32

- 31 ESR

- 7

- 32

- 31 ESR

- 6

- 32

- 31 ESR

- 6

- 32

- 31 ESR

32 The Java plug-in for web browsers relies on the cross platform plugin architecture NPAPI. In Chrome Version 42, you need to
                           perform the steps mentioned in Configuring Chrome 42 " section to continue using NPAPI plugins.

33 Media Master is not compatible with Edge browser.

34 Windows 8.1 in the Desktop
                           					 Mode.

It is recommended that for 32-bit browsers, the java version should
                                 		  be 32-bit only. 32 bit browser does not support 64 bit java version.

### Browsers Supported
                  	 with Cisco Unity Connection Administration for Unity Connection 10.x

- Professional

- Enterprise

- 45

- 45 ESR

- 11

- 42 35

- 20 36

(32-bit
                                    					 and 64-bit)

- Standard

- Professional

- Enterprise

- 32

- 31 ESR

- 11

- 37

(32-bit
                                    					 and 64-bit)

- Professional

- Enterprise

- Ultimate

- 32

- 31 ESR

- 11

- 10

- 9

- 37

(32-bit
                                    					 and 64-bit)

- 32

- 31 ESR

- 9

- 32

- 31 ESR

- 7

- 32

- 31 ESR

- 6

- 32

- 31 ESR

- 6

- 32

- 31 ESR

35 The Java plug-in for web browsers relies on the cross platform plugin architecture NPAPI. In Chrome Version 42, you need to
                           perform the steps mentioned in " Configuring Chrome 42 section to continue using NPAPI plugins.

36 Menus of Cisco Unity Connection are not working on Edge
                           								Browser.

37 Windows 8.1 in the Desktop
                           					 Mode.

It is recommended that for 32-bit browsers, the java version
                                    			 should be 32-bit only. 32 bit browser does not support 64 bit java version.

We recommend
                                 		  using Java 8 update 79 for Cisco Unity Connection Administration.

| Note | For more
                              		information on Mini Web Inbox, refer to the Quick Start Guide for the Cisco
                              		Unity Connection Mini Web Inbox available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/quick_start/guide/b_11xcucqsgminiinbox.html . |
|---|---|

| Supported Operating System | Supported Browser | IMAP Clients | ViewMail Application (Compatibility with version - 12.5(3)) | ViewMail Application (Compatibility with version - 12.5(2)) |
|---|---|---|---|---|
| Web Inbox and Mini Web Inbox | Cisco Unity Connection Administration, Messaging Assistant and Personal Call Transfer Rules |
| Windows 10 (32-bit and 64-bit) Professional Enterprise | Firefox 45 45 ESR Chrome 49 Edge 1 20 | Firefox 45 45 ESR Internet Explorer 11 Chrome 49 2 Edge 20 3 | Outlook 2016 2013 4 2010 5 2007 Windows Live Mail 2012 Lotus Notes 6 9 7 Thunderbird 38 38 ESR | Outlook Desktop Application 8 2019 9 2016 28 2013 | Outlook Desktop Application 27 2019 2016 28 2013 28 |
| Windows 8.1 10 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 45 45 ESR Chrome 49 | Firefox 45 45 ESR Internet Explorer 11 Chrome 49 21 | Outlook 2016 2013 23 2010 24 2007 Windows Live Mail 2012 Lotus Notes 25 9 26 Thunderbird 38 38 ESR | Same as above | Same as above |
| Windows 7 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 45 45 ESR Chrome 49 | Firefox 45 45 ESR Internet Explorer 11 Chrome 49 21 | Outlook 2016 2013 23 2010 24 2007 Windows Live Mail 2012 Lotus Notes 25 9 26 Thunderbird 38 38 ESR | Not Supported | Not Supported |
| Mac OS X 10.11 (El Capitan) | Firefox 11 45 45 ESR Safari 9 Chrome 49 | Firefox 45 45 ESR Safari 9 Chrome 49 21 | Outlook 2011 Apple Mail 9 Thunderbird 45 45 ESR | Not Applicable | Not Applicable |
| Mac OS X 10.10 (Yosemite) | Firefox 30 45 45 ESR Safari 8 Chrome 49 | Firefox 45 45 ESR Safari 8 Chrome 49 21 | Outlook 2011 Apple Mail 8 Thunderbird 45 45 ESR | Not Applicable | Not Applicable |
| Mac OS X 10.9 (Mavericks) | Firefox 30 45 45 ESR Safari 7 Chrome 49 | Firefox 45 45 ESR Safari 7 Chrome 49 21 | Outlook 2011 Apple Mail 7 Thunderbird 45 45 ESR | Not Applicable | Not Applicable |

| Note | It is recommended that
                                          				  for 32-bit browsers, the java version should be 32-bit only. 32 bit browser
                                          				  does not support 64 bit java version. The IMAP clients support
                                          				  both the IPv4 and IPv6 addresses. However, the IPv6 address works only when the
                                          				  Unity Connection platform is configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Supported Operating System | Supported Browser for Web Inbox and Mini Web Inbox | Supported Browser for Cisco Unity Connection Administration, Messaging Assistant and Personal Call Transfer Rules |
|---|---|---|
| Window 10 (32-bit and 64-bit) Professional Enterprise | Firefox 60 60 ESR Chrome 67 Edge 12 40 | Firefox 13 60 60 ESR Chrome 67 Edge 40 |
| Windows 8.1 14 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 60 60 ESR Chrome 67 | Firefox 32 60 60 ESR Chrome 67 |
| Windows 7 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 60 60 ESR Chrome 67 | Firefox 32 60 60 ESR Chrome 67 |
| Mac OS X 10.12 (Sierra) | Firefox 15 60 60 ESR Safari 11 Chrome 67 | Firefox 32 60 60 ESR Safari 16 11 Chrome 67 |
| Mac OS X 10.11 (El Capitan) | Firefox 34 60 60 ESR Safari 11 Chrome 67 | Firefox 32 60 60 ESR Safari 35 11 Chrome 67 |

| Supported Operating System | Supported Browser for Web Inbox and Mini Web Inbox |
|---|---|
| Window 10 (64-bit) Enterprise | Edge 44 Chrome 81 Firefox 17 73 |
| Windows 7 (64-bit) Enterprise | Edge 44 Chrome 81 Firefox 36 73 |
| Mac OS X 10.12.6 | Edge 44 Chrome 81 Firefox 36 73 Safari 12 |

| Supported Operating System | ViewMail Application |
|---|---|
| Windows 10 (32-bit
                                    					 and 64-bit) Professional Enterprise | 11.5(1)—Supported with Outlook 2016 18 19 , 2013 38 20 , 2010, and 2007. |
| Windows 8.1 (32-bit
                                    					 and 64-bit) Standard Professional Enterprise | 11.5(1)—Supported with Outlook 2016 37 38 , 2013 38 39 , 2010, and 2007. 11.0(1)—Supported with Outlook 2013 38 39 , 2010, and 2007. 10.0(1)—Supported with Outlook 2013 38 39 , 2010, and 2007. 9.0(2)—Supported with Outlook 2013 38 , 2010, and 2007. |
| Windows 7 (32-bit
                                    					 and 64-bit) Standard Professional Enterprise | Same as above |
| Windows Vista (32-bit
                                    					 and 64-bit) | Same as above |

| Supported Operating System | Supported Browser |
|---|---|
| Window 10 (32-bit
                                    					 and 64-bit) Professional Enterprise | Firefox 45 45 ESR Internet Explorer 11 Chrome 42 Edge 20 |
| Windows 8.1 (32-bit and 64-bit) Standard Professional Enterprise | Firefox 32 31 ESR Internet Explorer 11 Chrome 37 |
| Windows 7 (32-bit and 64-bit) Professional Enterprise Ultimate | Firefox 32 31 ESR Internet Explorer 11 10 9 Chrome 37 |
| Windows Vista 41 (32-bit and 64-bit) | Firefox 32 31 ESR Internet Explorer 9 Chrome 37 |
| Mac OS X 23 10.9 (Mavericks) | Firefox 32 31 ESR Safari 7 Chrome 37 |
| Mac OS X 42 10.8 (Mountain Lion) | Firefox 32 31 ESR Safari 6 Chrome 37 |
| Mac OS X 42 10.7 (Lion) | Firefox 32 31 ESR Safari 6 Chrome 37 |
| Mac OS X 42 10.6 (Snow Leopard) | Firefox 32 31 ESR Chrome 37 |
| Red Hat Enterprise Linux 5.0(32 bit) | Firefox 10 |

| Note | It is
                                    			 recommended that for 32-bit browsers, the java version should be 32-bit only.
                                    			 32 bit browser does not support 64 bit java version. |
|---|---|

| Note | For more
                                 		  information on Mini Web Inbox, refer to the Quick Start
                                    			 Guide for the Cisco Unity Connection Mini Web Inbox available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/10x/quick_start/guide/b_10xcucqsgminiinbox.html . |
|---|---|

| Supported Operating System | Supported Browsers |
|---|---|
| Windows 10 (32-bit
                                    					 and 64-bit) Professional Enterprise | Firefox 45 45 ESR Internet Explorer 11 Chrome 42 Edge 20 |
| Windows 8.1 (32-bit and
                                 				  64-bit) 24 Standard Professional Enterprise | Firefox 32 31 ESR Internet Explorer 11 Chrome 37 |
| Windows 7 25 (32-bit and 64-bit) Professional Enterprise Ultimate | Firefox 32 31 ESR Internet Explorer 11 10 9 Chrome 37 |
| Windows Vista 44 (32-bit and 64-bit) | Firefox 32 31 ESR Internet Explorer 9 Chrome 37 |
| Mac OS X 26 10.9 (Mavericks) | Firefox 32 31 ESR Safari 7.0.6 Chrome 37 |
| Mac OS X 45 10.8 (Mountain Lion) | Firefox 32 31 ESR Safari 6 Chrome 37 |
| Mac OS X 45 10.7 (Lion) | Firefox 32 31 ESR Safari 6 Chrome 37 |
| Mac OS X 45 10.6 (Snow Leopard) | Firefox 32 31 ESR Chrome 37 |

| Note | It is
                                 		  recommended that for 32-bit browsers, the java version should be 32-bit only.
                                 		  32 bit browser does not support 64 bit java version. |
|---|---|

| Note | The IMAP
                                 		  clients support both the IPv4 and IPv6 addresses. However, the IPv6 address
                                 		  works only when the Unity Connection platform is configured in Dual (IPv4/IPv6)
                                 		  mode. |
|---|---|

| Supported Operating System | Supported Browser |
|---|---|
| Windows 10 (32-bit
                                    					 and 64-bit) Professional Enterprise | Outlook 2016 2013 27 2010 28 2007 Windows Live Mail 2012 Lotus Notes 29 9 30 Thunderbird 38 38 ESR |
| Windows 8.1 (32-bit
                                    					 and 64-bit) Standard Professional Enterprise | Outlook 2013 46 2010 47 2007 Windows Live Mail 2012 Lotus Notes 48 9 8 Thunderbird 31 31 ESR Opera Mail 1 |
| Windows 7 (32-bit
                                    					 and 64-bit) Professional Enterprise Ultimate | Outlook 2013 46 2010 47 2007 Windows Live Mail 2012 2011 Lotus Notes 48 9 8 Thunderbird 31 31 ESR Opera Mail 1 |
| Windows Vista (32-bit
                                    					 and 64-bit) | Outlook 2010 47 2007 Windows Live Mail 2011 Lotus Notes 48 9 8 Thunderbird 31 31 ESR Opera Mail 1 |
| Mac OS X 10.9 (Mavericks) | Outlook 2011 Apple Mail 7 Lotus Notes 48 9 Thunderbird 31 31 ESR Opera Mail 1 |
| Mac OS X 10.8 (Mountain
                                 				  Lion) | Outlook 2011 Apple Mail 6 Lotus Notes 48 9 8 Thunderbird 24 24 ESR Opera Mail 1 |
| Mac OS X 10.7 (Lion) | Outlook 2011 Apple Mail 5 Lotus Notes 48 9 8 Thunderbird 24 24 ESR Opera Mail 1 |
| Mac OS X 10.6 (Snow Leopard) | Outlook 2011 Apple Mail 4 Lotus Notes 48 9 8 Thunderbird 24 24 ESR Opera Mail 1 |
| Red Hat Enterprise Linux 5.0(32 bit) 5.0 4.0 | Thunderbird 9 8 Opera 11 10 |

| Supported Operating System | Supported Browser |
|---|---|
| Windows 10 (32-bit
                                    					 and 64-bit) Professional Enterprise | Firefox 45 45 ESR Internet Explorer 11 Chrome 42 32 Edge 20 33 |
| Windows 8.1 (32-bit
                                    					 and 64-bit) Standard Professional Enterprise | Firefox 32 31 ESR Internet Explorer 11 Chrome 37 |
| Windows 7 (32-bit
                                    					 and 64-bit) Professional Enterprise Ultimate | Firefox 32 31 ESR Internet Explorer 11 10 9 Chrome 37 |
| Windows Vista (32-bit
                                    					 and 64-bit) | Firefox 32 31 ESR Internet Explorer 9 Chrome 37 |
| Mac OS X 10.9 (Mavericks) | Firefox 32 31 ESR Safari 7 |
| Mac OS X 10.8 (Mountain
                                 				  Lion) | Firefox 32 31 ESR Safari 6 |
| Mac OS X 10.7 (Lion) | Firefox 32 31 ESR Safari 6 |
| Mac OS X 10.6 (Snow
                                 				  Leopard) | Firefox 32 31 ESR |

| Note | It is recommended that for 32-bit browsers, the java version should
                                 		  be 32-bit only. 32 bit browser does not support 64 bit java version. |
|---|---|

| Supported Operating System | Supported Browser |
|---|---|
| Windows 10 (32-bit
                                    					 and 64-bit) Professional Enterprise | Firefox 45 45 ESR Internet Explorer 11 Chrome 42 35 Edge 20 36 |
| Windows 8.1 (32-bit
                                    					 and 64-bit) Standard Professional Enterprise | Firefox 32 31 ESR Internet Explorer 11 Chrome 37 |
| Windows 7 (32-bit
                                    					 and 64-bit) Professional Enterprise Ultimate | Firefox 32 31 ESR Internet Explorer 11 10 9 Chrome 37 |
| Windows Vista (32-bit
                                    					 and 64-bit) | Firefox 32 31 ESR Internet Explorer 9 |
| Mac OS X 10.9 (Mavericks) | Firefox 32 31 ESR Safari 7 |
| Mac OS X 10.8 (Mountain
                                 				  Lion) | Firefox 32 31 ESR Safari 6 |
| Mac OS X 10.7 (Lion) | Firefox 32 31 ESR Safari 6 |
| Mac OS X 10.6 (Snow
                                 				  Leopard) | Firefox 32 31 ESR |

| Note | It is recommended that for 32-bit browsers, the java version
                                    			 should be 32-bit only. 32 bit browser does not support 64 bit java version. |
|---|---|

| Note | We recommend
                                 		  using Java 8 update 79 for Cisco Unity Connection Administration. |
|---|---|