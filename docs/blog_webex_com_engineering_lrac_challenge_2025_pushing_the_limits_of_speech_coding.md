[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-primary-logo.svg)](https://blog.webex.com)
[![](https://blog.webex.com/wp-content/uploads/2024/08/webex-secondary-logo.svg)](https://blog.webex.com)
  * [Collaboration](https://blog.webex.com/category/collaboration/)
  * [Workspaces](https://blog.webex.com/category/workspaces/)
  * [Customer Experience](https://blog.webex.com/category/customer-experience/)
  * [Event Management](https://blog.webex.com/category/event-management/)
  * [Innovation & AI](https://blog.webex.com/category/innovation-ai/)


[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2079%2024%22%3E%3C/svg%3E)](https://blog.webex.com)
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding&title=LRAC%20Challenge%202025:%20Pushing%20the%20limits%20of%20speech%20coding) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding)
[ ](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/ "Copy Link") [ ](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/ "Print")
[Engineering](https://blog.webex.com/category/engineering/)
# LRAC Challenge 2025: Pushing the limits of speech coding
On Aug 12, 2025Aug 13, 2025By [Ivana Balic](https://blog.webex.com/contributors/ibalic/)4 Min Read
[ ](https://twitter.com/intent/tweet?url=https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding) [ ](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding&title=LRAC%20Challenge%202025:%20Pushing%20the%20limits%20of%20speech%20coding) [ ](https://www.facebook.com/sharer/sharer.php?u=https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding)
[ ](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/ "Copy Link") [ ](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/ "Print")
![](https://blog.webex.com/wp-content/uploads/2025/08/audio-signal-processing-neural-networks.jpg)
The field of neural speech and audio coding has witnessed an explosive growth, marking a paradigm shift from traditional signal processing approaches. Recent models have achieved unprecedented compression, delivering intelligible speech at bitrates often below 1 kbps.
However, most of these cutting-edge systems grapple with high computational complexity and considerable latency. This often renders them impractical for real-world telecommunication use cases, especially on resource-constrained devices like wearables, mobile phones, or IoT.
The inaugural 2025 Low Resources Audio Codec (LRAC) Challenge [co-organized by Cisco](https://crowdsourcing.cisco.com/lrac-challenge/2025/about) tackles the above head-on, inviting engineers and researchers to design speech codecs that aren’t just low-bitrate, but also low-complexity, low-latency, and deployable on everyday hardware and in everyday communication environments. **We are looking for solutions that can operate effectively at 1 kbps and 6 kbps bitrates in the real world.**
This challenge runs from Aug. 1 to Sept.30 and culminates in a satellite workshop at [ICASSP 2026](https://2026.ieeeicassp.org/), where participants will publish and present their solutions.
## Challenge Focus: Low-Bitrate, Low-Complexity, Low-Latency, High-Impact
Unlike many research efforts that primarily push quality under ideal conditions, LRAC puts practical engineering first. This challenge tackles some of the most critical issues and opportunities of neural speech coding, demanding solutions that excel under strict constraints in:
  * **Bitrate:** Pushing the boundaries of ultra-low compression, with target bitrates of **1 kbps and 6 kbps.**
  * **Compute:** Ensuring high computational efficiency for resource-constrained environments.
  * **Latency:** Achieving real-time performance crucial for interactive applications.


Participants are encouraged to explore hybrid neural coding, real-time pipelines, and efficient quantization schemes—especially those suitable for embedded or CPU-only environments.
## Related Work: Where LRAC Fits In
The journey towards neural codecs was significantly propelled by foundational models like [WaveNet](https://deepmind.google/discover/blog/wavenet-a-generative-model-for-raw-audio/)[6], which demonstrated the immense potential of neural networks for raw audio generation. Subsequent advancements like [LPCNet](https://jmvalin.ca/demo/lpcnet/)[7] and [SoundStream](https://research.google/blog/soundstream-an-end-to-end-neural-audio-codec/)[8] built on those breakthroughs by applying neural network techniques to actual speech and audio coding, enabling real-time operation and high-quality reconstruction.
While these models and others have shown what’s possible, the quest for ultra-low bitrate and highly deployable codecs continues. The models listed below represent significant strides in achieving impressive compression, yet many still face the practical hurdles of high complexity and compute demands for edge deployment. The LRAC Challenge aims to bridge this gap by identifying and highlighting unresolved problem areas for the research community to address, with the goal of propelling the state-of-art towards truly practical solutions for resource-constrained devices.  
| **Codec**  | **Bitrate**  | Notes  |  
| --- | --- | --- |  
| FocalCodec [1]  | 0.16–0.65 kbp  | Single binary codebook, semantic-aware, minimal compute  |  
| DualCodec [2]  | 0.85–0.93 kbps  | Semantic + waveform streams, open source  |  
| PSCodecDRLICT  
[3]  | ~0.675 kbps  | Prompt-based encoding, strong intelligibility  |  
| ESC [4]  | ~1 kbps  | Lightweight transformer with residual VQ  |  
| BigCodec [5]  | ~1.04 kbps  | High quality, but large (159M parameters)  |  
While these models set quality benchmarks, few are designed for real-time use on edge devices—a gap the LRAC Challenge aims to fill.
#### Who Should Participate?
  * **Speech and audio researchers** working on compression, coding, or enhancement.
  * **ML engineers** focusing on edge inference, streaming models, or low-power deployment.
  * **Anyone interested** in pushing the state-of-the-art in codec design toward real-world applications.


#### Incentives for Engineers
  * **Rigorous benchmarking** with comprehensive subjective testing battery.
  * **Opportunity to present and publish** at the LRAC Workshop at ICASSP 2026.
  * **Join a vibrant community** of engineers, researchers, and developers tackling neural audio and speech compression.


#### How to Get Started
If you’re ready to apply your expertise to a challenge with profound real-world impact and immediate relevance, join us for [LRAC 2025](https://lrac.short.gy/) and help revolutionize speech technology. View the [rules, including evaluation protocol](https://crowdsourcing.cisco.com/lrac-challenge/2025/rules), for more information.
Whether you already have a strong solution—or are simply curious to explore the problem space—we invite you to participate, connect with others, share ideas, and help advance the field together.
**Sometimes, the biggest breakthroughs start with just trying.**
**References**
[1] L. Della Libera, F. Paissan, C. Subakan, and M. Ravanelli, “FocalCodec: Low‑Bitrate Speech Coding via Focal Modulation Networks,” arXiv preprint arXiv:2502.04465, Feb. 2025
[2] J. Li, X. Lin, Z. Li, S. Huang, Y. Wang, C. Wang, Z. Zhan, and Z. Wu, “DualCodec: Dual‑Stream Neural Speech Codec with Semantic and Waveform Encoding,” Proc. Interspeech, 2025. Available: <https://dualcodec.github.io>
[3] Y. Pan, X. Zhang, Y. Yang, J. Yao, Y. Hu, J. Ye, H. Zhou, L. Ma, and J. Zhao, “PSCodec: A Series of High‑Fidelity Low‑Bitrate Neural Speech Codecs Leveraging Prompt Encoders,” arXiv preprint arXiv:2404.02702, Apr. 2024 (rev. Nov. 2024)
[4] Y. Gu and E. Diao, “ESC: Efficient Speech Coding with Cross‑Scale Residual Vector Quantized Transformers,” arXiv preprint arXiv:2404.19441, Apr. 2024
[5] D. Xin, X. Tan, S. Takamichi, and H. Saruwatari, “BigCodec: Pushing the Limits of Low‑Bitrate Neural Speech Codec,” arXiv preprint arXiv:2409.05377, Sept. 2024, and code at <https://github.com/Aria-K-Alethia/BigCodec.>
[6] van den Oord, A., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., Kalchbrenner, N., Senior, A., Kavukcuoglu, K. (2016) [WaveNet](https://deepmind.google/discover/blog/wavenet-a-generative-model-for-raw-audio/): A Generative Model for Raw Audio. Proc. 9th ISCA Workshop on Speech Synthesis Workshop (SSW 9), 125
Arxiv: <https://arxiv.org/abs/1609.03499>
GitHub: <https://github.com/huyouare/WaveNet-Theano>
[7] J.-M. Valin and J. Skoglund, “[LPCNet](https://jmvalin.ca/demo/lpcnet/): Improving Neural Speech Synthesis Through Linear Prediction,” Proc. ICASSP, 2019
Arxiv: <https://arxiv.org/abs/1810.11846>
GitHub: <https://github.com/xiph/LPCNet>
[8] N. Zeghidour, A. Luebs, A. Omran, J. Skoglund, and M. Tagliasacchi, “[SoundStream](https://research.google/blog/soundstream-an-end-to-end-neural-audio-codec/): An End-to-End Neural Audio Codec,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 30, pp. 495-507, 2022. doi: 10.1109/TASLP.2021.3129994
Arxiv: <https://arxiv.org/abs/2107.03312>
GitHub: no official implementation shared on GitHub.
#### About The Author
![Ivana Balic](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2096%2096%22%3E%3C/svg%3E)
Ivana Balic Principal Software Engineer Cisco
Ivana Balic is a Principal Engineer at Cisco working on next-generation data strategies for training and evaluating AI audio-video models.
[Learn more](https://blog.webex.com/contributors/ibalic/)
#### Topics
[audio-innovation](https://blog.webex.com/tag/audio-innovation/)[audio-tech](https://blog.webex.com/tag/audio-tech/)[audio‑compression](https://blog.webex.com/tag/audio%e2%80%91compression/)[edge‑AI](https://blog.webex.com/tag/edge%e2%80%91ai/)[embedded-systems](https://blog.webex.com/tag/embedded-systems/)[embedded‑AI](https://blog.webex.com/tag/embedded%e2%80%91ai/)[ICASSP](https://blog.webex.com/tag/icassp/)[low‑bitrate](https://blog.webex.com/tag/low%e2%80%91bitrate/)[low‑compute](https://blog.webex.com/tag/low%e2%80%91compute/)[low‑latency](https://blog.webex.com/tag/low%e2%80%91latency/)[LRAC2025](https://blog.webex.com/tag/lrac2025/)[machine-learning](https://blog.webex.com/tag/machine-learning-3/)[neural-speech-codec](https://blog.webex.com/tag/neural-speech-codec/)[neural‑codec](https://blog.webex.com/tag/neural%e2%80%91codec/)[real-time](https://blog.webex.com/tag/real-time-2/)[speech‑codec](https://blog.webex.com/tag/speech%e2%80%91codec/)[speech‑engineering](https://blog.webex.com/tag/speech%e2%80%91engineering/)
* * *
## More like this
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%201200%22%3E%3C/svg%3E)simple Engineering Building voice AI that can keep up with real conversations By Gergely Lukacsy, Vibhor Jain5 Min Read ](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/)
[ ![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202100%20961%22%3E%3C/svg%3E)simple Engineering Resilience by Design: How Webex Contact Center Stays Up When the ... By Iyer Venkataraman, Divyesh Khandeshi5 Min Read ](https://blog.webex.com/engineering/resilience-by-design-how-webex-contact-center-stays-up-when-the-cloud-wobbles/)
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
  * [English](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/)


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
  * [English](https://blog.webex.com/engineering/lrac-challenge-2025-pushing-the-limits-of-speech-coding/)


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
