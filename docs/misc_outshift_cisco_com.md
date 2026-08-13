

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


---
# ORIGEN: https://outshift.cisco.com/blog

[![Outshift Logo](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/outshift-logo-text-white.svg)](https://outshift.cisco.com/)
  * Initiatives
  * About us
  * [Blog](https://outshift.cisco.com/blog)
  * Tools
  * Case studies


[](https://outshift.cisco.com/blog/search)
# Outshift Blog
![Diamond](https://outshift.cisco.com/images/graphics/middle-diamond.png)![Diamond](https://outshift.cisco.com/images/graphics/middle-diamond.png)
[ ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML 6 min read ![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA_1634_CASA_deep_dive_2a90340fb3.png) CNJulu Panat Continuous Agent Semantic Authorization (CASA) for Multi-Agent Systems  Learn how CASA brings the Internet of Cognition to life through semantic authorization, enabling trusted and intent-aligned multi-agent AI systems.  ](https://outshift.cisco.com/blog/ai-ml/continuous-agentic-semantic-authorization-for-mas)
![Subscribe card background](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/subscribe-card-background.png)
![Subscribe](https://outshift.cisco.com/images/pages/home/subscribe-logo.svg)
Subscribe to 
The Shift!
##### Get emerging insights on innovative technology straight to your inbox.
[Subscribe to newsletter](https://outshift.cisco.com/blog#theshift)
![Subscribe card background](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/subscribe-card-background.png)
![Subscribe](https://outshift.cisco.com/images/pages/home/subscribe-logo.svg)
Subscribe to 
The Shift!
##### Get emerging insights on innovative technology straight to your inbox.
[Subscribe to newsletter](https://outshift.cisco.com/blog#theshift)
##### [The Outshift case study hub: Where real-world partner stories come together](https://outshift.cisco.com/blog/in-depth-tech/use-case-hub)
##### [Post-Quantum Cryptography: It's Time to Rethink Digital Security](https://outshift.cisco.com/blog/quantum/quantum-safe-cryptography)
##### [How Cisco’s culture of giving back shapes the leaders of tomorrow ](https://outshift.cisco.com/blog/inside-outshift/cisco-culture-of-giving-back-shapes-leaders-of-tomorrow)
##### [The Outshift case study hub: Where real-world partner stories come together](https://outshift.cisco.com/blog/in-depth-tech/use-case-hub)
##### [Post-Quantum Cryptography: It's Time to Rethink Digital Security](https://outshift.cisco.com/blog/quantum/quantum-safe-cryptography)
##### [How Cisco’s culture of giving back shapes the leaders of tomorrow ](https://outshift.cisco.com/blog/inside-outshift/cisco-culture-of-giving-back-shapes-leaders-of-tomorrow)
##### [The Outshift case study hub: Where real-world partner stories come together](https://outshift.cisco.com/blog/in-depth-tech/use-case-hub)
##### [Post-Quantum Cryptography: It's Time to Rethink Digital Security](https://outshift.cisco.com/blog/quantum/quantum-safe-cryptography)
##### [How Cisco’s culture of giving back shapes the leaders of tomorrow ](https://outshift.cisco.com/blog/inside-outshift/cisco-culture-of-giving-back-shapes-leaders-of-tomorrow)
![Diamond](https://outshift.cisco.com/images/graphics/middle-diamond.png)![Diamond](https://outshift.cisco.com/images/graphics/middle-diamond.png)
## Recent articles
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Use_Cases_Website_launch_e4511646cd.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/product-icon.svg)In-depth Tech The Outshift case study hub: Where real-world partner stories come together](https://outshift.cisco.com/blog/in-depth-tech/use-case-hub)
[AI/ML](https://outshift.cisco.com/blog/topic/artificial-intelligence)[Use Case](https://outshift.cisco.com/blog/topic/use-case)[Quantum](https://outshift.cisco.com/blog/topic/quantum)[Strategy & Insights](https://outshift.cisco.com/blog/topic/strategy-insights)[In-depth Tech](https://outshift.cisco.com/blog/topic/in-depth-tech)[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[Open Source](https://outshift.cisco.com/blog/topic/open-source)[Platform Engineering](https://outshift.cisco.com/blog/topic/platform-engineering)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/PQC_Blog_Quantum_bfef161005.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/quantum.svg)Quantum Post-Quantum Cryptography: It's Time to Rethink Digital Security](https://outshift.cisco.com/blog/quantum/quantum-safe-cryptography)
[Quantum](https://outshift.cisco.com/blog/topic/quantum)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Girls_on_the_Run_0dbf9a07d3.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/inside-outshift-icon.svg)Inside Outshift How Cisco’s culture of giving back shapes the leaders of tomorrow ](https://outshift.cisco.com/blog/inside-outshift/cisco-culture-of-giving-back-shapes-leaders-of-tomorrow)
[Inside Outshift](https://outshift.cisco.com/blog/topic/inside-outshift)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Frame_19_67a7d39b79.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML Agentic AI Foundation Chairs discuss AGNTCY, AAIF, and building in the open](https://outshift.cisco.com/blog/ai-ml/aaif-chairs-interview)
[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[AI/ML](https://outshift.cisco.com/blog/topic/artificial-intelligence)[Inside Outshift](https://outshift.cisco.com/blog/topic/inside-outshift)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA_1634_CASA_deep_dive_2a90340fb3.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML Continuous Agent Semantic Authorization (CASA) for Multi-Agent Systems ](https://outshift.cisco.com/blog/ai-ml/continuous-agentic-semantic-authorization-for-mas)
[AI/ML](https://outshift.cisco.com/blog/topic/artificial-intelligence)[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[In-depth Tech](https://outshift.cisco.com/blog/topic/in-depth-tech)[Use Case](https://outshift.cisco.com/blog/topic/use-case)[Internet of Cognition ](https://outshift.cisco.com/blog/topic/internet-of-cognition)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA_1634_Mycelium_Blog_c38b8ed0cd.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML Mycelium: Coordination Layer for Multi-Agent Systems](https://outshift.cisco.com/blog/ai-ml/mycelium-coordination-layer-for-multi-agent-systems)
[Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)[AI/ML](https://outshift.cisco.com/blog/topic/artificial-intelligence)[In-depth Tech](https://outshift.cisco.com/blog/topic/in-depth-tech)[Use Case](https://outshift.cisco.com/blog/topic/use-case)[Internet of Cognition ](https://outshift.cisco.com/blog/topic/internet-of-cognition)
Load more
![Careers](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/BlogTopicsBG.png)
![Blur Background](https://outshift.cisco.com/images/pages/blog/blur-bg.webp)
![Blur Background](https://outshift.cisco.com/images/pages/blog/blur-bg.webp)
## Explore more topics
###### [Research](https://outshift.cisco.com/blog/topic/research)###### [Events](https://outshift.cisco.com/blog/topic/events)###### [Quantum](https://outshift.cisco.com/blog/topic/quantum)###### [Team](https://outshift.cisco.com/blog/topic/team)###### [Use Case](https://outshift.cisco.com/blog/topic/use-case)###### [Open Source](https://outshift.cisco.com/blog/topic/open-source)###### [Gen AI](https://outshift.cisco.com/blog/topic/gen-ai)###### [AI/ML](https://outshift.cisco.com/blog/topic/artificial-intelligence)###### [Agentic AI](https://outshift.cisco.com/blog/topic/agentic-ai)###### [Apps](https://outshift.cisco.com/blog/topic/apps)###### [Platform Engineering](https://outshift.cisco.com/blog/topic/platform-engineering)
### Welcome to the future of agentic AI: The Internet of Agents
Outshift is leading the way in building an open, interoperable, agent-first, quantum-safe infrastructure for the future of artificial intelligence.
[Read the whitepaper](https://outshift.cisco.com/the-internet-of-agents/whitepaper)
![thumbnail](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA_838_2x_32a1a6457a.png)
[Read the whitepaper](https://outshift.cisco.com/the-internet-of-agents/whitepaper)
#### Featured collection
## Agentic AI
##### Dive into the latest predictions, industry changes, and thought leadership on agentic AI.
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA_1603_AOP_New_Use_Cases_AIML_706153c4a9.png) AI/ML Exploring the Internet of Cognition ](https://outshift.cisco.com/blog/ai-ml/exploring-the-internet-of-cognition)
## [AGNTCY in action: How three teams are driving agentic AI forward](https://outshift.cisco.com/blog/how-agntcy-is-empowering-the-next-wave-of-agentic-innovation)## [Agentic SDLC: A new evolution in software engineering ](https://outshift.cisco.com/blog/agentic-sdlc-new-evolution-in-software-engineering)## [Bridge the semantic gap: The mechanics of shared knowledge in cognitive AI systems ](https://outshift.cisco.com/blog/bridging-the-semantic-gap-cognitive-ai-systems)## [Why shared intent is the missing layer in multi-agent AI](https://outshift.cisco.com/blog/shared-intent-missing-layer-multi-agent-ai)[View more articles](https://outshift.cisco.com/blog/topic/agentic-ai)
## Editor’s picks
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/The_State_of_Cisco_Quantum_Labs_82c123750c.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/quantum.svg)Quantum The state of Cisco Quantum Labs: The quantum networking advancements achieved in one year ](https://outshift.cisco.com/blog/quantum/state-quantum-labs-innovations)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA_1603_AOP_New_Use_Cases_AIML_706153c4a9.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML Exploring the Internet of Cognition ](https://outshift.cisco.com/blog/ai-ml/exploring-the-internet-of-cognition)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/CREA_1607_what_is_quantum_972e03d79d.webp) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/quantum.svg)Quantum Quantum internet 101: What it is, and why it matters](https://outshift.cisco.com/blog/quantum/quantum-internet-101-what-and-why)
[![Featured home blog](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Io_C_What_AI_vs_ASI_0516002c57.png) ![Icon](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Black.svg)AI/ML AI vs. ASI: Understanding the future of artificial superintelligence](https://outshift.cisco.com/blog/ai-ml/ai-asi-future-of-artificial-superintelligence)
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


---
# ORIGEN: https://outshift.cisco.com/about-us

[![Outshift Logo](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/outshift-logo-text-white.svg)](https://outshift.cisco.com/)
  * Initiatives
  * About us
  * [Blog](https://outshift.cisco.com/blog)
  * Tools
  * Case studies


# About Us
#### Outshift takes the first steps in emerging technologies to help Cisco deliver critical infrastructure and innovative solutions in:
###### Agentic AI
###### Superintelligence
###### Quantum
[Explore: _Outshift impact over time_](https://outshift.cisco.com/about-us#timeline)
# Our Mission
## Technology doesn’t just evolve. It transforms.
And that transformative edge is where you’ll find Outshift by Cisco. Outshift is Cisco’s in-house incubation engine.
## Outshift's Path to Impact
From early exploration to real-world impact, these moments define Outshift's work in emerging technology.
Key Milestones (Jump)
### Internet of Agents
  1. [Internet of Agents vision white paper published](https://outshift.cisco.com/about-us#internet-of-agents-vision-white-paper)
  2. [Community AI Platform Engineering (CAIPE) open source project launched](https://outshift.cisco.com/about-us#community-ai-platform-engineering-caipe)
  3. [33 published repositories on AGNTCY](https://outshift.cisco.com/about-us#agntcy-published-repositories)
  4. [AGNTCY graduates to Linux Foundation](https://outshift.cisco.com/about-us#agntcy-graduates-linux-foundation)
  5. [Splunk is building with AGNCTY to enhance AI Observability](https://outshift.cisco.com/about-us#splunk-agntcy-ai-observability)


### Quantum Networking
  1. [Opening of Quantum Labs in Santa Monica](https://outshift.cisco.com/about-us#quantum-labs-santa-monica-opening)
  2. [Entanglement Chip announced](https://outshift.cisco.com/about-us#entanglement-chip-announced)
  3. [Quantum Random Number Generator launch](https://outshift.cisco.com/about-us#qrng-launch)
  4. [Network-aware Quantum Compiler announced](https://outshift.cisco.com/about-us#network-aware-quantum-compiler)


### Outshift
  1. [Panoptica graduates to Cisco Cloud Application Security](https://outshift.cisco.com/about-us#panoptica-graduates-cisco-cloud-application-security)
  2. [Swisscom and Outshift team up to build agentic AI-enabled networks](https://outshift.cisco.com/about-us#swisscom-outshift-agentic-ai-networks)
  3. [Outshift joins Google's A2A steering committee](https://outshift.cisco.com/about-us#outshift-google-a2a-steering-committee)


Today
2026 - present
### Production deployments using AGNTCY code
Built with code from AGNTCY’s 33 repositories, teams are creating multi-agent systems to reduce outages, secure healthcare scheduling, power video intelligence, automate workflows, and beyond.
Sept 2025
### Network-aware Quantum Compiler Announced
The industry-first network-aware Quantum Compiler was purpose-built to accelerate the realization of scalable, fault-tolerant, and efficient quantum data centers greater scalability and efficiency.
Sept 2025
### Community AI Platform Engineering (CAIPE) open source project launched
Originally developed as an internal solution, CAIPE is Cisco's open-source, multi-agent system designed to automate platform operations and free engineers from repetitive, manual tasks.
Sept 2025
### Splunk is building with AGNTCY to enhance AI Observability
Splunk and AGNTCY teamed up to address the challenges of AI Observability by introducing tools and standards designed to transform how organizations monitor and improve their AI systems.
July 2025
### AGNTCY graduates to Linux Foundation
Cisco donated AGNTCY—a framework for interoperable, multi-agent AI systems—to the Linux Foundation, advancing open standards for collaborative AI.
June 2025
### Outshift by Cisco joins Google’s A2A steering committee
Cisco joins as a foundational member, along with six other companies, in the formation of Agent-to-Agent (A2A) Project, donated by Google to the The Linux Foundation. 
May 2025
### Quantum Random Number Generator launch
Outshift launched the Quantum Random Number Generator (QRNG), delivering enhanced cryptographic security and true randomness for enterprise applications and digital infrastructure.
May 2025
### Unveiling Cisco’s Quantum Network Entanglement Chip
Cisco Research reveals a research prototype and breakthrough technology that enables quantum networks to scale and connect quantum processors for practical applications.
May 2025
### Opening of Cisco Quantum Labs in Santa Monica
Cisco Quantum Labs is our new research hub where quantum scientists and engineers are building tomorrow’s quantum networking technologies.
April 2025
### Swisscom and Outshift team up to build agentic AI-enabled networks
Swisscom, Switzerland’s largest telecom provider, and Outshift partnered to develop practical applications of AI agents in network operations to redefine customer experiences.
Jan 2025
### Internet of Agents whitepaper published
The Internet of Agents, introduced in Outshifts’s January 2025 whitepaper, outlines a unified framework for interoperable, collaborative AI agents across distributed systems.
Nov 2024
### Panoptica graduates to Cisco Cloud Application Security
Panoptica, provides end-to-end lifecycle protection for cloud native application environments. It graduated into Cisco’s Cloud Application Security in 2024.
FEB 2024
### Motific.ai launch
Motific.ai went from concept to GA in just nine months and showcased Outshift's agility in AI innovation.
June 2023
### Cisco ET&I becomes Outshift by Cisco
While our name might have been a mouthful, our mission is more to the point: We incubate new businesses and deliver what’s next and new for Cisco.
![Corner](https://outshift.cisco.com/images/pages/home/corner-left.svg)
![Sponsored Research](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/sponsor-bg.png)
##### Sponsored Research
Cisco Research is committed to establishing long-term funded partnerships with universities to foster research and innovation through our Open RFPs. Browse our list of partnerships and learn how you can become involved.
###### Our approach
## Research drives our approach to develop cutting-edge technologies
As Outshifters, we blend startup speed with enterprise strength. We feed our curiosity, act with urgency, embrace challenges, and make bold ideas real. From quantum-safe infrastructure to agentic AI-first applications and platform services, we’re building the foundation that will share tomorrow’s technology landscape.
  

By collaborating with Cisco Research, we connect Cisco’s best engineers and researchers with world-class academic research labs to explore new and promising technologies that are of strategic interest to Cisco’s vision.
[Learn about Cisco Researchabout research](https://research.cisco.com/)
###### Who we are
## Get to know our leadership team defining the future of tech
[Meet the team](https://outshift.cisco.com/our-team)
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
