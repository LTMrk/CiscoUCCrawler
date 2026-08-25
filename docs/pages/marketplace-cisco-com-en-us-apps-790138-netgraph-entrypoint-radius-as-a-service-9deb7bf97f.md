---
doc_id: marketplace-cisco-com-en-us-apps-790138-netgraph-entrypoint-radius-as-a-service-9deb7bf97f
source_url: https://marketplace.cisco.com/en-US/apps/790138/netgraph-entrypoint---radius-as-a-service
retrieved_at: 2026-08-25T23:45:30.845758+00:00
---

# Netgraph EntryPoint - Radius-as-a-Service

by Netgraph

Netgraph Entrypoint is a cloud-native RADIUS-as-a-Service platform for Cisco enterprise and Cisco Meraki environments.

The platform supports 802.1X (EAP-TLS, PEAP), MAB, and Cisco-based iPSK authentication, while enabling secure self-service credential distribution and delegated IoT onboarding.

With RADsec secure transport and dynamic return of authorization attributes such as VLAN, SGT, and UDN tags, Entrypoint supports identity-driven micro-segmentation and Zero Trust architectures.

Entrypoint integrates with existing PKI and device management platforms such as Microsoft Intune and is delivered as a fully managed cloud service, eliminating the need for on-premises RADIUS infrastructure.

## Overview

### Netgraph EntryPoint – Cloud RADIUS for Cisco Networks

Netgraph EntryPoint delivers cloud-native, standards-based RADIUS-as-a-Service purpose-built for Cisco and Cisco Meraki network environments. The platform supports 802.1X (EAP-TLS, PEAP), MAC Authentication Bypass (MAB), and Cisco-based iPSK authentication. Organizations can securely distribute encrypted PEAP credentials for BYOD access, enable certificate-based EAP-TLS authentication using certificates issued through their existing PKI or device management platform, and delegate IoT onboarding via built-in self-service workflows. EntryPoint supports RADsec secure transport and dynamically returns authorization attributes such as VLAN, SGT, and UDN tags to enable identity-driven micro-segmentation and scalable Zero Trust architectures. As a fully managed cloud service, EntryPoint allows organizations to activate authentication services within minutes while maintaining centralized governance and audit visibility.

### Key benefits

- 802.1X Authentication Framework EntryPoint provides enterprise-grade 802.1X authentication across Cisco wired and wireless networks. As a standards-based RADIUS implementation, it supports interoperable 802.1X deployments while remaining optimized for Cisco environments. Certificate-based EAP-TLS authentication integrates with certificates issued by the organization’s existing PKI or device management platform (e.g., Microsoft Intune). EntryPoint focuses on authentication and policy enforcement, while certificate enrollment and lifecycle management remain under customer control.

- Cisco iPSK & IoT Authentication EntryPoint supports Cisco-based identity PSK (iPSK) and MAC Authentication Bypass (MAB), enabling secure onboarding of IoT and non-802.1X devices in Cisco environments. The iPSK implementation is optimized for Cisco enterprise and Cisco Meraki networks and integrates with the built-in self-service workflow.

- Dynamic RADIUS Attributes & Micro-Segmentation EntryPoint dynamically returns authorization attributes to network infrastructure during authentication, enabling identity-driven segmentation and policy enforcement. This includes VLAN assignment, Cisco Security Group Tags (SGT), UDN tags, and other vendor-specific RADIUS attributes supported by Cisco environments. Combined with RADsec support for secure transport, EntryPoint enables scalable micro-segmentation and Zero Trust architectures.

- Built-In Self-Service & Delegated Administration EntryPoint includes a native self-service portal enabling secure credential distribution and delegated device onboarding without granting access to network infrastructure configuration. Organizations can distribute encrypted PEAP accounts for consultants and employees, allow designated administrators to manage onboarding, and delegate Cisco iPSK device registration for IoT environments.

- Cloud-Native Deployment & Operational Visibility EntryPoint is delivered as a fully managed cloud service with rapid activation and no on-premises RADIUS infrastructure requirements. The dedicated RADIUS administration portal provides full authentication audit trails, real-time statistics, and operational insight.

- Intune Compliance & Device Validation EntryPoint integrates with Microsoft Intune to validate device compliance during authentication. Compliance validation occurs in real time and is included within the standard endpoint license. When combined with certificate-based authentication through enterprise PKI enrollment, organizations can enforce identity and device posture as part of a unified Zero Trust access model.

- Use Cases Practical scenarios where organizations use Netgraph EntryPoint to implement certificate-based authentication, secure BYOD access, delegated IoT onboarding, and identity-driven micro-segmentation across Cisco network environments.

- FAQ Common questions regarding deployment, authentication methods, self-service capabilities, and integration with Cisco network environments.

## Features

### 802.1X Authentication Framework

EntryPoint provides enterprise-grade 802.1X authentication across Cisco wired and wireless networks. As a standards-based RADIUS implementation, it supports interoperable 802.1X deployments while remaining optimized for Cisco environments. Certificate-based EAP-TLS authentication integrates with certificates issued by the organization’s existing PKI or device management platform (e.g., Microsoft Intune). EntryPoint focuses on authentication and policy enforcement, while certificate enrollment and lifecycle management remain under customer control.

#### EAP-TLS (Machine & User Certificates)

- Support for device and user certificate authentication using enterprise PKI-issued certificates.

#### EAP-TLS with Microsoft Entra ID Backend

- Identity validation and lookup via Entra ID integration.

#### EAP-PEAP for Encrypted BYOD

- Secure credential-based authentication over encrypted transport.

#### Standards-Based RADIUS Operation

- Full support for standard RADIUS attributes and authentication flows.

#### Highlights

- - Standards-aligned implementation - Encrypted BYOD or Consultant access - Machine & User certificate support - Identity-first authentication

### Cisco iPSK & IoT Authentication

EntryPoint supports Cisco-based identity PSK (iPSK) and MAC Authentication Bypass (MAB), enabling secure onboarding of IoT and non-802.1X devices in Cisco environments. The iPSK implementation is optimized for Cisco enterprise and Cisco Meraki networks and integrates with the built-in self-service workflow.

#### Cisco Enterprise iPSK Support

- Identity-based PSK authentication for Cisco enterprise wireless deployments.

#### Cisco Meraki iPSK Support

- Integration with Cisco Meraki identity-based PSK frameworks.

#### MAC Authentication Bypass (MAB)

- Secure onboarding for non-802.1X capable devices.

#### Delegated IoT Onboarding via Self-Service

- Distributed device registration without granting infrastructure access.

#### Credential Lifecycle Management

- Centralized creation, rotation, and revocation of PSK credentials.

#### Policy-Based IoT Segmentation

- Combine iPSK authentication with dynamic RADIUS attribute return for VLAN, SGT, UDN-tags and other segmentation control.

### Dynamic RADIUS Attributes & Micro-Segmentation

EntryPoint dynamically returns authorization attributes to network infrastructure during authentication, enabling identity-driven segmentation and policy enforcement. This includes VLAN assignment, Cisco Security Group Tags (SGT), UDN tags, and other vendor-specific RADIUS attributes supported by Cisco environments. Combined with RADsec support for secure transport, EntryPoint enables scalable micro-segmentation and Zero Trust architectures.

#### Dynamic VLAN Assignment

- Policy-based VLAN allocation per identity group or device.

#### SGT / TrustSec Tag Support

- Return Cisco Security Group Tags for scalable segmentation.

#### UDN & Attribute-Based Authorization

- Support for advanced authorization attributes.

#### RADsec (RADIUS over TLS)

- Secure encrypted RADIUS transport.

#### Highlights

- - Secure RADsec & IPsec transport - Zero Trust-ready architecture - Supports Cisco SGT, UDN, ACL & VLAN enforcement - Enables identity-based micro-segmentation

### Built-In Self-Service & Delegated Administration

EntryPoint includes a native self-service portal enabling secure credential distribution and delegated device onboarding without granting access to network infrastructure configuration. Organizations can distribute encrypted PEAP accounts for consultants and employees, allow designated administrators to manage onboarding, and delegate Cisco iPSK device registration for IoT environments.

#### PEAP Credential Distribution

- Secure account provisioning for encrypted BYOD access.

#### Delegated Cisco iPSK Registration

- Distributed onboarding of IoT devices for Cisco networks.

#### Scoped Administrative Roles

- Role-based access per user group or device category.

#### Credential Retrieval Portal

- End-users securely retrieve and manage credentials.

#### Highlights

- - Reduces IT workload

- - Secure onboarding without exposing network config

- - Enables distributed administration

- - Unique built-in self-service capability

### Cloud-Native Deployment & Operational Visibility

EntryPoint is delivered as a fully managed cloud service with rapid activation and no on-premises RADIUS infrastructure requirements. The dedicated RADIUS administration portal provides full authentication audit trails, real-time statistics, and operational insight.

#### Fully Managed RADIUS Infrastructure

- Cloud-hosted, high-availability RADIUS control plane.

#### Rapid Service Activation

- Provision and activate authentication services within minutes.

#### High Availability & Redundancy

- Distributed architecture for enterprise resilience.

#### Full RADIUS & API Audit Trail

- Detailed authentication logs with timestamp, identity, and policy match visibility.

#### Authentication Metrics & Reporting

- Real-time statistics for monitoring and troubleshooting.

#### Secure RADIUS Transport (RADsec)

- Encrypted RADIUS communication over TLS.

#### Centralized Administration Portal

- Single-pane-of-glass operational management interface.

#### Multi-Language Support

- Localized self-service interfaces.

#### Highlights

- - Deploy within minutes - No server maintenance - Complete authentication transparency - Enterprise-grade reporting

### Intune Compliance & Device Validation

EntryPoint integrates with Microsoft Intune to validate device compliance during authentication. Compliance validation occurs in real time and is included within the standard endpoint license. When combined with certificate-based authentication through enterprise PKI enrollment, organizations can enforce identity and device posture as part of a unified Zero Trust access model.

#### Microsoft Intune Compliance Validation

- Validate device compliance state during RADIUS authentication.

#### Conditional Access Enforcement

- Deny or restrict network access based on compliance state.

#### Integrated Entra ID Identity Context

- Combine user identity and device posture for authentication decisions.

#### No Additional Compliance Licensing Tier

- Included within the standard endpoint license.

#### Zero Trust Alignment

- Enforce device posture verification as part of authentication flow.

#### Real-Time Policy Evaluation

- Compliance validation performed during authentication, not post-session.

### Use Cases

Practical scenarios where organizations use Netgraph EntryPoint to implement certificate-based authentication, secure BYOD access, delegated IoT onboarding, and identity-driven micro-segmentation across Cisco network environments.

#### Use Case 1 – Certificate-Based Corporate Device Access

- Organizations enrolling corporate devices through enterprise PKI or cloud-based certificate services such as Microsoft Intune Cloud PKI can use Entrypoint to enforce secure EAP-TLS authentication. Entrypoint leverages certificates issued by the organization’s existing enrollment solution and focuses on authentication, authorization, and dynamic attribute enforcement. During authentication, VLAN, SGT, and other RADIUS attributes can be returned to enable scalable micro-segmentation.

#### Use Case 2 – Secure BYOD for Consultants & Employees

- Organizations providing encrypted network access to consultants and employees can distribute secure PEAP credentials via built-in self-service. Entrypoint enables encrypted BYOD access without certificate enrollment complexity, while maintaining centralized authentication control and full audit visibility.

#### Use Case 3 – Delegated IoT Onboarding

- Departments and external vendors often need to onboard non-802.1X devices without access to network configuration. Entrypoint supports Cisco-based iPSK and MAB workflows, combined with delegated self-service registration. Dynamic VLAN or segmentation attributes can be returned during authentication to ensure policy alignment.

#### Use Case 4 – Identity-Driven Micro-Segmentation

- Modern network architectures require identity-based segmentation rather than static VLAN design. Entrypoint dynamically returns VLAN, SGT, and other RADIUS attributes during authentication, enabling scalable micro-segmentation across Cisco wired and wireless environments.

#### Use Case 5 – Rapid Cloud-Based RADIUS Deployment

- Organizations modernizing authentication infrastructure can deploy Entrypoint within minutes as a fully managed cloud service. Without maintaining on-prem RADIUS servers, enterprises can activate certificate-based authentication, Entra ID integration, Intune compliance validation, and delegated onboarding workflows through a unified platform.

### FAQ

Common questions regarding deployment, authentication methods, self-service capabilities, and integration with Cisco network environments.

#### Q: Does Entrypoint require on-premises RADIUS servers?

- No. EntryPoint is delivered as a fully managed cloud service. Organizations can activate RADIUS functionality within minutes without deploying or maintaining on-premises RADIUS infrastructure.

#### Q: Does EntryPoint support Cisco network environments?

- Yes. EntryPoint supports Cisco enterprise infrastructure and Cisco Meraki deployments, including 802.1X, MAB, and Cisco-based identity PSK (iPSK) authentication models.

#### Q: Does the platform support certificate-based authentication (EAP-TLS)?

- Yes. EntryPoint supports EAP-TLS for both machine and user certificates issued through the organization’s existing PKI or device management solution, such as Microsoft Intune Cloud PKI or enterprise certificate services.

#### Q: Does Entrypoint provide certificate enrollment services?

- No. EntryPoint operates as a RADIUS authentication and policy platform. Certificate issuance and lifecycle management are handled by the organization’s existing PKI or device management system. EntryPoint integrates seamlessly with PKI-enrolled certificates.

#### Q: Does EntryPoint integrate with Microsoft Entra ID and Intune?

- Yes. EntryPoint supports identity validation through Microsoft Entra ID and can perform real-time Intune device compliance validation during authentication. Compliance validation is included within the standard endpoint license.

#### Q: Does EntryPoint return dynamic RADIUS attributes?

- Yes. Entrypoint can dynamically return authorization attributes such as VLAN assignment, Cisco Security Group Tags (SGT), UDN tags, and other RADIUS attributes to enable identity-driven segmentation and micro-segmentation policies.

#### Q: Is RADsec supported?

- Yes. EntryPoint supports RADsec (RADIUS over TLS) to provide secure, encrypted RADIUS transport between network infrastructure and the cloud service.

#### Q: Does the platform include self-service capabilities?

- Yes. EntryPoint includes a built-in self-service portal for distributing PEAP credentials, delegating Cisco iPSK device registration, and enabling scoped administrative workflows without granting access to network configuration.

#### Q: How is licensing structured?

- EntryPoint is delivered using a single endpoint license model. All core functionality — including 802.1X authentication, self-service workflows, Intune compliance validation, dynamic RADIUS attributes, and RADsec support — is included without tiered feature add-ons.

## Resources

EntryPoint Presentation Download PDF

#### EntryPoint Presentation

## Get started with Netgraph EntryPoint - Radius-as-a-Service