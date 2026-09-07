---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-217006-collaboration-solution-analyser-csa-html-a990ac21dd
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/217006-collaboration-solution-analyser-csa.html
retrieved_at: 2026-09-07T13:03:27.876236+00:00
---

Collaboration Solution Analyser (CSA) - BroadWorks Components

# Collaboration Solution Analyser (CSA) - BroadWorks Components

### Download Options

Updated: March 26, 2021

Document ID: 217006

Contents

## Contents

# Collaboration Solutions Analyzer (CSA)

The Collaboration Solutions Analyzer (CSA) is a Cisco collaboration tool that provides various analysis and troubleshooting for multiple Cisco's technologies.

The CSA supports BroadWorks Analysis for:

- Call engine/Call Flow analysis: Application Server (AS) XSLog

- Software Level Analyser (SLA): All Servers (AS, NS, MS, etc..) tech-support file

The tool can be reach at the following URL:

https://cway.cisco.com/csa/

BroadWorks files (AS XSLog and tech-support) can be analysed by clicking the Log analysis box:

This will bring the user to the file upload menu where you can upload XSLog and Tech-Support files:

Software Level Advisor

The CSA Software Level Advisor (SLA) functionality consist of:

- Tech-support analysis

- Report creation of missing patches (HTMLformat).  TXT format will be available soon.

The CSA/SLA tool does not build/create a patch bundle.  automatinc patch installation and bundles ae discussed in this article:

The Tech-Soupprt analysis is triggered when the CSA detects a BroadWorks (BRWKS) file and that the file is determined to be a tech-support:

By selecting the file and clicking on the "Run analysis' button, the CSA will process the file and return the Software Level Advisor Report:

The view the missing patch, the user click on the "List of Missing Patch" button (not show here).

Call Engine / Call Flow Analyser

The CSA Call Engine (Call Flow Analyser) is a tool that parse the Application Server (AS) XSLog and extract the various call within the XSLog.  A specific call can be selected which will generates amongs other thing a ladder diagram.

The Call Engine/Call Flow analysis is triggered when the CSA detects a BroadWorks (BRWKS) file and that the file is determined to be an Application Server (AS) XSLog:

By selecting the file and clicking on the "Run analysis' button, the CSA will process the file and return the list of calls contained within the file(s):

To run the call analysis, search/select the call to be analysed by clicking the call itself.  The CSA will return the complete analysis of this call.

Call detail:

Ladder diagram:

Diagnostic Signature finding(s) - (if any):

### Revision History

1.0

26-Mar-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Mar-2021 | Initial Release |