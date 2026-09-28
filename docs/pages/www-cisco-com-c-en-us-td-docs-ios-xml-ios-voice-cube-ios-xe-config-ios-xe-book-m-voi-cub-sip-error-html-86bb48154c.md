---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cub-sip-error-html-86bb48154c
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cub-sip-error.html
retrieved_at: 2026-08-16T15:47:52.231982+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configuring SIP Error Message Pass Through

## Chapter: Configuring SIP Error Message Pass Through

# Configuring SIP Error Message Pass Through

The Configuring SIP Error Message Pass Through feature allows an error response that is received from one SIP leg to pass
                        transparently over to another SIP leg. This functionality will pass SIP error responses that are not yet supported on the
                        Cisco Unified Border Element (Cisco UBE) or will preserve the Q.850 cause code across two sip call-legs.

## Feature Information for Configuring SIP Error Message Pass Through

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Configure SIP Error Message Pass Through

Baseline Functionality

This feature allows a received error response from one SIP leg to pass transparently over to another SIP leg.

## Restrictions for Configuring SIP Error Message Pass Through

Configuring SIP error header passing in at the dial-peer level is not supported.

## Information About Configuring SIP Error Message Pass Through

SIP error responses that are not supported on the Cisco UBE include: 300—Multiple choices, 301—Moved permanently, and 485—Ambiguous.

Pre-leg SIP error responses that are not transparently passed though include:

Error Code Received

Corresponding Error Reported on the Peer Leg

400—Bad request

500—Internal Server Error

401—Unauthorized

503—Service Unavailable

406—Not acceptable

500—Internal Server Error

407—Authentication required

503—Service Unavailable

413—Request message body too large

500—Internal Server Error

414—Request URI too large

500—Internal Server Error

416—Unsupported URI scheme

500—Internal Server Error

423—Interval too brief

500—Internal Server Error

482—Loop detected

500—Internal Server Error

483—Too many hops

500—Internal Server Error

488— Not acceptable media (applicable only when the call is transcoded)

500—Internal Server Error

## How to Configure SIP Error Message Pass Through

### Configuring SIP Error Message Pass Through

Perform this task to configure the SIP Error Message Pass Through feature.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- header-passing error pass-thru

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters VoIP voice service configuration mode.

Step 4

sip

#### Example:

```
Device(config-voi-serv)# sip
```

Enters SIP configuration mode.

Step 5

header-passing error pass-thru

#### Example:

```
Device(conf-serv-sip)# header-passing error pass-thru
```

Passes received error responses from one SIP leg to pass transparently to another SIP leg.

Step 6

end

#### Example:

```
Device(conf-serv-sip)# end
```

Returns to privileged EXEC mode.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Configure SIP Error Message Pass Through | Baseline Functionality | This feature allows a received error response from one SIP leg to pass transparently over to another SIP leg. |

| Error Code Received | Corresponding Error Reported on the Peer Leg |
|---|---|
| 400—Bad request | 500—Internal Server Error |
| 401—Unauthorized | 503—Service Unavailable |
| 406—Not acceptable | 500—Internal Server Error |
| 407—Authentication required | 503—Service Unavailable |
| 413—Request message body too large | 500—Internal Server Error |
| 414—Request URI too large | 500—Internal Server Error |
| 416—Unsupported URI scheme | 500—Internal Server Error |
| 423—Interval too brief | 500—Internal Server Error |
| 482—Loop detected | 500—Internal Server Error |
| 483—Too many hops | 500—Internal Server Error |
| 488— Not acceptable media (applicable only when the call is transcoded) | 500—Internal Server Error |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters VoIP voice service configuration mode. |
| Step 4 | sip Example: Device(config-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | header-passing error pass-thru Example: Device(conf-serv-sip)# header-passing error pass-thru | Passes received error responses from one SIP leg to pass transparently to another SIP leg. |
| Step 6 | end Example: Device(conf-serv-sip)# end | Returns to privileged EXEC mode. |