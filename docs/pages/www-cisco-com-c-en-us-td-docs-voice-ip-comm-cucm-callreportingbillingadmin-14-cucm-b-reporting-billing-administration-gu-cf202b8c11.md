---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-14-cucm-b-reporting-billing-administration-gu-cf202b8c11
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/14/cucm_b_reporting-billing-administration-guide-14/cucm_b_reporting-and-billing-administration-guide_chapter_01001.html
retrieved_at: 2026-08-17T00:26:55.648097+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 9, 2026

Chapter: CDR Examples

## Chapter: CDR Examples

# CDR Examples

This chapter provides examples of the call detail records (CDRs) that the Unified Communications Manager Release system generates for all call types. You can use this information for post-processing activities such as generating
                        billing records and network analysis.

When you install your system, the system enables CDRs by default. You can enable or disable CDRs at any time that the system
                        is in operation. You do not need to restart Unified Communications Manager for the change to take effect. The system responds to all changes within a few seconds.

## AAC Calls

Advanced Audio Coding-Low Delay (AAC-LD) is a super-wideband codec that provides excellent speech and music quality at various
                              bit rates. The audio quality scales up with the bit rate. Two mutually incompatible RTP payload formats are supported: mpeg4-generic
                              and MP4A-LATM.

For AAC-LD (mpeg4-generic) calls, the codec type (payload capability) value 42 is used.

For AAC-LD (MP4A-LATM) calls, a separate codec type value is used for each supported bit rate. The codec type values are 43
                              (128K), 44 (64K), 45 (56K), 46 (48K), 47 (32K), and 48 (24K).

The system adds an audio bandwidth field to the CDR for AAC-LD calls.

Field Names

Definitions

origMediaCap_bandwidth

This integer field contains the audio bandwidth.

destMediaCap_bandwidth

This integer field contains the audio bandwidth.

The system populates the bandwidth fields based on the following table:

Codec

Bandwidth

G711Alaw64k

64

G711Alaw56k

56

G711mu-law64k

64

G711mu-law56k

56

G722 64k

64

G722 56k

56

G722 48k

48

G7231

7

G728

16

G729

8

G729AnnexA

8

Is11172AudioCap

0

Is13818AudioCap

0

G729AnnexB

8

G729AnnexAwAnnexB

8

GSM Full Rate

13

GSM Half Rate

7

GSM Enhanced Full Rate

13

Wideband 256K

256

Data 64k

64

Data 56k

56

G7221 32K

32

G7221 24K

24

AAC-LD (mpeg4-generic)

256

AAC-LD (MP4A-LATM) 128K

128

AAC-LD (MP4A-LATM) 64K

64

AAC-LD (MP4A-LATM) 56K

56

AAC-LD (MP4A-LATM) 48K

48

AAC-LD (MP4A-LATM) 32K

32

AAC-LD (MP4A-LATM) 24K

24

GSM

13

iLBC

15 or 13

iSAC

32

XV150 MR 729A

8

NSE VBD 729A

8

### AAC-LD (mpeg4-generic) Calls CDR Example

This example applies to a call with AAC-LD (mpeg4-generic) codec:

Field Names

AAC CDR

globalCallID_callId

121

origLegCallIdentifier

101

destLegIdentifier

102

callingPartyNumber

51234

originalCalledPartyNumber

57890

finalCalledPartyNumber

57890

lastRedirectDn

57890

origCause_Value

0

dest_CauseValue

16

origMediaCap_payloadCapability

42

origMediaCap_Bandwidth

256

destMediaCap_payloadCapability

42

destMediaCap_Bandwidth

256

## Abandoned Calls

The logging of calls with zero duration represents an optional action. If logging calls with zero duration is enabled, the
                              following actions occur:

All calls generate a CDR.

If the call is abandoned, such as when a phone is taken off hook and placed back on hook, various fields do not contain data.
                                    In this case, the originalCalledPartyNumber, finalCalledPartyNumber, the partitions that are associated with them, the destIpAddr,
                                    and the dateTimeConnect fields all remain blank. All calls that are not connected have a duration of 0 second. When a call
                                    is abandoned, the cause code contains 0 .

If the user dials a directory number and abandons the call before it connects, the FirstDest and FinalDest fields and their
                                    associated partitions contain the directory number and the partition to which the call would have been extended. The DestIp
                                    field remains blank, and the duration specifies 0 second.

You must enable the CDR Log Calls With Zero Duration Flag service parameter to log calls with zero duration. This parameter
                                          enables or disables the logging of CDRs for calls which lasted less than 1 second. See Configure CDR Service Parameters for more information.

### Examples of Abandoned Calls

Extension 2001 goes off hook, then on hook.

Field Names

CDR

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

0

callingPartyNumber

2001

originalCalledPartyNumber

finalCalledPartyNumber

lastRedirectDn

origCause_Value

16

dest_CauseValue

0

duration

0

Extension 2001 calls 2309, but 2001 hangs up (abandons) the call before it is answered.

Field Names

CDR

globalCallID_callId

2

origLegCallIdentifier

200

destLegIdentifier

201

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origCause_Value

16

dest_CauseValue

0

duration

0

## Ad Hoc Conference Linking

The advanced ad hoc conference linking feature allows you to link multiple ad hoc conferences together by adding an ad hoc
                              conference to another ad hoc conference as if it were an individual participant. You can also use the methods that are available
                              for adding individual participants to an ad hoc conference to add another conference to an ad hoc conference.

CDRs that the advanced ad hoc conference linking feature generates include a field that is called OrigConversationId. This
                              field associates the conference bridges that are involved in a linked conference. The Comment field of the CDR adds the ConfRequestorDN
                              and ConfRequestorDeviceName tags to indicate add/drop of participants of the conference by a non-controller of the conference.

The following scenarios show some of the various CDRs:

### Conference Linking Using Join

The direction of the call between the bridges depends upon which of the two calls that involve Carol is primary. The primary
                                 call survives, and the secondary call gets redirected to the conference.

Alice calls Bob, and Bob conferences in Carol (Conference 1). Dave calls Carol, and conferences in Ed (Conference 2). Two
                                 separate conferences get created. Carol exists in both conferences. At this point, CDR1, CDR2, CDR3, and CDR4 get generated.

Carol joins the two conferences. At this point, CDR5 gets generated.

When the remaining parties hang up, the remaining CDRs get generated in the order that the parties leave the conference.

#### Conference Linking Using Join Example

Field Names

CDR1: Alice -> Bob (original call)

CDR2: Bob -> Carol (consultation call)

CDR3: Dave -> Carol (original call)

CDR4: Dave -> Ed (consultation call)

CDR5: Carol -> Conference Bridge (conference call)

CDR6: Dave -> Conference Bridge (conference call)

globalCallID_callId

1

2

3

4

3

3

origLegCallIdentifier

11

13

21

23

22

22

destLegIdentifier

12

14

22

24

25

26

callingPartyNumber

1000

1001

1003

1003

1002

1003

originalCalledPartyNumber

1001

1002

1002

1004

b0029901222

b0029901222

finalCalledPartyNumber

1001

1002

1002

1004

b0029901222

b0029901222

lastRedirectDn

1001

1002

1002

1004

1003

1003

origTerminationOnBehalfOf

4

4

4

4

4

4

destTerminationOnBehalfOf

4

4

4

4

4

4

lastRedirectRedirectReason

0

0

0

0

98

98

lastRedirectRedirectOnBehalfOf

0

0

0

0

4

4

origConversationID

0

0

0

0

0

0

destConversationID

0

0

0

0

2222

2222

Comment

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

Field Names

CDR7: Dave -> Conference Bridge (conference call)

CDR8: Ed -> Conference Bridge (conference call)

CDR9: Conference Bridge (conference call)

CDR10: Alice -> Conference Bridge (conference call)

CDR11: Bob -> Conference Bridge (conference call)

globalCallID_callId

3

3

1

1

1

origLegCallIdentifier

21

24

17

11

12

destLegIdentifier

26

27

28

15

16

callingPartyNumber

1003

1004

b0029901001

1000

1001

originalCalledPartyNumber

b0029901222

b0029901222

b0029901222

b0029901001

b0029901001

finalCalledPartyNumber

b0029901222

b0029901222

b0029901222

b0029901001

b0029901001

lastRedirectDn

1003

1003

1002

1001

1001

origTerminationOnBehalfOf

0

0

0

0

0

destTerminationOnBehalfOf

0

0

0

0

0

lastRedirectRedirectReason

98

98

4

98

98

lastRedirectRedirectOnBehalfOf

4

4

10

4

4

origConversationID

0

0

0

0

0

destConversationID

2222

2222

2222

2222

2222

Comment

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

### Conference Linking Using Transfer or Direct Transfer

Alice calls Bob, and Bob conferences Carol (Conference 1). Dave calls Carol and conferences in Ed (Conference 2). Two separate
                                 conferences get created; Carol exists in both conferences. At this point, CDR1, CDR2, CDR3, and CDR4 get generated.

Carol presses the Direct Transfer (DirTrfr) softkey on the call to the first conference. Alice and Bob exist in Conference 1 while Dave and Ed are in Conference
                                 2. When the remaining parties hang up, the remaining CDRs get generated in the order in which the parties leave the conference.

The direction of the call between the bridges depends on which of the two calls that involve Carol is the primary call. The
                                             primary call side represents the calling party of the transferred call.

#### Conference Linking Using Transfer or Direct Transfer Example

Field Names

CDR1: Alice -> Bob (original call)

CDR2: Bob -> Carol (consultation call)

CDR3: Dave -> Carol (original call)

CDR4: Dave -> Carol (consultation call)

CDR5: Carol -> Conference Bridge (conference call)

CDR6: Carol -> Conference Bridge (conference call)

globalCallID_callId

1

2

3

4

1

3

origLegCallIdentifier

11

13

21

23

14

22

destLegIdentifier

12

14

22

24

17

25

callingPartyNumber

1000

1001

1003

1003

1002

1003

originalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

finalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

lastRedirectDn

1001

1002

1002

1004

1001

1003

origTerminationOnBehalfOf

4

4

4

4

10

10

destTerminationOnBehalfOf

4

4

4

4

10

10

lastRedirectRedirectReason

0

0

0

0

98

98

lastRedirectRedirectOnBehalfOf

0

0

0

0

4

4

origConversationID

0

0

0

0

0

0

destConversationID

0

0

0

0

1111

2222

Comment

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

Field Names

CDR7: Dave -> Conference Bridge (conference call)

CDR8: Ed -> Conference Bridge (conference call)

CDR9: Conference Bridge (conference call)

CDR10: Alice -> Conference Bridge (conference call)

CDR11: Bob -> Conference Bridge (conference call)

globalCallID_callId

3

3

1

1

1

origLegCallIdentifier

21

24

17

11

12

destLegIdentifier

26

27

28

15

16

callingPartyNumber

1003

1004

b0029901001

1000

1001

originalCalledPartyNumber

b0029901222

b0029901222

b0029901222

b0029901001

b0029901001

finalCalledPartyNumber

b0029901222

b0029901222

b0029901222

b0029901001

b0029901001

lastRedirectDn

1003

1003

1002

1001

1001

origTerminationOnBehalfOf

0

0

0

0

0

destTerminationOnBehalfOf

0

0

0

0

0

lastRedirectRedirectReason

98

98

4

98

98

lastRedirectRedirectOnBehalfOf

4

4

10

4

4

origConversationID

0

0

111

0

0

destConversationID

2222

2222

2222

1111

1111

Comment

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

### Linked Conference Party Removal

CDRs get generated in the order in which the parties leave a conference. When the remaining conference only has two parties,
                                 the two parties get joined directly together.

Alice calls Bob, and Bob conferences Carol (Conference 1). Dave calls Carol, and conferences in Ed (Conference 2). Two separate
                                 conferences get created; Carol participates in both conferences. At this point, CDR1, CDR2, CDR3, and CDR4 get generated.

Carol presses the Direct Transfer (DirTrfr) softkey on the call to the first conference. Alice and Bob exist in Conference1 while Dave and Ed are in Conference2.
                                 Conference 1 and Conference 2 get transferred together. Carol hangs up and leaves only two parties in Conference 1.

Because only two parties exist in the conference, Bob and the conference link get joined together. At this point, CDR7, CDR8,
                                 and CDR9 get generated. Because Bob is the controller in Conference1, Bob represents the calling party in the call between
                                 Bob and Conference2. When the remaining parties hang up, the remaining CDRs get generated in the order in which the parties
                                 leave the conference.

If Bob is not a controller and the chaining occurs before Bob joins Conference1, the call between Bob and Conference2 gets
                                             generated in the opposite direction from what is shown in the CDRs.

The direction of the call between the final two parties of a conference depends on who has been in the conference the longest.
                                 The party that has been in the conference the longest becomes the calling party.

#### Removing a Party From a Linked Conference Example

Field Names

CDR1: Alice -> Bob (original call)

CDR2: Bob -> Carol (consultation call)

CDR3: Dave -> Carol (original call)

CDR4: Dave -> Carol (consultation call)

CDR5: Carol -> Conference Bridge (conference call)

CDR6: Carol -> Conference Bridge (conference call)

globalCallID_callId

1

2

3

4

1

3

origLegCallIdentifier

11

13

21

23

14

22

destLegIdentifier

12

14

22

24

17

25

callingPartyNumber

1000

1001

1003

1003

1002

1002

originalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

finalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

lastRedirectDn

1001

1002

1002

1004

1001

1003

origTerminationOnBehalfOf

4

4

4

4

10

10

destTerminationOnBehalfOf

4

4

4

4

10

10

lastRedirectRedirectReason

0

0

0

0

98

98

lastRedirectRedirectOnBehalfOf

0

0

0

0

4

4

origConversationID

0

0

0

0

0

0

destConversationID

0

0

0

0

1111

2222

Comment

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

Field Names

CDR7: Alice -> Conference Bridge (conference call)

CDR8: Bob -> Conference Bridge (conference call)

CDR9: Conference Bridge -> Conference Bridge

CDR10: Bob -> Conference Bridge (conference call)

CDR11: Dave -> Conference Bridge (conference call)

CDR12: Ed -> Conference Bridge (conference call)

globalCallID_callId

1

1

3

3

3

3

origLegCallIdentifier

11

12

25

11

12

24

destLegIdentifier

15

16

28

15

16

27

callingPartyNumber

1001

1001

b0029901222

1000

1001

1003

originalCalledPartyNumber

b0029901001

b0029901001

b0029901001

b0029901222

b0029901222

b0029901222

finalCalledPartyNumber

b0029901001

b0029901001

b0029901001

b0029901222

b0029901222

b0029901222

lastRedirectDn

1001

1001

1002

b0029901001

1003

1003

origTerminationOnBehalfOf

16

4

4

4

0

0

destTerminationOnBehalfOf

0

4

4

4

0

0

lastRedirectRedirectReason

98

98

4

98

98

98

lastRedirectRedirectOnBehalfOf

4

4

10

4

4

4

origConversationID

0

0

2222

0

0

0

destConversationID

1111

1111

1111

2222

2222

2222

Comment

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

### Linked Conference Party (Controller) Removal

CDRs get generated in the order in which the parties leave a conference. When the remaining conference only has two parties,
                                 these two parties get joined directly together.

Alice calls Bob, and Bob conferences Carol (Conference 1). Dave calls Carol and conferences in Ed (Conference 2). Two separate
                                 conferences get created; Carol participates in both conferences. At this point, CDR1, CDR2, CDR3, and CDR4 get generated.

Carol presses the Direct Transfer (DirTrfr) softkey on the call to the first conference. Alice and Bob exist in Conference1, while Dave and Ed are in Conference2.
                                 Conference 1 and Conference 2 get transferred together. Bob hangs up which leaves only two parties that are connected to Conference1.

Because only two parties exist in Conference1, Alice and the conference link get joined directly together. At this point,
                                 CDR7, CDR8, and CDR9 get generated. Because Alice has been in the conference longer, she becomes the calling party in the
                                 call between Alice and Conference2. When the remaining parties hang up, the remaining CDRs get generated in the order in which
                                 the parties leave the conference.

The direction of a call between the final two parties of a conference depends on who has been in the conference the longest.
                                             The party that has been in the conference the longest becomes the calling party.

#### Removing a Controller From a Linked Conference Example

Field Names

CDR1: Alice -> Bob (original call)

CDR2: Bob -> Carol (consultation call)

CDR3: Dave -> Carol (original call)

CDR4: Dave -> Carol (consultation call)

CDR5: Carol -> Conference Bridge (conference call)

CDR6: Carol -> Conference Bridge (conference call)

globalCallID_callId

1

2

3

4

1

3

origLegCallIdentifier

11

13

21

23

14

22

destLegIdentifier

12

14

22

24

17

25

callingPartyNumber

1000

1001

1003

1003

1002

1002

originalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

finalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

lastRedirectDn

1001

1002

1002

1004

1001

1003

origTerminationOnBehalfOf

4

4

4

4

10

10

destTerminationOnBehalfOf

4

4

4

4

10

10

lastRedirectRedirectReason

0

0

0

0

98

98

lastRedirectRedirectOnBehalfOf

0

0

0

0

4

4

origConversationID

0

0

0

0

0

0

destConversationID

0

0

0

0

1111

2222

Comment

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

Field Names

CDR7: Conference Bridge -> Conference Bridge

CDR8: Alice -> Conference Bridge (conference call)

CDR9: Conference Bridge -> Conference Bridge

CDR10: Alice -> Conference Bridge (conference call)

CDR11: Dave -> Conference Bridge (conference call)

CDR12: Ed -> Conference Bridge (conference call)

globalCallID_callId

1

1

3

3

3

3

origLegCallIdentifier

12

11

25

11

21

24

destLegIdentifier

16

15

28

25

26

27

callingPartyNumber

1001

1000

b0029901001

1001

1003

1004

originalCalledPartyNumber

b0029901001

b0029901001

b0029901001

b0029901222

b0029901222

b0029901222

finalCalledPartyNumber

b0029901001

b0029901001

b0029901001

b0029901222

b0029901222

b0029901222

lastRedirectDn

1001

1001

1002

b0029901001

1003

1003

origTerminationOnBehalfOf

4

16

4

4

0

0

destTerminationOnBehalfOf

4

0

4

4

0

0

lastRedirectRedirectReason

98

98

4

98

98

98

lastRedirectRedirectOnBehalfOf

4

4

10

4

4

4

origConversationID

0

0

2222

0

0

0

destConversationID

1111

1111

1111

2222

2222

2222

Comment

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

### Linked Conference Removal

Alice calls Bob, and Bob conferences Carol (Conference 1). Dave calls Carol, and conferences in Ed (Conference 2). Two separate
                                 conferences get created; Carol participates in both conferences. At this point, CDR1, CDR2, CDR3, and CDR4 get generated.

Carol presses the Direct Transfer (DirTrfr) softkey on the call to the first conference. Alice and Bob exist in Conference1, while Dave and Ed are in Conference2.
                                 Conference 1 and Conference 2 get transferred together.

Bob presses the ConfList softkey and has Alice, Bob, and the conference link "Conference" shown in the list. Bob selects "Conference" and presses the Remove softkey. At this point, CDR7, CDR8, and CDR9 get generated. The conference link gets removed, which leaves two parties in
                                 the conference.

The remaining two parties get joined together. In Conference 1, Alice and Bob get joined together, and in Conference2, Dave
                                 and Ed get joined together. When the remaining parties hang up, the remaining CDRs get generated in the order in which the
                                 parties leave the conference.

#### Removing the Linked Conference Example

Field Names

CDR1: Alice -> Bob (original call)

CDR2: Bob -> Carol (consultation call)

CDR3: Dave -> Carol (original call)

CDR4: Dave -> Carol (consultation call)

CDR5: Carol -> Conference Bridge (conference call)

CDR6: Carol -> Conference Bridge (conference call)

globalCallID_callId

1

2

3

4

1

3

origLegCallIdentifier

11

13

21

23

14

22

destLegIdentifier

12

14

22

24

17

25

callingPartyNumber

1000

1001

1003

1003

1002

1002

originalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

finalCalledPartyNumber

1001

1002

1002

1004

b0029901001

b0029901222

lastRedirectDn

1001

1002

1002

1004

1001

1003

origTerminationOnBehalfOf

4

4

4

4

10

10

destTerminationOnBehalfOf

4

4

4

4

10

10

lastRedirectRedirectReason

0

0

0

0

98

98

lastRedirectRedirectOnBehalfOf

0

0

0

0

4

4

origConversationID

0

0

0

0

0

0

destConversationID

0

0

0

0

1111

2222

Comment

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

Field Names

CDR7: Conference Bridge -> Conference Bridge

CDR8: Alice -> Conference Bridge (conference call)

CDR9: Bob -> Conference Bridge

CDR10: Dave -> Conference Bridge (conference call)

CDR11: Ed -> Conference Bridge (conference call)

CDR12: Bob-> Alice

globalCallID_callId

3

1

1

3

3

3

origLegCallIdentifier

25

11

12

21

24

21

destLegIdentifier

28

15

16

26

27

24

callingPartyNumber

b0029901222

1000

1001

1003

1004

1003

originalCalledPartyNumber

b0029901001

b0029901001

b0029901001

b0029901222

b0029901222

b0029901222

finalCalledPartyNumber

b0029901001

b0029901001

b0029901001

b0029901222

b0029901222

1004

lastRedirectDn

1002

1001

1001

1003

1003

b0029901222

origTerminationOnBehalfOf

4

4

4

16

0

0

destTerminationOnBehalfOf

4

4

4

0

0

0

lastRedirectRedirectReason

4

98

98

98

98

98

lastRedirectRedirectOnBehalfOf

10

4

4

4

4

4

origConversationID

0

0

0

0

0

0

destConversationID

1111

1111

1111

2222

2222

0

Comment

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

```
ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1
```

Field Names

CDR13: Dave -> Ed

globalCallID_callId

3

origLegCallIdentifier

21

destLegIdentifier

24

callingPartyNumber

1003

originalCalledPartyNumber

b0029901222

finalCalledPartyNumber

1004

lastRedirectDn

b0029901222

origTerminationOnBehalfOf

0

destTerminationOnBehalfOf

0

lastRedirectRedirectReason

98

lastRedirectRedirectOnBehalfOf

4

origConversationID

0

destConversationID

0

Comment

```
ConfControllerDn=10
03;ConfControllerDe
viceName=SEP0003E33
3FAD1;ConfRequestor
Dn-1003;ConfRequest
orDeviceName=SEP000
3E333FAD1
```

## Agent Greeting Calls

The Agent Greeting call feature instructs Unified Communications Manager to play a prerecorded announcement to the customer automatically after successful media connection to the agent device occurs.
                              Both the agent and the customer hear the Agent Greeting.

### Example of an Agent Greeting Call

The customer (1001) calls the agent (1006).

The agent (1006) answers the call. The customer and the agent connect.

The Agent Greeting call feature instructs Unified Communications Manager to play a prerecorded announcement to the customer automatically after successful media connection to the agent device occurs.
                                    This causes an IVR (1000) to connect to the Built-In Bridge (BIB) of agent phone. Both the agent and the customer hear the
                                    Agent Greeting.

The customer-agent call ends. A CDR gets generated for the customer-to-agent call. A CDR gets generated for the IVR (1000)
                                    to BIB of agent phone.

The CDR for the IVR to agent BIB specifies the comment AgentGreeting=<agentCI> . The OnBehalfOf field is set to 33 and redirectReason code is set to 752 for Agent Greeting call.

Field Names

Call From Customer to Agent

Call From IVR to Agent BIB

globalCallID_callId

270001

270002

origLegCallIdentifier

22980857

22980861

destLegIdentifier

22980858

22980862

callingPartyNumber

1001

1000

originalCalledPartyNumber

1006

b00121104001

finalCalledPartyNumber

1006

b00121104001

origCallTerminationOnBehalfOf

12

0

destCallTerminationOnBehalfOf

0

33

origCalledPartyRedirectOnBehalfOf

0

33

lastRedirectRedirectOnBehalfOf

0

33

origCalledPartyRedirectReason

0

752

lastRedirectRedirectReason

0

752

destConversationId

0

22980858

joinOnBehalfOf

33

comment

AgentGreeting=22980858

duration

23

9

## Barge

When a shared line uses the barge feature, the origCalledPartyNumber , finalCalledPartyNumber, and lastRedirectDn represent the conference bridge number 'b00. . .'. The redirect and join OnBehalfOf fields reflect a value of Barge = 15,
                              and the redirect reason fields specify Barge = 114.

### Barge Examples

40003 calls 40001, and 40001 answers. Shared line 40001' on another phone presses the Barge softkey. All the parties get conferenced
                                    together; then, 40003 hangs up.

Both CDRs have the same globalCallID_callId, and the conversationID field links back to the CI (call Identifier) of the barged
                                                call.

Field Names

Original Call CDR

Barge Call CDR

globalCallID_callId

7

7

origLegCallIdentifier

16777230

16777232

destLegIdentifier

16777231

16777235

callingPartyNumber

40003

40003

origCalledPartyNumber

40001

b001501001

finalCalledPartyNumber

40001

b001501001

lastRedirectDn

40001

b001501001

origCause_Value

16

0

dest_CauseValue

0

0

origCalledPartyRedirectReason

0

114

lastRedirectRedirectReason

0

114

origCalledPartyRedirectOnBehalfOf

15

lastRedirectRedirectOnBehalfOf

15

joinOnBehalfOf

15

destConversationID

0

16777231

40003 calls 40001, and 40001 answers. Shared line 40001' on another phone presses the Barge softkey. All the parties get conferenced
                                    together; then, 40001 hangs up.

Both CDRs have the same globalCallID_callId, and the conversationID field links back to the CI (call Identifier) of the barged
                                                call.

Field Names

Original Call CDR

Barge Call 1 CDR

Final Call 2 CDR

globalCallID_callId

origLegCallIdentifier

16777236

16777238

16777236

destLegIdentifier

16777237

16777241

16777238

callingPartyNumber

40003

40001

40003

origCalledPartyNumber

40001

b001501001

40001

finalCalledPartyNumber

40001

b001501001

40001

lastRedirectDn

40001

b001501001

40001

origCause_Value

0

393216

16

dest_CauseValue

16

393216

0

origCalledPartyRedirectReason

0

114

0

lastRedirectRedirectReason

0

114

0

origTerminationOnBehalfOf

15

12

destTerminationOnBehalfOf

12

15

12

lastRedirectRedirectOnBehalfOf

15

joinOnBehalfOf

15

destConversationID

0

16777237

0

40003 calls 40001, and 40001 answers. Shared line 40001' on another phone presses the Barge softkey. All the parties get conferenced
                                    together; then, 40001' (another shared line and phone) presses the Barge softkey. 40003 hangs up first.

All CDRs have the same globalCallID_callId , and the conversationID field links back to the CI (call Identifier) of the barged call.

Field Names

Original Call CDR

Barge Call 1 CDR

Final Call 2 CDR

globalCallID_callId

origLegCallIdentifier

16777249

16777251

16777255

destLegIdentifier

16777250

16777254

16777258

callingPartyNumber

40003

40001

40001

origCalledPartyNumber

40001

b001501001

b001501001

finalCalledPartyNumber

40001

b001501001

b001501001

lastRedirectDn

40001

b001501001

b001501001

origCause_Value

16

0

0

dest_CauseValue

0

0

0

origCalledPartyRedirectReason

0

114

114

lastRedirectRedirectReason

0

114

114

origTerminationOnBehalfOf

12

15

15

destTerminationOnBehalfOf

origRedirectRedirectOnBehalfOf

15

15

lastRedirectRedirectOnBehalfOf

15

15

joinOnBehalfOf

15

15

destConversationID

0

16777250

16777251

## Call Monitoring

The system generates CDRs for the Call Monitoring feature by using existing CDR fields.

The monitoring calls have one-way media. The media fields stay empty for one side of the call for one-way media CDRs.

The destConversationID field of the Call Monitoring CDR matches the agent call leg identifier in the CDR of the call that is monitored and links
                              together the Call Monitoring CDR and the CDR of the monitored call.

### Call Monitoring Examples

The customer (9728134987) calls the agent (30000), and the agent answers. The supervisor (40003) monitors the call. The destConversationID
                                    from the monitoring call matches the destLegIdentifier of the monitored call.

Field Names

Monitored Call CDR

Monitoring Call CDR

globalCallID_callId

7

10

origLegCallIdentifier

16777230

16777232

destLegIdentifier

16777231

16777235

callingPartyNumber

9728134987

40003

originalCalledPartyNumber

30000

b001501001

finalCalledPartyNumber

30000

b001501001

lastRedirectDn

30000

b001501001

origCause_Value

16

0

dest_CauseValue

0

0

origCalledPartyRedirectReason

0

370

lastRedirectRedirectOnBehalfOf

0

370

origCalledPartyRedirectOnBehalfOf

28

lastRedirectRedirectOnBehalfOf

28

destConversationID

0

16777231

The agent (30000) calls the customer (9728134987), and the customer answers. The supervisor (40003) monitors the call. The
                                    destConversationID from the monitoring call matches the origLegCallIdentifier of the monitored call.

Field Names

Monitored Call CDR

Monitoring Call CDR

globalCallID_callId

71

101

origLegCallIdentifier

16777299

16777932

destLegIdentifier

16777300

16777235

callingPartyNumber

30000

40003

originalCalledPartyNumber

9728134987

b001501002

finalCalledPartyNumber

9728134987

b001501002

lastRedirectDn

9728134987

b001501002

origCause_Value

16

0

dest_CauseValue

0

0

origCalledPartyRedirectReason

0

370

lastRedirectRedirectOnBehalfOf

0

370

origCalledPartyRedirectOnBehalfOf

28

lastRedirectRedirectOnBehalfOf

28

destConversationID

0

16777299

## Call Park

Call Park generates two CDRs, one for the original call that gets parked and another for the call that gets picked up or reverted.
                              These CDRs will have the same globalCallID_callId.

### Call Park Pickup

When the call is parked, the call gets split. The original call generates a CDR. The origTerminationOnBehalfOf and destTerminationOnBehalfOf fields get set to Call Park = 3 for this CDR.

When the parked call gets retrieved, the user goes off hook and enters the park code. This call joins with the parked call.
                                 Because the user who is picking up the call gets joined with the parked call, the system treats the user as the originator
                                 of the call, and the parked user gets treated as the destination. This means that the callingPartyNumber field of the call contains the directory number of the user who is picking up the call, and the originalCalledNumber and finalCalledNumber fields contain the directory number of the parked user. The lastRedirectDn field contains the park code that is used to pick up the call. The lastRedirectRedirectReason field specifies Call Park Pickup = 8. The lastRedirectRedirectOnBehalfOf field should specify Call Park = 3.

#### Call Park Pickup CDR Example

50003 calls 50002; 50002 presses the Park softkey. 50001 picks up the parked call by dialing the park code (44444).

Field Names

Original Call That Is Parked CDR

Parked Call That Is Picked Up CDR

globalCallID_callId

1

1

origLegCallIdentifier

20863957

20863961

destLegIdentifier

20863958

20863957

callingPartyNumber

50003

50001

originalCalledPartyNumber

50002

50003

finalCalledPartyNumber

50002

50003

lastRedirectDn

50002

44444

origCause_Value

393216

0

dest_CauseValue

393216

16

origCalledPartyRedirectReason

0

0

lastRedirectRedirectReason

0

8

origCalledPartyRedirectOnBehalfOf

0

0

lastRedirectRedirectOnBehalfOf

0

3

origTerminationOnBehalfOf

3

0

destTerminationOnBehalfOf

3

12

joinOnBehalfOf

0

3

duration

4

60

### Call Park Reversion

When a call is parked and not picked up, the call park reversion timer expires and redirects the call to the called party.
                                 In this case, the system generates two CDRs. The first CDR appears the same as the preceding Call Park Pickup scenario, but
                                 the second CDR differs slightly. When the Call Pickup Reversion timer expires, the call gets redirected to the called party.

When the call is parked, the call gets split. This action generates a CDR for the original call. The origTerminationOnBehalfOf and destTerminationOnBehalfOf fields get set to Call Park = 3 for this CDR, the same as the Call Park Pickup scenario.

When the Call Park Reversion timer expires, the call gets redirected to the called party. The origCalledPartyRedirectOnBehalfOf and lastRedirectRedirectOnBehalfOf fields specify Call Park = 3. The origCalledPartyRedirectReason field specifies Call Park = 7, and the lastRedirectRedirectReason field specifies Call Park Reversion = 11.

#### Call Park Reversion CDR Example

Call Park Reversion Example – 50003 calls 50002; 50002 presses the Park softkey. Nobody picks up the parked call; the parked call reverts to 50002, and
                                       50002 answers.

Field Names

Original Call That Is Parked CDR

Reverted Call CDR

globalCallID_callId

2

2

origLegCallIdentifier

20863963

20863963

destLegIdentifier

20863964

20863967

callingPartyNumber

50003

50003

originalCalledPartyNumber

50002

50002

finalCalledPartyNumber

50002

50002

lastRedirectDn

50002

50002

origCause_Value

393216

0

dest_CauseValue

393216

16

origCalledPartyRedirectReason

0

7

lastRedirectRedirectReason

0

11

origCalledPartyRedirectOnBehalfOf

0

3

lastRedirectRedirectOnBehalfOf

0

3

origTerminationOnBehalfOf

3

3

destTerminationOnBehalfOf

3

12

joinOnBehalfOf

0

3

duration

7

60

## Call Pickup

There are two types of call pickup in Unified Communications Manager : Pickup and Auto Pickup. The CDR records appear slightly different for these two types of call pickup.

### Pickup

#### Pickup CDR Example

A call comes in from the PSTN to extensions 2000, 2001, and 2002. These extensions reside in the same pickup group. Extension
                                 2002 picks up the call that is ringing on 2001. Extension 2002 answers the call, and the call connects between the PSTN caller
                                 and extension 2002.

Field Names

Pickup Call CDR

globalCallID_callId

22

callingPartyNumber

9728131234

originalCalledPartyNumber

2001

finalCalledPartyNumber

2002

lastRedirectDn

2001

origCause_Value

0

dest_CauseValue

16

origTerminationOnBehalfOf

16

destTerminationOnBehalfOf

16

lastRedirectOnBehalfOf

16

lastRedirectReason

5

joinOnBehalfOf

16

### Auto Pickup

Auto Pickup acts like call pickup with auto answer. The user does not need to press the last answer softkey. The call automatically
                                 connects. Two CDRs get generated for Auto Pickup. These CDRs have the same Call ID.

The first CDR gets generated for the original call. This CDR has the origTerminationOnBehalfOf and destTerminationOnBehalfOf fields equal to 16 (Pickup). Thisvalue indicates that the call got terminated on behalf of the Pickup feature.

The second CDR represents the final call after it was picked up. This CDR has the lastRedirectOnBehalfOf and the joinOnBehalfOf fields set to 16 (Pickup). This value indicates that the call was joined on behalf of the Pickup feature. The lastRedirectReason contains the redirect reason of 5 (Pickup).

Auto Pickup CDRs look the same for all types of auto pickup: Auto Pickup, Auto Group Pickup and Auto Other Pickup.

When the Service Parameter Auto Call Pickup Enabled is set to True for an IP Phone and a Unified Communications Manager receives an incoming call that the IP phone picks up,
                                             the prefix digit defined in the Translation Pattern is added to the callingPartyNumber in CDR. However, the prefix digit is not added when the Service Parameter Auto Call Pickup Enabled is set to False.

#### Auto Pickup CDR Example

Auto Pickup Example - Call goes from the PSTN to extension 2001; 2001 and 2002 exist in the same pickup group. 2002 picks up the call that rings
                                       on 2001; the call automatically connects between the PSTN caller and 2002. They talk for 2 minutes.

The prefix digits defined in the Translation Pattern only applies to basic call.

Field Names

Original Call CDR

Pickup CDR

globalCallID_callId

11

11

origLegCallIdentifier

12345

12345

destLegIdentifier

12346

12347

callingPartyNumber

9728134987

9728134987

originalCalledPartyNumber

2001

2001

finalCalledPartyNumber

2001

2002

lastRedirectDn

2001

2001

origCause_Value

393216

16

dest_CauseValue

393216

0

origTerminationOnBehalfOf

16

12

destTerminationOnBehalfOf

16

16

lastRedirectRedirectReason

0

5

lastRedirectRedirectOnBehalfOf

0

16

joinOnBehalfOf

0

16

duration

0

120

## Call Recording

The system generates CDRs for the Call Recording feature by using existing CDR fields.

The recording calls have one-way media. The media fields stay empty for one side of the call for one-way media CDRs.

The origConversationID field of the two Call Recording CDRs matches the agent call leg identifier in the Recording Call CDR and links together the
                              Call Recording CDR and the CDR of the recorded call.

If the CDR Log Calls with Zero Duration Flag service parameter is set to true, two additional server call records are created.

### Call Recording CDR Examples

The customer (9728134987) calls the agent (30000), and the agent answers. The Recorder's DN is 90000. The recording feature
                                    creates two recording calls to the recording device, which results in two additional CDRs: one for the agent voice, and another
                                    for the customer voice. The origConversationID from the recording CDRs matches the destLegIdentifier of the recorded CDR.
                                    In this scenario, the customer hangs up.

Field Names

Recorded Call CDR

Recording Call CDR1

Recording Call CDR2

globalCallID_callId

7

10

11

origLegCallIdentifier

16777110

16777120

16777122

destLegIdentifier

16777111

16777121

16777123

callingPartyNumber

9728134987

BIB

BIB

originalCalledPartyNumber

30000

90000

90000

finalCalledPartyNumber

30000

90000

90000

lastRedirectDn

30000

90000

90000

origCause_Value

16

0

0

dest_CauseValue

0

0

0

origCalledPartyRedirectReason

0

354

354

lastRedirectRedirectOnBehalfOf

0

354

354

origCalledPartyRedirectOnBehalfOf

27

27

lastRedirectRedirectOnBehalfOf

27

27

origConversationID

0

16777111

16777111

The agent (30000) calls the customer (9728134987), and the customer answers. The Recorder's DN is 90000. The recording feature
                                    creates two recording calls to the recording device, which results in two additional CDRs: one for the agent voice, and another
                                    for the customer voice. The origConversationID field from the recording CDRs will match the origLegCallIdentifier field of the recorded CDR. In this scenario, the agent hangs up.

Field Names

Recorded Call CDR

Recording Call CDR 1

Recording Call CDR 2

globalCallID_callId

71

100

110

origLegCallIdentifier

16777113

16777220

16777222

destLegIdentifier

16777114

16777221

16777223

callingPartyNumber

30000

BIB

BIB

originalCalledPartyNumber

9728134987

90000

90000

finalCalledPartyNumber

9728134987

90000

90000

lastRedirectDn

9728134987

90000

90000

origCause_Value

16

16

16

dest_CauseValue

0

0

0

origCalledPartyRedirectReason

0

354

354

lastRedirectRedirectOnBehalfOf

0

354

354

origCalledPartyRedirectOnBehalfOf

27

27

lastRedirectRedirectOnBehalfOf

27

27

origConversationID

0

16777113

16777113

## Call Secured Status

This field identifies security status of the call. It contains the highest level of security that is reached during a call.
                              For example, if the call is originally unsecured, and later the call changes to secured, the CDR contains 1 for "Secured" even though different portions of the call have different status values. The callSecuredStatus field identifies the security status of the call.

### Call Secured Status CDR Examples

Encrypted Call - The system encrypts the call between 20000 and 20001. The parties talk for 5minutes.

Field Names

CDR

globalCallID_callId

102

origLegCallIdentifier

16777140

destLegIdentifier

16777141

callingPartyNumber

20000

origCalledPartyNumber

20001

finalCalledPartyNumber

20001

lastRedirectDn

20001

origCause_Value

0

dest_CauseValue

16

callSecuredStatus

2

duration

300

Authenticated Call - The call between 20000 and 20001 gets authenticated (not encrypted). The parties talk for 10 minutes.

Field Names

CDR

globalCallID_callId

103

origLegCallIdentifier

16777142

destLegIdentifier

16777143

callingPartyNumber

20000

origCalledPartyNumber

20001

finalCalledPartyNumber

20001

lastRedirectDn

20001

origCause_Value

0

dest_CauseValue

16

callSecuredStatus

1

duration

600

## Calling Party Normalization

This feature provides the support of the international escape code "+" to Unified Communications Manager . This addition enhances the dialing capabilities of dual-mode phones and improves callbacks for companies in different geographical
                              locations.

The callingPartyNumber , originalCalledPartyNumber , finalCalledPartyNumber , lastRedirectDN fields , and the new fields, outpulsedCallingPartyNumber and outpulsedCalledPartyNumber, may now contain a "+" in the CDR. The device reports the Calling Party Number that it outpulsed back to Call Control only
                              if calling party normalization/localization takes place. If calling party normalization/localization occurs, the action gets
                              recorded in the CDR in the new field outpulsedCallingPartyNumber .

### Calling Party Normalization CDR Examples

A call gets placed from a Dallas PSTN to an enterprise phone. The 7-digit calling number comprises 5001212; the Dallas area
                                    code displays 972. The calling party transformation contains +1972. The callingPartyNumber field in the CDR contains +1 972 500 1212 (global format). The new field outpulsedCallingPartyNumber contains the localized number 500 1212.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

+19725001212

outpulsedCallingPartyNumber

5001212

duration

60

A call gets placed from an enterprise phone to a Dallas PSTN. The extension of the enterprise phone comprises 12345; the fully
                                    qualified number comprises 9725002345. Calling party transformation checks the external phone number mask feature. The callingPartyNumber field in the CDR contains +1 972 500 2345 (global format). The new field outpulsedCallingPartyNumber contains the localized number 9725002345.

Field Names

Values

globalCallID_callId

2

origLegCallIdentifier

102

destLegIdentifier

103

callingPartyNumber

+19725002345

outpulsedCallingPartyNumber

9725002345

duration

60

## Calls with Busy or Bad Destinations

The system logs all these calls as normal calls, and all relevant fields contain data. The Calling or Called Party Cause fields
                              contain a cause code that indicates why the call does not connect, and the Called Party IP and Date/Time Connect fields remain
                              blank. The system logs all unsuccessful calls, even if zero duration calls are not being logged (CdrLogCallsWithZeroDurationFlag
                              set at True or False , a duration of zero, and a DateTimeConnect value of zero).

### Examples of Unsuccessful Calls CDRs

Call goes to PSTN number, but party already is engaged (cause 17 = user busy)

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

origCause_Value

0

dest_CauseValue

17

duration

0

Call goes to PSTN number, but number does not exist (cause 1 = number unavailable)

Field Names

CDR

globalCallID_callId

4

origLegCallIdentifier

302

destLegIdentifier

303

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

origCause_Value

1

dest_CauseValue

0

duration

0

Call to PSTN fails because PSTN trunks are out of order (cause 38 = Network Out Of Order).

Field Names

CDR

globalCallID_callId

5

origLegCallIdentifier

304

destLegIdentifier

305

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

origCause_Value

0

dest_CauseValue

38

duration

0

## cBarge

The cBarge feature acts very similar to the conference feature. When a shared line uses the cBarge feature, the origCalledPartyNumber, finalCalledPartyNumber and lastRedirectDn represent the conference bridge number 'b00. . . '. The redirect and join OnBehalfOf fields have a value of Conference = 4, and the redirect reason fields specify Conference = 98.

### cBarge CDR Example

40003 calls 40001, and 40001 answers; 40001' (shared line) on another phone presses the cBarge button.

Field Names

Orig Call CDR

cBarge Call CDR 1

cBarge Call CDR 2

cBarge Call CDR 3

Final Call CDR

globalCallID_callId

49

49

49

49

49

origLegCallIdentifier

1677346

1677348

1677347

1677346

1677347

destLegIdentifier

1677347

1677353

1677351

1677352

1677346

callingPartyNumber

40003

40001

40001

40003

40001

originalCalledPartyNumber

40001

b0029901001

b0029901001

b0029901001

40003

finalCalledPartyNumber

40001

b0029901001

b0029901001

b0029901001

40003

lastRedirectDn

40001

b0029901001

40001

40001

b0029901001

origCause_Value

393216

16

393216

393216

16

dest_CauseValue

393216

0

393216

393216

0

origCalledPartyRedirectReason

0

98

98

98

0

lastRedirectRedirectReason

0

98

98

98

98

destTerminationOnBehalfOf

4

4

4

4

origCalledRedirectOnBehalfOf

4

4

4

lastRedirectRedirectOnBehalfOf

4

4

4

4

joinOnBehalfOf

4

4

4

4

Conversation ID

0

16777220

16777220

16777220

1

duration

60

360

360

360

Comment

Orig Call CDR

cBarge Call CDR 1

ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD

cBarge Call CDR 2

ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD

cBarge Call CDR 3

ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD

Final Call CDR

ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD

## Client Matter Code (CMC)

When the CMC feature gets invoked, the system writes the client matter code into the CDR. The clientMatterCode field contains the client matter code that the caller enters.

### CMC CDR Example

10000 calls 2142364624; the user gets prompted for a client matter code and enters 11111. The caller answers the call and
                              talks for 10 minutes.

Field Names

Values

globalCallID_callId

101

origLegCallIdentifier

16777130

destLegIdentifier

16777131

callingPartyNumber

10000

origCalledPartyNumber

2142364624

finalCalledPartyNumber

2142364624

lastRedirectDn

2142364624

origCause_Value

0

dest_CauseValue

16

clientMatterCode

11111

duration

600

### CMC Example 2

Blind conference using CMC :

Call from 136201 to 136111.

136111 answers and speaks for a few seconds.

136201 presses the Conference softkey and dials 136203.

The user is prompted to enter the CMC code and the user enters 125. CMC code 125 is configured as level 1 and is given a name
                                    as Forward_CMC.

While 136203 is ringing, 136201 presses Conference softkey to complete the conference.

136203 answers the call.

The three members in the conference talk for sometime.

136111 hangs sup, leaving 136201 and 136203 in the conference. Since there are only two participants in the conference, the
                                    conference feature will join these two directly together and they talk for a few seconds.

FieldNames

Orig Call CDR

Setup Call CDR

Conference CDR 1

Conference CDR 2

Conference CDR 3

Final CDR

globalCallID_callId

60025

60026

60025

60025

60025

60027

origLegCallIdentifier

23704522

23704524

23704523

23704522

23704526

23704527

destLegIdentifier

23704523

23704526

23704531

23704530

23704532

23704528

callingPartyNumber

136201

136201

136111

136201

136203

136201

origCalledPartyNumber

136111

136203

b00105401002

b00105401002

b00105401002

136203

finalCalledPartyNumber

136111

136203

b00105401002

b00105401002

b00105401002

136203

lastRedirectDn

136111

136203

136201

136201

136201

136203

origCause_Value

393216

0

16

393216

393216

0

dest_CauseValue

393216

0

393216

393216

393216

16

authCodeDescription

Forward_CMC

authorizationLevel

0

1

0

0

0

0

Duration

20

0

32

32

25

48

authorizationCode

125

The setup call CDR for this example is generated even though it is of zero duration since CMC is used for this call.

## Conference Calls

Multiple records get logged for calls that are part of a conference. The number of CDR records that get generated depends
                              on the number of parties in the conference. One CDR exists for each party in the conference; one CDR for the original placed
                              call, one CDR for each setup call that gets used to join other parties to the conference, and one CDR for the last two parties
                              that get connected in the conference. For a three-party, ad hoc conference, six CDRs exist: one CDR for the original call,
                              three CDRs for the parties that get connected to the conference, one CDR for each setup call, and one CDR for the final two
                              parties in the conference. You can associate the setup calls with the correct call leg in the conference by examining the
                              calling leg ID and called leg ID.

The conference bridge device represents special significance to the Unified Communications Manager , and calls to the conference bridge appear as calls to the conference bridge device. A special number in the form "b0019901001" shows the conference bridge port. Records show all calls into the conference bridge, regardless of the actual direction;
                              however, by examining the setup call CDRs, you can determine the original direction of each call.

You can find the conference controller information in the comment field of the CDR. The format of this information follows:

Comment field = "ConfControllerDn=1000;ConfControllerDeviceName=SEP0003"

The conference controller DN + conference controller device name uniquely identify the conference controller. The system needs
                                    the device name in the case of shared lines.

If the call is involved in multiple conference calls, the comment field contains multiple conference controller information.
                                    This situation can occur when the conference goes down to two parties, and one of these parties starts another conference.
                                    If this is the case, the last conference controller information in the comment field identifies the conference controller.

The call legs that are connected to the conference include the following information fields:

The finalCalledPartyNumber field contains the conference bridge number "b0019901001."

The origCalledPtyRedirectOnBehalfOf field gets set to Conference = 4.

The lastRedirectRedirectOnBehalfOf field gets set to Conference = 4.

The joinOnBehalfOf field gets set to (Conference = 4).

The comment field identifies the conference controller.

The destConversationID field remains the same for all members in the conference. You can use this field to identify members of a conference call.

The original placed call and all setup calls that were used to join parties to the conference have the following characteristics:

The origCallTerminationOnBehalfOf field gets set to Conference = 4.

The destCallTerminationOnBehalfOf field gets set to Conference = 4.

### Conference Call CDR Example

Call goes from 2001 to 2309.

2309 answers and talks for 60 seconds.

2001 presses the conference softkey and dials 3071111.

307111 answers and talks for 20 seconds; then, 2001 presses the conference softkey to complete the conference.

The three members of the conference talk for 360 seconds.

3071111 hangs up and leaves 2001 and 2309 in the conference. Because only two participants are left in the conference, the
                              conference features joins these two directly together, and they talk for another 55 seconds.

Each conference call leg gets shown as placing a call into the conference bridge. The system shows the call as a call into
                                          the bridge, regardless of the actual direction of the call.

Field Names

Orig Call CDR

Setup Call CDR

Conference CDR 1

Conference CDR 2

Conference CDR 3

Final CDR

globalCallID_callId

1

2

1

1

1

1

origLegCallIdentifier

101

105

101

102

106

101

destLegIdentifier

102

106

115

116

117

102

callingPartyNumber

2001

2001

2001

2309

3071111

2001

originalCalledPartyNumber

2309

3071111

b0029901001

b0029901001

b0029901001

2309

finalCalledPartyNumber

2301

3071111

b0029901001

b0029901001

b0029901001

2309

lastRedirectDn

2001

3071111

b0029901001

b0029901001

b0029901001

b0029901001

origCause_Value

393216

0

16

393216

393216

16

dest_CauseValue

393216

0

393216

393216

393216

0

origCalledPartyRedirectReason

0

0

0

0

0

0

lastRedirectRedirectReason

0

0

0

0

0

98

origTerminationOnBehalfOf

4

4

12

12

4

12

destTerminationOnBehalfOf

4

4

0

0

4

4

origCalledRedirectOnBehalfOf

0

0

4

4

4

0

lastRedirectRedirectOnBehalfOf

0

0

4

4

4

4

joinOnBehalfOf

0

0

4

4

4

4

Conversation ID

0

0

1

1

1

0

duration

60

20

360

360

360

55

Comment

Orig Call CDR

Setup Call CDR

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Conference CDR 1

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Conference CDR 2

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Conference CDR 3

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Final CDR

### Operational Factors

Three major operational factors exist for conference call CDRs:

When a conference decreases to two parties, the two parties connect directly and release the conference resource. This change
                                       generates an additional CDR for the call between the last two parties in the conference call.

For example, if four people connect in a conference call (Amy, Dustin, Spencer, Ethan), when Ethan hangs up, three people
                                       remain in the conference call that is connected to the conference bridge (Amy, Dustin, Spencer). When Spencer hangs up, only
                                       two people remain in the conference call (Amy and Dustin). The system joins Amy and Dustin directly, and, the conference resource
                                       gets released. Directly joining Amy and Dustin creates an additional CDR between the last two parties in the conference.

The system adds the conference controller information to the comment field in the CDR. This information identifies the conference
                                       controller. No need now exists to examine the consultation call to determine who is the conference controller. The following
                                       example shows this information:

Comment field = "ConfControllerDn=1000;ConfControllerDeviceName=SEP0003E333FEBD"

The conference controller DN + conference controller device name uniquely identify the conference controller. A need for the
                                             device name exists in the case of shared lines.

If the call is involved in multiple conference calls, the comment field contains multiple conference controller information.
                                             This situation may occur when the conference goes down to two parties, and one of these parties starts another conference.
                                             If this is the case, the last conference controller information in the comment field identifies the conference controller.

The party that added the participant, known as the requestor party, appears in the CDR comment field. The tags for the requestor
                                       information include ConfRequestorDn and ConfRequestorDeviceName. The party that requested to remove a participant, known as
                                       the drop requestor, appears in the CDR comment field. The tags for the drop requestor information include DropConfRequestorDn
                                       and DropConRequestorDeviceName.

Calls that are part of a conference have multiple records that are logged for them. The number of CDRs that get generated
                                 depends on the number of parties in the conference. One CDR exists for each party in the conference, one CDR for the original
                                 placed call, and one CDR for each setup call that is used to join other parties to the conference. Therefore, for a three-party
                                 ad hoc conference, six CDRs exist:

One CDR for the original call.

Three CDRs for the parties that are connected to the conference.

One CDR for each setup call.

One CDR for the final two parties in the conference.

You can associate the setup calls with the correct call leg in the conference by examining the callinglegID and the calledlegID.

The conference bridge device holds special significance to the Unified Communications Manager . Calls to the conference bridge appear as calls to the conference bridge device. A special number in the form "b0019901001" shows the conference bridge port. All calls get shown "into" the conference bridge, regardless of the actual direction. You can determine the original direction of each call by examining
                                 the setup call CDRs.

The call legs that are connected to the conference have the following values for these fields:

finalCalledPartyNumber —Represents a conference bridge "b0019901001" .

origCalledPartyRedirectOnBehalfOf —Set to Conference (4).

lastRedirectRedirectOnBehalfOf —Set to Conference (4).

joinOnBehalfOf —Set to Conference (4).

comment —Identifies the conference controller.

The original placed call and all setup calls that get used to join parties to the conference have the following values for
                                 the fields:

origCallTerminationOnBehalfOf —Set to Conference (4).

destCallTerminationOnBehalfOf —Set to Conference (4).

## Conference Now Calls

This feature allows both external and internal callers to join a conference by dialing a Conference Now IVR Directory Number.
                              An Interactive Voice Response (IVR) application guides the caller to join the conference by playing an announcement and collecting
                              caller entered DTMF digits.

A conference call using the Conference Now feature logs multiple CDR records for a call. The number of CDR records that get
                              generated depends on the number of parties in the conference. One CDR exists for each party in the conference; one CDR for
                              the original placed call, and one CDR for each setup call that get used to join the conference bridge. For a two-party, Conference
                              Now, four CDRs exists: two CDR for the original call, and two CDR for parties that get connected to the conference bridge.

The conference bridge device represents special significance to the Unified Communications Manager , and calls to the conference bridge appear as calls to the conference bridge device. A special number in the form "b00105401006" shows the conference bridge port. Records show all calls into the conference bridge, regardless of the actual direction;
                              however, by examining the setup call CDRs, you can determine the original direction of each call.

You can find the Conference Now host information in the comment field of the CDR. The comments field will only be populated
                              for redirection of the call to the CFB. The format of this information follows:

Comment field = "ConferenceNowHostId =john; ConferenceNowMeetingNumber=136136" .

The ConferenceNowHostId+ConferenceNowMeetingNumber uniquely identifies the Conference Now information.

The call legs that are connected to the conference include the following information fields:

The finalCalledPartyNumber field contains the conference bridge number "b00105401006" .The finalCalledPartyNumber field in case of initial call when it connects to IVR contains the IVR directory number "c00124401001" .

The origCalledPtyRedirectOnBehalfOf field is set to (Meet-me Conference Intercepts= 7).

The lastRedirectRedirectOnBehalfOf field is set to (Meet-me Conference Intercepts= 7).

The joinOnBehalfOf field is set to (Meet-me Conference Intercepts=7).

The comment field identifies ConfrenceNowHostId and ConferenceNowMeetingNumber.

The destConversationId field is the same for all members in the conference. This field can be used to identify members of
                                    a conference call.

The original placed call and all setup calls that were used to join parties to the conference have the following characteristics:

The origCallTerminationOnBehalfOf field is set to (Meet-me Conference Intercepts= 7).

The destCallTerminationOnBehalfOf field is set to (Meet-me Conference Intercepts= 7).

### ConferenceNow CDR Example

The following table contains an example CDR for the following scenario.

User A (139139) calls into a Conference Now conference bridge with the phone number 1010.

User A (139139) connects to IVR and IVR requests for a Meeting Number.

User A (139139) dials the Meeting Number " 136136" followed by #.

User A (139139) joins as an attendee; therefore presses # and then enters attendee access code followed by #.

User A (139139) is placed on Music On Hold (MoH).

User B (136136) dials the Conference Now phone number 1010.

User B (136136) connects to IVR and the IVR requests for a Meeting Number.

User B (136136) dials in the Meeting Number followed by #.

User B (136136) enters the host pin followed by # as the user is joining the conference call as a host.

Both the attendee and the host get redirected to Conference Bridge and are placed into conference.

FieldNames

Orig Call CDR1

Conference CDR 1

Orig Call CDR2

Conference CDR 2

globalCallID_callId

47002

47002

47003

47003

origLegCallIdentifier

20795093

20795093

20795098

20795098

destLegIdentifier

20795096

20795104

20795101

20795103

callingPartyNumber

139139

139139

136136

136136

originalCalledPartyNumber

1010

1010

1010

1010

finalCalledPartyNumber

c00124401001

b00105401006

c00124401001

b00105401006

lastRedirectDn

1010

c00124401001

1010

c00124401001

origCause_Value

0

16

0

16

dest_CauseValue

0

0

0

0

origCalledPartyRedirectReason

0

0

0

0

lastRedirectRedirectReason

0

0

0

0

origTerminationOnBehalfOf

7

12

7

12

destTerminationOnBehalfOf

7

7

7

7

origCalledRedirectOnBehalfOf

0

0

0

0

lastRedirectRedirectOnBehalfOf

0

7

0

7

joinOnBehalfOf

0

7

0

7

Conversation ID

0

16809217

0

16809217

duration

14

20

10

9

Comment

Orig Call CDR 1

Conference CDR 1

ConferenceNowHostID=Rishi;ConferenceNowMeetingNumber=136136

Orig Call CDR 2

Conference CDR 2

ConferenceNowHostID=Rishi;ConferenceNowMeetingNumber=136136

## Conference Drop Any Party

The Conference Drop Any Party feature terminates calls that look the same as other calls except for a new cause code. The
                              cause code identifies the calls that this feature terminates.

### Conference Drop Any Party CDR Example

The following table contains an example CDR for a call that connects to a conference and gets dropped by this feature.

Calling

Party

Calling

Partition

Original Called Party

Orig Cause

Original Called Partition

Called Leg

Dest Cause

Final Called

Party

Final Called

Partition

Last Redirect Party

2001

ACNTS

2309

0

MKTG

102

16

2309

MKTG

2001

2001

ACNTS

2309

16

MKTG

115

0

b0029901001

b0029901001

2309

ACNTS

b0029901001

0

116

128

b0029901001

b0029901001

3071111

PSTN

b0029901001

16

117

0

b0029901001

b0029901001

2001

ACNTS

2309

16

PSTN

106

0

3071111

PSTN

30711111

Orig Conversation ID

OrigCall Termination OnBehalfOf

DestCall Termination OnBehalfOf

OriginalCalled Pty Redirect OnBehalfOf

LastRedirect Redirect OnBehalfOf

Join OnBehalfOf

Duration

0

4

4

0

0

0

60

1

12

0

4

4

4

360

1

13

0

4

4

4

200

1

4

4

4

4

4

360

0

4

4

0

0

0

20

### Original Calling Party on Transfer

## DTMF Method

These fields identify the Dual Tone Multi-Frequency (DTMF) method that gets used for the call.

### DTMF CDR Examples

No Preference Example - The DTMF method that gets used during this call represents No Preference/Best Effort. This call connects for 1minute.

Field Names

CDR

globalCallID_callId

200

origLegCallIdentifier

16777500

destLegIdentifier

16777501

callingPartyNumber

20000

origCalledPartyNumber

20001

finalCalledPartyNumber

20001

lastRedirectDn

20001

origCause_Value

0

dest_CauseValue

16

origDTMFMethod

0

destDTMFMethod

0

duration

60

Preferred OOB Example - The DTMF method that is used during this call represents OOB Preferred. This call remains connected for 1minute.

Field Names

CDR

globalCallID_callId

201

origLegCallIdentifier

16777502

destLegIdentifier

16777503

callingPartyNumber

20000

origCalledPartyNumber

20001

finalCalledPartyNumber

20001

lastRedirectDn

20001

origCause_Value

0

dest_CauseValue

16

origDTMFMethod

1

destDTMFMethod

1

duration

60

## End-to-End Call Trace

The End-to-End Call Trace feature facilitates tracing calls that traverse multiple Cisco voice products, such as Unified CM,
                              Cisco IOS Gateways, and other products.

### End-to-End Call Trace Example

H323 - Calling party 1003 calls 1004 via H.323 trunk.

FieldNames

Values

cdrRecordType

1

globalCallID_callManagerId

1

globalCallID_callId

32009

origLegCallIdentifier

19654113

dateTimeOrigination

1221263718

origNodeId

1

origSpan

0

origIpAddr

1897990154

callingPartyNumber

1004

origCause_value

16

origPrecedenceLevel

4

origMediaTransportAddress_IP

1897990154

origMediaTransportAddress_Port

19824

origMediaCap_payloadCapability

4

origMediaCap_maxFramesPerPacket

20

destLegIdentifier

19654114

destNodeId

1

destSpan

19654114

destIpAddr

424630538

originalCalledPartyNumber

1003

finalCalledPartyNumber

1003

destCause_value

0

destPrecedenceLevel

4

destMediaTransportAddress_IP

-1759442934

destMediaTransportAddress_Port

27508

destMediaCap_payloadCapability

4

destMediaCap_maxFramesPerPacket

20

dateTimeConnect

1221263720

dateTimeDisconnect

1221263721

lastRedirectDn

1003

Pkid

c8868f84-0f4e-452c-a814-bf97a7fe69fc

Duration

1

origDeviceName

SEP003094C2B08C

destDeviceName

self-loop

origCallTerminationOnBehalfOf

12

destCallTerminationOnBehalfOf

0

origDTMFMethod

3

destDTMFMethod

4

origMediaCap_Bandwidth

64

destMediaCap_Bandwidth

64

origIpv4v6Addr

10.8.33.113

destIpv4v6Addr

10.8.33.151

IncomingProtocolID

0

IncomingProtocolCallRef

OutgoingProtocolID

2

OutgoingProtocolCallRef

0053C43F6701B18C030004010A082171

Q931 - 1004 calls 1003 via Q931.

FieldNames

Values

cdrRecordType

1

globalCallID_callManagerId

1

globalCallID_callId

32008

origLegCallIdentifier

19654111

dateTimeOrigination

1221263350

origNodeId

1

origSpan

2

origIpAddr

122640650

callingPartyNumber

1004

origCause_value

0

origPrecedenceLevel

4

origMediaTransportAddress_IP

122640650

origMediaTransportAddress_Port

17218

origMediaCap_payloadCapability

4

origMediaCap_maxFramesPerPacket

20

destLegIdentifier

19654112

destNodeId

1

destSpan

0

destIpAddr

-1759442934

originalCalledPartyNumber

1003

finalCalledPartyNumber

1003

destCause_value

16

destPrecedenceLevel

4

destMediaTransportAddress_IP

-1759442934

destMediaTransportAddress_Port

23350

destMediaCap_payloadCapability

4

destMediaCap_maxFramesPerPacket

20

dateTimeConnect

1221263351

dateTimeDisconnect

1221263352

lastRedirectDn

1003

Pkid

b576bd8d-9703-4f66-ae45-64ae5c04738e

Duration

1

origDeviceName

BRI/S1/SU0/P1@nw052b-3640.cisco.com

destDeviceName

SEP003094C2D263

origCallTerminationOnBehalfOf

0

destCallTerminationOnBehalfOf

12

origDTMFMethod

1

destDTMFMethod

3

origMediaCap_Bandwidth

64

destMediaCap_Bandwidth

64

origIpv4v6Addr

10.89.79.7

destIpv4v6Addr

10.8.33.151

IncomingProtocolID

4

IncomingProtocolCallRef

01-1004-1003

OutgoingProtocolID

0

OutgoingProtocolCallRef

## Forced Authorization Code (FAC)

When the FAC feature gets invoked, the system writes the authorization description and level into the CDR. For security reasons,
                              the actual authorization code does not get written to the CDR.

The authCodeDescription field contains the description of the authorization code.

The authorizationLevel field contains the level of authorization that is associated with the authorization code.

### FAC CDR Example 1

45000 calls 9728134987; the system prompts the user for an authorization code and enters 12345. FAC code 12345 gets configured
                              as level 1 and name Legal1. The caller answers the call and talks for 2minutes.

Field Names

Values

globalCallID_callId

100

origLegCallIdentifier

16777123

destLegIdentifier

16777124

callingPartyNumber

45000

origCalledPartyNumber

9728134987

finalCalledPartyNumber

9728134987

lastRedirectDn

9728134987

origCause_Value

0

dest_CauseValue

16

authCodeDescription

Legal1

authorizationLevel

1

duration

120

authorizationCode

12345

### FAC Example 2

CDR will now be written for a setup call leg for all the unanswered calls before the call is redirected to another caller
                              if FAC is used to setup the call.

The unanswered call will not have any connect time since media is not connected for this call. The CDR will be logged regardless
                                          of the service parameter CdrLogCallsWithZeroDurationFlag if FAC is present in the call.

Blind conference using FAC:

Call from 136201 to 136111.

136111 answers and speaks for a few seconds.

136201 presses the Conference softkey and dials 136203.

The user is prompted to enter the FAC code and the user enters 124. FAC code 124 is configured as level 1 and given a name
                                    as Forward_FAC.

While 136203 is ringing, 136201 presses the Conference softkey to complete the conference.

136203 answers the call.

The three members in the conference talk for sometime.

136111 hangs up, leaving 136201 and 136203 in the conference. Since there are only two participants in the conference, the
                                    conference feature will join these two directly together and they talk for a few seconds.

FieldNames

Orig Call CDR

Setup Call CDR

Conference CDR 1

Conference CDR 2

Conference CDR 3

Final CDR

globalCallID_callId

60015

60016

60015

60015

60015

60017

origLegCallIdentifier

23704372

23704374

23704373

23704372

23704376

23704377

destLegIdentifier

23704373

23704376

23704381

23704380

23704382

23704378

callingPartyNumber

136201

136201

136111

136201

136203

136201

origCalledPartyNumber

136111

136203

b00105401002

b00105401002

b00105401002

136203

finalCalledPartyNumber

136111

136203

b00105401002

b00105401002

b00105401002

136203

lastRedirectDn

136111

136203

136201

136201

136201

136203

origCause_Value

393216

0

16

393216

393216

0

dest_CauseValue

393216

0

393216

393216

393216

16

authCodeDescription

Forward_FAC

authorizationLevel

0

1

0

0

0

0

Duration

18

0

37

37

32

38

authorizationCode

124

The setup call CDR for this example is generated even though it is of zero duration since FAC is used for this call.

## Forwarded or Redirected Calls

Forwarded calls generate a single CDR and show the Calling Party, Original Called Number, Last Redirecting Number, Final Called
                              Number, and the associated partitions. If the call gets forwarded more than twice, the intermediate forwarding parties do
                              not populate in the CDR.

Call forwarding can occur on several conditions (always, busy, and no answer). The condition under which the call gets forwarded
                              does not populate in the CDR.

The CDRs for forwarded calls match those for normal calls, except for the originalCalledPartyNumber field and the originalCalledPartyNumberPartition
                              field. These fields contain the directory number and partition for the destination that was originally dialed by the originator
                              of the call. If the call gets forwarded, the finalCalledPartyNumber and finalCalledPartyNumberPartition fields differ and
                              contain the directory number and partition of the final destination of the call.

Also, when a call gets forwarded, the lastRedirectDn and lastRedirectDnPartition fields contain the directory number and partition
                              of the last phone that forwarded or redirected the call.

Call Forwarding uses the redirect call primitive to forward the call. Features that use the redirect call primitive have similar
                              CDRs. Some of the important CDR fields for forwarded calls follow:

The originalCalledPartyNumber contains the number of the original called party.

The finalCalledPartyNumber represents the number that answered the call.

The lastRedirectDn field specifies the number that performed the last redirect.

The origCalledPartyRedirectReason represents the reason that the call was redirected the first time. For call forwarding, this field can contain Call Forward Busy=1, Call Forward No Answer=2, Call Forward All=15 .

The lastRedirectRedirectReason specifies the reason that the call was redirected the last time. For call forwarding, this field can contain Call Forward Busy=1, Call Forward No Answer=2, Call Forward All=15 .

The origCalledPartyRedirectOnBehalfOf field identifies which feature redirects the call for the first redirect. For call forwarding, this field specifies 5 (Call
                                    Forward).

The lastRedirectRedirectOnBehalfOf field identifies which feature redirects the call for the last redirect. For call forwarding, this field specifies 5 (Call
                                    Forward).

### Forwarded Calls CDR Examples

CFA - Call comes in from the PSTN to extension 2001; the call gets forwarded (CFA) to 2309, where the call is answered, and talk
                                    occurs for 2minutes.

Field Names

CDR

globalCallID_callId

12345

origLegCallIdentifier

100

destLegIdentifier

102

callingPartyNumber

9728134987

originalCalledPartyNumber

2001

finalCalledPartyNumber

2309

lastRedirectDn

2001

origCause_Value

0

dest_CauseValue

16

origCalledPartyRedirectReason

15

lastRedirectRedirectReason

15

origCalledPartyRedirectOnBehalfOf

5

lastRedirectRedirectOnBehalfOf

5

duration

120

Multiple Hop CFA & CFNA - Call comes in from the PSTN to extension 1000; the call gets forwarded (CFA) to 2000; then, the call gets forwarded (CFNA)
                                    to the voice-messaging system (6000) where the caller leaves a message.

Field Names

CDR

globalCallID_callId

12346

origLegCallIdentifier

102

destLegIdentifier

105

callingPartyNumber

9728134987

originalCalledPartyNumber

1000

finalCalledPartyNumber

6000

lastRedirectDn

2000

origCause_Value

0

dest_CauseValue

16

origCalledPartyRedirectReason

15

lastRedirectRedirectReason

2

origCalledPartyRedirectOnBehalfOf

5

lastRedirectRedirectOnBehalfOf

5

duration

15

Multiple Hop CFNA & CFB - Call comes in from the PSTN to extension 4444; the call gets forwarded (CFNA) to 5555; then, it gets forwarded (CFB) to
                                    6666 where the call is answered, and they talk for 30 seconds.

Field Names

CDR

globalCallID_callId

12347

origLegCallIdentifier

106

destLegIdentifier

108

callingPartyNumber

9728134987

originalCalledPartyNumber

4444

finalCalledPartyNumber

6666

lastRedirectDn

5555

origCause_Value

16

dest_CauseValue

0

origCalledPartyRedirectReason

2

lastRedirectRedirectReason

1

origCalledPartyRedirectOnBehalfOf

5

lastRedirectRedirectOnBehalfOf

5

duration

30

## Hunt List Support

### Hunt List Examples

Answered Calls - In this example, calls go to a hunt list and a member of the hunt list answers the call.

Cisco Unified IP Phone s 3001, 3002, 3003 and 3004 are part of the hunt list. The display names for the phones are 3001-Name, 3002-Name, 3003-Name
                                          and 3004-Name, respectively.

Hunt Pilot 2000 is associated with a hunt list. Hunt pilot 2000 is configured with display name as 2000-Name.

Phone 1000 calls hunt pilot 2000; call is offered at 3001 and answered.

When the Show Line Group Member DN in finalCalledPartyNumber CDR Field service parameter is set to True, the following values appear in the CDR.

Field Names

CDR

callingPartyNumber

1000

callingPartyNumberPartition

originalCalledPartyNumber

2000

originalCalledPartyNumberPartition

finalCalledPartyNumber

3001

finalCalledPartyNumberPartition

origDeviceName

Phone 1000

destDeviceName

Phone 3001

huntPilotDN

2000

huntPilotPartition

When the Show Line Group Member DN in finalCalledPartyNumber CDR Field service parameter is set to False, the following values in the table display in the CDR.

Field Names

CDR

callingPartyNumber

1000

callingPartyNumberPartition

originalCalledPartyNumber

2000

originalCalledPartyNumberPartition

finalCalledPartyNumber

2000

finalCalledPartyNumberPartition

origDeviceName

Phone 1000

destDeviceName

Phone 3001

huntPilotDN

2000

huntPilotPartition

Abandoned or Failed Calls - In this example, calls go to a hunt list and a member of the hunt list abandons or fails the call.

Cisco Unified IP Phone s 3001, 3002, 3003 and 3004 are part of the hunt list.

Hunt Pilot 2000 is associated with a hunt list.

Phone 1000 calls hunt pilot 2000; call is offered at 3001 and abandoned. When the Show Line Group Member DN in finalCalledPartyNumber CDR field service parameter is set to True, the following values from the table display in the CDR:

Field Names

CDR

callingPartyNumber

1000

callingPartyNumberPartition

originalCalledPartyNumber

2000

originalCalledPartyNumberPartition

finalCalledPartyNumber

2000

finalCalledPartyNumberPartition

origDeviceName

Phone 1000

destDeviceName

Phone 3001

huntPilotDN

huntPilotPartition

calledPartyPatternUsage

7

If the call is not answered by any of the hunt group members, the finalCalledPartyNumber field shows the hunt pilot DN. The
                                          number shows a line group member DN only when one of the line group member answers the call.

Because the call does not get answered, the huntPilotDN is not available in the CDR. The PatternUsage (7 = PATTERN_HUNT_PILOT) field gets set to 7 to indicate that the call was made to a hunt pilot. When the service parameter
                              is enabled, the finalCalledPartyNumber field denotes the member hunt DN and the originalCalledPartyNumber field denotes the huntPilot DN.

When the Show Line Group Member DN in the finalCalledPartyNumber CDR field service parameter is set to False, the following values in the table display in the CDR:

Field Names

CDR

callingPartyNumber

1000

callingPartyNumberPartition

originalCalledPartyNumber

2000

originalCalledPartyNumberPartition

finalCalledPartyNumber

2000

finalCalledPartyNumberPartition

origDeviceName

Phone 1000

destDeviceName

Phone 3001

huntPilotDN

huntPilotPartition

calledPartyPatternUsage

7

Because the call is not answered, the huntPilotDN is not available in the CDR. The PatternUsage (7 = PATTERN_HUNT_PILOT) field gets set to 7 to indicate that the call was made to a hunt pilot. When the service parameter
                              is not enabled, the finalCalledPartyNumber field denotes the member hunt DN.

## H.239

Unified Communications Manager supports H.239. This feature defines the procedures for use of up to two video channels in H.320-based systems and for labeling
                              individual channels with a role of "presentation" or "live." This procedure indicates the requirements for processing the channel and the role of the channel content in the call. Role
                              labels apply to both H.320 and H.245 signaling-based systems.

Several new CDR fields support a second video channel for both the origination and destination devices. This CDR provides
                              an example of these new fields.

### H.239 CDR Example

When A and B declare H.239 capability in Terminal Capability Set (TCS) and one, or both, of the endpoints initiates the receiving
                              channel to have an extended video channel in an H.239 mechanism for presentation or video feed, the new CDR fields display
                              in the CDR in addition to the existing fields of a video call.

Calling party 51234 calls the called party 57890. Let 103 represent H.264, 187962284 represents 172.19.52.11, 288625580 represents
                              172.19.52.17, and 352 represents 352K.

Field Names

CDR

globalCallID_callId

121

origLegCallIdentifier

101

destLegIdentifier

102

callingPartyNumber

51234

originalCalledPartyNumber

57890

finalCalledPartyNumber

57890

lastRedirectDn

57890

origCause_Value

0

destCause_Value

16

origVideoCap_Codec

103

origVideoCap_Bandwidth

352

origVideoCap_Resolution

0

origVideoTransportAddress_IP

187962284

origVideoTransportAddress_Port

2406

destVideoCap_Codec

103

destVideoCap_Bandwidth

352

destVideoCap_Resolution

0

destVideoTransportAddress_IP

288625580

destVideoTransportAddress_Port

2328

origVideoCap_Codec_Channel2

103

origVideoCap_Bandwidth_Channel2

352

origVideoCap_Resolution_Channel2

0

origVideoTransportAddress_IP_Channel2

187962284

origVideoTransportAddress_Port_Channel2

2410

origVideoChannel_Role_Channel2

0

destVideoCap_Codec_Channel2

103

destVideoCap_Bandwidth_Channel2

352

destVideoCap_Resolution_Channel2

0

destVideoTransportAddress_IP_Channel2

288625580

destVideoTransportAddress_Port_Channel2

2330

destVideoChannel_Role_Channel2

0

## iLBC Calls

Internet Low Bit Rate Codec (iLBC) enables graceful speech quality degradation in a lossy network where frames get lost. For
                              iLBC calls, the codec specifies Media_Payload_ILBC = 86.

The system adds an audio bandwidth field to the CDR for iLBC calls.

Field Names

Definitions

origMediaCap_bandwidth

This integer field contains the audio bandwidth.

destMediaCap_bandwidth

This integer field contains the audio bandwidth.

The system populates the bandwidth fields based on the following table:

Codec

Bandwidth

G711Alaw64k

64

G711Alaw56k

56

G711mu-law64k

64

G711mu-law56k

56

G722 64k

64

G722 56k

56

G722 48k

48

G7231

7

G728

16

G729

8

G729AnnexA

8

Is11172AudioCap

0

Is13818AudioCap

0

G729AnnexB

8

G729AnnexAwAnnexB

8

GSM Full Rate

13

GSM Half Rate

7

GSM Enhanced Full Rate

13

Wideband 256K

256

Data 64k

64

Data 56k

56

G7221 32K

32

G7221 24K

24

AAC-LD (mpeg4-generic)

256

AAC-LD (MP4A-LATM) 128K

128

AAC-LD (MP4A-LATM) 64K

64

AAC-LD (MP4A-LATM) 56K

56

AAC-LD (MP4A-LATM) 48K

48

AAC-LD (MP4A-LATM) 32K

32

AAC-LD (MP4A-LATM) 24K

24

GSM

13

iLBC

15 or 13

iSAC

32

XV150 MR 729A

8

NSE VBD 729A

8

### iLBC Call CDR Example

This example applies to a call with iLBC codec.

Field Names

iLBC CDR

globalCallID_callId

121

origLegCallIdentifier

101

destLegIdentifier

102

callingPartyNumber

51234

originalCalledPartyNumber

57890

finalCalledPartyNumber

57890

lastRedirectDn

57890

origCause_Value

0

dest_CauseValue

16

origMediaCap_payloadCapability

86

origMediaCap_Bandwidth

15

destMediaCap_payloadCapability

86

destMediaCap_Bandwidth

15

## Intercompany Media Engine

### Successful IME Calls

A call is made to PSTN. The gateway has it in the learned IME route and the call is extended to IME trunk. Call is successfully
                              routed out through IME trunk.

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

lastRedirectRedirectOnBehalfOf

30

lastRedirectRedirectReason

0

duration

10

### Failed IME Calls Due to IME Trunk Rejection

A call is made to PSTN. The gateway has it in the learned IME route and the call is extended to IME trunk. The IME trunk
                              rejects the call, and the call treatment does not cause the call to be redirected to the PSTN, so the call gets rejected.
                              Depending on the reason of IME trunk reject, different lastRedirectRedirectReason can be reported.

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

origTerminationOnBehalfOf

30

lastRedirectRedirectOnBehalfOf

30

lastRedirectRedirectReason

496 OR 512 OR 528 OR 544 OR 560 OR 576 OR 592 OR 608 OR 624 OR 640 OR 656 OR 672 OR 688 OR 704

origCause_Value

31

duration

0

### IME Calls Redirected to PSTN Due to IME Trunk Rejection

A call is made to PSTN. The gateway has it in the learned IME route and the call is extended to IME trunk. The IME Trunk
                              rejects the call, and the call treatment DOES cause the call to be redirected to the PSTN, so the call gets rejected. Depending
                              on reason of IME trunk reject, different lastRedirectRedirectReason can be reported.

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

lastRedirectRedirectOnBehalfOf

30

lastRedirectRedirectReason

496 OR 512 OR 528 OR 544 OR 560 OR 576 OR 592 OR 608 OR 624 OR 640 OR 656 OR 672 OR 688 OR 704

duration

10

### IME Call Successfully Routed Out Through IME Trunk, Call Fallback to PSTN Due to Poor QoS

A call is made to PSTN. The gateway has it in the learned IME route and the call is extended to IME trunk. Call is routed
                              out through IME trunk. Bad QoS later discovered and call falls back to PSTN.

Two CDRs are generated in this case; one for the IME call and one for fallback to PSTN call.

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

OrigTerminationOnBehalfOf

30

lastRedirectRedirectOnBehalfOf

30

origCause_value

132

duration

5

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

lastRedirectRedirectOnBehalfOf

31

joinOnBehalfOf

31

lastRedirectRedirectReason

722

duration

5

### Clear the PSTN Failback Call Case 1

A call is made to PSTN. The gateway has it in the learned IME route and the call is extended to IME trunk. Call is routed
                              out through IME trunk. Bad QoS is discovered later and fall back initiated to PSTN. Call is rejected by PSTN gateway. Call
                              is intercepted by Fallback Manager which clears the call. IME call remains untouched.

Two CDRs are generated in this case; one for the IME call and one for fallback to PSTN call.

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

lastRedirectRedirectOnBehalfOf

30

lastRedirectRedirectReason

0

duration

5

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

OrigTerminationOnBehalfOf

31

origCause_value

Existing PSTN GW cause codes

duration

0

### Clear the PSTN Failback Call Case 2

A call is made to PSTN. The gateway has it in the learned IME route and the call is extended to IME trunk. Call is routed
                              out through IME trunk. Bad QoS is discovered later and fall back initiated to PSTN. Cannot find link to IME call. Call is
                              intercepted by Fallback Manager which clears the call. IME call remains untouched.

Two CDRs are generated in this case; one for the IME call and one for fallback to PSTN call.

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

lastRedirectRedirectOnBehalfOf

30

lastRedirectRedirectReason

0

duration

5

Field Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

callingPartyNumber

2001

originalCalledPartyNumber

9728134987

OrigTerminationOnBehalfOf

31

origCause_value

133 OR 134 OR existing cause codes

duration

0

## Immediate Divert (to Voice-Messaging System)

Immediate Divert (IDivert) gets invoked in three different call states:

You can invoke the IDivert feature while the incoming call is ringing. The CDR for the ringing case acts very similar to call
                                    forwarding, but the origCalledPartyRedirectOnBehalfOf and the lastRedirectRedirectOnBehalfOf fields specify Immediate Divert = 14.

You can invoke the IDivert feature while the call is connected or on hold. These scenarios generate two CDRs. Both CDRs have
                                    the same globalCallID_CallId field. The first CDR applies to the original connection, and the second CDR applies to the call redirected to the voice-messaging
                                    system. The first call has the origTerminationOnBehalfOf and destTerminationOnBehalfOf fields set to Immediate Divert = 14.

The call that gets redirected to the voice-messaging system has the origCalledPartyRedirectOnBehalfOf and lastRedirectRedirectOnBehalfOf fields set to Immediate Divert = 14.

### IDivert CDR Examples

IDivert during Alerting – 40003 calls 40001, and while 40001 is ringing, 40001 presses the IDivert button, and call diverts to the voice-messaging system
                                    40000.

If the call gets redirected by IDivert in the Alerting state, only one CDR gets generated.

Field Names

Original call CDR

globalCallID_callId

37

origLegCallIdentifier

16777327

destLegIdentifier

16777329

callingPartyNumber

40003

origCalledPartyNumber

40001

finalCalledPartyNumber

40000

lastRedirectDn

40001

origCause_Value

16

dest_CauseValue

0

origCalledPartyRedirectReason

50

lastRedirectRedirectReason

50

origCalledPartyRedirectOnBehalfOf

14

lastRedirectRedirectOnBehalfOf

14

joinOnBehalfOf

14

IDivert during Connect – 40003 calls 40001, and 40001 answers the call. 40001 decides to divert the caller to the voice-messaging system and presses
                                    the IDivert softkey. 40003 gets diverted to the voice-messaging system 40000.

Because the call gets connected before the redirect, two CDRs get generated: one for the original connected call, and another
                                    for the call that is diverted to the voice-messaging system.

Field Names

Original Connected Call CDR

Diverted Call CDR

globalCallID_callId

38

38

origLegCallIdentifier

16777330

16777330

destLegIdentifier

16777331

16777332

callingPartyNumber

40003

40003

origCalledPartyNumber

40001

40001

finalCalledPartyNumber

40001

40000

lastRedirectDn

40001

40001

origCause_Value

0

16

dest_CauseValue

0

0

origCalledPartyRedirectReason

0

50

lastRedirectRedirectReason

0

50

origCalledPartyRedirectOnBehalfOf

14

lastRedirectRedirectOnBehalfOf

14

origTerminationOnBehalfOf

14

14

destTerminationOnBehalfOf

14

12

joinOnBehalfOf

14

## IMS Application Server

IMS A with calls IMS B through Unified Communications Manager

The incoming invite to Unified Communications Manager contains:

Icid: 5802170000010000000000A85552590A (say, PCV1) and orig_ioi: rcdn-85.swyan.open-ims.test (say, IOI_1).

The INVITE from the Unified Communications Manager to IMS B has the same icid as 5802170000010000000000A85552590A (PCV1), orig_ioi as rcdn-85.swyan.open-ims.test (IOI_1).

When B answers, 200 OK to Unified Communications Manager has icid as 5802170000010000000000A85552590A (PCV1), orig_ioi as rcdn-85.swyan.open-ims.test (IOI_1), and term_ioi, rcdn-86.swyan.open-ims.test
                                    (IOI_2). There could be extra fields with this 200 OK.

The 200 OK from Unified Communications Manager to IMS A has icid 5802170000010000000000A85552590A (PCV1), orig_ioi as rcdn-85.swyan.open-ims.test (IOI_1), and term_ioi
                                    as rcdn-86.swyan.open-ims.test (IOI_2). The extra fields in the 200 OK will be passed to IMS A.

CDR

Side A

Side B

parties

icid

orig_ioi

term_ioi

icid

orig_ioi

term_ioi

A-B

PCV1

IOI_1

IOI_2

PCV1

IOI_1

IOI_2

Fields Names

CDR

globalCallID_callId

3

origLegCallIdentifier

300

destLegIdentifier

301

origDeviceName

CUCM_ISC_TRUNK1

destDeviceName

CUCM_ISC_TRUNK2

IncomingICID

5802170000010000000000A85552590A

IncomingOrigIOI

rcdn-85.swyan.open-ims.test

IncomingTermIOI

rcdn-86.swyan.open-ims.test

OutgoingICID

5802170000010000000000A85552590A

OutgoingOrigIOI

rcdn-85.swyan.open-ims.test

OutgoingTermIOI

rcdn-86.swyan.open-ims.test

## Intercom Calls

The Intercom feature provides one-way audio; therefore, the CDR reflects one-way audio. For talk-back intercom, two-way audio
                              exists, and the CDR reflects two-way audio.

The Intercom feature requires a partition (intercom partition), and existing CDR partition fields get used to identify intercom
                              calls.

The following two examples show CDRs for intercom.

### Intercom CDR Examples

Whisper Intercom - Phone 20000 invokes the intercom. The configured intercom partition name specifies "Intercom."

Field Names

Original Call CDR

globalCallID_callId

1111000

origLegCallIdentifier

21822467

destLegIdentifier

21822468

callingPartyNumber

20000

originalCalledPartyNumber

20001

finalCalledPartyNumber

20001

origCause_Value

16

dest_CauseValue

0

origMediaTransportAddress_IP

0

origMediaTransportAddress_Port

0

destMediaTransportAddress_IP

-47446006

destMediaTransportAddress_Port

28480

origCalledPartyNumberPartition

Intercom

callingPartyNumberPartition

Intercom

finalCalledPartyNumberPartition

Intercom

duration

5

Talk-Back Intercom - Phone 20000 presses the intercom button. 20001 invokes Talk-Back and talks to 20000. The configured intercom partition name
                                    specifies "Intercom."

Field Names

Original Call CDR

globalCallID_callId

1111000

origLegCallIdentifier

21822469

destLegIdentifier

21822470

callingPartyNumber

20000

originalCalledPartyNumber

20001

finalCalledPartyNumber

20001

origCause_Value

16

dest_CauseValue

0

origMediaTransportAddress_IP

-131332086

origMediaTransportAddress_Port

29458

destMediaTransportAddress_IP

-47446006

destMediaTransportAddress_Port

29164

origCalledPartyNumberPartition

Intercom

callingPartyNumberPartition

Intercom

finalCalledPartyNumberPartition

Intercom

duration

5

## IPv6 Calls

Unified Communications Manager supports IPv6 in this release. There are two new fields in the CDR for this feature:

origIpv4v6Addr— This field identifies the IP address of the device that originates the call signaling. The field can be in either IPv4 or
                                    IPv6 format depending on the IP address type that gets used for the call.

destIpv4v6Addr —This field identifies the IP address of the device that terminates the call signaling. The field can be in either IPv4 or
                                    IPv6 format depending on the IP address type that gets used for the call.

The following CDR examples display IPv6 with successful and unsuccessful calls.

### Successful Calls

A talks to B; A hangs up. A is configured as v4_only and B is configured as v4_only. The new fields origIpv4v6Addr and destIpv4v6Addr get populated with the format of their respective v4 addresses.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origIpAddr

352737802

destIpAddr

1878566390

origIpv4v6Addr

10.90.6.21

destIpv4v6Addr

10.90.7.144

duration

60

A talks to B; A hangs up. A is configured as v6_only and B is configured as v6_only. The new fields origIpv4v6Addr anddestIpv4v6Addr get populated with the format of their respective v6 addresses.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origIpAddr

0

destIpAddr

0

origIpv4v6Addr

2001:fecd:ba23:cd1f:dcb1:1010:9234:40881

destIpv4v6Addr

2001:420:1e00:e5:217:8ff:fe5c:2fa9

duration

60

A talks to B; A hangs up. A is configured as v4_only and B is configured as v6_only. The new fields origIpv4v6Addr and destIpv4v6Addr get populated with the format of their respective v4/v6 addresses.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origIpAddr

352737802

destIpAddr

-1878566390

origIpv4v6Addr

10.90.6.21

destIpv4v6Addr

10.90.7.144

duration

60

A talks to B; A hangs up. A is configured as v4_v6 and B is configured as v4_only. In this case, media negotiates v4. The
                                    new fields origIpv4v6Addr and destIpv4v6Addr get populated with the format of their respective v4 addresses.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origIpAddr

352737802

destIpAddr

-1878566390

origIpv4v6Addr

10.90.6.21

destIpv4v6Addr

10.90.7.144

duration

60

A talks to B; A hangs up. A is configured as v4_v6 and B is configured as v6_only. In this case, media negotiates v6. The
                                    new fields origIpv4v6Addr and destIpv4v6Addr get populated with the format of their respective v6 addresses.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origIpAddr

352737802

destIpAddr

0

origIpv4v6Addr

2001:fecd:ba23:cd1f:dcb1:1010:9234:4088

destIpv4v6Addr

2001:420:1e00:e5:217:8ff:fe5c:2fa9

duration

60

### Unsuccessful Calls

A calls B; A abandons the call. A is configured as v4_only and B is configured as v6_only. The new field origIpv4v6Addr gets populated with the format of its v4 address. The new field destIpv4v6Addr does not get populated.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origIpAddr

352737802

destIpAddr

-569419254

origIpv4v6Addr

10.90.15.222

destIpv4v6Addr

duration

0

A calls B; the call fails. A is configured as v6_only and B is configured as v4_v6. The new field origIpv4v6Addr gets populated with the format of its v6 address. The new field destIpv4v6Addr does not get populated in this case.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origIpAddr

0

destIpAddr

0

origIpv4v6Addr

2001:fecd:ba23:cd1f:dcb1:1010:9234:4088

destIpv4v6Addr

duration

0

## Legacy Call Pickup

Legacy Call Pickup calls act similar to forwarded calls. Legacy Call Pickup uses the redirect call control primitive like
                              call forwarding. Some of the important CDR fields for Legacy Call Pickup calls follow:

The originalCallPartyNumber field contains the number of the original called party.

The finalCalledPartyNumber field specifies the number of the party that picks up the call.

The lastRedirectDn field specifies the number that rings when the call gets picked up.

The origCalledPartyRedirectReason field specifies the reason that the call gets redirected the first time. For call pickup calls, this field can contain Call Pickup = 5 .

The lastRedirectRedirectReason field specifies the reason that the call gets redirected the last time. For call pickup, this field can contain Call Pickup = 5 .

The origCalledPartyRedirectOnBehalfOf field identifies which feature redirects the call for the first redirect. For call pickup, this field specifies Pickup = 16 .

The lastRedirectRedirectOnBehalfOf field identifies which feature redirects the call for the last redirect. For call pickup, this field specifies Pickup = 16 .

### Legacy Call Pickup CDR Example

Call from the PSTN to extension 2001; 2001 and 2002 exist in the same pickup group. 2002 picks up the call that rings on 2001.
                              2002 answers the call, and the call connects between the PSTN caller and 2002. They talk for 2 minutes.

Field Names

CDR

globalCallID_callId

22

origLegCallIdentifier

1

destLegIdentifier

2

callingPartyNumber

9728134987

originalCalledPartyNumber

2001

finalCalledPartyNumber

2002

lastRedirectDn

2001

origCause_Value

0

dest_CauseValue

16

origCalledPartyRedirectReason

0

lastRedirectRedirectReason

5

origCalledPartyRedirectOnBehalfOf

16

lastRedirectRedirectOnBehalfOf

16

duration

120

## Local Route Groups and Called Party Transformation

In this release, Unified Communications Manager supports the new feature, local route groups and called party transformation. The device reports the Called Party Number
                              that it outpulsed back to Call Control only if called party transformation occurs. This action gets recorded in the CDR in
                              the new field outpulsedCalledPartyNumber .

### Local Route Groups and Called Party Normalization CDR Example

A call gets placed from an enterprise phone in Dallas to the PSTN; the dialed number specifies 9.5551212.

The translation causes the called party number to take the digits as dialed by the originator, discard PreDot and add the
                              Prefix +1 214.

The finalCalledPartyNumber in the CDR comprises the globally unique E.164 string +12145551212.

If a San Jose gateway gets selected, it transforms the global string +1 214 555 1212 into 12145551212, and if a Dallas gateway
                              gets selected, the global string gets transformed into 2145551212.

The device returns this global string to Call Control as the outpulsedCalledPartyNumber; it gets recorded in the CDR.

The following CDR gets created if the San Jose gateway gets selected.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

+12145551212

finalCalledPartyNumber

2309

lastRedirectDn

2309

origCause_Value

16

dest_CauseValue

0

duration

60

outpulsedCalledPartyNumber

12145551212

The following CDR gets created if the Dallas gateway gets selected.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

+12145551212

finalCalledPartyNumber

+12145551212

lastRedirectDn

+12145551212

origCause_Value

16

dest_CauseValue

0

duration

60

outpulsedCalledPartyNumber

2145551212

## Logical Partitioning Calls

The Telecom Regulatory Authority of India (TRAI) requires that voice traffic over an enterprise data network and a PSTN network
                              remain separate. The logical partitioning feature ensures that a single system can be used to support both types of calls
                              as long as calls that pass through a PSTN gateway can never directly connect to a VoIP phone or VoIP PSTN gateway in another
                              geographic location (geolocation).

### CDR Example for Call Termination Cause Code CCM_SIP_424_BAD_LOCATION_INFO

A SIP trunk call goes from cluster1 to cluster2. The call contains a geolocation header but does not include an XML location.
                              Cluster2 releases the call with a SIP Status code of 424 (bad location information [decimal value = 419430421]).

Cause code CCM_SIP_424_BAD_LOCATION_INFO gets logged for calls that are cleared because of bad location information by the
                              SIP trunk on the Unified Communications Manager . The remote endpoint on the SIP trunk can send the 424 SIP Status code for cases when the geolocation information is bad
                              for some of the following reasons:

The geolocation header indicates the inclusion of PIDF-LO, but the message body does not carry this information.

The geolocation header has a CID header that refers to a URL, but no corresponding Content-IP header with the same URL exists.

The geolocation header has a URL other than the CID header (that is a SIP, or SIPS URL).

Refer to additional CDR examples for more information on other call termination cause codes.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

9900

finalCalledPartyNumber

9900

lastRedirectDn

9900

origCause_Value

0

dest_CauseValue

419430421

duration

0

### CDR Example for Call Termination Cause Code 503

Call 82291002 from cluster1 gets call-forwarded to the PSTN 41549901. A call occurs from cluster2 from DN 89224001 to cluster1
                              DN 82291002. The call gets denied because of logical partitioning with a call termination cause code of CCM_SIP_503_SERVICE_UNAVAIL_SER_OPTION_NOAVAIL
                              [decimal value of -1493172161]) for the dest_CauseValue.

Cause code CCM_SIP_503_SERVICE_UNAVAIL_SER_OPTION_NOAVAIL gets logged for calls that get cleared because of restricted logical
                              partitioning policy checks during the call establishment phase (basic call, call forwarding, call pickup, call park, meet-me
                              conferences, and so forth). Refer to additional CDR examples for more information on other call termination cause codes.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

89224001

originalCalledPartyNumber

82291002

finalCalledPartyNumber

41549901

lastRedirectDn

82291002

origCause_Value

0

dest_CauseValue

-1493172161

duration

0

## Malicious Calls

When a call gets identified as a malicious call (button press), the local Unified Communications Manager network flags the call. The Comment field flags the malicious call.

### Malicious Calls CDR Example

The following table contains an example CDR of a customer call that gets marked as malicious.

Calling Party

Calling Partition

Original Called Party

Original Called Partition

Orig Cause

Dest Cause

Comment

9728552001

CUST

5555

ACNTS

0

16

"callFlag=MALICIOUS"

## Meet-Me Conferences

A meet-me conference occurs when several parties individually dial into a conference bridge at a predetermined time.

The Cisco Secure Conference feature uses the existing callSecuredStatus field to display the highest security status that a call reaches. For meet-me conferences, the system clears calls that try
                              to join the conference but do not meet the security level of the meet-me conference with a terminate cause = 58 (Bearer capability
                              not presently available).

### Meet-Me Conference CDR Example

The following table contains an example CDR for the following scenario. 5001 specifies the dial-in number. The conference
                              bridge device signifies special significance to the Unified Communications Manager , and calls to the conference bridge appear as forwarded calls; that is, UserA phones the predetermined number (5001); the
                              call gets forwarded to a conference bridge port. The conference bridge port appears with a special number of the form "b0019901001."

User A (2001) calls into a meet-me conference bridge with the phone number 5001.

User B (2002) calls into a meet-me conference bridge with the phone number 5001.

User C (2003) calls into a meet-me conference bridge with the phone number 5001.

Calling Party

Calling Partition

Original Called Party

Original Called Partition

Final Called Party

Final Called Partition

Last Redirect Party

Last Redirect Partition

Duration

A

2001

Accounts

5001

b0019901001

b0019901001

70

B

2002

Accounts

5001

b0019901001

b0019901001

65

C

2003

Accounts

5001

b0019901001

b0019901001

80

## Mobility

The following call detail record (CDR) fields apply specifically to Mobility calls. If the call does not invoke a mobility
                              feature, these fields remain empty:

mobileCallingPartyNumber

finalMobileCalledPartyNumber

origMobileDeviceName

destMobileDeviceName

origMobileCallDuration

destMobileCallDuration

mobileCallType

The system generates a standard CDR for every call that uses the Mobility features. When a call gets split, redirected, or
                              joined by the Mobility feature, the corresponding OnBehalfOf code represents a new value that is designated to Mobility. If any of the following OnBehalfOf fields has the Mobility code of 24, the CDR has the Mobility call type:

origCallTerminationOnBehalfOf

destCallTerminationOnBehalfOf

origCalledPartyRedirectOnBehalfOf

lastRedirectRedirectOnBehalfOf

joinOnBehalfOf

### MobileCallType Values

The following table displays the field values for the mobileCallType CDR field. Cisco Analysis and Reporting (CAR) uses the
                              mobileCallType field to determine the CAR call type. If a single call invokes more than one mobility feature, the value of
                              the mobileCallType field represents the integer values added together. For example, if a call uses the Mobile Connect feature
                              and then invokes Hand-Out, the mobile call type will be 136 (8 + 128).

Mobility Feature

mobileCallType Value

Nonmobility call

0

Dial via Office Reverse Callback

1

Dial via Office Forward

2

Reroute remote destination call to enterprise network

4

Mobile Connect

8

Interactive Voice Response

10

Enterprise Feature Access

20

Hand-In

40

Hand-Out

80

Redial

100

Least Cost Routing with dial-via-office reverse callback

200

Least Cost Routing with dial-via-office forward

82

Send call to mobile

800

Session handoff

1000

### Last Redirect Reason

In legacy deployments before 10.0, CAR uses the lastRedirectReason field to identify the mobility call type. The following
                              table shows the Mobility values for lastRedirectReason.

Mobility Feature

lastRedirectReason Value

Hand-In

303

Hand-Out

319

Mobile Connect

335

Redial

351

Interactive Voice Response

399

Dial via Office Reverse Callback

401

Enterprise Feature Access

402

Session Handoff

403

Send call to mobile

415

Reroute remote destination call to enterprise network

783

### Mobility CDR Examples

The following examples demonstrate how mobility features display in CDR records:

Mobile phone initiates Dial via Office Reverse Callback - A mobile phone with a device name of BOTSAU, a mobile number of 2145551234, and an enterprise number of 1000 invokes the
                                    dial-via-office Reverse callback feature to place a call to extension 2000. The MAC address of the called device is SEP001FCAE90004.
                                    The IP address of the SIP gateway is 10.194.108.70. The total call duration is 55 seconds.

Field

Dial via Office Reverse Callback CDR

origCallTerminationOnBehalfOf

0

destCallTerminationOnBehalfOf

12

origCalledRedirectOnBehalfOf

24

lastRedirectOnBehalfOf

24

joinOnBehalfOf

24

origCalledPartyRedirectReason

401

lastRedirectReason

401

origDeviceName

10.194.108.70

destDeviceName

SEP001FCAE9004

finalCalledPartyNumber

2000

huntPilotDN

mobileCallingPartyNumber

2145551234

finalMobileCalledPartyNumber

origMobileDeviceName

BOTSAU

destMobileDeviceName

origMobileCallDuration

55

destMobileCallDuration

mobileCallType

1

Mobile phone initiates Dial via Office Forward - Mobile phone 2145551234 initiates the Dial via Office Forward feature to place a call. The mobile phone has a device name
                                    of BOTSAU and is mapped to enterprise number 1000. The called number is extension 823006 with a device MAC address of SEP001FCAE90004.
                                    The call crosses a SIP gateway at 10.194.108.70 and lasts for a total duration of 120 seconds.

Field

Dial via Office Forward CDR

origCallTerminationOnBehalfOf

0

destCallTerminationOnBehalfOf

12

origCalledRedirectOnBehalfOf

0

lastRedirectOnBehalfOf

0

joinOnBehalfOf

0

origCalledPartyRedirectReason

0

lastRedirectReason

0

origDeviceName

10.194.108.70

destDeviceName

SEP001FCAE90004

finalCalledPartyNumber

823006

huntPilotDN

mobileCallingPartyNumber

2145551234

finalMobileCalledPartyNumber

origMobileDeviceName

BOTSAU

destMobileDeviceName

origMobileCallDuration

120

destMobileCallDuration

0

mobileCallType

2

Call to remote destination is rerouted to enterprise number - Cisco Unified IP Phone SEP001FCAE90004, at extension 2000, dials mobile number 2145551234. The destination mobile phone
                                    is mapped to enterprise number 1000 and has the Reroute Remote Destination Calls to Enterprise Number service parameter enabled
                                    in Unified Communications Manager. Unified Communications Manager reroutes the mobile call to enterprise number 1000. The
                                    call crosses SIP gateway GW_SIP and lasts for a total duration of 60 seconds.

Field

Reroute Remote Detination CDR

origCallTerminationOnBehalfOf

0

destCallTerminationOnBehalfOf

12

origCalledRedirectOnBehalfOf

24

lastRedirectOnBehalfOf

24

joinOnBehalfOf

0

origCalledPartyRedirectReason

783

lastRedirectReason

783

origDeviceName

SEP001FCAE90004

destDeviceName

GW_SIP

finalCalledPartyNumber

1000

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

2145551234

origMobileDeviceName

destMobileDeviceName

2145551234:rdp

origMobileCallDuration

0

destMobileCallDuration

60

mobileCallType

4

Mobile phone invokes deskphone call pickup - Cisco Unified IP Phone SEP001FCAE90004 calls extension 1000, which is shared between a desk phone and a mobile device.
                                    The mobile phone answers the call and then hangs up, triggering the desktop pickup feature. The desktop call pickup timer
                                    runs for about 10 seconds before expiring. After the timer expires, the call is resumed on a Wi-Fi device for another 10 seconds.

Field

Desktop Call Pickup CDR

origCallTerminationOnBehalfOf

0

destCallTerminationOnBehalfOf

12

origCalledRedirectOnBehalfOf

0

lastRedirectOnBehalfOf

0

joinOnBehalfOf

0

origCalledPartyRedirectReason

0

lastRedirectReason

0

origDeviceName

SEP001FCAE90004

destDeviceName

GW_SIP

finalCalledPartyNumber

1000

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

origMobileDeviceName

destMobileDeviceName

origMobileCallDuration

0

destMobileCallDuration

10

mobileCallType

8

Mobile Connect Call - Single Number Reach Voicemail policy set to Timer Control - Cisco Unified IP Phone SEP001FCAE90004, at extension 2000, calls enterprise number 1000. Mobile Connect is invoked and
                                    both the desk phone and mobile phone ring. The mobile phone uses a mobile identity with a device name of BOTSARAH. The Single
                                    Number Reach Voicemail policy is set to Timer Control. The call traverses a SIP gateway and lasts for 10 minutes.

Field

CDR

origCallTerminationOnBehalfOf

0

destCallTerminationOnBehalfOf

12

origCalledRedirectOnBehalfOf

0

lastRedirectOnBehalfOf

0

joinOnBehalfOf

0

origCalledPartyRedirectReason

0

lastRedirectReason

0

origDeviceName

SEP001FCAE90004

destDeviceName

GW_SIP

finalCalledPartyNumber

1000

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

2145551234

origMobileDeviceName

destMobileDeviceName

BOTSARAH

origMobileCallDuration

0

destMobileCallDuration

10

mobileCallType

8

Mobile Connect Call - Single Number Reach Voicemail Policy set to UserControl Mode -Cisco Unified IP Phone SEP001FCAE91231 at enterprise number 238011 calls across a SIP gateway, GW_SIP. The called party
                                    is SEP001FCEA91289, at enterprise number 238006 and mobile number 14089022179. Three CDRs are produced.

Field

Announcement to user

0 Duration Call

IP Phone to Mobile Phone

origCallTerminationOnBehalfOf

24

24

12

destCallTerminationOnBehalfOf

24

24

24

origCalledRedirectOnBehalfOf

24

24

24

lastRedirectOnBehalfOf

24

24

24

joinOnBehalfOf

0

0

24

origCalledPartyRedirectReason

335

335

335

lastRedirectReason

335

335

335

origDeviceName

SEP001FCAE91231

ParkingLotDevice

SEP001FCAE91231

destDeviceName

GW_SIP

GW_SIP

GW_SIP

finalCalledPartyNumber

238006

238006

238006

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

14089022179

14089022179

14089022179

origMobileDeviceName

destMobileDeviceName

14089022179:rdp

14089022179:rdp

14089022179:rdp

origMobileCallDuration

0

0

destMobileCallDuration

3

6

mobileCallType

8

8

8

Mobile phone makes an Enterprise Feature Access (EFA) call with two-stage dialing - Remote destination deepak-RDP, at 4089022179 with shared-line desk phone SEP001EBE90DE95 and enterprise number 238006,
                                    calls internal desk phone SEP001FCAE91231, at enterprise number 238011, using Enterprise Feature Access two-stage dialing.
                                    Total call duration is 30 seconds. Two CDRs are produced: one for the mobile phone dialing the EFA access codes into Unified
                                    Communications Manager and the second for the mobile phone to desk phone conversation.

Field

Mobile Phone to Unified Communications Manager

Mobile Phone to Desk Phone

origCallTerminationOnBehalfOf

24

12

destCallTerminationOnBehalfOf

24

24

origCalledRedirectOnBehalfOf

24

24

lastRedirectOnBehalfOf

24

24

joinOnBehalfOf

24

24

origCalledPartyRedirectReason

402

402

lastRedirectReason

402

402

origDeviceName

GW_SIP

GW_SIP

destDeviceName

ParkingLotDevice

SEP001FCAE91231

finalCalledPartyNumber

00111101001

238011

huntPilotDN

mobileCallingPartyNumber

14089022179

14089022179

finalMobileCalledPartyNumber

origMobileDeviceName

14089022179:rdp

14089022179:rdp

destMobileDeviceName

origMobileCallDuration

5

25

destMobileCallDuration

0

mobileCallType

32

32

Mobile phone makes a Mobile Voice Access call - Remote destination 4089022179, with shared line desk phone SEP001EBE90DE95 at enterprise number 238006, uses Mobile Voice
                                    Access to call an internal desk phone SEP00000000000002 at enterprise number 238011. The remote destination has a remote destination
                                    profile of deepak-rdp. The call traverses SIP gateway GW_SIP and lasts for 60 seconds.

Field

Mobile Phone to Desk Phone

origCallTerminationOnBehalfOf

12

destCallTerminationOnBehalfOf

0

origCalledRedirectOnBehalfOf

24

lastRedirectOnBehalfOf

24

joinOnBehalfOf

24

origCalledPartyRedirectReason

399

lastRedirectReason

399

origDeviceName

GW_SIP

destDeviceName

SEP00000000000002

finalCalledPartyNumber

238011

huntPilotDN

mobileCallingPartyNumber

14089022179

finalMobileCalledPartyNumber

origMobileDeviceName

14089022179:rdp

destMobileDeviceName

origMobileCallDuration

60

destMobileCallDuration

mobileCallType

16

Mobility Hand-In - Cisco Unified IP Phone SEP001FCAE91231 at enterprise number 238011, calls enterprise number 238006, which is unregistered
                                    on the VoIP side, but registered to the smartphone TCTSAU. The mobile identity of the smartphone is 14089022179. At the beginning
                                    of the call TCTSAU is located in a cellular network, but the device moves into Wi-Fi range and the Hand-In feature is invoked
                                    to move the call into the enterprise. The total call duration is 85 seconds, with the called device in Wi-Fi range for the
                                    last 30 seconds.

Field

IP Phone to Cellular Phone

IP Phone to IP Phone

origCallTerminationOnBehalfOf

24

12

destCallTerminationOnBehalfOf

24

24

origCalledRedirectOnBehalfOf

0

0

lastRedirectOnBehalfOf

0

24

joinOnBehalfOf

0

24

origCalledPartyRedirectReason

0

303

lastRedirectReason

0

303

origDeviceName

SEP001FCAE91231

SEP001FCAE91231

destDeviceName

GW_SIP

TCTSAU

finalCalledPartyNumber

238006

238006

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

14089022179

origMobileDeviceName

destMobileDeviceName

TCTSAU

origMobileCallDuration

0

0

destMobileCallDuration

55

mobileCallType

8

72

Mobility Hand-Out - Cisco Unified IP Phone SEP001FCAE94005 at enterprise number 238011, calls a dual-mode smartphone with a mobile identity
                                    of 14089022179, at enterprise number 238006. The smartphone is in local Wi-Fi range when the call is answered and the two
                                    parties speak for 27 seconds. The smartphone moves out of the enterprise network and the call is switched to the cell network,
                                    after which the parties continue to speak for another 25 seconds.

Field

IP Phone to IP Phone

IP Phone to Cell Network

origCallTerminationOnBehalfOf

24

0

destCallTerminationOnBehalfOf

24

12

origCalledRedirectOnBehalfOf

0

0

lastRedirectOnBehalfOf

0

24

joinOnBehalfOf

0

24

origCalledPartyRedirectReason

0

0

lastRedirectReason

0

319

origDeviceName

SEP001FCAE94005

SEP001FCAE94005

destDeviceName

TCTSAU

GW_SIP

finalCalledPartyNumber

238006

238006

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

14089022179

origMobileDeviceName

destMobileDeviceName

TCTSAU

origMobileCallDuration

0

0

destMobileCallDuration

0

23

mobileCallType

0

128

Mobile phone invokes Least Cost Routing Hand-Out using Dial via Office Reverse Callback - A dual-mode phone, BOTSAU, with a mobile identity of 14089022179, is within the enterprise wifi network and registered
                                    to enterprise number 238006. The phone invokes Dial via Office Reverse Callback (DVOR) using least cost routing to call enterprise
                                    number 238011. The two parties speak for 25 seconds, but the mobile phone moves out of Wi-Fi range, triggering the handout
                                    feature to the cellular network. On the cell network, the two parties speak for another 35 seconds.

Field

DVOR callback

IP phone to IP phone

Mobile phone to IP phone

origCallTerminationOnBehalfOf

24

24

0

destCallTerminationOnBehalfOf

24

24

12

origCalledRedirectOnBehalfOf

0

0

0

lastRedirectOnBehalfOf

0

0

24

joinOnBehalfOf

0

0

24

origCalledPartyRedirectReason

0

0

0

lastRedirectReason

0

0

319

origDeviceName

ParkingLotDevice

BOTSAU

GW_SIP

destDeviceName

GW_SIP

SEP001FCAE91231

SEP001FCAE91231

finalCalledPartyNumber

238006

238011

238011

huntPilotDN

mobileCallingPartyNumber

14089022179

finalMobileCalledPartyNumber

14089022179

origMobileDeviceName

BOTSAU

destMobileDeviceName

BOTSAU

origMobileCallDuration

0

0

35

destMobileCallDuration

0

0

mobileCallType

0

0

512

Mobile Phone invokes Least Cost Routing Hand-Out using Dial via Office Forward - A dual-mode phone, BOTSAU, with a mobile number of 14089022179, is mapped to enterprise number 238006 and is within Wi-Fi
                                    range of the enterprise. The phone invokes Dial via Office Forward with least cost routing to place a call to enterprise number
                                    238011, which is registered to a Cisco Unified IP Phone SEP001FCAE91006. The two parties talk for 30 seconds before the mobile
                                    phone moves out of Wi-Fi range and the call is handed out to the cell network, following which the call continues for another
                                    25 seconds.

Field

IP Phone to IP Phone

Mobile Phone to IP Phone

origCallTerminationOnBehalfOf

24

12

destCallTerminationOnBehalfOf

24

0

origCalledRedirectOnBehalfOf

0

0

lastRedirectOnBehalfOf

0

24

joinOnBehalfOf

0

24

origCalledPartyRedirectReason

0

0

lastRedirectReason

0

319

origDeviceName

BOTSAU

GW_SIP

destDeviceName

SEP001FCAE91006

SEP001FCAE91006

finalCalledPartyNumber

238011

238011

huntPilotDN

mobileCallingPartyNumber

14089022179

finalMobileCalledPartyNumber

origMobileDeviceName

BOTSAU

destMobileDeviceName

origMobileCallDuration

0

0

destMobileCallDuration

0

25

mobileCallType

0

130

Send Call to Mobile - A Cisco Unified IP Phone SEP001FCAE90001 at 238011, makes a call to enterprise number 238006. The called party answers
                                    the call on Cisco Unified IP Phone SEP001FCAE90022. The conversation continues for 45 seconds before the called party presses
                                    the Mobility softkey to send the call to the mobile phone, BOTSAU, at 12145551234. The call continues on the mobile phone
                                    for another 35 seconds. The total call duration is 55 seconds.

Field

Announcement

IP Phone to IP Phone

IP Phone to Mobile Phone

origCallTerminationOnBehalfOf

24

24

24

destCallTerminationOnBehalfOf

24

24

12

origCalledRedirectOnBehalfOf

0

0

0

lastRedirectOnBehalfOf

0

0

24

joinOnBehalfOf

0

0

24

origCalledPartyRedirectReason

0

0

0

lastRedirectReason

0

0

415

origDeviceName

SEP001FCAE90001

SEP001FCAE90001

SEP001FCAE90001

destDeviceName

GW_SIP

SEP001FCAE90022

GW_SIP

finalCalledPartyNumber

238006

238006

238006

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

12145551234

12145551234

origMobileDeviceName

destMobileDeviceName

BOTSAU

BOTSAU

origMobileCallDuration

0

0

0

destMobileCallDuration

0

0

35

mobileCallType

0

0

2048

Session Handoff - Cisco Unified IP Phone SEP001FCAE90001, at extension 1000, calls extension 2500. The phone rings at both a desk phone and
                                    a mobile phone. The called party answers on a mobile phone, BOTSAU at mobile number 2145551234 and a conversation begins.
                                    After 35 seconds, the called party triggers the Session Handoff feature and transfers the call to a desk phone. The call continues
                                    on desk phone SEP001FCAE90022 for another 60 seconds.

Field

Parking Lot to Desk Phone

IP Phone to Mobile Phone

IP Phone to IP Phone

origCallTerminationOnBehalfOf

24

24

24

destCallTerminationOnBehalfOf

24

24

12

origCalledRedirectOnBehalfOf

0

0

0

lastRedirectOnBehalfOf

0

0

24

joinOnBehalfOf

0

0

24

origCalledPartyRedirectReason

0

0

0

lastRedirectReason

0

0

403

origDeviceName

SEP001FCAE90001

SEP001FCAE90001

SEP001FCAE90001

destDeviceName

SEP001FCAE90022

BOTSARAH

SEP001FCAE90022

finalCalledPartyNumber

2500

2500

2500

huntPilotDN

mobileCallingPartyNumber

finalMobileCalledPartyNumber

2145551234

origMobileDeviceName

destMobileDeviceName

BOTSARAH

origMobileCallDuration

0

0

0

destMobileCallDuration

0

15

10

mobileCallType

0

0

5096

## Native Call Queuing

The Native Call Queuing feature provides an enhanced capability to handle incoming calls to a hunt pilot number. Unified Communications
                              Manager provides call queuing natively to users so that callers can be held in a queue until hunt members are available to
                              answer them. Callers in a queue receive an initial greeting announcement followed by music on hold or tone on hold. If the
                              caller remains in a queue for time, a secondary announcement is played at a configured interval until the call can be answered—or
                              until the maximum wait timer expires.

### Native Call Queuing Example

Unified Communications Manager cluster has four IP Phones: DN 1000, 1001, 1002, and 1003.

A hunt pilot (HP) 2000 is created with line group DN 1000 associated with it. So, this hunt pilot 2000 can only handle one
                              call. Now, Check the "Queuing" enabled flag on the hunt pilot 2000 configuration page. Set the "Max Call Waiting Timer" to be 30 seconds, and select "Route the call to this destination" to be DN 1003. Ideally, if a caller has been put into that queue for 30 seconds, then it will be routed to DN 1003.

DN 1001 calls HP 2000, and 1000 answers the call.

DN 1002 calls HP 2000. Since the agent is busy, call is queued.

After 30 seconds, call is routed to DN 1003.

DN 1003 answers the call.

Field Names

CDR

globalCallID_callId

87029

origLegCallIdentifier

30117105

callingPartyNumber

1002

originalCalledPartyNumber

2000

wasCallQueued

1

totalWaitTimeInQueue

30

## Normal Calls (Cisco Unified IP Phone to Cisco Unified IP Phone)

Normal calls log three records per call; one CDR and two CMRs, one for each endpoint. In the CDR, the "originalCalledPartyNumber" field contains the same Directory Number as the "finalCalledPartyNumber" field.

### Successful Normal Calls CDR Examples

A successful call between two Cisco Unified IP Phone s generates a single CDR at the end of the call.

The caller terminates a 60-second call. Because the calling party hangs up, the orig_CauseValue specifies 16 (Normal Clearing).

Field Names

CDR

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origCause_Value

16

dest_CauseValue

0

duration

60

The called party clears a 60-second call. Because the called party hangs up, the dest_CauseValue specifies 16 (Normal Clearing).

Field Names

CDR

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

2001

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origCause_Value

0

dest_CauseValue

16

duration

60

## Original Calling Party on Transfer

This feature changes the calling party number for a consultation call of a Cisco Unity or Cisco Unity Connection -initiated call transfer. The CDR of the consultation call shows that the original caller calls the transfer destination,
                              not that the Cisco Unity or Cisco Unity Connection port calls the transfer destination.

You must configure this feature in the service parameters in Unified Communications Manager . See additional information at "Configuring CDR Service Parameters" section of the CDR Analysis and Reporting Administration Guide .

### Original Calling Party on Transfer CDR Example

4001 calls 4002. 4002 transfers the call to 4003. The system generates three CDRs:

The call between the original parties (4001 to 4002).

The consultation call between the transferring party (4002) to the final transfer destination (4003).

The call from the transferred party (4001) to the transfer destination (4003).

Call

CallingPartyNumber

originalCalledPartyNumber

1

4001

4002

2

4002

4003

3

4001

4003

No originalCallingParty field exists in the CDR.

## Personal Assistant Calls

This section contains information about Personal Assistant Calls.

### Personal Assistant Direct Call

A personal assistant direct call acts similar to the Blind Transfer from the Calling Party call type.

#### Personal Assistant Direct Call CDR Example

The following table contains an example CDR for this scenario:

User A (2101) calls a Personal Assistant route point (2000) and says "call User B."

The call transfers to User B (2105). In this case, User B did not configure any rules.

In the following example, 2000 represents the main personal assistant route point to reach personal assistant, 21XX represents
                                             the personal assistant interceptor route point, and 2001-2004 represents the media port.

In all cases, 2101 specifies the calling number.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2101

16777217

PAManaged

16777219

2004

Phones

2000

1023970182

2000

Phones

34

2004

16777221

Phones

16777222

2105

PAManaged

2105

1023970182

2105

PAManaged

0

2101

16777217

PAManaged

16777222

2105

PAManaged

2105

1023970191

2105

PAManaged

5

### Personal Assistant Interceptor Going to Media Port and Transferring Call

This scenario acts similar to Blind Transfer from the Calling Party and Forwarded Calls actions.

#### Personal Assistant Interceptor Going to Media Port and Transferring the Call CDR Example

The following table contains an example CDR for this scenario:

User A (2101) dials 2105.

The personal assistant interceptor (21XX) picks up the call and redirects it to a media port (2002).

Personal assistant processes the call according to the rules (if any) and transfers the call to the destination (2105), which
                                       has not configured any rules.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2002

16777234

Phones

16777285

2105

PAManaged

2105

1023970478

2105

PAManaged

2

2101

16777230

PAManaged

16777232

2002

PA

2105

1023970478

21xx

" "

9

2105

16777235

PAManaged

16777230

2101

" "

" "

1023970483

" "

" "

5

### Personal Assistant Interceptor Going Directly to Destination

This scenario can have two different cases: with rules and with no rules.

#### Example Personal Assistant Interceptor Going Directly to Destination with No Rules CDR

The following table contains an example CDR for this scenario:

User A (2101) dials 2105.

The personal assistant interceptor (21XX) picks up the call, processes it according to the rules (if any), and redirects the
                                          call to the destination (2105).

The following table contains an example CDR for this scenario:

Calling Party Number

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Number

FinalCalled Party Number Partition

Original Called Party Number

Original Called Party Number Partition

Last Redirect DN

Last Redirect DN Partition

Duration(secs)

2101

16777240

PAManaged

16777242

2105

PA

2105

1023970710

21XX

" "

8

#### Example Personal Assistant Going Directly to Destination with Rule to Forward Calls to Different Destination CDR

The following table contains an example CDR for this scenario:

User A (2101) dials 2105.

The Personal Assistant interceptor (21XX) picks up the call and processes it according to the rules.

The Personal Assistant interceptor then redirects the call to the final destination (2110). In this case, 2105 configured
                                          a rule to forward the call to extension 2110.

Calling Party Number

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Number

FinalCalled Party Number Partition

Original Called Party Number

Original Called Party Number Partition

Last Redirect DN

Last Redirect DN Partition

Duration(secs)

2101

16777240

PAManaged

16777242

2110

PA

2105

1023970710

21XX

" "

8

### Personal Assistant Interceptor Going to Multiple Destinations

This scenario can have several different cases. In each case, User B (2105) configures a rule to reach him at extension 2110
                                 or 2120. This rule can activate when a caller calls Personal Assistant route point (2000) and says "call User B" (direct case) or when the caller dials User B (2105) directly (interceptor case).

#### Personal Assistant Interceptor Going to Multiple Destinations CDR Examples

The following sections contain examples of each case. The following tables contain example CDRs for each of these scenarios:

Personal assistant direct multiple destinations: 2110 and 2120 (call accepted at first destination)

Personal assistant direct multiple destinations: 2110 and 2120 (call accepted at second destination)

Personal assistant direct multiple destinations: 2110 and 2120 (call accepted at third destination)

Personal assistant intercept multiple destinations: 2110 and 2120 (call accepted at first destination)

Personal assistant intercept multiple destinations: 2110 and 2120 (call accepted at second destination)

Personal assistant intercept multiple destinations: 2110 and 2120 (call accepted at third destination)

#### Personal Assistant Direct Multiple Destinations: 2110 and 2120 (Call Accepted at First Destination)

User A calls personal assistant and says, "call User B."

User B answers the call at 2110 extension.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2004

16777262

Phones

16777263

2110

PAManaged

2110

1023971303

2110

PAManaged

6

2101

16777258

PAManaged

16777260

2004

Phones

2000

1023971303

2000

Phones

22

2110

16777263

PAManaged

16777258

2101

" "

" "

1023971312

" "

" "

9

#### Personal Assistant Direct Multiple Destinations: 2110 and 2120 (Call Accepted at Second Destination)

User A calls personal assistant and says, "call User B."

User B answers the call at 2120 extension.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2001

16777269

Phones

16777270

2110

PAManaged

2110

1023971456

2110

PAManaged

0

2001

16777272

Phones

16777273

2120

PAManaged

2120

1023971467

2120

PAManaged

4

2101

16777265

PAManaged

16777267

2001

Phones

2000

1023971467

2000

Phones

37

2120

16777273

PAManaged

16777265

2101

" "

" "

1023971474

" "

" "

7

2110

16777275

PAManaged

0

" "

" "

" "

1023971476

" "

" "

0

#### Personal Assistant Direct Multiple Destinations: 2110 and 2120 (Call Accepted at Third Destination)

User A calls personal assistant and says, "call User B."

User B does not answer at either extension 2110 or 2120.

Personal Assistant transfers the call to the original destination (2105), and User B then answers at that extension.

2105 (the original destination) represents the third destination in this case.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2002

16777281

Phones

16777282

2110

PAManaged

2110

1023971602

2110

PAManaged

0

2002

16777284

Phones

16777285

2120

PAManaged

2120

1023971615

2120

PAManaged

0

2101

16777277

PAManaged

16777279

2002

Phones

2000

1023971619

2000

Phones

38

2002

16777287

Phones

16777288

2105

PAManaged

2105

1023971619

2105

PAManaged

0

2101

16777277

PAManaged

16777288

2105

PAManaged

2105

1023971627

2105

PAManaged

7

2105

16777289

PAManaged

0

" "

" "

" "

1023971629

" "

" "

0

#### Personal Assistant Intercept Multiple Destinations: 2110 and 2120 (Call Accepted at First Destination)

User A calls personal assistant and says, "call User B."

User B answers the call at extension 2110.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2003

16777295

Phones

16777296

2110

PAManaged

2110

1023971740

2110

PAManaged

4

2101

16777291

PAManaged

16777293

2003

PA

2105

1023971740

21XX

" "

10

2110

16777296

PAManaged

16777291

2101

" "

" "

1023971749

" "

" "

9

#### Personal Assistant Intercept Multiple Destinations: 2110 and 2120 (Call Accepted at Second Destination)

User A calls personal assistant and says, "call User B."

User B answers the call at extension 2120.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2004

16777302

Phones

16777303

2110

PAManaged

2110

1023971815

2110

PAManaged

0

2004

16777305

Phones

16777306

2120

PAManaged

2120

1023971824

2120

PAManaged

3

2101

16777298

PAManaged

16777300

2004

PA

2105

1023971824

21XX

" "

22

2120

16777306

PAManaged

16777298

2101

" "

" "

1023971832

" "

" "

8

#### Personal Assistant Intercept Multiple Destinations: 2110 and 2120 (Call Accepted at Third Destination)

User A calls personal assistant and says, "call User B."

User B does not answer at either extension 2110 or 2120.

Personal assistant transfers the call to the original destination (2105), which User B then answers.

2110 (the original destination) represents the third destination in this case.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

Original Called Party Num

Original Called Party Number Partition

Last Redir DN

Last Redirect DN Partition

Duration (secs)

2001

16777312

Phones

16777313

2110

PAManaged

2110

1023971923

2110

PAManaged

0

2001

16777315

Phones

16777316

2120

PAManaged

2120

1023971936

2120

PAManaged

0

2101

16777308

PAManaged

16777310

2001

PA

2105

1023971940

21XX

" "

30

2001

16777318

Phones

16777319

2105

PAManaged

2105

1023971940

2105

PAManaged

0

2101

16777308

PAManaged

16777319

2105

PAManaged

2105

1023971953

2105

PAManaged

12

### Personal Assistant Conferencing

Personal assistant conferencing acts similar to the ad hoc conferences call type.

#### Personal Assistant Conferencing CDR Example

The following table contains an example CDR for this scenario:

User A calls personal assistant route point (2000) and says, "conference User B (2105) and User C (2110)."

Personal assistant conferences User B and C into User A conference.

Calling Party Num

OrigLegCall Identifier

Calling Party Number Partition

DestLeg Identifier

Final Called Party Num

Final Called Party Number Partition

2003

16777345

Phones

16777346

2105

PAManaged

2101

16777340

PAManaged

16777342

2003

Phones

2003

16777350

Phones

16777351

2002

PAManaged

2003

16777342

Phones

16777347

2110

" "

2110

16777351

PAManaged

16777352

b00110201001

" "

2105

16777346

PAManaged

16777349

b00110201001

" "

2101

16777340

PAManaged

16777348

b00110201001

" "

This table continues with this additional information.

Original CalledParty Number

Original Called Party Number Partition

Last Redirect DN

Last Redirect DN Partition

Duration (seconds)

2105

1023972575

2105

PAManaged

6

2000

1023972576

2003

Phones

62

2110

1023972595

2110

PAManaged

39

b00110201001

1023972601

b00110201001

" "

25

b00110201001

1023972609

b00110201001

" "

14

b00110201001

1023972610

b00110201001

" "

34

b00110201001

1023972610

b00110201001

" "

34

## Precedence Calls (MLPP)

Precedence calls take place the same as other calls except the precedence level fields get set in the CDR. Also, when a higher
                              level precedence call preempts a call, the cause codes indicate the reason for the preemption.

### Precedence Call CDR Examples

A call to another IP phone occurs by dialing a precedence pattern (precedence level 2).

Field Names

Precedence Call CDR

globalCallID_callId

100

origLegCallIdentifier

12345

destLegIdentifier

12346

callingPartyNumber

2001

origCalledPartyNumber

826001

origCause_Value

0

dest_CauseValue

16

origPrecedenceLevel

2

destPrecedenceLevel

2

A precedence call gets received from another network (precedence level 1).

Field Names

Precedence Call CDR

globalCallID_callId

102

origLegCallIdentifier

11111

destLegIdentifier

11112

callingPartyNumber

9728552001

origCalledPartyNumber

6001

origCause_Value

16

dest_CauseValue

0

origPrecedenceLevel

1

destPrecedenceLevel

1

A call gets preempted by a higher precedence level call.

Field Names

Original call CDR

Higher Level Call CDR

globalCallID_callId

10000

10001

origLegCallIdentifier

12345678

12345680

destLegIdentifier

12345679

12345681

callingPartyNumber

2001

9728551234

origCalledPartyNumber

826001

826001

origCause_Value

0

0

dest_CauseValue

9

16

origPrecedenceLevel

2

1

destPrecedenceLevel

2

1

## Redirection (3xx) Calls

This example shows CDRs for the redirection feature (3xx).

When a call is redirected by the Redirection Feature (3xx), the origCalledPartyRedirectOnBehalfOf and lastRedirectRedirectOnBehalfOf fields specify UnifiedCM Redirection = 19. The origCalledPartyRedirectReason and the lastRedirectRedirectReason fields specify Redirection = 162.

### Redirection (3xx) CDR Example

Activate CFA on phone 10010 that is running SIP (registered to Unified Communications Manager ) with a CFA destination of 10000. 35010 calls 10010, which is CFA to 10000. The call gets redirected from 10010 to 10000.
                              10000 answers the call and talks for 1minute.

Field Names

Original Call CDR

globalCallID_callId

11

origLegCallIdentifier

21832023

destLegIdentifier

21832026

callingPartyNumber

35010

originalCalledPartyNumber

10010

finalCalledPartyNumber

10000

lastRedirectDn

10010

origCause_Value

0

dest_CauseValue

16

origCalledPartyRedirectReason

162

lastRedirectRedirectReason

162

origCalledPartyRedirectOnBehalfOf

19

lastRedirectRedirectOnBehalfOf

19

origTerminationOnBehalfOf

0

destTerminationOnBehalfOf

12

joinOnBehalfOf

19

duration

60

## Redirecting Number Transformation

When the redirecting number transformation feature is enabled, original called and last redirecting number are transformed
                              before it sends out in outgoing setup message.

### Redirecting Number Transformation Example

CCM1 - Phone A [ 180000 ] , Phone B [ 180001 ] , Phone C [ 180002 ]

SIP trunk is configured on CCM1 pointing to SIP Gateway

Phone B has external mask set as +9111XXXX

Phone C has external mask set as +9122XXXX

On SIP trunk, redirecting party CSS is configured which has the partitions P1 and there is a Calling Party transformation
                              pattern associated with P1. This pattern has external phone number mask enabled.

Scenario

A - calls Phone B ---- CFA - Phone C CFA --- SIP Trunk --- SIP Gateway

B - Original Called Party, C - Last Redirecting Party

There are 2 diversion headers corresponding to original and last redirecting party that is sent out in outgoing SIP INVITE
                              message and these diversion headers have transformed redirecting number, that is, +91110001 and +91220002.

These values are also stored in CDR records. Transformed original called number will be stored in outpulsedOriginalCalledPartyNumber
                              and transformed last redirecting number will be stored in outpulsedLastRedirectingNumber.

Field Names

CDR

globalCallID_callId

115010

origLegCallIdentifier

30751507

callingPartyNumber

180000

outpulsedCallingPartyNumber

880003

outpulsedOriginalCalledPartyNumber

+91110001

outpulsedLastRedirectingNumber

+91220002

## Refer Calls

See the replaces calls topic for an example of Refer with Replaces.

## Replaces Calls

The examples show CDRs for various types of Replaces calls.

### Replaces CDR Examples

Invite with Replaces – Phone 35010 that is running SIP calls phone 35020 that is running SIP. The transfer button gets pressed on 35010, and a
                                    call gets placed to SCCP phone 3000, 3000 answers the call; then, phone 35010 completes the transfer. The final transferred
                                    call occurs between 35020 and 3000.

When the transfer is complete, the system sends an Invite with Replaces to Unified Communications Manager .

Field Names

Original Call CDR

Reverted Call CDR

globalCallID_callId

5045247

5045248

origLegCallIdentifier

21822467

21822469

destLegIdentifier

21822468

21822468

callingPartyNumber

35010

35020

originalCalledPartyNumber

3000

3000

finalCalledPartyNumber

3000

3000

lastRedirectDn

3000

35010

origCause_Value

393216

0

dest_CauseValue

393216

16

origCalledPartyRedirectReason

0

0

lastRedirectRedirectReason

0

146

origCalledPartyRedirectOnBehalfOf

0

0

lastRedirectRedirectOnBehalfOf

0

18

origTerminationOnBehalfOf

18

0

destTerminationOnBehalfOf

18

12

joinOnBehalfOf

0

18

duration

5

60

Refer with Replaces – Phone 35010 that is running SIP calls SCCP 3000, the transfer button gets pressed on 35010, and a call is placed to SCCP
                                    3001; 3001 answers the call; then, phone 35010 completes the transfer. The final transferred call occurs between 3000 and
                                    3001.

When the transfer completes, a Refer with Replaces gets sent to Unified Communications Manager .

Field Names

Original Call CDR

Consultation Call CDR

Final Transferred Call CDR

globalCallID_callId

5045245

5045246

5045245

origLegCallIdentifier

21822461

21822463

21822462

destLegIdentifier

21822462

21822464

21822464

callingPartyNumber

35010

35010

3000

originalCalledPartyNumber

3000

3001

3001

finalCalledPartyNumber

3000

3001

3001

lastRedirectDn

3000

3001

35010

origCause_Value

393216

393216

16

dest_CauseValue

393216

393216

0

origCalledPartyRedirectReason

0

0

130

lastRedirectRedirectReason

0

0

146

origCalledPartyRedirectOnBehalfOf

0

0

17

lastRedirectRedirectOnBehalfOf

0

0

18

origTerminationOnBehalfOf

17

18

12

destTerminationOnBehalfOf

17

18

17

joinOnBehalfOf

0

0

18

duration

25

4

25

## RSVP

These fields identify the status of RSVP reservation for the call. Be aware that the Unified Communications Manager RSVP CDR status field value gets concatenated, and the system retains the last 32 status values for the call.

For example, if a call is established with "Optional" policy, and the initial RSVP reservation is successful, and then it subsequently loses its bandwidth reservation and then
                              regains its bandwidth reservation after retry, for several times during middle of the call, the call ends with a successful
                              RSVP reservation. The CDR shows the following string as the UnifiedCommunication RSVP reservation status for that particular
                              stream: "2:5:2:5:2:5:2" (success:lost_bw:success:lost_bw:success:lost_bw:success).

### RSVP Call CDR Examples

The example represents a call that gets established with "Optional" policy, and the initial RSVP reservation succeeds. The parties talk for 5minutes.

Field Names

CDR

globalCallID_callId

300

origLegCallIdentifier

16777300

destLegIdentifier

16777301

callingPartyNumber

20000

origCalledPartyNumber

20001

finalCalledPartyNumber

20001

lastRedirectDn

20001

origCause_Value

0

dest_CauseValue

16

origDTMFMethod

2

destDTMFMethod

2

duration

300

The example represents a call that is established with "Optional" policy, and the initial RSVP reservation succeeds, then it loses its bandwidth reservation but regains it after a retry.
                                    The parties talk for 1minute.

Field Names

CDR

globalCallID_callId

301

origLegCallIdentifier

16777302

destLegIdentifier

16777303

callingPartyNumber

20000

origCalledPartyNumber

20001

finalCalledPartyNumber

20001

lastRedirectDn

20001

origCause_Value

0

dest_CauseValue

16

origDTMFMethod

2:5:2

destDTMFMethod

2:5:2

duration

60

## Secure Conference Meet-Me

The following example shows a CDR for a meet-me secure conference. 35010 calls into a secure meet-me conference, but 35010
                              is a non-secure phone. Because 35010 does not meet the minimum security level of the meet-me conference, the call gets cleared
                              with the cause code of 58 (meet-me conference minimum security level not met).

### Secure Conference Meet-Me CDR Example

Field Names

Call to the Meet-Me Conference CDR

globalCallID_callId

5045247

origLegCallIdentifier

123456879

destLegIdentifier

123456999

callingPartyNumber

35010

originalCalledPartyNumber

50000

finalCalledPartyNumber

50000

lastRedirectDn

50000

origCause_Value

58

dest_CauseValue

0

origCalledPartyRedirectReason

0

lastRedirectRedirectReason

0

origCalledPartyRedirectOnBehalfOf

0

lastRedirectRedirectOnBehalfOf

0

origTerminationOnBehalfOf

6

destTerminationOnBehalfOf

6

## Short Calls

A short call, with a CdrLogCallsWithZeroDurationFlag set at True and a duration of less than 1second, appears as a zero duration call in the CDR. The DateTimeConnect field, which shows the actual connect time of the call, differentiates these calls from failed calls. For failed calls (which
                              never connected), this value equals zero.

### Short Calls CDR Example

The following table contains an example of a successful On Net call with a duration of less than 1second that the called party
                              cleared.

Calling

Party

Calling

Partition

Original CalledParty

Original CalledPartition

Orig Cause

Dest Cause

DateTime Connect

Duration

2001

Accounts

2309

Marketing

0

16

973795815

0

## SIP Call with URL in CallingPartyNumber Field

Calling and called parties can have SIP calls where the extension number is a URL. The extension number can use all printable
                              ASCII characters. Do not leave any spaces in the URL. For example, extension "1000 1001" does not get accepted as a valid URL.

Printable ASCII characters represent characters with ASCII code (in decimal) from 33 to 126.

### SIP Call with URL in CallingPartyNumber Field CDR Example

The SIP trunk of the Unified Communications Manager receives an incoming call. The call contains a SIP URL for the callingPartyNumber.

Field Names

Values

globalCallID_callId

1

origLegCallIdentifier

100

destLegIdentifier

101

callingPartyNumber

bob@abc.com

originalCalledPartyNumber

2309

finalCalledPartyNumber

2309

lastRedirectDn

2309

origCause_Value

16

dest_CauseValue

0

duration

60

## Successful on Net Calls

A successful call between two Cisco Unified IP Phone s generates a single CDR at the end of the call.

### Successful On Net Call CDR Examples

The following table contains two examples:

A—A 60-second call that the caller terminates

B—A 60-second call that the called party clears

Calling

Party

Calling

Partition

Original Called Party

Original Called Partition

Orig Cause

Dest Cause

Duration

A

2001

Accounts

2309

Marketing

16

0

60

B

2001

Accounts

2309

Marketing

0

16

60

## Transferred Calls

Calls that are transferred generate multiple CDRs. One CDR exists for the original call, one for the consultation call, and
                              another for the final transferred call.

For the original call, the origCause_value and destCause_value gets set to split = 393216, which indicates the call was split. The origCallTerminationOnBehalfOf and destCallTerminationOnBehalfOf fields get set to Transfer = 10 to indicate that this call was involved in a transfer.

For the consultation call, the origCause_value and destCause_value fields get set to split = 393216, which indicates that the call was split. The origCallTerminationOnBehalfOf and destCallTerminationOnBehalfOf fields get set to Transfer = 10 to indicate that this call was involved in a transfer.

For the final transferred call, the joinOnBehalfOf field gets set to Transfer = 10 to indicate that this call resulted from a transfer.

### Transferred Calls CDR Examples

The following examples, which are not an exhaustive set, illustrate the records that would be generated under the stated circumstances.
                              These examples help clarify what records are generated on transferred calls.

### Blind Transfer From the Calling Party CDR Example

Call goes from extension 2001 to a PSTN number; they talk for 120 seconds. 2001 initiates a blind transfer to 2002. CDR 1 (original call) shows a call from extension 2001 to a PSTN number, talking for 120 seconds. CDR 2 (consultation call) shows a call from 2001 to extension 2002. CDR 3 represents the final transferred call where 2001 completes the transfer, drops out of the call, and leaves a call between
                              the PSTN and 2002.

Field Names

Original Call CDR

Consultation Call CDR

Final Transferred CDR

globalCallID_callId

1

2

1

origLegCallIdentifier

101

103

102

destLegIdentifier

102

104

104

callingPartyNumber

2001

2001

3071111

originalCalledPartyNumber

3071111

2002

2002

finalCalledPartyNumber

3071111

2002

2002

lastRedirectDn

3071111

2002

2001

origCause_Value

393216

393216

16

dest_CauseValue

393216

393216

0

origTerminationOnBehalfOf

10

10

0

destTerminationOnBehalfOf

10

10

0

joinOnBehalfOf

0

0

10

duration

120

0

360

### Consultation Transfer From the Calling Party CDR Example

Call goes from extension 2001 to a PSTN number; they talk for 60 seconds. 2001 initiates a consultation transfer to 2002 and
                              talks for 10 seconds before the transfer completes. The final transferred call talks for 360 seconds. CDR 1 (original call) shows a call from extension 2001 to a PSTN number, talking for 60 seconds. CDR 2 (consultation call) shows a call from 2001 to extension 2002, talking for 10 seconds. CDR 3 represents the final transferred call where 2001 completes the transfer, drops out of the call, and leaves a call between
                              the PSTN and 2002.

Field Names

Original Call CDR

Consultation Call CDR

Final Transferred Call CDR

globalCallID_callId

1

2

1

origLegCallIdentifier

111

113

112

destLegIdentifier

112

114

114

callingPartyNumber

2001

2001

3071111

originalCalledPartyNumber

3071111

2002

2002

finalCalledPartyNumber

3071111

2002

2002

lastRedirectDn

50001

50001

2001

origCause_Value

393216

393216

16

dest_CauseValue

393216

393216

0

origTerminationOnBehalfOf

10

10

0

destTerminationOnBehalfOf

10

10

0

joinOnBehalfOf

0

0

10

duration

60

10

360

### Blind Transfer From the Called Party CDR Example

Call goes from 50000 to 50001; they talk for 120 seconds. 50001 initiates a blind transfer to 50002. CDR 1 (original call) shows a call from extension 50001 to 50002, talking for 120 seconds. CDR 2 (consultation call) shows a call from 50001 to extension 50002. CDR 3 represents the final transferred call where 50001 completes the transfer, drops out of the call, and leaves a call between
                              50000 and 50002.

Field Names

Original Call CDR

Consultation Call CDR

Final Transferred Call CDR

globalCallID_callId

1

2

1

origLegCallIdentifier

200

202

200

destLegIdentifier

201

203

203

callingPartyNumber

50000

50001

50000

originalCalledPartyNumber

50001

50002

50002

finalCalledPartyNumber

50001

50002

50002

lastRedirectDn

50001

50001

50001

origCause_Value

393216

393216

16

dest_CauseValue

393216

393216

0

origTerminationOnBehalfOf

10

10

0

destTerminationOnBehalfOf

10

10

0

joinOnBehalfOf

0

0

10

duration

120

0

360

### Consultation Transfer From the Called Party CDR Example

Call goes from 50000 to 50001; they talk for 120 seconds. 50000 initiates a blind transfer to 50002. CDR1 (original call) shows a call from extension 50000 to a 50001, talking for 120 seconds. CDR2 (consultation call) shows a call from 50000 to extension 50002. CDR3 represents the final transferred call where 50000 completes the transfer, drops out of the call, and leaves a call between
                              50001 and 50002.

Field Names

Original Call CDR

Consultation Call CDR

Final Transferred Call CDR

globalCallID_callId

1

2

1

origLegCallIdentifier

200

202

201

destLegIdentifier

201

203

203

callingPartyNumber

50000

50001

50000

originalCalledPartyNumber

50001

50002

50002

finalCalledPartyNumber

50001

50002

50002

lastRedirectDn

50001

50001

50001

origCause_Value

393216

393216

16

dest_CauseValue

393216

393216

0

origTerminationOnBehalfOf

10

10

0

destTerminationOnBehalfOf

10

10

0

joinOnBehalfOf

0

0

10

duration

120

0

360

## Video Calls

The following example shows a CDR for a video call.

### Video Calls CDR Example

Calling party 51234 calls the called party 57890. In the following example, let 100 = H.261, 187962284=172.19.52.11, 288625580=172.19.52.17,
                              320=320K, and 2=QCIF.

Field Names

Video Call CDR

globalCallID_callId

121

origLegCallIdentifier

101

destLegIdentifier

102

callingPartyNumber

51234

origCalledPartyNumber

57890

finalCalledPartyNumber

57890

lastRedirectDn

57890

origCause_Value

0

dest_CauseValue

16

origVideoCap_Codec

100

origVideoCap_Bandwidth

320

origVideoCap_Resolution

2

origVideoTransportAddress_IP

187962284

origVideoTransportAddress_Port

49208

destVideoCap_Codec

100

destVideoCap_Bandwidth

320

destVideoCap_Resolution

2

destVideoTransportAddress_IP

288625580

destVideoTransportAddress_Port

49254

## Video Conference Calls

Calls that are part of a video conference have multiple records logged. The number of CDR records that are generated depends
                              on the number of parties in the video conference. One CDR record exists for each party in the video conference, one for the
                              original placed call, one for each setup call that was used to join other parties to the video conference, and one for the
                              last two parties that are connected in the video conference.

Therefore, for a three party ad hoc video conference, six CDR records exist:

1 record for the original call

3 records for the parties that connected to the conference

1 record for each setup call

1 record for the final two parties in the conference

You can associate the setup calls with the correct call leg in the conference by examining the calling leg ID and called leg
                              ID.

The conference bridge device has special significance to the Unified Communications Manager, and calls to the conference bridge
                              appear as calls to the conference bridge device. A special number in the form "b0019901001" shows the conference bridge port.

All calls in or out of the conference bridge get shown going into the conference bridge, regardless of the actual direction.
                              By examining the setup call CDR records, you can determine the original direction of each call.

You can find the conference controller information in the comment field of the CDR. The format of this information follows:

Comment field = "ConfControllerDn=1000;ConfControllerDeviceName=SEP0003"

The conference controller DN + conference controller device name uniquely identifies the conference controller. You need the
                                    device name in the case of shared lines.

If the call is involved in multiple conference calls, the comment field will contain multiple conference controller information.
                                    This could happen in case the conference goes down to two parties and one of these parties starts another conference. If this
                                    is the case, the last conference controller information in the comment field will identify the conference controller.

The call legs that are connected to the conference will have the following fields information:

The finalCalledPartyNumber field contains the conference bridge number "b0019901001".

The origCalledPtyRedirectOnBehalfOf field gets set to (Conference = 4).

The lastRedirectRedirectOnBehalfOf field gets set to (Conference = 4).

The joinOnBehalfOf field gets set to (Conference = 4).

The comment field identifies the conference controller.

The destConversationId field remains the same for all members in the conference. You can use this field to identify members of a conference call.

The original placed call and all setup calls that were used to join parties to the conference will have the following fields:

The origCallTerminationOnBehalfOf field gets set to (Conference = 4).

The destCallTerminationOnBehalfOf field gets set to (Conference = 4).

### Video Conference Call CDR Example

Call from 2001 to 2309; 2309 answers, and they talk for 60 seconds.

2001 presses the conference softkey and dials 3071111.

307111 answers and talks for 20 seconds; 2001 presses the conference softkey to complete the conference.

The three members of the conference talk for 360 seconds.

3071111 hangs up; 2001 and 2309 stay in the conference. Because only two participants remain in the conference, the conference
                                    feature joins the two directly together, and they talk for another 55seconds.

Each video conference call leg gets shown placing a call into the conference bridge. The call gets shown as a call into the
                                          bridge, regardless of the actual direction of the call.

FieldNames

Orig Call CDR

Setup Call CDR

Conference CDR 1

Conference CDR 2

Conference CDR 3

Final CDR

globalCallID_callId

1

2

1

1

1

origLegCallIdentifier

101

105

101

102

106

101

destLegIdentifier

102

106

115

116

117

102

callingPartyNumber

2001

2001

2001

2309

3071111

2001

originalCalledPartyNumber

2309

3071111

b0029901001

b0029901001

b0029901001

2309

finalCalledPartyNumber

2309

3071111

b0029901001

b0029901001

b0029901001

2309

lastRedirectDn

2001

3071111

b0029901001

b0029901001

b0029901001

b0029901001

origCause_Value

393216

0

16

393216

393216

16

dest_CauseValue

393216

0

393216

393216

393216

0

origVideoCap_Codec

103

103

103

103

103

103

origVideoCap_Bandwidth

320

320

320

320

320

320

origVideoCap_Resolution

0

0

0

0

0

0

origVideoTransportAddress_IP

552953152

552953152

552953152

-822647488

-945658560

552953152

origVideoTransportAddress_Port

5445

5445

5445

5445

5445

5445

destVideoCap_Codec

103

103

103

103

103

103

destVideoCap_Bandwidth

320

320

320

320

320

320

destVideoCap_Resolution

0

0

0

0

0

0

destVideoTransportAddress_IP

-822647488

-945658560

-666216182

-666216182

-666216182

-822647488

destVideoTransportAddress_Port

5445

10002

10000

10004

10001

5445

origCalledPartyRedirectReason

0

0

0

0

0

0

lastRedirectRedirectReason

0

0

0

0

0

98

origTerminationOnBehalfOf

4

4

12

12

4

12

destTerminationOnBehalfOf

4

4

0

0

4

4

origCalledRedirectOnBehalfOf

0

0

4

4

4

0

lastRedirectRedirectOnBehalfOf

0

0

4

4

4

4

joinOnBehalfOf

0

0

4

4

4

4

Conversation ID

0

1

1

1

0

duration

60

360

360

360

55

Comment

Orig Call CDR

Setup Call CDR

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Conference CDR 1

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Conference CDR 2

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Conference CDR 3

ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD

Final CDR

| Field Names | Definitions |
|---|---|
| origMediaCap_bandwidth | This integer field contains the audio bandwidth. |
| destMediaCap_bandwidth | This integer field contains the audio bandwidth. |

| Codec | Bandwidth |
|---|---|
| G711Alaw64k | 64 |
| G711Alaw56k | 56 |
| G711mu-law64k | 64 |
| G711mu-law56k | 56 |
| G722 64k | 64 |
| G722 56k | 56 |
| G722 48k | 48 |
| G7231 | 7 |
| G728 | 16 |
| G729 | 8 |
| G729AnnexA | 8 |
| Is11172AudioCap | 0 |
| Is13818AudioCap | 0 |
| G729AnnexB | 8 |
| G729AnnexAwAnnexB | 8 |
| GSM Full Rate | 13 |
| GSM Half Rate | 7 |
| GSM Enhanced Full Rate | 13 |
| Wideband 256K | 256 |
| Data 64k | 64 |
| Data 56k | 56 |
| G7221 32K | 32 |
| G7221 24K | 24 |
| AAC-LD (mpeg4-generic) | 256 |
| AAC-LD (MP4A-LATM) 128K | 128 |
| AAC-LD (MP4A-LATM) 64K | 64 |
| AAC-LD (MP4A-LATM) 56K | 56 |
| AAC-LD (MP4A-LATM) 48K | 48 |
| AAC-LD (MP4A-LATM) 32K | 32 |
| AAC-LD (MP4A-LATM) 24K | 24 |
| GSM | 13 |
| iLBC | 15 or 13 |
| iSAC | 32 |
| XV150 MR 729A | 8 |
| NSE VBD 729A | 8 |

| Field Names | AAC CDR |
|---|---|
| globalCallID_callId | 121 |
| origLegCallIdentifier | 101 |
| destLegIdentifier | 102 |
| callingPartyNumber | 51234 |
| originalCalledPartyNumber | 57890 |
| finalCalledPartyNumber | 57890 |
| lastRedirectDn | 57890 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origMediaCap_payloadCapability | 42 |
| origMediaCap_Bandwidth | 256 |
| destMediaCap_payloadCapability | 42 |
| destMediaCap_Bandwidth | 256 |

| Note | You must enable the CDR Log Calls With Zero Duration Flag service parameter to log calls with zero duration. This parameter
                                          enables or disables the logging of CDRs for calls which lasted less than 1 second. See Configure CDR Service Parameters for more information. |
|---|---|

| Field Names | CDR |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 0 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber |  |
| finalCalledPartyNumber |  |
| lastRedirectDn |  |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| duration | 0 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 2 |
| origLegCallIdentifier | 200 |
| destLegIdentifier | 201 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| duration | 0 |

| Field Names | CDR1: Alice -> Bob (original call) | CDR2: Bob -> Carol (consultation call) | CDR3: Dave -> Carol (original call) | CDR4: Dave -> Ed (consultation call) | CDR5: Carol -> Conference Bridge (conference call) | CDR6: Dave -> Conference Bridge (conference call) |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 2 | 3 | 4 | 3 | 3 |
| origLegCallIdentifier | 11 | 13 | 21 | 23 | 22 | 22 |
| destLegIdentifier | 12 | 14 | 22 | 24 | 25 | 26 |
| callingPartyNumber | 1000 | 1001 | 1003 | 1003 | 1002 | 1003 |
| originalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901222 | b0029901222 |
| finalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901222 | b0029901222 |
| lastRedirectDn | 1001 | 1002 | 1002 | 1004 | 1003 | 1003 |
| origTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 4 | 4 |
| destTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 4 | 4 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 0 | 0 | 4 | 4 |
| origConversationID | 0 | 0 | 0 | 0 | 0 | 0 |
| destConversationID | 0 | 0 | 0 | 0 | 2222 | 2222 |
| Comment |  |  |  |  | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Field Names | CDR7: Dave -> Conference Bridge (conference call) | CDR8: Ed -> Conference Bridge (conference call) | CDR9: Conference Bridge (conference call) | CDR10: Alice -> Conference Bridge (conference call) | CDR11: Bob -> Conference Bridge (conference call) |
|---|---|---|---|---|---|
| globalCallID_callId | 3 | 3 | 1 | 1 | 1 |
| origLegCallIdentifier | 21 | 24 | 17 | 11 | 12 |
| destLegIdentifier | 26 | 27 | 28 | 15 | 16 |
| callingPartyNumber | 1003 | 1004 | b0029901001 | 1000 | 1001 |
| originalCalledPartyNumber | b0029901222 | b0029901222 | b0029901222 | b0029901001 | b0029901001 |
| finalCalledPartyNumber | b0029901222 | b0029901222 | b0029901222 | b0029901001 | b0029901001 |
| lastRedirectDn | 1003 | 1003 | 1002 | 1001 | 1001 |
| origTerminationOnBehalfOf | 0 | 0 | 0 | 0 | 0 |
| destTerminationOnBehalfOf | 0 | 0 | 0 | 0 | 0 |
| lastRedirectRedirectReason | 98 | 98 | 4 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 4 | 4 | 10 | 4 | 4 |
| origConversationID | 0 | 0 | 0 | 0 | 0 |
| destConversationID | 2222 | 2222 | 2222 | 2222 | 2222 |
| Comment | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD |

| Note | The direction of the call between the bridges depends on which of the two calls that involve Carol is the primary call. The
                                             primary call side represents the calling party of the transferred call. |
|---|---|

| Field Names | CDR1: Alice -> Bob (original call) | CDR2: Bob -> Carol (consultation call) | CDR3: Dave -> Carol (original call) | CDR4: Dave -> Carol (consultation call) | CDR5: Carol -> Conference Bridge (conference call) | CDR6: Carol -> Conference Bridge (conference call) |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 2 | 3 | 4 | 1 | 3 |
| origLegCallIdentifier | 11 | 13 | 21 | 23 | 14 | 22 |
| destLegIdentifier | 12 | 14 | 22 | 24 | 17 | 25 |
| callingPartyNumber | 1000 | 1001 | 1003 | 1003 | 1002 | 1003 |
| originalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| finalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| lastRedirectDn | 1001 | 1002 | 1002 | 1004 | 1001 | 1003 |
| origTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| destTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 0 | 0 | 4 | 4 |
| origConversationID | 0 | 0 | 0 | 0 | 0 | 0 |
| destConversationID | 0 | 0 | 0 | 0 | 1111 | 2222 |
| Comment |  |  |  |  | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Field Names | CDR7: Dave -> Conference Bridge (conference call) | CDR8: Ed -> Conference Bridge (conference call) | CDR9: Conference Bridge (conference call) | CDR10: Alice -> Conference Bridge (conference call) | CDR11: Bob -> Conference Bridge (conference call) |
|---|---|---|---|---|---|
| globalCallID_callId | 3 | 3 | 1 | 1 | 1 |
| origLegCallIdentifier | 21 | 24 | 17 | 11 | 12 |
| destLegIdentifier | 26 | 27 | 28 | 15 | 16 |
| callingPartyNumber | 1003 | 1004 | b0029901001 | 1000 | 1001 |
| originalCalledPartyNumber | b0029901222 | b0029901222 | b0029901222 | b0029901001 | b0029901001 |
| finalCalledPartyNumber | b0029901222 | b0029901222 | b0029901222 | b0029901001 | b0029901001 |
| lastRedirectDn | 1003 | 1003 | 1002 | 1001 | 1001 |
| origTerminationOnBehalfOf | 0 | 0 | 0 | 0 | 0 |
| destTerminationOnBehalfOf | 0 | 0 | 0 | 0 | 0 |
| lastRedirectRedirectReason | 98 | 98 | 4 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 4 | 4 | 10 | 4 | 4 |
| origConversationID | 0 | 0 | 111 | 0 | 0 |
| destConversationID | 2222 | 2222 | 2222 | 1111 | 1111 |
| Comment | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD |

| Note | If Bob is not a controller and the chaining occurs before Bob joins Conference1, the call between Bob and Conference2 gets
                                             generated in the opposite direction from what is shown in the CDRs. |
|---|---|

| Field Names | CDR1: Alice -> Bob (original call) | CDR2: Bob -> Carol (consultation call) | CDR3: Dave -> Carol (original call) | CDR4: Dave -> Carol (consultation call) | CDR5: Carol -> Conference Bridge (conference call) | CDR6: Carol -> Conference Bridge (conference call) |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 2 | 3 | 4 | 1 | 3 |
| origLegCallIdentifier | 11 | 13 | 21 | 23 | 14 | 22 |
| destLegIdentifier | 12 | 14 | 22 | 24 | 17 | 25 |
| callingPartyNumber | 1000 | 1001 | 1003 | 1003 | 1002 | 1002 |
| originalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| finalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| lastRedirectDn | 1001 | 1002 | 1002 | 1004 | 1001 | 1003 |
| origTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| destTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 0 | 0 | 4 | 4 |
| origConversationID | 0 | 0 | 0 | 0 | 0 | 0 |
| destConversationID | 0 | 0 | 0 | 0 | 1111 | 2222 |
| Comment |  |  |  |  | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Field Names | CDR7: Alice -> Conference Bridge (conference call) | CDR8: Bob -> Conference Bridge (conference call) | CDR9: Conference Bridge -> Conference Bridge | CDR10: Bob -> Conference Bridge (conference call) | CDR11: Dave -> Conference Bridge (conference call) | CDR12: Ed -> Conference Bridge (conference call) |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 1 | 3 | 3 | 3 | 3 |
| origLegCallIdentifier | 11 | 12 | 25 | 11 | 12 | 24 |
| destLegIdentifier | 15 | 16 | 28 | 15 | 16 | 27 |
| callingPartyNumber | 1001 | 1001 | b0029901222 | 1000 | 1001 | 1003 |
| originalCalledPartyNumber | b0029901001 | b0029901001 | b0029901001 | b0029901222 | b0029901222 | b0029901222 |
| finalCalledPartyNumber | b0029901001 | b0029901001 | b0029901001 | b0029901222 | b0029901222 | b0029901222 |
| lastRedirectDn | 1001 | 1001 | 1002 | b0029901001 | 1003 | 1003 |
| origTerminationOnBehalfOf | 16 | 4 | 4 | 4 | 0 | 0 |
| destTerminationOnBehalfOf | 0 | 4 | 4 | 4 | 0 | 0 |
| lastRedirectRedirectReason | 98 | 98 | 4 | 98 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 4 | 4 | 10 | 4 | 4 | 4 |
| origConversationID | 0 | 0 | 2222 | 0 | 0 | 0 |
| destConversationID | 1111 | 1111 | 1111 | 2222 | 2222 | 2222 |
| Comment | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Note | The direction of a call between the final two parties of a conference depends on who has been in the conference the longest.
                                             The party that has been in the conference the longest becomes the calling party. |
|---|---|

| Field Names | CDR1: Alice -> Bob (original call) | CDR2: Bob -> Carol (consultation call) | CDR3: Dave -> Carol (original call) | CDR4: Dave -> Carol (consultation call) | CDR5: Carol -> Conference Bridge (conference call) | CDR6: Carol -> Conference Bridge (conference call) |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 2 | 3 | 4 | 1 | 3 |
| origLegCallIdentifier | 11 | 13 | 21 | 23 | 14 | 22 |
| destLegIdentifier | 12 | 14 | 22 | 24 | 17 | 25 |
| callingPartyNumber | 1000 | 1001 | 1003 | 1003 | 1002 | 1002 |
| originalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| finalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| lastRedirectDn | 1001 | 1002 | 1002 | 1004 | 1001 | 1003 |
| origTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| destTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 0 | 0 | 4 | 4 |
| origConversationID | 0 | 0 | 0 | 0 | 0 | 0 |
| destConversationID | 0 | 0 | 0 | 0 | 1111 | 2222 |
| Comment |  |  |  |  | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Field Names | CDR7: Conference Bridge -> Conference Bridge | CDR8: Alice -> Conference Bridge (conference call) | CDR9: Conference Bridge -> Conference Bridge | CDR10: Alice -> Conference Bridge (conference call) | CDR11: Dave -> Conference Bridge (conference call) | CDR12: Ed -> Conference Bridge (conference call) |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 1 | 3 | 3 | 3 | 3 |
| origLegCallIdentifier | 12 | 11 | 25 | 11 | 21 | 24 |
| destLegIdentifier | 16 | 15 | 28 | 25 | 26 | 27 |
| callingPartyNumber | 1001 | 1000 | b0029901001 | 1001 | 1003 | 1004 |
| originalCalledPartyNumber | b0029901001 | b0029901001 | b0029901001 | b0029901222 | b0029901222 | b0029901222 |
| finalCalledPartyNumber | b0029901001 | b0029901001 | b0029901001 | b0029901222 | b0029901222 | b0029901222 |
| lastRedirectDn | 1001 | 1001 | 1002 | b0029901001 | 1003 | 1003 |
| origTerminationOnBehalfOf | 4 | 16 | 4 | 4 | 0 | 0 |
| destTerminationOnBehalfOf | 4 | 0 | 4 | 4 | 0 | 0 |
| lastRedirectRedirectReason | 98 | 98 | 4 | 98 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 4 | 4 | 10 | 4 | 4 | 4 |
| origConversationID | 0 | 0 | 2222 | 0 | 0 | 0 |
| destConversationID | 1111 | 1111 | 1111 | 2222 | 2222 | 2222 |
| Comment | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Field Names | CDR1: Alice -> Bob (original call) | CDR2: Bob -> Carol (consultation call) | CDR3: Dave -> Carol (original call) | CDR4: Dave -> Carol (consultation call) | CDR5: Carol -> Conference Bridge (conference call) | CDR6: Carol -> Conference Bridge (conference call) |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 2 | 3 | 4 | 1 | 3 |
| origLegCallIdentifier | 11 | 13 | 21 | 23 | 14 | 22 |
| destLegIdentifier | 12 | 14 | 22 | 24 | 17 | 25 |
| callingPartyNumber | 1000 | 1001 | 1003 | 1003 | 1002 | 1002 |
| originalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| finalCalledPartyNumber | 1001 | 1002 | 1002 | 1004 | b0029901001 | b0029901222 |
| lastRedirectDn | 1001 | 1002 | 1002 | 1004 | 1001 | 1003 |
| origTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| destTerminationOnBehalfOf | 4 | 4 | 4 | 4 | 10 | 10 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 0 | 0 | 4 | 4 |
| origConversationID | 0 | 0 | 0 | 0 | 0 | 0 |
| destConversationID | 0 | 0 | 0 | 0 | 1111 | 2222 |
| Comment |  |  |  |  | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Field Names | CDR7: Conference Bridge -> Conference Bridge | CDR8: Alice -> Conference Bridge (conference call) | CDR9: Bob -> Conference Bridge | CDR10: Dave -> Conference Bridge (conference call) | CDR11: Ed -> Conference Bridge (conference call) | CDR12: Bob-> Alice |
|---|---|---|---|---|---|---|
| globalCallID_callId | 3 | 1 | 1 | 3 | 3 | 3 |
| origLegCallIdentifier | 25 | 11 | 12 | 21 | 24 | 21 |
| destLegIdentifier | 28 | 15 | 16 | 26 | 27 | 24 |
| callingPartyNumber | b0029901222 | 1000 | 1001 | 1003 | 1004 | 1003 |
| originalCalledPartyNumber | b0029901001 | b0029901001 | b0029901001 | b0029901222 | b0029901222 | b0029901222 |
| finalCalledPartyNumber | b0029901001 | b0029901001 | b0029901001 | b0029901222 | b0029901222 | 1004 |
| lastRedirectDn | 1002 | 1001 | 1001 | 1003 | 1003 | b0029901222 |
| origTerminationOnBehalfOf | 4 | 4 | 4 | 16 | 0 | 0 |
| destTerminationOnBehalfOf | 4 | 4 | 4 | 0 | 0 | 0 |
| lastRedirectRedirectReason | 4 | 98 | 98 | 98 | 98 | 98 |
| lastRedirectRedirectOnBehalfOf | 10 | 4 | 4 | 4 | 4 | 4 |
| origConversationID | 0 | 0 | 0 | 0 | 0 | 0 |
| destConversationID | 1111 | 1111 | 1111 | 2222 | 2222 | 0 |
| Comment | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1001;Co
nfController
DeviceName=S
EP0003E333FE
BD;ConfReque
storDn-1001;
ConfRequesto
rDeviceName=
SEP0003E333F
EBD | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 | ConfControll
erDn=1003;Co
nfController
DeviceName=S
EP0003E333FA
D1;ConfReque
storDn-1003;
ConfRequesto
rDeviceName=
SEP0003E333F
AD1 |

| Field Names | CDR13: Dave -> Ed |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 21 |
| destLegIdentifier | 24 |
| callingPartyNumber | 1003 |
| originalCalledPartyNumber | b0029901222 |
| finalCalledPartyNumber | 1004 |
| lastRedirectDn | b0029901222 |
| origTerminationOnBehalfOf | 0 |
| destTerminationOnBehalfOf | 0 |
| lastRedirectRedirectReason | 98 |
| lastRedirectRedirectOnBehalfOf | 4 |
| origConversationID | 0 |
| destConversationID | 0 |
| Comment | ConfControllerDn=10
03;ConfControllerDe
viceName=SEP0003E33
3FAD1;ConfRequestor
Dn-1003;ConfRequest
orDeviceName=SEP000
3E333FAD1 |

| Field Names | Call From Customer to Agent | Call From IVR to Agent BIB |
|---|---|---|
| globalCallID_callId | 270001 | 270002 |
| origLegCallIdentifier | 22980857 | 22980861 |
| destLegIdentifier | 22980858 | 22980862 |
| callingPartyNumber | 1001 | 1000 |
| originalCalledPartyNumber | 1006 | b00121104001 |
| finalCalledPartyNumber | 1006 | b00121104001 |
| origCallTerminationOnBehalfOf | 12 | 0 |
| destCallTerminationOnBehalfOf | 0 | 33 |
| origCalledPartyRedirectOnBehalfOf | 0 | 33 |
| lastRedirectRedirectOnBehalfOf | 0 | 33 |
| origCalledPartyRedirectReason | 0 | 752 |
| lastRedirectRedirectReason | 0 | 752 |
| destConversationId | 0 | 22980858 |
| joinOnBehalfOf |  | 33 |
| comment |  | AgentGreeting=22980858 |
| duration | 23 | 9 |

| Note | Both CDRs have the same globalCallID_callId, and the conversationID field links back to the CI (call Identifier) of the barged
                                                call. |
|---|---|

| Field Names | Original Call CDR | Barge Call CDR |
|---|---|---|
| globalCallID_callId | 7 | 7 |
| origLegCallIdentifier | 16777230 | 16777232 |
| destLegIdentifier | 16777231 | 16777235 |
| callingPartyNumber | 40003 | 40003 |
| origCalledPartyNumber | 40001 | b001501001 |
| finalCalledPartyNumber | 40001 | b001501001 |
| lastRedirectDn | 40001 | b001501001 |
| origCause_Value | 16 | 0 |
| dest_CauseValue | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 114 |
| lastRedirectRedirectReason | 0 | 114 |
| origCalledPartyRedirectOnBehalfOf |  | 15 |
| lastRedirectRedirectOnBehalfOf |  | 15 |
| joinOnBehalfOf |  | 15 |
| destConversationID | 0 | 16777231 |

| Note | Both CDRs have the same globalCallID_callId, and the conversationID field links back to the CI (call Identifier) of the barged
                                                call. |
|---|---|

| Field Names | Original Call CDR | Barge Call 1 CDR | Final Call 2 CDR |
|---|---|---|---|
| globalCallID_callId | 9 | 9 | 9 |
| origLegCallIdentifier | 16777236 | 16777238 | 16777236 |
| destLegIdentifier | 16777237 | 16777241 | 16777238 |
| callingPartyNumber | 40003 | 40001 | 40003 |
| origCalledPartyNumber | 40001 | b001501001 | 40001 |
| finalCalledPartyNumber | 40001 | b001501001 | 40001 |
| lastRedirectDn | 40001 | b001501001 | 40001 |
| origCause_Value | 0 | 393216 | 16 |
| dest_CauseValue | 16 | 393216 | 0 |
| origCalledPartyRedirectReason | 0 | 114 | 0 |
| lastRedirectRedirectReason | 0 | 114 | 0 |
| origTerminationOnBehalfOf |  | 15 | 12 |
| destTerminationOnBehalfOf | 12 | 15 | 12 |
| lastRedirectRedirectOnBehalfOf |  | 15 |  |
| joinOnBehalfOf |  | 15 |  |
| destConversationID | 0 | 16777237 | 0 |

| Note | All CDRs have the same globalCallID_callId , and the conversationID field links back to the CI (call Identifier) of the barged call. |
|---|---|

| Field Names | Original Call CDR | Barge Call 1 CDR | Final Call 2 CDR |
|---|---|---|---|
| globalCallID_callId | 14 | 14 | 14 |
| origLegCallIdentifier | 16777249 | 16777251 | 16777255 |
| destLegIdentifier | 16777250 | 16777254 | 16777258 |
| callingPartyNumber | 40003 | 40001 | 40001 |
| origCalledPartyNumber | 40001 | b001501001 | b001501001 |
| finalCalledPartyNumber | 40001 | b001501001 | b001501001 |
| lastRedirectDn | 40001 | b001501001 | b001501001 |
| origCause_Value | 16 | 0 | 0 |
| dest_CauseValue | 0 | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 114 | 114 |
| lastRedirectRedirectReason | 0 | 114 | 114 |
| origTerminationOnBehalfOf | 12 | 15 | 15 |
| destTerminationOnBehalfOf |  |  |  |
| origRedirectRedirectOnBehalfOf |  | 15 | 15 |
| lastRedirectRedirectOnBehalfOf |  | 15 | 15 |
| joinOnBehalfOf |  | 15 | 15 |
| destConversationID | 0 | 16777250 | 16777251 |

| Field Names | Monitored Call CDR | Monitoring Call CDR |
|---|---|---|
| globalCallID_callId | 7 | 10 |
| origLegCallIdentifier | 16777230 | 16777232 |
| destLegIdentifier | 16777231 | 16777235 |
| callingPartyNumber | 9728134987 | 40003 |
| originalCalledPartyNumber | 30000 | b001501001 |
| finalCalledPartyNumber | 30000 | b001501001 |
| lastRedirectDn | 30000 | b001501001 |
| origCause_Value | 16 | 0 |
| dest_CauseValue | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 370 |
| lastRedirectRedirectOnBehalfOf | 0 | 370 |
| origCalledPartyRedirectOnBehalfOf |  | 28 |
| lastRedirectRedirectOnBehalfOf |  | 28 |
| destConversationID | 0 | 16777231 |

| Field Names | Monitored Call CDR | Monitoring Call CDR |
|---|---|---|
| globalCallID_callId | 71 | 101 |
| origLegCallIdentifier | 16777299 | 16777932 |
| destLegIdentifier | 16777300 | 16777235 |
| callingPartyNumber | 30000 | 40003 |
| originalCalledPartyNumber | 9728134987 | b001501002 |
| finalCalledPartyNumber | 9728134987 | b001501002 |
| lastRedirectDn | 9728134987 | b001501002 |
| origCause_Value | 16 | 0 |
| dest_CauseValue | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 370 |
| lastRedirectRedirectOnBehalfOf | 0 | 370 |
| origCalledPartyRedirectOnBehalfOf |  | 28 |
| lastRedirectRedirectOnBehalfOf |  | 28 |
| destConversationID | 0 | 16777299 |

| Field Names | Original Call That Is Parked CDR | Parked Call That Is Picked Up CDR |
|---|---|---|
| globalCallID_callId | 1 | 1 |
| origLegCallIdentifier | 20863957 | 20863961 |
| destLegIdentifier | 20863958 | 20863957 |
| callingPartyNumber | 50003 | 50001 |
| originalCalledPartyNumber | 50002 | 50003 |
| finalCalledPartyNumber | 50002 | 50003 |
| lastRedirectDn | 50002 | 44444 |
| origCause_Value | 393216 | 0 |
| dest_CauseValue | 393216 | 16 |
| origCalledPartyRedirectReason | 0 | 0 |
| lastRedirectRedirectReason | 0 | 8 |
| origCalledPartyRedirectOnBehalfOf | 0 | 0 |
| lastRedirectRedirectOnBehalfOf | 0 | 3 |
| origTerminationOnBehalfOf | 3 | 0 |
| destTerminationOnBehalfOf | 3 | 12 |
| joinOnBehalfOf | 0 | 3 |
| duration | 4 | 60 |

| Field Names | Original Call That Is Parked CDR | Reverted Call CDR |
|---|---|---|
| globalCallID_callId | 2 | 2 |
| origLegCallIdentifier | 20863963 | 20863963 |
| destLegIdentifier | 20863964 | 20863967 |
| callingPartyNumber | 50003 | 50003 |
| originalCalledPartyNumber | 50002 | 50002 |
| finalCalledPartyNumber | 50002 | 50002 |
| lastRedirectDn | 50002 | 50002 |
| origCause_Value | 393216 | 0 |
| dest_CauseValue | 393216 | 16 |
| origCalledPartyRedirectReason | 0 | 7 |
| lastRedirectRedirectReason | 0 | 11 |
| origCalledPartyRedirectOnBehalfOf | 0 | 3 |
| lastRedirectRedirectOnBehalfOf | 0 | 3 |
| origTerminationOnBehalfOf | 3 | 3 |
| destTerminationOnBehalfOf | 3 | 12 |
| joinOnBehalfOf | 0 | 3 |
| duration | 7 | 60 |

| Field Names | Pickup Call CDR |
|---|---|
| globalCallID_callId | 22 |
| callingPartyNumber | 9728131234 |
| originalCalledPartyNumber | 2001 |
| finalCalledPartyNumber | 2002 |
| lastRedirectDn | 2001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origTerminationOnBehalfOf | 16 |
| destTerminationOnBehalfOf | 16 |
| lastRedirectOnBehalfOf | 16 |
| lastRedirectReason | 5 |
| joinOnBehalfOf | 16 |

| Note | When the Service Parameter Auto Call Pickup Enabled is set to True for an IP Phone and a Unified Communications Manager receives an incoming call that the IP phone picks up,
                                             the prefix digit defined in the Translation Pattern is added to the callingPartyNumber in CDR. However, the prefix digit is not added when the Service Parameter Auto Call Pickup Enabled is set to False. |
|---|---|

| Note | The prefix digits defined in the Translation Pattern only applies to basic call. |
|---|---|

| Field Names | Original Call CDR | Pickup CDR |
|---|---|---|
| globalCallID_callId | 11 | 11 |
| origLegCallIdentifier | 12345 | 12345 |
| destLegIdentifier | 12346 | 12347 |
| callingPartyNumber | 9728134987 | 9728134987 |
| originalCalledPartyNumber | 2001 | 2001 |
| finalCalledPartyNumber | 2001 | 2002 |
| lastRedirectDn | 2001 | 2001 |
| origCause_Value | 393216 | 16 |
| dest_CauseValue | 393216 | 0 |
| origTerminationOnBehalfOf | 16 | 12 |
| destTerminationOnBehalfOf | 16 | 16 |
| lastRedirectRedirectReason | 0 | 5 |
| lastRedirectRedirectOnBehalfOf | 0 | 16 |
| joinOnBehalfOf | 0 | 16 |
| duration | 0 | 120 |

| Note | If the CDR Log Calls with Zero Duration Flag service parameter is set to true, two additional server call records are created. |
|---|---|

| Field Names | Recorded Call CDR | Recording Call CDR1 | Recording Call CDR2 |
|---|---|---|---|
| globalCallID_callId | 7 | 10 | 11 |
| origLegCallIdentifier | 16777110 | 16777120 | 16777122 |
| destLegIdentifier | 16777111 | 16777121 | 16777123 |
| callingPartyNumber | 9728134987 | BIB | BIB |
| originalCalledPartyNumber | 30000 | 90000 | 90000 |
| finalCalledPartyNumber | 30000 | 90000 | 90000 |
| lastRedirectDn | 30000 | 90000 | 90000 |
| origCause_Value | 16 | 0 | 0 |
| dest_CauseValue | 0 | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 354 | 354 |
| lastRedirectRedirectOnBehalfOf | 0 | 354 | 354 |
| origCalledPartyRedirectOnBehalfOf |  | 27 | 27 |
| lastRedirectRedirectOnBehalfOf |  | 27 | 27 |
| origConversationID | 0 | 16777111 | 16777111 |

| Field Names | Recorded Call CDR | Recording Call CDR 1 | Recording Call CDR 2 |
|---|---|---|---|
| globalCallID_callId | 71 | 100 | 110 |
| origLegCallIdentifier | 16777113 | 16777220 | 16777222 |
| destLegIdentifier | 16777114 | 16777221 | 16777223 |
| callingPartyNumber | 30000 | BIB | BIB |
| originalCalledPartyNumber | 9728134987 | 90000 | 90000 |
| finalCalledPartyNumber | 9728134987 | 90000 | 90000 |
| lastRedirectDn | 9728134987 | 90000 | 90000 |
| origCause_Value | 16 | 16 | 16 |
| dest_CauseValue | 0 | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 354 | 354 |
| lastRedirectRedirectOnBehalfOf | 0 | 354 | 354 |
| origCalledPartyRedirectOnBehalfOf |  | 27 | 27 |
| lastRedirectRedirectOnBehalfOf |  | 27 | 27 |
| origConversationID | 0 | 16777113 | 16777113 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 102 |
| origLegCallIdentifier | 16777140 |
| destLegIdentifier | 16777141 |
| callingPartyNumber | 20000 |
| origCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| lastRedirectDn | 20001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| callSecuredStatus | 2 |
| duration | 300 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 103 |
| origLegCallIdentifier | 16777142 |
| destLegIdentifier | 16777143 |
| callingPartyNumber | 20000 |
| origCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| lastRedirectDn | 20001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| callSecuredStatus | 1 |
| duration | 600 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | +19725001212 |
| outpulsedCallingPartyNumber | 5001212 |
| duration | 60 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 2 |
| origLegCallIdentifier | 102 |
| destLegIdentifier | 103 |
| callingPartyNumber | +19725002345 |
| outpulsedCallingPartyNumber | 9725002345 |
| duration | 60 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| origCause_Value | 0 |
| dest_CauseValue | 17 |
| duration | 0 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 4 |
| origLegCallIdentifier | 302 |
| destLegIdentifier | 303 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| origCause_Value | 1 |
| dest_CauseValue | 0 |
| duration | 0 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 5 |
| origLegCallIdentifier | 304 |
| destLegIdentifier | 305 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| origCause_Value | 0 |
| dest_CauseValue | 38 |
| duration | 0 |

| Field Names | Orig Call CDR | cBarge Call CDR 1 | cBarge Call CDR 2 | cBarge Call CDR 3 | Final Call CDR |
|---|---|---|---|---|---|
| globalCallID_callId | 49 | 49 | 49 | 49 | 49 |
| origLegCallIdentifier | 1677346 | 1677348 | 1677347 | 1677346 | 1677347 |
| destLegIdentifier | 1677347 | 1677353 | 1677351 | 1677352 | 1677346 |
| callingPartyNumber | 40003 | 40001 | 40001 | 40003 | 40001 |
| originalCalledPartyNumber | 40001 | b0029901001 | b0029901001 | b0029901001 | 40003 |
| finalCalledPartyNumber | 40001 | b0029901001 | b0029901001 | b0029901001 | 40003 |
| lastRedirectDn | 40001 | b0029901001 | 40001 | 40001 | b0029901001 |
| origCause_Value | 393216 | 16 | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 0 | 393216 | 393216 | 0 |
| origCalledPartyRedirectReason | 0 | 98 | 98 | 98 | 0 |
| lastRedirectRedirectReason | 0 | 98 | 98 | 98 | 98 |
| destTerminationOnBehalfOf | 4 |  | 4 | 4 | 4 |
| origCalledRedirectOnBehalfOf |  | 4 | 4 | 4 |  |
| lastRedirectRedirectOnBehalfOf |  | 4 | 4 | 4 | 4 |
| joinOnBehalfOf |  | 4 | 4 | 4 | 4 |
| Conversation ID | 0 | 16777220 | 16777220 | 16777220 | 1 |
| duration | 60 | 360 |  | 360 | 360 |

| Comment |
|---|
| Orig Call CDR |  |
| cBarge Call CDR 1 | ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD |
| cBarge Call CDR 2 | ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD |
| cBarge Call CDR 3 | ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD |
| Final Call CDR | ConfControllerDn=40003;ConfControlerDeviceName=SEP0003E333FEBD |

| Field Names | Values |
|---|---|
| globalCallID_callId | 101 |
| origLegCallIdentifier | 16777130 |
| destLegIdentifier | 16777131 |
| callingPartyNumber | 10000 |
| origCalledPartyNumber | 2142364624 |
| finalCalledPartyNumber | 2142364624 |
| lastRedirectDn | 2142364624 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| clientMatterCode | 11111 |
| duration | 600 |

| FieldNames | Orig Call CDR | Setup Call CDR | Conference CDR 1 | Conference CDR 2 | Conference CDR 3 | Final CDR |
|---|---|---|---|---|---|---|
| globalCallID_callId | 60025 | 60026 | 60025 | 60025 | 60025 | 60027 |
| origLegCallIdentifier | 23704522 | 23704524 | 23704523 | 23704522 | 23704526 | 23704527 |
| destLegIdentifier | 23704523 | 23704526 | 23704531 | 23704530 | 23704532 | 23704528 |
| callingPartyNumber | 136201 | 136201 | 136111 | 136201 | 136203 | 136201 |
| origCalledPartyNumber | 136111 | 136203 | b00105401002 | b00105401002 | b00105401002 | 136203 |
| finalCalledPartyNumber | 136111 | 136203 | b00105401002 | b00105401002 | b00105401002 | 136203 |
| lastRedirectDn | 136111 | 136203 | 136201 | 136201 | 136201 | 136203 |
| origCause_Value | 393216 | 0 | 16 | 393216 | 393216 | 0 |
| dest_CauseValue | 393216 | 0 | 393216 | 393216 | 393216 | 16 |
| authCodeDescription |  | Forward_CMC |  |  |  |  |
| authorizationLevel | 0 | 1 | 0 | 0 | 0 | 0 |
| Duration | 20 | 0 | 32 | 32 | 25 | 48 |
| authorizationCode |  | 125 |  |  |  |  |

| Note | The setup call CDR for this example is generated even though it is of zero duration since CMC is used for this call. |
|---|---|

| Note | Each conference call leg gets shown as placing a call into the conference bridge. The system shows the call as a call into
                                          the bridge, regardless of the actual direction of the call. |
|---|---|

| Field Names | Orig Call CDR | Setup Call CDR | Conference CDR 1 | Conference CDR 2 | Conference CDR 3 | Final CDR |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 2 | 1 | 1 | 1 | 1 |
| origLegCallIdentifier | 101 | 105 | 101 | 102 | 106 | 101 |
| destLegIdentifier | 102 | 106 | 115 | 116 | 117 | 102 |
| callingPartyNumber | 2001 | 2001 | 2001 | 2309 | 3071111 | 2001 |
| originalCalledPartyNumber | 2309 | 3071111 | b0029901001 | b0029901001 | b0029901001 | 2309 |
| finalCalledPartyNumber | 2301 | 3071111 | b0029901001 | b0029901001 | b0029901001 | 2309 |
| lastRedirectDn | 2001 | 3071111 | b0029901001 | b0029901001 | b0029901001 | b0029901001 |
| origCause_Value | 393216 | 0 | 16 | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 0 | 393216 | 393216 | 393216 | 0 |
| origCalledPartyRedirectReason | 0 | 0 | 0 | 0 | 0 | 0 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 | 0 | 98 |
| origTerminationOnBehalfOf | 4 | 4 | 12 | 12 | 4 | 12 |
| destTerminationOnBehalfOf | 4 | 4 | 0 | 0 | 4 | 4 |
| origCalledRedirectOnBehalfOf | 0 | 0 | 4 | 4 | 4 | 0 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 4 | 4 | 4 | 4 |
| joinOnBehalfOf | 0 | 0 | 4 | 4 | 4 | 4 |
| Conversation ID | 0 | 0 | 1 | 1 | 1 | 0 |
| duration | 60 | 20 | 360 | 360 | 360 | 55 |

| Comment |
|---|
| Orig Call CDR |  |
| Setup Call CDR | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Conference CDR 1 | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Conference CDR 2 | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Conference CDR 3 | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Final CDR |  |

| FieldNames | Orig Call CDR1 | Conference CDR 1 | Orig Call CDR2 | Conference CDR 2 |
|---|---|---|---|---|
| globalCallID_callId | 47002 | 47002 | 47003 | 47003 |
| origLegCallIdentifier | 20795093 | 20795093 | 20795098 | 20795098 |
| destLegIdentifier | 20795096 | 20795104 | 20795101 | 20795103 |
| callingPartyNumber | 139139 | 139139 | 136136 | 136136 |
| originalCalledPartyNumber | 1010 | 1010 | 1010 | 1010 |
| finalCalledPartyNumber | c00124401001 | b00105401006 | c00124401001 | b00105401006 |
| lastRedirectDn | 1010 | c00124401001 | 1010 | c00124401001 |
| origCause_Value | 0 | 16 | 0 | 16 |
| dest_CauseValue | 0 | 0 | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 0 | 0 | 0 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 |
| origTerminationOnBehalfOf | 7 | 12 | 7 | 12 |
| destTerminationOnBehalfOf | 7 | 7 | 7 | 7 |
| origCalledRedirectOnBehalfOf | 0 | 0 | 0 | 0 |
| lastRedirectRedirectOnBehalfOf | 0 | 7 | 0 | 7 |
| joinOnBehalfOf | 0 | 7 | 0 | 7 |
| Conversation ID | 0 | 16809217 | 0 | 16809217 |
| duration | 14 | 20 | 10 | 9 |

| Comment |
|---|
| Orig Call CDR 1 |  |
| Conference CDR 1 | ConferenceNowHostID=Rishi;ConferenceNowMeetingNumber=136136 |
| Orig Call CDR 2 |  |
| Conference CDR 2 | ConferenceNowHostID=Rishi;ConferenceNowMeetingNumber=136136 |

| Calling Party | Calling Partition | Original Called Party | Orig Cause | Original Called Partition | Called Leg | Dest Cause | Final Called Party | Final Called Partition | Last Redirect Party |
|---|---|---|---|---|---|---|---|---|---|
| 2001 | ACNTS | 2309 | 0 | MKTG | 102 | 16 | 2309 | MKTG | 2001 |
| 2001 | ACNTS | 2309 | 16 | MKTG | 115 | 0 | b0029901001 |  | b0029901001 |
| 2309 | ACNTS | b0029901001 | 0 |  | 116 | 128 | b0029901001 |  | b0029901001 |
| 3071111 | PSTN | b0029901001 | 16 |  | 117 | 0 | b0029901001 |  | b0029901001 |
| 2001 | ACNTS | 2309 | 16 | PSTN | 106 | 0 | 3071111 | PSTN | 30711111 |

| Orig Conversation ID | OrigCall Termination OnBehalfOf | DestCall Termination OnBehalfOf | OriginalCalled Pty Redirect OnBehalfOf | LastRedirect Redirect OnBehalfOf | Join OnBehalfOf | Duration |
|---|---|---|---|---|---|---|
| 0 | 4 | 4 | 0 | 0 | 0 | 60 |
| 1 | 12 | 0 | 4 | 4 | 4 | 360 |
| 1 | 13 | 0 | 4 | 4 | 4 | 200 |
| 1 | 4 | 4 | 4 | 4 | 4 | 360 |
| 0 | 4 | 4 | 0 | 0 | 0 | 20 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 200 |
| origLegCallIdentifier | 16777500 |
| destLegIdentifier | 16777501 |
| callingPartyNumber | 20000 |
| origCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| lastRedirectDn | 20001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origDTMFMethod | 0 |
| destDTMFMethod | 0 |
| duration | 60 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 201 |
| origLegCallIdentifier | 16777502 |
| destLegIdentifier | 16777503 |
| callingPartyNumber | 20000 |
| origCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| lastRedirectDn | 20001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origDTMFMethod | 1 |
| destDTMFMethod | 1 |
| duration | 60 |

| FieldNames | Values |
|---|---|
| cdrRecordType | 1 |
| globalCallID_callManagerId | 1 |
| globalCallID_callId | 32009 |
| origLegCallIdentifier | 19654113 |
| dateTimeOrigination | 1221263718 |
| origNodeId | 1 |
| origSpan | 0 |
| origIpAddr | 1897990154 |
| callingPartyNumber | 1004 |
| origCause_value | 16 |
| origPrecedenceLevel | 4 |
| origMediaTransportAddress_IP | 1897990154 |
| origMediaTransportAddress_Port | 19824 |
| origMediaCap_payloadCapability | 4 |
| origMediaCap_maxFramesPerPacket | 20 |
| destLegIdentifier | 19654114 |
| destNodeId | 1 |
| destSpan | 19654114 |
| destIpAddr | 424630538 |
| originalCalledPartyNumber | 1003 |
| finalCalledPartyNumber | 1003 |
| destCause_value | 0 |
| destPrecedenceLevel | 4 |
| destMediaTransportAddress_IP | -1759442934 |
| destMediaTransportAddress_Port | 27508 |
| destMediaCap_payloadCapability | 4 |
| destMediaCap_maxFramesPerPacket | 20 |
| dateTimeConnect | 1221263720 |
| dateTimeDisconnect | 1221263721 |
| lastRedirectDn | 1003 |
| Pkid | c8868f84-0f4e-452c-a814-bf97a7fe69fc |
| Duration | 1 |
| origDeviceName | SEP003094C2B08C |
| destDeviceName | self-loop |
| origCallTerminationOnBehalfOf | 12 |
| destCallTerminationOnBehalfOf | 0 |
| origDTMFMethod | 3 |
| destDTMFMethod | 4 |
| origMediaCap_Bandwidth | 64 |
| destMediaCap_Bandwidth | 64 |
| origIpv4v6Addr | 10.8.33.113 |
| destIpv4v6Addr | 10.8.33.151 |
| IncomingProtocolID | 0 |
| IncomingProtocolCallRef |  |
| OutgoingProtocolID | 2 |
| OutgoingProtocolCallRef | 0053C43F6701B18C030004010A082171 |

| FieldNames | Values |
|---|---|
| cdrRecordType | 1 |
| globalCallID_callManagerId | 1 |
| globalCallID_callId | 32008 |
| origLegCallIdentifier | 19654111 |
| dateTimeOrigination | 1221263350 |
| origNodeId | 1 |
| origSpan | 2 |
| origIpAddr | 122640650 |
| callingPartyNumber | 1004 |
| origCause_value | 0 |
| origPrecedenceLevel | 4 |
| origMediaTransportAddress_IP | 122640650 |
| origMediaTransportAddress_Port | 17218 |
| origMediaCap_payloadCapability | 4 |
| origMediaCap_maxFramesPerPacket | 20 |
| destLegIdentifier | 19654112 |
| destNodeId | 1 |
| destSpan | 0 |
| destIpAddr | -1759442934 |
| originalCalledPartyNumber | 1003 |
| finalCalledPartyNumber | 1003 |
| destCause_value | 16 |
| destPrecedenceLevel | 4 |
| destMediaTransportAddress_IP | -1759442934 |
| destMediaTransportAddress_Port | 23350 |
| destMediaCap_payloadCapability | 4 |
| destMediaCap_maxFramesPerPacket | 20 |
| dateTimeConnect | 1221263351 |
| dateTimeDisconnect | 1221263352 |
| lastRedirectDn | 1003 |
| Pkid | b576bd8d-9703-4f66-ae45-64ae5c04738e |
| Duration | 1 |
| origDeviceName | BRI/S1/SU0/P1@nw052b-3640.cisco.com |
| destDeviceName | SEP003094C2D263 |
| origCallTerminationOnBehalfOf | 0 |
| destCallTerminationOnBehalfOf | 12 |
| origDTMFMethod | 1 |
| destDTMFMethod | 3 |
| origMediaCap_Bandwidth | 64 |
| destMediaCap_Bandwidth | 64 |
| origIpv4v6Addr | 10.89.79.7 |
| destIpv4v6Addr | 10.8.33.151 |
| IncomingProtocolID | 4 |
| IncomingProtocolCallRef | 01-1004-1003 |
| OutgoingProtocolID | 0 |
| OutgoingProtocolCallRef |  |

| Field Names | Values |
|---|---|
| globalCallID_callId | 100 |
| origLegCallIdentifier | 16777123 |
| destLegIdentifier | 16777124 |
| callingPartyNumber | 45000 |
| origCalledPartyNumber | 9728134987 |
| finalCalledPartyNumber | 9728134987 |
| lastRedirectDn | 9728134987 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| authCodeDescription | Legal1 |
| authorizationLevel | 1 |
| duration | 120 |
| authorizationCode | 12345 |

| Note | The unanswered call will not have any connect time since media is not connected for this call. The CDR will be logged regardless
                                          of the service parameter CdrLogCallsWithZeroDurationFlag if FAC is present in the call. |
|---|---|

| FieldNames | Orig Call CDR | Setup Call CDR | Conference CDR 1 | Conference CDR 2 | Conference CDR 3 | Final CDR |
|---|---|---|---|---|---|---|
| globalCallID_callId | 60015 | 60016 | 60015 | 60015 | 60015 | 60017 |
| origLegCallIdentifier | 23704372 | 23704374 | 23704373 | 23704372 | 23704376 | 23704377 |
| destLegIdentifier | 23704373 | 23704376 | 23704381 | 23704380 | 23704382 | 23704378 |
| callingPartyNumber | 136201 | 136201 | 136111 | 136201 | 136203 | 136201 |
| origCalledPartyNumber | 136111 | 136203 | b00105401002 | b00105401002 | b00105401002 | 136203 |
| finalCalledPartyNumber | 136111 | 136203 | b00105401002 | b00105401002 | b00105401002 | 136203 |
| lastRedirectDn | 136111 | 136203 | 136201 | 136201 | 136201 | 136203 |
| origCause_Value | 393216 | 0 | 16 | 393216 | 393216 | 0 |
| dest_CauseValue | 393216 | 0 | 393216 | 393216 | 393216 | 16 |
| authCodeDescription |  | Forward_FAC |  |  |  |  |
| authorizationLevel | 0 | 1 | 0 | 0 | 0 | 0 |
| Duration | 18 | 0 | 37 | 37 | 32 | 38 |
| authorizationCode |  | 124 |  |  |  |  |

| Note | The setup call CDR for this example is generated even though it is of zero duration since FAC is used for this call. |
|---|---|

| Field Names | CDR |
|---|---|
| globalCallID_callId | 12345 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 102 |
| callingPartyNumber | 9728134987 |
| originalCalledPartyNumber | 2001 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origCalledPartyRedirectReason | 15 |
| lastRedirectRedirectReason | 15 |
| origCalledPartyRedirectOnBehalfOf | 5 |
| lastRedirectRedirectOnBehalfOf | 5 |
| duration | 120 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 12346 |
| origLegCallIdentifier | 102 |
| destLegIdentifier | 105 |
| callingPartyNumber | 9728134987 |
| originalCalledPartyNumber | 1000 |
| finalCalledPartyNumber | 6000 |
| lastRedirectDn | 2000 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origCalledPartyRedirectReason | 15 |
| lastRedirectRedirectReason | 2 |
| origCalledPartyRedirectOnBehalfOf | 5 |
| lastRedirectRedirectOnBehalfOf | 5 |
| duration | 15 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 12347 |
| origLegCallIdentifier | 106 |
| destLegIdentifier | 108 |
| callingPartyNumber | 9728134987 |
| originalCalledPartyNumber | 4444 |
| finalCalledPartyNumber | 6666 |
| lastRedirectDn | 5555 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| origCalledPartyRedirectReason | 2 |
| lastRedirectRedirectReason | 1 |
| origCalledPartyRedirectOnBehalfOf | 5 |
| lastRedirectRedirectOnBehalfOf | 5 |
| duration | 30 |

| Field Names | CDR |
|---|---|
| callingPartyNumber | 1000 |
| callingPartyNumberPartition |  |
| originalCalledPartyNumber | 2000 |
| originalCalledPartyNumberPartition |  |
| finalCalledPartyNumber | 3001 |
| finalCalledPartyNumberPartition |  |
| origDeviceName | Phone 1000 |
| destDeviceName | Phone 3001 |
| huntPilotDN | 2000 |
| huntPilotPartition |  |

| Field Names | CDR |
|---|---|
| callingPartyNumber | 1000 |
| callingPartyNumberPartition |  |
| originalCalledPartyNumber | 2000 |
| originalCalledPartyNumberPartition |  |
| finalCalledPartyNumber | 2000 |
| finalCalledPartyNumberPartition |  |
| origDeviceName | Phone 1000 |
| destDeviceName | Phone 3001 |
| huntPilotDN | 2000 |
| huntPilotPartition |  |

| Field Names | CDR |
|---|---|
| callingPartyNumber | 1000 |
| callingPartyNumberPartition |  |
| originalCalledPartyNumber | 2000 |
| originalCalledPartyNumberPartition |  |
| finalCalledPartyNumber | 2000 |
| finalCalledPartyNumberPartition |  |
| origDeviceName | Phone 1000 |
| destDeviceName | Phone 3001 |
| huntPilotDN |  |
| huntPilotPartition |  |
| calledPartyPatternUsage | 7 |

| Note | If the call is not answered by any of the hunt group members, the finalCalledPartyNumber field shows the hunt pilot DN. The
                                          number shows a line group member DN only when one of the line group member answers the call. |
|---|---|

| Field Names | CDR |
|---|---|
| callingPartyNumber | 1000 |
| callingPartyNumberPartition |  |
| originalCalledPartyNumber | 2000 |
| originalCalledPartyNumberPartition |  |
| finalCalledPartyNumber | 2000 |
| finalCalledPartyNumberPartition |  |
| origDeviceName | Phone 1000 |
| destDeviceName | Phone 3001 |
| huntPilotDN |  |
| huntPilotPartition |  |
| calledPartyPatternUsage | 7 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 121 |
| origLegCallIdentifier | 101 |
| destLegIdentifier | 102 |
| callingPartyNumber | 51234 |
| originalCalledPartyNumber | 57890 |
| finalCalledPartyNumber | 57890 |
| lastRedirectDn | 57890 |
| origCause_Value | 0 |
| destCause_Value | 16 |
| origVideoCap_Codec | 103 |
| origVideoCap_Bandwidth | 352 |
| origVideoCap_Resolution | 0 |
| origVideoTransportAddress_IP | 187962284 |
| origVideoTransportAddress_Port | 2406 |
| destVideoCap_Codec | 103 |
| destVideoCap_Bandwidth | 352 |
| destVideoCap_Resolution | 0 |
| destVideoTransportAddress_IP | 288625580 |
| destVideoTransportAddress_Port | 2328 |
| origVideoCap_Codec_Channel2 | 103 |
| origVideoCap_Bandwidth_Channel2 | 352 |
| origVideoCap_Resolution_Channel2 | 0 |
| origVideoTransportAddress_IP_Channel2 | 187962284 |
| origVideoTransportAddress_Port_Channel2 | 2410 |
| origVideoChannel_Role_Channel2 | 0 |
| destVideoCap_Codec_Channel2 | 103 |
| destVideoCap_Bandwidth_Channel2 | 352 |
| destVideoCap_Resolution_Channel2 | 0 |
| destVideoTransportAddress_IP_Channel2 | 288625580 |
| destVideoTransportAddress_Port_Channel2 | 2330 |
| destVideoChannel_Role_Channel2 | 0 |

| Field Names | Definitions |
|---|---|
| origMediaCap_bandwidth | This integer field contains the audio bandwidth. |
| destMediaCap_bandwidth | This integer field contains the audio bandwidth. |

| Codec | Bandwidth |
|---|---|
| G711Alaw64k | 64 |
| G711Alaw56k | 56 |
| G711mu-law64k | 64 |
| G711mu-law56k | 56 |
| G722 64k | 64 |
| G722 56k | 56 |
| G722 48k | 48 |
| G7231 | 7 |
| G728 | 16 |
| G729 | 8 |
| G729AnnexA | 8 |
| Is11172AudioCap | 0 |
| Is13818AudioCap | 0 |
| G729AnnexB | 8 |
| G729AnnexAwAnnexB | 8 |
| GSM Full Rate | 13 |
| GSM Half Rate | 7 |
| GSM Enhanced Full Rate | 13 |
| Wideband 256K | 256 |
| Data 64k | 64 |
| Data 56k | 56 |
| G7221 32K | 32 |
| G7221 24K | 24 |
| AAC-LD (mpeg4-generic) | 256 |
| AAC-LD (MP4A-LATM) 128K | 128 |
| AAC-LD (MP4A-LATM) 64K | 64 |
| AAC-LD (MP4A-LATM) 56K | 56 |
| AAC-LD (MP4A-LATM) 48K | 48 |
| AAC-LD (MP4A-LATM) 32K | 32 |
| AAC-LD (MP4A-LATM) 24K | 24 |
| GSM | 13 |
| iLBC | 15 or 13 |
| iSAC | 32 |
| XV150 MR 729A | 8 |
| NSE VBD 729A | 8 |

| Field Names | iLBC CDR |
|---|---|
| globalCallID_callId | 121 |
| origLegCallIdentifier | 101 |
| destLegIdentifier | 102 |
| callingPartyNumber | 51234 |
| originalCalledPartyNumber | 57890 |
| finalCalledPartyNumber | 57890 |
| lastRedirectDn | 57890 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origMediaCap_payloadCapability | 86 |
| origMediaCap_Bandwidth | 15 |
| destMediaCap_payloadCapability | 86 |
| destMediaCap_Bandwidth | 15 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| lastRedirectRedirectOnBehalfOf | 30 |
| lastRedirectRedirectReason | 0 |
| duration | 10 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| origTerminationOnBehalfOf | 30 |
| lastRedirectRedirectOnBehalfOf | 30 |
| lastRedirectRedirectReason | 496 OR 512 OR 528 OR 544 OR 560 OR 576 OR 592 OR 608 OR 624 OR 640 OR 656 OR 672 OR 688 OR 704 |
| origCause_Value | 31 |
| duration | 0 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| lastRedirectRedirectOnBehalfOf | 30 |
| lastRedirectRedirectReason | 496 OR 512 OR 528 OR 544 OR 560 OR 576 OR 592 OR 608 OR 624 OR 640 OR 656 OR 672 OR 688 OR 704 |
| duration | 10 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| OrigTerminationOnBehalfOf | 30 |
| lastRedirectRedirectOnBehalfOf | 30 |
| origCause_value | 132 |
| duration | 5 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| lastRedirectRedirectOnBehalfOf | 31 |
| joinOnBehalfOf | 31 |
| lastRedirectRedirectReason | 722 |
| duration | 5 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| lastRedirectRedirectOnBehalfOf | 30 |
| lastRedirectRedirectReason | 0 |
| duration | 5 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| OrigTerminationOnBehalfOf | 31 |
| origCause_value | Existing PSTN GW cause codes |
| duration | 0 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| lastRedirectRedirectOnBehalfOf | 30 |
| lastRedirectRedirectReason | 0 |
| duration | 5 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9728134987 |
| OrigTerminationOnBehalfOf | 31 |
| origCause_value | 133 OR 134 OR existing cause codes |
| duration | 0 |

| Note | If the call gets redirected by IDivert in the Alerting state, only one CDR gets generated. |
|---|---|

| Field Names | Original call CDR |
|---|---|
| globalCallID_callId | 37 |
| origLegCallIdentifier | 16777327 |
| destLegIdentifier | 16777329 |
| callingPartyNumber | 40003 |
| origCalledPartyNumber | 40001 |
| finalCalledPartyNumber | 40000 |
| lastRedirectDn | 40001 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| origCalledPartyRedirectReason | 50 |
| lastRedirectRedirectReason | 50 |
| origCalledPartyRedirectOnBehalfOf | 14 |
| lastRedirectRedirectOnBehalfOf | 14 |
| joinOnBehalfOf | 14 |

| Field Names | Original Connected Call CDR | Diverted Call CDR |
|---|---|---|
| globalCallID_callId | 38 | 38 |
| origLegCallIdentifier | 16777330 | 16777330 |
| destLegIdentifier | 16777331 | 16777332 |
| callingPartyNumber | 40003 | 40003 |
| origCalledPartyNumber | 40001 | 40001 |
| finalCalledPartyNumber | 40001 | 40000 |
| lastRedirectDn | 40001 | 40001 |
| origCause_Value | 0 | 16 |
| dest_CauseValue | 0 | 0 |
| origCalledPartyRedirectReason | 0 | 50 |
| lastRedirectRedirectReason | 0 | 50 |
| origCalledPartyRedirectOnBehalfOf |  | 14 |
| lastRedirectRedirectOnBehalfOf |  | 14 |
| origTerminationOnBehalfOf | 14 | 14 |
| destTerminationOnBehalfOf | 14 | 12 |
| joinOnBehalfOf |  | 14 |

| CDR | Side A | Side B |
|---|---|---|
| parties | icid | orig_ioi | term_ioi | icid | orig_ioi | term_ioi |
| A-B | PCV1 | IOI_1 | IOI_2 | PCV1 | IOI_1 | IOI_2 |

| Fields Names | CDR |
|---|---|
| globalCallID_callId | 3 |
| origLegCallIdentifier | 300 |
| destLegIdentifier | 301 |
| origDeviceName | CUCM_ISC_TRUNK1 |
| destDeviceName | CUCM_ISC_TRUNK2 |
| IncomingICID | 5802170000010000000000A85552590A |
| IncomingOrigIOI | rcdn-85.swyan.open-ims.test |
| IncomingTermIOI | rcdn-86.swyan.open-ims.test |
| OutgoingICID | 5802170000010000000000A85552590A |
| OutgoingOrigIOI | rcdn-85.swyan.open-ims.test |
| OutgoingTermIOI | rcdn-86.swyan.open-ims.test |

| Field Names | Original Call CDR |
|---|---|
| globalCallID_callId | 1111000 |
| origLegCallIdentifier | 21822467 |
| destLegIdentifier | 21822468 |
| callingPartyNumber | 20000 |
| originalCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| origMediaTransportAddress_IP | 0 |
| origMediaTransportAddress_Port | 0 |
| destMediaTransportAddress_IP | -47446006 |
| destMediaTransportAddress_Port | 28480 |
| origCalledPartyNumberPartition | Intercom |
| callingPartyNumberPartition | Intercom |
| finalCalledPartyNumberPartition | Intercom |
| duration | 5 |

| Field Names | Original Call CDR |
|---|---|
| globalCallID_callId | 1111000 |
| origLegCallIdentifier | 21822469 |
| destLegIdentifier | 21822470 |
| callingPartyNumber | 20000 |
| originalCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| origMediaTransportAddress_IP | -131332086 |
| origMediaTransportAddress_Port | 29458 |
| destMediaTransportAddress_IP | -47446006 |
| destMediaTransportAddress_Port | 29164 |
| origCalledPartyNumberPartition | Intercom |
| callingPartyNumberPartition | Intercom |
| finalCalledPartyNumberPartition | Intercom |
| duration | 5 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origIpAddr | 352737802 |
| destIpAddr | 1878566390 |
| origIpv4v6Addr | 10.90.6.21 |
| destIpv4v6Addr | 10.90.7.144 |
| duration | 60 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origIpAddr | 0 |
| destIpAddr | 0 |
| origIpv4v6Addr | 2001:fecd:ba23:cd1f:dcb1:1010:9234:40881 |
| destIpv4v6Addr | 2001:420:1e00:e5:217:8ff:fe5c:2fa9 |
| duration | 60 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origIpAddr | 352737802 |
| destIpAddr | -1878566390 |
| origIpv4v6Addr | 10.90.6.21 |
| destIpv4v6Addr | 10.90.7.144 |
| duration | 60 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origIpAddr | 352737802 |
| destIpAddr | -1878566390 |
| origIpv4v6Addr | 10.90.6.21 |
| destIpv4v6Addr | 10.90.7.144 |
| duration | 60 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origIpAddr | 352737802 |
| destIpAddr | 0 |
| origIpv4v6Addr | 2001:fecd:ba23:cd1f:dcb1:1010:9234:4088 |
| destIpv4v6Addr | 2001:420:1e00:e5:217:8ff:fe5c:2fa9 |
| duration | 60 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origIpAddr | 352737802 |
| destIpAddr | -569419254 |
| origIpv4v6Addr | 10.90.15.222 |
| destIpv4v6Addr |  |
| duration | 0 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origIpAddr | 0 |
| destIpAddr | 0 |
| origIpv4v6Addr | 2001:fecd:ba23:cd1f:dcb1:1010:9234:4088 |
| destIpv4v6Addr |  |
| duration | 0 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 22 |
| origLegCallIdentifier | 1 |
| destLegIdentifier | 2 |
| callingPartyNumber | 9728134987 |
| originalCalledPartyNumber | 2001 |
| finalCalledPartyNumber | 2002 |
| lastRedirectDn | 2001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origCalledPartyRedirectReason | 0 |
| lastRedirectRedirectReason | 5 |
| origCalledPartyRedirectOnBehalfOf | 16 |
| lastRedirectRedirectOnBehalfOf | 16 |
| duration | 120 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | +12145551212 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| duration | 60 |
| outpulsedCalledPartyNumber | 12145551212 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | +12145551212 |
| finalCalledPartyNumber | +12145551212 |
| lastRedirectDn | +12145551212 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| duration | 60 |
| outpulsedCalledPartyNumber | 2145551212 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 9900 |
| finalCalledPartyNumber | 9900 |
| lastRedirectDn | 9900 |
| origCause_Value | 0 |
| dest_CauseValue | 419430421 |
| duration | 0 |

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 89224001 |
| originalCalledPartyNumber | 82291002 |
| finalCalledPartyNumber | 41549901 |
| lastRedirectDn | 82291002 |
| origCause_Value | 0 |
| dest_CauseValue | -1493172161 |
| duration | 0 |

| Calling Party | Calling Partition | Original Called Party | Original Called Partition | Orig Cause | Dest Cause | Comment |
|---|---|---|---|---|---|---|
| 9728552001 | CUST | 5555 | ACNTS | 0 | 16 | "callFlag=MALICIOUS" |

|  | Calling Party | Calling Partition | Original Called Party | Original Called Partition | Final Called Party | Final Called Partition | Last Redirect Party | Last Redirect Partition | Duration |
|---|---|---|---|---|---|---|---|---|---|
| A | 2001 | Accounts | 5001 |  | b0019901001 |  | b0019901001 |  | 70 |
| B | 2002 | Accounts | 5001 |  | b0019901001 |  | b0019901001 |  | 65 |
| C | 2003 | Accounts | 5001 |  | b0019901001 |  | b0019901001 |  | 80 |

| Mobility Feature | mobileCallType Value |
|---|---|
| Nonmobility call | 0 |
| Dial via Office Reverse Callback | 1 |
| Dial via Office Forward | 2 |
| Reroute remote destination call to enterprise network | 4 |
| Mobile Connect | 8 |
| Interactive Voice Response | 10 |
| Enterprise Feature Access | 20 |
| Hand-In | 40 |
| Hand-Out | 80 |
| Redial | 100 |
| Least Cost Routing with dial-via-office reverse callback | 200 |
| Least Cost Routing with dial-via-office forward | 82 |
| Send call to mobile | 800 |
| Session handoff | 1000 |

| Mobility Feature | lastRedirectReason Value |
|---|---|
| Hand-In | 303 |
| Hand-Out | 319 |
| Mobile Connect | 335 |
| Redial | 351 |
| Interactive Voice Response | 399 |
| Dial via Office Reverse Callback | 401 |
| Enterprise Feature Access | 402 |
| Session Handoff | 403 |
| Send call to mobile | 415 |
| Reroute remote destination call to enterprise network | 783 |

| Field | Dial via Office Reverse Callback CDR |
|---|---|
| origCallTerminationOnBehalfOf | 0 |
| destCallTerminationOnBehalfOf | 12 |
| origCalledRedirectOnBehalfOf | 24 |
| lastRedirectOnBehalfOf | 24 |
| joinOnBehalfOf | 24 |
| origCalledPartyRedirectReason | 401 |
| lastRedirectReason | 401 |
| origDeviceName | 10.194.108.70 |
| destDeviceName | SEP001FCAE9004 |
| finalCalledPartyNumber | 2000 |
| huntPilotDN |  |
| mobileCallingPartyNumber | 2145551234 |
| finalMobileCalledPartyNumber |  |
| origMobileDeviceName | BOTSAU |
| destMobileDeviceName |  |
| origMobileCallDuration | 55 |
| destMobileCallDuration |  |
| mobileCallType | 1 |

| Field | Dial via Office Forward CDR |
|---|---|
| origCallTerminationOnBehalfOf | 0 |
| destCallTerminationOnBehalfOf | 12 |
| origCalledRedirectOnBehalfOf | 0 |
| lastRedirectOnBehalfOf | 0 |
| joinOnBehalfOf | 0 |
| origCalledPartyRedirectReason | 0 |
| lastRedirectReason | 0 |
| origDeviceName | 10.194.108.70 |
| destDeviceName | SEP001FCAE90004 |
| finalCalledPartyNumber | 823006 |
| huntPilotDN |  |
| mobileCallingPartyNumber | 2145551234 |
| finalMobileCalledPartyNumber |  |
| origMobileDeviceName | BOTSAU |
| destMobileDeviceName |  |
| origMobileCallDuration | 120 |
| destMobileCallDuration | 0 |
| mobileCallType | 2 |

| Field | Reroute Remote Detination CDR |
|---|---|
| origCallTerminationOnBehalfOf | 0 |
| destCallTerminationOnBehalfOf | 12 |
| origCalledRedirectOnBehalfOf | 24 |
| lastRedirectOnBehalfOf | 24 |
| joinOnBehalfOf | 0 |
| origCalledPartyRedirectReason | 783 |
| lastRedirectReason | 783 |
| origDeviceName | SEP001FCAE90004 |
| destDeviceName | GW_SIP |
| finalCalledPartyNumber | 1000 |
| huntPilotDN |  |
| mobileCallingPartyNumber |  |
| finalMobileCalledPartyNumber | 2145551234 |
| origMobileDeviceName |  |
| destMobileDeviceName | 2145551234:rdp |
| origMobileCallDuration | 0 |
| destMobileCallDuration | 60 |
| mobileCallType | 4 |

| Field | Desktop Call Pickup CDR |
|---|---|
| origCallTerminationOnBehalfOf | 0 |
| destCallTerminationOnBehalfOf | 12 |
| origCalledRedirectOnBehalfOf | 0 |
| lastRedirectOnBehalfOf | 0 |
| joinOnBehalfOf | 0 |
| origCalledPartyRedirectReason | 0 |
| lastRedirectReason | 0 |
| origDeviceName | SEP001FCAE90004 |
| destDeviceName | GW_SIP |
| finalCalledPartyNumber | 1000 |
| huntPilotDN |  |
| mobileCallingPartyNumber |  |
| finalMobileCalledPartyNumber |  |
| origMobileDeviceName |  |
| destMobileDeviceName |  |
| origMobileCallDuration | 0 |
| destMobileCallDuration | 10 |
| mobileCallType | 8 |

| Field | CDR |
|---|---|
| origCallTerminationOnBehalfOf | 0 |
| destCallTerminationOnBehalfOf | 12 |
| origCalledRedirectOnBehalfOf | 0 |
| lastRedirectOnBehalfOf | 0 |
| joinOnBehalfOf | 0 |
| origCalledPartyRedirectReason | 0 |
| lastRedirectReason | 0 |
| origDeviceName | SEP001FCAE90004 |
| destDeviceName | GW_SIP |
| finalCalledPartyNumber | 1000 |
| huntPilotDN |  |
| mobileCallingPartyNumber |  |
| finalMobileCalledPartyNumber | 2145551234 |
| origMobileDeviceName |  |
| destMobileDeviceName | BOTSARAH |
| origMobileCallDuration | 0 |
| destMobileCallDuration | 10 |
| mobileCallType | 8 |

| Field | Announcement to user | 0 Duration Call | IP Phone to Mobile Phone |
|---|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 24 | 12 |
| destCallTerminationOnBehalfOf | 24 | 24 | 24 |
| origCalledRedirectOnBehalfOf | 24 | 24 | 24 |
| lastRedirectOnBehalfOf | 24 | 24 | 24 |
| joinOnBehalfOf | 0 | 0 | 24 |
| origCalledPartyRedirectReason | 335 | 335 | 335 |
| lastRedirectReason | 335 | 335 | 335 |
| origDeviceName | SEP001FCAE91231 | ParkingLotDevice | SEP001FCAE91231 |
| destDeviceName | GW_SIP | GW_SIP | GW_SIP |
| finalCalledPartyNumber | 238006 | 238006 | 238006 |
| huntPilotDN |  |  |  |
| mobileCallingPartyNumber |  |  |  |
| finalMobileCalledPartyNumber | 14089022179 | 14089022179 | 14089022179 |
| origMobileDeviceName |  |  |  |
| destMobileDeviceName | 14089022179:rdp | 14089022179:rdp | 14089022179:rdp |
| origMobileCallDuration | 0 | 0 |  |
| destMobileCallDuration | 3 |  | 6 |
| mobileCallType | 8 | 8 | 8 |

| Field | Mobile Phone to Unified Communications Manager | Mobile Phone to Desk Phone |
|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 12 |
| destCallTerminationOnBehalfOf | 24 | 24 |
| origCalledRedirectOnBehalfOf | 24 | 24 |
| lastRedirectOnBehalfOf | 24 | 24 |
| joinOnBehalfOf | 24 | 24 |
| origCalledPartyRedirectReason | 402 | 402 |
| lastRedirectReason | 402 | 402 |
| origDeviceName | GW_SIP | GW_SIP |
| destDeviceName | ParkingLotDevice | SEP001FCAE91231 |
| finalCalledPartyNumber | 00111101001 | 238011 |
| huntPilotDN |  |  |
| mobileCallingPartyNumber | 14089022179 | 14089022179 |
| finalMobileCalledPartyNumber |  |  |
| origMobileDeviceName | 14089022179:rdp | 14089022179:rdp |
| destMobileDeviceName |  |  |
| origMobileCallDuration | 5 | 25 |
| destMobileCallDuration | 0 |  |
| mobileCallType | 32 | 32 |

| Field | Mobile Phone to Desk Phone |
|---|---|
| origCallTerminationOnBehalfOf | 12 |
| destCallTerminationOnBehalfOf | 0 |
| origCalledRedirectOnBehalfOf | 24 |
| lastRedirectOnBehalfOf | 24 |
| joinOnBehalfOf | 24 |
| origCalledPartyRedirectReason | 399 |
| lastRedirectReason | 399 |
| origDeviceName | GW_SIP |
| destDeviceName | SEP00000000000002 |
| finalCalledPartyNumber | 238011 |
| huntPilotDN |  |
| mobileCallingPartyNumber | 14089022179 |
| finalMobileCalledPartyNumber |  |
| origMobileDeviceName | 14089022179:rdp |
| destMobileDeviceName |  |
| origMobileCallDuration | 60 |
| destMobileCallDuration |  |
| mobileCallType | 16 |

| Field | IP Phone to Cellular Phone | IP Phone to IP Phone |
|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 12 |
| destCallTerminationOnBehalfOf | 24 | 24 |
| origCalledRedirectOnBehalfOf | 0 | 0 |
| lastRedirectOnBehalfOf | 0 | 24 |
| joinOnBehalfOf | 0 | 24 |
| origCalledPartyRedirectReason | 0 | 303 |
| lastRedirectReason | 0 | 303 |
| origDeviceName | SEP001FCAE91231 | SEP001FCAE91231 |
| destDeviceName | GW_SIP | TCTSAU |
| finalCalledPartyNumber | 238006 | 238006 |
| huntPilotDN |  |  |
| mobileCallingPartyNumber |  |  |
| finalMobileCalledPartyNumber | 14089022179 |  |
| origMobileDeviceName |  |  |
| destMobileDeviceName | TCTSAU |  |
| origMobileCallDuration | 0 | 0 |
| destMobileCallDuration | 55 |  |
| mobileCallType | 8 | 72 |

| Field | IP Phone to IP Phone | IP Phone to Cell Network |
|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 0 |
| destCallTerminationOnBehalfOf | 24 | 12 |
| origCalledRedirectOnBehalfOf | 0 | 0 |
| lastRedirectOnBehalfOf | 0 | 24 |
| joinOnBehalfOf | 0 | 24 |
| origCalledPartyRedirectReason | 0 | 0 |
| lastRedirectReason | 0 | 319 |
| origDeviceName | SEP001FCAE94005 | SEP001FCAE94005 |
| destDeviceName | TCTSAU | GW_SIP |
| finalCalledPartyNumber | 238006 | 238006 |
| huntPilotDN |  |  |
| mobileCallingPartyNumber |  |  |
| finalMobileCalledPartyNumber |  | 14089022179 |
| origMobileDeviceName |  |  |
| destMobileDeviceName |  | TCTSAU |
| origMobileCallDuration | 0 | 0 |
| destMobileCallDuration | 0 | 23 |
| mobileCallType | 0 | 128 |

| Field | DVOR callback | IP phone to IP phone | Mobile phone to IP phone |
|---|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 24 | 0 |
| destCallTerminationOnBehalfOf | 24 | 24 | 12 |
| origCalledRedirectOnBehalfOf | 0 | 0 | 0 |
| lastRedirectOnBehalfOf | 0 | 0 | 24 |
| joinOnBehalfOf | 0 | 0 | 24 |
| origCalledPartyRedirectReason | 0 | 0 | 0 |
| lastRedirectReason | 0 | 0 | 319 |
| origDeviceName | ParkingLotDevice | BOTSAU | GW_SIP |
| destDeviceName | GW_SIP | SEP001FCAE91231 | SEP001FCAE91231 |
| finalCalledPartyNumber | 238006 | 238011 | 238011 |
| huntPilotDN |  |  |  |
| mobileCallingPartyNumber |  |  | 14089022179 |
| finalMobileCalledPartyNumber | 14089022179 |  |  |
| origMobileDeviceName |  |  | BOTSAU |
| destMobileDeviceName | BOTSAU |  |  |
| origMobileCallDuration | 0 | 0 | 35 |
| destMobileCallDuration | 0 | 0 |  |
| mobileCallType | 0 | 0 | 512 |

| Field | IP Phone to IP Phone | Mobile Phone to IP Phone |
|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 12 |
| destCallTerminationOnBehalfOf | 24 | 0 |
| origCalledRedirectOnBehalfOf | 0 | 0 |
| lastRedirectOnBehalfOf | 0 | 24 |
| joinOnBehalfOf | 0 | 24 |
| origCalledPartyRedirectReason | 0 | 0 |
| lastRedirectReason | 0 | 319 |
| origDeviceName | BOTSAU | GW_SIP |
| destDeviceName | SEP001FCAE91006 | SEP001FCAE91006 |
| finalCalledPartyNumber | 238011 | 238011 |
| huntPilotDN |  |  |
| mobileCallingPartyNumber |  | 14089022179 |
| finalMobileCalledPartyNumber |  |  |
| origMobileDeviceName |  | BOTSAU |
| destMobileDeviceName |  |  |
| origMobileCallDuration | 0 | 0 |
| destMobileCallDuration | 0 | 25 |
| mobileCallType | 0 | 130 |

| Field | Announcement | IP Phone to IP Phone | IP Phone to Mobile Phone |
|---|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 24 | 24 |
| destCallTerminationOnBehalfOf | 24 | 24 | 12 |
| origCalledRedirectOnBehalfOf | 0 | 0 | 0 |
| lastRedirectOnBehalfOf | 0 | 0 | 24 |
| joinOnBehalfOf | 0 | 0 | 24 |
| origCalledPartyRedirectReason | 0 | 0 | 0 |
| lastRedirectReason | 0 | 0 | 415 |
| origDeviceName | SEP001FCAE90001 | SEP001FCAE90001 | SEP001FCAE90001 |
| destDeviceName | GW_SIP | SEP001FCAE90022 | GW_SIP |
| finalCalledPartyNumber | 238006 | 238006 | 238006 |
| huntPilotDN |  |  |  |
| mobileCallingPartyNumber |  |  |  |
| finalMobileCalledPartyNumber | 12145551234 |  | 12145551234 |
| origMobileDeviceName |  |  |  |
| destMobileDeviceName | BOTSAU |  | BOTSAU |
| origMobileCallDuration | 0 | 0 | 0 |
| destMobileCallDuration | 0 | 0 | 35 |
| mobileCallType | 0 | 0 | 2048 |

| Field | Parking Lot to Desk Phone | IP Phone to Mobile Phone | IP Phone to IP Phone |
|---|---|---|---|
| origCallTerminationOnBehalfOf | 24 | 24 | 24 |
| destCallTerminationOnBehalfOf | 24 | 24 | 12 |
| origCalledRedirectOnBehalfOf | 0 | 0 | 0 |
| lastRedirectOnBehalfOf | 0 | 0 | 24 |
| joinOnBehalfOf | 0 | 0 | 24 |
| origCalledPartyRedirectReason | 0 | 0 | 0 |
| lastRedirectReason | 0 | 0 | 403 |
| origDeviceName | SEP001FCAE90001 | SEP001FCAE90001 | SEP001FCAE90001 |
| destDeviceName | SEP001FCAE90022 | BOTSARAH | SEP001FCAE90022 |
| finalCalledPartyNumber | 2500 | 2500 | 2500 |
| huntPilotDN |  |  |  |
| mobileCallingPartyNumber |  |  |  |
| finalMobileCalledPartyNumber |  | 2145551234 |  |
| origMobileDeviceName |  |  |  |
| destMobileDeviceName |  | BOTSARAH |  |
| origMobileCallDuration | 0 | 0 | 0 |
| destMobileCallDuration | 0 | 15 | 10 |
| mobileCallType | 0 | 0 | 5096 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 87029 |
| origLegCallIdentifier | 30117105 |
| callingPartyNumber | 1002 |
| originalCalledPartyNumber | 2000 |
| wasCallQueued | 1 |
| totalWaitTimeInQueue | 30 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| duration | 60 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | 2001 |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| duration | 60 |

| Call | CallingPartyNumber | originalCalledPartyNumber |
|---|---|---|
| 1 | 4001 | 4002 |
| 2 | 4002 | 4003 |
| 3 | 4001 | 4003 |

| Note | No originalCallingParty field exists in the CDR. |
|---|---|

| Note | In the following example, 2000 represents the main personal assistant route point to reach personal assistant, 21XX represents
                                             the personal assistant interceptor route point, and 2001-2004 represents the media port. |
|---|---|

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2101 | 16777217 | PAManaged | 16777219 | 2004 | Phones | 2000 | 1023970182 | 2000 | Phones | 34 |
| 2004 | 16777221 | Phones | 16777222 | 2105 | PAManaged | 2105 | 1023970182 | 2105 | PAManaged | 0 |
| 2101 | 16777217 | PAManaged | 16777222 | 2105 | PAManaged | 2105 | 1023970191 | 2105 | PAManaged | 5 |

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2002 | 16777234 | Phones | 16777285 | 2105 | PAManaged | 2105 | 1023970478 | 2105 | PAManaged | 2 |
| 2101 | 16777230 | PAManaged | 16777232 | 2002 | PA | 2105 | 1023970478 | 21xx | " " | 9 |
| 2105 | 16777235 | PAManaged | 16777230 | 2101 | " " | " " | 1023970483 | " " | " " | 5 |

| Calling Party Number | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Number | FinalCalled Party Number Partition | Original Called Party Number | Original Called Party Number Partition | Last Redirect DN | Last Redirect DN Partition | Duration(secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2101 | 16777240 | PAManaged | 16777242 | 2105 | PA | 2105 | 1023970710 | 21XX | " " | 8 |

| Calling Party Number | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Number | FinalCalled Party Number Partition | Original Called Party Number | Original Called Party Number Partition | Last Redirect DN | Last Redirect DN Partition | Duration(secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2101 | 16777240 | PAManaged | 16777242 | 2110 | PA | 2105 | 1023970710 | 21XX | " " | 8 |

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2004 | 16777262 | Phones | 16777263 | 2110 | PAManaged | 2110 | 1023971303 | 2110 | PAManaged | 6 |
| 2101 | 16777258 | PAManaged | 16777260 | 2004 | Phones | 2000 | 1023971303 | 2000 | Phones | 22 |
| 2110 | 16777263 | PAManaged | 16777258 | 2101 | " " | " " | 1023971312 | " " | " " | 9 |

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2001 | 16777269 | Phones | 16777270 | 2110 | PAManaged | 2110 | 1023971456 | 2110 | PAManaged | 0 |
| 2001 | 16777272 | Phones | 16777273 | 2120 | PAManaged | 2120 | 1023971467 | 2120 | PAManaged | 4 |
| 2101 | 16777265 | PAManaged | 16777267 | 2001 | Phones | 2000 | 1023971467 | 2000 | Phones | 37 |
| 2120 | 16777273 | PAManaged | 16777265 | 2101 | " " | " " | 1023971474 | " " | " " | 7 |
| 2110 | 16777275 | PAManaged | 0 | " " | " " | " " | 1023971476 | " " | " " | 0 |

| Note | 2105 (the original destination) represents the third destination in this case. |
|---|---|

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2002 | 16777281 | Phones | 16777282 | 2110 | PAManaged | 2110 | 1023971602 | 2110 | PAManaged | 0 |
| 2002 | 16777284 | Phones | 16777285 | 2120 | PAManaged | 2120 | 1023971615 | 2120 | PAManaged | 0 |
| 2101 | 16777277 | PAManaged | 16777279 | 2002 | Phones | 2000 | 1023971619 | 2000 | Phones | 38 |
| 2002 | 16777287 | Phones | 16777288 | 2105 | PAManaged | 2105 | 1023971619 | 2105 | PAManaged | 0 |
| 2101 | 16777277 | PAManaged | 16777288 | 2105 | PAManaged | 2105 | 1023971627 | 2105 | PAManaged | 7 |
| 2105 | 16777289 | PAManaged | 0 | " " | " " | " " | 1023971629 | " " | " " | 0 |

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2003 | 16777295 | Phones | 16777296 | 2110 | PAManaged | 2110 | 1023971740 | 2110 | PAManaged | 4 |
| 2101 | 16777291 | PAManaged | 16777293 | 2003 | PA | 2105 | 1023971740 | 21XX | " " | 10 |
| 2110 | 16777296 | PAManaged | 16777291 | 2101 | " " | " " | 1023971749 | " " | " " | 9 |

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2004 | 16777302 | Phones | 16777303 | 2110 | PAManaged | 2110 | 1023971815 | 2110 | PAManaged | 0 |
| 2004 | 16777305 | Phones | 16777306 | 2120 | PAManaged | 2120 | 1023971824 | 2120 | PAManaged | 3 |
| 2101 | 16777298 | PAManaged | 16777300 | 2004 | PA | 2105 | 1023971824 | 21XX | " " | 22 |
| 2120 | 16777306 | PAManaged | 16777298 | 2101 | " " | " " | 1023971832 | " " | " " | 8 |

| Note | 2110 (the original destination) represents the third destination in this case. |
|---|---|

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition | Original Called Party Num | Original Called Party Number Partition | Last Redir DN | Last Redirect DN Partition | Duration (secs) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2001 | 16777312 | Phones | 16777313 | 2110 | PAManaged | 2110 | 1023971923 | 2110 | PAManaged | 0 |
| 2001 | 16777315 | Phones | 16777316 | 2120 | PAManaged | 2120 | 1023971936 | 2120 | PAManaged | 0 |
| 2101 | 16777308 | PAManaged | 16777310 | 2001 | PA | 2105 | 1023971940 | 21XX | " " | 30 |
| 2001 | 16777318 | Phones | 16777319 | 2105 | PAManaged | 2105 | 1023971940 | 2105 | PAManaged | 0 |
| 2101 | 16777308 | PAManaged | 16777319 | 2105 | PAManaged | 2105 | 1023971953 | 2105 | PAManaged | 12 |

| Calling Party Num | OrigLegCall Identifier | Calling Party Number Partition | DestLeg Identifier | Final Called Party Num | Final Called Party Number Partition |
|---|---|---|---|---|---|
| 2003 | 16777345 | Phones | 16777346 | 2105 | PAManaged |
| 2101 | 16777340 | PAManaged | 16777342 | 2003 | Phones |
| 2003 | 16777350 | Phones | 16777351 | 2002 | PAManaged |
| 2003 | 16777342 | Phones | 16777347 | 2110 | " " |
| 2110 | 16777351 | PAManaged | 16777352 | b00110201001 | " " |
| 2105 | 16777346 | PAManaged | 16777349 | b00110201001 | " " |
| 2101 | 16777340 | PAManaged | 16777348 | b00110201001 | " " |

| Original CalledParty Number | Original Called Party Number Partition | Last Redirect DN | Last Redirect DN Partition | Duration (seconds) |
|---|---|---|---|---|
| 2105 | 1023972575 | 2105 | PAManaged | 6 |
| 2000 | 1023972576 | 2003 | Phones | 62 |
| 2110 | 1023972595 | 2110 | PAManaged | 39 |
| b00110201001 | 1023972601 | b00110201001 | " " | 25 |
| b00110201001 | 1023972609 | b00110201001 | " " | 14 |
| b00110201001 | 1023972610 | b00110201001 | " " | 34 |
| b00110201001 | 1023972610 | b00110201001 | " " | 34 |

| Field Names | Precedence Call CDR |
|---|---|
| globalCallID_callId | 100 |
| origLegCallIdentifier | 12345 |
| destLegIdentifier | 12346 |
| callingPartyNumber | 2001 |
| origCalledPartyNumber | 826001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origPrecedenceLevel | 2 |
| destPrecedenceLevel | 2 |

| Field Names | Precedence Call CDR |
|---|---|
| globalCallID_callId | 102 |
| origLegCallIdentifier | 11111 |
| destLegIdentifier | 11112 |
| callingPartyNumber | 9728552001 |
| origCalledPartyNumber | 6001 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| origPrecedenceLevel | 1 |
| destPrecedenceLevel | 1 |

| Field Names | Original call CDR | Higher Level Call CDR |
|---|---|---|
| globalCallID_callId | 10000 | 10001 |
| origLegCallIdentifier | 12345678 | 12345680 |
| destLegIdentifier | 12345679 | 12345681 |
| callingPartyNumber | 2001 | 9728551234 |
| origCalledPartyNumber | 826001 | 826001 |
| origCause_Value | 0 | 0 |
| dest_CauseValue | 9 | 16 |
| origPrecedenceLevel | 2 | 1 |
| destPrecedenceLevel | 2 | 1 |

| Field Names | Original Call CDR |
|---|---|
| globalCallID_callId | 11 |
| origLegCallIdentifier | 21832023 |
| destLegIdentifier | 21832026 |
| callingPartyNumber | 35010 |
| originalCalledPartyNumber | 10010 |
| finalCalledPartyNumber | 10000 |
| lastRedirectDn | 10010 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origCalledPartyRedirectReason | 162 |
| lastRedirectRedirectReason | 162 |
| origCalledPartyRedirectOnBehalfOf | 19 |
| lastRedirectRedirectOnBehalfOf | 19 |
| origTerminationOnBehalfOf | 0 |
| destTerminationOnBehalfOf | 12 |
| joinOnBehalfOf | 19 |
| duration | 60 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 115010 |
| origLegCallIdentifier | 30751507 |
| callingPartyNumber | 180000 |
| outpulsedCallingPartyNumber | 880003 |
| outpulsedOriginalCalledPartyNumber | +91110001 |
| outpulsedLastRedirectingNumber | +91220002 |

| Note | When the transfer is complete, the system sends an Invite with Replaces to Unified Communications Manager . |
|---|---|

| Field Names | Original Call CDR | Reverted Call CDR |
|---|---|---|
| globalCallID_callId | 5045247 | 5045248 |
| origLegCallIdentifier | 21822467 | 21822469 |
| destLegIdentifier | 21822468 | 21822468 |
| callingPartyNumber | 35010 | 35020 |
| originalCalledPartyNumber | 3000 | 3000 |
| finalCalledPartyNumber | 3000 | 3000 |
| lastRedirectDn | 3000 | 35010 |
| origCause_Value | 393216 | 0 |
| dest_CauseValue | 393216 | 16 |
| origCalledPartyRedirectReason | 0 | 0 |
| lastRedirectRedirectReason | 0 | 146 |
| origCalledPartyRedirectOnBehalfOf | 0 | 0 |
| lastRedirectRedirectOnBehalfOf | 0 | 18 |
| origTerminationOnBehalfOf | 18 | 0 |
| destTerminationOnBehalfOf | 18 | 12 |
| joinOnBehalfOf | 0 | 18 |
| duration | 5 | 60 |

| Note | When the transfer completes, a Refer with Replaces gets sent to Unified Communications Manager . |
|---|---|

| Field Names | Original Call CDR | Consultation Call CDR | Final Transferred Call CDR |
|---|---|---|---|
| globalCallID_callId | 5045245 | 5045246 | 5045245 |
| origLegCallIdentifier | 21822461 | 21822463 | 21822462 |
| destLegIdentifier | 21822462 | 21822464 | 21822464 |
| callingPartyNumber | 35010 | 35010 | 3000 |
| originalCalledPartyNumber | 3000 | 3001 | 3001 |
| finalCalledPartyNumber | 3000 | 3001 | 3001 |
| lastRedirectDn | 3000 | 3001 | 35010 |
| origCause_Value | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 393216 | 0 |
| origCalledPartyRedirectReason | 0 | 0 | 130 |
| lastRedirectRedirectReason | 0 | 0 | 146 |
| origCalledPartyRedirectOnBehalfOf | 0 | 0 | 17 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 18 |
| origTerminationOnBehalfOf | 17 | 18 | 12 |
| destTerminationOnBehalfOf | 17 | 18 | 17 |
| joinOnBehalfOf | 0 | 0 | 18 |
| duration | 25 | 4 | 25 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 300 |
| origLegCallIdentifier | 16777300 |
| destLegIdentifier | 16777301 |
| callingPartyNumber | 20000 |
| origCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| lastRedirectDn | 20001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origDTMFMethod | 2 |
| destDTMFMethod | 2 |
| duration | 300 |

| Field Names | CDR |
|---|---|
| globalCallID_callId | 301 |
| origLegCallIdentifier | 16777302 |
| destLegIdentifier | 16777303 |
| callingPartyNumber | 20000 |
| origCalledPartyNumber | 20001 |
| finalCalledPartyNumber | 20001 |
| lastRedirectDn | 20001 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origDTMFMethod | 2:5:2 |
| destDTMFMethod | 2:5:2 |
| duration | 60 |

| Field Names | Call to the Meet-Me Conference CDR |
|---|---|
| globalCallID_callId | 5045247 |
| origLegCallIdentifier | 123456879 |
| destLegIdentifier | 123456999 |
| callingPartyNumber | 35010 |
| originalCalledPartyNumber | 50000 |
| finalCalledPartyNumber | 50000 |
| lastRedirectDn | 50000 |
| origCause_Value | 58 |
| dest_CauseValue | 0 |
| origCalledPartyRedirectReason | 0 |
| lastRedirectRedirectReason | 0 |
| origCalledPartyRedirectOnBehalfOf | 0 |
| lastRedirectRedirectOnBehalfOf | 0 |
| origTerminationOnBehalfOf | 6 |
| destTerminationOnBehalfOf | 6 |

| Calling Party | Calling Partition | Original CalledParty | Original CalledPartition | Orig Cause | Dest Cause | DateTime Connect | Duration |
|---|---|---|---|---|---|---|---|
| 2001 | Accounts | 2309 | Marketing | 0 | 16 | 973795815 | 0 |

| Note | Printable ASCII characters represent characters with ASCII code (in decimal) from 33 to 126. |
|---|---|

| Field Names | Values |
|---|---|
| globalCallID_callId | 1 |
| origLegCallIdentifier | 100 |
| destLegIdentifier | 101 |
| callingPartyNumber | bob@abc.com |
| originalCalledPartyNumber | 2309 |
| finalCalledPartyNumber | 2309 |
| lastRedirectDn | 2309 |
| origCause_Value | 16 |
| dest_CauseValue | 0 |
| duration | 60 |

|  | Calling Party | Calling Partition | Original Called Party | Original Called Partition | Orig Cause | Dest Cause | Duration |
|---|---|---|---|---|---|---|---|
| A | 2001 | Accounts | 2309 | Marketing | 16 | 0 | 60 |
| B | 2001 | Accounts | 2309 | Marketing | 0 | 16 | 60 |

| Field Names | Original Call CDR | Consultation Call CDR | Final Transferred CDR |
|---|---|---|---|
| globalCallID_callId | 1 | 2 | 1 |
| origLegCallIdentifier | 101 | 103 | 102 |
| destLegIdentifier | 102 | 104 | 104 |
| callingPartyNumber | 2001 | 2001 | 3071111 |
| originalCalledPartyNumber | 3071111 | 2002 | 2002 |
| finalCalledPartyNumber | 3071111 | 2002 | 2002 |
| lastRedirectDn | 3071111 | 2002 | 2001 |
| origCause_Value | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 393216 | 0 |
| origTerminationOnBehalfOf | 10 | 10 | 0 |
| destTerminationOnBehalfOf | 10 | 10 | 0 |
| joinOnBehalfOf | 0 | 0 | 10 |
| duration | 120 | 0 | 360 |

| Field Names | Original Call CDR | Consultation Call CDR | Final Transferred Call CDR |
|---|---|---|---|
| globalCallID_callId | 1 | 2 | 1 |
| origLegCallIdentifier | 111 | 113 | 112 |
| destLegIdentifier | 112 | 114 | 114 |
| callingPartyNumber | 2001 | 2001 | 3071111 |
| originalCalledPartyNumber | 3071111 | 2002 | 2002 |
| finalCalledPartyNumber | 3071111 | 2002 | 2002 |
| lastRedirectDn | 50001 | 50001 | 2001 |
| origCause_Value | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 393216 | 0 |
| origTerminationOnBehalfOf | 10 | 10 | 0 |
| destTerminationOnBehalfOf | 10 | 10 | 0 |
| joinOnBehalfOf | 0 | 0 | 10 |
| duration | 60 | 10 | 360 |

| Field Names | Original Call CDR | Consultation Call CDR | Final Transferred Call CDR |
|---|---|---|---|
| globalCallID_callId | 1 | 2 | 1 |
| origLegCallIdentifier | 200 | 202 | 200 |
| destLegIdentifier | 201 | 203 | 203 |
| callingPartyNumber | 50000 | 50001 | 50000 |
| originalCalledPartyNumber | 50001 | 50002 | 50002 |
| finalCalledPartyNumber | 50001 | 50002 | 50002 |
| lastRedirectDn | 50001 | 50001 | 50001 |
| origCause_Value | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 393216 | 0 |
| origTerminationOnBehalfOf | 10 | 10 | 0 |
| destTerminationOnBehalfOf | 10 | 10 | 0 |
| joinOnBehalfOf | 0 | 0 | 10 |
| duration | 120 | 0 | 360 |

| Field Names | Original Call CDR | Consultation Call CDR | Final Transferred Call CDR |
|---|---|---|---|
| globalCallID_callId | 1 | 2 | 1 |
| origLegCallIdentifier | 200 | 202 | 201 |
| destLegIdentifier | 201 | 203 | 203 |
| callingPartyNumber | 50000 | 50001 | 50000 |
| originalCalledPartyNumber | 50001 | 50002 | 50002 |
| finalCalledPartyNumber | 50001 | 50002 | 50002 |
| lastRedirectDn | 50001 | 50001 | 50001 |
| origCause_Value | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 393216 | 0 |
| origTerminationOnBehalfOf | 10 | 10 | 0 |
| destTerminationOnBehalfOf | 10 | 10 | 0 |
| joinOnBehalfOf | 0 | 0 | 10 |
| duration | 120 | 0 | 360 |

| Field Names | Video Call CDR |
|---|---|
| globalCallID_callId | 121 |
| origLegCallIdentifier | 101 |
| destLegIdentifier | 102 |
| callingPartyNumber | 51234 |
| origCalledPartyNumber | 57890 |
| finalCalledPartyNumber | 57890 |
| lastRedirectDn | 57890 |
| origCause_Value | 0 |
| dest_CauseValue | 16 |
| origVideoCap_Codec | 100 |
| origVideoCap_Bandwidth | 320 |
| origVideoCap_Resolution | 2 |
| origVideoTransportAddress_IP | 187962284 |
| origVideoTransportAddress_Port | 49208 |
| destVideoCap_Codec | 100 |
| destVideoCap_Bandwidth | 320 |
| destVideoCap_Resolution | 2 |
| destVideoTransportAddress_IP | 288625580 |
| destVideoTransportAddress_Port | 49254 |

| Note | Each video conference call leg gets shown placing a call into the conference bridge. The call gets shown as a call into the
                                          bridge, regardless of the actual direction of the call. |
|---|---|

| FieldNames | Orig Call CDR | Setup Call CDR | Conference CDR 1 | Conference CDR 2 | Conference CDR 3 | Final CDR |
|---|---|---|---|---|---|---|
| globalCallID_callId | 1 | 2 | 1 | 1 |  | 1 |
| origLegCallIdentifier | 101 | 105 | 101 | 102 | 106 | 101 |
| destLegIdentifier | 102 | 106 | 115 | 116 | 117 | 102 |
| callingPartyNumber | 2001 | 2001 | 2001 | 2309 | 3071111 | 2001 |
| originalCalledPartyNumber | 2309 | 3071111 | b0029901001 | b0029901001 | b0029901001 | 2309 |
| finalCalledPartyNumber | 2309 | 3071111 | b0029901001 | b0029901001 | b0029901001 | 2309 |
| lastRedirectDn | 2001 | 3071111 | b0029901001 | b0029901001 | b0029901001 | b0029901001 |
| origCause_Value | 393216 | 0 | 16 | 393216 | 393216 | 16 |
| dest_CauseValue | 393216 | 0 | 393216 | 393216 | 393216 | 0 |
| origVideoCap_Codec | 103 | 103 | 103 | 103 | 103 | 103 |
| origVideoCap_Bandwidth | 320 | 320 | 320 | 320 | 320 | 320 |
| origVideoCap_Resolution | 0 | 0 | 0 | 0 | 0 | 0 |
| origVideoTransportAddress_IP | 552953152 | 552953152 | 552953152 | -822647488 | -945658560 | 552953152 |
| origVideoTransportAddress_Port | 5445 | 5445 | 5445 | 5445 | 5445 | 5445 |
| destVideoCap_Codec | 103 | 103 | 103 | 103 | 103 | 103 |
| destVideoCap_Bandwidth | 320 | 320 | 320 | 320 | 320 | 320 |
| destVideoCap_Resolution | 0 | 0 | 0 | 0 | 0 | 0 |
| destVideoTransportAddress_IP | -822647488 | -945658560 | -666216182 | -666216182 | -666216182 | -822647488 |
| destVideoTransportAddress_Port | 5445 | 10002 | 10000 | 10004 | 10001 | 5445 |
| origCalledPartyRedirectReason | 0 | 0 | 0 | 0 | 0 | 0 |
| lastRedirectRedirectReason | 0 | 0 | 0 | 0 | 0 | 98 |
| origTerminationOnBehalfOf | 4 | 4 | 12 | 12 | 4 | 12 |
| destTerminationOnBehalfOf | 4 | 4 | 0 | 0 | 4 | 4 |
| origCalledRedirectOnBehalfOf | 0 | 0 | 4 | 4 | 4 | 0 |
| lastRedirectRedirectOnBehalfOf | 0 | 0 | 4 | 4 | 4 | 4 |
| joinOnBehalfOf | 0 | 0 | 4 | 4 | 4 | 4 |
| Conversation ID | 0 | 1 |  | 1 | 1 | 0 |
| duration | 60 | 360 |  | 360 | 360 | 55 |

| Comment |
|---|
| Orig Call CDR |  |
| Setup Call CDR | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Conference CDR 1 | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Conference CDR 2 | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Conference CDR 3 | ConfControllerDn=2001;ConfControlerDeviceName=SEP0003E333FEBD |
| Final CDR |  |