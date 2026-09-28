---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-timg-b-12xcucinttimg-b-12xcucinttimg-chapte-fa89ced936
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/timg/b_12xcucinttimg/b_12xcucinttimg_chapter_0111.html
retrieved_at: 2026-08-16T18:46:04.208691+00:00
---

TIMG Integration Guide for Cisco Unity Connection Release 12.x

# TIMG Integration Guide for Cisco Unity Connection Release 12.x

Updated: October 30, 2018

Chapter: Application Note for the Intecom Pointspan 6880 TIMG
	 Integration

## Chapter: Application Note for the Intecom Pointspan 6880 TIMG
	 Integration

# Application Note for the Intecom Pointspan 6880 TIMG
                     	 Integration

## Introduction

This is an application note for programming the Intecom
                           		Pointspan 6880 phone system for a serial SMDI integration with Cisco Unity
                           		Connection using TIMG units. For instructions on setting up the TIMG units
                           		(media gateways) and creating the integration in Unity Connection, see the Setting Up an Avaya Definity G3 In-Band TIMG
                              		  Integration with Cisco Unity Connection chapter.

## Network
                        	 Topology

Figure 8-1 shows the required Cisco Unity
                           		Connection Administration for a serial SMDI integration using TIMG units.

For more information about this integration, see Integration Description chapter.

## Requirements

The phone system met the following requirements:

The Intecom Pointspan 6880 phone system.

Software version 3.4K or later.

PDI cards model 520-1000-004.

T1 cards model 300-0289-001.

## Programming Intecom Pointspan 6880 Phone System for TIMG
                        	 Integration

The following programming instructions are
                           		provided as an example. The specific programming for your phone system may vary
                           		depending on its configuration.

Example of Programming for the Intecom Pointspan 6880 Phone System in
                              		  a TIMG Integration

```
** TRUNK GROUP DEFINITION
***...TRUNK GROUP........................17
***...TRUNK GROUP TYPE...................UNIVERSAL
TCI...TRUNK CLASS IDENTIFICATION.........LOCAL CO
UGP...USER GROUP NUMBER..................11
VTT...VOICE TRUNK TRANSFER ENABLED.......YES
CDT...TRANSFER COLLECT DIGIT TABLE #.....NONE
DCS...DEFAULT CLASS OF SERVICE...........0
CNC...NATIONAL CALLING PARTY # CONTENTS..USER GROUP
CNI...USER GROUP CALLING PARTY #.........4 = 206-555-1212
DCP...DISPLAY CALLING PARTY NUMBER.......YES
PND...PRIVATE NETWORK....................NO
ITY...INTEMAIL TYPE......................INTEMAIL TYPE II
IST...DOES InteMail SUPERVISE TRANSFERS?.NO
IML...InteMail USER ID LENGTH............5
IIN...INTEMAIL INTERFACE NUMBER..........2
VNP...InteMail NUMBER FORMAT.............DIRN
OAM...OAI ASSOCIATED MEMBER..............NO
BTG...BROADCAST TRUNK GROUP..............NO
TCM...TRAVELING CLASSMARK................NO
FTH...FAILURE THRESHOLD..................3
RDT...RESEIZE DELAY TIME............MSEC:200
CHT...TRUNK MONITOR MINIMUM HOLD TIME....0
DET...DISTANT END RELEASE TIME.......SEC:55
DCT...DATA CALLS ALLOWED.................NO
SWM...SEIZE WHEN MOS.....................NO
TCH...TRUNK CALL HANDLING................INTERNAL
NDS...DISCONNECT SUPERVISION.............YES
IGG...IGNORE GLARE.......................NO
GDT...GLARE DETECT TIME.............MSEC:100
XFT...DISTANT IBX ALLOWS FEATURE TRANSP..NO
DPT...DTMF PASSTHROUGH TIMING INDEX......NONE
......TRUNK DIRECTION....................BOTH WAYS
 *** INCOMING PARAMETERS
STY...INCOMING CALL ORIGINATION TYPE.....T1 OFF PREM.....OPX (OFF PREMISE)
TYP...INCOMING TRUNK TYPE................DIALED
ICM...INCOMING CALL MESSAGE #............17
IDS...INCOMING DIGIT SEQUENCE............DESTINATION NUMBER ONLY
IRD...RESPONSE TO DESTINATION NUMBER.....NONE
IRC...RESPONSE TO CALLING PARTY NUMBER...NONE
IIT...INCOMING INFO DIGIT TYPE/LENGTH....NONE
WPR...WHISPER MESSAGE SOURCE GROUP.......NONE
APA...TRUNK GROUP AUTHORIZATION TYPE.....NONE
PVA...PRE-VALIDATE AUTHORIZATION CODE....NO
RSC...RESET COUNT........................1
LVL...PREDEFINED LEVEL CODE..............NONE
TNE...TONE TABLE ENTRY NUMBER............NONE
MOD...INCOMING DIAL MODE.................DTMF
RGF...DTMF RECEIVER GROUP................52
TOO...TIMEOUT TO ATTENDANT...............NO
MCL...MULTIPLE CALLING ALLOWED...........NO
RAC...REUSE AUTH FOR MULT. CALLS.........NO
GAC...GROUP AUTH REQUIRED FOR TRUNKS.....NO
SAC...SYSTEM ACCESS CODE.................NONE
CWR...CALLWAIT RINGBACK..................NO
UCT...TRUNK UPDATE CDR ON TRANSFER.......ALL
CPT...CALL PROGRESSING TONES:............IBX PROVIDED
RIO...RESPONSE TO INCOMING ORIGINATION...NONE
IUG...InteMail LAMP MESSAGE USER GROUPS..ALL
NUG...INTER-USER GROUP NNP USER GROUPS...ALL
TCT...STATION CALL RESTRICTION ENABLED...NO
8NC...800 TO 4D SPEED NUMBER CONVERSION..NO
NWT...CALL PARTY NAME WAIT TIME..........NONE
 *** OUTGOING PARAMETERS
MSG...MODEM SIGNALLING...................YES
TXA...DIRECT TGRP SELECT ALLOWED.........YES
ATG...ANNOUNCEMENT TRUNK GROUP...........NO
SLC...TRUNK SELECTION....................TOP DOWN
ICA...INTER-LATA CARRIER.................10XXX
OPS...OUTGOING OUTPULSING SEQUENCE.......DESTINATION NUMBER ONLY
DIAGNOSTIC PARAMETERS: Y or N...............N
```

## Configuring the RS-232 Serial Cable

This integration followed the pinout below to configure the RS-232 serial cable using an RJ-45-to-DB-9 terminal adaptor connector.

DB-9 Pin

Serial Port Pin Definition from the Phone System

1

DCD (data carrier detect)

2

RX (transmit)

3

TX (receive)

4

DTR (data terminal ready)

5

GND (signal ground)

6

DSR (data set ready)

7

RTS (request to send)

8

CTS (clear to send)

9

(no Unity Connection)

| Caution | In programming the phone system, do not send calls to
                                    		voice messaging ports in Unity Connection that cannot answer calls (voice
                                    		messaging ports that are not set to Answer Calls). For example, if a voice
                                    		messaging port is set only to Perform Message Notification, do not send calls
                                    		to it. |
|---|---|

| DB-9 Pin | Serial Port Pin Definition from the Phone System |
|---|---|
| 1 | DCD (data carrier detect) |
| 2 | RX (transmit) |
| 3 | TX (receive) |
| 4 | DTR (data terminal ready) |
| 5 | GND (signal ground) |
| 6 | DSR (data set ready) |
| 7 | RTS (request to send) |
| 8 | CTS (clear to send) |
| 9 | (no Unity Connection) |