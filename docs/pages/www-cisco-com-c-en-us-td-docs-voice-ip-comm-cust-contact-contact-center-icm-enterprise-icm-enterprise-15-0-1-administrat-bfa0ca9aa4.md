---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-administrat-bfa0ca9aa4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/administration/guide/ucce_b_150_administration-guide-for-cisco-unified-contact-center-enterprise/ucce_m_150_web-setup.html
retrieved_at: 2026-08-16T20:44:47.426597+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

# Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

Updated: July 31, 2026

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