---
doc_id: developer-cisco-com-site-im-and-presence-downloads-caxl-downloads-aef016d5ad
source_url: https://developer.cisco.com/site/im-and-presence/downloads/caxl_downloads/
retrieved_at: 2026-09-07T14:15:40.512505+00:00
---

# CAXL Distributions

Distributions (DEBUG versus RELEASE)

Cisco provides two distributions of the Cisco AJAX XMPP Library, the Debug distribution (for troubleshooting purposes), and the Release distribution.

Note! Do not use the Debug distribution in the final end-user product. The Debug distribution is for troubleshooting purposes only. While functionally equivalent, the Debug distribution may load and run significantly slower than the Release distribution.

The Cisco AJAX XMPP Library is delivered as one of two distributions: Release and Debug. Both distributions include the library code, resources, examples, and documentation. The Release distribution provides a "minified" library code file, where all core code and dependencies are in a single, standalone file for each target (jabberwerx.js for the core non-UI library; jabberwerx.ui.js for the UI library). The Debug distribution provides the library code as a set of individual javascript files, with jabberwerx.js and jabberwerx.ui.js acting as dependency loaders. The two distributions are interchangable, and require no changes in how the library loads or operates.

To use the Debug distribution in parallel with the Release distribution, first unpackage the Release distribution into its own directory, called "caxl". Then unpackage the Debug distribution into its own directory, called "caxl/debug". These two directories must be in the same parent directory for your web site.

To load the release builds, the <script> tag that loads the Cisco AJAX XMPP Library should be set to "caxl/jabberwerx.js" (for core) or "caxl/jabberwerx.ui.js" (for UI) to load the release builds (assuming the HTML is in the same directory that holds the Cisco AJAX XMPP Library sub-directories). To switch to the debug builds, change the path to "caxl/debug/jabberwerx.js" or "caxl/debug/jabberwerx.ui.js".

To remove the Debug distribution, delete the "caxl-debug" directory.

# Cisco AJAX XMPP Library - Release

- Released as part of CUP 8.6.1.

- Released as part of CUP 8.5.1.

- Released as part of CUP 8.0.2.

- Released as part of CUP 8.0.1.

# Cisco AJAX XMPP Library - Debug

- Released as part of CUP 8.6.1.

- Released as part of CUP 8.5.1.

- Released as part of CUP 8.0.2.

- Released as part of CUP 8.0.1.