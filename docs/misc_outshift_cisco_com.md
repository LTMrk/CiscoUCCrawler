

---
# ORIGEN: https://outshift.cisco.com/blog/multi-agentic-systems-agntcy-application-sdk-reference-application

[![Outshift Logo](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/outshift-logo-text-white.svg)](https://outshift.cisco.com/)
  * Initiatives
  * About us
  * [Blog](https://outshift.cisco.com/blog)
  * Tools
  * Case studies


[](https://outshift.cisco.com/blog/search)
AI/ML
![clock icon](https://outshift.cisco.com/images/graphics/clock-icon.png)
3 min read
# Building multi-agentic systems with AGNTCY's Application SDK and reference application
![Blog thumbnail](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CoffeeAGNTCY.webp)
![Border Image](https://outshift.cisco.com/images/graphics/middle-diamond.png)
Building multi-agentic systems with AGNTCY's Application SDK and reference application
Share
![Luke Tucker](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/luke-headshot-square.png)
by [Luke Tucker](https://outshift.cisco.com/blog/author/luke-tucker)
Published on 07/23/2025Last updated on 03/13/2026
![clock icon](https://outshift.cisco.com/images/graphics/clock-icon.png)
3 min read
### Table of contents
  * [Watch the overview video below for more details:](https://outshift.cisco.com/blog/ai-ml/agntcy-sdk-multi-agent-systems-reference#watch-the-overview-video-below-for-more-details--0)
  * [Get started with the Corto demo](https://outshift.cisco.com/blog/ai-ml/agntcy-sdk-multi-agent-systems-reference#get-started-with-the-corto-demo-1)
  * [Building with the AGNTCY App SDK](https://outshift.cisco.com/blog/ai-ml/agntcy-sdk-multi-agent-systems-reference#building-with-the-agntcy-app-sdk-2)
  * [Shape the future of open agentic development with AGNTCY](https://outshift.cisco.com/blog/ai-ml/agntcy-sdk-multi-agent-systems-reference#shape-the-future-of-open-agentic-development-with-agntcy-3)


Share:
Today, we are pleased to announce the launch of the multi-agent software reference application we call [coffeeAGNTCY,](https://github.com/agntcy/coffeeAgntcy) as well as an [Application SDK](https://github.com/agntcy/app-sdk). 
CoffeeAGNTCY is the fastest way to experiment within the agentic open source ecosystem. See how to build multi-agent software with Model Context Protocol (MCP), Agent2Agent (A2A), and AGNTCY components. It's where “hello world” meets “hello agents.”
The reference application muse is a fictional global coffee enterprise. Open source reference applications are not new. Just like the cloud native Sock Shop began as a simple demo app, then grew into a fully containerized, cloud native reference application, we are starting small with coffeeAGNTCY.
The first version has a simple two-agent system we call Corto, and a full multi-agent simulation with different patterns of communication, which we call Lungo. 
> "The coffeeAGNTCY reference application is a great launchpad for us to implement AGNTCY components in our latest project. The easy-to-follow [ReadMe](https://github.com/agntcy/coffeeAgntcy/tree/main/coffeeAGNTCY/coffee_agents/corto) and ready-made Docker compose files are super convenient," said Amogh Tarcar, Senior Data Scientist at Persistent.
### Watch the overview video below for more details:
The coffeeAGNTCY is built to be extensible for everyone building multi-agent applications and is designed to support ALL open source protocols for a multi-agent system. 
### Get started with the Corto demo
We recommend starting with the [Corto ReadMe](https://github.com/agntcy/coffeeAgntcy/tree/main/coffeeAGNTCY/coffee_agents/corto). Here, we demonstrate the integration of an A2A client within a LangGraph workflow with an A2A server agent. It models a simplified agent system that acts as a coffee sommelier.
  * The exchange agent acts as a client interface, receiving prompts from the user interface about coffee flavor profiles and forwarding them to the farm agent.
  * The farm agent serves as a backend flavor profile generator, processing incoming requests and returning descriptive output.


The user interface forwards all prompts to the exchange’s API, which are then given to a LangGraph which contains an A2A client node. This A2A client node connects to the farm’s A2A server. The underlying A2A transport layer is fully configurable. By default, the system uses AGNTCY's SLIM (Secure Low-latency Interactive Messaging), but it’s built to be interoperable, so you can use NATS, Kafka, or your preferred messaging protocol.
You can use Corto in two ways: Local Python which runs each component directly on your machine or via Docker Compose which will quickly spin up all components as containers. 
### **Building with the AGNTCY App SDK**
The AGNTCY Application SDK provides a convenient way to integrate with AGNTCY components, beginning with [SLIM](https://github.com/agntcy/slim) and later expanding to incorporate many others including , and . All this while enabling interoperability with agentic protocols such as A2A and Model Context Protocol.  
| To start with, the App SDK covers all the following:   | Coming Soon:   |  
| --- | --- |  
| ✅ A2A over SLIM   | 🕐 A2A over MQTT  |  
| ✅ A2A over NATS   | 🕐 Identity provider   |  
| ✅ Request-reply   | 🕐 Observability provider   |  
| ✅ Publish-subscribe   |   |  
| ✅ MCP client factory   |   |  
Stay tuned for more coming soon!
### Shape the future of open agentic development with AGNTCY
Helping the world build multi-agentic systems with open source solutions is one of our passions here at Outshift. The future doesn’t build itself, and we're excited to create foundational tools to empower technologists to create. And we don’t do it alone: dozens of companies have joined AGNTCY with the same vision, building an open, interoperable internet of agents. To get involved in building AGNTCY with us, contribute to and . 
[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[In-depth Tech](https://outshift.cisco.com/blog/topic/in-depth-tech)[Open Source](https://outshift.cisco.com/blog/topic/open-source)
### Welcome to the future of agentic AI: The Internet of Agents
Outshift is leading the way in building an open, interoperable, agent-first, quantum-safe infrastructure for the future of artificial intelligence.
[Download Whitepaper](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Internet_of_Agents_Whitepaper.pdf)
* No email required
![thumbnail](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/crea-838.webp)
[Download Whitepaper](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Internet_of_Agents_Whitepaper.pdf)
* No email required
## Related articles
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Service_Now_Use_Case_Blog_4dd2b7727e.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML ServiceNow and Outshift by Cisco are untangling the multi-agent enterprise ](https://outshift.cisco.com/blog/ai-ml/service-now-outshift-multi-agent-enterprise)
[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[Open Source](https://outshift.cisco.com/blog/topic/open-source)[AI/ML](https://outshift.cisco.com/blog/topic/artificial-intelligence)[Use Case](https://outshift.cisco.com/blog/topic/use-case)[In-depth Tech](https://outshift.cisco.com/blog/topic/in-depth-tech)[Strategy & Insights](https://outshift.cisco.com/blog/topic/strategy-insights)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/coffee_AGNTCY_Digital_Realty_9a1e0af194.webp) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML Scaling multi-agent systems: coffeeAGNTCY in Digital Realty's Lab ](https://outshift.cisco.com/blog/ai-ml/multi-agent-systems-coffeeagntcy-digital-realty)
[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[Open Source](https://outshift.cisco.com/blog/topic/open-source)[In-depth Tech](https://outshift.cisco.com/blog/topic/in-depth-tech)[Use Case](https://outshift.cisco.com/blog/topic/use-case)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA-999%20AIML%20generic_V21.webp) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML AI observability in multi-agent systems using OpenTelemetry](https://outshift.cisco.com/blog/ai-ml/ai-observability-multi-agent-systems-opentelemetry)
[In-depth Tech](https://outshift.cisco.com/blog/topic/in-depth-tech)[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[Open Source](https://outshift.cisco.com/blog/topic/open-source)
![Another Image](https://outshift.cisco.com/images/graphics/middle-diamond.png)
![Subscribe](https://outshift.cisco.com/images/pages/home/subscribe-logo.svg)
Subscribe to 
The Shift
!
Get 
emerging insights
on innovative technology straight to your inbox. 
The Shift is Outshift’s exclusive newsletter.
Get the latest news and updates on agentic AI, quantum, next-gen infra, and other groundbreaking innovations shaping the future of technology straight to your inbox. 
![Outshift Background](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/subscribe-background.png)
![Footer BG](https://outshift.cisco.com/images/layout/footer/new-footer-bg-lg.webp)
![Footer BG](https://outshift.cisco.com/images/layout/footer/new-footer-bg-sm.webp)
![Image](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/logo-white.png)
[](https://twitter.com/outshiftbycisco)
[](https://www.linkedin.com/showcase/outshiftbycisco)
[](https://www.youtube.com/channel/UCyf0N9nryCKAecEuCkcECxg)
#### Initiatives
##### Our Work
[Internet of Agents](https://outshift.cisco.com/the-internet-of-agents)
[Internet of Cognition](https://outshift.cisco.com/internet-of-cognition)
[AI/ML](https://outshift.cisco.com/ai)
[Quantum](https://outshift.cisco.com/quantum)
[Open Source](https://outshift.cisco.com/blog/topic/open-source)
##### Our Collaborators
[DevNet](https://developer.cisco.com/)
[Research](https://research.cisco.com/)
[Quantum Labs](https://research.cisco.com/research-projects/quantum)
[AGNTCY](https://agntcy.org/)
#### About us
##### Company
[About Us](https://outshift.cisco.com/about-us)
[Our Team](https://outshift.cisco.com/our-team)
[The Shift](https://outshift.cisco.com/outshift-newsletter)
##### Apply
[Job Openings](https://outshift.cisco.com/careers)
##### Connect
[Events](https://outshift.cisco.com/events)
[Contact Us](https://outshift.cisco.com/contact-us)
[YouTube](https://www.youtube.com/channel/UCyf0N9nryCKAecEuCkcECxg)
[LinkedIn](https://www.linkedin.com/showcase/outshiftbycisco/)
[GitHub](https://github.com/agntcy)
[X](https://twitter.com/outshiftbycisco)
[BlueSky](https://bsky.app/profile/outshift.cisco.com)
#### Blog
##### Categories
[AI/ML](https://outshift.cisco.com/blog/ai-ml)
[Quantum](https://outshift.cisco.com/blog/quantum)
[In-depth Tech](https://outshift.cisco.com/blog/in-depth-tech)
[Strategy & Insights](https://outshift.cisco.com/blog/insights)
[Research](https://outshift.cisco.com/blog/research)
[Inside Outshift](https://outshift.cisco.com/blog/inside-outshift)
#### Tools
##### Resource Hub
[View all](https://outshift.cisco.com/resources)
[Ebooks](https://outshift.cisco.com/resources?type=eBooks)
[Videos](https://outshift.cisco.com/resources?type=Videos)
[Webinars on demand](https://outshift.cisco.com/resources?type=Webinars%20on-demand%20)
[White papers](https://outshift.cisco.com/resources?type=White%20Papers)
[Case studies](https://outshift.cisco.com/case-studies)
##### Apps & Services
[View all](https://outshift.cisco.com/services)
[Agent Identity Service](http://agent-identity.outshift.com/)
[Agent Directory](https://github.com/agntcy/dir)
[AI Catalog](https://ai-catalog.outshift.io/)
[Open Agent Schema Framework](https://schema.oasf.outshift.com/)
[Network-aware Quantum Compiler](https://outshift.cisco.com/quantum-compiler-app)
[Quantum Random Number Generator](https://outshift.cisco.com/quantum-random-number-generator)
[Community AI Platform Engineering](https://github.com/cnoe-io/ai-platform-engineering)
[Explore Cisco](https://www.cisco.com)
![cta](https://outshift.cisco.com/images/layout/footer/cta.svg)
[Website Terms of Use](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
[Privacy Policy](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
Cookies / Do not sell or share my personal data
[Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
©2025 Cisco Systems, Inc.
