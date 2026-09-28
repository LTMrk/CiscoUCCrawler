---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-hybridservices-hybridcalldevices-wbxhs-m-deployment--f2ff1f4563
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/hybridservices/hybridcalldevices/wbxhs_m_deployment-guide-for-webex-devices-hybrid-call/wbxhs_m_deployment-guide-for-webex-devices-hybrid-call_preface_0100.html
retrieved_at: 2026-08-20T23:57:18.248219+00:00
---

Deployment guide for Hybrid Calling for Webex Devices (Device Connector)

# Deployment guide for Hybrid Calling for Webex Devices (Device Connector)

Updated: October 12, 2023

Chapter: New and changed information

## Chapter: New and changed information

- New and changed information

# New and changed information

Date

Changes Made

October 12, 2023

Added a note to Overview that Webex Calling Dedicated Instance does not require the Device Connector.

December 3, 2021

Added the following note to the mutual TLS authentication
                                          configuration steps:

If you Expressway-E is clustered, you can't disable H.323
                                          box-wide because clustering relies on H.323. For this
                                          reason, we recommend setting up firewall rules on Expressway
                                          or the Internet firewall to block H.323 inbound.

In the Unified CM SIP trunk security profile configuration,
                                          added a step to set the Device Security Mode to
                                          Encrypted.

Added the following note to the "Complete the
                                             prerequisites" section:

If you plan to use the manual method, you must trust
                                                      IdenTrust as a public certificate authority (CA). See Webex Root CA
                                                         Certificate Update . Upload the IdenTrust
                                                      certificate to your Expressway devices as soon as
                                                      possible. Otherwise, calls from the Expressway-E to the
                                                      cloud may fail.

In accordance with style guidelines, changed section titles
                                          from title case to sentence case.

July 9, 2021

Updated naming and diagrams to reflect the new Webex Suite branding .

Moved non-deployment tasks (such as Rename Workspace, Remove
                                          Calling, and so on) to the Manage and Troubleshoot
                                          chapter.

May 21, 2021

Corrected references to various parts of the Control Hub web
                                          interface.

In the Known Issues section, added a link to the Preferred
                                          Architecture guide which contains more information about
                                          loop detection and avoidance.

Retitled "Configure Directory Number" to "Configure Directory
                                          Number and Directory URI", and added a statement to clarify
                                          the workaround for Directory URI dialing between a user and
                                          a device.

January 20, 2021

Added new section "Enable Hybrid Calling for Personal Mode
                                             Devices" in the deployment chapter.

Combined the personal mode and shared mode enablement steps
                                          under a single workflow table.

December 9, 2020

References to "Webex Teams" are changed to "Webex."

Clarified that Hybrid Calling calls don't consume traversal
                                          licenses.

Added known issues about extension dialing, directory URI
                                          dialing, and calling from one organization to another.

August 19, 2020

Removed incorrect content about the automatic creation of Cisco Spark-RD.

Rearranged deployment chapter; now, the directory number, Cisco Spark-RD, end user, and Workspaces steps are tied together
                                          in a mini task flow.

June 16, 2020

References to "Places" have been changed to "Workspaces."

April 23, 2020

Added "Migrate Hybrid Calling Organization Using Webex Device Connector" section to the Prepare Your Environment chapter.

February 28, 2020

Initial version of the document.

| Date | Changes Made |
|---|---|
| October 12, 2023 | Added a note to Overview that Webex Calling Dedicated Instance does not require the Device Connector. |
| December 3, 2021 | Added the following note to the mutual TLS authentication
                                          configuration steps: If you Expressway-E is clustered, you can't disable H.323
                                          box-wide because clustering relies on H.323. For this
                                          reason, we recommend setting up firewall rules on Expressway
                                          or the Internet firewall to block H.323 inbound. In the Unified CM SIP trunk security profile configuration,
                                          added a step to set the Device Security Mode to
                                          Encrypted. Added the following note to the "Complete the
                                             prerequisites" section: Note If you plan to use the manual method, you must trust
                                                      IdenTrust as a public certificate authority (CA). See Webex Root CA
                                                         Certificate Update . Upload the IdenTrust
                                                      certificate to your Expressway devices as soon as
                                                      possible. Otherwise, calls from the Expressway-E to the
                                                      cloud may fail. In accordance with style guidelines, changed section titles
                                          from title case to sentence case. | Note | If you plan to use the manual method, you must trust
                                                      IdenTrust as a public certificate authority (CA). See Webex Root CA
                                                         Certificate Update . Upload the IdenTrust
                                                      certificate to your Expressway devices as soon as
                                                      possible. Otherwise, calls from the Expressway-E to the
                                                      cloud may fail. |
| Note | If you plan to use the manual method, you must trust
                                                      IdenTrust as a public certificate authority (CA). See Webex Root CA
                                                         Certificate Update . Upload the IdenTrust
                                                      certificate to your Expressway devices as soon as
                                                      possible. Otherwise, calls from the Expressway-E to the
                                                      cloud may fail. |
| July 9, 2021 | Updated naming and diagrams to reflect the new Webex Suite branding . Moved non-deployment tasks (such as Rename Workspace, Remove
                                          Calling, and so on) to the Manage and Troubleshoot
                                          chapter. |
| May 21, 2021 | Corrected references to various parts of the Control Hub web
                                          interface. In the Known Issues section, added a link to the Preferred
                                          Architecture guide which contains more information about
                                          loop detection and avoidance. Retitled "Configure Directory Number" to "Configure Directory
                                          Number and Directory URI", and added a statement to clarify
                                          the workaround for Directory URI dialing between a user and
                                          a device. |
| January 20, 2021 | Added new section "Enable Hybrid Calling for Personal Mode
                                             Devices" in the deployment chapter. Combined the personal mode and shared mode enablement steps
                                          under a single workflow table. |
| December 9, 2020 | References to "Webex Teams" are changed to "Webex." Clarified that Hybrid Calling calls don't consume traversal
                                          licenses. Added known issues about extension dialing, directory URI
                                          dialing, and calling from one organization to another. |
| August 19, 2020 | Removed incorrect content about the automatic creation of Cisco Spark-RD. Rearranged deployment chapter; now, the directory number, Cisco Spark-RD, end user, and Workspaces steps are tied together
                                          in a mini task flow. |
| June 16, 2020 | References to "Places" have been changed to "Workspaces." |
| April 23, 2020 | Added "Migrate Hybrid Calling Organization Using Webex Device Connector" section to the Prepare Your Environment chapter. |
| February 28, 2020 | Initial version of the document. |

| Note | If you plan to use the manual method, you must trust
                                                      IdenTrust as a public certificate authority (CA). See Webex Root CA
                                                         Certificate Update . Upload the IdenTrust
                                                      certificate to your Expressway devices as soon as
                                                      possible. Otherwise, calls from the Expressway-E to the
                                                      cloud may fail. |
|---|---|