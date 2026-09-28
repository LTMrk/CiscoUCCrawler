---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-7-cjab-b-planning-guide-cisco-jabber-127-cjab-m-configuration-mana-d8395685ae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_7/cjab_b_planning-guide-cisco-jabber-127/cjab_m_configuration-management-127.html
retrieved_at: 2026-08-21T19:08:33.171610+00:00
---

Planning Guide for Cisco Jabber 12.7

# Planning Guide for Cisco Jabber 12.7

Updated: April 2, 2024

Chapter: Configuration Management

## Chapter: Configuration Management

- Configuration Management

- Fast Sign-in

# Configuration Management

## Fast Sign-in

This feature enables you to sign in to all Cisco Jabber services at the same time instead of the sequential sign-in process
                              used earlier. Each service independently connects to its respective server and authenticates you based on cached data. This
                              makes the sign-in process quick and dynamic. However, this feature is effective only from the second time you sign into Jabber.

You can configure the Fast Sign-in by using the STARTUP_AUTHENTICATION_REQUIRED parameter for all clients. However, for mobile clients you have to configure both STARTUP_AUTHENTICATION_REQUIRED and CachePasswordMobile parameters. For more information on configuring these parameters, see the latest Parameters Reference Guide for Cisco Jabber .

Configuration Refetch —Fast Sign-in does not retrieve server-side settings synchronously on every sign-in or sign-out. This happens only during
                              the first sign-in as in previous Jabber releases.

For subsequent logins, a request is sent to fetch fresh configuration from the server at various points like within 1 to 5
                              minutes after sign-in, within 7 to 9 hours after sign-in, or whenever your users do a manual refresh for fetching the configuration.

You can configure ConfigRefetchInterval parameter to fetch configuration from the server every 7 or 8 hours. For more information on this parameter, see the latest Parameters Reference Guide for Cisco Jabber .

### Action for Dynamic Configuration Changes

In Jabber 11.9, components and services react dynamically to configuration changes. You receive a notification prompt to Sign
                              out or Reset Jabber depending on these scenarios:

Reset Jabber —If a primary service is changed, you will receive a notification prompt to Reset Jabber. For example, if the IM&P and Telephony
                              account changes to a Phone only account, Jabber will require a Reset.

Windows —You will receive a pop-up notification that configuration has changed. You can either ignore the notification or Sign out
                                       and Login to use the new configuration.

Mobile Clients —Jabber signs out automatically. You then receive a pop-up notification indicating that the configuration has changed. Click OK to accept the configuration changes to sign in to Jabber automatically.

Persistent_Chat_Mobile_Enabled

Mobile Clients

Sign out

| Key Name | Platform | Sign Out |
|---|---|---|
| RemoteAccess | All Clients | Sign out |
| Meetings_Enabled | All Clients | Sign out |
| DirectoryServerType | All Clients | Sign out |
| DirectoryUri | All Clients | Sign out |
| UseSipUriToResolveContacts | All Clients | Sign out |
| SipUri | All Clients | Sign out |
| UriPrefix | All Clients | Sign out |
| DirectoryUriPrefix | All Clients | Sign out |
| SwapDisplayNameOrder | All Clients | Sign out |
| PresenceDomain | All Clients | Sign out |
| Support_SSL_Encoding | All Clients | Sign out |
| Support_No_Encoding | All Clients | Sign out |
| IM_Logging_Enabled | All Clients | Sign out |
| IGS_CUP_ENABLESECURE | All Clients | Sign out |
| DISALLOW_FILE_TRANSFER_ON_MOBILE | All Clients | Sign out |
| Persistent_Chat_Enabled | Desktop Clients | Sign out |
| Persistent_Chat_Mobile_Enabled | Mobile Clients | Sign out |
| Disable_MultiDevice_Message | All Clients | Sign out |
| Location_Enabled/Location_Matching_Mode | All Clients | Sign out |
| IP_MODE | All Clients | Sign out |
| Telephony_Enabled | All Clients | Sign out |
| Voicemail_Enabled | All Clients | Sign out |
| EnableLoadAddressBook | Mobile Clients | Sign out |
| ShowRecentsTab | Jabber Windows only | Sign out |
| IM_Enabled | All Clients | Sign out |
| Disallow-jaibreak-device | Mobile Clients | Sign out |
| EnableChats | Jabber Windows only | Sign out |