---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-appendix-011111-d21e8afa3a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_appendix_011111.html
retrieved_at: 2026-08-17T02:30:34.626869+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting
	 Phone View

## Chapter: Troubleshooting
	 Phone View

# Troubleshooting
                     	 Phone View

## Problems with
                        	 Phone View

Use the
                           		troubleshooting information in this section if an error message appears when
                           		the user attempts to use Phone View. Consider the following possible causes:

- The application user is
                              		  configured incorrectly. See the Application User Configured Incorrectly section.

- The user phone
                              		  configuration is not correct. See the User Phone Configuration Not Correct

- The phone system
                              		  integration is configured incorrectly. See the Phone System Integration Configured Incorrectly

The Phone View
                           		feature is supported only with Cisco Unified Communications Manager phone
                           		system integrations.

The Phone View
                           		feature may not function correctly outside a firewall or through a VPN router.
                           		Requirements for Phone View are available in the " Requirements for Phone
                              		  View " section of the System Requirements for Cisco Unity Connection
                           		Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

### Application User
                           	 Configured Incorrectly

The problem may be caused by the
                                 		  incorrect configuration of the application user on the Cisco Unified
                                 		  Communications Manager server.

To Verify the Configuration of the Application User

In Cisco Unified
                                          			 Communications Manager Administration, on the User Management menu, select Application User .

On the Find and List
                                          			 Application Users page, select Find .

Select the user ID of the
                                          			 application user that is used by Phone View.

On the Application User Configuration page, under Application User
                                          			 Information, select Edit Credential .

On the Credential Configuration page, confirm that the following
                                          			 check boxes are checked:

- User Must Change at Next Login

- Does Not Expire

Select Save .

In the Related Links box, select Back to User and select Go .

On the Application User Configuration page, under Application User
                                          			 Information, in the Password field, reenter the password.

In the Confirm Password field, reenter the password.

Under Device Information, in the Controlled Devices field, confirm
                                          			 that the devices that are associated with the application user account are
                                          			 correct and select Save .

On the System menu, select Enterprise Parameters .

On the Enterprise Parameters Configuration page, under Phone URL
                                          			 Parameters, in the URL Authentication field, confirm that the URL is correct.

If you made any changes, select Save .

### User Phone
                           	 Configuration Not Correct

One possible cause may be that the
                              		configuration on the user phone is not current. You can reboot the phone so
                              		that it reloads the configuration from the Cisco Unified CM server.

Another possible cause is that the user phone is not supported.

### Phone System
                           	 Integration Configured Incorrectly

The problem may be caused by the
                              		incorrect configuration of the Cisco Unified CM phone system integration in
                              		Cisco Unity Connection Administration.

### To Verify the
                           	 Configuration of the Cisco Unified Communications Manager Phone System
                           	 Integration

In Cisco Unity Connection
                                          			 Administration, expand Telephony Integration , then select Phone Systems .

On the Search Phone Systems
                                          			 page, select the name of the phone system.

On the Phone System Basics
                                          			 page, under Phone View Settings, confirm that the Enable Phone View check box is checked.

In the CTI Phone Access Username field, confirm that the name of
                                          			 the application user in Cisco Unified CM Administration is correct.

In the CTI Phone Access Password field, reenter the password of
                                          			 the application user in Cisco Unified CM Administration and select Save .

### To Verify the
                           	 Configuration of the User

In Cisco Unity Connection
                                          			 Administration, expand Users , then select Users . On the Search Users page, select the name of the user.

On the Edit User Basics page,
                                          			 on the Edit menu, select Phone Menu ..

On the Phone Menu page, under
                                          			 Finding Messages with Message Locator, confirm that the Enable check box is checked.

Confirm that the Enable Phone View check box is checked and select Save .

## Using Traces to
                        	 Troubleshoot Phone View Issues

You can use traces to troubleshoot
                           		phone view issues. For detailed instructions on enabling the applicable traces
                           		and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting section.

| Step 1 | In Cisco Unified
                                          			 Communications Manager Administration, on the User Management menu, select Application User . |
|---|---|
| Step 2 | On the Find and List
                                          			 Application Users page, select Find . |
| Step 3 | Select the user ID of the
                                          			 application user that is used by Phone View. |
| Step 4 | On the Application User Configuration page, under Application User
                                          			 Information, select Edit Credential . |
| Step 5 | On the Credential Configuration page, confirm that the following
                                          			 check boxes are checked: User Must Change at Next Login Does Not Expire |
| Step 6 | Select Save . |
| Step 7 | In the Related Links box, select Back to User and select Go . |
| Step 8 | On the Application User Configuration page, under Application User
                                          			 Information, in the Password field, reenter the password. |
| Step 9 | In the Confirm Password field, reenter the password. |
| Step 10 | Under Device Information, in the Controlled Devices field, confirm
                                          			 that the devices that are associated with the application user account are
                                          			 correct and select Save . |
| Step 11 | On the System menu, select Enterprise Parameters . |
| Step 12 | On the Enterprise Parameters Configuration page, under Phone URL
                                          			 Parameters, in the URL Authentication field, confirm that the URL is correct. |
| Step 13 | If you made any changes, select Save . |

| Step 1 | In Cisco Unity Connection
                                          			 Administration, expand Telephony Integration , then select Phone Systems . |
|---|---|
| Step 2 | On the Search Phone Systems
                                          			 page, select the name of the phone system. |
| Step 3 | On the Phone System Basics
                                          			 page, under Phone View Settings, confirm that the Enable Phone View check box is checked. |
| Step 4 | In the CTI Phone Access Username field, confirm that the name of
                                          			 the application user in Cisco Unified CM Administration is correct. Note The name of the application user is case-sensitive. | Note | The name of the application user is case-sensitive. |
| Note | The name of the application user is case-sensitive. |
| Step 5 | In the CTI Phone Access Password field, reenter the password of
                                          			 the application user in Cisco Unified CM Administration and select Save . |

| Note | The name of the application user is case-sensitive. |
|---|---|

| Step 1 | In Cisco Unity Connection
                                          			 Administration, expand Users , then select Users . On the Search Users page, select the name of the user. |
|---|---|
| Step 2 | On the Edit User Basics page,
                                          			 on the Edit menu, select Phone Menu .. |
| Step 3 | On the Phone Menu page, under
                                          			 Finding Messages with Message Locator, confirm that the Enable check box is checked. |
| Step 4 | Confirm that the Enable Phone View check box is checked and select Save . |