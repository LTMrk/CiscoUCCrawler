---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-installation-guide-rcct-b-v-79554fa8a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/installation/guide/rcct_b_vpn-less-finesse/rcct_m_150_reverse-proxy-installer-environment-file-properties.html
retrieved_at: 2026-08-16T19:58:15.148917+00:00
---

Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1)

# Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Reverse Proxy Installer Environment File Properties

## Chapter: Reverse Proxy Installer Environment File Properties

# Reverse Proxy Installer Environment File Properties

## Reverse Proxy Installer Environment File Properties

### Environment Files

The Reverse Proxy Installer behavior is driven using user-editable configuration files called environment files (.env). The
                              environment file contains configuration data in the form of key=value pairs, which are referred to as properties. Each upstream component has custom environment files and properties specific
                              to the respective component. The Installer also has its own specific environment files, used to customize its behavior. Reverse
                              proxy installation requires the administrator to modify the properties to match the deployment. The following tables list
                              and describe these properties, with their default values and guidance about changing them:

Hot reload is not supported for the installer.env properties and for properties that are not recommended to be changed.

Cisco Reverse Proxy Installer is a per-requisite reading for this chapter.

### Installer env properties

The installer runs the Podman container that contains the proxy. The properties determine the configuration of the container
                                 like the resources made available to it and the network configurations and such. By default, the properties are set to 2000
                                 users deployment. Deployments which are bigger or smaller than 2000 users must verify these values and modify them appropriately.

Property Name, Description, and Default

Change Recommended?

When to Change?

CONTAINER_NAME

Specifies the name of the reverse-proxy container—generally the reverse-proxy hostname.

Default: proxy25.autobot.cvp

Yes

When you change the name of the container.

CONTAINER_NETWORK_MODE

Specifies the network mode of the container.

Default: host

Yes, if required.

If you use the host network mode for a container, the network stack for that container isn’t isolated from the host. 1

The other value is bridge . A bridge network creates a separate network for containers to communicate with each other, even if it is isolated from other
                                             networks on the host. This is useful when you want to deploy multiple containers on a single host and communicate with each
                                             other, but not with the outside world.

CONTAINER_DNS_RESOLVER

Specifies a list of DNS servers separated by the | symbol.

Default: 1.1.1.1|8.8.8.8

Yes

If an IP address changes, update the list.

CONTAINER_DNS_SEARCH_DOMAIN

Specifies a DNS search domain to use when resolving hostnames inside the container. This property takes one or more domain
                                             names as arguments, separated by commas.

In this example, the DNS search domain is example.com . Inside the container, the DNS resolver appends the search domain to the hostname and attempts to resolve it. If you ping
                                             the webserver inside the container, the DNS resolver tries to resolve webserver.example.com ; if that fails, it tries to resolve webserver .

Default: search.domain.1|search.domain.2

Yes

—

PROXY_BINDING_IP

Running multiple proxy containers on the same host can be supported by using multiple DNS hostnames mapped to distinct IP
                                             addresses on that host. These addresses must be configured on the same external NIC used for the reverse proxy container during
                                             the install_os_settings.sh configuration. Specify one of the external NIC's IP addresses as the PROXY_BINDING_IP. This setup
                                             ensures that traffic intended for a specific hostname is directed to the container bound to the corresponding IP address.

For example, if the external NIC is ens192 with IP addresses 192.168.1.69 and 192.168.1.70, use 192.168.1.69 as the PROXY_BINDING_IP
                                             for one container and 192.168.1.70 for the other container.

Default: No value

Yes, if required.

By default, if the external NIC is configured with a single IP address, the installer automatically uses that value, and there
                                             is no need to explicitly specify it. However, if the external NIC has multiple IP addresses, the PROXY_BINDING_IP field must
                                             be populated with one of those IP addresses.

PROXY_BINDING_INTERNAL_IP

Specify the internal IP that will be used for accessing the reverse proxy container.

Default: No value

Only if required.

When there are more than one internal IP configured in the system.

When you want to access the reverse proxy container through a specific internal IP.

CREATE_SELF_SIGNED_SSL_CERT

Specifies whether to create a self-singed certificate during the reverse-proxy installation.

Default: TRUE

Yes, if required.

If the CA-signed certificates are present, you don't need to install self-signed certificates during the installation. In
                                             this case, change to FALSE.

CERTIFICATE_COMMON_NAME

Specifies the common name for the certificate.

This value is required to create self-signed certificates. Used on the next property.

Default: *.cisco.com

Yes, if required.

Required only for creating self-singed certificates.

CERTIFICATE_SUBJECT

Specifies the subject line to be used on the self-signed certificate.

Default: /C=IN/ST=KA/L=BLR/O=Cisco/OU=CCBU/CN=${CERTIFICATE_COMMON_NAME}

Yes, if required.

Required only for creating self-singed certificates.

SSL_CERT_NAME

Specifies the name of the certificate file to be auto-generated.

Default: reverseproxy.crt

Yes, If required.

Required only for creating self-singed certificates.

SSL_KEY_NAME

Specifies the name of the key file to be auto-generated.

Default: reverseproxy.key

Yes, if required.

Required only for creating self-singed certificates.

SSL_CERT_KEY_LENGTH

Specifies the certificate key length to create the self-signed certificate.

Default: 2048

Yes, if required.

Required only for creating self-singed certificates.

SSL_CERT_EXPIRY_IN_DAYS

Certificate expiry in days, to be specified in the self-signed certificate.

Default: 1095

Yes, if required.

Required only for creating self-singed certificates.

AUTO_RESTART_CONTAINER

Toggles auto-restart of the reverse-proxy container when the host system reboots.

Default: 0

Yes

Enable this property only when the reverse-proxy is in working condition.

NOFILE_LIMIT

Specifies the initial and maximum number of open file descriptors that a container can have.

Option in Podman is used to set system resource limits on a container.

Default: nofile=102400:102400

Yes, if required.

nofile=204800:204800 for a 4000 deployment.

CPU_LIMIT

Specifies the number of CPUs that a container can use.

Default: 2

Yes, if required.

MEM_LIMIT

Specifies the maximum amount of memory that a container can use, in bytes or using a human-readable format.

Default: 4G

Yes, if required.

MEM_SWAP_LIMIT

Specifies the maximum amount of memory and swap for a container—in bytes or using a human-readable format such as 1G for 1
                                             gigabyte.

Default: 8G

Yes, if required.

MEM_RES

Sets a soft limit on the minimum amount of memory to be available for the container.

Default: 2G

Yes, if required.

Ensure that the host has adequate resources to run the container with the modified resource constraints.

#### Installer env properties that aren’t recommended to be altered

These properties are provided for reference and they are available in the configuration to provide flexibility, to adjust
                                             the behavior if necessary, and in exceptional situations. It isn't recommended to change casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

CONTAINER_IMAGE

A container image is a read-only template that contains a set of instructions for creating a container and defining the resources
                                          within the container.

Default: reverse-proxy-openresty-container:12.6(2)

No

Never

HOST_WORKING_DIR

Specifies the working directory of the container

Default: ~/reverse_proxy/${CONTAINER_NAME}

No

NGX_HOME

Specifies the home directory of the NGINX server inside the container.

Default: /usr/local/openresty/NGINX

No

HOST_CACHE_VOL

Specifies the host system directory used to mount on the container. 3 Mapped with the following container directory: NGX_CACHE_DIR.

Default: ${HOST_WORKING_DIR}/cache

No

HOST_SSL_VOL

Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_SSL_DIR

Default: ${HOST_WORKING_DIR}/ssl

No

HOST_LOGS_VOL

Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_LOG_DIR

Default: ${HOST_WORKING_DIR}/logs

No

HOST_CONF_VOL

Specifies the host system directory used to mount on the container. Mapped with the container directory mentioned here: NGX_CONF_DIR

Default: ${HOST_WORKING_DIR}/conf

No

HOST_HTML_VOL

Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_HTML_DIR

Default: ${HOST_WORKING_DIR}/html

No

HOST_LUA_VOL

Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_LUA_DIR

Default: ${HOST_WORKING_DIR}/lua

No

NGX_CACHE_DIR

Specifies the container directory location mapped with the corresponding host system directory specified in the HOST_CACHE_VOL
                                          property.

Default: ${NGX_HOME}/cache

No

NGX_SSL_DIR

Specifies the container directory location mapped with the corresponding host system directory mentioned in the HOST_LOGS_VOL
                                          property.

Default: ${NGX_HOME}/ssl

No

NGX_LOG_DIR

Specifies the container directory location mapped with the corresponding host system directory mentioned in the HOST_LOGS_VOL
                                          property.

Default: ${NGX_HOME}/logs

No

NGX_CONF_DIR

Specifies the container directory location mapped with the corresponding host system's directory mentioned in the HOST_CONF_VOL
                                          property.

Default: ${NGX_HOME}/conf

No

NGX_HTML_DIR

Specifies the container directory location mapped with the corresponding host system directory mentioned in the HOST_HTML_VOL
                                          property.

Default: ${NGX_HOME}/html

No

NGX_LUA_DIR

Specifies the container's directory location mapped with the corresponding host system's directory mentioned on this property
                                          HOST_LUA_VOL.

Default: ${NGX_HOME}/lua

No

MEM_SWAPPINESS

Controls how aggressively the kernel should swap memory pages of the container to disk when the container exceeds its memory
                                          limit.

Default: 1

No

NGX_USER_USERID

The Reverse Proxy Installer generates a new user ID to start the reverse proxy container, which will run under this user.

Default: nginxuser

No

NGX_USER_UID

The UID to be assigned to 'nginxuser'.

Default: 9876

No.

If UID 9876 is already assigned to another user, you can update it to the next available UID.

NGX_USER_USERGROUP

The user group created to map to nginxuser.

Default: nginxusergroup

No

LOAD_CONTAINER_IMAGE_FROM_TAR

This property is commented out by default.

The default value (when it’s commented) is true.

Default: This property is commented by default.

No

You can change the value to load the container image from a different location.

REVERSE_PROXY_CONTAINER_IMAGE_TAR

Specifies the location of the container image tar file.

This property is commented out by default. ${SCRIPTPATH} is the location of the proxy_launcher.sh script.

Default:

${SCRIPTPATH}//reverse-proxy-openresty-container/reverse-proxy-openresty-container.tar.gz

No

#### Core properties

These are the basic properties that determine the behavior of the included OpenResty® Nginx proxy and control various aspects
                                    of its runtime behavior. It also contains request rates and various cache sizes setting for Nginx.

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_JWT_SECRET

OpenResty® Constants(defined in maps.conf) configuration. JWT secret pulled from IdS host using CLI "show ids secret"

This secret is used to verify and validate tokens at proxy for authentication in SSO mode

This secret is applicable only for IdS < 12.6(2).

Default: TWSFbB9J6fBnu/D/hrHiQl2O0WEgrVj69ZiHJCtwahI=

Yes, if IdS is running in < 12.6(2) version

Update it with the output of this command from IdS:

"show ids secret"

Yes

NGX_SYSLOG_SVR_IP

Specifies the syslog server IP to which NGINX pushes some specific notification logs when the access for an IP is blocked.

Default: 127.0.0.1

Yes, if necessary.

The current syslog server is the current reverse-proxy. This can be changed to the IP for any syslog server, based on the
                                                configuration.

Yes

NGX_VALID_REFERRERS

Specifies the “Referrer” request header field values for which the request is allowed. Request is blocked for all other referrers.
                                                The value is case-sensitive.

Include all reverse-proxy hostnames, IdS hostnames and ADFS hostname in this list. They are required for reverse-proxy and
                                                other functionality.

Default:

proxy_pub.host.domain|proxy_sub.host.domain|

ids_pub.host.domain|ids_sub.host.domain|adfs.host.domain

Yes

If not updated, the pages return with 417 HTTP error code. Make sure there are no typos in the hostnames.

Yes

NGX_LOCALHOST_IPS

Specifies the list of IPs assigned to the reverse-proxy host across all NICs. Include all public and private IPs for reverse-proxy
                                                in this list. Include the alternate side reverse-proxy's IP addresses as well.

Default: 192.168.1.69|192.168.1.169

Yes

Update all the reverse-proxy IPs here.

Yes

NGX_RATELIMIT_DISABLE_IPS

Specifies a list of IP addresses for which rate limits aren't applied.

Default: 192.168.1.69|192.168.1.169|127.0.0.1

All the IP address that should be allowed to exclude on rate-limiting.

Update the list with all the public and private IPs of both the primary and secondary reverse-proxy. It can also include any
                                                other load balancer or proxy which are forwarding requests to reverse-proxy.

Yes

NGX_LOAD_BALANCER_IPS

Hostnames aren’t supported as a permissible value in NGX_LOAD_BALANCER_IPS

The list of entries should be | separated

# Example: "192.162.1.0/24|10.78.95.76"

Alternatively, if the internet client connection is stopped at the reverse-proxy directly, these variables MUST be empty.

Yes, if required.

If the load balancer forwards requests to the reverse-proxy, populate with the load balancer IP addresses.

No

NGX_LOAD_BALANCER_REAL_IP_HEADER

Devices must also send the end client IP alone, in a custom header.

Add the name of the custom header used for this purpose to the NGX_LOAD_BALANCER_REAL_IP_HEADER variable. For example, " X-Real-IP ".

If you use the X-Forwarded-For as the field used to detect the client IP, include all trusted devices that can appear in this list in the NGX_LOAD_BALANCER_IPS
                                                variable. The first untrusted IP encountered is used as the client IP. We don't recommend using this field ( X-Forwarded-For ) for detecting the client IP.

Yes, if required.

No

NGX_ERR_LOG_LEVEL

The log level of the error.log file can be set to debug, info, alert, warn, error, crit, or emerg. Messages from the specified level and all higher severity
                                                levels will be logged.

Default: info

Yes, if required.

The log level can be set to debug for troubleshooting purposes. But, it is not recommended to maintain this setting for an
                                                extended period, as it may generate a large amount of log data.

Yes

##### Core properties that are not recommended to be altered

These properties are provided for reference and they are available in the configuration, to provide flexibility and adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended to be changed casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

NGX_NUM_WKR_PRC

OpenResty® NGINX core configurations.

Specifies the number of worker processes. The value "auto" uses the number of available CPU cores.

Default: auto

No

NGX_PID_FILE

Defines a file that stores the process ID of the main process.

Default: openresty.pid

No

NGX_WKR_CPU_AFFINITY

Binds the worker processes to the sets of CPUs. The value "auto" binds worker processes automatically to the available CPUs.

Default: auto

No

NGX_WKR_PRIORITY

Defines the scheduling priority for worker processes like it’s done by the nice command. A negative number means higher priority.
                                                The allowed range varies from -20 to 20.

Default: 0

No

NGX_NUM_RLIMIT

Changes the limit on the maximum number of open files (RLIMIT_NOFILE) for worker processes. Used to increase the limit without
                                                restarting the main process.

Default: 102400

No

NGX_MULTI_ACCEPT

If multi_accept is disabled, a worker process accepts one new connection at a time. Otherwise, a worker process accepts all
                                                new connections at a time.

Default: on

No

NGX_NUM_WKR_CONN

Specifies the maximum number of simultaneous connections that can be opened by a worker process.

Default: 10240

No

NGX_SEND_FILE

Enables or disables the use of sendfile .

No

No

NGX_TCP_NOPUSH

Enables or disables the use of the TCP_NOPUSH socket option on FreeBSD or the TCP_CORK socket option on Linux. The options
                                                are enabled only when the sendfile is used.

Default: on

No

NGX_MAP_HASH_BUCKET_SIZE

Specifies the bucket size for the map variables hash tables.

Default: 128

No

NGX_SERVERNAMES_HASH_BUCKET_SIZE

Specifies the bucket size for the server names hash tables.

Default: 512

No

NGX_JWT_EXPIRY

Specifies the JWT token expiry in seconds as configured in the IdS host.

Token cache expiry time in reverse-proxy. Reverse-proxy keeps the cached token for 2 hours for the default configuration of
                                                1-hour access token expiry time configured in IdS.

Default: 7200

No

NGX_IDS_PUBLIC_KEY_POLL_INTERVAL

Specifies the IdS public key poll frequency in seconds.

The frequency at which reverse-proxy polls the ids to get the public key value. The default is once in 5 minutes.

Default: 300

No

NGX_CLIENT_LOCK_THRESHOLD

If the threshold to detect DoS attacks is crossed in the specified interval, the client IP is blocked for the specified duration.

Default: 5

No

NGX_CLIENT_LOCK_DURATION

Specifies the request authorization failure threshold over a given interval for a source IP.

Default: 30

No

NGX_CLIENT_BLOCK_DURATION

Specifies the duration of blocking (in seconds) for clients to avoid brute force attacks.

The block duration for the client IP is 30 minutes.

Default: 1800

No

NGX_SYSLOG_SVR_PORT

Specifies the port for the syslog server.

Default: 514

No

Usually the syslog server listens on 514, if the syslog server is configured to listen on some other port then this can be
                                                changed.

NGX_LOG_FILE

Specifies the OpenResty® logging file.

Default: access.log

No

NGX_LOG_FORMAT

Specifies the OpenResty® NGINX access log format name as specified in logging.conf.

Default: info

No

Not recommended to change on a production system. You can change it to the debug format in LAB setup for more detailed logging.

NGX_LOG_BUFFER

Specifies the OpenResty® NGINX access log buffer size. When this buffer is full or the flush interval is reached, the system
                                                writes the logs to the disk.

Default: 16k

No

NGX_LOG_FLUSH_INTERVAL

Specifies the OpenResty® NGINX access log flush interval. Logs are written to the disk after this interval is reached or the
                                                log buffer is full.

Default: 30s

No

Not recommended changing on production servers.

For a LAB system, you can reduce this value to 1 to 5s so you can check the access.log file updates immediately.

NGX_PROXY_CACHE_LOCK

Only one request at a time can populate a new cache element identified according to the proxy_cache_key directive by passing a request to the server, which is enabled with reverse-proxy. Other requests of the same cache element
                                                either wait for a response to appear in the cache or the cache lock for this element to be released, up to the time set by
                                                the NGX_PROXY_CACHE_LOCK_TIMEOUT value.

Default: on

No

NGX_PROXY_CACHE_LOCK_TIMEOUT

Specifies the timeout for NGX_PROXY_CACHE_LOCK. When the time expires, the request is passed to the server, which is enabled
                                                with reverse-proxy; however, the response isn't cached.

Default: 30s

No

NGX_PROXY_CACHE_LOCK_AGE

If the last request passed to the server, which is enabled with reverse-proxy, for populating a new cache element hasn’t completed
                                                for the specified time, one more request passes to the server, which is enabled with reverse-proxy.

Default: 5s

No

NGX_PROXY_CACHE_BACKGROUND_UPDATE

Allows starting a background sub request to update an expired cache item, while a stale cached response is returned to the
                                                client.

Default: on

No

NGX_PROXY_CACHE_REVALIDATE

Enables revalidation of expired cache items using conditional requests with the “If-Modified-Since” and “If-None-Match” header
                                                fields.

Default: on

No

NGX_PROXY_CACHE_VALID

Specifies the caching time for 200, 301, and 302 responses.

Default: 24h

No

NGX_VARIABLES_HASH_BUCKET_SIZE

Specifies the bucket size for the variables hash table.

Default: 128

No

NGX_KEEPALIVE_TIMEOUT

Specifies a timeout during which a keep-alive client connection stays open on the server side. The zero value disables keep-alive
                                                client connections.

Default: 20s

No

NGX_SEND_TIMEOUT

Specifies a timeout for transmitting a response to the client. The timeout is set only between two successive write operations,
                                                not for the transmission of the whole response.

Default: 10s

No

NGX_CLIENT_HEADER_TIMEOUT

Specifies the timeout for reading the client request header.

Default: 10s

No

NGX_CLIENT_BODY_TIMEOUT

Specifies a timeout for the reading the client request body. The timeout is set only for a period between two successive read
                                                operations, not for the transmission of the whole request body.

Default: 10s

No

NGX_RESET_TIMEDOUT_CONNECTION

Enables or disables resetting timed out connections and connections closed with the non-standard code 444.

Default: on

No

NGX_CLIENT_HEADER_BUFFER_SIZE

Specifies the buffer size for reading the client request header.

Default: 4K

No

NGX_CLIENT_BODY_BUFFER_SIZE

Specifies the buffer size for reading the client request body.

Default: 2k

No

NGX_CLIENT_MAX_BODY_SIZE

Specifies the maximum allowed size of the client request body.

Default: 15m

No

NGX_LARGE_CLIENT_HEADER_BUFFER_NUM

Specifies the maximum number of buffers used for reading a large client request header. Buffers are allocated only on demand.

Default: 2

No

NGX_LARGE_CLIENT_HEADER_BUFFER_SIZE

Specifies the maximum size of buffers used for reading a large client request header. A request line can’t exceed the size
                                                of one buffer. Buffers are allocated only on demand.

Default: 8K

No

NGX_UNDERSCORES_IN_HEADERS

Enables or disables the use of underscores in client request header fields.

Default: on

No

NGX_KEEPALIVE_REQUESTS

Specifies the maximum number of requests that are served through one keep-alive connection.

After the maximum number of requests are made, the connection is closed.

Default: 500

No

NGX_HTTP2_MAX_CONCURRENT_STREAMS

Specifies the maximum number of concurrent HTTP/2 streams in a connection.

Default: 150

No

NGX_SERVER_TOKENS

Enables or disables emitting NGINX version on error pages and in the “Server” response header field.

Default: off

No

NGX_LIMIT_CONN_DRY_RUN

Enables the dry-run mode for limiting HTTP connections. In this mode, the number of connections isn’t limited. However, in
                                                the shared memory zone, the number of excessive connections is considered as usual.

Default: off

No

On a production system, this should be always "off".

If the system is running in lab mode, you can toggle this "on" to avoid rate limiting.

NGX_LIMIT_REQ_DRY_RUN

Enables the dry-run mode for limiting HTTP requests. In this mode, the number of connections isn’t limited, however, in the
                                                shared memory zone, the number of excessive connections is considered as usual.

Default: off

No

On a production setup, this should be always "off".

If the system is running in lab mode, you can toggle this "on" to avoid rate limiting.

NGX_LIMIT_CONN_LOG_LEVEL

Specifies the desired logging level for cases when the server limits the number of connections.

Default: error

No

NGX_LIMIT_REQ_LOG_LEVEL

Specifies the desired logging level for cases when the server refuses to process requests due to rate exceeding, or delays
                                                request processing.

Default: error

No

NGX_LIMIT_REQ_STATUS

Specifies the status code to return in response to rejected requests due to HTTP request rate limits.

This is the standard HTTP error code for rate-limiting errors.

Default: 429

No

NGX_LIMIT_CONN_STATUS

Specifies the status code to return in response to rejected requests due to HTTP connection rate limits.

Default: 503

No

Error code returned when the connection limits are reached.

NGX_CHAT_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for chat access.

Default: 30r/s

No

NGX_IDS_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for IdS access.

Default: 5r/s

No

NGX_FIN_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for Finesse access.

Default: 90r/s

No

NGX_FIN_CLIENT_LOG_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for Finesse client log requests.

Default: 5r/s

No

NGX_FIN_SSO_VALVE_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for Finesse SSO valve requests.

Default: 5r/s

No

NGX_CUIC_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for CUIC access.

Default: 50r/s

No

NGX_CUIC_HISTORICAL_REPORT_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for CUIC historical report requests.

Default: 16r/s

No

NGX_CUIC_REALTIME_REPORT_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for CUIC realtime report requests.

Default: 48r/s

No

NGX_CUIC_REPORT_EXECUTION_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for CUIC report execution requests.

Default: 12r/s

No

NGX_LIVEDATA_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for livedata access.

Default: 25r/s

No

NGX_CLOUDCONNECT_DR_TASK_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for DR API task request access.

Default: 100r/s

No

NGX_CLOUDCONNECT_USER_SYNC_CALLBACK_REQUEST_RATE_LIMIT

Specifies the HTTP request rate limit for user sync callback request access.

Default: 5r/m

No

NGX_PRXY_STATIC_FILES_PORT

Specifies the OpenResty® static content configuration. The reverse-proxy port is used to serve static files under the HTML
                                                directory.

Default: 10000

This location serves the proxy-map information. You can change the port number if necessary.

NGX_PRXY_STATUS_IP

Specifies the reverse-proxy IP used to access OpenResty® NGINX stats over the "/reverseproxy_status" endpoint

Internal request is accessible from only the host system.

Default: 127.0.0.1

NGX_PRXY_STATUS_PORT

Specifies the reverse-proxy port used to access OpenResty® NGINX stats over the "/reverseproxy_status" endpoint.

Default: 10001

No

NGX_USERTIMERTHREAD_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100k

No

NGX_USERLIST_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 50m

No

NGX_CREDENTIALSSTORE_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100m

No

NGX_USERCOUNT_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100k

No

NGX_CLIENTSTORAGE_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100m

No

NGX_BLOCKINGRESOURCES_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100m

No

NGX_TOKENCACHE_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 10m

No

NGX_IPSTORE_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 10m

No

NGX_DESKTOPURLLIST_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 10m

No

NGX_DESKTOPURLCOUNT_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100k

No

NGX_THIRDPARTYGADGETURLLIST_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100m

No

NGX_THIRDPARTYGADGETURLCOUNT_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100k

No

NGX_CORSHEADERSSTORE_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100k

No

NGX_TIMERTHREADSSTORE_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100k

No

NGX_ALTERNATE_HOSTS_SHRD_DICT_SIZE

Specifies the LUA shared dictionary sizes used by reverse-proxy internally.

Default: 100k

No

NGX_VALID_USER_AGENTS_REGEX

Defines the valid User-Agent regular expression that the reverse proxy permits.

Default: ~*(^Mozilla/5\.0 .*(Firefox|Chrome|Edg|Safari)/[0-9]+)

No

The regular expression includes all valid User-Agent values that are sent by browsers when accessed through the list of browsers
                                                supported by Cisco. If necessary, you can modify the regular expression to accommodate additional browser types.

NGX_USE_REGEX_TO_VALIDATE_USER_AGENT

If set to true, user agent validation is based on the NGX_VALID_USER_AGENTS_REGEX value; otherwise, it falls back to the default
                                                block list to block invalid user agents.

Default: true

No

This property can be set to false if the user agent check should be performed based on the block list instead of NGX_VALID_USER_AGENTS_REGEX.

## Directory (DIR) properties

The following table lists the directory properties and the default values for various OpenResty® folders.

These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                          the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

NGX_CACHE_DIR

Specifies the cache directory where various resources for components are cached.

Default: ${NGX_HOME}/cache

No

NGX_CONF_DIR

Specifies the OpenResty® directory containing NGINX configurations, such as core and component configurations.

Default: ${NGX_HOME}/conf

No

NGX_HOME

Specifies the home directory for OpenResty® nginx installation.

Default: /usr/local/openresty/nginx

No

NGX_HTML_DIR

Specifies the OpenResty® directory

Default: ${NGX_HOME}/html

Directory containing static resources.

No

NGX_LOG_DIR

Specifies the OpenResty® directory where OpenResty® logs are stored.

Default: ${NGX_HOME}/logs

No

NGX_LUA_DIR

Specifies the OpenResty® directory containing lua resources.

Default: ${NGX_HOME}/lua

No

NGX_SSL_DIR

Specifies the OpenResty® directory containing SSL resources like certs and keys.

Default: ${NGX_HOME}/ssl

No

### Common Properties

## Common SSL-Related Properties

The following table lists SSL-related properties that are common across components.

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_SSL_TRUST_CRT

Specifies a file with trusted CA certificates in the PEM format used to verify the certificate of the Finesse HTTPS server,
                                          which is enabled for reverse-proxy.

Default: ${NGX_SSL_DIR}/upstreams_finesse_trust.crt

Yes, if necessary.

Point to the exact location of upstream Finesse's certificate for mutual trust establishment.

No

NGX_SSL_CRT

SSL connector configuration for the component access.

Specifies the location of a file with the certificate, for the given component, in the PEM format.

Default: ${NGX_SSL_DIR}/reverseproxy.crt

Yes, if necessary.

Update the location of the Finesse reverse-proxy certificate.

No

NGX_SSL_KEY

Specifies the location of a file with the secret key, for the given component, in the PEM format.

Default: ${NGX_SSL_DIR}/reverseproxy.key

Yes, if necessary.

If the location of the file changes.

No

### Common SSL-Related properties that are not recommended to be altered

These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                          the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

#NGX_SSL_DHPARAM

Specifies a file with DH parameters for DHE ciphers.

Default: ${NGX_SSL_DIR}/dhparam.pem

This property is disabled by default. Uncomment the parameter to use it.

No.

Can be changed if necessary.

Enable for more security, to prevent affecting by an attack exploiting the Logjam vulnerability.

For more information, see Understanding Logjam and Future-Proofing Your Infrastructure at:

https://cisco.blogs.com

NGX_PRXY_SSL_VERIFY

Enables or disables verification of the HTTPS server certificate, which is enabled for reverse-proxy.

Default: on

No

Changing this to off disables SSL verification of the requests.

NGX_PRXY_SSL_VERIFY_DEPTH

Specifies the verification depth in the HTTPS server certificates chain, which is enabled for reverse-proxy.

This is for DoS prevention. Building the chain might be an exponential algorithm with backoff, so with the openssl default
                                       of 100 a malicious backend might cause denial of service in nginx.

Default: 10; less than 4 is easy to break.

No

NGX_SSL_CACHE_SIZE

Specifies the SSL session cache size for session parameters storage for client connections.

This cache is shared between all worker processes. The cache size is specified in bytes; one megabyte can store about 4000
                                       sessions. Each shared cache should have an arbitrary name.

Default: 10m

No

NGX_SSL_CIPHERS

Specifies the OpenSSL format for enabled ciphers.

Default: EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH

No

This list contains all the strong ciphers available. You can update the list if ciphers are found to be vulnerable or to add
                                       new supported ciphers.

NGX_SSL_PRFR_SRVR_CIPHERS

Prefer server ciphers over client ciphers.

Default: on

No

NGX_SSL_PROTO

Specifies the TLS versions enabled for the connections. To specify multiple values, use space delimiters.

# Example: NGX_SSL_PROTO="TLSv1 TLSv1.1 TLSv1.2"

Generally TLS version 1.2 is supported for the webapp requests. TLS v1 and TLS v1.1 aren’t recommended.

Default: TLSv1.2

No

NGX_SSL_SESSION_TICKETS

Enables or disables session resumption through TLS session tickets.

Default: off

No

NGX_SSL_SSN_TIMEOUT

Specifies a time during which a client may reuse the session parameters—how long each session lives in reverse-proxy.

Default: 30m

No

NGX_SSL_STAPLING

Enables or disables stapling of OCSP responses by the server.

SSL stapling means that revocation information about the servers certificate (that is, the OCSP response) are included in
                                       the TLS handshake together with the server certificate.

Default: off

No

NGX_SSL_STAPLING_VERIFY

Enables or disables the verification of OCSP responses by the server.

Allows the presenter of a certificate to bear the resource cost involved in providing OCSP responses by appending ("stapling")
                                       a time-stamped OCSP response signed by the CA to the initial TLS handshake, eliminating the need for clients to contact the
                                       CA".

Default: off

No

### Cisco Finesse Properties

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_FIN_HOSTNAME

Reverse proxy hostname through which this Finesse host is accessed.

Default: reverseproxy.host.domain

Yes

No

NGX_PRXY_ALT_FIN_HOSTNAME

Specifies the reverse proxy hostname for the Finesse failover node associated with this Finesse host. This should reference
                                             the reverse proxy node on the alternate side.

Default: Empty

Yes, if required.

While deploying the secondary reverse proxy in a high availability mode.

No

NGX_PRXY_FIN_PORT

Specifies the reverse proxy port over which this Finesse host are accessed.

Default: 8445

Yes, if necessary.

No

NGX_PRXY_ALT_FIN_PORT

Specifies the reverse proxy port for the Finesse failover node associated with this Finesse host. This should reference the
                                             reverse proxy node on the alternate side.

Default: Empty

Yes, if required.

While deploying the secondary reverse proxy in a high availability mode.

No

NGX_FIN_HOSTNAME

Specifies the upstream Finesse hostname.

Default: finesse.host.domain

Yes

New installation or if the hostname of the Finesse box changes.

No

NGX_ALT_FIN_HOSTNAME

Specifies the finesse hostname for the alternate side.

Default: Empty

Yes, if required.

While deploying secondary finesse node in a high availability mode.

No

NGX_AUTH_URL

Specifies the Finesse URL to fetch the users list to perform authentication at proxy.

Default: https://reverseproxy.host.domain:8445/finesse/api/UserAuth

Yes

Replace "reverseproxy.host.domain" with the FQDN of the reverse proxy.

No

NGX_AUTHENTICATE_WEBSOCKET

Specifies how to enable the authentication of websocket request.

Default: true

No

When websocket authentication needs to be disabled, you can change the value to false.

If the value is false, to mitigate the possible DoS attack, reverse proxy performs specific checks before allowing the websocket
                                             connections. Accept the websocket connections only from those IP addresses that have successfully made an authenticated REST
                                             request. Authenticate the REST request before establishing the websocket connection.

Reverse proxy deployments that use L7 intermediaries, such as Content Delivery Network (CDN), often redirect traffic through
                                             interim servers before the traffic reaches the reverse proxy. In such deployments, ensure X-Forwarded-For headers are correctly relayed to identify the client’s IP address. The X-Forwarded-For headers are used to authenticate the websocket connection by matching it with the previously authenticated REST request.

If you set the default value to false, the attempt to create the websocket connections before issuing any REST request displays
                                                         an Authorization Failed error message. The authentication check done by the reverse proxy gets disabled, but the XMPP authentication is done upstream.

Yes

NGX_FIN_USERS_URL

If the externally accessible FQDN of the reverse proxy differs from its internal FQDN, this field should be filled in. For
                                             example, NGX_FIN_USERS_URL="https://internal-reverseproxyhostname.cisco.com:8445/finesse/api/Users". If the external and internal
                                             FQDNs of the reverse proxy are the same, this field can be left blank.

Default: Empty

Yes, if required.

External FQDN of the reverse proxy does not match the internal FQDN of the reverse proxy.

Yes

#### Cisco Finesse properties that are not recommended to be altered

These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                             if necessary, in exceptional situations and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

NGX_FIN_UPSTREAM_KEEPALIVE

Specifies the proxy backend configurations for Finesse, and activates the cache for connections to an upstream IdS server.
                                          The value sets the maximum number of idle keep-alive connections to upstream servers that are preserved in the cache of each
                                          worker process. When this number is exceeded, the least recently used connections are closed.

Default: 128

No

This default is the optimal value for keeping alive the upstream connection per component.

NGX_SET_UPSTREAM_MAX_CONNS

To set the maximum connection limit for upstream components.

Default: true

No

You can set the value to false when you want to remove the upstream maximum connection limit. Restart the container for the
                                          change to take effect.

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, Finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                          and idp-adfs3.

Default: Finesse

No

Never

NGX_FIN_DESKTOP_CACHE_SIZE

Specifies the proxy cache configuration for the Finesse desktop and the initial size of the Finesse desktop endpoints cache.

Default: 10m

No

The default is the optimal value.

NGX_FIN_DESKTOP_CACHE_MAX_SIZE

Specifies the maximum size for the Finesse desktop endpoints cache. When the size exceeds or there isn’t enough free space,
                                          it removes the least recently used data.

Default: 50m

No

The default is the optimal value.

NGX_FIN_DESKTOP_CACHE_INACTIVE_DURATION

Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that is not accessed during the
                                          time specified gets removed from the cache regardless of their duration.

Default: 3y

No

The default is the optimal value.

After this time, the cache contents expire.

NGX_FIN_SHINDIG_CACHE_SIZE

Specifies the proxy cache configuration for Finesse Shindig and the initial size of the Finesse Shindig endpoints cache.

Default: 10m

No

NGX_FIN_SHINDIG_CACHE_MAX_SIZE

Max size for Finesse shindig endpoints cache. When the size exceeds or there isn’t enough free space, it removes the least
                                          recently used data.

Default: 500m

No

NGX_FIN_SHINDIG_CACHE_INACTIVE_DURATION

Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that aren’t accessed during the
                                          time specified get removed from the cache regardless of their freshness.

Default: 3y

No

NGX_FIN_OPENFIRE_CACHE_SIZE

Specifies the initial size of the Finesse openfire endpoints cache.

Default: 10m

No

NGX_FIN_OPENFIRE_CACHE_MAX_SIZE

Specifies the maximum size for the Finesse openfire endpoints cache. When the size exceeds or there isn’t enough free space,
                                          it removes the least recently used data.

Default: 10m

No

NGX_FIN_OPENFIRE_CACHE_INACTIVE_DURATION

Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that is not accessed during the
                                          time specified is removed from the cache regardless of their duration.

Default: 3y

No

NGX_FIN_REST_CACHE_SIZE

Specifies the initial size of the Finesse REST endpoints cache

Default: 10m

No

NGX_FIN_REST_CACHE_MAX_SIZE

Specifies the maximum size for the Finesse REST endpoints cache. When the size exceeds or there isn’t enough free space, it
                                          removes the least recently used data.

Default: 1500m

No

NGX_FIN_REST_CACHE_INACTIVE_DURATION

Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that is not accessed during the
                                          time specified, get removed from the cache regardless of their duration.

Default: 40m

No

NGX_FIN_LAYOUT_CACHE_SIZE

Specifies the initial size of the Finesse layout endpoints cache.

Default: 150m

No

NGX_FIN_LAYOUT_CACHE_MAX_SIZE

Specifies the maximum size for the Finesse layout endpoints cache. When the size exceeds or there isn’t enough free space,
                                          the system removes the least recently used data.

Default: 300m

No

NGX_FIN_LAYOUT_CACHE_INACTIVE_DURATION

Specifies the inactive duration for content stored in the Finesse desktop endpoints cache. Cached data that aren’t accessed
                                          during the time specified get removed from the cache regardless of their duration.

Default: 40m

No

NGX_FIN_HTTP1_CONN_LIMIT

Specifies the number of concurrent HTTP/1.1 connections allowed per source IP

Default: 12

No

NGX_FIN_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 150

No

NGX_FIN_DESKTOP_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for desktop endpoints

Default: 50

No

NGX_FIN_SHINDIG_CORE_RPC_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for shindig rpc endpoints

Default: 40

No

NGX_FIN_SHINDIG_IFR_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for shindig ifr endpoints

Default: 30

No

NGX_FIN_SSOVALVE_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for SSO valve endpoints

Default: 5

No

NGX_FIN_LIMIT_REQ_STATUS

Specifies the HTTP response code to return when the HTTP request rate reaches the limit

Default: 429

No

NGX_FIN_PROXY_BUFFER_SIZE

Specifies the size of the buffer used for reading the first part of the response received from the server, which is enabled
                                          for reverse proxy.

Configurations are overridden from the common config for Finesse.

Default: 8k

No

NGX_FIN_MAX_TEMP_FILE_SIZE

Applies when buffering of responses from the server (which is enabled for reverse proxy) is enabled. If the whole response
                                          doesn't fit into the buffers set by the NGX_FIN_PROXY_BUFFER_SIZE, the system saves part of the response in a temporary file.

Default: 100m

No

#### Chat properties

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_CHAT_PORT

Specifies the reverse-proxy port over which this chat server is accessed.

Default: 5280

Yes, if necessary.

No

NGX_PRXY_CHAT_HOSTNAME

Specifies the reverse-proxy hostname over which this chat server is accessed.

Default: reverseproxy.host.domain

Yes

No

NGX_CHAT_HOSTNAME

Specifies the hostname of the chat server.

Default: chat1.host.domain

Yes

New installation or if the host name of the upstream chat server changes.

No

NGX_CHAT_HOST[1-8]_PROXY

Required for substituting user home and backup node information in the log-in response.

(Similar keys configurations exist for 4 HA clusters of chat servers.)

Default: reverseproxy.host.domain:5280/reverseproxy-sub.host.domain:15280

Yes

New installation or if the chat server proxy hostname FQDN changes.

No

NGX_CHAT_HOST[1-8]

Specifies the proxy access information for all chat nodes in the deployment. Required for substituting user home and backup
                                                node information in the log-in response.

(Similar keys configurations exist for 4 HA clusters of chat servers.)

Default: chat[1-4].host.domain/chat[1-4]-sub.host.domain

Yes

New installation or if the chat server upstream hostname FQDN changes.

No

NGX_CHAT_BIND_PATH

Specifies the binding URL for the chat server.

Default: httpbinding

Yes

If the binding URL for the chat server changes.

No

NGX_AUTH_URL

Specifies the Finesse URL to fetch the users list to perform authentication at proxy.

Default: https://proxy.host.domain:8445/finesse/api/UserAuth

Yes

New installation or if proxy.host.domain is the hostname of the the reverse-proxy.

No

##### Chat properties that are not recommended to be altered

These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended for changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata.

Default: chat

No

NGX_CHAT_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit.

Default: 10

No

NGX_CHAT_PORT

Specifies the port for the chat server.

Default: 5280

No

New installation or if the port number for the upstream chat server is different.

NGX_CHAT_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 30

No

NGX_CHAT_HTTP1_CONN_LIMIT

Specifies the rate limit for desktop chat, the number of concurrent HTTP/1.1 connections allowed per source IP.

Default: 6

No

#### Cloud Connect properties

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_CLOUDCONNECT_PORT

Specifies the reverse-proxy port over which this Cloud Connect server is accessed.

Default: 443

Yes, if necessary.

If there is a change in the port number.

No

NGX_PRXY_CLOUDCONNECT_HOSTNAME

Specifies the reverse-proxy hostname over which this Cloud Connect server is accessed.

Default: reverseproxy.host.domain

Yes

If there is a change in the chat hostname of the reverse-proxy that has must accessed from the internet.

No

NGX_CLOUDCONNECT_HOSTNAME

Specifies the hostname for the Cloud Connect server and the hostname of the Publisher or Primary Cloud Connect node. (Conversely
                                                on the alternate side)

Default: cloudconnect.host.domain

Yes

If there is a change in the FQDN for the upstream Cloud Connect server.

No

NGX_CLOUDCONNECT_FAILOVER_HOSTNAME

Specifies the hostname of the Cloud Connect failover node and the hostname of the Subscriber or Secondary Cloud Connect node.
                                                (Conversely on the alternate side)

Default: cloudconnct.failover.hostname

Yes

If there is change in the FQDN of the alternate Cloud Connect server.

No

NGX_CLOUDCONNECT_CLIENT_IPS

Creates a list of known IP addresses for clients connecting to Cloud Connect services like DigitalRouting and UserSync.

Default:

35.161.238.252|35.166.68.236|34.240.73.178|3.9.155.97|54.206.189.15|52.62.185.51|

13.210.45.137|52.40.46.90|52.214.81.91|3.9.151.19|3.105.22.233|52.17.23.194

Yes

Validate and update the list when there is a change in the IP addresses.

Yes

##### Cloud Connect properties that are not recommended to be altered

These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                                if necessary, in exceptional situations and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3.

Default: cloudconnect

No

NGX_CLOUDCONNECT_USER_SYNC_CALLBACK_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for user sync bulk requests.

Default: 10

No

NGX_CLOUDCONNECT_UPSTREAM_KEEPALIVE

Activates the cache for connections to the upstream Cloud Connect server.

Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections close.

Default: 150

No

NGX_CLOUDCONNECT_LIMIT_REQ_STATUS

Specifies the HTTP response code to return when the HTTP request rate reaches the limit.

Default: 429

No

NGX_CLOUDCONNECT_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 250

No

NGX_CLOUDCONNECT_HTTP1_CONN_LIMIT

Specifies the number of concurrent HTTP/1.1 connections allowed per source IP—the rate limit for Digital Routing requests.

Default: 50

No

NGX_CLOUDCONNECT_HEALTHCHECK_TIMEOUT

Specifies the timeout for the health check API in milliseconds, if there is a failure.

Default: 2000

No

NGX_CLOUDCONNECT_HEALTHCHECK_SSL_VERIFY

Specifies whether to verify the SSL certificate for health checks.

Default: FALSE

No

NGX_CLOUDCONNECT_HEALTHCHECK_RISE

Specifies the number of successive health check successes before turning up a peer.

Default: 2

No

NGX_CLOUDCONNECT_HEALTHCHECK_RESPONSE_CODES

Generates a comma-separated list of valid HTTP status codes for the health check API.

Default: {200}

No

NGX_CLOUDCONNECT_HEALTHCHECK_INTERVAL

Specifies the interval between health checks in milliseconds.

Default: 2000

No

NGX_CLOUDCONNECT_HEALTHCHECK_FALL

Specifies the number of successive health check failures before turning down a peer.

Default: 2

No

NGX_CLOUDCONNECT_HEALTHCHECK_CONCURRENCY

Specifies the number of concurrent health checks.

Default: 2

No

NGX_CLOUDCONNECT_HEALTHCHECK_API

Specifies the active health check configurations for the DR API. The system uses this URL to check the health of the Cloud
                                             Connect.

Default: /drapi/v1/ping

No

NGX_CLOUDCONNECT_DR_TASK_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for digital routing tasks.

Default: 200

No

#### Cisco IdS properties

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_IDS_HOSTNAME

Specifies the reverse proxy hostname over which this IdS host is accessed.

Default: reverseproxy.host.domain

Yes

New installation or if the reverse proxy IdS hostname changes.

No

NGX_PRXY_ALT_IDS_HOSTNAME

Specifies the reverse proxy hostname for the IdS failover node associated with this IdS host. This should reference the reverse
                                                proxy node on the alternate side.

Default: Empty

Yes, if required.

While deploying the secondary reverse proxy in a high availability mode.

No

NGX_PRXY_IDS_PORT

Specifies the reverse proxy port over which this IdS host is accessed.

Default: 8553

Yes, if required.

New installation or if the reverse proxy port changes.

No

NGX_PRXY_ALT_IDS_PORT

Specifies the reverse proxy port for the IdS failover node associated with this IdS host. This should reference the reverse
                                                proxy node on the alternate side.

Default: Empty

Yes, if required.

While deploying the secondary reverse proxy in a high availability mode.

No

NGX_IDS_HOSTNAME

IdS server actual hostname

Default: ids.host.domain

Yes

New installation or if the FQDN host name of the IdS server changes.

No

NGX_ALT_IDS_HOSTNAME

Specifies the Ids hostname for the alternate side.

Default: Empty

Yes, if required.

While deploying secondary Ids in a high availability mode.

No

##### Cisco IdS properties that are not recommended to be altered

These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                                and idp-adfs3.

Default: ids

No

NGX_IDS_UPSTREAM_KEEPALIVE

Proxy backend configurations for IDS. Activates the cache for connections to the upstream IDP server.

Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                                process. When the count exceeds this number, the least recently used connections close.

Default: 128

No

NGX_IDS_HTTP1_CONN_LIMIT

Rate limits configuration for IdS.

Specifies the number of concurrent HTTP/1.1 connections allowed per source IP.

Default: 4

No

NGX_IDS_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 4

No

NGX_IDS_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit.

Default: 4

No

#### IdP Properties (ADFS 3.0 or 5.0)

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_IDP_HOSTNAME

Specifies the reverse-proxy hostname over which this IdP host will be accessed.

Default: adfs-reverseproxy.host.domain

Yes

New installation or if the FQDN of the reverse-proxy IdP host changes.

No

NGX_PRXY_IDP_PORT

Specifies the reverse-proxy port over which this IdP host will be accessed.

Default: 443

Yes, If required.

New installation or if unchanged, reverse-proxy uses the 443 port for CUIC.

No

NGX_IDP_HOSTNAME

Specifies the CUIC server hostname.

Default: idp.host.domain

Yes

New installation or if the FQDN of the IdP host changes.

No

##### IdP Properties (ADFS 3.0 or 5.0 ) that are not recommended to be altered

These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and are not recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3.

Default: idp-adfs3

No

NGX_IDP_UPSTREAM_KEEPALIVE

Proxy backend configurations for IDP. Activates the cache for connections to upstream IDP server

Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections close.

Default: 128

No

### Live Data Properties

#### LiveData 12.6(1) Properties

Use livedata_12.6(1).env when the upstream Livedata is still on Release12.6(1). Otherwise, use livedata.env.

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_LD_HOSTNAME

Specifies the reverse-proxy hostname over which this LD host is accessed.

Default: reverseproxy.host.domain

Yes

If the reverse-proxy livedata host FQDN changes.

No

NGX_PRXY_LD_PORT

Specifies the reverse-proxy port over which this livedata host is accessed.

Default: 12005

Yes, If required.

If there is a change in the reverse-proxy port for livedata.

No

NGX_PRXY_LD_SCKT_IO_PORT

Specifies the reverse-proxy port over which the socket IO endpoint of this livedata host will be accessed.

Default: 12008

Yes, If required.

If there is a change in the reverse-proxy port for socket IO connections.

No

NGX_LD_HOSTNAME

Specifies the Livedata server hostname.

Default: livedata.host.domain

Yes

If there is a change in the upstream livedata host FQDN.

No

NGX_LD_SIO_UPSTREAM_KEEPALIVE

Activates the cache for connections to the upstream livedata server socketio endpoint.

Default: 128

No

—

No

NGX_LD_BACKEND_FAILOVER

Livedata failover configuration. This is used to translate the location header during failover.

For SideA LiveData, point to SideB LiveData and for SideB Livedata, point to SideA Livedata.

Yes

If there is a change in the FQDN or port.

No

NGX_LD_BACKEND_PROXY_FAILOVER

Livedata proxy failover configuration. Each side points to the other side of the reverse-proxy node.

Yes

If there is a change in the FQDN or port.

No

##### LiveData 12.6(1) properties that are not recommended to be altered

These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3.

Default: livedata_12.6(1)

No

—

NGX_LD_WEB_UPSTREAM_KEEPALIVE

Proxy backend configurations for livedata. Activates the cache for connections to the upstream livedata server.

Specifies the maximum number of idle keep alive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections close.

Default: 128

No

—

NGX_LD_SIO_UPSTREAM_KEEPALIVE

Activates the cache for connections to the upstream livedata server socketio endpoint.

Default: 128

No

—

NGX_LD_HTTP1_CONN_LIMIT

Specifies the number of concurrent HTTP/1.1 connections allowed per source IP.

Default: 12

No

—

NGX_LD_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 150

No

—

NGX_LD_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit.

Default: 25

No

—

NGX_LD_PROXY_BUFFER_SIZE

Default: 8k

No

—

NGX_LD_MAX_TEMP_FILE_SIZE

Default: 100m

No

—

#### LiveData 12.6(2) Properties

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_LD_HOSTNAME

Specifies the reverse-proxy hostname over which this LD host is accessed.

Default: reverseproxy.host.domain

Yes

If the reverse-proxy livedata host FQDN changes.

No

NGX_PRXY_LD_PORT

Specifies the reverse-proxy port over which this livedata host is accessed.

Default: 443

Yes, If required.

If the reverse-proxy port for livedata changes.

No

NGX_LD_HOSTNAME

Specifies the Livedata server hostname.

Default: livedata.host.domain

Yes

If the upstream livedata host FQDN changes.

No

NGX_LD_BACKEND_FAILOVER

Specifies the livedata failover configurations. This is used to translate the location header during failover.

Default: hostname:port

Yes

For the SideA upstream LiveData, point to the upstream SideB LiveData.

For the SideB upstream, point to the upstream SideA.

No

NGX_LD_BACKEND_PROXY_FAILOVER

Specifies the livedata failover node for this livedata host. This is used to translate the location header during failover.

Default: hostname:port

Yes

Point to the other side of the reverse-proxy node.

No

##### LiveData 12.6(2) properties that are not recommended to be altered

These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                                if necessary, in exceptional situations and aren’t recommended to be changed casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3.

Default: livedata

No

NGX_LD_WEB_UPSTREAM_KEEPALIVE

Proxy backend configurations for livedata. Activates the cache for connections to the upstream livedata server.

Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections are closed.

Default: 128

No

NGX_LD_SIO_UPSTREAM_KEEPALIVE

Activates the cache for connections to the upstream livedata server socketIO endpoint.

Default: 128

No

NGX_LD_HTTP1_CONN_LIMIT

Specifies the number of concurrent HTTP/1.1 connections allowed per source IP.

Default: 12

No

NGX_LD_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 150

No

NGX_LD_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit.

Default: 25

No

NGX_LD_PROXY_BUFFER_SIZE

Sets the size of the buffer used for reading the first part of the response received from the server, which is enabled with
                                             reverse-proxy.

Default: 8k

No

NGX_LD_MAX_TEMP_FILE_SIZE

When buffering of responses from the server (which is enabled with reverse-proxy) is enabled, and the whole response doesn’t
                                             fit into the NGX_LD_PROXY_BUFFER_SIZE, a part of the response can be saved to a temporary file.

Default: 100m

No

### CUIC Properties

#### Unified Intelligence Center 12.6(1) properties

Use this env file when the upstream Unified Intelligence Center is still on 12.6(1) release. Otherwise use cuic.env.

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_CUIC_HOSTNAME

Specifies the reverse-proxy hostname over which this CUIC host is accessed.

Default: reverseproxy.host.domain

Yes

No

NGX_PRXY_CUIC_PORT

Specifies the reverse-proxy port over which this cuic host is accessed.

Default: 8444

Yes, If required.

New installation or if the port number changes.

No

NGX_PRXY_CUIC_DOC_PORT

Specifies the reverse-proxy port over which this CUIC host doc endpoint is accessed.

Default: 8447

Yes, If required.

New installation or if the port number changes.

No

NGX_CUIC_HOSTNAME

Specifies the CUIC server hostname.

Default: cuic.host.domain

Yes

If the upstream CUIC host FQDN changes.

No

##### Unified Intelligence Center 12.6(1) properties that are not recommended to be altered

These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             idp-adfs3.

Default: cuic_12.6(1)

No

Never

NGX_CUIC_UPSTREAM_KEEPALIVE

Activates the cache for connections to the upstream CUIC server.

Specifies the maximum number of idle keep alive connections to upstream servers that are preserved in the cache of each worker
                                             process. When this number exceededs, the least recently used connections are closed.

Default: 128

No

—

NGX_CUICDOC_UPSTREAM_KEEPALIVE

Activates the cache for connections to the upstream CUIC server doc endpoint.

Default: 128

No

—

NGX_CUIC_CACHE_SIZE

Specifies the initial size of the CUIC proxy cache.

Default: 15m

No

—

NGX_CUIC_CACHE_MAX_SIZE

Specifies the maximum size for the CUIC cache. When the size exceeds or there's not enough free space, the system removes
                                             the least recently used data.

Default: 50m

No

—

NGX_CUIC_CACHE_INACTIVE_DURATION

Specifies the content inactive duration for the CUIC cache. Cached data that is not accessed during the time specified get
                                             removed from the cache regardless of their freshness.

Default: 3y

No

—

NGX_CUICDOC_CACHE_SIZE

Specifies the initial size of the CUIC doc cache.

Default: 15m

No

—

NGX_CUICDOC_CACHE_MAX_SIZE

Specifies the maximum size for the CUIC doc cache. When the size exceeds or there isn’t enough free space, the system removes
                                             the least recently used data.

Default: 50m

No

—

NGX_CUICDOC_CACHE_INACTIVE_DURATION

Specifies the content inactive duration for CUIC doc cache. Cached data that aren’t accessed during the time specified get
                                             removed from the cache regardless of their freshness.

Default: 3y

No

—

NGX_CUIC_HTTP1_CONN_LIMIT

Specifies the number of concurrent HTTP/1.1 connections allowed per source IP.

Default: 12

No

—

NGX_CUIC_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 150

No

—

NGX_CUIC_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit.

Default: 100

No

—

NGX_CUIC_HISTORICAL_REPORT_CONN_LIMIT

Specifies the number of concurrent connections allowed, per source IP, for CUIC historical reports endpoints.

Default: 4

No

—

NGX_CUIC_HISTORICAL_REPORT_NEW_CONN_LIMIT

Specifies the number of concurrent connections allowed, per source IP, for CUIC historical reports newRest endpoints.

Default: 4

No

—

NGX_CUIC_HISTORICAL_REPORT_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for CUIC historical reports endpoints.

Default: 4

No

—

NGX_CUIC_REALTIME_REPORT_CONN_LIMIT

Specifies the number of concurrent connections allowed, per source IP, for CUIC realtime reports endpoints.

Default: 4

No

—

NGX_CUIC_REALTIME_REPORT_NEW_CONN_LIMIT

Specifies the number of concurrent connections allowed, per source IP, for CUIC realtime reports newRest endpoints.

Default: 4

No

—

NGX_CUIC_REALTIME_REPORT_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for CUIC realtime reports endpoints.

Default: 4

No

—

NGX_CUIC_REPORT_EXECUTION_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for CUIC reports execution endpoints.

Default: 4

No

—

NGX_CUIC_PROXY_BUFFER_SIZE

Specifies the size of the buffer used for reading the first part of the response received from the server, which is enabled
                                             for reverse-proxy.

Default: 8k

No

—

NGX_CUIC_MAX_TEMP_FILE_SIZE

When buffering of responses from the server (which is enabled for reverse-proxy) is enabled, and the whole response doesn't
                                             fit into the buffers set by the NGX_CUIC_PROXY_BUFFER_SIZE, a part of the response is saved to a temporary file.

Default: 100m

No

—

#### Unified Intelligence Center 12.6(2) properties

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

NGX_PRXY_CUIC_HOSTNAME

Specifies the reverse-proxy hostname over which this cuic host is accessed.

Default: reverseproxy.host.domain

Yes

If the reverse-proxy CUIC host FQDN changes.

No

NGX_PRXY_CUIC_PORT

Specifies the reverse-proxy port over which this cuic host is accessed.

Default: 443

Yes, If required.

If the reverse-proxy port changes.

No

NGX_CUIC_HOSTNAME

Specifies the CUIC server hostname.

Default: cuic.host.domain

Yes

If the upstream CUIC host FQDN changes.

No

##### Unified Intelligence Center 12.6(2) properties that are not recommended to be altered

These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                                if necessary, in exceptional situations and aren’t recommended changing casually without extensive testing.

Property Name, Description, and Default

Change Recommended?

When to Change?

TEMPLATE_TYPE

Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3.

Default: cuic

No

NGX_CUIC_UPSTREAM_KEEPALIVE

Activates the cache for connections to the upstream CUIC server.

Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the system closes the least recently used connections.

Default: 128

No

NGX_CUIC_CACHE_SIZE

Specifies the initial size of the CUIC cache.

Default: 30m

No

NGX_CUIC_CACHE_MAX_SIZE

Specifies the maximum size for the CUIC cache. When the size exceeds the set maximum, or there isn’t enough free space, the
                                             system removes the least recently used data.

Default: 100m

No

NGX_CUIC_CACHE_INACTIVE_DURATION

Specifies the content inactive duration for the CUIC cache. Cached data that aren’t accessed during the time specified get
                                             removed from the cache regardless of their freshness.

Default: 3y

No

NGX_CUIC_HTTP1_CONN_LIMIT

Specifies the number of concurrent HTTP/1.1 connections allowed per source IP.

Default: 12

No

NGX_CUIC_HTTP2_CONN_LIMIT

Specifies the number of concurrent HTTP/2 streams allowed per source IP.

Default: 150

No

NGX_CUIC_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit.

Default: 100

No

NGX_CUIC_HISTORICAL_REPORT_CONN_LIMIT

Specifies the number of concurrent connections allowed per source IP for CUIC historical reports endpoints.

Default: 4

No

NGX_CUIC_HISTORICAL_REPORT_NEW_CONN_LIMIT

Specifies the number of concurrent connections allowed per source IP for CUIC historical reports newRest endpoints.

Default: 4

No

NGX_CUIC_HISTORICAL_REPORT_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for CUIC historical reports endpoints.

Default: 4

No

NGX_CUIC_REALTIME_REPORT_CONN_LIMIT

Specifies the number of concurrent connections allowed per source IP for CUIC realtime reports endpoints.

Default: 4

No

NGX_CUIC_REALTIME_REPORT_NEW_CONN_LIMIT

Specifies the number of concurrent connections allowed per source IP for CUIC realtime reports new REST endpoints.

Default: 4

No

NGX_CUIC_REALTIME_REPORT_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for CUIC realtime reports endpoints.

Default: 4

No

NGX_CUIC_REPORT_EXECUTION_REQUEST_BURST_LIMIT

Specifies the HTTP request burst limit for CUIC reports execution endpoints.

Default: 4

No

NGX_CUIC_PROXY_BUFFER_SIZE

Configurations overridden from common config for CUIC.

Specifies the size of the buffer used for reading the first part of the response received from the server, which is enabled
                                             for reverse-proxy.

Default: 8k

No

NGX_CUIC_MAX_TEMP_FILE_SIZE

When buffering of responses from the server (which is enabled for reverse-proxy) is enabled, and the whole response doesn’t
                                             fit into the buffers set by the NGX_CUIC_PROXY_BUFFER_SIZE, a part of the response is saved to a temporary file.

Default: 100m

No

## Common Rate Limit Properties

Configure these properties separately for each component.

Property Name, Description, and Default

Change Recommended?

When to Change?

Hot Reload Supported?

IPTABLES_CONNECTION_LIMIT_ABOVE

Specifies the maximum number of parallel connections to reverse proxy per client IP address.

Default:

Finesse: 10

Chat: 30

Cloud Connect: 8

CUIC: 6

IdP: 8

IdS: 6

LD: 10

Only if required

Change when you want to increase/decrease the number of parallel connections to reverse proxy per client IP address.

No

IPTABLES_HASH_LIMIT_UPTO

Specifies the rate/sec at which connection to a port will be accepted.

Default:

Finesse: 6/sec

Chat: 20/sec

Cloud Connect: 4/sec

CUIC: 2/sec

IdP: 4/sec

IdS: 2/sec

LD: 6/sec

Only if required

Change when you want to increase/decrease the number of requests per second per combination of source IP and destination port.

No

IPTABLES_HASH_LIMIT_BURST

Specifies the maximum initial number of requests to a port that will be accepted.

Default:

Finesse: 8

Chat: 25

Cloud Connect: 6

CUIC: 4

IdP: 6

IdS: 4

LD: 8

Only if required

Change when you want to increase/decrease the maximum initial number of requests.

No

IPTABLES_LOG_LIMIT_BURST

Specifies the maximum initial number of requests for logging, that are rejected for a port by iptables.

Default: 1

Only if required

Change when you want to increase/decrease logging for the number of requests/min that are not accepted by iptables rule.

No

IPTABLES_LOG_LIMIT

Specifies the rate of logging the number of requests/min that are rejected for a port by iptables.

Only if required

Change when you want to increase/decrease logging for the number of requests/min that are not accepted by iptables rule.

No

| Note | Hot reload is not supported for the installer.env properties and for properties that are not recommended to be changed. |
|---|---|

| Note | Cisco Reverse Proxy Installer is a per-requisite reading for this chapter. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| CONTAINER_NAME Specifies the name of the reverse-proxy container—generally the reverse-proxy hostname. Default: proxy25.autobot.cvp | Yes | When you change the name of the container. |
| CONTAINER_NETWORK_MODE Specifies the network mode of the container. Default: host | Yes, if required. | If you use the host network mode for a container, the network stack for that container isn’t isolated from the host. 1 The other value is bridge . A bridge network creates a separate network for containers to communicate with each other, even if it is isolated from other
                                             networks on the host. This is useful when you want to deploy multiple containers on a single host and communicate with each
                                             other, but not with the outside world. |
| CONTAINER_DNS_RESOLVER Specifies a list of DNS servers separated by the \| symbol. Note Only internal hosts are reachable from this configuration depending on the security hardening applied. Default: 1.1.1.1\|8.8.8.8 | Note | Only internal hosts are reachable from this configuration depending on the security hardening applied. | Yes | If an IP address changes, update the list. |
| Note | Only internal hosts are reachable from this configuration depending on the security hardening applied. |
| CONTAINER_DNS_SEARCH_DOMAIN Specifies a DNS search domain to use when resolving hostnames inside the container. This property takes one or more domain
                                             names as arguments, separated by commas. In this example, the DNS search domain is example.com . Inside the container, the DNS resolver appends the search domain to the hostname and attempts to resolve it. If you ping
                                             the webserver inside the container, the DNS resolver tries to resolve webserver.example.com ; if that fails, it tries to resolve webserver . Default: search.domain.1\|search.domain.2 | Yes | — |
| PROXY_BINDING_IP Running multiple proxy containers on the same host can be supported by using multiple DNS hostnames mapped to distinct IP
                                             addresses on that host. These addresses must be configured on the same external NIC used for the reverse proxy container during
                                             the install_os_settings.sh configuration. Specify one of the external NIC's IP addresses as the PROXY_BINDING_IP. This setup
                                             ensures that traffic intended for a specific hostname is directed to the container bound to the corresponding IP address. For example, if the external NIC is ens192 with IP addresses 192.168.1.69 and 192.168.1.70, use 192.168.1.69 as the PROXY_BINDING_IP
                                             for one container and 192.168.1.70 for the other container. Default: No value | Yes, if required. | By default, if the external NIC is configured with a single IP address, the installer automatically uses that value, and there
                                             is no need to explicitly specify it. However, if the external NIC has multiple IP addresses, the PROXY_BINDING_IP field must
                                             be populated with one of those IP addresses. |
| PROXY_BINDING_INTERNAL_IP Specify the internal IP that will be used for accessing the reverse proxy container. Default: No value | Only if required. | When there are more than one internal IP configured in the system. When you want to access the reverse proxy container through a specific internal IP. |
| CREATE_SELF_SIGNED_SSL_CERT Specifies whether to create a self-singed certificate during the reverse-proxy installation. Default: TRUE | Yes, if required. | If the CA-signed certificates are present, you don't need to install self-signed certificates during the installation. In
                                             this case, change to FALSE. |
| CERTIFICATE_COMMON_NAME Specifies the common name for the certificate. This value is required to create self-signed certificates. Used on the next property. Default: *.cisco.com | Yes, if required. | Required only for creating self-singed certificates. |
| CERTIFICATE_SUBJECT Specifies the subject line to be used on the self-signed certificate. Default: /C=IN/ST=KA/L=BLR/O=Cisco/OU=CCBU/CN=${CERTIFICATE_COMMON_NAME} | Yes, if required. | Required only for creating self-singed certificates. |
| SSL_CERT_NAME Specifies the name of the certificate file to be auto-generated. Default: reverseproxy.crt | Yes, If required. | Required only for creating self-singed certificates. |
| SSL_KEY_NAME Specifies the name of the key file to be auto-generated. Default: reverseproxy.key | Yes, if required. | Required only for creating self-singed certificates. |
| SSL_CERT_KEY_LENGTH Specifies the certificate key length to create the self-signed certificate. Default: 2048 | Yes, if required. | Required only for creating self-singed certificates. |
| SSL_CERT_EXPIRY_IN_DAYS Certificate expiry in days, to be specified in the self-signed certificate. Default: 1095 | Yes, if required. | Required only for creating self-singed certificates. |
| AUTO_RESTART_CONTAINER Toggles auto-restart of the reverse-proxy container when the host system reboots. Default: 0 | Yes | Enable this property only when the reverse-proxy is in working condition. 2 |
| NOFILE_LIMIT Specifies the initial and maximum number of open file descriptors that a container can have. Option in Podman is used to set system resource limits on a container. Default: nofile=102400:102400 | Yes, if required. | nofile=204800:204800 for a 4000 deployment. |
| CPU_LIMIT Specifies the number of CPUs that a container can use. Default: 2 | Yes, if required. | 4 for 4000 deployment |
| MEM_LIMIT Specifies the maximum amount of memory that a container can use, in bytes or using a human-readable format. Default: 4G | Yes, if required. | 8G for 4000 deployment |
| MEM_SWAP_LIMIT Specifies the maximum amount of memory and swap for a container—in bytes or using a human-readable format such as 1G for 1
                                             gigabyte. Default: 8G | Yes, if required. |  |
| MEM_RES Sets a soft limit on the minimum amount of memory to be available for the container. Default: 2G | Yes, if required. | 4G for 4000 deployment |

| Note | Only internal hosts are reachable from this configuration depending on the security hardening applied. |
|---|---|

| Note | Ensure that the host has adequate resources to run the container with the modified resource constraints. |
|---|---|

| Note | These properties are provided for reference and they are available in the configuration to provide flexibility, to adjust
                                             the behavior if necessary, and in exceptional situations. It isn't recommended to change casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| CONTAINER_IMAGE A container image is a read-only template that contains a set of instructions for creating a container and defining the resources
                                          within the container. Default: reverse-proxy-openresty-container:12.6(2) | No | Never |
| HOST_WORKING_DIR Specifies the working directory of the container Default: ~/reverse_proxy/${CONTAINER_NAME} | No |  |
| NGX_HOME Specifies the home directory of the NGINX server inside the container. Default: /usr/local/openresty/NGINX | No |  |
| HOST_CACHE_VOL Specifies the host system directory used to mount on the container. 3 Mapped with the following container directory: NGX_CACHE_DIR. Default: ${HOST_WORKING_DIR}/cache | No |  |
| HOST_SSL_VOL Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_SSL_DIR Default: ${HOST_WORKING_DIR}/ssl | No |  |
| HOST_LOGS_VOL Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_LOG_DIR Default: ${HOST_WORKING_DIR}/logs | No |  |
| HOST_CONF_VOL Specifies the host system directory used to mount on the container. Mapped with the container directory mentioned here: NGX_CONF_DIR Default: ${HOST_WORKING_DIR}/conf | No |  |
| HOST_HTML_VOL Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_HTML_DIR Default: ${HOST_WORKING_DIR}/html | No |  |
| HOST_LUA_VOL Specifies the host system directory used to mount on the container. Mapped to the following container directory: NGX_LUA_DIR Default: ${HOST_WORKING_DIR}/lua | No |  |
| NGX_CACHE_DIR Specifies the container directory location mapped with the corresponding host system directory specified in the HOST_CACHE_VOL
                                          property. Default: ${NGX_HOME}/cache | No |  |
| NGX_SSL_DIR Specifies the container directory location mapped with the corresponding host system directory mentioned in the HOST_LOGS_VOL
                                          property. Default: ${NGX_HOME}/ssl | No |  |
| NGX_LOG_DIR Specifies the container directory location mapped with the corresponding host system directory mentioned in the HOST_LOGS_VOL
                                          property. Default: ${NGX_HOME}/logs | No |  |
| NGX_CONF_DIR Specifies the container directory location mapped with the corresponding host system's directory mentioned in the HOST_CONF_VOL
                                          property. Default: ${NGX_HOME}/conf | No |  |
| NGX_HTML_DIR Specifies the container directory location mapped with the corresponding host system directory mentioned in the HOST_HTML_VOL
                                          property. Default: ${NGX_HOME}/html | No |  |
| NGX_LUA_DIR Specifies the container's directory location mapped with the corresponding host system's directory mentioned on this property
                                          HOST_LUA_VOL. Default: ${NGX_HOME}/lua | No |  |
| MEM_SWAPPINESS Controls how aggressively the kernel should swap memory pages of the container to disk when the container exceeds its memory
                                          limit. Default: 1 | No |  |
| NGX_USER_USERID The Reverse Proxy Installer generates a new user ID to start the reverse proxy container, which will run under this user. Default: nginxuser | No |  |
| NGX_USER_UID The UID to be assigned to 'nginxuser'. Default: 9876 | No. | If UID 9876 is already assigned to another user, you can update it to the next available UID. |
| NGX_USER_USERGROUP The user group created to map to nginxuser. Default: nginxusergroup | No |  |
| LOAD_CONTAINER_IMAGE_FROM_TAR This property is commented out by default. The default value (when it’s commented) is true. Default: This property is commented by default. | No | You can change the value to load the container image from a different location. |
| REVERSE_PROXY_CONTAINER_IMAGE_TAR Specifies the location of the container image tar file. This property is commented out by default. ${SCRIPTPATH} is the location of the proxy_launcher.sh script. Default: ${SCRIPTPATH}//reverse-proxy-openresty-container/reverse-proxy-openresty-container.tar.gz | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_JWT_SECRET OpenResty® Constants(defined in maps.conf) configuration. JWT secret pulled from IdS host using CLI "show ids secret" This secret is used to verify and validate tokens at proxy for authentication in SSO mode This secret is applicable only for IdS < 12.6(2). Default: TWSFbB9J6fBnu/D/hrHiQl2O0WEgrVj69ZiHJCtwahI= | Yes, if IdS is running in < 12.6(2) version | Update it with the output of this command from IdS: "show ids secret" | Yes |
| NGX_SYSLOG_SVR_IP Specifies the syslog server IP to which NGINX pushes some specific notification logs when the access for an IP is blocked. Default: 127.0.0.1 | Yes, if necessary. | The current syslog server is the current reverse-proxy. This can be changed to the IP for any syslog server, based on the
                                                configuration. | Yes |
| NGX_VALID_REFERRERS Specifies the “Referrer” request header field values for which the request is allowed. Request is blocked for all other referrers.
                                                The value is case-sensitive. Include all reverse-proxy hostnames, IdS hostnames and ADFS hostname in this list. They are required for reverse-proxy and
                                                other functionality. Default: proxy_pub.host.domain\|proxy_sub.host.domain\| ids_pub.host.domain\|ids_sub.host.domain\|adfs.host.domain | Yes | If not updated, the pages return with 417 HTTP error code. Make sure there are no typos in the hostnames. | Yes |
| NGX_LOCALHOST_IPS Specifies the list of IPs assigned to the reverse-proxy host across all NICs. Include all public and private IPs for reverse-proxy
                                                in this list. Include the alternate side reverse-proxy's IP addresses as well. Default: 192.168.1.69\|192.168.1.169 | Yes | Update all the reverse-proxy IPs here. | Yes |
| NGX_RATELIMIT_DISABLE_IPS Specifies a list of IP addresses for which rate limits aren't applied. Default: 192.168.1.69\|192.168.1.169\|127.0.0.1 | Yes | All the IP address that should be allowed to exclude on rate-limiting. Update the list with all the public and private IPs of both the primary and secondary reverse-proxy. It can also include any
                                                other load balancer or proxy which are forwarding requests to reverse-proxy. | Yes |
| NGX_LOAD_BALANCER_IPS Hostnames aren’t supported as a permissible value in NGX_LOAD_BALANCER_IPS The list of entries should be \| separated # Example: "192.162.1.0/24\|10.78.95.76" Alternatively, if the internet client connection is stopped at the reverse-proxy directly, these variables MUST be empty. | Yes, if required. | If the load balancer forwards requests to the reverse-proxy, populate with the load balancer IP addresses. | No |
| NGX_LOAD_BALANCER_REAL_IP_HEADER Devices must also send the end client IP alone, in a custom header. Add the name of the custom header used for this purpose to the NGX_LOAD_BALANCER_REAL_IP_HEADER variable. For example, " X-Real-IP ". If you use the X-Forwarded-For as the field used to detect the client IP, include all trusted devices that can appear in this list in the NGX_LOAD_BALANCER_IPS
                                                variable. The first untrusted IP encountered is used as the client IP. We don't recommend using this field ( X-Forwarded-For ) for detecting the client IP. | Yes, if required. |  | No |
| NGX_ERR_LOG_LEVEL The log level of the error.log file can be set to debug, info, alert, warn, error, crit, or emerg. Messages from the specified level and all higher severity
                                                levels will be logged. Default: info | Yes, if required. | The log level can be set to debug for troubleshooting purposes. But, it is not recommended to maintain this setting for an
                                                extended period, as it may generate a large amount of log data. | Yes |

| Note | These properties are provided for reference and they are available in the configuration, to provide flexibility and adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended to be changed casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| NGX_NUM_WKR_PRC OpenResty® NGINX core configurations. Specifies the number of worker processes. The value "auto" uses the number of available CPU cores. Default: auto | No |  |
| NGX_PID_FILE Defines a file that stores the process ID of the main process. Default: openresty.pid | No |  |
| NGX_WKR_CPU_AFFINITY Binds the worker processes to the sets of CPUs. The value "auto" binds worker processes automatically to the available CPUs. Default: auto | No |  |
| NGX_WKR_PRIORITY Defines the scheduling priority for worker processes like it’s done by the nice command. A negative number means higher priority.
                                                The allowed range varies from -20 to 20. Default: 0 | No |  |
| NGX_NUM_RLIMIT Changes the limit on the maximum number of open files (RLIMIT_NOFILE) for worker processes. Used to increase the limit without
                                                restarting the main process. Default: 102400 | No |  |
| NGX_MULTI_ACCEPT If multi_accept is disabled, a worker process accepts one new connection at a time. Otherwise, a worker process accepts all
                                                new connections at a time. Default: on | No |  |
| NGX_NUM_WKR_CONN Specifies the maximum number of simultaneous connections that can be opened by a worker process. Default: 10240 | No |  |
| NGX_SEND_FILE Enables or disables the use of sendfile . | No | No |
| NGX_TCP_NOPUSH Enables or disables the use of the TCP_NOPUSH socket option on FreeBSD or the TCP_CORK socket option on Linux. The options
                                                are enabled only when the sendfile is used. Default: on | No |  |
| NGX_MAP_HASH_BUCKET_SIZE Specifies the bucket size for the map variables hash tables. Default: 128 | No |  |
| NGX_SERVERNAMES_HASH_BUCKET_SIZE Specifies the bucket size for the server names hash tables. Default: 512 | No |  |
| NGX_JWT_EXPIRY Specifies the JWT token expiry in seconds as configured in the IdS host. Token cache expiry time in reverse-proxy. Reverse-proxy keeps the cached token for 2 hours for the default configuration of
                                                1-hour access token expiry time configured in IdS. Default: 7200 | No |  |
| NGX_IDS_PUBLIC_KEY_POLL_INTERVAL Specifies the IdS public key poll frequency in seconds. The frequency at which reverse-proxy polls the ids to get the public key value. The default is once in 5 minutes. Default: 300 | No |  |
| NGX_CLIENT_LOCK_THRESHOLD If the threshold to detect DoS attacks is crossed in the specified interval, the client IP is blocked for the specified duration. Default: 5 | No |  |
| NGX_CLIENT_LOCK_DURATION Specifies the request authorization failure threshold over a given interval for a source IP. Default: 30 | No |  |
| NGX_CLIENT_BLOCK_DURATION Specifies the duration of blocking (in seconds) for clients to avoid brute force attacks. The block duration for the client IP is 30 minutes. Default: 1800 | No |  |
| NGX_SYSLOG_SVR_PORT Specifies the port for the syslog server. Default: 514 | No | Usually the syslog server listens on 514, if the syslog server is configured to listen on some other port then this can be
                                                changed. |
| NGX_LOG_FILE Specifies the OpenResty® logging file. Default: access.log | No |  |
| NGX_LOG_FORMAT Specifies the OpenResty® NGINX access log format name as specified in logging.conf. Default: info | No | Not recommended to change on a production system. You can change it to the debug format in LAB setup for more detailed logging. |
| NGX_LOG_BUFFER Specifies the OpenResty® NGINX access log buffer size. When this buffer is full or the flush interval is reached, the system
                                                writes the logs to the disk. Default: 16k | No |  |
| NGX_LOG_FLUSH_INTERVAL Specifies the OpenResty® NGINX access log flush interval. Logs are written to the disk after this interval is reached or the
                                                log buffer is full. Default: 30s | No | Not recommended changing on production servers. For a LAB system, you can reduce this value to 1 to 5s so you can check the access.log file updates immediately. |
| NGX_PROXY_CACHE_LOCK Only one request at a time can populate a new cache element identified according to the proxy_cache_key directive by passing a request to the server, which is enabled with reverse-proxy. Other requests of the same cache element
                                                either wait for a response to appear in the cache or the cache lock for this element to be released, up to the time set by
                                                the NGX_PROXY_CACHE_LOCK_TIMEOUT value. Default: on | No |  |
| NGX_PROXY_CACHE_LOCK_TIMEOUT Specifies the timeout for NGX_PROXY_CACHE_LOCK. When the time expires, the request is passed to the server, which is enabled
                                                with reverse-proxy; however, the response isn't cached. Default: 30s | No |  |
| NGX_PROXY_CACHE_LOCK_AGE If the last request passed to the server, which is enabled with reverse-proxy, for populating a new cache element hasn’t completed
                                                for the specified time, one more request passes to the server, which is enabled with reverse-proxy. Default: 5s | No |  |
| NGX_PROXY_CACHE_BACKGROUND_UPDATE Allows starting a background sub request to update an expired cache item, while a stale cached response is returned to the
                                                client. Default: on | No |  |
| NGX_PROXY_CACHE_REVALIDATE Enables revalidation of expired cache items using conditional requests with the “If-Modified-Since” and “If-None-Match” header
                                                fields. Default: on | No |  |
| NGX_PROXY_CACHE_VALID Specifies the caching time for 200, 301, and 302 responses. Default: 24h | No |  |
| NGX_VARIABLES_HASH_BUCKET_SIZE Specifies the bucket size for the variables hash table. Default: 128 | No |  |
| NGX_KEEPALIVE_TIMEOUT Specifies a timeout during which a keep-alive client connection stays open on the server side. The zero value disables keep-alive
                                                client connections. Default: 20s | No |  |
| NGX_SEND_TIMEOUT Specifies a timeout for transmitting a response to the client. The timeout is set only between two successive write operations,
                                                not for the transmission of the whole response. Default: 10s | No |  |
| NGX_CLIENT_HEADER_TIMEOUT Specifies the timeout for reading the client request header. Default: 10s | No |  |
| NGX_CLIENT_BODY_TIMEOUT Specifies a timeout for the reading the client request body. The timeout is set only for a period between two successive read
                                                operations, not for the transmission of the whole request body. Default: 10s | No |  |
| NGX_RESET_TIMEDOUT_CONNECTION Enables or disables resetting timed out connections and connections closed with the non-standard code 444. Default: on | No |  |
| NGX_CLIENT_HEADER_BUFFER_SIZE Specifies the buffer size for reading the client request header. Default: 4K | No |  |
| NGX_CLIENT_BODY_BUFFER_SIZE Specifies the buffer size for reading the client request body. Default: 2k | No |  |
| NGX_CLIENT_MAX_BODY_SIZE Specifies the maximum allowed size of the client request body. Default: 15m | No |  |
| NGX_LARGE_CLIENT_HEADER_BUFFER_NUM Specifies the maximum number of buffers used for reading a large client request header. Buffers are allocated only on demand. Default: 2 | No |  |
| NGX_LARGE_CLIENT_HEADER_BUFFER_SIZE Specifies the maximum size of buffers used for reading a large client request header. A request line can’t exceed the size
                                                of one buffer. Buffers are allocated only on demand. Default: 8K | No |  |
| NGX_UNDERSCORES_IN_HEADERS Enables or disables the use of underscores in client request header fields. Default: on | No |  |
| NGX_KEEPALIVE_REQUESTS Specifies the maximum number of requests that are served through one keep-alive connection. After the maximum number of requests are made, the connection is closed. Default: 500 | No |  |
| NGX_HTTP2_MAX_CONCURRENT_STREAMS Specifies the maximum number of concurrent HTTP/2 streams in a connection. Default: 150 | No |  |
| NGX_SERVER_TOKENS Enables or disables emitting NGINX version on error pages and in the “Server” response header field. Default: off | No |  |
| NGX_LIMIT_CONN_DRY_RUN Enables the dry-run mode for limiting HTTP connections. In this mode, the number of connections isn’t limited. However, in
                                                the shared memory zone, the number of excessive connections is considered as usual. Default: off | No | On a production system, this should be always "off". If the system is running in lab mode, you can toggle this "on" to avoid rate limiting. |
| NGX_LIMIT_REQ_DRY_RUN Enables the dry-run mode for limiting HTTP requests. In this mode, the number of connections isn’t limited, however, in the
                                                shared memory zone, the number of excessive connections is considered as usual. Default: off | No | On a production setup, this should be always "off". If the system is running in lab mode, you can toggle this "on" to avoid rate limiting. |
| NGX_LIMIT_CONN_LOG_LEVEL Specifies the desired logging level for cases when the server limits the number of connections. Default: error | No |  |
| NGX_LIMIT_REQ_LOG_LEVEL Specifies the desired logging level for cases when the server refuses to process requests due to rate exceeding, or delays
                                                request processing. Default: error | No |  |
| NGX_LIMIT_REQ_STATUS Specifies the status code to return in response to rejected requests due to HTTP request rate limits. This is the standard HTTP error code for rate-limiting errors. Default: 429 | No |  |
| NGX_LIMIT_CONN_STATUS Specifies the status code to return in response to rejected requests due to HTTP connection rate limits. Default: 503 | No | Error code returned when the connection limits are reached. |
| NGX_CHAT_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for chat access. Default: 30r/s | No |  |
| NGX_IDS_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for IdS access. Default: 5r/s | No |  |
| NGX_FIN_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for Finesse access. Default: 90r/s | No |  |
| NGX_FIN_CLIENT_LOG_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for Finesse client log requests. Default: 5r/s | No |  |
| NGX_FIN_SSO_VALVE_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for Finesse SSO valve requests. Default: 5r/s | No |  |
| NGX_CUIC_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for CUIC access. Default: 50r/s | No |  |
| NGX_CUIC_HISTORICAL_REPORT_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for CUIC historical report requests. Default: 16r/s | No |  |
| NGX_CUIC_REALTIME_REPORT_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for CUIC realtime report requests. Default: 48r/s | No |  |
| NGX_CUIC_REPORT_EXECUTION_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for CUIC report execution requests. Default: 12r/s | No |  |
| NGX_LIVEDATA_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for livedata access. Default: 25r/s | No |  |
| NGX_CLOUDCONNECT_DR_TASK_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for DR API task request access. Default: 100r/s | No |  |
| NGX_CLOUDCONNECT_USER_SYNC_CALLBACK_REQUEST_RATE_LIMIT Specifies the HTTP request rate limit for user sync callback request access. Default: 5r/m | No |  |
| NGX_PRXY_STATIC_FILES_PORT Specifies the OpenResty® static content configuration. The reverse-proxy port is used to serve static files under the HTML
                                                directory. Default: 10000 | No | This location serves the proxy-map information. You can change the port number if necessary. |
| NGX_PRXY_STATUS_IP Specifies the reverse-proxy IP used to access OpenResty® NGINX stats over the "/reverseproxy_status" endpoint Internal request is accessible from only the host system. Default: 127.0.0.1 | No |  |
| NGX_PRXY_STATUS_PORT Specifies the reverse-proxy port used to access OpenResty® NGINX stats over the "/reverseproxy_status" endpoint. Default: 10001 | No |  |
| NGX_USERTIMERTHREAD_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100k | No |  |
| NGX_USERLIST_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 50m | No |  |
| NGX_CREDENTIALSSTORE_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100m | No |  |
| NGX_USERCOUNT_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100k | No |  |
| NGX_CLIENTSTORAGE_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100m | No |  |
| NGX_BLOCKINGRESOURCES_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100m | No |  |
| NGX_TOKENCACHE_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 10m | No |  |
| NGX_IPSTORE_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 10m | No |  |
| NGX_DESKTOPURLLIST_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 10m | No |  |
| NGX_DESKTOPURLCOUNT_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100k | No |  |
| NGX_THIRDPARTYGADGETURLLIST_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100m | No |  |
| NGX_THIRDPARTYGADGETURLCOUNT_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100k | No |  |
| NGX_CORSHEADERSSTORE_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100k | No |  |
| NGX_TIMERTHREADSSTORE_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100k | No |  |
| NGX_ALTERNATE_HOSTS_SHRD_DICT_SIZE Specifies the LUA shared dictionary sizes used by reverse-proxy internally. Default: 100k | No |  |
| NGX_VALID_USER_AGENTS_REGEX Defines the valid User-Agent regular expression that the reverse proxy permits. Default: ~*(^Mozilla/5\.0 .*(Firefox\|Chrome\|Edg\|Safari)/[0-9]+) | No | The regular expression includes all valid User-Agent values that are sent by browsers when accessed through the list of browsers
                                                supported by Cisco. If necessary, you can modify the regular expression to accommodate additional browser types. |
| NGX_USE_REGEX_TO_VALIDATE_USER_AGENT If set to true, user agent validation is based on the NGX_VALID_USER_AGENTS_REGEX value; otherwise, it falls back to the default
                                                block list to block invalid user agents. Default: true | No | This property can be set to false if the user agent check should be performed based on the block list instead of NGX_VALID_USER_AGENTS_REGEX. |

| Note | These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                          the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| NGX_CACHE_DIR Specifies the cache directory where various resources for components are cached. Default: ${NGX_HOME}/cache | No |  |
| NGX_CONF_DIR Specifies the OpenResty® directory containing NGINX configurations, such as core and component configurations. Default: ${NGX_HOME}/conf | No |  |
| NGX_HOME Specifies the home directory for OpenResty® nginx installation. Default: /usr/local/openresty/nginx | No |  |
| NGX_HTML_DIR Specifies the OpenResty® directory Default: ${NGX_HOME}/html Directory containing static resources. | No |  |
| NGX_LOG_DIR Specifies the OpenResty® directory where OpenResty® logs are stored. Default: ${NGX_HOME}/logs | No |  |
| NGX_LUA_DIR Specifies the OpenResty® directory containing lua resources. Default: ${NGX_HOME}/lua | No |  |
| NGX_SSL_DIR Specifies the OpenResty® directory containing SSL resources like certs and keys. Default: ${NGX_HOME}/ssl | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_SSL_TRUST_CRT Specifies a file with trusted CA certificates in the PEM format used to verify the certificate of the Finesse HTTPS server,
                                          which is enabled for reverse-proxy. Default: ${NGX_SSL_DIR}/upstreams_finesse_trust.crt | Yes, if necessary. | Point to the exact location of upstream Finesse's certificate for mutual trust establishment. | No |
| NGX_SSL_CRT SSL connector configuration for the component access. Specifies the location of a file with the certificate, for the given component, in the PEM format. Default: ${NGX_SSL_DIR}/reverseproxy.crt | Yes, if necessary. | Update the location of the Finesse reverse-proxy certificate. | No |
| NGX_SSL_KEY Specifies the location of a file with the secret key, for the given component, in the PEM format. Default: ${NGX_SSL_DIR}/reverseproxy.key | Yes, if necessary. | If the location of the file changes. | No |

| Note | These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                          the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| #NGX_SSL_DHPARAM Specifies a file with DH parameters for DHE ciphers. Default: ${NGX_SSL_DIR}/dhparam.pem This property is disabled by default. Uncomment the parameter to use it. | No. Can be changed if necessary. | Enable for more security, to prevent affecting by an attack exploiting the Logjam vulnerability. For more information, see Understanding Logjam and Future-Proofing Your Infrastructure at: https://cisco.blogs.com |
| NGX_PRXY_SSL_VERIFY Enables or disables verification of the HTTPS server certificate, which is enabled for reverse-proxy. Default: on | No | Changing this to off disables SSL verification of the requests. |
| NGX_PRXY_SSL_VERIFY_DEPTH Specifies the verification depth in the HTTPS server certificates chain, which is enabled for reverse-proxy. This is for DoS prevention. Building the chain might be an exponential algorithm with backoff, so with the openssl default
                                       of 100 a malicious backend might cause denial of service in nginx. Default: 10; less than 4 is easy to break. | No |  |
| NGX_SSL_CACHE_SIZE Specifies the SSL session cache size for session parameters storage for client connections. This cache is shared between all worker processes. The cache size is specified in bytes; one megabyte can store about 4000
                                       sessions. Each shared cache should have an arbitrary name. Default: 10m | No |  |
| NGX_SSL_CIPHERS Specifies the OpenSSL format for enabled ciphers. Default: EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH | No | This list contains all the strong ciphers available. You can update the list if ciphers are found to be vulnerable or to add
                                       new supported ciphers. |
| NGX_SSL_PRFR_SRVR_CIPHERS Prefer server ciphers over client ciphers. Default: on | No |  |
| NGX_SSL_PROTO Specifies the TLS versions enabled for the connections. To specify multiple values, use space delimiters. # Example: NGX_SSL_PROTO="TLSv1 TLSv1.1 TLSv1.2" Generally TLS version 1.2 is supported for the webapp requests. TLS v1 and TLS v1.1 aren’t recommended. Default: TLSv1.2 | No |  |
| NGX_SSL_SESSION_TICKETS Enables or disables session resumption through TLS session tickets. Default: off | No | Enable to resume sessions and avoid keeping a per-client session state. The TLS server encapsulates the session state into
                                    a ticket and forwards it to the client. The client can later resume a session using the obtained ticket. |
| NGX_SSL_SSN_TIMEOUT Specifies a time during which a client may reuse the session parameters—how long each session lives in reverse-proxy. Default: 30m | No |  |
| NGX_SSL_STAPLING Enables or disables stapling of OCSP responses by the server. SSL stapling means that revocation information about the servers certificate (that is, the OCSP response) are included in
                                       the TLS handshake together with the server certificate. Default: off | No |  |
| NGX_SSL_STAPLING_VERIFY Enables or disables the verification of OCSP responses by the server. Allows the presenter of a certificate to bear the resource cost involved in providing OCSP responses by appending ("stapling")
                                       a time-stamped OCSP response signed by the CA to the initial TLS handshake, eliminating the need for clients to contact the
                                       CA". Default: off | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_FIN_HOSTNAME Reverse proxy hostname through which this Finesse host is accessed. Default: reverseproxy.host.domain | Yes | New installation or if the hostname of the reverse proxy must be accessed from the internet changes. | No |
| NGX_PRXY_ALT_FIN_HOSTNAME Specifies the reverse proxy hostname for the Finesse failover node associated with this Finesse host. This should reference
                                             the reverse proxy node on the alternate side. Default: Empty | Yes, if required. | While deploying the secondary reverse proxy in a high availability mode. | No |
| NGX_PRXY_FIN_PORT Specifies the reverse proxy port over which this Finesse host are accessed. Default: 8445 | Yes, if necessary. | New installation or if the port number of the reverse proxy must be accessed from the internet changes. | No |
| NGX_PRXY_ALT_FIN_PORT Specifies the reverse proxy port for the Finesse failover node associated with this Finesse host. This should reference the
                                             reverse proxy node on the alternate side. Default: Empty | Yes, if required. | While deploying the secondary reverse proxy in a high availability mode. | No |
| NGX_FIN_HOSTNAME Specifies the upstream Finesse hostname. Default: finesse.host.domain | Yes | New installation or if the hostname of the Finesse box changes. | No |
| NGX_ALT_FIN_HOSTNAME Specifies the finesse hostname for the alternate side. Default: Empty | Yes, if required. | While deploying secondary finesse node in a high availability mode. | No |
| NGX_AUTH_URL Specifies the Finesse URL to fetch the users list to perform authentication at proxy. Default: https://reverseproxy.host.domain:8445/finesse/api/UserAuth | Yes | Replace "reverseproxy.host.domain" with the FQDN of the reverse proxy. | No |
| NGX_AUTHENTICATE_WEBSOCKET Specifies how to enable the authentication of websocket request. Default: true | No | When websocket authentication needs to be disabled, you can change the value to false. If the value is false, to mitigate the possible DoS attack, reverse proxy performs specific checks before allowing the websocket
                                             connections. Accept the websocket connections only from those IP addresses that have successfully made an authenticated REST
                                             request. Authenticate the REST request before establishing the websocket connection. Reverse proxy deployments that use L7 intermediaries, such as Content Delivery Network (CDN), often redirect traffic through
                                             interim servers before the traffic reaches the reverse proxy. In such deployments, ensure X-Forwarded-For headers are correctly relayed to identify the client’s IP address. The X-Forwarded-For headers are used to authenticate the websocket connection by matching it with the previously authenticated REST request. Note If you set the default value to false, the attempt to create the websocket connections before issuing any REST request displays
                                                         an Authorization Failed error message. The authentication check done by the reverse proxy gets disabled, but the XMPP authentication is done upstream. | Note | If you set the default value to false, the attempt to create the websocket connections before issuing any REST request displays
                                                         an Authorization Failed error message. The authentication check done by the reverse proxy gets disabled, but the XMPP authentication is done upstream. | Yes |
| Note | If you set the default value to false, the attempt to create the websocket connections before issuing any REST request displays
                                                         an Authorization Failed error message. The authentication check done by the reverse proxy gets disabled, but the XMPP authentication is done upstream. |
| NGX_FIN_USERS_URL If the externally accessible FQDN of the reverse proxy differs from its internal FQDN, this field should be filled in. For
                                             example, NGX_FIN_USERS_URL="https://internal-reverseproxyhostname.cisco.com:8445/finesse/api/Users". If the external and internal
                                             FQDNs of the reverse proxy are the same, this field can be left blank. Default: Empty | Yes, if required. | External FQDN of the reverse proxy does not match the internal FQDN of the reverse proxy. | Yes |

| Note | If you set the default value to false, the attempt to create the websocket connections before issuing any REST request displays
                                                         an Authorization Failed error message. The authentication check done by the reverse proxy gets disabled, but the XMPP authentication is done upstream. |
|---|---|

| Note | These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                             if necessary, in exceptional situations and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| NGX_FIN_UPSTREAM_KEEPALIVE Specifies the proxy backend configurations for Finesse, and activates the cache for connections to an upstream IdS server.
                                          The value sets the maximum number of idle keep-alive connections to upstream servers that are preserved in the cache of each
                                          worker process. When this number is exceeded, the least recently used connections are closed. Default: 128 | No | This default is the optimal value for keeping alive the upstream connection per component. |
| NGX_SET_UPSTREAM_MAX_CONNS To set the maximum connection limit for upstream components. Default: true | No | You can set the value to false when you want to remove the upstream maximum connection limit. Restart the container for the
                                          change to take effect. |
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, Finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                          and idp-adfs3. Default: Finesse | No | Never |
| NGX_FIN_DESKTOP_CACHE_SIZE Specifies the proxy cache configuration for the Finesse desktop and the initial size of the Finesse desktop endpoints cache. Default: 10m | No | The default is the optimal value. |
| NGX_FIN_DESKTOP_CACHE_MAX_SIZE Specifies the maximum size for the Finesse desktop endpoints cache. When the size exceeds or there isn’t enough free space,
                                          it removes the least recently used data. Default: 50m | No | The default is the optimal value. |
| NGX_FIN_DESKTOP_CACHE_INACTIVE_DURATION Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that is not accessed during the
                                          time specified gets removed from the cache regardless of their duration. Default: 3y | No | The default is the optimal value. After this time, the cache contents expire. |
| NGX_FIN_SHINDIG_CACHE_SIZE Specifies the proxy cache configuration for Finesse Shindig and the initial size of the Finesse Shindig endpoints cache. Default: 10m | No |  |
| NGX_FIN_SHINDIG_CACHE_MAX_SIZE Max size for Finesse shindig endpoints cache. When the size exceeds or there isn’t enough free space, it removes the least
                                          recently used data. Default: 500m | No |  |
| NGX_FIN_SHINDIG_CACHE_INACTIVE_DURATION Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that aren’t accessed during the
                                          time specified get removed from the cache regardless of their freshness. Default: 3y | No |  |
| NGX_FIN_OPENFIRE_CACHE_SIZE Specifies the initial size of the Finesse openfire endpoints cache. Default: 10m | No |  |
| NGX_FIN_OPENFIRE_CACHE_MAX_SIZE Specifies the maximum size for the Finesse openfire endpoints cache. When the size exceeds or there isn’t enough free space,
                                          it removes the least recently used data. Default: 10m | No |  |
| NGX_FIN_OPENFIRE_CACHE_INACTIVE_DURATION Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that is not accessed during the
                                          time specified is removed from the cache regardless of their duration. Default: 3y | No |  |
| NGX_FIN_REST_CACHE_SIZE Specifies the initial size of the Finesse REST endpoints cache Default: 10m | No |  |
| NGX_FIN_REST_CACHE_MAX_SIZE Specifies the maximum size for the Finesse REST endpoints cache. When the size exceeds or there isn’t enough free space, it
                                          removes the least recently used data. Default: 1500m | No |  |
| NGX_FIN_REST_CACHE_INACTIVE_DURATION Specifies the content inactive duration for the Finesse desktop endpoints cache. Cached data that is not accessed during the
                                          time specified, get removed from the cache regardless of their duration. Default: 40m | No |  |
| NGX_FIN_LAYOUT_CACHE_SIZE Specifies the initial size of the Finesse layout endpoints cache. Default: 150m | No |  |
| NGX_FIN_LAYOUT_CACHE_MAX_SIZE Specifies the maximum size for the Finesse layout endpoints cache. When the size exceeds or there isn’t enough free space,
                                          the system removes the least recently used data. Default: 300m | No |  |
| NGX_FIN_LAYOUT_CACHE_INACTIVE_DURATION Specifies the inactive duration for content stored in the Finesse desktop endpoints cache. Cached data that aren’t accessed
                                          during the time specified get removed from the cache regardless of their duration. Default: 40m | No |  |
| NGX_FIN_HTTP1_CONN_LIMIT Specifies the number of concurrent HTTP/1.1 connections allowed per source IP Default: 12 | No |  |
| NGX_FIN_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 150 | No |  |
| NGX_FIN_DESKTOP_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for desktop endpoints Default: 50 | No |  |
| NGX_FIN_SHINDIG_CORE_RPC_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for shindig rpc endpoints Default: 40 | No |  |
| NGX_FIN_SHINDIG_IFR_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for shindig ifr endpoints Default: 30 | No |  |
| NGX_FIN_SSOVALVE_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for SSO valve endpoints Default: 5 | No |  |
| NGX_FIN_LIMIT_REQ_STATUS Specifies the HTTP response code to return when the HTTP request rate reaches the limit Default: 429 | No |  |
| NGX_FIN_PROXY_BUFFER_SIZE Specifies the size of the buffer used for reading the first part of the response received from the server, which is enabled
                                          for reverse proxy. Configurations are overridden from the common config for Finesse. Default: 8k | No |  |
| NGX_FIN_MAX_TEMP_FILE_SIZE Applies when buffering of responses from the server (which is enabled for reverse proxy) is enabled. If the whole response
                                          doesn't fit into the buffers set by the NGX_FIN_PROXY_BUFFER_SIZE, the system saves part of the response in a temporary file. Default: 100m | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_CHAT_PORT Specifies the reverse-proxy port over which this chat server is accessed. Default: 5280 | Yes, if necessary. | New installation or if not changed, 5280 is the port for the chat server. | No |
| NGX_PRXY_CHAT_HOSTNAME Specifies the reverse-proxy hostname over which this chat server is accessed. Default: reverseproxy.host.domain | Yes | New installation or if the chat hostname of the reverse-proxy is accessed from the the internet changes. | No |
| NGX_CHAT_HOSTNAME Specifies the hostname of the chat server. Default: chat1.host.domain | Yes | New installation or if the host name of the upstream chat server changes. | No |
| NGX_CHAT_HOST[1-8]_PROXY Required for substituting user home and backup node information in the log-in response. (Similar keys configurations exist for 4 HA clusters of chat servers.) Default: reverseproxy.host.domain:5280/reverseproxy-sub.host.domain:15280 | Yes | New installation or if the chat server proxy hostname FQDN changes. | No |
| NGX_CHAT_HOST[1-8] Specifies the proxy access information for all chat nodes in the deployment. Required for substituting user home and backup
                                                node information in the log-in response. (Similar keys configurations exist for 4 HA clusters of chat servers.) Default: chat[1-4].host.domain/chat[1-4]-sub.host.domain | Yes | New installation or if the chat server upstream hostname FQDN changes. | No |
| NGX_CHAT_BIND_PATH Specifies the binding URL for the chat server. Default: httpbinding | Yes | If the binding URL for the chat server changes. | No |
| NGX_AUTH_URL Specifies the Finesse URL to fetch the users list to perform authentication at proxy. Default: https://proxy.host.domain:8445/finesse/api/UserAuth | Yes | New installation or if proxy.host.domain is the hostname of the the reverse-proxy. | No |

| Note | These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended for changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata. Default: chat | No |  |
| NGX_CHAT_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit. Default: 10 | No |  |
| NGX_CHAT_PORT Specifies the port for the chat server. Default: 5280 | No | New installation or if the port number for the upstream chat server is different. |
| NGX_CHAT_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 30 | No |  |
| NGX_CHAT_HTTP1_CONN_LIMIT Specifies the rate limit for desktop chat, the number of concurrent HTTP/1.1 connections allowed per source IP. Default: 6 | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_CLOUDCONNECT_PORT Specifies the reverse-proxy port over which this Cloud Connect server is accessed. Default: 443 | Yes, if necessary. | If there is a change in the port number. | No |
| NGX_PRXY_CLOUDCONNECT_HOSTNAME Specifies the reverse-proxy hostname over which this Cloud Connect server is accessed. Default: reverseproxy.host.domain | Yes | If there is a change in the chat hostname of the reverse-proxy that has must accessed from the internet. | No |
| NGX_CLOUDCONNECT_HOSTNAME Specifies the hostname for the Cloud Connect server and the hostname of the Publisher or Primary Cloud Connect node. (Conversely
                                                on the alternate side) Default: cloudconnect.host.domain | Yes | If there is a change in the FQDN for the upstream Cloud Connect server. | No |
| NGX_CLOUDCONNECT_FAILOVER_HOSTNAME Specifies the hostname of the Cloud Connect failover node and the hostname of the Subscriber or Secondary Cloud Connect node.
                                                (Conversely on the alternate side) Default: cloudconnct.failover.hostname | Yes | If there is change in the FQDN of the alternate Cloud Connect server. | No |
| NGX_CLOUDCONNECT_CLIENT_IPS Creates a list of known IP addresses for clients connecting to Cloud Connect services like DigitalRouting and UserSync. Default: 35.161.238.252\|35.166.68.236\|34.240.73.178\|3.9.155.97\|54.206.189.15\|52.62.185.51\| 13.210.45.137\|52.40.46.90\|52.214.81.91\|3.9.151.19\|3.105.22.233\|52.17.23.194 | Yes | Validate and update the list when there is a change in the IP addresses. | Yes |

| Note | These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                                if necessary, in exceptional situations and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3. Default: cloudconnect | No |  |
| NGX_CLOUDCONNECT_USER_SYNC_CALLBACK_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for user sync bulk requests. Default: 10 | No |  |
| NGX_CLOUDCONNECT_UPSTREAM_KEEPALIVE Activates the cache for connections to the upstream Cloud Connect server. Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections close. Default: 150 | No |  |
| NGX_CLOUDCONNECT_LIMIT_REQ_STATUS Specifies the HTTP response code to return when the HTTP request rate reaches the limit. Default: 429 | No |  |
| NGX_CLOUDCONNECT_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 250 | No |  |
| NGX_CLOUDCONNECT_HTTP1_CONN_LIMIT Specifies the number of concurrent HTTP/1.1 connections allowed per source IP—the rate limit for Digital Routing requests. Default: 50 | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_TIMEOUT Specifies the timeout for the health check API in milliseconds, if there is a failure. Default: 2000 | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_SSL_VERIFY Specifies whether to verify the SSL certificate for health checks. Default: FALSE | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_RISE Specifies the number of successive health check successes before turning up a peer. Default: 2 | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_RESPONSE_CODES Generates a comma-separated list of valid HTTP status codes for the health check API. Default: {200} | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_INTERVAL Specifies the interval between health checks in milliseconds. Default: 2000 | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_FALL Specifies the number of successive health check failures before turning down a peer. Default: 2 | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_CONCURRENCY Specifies the number of concurrent health checks. Default: 2 | No |  |
| NGX_CLOUDCONNECT_HEALTHCHECK_API Specifies the active health check configurations for the DR API. The system uses this URL to check the health of the Cloud
                                             Connect. Default: /drapi/v1/ping | No |  |
| NGX_CLOUDCONNECT_DR_TASK_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for digital routing tasks. Default: 200 | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_IDS_HOSTNAME Specifies the reverse proxy hostname over which this IdS host is accessed. Default: reverseproxy.host.domain | Yes | New installation or if the reverse proxy IdS hostname changes. | No |
| NGX_PRXY_ALT_IDS_HOSTNAME Specifies the reverse proxy hostname for the IdS failover node associated with this IdS host. This should reference the reverse
                                                proxy node on the alternate side. Default: Empty | Yes, if required. | While deploying the secondary reverse proxy in a high availability mode. | No |
| NGX_PRXY_IDS_PORT Specifies the reverse proxy port over which this IdS host is accessed. Default: 8553 | Yes, if required. | New installation or if the reverse proxy port changes. | No |
| NGX_PRXY_ALT_IDS_PORT Specifies the reverse proxy port for the IdS failover node associated with this IdS host. This should reference the reverse
                                                proxy node on the alternate side. Default: Empty | Yes, if required. | While deploying the secondary reverse proxy in a high availability mode. | No |
| NGX_IDS_HOSTNAME IdS server actual hostname Default: ids.host.domain | Yes | New installation or if the FQDN host name of the IdS server changes. | No |
| NGX_ALT_IDS_HOSTNAME Specifies the Ids hostname for the alternate side. Default: Empty | Yes, if required. | While deploying secondary Ids in a high availability mode. | No |

| Note | These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                                and idp-adfs3. Default: ids | No |  |
| NGX_IDS_UPSTREAM_KEEPALIVE Proxy backend configurations for IDS. Activates the cache for connections to the upstream IDP server. Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                                process. When the count exceeds this number, the least recently used connections close. Default: 128 | No |  |
| NGX_IDS_HTTP1_CONN_LIMIT Rate limits configuration for IdS. Specifies the number of concurrent HTTP/1.1 connections allowed per source IP. Default: 4 | No |  |
| NGX_IDS_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 4 | No |  |
| NGX_IDS_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit. Default: 4 | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_IDP_HOSTNAME Specifies the reverse-proxy hostname over which this IdP host will be accessed. Default: adfs-reverseproxy.host.domain | Yes | New installation or if the FQDN of the reverse-proxy IdP host changes. | No |
| NGX_PRXY_IDP_PORT Specifies the reverse-proxy port over which this IdP host will be accessed. Default: 443 | Yes, If required. | New installation or if unchanged, reverse-proxy uses the 443 port for CUIC. | No |
| NGX_IDP_HOSTNAME Specifies the CUIC server hostname. Default: idp.host.domain | Yes | New installation or if the FQDN of the IdP host changes. | No |

| Note | These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and are not recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3. Default: idp-adfs3 | No |  |
| NGX_IDP_UPSTREAM_KEEPALIVE Proxy backend configurations for IDP. Activates the cache for connections to upstream IDP server Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections close. Default: 128 | No |  |

| Note | Use livedata_12.6(1).env when the upstream Livedata is still on Release12.6(1). Otherwise, use livedata.env. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_LD_HOSTNAME Specifies the reverse-proxy hostname over which this LD host is accessed. Default: reverseproxy.host.domain | Yes | If the reverse-proxy livedata host FQDN changes. | No |
| NGX_PRXY_LD_PORT Specifies the reverse-proxy port over which this livedata host is accessed. Default: 12005 | Yes, If required. | If there is a change in the reverse-proxy port for livedata. | No |
| NGX_PRXY_LD_SCKT_IO_PORT Specifies the reverse-proxy port over which the socket IO endpoint of this livedata host will be accessed. Default: 12008 | Yes, If required. | If there is a change in the reverse-proxy port for socket IO connections. | No |
| NGX_LD_HOSTNAME Specifies the Livedata server hostname. Default: livedata.host.domain | Yes | If there is a change in the upstream livedata host FQDN. | No |
| NGX_LD_SIO_UPSTREAM_KEEPALIVE Activates the cache for connections to the upstream livedata server socketio endpoint. Default: 128 | No | — | No |
| NGX_LD_BACKEND_FAILOVER Livedata failover configuration. This is used to translate the location header during failover. For SideA LiveData, point to SideB LiveData and for SideB Livedata, point to SideA Livedata. | Yes | If there is a change in the FQDN or port. | No |
| NGX_LD_BACKEND_PROXY_FAILOVER Livedata proxy failover configuration. Each side points to the other side of the reverse-proxy node. | Yes | If there is a change in the FQDN or port. | No |

| Note | These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3. Default: livedata_12.6(1) | No | — |
| NGX_LD_WEB_UPSTREAM_KEEPALIVE Proxy backend configurations for livedata. Activates the cache for connections to the upstream livedata server. Specifies the maximum number of idle keep alive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections close. Default: 128 | No | — |
| NGX_LD_SIO_UPSTREAM_KEEPALIVE Activates the cache for connections to the upstream livedata server socketio endpoint. Default: 128 | No | — |
| NGX_LD_HTTP1_CONN_LIMIT Specifies the number of concurrent HTTP/1.1 connections allowed per source IP. Default: 12 | No | — |
| NGX_LD_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 150 | No | — |
| NGX_LD_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit. Default: 25 | No | — |
| NGX_LD_PROXY_BUFFER_SIZE Default: 8k | No | — |
| NGX_LD_MAX_TEMP_FILE_SIZE Default: 100m | No | — |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_LD_HOSTNAME Specifies the reverse-proxy hostname over which this LD host is accessed. Default: reverseproxy.host.domain | Yes | If the reverse-proxy livedata host FQDN changes. | No |
| NGX_PRXY_LD_PORT Specifies the reverse-proxy port over which this livedata host is accessed. Default: 443 | Yes, If required. | If the reverse-proxy port for livedata changes. | No |
| NGX_LD_HOSTNAME Specifies the Livedata server hostname. Default: livedata.host.domain | Yes | If the upstream livedata host FQDN changes. | No |
| NGX_LD_BACKEND_FAILOVER Specifies the livedata failover configurations. This is used to translate the location header during failover. Default: hostname:port | Yes | For the SideA upstream LiveData, point to the upstream SideB LiveData. For the SideB upstream, point to the upstream SideA. | No |
| NGX_LD_BACKEND_PROXY_FAILOVER Specifies the livedata failover node for this livedata host. This is used to translate the location header during failover. Default: hostname:port | Yes | Point to the other side of the reverse-proxy node. | No |

| Note | These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                                if necessary, in exceptional situations and aren’t recommended to be changed casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3. Default: livedata | No |  |
| NGX_LD_WEB_UPSTREAM_KEEPALIVE Proxy backend configurations for livedata. Activates the cache for connections to the upstream livedata server. Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the least recently used connections are closed. Default: 128 | No |  |
| NGX_LD_SIO_UPSTREAM_KEEPALIVE Activates the cache for connections to the upstream livedata server socketIO endpoint. Default: 128 | No |  |
| NGX_LD_HTTP1_CONN_LIMIT Specifies the number of concurrent HTTP/1.1 connections allowed per source IP. Default: 12 | No |  |
| NGX_LD_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 150 | No |  |
| NGX_LD_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit. Default: 25 | No |  |
| NGX_LD_PROXY_BUFFER_SIZE Sets the size of the buffer used for reading the first part of the response received from the server, which is enabled with
                                             reverse-proxy. Default: 8k | No |  |
| NGX_LD_MAX_TEMP_FILE_SIZE When buffering of responses from the server (which is enabled with reverse-proxy) is enabled, and the whole response doesn’t
                                             fit into the NGX_LD_PROXY_BUFFER_SIZE, a part of the response can be saved to a temporary file. Default: 100m | No |  |

| Note | Use this env file when the upstream Unified Intelligence Center is still on 12.6(1) release. Otherwise use cuic.env. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_CUIC_HOSTNAME Specifies the reverse-proxy hostname over which this CUIC host is accessed. Default: reverseproxy.host.domain | Yes | If the reverse-proxy CUIC host FQDN changes. | No |
| NGX_PRXY_CUIC_PORT Specifies the reverse-proxy port over which this cuic host is accessed. Default: 8444 | Yes, If required. | New installation or if the port number changes. | No |
| NGX_PRXY_CUIC_DOC_PORT Specifies the reverse-proxy port over which this CUIC host doc endpoint is accessed. Default: 8447 | Yes, If required. | New installation or if the port number changes. | No |
| NGX_CUIC_HOSTNAME Specifies the CUIC server hostname. Default: cuic.host.domain | Yes | If the upstream CUIC host FQDN changes. | No |

| Note | These properties are provided for reference and they are available in the configuration. They provide flexibility to adjust
                                                the behavior if necessary, in exceptional situations, and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             idp-adfs3. Default: cuic_12.6(1) | No | Never |
| NGX_CUIC_UPSTREAM_KEEPALIVE Activates the cache for connections to the upstream CUIC server. Specifies the maximum number of idle keep alive connections to upstream servers that are preserved in the cache of each worker
                                             process. When this number exceededs, the least recently used connections are closed. Default: 128 | No | — |
| NGX_CUICDOC_UPSTREAM_KEEPALIVE Activates the cache for connections to the upstream CUIC server doc endpoint. Default: 128 | No | — |
| NGX_CUIC_CACHE_SIZE Specifies the initial size of the CUIC proxy cache. Default: 15m | No | — |
| NGX_CUIC_CACHE_MAX_SIZE Specifies the maximum size for the CUIC cache. When the size exceeds or there's not enough free space, the system removes
                                             the least recently used data. Default: 50m | No | — |
| NGX_CUIC_CACHE_INACTIVE_DURATION Specifies the content inactive duration for the CUIC cache. Cached data that is not accessed during the time specified get
                                             removed from the cache regardless of their freshness. Default: 3y | No | — |
| NGX_CUICDOC_CACHE_SIZE Specifies the initial size of the CUIC doc cache. Default: 15m | No | — |
| NGX_CUICDOC_CACHE_MAX_SIZE Specifies the maximum size for the CUIC doc cache. When the size exceeds or there isn’t enough free space, the system removes
                                             the least recently used data. Default: 50m | No | — |
| NGX_CUICDOC_CACHE_INACTIVE_DURATION Specifies the content inactive duration for CUIC doc cache. Cached data that aren’t accessed during the time specified get
                                             removed from the cache regardless of their freshness. Default: 3y | No | — |
| NGX_CUIC_HTTP1_CONN_LIMIT Specifies the number of concurrent HTTP/1.1 connections allowed per source IP. Default: 12 | No | — |
| NGX_CUIC_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 150 | No | — |
| NGX_CUIC_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit. Default: 100 | No | — |
| NGX_CUIC_HISTORICAL_REPORT_CONN_LIMIT Specifies the number of concurrent connections allowed, per source IP, for CUIC historical reports endpoints. Default: 4 | No | — |
| NGX_CUIC_HISTORICAL_REPORT_NEW_CONN_LIMIT Specifies the number of concurrent connections allowed, per source IP, for CUIC historical reports newRest endpoints. Default: 4 | No | — |
| NGX_CUIC_HISTORICAL_REPORT_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for CUIC historical reports endpoints. Default: 4 | No | — |
| NGX_CUIC_REALTIME_REPORT_CONN_LIMIT Specifies the number of concurrent connections allowed, per source IP, for CUIC realtime reports endpoints. Default: 4 | No | — |
| NGX_CUIC_REALTIME_REPORT_NEW_CONN_LIMIT Specifies the number of concurrent connections allowed, per source IP, for CUIC realtime reports newRest endpoints. Default: 4 | No | — |
| NGX_CUIC_REALTIME_REPORT_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for CUIC realtime reports endpoints. Default: 4 | No | — |
| NGX_CUIC_REPORT_EXECUTION_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for CUIC reports execution endpoints. Default: 4 | No | — |
| NGX_CUIC_PROXY_BUFFER_SIZE Specifies the size of the buffer used for reading the first part of the response received from the server, which is enabled
                                             for reverse-proxy. Default: 8k | No | — |
| NGX_CUIC_MAX_TEMP_FILE_SIZE When buffering of responses from the server (which is enabled for reverse-proxy) is enabled, and the whole response doesn't
                                             fit into the buffers set by the NGX_CUIC_PROXY_BUFFER_SIZE, a part of the response is saved to a temporary file. Default: 100m | No | — |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| NGX_PRXY_CUIC_HOSTNAME Specifies the reverse-proxy hostname over which this cuic host is accessed. Default: reverseproxy.host.domain | Yes | If the reverse-proxy CUIC host FQDN changes. | No |
| NGX_PRXY_CUIC_PORT Specifies the reverse-proxy port over which this cuic host is accessed. Default: 443 | Yes, If required. | If the reverse-proxy port changes. | No |
| NGX_CUIC_HOSTNAME Specifies the CUIC server hostname. Default: cuic.host.domain | Yes | If the upstream CUIC host FQDN changes. | No |

| Note | These properties are provided for reference and they exist in the configuration to provide flexibility to adjust the behavior
                                                if necessary, in exceptional situations and aren’t recommended changing casually without extensive testing. |
|---|---|

| Property Name, Description, and Default | Change Recommended? | When to Change? |
|---|---|---|
| TEMPLATE_TYPE Specifies the component template type—valid values are: chat, cuic, finesse, ids, livedata, cuic_12.6(1), livedata_12.6(1),
                                             and idp-adfs3. Default: cuic | No |  |
| NGX_CUIC_UPSTREAM_KEEPALIVE Activates the cache for connections to the upstream CUIC server. Specifies the maximum number of idle keepalive connections to upstream servers that are preserved in the cache of each worker
                                             process. When the count exceeds this number, the system closes the least recently used connections. Default: 128 | No |  |
| NGX_CUIC_CACHE_SIZE Specifies the initial size of the CUIC cache. Default: 30m | No |  |
| NGX_CUIC_CACHE_MAX_SIZE Specifies the maximum size for the CUIC cache. When the size exceeds the set maximum, or there isn’t enough free space, the
                                             system removes the least recently used data. Default: 100m | No |  |
| NGX_CUIC_CACHE_INACTIVE_DURATION Specifies the content inactive duration for the CUIC cache. Cached data that aren’t accessed during the time specified get
                                             removed from the cache regardless of their freshness. Default: 3y | No |  |
| NGX_CUIC_HTTP1_CONN_LIMIT Specifies the number of concurrent HTTP/1.1 connections allowed per source IP. Default: 12 | No |  |
| NGX_CUIC_HTTP2_CONN_LIMIT Specifies the number of concurrent HTTP/2 streams allowed per source IP. Default: 150 | No |  |
| NGX_CUIC_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit. Default: 100 | No |  |
| NGX_CUIC_HISTORICAL_REPORT_CONN_LIMIT Specifies the number of concurrent connections allowed per source IP for CUIC historical reports endpoints. Default: 4 | No |  |
| NGX_CUIC_HISTORICAL_REPORT_NEW_CONN_LIMIT Specifies the number of concurrent connections allowed per source IP for CUIC historical reports newRest endpoints. Default: 4 | No |  |
| NGX_CUIC_HISTORICAL_REPORT_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for CUIC historical reports endpoints. Default: 4 | No |  |
| NGX_CUIC_REALTIME_REPORT_CONN_LIMIT Specifies the number of concurrent connections allowed per source IP for CUIC realtime reports endpoints. Default: 4 | No |  |
| NGX_CUIC_REALTIME_REPORT_NEW_CONN_LIMIT Specifies the number of concurrent connections allowed per source IP for CUIC realtime reports new REST endpoints. Default: 4 | No |  |
| NGX_CUIC_REALTIME_REPORT_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for CUIC realtime reports endpoints. Default: 4 | No |  |
| NGX_CUIC_REPORT_EXECUTION_REQUEST_BURST_LIMIT Specifies the HTTP request burst limit for CUIC reports execution endpoints. Default: 4 | No |  |
| NGX_CUIC_PROXY_BUFFER_SIZE Configurations overridden from common config for CUIC. Specifies the size of the buffer used for reading the first part of the response received from the server, which is enabled
                                             for reverse-proxy. Default: 8k | No |  |
| NGX_CUIC_MAX_TEMP_FILE_SIZE When buffering of responses from the server (which is enabled for reverse-proxy) is enabled, and the whole response doesn’t
                                             fit into the buffers set by the NGX_CUIC_PROXY_BUFFER_SIZE, a part of the response is saved to a temporary file. Default: 100m | No |  |

| Property Name, Description, and Default | Change Recommended? | When to Change? | Hot Reload Supported? |
|---|---|---|---|
| IPTABLES_CONNECTION_LIMIT_ABOVE Specifies the maximum number of parallel connections to reverse proxy per client IP address. Default: Finesse: 10 Chat: 30 Cloud Connect: 8 CUIC: 6 IdP: 8 IdS: 6 LD: 10 | Only if required | Change when you want to increase/decrease the number of parallel connections to reverse proxy per client IP address. | No |
| IPTABLES_HASH_LIMIT_UPTO Specifies the rate/sec at which connection to a port will be accepted. Default: Finesse: 6/sec Chat: 20/sec Cloud Connect: 4/sec CUIC: 2/sec IdP: 4/sec IdS: 2/sec LD: 6/sec | Only if required | Change when you want to increase/decrease the number of requests per second per combination of source IP and destination port. | No |
| IPTABLES_HASH_LIMIT_BURST Specifies the maximum initial number of requests to a port that will be accepted. Default: Finesse: 8 Chat: 25 Cloud Connect: 6 CUIC: 4 IdP: 6 IdS: 4 LD: 8 | Only if required | Change when you want to increase/decrease the maximum initial number of requests. | No |
| IPTABLES_LOG_LIMIT_BURST Specifies the maximum initial number of requests for logging, that are rejected for a port by iptables. Note You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. Default: 1 | Note | You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. | Only if required | Change when you want to increase/decrease logging for the number of requests/min that are not accepted by iptables rule. | No |
| Note | You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. |
| IPTABLES_LOG_LIMIT Specifies the rate of logging the number of requests/min that are rejected for a port by iptables. Note You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. | Note | You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. | Only if required | Change when you want to increase/decrease logging for the number of requests/min that are not accepted by iptables rule. | No |
| Note | You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. |

| Note | You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. |
|---|---|

| Note | You can view the logs for requests rejected by iptables at syslogs → /var/log/messages. |
|---|---|