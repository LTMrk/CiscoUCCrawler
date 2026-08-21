---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-exwy-b-cisco-expressway-on-virtual-machine-exwy-b-v-4ac94c6242
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/exwy_b_cisco-expressway-on-virtual-machine/exwy_b_vm-install-guide_appendix_01010.html
retrieved_at: 2026-08-21T18:08:08.871811+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X12.7)

# Cisco Expressway on Virtual Machine Installation Guide (X12.7)

Updated: April 8, 2020

Chapter: Deploying Multiple Datastores

## Chapter: Deploying Multiple Datastores

- Deploying Multiple Datastores

- Deploying Multiple Datastores

# Deploying Multiple Datastores

## Deploying Multiple Datastores

From vSphere or vCenter Inventory list select the relevant Host.

Select the Configuration tab.

Select Storage .

Select Add Storage … (on the right hand side window).

Select Disk/LUN and click Next .

Under Disk/LUN select the required Disc/LUN from the list presented and click Next .

On the File System Version page select VMFS-5 and then click Next .

On the Current Disk Layout page verify the details and then click Next .

On the Properties page enter a name for the new datastore and then click Next .

On the Formatting page select Maximum available space and then click Next .

On the Ready to Complete page verify the details and then click Finish .

Wait for the Create VMFS Datastore task to complete.

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