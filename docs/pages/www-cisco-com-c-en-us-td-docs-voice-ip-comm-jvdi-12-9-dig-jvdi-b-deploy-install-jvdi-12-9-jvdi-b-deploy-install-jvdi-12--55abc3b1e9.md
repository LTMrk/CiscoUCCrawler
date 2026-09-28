---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-9-dig-jvdi-b-deploy-install-jvdi-12-9-jvdi-b-deploy-install-jvdi-12--55abc3b1e9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_9/dig/jvdi_b_deploy-install-jvdi-12-9/jvdi_b_deploy-install-jvdi-12-9_chapter_0101.html
retrieved_at: 2026-08-22T00:32:09.901269+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.9

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.9

Updated: July 8, 2020

Chapter: Upgrade

## Chapter: Upgrade

# Upgrade

## Upgrade Notes

To get the new Cisco Jabber Softphone for VDI features, you must upgrade all of the following components to the
                              current release:

Cisco Jabber for Windows

Cisco JVDI Agent

Cisco JVDI Client

Both the Cisco JVDI Agent and Cisco JVDI Client are required for softphone registration to succeed. The Cisco Jabber for Windows and the Cisco JVDI Agent versions must always match. However, the Cisco JVDI Client version can be the same, or up to two releases earlier. The earlier software version determines the available feature set.

## Version Support Strategy

The Cisco Jabber for Windows and Cisco JVDI Agent major versions (N.A) must
                                    always match. However, the JVDI Client version can be the same, or up to two
                                    releases earlier (N-2 support).

N.A-C denotes the range of major releases. x-z denotes the numbers of different maintenance
                                                releases. These numbers are used for example purposes only.

For example, the following version combinations are supported within a
                                    release range:

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.A(z)

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.B(z)

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.C(z)

The above examples cover the supported range within a single major
                                                release. For a major release that starts at a new release number (for
                                                example, 14.0), the JVDI client is also supported on the two previous
                                                releases (for example, 12.9 and 12.8).

The following version combinations are not supported within a release
                                    range:

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.D(z)

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.B(y), and Cisco JVDI Client Release N.C(z)

## Upgrade Workflow

We recommend that you read the release notes document for your platform. Review the requirements to confirm that all hardware
                              and software meet them. Failure to meet all requirements can result in a nonfunctional deployment.

### Before you begin

Ensure that you have all of the required files on hand. If you plan to manually install Cisco JVDI Client on the thin clients, copy the files to a USB stick.

Follow the steps to install the Cisco Jabber Softphone for VDI components on the thin clients and the HVDs.

Both the Cisco JVDI Agent and Cisco JVDI Client are required for softphone registration to succeed. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the Cisco JVDI Client version can be the same, or the previous version. The earlier software version determines the available feature set.

If you're not upgrading the Cisco JVDI Client , you can skip the steps to install it.

| Note | N.A-C denotes the range of major releases. x-z denotes the numbers of different maintenance
                                                releases. These numbers are used for example purposes only. |
|---|---|

| Note | The above examples cover the supported range within a single major
                                                release. For a major release that starts at a new release number (for
                                                example, 14.0), the JVDI client is also supported on the two previous
                                                releases (for example, 12.9 and 12.8). |
|---|---|

| Follow the steps to install the Cisco Jabber Softphone for VDI components on the thin clients and the HVDs. Important Both the Cisco JVDI Agent and Cisco JVDI Client are required for softphone registration to succeed. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the Cisco JVDI Client version can be the same, or the previous version. The earlier software version determines the available feature set. If you're not upgrading the Cisco JVDI Client , you can skip the steps to install it. | Important | Both the Cisco JVDI Agent and Cisco JVDI Client are required for softphone registration to succeed. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the Cisco JVDI Client version can be the same, or the previous version. The earlier software version determines the available feature set. If you're not upgrading the Cisco JVDI Client , you can skip the steps to install it. |
|---|---|---|
| Important | Both the Cisco JVDI Agent and Cisco JVDI Client are required for softphone registration to succeed. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the Cisco JVDI Client version can be the same, or the previous version. The earlier software version determines the available feature set. If you're not upgrading the Cisco JVDI Client , you can skip the steps to install it. |

| Important | Both the Cisco JVDI Agent and Cisco JVDI Client are required for softphone registration to succeed. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the Cisco JVDI Client version can be the same, or the previous version. The earlier software version determines the available feature set. If you're not upgrading the Cisco JVDI Client , you can skip the steps to install it. |
|---|---|