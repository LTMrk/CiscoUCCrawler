---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-3-cluster-creation-maint-exwy-b-cisco-expressway-48f62361e8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-3/cluster_creation_maint/exwy_b_cisco-expressway-cluster-creation-and-maintenance-deployment-guide-x143/exwy_m_about-this-guide.html
retrieved_at: 2026-08-16T15:17:30.410535+00:00
---

Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.3)

# Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.3)

Updated: March 18, 2025

Chapter: About This Guide

## Chapter: About This Guide

- About This Guide

- Information Covered

- Change History

# About This Guide

This chapter explains the following:

## Information Covered

From version X12.5 onwards, this guide applies only to the Cisco Expressway Series product (Expressway) and no longer applies
                           to the Cisco VCS product (VCS). Older VCS guides on Cisco.com are still valid for the VCS versions they apply to—as specified on the title page of each guide.

The guide covers the following topics:

Clustering Requirements

Describes the required network environment and minimum configuration of the peer Expressways before you can cluster them.

How to Form a Cluster

How to form a cluster of one, add peers to a cluster, and configure cluster address mapping if necessary.

How to Change a Cluster

Processes like upgrading, taking peers offline, changing the primary peer, and disbanding the cluster.

How to Connect the Expressway Cluster to Other Systems

How to connect the cluster with external systems like Cisco TMS, other Expressways, and endpoints.

Troubleshooting

Guidance that may assist if the cluster is not working as expected.

Reference

Additional material that may be relevant to your environment.

For information about license usage and capacity with clustered systems, refer to the Expressway Administrator Guide on the Cisco Expressway Series Maintain and Operate Guides page.

## Change History

Date

Change

Reason

March 2025

Removed the section "How to Rebuild a Cluster from Backup" from the "Troubleshooting" chapter.

Republished X14.3 release.

June 2023

First published for X14.3 release

Included a section "Usage Note for Expressway-E Traversal Zones" in chapter "(Optional) Use Fully Qualified Domain Names to
                                       Form a Cluster"

Included a Note to the section "Mix Cluster Deployment With Expressway and Expressway Select" in chapter "Clustering Requirements"

X14.3 release

July 2021

Updates for X14.0.2 release

Addressed a few CDETs

X14.0.2 release

April 2021

First published for X14.0 release

Included a few "Expressway Alarms and Warning" in the chapter "Troubleshooting"

X14.0 release

June 2020

Updated for X12.6. Also remove cluster license usage and capacity guidelines, which are now in the Expressway Administrator Guide .

Update Clustering Requirements to clarify DNS SRV record with A or AAAA records per peer for B2B deployments is recommended but not required.

X12.6 release and document correction

March 2019

Clarify that removal of a cluster peer deletes all configuration for the LAN2 interface in dual NIC deployments.

Clarification

February 2019

Updated for X12.5.

From this version, the guide applies only to Cisco Expressway Series and not to Cisco VCS.

X12.5 release

February 2019

Cluster Address Mapping section edited. Software version updated to X8.11.4 maintenance release. Other superficial enhancements
                                       to text.

Documentation defect, X8.11.4 release

September 2018

Updated for Webex and Spark platform rebranding, CE1200 appliance, and X8.11.1 maintenance release.

X8.11.1 release

August 2018

Corrected text and example in "Cluster Name and DNS SRV Records" section.

Correction

July 2018

Updated for X8.11.

X8.11 release

November 2017

Updated round trip delay and maximum hop distances in "Prerequisites" section.

Update

October 2017

Strengthened advice on cluster upgrade order.

Clarification

August 2017

Added note that all cluster peers should be configured in the same domain.

Omission

July 2017

Updated for X8.10.

X8.10 release

April 2017

Added section and related edits for cluster address mapping.

X8.9.2 release

December 2016

Added section on clusters in isolated networks in relation to TLS.

X8.9 release

June 2016

Cluster communications now use TLS. Registrations, FindMe, TMSPE support introduced on Expressway.

X8.8 release

November 2015

Updated for X8.7.

July 2015

Updated for X8.6. New procedure for replacing a peer.

April 2015

Menu path changes for X8.5 onwards. Republished with X8.5.2.

December 2014

Updated for X8.5.

June 2014

Republished for X8.2.

April 2014

Updated for Expressway X8.1.1:

New 'Upgrading a cluster' section for Expressway

New 'Replacing an Expressway peer' section

Updates to 'IP ports and protocols' appendix

December 2013

First release of Expressway version of this document. For older VCS versions see VCS Configuration Guides page.

| Date | Change | Reason |
|---|---|---|
| March 2025 | Removed the section "How to Rebuild a Cluster from Backup" from the "Troubleshooting" chapter. | Republished X14.3 release. |
| June 2023 | First published for X14.3 release Included a section "Usage Note for Expressway-E Traversal Zones" in chapter "(Optional) Use Fully Qualified Domain Names to
                                       Form a Cluster" Included a Note to the section "Mix Cluster Deployment With Expressway and Expressway Select" in chapter "Clustering Requirements" | X14.3 release |
| July 2021 | Updates for X14.0.2 release Addressed a few CDETs | X14.0.2 release |
| April 2021 | First published for X14.0 release Included a few "Expressway Alarms and Warning" in the chapter "Troubleshooting" | X14.0 release |
| June 2020 | Updated for X12.6. Also remove cluster license usage and capacity guidelines, which are now in the Expressway Administrator Guide . Update Clustering Requirements to clarify DNS SRV record with A or AAAA records per peer for B2B deployments is recommended but not required. | X12.6 release and document correction |
| March 2019 | Clarify that removal of a cluster peer deletes all configuration for the LAN2 interface in dual NIC deployments. | Clarification |
| February 2019 | Updated for X12.5. From this version, the guide applies only to Cisco Expressway Series and not to Cisco VCS. | X12.5 release |
| February 2019 | Cluster Address Mapping section edited. Software version updated to X8.11.4 maintenance release. Other superficial enhancements
                                       to text. | Documentation defect, X8.11.4 release |
| September 2018 | Updated for Webex and Spark platform rebranding, CE1200 appliance, and X8.11.1 maintenance release. | X8.11.1 release |
| August 2018 | Corrected text and example in "Cluster Name and DNS SRV Records" section. | Correction |
| July 2018 | Updated for X8.11. | X8.11 release |
| November 2017 | Updated round trip delay and maximum hop distances in "Prerequisites" section. | Update |
| October 2017 | Strengthened advice on cluster upgrade order. | Clarification |
| August 2017 | Added note that all cluster peers should be configured in the same domain. | Omission |
| July 2017 | Updated for X8.10. | X8.10 release |
| April 2017 | Added section and related edits for cluster address mapping. | X8.9.2 release |
| December 2016 | Added section on clusters in isolated networks in relation to TLS. | X8.9 release |
| June 2016 | Cluster communications now use TLS. Registrations, FindMe, TMSPE support introduced on Expressway. | X8.8 release |
| November 2015 | Updated for X8.7. |  |
| July 2015 | Updated for X8.6. New procedure for replacing a peer. |  |
| April 2015 | Menu path changes for X8.5 onwards. Republished with X8.5.2. |  |
| December 2014 | Updated for X8.5. |  |
| June 2014 | Republished for X8.2. |  |
| April 2014 | Updated for Expressway X8.1.1: New 'Upgrading a cluster' section for Expressway New 'Replacing an Expressway peer' section Updates to 'IP ports and protocols' appendix |  |
| December 2013 | First release of Expressway version of this document. For older VCS versions see VCS Configuration Guides page. |  |