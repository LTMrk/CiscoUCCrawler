---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-9-cjab-b-parameter-reference-guide-jabber-129-cjab-b-parameter-ref-c820bee151
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_9/cjab_b_parameter-reference-guide-jabber-129/cjab_b_parameter-reference-guide-jabber-129_chapter_01001.html
retrieved_at: 2026-08-21T05:25:27.364056+00:00
---

Parameters reference guide for Cisco Jabber 12.9

# Parameters reference guide for Cisco Jabber 12.9

Updated: September 26, 2023

Chapter: Voicemail

## Chapter: Voicemail

# Voicemail

## ForwardVoicemail

Applies to all clients.

true (default)—voicemail forwarding is enabled. When users select a voicemail in the Voice Messages tab, the Forward voice message option is available.

false—voicemail forwarding is not enabled.

Example: <ForwardVoicemail>false</ForwardVoicemail>

## VoicemailBackup1Server

Applies to Cisco Jabber for desktop and mobile clients.

Hostname ( hostname )

IP Address ( 123.45.254.1 )

FQDN ( hostname.domain.com )

The Cisco Jabber client supports having two backup servers, plus the primary server, totaling three servers. However, the
                              voicemail server supports only two voicemail servers in one cluster. To configure two backup servers, put one in the same
                              cluster as the primary server, and the second in another cluster

Example: <VoicemailBackup1Server> hostname </VoicemailBackup1Server>

## VoicemailBackup2Server

Applies to Cisco Jabber for desktop and mobile clients.

Hostname ( hostname )

IP Address ( 123.45.254.1 )

FQDN ( hostname.domain.com )

The Cisco Jabber client supports having two backup servers plus the primary server, totaling three servers. However, the voicemail
                              server supports only two voicemail servers in one cluster. To configure two backup servers, put one in the same cluster as
                              the primary server, and the second in another cluster.

Example: <VoicemailBackup2Server> hostname.domain.com </VoicemailBackup2Server>

## VoicemailPrimaryServer

Hostname
                                       				( hostname )

IP address
                                       				( 123.45.254.1 )

FQDN ( hostname.domain.com )

Example: <VoicemailPrimaryServer> hostname </VoicemailPrimaryServer>

## VoiceMailService_UseCredentialsFrom

Specifies that the client uses the phone service credentials to access voicemail services.

Ensure the user's phone service credentials match their voicemail service credentials. If you set this configuration, users
                              cannot specify voicemail service credentials in the client interface.

This parameter is not set by default. The value is phone.

You should set this parameter in the following deployments only:

Hybrid cloud-based deployments.

Phone mode deployments.

In on-premises deployments, set the credentials source on the presence server for voicemail services.

The following is an example of the voicemail service credentials parameter:

```
<?xml version="1.0" encoding="utf-8"?> 
<config version="1.0"> 
	<Voicemail> 
		<VoicemailService_UseCredentialsFrom>phone</VoicemailService_UseCredentialsFrom> 
	</Voicemail> 
</config>
```