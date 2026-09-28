---
doc_id: developer-cisco-com-docs-webdialer-docs-72ce18c992
source_url: https://developer.cisco.com/docs/webdialer-docs/
retrieved_at: 2026-08-24T22:12:53.680740+00:00
---

# Overview

## What is WebDialer?

WebDialer is a built-in feature of CUCM that allows users to make click-to-dial (C2D) calls from applications, for example from a corporate directory web page or as a part of a custom desktop application.

WebDialer can make calls using either an end-user's credentials, or with an application-user's credentials on-behalf-of an end-user.  The call is launched directly from the end-user's phone.

Any phones supported by CUCM CTI (TAPI or JTAPI) can be used with WebDialer, see the CTI Supported Device Matrix

## WebDialer API Interfaces

There are two interfaces available for developing WebDialer integrations:

SOAP - This API uses SOAP over HTTPS to send XML formatted requests to CUCM.

Best for programmatic click-to-dial functionality; full control over the user experience.

Can be used with any programming language/framework capable of sending XML over HTTP.

For building desktop/mobile/service applications.

HTML - URL-based, this interface is designed to enable embedding simple HTML/JavaScript into existing web applications to provide WebDialer click-to-dial functionality.

Use-case: easily embed C2D into web pages without writing code.

Provides a basic interactive user interface for users to log in, select their desired/preferred calling device/line and launch/terminate a call.

Limited functionality; UI is not customizable.

Next