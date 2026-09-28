---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-4eee6564d6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_01110.html
retrieved_at: 2026-09-01T15:41:37.220959+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

Chapter: Corporate and Personal Directory Setup

## Chapter: Corporate and Personal Directory Setup

# Corporate and Personal Directory Setup

## Personal Directory Setup

The Personal Directory allows a user to store a set of personal numbers.

Personal Directory consists of the following feature:

Personal Address Book (PAB)

Users can use these methods to access Personal Directory features:

From a web browser—Users can access the PAB and Speed Dials features from the Configuration Utility web page.

From the Cisco IP Phone—Choose Contacts to search the corporate directory or the user personal directory.

To configure Personal Directory from a web browser, users must access their Configuration Utility. You must provide users
                           with a URL and sign-in information.

## LDAP Configuration

The Cisco IP Phone supports Lightweight Directory Access Protocol (LDAP) v3. LDAP Corporate Directory Search allows a user
                              to search a specified LDAP directory for a name, phone number, or both. LDAP-based directories, such as Microsoft Active Directory
                              2003 and OpenLDAP-based databases, are supported.

Users access LDAP from the Directory menu on their IP phone. An LDAP search returns up to 20 records.

The instructions in this section assume that you have the following equipment and services:

An LDAP server, such as OpenLDAP or Microsoft Active Directory Server 2003.

### Prepare the LDAP Corporate Directory Search

Click Admin Login > advanced > Voice > System .

In the IPv4 Settings section, in the Primary DNS field, enter the IP address of the DNS server.

This step is required only if you are using Active Directory with authentication set to MD5.

In the Optional Network Configuration section, in the Domain field, enter the LDAP domain.

This step is required only if you are using Active Directory with authentication set to MD5.

Some sites might not deploy DNS internally and instead use Active Directory 2003. In this case, it is not necessary to enter
                                             a Primary DNS address and an LDAP Domain. However, with Active Directory 2003, the authentication method is restricted to
                                             Simple.

Click the Phone tab.

In the LDAP section, use the LDAP Dir Enable drop-down list box to choose Yes .

This action enables LDAP and causes the name that is defined in the Corp Dir Name field to appear in the phone directory.

Configure the LDAP fields as described in LDAP .

Click Submit All Changes .

## Configure BroadSoft Settings

The BroadSoft directory service enables users to search and view their personal, group, or enterprise contacts. This application
                              feature uses BroadSoft's Extended Services Interface (XSI).

To improve security, the phone firmware places access restrictions on the host server and directory name entry fields.

User login credentials: The phone uses the XSI user id and password.

SIP credentials: The register name and password of the SIP account registered on the phone. For this method, the phone can
                                       use the XSI user ID along with the SIP authentication credentials for the authentication.

In the phone web page, navigate to Admin Login > advanced > Voice > Phone .

In the XSI Service section, choose Yes from the Directory Enable drop down list box.

Set up the fields as described in XSI Phone Service .

Click Submit All Changes .

## Configure the XML Directory Service

In the Phone Web page, click Admin Login > advanced > Voice > Phone .

In the XML Directory Service Name field, enter the name of XML directory.

In the XML Directory Service URL field, enter the url where  XML directory is located.

In the XML User Name field, enter the username of XML service.

In the XML Password field, enter the password of XML service.

Click Submit All Changes .

| Step 1 | Click Admin Login > advanced > Voice > System . |
|---|---|
| Step 2 | In the IPv4 Settings section, in the Primary DNS field, enter the IP address of the DNS server. This step is required only if you are using Active Directory with authentication set to MD5. |
| Step 3 | In the Optional Network Configuration section, in the Domain field, enter the LDAP domain. This step is required only if you are using Active Directory with authentication set to MD5. Some sites might not deploy DNS internally and instead use Active Directory 2003. In this case, it is not necessary to enter
                                             a Primary DNS address and an LDAP Domain. However, with Active Directory 2003, the authentication method is restricted to
                                             Simple. |
| Step 4 | Click the Phone tab. |
| Step 5 | In the LDAP section, use the LDAP Dir Enable drop-down list box to choose Yes . This action enables LDAP and causes the name that is defined in the Corp Dir Name field to appear in the phone directory. |
| Step 6 | Configure the LDAP fields as described in LDAP . |
| Step 7 | Click Submit All Changes . |

| Step 1 | In the phone web page, navigate to Admin Login > advanced > Voice > Phone . |
|---|---|
| Step 2 | In the XSI Service section, choose Yes from the Directory Enable drop down list box. |
| Step 3 | Set up the fields as described in XSI Phone Service . |
| Step 4 | Click Submit All Changes . |

| Step 1 | In the Phone Web page, click Admin Login > advanced > Voice > Phone . |
|---|---|
| Step 2 | In the XML Directory Service Name field, enter the name of XML directory. |
| Step 3 | In the XML Directory Service URL field, enter the url where  XML directory is located. |
| Step 4 | In the XML User Name field, enter the username of XML service. |
| Step 5 | In the XML Password field, enter the password of XML service. |
| Step 6 | Click Submit All Changes . |