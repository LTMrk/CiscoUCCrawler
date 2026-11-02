---
doc_id: help-webex-com-en-us-article-n6he59h-9c665f6e44
source_url: https://help.webex.com/en-us/article/n6he59h
retrieved_at: 2026-11-02T13:11:20.706555+00:00
---

Follow the workflow to register your phones to a BroadWorks platform.

Before you begin

Log in with your Cisco account to view and download resources from Cisco.com.

Download the CPE Kit from cisco.com. To download the latest CPE kits, go to this URL: https://www.cisco.com/c/en/us/support/unified-communications/broadworks/products-installation-and-configuration-guides-list.html .

Import the most recent DTAF file to the BroadWorks (system level) server.

For the procedures, see the section Configure BroadWorks Device Profile Type in Cisco BroadSoft Partner Configuration Guide Cisco
                Multi-Platform Phone .

Configure Broadworks Device Profile Type.

For the procedures, see the section Cisco Broadworks Device Profile Type
              Configuration in Cisco BroadSoft Partner Configuration Guide Cisco
                Multi-Platform Phone .

## OOB onboarding flowchart

The following Out-Of-Box (OOB) flowchart shows the process for phone onboarding.

OOB: Phone is just taken out of the phone box and turned on for its initial onboarding to
        the target call control system.

Click the chart to view it in full size.

Near Field Communication (NFC) is only available on Cisco Desk Phone 9841, 9851, 9861, and 9871.

### Provisioning with DHCP options

The phone can automatically locate its configuration server through DHCP options. During a
        resync, the phone queries the following DHCP options:

- IPv4: 66, 160, 159, 150

- IPv6: 17, 160, 159

Based on the DHCP response, the phone behaves as follows:

If a valid file is found, the phone will register in MPP mode using that file.

If the DHCP option does not specify a file name, the phone tries the following default
            paths in sequence:

- /$PSN.xml

- /Cisco/$PN/$MA.cfg

where

- $PSN = Phone Serial Number

- $PN = Phone Product Name

- $MA = Phone MAC Address

If DHCP responds but no valid file is available, the phone will attempt CDA

If DHCP query times out (no server response), the phone will proceed to query DHCP
            150/66 for the default provisioning file to register with CUCM.

| 1 | Download the CPE Kit from cisco.com. To download the latest CPE kits, go to this URL: https://www.cisco.com/c/en/us/support/unified-communications/broadworks/products-installation-and-configuration-guides-list.html . |
|---|---|
| 2 | Import the most recent DTAF file to the BroadWorks (system level) server. For the procedures, see the section Configure BroadWorks Device Profile Type in Cisco BroadSoft Partner Configuration Guide Cisco
                Multi-Platform Phone . |
| 3 | Configure Broadworks Device Profile Type. For the procedures, see the section Cisco Broadworks Device Profile Type
              Configuration in Cisco BroadSoft Partner Configuration Guide Cisco
                Multi-Platform Phone . |

## Figuras

![PhoneOS Devices Onboarding Flowchart](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487668.png)