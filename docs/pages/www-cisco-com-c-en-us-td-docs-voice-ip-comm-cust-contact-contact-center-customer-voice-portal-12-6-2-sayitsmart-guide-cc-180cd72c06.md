---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-sayitsmart-guide-cc-180cd72c06
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/sayitsmart/guide/ccvp_b_1262-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_0111.html
retrieved_at: 2026-08-21T17:39:52.203433+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Number

## Chapter: Number

# Number

Plugin
                                    Name:

number

Display Name:

Number

Class Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmartNumber

## Description

This Say It Smart type handles the reading of any number. The number can
                           be negative or positive, contain a decimal, and can even contain an exponent.
                           The whole part of the number is read normally and the decimal part of the
                           number is read digit-by-digit. This plug-in can handle numbers up to 999
                           trillion.

The number can be read back in a way that sounds somewhat
                           robotic, though it uses a minimum number of audio files. The number can also be
                           read back in a manner that sounds better to the caller but will require more
                           files to do so. These differences are encapsulated in the Number type’s two
                           filesets: standard and enhanced . All Unified CVP Say It Smart plug-ins that
                           have numerical components use the Number plug-in to convert their numbers so
                           those plug-ins will list these two filesets as well.

## Input
                        	 Formats

Name

(Display Name)

Description

standard

(Standard)

This represents any number, negative or positive, with or
                                          						without a decimal, and optionally containing an exponent. No commas are
                                          						allowed.

## Output Formats

Name

(Display Name)

Input Format
                                             Depends On

Description

standard

(Standard Number)

standard

The whole part of the number is read normally and
                                          the decimal is read digit-by-digit.

no_trailing_0s

(Read w/ no Trailing
                                          0s)

standard

The whole part of the number is read normally, the
                                          decimal is read digit-by-digit, omitting trailing zeros.

## Filesets

Name

(Display
                                             Name)

Output Format
                                             Depends On

Description

standard

(Standard)

standard no_trailing_0s

This fileset involves fewer audio files to render
                                          the number but at the cost of sounding a bit robotic.

enhanced

(Enhanced)

standard
                                          no_trailing_0s

This fileset
                                          involves more audio files to render a better sounding
                                          number.

## Audio Files

Standard Fileset

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

30

40

50

60

70

80

90

negative

point

hundred

thousand

million

billion

trillion

Enhanced
                                 Fileset

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

200

300

400

500

600

700

800

900

1000

2000

3000

4000

5000

6000

7000

8000

9000

negative

point

thousand

million

billion

trillion

## Examples

Example #1

Data:

4836945.160

Input Format:

standard

Output Format:

standard

Fileset

enhanced

Playback:

"4" "million" "800" "36" "thousand" "900" "45" "point" "1" "6" "0"

Example #2

Data:

3.10

Input
                                          						Format:

standard

Output
                                          						Format:

no_trailing_0s

Fileset

standard

Playback:

"3" "point" "1"

Example #3

Data:

36.1234E2

Input Format:

standard

Output Format:

standard

Fileset

standard

Playback:

"3" "thousand" "6" "hundred" "12" "point" "3" "4"

Example #4

Data:

-3E-2

Input Format:

standard

Output Format:

standard

Fileset

standard

Playback:

"negative" "0" "point" "0" "0" "3"

| Plugin
                                    Name: | number |
|---|---|
| Display Name: | Number |
| Class Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmartNumber |

| Name (Display Name) | Description |
|---|---|
| standard (Standard) | This represents any number, negative or positive, with or
                                          						without a decimal, and optionally containing an exponent. No commas are
                                          						allowed. |

| Name (Display Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard Number) | standard | The whole part of the number is read normally and
                                          the decimal is read digit-by-digit. |
| no_trailing_0s (Read w/ no Trailing
                                          0s) | standard | The whole part of the number is read normally, the
                                          decimal is read digit-by-digit, omitting trailing zeros. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard) | standard no_trailing_0s | This fileset involves fewer audio files to render
                                          the number but at the cost of sounding a bit robotic. |
| enhanced (Enhanced) | standard
                                          no_trailing_0s | This fileset
                                          involves more audio files to render a better sounding
                                          number. |

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |  |  |
| negative | point | hundred | thousand | million | billion | trillion |  |  |  |

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |
| 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |
| 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 |
| 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 |
| 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 |
| 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 |
| 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 |
| 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 |
| 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |  |
| 1000 | 2000 | 3000 | 4000 | 5000 | 6000 | 7000 | 8000 | 9000 |  |
| negative | point | thousand | million | billion | trillion |  |  |  |  |

| Data: | 4836945.160 |
|---|---|
| Input Format: | standard |
| Output Format: | standard |
| Fileset | enhanced |
| Playback: | "4" "million" "800" "36" "thousand" "900" "45" "point" "1" "6" "0" |

| Data: | 3.10 |
|---|---|
| Input
                                          						Format: | standard |
| Output
                                          						Format: | no_trailing_0s |
| Fileset | standard |
| Playback: | "3" "point" "1" |

| Data: | 36.1234E2 |
|---|---|
| Input Format: | standard |
| Output Format: | standard |
| Fileset | standard |
| Playback: | "3" "thousand" "6" "hundred" "12" "point" "3" "4" |

| Data: | -3E-2 |
|---|---|
| Input Format: | standard |
| Output Format: | standard |
| Fileset | standard |
| Playback: | "negative" "0" "point" "0" "0" "3" |