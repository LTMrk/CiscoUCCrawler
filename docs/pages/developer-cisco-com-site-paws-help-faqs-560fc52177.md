---
doc_id: developer-cisco-com-site-paws-help-faqs-560fc52177
source_url: https://developer.cisco.com/site/paws/help/faqs/
retrieved_at: 2026-08-25T21:10:29.845140+00:00
---

# PAWS FAQs

## Table of contents

- General

## General

Why is an upgrade broken into two steps with different services (e.g. prepare and then start)?

Separating the preparation (i.e. - downloading and validating large upgrade files) from the upgrade process allows for more flexibility. For example, your server maintenance window could be shorter if you download the upgrade file during normal business hours. Thus, only the actual upgrade process is executed during the maintenance window.

How many concurrent SOAP requests can I make?

3

What's the difference between the SOAP layer and UC application layer messages?

The SOAP services utilize a number of existing UC application interfaces to avoid duplication of business logic. If there is a problem in the SOAP service itself, then a SOAP layer message will be generated. This indicates there is either a defect in the service or with the SOAP message. If there is a problem in the underlying UC application interface, then a UC application layer message will be generated. This indicates any number of expected UC application issues has occurred (e.g. - not enough disk space) or a problem with data passed in the SOAP message.

How do I troubleshoot a failed upgrade?

Exactly like you would had the upgrade been started via the OS Admin or CLI.

Can I use 3rd party libraries like Apache Axis2 or JAX-WS to auto-generate SOAP clients?

Yes.

Do the SOAP services generate any logs that I can use to help debug my client code?

The SOAP services use the existing Platform API logs accessible via the CLI "file get activelog tomcat/logs/platform-api/log4j/*" command.

What authentication credentials do I use to access the SOAP services?

Use the OS Administrator account -- the same one you use to access the CLI and OS Admin GUI.

Do all of the SOAP services support both synchronous and asynchronous requests?

Yes. However, some services like PrepareRemoteUpgradeService and StartUpgradeService generally take a while and thus should only be called asynchronously.

Back to Top