---
doc_id: ucshcltool-cloudapps-cisco-com-public-3fec81b994
source_url: https://ucshcltool.cloudapps.cisco.com/public
retrieved_at: 2026-08-20T21:36:03.527785+00:00
---

UCS Hardware and Software Compatibility

View Change Log

Search By :

Servers

Server Type :

Search or Select Server Type (e.g. "C-Series Server")

Server Model :

Search or Select Server Model (e.g. "X210c M8, C240 M8L")

Processor Version :

Search or Select Processor (e.g. "Intel Xeon 6")

Operating System :

Search or Select Operating System (e.g "VMware, Microsoft, RedHat")

Operating System Version :

Search or Select Operating System Version

Choose or Drag and drop file.

Import JSON

Compatibility Notes 1 0

Customers can run Proxmox VE on Cisco UCS M7 and M8 servers. The inbox enic driver in Proxmox VE 9 provides native support for the Cisco VIC 15000 series adapters, and other components are also supported by Linux inbox drivers. Proxmox VE support is provided by Proxmox, their support partners, and the open-source community. For customers running Proxmox on UCS servers, Cisco TAC will provide hardware and firmware support for Cisco servers under the relevant warranties and support contracts.

GPU driver version listed in Cisco HCL is the minimum version Cisco has verified. Any newer driver in the same branch with same major number but higher minor number is supported.

Rocky Linux OS support on S3260M5 is limited to deployment with the Commvault solution

CentOS 7.9 support for C240, C220 and UCS-X M6 is limited to deployments with the Cohesity solution.

Cisco IMC 4.3(1) software is supported with Cisco C-Series M7 servers. Cisco HSU 5.1.0 is supported with Cisco X-Series M6 and M7 and B-Series M5 and M6 generation servers in Intersight Managed Mode

For VMware NSX-T related issues Cisco can provide only hardware troubleshooting support. For NSX-T software support we recommend customers to open a case with VMware.

For Hyperflex with external storage arrays, refer to Cisco UCS C-series/B-series Hardware and Software Compatibility matrix for supported storage arrays models and firmware versions.

Starting from vSphere 8.0, SD cards/USB media as a standalone boot device will not be supported by VMware. For more information please refer to the VMware KB article: https://kb.vmware.com/s/article/85685

The local storage controller firmware and driver combinations in this matrix do not apply to VMware vSAN deployments. For VMware vSAN deployments, consult the VMware Compatibility Guide - vSAN http://www.vmware.com/resources/compatibility/search.php?deviceCategory=vsan.

For community-supported operating systems not listed in the Cisco HCL, Cisco TAC will provide hardware and firmware support for Cisco servers under the relevant warranties and support contracts. Customers are responsible for obtaining support for these operating systems from the community or third-party providers.

UCS HCL Version 4.5.6 © 2015-2026 Cisco Systems. Inc. All rights reserved. Database updated on 08/19/2026