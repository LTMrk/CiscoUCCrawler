---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-all-models-xsi-9-1-1-cuip-bk-p82b3b16-00-phones-services-application--f27db1eeec
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes1_appendix_01101.html
retrieved_at: 2026-08-16T18:02:14.316984+00:00
---

Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

# Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

Updated: August 6, 2026

Chapter: Device Capability Query via CTI Feature

## Chapter: Device Capability Query via CTI Feature

# Device Capability Query via CTI Feature

## Feature Description

The Device Capability Query via CTI feature was added for Cisco Unified Communications Manager Release 8.0(1).

A backend CTI application that communicates with the phone using the UserData tunnel cannot retrieve information on device
                              capabilities such as XSI feature support on a phone. Due to this lack of information, and to ensure compatibility, only a
                              minimum set of features were generally configured.

The Device Capability Query via CTI feature overcomes this limitation. This feature allows a CTI-based application or a Cisco
                              Unified Communications Manager application to query a registered phone for device capabilities using the UserData tunnel interface
                              of the phone (over SCCP or SIP and RemoteCC).

Applications that have an HTTP interface with a phone do not have this limitation. The HTTP request from such phones include
                              XSI capabilities header, and the DeviceInformationX servlet of such phones can be accessed to retrieve other device information.

Although designed to work using CTI over the UserData tunnel, this feature can also work over HTTP using the POST method.

## Supported IP Phones and Codecs

The following table lists the Cisco Unified IP Phone models that support the Device Capability Query via CTI feature.

Cisco Desk Phone 9800 series

9811

PhoneOS 4.0(1) and later

9841

On-premises: PhoneOS 3.0(1) and later

Multiplatform: PhongOS 3.2(1) and later

9851

On-premises: PhoneOS 3.0(1) and later

Multiplatform: PhongOS 3.2(1) and later

9861/9861NR

On-premises: PhoneOS 3.1(1) and later

Multiplatform: PhongOS 3.2(1) and later

9871/9871NR

On-premises: PhoneOS 3.1(1) and later

Multiplatform: PhongOS 3.2(1) and later

Cisco IP Phone 8800 Series

Not supported on 8800 Series (except 8875) running multiplatform firmware

8811

10.2(2) and later

8841, 8851, 8861

10.2(1) and later

8851NR

10.3(1) and later

8845, 8865

10.3(2) and later

8865NR

11.7(1) and later

8875, 8875NR

On-premises: PhoneOS 2.1(1) and later

Multiplatform: PhoneOS 3.2(1) and later

Cisco IP Conference Phones

Not supported on all Multiplatform phones

8831

9.3(3) and later

8832

12.0(1) and later

7832

12.0(1) and later

8821

11.0(1) and later

9821

PhoneOS 5.0(1) and later

Cisco IP Phone 7800 Series

Not supported on all Multiplatform phones

7811

10.3(1) and later

7821

9.1(1) and later

7841

9.1(1) and later

7861

9.1(1) and later

Cisco recommends the use of latest firmware. The firmware can be downloaded from the following location (requires login or
                                          service contract):

http://software.cisco.com/download/navigator.html?i=!mmd

Although several codecs are listed within the schema, only the codecs G711, G729, and G722 are currently supported.

## XML Object Changes

To support this feature, new request and response objects are created. The <getDeviceCaps> is the request object and the <getDeviceCapsResponse> is the response object.

On receiving the <getDeviceCaps> object, the phone returns the <getDeviceCapsResponse> object. All elements in the <getDeviceCapsResponse> object are required and must not be null.

## Schema Definition

The getDeviceCapsResponse XML schema is as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<schema targetNamespace="http://www.example.org/devicecaps" xmlns:tns="http://www.example.org/devicecaps" xmlns="http://www.w3.org/2001/XMLSchema">
	<element name="getDeviceCapsResponse" type="tns:deviceCapType" nillable="true"/>
	<complexType name="deviceCapType">
		<all>
			<element name="physical" type="tns:physicalCapType" nillable="true"/>
			<element name="services" nillable="true">
				<complexType>
					<complexContent>
						<extension base="tns:servicesCapType">
							<attribute name="sdkVersion" type="string" use="required"/>
						</extension>
					</complexContent>
				</complexType>
			</element>
		</all>
	</complexType>
	<complexType name="physicalCapType">
		<all>
			<element name="modelNumber" nillable="false">
				<simpleType>
					<restriction base="string">
						<maxLength value="32"/>
						<minLength value="1"/>
					</restriction>
				</simpleType>
			</element>
			<element name="display" nillable="true">
				<complexType>
					<attribute name="width" type="unsignedShort" use="required"/>
					<attribute name="height" type="unsignedShort" use="required"/>
					<attribute name="bitDepth" type="unsignedShort" use="required"/>
					<attribute name="isColor" type="boolean" use="required"/>
				</complexType>
			</element>
		</all>
	</complexType>
	<complexType name="servicesCapType">
		<all>
			<element name="browser" type="tns:browserCapType" nillable="true"/>
		</all>
	</complexType>
	<complexType name="browserCapType">
		<all>
			<element name="accept" nillable="false"/>
			<element name="acceptLanguage" nillable="false"/>
			<element name="acceptCharset" nillable="false"/>
		</all>
	</complexType>
</schema>
```

## Request and Response Examples for getDeviceCaps

The following are the request and response examples for a getDeviceCaps object:

```
<getDeviceCaps/>
```

```
<getDeviceCapsResponse>
  <physical>
    <modelNumber>CP-7970</modelNumber> 
    <display width="298" height="168" bitDepth="12" isColor="true"/>
  </physical>
  	<services sdkVersion="5.0.3">
    <browser>
	</services>
</getDeviceCapsResponse>
```

## Troubleshooting

The following error may occur in this feature:

If the getDeviceCaps object is invalid (misspelled), a parsing error is generated and a CiscoIPPhoneError object (with Number="1")
                                    is returned as the response.

### Error Handling

Standard XML services debugging techniques are applied to this feature.

The root cause for any parsing errors is displayed in the phone console logs. For HTTP requests and responses, sniffer traces
                                 and web server debug can be used to examine the getDeviceCaps object to ensure that it conforms to the schema.

| Phone model | Firmware supported |
|---|---|
| Cisco Desk Phone 9800 series |
| 9811 | PhoneOS 4.0(1) and later |
| 9841 | On-premises: PhoneOS 3.0(1) and later Multiplatform: PhongOS 3.2(1) and later |
| 9851 | On-premises: PhoneOS 3.0(1) and later Multiplatform: PhongOS 3.2(1) and later |
| 9861/9861NR | On-premises: PhoneOS 3.1(1) and later Multiplatform: PhongOS 3.2(1) and later |
| 9871/9871NR | On-premises: PhoneOS 3.1(1) and later Multiplatform: PhongOS 3.2(1) and later |
| Cisco IP Phone 8800 Series Note Not supported on 8800 Series (except 8875) running multiplatform firmware | Note | Not supported on 8800 Series (except 8875) running multiplatform firmware |
| Note | Not supported on 8800 Series (except 8875) running multiplatform firmware |
| 8811 | 10.2(2) and later |
| 8841, 8851, 8861 | 10.2(1) and later |
| 8851NR | 10.3(1) and later |
| 8845, 8865 | 10.3(2) and later |
| 8865NR | 11.7(1) and later |
| 8875, 8875NR | On-premises: PhoneOS 2.1(1) and later Multiplatform: PhoneOS 3.2(1) and later |
| Cisco IP Conference Phones Note Not supported on all Multiplatform phones | Note | Not supported on all Multiplatform phones |
| Note | Not supported on all Multiplatform phones |
| 8831 | 9.3(3) and later |
| 8832 | 12.0(1) and later |
| 7832 | 12.0(1) and later |
| Cisco Wireless Phones |
| 8821 | 11.0(1) and later |
| 9821 | PhoneOS 5.0(1) and later |
| Cisco IP Phone 7800 Series Note Not supported on all Multiplatform phones | Note | Not supported on all Multiplatform phones |
| Note | Not supported on all Multiplatform phones |
| 7811 | 10.3(1) and later |
| 7821 | 9.1(1) and later |
| 7841 | 9.1(1) and later |
| 7861 | 9.1(1) and later |

| Note | Not supported on 8800 Series (except 8875) running multiplatform firmware |
|---|---|

| Note | Not supported on all Multiplatform phones |
|---|---|

| Note | Not supported on all Multiplatform phones |
|---|---|

| Note | Cisco recommends the use of latest firmware. The firmware can be downloaded from the following location (requires login or
                                          service contract): |
|---|---|