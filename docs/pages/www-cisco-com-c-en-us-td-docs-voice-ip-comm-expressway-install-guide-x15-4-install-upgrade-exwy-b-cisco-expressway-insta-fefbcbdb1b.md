---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-4-install-upgrade-exwy-b-cisco-expressway-insta-fefbcbdb1b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-4/install-upgrade/exwy_b_cisco-expressway-install-and-upgrade-guide-x154/exwy_m_nutanix-ahv.html
retrieved_at: 2026-08-16T22:07:07.778754+00:00
---

Cisco Expressway Install and Upgrade Guide (X15.4)

# Cisco Expressway Install and Upgrade Guide (X15.4)

Updated: April 3, 2026

Chapter: Nutanix AHV

## Chapter: Nutanix AHV

# Nutanix AHV

## VM Deployment using OVA

This section outlines procedures for deploying, managing, and monitoring Virtual Machines (VMs) in the Nutanix environment
                              using Open Virtualization Format (OVF) files.

Step 1

Log in to the Nutanix Prism Central or management portal to access the Infrastructure dashboard.

Step 2

Navigate to Compute > OVAs under the Infrastructure menu. Select the option to upload your OVA file, either by browsing local storage or providing a remote URL.

Step 3

Ensure you select the specific Nutanix-compatible image, typically identified by the XXXX_nutanix.ova .

Step 4

For local uploads, you can track progress in real time or delegate the process to a background task. URL-based uploads will
                                       trigger a " Successfully created OVA upload task " notification.

Step 5

Monitor the ingestion process status at any time by navigating to Activity > Tasks . Once complete, the image will appear as Active in the OVA s section.

Step 6

Select the uploaded OVA and navigate to Actions > Deploy as VM .

While the OVA includes preconfigured parameters, you must manually define the CPU allocation.

Nutanix implementations currently support only Medium and Large deployment profiles.

Step 7

Under the Network s section, click Edit to map the virtual interfaces to the appropriate subnets. You must assign a network to all three interfaces to satisfy deployment
                                       prerequisites.

Ensure the boot mode is set to Legacy BIOS .

In Management settings, set the system time zone to match your local time zone.

Review the configuration summary and select Create VM . You can track the provisioning status via the quick-view drawer in the top-right corner.

### What to do next

For Managing Virtual Machine, see Virtual Machine Lifecycle Management .

## VM Lifecycle Management

Step 1

Navigate to Compute > VMs to locate and verify the newly provisioned instance.

Step 2

Access the VM details page.

The remote console is unavailable until the instance is initialized.

Step 3

To start the machine, navigate to More > Power On .

Step 4

Once the VM is in a " Running " state, click the Console button to launch the interactive remote management interface .

Step 5

Use the More menu to execute specific power state changes:

Guest Reboot: Initiates a graceful restart signal to the Guest OS.

Reset: Performs a hard reset of the virtual hardware, then immediately powers on.

Power-Cycle: Executes an immediate cold boot of the VM.

Guest Shutdown: Sends an ACPI signal to gracefully terminate the OS.

### What to do next

For information on "Monitoring the Performance", see Performance Monitoring .

## Performance Monitoring

Select the Metrics tab within the VM view to access real-time performance data.

The system tracks 23 distinct telemetry points, providing deep visibility into CPU utilization, memory residency, IOPS, and
                           I/O read/write latency.

| Step 1 | Log in to the Nutanix Prism Central or management portal to access the Infrastructure dashboard. |
|---|---|
| Step 2 | Navigate to Compute > OVAs under the Infrastructure menu. Select the option to upload your OVA file, either by browsing local storage or providing a remote URL. |
| Step 3 | Ensure you select the specific Nutanix-compatible image, typically identified by the XXXX_nutanix.ova . |
| Step 4 | For local uploads, you can track progress in real time or delegate the process to a background task. URL-based uploads will
                                       trigger a " Successfully created OVA upload task " notification. |
| Step 5 | Monitor the ingestion process status at any time by navigating to Activity > Tasks . Once complete, the image will appear as Active in the OVA s section. |
| Step 6 | Select the uploaded OVA and navigate to Actions > Deploy as VM . While the OVA includes preconfigured parameters, you must manually define the CPU allocation. Note Nutanix implementations currently support only Medium and Large deployment profiles. | Note | Nutanix implementations currently support only Medium and Large deployment profiles. |
| Note | Nutanix implementations currently support only Medium and Large deployment profiles. |
| Step 7 | Under the Network s section, click Edit to map the virtual interfaces to the appropriate subnets. You must assign a network to all three interfaces to satisfy deployment
                                       prerequisites. Note Ensure the boot mode is set to Legacy BIOS . In Management settings, set the system time zone to match your local time zone. Review the configuration summary and select Create VM . You can track the provisioning status via the quick-view drawer in the top-right corner. | Note | Ensure the boot mode is set to Legacy BIOS . |
| Note | Ensure the boot mode is set to Legacy BIOS . |

| Note | Nutanix implementations currently support only Medium and Large deployment profiles. |
|---|---|

| Note | Ensure the boot mode is set to Legacy BIOS . |
|---|---|

| Step 1 | Navigate to Compute > VMs to locate and verify the newly provisioned instance. |
|---|---|
| Step 2 | Access the VM details page. Note The remote console is unavailable until the instance is initialized. | Note | The remote console is unavailable until the instance is initialized. |
| Note | The remote console is unavailable until the instance is initialized. |
| Step 3 | To start the machine, navigate to More > Power On . |
| Step 4 | Once the VM is in a " Running " state, click the Console button to launch the interactive remote management interface . |
| Step 5 | Use the More menu to execute specific power state changes: Guest Reboot: Initiates a graceful restart signal to the Guest OS. Reset: Performs a hard reset of the virtual hardware, then immediately powers on. Power-Cycle: Executes an immediate cold boot of the VM. Guest Shutdown: Sends an ACPI signal to gracefully terminate the OS. |

| Note | The remote console is unavailable until the instance is initialized. |
|---|---|