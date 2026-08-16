---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-14-cup0-b-rcc-lync-server-integration-14-c-2091119e77
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/14/cup0_b_rcc-lync-server-integration-14/cup0_b_rcc-lync-server-integration-1251_chapter_01010.html
retrieved_at: 2026-08-16T16:34:57.313871+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

Updated: November 27, 2025

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## IM and Presence
                        	 Service Web Page Does Not Open from the Microsoft Lync Client Default Web
                        	 Browser.

Problem When the Microsoft Lync client user accesses the IM and Presence Service menu item, the
                              		  default web browser cannot connect to the IM and Presence Service node and the IM and Presence Service web page does not
                              		  open.

Solution When the Microsoft Lync client user accesses the IM and Presence Service menu item, IM and Presence Service should open a web
                              		  page in the user's default web browser. If the web browser cannot connect to
                              		  the IM and Presence Service node, check the
                              		  following:

Ensure that
                                       				JavaScript is enabled in the browser settings.

Enter the
                                       				following address in a web browser to verify that the browser can connect to
                                       				the IM and Presence Service node:
                                       				https:/ /imp_server_address :8443/cucmuser/showHomeMini.do?mini=true

Where imp_server_address is the hostname, FQDN, or IP address of  the IM and Presence Service node.

If you specified
                                       				an invalid IP address or FQDN for your IM and Presence Service node, repeat the
                                       				plug-in installation procedure, specifying the correct IM and Presence Service node address.

Add the web
                                                					 address of the IM and Presence Service node to the list of
                                                					 trusted web addresses in the browser on the Microsoft Lync client computer. In Microsoft Explorer, select Internet Options > Security > Trusted
                                                      						  Sites and add the following entry to the list of
                                                					 trusted web addresses:

https://<IM and
                                                   						Presence_server_name>

Add the
                                                					 HTTPS web address of your domain to the security zone of the IM and Presence Service node. In Microsoft
                                                					 Explorer, select Microsoft Internet
                                                      						  Explorer > Internet Options > Security > Local
                                                      						  Internet > Sites > Advanced and add the following entry
                                                					 to the list of web addresses for the security zone: https://*.<your_domain>

If an error
                                       				message appears informing the users that they do not have permission to use
                                       				this feature, you must enable the users for Microsoft Lync in
                                       				the IM and Presence Service node. See Remote Call Control Setup .

If an error
                                       				message appears regarding an un-trusted security certificate issue or similar
                                       				warning, select Continue . Most browsers allow you to download a
                                       				website security certificate and mark it as trusted.

## Lync Error When Using E.164 Numbers

Solution When you add the tel: value in the Line URI field shown in Enable Users in Lync Server Control Panel , do not add phone-context=dialstring if you are using E.164 numbers. For example, the Line URI field must be configured as "tel:+19728131000" and not "tel:+19728131000;phone-context=dialstring."

If phone-context=dialstring is added, the Lync client will produce an error and will not send out the initial INVITE to the Lync server to begin the
                              sign-in sequence.

## Synchronize User to Cisco Unified Communications Manager

If the user is provisioned in AD but does not appear in Cisco Unified Communications Manager , perform the following procedure to synchronize the user to Cisco Unified Communications Manager .

Step 1

Select Cisco Unified Communications Manager Administration > System > LDAP > LDAP Directory (select the LDAP Configuration Name that matches AD).

Step 2

Verify that the configuration is correct.

Step 3

Select Perform Full Sync Now and select OK when prompted.

Step 4

Select Cisco Unified Communications Manager Administration > User Management > End User .

The user should now display in the user list.

## Enable IM and
                        	 Presence for User ID

If the
                              		  user is configured in Cisco Unified Communications
                                 			 Manager but does not appear in IM and Presence Service , perform the
                              		  following procedure.

Step 1

Select Cisco Unified Communications Manager Administration > User Management > End User .

Step 2

Search for the
                                       			 user.

Step 3

Select the user.

Step 4

Check the Enable
                                          				User for Unified CM IM and Presence check box.

Step 5

Select Save .

## Verify User Phone
                        	 Call Control at the Lync Client Is Enabled

If the
                              		  user has no call control at the Lync client, the user must complete the
                              		  following procedure.

Step 1

Sign in to the
                                       			 Lync client.

Step 2

Click the
                                       			 drop-down arrow on the top right of the window.

Step 3

Select Tools > Options > Phones .

Step 4

In the Phone
                                          				Integration area, select the option Enable
                                          				integration with your phone system .

Step 5

Select Advanced .

Step 6

Verify that the
                                       			 Automatic Configuration option is selected.

This option
                                          				allows the client to access the correct information from the Lync server
                                          				database.

Step 7

Select OK .

If the problem
                                          				persists, ensure that the user is sychronized from Cisco Unified Communications
                                             				  Manager and that the user is enabled for RCC in the IM and Presence Service node.

## Phone Icon with a Red X in the Status Bar in Microsoft Lync Client

Solution The integration configuration is successful if a user signs into Microsoft Lync client and sees the text "Call forwarding is on" or "Call forwarding is off" in the status bar at the bottom of the window. If there is a phone icon with a red X in the status bar, the integration is
                              unsuccessful. To resolve sign-in problems, you can initiate a trace of the Lync server to identify any problems with the INVITE/INFO
                              SIP message exchange sequence between the IM and Pesence server and the Microsoft Lync server. See the Microsoft Lync documentation for more information about Microsoft Lync server logging and Microsoft Lync client logging.

| Step 1 | Select Cisco Unified Communications Manager Administration > System > LDAP > LDAP Directory (select the LDAP Configuration Name that matches AD). |
|---|---|
| Step 2 | Verify that the configuration is correct. |
| Step 3 | Select Perform Full Sync Now and select OK when prompted. |
| Step 4 | Select Cisco Unified Communications Manager Administration > User Management > End User . The user should now display in the user list. |

| Step 1 | Select Cisco Unified Communications Manager Administration > User Management > End User . |
|---|---|
| Step 2 | Search for the
                                       			 user. |
| Step 3 | Select the user. |
| Step 4 | Check the Enable
                                          				User for Unified CM IM and Presence check box. |
| Step 5 | Select Save . |

| Step 1 | Sign in to the
                                       			 Lync client. |
|---|---|
| Step 2 | Click the
                                       			 drop-down arrow on the top right of the window. |
| Step 3 | Select Tools > Options > Phones . |
| Step 4 | In the Phone
                                          				Integration area, select the option Enable
                                          				integration with your phone system . |
| Step 5 | Select Advanced . |
| Step 6 | Verify that the
                                       			 Automatic Configuration option is selected. This option
                                          				allows the client to access the correct information from the Lync server
                                          				database. |
| Step 7 | Select OK . If the problem
                                          				persists, ensure that the user is sychronized from Cisco Unified Communications
                                             				  Manager and that the user is enabled for RCC in the IM and Presence Service node. |