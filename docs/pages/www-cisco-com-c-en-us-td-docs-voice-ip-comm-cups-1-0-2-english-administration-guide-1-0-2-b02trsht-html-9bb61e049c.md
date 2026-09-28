---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b02trsht-html-9bb61e049c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b02trsht.html
retrieved_at: 2026-08-21T16:11:07.894902+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Configuration Troubleshooter

## Chapter: Configuration Troubleshooter

- Using the Troubleshooter

## Configuration Troubleshooter

Use the Configuration Troubleshooter to diagnose Cisco Unified Presence Server configuration issues after the initial configuration or whenever you make configuration changes. The Troubleshooter performs a set of tests on both the Cisco Unified Presence Server cluster and on the Cisco Unified CallManager cluster to validate the Cisco Unified Presence Server configuration.

After the Troubleshooter finishes testing, it reports one of three possible states for each test:

• Test passed

• Test failed

• Test warning, which indicates a possible configuration issue

For each test that fails or that results in a warning, the Troubshooter provides a description of the problem and a possible solution.

## Using the Troubleshooter

Follow this procedure to access the Configuration Troubleshooter:

Step 1 From the Cisco Unified Presence Server Administration window, choose System > Troubleshooter .

The Configuration Troubleshooter window displays. See Table 7-1 for a list of tests that the Troubleshooter performs.

Step 2 Examine the Results table for any tests that failed or that generated a warning.

Step 3 For any test failures or test warnings, click the fix link in the solution column to go to the Cisco Unified Presence Server Administration window where the Troubleshooter found the problem.

Step 4 Correct any configuration errors you find and rerun the Troubleshooter.

Table 7-1 Configuration Troubleshooter Tests

AXL tests

Verify that an AXL settings entry exists.

Verify that the AXL user-id is valid.

Verify that the publisher address is reachable; then, log in and execute a basic query.

Verify that the Sync Agent synchronized the relevant data (for example, devices, users, and licensing information).

Verify that the Sync Agent service is running.

IPPM tests

Verify that an IPPM settings entry exists.

Verify that the IPPM application usernames is valid.

Verify that the IPPM application password is valid.

Verify that the Cisco Unified Presence Server IPPM application username and password match the configured Cisco Unified CallManager application username and password.

Verify that the IPPM service is active.

Verify that the IPPM service is running.

Presence Engine tests

Verify that the Cisco Unified CallManager Presence Gateway entry exists.

Verify that the Presence Engine service is running.

Verify that the Presence Engine OAM Agent service is running.

Verify that the Presence Engine Database service is running.

Verify that the Cisco Unified CallManager Presence Gateway is valid.

Verify that a valid SIP trunk exists on the Cisco Unified CallManager server.

Proxy Server tests

Verify that the SIP Proxy service Proxy Domain service parameter value is valid.

Verify that default method/event routes exist.

Verify that the SIP Proxy service is running.

Verify that the Config Agent service is running.

Verify that all incoming SIP Proxy ACL entries are reachable.

Verify that the outgoing SIP Proxy ACL entries are reachable.

CTI Gateway tests

Verify that the CTI Gateway Settings entry exists.

Verify that the CTI address address is reachable.

Verify that the application username and password are valid.

Verify that the preferred SIP Proxy listener is using transport type of TCP.

Verify that the CTI Gateway service is active.

Verify that the CTI Gateway service is running.

.

| Test Group | Test Action |
|---|---|
| AXL tests | Verify that an AXL settings entry exists. |
| Verify that the AXL user-id is valid. |
| Verify that the publisher address is reachable; then, log in and execute a basic query. |
| Verify that the Sync Agent synchronized the relevant data (for example, devices, users, and licensing information). |
| Verify that the Sync Agent service is running. |
| IPPM tests | Verify that an IPPM settings entry exists. |
| Verify that the IPPM application usernames is valid. |
| Verify that the IPPM application password is valid. |
| Verify that the Cisco Unified Presence Server IPPM application username and password match the configured Cisco Unified CallManager application username and password. |
| Verify that the IPPM service is active. |
| Verify that the IPPM service is running. |
| Presence Engine tests | Verify that the Cisco Unified CallManager Presence Gateway entry exists. |
| Verify that the Presence Engine service is running. |
| Verify that the Presence Engine OAM Agent service is running. |
| Verify that the Presence Engine Database service is running. |
| Verify that the Cisco Unified CallManager Presence Gateway is valid. |
| Verify that a valid SIP trunk exists on the Cisco Unified CallManager server. |
| Proxy Server tests | Verify that the SIP Proxy service Proxy Domain service parameter value is valid. |
| Verify that default method/event routes exist. |
| Verify that the SIP Proxy service is running. |
| Verify that the Config Agent service is running. |
| Verify that all incoming SIP Proxy ACL entries are reachable. |
| Verify that the outgoing SIP Proxy ACL entries are reachable. |
| CTI Gateway tests | Verify that the CTI Gateway Settings entry exists. |
| Verify that the CTI address address is reachable. |
| Verify that the application username and password are valid. |
| Verify that the preferred SIP Proxy listener is using transport type of TCP. |
| Verify that the CTI Gateway service is active. |
| Verify that the CTI Gateway service is running. |