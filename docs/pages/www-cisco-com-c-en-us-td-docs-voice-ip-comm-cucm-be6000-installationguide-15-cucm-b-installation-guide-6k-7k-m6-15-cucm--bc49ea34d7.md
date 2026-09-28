---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-15-cucm-b-installation-guide-6k-7k-m6-15-cucm--bc49ea34d7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/15/cucm_b_installation-guide-6k_7k_m6_15/cucm_m_post-installation-of-the-cisco-business.html
retrieved_at: 2026-08-21T22:40:51.451384+00:00
---

Installation Guide for Cisco Business Edition 6000 and 7000, Release 15 (M6 Appliances, preloads 14X15X-K9-16 / 14X15X-XU-16)

# Installation Guide for Cisco Business Edition 6000 and 7000, Release 15 (M6 Appliances, preloads 14X15X-K9-16 / 14X15X-XU-16)

Updated: August 4, 2025

Chapter: Post-Installation of the Cisco Business Edition 6000 or 7000

## Chapter: Post-Installation of the Cisco Business Edition 6000 or 7000

# Post-Installation of the Cisco Business Edition 6000 or 7000

## Post-Installation of the Cisco Business Edition 6000/7000 appliance

Step 1

Freshen Hardware BIOS, Firmware, and Drivers

Step 2

Licensing Applications

Follow these steps to perform the first-time setup and apply licenses for your UC applications.

Step 3

Install Locales or Patches for Applications

Install new locales for your UC applications.

### Freshen Hardware BIOS, Firmware, and Drivers

Follow these steps to freshen hardware BIOS, firmware, and drivers.

Step 1

Go to UCS Hardware and Software Compatibility at https://ucshcltool.cloudapps.cisco.com/public/ .

Step 2

Select Search By Servers .

Step 3

In Search Options:

- Server Type = C-Series

Server Model =

for BE6K, C220 M7S

for BE7K, C240 M7SX

- Processor Version = 5th-gen Intel (Emerald Rapids)

- Operating System = VMware

- Operating System Version = 7.0 or 8.0 depending on what you installed.

Then you will be advised on the latest compatible hardware updates.

### Licensing Applications

Refer to the technical documentation of each application you are using for license logistics. No application software or application
                                 licenses are included with these appliances.

### Install Locales or Patches for Applications

Complete the following tasks to install locales or patches for your application VMs.

Patches that are shipped with the appliance were current at the time of manufacture. Visit http://software.cisco.com for more
                                                   recent updates.

For additional information on locales, refer to the Phone Locale Installers wiki at: http://docwiki.cisco.com/wiki/Cucm-phone-locale-installers .

Step 1

Associate Bundled Locale or Patch ISO with Virtual Machines

Associate the locale or patch installer with the appropriate VM.

Step 2

Stop Services for Unity Connection

If you want to install locales or patches for Cisco Unity Connection, stop the services before you install the locale or patch.

Step 3

Install New Locales or Patches

Install the locale or patchon the VM.

#### Associate Bundled Locale or Patch ISO with Virtual Machines

##### Before you begin

Use this procedure to associate your locale or patch images with the appropriate application VM before starting the install
                                    process.

Step 1

In the VMware Embedded Host Client, select the Virtual Machine on which you want to install a new locale or patch.

Step 2

Click Edit .

Step 3

From Virtual Hardware tab, select CD/DVD Drive .

Step 4

Select Datastore ISO File from CD/DVD Drive 1 drop-down list.

Step 5

Browse to the datastore, and select the appropriate locale or patch ISO file.

Step 6

Click Select .

Step 7

In CD/DVD Drive 1 , check the Connect at power on check box under Status .

Step 8

Repeat this procedure for each VM for which you want to install a new locale or patch.

#### Stop Services for Unity Connection

Use this procedure if you want to install a new locale or patch for Cisco Unity Connection. You must stop services on the
                                    Unity Connection VM before you install a new locale or patch.

Step 1

Log in to Cisco Unity Connection Serviceability.

Step 2

Choose Tools > Service Management .

Step 3

Stop the following services:

- Connection Conversation Manager

- Connection Mixer

#### Install New Locales or Patches

Use this procedure to install a new locale or patch for any UC applications on your Business Edition appliance.

For Cisco Unified Communications Manager, you must install locales or patches for the publisher node and restart it before
                                                      you install it for any subscriber nodes.

You can install locales for Cisco Unified Communications Manager and Cisco Unity Connection in parallel.

Step 1

Log in to Cisco Unified Communications OS Administration.

Step 2

Navigate to Software Upgrades > Install/Upgrade . The Software Installation/Upgrade window displays.

Step 3

From the Source drop-down list, choose DVD/CD .

Step 4

Click Next .

Step 5

Select the update file that you want to install and click Next .

Step 6

After the download completes, click Next .

Step 7

After the locale or patch installs, follow these steps to restart the appliance:

Log in to the VMware Embedded Host Client.

Right-click the VM on which you installed the locale or patch and select the Guest OS > Restart .

##### What to do next

After you installed your Cisco Business Edition 6000/7000 appliance, you can provision users, devices, and configure features
                                    on the system. See the administration guides of the applications that you installed.

| Step 1 | Freshen Hardware BIOS, Firmware, and Drivers |
|---|---|
| Step 2 | Licensing Applications Follow these steps to perform the first-time setup and apply licenses for your UC applications. |
| Step 3 | Install Locales or Patches for Applications Install new locales for your UC applications. |

| Step 1 | Go to UCS Hardware and Software Compatibility at https://ucshcltool.cloudapps.cisco.com/public/ . |
|---|---|
| Step 2 | Select Search By Servers . |
| Step 3 | In Search Options: Server Type = C-Series Server Model = for BE6K, C220 M7S for BE7K, C240 M7SX Processor Version = 5th-gen Intel (Emerald Rapids) Operating System = VMware Operating System Version = 7.0 or 8.0 depending on what you installed. Then you will be advised on the latest compatible hardware updates. |

| Note | Patches that are shipped with the appliance were current at the time of manufacture. Visit http://software.cisco.com for more
                                                   recent updates. For additional information on locales, refer to the Phone Locale Installers wiki at: http://docwiki.cisco.com/wiki/Cucm-phone-locale-installers . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Associate Bundled Locale or Patch ISO with Virtual Machines | Associate the locale or patch installer with the appropriate VM. |
| Step 2 | Stop Services for Unity Connection | If you want to install locales or patches for Cisco Unity Connection, stop the services before you install the locale or patch. |
| Step 3 | Install New Locales or Patches | Install the locale or patchon the VM. |

| Step 1 | In the VMware Embedded Host Client, select the Virtual Machine on which you want to install a new locale or patch. |
|---|---|
| Step 2 | Click Edit . |
| Step 3 | From Virtual Hardware tab, select CD/DVD Drive . |
| Step 4 | Select Datastore ISO File from CD/DVD Drive 1 drop-down list. |
| Step 5 | Browse to the datastore, and select the appropriate locale or patch ISO file. |
| Step 6 | Click Select . |
| Step 7 | In CD/DVD Drive 1 , check the Connect at power on check box under Status . |
| Step 8 | Repeat this procedure for each VM for which you want to install a new locale or patch. |

| Step 1 | Log in to Cisco Unity Connection Serviceability. |
|---|---|
| Step 2 | Choose Tools > Service Management . |
| Step 3 | Stop the following services: Connection Conversation Manager Connection Mixer |

| Note | For Cisco Unified Communications Manager, you must install locales or patches for the publisher node and restart it before
                                                      you install it for any subscriber nodes. You can install locales for Cisco Unified Communications Manager and Cisco Unity Connection in parallel. |
|---|---|

| Step 1 | Log in to Cisco Unified Communications OS Administration. |
|---|---|
| Step 2 | Navigate to Software Upgrades > Install/Upgrade . The Software Installation/Upgrade window displays. |
| Step 3 | From the Source drop-down list, choose DVD/CD . |
| Step 4 | Click Next . |
| Step 5 | Select the update file that you want to install and click Next . |
| Step 6 | After the download completes, click Next . |
| Step 7 | After the locale or patch installs, follow these steps to restart the appliance: Log in to the VMware Embedded Host Client. Right-click the VM on which you installed the locale or patch and select the Guest OS > Restart . |