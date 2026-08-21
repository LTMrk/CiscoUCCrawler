---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-b83746e33f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_data-center-api_1501.html
retrieved_at: 2026-08-21T16:46:10.677977+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Data Center API

## Chapter: Data Center API

- Data Center API

- Data Center                              	 API

# Data Center API

## Data Center
                        	 API

### URL

### Operations

create :
                                    				Creates a new data center and stores it in the database.

delete :
                                    				Deletes one data center from the database. https://<server>/unifiedconfig/config/datacenter/{id}

This operation deletes all the data center configuration only if there are no agents, teams, dialed numbers, route patterns, or skill groups associated to the data center. Otherwise it returns an error.

This
                                          					 operation deletes the external machines configured to the remote data center.

get :
                                    				Returns one data center, using the URL https://<server>/unifiedconfig/config/datacenter/<id>

list :
                                    				Retrieves a list of data centers configured in the database.

You
                                             					 cannot change the data center name, and Side A and Side B PG addresses.

You can
                                             					 add new PG types but cannot remove the existing ones.

### Parameters

name:
                                    				Required. The unique name of the data center. Maximum length is ten characters.
                                    				Valid characters are alphanumeric, period (.), and underscore (_). The first
                                    				character must be alphanumeric.

agentPG:
                                    				Information about the agent PG for the remote data center, which includes the
                                    				following:

configured: Indicates whether an agent PG is configured for the
                                          					 remote data center. True or false. If the value is false, the rest of the
                                          					 values for the agent PG are ignored.

name: Name of the Call Manager subscriber sideA. Maximum length
                                                						  is ten characters. Valid characters are alphanumeric, period (.), and
                                                						  underscore (_). The first character must be alphanumeric.

refURL: Reference to Call Manager subscriber sideA.

cmSubSideB:

name: Name of the Call Manager subscriber sideB. Maximum length
                                                						  is ten characters. Valid characters are alphanumeric, period (.), and
                                                						  underscore (_). The first character must be alphanumeric.

refURL: Reference to Call Manager subscriber sideB.

finessePrimaryAddress: Address of Finesse primary.

finesseUserName: Username to access Finesse primary.

finessePassword: Password to access Finesse primary.

vruPG:
                                    				Information about the VRU PG for the remote data center, which includes the
                                    				following:

configured: Indicates whether a VRU PG is configured for the
                                          					 remote data center. True or false. If the value is false, the rest of the
                                          					 values for the VRU PG are ignored.

cvp1Address: Address of the CVP1 server.

cvp2Address: Address of the CVP2 server.

mrPG:
                                    				Information about the MR PG for the remote data center, which includes the
                                    				following:

configured: Indicates whether an MR PG is configured for the
                                          					 remote data center. True or false. If the value is false, the rest of the
                                          					 parameters for the MR PG are ignored.

### Search and
                              		  Sort Parameters

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

Search
                                          						Parameters

Sort
                                          						Parameters

name

name

### External
                              		  Machines

Remote data centers support the following types of external machines:

CVP Reporting Server

Gateways

Cisco Virtualized Voice Browser (CVVB)

Cisco Contact Center SIP Proxy ( CCCSP ) Server

Enterprise Chat and Email

SocialMiner

Third Party Multichannel

Agent: None

VRU: Unified
                                       				CVP Reporting

Multichannel: Third-party Multichannel, Enterprise Chat and Email, and SocialMiner

When you add an
                              		  external CVP reporting server to a remote data center, the CVP call server of
                              		  that data center associates to this reporting server.

When you delete
                              		  the external CVP reporting server, the call servers of the remote data center
                              		  re-associates to the core data center CVP reporting server.

### Example Get
                              		  Response

```
<datacenter>
    <name>Boston</name>
    <refURL>/unifiedconfig/config/datacenter/5001</refURL>
    <changeStamp>1</changeStamp>
    <sideAPGHostName>pg1a.boston.icm</sideAPGHostName> 
    <sideBPGHostName>pg1b.boston.icm</sideBPGHostName> 
 <agentPG>
        <configured>true</configured>
        <cmSubSideA>
               <refURL>/unifiedconfig/config/machineinventory/1234</refURL>
               <name>cmSubA.boston.icm</name>
        </cmSubSideA>
        <cmSubSideB>
               <refURL>/unifiedconfig/config/machineinventory/5678</refURL>
               <name>cmSubB.boston.icm</name>
        </cmSubSideB>
        <finessePrimaryHostName>finesseP.boston.icm</finessePrimaryHostName>
        <finesseUserName>boston</finesseUserName>
    </agentPG>
    <vruPG>
        <configured>true</configured>
        <cvp1HostName>cvp1.boston.icm</cvp1HostName>
        <cvp2HostName>cvp2.boston.icm</cvp2HostHame>
    </vruPG>
    <mrPG>
        <configured>true</configured>
    </mrPG>
</datacenter>
```

| Note | The term "data center" refers to site (remote site/main site) in PCCE deployment. |
|---|---|

| Search
                                          						Parameters | Sort
                                          						Parameters |
|---|---|
| name | name |