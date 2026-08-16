---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-4-install-upgrade-exwy-b-cisco-expressway-insta-f21119d833
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-4/install-upgrade/exwy_b_cisco-expressway-install-and-upgrade-guide-x154/exwy_m_cisco-nfvis-for-uc.html
retrieved_at: 2026-08-16T22:07:12.103425+00:00
---

Cisco Expressway Install and Upgrade Guide (X15.4)

# Cisco Expressway Install and Upgrade Guide (X15.4)

Updated: April 3, 2026

Chapter: Cisco NFVIS-for-UC

## Chapter: Cisco NFVIS-for-UC

# Cisco NFVIS-for-UC

## Deploying Virtual Machines

Upload ISO Image to Datastore : This section provides instructions for deploying, managing, and monitoring Virtual Machines (VMs) within the NFVIS management
                              portal.

NFVIS supports two registration methods:

Local Registration: Upload the XXXX_NFVIS.tar.gz file directly from your workstation.

Remote Registration: Import the file from a network location via HTTP, FTP, or SCP.

### Before you begin

Verify that the correct Product ID (PID), such as BE6k or BE7k, is displayed on the dashboard.

NFVIS requires the .tar.gz distribution package; standard Expressway .ova files are not supported.

Step 1

To upload an image using the local registration method, perform the following:

Navigate to Configuration > Virtual Machine > Images > Image Repository .

Select File

Click the Select File field and choose a file with a supported format (.iso, .ova, .tgz, .tar, .gz, .img, .vmdk, .qcow2, .raw, .docker). For example,
                                                s42700x15_4_0_NFVIS.tar.gz is selected.

Upload the File (if not already uploaded)

Click + Upload File to upload the selected file or Delete File to remove an existing one.

```
An " Image upload started " notification will appear.
```

Select Destination

From the Select Destination dropdown, choose the target datastore. For example, datastore1(internal)

Image Name

The Image Name automatically populates in the field. This is the default selection. For example, s42700x15_4_0_NFVIS.tar.gz

Select VM Workload Type

In the VM Workload Type dropdown field, Calling should appear by default.

Make sure you select the VM Workload Type as Calling if it does not.

Select VM Type

From the VM Type dropdown, choose the VM type: EXPRESSWAY .

Enable Dedicated Cores

Select the Dedicated Cores check box. For production environments, this is necessary to meet documented performance expectations.

To submit the registration, click the Upload File button.

Monitor the progress via the blue status indicator. Once complete, a green checkmark will appear.

The system will automatically detect the image type as Expressway and identify the version. The initial state will show as
                                             " Create " and transition to " Active " once the image is ready.

Step 2

To upload an image using the remote registration method, perform the following:

Navigate to Configuration > Virtual Machine > Images > Image Repository .

To select the Remote Registration, click Register Image and select Remote Image Registration option.

To configure the Image Details, enter a descriptive name in the Image Name field. For example, exwy-15.4 .

To configure the Remote Server Connection Protocol, enter the following details:

Protocol : Select from the drop-down list (HTTP/HTTPS/FTP/SCP).

IP Address: Enter the server hostname or IP address.

Image File Path: Enter the directory path to the ISO file with the image name.

Enter the Configure Authentication details for FTP/SCP (only).

Username: Enter the username for the remote server.

Password: Enter the password.

Select VM Type

From the VM Type dropdown, choose the VM type: EXPRESSWAY .

Enable Dedicated Cores

Select the Dedicated Cores check box. For production environments, this is necessary to meet documented performance expectations.

To submit the registration, click the Submit button.

NFVIS performs the following:

Download the ISO image from the remote server

Upload and parse the OVA file

Register the image

Automatically create profiles/flavors from OVA metadata

To verify registration, wait for the process to complete. The image should appear in the Image Repository with the status Active . Verify that flavors are populated from the OVA file.

Downloading large files may take several minutes.

Step 3

Deploy VM via NFVIS Portal

Navigate to Configuration > Deploy to deploy a new virtual machine. The interface will display a canvas showing existing VM connections.

Select an option from the VM. Select the Calling menu to view available applications and choose Expressway .

If your application type is not listed, select OTHER. If necessary, you can change the name of the VM Type created.

Choose the required image from the drop-down list. Images are populated based on the VM type selected.

Select the uploaded .tar.gz file and choose the appropriate deployment profile.

To configure Network Connections, perform the following in the Network Design section:

Locate the VM icon on the canvas.

Drag a line from the VM to the desired network.

Connect to the appropriate network(s) for your deployment. Enter the directory path to the ISO file.

Add additional networks as required.

Network Mapping: Use the interactive canvas to drag and connect the VM to your desired network segments.

Click Deploy to initiate the process. You can monitor the progress on the canvas or via the Notifications tab.

```
A confirmation message will appear upon successful deployment.
```

### What to do next

To know more about managing virtual machines, see Managing Virtual Machines .

## Managing Virtual Machines

Administrative tasks and power operations are handled through the management interface.

Accessing VM Details:

Navigate to Configuration > Virtual Machine > Manage . Click on a specific VM name to view interface configurations and software image details.

Network Configuration: Click the Edit button next to the VM name to modify network assignments based on your environmental requirements.

Console Access: Click the Cursor icon to launch the CLI console in a new browser tab.

Power Operations:

Reload: Located under Action Items , this performs an immediate Power-On or hard reset.

Switch Power: Use this to gracefully shut down or power on the VM.

Event Logging: Review the Logs section under Action Items to verify VM events, such as shutdown, reboot, or power-off sequences.

### What to do next

To learn more about monitoring virtual machines, see Monitoring Virtual Machines ..

## Monitoring Virtual Machines

NFVIS provides real-time performance metrics and resource allocation data to ensure system health.

Performance Metrics

Navigate to Monitoring > Virtual Machine and select a VM from the canvas to view the following telemetry:

CPU Utilization: Tracks performance for all vCPUs.

Memory Utilization: Monitors overall RAM consumption.

vNIC & Network Stats: Displays throughput (Rx/Tx) and packet drop rates.

Disk Utilization: Monitors data for virtual disks A and B.

Historical Data: All metrics can be filtered by duration: 5 minutes, 1 hour, 6 hours, 1 day, or 5 days.

Host Resource Allocation

To view the physical resource distribution, navigate to Monitoring > Host > Resource Allocation .

This page provides a high-level overview of:

CPU Allocation: Available vs. allocated CPU sockets.

Memory & Disk: Total virtual memory and physical hard disk availability.

| Note | NFVIS requires the .tar.gz distribution package; standard Expressway .ova files are not supported. |
|---|---|

| Step 1 | To upload an image using the local registration method, perform the following: Navigate to Configuration > Virtual Machine > Images > Image Repository . Select File Click the Select File field and choose a file with a supported format (.iso, .ova, .tgz, .tar, .gz, .img, .vmdk, .qcow2, .raw, .docker). For example,
                                                s42700x15_4_0_NFVIS.tar.gz is selected. Upload the File (if not already uploaded) Click + Upload File to upload the selected file or Delete File to remove an existing one. An " Image upload started " notification will appear. Select Destination From the Select Destination dropdown, choose the target datastore. For example, datastore1(internal) Image Name The Image Name automatically populates in the field. This is the default selection. For example, s42700x15_4_0_NFVIS.tar.gz Select VM Workload Type In the VM Workload Type dropdown field, Calling should appear by default. Note Make sure you select the VM Workload Type as Calling if it does not. Select VM Type From the VM Type dropdown, choose the VM type: EXPRESSWAY . Enable Dedicated Cores Select the Dedicated Cores check box. For production environments, this is necessary to meet documented performance expectations. To submit the registration, click the Upload File button. Monitor the progress via the blue status indicator. Once complete, a green checkmark will appear. The system will automatically detect the image type as Expressway and identify the version. The initial state will show as
                                             " Create " and transition to " Active " once the image is ready. | Note | Make sure you select the VM Workload Type as Calling if it does not. |
|---|---|---|---|
| Note | Make sure you select the VM Workload Type as Calling if it does not. |
| Step 2 | To upload an image using the remote registration method, perform the following: Navigate to Configuration > Virtual Machine > Images > Image Repository . To select the Remote Registration, click Register Image and select Remote Image Registration option. To configure the Image Details, enter a descriptive name in the Image Name field. For example, exwy-15.4 . To configure the Remote Server Connection Protocol, enter the following details: Protocol : Select from the drop-down list (HTTP/HTTPS/FTP/SCP). IP Address: Enter the server hostname or IP address. Image File Path: Enter the directory path to the ISO file with the image name. Enter the Configure Authentication details for FTP/SCP (only). Username: Enter the username for the remote server. Password: Enter the password. Select VM Type From the VM Type dropdown, choose the VM type: EXPRESSWAY . Enable Dedicated Cores Select the Dedicated Cores check box. For production environments, this is necessary to meet documented performance expectations. To submit the registration, click the Submit button. NFVIS performs the following: Download the ISO image from the remote server Upload and parse the OVA file Register the image Automatically create profiles/flavors from OVA metadata To verify registration, wait for the process to complete. The image should appear in the Image Repository with the status Active . Verify that flavors are populated from the OVA file. Note Downloading large files may take several minutes. | Note | Downloading large files may take several minutes. |
| Note | Downloading large files may take several minutes. |
| Step 3 | Deploy VM via NFVIS Portal Navigate to Configuration > Deploy to deploy a new virtual machine. The interface will display a canvas showing existing VM connections. Select an option from the VM. Select the Calling menu to view available applications and choose Expressway . Note If your application type is not listed, select OTHER. If necessary, you can change the name of the VM Type created. Choose the required image from the drop-down list. Images are populated based on the VM type selected. Select the uploaded .tar.gz file and choose the appropriate deployment profile. To configure Network Connections, perform the following in the Network Design section: Locate the VM icon on the canvas. Drag a line from the VM to the desired network. Connect to the appropriate network(s) for your deployment. Enter the directory path to the ISO file. Add additional networks as required. Note Network Mapping: Use the interactive canvas to drag and connect the VM to your desired network segments. Click Deploy to initiate the process. You can monitor the progress on the canvas or via the Notifications tab. A confirmation message will appear upon successful deployment. | Note | If your application type is not listed, select OTHER. If necessary, you can change the name of the VM Type created. | Note | Network Mapping: Use the interactive canvas to drag and connect the VM to your desired network segments. |
| Note | If your application type is not listed, select OTHER. If necessary, you can change the name of the VM Type created. |
| Note | Network Mapping: Use the interactive canvas to drag and connect the VM to your desired network segments. |

| Note | Make sure you select the VM Workload Type as Calling if it does not. |
|---|---|

| Note | Downloading large files may take several minutes. |
|---|---|

| Note | If your application type is not listed, select OTHER. If necessary, you can change the name of the VM Type created. |
|---|---|

| Note | Network Mapping: Use the interactive canvas to drag and connect the VM to your desired network segments. |
|---|---|

| Accessing VM Details: Navigate to Configuration > Virtual Machine > Manage . Click on a specific VM name to view interface configurations and software image details. Network Configuration: Click the Edit button next to the VM name to modify network assignments based on your environmental requirements. Console Access: Click the Cursor icon to launch the CLI console in a new browser tab. Power Operations: Reload: Located under Action Items , this performs an immediate Power-On or hard reset. Switch Power: Use this to gracefully shut down or power on the VM. Event Logging: Review the Logs section under Action Items to verify VM events, such as shutdown, reboot, or power-off sequences. |
|---|