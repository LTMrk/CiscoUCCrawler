---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-mcu-4203-112803-pqa-112803-00-html-9bb9b43742
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-mcu-4203/112803-pqa-112803-00.html
retrieved_at: 2026-08-21T06:29:08.915789+00:00
---

How do I call someone on a different IP network?

# How do I call someone on a different IP network?

Updated: April 23, 2015

Document ID: 112803

Contents

## Contents

## Introduction

This article relates to the Cisco TelePresence MCU 4203, Cisco TelePresence MCU MSE 8420, Cisco TelePresence IP GW 3510, Cisco TelePresence MCU 4505, Cisco TelePresence Video Communication Server Expressway, Cisco TelePresence Management Suite, Cisco IP Video Phone E20, Cisco TelePresence System Codec C90, Cisco TelePresence System Codec C60, Cisco TelePresence MCU MSE 8510, Cisco TelePresence System Codec C40 and Cisco TelePresence System EX90 products.

### Q. How do I call someone on a different IP network?

A. TANDBERG provides a number of different solutions that enable organizations on different networks to be able to communicate using video.

The TANDBERG VCS or Expressway solution

The TANDBERG VCS/Expressway is most suitable for large-scale deployments. It allows you to connect across organizations without requiring any exceptions or extra ports to be opened on the firewall. In this solution, both organizations need to have a VCS and you need to configure a connection between the two VCSs.

The IP Gateway solution

The TANDBERG Codian IP Gateway also allows organizations using different networks to connect using video. In this solution, no VCS is required. Only one of the organizations that want to connect together needs to have an IP Gateway. The IP Gateway allows video calls from the internet to endpoints inside the organization's private network without compromising security. For example, if "company B" has an IP Gateway, then "company A" can call into "company B," see the directory and scroll to find the person they want. The IT administrator may need to open ports on the company firewall to allow this.

The MCU solution

Organizations using the TANDBERG Codian MCU can configure it to have one port connected to their own network and one port connected to the internet. In this solution, you will need the video firewall feature key which enables people from outside your network to join video conferences securely and from any vendor's endpoint. For more information, see How do I configure the video firewall in a Codian MCU / IP VCR?

## Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

23-Apr-2015

Initial Release

### This Document Applies to These Products

- TelePresence Management Suite (TMS)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Apr-2015 | Initial Release |