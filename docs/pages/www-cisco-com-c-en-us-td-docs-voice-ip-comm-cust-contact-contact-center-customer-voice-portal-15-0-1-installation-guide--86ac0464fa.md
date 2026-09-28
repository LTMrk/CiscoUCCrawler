---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-installation-guide--86ac0464fa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/installation/guide/ccvp_b_1501_installation-upgrade-guide-cisco-unified-customer-voice-portal/ccvp_b_install_and_upgrade_12-5_chapter_011.html
retrieved_at: 2026-08-21T03:01:10.652762+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: April 30, 2025

Chapter: Unified CVP
	 Postinstallation

## Chapter: Unified CVP
	 Postinstallation

# Unified CVP
                     	 Postinstallation

After you install Unified CVP, perform postinstallation tasks to ensure that the all the CVP components are installed successfully.
                           In addition, disable port blocking and address security issues. To beign with, do the following:

Go to the %CVP_HOME%\conf directory and add the following entry in the vxml.properties file:

VXML.usagefactor = 1.0

Restart the WebServicesManager service.

Sometimes after installation, clean.cvp file may not be available at %CVP_HOME%\bin\TAC . This can happen sporadically but does not impact the functionality of CVP. You can always retrieve this file from the CVP\Utilities folder of the CVP iso.

After installation, go to C:\Cisco\CVP\conf\orm.properties file and check if the orm.oamp.id parameter has any oamp ID (for example, 495a891e-a64f-4e1b-b80d-26e0dce0e249-2098391835) assigned to it. If so, then delete
                                             the ID and restart the WebServicesManager service.

Postinstallation excludes CVP components configuration. For information about CVP component configuration, see the Configuration Guide for Cisco Unified Customer Voice Portal available at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

If CVP Server, Operation Console, and Reporting Server have not been installed to the default C:\Cisco\CVP path, then update the following files under <install_path>/conf :

cvpconfigdb.properties: Update the connection URI so that it matches path of the DB directory ConnectionUrl=jdbc:derby://localhost:1529/<install_path>/OPSConsoleServer/sql/db

Example: ConnectionUrl=jdbc:derby://localhost:1529/C:/Cisco/CVP/OPSConsoleServer/sql/db

cvpwsm.properties: Update CVP_HOME.default.dir as CVP_HOME.default.dir = <install_path>

Example: CVP_HOME.default.dir = C:\\Cisco\\CVP

sip.properties: Update SIP.Secure.KeyStorePath as SIP.Secure.KeyStorePath= <install_path>\\security\\.keystore

Example: SIP.Secure.KeyStorePath= C:\\Cisco\\CVP\\conf\\security\\.keystore

This chapter
                           		  explains the following postinstallation tasks.

## Disable Port
                        	 Blocking

Exclude the following folders from on-access scanning configuration of the AV program for all Antivirus scans:

c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA , and D:\IFMXDATA .

It is the customer's responsibility to deploy the VXML applications after the Antivirus scans. This also applies to the custom java/jar/class files deployed in the shared path.

For more information on the Virus Scan guidelines, refer to the following sections of the UCCE documentation:

The Virus Protection section of UCCE Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

The General Antivirus Guidelines section of the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

## Security

Depending on your choice of Unified CVP deployment, you may need to address certain security considerations. For information
                           about security, see the Configuration Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

If you are concerned about any vulnerability in Microsoft Visual VC++ 2005 Redistributable, then uninstall it from Control
                                       Panel. This will not impact the normal operation of the CVP Reporting Sever.

## Initiate Metadata Synchronization for Unified CVP Rest API

In the CVP REST API architecture, customers use the REST API to create, update, and delete media files on the media server
                              and VXML applications on the VXML server. When this process is used, media files on the media server and VXML applications
                              on the VXML server are saved as metadata in the OpsConsole server’s Derby database. There may be situations where the metadata
                              becomes out of sync with the files on the media servers and VXML servers. Typical examples include the addition or deletion
                              of CVP servers, and the deployment of applications and media files using tools other than the REST API.

A command line tool “metasynch.cmd” is available in the C:\Cisco\CVP\wsm\CLI location on the OpsConsole server to enable synchronization of metadata with the files on VXML servers and media servers.
                              The tool internally uses the Sync Up API to perform synchronization. It takes three arguments: WSM username, WSM user password,
                              and server type (MEDIA, VXML, or VXML_STANDALONE). Based on the server type specified, all servers of the respective server
                              type are synchronized with the OpsConsole server as metadata. If the server type argument is not provided, metadata is synchronized
                              from all media servers and VXML servers configured in the OpsConsole server. In case of an upgrade from an earlier version,
                              the media files and VXML applications are present on the media servers and VXML servers, but the corresponding metadata information
                              is not present on the WSM server. The absence of metadata limits the user from using the REST API to access, update, or delete
                              existing media files and VXML applications on the media server and VXML server.

In case of Upgrade from an earlier version, the media files and vxml applications are present in the media servers and vxml
                              servers but corresponding metadata information is not present in the WSM server. The absence of metadata information limits
                              the user from using the REST API to access, update, and delete existing media files and vxml applications on the media server
                              and the vxml server.

Wsmadmin (CLI) users or any other serviceability/readonly role users cannot login or use OAMP/NOAMP/CLI until an Administrator
                                          or Super Administrator role user updates their password post an install/upgrade.

### Synchronize
                           	 Metadata Files Using Sync-Up Tool

To invoke metasynch.cmd , complete the following steps.

Step 1

On the Unified CVP OAMP Server, navigate to the C:\Cisco\CVP\wsm\ CLI location.

Step 2

Run the metasynch.cmd file with following arguments:

- wsm
                                                				  username

- wsm
                                                				  password

#### Example:

```
metasynch.cmd wsmusername wsmpassword MEDIA
```

servertype : MEDIA/VXML /VXML_STANDALONE

options : -help -? print this help message

C:\Cisco\CVP\wsm\CLI\log\SyncTool.log

| Note | Sometimes after installation, clean.cvp file may not be available at %CVP_HOME%\bin\TAC . This can happen sporadically but does not impact the functionality of CVP. You can always retrieve this file from the CVP\Utilities folder of the CVP iso. |
|---|---|

| Note | After installation, go to C:\Cisco\CVP\conf\orm.properties file and check if the orm.oamp.id parameter has any oamp ID (for example, 495a891e-a64f-4e1b-b80d-26e0dce0e249-2098391835) assigned to it. If so, then delete
                                             the ID and restart the WebServicesManager service. Postinstallation excludes CVP components configuration. For information about CVP component configuration, see the Configuration Guide for Cisco Unified Customer Voice Portal available at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html . If CVP Server, Operation Console, and Reporting Server have not been installed to the default C:\Cisco\CVP path, then update the following files under <install_path>/conf : cvpconfigdb.properties: Update the connection URI so that it matches path of the DB directory ConnectionUrl=jdbc:derby://localhost:1529/<install_path>/OPSConsoleServer/sql/db Example: ConnectionUrl=jdbc:derby://localhost:1529/C:/Cisco/CVP/OPSConsoleServer/sql/db cvpwsm.properties: Update CVP_HOME.default.dir as CVP_HOME.default.dir = <install_path> Example: CVP_HOME.default.dir = C:\\Cisco\\CVP sip.properties: Update SIP.Secure.KeyStorePath as SIP.Secure.KeyStorePath= <install_path>\\security\\.keystore Example: SIP.Secure.KeyStorePath= C:\\Cisco\\CVP\\conf\\security\\.keystore |
|---|---|

| Note | Exclude the following folders from on-access scanning configuration of the AV program for all Antivirus scans: c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA , and D:\IFMXDATA . It is the customer's responsibility to deploy the VXML applications after the Antivirus scans. This also applies to the custom java/jar/class files deployed in the shared path. For more information on the Virus Scan guidelines, refer to the following sections of the UCCE documentation: The Virus Protection section of UCCE Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . The General Antivirus Guidelines section of the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
|---|---|

| Note | If you are concerned about any vulnerability in Microsoft Visual VC++ 2005 Redistributable, then uninstall it from Control
                                       Panel. This will not impact the normal operation of the CVP Reporting Sever. |
|---|---|

| Note | Wsmadmin (CLI) users or any other serviceability/readonly role users cannot login or use OAMP/NOAMP/CLI until an Administrator
                                          or Super Administrator role user updates their password post an install/upgrade. |
|---|---|

| Step 1 | On the Unified CVP OAMP Server, navigate to the C:\Cisco\CVP\wsm\ CLI location. |
|---|---|
| Step 2 | Run the metasynch.cmd file with following arguments: wsm
                                                				  username wsm
                                                				  password Example: metasynch.cmd wsmusername wsmpassword MEDIA Usage : metasynch [options] username password [servertype] servertype : MEDIA/VXML /VXML_STANDALONE options : -help -? print this help message Note The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                      and all media files on Media servers. Logs for synch command tool can be found at the following location: C:\Cisco\CVP\wsm\CLI\log\SyncTool.log | Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                      and all media files on Media servers. Logs for synch command tool can be found at the following location: |
| Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                      and all media files on Media servers. Logs for synch command tool can be found at the following location: |

| Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                      and all media files on Media servers. Logs for synch command tool can be found at the following location: |
|---|---|