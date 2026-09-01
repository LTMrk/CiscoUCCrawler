---
doc_id: sec-cloudapps-cisco-com-security-center-resources-third-party-attestation-policy-html-98e5d7cc59
source_url: https://sec.cloudapps.cisco.com/security/center/resources/third_party_attestation_policy.html
retrieved_at: 2026-09-01T14:09:01.691585+00:00
---

Home / Cisco Security

Third-Party Code Attestation Policy

# Third-Party Code Attestation Policy

### Contents

# Overview

Third-party code attestation is a process in which a vendor’s code is tested for resilience against one or more security standards by a third party. Such tests are performed by an independent resource, which is expected to be neutral about the results (in comparison to having the vendor perform these tests itself).

The practice of third-party code attestation is a portion of what is sometimes referred to as trustworthy computing . 1

# Third-Party Code Testing Policy

Cisco customers who wish to perform third-party attestation of Cisco code may do so under the following conditions:

- Only production versions of code may be used. Production code refers to any image that can be downloaded from the Download Software section of Cisco.com.

- Customer-specific images created and published by Cisco may also be tested, provided the software passed the Cisco standard quality assurance (QA) processes and with an expectation by both Cisco and the customer that the code would be deployed in a production environment.

- Images that have been provided by Cisco specifically to troubleshoot or perform other diagnostic analysis of one or more active customer issues may not be used for third-party attestation. These images contain additional code that could alter the performance of the image, has not been through the Cisco standard QA processes, and may contain functionality that constitutes trade secrets.

- Requests for images that contain instrumented code for the purposes of third-party attestation will not be honored due to the likelihood of exposing trade secrets and/or intellectual property unique to Cisco.

- Any other images that are not considered to be in general availability are not eligible for third-party attestation.

Cisco welcomes reports from independent researchers, industry organizations, vendors, customers, and other sources concerned with product or network security. Should any issues be identified in the course of third-party attestation, the Cisco Security Vulnerability Policy applies and provides guidance on how to contact Cisco for issue resolution.

# Cisco Secure Development Lifecycle

As an industry leader, Cisco is expected to deliver secure and resilient products that can withstand attack. Our customers not only look to us to ensure their networks are safe and secure, but they expect product security to be seamlessly integrated into all of our products. In order to achieve this, we’ve integrated security best practices into our product architecture, design, and development processes so that product security becomes part of our DNA and corporate culture. This process is referred to as the Cisco Secure Development Lifecycle (CSDL). Further information on the CSDL program can be found on Cisco.com .

1. The term trustworthy computing is used to assign several principles to a system. When used with initial capital letters, Trustworthy Computing refers to an initiative that is similar but unique to Microsoft Corporation. In addition, Cisco uses the term trustworthy systems to describe an infrastructure that enables public and private organizations around the world to deliver goods and services over computer networks with maximum possible confidence. For further information, refer to Key Considerations in Building and Operating Trustworthy Systems: The Role of the Trustworthy Vendor .

Last Updated: 2013 Oct 25

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top