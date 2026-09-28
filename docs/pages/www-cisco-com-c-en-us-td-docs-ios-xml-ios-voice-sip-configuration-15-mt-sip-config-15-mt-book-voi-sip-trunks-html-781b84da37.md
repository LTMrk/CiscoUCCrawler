---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-sip-configuration-15-mt-sip-config-15-mt-book-voi-sip-trunks-html-781b84da37
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/sip/configuration/15-mt/sip-config-15-mt-book/voi-sip-trunks.html
retrieved_at: 2026-08-20T23:45:17.857097+00:00
---

SIP Configuration Guide, Cisco IOS Release 15M&T

# SIP Configuration Guide, Cisco IOS Release 15M&T

Updated: November 25, 2014

Chapter: Support for Resource Availability Indication Over SIP Trunks

## Chapter: Support for Resource Availability Indication Over SIP Trunks

# Support for Resource Availability Indication Over SIP Trunks

The Support for Monitoring Utilization of Critical Resources on Gateway Router, Cisco UBE and Cisco UCME and Reporting Over
                        SIP Trunks feature implements monitoring of resource utilization and reporting functionality over the Session Initiation Protocol
                        (SIP) trunk on the Cisco IOS gateway, Cisco Unified Border Element (Cisco UBE) and Cisco Unified Communications Manager Express
                        (Cisco UCME). This feature supports monitoring of CPU, memory, Digital Signaling Processor (DSP) and the DS0 port on the Cisco
                        IOS gateway and reporting the status to external devices using SIP OPTION mechanism.

## Finding Feature Information

Your software release may not support all the features documented in this module. For the latest caveats and feature information,
                           see Bug Search Tool and the release notes for your platform and software release. To find information about the features documented in this module,
                           and to see a list of the releases in which each feature is supported, see the feature information table at the end of this
                           module.

Use Cisco Feature Navigator to find information about platform support and Cisco software image support. To access Cisco Feature
                           Navigator, go to www.cisco.com/go/cfn . An account on Cisco.com is not required.

## Restrictions for the Support
                        	 for Resource Availability Indication Over SIP Trunks Feature

The number of
                                 			 resource monitoring entities should be limited to a maximum of 50.

The target device
                                 			 configured on the Cisco IOS gateway and the OPTIONS message obtained from the
                                 			 external polling device must be the same to accept the resource status query.
                                 			 For example, if an IP address is configured as the target on the Cisco IOS
                                 			 gateway, it is expected that the OPTIONS message coming into the Cisco IOS
                                 			 gateway will have the same IP address. The same applies if a Fully Qualified
                                 			 Domain Name (FQDN) is configured against the target device.

## Information About the Support for Resource Availability Indication Over SIP Trunks Feature

### Overview of the Support for Resource Availablity Indication Over SIP Trunks

The Support for Resource Available Indication Over SIP Trunks feature enables monitoring of CPU, memory, DSP, and DS0 resources
                              on the Cisco IOS gateway and reporting of the status to external device using the gateway resources. The reporting from the
                              gateway takes place either based on a configured time interval or on the configured threshold crossover. The gateway also
                              supports extracting the gateway resource information from the external entity either on periodic or nonperiodic basis.

The monitoring and reporting of resources is achieved by SIP OPTIONS using x-cisco-rai headers. The highlights of monitoring and reporting of resources are as follows:

Resource groups are created by grouping the required resource monitoring entities together and providing each of the resource
                                    groups a unique index value.

The required monitoring and reporting parameters are applied on the resource groups for monitoring the selected resource entities.

In the periodic reporting, Resource Allocation Indication (RAI) information is reported based on a periodic-interval value
                                    configured through a CLI. The periodic reporting is disabled by default.

In the threshold-based reporting, RAI information is reported when one of the resources reaches an out-of-resource state.
                                    Threshold-based reporting is disabled by default.

Call treatment is not handled as part of this feature on the gateway. If call treatment needs to be performed along with reporting,
                                          then the call threshold feature needs to be configured appropriately with desired threshold values. The gateway supports CPU,
                                          memory, and maximum number of calls per interface.

### Benefits of the Support for Resource Availablity Indication Over SIP Trunks

Intelligent routing can be performed by Customer Voice Portal (CVP) if the Cisco IOS gateway passes information with the methodology
                                    provided by this feature.

Call handling is performed more efficiently in Voice over Internet Protocol (VOIP) networks where CVP uses the Cisco IOS gateway
                                    for both VoiceXML (VXML) application as well as time-division multiplexing (TDM) calls for Public Switched Telephone Network
                                    (PSTN) connectivity.

By monitoring and reporting the usage status of the gateway resources and generic resources to the external entity, you can
                                    take decisions based on the current load and status of various gateway resources.

Migration from H.323 to SIP is made easier.

### Overview on Monitoring and Reporting of Gateway Resources

The gateway uses the x-cisco-rai header in the OPTIONS message to report the resource utilization to the routing or monitoring entities.

#### ABNF Format for Reporting

The Augmented Backus-Naur Form (ABNF) format of reporting is used to report the status of the report utilization to the monitoring
                                 entity. The Cisco IOS gateway may not use all the fields. Provision is also made for adding new resource types and new parameters
                                 for the resources.

The following is the format of the header used for reporting:

```
x-cisco-rai = ("x-cisco-rai") HCOLON resource-param *(COMMA resource-param)
resource-param = resource-name-param SEMI resource-params *(SEMI resource-params)
resource-name-param = "SYSTEM" / "CPU" / "MEM" / "DS0" / "DSP" / token
resource-params =  resource-status-param/resource-total-param/resource-available-param/resource-used-param/resource-extension
resource-status-param = "almost-out-of-resource" EQUAL ("true" / "false")
resource-total-param="total" EQUAL 1*(DIGIT) ["%" / "MB" / token]
resource-available-param = "available" EQUAL 1*(DIGIT) ["%" / "MB" / token]
resource-used-param = "used" EQUAL 1*3DIGIT "%"
resource-extension=generic-param
```

#### Semantics of the Header

The rules for constructing the header are as follows:

SYSTEM is a mandatory parameter that should be the first resource for a given device. Other resource-name-param values are
                                       optional parameters.

The resource-identity-param parameter is a mandatory parameter within the SYSTEM resource-name-param parameter.

At least one resource parameter (resource-params) should be present. If the resource-available-param parameter is present,
                                       the resource-total-param parameter should also be present so that the resource-used-param parameter can be calculated.

For the SYSTEM resource-name-param parameter, the provision of a resource-status-param parameter is mandatory.

Following are the examples of the reporting format in the SIP OPTIONS message:

##### Example 1: Cisco IOS Gateway Sending Resource Header when the Resources are Available

```
x-cisco-rai : SYSTEM; almost-out-of-resource=false
x-cisco-rai : CPU; almost-out-of-resource=false;total=100%;available=60%
x-cisco-rai : MEM; almost-out-of-resource=false;total=100%;available=40%
x-cisco-rai : DSO; almost-out-of-resource=false;total=64;available=20
x-cisco-rai : DSP; almost-out-of-resource=false;total=64;available=20
```

##### Example 2: Cisco IOS Gateway Sending Resource Header when CPU Resources are Not Available

```
x-cisco-rai : SYSTEM; almost-out-of-resource=true
x-cisco-rai : CPU; almost-out-of-resource=true;total=100%;available=20%
x-cisco-rai : MEM; almost-out-of-resource=false;total=100%;available=40%
x-cisco-rai : DSO; almost-out-of-resource=false;total=64;available=20
x-cisco-rai : DSP; almost-out-of-resource=false;total=64;available=20
```

### Modes of Reporting

There are two modes of reporting:

#### Gateway Triggered Reporting to Routing Monitoring Entity

In gateway triggered reporting, the gateway sends the resource utilization information in an OPTION message to the external
                                 entity. The gateway includes a supported header with the option tag x-cisco-rai to indicate that this OPTION message carries the resource availability information. The trigger to send the OPTION message
                                 can be either periodic, or threshold based, or both.

##### Periodic Reporting

In the periodic reporting mode, reporting is triggered based on a preconfigured timer value. This type of reporting is used
                                    to collect information on a resource usage.

##### Threshold Triggered Reporting

In the threshold triggered reporting mode, reporting is triggered depending on the threshold levels configured for the resources
                                    that are being monitored. This mode of reporting is used to inform the external entity of the availability or nonavailability
                                    of the gateway to service further call requests from the external entity. Threshold triggered reporting is disabled by default.

#### Routing Monitoring Entity Triggered Reporting

In routing or monitor triggered reporting, the external entity can extract the resource information from the gateway using
                                 the SIP OPTIONS message. The gateway expects the x-cisco-rai tag in either the require: or supported: header fields for an incoming OPTIONS message. The presence of the x-cisco-rai tag in any one of the header fields informs the gateway that this option is to retrieve the gateway resource information.

### Reporting Mechanism over SIP Trunk

The monitoring and reporting of gateway resources to an external entity is achieved by SIP OPTIONS using x-cisco-rai headers. The sample OPTIONS message format is as provided below.

#### Inbound OPTIONS Message

The following is a sample format of the incoming OPTIONS message and the corresponding response from the Cisco IOS gateway
                                 for resource statistics request:

```
Received:OPTIONS sip:9.13.38.162:5060 SIP/2.0Via: SIP/2.0/UDP 9.13.40.83:5060;branch=z9hG4bK-21983-1-0From: <sip:9.13.40.83:5060>;tag=1To: sut <sip:service@9.13.38.162:5060>Call-ID: 1-21983@9.13.40.83CSeq: 1 OPTIONSContact: sip:sipp@9.13.40.83:5060Max-Forwards: 70Subject: Performance TestSupported: sec-agree, precondition
Require:  x-cisco-rai   Content-Type: application/sdpContent-Length: 0
```

#### Outbound OPTIONS Message

The following is a sample format of the OPTIONS message that is sent out from the Cisco IOS gateway to the external entity
                                 with resource statistics information in it:

```
Sent:OPTIONS sip:9.13.38.163:5060 SIP/2.0
Via: SIP/2.0/UDP 9.13.38.162:5060;branch=z9hG4bKE211D
From: <sip:9.13.38.162>;tag=1005B0-1CB
To: <sip:9.13.38.163>
Date: Wed, 16 Dec 2009 05:53:35 GMT
Call-ID: 2EE072F6-E93E11DE-801BBA85-BFCDE3D6@9.13.38.162
User-Agent: Cisco-SIPGateway/IOS-12.x
Max-Forwards: 70
CSeq: 101 OPTIONS
Contact: <sip:9.13.38.162:5060>
X-cisco-rai: SYSTEM ; almost-out-of-resource=true
X-cisco-rai: CPU ; almost-out-of-resource=false;available=99%;total=100%;used=1%
X-cisco-rai: DS0 ; almost-out-of-resource=false;available=23;total=23;used=0%
X-cisco-rai: DSP ; almost-out-of-resource=false;available=96;total=96;used=0%
X-cisco-rai: MEM ; almost-out-of-resource=true;available=51%;total=100%;used=49%
Supported: x-cisco-rai
Content-Length: 0
```

## How to Configure the Support for Resource Availability Indication Over SIP Trunks Feature

### Configuring Resource Groups and Resource Monitoring Parameters

### SUMMARY STEPS

- enable

- configure terminal

- voice class resource-group tag

- resource { cpu { 1-min-avg | 5-sec-avg } | ds0 | dsp | mem { io-mem | proc-mem | total-mem }} [ threshold high threshold-value low threshold-value ]

- end

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

voice class resource-group tag

#### Example:

```
Router(config)# voice class resource-group 1
```

Enters voice-class configuration mode and assigns a unique value to the resource group.

resource { cpu { 1-min-avg | 5-sec-avg } | ds0 | dsp | mem { io-mem | proc-mem | total-mem }} [ threshold high threshold-value low threshold-value ]

#### Example:

```
Router(config-class)# resource cpu 1-min-avg mem io-mem threshold high 5 low 1
```

Selects the required resources to be monitored and configures parameters for monitoring them.

end

#### Example:

```
Router(config-class)# end
```

Returns to privileged EXEC mode.

#### Troubleshooting Tips

You can use the show voice class resource-group command to display the configuration parameters for monitoring gateway resources.

### Configuring SIP RAI Mechanism

This task enables the router to extract the details of the SIP along with the index of the resource group that needs to be
                                 monitored.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- rai target target-address resource-group group-index [ transport [ tcp [ tls [ scheme { sip | sips }]] | udp ]]

- end

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters into SIP UA configuration mode.

rai target target-address resource-group group-index [ transport [ tcp [ tls [ scheme { sip | sips }]] | udp ]]

#### Example:

```
Router(config-class)# rai target ipv4:10.2.1.1 resource-group 1
```

Configures the SIP RAI mechanism.

end

#### Example:

```
Router(config-class)# end
```

Returns to privileged EXEC mode.

#### Troubleshooting Tips

You can use the debug rai command to enable debugging for RAI.

## Configuration Examples for the Support for Resource Availability Indication Over SIP Trunks Feature

### Example  Configuring Resource Groups and Resource Monitoring Parameters

The following example shows how to configure the resource group 1 to monitor CPU, DS0, DSP, and memory resources:

```
voice class resource-group 1
 resource cpu 1-min-avg threshold high 50 low 30
 resource ds0 threshold high 50 low 30
 resource dsp threshold high 50 low 30
 resource memory total-mem threshold high 50 low 30
 periodic-report interval 30
```

### Example Configuring SIP RAI Mechanism

```
sip-ua
 rai target ipv4:9.13.40.83 resource-group 1 transport udp
 rai target dns:whitesmoke resource-group 2 transport tcp
 rai target ipv6:[2217:10:10:10:10:10:10:2] resource-group 3  transport tcp
 rai target dns:butterfly resource-group 4 transport tcp tls scheme sips
 rai target ipv4:10.13.40.84 resource-group 5 transport tcp
 rai target ipv4:10.13.40.83 resource-group 1
```

## Additional References

### Related Documents

Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

Voice commands: complete command syntax, command mode, defaults, usage guidelines, and examples

Cisco IOS Voice Command Reference

### Standards

Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not been modified by this
                                          feature.

--

### MIBs

MIB

MIBs Link

No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature.

To locate and download MIBs for selected platforms, Cisco software releases, and feature sets, use Cisco MIB Locator found
                                          at the following URL:

http://www.cisco.com/go/mibs

### RFCs

RFC

Title

None

--

### Technical Assistance

Description

Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and
                                          resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product
                                          Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/cisco/web/support/index.html

## Feature Information for the Support for Resource Availability Indication Over SIP Trunks

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Support for Monitoring Utilization of Critical Resources on Gateway Router, Cisco UBE and Cisco UCME and Reporting Over SIP
                                          Trunks

15.1(2)T

The Support for Monitoring Utilization of Critical Resources on Gateway Router, Cisco UBE and Cisco UCME and Reporting Over
                                          SIP Trunks feature implements monitoring of resource utilization and reporting functionality over SIP trunk on Cisco IOS gateway,
                                          Cisco UBE and Cisco UCME.

The following commands were introduced or modified: debug rai , rai target , voice class resource-group , show voice class resource-group .

| Note | Call treatment is not handled as part of this feature on the gateway. If call treatment needs to be performed along with reporting,
                                          then the call threshold feature needs to be configured appropriately with desired threshold values. The gateway supports CPU,
                                          memory, and maximum number of calls per interface. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice class resource-group tag Example: Router(config)# voice class resource-group 1 | Enters voice-class configuration mode and assigns a unique value to the resource group. |
| Step 4 | resource { cpu { 1-min-avg \| 5-sec-avg } \| ds0 \| dsp \| mem { io-mem \| proc-mem \| total-mem }} [ threshold high threshold-value low threshold-value ] Example: Router(config-class)# resource cpu 1-min-avg mem io-mem threshold high 5 low 1 | Selects the required resources to be monitored and configures parameters for monitoring them. |
| Step 5 | end Example: Router(config-class)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters into SIP UA configuration mode. |
| Step 4 | rai target target-address resource-group group-index [ transport [ tcp [ tls [ scheme { sip \| sips }]] \| udp ]] Example: Router(config-class)# rai target ipv4:10.2.1.1 resource-group 1 | Configures the SIP RAI mechanism. |
| Step 5 | end Example: Router(config-class)# end | Returns to privileged EXEC mode. |

| Related Topic | Document Title |
|---|---|
| Cisco IOS commands | Cisco IOS Master Commands List, All Releases |
| Voice commands: complete command syntax, command mode, defaults, usage guidelines, and examples | Cisco IOS Voice Command Reference |

| Standard | Title |
|---|---|
| No new or modified standards are supported by this feature, and support for existing standards has not been modified by this
                                          feature. | -- |

| MIB | MIBs Link |
|---|---|
| No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature. | To locate and download MIBs for selected platforms, Cisco software releases, and feature sets, use Cisco MIB Locator found
                                          at the following URL: http://www.cisco.com/go/mibs |

| RFC | Title |
|---|---|
| None | -- |

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and
                                          resolving technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product
                                          Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/cisco/web/support/index.html |

| Feature Name | Releases | Feature Information |
|---|---|---|
| Support for Monitoring Utilization of Critical Resources on Gateway Router, Cisco UBE and Cisco UCME and Reporting Over SIP
                                          Trunks | 15.1(2)T | The Support for Monitoring Utilization of Critical Resources on Gateway Router, Cisco UBE and Cisco UCME and Reporting Over
                                          SIP Trunks feature implements monitoring of resource utilization and reporting functionality over SIP trunk on Cisco IOS gateway,
                                          Cisco UBE and Cisco UCME. The following commands were introduced or modified: debug rai , rai target , voice class resource-group , show voice class resource-group . |