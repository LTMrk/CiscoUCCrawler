---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-administrat-63770fb8d0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5/ucce_b_administration-guide-for-cisco-unified12_5_chapter_01010.html
retrieved_at: 2026-08-16T20:50:12.720640+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

Updated: February 7, 2019

Chapter: Web Setup

## Chapter: Web Setup

- Web Setup

- Session                              	 Timeout

- Implementing                              	 Session Timeouts

# Web Setup

## Session
                        	 Timeout

Timeout

Description

Range
                                          					 Values

Default
                                          					 Value

Idle
                                          					 Timeout

The time
                                          					 interval for which the session remains active without any activity.

5 minutes
                                          					 to 30 minutes.

30 minutes

Absolute
                                          					 Timeout

The
                                          					 maximum time interval for which the session remains active.

Maximum
                                          					 1440 minutes (24 hours).

1440
                                          					 minutes

## Implementing
                        	 Session Timeouts

Implement the
                              		  session timeout configurations in the Web.xml file.

Step 1

Implement Idle
                                       			 Timeout using the session configuration:

Step 2

Implement
                                       			 Absolute Timeout using the session filter:

```
<filter>
           <filter-name>sessionFilter</filter-name>
           <filter-class>com.cisco.icm.websetup.filter.SessionFilter</filter-class>
           <init-param>
                              <param-name>maxPeriod</param-name>
                              <param-value>1440</param-value>
           </init-param>
</filter>
```

| Timeout | Description | Range
                                          					 Values | Default
                                          					 Value |
|---|---|---|---|
| Idle
                                          					 Timeout | The time
                                          					 interval for which the session remains active without any activity. | 5 minutes
                                          					 to 30 minutes. | 30 minutes |
| Absolute
                                          					 Timeout | The
                                          					 maximum time interval for which the session remains active. | Maximum
                                          					 1440 minutes (24 hours). | 1440
                                          					 minutes |

| Step 1 | Implement Idle
                                       			 Timeout using the session configuration: |
|---|---|
| Step 2 | Implement
                                       			 Absolute Timeout using the session filter: <filter>
           <filter-name>sessionFilter</filter-name>
           <filter-class>com.cisco.icm.websetup.filter.SessionFilter</filter-class>
           <init-param>
                              <param-name>maxPeriod</param-name>
                              <param-value>1440</param-value>
           </init-param>
</filter> |