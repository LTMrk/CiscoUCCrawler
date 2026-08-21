---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-maintenance-guide-pcce-b-1501-f-79e5222a0f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/maintenance/guide/pcce_b_1501_features-guide/pcce_m_1501_media_server.html
retrieved_at: 2026-08-21T12:10:46.252300+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Media Server

## Chapter: Media Server

# Media Server

## About Media Server

Many of the optional features in Packaged CCE require a Cisco Unified Customer Voice Portal (CVP) media server to store and
                              serve supporting .wav files. This chapter describes how to set up a CVP media server. It also describes expanded call variable settings that are
                              related to the media server and requirements for accessing a media server in call routing scripts.

The features that require a CVP media server include Agent Greeting, Courtesy Callback, Post-Call Survey, and Whisper Announcement.

## Prepare a Media Server

A media server is installed by default on each of the CVP servers in a Packaged CCE deployment.

### Before you begin

When IIS is installed, ensure the Directory Browsing option is selected; if it is not, configure it by going to Start > Control Panel > Administrative Tools > Server Manager . In the Server Manager window, navigate to the IIS section and locate the Roles and Features section. Check if the required role services are installed, and in the Common HTTP Features list, make sure to select Directory Browsing .

Step 1

Ensure that IIS is properly configured and running on the server. It must be listening on port 80. To validate proper configuration
                                       of the media server, launch a browser from a remote machine that is able to ping the CVP server and attempt to access and
                                       play one of the default media files installed during the CVP installation such as http://<cvp_ip>/en-us/app/en_1.wav . If the file is accessible, the media server is installed correctly.

Use Microsoft IIS with Unified CVP. This component is automatically installed as part of the CVP server package installation.

Step 2

Ensure the server is accessible to CVP, Unified CCE, and your agent desktops.

Step 3

Perform the following steps:

On the taskbar, click Start , point to Administrative Tools , and then click Server Manager .

In the Server Manager hierarchy pane, expand Roles , and then click Web Server (IIS) .

In the Web Server (IIS) pane, scroll to the Role Services section, and then click Add Role Services .

On the Select Role Services page of the Add Role Services wizard, expand FTP Server .

Select FTP Service

To support ASP.NET membership or IIS Manager authentication for the FTP service, you need to select FTP Extensibility .

Click Next .

On the Confirm Installation Selections page, click Install.

On the Results page, click Close.

In the sites section, click Add FTP Site . Provide a site name and path to the same location as the http directory c:\inetpub\wwwroot.

Select your desired binding method, and specify to start immediately.

On the FTP SSL Settings, select Allow SSL Connections .

On the Authentication and Authorization section select the type of authentication required. If using basic, note the name and password of the account.

Select the authorization; for anonymous select Anonymous users .

Set the read and write permissions.

Step 4

Make sure that the FTP and the IIS share the same root directory.

The recording application writes the file to the media server directory structure, and the greeting playback call uses IIS
                                          to fetch the file. The en-us/app directory should be under the same root directory for FTP and IIS.

Step 5

Create a dedicated directory on the server to store your greeting files.

This lets you specify a lower cache timeout of 5 minutes for your agent greeting files that does not affect other more static
                                          files you may be serving from other directories. By default, the Record Greeting application posts the .wav file to the en-us/app directory under your web/ftp root directory. You may create a dedicated directory such as ag_gr under the en-us/app directory, and then indicate this in the Unified CCE script that invokes the recording application. Use the array for the
                                          expanded call variable call.user.microapp.ToExtVXML to send the ftpPath parameter to the recording application. Make sure the expanded call variable length is long enough, or
                                          it may get truncated and fail.

Step 6

To allow re-recorded greetings to replace their predecessor in a reasonable amount of time while minimizing requests for data
                                       to the media server from Cisco VVB , configure a cache expiration value in IIS Manager.

The ideal value varies depending on the number of agents you support and how often they re-record their greetings. Two minutes
                                          may be a reasonable starting point.

To configure a cache expiration value in IIS Manager:

Find the site you are using, go to the agent greeting folder you created (ag_gr), and then select HTTP Response Headers .

Click Set Common Headers on Actions panel.

Select Expire Web Content and set the desired value.

## Reference a Media Server in CCE Scripts

### Specify Media Server in Routing Scripts

When you configure media servers in CVP, you can specify a default media server. The benefit to specifying a default media
                                 server is that your scripts do not need a Set Variable node to access the default media server. For this to work, you must
                                 make sure that the files a script requests are stored on the default server.

If you do not define a default media server, or if you define a default but the files that your script requires are not stored
                                 on the default, then the script must include a Set Variable node to identify a media server.

To specify a media server that stores the files required by your script, use the following settings in the Set Variable node:

Object Type: Call.

Variable: Must use the user.microapp.media_server expanded call variable.

Value: Specify the HTTP path to the server. For example: “http://myserver.mydomain.net.” You must enclose the path in quotes.

Alternately you can specify an IP address in place of a hostname.

See the following example.

### Specify Greeting File Locale and Application Directories in Routing Scripts

CVP uses a default storage directory for media files: <web_server_root> /en-us/app . The physical location of the default storage directory is c:\inetpub\wwwroot\en-us\app . To take advantage of this, Packaged CCE call routing scripts automatically add en-us/app to the server name when constructing HTTP requests for media files. For example:

If the script node that defines the media server has a value of "http://myserver.mydomain.com," and

The script node that defines which audio file to play has a value of "5050_1.wav" (for an agent with a Person ID of 5050), then

The HTTP request for the file is automatically constructed as http://myserver.mydomain.com/en-us/app/5050_1.wav

If your greeting audio files are stored in a different locale directory, you must add a Set Variable node to your script that
                                 identifies the locale directory. As you must store your greeting files in a dedicated subdirectory under the locale, you must
                                 always add a Set Variable node that identifies that directory.

Step 1

Use these settings in the Set Variable node to specify your locale directory:

Object Type: Call.

Variable: Must use the user.microapp.locale expanded call variable.

Value: Specify the directory name. For example: "pt-br" (Portuguese-Brazil). You must enclose the path in quotes.

Step 2

Use these settings in the Set Variable node to specify your application directory:

Object Type: Call.

Variable: Must use the user.microapp.app_media_lib expanded call variable.

Value: Specify the directory name. For example: to use a directory "greet" in place of the default directory "app" , enter "greet" . To use a sub-directory "greet" under "app" enter "app/greet" . You must enclose the path in quotes.

### Verify Length for Media Server Locale and Application Directory Variables

To configure ECC variables. In Unified CCE Administration, navigate to Overview > Call Settings > Route Settings > Expanded Call Variables .

If you include Set Variable nodes for the media server, locale, and/or application directories, make sure that the values
                                             you set for them do not exceed the Maximum Length settings for their corresponding expanded call variables.

For example, if you include a Set Variable node for the media server with a value of "http://mysubdomain.mydomain.co.uk" , the string is 33 characters long. Therefore, the Maximum Length setting for the user.microapp.media_server expanded call
                                             variable must be 33 or greater. Otherwise, the server name is truncated in the HTTP request for the file and the file is not
                                             found.

| Step 1 | Ensure that IIS is properly configured and running on the server. It must be listening on port 80. To validate proper configuration
                                       of the media server, launch a browser from a remote machine that is able to ping the CVP server and attempt to access and
                                       play one of the default media files installed during the CVP installation such as http://<cvp_ip>/en-us/app/en_1.wav . If the file is accessible, the media server is installed correctly. Note Use Microsoft IIS with Unified CVP. This component is automatically installed as part of the CVP server package installation. | Note | Use Microsoft IIS with Unified CVP. This component is automatically installed as part of the CVP server package installation. |
|---|---|---|---|
| Note | Use Microsoft IIS with Unified CVP. This component is automatically installed as part of the CVP server package installation. |
| Step 2 | Ensure the server is accessible to CVP, Unified CCE, and your agent desktops. |
| Step 3 | Perform the following steps: On the taskbar, click Start , point to Administrative Tools , and then click Server Manager . In the Server Manager hierarchy pane, expand Roles , and then click Web Server (IIS) . In the Web Server (IIS) pane, scroll to the Role Services section, and then click Add Role Services . On the Select Role Services page of the Add Role Services wizard, expand FTP Server . Select FTP Service Note To support ASP.NET membership or IIS Manager authentication for the FTP service, you need to select FTP Extensibility . Click Next . On the Confirm Installation Selections page, click Install. On the Results page, click Close. In the sites section, click Add FTP Site . Provide a site name and path to the same location as the http directory c:\inetpub\wwwroot. Select your desired binding method, and specify to start immediately. On the FTP SSL Settings, select Allow SSL Connections . On the Authentication and Authorization section select the type of authentication required. If using basic, note the name and password of the account. Select the authorization; for anonymous select Anonymous users . Set the read and write permissions. Note Make note of your FTP connection information -- connection type, user name, password, and port number. | Note | To support ASP.NET membership or IIS Manager authentication for the FTP service, you need to select FTP Extensibility . | Note | Make note of your FTP connection information -- connection type, user name, password, and port number. |
| Note | To support ASP.NET membership or IIS Manager authentication for the FTP service, you need to select FTP Extensibility . |
| Note | Make note of your FTP connection information -- connection type, user name, password, and port number. |
| Step 4 | Make sure that the FTP and the IIS share the same root directory. The recording application writes the file to the media server directory structure, and the greeting playback call uses IIS
                                          to fetch the file. The en-us/app directory should be under the same root directory for FTP and IIS. |
| Step 5 | Create a dedicated directory on the server to store your greeting files. This lets you specify a lower cache timeout of 5 minutes for your agent greeting files that does not affect other more static
                                          files you may be serving from other directories. By default, the Record Greeting application posts the .wav file to the en-us/app directory under your web/ftp root directory. You may create a dedicated directory such as ag_gr under the en-us/app directory, and then indicate this in the Unified CCE script that invokes the recording application. Use the array for the
                                          expanded call variable call.user.microapp.ToExtVXML to send the ftpPath parameter to the recording application. Make sure the expanded call variable length is long enough, or
                                          it may get truncated and fail. |
| Step 6 | To allow re-recorded greetings to replace their predecessor in a reasonable amount of time while minimizing requests for data
                                       to the media server from Cisco VVB , configure a cache expiration value in IIS Manager. The ideal value varies depending on the number of agents you support and how often they re-record their greetings. Two minutes
                                          may be a reasonable starting point. To configure a cache expiration value in IIS Manager: Find the site you are using, go to the agent greeting folder you created (ag_gr), and then select HTTP Response Headers . Click Set Common Headers on Actions panel. Select Expire Web Content and set the desired value. |

| Note | Use Microsoft IIS with Unified CVP. This component is automatically installed as part of the CVP server package installation. |
|---|---|

| Note | To support ASP.NET membership or IIS Manager authentication for the FTP service, you need to select FTP Extensibility . |
|---|---|

| Note | Make note of your FTP connection information -- connection type, user name, password, and port number. |
|---|---|

| Step 1 | Use these settings in the Set Variable node to specify your locale directory: Object Type: Call. Variable: Must use the user.microapp.locale expanded call variable. Value: Specify the directory name. For example: "pt-br" (Portuguese-Brazil). You must enclose the path in quotes. |
|---|---|
| Step 2 | Use these settings in the Set Variable node to specify your application directory: Object Type: Call. Variable: Must use the user.microapp.app_media_lib expanded call variable. Value: Specify the directory name. For example: to use a directory "greet" in place of the default directory "app" , enter "greet" . To use a sub-directory "greet" under "app" enter "app/greet" . You must enclose the path in quotes. |

| To configure ECC variables. In Unified CCE Administration, navigate to Overview > Call Settings > Route Settings > Expanded Call Variables . If you include Set Variable nodes for the media server, locale, and/or application directories, make sure that the values
                                             you set for them do not exceed the Maximum Length settings for their corresponding expanded call variables. For example, if you include a Set Variable node for the media server with a value of "http://mysubdomain.mydomain.co.uk" , the string is 33 characters long. Therefore, the Maximum Length setting for the user.microapp.media_server expanded call
                                             variable must be 33 or greater. Otherwise, the server name is truncated in the HTTP request for the file and the file is not
                                             found. |
|---|