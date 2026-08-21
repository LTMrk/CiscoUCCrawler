---
doc_id: sec-cloudapps-cisco-com-security-center-resources-risk-based-disclosure-3f02c78bc8
source_url: https://sec.cloudapps.cisco.com/security/center/resources/risk-based-disclosure
retrieved_at: 2026-08-21T06:05:24.337453+00:00
---

Home / Cisco Security

Cisco's Transition to a Risk-Based Vulnerability Disclosure Model

# Cisco's Transition to a Risk-Based Vulnerability Disclosure Model

### Summary

Starting in July 2026, Cisco will further evolve to a risk-based vulnerability disclosure model to address the rapid evolution of AI-driven cyber threat discovery and mitigation. This evolved model prioritizes critical security information and establishes a predictable cadence for hardening releases and related disclosures, helping ensure customers receive prioritized and actionable security information. The operational process is structured as follows:

- Vulnerability Management: Cisco is systematically evaluating our product portfolio to identify and address security vulnerabilities. Vulnerabilities that share common weaknesses (CWE) are consolidated into "umbrella" CVE IDs, assigning a CVSS score based on the highest severity within that category. To facilitate proactive patching, Cisco plans to issue software "hardening releases" that are grouped by major Network Operating System (NOS) platform (IOS XE, IOS XR, NX-OS, Secure Firewall, and ASA). Advisories are planned to be published generally only after [fix/hardening/update] software is available on the Cisco Software Download Center (CCO) to ensure customers have an immediate upgrade path.

- Release Cadence and Notification: Cisco plans to publish security advisories , including those for hardening releases, twice a month, provided the hardening release is available. Customers will also see advanced notification even when no vulnerabilities will be disclosed on the first or third Wednesday. Each major NOS platform is expected to receive security updates on a quarterly basis, with the possibility of out-of-cycle releases if the need arises.

- Advance Notification: To support customers with change-control planning, Cisco plans to provide seven-day advance notice of upcoming security advisories, including affected technology and platform, to customers who are subscribed to receive external PSIRT security announcements. This advance notification will also alert customers when no vulnerabilities will be disclosed on the first or third Wednesday.

- Software Patching Strategy: Software updates are categorized as maintenance releases (security hardening updates and bug fixes only) or feature trains (including security fixes, defect resolutions, and new features). Cisco uses a mix of hotfixes and minor or major releases based on business unit discretion. Due to the risk of rapid exploitation given advancements in AI models, customers are advised to upgrade immediately.

- Emergency and Low-Risk Protocols: Cisco will in its discretion continue to release out-of-cycle security advisories with or without software updates or patches and with or without advance notifications, as needed in exigent circumstances such as active exploitation, serious third-party software issues, serious open-source component issues, and critical- or high-risk vulnerabilities. In general, low-risk findings will no longer receive individual advisories and will instead be addressed through less detailed disclosures. Disclosure protocols for third-party and open-source components remain unchanged.

### Additional Information

For the official announcement on changes to Cisco's Product Security Incident Response Team (PSIRT) disclosures, see the blog post Strengthening the Foundation: A Predictable, Customer-Focused Response to AI-Accelerated Vulnerability Discovery .

### Frequently Asked Questions

Q1: What is a "risk-based" disclosure process?

A1: A risk-based disclosure process prioritizes detailed technical information for vulnerabilities that pose the highest risk—those that are critical or high severity, actively exploited, have a high likelihood of exploitation, etc. Cisco will in its discretion continue to release out-of-cycle security advisories as needed in exigent circumstances such as active exploitation, serious third-party software issues, serious open-source component issues, and high-risk or critical-risk vulnerabilities. Lower-risk vulnerabilities (including those found internally) may receive less detailed disclosure, focusing instead on remediation and software upgrades.

Q2: Why is Cisco evolving its security release schedule?

A2: The rapid evolution of AI-driven vulnerability discovery has increased the volume and speed of findings. Traditional ad-hoc patching is now largely insufficient. Meeting current cybersecurity needs requires prioritizing vulnerability disclosure based on risk. Shifting to a planned, twice-monthly disclosure schedule provides predictability and discipline to help secure infrastructure at scale, so customers can focus on critical patching and mitigation efforts. Cisco will continue to adjust as needed within our tenets of security, transparency, and trust. More information is available on Cisco's blog .

Q3: When does this evolved process go into effect? When is the first disclosure scheduled?

A3: The evolved process went into effect in July 2026 with the release of the first Cisco Advance Notification for Publication of Security Advisories .

Q4: What is the new disclosure schedule?

A4: Hardening release publications (a new type of security advisory for hardening releases that will address multitudes of vulnerabilities discovered through Cisco's harnessing of frontier AI models) are scheduled for publication on the first and third Wednesday of each month at 16:00 UTC, provided the corresponding hardening release is available. Other types of security advisories are generally planned for release on the same schedule. In exigent circumstances (such as observed exploitation of greater-severity vulnerabilities), security advisories are planned to continue to be published outside of this schedule.

Q5: How will customers be notified about an upcoming disclosure?

A5: Cisco plans to publish informational advance notifications, which will list which products will be covered or indicate that there are no products to be covered, seven days prior to scheduled Wednesday publications. Customers will also see advanced notification even when no vulnerabilities will be disclosed on the first or third Wednesday. Customers can sign up to receive alerts when new announcements are released using the notification services and RSS feeds that are available on Cisco's security website and read more about the available channels for security vulnerability information the Cisco Security Vulnerability Policy .

Q6: What type of information will be shared in the seven-day advance notification for publication to the public?

A6: Cisco is evolving its model to give customers visibility into what is coming, on which products, before it lands, empowering customers to pre-stage change windows, lab validation, and maintenance approvals, turning patch management into planned activity. The seven-day advance notification for publication is designed to provide high-level awareness of an impending disclosure, including summary-level product information.

Q7: Will Cisco still release security advisories or software updates outside of the twice-monthly risk-based disclosure cadence?

A7: Yes. Cisco prioritizes customer safety and real-time threat response and will in its discretion continue to release out-of-cycle security advisories as needed in exigent circumstances such as active exploitation, serious third-party software issues, serious open-source component issues, and high-risk or critical-risk vulnerabilities.

Q8: What is Cisco's guidance and expectation around how quickly customers should upgrade to these patched releases?

A8: Customers are advised to upgrade immediately.

Q9: Why is one CVE ID assigned to multiple vulnerabilities?

A9: In this evolved risk-based disclosure process, Cisco groups bugs that share the same weakness (CWE) into "umbrella" CVE IDs to simplify vulnerability management and patching workflows.

Q10: How is the CVSS score calculated for an "umbrella" CVE ID?

A10: The CVSS score represents the highest severity (worst-case scenario) of all individual bugs that are grouped under that CWE category.

Q11: What happens if there is a critical emergency or zero-day vulnerability?

A11: Cisco's process for responding to active exploitation or critical incidents outside the normal cycle remains unchanged. Cisco remains committed to transparency for critical issues and will in its discretion continue to release out-of-cycle security advisories as needed in exigent circumstances.

Q12: Does this change affect third-party or open-source component vulnerabilities?

A12: Existing practices for third-party and open-source components remain unchanged. Cisco plans to continue to provide timely responses and regular updates for high-risk and critical issues in these areas as patches are developed and released.

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top