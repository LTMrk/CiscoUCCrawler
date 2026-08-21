---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-cdrdef-cucm-b-cdr-admin-guide-1251-cucm-b-cdr-admin-guid-1551a1e1d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/cdrdef/cucm_b_cdr-admin-guide-1251/cucm_b_cdr-admin-guide-1251_chapter_01001.html
retrieved_at: 2026-08-21T01:38:40.193525+00:00
---

Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Call Detail Records Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: Cisco Call Management Records K-Factor Data

## Chapter: Cisco Call Management Records K-Factor Data

- Cisco Call Management Records K-Factor Data

- K-Factor Data

# Cisco Call Management Records K-Factor Data

This chapter provides information about the K-factor data that is present in
                           		  the Cisco call management records (CMRs).

## K-Factor Data

K-factor represents an endpoint mean opinion score (MOS) estimation algorithm that is defined in ITU standard P.VTQ. It represents
                              a general estimator that is used to estimate the mean value of a perceptual evaluation of speech quality (PESQ) population
                              for a specific impairment pattern.

MOS relates to the output of a well designed listening experiment. All MOS experiments use a five-point PESQ scale as defined
                              in ITU standard P.862.1, which describes the PESQ as an objective method for end-to-end speech quality assessment of narrow-band
                              telephone networks and speech codecs.

The MOS estimate provides a number that is inversely proportional to frame loss density. Clarity decreases as more frames
                              are lost or discarded at the receiving end. Consider the loss or discarding of these frames as concealment. Concealment statistics
                              measure packet (frame) loss and its effect on voice quality in an impaired network.

K-factor represents a weighted estimate of average user annoyance due to distortions that are caused by effective packet loss
                              such as dropouts and warbles. It does not estimate the impact of delay-related impairments such as echo. It provides an estimate
                              of listening quality (MOS-LQO) rather than conversational quality (MOS-CQO), and measurements of average user annoyance range
                              from 1 (poor voice quality) to 5 (very good voice quality).

K-factor gets trained or conditioned by speech samples from numerous speech databases, where each training sentence or network
                              condition that is associated with a P.862.1 value has a duration of 8 seconds. For more accurate scores, the system generates
                              k-factor estimates for every 8 seconds of active speech.

Consider K-factor and other MOS estimators to be secondary or derived statistics because they warn a network operator of frame
                              loss only after the problem becomes significant. Packet counts, concealment ratios, and concealment second counters represent
                              primary statistics because they alert the network operator before network impairment has an audible impact or is visible through
                              MOS.

The following table displays the K-factor date that is stored in the Unified Communications Manager CMRs.

Field Name

Phone Display Name

D&I User Interface Text and Description

CCR

Cum Conceal Ratio

Cumulative Conceal Ratio represents the cumulative ratio of concealment time over speech time that is observed after starting
                                          a call.

ICR

Interval Conceal Ratio

Interval Conceal Ratio represents an interval-based average concealment rate that is the ratio of concealment time over speech
                                          time for the last 3 seconds of active speech.

ICRmx

Max Conceal Ratio

Interval Conceal Ratio Max represents the maximum concealment ratio that is observed during the call.

CS

Conceal Secs

Conceal Secs represents the time during which some concealment is observed during a call.

SCS

Severely Conceal Secs

Severely Conceal Secs represents the time during which a significant amount of concealment is observed. If the concealment
                                          that is observed is usually greater than 50 milliseconds or approximately 5 percent, the speech probably does not seem very
                                          audible.

MLQK

MOS LQK

MOS Listening Quality K-factor provides an estimate of the MOS score of the last 8 seconds of speech on the reception signal
                                          path.

MLQKmn

Min MOS LQK

MOS Listening Quality K-factor Min represents the minimum score that is observed since the beginning of a call and represents
                                          the worst sounding 8-second interval.

MLQKmx

Max MOS LQK

MOS Listening Quality K-factor Max represents the maximum score that is observed since the beginning of a call and represents
                                          the best sounding 8-second interval.

MLQKav

Avg MOS LQK

MOS Listening Quality K-factor Avg8 represents the running average of scores that are observed since the beginning of a call.

| Field Name | Phone Display Name | D&I User Interface Text and Description |
|---|---|---|
| CCR | Cum Conceal Ratio | Cumulative Conceal Ratio represents the cumulative ratio of concealment time over speech time that is observed after starting
                                          a call. |
| ICR | Interval Conceal Ratio | Interval Conceal Ratio represents an interval-based average concealment rate that is the ratio of concealment time over speech
                                          time for the last 3 seconds of active speech. |
| ICRmx | Max Conceal Ratio | Interval Conceal Ratio Max represents the maximum concealment ratio that is observed during the call. |
| CS | Conceal Secs | Conceal Secs represents the time during which some concealment is observed during a call. |
| SCS | Severely Conceal Secs | Severely Conceal Secs represents the time during which a significant amount of concealment is observed. If the concealment
                                          that is observed is usually greater than 50 milliseconds or approximately 5 percent, the speech probably does not seem very
                                          audible. |
| MLQK | MOS LQK | MOS Listening Quality K-factor provides an estimate of the MOS score of the last 8 seconds of speech on the reception signal
                                          path. |
| MLQKmn | Min MOS LQK | MOS Listening Quality K-factor Min represents the minimum score that is observed since the beginning of a call and represents
                                          the worst sounding 8-second interval. |
| MLQKmx | Max MOS LQK | MOS Listening Quality K-factor Max represents the maximum score that is observed since the beginning of a call and represents
                                          the best sounding 8-second interval. |
| MLQKav | Avg MOS LQK | MOS Listening Quality K-factor Avg8 represents the running average of scores that are observed since the beginning of a call. |