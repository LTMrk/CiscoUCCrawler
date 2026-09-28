---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8832-english-adminguide-cs88-b-conference-8832-admin-guide-cucm-cs88--aa11a93396
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8832/english/adminguide/cs88_b_conference-8832-admin-guide-cucm/cs88_b_conference-8832-admin-guide-cucm_chapter_0100.html
retrieved_at: 2026-08-21T13:36:50.688826+00:00
---

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

# Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Self Care Portal Management

## Chapter: Self Care Portal Management

# Self Care Portal Management

## Self Care Portal
                        	 Overview

From the Cisco Unified Communications Self Care Portal, users can
                              		  customize and control phone features and settings.

As the administrator, you control access to the Self Care Portal. You
                              		  must also provide information to your users so that they can access the Self
                              		  Care Portal.

Before a user can access the Cisco Unified Communications Self Care Portal, you must use Cisco Unified
                                 				Communications Manager Administration to add the user to a standard Cisco Unified
                                 				Communications Manager End User group.

You must provide end users with the following information about the Self
                              		Care Portal:

The URL to access the application. This URL is:

https://<server_name:portnumber>/ucmuser/ , where server_name is the host on which the web server is installed, and portnumber is the port number on that host.

A user ID and default password to access  the application.

An overview of the tasks that users can accomplish with  the
                                    			 portal.

These settings correspond to the values that you entered when you added the user to Cisco Unified
                                 				Communications Manager .

For more information, see the documentation for your particular Cisco Unified
                                 				Communications Manager release.

## Set Up User Access to
                        	 the Self Care Portal

Before a user can access the Self Care Portal, you need to authorize the access.

Step 1

In Cisco Unified
                                          				Communications Manager Administration, select User Management > End User .

Step 2

Search for the
                                       			 user.

Step 3

Click the user ID link.

Step 4

Ensure that
                                       			 the user has a password and PIN configured.

Step 5

In the Permission Information section, ensure that the Groups list includes Standard CCM End Users .

Step 6

Select Save .

## Customize the Self Care Portal Display

Most options display on the Self Care Portal. However, you must set the following options by using Enterprise Parameters Configuration
                              settings in Cisco Unified Communications Manager Administration:

Show Ring Settings

Show Line Label Settings

The settings apply to all Self Care Portal pages at your site.

Step 1

In Cisco Unified Communications Manager Administration, select System > Enterprise Parameters .

Step 2

In the Self Care Portal area, set the Self Care Portal Default Server field.

Step 3

Enable or disable the parameters that the users can access in the portal.

Step 4

Select Save .

| Step 1 | In Cisco Unified
                                          				Communications Manager Administration, select User Management > End User . |
|---|---|
| Step 2 | Search for the
                                       			 user. |
| Step 3 | Click the user ID link. |
| Step 4 | Ensure that
                                       			 the user has a password and PIN configured. |
| Step 5 | In the Permission Information section, ensure that the Groups list includes Standard CCM End Users . |
| Step 6 | Select Save . |

| Note | The settings apply to all Self Care Portal pages at your site. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select System > Enterprise Parameters . |
|---|---|
| Step 2 | In the Self Care Portal area, set the Self Care Portal Default Server field. |
| Step 3 | Enable or disable the parameters that the users can access in the portal. |
| Step 4 | Select Save . |