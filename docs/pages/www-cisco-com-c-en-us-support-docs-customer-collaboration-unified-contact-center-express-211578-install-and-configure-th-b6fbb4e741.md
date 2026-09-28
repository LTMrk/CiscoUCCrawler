---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-211578-install-and-configure-th-b6fbb4e741
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/211578-Install-and-Configure-the-Shibboleth-Ide.html
retrieved_at: 2026-08-16T20:55:02.080508+00:00
---

Install and Configure the Shibboleth Identity Provider (IdP) for Cisco Identity Service (IdS) to enable SSO

# Install and Configure the Shibboleth Identity Provider (IdP) for Cisco Identity Service (IdS) to enable SSO

Updated: August 13, 2017

Document ID: 211578

Contents

## Contents

## Introduction

This document describes the configuration on the OpenAM Identity Provider (IdP) to enable Single Sign On (SSO).

Cisco IdS Deployment Models

Co-resident with CUIC and LD for 2k deployments.

Standalone for 4k and 12k deployments.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Contact Center Express (UCCX) Release 11.6 or Cisco Unified Contact Center Enterprise Release 11.6 or Packaged Contact Center Enterprise (PCCE) Release 11.6 as applicable.

Note : This document references the configuration with respect to the Cisco Identitify Service (IdS) and the Identity Provider (IdP). The document references UCCX in the screenshots and examples, however the configuration is similar with respect to the Cisco Identitify Service (UCCX/UCCE/PCCE) and the IdP.

### Components Used

This document is not restricted to specific software and hardware versions. The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Install

Shibboleth is an open-source project that provides Single Sign-On capabilities and allows sites to make informed authorization decisions for individual access of protected online resources in a privacy-preserving manner. It supports Security Assertion Markup Language (SAML2). IdS is a SAML2 client and expected to support Shibboleth with minimal or no changes in IdS. In 11.6, IdS is qualified to work with Shibboleth IdP.

Note : This document references Shibboleth release 3.3.0 as a part of the qualification with SSO

### System Requirements

Ubuntu 14.0.4

java version "1.8.0_121"

Please refer the wiki for installation of Shibboleth

https://wiki.shibboleth.net/confluence/display/IDP30/Installation

## Configure

### Integrate with an LDAP server

To integrate an LDAP server with shibboleth, the fields need to be updated in $ shibboleth_home /conf/ldap.properties where $shibboleth_home (default is /opt/shibboleth-idp) refers to the install directory which is used at the installation of shibboleth.

For more details, refer:

https://wiki.shibboleth.net/confluence/display/IDP30/LDAPAuthnConfiguration

### Sample Configuration File

# Time in milliseconds to wait for responses

#idp.authn.LDAP.responseTimeout                 = PT3S

## SSL configuration, either jvmTrust, certificateTrust, or keyStoreTrust

#idp.authn.LDAP.sslConfig                       = certificateTrust

## If using certificateTrust above, set to the trusted certificate's path

idp.authn.LDAP.trustCertificates                = %{idp.home}/credentials/ldap-server.crt

## If using keyStoreTrust above, set to the truststore path

idp.authn.LDAP.trustStore                       = %{idp.home}/credentials/ldap-server.truststore

## Return attributes during authentication

#idp.authn.LDAP.returnAttributes                 = userPrincipalName, sAMAccountName

idp.authn.LDAP.returnAttributes                  = *

## DN resolution properties ##

# Search DN resolution, used by anonSearchAuthenticator, bindSearchAuthenticator

# for AD: CN=Users,DC=example,DC=org

idp.authn.LDAP.baseDN                           = CN=users,DC=cisco,DC=com

idp.authn.LDAP.subtreeSearch                   = true

*idp.authn.LDAP.userFilter                       = (sAMAccountName={user})*

# bind search configuration

# for AD: idp.authn.LDAP.bindDN=adminuser @domain .com

idp.authn.LDAP.bindDN                           = administrator @cisco .com

idp.authn.LDAP.bindDNCredential                 = Cisco @123

# Format DN resolution, used by directAuthenticator, adAuthenticator

# for AD use idp.authn.LDAP.dnFormat=%s @domain .com

#idp.authn.LDAP.dnFormat                        = %s @adfsserver .cisco.com

# LDAP attribute configuration, see attribute-resolver.xml

# Note, this likely won't apply to the use of legacy V2 resolver configurations

idp.attribute.resolver.LDAP.ldapURL             = %{idp.authn.LDAP.ldapURL}

idp.attribute.resolver.LDAP.connectTimeout      = %{idp.authn.LDAP.connectTimeout:PT3S}

idp.attribute.resolver.LDAP.responseTimeout     = %{idp.authn.LDAP.responseTimeout:PT3S}

idp.attribute.resolver.LDAP.baseDN              = %{idp.authn.LDAP.baseDN:undefined}

idp.attribute.resolver.LDAP.bindDN              = %{idp.authn.LDAP.bindDN:undefined}

idp.attribute.resolver.LDAP.bindDNCredential    = %{idp.authn.LDAP.bindDNCredential:undefined}

idp.attribute.resolver.LDAP.useStartTLS         = %{idp.authn.LDAP.useStartTLS: true }

idp.attribute.resolver.LDAP.trustCertificates   = %{idp.authn.LDAP.trustCertificates:undefined}

idp.attribute.resolver.LDAP.searchFilter        = (sAMAccountName=$resolutionContext.principal)

### Allow requests from all clients

To ensure that requests from all clients reach, changes are required in "$shibboleth_home/conf/access-control.xml"

<entry key="AccessByIPAddress"> <bean id="AccessByIPAddress" parent="shibboleth.IPRangeAccessControl" p:allowedRanges="#{ {'127.0.0.1/32', '0.0.0.0/0' , '::1/128', '10.78.93.103/32'} }" /> </entry>

Add '0.0.0.0/0' to the allowed ranges. This allows requests from any ip range.

### Configure Shibboleth to integrate with IdS

#### Secure Hash Algorithm (SHA1) and encryption configuration in IdS

To configure IdS to default to SHA1,  open "$shibboleth_home/conf/idp.properties" and set:

idp.signing.config = shibboleth.SigningConfiguration.SHA1

This configuration can also be changed:

idp.encryption.optional = true

If you set it to true, failure to locate an encryption key to use, when enabled, won't result in request failure . This h elps to do encryption "opportunistically", that is, to encrypt whenever possible (a compatible key is found in the peer's metadata to encrypt with) but to skip encryption otherwise.

#### Configure uid and user_principal to the SAML Response

The AttributeDefinition is added in "$shibboleth_home/conf/attribute-resolver.xml" to map sAMAccountName and userPrincipalName to the to uid and user_principal in the SAML response.

In addition, add the ldap connector settings with the tag <DataConnector>.

Note : ReturnAttributes needs to be specified with value " sAMAccountName userPrincipalName ".

Note : LDAPProperty is mandatory in case if there is an integration with a Active Directory (AD).

```
<AttributeDefinition xsi:type="Simple" id="ciscoUPN" sourceAttributeID="userPrincipalName">
 <Dependency ref="LDAP" />
 <AttributeEncoder xsi:type="SAML1String" name="user_principal" />
 <AttributeEncoder xsi:type="SAML2String" name="user_principal" friendlyName="user_principal" />
</AttributeDefinition>
 
<AttributeDefinition xsi:type="Simple" id="ciscoUID" sourceAttributeID="sAMAccountName">
 <Dependency ref="LDAP" />
 <AttributeEncoder xsi:type="SAML1String" name="uid" />
 <AttributeEncoder xsi:type="SAML2String" name="uid" friendlyName="uid" />
</AttributeDefinition>
 
    <DataConnector id="LDAP" xsi:type="LDAPDirectory"
     ldapURL="ldap://adfsserver.cisco.com"
     baseDN="CN=users,DC=cisco,DC=com"
     principal="administrator@cisco.com"
     principalCredential="<cred>">
        <FilterTemplate>
            <![CDATA[
                %{idp.attribute.resolver.LDAP.searchFilter}
            ]]>
        </FilterTemplate>
      <ReturnAttributes>sAMAccountName userPrincipalName</ReturnAttributes>
      <LDAPProperty name="java.naming.referral" value="follow"/>
    </DataConnector>
```

Incorporate the changes in "$shibboleth_home/conf/attribute-filter.xml"

```
<PolicyRequirementRule xsi:type="ANY" />
 
 
        <AttributeRule attributeID="ciscoUID">
            <PermitValueRule xsi:type="ANY" />
        </AttributeRule>
 
        <AttributeRule attributeID="ciscoUPN">
            <PermitValueRule xsi:type="ANY" />
        </AttributeRule>
```

Change the "$shibboleth_home/conf/saml-nameid.xml" toinclude

```
<bean parent="shibboleth.SAML2AttributeSourcedGenerator"
        p:format="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent"   
        p:attributeSourceIds="#{ {'ciscoUPN'} }" />
<bean parent="shibboleth.SAML2AttributeSourcedGenerator"
        p:format="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent"   
        p:attributeSourceIds="#{ {'ciscoUID'} }" />
```

#### IdP metadata

IdP metadata is available in the folder  " $shibboleth_home/metadata " . The idp-metadata.xml file can be uploaded to IdS via the Application Programming Interface (API)

PUT https://<idshost>: <idsport> /ids/v1/config/idpmetadata

where idsport is not a configurable entity and the value is "8553"

Warning : S hibboleth metadata can contain 2 signing certificates, the general signing certificate and the backchannel. Navigate to the file idp-backchannel.crt in "$shibboleth_home/credentials" to identify the backchannel certificate . If the back channel certificate is available in the metadata, You should remove the back channel certificate from the metadata xml before upload to IdS. This is because fedlet 12.0 library that IdS uses supports only one certifcate in the metadata. If more than one signing certificate is available, fedlet uses the first available certificate.

#### Configure metadata providers

We need to configure the metadata providers with the entry  in $shibboleth_home/metadata-providers.xml.

```
<MetadataProvider id="smart-86"  xsi:type="FilesystemMetadataProvider" metadataFile="/opt/shibboleth-idp/SP/sp.xml"/>
```

where "id" attribute can be any unique name.

This entry indicates that a metadata provider is registered with the given id and the metadata is available in the specified file /opt/shibboleth-idp/SP/sp.xml.

Service Provider (SP) metadata of IdS must be copied to the metadataFile specified in the entry.

Note : SP metadata of IdS can be retrieved via GET https://<idshost>:< idsport >/ids/v1/config/spmetadata, where idsport is not a configurable entity and the value is "8553".

## Further Configuration for SSO

This document describes the configuration from the IdP aspect for SSO to integrate with the Cisco Identity Service. For further details, refer to the individual product configuration guides:

- UCCX

- UCCE

- PCCE

### Revision History

1.0

17-Aug-2017

Initial Release

### Contributed by Cisco Engineers

Arundeep Nagaraj

Cisco TAC

Balakrishnan Doraisamy

Cisco Engineering

Venkatesh Vedurumudi

Cisco Engineering

### This Document Applies to These Products

- Unified Contact Center Express

| Product | Deployment |
|---|---|
| UCCX | Co-resident |
| PCCE | Co-resident with CUIC (Cisco Unified Intelligence Center) and LD (Live Data) |
| UCCE | Co-resident with CUIC and LD for 2k deployments. Standalone for 4k and 12k deployments. |

| Component | Details |
|---|---|
| Shibboleth version | v3.3.0 |
| Download location | http://shibboleth.net/downloads/identity-provider/ |
| Install platform | Ubuntu 14.0.4 java version "1.8.0_121" |
| Lightweight Directory Access Protocol (LDAP) version | Active Directory 2.0 |
| Shibboleth webserver | Apache Tomcat/8.5.12 |

| Field | Expected Value | Description |
|---|---|---|
| idp.authn.LDAP.trustCertificates | A resource to load trust anchors from, usually a local file in ${idp.home}/credentials where idp.home is an environment variable exported as JAVA_OPTS in setenv.sh | %{idp.home}/credentials/ldap-server.crt |
| idp.authn.LDAP.trustStore | A resource to load a Java keystore that contains trust anchors, usually a local file in %{idp.home}/credentials | %{idp.home}/credentials/ldap-server.truststore |
| idp.authn.LDAP.returnAttributes | The comma separated list of LDAPAttributes that needs to be returned. If you want to return all attributes, add "*". | * |
| idp.authn.LDAP.baseDN | The baseDN at which the LDAP search needs to be performed | CN=users,DC=cisco,DC=com |
| idp.authn.LDAP.subtreeSearch | Whether to search recursively | true |
| idp.authn.LDAP.userFilter | LDAP search filter | (sAMAccountName={user})* |
| idp.authn.LDAP.bindDN | DN to bind with when search is performed | administrator@cisco.com |
| idp.authn.LDAP.bindDNCredential | Password to bind with when search is performed |  |
| idp.authn.LDAP.dnFormat | A formatting string to generate the user DNs to authenticate | %s@adfsserver.cisco.com (%s@domainname) |
| idp.authn.LDAP.authenticator | Controls the workflow for how authentication occurs against the LDAP | bindSearchAuthenticator |
| idp.authn.LDAP.ldapURL | Connection URI for LDAP directory |  |

| # Time in milliseconds to wait for responses #idp.authn.LDAP.responseTimeout                 = PT3S ## SSL configuration, either jvmTrust, certificateTrust, or keyStoreTrust #idp.authn.LDAP.sslConfig                       = certificateTrust ## If using certificateTrust above, set to the trusted certificate's path idp.authn.LDAP.trustCertificates                = %{idp.home}/credentials/ldap-server.crt ## If using keyStoreTrust above, set to the truststore path idp.authn.LDAP.trustStore                       = %{idp.home}/credentials/ldap-server.truststore ## Return attributes during authentication #idp.authn.LDAP.returnAttributes                 = userPrincipalName, sAMAccountName idp.authn.LDAP.returnAttributes                  = * ## DN resolution properties ## # Search DN resolution, used by anonSearchAuthenticator, bindSearchAuthenticator # for AD: CN=Users,DC=example,DC=org idp.authn.LDAP.baseDN                           = CN=users,DC=cisco,DC=com idp.authn.LDAP.subtreeSearch                   = true *idp.authn.LDAP.userFilter                       = (sAMAccountName={user})* # bind search configuration # for AD: idp.authn.LDAP.bindDN=adminuser @domain .com idp.authn.LDAP.bindDN                           = administrator @cisco .com idp.authn.LDAP.bindDNCredential                 = Cisco @123 # Format DN resolution, used by directAuthenticator, adAuthenticator # for AD use idp.authn.LDAP.dnFormat=%s @domain .com #idp.authn.LDAP.dnFormat                        = %s @adfsserver .cisco.com # LDAP attribute configuration, see attribute-resolver.xml # Note, this likely won't apply to the use of legacy V2 resolver configurations idp.attribute.resolver.LDAP.ldapURL             = %{idp.authn.LDAP.ldapURL} idp.attribute.resolver.LDAP.connectTimeout      = %{idp.authn.LDAP.connectTimeout:PT3S} idp.attribute.resolver.LDAP.responseTimeout     = %{idp.authn.LDAP.responseTimeout:PT3S} idp.attribute.resolver.LDAP.baseDN              = %{idp.authn.LDAP.baseDN:undefined} idp.attribute.resolver.LDAP.bindDN              = %{idp.authn.LDAP.bindDN:undefined} idp.attribute.resolver.LDAP.bindDNCredential    = %{idp.authn.LDAP.bindDNCredential:undefined} idp.attribute.resolver.LDAP.useStartTLS         = %{idp.authn.LDAP.useStartTLS: true } idp.attribute.resolver.LDAP.trustCertificates   = %{idp.authn.LDAP.trustCertificates:undefined} idp.attribute.resolver.LDAP.searchFilter        = (sAMAccountName=$resolutionContext.principal) |
|---|

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Aug-2017 | Initial Release |