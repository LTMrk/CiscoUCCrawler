---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-0-1-userguide-cplm-bk-u2c0c808-00-user-guide-rel-1101-cplm-bk-u2-cc189c7117
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_0_1/userguide/CPLM_BK_U2C0C808_00_user-guide-rel-1101/CPLM_BK_U2C0C808_00_user-guide-rel-1101_chapter_00.html
retrieved_at: 2026-09-08T05:00:40.806788+00:00
---

Cisco Prime License Manager User Guide, Release 11.0(1)

# Cisco Prime License Manager User Guide, Release 11.0(1)

Updated: September 12, 2017

Chapter: Deployment

## Chapter: Deployment

# Deployment

## Deployment
	 Options

Coresident deployments— Cisco Prime License Manager is installed automatically
		  as part of the installation of Cisco
			 Unified Communications Manager and Cisco Unity Connection. You may choose to run Cisco Prime License Manager on one of these servers in
		  a coresident configuration. Refer to the latest release of the
		  platform-specific installation document for more information:

Standalone deployments—You need two files to install Cisco Prime License Manager:

A virtual machine template (OVA file) is available from Software Download Center.

An ISO file is available  via electronic software download after you purchase Cisco Unified Communications Manager or Cisco Unity Connection.

## Requirements

### System
	 Requirements

Here are the server requirements as defined in the virtual machine template that should be
		  used to install a standalone instance of Cisco Prime License Manager.

Version

11.0(1)

CPU

1 vCPU with 1800 Mhz reservation

Memory

4 GB (RAM) with 4 GB reservation

Hard Drive

1 - 50 GB disk

### Port
	 Requirements

The following
		  table provides a list of ports used by Cisco Prime License Manager. If you wish to use automatic license fulfillment, Cisco Prime License Manager should be allowed direct outbound access to the Internet.

Browser
						HTTP

TCP

80/8080, 443/8443

N/A

SSH/SFTP

TCP

22

N/A

Ephemeral port ranges for clients initiating connections

TCP,
						UDP

32768-61000

N/A

DNS
						name resolution

TCP,
						UDP

N/A

53

To
						connect to Product instances and to the Cisco licensing portal for e-Fulfillment

TCP

N/A

80,
						8080, 443, 8443 (HTTP and HTTPS)

DRS

TCP

N/A

22
						(SSH/SFTP)

DHCP
						client

UDP

N/A

67

NTP
						client

TCP,
						UDP

N/A

123

### Supported Products

Cisco Unified Communications Manager

Cisco Unity Connection

Cisco Emergency Responder

### Supported Locales

The following
		  locales are supported for Cisco Prime License Manager:

- English (default)

- Japanese

- Chinese (simplified)

- Korean

- Chinese (traditional)

- German

- French (France)

- Italian

- Spanish (Spain)

- Spanish (Latin American)
			 - also known as Spanish (Colombia)

- Portuguese (Brazil)

- Dutch (Netherlands)

- Russian

### Supported
	 Browsers

The following
		  table defines Cisco Prime License Manager browser support:

Chrome 22

Supported

Supported

Supported

The following
			 browsers and operating systems are not currently supported: Opera, Linux OS,
			 Google Chrome OS.

| Requirement | Details |
|---|---|
| Version | 11.0(1) |
| CPU | 1 vCPU with 1800 Mhz reservation |
| Memory | 4 GB (RAM) with 4 GB reservation |
| Hard Drive | 1 - 50 GB disk |

| Description | Protocol | Inbound
						Port | Outbound
						Port |
|---|---|---|---|
| Browser
						HTTP | TCP | 80/8080, 443/8443 | N/A |
| SSH/SFTP | TCP | 22 | N/A |
| Ephemeral port ranges for clients initiating connections | TCP,
						UDP | 32768-61000 | N/A |
| DNS
						name resolution | TCP,
						UDP | N/A | 53 |
| To
						connect to Product instances and to the Cisco licensing portal for e-Fulfillment | TCP | N/A | 80,
						8080, 443, 8443 (HTTP and HTTPS) |
| DRS | TCP | N/A | 22
						(SSH/SFTP) |
| DHCP
						client | UDP | N/A | 67 |
| NTP
						client | TCP,
						UDP | N/A | 123 |

| Browser | Browser Version | Windows OS | Apple OS |
|---|---|---|---|
| Win 8 | Windows 7 (32 and 64 bit) | OSX 10.8 |
| Firefox | FF 17-33 | Supported | Supported | Supported |
| Chrome | Chrome 23-24 | Supported | Supported | Supported |
| Chrome 22 | Supported | Supported | Supported |
| Safari | Safari 6.0-6.1 | Not supported | Not supported | Supported |
| Internet Explorer | IE 9-10 | Supported | Supported | N/A |
| IE 8 | Not supported | Secondary | N/A |

| Note | The following
			 browsers and operating systems are not currently supported: Opera, Linux OS,
			 Google Chrome OS. |
|---|---|