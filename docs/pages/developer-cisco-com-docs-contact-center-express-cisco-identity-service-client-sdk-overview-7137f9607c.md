---
doc_id: developer-cisco-com-docs-contact-center-express-cisco-identity-service-client-sdk-overview-7137f9607c
source_url: https://developer.cisco.com/docs/contact-center-express/cisco-identity-service-client-sdk-overview/
retrieved_at: 2026-09-07T14:06:03.918631+00:00
---

# What is Cisco Identity Service SDK?

Cisco Identity Service (IdS) is a light-weight OAuth server built to support Single Sign-On. From 11.5(1) release, onward, IdS is supported in Unified CCX, Unified CCE and Packaged CCE solutions.

Single Sign-On (SSO) is a user authentication process that allows users to sign in to one application and then securely access other authorized applications without the need to reenter the user credentials. Once authenticated, the user is allowed to access all authorized web applications for which the user has been provided the rights to access.

# Technical Overview

Cisco Identity Service uses the combination of Security Assertion Markup Language 2.0 (SAML 2.0) and OAuth 2.0 protocols to offer cross-domain and cross-product Single Sign-On for Cisco Customer Care solutions. It enables SSO across Cisco applications and enables federation between Cisco applications and an Identity Provider (IdP) .
It allows users to access secure web domains, to exchange user authentication data between an IdP, IdS and Applications while maintaining high security levels.
SAML 2.0 is used as the user authentication protocol. Using OAuth, IdS works as an OAuth server to issue tokens for allowing users to log in to various web applications and also access service REST APIs . The IdS supports the Authorization Code Grant flow implementation of OAuth.
IdS establishes a Circle of Trust (CoT) by exchanging metadata and certificates as part of the provisioning process between the IdP and the IdS. All the applications register as OAuth clients with the IdS to access and validate tokens with the IdS.
When an unauthenticated user tries to access an application, it triggers an Authcode Grant Flow and redirects to IdS to get an access token. IdS uses SAML to authenticate the user for which it acts like a SAML SP and redirects to IdP.
After IdP authenticates the user, it provides a SAML assertion which is accepted by IdS and an authcode is issued, which then can be exchanged for an access token and refresh token pair.
The authorization of the users is done locally in the individual applications.

# What can a developer do with the Cisco Identity Service SDK?

Integrating with the Cisco Identity Service SDK allows end users to seemlessly use various web applications and applications built with the REST APIs within the Cisco Contact Center solution after a single login. As a result, it reduces the number of logins for that user and provides a better user experience.

# What programming languages can I use to interact with the Cisco Identity Service SDK?

The Cisco Identity Service SDK exposes Java APIs, so therefore, any application that interacts with the SDK must also be in Java.

# Next Steps

The best way to really understand the Cisco Identity Service SDK is to try it for yourself. After installing the necessary components for the IdS Service,

- Download the Cisco Identity Service Client SDK .

- Follow the steps to register your application .

- Follow the steps to integrate your application using the IdS SDK .

Next