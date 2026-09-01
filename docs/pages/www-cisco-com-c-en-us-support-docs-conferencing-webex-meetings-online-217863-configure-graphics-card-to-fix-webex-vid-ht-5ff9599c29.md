---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-online-217863-configure-graphics-card-to-fix-webex-vid-ht-5ff9599c29
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings-online/217863-configure-graphics-card-to-fix-webex-vid.html
retrieved_at: 2026-09-01T14:56:41.256535+00:00
---

Configure Graphics Card to Fix Webex Video Image

# Configure Graphics Card to Fix Webex Video Image

### Download Options

Updated: May 10, 2022

Document ID: 217863

Contents

## Contents

## Introduction

This document describes how to ensure that the Video Graphic Display is correct in Webex on the Windows 7 or 10 platforms.

## Problem

In a Webex, when you start your web cam, the video for all participants does not display correctly and appears cut off.

These images display the problem.

## Solution

Confirm that the Windows 7 or 10 system uses the NVIDIA graphic card:

- Navigate to Start>Run.

- In the Open field type, DxDiag, and select Ok.

- The DirectX Diagnostic Tool opens.

- Select each display tab for each display monitor.

- In each display tab, search in the Device field to ensure that the NVIDIA Graphic Card is listed.

- If so, the root cause is the Graphics Processing Unit (GPU).

- Next, improve the NVIDIA Graphics Card performance and boost the Frames per Second (FPS).

### Improve the NVIDIA Graphics and FPS

- RMB click the desktop and select the NVIDIA Control Panel from the menu.

2. In the NVIDIA Control panel, from the side menu, select "Adjust image setup with preview".

3. In that panel, select the radio button next to "Use my preference emphasize: Quality".

4. Select the Apply button.

5. The slider moves to Quality.

6. Navigate to Manage 3D window from the side menu.

7. In this tab, use the drop-down under Preferred graphics processor, and select High-performance NVIDIA processor.

8. In the field, set the feature preferences as shown in the table and then select Apply:

Feature

Set

Ambient Occlusion

Off

Anisotropic Filtering

Off

Antialiasing-Gamma correction

On

CUDA-GPUs

All

Maximum pre-rendered frames

4

Multi-display/mixed-GPU acceleration

Single display performance mode

Power management mode

Prefer maximum performance

Texture filtering-Anisotropic sample options

Off

Texture filtering-Negative LOD bias

Allow

Texture filtering-Quality

High performance

Texture filtering-Trilinear optimization

On

Threaded Optimization

Auto

9. On the left Panel, select Set PhysX Configuration.

10. Under the Select a PhysX processor drop-down menu, select GeForce GT 540M. Then select Apply.

### Revision History

1.0

10-May-2022

Initial Release

### Contributed by Cisco Engineers

Miguel Arizmendi Zambrano

CX

### This Document Applies to These Products

- WebEx Meetings

| Feature | Set |
|---|---|
| Ambient Occlusion | Off |
| Anisotropic Filtering | Off |
| Antialiasing-Gamma correction | On |
| CUDA-GPUs | All |
| Maximum pre-rendered frames | 4 |
| Multi-display/mixed-GPU acceleration | Single display performance mode |
| Power management mode | Prefer maximum performance |
| Texture filtering-Anisotropic sample options | Off |
| Texture filtering-Negative LOD bias | Allow |
| Texture filtering-Quality | High performance |
| Texture filtering-Trilinear optimization | On |
| Threaded Optimization | Auto |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-May-2022 | Initial Release |