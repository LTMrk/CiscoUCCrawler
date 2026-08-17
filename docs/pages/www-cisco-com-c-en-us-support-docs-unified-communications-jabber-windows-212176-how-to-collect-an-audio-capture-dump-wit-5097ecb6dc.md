---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-212176-how-to-collect-an-audio-capture-dump-wit-5097ecb6dc
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/212176-How-to-collect-an-Audio-Capture-Dump-wit.html
retrieved_at: 2026-08-17T03:32:19.887343+00:00
---

How to collect an Audio Capture Dump with Jabber for Windows

# How to collect an Audio Capture Dump with Jabber for Windows

### Download Options

Updated: April 27, 2021

Document ID: 212176

Contents

## Contents

### Introduction

This document describes how to configure a Windows PC to dump audio packets to a file location in order to help troubleshoot Jabber for Windows audio quality issues. Often, Administrators and Cisco Technical Assistance Center (TAC) engineers troubleshoot problems where Jabber users are unable to hear calling party clearly or vice versa.  Not all these issues correspond to a Jabber failure. These issues could occur because of the Windows operating system, the network interface card (NIC) or the personal computer (PC) audio drivers. The below document will help an Administrator or TAC engineer to isolate the Jabber audio quality issue.

### Steps to Perform

Step 1. Start by creating a directory on the end user's PC to save the audio dump to.

- Example:  C:\JabberAudioDump

Step 2. Set an environment variable named PME_AUDIOIO_DUMP_DIR on the user PC.

- Select Environment Variables

- Select New

For previous Windows versions:

For new Windows versions:

Step 3. Verify Jabber isn't running on the PC.

Step 4. Launch Jabber and reproduce the audio Issue

Step 5. Navigate to the directory that was created in Step 1 and verify these files exist.

- Audioiostatistics.txt

- ringbuffer_capture.txt

- ringbuffer_playout.txt

- mInFromMic.raw (local voice on jabber side)

- mInFromNetwork.raw (voice from remote side)

- mOutToSpeaker.raw (voice from remote side)

- mOutToNetwork.raw (local voice on jabber side)

Step 6. If you are working with TAC and all the files were created correctly you will want compress the directory as the .raw files can get pretty big. Upload the Jabber problem report and the audio dump files to the Case File Uploader .

### How to play back Audio in Audacity

Step 1. Launch Audacity

Step 2. Import the .raw files into Audacity

- You will be prompted for the parameters of the import, typically the default values will suffice.

Step 3. Next you can playback the audio by pressing the play button.

Note : If the audio play back is too fast or too slow you can play with the Hz level located at the bottom of the application to speed up or slow down the playback

### Revision History

1.0

29-Sep-2017

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 29-Sep-2017 | Initial Release |