---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-design-guide-b-12xcucdg-b-12xcucdg-chapter-010101-html-4332eb8244
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg/b_12xcucdg_chapter_010101.html
retrieved_at: 2026-08-17T02:34:59.772443+00:00
---

Design Guide for Cisco Unity Connection 12.x

# Design Guide for Cisco Unity Connection 12.x

Updated: August 17, 2017

Chapter: Tenant
	 Partitioning

## Chapter: Tenant
	 Partitioning

# Tenant
                     	 Partitioning

If Unity Connection
                        		server is being shared by N (N=2, 3, 4….) tenants for voicemail service, each
                        		tenant can be setup as a separate "tenant" that is effectively isolated from
                        		other tenant hosted on the same server. Hence, a tenant entity refers to
                        		logical group of resources in Unity Connection assigned to a single company,
                        		where each tenant is assigned with only one partition, search space, and phone
                        		system.

Tenant partitioning
                        		also introduces the concept of using the corporate email addresses as their
                        		alias, which enables alias uniqueness across tenants. In addition, separate
                        		Unity Connection SMTP domain is provided for each tenant.

## Supported Tenant
                        	 Partitioning Topology

Figure 7-1 Sample
                           		Deployment scenario depicts the high level topology or deployment scenario that
                           		is being followed for tenant partitioning. Here, tenant 1 and tenant 2 have
                           		unique phone systems to identify inbound and outbound voicemail traffic. Each
                           		tenant has its own dedicated Cisco Unified Communication Manager.

Here each tenant has its own partition, schedule set, schedule,
                           		schedule detail, search space, search space member, phone system, class of
                           		service, user template, distribution list, distribution list membership, user
                           		operator, call handler template, directory handler, interview handler, call
                           		handlers (operator, opening greeting, Good Bye), and routing rules.

## Licensing

The tenant partitioning implementation does not require any additional licenses.

## Scalability

Tenant Partitioning is a feature that offers a voice messaging
                           		solution for up to 60 tenants where each tenant can have maximum of 100 users
                           		on the Cisco Unity Connection 7vCPU OVA. For more information, see the “ Specifications for Virtual
                              		  Platform Overlays for Currently Shipping Unity Connection Servers ”
                           		section of the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

## Limitations of Tenant Partitioning

The following is the list of limitations of Tenant Partitioning:

Each tenant is associated with only one phone system and Cisco Unified Communications Manager.

Any other kind of networking like Diginet or VPIM is not supported.

There is no way to share ports between multiple tenants. Each tenant has dedicated pool of ports.

Overlapping extensions within a tenant is not supported.

Any configurations done at the system level is not supported.

At least one user in each tenant has to assign role of Greeting administrator so that tenant can customize their greetings.

Tenants have to provide users alias as corporate email address to maintain uniqueness of alias across tenants.

SAML SSO (Security Assertion Markup Language Single Sign-On) access feature in Unity Connection 10.0(1) and later releases
                                 are not supported with tenant partitioning.

Multi-tenancy mode is not turned ON if there is any non-tenant user.

Each object of tenant (like call handlers, directory handlers) should be mapped to object related to that tenant only.

Custom keypad mappings are shared among all tenants.

| Note | If
                                    		you are upgrading Unity Connection 10.0(1) with Tenant Partitioning configured
                                    		to a higher release then the Tenant Partitioning feature remains enabled on the
                                    		upgraded system also. |
|---|---|