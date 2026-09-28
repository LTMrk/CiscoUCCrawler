---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-9-rns-jvdi-b-release-notes-jvdi-129-jvdi-b-release-notes-jvdi-129-ch-6a848fcf3a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_9/rns/jvdi_b_release-notes-jvdi-129/jvdi_b_release-notes-jvdi-129_chapter_011.html
retrieved_at: 2026-08-21T12:36:53.228044+00:00
---

Release Notes for Cisco Jabber Softphone for VDI Release 12.9

# Release Notes for Cisco Jabber Softphone for VDI Release 12.9

Updated: July 8, 2020

Chapter: Performance and Behavior Notes

## Chapter: Performance and Behavior Notes

# Performance and Behavior Notes

## General Performance and Behavior Notes

### Adjust Settings for Jabra Bluetooth Devices

Most Jabra Bluetooth devices introduce a short delay in bringing up the audio path (about 1 to 3 seconds). For supported Jabra
                                 Bluetooth devices, you can eliminate the delay by changing the device settings in Jabra Direct. For more information, visit
                                 the Jabra website.

#### Before you begin

Jabra Direct  must be installed.

Open Jabra Direct.

Click the Jabra device for which you want to modify the settings.

Click Settings .

Click to expand Softphone (PC) .

From the Preferred softphone list, select Cisco Jabber .

Set Open phone line to On.

Set PC audio to Off.

Click Apply .

### Camera Hot Swap

Cisco Jabber Softphone for VDI establishes video quality at the start of a call. If you start a call with one of the supported HD cameras, and then switch
                                 to a standard-definition camera, video quality is affected. We recommend that you switch cameras between calls.

### Cisco Jabber Installed on the Thin Client

We recommend that you do not install Cisco Jabber on the thin clients. If you do install Cisco Jabber on the thin clients, ensure that users sign out of Cisco Jabber before they sign in to their hosted virtual desktops. Cisco Jabber Softphone for VDI works only with Cisco Jabber installed on the HVD.

### Echo Cancellation

Echo cancellation is enabled only for audio calls.

### GPU Passthrough

Cisco Jabber Softphone for VDI depends on the display adapter name to determine whether Cisco Jabber operates in VDI-optimized mode. Cisco Jabber Softphone for VDI supports only display adapter names that include the substring "Citrix" or "VMWare".

After you set up GPU passthrough to give the HVD direct access to the display adapter, the display adapter name doesn't include
                                 the required substring. Therefore, Cisco Jabber Softphone for VDI mistakenly identifies the deployment as non-VDI.

You can work around this issue by adding the following to the Windows registry on the HVDs:

[HKEY_CURRENT_USER\Software\Cisco Systems, Inc.\JVDI] "isVDIEnabled"="true"

After you edit the registry, restart Cisco Jabber .

### Jabra Firmware

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information,
                                 visit the Jabra website.

### Video Codec Performance

Software decoding relies heavily on the CPU. Estimated CPU usage for the Cisco JVDI Client with lower-end CPUs is as follows:

1.5Ghz, Dual core CPU—65% (55 to 75%)

1.5Ghz, Quad core CPU—35% (25 to 45%)

Use of a camera with a built-in hardware decoder reduces the load on the CPU.

| Step 1 | Open Jabra Direct. |
|---|---|
| Step 2 | Click the Jabra device for which you want to modify the settings. |
| Step 3 | Click Settings . |
| Step 4 | Click to expand Softphone (PC) . |
| Step 5 | From the Preferred softphone list, select Cisco Jabber . |
| Step 6 | Set Open phone line to On. |
| Step 7 | Set PC audio to Off. |
| Step 8 | Click Apply . |