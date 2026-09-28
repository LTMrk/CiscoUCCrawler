---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-9-cjab-b-deploy-jabber-on-premises-129-cjab-b-deploy-jabber-on-pre-7cdea6ed5d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_9/cjab_b_deploy-jabber-on-premises-129/cjab_b_deploy-jabber-on-premises-129_chapter_010100.html
retrieved_at: 2026-08-21T05:24:10.128290+00:00
---

On-Premises Deployment for Cisco Jabber 12.9

# On-Premises Deployment for Cisco Jabber 12.9

Updated: April 1, 2024

Chapter: Troubleshooting

## Chapter: Troubleshooting

- Troubleshooting

- Cisco Jabber Diagnostic Tool

- Contact Resolution Tool

# Troubleshooting

## Cisco Jabber Diagnostic Tool

### Windows and Mac

Service Discovery

- Webex

Cisco Unified Communications Manager Summary

Cisco Unified Communications Manager Configuration

Voicemail

Certificate Validation

Active Directory

DNS Records

To access the tool, users must bring the hub, call, or chat window into focus and select Ctrl + Shift + D .

Users can update the data by selecting Reload . Users can also save the information to an html file by selecting Save .

For Jabber for Windows set the DIAGNOSTICSTOOLENABLED installation parameter to FALSE.

For Jabber for Mac include the DiagnosticsToolEnabled parameter in the configuration URL with the value set to FALSE.

## Contact Resolution Tool

Applies to Cisco Jabber for Windows.

The Contact Resolution tool provides information for the available directory sources and a search tool to display contact
                              search results.

To access the Contact Resolution tool, users must bring the hub, call, or chat window into focus and select Ctrl + Shift + C .

The tool is available by default and can be disabled by setting the ContactsDiagnosticsToolEnabled installation parameter to FALSE.

Predictive—The search takes the entered string and displays the matching records. This is the same search that is used when
                                       a user searches for a contact in the client.

URI or JID

Phone number

SIP URI

Email

For more information about the ContactsDiagnosticsToolEnabled installation parameter, see On-Premises Deployment for Cisco Jabber , or Cloud and Hybrid Deployments for Cisco Jabber , depending on your deployment.