---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-unified-messaging-b-12xcucumgx-b-12xcucumgx-chapter-011-html-b74fc98ddf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/unified_messaging/b_12xcucumgx/b_12xcucumgx_chapter_011.html
retrieved_at: 2026-08-17T03:45:13.381903+00:00
---

Unified Messaging Guide for Cisco Unity Connection Release 12.x

# Unified Messaging Guide for Cisco Unity Connection Release 12.x

Updated: August 30, 2023

Chapter: Configuring Calendar and Contact Integration

## Chapter: Configuring Calendar and Contact Integration

# Configuring Calendar and Contact Integration

Configuring Calendar and Contact Integration

## Overview

You can configure calendar and contact integration on Unity Connection with Exchange, Office 365, or Cisco Unified MeetingPlace
                           servers. For more information on calendar and contact integration, see the Calendar and Contact Integration, page 1-11 section.

## Configuring
                        	 Calendar and Contact Integration with Exchange or Office 365 Servers

Review the system requirements to ensure that all the requirements for Exchange 2019, Exchange 2016, Exchange 2013, Exchange
                                 2010, and Office 365 are met. For more information see the sections “ Requirements for Accessing Calendar Information for Meetings ” and “Requirements for Accessing Exchange Contact Information” of System Requirements for Cisco Unity Connection, Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

Configure the Exchange server with which Unity Connection is
                                 			 integrated for calendar and contact integration. See the following sections:

Configuring
                                          					 Office 365, Exchange 2016, Exchange 2013, Exchange 2010, or Exchange 2007 for
                                          					 Calendar and Contact Integration

Configuring
                                          					 Unity Connection for Calendar and Contact Integration

Configure Unity Connection for calendar and contact integration.
                                 			 See the Configuring
                                    				Unity Connection for Calendar and Contact Integration .

(When enabling Personal Call Transfer Rules only) Verify
                                 			 that the users or templates are assigned to a class of service that enables
                                 			 them to use the personal call transfer rules feature.

Configure the Unity Connection users for calendar and contact
                                 			 integration. See the Configuring
                                    				Unity Connection Users for Calendar and Contact Integration .

Test the calendar integration. See the Testing
                                    				Calendar Integration with Exchange or Office 365 Servers .

### Configuring Office 365, Exchange 2019, Exchange 2016, Exchange 2013 or Exchange 2010 for Calendar and Contact Integration

Do the following tasks to configure Exchange 2019, Exchange 2016, Exchange 2013, Exchange 2010 for the calendar and contact
                              integration:

Confirm that Client Access role has been enabled on Exchange 2019, Exchange 2016, Exchange 2013 and Exchange 2010 server.

Do the Configuring
                                       				Exchange 2016, Exchange 2013 and Exchange 2010 for Calendar and Contact
                                       				Integration, page 4-2 .

(Optional) If you are using SSL for secure access to the
                                    			 Exchange server, follow the steps mentioned in the section Configuring
                                       				Secure Access to Exchange 2016, Exchange 2013 and Exchange 2010 .

If you have already configured secure IMAP with SSL on Exchange
                                                				server and enabled the certificate for both IMAP and IIS, then follow the
                                                				section “Configuring
                                                   				  Exchange 2016, Exchange 2013, Exchange 2010 for Calendar and Contact
                                                   				  Integration” procedure on page 4-2 .

#### Configuring Exchange 2019, Exchange 2016, Exchange 2013, Exchange 2010 for Calendar and Contact Integration

Step 1

On the Exchange server, open the Internet Services (IIS) Manager application.

Step 2

Go to Internet Information Services > 
                                             			 <Exchange server name> > Web Sites >  Default Web Site.

Step 3

Right-click Exchange and select Properties .

Step 4

In the Exchange
                                                				Properties dialog box, select the Virtual Directory tab.

Step 5

From the Content For
                                                				This Resource Should Come From menu, select A Directory
                                                				Located On This Computer .

Step 6

Confirm the Local Path is set to \\.\BackOfficeStorage\<your-domain.com>\MBX .

Step 7

Select the Read check
                                             			 box.

Step 8

Select the Directory Security tab.

Step 9

From the Authentication
                                                				and Access Control menu, select Edit .

Step 10

In the Authenticated
                                                				Access section of the Authentication Methods dialog box, check the check
                                             			 boxes for one or more of the following options:

Integrated Windows authentication (sometimes referred to as
                                                      					 NTLM)

Basic Authentication

Digest Authentication for Windows Domain Servers

Step 11

Select OK .

Step 12

In the Exchange
                                                				Properties dialog box, select OK .

Step 13

Go to Internet Information Services > <server name > > Web Service
                                                   				  Extensions .

Step 14

In the right-hand pane, select WebDav and
                                             			 confirm that the status is “Allowed.” If the status is not “Allowed”, click Allow .

Step 15

On the Exchange server, open the Exchange Management Console .

Step 16

Go to Server
                                                				Configuration > Mailbox .

Step 17

Do the following for each mailbox that you want to configure for
                                             			 the calendar and contact integration:

In the upper middle pane, select the mailbox name.

In the lower middle pane, select the WebDav tab.

Right-click Exchange
                                                      					 (Default Web Site) and select Properties .

In the Exchange
                                                      					 (Default Web Site) Properties dialog box, select the Authentication tab.

Select Use One
                                                      					 or More Standard Authentication Methods and select the same authentication
                                                   				  method(s) that you configured in Step 10 .

Step 18

Click OK .

Step 19

Open the Exchange Management Shell .

Step 20

In the Exchange
                                                				Management Shell , enter the following command:

iisbreset /noforce

Step 21

Press Enter .

#### Configuring Secure
                              	 Access to Exchange 2013, Exchange 2010

Step 1

On the Exchange Server, open the Exchange Management Shell application.

Step 2

Enter the following command, where < Exchange server > is
                                             			 the IP address or fully qualified domain name of the Exchange server and < friendly name > is
                                             			 the friendly name that you selected for the Exchange server:

new-exchangecertificate -generaterequest -domainname < Exchange server > -friendlyname < friendly name > -path c:\csr.txt

Caution

Step 3

Press Enter .

A Certificate Signing Request (CSR) file with the name Csr.txt
                                                				is created in the root directory.

Step 4

Send the CSR file to a Certification Authority (CA), which
                                             			 generates and sends back a new certificate.

Step 5

Save the new certificate in a location that is accessible to the
                                             			 Exchange server on which you want to import the certificate.

Step 6

On the Exchange Server, open the Exchange
                                                				Management Shell application.

Step 7

Enter the following command, where <path> is the full path
                                             			 of the new certificate that you received from the CA:

import-exchangecertificate -path <path>

Step 8

Press Enter .

Step 9

Enter the following command:

dir
                                                   				  cert:\localmachine\my | fl

Step 10

Press Enter .

Step 11

Highlight the “thumbprint” property and press Ctrl-C to copy it to the clipboard.

Step 12

If Unity Connection is configured to use IMAP to access both email and calendar data from Exchange server, enter the following
                                             command, where <thumbprint> is the “thumbprint” that you copied in Step 11 :

enable-exchangecertificate -thumbprint <thumbprint> -services "IIS,IMAP"

If Unity Connection is not configured to use IMAP but configured to use calendar data from Exchange server, enter the following
                                                command, where <thumbprint> is the “thumbprint” that you copied in Step 11 :

enable-exchangecertificate -thumbprint <thumbprint> -services "IIS"

Step 13

Press Enter .

Step 14

If you want data transmitted as clear text, skip the remaining
                                             			 steps in this procedure and continue with the “Configuring
                                                				Unity Connection for Calendar and Contact Integration” section on
                                                				page 4-4 . Otherwise, open the IIS Manager application.

Step 15

Go to IIS > <server name > > Web
                                                   				  Sites > Default Web
                                                   				  Site .

Step 16

Right-click Default Web Site and select Properties .

Step 17

In the Properties dialog box, select the Directory Security tab.

Step 18

From the Secure
                                                				Communications menu, select Edit .

Step 19

Check the Require Secure Channel check box.

Step 20

Select OK .

Step 21

In the Properties dialog box, select OK .

### Configuring Unity
                           	 Connection for Calendar and Contact Integration

Step 1

In Cisco Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services . You can modify an
                                          			 existing unified messaging service or create a new service using Add New .

Step 2

On the New Unified Messaging Service page, in the Type list, select Exchange/BPOS-D and check the Enabled check box to enable the unified messaging
                                          			 service.

Step 3

Enter the details of the required fields and select Save . (For information on each field, see Help> This Page ).

Step 4

Select Test and a message appears indicating whether the
                                          			 configuration has been successfully verified. If the verification fails, follow
                                          			 the above configuration steps to ensure that they have been properly
                                          			 implemented.

### Configuring Unity
                           	 Connection Users for Calendar and Contact Integration

After configuring the Unity Connection server for calendar and
                                 		  contact integration, you can configure the applicable users.

Step 1

In Cisco Unity Connection Administration, expand Users and select Users . Select an applicable user.

Step 2

On the Edit User Basics page, in the Edit menu,
                                          			 select Unified Messaging Accounts .

Step 3

On the Unified Messaging Accounts page, select Add New .

Step 4

On the New Unified Messaging Accounts page, select the following
                                          			 details:

In Unified
                                                      						Messaging Service drop-down, select the unified messaging service created
                                                   					 in the section Configuring
                                                      						Unity Connection for Calendar and Contact Integration, page 4-4 .

From the Account
                                                      						Information menu, in the Use This
                                                      						Email Address field, enter the Exchange email address in Active Directory
                                                   					 for the user.

Step 5

In the Service
                                             				Capabilities menu, check the Access Exchange Calendar and Contacts check box and
                                          			 select Save .

Step 6

Check the calendar and contact configuration for the user, selecting Test . The Task Execution Results window appears with the test results. If any part of the test fails, verify the configuration for Exchange 2019, Exchange
                                          2016, Exchange 2013, or Exchange 2010, Active Directory, Unity Connection, and the user.

Step 7

Repeat Step 2 through Step 6 for all
                                          			 remaining users.

### Testing Calendar
                           	 Integration with Exchange or Office 365 Servers

Step 1

Sign in to Outlook.

Step 2

On the Go menu,
                                          			 select Calendar .

Step 3

On the File menu,
                                          			 select New > Meeting
                                                				  Request .

Step 4

Enter values in the required fields to schedule a new meeting
                                          			 for the current time, and invite a user who has an account on Unity Connection.
                                          			 Select Send .

Step 5

Sign in to the Unity Connection mailbox of the user that you
                                          			 invited to the Outlook meeting:

If the user account is configured for speech access, say Play Meetings .

If the user account is not configured for speech access, press 6 , and then follow the prompts to list meetings.

Unity Connection reads the information about the Exchange 2019, 2016, 2013, 2010 meetings.

## Configuring
                        	 Calendar and Contact Integration with Cisco Unified MeetingPlace or Cisco
                        	 Unified MeetingPlace Express

Review the system requirements to confirm that all requirements
                                 			 for Cisco Unified MeetingPlace and the Unity Connection server have been met.
                                 			 See the “ Requirements for Accessing
                                    				Calendar Information for Meetings ” section of System Requirements for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

Configure Cisco Unified MeetingPlace or Cisco Unified
                                 			 MeetingPlace Express. See the following sections:

Configuring
                                          					 Cisco Unified MeetingPlace for Calendar Integration

Configuring
                                          					 Cisco Unified MeetingPlace Express for Calendar Integration

Configure Unity Connection. See the “Configuring
                                    				Unity Connection for Calendar Integration” section.

If you configured Cisco Unified MeetingPlace to use HTTPS in
                                 			 step 2. , and configured
                                 			 unified messaging services to validate certificates for MeetingPlace servers in
                                 			 step 3. : on the Unity
                                 			 Connection server, in Cisco Unified Communications Operating System, upload
                                 			 certificates from the certification authority that issued the SSL certificates
                                 			 for MeetingPlace servers to both tomcat-trust and Unity Connection-trust
                                 			 locations. For more information on SSL instructions, see the “ Using SSL to Secure
                                    				Client/Server Connections ” chapter of the Security Guide
                                    				for Cisco Unity Connection, Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/b_12xcucsecx.html .

Configure the Unity Connection users. See the “Configuring
                                    				Unity Connection Users for Calendar Integration” section.

Test the calendar integration. See the “Testing
                                    				Calendar Integration with Cisco Unified MeetingPlace or Cisco Unified
                                    				MeetingPlace Express” section.

To teach users how to list, join, and schedule meetings, see the
                                 			 “ Phone Menus and
                                    				Voice Commands ” chapter of the User Guide for the Cisco Unity Connection Phone Interface
                                    				(Release 12.x) at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/phone/b_12xcucugphone.html .

### Configuring Cisco
                           	 Unified MeetingPlace for Calendar Integration

Step 1

Sign in to the Cisco Unified MeetingPlace Application Server as
                                          			 an administrator.

Step 2

Select User
                                                				  Configuration > User
                                                				  Profiles .

Step 3

Select Add New .

Step 4

Enter the following values in the required fields to create a
                                          			 privileged service account:

First Name

Leave this field blank.

Last Name

Enter Cisco Unity Connection .

User ID

Enter cucsvc or another user
                                                         							 ID that you want.

User Password

Enter the applicable
                                                         							 password.

Profile Number

Enter the applicable
                                                         							 profile number.

Profile Password

Enter the applicable
                                                         							 profile password.

Type of User

Select System Administrator .

Step 5

Select Save .

Step 6

Sign out of Cisco Unified MeetingPlace.

Step 7

In the Address field of a web browser, if SSL is not enabled,
                                          			 enter the following URL (where <server> is the IP address or host name of
                                          			 the Cisco Unified MeetingPlace server):

http://<server>/webservices/services/meetingservice?wsdl

If SSL is enabled, enter the following URL:

https://<server>/webservices/services/meetingservice?wsdl

Step 8

Press Enter .

Step 9

When prompted to sign in, enter the user ID and password for the
                                          			 privileged service account.

The Cisco Unified MeetingPlace Web Services Description Language
                                             				(WSDL) download page appears with the title “XFire Services”.

### Configuring Cisco
                           	 Unified MeetingPlace Express for Calendar Integration

Step 1

Sign in to Cisco Unified MeetingPlace Express and select Administration .

Step 2

Select User
                                                				  Configuration > User Profile
                                                				  Management .

Step 3

Select Add New .

Step 4

Enter the following values in the required fields to create an
                                          			 API user:

First Name

Leave this field blank.

Last Name

Enter Cisco Unity Connection .

User ID

Enter cucsvc or another user
                                                         							 ID that you want.

User Password

Enter the applicable
                                                         							 password.

Profile Number

Enter the applicable
                                                         							 profile number.

Type of User

Select API User .

Step 5

Select Save .

Step 6

Sign out of Cisco Unified MeetingPlace Express.

If you do not sign out of Cisco Unified MeetingPlace Express,
                                             				the test fails in the Testing
                                                				  Calendar Integration with Cisco Unified MeetingPlace or Cisco Unified
                                                				  MeetingPlace Express, page 4-9 .

Step 7

In the Address field of a web browser:

if SSL is not enabled, enter the following URL (where
                                                   					 <server> is the IP address or host name of the Cisco Unified MeetingPlace
                                                   					 Express server):

http://<server>.com/webservices/services/meetingservice?wsdl

If SSL is enabled, enter the following URL:

https://<server>.com/webservices/services/meetingservice?wsdl

Step 8

Press Enter .

Step 9

When prompted
                                          			 to sign in, enter the user ID and password for the API user.

The Cisco Unified MeetingPlace Express WSDL download page
                                             				appears with the title “XFire Services.”

### Configuring Unity
                           	 Connection for Calendar Integration

Step 1

In Cisco Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services.

Step 2

Modify an existing unified messaging service or create a new
                                          			 service by selecting Add New .

Step 3

On the New Unified Messaging Service page, in the Type list, select MeetingPlace 8.x and check the Enabled check box to enable
                                          			 unified messaging with Cisco Unified MeetingPlace server.

Step 4

Enter the values of the required fields and select Save . (For information on each field, see Help> This Page ).

Step 5

To check the integration with Cisco Unified MeetingPlace, select Test . The Task Execution Results window appears with the test results.
                                          			 If any part of the test fails, verify the configuration for Cisco Unified
                                          			 MeetingPlace and Unity Connection.

### Configuring Unity
                           	 Connection Users for Calendar Integration

Caution

Step 1

In Cisco Unity Connection Administration, expand Users and select Users . Select an applicable user.

Step 2

On the Edit User Basics page, on the Edit menu, select Unified Messaging Accounts .

Step 3

On the Unified Messaging Accounts page, select Add New . The New Unified Messaging Account page
                                          			 appears.

Step 4

On the New Unified Messaging Account page, select the Unified Messaging Service for Cisco Unified MeetingPlace.
                                          			 Enter the values of the required fields and select Save. (For information on
                                          			 each field, see Help> This Page ).

Step 5

To check the calendar configuration for the user, select Test . The Task Execution Results window appears with the test results.If
                                          			 any part of the test fails, verify the configuration for Cisco Unified
                                          			 MeetingPlace, Unity Connection, and the user.

Step 6

Repeat Step 2 through Step 5 for all
                                          			 remaining users.

### Testing Calendar Integration with Cisco Unified MeetingPlace or Cisco
                           	 Unified MeetingPlace Express

Step 1

Sign in to Cisco Unified MeetingPlace as an
                                          			 end user.

Step 2

Select Schedule .

Step 3

Enter values in the required fields to
                                          			 schedule a new meeting for the current time, and invite a user who has an
                                          			 account on Unity Connection.

Step 4

Sign in to the Unity Connection mailbox of
                                          			 the user that you invited to the Cisco Unified MeetingPlace meeting in Step 3 .

Step 5

If the user account is configured for speech
                                          			 access, say Play Meetings .

If the user account is not configured for
                                             				speech access, press 6 , and then follow the prompts to list
                                             				meetings.

Step 6

When you hear the system announce the Cisco
                                          			 Unified MeetingPlace meeting that you just scheduled, either say Join , or press the
                                          			 applicable keys on the phone keypad to join the meeting.

| Note | If you have already configured secure IMAP with SSL on Exchange
                                                				server and enabled the certificate for both IMAP and IIS, then follow the
                                                				section “Configuring
                                                   				  Exchange 2016, Exchange 2013, Exchange 2010 for Calendar and Contact
                                                   				  Integration” procedure on page 4-2 . |
|---|---|

| Step 1 | On the Exchange server, open the Internet Services (IIS) Manager application. |
|---|---|
| Step 2 | Go to Internet Information Services > 
                                             			 <Exchange server name> > Web Sites >  Default Web Site. |
| Step 3 | Right-click Exchange and select Properties . |
| Step 4 | In the Exchange
                                                				Properties dialog box, select the Virtual Directory tab. |
| Step 5 | From the Content For
                                                				This Resource Should Come From menu, select A Directory
                                                				Located On This Computer . |
| Step 6 | Confirm the Local Path is set to \\.\BackOfficeStorage\<your-domain.com>\MBX . |
| Step 7 | Select the Read check
                                             			 box. |
| Step 8 | Select the Directory Security tab. |
| Step 9 | From the Authentication
                                                				and Access Control menu, select Edit . |
| Step 10 | In the Authenticated
                                                				Access section of the Authentication Methods dialog box, check the check
                                             			 boxes for one or more of the following options: Integrated Windows authentication (sometimes referred to as
                                                      					 NTLM) Basic Authentication Digest Authentication for Windows Domain Servers |
| Step 11 | Select OK . |
| Step 12 | In the Exchange
                                                				Properties dialog box, select OK . |
| Step 13 | Go to Internet Information Services > <server name > > Web Service
                                                   				  Extensions . |
| Step 14 | In the right-hand pane, select WebDav and
                                             			 confirm that the status is “Allowed.” If the status is not “Allowed”, click Allow . |
| Step 15 | On the Exchange server, open the Exchange Management Console . |
| Step 16 | Go to Server
                                                				Configuration > Mailbox . |
| Step 17 | Do the following for each mailbox that you want to configure for
                                             			 the calendar and contact integration: In the upper middle pane, select the mailbox name. In the lower middle pane, select the WebDav tab. Right-click Exchange
                                                      					 (Default Web Site) and select Properties . In the Exchange
                                                      					 (Default Web Site) Properties dialog box, select the Authentication tab. Select Use One
                                                      					 or More Standard Authentication Methods and select the same authentication
                                                   				  method(s) that you configured in Step 10 . |
| Step 18 | Click OK . |
| Step 19 | Open the Exchange Management Shell . |
| Step 20 | In the Exchange
                                                				Management Shell , enter the following command: iisbreset /noforce |
| Step 21 | Press Enter . |

| Step 1 | On the Exchange Server, open the Exchange Management Shell application. |
|---|---|
| Step 2 | Enter the following command, where < Exchange server > is
                                             			 the IP address or fully qualified domain name of the Exchange server and < friendly name > is
                                             			 the friendly name that you selected for the Exchange server: new-exchangecertificate -generaterequest -domainname < Exchange server > -friendlyname < friendly name > -path c:\csr.txt Caution The domain name for the Exchange server must be the IP address
                                                               					 or the fully qualified domain name (recommended) so that the Unity Connection
                                                               					 server can successfully ping the Exchange server. Otherwise, the calendar and
                                                               					 contact integration may not function correctly. | Caution | The domain name for the Exchange server must be the IP address
                                                               					 or the fully qualified domain name (recommended) so that the Unity Connection
                                                               					 server can successfully ping the Exchange server. Otherwise, the calendar and
                                                               					 contact integration may not function correctly. |
| Caution | The domain name for the Exchange server must be the IP address
                                                               					 or the fully qualified domain name (recommended) so that the Unity Connection
                                                               					 server can successfully ping the Exchange server. Otherwise, the calendar and
                                                               					 contact integration may not function correctly. |
| Step 3 | Press Enter . A Certificate Signing Request (CSR) file with the name Csr.txt
                                                				is created in the root directory. |
| Step 4 | Send the CSR file to a Certification Authority (CA), which
                                             			 generates and sends back a new certificate. Note You must have a copy of the CA public root certificate or public root certificate chain. This certificate is needed for configuring
                                                         Unity Connection to trust the Exchange server. | Note | You must have a copy of the CA public root certificate or public root certificate chain. This certificate is needed for configuring
                                                         Unity Connection to trust the Exchange server. |
| Note | You must have a copy of the CA public root certificate or public root certificate chain. This certificate is needed for configuring
                                                         Unity Connection to trust the Exchange server. |
| Step 5 | Save the new certificate in a location that is accessible to the
                                             			 Exchange server on which you want to import the certificate. |
| Step 6 | On the Exchange Server, open the Exchange
                                                				Management Shell application. |
| Step 7 | Enter the following command, where <path> is the full path
                                             			 of the new certificate that you received from the CA: import-exchangecertificate -path <path> |
| Step 8 | Press Enter . |
| Step 9 | Enter the following command: dir
                                                   				  cert:\localmachine\my \| fl |
| Step 10 | Press Enter . |
| Step 11 | Highlight the “thumbprint” property and press Ctrl-C to copy it to the clipboard. |
| Step 12 | If Unity Connection is configured to use IMAP to access both email and calendar data from Exchange server, enter the following
                                             command, where <thumbprint> is the “thumbprint” that you copied in Step 11 : enable-exchangecertificate -thumbprint <thumbprint> -services "IIS,IMAP" If Unity Connection is not configured to use IMAP but configured to use calendar data from Exchange server, enter the following
                                                command, where <thumbprint> is the “thumbprint” that you copied in Step 11 : enable-exchangecertificate -thumbprint <thumbprint> -services "IIS" |
| Step 13 | Press Enter . |
| Step 14 | If you want data transmitted as clear text, skip the remaining
                                             			 steps in this procedure and continue with the “Configuring
                                                				Unity Connection for Calendar and Contact Integration” section on
                                                				page 4-4 . Otherwise, open the IIS Manager application. |
| Step 15 | Go to IIS > <server name > > Web
                                                   				  Sites > Default Web
                                                   				  Site . |
| Step 16 | Right-click Default Web Site and select Properties . |
| Step 17 | In the Properties dialog box, select the Directory Security tab. |
| Step 18 | From the Secure
                                                				Communications menu, select Edit . |
| Step 19 | Check the Require Secure Channel check box. |
| Step 20 | Select OK . |
| Step 21 | In the Properties dialog box, select OK . |

| Caution | The domain name for the Exchange server must be the IP address
                                                               					 or the fully qualified domain name (recommended) so that the Unity Connection
                                                               					 server can successfully ping the Exchange server. Otherwise, the calendar and
                                                               					 contact integration may not function correctly. |
|---|---|

| Note | You must have a copy of the CA public root certificate or public root certificate chain. This certificate is needed for configuring
                                                         Unity Connection to trust the Exchange server. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services . You can modify an
                                          			 existing unified messaging service or create a new service using Add New . |
|---|---|
| Step 2 | On the New Unified Messaging Service page, in the Type list, select Exchange/BPOS-D and check the Enabled check box to enable the unified messaging
                                          			 service. |
| Step 3 | Enter the details of the required fields and select Save . (For information on each field, see Help> This Page ). Note Make sure to
                                                      				check the Access Exchange Calendars and Contacts check box under Service Capabilities menu. | Note | Make sure to
                                                      				check the Access Exchange Calendars and Contacts check box under Service Capabilities menu. |
| Note | Make sure to
                                                      				check the Access Exchange Calendars and Contacts check box under Service Capabilities menu. |
| Step 4 | Select Test and a message appears indicating whether the
                                          			 configuration has been successfully verified. If the verification fails, follow
                                          			 the above configuration steps to ensure that they have been properly
                                          			 implemented. |

| Note | Make sure to
                                                      				check the Access Exchange Calendars and Contacts check box under Service Capabilities menu. |
|---|---|

| Note | There must be a user account in Active Directory for each Unity Connection user configured for unified messaging. Also, there
                                          must be a corresponding mailbox for each user account in Exchange 2019, Exchange 2016, Exchange 2013, Exchange 2010 that communicates
                                          with the Unity Connection server. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Users and select Users . Select an applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, in the Edit menu,
                                          			 select Unified Messaging Accounts . |
| Step 3 | On the Unified Messaging Accounts page, select Add New . Note Make sure that a unified messaging service is configured before
                                                      				creating unified messaging accounts. | Note | Make sure that a unified messaging service is configured before
                                                      				creating unified messaging accounts. |
| Note | Make sure that a unified messaging service is configured before
                                                      				creating unified messaging accounts. |
| Step 4 | On the New Unified Messaging Accounts page, select the following
                                          			 details: In Unified
                                                      						Messaging Service drop-down, select the unified messaging service created
                                                   					 in the section Configuring
                                                      						Unity Connection for Calendar and Contact Integration, page 4-4 . From the Account
                                                      						Information menu, in the Use This
                                                      						Email Address field, enter the Exchange email address in Active Directory
                                                   					 for the user. |
| Step 5 | In the Service
                                             				Capabilities menu, check the Access Exchange Calendar and Contacts check box and
                                          			 select Save . |
| Step 6 | Check the calendar and contact configuration for the user, selecting Test . The Task Execution Results window appears with the test results. If any part of the test fails, verify the configuration for Exchange 2019, Exchange
                                          2016, Exchange 2013, or Exchange 2010, Active Directory, Unity Connection, and the user. |
| Step 7 | Repeat Step 2 through Step 6 for all
                                          			 remaining users. |

| Note | Make sure that a unified messaging service is configured before
                                                      				creating unified messaging accounts. |
|---|---|

| Step 1 | Sign in to Outlook. |
|---|---|
| Step 2 | On the Go menu,
                                          			 select Calendar . |
| Step 3 | On the File menu,
                                          			 select New > Meeting
                                                				  Request . |
| Step 4 | Enter values in the required fields to schedule a new meeting
                                          			 for the current time, and invite a user who has an account on Unity Connection.
                                          			 Select Send . |
| Step 5 | Sign in to the Unity Connection mailbox of the user that you
                                          			 invited to the Outlook meeting: If the user account is configured for speech access, say Play Meetings . If the user account is not configured for speech access, press 6 , and then follow the prompts to list meetings. Unity Connection reads the information about the Exchange 2019, 2016, 2013, 2010 meetings. |

| Step 1 | Sign in to the Cisco Unified MeetingPlace Application Server as
                                          			 an administrator. |
|---|---|
| Step 2 | Select User
                                                				  Configuration > User
                                                				  Profiles . |
| Step 3 | Select Add New . |
| Step 4 | Enter the following values in the required fields to create a
                                          			 privileged service account: First Name Leave this field blank. Last Name Enter Cisco Unity Connection . User ID Enter cucsvc or another user
                                                         							 ID that you want. User Password Enter the applicable
                                                         							 password. Profile Number Enter the applicable
                                                         							 profile number. Profile Password Enter the applicable
                                                         							 profile password. Type of User Select System Administrator . Note The values
                                                      				that you enter for the User ID, User Password, Profile Number, and Profile Password fields are used in the “Configuring
                                                         				  Unity Connection for Calendar Integration” section on page 4-8 . | First Name | Leave this field blank. | Last Name | Enter Cisco Unity Connection . | User ID | Enter cucsvc or another user
                                                         							 ID that you want. | User Password | Enter the applicable
                                                         							 password. | Profile Number | Enter the applicable
                                                         							 profile number. | Profile Password | Enter the applicable
                                                         							 profile password. | Type of User | Select System Administrator . | Note | The values
                                                      				that you enter for the User ID, User Password, Profile Number, and Profile Password fields are used in the “Configuring
                                                         				  Unity Connection for Calendar Integration” section on page 4-8 . |
| First Name | Leave this field blank. |
| Last Name | Enter Cisco Unity Connection . |
| User ID | Enter cucsvc or another user
                                                         							 ID that you want. |
| User Password | Enter the applicable
                                                         							 password. |
| Profile Number | Enter the applicable
                                                         							 profile number. |
| Profile Password | Enter the applicable
                                                         							 profile password. |
| Type of User | Select System Administrator . |
| Note | The values
                                                      				that you enter for the User ID, User Password, Profile Number, and Profile Password fields are used in the “Configuring
                                                         				  Unity Connection for Calendar Integration” section on page 4-8 . |
| Step 5 | Select Save . |
| Step 6 | Sign out of Cisco Unified MeetingPlace. |
| Step 7 | In the Address field of a web browser, if SSL is not enabled,
                                          			 enter the following URL (where <server> is the IP address or host name of
                                          			 the Cisco Unified MeetingPlace server): http://<server>/webservices/services/meetingservice?wsdl If SSL is enabled, enter the following URL: https://<server>/webservices/services/meetingservice?wsdl |
| Step 8 | Press Enter . |
| Step 9 | When prompted to sign in, enter the user ID and password for the
                                          			 privileged service account. The Cisco Unified MeetingPlace Web Services Description Language
                                             				(WSDL) download page appears with the title “XFire Services”. |

| First Name | Leave this field blank. |
|---|---|
| Last Name | Enter Cisco Unity Connection . |
| User ID | Enter cucsvc or another user
                                                         							 ID that you want. |
| User Password | Enter the applicable
                                                         							 password. |
| Profile Number | Enter the applicable
                                                         							 profile number. |
| Profile Password | Enter the applicable
                                                         							 profile password. |
| Type of User | Select System Administrator . |

| Note | The values
                                                      				that you enter for the User ID, User Password, Profile Number, and Profile Password fields are used in the “Configuring
                                                         				  Unity Connection for Calendar Integration” section on page 4-8 . |
|---|---|

| Step 1 | Sign in to Cisco Unified MeetingPlace Express and select Administration . |
|---|---|
| Step 2 | Select User
                                                				  Configuration > User Profile
                                                				  Management . |
| Step 3 | Select Add New . |
| Step 4 | Enter the following values in the required fields to create an
                                          			 API user: First Name Leave this field blank. Last Name Enter Cisco Unity Connection . User ID Enter cucsvc or another user
                                                         							 ID that you want. User Password Enter the applicable
                                                         							 password. Profile Number Enter the applicable
                                                         							 profile number. Type of User Select API User . Note The values
                                                      				that you enter for the User ID, User Password, and Profile Number fields are used in the “Configuring
                                                         				  Unity Connection Users for Calendar Integration” section on page 4-9 . | First Name | Leave this field blank. | Last Name | Enter Cisco Unity Connection . | User ID | Enter cucsvc or another user
                                                         							 ID that you want. | User Password | Enter the applicable
                                                         							 password. | Profile Number | Enter the applicable
                                                         							 profile number. | Type of User | Select API User . | Note | The values
                                                      				that you enter for the User ID, User Password, and Profile Number fields are used in the “Configuring
                                                         				  Unity Connection Users for Calendar Integration” section on page 4-9 . |
| First Name | Leave this field blank. |
| Last Name | Enter Cisco Unity Connection . |
| User ID | Enter cucsvc or another user
                                                         							 ID that you want. |
| User Password | Enter the applicable
                                                         							 password. |
| Profile Number | Enter the applicable
                                                         							 profile number. |
| Type of User | Select API User . |
| Note | The values
                                                      				that you enter for the User ID, User Password, and Profile Number fields are used in the “Configuring
                                                         				  Unity Connection Users for Calendar Integration” section on page 4-9 . |
| Step 5 | Select Save . |
| Step 6 | Sign out of Cisco Unified MeetingPlace Express. If you do not sign out of Cisco Unified MeetingPlace Express,
                                             				the test fails in the Testing
                                                				  Calendar Integration with Cisco Unified MeetingPlace or Cisco Unified
                                                				  MeetingPlace Express, page 4-9 . |
| Step 7 | In the Address field of a web browser: if SSL is not enabled, enter the following URL (where
                                                   					 <server> is the IP address or host name of the Cisco Unified MeetingPlace
                                                   					 Express server): http://<server>.com/webservices/services/meetingservice?wsdl If SSL is enabled, enter the following URL: https://<server>.com/webservices/services/meetingservice?wsdl |
| Step 8 | Press Enter . |
| Step 9 | When prompted
                                          			 to sign in, enter the user ID and password for the API user. The Cisco Unified MeetingPlace Express WSDL download page
                                             				appears with the title “XFire Services.” |

| First Name | Leave this field blank. |
|---|---|
| Last Name | Enter Cisco Unity Connection . |
| User ID | Enter cucsvc or another user
                                                         							 ID that you want. |
| User Password | Enter the applicable
                                                         							 password. |
| Profile Number | Enter the applicable
                                                         							 profile number. |
| Type of User | Select API User . |

| Note | The values
                                                      				that you enter for the User ID, User Password, and Profile Number fields are used in the “Configuring
                                                         				  Unity Connection Users for Calendar Integration” section on page 4-9 . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services. |
|---|---|
| Step 2 | Modify an existing unified messaging service or create a new
                                          			 service by selecting Add New . |
| Step 3 | On the New Unified Messaging Service page, in the Type list, select MeetingPlace 8.x and check the Enabled check box to enable
                                          			 unified messaging with Cisco Unified MeetingPlace server. |
| Step 4 | Enter the values of the required fields and select Save . (For information on each field, see Help> This Page ). Note Make sure to
                                                      				check the User MeetingPlace Meetings and MeetingPlace Scheduling and Joining check boxes under Service Capabilities menu. | Note | Make sure to
                                                      				check the User MeetingPlace Meetings and MeetingPlace Scheduling and Joining check boxes under Service Capabilities menu. |
| Note | Make sure to
                                                      				check the User MeetingPlace Meetings and MeetingPlace Scheduling and Joining check boxes under Service Capabilities menu. |
| Step 5 | To check the integration with Cisco Unified MeetingPlace, select Test . The Task Execution Results window appears with the test results.
                                          			 If any part of the test fails, verify the configuration for Cisco Unified
                                          			 MeetingPlace and Unity Connection. |

| Note | Make sure to
                                                      				check the User MeetingPlace Meetings and MeetingPlace Scheduling and Joining check boxes under Service Capabilities menu. |
|---|---|

| Caution | Cisco Unified
                                          		  MeetingPlace must have an end user for each Unity Connection user that you are
                                          		  configuring. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Users and select Users . Select an applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Unified Messaging Accounts . |
| Step 3 | On the Unified Messaging Accounts page, select Add New . The New Unified Messaging Account page
                                          			 appears. |
| Step 4 | On the New Unified Messaging Account page, select the Unified Messaging Service for Cisco Unified MeetingPlace.
                                          			 Enter the values of the required fields and select Save. (For information on
                                          			 each field, see Help> This Page ). Note Make sure to
                                                      				check the MeetingPlace Scheduling and Joining and Primary Meeting Service check boxes under the Service Capabilities menu. | Note | Make sure to
                                                      				check the MeetingPlace Scheduling and Joining and Primary Meeting Service check boxes under the Service Capabilities menu. |
| Note | Make sure to
                                                      				check the MeetingPlace Scheduling and Joining and Primary Meeting Service check boxes under the Service Capabilities menu. |
| Step 5 | To check the calendar configuration for the user, select Test . The Task Execution Results window appears with the test results.If
                                          			 any part of the test fails, verify the configuration for Cisco Unified
                                          			 MeetingPlace, Unity Connection, and the user. |
| Step 6 | Repeat Step 2 through Step 5 for all
                                          			 remaining users. |

| Note | Make sure to
                                                      				check the MeetingPlace Scheduling and Joining and Primary Meeting Service check boxes under the Service Capabilities menu. |
|---|---|

| Step 1 | Sign in to Cisco Unified MeetingPlace as an
                                          			 end user. |
|---|---|
| Step 2 | Select Schedule . |
| Step 3 | Enter values in the required fields to
                                          			 schedule a new meeting for the current time, and invite a user who has an
                                          			 account on Unity Connection. |
| Step 4 | Sign in to the Unity Connection mailbox of
                                          			 the user that you invited to the Cisco Unified MeetingPlace meeting in Step 3 . |
| Step 5 | If the user account is configured for speech
                                          			 access, say Play Meetings . If the user account is not configured for
                                             				speech access, press 6 , and then follow the prompts to list
                                             				meetings. |
| Step 6 | When you hear the system announce the Cisco
                                          			 Unified MeetingPlace meeting that you just scheduled, either say Join , or press the
                                          			 applicable keys on the phone keypad to join the meeting. |