---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-book-parameters-reference-guide-for-cisco-jabber-14-0-cjab--d7c720d1d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_book_parameters-reference-guide-for-cisco-jabber-14_0/cjab_b_parameter-reference-guide-jabber-129_chapter_01010.html
retrieved_at: 2026-08-21T21:03:22.339027+00:00
---

Parameters Reference Guide for Cisco Jabber 14.0

# Parameters Reference Guide for Cisco Jabber 14.0

Updated: March 29, 2021

Chapter: Cisco Unified Communications Manager

## Chapter: Cisco Unified Communications Manager

# Cisco Unified Communications Manager

## Audio_Start_Port_Range and Audio_End_Port_Range

Specifies the port range for Jabber audio. The following rules apply when selecting the range:

The allowed values are 2048-65535.

The minimum number of ports in the range is two.

Select an even number for Audio_Start_Port_Range .

Select an odd number for Audio_End_Port_Range .

The audio port range can’t overlap either the video port range or the Far-End Camera Control (FECC) port range.

Example:

```
<Audio_Start_Port_Range>2068</Audio_Start_Port_Range>
<Audio_End_Port_Range>2071</Audio_End_Port_Range>
```

## Fecc_Start_Port_Range and Fecc_End_Port_Range

Specifies the port range for Far-End Camera Control (FECC). The following rules apply when selecting the range:

The minimum number of ports in the range is two.

Select an even number for Fecc_Start_Port_Range with a default of 30000.

Select an odd number for Fecc_End_Port_Range with a default of 39999.

The Far-End Camera Control (FECC) port range can’t overlap either the audio port range or the video port range.

Example:

```
<Fecc_Start_Port_Range>30010</Fecc_Start_Port_Range>
<Fecc_End_Port_Range>30013</Fecc_End_Port_Range>
```

## Video_Start_Port_Range and Video_End_Port_Range

Specifies the port range for Jabber video. The following rules apply when selecting the range:

The allowed values are 2048-65535.

The minimum number of ports in the range is four.

Select an even number for Video_Start_Port_Range .

Select an odd number for Video_End_Port_Range .

The video port range can’t overlap either the audio port range or the Far-End Camera Control (FECC) port range.

Example:

```
<Video_Start_Port_Range>2048</Video_Start_Port_Range>
<Video_End_Port_Range>2053</Video_End_Port_Range>
```