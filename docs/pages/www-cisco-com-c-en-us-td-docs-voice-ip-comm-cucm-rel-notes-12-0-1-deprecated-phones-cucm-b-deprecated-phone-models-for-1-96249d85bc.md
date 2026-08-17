---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-12-0-1-deprecated-phones-cucm-b-deprecated-phone-models-for-1-96249d85bc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_0_1/deprecated_phones/cucm_b_deprecated-phone-models-for-1201.html
retrieved_at: 2026-08-17T02:04:07.099949+00:00
---

Deprecated Phone Models for Cisco Unified Communications Manager, Release 12.0(x)

# Deprecated Phone Models for Cisco Unified Communications Manager, Release 12.0(x)

### Download Options

Updated: February 21, 2020

# Deprecated Phone Models for 12.0(x)

## Cisco Unified Communications Manager Release 12.0(x) does not support some deprecated phone models

THIS ADVISORY IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY
                     OF MERCHANTABILITY. YOUR USE OF THE INFORMATION OR MATERIALS LINKED FROM THE ADVISORY IS AT YOUR OWN RISK. CISCO RESERVES
                     THE RIGHT TO CHANGE OR UPDATE THIS ADVISORY AT ANY TIME.

### Products Affected

Products Affected

Version

Cisco Unified Communications Manager

12.0(x)

Cisco Business Edition 6000

12.0(x)

Cisco Business Edition 7000

12.0(x)

### Problem Description

The following phone models are deprecated and are not supported by Cisco Unified Communications Manager, Release 12.0(x).
                     If you are using any of these phone models and you upgrade to Release 12.0(x), you will be unable to use the phone after the
                     upgrade. After you switch over to the new release, registration on the phone will be blocked.

The following phone models are newly deprecated as of the 12.0(x) release:

Cisco Unified Wireless IP Phone 7921

Cisco Unified IP Phone 7970

Cisco Unified IP Phone 7971

The following phone models were first deprecated in the 11.5(x) release. That deprecation status carries over to the 12.0(x)
                     release:

Cisco IP Phone 12 S

Cisco IP Phone 12 SP

Cisco IP Phone 12 SP+

Cisco IP Phone 30 SP+

Cisco IP Phone 30 VIP

Cisco Unified IP Phone 7902G

Cisco Unified IP Phone 7905G

Cisco Unified IP Phone 7910

Cisco Unified IP Phone 7910G

Cisco Unified IP Phone 7910+SW

Cisco Unified IP Phone 7910G+SW

Cisco Unified IP Phone 7912G

Cisco Unified Wireless IP Phone 7920

Cisco Unified IP Conference Station 7935

### Background

The legacy phone models are deprecated for the following reasons:

Security—since legacy phone models are not updated with critical software fixes, we have limited ability to protect customers
                           when security issues arise.

New feature implementation—legacy phone usage slows down implementation of newer features.

Sustaining—no development support or regression testing is currently being done for these older phones.

### Problem / Symptom

If you are running any of these phone models, after you upgrade and switch over to the new release, registration will be blocked
                     on the phone. If the phone remains powered on, the phone will make repeated registration attempts, which will create unnecessary
                     network traffic as well as a load on the Cisco CallManager service.

### Upgrades that Involve Deprecated Phones

To guarantee that you have full support, before you upgrade, do the following:

Confirm whether the phones in your network will be supported in Release 12.0(x).

Identify any non-supported phones.

For  any non-supported phones, power down the phone and disconnect the phone from the network.

Provision a supported phone for the phone user. You can use the Migration FX tool to migrate from older model to newer model
                           phones. For details, go to: http://refreshcollab.cisco.com/webportal/46/CUCM%20Readiness%20Assessment#endpoint_refresh_tool .

Once  all the phones in your network are supported by Release 12.0(x), upgrade your system.

Deprecated phones can also be removed after the upgrade. When the administrator logs in to Cisco Unified Communications Manager
                                 after completing  the upgrade, the system displays a warning message notifying the administrator of the deprecated phones.

### Licensing

You do not need to purchase a new device license to replace a deprecated phone with a supported phone. The device license
                     becomes available for a new phone when you either remove the deprecated phone from the system, or when you switch to the new
                     Cisco Unified Communications Manager version, and the deprecated phone fails to register.

### For More Information

If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco
                     Systems Technical Assistance Center (TAC) by one of the following methods:

Open a service request on cisco.com

By email

By Telephone

### Receive Email Notification for New Field Notices

Cisco Notification Service —Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco
                     products you specify.

### This Document Applies to These Products

- Unified Communications Manager Version 12.0

| Products Affected | Version |
|---|---|
| Cisco Unified Communications Manager | 12.0(x) |
| Cisco Business Edition 6000 | 12.0(x) |
| Cisco Business Edition 7000 | 12.0(x) |

| Note | Deprecated phones can also be removed after the upgrade. When the administrator logs in to Cisco Unified Communications Manager
                                 after completing  the upgrade, the system displays a warning message notifying the administrator of the deprecated phones. |
|---|---|