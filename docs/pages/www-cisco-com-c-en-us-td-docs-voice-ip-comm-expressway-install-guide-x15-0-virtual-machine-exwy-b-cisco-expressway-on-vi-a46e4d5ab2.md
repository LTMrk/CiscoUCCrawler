---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x15-0-virtual-machine-exwy-b-cisco-expressway-on-vi-a46e4d5ab2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X15-0/virtual-machine/exwy_b_cisco-expressway-on-virtual-machine-installation-guide-x150/exwy_m_additional-information.html
retrieved_at: 2026-08-16T22:11:50.967969+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X15.0)

# Cisco Expressway on Virtual Machine Installation Guide (X15.0)

Updated: December 19, 2023

Chapter: Additional Information

## Chapter: Additional Information

# Additional Information

## Upgrading or Downgrading an Expressway VM

### Before you begin

Profile Information is Removed from Backups

From X12.6, Expressway backup files do not include system profile information
                              				(ProfileID value). This is to prevent a known issue with unexpected changes to
                              				sizing if a backup is restored across a different sized deployment. Therefore,
                              				device profiles are unaffected by backup and restore operations. Refer to Bug ID CSCvs59766 .

Step 1

Take a backup of the smaller (or the larger for downgrade) VM configuration.
                                       					Use the Expressway’s backup function, not the VMware snapshot.

Step 2

Install and deploy the new, larger (or smaller for downgrade) VM as described
                                       					in this guide.

Step 3

Restore the configuration of the (old) smaller (or the larger for downgrade) VM
                                       					onto the newly deployed VM. Note that profile information will not be included
                                       					in the backup/restore.

## Clustering for Resilience and Capacity

If you cluster Expressway VMs, we strongly advise you to use at least two physical hardware hosts. Hardware resilience requires
                              Expressway peers to run on at least two different hardware platforms.

For the current maximum supported round trip delay (RTT) and hop distances between peers, see the Cisco Expressway Cluster Creation and Maintenance Deployment Guide for your version, on the Cisco Expressway Series configuration guides page.

## Migrating from a Physical Appliance to a VM

If you are migrating from a physical appliance to a VM, the backup/restore process ( Maintenance > Backup and restore ) can be used to transfer configuration between the two installations. You will receive a warning message, but you will be
                              allowed to continue.

## Migrating the Host (use VMware VMotion)

If you need to move Expressway to a new host, you must use VMware VMotion to perform the host migration.

Before you start, there may be glitches (packet loss/jitter) in media for calls that are interworked by Expressway as the
                              VM is moved. We recommend that a VMotion move is carried out when there is minimal activity on the VM Expressway. To ensure
                              this, before you carry out the move put the Expressway VM into maintenance mode ( Maintenance > Maintenance mode ) and wait for active calls to clear.

## SAN with Fibre Interconnect is Recommended

Use of a SAN with Fibre interconnect, rather than a NAS, is recommended in order to maximize the transfer speed.

## Unsupported Features

### VMware Fault Tolerant Mode

VMware fault tolerant mode is not supported (because the Expressway uses multiple cores).

### VMware HA

We do not support VMware High Availability. We recommend clustering for resilience. If you need to move a virtual Expressway,
                              you can use VMotion.

### VMware Snapshots

We do not support VMware snapshots. We recommend you take regular backups of the Expressway instead.

### Shutdown VCS/Expressway VMs Before Upgrading ESXi Host

We recommend shutting down VCS/Expressway virtual machines (VMs) before upgrading ESXi host. Not shutting down the VMs can
                              damage or cause database (DB) instability to the VCS/Expressway servers.

## Licensing

A virtual Expressway requires licensing in the same way that an Expressway appliance requires licensing.

Do not copy the VM, as the Expressway serial number will change and the existing license keys and option keys will be invalidated.
                              If you need to move Expressway to a new host, use VMware VMotion to perform the host migration.

## Security Hardening

Information on how to deploy and operate VMware products in a secure manner is available from the VMware Security Hardening Guide s.

| Step 1 | Take a backup of the smaller (or the larger for downgrade) VM configuration.
                                       					Use the Expressway’s backup function, not the VMware snapshot. |
|---|---|
| Step 2 | Install and deploy the new, larger (or smaller for downgrade) VM as described
                                       					in this guide. |
| Step 3 | Restore the configuration of the (old) smaller (or the larger for downgrade) VM
                                       					onto the newly deployed VM. Note that profile information will not be included
                                       					in the backup/restore. |