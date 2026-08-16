---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-1447daab63
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_security-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/security_considerations_for_mobile_agent_deployments.html
retrieved_at: 2026-08-16T14:36:19.345815+00:00
---

Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Security Considerations for Reverse Proxy Deployment

## Chapter: Security Considerations for Reverse Proxy Deployment

# Security Considerations for Reverse Proxy Deployment

## Security Guidelines for Reverse-Proxy Deployment

To enable VPN-less access, reverse proxy hosts must be directly accessible from the internet and therefore needs to be deployed
                              on the edge, where they can be reached via internet based IPs. As the initial ingress point, the proxy plays a significant
                              role in enhancing the security posture of the deployment . Therefore, security is crucial in a reverse-proxy deployment. This
                              section provides a set of guidelines to secure a reverse-proxy deployment.

Note

The guidelines and recommendations provided are intended to be used as a minimum required guidance for administrators to secure
                                          the deployment. The deployment, configuration, and security of reverse-proxy and the network is the Contact Center’s responsibility.

### Reverse Proxy

The reverse proxy is the first application-level landing point for all requests that come into the Cisco Contact Center network
                                 from the internet. Therefore, the reverse proxy must have a high level of security to withstand attacks.

The following are the general set of guidelines to secure a generic reverse proxy deployment:

Note

All these are automatically available and configured when the Reverse Proxy Installer is used.

Configure TLS 1.2 and turn off other TLS protocols.

Ensure only relevant ports are opened to the internet.

Ensure rate limit and connection limit are enforced on upstream access.

Ensure that basic authentication is implemented to authenticate all requests at the edge before they are forwarded to the
                                       respective upstream servers.

Turn off default access and default rules for your proxy to avoid unplanned access to the proxy.

Ensure that the reverse proxy and the host systems are up to date with security patches to prevent potential breaches.

Ensure that the reverse proxy is not allowed to establish direct outbound connections to the internet.

Harden your proxy host to ensure its safety when exposed to the Internet. For best practices, refer to https://www.cisecurity.org/cis-benchmarks/ .

Conduct regular security audits on reverse proxy hosts to ensure that their security has not been compromised.

For security reasons, ensure that API paths other than those explicitly exposed are not available through the configured rules.
                                       If OpenResty Nginx reverse proxy is being deployed, refer to the rules shipped with the Reverse Proxy Installer to find the
                                       paths which are explicitly opened for each category of upstreams such as Finesse, IdS, and CUIC servers, and so on.

Caching is important from a security perspective because most of the static resources are unsecured. Simple DoS attacks can
                                       be prevented by caching these resources on the Finesse server. However, the resources have to be validated periodically with
                                       the Finesse, IdS, and CUIC servers to ensure that the resources are the latest.

Validate the HOST headers to ensure that only the intended domains are accessed by the client.

Regulate the WebSocket connections of Finesse, IdS, and CUIC servers for each domain corresponding to the expected number of clients.

It is a best practice to maintain security hardened golden images of the reverse proxy with updated patches and configuration
                                       changes. Installing from these golden images ensure that all the reverse proxy instances are consistent and are as secure
                                       as possible.

The rules configured should be compared against known vulnerabilities specific to the type of proxy being deployed.

Note

For Nginx-based reverse proxy rules, installation, configuration, and security hardening instructions, refer to the Reverse Proxy Automated Installer chapter in the Cisco Unified Contact Center Enterprise Features Guide . Any reverse proxy supporting the required criteria as mentioned in the above chapter can be used in place of Nginx for supporting
                                             this feature.

### Demilitarized Zone Security

Without an ongoing process and related efforts to ensure that the security of the network and the hosts are updated, a reverse-proxy
                                 deployment cannot maintain its security posture. The following are the important points to ensure that the DMZ is secure:

Consider using dual firewalls (instead of a single firewall with multiple interfaces) to separate the DMZ from the internal
                                       network.

Configure rules in the internal firewall to ensure that the requests originating from the DMZ do not reach hosts other than
                                       the ones configured in the reverse-proxy.

Ensure that the DMZ is separated from the internal network with isolated routing and security policies.

The security of the reverse-proxy deployment depends on the process to keep the configurations and software updated.

### Rate Limit

Finesse, IdS, and CUIC rely on host-level firewall rules for protection from DoS attacks. When reverse-proxy hosts are configured
                                 in these components, they exempt the configured reverse-proxy host from all host-level rate limiting rules. This is to support
                                 the required throughput for the proxy which is serving multiple clients that are connected to it. Therefore, packet rate limits
                                 and request rate limits (if available) should be enforced to ensure that the traffic routed to the hosts through the reverse-proxy
                                 are regulated for each individual IP. This ensures higher availability of the reverse-proxy and the hosts.

Note

Consider imposing general network packet rate limits on ISP routers that connect your network to the DMZ. Implementing rate
                                             limits on the perimeter router is not effective against DoS attacks that are aimed at saturating the ISP links.

For more information on calculating the rate limits, refer to the Determine Scale and Hardware for Proxy section in the Cisco Unified Contact Center Enterprise Features Guide .

### Network Security Devices

Network security devices that incorporate Intrusion Prevention System (IPS) functionality must be deployed to offer additional
                                 security to the traffic that enters the DMZ. These are devices that can prevent entire class of attacks that a proxy or firewall
                                 is not equipped to detect or prevent effectively. While deploying IPS devices, deploy devices that can detect Distributed
                                 Denial of Service (DDoS) signatures to guard against DDoS attacks.

#### Web Application Firewalls

Web Application Firewall (WAF) provides a higher layer of security for reverse-proxy deployments. The WAF devices extend the
                                 security checks into the application layer. This is achieved by inspecting the web application traffic for scripts, headers,
                                 cookies, HTTP methods, and so on to find known vulnerabilities and loopholes to block malicious traffic. This prevents diversified
                                 cyber-attacks that exploit vulnerabilities that are specific to web applications. You can have devices that integrate IPS
                                 and WAF functionalities or use cloud services that provide all the above-mentioned capabilities.

### DDoS Protection

Sophisticated attacks that get past the rate limits by using multiple clients to initiate DoS attacks are referred to as DDoS
                                 attacks. Individual systems are often unable to detect or react properly to DDoS attacks. To avoid such attacks, ensure that
                                 the traffic is regulated by applying proper rate limits.

One of the most effective ways to handle DDoS attacks is to employ Content Distribution Networks (CDN) that provide a high
                                 level of protection against most attacks and can absorb the brunt of these brute force attacks. Incorporating IPS devices,
                                 routers, or a firewall that can detect DDoS signatures can also help in preventing such attacks.

### Reverse Proxy Security Configuration

The following are the additional security enhancements included with the Reverse Proxy Installer:

SELinux Rules – These rules define how processes and users can access system resources like files, devices, and networks. This minimizes
                                       potential damage from compromised processes by providing a more detailed level of security than traditional UNIX file permissions
                                       (read, write, execute).

iptables Rules – Packet processing rules applied to the configured external NIC interface. These rules are used to filter packets against
                                       unsupported or malicious access at the network packet processing level.

Brute Force Attack Prevention – Prevent repeated attempts to guess the user password by systematically trying numerous combinations.

Mutual TLS (mTLS) Verification – mTLS requires that both the server and client be pre-configured with mutual information about each other, as well as that
                                       the mutual certificates be properly verified.

Log Shipping – Automatically copies logs from the primary server to a centralized logging server, so that a crash or an attack on the
                                       primary server doesn't cause loss of information.

Hardened Reverse Proxy Rules – New static rules added in reverse proxy to limit the exposure of upstream servers.

Automatic TCP Rate Limits – TCP rate limits are useful in protecting applications from Denial of Service (DoS) attacks. Linux hosts provide inbuilt
                                       firewall capabilities through the iptables service. The Reverse Proxy Installer uses this iptables service to configure firewall
                                       settings or rate limits for the reverse proxy host.

Request Rate Limits – The proxy configurations are used to check the rate limits at application protocol level (HTTP / HTTP2), providing additional
                                       protection in addition to packet rate limits.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | The guidelines and recommendations provided are intended to be used as a minimum required guidance for administrators to secure
                                          the deployment. The deployment, configuration, and security of reverse-proxy and the network is the Contact Center’s responsibility. |
|---|---|

| Note | All these are automatically available and configured when the Reverse Proxy Installer is used. |
|---|---|

| Note | For Nginx-based reverse proxy rules, installation, configuration, and security hardening instructions, refer to the Reverse Proxy Automated Installer chapter in the Cisco Unified Contact Center Enterprise Features Guide . Any reverse proxy supporting the required criteria as mentioned in the above chapter can be used in place of Nginx for supporting
                                             this feature. |
|---|---|

| Note | Consider imposing general network packet rate limits on ISP routers that connect your network to the DMZ. Implementing rate
                                             limits on the perimeter router is not effective against DoS attacks that are aimed at saturating the ISP links. |
|---|---|