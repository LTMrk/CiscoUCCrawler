---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-b-deploy-jabber-on-premises-14-0-cjab-b-deploy-jabber-on-pr-938aa5be6b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_b_deploy-jabber-on-premises-14_0/cjab_b_deploy-jabber-on-premises-129_chapter_010100.html
retrieved_at: 2026-08-21T07:07:51.922252+00:00
---

On-Premises Deployment for Cisco Jabber 14.0

# On-Premises Deployment for Cisco Jabber 14.0

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

### Android, iPhone, and iPad

If users are unable to sign into Cisco Jabber or your Cisco Jabber IM and Phone services aren’t connected, they can use the Diagnose Error option to check what’s causing the issue.

Users can tap Diagnose Error option either from the Sign In page or from the warning notification they get when connecting to Cisco Jabber services. Cisco Jabber then verifies:

If there are any network issues

If Cisco Jabber servers are reachable

If Cisco Jabber can reconnect

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