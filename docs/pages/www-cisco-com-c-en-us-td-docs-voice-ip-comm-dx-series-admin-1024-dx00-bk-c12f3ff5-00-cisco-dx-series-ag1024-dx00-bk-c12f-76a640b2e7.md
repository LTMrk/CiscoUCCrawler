---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-dx-series-admin-1024-dx00-bk-c12f3ff5-00-cisco-dx-series-ag1024-dx00-bk-c12f-76a640b2e7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/dx/series/admin/1024/DX00_BK_C12F3FF5_00_cisco-dx-series-ag1024/DX00_BK_C12F3FF5_00_cisco-dx-series-ag1024_chapter_0111.html
retrieved_at: 2026-08-21T04:58:16.521334+00:00
---

Cisco DX Series Administration Guide, Release 10.2(4)

# Cisco DX Series Administration Guide, Release 10.2(4)

Updated: June 25, 2015

Chapter: Self Care Portal Management

## Chapter: Self Care Portal Management

- Self Care Portal	 Overview

- Set Up Access to	 Self Care Portal

- Customize Self Care Portal Display

# Self Care Portal Management

## Self Care Portal
	 Overview

From the Cisco Unified Communications Self Care Portal, users can
		  customize and control phone features and settings. For information about the
		  Self Care Portal, see the Cisco Unified Communications Self Care Portal User Guide located at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-user-guide-list.html .

As the administrator, you control access to the Self Care Portal. You
		  must also provide information to your users so that they can access the Self
		  Care Portal.

Before a user can access the Cisco Unified Communications Self Care
		Portal, you must use Cisco Unified Communications Manager Administration to add
		the user to a standard Cisco Unified Communications Manager End User group.

You must provide end users with the following information about the Self
		Care Portal:

The URL to access the application. This URL is:

http://<server_name:portnumber>/ucmuser/ ,
			 where server_name is the host on which the web server is installed and
			 portnumber is the port number on that host.

A user ID and default password to access  the application.

An overview of the tasks that users can accomplish with  the
			 portal.

These settings correspond to the values that you entered when you added
		the user to Cisco Unified Communications Manager.

For more information, see:

Cisco Unified Communications Manager Administration
				Guide , "Access Control  Group Setup" chapter

Cisco Unified Communications Manager Administration
				Guide , "End User Setup" chapter

Cisco Unified Communications Manager Administrator
				Guide , "Role Setup" chapter

## Set Up Access to
	 Self Care Portal

Use this procedure to enable a user to access the Self Care Portal.

## Customize Self Care Portal Display

Most options display on the Self Care Portal. However, you must set the following options by using Enterprise Parameters Configuration settings in Cisco Unified Communications Manager Administration:

Show Ring Settings

Show Line Label Settings

The settings apply to all Self Care Portal pages at your site.

| Step 1 | In Cisco
			 Unified Communications Manager Administration, select User
				  Management > End User . |
|---|---|
| Step 2 | Search for the
			 user and click the user ID link. |
| Step 3 | Ensure that
			 the user has a password and PIN configured. |
| Step 4 | Select Save . |

| Note | The settings apply to all Self Care Portal pages at your site. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select System > Enterprise Parameters . |
|---|---|
| Step 2 | In the Self Care Portal area, set the Self Care Portal Default Server field. |
| Step 3 | Enable or disable the parameters that the users can access in the portal. |
| Step 4 | Select Save . |