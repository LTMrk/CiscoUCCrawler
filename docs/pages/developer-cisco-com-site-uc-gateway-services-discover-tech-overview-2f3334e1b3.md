---
doc_id: developer-cisco-com-site-uc-gateway-services-discover-tech-overview-2f3334e1b3
source_url: https://developer.cisco.com/site/uc-gateway-services/discover/tech-overview/
retrieved_at: 2026-08-25T21:11:16.922089+00:00
---

## Introduction

The Cisco Unified Communication Gateway Services API, supported on Cisco ISR-G2 Voice 		Gateways, provides visibility and control of real time signaling and media voice 			        traffic being routed through the gateway, whether via TDM or SIP trunk interfaces to        the Service Provider. The API enables applications to instruct the Cisco Voice        Gateway to take policy control, including such actions as call termination, call        redirection or call forking (for recording) to support a wide range of voice network        use cases.

The Cisco UC Gateway Services API is available with both the Cisco Unified Border         Element (CUBE) and Cisco TDM Gateway, both of which are supported on the ISR-G2
         platform. As a result, the API enables external application integration using the         Cisco ISR-G2 gateway with either SIP or TDM trunks to the service provider.          Therefore, the services enabled by this API can be extended across all ISR-G2-based          voice gateways throughout the entire enterprise on a global basis to achieve the          service benefits through monitoring and  control of the edge voice network no          matter what stage the enterprise voice network might be in transitioning from TDM          trunks to SIP trunks.

## Usage

- Applications may monitor or control live sessions on Cisco ISR-G2 Voice Gateway configured either for TDM Gateway functionality or for CUBE session border control functionality, or both.

- Cisco UC Gateway Services API is entirely web-based, which means that WSDL-compatible development tools can be used to define schemas to be used to interact with this API.

- Three categories of API messages are provided with the UC Gateway Services Interface, referred to as Extended Call Control, (XCC), Extended Call Detail Record (XCDR) and Extended Serviceability (XSVC)

- Extended Call Control (XCC) provider supports operations that allow an application to perform call control and real-time call monitoring of active call sessions traversing the gateway

- Extended Call Control (XCC) also performs monitoring of certain aspects of the voice media, including DTMF events, control of media forking, and call mode changes.

- Extended Call Control (XCC) call mode changes that are detectable include the following modes:

- Voice Call

- Fax Call

- Video Call

- Modem Call

- Data Call

- Extended Call Control (XCC) enables the voice gateway to provide notification of the following specified tones:

- Busy Tone

- Dial Tone

- Ring back Tone

- Out-of-Service Tone

- Second Dial Tone

- Extended Call Detail Record (XCDR) provider supplies CDR information to the application and notifies the application when calls have ended.

- Extended Serviceability (XSVC) provider monitors trunk status, and provides real-time link status and configuration change notification to application.

## Tech Details

The Cisco Unified Communication Gateway Services API supports the following standard protocols:

- XML 1.0

- Web Services Description Language (WSDL) 1.1 (http://www.w3.org/TR/wsdl20-primer/)

- SOAP, version 1.2 (http://www.w3.org/TR/soap12-part1/)

- HTTP, version 1.1

## Cisco UC Gateway Services API Architecture

Below is a diagram that illustrates the architecture of Cisco UC Gateway Services API: