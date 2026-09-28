---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-0-2-virtual-machine-exwy-b-cisco-expressway-on--d3d4853f94
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-0-2/virtual-machine/exwy_b_cisco-expressway-on-virtual-machine-installation-guide-x1502/exwy_m_about-the-documentation.html
retrieved_at: 2026-08-16T22:10:44.497669+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X15.0.2)

# Cisco Expressway on Virtual Machine Installation Guide (X15.0.2)

Updated: May 15, 2024

Chapter: About the Documentation

## Chapter: About the Documentation

# About the Documentation

## This Guide does not Apply for VCS

New features in software version X12.5 and later are not supported for the Cisco TelePresence Video Communication Server product
                              (VCS). They apply only to the Cisco Expressway Series product (Expressway). This software version is provided for the VCS
                              for maintenance and bug fixing purposes only.

## Change History

Date

Change

Reason

May 2024

Updated for X15.0.2 release.

Updated the section "ESXi Requirements" and "Limitations."

X15.0.2 release

December 2023

Updated for X15.0 release.

X15.0 release

May 2023

Updated for X14.3 release.

Updated the section "ESXi Requirements", Replaced screenshot with dagger symbol to a new symbol, Revamped the guide, that
                                          is, removed repeated headings  and aligned guide as per Cisco standards

X14.3 release

June 2022

Updated for X14.2 release.

Fixed a few CDETS.

X14.2 release

July 2021

Updated for X14.0.2 release.

Updated section "Configuring the VM Guest (vCenter)".

X14.0.2 release

June 2021

Updated for X14.0.1 release.

Fixed a few CDETS.

X14.0.1 release

April 2021

Updated for X14.0 release.

Replaced screenshot in the section "Deploying OVA to Host Managed by vCenter" because a new Port is introduced.

X14.0 release

December 2020

Added a section, "Automating the deployment process" in the "Installing a Virtual Machine" chapter. Also, updated the sections,
                                          "Deploying OVA to Host Managed by vCenter", and "ESXi Requirements".

X12.7 release

July 2020

Updated for X12.6.1. Added a section, "How to Increase
                                          ExpresswayVM Capacity" in the "System Requirements" chapter.
                                          Also, updated the section, "Upgrading or Downgrading an
                                          Expressway VM".

X12.6.1

June 2020

Added a new section "How to Modify Expressway Capacity" in
                                          Chapter 3, "System Requirements". Also, modified the section
                                          "Upgrading or Downgrading an Expressway VM".

Document correction

June 2020

X12.6 release. Also, modified Chapter 5 by removing obsolete
                                          content and rearranging/modifying steps.

X12.6

July 2019

Updated for X12.5.4. Removed references to release key as it is
                                          not required to upgrade a system on X8.6.x or later software to
                                          12.5.4 or later

Clarify reserved CPU resource for Large VMs

X12.5.4

May 2019

Clarify virtual machine name, hostname, and domain name must contain only ASCII characters.

Clarification

April 2019

Remove caveat that Small VM is for BE6000 platforms only, as now also supported on VMware ESXi platforms (subject to same
                                          minimum hardware specification as BE6000).

Update

January 2019

Updated for X12.5

X12.5

September 2018

Change software version from X8.11 to X8.11.1, as X8.11 is no longer available.

Software withdrawn

August 2018

Add requirement not to change MAC address of VM (serial number of virtual Expressway is based on the address).

Clarification

August 2018

Clarify VM console requirement for factory reset process.

Clarification

July 2018

Republished as single variant to cover both Cisco Expressway and Cisco VCS.

Document change

May 2018

Revised the Recommended Platform section to clarify that the Flashbased client may be required (version dependent).

Clarification

November 2017

Updated the Recommended Platform section regarding VMware vSphere client availability.

Clarification

August 2017

Added ESXi 6.5 support.

Validation complete

July 2017

Removed requirement for 10 Gb NIC on large systems. Removed support for ESXi 5.0 and ESXi 5.1. Other minor documentation changes

X8.10 updates

January 2017

Updated to include bug fix in relation to unsupported SSH key message in Install Wizard. Wizard now displays serial and release
                                          key for reference. Added caution regarding use of backslashes or forward slashes in Name and Location field.

X8.9.1 updates

December 2016

Updated to include new secure install wizard functionality.

X8.9 updates

June 2016

Decreased CPU reservation for Large OVA. Mention lack of support for VMware HA and VMware snapshots.

X8.8 updates

February 2016

Updated for X8.7.1.

Upgrade prerequisite added for Hybrid Services

November 2015

Updated for X8.7. ESXi 6.0 support added. Virtual hardware version change 7 to 8.

July 2015

Republished for X8.6.

December 2014

Republished for X8.5

August 2014

Removed misleading RAID 5 prerequisite for UCS.

June 2014

Republished for X8.2

December 2013

Initial release of Expressway variant of this document.

X8.1 release

## Related Documents

The following documents may help with setting up your environment:

| Date | Change | Reason |
|---|---|---|
| May 2024 | Updated for X15.0.2 release. Updated the section "ESXi Requirements" and "Limitations." | X15.0.2 release |
| December 2023 | Updated for X15.0 release. | X15.0 release |
| May 2023 | Updated for X14.3 release. Updated the section "ESXi Requirements", Replaced screenshot with dagger symbol to a new symbol, Revamped the guide, that
                                          is, removed repeated headings  and aligned guide as per Cisco standards | X14.3 release |
| June 2022 | Updated for X14.2 release. Fixed a few CDETS. | X14.2 release |
| July 2021 | Updated for X14.0.2 release. Updated section "Configuring the VM Guest (vCenter)". | X14.0.2 release |
| June 2021 | Updated for X14.0.1 release. Fixed a few CDETS. | X14.0.1 release |
| April 2021 | Updated for X14.0 release. Replaced screenshot in the section "Deploying OVA to Host Managed by vCenter" because a new Port is introduced. | X14.0 release |
| December 2020 | Added a section, "Automating the deployment process" in the "Installing a Virtual Machine" chapter. Also, updated the sections,
                                          "Deploying OVA to Host Managed by vCenter", and "ESXi Requirements". | X12.7 release |
| July 2020 | Updated for X12.6.1. Added a section, "How to Increase
                                          ExpresswayVM Capacity" in the "System Requirements" chapter.
                                          Also, updated the section, "Upgrading or Downgrading an
                                          Expressway VM". | X12.6.1 |
| June 2020 | Added a new section "How to Modify Expressway Capacity" in
                                          Chapter 3, "System Requirements". Also, modified the section
                                          "Upgrading or Downgrading an Expressway VM". | Document correction |
| June 2020 | X12.6 release. Also, modified Chapter 5 by removing obsolete
                                          content and rearranging/modifying steps. | X12.6 |
| July 2019 | Updated for X12.5.4. Removed references to release key as it is
                                          not required to upgrade a system on X8.6.x or later software to
                                          12.5.4 or later Clarify reserved CPU resource for Large VMs | X12.5.4 |
| May 2019 | Clarify virtual machine name, hostname, and domain name must contain only ASCII characters. | Clarification |
| April 2019 | Remove caveat that Small VM is for BE6000 platforms only, as now also supported on VMware ESXi platforms (subject to same
                                          minimum hardware specification as BE6000). | Update |
| January 2019 | Updated for X12.5 | X12.5 |
| September 2018 | Change software version from X8.11 to X8.11.1, as X8.11 is no longer available. | Software withdrawn |
| August 2018 | Add requirement not to change MAC address of VM (serial number of virtual Expressway is based on the address). | Clarification |
| August 2018 | Clarify VM console requirement for factory reset process. | Clarification |
| July 2018 | Republished as single variant to cover both Cisco Expressway and Cisco VCS. | Document change |
| May 2018 | Revised the Recommended Platform section to clarify that the Flashbased client may be required (version dependent). | Clarification |
| November 2017 | Updated the Recommended Platform section regarding VMware vSphere client availability. | Clarification |
| August 2017 | Added ESXi 6.5 support. | Validation complete |
| July 2017 | Removed requirement for 10 Gb NIC on large systems. Removed support for ESXi 5.0 and ESXi 5.1. Other minor documentation changes | X8.10 updates |
| January 2017 | Updated to include bug fix in relation to unsupported SSH key message in Install Wizard. Wizard now displays serial and release
                                          key for reference. Added caution regarding use of backslashes or forward slashes in Name and Location field. | X8.9.1 updates |
| December 2016 | Updated to include new secure install wizard functionality. | X8.9 updates |
| June 2016 | Decreased CPU reservation for Large OVA. Mention lack of support for VMware HA and VMware snapshots. | X8.8 updates |
| February 2016 | Updated for X8.7.1. | Upgrade prerequisite added for Hybrid Services |
| November 2015 | Updated for X8.7. ESXi 6.0 support added. Virtual hardware version change 7 to 8. |  |
| July 2015 | Republished for X8.6. |  |
| December 2014 | Republished for X8.5 |  |
| August 2014 | Removed misleading RAID 5 prerequisite for UCS. |  |
| June 2014 | Republished for X8.2 |  |
| December 2013 | Initial release of Expressway variant of this document. | X8.1 release |