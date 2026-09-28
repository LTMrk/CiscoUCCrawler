---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-d9a05f802a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0110001.html
retrieved_at: 2026-08-16T17:32:56.587336+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Install Plugins

## Chapter: Install Plugins

# Install Plugins

## Plugins Overview

Application plugins extend the functionality
                           of
                           your system.

Cisco AXL Toolkit—Lets developers create applications that create, read, update and delete provisioning objects on the publisher
                                    node. The zip file contains Java-based libraries that use SOAP over HTTP/HTTPS to send and receive AXL requests and responses.

Cisco JTAPI Client—Provides a standard programming interface for communication-enabled applications that are written in the
                                    Java programming language.

Cisco TAPI Client—Provides a standard programming interface for communication-enabled applications that are running on Microsoft
                                    Windows.

Cisco Tool for Auto-Registered Phone Support (TAPS)—Helps users remotely download preconfigured phone settings to provision
                                    their devices.

Cisco Unified CM Assistant Console—Helps assistants more effectively handle calls for their managers. The assistant console
                                    connects to the Cisco Unified Communications Manager IP Manager Assistant (IPMA) Service for login and directory services.

Cisco Unified Real-Time Monitoring Tool—Monitors device status system performance device discovery and CTI applications running
                                    on your cluster in real-time. RTMT also connects directly to devices to aid in troubleshooting.

## Install Plugins Task Flow

Perform the following tasks as needed.

Step 1

Download a Plugin

Download a plugin, and then follow installation instructions from the executable or ZIP file. After you upgrade your system,
                                          you must reinstall all plugins.

Step 2

(Optional) Update the Plugin URLs

Update the plugin URLs if your domain name server (DNS) changes. At the time of your system installation, the DNS provides
                                          the basis for the plugin URL. If the DNS changes, the URL is not automatically updated.

### Download a Plugin

Download a plugin, and then follow installation instructions from the executable or ZIP file. After you upgrade your system,
                                 you must reinstall all plugins.

#### Before you begin

Temporarily disable all intrusion detection or antivirus services that run on the server where you plan to install the plugin.

Step 1

From Cisco Unified CM Administration, choose Application > Plugins .

Step 2

Enter search criteria or leave the dialog box blank, and then click Find .

The window that appears contains more information about the application plugins.

Step 3

Click Download for the plugin that you want to download and install.

You can also right click Download and click Save As to choose a folder that is easy for you to find.

Step 4

(Optional) If your plugin is a ZIP file, unzip this file using a built-in or third-party zip program.

Step 5

Run the executable file or, if applicable, consult the readme file contained in a ZIP file.

#### What to do next

Walk through the instructions in the executable file to install the plugin.

### Update the Plugin URLs

Update the plugin URLs if your domain name server (DNS) changes. At the time of your system installation, the DNS provides
                                 the basis for the plugin URL. If the DNS changes, the URL is not automatically updated.

Step 1

From Cisco Unified CM Administration, choose Application > Plugins .

Step 2

Click Find .

Step 3

Click the plugin name that you want to update.

Step 4

In the Custom URL field, enter the updated URL for the plugin.

Step 5

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Download a Plugin | Download a plugin, and then follow installation instructions from the executable or ZIP file. After you upgrade your system,
                                          you must reinstall all plugins. |
| Step 2 | (Optional) Update the Plugin URLs | (Optional) Update the plugin URLs if your domain name server (DNS) changes. At the time of your system installation, the DNS provides
                                          the basis for the plugin URL. If the DNS changes, the URL is not automatically updated. |

| Step 1 | From Cisco Unified CM Administration, choose Application > Plugins . |
|---|---|
| Step 2 | Enter search criteria or leave the dialog box blank, and then click Find . The window that appears contains more information about the application plugins. |
| Step 3 | Click Download for the plugin that you want to download and install. You can also right click Download and click Save As to choose a folder that is easy for you to find. |
| Step 4 | (Optional) If your plugin is a ZIP file, unzip this file using a built-in or third-party zip program. |
| Step 5 | Run the executable file or, if applicable, consult the readme file contained in a ZIP file. |

| Step 1 | From Cisco Unified CM Administration, choose Application > Plugins . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Click the plugin name that you want to update. |
| Step 4 | In the Custom URL field, enter the updated URL for the plugin. |
| Step 5 | Click Save . |