---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-993425b8a2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/ucce_b_cisco-ucce_developer_guide-12_6_1_chapter_0111.html
retrieved_at: 2026-08-16T20:22:03.501934+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

Updated: August 21, 2023

Chapter: Bucket Interval API

## Chapter: Bucket Interval API

- Bucket Interval API

- Bucket Interval                              	 API

# Bucket Interval API

## Bucket Interval
                        	 API

Configure bucket
                           		intervals to report how many calls are handled or abandoned during specific,
                           		incremental time slots. Each bucket interval has a maximum of nine configurable
                           		time slots, called Upper Bounds. Upper Bounds are ranges measured in seconds to
                           		segment and capture call-handling activity. You can run reports that show calls
                           		answered and calls abandoned for these intervals.

Use the Bucket
                           		Intervals API to add new bucket intervals, edit the name of an existing bucket
                           		interval, get a list of all of the configured bucket intervals, and delete
                           		existing bucket intervals.

### URL

### Operations

create :
                                    				Creates one bucket interval.

delete :
                                    				Deletes one bucket interval from the database.

get :
                                    				Returns one bucket interval, using the URL https://<server>/unifiedconfig/config/bucketinterval/<id> .

list :
                                    				Retrieves a list of bucket intervals.

update :
                                    				Updates the name of one bucket interval.

### Parameters

refURL: The
                                    				refURL of the bucket interval. See Shared Parameters .

name: The name
                                    				of the bucket interval. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

upperBound1:
                                    				Required. The first Bucket Interval value, in seconds. Must be greater than 0.
                                    				This parameter cannot be updated.

upperBound2 to
                                    				upperBound 9: Optional. The next Bucket Interval values, in seconds. Each must
                                    				be greater than the previous upperBound field or be left blank (if blank, all
                                    				remaining upperBound fields must also be blank). These parameters cannot be
                                    				updated.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- name

- name (default)

- upperBound 1-9

See Search and Sort .

### Example Get
                              		  Response

```
<bucketInterval>
    <refURL>/unified/config/bucketInterval/(id)</refURL>
    <name>test</name>
    
    <upperBound1>10</upperBound1>
    <upperBound2>20</upperBound2>
    <upperBound3>30</upperBound3>
    <upperBound4>40</upperBound4>
    <upperBound5>50</upperBound5>
    <upperBound6>60</upperBound6>
    <upperBound7>70</upperBound7>
    <upperBound8>80</upperBound8>
    <upperBound9>90</upperBound9>
    <changeStamp>0</changeStamp>
</bucketInterval>
```

| Search parameters | Sort parameters |
|---|---|
| name | name (default) upperBound 1-9 |