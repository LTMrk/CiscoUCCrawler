---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-5-exwy-b-mra-expressway-deployment-guide-exwy-b--e80c656fcc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-5/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_01111.html
retrieved_at: 2026-08-16T15:35:38.558282+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

Updated: September 13, 2019

Chapter: About the Documentation

## Chapter: About the Documentation

# About the Documentation

## Change History

Date

Change

Reason

April 2020

Various clarifications and corrections to the guide.

Document corrections & enhancements

December 2019

Various clarifications to the guide:

Reverse DNS requirement updates

TLS verify subject name requirement

Minimum TLS version pre-11.5(1)SU3

No call preservation if node fails

Document corrections & enhancements

March 2019

Clarify that from X12.5, local DNS no longer requires _cisco-uds._tcp.<domain> SRV records (still recommended).

Document correction

February 2019

Clarify UID mapping is mandatory on IdP for single, cluster-wide SAML agreement.

Content enhancement

February 2019

Add Jabber 12.5 clients to supported endpoints for ICE passthrough (subject to Unified CM 12.5).

Software dependency change

January 2019

Fixed CE version for ICE support in MRA to 9.6.1 or later.

Removed Jabber endpoints from ICE for MRA supported components.

Correction to section Unsupported Expressway Features and Limitations for ICE for MRA with Static NAT.

Document correction

January 2019

Updated for X12.5.

X12.5 release

September 2018

Updated for X8.11.2 (change to Unsupported Expressway Features and Limitations for chat/messaging if user authentication by OAuth refresh).

X8.11.2 release

September 2018

Updated for Webex and Spark platform rebranding, and for X8.11.1 maintenance release.

Added, to Unsupported Expressway Features and Limitations section, a known issue with chat/messaging services over MRA if user authentication is by OAuth refresh (self-describing
                                          tokens).

X8.11.1 release

Clarification

July 2018

Included Hunt Group support, subject to Cisco Unified Communications Manager 11.5(1)SU5 or later fixed version.

Software dependency change

July 2018

Updated for X8.11. Also removed port reference topic, which is now available in the Cisco Expressway IP Port Usage Guide .

X8.11 release

May 2018

Clarify MFT over MRA is not supported when using an unrestricted version of IM and Presence Service .

Clarification

March 2018

Clarify no Jabber support for redundant UDS services.

Clarification

December 2017

Added configuration step to enable SIP protocol (disabled by default on new installs).

Content defect

November 2017

Clarified which Cisco IP Phones in the 88xx series support MRA (Configuration Overview section).

Content defect

September 2017

Added links to information about supported features for MRA-connected endpoints. Add information about Collaboration Solutions
                                          Analyzer.

Content enhancement

August 2017

Deskphone control functions bullet removed from "Unsupported Contact Center Features" as not applicable.

Content defect

July 2017

Clarify required versions for Unified Communications software. Corrected duplicated prerequisites for Push Notifications feature.

Content defect

July 2017

Updated.

X8.10 release

April 2017

Added details on partial support for Cisco Jabber SDK features.

Content defect

January 2017

Updated section on unsupported features when using MRA. Added description of Maintenance Mode. Clarified that Expressway-C
                                          and Expressway-E need separate IP addresses.

X8.9.1 release

December 2016

Updated.

X8.9 release

September 2016

Unsupported deployments section updated. Minimum versions note about TLS added.

Clarification to avoid misconfiguration

August 2016

Updated DNS prerequisite to create reverse lookup entries for Expressway-E.

Customer found defect

June 2016

HTTP Allow list feature updates.

X8.8 release

Entries before X8.8 are removed for clarity

## This Guide Does not Apply for the VCS

New features in software version X12.5 and later are not supported for the Cisco TelePresence Video Communication Server (VCS)
                                          product. They apply only to the Cisco Expressway Series (Expressway) product. This software version is provided for the VCS
                                          for maintenance and bug fixing purposes only.

From version X12.5 onwards, this guide applies only to the Cisco Expressway Series product (Expressway) and no longer applies
                              to the Cisco VCS product (VCS).

## Related Documents

The following documents may help with setting up your environment:

| Date | Change | Reason |
|---|---|---|
| April 2020 | Various clarifications and corrections to the guide. | Document corrections & enhancements |
| December 2019 | Various clarifications to the guide: Reverse DNS requirement updates TLS verify subject name requirement Minimum TLS version pre-11.5(1)SU3 No call preservation if node fails | Document corrections & enhancements |
| March 2019 | Clarify that from X12.5, local DNS no longer requires _cisco-uds._tcp.<domain> SRV records (still recommended). | Document correction |
| February 2019 | Clarify UID mapping is mandatory on IdP for single, cluster-wide SAML agreement. | Content enhancement |
| February 2019 | Add Jabber 12.5 clients to supported endpoints for ICE passthrough (subject to Unified CM 12.5). | Software dependency change |
| January 2019 | Fixed CE version for ICE support in MRA to 9.6.1 or later. Removed Jabber endpoints from ICE for MRA supported components. Correction to section Unsupported Expressway Features and Limitations for ICE for MRA with Static NAT. | Document correction |
| January 2019 | Updated for X12.5. | X12.5 release |
| September 2018 | Updated for X8.11.2 (change to Unsupported Expressway Features and Limitations for chat/messaging if user authentication by OAuth refresh). | X8.11.2 release |
| September 2018 | Updated for Webex and Spark platform rebranding, and for X8.11.1 maintenance release. Added, to Unsupported Expressway Features and Limitations section, a known issue with chat/messaging services over MRA if user authentication is by OAuth refresh (self-describing
                                          tokens). | X8.11.1 release Clarification |
| July 2018 | Included Hunt Group support, subject to Cisco Unified Communications Manager 11.5(1)SU5 or later fixed version. | Software dependency change |
| July 2018 | Updated for X8.11. Also removed port reference topic, which is now available in the Cisco Expressway IP Port Usage Guide . | X8.11 release |
| May 2018 | Clarify MFT over MRA is not supported when using an unrestricted version of IM and Presence Service . | Clarification |
| March 2018 | Clarify no Jabber support for redundant UDS services. | Clarification |
| December 2017 | Added configuration step to enable SIP protocol (disabled by default on new installs). | Content defect |
| November 2017 | Clarified which Cisco IP Phones in the 88xx series support MRA (Configuration Overview section). | Content defect |
| September 2017 | Added links to information about supported features for MRA-connected endpoints. Add information about Collaboration Solutions
                                          Analyzer. | Content enhancement |
| August 2017 | Deskphone control functions bullet removed from "Unsupported Contact Center Features" as not applicable. | Content defect |
| July 2017 | Clarify required versions for Unified Communications software. Corrected duplicated prerequisites for Push Notifications feature. | Content defect |
| July 2017 | Updated. | X8.10 release |
| April 2017 | Added details on partial support for Cisco Jabber SDK features. | Content defect |
| January 2017 | Updated section on unsupported features when using MRA. Added description of Maintenance Mode. Clarified that Expressway-C
                                          and Expressway-E need separate IP addresses. | X8.9.1 release |
| December 2016 | Updated. | X8.9 release |
| September 2016 | Unsupported deployments section updated. Minimum versions note about TLS added. | Clarification to avoid misconfiguration |
| August 2016 | Updated DNS prerequisite to create reverse lookup entries for Expressway-E. | Customer found defect |
| June 2016 | HTTP Allow list feature updates. | X8.8 release |
|  | Entries before X8.8 are removed for clarity |  |

| Important | New features in software version X12.5 and later are not supported for the Cisco TelePresence Video Communication Server (VCS)
                                          product. They apply only to the Cisco Expressway Series (Expressway) product. This software version is provided for the VCS
                                          for maintenance and bug fixing purposes only. |
|---|---|