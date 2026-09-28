---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-319701da86
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_1501-configuration-guide-for-cisco-customer-voice-portal-release/ccai_services_configuration.html
retrieved_at: 2026-08-21T12:07:50.319331+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: December 12, 2025

Chapter: CCAI Services Configuration

## Chapter: CCAI Services Configuration

- CCAI Services Configuration

- HTTP Proxy Settings in Call Server

- HTTP Proxy Settings in OAMP Server

# CCAI Services Configuration

## HTTP Proxy Settings in Call Server

For Agent Answers and other CCAI services to function, the Call server must be connected to the internet. Enable direct access
                              to the internet or configure HTTP proxy settings in the Call server. To configure HTTP proxy settings in Call server, perform
                              the following steps:

Step 1

Open Windows regedit in the Call server.

Step 2

Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\CallServer\Parameters\Java\Options .

Step 3

Add the following entries:

```
-Dhttp.proxyHost=<proxy IP>
-Dhttp.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttp.nonProxyHosts=<hostname>
```

```
-Dhttps.proxyHost=<proxy IP/FQDN>
-Dhttps.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttps.nonProxyHosts=<hostname>
```

Step 4

Restart the CVP Call server from Windows services.

## HTTP Proxy Settings in OAMP Server

For Agent Answers and other CCAI services to function, the OAMP server must be connected to the internet. Enable direct access
                              to the internet or configure HTTP proxy settings in the OAMP server. To configure HTTP proxy settings in OAMP server, perform
                              the following steps:

Step 1

Open Windows regedit in the OAMP server.

Step 2

Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\OPSConsoleServer\Parameters\Java\Options .

Step 3

Add the following entries:

```
-Dhttp.proxyHost=<proxy IP>
-Dhttp.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttp.nonProxyHosts=<hostname>
```

Step 4

Restart the OAMP server from Windows services.

| Step 1 | Open Windows regedit in the Call server. |
|---|---|
| Step 2 | Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\CallServer\Parameters\Java\Options . |
| Step 3 | Add the following entries: -Dhttp.proxyHost=<proxy IP>
-Dhttp.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttp.nonProxyHosts=<hostname> Note Based on the call server environment, you can use the following Dhttps instead of Dhttp: -Dhttps.proxyHost=<proxy IP/FQDN>
-Dhttps.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttps.nonProxyHosts=<hostname> | Note | Based on the call server environment, you can use the following Dhttps instead of Dhttp: -Dhttps.proxyHost=<proxy IP/FQDN>
-Dhttps.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttps.nonProxyHosts=<hostname> |
| Note | Based on the call server environment, you can use the following Dhttps instead of Dhttp: -Dhttps.proxyHost=<proxy IP/FQDN>
-Dhttps.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttps.nonProxyHosts=<hostname> |
| Step 4 | Restart the CVP Call server from Windows services. |

| Note | Based on the call server environment, you can use the following Dhttps instead of Dhttp: -Dhttps.proxyHost=<proxy IP/FQDN>
-Dhttps.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttps.nonProxyHosts=<hostname> |
|---|---|

| Step 1 | Open Windows regedit in the OAMP server. |
|---|---|
| Step 2 | Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\OPSConsoleServer\Parameters\Java\Options . |
| Step 3 | Add the following entries: -Dhttp.proxyHost=<proxy IP>
-Dhttp.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttp.nonProxyHosts=<hostname> |
| Step 4 | Restart the OAMP server from Windows services. |