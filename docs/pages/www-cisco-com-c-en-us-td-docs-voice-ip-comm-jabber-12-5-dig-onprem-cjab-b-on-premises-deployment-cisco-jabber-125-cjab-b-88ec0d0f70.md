---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-5-dig-onprem-cjab-b-on-premises-deployment-cisco-jabber-125-cjab-b-88ec0d0f70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_5/DIG_OnPrem/cjab_b_on-premises-deployment-cisco-jabber_125/cjab_b_on-premises-deployment-cisco-jabber_125_chapter_010100.html
retrieved_at: 2026-08-21T21:12:26.154536+00:00
---

On-Premises Deployment for Cisco Jabber 12.5

# On-Premises Deployment for Cisco Jabber 12.5

Updated: November 27, 2018

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