---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-222147-download-call-recordings-through-api-wit--61107c614c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/222147-download-call-recordings-through-api-wit.html
retrieved_at: 2026-08-20T23:21:40.474758+00:00
---

Download Call Recordings through API with Webex as the Provider

# Download Call Recordings through API with Webex as the Provider

### Download Options

Updated: July 18, 2024

Document ID: 222147

Contents

## Contents

## Introduction

This document describes how administrators with Compliance Officer role can download individual call recordings for Virtual Lines and Users with API.

## Prerequisites

### Requirements

- Admin access in Control Hub.

- Compliance Officer role.

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Calling.

- Webex Calling APIs.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

### Background Information

In Webex Calling, you can have the option to use Webex as the recording provider for call recordings. This allows you to easily record and store your calls within the Webex platform.

Only administrators with Compliance Officer role can download and permanently delete recordings via API.

This next example explains the steps to download a call recording via API method using the developer documentation Converged Recordings .

Note : For advanced searches or encounter any issues, contact developer support at Developer Support for Webex .

## Steps to Download a Call Recording

Step 1. Log in to the Webex Developer Portal with your administrator credentials and search for Converged Recordings .

Select the Converged Recordings Option

Step 2.From the Method list, select the GET request List Recordings for Compliance officer .

List Recordings for Compliance Officer Option

Step 3.In the Query Parameters section, enter the parameters for your search and click on the Run button to execute the request.

Query Parameters and Run Button

Note : Use the information on the right pane to get more details of each field, for example, the locationId can be obtained from the Webex Control Hub - Locations section.

Step 4. The response displays in the Response box. Each individual recording is listed within curly braces {} , with the id attribute representing the recordingId . Copy the results to a text file for reference.

Response Box Elements

{
  "items": [
    {
      " id ": " 00060000-0300-0b00-0500-ab0000000000 ",
      "topic": "Call with +000000000000-20240625 1916",
      "createTime": "2024-06-25T19:16:41Z",
      "timeRecorded": "2024-06-25T19:15:48Z",
      "ownerId": "0000000d-0000-0000-0000-00000000000d",
      "ownerType": "virtualLine",
      "format": "MP3",
      "durationSeconds": 40,
      "sizeBytes": 122419,
      "serviceType": "calling",
      "storageRegion": "US",
      "status": "available",
      "serviceData": {
        "locationId": "eeeeeeeee-xxxx-0000-eeee-000000000000",
        "callSessionId": "00000000-xxxx-0000-0000-00000000000"
      }
    },
    {
      " id ": " 0005n000-0400-0c00-05600-cd0000000000 ",
      "topic": "Call with +000000000000-20240625 1914",
      "createTime": "2024-06-25T19:14:20Z",
      "timeRecorded": "2024-06-25T19:13:45Z",
      "ownerId": "0000000c-0000-0000-0000-00000000000e",
      "ownerType": "virtualLine",
      "format": "MP3",
      "durationSeconds": 15,
      "sizeBytes": 49195,
      "serviceType": "calling",
      "storageRegion": "US",
      "status": "available",
      "serviceData": {
        "locationId": "eeeeeeeee-xxxx-0000-eeee-000000000000",
        "callSessionId": "00000000-xxxx-0000-0000-0000000000x"
      }

Step 5. To download a specific recording, go back to the method list and select the GET request, Get Recording Details .

Get Recording Details.

Step 6. In the GET URL, replace recordingId with the actual id of the recording you want to download. Then click on the Run button to execute the request.

Click on the recordingId Button.

Recording Id and Run Button

Step 7. The Response box contains the results of your search. Copy the output to a text file and identify the audioDownloadLink attribute.

{
  "id": "0005n000-0400-0c00-05600-cd0000000000",
  "topic": "Call with +000000000000-20240625 1914",
  "createTime": "2024-06-25T19:14:20Z",
  "timeRecorded": "2024-06-25T19:13:45Z",
  "temporaryDirectDownloadLinks": {
    " audioDownloadLink ": " url-xxxxx ",
    "expiration": "2024-06-25T23:18:11Z"
  },
  "ownerId": "000000000-0000-0000-xxxx-000000xxxxxx",
  "ownerType": "virtualLine",
  "format": "MP3",
  "durationSeconds": 15,
  "sizeBytes": 49195,
  "serviceType": "calling",
  "storageRegion": "US",
  "status": "available",
  "serviceData": {
    "locationId": "eeeeeeeee-xxxx-0000-eeee-000000000000",
    "callSessionId": "xxxxxxxx-0000-0000-xxxx-0000xxxxxxxx"
  }
}

Step 8. Copy the entire URL that is under audioDownloadLink and paste it into a web browser. Make sure to include all characters between the quotation marks. Press Enter to initiate the download. The recording downloads to your machine as an MP3 file.

MP3 File Downloads

Note : Contact Webex Developer Support for questions and issues related to API at Developer Support for Webex .

## Related Information

- Ensure Regulatory Compliance of Webex Calling Content

- Manage call recording for Webex Calling

### Revision History

1.0

19-Jul-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Jul-2024 | Initial Release |