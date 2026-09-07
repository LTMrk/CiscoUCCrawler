---
doc_id: developer-cisco-com-docs-finesse-gadget-caching-19eab1416c
source_url: https://developer.cisco.com/docs/finesse/gadget-caching/
retrieved_at: 2026-09-07T14:08:08.011740+00:00
---

# Gadget Caching

When gadget caching is enabled, the contents are cached in the Finesse server cache and Finesse gadget container. If changes are made to the code of an existing gadget, then perform one of the following:

Restart Cisco Finesse tomcat.

Pass a nocache parameter in the URL to clear the cache and use the CLI command utils webproxy cache clear shindig to clear the Shindig cache.

You can pass the nocache parameter at the root level or at the desktop web application. For example,

https ://server?nocache

https ://server/desktop?nocache

https ://server/desktop/container?nocache