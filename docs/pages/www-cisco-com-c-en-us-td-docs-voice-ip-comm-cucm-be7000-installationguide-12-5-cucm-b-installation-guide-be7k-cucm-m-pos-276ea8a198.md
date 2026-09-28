---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be7000-installationguide-12-5-cucm-b-installation-guide-be7k-cucm-m-pos-276ea8a198
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE7000/installationguide/12_5/cucm_b_installation-guide-be7k/cucm_m_post-installation-of-the-cisco-business.html
retrieved_at: 2026-08-21T01:06:58.545456+00:00
---

Installation Guide for Cisco Business Edition 7000H/M (M5), Release 12.5(CSR 12.7)

# Installation Guide for Cisco Business Edition 7000H/M (M5), Release 12.5(CSR 12.7)

Updated: December 1, 2025

Chapter: Post-Installation of the Cisco Business Edition 7000H/M

## Chapter: Post-Installation of the Cisco Business Edition 7000H/M

# Post-Installation of the Cisco Business Edition 7000H/M

## Post-Installation of the Cisco Business Edition 7000H/M

Step 1

Licensing Applications

Follow these steps to perform the first-time setup and apply licenses for your UC applications.

Step 2

Install Locales or Patches for Applications

(Optional) Install new locales for your UC applications.

### Licensing Applications

Skip this section.

Applications licensed with Product Authorization Keys (PAKs) : Applies to Cisco Unified Communications Manager 11.5 preloaded on Business Edition 7000.

1.x applications are not preloaded on appliances with virtualization software version 7.x. License logistics information for
                                                11.x applications is kept here for convenience.

Follow these steps to access each application, perform the first-time setup for some applications, and apply the licenses.

Step 1

To access the administration portal for each individual application, browse to the IP address of application. Consider the
                                          following information:

- (Optional) For Paging Server installations: Collect information about the application URL from the virtual machine console. The default first-time username and password
                                             are admin and changeMe .

- Cisco Prime Collaboration Provisioning: Browse to the IP address and use globaladmin as the username.

- Cisco Prime Collaboration Assurance and Analytics Business: Browse to the IP address and use globaladmin as the username.

Cisco Prime Collaboration Deployment:

Browse to the IP address and use the Administrator account and password you specified during installation. For more information,
                                                see the Cisco Prime Collaboration Deployment Administration Guide, Release 11.5(2) Admin Guide .

Step 2

After you purchase an application license, Cisco sends a Product Authorization Key (PAK) through mail or email. You can use
                                          the PAK to generate a license key for your specific installation using the Cisco Product License Registration portal at the www.cisco.com/go/license or you can enter the information directly in Cisco Prime License Manager.

Step 3

Apply license keys using the application administration portal. Refer to the following points for licensing information specific
                                          to whichever applications that you have installed:

- Cisco Prime Collaboration Provisioning: No license is required to use Cisco Prime Collaboration Provisioning Standard Edition.
                                             You may purchase an upgrade to Cisco Prime Collaboration Provisioning Advanced Edition if necessary.

- Cisco Prime Collaboration Assurance and Analytics : No license is required to use Cisco Prime Collaboration Assurance Standard
                                             Edition. You may purchase an upgrade to Cisco Prime Collaboration Assurance Advanced and Analytics or Advanced Edition if
                                             necessary.

- Cisco Prime Collaboration Deployment: No license is required to use Cisco Prime Collaboration Deployment Edition, as the Cisco
                                             Prime Collaboration Deployment license is entitled by the Cisco Unified Communications Manager license.

- Paging Server: No license is required to use Basic Paging Server. You may purchase an upgrade to Advanced Edition if necessary.

Cisco Prime License Manager (PLM) gets installed automatically as part of the Cisco Unified Communications Manager and Cisco
                                                            Unity Connection installation. Use only the instance that is installed with the Unified Communications Manager publisher to
                                                            manage all of your licenses. Do not use separate Prime License Manager instances to manage Unified Communications Manager
                                                            and Unity Connection licenses separately. For details, see the Cisco Prime License Manager User Guide at: http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . Alternatively a standalone instance of PLM may be installed using the files in the datastore.

### Install Locales or Patches for Applications

Complete the following tasks to install locales or patches for your application VMs.

Patches that are shipped with the appliance were current at the time of manufacture. Visit http://software.cisco.com for more
                                                   recent updates.

For additional information on locales, refer to the Phone Locale Installers wiki at: http://docwiki.cisco.com/wiki/Cucm-phone-locale-installers .

Step 1

Associate Bundled Locale or Patch ISO with Virtual Machines

Associate the locale or patch installer with the appropriate VM.

Step 2

Stop Services for Unity Connection, on page

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

Browse to the datastore and select the appropriate locale or patch ISO file.

Step 6

Click Select .

Step 7

In CD/DVD Drive 1 , check the Connect at power on check box under the Status .

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

From the Source drop-down list box, choose DVD/CD .

Step 4

Click Next .

Step 5

Select the update file that you want to install and click Next .

Step 6

After the download completes, click Next .

Step 7

After the locale or patch installs, restart the appliance:

Log in to the vSphere Client.

Right-click the VM on which you installed the locale or patchand select the Power > Restart Guest.

Log in to the VMware Embedded Host Client

Right-click the VM on which you installed the locale or patch and select the Guest OS > Restart

##### What to do next

After you install your Cisco Business Edition 7000 appliance, you can provision users, devices and configure features on the
                                    system. Refer to the following guides:

Cisco Prime Collaboration Provisioning Guide

Cisco Prime Collaboration Deployment Administration Guide

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Licensing Applications | Follow these steps to perform the first-time setup and apply licenses for your UC applications. |
| Step 2 | Install Locales or Patches for Applications | (Optional) Install new locales for your UC applications. |

| Note | 1.x applications are not preloaded on appliances with virtualization software version 7.x. License logistics information for
                                                11.x applications is kept here for convenience. |
|---|---|

| Step 1 | To access the administration portal for each individual application, browse to the IP address of application. Consider the
                                          following information: (Optional) For Paging Server installations: Collect information about the application URL from the virtual machine console. The default first-time username and password
                                             are admin and changeMe . Cisco Prime Collaboration Provisioning: Browse to the IP address and use globaladmin as the username. Cisco Prime Collaboration Assurance and Analytics Business: Browse to the IP address and use globaladmin as the username. Cisco Prime Collaboration Deployment: Browse to the IP address and use the Administrator account and password you specified during installation. For more information,
                                                see the Cisco Prime Collaboration Deployment Administration Guide, Release 11.5(2) Admin Guide . |
|---|---|
| Step 2 | After you purchase an application license, Cisco sends a Product Authorization Key (PAK) through mail or email. You can use
                                          the PAK to generate a license key for your specific installation using the Cisco Product License Registration portal at the www.cisco.com/go/license or you can enter the information directly in Cisco Prime License Manager. |
| Step 3 | Apply license keys using the application administration portal. Refer to the following points for licensing information specific
                                          to whichever applications that you have installed: Cisco Prime Collaboration Provisioning: No license is required to use Cisco Prime Collaboration Provisioning Standard Edition.
                                             You may purchase an upgrade to Cisco Prime Collaboration Provisioning Advanced Edition if necessary. Cisco Prime Collaboration Assurance and Analytics : No license is required to use Cisco Prime Collaboration Assurance Standard
                                             Edition. You may purchase an upgrade to Cisco Prime Collaboration Assurance Advanced and Analytics or Advanced Edition if
                                             necessary. Cisco Prime Collaboration Deployment: No license is required to use Cisco Prime Collaboration Deployment Edition, as the Cisco
                                             Prime Collaboration Deployment license is entitled by the Cisco Unified Communications Manager license. Paging Server: No license is required to use Basic Paging Server. You may purchase an upgrade to Advanced Edition if necessary. Unified Communications Manager, Cisco Unity Connection, and Cisco Emergency Responder: Note Cisco Prime License Manager (PLM) gets installed automatically as part of the Cisco Unified Communications Manager and Cisco
                                                            Unity Connection installation. Use only the instance that is installed with the Unified Communications Manager publisher to
                                                            manage all of your licenses. Do not use separate Prime License Manager instances to manage Unified Communications Manager
                                                            and Unity Connection licenses separately. For details, see the Cisco Prime License Manager User Guide at: http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . Alternatively a standalone instance of PLM may be installed using the files in the datastore. | Note | Cisco Prime License Manager (PLM) gets installed automatically as part of the Cisco Unified Communications Manager and Cisco
                                                            Unity Connection installation. Use only the instance that is installed with the Unified Communications Manager publisher to
                                                            manage all of your licenses. Do not use separate Prime License Manager instances to manage Unified Communications Manager
                                                            and Unity Connection licenses separately. For details, see the Cisco Prime License Manager User Guide at: http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . Alternatively a standalone instance of PLM may be installed using the files in the datastore. |
| Note | Cisco Prime License Manager (PLM) gets installed automatically as part of the Cisco Unified Communications Manager and Cisco
                                                            Unity Connection installation. Use only the instance that is installed with the Unified Communications Manager publisher to
                                                            manage all of your licenses. Do not use separate Prime License Manager instances to manage Unified Communications Manager
                                                            and Unity Connection licenses separately. For details, see the Cisco Prime License Manager User Guide at: http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . Alternatively a standalone instance of PLM may be installed using the files in the datastore. |

| Note | Cisco Prime License Manager (PLM) gets installed automatically as part of the Cisco Unified Communications Manager and Cisco
                                                            Unity Connection installation. Use only the instance that is installed with the Unified Communications Manager publisher to
                                                            manage all of your licenses. Do not use separate Prime License Manager instances to manage Unified Communications Manager
                                                            and Unity Connection licenses separately. For details, see the Cisco Prime License Manager User Guide at: http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . Alternatively a standalone instance of PLM may be installed using the files in the datastore. |
|---|---|

| Note | Patches that are shipped with the appliance were current at the time of manufacture. Visit http://software.cisco.com for more
                                                   recent updates. For additional information on locales, refer to the Phone Locale Installers wiki at: http://docwiki.cisco.com/wiki/Cucm-phone-locale-installers . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Associate Bundled Locale or Patch ISO with Virtual Machines | Associate the locale or patch installer with the appropriate VM. |
| Step 2 | Stop Services for Unity Connection, on page | If you want to install locales or patches for Cisco Unity Connection, stop the services before you install the locale or patch. |
| Step 3 | Install New Locales or Patches | Install the locale or patchon the VM. |

| Step 1 | In the VMware Embedded Host Client, select the Virtual Machine on which you want to install a new locale or patch. |
|---|---|
| Step 2 | Click Edit . |
| Step 3 | From Virtual Hardware tab, select CD/DVD Drive . |
| Step 4 | Select Datastore ISO File from CD/DVD Drive 1 drop-down list. |
| Step 5 | Browse to the datastore and select the appropriate locale or patch ISO file. |
| Step 6 | Click Select . |
| Step 7 | In CD/DVD Drive 1 , check the Connect at power on check box under the Status . |
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
| Step 3 | From the Source drop-down list box, choose DVD/CD . |
| Step 4 | Click Next . |
| Step 5 | Select the update file that you want to install and click Next . |
| Step 6 | After the download completes, click Next . |
| Step 7 | After the locale or patch installs, restart the appliance: Log in to the vSphere Client. Right-click the VM on which you installed the locale or patchand select the Power > Restart Guest. Log in to the VMware Embedded Host Client Right-click the VM on which you installed the locale or patch and select the Guest OS > Restart |