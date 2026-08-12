[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-primary-logo.svg)](https://blog.webex.com)
[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-secondary-logo.svg)](https://blog.webex.com)
  * [Collaboration](https://blog.webex.com/category/collaboration/)
  * [Workspaces](https://blog.webex.com/category/workspaces/)
  * [Customer Experience](https://blog.webex.com/category/customer-experience/)
  * [Event Management](https://blog.webex.com/category/event-management/)
  * [Innovation & AI](https://blog.webex.com/category/innovation-ai/)


[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2079%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles&title=Resilience%20by%20Design:%20How%20Webex%20Contact%C2%A0Center%C2%A0Stays%20Up%20When%20the%20...) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles)
[ ](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/ "Copy Link") [ ](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/ "Print")
[Engineering](https://blog.webex.com/category/engineering/)
# Resilience by Design: How Webex Contact Center Stays Up When the Cloud Wobbles
On Nov 4, 2025Nov 4, 2025By [Iyer Venkataraman](https://blog.webex.com/contributors/ivaidyan/), [Divyesh Khandeshi](https://blog.webex.com/contributors/divyeshkhandeshi/)5 Min Read
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles&title=Resilience%20by%20Design:%20How%20Webex%20Contact%C2%A0Center%C2%A0Stays%20Up%20When%20the%20...) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles)
[ ](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/ "Copy Link") [ ](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/ "Print")
![](https://blog.webex.com/wp-content/uploads/2025/11/conversations-flowing-1.jpg)
Outages happen—even in world-class clouds. Our job isn’t to predict which service might fail next; it’s to ensure customers can always reach agents, no matter what. Webex Contact Center is built to ride through **control-plane turbulence** (DNS resolution timeouts or increased latencies, instance launch failures, increased network latencies, health-check flaps, etc.) and to **degrade gracefully**.
## Resiliency mindset: Setting a high bar in the face of the unknown
Our expectations are that:
  * **Critical Services:** Remain fully operational;**l** ive conversations and routing stay available
  * **Non-Critical Services: May experience brief, bounded impacts,** including analytics, administrative functions, and automated engagement workflows.
  * **Add-On Services: May see partial slowdowns,** such as auxiliary management features and supporting back-office operations.


That’s not luck, it’s by design. It’s built in from the ground up in our event-driven cloud-native microservice-based architecture and processes and is practiced through regularly simulated chaos tests.
## Our thesis: Engineer for classes of failures, not specific services
We don’t harden around “the next EC2/Dynamo/ELB issue,” we design for patterns that recur across services:
  * **Can’t resolve:** DNS misbehaviour or stale answers.
  * **Can’t launch/scale:** New capacity is unavailable or slow to attach.
  * **Propagation lag / out-of-order control state** _:_ Updates may arrive at different times across regions; components serve using last-known-good defaults until state converges.
  * **Health check flaps & scaling thrash:** We filter false alarms and dampen scaling actions (via hysteresis, slow-start) keeping the system steady.


Everything below exists to blunt those patterns.
## The choices that keep us steady
### System & deployment (steady under stress)
  * **Redundant instances in active-active mode across AZs** with critical apps running 3 or more **replicas** spread across **three AZs** —small failure domains beat big ones.
  * **Event-driven, resilient services** and **elastic headroom** , with the ability to **freeze scale changes** during an incident and rely on **pre-provisioned capacity** for hot paths.
  * **No maintenance window** philosophy—changes are designed for zero customer impact for both applications as well as infrastructure changes


### Guardrails (catch issues before they reach customers)
  * Uniform **CI/CD pipelines** , rigorous **code reviews and testing** , and **frequent, small deployments.**
  * **Solution E2E automation for every service** (end-to-end solution tests) and **daily solution load tests** for deployments—with **strict gating** that blocks anything that degrades the end-user experience or solution outcomes.
  * **Automated chaos tests, triggered on demand** , validate real failure modes and exercise runbooks. For a deeper dive into our chaos engineering practices, please refer to the ‘Further Reading’ section at the end of this article.
  * Frequent, manually run **Game Day** chaos events with controlled random failure injections, outside automated tests, simulate real‑world outages and stress conditions. These exercises validate resilience and sharpen incident response.


### Traffic shaping & graceful degradation
  * **Istio service mesh** for mutual TLS, **consistent timeouts and retry algorithms** , circuit breakers, and traffic controls that prevent retry storms.
  * **Application Load Balancer (ALB) with a connection-reuse posture** and aggressive caching to reduce hot-path dependence on a fresh control-plane state.
  * **Steady health checks:** act only on sustained failures, and ramp traffic in/out gradually; with short wait time to prevent reactive scaling.


### Network & egress
  * **Multiple NAT gateways – NAT gateway per AZ** so outbound paths don’t share a single choke point and provide increased resiliency in case of AZ failures.


### Managed vs. self-hosted—on purpose
Each service is chosen after being evaluated for **reliability, cost, and operational attributes** , not just its features. If a managed service’s control plane is risky on a hot path, we will insulate it or avoid it.
### Rearguard (we look for trouble before it finds you)
Across every region where Webex Contact Center runs, we continuously execute automated end-to-end tests for each persona—caller, agent, supervisor, and admin. These checks verify call quality, call controls, and that reporting and configuration behave as expected. If a check fails, we open a proactive incident, bring the right teams onto a bridge, and follow a runbook to diagnose and fix it fast. We do this in all production regions and run regular game-days in a large production-like environment to rehearse and refine our response.
### The coroner (we learn fast and permanently)
  * **24×7 incident response** on a single bridge, timed runbooks, crisp communications.
  * **Postmortems** that update designs and runbooks—no shelfware.


## A case study: October 2025 case study: us-east-1 outage
During a regional event triggered by a DNS race condition, followed by EC2 instance launch failures and load balancer health-check failures, our core experience stayed steady:
  * **No impact to calls.**
  * **No impact to agent logins.**
  * **Brief impact** to **real-time reporting** , **outbound** , and **digital interaction routing**.
  * **Partial degradation** in **recording management** and some **IVR flows**.


### Why the impact remained minimal:
  * We **were not dependent on fresh capacity** mid-incident: scale changes were frozen, and hot paths ran on **pre-provisioned nodes**.
  * Circuit breakers and steady health checks prevented rapid flip-flops when dependencies were noisy.
  * A known playbook: **pause scale changes → enforce mesh policies → activate degradation flags → drain/recover backlogs** —all while keeping voice rock-solid.


## The long game (culture and processes)
  * Culture focused on security and automation
  * **Proactive incidents:** when automated end-to-end checks fail, we open an incident early, trigger auto-mitigations, and page on-call with a runbook
  * Chaos testing for AZ failure, Kafka blips, database failovers, and DNS path issues (see the 6-minute chaos-engineering blog for how we do this in practice)
  * Dependency tiering with budgets, breakers, and fallbacks for every external call
  * Zonal bulkheads and “don’t-cross-the-streams” routing between failure domains
  * Continuous production testing and capacity reviews
  * Automated zero-downtime upgrades for Kubernetes clusters and node pools
  * Vault sidecars to ride through primary secret-store disruptions
  * Karpenter available for native cluster autoscaling
  * CoreDNS auto-scaling with **Cisco Umbrella (formerly OpenDNS)** as upstream resolvers, plus health-checks that automatically failover to secondary/tertiary resolvers while providing centralized DNS visibility.
  * Metrics backend migration to a resilient, horizontally scalable time-series store to harden the monitoring pipeline.
  * Direct Connect monitoring/alerting integrated with VPOPs and Webex Calling
  * Automated certificate lifecycle management and centralized OCSP/CRL checking to reduce tail latency and insulate apps from OCSP/CRL responder outages
  * Strimzi Kafka operator for consistent, secure Kafka operations
  * Careful, staged rollouts with exhaustive pre-flight checks


## Why this matters beyond any single outage
Webex Contact Center is engineered so **customer-critical flows stay alive,** independent of which upstream service is having a bad day.
**We don’t celebrate dodging a broken service.** We celebrate that when the cloud shakes, Webex Contact Center keeps doing the boring, dependable thing: **connecting customers to agents, every time!**
## Further reading
**Adopting Chaos Engineering in Webex Contact Center:** For a deeper dive into our chaos engineering practices, read our 6-minute article on how we implement and benefit from this [critical discipline](https://blog.webex.com/engineering/chaos-engineering-in-webex-contact-center/).
#### About The Authors
![Iyer Venkataraman](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2096%22%3E%3C/svg%3E)
Iyer Venkataraman Cloud Engineering Sr. Technical Lead Cisco
Iyer Venkataraman Vaidyanathan designs and scales test infrastructure for the Webex Contact Center product, combining chaos engineering, UI/API automation, and embedded AI models to improve reliability across product and test systems.
[Learn more](https://blog.webex.com/contributors/ivaidyan/)
![Divyesh Khandeshi](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2096%22%3E%3C/svg%3E)
Divyesh Khandeshi Cloud Architect and Devops Professional Cisco
Cloud architect and Devops professional specializing in AWS, Google Cloud Platform, Kubernetes, Docker and OpenStack. Hands-on experience designing, building, managing and operating Cloud Platforms. Experienced SRE managing and operating Cloud-native products. Java Software Professional with expertise designing and implementing high performance distributed and concurrent, server-sided systems.
[Learn more](https://blog.webex.com/contributors/divyeshkhandeshi/)
#### Topics
[Chaos Engineering](https://blog.webex.com/tag/chaos-engineering/)[Cloud Resilience](https://blog.webex.com/tag/cloud-resilience/)[Control-plane turbulence](https://blog.webex.com/tag/control-plane-turbulence/)[Site Reliability Engineering (SRE)](https://blog.webex.com/tag/site-reliability-engineering-sre/)[Webex Contact Center](https://blog.webex.com/tag/webex-contact-center-2/)
* * *
## More like this
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering Building voice AI that can keep up with real conversations By Gergely Lukacsy, Vibhor Jain5 Min Read ](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/)
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering LRAC Challenge 2025: Pushing the limits of speech coding By Ivana Balic4 Min Read ](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/)
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering Proprietary RTCP Messages and Key Extensions By Rob Hanton8 Min Read ](https://blog.webex.com/engineering/proprietary-rtcp-messages-and-key-extensions/)
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering RTCP Receiver Reports and Stream Synchronization. By Rob Hanton8 Min Read ](https://blog.webex.com/engineering/rtcp-receiver-reports-and-stream-synchronization/)
Products
  * [Webex Suite](https://www.webex.com/suite/collaboration-suite.html)
  * [Meetings](https://www.webex.com/meetings.html)
  * [Calling](https://www.webex.com/enterprise-cloud-calling.html)
  * [Messaging](https://www.webex.com/team-collaboration.html)
  * [Events](https://www.webex.com/events.html)
  * [Video Messaging](https://vidcast.io/)
  * [Polling](https://www.webex.com/suite/polling.html)
  * [Webinars](https://www.webex.com/webinar.html)
  * [Whiteboarding](https://www.webex.com/suite/whiteboard.html)
  * [Cloud Contact Center](https://www.webex.com/us/en/products/customer-experience/contact-center.html)
  * [CPaaS](https://www.webex.com/us/en/products/customer-experience/cpaas.html)


Footer Terms Menu
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
  * [Trademarks](https://www.cisco.com/web/siteassets/legal/trademark.html)
  * [English](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/)


Devices
  * [Room Devices](https://www.webex.com/us/en/devices/room-devices.html)
  * [Desk Devices](https://www.webex.com/us/en/devices/desk-series.html)
  * [Digital Whiteboards](https://www.webex.com/us/en/devices/digital-whiteboards.html)
  * [Phones](https://www.webex.com/us/en/devices/phone-series.html)
  * [Cameras](https://www.webex.com/us/en/devices/cameras.html)
  * [Headsets](https://www.webex.com/us/en/devices/headsets.html)
  * [Room Accessories](https://www.webex.com/us/en/devices/accessories.html)


Resources
  * [Pricing](https://pricing.webex.com/us/en/)
  * [Downloads](https://www.webex.com/downloads.html)
  * [Help Center](https://help.webex.com/)
  * [Webex Community](https://cs.co/webexcommunity)
  * [Product Essentials](https://essentials.webex.com/)
  * [Watch Webinars](https://www.webex.com/learn/webinars-demos.html)
  * [App Hub](https://apphub.webex.com/)
  * [Accessibility](https://www.webex.com/accessibility.html)
  * [Developers](https://developer.webex.com/)


Company
  * [Cisco](https://www.cisco.com/c/en/us/solutions/collaboration/index.html#~stickynav=1)
  * [Webex Customer Advocacy Program](https://www.webex.com/us/en/dg/customer-advocacy-program.html)
  * [Contact Support](https://help.webex.com/contact/)
  * [Contact Sales](https://www.webex.com/contact-sales.html?locale=US)
  * [Webex Merch Store](https://merchandise.cisco.com/featured/webex-by-cisco.html)
  * [Careers](https://www.webex.com/company/careers.html)


  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://twitter.com/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.linkedin.com/company/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.facebook.com/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.youtube.com/c/webex)
  * [ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E) ](https://www.instagram.com/webex/)


©2026 Cisco and/or its affiliates. All Rights Reserved.
  * [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
  * [Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
  * [Cookies](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
  * [Trademarks](https://www.cisco.com/web/siteassets/legal/trademark.html)
  * [English](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/)


By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
