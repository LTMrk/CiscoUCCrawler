[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-primary-logo.svg)](https://blog.webex.com)
[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-secondary-logo.svg)](https://blog.webex.com)
  * [Collaboration](https://blog.webex.com/category/collaboration/)
  * [Workspaces](https://blog.webex.com/category/workspaces/)
  * [Customer Experience](https://blog.webex.com/category/customer-experience/)
  * [Event Management](https://blog.webex.com/category/event-management/)
  * [Innovation & AI](https://blog.webex.com/category/innovation-ai/)


[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2079%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations&title=Building%20voice%20AI%20that%20can%20keep%20up%20with%20real%20conversations) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations)
[ ](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/ "Copy Link") [ ](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/ "Print")
[Engineering](https://blog.webex.com/category/engineering/)
# Building voice AI that can keep up with real conversations
On Dec 4, 2025Mar 2, 2026By [Gergely Lukacsy](https://blog.webex.com/contributors/glukacsy/), [Vibhor Jain](https://blog.webex.com/contributors/vibhjain/)5 Min Read
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations&title=Building%20voice%20AI%20that%20can%20keep%20up%20with%20real%20conversations) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations)
[ ](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/ "Copy Link") [ ](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/ "Print")
![](https://blog.webex.com/wp-content/uploads/2025/12/ai-agent-opt.jpg)
##### A deep dive series on Webex AI Agent
_This blogpost is dedicated to the memory of[Jay Patel](https://blog.webex.com/contributors/j_patel/), an enthusiastic champion of our AI Agent vision and a tireless advocate for every millisecond of improvement._
## Why low latency matters for voice AI
In voice AI, latency is everything. Humans naturally pause for only a few hundred milliseconds between speaking turns — so when an AI agent waits longer, the conversation immediately feels robotic and inattentive. For AI agents, staying within that natural pause window is critical because even small delays can break the flow and frustrate customers.
On telephony network (PSTN) the challenge is even tougher, as roughly 500 ms of latency is introduced across the call path – leaving only a few hundred milliseconds for turn detection, retrieval, reasoning and speech synthesis. Efficiency in every component is essential to keep conversations flowing naturally.
![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201672%201028%22%3E%3C/svg%3E)
Yet speed alone isn’t enough. Smaller models may be fast, but real customer-facing agents must also be accurate, instruction-following, hallucination-resistant, and enterprise-grade — qualities tiny models simply don’t deliver. Larger models provide that intelligence, but at the cost of added latency. And that latency matters most once you move beyond web demos and into real calls. Delivering speed is easy in web demos, where connections are higher fidelity and avoid the PSTN’s extra latency and encoding overhead. The real challenge is delivering that intelligence while still responding in under a second on real telephony paths.
This is where Cisco takes a unique approach. By combining the intelligence of high-quality models with deep latency engineering, Webex AI Agent delivers responses that are smart, immediate, and _feel_ human.
## Our approach
To deliver natural, low-latency responses, we use a modular pipeline: Voice Activity Detection (VAD) → Automatic Speech Recognition (ASR) → business logic → Large Language Model (LLM) → Text-to-Speech (TTS). This structure provides transparency and allows each component to be tuned for both speed and quality.
VAD detects when the customer starts and stops speaking, enabling barge-in and turn taking, while ASR converts speech to text, a critical step since all downstream logic relies on its accuracy. The business logic layer then interprets the transcript, managing turn detection (with entity-aware checks like digit sequences), grounding LLM responses with retrieval-augmented generation (RAG), which fetches relevant facts from corporate knowledge bases to prevent hallucinations, and handling additional decisions such as small-talk detection and tool usage.
The LLM generates the answer using transcript, context, and retrieved data, and TTS produces the natural audio the customer hears. We currently deploy trillion-parameter commercial models alongside Cisco’s internal models to balance accuracy and latency, as detailed in our [Webex AI Transparency Note](https://trustportal.cisco.com/c/r/ctp/trust-portal.html?search_keyword=transparency%20note#/19445370048945010). VAD and turn detection ensure we know precisely when to speak, RAG and business logic ground the answers, and the LLM and TTS deliver high-quality responses – all within strict timing constraints. Behind the scenes, several proprietary Cisco models provide additional intelligence and latency optimizations, further enhancing accuracy and responsiveness.
These choices will continue to evolve as the industry and model capabilities advance.
![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201672%20661%22%3E%3C/svg%3E)
## Generating the first part of the final answer upfront
A key optimization is generating the beginning of the final answer while the customer is still speaking. Instead of waiting for a full transcript and completed retrievals, we pre-compute an initial segment so that playback can start immediately once VAD and TD confirm the end of turn. This mirrors human conversation: skilled agents begin speaking as they’re still formulating the rest of their response. By generating the first part early, we maintain sub-second responsiveness while heavier, more accurate models continue processing in the background.
#### Why This Matters
Without upfront generation, we’d be forced to use much smaller, less accurate models to meet latency budgets. That means real tradeoffs: the LLM would need to be lightweight with weaker instruction following, the ASR might have to be ultra-fast but less accurate, and the TTS would likely rely on faster but robotic-sounding engines. In practice, customers would get responses sooner, but those responses would be noticeably less helpful, natural, and trustworthy.
By generating and caching the first part early, we create valuable time for slower, higher-quality reasoning, retrieval, and synthesis. That breathing room lets larger, more capable models run in the background to perform the heavier reasoning and retrieval needed to generate intelligent responses – all before the customer ever notices a delay. The result is speed without compromise, rapid responses that are both accurate and natural.
#### Challenges and Design Choices
Generating early output introduces several requirements:
  * Incomplete input: The early segment must be safe, contextually plausible, and able to continue naturally after the full reasoning completes.
  * Continuation model: We never discard the early part; the final answer simply continues from it.
  * Mid-sentence flexibility: The early part doesn’t need to be a full sentence (e.g., “I’m happy to help…”), making it blend seamlessly into the final answer.
  * Multiple candidates: We generate several possible starts and pick the best one as more context arrives.


This design delivers a single, smooth response from the customer’s perspective, even as complex processing continues behind the scenes.
![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201672%20782%22%3E%3C/svg%3E)
## Additional latency optimizations
Across the stack, we implement multiple engineering optimizations, each shaving small amounts of time to keep the pipeline fast even when using higher-quality models.
**Streaming**
  * Low-latency ASR/TTS streaming
  * LLM token streaming


**Infrastructure**
  * Regional media colocation
  * Reserved capacity for critical LLM calls


******Modelling******
  * Hybrid multi-model mixtures for lightweight tasks
  * Robust End of Speech (EOS) detection combining VAD, ASR, and custom signals


**Caching**
  * Common prompt caching
  * Pre-synthesized audio


On the infrastructure side, we build multiple layers of resilience to keep latencies predictable under real production conditions. This includes an LLM proxy with regional failover, parallel “safety-net” requests to hedge against slow LLM responses, coordinated retries and caching for ASR and TTS paths, and a system-wide orchestration layer that dynamically adjusts model sizes and fallback strategies.
## Real life latency numbers
We measure latency from the moment the customer stops speaking to when they hear the first audio. In practice, the breakdown looks like this:
  * VAD EOS: ~500 ms
  * Turn Detection: <75 ms p99
  * First part of answer: Already generated + cached by EOS
  * TTS for the first segment: Usually 10–20 ms (due to cache hits)
  * PSTN return path: ~500 ms


Because the early segment is ready immediately at EOS, playback can start almost instantly. Meanwhile, the heavier generation and RAG retrieval complete in parallel, seamlessly continuing the answer. The result is natural, sub-second responsiveness despite larger models running in the background.
## Our low latency advantage
Delivering a truly human, natural, and immediate voice AI experience requires more than connecting ASR, LLM, and TTS. It demands careful orchestration of every component — precision turn detection, early-answer generation, caching, and resilient infrastructure — all working together to minimize latency without compromising intelligence.
Webex AI Agent combines high-quality models with deep latency engineering to consistently achieve ~1.3 second PSTN latencies over real telephony paths. The result is an AI agent that feels human, attentive, and reliable, helping enterprises meet customer expectations while maintaining accuracy, grounding, and enterprise-grade reliability.
Discover how Webex AI Agent can bring fast, natural, and accurate voice experiences to your PSTN interactions — reach out to your Webex sales representative or partner for a personalized demo.
#### About The Authors
![Gergely Lukacsy](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2096%22%3E%3C/svg%3E)
Gergely Lukacsy Principal Engineer Cisco
Gergely Lukacsy is a Principal Engineer and Lead Architect for the Cisco AI Agent and the broader cloud-based Cisco Contact Center portfolio.
[Learn more](https://blog.webex.com/contributors/glukacsy/)
![Vibhor Jain](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2096%22%3E%3C/svg%3E)
Vibhor Jain Senior Cloud Engineering Technical Leader Cisco
Vibhor Jain is a Cloud Engineering Technical Leader at Cisco, currently responsible for spearheading the voice experience flow for Webex AI Agent.
[Learn more](https://blog.webex.com/contributors/vibhjain/)
#### Topics
[Customer Experience](https://blog.webex.com/tag/customer-experience-4/)[Enterprise AI](https://blog.webex.com/tag/enterprise-ai/)
* * *
## More like this
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%20961%22%3E%3C/svg%3E)simple Engineering Resilience by Design: How Webex Contact Center Stays Up When the ... By Iyer Venkataraman, Divyesh Khandeshi5 Min Read ](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/)
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
  * [English](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/)


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
  * [English](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/)


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
