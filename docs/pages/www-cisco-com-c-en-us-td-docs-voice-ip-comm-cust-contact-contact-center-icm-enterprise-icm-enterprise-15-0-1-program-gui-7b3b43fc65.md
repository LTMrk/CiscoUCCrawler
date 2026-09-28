---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-7b3b43fc65
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_inventory-import-api_1501.html
retrieved_at: 2026-08-21T16:47:04.825035+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Inventory Import API

## Chapter: Inventory Import API

- Inventory Import API

- Inventory Import API

# Inventory Import API

## Inventory Import API

The Inventory Import API allows to import inventory during fresh install, and after deployment initialization. This is for
                           Packaged CCE 4000 Agents and 12000 Agents deployment.

### Operations

create : Creates a new data center and peripheral set, and stores it in the database.

Main Data Center: https://<server>:<serverport>/unifiedconfig/config/inventory/datacenter

Remote Data Center: https://<server>:<serverport>/unifiedconfig/config/inventory/datacenter

Peripheral Set: https://<server>:<serverport>/unifiedconfig/config/inventory/datacenter/

<Main/datacenter_name>/peripheralset

To search for peripheral sets that belong to a specific type of PG in a Main or remote date center, use the below URL https://<server>:<serverport>/unifiedconfig/config/inventory/datacenter/

get : Returns the list of data centers and peripheral sets using the URL:

Data Center: https://<IP>/unifiedconfig/config/inventory/datacenter . The data centers contain the peripheral sets.

Peripheral Set: https://<IP>/unifiedconfig/config/inventory/peripheralset

delete : Deletes data center or machine or peripheral set from the database.

Remote Data Center: https://<server>:<serverport>/unifiedconfig/config/inventory/datacenter/

<datacenterid>?async=<true/false>

Machine: https://<server>:<serverport>/unifiedconfig/config/inventory/

datacenter/<dc_name>/machine/id where id = machineHostID

Peripheral Set: https://<IP>/unifiedconfig/config/inventory/peripheralset/id where id = peripheralSetID

### CSV File Structure

For more information, see the latest PCCE Administration and Configuration Guide available at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Parameters

name: The name of the data center.

Do not use system reserved terms like the core and main.

inventoryFile: This is the CSV file that contains records of machines used in a deployment.

content: The content of the CSV file.

To get the polling status of any task, go to GET /unifiedconfig/inventory/results?taskId=<task_id>

If the name field in the payload is set to Main (case-sensitive), then the operation is performed on the Main data center. If not, a new remote data center is created.

### Advanced Search Parameters

pgType: Returns all the peripheral sets that belong to the specified pgType: UCM, VRU or MR. You can specify only one pgType at a
                                    time.

### Example XML Request

```
<datacenter>
   <name>Main</name>
   <inventoryFile>
       <content>
            [filecontent]
       </content>
   </inventoryFile>
</datacenter>
```

```
<datacenter>
   <name>Site1</name>
        <name>
              site1.csv
        </name>
   <inventoryFile>
       <content>
            [filecontent]
       </content>
   </inventoryFile>
</datacenter>
```

```
<datacenter>
  <inventoryFile>
     <content>
       [filecontent]
     </content> 
  </inventoryFile>
</datacenter>
```

Machine

```
<inventoryFile>
  <name>
        machine.csv
  </name>  
     <content>
       [filecontent]
     </content> 
</inventoryFile>
```

| Note | To search for peripheral sets that belong to a specific type of PG in a Main or remote date center, use the below URL https://<server>:<serverport>/unifiedconfig/config/inventory/datacenter/ <Main/datacenter_name>/peripheralset?q=pgType:<UCM/VRU/MR> |
|---|---|

| Note | Do not use system reserved terms like the core and main. |
|---|---|

| Note | To get the polling status of any task, go to GET /unifiedconfig/inventory/results?taskId=<task_id> If the name field in the payload is set to Main (case-sensitive), then the operation is performed on the Main data center. If not, a new remote data center is created. |
|---|---|