---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-842f1b4614
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_log-collection-api_1501.html
retrieved_at: 2026-08-21T16:47:17.707561+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Log Collection API

## Chapter: Log Collection API

- Log Collection API

- Log Collection API

# Log Collection API

## Log Collection API

Use the Log Collection API to collect the log files, or  request a download of the log files in one collected zipped file.

### Operations

create : Creates one request to collect the log files, and begins collecting them.

Only one log collection may be performed at a time.

The maximum number of saved log collections is 3.

Inventory status errors must be cleared before log collection
                                       starts.

delete : Deletes one log collection.

get : Returns the log collection item, using the URL https://<server>/unifiedconfig/config/logcollection/<id> .

list : Retrieves a list of collection requests.

### Parameters

refURL: The refURL of the log collection. See Shared Parameters .

startDateTime: The start date of the logs collected.

endDateTime: The end date of the logs collected.

description: See Shared Parameters .

components: A list of components for which logs are collected. Defaults to all components if the list is blank or not provided.
                                    Possible component values include:

1: Unified Contact Center Enterprise (CCE)

2: Unified Customer Voice Portal (CVP)

3: Unified Communications Manager (CM)

4: Cisco Unified Intelligence Center (Intelligence Center)

5: Finesse

status.state: The status of the collection request: IN_PROGRESS, DONE, or ERROR.

status.apiErrors: The error indicating why the collection request failed. Returned when status.state is ERROR.

resultsFile: Zipped file containing logs collected. Includes the following parameters:

refURL: The URL of the zipped file which is used for download.

size: The size of the zipped file (in bytes).

### Example Get Response

```
<logCollection>
    <refURL>/unifiedconfig/config/logcollection/1</refURL>
     <status>
         <state>IN_PROGRESS</state>
     </status>
     <components>
          <component>1</component>
          <component>2</component>
     </components>
     <description>this is a log collection to see if ____</description>
     <startDateTime>1368564152000</startDateTime>
     <endDateTime>1368564156000</endDateTime>
     <resultsFile>
        <refUrl>/unifiedconfig/config/logcollection/(id)/log</refUrl>
        <size>450</size>
     </resultsFile>
</logCollection>
```