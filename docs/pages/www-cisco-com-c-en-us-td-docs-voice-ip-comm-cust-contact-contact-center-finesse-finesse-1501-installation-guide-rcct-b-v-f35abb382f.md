---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-installation-guide-rcct-b-v-f35abb382f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/installation/guide/rcct_b_vpn-less-finesse/rcct_m_150_frequently-asked-questions.html
retrieved_at: 2026-08-16T19:58:09.252443+00:00
---

Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1)

# Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Frequently Asked Questions

## Chapter: Frequently Asked Questions

- Frequently Asked Questions

- Frequently Asked Questions

# Frequently Asked Questions

## Frequently Asked Questions

Why does the proxy launcher fail to restart the Reverse-Proxy?

The environment settings are incorrect. Correct any errors in the environment data and retry.The log file is stored at ${HOST_WORKING_DIR}/logs/openresty_launcher.log . Using the command podman ps -a , see if the container is up and running.

How to check the different instances of the reverse proxy container?

Use the command podman ps to list all the reverse proxy containers running on the host.

How can I solve the OpenResty® launch error?

Some error during OpenResty® start. Fix any of the errors listed in the error log file available at ${HOST_WORKING_DIR}/logs/error.log and try to restart.

Why is the content not refreshed to the end user?

Cache is not updated with latest contents. Run the following command to clear the cache:

podman exec <PROXY_HOSTNAME> /usr/local/openresty/nginx/sbin/openresty_launcher.sh clear_cache . The error log file available at ${HOST_WORKING_DIR}/logs/access.log

Why is configuration generation from templates unsuccessful?

Failed to validate while generating the configuration. Correct any problems or failures reported on the console or in the
                                 error file. The error file as follows "Configuration generation from templates fails".

How can I fix problems or failures reported on the console or in the error file?

Reverse-proxy is not included in the authorized list. Use this list of CLI Reverse-Proxy authorized hosts and confirm if the
                                 list of Reverse-Proxy authorized host names configured on Cisco IdS and Finesse boxes. This must contain the Reverse-Proxy
                                 hostname and the allowed IP address.

What causes intermittent failures of Finesse REST API?

Because of the NGINX proxy rate limit issue, gadgets are not loading in the Finesse desktop. This results in intermittent
                                 Finesse REST API failures.

How do I determine which OpenResty® version is being used in the Installer?

Run the following command in the proxy instance to check the OpenResty® version on the Installer:

Why does proxy send HTTP error code 4xx ?

Refer to the HTTP Return codes returned by the reverse-proxy section.

Problem Summary

Log File

Possible Cause

Recommendation Action

Proxy launcher fails to restart the reverse-proxy

${HOST_WORKING_DIR}/

logs/openresty_launcher.log

Check if the container is up, and running using the command podman ps -a

Wrong environment configurations

Correct any of the issues within the environment data, and retry.

OpenResty® startup failure

${HOST_WORKING_DIR}/

logs/error.log

Some error during OpenResty® start

Resolve any of the error stated in the error log file, and try "Restart".

Content not updated for the end user

${HOST_WORKING_DIR}/

logs/access.log

Cache not updated with latest content

Run the following command to clear the cache:

podman exec <PROXY_HOSTNAME> /usr/local/openresty/nginx/sbin/openresty_launcher.sh clear_cache

Config generation from templates fails

Config generation from templates fails

Validation failures during config generation

Correct the issues or the failures as reported on the console or in the error file

Correct issues/failures as reported on console or in error file

—

Reverse-proxy is not part of the allowed list.

Use this CLI utils system reverse-proxy allowed-hosts list and validate if the list of whitelisted reverse-proxy hostnames
                                          configured on IdS and Finesse boxes. It should contain the reverse-proxy hostname, and whitelisted IP address.

Intermittent Finesse REST API failures

—

Gadgets fails to load in Finesse desktop due to the rate limit issue at NGINX proxy.

Check if the rate limit of the values configured on the core.env are correct. Also, validate if the bug CSCwc65529 fixed is present on the current config.

—

—

Run the following command in the proxy instance to check the OpenResty® version:

podman exec <proxy_instance_name> | grep resty_rpm_version | cut -d ":" -f2

| Problem Summary | Log File | Possible Cause | Recommendation Action |
|---|---|---|---|
| Proxy launcher fails to restart the reverse-proxy | ${HOST_WORKING_DIR}/ logs/openresty_launcher.log Check if the container is up, and running using the command podman ps -a | Wrong environment configurations | Correct any of the issues within the environment data, and retry. |
| OpenResty® startup failure | ${HOST_WORKING_DIR}/ logs/error.log | Some error during OpenResty® start | Resolve any of the error stated in the error log file, and try "Restart". |
| Content not updated for the end user | ${HOST_WORKING_DIR}/ logs/access.log | Cache not updated with latest content | Run the following command to clear the cache: podman exec <PROXY_HOSTNAME> /usr/local/openresty/nginx/sbin/openresty_launcher.sh clear_cache |
| Config generation from templates fails | Config generation from templates fails | Validation failures during config generation | Correct the issues or the failures as reported on the console or in the error file |
| Correct issues/failures as reported on console or in error file | — | Reverse-proxy is not part of the allowed list. | Use this CLI utils system reverse-proxy allowed-hosts list and validate if the list of whitelisted reverse-proxy hostnames
                                          configured on IdS and Finesse boxes. It should contain the reverse-proxy hostname, and whitelisted IP address. |
| Intermittent Finesse REST API failures | — | Gadgets fails to load in Finesse desktop due to the rate limit issue at NGINX proxy. | Check if the rate limit of the values configured on the core.env are correct. Also, validate if the bug CSCwc65529 fixed is present on the current config. |
| To check the OpenResty® version being run in the Installer | — | — | Run the following command in the proxy instance to check the OpenResty® version: podman exec <proxy_instance_name> \| grep resty_rpm_version \| cut -d ":" -f2 |