---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be7000-installationguide-14-cucm-b-installation-be7k-14-cucm-m-rebuildi-6b4ae09942
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE7000/installationguide/14/cucm_b_installation-be7k-14/cucm_m_rebuilding-a-business-edition-7000.html
retrieved_at: 2026-08-21T22:41:21.295721+00:00
---

Installation Guide for Cisco Business Edition 7000H/M (M5), Release 14

# Installation Guide for Cisco Business Edition 7000H/M (M5), Release 14

Updated: December 1, 2025

Chapter: Rebuilding a Business Edition 7000 Appliance

## Chapter: Rebuilding a Business Edition 7000 Appliance

# Rebuilding a Business Edition 7000 Appliance

## Rebuilding a Business Edition 7000 Appliance

Use this appendix for the following situations:

Appliance hardware replacement or RMA.

Software reinstallation caused by hardware replacement, disk reformatting, RAID rebuilds, virtualization software reinstall/upgrade
                                    or other factors.

Reapplying an embedded virtualization license key.

## Hardware and Virtualization Software Reinstall

If hardware needs to be re-provisioned, or VMware vSphere ESXi needs to be reinstalled, follow the instructions in Cisco Collaboration on Virtual Servers at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/virtual/CUCM_BK_C90D1BE9_00_cisco-collaboration-on-virtual-servers.html

BE7000M (M5) appliance corresponds to UCS C240 M5SX TRC#1

BE7000H (M5) appliance corresponds to UCS C240 M5SX TRC#2

## Reapplying Embedded Virtualization License

Check Cisco Commerce Services & Subscriptions or Cisco License Central on cisco.com to see what virtualization software options
                              your appliance ordered.

If your appliance was ordered with one of the following options, then it has an embedded virtualization license :

BE6/7K-VIRTBASP-7X

BE6/7K-VIRTENH-7X

VMW-VS6-FND-K9

VMW-VS6-CVSTD-K9

If you instead ordered the appliance with option VIRT-LIC-NONE , or you have substituted a different virtualization license, then you do not have an embedded virtualization license and
                              the instructions below do not apply.

By VMware’s design, embedded virtualization licenses work differently from general-purpose VMware vSphere ESXi licenses.

They are supported by Cisco TAC; do not contact VMware for support.

They may not be managed at myvmware.com.

They are neither VMware.com Partner Activation Codes (PAC) nor Cisco Product Authorization Keys (PAK).

Licenses are pre-activated serial numbers and do not require or support activation on myvmware.com.

They are pre-combined to fixed 2-CPU, and cannot be split or expanded through myvmware.com.

They must be applied to the appliance through the Embedded Host Client, never add these license keys to vCenter. They do not
                                    support being applied by vCenter or being added to vCenter license pools.

For more details, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html#license_comparison

Embedded virtualization licenses are master keys. If you purchased multiple appliances with the same embedded virtualization
                              license option, they will all use the same license serial number for the initial install. If you version-upgrade to a new
                              major release (e.g. 6.x to 7.x), then vCenter-supporting licenses will become a license key unique to each appliance.

You must apply the embedded virtualization license serial number as-is to an appliance using Embedded Host Client, NEVER add
                              these license keys to vCenter. Trying to apply through vCenter will either not work at all or will only work for some of the
                              appliances you purchased.

If you tried to apply for an embedded virtualization license serial number through vCenter, follow the steps below to “un-do”
                              (“host” refers to the appliance as an ESXi host):

In vCenter, make sure the host is standalone (NOT managed by vCenter): from vCenter, remove the host from inventory (important:
                                    don’t just “disconnect”).

While the host is standalone (NOT being managed by vCenter): in Embedded Host Client on the host, select & remove/delete any
                                    existing license key, then enter/assign the embedded virtualization license key.

Back to vCenter: re-add the host to inventory. It should show up with the embedded master key that was entered in step 2.

For embedded virtualization keys that support vCenter integration, note that these keys will not display normal "capacity"
                                    vs. "used". This is expected behavior.