---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-sayitsmartspecs-gui-b42f472efe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/sayitsmartspecs/guide/cvp_b_1501-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_m_1501-date.html
retrieved_at: 2026-08-21T03:04:53.255228+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal Release 15.0(1)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal Release 15.0(1)

Updated: March 1, 2025

Chapter: Date

## Chapter: Date

# Date

## Description

This Say It Smart type handles the reading of a date or portions of a
                           date. It handles many input formats for the date, some of which provide only a
                           partial date. The plug-in also supports the components of the date separated by
                           forward slashes (/) and will require the use of this delimiter if any component
                           of the date is expressed with one digit instead of two (for example, May 2 can
                           be expressed as 0502 or 5/2 where the slash is required if any component is not
                           padded with 0s). The date is read back in standard English fashion; the month
                           name (rather than the number), the day, and the year. If only partial
                           information is available, only that data will be read. The plug-in will only
                           read legitimate dates according to the standard Gregorian calendar and will
                           throw an error if an incorrect date is given.

This plug-in uses the
                           Unified CVP Number Say it Smart plug-in to render the year. It uses the same
                           audio files so recordings done to support Number can be leveraged to support
                           Date.

## Input
                        	 Formats

All input formats
                              		  with more than one date component can appear delimited with forward slashes.

Name

(Display Name)

Description

mmddyyyy

(MMDDYYYY)

The full date with the month, day, and four digit year. The
                                          						data can be handled in any of the following formats:

mmddyyyy

mm/dd/yyyy

m/dd/yyyy

mm/d/yyyy

m/d/yyyy

mmddyy

(MMDDYY)

The full date with the month, day, and two digit year. The
                                          						data can be handled in any of the following formats:

mmddyy

mm/dd/yy

m/dd/yy

mm/d/yy

mm/dd/y

m/d/yy

m/dd/y

mm/d/y

m/d/y

ddmmyyyy

(DDMMYYYY)

The full date with the day, month, and four digit year. The
                                          						data can be handled in any of the following formats:

ddmmyyyy

dd/mm/yyyy

d/mm/yyyy

dd/m/yyyy

d/m/yyyy

ddmmyy

(DDMMYY)

The full date with the day, month, and two digit year. The
                                          						data can be handled in any of the following formats:

ddmmyy

dd/mm/yy

d/mm/yy

dd/m/yy

dd/mm/y

d/m/yy

d/mm/y

dd/m/y

d/m/y

yyyymmdd

(YYYYMMDD)

The full date with the four digit year, month, and day. The
                                          						data can be handled in any of the following formats:

yyyymmdd

yyyy/mm/dd

yyyy/m/dd

yyyy/mm/d

yyyy/m/d

mmyyyy

(MMYYYY)

The month and four digit year. The data can be handled in
                                          						any of the following formats:

mmyyyy

mm/yyyy

m/yyyy

mmyy

(MMYY)

The month and two digit year. The data can be handled in any
                                          						of the following formats:

mmyy

mm/yy

m/yy

mm/y

m/y

mmdd

(MMDD)

The month and day. The data can be handled in any of the
                                          						following formats:

mmdd

mm/dd

m/dd

mm/d

m/d

yyyy

(YYYY)

The four digit year alone. The data can be handled in the
                                          						following format:

yyyy

ddmm

(DDMM)

The day and month. The data can be handled in any of the
                                          						following formats:

ddmm

dd/mm

d/mm

dd/m

d/m

mm

(MM)

The month alone. The data can be handled in the following
                                          						format:

mm

## Output
                        	 Formats

Name

(Display Name)

Input Format Depends On

Description

date

(The Date)

mmddyyyy ddmmyyyy yyyymmdd

For all input formats containing the full date, this output
                                          						format plays the month name, day, and full four digit year.

date_19

(The Date w/ YY=19)

mmddyy ddmmyy

For all input formats containing the full date and a two
                                          						digit year, this plays the month name, day, and year assuming it is in the
                                          						1900s.

date_20 (The Date w/ YY=20)

mmddyy ddmmyy

For all input formats containing the full date and a two
                                          						digit year, this plays the month name, day, and year assuming it is in the
                                          						2000s.

month_year

(Month/Year)

mmyyyy

Plays the month name and full four digit year.

month_year_19

(Month/Year w/ YY=19)

mmyy

Plays the month name and year assuming it is in the 1900s.

month_year_20

(Month/Year w/ YY=20)

mmyy

Plays the month name and year assuming it is in the 2000s.

month_day

(Month/Day)

mmdd ddmm

Plays the month name and the day.

month

(Month)

mm

Plays the month name only.

year

(Year)

yyyy

Plays the full four digit year only.

## Filesets

Name

(Display Name)

Output Format Depends On

Description

standard_date

(Standard Full Date)

date date_19 date_20

This fileset contains all files needed to render the full
                                          						date. It involves fewer audio files to render the year but at the cost of
                                          						sounding a bit robotic. This directly correlates to the Unified CVP Number Say
                                          						it Smart plug-in’s standard fileset.

enhanced_date

(Enhanced Full Date)

date date_19 date_20

This fileset contains all files needed to render the full
                                          						date. This fileset involves more audio files to render a better sounding year.
                                          						This directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset.

month_standard_year

(Month/Standard Year)

month_year month_year_19 month_year_20

This fileset contains all files needed to render a month and
                                          						a year. It involves fewer audio files to render the year but at the cost of
                                          						sounding a bit robotic. This directly correlates to the Unified CVP Number Say
                                          						it Smart plug-in’s standard fileset.

month_enhanced_year

(Month/Enhanced Year)

month_year month_year_19 month_year_20

This fileset contains all files needed to render a month and
                                          						a year. This fileset involves more audio files to render a better sounding
                                          						year. This directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset.

month_day

(Month/Day)

month_day

This fileset contains all files needed to render a month and
                                          						a day.

month

(Month Only)

month

This fileset contains all files needed to render the month
                                          						alone.

standard_year (Standard Year)

year

This fileset contains all files needed to render the year
                                          						alone. It involves fewer audio files but at the cost of sounding a bit robotic.
                                          						This directly correlates to the Unified CVP Number Say it Smart plug-in’s standard fileset.

enhanced_year

(Enhanced Year)

year

This fileset contains all files needed to render the year
                                          						alone. This fileset involves more audio files to render a better sounding year.
                                          						This directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset.

## Audio Files

All filesets
                              		  including the month have a separate file for each month. All filesets with the
                              		  day of the month will have a separate file for each day ( 1st , 2nd , and so
                              		  on). Only those filesets containing the year have standard and enhanced
                              		  versions that render the year with less files or more files respectively. The
                              		  files required to render the year are almost the same as the Unified CVP Number
                              		  Say it Smart plug-in with the exception that numbers greater than 9999 are not
                              		  necessary and zero is replaced with oh .

Standard Full Date

January

February

March

April

May

June

July

August

September

October

November

December

1st

2nd

3rd

4th

5th

6th

7th

8th

9th

10th

11th

12th

13th

14th

15th

16th

17th

18th

19th

20th

21th

22nd

23rd

25th

26th

27th

28th

29th

30th

31st

oh

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

hundred

thousand

Enhanced Full Date

January

February

March

April

May

June

July

August

September

October

November

December

1st

2nd

3rd

4th

5th

6th

7th

8th

9th

10th

11th

12th

13th

14th

15th

16th

17th

18th

19th

20th

21th

22nd

23rd

25th

26th

27th

28th

29th

30th

31st

oh

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

hundred

Month/Standard Year

January

February

March

April

May

June

July

August

September

October

November

December

oh

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

hundred

thousand

Month/Enhanced Year

January

February

March

April

May

June

July

August

September

October

November

December

oh

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

hundred

Month/Day

January

February

March

April

May

June

July

August

September

October

November

December

1st

2nd

3rd

4th

5th

6th

7th

8th

9th

10th

11th

12th

13th

14th

15th

16th

17th

18th

19th

20th

21th

22nd

23rd

25th

26th

27th

28th

29th

30th

31st

Month Only

January

February

March

April

May

June

July

August

September

October

November

December

Standard Year

oh

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

hundred

thousand

Enhanced Year

oh

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

hundred

## Examples

Example #1

Data:

02171971

Input Format:

mmddyyyy

Output Format:

date

Fileset

standard_date

Playback:

"February" "17th" "19" "70" "1"

Example #2

Data:

02/09/05

Input Format:

ddmmyy

Output Format:

date_19

Fileset

enhanced_date

Playback:

"September" "2nd" "19" "oh" "5"

Example #3

Data:

072003

Input Format:

mmyyyy

Output Format:

month_year

Fileset

month_standard_year

Playback:

"July" "2" "thousand" "3"

Example #4

Data:

2387

Input Format:

yyyy

Output Format:

year

Fileset

enhanced_year

Playback:

"23" "87"

Example #5

Data:

12

Input Format:

mm

Output Format:

month

Fileset

month

Playback:

"December"

Example #6

Data:

10/10

Input Format:

mmdd

Output Format:

month_day

Fileset

month_day

Playback:

"October" "10th"

| Name (Display Name) | Description |
|---|---|
| mmddyyyy (MMDDYYYY) | The full date with the month, day, and four digit year. The
                                          						data can be handled in any of the following formats: mmddyyyy mm/dd/yyyy m/dd/yyyy mm/d/yyyy m/d/yyyy |
| mmddyy (MMDDYY) | The full date with the month, day, and two digit year. The
                                          						data can be handled in any of the following formats: mmddyy mm/dd/yy m/dd/yy mm/d/yy mm/dd/y m/d/yy m/dd/y mm/d/y m/d/y |
| ddmmyyyy (DDMMYYYY) | The full date with the day, month, and four digit year. The
                                          						data can be handled in any of the following formats: ddmmyyyy dd/mm/yyyy d/mm/yyyy dd/m/yyyy d/m/yyyy |
| ddmmyy (DDMMYY) | The full date with the day, month, and two digit year. The
                                          						data can be handled in any of the following formats: ddmmyy dd/mm/yy d/mm/yy dd/m/yy dd/mm/y d/m/yy d/mm/y dd/m/y d/m/y |
| yyyymmdd (YYYYMMDD) | The full date with the four digit year, month, and day. The
                                          						data can be handled in any of the following formats: yyyymmdd yyyy/mm/dd yyyy/m/dd yyyy/mm/d yyyy/m/d |
| mmyyyy (MMYYYY) | The month and four digit year. The data can be handled in
                                          						any of the following formats: mmyyyy mm/yyyy m/yyyy |
| mmyy (MMYY) | The month and two digit year. The data can be handled in any
                                          						of the following formats: mmyy mm/yy m/yy mm/y m/y |
| mmdd (MMDD) | The month and day. The data can be handled in any of the
                                          						following formats: mmdd mm/dd m/dd mm/d m/d |
| yyyy (YYYY) | The four digit year alone. The data can be handled in the
                                          						following format: yyyy |
| ddmm (DDMM) | The day and month. The data can be handled in any of the
                                          						following formats: ddmm dd/mm d/mm dd/m d/m |
| mm (MM) | The month alone. The data can be handled in the following
                                          						format: mm |

| Name (Display Name) | Input Format Depends On | Description |
|---|---|---|
| date (The Date) | mmddyyyy ddmmyyyy yyyymmdd | For all input formats containing the full date, this output
                                          						format plays the month name, day, and full four digit year. |
| date_19 (The Date w/ YY=19) | mmddyy ddmmyy | For all input formats containing the full date and a two
                                          						digit year, this plays the month name, day, and year assuming it is in the
                                          						1900s. |
| date_20 (The Date w/ YY=20) | mmddyy ddmmyy | For all input formats containing the full date and a two
                                          						digit year, this plays the month name, day, and year assuming it is in the
                                          						2000s. |
| month_year (Month/Year) | mmyyyy | Plays the month name and full four digit year. |
| month_year_19 (Month/Year w/ YY=19) | mmyy | Plays the month name and year assuming it is in the 1900s. |
| month_year_20 (Month/Year w/ YY=20) | mmyy | Plays the month name and year assuming it is in the 2000s. |
| month_day (Month/Day) | mmdd ddmm | Plays the month name and the day. |
| month (Month) | mm | Plays the month name only. |
| year (Year) | yyyy | Plays the full four digit year only. |

| Name (Display Name) | Output Format Depends On | Description |
|---|---|---|
| standard_date (Standard Full Date) | date date_19 date_20 | This fileset contains all files needed to render the full
                                          						date. It involves fewer audio files to render the year but at the cost of
                                          						sounding a bit robotic. This directly correlates to the Unified CVP Number Say
                                          						it Smart plug-in’s standard fileset. |
| enhanced_date (Enhanced Full Date) | date date_19 date_20 | This fileset contains all files needed to render the full
                                          						date. This fileset involves more audio files to render a better sounding year.
                                          						This directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset. |
| month_standard_year (Month/Standard Year) | month_year month_year_19 month_year_20 | This fileset contains all files needed to render a month and
                                          						a year. It involves fewer audio files to render the year but at the cost of
                                          						sounding a bit robotic. This directly correlates to the Unified CVP Number Say
                                          						it Smart plug-in’s standard fileset. |
| month_enhanced_year (Month/Enhanced Year) | month_year month_year_19 month_year_20 | This fileset contains all files needed to render a month and
                                          						a year. This fileset involves more audio files to render a better sounding
                                          						year. This directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset. |
| month_day (Month/Day) | month_day | This fileset contains all files needed to render a month and
                                          						a day. |
| month (Month Only) | month | This fileset contains all files needed to render the month
                                          						alone. |
| standard_year (Standard Year) | year | This fileset contains all files needed to render the year
                                          						alone. It involves fewer audio files but at the cost of sounding a bit robotic.
                                          						This directly correlates to the Unified CVP Number Say it Smart plug-in’s standard fileset. |
| enhanced_year (Enhanced Year) | year | This fileset contains all files needed to render the year
                                          						alone. This fileset involves more audio files to render a better sounding year.
                                          						This directly correlates to the Unified CVP Number Say It Smart plug-in’s enhanced fileset. |

| January | February | March | April | May | June | July | August | September | October | November | December |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th | 11th | 12th |
| 13th | 14th | 15th | 16th | 17th | 18th | 19th | 20th | 21th | 22nd | 23rd | 25th |
| 26th | 27th | 28th | 29th | 30th | 31st |  |  |  |  |  |  |
| oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 30 | 40 | 50 |
| 60 | 70 | 80 | 90 | hundred | thousand |  |  |  |  |  |  |

| January | February | March | April | May | June | July | August | September | October | November | December |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th | 11th | 12th |
| 13th | 14th | 15th | 16th | 17th | 18th | 19th | 20th | 21th | 22nd | 23rd | 25th |
| 26th | 27th | 28th | 29th | 30th | 31st |  |  |  |  |  |  |
| oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
| 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
| 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 |
| 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 |
| 72 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 |
| 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 |
| 95 | 96 | 97 | 98 | 99 | 100 | 200 | 300 | 400 | 500 | 600 | 700 |
| 800 | 900 | 1000 | 2000 | 3000 | 4000 | 5000 | 6000 | 7000 | 8000 | 9000 | hundred |

| January | February | March | April | May | June | July | August | September | October | November | December |
|---|---|---|---|---|---|---|---|---|---|---|---|
| oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 30 | 40 | 50 |
| 60 | 70 | 80 | 90 | hundred | thousand |  |  |  |  |  |  |

| January | February | March | April | May | June | July | August | September | October | November | December |
|---|---|---|---|---|---|---|---|---|---|---|---|
| oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
| 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
| 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 |
| 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 |
| 72 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 |
| 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 |
| 95 | 96 | 97 | 98 | 99 | 100 | 200 | 300 | 400 | 500 | 600 | 700 |
| 800 | 900 | 1000 | 2000 | 3000 | 4000 | 5000 | 6000 | 7000 | 8000 | 9000 | hundred |

| January | February | March | April | May | June | July | August | September | October | November | December |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th | 11th | 12th |
| 13th | 14th | 15th | 16th | 17th | 18th | 19th | 20th | 21th | 22nd | 23rd | 25th |
| 26th | 27th | 28th | 29th | 30th | 31st |  |  |  |  |  |  |

| January | February | March | April | May | June | July | August | September | October | November | December |
|---|---|---|---|---|---|---|---|---|---|---|---|

| oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 30 | 40 | 50 |
| 60 | 70 | 80 | 90 | hundred | thousand |  |  |  |  |  |  |

| oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
| 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
| 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 |
| 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 |
| 72 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 |
| 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 |
| 95 | 96 | 97 | 98 | 99 | 100 | 200 | 300 | 400 | 500 | 600 | 700 |
| 800 | 900 | 1000 | 2000 | 3000 | 4000 | 5000 | 6000 | 7000 | 8000 | 9000 | hundred |

| Data: | 02171971 |
|---|---|
| Input Format: | mmddyyyy |
| Output Format: | date |
| Fileset | standard_date |
| Playback: | "February" "17th" "19" "70" "1" |

| Data: | 02/09/05 |
|---|---|
| Input Format: | ddmmyy |
| Output Format: | date_19 |
| Fileset | enhanced_date |
| Playback: | "September" "2nd" "19" "oh" "5" |

| Data: | 072003 |
|---|---|
| Input Format: | mmyyyy |
| Output Format: | month_year |
| Fileset | month_standard_year |
| Playback: | "July" "2" "thousand" "3" |

| Data: | 2387 |
|---|---|
| Input Format: | yyyy |
| Output Format: | year |
| Fileset | enhanced_year |
| Playback: | "23" "87" |

| Data: | 12 |
|---|---|
| Input Format: | mm |
| Output Format: | month |
| Fileset | month |
| Playback: | "December" |

| Data: | 10/10 |
|---|---|
| Input Format: | mmdd |
| Output Format: | month_day |
| Fileset | month_day |
| Playback: | "October" "10th" |