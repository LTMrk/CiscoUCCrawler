---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-user-guide-ccvp-b-1-080d7b3f0a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/user/guide/ccvp_b_1501_user-guide-for-unified-cvp-vxml-server-and-unified-cvp-call-studio-release/rcct_m_1501-cvp-port-usage-api.html
retrieved_at: 2026-08-21T17:36:59.639937+00:00
---

User Guide for Unified CVP VXML Server and Unified CVP Call Studio, Release 15.0(1)

# User Guide for Unified CVP VXML Server and Unified CVP Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: CVP Port Usage API

## Chapter: CVP Port Usage API

# CVP Port Usage API

## Overview

The CVP Port Usage API is a RESTful interface that delivers real-time insights into Cisco Unified Customer Voice Portal (CVP)
                           VXML server license utilization. It aggregates license usage data from all deployed VXML servers, providing both a consolidated
                           overview and detailed, segregated information for each individual server, enabling customers to easily monitor license consumption
                           across their entire deployment.

By providing essential capacity and live usage metrics, this API empowers contact centers to optimize resource allocation,
                           refine business logic such as campaign management, and boost overall operational efficiency.

With the introduction of the CVP Port Usage API, modern outbound campaigns can now address and overcome previous limitations,
                           leading to more efficient operations:

Oversubscription or Underutilization : Difficulty in accurately managing CVP port usage led to either oversubscribing ports (resulting in dropped calls when agents
                                 were unavailable) or underutilizing valuable resources.

Lack of Real-time Visibility : Contact center administrators lacked real-time insight into port capacity and usage, making it difficult to react quickly
                                 to changing demands.

Business Logic Limited by Resource Availability : Due to reliance on available resources rather than accurate, real-time data, outbound campaign planning was inefficient,
                                 resulting in suboptimal performance and customer dissatisfaction.

The CVP Port Usage API offers the following capabilities:

Real-time Metrics : Provides both current capacity and live usage metrics for CVP ports.

Dynamic Polling : The API endpoint can be polled at any time to assess current usage against capacity.

Threshold-based Alerts : Supports triggering alerts when predefined usage thresholds are met, preventing overloads or underutilization.

Aggregated and Per-Server Data : Offers both a consolidated view and detailed information for individual VXML servers.

Fine-Grained Real-Time Data Availability : Provides highly granular, real-time availability data with per-second accuracy.

High-performance Caching : Utilizes in-memory caching for efficient data retrieval.

High Availability (HA) : Built with high availability, the API ensures uninterrupted access to critical data, supporting resilient operations.

### Configure CVP Port Usage

For more information on configuring the CVP port usage, see the Configure CVP Port Usage section of the VXML Server Configuration chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Manage CVP Port Usage

For more information on monitoring and managing license usage across your CVP deployment, see License Usage APIs section of the CVP REST API Developer Guide at https://developer.cisco.com/docs/customer-voice-portal/cvp-rest-api-dev-guide/ .

## CVP Port Usage

Cisco Unified Customer Voice Portal (CVP) ports are a critical resource in the contact center environment, enabling concurrent
                           IVR call processing. Effective management and real-time monitoring of CVP port usage help optimize capacity planning, license
                           compliance, and operational visibility. Integrating port usage tracking into the solution architecture ensures accurate reporting
                           and responsive scaling as business needs evolve.

To enable real-time insight into port utilization, a RESTful API has been introduced to provide telemetry on CVP port usage
                           throughout the deployment. The API delivers the following essential data points:

Total available ports on the system

Ports currently in use (active IVR sessions)

Total entitled self-service ports (per customer license)

The CVP Port Usage architecture leverages the following:

Caller : Initiates calls to the contact center, consuming a CVP port for the duration of IVR interactions.

VXML Server : Hosts IVR applications and manages session lifecycles. Each active session corresponds to a CVP port in use.

Port Usage Publisher : Publishes the license utilization information through a secure RESTful interface, making the data available to authorized
                                 clients via the CVP Port Usage API.

API Server : Receives, aggregates, and caches port usage metrics, exposing them via REST APIs for consumption.

Cache Service : Provides a time-windowed view (e.g., 15 seconds) of recent port usage, enabling near-real-time reporting with minimal performance
                                 impact.

License Entitlement Data Store : Stores customer license entitlements for correlation with usage.

Authentication Services : Supports both basic authentication and JWT-based authentication, with validation via an external public key provider.

External Users : Customers or partners accessing port usage data via API.

## High Availability of the Cache Service for the CVP Port Usage API

The Cache Service is a core dependency of the CVP Port Usage API, providing a sliding time-windowed view (for example, 15
                           seconds) of recent port usage data. This capability enables near-real-time visibility into total available ports, ports currently
                           in use, and total entitled self-service ports across the deployment.

To eliminate a single point of failure, the system supports a high-availability (HA) cache architecture with Primary and Secondary
                           Cache Service instances. This ensures uninterrupted access to real-time CVP port usage metrics through automatic failover.

The high-availability cache architecture for the CVP Port Usage API comprises of the following components that work together
                           to ensure uninterrupted access to real-time port usage metrics.

The VXML Server hosts IVR applications and is responsible for pushing port usage data to the Cache Service over gRPC. It is
                                 preconfigured with connection details for both the Primary and Secondary Cache Service endpoints, enabling it to seamlessly
                                 redirect traffic during a failover event.

The API Server is deployed as a high-availability pair behind a load balancer. It hosts the Cache Service and exposes port
                                 usage metrics via REST APIs, allowing both internal and external consumers to retrieve real-time data on CVP port utilization.

The Cache Service stores recent port usage data in a sliding time window (for example, 15 seconds) using in-memory caching
                                 for efficient data retrieval. It is deployed as Primary and Secondary instances to eliminate a single point of failure and
                                 ensure continuous data availability.

The Load Balancer distributes external API traffic between the Primary and Secondary API Server instances based on health
                                 checks. It plays a critical role in detecting endpoint failures and redirecting traffic to the healthy instance during failover
                                 scenarios.

The External Authentication Server provides the public key used for JWT-based token validation, ensuring that external API
                                 consumers, such as customers or partners accessing CVP port usage data are securely authenticated before accessing the API.

How Failover Works

During normal operation, the VXML Server pushes port usage data to the Primary Cache Service endpoint over gRPC, while the
                           Load Balancer routes all external CVP Port Usage API traffic to the Primary API Server. Both the VXML Server and the Load
                           Balancer continuously monitor the health of the Primary and Secondary endpoints using a heartbeat mechanism to ensure availability.

If the heartbeat mechanism detects that the Primary endpoint is no longer responding, failover is initiated automatically.
                           The VXML Server redirects its gRPC data stream to the Secondary Cache Service endpoint, and the Load Balancer redirects all
                           incoming REST API traffic to the Secondary API Server. This ensures that the CVP Port Usage API continues to serve real-time
                           port usage metrics including total available ports, ports currently in use, and total entitled self-service ports with minimal
                           or no interruption to API consumers.

When the Primary endpoint becomes available again, the heartbeat mechanism detects its recovery and marks it as active. The
                           VXML Server and the Load Balancer then restore traffic to the Primary endpoint, resuming the original traffic flow.

For more information on High Availability of Cache Service, see CVP REST API Developer Guide at https://developer.cisco.com/docs/customer-voice-portal/ha-cache-container-samples/ .