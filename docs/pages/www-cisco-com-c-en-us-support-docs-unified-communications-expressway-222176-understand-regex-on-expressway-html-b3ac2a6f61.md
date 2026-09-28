---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-222176-understand-regex-on-expressway-html-b3ac2a6f61
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/222176-understand-regex-on-expressway.html
retrieved_at: 2026-08-16T15:41:54.682412+00:00
---

Understand Regex on Expressway

# Understand Regex on Expressway

### Download Options

Updated: July 22, 2024

Document ID: 222176

Contents

## Contents

## Introduction

This document describes how regular expressions (regex) work and how to test them in expressway servers.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Video Communications Server (VCS) and Expressway Servers

- Telepresence Devices

- Business to Business (B2B) Calling

- Collaboration Deployments

### Components Used

The information in this document is based on these software and hardware versions:

- Expressway x15

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

### Background Information

Regular expressions are sequences of characters that define patterns used to match strings in text. These strings can then be modified or preserved on search rules or transforms, these are the most common uses for regular expressions.

## Types of Regular Expressions

### Basic Expressions

- Dot (.) Matches any single character.

- Digit (\d) Matches any single decimal digit.

- Asterisk (*) Matches 0 or more repetitions of the previous character or expression.

- Plus sign (+) Matches 1 or more repetitions of the previous character or expression.

- Question Mark (?) Matches 0 or 1 repetition of the previous character or expression.

- Curly brace {n} Matches n repetitions of the previous character or expression, for example, (\d{3}) matches any 3 digit string.

- Curly brace range {n,m} Matches n to m repetitions of the previous character or expression, for example, (\d{3,5}) matches any 3, 4 or 5 digit string.

- To specify a range, use the hyphen (-) character between the start and end of the range, for example, [a-z] matches any alphabetical character.

- The use of caret (^) after the open bracket inverts the match, for example, [^a-z] matches any non-alphabetical character.

- Parentheses (...) Groups a set of matching characters. These groups can later be referenced in order using the characters \n as part of a replace string.

- Pipe (|) Matches against one or an alternate expression, for example, (com|net) matches either of the strings com or net.

### Other Expressions

- (?!...) This is a negative look ahead. Defines a sub-expression that must not be present.

- %localdomains% Matches all SIP domains currently configured on the server.

## Create and Test Patterns

The Expressway servers provide a tool to test patterns without changes to the configuration to avoid possible business impact when creating new items.

This tool can be found on the web interface of the Expressway server, navigate to Maintenance > Tools > Check Pattern .

Check Pattern Tool

- Alias: The string to test, it can be the destination or registration Uniform Resource Identifier (URI). This string is compared against the pattern string to test for a match.

- Exact: The entire string must exactly match the alias character for character.

- Prefix: The string must appear at the beginning of the alias.

- Suffix: The string must appear at the end of the alias.

- Regex: The string is treated as a regular expression.

- Pattern string: The pattern against which the alias is compared.

- Strip: Removes the matching prefix or suffix from the alias. Only available when pattern type is set to prefix or suffix.

- Leave: No modification is applied to the alias.

- Replace: Substitutes the matching part of the alias with the text in the replace string.

- Add Prefix: Prepends the additional text to the alias.

- Add Suffix: Appends the additional text to the alias.

## Commonly Used Regex Examples

### Match Everything Wildcard

This pattern is widely used when no specific pattern match is required but a search rule or transform needs to be considered, the regular expression (.*) matches any input regardless of format or length. The dot matches any character, and the asterisk is any amount of repetitions of that expression.

Match Everything Wildcard Example 1

The same pattern succeeds regardless of the alias input.

Match Everything Wildcard Example 2

### Match Local and Non-Local Domains

This is commonly used for matching a pattern with a destination of one of the local domains configured on the server and keep the call locally routed instead of routing it to the internet. The regex %localdomains% can be used as a suffix or as the second part of the regex pattern.

To configure local domains, navigate to Configuration > Domains .

Locally Configured Domains

The pattern match fails for any domain other than the ones configured locally.

Local Domains Match Failure

And it succeeds for any locally configured domains.

Local Domains Match Success

The negative look ahead of this pattern (?!.*@%localdomains%) can also be used for the opposite result. This means any alias that is not the local domains is a successful match.

Negative Lookahead for Local Domains

### Match Different Domain Extensions

This pattern is commonly used when the company owns a domain with multiple extensions and allows either one to be called, but for call management, these need to be normalized before considering search rules.

This is usually accomplished through transforms with the use of the pipe (|) regular expression.

Different Domain Extension Example 1

The same pattern matches the domain with either of the two domain extensions but converts it to the normalized extension chosen as a result.

Different Domain Extension Example 2

### Match Toll Fraud Patterns

The commonality among toll fraud calls often resides in the amount of digits dialed, international calls require a country code followed by the phone number being called, which causes these calls to have at least 7 digits. It is also common for internal dial plans within companies to be around 4 to 6 digits long.

This creates a clear difference that can be used to take different actions for either of these types of calls. Using the digit count regex, you can specify what action to take with each call.

Digit Count Example 1

This pattern matches any alias between 7 and 15 digits only. Fewer digits do not result in a match.

Digit Count Example 2

Any other character besides digits also results in a failure.

Digit Count Example 3

## Groups and Reference Patterns

Groups and references are used along with regex patterns to modify some sections of an alias while preserving others, this is useful when adding or removing prefixes or modifying domains. Groups are designated on the pattern string section, and the references are done by order in the replace string field.

Groups and References Example 1

In this example, there is a literal match with @cisco.com and the testuri string is matched and grouped by the match all regex.

The \1 reference in the replace string calls back the first group inside the pattern string, which links to the URI, regardless of what the URI is, and therefore the URI is conserved in the result alias.

The domain is not referenced in the replaced string, instead it is replaced by internaldomain, this can be seen in the result alias.

Groups can also be used to reorder the URI as this allows for flexible dial plans.

Groups and References Example 2

In this example, there is an alias with the format of 5 digits, followed by a dot and another digit, followed then by the domain.

In the pattern string, there are different groups and sections that can be analyzed separately.

- Group 1, the pattern (\d{5}) matches any 5 digits at the start of the string.

- The regular expression (\.) matches a literal dot, this means that the original alias requires a dot after the 5 initial digits.

- Group 2, the pattern (\d) matches a single digit.

- Group 3, the literal pattern (@cisco.com) matches only that sequence of characters, this can be further modified to include multiple domains, or any string after the previous matches.

Once the alias matches the pattern string, the action causes it to be replaced by the replace string.

The replace string references the previous groups in a new order.

- The reference \2 calls back group 2, this is the single digit after the dot and before the domain.

- The reference \1 calls back group 1, this is the first 5 digits of the alias.

- The reference \3 calls back group 3, this is the domain section of the alias

- The dot is never referenced nor is it part of any group, therefore is not part of the result alias.

The alias then results in the same digits as the original alias but with the digit that was originally after the dot, at the beginning of the alias.

The dot that separated the 5 digits and the single digit, is no longer part of the alias, the domain is preserved.

Not every group needs to be referenced, a group that is not referenced is not part of the result alias.

## Related Information

Cisco Technical Support & Downloads

### Revision History

1.0

23-Jul-2024

Initial Release

### Contributed by Cisco Engineers

Randy Eduardo Valverde Rojas

Technical Consulting Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Jul-2024 | Initial Release |