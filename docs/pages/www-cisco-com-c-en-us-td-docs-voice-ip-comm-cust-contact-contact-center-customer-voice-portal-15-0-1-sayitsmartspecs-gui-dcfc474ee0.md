---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-sayitsmartspecs-gui-dcfc474ee0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/sayitsmartspecs/guide/cvp_b_1501-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_m_1501-currency.html
retrieved_at: 2026-08-21T03:04:44.091606+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal Release 15.0(1)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal Release 15.0(1)

Updated: March 1, 2025

Chapter: Currency

## Chapter: Currency

# Currency

## Description

This Say It Smart type handles the reading of a currency value in dollars and cents. It only handles dollars and cents, so
                           will work with U.S., Canadian, and other currencies using dollars and cents. The input data can optionally include a dollar
                           sign ($) and does not need to include a decimal point. The amount can be positive or negative, and can even contain an exponent.
                           The amount can be up to $999 trillion. The value is read ordinarily, though if one component is zero, it will not be read.
                           If the decimal contains more than two significant digits it will be rounded to the nearest cent.

This
                           plug-in uses the Unified CVP Number Say it Smart plug-in to render the dollar
                           and cent amounts. It uses the same audio files so if recording was done to
                           support Number, those files can be leveraged to support
                           Currency.

## Input Formats

Name

(Display Name)

Description

standard

(Standard Currency)

The data can appear as a standard
                                          number with or without a minus sign, decimal point, $ sign, and even an
                                          exponent. No commas are
                                          allowed.

## Output Formats

Name

(Display
                                             Name)

Input Format
                                             Depends On

Description

dollars_cents

(X dollars and Y
                                          cents)

standard

The dollar and cent amounts are read
                                          separately.

## Filesets

Name

(Display
                                             Name)

Output Format
                                             Depends On

Description

standard

(Standard)

dollars_cents

This fileset involves fewer audio files to render the currency amount but
                                          at the cost of sounding a bit robotic. This directly correlates to the Unified
                                          CVP Number Say it Smart plug-in’s standard fileset.

enhanced

(Enhanced)

dollars_cents

This fileset
                                          involves more audio files to render a better sounding currency amount. This
                                          directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset.

## Audio Files

All audio files must
                              		  be named as appears below. The names do not have an extension, the developer
                              		  can choose whatever file type supported by their voice browser.

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

hundred

thousand

million

billion

trillion

dollars

dollar

and

cents

cent

Enhanced Fileset

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

thousand

million

billion

trillion

dollars

dollar

and

cents

cent

## Currency
                        	 Examples

Example #1

Data:

$25052.085

Input
                                          						Format:

standard

Output
                                          						Format:

dollars_cents

Fileset

enhanced

Playback:

"25" "thousand" "52" "dollars" "and" "9" "cents"

Example #2

Data:

0.01

Input Format:

standard

Output Format:

dollars_cents

Fileset

standard

Playback:

"1" "cent"

Example #3

Data:

6.99E4

Input Format:

standard

Output Format:

dollars_cents

Fileset

standard

Playback:

"60" "9" "thousand" "9" "hundred" "dollars"

Example #4

Data:

-$69900

Input Format:

standard

Output Format:

dollars_cents

Fileset

enhanced

Playback:

"negative" "69" "thousand" "900" "dollars"

| Name (Display Name) | Description |
|---|---|
| standard (Standard Currency) | The data can appear as a standard
                                          number with or without a minus sign, decimal point, $ sign, and even an
                                          exponent. No commas are
                                          allowed. |

| Name (Display
                                             Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| dollars_cents (X dollars and Y
                                          cents) | standard | The dollar and cent amounts are read
                                          separately. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard) | dollars_cents | This fileset involves fewer audio files to render the currency amount but
                                          at the cost of sounding a bit robotic. This directly correlates to the Unified
                                          CVP Number Say it Smart plug-in’s standard fileset. |
| enhanced (Enhanced) | dollars_cents | This fileset
                                          involves more audio files to render a better sounding currency amount. This
                                          directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset. |

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | negative |  |
| hundred | thousand | million | billion | trillion | dollars | dollar | and | cents | cent |

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
| negative | thousand | million | billion | trillion | dollars | dollar | and | cents | cent |

| Data: | $25052.085 |
|---|---|
| Input
                                          						Format: | standard |
| Output
                                          						Format: | dollars_cents |
| Fileset | enhanced |
| Playback: | "25" "thousand" "52" "dollars" "and" "9" "cents" |

| Data: | 0.01 |
|---|---|
| Input Format: | standard |
| Output Format: | dollars_cents |
| Fileset | standard |
| Playback: | "1" "cent" |

| Data: | 6.99E4 |
|---|---|
| Input Format: | standard |
| Output Format: | dollars_cents |
| Fileset | standard |
| Playback: | "60" "9" "thousand" "9" "hundred" "dollars" |

| Data: | -$69900 |
|---|---|
| Input Format: | standard |
| Output Format: | dollars_cents |
| Fileset | enhanced |
| Playback: | "negative" "69" "thousand" "900" "dollars" |