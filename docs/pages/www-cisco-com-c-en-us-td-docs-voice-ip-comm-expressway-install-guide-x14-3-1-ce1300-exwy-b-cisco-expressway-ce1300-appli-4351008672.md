---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-3-1-ce1300-exwy-b-cisco-expressway-ce1300-appli-4351008672
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-3-1/CE1300/exwy_b_cisco-expressway-ce1300-appliance-installation-guide-x1431/exwy_m_enable-encryption-on-self-encrypting.html
retrieved_at: 2026-08-16T22:10:27.418178+00:00
---

Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

# Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

Updated: October 15, 2024

Chapter: Enable Encryption on Self Encrypting Disks

## Chapter: Enable Encryption on Self Encrypting Disks

- Enable Encryption on Self Encrypting Disks

# Enable Encryption on Self Encrypting Disks

CE1300 ships with UCS-HD12T10NK9 , which are FIPS140-2 compliant Self Encrypting Disks. However, this is not shipped with encryption enabled by default.

This section describes enabling Drive Security for the individual disks and securing the RAID 1 Array. Users can apply these
                        without data loss. But, if this is done on an active machine in service, follow the instructions in the Cisco  Expressway Administrator  Guide to back up the machine configuration.

If the Expressway has option keys installed, ensure these are safely copied in the unlikely event there are issues enabling
                                    security.

Perform these steps to encrypt the hardware in the disks and to secure the array after backing up the Expressway backup (if
                        required):

Log into the CIMC, and from the top left menu icon, select Storage/Cisco 12G SAS RAID Controller with 4GB FBWC (16 drives) (MRAID) .

Select the Controller Info tab and click Enable Drive Security .

Select Local Key Management ; either enter a Security Key Identifier or Security Key or press the Suggest button to generate values and select any one of them.

Record the values in a secure location if they are required again.

Click Save the disks to enable the SED functionality.

Click the Virtual Drive Info tab.

Check the RAID 1 disk checkbox.

Select Secure Virtual Drive and confirm if you want to secure the virtual drive at the prompt.

| Note | If the Expressway has option keys installed, ensure these are safely copied in the unlikely event there are issues enabling
                                    security. |
|---|---|