---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-ffce39f8cc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_011010.html
retrieved_at: 2026-08-16T20:29:14.274862+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Single Sign-On Status API

## Chapter: Single Sign-On Status API

- Single Sign-On Status API

- Single Sign-On Status API

# Single Sign-On Status API

## Single Sign-On Status API

Use the Single Sign-On (SSO) Registration API to get the current status of registering components with the Cisco Identity
                           Service (IdS) and setting SSO state on the SSO-compatible components.  These components include AW, Finesse, and Unified Intelligence
                           Center machines.

### URL

https://<server>/unifiedconfig/config/sso/status

### Operations

get component status: Returns the status of registering a specific component with the Cisco IdS and setting SSO state, using
                                    the URL https://<server>/unifiedconfig/config/sso/status/<id> . The <id> is the machine_id of the component.

list :
                                    				Retrieves a list with the overall and individual component statuses of registering SSO-compatible components with the
                                    Cisco Identity Service and setting SSO state, using the URL https://<server>/unifiedconfig/config/sso/status .

### Parameters

globalSsoState: The current SSO state as set in the AW database. The values are NON_SSO (SSO is disabled for all users), SSO
                                    (SSO is enabled for all users), and HYBRID (mix of enabled and disabled).

SUCCEEDED: All of the components were successfully registered.

FAILED: Registration failed on one or more components.  Error detail is set on each failed component.

PROCESSING: Registration started and is not complete.

NOT_STARTED: Registration has not started.

SUCCEEDED: The SSO state was successfully set on all of  the components.

FAILED: The SSO state failed to be set on one or more components.  Error detail is set on each failed component.

PROCESSING: The SSO state change has started and is not complete.

NOT_STARTED: The SSO state change has not started.

idSConfigurationState: Whether the Cisco IdS has been configured and is in service.

STATE_NOT_CONFIGURED
                                          : The Cisco IdS is not been configured.

STATE_IN_SERVICE
                                          : The Cisco IdS is configured and is in service.

STATE_OUT_OF_SERVICE
                                          : The Cisco IdS is configured and is out of service.

STATE_PARTIAL_SERVICE: The Cisco IdS is configured and is partially in service.

STATE_UNREACHABLE: The Cisco IdS cannot be reached.

hasIdsCredentials: Whether the Machine Inventory has the necessary IdS credentials  to register components (see Machine Inventory API . Values are true or false. The default is false.

idsBaseUrl: The base URL for  accessing the Identity Service.

ssoComponentStatuses: A collection of registration and SSO state status information for all of the individual components.
                                    Returned on a list operation.

ssoComponentStatus: Registration and SSO state status information for an individual component.   Includes the following parameters:

registrationState: The status of registering the component with the IdS. See the values for this parameter above.

modeState: The status of setting the SSO state for the component. See the values for this parameter above.

refURL: The refURL for the component machine. See Shared Parameters .

name: The name of the component machine.

### Example Get Response

Example URL: https://<server>/unifiedconfig/config/sso/status/21

```
<ssoComponentStatus>
  <registrationState>FAILED</registrationState>
  <modeState>NOT_STARTED</modeState>
  <refURL>/unifiedconfig/config/machineinventory/21</refURL>
  <name>FINESSE-A.boston.com</name>
</ssoComponentStatus>
```

### Example List Response

```
<ssoStatus>
  <globalSsoState>HYBRID</globalSsoState>
  <registrationState>FAILED</registrationState>
  <modeState>NOT_STARTED</modeState>
  <idSConfigurationState>STATE_IN_SERVICE</idSConfigurationState>
  <hasIdsCredentials>true</hasIdsCredentials>
  <idsBaseUrl>https://<server>:<serverport></idsBaseUrl>
  <ssoComponentStatuses>
    <ssoComponentStatus>
      <registrationState>FAILED</registrationState>
      <modeState>NOT_STARTED</modeState>
      <refURL>/unifiedconfig/config/machineinventory/21</refURL>
      <name>FINESSE-A.boston.com</name>
    </ssoComponentStatus>
    <ssoComponentStatus>
      <registrationState>FAILED</registrationState>
      <modeState>NOT_STARTED</modeState>
      <refURL>/unifiedconfig/config/machineinventory/22</refURL>
      <name>FINESSE-B.boston.com</name>
    </ssoComponentStatus>
    <ssoComponentStatus>
      <registrationState>FAILED</registrationState>
      <modeState>NOT_STARTED</modeState>
      <refURL>/unifiedconfig/config/machineinventory/23</refURL>
      <name>CUIC-A.boston.com</name>
    </ssoComponentStatus>
  </ssoComponentStatuses>
</ssoStatus>
```