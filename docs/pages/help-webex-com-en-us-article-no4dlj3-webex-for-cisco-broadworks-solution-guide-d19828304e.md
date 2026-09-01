---
doc_id: help-webex-com-en-us-article-no4dlj3-webex-for-cisco-broadworks-solution-guide-d19828304e
source_url: https://help.webex.com/en-us/article/no4dlj3/Webex-for-Cisco-BroadWorks-Solution-Guide
retrieved_at: 2026-09-01T17:20:39.230887+00:00
---

### Deployment Overview

The following diagrams represent the typical order of your deployment tasks for the different user provisioning modes. Many of the tasks are common to all provisioning modes.

### Partner Onboarding for Webex for Cisco BroadWorks

Each Webex for Cisco BroadWorks Service Provider or Reseller needs a to be setup as a Partner Organization for Webex for Cisco BroadWorks. If you have an existing Webex Partner Organization, this can be used.

In order to complete the necessary onboarding, you must execute your Webex  Cisco BroadWorks paperwork and new partners must accept the online Indirect Channel Partner Agreement (ICPA). When these steps are completed, Cisco Compliance will create a new Partner Org in Partner Hub (if needed) and send an email with authentication details to the Admin of Record in your paperwork. At the same time, your Partner Activation and/or Customer Success Program Manager will contact you to start your onboarding.

Webex Partners in one region can create customer organizations in any region that we offer the services. For help, see: Data residency in Webex .

### Configure Services on Your Webex for Cisco BroadWorks XSP|ADPs

We require that the NPS application be run on a different XSP|ADP. Requirements for that
            XSP|ADP are described in Configure Call Notifications from your Network .

You need the following applications / services on your XSP|ADPs.

Service/Application

Authentication required

Service/application purpose

Xsi-Events

TLS (server authenticates itself to clients)

Call control, service notifications

Xsi-Actions

TLS (server authenticates itself to clients)

Call control, actions

Device management

TLS (server authenticates itself to clients)

Calling configuration download

Authentication Service

TLS (server authenticates itself to clients)

User authentication

Computer Telephony Integration

mTLS (client and server authenticate each other)

Telephony presence

Call Settings Webview application

TLS (server authenticates itself to clients)

Exposes user call settings in the selfcare portal within the Webex app

This section describes how to apply the required configurations for TLS and mTLS on these
            interfaces, but you should reference existing documentation to get the applications
            installed on your XSP|ADPs.

#### Co-Residency Requirements

Authentication Service must be co-resident with Xsi applications, because those interfaces must accept long-lived tokens for service authorization. The authentication service is required to validate those tokens.

Authentication service and Xsi can run on the same port if required.

You may separate the other services/applications as required for your scale
                        (dedicated device management XSP|ADP farm, for example).

You may co-locate the Xsi, CTI, Authentication Service, and DMS applications.

Do not install other applications or services on the XSP|ADPs that are used
                        for integrating BroadWorks with Webex.

Do not co-locate the NPS application with any other applications.

#### Xsi Interfaces

Install and configure the Xsi-Actions and Xsi-Events applications as described in Cisco BroadWorks Xtended Services Interface Configuration Guide .

Only one instance of the Xsi-Events applications should be deployed on the XSP|ADP
                used for the CTI interface.

All Xsi-Events used for integrating Broadworks with Webex must have the same callControlApplicationName defined under Applications/Xsi-Events/GeneralSettings. For example:

ADP_CLI/Applications/Xsi-Events/GeneralSettings> get

callControlApplicationName = com.broadsoft.xsi-events

When a user is onboarded to Webex, Webex creates a subscription for the user on the AS in order to receive telephony events for presence and call history. The subscription is associated with the callControlApplicationName and the AS uses it to know to which Xsi-Events to send the telephony events.

Changing the callControlApplicationName, or not having the same name on all Xsi-Events webapps will impact subscriptions and telephony events functionality.

#### Configure Authentication Service (with CI Token Validation)

Use this procedure to configure the Authentication Service to use CI Token Validation with TLS. This authentication method is recommended if you are running R22 or higher and your system supports it.

Mutual TLS (mTLS) is also supported as an alternative authentication method for
                    the Auth Service. If you have multiple Webex organizations running off the same
                    XSP|ADP server, you must use mTLS authentication because CI Token Validation
                    does not support multiple connections to the same XSP|ADP Auth Service.

To configure mTLS authentication for the Auth Service instead of CI Token Validation, refer to the Appendix for Configure Services (with mTLS for the Auth Service) .

If you currently use mTLS for the Auth Service, it's not mandatory that you reconfigure to use CI Token Validation with TLS.

Obtaining OAuth credentials for
                            your Webex for Cisco BroadWorks .

Install the following patches on each XSP|ADP server. Install the patches
                        that are appropriate to your release:

For R22:

AP.platform.22.0.1123.ap376508

AP.xsp.22.0.1123.ap376508

AP.xsp.22.0.1123.ap368601

For R23:

AP.xsp.23.0.1075.ap376509

AP.platform.23.0.1075.ap376509

For R24—no patch required

Any reference to XSP includes either XSP or ADP.

Install the AuthenticationService application on each
                        XSP|ADP service.

Run the following command to activate the AuthenticationService
                                application on the XSP|ADP to the /authService context
                                path.

Run this command to deploy the AuthenticationService on the
                                XSP|ADP:

Starting with Broadworks build 2022.10, the certificates authorities that are coming with Java are no longer automatically included to the BroadWorks trust store when switching to a new version of java. The AuthenticationService opens a TLS connection to Webex to fetch the access token, and needs to have the following in its truststore to validate the IDBroker and Webex URL:

IdenTrust Commercial Root CA 1

Go Daddy Root Certificate Authority - G2

Verify that these certificates are present under the following CLI

ADP_CLI/System/SSLCommonSettings/Trusts/Defaults> get

If not present, run the following command to import the default Java trusts:

ADP_CLI/System/SSLCommonSettings/Trusts/Defaults> importJavaCATrust

Alternatively, you can manually add these certificates as trust anchors with the following command:

ADP_CLI/System/SSLCommonSettings/Trusts/BroadWorks> updateTrust <alias> <trustAnchorFile>

If the ADP is upgraded from a previous release, then the certificate authorities from the old release are automatically imported to the new release and will continue to be imported until they are manually removed.

The AuthenticationService application is exempt from the validatePeerIdentity setting under ADP_CLI/System/SSLCommonSettings/GeneralSettings, and always validates the peer Identity. See the Cisco Broadworks X509 Certificate Validation FD for more info on this setting.

Configure the Identity Providers by running the following commands on each
                        XSP|ADP server:

XSP|ADP_CLI/Applications/AuthenticationService/IdentityProviders/Cisco>
                            get

set clientId client-Id-From-Step1

set enabled true

set clientSecret client-Secret-From-Step1

set ciResponseBodyMaxSizeInBytes 65536

set issuerName <URL> —For the URL , enter the IssuerName URL that applies to your CI Cluster. See following table.

set issuerUrl <URL> —For the URL , enter the IssuerUrl that applies to your CI Cluster. See the following table.

set tokenInfoUrl <IdPProxy URL> —Enter the IdP Proxy URL that applies to your Teams Cluster. See the second table that follows.

US-A

https://idbroker.webex.com/idb

EU

https://idbroker-eu.webex.com/idb

US-B

https://idbroker-b-us.webex.com/idb

CA

https://idbroker-ca.webex.com/idb

SG

https://idbroker-sg.webex.com/idb

IN

https://idbroker-in.webex.com/idb

AE

https://idbroker-ae.webex.com/idb

AU

https://idbroker-au.webex.com/idb

If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub.

ACHM

https://broadworks-idp-proxy-a.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

AFRA

https://broadworks-idp-proxy-k.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

AORE

https://broadworks-idp-proxy-r.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

ADXB

https://broadworks-idp-proxy-d.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

ASYD

https://broadworks-idp-proxy-m.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

If you don't know your Teams Cluster , you can obtain the information from the Customer details in the Help Desk view of Control Hub.

For testing, you can verify that the tokenInfoURL is valid by replacing the " idp/authenticate " portion of the URL with " ping ".

Specify the Webex entitlement that must be present in the user profile in Webex by running the following command:

XSP|ADP_CLI/Applications/AuthenticationService/IdentityProviders/Cisco/Scopes>
                            set scope broadworks-connector:user

Configure Identity Providers for Cisco Federation using the following
                        commands on each XSP|ADP server:

XSP|ADP_CLI/Applications/AuthenticationService/IdentityProviders/Cisco/Federation>
                            get

set flsUrl https://cifls.webex.com/federation

set refreshPeriodInMinutes 60

set refreshToken refresh-Token-From-Step1

Run the following command to validate that your FLS configuration is working. This command will return the list of Identity Providers:

XSP|ADP_CLI/Applications/AuthService/IdentityProviders/Cisco/Federation/ClusterMap>
                            Get

Configure Token Management using the following commands on each XSP|ADP
                        server:

XSP|ADP_CLI/Applications/AuthenticationService/TokenManagement>

set tokenIssuer BroadWorks

set tokenDurationInHours 720

Generate and Share RSA Keys. You must generate keys on one XSP|ADP then copy
                        them to all other XSP|ADPs. This is due to the following factors:

You must use the same public/private key pairs for token encryption/decryption across all instances of the authentication service.

The key pair is generated by the authentication service when it is first required to issue a token.

If you cycle keys or change the key length, you need to repeat the following configuration and restart all the XSP|ADPs.

Select one XSP|ADP to use for generating a key pair.

Use a client to request an encrypted token from that XSP|ADP, by
                                requesting the following URL from the client’s browser:

https://<XSP|ADP-IPAddress>/authService/token?key=BASE64URL(clientPublicKey)

(This generates a private / public key pair on the XSP|ADP, if there
                                wasn’t one already)

The key store location is not configurable. Export the keys:

XSP|ADP_CLI/Applications/authenticationService/KeyManagement> exportKeys

Copy the exported file /var/broadworks/tmp/authService.keys to the
                                same location on the other XSP|ADPs, overwriting an older .keys file if necessary.

Import the keys on each of the other XSP|ADPs:

XSP|ADP_CLI/Applications/authenticationService/KeyManagement> importKeys /var/broadworks/tmp/authService.keys

Provide the authService URL to the web container. The XSP|ADP’s web container
                        needs the authService URL so it can validate tokens. On each of the
                        XSP|ADPs:

Add the authentication service URL as an external authentication service for the BroadWorks Communications Utility:

XSP|ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/AuthService> set url http://127.0.0.1:80/authService

Add the authentication service URL to the container:

XSP|ADP_CLI/Maintenance/ContainerOptions> add
                                    tomcat bw.authservice.authServiceUrl
                                    http://127.0.0.1:80/authService

This enables Webex to use the Authentication Service to validate tokens presented as credentials.

Check the parameter with get .

Restart the XSP|ADP.

#### Remove Client Authentication Requirement for Auth Service (R24 only)

If you have the Authentication Service configured with CI Token validation on R24, you also need to remove the Client Authentication Requirement for the Authentication Service. Run the following CLI command:

ADP_CLI/Interface/Http/SSLCommonSettings/ClientAuthentication/WebApps> set <interfaceIp> <port> AuthenticationService clientAuthReq false

#### Configuring
                TLS and Ciphers on the HTTP Interfaces (for XSI and Authentication
                Service)

The Authentication Service, Xsi-Actions, and Xsi-Events
                applications use HTTP server interfaces. Levels of TLS configurability for these
                applications are as follows:

Most general = System > Transport > HTTP
                > HTTP Server interface = Most specific

The CLI contexts you use to view or
                modify the different SSL settings are:

XSP|ADP_CLI/System/SSLCommonSettings/JSSE/Ciphers>

XSP|ADP_CLI/System/SSLCommonSettings/JSSE/Protocols>

XSP|ADP_CLI/System/SSLCommonSettings/OpenSSL/Ciphers>

XSP|ADP_CLI/System/SSLCommonSettings/OpenSSL/Protocols>

XSP|ADP_CLI/Interface/Http/SSLCommonSettings/Ciphers>

XSP|ADP_CLI/Interface/Http/SSLCommonSettings/Protocols>

XSP|ADP_CLI/Interface/Http/HttpServer/SSLSettings/Ciphers>

XSP|ADP_CLI/Interface/Http/HttpServer/SSLSettings/Protocols>

Reading HTTP Server TLS Interface Configuration on the XSP|ADP

Sign in to the XSP|ADP and navigate to XSP|ADP_CLI/Interface/Http/HttpServer>

Enter the get command and read the results. You should see
                        the interfaces (IP addresses) and, for each, whether they are secure and
                        whether they require client authentication.

Apache tomcat mandates a certificate for each secure interface; the system
                generates a self-signed certificate if it needs one.

```
XSP|ADP_CLI/Interface/Http/HttpServer> get
```

Adding TLS 1.2 Protocol to the HTTP Server
                Interface

The HTTP interface that is interacting with the Webex Cloud must
                be configured for TLSv1.2. The cloud does not negotiate earlier versions of the TLS
                protocol.

To configure the TLSv1.2 protocol on the HTTP Server interface:

Sign in to the XSP|ADP and navigate to XSP|ADP_CLI/Interface/Http/HttpServer/SSLSettings/Protocols>

Enter the command get <interfaceIp> 443 to see which
                        protocols are already used on this interface.

Enter the command add <interfaceIp> 443 TLSv1.2 to
                        ensure that interface can use TLS 1.2 when communicating with the cloud.

Editing TLS Ciphers Configuration on the HTTP Server Interface

To
                configure the required ciphers:

Sign in to the XSP|ADP and navigate to XSP|ADP_CLI/Interface/Http/HttpServer/SSLSettings/Ciphers>

Enter the command get <interfaceIp> 443 to see which
                        ciphers are already used on this interface. There must be at least one from
                        the Cisco recommended suites (see XSP|ADP Identity and Security
                            Requirements in the Overview section).

Enter the command add <interfaceIp> 443
                            <cipherName> to add a cipher to the HTTP Server
                        interface.

The XSP|ADP CLI requires the IANA standard cipher suite name, not the
                            openSSL cipher suite name. For example, to add the openSSL cipher ECDHE-ECDSA-CHACHA20-POLY1305 to the HTTP server
                            interface, you would use: XSP|ADP_CLI/Interface/Http/HttpServer/SSLSettings/Ciphers> add
                                192.0.2.7 443 TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305

See https://ciphersuite.info/ to find the suite by either name.

#### Configure Device Management on XSP|ADP, Application Server, and Profile
                Server

Profile Server and XSP|ADP are mandatory for Device Management. They must be
                configured according to instructions in the BroadWorks Device Management Configuration
                    Guide .

### CTI Interface and Related Configuration

The “inmost to outmost” configuration order is listed below. Following this order is not mandatory.

Configure Application Server for CTI Subscriptions

Configure XSP|ADPs for mTLS Authenticated CTI Subscriptions

Open Inbound Ports for Secure CTI Interface

Subscribe Your Webex Organization to BroadWorks CTI Events

#### Configure Application Server for CTI Subscriptions

Update the ClientIdentity on Application Server with the common name (CN) of the Webex for Cisco BroadWorks CTI client certificate.

For each Application Server you are using with Webex, add the certificate identity to the ClientIdentity as follows:

AS_CLI/System/ClientIdentity> add bwcticlient.webex.com

The common name of the Webex for Cisco BroadWorks client certificate is bwcticlient.webex.com .

#### Configure TLS and Ciphers on the CTI Interface

The levels of configurability for the XSP|ADP CTI interface are as follows:

Most general = System > Transport > CTI Interfaces > CTI interface = Most specific

The CLI contexts you use to view or modify the different SSL settings are:

Specificity

CLI Context

System (global)

(R22 and later)

XSP|ADP_CLI/System/SSLCommonSettings/JSSE/Ciphers>

XSP|ADP_CLI/System/SSLCommonSettings/JSSE/Protocols>

Transport protocols for this system

(R22 and later)

XSP|ADP_CLI/System/SSLCommonSettings/OpenSSL/Ciphers>

XSP|ADP_CLI/System/SSLCommonSettings/OpenSSL/Protocols>

All CTI interfaces on this system

(R22 and later)

XSP|ADP_CLI/Interface/CTI/SSLCommonSettings/Ciphers>

XSP|ADP_CLI/Interface/CTI/SSLCommonSettings/Protocols>

A specific CTI interface on this system

(R22 and later)

XSP|ADP_CLI/Interface/CTI/CTIServer/SSLSettings/Ciphers>

XSP|ADP_CLI/Interface/CTI/CTIServerSSLSettings/Protocols>

On a fresh install, the following ciphers are installed by default at the system level. If nothing is configured at the interface level (for example, at the CTI interface or HTTP interface), this cipher list applies. Note that this list may change over time:

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256

TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256

TLS_DHE_DSS_WITH_AES_128_GCM_SHA256

TLS_DHE_RSA_WITH_AES_128_GCM_SHA256

TLS_DHE_RSA_WITH_AES_128_CBC_SHA256

TLS_DHE_DSS_WITH_AES_128_CBC_SHA256

TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256

TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256

TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256

Reading CTI TLS Interface Configuration on the XSP|ADP

Sign in to the XSP|ADP and navigate to XSP|ADP_CLI/Interface/CTI/CTIServer>

Enter the get command and read the results. You should see the interfaces (IP addresses) and, for each, whether they require a server certificate and whether they require client authentication.

```
XSP|ADP_CLI/Interface/CTI/CTIServer> get
  Interface IP  Port  Secure  Server Certificate  Client Auth Req
=================================================================
  10.155.6.175  8012    true                true             true
```

Adding TLS 1.2 Protocol to the CTI Interface

The XSP|ADP CTI interface that is interacting with the Webex Cloud must be configured
                for TLS v1.2. The cloud does not negotiate earlier versions of the TLS protocol.

To configure the TLSv1.2 protocol on the CTI interface:

Sign in to the XSP|ADP and navigate to XSP|ADP_CLI/Interface/CTI/CTIServer/SSLSettings/Protocols>

Enter the command get <interfaceIp> to see which protocols are already used on this interface.

Enter the command add <interfaceIp> TLSv1.2 to ensure that interface can use TLS 1.2 when communicating with the cloud.

Editing TLS Ciphers Configuration on the CTI Interface

To configure the required ciphers on the CTI interface:

Sign in to the XSP|ADP and navigate to XSP|ADP_CLI/Interface/CTI/CTIServer/SSLSettings/Ciphers>

Enter the get command to see which ciphers are already used
                        on this interface. There must be at least one from the Cisco recommended
                        suites (see XSP|ADP Identity and Security Requirements in the
                        Overview section).

Enter the command add <interfaceIp> <cipherName> to add a cipher to the CTI interface.

The XSP|ADP CLI requires the IANA standard cipher suite name, not the
                            openSSL cipher suite name. For example, to add the openSSL cipher ECDHE-ECDSA-CHACHA20-POLY1305 to the CTI interface,
                            you would use: XSP|ADP_CLI/Interface/CTI/CTIServer/SSLSettings/Ciphers> add 192.0.2.7 TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305

See https://ciphersuite.info/ to find the suite by either name.

#### Trust Anchors for CTI Interface (R22 and later)

This procedure assumes the XSP|ADPs are either internet-facing or face the internet
                via pass-through proxy. The certificate configuration is different for a bridging
                proxy (see TLS Certificate Requirements for TLS-bridge Proxy ).

For each XSP|ADP in your infrastructure that is publishing CTI events to Webex, do
                the following:

Sign in to Partner Hub.

Go to Services > Additional links and click Download Webex CA Certificate to get CombinedCertChain2023.txt on your local computer.

These files contain two sets of two certificates. You need to split the
                            files before you upload them to the XSP|ADPs. All files are
                            required.

Split the certificate chain into two certificates - combinedcertchain2023.txt

Open combinedcertchain2023.txt in
                                a text editor.

Select and cut the first block of text, including
                                the lines -----BEGIN CERTIFICATE----- and -----END CERTIFICATE----- , and paste the text
                                block into a new file.

Save the new file as root2023.txt .

Save the original file as issuing2023.txt . The original file should now
                                only have one block of text, surrounded by the lines -----BEGIN CERTIFICATE----- and -----END CERTIFICATE----- .

Copy both text files to a temporary location on the XSP|ADP you are securing,
                        e.g. /var/broadworks/tmp/root2023.txt and /var/broadworks/tmp/issuing2023.txt

Sign in to the XSP|ADP and navigate to /XSP|ADP_CLI/Interface/CTI/SSLCommonSettings/ClientAuthentication/Trusts>

(Optional) Run help updateTrust to see the parameters and command format.

Upload the certificate files to new trust anchors - 2023

XSP|ADP_CLI/Interface/CTI/SSLCommonSettings/ClientAuthentication/Trusts> updateTrust webexclientroot2023
                            /var/broadworks/tmp/root2023.txt

XSP|ADP_CLI/Interface/CTI/SSLCommonSettings/ClientAuthentication/Trusts> updateTrust webexclientissuing2023
                            /var/broadworks/tmp/issuing2023.txt

All aliases must have a different name. webexclientroot2023 , and webexclientissuing2023 are example aliases for the trust anchors; you can use your own as long as all entries are unique.

Confirm the anchors are updated:

XSP|ADP_CLI/Interface/CTI/SSLCommonSettings/ClientAuthentication/Trusts> get

```
Alias   Owner                                   Issuer
=============================================================================
webexclientissuing2023       Internal Private TLS SubCA      Internal Private Root
webexclientroot2023       Internal Private Root      Internal Private Root[self-signed]
```

Allow clients to authenticate with certificates:

```
XSP|ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CertificateAuthentication> set allowClientApp true
```

#### Add CTI Interface and Enable mTLS

Add the CTI SSL interface.

The CLI context depends on your BroadWorks version. The command creates a self-signed server certificate on the interface, and forces the interface to require a client certificate.

On BroadWorks R22 and R23:

XSP|ADP_CLI/Interface/CTI/CTIServer> add <Interface
                                    IP> 8012 true true true

Replace the server certificate and key on the XSP|ADP's CTI interfaces. You
                        need the IP address of the CTI interface for this; you can read it from the
                        following context:

On BroadWorks R22 and R23:

XSP|ADP_CLI/Interface/CTI/CTIServer> get

Then run the following commands to replace the interface’s self-signed certificate with your own certificate and private key:

XSP|ADP_CLI/Interface/CTI/CTIServer/SSLSettings/Certificates>
                                    sslUpdate <interface IP> keyFile</path/to/certificate
                                    key file> certificateFile </path/to/server certificate>
                                    chainFile</path/to/chain file>

Restart the XSP|ADP.

#### Enable Access to BroadWorks CTI Events on Webex

You
                need to add and validate the CTI interface when you configure your clusters in
                Partner Hub. See Configure Your Partner Organization in Partner Hub for
                detailed instructions.

Specify the CTI address by which Webex can subscribe to BroadWorks CTI Events.

CTI subscriptions are on a per-subscriber basis and are only established and
                        maintained while that subscriber is provisioned for Webex for Cisco
                        BroadWorks.

### Call Settings Webview

Call Settings Webview (CSWV) is an application hosted on XSP|ADP to enable users to
            modify their BroadWorks call settings through a webview that they see in the soft
            client. See the Cisco BroadWorks Call Settings Webview Solution
                Guide .

Webex makes use of this feature to provide users with access to common BroadWorks call settings that are not native to the Webex App.

If you want your Webex for Cisco BroadWorks subscribers to access call settings beyond the defaults available in the Webex app, you need to deploy Call Settings Webview feature.

Call Settings Webview has two components:

Call Settings Webview application, hosted on a Cisco BroadWorks XSP|ADP.

The Webex App, which renders the call settings in a Webview.

#### User Experience

Windows users: Click Call Settings and then click Open Call Preferences > Advanced Call Settings .

Mac users: Click profile picture, then Preferences > Advanced Call Settings .

### Deploy CSWV on BroadWorks

#### Install Call Settings Webview on XSP|ADPs

CSWV application must be on the same XSP|ADP(s) that host the Xsi-Actions interface
                in your environment. It is an unmanaged application on XSP|ADP, so you need to
                install and deploy a web archive file.

Sign in to cisco.com and search for "BWCallSettingsWeb" in the software download section.

Find and download the most recent version of the file.

For example, BWCallSettingsWeb_1.8.2_1.war ( https://software.cisco.com/download/home/286326302/type/286326345/release/RI.2022.04 ) was the most recent at the time of writing.

Install, activate, and deploy the web archive according to the Cisco
                        BroadWorks Xtended Service Platform Configuration Guide for your XSP|ADP
                        version. (R24 version is https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/broadworks/Design/XSP/BW-XtendedServicesInterfaceConfigGuide.pdf ).

Copy the .war file to a temporary location on the XSP|ADP, such as /tmp/ .

Navigate to the following CLI context and run the install command:

XSP|ADP_CLI/Maintenance/ManagedObjects> install
                                    application /tmp/BWCallSettingsWeb_1.7.5_1.war

The BroadWorks software manager validates and installs the file.

[Optional] Delete /tmp/BWCallSettingsWeb_1.7.5_1.war (this file is no longer required).

Activate the application:

XSP|ADP_CLI/Maintenance/ManagedObjects> activate
                                    application BWCallSettingsWeb 1.7.5 /callsettings

The name and version are mandatory for any application, but for CSWV you must also provide a contextPath because it is an unmanaged application. You can use any value that is not used by another application, for example, /callsettings .

Deploy the Call Settings application on the selected context path:

XSP|ADP_CLI/Maintenance/ManagedObjects> deploy
                                    application /callsettings

You can now predict the call settings URL that you will specify for clients, as follows:

https:// <XSP|ADP-FQDN> /callsettings/

Notes:

You must supply the trailing slash on this URL when you enter it in the client configuration file.

The XSP|ADP-FQDN must match the Xsi-Actions FQDN, because CSWV needs
                                to use Xsi-Actions, and CORS is not supported.

Make sure to add the <XSP|ADP-FQDN> to the HttpAlias on each ADP or XSP hosting CSWV: ADP_CLI/Interface/Http/HttpAlias>

Repeat this procedure for other XSP|ADPs in your Webex for Cisco BroadWorks environment (if necessary).

The Call Settings Webview application is now active on the XSP|ADPs.

### Configure the Webex App to use Call Settings Webview

For more detail on client configuration, see Webex for Cisco BroadWorks Configuration Guide .

There's a custom tag in the Webex app configuration file that you can use to set the CSWV URL. This URL shows the call settings to the users through the application interface.

```
<config>
    <services>
        <web-call-settings target="%WEB_CALL_SETTINGS_TARGET_WXT%">
            <url>%WEB_CALL_SETTINGS_URL_WXT%</url>
        </web-call-settings>
```

In the Webex app configuration template on BroadWorks, configure the CSWV URL in the %WEB_CALL_SETTINGS_URL_WXT% tag.

If you don't explicitly specify the URL, the default is empty and the call settings page isn't visible to the users.

Make sure you have the latest configuration templates for the Webex app (see Device Profiles ).

Set the Web Call Settings Target to csw :

%WEB_CALL_SETTINGS_TARGET_WXT% csw

Set the Web Call Settings URL for your environment, for example:

%WEB_CALL_SETTINGS_URL_WXT% https://yourxsp.example.com/callsettings/

You derived this value when deploying the CSWV application.

The resulting client configuration file should have an entry as follows:

```
<web-call-settings target="csw">
    <url>https://yourxsp.example.com/callsettings/</url>
</web-call-settings>
```

Any reference to XSP includes either XSP or ADP.

### Configure call push notifications in Webex for BroadWorks

In this document we use the term Call Notifications Push Server (CNPS) to describe an XSP-hosted, or ADP-hosted application that runs in your environment. Your CNPS works with your BroadWorks system to be aware of incoming calls to your users, and pushes notifications of those to the Google Firebase Cloud Messaging (FCM) or Apple Push Notification service (APNs) notification services.

Those services notify the mobile devices of Webex for Cisco BroadWorks subscribers that they have incoming calls on Webex.

For more information about NPS, see the Notification Push Server Feature Description .

A similar mechanism in Webex works with Webex messaging and presence services to push notifications to the Google (FCM) or Apple (APNS) notification services. Those services in turn notify the mobile Webex users of incoming messages or presence changes.

This section describes how to configure NPS for authentication proxy when the NPS
                doesn’t already support other apps. If you need to migrate a shared NPS to use NPS
                proxy, see Updating Cisco BroadWorks NPS to Use NPS Proxy .

#### NPS Proxy Overview

For compatibility with Webex for Cisco BroadWorks, your CNPS must be patched to support the NPS Proxy feature, Push Server for VoIP in UCaaS .

The feature implements a new design in the Notification Push Server to resolve the security vulnerability of sharing push notification certificate private keys with service providers for mobile clients. Instead of sharing push notification certificates and keys with the service provider, the NPS uses a new API to obtain a short-lived push notification token from Webex for Cisco BroadWorks backend, and uses this token for authentication with the Apple APNs and Google FCM services.

The feature also enhances the capability of the Notification Push Server to push notifications to Android devices through the new Google Firebase Cloud Messaging (FCM) HTTPv1 API.

For more information, see the Push Server for VoIP in UCaaS Feature Description .

The BroadWorks patches for the feature are available on: https://software.cisco.com/download/home/286326302/type/286326345/release/RI.2022.04 .

For NPS software and patches, see the section Prepare Your NPS for Webex for Cisco BroadWorks .

Search and download the patch from the software download page.

More information on the ADP server can be found at Cisco BroadWorks Application Delivery
                            Platform .

#### APNS Considerations

Apple will no longer support the HTTP/1-based binary protocol on the Apple Push Notification
				service after March 31, 2021. We recommend that you configure your XSP|ADP to use
				the HTTP/2-based interface for APNs. This update requires that your XSP|ADP hosting
				the NPS be running R22 or later.

#### Prepare Your NPS for Webex for Cisco BroadWorks

Install and configure a dedicated XSP (minimum version R22), or Application Delivery Platform (ADP).

Install the NPS Authentication Proxy patches:

Activate the Notification Push Server application.

(For Android notifications) Enable the FCM v1 API on the NPS.

XSP_CLI/Applications/NotificationPushServer/FCM> set V1Enabled true

(For Apple iOS notifications) Enable HTTP/2 on the NPS.

XSP_CLI/Applications/NotificationPushServer/APNS/GeneralSettings> set HTTP2Enabled true

This is exclusive to Release 22 and earlier versions; it is not available in Release 23 and above versions, which only support HTTP/2.

Attach a techsupport from the NPS XSP/ADP.

On each AS server:

Set the Push URL, Example: AS_CLI/System/NotificationPushServer> set url https://qaxsps.broadsoft.com/nps

The namedefs file in /usr/local/broadworks/bw_base/conf must be configured with SRV and A records for Notification Push Server (XSP/ADP) lookup, if multiple XSP/ADP then add an entry for each as required.

Example for multiple ADP/XSP:

_pushnotification-client._tcp.qaxsps.broadsoft.com SRV 20 20 443 ADP1-qaxsps.broadsoft.com

_pushnotification-client._tcp.qaxsps.broadsoft.com SRV 20 20 443 ADP2-qaxsps.broadsoft.com

ADP1-qaxsps.broadsoft.com IN A 10.193.78.149

ADP2-qaxsps.broadsoft.com IN A 10.193.78.150

Once set, one of the following is required to pickup the changes:

A restartbw be preformed in a maintenance window.

Via the Cisco BroadWorks CLI:

R24 and older

AS_CLI/ASDiagnostic/DNS> reload

R25 +

AS_CLI/ASDiagnostic/DNS/ExecutionServer> reload

AS_CLI/ASDiagnostic/DNS/ProvisioningServer> reload

What to do next

For fresh installs of an NPS, go to Configure NPS to use authentication proxy

To migrate an existing Android deployment to FCMv1, go to Migrate NPS to FCMv1

#### Configure NPS to use authentication proxy

This task applies to a new installation of NPS, dedicated to Webex for Cisco BroadWorks.

If you want to configure the authentication proxy on an NPS that is shared with other
                mobile apps, see Updating Cisco BroadWorks NPS to Use NPS Proxy .

Obtaining OAuth credentials for your Webex for Cisco
                    BroadWorks .

Create the client account on the NPS:

XSP|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> set clientId client-Id-From-Step1

```
XSP|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> set clientSecret New Password: client-Secret-From-Step1
```

```
XSP|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> set RefreshToken New Password: Refresh-Token-From-Step1
```

To verify the values you entered match with what you were given, run XSP|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> get

The CiscoCI issuerUrl should ALWAYS be US CI cluster irrespective of your
                            location and the default should be:

```
XSP|ADP_CLI/Applications/NotificationPushServer/CiscoCI> get issuerUrl = https://idbroker.webex.com/idb
```

Enter the NPS Proxy URL, and set the token refresh interval (30 minutes recommended):

Region-based FQDNs:

US East:

XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-a.wbx2.com/nps/

US West:

XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-r.wbx2.com/nps/

Europe:

XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-k.wbx2.com/nps/

XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set VOIPTokenRefreshInterval 1800

Saudi Arabia:

XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-d.wbx2.com/nps/

Australia:

XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-m.wbx2.com/nps/

If push notifications time out due to a delay in DNS resolution, increase the timeout value in the "/etc/resolv.conf" file on the BroadWorks server.

(For Android notifications) Add the Android application ID to the FCM applications context on the NPS.

XSP|ADP_CLI/Applications/NotificationPushServer/FCM/Applications> add com.cisco.wx2.android

(For Apple iOS notifications) Add the application ID to the APNS applications context, making sure to omit the Auth key – set it to empty.

XSP|ADP_CLI/Applications/NotificationPushServer/APNS/Production/Tokens> add com.cisco.squared

Configure the following NPS URLs:

XSP|ADP CLI Context

Parameter

Value

XSP|ADP_CLI/Applications/NotificationPushServer/FCM>

authURL

https://www.googleapis.com/oauth2/v4/token

pushURL

https://fcm.googleapis.com/v1/projects/PROJECT-ID/messages:send

scope

https://www.googleapis.com/auth/firebase.messaging

XSP|ADP_CLI/Applications/NotificationPushServer/APNS/Production>

url

https://api.push.apple.com/3/device

Configure the following NPS connection parameters to the recommended values shown:

XSP|ADP CLI Context

Parameter

Value

XSP|ADP_CLI/Applications/

NotificationPushServer/FCM>

tokenTimeToLiveInSeconds

3600

connectionPoolSize

10

connectionTimeoutInMilliseconds

3600

connectionIdleTimeoutInSeconds

600

XSP|ADP_CLI/Applications/NotificationPushServer/

APNS/Production>

connectionTimeout

3000

connectionPoolSize

2

connectionIdleTimeoutInSeconds

600

Check if the Application Server is screening application IDs, because you may need to add the Webex apps to the allow list:

Run AS_CLI/System/PushNotification> get and
                            check the value of enforceAllowedApplicationList . If
                            it’s true , you need to complete this sub task.
                            Otherwise, skip the rest of the sub task.

AS_CLI/System/PushNotification/AllowedApplications> add com.cisco.wx2.android “Webex Android”

AS_CLI/System/PushNotification/AllowedApplications> add com.cisco.squared “Webex iOS”

Restart the XSP|ADP: bwrestart

Test call notifications by making calls from a BroadWorks subscriber to two
                    Webex mobile users. Verify that the call notification appears on iOS and Android
                    devices.

#### Migrate NPS to FCMv1

This topic contains optional procedures that you can use in Google FCM Console when you have an existing NPS deployment that you need to migrate to FCMv1. There are three procedures:

Migrate UC-One clients to FCMv1 —When you have existing UCaaS clients and need to migrate them to use FCMv1.

Migrate SaaS Clients to FCMv1 —When you have existing SaaS clients and need to migrate them to use FCMv1.

Update ADP Server —When you are migrating the NPS to an ADP server.

##### Migrate UC-One Clients to FCMv1

Use the below steps in Google FCM Console to migrate UC-One clients to Google FCM HTTPv1.

If branding is applied to the client, the client must have the Sender ID. In the FCM Console, see Project Settings > Cloud Messaging . The setting appears in the Project credentials table.

For details, see the Connect Mobile Branding Guide . Refer to
					the gcm_defaultSenderId parameter, which is located in the
					Branding Kit, Resource folder, branding.xml file with the below syntax:

<string name="gcm_defaultSenderId">xxxxxxxxxxxxx</string>

Log into FCM Admin SDK at http://console.firebase.google.com .

Select the appropriate Android application.

In the General tab, record the project ID

Navigate to the service accounts tab to configure a service account. You can create a new service account or configure an existing one.

To create a new Service Account:

Click the blue button for create new service account

Click on the blue button to generate a new private key

Download key to a secure location

To reuse an existing service account:

Click on the blue text to view existing service accounts.

Identify the service account to use. Service account needs permission firebaseadmin-sdk .

On the very right, click the hamburger menu and create a new private key.

Download the json file that contains the key and save to a secure location.

Copy the json file onto the XSP|ADP.

Configure the project ID and :

```
XSP|ADP_CLI/Applications/NotificationPushServer/FCM/Projects> add <project id> <path/to/json-key-file>
...Done

XSP|ADP_CLI/Applications/NotificationPushServer/FCM/Projects> get
  Project ID  Accountkey
========================
  my_project    ********
```

Configure the application:

```
XSP|ADP_CLI/Applications/NotificationPushServer/FCM/Applications> add <app id> projectId <project id>
...Done

XSP|ADP_CLI/Applications/NotificationPushServer/FCM/Applications> get
  Application ID    Project ID
==============================
          my_app    my_project
```

Enable FCMv1:

```
XSP|ADP_CLI/Applications/NotificationPushServer/FCM> set V1Enabled true
...Done
```

Run the bwrestart command to restart the XSP|ADP.

##### Migrate SaaS Clients to FCMv1

Use the below steps on Google FCM Console if you want to migrate SaaS clients to FCMv1.

Make sure that you have already completed the procedure "Configure NPS to Use Authentication Proxy".

Disable FCM:

```
XSP|ADP_CLI/Applications/NotificationPushServer/FCM> set V1Enabled false
...Done
```

Run the bwrestart command to restart the XSP|ADP.

Enable FCM:

```
XSP|ADP_CLI/Applications/NotificationPushServer/FCM> set V1Enabled true
...Done
```

Run the bwrestart command to restart the XSP|ADP.

##### Update ADP Server

Use the below steps in Google FCM Console if you are migrating the NPS to use an ADP server.

Get the JSON file from the Google Cloud Console:

On the Google Cloud Console, go to the Service Accounts page.

Click Select a project , choose your project and click Open .

Find the row of the service account that you want to create a key for, click the More vertical button, then click Create key.

Select a Key type and click Create

The file downloads.

Add FCM to the ADP server:

Import the JSON file to the ADP server using the /bw/install command.

Login to the ADP CLI and add Project and API key:

ADP_CLI/Applications/NotificationPushServer/FCM/Projects> add connect /bw/install/google JSON :

Next, add the Application and key:

ADP_CLI/Applications/NotificationPushServer/FCM/Applications> add com.broadsoft.ucaas.connect projectId connect-ucaas...Done

Verify the configuration:

```
ADP_CLI/Applications/NotificationPushServer/FCM/Projects> g
Project ID Accountkey
========================
connect-ucaas ********

ADP_CLI/Applications/NotificationPushServer/FCM/Applications> g
Application ID Project ID
===================================
com.broadsoft.ucaas.connect connect-ucaas
```

### Configure Your Partner Organization in Partner Hub

#### Configure Your BroadWorks Clusters

[once per cluster]

This is done for the following reasons:

To enable Webex cloud to authenticate your users against BroadWorks (via
                        XSP|ADP-hosted authentication service).

To enable Webex apps to use Xsi interface for call control.

To enable Webex to listen for CTI events published by BroadWorks (telephony presence and call history).

The cluster wizard automatically validates the interfaces as you add them. You can continue editing the cluster if any of the interfaces do not validate successfully, but you cannot save a cluster if there are invalid entries .

We prevent this because a misconfigured cluster could cause issues that are difficult to solve.

What you need to do:

Sign in to Partner Hub at admin.webex.com .

Open Services page from the side menu, and find Additional links card.

If the admin user does not have visibility of the Additional links card, it is recommended that you must open a case with Cisco TAC.

Click Add Cluster .

This launches a wizard where you supply your XSP|ADP interfaces (URLs). You
                        can add a port to the interface URL if you are using a non-standard
                        port.

Name this cluster and click Next .

The cluster concept here is simply a collection of interfaces, typically
                        collocated on an XSP|ADP server or farm, that enable Webex to read
                        information from your Application Server (AS). You may have one XSP|ADP per
                        AS cluster, or multiple XSP|ADPs per cluster, or multiple AS clusters per
                        XSP|ADP. Scale requirements for your BroadWorks system are out of scope
                        here.

(Optional) Enter a BroadWorks user Account Name and Password that you know is within the BroadWorks system you are connecting to Webex, then click Next .

The validation tests can use this account to validate the connections to the interfaces in the cluster.

Add your XSI Actions and XSI Events URLs.

Optional. Update the DAS URL with the URL of the Device Activation Service.

Optional. Check the Enable direct BroadWorks authentication check box if you want logins to BroadWorks to be direct to BroadWorks. Otherwise, authentication to BroadWorks is proxied through the Webex-hosted IdP proxy service.

This check box affects these login situations:

User Activation Portal login—Users must enter their BroadWorks credentials when logging in to the portal. The above setting determines if the login is direct to BroadWorks or is through the IdP Proxy.

Client Login—If BroadWorks Authentication is configured in the Onboarding template, the above setting determines if client login to the Webex App is direct to BroadWorks or is proxied through the IdP Proxy.

Click Next .

On the CTI Interface page, do the following:

Add the CTI URL and Port for the CTI interface to which you want to connect.

Optional. Enable the Call History toggle and then enter your BroadWorks user ID. When this option is selected, BroadWorks call history events get synced to the Webex cloud. Users can view their call history on the Webex App.

Optional. Enable the Do not disturb (DND) sync toggle and then enter your BroadWorks user ID. This option syncs DND events between Webex and BroadWorks, ensuring that the feature works the same on both platforms.

Optional. Enable the Personal Assistant Status Sync toggle and then enter your BroadWorks user ID. This option synchronizes the personal assistant presence status between the BroadWorks Calling devices and the Webex App.

Click Next .

Add your Authentication Service URL.

Select Auth Service with CI token validation .

This option does not require mTLS to protect the connection from Webex, because the Authentication Service properly validates the user token against the Webex identity service before it issues the long-lived token to the user.

Review your entries on the final screen, and then click Create . You should see a success message.

Partner Hub passes the URLs to various Webex microservices that test the connections to the supplied interfaces.

Click View Clusters and you should see your new cluster, and whether the validation succeeded.

The Create button may be disabled on the final (preview) screen of the wizard. If you cannot save the template, it indicates a problem with one of the integrations you just configured.

We implemented this check to prevent errors in subsequent tasks. You can go
                        back through the wizard as you configure your deployment, which may require
                        modifications to your infrastructure (e.g. XSP|ADP, load balancer, or
                        firewall) as documented in this guide, before you can save the template.

#### Checking the Connections to Your BroadWorks Interfaces

Sign in to Partner Hub (admin.webex.com) with your partner administrator credentials.

Open Services page from the side menu, and find BroadWorks Calling card.

Click View Broadworks Calling .

Partner Hub initiates connectivity tests from the various microservices towards the interfaces in the clusters.

After the tests complete, the cluster list page shows status message next to each cluster.

You should see green Success messages. If you see a red Error message, click the affected cluster name to see which setting is causing the problem.

Optional. Select a cluster if you want to see existing settings for that cluster, such as XSI-Actions, XSI-Events, DAS URL and the CTI interface settings.

#### Configure your Onboarding templates

Onboarding templates are the way that you will apply shared configuration to one or more customers as you onboard them via the provisioning methods. You must associate each template with a cluster (that you created in previous section).

You can create as many templates as you need, but only one template can be associated with a customer.

Sign in to the Partner Hub and select Customers .

Click the Onboarding templates button to view the existing templates.

Click Create Template .

In the Template Details window, add the Template name, Country or Region and Default email Language.

Click the drop-down for the CCW Subscription ID , find the listed subscriptions for the partner, and select the applicable subscription.

This field is shown only for partners migrated from Webex for BroadWorks to Webex.

In the Service Setting window, use the Cluster dropdown to choose the cluster you want to use with this template.

Enter a Template Name , then click Next .

Configure your provisioning mode, using these recommended settings:

Setting Name

Flowthrough provisioning with trusted emails

Flowthrough provisioning without emails

User self-provisioning

Enable BroadWorks Flow Through Provisioning (include provisioning account credentials if On**)

On

Supply the provisioning Account Name and Password as per BroadWorks configuration.

On

Supply the provisioning Account Name and Password as per BroadWorks configuration.

Off

Automatically Create New Organizations in Control Hub

On †

On †

On †

Service Provider Email Address

Select an email address from the dropdown (you can type some characters, to find the address if it's a long list).

This email address identifies the administrator within your Partner organization who will be granted delegated admin access to any new customer organizations created with the Onboarding template.

Country

Choose which country you use for this template.

The country you choose matches customer organizations that are created with this template to a particular region. At present, the region could be (EMEAR) or (North America and rest of world). See the country to region mappings in this spreadsheet .

The organization country will determine the default global call-in numbers for Cisco PSTN in Webex Meeting Sites. Refer to the Country section of help page for more information.

BroadWorks Enterprise Mode Active

Enable this if the customers you provision with this template are enterprises in BroadWorks.

If they are groups, leave this switch off.

If you have a mix of enterprises and groups in your BroadWorks, you should create different templates for those different cases.

Notes from the table:

† This switch ensures that a new customer organization is created if a subscriber’s email domain does not match an existing Webex organization.

This should always be on, unless you are using a manual ordering and fulfilment process (via Cisco Commerce Workspace) to create customer organizations in Webex (before you start provisioning users in those organizations). That option is often referred to as the "Hybrid Provisioning" model, and is out of the scope of this document.

** "Provisioning account" refers to the BroadWorks system-level admin account. On BroadWorks, you need an admin account with these attributes: Administrator Type=Provisioning, Read-only=Off.

Select the default services package for customers using this template (see Packages in the Overview section); either Basic , Standard , Premium or Softphone .

You can override this setting for individual users via Partner Hub.

Optional. Check Disable Cisco Webex Free Calling if you want to disable Webex Calls,.

For Meeting Join Configuration , select one of the following options:

Cisco Call-in Numbers (PSTN)

Partner-provided Call-in Numbers (BYoPSTN) —If you select this option, refer the Bring Your Own PSTN Solution Guide for Webex for Cisco BroadWorks for detailed information on how to configure this option.

Click Next .

There are two approaches for provisioning subscribers with regards to how their identities are verified – using Trusted Emails or Untrusted Emails.

In the Trusted Email workflow users provide email addresses to the partner who adds them in BroadWorks. You as a partner are responsible for provisioning the email address as part of either the flow-through or API method.

It is highly recommended to use the Trusted provisioning method because it ensures that all subscribers are fully provisioned by you as a partner and there is no action required from the end users.

In the Untrusted email case users need to verify their emails before provisioning, or users can self-activate themselves.

In the Untrusted case there are several provisioning modes based on the verification settings in the table below:

Setting Name

Flowthrough provisioning without emails

User self-provisioning

Provision Admin First

Recommended*

Not applicable

Allow users to self activate

Not applicable

Required

Notes from the table:

* Each customer organization in Webex is required to have at least one user with administrator role. The first user to whom you assign Integrated IM&P in BroadWorks takes the customer administrator role if a new customer organization is created in Webex. As a Service Provider you may want to have control over who gets the role. Checking this setting blocks users from completing activation until the first user you provisioned is activated. If you uncheck this setting, then the first user to become active in the new organization becomes the customer administrator.

Click Next .

Select the default authentication mode (either BroadWorks Authentication or Webex Authentication ) for user login to Webex.

This setting has no effect on user login to the User Activation Portal. Users must use their BroadWorks user ID and password when logging in to the portal, irrespective of how the Onboarding template is configured.

This setting will be applied to newly created customer organizations only. If partner administrators try to apply a new authentication setting to existing customer organizations, the existing settings apply so that existing users don't lose access. To change the authentication mode for existing customer organizations, you must open a ticket with Cisco TAC.

(See Authentication Mode in the Prepare your Environment section).

Click Next .

For Preferences , configure the following:

Choose whether you want to Prefill user email addresses in login page .

You should only use this option if you selected BroadWorks Authentication and have also have put the users’ email addresses in the Alternate ID attribute in BroadWorks. Otherwise, they will need to use their BroadWorks username. The login page gives an option to change user, if necessary, but this may lead to login issues.

If you want to enable directory sync, set the Enable phone directory sync for all new customer organizations toggle to On.

This option enables Webex to read BroadWorks contacts into the customer organization, so that users can find and call them from the Webex app.

Enter a Partner Admin .

This name is used in the automated email message from Webex, that invites users to validate their email addresses.

Make sure the Allow admin-invite emails when attaching to existing orgs toggle is On (the default setting is On).

Click Next .

Review your entries on the final screen. You can click the navigation controls at the top of the wizard to go back and change any details. Click Create .

You should see a success message.

Click View Templates and you should see your new template listed with any other templates.

Click the template name to modify or delete the template, if necessary.

You do not need to re-enter the provisioning account details. The empty password/password confirm fields are there to change the credentials if you need to, but leave them empty to keep the values you gave to the wizard.

Add more templates if you have different shared configurations you want to provide to customers.

Keep the View Templates page open, as you may need template details for a following task.

### Configure Application Server with Provisioning Service URL

This task is only required for flow through provisioning.

#### Patch Application Server (R22, R23, and R24 only)

If you haven't yet done so, apply the following patch that applies to your release:.

For R22: AP.as.22.0.1123.ap373197

For R23: AP.as.23.0.1075.ap373197

For R24: AP.as.24.0.944.ap384177

For a complete list of BroadWorks patches that form the requirement for deploying Webex for Cisco BroadWorks, See BroadWorks Software Requirements in the Reference section.

Change to the Maintenance/ContainerOptions context.

Enable the provisioning URL parameter:

/AS_CLI/Maintenance/ContainerOptions> add provisioning bw.imp.useProvisioningUrl true

#### Get the Provisioning URL(s) from Partner Hub

Refer to the Cisco BroadWorks Application Server Command Line Interface Administration Guide for details (Interface > Messaging and Service > Integrated IM&P) of the AS commands.

Sign in to Partner Hub and go to Customers > Onboarding templates .

Click View Templates .

Select the template you’re using to provision this enterprise/group’s subscribers in Webex.

The template details display in a flyout pane on the right. If you haven’t yet created a template, you need to do that before you can get the provisioning URL.

Copy the Provisioning Adapter URL .

Repeat this for other templates if you have more than one.

#### (Option) Configure System-Wide Provisioning Parameters on Application Server

You may not want to set system-wide provisioning and service domain if you are using UC-One SaaS. See Decision Points in the Prepare your Environment section.

Sign in to the Application Server and configure the messaging interface.

AS_CLI/Interface/Messaging> set provisioningUrl provisioningURL

AS_CLI/Interface/Messaging> set provisioningUserId provisioning_account_name

AS_CLI/Interface/Messaging> set provisioningPassword provisioning_account_password

AS_CLI/Interface/Messaging> set enableSynchronization true

Activate the Integrated IMP interface:

/AS_CLI/Service/IntegratedIMP> set serviceDomain example.com

/AS_CLI/Service/IntegratedIMP/DefaultAttribute> set userAttrIsActive true

You must enter the fully qualified name for the provisioningURL parameter, as it was given in Control Hub. If your Application Server cannot access DNS to resolve the hostname, then you must create the mapping in the /etc/hosts file on the AS.

#### (Option) Configure Per-Enterprise Provisioning Parameters on Application Server

In BroadWorks UI, open the enterprise you want to configure, and go to Services > Integrated IM&P .

Select Use service domain and enter a dummy value (Webex ignores this parameter. You could use example.com ).

Select Use Messaging Server .

In the URL field, paste the provisioning URL you copied from your template in Partner Hub.

You must enter the fully qualified name for the provisioningURL parameter, as it was given in Partner Hub. If your Application Server cannot access DNS to resolve the hostname, then you must create the mapping in the /etc/hosts file on the AS.

In the Username field, enter a name for the provisioning administrator. This must match the value on the template in Partner Hub.

Enter a password for the provisioning administrator. This must match the value on the template in Partner Hub.

For Default User Identity for IM&P ID , select Primary .

Click Apply .

Repeat for other enterprises you want to configure for flow through provisioning.

#### User Provisioning Data

For information on the user data that gets exchanged between BroadWorks and Webex during user provisioning, see Service Provider User Provisioning .

### Pre-provisioning check API

The pre-provisioning check API helps partners and sales teams identify potential
                errors or conflicts before provisioning a customer or subscriber (user) for a
                package. Only users or integrations authorized by a user with the partner full
                administrator role can access this API.

The API performs several validation checks, such as:

Whether the subscriber is already assigned to another customer or
                            partner.

If the email address is already in use by another subscriber.

Conflicts between the requested provisioning parameters and existing
                            Webex records.

This helps you catch and fix problems early, so the provisioning goes smoothly
                without unexpected errors.

For more information on precheck customer provisioning and precheck subscriber
                provisioning, see developer.webex.com portal.

### Configure partner SSO with OpenID Connect (OIDC) (Recommended)

Partner administrators can configure OIDC SSO for newly created customer
                organizations. They can configure a single predefined SSO relationship and apply
                that configuration to the customer organizations they manage, and to their own
                employees.

The following partner SSO OIDC steps apply to newly created customer
                    organizations only. If partner administrators try to modify the default
                    authentication type to partner SSO OIDC in an existing template, the changes
                    don't apply to the customer organizations already onboarded using the
                    template.

Open a service request with Cisco TAC with the details of the OpenID Connect
                        IDP.

The following table shows the mandatory and optional IDP attributes. TAC set
                        up the IDP on the CI and provide you with the redirect URI to be configured
                        on the IDP.

Attribute

Required

Description

IDP Name

Yes

Unique, case-insensitive name. It can include letters,
                                            numbers, hyphens, underscores, tildes, and dots. Max
                                            length: 128 characters.

OAuth client Id

Yes

Used to request OIDC IdP authentication.

OAuth client Secret

Yes

Used to request OIDC IdP authentication.

List of scopes

Yes

Used to request OIDC IdP authentication. Space-separated
                                            list of scopes (for example, openid email profile) must
                                            include openid and email.

Authorization Endpoint

Yes if discoveryEndpoint isn’t provided

URL of the IdP's OAuth 2.0 authorization endpoint.

tokenEndpoint

Yes if discoveryEndpoint isn’t provided

URL of the IdP's OAuth 2.0 token endpoint.

Discovery Endpoint

No

URL of the IdP's discovery endpoint for OpenID endpoints
                                            discovery.

userInfoEndpoint

No

URL of the IdP's UserInfo endpoint.

Key Set Endpoint

No

URL of the IdP's JSON web key set endpoint.

In addition to the above IDP attributes, you need to specify a partner
                            organization ID in the TAC request.

Configure the redirect URI on the OpenID connect IDP.

Configure an onboarding template.

For the Authentication Mode setting, select Partner authentication with OpenID Connect

For OpenID Connect IDP Entity ID , enter the IDP name
                        provided during the IDP setup.

Once you've completed the configuration, you can manually verify that the Partner IdP
                Entity ID is set up correctly.

Onboard a customer that uses the template and create a new user in the
                            customer organization.

Very that the user can sign in using the SSO authentication flow.

### Configure partner SSO with SAML

Partner administrators can configure SAML SSO for newly created customer organizations.
        They can configure a single predefined SSO relationship and apply that configuration to the
        customer organizations they manage, and to their own employees.

The following partner SSO steps apply to newly created customer organizations only. If
          partner administrators try to add Partner SSO to an existing customer organization, the
          system retains the existing authentication method to prevent existing users from losing
          access.

Verify that the third-party Identity Provider (IdP) meets the requirements listed in
          the Requirements for Identity Providers section of Single Sign-On Integration in Control Hub .

Open a service request with Cisco TAC. TAC must establish a trust relationship between
          the third-party IdP and Cisco Common Identity service.

If your IdP requires enabling the passEmailInRequest feature, make sure to include this requirement
                in the service request. Check with your IdP if you’re unsure of whether this feature
                is required.

Upload the CI metadata file that TAC provided to your IdP.

Configure an onboarding template:

For the Authentication Mode setting, select Partner Authentication .

Enter the IDP Entity ID . You can find the EntityID from the
                SAML metadata XML of the third-party IdP.

Once you've completed the configuration, you can manually verify that the Partner IdP
        Entity ID is set up correctly.

Onboard a customer that uses the template and create a new user in the customer
              organization.

Verify that the user can sign in.

User sign-in should redirect to the partner IdP sign-in page, and the user must be
              able to sign in successfully with valid credentials.

#### Activate BroadWorks IdP in Control Hub

Once you've completed the configuration and verified that the partner IdP is set up
        correctly, you can activate it in Control Hub.

Before you begin

Configure and verify the partner IdP for single
        sign-on integration.

Sign in to Control Hub .

Go to Security > Authentication > Activate SSO .

Select Broadworks and click Activate .

The IdP appears in the Identity provider tab.

### Enable Call Correlation Identifier

To run Webex for Cisco BroadWorks, it's required that you enable the Call Correlation Identifier. This setting is required for many calling features, including Call Recording, Group Call Pickup, Executive and Executive-Assistant.

Use the CLI to enable the feature on all AS and XSP|ADP interfaces.

Run the following commands on AS interfaces. This will enable the AS to send the X-BroadWorks-Correlation-Info SIP header:

AS_CLI/Interface/SIP> set sendCallCorrelationIDNetwork true

AS_CLI/Interface/SIP> set sendCallCorrelationIDAccess true

The enableCallCorrelationID parameter associated with the Xsi-Actions
						application is used to control the inclusion of call correlation information
						in Xsi-Actions logs. It is recommended to have enableCallCorrelationID enabled using the following
						command on XSP|ADP interfaces:

XSP|ADP_CLI/Applications/Xsi-Actions/GeneralSettings>set enableCallCorrelationID
							true

For additional information on the Call Correlation Identifier, see Cisco BroadWorks Call Correlation Identifier Feature Description .

### Directory Sync

Directory sync ensures that Webex for Cisco BroadWorks users can use the Webex directory to call any calling entity from the BroadWorks server. When this feature is enabled, the full calling directory from the BroadWorks server gets synced to the Webex directory. Users can access the directory from the Webex App and place a call to any calling entity from the BroadWorks server.

To turn Directory Sync on, go to Directory Sync in Webex for Cisco BroadWorks .

Webex for Cisco BroadWorks flowthrough provisioning adds messaging users and associated calling information from the BroadWorks server to the Webex platform. However, phone lists, non-messaging users, and non-user entities are not included (for example, a conference room phone, fax machine or hunt group number). Turning on Directory sync ensures that all calling entities get added to the Webex platform.

### Unified Call History

When Unified Call History is enabled, BroadWorks call events sync to the Webex cloud and become part of the Webex Unified Call and Meetings History that displays on the Webex App. Users can view their own detailed Call history and Meeting history from the Webex App.

Unified Call History can be enabled by partner-level administrators in Partner Hub on a cluster-by-cluster basis. When this feature is turned on, the BroadWorks deployment syncs the following call events to the Webex cloud:

Call History events—these events get used to build a detailed Unified Call History

Hook Status events—Unified Call History includes hook status optimizations that decrease the amount of network bandwidth for Telephony Presence updates

#### Unified Call History Requirements

Before configuring Unified Call History, make sure that you’ve patched your system. This
				feature depends on the following BroadWorks patches being installed. If your system
				is on a Release Independent (RI) version, the requirements are already included.

For R22:

AP.xsp.22.0.1123.ap378585

AP.as.22.0.1123.ap378585 —after patch installation, you must activate feature 25433. For example: AS_CLI/System/ActivatableFeature> activate 25433

AP.platform.22.0.1123.ap378585

AP.ps.22.0.1123.ap378585

For R23:

AP.as.23.0.1075.ap378585 —after patch installation, you must activate feature 25433. For example: AS_CLI/System/ActivatableFeature> activate 25433

AP.platform.23.0.1075.ap378585

If using XSP— AP.xsp.23.0.1075.ap378585

If using ADP— Xsi-Events-23_2021.05_1.251.bwar

For R24:

AP.as.24.0.944.ap378585 —after patch installation, you must activate feature 25433. For example: AS_CLI/System/ActivatableFeature> activate 25433

Xsi-Events-24_2021.05_1.251.bwar

For the full list of BroadWorks patches that you must install as a prerequisite to running Webex for Cisco BroadWorks, see BroadWorks Software Requirements .

In addition to patching your system, the client config file ( config-wxt.xml ) must have the following tag set: <call-history enable-unified-history=”%ENABLE_UNIFIED_CALL_HISTORY_WXT%”/>

To have Hunt Group, Call Center and other redirection info in Unified Call History, the
				following BroadWorks patches must be installed and active:

For R23:

AP.as.23.0.1075.ap383346

AP.as.23.0.1075.ap383994

For R24:

AP.as.24.0.944.ap383346

AP.as.24.0.944.ap383994

To have Executive-Assistant info in Unified Call History, the following BroadWorks patches
				must be installed and active:

For R24:

AP.as.24.0.944.ap380052

AP.as.24.0.944.ap384239

ADP running Xsi-Events-24_2022.06 or later

In addition to the BroadWorks patches, Directory Sync must also be enabled for the
				Executive-Assistant Unified Call History.

When you enable Call History or DND Sync, Webex sends CTI subscription refresh requests for
					all users under the cluster. Depending on the number of users, this may last up
					to a few hours. It’s recommended to not perform any BroadWorks maintenance
					activity during the same maintenance window.

#### Enable Call History (New Cluster)

To enable Call History on a new cluster, see the steps for adding a cluster in Configure Your Partner Organization in Partner Hub .

#### Enable Call History (Existing Cluster)

To enable Call History on an existing cluster, follow the below steps:

Sign in to Partner Hub at admin.webex.com .

Go to Services .

Click View Broadworks Calling and select the appropriate BroadWorks cluster.

Verify the cluster connection is good. The right panel should display a green check mark with Connection established .

If this doesn't appear, under Check Connnections (Optional) , enter BroadWorks User Id and BroadWorks Password and click Check to verify the connection is good.

Check the Enable call history check box.

Click Save .

#### Feature Interactions

The following feature interactions exist for Unified Call History:

Unified Call History isn’t supported for users who are configured in BroadWorks with Route
						Lists or Direct Routes. When this situation exists, Call History and Hook
						Status events don’t get sent to the Webex App.

Unified Call History isn’t supported with extension dialing. Calls that are placed using
						extension dialing may not be reflected correctly in the Call History.

#### View Call History on Webex App

End users can access and view their Unified Call History from the Webex App. For details, see: Webex | View Call and Meeting History .

#### Disable Unified Call History

Once you enable Unified Call History on a cluster, you can’t disable the feature on your own.
				If you need to disable the feature, contact Cisco
					Technical Assistance Center (TAC) .

#### Visual Spam Indication

The Webex App supports a visual indication of spam calls in the call toast when the call is
				presented to the callee and in the Unified Call History records when BroadWorks is
				updated to perform Caller ID validation through the STIR/SHAKEN framework. To have
				this feature:

- Enable Unified Call History as described in the previous section.

- AP.as.23.0.1075.ap384591 / AP.as.24.0.944.ap384591

- or AS-25_Rel_2022.12 at a minimum

- AS_CLI/System/ActivatableFeature> activate 104112

- AS_CLI/System/StirShaken> set enableVerification true

- BroadWorks must be configured to perform STIR-SHAKEN signing, tagging, and verification as
					described in Cisco BroadWorks STIR-SHAKEN Signing Tagging
						and Verification

When BroadWorks is properly configured, a new header X-Cisco-CallerId-Disposition will be
				added in INVITE requests sent to Cisco clients and a new field callerIdDisposition
				will be added to the existing Call History Events that are sent to Webex Cloud
				through the CTI interface. Webex devices use this information to provide a visual
				spam indication in the call presentation and the Unified Call History of the
				callee.

### Personal Assistant Status Sync

The Personal Assistant (PA) Status Sync feature synchronizes the personal assistant presence status between the BroadWorks Calling devices and the Webex App.

The PA service provides the user an option to inform the callers the reason the called party isn't available, optionally providing information on when the called party returns and whether there's an attendant to handle the call. PA feature enables users in the Webex Apps to see the user’s Away presence along with the PA status and the duration configured.

#### Prerequisites

Make sure that the following patches are applied to the AS and XSP|ADP. Apply only the
        patches for your BroadWorks version.

Patch for RI and Release 24:

AP.as.24.0.944.ap385558

XSI Event Package for Personal Assistant Status Synchronization feature introduces a new PersonalAssistantSync event package to allow XSI clients to synchronize with Cisco BroadWorks Personal Assistant presence changes. For more information, see XSI Event Package for Personal Assistant Status Synchronization Feature .

In addition to patching your system, the client config file (config-wxt.xml) must have the following tag set: <personal-assistant enabled="%PERSONAL_ASSISTANT_ENABLED_WXT%"/>

#### Enable Personal Assistant Status Sync (New Cluster)

To enable Personal Assistant Status Sync on a new cluster, see the steps for adding a
        cluster in Configure Your Partner Organization in Partner
        Hub .

If there are more than 50 customers in a BroadWorks cluster, operations such as updating XSI Actions, XSI Events, DAS URL, XSP|ADP URL, Personal Assistant or DND sync are not supported. In such instances, it is recommended to contact a Cisco TAC support engineer for assistance to get this enabled.

#### Enable Personal Assistant Status Sync (Existing cluster)

Sign in to Partner Hub with your partner admin credentials at https://admin.webex.com .

Click Services .

Click View Broadworks Calling and select the appropriate BroadWorks cluster.

- Under CTI Interface section, enable the Personal Assistant Status Sync toggle.

Enter your BroadWorks user ID and click Enable .

The system validates that the BroadWorks cluster has the appropriate patches to support PA Sync. If validation fails, the Save button is disabled.

If validation succeeds, click Save .

Enabling PA Status Sync is a one-way toggle. Once the feature is enabled, you can’t disable it on your own.

#### Disable Personal Assistant Status Sync

Once you enable PA Sync status on any of the BroadWorks clusters, you can’t disable this
        feature on your own. If you need to disable, contact Cisco Technical
          Assistance Center (TAC) .

### Caller Identification and Call Redirection

Caller Identification

When the Webex App receives a call, it will attempt to identify who the caller is and display this information in the incoming call notification, the in-call window, and after the call is complete, in the call history and voicemail.

The Webex App will attempt to find the caller ID by matching the incoming phone number with the phone numbers of contacts found in various sources. The Webex App will use the following sources in this order. Once it finds it in one source it will not attempt to search anywhere else.

If it finds multiple instances of a number in one source, it will not try to choose one of them, in this case, it will not display any caller ID.

Webex Common Identity (CI) which contains your organization users.

Personal and Organization Contacts. Personal Contacts are visible under the Contacts tab.

Local Address Book. In Windows - Outlook application, in Mac - Mac Contacts, in iOS - iPhone contacts, in Android - Android contacts.

If there is no match found with the incoming phone number, then the app will use the display name in the SIP FROM header if available. Otherwise, it will use the username part of the SIP URI from the SIP From header as a last resort.

For remote call control (i.e., Deskphone Control Mode) XSI info is used, where BWKS ID or extension is used, extracted from remote-party-info in the XSI event. If remote-party-info is not available, then P-Asserted Identity (PAI) (if configured) will be used.

Call Redirection

In the case where a call has been redirected or forwarded, then the app will attempt to show who the caller is and how it was forwarded in the call notification and call history.

Call Forwarded: Shows number that forwarded the call.

Hunt Group: Shows name of the hunt group that forwarded the call.

Call Center Queue: Shows name of the queue that forwarded the call.

Executive-Assistant: Shows name of Executive the call is coming in for.

Exceptions:

For internal call queue calls, where an agent calls back an internal party, the remote party will not see the name of the call queue but will see the name of the agent calling them.

Call Answered Elsewhere:

For Hunt Groups or Call Queues that are set up with simultaneous routing, agents will see a call answered elsewhere in call history if another agent picks up the call. For Hunt Groups or Call Queues with sequential routing, or in an overflow, calls will show as missed call in call history if answered by another agent.

### Select Caller ID

#### Overview

The "Select Caller ID" feature enables users to switch between different Calling Line IDs for external calls. If enabled by the admin, users can choose from the following options for their Calling Line Identity:

User number ("Use user phone number for Calling Line Identity")

Configurable CLID ("Use configurable CLID for Calling Line Identity")

Group CLID ("Use group/department phone number for Calling Line Identity")

#### Functionality

Users have two methods to change their Caller ID as provisioned by the administrator:

Feature Access Codes (FAC) : Specific codes for each of the three Caller ID options.

Webex App Interface : A user-friendly view within the Webex desktop and mobile apps that display the available Caller ID options enabled by the administrator, allowing users to select their preferred ID.

#### Additional Features

The Webex apps will also include options for Call Center queues DNIS.

Mobile app users will have Dual Persona options available for Mobility users.

#### Preconditions

The following conditions must be met on the BroadWorks server for the user to be able to control their choice of external CLID policy:

To enable the system flag 'EnableUserSelectionOfExternalCLIDPolicy'

Run the CLI command:

AS_CLI/SubscriberMgmt/Policy/CallProcessing/CallingLineId> set defaultEnableUserSelectionOfCLIDPolicy true .

To enable 'EnableUserConfigurableCLIDModification'

Run the CLI command:

AS_CLI/SubscriberMgmt/Policy/CallProcessing/CallingLineId> set defaultEnableUserConfigurableCLIDModification true .

This enables Allow User Selection of External CLID Policy and Allow User Configurable CLID Modification .

User level Call Processing Policy Calling Line ID scope is set to "Use User Calling Line Id Policy" for this user.

The User level Call Processing Policies flag 'Allow User Selection of External CLID Policy' is enabled for the user.

If no number is defined for the "Use configurable CLID for Calling Line Identity" or "Use group/department phone number for Calling Line Identity" options, the FACs or app display will have no effect. This setting must be configured by the administrator prior to user selection.

For more information see, User Selection of External Calling Line ID Option feature description guide.

#### BroadWorks Patches

This feature requires two specific BroadWorks patches to function correctly:

Refer to Section 8 Release Independent and Service Patch Information.

BWKS-5230 was the original user-selectable CLID feature - it lets users (if the system is configured properly) change which CLID policy is applicable. See FD here: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/broadworks/FD/AS/UserSelectionOfExternalCallingLineIDOptionFD-R250.pdf

BWKS-9510 is an XSI enhancement requested by the Webex client team to make it easier to discover which options are available for a user. This is necessary because the choice of CLID policy isn't a simple user-level feature (like CFA) that is directly controllable. Rather it depends on various system configuration options and the "call processing policies" hierarchy. You can see details here: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/broadworks/FD/AS/XSIEnhancementToSupportUserSelectableCLIDFD-R250.pdf

#### Webex App Configuration

These tag needs to be enabled in the desktop, tablet, and mobile configurations:

```
<config>
<services>
<calls>
<caller-id>
<outgoing-calls enabled="%ENABLE_CLID_OUTGOING_CALLS_WXT%">
```

### Shared line appearance

Shared line appearance is the ability to provision other users' lines as shared lines on the end-user device. The shared line configuration for the Webex App is similar to the shared line configuration for desk phones. This specific feature allows you to assign shared line appearances to the end user's Webex App.

This feature benefits the users to handle calls on other user's extension directly from the Webex App.

You can configure shared line appearance only for the desktop version of a Webex App.

You can add a maximum of 10 lines including the primary line to Webex App.

You can't assign workspace line as shared line.

A user cannot be provisioned with Executive-Assistant service at the same time as having Shared Lines.

A user's primary line port should not be changed to a Shared Line.

Requirements

To deploy this feature on Webex for Cisco BroadWorks, you must deploy the following BroadWorks patches:

Patch 1: Owner Flag in Device List to Support Webex Client Shared Lines

R23 without ADP:

AP.as.23.0.1075.ap384179

AP.xsp.23.0.1075.ap384179

R23 with ADP:

AP.as.23.0.1075.ap384179

Xsi-Actions-23_2022.10

R24:

AS: AP.as.24.0.944.ap384179

Xsi-Actions-24_2022.10

R25:

AS: RI release Rel_2022.10_1.310

Xsi-Actions-25_2022.10

Patch 2: Patches for increasing port count on device profile types. Example: For the desktop client: System>Identity/Device Profile Type Modify> Business Communicator - PC: Profile , Standard Options, Number of Ports:

- IF 'Unlimited' is enabled, no change is required

- IF 'Limited To' is <10, change the value = 10 and save to utilize all available lines

RI release Rel_2022.10_1.310

For details on client configuration, see section 6.1.44 'Primary Profile' from the Webex for Cisco BroadWorks Configuration
                    Guide .

### Do Not Disturb (DND) Sync

Do Not Disturb (DND) Sync aligns DND settings between Webex and BroadWorks by
                synchronizing DND status between the two platforms. For example, if a user turns on
                DND from the Webex App, that status syncs to BroadWorks calling devices. As a
                result, the user’s BroadWorks-registered desk phone doesn’t ring when someone
                attempts to call it. Similarly, if a user sets DND from a desk phone, the status
                syncs to the Webex App. Without this feature, DND updates from one platform don't
                get recognized by the other platform.

DND Sync gets applied at the BroadWorks cluster level and can be enabled in Partner Hub by a partner administrator.

If there are more than 50 organizations/customers in the BroadWorks cluster, DND sync isn't supported on the cluster. In such cases, you must open a Cisco TAC support ticket to enable DND sync.

#### Prerequisites

Make sure that the following patches are applied to the AS and XSP|ADP. Apply only the patches for your BroadWorks version.

For Release 23:

<snipped>

- ADP apps: Xsi-Actions-23_2022.03_1.220.bwar, Xsi-Events-23_2022.03_1.220.bwar

For Release 24:

<snipped>

- ADP apps: Xsi-Actions-24_2022.03_1.220.bwar, Xsi-Events-24_2022.03_1.220.bwar

After you apply the patches, activate feature 25433 on the AS:

AS_CLI/System/ActivatableFeature> activate 25433

Configure Device Feature Key Synchronization on BroadWorks. Make sure that the phone supports SIP SUBSCRIBE/NOTIFY for the “as-feature-event” event package. For details, see Cisco BroadWorks Device Feature Key Synchronization .

#### Enable DND Sync (Existing cluster)

Sign in to Partner Hub

Click Services .

Click View Broadworks Calling and select the appropriate BroadWorks cluster.

Enable the Do not disturb (DND) sync toggle.

Enter your BroadWorks user ID and click Enable .

The system validates that the BroadWorks cluster has the appropriate patches to support DND Sync. If validation fails, the Save button gets disabled.

If validation succeeds, click Save .

Once DND Sync gets enabled, Webex refreshes all user subscriptions to include the Do not disturb event package. Depending on the number of users, this process may take a few hours to complete.

Enabling DND Sync is a one-way toggle. Once the feature is enabled, you can’t disable it on your own.

#### Enable DND Sync (New cluster)

You can also enable the feature during cluster creation. For details, see “Configure Your BroadWorks Clusters” in Configure Your Partner Organization in Partner Hub .

#### Quiet Hours

In Webex for BroadWorks deployments, the 'Quiet Hours' feature relies on the 'Do Not Disturb (DND) Sync' functionality to ensure that the quiet hours settings are synchronized across all devices. To properly synchronize quiet hours across desktop and mobile devices, ensure that 'DND Sync' is enabled on the user's account.

#### Disable DND Sync

You can’t disable DND sync on your own. To disable the DND feature, create a TAC case
                with the title "Disable Do Not Disturb Sync" and provide partnerId and BroadWorks cluster name .

#### Use Cases

### Call Recording

Webex for Cisco BroadWorks supports four modes of call recording.

Recording Modes

Description

Controls/Indicators that display on the Webex App

Always

Recording is initiated automatically when the call is established. The user has no ability to start or stop recording.

Visual indicator that recording is in progress

Always with Pause/Resume

Recording is initiated automatically when the call is established. The user can pause and
									resume recording.

Visual indicator that recording is in progress

Pause Recording button

Resume Recording button

OnDemand

Recording is initiated automatically when call is established, but the recording is deleted unless the user presses Start Recording .

If the user starts recording, the full recording from the call setup is retained. After
									starting the recording, the user can also pause and resume
									recording

Start Recording button

Pause Recording button

Resume Recording button

OnDemand with User-Initiated Start

Recording doesn’t initiate unless the user selects the Start
										Recording option on the Webex App. The user has
									the option to start and stop recording multiple times during a
									call.

Start Recording button

Stop Recording button

Pause Recording button

#### Requirements

To deploy this feature on Webex for Cisco BroadWorks, you must deploy the following BroadWorks patches. If your system is on a Release
				Independent (RI) version, the requirements are already included.

For R22: AP.as.22.0.1123.ap377718

For R23: AP.as.23.0.1075.ap377718

For R24: AP.as.24.0.944.ap377718

The Call Correlation Identifier must be turned on. For details, see Enable Call Correlation Identifier .

The following configuration tag must be enabled in order to use this feature: %ENABLE_CALL_RECORDING_WXT% .

This feature requires an integration with a third-party call recording platform.

To configure call recording on BroadWorks, go to the Cisco BroadWorks Call Recording Interface Guide .

#### Additional Information

For user information on how to use the Recording feature, see Webex |
					Record Your Calls .

To replay a recording, users or administrators must go to their third-party call recording platform.

### Enabling Voicemail for Microsoft Teams Integration

You can enable voicemail for Microsoft Teams users in the Webex for BroadWorks solution. This integration allows users to retrieve their voicemails directly through Microsoft Teams, enhancing the overall user experience.

#### Steps to Enable Voicemail

To enable Voicemail for BroadWorks, you need to enable the toggle broadworks-voicemail-enabled-spark-541886: true at the organization level.

To enable this feature, contact Cisco Technical Assistance Center (TAC) .

#### User Experience

Once the integration is set up, users can:

- Retrieve voicemails directly within the Microsoft Teams application.

- Receive notifications for new voicemails.

- Manage voicemail settings from the Webex interface.

#### Requirements

To support voicemail retrieval in the Microsoft Teams integration with the Webex for BroadWorks offer, additional network changes are required. BroadWorks partners should enable Cross-Origin Resource Sharing (CORS) for the following URLs on their BroadWorks platform:

https://jabber-integration-a.wbx2.com

https://jabber-integration-r.wbx2.com

https://jabber-integration-k.wbx2.com

https://msteams-calling.webex.com

Ensure that the BroadWorks Voicemail is configured according to the settings outlined in Voicemail Playback .

For more details on the configuration steps, refer to section 8.5.1.2 of the BW Application Delivery Platform Configuration Guide ,
        which requires version 2024.05 on the ADP.

### Group Call Park and Retrieve

Webex for Cisco BroadWorks supports Group Call Park and Retrieve. This feature provides a way for users within a group to park calls, which can then be retrieved by other users in the group. For example, retail employees in a store setting could use the feature to park a call that can then be picked up by someone in another department.

#### Feature Operation

Once the feature is configured

While in a call, a user clicks the Park option on their Webex app to park the call at an extension that the system selects automatically. The system displays the extension to the user for a period of 10 seconds.

Another user in the group clicks the Retrieve call option on their Webex app. The user then enters the extension of the parked call in order to continue the call.

#### Requirements

For this feature to work, make sure of the following:

The client config file must have the following tags set:

```
<call-park enabled="%ENABLE_CALL_PARK_WXT%"
        timer="%CALL_PARK_AUTO_CLOSE_DIALOG_TIMER_WXT%"/>
```

The Call Correlation Identifier must be enabled on the AS and XSP|ADP. For details, see Enable Call Correlation Identifier .

Your SBC must be configured to pass the ‘ x-broadworks-correlation-in ' SIP attribute to and from the Application Server.

#### Configuration

For information on how to configure Group Call Park on BroadWorks, see “Add Call Park Group” in the Cisco BroadWorks Application Server Group Web Interface Administration Guide – Part 2 . You must create a group and add users to the group.

For information on how to configure the Call Correlation Identifier on BroadWorks, see Cisco BroadWorks Call Correlation Identifier Feature Description .

#### Additional Information

For user information on how to use Group Call Park, see Webex | Park and Retrieve Calls .

#### Call Park/Directed Call Park

Regular or directed call park is not supported in the Webex app UI, but provisioned users can deploy the feature using Feature Access Codes:

Enter *68 to park a call

Enter *88 to retrieve a call

### Barge-in

Barge-in service is commonly used in call center environments or other situations where immediate assistance or intervention may be required.

When a barge-in service is enabled, a designated user or supervisor can enter an active call by initiating a specific command or by using a dedicated button or key combination on their phone or communication device. Once the barge-in request is made, the system establishes a connection with the ongoing call, allowing the authorized person to listen to the conversation or join the call as an active participant.

Barge-in service can be useful in various scenarios. In a call center setting, supervisors or trainers can monitor and coach customer service representatives by listening to their calls in real-time. If necessary, they can intervene to provide guidance or take over the call if the representative is struggling. In emergency situations or critical discussions, authorized personnel can quickly join ongoing conversations to provide assistance or make important decisions.

In the Webex app for Barge in, we get a notification that the call is transformed into a conference. There is no additional information in the NOTIFY (call-info or conference-info) what is the type of conference, so we can treat it in a different way.

When a barge-in occurs, a three-way call is established between the parties. The following terms are introduced:

Supervisor : A supervisor is a person who oversees and manages a team of customer service agents or call center representatives. In the context of call barge-in, a supervisor typically has the ability to monitor and intervene in ongoing customer calls. They may use call monitoring tools or software to listen in on calls, provide guidance to agents, and ensure quality control. The supervisor's role may involve training agents, addressing customer concerns, and optimizing the performance of the team.

Customer : A customer refers to an individual or entity that engages with a company or organization to obtain products, services, or support. In the context of call barge-in, a customer is someone who is making or receiving a phone call with a customer service agent. Customers may seek assistance, information, or resolution to their queries or issues during the call. The call barge-in feature allows supervisors or authorized personnel to join the ongoing call between the customer and the agent.

Agent : An agent, also known as a customer service representative or call center agent, is a person responsible for handling customer interactions and providing support or assistance over the phone or other communication channels. Agents are trained to address customer inquiries, resolve problems, process transactions, and deliver a positive customer experience. In the context of call barge-in, an agent is the individual speaking directly to the customer during the phone call. The agent may receive guidance or feedback from the supervisor through call barge-in if necessary.

For any client initiated requests such as CallStartRequest, CallPickupRequest, DirectedCallPickupRequest, DirectedCallPickupWithBargeInRequest, etc, if <Webex Client> (please choose the right name instead of Webex client, if it is not appropriate) is provisioned as a Shared Call Appearance device, 'Alert all appearances for Click-to-Dial calls' configuration should be enabled on Shared Call Appearance setting for the client to receive a call, unless the location is explicitly provided by the client initiating the request.

### SIP call transfer to Webex Meeting

The SIP call transfer to Webex Meeting comes with two unique features:

New Push Notification (Mobile)

Users on a native call can now switch to the Webex App by tapping on the New push notification. When you start a native call screen a new push notification appears on the screen and tapping the notification takes you straight to the Webex App in-call screen.

You see the Webex notification during a mobile phone call if you use Webex Go or your mobile network operator (MNO) has call signaling using Cisco call control for your mobile phone calls.

Move Call to Meeting

When you're in the middle of a call with someone, you may want to move that call into a meeting to make use of some advanced meetings features like video, share, or whiteboarding. Or invite other people into the discussion and move to a meeting.

#### BroadWorks requirements

Activatable feature 25239

R23 with XSP|ADP:

AS Patch AP.as.23.0.1075.ap383064

XSP|ADP Patch AP.xsp.23.0.1075.ap383064

Patch AP.platform.23.0.1075.ap383064

R23 with ADP:

AS Patch AP.as.23.0.1075.ap383064

ADP with Xsi-Actions-23, CommPilot-23 version > 2022.05_1.303 and NPS version > 2022.08_1.350

R24:

AS patch: AP.as.24.0.944.ap383064

ADP with Xsi-Actions-24, CommPilot-24 version > 2022.05_1.303 and NPS version > 2022.08_1.350

R25:

AS RI release Rel_2022.08_1.354

ADP with Xsi-Actions-25, CommPilot-25 > 2022.08_1.350 and NPS version > 2022.08_1.350

#### Configure URI dialing

Enable BroadWorks to route a REFER‑generated SIP INVITE to a Webex meeting URI. Example: sip:<digits>+<meetingID>@<site>.webex.com .

Before you begin

This configuration enables routing only.

An internet‑facing SBC/CUBE is required for call completion.

- Configuration is required on Application Server (AS) and Network Server (NS).

Configure Application Server (AS).

Enable URL dialing (Mandatory): AS_CLI/System/CallP/DNS> set enableNameLookupForURLDialing true .

Verify: enableNameLookupForURLDialing = Y .

This configuration allows AS to process SIP URI calls and generate INVITEs after REFER.

Configure Network Server (NS).

Enable URL dialing policy: NS_CLI/Policy/UrlDialing> add DefaultInst true callTypes all .

Attach URL dialing policy to routing profile: NS_CLI/Policy/Profile> add routing UrlDialing DefaultInst .

This is required to avoid 404 Not Found (usrnf).

Enable SIP URI domain matching: NS_CLI/Policy/UrlDialing> set DefaultInst enableSipURIMatchingRules true .

Add routing rule for Webex domain: NS_CLI/Policy/UrlDialing/Rules> add DefaultInst *@<webex-site>.webex.com <RoutingNE_to_Internet_SBC> 1 99 .

Example: NS_CLI/Policy/UrlDialing/Rules> add DefaultInst *@digiceloffice-200.webex.com Internet_SBC 1 99

This routes Webex meeting INVITEs to the SBC.

Verify internet routing network element.

Routing NE must point to an internet‑facing SBC/CUBE. NS must not send SIP traffic directly to the internet.

Validate the route test: NS_CLI> vtri <calling-number> <meeting-URI>@<webex-site>.webex.com .

You can expect any one of the following results:

No 404 error

RoutingNE selected

Contact returned

#### Best practices, limitations and troubleshooting

##### Best practices

To ensure the Webex Cloud correctly identifies the Meeting ID and enterprise context, you must configure the CUBE to preserve the original Request-URI (R-URI).

Example configuration:

```
dial-peer voice 1000 voip
 description *** Webex Edge Deployment ***
 session protocol sipv2
 session target dns:<REGIONAL_SESSION_TARGET>
 voice-class sip requri-passing
 dtmf-relay rtp-nte
 codec g711ulaw
 no vad
```

The key functional elements are:

Voice-class sip requri-passing: This command is mandatory. It ensures that the original R-URI (containing the enterprise domain and meeting ID) is preserved in the outbound INVITE. Without this, the Webex Cloud can't associate the call with the correct meeting.

Regional Session Targets: The session target must point to the appropriate regional Webex Cloud ingress. This must be configured based on the customer’s geographic region. For example, EMEA: dns:ecccp.euro.pub.webex.com . Partners must verify the correct regional FQDN for their specific deployment cluster through the Control Hub.

In multi-tenant deployments, ensuring the R-URI remains unmodified is critical. If the R-URI is altered by the CUBE, the call fails to route to the intended meeting.

Partners are responsible for ensuring that their specific CUBE version and dial-peer logic don't conflict with this command. Always ensure that the enterprise domain and meeting context are correctly mapped within the Control Hub to match the traffic ingress.

##### Known limitations

Here are some known limitations:

BroadWorks AS has no direct internet access.

SBC/CUBE configuration is still required.

Desktop REFER escalation support is under validation.

##### Troubleshooting call failure

If the call fails, perform the following steps:

Capture AS XS logs.

Capture NS routing logs.

Verify SBC internet connectivity.

Share logs with Cisco TAC.

### E911 Emergency Calling

Webex for Cisco BroadWorks supports E911 emergency services calling. With this feature, emergency calls get routed to a Public Safety Answering Point (PSAP) who can then direct emergency services to the caller’s location. To use this feature, you must integrate Webex for Cisco BroadWorks with an E911 emergency call provider.

Use the following Webex articles to configure support for E911 emergency calling services:

E911 Emergency Calling in Webex for BroadWorks —Use this article to configure E911 emergency calling in Webex for Cisco BroadWorks using one of the following supported E911 providers:

Bandwidth

Intrado

RedSky

Emergency Call Disclaimer —If you have a location service, you can configure the Emergency Services Disclaimer window on the Webex App to include an option for users to update their location when logging in.

### Customize and provision clients

Users download and install their generic Webex App, for desktop or mobile (for download links, see Webex App Platforms ). Once the user authenticates, the
            client registers against the Webex Cloud for Messaging and Meetings, retrieves its
            branding info, discovers its BroadWorks service info, and downloads its calling
            configuration from BroadWorks Application Server (through DMS on XSP|ADP).

You configure the calling parameters for Webex App in BroadWorks (as normal). You configure branding, messaging, and meeting parameters
            for the clients in the Control Hub. You don’t directly modify a configuration file.

These two sets of configurations can overlap, in which case the Webex configuration supersedes the BroadWorks configuration.

#### Add Webex App configuration templates to BroadWorks Application Server

Webex App is configured with DTAF files. The clients download a configuration XML file from the
        Application Server, through the Device Management service on the XSP|ADP.

The R22.0 template files are no longer supported and are removed from the DTAF archive.
          The templates previously labeled R23.0 are renamed to R24.0, as BroadWorks R24.0 is the
          oldest version currently supported. These R24.0 templates are intended for use on all
          supported Application Server releases, including R24.0, R25.0, and R26.0.

Download the zip files of the desired Webex App (Desktop, Mobile, or Tablet) from Software Downloads site.

For details on Device Profile Type and Package name, see Device Profiles in the Prepare Your Environment section.

Check that you've the right tag sets in BroadWorks System > Resources > Device Management > Tag Sets .

Import and update DTAF Files.

The DTAF package downloaded from the Cisco Software Download site is a container
            archive. You must extract this archive locally to access the specific .DTAF.zip files required for import into the BroadWorks Application
            Server.

Locate the downloaded DTAF zip file (for example,
              ucone-mobile-ucaas-X.X.XX-wxt-MonthYear_DTAF.zip) and extract the contents to a local
              directory on your computer.

Navigate to the extracted folder. Locate the latest DTAF file for your client (for
              example, Business_Communicator_-_PC(R24.0).DTAF.zip).

Log in to the CommPilot interface as a system administrator and go to System > Resources > Identity/Device Profile Types > Import .

In the Device Type File Upload section, click Browse , select the .DTAF.zip
              file, and Click OK to import the file.

(Optional): If you're updating an existing device type, ensure the Device Type
                File Update check box is selected. This action overwrites existing templates
              with the latest configurations provided in the new DTAF.

Configure Device Profiles for each client you're provisioning.

Open the newly added device profile for editing.

Enter the XSP|ADP farm FQDN and Device Access Protocol.

Check the Support Remote Party Info check box. This support is required for desktop sharing to work and Remote party CLID to be presented in the Webex client.

You can also enable Remote Party support by running the following CLI command on the Application Server: AS_CLI/System/DeviceType/SIP> set <device_profile_type> supportRemotePartyInfo true .

Modify the templates according to your environment. For details, see the following
              table.

Save the profile.

Click Files and Authentication and then select the option to
          rebuild all system files.

Name

Description

Codec Priority

Configure priority order for the audio and video codecs for VoIP calls

TCP, UDP, and TLS

Configure the protocols used for SIP signaling and media

RTP Audio and Video Ports

Configure port ranges for RTP audio and video

SIP options

Configure various options related to SIP (SIP INFO, use rport, SIP proxy
                      discovery, refresh intervals for registration and subscription, and so on)

#### Customize branding for Webex App

Partner customizations—Partner administrators can apply advanced branding
            customizations that apply to the partner organization and/or customers that the partner
            manages. See Configure Advanced Branding Customizations .

Customer customizations—If the partner allows customers to apply their own Branding
            customizations, customer administrators can follow the procedures at Add Your Company Branding to
              Webex .

The User Activation Portal uses the same logo that you add for client Branding.

#### Customize problem reporting and help URLs

To customize these options, administrators can follow the procedure "Add Feedback and Help
        Site URLs", which can be found in both of the preceding branding articles.

### Configure Your Test Organization for Webex for Cisco BroadWorks

Before you begin

With Flowthrough Provisioning

You must configure all the XSP|ADP services, and the partner organization in Control
        Hub, before you can perform this task.

Assign Service in BroadWorks:

Create a test enterprise under your service provider enterprise in BroadWorks, or create a test group under your Service Provider (depends on your BroadWorks setup).

Configure the IM&P service for that enterprise, to point to the template you are testing (retrieve the provisioning adapter URL and credentials from Control Hub Onboarding template).

Create test subscribers in that enterprise / group.

Give the users unique email addresses in the email field in BroadWorks. Copy those into the Alternate ID attribute as well.

Assign the Integrated IM&P service to those subscribers.

This triggers the creation of the customer organization and the first users, which takes several minutes. Please wait a little while before trying to sign in with your new users.

Verify Customer Organization and Users in Control Hub:

Sign in to Control Hub with your partner administrator account.

Go to Customers and verify that your new customer organization is in the list (name follows the group name or enterprise name, from BroadWorks).

Open the customer organization and verify that the subscribers are users in that organization.

Verify that the first subscriber to whom you assigned the Integrated IM&P service has become the customer administrator of that organization.

### User Testing

Download the Webex app on two different machines.

Sign in as your test users on the two machines.

Make test calls.

| Service/Application | Authentication required | Service/application purpose |
|---|---|---|
| Xsi-Events | TLS (server authenticates itself to clients) | Call control, service notifications |
| Xsi-Actions | TLS (server authenticates itself to clients) | Call control, actions |
| Device management | TLS (server authenticates itself to clients) | Calling configuration download |
| Authentication Service | TLS (server authenticates itself to clients) | User authentication |
| Computer Telephony Integration | mTLS (client and server authenticate each other) | Telephony presence |
| Call Settings Webview application | TLS (server authenticates itself to clients) | Exposes user call settings in the selfcare portal within the Webex app |

| If CI Cluster is... | Set issuerName and issuerURL to... |
|---|---|
| US-A | https://idbroker.webex.com/idb |
| EU | https://idbroker-eu.webex.com/idb |
| US-B | https://idbroker-b-us.webex.com/idb |
| CA | https://idbroker-ca.webex.com/idb |
| SG | https://idbroker-sg.webex.com/idb |
| IN | https://idbroker-in.webex.com/idb |
| AE | https://idbroker-ae.webex.com/idb |
| AU | https://idbroker-au.webex.com/idb |
| If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. |

| If Teams Cluster is... | Set tokenInfoURL to...(IdP Proxy URL) |
|---|---|
| ACHM | https://broadworks-idp-proxy-a.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| AFRA | https://broadworks-idp-proxy-k.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| AORE | https://broadworks-idp-proxy-r.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| ADXB | https://broadworks-idp-proxy-d.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| ASYD | https://broadworks-idp-proxy-m.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| If you don't know your Teams Cluster , you can obtain the information from the Customer details in the Help Desk view of Control Hub. For testing, you can verify that the tokenInfoURL is valid by replacing the " idp/authenticate " portion of the URL with " ping ". |

| Specificity | CLI
                                    context |
|---|---|
| System
                                (global) | XSP\|ADP_CLI/System/SSLCommonSettings/JSSE/Ciphers> XSP\|ADP_CLI/System/SSLCommonSettings/JSSE/Protocols> |
| Transport
                                protocols for this system | XSP\|ADP_CLI/System/SSLCommonSettings/OpenSSL/Ciphers> XSP\|ADP_CLI/System/SSLCommonSettings/OpenSSL/Protocols> |
| HTTP on this
                                system | XSP\|ADP_CLI/Interface/Http/SSLCommonSettings/Ciphers> XSP\|ADP_CLI/Interface/Http/SSLCommonSettings/Protocols> |
| Specific HTTP
                                server interfaces on this system | XSP\|ADP_CLI/Interface/Http/HttpServer/SSLSettings/Ciphers> XSP\|ADP_CLI/Interface/Http/HttpServer/SSLSettings/Protocols> |

| Specificity | CLI Context |
|---|---|
| System (global) (R22 and later) | XSP\|ADP_CLI/System/SSLCommonSettings/JSSE/Ciphers> XSP\|ADP_CLI/System/SSLCommonSettings/JSSE/Protocols> |
| Transport protocols for this system (R22 and later) | XSP\|ADP_CLI/System/SSLCommonSettings/OpenSSL/Ciphers> XSP\|ADP_CLI/System/SSLCommonSettings/OpenSSL/Protocols> |
| All CTI interfaces on this system (R22 and later) | XSP\|ADP_CLI/Interface/CTI/SSLCommonSettings/Ciphers> XSP\|ADP_CLI/Interface/CTI/SSLCommonSettings/Protocols> |
| A specific CTI interface on this system (R22 and later) | XSP\|ADP_CLI/Interface/CTI/CTIServer/SSLSettings/Ciphers> XSP\|ADP_CLI/Interface/CTI/CTIServerSSLSettings/Protocols> |
|  |

| 1 | Install and configure a dedicated XSP (minimum version R22), or Application Delivery Platform (ADP). |
|---|---|
| 2 | Install the NPS Authentication Proxy patches: |
| 3 | Activate the Notification Push Server application. |
| 4 | (For Android notifications) Enable the FCM v1 API on the NPS. XSP_CLI/Applications/NotificationPushServer/FCM> set V1Enabled true |
| 5 | (For Apple iOS notifications) Enable HTTP/2 on the NPS. XSP_CLI/Applications/NotificationPushServer/APNS/GeneralSettings> set HTTP2Enabled true This is exclusive to Release 22 and earlier versions; it is not available in Release 23 and above versions, which only support HTTP/2. |
| 6 | Attach a techsupport from the NPS XSP/ADP. |
| 7 | On each AS server: Set the Push URL, Example: AS_CLI/System/NotificationPushServer> set url https://qaxsps.broadsoft.com/nps The namedefs file in /usr/local/broadworks/bw_base/conf must be configured with SRV and A records for Notification Push Server (XSP/ADP) lookup, if multiple XSP/ADP then add an entry for each as required. Example for multiple ADP/XSP: _pushnotification-client._tcp.qaxsps.broadsoft.com SRV 20 20 443 ADP1-qaxsps.broadsoft.com _pushnotification-client._tcp.qaxsps.broadsoft.com SRV 20 20 443 ADP2-qaxsps.broadsoft.com ADP1-qaxsps.broadsoft.com IN A 10.193.78.149 ADP2-qaxsps.broadsoft.com IN A 10.193.78.150 Once set, one of the following is required to pickup the changes: A restartbw be preformed in a maintenance window. Via the Cisco BroadWorks CLI: R24 and older AS_CLI/ASDiagnostic/DNS> reload R25 + AS_CLI/ASDiagnostic/DNS/ExecutionServer> reload AS_CLI/ASDiagnostic/DNS/ProvisioningServer> reload |

| 1 | Obtaining OAuth credentials for your Webex for Cisco
                    BroadWorks . |
|---|---|
| 2 | Create the client account on the NPS: XSP\|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> set clientId client-Id-From-Step1 XSP\|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> set clientSecret New Password: client-Secret-From-Step1 XSP\|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> set RefreshToken New Password: Refresh-Token-From-Step1 To verify the values you entered match with what you were given, run XSP\|ADP_CLI/Applications/NotificationPushServer/CiscoCI/Client> get The CiscoCI issuerUrl should ALWAYS be US CI cluster irrespective of your
                            location and the default should be: XSP\|ADP_CLI/Applications/NotificationPushServer/CiscoCI> get issuerUrl = https://idbroker.webex.com/idb |
| 3 | Enter the NPS Proxy URL, and set the token refresh interval (30 minutes recommended): Region-based FQDNs: US East: XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-a.wbx2.com/nps/ US West: XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-r.wbx2.com/nps/ Europe: XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-k.wbx2.com/nps/ XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set VOIPTokenRefreshInterval 1800 Saudi Arabia: XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-d.wbx2.com/nps/ Australia: XSP_CLI/Applications/NotificationPushServer/CloudNPSService> set url https://broadworks-idp-proxy-m.wbx2.com/nps/ If push notifications time out due to a delay in DNS resolution, increase the timeout value in the "/etc/resolv.conf" file on the BroadWorks server. |
| 4 | (For Android notifications) Add the Android application ID to the FCM applications context on the NPS. XSP\|ADP_CLI/Applications/NotificationPushServer/FCM/Applications> add com.cisco.wx2.android |
| 5 | (For Apple iOS notifications) Add the application ID to the APNS applications context, making sure to omit the Auth key – set it to empty. XSP\|ADP_CLI/Applications/NotificationPushServer/APNS/Production/Tokens> add com.cisco.squared |
| 6 | Configure the following NPS URLs: XSP\|ADP CLI Context Parameter Value XSP\|ADP_CLI/Applications/NotificationPushServer/FCM> authURL https://www.googleapis.com/oauth2/v4/token pushURL https://fcm.googleapis.com/v1/projects/PROJECT-ID/messages:send scope https://www.googleapis.com/auth/firebase.messaging XSP\|ADP_CLI/Applications/NotificationPushServer/APNS/Production> url https://api.push.apple.com/3/device | XSP\|ADP CLI Context | Parameter | Value | XSP\|ADP_CLI/Applications/NotificationPushServer/FCM> | authURL | https://www.googleapis.com/oauth2/v4/token | pushURL | https://fcm.googleapis.com/v1/projects/PROJECT-ID/messages:send | scope | https://www.googleapis.com/auth/firebase.messaging | XSP\|ADP_CLI/Applications/NotificationPushServer/APNS/Production> | url | https://api.push.apple.com/3/device |
| XSP\|ADP CLI Context | Parameter | Value |
| XSP\|ADP_CLI/Applications/NotificationPushServer/FCM> | authURL | https://www.googleapis.com/oauth2/v4/token |
| pushURL | https://fcm.googleapis.com/v1/projects/PROJECT-ID/messages:send |
| scope | https://www.googleapis.com/auth/firebase.messaging |
| XSP\|ADP_CLI/Applications/NotificationPushServer/APNS/Production> | url | https://api.push.apple.com/3/device |
| 7 | Configure the following NPS connection parameters to the recommended values shown: XSP\|ADP CLI Context Parameter Value XSP\|ADP_CLI/Applications/ NotificationPushServer/FCM> tokenTimeToLiveInSeconds 3600 connectionPoolSize 10 connectionTimeoutInMilliseconds 3600 connectionIdleTimeoutInSeconds 600 XSP\|ADP_CLI/Applications/NotificationPushServer/ APNS/Production> connectionTimeout 3000 connectionPoolSize 2 connectionIdleTimeoutInSeconds 600 | XSP\|ADP CLI Context | Parameter | Value | XSP\|ADP_CLI/Applications/ NotificationPushServer/FCM> | tokenTimeToLiveInSeconds | 3600 | connectionPoolSize | 10 | connectionTimeoutInMilliseconds | 3600 | connectionIdleTimeoutInSeconds | 600 | XSP\|ADP_CLI/Applications/NotificationPushServer/ APNS/Production> | connectionTimeout | 3000 | connectionPoolSize | 2 | connectionIdleTimeoutInSeconds | 600 |
| XSP\|ADP CLI Context | Parameter | Value |
| XSP\|ADP_CLI/Applications/ NotificationPushServer/FCM> | tokenTimeToLiveInSeconds | 3600 |
| connectionPoolSize | 10 |
| connectionTimeoutInMilliseconds | 3600 |
| connectionIdleTimeoutInSeconds | 600 |
| XSP\|ADP_CLI/Applications/NotificationPushServer/ APNS/Production> | connectionTimeout | 3000 |
| connectionPoolSize | 2 |
| connectionIdleTimeoutInSeconds | 600 |
| 8 | Check if the Application Server is screening application IDs, because you may need to add the Webex apps to the allow list: Run AS_CLI/System/PushNotification> get and
                            check the value of enforceAllowedApplicationList . If
                            it’s true , you need to complete this sub task.
                            Otherwise, skip the rest of the sub task. AS_CLI/System/PushNotification/AllowedApplications> add com.cisco.wx2.android “Webex Android” AS_CLI/System/PushNotification/AllowedApplications> add com.cisco.squared “Webex iOS” |
| 9 | Restart the XSP\|ADP: bwrestart |
| 10 | Test call notifications by making calls from a BroadWorks subscriber to two
                    Webex mobile users. Verify that the call notification appears on iOS and Android
                    devices. |

| XSP\|ADP CLI Context | Parameter | Value |
|---|---|---|---|
| XSP\|ADP_CLI/Applications/NotificationPushServer/FCM> | authURL | https://www.googleapis.com/oauth2/v4/token |
| pushURL | https://fcm.googleapis.com/v1/projects/PROJECT-ID/messages:send |
| scope | https://www.googleapis.com/auth/firebase.messaging |
| XSP\|ADP_CLI/Applications/NotificationPushServer/APNS/Production> | url | https://api.push.apple.com/3/device |

| XSP\|ADP CLI Context | Parameter | Value |
|---|---|---|---|
| XSP\|ADP_CLI/Applications/ NotificationPushServer/FCM> | tokenTimeToLiveInSeconds | 3600 |
| connectionPoolSize | 10 |
| connectionTimeoutInMilliseconds | 3600 |
| connectionIdleTimeoutInSeconds | 600 |
| XSP\|ADP_CLI/Applications/NotificationPushServer/ APNS/Production> | connectionTimeout | 3000 |
| connectionPoolSize | 2 |
| connectionIdleTimeoutInSeconds | 600 |

| Setting Name | Flowthrough provisioning with trusted emails | Flowthrough provisioning without emails | User self-provisioning |
|---|---|---|---|
| Enable BroadWorks Flow Through Provisioning (include provisioning account credentials if On**) | On Supply the provisioning Account Name and Password as per BroadWorks configuration. | On Supply the provisioning Account Name and Password as per BroadWorks configuration. | Off |
| Automatically Create New Organizations in Control Hub | On † | On † | On † |
| Service Provider Email Address | Select an email address from the dropdown (you can type some characters, to find the address if it's a long list). This email address identifies the administrator within your Partner organization who will be granted delegated admin access to any new customer organizations created with the Onboarding template. |
| Country | Choose which country you use for this template. The country you choose matches customer organizations that are created with this template to a particular region. At present, the region could be (EMEAR) or (North America and rest of world). See the country to region mappings in this spreadsheet . The organization country will determine the default global call-in numbers for Cisco PSTN in Webex Meeting Sites. Refer to the Country section of help page for more information. |
| BroadWorks Enterprise Mode Active | Enable this if the customers you provision with this template are enterprises in BroadWorks. If they are groups, leave this switch off. If you have a mix of enterprises and groups in your BroadWorks, you should create different templates for those different cases. |

| Setting Name | Flowthrough provisioning without emails | User self-provisioning |
|---|---|---|
| Provision Admin First | Recommended* | Not applicable |
| Allow users to self activate | Not applicable | Required |

| Attribute | Required | Description |
|---|---|---|
| IDP Name | Yes | Unique, case-insensitive name. It can include letters,
                                            numbers, hyphens, underscores, tildes, and dots. Max
                                            length: 128 characters. |
| OAuth client Id | Yes | Used to request OIDC IdP authentication. |
| OAuth client Secret | Yes | Used to request OIDC IdP authentication. |
| List of scopes | Yes | Used to request OIDC IdP authentication. Space-separated
                                            list of scopes (for example, openid email profile) must
                                            include openid and email. |
| Authorization Endpoint | Yes if discoveryEndpoint isn’t provided | URL of the IdP's OAuth 2.0 authorization endpoint. |
| tokenEndpoint | Yes if discoveryEndpoint isn’t provided | URL of the IdP's OAuth 2.0 token endpoint. |
| Discovery Endpoint | No | URL of the IdP's discovery endpoint for OpenID endpoints
                                            discovery. |
| userInfoEndpoint | No | URL of the IdP's UserInfo endpoint. |
| Key Set Endpoint | No | URL of the IdP's JSON web key set endpoint. |

| 1 | Verify that the third-party Identity Provider (IdP) meets the requirements listed in
          the Requirements for Identity Providers section of Single Sign-On Integration in Control Hub . |
|---|---|
| 2 | Open a service request with Cisco TAC. TAC must establish a trust relationship between
          the third-party IdP and Cisco Common Identity service. If your IdP requires enabling the passEmailInRequest feature, make sure to include this requirement
                in the service request. Check with your IdP if you’re unsure of whether this feature
                is required. . |
| 3 | Upload the CI metadata file that TAC provided to your IdP. |
| 4 | Configure an onboarding template: For the Authentication Mode setting, select Partner Authentication . Enter the IDP Entity ID . You can find the EntityID from the
                SAML metadata XML of the third-party IdP. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Go to Security > Authentication > Activate SSO . |
| 3 | Select Broadworks and click Activate . The IdP appears in the Identity provider tab. |

| Recording Modes | Description | Controls/Indicators that display on the Webex App |
|---|---|---|
| Always | Recording is initiated automatically when the call is established. The user has no ability to start or stop recording. | Visual indicator that recording is in progress |
| Always with Pause/Resume | Recording is initiated automatically when the call is established. The user can pause and
									resume recording. | Visual indicator that recording is in progress Pause Recording button Resume Recording button |
| OnDemand | Recording is initiated automatically when call is established, but the recording is deleted unless the user presses Start Recording . If the user starts recording, the full recording from the call setup is retained. After
									starting the recording, the user can also pause and resume
									recording | Start Recording button Pause Recording button Resume Recording button |
| OnDemand with User-Initiated Start | Recording doesn’t initiate unless the user selects the Start
										Recording option on the Webex App. The user has
									the option to start and stop recording multiple times during a
									call. | Start Recording button Stop Recording button Pause Recording button |

| 1 | Configure Application Server (AS). Enable URL dialing (Mandatory): AS_CLI/System/CallP/DNS> set enableNameLookupForURLDialing true . Verify: enableNameLookupForURLDialing = Y . This configuration allows AS to process SIP URI calls and generate INVITEs after REFER. |
|---|---|
| 2 | Configure Network Server (NS). Enable URL dialing policy: NS_CLI/Policy/UrlDialing> add DefaultInst true callTypes all . Attach URL dialing policy to routing profile: NS_CLI/Policy/Profile> add routing UrlDialing DefaultInst . This is required to avoid 404 Not Found (usrnf). Enable SIP URI domain matching: NS_CLI/Policy/UrlDialing> set DefaultInst enableSipURIMatchingRules true . Add routing rule for Webex domain: NS_CLI/Policy/UrlDialing/Rules> add DefaultInst *@<webex-site>.webex.com <RoutingNE_to_Internet_SBC> 1 99 . Example: NS_CLI/Policy/UrlDialing/Rules> add DefaultInst *@digiceloffice-200.webex.com Internet_SBC 1 99 This routes Webex meeting INVITEs to the SBC. Verify internet routing network element. Routing NE must point to an internet‑facing SBC/CUBE. NS must not send SIP traffic directly to the internet. |
| 3 | Validate the route test: NS_CLI> vtri <calling-number> <meeting-URI>@<webex-site>.webex.com . You can expect any one of the following results: No 404 error RoutingNE selected Contact returned |

| 1 | Download the zip files of the desired Webex App (Desktop, Mobile, or Tablet) from Software Downloads site. For details on Device Profile Type and Package name, see Device Profiles in the Prepare Your Environment section. |
|---|---|
| 2 | Check that you've the right tag sets in BroadWorks System > Resources > Device Management > Tag Sets . |
| 3 | Import and update DTAF Files. The DTAF package downloaded from the Cisco Software Download site is a container
            archive. You must extract this archive locally to access the specific .DTAF.zip files required for import into the BroadWorks Application
            Server. Locate the downloaded DTAF zip file (for example,
              ucone-mobile-ucaas-X.X.XX-wxt-MonthYear_DTAF.zip) and extract the contents to a local
              directory on your computer. Navigate to the extracted folder. Locate the latest DTAF file for your client (for
              example, Business_Communicator_-_PC(R24.0).DTAF.zip). Log in to the CommPilot interface as a system administrator and go to System > Resources > Identity/Device Profile Types > Import . In the Device Type File Upload section, click Browse , select the .DTAF.zip
              file, and Click OK to import the file. (Optional): If you're updating an existing device type, ensure the Device Type
                File Update check box is selected. This action overwrites existing templates
              with the latest configurations provided in the new DTAF. |
| 4 | Configure Device Profiles for each client you're provisioning. Open the newly added device profile for editing. Enter the XSP\|ADP farm FQDN and Device Access Protocol. Check the Support Remote Party Info check box. This support is required for desktop sharing to work and Remote party CLID to be presented in the Webex client. You can also enable Remote Party support by running the following CLI command on the Application Server: AS_CLI/System/DeviceType/SIP> set <device_profile_type> supportRemotePartyInfo true . Modify the templates according to your environment. For details, see the following
              table. Save the profile. |
| 5 | Click Files and Authentication and then select the option to
          rebuild all system files. Name Description Codec Priority Configure priority order for the audio and video codecs for VoIP calls TCP, UDP, and TLS Configure the protocols used for SIP signaling and media RTP Audio and Video Ports Configure port ranges for RTP audio and video SIP options Configure various options related to SIP (SIP INFO, use rport, SIP proxy
                      discovery, refresh intervals for registration and subscription, and so on) | Name | Description | Codec Priority | Configure priority order for the audio and video codecs for VoIP calls | TCP, UDP, and TLS | Configure the protocols used for SIP signaling and media | RTP Audio and Video Ports | Configure port ranges for RTP audio and video | SIP options | Configure various options related to SIP (SIP INFO, use rport, SIP proxy
                      discovery, refresh intervals for registration and subscription, and so on) |
| Name | Description |
| Codec Priority | Configure priority order for the audio and video codecs for VoIP calls |
| TCP, UDP, and TLS | Configure the protocols used for SIP signaling and media |
| RTP Audio and Video Ports | Configure port ranges for RTP audio and video |
| SIP options | Configure various options related to SIP (SIP INFO, use rport, SIP proxy
                      discovery, refresh intervals for registration and subscription, and so on) |

| Name | Description |
|---|---|
| Codec Priority | Configure priority order for the audio and video codecs for VoIP calls |
| TCP, UDP, and TLS | Configure the protocols used for SIP signaling and media |
| RTP Audio and Video Ports | Configure port ranges for RTP audio and video |
| SIP options | Configure various options related to SIP (SIP INFO, use rport, SIP proxy
                      discovery, refresh intervals for registration and subscription, and so on) |

| 1 | Assign Service in BroadWorks: Create a test enterprise under your service provider enterprise in BroadWorks, or create a test group under your Service Provider (depends on your BroadWorks setup). Configure the IM&P service for that enterprise, to point to the template you are testing (retrieve the provisioning adapter URL and credentials from Control Hub Onboarding template). Create test subscribers in that enterprise / group. Give the users unique email addresses in the email field in BroadWorks. Copy those into the Alternate ID attribute as well. Assign the Integrated IM&P service to those subscribers. This triggers the creation of the customer organization and the first users, which takes several minutes. Please wait a little while before trying to sign in with your new users. |
|---|---|
| 2 | Verify Customer Organization and Users in Control Hub: Sign in to Control Hub with your partner administrator account. Go to Customers and verify that your new customer organization is in the list (name follows the group name or enterprise name, from BroadWorks). Open the customer organization and verify that the subscribers are users in that organization. Verify that the first subscriber to whom you assigned the Integrated IM&P service has become the customer administrator of that organization. |

| 1 | Download the Webex app on two different machines. |
|---|---|
| 2 | Sign in as your test users on the two machines. |
| 3 | Make test calls. |