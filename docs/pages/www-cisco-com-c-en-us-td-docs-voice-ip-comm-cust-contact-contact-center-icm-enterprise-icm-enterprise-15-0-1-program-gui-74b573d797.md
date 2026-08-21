---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-74b573d797
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_cvp-dnis-api_1501.html
retrieved_at: 2026-08-21T16:46:02.154031+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: CVP DNIS API

## Chapter: CVP DNIS API

- CVP DNIS API

- CVP Dialed Number Identification Service API

# CVP DNIS API

## CVP Dialed Number Identification Service API

Use the CVP DNIS API to retrieve and update the DNIS number in the CVP call server.

### URL

### Operations

Retrieves the CVP DNIS list of a single CVP call server. To retrieve the DNIS list, enter the hostname of the CVP call server
                                    in the URL https://<server>:<serverport>/unifiedconfig/config/deviceconfig/cvpdnis?hostname=<hostname>

Hostname is a mandatory parameter in the Get URL.

Updates the CVP DNIS list of a single CVP call server. To update the DNIS list, enter the hostname of the CVP call server
                                    in the payload. https://<server>:<serverport>/unifiedconfig/config/deviceconfig/cvpdnis

### Parameters

hostname: Indicates the CVP hostname as defined in the PCCE inventory

dnisList: Indicates the semi-colon separated list of DNIS numbers. Enter a DNIS number or DNIS range.

The length of each DNIS in this list can be up to 32 characters. DNIS must be a positive integer; DNIS can begin with a zero
                                    (0).

DNIS range is 1- 32 characters. The upper and lower limit of the DNIS range must be of the same length. For example, a range
                                    from 100 - 900 is valid because each number is three characters in length.

### Example Get Response

```
<cvpDnis>
    <hostname>cvp1a.berlin.icm</hostname>
    <dnisList>12312355;12412455</dnisList>
</cvpDnis>
```

### Responses

Success : 200 OK. The DNIS number was successfully updated in the CVP call server.

Errors : Errors indicate that the validation has failed. Check the error messages to enter the correct hostname or dnisList.

| Note | Hostname is a mandatory parameter in the Get URL. |
|---|---|