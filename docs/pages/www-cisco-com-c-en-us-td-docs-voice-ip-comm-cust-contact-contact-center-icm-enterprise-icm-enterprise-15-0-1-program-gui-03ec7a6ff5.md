---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-03ec7a6ff5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_routing-pattern-api_1501.html
retrieved_at: 2026-08-21T16:48:07.887254+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Routing Pattern API

## Chapter: Routing Pattern API

- Routing Pattern API

- Routing Pattern                              	 API

# Routing Pattern API

## Routing Pattern
                        	 API

The Routing Pattern API configures CVP routing pattern for the CVP server. The configured CVP routing pattern through API
                           enables application user interface to configure routing pattern and the associated settings.

### URL

### Operations

create :
                                    				Creates a routing pattern.

delete : Permanently deletes one routing pattern.

get :
                                    				Returns specific routing patterns from the database using the URL https://<server>:<serverport>/unifiedconfig/config/
                                       				  routingpattern/(id) .

list :
                                    				Returns a list of routing patterns.

update : Updates a routing pattern.

### Parameters

pattern: Required. Pattern for routing the call. The maximum length is 24 characters. It can contain alphanumeric characters,
                                    wildcard characters such as exclamation point (!) or asterisk (*), single digit matches such as the letter X or period (.).
                                    It can end with an optional greater than (>) wildcard character. This parameter cannot be updated.

patternType: Required. Type of pattern. The value is 1 for VRU,  2 for Agents, and 3 for External.

datacenter: A
                                    				reference to the data center, including the refURL and name. This parameter
                                    				cannot be updated.

description:
                                    				See Shared Parameters .

destination: Required. SIP Server Group/FQDN to which the pattern routes the call.

sendToOriginator: Optional. Enables send calls to originator. The values are true or false. The calls are sent back to the
                                    originating Ingress gateway. This feature is not supported on Virtualized Voice Browser (VVB).

rnaTimeout: Optional. Enables RNA Timeout for outbound calls. The value is an integer between 5 and 60.

configParam: Optional. Miscellaneous futuristic field for future.

changeStamp:
                                    				See Shared Parameters .

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

pattern

description

destination

pattern

datacenter.name

patternType

destination

description

See Search and Sort .

Advanced search parameters

The Routing Pattern API also supports advanced search parameters, such as patternType, datacenters, rnaTimeoutEnabled, and
                              sendToOriginator.

patternType: Finds all routing patterns that are associated to the specified pattern type - 1 for VRU, 2 for Agent, and 3 for External.

datacenters:(dc1|dc2|dc3): Returns all routing patterns which belong to any of the specified data centers. You can specify up to three data centers.
                                    The data center names are fully matched (case-insensitive, no partial matches). Searching for "core" returns all routing patterns
                                    in the core data center.

rnaTimeoutEnabled : Finds all routing patterns for which RNA timeout is either configured or not. The possible values of the search parameter
                                    are as follows:

true - To search all routing patterns for which RNA timeout is configured.

false - To search all routing patterns for which RNA timeout is not configured.

sendToOriginator : Finds all routing patterns for which Send to originator is either enabled or not. The possible values of the search parameter
                                    are as follows:

true - To search all routing patterns for which Send to originator is enabled.

false - To search all routing patterns for which Send to originator is not enabled.

### Example Create
                              		  Request

```
<routingPattern>
    <pattern>xyz</pattern>
    <patternType>1</patternType>
    <destination>berlin.icm</destination>
    <datacenter>
        <name>Berlin</name>
        <refURL>/unifiedconfig/config/datacenter/10370</refURL>
    </datacenter>
    <description>Test</description>
    <rnaTimeout>30</rnaTimeout>
    <sendToOriginator>true</sendToOriginator>
    <configParam>abc</configParam>
</routingPattern>
```

### Example Get
                              		  Response

```
<routingPattern>
    <refURL>unifiedconfig/config/routingPattern/(id)</refURL>
    <changeStamp>0</changeStamp>
    <pattern>xyz</pattern>
    <patternType>1</patternType>
    <destination>berlin.icm</destination>
    <datacenter>
        <name>Berlin</name>
        <refURL>/unifiedconfig/config/datacenter/10370</refURL>
    </datacenter>
    <description>Test</description>
    <rnaTimeout>30</rnaTimeout>
    <sendToOriginator>true</sendToOriginator>
    <configParam>abc</configParam>
</routingPattern>
```

| Search parameters | Sort parameters |
|---|---|
| pattern description destination | pattern datacenter.name patternType destination description |