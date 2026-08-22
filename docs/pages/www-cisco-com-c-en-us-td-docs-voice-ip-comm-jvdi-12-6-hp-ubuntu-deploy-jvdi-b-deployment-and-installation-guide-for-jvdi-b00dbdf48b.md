---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-6-hp-ubuntu-deploy-jvdi-b-deployment-and-installation-guide-for-jvdi-b00dbdf48b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_6/hp_ubuntu/deploy/jvdi_b_deployment-and-installation-guide-for-jvdi-hp-ubuntu-12-6/jvdi_b_deployment-and-installation-guide-for-jvdi-hp-ubuntu-12-6_chapter_00.html
retrieved_at: 2026-08-22T00:34:19.689657+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.6

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.6

Updated: April 9, 2019

Chapter: Cisco Jabber Softphone for VDI

## Chapter: Cisco Jabber Softphone for VDI

# Cisco Jabber Softphone for VDI

## Purpose of this Guide

This guide provides information about the following topics:

Installing and configuring Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu.

Upgrading Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu.

## About Cisco Jabber Softphone for VDI

Cisco Jabber Softphone for VDI extends the Cisco collaboration experience to virtual deployments. With a supported version of Cisco Jabber for Windows, users can send and receive phone calls on their hosted virtual desktops (HVD). The Cisco Jabber Softphone for VDI software detects the virtual environment and routes all audio and video streams directly from one endpoint to another, without
                              going through the HVD.

The applications in the Cisco Jabber Softphone for VDI family of products are:

Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu

Cisco Jabber Softphone for VDI —Unicon eLux

Cisco Jabber Softphone for VDI —Windows

### Virtual Deployments

With Cisco Jabber Softphone for VDI , thin client users can place and receive calls with their Cisco Unified Communications application ( Cisco Jabber ). Cisco Jabber Softphone for VDI consists of the Cisco JVDI Agent and the Cisco JVDI Client. To reduce latency and to enhance media quality, Cisco Jabber Softphone for VDI streams media between the endpoints without going through the hosted virtual desktops.

Cisco Jabber Softphone for VDI supports some audio and video accessories. For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Use the following flowchart to determine whether you require Cisco Jabber Softphone for VDI .

A Cisco Jabber Softphone for VDI deployment consists of the following components:

Supported HP Thin Pro or Ubuntu thin clients.

For more information about supported thin clients, see Release Notes for Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu .

Cisco JVDI Client installed on the thin client.

Windows hosted virtual desktops (HVD), in a data center.

The Virtual Machines for the HVDs can be either Citrix-, or VMware-provisioned. Citrix-provisioned virtual machines can be
                                       dedicated, or have multiple users connected over multiple remote sessions. To support multiple remote sessions, the virtual
                                       machine must be running a supported Microsoft Windows Server operating system.

Cisco Jabber installed on the HVD.

Cisco JVDI Agent installed on the HVD.

Cisco Unified Communications Manager.

### Differences in the Virtual Environment

The user experience, with Cisco Jabber Softphone for VDI and a supported Cisco Unified Communications client, is similar to the experience provided by a standard installation. However,
                                 in a virtual environment there are some differences:

The Cisco Unified Communications client detects the virtual environment at run time and starts in virtualization mode.

Cisco Jabber can control a Cisco IP Phone or use the computer to make and receive calls. The default phone selection is Use my computer for calls . After device selection, the Cisco Jabber Softphone for VDI application starts the transfer of the phone configuration data for that user. For more information, see Configuration Files .

Use the Device Selector , which is located in the Windows notification area, to manage camera and audio devices. Device management is also available
                                       from within the Cisco Unified Communications client.

By default, all calls send and receive video if both parties have video capability. The available options are:

Always start calls with video: Starts all calls as video calls, which send local video

Never start calls with video: Starts all calls as audio-only calls

This setting applies to all calls placed and received. The default setting is Always start calls with video .

You can disable video globally or on a per-device basis on the Cisco Unified Communications Manager. Navigate to System > Enterprise Phone Configuration and set Video Calling to Disabled .

Some menus and options are different in a virtual deployment. For example, Video Desktop Share (Binary Floor Control Protocol)
                                       is not available from the call window. Video Desktop Share is supported only from the IM-chat window (Remote Desktop Protocol).

If Cisco Jabber is also installed on the thin clients, ensure that everyone exits Jabber before signing in to their HVD. If Cisco Jabber is running on the local desktop, and one tries to sign in to Jabber on their HVD, the Cisco JVDI Client cannot register.
                                             Problems with accessories can also occur.

| Note | You can disable video globally or on a per-device basis on the Cisco Unified Communications Manager. Navigate to System > Enterprise Phone Configuration and set Video Calling to Disabled . |
|---|---|

| Important | If Cisco Jabber is also installed on the thin clients, ensure that everyone exits Jabber before signing in to their HVD. If Cisco Jabber is running on the local desktop, and one tries to sign in to Jabber on their HVD, the Cisco JVDI Client cannot register.
                                             Problems with accessories can also occur. |
|---|---|