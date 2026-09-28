---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-0-virtual-machine-exwy-b-cisco-expressway-on-vi-d015d2f07b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-0/virtual-machine/exwy_b_cisco-expressway-on-virtual-machine-installation-guide-x150/exwy_m_deploying-multiple-datastores.html
retrieved_at: 2026-08-16T22:11:59.313784+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X15.0)

# Cisco Expressway on Virtual Machine Installation Guide (X15.0)

Updated: December 19, 2023

Chapter: Deploying Multiple Datastores

## Chapter: Deploying Multiple Datastores

- Deploying Multiple Datastores

- Deploying Multiple Datastores

# Deploying Multiple Datastores

## Deploying Multiple Datastores

Step 1

From vSphere or vCenter Inventory list select the relevant Host.

Step 2

Select the Configuration tab.

Step 3

Select Storage .

Step 4

Select Add Storage … (on the right hand side window).

Step 5

Select Disk/LUN and click Next .

Step 6

Under Disk/LUN select the required Disc/LUN from the list presented and click Next .

Step 7

On the File System Version page select VMFS-5 and then click Next .

Step 8

On the Current Disk Layout page verify the details and then click Next .

Step 9

On the Properties page enter a name for the new datastore and then click Next .

Step 10

On the Formatting page select Maximum available space and then click Next .

Step 11

On the Ready to Complete page verify the details and then click Finish .

Step 12

Wait for the Create VMFS Datastore task to complete.

Step 13

On completion, the new datastore will be listed under the Storage section.

| Step 1 | From vSphere or vCenter Inventory list select the relevant Host. |
|---|---|
| Step 2 | Select the Configuration tab. |
| Step 3 | Select Storage . Figure 1. Select Storage |
| Step 4 | Select Add Storage … (on the right hand side window). |
| Step 5 | Select Disk/LUN and click Next . Figure 2. Select Disk/LUN |
| Step 6 | Under Disk/LUN select the required Disc/LUN from the list presented and click Next . Figure 3. Required Disc/LUN |
| Step 7 | On the File System Version page select VMFS-5 and then click Next . Figure 4. Select VMFS-5 |
| Step 8 | On the Current Disk Layout page verify the details and then click Next . Figure 5. Verify Details |
| Step 9 | On the Properties page enter a name for the new datastore and then click Next . Figure 6. Name for New Datastore |
| Step 10 | On the Formatting page select Maximum available space and then click Next . Figure 7. Select Maximum Available Space |
| Step 11 | On the Ready to Complete page verify the details and then click Finish . Figure 8. Verify the Details |
| Step 12 | Wait for the Create VMFS Datastore task to complete. |
| Step 13 | On completion, the new datastore will be listed under the Storage section. Figure 9. New Datastore |