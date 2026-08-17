---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-011101--753544275f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_011101.html
retrieved_at: 2026-08-17T02:30:25.727271+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting
	 Custom Roles

## Chapter: Troubleshooting
	 Custom Roles

# Troubleshooting
                     	 Custom Roles

This section covers the problems that you might face while creating,
                        		updating, deleting or assigning custom roles to users.

## Troubleshooting
                        	 Custom Roles

This section covers the problems that you might face while creating,
                           		updating, deleting or assigning custom roles to users.

### Unable to
                           	 Configure Custom Role

While creating,
                              		updating or deleting a custom role, If you receive the "Not Authorised" error
                              		message, confirm that you are logged in as a system administrator. Only a user
                              		with system administrator role can create, update or delete custom roles.

### Getting "Not
                           	 Authorized" Error Message on Role Assignment or Unassignment

- Confirm that you are not
                                       			 trying to assign any of the system roles to the user. A system role can be
                                       			 assigned to users only by the system administrator.

- confirm that you have a
                                       			 role with Manage Users:
                                          				Assign/Unassign Roles privilege. Do the following steps to confirm the
                                       			 same:

In Cisco Unity
                                          			 Connection Administration page, go to Users and
                                          			 select your user name.

Go to Edit > Roles and
                                          			 note the role in the Assigned
                                             				Role field.

Go to System
                                             				Settings > Roles > Custom Roles page and on the Search Custom
                                             				Role page select the role assigned to you.

On the Edit
                                          			 Custom Role page check if the check box for the "Manage Users: Assign/Unassign
                                          			 Roles" privilege is checked. If the checkbox is not checked that means you do
                                          			 not have the privilege to assign or unassign roles.

Contact the
                                          			 system administrator to assign the privilege to the role assigned to you.

### Getting "Not
                           	 Authorized" Error on Cisco Unity Connection Administration Pages

After logging in to
                              		Cisco Unity Connection Administration page, if you are getting "Not Authorized"
                              		error on every page, contact the system administrator to check that you have a
                              		role with "Read Access To System Configuration Data - Read Access " privilege.

For information
                              		about custom roles and its configurations, see the Custom Roles section in
                              		the "User Attributes" chapter of the System Administration Guide for Cisco
                              		Unity Connection Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html

| Step 1 | In Cisco Unity
                                          			 Connection Administration page, go to Users and
                                          			 select your user name. |
|---|---|
| Step 2 | Go to Edit > Roles and
                                          			 note the role in the Assigned
                                             				Role field. |
| Step 3 | Go to System
                                             				Settings > Roles > Custom Roles page and on the Search Custom
                                             				Role page select the role assigned to you. |
| Step 4 | On the Edit
                                          			 Custom Role page check if the check box for the "Manage Users: Assign/Unassign
                                          			 Roles" privilege is checked. If the checkbox is not checked that means you do
                                          			 not have the privilege to assign or unassign roles. |
| Step 5 | Contact the
                                          			 system administrator to assign the privilege to the role assigned to you. |