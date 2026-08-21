---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-user-guide-ccvp-b-62c83179cd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/user/guide/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_01011.html
retrieved_at: 2026-08-21T03:09:08.214631+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: February 2, 2020

Chapter: State

## Chapter: State

# State

Plugin
                                    Name:

state

Display Name:

U.S./Canada State

Class Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmartState

## Description

This Say It Smart type handles the reading of a U.S. or Canadian state,
                           territory, or province. The data is passed as the two-letter abbreviation of
                           the state and the plug-in plays back the full name. Please see the Audio Files
                           section to see a list of U.S. and Canadian states, territories, and provinces.

## Input
                        	 Formats

Name

(Display Name)

Description

state_abbreviation

(2-Character Abbreviation)

A two letter abbreviation of the state (case insensitive).

## Output Formats

Name

(Display Name)

Input Format
                                             Depends On

Description

state_name

(Full State Name)

state_abbreviation

An audio file playing the full state, territory, or
                                          province name.

## Filesets

Name

(Display
                                             Name)

Output Format
                                             Depends On

Description

standard

(Standard)

state_name

There is only one fileset: a separate audio file for each U.S. or
                                          Canadian state, territory or province.

## Audio Files

The filenames are as
                              		  shown (no spaces in the names). The two-letter abbreviation for each state,
                              		  territory, or province is listed in parentheses.

U.S. Territories

american_samoa
                                          				  (AS)

federated_states_of_micronesia (FM)

guam (GU)

marshall_islands (MH)

northern_mariana_islands (MP)

puerto_rico
                                          				  (PR)

us_virgin_islands (VI)

palau (PW)

U.S. States

alabama (AL)

alaska (AK)

arizona (AZ)

arkansas (AR)

california (CA)

colorado (CO)

connecticut (CT)

delaware (DE)

district_of_columbia (DC)

florida (FL)

georgia (GA)

hawaii (HI

idaho (ID)

illinois (IL)

indiana (IN)

iowa (IA)

kansas (KS)

kentucky (KY)

louisiana (LA)

maine (ME)

maryland (MD)

massachusetts (MA)

michigan (MI)

minnesota (MN)

mississippi (MS)

missouri (MO)

montana (MT)

nebraska (NE)

nevada (NV)

new_hampshire (NH)

new_jersey (NJ)

new_mexico (NM)

new_york (NY)

north_carolina (NC)

north_dakota (ND)

ohio (OH)

oklahoma (OK)

oregon (OR)

pennsylvania (PA)

rhode_island (RI)

south_carolina (SC)

south_dakota (SD)

tennessee (TN)

texas (TX)

utah (UT)

vermont (VT)

virginia (VA)

washington (WA)

west_virginia (WV)

wisconsin (WI)

wyoming (WY)

Canadian
                                 			 Provinces/Territories

alberta (AB)

british_columbia (BC)

manitoba (MB)

new_brunswick
                                          				  (NB)

newfoundland
                                          				  (NL)

nova_scotia
                                          				  (NS)

northwest_territories (NT)

nunavut (NU)

ontario (ON)

prince_edward (PE)

quebec (QC)

sasketchewan
                                          				  (SK)

yukon (YT)

## Examples

Example #1 (shows
                              		  case is not important)

Data:

nY

Input Format:

state_abbreviation

Output Format:

state_name

Fileset

standard

Playback:

"new_york"

Example #2

Data:

SK

Input Format:

state_abbreviation

Output Format:

state_name

Fileset

standard

Playback:

"sasketchewan"

| Plugin
                                    Name: | state |
|---|---|
| Display Name: | U.S./Canada State |
| Class Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmartState |

| Note | When the VoiceXML is produced, the TTS transcript will be exactly
                                    the same as the audio filename except without any
                                    underscores. |
|---|---|

| Name (Display Name) | Description |
|---|---|
| state_abbreviation (2-Character Abbreviation) | A two letter abbreviation of the state (case insensitive). |

| Name (Display Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| state_name (Full State Name) | state_abbreviation | An audio file playing the full state, territory, or
                                          province name. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| standard (Standard) | state_name | There is only one fileset: a separate audio file for each U.S. or
                                          Canadian state, territory or province. |

| american_samoa
                                          				  (AS) | federated_states_of_micronesia (FM) | guam (GU) |
|---|---|---|
| marshall_islands (MH) | northern_mariana_islands (MP) | puerto_rico
                                          				  (PR) |
| us_virgin_islands (VI) | palau (PW) |  |

| alabama (AL) | alaska (AK) | arizona (AZ) | arkansas (AR) |
|---|---|---|---|
| california (CA) | colorado (CO) | connecticut (CT) | delaware (DE) |
| district_of_columbia (DC) | florida (FL) | georgia (GA) | hawaii (HI |
| idaho (ID) | illinois (IL) | indiana (IN) | iowa (IA) |
| kansas (KS) | kentucky (KY) | louisiana (LA) | maine (ME) |
| maryland (MD) | massachusetts (MA) | michigan (MI) | minnesota (MN) |
| mississippi (MS) | missouri (MO) | montana (MT) | nebraska (NE) |
| nevada (NV) | new_hampshire (NH) | new_jersey (NJ) | new_mexico (NM) |
| new_york (NY) | north_carolina (NC) | north_dakota (ND) | ohio (OH) |
| oklahoma (OK) | oregon (OR) | pennsylvania (PA) | rhode_island (RI) |
| south_carolina (SC) | south_dakota (SD) | tennessee (TN) | texas (TX) |
| utah (UT) | vermont (VT) | virginia (VA) | washington (WA) |
| west_virginia (WV) | wisconsin (WI) | wyoming (WY) |  |

| alberta (AB) | british_columbia (BC) | manitoba (MB) | new_brunswick
                                          				  (NB) |
|---|---|---|---|
| newfoundland
                                          				  (NL) | nova_scotia
                                          				  (NS) | northwest_territories (NT) | nunavut (NU) |
| ontario (ON) | prince_edward (PE) | quebec (QC) | sasketchewan
                                          				  (SK) |
| yukon (YT) |  |  |  |

| Data: | nY |
|---|---|
| Input Format: | state_abbreviation |
| Output Format: | state_name |
| Fileset | standard |
| Playback: | "new_york" |

| Data: | SK |
|---|---|
| Input Format: | state_abbreviation |
| Output Format: | state_name |
| Fileset | standard |
| Playback: | "sasketchewan" |