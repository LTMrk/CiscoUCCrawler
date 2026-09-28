---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-cdrdef-cucm-b-cdr-admin-guide-1251-cucm-b-cdr-admin-guid-31c790180a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/cdrdef/cucm_b_cdr-admin-guide-1251/cucm_b_cdr-admin-guide-1251_chapter_0110.html
retrieved_at: 2026-08-21T01:38:27.894991+00:00
---

Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: Cisco Call Detail Records Codes

## Chapter: Cisco Call Detail Records Codes

# Cisco Call Detail Records Codes

This chapter provides information about the codec types and codes that are used
                        		in the Call Detail Record fields.

## Codec Types

The following table contains the compression and payload
                              		  types that may appear in the codec fields.

Value

Description

1

NonStandard

2

G711Alaw 64k

3

G711Alaw 56k

4

G711mu-law 64k

5

G711mu-law 56k

6

G722 64k

7

G722 56k

8

G722 48k

9

G7231

10

G728

11

G729

12

G729AnnexA

13

Is11172AudioCap

14

Is13818AudioCap

15

G.729AnnexB

16

G.729 Annex AwAnnexB

18

GSM Full Rate

19

GSM Half Rate

20

GSM Enhanced Full Rate

25

Wideband 256K

32

Data 64k

33

Data 56k

40

G7221 32K

41

G7221 24K

42

AAC

43

MP4ALATM_128

44

MP4ALATM_64

45

MP4ALATM_56

46

MP4ALATM_48

47

MP4ALATM_32

48

MP4ALATM_24

49

MP4ALATM_NA

80-

GSM

81

ActiveVoice

82

G726 32K

83

G726 24K

84

G726 16K

86

iLBC

89

iSAC

90

OPUS

100

H261

101

H263

102

Vieo

103

H264

104

H264_SVC

105

T120

106

H224

107

T38Fax

108

TOTE

109

H265

110

H264_UC

111

XV150_MR_711U

112

NSE_VBD_711U

113

XV150_MR_729A

114

NSE_VBD_729A

115

H264_FEC

120

Clear_Chan

222

Universal_Xcoder

257

RFC2833_DynPayload

258

PassThrough

259

Dynamic_Payload_PassThru

260

DTMF_OOB

261

Inband_DTMF_RFC2833

299

NoAudio

300

v150_LC_ModemRelay

301

v150_LC_SPRT

302

v150_LC_SSE

## Call Termination
                        	 Cause Codes

The
                              		  following tables contain call termination cause codes that may appear in the
                              		  Cause fields in CDRs.

Cause Code is
                                          			 defined in call control as Natural number. It is a 32 bit unsigned (long)
                                          			 positive integer with values ranging from 0 to +4,294,967,295.

Code

Description

0

No
                                          					 error

1

Unallocated (unassigned) number

2

No
                                          					 route to specified transit network (national use)

3

No
                                          					 route to destination

4

Send special information tone

5

Misdialed trunk prefix (national use)

6

Channel unacceptable

7

Call awarded and being delivered in an established channel

8

Preemption

9

Preemption—circuit reserved for reuse

16

Normal call clearing

17

User busy

18

No
                                          					 user responding

19

No answer from user (If "No Answer Ring duration" value is greater than the
                                          					 T301 Timer value and after T301 Timer expiry, Call Forwarding No Answer(CFNA)
                                          					 Feature would be invoked).

20

Subscriber absent

21

Call rejected

22

Number changed

25

Natural Exchange Routing Error

26

Non-selected user clearing

27

Destination out of order

28

Invalid number format (address incomplete)

29

Facility rejected

30

Response to STATUS ENQUIRY

31

Normal, unspecified

34

No
                                          					 circuit/channel available

38

Network out of order

39

Permanent frame mode connection out of service

40

Permanent frame mode connection operational

41

Temporary failure

42

Switching equipment congestion

43

Access information discarded

44

Requested circuit/channel not available

46

Precedence call blocked

47

Resource unavailable, unspecified

49

Quality of Service not available

50

Requested facility not subscribed

53

Service operation violated

54

Incoming calls barred

55

Incoming calls barred within Closed User Group (CUG)

57

Bearer capability not authorized

58

Bearer capability not presently available

62

Inconsistency in designated outgoing access information and
                                          					 subscriber class

63

Service or option not available, unspecified

65

Bearer capability not implemented

66

Channel type not implemented

69

Requested facility not implemented

70

Only restricted digital information bearer capability is
                                          					 available (national use)

79

Service or option not implemented, unspecified

81

Invalid call reference value

82

Identified channel does not exist

83

A suspended call exists, but this call identity does not

84

Call identity in use

85

No call suspended

86

Call having the requested call identity has been cleared

87

User not member of CUG (Closed User Group)

88

Incompatible destination

90

Destination number missing and DC not subscribed

91

Invalid transit network selection (national use)

95

Invalid message, unspecified

96

Mandatory information element is missing

97

Message type nonexistent or not implemented

98

Message is not compatible with the call state, or the message
                                          					 type is nonexistent or not implemented

99

An information element or parameter does not exist or is not
                                          					 implemented

100

Invalid information element contents

101

The message is not compatible with the call state

102

Call terminated when timer expired; a recovery routine executed
                                          					 to recover from the error

103

Parameter nonexistent or not implemented - passed on (national
                                          					 use)

110

Message with unrecognized parameter discarded

111

Protocol error, unspecified

122

Precedence Level Exceeded

123

Device not Preemptable

125

Out of bandwidth (Cisco specific)

126

Call split (Cisco specific)

127

Interworking, unspecified

129

Precedence out of bandwidth

130

Natural Isolated Code

131

Call Control Discovery PSTN Failover (Cisco specific)

132

IME QOS
                                          					 Fallback (Cisco specific)

133

PSTN
                                          					 Fallback locate Call Error (Cisco specific)

134

PSTN
                                          					 Fallback wait for DTMF Timeout (Cisco specific)

135

IME
                                          					 Failed Connection Timed out (Cisco specific)

136

IME
                                          					 Failed not enrolled (Cisco specific)

137

IME
                                          					 Failed socket error (Cisco specific)

138

IME
                                          					 Failed domain blacklisted (Cisco specific)

139

IME
                                          					 Failed prefix blacklisted (Cisco specific)

140

IME
                                          					 Failed expired ticket (Cisco specific)

141

IME
                                          					 Failed remote no matching route (Cisco specific)

142

IME
                                          					 Failed remote unregistered (Cisco specific)

143

IME
                                          					 Failed remote IME disabled (Cisco specific)

144

IME
                                          					 Failed remote invalid IME trunk URI (Cisco specific)

145

IME
                                          					 Failed remote URI not E164 (Cisco specific)

146

IME
                                          					 Failed remote called number not available (Cisco specific)

147

IME
                                          					 Failed Invalid Ticket (Cisco specific)

148

IME
                                          					 Failed unknown (Cisco specific)

155

DCC Allowed Percentage Exceeded

Decimal Value Code

Hex Value Code

Description

262144

0x40000

Conference Full (was 124)

393216

0x60000

Call split (was 126)This code applies when a call terminates
                                          					 during a transfer operation because it was split off and terminated (was not
                                          					 part of the final transferred call). This code can help you to determine which
                                          					 calls terminated as part of a feature operation.

458752

0x70000

Conference drop any party/Conference drop last party (was 128)

16777257

0x1000029

CCM_SIP_400_BAD_REQUEST

33554453

0x2000015

CCM_SIP_401_UNAUTHORIZED

50331669

0x3000015

CCM_SIP_402_PAYMENT_REQUIRED

67108885

0x4000015

CCM_SIP_403_FORBIDDEN

83886081

0x5000001

CCM_SIP_404_NOT_FOUND

100663359

0x600003F

CCM_SIP_405_METHOD_NOT_ALLOWED

117440591

0x700004F

CCM_SIP_406_NOT_ACCEPTABLE

134217749

0x8000015

CCM_SIP_407_PROXY_AUTHENTICATION_REQUIRED

150995046

0x9000066

CCM_SIP_408_REQUEST_TIMEOUT

184549398

0xB000016

CCM_SIP__410_GONE

201326719

0xC00007F

CCM_SIP_411_LENGTH_REQUIRED

234881151

0xE00007F

CCM_SIP_413_REQUEST_ENTITY_TOO_LONG

251658367

0xF00007F

CCM_SIP_414_REQUEST_URI_TOO_LONG

268435535

0x1000004F

CCM_SIP_415_UNSUPPORTED_MEDIA_TYPE

285212799

0x1100007F

CCM_SIP_416_UNSUPPORTED_URI_SCHEME

83886207

0x1500007F

CCM_SIP_420_BAD_EXTENSION

369098879

0x1600007F

CCM_SIP_421_EXTENSION_REQUIRED

402653311

0x1800007F

CCM_SIP_423_INTERVAL_TOO_BRIEF

419430421

0x19000015

CCM_SIP_424_BAD_LOCATION_INFO

503316501

0x1E000015

CCM_SIP_429_PROVIDE_REFER_IDENTITY

1073741842

0x40000012

CCM_SIP_480_TEMPORARILY_UNAVAILABLE

1090519081

0x41000029

CCM_SIP_481_CALL_LEG_DOES_NOT_EXIST

1107296281

0x42000019

CCM_SIP_482_LOOP_DETECTED = 0x42000000 + EXCHANGE_ROUTING_ERROR

1124073497

0x43000019

CCM_SIP_483_TOO_MANY_HOOPS

1140850716

0x4400001C

CCM_SIP_484_ADDRESS_INCOMPLETE

1157627905

0x45000001

CCM_SIP_485_AMBIGUOUS

1174405137

0x46000011

CCM_SIP_486_BUSY_HERE

1191182367

0x4700001F

CCM_SIP_487_REQUEST_TERMINATED

1207959583

0x4800001F

CCM_SIP_488_NOT_ACCEPTABLE_HERE

1258291217

0x4B000011

CCM_SIP_491_REQUEST_PENDING

1291845649

0x4D000011

CCM_SIP_493_UNDECIPHERABLE

1409286185

0x54000029

CCM_SIP_500_SERVER_INTERNAL_ERROR

1442840614

0x56000026

CCM_SIP_502_BAD_GATEWAY

1459617833

0x57000029

CCM_SIP_503_SERVICE_UNAVAILABLE

2801795135

0xA700003F

CCM_SIP_503_SERVICE_UNAVAILABLE_SER_OPTION_NOAV

1476395110

0x58000066

CCM_SIP__504_SERVER_TIME_OUT

1493172351

0x5900007F

CCM_SIP_505_SIP_VERSION_NOT_SUPPORTED

1509949567

0x5A00007F

CCM_SIP_513_MESSAGE_TOO_LARGE

2701131793

0xA1000011

CCM_SIP_600_BUSY_EVERYWHERE

2717909013

0xA2000015

CCM_SIP_603_DECLINE

2734686209

0xA3000001

CCM_SIP_604_DOES_NOT_EXIST_ANYWHERE

2751463455

0xA400001F

CCM_SIP_606_NOT_ACCEPTABLE

655360

0xA0000

CTI_REQUEST_INVALID_PRIMARY_CALL_STATE

851976

0xD0008

PREEMPTION_NON_IP

917512

0xE0008

PREEMPTION_NETWORK

301989951

0x1200003F

CCM_SIP_417_ERR_RESOURCE_PRIORITY_ROUTINE

570425365

0x22000015

CCM_SIP_433_ANONYMITY_DISALLOWED

## Redirect Reason
                        	 Codes

The
                              		  following table contains the available Redirect Reason Codes that may appear in
                              		  a record.

Q.931 Standard Redirect Reason Codes

Value

Description

0

Unknown

1

Call Forward Busy

2

Call Forward No Answer

4

Call Transfer

5

Call Pickup

7

Call Park

8

Call Park Pickup

9

CPE Out of Order

10

Call Forward

11

Call Park Reversion

15

Call Forward all

Nonstandard Redirect Reason
                                             						  Codes

18

Call Deflection

34

Blind Transfer

50

Call Immediate Divert

66

Call Forward Alternate Party

82

Call Forward On Failure

98

Conference

114

Barge

129

Aar

130

Refer

146

Replaces

162

Redirection (3xx)

177

SIP-forward busy greeting

178

Call
                                          						Forward Unregistered

207

Follow Me (SIP-forward all greeting)

209

Out of Service (SIP-forward busy greeting)

239

Time of Day (SIP-forward all greeting)

242

Do Not Disturb (SIP-forward no answer greeting)

257

Unavailable (SIP-forward busy greeting)

274

Away (SIP-forward no answer greeting)

303

Mobility HandIn

319

Mobility HandOut

335

Mobility Follow Me

351

Mobility Redial

354

Recording

370

Monitoring

399

Mobility IVR

401

Mobility DVOR

402

Mobility EFA

403

Mobility Session Handoff

415

Mobility Cell Pickup

418

Click to Conference

434

Forward No Retrieve

450

Forward No Retrieve Send Back to Parker

464

Call Control Discovery (indicates that the call is redirected to
                                          						a PSTN failover number)

480

Intercompany Media Engine (IME)

496

IME Connection Timed Out

512

IME Not Enrolled

528

IME Socket Error

544

IME Domain Blacklisted

560

IME Prefix Blacklisted

576

IME Expired Ticket

592

IME Remote No Matching Route

608

IME Remote Unregistered

624

IME Remote IME Disabled

640

IME Remote Invalid IME Trunk URI

656

IME Remote URI not E164

672

IME Remote Called Number Not Available

688

IME Invalid Ticket

704

IME Unknown

720

IME PSTN Fallback

738

Presence Enabled Routing

752

Agent Greeting

783

NuRD

786

Native
                                          						Call Queuing, queue a call

802

Native
                                          						Call Queuing, de-queue a call

818

Native
                                          						Call Queuing, redirect to the second destination when no agent is logged in

834

Native
                                          						Call Queuing, redirect to the second destination when the queue is full

850

Native
                                          						Call Queuing, redirect to the second destination when the maximum wait time in
                                          						queue is reached

## OnBehalfof
                        	 Codes

The
                              		  following table contains the available OnBehalfof Codes that may appear in a
                              		  CDR record.

Value

Description

0

Unknown

1

CctiLine

2

Unicast Shared Resource Provider

3

Call Park

4

Conference

5

Call Forward

6

Meet-Me Conference

7

Meet-Me Conference Intercepts

8

Message Waiting

9

Multicast Shared Resource Provider

10

Transfer

11

SSAPI Manager

12

Device

13

Call Control

14

Immediate Divert

15

Barge

16

Pickup

17

Refer

18

Replaces

19

Redirection

20

Callback

21

Path Replacement

22

FacCmc Manager

23

Malicious Call

24

Mobility

25

Aar

26

Directed Call Park

27

Recording

28

Monitoring

29

CCDRequestingService

30

Intercompany Media Engine

31

FallBack Manager

32

Presence Enabled Routing

33

AgentGreeting

34

NativeCallQueuing

35

MobileCallType

| Value | Description |
|---|---|
| 1 | NonStandard |
| 2 | G711Alaw 64k |
| 3 | G711Alaw 56k |
| 4 | G711mu-law 64k |
| 5 | G711mu-law 56k |
| 6 | G722 64k |
| 7 | G722 56k |
| 8 | G722 48k |
| 9 | G7231 |
| 10 | G728 |
| 11 | G729 |
| 12 | G729AnnexA |
| 13 | Is11172AudioCap |
| 14 | Is13818AudioCap |
| 15 | G.729AnnexB |
| 16 | G.729 Annex AwAnnexB |
| 18 | GSM Full Rate |
| 19 | GSM Half Rate |
| 20 | GSM Enhanced Full Rate |
| 25 | Wideband 256K |
| 32 | Data 64k |
| 33 | Data 56k |
| 40 | G7221 32K |
| 41 | G7221 24K |
| 42 | AAC |
| 43 | MP4ALATM_128 |
| 44 | MP4ALATM_64 |
| 45 | MP4ALATM_56 |
| 46 | MP4ALATM_48 |
| 47 | MP4ALATM_32 |
| 48 | MP4ALATM_24 |
| 49 | MP4ALATM_NA |
| 80- | GSM |
| 81 | ActiveVoice |
| 82 | G726 32K |
| 83 | G726 24K |
| 84 | G726 16K |
| 86 | iLBC |
| 89 | iSAC |
| 90 | OPUS |
| 100 | H261 |
| 101 | H263 |
| 102 | Vieo |
| 103 | H264 |
| 104 | H264_SVC |
| 105 | T120 |
| 106 | H224 |
| 107 | T38Fax |
| 108 | TOTE |
| 109 | H265 |
| 110 | H264_UC |
| 111 | XV150_MR_711U |
| 112 | NSE_VBD_711U |
| 113 | XV150_MR_729A |
| 114 | NSE_VBD_729A |
| 115 | H264_FEC |
| 120 | Clear_Chan |
| 222 | Universal_Xcoder |
| 257 | RFC2833_DynPayload |
| 258 | PassThrough |
| 259 | Dynamic_Payload_PassThru |
| 260 | DTMF_OOB |
| 261 | Inband_DTMF_RFC2833 |
| 299 | NoAudio |
| 300 | v150_LC_ModemRelay |
| 301 | v150_LC_SPRT |
| 302 | v150_LC_SSE |

| Note | Cause Code is
                                          			 defined in call control as Natural number. It is a 32 bit unsigned (long)
                                          			 positive integer with values ranging from 0 to +4,294,967,295. |
|---|---|

| Code | Description |
|---|---|
| 0 | No
                                          					 error |
| 1 | Unallocated (unassigned) number |
| 2 | No
                                          					 route to specified transit network (national use) |
| 3 | No
                                          					 route to destination |
| 4 | Send special information tone |
| 5 | Misdialed trunk prefix (national use) |
| 6 | Channel unacceptable |
| 7 | Call awarded and being delivered in an established channel |
| 8 | Preemption |
| 9 | Preemption—circuit reserved for reuse |
| 16 | Normal call clearing |
| 17 | User busy |
| 18 | No
                                          					 user responding |
| 19 | No answer from user (If "No Answer Ring duration" value is greater than the
                                          					 T301 Timer value and after T301 Timer expiry, Call Forwarding No Answer(CFNA)
                                          					 Feature would be invoked). |
| 20 | Subscriber absent |
| 21 | Call rejected |
| 22 | Number changed |
| 25 | Natural Exchange Routing Error |
| 26 | Non-selected user clearing |
| 27 | Destination out of order |
| 28 | Invalid number format (address incomplete) |
| 29 | Facility rejected |
| 30 | Response to STATUS ENQUIRY |
| 31 | Normal, unspecified |
| 34 | No
                                          					 circuit/channel available |
| 38 | Network out of order |
| 39 | Permanent frame mode connection out of service |
| 40 | Permanent frame mode connection operational |
| 41 | Temporary failure |
| 42 | Switching equipment congestion |
| 43 | Access information discarded |
| 44 | Requested circuit/channel not available |
| 46 | Precedence call blocked |
| 47 | Resource unavailable, unspecified |
| 49 | Quality of Service not available |
| 50 | Requested facility not subscribed |
| 53 | Service operation violated |
| 54 | Incoming calls barred |
| 55 | Incoming calls barred within Closed User Group (CUG) |
| 57 | Bearer capability not authorized |
| 58 | Bearer capability not presently available |
| 62 | Inconsistency in designated outgoing access information and
                                          					 subscriber class |
| 63 | Service or option not available, unspecified |
| 65 | Bearer capability not implemented |
| 66 | Channel type not implemented |
| 69 | Requested facility not implemented |
| 70 | Only restricted digital information bearer capability is
                                          					 available (national use) |
| 79 | Service or option not implemented, unspecified |
| 81 | Invalid call reference value |
| 82 | Identified channel does not exist |
| 83 | A suspended call exists, but this call identity does not |
| 84 | Call identity in use |
| 85 | No call suspended |
| 86 | Call having the requested call identity has been cleared |
| 87 | User not member of CUG (Closed User Group) |
| 88 | Incompatible destination |
| 90 | Destination number missing and DC not subscribed |
| 91 | Invalid transit network selection (national use) |
| 95 | Invalid message, unspecified |
| 96 | Mandatory information element is missing |
| 97 | Message type nonexistent or not implemented |
| 98 | Message is not compatible with the call state, or the message
                                          					 type is nonexistent or not implemented |
| 99 | An information element or parameter does not exist or is not
                                          					 implemented |
| 100 | Invalid information element contents |
| 101 | The message is not compatible with the call state |
| 102 | Call terminated when timer expired; a recovery routine executed
                                          					 to recover from the error |
| 103 | Parameter nonexistent or not implemented - passed on (national
                                          					 use) |
| 110 | Message with unrecognized parameter discarded |
| 111 | Protocol error, unspecified |
| 122 | Precedence Level Exceeded |
| 123 | Device not Preemptable |
| 125 | Out of bandwidth (Cisco specific) |
| 126 | Call split (Cisco specific) |
| 127 | Interworking, unspecified |
| 129 | Precedence out of bandwidth |
| 130 | Natural Isolated Code |
| 131 | Call Control Discovery PSTN Failover (Cisco specific) |
| 132 | IME QOS
                                          					 Fallback (Cisco specific) |
| 133 | PSTN
                                          					 Fallback locate Call Error (Cisco specific) |
| 134 | PSTN
                                          					 Fallback wait for DTMF Timeout (Cisco specific) |
| 135 | IME
                                          					 Failed Connection Timed out (Cisco specific) |
| 136 | IME
                                          					 Failed not enrolled (Cisco specific) |
| 137 | IME
                                          					 Failed socket error (Cisco specific) |
| 138 | IME
                                          					 Failed domain blacklisted (Cisco specific) |
| 139 | IME
                                          					 Failed prefix blacklisted (Cisco specific) |
| 140 | IME
                                          					 Failed expired ticket (Cisco specific) |
| 141 | IME
                                          					 Failed remote no matching route (Cisco specific) |
| 142 | IME
                                          					 Failed remote unregistered (Cisco specific) |
| 143 | IME
                                          					 Failed remote IME disabled (Cisco specific) |
| 144 | IME
                                          					 Failed remote invalid IME trunk URI (Cisco specific) |
| 145 | IME
                                          					 Failed remote URI not E164 (Cisco specific) |
| 146 | IME
                                          					 Failed remote called number not available (Cisco specific) |
| 147 | IME
                                          					 Failed Invalid Ticket (Cisco specific) |
| 148 | IME
                                          					 Failed unknown (Cisco specific) |
| 155 | DCC Allowed Percentage Exceeded |

| Decimal Value Code | Hex Value Code | Description |
|---|---|---|
| 262144 | 0x40000 | Conference Full (was 124) |
| 393216 | 0x60000 | Call split (was 126)This code applies when a call terminates
                                          					 during a transfer operation because it was split off and terminated (was not
                                          					 part of the final transferred call). This code can help you to determine which
                                          					 calls terminated as part of a feature operation. |
| 458752 | 0x70000 | Conference drop any party/Conference drop last party (was 128) |
| 16777257 | 0x1000029 | CCM_SIP_400_BAD_REQUEST |
| 33554453 | 0x2000015 | CCM_SIP_401_UNAUTHORIZED |
| 50331669 | 0x3000015 | CCM_SIP_402_PAYMENT_REQUIRED |
| 67108885 | 0x4000015 | CCM_SIP_403_FORBIDDEN |
| 83886081 | 0x5000001 | CCM_SIP_404_NOT_FOUND |
| 100663359 | 0x600003F | CCM_SIP_405_METHOD_NOT_ALLOWED |
| 117440591 | 0x700004F | CCM_SIP_406_NOT_ACCEPTABLE |
| 134217749 | 0x8000015 | CCM_SIP_407_PROXY_AUTHENTICATION_REQUIRED |
| 150995046 | 0x9000066 | CCM_SIP_408_REQUEST_TIMEOUT |
| 184549398 | 0xB000016 | CCM_SIP__410_GONE |
| 201326719 | 0xC00007F | CCM_SIP_411_LENGTH_REQUIRED |
| 234881151 | 0xE00007F | CCM_SIP_413_REQUEST_ENTITY_TOO_LONG |
| 251658367 | 0xF00007F | CCM_SIP_414_REQUEST_URI_TOO_LONG |
| 268435535 | 0x1000004F | CCM_SIP_415_UNSUPPORTED_MEDIA_TYPE |
| 285212799 | 0x1100007F | CCM_SIP_416_UNSUPPORTED_URI_SCHEME |
| 83886207 | 0x1500007F | CCM_SIP_420_BAD_EXTENSION |
| 369098879 | 0x1600007F | CCM_SIP_421_EXTENSION_REQUIRED |
| 402653311 | 0x1800007F | CCM_SIP_423_INTERVAL_TOO_BRIEF |
| 419430421 | 0x19000015 | CCM_SIP_424_BAD_LOCATION_INFO |
| 503316501 | 0x1E000015 | CCM_SIP_429_PROVIDE_REFER_IDENTITY |
| 1073741842 | 0x40000012 | CCM_SIP_480_TEMPORARILY_UNAVAILABLE |
| 1090519081 | 0x41000029 | CCM_SIP_481_CALL_LEG_DOES_NOT_EXIST |
| 1107296281 | 0x42000019 | CCM_SIP_482_LOOP_DETECTED = 0x42000000 + EXCHANGE_ROUTING_ERROR |
| 1124073497 | 0x43000019 | CCM_SIP_483_TOO_MANY_HOOPS |
| 1140850716 | 0x4400001C | CCM_SIP_484_ADDRESS_INCOMPLETE |
| 1157627905 | 0x45000001 | CCM_SIP_485_AMBIGUOUS |
| 1174405137 | 0x46000011 | CCM_SIP_486_BUSY_HERE |
| 1191182367 | 0x4700001F | CCM_SIP_487_REQUEST_TERMINATED |
| 1207959583 | 0x4800001F | CCM_SIP_488_NOT_ACCEPTABLE_HERE |
| 1258291217 | 0x4B000011 | CCM_SIP_491_REQUEST_PENDING |
| 1291845649 | 0x4D000011 | CCM_SIP_493_UNDECIPHERABLE |
| 1409286185 | 0x54000029 | CCM_SIP_500_SERVER_INTERNAL_ERROR |
| 1442840614 | 0x56000026 | CCM_SIP_502_BAD_GATEWAY |
| 1459617833 | 0x57000029 | CCM_SIP_503_SERVICE_UNAVAILABLE |
| 2801795135 | 0xA700003F | CCM_SIP_503_SERVICE_UNAVAILABLE_SER_OPTION_NOAV |
| 1476395110 | 0x58000066 | CCM_SIP__504_SERVER_TIME_OUT |
| 1493172351 | 0x5900007F | CCM_SIP_505_SIP_VERSION_NOT_SUPPORTED |
| 1509949567 | 0x5A00007F | CCM_SIP_513_MESSAGE_TOO_LARGE |
| 2701131793 | 0xA1000011 | CCM_SIP_600_BUSY_EVERYWHERE |
| 2717909013 | 0xA2000015 | CCM_SIP_603_DECLINE |
| 2734686209 | 0xA3000001 | CCM_SIP_604_DOES_NOT_EXIST_ANYWHERE |
| 2751463455 | 0xA400001F | CCM_SIP_606_NOT_ACCEPTABLE |
| 655360 | 0xA0000 | CTI_REQUEST_INVALID_PRIMARY_CALL_STATE |
| 851976 | 0xD0008 | PREEMPTION_NON_IP |
| 917512 | 0xE0008 | PREEMPTION_NETWORK |
| 301989951 | 0x1200003F | CCM_SIP_417_ERR_RESOURCE_PRIORITY_ROUTINE |
| 570425365 | 0x22000015 | CCM_SIP_433_ANONYMITY_DISALLOWED |

| Q.931 Standard Redirect Reason Codes |
|---|
| Value | Description |
| 0 | Unknown |
| 1 | Call Forward Busy |
| 2 | Call Forward No Answer |
| 4 | Call Transfer |
| 5 | Call Pickup |
| 7 | Call Park |
| 8 | Call Park Pickup |
| 9 | CPE Out of Order |
| 10 | Call Forward |
| 11 | Call Park Reversion |
| 15 | Call Forward all |
| Nonstandard Redirect Reason
                                             						  Codes |
| 18 | Call Deflection |
| 34 | Blind Transfer |
| 50 | Call Immediate Divert |
| 66 | Call Forward Alternate Party |
| 82 | Call Forward On Failure |
| 98 | Conference |
| 114 | Barge |
| 129 | Aar |
| 130 | Refer |
| 146 | Replaces |
| 162 | Redirection (3xx) |
| 177 | SIP-forward busy greeting |
| 178 | Call
                                          						Forward Unregistered |
| 207 | Follow Me (SIP-forward all greeting) |
| 209 | Out of Service (SIP-forward busy greeting) |
| 239 | Time of Day (SIP-forward all greeting) |
| 242 | Do Not Disturb (SIP-forward no answer greeting) |
| 257 | Unavailable (SIP-forward busy greeting) |
| 274 | Away (SIP-forward no answer greeting) |
| 303 | Mobility HandIn |
| 319 | Mobility HandOut |
| 335 | Mobility Follow Me |
| 351 | Mobility Redial |
| 354 | Recording |
| 370 | Monitoring |
| 399 | Mobility IVR |
| 401 | Mobility DVOR |
| 402 | Mobility EFA |
| 403 | Mobility Session Handoff |
| 415 | Mobility Cell Pickup |
| 418 | Click to Conference |
| 434 | Forward No Retrieve |
| 450 | Forward No Retrieve Send Back to Parker |
| 464 | Call Control Discovery (indicates that the call is redirected to
                                          						a PSTN failover number) |
| 480 | Intercompany Media Engine (IME) |
| 496 | IME Connection Timed Out |
| 512 | IME Not Enrolled |
| 528 | IME Socket Error |
| 544 | IME Domain Blacklisted |
| 560 | IME Prefix Blacklisted |
| 576 | IME Expired Ticket |
| 592 | IME Remote No Matching Route |
| 608 | IME Remote Unregistered |
| 624 | IME Remote IME Disabled |
| 640 | IME Remote Invalid IME Trunk URI |
| 656 | IME Remote URI not E164 |
| 672 | IME Remote Called Number Not Available |
| 688 | IME Invalid Ticket |
| 704 | IME Unknown |
| 720 | IME PSTN Fallback |
| 738 | Presence Enabled Routing |
| 752 | Agent Greeting |
| 783 | NuRD |
| 786 | Native
                                          						Call Queuing, queue a call |
| 802 | Native
                                          						Call Queuing, de-queue a call |
| 818 | Native
                                          						Call Queuing, redirect to the second destination when no agent is logged in |
| 834 | Native
                                          						Call Queuing, redirect to the second destination when the queue is full |
| 850 | Native
                                          						Call Queuing, redirect to the second destination when the maximum wait time in
                                          						queue is reached |

| Value | Description |
|---|---|
| 0 | Unknown |
| 1 | CctiLine |
| 2 | Unicast Shared Resource Provider |
| 3 | Call Park |
| 4 | Conference |
| 5 | Call Forward |
| 6 | Meet-Me Conference |
| 7 | Meet-Me Conference Intercepts |
| 8 | Message Waiting |
| 9 | Multicast Shared Resource Provider |
| 10 | Transfer |
| 11 | SSAPI Manager |
| 12 | Device |
| 13 | Call Control |
| 14 | Immediate Divert |
| 15 | Barge |
| 16 | Pickup |
| 17 | Refer |
| 18 | Replaces |
| 19 | Redirection |
| 20 | Callback |
| 21 | Path Replacement |
| 22 | FacCmc Manager |
| 23 | Malicious Call |
| 24 | Mobility |
| 25 | Aar |
| 26 | Directed Call Park |
| 27 | Recording |
| 28 | Monitoring |
| 29 | CCDRequestingService |
| 30 | Intercompany Media Engine |
| 31 | FallBack Manager |
| 32 | Presence Enabled Routing |
| 33 | AgentGreeting |
| 34 | NativeCallQueuing |
| 35 | MobileCallType |