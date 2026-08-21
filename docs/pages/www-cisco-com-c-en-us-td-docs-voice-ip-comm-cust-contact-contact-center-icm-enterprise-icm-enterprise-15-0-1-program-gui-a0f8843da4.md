---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-a0f8843da4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce-m_dialed-number-api_1501.html
retrieved_at: 2026-08-21T16:46:27.589662+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Dialed Number API

## Chapter: Dialed Number API

- Dialed Number API

- Dialed Number API for Avaya PG

- Dialed Number                              	 API

# Dialed Number API

## Dialed Number API for Avaya PG

Use the Dialed Number API to list the dialed numbers currently defined in the database, define new dialed numbers, view,
                           and edit existing dialed numbers for Avaya PG.

### URL

### Operations

create : Creates one dialed number.

get : Returns all Avaya dialed numbers using the URL https://<server>/unifiedconfig/config/dialednumber/avayadialednumber .

update : Updates one dialed number.

### Parameters

description: See Shared Parameters .

dialedNumberString: Required. Value used to route the call or direct the non-voice task. A unique string for the routing type.
                                    Maximum of 25 characters. The External Voice and Post Call Survey routing types cannot have the same dialed number string.

changeStamp: See Shared Parameters .

mediaRoutingDomain: A reference to the media routing domain ( Media Routing Domain API ) for the dialed number. See References .

callType: A reference to a call type for this dialed number, including a refURL and name. See References .

dialedNumberRecords: A collection of dialed number record entries each containing the id and name of a dialed number database
                                    record. Read-only.

peripheral: A unique identifier for the peripheral.

label: Name of the default label for the dialed number. The default label for the dialed number is used when the system software
                                    fails to determine a target for the call within the routing client's time-out threshold.

pcsEnabledDialedNumberPattern: Optional. Dialed Numbers (DN) or DN patterns to associate with the Post Call Survey number.
                                    The maximum character length is 512 that can contain comma separated list without any spaces. Applicable only when the Routing
                                    Type is 7 (Post Call Survey -Unified CVP). If the Routing Type is not 7, the system returns an error message.

ringtoneName: Optional. A file name that has the customized ringtone. The file name can have a maximum length of 256 characters.
                                    Internationalized characters are allowed. Applicable only when the Routing Type is 1 (External Voice - Unified CVP). If the
                                    Routing Type is not 1, the system returns an error message.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

dialedNumberString

description

dialedNumberString (default)

description

pcsEnabledDialedNumberPattern

See Search and Sort .

Advanced search parameters

The Dialed Number API also supports advanced search parameters, such as peripheral.

Following are the REST responses received when the REST API runs to configure the dialed number:

Success - Configuration changes persist in AW DB and synchronized with respective devices.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with one or more devices.

Code: 201

Response: Configuration update failed for one or more devices. (This occurs when the AW DB is updated but Sync with CVP failed.)

Code: 503

Response: The server is currently busy. Please try again later. (This occurs when data synchronization to a device is in progress.)

```
<apiErrors>
<apiError>
<errorMessage>Configuration update failed for one or more devices.</errorMessage>
<errorType>PARTIAL_SUCCESS</errorType>
</apiError>
</apiErrors>
```

The partial success generally occurs for dialed number configured with Post Call Survey (PCS) and/or Ringtone.

Failure - The configuration updates to AW DB is failed.

### Example Get Response for Packaged CCE 4000 Agents and 12000 Agents Deployment

```
<dialedNumber>
  <description>test dialed number</description>
  <dialedNumberString>8885551212</dialedNumberString>
  <changeStamp>0</changeStamp>
  <mediaRoutingDomain>
    <refURL>[https://***.***.***.***/unifiedconfig/config/mediaroutingdomain/1]<refURL>
    <name>Cisco_Voice</name>
  </mediaRoutingDomain>
  <callType>
    <refURL>[https://***.***.***.***/unifiedconfig/config/calltype/(id)]</refURL>
    <name>calltype name</name>
  </callType>
  <dialedNumberRecords>
    <dialedNumberRecord>
      <id>10</id>
      <name>cvp1rc.8885551212</name>
    </dialedNumberRecord>
    <dialedNumberRecord>
      <id>11</id>
      <name>cvp2rc.8885551212</name>
    </dialedNumberRecord>
  </dialedNumberRecords>
  <peripheral>
    <id>5000</id>
  </peripheral>
  <defaultLabel>11223344</defaultLabel>
 </dialedNumber>
```

## Dialed Number
                        	 API

Dialed numbers are
                           		string values used to select the appropriate routing script so that a voice
                           		call or a non-voice task (such as an email or a request for a web chat) can be
                           		delivered to an agent.

Use the Dialed
                           		Number API to list the dialed numbers currently defined in the database, define
                           		new dialed numbers, and view, edit, and delete existing dialed numbers.

### URL

### Operations

create :
                                    				Creates one dialed number.

delete :
                                    				Marks one dialed number for deletion.

get :
                                    				Returns one dialed number, using the URL https://<server>/unifiedconfig/config/dialednumber/<id> .

list :
                                    				Retrieves a list of dialed numbers.

Query
                                             						parameters:

Summary list: See list .

update :
                                    				Updates one dialed number.

### Parameters

dialedNumberString: Required. Value used to route the call or direct the non-voice task. A unique string for the routing type.
                                    Maximum of 25 characters. The External Voice and Post Call Survey routing types cannot have the same dialed number string.

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

department: A
                                    				reference to the department ( Department API ),
                                    				including the refURL and name. See References .

routingType:
                                    				Specifies where a call or non-voice task request originates.

Refer to the Routing Type API to determine the routing types on which you can create a dialed number.

Forking Dialed Number. Calls come from Unified CVP. When selecting this routing type, a single dialed call is duplicated or
                                          "forked" to multiple destinations or media streams simultaneously.

External Voice. Calls come from Unified CVP. When creating a Dialed Number using this type, a dialed number database record
                                          is created for Unified CVP routing client.

Post Call Survey. Calls come from Unified CVP. When creating a Post Call Survey Dialed Number using this type, a dialed number
                                          database record is created for Unified CVP routing client.

Internal Voice. Calls come from a Unified CM phone.

Outbound. Calls that come from the Outbound Option Dialer.

Multichannel 1. Requests that come from an Enterprise Chat and
                                                						Email , SocialMiner , or third party.

Multichannel 2. Requests that come from an Enterprise Chat and
                                                						Email , SocialMiner , or third party.

Multichannel 3. Requests that come from an Enterprise Chat and
                                                						Email , SocialMiner , or third party.

callType: A reference to a call type for this dialed number, including a refURL and name. See References .

dialedNumberRecords: A collection of dialed number record
                                    				entries each containing the id and name of a dialed number database record.
                                    				Read-only.

mediaRoutingDomain: A reference to the media routing domain ( Media Routing Domain API ) for the dialed number. See References .

peripheralSet: A reference to a peripheral set for the dialed number.This parameter is mandatory for Packaged CCE 4000 Agents
                                    and 12000 Agents deployment type.

The peripheralSet parameter is not available for Packaged CCE 2000 Agents deployment type.

datacenter:
                                    				A reference to the data center, including the refURL and name.

This parameter is mandatory for Packaged CCE 4000 Agents or 12000 Agents deployment type. You must provide the reference to
                                    a data center that contains above peripheral set. For more information on data center for 4000 Agents or 12000 Agents deployment,
                                    see Inventory Import API .

pcsEnabledDialedNumberPattern: Optional. Dialed Numbers (DN) or DN patterns to associate with the Post Call Survey number.
                                    The maximum character length is 512 that can contain comma separated list without any spaces. Applicable only when the Routing
                                    Type is 7 (Post Call Survey -Unified CVP). If the Routing Type is not 7, the system returns an error message.

ringtoneName: Optional. A file name that has the customized ringtone. The file name can have a maximum length of 256 characters.
                                    Internationalized characters are allowed. Applicable only when the Routing Type is 1 (External Voice - Unified CVP). If the
                                    Routing Type is not 1, the system returns an error message.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

dialedNumberString

description

dialedNumberString (default)

description

datacenter.name

pcsEnabledDialedNumberPattern

peripheralSet.name (Available for Packaged CCE 4000 Agents and 12000 Agents deployment type.)

See Search and Sort .

Advanced
                                 			 search parameters

The Dialed
                              		  Number API also supports advanced search parameters, such as routing type
                              		  ( Routing Type API )
                              		  and data center ( Data Center API ).

routingType:<type> Finds all dialed numbers with the
                                    				specified routing type value. Valid types match those in the routingType
                                    				parameter.

routingType:1 Returns all dialed numbers with an external
                                          					 voice routing type.

datacenters:(dc1|dc2|dc3...) which returns all dialed
                                    				numbers which belong to any of the specified data centers. You can specify up
                                    				to three data centers. The data center names are fully matched
                                    				(case-insensitive, no partial matches). Searching for "core" returns all dialed
                                    				numbers in the core data center.

peripheralsets: (ps1|ps2|ps3...) returns the dialed numbers specific to the peripheral sets in 4000 Agents and 12000 Agents deployment. The peripheral set
                                    names are fully matched (case-insensitive, no partial matches).

### Example Get
                              		  Response

```
<dialedNumber> <department>
     <refURL>/unifiedconfig/config/department/5001</refURL>
     <name>Sales</name>
   </department> <refURL>/unifiedconfig/config/dialedNumber/(id)</refURL>
  <description>test dialed number</description>
  <dialedNumberString>8885551212</dialedNumberString>
  <routingType>1</routingType>
  <changeStamp>0</changeStamp>
  <mediaRoutingDomain>
    <refURL>/unifiedconfig/config/mediaroutingdomain/1<refURL>
    <name>Cisco_Voice</name>
  </mediaRoutingDomain> <datacenter>
    <name>Boxborough</name>
    <refURL>/unifiedconfig/config/datacenter/5000</refURL>
  </datacenter> <callType>
    <refURL>/unifiedconfig/config/calltype/(id)</refURL>
    <name>calltype name</name>
  </callType>
  <dialedNumberRecords>
    <dialedNumberRecord>
      <id>10</id> <name>C5011.8885551212</name> </dialedNumberRecord>
    <dialedNumberRecord>
      <id>11</id> <name>C5012.8885551212</name> </dialedNumberRecord>
   
  </dialedNumberRecords> <pcsEnabledDialedNumberPattern>1800*,1700*</pcsEnabledDialedNumberPattern> <ringtoneName>abc.wav</ringtoneName> <routingType>7</routingType> </dialedNumber>
```

Following are the REST responses received when the REST API runs to configure the dialed number:

Success - Configuration changes persist in AW DB and synchronized with respective devices.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with one or more devices.

Code: 201

Response: Configuration update failed for one or more devices. (This occurs when the AW DB is updated but Sync with CVP failed.)

Code: 503

Response: The server is currently busy. Please try again later. (This occurs when data synchronization to a device is in progress.)

```
<apiErrors>
<apiError>
<errorMessage>Configuration update failed for one or more devices.</errorMessage>
<errorType>PARTIAL_SUCCESS</errorType>
</apiError>
</apiErrors>
```

The partial success generally occurs for dialed number configured with Post Call Survey (PCS) and/or Ringtone.

Failure - The configuration updates to AW DB is failed.

### Example Get Response for Packaged CCE 4000 Agents and 12000 Agents Deployment

```
<dialedNumber> <department>
     <refURL>/unifiedconfig/config/department/5001</refURL>
     <name>Sales</name>
   </department> <refURL>[https://***.***.***.***/unifiedconfig/config/dialedNumber/(id)]</refURL>
  <description>test dialed number</description>
  <dialedNumberString>8885551212</dialedNumberString>
  <routingType>1</routingType>
  <changeStamp>0</changeStamp>
  <mediaRoutingDomain>
    <refURL>[https://***.***.***.***/unifiedconfig/config/mediaroutingdomain/1]<refURL>
    <name>Cisco_Voice</name>
  </mediaRoutingDomain>
  <peripheralSet>
    <refURL>/unifiedconfig/config/inventory/datacenter/(datacenter name)/peripheralset/(id)</refURL>
    <name>rack1</name>
  </peripheralSet>
  <callType>
    <refURL>[https://***.***.***.***/unifiedconfig/config/calltype/(id)]</refURL>
    <name>calltype name</name>
  </callType>
  <dialedNumberRecords>
    <dialedNumberRecord>
      <id>10</id>
      <name>cvp1rc.8885551212</name>
    </dialedNumberRecord>
    <dialedNumberRecord>
      <id>11</id>
      <name>cvp2rc.8885551212</name>
    </dialedNumberRecord>
  </dialedNumberRecords>
 </dialedNumber>
```

| Search parameters | Sort parameters |
|---|---|
| dialedNumberString description | dialedNumberString (default) description pcsEnabledDialedNumberPattern |

| Note | The partial success generally occurs for dialed number configured with Post Call Survey (PCS) and/or Ringtone. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| dialedNumberString description | dialedNumberString (default) description datacenter.name pcsEnabledDialedNumberPattern peripheralSet.name (Available for Packaged CCE 4000 Agents and 12000 Agents deployment type.) |

| Note | The partial success generally occurs for dialed number configured with Post Call Survey (PCS) and/or Ringtone. |
|---|---|