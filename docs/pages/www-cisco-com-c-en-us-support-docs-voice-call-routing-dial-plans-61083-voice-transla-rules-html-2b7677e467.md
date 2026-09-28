---
doc_id: www-cisco-com-c-en-us-support-docs-voice-call-routing-dial-plans-61083-voice-transla-rules-html-2b7677e467
source_url: https://www.cisco.com/c/en/us/support/docs/voice/call-routing-dial-plans/61083-voice-transla-rules.html
retrieved_at: 2026-08-20T23:24:40.275681+00:00
---

Determine Voice Translation Rules

# Determine Voice Translation Rules

### Download Options

Updated: May 29, 2026

Document ID: 61083

Contents

## Contents

## Introduction

This document describes how to determine and define voice translation rules.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The syntax used throughout this document is:

Syntax

Definition

rule precedence /match pattern/ /replacement pattern/

/ -- / delimits the whole number.

rule precedence /match pattern/ /replacement pattern/

/ -- / delimits the whole number.

## Simple Match and Replace

### Example 1

This example replaces the first occurrence of the number 123 with 456.

```
voice translation-rule 1 rule 1 /123/ /456/
```

These are test voice translation-rule examples:

```
router# test voice translation-rule 1 123 Matched with rule 1
Original number: 123    Translated number: 456

router# test voice translation-rule 1 1234 Matched with rule 1
Original number: 1234   Translated number: 4564

router# test voice translation-rule 1 6123 Matched with rule 1
Original number: 6123   Translated number: 6456
```

```
router# test voice translation-rule 1 6123123 Matched with rule 1
Original number: 6123123        Translated number: 6456123
Original number type: none      Translated number type: none
Original number plan: none      Translated number plan: none
```

In this example, the rule matches the first occurrence of the number that contains the pattern 123 anywhere in the number. Specifically, you can use the start and end of number indicators. These examples show this.

### Example 2

This example shows how to replace any occurrence of 123 at the start of a number with 456.

```
voice translation-rule 1 rule 1 /^123/ /456/
```

These aretest voice translation-rule examples.

```
router# test voice translation-rule 1 123 Matched with rule 1
Original number: 123    Translated number: 456

router# test voice translation-rule 1 1234 Matched with rule 1
Original number: 1234   Translated number: 4564

router# test voice translation-rule 1 6123 6123 Didn't match with any of rules
```

### Example 3

If you want only the match of an exact number, specify both the start and end number indicators:

```
voice translation-rule 1 rule 1 /^123$/ /456/
```

```
router# test voice translation-rule 1 123 Matched with rule 1
Original number: 123    Translated number: 456

router# test voice translation-rule 1 1234 1234 Didn't match with any of rules

router# test voice translation-rule 1 6123 6123 Didn't match with any of rules
```

## Pattern Match with Wildcards

These tables define wildcard and wildcard combinations, and show some examples.

Wildcard

Definition

.

Any single digit

0 to 9,*,#

Any specific character

[0-9]

Any range or sequence of characters

*

Modifier—match none or more occurrences

+

Modifier—match one or more occurrences

?

Modifier—match none or one occurrence

Wildcard Combination

Definition

.*

Any single character followed by none or more occurrences. This means it can match an empty string, a single character, or a sequence of many characters (except for newline character, by default).

.+

Any single character followed by one or more occurrences. Except for newline character, by default.

^$

No digits, null

### Example 1

This example replaces any five-digit number that begins with 40 with the number 6666000.

```
voice translation-rule 1 rule 1 /^40.../ /6666000/
```

```
router# test voice translation-rule 1 40123 Matched with rule 1
Original number: 40123    Translated number: 6666000
```

### Example 2

This example replaces all numbers with 5554000.

```
voice translation-rule 2 rule 1 /.*/ /5554000/
```

```
router# test voice translation-rule 2 123 Matched with rule 1
Original number: 123    Translated number: 5554000

router# test voice translation-rule 2 86573 Matched with rule 1
Original number: 86573  Translated number: 5554000

router# test voice translation-rule 2 "" Matched with rule 1
Original number:   Translated number: 5554000
```

### Example 3

This example replaces all numbers, except null, with 5554000.

```
voice translation-rule 2 rule 1 /.+/ /5554000/
```

```
router# test voice translation-rule 2 123 Matched with rule 1
Original number: 123    Translated number: 5554000

router# test voice translation-rule 2 "" Didn't match with any of rules
```

### Example 4

This example replaces any number that starts with a combination of zeros (0, 00, and so forth) with 909.

```
voice translation-rule 5 rule 1 /^0+/ /909/
```

```
router# test voice translation-rule 5 0123456 Matched with rule 1
Original number: 0123456        Translated number: 909123456

router# test voice translation-rule 5 00123456 Matched with rule 1
Original number: 00123456       Translated number: 909123456

router# test voice translation-rule 5 000123456 Matched with rule 1
Original number: 000123456      Translated number: 909123456

router# test voice translation-rule 5 123456 123456 Didn't match with any of rules
```

## Number Slice

You can use number slice when you need to copy parts of a matched number across to the replacement number. You slice the matched number into sets that you can keep or ignore.

Character

Description

\

In the match pattern, indicates where to slice up the number.

\

In the replacement pattern, indicates where to copy the sets to keep.

( )

Indicates which sets in the matched number to keep.

Character Usage

Description

(a\)

Keep expression a.

b\

Ignore expression b.

\1

Copy the first set into the replacement number.

### Generic Example

This example provides a general explanation.

```
/ ( x \) y \ ( z \) /  / w \1\2/
```

Split the matched number into three sets ofx, y, and z. The backward slash (\) indicates the places to slice up the number. The brackets () indicate which sets you want to reuse in the replacement pattern. Thew represents additional digits to insert into the replacement number.

Set 1 becomes expressionx.

Set 2 becomes expressionz.

Expressiony is ignored.

The replacement number is a concatenated number:wxz.

### Related Example

This example provides further detail:

```
voice translation-rule 1 rule 1 /^\(12\)3\(45\)$/ /6\1\2/
```

Set 1: 12

Set 2: 45

Ignore: 3

```
router# test voice translation-rule 1 12345 Matched with rule 1
Original number: 12345        Translated number: 61245
```

## Number Type and Plan

You can restrict matches to particular number or plan types. Also, you can alter the replacement plan or type.

### Example 1

In this example, if a number starts with 4 and the type is national, the rule adds 90 as a prefix. If the type is international, the rule adds 900 as the prefix.

```
voice translation-rule 7 rule 1 /^4/ /904/ type national national rule 2 /^4/ /9004/ type international international
```

```
router# test voice translation-rule 7 493456567 type national Matched with rule 1
Original number: 493456567      Translated number: 90493456567
Original number type: national  Translated number type: national
Original number plan: none      Translated number plan: none
	
router# test voice translation-rule 7 493456567 type international Matched with rule 2
Original number: 493456567              Translated number: 900493456567
Original number type: international     Translated number type: international
Original number plan: none              Translated number plan: none
```

This is useful when telephone companies (Telcos) remove access codes on national and international numbers. You can add the correct prefix with the number type as a basis.

### Example 2

This example changes the number type and plan.

```
voice translation-rule 8 rule 1 /^2\(...$\)/ /01779345\1/ type unknown national plan unknown isdn
```

This rule matches any four-digit number that starts with 2. The rule removes the 2, adds the number 01779345 as a prefix, and sets the plan to isdn and the type to national.

```
router# test voice translation-rule 8 2001 type unknown plan unknown Matched with rule 1
Original number: 2001   Translated number: 01779345001
Original number type: unknown   Translated number type: national
Original number plan: unknown   Translated number plan: isdn
```

## Reject Calls

Use thereject keyword to reject calls that match. This example rejects all calls that start with 234.

```
rule 1 reject /^234/
```

```
router# test voice translation-rule 10 1234 1234 Didn't match with any of rules

router# test voice translation-rule 10 2345 blocked on rule 1
```

## Apply Rules

Voice Translation Rules are applied to Voice Translation Profiles. These profiles are then applied to dial peers or voice ports. Profiles can be applied to VoIP or POTS dial peers or voice ports and can be applied to inbound or outbound calls. A profile can translate Called, Calling, or Redirecting numbers.

```
voice translation-rule 3 
 rule 1 /123/ /456/ 

voice translation-profile profile1
 translate calling 3 

dial-peer voice 10 pots
 translation-profile outgoing profile1
```

## Additional Examples

### Truncate Numbers Down to the Last Two Digits

```
rule 1 /^.*\(..\)/ /\1/
```

This is a number divided into one set and one ignored statement.

Ignored: ^.* None or more digits from the beginning of number

Set 1: .. two digits

The replacement statement specifies Set 1. This rule copies the last two digits of the number.

```
router# test voice translation-rule 9 12345 Matched with rule 1
Original number: 12345	Translated number: 45

router# test voice translation-rule 9 123456 Matched with rule 1
Original number: 123456	Translated number: 56
```

### Remove Unwanted Digits in a Number

This example is useful because certain Telcos have been known to insert hyphens into calling party numbers. Since this is against standards, it causes the calling party number to be ignored. The Telco sends the calling numbers in two formats, with one hyphen and sometimes with two. Two rules are required in the voice translation rule. Additionally, the first format can have five or six digit numbers after the hyphen. You can match both of these conditions with one rule with the '?' character (match none or one occurrence).

Special characters:

The hyphen character is used to indicate a range in a match pattern, for example [0-9]. To indicate in this rule that you want to match on the hyphen character, it is necessary to use the '\' character to escape its meaning. This is because the hyphen character is a special character. The '\-' characters really means hyphen. The end '\' indicates that the number is sliced here.

If you type ? directly, Cisco IOS® thinks it is a request for help. You must type Control-V then ? .

```
voice translation-rule 12
 rule 1 /^\(01...\)\-\(......?$\)/ /\1\2/ 
 rule 2 /^\(0[12]..\)\-\(...\)\-\(....$\)/ /\1\2\3/
```

Rule 1: The number is sliced into three sequences, with two sets to be kept.

Set 1: 01...

Ignore: -

Set 2: ...... or .....

Rule 2: The number is sliced into five sequences with three sets to be kept.

Set 1: 0[12]..

Ignore: -

Set 2: ...

Ignore: -

Set 3: ....

```
router# test voice translation-rule 12 "01208-333444" Matched with rule 1
Original number: 01208-333444   Translated number: 01208333444

router# test voice translation-rule 12 "01208-72345" Matched with rule 1
Original number: 01208-72345    Translated number: 0120872345

router# test voice translation-rule 12 "0161-333-4444" Matched with rule 2
Original number: 0161-333-4444  Translated number: 01613334444

router# test voice translation-rule 12 "0208-123-4567" Matched with rule 2
Original number: 0208-123-4567  Translated number: 02081234567
```

## Related Information

### Revision History

4.0

29-May-2026

Recertification

2.0

13-Nov-2023

Updated for Formatting and Spelling.

1.0

10-Aug-2004

Initial Release

### Contributed by Cisco Engineers

Cisco TAC Engineers

### Customers Also Viewed

- Configure Number Translation with Voice Translation Profiles

- Understand Matching Inbound/Outbound Dial Peers on IOS Platforms

### This Document Applies to These Products

- Call Routing / Dial Plans

| Syntax | Definition |
|---|---|
| rule precedence /match pattern/ /replacement pattern/ | / -- / delimits the whole number. |
| rule precedence /match pattern/ /replacement pattern/ | / -- / delimits the whole number. |

| Wildcard | Definition |
|---|---|
| . | Any single digit |
| 0 to 9,*,# | Any specific character |
| [0-9] | Any range or sequence of characters |
| * | Modifier—match none or more occurrences |
| + | Modifier—match one or more occurrences |
| ? | Modifier—match none or one occurrence |

| Wildcard Combination | Definition |
|---|---|
| .* | Any single character followed by none or more occurrences. This means it can match an empty string, a single character, or a sequence of many characters (except for newline character, by default). |
| .+ | Any single character followed by one or more occurrences. Except for newline character, by default. |
| ^$ | No digits, null |

| Character | Description |
|---|---|
| \ | In the match pattern, indicates where to slice up the number. |
| \ | In the replacement pattern, indicates where to copy the sets to keep. |
| ( ) | Indicates which sets in the matched number to keep. |

| Character Usage | Description |
|---|---|
| (a\) | Keep expression a. |
| b\ | Ignore expression b. |
| \1 | Copy the first set into the replacement number. |

| Revision | Publish Date | Comments |
|---|---|---|
| 4.0 | 29-May-2026 | Recertification |
| 2.0 | 13-Nov-2023 | Updated for Formatting and Spelling. |
| 1.0 | 10-Aug-2004 | Initial Release |