---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-060dbe41a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_1501-configuration-guide-for-cisco-customer-voice-portal-release/media_server_configuration.html
retrieved_at: 2026-08-21T12:06:50.866930+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: December 12, 2025

Chapter: Media Server Configuration

## Chapter: Media Server Configuration

# Media Server Configuration

## Configure Media
                        	 Server

Step 1

From the
                                       			 Unified CVP Operations Console, select Device
                                             				  Management > Media Server .

Step 2

Click Add
                                          				New to add a new Media Server or click Use As
                                          				Template to use an existing template to configure the new Media
                                       			 Server.

Step 3

Click the
                                       			 following tabs and configure the settings based on your call flow:

General tab.
                                             				  For more information, see General Settings .

Device Pool tab. For more information about adding, deleting and editing device pool, see Add or Remove Device From Device Pool .

Step 4

Click Save .

### What to do next

All the configured Media Servers appear in the Default Media Server drop-down box. To set the
                              		  default Media Server, select one of the listed Media Servers from the Default Media Server drop-down box, and click Set .

## Media Server Settings

### General
                           	 Settings

Field

Description

Default

Value

Restart
                                             					 Required

IP Address

The IP
                                             					 address of Media Server

None

Valid IP
                                             					 address.

No

Hostname

The name
                                             					 of the Media Server

None

Follow
                                             					 naming conventions for hostnames.

No

Description

The
                                             					 description of the Media Server

None

Up to
                                             					 1,024 characters.

No

FTP
                                             					 Enabled

Indicates whether a Media Server has FTP enabled. A Media Server, which has FTP enabled, is automatically populated as a session
                                             variable to the VXML Server. The default agent greeting recording application automatically uses the Media Servers defined
                                             in the Operations Console that have FTP enabled for the agent greeting recording.

If Microsoft FTP Service is not enabled in Windows Services
                                             					 Control Panel, then set it to Automatic and start the service.

SFTP is also supported with Media Servers.

Disabled

Select the
                                             					 check box to enable this feature.

No

Use Test Sign-in button to verify the FTP credentials.

Anonymous
                                             					 Access

Indicates
                                             					 that this Media Server uses anonymous FTP access. In this case, the username is
                                             					 specified by default as anonymous. The password field is not specified for
                                             					 anonymous access.

The user
                                             					 can specify the port number or select the default port number (21).

Disabled

Select the
                                             					 check box to enable this feature.

You
                                             					 must enable FTP to enable Anonymous Access.

No

Use Test
                                             					 Sign-in button to verify the FTP credentials.

Username
                                             					 and Password

These
                                             					 fields apply if FTP is enabled and Anonymous Access is disabled. In this case, enter
                                             					 the username and password.

None

A valid
                                             					 username and password.

No

Use Test
                                             					 Sign-in button to verify the FTP credentials.

Port

Enter a
                                             					 new port number or use the default port number (21).

For SFTP, use port 22 or any other custom port that you may have configured.

21

Valid
                                             					 ports are 1 to 65,535.

No

Use Test
                                             					 Sign-in button to verify the FTP credentials.

## Media Server
                        	 Association with Call Server and VXML Server

If your
                           		Unified CVP Call Server, Media Server, and UnifiedCVP VXMLServer reside on
                           		the same hardware server and you have multiple co-resident servers, UnifiedCVP
                           		does not automatically use the same physical server for call control, VXML, and
                           		media file services. If the components are co-resident, no component is forced
                           		to use the other co-resident components, and Unified CVP might possibly use the
                           		components located on another server.

By default,
                           		the components are load balanced across all of the physical servers and do not
                           		attempt to use the same server for all of the services. During thousands of
                           		calls, all of the components on all of the servers are load balanced and
                           		equally utilized, but one specific call could be using several different
                           		physical servers. For example, for one particular call you can be using SIP
                           		call control on one server, VoiceXML on another server, and the media files on
                           		another server.

You can
                           		simplify management and troubleshooting by configuring Unified CVP to use the
                           		same physical server for all of these functions on a per-call basis. If there
                           		is only one server in the system, then simplification is not a concern. The
                           		instructions in the following procedures show you how to configure UnifiedCVP
                           		so that it uses components on the same physical server instead of load
                           		balancing and using a random server for each component.

### Choose Coresident
                           	 Unified CVP VXML Server in ICM Script Editor

Step 1

Set up the media_server ECC variable that specifies your UnifiedCVP
                                          			 VXMLServer in the ICM script by using use the Formula Editor to set the media_server ECC variable to concatenate("http://",Call.RoutingClient,":7000/CVP") .

Call.RoutingClient is the built-in call variable that ICM
                                             				sets automatically for you. The routing client name in ICM is usually not the
                                             				same as the UnifiedCVP Server's hostname.

Step 2

Apply the routing client name as a hostname in the VXML server . Do not use noncompliant characters such as an underscore as part of the hostname because the router cannot translate the
                                          hostname to an IP address if it contains noncomplaint characters.

Step 3

Configure the
                                          			 routing client hostname for every UnifiedCVP Server Routing Client.

### Choose Coresident
                           	 Media Server in Call Studio

Step 1

In the ICM
                                          			 script, set one of the ToExtVXML[] array variables with the call.routingclient
                                          			 data, such as ServerName=call.routingclient. This variable is passed to the
                                          			 UnifiedCVP VXMLServer, and the variable is stored in the session data with
                                          			 the variable name ServerName.

Step 2

In Cisco
                                          			 Unified Call Studio, use a substitution to populate the Default Audio Path. Add
                                          			 the Application_Modifier element found in the Context folder, and specify the
                                          			 Default Audio Path in the Settings tab in the following format: http:// {Data.Session.ServerName}

### Choose Coresident
                           	 VXML Server Using Micro-Apps

If you are using Micro-Apps in conjunction with the Unified CVP VXMLServer, pay careful attention to the media_server ECC variable in the ICM script because the same variable is used to specify both the Unified CVP VXML Server and the media
                                 server, but the contents of the variable use a different format depending on which server you want to specify. Use the media_server ECC variable as indicated in this procedure whenever you want to use a Micro-App for prompting. If you subsequently want
                                 to use the Unified CVP VXML Server, rewrite this variable by following the previous procedure.

Step 1

Set up the media_server ECC variable that specifies your Media server
                                          			 in the ICM script by using the Formula Editor to set the media_server ECC variable to concatenate("http://",Call.RoutingClient)

Call.RoutingClient is the built-in call variable that ICM sets automatically for you. The routing client name in ICM usually is not the same
                                             as the Unified CVP Server hostname.

Step 2

Use the name of the routing client as a hostname in the VXML server .

Do not use noncompliant characters such as an underscore as part of the hostname because the router cannot translate the
                                             hostname to an IP address if it contains any noncomplaint characters.

Step 3

Configure the routing client hostname for every Unified CVP Server Routing Client.

## Microsoft Windows IIS Cache Expiration

To allow new media files to replace their predecessor in a reasonable amount of time while minimizing requests for data to
                                       the media server from the Virtualized Voice Browser, configure a cache expiration value in IIS Manager. The ideal value will
                                       require testing as it depends on how frequently media files are changed.

To configure a cache expiration value in IIS Manager:

Find the site you are using, go to the folder where the media files are being stored, and then click HTTP Response Headers .

Click Set Common Headers on the Actions panel.

Select Expire Web Content and set the desired value.

## Media File Names and Types

A media file name is specified
                           through Unified ICME Network VRU Script Configuration and used in the Run VRU
                           Script request for the Play Media, Play Data, Get Digits, Menu, and Get Speech
                           (in non-TTS applications) micro-applications. The media file naming convention
                           allows alpha-numeric characters with the underbar character as a separator.
                           (Spaces or hyphens are not allowed.) This naming convention provides a
                           mechanism for an "understandable" naming convention as opposed to numeric media
                           file names typically used by stand-alone VRUs.

Caution

The media file types Unified CVP supports are µ-Law 8-bit .wav files and A-law 8-bit .wav
                           files. Media files specified with an extension are used "as is," for
                           example, hello.xxx. (The default file extension is .wav.)

Caution

## Location of Media
                        	 Files

The following
                           		figure displays the location of the media files if you choose to install System
                           		Media Files during Unified CVP installation.

## Media File
                        	 Address

The address for media files that reside on the Media Server(s) is generated by the Unified CVP. Unified ICME provides information about the file location or base URL address in the Unified ICME /IVR messages it passes when the Run VRU Script node is run. The Unified ICME /IVR messages include ECC variables for: locale, media server set address, as well as optional system and application library
                           name overrides. (For details about the Unified ICME /IVR messages passed to Unified CVP, see Feature Guide - Writing
                                    				  Scripts for Unified Customer Voice Portal .

The table below
                           		summarizes the data that combines to form the address of the media file:

Parameter

Location of Data

Description

Examples

Media Server Set

ECC variable: user.microapp.media

_server

File location or base URL for the Media Server.

When the Media Server URL is the DNS name and the DNS Server is configured to return multiple IP addresses for a host name,
                                       the Unified CVP attempts to get the media files from each Media Server IP address in sequence with the priority given to those
                                       on the subnet.

When using the Media Server set for external grammars or external VXML, if the Media Server URL is the DNS name with multiple
                                       IP addresses for the hostname, it is the ASR Engine’s responsibility to decide which machine to retrieve the grammar file
                                       from.

Tomcat version (9.0.8) packaged with CVP does not support underscore "_" in the hostname. Therefore, it is recommended to
                                                   set user.microapp.media_server to a hostname that does not use "_".

Base URL example: http://www.machine1.com

/dir1/ dirs/cust1

Locale

ECC variable: user.microapp.locale

Default: en-us

This field is a combination of language and country with a default of en-us for English spoken in the United States.

en-us

Media Library Type

The Media Library Type value passed from the VRU Script Name field. Valid options are:

A - Application prompt library.

S - System prompt library.

V - External VXML.

Default: A

The media library (directory) for the prompt is either the application prompt library defined by ECC variable user.microapp.app_media_lib
                                       (default "app" ) or the system prompt library defined by ECC variable user.microapp.sys_media_lib (default "sys" ).

A (user.microapp.app_media_ lib= app_banking)

Media File Name

The Media File Name value passed from the VRU Script Name field. Valid options are the name of the .wav file to be played,
                                       or external VXML file name, or <blank>, which translates to playing no media. This file name is ignored if TTS is being used
                                       (that is, if the user.microapp.inline_tts ECC variable contains a value.)

Default: none

Name of media file or external VXML file to be played.

Main_menu

Media File Name Type

If not given as part of the Media File Name, the type is .wav

Type of media file to be played.

.wav

Based on the examples shown in the table above, a valid address for the Media File might be:

http://www.machine1.com/dir1/dirs/cust1/en-us/app_banking/main_menu.wav

## Locale Backward Compatibility

The locale string values are
                           compatible with current industry naming schemes:

en_US has changed to en-us , which means that
                                 " en underscore US " (upper case) has changed
                                 to " en hyphen u s" (lower case).

en_GB has changed to en-gb , which means that " en underscore GB " (upper case) has
                                 changed to " en hyphen gb " (lower
                                 case).

Existing scripts from previous
                           versions of Unified CVP will continue to work with the current version of
                           Unified CVP:

en_US and en-us both map to U.S. English in the Application Server for
                                 use by the Application Server’s internal grammar

en_GB and en-gb both map to U.K.
                                 English in the Application Server for use by the Application Server’s internal
                                 grammar.

The base URL for media prompts uses the
                                 locale that is specified, without making modifications. For example, if the
                                 locale is set to EN_US , the base URL contains EN_US . If the locale is set to XX , the base
                                 URL contains XX .

To use the Unified
                           CVP Version 1.1 default locale directory (for example, en_US ),
                           you must explicitly set it. When you upgrade to the current version of Unified
                           CVP, only the new files are installed under the Unified CVP default locale
                           directory, en-us . You want to have all your system prompts
                           under one directory and all your application prompts and, optionally, external
                           VXML in another directory. Use the user.microapp.locale ECC
                           variable to set the locale directory to use, such as en_US .

## System Media
                        	 Files

The following tables
                           		describe the English System Media Files installed by Unified CVP. These system
                           		media files are intended as samples only. It is the Customer/Media
                           		Administrator’s responsibility to record all the system prompts for all the
                           		locales.

The table that
                           		follows lists the System Media File information for cardinal numbers.

Symbol (where
                                       				applicable)

Decimal Value

Media File Name

Media File
                                       				Content

Data Play Back
                                       				Types / When Media File Is Used

point

point

Number

minus

minus

Number

0

48

0

zero

All except DOW

1

49

1

one (masculine
                                       				version), uno (es-mx and es-es)

All except DOW

2

50

2

two

All except DOW

3

51

3

three

All except DOW

4

52

4

four

All except DOW

5

53

5

five

All except DOW

6

54

6

six

All except DOW

7

55

7

seven

All except DOW

8

56

8

eight

All except DOW

9

57

9

nine

All except DOW

10

ten

Same for the
                                       				rest of all the numbers

11

eleven

12

twelve

13

thirteen

14

fourteen

15

fifteen

16

sixteen

17

seventeen

18

eighteen

19

nineteen

20

twenty

21

twenty-one

22

twenty-two

23

twenty-three

24

twenty-four

25

twenty-five

26

twenty-six

27

twenty-seven

28

twenty-eight

29

twenty-nine

30

thirty

31

thirty-one

32

thirty-two

33

thirty-three

34

thirty-four

35

thirty-five

36

thirty-six

37

thirty-seven

38

thirty-eight

39

thirty-nine

40

forty

41

forty-one

42

forty-two

43

forty-three

44

forty-four

45

forty-five

46

forty-six

47

forty-seven

48

forty-eight

49

forty-nine

50

fifty

51

fifty-one

52

fifty-two

53

fifty-three

54

fifty-four

55

fifty-five

56

fifty-six

57

fifty-seven

58

fifty-eight

59

fifty-nine

60

sixty

61

sixty-one

62

sixty-two

63

sixty-three

64

sixty-four

65

sixty-five

66

sixty-six

67

sixty-seven

68

sixty-eight

69

sixty-nine

70

seventy

71

seventy-one

72

seventy-two

73

seventy-three

74

seventy-four

75

seventy-five

76

seventy-six

77

seventy-seven

78

seventy-eight

79

seventy-nine

80

eighty

81

eighty-one

82

eighty-two

83

eighty-three

84

eighty-four

85

eighty-five

86

eighty-six

87

eighty-seven

88

eighty-eight

89

eighty-nine

90

ninety

91

ninety-one

92

ninety-two

93

ninety-three

94

ninety-four

95

ninety-five

96

ninety-six

97

ninety-seven

98

ninety-eight

99

ninety-nine

oh

oh

24TOD, Date

hundred

hundred

Number, 24TOD,
                                       				Date, Currency

thousand

thousand

Number, Date,
                                       				Currency

million

million

Number,
                                       				Currency

billion

billion

Number, Date,
                                       				Currency

trillion

trillion

Number,
                                       				Currency

The table that
                           	 follows lists the System Media File information for ordinal numbers.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

1ord

first

Date

2ord

second

Date for all
                                       				ordinal numbers

3ord

third

4ord

fourth

5ord

fifth

6ord

sixth

7ord

seventh

8ord

eighth

9ord

nineth

10ord

tenth

11ord

eleventh

12ord

twelveth

13ord

thirteenth

14ord

fourteenth

15ord

fifteenth

16ord

sixteenth

17ord

seventeenth

18ord

eighteenth

19ord

nineteenth

20ord

twentieth

21ord

twenty-first

22ord

twenty-second

23ord

twenty-third

24ord

twenty-fourth

25ord

twenty-fifth

26ord

twenty-sixth

27ord

twenty-seventh

28ord

twenty-eight

29ord

twenty-nineth

30ord

thirtieth

31ord

thirty-first

The table that
                           	 follows lists the System Media File information for measurements.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

½

189

one_half

one half

Char

¼

188

one_quarter

one quarter

Char

¾

190

three_quarters

three quarters

Char

A, a

65,97

a

A

Char

B,b

66,98

b

B

Char

C, c

67,99

c

C

Char

D, d

68,100

d

D

Char

E, e

69,101

e

E

Char

F, f

70,102

f

F

Char

G, g

71,103

g

G

Char

H, h

72,104

h

H

Char

I, I

73,105

I

I

Char

J, j

74,106

j

J

Char

K, k

75,107

k

K

Char

L, l

76,108

l

L

Char

M, m

77,109

m

M

Char

N, n

78,110

n

N

Char

O, o

79,111

o

O

Char

P, p

80,112

p

P

Char

Q, q

81,113

q

Q

Char

R, r

82,114

r

R

Char

S, s

83,115

s

S

Char

T, t

84,116

t

T

Char

U, u

85,117

u

U

Char

V, v

86,118

v

V

Char

W, w

87,119

w

W

Char

X, x

88,120

x

X

Char

Y, y

89,121

y

Y

Char

Z, z

90,122

z

Z

Char

Œ, œ

140,156

oe_140_156

Ligature OE

Char

À,à

192,224

a_192_224

A grave

Char

Á,á

193,225

a_193_225

A acute

Char

Â,â

194,226

a_194_226

A circumflex

Char

Ã,ã

195,227

a_195_227

A tilde

Char

Ä,ä

196,228

a_196_228

A umlaut

Char

Å,å

197,229

a_197_229

A with ring
                                       				above

Char

Æ,æ

198,230

ae_198_230

Ligature AE

Char

È,è

200,232

e_200_232

E grave

Char

É,é

201,233

e_201_233

E acute

Char

Ê,ê

202,234

e_202_234

E circumflex

Char

Ë,ë

203,235

e_203_235

E umlaut

Ì,ì

204,236

i_204_236

I grave

Char

Í, í

205,237

i_205

I acute

Char

Î,î

206,238

i_206

I circumflex

Char

Ï,ï

207,239

i_207

I umlaut

Char

Ð

208

char_208

character 208

Char

ð

240

char_240

character 240

Ò,ò

210,242

o_210_242

O grave

Char

Ó,ó

211,243

o_211_243

O acute

Char

Ô,ô

212,244

o_212_244

O circumflex

Char

Õ,õ

213,245

o_213_245

O tilde

Char

Ö,ö

214,246

o_214_246

O umlaut

Char

x

215

multiply

multiplication
                                       				sign

Char

Ø,ø

216,248

o_216_248

oh stroke

Char

Ù,ù

217,249

u_217_249

U grave

Char

Ú,ú

218,250

u_218_250

U acute

Char

Û,û

219,251

u_219_251

U circumflex

Char

Ü,ü

220,252

u_220_252

U umlaut

Char

Ý,ý

221,253

y_221_253

Y acute

Char

Þ

222

char_222

character 222

Char

ß

223

ss

double s

Char

÷

247

divide

division sign

Char

þ

254

char_254

character 254

Char

Ÿ,ÿ

159,255

y_159_255

character 159
                                       				or 255

Char

The table that
                           	 follows lists the System Media File information for month values.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

January

January

Date

February

February

Date

March

March

Date

April

April

Date

May

May

Date

June

June

Date

July

July

Date

August

August

Date

September

September

Date

October

October

Date

November

November

Date

December

December

Date

The table that
                           	 follows lists the System Media File information for month values.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

Sunday

Sunday

DOW

Monday

Monday

DOW

Tuesday

Tuesday

DOW

Wednesday

Wednesday

DOW

Thursday

Thursday

DOW

Friday

Friday

DOW

Saturday

Saturday

DOW

The table that
                           	 follows lists the System Media File information for month values.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

hour

hour

Etime, 24TOD
                                       				per locale, TOD per locale

hours

hours

Etime,24TOD
                                       				per locale,TOD per locale

minute

minute

Etime

minutes

minutes

Etime

second

second

Etime,24TOD

seconds

seconds

Etime,24TOD

on

on

per
                                       				locale(unused for en-us)

at

at

per
                                       				locale(unused for en-us)

am

am

TOD

pm

pm

TOD

oclock

oclock

TOD

The table that
                           	 follows lists the System Media File information for currency values.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

currency_
                                       				minus

minus

Currency

currency_and

and

Currency

$

36

USD_dollar

dollar

Currency

USD_dollars

dollars

Currency

$

36

CAD_dollar

dollar

Currency

CAD_dollars

dollars

Currency

HKD_dollar

dollar

Currency

HKD_dollars

dollars

Currency

¢

162

cent

cent

Currency

cents

cents

Currency

euro

euro

Currency

£

163

GBP_pound

pound

Currency

GBP_pounds

pounds

Currency

penny

penny

Currency

pence

pence

Currency

MXN_peso

peso

Currency

MXN_pesos

pesos

Currency

centavo

centavo

Currency

centavos

centavos

Currency

The table that
                           	 follows lists the System Media File information for gaps of silence and
                           	 miscellaneous phrases.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

silence_.1_
                                       				sec

(.1 second of
                                       				silence)

Used for
                                       				pauses where needed

silence_.25_
                                       				sec

(.25 second
                                       				of silence)

Used for
                                       				pauses where needed

silence_.5_
                                       				sec

(.5 second of
                                       				silence)

Used for
                                       				pauses where needed

silence_1_sec

(1 second of
                                       				silence)

Used for
                                       				pauses where needed

and

and

Etime,TOD,25TOD

The table that
                           	 follows lists the System Media File information for ANSI characters.

Symbol (where
                                       				applicable)

Decimal Value

Media File
                                       				Name

Media File
                                       				Content

Data Play
                                       				Back Types / When Media File Is Used

32

space

space

Char

!

33

exclamation_
                                       				mark

exclamation
                                       				mark

Char

"

34

double_ quote

double quote

Char

#

35

pound

pound

Char

%

37

percent

percent

Char

&

38

ampersand

ampersand

Char

'

39

apostrophe

apostrophe

Char

(

40

open_
                                       				parenthesis

open
                                       				parenthesis

Char

)

41

close_
                                       				parenthesis

close
                                       				parenthesis

Char

*

42

asterisk

asterisk

Char

+

43

plus

plus

Char

,

44

comma

comma

Char

-

45

hyphen

hyphen

Char

.

46

period

period

Char

/

47

slash

slash

Char

:

58

colon

colon

Char

;

59

semicolon

semicolon

Char

<

60

less_than

less than

Char

=

61

equal

equal

Char

62

greater_than

greater than

Char

?

63

question_ mark

question mark

Char

@

64

at_symbol

at

Char

[

91

left_square_bracket

left square
                                       				bracket

Char

\

92

backslash

backslash

Char

]

93

right_square_bracket

right square
                                       				bracket

Char

^

94

caret

caret

Char

_

95

underscore

underscore

Char

`

96

single_quote

single quote

Char

{

123

open_brace

open brace

Char

|

124

pipe

pipe

Char

}

125

close_brace

close brace

Char

~

126

tilde

tilde

Char

’

130

char_130

low single
                                       				quote

Char

ƒ

131

char_131

F with hook

Char

”

132

low double
                                       				quote

low double
                                       				quote

Char

…

133

ellipsis

ellipsis

Char

†

134

char_134

character 134

Char

‡

135

char_135

character 135

Char

ˆ

136

char_136

character 136

Char

‰

137

per_mille

per mile

Char

Š

138

char_138

character 138

<

139

left_pointing
                                       				_angle

left pointing
                                       				angle

Char

‘

145

left_single_
                                       				quote

left single
                                       				quote

Char

’

146

right_single_
                                       				quote

right single
                                       				quote

Char

“

147

left_double_
                                       				quote

left double
                                       				quote

Char

”

148

right_double
                                       				_quote

right double
                                       				quote

Char

·

149

bullet

bullet

Char

–

150

en_dash

en dash

Char

—

151

em_dash

em dash

˜

152

small_tilde

small tilde

Char

™

153

trade_mark

trade mark

Char

š

154

char_154

character 154

Char

›

155

char_155

character 155

Char

¡

161

exclamation_
                                       				mark_ inverted

inverted
                                       				exclamation mark

Char

¤

164

char_164

character 164

Char

¦

166

broken_pipe

broken pipe

Char

§

167

section

section

Char

¨

168

char_168

character 168

Char

©

169

copyright

copyright

Char

ª

170

char_170

character 170

Char

«

171

left_double_
                                       				angle_ quote

left double
                                       				angle quote

Char

¬

172

not

not

Char

-

173

char_173

character 173

Char

®

174

registered

registered

Char

¯

175

char_175

character 175

Char

°

176

degree

degree

Char

±

177

plus_minus

plus or minus

Char

²

178

superscript_ 2

superscript
                                       				two

Char

³

179

superscript_ 3

superscript
                                       				three

Char

´

180

acute_accent

acute accent

Char

µ

181

micro

micro

Char

¶

182

paragraph

paragraph

Char

·

183

middle_dot

middle dot

Char

¸

184

cedilla

cedilla

Char

¹

185

superscript_ 1

superscript
                                       				one

Char

º

186

char_186

character 186

Char

»

187

right_double
                                       				_angle_ quote

right double
                                       				angle quote

Char

¿

191

question_
                                       				mark_ inverted

inverted
                                       				question mark

Char

### Miscellaneous Files

The table that follows lists files that are not used by Unified CVP
                              micro-applications; these files are included for use in customer scripts.

Symbol (where applicable)

Decimal Value

Media File Name

Media File Content

Data Play Back Types / When Media
                                          File Is Used

Error

v

invalid_entry_error

Your entry is invalid.

Error message

v

no_entry_error

Please make a selection.

Error message

v

system_error

We are currently experiencing technical difficulties with this site.
                                          Please try again later when we can service you much better.

Error message

v

critical_error

We are currently experiencing technical difficulties with
                                          this site. Please try again later when we can service you much better.

Error message

v

critical_error_ULaw .

We are currently experiencing
                                          technical difficulties with this site. Please try again later when we can
                                          service you much better

Error
                                          message

v

critical_error_ALaw

We are
                                          currently experiencing technical difficulties with this site. Please try again
                                          later when we can service you much better.

Error message

v

440beep

<single beep tone>

Unused

v

busy_tone

<single busy
                                          tone>

Unused

v

busy_tone30

<busy tone 1
                                          per second for 30 seconds>

Unused

v

central

Central

Unused

v

credit_of

Credit Of

Unused

v

dash

dash

Unused

v

daylight

daylight

Unused

v

dialtone

<4 seconds of
                                          dial tone>

Unused

v

dialtone2fastbusy60

<9
                                          seconds of dialtone> followed by <30 seconds of fast busy tone>

Unused

v

dot

dot

Unused

v

eastern

Eastern

Unused

v

ENTER_PHONE_NUMBER

Please
                                          enter the phone number.

Unused

v

fastbusy

<a single fastbusy
                                          tone + silence (total of 1 second)>

Unused

v

fastbusy60

30 seconds of
                                          <fastbusy tone>

Unused

v

FINISHED

When you have
                                          finished, press

Unused

v

goodbye

Goodbye

Unused

v

Mountain

Mountain

Unused

v

negative

negative

Unused

v

of

of

Unused

v

pmgr_sys

pmgr_sys

Unused

v

pacific

Pacific

Unused

v

positive

positive

Unused

v

ringback

<ring back tone
                                          for 1 second followed by 2 seconds of silence>

Unused

v

savings

savings

Unused

v

standard

Standard

Unused

v

Star

star

Unused

v

thankyou

Thank you

Unused

v

the

the

Unused

v

time

time

Unused

v

try_again

Please try again

Unused

### System Media File
                           	 Error Messages

Three error
                              		messages are included with the System Media files:

Critical error. Message played when system problem exists and the SIP Service
                                    			 cannot process the call. (Example content for en-us: "We are
                                       				currently experiencing technical difficulties with the site, please try again
                                       				later and we can serve you much better." )

Critical error
                                    			 messages are not located on the Media Server:

For SIP
                                             					 Service , the critical_error.wav media file is located in <install path> \OpsConsoleServer\GWDownloads (for example,
                                          				  C:\Cisco\CVP\OpsConsoleServer\GWDownloads).

For non-Unified CVP SIP Service , an error.wav media file is
                                          				  located in <install path> \CVP\audio (for example,
                                          				  C:\Cisco\VXMLServer\Tomcat\webapps\CVP\audio).

no_entry_error . Message
                                    			 played when the caller does not respond to a menu prompt. (Example content for
                                    			 en-us: "Please make a
                                       				selection." ) The original prompt is then repeated.

invalid_entry_error .
                                    			 Message played when the caller enters an incorrect response to a menu prompt.
                                    			 (Example content for en-us: "Your entry is
                                       				invalid." ) The original prompt is then repeated.

If a dialogue needs to be altered for a specific Get Digits, Get Speech or Menu request in the Unified ICME script, override
                              flags can be set in the Network VRU Script Configuration Parameters.

You must record the "override" prompts, save them with the hard coded names <prompt
                              		name>_no_entry_error.wav and <prompt_name>_invalid_entry_error.wav,
                              		and place them with other application-specific media files in the Application
                              		Media library.

## Unified CVP
                        	 Microapplication Configuration

The Cisco VVB sends HTTP requests to an HTTP media server to obtain audio files. It uses the following Cisco VVB configuration parameters to locate a server when not using a load balancer:

```
utils vvb add host-to-ip
```

The backup
                           		server is invoked only if the primary server is not accessible, and this is not
                           		a load-balancing method. Each new call attempts to connect to the primary
                           		server. If failover occurs, the backup server is used for the duration of the
                           		call; the next new call will attempt to connect to the primary server.

Note that
                           		the Media Server is not a fixed name, and it needs to match whatever name was
                           		assigned to the media_server ECC variable in the ICM script.

This configuration is applicable to all the microapplications except for Get Speech microapplication. For Get Speech microapplication,
                                       backup media server is not configured. You need to use an HTTP load balancer to achieve redundancy.

This feature is not required for Cisco VVB as DNS is used to resolve
                                       		  the hostname.

| Step 1 | From the
                                       			 Unified CVP Operations Console, select Device
                                             				  Management > Media Server . |
|---|---|
| Step 2 | Click Add
                                          				New to add a new Media Server or click Use As
                                          				Template to use an existing template to configure the new Media
                                       			 Server. |
| Step 3 | Click the
                                       			 following tabs and configure the settings based on your call flow: General tab.
                                             				  For more information, see General Settings . Device Pool tab. For more information about adding, deleting and editing device pool, see Add or Remove Device From Device Pool . |
| Step 4 | Click Save . |

| Field | Description | Default | Value | Restart
                                             					 Required |
|---|---|---|---|---|
| IP Address | The IP
                                             					 address of Media Server | None | Valid IP
                                             					 address. | No |
| Hostname | The name
                                             					 of the Media Server | None | Follow
                                             					 naming conventions for hostnames. | No |
| Description | The
                                             					 description of the Media Server | None | Up to
                                             					 1,024 characters. | No |
| FTP
                                             					 Enabled | Indicates whether a Media Server has FTP enabled. A Media Server, which has FTP enabled, is automatically populated as a session
                                             variable to the VXML Server. The default agent greeting recording application automatically uses the Media Servers defined
                                             in the Operations Console that have FTP enabled for the agent greeting recording. If Microsoft FTP Service is not enabled in Windows Services
                                             					 Control Panel, then set it to Automatic and start the service. SFTP is also supported with Media Servers. | Disabled | Select the
                                             					 check box to enable this feature. | No Use Test Sign-in button to verify the FTP credentials. |
| Anonymous
                                             					 Access | Indicates
                                             					 that this Media Server uses anonymous FTP access. In this case, the username is
                                             					 specified by default as anonymous. The password field is not specified for
                                             					 anonymous access. The user
                                             					 can specify the port number or select the default port number (21). | Disabled | Select the
                                             					 check box to enable this feature. You
                                             					 must enable FTP to enable Anonymous Access. | No Use Test
                                             					 Sign-in button to verify the FTP credentials. |
| Username
                                             					 and Password | These
                                             					 fields apply if FTP is enabled and Anonymous Access is disabled. In this case, enter
                                             					 the username and password. | None | A valid
                                             					 username and password. | No Use Test
                                             					 Sign-in button to verify the FTP credentials. |
| Port | Enter a
                                             					 new port number or use the default port number (21). For SFTP, use port 22 or any other custom port that you may have configured. | 21 | Valid
                                             					 ports are 1 to 65,535. | No Use Test
                                             					 Sign-in button to verify the FTP credentials. |

| Note | Unified CVP Call
                                    		Server, Media Server, and Unified CVP VXML Server are co-resident on the same
                                    		server. |
|---|---|

| Note | For routing client name, follow RFC 952 guidelines. |
|---|---|

| Step 1 | Set up the media_server ECC variable that specifies your UnifiedCVP
                                          			 VXMLServer in the ICM script by using use the Formula Editor to set the media_server ECC variable to concatenate("http://",Call.RoutingClient,":7000/CVP") . Call.RoutingClient is the built-in call variable that ICM
                                             				sets automatically for you. The routing client name in ICM is usually not the
                                             				same as the UnifiedCVP Server's hostname. |
|---|---|
| Step 2 | Apply the routing client name as a hostname in the VXML server . Do not use noncompliant characters such as an underscore as part of the hostname because the router cannot translate the
                                          hostname to an IP address if it contains noncomplaint characters. |
| Step 3 | Configure the
                                          			 routing client hostname for every UnifiedCVP Server Routing Client. |

| Step 1 | In the ICM
                                          			 script, set one of the ToExtVXML[] array variables with the call.routingclient
                                          			 data, such as ServerName=call.routingclient. This variable is passed to the
                                          			 UnifiedCVP VXMLServer, and the variable is stored in the session data with
                                          			 the variable name ServerName. |
|---|---|
| Step 2 | In Cisco
                                          			 Unified Call Studio, use a substitution to populate the Default Audio Path. Add
                                          			 the Application_Modifier element found in the Context folder, and specify the
                                          			 Default Audio Path in the Settings tab in the following format: http:// {Data.Session.ServerName} |

| Step 1 | Set up the media_server ECC variable that specifies your Media server
                                          			 in the ICM script by using the Formula Editor to set the media_server ECC variable to concatenate("http://",Call.RoutingClient) Call.RoutingClient is the built-in call variable that ICM sets automatically for you. The routing client name in ICM usually is not the same
                                             as the Unified CVP Server hostname. |
|---|---|
| Step 2 | Use the name of the routing client as a hostname in the VXML server . Do not use noncompliant characters such as an underscore as part of the hostname because the router cannot translate the
                                             hostname to an IP address if it contains any noncomplaint characters. |
| Step 3 | Configure the routing client hostname for every Unified CVP Server Routing Client. |

| To allow new media files to replace their predecessor in a reasonable amount of time while minimizing requests for data to
                                       the media server from the Virtualized Voice Browser, configure a cache expiration value in IIS Manager. The ideal value will
                                       require testing as it depends on how frequently media files are changed. To configure a cache expiration value in IIS Manager: Find the site you are using, go to the folder where the media files are being stored, and then click HTTP Response Headers . Click Set Common Headers on the Actions panel. Select Expire Web Content and set the desired value. |
|---|

| Caution | The Unified
                                    Customer Voice Portal includes a library of media files/prompts for individual
                                    digits, months (referenced internally by Unified Customer Voice Portal software
                                    for a Play Data script type request), default error messages, and so on. Creation of a full set of media/prompts for each locale referenced by
                                       the Unified CVP customer is the responsibility of the customer’s Media
                                       Administrator. |
|---|---|

| Caution | Any
                                    unexpected (and unsupported) type of media file encountered generates the
                                    logging of an error and a result code of False is returned to Unified ICME along with the ECC user.microapp.error_code set appropriately. From the caller’s
                                    perspective, nothing was played, however it is the Script Editor developer’s
                                    responsibility to write the script to handle this error
                                    condition. |
|---|---|

| Parameter | Location of Data | Description | Examples |
|---|---|---|---|
| Media Server Set | ECC variable: user.microapp.media _server | File location or base URL for the Media Server. When the Media Server URL is the DNS name and the DNS Server is configured to return multiple IP addresses for a host name,
                                       the Unified CVP attempts to get the media files from each Media Server IP address in sequence with the priority given to those
                                       on the subnet. Note Unified CVP supports playing prompts from flash on the GW. To play these prompts, set the media_server to "flash:" instead
                                                of the hostname or IP address of the media server. When using the Media Server set for external grammars or external VXML, if the Media Server URL is the DNS name with multiple
                                       IP addresses for the hostname, it is the ASR Engine’s responsibility to decide which machine to retrieve the grammar file
                                       from. Note Tomcat version (9.0.8) packaged with CVP does not support underscore "_" in the hostname. Therefore, it is recommended to
                                                   set user.microapp.media_server to a hostname that does not use "_". | Note | Unified CVP supports playing prompts from flash on the GW. To play these prompts, set the media_server to "flash:" instead
                                                of the hostname or IP address of the media server. | Note | Tomcat version (9.0.8) packaged with CVP does not support underscore "_" in the hostname. Therefore, it is recommended to
                                                   set user.microapp.media_server to a hostname that does not use "_". | Base URL example: http://www.machine1.com /dir1/ dirs/cust1 Note By convention, the service provider may include their customer names at the end of the Media Server set. | Note | By convention, the service provider may include their customer names at the end of the Media Server set. |
| Note | Unified CVP supports playing prompts from flash on the GW. To play these prompts, set the media_server to "flash:" instead
                                                of the hostname or IP address of the media server. |
| Note | Tomcat version (9.0.8) packaged with CVP does not support underscore "_" in the hostname. Therefore, it is recommended to
                                                   set user.microapp.media_server to a hostname that does not use "_". |
| Note | By convention, the service provider may include their customer names at the end of the Media Server set. |
| Locale | ECC variable: user.microapp.locale Default: en-us | This field is a combination of language and country with a default of en-us for English spoken in the United States. | en-us |
| Note The Unified CVP supports the following locales: en-us (English, United States) and en-gb (English, United Kingdom), es-es (Spanish, Spain), and es-mx (Spanish, Mexico). The locale defines the grammar of a Play Data script type. If a date is to be played with a locale of en-gb (English, United Kingdom), the date would be played in the order of day, month, then year; for en-us , it is month, day, year. | Note | The Unified CVP supports the following locales: en-us (English, United States) and en-gb (English, United Kingdom), es-es (Spanish, Spain), and es-mx (Spanish, Mexico). The locale defines the grammar of a Play Data script type. If a date is to be played with a locale of en-gb (English, United Kingdom), the date would be played in the order of day, month, then year; for en-us , it is month, day, year. |
| Note | The Unified CVP supports the following locales: en-us (English, United States) and en-gb (English, United Kingdom), es-es (Spanish, Spain), and es-mx (Spanish, Mexico). The locale defines the grammar of a Play Data script type. If a date is to be played with a locale of en-gb (English, United Kingdom), the date would be played in the order of day, month, then year; for en-us , it is month, day, year. |
| Media Library Type | The Media Library Type value passed from the VRU Script Name field. Valid options are: A - Application prompt library. S - System prompt library. V - External VXML. Default: A | The media library (directory) for the prompt is either the application prompt library defined by ECC variable user.microapp.app_media_lib
                                       (default "app" ) or the system prompt library defined by ECC variable user.microapp.sys_media_lib (default "sys" ). Note When the Media Library Type is V (external VXML), the VXML file will reside in the Application Prompt Library. Note When the Media Library Type is A (Application prompt library), you must create the directory specified by this variable.
                                                For example, if you use the default "app" directory, you must create an app directory in ./wwwroot/en-us | Note | When the Media Library Type is V (external VXML), the VXML file will reside in the Application Prompt Library. | Note | When the Media Library Type is A (Application prompt library), you must create the directory specified by this variable.
                                                For example, if you use the default "app" directory, you must create an app directory in ./wwwroot/en-us | A (user.microapp.app_media_ lib= app_banking) |
| Note | When the Media Library Type is V (external VXML), the VXML file will reside in the Application Prompt Library. |
| Note | When the Media Library Type is A (Application prompt library), you must create the directory specified by this variable.
                                                For example, if you use the default "app" directory, you must create an app directory in ./wwwroot/en-us |
| Media File Name | The Media File Name value passed from the VRU Script Name field. Valid options are the name of the .wav file to be played,
                                       or external VXML file name, or <blank>, which translates to playing no media. This file name is ignored if TTS is being used
                                       (that is, if the user.microapp.inline_tts ECC variable contains a value.) Default: none | Name of media file or external VXML file to be played. | Main_menu |
| Note There are four possible reasons for using <blank> as the Media File Name: (1) For Get Digits, a prompt may not be necessary,
                                                (2) the customer may want to have a "placeholder" in the script for playing a prompt which may or may not be there (for example, an emergency conditions message), (3) change
                                                the value of barge-in to indicate a buffer flush, and (4) TTS is being used and this field is ignored. | Note | There are four possible reasons for using <blank> as the Media File Name: (1) For Get Digits, a prompt may not be necessary,
                                                (2) the customer may want to have a "placeholder" in the script for playing a prompt which may or may not be there (for example, an emergency conditions message), (3) change
                                                the value of barge-in to indicate a buffer flush, and (4) TTS is being used and this field is ignored. |
| Note | There are four possible reasons for using <blank> as the Media File Name: (1) For Get Digits, a prompt may not be necessary,
                                                (2) the customer may want to have a "placeholder" in the script for playing a prompt which may or may not be there (for example, an emergency conditions message), (3) change
                                                the value of barge-in to indicate a buffer flush, and (4) TTS is being used and this field is ignored. |
| Media File Name Type | If not given as part of the Media File Name, the type is .wav | Type of media file to be played. | .wav |

| Note | Unified CVP supports playing prompts from flash on the GW. To play these prompts, set the media_server to "flash:" instead
                                                of the hostname or IP address of the media server. |
|---|---|

| Note | Tomcat version (9.0.8) packaged with CVP does not support underscore "_" in the hostname. Therefore, it is recommended to
                                                   set user.microapp.media_server to a hostname that does not use "_". |
|---|---|

| Note | By convention, the service provider may include their customer names at the end of the Media Server set. |
|---|---|

| Note | The Unified CVP supports the following locales: en-us (English, United States) and en-gb (English, United Kingdom), es-es (Spanish, Spain), and es-mx (Spanish, Mexico). The locale defines the grammar of a Play Data script type. If a date is to be played with a locale of en-gb (English, United Kingdom), the date would be played in the order of day, month, then year; for en-us , it is month, day, year. |
|---|---|

| Note | When the Media Library Type is V (external VXML), the VXML file will reside in the Application Prompt Library. |
|---|---|

| Note | When the Media Library Type is A (Application prompt library), you must create the directory specified by this variable.
                                                For example, if you use the default "app" directory, you must create an app directory in ./wwwroot/en-us |
|---|---|

| Note | There are four possible reasons for using <blank> as the Media File Name: (1) For Get Digits, a prompt may not be necessary,
                                                (2) the customer may want to have a "placeholder" in the script for playing a prompt which may or may not be there (for example, an emergency conditions message), (3) change
                                                the value of barge-in to indicate a buffer flush, and (4) TTS is being used and this field is ignored. |
|---|---|

| Note | Do not set the user.microapp.locale ECC variable if you used the default en-us . Also, remember that all locale values are
                                    case-sensitive. |
|---|---|

| Symbol (where
                                       				applicable) | Decimal Value | Media File Name | Media File
                                       				Content | Data Play Back
                                       				Types / When Media File Is Used |
|---|---|---|---|---|
|  |  | point | point | Number |
|  |  | minus | minus | Number |
| 0 | 48 | 0 | zero | All except DOW |
| 1 | 49 | 1 | one (masculine
                                       				version), uno (es-mx and es-es) | All except DOW |
| 2 | 50 | 2 | two | All except DOW |
| 3 | 51 | 3 | three | All except DOW |
| 4 | 52 | 4 | four | All except DOW |
| 5 | 53 | 5 | five | All except DOW |
| 6 | 54 | 6 | six | All except DOW |
| 7 | 55 | 7 | seven | All except DOW |
| 8 | 56 | 8 | eight | All except DOW |
| 9 | 57 | 9 | nine | All except DOW |
|  |  | 10 | ten | Same for the
                                       				rest of all the numbers |
|  |  | 11 | eleven |  |
|  |  | 12 | twelve |  |
|  |  | 13 | thirteen |  |
|  |  | 14 | fourteen |  |
|  |  | 15 | fifteen |  |
|  |  | 16 | sixteen |  |
|  |  | 17 | seventeen |  |
|  |  | 18 | eighteen |  |
|  |  | 19 | nineteen |  |
|  |  | 20 | twenty |  |
|  |  | 21 | twenty-one |  |
|  |  | 22 | twenty-two |  |
|  |  | 23 | twenty-three |  |
|  |  | 24 | twenty-four |  |
|  |  | 25 | twenty-five |  |
|  |  | 26 | twenty-six |  |
|  |  | 27 | twenty-seven |  |
|  |  | 28 | twenty-eight |  |
|  |  | 29 | twenty-nine |  |
|  |  | 30 | thirty |  |
|  |  | 31 | thirty-one |  |
|  |  | 32 | thirty-two |  |
|  |  | 33 | thirty-three |  |
|  |  | 34 | thirty-four |  |
|  |  | 35 | thirty-five |  |
|  |  | 36 | thirty-six |  |
|  |  | 37 | thirty-seven |  |
|  |  | 38 | thirty-eight |  |
|  |  | 39 | thirty-nine |  |
|  |  | 40 | forty |  |
|  |  | 41 | forty-one |  |
|  |  | 42 | forty-two |  |
|  |  | 43 | forty-three |  |
|  |  | 44 | forty-four |  |
|  |  | 45 | forty-five |  |
|  |  | 46 | forty-six |  |
|  |  | 47 | forty-seven |  |
|  |  | 48 | forty-eight |  |
|  |  | 49 | forty-nine |  |
|  |  | 50 | fifty |  |
|  |  | 51 | fifty-one |  |
|  |  | 52 | fifty-two |  |
|  |  | 53 | fifty-three |  |
|  |  | 54 | fifty-four |  |
|  |  | 55 | fifty-five |  |
|  |  | 56 | fifty-six |  |
|  |  | 57 | fifty-seven |  |
|  |  | 58 | fifty-eight |  |
|  |  | 59 | fifty-nine |  |
|  |  | 60 | sixty |  |
|  |  | 61 | sixty-one |  |
|  |  | 62 | sixty-two |  |
|  |  | 63 | sixty-three |  |
|  |  | 64 | sixty-four |  |
|  |  | 65 | sixty-five |  |
|  |  | 66 | sixty-six |  |
|  |  | 67 | sixty-seven |  |
|  |  | 68 | sixty-eight |  |
|  |  | 69 | sixty-nine |  |
|  |  | 70 | seventy |  |
|  |  | 71 | seventy-one |  |
|  |  | 72 | seventy-two |  |
|  |  | 73 | seventy-three |  |
|  |  | 74 | seventy-four |  |
|  |  | 75 | seventy-five |  |
|  |  | 76 | seventy-six |  |
|  |  | 77 | seventy-seven |  |
|  |  | 78 | seventy-eight |  |
|  |  | 79 | seventy-nine |  |
|  |  | 80 | eighty |  |
|  |  | 81 | eighty-one |  |
|  |  | 82 | eighty-two |  |
|  |  | 83 | eighty-three |  |
|  |  | 84 | eighty-four |  |
|  |  | 85 | eighty-five |  |
|  |  | 86 | eighty-six |  |
|  |  | 87 | eighty-seven |  |
|  |  | 88 | eighty-eight |  |
|  |  | 89 | eighty-nine |  |
|  |  | 90 | ninety |  |
|  |  | 91 | ninety-one |  |
|  |  | 92 | ninety-two |  |
|  |  | 93 | ninety-three |  |
|  |  | 94 | ninety-four |  |
|  |  | 95 | ninety-five |  |
|  |  | 96 | ninety-six |  |
|  |  | 97 | ninety-seven |  |
|  |  | 98 | ninety-eight |  |
|  |  | 99 | ninety-nine |  |
|  |  | oh | oh | 24TOD, Date |
|  |  | hundred | hundred | Number, 24TOD,
                                       				Date, Currency |
|  |  | thousand | thousand | Number, Date,
                                       				Currency |
|  |  | million | million | Number,
                                       				Currency |
|  |  | billion | billion | Number, Date,
                                       				Currency |
|  |  | trillion | trillion | Number,
                                       				Currency |

| Note | If ordinal system
                                    	 prompts are to be used in a script for a purpose other than dates, they should
                                    	 be recorded as application prompts with the true ordinal values. |
|---|---|

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
|  |  | 1ord | first | Date |
|  |  | 2ord | second | Date for all
                                       				ordinal numbers |
|  |  | 3ord | third |  |
|  |  | 4ord | fourth |  |
|  |  | 5ord | fifth |  |
|  |  | 6ord | sixth |  |
|  |  | 7ord | seventh |  |
|  |  | 8ord | eighth |  |
|  |  | 9ord | nineth |  |
|  |  | 10ord | tenth |  |
|  |  | 11ord | eleventh |  |
|  |  | 12ord | twelveth |  |
|  |  | 13ord | thirteenth |  |
|  |  | 14ord | fourteenth |  |
|  |  | 15ord | fifteenth |  |
|  |  | 16ord | sixteenth |  |
|  |  | 17ord | seventeenth |  |
|  |  | 18ord | eighteenth |  |
|  |  | 19ord | nineteenth |  |
|  |  | 20ord | twentieth |  |
|  |  | 21ord | twenty-first |  |
|  |  | 22ord | twenty-second |  |
|  |  | 23ord | twenty-third |  |
|  |  | 24ord | twenty-fourth |  |
|  |  | 25ord | twenty-fifth |  |
|  |  | 26ord | twenty-sixth |  |
|  |  | 27ord | twenty-seventh |  |
|  |  | 28ord | twenty-eight |  |
|  |  | 29ord | twenty-nineth |  |
|  |  | 30ord | thirtieth |  |
|  |  | 31ord | thirty-first |  |

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
| ½ | 189 | one_half | one half | Char |
| ¼ | 188 | one_quarter | one quarter | Char |
| ¾ | 190 | three_quarters | three quarters | Char |
| A, a | 65,97 | a | A | Char |
| B,b | 66,98 | b | B | Char |
| C, c | 67,99 | c | C | Char |
| D, d | 68,100 | d | D | Char |
| E, e | 69,101 | e | E | Char |
| F, f | 70,102 | f | F | Char |
| G, g | 71,103 | g | G | Char |
| H, h | 72,104 | h | H | Char |
| I, I | 73,105 | I | I | Char |
| J, j | 74,106 | j | J | Char |
| K, k | 75,107 | k | K | Char |
| L, l | 76,108 | l | L | Char |
| M, m | 77,109 | m | M | Char |
| N, n | 78,110 | n | N | Char |
| O, o | 79,111 | o | O | Char |
| P, p | 80,112 | p | P | Char |
| Q, q | 81,113 | q | Q | Char |
| R, r | 82,114 | r | R | Char |
| S, s | 83,115 | s | S | Char |
| T, t | 84,116 | t | T | Char |
| U, u | 85,117 | u | U | Char |
| V, v | 86,118 | v | V | Char |
| W, w | 87,119 | w | W | Char |
| X, x | 88,120 | x | X | Char |
| Y, y | 89,121 | y | Y | Char |
| Z, z | 90,122 | z | Z | Char |
| Œ, œ | 140,156 | oe_140_156 | Ligature OE | Char |
| À,à | 192,224 | a_192_224 | A grave | Char |
| Á,á | 193,225 | a_193_225 | A acute | Char |
| Â,â | 194,226 | a_194_226 | A circumflex | Char |
| Ã,ã | 195,227 | a_195_227 | A tilde | Char |
| Ä,ä | 196,228 | a_196_228 | A umlaut | Char |
| Å,å | 197,229 | a_197_229 | A with ring
                                       				above | Char |
| Æ,æ | 198,230 | ae_198_230 | Ligature AE | Char |
| È,è | 200,232 | e_200_232 | E grave | Char |
| É,é | 201,233 | e_201_233 | E acute | Char |
| Ê,ê | 202,234 | e_202_234 | E circumflex | Char |
| Ë,ë | 203,235 | e_203_235 | E umlaut |  |
| Ì,ì | 204,236 | i_204_236 | I grave | Char |
| Í, í | 205,237 | i_205 | I acute | Char |
| Î,î | 206,238 | i_206 | I circumflex | Char |
| Ï,ï | 207,239 | i_207 | I umlaut | Char |
| Ð | 208 | char_208 | character 208 | Char |
| ð | 240 | char_240 | character 240 |  |
| Ò,ò | 210,242 | o_210_242 | O grave | Char |
| Ó,ó | 211,243 | o_211_243 | O acute | Char |
| Ô,ô | 212,244 | o_212_244 | O circumflex | Char |
| Õ,õ | 213,245 | o_213_245 | O tilde | Char |
| Ö,ö | 214,246 | o_214_246 | O umlaut | Char |
| x | 215 | multiply | multiplication
                                       				sign | Char |
| Ø,ø | 216,248 | o_216_248 | oh stroke | Char |
| Ù,ù | 217,249 | u_217_249 | U grave | Char |
| Ú,ú | 218,250 | u_218_250 | U acute | Char |
| Û,û | 219,251 | u_219_251 | U circumflex | Char |
| Ü,ü | 220,252 | u_220_252 | U umlaut | Char |
| Ý,ý | 221,253 | y_221_253 | Y acute | Char |
| Þ | 222 | char_222 | character 222 | Char |
| ß | 223 | ss | double s | Char |
| ÷ | 247 | divide | division sign | Char |
| þ | 254 | char_254 | character 254 | Char |
| Ÿ,ÿ | 159,255 | y_159_255 | character 159
                                       				or 255 | Char |

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
|  |  | January | January | Date |
|  |  | February | February | Date |
|  |  | March | March | Date |
|  |  | April | April | Date |
|  |  | May | May | Date |
|  |  | June | June | Date |
|  |  | July | July | Date |
|  |  | August | August | Date |
|  |  | September | September | Date |
|  |  | October | October | Date |
|  |  | November | November | Date |
|  |  | December | December | Date |

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
|  |  | Sunday | Sunday | DOW |
|  |  | Monday | Monday | DOW |
|  |  | Tuesday | Tuesday | DOW |
|  |  | Wednesday | Wednesday | DOW |
|  |  | Thursday | Thursday | DOW |
|  |  | Friday | Friday | DOW |
|  |  | Saturday | Saturday | DOW |

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
|  |  | hour | hour | Etime, 24TOD
                                       				per locale, TOD per locale |
|  |  | hours | hours | Etime,24TOD
                                       				per locale,TOD per locale |
|  |  | minute | minute | Etime |
|  |  | minutes | minutes | Etime |
|  |  | second | second | Etime,24TOD |
|  |  | seconds | seconds | Etime,24TOD |
|  |  | on | on | per
                                       				locale(unused for en-us) |
|  |  | at | at | per
                                       				locale(unused for en-us) |
|  |  | am | am | TOD |
|  |  | pm | pm | TOD |
|  |  | oclock | oclock | TOD |

| Note | The customer’s Media Administrator may want to replace the contents of "currency_minus" (for the negative amount) and "currency_and" (the latter can even be changed to contain silence). |
|---|---|

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
|  |  | currency_
                                       				minus | minus | Currency |
|  |  | currency_and | and | Currency |
| $ | 36 | USD_dollar | dollar | Currency |
| USD_dollars | dollars | Currency |
| Note Unified
                                                				CVP uses the USD_dollar.wav and USD_dollars.wav media files; the dollar.wav and
                                                				dollars.wav used by ISN Version 1.0 are no longer installed. | Note | Unified
                                                				CVP uses the USD_dollar.wav and USD_dollars.wav media files; the dollar.wav and
                                                				dollars.wav used by ISN Version 1.0 are no longer installed. |
| Note | Unified
                                                				CVP uses the USD_dollar.wav and USD_dollars.wav media files; the dollar.wav and
                                                				dollars.wav used by ISN Version 1.0 are no longer installed. |
| $ | 36 | CAD_dollar | dollar | Currency |
|  |  | CAD_dollars | dollars | Currency |
|  |  | HKD_dollar | dollar | Currency |
|  |  | HKD_dollars | dollars | Currency |
| ¢ | 162 | cent | cent | Currency |
|  |  | cents | cents | Currency |
|  |  | euro | euro | Currency |
| £ | 163 | GBP_pound | pound | Currency |
|  |  | GBP_pounds | pounds | Currency |
|  |  | penny | penny | Currency |
|  |  | pence | pence | Currency |
|  |  | MXN_peso | peso | Currency |
|  |  | MXN_pesos | pesos | Currency |
|  |  | centavo | centavo | Currency |
|  |  | centavos | centavos | Currency |

| Note | Unified
                                                				CVP uses the USD_dollar.wav and USD_dollars.wav media files; the dollar.wav and
                                                				dollars.wav used by ISN Version 1.0 are no longer installed. |
|---|---|

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
|  |  | silence_.1_
                                       				sec | (.1 second of
                                       				silence) | Used for
                                       				pauses where needed |
|  |  | silence_.25_
                                       				sec | (.25 second
                                       				of silence) | Used for
                                       				pauses where needed |
|  |  | silence_.5_
                                       				sec | (.5 second of
                                       				silence) | Used for
                                       				pauses where needed |
|  |  | silence_1_sec | (1 second of
                                       				silence) | Used for
                                       				pauses where needed |
|  |  | and | and | Etime,TOD,25TOD |

| Symbol (where
                                       				applicable) | Decimal Value | Media File
                                       				Name | Media File
                                       				Content | Data Play
                                       				Back Types / When Media File Is Used |
|---|---|---|---|---|
|  | 32 | space | space | Char |
| ! | 33 | exclamation_
                                       				mark | exclamation
                                       				mark | Char |
| " | 34 | double_ quote | double quote | Char |
| # | 35 | pound | pound | Char |
| % | 37 | percent | percent | Char |
| & | 38 | ampersand | ampersand | Char |
| ' | 39 | apostrophe | apostrophe | Char |
| ( | 40 | open_
                                       				parenthesis | open
                                       				parenthesis | Char |
| ) | 41 | close_
                                       				parenthesis | close
                                       				parenthesis | Char |
| * | 42 | asterisk | asterisk | Char |
| + | 43 | plus | plus | Char |
| , | 44 | comma | comma | Char |
| - | 45 | hyphen | hyphen | Char |
| . | 46 | period | period | Char |
| / | 47 | slash | slash | Char |
| : | 58 | colon | colon | Char |
| ; | 59 | semicolon | semicolon | Char |
| < | 60 | less_than | less than | Char |
| = | 61 | equal | equal | Char |
|  | 62 | greater_than | greater than | Char |
| ? | 63 | question_ mark | question mark | Char |
| @ | 64 | at_symbol | at | Char |
| [ | 91 | left_square_bracket | left square
                                       				bracket | Char |
| \ | 92 | backslash | backslash | Char |
| ] | 93 | right_square_bracket | right square
                                       				bracket | Char |
| ^ | 94 | caret | caret | Char |
| _ | 95 | underscore | underscore | Char |
| ` | 96 | single_quote | single quote | Char |
| { | 123 | open_brace | open brace | Char |
| \| | 124 | pipe | pipe | Char |
| } | 125 | close_brace | close brace | Char |
| ~ | 126 | tilde | tilde | Char |
| ’ | 130 | char_130 | low single
                                       				quote | Char |
| ƒ | 131 | char_131 | F with hook | Char |
| ” | 132 | low double
                                       				quote | low double
                                       				quote | Char |
| … | 133 | ellipsis | ellipsis | Char |
| † | 134 | char_134 | character 134 | Char |
| ‡ | 135 | char_135 | character 135 | Char |
| ˆ | 136 | char_136 | character 136 | Char |
| ‰ | 137 | per_mille | per mile | Char |
| Š | 138 | char_138 | character 138 |  |
| < | 139 | left_pointing
                                       				_angle | left pointing
                                       				angle | Char |
| ‘ | 145 | left_single_
                                       				quote | left single
                                       				quote | Char |
| ’ | 146 | right_single_
                                       				quote | right single
                                       				quote | Char |
| “ | 147 | left_double_
                                       				quote | left double
                                       				quote | Char |
| ” | 148 | right_double
                                       				_quote | right double
                                       				quote | Char |
| · | 149 | bullet | bullet | Char |
| – | 150 | en_dash | en dash | Char |
| — | 151 | em_dash | em dash |  |
| ˜ | 152 | small_tilde | small tilde | Char |
| ™ | 153 | trade_mark | trade mark | Char |
| š | 154 | char_154 | character 154 | Char |
| › | 155 | char_155 | character 155 | Char |
| ¡ | 161 | exclamation_
                                       				mark_ inverted | inverted
                                       				exclamation mark | Char |
| ¤ | 164 | char_164 | character 164 | Char |
| ¦ | 166 | broken_pipe | broken pipe | Char |
| § | 167 | section | section | Char |
| ¨ | 168 | char_168 | character 168 | Char |
| © | 169 | copyright | copyright | Char |
| ª | 170 | char_170 | character 170 | Char |
| « | 171 | left_double_
                                       				angle_ quote | left double
                                       				angle quote | Char |
| ¬ | 172 | not | not | Char |
| - | 173 | char_173 | character 173 | Char |
| ® | 174 | registered | registered | Char |
| ¯ | 175 | char_175 | character 175 | Char |
| ° | 176 | degree | degree | Char |
| ± | 177 | plus_minus | plus or minus | Char |
| ² | 178 | superscript_ 2 | superscript
                                       				two | Char |
| ³ | 179 | superscript_ 3 | superscript
                                       				three | Char |
| ´ | 180 | acute_accent | acute accent | Char |
| µ | 181 | micro | micro | Char |
| ¶ | 182 | paragraph | paragraph | Char |
| · | 183 | middle_dot | middle dot | Char |
| ¸ | 184 | cedilla | cedilla | Char |
| ¹ | 185 | superscript_ 1 | superscript
                                       				one | Char |
| º | 186 | char_186 | character 186 | Char |
| » | 187 | right_double
                                       				_angle_ quote | right double
                                       				angle quote | Char |
| ¿ | 191 | question_
                                       				mark_ inverted | inverted
                                       				question mark | Char |

| Symbol (where applicable) | Decimal Value | Media File Name | Media File Content | Data Play Back Types / When Media
                                          File Is Used |
|---|---|---|---|---|
| Error | v | invalid_entry_error | Your entry is invalid. | Error message |
|  | v | no_entry_error | Please make a selection. | Error message |
|  | v | system_error | We are currently experiencing technical difficulties with this site.
                                          Please try again later when we can service you much better. | Error message |
|  | v | critical_error | We are currently experiencing technical difficulties with
                                          this site. Please try again later when we can service you much better. | Error message |
|  | v | critical_error_ULaw . | We are currently experiencing
                                          technical difficulties with this site. Please try again later when we can
                                          service you much better | Error
                                          message |
|  | v | critical_error_ALaw | We are
                                          currently experiencing technical difficulties with this site. Please try again
                                          later when we can service you much better. | Error message |
|  | v | 440beep | <single beep tone> | Unused |
|  | v | busy_tone | <single busy
                                          tone> | Unused |
|  | v | busy_tone30 | <busy tone 1
                                          per second for 30 seconds> | Unused |
|  | v | central | Central | Unused |
|  | v | credit_of | Credit Of | Unused |
|  | v | dash | dash | Unused |
|  | v | daylight | daylight | Unused |
|  | v | dialtone | <4 seconds of
                                          dial tone> | Unused |
|  | v | dialtone2fastbusy60 | <9
                                          seconds of dialtone> followed by <30 seconds of fast busy tone> | Unused |
|  | v | dot | dot | Unused |
|  | v | eastern | Eastern | Unused |
|  | v | ENTER_PHONE_NUMBER | Please
                                          enter the phone number. | Unused |
|  | v | fastbusy | <a single fastbusy
                                          tone + silence (total of 1 second)> | Unused |
|  | v | fastbusy60 | 30 seconds of
                                          <fastbusy tone> | Unused |
|  | v | FINISHED | When you have
                                          finished, press | Unused |
|  | v | goodbye | Goodbye | Unused |
|  | v | Mountain | Mountain | Unused |
|  | v | negative | negative | Unused |
|  | v | of | of | Unused |
|  | v | pmgr_sys | pmgr_sys | Unused |
|  | v | pacific | Pacific | Unused |
|  | v | positive | positive | Unused |
|  | v | ringback | <ring back tone
                                          for 1 second followed by 2 seconds of silence> | Unused |
|  | v | savings | savings | Unused |
|  | v | standard | Standard | Unused |
|  | v | Star | star | Unused |
|  | v | thankyou | Thank you | Unused |
|  | v | the | the | Unused |
|  | v | time | time | Unused |
|  | v | try_again | Please try again | Unused |

| Note | If you do
                                             			 not want an English spoken critical media, you need to copy the language
                                             			 specific files to the location specified in this section. |
|---|---|

| Note | You can
                                             			 record "override" prompts to replace the critical media files. However, you must save them with
                                             			 their original hard-coded names and place them in their original locations. |
|---|---|

| Note | These files are
                                       		shared by all applications. |
|---|---|

| Note | Override flags
                                       		are available for the Get Digits, Get Speech, and Menu micro-applications,
                                       		only. See Feature Guide -
                                          		  Writing Scripts for Cisco Unified Customer Voice Portal for details. |
|---|---|

| Note | This override
                                       		will not work when there is not a specific file name used (for instance, when
                                       		Unified CVP is using the TTS feature). |
|---|---|

| Note | This configuration is applicable to all the microapplications except for Get Speech microapplication. For Get Speech microapplication,
                                       backup media server is not configured. You need to use an HTTP load balancer to achieve redundancy. |
|---|---|

| Note | This feature is not required for Cisco VVB as DNS is used to resolve
                                       		  the hostname. |
|---|---|