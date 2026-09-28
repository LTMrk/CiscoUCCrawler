---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-4283adcdd2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_machine-inventory-api_1501.html
retrieved_at: 2026-08-21T16:47:21.904660+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Machine Inventory API

## Chapter: Machine Inventory API

- Machine Inventory API

- Bulk Operation API

# Machine Inventory API

The term "CUSP" mentioned in the sections below refers to Cisco Contact Center SIP Proxy (CCCSP).

## Machine Inventory
                        	 API

This API returns the
                           		machines in the solution. Machines include VMs, VM Hosts, external machines,
                           		and gateways.

For information on
                           		how to perform a machine inventory scan, see Scan API .

### URL

### Operations

create :
                                    				Creates a machine by updating the database. See table below for restrictions
                                    				per machine type. Create is allowed for external machines types only.

delete :
                                    				Removes one machine.

You cannot delete the Virtualized Voice Browser (VVB), Cisco Contact Center SIP Proxy and Gateway external machines if they are associated with a SIP Server Group. To delete these external machines, you must
                                                      disassociate them from the SIP Server Group.

You cannot delete a Principal VVB.

get : Returns one machine and all associated addresses and services based on machine ID, using the URL https://<server>/unifiedconfig/config/machineinventory/<id> .

status: Returns any alerts indicating errors in the state of the inventory, using the URL https://<server>/unifiedconfig/config/machineinventory/status .

stats: Returns CVP Call Server and VXML Server statistics based on the machine type, using the URL https://<server>/unifiedconfig/config/machineinventory/<machine_id>/stats .

list :
                                    				Retrieves a list of all machines in the inventory. See table below for more
                                    				details.

update :
                                    				Updates one machine.

VM_HOST

1 Side A

1 Side B

CCE_ROGGER

(Applicable only for 2000 Agents and 4000 Agents)

No

1 Side A

1 Side B

CCE_ROUTER

(Applicable only for 12000 Agents)

No

1 Side A

1 Side B

CCE_LOGGER

(Applicable only for 12000 Agents)

No

1 Side A

1 Side B

CCE_PG

1 Side A

1 Side B

CCE_AW

Side A:
                                          						Update only

Side B:
                                          						No

1 Side A

1 Side B

CVP

1 Side A

1 Side B

CM

0 - Must
                                          						be changed after initial scan.

CM_PUBLISHER

1 Side
                                          						A, 0 Side B for on box CM Deployments

0 for
                                          						off box CM deployments

CM_SUBSCRIBER

1 Side
                                          						A, 1 Side B for on box CM Deployments

0 for
                                          						off box CM deployments

CVP_REPORTING

0 - 1
                                          						Side A

CUIC_PUBLISHER

Update
                                          						only

1 Side
                                          						A

CUIC_SUBSCRIBER

1 Side
                                          						B

FINESSE

Side
                                          						A: Update only

Side
                                          						B: No

1 Side
                                          						A

1 Side
                                          						B

0 - 1
                                          						Side B

ECE

No

EXTERNAL_CVVB

(Cisco Virtualized Voice Browser / Media Gateway)

All

Supports 0 to unlimited number of external CVVB or Media Gateway machines for the main site.

EXTERNAL_GATEWAY

All

Supports 0 to unlimited number of  external Gateways for the main site.

EXTERNAL_THIRD_PARTY_GATEWAY

Create and Delete only

Supports 0 to unlimited number of Gateways.

EXTERNAL_CUSP

(Cisco Contact Center SIP Proxy)

All

Supports 0 to unlimited number of external Cisco Contact Center SIP Proxy Servers for the main site.

EXTERNAL_SOCIAL_MINER )

All

0 - 1

EXTERNAL_CM_PUBLISHER

All

0 -
                                          						10 for on box CM deployments

1 -
                                          						11 for off box CM deployments

EXTERNAL_CM_SUBSCRIBER

No

External subscribers cannot be created, updated, or deleted as
                                          						this automatically occurs when the external publisher is created, updated, or
                                          						deleted.

EXTERNAL_CVP_REPORTING

0 - 1

EXTERNAL_HDS

0 - 2

EXTERNAL_MEDIA_SENSE

0 - 1

EXTERNAL_ECE

0 - 1

EXTERNAL_THIRD_PARTY _MULTICHANNEL

0 - 1

EXTERNAL_MEDIA_SERVER

All

No limit

DATA_CENTER

No
                                          						create, update, or delete

0 - 10

DC_CCE_PG

No
                                          						create, update, or delete

0 - 20

DC_CVP

No
                                          						create, update, or delete

0 - 20

DC_FINESSE_PRIMARY

Update
                                          						only

0 - 10

DC_FINESSE_SECONDARY

No
                                          						create, update, or delete

0 - 10

DC_EXTERNAL_CUSP

All

Supports 0 to unlimited number of Cisco Contact Center SIP Proxy Server for the remote site.

DC_EXTERNAL_GATEWAY

All

Supports 0 to unlimited number of Gateways for the remote site.

DC_EXTERNAL_THIRD_PARTY_GATEWAY

Create and Delete only

Supports 0 to unlimited number of Gateways.

DC_EXTERNAL_CVVB

All

Supports 0 to unlimited number of CVVB machines for the remote site.

DC_EXTERNAL_CVP_REPORTING

All

0 - 1

DC_EXTERNAL_MEDIA_SERVER

All

No limit

ECE_WEB_SERVER

Yes

No limit

DC_ECE_WEB_SERVER

Yes

No limit

CLOUD_CONNECTOR_PUB

All

0-1

CLOUD_CONNECTOR_SUB

No

0-1

### Parameters

Machine parameters:

refURL: The
                                    				refURL of the machine. See Shared Parameters .

name:
                                    				External name of the machine. For example, the VM host name. Valid characters
                                    				are period (.), hyphen (-), underscore (_), and alphanumeric. The first
                                    				character must be alphanumeric. Maximum length is 128 characters.

changeStamp:
                                    				See Shared Parameters .

type: The
                                    				type of machine.

versionInfo:
                                    				Version info available depending on product type. Includes the following
                                    				parameters (by product type):

UCCE: version, buildNumber, esNumber, patchVersion

CVVB: version and buildNumber

CVP: version, buildNumber, buildDate, esNumber, srNumber, dropNumber

VOS: version and buildNumber

Gateway: version

vmhost: A
                                    				reference to a machine of type VM_HOST, including refURL and name. See References .

autogenerated: Indicates if the information was generated
                                    				automatically.

hostName:
                                    				The host name of the machine.

If you
                                          					 provide a hostname, a lookup is performed to find the FQDN for that host. If
                                          					 the FQDN is found, the hostName field is then set to that FQDN value and the
                                          					 Machine Address is set to the IP address corresponding to the hostname.

If you
                                          					 do not provide a hostname, a lookup is performed using the address field in the
                                          					 API request. If the FQDN is found, the hostName field is set to that FQDN
                                          					 value.

networks: A
                                    				collection of network parameters. See the network parameters below.

vmInstanceUuid: A unique identifier for the virtual machine.

Network parameters:

type: Public
                                    				or private. Private networks are only specified for CCE_PG and CCE_ROGGER.

address: The
                                    				IP address. Must be valid hostname, IPV4, or IPV6 address.

services: A
                                    				collection of service parameters. See the services parameters below.

Services parameters:

uri: The service URL, for example, Diagnostic Portal URL or management console link.

port: The port for this service.

password: The password used to access the service. The password can be used when creating or updating, but is not returned.

enablePassword: Used for gateways.

description: The description of the service. See Shared Parameters .

pairing: Indicates if services on different machines are related. Related services have a matching value.

For the service type PRINCIPAL_AW , the pairing value is "true" for the AW that manages credentials for the features, and "false" for all other AWs.

For the service type PRINCIPAL_VVB , the pairing value is "true" for the VVB that manages configurations for the feature like Customer Virtual Assistant, and
                                    is "false" for all other VVBs.

For the service type FTP_CREDENTIAL , the following pairing values are supported:

True: Indicates FTP is enabled on the Media Server.

False: Indicates FTP is disabled on the Media Server.

username: The username used to access the service. Username maximum is 128 characters.

For the service type FTP_CREDENTIAL , the userName Anonymous indicates that anonymous access is enabled on the FTP Server.

For the machine types EXTERNAL_THIRD_PARTY_GATEWAY and DC_EXTERNAL_THIRD_PARTY_GATEWAY username and password are not required.

status: Used to indicate the status of the machine which are of type CVP_WSM, DIAGOSTIC_PORTAL, or CVVB.

type: The service type. Values for type are as follows:

ESXI: VM Host running ESXi server for connection to interrogate for VMs.

AXL: AXL connection information for Unified CM. Required for UCM Publisher.

DIAGNOSTIC_PORTAL: For CCE and Unified CVP, this is the Diagnostic Portal API. For Finesse and Unified Intelligence Center,
                                          this is the SOAP API. Required for CCE_AW on side A, CVP Reporting Server, CCCSP and FINESSE on side A, and CUIC Publisher.

CVP_WSM: Connection information for CVP Servers.

FTP_CREDENTIAL: Connection information for FTP service on the Media Server.

GATEWAY: Connection information for gateways.

CVVB: Provides connection information of the external CVVB machines.

MANAGEMENT_LINK: Provides a URL of the management console for the machine.

PRINCIPAL_VVB: Indicates the VVB that manages configurations for the feature like Customer Virtual Assistant.

TIP_PG: LiveData connection information for peripheral gateways.

TIP_ROUTER: LiveData connection information for the router.

ADMINISTRATION: Connection information for administrative access. Required for CVP OAMP.

SM_REST_API: SocialMiner REST API.

IDS: Indicates an Identity Server service. IDS contains the following parameters:

components: Information about the component, including the component refURL and component name.

IDS_PRIMARY_REF: When present, the <uri> parameter for this service refers to the primary Identity Server (IdS) to which this
                                          component is associated.

IDS_SECONDARY_REF: Read only. The <uri> parameter for this service refers to the backup IdS to which this component is associated.
                                          For a create or update request, this field is automatically filled with the refURL of the secondary IdS (if present).

MR_PG_CONNECTION: Connection information for the MR PG.

VRU_PG_CONNECTION: Connection information for the VRU PG.

UCM_PG_CONNECTION: Connection information for the UCM PG.

DATA_CENTER_REF: Read only. Contains information for the Data Center machine.

PRINCIPAL_AW: Indicates the AW that manages credentials for the features.

MACHINE_INFO: Refer the following table for machine information and its usage for different machine types:

Machine Type

Purpose of MACHINE_INFO

CVP

Message bus ID and Reporting server info

DC_CVP

Message bus ID and Reporting server info

EXTERNAL_CVVB

Mode VVB/MGW/VVB_MGW

DC_EXTERNAL_CVVB

Mode VVB/MGW/VVB_MGW

ECE_WEB_SERVER

Application instance

DC_ECE_WEB_SERVER

Application instance

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

name

description

hostName

name (default)

description

hostName

See Search and Sort .

Advanced search
                                 			 parameters

You can perform a machine type search or a service type search on the Machine Inventory API:

types: (machine_type1 | machine_type2 | machine_type3...) : Returns all the machines of the specified type. For example, types:(VM_HOST | EXTERNAL_SOCIAL_MINER | PUB_SUBSCRIBER) returns all the machines that belong to any of the specified machine types. The machine type is case-insensitive.

datacenters: (dc1|dc2|dc3...) : Returns machines which belong to any of the specified data center. The data center names are fully matched (case-insensitive,
                                    no partial matches). Searching for "core" returns all machines in the core data center.

serviceType:<service type> : Returns only machines associated with the specified service type. For example, serviceType:IDS_PRIMARY_REF returns only SSO-capable machines.

peripheralsets: (ps1|ps2|ps3...) : Returns machines which belong to any of the specified peripheral sets. The peripheral set names are fully matched (case-insensitive,
                                    no partial matches).

ipaddress: <IP address> : Returns machines that are configured with the specified IP address in the inventory. You can even specify a partial IP address
                                    to search. Search includes both public and private IP addresses.

### Example
                              		  Inventory Status Response

https://<server>/unifiedconfig/config/machineinventory/status

```
<status>
   <alerts>
      <alert>
         <apiErrors>
            <apiError>
               <errorData>CM_PUBLISHER</errorData>
               <errorMessage>CM_PUBLISHER not found on vmhost sideA</errorMessage>
               <errorType>inventory.MissingMachine</errorType>
            </apiError>
         </apiErrors>
         <machine>
            <host>sideA</host>
            <type>CM_PUBLISHER</type>
         </machine>      
      </alert>
   </alerts>
   <scanInfo>
      <lastScanDateTime>1374842924017</lastScanDateTime>
      <scanState>Idle</scanState>
   </scanInfo>
</status>
```

### Example Stats Response

https://<server>/unifiedconfig/config/machineinventory/<machine_id>/stats

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<statistics>
    <callServer>
        <icmStats>
         ....
        </icmStats>
        <infrastrutureStats>
         ....   
        </infrastrutureStats>
        <sipStats>
         ...   
        </sipStats>
    </callServer>
    <vxmlServer>
        <infraStructure>
         ...
        </infraStructure>
        <ivr>
         ...
        </ivr>
        <vxml>
         ...
        </vxml>
    </vxmlServer>
</statistics>
```

### Example Get
                              		  Response

https://<server>/unifiedconfig/config/machineinventory/<id>

```
<machine>
    <changeStamp>4</changeStamp>
    <refURL>/unifiedconfig/config/machineinventory/12073</refURL>
    <networks>
        <network>
            <address>10.10.10.21</address>
            <services>
                <service>
                    <autoGenerated>false</autoGenerated>
                    <port>7890</port> <status>OUT_OF_SYNC</status> <type>DIAGNOSTIC_PORTAL</type>
                    <userName>user@domain</userName>
                </service>
		 
            </services>
            <type>PUBLIC</type>
        </network>
    </networks>
    <autoGenerated>false</autoGenerated>
    <hostName>CCE-AW-1-21</hostName>
    <type>CCE_AW</type>
    <versionInfo>
        <buildNumber>03297</buildNumber>
        <version>11.0(1)</version>
    </versionInfo>
    <name>WJ2-AW-1</name>
    <vmHost>
        <refURL>/unifiedconfig/config/machineinventory/12071</refURL>
        <name>sideA</name>
    </vmHost>
    <vmInstanceUuid>50290e07-fa3d-2667-b84b-1c35989000e2</vmInstanceUuid>
</machine>
```

### Example
                              		  Updating SSO-Capable Components Associated to an IdS

SSO-capable
                              		  components can be associated to an IdS with the <components> element. For
                              		  example, a PUT request like this will update the IDS_PRIMARY_REF and
                              		  IDS_SECONDARY_REF of any SSO-capable components. Note that refURLs of any
                              		  on-box PCCE machines will be ignored as these cannot be changed. An example of
                              		  an off-box PCCE machine is the EXTERNAL_HDS machine.

This operation will also de-associate any existing component references to that IdS that aren’t in the list. For example,
                              if there were three components associated to this IdS before the operation, only two components would be associated after
                              the operation is complete.

```
<machine>
    <changeStamp>1</changeStamp>
    <refURL>/unifiedconfig/config/machineinventory/5000</refURL>
    <networks>
        <network>
            <type>PUBLIC</type>
            <address>10.10.10.22</address>
            <services>
                <service>
                    <type>IDS</type>
                    <components>
                        <component>
                            <refURL>/unifiedconfig/config/machineinventory/6000</refURL>
                        </component>
                        <component>
                            <refURL>/unifiedconfig/config/machineinventory/6001</refURL>
                        </component>
                    </components>
                </service>
            </services>
        </network>
    </networks>
</machine>
```

### Bulk Operation API

Use the Bulk Operation API to retrieve the current inventory file information, update the IP address or hostnames, rebuild Virtual Machines (VMs), perform
                              full synchronization, and complete the upgrade.

#### Operations

create : Update IP address or hostnames, rebuild (if chosen) VMs in the inventory, perform full synchronization, and complete the
                                       upgrade using the URL:

https://<server>:<serverport>/unifiedconfig/config/machineinventory/bulkoperation

get : Returns a list of machines in the CSV format based on the response parameters, using the URL:

https://<server>/unifiedconfig/config/machineinventory/bulkoperation/template? datacenter=<sitename>&category=<category>&<peripheralSet=<peripheralSet
                                          name>

#### Response Parameters for get

datacenter: The name of the datacenter. For example: Main . This field is case-sensitive. Use Main to refer to Main site in 4000 and 12000 Agent deployments and Core to refer to Main site in 2000 Agent deployments.

category: The machine category. Supported values are core , optional , or peripheral .

peripheralSet: The name of the peripheral set. This parameter is mandatory only for Packaged CCE 4000 or 12000 Agent deployments,
                                       if the category is PERIPHERAL .

To get the polling status of any task, go to GET

/unifiedconfig/config/machineinventory/bulkoperation/results?taskId=<task_id>

You can get the polling status only if create operation is performed asynchronously by including the query parameter async=true .

#### Payload for Create

Payload for Inventory Update:

name: The name of the inventory file. For example: main_updateinventory.csv .

operation: The type of operation. Supported value is:

UPDATE : updates the inventory with as per the content of the inventory file.

content: The content of the inventory file.

For more information on the Inventory file details, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

The properties for inventory update also include datacenter, category, and peripheralSet 1 . For more information, see Response Parameters for get .

Payload for Full Synchronization:

operation: The type of operation. Supported value is:

FULL_SYNC : triggers a solution synchronization after each EDMT run during Technology Refresh upgrade.

VALIDATE_UPGRADE_COMPLETION : validates the IP address, hostnames, and synchronization status of all machines in the inventory. Also validates the VM
                                                Hosts in 2000 Agent deployments.

UPGRADE_COMPLETION : completes Technology Refresh upgrade on the staged server.

#### Example Create Request for 4000 and 12000 Agent Deployments

```
<inventoryUpdateFile>
    <name>main_ps1_peripheral_inventory.csv</name>
    <operation>UPDATE</operation>
    <datacenter>Main</datacenter>
    <category>peripheral</category>
    <content>
	name,machineType,publicAddress,privateAddress,side,newPublicAddress,newPrivateAddress,connectionInfo,isReinstalled
	TR1-PG1A,CCE_PG,10.10.10.26,10.10.20.26,sideA,10.10.10.26,10.10.20.26,,Yes
	TR1-PG1B,CCE_PG,10.10.10.27,10.10.20.27,sideB,10.10.10.27,10.10.20.27,,Yes
    </content>
    <peripheralSetName>ps1</peripheralSetName>
</inventoryUpdateFile>
```

#### Example Create Response for 4000 and 12000 Agent Deployments

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<results>
    <state>SUCCEEDED</state>
    <statuses>
        <status>
            <state>SUCCEEDED</state>
            <name>LoggerUpdateTask_sideA</name>
        </status>
        <status>
            <state>SUCCEEDED</state>
            <name>LoggerUpdateTask_sideB</name>
        </status>
        <status>
            <state>SUCCEEDED</state>
            <name>RouterUpdateTask_sideA</name>
        </status>
        <status>
            <state>SUCCEEDED</state>
            <name>RouterUpdateTask_sideB</name>
        </status>
        <status>
            <state>SUCCEEDED</state>
            <name>AwUpdateTask</name>
        </status>
        <status>
            <state>SUCCEEDED</state>
            <name>InventoryDBUpdateTask</name>
        </status>
    </statuses>
</results>
```

| Note | The term "CUSP" mentioned in the sections below refers to Cisco Contact Center SIP Proxy (CCCSP). |
|---|---|

| Note | You cannot delete the Virtualized Voice Browser (VVB), Cisco Contact Center SIP Proxy and Gateway external machines if they are associated with a SIP Server Group. To delete these external machines, you must
                                                      disassociate them from the SIP Server Group. You cannot delete a Principal VVB. |
|---|---|

| Type | Create / Update / Delete operations allowed | Number allowed |
|---|---|---|
| VM_HOST | No | 1 Side A 1 Side B |
| CCE_ROGGER (Applicable only for 2000 Agents and 4000 Agents) | No | 1 Side A 1 Side B |
| CCE_ROUTER (Applicable only for 12000 Agents) | No | 1 Side A 1 Side B |
| CCE_LOGGER (Applicable only for 12000 Agents) | No | 1 Side A 1 Side B |
| CCE_PG | No | 1 Side A 1 Side B |
| CCE_AW | Side A:
                                          						Update only Side B:
                                          						No | 1 Side A 1 Side B |
| CVP | No | 1 Side A 1 Side B |
| CM | Update only | 0 - Must
                                          						be changed after initial scan. |
| CM_PUBLISHER | Update only | 1 Side
                                          						A, 0 Side B for on box CM Deployments 0 for
                                          						off box CM deployments |
| CM_SUBSCRIBER | Update only | 1 Side
                                          						A, 1 Side B for on box CM Deployments 0 for
                                          						off box CM deployments |
| CVP_REPORTING | No | 0 - 1
                                          						Side A |
| CUIC_PUBLISHER | Update
                                          						only | 1 Side
                                          						A |
| CUIC_SUBSCRIBER | No | 1 Side
                                          						B |
| FINESSE | Side
                                          						A: Update only Side
                                          						B: No | 1 Side
                                          						A 1 Side
                                          						B 0 - 1
                                          						Side B |
| ECE | No |  |
| EXTERNAL_CVVB (Cisco Virtualized Voice Browser / Media Gateway) | All | Supports 0 to unlimited number of external CVVB or Media Gateway machines for the main site. |
| EXTERNAL_GATEWAY | All | Supports 0 to unlimited number of  external Gateways for the main site. |
| EXTERNAL_THIRD_PARTY_GATEWAY | Create and Delete only | Supports 0 to unlimited number of Gateways. |
| EXTERNAL_CUSP (Cisco Contact Center SIP Proxy) | All | Supports 0 to unlimited number of external Cisco Contact Center SIP Proxy Servers for the main site. |
| EXTERNAL_SOCIAL_MINER ) | All | 0 - 1 |
| EXTERNAL_CM_PUBLISHER | All | 0 -
                                          						10 for on box CM deployments 1 -
                                          						11 for off box CM deployments |
| EXTERNAL_CM_SUBSCRIBER | No | External subscribers cannot be created, updated, or deleted as
                                          						this automatically occurs when the external publisher is created, updated, or
                                          						deleted. |
| EXTERNAL_CVP_REPORTING | All | 0 - 1 |
| EXTERNAL_HDS | Update only | 0 - 2 |
| EXTERNAL_MEDIA_SENSE | All | 0 - 1 |
| EXTERNAL_ECE | All | 0 - 1 |
| EXTERNAL_THIRD_PARTY _MULTICHANNEL | All | 0 - 1 |
| EXTERNAL_MEDIA_SERVER | All | No limit |
| DATA_CENTER | No
                                          						create, update, or delete | 0 - 10 |
| DC_CCE_PG | No
                                          						create, update, or delete | 0 - 20 |
| DC_CVP | No
                                          						create, update, or delete | 0 - 20 |
| DC_FINESSE_PRIMARY | Update
                                          						only | 0 - 10 |
| DC_FINESSE_SECONDARY | No
                                          						create, update, or delete | 0 - 10 |
| DC_EXTERNAL_CUSP | All | Supports 0 to unlimited number of Cisco Contact Center SIP Proxy Server for the remote site. |
| DC_EXTERNAL_GATEWAY | All | Supports 0 to unlimited number of Gateways for the remote site. |
| DC_EXTERNAL_THIRD_PARTY_GATEWAY | Create and Delete only | Supports 0 to unlimited number of Gateways. |
| DC_EXTERNAL_CVVB | All | Supports 0 to unlimited number of CVVB machines for the remote site. |
| DC_EXTERNAL_CVP_REPORTING | All | 0 - 1 |
| DC_EXTERNAL_MEDIA_SERVER | All | No limit |
| ECE_WEB_SERVER | Yes | No limit |
| DC_ECE_WEB_SERVER | Yes | No limit |
| CLOUD_CONNECTOR_PUB | All | 0-1 |
| CLOUD_CONNECTOR_SUB | No | 0-1 |

| Machine Type | Purpose of MACHINE_INFO |
|---|---|
| CVP | Message bus ID and Reporting server info |
| DC_CVP | Message bus ID and Reporting server info |
| EXTERNAL_CVVB | Mode VVB/MGW/VVB_MGW |
| DC_EXTERNAL_CVVB | Mode VVB/MGW/VVB_MGW |
| ECE_WEB_SERVER | Application instance |
| DC_ECE_WEB_SERVER | Application instance |

| Search parameters | Sort parameters |
|---|---|
| name description hostName | name (default) description hostName |

| Note | To get the polling status of any task, go to GET /unifiedconfig/config/machineinventory/bulkoperation/results?taskId=<task_id> You can get the polling status only if create operation is performed asynchronously by including the query parameter async=true . |
|---|---|

| Note | The properties for inventory update also include datacenter, category, and peripheralSet 1 . For more information, see Response Parameters for get . |
|---|---|