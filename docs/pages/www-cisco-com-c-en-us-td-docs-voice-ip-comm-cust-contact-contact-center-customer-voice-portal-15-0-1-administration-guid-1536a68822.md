---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-administration-guid-1536a68822
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/administration/guide/ccvp_b_1501-admin-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1501_bulk-administration.html
retrieved_at: 2026-08-21T02:57:31.127385+00:00
---

Administration Guide for Cisco Unified Customer Voice Portal 15.0(1)

# Administration Guide for Cisco Unified Customer Voice Portal 15.0(1)

Updated: December 12, 2025

Chapter: Bulk Administration

## Chapter: Bulk Administration

# Bulk Administration

## Bulk Administration File Transfer (BAFT)

You can transfer multiple VXML application files and Script and Media files from the Operations Console to one or more devices
                              in a single operation.  Some types of files can only be transferred to certain types of devices.  Script and Media files can
                              be transferred to Gateways. VXML Application files can be transferred to Unified CVP VXML Servers.

See also:

### Transfer License Files Using BAFT

To transfer a license file:

Step 1

Select Bulk Administration > File Transfer > Licenses .

The File Transfer - Licenses window opens.

Step 2

In the Device Association panel, use the Select Device Type drop-down menu and select the type of device to which you want to transfer a license file.

Step 3

To select a device, perform the following steps:

Only devices of the selected type are displayed in the Available Devices box.

#### Example:

Select a device from the Available box.

Select the right arrow to move the device to the Selected box.

Step 4

To remove a device from the Selected Devices box, perform the following steps:

Select the device.

Select the left arrow to move the device to the Available Devices box.

You can check the Select all Unified CVP Devices check box to move all available devices to the selected devices column.

Step 5

In the License File portion of the screen, select the check box for the type of license you want to upload: a new license or a license from the
                                          managed files section.

- If you are selecting a new license then select Browse to select the license file from your local computer. (This license is added to managed files after the transfer finishes.)

Step 6

When you finish selecting devices and the license, click Transfer .

The file you selected is transferred to each selected device. Obtain the status of the transfer by selecting File Transfer
                                             Status. See View File Transfer Status .

### Transfer Scripts and Media Files Using BAFT

To transfer one or more script or media files:

Step 1

Select Bulk
                                                				  Administration > File
                                                				  Transfer > Scripts and Media .

The File Transfer - Scripts and Media window opens.

Step 2

In the Device Association panel, use the Select Device Type drop-down menu and select
                                          			 the type of device to which you want to transfer scripts and/or media files.

Step 3

Select a device from the Available box and click the right arrow to
                                          			 move the device to the Selected box.

Step 4

To remove a device from the Selected Devices box, select the device and
                                          			 click the left arrow to move the device to the Available box.

Step 5

In the Script and Media Files panel, select the radio
                                          			 button for the action you want to perform, then select or browse for the files
                                          			 you want to transfer.

There are three choices:

Default Gateway files - the default gateway files are
                                                   					 displayed in the list box. By default, all default files are selected. You can
                                                   					 select or deselect one or more files using CTRL-click. Highlighted files are
                                                   					 sent to the device(s) after you click transfer.

Managed files - Managed files are non-default files that have
                                                   					 already been transferred to a device from this Operations Console server. You
                                                   					 can select or deselect one or more files using CTRL-click. Highlighted files
                                                   					 are sent to the device(s) after you click transfer. You can optionally
                                                   					 highlight files and then click Delete Managed file to remove the file
                                                   					 from this Operations Console server and the managed files list.

Select new files - You can click browse to select a new file
                                                   					 to upload from your local computer. After you browse and select a file, another
                                                   					 slot is made available to browse and upload, up to a limit of 10 files. After
                                                   					 transfer, these files are displayed in the Managed Files section.

Step 6

When you finish selecting devices and files, select Transfer .

The selected file(s) is transferred to each selected device. You
                                             				can view the status of the transfer by clicking 
                                             				File Transfer Status. See View File Transfer Status .

### Transfer VXML Applications Using BAFT

To transfer one or more VXML applications:

Step 1

Select Bulk
                                                				  Administration > File Transfer > VXML
                                                				  Applications .

The File Transfer - VXML Application window opens.

Step 2

Select one or more
                                          			 Unified CVP VXML Servers and click the appropriate arrow to move them into the Selected panel.

The list of available Unified CVP VXML Servers to which you can
                                             			 transfer a VXML application is listed in 
                                             			 the Associated Unified CVP VXML
                                             				Server(s)Available panel.

Step 3

In the VXML Application Files panel, select the radio
                                          			 button for the action that you want to perform, then select or browse for the
                                          			 files that you want to transfer.

There are two choices:

Select new files - You can click browse to select a new VXML
                                                   					 application to upload from your local computer. After you browse and select a
                                                   					 VXML application, another slot is made available to browse and upload, up to a
                                                   					 limit of 10 VXML applications. After the transfer finishes, these files are displayed in
                                                   					 the Managed Files section.

Managed files - Managed files are files that have already been
                                                   					 transferred to a device from this Operations Console server. You can select or
                                                   					 deselect one or more files using CTRL-click. Highlighted files are sent to the
                                                   					 device(s) after you click Transfer . You can also highlight files and then
                                                   					 click Delete Managed file to remove the file
                                                   					 from this Operations Console server and the managed files list.

During the Enforcement state, uploading of VXML application from OAMP is blocked. Refer the NOAMP Help to understand the Enforcement
                                                               Rules.

Step 4

When you finish selecting devices, click Transfer .

The Operations Console server allows transfer of files upto 40 MB only. To transfer files greater than 40 MB, the files must
                                                         be directly placed on the server.

The selected file(s) is transferred to each selected device. You
                                             				can view the status of the transfer by clicking 
                                             				File Transfer Status. See View File Transfer Status .

### View File Transfer Status

To view the status of a bulk administration file transfer:

Step 1

Select Bulk Administration > File Transfer then Scripts and Media Files or VXML Application .

Step 2

Select the File Transfer Status button on the resulting
                                          			 page.

The status for the transfer is listed in the table.

Select Refresh to refresh the list of statuses.

| Step 1 | Select Bulk Administration > File Transfer > Licenses . The File Transfer - Licenses window opens. |
|---|---|
| Step 2 | In the Device Association panel, use the Select Device Type drop-down menu and select the type of device to which you want to transfer a license file. |
| Step 3 | To select a device, perform the following steps: Only devices of the selected type are displayed in the Available Devices box. Note Click the check box Select all Unified CVP devices to move all servers listed in Available to Selected . Example: For example, if you select Unified CVP Reporting Server , then only Unified CVP Reporting Servers are displayed in the Available box. Select a device from the Available box. Select the right arrow to move the device to the Selected box. | Note | Click the check box Select all Unified CVP devices to move all servers listed in Available to Selected . |
| Note | Click the check box Select all Unified CVP devices to move all servers listed in Available to Selected . |
| Step 4 | To remove a device from the Selected Devices box, perform the following steps: Select the device. Select the left arrow to move the device to the Available Devices box. You can check the Select all Unified CVP Devices check box to move all available devices to the selected devices column. |
| Step 5 | In the License File portion of the screen, select the check box for the type of license you want to upload: a new license or a license from the
                                          managed files section. If you are selecting a new license then select Browse to select the license file from your local computer. (This license is added to managed files after the transfer finishes.) |
| Step 6 | When you finish selecting devices and the license, click Transfer . The file you selected is transferred to each selected device. Obtain the status of the transfer by selecting File Transfer
                                             Status. See View File Transfer Status . |

| Note | Click the check box Select all Unified CVP devices to move all servers listed in Available to Selected . |
|---|---|

| Step 1 | Select Bulk
                                                				  Administration > File
                                                				  Transfer > Scripts and Media . The File Transfer - Scripts and Media window opens. |
|---|---|
| Step 2 | In the Device Association panel, use the Select Device Type drop-down menu and select
                                          			 the type of device to which you want to transfer scripts and/or media files. |
| Step 3 | Select a device from the Available box and click the right arrow to
                                          			 move the device to the Selected box. |
| Step 4 | To remove a device from the Selected Devices box, select the device and
                                          			 click the left arrow to move the device to the Available box. |
| Step 5 | In the Script and Media Files panel, select the radio
                                          			 button for the action you want to perform, then select or browse for the files
                                          			 you want to transfer. There are three choices: Default Gateway files - the default gateway files are
                                                   					 displayed in the list box. By default, all default files are selected. You can
                                                   					 select or deselect one or more files using CTRL-click. Highlighted files are
                                                   					 sent to the device(s) after you click transfer. Managed files - Managed files are non-default files that have
                                                   					 already been transferred to a device from this Operations Console server. You
                                                   					 can select or deselect one or more files using CTRL-click. Highlighted files
                                                   					 are sent to the device(s) after you click transfer. You can optionally
                                                   					 highlight files and then click Delete Managed file to remove the file
                                                   					 from this Operations Console server and the managed files list. Select new files - You can click browse to select a new file
                                                   					 to upload from your local computer. After you browse and select a file, another
                                                   					 slot is made available to browse and upload, up to a limit of 10 files. After
                                                   					 transfer, these files are displayed in the Managed Files section. |
| Step 6 | When you finish selecting devices and files, select Transfer . The selected file(s) is transferred to each selected device. You
                                             				can view the status of the transfer by clicking 
                                             				File Transfer Status. See View File Transfer Status . |

| Step 1 | Select Bulk
                                                				  Administration > File Transfer > VXML
                                                				  Applications . The File Transfer - VXML Application window opens. |
|---|---|
| Step 2 | Select one or more
                                          			 Unified CVP VXML Servers and click the appropriate arrow to move them into the Selected panel. The list of available Unified CVP VXML Servers to which you can
                                             			 transfer a VXML application is listed in 
                                             			 the Associated Unified CVP VXML
                                             				Server(s)Available panel. |
| Step 3 | In the VXML Application Files panel, select the radio
                                          			 button for the action that you want to perform, then select or browse for the
                                          			 files that you want to transfer. There are two choices: Select new files - You can click browse to select a new VXML
                                                   					 application to upload from your local computer. After you browse and select a
                                                   					 VXML application, another slot is made available to browse and upload, up to a
                                                   					 limit of 10 VXML applications. After the transfer finishes, these files are displayed in
                                                   					 the Managed Files section. Managed files - Managed files are files that have already been
                                                   					 transferred to a device from this Operations Console server. You can select or
                                                   					 deselect one or more files using CTRL-click. Highlighted files are sent to the
                                                   					 device(s) after you click Transfer . You can also highlight files and then
                                                   					 click Delete Managed file to remove the file
                                                   					 from this Operations Console server and the managed files list. Note During the Enforcement state, uploading of VXML application from OAMP is blocked. Refer the NOAMP Help to understand the Enforcement
                                                               Rules. | Note | During the Enforcement state, uploading of VXML application from OAMP is blocked. Refer the NOAMP Help to understand the Enforcement
                                                               Rules. |
| Note | During the Enforcement state, uploading of VXML application from OAMP is blocked. Refer the NOAMP Help to understand the Enforcement
                                                               Rules. |
| Step 4 | When you finish selecting devices, click Transfer . Note The Operations Console server allows transfer of files upto 40 MB only. To transfer files greater than 40 MB, the files must
                                                         be directly placed on the server. The selected file(s) is transferred to each selected device. You
                                             				can view the status of the transfer by clicking 
                                             				File Transfer Status. See View File Transfer Status . | Note | The Operations Console server allows transfer of files upto 40 MB only. To transfer files greater than 40 MB, the files must
                                                         be directly placed on the server. |
| Note | The Operations Console server allows transfer of files upto 40 MB only. To transfer files greater than 40 MB, the files must
                                                         be directly placed on the server. |

| Note | During the Enforcement state, uploading of VXML application from OAMP is blocked. Refer the NOAMP Help to understand the Enforcement
                                                               Rules. |
|---|---|

| Note | The Operations Console server allows transfer of files upto 40 MB only. To transfer files greater than 40 MB, the files must
                                                         be directly placed on the server. |
|---|---|

| Step 1 | Select Bulk Administration > File Transfer then Scripts and Media Files or VXML Application . |
|---|---|
| Step 2 | Select the File Transfer Status button on the resulting
                                          			 page. The status for the transfer is listed in the table. Select Refresh to refresh the list of statuses. |