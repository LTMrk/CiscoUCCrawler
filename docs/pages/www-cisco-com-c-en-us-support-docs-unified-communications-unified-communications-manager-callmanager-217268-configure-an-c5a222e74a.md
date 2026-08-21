---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-217268-configure-an-c5a222e74a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/217268-configure-and-troubleshoot-sso-on-cisco.html
retrieved_at: 2026-08-21T13:59:20.242925+00:00
---

Configure and Troubleshoot SSO on Cisco Unified Communications Manager (CUCM)

# Configure and Troubleshoot SSO on Cisco Unified Communications Manager (CUCM)

### Download Options

Updated: August 5, 2021

Document ID: 217268

Contents

## Contents

## Introduction

This document describes the SSO feature in CUCM, configuration, tips to troubleshoot, example log analysis, and resources for additional information.

## Prerequisites

### Requirements

Cisco recommends knowledge of a few Single Sign-On (SSO) terms:

- Security Assertion Markup Language (SAML) - an open standard to exchange authentication and authorization data between parties

- Service Provider (SP) - The SP is the entity that is hosts the service. In this document, Cisco Unified Communications Manager (CUCM) is the service provider

- Identity Provider (IdP) - The IdP is the entity that authenticates client credentials. Authentication is completely transparent to the SP so the credentials can be a smart card, username/password, and so on. Once the IdP authenticates client credentials, it generates an assertion, sends it to the client, and redirects the client back to the SP

- Assertions – A time-sensitive piece of information that the IdP generates after successful authentication of a user. The purpose of the assertion is to provide information about the authenticated user to the SP

- Bindings – defines the transport method used to deliver the SAML protocol messages between entities.  Cisco Unified Communications products use HTTP

- Profiles – predefined constraints and combinations of SAML message content (assertions, protocol, bindings) that work to achieve a specific business use-case. This training focuses on the Web browser Single Sign-On profile as that is the method used by CUCM

- Metadata – set of configuration information that is exchanged between parties. Contains information such as supported SAML bindings, operational roles such as IdP or SP, supported identifer attributes, identifier information, and certificate information used to sign and encrypt the request or response.

### Components Used

- Cisco Unified Communications Manager (CUCM) 12.5.1.14900-63

- Microsoft Windows Server 2016

- Active Directory Federation Services (AD FS) 4.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The purpose of SSO is to allow users and administrators to access multiple Cisco collaboration applications withou require separate authentications to each one. Enablement of SSO results in several advantages:

- It improves productivity because users do not need to re-enter credentials for the same identity on different products.

- It transfers the authentication from your system that hosts the applications to a third party system. You create a circle of trust between an IdP and a service provider which allows the IdP to authenticate users on behalf of the SP.

- It provides encryption to protect authentication information passed between the IdP, service provider, and user. SSO also hides authentication messages passed between the IdP and the service provider from any external party.

- It can reduce costs as fewer help desk calls are made for password resets.

#### Circle of Trust

Certificates play a very important role in SSO and they are exchanged between the SP and IdP via metadata files. The SP metadata file contains the service provider signing- and encryption certificate along with some other important information such as the Assertion Consume Service Index values and HTTP POST/REDIRECT information. The IdP metadata file contains its certificate(s) along with some other informataion about the IdP capabilities. You must import the SP metadata into the IdP and import the IdP metadata into the SP to create a circle of trust. Essentially, the SP signs and encrypts any request that it generates with the certificate that the IdP trusts, and the IdP signs and encrypts any assertion (response) it generates with certificate(s) that the SP trusts.

Note : If certain information on the SP changes, such as the hostname/Full Qualified Domain Name (FQDN) or signing/encryption certificate (Tomcat or ITLRecovery), then the circle of trust can be broken. Download a new metadata file from the SP and import it into the IdP.  If certain information on the IdP changes, download a new metadata file from the IdP and re-run the SSO test so that you can update the information on the SP. If you are not sure whether your change necessitates a metadata update on the opposite device, it is best to update the file. There is no downside to a metadata update on either side and this is a valid step to troubleshoot SSO issues, especially if there has been a configuration change.

## Configure

### Network Diagram

The flow for a standard SSO log in is shown in the image:

Note : The process in the image is not in order from left to right. Remember that the SP is CUCM and the IdP is the third-party application.

### Configuration

From the CUCM perspective, there is very little to configure with regard to SSO. In CUCM 11.5 and higher, you can select Cluster wide or per-node SSO.

- In CUCM 11.5, Cluster wide SSO requires a multi-server tomcat certificate to be installed on all nodes since there is only one metadata file for the whole cluster (and the certificate is stored in that file, so each node must have the same tomcat certificate).

- In CUCM 12.0 and up, you have the option to Use system generated self-signed certificate for Cluster wide SSO. This option uses the ITLRecovery certificate rather than tomcat:

- Per-node SSO is the default prior to CUCM 11.5. In a per-node configuration, each node has its own metadata file that needs to be imported to the IdP since any of those nodes can potentially redirect a user for authentication.

- You can also enable SSO for RTMT in CUCM 11.5. This is enabled by default and it is located at Cisco Unified CM Administration > Enterprise Parameters > Use SSO for RTMT .

Note : The note that states If SSO mode is Cluster Wide, Tomcat certificate must be multi-server CA Signed certificate is erroneous on 12.0 and 12.5 and a defect has been opened to correct it ( Cisco bug ID CSCvr49382 ).

Aside from these options, the rest of the configuration for SSO is on the IdP. The configuration steps can differ drastically based on which IdP you choose. These documents contain steps to configure some of the more common IdPs:

## Troubleshoot

### Data to Collect

In order to troubleshoot an SSO issue, set the SSO traces to debug. The SSO log level cannot be set to debug via GUI. To set the SSO log level to debug, run this command in the CLI: set samltrace level debug

Note : This command is not Cluster wide, so it needs to be run on each node that could be involved with an SSO log in attempt.

Once the log level has been set to debug, reproduce the issue and collect this data from CUCM:

- Cisco SSO logs

- Cisco Tomcat logs

Most SSO issues generate exceptions or errors in the SSO logs but in some circumstances, the Tomcat logs can be helpful as well.

### Example Analysis

#### Device information from TAC lab

CUCM (Service Provider):

- Version: 12.5.1.14900-11

- FQDN: 1cucm1251.sckiewer.lab

Windows Server 2016 (Identity Provider):

- Active Directory Federation Services 3.0

- FQDN: WinServer2016.sckiewer.lab

#### Log Review for CUCM

```
tomcat/logs/ssosp/log4j/ %%%%% A user has attempted to access Cisco Unified CM Administration 2021-04-30 09:00:53,156 DEBUG [http-bio-443-exec-83] filter.SSOAuthAgentFilter - servlet path :/showHome.do 2021-04-30 09:00:53,157 DEBUG [http-bio-443-exec-83] filter.SSOAuthAgentFilter - recovery URL :/showRecovery.do %%%%% You can see the SP and IdP EntityIDs here 2021-04-30 09:00:53,194 DEBUG [http-bio-443-exec-83] fappend.SamlLogger - SPSSOFederate: spEntityID is : 1cucm1251.sckiewer.lab 2021-04-30 09:00:53,194 DEBUG [http-bio-443-exec-83] fappend.SamlLogger - SPSSOFederate: idpEntityID : http://WinServer2016.sckiewer.lab/adfs/services/trust %%%%% The client is redirected to the SSO URL listed here 2021-04-30 09:00:53,196 DEBUG [http-bio-443-exec-83] fappend.SamlLogger - SPSSOFederate: SingleSignOnService URL :https://winserver2016.sckiewer.lab/adfs/ls/ %%%%% CUCM prints the AssertionConsumerService URL and you can see that CUCM uses an HTTP-POST 2021-04-30 09:00:53,196 DEBUG [http-bio-443-exec-83] fappend.SamlLogger - SPSSOFederate: AssertionConsumerService : URL :https://1cucm1251.sckiewer.lab:8443/ssosp/saml/SSO/alias/1cucm1251.sckiewer.lab 2021-04-30 09:00:53,196 DEBUG [http-bio-443-exec-83] fappend.SamlLogger - SPSSOFederate: AssertionConsumerService : Binding Passed in Query: urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST 2021-04-30 09:00:53,196 DEBUG [http-bio-443-exec-83] fappend.SamlLogger - SPSSOFederate: AssertionConsumerService : Binding : urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST %%%%% Here CUCM prints the AuthnRequest to the client. The client is redirected to the IdP with a 302 and this request 2021-04-30 09:00:53,199 DEBUG [http-bio-443-exec-83] fappend.SamlLogger - SPSSOFederate: AuthnRequest:<samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="s29fd87c888ef6a4bc8c48d7e7087a8aeb997dd76f" Version="2.0" IssueInstant="2021-04-30T13:00:53Z" Destination="https://winserver2016.sckiewer.lab/adfs/ls/" ForceAuthn="false" IsPassive="false" AssertionConsumerServiceIndex="0"> <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">1cucm1251.sckiewer.lab</saml:Issuer> <samlp:NameIDPolicy xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" SPNameQualifier="1cucm1251.sckiewer.lab" AllowCreate="true"></samlp:NameIDPolicy> </samlp:AuthnRequest> %%%%% You can see that CUCM has received an encoded SAML response that is base64 encoded 2021-04-30 09:01:03,986 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - SAML Response is ::PHNhbWxwOlJlc3BvbnNlIElEPSJfYTM2ZDE5ZjItM2UzZC00Yjg0LTlhNDItNGFmN2JkMWQ4YTcxIiBWZXJzaW9uPSIyLjAiIElzc3VlSW5zdGFudD0iMjAxOS0wOC0zMFQxMzowMTowMy44OTFaIiBEZXN0aW5hdGlvbj0iaHR0cHM6Ly8xY3VjbTEyNTEuc2NraWV3ZXIubGFiOjg0NDMvc3Nvc3Avc2FtbC9TU08vYWxpYXMvMWN1Y20xMjUxLnNja2lld2VyLmxhYiIgQ29uc2VudD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmNvbnNlbnQ6dW5zcGVjaWZpZWQiIEluUmVzcG9uc2VUbz0iczI5ZmQ4N2M4ODhlZjZhNGJjOGM0OGQ3ZTcwODdhOGFlYjk5N2RkNzZmIiB4bWxuczpzYW1scD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOnByb3RvY29sIj48SXNzdWVyIHhtbG5zPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uIj5odHRwOi8vV2luU2VydmVyMjAxNi5zY2tpZXdlci5sYWIvYWRmcy9zZXJ2aWNlcy90cnVzdDwvSXNzdWVyPjxzYW1scDpTdGF0dXM+PHNhbWxwOlN0YXR1c0NvZGUgVmFsdWU9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpzdGF0dXM6U3VjY2VzcyIgLz48L3NhbWxwOlN0YXR1cz48RW5jcnlwdGVkQXNzZXJ0aW9uIHhtbG5zPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uIj48eGVuYzpFbmNyeXB0ZWREYXRhIFR5cGU9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZW5jI0VsZW1lbnQiIHhtbG5zOnhlbmM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZW5jIyI+PHhlbmM6RW5jcnlwdGlvbk1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZW5jI2FlczI1Ni1jYmMiIC8+PEtleUluZm8geG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiPjxlOkVuY3J5cHRlZEtleSB4bWxuczplPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGVuYyMiPjxlOkVuY3J5cHRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGVuYyNyc2Etb2FlcC1tZ2YxcCI+PERpZ2VzdE1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNzaGExIiAvPjwvZTpFbmNyeXB0aW9uTWV0aG9kPjxLZXlJbmZvPjxkczpYNTA5RGF0YSB4bWxuczpkcz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PGRzOlg1MDlJc3N1ZXJTZXJpYWw+PGRzOlg1MDlJc3N1ZXJOYW1lPkw9UlRQLCBTPU5DLCBDTj1JVExSRUNPVkVSWV8xY3VjbTEyNTEuc2NraWV3ZXIubGFiLCBPVT1UQUMsIE89Q2lzY28sIEM9VVM8L2RzOlg1MDlJc3N1ZXJOYW1lPjxkczpYNTA5U2VyaWFsTnVtYmVyPjEzNDkzNjAzNDA3NzA3NTkxMzA3MzMwMTI3MjY3OTM0NDY5MjA1MzwvZHM6WDUwOVNlcmlhbE51bWJlcj48L2RzOlg1MDlJc3N1ZXJTZXJpYWw+PC9kczpYNTA5RGF0YT48L0tleUluZm8+PGU6Q2lwaGVyRGF0YT48ZTpDaXBoZXJWYWx1ZT5uRk9uN3RjNVFwZGV6SU1TTVMxc1RBMW55aHNJTG5VQVRLakRkNUNMNkV0L3c3R2dVeEsrZkZsaDdhaGkzVFg1ZUcweEs4QkRXMXNORHM4dm94ZEYycTduL0xmckFPTmg4ZzUzY1ZRZWN5TEtPaGlHZDNVZDNvazl5cHkwMmlZU1pYNkNMWGtGdGR5V0l6WUIzZDBwb0paeG5pdkRNUE8zMHEzbVRwZmNQZVgzeTdGRU5UVS9DZ1Z3dkpTdllyNDRudnZmcmRHTm9DMTRhc2pqUHFvVXJ2MEN4TnUwNThCcGQwU25JSzdhSnRQaExya29OK1JNaWZVdzlzRWxIY0o1SVVkWE5wczhKVnNxaFBwZWpvYnZiSnBwRWM3QkdkT0ZZTW8yVWJmeTVSZ3M1UE4ya2lLTE5YSVV0Qnh4emVxNi91VjlmbktYcFpqMy9KRWRRR3ZsOVE9PTwvZTpDaXBoZXJWYWx1ZT48L2U6Q2lwaGVyRGF0YT48L2U6RW5jcnlwdGVkS2V5PjwvS2V5SW5mbz48eGVuYzpDaXBoZXJEYXRhPjx4ZW5jOkNpcGhlclZhbHVlPjVxeVZRYmRYaEx5L2xOdHUvNnVQbmVUSzNIaStSc3dYVG10UnRSK1ZuQzNZMEtxU1VlWDR0TkJtNFZwclNrVUlFcDkrZDFueU9sclRPQkZNME1XUmtpbXdKbDVGeTluWExQWXpIVndYQU5WaEFaZ3A0MEpTMXVQTlR2ZTVmY1RtbFh2UkhMR1U5WkFFbG9veGNGVDhKQloyRmJzM29NeE5CK0J4N242bDFUZ2hpZE01M3d1Qm1xckRHWFFyQ0xJVGxOVmxMcjRJNnN4L0lmZUNJUS9KUHI3N011T20xTFk3a1BRSFFqOEI5YlgzKzVLbUNWazhVbXFnRGZGcEVqdUl2OUdIbFVoS2FxeitGUVU4M3B5Y3B1djkvMjNQcnBIc01RTjNIQ3QvV0lDbHZPQVBzV251Z0xrcytqVy9UTXZFWlBKdWMvWUVIYkVGc2kreWxhdDZ0UyttM2hNdGJGUVV1a3JCekM3L3RrUmFPNXhnbkJ5ZmtGakxxVUE1ZFE3ZXY3YUU1azJJM3ZmN2haeU4wdkJKK2FnUEN4MVlpOFgxOERPS2J0dm9IYXJZNUpkUzVGQzVPeHFJVTdnVmpmdjFIWUUvdjE1RjgzOEMxMmZzaVJZSlNPUjk4UzdZamdmaVJWK3NVdUsvV21UanpXUVhYWGVsQktBc0NCb2lvNDE3RTJLU29iaUhiaklhbXczTUIwdlJ2MUFuZkJHazJJMUZhcms3WVM3OUkzSnZjMjlxRDVuNHB4ZllkU0xHRHlmcUxzYUN6MEE2WjR0eUtQU0FMRk1LdE0weUxUUEcySnA4UklEaWpERDFZeU04eDN1NmIxenZrY2I2Mmo4Z2lGSWY2K1hiSkRWSVR1ZW4wa0cxeWFiM0NjZmY2OG8rQk1kVUFTc094UGZLVUF2UkN1WmdocDcrbFpmeEVjWlFHUnpVZ3B6MjI0TWNJVnVGbXNMVUtJMDVTVVJFNHJzaExGdXRJRlJXNit6eXljSUlZWWFXRE5kUzUvWjRzd3lhTTQ1VFkyU1lBbW5laWYvVUwyVUMzSHphWWNta2xxak9OTG1WNFlycnN3YjZxTFdOS3RrUnpJUnBpb0NZVjB3RFg4blZIRUhLNTk4RW1yclI2bWIzT0N2Y21IYnhUY2dCRGV5ZWFNd1Z1dVpxd2UrN29YOXhZUjRZSHZTa1pVbXdOd0tmeGpvUUQrK3lKOTZ6QVFqQkpjRC81c1dOTm9ldTBJNFNtSXNmbEVkT1NRSzlzUjI5ZXJQV1J6c0hBbkpaRVptK1I5Mm9SWU9Yd2hVb2J1WjF6bWM4dUt0K2tlMkRBVCtjU3N6bUZKbFo5SVdwQzJtSVh1RFpGdnNXLzR1QjJXWitWc2dYdUo4eEJ4cFB4RWhjaGNNMk5yaHJxMTZOczRuL3dhZS82Nk16NFN2Z0hkM3RjZUNheWdGOEF3a1JlSHVBM2VGRjVMWmhrRjN3UzM0Zk9ieDhPbFhER1BMNE13M09GbVF4Q0p5ZDZtVXl6Qzk1WUhYckcvNHp2ek1YVXJ6NU9lUVBQNXRxNHl2clR6ODlHMVFFMHJkMXZGN29PNGE0aFNPOFg0VllQdmoyT2h5Yk00ZUhOQU92K2hmTzNqeWlGTnN0SnVENlU2bVZQLzhSQjg3RWsxWHAxNUJ5YWpMR0k0V3dFYkFJZjZtVUVSQlhrTCs4Ukh4RnVvRlVuQ1kwb0dkaGdkZGRtKzNXVlIwZXE2RjNiT1dyZVdZVjlMa3pnMXo1VjlkR2hGazVhd0ZKQkJOZ1dDeHFJQ3RrV09URHZwRnRVRk5DUmc5dHdVb3lYQTlncnAyeEsvUURieEE4dzJFNXNpUUVYN29VSFM3STVIbUUwdW50RkxDT2xOL2tYVXNneHpuVy90WWlESUZhSEd3bStId2pCN0I5WFhhbzB2aTZVS1Y5bnBCVngxNVlLbXhPMkIyc282Z25JaUNzTno0c0ozOWR4YzhrWnhCYUtIYkt0c0N5aWtXRzh4VkY1cUlZTU5RV1JNTU0zam83Zk9HaElaV00zd0VOa1BYc1lqa3d2dExidnVSOEZRU3lIcXNwbnVYWktPQlJ3VjllMjQzMFV4Y3diM3ZsTTU1V2JndlpzSXBSdXg5aE1nSWZIdXlGVzJXV2lZdTJZaHZLamNpQndjL2NpQjJyVEYwc0dRNHBmY00vRWZ4S3VFbGhyY1kwbkwrVnNpVzFvem5mc2VjOXVsVnpEcWlXWlNCNldEQ05FNmJrQVB6WmJJT1FUT3FqRmp1UkIzdTJEV3FhUEhNNFFTWnRsNForTC9HSGszZmRLYXZTcVA2UU1LOWNtTERyWkdtaFM5ZWpnSXJPOTV4aGF1aWhidWYvc0NmbXpTMHZjOTFsc0JkM1YrMURoY2JkM0daaUFuRHpncEdiRlVqM1piSnhPM0lSZDBEdFRtOVFRV2lYQndVczNYd2NOVWNWTSt4ZjkzenFVazRsejJEQmw1N3VVWjIvQ0ZraDZ0TlVxaXAvZzgzQytTcVZTZ2dNbEY1UTUrWW4zdC9RZVRsRmtxdXFZQmltTk5sM202V1J3ZkE1WXhRTXYyWXRFR0Q2bkFMNjExb3J0UnVUOVFnd2Jmc29ROUZ0ajhaU3BMaG9hRXAvMVpKVEFqMFRsc0hwS3V3WWN5dS9zSGlSaVZPZ3ZlajhFY3grbUNBMjFiTysydnBJY2V2YTV5TXduZmhiQTdhSGpuM3V6L29hYytvNWsvZDNtMTIrTndvSHFSSWNLN3g5UWYxQjhFeTJBY1VhTzJlWEgyZ3JqV0VKdzJnZC9kVDNYc2ZDclpjdVd2R3pNai9ONW1CVXpRa2VqN2xiNkJpa3ZDaW9ma3VWVFZocUR2cXVpMWQrT3B5MExjYitNM2xYQUZZUlZsMk9RWFgzUEdPZ3NubGNoTitXOWtSSU1EQldRQWtpcG5EWG1GeVc3K1JYZHR4RitObDdTZ2ZLd3NlMDczd1RaMlZKQ0N0bVljK0xvai9MTTErNEp0N0U0SmprdEJYRzhURDhSSGNWNGZMUDdQOFpKQThkTTFNNTBaVXRkcFQzVzdhWjdPMEhNdVBub1BUVTQ1bzhacUxoQndkb2dyRHhEbEc5bkFrQmxacHNWMTdJaEp1ekVkZmV1dFdUcElnTTB2TVVWbDhNYVlDcTk3THBJZThYOFVYWmZBcldITUJ6bHhDZyswT29rdW0yRmxLRmF2SGJsZXFqUWc2MThqRithSzBoNEVObHd3WW4vdkRLc0Vwc0tQZ1RFTElDNHJESkpXaDAvRVdVQ01YcXQra3hyMDRXMzZMMkY3aDlIQVFnU2tkdHQ5ckZkTWlBNVVUQWp1NHd0WWNBUEF3T3JYcGM2NTY3WGo0YkNvazlGaDB4ZU5CSm5NYTFhSUdHeUhxL2xnK1hWbWpsYWlFSXJQcHlFaWFIYTMyTWVZd1B3em1JOWI0NVdCZG9scVRMTXZ3aHZ4U0ovN3N5MkdBVDVneGF0ajVHSmZJRzVXM0dlTThRczBpc0txWjZVWFM4T0ZaY1RzeEUvSHRsL3B5dndzZ3J6Z2NlN3hKT210Q1RKTzV5YUJHczloZWhNUERMVXhZZ1JGRFlzWVJ5K0ZuUFZQalJ1b01WNnRpekszcFEzUDgrdXZBcEJiVzNZTWYySDhBTTlHMVY4Tzg2RGw3TUdoRTRSZGhPSHBYalJ4eXQ2ZGhXcG5CRi9uNUVFZjI0ZlZDVlhiSFRYcUNkcjhTenZCdjlvOS9UMkw0RHp4QnZ4VkI4ZWE3dkhJNWpaQ0Q5VVc5OG5FTWpKeitSc2NIU1JOeXhDR080K3JOanVvNUpZTDNyaXVlQlZXRjhNcEdLZG5ST2oxVEhvTWhiSjVlRlZKWGJlcE9kaVd5Z2h2VTFraHFVbVJpUkFuSXlkcUFQbG5SR3VnaFhpbnlhbjVQK0hjcUFTUDlIRXR4Zlh3OC9aNzhCUkhQbThxWUVLSjdxZjRMKzFjbmtuMDhFWk5ra2hsN1pKUm5zWGtMbDZsT3VURXUvTzBGYUNYQ1B1R1g0clg1VXY3QW5wT1dkN3kzUmNxK1hQT1JDamI1R0Mya1FoUG9xaDBCNlhKbUJzeFlHOGZ4bGR3NmdHVVMyZVFjdldpb2RxWlNaQmhPb0k2UmxJSkxaT1dZRnYxcm5LZndKVjljdFhYdk5iWGJlV1hoYUJ1NGJrY0gzSzhFcmhJTWZrWnNKU3pTaEpna0FIU0RDY0gxYW5xbWxHL0pTc3BUckZseXV3enBtdCtZNkRnNENxOGpRZVVzWTFxbDZCZFM1aXc4RnhveWlwKzQ4U1J4RUU1Y0RONWZlRHorM25YYko3ektaUWl1Z0VZTGJodFJESG16VW04RzRDejNtempNYWR1TzVFbzUvWUFUdzkvU0pic3VmYTlZK3lIN3l5KzZVU2RSbmJYTS9JaWxFRGIyR05nMmlFRGhvcXlxT2hPcW1abmpxNjlZQ1BvUHZCQ2VRNDIrS3RNa1NYdFQrb3RRRmpvSXFrSzRzYTdjTVZkb3QvZFdwUlFaWnBPcDhLWjFoelBheVowazRyUU5WdW1xOThGOXp1WjVnNGV2dktTcm1RakVyaWhOODRLc01JdjZCMzJUOEJpL2RIRlZIU1hXQVRtd0tNQkpYUHVUaVRub3hHU1J6UllTeDlDMng4ZitWU054c3d3MEJMYVIwQjBxQ0wwL3ZKUEN4V2NkVDJCdk1xbXJEYUg3OHFVU3VxUEI3V3p1RjhsTGVrWHhIQzBpcFV5MFp3ZHJ0Y2g0VTVaOHpZS05WWDVoZkZrVjZXM1p5cE5uR2t4d2JNYkJQbTZiN0hVOE80aVVLR1JLZndoYktrYitROU5wU3lkcVE5Q0ozNDg0V1B6eTY1RFAxQlkxQldKTkovQ2dLN0NYT0xzVmVoZTV2R0VNVnJxWFdnOVY5Z2tUd25aSXFBNGZpRlRtSC94MnBmQzNVcG8yemdhVEluRHVrZzVHODZ1bkpYQm9EMVFlZVVJcWRjeWUrS0FWU2F1eW9kdmgzTk9JcjAremh4amxZUjZibEl6NzRDWU0zRnBQWUZwL0E0WGN4MWU4MUd1R2c0OGF5K3RoK1VYRkhJSGROTGpMQUp6eW93NFhwSFV3cHQ1M1V4WkxmUEVXVE54TjkySWQ2eit2aTVEbDNMalRXNWZHUWVEL3BkRHY1S3l2Q1FpYXVmV0pBRnY4MHRHbStZSFROT2RNN0lScjdZV1VFamIyQ3hQUXF0T2EzckFOSGFFSEZDS1BQei9FOExtRHRNTlY4ZGw3ZnpIbWZMalozeGRVV1VZZzFYYkIvRG9kaVZUS2ZPUHg2YllLbVhLSUJTeVM4SFRQQlRnUDZsQlNNeDRSa0JkNUFjV0xNL1p4cHFDblhkTTIyNjF4ZXh4YlQ2UzlwUDNlMk96eCtVSHRLY0tGL0ZxTTdUbHlTZWJMdWxSMGdyNmFtdXNQcnFFWjF1M2w5NXowc1EvckoxWXk2MC9ON2w2MENjWmh1NDMxa2xQZHkreHBkdjJob0hTWGt2Smhkak95QnQ5alFueHJwRE1ULzdRVFc2eWg3NzUwSkdwUkJYSkhyODhDMlEydFl5S1hqY2psU3h3MlBEbS9zYTY2ckdWaHJmNWlzK2VFYlZibmJrVStSRnM1ZStJc01wTTVPbmNWQ0hNZ2NqSHQ4N2hVVVJJNjA3U0RwaWN2VGE2cklLUGxuNmRleXJjUE9sb1krUld6aXRTQk43bnhnWVZlQUIyVnJSdWxUTG5aRjFMVmF1bUlxc0pNcEdhNWIycFdaWDczU2hkV0M4OVVDa1lrRFlDVlJ3YkQ0bEVOenhLYk5tYXpZM3BDRkZ4VU5LVjd3T1NkVXpTVnJwYktIR2dLcC8yaGtZd2ZTMHNtTmJKdFdGaWZKNi9TLzNUSlBjWVR4ZGppdmF5dzdmeVVKTVBoR2V6bU9tL01QVzkycDVUeWMwMGQrdlNHeGV5YTd0Y2RjVXNZZ0p2MUUrN2l0azBBUzVLNDBON0s1R0Z6MlhWNy9VM0NPZXA3MjJKSm1ReWh4eVRHNndOK09PRHc1TmZsaGliNmkxdmt0V2l3Z3dVd0N4SjFTNGZQWExYdlpGSHR1L2ZXQit4SlBmamJLeTRNVllabFg5MytSRXArZklQUUJraXZJZlgyaVhzbGJRL1FTUVFFV3dCN05kYnpJOEJBRFluYi9jMjNTZlVhdUxDQ2V4UTBZbSt6Kzd4bHVBYS9WNUd4Q1BaTFNzR0M4ZGlrUjhHQmt0d0gxWG8rWWtmd3dkZ2p4S2l4TFRZbGFiTDMzPC94ZW5jOkNpcGhlclZhbHVlPjwveGVuYzpDaXBoZXJEYXRhPjwveGVuYzpFbmNyeXB0ZWREYXRhPjwvRW5jcnlwdGVkQXNzZXJ0aW9uPjwvc2FtbHA6UmVzcG9uc2U+ %%%%% Here is the encrypted SAML response from the client. You can see that the InResponseTo value matches the ID from the SAML request, so it is clear that this is a response to that request 2021-04-30 09:01:04,005 DEBUG [http-bio-8443-exec-85] fappend.SamlLogger - SPACSUtils.getResponse: got response=<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="_a36d19f2-3e3d-4b84-9a42-4af7bd1d8a71" InResponseTo="s29fd87c888ef6a4bc8c48d7e7087a8aeb997dd76f" Version="2.0" IssueInstant="2021-04-30T13:01:03Z" Destination="https://1cucm1251.sckiewer.lab:8443/ssosp/saml/SSO/alias/1cucm1251.sckiewer.lab" Consent="urn:oasis:names:tc:SAML:2.0:consent:unspecified"><saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">http://WinServer2016.sckiewer.lab/adfs/services/trust</saml:Issuer><samlp:Status xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"> <samlp:StatusCode xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" Value="urn:oasis:names:tc:SAML:2.0:status:Success"> </samlp:StatusCode> </samlp:Status><EncryptedAssertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion"><xenc:EncryptedData xmlns:xenc="http://www.w3.org/2001/04/xmlenc#" Type="http://www.w3.org/2001/04/xmlenc#Element"><xenc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes256-cbc"/><KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><e:EncryptedKey xmlns:e="http://www.w3.org/2001/04/xmlenc#"><e:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p"><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/></e:EncryptionMethod><KeyInfo><ds:X509Data xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:X509IssuerSerial><ds:X509IssuerName>L=RTP, S=NC, CN=ITLRECOVERY_1cucm1251.sckiewer.lab, OU=TAC, O=Cisco, C=US</ds:X509IssuerName><ds:X509SerialNumber>134936034077075913073301272679344692053</ds:X509SerialNumber></ds:X509IssuerSerial></ds:X509Data></KeyInfo><e:CipherData><e:CipherValue>nFOn7tc5QpdezIMSMS1sTA1nyhsILnUATKjDd5CL6Et/w7GgUxK+fFlh7ahi3TX5eG0xK8BDW1sNDs8voxdF2q7n/LfrAONh8g53cVQecyLKOhiGd3Ud3ok9ypy02iYSZX6CLXkFtdyWIzYB3d0poJZxnivDMPO30q3mTpfcPeX3y7FENTU/CgVwvJSvYr44nvvfrdGNoC14asjjPqoUrv0CxNu058Bpd0SnIK7aJtPhLrkoN+RMifUw9sElHcJ5IUdXNps8JVsqhPpejobvbJppEc7BGdOFYMo2Ubfy5Rgs5PN2kiKLNXIUtBxxzeq6/uV9fnKXpZj3/JEdQGvl9Q==</e:CipherValue></e:CipherData></e:EncryptedKey></KeyInfo><xenc:CipherData><xenc:CipherValue>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</xenc:CipherValue></xenc:CipherData></xenc:EncryptedData></EncryptedAssertion></samlp:Response> %%%%% Here you can see that the IdP uses a supported binding type 2021-04-30 09:01:04,010 DEBUG [http-bio-8443-exec-85] fappend.SamlLogger - SAML2Utils.verifyResponse:binding is :urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST %%%%% The decrypted assertion is printed here. You see that a lot of important information covered later in this doc 2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - <Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_23d2b89f-7e75-4dc8-b154-def8767a391c" IssueInstant="2021-04-30T13:01:03.891Z" Version="2.0"><Issuer>http://WinServer2016.sckiewer.lab/adfs/services/trust</Issuer><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/><ds:Reference URI="#_23d2b89f-7e75-4dc8-b154-def8767a391c"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/><ds:DigestValue>aYnlNK8NiHWHshYMggpeDsta2GyUKQI5MmRmx+gI374=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>rvkc6QWoTCLDly8/MoRCzGcu0FJr6PSu5BTQt3qp5ua7J/AQbbzWn7gWK6TzI+xcH2478M2Smm5mIVVINXnGW4N0U62hZz/aqIEm+3YAYTnvaytw9TFjld2rngkWzTIILAm6fslr9uZCVDHS37g0Ry2mUHYU0KHHXsbm/ouDS/F/LAm/w27X+5++U0o6g+NGE00QYwmo5hg+tNWmMxCnLtfENi8dGE+CSRv1oklLIx1QtK3mMI13WiebxOzp9ZP8IR5J1JxkkOWt9wSGBmZO7Gr7ZUmmEFpJ13qfKtcNZ9P8545rZ9UYHBcPH6H2uwYL0g8Awp5P74CAXHFwS1X2eg==</ds:SignatureValue><KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIC8DCCAdigAwIBAgIQQ2RhydxzTY1GQQ88eF3LWjANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylBREZTIFNpZ25pbmcgLSBXaW5TZXJ2ZXIyMDE2LnNja2lld2VyLmxhYjAeFw0xOTA0MTYxMjM0NDFaFw0yMDA0MTUxMjM0NDFaMDQxMjAwBgNVBAMTKUFERlMgU2lnbmluZyAtIFdpblNlcnZlcjIwMTYuc2NraWV3ZXIubGFiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsR20Nb3o8UqWeP8z17wkXJqIIYnqtbxiQXmdh4fJ4kNDno590dWFRjGTtcM+S44d6inis1lAfTWUgpsPWOCUgQWlA0o8Dyaq8UfiMIkt9ZrvMWc7krMCgILTC3m9eeCcypm9CdPZnuoL863yfRI+2TJr6j/nbUeIVL1KzJHcDgAVtcn/p/+0aHOC7GplC0yVI67FumWagVt9EaK+0SumclZYFyFTX641lfbpRbmcfAKrx0b10bfCkKDdCjgzXobuxlabzPp6IUb4NIsGIpm7fo7B23wHl/WIswu26XDp0IADbX25id9bRnR6GXRbfnYj1LBxCmpBq0VHsO1G7VwR4QIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQCPckMMbI7J/AQh62rFQbt2KFXJyyKCHhzQKai6hwMseM/eKScqOXG1VqPEjtbXx2XdqECZ8AJu64i6iaH1oMIcjxQtepZMHqMh/sKh1565oA23cFO5DttgXeEfyUBQe6R4lILi7m6IFapyPN3jL4+y4ggS/4VFVS02QPaQYZmTNnor2PPbOlMkq0mZO0D81MFk5ou1Np2zOGASq96/pa0Gi58BxyEZGCLbJlTe5v5dQnGHL3/f5BmIxduer7nUOvrEb+EdarxxwNHHRLB484j0W7GVQ/g6WVzvOGd1uAMdYfrW5Djw1W42Kv150eSh3RJg54Kr5EsoUidrz982Z+lX</ds:X509Certificate></ds:X509Data></KeyInfo></ds:Signature><Subject><NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" NameQualifier="http://WinServer2016.sckiewer.lab/adfs/com/adfs/service/trust" SPNameQualifier="1cucm1251.sckiewer.lab">SCKIEWER\admin</NameID><SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><SubjectConfirmationData InResponseTo="s29fd87c888ef6a4bc8c48d7e7087a8aeb997dd76f" NotOnOrAfter="2021-04-30T13:06:03.891Z" Recipient="https://1cucm1251.sckiewer.lab:8443/ssosp/saml/SSO/alias/1cucm1251.sckiewer.lab"/></SubjectConfirmation></Subject><Conditions NotBefore="2021-04-30T13:01:03.891Z" NotOnOrAfter="2021-04-30T14:01:03.891Z"><AudienceRestriction><Audience>1cucm1251.sckiewer.lab</Audience></AudienceRestriction></Conditions><AttributeStatement><Attribute Name="uid"><AttributeValue>admin</AttributeValue></Attribute></AttributeStatement><AuthnStatement AuthnInstant="2021-04-30T13:01:03.844Z" SessionIndex="_23d2b89f-7e75-4dc8-b154-def8767a391c"><AuthnContext><AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</AuthnContextClassRef></AuthnContext></AuthnStatement></Assertion> XML Representation %%%%% CUCM looks at its current time and makes sure that it is within the validity timeframe of the assertion 2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - Time Valid?:true 2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - SAML Authenticator:ProcessResponse. End of time validation 2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - Attributes: {uid=[admin]} %%%%% CUCM prints the username here 2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - userid is ::admin 2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - Realy state is ::/ccmadmin/showHome.do 2021-04-30 09:01:04,091 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - http request context is ::/ssosp %%%%% The client is redirected to the resource it initially tried to access 2021-04-30 09:01:04,283 INFO [http-bio-8443-exec-85] servlet.RelayToOriginalAppServlet - relayUrl ::/ccmadmin/showHome.do:: 2021-04-30 09:01:04,284 INFO [http-bio-8443-exec-85] servlet.RelayToOriginalAppServlet - redirecting to ::/ccmadmin/showHome.do::
```

### Closer Look at the SAML Request and Assertion

#### SAML Request

Analysis and information about the SAML request:

```
AuthnRequest:<samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" %%%%% The ID from the request is returned in the assertion generated by the IdP.  This allows CUCM to correlate the assertion with a specific request %%%%% This log snippet was taken from CUCM 12.5, so you use the AssertionConsumerServiceIndex rather than AssertionConsumerServiceURL (more information later in this doc) ID="s29fd87c888ef6a4bc8c48d7e7087a8aeb997dd76f" Version="2.0" IssueInstant="2021-04-30T13:00:53Z" Destination="https://winserver2016.sckiewer.lab/adfs/ls/" ForceAuthn="false" IsPassive="false" AssertionConsumerServiceIndex="0"> <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">1cucm1251.sckiewer.lab</saml:Issuer> %%%%% The NameID Format must be transient. %%%%% The SP Name Qualifier allows us to see which node generated the request. <samlp:NameIDPolicy xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" SPNameQualifier="1cucm1251.sckiewer.lab" AllowCreate="true"/> </samlp:AuthnRequest>
```

#### Assertion

Analysis and information about the SAML response:

```
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_23d2b89f-7e75-4dc8-b154-def8767a391c" IssueInstant="2021-04-30T13:01:03.891Z" Version="2.0"> %%%%% You can see that the issuer of the assertion was my Windows server <Issuer>http://WinServer2016.sckiewer.lab/adfs/services/trust</Issuer> <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"> <ds:SignedInfo> <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/> <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/> <ds:Reference URI="#_23d2b89f-7e75-4dc8-b154-def8767a391c"> <ds:Transforms> <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/> <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/> </ds:Transforms> <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/> <ds:DigestValue>aYnlNK8NiHWHshYMggpeDsta2GyUKQI5MmRmx+gI374=</ds:DigestValue> </ds:Reference> </ds:SignedInfo> <ds:SignatureValue>rvkc6QWoTCLDly8/MoRCzGcu0FJr6PSu5BTQt3qp5ua7J/AQbbzWn7gWK6TzI+xcH2478M2Smm5mIVVINXnGW4N0U62hZz/aqIEm+3YAYTnvaytw9TFjld2rngkWzTIILAm6fslr9uZCVDHS37g0Ry2mUHYU0KHHXsbm/ouDS/F/LAm/w27X+5++U0o6g+NGE00QYwmo5hg+tNWmMxCnLtfENi8dGE+CSRv1oklLIx1QtK3mMI13WiebxOzp9ZP8IR5J1JxkkOWt9wSGBmZO7Gr7ZUmmEFpJ13qfKtcNZ9P8545rZ9UYHBcPH6H2uwYL0g8Awp5P74CAXHFwS1X2eg==</ds:SignatureValue> <KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#"> <ds:X509Data> <ds:X509Certificate>MIIC8DCCAdigAwIBAgIQQ2RhydxzTY1GQQ88eF3LWjANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylBREZTIFNpZ25pbmcgLSBXaW5TZXJ2ZXIyMDE2LnNja2lld2VyLmxhYjAeFw0xOTA0MTYxMjM0NDFaFw0yMDA0MTUxMjM0NDFaMDQxMjAwBgNVBAMTKUFERlMgU2lnbmluZyAtIFdpblNlcnZlcjIwMTYuc2NraWV3ZXIubGFiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsR20Nb3o8UqWeP8z17wkXJqIIYnqtbxiQXmdh4fJ4kNDno590dWFRjGTtcM+S44d6inis1lAfTWUgpsPWOCUgQWlA0o8Dyaq8UfiMIkt9ZrvMWc7krMCgILTC3m9eeCcypm9CdPZnuoL863yfRI+2TJr6j/nbUeIVL1KzJHcDgAVtcn/p/+0aHOC7GplC0yVI67FumWagVt9EaK+0SumclZYFyFTX641lfbpRbmcfAKrx0b10bfCkKDdCjgzXobuxlabzPp6IUb4NIsGIpm7fo7B23wHl/WIswu26XDp0IADbX25id9bRnR6GXRbfnYj1LBxCmpBq0VHsO1G7VwR4QIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQCPckMMbI7J/AQh62rFQbt2KFXJyyKCHhzQKai6hwMseM/eKScqOXG1VqPEjtbXx2XdqECZ8AJu64i6iaH1oMIcjxQtepZMHqMh/sKh1565oA23cFO5DttgXeEfyUBQe6R4lILi7m6IFapyPN3jL4+y4ggS/4VFVS02QPaQYZmTNnor2PPbOlMkq0mZO0D81MFk5ou1Np2zOGASq96/pa0Gi58BxyEZGCLbJlTe5v5dQnGHL3/f5BmIxduer7nUOvrEb+EdarxxwNHHRLB484j0W7GVQ/g6WVzvOGd1uAMdYfrW5Djw1W42Kv150eSh3RJg54Kr5EsoUidrz982Z+lX</ds:X509Certificate> </ds:X509Data> </KeyInfo> </ds:Signature> <Subject> %%%%% The NameID Format is transient which is what CUCM expects <NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" NameQualifier="http://WinServer2016.sckiewer.lab/adfs/com/adfs/service/trust" SPNameQualifier="1cucm1251.sckiewer.lab">SCKIEWER\admin</NameID> <SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"> %%%%% You have an InResponseTo value that matches our SAML request, so you can correlate a given assertion to a SAML request <SubjectConfirmationData InResponseTo="s29fd87c888ef6a4bc8c48d7e7087a8aeb997dd76f" NotOnOrAfter="2021-04-30T13:06:03.891Z" Recipient="https://1cucm1251.sckiewer.lab:8443/ssosp/saml/SSO/alias/1cucm1251.sckiewer.lab"/> </SubjectConfirmation> </Subject> %%%%% You can see here that this assertion is only to be considered valid from 13:01:03:891-14:01:03:891 on 8/30/19 <Conditions NotBefore="2021-04-30T13:01:03.891Z" NotOnOrAfter="2021-04-30T14:01:03.891Z"> <AudienceRestriction> <Audience>1cucm1251.sckiewer.lab</Audience> </AudienceRestriction> </Conditions> %%%%% AttributeStatement is a required section that provides the ID of the user (admin in this case) and the attribute type <AttributeStatement> <Attribute Name="uid"> <AttributeValue>admin</AttributeValue> </Attribute> </AttributeStatement> <AuthnStatement AuthnInstant="2021-04-30T13:01:03.844Z" SessionIndex="_23d2b89f-7e75-4dc8-b154-def8767a391c"> <AuthnContext> <AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</AuthnContextClassRef> </AuthnContext> </AuthnStatement> </Assertion> XML Representation
```

### Helpful CLI Commands

- utils sso disable - This allows you to disable SSO if it is not functional

- utils sso status - This shows the current status of SSO on the node

- utils sso recovery-url enable - This allows you to disable the recovery URL

- utils sso recovery-url disable - This allows you to enable the recovery URL

- show samltrace level - This shows the current log level for SSO logs

- set samltrace level - This allows you to set the log level for SSO logs.  This needs to be set to DEBUG in order for us to effectively troubleshoot issues.

### Change from AssertionConsumerServiceURL to AssertionConsumerServiceIndex

When Cluster wide SSO was added in CUCM 11.5, CUCM no longer writes the AssertionConsumerService (ACS) URL in the SAML request. Instead, CUCM writes the AssertionConsumerServiceIndex. See these snippets from a SAML request:

CUCM pre 11.5.1:

```
AssertionConsumerServiceURL=" https://1cucm1101.sckiewer.lab:443/ssosp/saml/SSO/alias/1cucm1101.sckiewer.lab"
```

CUCM 11.5.1 and up:

```
AssertionConsumerServiceIndex="0"
```

In 11.5 and higher, CUCM expects the IdP to use the ACS Index # from the request in order to look up the ACS URL from the metadata file that was uploaded during the configuration process. This CUCM metadata snippet shows the POST URL (of the Publisher) associated with index 0:

```
<md:AssertionConsumerService index="0" Location="https://cucm14.sckiewer.lab:8443/ssosp/saml/SSO/alias/cucm14.sckiewer.lab" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"/>
```

There is no workaround to change this behavior and the IdP must use the ACS Index values rather than the ACS URL. More information can be found here, Cisco bug ID CSCvc56596 .

## Common Issues

### Unable to Access OS Administration or Disaster Recovery

In CUCM 12.x, the Cisco Unified OS Administration and Disaster Recovery System web applications utilize SSO. If log in attempts to these applications fail with a 403 error after you enable SSO, it is likely due to the CUCM platform being unable to find the user ID. This occurs because these applications do not reference the enduser table used by CM Administration, Serviceability, and Reporting. Because of this, the user ID that the IdP has authenticated does not exist on the CUCM platform side so CUCM returns a 403 Forbidden. This document details how to add the appropriate users into the system so that platform applications use SSO successfuly.

### NTP Failure

SSO is time-sensitive because the IdP attaches a 'validity timeframe' to assertions. In order to verify whether the time is the issue in your case, you can look for this section in the SSO logs:

```
2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - Time Valid?:true
2021-04-30 09:01:04,090 DEBUG [http-bio-8443-exec-85] authentication.SAMLAuthenticator - SAML Authenticator:ProcessResponse. End of time validation
```

If you find Time Valid?:false in your SSO logs, investigate the Conditions section of the assertion to identify the timeframe that the assertion must be considered valid:

```
<Conditions NotBefore="2021-04-30T13:01:03.891Z" NotOnOrAfter="2021-04-30T14:01:03.891Z"> <AudienceRestriction> <Audience>1cucm1251.sckiewer.lab</Audience> </AudienceRestriction> </Conditions>
```

You can see in the example snippet that this assertion is only valid from 13:01:03:8917 to 14:01:03:8917 on 4/30/2021. In a failure scenario, refer to the time that CUCM received this assertion and verify that it is within the validity period from the assertion. If the time that CUCM processed the assertion is outside the validity period, this is the cause of your issue. Ensure that CUCM and the IdP both sync to the same NTP server since SSO is very time-sensitive.

### Invalid Attribute Statement

Refer to the analysis of the assertion here and see the note about the attribute statement. Cisco Unified Communications products require an attribute statement to be provided by the IdP, but sometimes the IdP does not send one. For reference, this is a valid AttributeStatement:

```
<AttributeStatement>
<Attribute Name="uid">
<AttributeValue>admin</AttributeValue>
</Attribute>
</AttributeStatement>
```

If you see an assertion from the IdP, but the attribute statement is omitted, work with the vendor of your IdP software to make the necessary changes so that it provides this statement. The fix differs based on the IdP and in some scenarios, more information can be sent in this statement than you see in the snippet. As long as there is an Attribute Name set to uid and an AttributeValue that matches a user with the correct privileges in the CUCM database, the log in is successful.

### Two Signing Certificates - AD FS

This issue is specific to Microsoft AD FS. When the signing certificate on AD FS is close to expiration, the Windows Server automatically generates a new certificate, but leave the old certificate in place until it expires. When this occurs, the AD FS metadata contains two signing certificates. The error message you can see when you attempt to run the SSO test during this timeframe is, Error while processing SAML response .

Note: Error while processing SAML response can also be presented for other issues so do not assume that this is your issue if you see this error.  Be sure to check the SSO logs to verify.

If you see this error, review the SSO logs and look for this:

```
2018-12-26 13:49:59,581 ERROR [http-bio-443-exec-45] authentication.SAMLAuthenticator - Error while processing saml response The signing certificate does not match what's defined in the entity metadata.
com.sun.identity.saml2.common.SAML2Exception: The signing certificate does not match what's defined in the entity metadata.
```

This error indicates that the IdP metadata imported into CUCM contains a signing certificate that does not match what the IdP used in this SAML exchange. This error usually occurs because AD FS has two signing certificates.  When the original cert is close to expiration, AD FS automatically generates a new certificate.  You must download a new metadata file from AD FS, verify that it only has one signing and encryption certificate and import it into CUCM. Other IdPs also have signing certificates that need to be updated so it is possible that someone updated it manually but simply has not imported the new metadata file that contains the new certificate to CUCM.

If you encounter the errors mentioned:

- If you use AD FS, refer to Cisco bug ID CSCuj66703

- If you do NOT use AD FS, collect a new metadata file from the IdP and import it into CUCM

### Invalid Status code in Response

This is a common error in deployments with AD FS:

```
Invalid Status code in Response. This may be caused by a configuration error in the IDP. Please check the IDP logs and configuration.
```

In almost all cases, this is an issue with the claim rule on the AD FS side. Paste the rule into notepad first, add your entityIDs, and then paste the rule from notepad into AD FS. In some scenarios, a copy/paste directly from your email or browser can omit some of the punctuation and cause a syntax error.

Another common issue is with the claim rule is that the capitalization of either the IdP or SP FQDNs does not match the entityID in the metadata files. Check the Event Viewer logs on the Windows Server to determine if this is your issue.

You can see in the image that the Requested NameID is 1cucm1251.sckiewer.lab while the Actual NameID is 1CUCM1251.sckiewer.lab.  The Requested NameID must match the entityID in the SP metadata file while the Actual NameID is set in the claim rule.  To fix this issue, I need to update the claim rule with a lower case FQDN for the SP.

### SSO Status Mismatch Between CLI & GUI

In some cases, utils sso status and the GUI can show different information with regard to whether SSO is enabled or disabled.  The easiest way to fix this is to disable and re-enable SSO. There are quite a few files and references that update through the enablement process, so it is not feasible to try to manually update all of those files.  In most cases, you can log into the GUI and disable and re-enable with no issues, however, it is possible to see this error when you try to access the publisher via Recovery URL or the main link:

You can check the GUI to see if the recovery URL is an option and you can also check the utils sso status output from the CLI:

```
admin:utils sso status
SSO Status: SAML SSO Enabled
IdP Metadata Imported Date = Fri Apr 09 09:09:00 EDT 2021
SP Metadata Exported Date = Fri Apr 02 15:00:42 EDT 2021
SSO Test Result Date = Fri Apr 09 09:10:39 EDT 2021
SAML SSO Test Status = passed
Recovery URL Status = enabled
Entity ID = http://WinServer2016.sckiewer.lab/adfs/services/trust
```

Next, Check the process node table.  In this example, you can see that SSO is disabled in the database (see the tkssomode value for 1cucm1251.sckiewer.lab on the far right):

```
admin:run sql select pkid,name,tkssomode from processnode pkid                                     name                   tkssomode ====================================     ==================     ========= 00000000-1111-0000-0000-000000000000     EnterpriseWideData        0 04bff76f-ba8c-456e-8e8f-5708ce321c20     1cucm1251.sckiewer.lab    0 admin:run sql select * from typessomode
enum name       moniker
==== ========== ===================
0    Disable    SSO_MODE_DISABLE
1    Agent Flow SSO_MODE_AGENT_FLOW
2    SAML       SSO_MODE_SAML
```

In order to fix this, set the tkssomode field on the process node table back to 2 so that you can log in via the recovery URL:

```
admin:run sql update processnode set tkssomode='2' where name ='1cucm1251.sckiewer.lab'
Rows: 1 admin:run sql select pkid,name,tkssomode from processnode pkid                                     name                   tkssomode ====================================     ==================     ========= 00000000-1111-0000-0000-000000000000     EnterpriseWideData        0 04bff76f-ba8c-456e-8e8f-5708ce321c20     1cucm1251.sckiewer.lab    2
```

At this point, test the Recovery URL and proceed with a Disable > Re-enable of SSO which triggers CUCM to update all of the references in the system.

## Related Information

- SAML SSO Deployment Guide for Cisco Unified Communications Applications, Release 12.5(1)

- Security Assertion Markup Language (SAML) V2.0 Technical Overview

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

05-Aug-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Aug-2021 | Initial Release |