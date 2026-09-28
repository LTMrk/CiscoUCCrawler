---
doc_id: www-cisco-com-c-en-us-support-docs-voice-voice-quality-30141-symptoms-html-5639b05c93
source_url: https://www.cisco.com/c/en/us/support/docs/voice/voice-quality/30141-symptoms.html
retrieved_at: 2026-08-21T07:21:08.668832+00:00
---

Recognizing and Categorizing Symptoms of Voice Quality Problems

# Recognizing and Categorizing Symptoms of Voice Quality Problems

### Download Options

Updated: September 14, 2017

Document ID: 30141

Contents

## Contents

## Introduction

The document defines a vocabulary that can be used to discuss symptoms of voice quality problems. Sound files are included to aid in the process of identification of the symptom. Also included where possible are one or more common causes (not necessarily the only ones) for the symptom that is defined.

The sound files and names of symptoms used in this document are based on common language used in Cisco Technical Support service requests, on the Technical Support website, and other sources. This document is intended to be a living resource in that the symptoms listed are expected to be revised as new problems arise and additional recordings become available.

## High Level Troubleshooting Procedure

This is the suggested high level procedure to troubleshoot voice quality problems, in conjunction with this document:

Check the sound files in this document for a symptom that matches or resembles the one that is experienced. You might wish to provide your users with a link to this document if you have not personally heard the symptom.

Access the Cisco Support Community in order to research the problem or ask questions.

If no resolution is gained by use of the Cisco Support Community, make use of the symptoms vocabulary defined in this document in order to raise a Technical Support service request.

The Technical Support engineer might ask you to make use of a Cisco utility that allows you to capture the Real Time Protocol (RTP) stream of the problem and convert it to a .wav file. This .wav file can be attached to the case and assist in the communication of the problem symptom. If you agree, an appropriate portion of the wav file can be used in this document and referenced from the TAC CC so that others can share the benefit of your experiences.

## Categorize and Define the Symptoms

These definitions were developed and applied in order to categorize the voice quality problem symptoms:

Noise

This is typically any noise on the line or in a voicemail message in addition to the voice signal. Noise typically leaves the conversation intelligible but still far from excellent. Static, hum, crosstalk, and intermittent popping tones are examples where the calling and called parties can understand each other, but with some effort. Some noises are so severe that the voice becomes unintelligible. One such example, among the samples provided in this document, is a motor sound.

Voice Distortion

This is typically any problem that affects the voice itself. This category is further divided:

Echoed Voice - Echo is where the voice signal is repeated on the line. It can be heard at either end of the call, in varying degrees and with many combinations of delay and loss within the echoed signal.

Garbled Voice - A garbled voice signal is one where the actual character of the voice is altered to a significant degree and often has a quality that fluctuates. On some occasions, the voice becomes unintelligible.

Volume Distortion - Volume distortion problems are associated with incorrect volume levels, whether constant or in flux.

Note : The categorization of the symptoms is to a large degree dependent on the severity of the symptom, perceptual factors, and cultural factors. Therefore, the placement and grouping of symptoms within categories is in many cases arguable. In addition, there can be situations where the categories overlap. For example, static on the line can cause some form of voice distortion. This is a best attempt to give some structure to these terms and define the vocabulary.

## Sample Sound Recordings

In this section, you can listen to sound recordings of the symptoms defined, along with control samples that allow you to hear the same recording without the accompanying symptom. A snippet sample of the symptom is included in order to allow for quicker download times and easier browsing. The full recording provides a longer sample so that the symptom can be properly heard.

The symptom recordings are kept as MP3 files and can be played by any sound player that supports the MP3 file format. Also, included where possible, are one or more common causes (not necessarily the only ones) for the symptom that is defined.

Note : Remember to keep your initial volume settings low. Increase volume as needed once you are comfortable with the volume levels of the recordings. If you have technical difficulties when you listen to or download these recordings, see the Common Problems Hearing Sound Files section of this document.

Note : There have been some problems discovered accessing the sounds files directly from the document when certain versions of Internet Explorer (IE) are used. See the The Sounds Do Not Play Directly from the Document section for troubleshooting information.

## Noise

This section contains sample recordings of noise problems that interfere with voice quality. Click on the links in the tables to hear a full recording, a control recording, or a snippet of the noise. A written description of the noise is also included along with possible causes.

#### Absolute Silence

Symptom - This type of silence between speech can be understood if you have ever had the experience of not knowing whether the other person is still there because there is no sound on the line.

Cause - A common cause for this problem is Voice Activity Detection (VAD) without comfort noise. In order to experience this symptom, usually the background noise is loud enough for the silence insertion to be noticeable but soft enough so that VAD is engaged.

#### Clicking

Symptom - Clicking is an external sound similar to a knock that is inserted usually at intervals.

Cause - Clock slips or other digital errors are common causes.

#### Crackling

Symptom - Crackling is an irregular form of very light static, similar to the sound a fire makes.

Cause - A common cause is poor electrical connections, in particular poor cable connections. Other causes are electrical interference and a defective power supply on the phone.

#### Crosstalk

Symptom - Crosstalk is a familiar concept where you can hear another conversation on the line. Commonly, the other parties cannot hear you. There are also forms of crosstalk where all parties can hear each other.

Cause - Wires in close proximity, where the signal of one is induced into the other, is a common cause of this problem.

#### Hissing

Symptom - Hissing is more driven and constant than static. White noise is a term often associated with strong hissing. Pink noise is a less constant hissing noise and brown noise even less constant still.

Cause - A common cause of hissing is VAD.

Symptom - Hissing with unintelligible voice is a driven white noise that overwhelms the voice, as shown in the next example. The white noise is constant.

Cause - This problem is addressed in Cisco bug ID CSCea15121 ( registered customers only) . It is heard for calls through an NM-2V/3275 that uses an AIM-VOICE-30 as a DSPfarm.

Symptom - Hissing periods often occur between segments of speech rather than throughout the whole signal.

Cause - A common cause is VAD.

#### Hum

Symptom - Hum is a buzzing noise of interference from an electromagnetic source. An example is the sound heard on a radio when a nearby mobile phone is about to be called or detecting a cell.

Cause - This problem is often caused by an electromagnetic source or telephone cables run near power lines.

#### Popping

Symptom - Popping is external sounds that are broader and less regular than clicking . This is similar to popping sounds that might be heard on a two-way radio.

Cause - A common cause of this is a Cisco Unity NIC card problem that inserts extra popping sounds.

#### Motor Sound

Symptom - A motor sound is a severe distortion or a loud, rough, beating sound.

Cause - A common cause is a fast switched cRTP bug. Cisco bug ID CSCdw73527 ( registered customers only) "no ip route-cache" provides the workaround for this problem.

#### Screeching

Cause - A common cause of screeching is a Digital Signal Processor (DSP) bug or failure.

#### Static

Symptom - Static is a granular distortion similar to bad reception on the radio.

Cause - Common causes are electrical interference or VAD.

Symptom - Severe static is an example of static that, in addition to creating background noise, affects the dial and ring tones and the voice itself. Another name for this symptom might be scratchy or gravel voice.

Cause - A common cause is A-law/Mu-law codec mismatch. For example, Compand-type A-law mistakenly added to an analog voice port.

## Voice Distortion

This section contains sample recordings of sound problems with voice distortion. Click on the links in the tables to hear a full recording, a control recording, or a snippet of the voice distortion. A written description of the distortion is also included along with possible causes.

Echoed Voice

Garbled Voice

Volume Distortion

### Echoed Voice

This section describes voice problems with an echo quality.

Listener Echo

Talker Echo

Tunnel Voice

#### Listener Echo

Symptom - Listener and talker echo sound similar, although the signal strength of listener echo might be lower. The essential difference between them is who hears the echo and where it is produced. Listener echo is the component of the talker echo that leaks through the near-end hybrid and returns again to the listener, which causes a delayed softer echo. The listener hears the talker twice.

Cause - Common causes are:

Insufficient loss of the echo signal.

Long echo tail.

Echo cancellers in the gateway adjacent to the near-end hybrid not activating.

#### Talker Echo

Symptom - Talker echo is the signal which leaks in the far-end hybrid and returns to the sender (talker). The talker hears an echo of his or her own voice.

Cause - Common causes are:

Insufficient loss of the echo signal.

Echo cancellers in the gateway adjacent to the far-end hybrid not activating.

Acoustic echo caused by the phone of the listener.

#### Tunnel Voice

Symptom - Tunnel voice is similar to talking in a tunnel or on a poor quality mobile phone car kit.

Cause - A common cause is tight echo with some loss. For example, 10 ms delay and 50 percent loss on the echo signal.

### Garbled Voice

This section describes voice problems where the voice sounds garbled.

#### Choppy Voice

Symptom - Choppy voice describes the sound when there are gaps in the voice. Syllables appear to be dropped or badly delayed in a start and stop fashion.

Note : Other terms used to describe this sound are clipped voice or broken voice. In this document, clipped voice refers to a different concept altogether as detailed in the Clipped Voice section.

Cause - Common causes are consecutive packets that are lost or excessively delayed, such that DSP predictive insertion cannot be used and silence is inserted instead. For example, delay inserted into a call through contention caused by a large data packets.

#### Clipped Voice

Symptom - Clipping is where words are cut off. It can occur at the front-end or tail-end of a word. Sometimes it occurs at the beginning of a sentence.

Note : The term clipped voice is used in a few different contexts. Sometimes it refers to the sound described in this document as choppy voice . Clipped voice is sometimes used to reference distortion caused to the signal when a sound is heavily amplified. In this document, that symptom is described as fuzzy voice .

Cause - A common cause for clipped voice is VAD.

#### Robotic Voice

Symptom - Robotic voice and synthetic voice are to some degree interchangeable. Cisco bug ID CSCdx36894 ( registered customers only) is commonly described in TAC cases as robotic voice. Therefore, this term is used in this document. However, it is really a special case of synthetic voice .

Cause - This is covered in Cisco bug ID CSCdx36894 ( registered customers only) on the 6608 and 6624 cards. The default playout delay was small enough to mean that jitter induced by Cisco Unity caused packets to be dropped and predictive insertion to occur.

#### Synthetic Voice

Symptom - The term synthetic means that the sound of the voice is artificial and with a quiver or fuzz. Predictive insertion causes this synthetic sound by replacing the sound lost when a packet is dropped with a best guess from a previous sample. Synthetic and choppy voice commonly occur together.

Cause - A common cause is single packet loss or delay beyond the bounds of the dejitter buffer playout period. DSP predictive insertion causes the synthetic quality of the voice. For example, when a call is provided insufficient bandwidth (such as G711 codec across 64Kbps).

#### Underwater Voice

Symptom - This voice problem is similar to the sound of your voice when heard underwater.

Note : In some documents, the term underwater voice means what this document refers to as synthetic voice.

Cause - This is often caused by a fast-switched cRTP bug associated with 1700 DSP firmware. Cisco bug ID CSCdy57722 ( registered customers only) "no ip route-cache" provides the workaround for this problem.

Symptom - Unintelligible underwater voice describes a distortion that makes it impossible to understand the voice. Descriptions of this sound include the sound of a cassette tape fast forwarded, a gulp sound, and a wishy-washy sound.

Cause - A common cause of this problem is G729 IETF and pre-IETF codec mismatch.

#### Quack

### Volume Distortion

This section describes voice problems where the volume is distorted.

#### Fluctuating Voice

Symptom - A fluctuating voice is when the volume of the voice increases and decreases in a wave fashion. If this occurs rapidly it can be confused with some form of garbled voice.

Cause - A common cause is a bug with IP telephone load P00303020208. Refer to Cisco bug ID CSCdy27331 ( registered customers only) . The workaround for this problem is to switch to the speaker and back.

#### Fuzzy Voice

Symptom - Fuzzy voice sounds similar to a radio turned up too loud and the voice is shaky. This might only occur at certain signal levels within the sentence. This depends on the level of gain applied.

Cause - This is often caused by too much gain on the signal, possibly introduced at one of a number of points in the network. For example, the signal can be overdriven from the PBX or high gain through the Cisco Unity Tag-switched Path (TSP) setting.

#### Loud Voice

Cause - Loud voice is usually caused by too much gain on the signal, possibly introduced at one of a number of points in the network. For example, the signal can be overdriven from the PBX or high gain through the Cisco Unity TSP setting. This is the same as fuzzy voice , but the distortion is not perceived.

#### Muffled Voice

Symptom - Muffled voice sounds similar to when you speak with your hand over your mouth.

Cause - A common cause is an overdriven signal or some other cause that eliminates or reduces signal level at frequencies inside the key range for voice (between 440 and 3500).

#### Soft Voice

Cause - Soft voice is usually caused by too much attenuation on signal possibly introduced at one of a number of points in the network (such as voice gateway when trying to reduce echo or Cisco Unity AGC settings for 3.1(3)).

#### Tinny Voice

Symptom - Tinny voice is similar to when you listen to an old-fashioned wireless broadcast.

Cause - A common cause is an overdriven signal, or some other cause that eliminates or reduces signal level at frequencies outside the key range for voice (less than 440 and greater than 3500) but important to the richness of the voice.

## Common Problems Hearing Sound Files

This section describes common problems encountered when you listen to sound files and the workarounds.

#### The Sound Player Buffers While Playing

If your sound player does not buffer the whole file before you play it and network congestion is heavy, you might notice interruptions in the audio while the player waits to receive information. These workarounds are suggested:

Some sound players allow you to specify the amount of buffering that is used. If possible, specify a greater amount of buffering prior to when you play. Choose Tools > Options > Performance and set the Network Buffering Value as required in order to change Windows Media Player settings. For example, Windows Sound Recorder should always buffer the whole file before you play it.

If you still have problems when you listen to the recordings across the Internet, right click and choose Save As in order to download the file to your hard drive and listen to it locally.

#### The Sounds Do Not Play Directly from the Document

A problem has been experienced with certain combinations and configurations of IE and the audio player that prevents the download of these sample files with a normal mouse left click. The sound player sends an error message which indicates that the file cannot be found. If you encounter this problem, use these workarounds:

For more recent versions of IE, play the file in the media bar window of a browser. IE might ask if you wish to do this. If it does, then choose Yes .

If not, then choose Media from the standard buttons menu in your browser. The WindowsMedia.com options window appears on the left side of the browser. At the bottom of the window, click on the Media down arrow and choose Settings > Play Web Media in the Bar . Now you can click on a file link and it plays from the browser.

Right-click the link, choose Save As to download to your hard disk, and play with your selected sound player.

Use Netscape.

Complete these steps in order to make Windows Media Player your default browser:

Choose Start > Settings > Control Panel > Folder Options > File Types .

Scroll to MP3, and click Advanced .

Ensure that Windows Media Player is specified and the default action is to play C:\Program Files\Windows Media Player\wmplayer.exe /Play "%L.

The Sound File Takes Too Long to Download

The largest file in this document is 900KB in size and it takes over four minutes to download on a 28kbps link. Most files are much smaller and take much less time. If you have this problem, review these workarounds:

Some smaller snippets of the sample files have been produced and are located in another column of the table. The size of these snippets ranges from approximately 60-150KB. The largest file takes about 40 seconds to download and smaller ones less than 10 seconds.

Even the largest file only takes a few seconds to download on a 1.5Mbps DSL connection.

#### The Sound is Too Soft or Loud

Remember to keep your initial volume settings low. Increase volume as needed once you are comfortable with the volume levels of the recordings.

Adjust the volume through the physical volume control on your PC or laptop and ensure it is not muted.

Adjust the volume for sound files in windows.

Choose Start > Settings > Control Panel > Sounds and Multimedia > Audio . Click Volume in the Sound Playback box and adjust the slider for Wave. Make sure it is not muted.

Adjust the volume in your sound player.

Note : If the volume of the message is low when you play back voicemail messages from Cisco Unity Express, you can issue the input gain command. Then, issue the shut and no shut commands in the voice port in order to increase the volume level. There is no way to boost the signal on the CUE voicemail ports. The only place where you can adjust the audio volume is the gain on the voice port.

```
Router# configure terminal Router(config)# voice-port XXX !--- Appropriate voice port. Router(config-voiceport)# input gain 3 !--- This increases the volume level by 3db. Router(config-voiceport)# shut Router(config-voiceport)# no shut
```

Note : Keep in mind that this affects all calls through the voice port, not just the calls to Unity Express.

#### No Sound is Playing

If you do not hear any sound when you play these recordings, use these workarounds:

Ensure the file has been downloaded. Look for any error messages from your sound player, in particular that indicate that the file cannot be found. In which case, see the The Sounds Do Not Play Directly from the Document section.

Ensure your sound is not muted.

There might be a problem with your browser or your sound player configuration. You can change browsers. If that does not work, change the sound players. Download a sound player from the Internet and use the instructions in the The Sounds Do Not Play Directly from the Document section in order to change the default player for sound files.

If you still have problems when you listen to the recordings across the Internet, right click and choose Save As to listen to it locally in order to download the file to your hard drive.

## Related Information

| Absolute Silence Periods Symptom Recording | Control Recording without the Symptom | Absolute Silence Periods Snippet Recording |
|---|---|---|

| Clicking Symptom Recording | Control Recording without the Symptom | Clicking Snippet Recording |
|---|---|---|

| Crackling Symptom Recording | Control Recording without the Symptom | Crackling Snippet Recording |
|---|---|---|

| Crosstalk Symptom Recording | Crosstalk Snippet Recording |
|---|---|

| Hissing Symptom Recording | Control Recording without the Symptom | Hissing Snippet Recording |
|---|---|---|

| Hissing with Unintelligible Voice Symptom Recording | Hissing with Unintelligible Voice Snippet Recording |
|---|---|

| Hissing Periods Symptom Recording | Hissing Periods Snippet Recording |
|---|---|

| Hum Symptom Recording | Control Recording without the Symptom | Hum Snippet Recording |
|---|---|---|

| Popping Symptom Recording | Popping Snippet Recording |
|---|---|

| Motor Sound Symptom Recording | Control Recording without the Symptom | Motor Sound Snippet Recording |
|---|---|---|

| Static Symptom Recording | Control Recording without the Symptom | Static Snippet Recording |
|---|---|---|

| Severe Static Symptom Recording | Control Recording without the Symptom | Severe Static Snippet Recording |
|---|---|---|

| Talker Echo Symptom Recording | Control Recording without the Symptom | Talker Echo Snippet Recording |
|---|---|---|

| Tunnel Voice Symptom Recording | Control Recording without the Symptom | Tunnel Voice Snippet Recording |
|---|---|---|

| Choppy Voice Symptom Recording | Control Recording without the Symptom | Choppy Voice Snippet Recording |
|---|---|---|

| Front-end Clipped Voice Symptom Recording | Control Recording without the Symptom | Front-end Clipped Voice Snippet Recording |
|---|---|---|

| Robotic Voice Symptom Recording | Robotic Voice Snippet Recording |
|---|---|

| Synthetic Voice Symptom Recording | Control Recording without the Symptom | Synthetic Voice Snippet Recording |
|---|---|---|

| Intelligible Underwater Voice Symptom Recording | Control Recording without the Symptom | Intelligible Underwater Voice Snippet Recording |
|---|---|---|

| Unintelligible Underwater Voice Symptom Recording | Control Recording without the Symptom | Unintelligible Underwater Voice Snippet Recording |
|---|---|---|

| Duck Quack Symptom Recording |
|---|

| Fluctuating Voice Symptom Recording | Fluctuating Voice Snippet Recording |
|---|---|

| Fuzzy Voice Symptom Recording | Fuzzy Voice Snippet Recording |
|---|---|

| Loud Voice Symptom Recording | Control Recording without the Symptom | Loud Voice Snippet Recording |
|---|---|---|

| Muffled Voice Symptom Recording | Control Recording without the Symptom | Muffled Voice Snippet Recording |
|---|---|---|

| Soft Voice Symptom Recording | Control Recording without the Symptom | Soft Voice Snippet Recording |
|---|---|---|

| Tinny Voice Symptom Recording | Control Recording without the Symptom | Tinny Voice Snippet Recording |
|---|---|---|