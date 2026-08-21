---
doc_id: www-cisco-com-c-en-us-support-docs-voice-ip-telephony-voice-over-ip-voip-64282-impedance-choice-html-547fdb85a2
source_url: https://www.cisco.com/c/en/us/support/docs/voice/ip-telephony-voice-over-ip-voip/64282-impedance-choice.html
retrieved_at: 2026-08-21T12:52:35.453233+00:00
---

Analog Voice Port Best Match Impedance Setting Choice

# Analog Voice Port Best Match Impedance Setting Choice

### Download Options

Updated: October 11, 2006

Document ID: 64282

Contents

## Contents

## Introduction

This document shows you how to perform tests to determine the best match impedance setting for an analog Foreign Exchange Office (FXO), Foreign Exchange Station (FXS), or Direct Inward Dialing (DID) voice port. The voice port connects to a voice switch such as a private branch exchange (PBX), a telephone company (telco), or central office (CO). With the judicious choice of the impedance setting for a voice port, you can improve echo cancellation (ECAN) performance. You can also mitigate any audible voice quality problems on the trunk.

## Prerequisites

### Requirements

Readers of this document should have basic knowledge of voice signaling. For more information about the voice signaling techniques, refer to Voice Network Signaling and Control .

Refer to these documents to better understand these voice interface cards (VICs):

FXO VICs— Understanding Foreign Exchange Office (FXO) Voice Interface Cards

FXS VICs— Understanding Foreign Exchange Station (FXS) Voice Interface Cards

DID VICs— Understanding Direct Inward Dial (DID) Voice Interface Cards

This document assumes that the reader already has an operational voice router configuration and that both inbound and outbound call scenarios function as expected.  This document builds on the configuration of an analog voice router that already works. The procedure in this document tunes the analog voice ports for optimal impedance matching to the telco lines.

### Components Used

Cisco IOS® Software Release 12.3(11)T and later support the testing features that this document discusses. The document discusses two different, but related, testing features. Therefore, the document mentions specific Cisco IOS Software releases only as necessary.

Voice router hardware with support includes:

Cisco 1751, 1760, 2600XM, 2691, 2800, 3640, 3660, 3700, 3800, IAD2430, and VG224 platform families

Analog FXO, FXS, and DID cards with support on these platforms

Where the document names specific hardware parts, the applicable software versions are those which support the named hardware. Refer to these documents for hardware and software compatibility matrices for analog FXO, FXS, and DID voice products:

The information in this document is based on these FXO, FXS, and DID hardware versions:

VIC-2FXO, VIC-2FXS—Refer to the Voice/Fax Network Modules for the Cisco 2600/3600/3700 Routers data sheet.

VIC-2DID—Refer to the VIC-2DID Documentation Roadmap data sheets, technical documentation, hardware installation guides, and troubleshooting guides.

VIC-4FXS/DID—Refer to the Cisco 4-Port High-Density FXS/DID Analog Voice Interface data sheet.

VIC2-2FXO, VIC2-4FXO, and VIC2-2FXS—Refer to the Cisco IP Communications Voice/Fax Network Modules for the Cisco 2600XM Series, 2691, 3600 Series, and 3700 Series Voice Gateway Routers data sheet.

NM-HDA FXO and FXS—Refer to the NM-HDA-4FXS, EM-HDA-8FXS, and EM-HDA-4FXO Documentation Roadmap data sheet.

EVM-HD FXO, FXS, and DID—Refer to the Cisco High Density Analog and Digital Extension Module for Voice and Fax data sheet.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

### Conventions

For more information on document conventions, refer to the Cisco Technical Tips Conventions .

## Problem Description

Assume the VoIP network topology that appears in this section for the purpose of this technical discussion. The diagram shows an FXO interface to the Public Switched Telephone Network (PSTN). Voice quality issues generally come up in gateways with analog FXO interfaces. The issues are often the result of the variations of the cable plant in combination with the hybrid. The hybrid performs two-wire to four-wire translation. The voice port can also be a DID interface to the PSTN because the port is also a long-haul trunk interface. However, FXO interfaces have a more dominant presence in field installations of long-haul analog voice. FXS interfaces, on the other hand, typically exhibit acceptable quality of service. FXS interfaces usually connect to short-distance premises wiring instead of miles of telco cable, as is typical of FXO interfaces.

After the installation and configuration of a voice router, users sometimes notice audio quality behavior which differs from their experience with a traditional time-division multiplexing (TDM) voice network.  Audio problem reports can include click noises, hiss, audio volume level issues, chop, one-way or no-way audio, or echo.  You can find these problems on voice routers that employ either digital voice port connectivity to a voice switch or analog voice port connectivity. But, in practice, the analog voice port connection more often causes complaints from users.  In most situations, you can eliminate audible voice quality issues if you properly understand the sources of these problems and the subsequent tuning of the packet voice network.  You can prioritize voice packets over data traffic. You can eliminate or mitigate clocking mismatches. You can adjust signal levels. And, in the case of analog voice ports, you can considerably reduce echo and mitigate other problems if you properly match impedance to the telco line conditions.

The next figure highlights some aspects of Cisco FXO voice port operation which influence the overall voice quality that a user experiences. The call in this scenario is a VoIP call between a Cisco voice router and a PSTN party.  These factors affect voice quality:

The performance of the analog front end of the VIC

Trans Hybrid Loss (THL) and receive path loss are key parameters. The performance varies with the VIC technology, port impedance configuration, cable plant, and possibly the CO line circuit.

The input gain , output attenuation , and impedance settings of the port

The echo canceller, which includes cancellation performance, double-talk detection performance, and the nonlinear processor (NLP) algorithm

The transmit level that the CO provides

A detailed discussion of each area of concern is beyond the scope of this document. However, note that at the interface between the Cisco FXO voice port and the PSTN cable plant is an impedance that attempts to match the channel as the PSTN presents it.

The cable plant that is attached to the Cisco FXO interface presents impedance that is primarily a function of cable length and cable gauge. There are secondary aspects of the cable plant which affect impedance, but these aspects are beyond the scope of this document. These aspects include the dielectric material of the cabling, temperature, twist pitch, mixed gauge lines, bridged taps, CO terminating impedance, voice frequency repeaters, and loading coils.

An RJ-11 Tip and Ring conductor pair is a very simple transmission line between your CO and the voice port on the Cisco voice router. Over the length of the transmission line, you have a model of distributed resistance, distributed capacitance, and distributed inductance. In the end, from the perspective of the voice port on the Cisco voice router, you are mating with an interface that you can model as an impedance Z composed of a real resistance R summed with a frequency-dependent complex-valued reactance X :

Z ( f ) = R + j X ( f ) = √( R 2 + X 2 ( f ) ) e j arctan( X ( f ) / R )

Note: f is the frequency in hertz.

X ( f ) is dependent on the capacitance and inductance on the line and is a function of frequency f . Other frequencies differently affect each spectral component of a voice band call. The varying nature of Z ( f ) causes this difference, with both a change in the magnitude of the signal as well as the phase.

You want to match the voice port impedance setting Z' with this aggregate transmission line impedance Z .You calculate the reflection parameter R f , which indicates how good the match is, with this equation:

R f = ( Z – Z' ) / ( Z + Z' )

The better the match, the smaller the magnitude |R f | tends toward zero. Also with a better match, less signal reflects back in either signal direction. If you have a perfect match, you have no reflected signals whatsoever. This is almost impossible to achieve over all frequencies f , so there is always some mismatch. Therefore, there is always some reflection of speech energy, which can cause some echo. Cisco analog FXO implementations have a finite selection of impedance settings. You cannot expect any setting to match the telco line impedance exactly. There can be a setting, however, which offers the best impedance match. This setting offers the best hybrid performance. The best match is a setting that provides both of these parameters:

The highest THL, which is the least amount of hybrid echo

The minimum receive loss, which is the highest receive level

Also, you can identify no best match when hybrid performance results are mixed or about the same. Under these conditions, you can use listening tests and comparisons of voice quality to choose the Cisco FXO interface impedance setting.

Refer to Understanding the Transmission Line Theory for more details on transmission line theory.

Most often, you cannot determine the best match Cisco voice port impedance setting from empirical tests.  A number of impedance settings are available under Cisco analog FXO, FXS, and DID voice ports:

```
Router(config)# voice-port 0/1/0 Router(config-voiceport)# impedance ? 600c      600 Ohms complex
600r      600 Ohms real
900c      900 Ohms complex
900r      900 ohms real
complex1  220 ohms + (820 ohms || 115nF)
complex2  270 ohms + (750 ohms || 150nF)
complex3  370 ohms + (620 ohms || 310nF)
complex4  600r, line = 270 ohms + (750 ohms || 150nF)
complex5  320 + (1050 || 230 nF), line = 12Kft
complex6  600r, line = 350 + (1000 || 210nF)

Router(config-voiceport)# impedance
```

```
Router(config)# voice-port 1/0/0 Router(config-voiceport)# impedance ? 600c      600 Ohms complex
600r      600 Ohms real
900c      900 Ohms complex
900r      900 ohms real
complex1  220 ohms + (820 ohms || 115nF)
complex2  270 ohms + (750 ohms || 150nF)
complex3  370 ohms + (620 ohms || 310nF)
complex4  600r, line = 270 ohms + (750 ohms || 150nF))
complex5  320 + (1050 || 230 nF), line = 12Kft
complex6  600r, line = 350 + (1000 || 210nF)

Router(config-voiceport)# impedance
```

The available impedance values under Cisco analog FXO, FXS, and DID voice ports are 600r , 600c , 900c , complex1 , complex2 , complex3 , complex4 , complex5 , and complex6 . When you set one of these values, you try to match the telco line as closely as you can. Choose either:

Settings which are fully resistive

An impedance which is mostly resistive

An impedance which is mostly reactive

Choose whatever seems to work best to reduce reflections on the line.

The impedance options complex4 and complex6 are compromise networks that the EIA RS-464 standard proposed.  These networks have fairly consistent performance characteristics over a large range of telco loop lengths with an output impedance of 600 ohms.  The impedance option complex5 is an optimized configuration for 12,000 feet of 26 American Wire Gauge (AWG) cabling. The complex5 option changes the output impedance to more closely resemble the line.

Use these recommendations as general guidelines:

0 to 5,000 feet—Use 600r , or match the voice port impedance setting to the impedance specification of the peer equipment.

In North America, for example, the typical impedance rating of a CO or PBX analog trunk port is 600r. But in other parts of the world, the impedance rating can be 900c.

5,000 to 10,000 feet—Use complex4 .

10,000 to 15,000 feet—Use either complex5 or complex6 .

The complex4 and complex6 settings have slightly less power transfer loss than complex5 . If there are signal-level issues to consider, choose the complex6 setting over complex5 .

## Techniques to Determine the Best Match Impedance Setting

Cisco IOS Software Release 12.3(11)T introduced tools which you can apply methodically to help ascertain the best match impedance setting for an analog voice port.  In releases earlier than Cisco IOS Software Release 12.3(11)T, empirical tests generally determined the choice of an impedance setting. These empirical tests involve the trial-and-error method, which can be frustrating and inconsistent.  The end user and an engineer from Cisco Technical Support usually performed the test on a conference bridge. They worked during a maintenance window for up to several hours.  With the new test tools in Cisco IOS Software Release 12.3(11)T and later, the end user can independently complete this voice port impedance tuning in a short amount of time. The end user only needs to engage Cisco Technical Support when problems persist.  The two test tools that this document discusses are:

```
test voice port X/Y/Z inject-tone local sweep 200 0 0
```

Note: This command should be on one line.

```
test voice port X/Y/Z thl-sweep verbose
```

(*) See the Additional Notes section of this document for important notes regarding support for the THL Tone Sweep feature on the Cisco 1751 and 1760 voice platforms.

Both test methods involve the placement of test calls through the analog FXO, FXS, or DID voice port, between a party on the IP network and another party. The test injects test tones of known signal strength and frequency out the analog port.  Then, the test inspects the return signal and tabulates the Echo Return Loss (ERL) in order to provide a channel profile of ERL versus frequency.  A higher ERL at any given frequency point is better.  Expect the channel profile to show good ERL levels at low frequencies and across the voice band. The ERL levels then start to taper off at higher frequencies.  You perform this test for each available impedance setting. The test selects the setting that provides the best channel profile as the best match impedance for that voice port and that telco line.  For both test features, the value that indicates the suitability of the channel profile is the arithmetic mean of the ERLs over all tested frequencies for a single impedance setting.  This formula illustrates:

ERL avg = (ERL 1 + ERL 2 + … + ERL N ) / N

Note: ERL i = ERL measured at the i th frequency. N is the total number of tested frequencies.

The best match impedance for the voice port is the impedance setting that yields the highest value of ERL avg .

### Original Tone Sweep Method

Cisco IOS Software Release 12.3(11)T introduced the Original Tone Sweep method of determination of the best match impedance. The method is also available in Cisco IOS Software Releases 12.3(14)T, 12.4(1), and later.  The method requires some manual work by the tester to complete the suite of tone tests.  Specifically, you must manually change the impedance setting under the voice port for each new battery of tone tests. You administratively issue the shutdown command and the no shutdown command on the voice port to have the change take effect. Then, you place a new test call from the FXO/FXS/DID voice port and execute the battery of tone tests again.  You repeat the process for each different impedance setting that the voice port allows.

These are the steps to complete:

Important: Disable ECAN under the voice port of interest.

Issue the no echo-cancel enable command.

Note: Be sure to administratively issue the shutdown command and the no shutdown command on the voice port so that the change takes effect.

Place a call over the FXS/FXO voice port of interest.

Issue the show voice call summary command to verify the connection of the call.

Note: The party out in the PSTN or on the PBX side of the voice port must be a “quiet termination”. If necessary, mute this phone so that it is not a source of audio.

Execute the tone sweep test for this voice port.

Calculate the value of ERL avg for this impedance setting.

Change the impedance setting under the voice port of interest.

Note: Be sure to administratively issue the shutdown command and the no shutdown command on the voice port so that the change takes effect.

Repeat steps 2 through 5 until you have exhausted all possible impedance settings under the voice port of interest.

Look over your collection of ERL avg to find the highest value.

The impedance setting to which this value corresponds is the best match impedance under the voice port of interest.

Here is an example of the sweep in action for two impedance settings, complex1 and complex2 :

```
CME1# configure terminal Enter configuration commands, one per line.  End with CNTL/Z.
CME1(config)# voice-port 1/0/3 CME1(config-voiceport)# no echo-cancel enable CME1(config-voiceport)# impedance complex1 CME1(config-voiceport)# shutdown CME1(config-voiceport)# no shutdown CME1(config-voiceport)# end <PLACE LIVE CALL OUT PORT 1/0/3> 

CME1#test voice port 1/0/3 inject-tone local sweep 200 0 0 

Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
104        26        -7              -33
304        19        -7              -26
504        17        -8              -25
704        19        -8              -27
904        19        -8              -27
1104       20        -8              -28
1304       21        -8              -29
1504       21        -8              -29
1704       22        -8              -30
1904       21        -8              -29
2104       22        -8              -30
2304       22        -8              -30
2504       22        -8              -30
2704       22        -8              -30
2904       22        -8              -30
3104       22        -8              -30
3304       22        -8              -30
3404       22        -8              -30 

CME1# configure terminal Enter configuration commands, one per line.  End with CNTL/Z.
CME1(config)# voice-port 1/0/3 CME1(config-voiceport)# impedance complex2 CME1(config-voiceport)# shutdown CME1(config-voiceport)# no shutdown CME1(config-voiceport)# end <PLACE LIVE CALL OUT PORT 1/0/3>

CME1#test voice port 1/0/3 inject-tone local sweep 200 0 0 

Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
104        26        -7              -33
304        19        -7              -26
504        17        -8              -25
704        19        -8              -27
904        19        -8              -27
1104       19        -8              -27
1304       20        -8              -28
1504       20        -8              -28
1704       20        -8              -28
1904       20        -8              -28
2104       20        -8              -28
2304       20        -8              -28
2504       20        -8              -28
2704       20        -8              -28
2904       20        -8              -28
3104       19        -8              -27
3304       19        -8              -27
3404       19        -8              -27
```

In this example, the ERL averages are:

For complex1—(26 + 19 + 17 + ... + 22) / 18 = 21.16

For complex2—(26 + 19 + 17 + ... + 19) / 18 = 19.77

Choose complex1 as the best match impedance because complex1 has the higher average ERL of 21.16.

This Original Tone Sweep method to determine the best match impedance setting can be cumbersome. The method is especially cumbersome in a live production environment where other parties compete for use of the same voice port that you wish to use as your reference port for the tests. With this method, you must place multiple calls over the same voice port to a “quiet termination” point out in the PSTN. You must change impedance settings manually between each set of tests. If a production call happens to seize the target voice port before you can initiate the next test sweep, the user likely hears echo. The echo occurs because you have disabled ECAN on that voice port.  Despite these drawbacks, this test method is superior to the trial-and-error method that preceded this feature.

### THL Tone Sweep Method

In order to ease the administrative burden of the Original Tone Sweep test method, Cisco IOS Software Releases 12.3(11)T6, 12.3(14)T3, and 12.4(1) introduced the THL Tone Sweep test method for the Cisco 2600XM, 2691, 2800, 3640, 3660, 3700, and 3800 Voice Router platforms. The feature was later extended to the Cisco 1751 and 1760 platforms in Cisco IOS Software Releases 12.3(14)T6, 12.4(3b), 12.4(5a), 12.4(7), 12.4(2)T3, 12.4(4)T1, and 12.4(6)T, as well as the Cisco IAD2430 and VG224 platforms in Cisco IOS Software Releases 12.4(7) and 12.4(6)T. This test feature allows the evaluation of all available impedances for a single test call to a quiet termination point out in the PSTN. You do not need to manually disable ECAN on the voice port under test. The test feature switches impedances automatically for the tester. The test feature calculates the arithmetic mean ERL and reports the mean for each channel profile at each impedance setting. Then, at the end of the test, the feature specifies the best match impedance setting. This test feature is simple to use and requires minimal supervision.

These are the steps to complete:

Place a call over the FXS/FXO/DID voice port of interest.

Issue the show voice call summary to verify the connection of the call.

Note: The party out in the PSTN or on the PBX side of the voice port must be a “quiet termination”. If necessary, mute this phone so that it is not a source of audio.

Execute the tone sweep test for this voice port.

The THL Sweep test feature automatically calculates the value of ERL avg for each impedance setting. The feature reports the setting that yields the highest value of ERL avg at the conclusion of the test.  This setting is the best match impedance setting to use under the voice port of interest.

Here is an example of the THL Sweep in action:

```
SL-C2851-MA#< NOW RUNNING THL-SWEEP >
            ^
% Invalid input detected at '^' marker. 

SL-C2851-MA#
SL-C2851-MA# test voice port 2/0/13 thl-sweep verbose Original impedance complex5. Input signal level=-48dBm 

testing 600r...... Input Signal level=-50dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        9         -3              -12
554        10        -3              -13
754        11        -3              -14
954        11        -3              -14
1154       11        -3              -14
1354       11        -3              -14
1554       11        -3              -14
1754       11        -3              -14
1954       10        -3              -13
2154       9         -3              -12
2354       8         -3              -11
2554       8         -3              -11
2754       8         -3              -11
2954       9         -3              -12
3154       8         -3              -11
3354       6         -3              -9
testing complete for 600r. ERL=9 

testing 900r...... Input Signal level=-50dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        11        -3              -14
554        12        -3              -15
754        12        -3              -15
954        12        -3              -15
1154       12        -3              -15
1354       12        -3              -15
1554       12        -3              -15
1754       11        -3              -14
1954       11        -3              -14
2154       9         -3              -12
2354       8         -3              -11
2554       7         -3              -10
2754       7         -3              -10
2954       8         -3              -11
3154       7         -3              -10
3354       5         -3              -8
testing complete for 900r. ERL=10 

testing 900c...... Input Signal level=-50dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        13        -3              -16
554        14        -3              -17
754        14        -3              -17
954        14        -3              -17
1154       14        -3              -17
1354       13        -3              -16
1554       13        -3              -16
1754       12        -3              -15
1954       11        -3              -14
2154       10        -3              -13
2354       9         -3              -12
2554       8         -3              -11
2754       8         -3              -11
2954       8         -3              -11
3154       8         -3              -11
3354       6         -3              -9
testing complete for 900c. ERL=11 

testing complex1...... Input Signal level=-49dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        14        -3              -17
554        17        -3              -20
754        19        -3              -22
954        21        -3              -24
1154       22        -3              -25
1354       22        -3              -25
1554       22        -3              -25
1754       20        -3              -23
1954       19        -3              -22
2154       17        -3              -20
2354       16        -3              -19
2554       16        -3              -19
2754       17        -3              -20
2954       18        -3              -21
3154       15        -3              -18
3354       13        -3              -16
testing complete for complex1. ERL=18 

testing complex2...... Input Signal level=-51dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        14        -3              -17
554        17        -3              -20
754        19        -3              -22
954        20        -3              -23
1154       21        -3              -24
1354       20        -3              -23
1554       20        -3              -23
1754       18        -3              -21
1954       17        -3              -20
2154       15        -3              -18
2354       14        -3              -17
2554       14        -3              -17
2754       15        -3              -18
2954       16        -3              -19
3154       13        -3              -16
3354       11        -3              -14
testing complete for complex2. ERL=17 

testing 600c...... Input Signal level=-50dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        10        -3              -13
554        10        -3              -13
754        11        -3              -14
954        11        -3              -14
1154       11        -3              -14
1354       11        -3              -14
1554       11        -3              -14
1754       11        -3              -14
1954       10        -3              -13
2154       9         -3              -12
2354       8         -3              -11
2554       8         -3              -11
2754       8         -3              -11
2954       9         -3              -12
3154       8         -3              -11
3354       6         -3              -9
testing complete for 600c. ERL=10 

testing complex4...... Input Signal level=-52dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        15        -3              -18
554        17        -3              -20
754        18        -3              -21
954        19        -3              -22
1154       19        -3              -22
1354       19        -3              -22
1554       18        -3              -21
1754       17        -3              -20
1954       15        -3              -18
2154       14        -3              -17
2354       12        -3              -15
2554       12        -3              -15
2754       12        -3              -15
2954       12        -3              -15
3154       10        -3              -13
3354       8         -3              -11
testing complete for complex4. ERL=15 

testing complex5...... Input Signal level=-51dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        32        -3              -35
554        31        -3              -34
754        28        -3              -31
954        26        -3              -29
1154       24        -3              -27
1354       23        -3              -26
1554       21        -3              -24
1754       19        -3              -22
1954       18        -3              -21
2154       16        -3              -19
2354       16        -3              -19
2554       15        -3              -18
2754       16        -3              -19
2954       16        -3              -19
3154       14        -3              -17
3354       11        -3              -14
testing complete for complex5. ERL=20 

testing complex3...... Input Signal level=-50dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        14        -3              -17
554        15        -3              -18
754        16        -3              -19
954        16        -3              -19
1154       16        -3              -19
1354       15        -3              -18
1554       14        -3              -17
1754       14        -3              -17
1954       13        -3              -16
2154       12        -3              -15
2354       11        -3              -14
2554       11        -3              -14
2754       11        -3              -14
2954       11        -3              -14
3154       10        -3              -13
3354       8         -3              -11
testing complete for complex3. ERL=13 

testing complex6...... Input Signal level=-52dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
354        19        -3              -22
554        22        -3              -25
754        24        -3              -27
954        24        -3              -27
1154       21        -3              -24
1354       20        -3              -23
1554       18        -3              -21
1754       16        -3              -19
1954       14        -3              -17
2154       12        -3              -15
2354       11        -3              -14
2554       11        -3              -14
2754       11        -3              -14
2954       11        -3              -14
3154       10        -3              -13
3354       7         -3              -10
testing complete for complex6. ERL=16

Recommended impedance(s) complex5
SL-C2851-MA#
```

The THL Tone Sweep feature is a much easier test mechanism to apply in practice.

## Additional Notes

As opposed to a trial-and-error method, the Original Tone Sweep and THL Tone Sweep test methods provide a consistent means to evaluate the worthiness of a particular impedance setting when used with the telco channel.  While you perform the tests, be aware of these points:

Keep the test methodology as consistent as possible.

If you use the Original Tone Sweep method, use the same party as the “quiet termination” in the PSTN for each set of tone sweeps at each impedance setting.  This choice keeps the path between the voice port and the termination point the same.

On voice routers with many analog FXO/FXS voice ports, you do not necessarily need to apply the tone sweep tests to every voice port.

If time is in short supply, you can test a single voice port and use the result as representative of the behavior of all the voice ports from that same telco provider.  In the majority of cases, this assumption is correct because the wiring path is most likely the same for all ports. For best results however, each voice port should be tested and tuned individually.

After selection of the best match impedance setting, perform further tuning of the voice ports as necessary in order to eliminate any residual audio problems.

Most likely, you need to tune the input gain and output attenuation settings in this case.

The best match voice port impedance setting applies to the direction from the Cisco voice router toward the PSTN.

After you set this best match voice port impedance, there is no guarantee that the ERL performance of the channel from the perspective of the PSTN toward the Cisco voice router will be symmetric and provide the highest possible ERL profile in this direction.  Gauge the overall voice quality in both directions and decide whether to tune voice port parameters further. Engage Cisco Technical Support , if necessary. In the majority of cases, the qualitative perception of voice quality is a noticeable improvement after you set the voice port impedance to the best match value. Users in the field have reported this improvement.

The Cisco 1751 and 1760 Voice Router platforms use the PVDM-256K-4, PVDM-256K-8, PVDM-256K-12, PVDM-256K-16, and PVDM-256K-20 DSP card products for voice signaling and media. These PVDM-256K-* cards use the Texas Instruments C549 DSP. Due to DSP firmware and processing power limitations when operating in Medium-Complexity (MC) Codec mode, the THL Sweep feature on the 1751/1760 Voice Router platforms only functions reliably when the DSPs are set for High-Complexity (HC) mode. By default, 2-port Voice Interface Cards (VICs) such as the VIC-2FXS, VIC2-2FXS, VIC-2FXO, VIC2-2FXO, VIC-2E/M, VIC2-2E/M, and VIC-2DID are assigned to a single C549 DSP operating in HC mode for its signaling and media resources. On the other hand, 4-port VICs such as the VIC2-4FXO and VIC-4FXS/DID are assigned to a single C549 DSP operating in MC mode to make the most optimum use of available DSP resources. As a result the THL Sweep feature on the 1751/1760 often fails when applied to the 4-port VICs, and you can potentially see this error:

```
1751GW# test voice port 2/0 thl-sweep verbose Original impedance 600r. Input signal level=-44dBm
 
Please Note: Impedance for voice port 2/0 changed to 600Real.
 
testing 600r...... Input Signal level=-44dBm
Freq (hz), ERL (dB), TX Power (dBm), RX Power (dBm)
 
ERL very low. set_impedance to 600r failed !!!.
Please Note: Impedance for voice port 2/0 changed to 600Real.
```

It is necessary to configure 4-port VICs to operate in HC mode, if sufficient DSP resources exist on the 1751/1760, in order for the THL Sweep feature to operate reliably and produce desired results. Refer to Troubleshooting Unrecognized Voice Interface Cards on Cisco 1750, 1751, and 1760 Routers for more information on DSP codec complexity settings on the Cisco 1700 Series Voice Platforms.

## Contact Cisco Technical Support

If you have completed all troubleshooting steps in this document and require further assistance or have questions, contact Cisco Technical Support . Use one of these methods:

## Related Information

### This Document Applies to These Products

- IP Telephony/Voice over IP (VoIP)

- VG Series Gateways

| FXO/DID Analog Voice Port impedance Options (Cisco IOS Software Release 12.4(1)) | FXS Analog Voice Port impedance Options (Cisco IOS Software Release 12.4(1)) |
|---|---|
| Router(config)# voice-port 0/1/0 Router(config-voiceport)# impedance ? 600c      600 Ohms complex
600r      600 Ohms real
900c      900 Ohms complex
900r      900 ohms real
complex1  220 ohms + (820 ohms \|\| 115nF)
complex2  270 ohms + (750 ohms \|\| 150nF)
complex3  370 ohms + (620 ohms \|\| 310nF)
complex4  600r, line = 270 ohms + (750 ohms \|\| 150nF)
complex5  320 + (1050 \|\| 230 nF), line = 12Kft
complex6  600r, line = 350 + (1000 \|\| 210nF)

Router(config-voiceport)# impedance | Router(config)# voice-port 1/0/0 Router(config-voiceport)# impedance ? 600c      600 Ohms complex
600r      600 Ohms real
900c      900 Ohms complex
900r      900 ohms real
complex1  220 ohms + (820 ohms \|\| 115nF)
complex2  270 ohms + (750 ohms \|\| 150nF)
complex3  370 ohms + (620 ohms \|\| 310nF)
complex4  600r, line = 270 ohms + (750 ohms \|\| 150nF))
complex5  320 + (1050 \|\| 230 nF), line = 12Kft
complex6  600r, line = 350 + (1000 \|\| 210nF)

Router(config-voiceport)# impedance |

| Test Feature | Platforms | Cisco IOS Software Availability |
|---|---|---|
| Original Tone Sweep —manual impedance changes test voice port X/Y/Z inject-tone local sweep 200 0 0 Note: This command should be on one line. | 1751, 1760, 2600XM, 2691, 2800,  3640, 3660, 3700, 3800, IAD2430, VG224 | Cisco IOS Software Release 12.3(11)T, 12.3(14)T, 12.4(1) |
| THL Tone Sweep —automatic impedance changes test voice port X/Y/Z thl-sweep verbose | 1751, 1760 (*) | Cisco IOS Software Release 12.3(14)T6, 12.4(3b), 12.4(5a), 12.4(7), 12.4(2)T3, 12.4(4)T1, 12.4(6)T |
| 2600XM, 2691, 2800, 3640, 3660, 3700, 3800 | Cisco IOS Software Release 12.3(11)T6, 12.3(14)T3, 12.4(1) |
| IAD2430, VG224 | Cisco IOS Software Release 12.4(7), 12.4(6)T |