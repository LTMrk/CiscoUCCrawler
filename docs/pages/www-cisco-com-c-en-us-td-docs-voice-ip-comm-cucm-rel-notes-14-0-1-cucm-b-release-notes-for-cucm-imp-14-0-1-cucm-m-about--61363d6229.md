---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-14-0-1-cucm-b-release-notes-for-cucm-imp-14-0-1-cucm-m-about--61363d6229
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/14_0_1/cucm_b_release-notes-for-cucm-imp-14_0_1/cucm_m_about-this-release.html
retrieved_at: 2026-08-16T23:51:05.129373+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 14

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 14

## Results

Updated: October 22, 2024

Chapter: About this Release

## Chapter: About this Release

# About this Release

## About Release Notes

This release describes new features, restrictions, and caveats for Cisco Unified Communications Manager ( Unified Communications Manager ) and Cisco Unified Communications Manager IM and Presence Service ( IM and Presence Service ) . The release notes are updated for every maintenance release but not for patches or hot fixes.

## Supported Versions

The following software versions apply to Release 14:

Unified Communications Manager: 14.0.1.10000-20

IM and Presence Service: 14.0.1.10000-16

### Version Compatibility Between Unified CM and the IM and Presence Service

Version compatibility depends on the IM and Presence Service deployment type. The following table outlines the options and
                                 whether a release mismatch is supported between the telephony deployment and the IM and Presence Service deployment. A release
                                 mismatch, if it is supported, would let you deploy your Unified Communications Manager telephony deployment and your IM and
                                 Presence Service deployment using different releases.

For Release 12.5(1)SU7a, a Unified Communications Manager ES with a build number of 12.5.1.181xx would be considered part
                                             of the 12.5(1)SU7a (12.5.1.18100-x) release.

For Release 12.5(1)SU8a, a Unified Communications Manager ES with a build number of 12.5.1.19[0-2]xx would be considered part
                                             of the 12.5(1)SU8a (12.5.1.18901-1) release.

Deployment Type

Release Mismatch

Description

Standard Deployment of IM and Presence Service

Not supported

Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                             mismatch is not supported.

Centralized Deployment of IM and Presence Service

Supported

The IM and Presence Service deployment and the telephony deployment are in different clusters and can run different releases—a
                                             release mismatch is supported.

## Documentation for this Release

For a complete list of the documentation that is available for this release, see the Documentation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14 .

## Installation Procedures

For information on how to install your system, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service .

## Upgrade Procedures

For information on how to upgrade to this release, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 14 .

| Note | Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                          of 12.5.1.18[0-2]xx would be considered part of the 12.5(1)SU7 (12.5.1.17900-x) release. For Release 12.5(1)SU7a, a Unified Communications Manager ES with a build number of 12.5.1.181xx would be considered part
                                             of the 12.5(1)SU7a (12.5.1.18100-x) release. For Release 12.5(1)SU8a, a Unified Communications Manager ES with a build number of 12.5.1.19[0-2]xx would be considered part
                                             of the 12.5(1)SU8a (12.5.1.18901-1) release. |
|---|---|

| Deployment Type | Release Mismatch | Description |
|---|---|---|
| Standard Deployment of IM and Presence Service | Not supported | Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                             mismatch is not supported. |
| Centralized Deployment of IM and Presence Service | Supported | The IM and Presence Service deployment and the telephony deployment are in different clusters and can run different releases—a
                                             release mismatch is supported. Note The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. Note Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. | Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. | Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. |
| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. |
| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. |

| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. |
|---|---|

| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. |
|---|---|