---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-configuring-vg410--32f477508b
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/configuring-vg410-software-dsp.html
retrieved_at: 2026-08-22T01:14:14.535983+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring Software DSP

## Chapter: Configuring Software DSP

# Configuring Software DSP

The Cisco VG410 Voice Gateway chassis utilizes its built-in CPU cores to handle the digital signal processing (DSP) tasks required for software implementation.
                        This means that the functionality typically provided by a separate DSP component is instead distributed among the CPU cores
                        within the device. As a result, there is no need for a physical DSP in this device. The Cisco VG410 Voice Gateway thus supports the Software DSP functionality which effectively replaces the PVDM4.

The Software DSP is a part of the vDSP container. The Software DSP and the virtual DSP (vDSP) are thus interchangably used
                                    in this document.

## Comparison Between Software and Hardware DSP

VG with Physical DSP (motherboard or NIM)

VG410 with vDSP (use 1 physical core from CPU)

Installation

DSP is on board

The Software is installed by default, and upgrade or downgrade automatically happens when you perform an image upgrade or
                                       downgrade.

The vDSP container is installed in the bootflash. Run the voice vdsp remove command if you need to format flash.

DSP Removal

Unplug the DSP physically to remove the DSP.

Run the voice vdsp remove command. The vDSP container is removed. To reinstall, run the voice vdsp install command .

Hardware module subslot

OIR DSP by CLI

Reload the DSP firmware running on the vDSP container.

Write, erase, reload

Perform the clean up startup-config

Clean up startup-config.

The vDSP container continues to exist if the vDSP is already installed on flash.

VirtualPortGroup0 interface

Not applicable

An IOS interface connecting to the vDSP container. Move the existing service-engine configuration to the VirtualPortGoup0
                                       interface.

Read the sections in this chapter to know how to install, verify, remove, and reinstall the vDSP container.

## Installing the Software DSP Container

The Software DSP functionality is available by default when you purchase a Cisco VG410 Voice Gateway .

This functionality is pre-installed in a vDSP container through the voice vdsp install command during the manufacturing process of the Cisco VG410 Voice Gateway . The default router configuration will thus include the following configuration during manufacturing.

```
interface VirtualPortGroup0
 ip address 192.168.253.250 255.255.255.252
!
!
iox
!
app-hosting appid vdsp
 app-vnic gateway0 virtualportgroup 0 guest-interface 0
  guest-ipaddress 192.168.253.249 netmask 255.255.255.0
 app-default-gateway 192.168.253.250 guest-interface 0
 start
```

The following EEM scripts are also added during the manufacturing process through the voice vdsp install command.

```
event manager applet enableiox
 event none sync yes
 action 01 cli command "enable"
 action 10 cli command "conf t"
 action 20 cli command "iox"
 action 30 cli command "end"
event manager applet configvdsp
 event none sync yes
 action 01 cli command "enable"
 action 02 cli command "show interface VirtualPortGroup0 | inc MTU"
 action 03 string match "*bytes*" "$_cli_result"
 action 04 if $_string_result ne "1"
 action 10  cli command "conf t"
 action 11  cli command "interface VirtualPortGroup0"
 action 12  cli command "ip address 192.168.253.250 255.255.255.252"
 action 13  cli command "app-hosting appid vdsp"
 action 14  cli command "app-vnic gateway0 virtualportgroup 0 guest-interface 0"
 action 15  cli command "guest-ipaddress 192.168.253.249 netmask 255.255.255.0"
 action 16  cli command "app-default-gateway 192.168.253.250 guest-interface 0"
 action 21  cli command "start"
 action 23  cli command "end"
 action 30 end

event manager applet installvdsp
 event none sync yes
 action 01 cli command "enable"
 action 10 cli command "show app-hosting detail appid vdsp | inc Version"
 action 20 string match "*Version*" "$_cli_result"
 action 30 if $_string_result ne "1"
 action 40  cli command "app-hosting install appid vdsp package flash:vDSP/vg4x0_vdsp.tar"
 action 50 end
event manager applet noiox
 event syslog pattern "('no iox')"
 action 01 cli command "enable"
 action 10 cli command "conf t"
 action 20 cli command "no iox"
 action 30 cli command "end"
event manager applet deactivdsp
 event syslog pattern "vdsp stopped successfully"
 action 01 cli command "enable"
 action 03 file open fh bootflash:/vDSP/vg4x0_vdsp.state r
 action 04 file read fh vdspstate
 action 05 string match "$vdspstate" "upgrade"
 action 06 if $_string_result eq "1"
 action 10  cli command "app-hosting deactivate appid vdsp"
 action 20 end
event manager applet upgradevdsp
 event syslog pattern "vdsp deactivated successfully"
 action 01 cli command "enable"
 action 03 file open fh bootflash:/vDSP/vg4x0_vdsp.state r
 action 04 file read fh vdspstate
 action 05 string match "$vdspstate" "upgrade"
 action 06 if $_string_result eq "1"
 action 10  cli command "app-hosting upgrade appid vdsp package flash:vDSP/vg4x0_vdsp.tar"
 action 15  file open fh bootflash:/vDSP/vg4x0_vdsp.state w
 action 16  file write fh "done"
 action 17  file close fh
 action 20 end
```

You do not have to perform any manual installation steps to use the Software DSP functionality.

## Verifying the Software DSP Container

To verify whether the Software DSP feature is pre-installed successfully and is functional, check for the following:

Run the show platform command. When the Cisco VG410 Voice Gateway starts, the virtual DSP slot 0/1 must be in the OK state.

```
vg410# show platform
Chassis type: VG410-48FXS

Slot      Type                State                 Insert time (ago) 
--------- ------------------- --------------------- ----------------- 
0         VG410-48FXS         ok                    1d03h         
 0/0      2x1G                ok                    1d03h         
 0/1      NIM-48FXS           ok                    1d03h         
R0        VG410-48FXS         ok, active            1d03h         
F0        VG410-48FXS         ok, active            1d03h         
P0        PWR-CC1-250WAC      ok                    1d03h         
P2        VG410-FAN-1R        ok                    1d03h
```

Run the show app-hosting list command. You will see that the vDSP container is in the RUNNING state.

```
App id                                   State
---------------------------------------------------------
         vdsp                                    RUNNING
```

Run the show voice dsp group all command. The DSP state must be UP.

```
vg410# show voice dsp group all
DSP groups on slot 0/1 slot id 1
dsp 1:
  State: UP, firmware: 62.3.0
  Max signal/voice channel: 48/48
  Max credits: 720, Voice credits: 720, Video credits: 0
  num_of_sig_chnls_allocated: 48
  Transcoding channels allocated: 0
  Group: FLEX_GROUP_VOICE, complexity: FLEX
    Shared credits: 720, reserved credits: 0
    Signaling channels allocated: 48
    Voice channels allocated: 0
    Credits used (rounded-up): 0
  Slot: 0/1
  Device idx: 0
  Dsp Type: vDSP
```

Run the show voice call summary command. The voice ports should be in the FXSLS_ONHOOK state.

```
vg410# show voice call summary
PORT           CODEC     VAD VTSP STATE            VPM STATE
============== ========= === ===================== =====================
0/1/0          -          -  -                     FXSLS_ONHOOK             
0/1/1          -          -  -                     FXSLS_ONHOOK             
0/1/2          -          -  -                     FXSLS_ONHOOK             
0/1/3          -          -  -                     FXSLS_ONHOOK             
0/1/4          -          -  -                     FXSLS_ONHOOK             
0/1/5          -          -  -                     FXSLS_ONHOOK             
0/1/6          -          -  -                     FXSLS_ONHOOK             
0/1/7          -          -  -                     FXSLS_ONHOOK             
0/1/8          -          -  -                     FXSLS_ONHOOK             
0/1/9          -          -  -                     FXSLS_ONHOOK             
0/1/10         -          -  -                     FXSLS_ONHOOK             
0/1/11         -          -  -                     FXSLS_ONHOOK             
0/1/12         -          -  -                     FXSLS_ONHOOK             
0/1/13         -          -  -                     FXSLS_ONHOOK  
……
0/1/40         -          -  -                     FXSLS_ONHOOK             
0/1/41         -          -  -                     FXSLS_ONHOOK             
0/1/42         -          -  -                     FXSLS_ONHOOK             
0/1/43         -          -  -                     FXSLS_ONHOOK             
0/1/44         -          -  -                     FXSLS_ONHOOK             
0/1/45         -          -  -                     FXSLS_ONHOOK             
0/1/46         -          -  -                     FXSLS_ONHOOK             
0/1/47         -          -  -                     FXSLS_ONHOOK
```

Further, all the voice ports should be in the READY state and displayed in the console or logging buffer.

```
*Jul 24 17:58:16.409: %LINK-3-UPDOWN: Interface Foreign Exchange Station 0/1/43, changed state to ready
*Jul 24 17:58:16.409: %LINK-3-UPDOWN: Interface Foreign Exchange Station 0/1/44, changed state to ready
*Jul 24 17:58:16.409: %LINK-3-UPDOWN: Interface Foreign Exchange Station 0/1/45, changed state to ready
*Jul 24 17:58:16.409: %LINK-3-UPDOWN: Interface Foreign Exchange Station 0/1/46, changed state to ready
*Jul 24 17:58:16.409: %LINK-3-UPDOWN: Interface Foreign Exchange Station 0/1/47, changed state to ready
```

From Cisco IOS-XE 17.12.1a release, all Voice Gateway platforms must have the final voice port state to be Ready before you can begin making calls.

## Reinstalling the vDSP Container

Although the Software DSP functionality is pre-installed with your Voice Gateway, in rare scenarios, you might have to manually
                              reinstall the vDSP container. For example, when the default VirtualPortGroup0 IP address does not fit your deployment, you
                              might have to configure the vDSP container manually. In these scenarios, perform the following steps to clean up, re-install,
                              and configure the vDSP container.

The following two new commands have been introduced in Cisco VG410 Voice Gateway for the Software DSP installation and removal:

voice vdsp install : Run this command in privilege exec mode to install the software DSP in the vDSP container. As a part of the installation
                                    process for a specific vDSPware version, it utilizes an EEM script to instantiate and deploy the vDSP container. Note that
                                    the same EEM script is used during vDSPware upgrade scenarios as well.

voice vdsp remove

Whenever you perform a software upgrade for your device, the vDSP container is also automatically upgraded. You do not have
                                          manually reinstall the vDSP container after an upgrade.

### SUMMARY STEPS

- Run the voice vdsp remove command.

- There are two ways to install the vDSP container. To install the vDSP container, perform one of the following steps:

- Run the voice vdsp install command

- Use the app-hosting CLI. This method is suitable when you do not want to use the default IP address.

### DETAILED STEPS

Step 1

Run the voice vdsp remove command.

### Example:

```
vg410# voice vdsp remove
```

The EEM applets are removed and vDSP is uninstalled. Save the configuration after the vDSP is removed successfully.

To verify whether the vDSP container has been removed successfully, run the show app-hosting list command. You must see a No App Found configuration output.

```
vg410# show app-hosting list
                No App found
```

If you want to format the bootflash device, we strongly recommend that you run the voice dsp remove command beforehand.

Step 2

There are two ways to install the vDSP container. To install the vDSP container, perform one of the following steps:

- Run the voice vdsp install command

### Example:

```
vg410# voice vdsp install

vg410# show app-hosting list
App id                                   State
---------------------------------------------------------
vdsp                                     RUNNING
```

- Use the app-hosting CLI. This method is suitable when you do not want to use the default IP address.

### Example:

```
!
interface VirtualPortGroup0
ip address [ipv4 address] [netmask]
!
!

app-hosting appid vdsp
app-vnic gateway0 virtualportgroup 0 guest-interface 0
guest-ipaddress [guest ipv4 address] netmask [mask]
app-default-gateway [gateway ipv4 address] guest-interface 0
start
end
```

Reinstalls the vDSP container.

For more information, refer this link .

## Verifying the vDSP Software Version

To verify the vDSP software version, run the show voice dsp group all command. Notice the firmware version that is displayed in the configuration output.

```
vg410# show voice dsp group all
DSP groups on slot 0/1 slot id 1
dsp 1:
  State: UP, firmware: 62.3.0
  Max signal/voice channel: 48/48
  Max credits: 720, Voice credits: 720, Video credits: 0
  num_of_sig_chnls_allocated: 48
  Transcoding channels allocated: 0
  Group: FLEX_GROUP_VOICE, complexity: FLEX
    Shared credits: 720, reserved credits: 0
    Signaling channels allocated: 48
    Voice channels allocated: 0
    Credits used (rounded-up): 0
  Slot: 0/1
  Device idx: 0
  Dsp Type: vDSP
```

```
vg410# show voice dsp
 
DSP  DSP                DSPWARE CURR  BOOT                         PAK     TX/RX
TYPE NUM CH CODEC       VERSION STATE STATE   RST AI VOICEPORT TS ABORT  PACK COUNT
==== === == ======== ========== ===== ======= === == ========= == ===== ============
 
------------------------------- FLEX VOICE CARD 0/1 -------------------------------------
                           *DSP VOICE CHANNELS*

CURR STATE : (busy)inuse (b-out)busy out (bpend)busyout pending 
LEGEND     : (bad)bad    (shut)shutdown  (dpend)download pending

DSP    DSP                 DSPWARE CURR  BOOT                         PAK   TX/RX
TYPE   NUM CH CODEC        VERSION STATE STATE   RST AI VOICEPORT TS ABRT PACK COUNT
====== === == ========= ========== ===== ======= === == ========= == ==== ============
                           *DSP SIGNALING CHANNELS*
DSP    DSP                 DSPWARE CURR  BOOT                         PAK   TX/RX
TYPE   NUM CH CODEC        VERSION STATE STATE   RST AI VOICEPORT TS ABRT PACK COUNT
====== === == ========= ========== ===== ======= === == ========= == ==== ============
vDSP   001 01 {flex}        62.3.0 alloc idle      0  0 0/1/0     00    0          5/0
vDSP   001 02 {flex}        62.3.0 alloc idle      0  0 0/1/1     00    0          5/0
vDSP   001 03 {flex}        62.3.0 alloc idle      0  0 0/1/2     00    0          5/0
vDSP   001 04 {flex}        62.3.0 alloc idle      0  0 0/1/3     00    0       

or,
vg410# show platform software subslot 0/1 module firmware 
Bundled vDSPware Version 62.3.0, built on Jun  5 2023:12:11:41 from /nobackup/kctsai/62.3.0
```

To verify the vDSP version when you use the app hosting CLI, run the show app-hosting detail appid vdsp command. The following codeblock is a small snippet of the output of this command which displays the firmware version:

```
Vg410#show app-hosting detail appid vdsp
App id                 : vdsp
Owner                  : iox
State                  : RUNNING
Application
  Type                 : docker
  Name                 : vDSPware
  Version              : vdsp_version 62.3.0
  Description          : virtual DSPware
  Author               : Cisco Systems, Inc.
  Path                 : bootflash:vDSP/vg4x0_vdsp.tar
  URL Path             : 
Activated profile name : custom
```

| Note | The Software DSP is a part of the vDSP container. The Software DSP and the virtual DSP (vDSP) are thus interchangably used
                                    in this document. |
|---|---|

|  | VG with Physical DSP (motherboard or NIM) | VG410 with vDSP (use 1 physical core from CPU) |
|---|---|---|
| Installation | DSP is on board | The Software is installed by default, and upgrade or downgrade automatically happens when you perform an image upgrade or
                                       downgrade. Note The vDSP container is installed in the bootflash. Run the voice vdsp remove command if you need to format flash. | Note | The vDSP container is installed in the bootflash. Run the voice vdsp remove command if you need to format flash. |
| Note | The vDSP container is installed in the bootflash. Run the voice vdsp remove command if you need to format flash. |
| DSP Removal | Unplug the DSP physically to remove the DSP. | Run the voice vdsp remove command. The vDSP container is removed. To reinstall, run the voice vdsp install command . |
| Hardware module subslot | OIR DSP by CLI | Reload the DSP firmware running on the vDSP container. |
| Write, erase, reload | Perform the clean up startup-config | Clean up startup-config. The vDSP container continues to exist if the vDSP is already installed on flash. Run the voice vdsp remove command prior to running the write erase command. |
| VirtualPortGroup0 interface | Not applicable | An IOS interface connecting to the vDSP container. Move the existing service-engine configuration to the VirtualPortGoup0
                                       interface. |

| Note | The vDSP container is installed in the bootflash. Run the voice vdsp remove command if you need to format flash. |
|---|---|

| Note | You do not have to perform any manual installation steps to use the Software DSP functionality. |
|---|---|

| Note | From Cisco IOS-XE 17.12.1a release, all Voice Gateway platforms must have the final voice port state to be Ready before you can begin making calls. |
|---|---|

| Note | Whenever you perform a software upgrade for your device, the vDSP container is also automatically upgraded. You do not have
                                          manually reinstall the vDSP container after an upgrade. |
|---|---|

| Step 1 | Run the voice vdsp remove command. Example: vg410# voice vdsp remove The EEM applets are removed and vDSP is uninstalled. Save the configuration after the vDSP is removed successfully. Note To verify whether the vDSP container has been removed successfully, run the show app-hosting list command. You must see a No App Found configuration output. vg410# show app-hosting list
                No App found If you want to format the bootflash device, we strongly recommend that you run the voice dsp remove command beforehand. | Note | To verify whether the vDSP container has been removed successfully, run the show app-hosting list command. You must see a No App Found configuration output. vg410# show app-hosting list
                No App found |
|---|---|---|---|
| Note | To verify whether the vDSP container has been removed successfully, run the show app-hosting list command. You must see a No App Found configuration output. vg410# show app-hosting list
                No App found |
| Step 2 | There are two ways to install the vDSP container. To install the vDSP container, perform one of the following steps: Run the voice vdsp install command Example: vg410# voice vdsp install

vg410# show app-hosting list
App id                                   State
---------------------------------------------------------
vdsp                                     RUNNING Use the app-hosting CLI. This method is suitable when you do not want to use the default IP address. Example: !
interface VirtualPortGroup0
ip address [ipv4 address] [netmask]
!
!

app-hosting appid vdsp
app-vnic gateway0 virtualportgroup 0 guest-interface 0
guest-ipaddress [guest ipv4 address] netmask [mask]
app-default-gateway [gateway ipv4 address] guest-interface 0
start
end Reinstalls the vDSP container. For more information, refer this link . |

| Note | To verify whether the vDSP container has been removed successfully, run the show app-hosting list command. You must see a No App Found configuration output. vg410# show app-hosting list
                No App found |
|---|---|