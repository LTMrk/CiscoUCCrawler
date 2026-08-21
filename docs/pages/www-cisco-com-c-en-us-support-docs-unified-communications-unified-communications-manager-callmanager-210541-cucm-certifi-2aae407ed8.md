---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-210541-cucm-certifi-2aae407ed8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/210541-CUCM-Certificate-Management-and-Change-N.html
retrieved_at: 2026-08-21T00:00:37.114119+00:00
---

CUCM Certificate Management and Change Notification

# CUCM Certificate Management and Change Notification

### Download Options

Updated: April 9, 2017

Document ID: 210541

Contents

## Contents

## 1. Introduction

This document describe that Certificate Management in Cisco Unified Operating System is very important component of CUCM and VOS itself because many applications and features rely on certificates for example: TVS, CAPF, Security by Default, or Unified Serviceability pages.CertMgmt provides a single repository of certificates and APIs for other components in order to easily include the security and secure data transfer(TLS).

The "Cisco Certificate Change Notification" service has been introduced mainly to sychronize some certificates across the nodes in the cluster and is monitored by ServM. It makes the certificate provision easier and faster for the administrator in bigger deployments.

Contributed by Mateusz Olszowy, Cisco TAC Engineer.

## 2. How certificates are stored ?

Certs are stored in the file system as well as in the database and CN service keeps sync of them between nodes. File system certificates are given higher precedence than DB certificates.

DB Tables:

- CERTIFICATE - stores all certificate details like subject, issuer,serial,certificate in PEM format etc.

- CERTIFICATESERVICECERTIFICATEMAP  - mapp between certificate and certificate type for example CallManager-Trust,CAPF-Trust

- CERTIFICATEHASHMAP - mapp between certificate and hash of the certificate

- CERTIFICATEPROCESSNODEMAP - mapp between certificate and processnode

- CERTIFICATETRUSTROLEMAP - mapp between certificate and role_enum

- TYPECERTIFICATESERVICE - maps enums you can find in CERTIFICATESERVICECERTIFICATEMAP to the certificate types (i.e. tomcat, tomcat-trust, callmanager etc.)

Storage in the file system:

- certs : public key (X509Certificate - Own certificate) ( .der and .pem format with .description) and also in pkcs-12 keystore format.

- keys : private key and passphrases and CSR.

- trust-certs : all trusted certificates(.der & .pem format) and also in PKCS-12 keystore format.

Sample paths:

/usr/local/cm/.security/CallManager/

/usr/local/cm/.security/CAPF

/usr/local/platform/.security/tomcat

Trust-certs subdirectory contains symbolic links which refer to .pem files with special names consist of openSSL hash and typically .0 extension which can be used as iterator when you have the same hash generated. Refer to the example below:

```
[root@cucmpub trust-certs]# pwd /usr/local/cm/.security/CallManager/trust-certs [root@cucmpub trust-certs]# ls -l cucmpub.pem -rwxr-xr-x 1 certbase ccmbase 993 Mar 15  2013 cucmpub.pem [root@cucmpub trust-certs]# openssl x509 -noout -hash -in cucmpub.pem 5eb51e07 [root@cucmpub trust-certs]# ls -l 5eb51e07.0 lrwxrwxrwx 1 certbase ccmbase 11 May 13 17:16 5eb51e07.0 -> cucmpub.pem
```

## 3. CertMgmt and Certificate CN design overview

When the certificate is upload under OS Administration page, the file in .PEM and .DER format is written to the file system and DB tables are updated.

These certificates get next replicated through DB replication to the other nodes in the cluster.

Some types of certificates are picked up by the Cisco Certificate Change Notification process on the remote nodes and uploaded on the file system by that same process.

The Cisco Certificate Change Notification process gets notified for changes on these tables: CERTIFICATE and CERTIFICATESERVICECERTIFICATEMAP.

The certs picked up by Cisco Certificate Change Notification are configured in follow configuration file /usr/local/platform/conf/certM.conf:

CHANGE_NOTIFICATION_UNIT=tomcat,tomcat-trust,directory-trust,CallManager,Phone-SAST-trust,CallManager-trust

Additionally, the service runs every 30 min(1800 sec) by default to keep all certs in sync, this timer is as well configured in above file: CN_SYNC_TIMER=1800

Once uploaded, replicated to remote nodes and uploaded there as well onto the file system the OS admin page will display the certificates.

It's important to note that the OS Admin page and all other services read the certificates from the file system and not from the DB.

## 4. Examples

In this section you will consider 3 different scenarios of certificate management.

For each scenario you follow the process in detail and use screenshots and logs.

For these scenario's you use a 2 node cluster with CUCM version 9.1.2.10000-28.

Legend : CM - Certificate Management (logs can be found under 'file list activelog platform/log/certMgmtXXXXX.log') certCN - Certificate Change Notification Service (logs can be found under 'file list activelog platform/log/certCNXXXXX.log')

Examples based on CUCM cluster 9.1.2.10000-28, two nodes: PUB, IP:10.48.46.29, HOSTNAME:CUCM861 SUB, IP: 10.48.46.30, HOSTNAME:CUCM861s

Certificates are presented in the OS Admin page with the serial number in decimal format. DB stores these number in HEX. In order to convert serial numbers between HEX/DEC you can use this online tool .

Log snippets contain some comments (bolded, starting with '##').

### 4.A. Insert a new tomcat-trust certificate.

In the first scenario you upload a certificate into the tomcat-trust through the OS Admin page, below steps will occur on both nodes in the cluster :

a. Manually upload the certificate

b. Certificate will be stored in the filesystem by CM. c. Certificate will be inserted into DB by CM. d. Certificate will be replicated via DB replication to the subscriber. CertCN on both nodes (pub and sub) will be notified about the change. It won't perform an action on the pub node.

e. CertCN on sub node will import certificate to the filesystem and add it to the keystore.

f. After these steps the certificate will be visable on the GUI under OS Admin page.

a. When certificate upload from PEM file takes place. Please follow below screenshots:

Serial number of our new cert: Dec: 162503161730851213217569888696899890998 Hex: 7A40F8743A793B44FE802B5F3E1E6F36

Certificate is written into the filesystem (you will follow this process in the next steps)

```
[root@ CUCM861 tomcat]# pwd /usr/local/platform/.security/tomcat [root@CUCM861 tomcat]# ls -la
total 40
drwxr-xr-x 5 root     root    4096 Apr  4 12:47 .
drwxr-xr-x 5 root     root    4096 Apr  4 12:47 ..
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 23:36 certs drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 23:36 keys
drwxr-xr-x 2 certbase ccmbase 4096 Aug  4 15:21 trust-certs [root@CUCM861 tomcat]# ls -la certs
total 48
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 23:36 .
drwxr-xr-x 5 root     root    4096 Apr  4 12:47 ..
-rwxr-xr-x 1 certbase ccmbase  939 Aug  2 23:36 tomcat.der
-rwxr-xr-x 1 certbase ccmbase   64 Aug  2 23:36 tomcat.description
-rwxr-xr-x 1 certbase ccmbase 2598 Aug  2 23:36 tomcat.keystore
-rwxr-xr-x 1 certbase ccmbase 1326 Aug  2 23:36 tomcat.pem [root@CUCM861 tomcat]# ls -la trust-certs
total 140
drwxr-xr-x 2 certbase ccmbase 4096 Aug  4 15:21 .
drwxr-xr-x 5 root     root    4096 Apr  4 12:47 ..
lrwxrwxrwx 1 certbase ccmbase   11 Aug  4 15:21 101f99a6.0 -> CUCM861.pem
lrwxrwxrwx 1 certbase ccmbase   10 Aug  4 15:21 25ffab9b.0 -> CUCM9X.pem lrwxrwxrwx 1 certbase ccmbase   42 Aug  4 15:21 7e0370f0.0 -> VeriSign_Class_3_Secure_Server_CA_-_G3.pem
-rwxr-xr-x 1 certbase ccmbase  939 Aug  2 23:36 CUCM861.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 23:36 CUCM861.description
-rwxr-xr-x 1 certbase ccmbase 1326 Aug  2 23:36 CUCM861.pem
-rwxr-xr-x 1 certbase ccmbase  941 Aug  2 22:51 CUCM861s.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 22:51 CUCM861s.description
-rwxr-xr-x 1 certbase ccmbase 1330 Aug  2 22:51 CUCM861s.pem
-rwxr-xr-x 1 certbase ccmbase  953 Aug  4 15:21 CUCM9X.der -rwxr-xr-x 1 certbase ccmbase   45 Aug  4 15:21 CUCM9X.description -rwxr-xr-x 1 certbase ccmbase 1346 Aug  4 15:21 CUCM9X.pem lrwxrwxrwx 1 certbase ccmbase   12 Aug  4 15:21 d0aacffb.0 -> CUCM861s.pem
-rwxr-xr-x 1 certbase ccmbase 4939 Aug  4 15:21 tomcat-trust.keystore
-rwxr-xr-x 1 certbase ccmbase 1520 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.der
-rwxr-xr-x 1 certbase ccmbase   44 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.description
-rwxr-xr-x 1 certbase ccmbase 2114 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.pem [root@CUCM861 tomcat]# md5sum trust-certs/CUCM9X.pem a0a2e12a42e4bbbf10655c9b299839d9 trust-certs/CUCM9X.pem
```

As you can see the new certificate is stored in trust-certs directory. Common Name (which equals to the hostname of CUCM node) has been used as a file name. It has been saved as .pem and .der. Symbolic link 25ffab9b.0 -> CUCM9X.pem has been also created and certificate has been added to the tomcat-trust.keystore. Finally, you compare md5 checksum of the cert file on the sub node to prove that this is the same certificate.

b. Let's take a closer look at how it happen that the certificate has been saved into the file system. From the CM log (comments in snippet, bolded, starts with ##):

```
2014-08-04 15:21:21,116 INFO [main] - log4j configuration successful.
2014-08-04 15:21:21,239 INFO [main] - IN -- CertMgr.java - mainInternal(args) - 
2014-08-04 15:21:21,241 INFO [main] - decode ## import is the operation that will be performed 2014-08-04 15:21:21,241 INFO [main] - op:import
2014-08-04 15:21:21,241 INFO [main] - type:trust-certs
2014-08-04 15:21:21,241 INFO [main] - unit:tomcat-trust
2014-08-04 15:21:21,241 INFO [main] - src-cert:%2Fusr%2Flocal%2Fplatform%2Fupload%2Fcerts%2Ftomcat.pem
2014-08-04 15:21:21,241 INFO [main] - cert-dir:%2Fusr%2Flocal%2Fplatform%2F.security%2Ftomcat%2Ftrust-certs
2014-08-04 15:21:21,241 INFO [main] - key-dir:%2Fusr%2Flocal%2Fplatform%2F.security%2Ftomcat%2Fkeys
2014-08-04 15:21:21,241 INFO [main] - rootCA-cert:Dummy+Root+cert
2014-08-04 15:21:21,241 INFO [main] - trust-dir:%2Fusr%2Flocal%2Fplatform%2F.security%2Ftomcat%2Ftrust-certs
2014-08-04 15:21:21,241 INFO [main] - logfile:%2Fvar%2Flog%2Factive%2Fplatform%2Flog%2Fcert-mgmt.log
2014-08-04 15:21:21,241 INFO [main] - resultfile:%2Fvar%2Flog%2Factive%2Fplatform%2Flog%2Fcertde-info.xml
2014-08-04 15:21:21,241 INFO [main] - description:Signed+Certificate
2014-08-04 15:21:21,294 INFO [main] - Parsed information
2014-08-04 15:21:21,294 INFO [main] - OrgName: CISCO
2014-08-04 15:21:21,294 INFO [main] - OrgUnit: TAC
2014-08-04 15:21:21,294 INFO [main] - Location: KRAKOW
2014-08-04 15:21:21,294 INFO [main] - Country: PL
2014-08-04 15:21:21,294 INFO [main] - State: MALOPOLSKA
2014-08-04 15:21:21,294 INFO [main] - Hostname: CUCM861
2014-08-04 15:21:21,294 INFO [main] - AlternateHostname: null
2014-08-04 15:21:21,294 INFO [main] - Domain Name: 
2014-08-04 15:21:21,294 INFO [main] - IPAddress: 10.48.46.29
2014-08-04 15:21:21,296 INFO [main] - In parseXML()
2014-08-04 15:21:21,359 INFO [main] - FQDN Name retrived by InetAddress : CUCM861
2014-08-04 15:21:21,360 INFO [main] - CN: CUCM861
2014-08-04 15:21:21,360 INFO [main] - Temp before mod is 
2014-08-04 15:21:21,361 INFO [main] - Temp afer mod is TAC
2014-08-04 15:21:21,361 INFO [main] - Temp in else is TAC
2014-08-04 15:21:21,361 INFO [main] - Temp before mod is 
2014-08-04 15:21:21,361 INFO [main] - Temp afer mod is TAC
2014-08-04 15:21:21,361 INFO [main] - Temp in else is TAC
2014-08-04 15:21:21,361 INFO [main] - OuFields are TAC
2014-08-04 15:21:21,361 DEBUG [main] - Field after encoding: TAC
2014-08-04 15:21:21,361 DEBUG [main] - Field after encoding: CISCO
2014-08-04 15:21:21,362 DEBUG [main] - Field after encoding: KRAKOW
2014-08-04 15:21:21,362 DEBUG [main] - Field after encoding: MALOPOLSKA
2014-08-04 15:21:21,362 DEBUG [main] - Field after encoding: PL
2014-08-04 15:21:21,366 INFO [main] - OU field is :TAC
2014-08-04 15:21:21,366 INFO [main] - SubjectDN :: CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL
2014-08-04 15:21:21,366 INFO [main] - IN -- CertMgr.java - getCertMgrObj(unit) - tomcat-trust
2014-08-04 15:21:21,386 INFO [main] - OUT -- CertMgr.java - getCertMgrObj - com.cisco.cpi.certMgmt.manager.TomcatCertMgr@162dbb6
2014-08-04 15:21:21,386 INFO [main] - Dummy loadProperties
2014-08-04 15:21:21,386 INFO [main] - IN -- CertMgr.java - doOp(info) - 
2014-08-04 15:21:21,387 INFO [main] - IN -- DefaultCertMgr.java - importCert(info) - 
decode:     true
op:         import
unit:       tomcat-trust
keystoreUnit:tomcat-trust
logFile:    /var/log/active/platform/log/cert-mgmt.log
resultFile: /var/log/active/platform/log/certde-info.xml
keyDir:     /usr/local/platform/.security/tomcat/keys
certDir:    /usr/local/platform/.security/tomcat/trust-certs
srcCert:    /usr/local/platform/upload/certs/tomcat.pem
type:       trust-certs
rootCACert: Dummy Root cert
trustDir:   /usr/local/platform/.security/tomcat/trust-certs
DNAME:      CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL
description:Signed Certificate
isDBInsert:true

2014-08-04 15:21:21,387 INFO [main] - IN -- DefaultCertMgr.java - loadInputCert(info) - 
2014-08-04 15:21:22,246 DEBUG [main] - Loading RSA providers explicitly...
2014-08-04 15:21:25,159 DEBUG [main] - RSA providers are loaded explicitly...
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.1=JsafeJCE
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.2=RsaJsse
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.3=BC
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.4=SUN
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.5=SunRsaSign
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.6=SunJSSE
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.7=SunJCE
2014-08-04 15:21:25,159 DEBUG [main] - New security.provider.8=SunJGSS
2014-08-04 15:21:25,160 DEBUG [main] - New security.provider.9=SunSASL
2014-08-04 15:21:25,160 DEBUG [main] - New security.provider.10=XMLDSig
2014-08-04 15:21:25,160 DEBUG [main] - New security.provider.11=SunPCSC
2014-08-04 15:21:25,160 INFO [main] - IN -- RSACryptoEngine.java - loadCertificates(..) - 
2014-08-04 15:21:25,160 INFO [main] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:25,772 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:25,772 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificates - 
2014-08-04 15:21:25,772 INFO [main] - OUT -- DefaultCertMgr.java - loadInputCert - Successfully loaded input cert
2014-08-04 15:21:25,772 DEBUG [main] - Checking validity of cert
2014-08-04 15:21:25,772 INFO [main] - Verifying certificate L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
2014-08-04 15:21:25,772 INFO [main] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-04 15:21:25,773 DEBUG [main] - parseCNfromDN( certSubjDN: 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL')
2014-08-04 15:21:25,773 DEBUG [main] - Truncating CN 'CUCM9X,OU=TAC,O=Cisco Systems,C=PL' -> 'CUCM9X'
2014-08-04 15:21:25,773 INFO [main] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-04 15:21:25,773 DEBUG [main] - Parsed CN 'CUCM9X' from DN 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL'
2014-08-04 15:21:25,773 INFO [main] - trying to load cert from trust store ::/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem
2014-08-04 15:21:25,773 INFO [main] - cert not available in trust store ::L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
2014-08-04 15:21:25,773 INFO [main] - IN -- DefaultCertMgr.java - importTrustCert(info, cert) - 
2014-08-04 15:21:25,773 INFO [main] - IN -- DefaultCertMgr.java - saveToTrustStore(info, cert) - 
2014-08-04 15:21:25,773 INFO [main] - IN -- DefaultCertMgr.java - saveTrustCert(cert, targetDir, certType) - 
2014-08-04 15:21:25,773 INFO [main] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-04 15:21:25,773 DEBUG [main] - parseCNfromDN( certSubjDN: 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL')
2014-08-04 15:21:25,773 DEBUG [main] - Truncating CN 'CUCM9X,OU=TAC,O=Cisco Systems,C=PL' -> 'CUCM9X'
2014-08-04 15:21:25,773 INFO [main] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-04 15:21:25,773 DEBUG [main] - Parsed CN 'CUCM9X' from DN 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL'
2014-08-04 15:21:25,773 INFO [main] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-04 15:21:25,773 DEBUG [main] - parseCNfromDN( certSubjDN: 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL')
2014-08-04 15:21:25,774 DEBUG [main] - Truncating CN 'CUCM9X,OU=TAC,O=Cisco Systems,C=PL' -> 'CUCM9X'
2014-08-04 15:21:25,774 INFO [main] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-04 15:21:25,774 DEBUG [main] - Parsed CN 'CUCM9X' from DN 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL' ## cert will be stored in filesystem with below filename (which is CN retrieved from certificate) 2014-08-04 15:21:25,774 DEBUG [main] - target filename for imported cert: 'CUCM9X.pem'
2014-08-04 15:21:25,774 DEBUG [main] - existing certificate with same filename not found.
2014-08-04 15:21:25,774 DEBUG [main] - Saving PEM encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem'
2014-08-04 15:21:25,776 INFO [main] - IN -- CryptoUtil.java - saveAsPEM(..) - File : /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem
2014-08-04 15:21:25,796 INFO [main] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-04 15:21:25,796 DEBUG [main] - Saving DER encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.der'
2014-08-04 15:21:25,797 INFO [main] - OUT -- DefaultCertMgr.java - saveTrustCert - ## saving it to key store 2014-08-04 15:21:25,797 INFO [main] - IN -- TomcatCertMgr.java - saveToKeyStore(..) - 
2014-08-04 15:21:25,797 INFO [main] - IN -- RSACryptoEngine.java - saveToKeyStore(keystoreFile, keystorePass, x509Certificate, alias) - 
2014-08-04 15:21:25,797 INFO [main] - IN -- RSACryptoEngine.java - loadKeyStore(keystoreFile, keystorePass) - 
2014-08-04 15:21:25,981 INFO [main] - OUT -- RSACryptoEngine.java - loadKeyStore - 
2014-08-04 15:21:25,981 INFO [main] - Size of the keystore before import is : 3
2014-08-04 15:21:25,982 INFO [main] - Importing certificate : CUCM9X
2014-08-04 15:21:26,023 INFO [main] - Size of the keystore after import is : 4
2014-08-04 15:21:26,023 INFO [main] - OUT -- RSACryptoEngine.java - saveToKeyStore - 
2014-08-04 15:21:26,023 INFO [main] - OUT -- TomcatCertMgr.java - saveToKeyStore - 
2014-08-04 15:21:26,023 DEBUG [main] - TrustCert description filename : 'CUCM9X.description'
2014-08-04 15:21:26,024 INFO [main] - IN -- DefaultCertMgr.java - createDescriptionFile(name, description) - 
2014-08-04 15:21:26,024 INFO [main] - description is :Signed Certificate
2014-08-04 15:21:26,024 INFO [main] - OUT -- DefaultCertMgr.java - createDescriptionFile - 
2014-08-04 15:21:26,024 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-04 15:21:26,024 DEBUG [main] - setOwnershipAndPermissions : CUCM9X.description
2014-08-04 15:21:26,025 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description'
2014-08-04 15:21:26,025 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:26,025 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown certbase /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description
2014-08-04 15:21:26,049 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:26,049 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description'
2014-08-04 15:21:26,049 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:26,049 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp ccmbase /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description
2014-08-04 15:21:26,064 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:26,065 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description'
2014-08-04 15:21:26,065 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:26,065 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod 755 /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description
2014-08-04 15:21:26,068 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:26,068 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-04 15:21:26,068 INFO [main] - OUT -- DefaultCertMgr.java - saveToTrustStore - ## certificate will be stored in trust-certs directory 2014-08-04 15:21:26,069 INFO [main] - trustdir ::/usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:26,069 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:26,069 DEBUG [main] - Executing command from Util.sysExec :  python /usr/local/platform/bin/c_rehash.py /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:26,449 INFO [main] - OUT -- Util.java - sysExec - ## setting necessary permissions 2014-08-04 15:21:26,449 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-04 15:21:26,449 DEBUG [main] - setOwnershipAndPermissions : trust-certs
2014-08-04 15:21:26,449 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-04 15:21:26,449 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:26,449 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:26,460 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:26,460 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-04 15:21:26,460 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:26,460 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:26,471 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:26,472 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-04 15:21:26,472 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:26,472 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:26,478 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:26,478 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-04 15:21:26,478 INFO [main] - IN -- CertUtil.java - populateCertInfo(cert, opInfo, certFilePemLocation) - 
2014-08-04 15:21:26,480 INFO [main] - IN -- CertUtil.java - getHostName(..) - 
2014-08-04 15:21:26,480 INFO [main] - OUT -- CertUtil.java - getHostName - CUCM861
2014-08-04 15:21:26,480 INFO [main] - IN -- CryptoUtil.java - saveAsPEM(..) - 
2014-08-04 15:21:26,482 INFO [main] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-04 15:21:26,483 INFO [main] - OUT -- CertUtil.java - populateCertInfo -
```

c. Certificate has been stored in the filesystem, now it needs to be inserted into DB. This operation is performed also by CM API.

```
2014-08-04 15:21:26,484 INFO [main] - IN -- CertDBAction.java - insertCertificateInDB(certFiletoStore, info) - 
2014-08-04 15:21:26,485 INFO [main] - ## certificate has been identified as tomcat-trust one DBParameters ... 
PKID :		null
CN :		L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
serialNo :	7a40f8743a793b44fe802b5f3e1e6f36
hostName :	CUCM861
issuerName :	L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
Certificate :	Not Printing huge Certificate String..
IPV4Address :	10.48.46.29
IPV6Address :	
TimeToLive :	NULL
UNIT :		tomcat-trust
TYPE :		trust-certs
ROLE :		null
RoleMoniker :	null
RoleEnum :null
SERVICE :		null
ServiceMoniker :	null
ServiceEnum :0

2014-08-04 15:21:26,485 INFO [main] - DB - Certifciate Store Plugin Handler is :com.cisco.ccm.certmgmt.db.CertDBImpl
2014-08-04 15:21:26,697 DEBUG [main] - Connection Initialized to localnode. Connection HashCode:896033  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:26,697 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:26,712 DEBUG [main] - Try to get a connection from pool
2014-08-04 15:21:26,712 DEBUG [main] - getting local connection from Pool
2014-08-04 15:21:26,714 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:26,715 DEBUG [main] - There are currently 0 connection pool entries
2014-08-04 15:21:26,719 DEBUG [main] - Checking if connection limit has been reached for database
2014-08-04 15:21:26,720 DEBUG [main] - Connecting to publisher so max number of connections allowed is 100
2014-08-04 15:21:26,720 DEBUG [main] - Number of connections in use is 0
2014-08-04 15:21:26,720 DEBUG [main] - There is currently 1 connection pool entry
2014-08-04 15:21:26,720 DEBUG [main] - Number of available connections in pool: 0
2014-08-04 15:21:27,411 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@135da43> to connection list
2014-08-04 15:21:27,411 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@135da43> as used
2014-08-04 15:21:27,411 DEBUG [main] - Got connection from pool
2014-08-04 15:21:27,418 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:27,422 DEBUG [main] - Closing the resultset.
2014-08-04 15:21:27,423 DEBUG [main] - Closing the connection. Connection HashCode:896033  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:27,423 DEBUG [main] - Attempting to close connection
2014-08-04 15:21:27,423 DEBUG [main] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:27,423 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-04 15:21:27,447 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@135da43> from connection list
2014-08-04 15:21:27,452 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@135da43> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:27,453 INFO [main] - Connection/Statement/Resultset is closed properly. ## service is checking current enums for TYPETRUSTROLEMAP (for tomcat-trust it is ## ROLE_APPLICATION_SERVER=7) and TYPESERVICEROLEMAP (for tomcat-trust it will be ## tomcat-trust=6) 2014-08-04 15:21:27,453 INFO [main] - TYPETRUSTROLEMAP ::{TRUST_ROLE_DATA_SERVICE=24, TRUST_ROLE_PROVISIONING_SERVICE=23, TRUST_ROLE_SERVICEABILITY=27, TRUST_ROLES_CALLMANAGER_TFTP=2, PHONE_TRUST_ROLES_FIREWALL=6, ROLE_APPLICATION_SERVER=7, TRUST_ROLES_SAST=0, ROLE_SIGNALING_CALL_CONTROL=22, TRUST_ROLES_CALLMANAGER=1, TRUST_ROLES_UNKNOWN=255, TRUST_ROLE_NETWORK_ELEMENT=25, TRUST_ROLES_SRST=5, ROLE_CERTIFICATE_AUTHORITY=20, TRUST_ROLE_VPN=26, TRUST_ROLES_CAPF=4, TRUST_ROLES_TFTP=3, ROLE_AUTHENTICATION_AUTHORIZATION=21}
2014-08-04 15:21:27,453 INFO [main] - TYPESERVICEROLEMAP ::{Phone-VPN-trust=2, CallManager=3, Phone-CTL-trust=15, tomcat-trust=6, TVS=11, ipsec-trust=8, Phone-trust=1, Phone-SAST-trust=14, tomcat=5, userlicensing-trust=16, CAPF=9, ipsec=7, CAPF-trust=10, CallManager-trust=4, TVS-trust=12, directory-trust=13}
2014-08-04 15:21:27,453 INFO [main] - unitRoleMap ::{Phone-VPN-trust=[TRUST_ROLE_VPN], CallManager=[TRUST_ROLES_CALLMANAGER_TFTP, TRUST_ROLES_SAST], Phone-CTL-trust=[ROLE_APPLICATION_SERVER], tomcat-trust=[ROLE_APPLICATION_SERVER], TVS=[ROLE_AUTHENTICATION_AUTHORIZATION], ipsec-trust=[], Phone-trust=[ROLE_APPLICATION_SERVER], Phone-SAST-trust=[TRUST_ROLES_SAST, TRUST_ROLES_TFTP], tomcat=[ROLE_APPLICATION_SERVER], userlicensing-trust=[], CAPF=[TRUST_ROLES_CAPF], ipsec=[ROLE_APPLICATION_SERVER], CAPF-trust=[], CallManager-trust=[], TVS-trust=[], directory-trust=[]}
2014-08-04 15:21:27,453 INFO [main] - commonTrustStoreMap ::{}
2014-08-04 15:21:27,456 DEBUG [main] - Connection Initialized to Publisher. Connection HashCode:7962652  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:27,456 INFO [main] - IN -- CertDBImpl.java - insertCertificate(certInfo, con) - 
2014-08-04 15:21:27,456 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-04 15:21:27,456 DEBUG [main] - Try to get a connection from pool
2014-08-04 15:21:27,456 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:27,456 DEBUG [main] - There is currently 1 connection pool entry
2014-08-04 15:21:27,456 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@135da43> to connection list
2014-08-04 15:21:27,456 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@135da43> as used
2014-08-04 15:21:27,457 DEBUG [main] - Got connection from pool
2014-08-04 15:21:27,459 INFO [main] - IN -- CertDBImpl.java - populateRoleEnumServiceEnum(certInfo) - 
2014-08-04 15:21:27,459 INFO [main] - UNIT ::: tomcat-trust
2014-08-04 15:21:27,459 INFO [main] - role ::: [ROLE_APPLICATION_SERVER]
2014-08-04 15:21:27,459 INFO [main] - roleEnum ::: [7]
2014-08-04 15:21:27,459 INFO [main] - service ::: null
2014-08-04 15:21:27,459 INFO [main] - serviceEnum ::: 6
2014-08-04 15:21:27,459 INFO [main] - OUT -- CertDBImpl.java - populateRoleEnumServiceEnum - 
2014-08-04 15:21:27,489 INFO [main] - IN -- CertDBUtil.java - getProcessNodeId(con, hostName, ipAddress, fqdn) - 
2014-08-04 15:21:27,489 INFO [main] - getProcessNodeId Query :SELECT PKID,NAME FROM PROCESSNODE WHERE UPPER(NAME)=UPPER("CUCM861") OR UPPER(NAME)=UPPER("10.48.46.29") OR UPPER(NAME)=UPPER("CUCM861")
2014-08-04 15:21:27,489 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-04 15:21:27,497 INFO [main] - ProcessNodeId:13f4b0d9-0bae-429a-a86e-625336a35bb6
2014-08-04 15:21:27,498 DEBUG [main] - Closing the resultset.
2014-08-04 15:21:27,498 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:27,498 INFO [main] - OUT -- CertDBUtil.java - getProcessNodeId - 
2014-08-04 15:21:27,498 INFO [main] - IN -- CertDBImpl.java - getPkidOfCertificate(hash, serverName, con) - 
2014-08-04 15:21:27,498 DEBUG [main] - GetPKID Query :SELECT A.PKID FROM CERTIFICATE A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND B.HASH = "a9Ww/WeDmBnnHHncUCqOGCz4O9g="
2014-08-04 15:21:27,498 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-04 15:21:27,522 DEBUG [main] - Closing the resultset.
2014-08-04 15:21:27,539 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:27,539 INFO [main] - OUT -- CertDBImpl.java - getPkidOfCertificate - 
2014-08-04 15:21:27,539 DEBUG [main] - INSERT FLAG :: isCertUpdate=false :: doNothing=false ## you can see an insert query that is used to upload the certificate into the CERTIFICATE ## table 2014-08-04 15:21:27,543 DEBUG [main] - INSERT/UPDATE Query of CERTIFICATE : INSERT INTO CERTIFICATE VALUES ("4152b36b-002e-68ac-711d-c373fa940779","CUCM861","L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL","L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL","7a40f8743a793b44fe802b5f3e1e6f36","-----BEGIN CERTIFICATE-----
MIIDtTCCAp2gAwIBAgIQekD4dDp5O0T+gCtfPh5vNjANBgkqhkiG9w0BAQsFADBq
MQswCQYDVQQGEwJQTDEWMBQGA1UEChMNQ2lzY28gU3lzdGVtczEMMAoGA1UECxMD
VEFDMQ8wDQYDVQQDEwZDVUNNOVgxEzARBgNVBAgTCk1hbG9wb2xza2ExDzANBgNV
BAcTBktyYWtvdzAeFw0xNDA4MDQxMzE5MDdaFw0xOTA4MDMxMzE5MDZaMGoxCzAJ
BgNVBAYTAlBMMRYwFAYDVQQKEw1DaXNjbyBTeXN0ZW1zMQwwCgYDVQQLEwNUQUMx
DzANBgNVBAMTBkNVQ005WDETMBEGA1UECBMKTWFsb3BvbHNrYTEPMA0GA1UEBxMG
S3Jha293MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy0IoIzjyDpaC
/gGMTwsJUaoyvAdxwRhAUvsro7lqr+rON+HQApZBFdTw9qL0Uv+cAvCTKfXsl4QJ
Il6vxcMWBqwF6S1OIwAE9DyhY2ZkuRiLX0O24eRnf30FePH9jl5eVVUwl4CKaVS3
xa9yq6yaYa4o7PE6QypK9SDIKm2IHQ6j1HX26ZXLKLJJmHhFK5cnFbo+7UUzdtiE
u3+XBQtnTQsS/bM7oVbcsyqYuaQddrT5Zrzo9QEjx4BuM62929jmEcgmI/OQ5O4s
aS+dEjx9u+g9rmrNuvZ0pgtsHHU3IijePZCnKm5JE4oiC1qI2zUwTecvkYk+MSZ0
XeXyN2WrkQIDAQABo1cwVTALBgNVHQ8EBAMCArwwJwYDVR0lBCAwHgYIKwYBBQUH
AwEGCCsGAQUFBwMCBggrBgEFBQcDBTAdBgNVHQ4EFgQUt6dlJJ8fTevcRHxEQKG9
fYV3SPswDQYJKoZIhvcNAQELBQADggEBALA9jn5CWQHMA+Eg9C6QUyLqKNN7Lshy
loSSE7Nn5RsIB4PQ9cD8Wvl7bzRYp70yFoQ1B+Z8U4FgSCWKbGAGAubMyb/6rXLW
uUyCrXhy48XrMDVJ3CqMHXhR5tjY9Sn1ziXdJe4AwvBRAzId4QrIdNuE6pUSLrrh
915dRYvrXpIXgeQJ2pGU+qo12CSaySSPTeFhNDh8U2yjw/tg8H1Amnv0VW+TY+9U
B6TC04iElmwuOr9tJ6+LyZI7emRmNkv5On5PZcK4RQz5NOefVXdSHLpwAuW+Q8Eb
mt7BbxyyZl5KbaSdAMvkYRbnuwDJyZWMJPOWftVcmRlRPk2/yDb959o=
-----END CERTIFICATE-----
","10.48.46.29","",NULL)
2014-08-04 15:21:27,543 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-04 15:21:27,766 INFO [main] - IN -- CertDBImpl.java - updateCertificateHashMap(certInfo, con) - ## hash for this certificate is being updated in teh CERTIFICATEHASMAP 2014-08-04 15:21:27,766 DEBUG [main] - Update query of CERTIFICATEHASHMAP :UPDATE CERTIFICATEHASHMAP SET HASH = "a9Ww/WeDmBnnHHncUCqOGCz4O9g=" WHERE FKCERTIFICATE = "4152b36b-002e-68ac-711d-c373fa940779" 
2014-08-04 15:21:27,766 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-04 15:21:27,771 INFO [main] - OUT -- CertDBImpl.java - updateCertificateHashMap - ## cert is in the DB, but there is still no info about the type of this certificate. ## Corresponding tables: CERTIFICATESERVICECERTIFICATEMAP, CERTIFICATETRUSTROLEMAP and ## CERTIFICATEPROCESSNODEMAP need to be updated with correct info. For each one CM will ## check if you have any entries in the DB with the PKID of certificate you just added. If ## no, proper entry is inserted 2014-08-04 15:21:27,771 INFO [main] - IN -- CertDBImpl.java - insertCertSrvCertMap(certInfo, con) - 
2014-08-04 15:21:27,771 INFO [main] - IN -- CertDBImpl.java - checkExistingCertificateServiceMapping(certInfo, serviceEnum, con) - ## checked here 2014-08-04 15:21:27,771 DEBUG [main] - checkExistingTrustCertificateForService Query :SELECT PKID,FKCERTIFICATE, TKCERTIFICATESERVICE FROM CERTIFICATESERVICECERTIFICATEMAP  WHERE FKCERTIFICATE = "4152b36b-002e-68ac-711d-c373fa940779" AND TKCERTIFICATESERVICE= "6"
2014-08-04 15:21:27,771 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-04 15:21:27,774 DEBUG [main] - Closing the resultset.
2014-08-04 15:21:27,774 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:27,774 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertificateServiceMapping - ## inserted here 2014-08-04 15:21:27,774 DEBUG [main] - Certificate to be inserted in CERTIFICATESERVICECERTIFICATEMAP table :tomcat-trust ::PKID :4152b36b-002e-68ac-711d-c373fa940779 ::toInsertInCertSrvMap:true
2014-08-04 15:21:27,774 DEBUG [main] - Insert query of CERTIFICATESERVICECERTIFICATEMAP :INSERT INTO CERTIFICATESERVICECERTIFICATEMAP VALUES (newid(),"4152b36b-002e-68ac-711d-c373fa940779",6)
2014-08-04 15:21:27,775 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-04 15:21:27,778 DEBUG [main] - CertService mapping entry already exists..
2014-08-04 15:21:27,778 INFO [main] - OUT -- CertDBImpl.java - insertCertSrvCertMap - 
2014-08-04 15:21:27,778 INFO [main] - IN -- CertDBImpl.java - insertCertTrustRoleMap(certInfo, log, con) - 
2014-08-04 15:21:27,779 INFO [main] - IN -- CertDBImpl.java - checkExistingCertificateRoleMapping(certInfo, roleEnum, con) - ## checked here 2014-08-04 15:21:27,779 DEBUG [main] - checkExistingTrustCertificateForRole Query :SELECT PKID,FKCERTIFICATE, TKTRUSTROLE FROM CERTIFICATETRUSTROLEMAP WHERE FKCERTIFICATE = "4152b36b-002e-68ac-711d-c373fa940779" AND TKTRUSTROLE= "7"
2014-08-04 15:21:27,779 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-04 15:21:27,781 DEBUG [main] - Closing the resultset.
2014-08-04 15:21:27,781 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:27,781 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertificateRoleMapping - ## inserted here 2014-08-04 15:21:27,781 DEBUG [main] - Certificate to be inserted in CERTIFICATETRUSTROLEMAP table :tomcat-trust ::PKID :4152b36b-002e-68ac-711d-c373fa940779 ::toInsertInCertSrvMap:true
2014-08-04 15:21:27,781 DEBUG [main] - Insert query of CERTIFICATETRUSTROLEMAP :INSERT INTO CERTIFICATETRUSTROLEMAP VALUES (newid(),"4152b36b-002e-68ac-711d-c373fa940779",7)
2014-08-04 15:21:27,782 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-04 15:21:27,868 INFO [main] - OUT -- CertDBImpl.java - insertCertTrustRoleMap - 
2014-08-04 15:21:27,868 INFO [main] - IN -- CertDBImpl.java - insertCertProcessNodeMap(certInfo, con) - 
2014-08-04 15:21:27,868 INFO [main] - IN -- CertDBImpl.java - checkExistingCertProcessNodeMapping(certInfo, con) - ## finally checked here 2014-08-04 15:21:27,868 DEBUG [main] - checkExistingCertProcessNodeMapping Query :SELECT PKID,FKCERTIFICATE, FKPROCESSNODE,SERVERNAME FROM CERTIFICATEPROCESSNODEMAP WHERE FKCERTIFICATE="4152b36b-002e-68ac-711d-c373fa940779" AND FKPROCESSNODE="13f4b0d9-0bae-429a-a86e-625336a35bb6" AND SERVERNAME="CUCM861"
2014-08-04 15:21:27,869 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-04 15:21:27,872 DEBUG [main] - Closing the resultset.
2014-08-04 15:21:27,872 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:27,872 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertProcessNodeMapping - ## and inserted here 2014-08-04 15:21:27,872 DEBUG [main] - Insert query of CERTIFICATEPROCESSNODEMAP :INSERT INTO CERTIFICATEPROCESSNODEMAP VALUES (newId(),"4152b36b-002e-68ac-711d-c373fa940779", "13f4b0d9-0bae-429a-a86e-625336a35bb6" , "CUCM861", "10.48.46.29" , "")
2014-08-04 15:21:27,872 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-04 15:21:27,879 INFO [main] - OUT -- CertDBImpl.java - insertCertProcessNodeMap - 
2014-08-04 15:21:27,930 DEBUG [main] - Connection committed for insertCertificate..
2014-08-04 15:21:27,930 DEBUG [main] - Insertion of Certificate in DB is Successful.
2014-08-04 15:21:27,930 INFO [main] - OUT -- CertDBImpl.java - insertCertificate - 
2014-08-04 15:21:27,930 DEBUG [main] - Closing the connection. Connection HashCode:7962652  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:27,930 DEBUG [main] - Attempting to close connection
2014-08-04 15:21:27,930 DEBUG [main] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:27,930 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-04 15:21:27,930 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@135da43> from connection list
2014-08-04 15:21:27,931 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@135da43> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:27,931 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:27,931 INFO [main] - DB - Generate Certificate operation in DB is successful
2014-08-04 15:21:27,931 INFO [main] - OUT -- CertDBAction.java - insertCertificateInDB - 
2014-08-04 15:21:27,931 INFO [main] - IN -- CryptoUtil.java - isOCSPEnabled(..) - 
2014-08-04 15:21:27,931 INFO [main] - IN -- CryptoUtil.java - getCertMonitorXmlParser(..) - 
2014-08-04 15:21:27,989 INFO [main] - OUT -- CryptoUtil.java - getCertMonitorXmlParser - 
2014-08-04 15:21:27,989 INFO [main] - OUT -- CryptoUtil.java - isOCSPEnabled - false
2014-08-04 15:21:27,990 DEBUG [main] - OCSP is not enabled. ## process of importing the cert to this node is finishing here. 2014-08-04 15:21:27,990 INFO [main] - Successfully imported trusted certificate with Subject DN:L&#61;Krakow,ST&#61;Malopolska,CN&#61;CUCM9X,OU&#61;TAC,O&#61;Cisco Systems,C&#61;PL
2014-08-04 15:21:27,990 INFO [main] - OUT -- DefaultCertMgr.java - importTrustCert - Successfully imported trusted certificate with Subject DN:L&#61;Krakow,ST&#61;Malopolska,CN&#61;CUCM9X,OU&#61;TAC,O&#61;Cisco Systems,C&#61;PL
2014-08-04 15:21:27,990 INFO [main] - result of import operations is ::Import of trust certificate is successful
2014-08-04 15:21:27,990 INFO [main] - OUT -- DefaultCertMgr.java - importCert - 
2014-08-04 15:21:27,990 INFO [main] - IN -- CertMgr.java - logResult(result, desc, resultFile) - 
2014-08-04 15:21:27,990 INFO [main] - CertMgmt Operation Result : null
2014-08-04 15:21:27,991 INFO [main] - OUT -- CertMgr.java - logResult - 
2014-08-04 15:21:27,991 INFO [main] - OUT -- CertMgr.java - doOp - 
2014-08-04 15:21:27,992 INFO [main] - OUT -- CertMgr.java - mainIntenal -
```

d. After certs are replicated, CertCN service on both nodes are notified about the change made in the DB. This can be seen in the logs. Below shows the log on the Publisher

```
## notification about the change comes, service is notified about change in CERTIFICATE and CERTIFICATESERVICECERTIFICATEMAP tables 2014-08-04 15:21:28,003 INFO [Thread-5] - IN - process. changeData &colon; 
2014-08-04 15:21:28,016 INFO [Thread-5] - Inside CERTIFICATE - I/U option..
2014-08-04 15:21:28,016 DEBUG [Thread-5] - Updated Data in CERTIFICATE ::<msg><type>DBL</type><table>certificate</table><tableid>41</tableid><action>I</action><time>1407158487</time><new><cdrserver>2</cdrserver><cdrtime>1407158486</cdrtime><pkid>4152b36b-002e-68ac-711d-c373fa940779</pkid><servername>CUCM861</servername><subjectname>L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL</subjectname><issuername>L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL</issuername><serialnumber>7a40f8743a793b44fe802b5f3e1e6f36</serialnumber><certificate></certificate><ipv4address>10.48.46.29</ipv4address><ipv6address></ipv6address><timetolive>NULL</timetolive><ifx_replcheck>6043699677659004930</ifx_replcheck></new></msg>
2014-08-04 15:21:28,016 DEBUG [Thread-5] - Certificate PKID : 4152b36b-002e-68ac-711d-c373fa940779 , ipAddress : 10.48.46.29 , OldSerialNo :  , NewSerialNo : 7a40f8743a793b44fe802b5f3e1e6f36
2014-08-04 15:21:28,017 INFO [Thread-5] - OUT - process.
2014-08-04 15:21:28,018 INFO [Thread-5] - IN - process. changeData &colon; 
2014-08-04 15:21:28,018 INFO [Thread-5] - Inside CERTIFICATESERVICECERTIFICATEMAP - I option..
2014-08-04 15:21:28,019 DEBUG [Thread-5] - Updated Data in CERTIFICATESERVICECERTIFICATEMAP ::<msg><type>DBL</type><table>certificateservicecertificatemap</table><tableid>44</tableid><action>I</action><time>1407158487</time><new><cdrserver>2</cdrserver><cdrtime>1407158487</cdrtime><pkid>798ff6e1-e1d6-42e5-a4e6-30d9d7360d6d</pkid><fkcertificate>4152b36b-002e-68ac-711d-c373fa940779</fkcertificate><tkcertificateservice>6</tkcertificateservice><ifx_replcheck>6043699681953972226</ifx_replcheck></new></msg>
2014-08-04 15:21:28,019 INFO [InsertThread --- 8] - IN -- CertKeystoreHandler.java - run() - 
2014-08-04 15:21:28,021 DEBUG [InsertThread --- 8] - InsertThread --- 8 -- START -- ## change is related to the PKID that has been assigned for the new certificate 2014-08-04 15:21:28,021 DEBUG [InsertThread --- 8] - DB Value UPDATE: 4152b36b-002e-68ac-711d-c373fa940779
2014-08-04 15:21:28,021 INFO [InsertThread --- 8] - IN -- CertKeystoreHandler.java - updateIntoKeystore() - 
2014-08-04 15:21:28,021 INFO [InsertThread --- 8] - IN -- CertDBImpl.java - getCertificate(certBash64SHA1:null --pkid:4152b36b-002e-68ac-711d-c373fa940779
2014-08-04 15:21:28,022 DEBUG [InsertThread --- 8] - Connection Initialized to localnode. Connection HashCode:14186201  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:28,022 DEBUG [InsertThread --- 8] - Select Query to getCertificate :SELECT A.*,B.HASH FROM CERTIFICATE  A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND A.PKID = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-04 15:21:28,022 DEBUG [InsertThread --- 8] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:28,022 DEBUG [InsertThread --- 8] - Try to get a connection from pool
2014-08-04 15:21:28,022 DEBUG [InsertThread --- 8] - getting local connection from Pool
2014-08-04 15:21:28,022 DEBUG [InsertThread --- 8] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:28,022 DEBUG [InsertThread --- 8] - There are currently 2 connection pool entries
2014-08-04 15:21:28,023 DEBUG [InsertThread --- 8] - Checking if connection limit has been reached for database
2014-08-04 15:21:28,023 DEBUG [InsertThread --- 8] - Connecting to publisher so max number of connections allowed is 100
2014-08-04 15:21:28,023 DEBUG [InsertThread --- 8] - Number of connections in use is 0
2014-08-04 15:21:28,023 DEBUG [InsertThread --- 8] - There are currently 2 connection pool entries
2014-08-04 15:21:28,023 DEBUG [InsertThread --- 8] - Number of available connections in pool: 0
2014-08-04 15:21:28,079 DEBUG [InsertThread --- 8] - Adding connection <com.informix.jdbc.IfxSqliConnect@162db76> to connection list
2014-08-04 15:21:28,079 DEBUG [InsertThread --- 8] - Marking connection <com.informix.jdbc.IfxSqliConnect@162db76> as used
2014-08-04 15:21:28,079 DEBUG [InsertThread --- 8] - Got connection from pool
2014-08-04 15:21:28,081 DEBUG [InsertThread --- 8] - Closing the resultset.
2014-08-04 15:21:28,081 DEBUG [InsertThread --- 8] - Closing the connection. Connection HashCode:14186201  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:28,081 DEBUG [InsertThread --- 8] - Attempting to close connection
2014-08-04 15:21:28,081 DEBUG [InsertThread --- 8] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:28,081 DEBUG [InsertThread --- 8] - removeConnectionFromConnectionList()
2014-08-04 15:21:28,081 DEBUG [InsertThread --- 8] - Removing connection <com.informix.jdbc.IfxSqliConnect@162db76> from connection list
2014-08-04 15:21:28,081 DEBUG [InsertThread --- 8] - Connection <com.informix.jdbc.IfxSqliConnect@162db76> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:28,082 INFO [InsertThread --- 8] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:28,082 DEBUG [InsertThread --- 8] - Connection released from CertDBImpl.getCertificate method.
2014-08-04 15:21:28,082 INFO [InsertThread --- 8] - OUT -- CertDBImpl.java - getCertificate - 
2014-08-04 15:21:28,082 INFO [InsertThread --- 8] - IN -- CertDBImpl.java - getCertUnitByPkid(pkid) - 
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - Connection Initialized to localnode. Connection HashCode:20337133  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - Select Query to getCertUnitByPkid :SELECT A.PKID, A.FKCERTIFICATE, A.TKCERTIFICATESERVICE, B.NAME UNIT FROM CERTIFICATESERVICECERTIFICATEMAP A, TYPECERTIFICATESERVICE B WHERE A.FKCERTIFICATE="4152b36b-002e-68ac-711d-c373fa940779" AND A.TKCERTIFICATESERVICE = B.ENUM
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - Try to get a connection from pool
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - getting local connection from Pool
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - There are currently 2 connection pool entries
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - Adding connection <com.informix.jdbc.IfxSqliConnect@162db76> to connection list
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - Marking connection <com.informix.jdbc.IfxSqliConnect@162db76> as used
2014-08-04 15:21:28,083 DEBUG [InsertThread --- 8] - Got connection from pool
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - Closing the resultset.
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - Closing the connection. Connection HashCode:20337133  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - Attempting to close connection
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - removeConnectionFromConnectionList()
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - Removing connection <com.informix.jdbc.IfxSqliConnect@162db76> from connection list
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - Connection <com.informix.jdbc.IfxSqliConnect@162db76> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:28,085 INFO [InsertThread --- 8] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:28,085 DEBUG [InsertThread --- 8] - Resultset released from CertDBImpl.getCertUnitByPkid method.
2014-08-04 15:21:28,085 INFO [InsertThread --- 8] - OUT -- CertDBImpl.java - getCertUnitByPkid - 
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - UNIT : tomcat-trust
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - CurrentIPAddress : 10.48.46.29
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - RemoteIPAddress : 10.48.46.29
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - OldSerialNo :
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - NewSerialNo :7a40f8743a793b44fe802b5f3e1e6f36
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - IN -- CertUtil.java - getListFromComaSeperatedStr(..) - 
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - OUT -- CertUtil.java - getListFromComaSeperatedStr - ## tomcat-trust is in scope of certCN for import but since it is already on the file ## system the service will nothing with that one. 2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - tomcat-trust --- is included unit for CN
2014-08-04 15:21:28,086 DEBUG [InsertThread --- 8] - Change notification not require on same node except tomcat cert.
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - tomcat-trust Certificate successfully updated in trust-store by Change Notification..
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - OUT -- CertKeystoreHandler.java - updateIntoKeystore - 
2014-08-04 15:21:28,086 DEBUG [InsertThread --- 8] - InsertThread --- 8 -- END --
2014-08-04 15:21:28,086 INFO [InsertThread --- 8] - OUT -- CertKeystoreHandler.java - run -
```

e. On the subscriber you see the same happens, certCN gets notified of the change and next import the certificate onto the file system, creates the symbolic links etc... This can be seen in below log:

```
## service is notified about the change in DB. Notifications are related to two tables: 2014-08-04 15:21:29,298 INFO [Thread-5] - IN - process. changeData &colon; 
2014-08-04 15:21:29,299 INFO [Thread-5] - Inside CERTIFICATE - I/U option.. ## CERTIFICATE one ... 2014-08-04 15:21:29,299 DEBUG [Thread-5] - Updated Data in CERTIFICATE ::<msg><type>DBL</type><table>certificate</table><tableid>41</tableid><action>I</action><time>1407158488</time><new><cdrserver>2</cdrserver><cdrtime>1407158487</cdrtime><pkid>4152b36b-002e-68ac-711d-c373fa940779</pkid><servername>CUCM861</servername><subjectname>L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL</subjectname><issuername>L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL</issuername><serialnumber>7a40f8743a793b44fe802b5f3e1e6f36</serialnumber><certificate></certificate><ipv4address>10.48.46.29</ipv4address><ipv6address></ipv6address><timetolive>NULL</timetolive><ifx_replcheck>6043699677659004930</ifx_replcheck></new></msg>
2014-08-04 15:21:29,299 DEBUG [Thread-5] - Certificate PKID : 4152b36b-002e-68ac-711d-c373fa940779 , ipAddress : 10.48.46.29 , OldSerialNo :  , NewSerialNo : 7a40f8743a793b44fe802b5f3e1e6f36
2014-08-04 15:21:29,299 INFO [Thread-5] - OUT - process.
2014-08-04 15:21:29,299 INFO [InsertThread --- 35] - IN -- CertKeystoreHandler.java - run() - 
2014-08-04 15:21:29,300 DEBUG [InsertThread --- 35] - InsertThread --- 35 -- START --
2014-08-04 15:21:29,300 DEBUG [InsertThread --- 35] - DB Value UPDATE: 4152b36b-002e-68ac-711d-c373fa940779
2014-08-04 15:21:29,300 INFO [InsertThread --- 35] - IN -- CertKeystoreHandler.java - updateIntoKeystore() - 
2014-08-04 15:21:29,300 INFO [InsertThread --- 35] - IN -- CertDBImpl.java - getCertificate(certBash64SHA1:null --pkid:4152b36b-002e-68ac-711d-c373fa940779
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - Connection Initialized to localnode. Connection HashCode:30607587  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - Select Query to getCertificate :SELECT A.*,B.HASH FROM CERTIFICATE  A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND A.PKID = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - Try to get a connection from pool
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - getting local connection from Pool
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - There are currently 2 connection pool entries
2014-08-04 15:21:29,301 DEBUG [InsertThread --- 35] - Checking if connection limit has been reached for database
2014-08-04 15:21:29,302 DEBUG [InsertThread --- 35] - Connecting to subscriber so max number of connections allowed is 100
2014-08-04 15:21:29,302 DEBUG [InsertThread --- 35] - Number of connections in use is 0
2014-08-04 15:21:29,302 DEBUG [InsertThread --- 35] - There are currently 2 connection pool entries
2014-08-04 15:21:29,302 DEBUG [InsertThread --- 35] - Number of available connections in pool: 0
2014-08-04 15:21:29,315 INFO [Thread-5] - IN - process. changeData &colon; 
2014-08-04 15:21:29,316 INFO [Thread-5] - Inside CERTIFICATESERVICECERTIFICATEMAP - I option.. ## ... and CERTIFICATESERVICECERTIFICATEMAP 2014-08-04 15:21:29,316 DEBUG [Thread-5] - Updated Data in CERTIFICATESERVICECERTIFICATEMAP ::<msg><type>DBL</type><table>certificateservicecertificatemap</table><tableid>44</tableid><action>I</action><time>1407158489</time><new><cdrserver>2</cdrserver><cdrtime>1407158487</cdrtime><pkid>798ff6e1-e1d6-42e5-a4e6-30d9d7360d6d</pkid><fkcertificate>4152b36b-002e-68ac-711d-c373fa940779</fkcertificate><tkcertificateservice>6</tkcertificateservice><ifx_replcheck>6043699681953972226</ifx_replcheck></new></msg>
2014-08-04 15:21:29,354 DEBUG [InsertThread --- 35] - Adding connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> to connection list
2014-08-04 15:21:29,355 DEBUG [InsertThread --- 35] - Marking connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> as used
2014-08-04 15:21:29,355 DEBUG [InsertThread --- 35] - Got connection from pool
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - Closing the resultset.
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - Closing the connection. Connection HashCode:30607587  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - Attempting to close connection
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - removeConnectionFromConnectionList()
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - Removing connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> from connection list
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - Connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:29,363 INFO [InsertThread --- 35] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:29,363 DEBUG [InsertThread --- 35] - Connection released from CertDBImpl.getCertificate method.
2014-08-04 15:21:29,363 INFO [InsertThread --- 35] - OUT -- CertDBImpl.java - getCertificate - 
2014-08-04 15:21:29,363 INFO [InsertThread --- 35] - IN -- CertDBImpl.java - getCertUnitByPkid(pkid) - 
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - Connection Initialized to localnode. Connection HashCode:29897942  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - Select Query to getCertUnitByPkid :SELECT A.PKID, A.FKCERTIFICATE, A.TKCERTIFICATESERVICE, B.NAME UNIT FROM CERTIFICATESERVICECERTIFICATEMAP A, TYPECERTIFICATESERVICE B WHERE A.FKCERTIFICATE="4152b36b-002e-68ac-711d-c373fa940779" AND A.TKCERTIFICATESERVICE = B.ENUM
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - Try to get a connection from pool
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - getting local connection from Pool
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - There are currently 2 connection pool entries
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - Adding connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> to connection list
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - Marking connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> as used
2014-08-04 15:21:29,364 DEBUG [InsertThread --- 35] - Got connection from pool
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - Closing the resultset.
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - Closing the connection. Connection HashCode:29897942  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - Attempting to close connection
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - removeConnectionFromConnectionList()
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - Removing connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> from connection list
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - Connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:29,369 INFO [InsertThread --- 35] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:29,369 DEBUG [InsertThread --- 35] - Resultset released from CertDBImpl.getCertUnitByPkid method.
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - OUT -- CertDBImpl.java - getCertUnitByPkid - 
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - UNIT : tomcat-trust
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - CurrentIPAddress : 10.48.46.30
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - RemoteIPAddress : 10.48.46.29
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - OldSerialNo :
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - NewSerialNo :7a40f8743a793b44fe802b5f3e1e6f36
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - IN -- CertUtil.java - getListFromComaSeperatedStr(..) - 
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - OUT -- CertUtil.java - getListFromComaSeperatedStr - 
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - tomcat-trust --- is included unit for CN
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - IN -- CertUtil.java - loadCertFromString(cert) - 
2014-08-04 15:21:29,370 INFO [InsertThread --- 35] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:29,373 INFO [InsertThread --- 35] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:29,373 INFO [InsertThread --- 35] - OUT -- CertUtil.java - loadCertFromString - ## Info about the certificate has been received. CertCN will try to delete old ## tomcat-trust for this node (if any) and import it 2014-08-04 15:21:29,373 INFO [InsertThread --- 35] - IN -- CertDBUtil.java - checkDeleteAndImport(unit, dbCert) - 
2014-08-04 15:21:29,373 INFO [InsertThread --- 35] - DB CertInfo.--SN:162503161730851213217569888696899890998--SubjectDN:L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL--GetNotBefore:Mon Aug 04 15:19:07 CEST 2014--GetNotAfter:Sat Aug 03 15:19:06 CEST 2019
2014-08-04 15:21:29,373 INFO [InsertThread --- 35] - loading certificate element named [tomcat-trust]
2014-08-04 15:21:29,373 INFO [InsertThread --- 35] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-04 15:21:29,373 INFO [InsertThread --- 35] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-04 15:21:29,374 INFO [InsertThread --- 35] - looking for first [trust-certs] in [product-cpi]
2014-08-04 15:21:29,374 INFO [InsertThread --- 35] - loaded element [tomcat-trust]
2014-08-04 15:21:29,374 INFO [InsertThread --- 35] - determining cert dir for [tomcat-trust]
2014-08-04 15:21:29,374 INFO [InsertThread --- 35] - looking for first [dir] in [tomcat-trust]
2014-08-04 15:21:29,374 INFO [InsertThread --- 35] - getting the value of [dir]
2014-08-04 15:21:29,374 INFO [InsertThread --- 35] - value is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-04 15:21:29,374 INFO [InsertThread --- 35] - cert dir is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.description] match is false
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.description] match is false
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.pem] match is true
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.der] match is true
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore] match is false
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.der] match is true
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.der] match is true
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description] match is false
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/7e0370f0.0] match is false
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/d0aacffb.0] match is false
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/101f99a6.0] match is false
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem] match is true
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.pem] match is true
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:29,375 INFO [InsertThread --- 35] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:29,376 INFO [InsertThread --- 35] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:29,376 INFO [InsertThread --- 35] - IN -- CertDBUtil.java - importTrustCertInFileSystem.. unit : tomcat-trust
2014-08-04 15:21:29,376 INFO [InsertThread --- 35] - IN -- CertDBUtil.java - populateOpInfo(operation, unit, type, fileLocation, x509Cert, isDBInsert) - 
2014-08-04 15:21:29,376 INFO [InsertThread --- 35] - loading certificate element named [tomcat-trust]
2014-08-04 15:21:29,376 INFO [InsertThread --- 35] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-04 15:21:29,376 INFO [InsertThread --- 35] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - looking for first [trust-certs] in [product-cpi]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - loaded element [tomcat-trust]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - determining key dir for [tomcat-trust]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - looking for first [key-dir] in [tomcat-trust]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - getting the value of [key-dir]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - value is [/usr/local/platform/.security/tomcat/keys]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - key dir is [/usr/local/platform/.security/tomcat/keys]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - loading certificate element named [tomcat-trust]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-04 15:21:29,377 INFO [InsertThread --- 35] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - looking for first [trust-certs] in [product-cpi]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - loaded element [tomcat-trust]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - determining cert dir for [tomcat-trust]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - looking for first [dir] in [tomcat-trust]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - getting the value of [dir]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - value is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - cert dir is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - OUT -- CertDBUtil.java - populateOpInfo - 
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- CertMgr.java - getCertMgrObj(unit) - tomcat-trust
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - OUT -- CertMgr.java - getCertMgrObj - com.cisco.cpi.certMgmt.manager.TomcatCertMgr@104f57f
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- DefaultCertMgr.java - importCert(info) - 
decode:     true
op:         import
unit:       tomcat-trust
keystoreUnit:tomcat-trust
logFile:    /var/log/active/platform/log/cert-mgmt.log
resultFile: /var/log/active/platform/log/certde-info.xml
keyDir:     /usr/local/platform/.security/tomcat/keys
certDir:    /usr/local/platform/.security/tomcat/trust-certs
srcCert:    null
type:       trust-certs
rootCACert: null
trustDir:   null
DNAME:      null
description:null
isDBInsert:false

2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Checking validity of cert
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - Verifying certificate L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - parseCNfromDN( certSubjDN: 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL')
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Truncating CN 'CUCM9X,OU=TAC,O=Cisco Systems,C=PL' -> 'CUCM9X'
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Parsed CN 'CUCM9X' from DN 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL'
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - trying to load cert from trust store ::/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - cert not available in trust store ::L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- DefaultCertMgr.java - importTrustCert(info, cert) - 
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- DefaultCertMgr.java - saveToTrustStore(info, cert) - 
2014-08-04 15:21:29,379 ERROR [InsertThread --- 35] - trust directory parameter is null
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- DefaultCertMgr.java - saveTrustCert(cert, targetDir, certType) - 
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - parseCNfromDN( certSubjDN: 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL')
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Truncating CN 'CUCM9X,OU=TAC,O=Cisco Systems,C=PL' -> 'CUCM9X'
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Parsed CN 'CUCM9X' from DN 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL'
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - parseCNfromDN( certSubjDN: 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL')
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Truncating CN 'CUCM9X,OU=TAC,O=Cisco Systems,C=PL' -> 'CUCM9X'
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Parsed CN 'CUCM9X' from DN 'L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL' ## certificate will be stored in filesystem with below name (CN from cert). Old ## certificate for CUCM9X has not been found 2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - target filename for imported cert: 'CUCM9X.pem'
2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - existing certificate with same filename not found. ## saving certificate as *.pem and *.der 2014-08-04 15:21:29,379 DEBUG [InsertThread --- 35] - Saving PEM encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem'
2014-08-04 15:21:29,379 INFO [InsertThread --- 35] - IN -- CryptoUtil.java - saveAsPEM(..) - File : /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem
2014-08-04 15:21:29,403 INFO [InsertThread --- 35] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-04 15:21:29,403 DEBUG [InsertThread --- 35] - Saving DER encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.der'
2014-08-04 15:21:29,406 INFO [InsertThread --- 35] - OUT -- DefaultCertMgr.java - saveTrustCert - 
2014-08-04 15:21:29,406 INFO [InsertThread --- 35] - IN -- TomcatCertMgr.java - saveToKeyStore(..) - 
2014-08-04 15:21:29,406 INFO [InsertThread --- 35] - IN -- RSACryptoEngine.java - saveToKeyStore(keystoreFile, keystorePass, x509Certificate, alias) - 
2014-08-04 15:21:29,406 INFO [InsertThread --- 35] - IN -- RSACryptoEngine.java - loadKeyStore(keystoreFile, keystorePass) - 
2014-08-04 15:21:29,421 INFO [InsertThread --- 35] - OUT -- RSACryptoEngine.java - loadKeyStore - 
2014-08-04 15:21:29,421 INFO [InsertThread --- 35] - Size of the keystore before import is : 3
2014-08-04 15:21:29,421 INFO [InsertThread --- 35] - Importing certificate : CUCM9X
2014-08-04 15:21:29,428 INFO [InsertThread --- 35] - Size of the keystore after import is : 4
2014-08-04 15:21:29,428 INFO [InsertThread --- 35] - OUT -- RSACryptoEngine.java - saveToKeyStore - 
2014-08-04 15:21:29,428 INFO [InsertThread --- 35] - OUT -- TomcatCertMgr.java - saveToKeyStore - 
2014-08-04 15:21:29,428 DEBUG [InsertThread --- 35] - TrustCert description filename : 'CUCM9X.description'
2014-08-04 15:21:29,439 INFO [InsertThread --- 35] - IN -- DefaultCertMgr.java - createDescriptionFile(name, description) - 
2014-08-04 15:21:29,439 INFO [InsertThread --- 35] - description is :Trust Certificate
2014-08-04 15:21:29,446 INFO [InsertThread --- 35] - OUT -- DefaultCertMgr.java - createDescriptionFile - 
2014-08-04 15:21:29,446 INFO [InsertThread --- 35] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - ## setting necessary permissions for the new created files (correcting access, owner and ## group) 2014-08-04 15:21:29,446 DEBUG [InsertThread --- 35] - setOwnershipAndPermissions : CUCM9X.description
2014-08-04 15:21:29,446 DEBUG [InsertThread --- 35] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description'
2014-08-04 15:21:29,446 INFO [InsertThread --- 35] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:29,446 DEBUG [InsertThread --- 35] - Executing command from Util.sysExec :  /bin/chown certbase /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description
2014-08-04 15:21:29,471 INFO [InsertThread --- 35] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:29,471 DEBUG [InsertThread --- 35] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description'
2014-08-04 15:21:29,472 INFO [InsertThread --- 35] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:29,472 DEBUG [InsertThread --- 35] - Executing command from Util.sysExec :  /bin/chgrp ccmbase /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description
2014-08-04 15:21:29,474 INFO [InsertThread --- 35] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:29,475 DEBUG [InsertThread --- 35] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description'
2014-08-04 15:21:29,475 INFO [InsertThread --- 35] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:29,475 DEBUG [InsertThread --- 35] - Executing command from Util.sysExec :  /bin/chmod 755 /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description
2014-08-04 15:21:29,484 INFO [InsertThread --- 35] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:29,484 INFO [InsertThread --- 35] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-04 15:21:29,484 INFO [InsertThread --- 35] - OUT -- DefaultCertMgr.java - saveToTrustStore - 
2014-08-04 15:21:29,485 INFO [InsertThread --- 35] - trustdir ::/usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:29,485 INFO [InsertThread --- 35] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:29,485 DEBUG [InsertThread --- 35] - Executing command from Util.sysExec :  python /usr/local/platform/bin/c_rehash.py /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:29,668 INFO [InsertThread --- 35] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:29,668 INFO [InsertThread --- 35] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-04 15:21:29,668 DEBUG [InsertThread --- 35] - setOwnershipAndPermissions : trust-certs
2014-08-04 15:21:29,668 DEBUG [InsertThread --- 35] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-04 15:21:29,668 INFO [InsertThread --- 35] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:29,669 DEBUG [InsertThread --- 35] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:29,675 INFO [InsertThread --- 35] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:29,675 DEBUG [InsertThread --- 35] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-04 15:21:29,675 INFO [InsertThread --- 35] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:29,675 DEBUG [InsertThread --- 35] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:29,680 INFO [InsertThread --- 35] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:29,680 DEBUG [InsertThread --- 35] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-04 15:21:29,680 INFO [InsertThread --- 35] - IN -- Util.java - sysExec(exe, args) - 
2014-08-04 15:21:29,680 DEBUG [InsertThread --- 35] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/trust-certs
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- Util.java - sysExec - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - No plugins registered for DB Store
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - IN -- CryptoUtil.java - isOCSPEnabled(..) - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - IN -- CryptoUtil.java - getCertMonitorXmlParser(..) - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- CryptoUtil.java - getCertMonitorXmlParser - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- CryptoUtil.java - isOCSPEnabled - false
2014-08-04 15:21:29,683 DEBUG [InsertThread --- 35] - OCSP is not enabled.
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - Successfully imported trusted certificate with Subject DN:L&#61;Krakow,ST&#61;Malopolska,CN&#61;CUCM9X,OU&#61;TAC,O&#61;Cisco Systems,C&#61;PL
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- DefaultCertMgr.java - importTrustCert - Successfully imported trusted certificate with Subject DN:L&#61;Krakow,ST&#61;Malopolska,CN&#61;CUCM9X,OU&#61;TAC,O&#61;Cisco Systems,C&#61;PL ## inserting certificate ends with success 2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - result of import operations is ::Import of trust certificate is successful
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- DefaultCertMgr.java - importCert - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- CertDBUtil.java - importTrustCertInFileSystem - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- CertDBUtil.java - checkDeleteAndImport - 
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - tomcat-trust Certificate successfully updated in trust-store by Change Notification..
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- CertKeystoreHandler.java - updateIntoKeystore - 
2014-08-04 15:21:29,683 DEBUG [InsertThread --- 35] - InsertThread --- 35 -- END --
2014-08-04 15:21:29,683 INFO [InsertThread --- 35] - OUT -- CertKeystoreHandler.java - run - 
2014-08-04 15:21:29,786 DEBUG [ConnectionCleaner] - Cleaning connection list ## above process was the result for row inserted into CERTIFICATE table. Similar check ## will be done for the row inserted into CERTIFICATESERVICECERTIFICATEMAP 2014-08-04 15:21:34,322 INFO [Thread-5] - Inside CERTIFICATESERVICECERTIFICATEMAP - I option..
2014-08-04 15:21:34,322 DEBUG [Thread-5] - Insert Data in CERTIFICATESERVICECERTIFICATEMAP ::<msg><type>DBL</type><table>certificateservicecertificatemap</table><tableid>44</tableid><action>I</action><time>1407158489</time><new><cdrserver>2</cdrserver><cdrtime>1407158487</cdrtime><pkid>798ff6e1-e1d6-42e5-a4e6-30d9d7360d6d</pkid><fkcertificate>4152b36b-002e-68ac-711d-c373fa940779</fkcertificate><tkcertificateservice>6</tkcertificateservice><ifx_replcheck>6043699681953972226</ifx_replcheck></new></msg>
2014-08-04 15:21:34,322 INFO [Thread-5] - IN -- CertDBImpl.java - getCertificate(certBash64SHA1:null --pkid:4152b36b-002e-68ac-711d-c373fa940779
2014-08-04 15:21:34,323 DEBUG [Thread-5] - Connection Initialized to localnode. Connection HashCode:32140521  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:34,323 DEBUG [Thread-5] - Select Query to getCertificate :SELECT A.*,B.HASH FROM CERTIFICATE  A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND A.PKID = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-04 15:21:34,323 DEBUG [Thread-5] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:34,323 DEBUG [Thread-5] - Try to get a connection from pool
2014-08-04 15:21:34,323 DEBUG [Thread-5] - getting local connection from Pool
2014-08-04 15:21:34,324 DEBUG [Thread-5] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:34,324 DEBUG [Thread-5] - There are currently 2 connection pool entries
2014-08-04 15:21:34,324 DEBUG [Thread-5] - Adding connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> to connection list
2014-08-04 15:21:34,324 DEBUG [Thread-5] - Marking connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> as used
2014-08-04 15:21:34,324 DEBUG [Thread-5] - Got connection from pool
2014-08-04 15:21:34,328 DEBUG [Thread-5] - Closing the resultset.
2014-08-04 15:21:34,329 DEBUG [Thread-5] - Closing the connection. Connection HashCode:32140521  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:34,329 DEBUG [Thread-5] - Attempting to close connection
2014-08-04 15:21:34,329 DEBUG [Thread-5] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:34,329 DEBUG [Thread-5] - removeConnectionFromConnectionList()
2014-08-04 15:21:34,329 DEBUG [Thread-5] - Removing connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> from connection list
2014-08-04 15:21:34,329 DEBUG [Thread-5] - Connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:34,329 INFO [Thread-5] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:34,329 DEBUG [Thread-5] - Connection released from CertDBImpl.getCertificate method.
2014-08-04 15:21:34,329 INFO [Thread-5] - OUT -- CertDBImpl.java - getCertificate - 
2014-08-04 15:21:34,329 DEBUG [Thread-5] - Certificate PKID : 4152b36b-002e-68ac-711d-c373fa940779 , ipAddress : 10.48.46.29 , OldSerialNo : 7a40f8743a793b44fe802b5f3e1e6f36 , NewSerialNo : 7a40f8743a793b44fe802b5f3e1e6f36
2014-08-04 15:21:34,329 INFO [Thread-5] - OUT - process.
2014-08-04 15:21:34,330 INFO [InsertThread --- 36] - IN -- CertKeystoreHandler.java - run() - 
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - InsertThread --- 36 -- START --
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - DB Value UPDATE: 4152b36b-002e-68ac-711d-c373fa940779
2014-08-04 15:21:34,330 INFO [InsertThread --- 36] - IN -- CertKeystoreHandler.java - updateIntoKeystore() - 
2014-08-04 15:21:34,330 INFO [InsertThread --- 36] - IN -- CertDBImpl.java - getCertificate(certBash64SHA1:null --pkid:4152b36b-002e-68ac-711d-c373fa940779
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - Connection Initialized to localnode. Connection HashCode:14972385  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - Select Query to getCertificate :SELECT A.*,B.HASH FROM CERTIFICATE  A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND A.PKID = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - Try to get a connection from pool
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - getting local connection from Pool
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - There are currently 2 connection pool entries
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - Adding connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> to connection list
2014-08-04 15:21:34,330 DEBUG [InsertThread --- 36] - Marking connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> as used
2014-08-04 15:21:34,331 DEBUG [InsertThread --- 36] - Got connection from pool
2014-08-04 15:21:34,333 DEBUG [InsertThread --- 36] - Closing the resultset.
2014-08-04 15:21:34,333 DEBUG [InsertThread --- 36] - Closing the connection. Connection HashCode:14972385  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:34,333 DEBUG [InsertThread --- 36] - Attempting to close connection
2014-08-04 15:21:34,333 DEBUG [InsertThread --- 36] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:34,333 DEBUG [InsertThread --- 36] - removeConnectionFromConnectionList()
2014-08-04 15:21:34,333 DEBUG [InsertThread --- 36] - Removing connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> from connection list
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:34,334 INFO [InsertThread --- 36] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Connection released from CertDBImpl.getCertificate method.
2014-08-04 15:21:34,334 INFO [InsertThread --- 36] - OUT -- CertDBImpl.java - getCertificate - 
2014-08-04 15:21:34,334 INFO [InsertThread --- 36] - IN -- CertDBImpl.java - getCertUnitByPkid(pkid) - 
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Connection Initialized to localnode. Connection HashCode:16196072  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Select Query to getCertUnitByPkid :SELECT A.PKID, A.FKCERTIFICATE, A.TKCERTIFICATESERVICE, B.NAME UNIT FROM CERTIFICATESERVICECERTIFICATEMAP A, TYPECERTIFICATESERVICE B WHERE A.FKCERTIFICATE="4152b36b-002e-68ac-711d-c373fa940779" AND A.TKCERTIFICATESERVICE = B.ENUM
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Try to get a connection from pool
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - getting local connection from Pool
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - There are currently 2 connection pool entries
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Adding connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> to connection list
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Marking connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> as used
2014-08-04 15:21:34,334 DEBUG [InsertThread --- 36] - Got connection from pool
2014-08-04 15:21:34,337 DEBUG [InsertThread --- 36] - Closing the resultset.
2014-08-04 15:21:34,337 DEBUG [InsertThread --- 36] - Closing the connection. Connection HashCode:16196072  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-04 15:21:34,337 DEBUG [InsertThread --- 36] - Attempting to close connection
2014-08-04 15:21:34,337 DEBUG [InsertThread --- 36] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-04 15:21:34,337 DEBUG [InsertThread --- 36] - removeConnectionFromConnectionList()
2014-08-04 15:21:34,337 DEBUG [InsertThread --- 36] - Removing connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> from connection list
2014-08-04 15:21:34,351 DEBUG [InsertThread --- 36] - Connection <com.informix.jdbc.IfxSqliConnect@1ec9f34> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - Connection/Statement/Resultset is closed properly.
2014-08-04 15:21:34,351 DEBUG [InsertThread --- 36] - Resultset released from CertDBImpl.getCertUnitByPkid method.
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - OUT -- CertDBImpl.java - getCertUnitByPkid - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - UNIT : tomcat-trust
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - CurrentIPAddress : 10.48.46.30
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - RemoteIPAddress : 10.48.46.29
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - OldSerialNo :7a40f8743a793b44fe802b5f3e1e6f36
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - NewSerialNo :7a40f8743a793b44fe802b5f3e1e6f36
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - IN -- CertUtil.java - getListFromComaSeperatedStr(..) - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - OUT -- CertUtil.java - getListFromComaSeperatedStr - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - tomcat-trust --- is included unit for CN
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - IN -- CertUtil.java - loadCertFromString(cert) - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - OUT -- CertUtil.java - loadCertFromString - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - IN -- CertDBUtil.java - checkDeleteAndImport(unit, dbCert) - 
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - DB CertInfo.--SN:162503161730851213217569888696899890998--SubjectDN:L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL--GetNotBefore:Mon Aug 04 15:19:07 CEST 2014--GetNotAfter:Sat Aug 03 15:19:06 CEST 2019
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - loading certificate element named [tomcat-trust]
2014-08-04 15:21:34,351 INFO [InsertThread --- 36] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-04 15:21:34,352 INFO [InsertThread --- 36] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-04 15:21:34,353 INFO [InsertThread --- 36] - looking for first [trust-certs] in [product-cpi]
2014-08-04 15:21:34,353 INFO [InsertThread --- 36] - loaded element [tomcat-trust]
2014-08-04 15:21:34,353 INFO [InsertThread --- 36] - determining cert dir for [tomcat-trust]
2014-08-04 15:21:34,353 INFO [InsertThread --- 36] - looking for first [dir] in [tomcat-trust]
2014-08-04 15:21:34,353 INFO [InsertThread --- 36] - getting the value of [dir]
2014-08-04 15:21:34,353 INFO [InsertThread --- 36] - value is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-04 15:21:34,353 INFO [InsertThread --- 36] - cert dir is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.description] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.description] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.description] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.pem] match is true
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.der] match is true
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.der] match is true
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/25ffab9b.0] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.der] match is true
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/7e0370f0.0] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/d0aacffb.0] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.der] match is true
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/101f99a6.0] match is false
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem] match is true
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem] match is true
2014-08-04 15:21:34,354 INFO [InsertThread --- 36] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.pem] match is true
2014-08-04 15:21:34,355 INFO [InsertThread --- 36] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:34,355 INFO [InsertThread --- 36] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:34,355 INFO [InsertThread --- 36] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:34,355 INFO [InsertThread --- 36] - OUT -- RSACryptoEngine.java - loadCertificate - ## but since it has been checked that the certificate is already in the filesystem, ## nothing will be added. 2014-08-04 15:21:34,355 DEBUG [InsertThread --- 36] - SUBJECTDN of DBCert and FileSystemCert compared correctly.. 
2014-08-04 15:21:34,355 DEBUG [InsertThread --- 36] - Certificate already exists in FileSystem..
2014-08-04 15:21:34,355 INFO [InsertThread --- 36] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:34,355 INFO [InsertThread --- 36] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:34,355 INFO [InsertThread --- 36] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-04 15:21:34,356 INFO [InsertThread --- 36] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-04 15:21:34,356 INFO [InsertThread --- 36] - OUT -- CertDBUtil.java - checkDeleteAndImport - 
2014-08-04 15:21:34,356 INFO [InsertThread --- 36] - tomcat-trust Certificate successfully updated in trust-store by Change Notification..
2014-08-04 15:21:34,356 INFO [InsertThread --- 36] - OUT -- CertKeystoreHandler.java - updateIntoKeystore - 
2014-08-04 15:21:34,356 DEBUG [InsertThread --- 36] - InsertThread --- 36 -- END --
2014-08-04 15:21:34,356 INFO [InsertThread --- 36] - OUT -- CertKeystoreHandler.java - run -
```

f. When you now look at the certificate on the filesystem level  you can verify the md5 checksum (md5sum) and will see it's the same as on the publisher node.

On the GUI you can verify the same by compare the serial number.

```
[root@ CUCM861s tomcat]# pwd
/usr/local/platform/.security/tomcat
[root@CUCM861s tomcat]# ls -la
total 40
drwxr-xr-x 5 root     root    4096 Apr  4 14:33 .
drwxr-xr-x 5 root     root    4096 Apr  4 14:33 ..
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 22:51 certs
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 22:51 keys
drwxr-xr-x 2 certbase ccmbase 4096 Aug  4 15:21 trust-certs
[root@CUCM861s tomcat]# ls -la certs
total 48
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 22:51 .
drwxr-xr-x 5 root     root    4096 Apr  4 14:33 ..
-rwxr-xr-x 1 certbase ccmbase  941 Aug  2 22:51 tomcat.der
-rwxr-xr-x 1 certbase ccmbase   64 Aug  2 22:51 tomcat.description
-rwxr-xr-x 1 certbase ccmbase 2598 Aug  2 22:51 tomcat.keystore
-rwxr-xr-x 1 certbase ccmbase 1330 Aug  2 22:51 tomcat.pem
[root@CUCM861s tomcat]# ls -la trust-certs
total 140
drwxr-xr-x 2 certbase ccmbase 4096 Aug  4 15:21 .
drwxr-xr-x 5 root     root    4096 Apr  4 14:33 ..
lrwxrwxrwx 1 certbase ccmbase   11 Aug  4 15:21 101f99a6.0 -> CUCM861.pem
lrwxrwxrwx 1 certbase ccmbase   10 Aug  4 15:21 25ffab9b.0 -> CUCM9X.pem lrwxrwxrwx 1 certbase ccmbase   42 Aug  4 15:21 7e0370f0.0 -> VeriSign_Class_3_Secure_Server_CA_-_G3.pem
-rwxr-xr-x 1 certbase ccmbase  939 Aug  2 23:36 CUCM861.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 23:36 CUCM861.description
-rwxr-xr-x 1 certbase ccmbase 1326 Aug  2 23:36 CUCM861.pem
-rwxr-xr-x 1 certbase ccmbase  941 Aug  2 22:51 CUCM861s.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 22:51 CUCM861s.description
-rwxr-xr-x 1 certbase ccmbase 1330 Aug  2 22:51 CUCM861s.pem
-rwxr-xr-x 1 certbase ccmbase  953 Aug  4 15:21 CUCM9X.der -rwxr-xr-x 1 certbase ccmbase   44 Aug  4 15:21 CUCM9X.description
-rwxr-xr-x 1 certbase ccmbase 1346 Aug  4 15:21 CUCM9X.pem lrwxrwxrwx 1 certbase ccmbase   12 Aug  4 15:21 d0aacffb.0 -> CUCM861s.pem
-rwxr-xr-x 1 certbase ccmbase 4939 Aug  4 15:21 tomcat-trust.keystore
-rwxr-xr-x 1 certbase ccmbase 1520 Apr  4 14:33 VeriSign_Class_3_Secure_Server_CA_-_G3.der
-rwxr-xr-x 1 certbase ccmbase   44 Apr  4 14:33 VeriSign_Class_3_Secure_Server_CA_-_G3.description
-rwxr-xr-x 1 certbase ccmbase 2114 Apr  4 14:33 VeriSign_Class_3_Secure_Server_CA_-_G3.pem
[root@CUCM861s tomcat]# md5sum trust-certs/CUCM9X.pem a0a2e12a42e4bbbf10655c9b299839d9 trust-certs/CUCM9X.pem
```

### 4.B. Delete tomcat-trust certificate

In the second scenario you will remove tomcat-trust certificate uploaded in the 4.A section.

When analyze this example you need to remember about below design statement:

"The change notification service will not propagate the delete of a certificate from tomcat trust store of a node to the other. This implies that delete of a certificate from the tomcat trust from one node does not automatically delete the same certificate from other nodes. This behavior is implemented to ensure that administrator will have the ability to remove certain nodes from trusting applications on other nodes due to security considerations."

Above is valid only for tomcat trust certificate type.

Delete operation consists of below steps:

a. delete the certificate from the CM page. b. certificate files are deleted from the filesystem c. certCN kicks in on the publisher and subscriber. No operation is required by both of them. d. deleting the same tomcat-trust certificate from the subscriber node

a. Delete operation initiated from CM page

Cert is deleted from the filesystem and corresponding rows in the database also deleted. Certificate itself is not  removed from CERTIFIACATE table. Let's follow this in the CM logs (comments inline):

```
2014-08-19 23:25:10,714 INFO [main] - log4j configuration successful.
2014-08-19 23:25:10,720 INFO [main] - IN -- CertMgr.java - mainInternal(args) - 
2014-08-19 23:25:10,721 INFO [main] - decode ## delete operation is invoked here 2014-08-19 23:25:10,722 INFO [main] - op:delete
2014-08-19 23:25:10,722 INFO [main] - unit:tomcat-trust
2014-08-19 23:25:10,722 INFO [main] - cert-dir:%2Fusr%2Flocal%2Fplatform%2F.security%2Ftomcat%2Ftrust-certs%2FCUCM9X.pem
2014-08-19 23:25:10,722 INFO [main] - key-dir:%2Fusr%2Flocal%2Fplatform%2F.security%2Ftomcat%2Fkeys
2014-08-19 23:25:10,722 INFO [main] - logfile:%2Fvar%2Flog%2Factive%2Fplatform%2Flog%2Fcert-mgmt.log
2014-08-19 23:25:10,722 INFO [main] - resultfile:%2Fvar%2Flog%2Factive%2Fplatform%2Flog%2Fcertde-info.xml
2014-08-19 23:25:10,722 INFO [main] - type:trust-certs
2014-08-19 23:25:10,749 INFO [main] - Parsed information
2014-08-19 23:25:10,749 INFO [main] - OrgName: CISCO
2014-08-19 23:25:10,749 INFO [main] - OrgUnit: TAC
2014-08-19 23:25:10,749 INFO [main] - Location: KRAKOW
2014-08-19 23:25:10,749 INFO [main] - Country: PL
2014-08-19 23:25:10,749 INFO [main] - State: MALOPOLSKA
2014-08-19 23:25:10,749 INFO [main] - Hostname: CUCM861
2014-08-19 23:25:10,750 INFO [main] - AlternateHostname: null
2014-08-19 23:25:10,750 INFO [main] - Domain Name: 
2014-08-19 23:25:10,750 INFO [main] - IPAddress: 10.48.46.29
2014-08-19 23:25:10,751 INFO [main] - In parseXML()
2014-08-19 23:25:10,761 INFO [main] - FQDN Name retrived by InetAddress : CUCM861
2014-08-19 23:25:10,761 INFO [main] - CN: CUCM861
2014-08-19 23:25:10,761 INFO [main] - Temp before mod is 
2014-08-19 23:25:10,761 INFO [main] - Temp afer mod is TAC
2014-08-19 23:25:10,761 INFO [main] - Temp in else is TAC
2014-08-19 23:25:10,761 INFO [main] - Temp before mod is 
2014-08-19 23:25:10,761 INFO [main] - Temp afer mod is TAC
2014-08-19 23:25:10,761 INFO [main] - Temp in else is TAC
2014-08-19 23:25:10,762 INFO [main] - OuFields are TAC
2014-08-19 23:25:10,762 DEBUG [main] - Field after encoding: TAC
2014-08-19 23:25:10,762 DEBUG [main] - Field after encoding: CISCO
2014-08-19 23:25:10,762 DEBUG [main] - Field after encoding: KRAKOW
2014-08-19 23:25:10,762 DEBUG [main] - Field after encoding: MALOPOLSKA
2014-08-19 23:25:10,762 DEBUG [main] - Field after encoding: PL
2014-08-19 23:25:10,765 INFO [main] - OU field is :TAC
2014-08-19 23:25:10,765 INFO [main] - SubjectDN :: CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL
2014-08-19 23:25:10,765 INFO [main] - IN -- CertMgr.java - getCertMgrObj(unit) - tomcat-trust
2014-08-19 23:25:10,774 INFO [main] - OUT -- CertMgr.java - getCertMgrObj - com.cisco.cpi.certMgmt.manager.TomcatCertMgr@92bbba
2014-08-19 23:25:10,774 INFO [main] - Dummy loadProperties
2014-08-19 23:25:10,774 INFO [main] - IN -- CertMgr.java - doOp(info) - ## details about the certificate that will be deleted 2014-08-19 23:25:10,774 INFO [main] - IN -- DefaultCertMgr.java - deleteCert(info) - 
decode:     true
op:         delete
unit:       tomcat-trust
keystoreUnit:tomcat-trust
logFile:    /var/log/active/platform/log/cert-mgmt.log
resultFile: /var/log/active/platform/log/certde-info.xml
keyDir:     /usr/local/platform/.security/tomcat/keys
certDir:    /usr/local/platform/.security/tomcat/trust-certs/CUCM9X.pem
srcCert:    null
type:       trust-certs
rootCACert: null
trustDir:   null
DNAME:      CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL
description:null
isDBInsert:true ## certificate file name 2014-08-19 23:25:10,775 INFO [main] - parsed filename: 'CUCM9X.pem'
2014-08-19 23:25:10,775 DEBUG [main] - filename: 'CUCM9X.pem'
2014-08-19 23:25:10,775 DEBUG [main] - fileRoot: 'CUCM9X'
2014-08-19 23:25:10,775 INFO [main] - IN -- DefaultCertMgr.java - deleteDERandPEM(filenameRoot, parentDir, info) - ## it will remove two files: CUCM9X.DER and CUCM9X.PEM 2014-08-19 23:25:10,775 DEBUG [main] - ParentDir:/usr/local/platform/.security/tomcat/trust-certsFileName.(DER/PEM):CUCM9X
2014-08-19 23:25:11,100 DEBUG [main] - Loading RSA providers explicitly...
2014-08-19 23:25:12,486 DEBUG [main] - RSA providers are loaded explicitly...
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.1=JsafeJCE
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.2=RsaJsse
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.3=BC
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.4=SUN
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.5=SunRsaSign
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.6=SunJSSE
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.7=SunJCE
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.8=SunJGSS
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.9=SunSASL
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.10=XMLDSig
2014-08-19 23:25:12,487 DEBUG [main] - New security.provider.11=SunPCSC
2014-08-19 23:25:12,487 INFO [main] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-19 23:25:12,802 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-19 23:25:12,826 INFO [main] - IN -- CertUtil.java - populateCertInfo(cert, opInfo, certFilePemLocation) - 
2014-08-19 23:25:12,827 INFO [main] - IN -- CertUtil.java - getHostName(..) - 
2014-08-19 23:25:12,827 INFO [main] - OUT -- CertUtil.java - getHostName - CUCM861
2014-08-19 23:25:12,830 INFO [main] - IN -- CryptoUtil.java - saveAsPEM(..) - 
2014-08-19 23:25:12,834 INFO [main] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-19 23:25:12,834 INFO [main] - OUT -- CertUtil.java - populateCertInfo - ## certificate on the filesystem level has been deleted. Now the same must be done on the ## DB level 2014-08-19 23:25:12,835 INFO [main] - IN -- CertDBAction.java - deleteCertificateInDB(certInfo) - 
2014-08-19 23:25:12,835 INFO [main] - 

DBParameters ... 
PKID :		null
CN :		L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
serialNo :	7a40f8743a793b44fe802b5f3e1e6f36
hostName :	CUCM861
issuerName :	L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL
Certificate :	Not Printing huge Certificate String..
IPV4Address :	10.48.46.29
IPV6Address :	
TimeToLive :	NULL
UNIT :		tomcat-trust
TYPE :		trust-certs
ROLE :		null
RoleMoniker :	null
RoleEnum :null
SERVICE :		null
ServiceMoniker :	null
ServiceEnum :0

2014-08-19 23:25:12,835 INFO [main] - DB - Certifciate Store Plugin Handler is :com.cisco.ccm.certmgmt.db.CertDBImpl
2014-08-19 23:25:12,859 INFO [main] - IN -- CertDBImpl.java - deleteCertificate(certInfo) - 
2014-08-19 23:25:13,024 DEBUG [main] - Connection Initialized to localnode. Connection HashCode:14098944  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-19 23:25:13,024 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-19 23:25:13,026 DEBUG [main] - Try to get a connection from pool
2014-08-19 23:25:13,026 DEBUG [main] - getting local connection from Pool
2014-08-19 23:25:13,029 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-19 23:25:13,029 DEBUG [main] - There are currently 0 connection pool entries
2014-08-19 23:25:13,034 DEBUG [main] - Checking if connection limit has been reached for database
2014-08-19 23:25:13,035 DEBUG [main] - Connecting to publisher so max number of connections allowed is 100
2014-08-19 23:25:13,035 DEBUG [main] - Number of connections in use is 0
2014-08-19 23:25:13,035 DEBUG [main] - There is currently 1 connection pool entry
2014-08-19 23:25:13,035 DEBUG [main] - Number of available connections in pool: 0
2014-08-19 23:25:13,406 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@196e136> to connection list
2014-08-19 23:25:13,407 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@196e136> as used
2014-08-19 23:25:13,407 DEBUG [main] - Got connection from pool
2014-08-19 23:25:13,412 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-19 23:25:13,418 DEBUG [main] - Closing the resultset.
2014-08-19 23:25:13,419 DEBUG [main] - Closing the connection. Connection HashCode:14098944  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-19 23:25:13,419 DEBUG [main] - Attempting to close connection
2014-08-19 23:25:13,419 DEBUG [main] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-19 23:25:13,419 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-19 23:25:13,431 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@196e136> from connection list
2014-08-19 23:25:13,442 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@196e136> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-19 23:25:13,442 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,443 INFO [main] - TYPETRUSTROLEMAP ::{TRUST_ROLE_DATA_SERVICE=24, TRUST_ROLE_PROVISIONING_SERVICE=23, TRUST_ROLE_SERVICEABILITY=27, TRUST_ROLES_CALLMANAGER_TFTP=2, PHONE_TRUST_ROLES_FIREWALL=6, ROLE_APPLICATION_SERVER=7, TRUST_ROLES_SAST=0, ROLE_SIGNALING_CALL_CONTROL=22, TRUST_ROLES_CALLMANAGER=1, TRUST_ROLES_UNKNOWN=255, TRUST_ROLE_NETWORK_ELEMENT=25, TRUST_ROLES_SRST=5, ROLE_CERTIFICATE_AUTHORITY=20, TRUST_ROLE_VPN=26, TRUST_ROLES_CAPF=4, TRUST_ROLES_TFTP=3, ROLE_AUTHENTICATION_AUTHORIZATION=21}
2014-08-19 23:25:13,443 INFO [main] - TYPESERVICEROLEMAP ::{Phone-VPN-trust=2, CallManager=3, Phone-CTL-trust=15, tomcat-trust=6, TVS=11, ipsec-trust=8, Phone-trust=1, Phone-SAST-trust=14, tomcat=5, userlicensing-trust=16, CAPF=9, ipsec=7, CAPF-trust=10, CallManager-trust=4, TVS-trust=12, directory-trust=13}
2014-08-19 23:25:13,443 INFO [main] - unitRoleMap ::{Phone-VPN-trust=[TRUST_ROLE_VPN], CallManager=[TRUST_ROLES_CALLMANAGER_TFTP, TRUST_ROLES_SAST], Phone-CTL-trust=[ROLE_APPLICATION_SERVER], tomcat-trust=[ROLE_APPLICATION_SERVER], TVS=[ROLE_AUTHENTICATION_AUTHORIZATION], ipsec-trust=[], Phone-trust=[ROLE_APPLICATION_SERVER], Phone-SAST-trust=[TRUST_ROLES_SAST, TRUST_ROLES_TFTP], tomcat=[ROLE_APPLICATION_SERVER], userlicensing-trust=[], CAPF=[TRUST_ROLES_CAPF], ipsec=[ROLE_APPLICATION_SERVER], CAPF-trust=[], CallManager-trust=[], TVS-trust=[], directory-trust=[]}
2014-08-19 23:25:13,443 INFO [main] - commonTrustStoreMap ::{}
2014-08-19 23:25:13,446 DEBUG [main] - Connection Initialized to Publisher. Connection HashCode:24762452  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-19 23:25:13,446 INFO [main] - IN -- CertDBImpl.java - getPkidOfCertificate(hash, serverName, con) - ## looking for PKID of the certificate that should be deleted. This is done basing on the ## certificate hash 2014-08-19 23:25:13,447 DEBUG [main] - GetPKID Query :SELECT A.PKID FROM CERTIFICATE A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND B.HASH = "a9Ww/WeDmBnnHHncUCqOGCz4O9g="
2014-08-19 23:25:13,447 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-19 23:25:13,447 DEBUG [main] - Try to get a connection from pool
2014-08-19 23:25:13,447 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-19 23:25:13,447 DEBUG [main] - There is currently 1 connection pool entry
2014-08-19 23:25:13,447 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@196e136> to connection list
2014-08-19 23:25:13,447 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@196e136> as used
2014-08-19 23:25:13,447 DEBUG [main] - Got connection from pool
2014-08-19 23:25:13,462 DEBUG [main] - Closing the resultset.
2014-08-19 23:25:13,463 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,463 INFO [main] - OUT -- CertDBImpl.java - getPkidOfCertificate - 
2014-08-19 23:25:13,463 DEBUG [main] - Closing the connection. Connection HashCode:24762452  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-19 23:25:13,463 DEBUG [main] - Attempting to close connection
2014-08-19 23:25:13,463 DEBUG [main] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-19 23:25:13,463 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-19 23:25:13,463 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@196e136> from connection list
2014-08-19 23:25:13,463 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@196e136> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-19 23:25:13,464 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,465 DEBUG [main] - Connection Initialized to Publisher. Connection HashCode:12085572  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-19 23:25:13,465 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-19 23:25:13,465 DEBUG [main] - Try to get a connection from pool
2014-08-19 23:25:13,465 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-19 23:25:13,466 DEBUG [main] - There is currently 1 connection pool entry
2014-08-19 23:25:13,466 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@196e136> to connection list
2014-08-19 23:25:13,466 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@196e136> as used
2014-08-19 23:25:13,466 DEBUG [main] - Got connection from pool
2014-08-19 23:25:13,467 INFO [main] - IN -- CertDBImpl.java - deleteCertFromCertSrvCertMap(con, serialNo, subjectName, serviceEnum) - ## removing association for our certificate from CERTIFICATESERVICECERTIFICATEMAP table ## first 2014-08-19 23:25:13,467 DEBUG [main] - Delete query of CERTIFICATESERVICECERTIFICATEMAP :DELETE FROM CERTIFICATESERVICECERTIFICATEMAP WHERE TKCERTIFICATESERVICE = "6"  AND FKCERTIFICATE = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-19 23:25:13,467 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-19 23:25:13,561 INFO [main] - OUT -- CertDBImpl.java - deleteCertFromCertSrvCertMap - 
2014-08-19 23:25:13,561 INFO [main] - IN -- CertDBImpl.java - deleteCertFromCertProcessNodeMap(con, certInfo) - ## corresponding entry is being deleted from CERTIFICATEPROCESSNODEMAP table 2014-08-19 23:25:13,562 DEBUG [main] - Delete query of CERTIFICATEPROCESSNODEMAP :DELETE FROM CERTIFICATEPROCESSNODEMAP WHERE FKCERTIFICATE="4152b36b-002e-68ac-711d-c373fa940779" AND SERVERNAME = "CUCM861"
2014-08-19 23:25:13,562 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-19 23:25:13,608 INFO [main] - OUT -- CertDBImpl.java - deleteCertFromCertProcessNodeMap - 
2014-08-19 23:25:13,609 DEBUG [main] - Certificate to be deleted UNIT: tomcat-trust :: RoleMoniker :ROLE_APPLICATION_SERVER :: RoleEnum :7 :: ServiceEnum :6
2014-08-19 23:25:13,609 INFO [main] - IN -- CertDBImpl.java - checkMultipleUnitForSameRole(con, roleMoniker, unit, certInfo) - 
2014-08-19 23:25:13,609 DEBUG [main] - checkMultipleUnitForSameRole : SELECT PKID,FKCERTIFICATE, TKCERTIFICATESERVICE,NAME UNIT FROM CERTIFICATESERVICECERTIFICATEMAP,TYPECERTIFICATESERVICE  WHERE ENUM=TKCERTIFICATESERVICE AND FKCERTIFICATE ="4152b36b-002e-68ac-711d-c373fa940779" AND NAME != "tomcat-trust"
2014-08-19 23:25:13,609 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-19 23:25:13,646 DEBUG [main] - Closing the resultset.
2014-08-19 23:25:13,654 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,654 INFO [main] - OUT -- CertDBImpl.java - checkMultipleUnitForSameRole - 
2014-08-19 23:25:13,654 INFO [main] - IN -- CertDBImpl.java - deleteCertFromTypeTrustRole(con, certInfo, roleEnum) - ## and the same for CERTIFICATETRUSTROLEMAP map 2014-08-19 23:25:13,654 DEBUG [main] - Delete query of CERTIFICATETRUSTROLEMAP :DELETE FROM CERTIFICATETRUSTROLEMAP WHERE  TKTRUSTROLE = "7" AND FKCERTIFICATE = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-19 23:25:13,654 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-19 23:25:13,680 INFO [main] - OUT -- CertDBImpl.java - deleteCertFromTypeTrustRole - 
2014-08-19 23:25:13,680 INFO [main] - IN -- CertDBImpl.java - checkMultipleCertForSrv(pkid, con) - 
2014-08-19 23:25:13,680 DEBUG [main] - checkMultipleCertForSrv : SELECT PKID,FKCERTIFICATE, TKCERTIFICATESERVICE FROM CERTIFICATESERVICECERTIFICATEMAP WHERE FKCERTIFICATE = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-19 23:25:13,680 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-19 23:25:13,682 DEBUG [main] - Closing the resultset.
2014-08-19 23:25:13,682 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,682 INFO [main] - OUT -- CertDBImpl.java - checkMultipleCertForSrv - 
2014-08-19 23:25:13,682 INFO [main] - IN -- CertDBImpl.java - checkMultipleCertForRole(certInfo, con) - 
2014-08-19 23:25:13,682 DEBUG [main] - checkMultipleCertForRole : SELECT PKID,FKCERTIFICATE, TKTRUSTROLE FROM CERTIFICATETRUSTROLEMAP WHERE FKCERTIFICATE = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-19 23:25:13,683 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-19 23:25:13,684 DEBUG [main] - Closing the resultset.
2014-08-19 23:25:13,684 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,684 INFO [main] - OUT -- CertDBImpl.java - checkMultipleCertForRole - 
2014-08-19 23:25:13,684 INFO [main] - IN -- CertDBImpl.java - checkMultipleCertForProcessnode(certInfo, con) - 
2014-08-19 23:25:13,684 DEBUG [main] - checkMultipleCertForProcessnode : SELECT PKID,FKCERTIFICATE,FKPROCESSNODE,SERVERNAME FROM CERTIFICATEPROCESSNODEMAP WHERE FKCERTIFICATE='4152b36b-002e-68ac-711d-c373fa940779'
2014-08-19 23:25:13,684 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-19 23:25:13,687 DEBUG [main] - Closing the resultset.
2014-08-19 23:25:13,687 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,687 INFO [main] - OUT -- CertDBImpl.java - checkMultipleCertForProcessnode - ## normally you would expect that the certificate would be removed from CERTIFICATE table. ## This will not happen since it is possible that some of the nodes in the cluster will ## have specific tomcat-trust certificate in the trust store but some not. This is in ## compliance with the design. Since you remove the certificate only from publisher ## (by removing coresponding entries from 3 tables above) node it still be used ## by subscriber node. That is why the certificate will not be removed from CERTIFICATE ## TABLE 2014-08-19 23:25:13,687 DEBUG [main] - DELETE FLAG :: isSrvMap=false :: isRoleMap=false :: isProcessnodeMap=true
2014-08-19 23:25:13,687 DEBUG [main] - The certificate is being used by either different role or unit or other node. So no need to delte from certificate table.
2014-08-19 23:25:13,690 DEBUG [main] - Connection committed for deleteCertificate..
2014-08-19 23:25:13,690 DEBUG [main] - Closing the connection. Connection HashCode:12085572  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-19 23:25:13,690 DEBUG [main] - Attempting to close connection
2014-08-19 23:25:13,690 DEBUG [main] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-19 23:25:13,690 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-19 23:25:13,690 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@196e136> from connection list
2014-08-19 23:25:13,690 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@196e136> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-19 23:25:13,691 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-19 23:25:13,691 DEBUG [main] - Connection released from CertDBImpl.deleteCertificate method.
2014-08-19 23:25:13,691 INFO [main] - OUT -- CertDBImpl.java - deleteCertificate - 
2014-08-19 23:25:13,691 INFO [main] - OUT -- CertDBAction.java - deleteCertificateInDB - 
2014-08-19 23:25:13,691 INFO [main] - OUT -- DefaultCertMgr.java - deleteDERandPEM - 
2014-08-19 23:25:13,691 DEBUG [main] - deleteDERandPEM: sCertDir = /usr/local/platform/.security/tomcat/trust-certs --- sAlias = CUCM9X ## removing the certificate from keystore on this node 2014-08-19 23:25:13,691 INFO [main] - IN -- TomcatCertMgr.java - removeFromKeyStore(..) - 
2014-08-19 23:25:13,691 INFO [main] - IN -- RSACryptoEngine.java - removeFromKeyStore(keystoreFile, keystorePass, alias) - 
2014-08-19 23:25:13,691 INFO [main] - IN -- RSACryptoEngine.java - loadKeyStore(keystoreFile, keystorePass) - 
2014-08-19 23:25:13,895 INFO [main] - OUT -- RSACryptoEngine.java - loadKeyStore - 
2014-08-19 23:25:13,922 DEBUG [main] - Removing certificate from keystore : CUCM9X
2014-08-19 23:25:13,923 DEBUG [main] - Size of the keystore after delete is : 3
2014-08-19 23:25:13,923 INFO [main] - OUT -- RSACryptoEngine.java - removeFromKeyStore - 
2014-08-19 23:25:13,923 INFO [main] - OUT -- TomcatCertMgr.java - removeFromKeyStore - 
2014-08-19 23:25:13,924 INFO [main] - trustdir ::/usr/local/platform/.security/tomcat/trust-certs
2014-08-19 23:25:13,924 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-19 23:25:13,924 DEBUG [main] - Executing command from Util.sysExec :  python /usr/local/platform/bin/c_rehash.py /usr/local/platform/.security/tomcat/trust-certs
2014-08-19 23:25:13,940 DEBUG [Finalizer] - Attempting to close connection
2014-08-19 23:25:13,940 DEBUG [Finalizer] - Connection already closed or never open
2014-08-19 23:25:13,940 DEBUG [Finalizer] - Attempting to close connection
2014-08-19 23:25:13,940 DEBUG [Finalizer] - Connection already closed or never open
2014-08-19 23:25:13,962 DEBUG [Finalizer] - Attempting to close connection
2014-08-19 23:25:13,962 DEBUG [Finalizer] - Connection already closed or never open
2014-08-19 23:25:14,203 INFO [main] - OUT -- Util.java - sysExec - ## setting/updating the rights and the ownership of the files in trust store (nothing will ## be changed since you just removed two cert files + description file, this is just ## standard procedure) 2014-08-19 23:25:14,203 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-19 23:25:14,203 DEBUG [main] - setOwnershipAndPermissions : trust-certs
2014-08-19 23:25:14,203 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-19 23:25:14,204 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-19 23:25:14,204 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-19 23:25:14,224 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-19 23:25:14,224 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-19 23:25:14,224 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-19 23:25:14,224 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-19 23:25:14,236 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-19 23:25:14,237 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-19 23:25:14,237 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-19 23:25:14,237 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/trust-certs
2014-08-19 23:25:14,239 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-19 23:25:14,240 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-19 23:25:14,240 INFO [main] - OUT -- DefaultCertMgr.java - deleteCert - 
2014-08-19 23:25:14,240 INFO [main] - IN -- CertMgr.java - logResult(result, desc, resultFile) - 
2014-08-19 23:25:14,240 INFO [main] - CertMgmt Operation Result : null
2014-08-19 23:25:14,241 INFO [main] - OUT -- CertMgr.java - logResult - 
2014-08-19 23:25:14,241 INFO [main] - OUT -- CertMgr.java - doOp - 
2014-08-19 23:25:14,241 INFO [main] - OUT -- CertMgr.java - mainIntenal -
```

b. To confirm that operation was successful on the filesystem level, let's check the tomcat trust directory:

```
[root@CUCM861 trust-certs]# ls -la
total 108
drwxr-xr-x 2 certbase ccmbase 4096 Aug 19 23:25 .
drwxr-xr-x 5 root     root    4096 Apr  4 12:47 ..
lrwxrwxrwx 1 certbase ccmbase   11 Aug 19 23:25 101f99a6.0 -> CUCM861.pem
lrwxrwxrwx 1 certbase ccmbase   42 Aug 19 23:25 7e0370f0.0 -> VeriSign_Class_3_Secure_Server_CA_-_G3.pem
-rwxr-xr-x 1 certbase ccmbase  939 Aug  2 23:36 CUCM861.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 23:36 CUCM861.description
-rwxr-xr-x 1 certbase ccmbase 1326 Aug  2 23:36 CUCM861.pem
-rwxr-xr-x 1 certbase ccmbase  941 Aug  2 22:51 CUCM861s.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 22:51 CUCM861s.description
-rwxr-xr-x 1 certbase ccmbase 1330 Aug  2 22:51 CUCM861s.pem
lrwxrwxrwx 1 certbase ccmbase   12 Aug 19 23:25 d0aacffb.0 -> CUCM861s.pem
-rwxr-xr-x 1 certbase ccmbase 3907 Aug 19 23:25 tomcat-trust.keystore
-rwxr-xr-x 1 certbase ccmbase 1520 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.der
-rwxr-xr-x 1 certbase ccmbase   44 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.description
-rwxr-xr-x 1 certbase ccmbase 2114 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.pem
```

As you can see 3 files has been removed (CUCM9X.pem, CUCM9X.der, CUCM9X.description) and the symbolic link.

c. CertCN service on the publisher and subscriber will be notified about the change in table CERTIFICATESERVICECERTIFICATEMAP by the DB change notification mechanism.

From the publisher node:

```
2014-08-19 23:25:13,811 INFO [Thread-5] - IN - process. changeData &colon; 
2014-08-19 23:25:13,812 INFO [Thread-5] - Inside CERTIFICATESERVICECERTIFICATEMAP - I option..
2014-08-19 23:25:13,812 DEBUG [Thread-5] - Updated Data in CERTIFICATESERVICECERTIFICATEMAP ::<msg><type>DBL</type><table>certificateservicecertificatemap</table><tableid>44</tableid><action>D</action><time>1408483513</time><old><cdrserver>2</cdrserver><cdrtime>1407158487</cdrtime><pkid>798ff6e1-e1d6-42e5-a4e6-30d9d7360d6d</pkid><fkcertificate>4152b36b-002e-68ac-711d-c373fa940779</fkcertificate><tkcertificateservice>6</tkcertificateservice><ifx_replcheck>6043699681953972226</ifx_replcheck></old></msg>
2014-08-19 23:25:18,818 INFO [Thread-5] - OUT - process.
```

Nothing needs to be done on the publisher node since all has been done by CM API. The same you can observe in the certCN logs on the subscriber.

d. Delete the same tomcat-trust certificate on the subscriber node perform almost the same operation as was observed on the publisher node. The only difference is a final step of remove the entry from CERTIFICATE table. From the logs of CM (only the part that contains the change):

```
2014-08-21 11:59:35,383 INFO [main] - OUT -- CertDBImpl.java - checkMultipleCertForProcessnode - 
2014-08-21 11:59:35,383 DEBUG [main] - DELETE FLAG :: isSrvMap=false :: isRoleMap=false :: isProcessnodeMap=false
2014-08-21 11:59:35,383 INFO [main] - IN -- CertDBImpl.java - deleteCertificateBySerialNo(con, certInfo) - ## certificate is removed from CERTIFICATE table 2014-08-21 11:59:35,383 DEBUG [main] - Delete query of CERTIFICATE :DELETE FROM CERTIFICATE WHERE PKID = "4152b36b-002e-68ac-711d-c373fa940779"
2014-08-21 11:59:35,383 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-21 11:59:35,596 INFO [main] - OUT -- CertDBImpl.java - deleteCertificateBySerialNo - 
2014-08-21 11:59:35,598 DEBUG [main] - Connection committed for deleteCertificate..
2014-08-21 11:59:35,598 DEBUG [main] - Closing the connection. Connection HashCode:6923467  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
```

Again certCN will be notified about the change in CERTIFICATESERVICECERTIFICATEMAP table on both nodes. No action will be done by certCN since all the work was done by CM.

### 4.C. Regenerate tomcat certificate on publisher node

In the third scenario you look at the process of tomcat.pem regeneration.

you can regenerate on the publisher node and next look  how this change propagates to the second node.

This operation consists of below steps:

a. regenerate action initiated under CM page. b. above triggers generate a new tomcat certificate and put it into the filesystem c. new tomcat certificate is inserted into DB (old one will be overwritten) by CM. This info will be replicated over DB replication. d. old tomcat-trust certificate is deleted from the filesystem (+remove it from the keystore) e. tomcat-trust is imported into the filesystem (+ corresponding DB entries are verified). f. certCN on the sub node kicks in and remove tomcat-trust from filesystem and from the keystore. g. finally the new one is reimported into the filesystem and readded to the keystore.

a. Hitting regenerate show us below output (timestamp 23:36):

Serial number of our new cert: Dec: 88769680872451706773275250466208361017 Hex: 42C86B2CF293630FE27BBDDC7FD02A39

Certificate saved in the filesystem (from root):

```
[root@CUCM861 tomcat]# pwd /usr/local/platform/.security/tomcat [root@CUCM861 tomcat]# ls -la certs
total 48
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 23:36 .
drwxr-xr-x 5 root     root    4096 Apr  4 12:47 ..
-rwxr-xr-x 1 certbase ccmbase  939 Aug  2 23:36 tomcat.der -rwxr-xr-x 1 certbase ccmbase   64 Aug  2 23:36 tomcat.description
-rwxr-xr-x 1 certbase ccmbase 2598 Aug  2 23:36 tomcat.keystore
-rwxr-xr-x 1 certbase ccmbase 1326 Aug  2 23:36 tomcat.pem [root@CUCM861 tomcat]#  ls -la trust-certs total 108
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 23:36 .
drwxr-xr-x 5 root     root    4096 Apr  4 12:47 ..
lrwxrwxrwx 1 certbase ccmbase   11 Aug  2 23:36 101f99a6.0 -> CUCM861.pem lrwxrwxrwx 1 certbase ccmbase   42 Aug  2 23:36 7e0370f0.0 -> VeriSign_Class_3_Secure_Server_CA_-_G3.pem
-rwxr-xr-x 1 certbase ccmbase  939 Aug  2 23:36 CUCM861.der -rwxr-xr-x 1 certbase ccmbase   44 Aug  2 23:36 CUCM861.description
-rwxr-xr-x 1 certbase ccmbase 1326 Aug  2 23:36 CUCM861.pem -rwxr-xr-x 1 certbase ccmbase  941 Aug  2 22:51 CUCM861s.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 22:51 CUCM861s.description
-rwxr-xr-x 1 certbase ccmbase 1330 Aug  2 22:51 CUCM861s.pem
lrwxrwxrwx 1 certbase ccmbase   12 Aug  2 23:36 d0aacffb.0 -> CUCM861s.pem
-rwxr-xr-x 1 certbase ccmbase 3907 Aug  2 23:36 tomcat-trust.keystore
-rwxr-xr-x 1 certbase ccmbase 1520 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.der
-rwxr-xr-x 1 certbase ccmbase   44 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.description
-rwxr-xr-x 1 certbase ccmbase 2114 Apr  4 12:47 VeriSign_Class_3_Secure_Server_CA_-_G3.pem
[root@CUCM861 tomcat]# md5sum certs/tomcat.der a0dd8031bcd3c269844df8a3fafd476c certs/tomcat.der
[root@CUCM861 tomcat]# md5sum trust-certs/CUCM861.der a0dd8031bcd3c269844df8a3fafd476c trust-certs/CUCM861.der
```

As you can see (based on the modification time) our new certificate is stored in certs directory (as tomcat.der ) and in trust-certs (as CUCM861.der ). MD5 checksum(md5sum) proves that this is the same certificate, stored twice. Symbolic link ( 101f99a6.0 -> CUCM861.pem ) is also updated.

b. The regeneration itself is done by CM. Let's take a closer look at the process of regeneration:

```
2014-08-02 23:36:40,962 INFO [main] - log4j configuration successful.
2014-08-02 23:36:40,977 INFO [main] - IN -- CertMgr.java - mainInternal(args) - 
2014-08-02 23:36:40,979 INFO [main] - decode ## operation invoked is "regenerate", if you would like to display the cert in OS ## Administration -> Security -> Certificate Management you would see "display" operation ## type. 2014-08-02 23:36:40,979 INFO [main] - op:regenerate ## you are going to regenerate tomcat cert, below the details of the cert are being listed 2014-08-02 23:36:40,979 INFO [main] - unit:tomcat
2014-08-02 23:36:40,979 INFO [main] - cert-dir:%2Fusr%2Flocal%2Fplatform%2F.security%2Ftomcat%2Fcerts%2Ftomcat
2014-08-02 23:36:40,979 INFO [main] - key-dir:%2Fusr%2Flocal%2Fplatform%2F.security%2Ftomcat%2Fkeys
2014-08-02 23:36:40,979 INFO [main] - logfile:%2Fvar%2Flog%2Factive%2Fplatform%2Flog%2Fcert-mgmt.log
2014-08-02 23:36:40,979 INFO [main] - resultfile:%2Fvar%2Flog%2Factive%2Fplatform%2Flog%2Fcertde-info.xml
2014-08-02 23:36:40,979 INFO [main] - type:certs
2014-08-02 23:36:41,006 INFO [main] - Parsed information
2014-08-02 23:36:41,006 INFO [main] - OrgName: CISCO
2014-08-02 23:36:41,006 INFO [main] - OrgUnit: TAC
2014-08-02 23:36:41,007 INFO [main] - Location: KRAKOW
2014-08-02 23:36:41,007 INFO [main] - Country: PL
2014-08-02 23:36:41,007 INFO [main] - State: MALOPOLSKA
2014-08-02 23:36:41,007 INFO [main] - Hostname: CUCM861
2014-08-02 23:36:41,007 INFO [main] - AlternateHostname: null
2014-08-02 23:36:41,007 INFO [main] - Domain Name: 
2014-08-02 23:36:41,007 INFO [main] - IPAddress: 10.48.46.29
2014-08-02 23:36:41,008 INFO [main] - In parseXML()
2014-08-02 23:36:41,021 INFO [main] - FQDN Name retrived by InetAddress : CUCM861
2014-08-02 23:36:41,021 INFO [main] - CN: CUCM861
2014-08-02 23:36:41,022 INFO [main] - Temp before mod is 
2014-08-02 23:36:41,022 INFO [main] - Temp afer mod is TAC
2014-08-02 23:36:41,022 INFO [main] - Temp in else is TAC
2014-08-02 23:36:41,022 INFO [main] - Temp before mod is 
2014-08-02 23:36:41,022 INFO [main] - Temp afer mod is TAC
2014-08-02 23:36:41,022 INFO [main] - Temp in else is TAC
2014-08-02 23:36:41,022 INFO [main] - OuFields are TAC
2014-08-02 23:36:41,022 DEBUG [main] - Field after encoding: TAC
2014-08-02 23:36:41,022 DEBUG [main] - Field after encoding: CISCO
2014-08-02 23:36:41,023 DEBUG [main] - Field after encoding: KRAKOW
2014-08-02 23:36:41,023 DEBUG [main] - Field after encoding: MALOPOLSKA
2014-08-02 23:36:41,023 DEBUG [main] - Field after encoding: PL
2014-08-02 23:36:41,026 INFO [main] - OU field is :TAC
2014-08-02 23:36:41,027 INFO [main] - SubjectDN :: CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL
2014-08-02 23:36:41,027 INFO [main] - IN -- CertMgr.java - getCertMgrObj(unit) - tomcat
2014-08-02 23:36:41,036 INFO [main] - OUT -- CertMgr.java - getCertMgrObj - com.cisco.cpi.certMgmt.manager.TomcatCertMgr@123b25c
2014-08-02 23:36:41,036 INFO [main] - Dummy loadProperties
2014-08-02 23:36:41,036 INFO [main] - IN -- CertMgr.java - doOp(info) - 
2014-08-02 23:36:41,037 DEBUG [main] - cert filename root: 'tomcat'
2014-08-02 23:36:41,037 DEBUG [main] - cert file parent directory: '/usr/local/platform/.security/tomcat/certs'
2014-08-02 23:36:41,037 DEBUG [main] - File created with certParentDir
2014-08-02 23:36:41,037 DEBUG [main] - DirCheck for certParentDir succeeded
2014-08-02 23:36:41,038 DEBUG [main] - File created with keyDir
2014-08-02 23:36:41,038 DEBUG [main] - DirCheck for keyDir succeeded ## API function for generating certificate is invoked 2014-08-02 23:36:41,039 DEBUG [main] - Calling genCertAPI() from regenCert()
2014-08-02 23:36:41,039 INFO [main] - IN -- DefaultCertMgr.java - genCertAPI(info) - 
2014-08-02 23:36:41,039 INFO [main] - parsed root path: '/usr/local/platform/.security/tomcat/certs'
2014-08-02 23:36:41,039 DEBUG [main] - cert file parent directory: '/usr/local/platform/.security/tomcat/certs'
2014-08-02 23:36:41,040 DEBUG [main] - tomcat Certificate keysize : 2048
2014-08-02 23:36:41,041 INFO [main] - parsed root path: '/usr/local/platform/.security/tomcat/certs'
2014-08-02 23:36:41,042 DEBUG [main] - SubjectAltName : null
2014-08-02 23:36:41,385 DEBUG [main] - Loading RSA providers explicitly...
2014-08-02 23:36:42,989 DEBUG [main] - RSA providers are loaded explicitly...
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.1=JsafeJCE
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.2=RsaJsse
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.3=BC
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.4=SUN
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.5=SunRsaSign
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.6=SunJSSE
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.7=SunJCE
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.8=SunJGSS
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.9=SunSASL
2014-08-02 23:36:42,989 DEBUG [main] - New security.provider.10=XMLDSig
2014-08-02 23:36:42,990 DEBUG [main] - New security.provider.11=SunPCSC ## at this moment generateCertificate() function is invoked which actually returns a new ## ertificate as a result 2014-08-02 23:36:42,990 INFO [main] - IN -- RSACryptoEngine.java - generateCertificate(..) - 
2014-08-02 23:36:43,003 INFO [main] - passphrase is ::LA20PvI2sezuPqph
2014-08-02 23:36:44,657 INFO [main] - OUT -- RSACryptoEngine.java - generateCertificate - 
2014-08-02 23:36:44,658 INFO [main] - IN -- RSACryptoEngine.java - loadCertificate(..) - ## certificate is written into filesystem and the owner (user:group) and rights are being ## adjusted 2014-08-02 23:36:45,009 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:45,009 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:45,009 DEBUG [main] - setOwnershipAndPermissions : certs
2014-08-02 23:36:45,009 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/certs'
2014-08-02 23:36:45,010 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,010 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/certs
2014-08-02 23:36:45,017 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,017 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/certs'
2014-08-02 23:36:45,018 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,018 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/certs
2014-08-02 23:36:45,021 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,021 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/certs'
2014-08-02 23:36:45,021 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,021 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/certs
2014-08-02 23:36:45,046 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,046 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:45,046 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:45,046 DEBUG [main] - setOwnershipAndPermissions : keys
2014-08-02 23:36:45,046 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/keys'
2014-08-02 23:36:45,046 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,046 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/keys
2014-08-02 23:36:45,051 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,051 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/keys'
2014-08-02 23:36:45,052 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,052 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/keys
2014-08-02 23:36:45,055 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,055 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/keys'
2014-08-02 23:36:45,055 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,055 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/keys
2014-08-02 23:36:45,061 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,061 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - ## description is generated and put into the description file 2014-08-02 23:36:45,061 INFO [main] - IN -- DefaultCertMgr.java - createDescriptionFile(name, description) - 
2014-08-02 23:36:45,063 INFO [main] - description is :Self-signed certificate generated by system
2014-08-02 23:36:45,063 INFO [main] - OUT -- DefaultCertMgr.java - createDescriptionFile - 
2014-08-02 23:36:45,064 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:45,064 DEBUG [main] - setOwnershipAndPermissions : tomcat.description
2014-08-02 23:36:45,064 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/certs/tomcat.description'
2014-08-02 23:36:45,064 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,064 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown certbase /usr/local/platform/.security/tomcat/certs/tomcat.description
2014-08-02 23:36:45,074 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,074 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/certs/tomcat.description'
2014-08-02 23:36:45,074 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,075 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp ccmbase /usr/local/platform/.security/tomcat/certs/tomcat.description
2014-08-02 23:36:45,077 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,077 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/certs/tomcat.description'
2014-08-02 23:36:45,077 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,077 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod 755 /usr/local/platform/.security/tomcat/certs/tomcat.description
2014-08-02 23:36:45,083 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,083 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:45,084 INFO [main] - IN -- CertUtil.java - populateCertInfo(cert, opInfo, certFilePemLocation) - 
2014-08-02 23:36:45,086 INFO [main] - IN -- CertUtil.java - getHostName(..) - 
2014-08-02 23:36:45,089 INFO [main] - OUT -- CertUtil.java - getHostName - CUCM861
2014-08-02 23:36:45,092 INFO [main] - IN -- CryptoUtil.java - saveAsPEM(..) - 
2014-08-02 23:36:45,098 INFO [main] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-02 23:36:45,098 INFO [main] - OUT -- CertUtil.java - populateCertInfo -
```

c. At this moment you have a new certificate ready on the filesystem level ( tomcat.pem in certs). CUCM861.pem in trust-certs is also here but has not been added at this stage. This is cover later. Now is the time to update our tomcat certificate in DB to share the change with other nodes.

Before regeneration you could see tomcat certificate in DB:

```
admin: run sql select c.pkid, c.serialnumber from certificate c, certificateservicecertificatemap m WHERE m.fkcertificate = c.pkid AND m.tkcertificateservice = '5' pkid serialnumber
==================================== ================================ 533dbbfc-78ce-b46f-7d64-cd2b7c536f6d 6cf5bc855b681f658f9e7506d3ec6ea5
a6b18f66-bf72-261d-8ecd-bfcea02add4e 68052e2e9cd6c979079e6449ff873031
```

As you can see there are two tomcat certificates in DB (for PUB and SUB), old tomcat cert had serialnumber = '6cf5bc855b681f658f9e7506d3ec6ea5'. PKID of our tomcat cert is ' 533dbbfc-78ce-b46f-7d64-cd2b7c536f6d ' and does not change when cert regeneration.

Check further CM log file (comments in snippet):

```
2014-08-02 23:36:45,099 INFO [main] - IN -- CertDBAction.java - insertCertificateInDB (certFiletoStore, info) - 
2014-08-02 23:36:45,099 INFO [main] - 

DBParameters ... 
PKID :		null
CN :		L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
serialNo :	42c86b2cf293630fe27bbddc7fd02a39
hostName :	CUCM861
issuerName :	L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
Certificate :	Not Printing huge Certificate String..
IPV4Address :	10.48.46.29
IPV6Address :	
TimeToLive :	NULL
UNIT :		tomcat
TYPE :		certs
ROLE :		null
RoleMoniker :	null
RoleEnum :null
SERVICE :		null
ServiceMoniker :	null
ServiceEnum :0

2014-08-02 23:36:45,099 INFO [main] - DB - Certifciate Store Plugin Handler is :com.cisco.ccm.certmgmt.db.CertDBImpl
2014-08-02 23:36:45,159 DEBUG [main] - Connection Initialized to localnode. Connection HashCode:17241377  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,159 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-02 23:36:45,160 DEBUG [main] - Try to get a connection from pool
2014-08-02 23:36:45,160 DEBUG [main] - getting local connection from Pool
2014-08-02 23:36:45,162 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-02 23:36:45,162 DEBUG [main] - There are currently 0 connection pool entries
2014-08-02 23:36:45,166 DEBUG [main] - Checking if connection limit has been reached for database
2014-08-02 23:36:45,167 DEBUG [main] - Connecting to publisher so max number of connections allowed is 100
2014-08-02 23:36:45,167 DEBUG [main] - Number of connections in use is 0
2014-08-02 23:36:45,167 DEBUG [main] - There is currently 1 connection pool entry
2014-08-02 23:36:45,168 DEBUG [main] - Number of available connections in pool: 0
2014-08-02 23:36:45,381 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@1a7789c> to connection list
2014-08-02 23:36:45,382 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@1a7789c> as used
2014-08-02 23:36:45,382 DEBUG [main] - Got connection from pool
2014-08-02 23:36:45,389 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-02 23:36:45,395 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,396 DEBUG [main] - Closing the connection. Connection HashCode:17241377  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,396 DEBUG [main] - Attempting to close connection
2014-08-02 23:36:45,396 DEBUG [main] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-02 23:36:45,396 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-02 23:36:45,397 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@1a7789c> from connection list
2014-08-02 23:36:45,399 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@1a7789c> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-02 23:36:45,399 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,399 INFO [main] - TYPETRUSTROLEMAP ::{TRUST_ROLE_DATA_SERVICE=24, TRUST_ROLE_PROVISIONING_SERVICE=23, TRUST_ROLE_SERVICEABILITY=27, TRUST_ROLES_CALLMANAGER_TFTP=2, PHONE_TRUST_ROLES_FIREWALL=6, ROLE_APPLICATION_SERVER=7, TRUST_ROLES_SAST=0, ROLE_SIGNALING_CALL_CONTROL=22, TRUST_ROLES_CALLMANAGER=1, TRUST_ROLES_UNKNOWN=255, TRUST_ROLE_NETWORK_ELEMENT=25, TRUST_ROLES_SRST=5, ROLE_CERTIFICATE_AUTHORITY=20, TRUST_ROLE_VPN=26, TRUST_ROLES_CAPF=4, TRUST_ROLES_TFTP=3, ROLE_AUTHENTICATION_AUTHORIZATION=21}
2014-08-02 23:36:45,399 INFO [main] - TYPESERVICEROLEMAP ::{Phone-VPN-trust=2, CallManager=3, Phone-CTL-trust=15, tomcat-trust=6, TVS=11, ipsec-trust=8, Phone-trust=1, Phone-SAST-trust=14, tomcat=5, userlicensing-trust=16, CAPF=9, ipsec=7, CAPF-trust=10, CallManager-trust=4, TVS-trust=12, directory-trust=13}
2014-08-02 23:36:45,399 INFO [main] - unitRoleMap ::{Phone-VPN-trust=[TRUST_ROLE_VPN], CallManager=[TRUST_ROLES_CALLMANAGER_TFTP, TRUST_ROLES_SAST], Phone-CTL-trust=[ROLE_APPLICATION_SERVER], tomcat-trust=[ROLE_APPLICATION_SERVER], TVS=[ROLE_AUTHENTICATION_AUTHORIZATION], ipsec-trust=[], Phone-trust=[ROLE_APPLICATION_SERVER], Phone-SAST-trust=[TRUST_ROLES_SAST, TRUST_ROLES_TFTP], tomcat=[ROLE_APPLICATION_SERVER], userlicensing-trust=[], CAPF=[TRUST_ROLES_CAPF], ipsec=[ROLE_APPLICATION_SERVER], CAPF-trust=[], CallManager-trust=[], TVS-trust=[], directory-trust=[]}
2014-08-02 23:36:45,400 INFO [main] - commonTrustStoreMap ::{}
2014-08-02 23:36:45,403 DEBUG [main] - Connection Initialized to Publisher. Connection HashCode:5823789  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,403 INFO [main] - IN -- CertDBImpl.java - insertCertificate(certInfo, con) - 
2014-08-02 23:36:45,404 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,404 DEBUG [main] - Try to get a connection from pool
2014-08-02 23:36:45,404 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-02 23:36:45,404 DEBUG [main] - There is currently 1 connection pool entry
2014-08-02 23:36:45,404 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@1a7789c> to connection list
2014-08-02 23:36:45,404 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@1a7789c> as used
2014-08-02 23:36:45,404 DEBUG [main] - Got connection from pool
2014-08-02 23:36:45,406 INFO [main] - IN -- CertDBImpl.java - populateRoleEnumServiceEnum(certInfo) - ## cert type is tomcat, you can see serviceEnum = 5 2014-08-02 23:36:45,407 INFO [main] - UNIT ::: tomcat
2014-08-02 23:36:45,407 INFO [main] - role ::: [ROLE_APPLICATION_SERVER]
2014-08-02 23:36:45,407 INFO [main] - roleEnum ::: [7]
2014-08-02 23:36:45,407 INFO [main] - service ::: null
2014-08-02 23:36:45,407 INFO [main] - serviceEnum ::: 5
2014-08-02 23:36:45,407 INFO [main] - OUT -- CertDBImpl.java - populateRoleEnumServiceEnum - 
2014-08-02 23:36:45,409 INFO [main] - IN -- CertDBUtil.java - getProcessNodeId(con, hostName, ipAddress, fqdn) - 
2014-08-02 23:36:45,409 INFO [main] - getProcessNodeId Query :SELECT PKID,NAME FROM PROCESSNODE WHERE UPPER(NAME)=UPPER("CUCM861") OR UPPER(NAME)=UPPER("10.48.46.29") OR UPPER(NAME)=UPPER("CUCM861")
2014-08-02 23:36:45,409 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,418 INFO [main] - ProcessNodeId:13f4b0d9-0bae-429a-a86e-625336a35bb6
2014-08-02 23:36:45,418 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,418 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,418 INFO [main] - OUT -- CertDBUtil.java - getProcessNodeId - 
2014-08-02 23:36:45,418 INFO [main] - IN -- CertDBImpl.java - getSelfSignedCertificate(certInfo, con) - 
2014-08-02 23:36:45,418 DEBUG [main] - getSelfSignedCertificate Query :SELECT A.PKID,SERVERNAME,SUBJECTNAME,ISSUERNAME,SERIALNUMBER,IPV4ADDRESS,IPV6ADDRESS,TIMETOLIVE, B.HASH FROM CERTIFICATE A, CERTIFICATEHASHMAP B, CERTIFICATESERVICECERTIFICATEMAP C WHERE A.PKID=B.FKCERTIFICATE AND A.PKID = C.FKCERTIFICATE AND C.TKCERTIFICATESERVICE = "5" AND A.SERVERNAME = "CUCM861"
2014-08-02 23:36:45,418 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,424 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,424 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,425 INFO [main] - OUT -- CertDBImpl.java - getSelfSignedCertificate - 
2014-08-02 23:36:45,425 INFO [main] - IN -- CertDBImpl.java - getPkidOfCertificate(hash, serverName, con) - ## looking for PKID of our cert 2014-08-02 23:36:45,425 DEBUG [main] - GetPKID Query :SELECT A.PKID FROM CERTIFICATE A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND B.HASH = "/hSVsEZT+yZeaxE+K0EM02n1Pgk="
2014-08-02 23:36:45,425 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,431 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,435 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,435 INFO [main] - OUT -- CertDBImpl.java - getPkidOfCertificate - 
2014-08-02 23:36:45,436 DEBUG [main] - Own certificate is regenerated. newCert is not available in DB.
2014-08-02 23:36:45,436 DEBUG [main] - INSERT FLAG :: isCertUpdate=true :: doNothing=false ## finally certificate is inserted. In fact this is an update since The same is used ## PKID of the tomcat cert as it was prior regeneration 2014-08-02 23:36:45,436 DEBUG [main] - INSERT/UPDATE Query of CERTIFICATE : UPDATE CERTIFICATE SET SERVERNAME="CUCM861", SUBJECTNAME="L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL", ISSUERNAME="L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL", SERIALNUMBER="42c86b2cf293630fe27bbddc7fd02a39", CERTIFICATE="-----BEGIN CERTIFICATE-----
MIIDpzCCAo+gAwIBAgIQQshrLPKTYw/ie73cf9AqOTANBgkqhkiG9w0BAQUFADBj
MQswCQYDVQQGEwJQTDEOMAwGA1UEChMFQ0lTQ08xDDAKBgNVBAsTA1RBQzEQMA4G
A1UEAxMHQ1VDTTg2MTETMBEGA1UECBMKTUFMT1BPTFNLQTEPMA0GA1UEBxMGS1JB
S09XMB4XDTE0MDgwMjIxMzY0NFoXDTE5MDgwMTIxMzY0M1owYzELMAkGA1UEBhMC
UEwxDjAMBgNVBAoTBUNJU0NPMQwwCgYDVQQLEwNUQUMxEDAOBgNVBAMTB0NVQ004
NjExEzARBgNVBAgTCk1BTE9QT0xTS0ExDzANBgNVBAcTBktSQUtPVzCCASIwDQYJ
KoZIhvcNAQEBBQADggEPADCCAQoCggEBALRs5cFzI5Yrq/eXoDHs2gc+AhY+OPeW
AHZsQ5+x3TXXiRQ5/SuIyd6VFLbwD6QtsFEeynF6m3mWVYttXH1d9rl7M4/I81JM
eMUSlJXxmlbdNDZUn/M4BhhEuZyTmJpfkgrHbNJF67Lzjg8Moc7S34f43X83yPFl
Yfx6YdZKAfIY62oj5WyV6RdHKZYCtY5FEvN3eAKP0mACnMXe8AN2iWnAlrOYgOZ3
oqAI63UXN5cXtdRftM6LlIaSHviCi1jsg0iytBw0QgQBtKKOTuMrTHbcjVkDJNZ3
SsaPGk71Sg1sJ3Un7E3AIj6hRXsVK9iMEXiwztqpxRhRLT+SuuItQysCAwEAAaNX
MFUwCwYDVR0PBAQDAgK8MCcGA1UdJQQgMB4GCCsGAQUFBwMBBggrBgEFBQcDAgYI
KwYBBQUHAwUwHQYDVR0OBBYEFPOxKMSHC4gnQQqIgLAgxQjIHOsrMA0GCSqGSIb3
DQEBBQUAA4IBAQBVsWFzSC1nLTYKuOPs4RtOUQXfuUMHLhI74QoBJs98A8a8w1Kg
M8ilXUkBg6VZ37xgYm2uaLTCunXeG/EiNx9nkC+kgJ9y78Q4jmRh2//wqdvAkI+R
R9745RRNtD4xS3svv3uGSljEGd1eCC76NUWpQAWezz0A1AEAe/EWO7h1yZVRqhuD
hq5vLVNrH0gQkjve56/K7E9E83PqVO9JTAGRvjL9/uRpeooucACJYI9WPyXMYa6w
sIpCqFRLocYIUGCy9ufrof1vptawOJQGZ9Z9kW2SpanRD2LJunqgY8Vbveq/7Z2x
ndm8j36Lyn4IrESrk7Umprm27fN8KktYvMaD
-----END CERTIFICATE-----
", IPV4ADDRESS="10.48.46.29", IPV6ADDRESS="", TIMETOLIVE=NULL WHERE PKID = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d"
2014-08-02 23:36:45,436 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,447 INFO [main] - IN -- CertDBImpl.java - updateCertificateHashMap(certInfo, con) - 
2014-08-02 23:36:45,448 DEBUG [main] - Update query of CERTIFICATEHASHMAP :UPDATE CERTIFICATEHASHMAP SET HASH = "/hSVsEZT+yZeaxE+K0EM02n1Pgk=" WHERE FKCERTIFICATE = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" 
2014-08-02 23:36:45,448 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,452 INFO [main] - OUT -- CertDBImpl.java - updateCertificateHashMap - 
2014-08-02 23:36:45,452 INFO [main] - IN -- CertDBImpl.java - insertCertSrvCertMap(certInfo, con) - 
2014-08-02 23:36:45,452 INFO [main] - IN -- CertDBImpl.java - checkExistingCertificateServiceMapping(certInfo, serviceEnum, con) - 
2014-08-02 23:36:45,452 DEBUG [main] - checkExistingTrustCertificateForService Query :SELECT PKID,FKCERTIFICATE, TKCERTIFICATESERVICE FROM CERTIFICATESERVICECERTIFICATEMAP  WHERE FKCERTIFICATE = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND TKCERTIFICATESERVICE= "5"
2014-08-02 23:36:45,453 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,455 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,456 INFO [main] - Connection/Statement/Resultset is closed properly. ## CM verifies if there is a proper mapping for the new cert in the ## CERTIFICATESERVICECERTIFICATEMAP table. There is so no need for update 2014-08-02 23:36:45,456 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertificateServiceMapping - 
2014-08-02 23:36:45,456 DEBUG [main] - Certificate to be inserted in CERTIFICATESERVICECERTIFICATEMAP table :tomcat ::PKID :533dbbfc-78ce-b46f-7d64-cd2b7c536f6d ::toInsertInCertSrvMap:false
2014-08-02 23:36:45,456 DEBUG [main] - CertService mapping entry already exists..
2014-08-02 23:36:45,456 INFO [main] - OUT -- CertDBImpl.java - insertCertSrvCertMap - 
2014-08-02 23:36:45,456 INFO [main] - IN -- CertDBImpl.java - insertCertTrustRoleMap(certInfo, log, con) - 
2014-08-02 23:36:45,456 INFO [main] - IN -- CertDBImpl.java - checkExistingCertificateRoleMapping(certInfo, roleEnum, con) - ## the same check for CERTIFICATETRUSTROLEMAP table. It is there, nothing to udpate. 2014-08-02 23:36:45,456 DEBUG [main] - checkExistingTrustCertificateForRole Query :SELECT PKID,FKCERTIFICATE, TKTRUSTROLE FROM CERTIFICATETRUSTROLEMAP WHERE FKCERTIFICATE = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND TKTRUSTROLE= "7"
2014-08-02 23:36:45,456 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,459 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,459 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,459 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertificateRoleMapping - 
2014-08-02 23:36:45,459 DEBUG [main] - Certificate to be inserted in CERTIFICATETRUSTROLEMAP table :tomcat ::PKID :533dbbfc-78ce-b46f-7d64-cd2b7c536f6d ::toInsertInCertSrvMap:false
2014-08-02 23:36:45,459 DEBUG [main] - CertRole mapping entry already exists..
2014-08-02 23:36:45,459 INFO [main] - OUT -- CertDBImpl.java - insertCertTrustRoleMap - 
2014-08-02 23:36:45,459 INFO [main] - IN -- CertDBImpl.java - insertCertProcessNodeMap(certInfo, con) - 
2014-08-02 23:36:45,459 INFO [main] - IN -- CertDBImpl.java - checkExistingCertProcessNodeMapping(certInfo, con) - 
2014-08-02 23:36:45,459 DEBUG [main] - checkExistingCertProcessNodeMapping Query :SELECT PKID,FKCERTIFICATE, FKPROCESSNODE,SERVERNAME FROM CERTIFICATEPROCESSNODEMAP WHERE FKCERTIFICATE="533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND FKPROCESSNODE="13f4b0d9-0bae-429a-a86e-625336a35bb6" AND SERVERNAME="CUCM861"
2014-08-02 23:36:45,460 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[1]connectToPubByDefault[true]
2014-08-02 23:36:45,462 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,463 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,463 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertProcessNodeMapping - 
2014-08-02 23:36:45,463 DEBUG [main] - CertProcessNode mapping entry already exists..
2014-08-02 23:36:45,463 INFO [main] - OUT -- CertDBImpl.java - insertCertProcessNodeMap - 
2014-08-02 23:36:45,467 DEBUG [main] - Connection committed for insertCertificate..
2014-08-02 23:36:45,467 DEBUG [main] - Insertion of Certificate in DB is Successful.
2014-08-02 23:36:45,467 INFO [main] - OUT -- CertDBImpl.java - insertCertificate - 
2014-08-02 23:36:45,467 DEBUG [main] - Closing the connection. Connection HashCode:5823789  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,468 DEBUG [main] - Attempting to close connection
2014-08-02 23:36:45,468 DEBUG [main] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-02 23:36:45,468 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-02 23:36:45,468 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@1a7789c> from connection list
2014-08-02 23:36:45,468 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@1a7789c> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-02 23:36:45,468 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,468 INFO [main] - DB - Generate Certificate operation in DB is successful
2014-08-02 23:36:45,468 INFO [main] - OUT -- CertDBAction.java - insertCertificateInDB - 
2014-08-02 23:36:45,468 INFO [main] - OUT -- DefaultCertMgr.java - genCertAPI - Self-signed certificate generated by system.
2014-08-02 23:36:45,469 INFO [main] - IN -- CertUtil.java - sendAlarm(alarmName, alarmParamName, alarmParamValue) - 
2014-08-02 23:36:45,469 DEBUG [main] - Sending alarm for :: TomcatCertRegen :: Message :: The tomcat certificate is regenerated
2014-08-02 23:36:45,471 DEBUG [main] - AlarmSender: getInstance
```

d. As you remember you could see the same cert in the filesystem as tomcat and tomcat-trust. Till now only the tomcat one has been properly updated in the filesystem. Let's follow further CM log to see how tomcat-trust is updated on this node:

```
2014-08-02 23:36:45,518 INFO [main] - OUT -- CertUtil.java - sendAlarm - 
2014-08-02 23:36:45,518 INFO [main] - IN -- TomcatCertMgr.java - copyToTomcatTrustStore(info) - 
2014-08-02 23:36:45,518 INFO [main] - IN -- TomcatCertMgr.java - deleteCertFromTomcatTrustStore(info) - 
2014-08-02 23:36:45,519 INFO [main] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:45,520 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:45,520 INFO [main] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-02 23:36:45,520 DEBUG [main] - parseCNfromDN( certSubjDN: 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL')
2014-08-02 23:36:45,520 DEBUG [main] - Truncating CN 'CUCM861,OU=TAC,O=CISCO,C=PL' -> 'CUCM861'
2014-08-02 23:36:45,520 INFO [main] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-02 23:36:45,520 DEBUG [main] - Parsed CN 'CUCM861' from DN 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL' ## first you need to delete old tomcat-trust certificate on the filesystem 2014-08-02 23:36:45,521 DEBUG [main] - Old Cert to be deleted during import : /usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
2014-08-02 23:36:45,521 INFO [main] - IN -- DefaultCertMgr.java - deleteCert(info) - 
decode:     true
op:         delete
unit:       tomcat-trust
keystoreUnit:tomcat-trust
logFile:    /var/log/active/platform/log/cert-mgmt.log
resultFile: /var/log/active/platform/log/certde-info.xml
keyDir:     /usr/local/platform/.security/tomcat/keys
certDir:    /usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
srcCert:    null
type:       trust-certs
rootCACert: null
trustDir:   null
DNAME:      CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL
description:null
isDBInsert:true

2014-08-02 23:36:45,521 INFO [main] - parsed filename: 'CUCM861.pem'
2014-08-02 23:36:45,521 DEBUG [main] - filename: 'CUCM861.pem'
2014-08-02 23:36:45,521 DEBUG [main] - fileRoot: 'CUCM861'
2014-08-02 23:36:45,521 INFO [main] - IN -- DefaultCertMgr.java - deleteDERandPEM(filenameRoot, parentDir, info) - 
2014-08-02 23:36:45,521 DEBUG [main] - ParentDir:/usr/local/platform/.security/tomcat/trust-certsFileName.(DER/PEM):CUCM861
2014-08-02 23:36:45,521 INFO [main] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:45,538 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:45,539 INFO [main] - IN -- CertUtil.java - populateCertInfo(cert, opInfo, certFilePemLocation) - 
2014-08-02 23:36:45,539 INFO [main] - IN -- CertUtil.java - getHostName(..) - 
2014-08-02 23:36:45,539 INFO [main] - OUT -- CertUtil.java - getHostName - CUCM861
2014-08-02 23:36:45,540 INFO [main] - IN -- CryptoUtil.java - saveAsPEM(..) - 
2014-08-02 23:36:45,540 INFO [main] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-02 23:36:45,540 INFO [main] - OUT -- CertUtil.java - populateCertInfo - ## the same should be done on the DB level. CM consider deleting the the association ## for this tomcat-trust cert from corresponding tables: CERTIFICATESERVICECERTIFICATEMAP, ## CERTIFICATEPROCESSNODEMAP and CERTIFICATETRUSTROLEMAP. As you see this does not ## happen since the certificate itself has not been deleted so FKCERTIFICATE in those ## tables become "null for this certificate" (cert still exists, has been 
## updated only) 2014-08-02 23:36:45,540 INFO [main] - IN -- CertDBAction.java - deleteCertificateInDB(certInfo) - 
2014-08-02 23:36:45,540 INFO [main] - 

DBParameters ... 
PKID :		null
CN :		L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
serialNo :	6cf5bc855b681f658f9e7506d3ec6ea5
hostName :	CUCM861
issuerName :	L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
Certificate :	Not Printing huge Certificate String..
IPV4Address :	10.48.46.29
IPV6Address :	
TimeToLive :	NULL
UNIT :		tomcat-trust
TYPE :		trust-certs
ROLE :		null
RoleMoniker :	null
RoleEnum :null
SERVICE :		null
ServiceMoniker :	null
ServiceEnum :0

2014-08-02 23:36:45,540 INFO [main] - DB - Certifciate Store Plugin Handler is :com.cisco.ccm.certmgmt.db.CertDBImpl
2014-08-02 23:36:45,541 INFO [main] - IN -- CertDBImpl.java - deleteCertificate(certInfo) - 
2014-08-02 23:36:45,542 DEBUG [main] - Connection Initialized to Publisher. Connection HashCode:12578138  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,542 INFO [main] - IN -- CertDBImpl.java - getPkidOfCertificate(hash, serverName, con) - 
2014-08-02 23:36:45,542 DEBUG [main] - GetPKID Query :SELECT A.PKID FROM CERTIFICATE A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND B.HASH = "/XB5QwYXgqrUTFZ2CDgT7BkSxNs="
2014-08-02 23:36:45,542 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,542 DEBUG [main] - Try to get a connection from pool
2014-08-02 23:36:45,542 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl>
2014-08-02 23:36:45,542 DEBUG [main] - There is currently 1 connection pool entry
2014-08-02 23:36:45,543 DEBUG [main] - Checking if connection limit has been reached for database
2014-08-02 23:36:45,543 DEBUG [main] - Connecting to publisher so max number of connections allowed is 100
2014-08-02 23:36:45,543 DEBUG [main] - Number of connections in use is 0
2014-08-02 23:36:45,543 DEBUG [main] - There are currently 2 connection pool entries
2014-08-02 23:36:45,544 DEBUG [main] - Number of available connections in pool: 0
2014-08-02 23:36:45,590 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@77eb97> to connection list
2014-08-02 23:36:45,590 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@77eb97> as used
2014-08-02 23:36:45,590 DEBUG [main] - Got connection from pool
2014-08-02 23:36:45,596 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,599 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,599 INFO [main] - OUT -- CertDBImpl.java - getPkidOfCertificate - 
2014-08-02 23:36:45,599 DEBUG [main] - Closing the connection. Connection HashCode:12578138  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,600 DEBUG [main] - Attempting to close connection
2014-08-02 23:36:45,600 DEBUG [main] - Removing connection <database, jdbcurl> from ConnectionManager list
2014-08-02 23:36:45,600 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-02 23:36:45,600 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@77eb97> from connection list
2014-08-02 23:36:45,600 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@77eb97> is not closed, adding it back to the pool entry <database,jdbcurl>
2014-08-02 23:36:45,600 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,602 DEBUG [main] - Connection Initialized to Publisher. Connection HashCode:17578504  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,602 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,602 DEBUG [main] - Try to get a connection from pool
2014-08-02 23:36:45,602 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl>
2014-08-02 23:36:45,602 DEBUG [main] - There are currently 2 connection pool entries
2014-08-02 23:36:45,602 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@77eb97> to connection list
2014-08-02 23:36:45,603 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@77eb97> as used
2014-08-02 23:36:45,603 DEBUG [main] - Got connection from pool
2014-08-02 23:36:45,604 INFO [main] - IN -- CertDBImpl.java - deleteCertFromCertSrvCertMap(con, serialNo, subjectName, serviceEnum) - ## you can see it here ... 2014-08-02 23:36:45,605 DEBUG [main] - Delete query of CERTIFICATESERVICECERTIFICATEMAP :DELETE FROM CERTIFICATESERVICECERTIFICATEMAP WHERE TKCERTIFICATESERVICE = "6"  AND FKCERTIFICATE = "null"
2014-08-02 23:36:45,605 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,618 INFO [main] - OUT -- CertDBImpl.java - deleteCertFromCertSrvCertMap - 
2014-08-02 23:36:45,618 INFO [main] - IN -- CertDBImpl.java - deleteCertFromCertProcessNodeMap(con, certInfo) - ## here ... 2014-08-02 23:36:45,619 DEBUG [main] - Delete query of CERTIFICATEPROCESSNODEMAP :DELETE FROM CERTIFICATEPROCESSNODEMAP WHERE FKCERTIFICATE="null" AND SERVERNAME = "CUCM861"
2014-08-02 23:36:45,619 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,624 INFO [main] - OUT -- CertDBImpl.java - deleteCertFromCertProcessNodeMap - 
2014-08-02 23:36:45,624 DEBUG [main] - Certificate to be deleted UNIT: tomcat-trust :: RoleMoniker :ROLE_APPLICATION_SERVER :: RoleEnum :7 :: ServiceEnum :6
2014-08-02 23:36:45,624 INFO [main] - IN -- CertDBImpl.java - checkMultipleUnitForSameRole(con, roleMoniker, unit, certInfo) - 
2014-08-02 23:36:45,624 DEBUG [main] - checkMultipleUnitForSameRole : SELECT PKID,FKCERTIFICATE, TKCERTIFICATESERVICE,NAME UNIT FROM CERTIFICATESERVICECERTIFICATEMAP,TYPECERTIFICATESERVICE  WHERE ENUM=TKCERTIFICATESERVICE AND FKCERTIFICATE ="null" AND NAME != "tomcat-trust"
2014-08-02 23:36:45,624 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,649 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,649 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,649 INFO [main] - OUT -- CertDBImpl.java - checkMultipleUnitForSameRole - 
2014-08-02 23:36:45,649 INFO [main] - IN -- CertDBImpl.java - deleteCertFromTypeTrustRole(con, certInfo, roleEnum) - ## and here 2014-08-02 23:36:45,649 DEBUG [main] - Delete query of CERTIFICATETRUSTROLEMAP :DELETE FROM CERTIFICATETRUSTROLEMAP WHERE  TKTRUSTROLE = "7" AND FKCERTIFICATE = "null"
2014-08-02 23:36:45,649 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,652 INFO [main] - OUT -- CertDBImpl.java - deleteCertFromTypeTrustRole - 
2014-08-02 23:36:45,653 INFO [main] - IN -- CertDBImpl.java - checkMultipleCertForSrv(pkid, con) - 
2014-08-02 23:36:45,653 DEBUG [main] - checkMultipleCertForSrv : SELECT PKID,FKCERTIFICATE, TKCERTIFICATESERVICE FROM CERTIFICATESERVICECERTIFICATEMAP WHERE FKCERTIFICATE = "null"
2014-08-02 23:36:45,653 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,655 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,655 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,655 INFO [main] - OUT -- CertDBImpl.java - checkMultipleCertForSrv - 
2014-08-02 23:36:45,655 INFO [main] - IN -- CertDBImpl.java - checkMultipleCertForRole(certInfo, con) - 
2014-08-02 23:36:45,655 DEBUG [main] - checkMultipleCertForRole : SELECT PKID,FKCERTIFICATE, TKTRUSTROLE FROM CERTIFICATETRUSTROLEMAP WHERE FKCERTIFICATE = "null"
2014-08-02 23:36:45,655 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,657 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,657 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,657 INFO [main] - OUT -- CertDBImpl.java - checkMultipleCertForRole - 
2014-08-02 23:36:45,657 INFO [main] - IN -- CertDBImpl.java - checkMultipleCertForProcessnode(certInfo, con) - 
2014-08-02 23:36:45,657 DEBUG [main] - checkMultipleCertForProcessnode : SELECT PKID,FKCERTIFICATE,FKPROCESSNODE,SERVERNAME FROM CERTIFICATEPROCESSNODEMAP WHERE FKCERTIFICATE='null'
2014-08-02 23:36:45,658 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,660 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:45,661 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,661 INFO [main] - OUT -- CertDBImpl.java - checkMultipleCertForProcessnode - 
2014-08-02 23:36:45,661 DEBUG [main] - DELETE FLAG :: isSrvMap=false :: isRoleMap=false :: isProcessnodeMap=false
2014-08-02 23:36:45,661 INFO [main] - IN -- CertDBImpl.java - deleteCertificateBySerialNo(con, certInfo) - ## finally it tries to remove all certificates from CERTIFICATE table with null PKID. ## Nothing will be deleted of course. 2014-08-02 23:36:45,661 DEBUG [main] - Delete query of CERTIFICATE :DELETE FROM CERTIFICATE WHERE PKID = "null"
2014-08-02 23:36:45,661 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:45,664 INFO [main] - OUT -- CertDBImpl.java - deleteCertificateBySerialNo - 
2014-08-02 23:36:45,664 DEBUG [main] - Connection committed for deleteCertificate..
2014-08-02 23:36:45,664 DEBUG [main] - Closing the connection. Connection HashCode:17578504  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,664 DEBUG [main] - Attempting to close connection
2014-08-02 23:36:45,665 DEBUG [main] - Removing connection <database, jdbcurl> from ConnectionManager list
2014-08-02 23:36:45,665 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-02 23:36:45,665 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@77eb97> from connection list
2014-08-02 23:36:45,665 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@77eb97> is not closed, adding it back to the pool entry <database,jdbcurl>
2014-08-02 23:36:45,665 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,665 DEBUG [main] - Connection released from CertDBImpl.deleteCertificate method.
2014-08-02 23:36:45,665 INFO [main] - OUT -- CertDBImpl.java - deleteCertificate - 
2014-08-02 23:36:45,665 INFO [main] - OUT -- CertDBAction.java - deleteCertificateInDB - 
2014-08-02 23:36:45,665 INFO [main] - OUT -- DefaultCertMgr.java - deleteDERandPEM - 
2014-08-02 23:36:45,665 DEBUG [main] - deleteDERandPEM: sCertDir = /usr/local/platform/.security/tomcat/trust-certs --- sAlias = CUCM861
2014-08-02 23:36:45,665 INFO [main] - IN -- TomcatCertMgr.java - removeFromKeyStore(..) - 
2014-08-02 23:36:45,666 INFO [main] - IN -- RSACryptoEngine.java - removeFromKeyStore(keystoreFile, keystorePass, alias) - 
2014-08-02 23:36:45,666 INFO [main] - IN -- RSACryptoEngine.java - loadKeyStore(keystoreFile, keystorePass) - 
2014-08-02 23:36:45,846 INFO [main] - OUT -- RSACryptoEngine.java - loadKeyStore - ## old tomcat-trust certificate is being removed from key store 2014-08-02 23:36:45,880 DEBUG [main] - Removing certificate from keystore : CUCM861
2014-08-02 23:36:45,880 DEBUG [main] - Size of the keystore after delete is : 2
2014-08-02 23:36:45,880 INFO [main] - OUT -- RSACryptoEngine.java - removeFromKeyStore - 
2014-08-02 23:36:45,880 INFO [main] - OUT -- TomcatCertMgr.java - removeFromKeyStore - 
2014-08-02 23:36:45,882 INFO [main] - trustdir ::/usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:45,883 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,883 DEBUG [main] - Executing command from Util.sysExec :  python /usr/local/platform/bin/c_rehash.py /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:45,993 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:45,995 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:45,995 DEBUG [main] - setOwnershipAndPermissions : trust-certs
2014-08-02 23:36:45,995 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:45,995 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:45,996 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,005 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,010 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,010 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,010 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,020 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,020 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,020 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,020 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,027 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,027 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:46,027 INFO [main] - OUT -- DefaultCertMgr.java - deleteCert - 
2014-08-02 23:36:46,027 INFO [main] - OUT -- TomcatCertMgr.java - deleteCertFromTomcatTrustStore -
```

e. At this moment you do not have tomcat-trust cert in the filesystem. CM will create it and reimport it to the trust store:

```
2014-08-02 23:36:46,027 INFO [main] - IN -- TomcatCertMgr.java - importCertToTomcatTrustStore(info) - 
2014-08-02 23:36:46,028 INFO [main] - IN -- DefaultCertMgr.java - importCert(info) - 
decode:     true
op:         import
unit:       tomcat-trust
keystoreUnit:tomcat-trust
logFile:    /var/log/active/platform/log/cert-mgmt.log
resultFile: /var/log/active/platform/log/certde-info.xml
keyDir:     /usr/local/platform/.security/tomcat/keys
certDir:    /usr/local/platform/.security/tomcat/trust-certs
srcCert:    /usr/local/platform/.security/tomcat/certs/tomcat.pem
type:       trust-certs
rootCACert: null
trustDir:   null
DNAME:      CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL
description:Trust Certificate
isDBInsert:true

2014-08-02 23:36:46,028 INFO [main] - IN -- DefaultCertMgr.java - loadInputCert(info) - 
2014-08-02 23:36:46,028 INFO [main] - IN -- RSACryptoEngine.java - loadCertificates(..) - 
2014-08-02 23:36:46,028 INFO [main] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,029 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,030 INFO [main] - OUT -- RSACryptoEngine.java - loadCertificates - 
2014-08-02 23:36:46,030 INFO [main] - OUT -- DefaultCertMgr.java - loadInputCert - Successfully loaded input cert
2014-08-02 23:36:46,030 DEBUG [main] - Checking validity of cert
2014-08-02 23:36:46,030 INFO [main] - Verifying certificate L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
2014-08-02 23:36:46,030 INFO [main] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-02 23:36:46,030 DEBUG [main] - parseCNfromDN( certSubjDN: 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL')
2014-08-02 23:36:46,030 DEBUG [main] - Truncating CN 'CUCM861,OU=TAC,O=CISCO,C=PL' -> 'CUCM861'
2014-08-02 23:36:46,030 INFO [main] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-02 23:36:46,030 DEBUG [main] - Parsed CN 'CUCM861' from DN 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL' ## certificate is being created on the filesystem 2014-08-02 23:36:46,030 INFO [main] - trying to load cert from trust store ::/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
2014-08-02 23:36:46,030 INFO [main] - cert not available in trust store ::L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
2014-08-02 23:36:46,031 INFO [main] - IN -- DefaultCertMgr.java - importTrustCert(info, cert) - 
2014-08-02 23:36:46,031 INFO [main] - IN -- DefaultCertMgr.java - saveToTrustStore(info, cert) - 
2014-08-02 23:36:46,031 ERROR [main] - trust directory parameter is null
2014-08-02 23:36:46,031 INFO [main] - IN -- DefaultCertMgr.java - saveTrustCert(cert, targetDir, certType) - 
2014-08-02 23:36:46,031 INFO [main] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-02 23:36:46,031 DEBUG [main] - parseCNfromDN( certSubjDN: 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL')
2014-08-02 23:36:46,031 DEBUG [main] - Truncating CN 'CUCM861,OU=TAC,O=CISCO,C=PL' -> 'CUCM861'
2014-08-02 23:36:46,031 INFO [main] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-02 23:36:46,031 DEBUG [main] - Parsed CN 'CUCM861' from DN 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL'
2014-08-02 23:36:46,031 INFO [main] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-02 23:36:46,031 DEBUG [main] - parseCNfromDN( certSubjDN: 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL')
2014-08-02 23:36:46,031 DEBUG [main] - Truncating CN 'CUCM861,OU=TAC,O=CISCO,C=PL' -> 'CUCM861'
2014-08-02 23:36:46,031 INFO [main] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-02 23:36:46,031 DEBUG [main] - Parsed CN 'CUCM861' from DN 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL'
2014-08-02 23:36:46,031 DEBUG [main] - target filename for imported cert: 'CUCM861.pem'
2014-08-02 23:36:46,032 DEBUG [main] - existing certificate with same filename not found.
2014-08-02 23:36:46,032 DEBUG [main] - Saving PEM encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem'
2014-08-02 23:36:46,032 INFO [main] - IN -- CryptoUtil.java - saveAsPEM(..) - File : /usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
2014-08-02 23:36:46,032 INFO [main] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-02 23:36:46,033 DEBUG [main] - Saving DER encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.der'
2014-08-02 23:36:46,033 INFO [main] - OUT -- DefaultCertMgr.java - saveTrustCert - 
2014-08-02 23:36:46,033 INFO [main] - IN -- TomcatCertMgr.java - saveToKeyStore(..) - 
2014-08-02 23:36:46,033 INFO [main] - IN -- RSACryptoEngine.java - saveToKeyStore(keystoreFile, keystorePass, x509Certificate, alias) - 
2014-08-02 23:36:46,033 INFO [main] - IN -- RSACryptoEngine.java - loadKeyStore(keystoreFile, keystorePass) - 
2014-08-02 23:36:46,050 INFO [main] - OUT -- RSACryptoEngine.java - loadKeyStore - 
2014-08-02 23:36:46,050 INFO [main] - Size of the keystore before import is : 2
2014-08-02 23:36:46,050 INFO [main] - Importing certificate : CUCM861
2014-08-02 23:36:46,061 INFO [main] - Size of the keystore after import is : 3
2014-08-02 23:36:46,061 INFO [main] - OUT -- RSACryptoEngine.java - saveToKeyStore - 
2014-08-02 23:36:46,061 INFO [main] - OUT -- TomcatCertMgr.java - saveToKeyStore - 
2014-08-02 23:36:46,062 DEBUG [main] - TrustCert description filename : 'CUCM861.description'
2014-08-02 23:36:46,062 INFO [main] - IN -- DefaultCertMgr.java - createDescriptionFile(name, description) - 
2014-08-02 23:36:46,062 INFO [main] - description is :Trust Certificate
2014-08-02 23:36:46,062 INFO [main] - OUT -- DefaultCertMgr.java - createDescriptionFile - 
2014-08-02 23:36:46,062 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:46,062 DEBUG [main] - setOwnershipAndPermissions : CUCM861.description
2014-08-02 23:36:46,063 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description'
2014-08-02 23:36:46,063 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,063 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown certbase /usr/local/platform/.security/tomcat/trust-certs/CUCM861.description
2014-08-02 23:36:46,066 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,066 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description'
2014-08-02 23:36:46,067 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,067 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp ccmbase /usr/local/platform/.security/tomcat/trust-certs/CUCM861.description
2014-08-02 23:36:46,069 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,069 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description'
2014-08-02 23:36:46,069 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,069 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod 755 /usr/local/platform/.security/tomcat/trust-certs/CUCM861.description
2014-08-02 23:36:46,073 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,073 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:46,073 INFO [main] - OUT -- DefaultCertMgr.java - saveToTrustStore - 
2014-08-02 23:36:46,074 INFO [main] - trustdir ::/usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,074 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,074 DEBUG [main] - Executing command from Util.sysExec :  python /usr/local/platform/bin/c_rehash.py /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,140 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,140 INFO [main] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:46,140 DEBUG [main] - setOwnershipAndPermissions : trust-certs
2014-08-02 23:36:46,141 DEBUG [main] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,141 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,141 DEBUG [main] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,144 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,144 DEBUG [main] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,144 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,144 DEBUG [main] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,147 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,147 DEBUG [main] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,148 INFO [main] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,148 DEBUG [main] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,152 INFO [main] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,152 INFO [main] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:46,152 INFO [main] - IN -- CertUtil.java - populateCertInfo(cert, opInfo, certFilePemLocation) - 
2014-08-02 23:36:46,156 INFO [main] - IN -- CertUtil.java - getHostName(..) - 
2014-08-02 23:36:46,156 INFO [main] - OUT -- CertUtil.java - getHostName - CUCM861
2014-08-02 23:36:46,156 INFO [main] - IN -- CryptoUtil.java - saveAsPEM(..) - 
2014-08-02 23:36:46,157 INFO [main] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-02 23:36:46,157 INFO [main] - OUT -- CertUtil.java - populateCertInfo -
```

Now new tomcat-trust is back in the filesystem. What left is to verify it it exists in the DB and if it is missing, add corresponding entries.

```
2014-08-02 23:36:46,157 INFO [main] - IN -- CertDBAction.java - insertCertificateInDB(certFiletoStore, info) - 
2014-08-02 23:36:46,157 INFO [main] - 

DBParameters ... 
PKID :		null
CN :		L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
serialNo :	42c86b2cf293630fe27bbddc7fd02a39
hostName :	CUCM861
issuerName :	L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
Certificate :	Not Printing huge Certificate String..
IPV4Address :	10.48.46.29
IPV6Address :	
TimeToLive :	NULL
UNIT :		tomcat-trust
TYPE :		trust-certs
ROLE :		null
RoleMoniker :	null
RoleEnum :null
SERVICE :		null
ServiceMoniker :	null
ServiceEnum :0

2014-08-02 23:36:46,157 INFO [main] - DB - Certifciate Store Plugin Handler is :com.cisco.ccm.certmgmt.db.CertDBImpl
2014-08-02 23:36:46,159 DEBUG [main] - Connection Initialized to Publisher. Connection HashCode:23817301  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:46,159 INFO [main] - IN -- CertDBImpl.java - insertCertificate(certInfo, con) - 
2014-08-02 23:36:46,159 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:46,159 DEBUG [main] - Try to get a connection from pool
2014-08-02 23:36:46,159 DEBUG [main] - Getting connection from connection pool entry <database,jdbcurl>
2014-08-02 23:36:46,159 DEBUG [main] - There are currently 2 connection pool entries
2014-08-02 23:36:46,159 DEBUG [main] - Adding connection <com.informix.jdbc.IfxSqliConnect@77eb97> to connection list
2014-08-02 23:36:46,159 DEBUG [main] - Marking connection <com.informix.jdbc.IfxSqliConnect@77eb97> as used
2014-08-02 23:36:46,159 DEBUG [main] - Got connection from pool
2014-08-02 23:36:46,166 INFO [main] - IN -- CertDBImpl.java - populateRoleEnumServiceEnum(certInfo) - 
2014-08-02 23:36:46,166 INFO [main] - UNIT ::: tomcat-trust
2014-08-02 23:36:46,166 INFO [main] - role ::: [ROLE_APPLICATION_SERVER]
2014-08-02 23:36:46,166 INFO [main] - roleEnum ::: [7]
2014-08-02 23:36:46,166 INFO [main] - service ::: null
2014-08-02 23:36:46,166 INFO [main] - serviceEnum ::: 6
2014-08-02 23:36:46,166 INFO [main] - OUT -- CertDBImpl.java - populateRoleEnumServiceEnum - 
2014-08-02 23:36:46,166 INFO [main] - IN -- CertDBUtil.java - getProcessNodeId(con, hostName, ipAddress, fqdn) - 
2014-08-02 23:36:46,166 INFO [main] - getProcessNodeId Query :SELECT PKID,NAME FROM PROCESSNODE WHERE UPPER(NAME)=UPPER("CUCM861") OR UPPER(NAME)=UPPER("10.48.46.29") OR UPPER(NAME)=UPPER("CUCM861")
2014-08-02 23:36:46,166 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:46,172 INFO [main] - ProcessNodeId:13f4b0d9-0bae-429a-a86e-625336a35bb6
2014-08-02 23:36:46,172 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:46,173 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,173 INFO [main] - OUT -- CertDBUtil.java - getProcessNodeId - 
2014-08-02 23:36:46,173 INFO [main] - IN -- CertDBImpl.java - getPkidOfCertificate(hash, serverName, con) - 
2014-08-02 23:36:46,173 DEBUG [main] - GetPKID Query :SELECT A.PKID FROM CERTIFICATE A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND B.HASH = "/hSVsEZT+yZeaxE+K0EM02n1Pgk="
2014-08-02 23:36:46,173 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:46,177 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:46,177 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,177 INFO [main] - OUT -- CertDBImpl.java - getPkidOfCertificate - 
2014-08-02 23:36:46,177 DEBUG [main] - INSERT FLAG :: isCertUpdate=false :: doNothing=false
2014-08-02 23:36:46,177 DEBUG [main] - INSERT/UPDATE Query of CERTIFICATE : null
2014-08-02 23:36:46,177 INFO [main] - IN -- CertDBImpl.java - insertCertSrvCertMap(certInfo, con) - 
2014-08-02 23:36:46,177 INFO [main] - IN -- CertDBImpl.java - checkExistingCertificateServiceMapping(certInfo, serviceEnum, con) - ## CM checks CERTIFICATESERVICECERTIFICATEMAP table if the mapping for our cert exist. 2014-08-02 23:36:46,178 DEBUG [main] - checkExistingTrustCertificateForService Query :SELECT PKID,FKCERTIFICATE, TKCERTIFICATESERVICE FROM CERTIFICATESERVICECERTIFICATEMAP  WHERE FKCERTIFICATE = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND TKCERTIFICATESERVICE= "6"
2014-08-02 23:36:46,178 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:46,184 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:46,184 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,184 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertificateServiceMapping - 
2014-08-02 23:36:46,184 DEBUG [main] - Certificate to be inserted in CERTIFICATESERVICECERTIFICATEMAP table :tomcat-trust ::PKID :533dbbfc-78ce-b46f-7d64-cd2b7c536f6d ::toInsertInCertSrvMap:false ## Since it has not been previousy removed it is there 2014-08-02 23:36:46,185 DEBUG [main] - CertService mapping entry already exists..
2014-08-02 23:36:46,185 INFO [main] - OUT -- CertDBImpl.java - insertCertSrvCertMap - 
2014-08-02 23:36:46,185 INFO [main] - IN -- CertDBImpl.java - insertCertTrustRoleMap(certInfo, log, con) - 
2014-08-02 23:36:46,185 INFO [main] - IN -- CertDBImpl.java - checkExistingCertificateRoleMapping(certInfo, roleEnum, con) - ## the same is being checked for CERTIFICATETRUSTROLEMAP table ... 2014-08-02 23:36:46,185 DEBUG [main] - checkExistingTrustCertificateForRole Query :SELECT PKID,FKCERTIFICATE, TKTRUSTROLE FROM CERTIFICATETRUSTROLEMAP WHERE FKCERTIFICATE = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND TKTRUSTROLE= "7"
2014-08-02 23:36:46,185 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:46,187 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:46,188 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,188 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertificateRoleMapping - 
2014-08-02 23:36:46,188 DEBUG [main] - Certificate to be inserted in CERTIFICATETRUSTROLEMAP table :tomcat-trust ::PKID :533dbbfc-78ce-b46f-7d64-cd2b7c536f6d ::toInsertInCertSrvMap:false ## it exists also here 2014-08-02 23:36:46,188 DEBUG [main] - CertRole mapping entry already exists..
2014-08-02 23:36:46,188 INFO [main] - OUT -- CertDBImpl.java - insertCertTrustRoleMap - 
2014-08-02 23:36:46,188 INFO [main] - IN -- CertDBImpl.java - insertCertProcessNodeMap(certInfo, con) - 
2014-08-02 23:36:46,188 INFO [main] - IN -- CertDBImpl.java - checkExistingCertProcessNodeMapping(certInfo, con) - 
2014-08-02 23:36:46,188 DEBUG [main] - checkExistingCertProcessNodeMapping Query :SELECT PKID,FKCERTIFICATE, FKPROCESSNODE,SERVERNAME FROM CERTIFICATEPROCESSNODEMAP WHERE FKCERTIFICATE="533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND FKPROCESSNODE="13f4b0d9-0bae-429a-a86e-625336a35bb6" AND SERVERNAME="CUCM861"
2014-08-02 23:36:46,188 DEBUG [main] - getConn: usePooling[true]connectToLocalDB[false]_target[0]connectToPubByDefault[true]
2014-08-02 23:36:46,190 DEBUG [main] - Closing the resultset.
2014-08-02 23:36:46,191 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,191 INFO [main] - OUT -- CertDBImpl.java - checkExistingCertProcessNodeMapping - 
2014-08-02 23:36:46,191 DEBUG [main] - CertProcessNode mapping entry already exists..
2014-08-02 23:36:46,191 INFO [main] - OUT -- CertDBImpl.java - insertCertProcessNodeMap - 
2014-08-02 23:36:46,191 DEBUG [main] - Connection committed for insertCertificate.. ## since no entries in DB were missing Insertion finishes. 2014-08-02 23:36:46,191 DEBUG [main] - Insertion of Certificate in DB is Successful.
2014-08-02 23:36:46,191 INFO [main] - OUT -- CertDBImpl.java - insertCertificate - 
2014-08-02 23:36:46,192 DEBUG [main] - Closing the connection. Connection HashCode:23817301  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:46,192 DEBUG [main] - Attempting to close connection
2014-08-02 23:36:46,192 DEBUG [main] - Removing connection <database, jdbcurl> from ConnectionManager list
2014-08-02 23:36:46,192 DEBUG [main] - removeConnectionFromConnectionList()
2014-08-02 23:36:46,192 DEBUG [main] - Removing connection <com.informix.jdbc.IfxSqliConnect@77eb97> from connection list
2014-08-02 23:36:46,192 DEBUG [main] - Connection <com.informix.jdbc.IfxSqliConnect@77eb97> is not closed, adding it back to the pool entry <database,jdbcurl>
2014-08-02 23:36:46,192 INFO [main] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,192 INFO [main] - DB - Generate Certificate operation in DB is successful
2014-08-02 23:36:46,192 INFO [main] - OUT -- CertDBAction.java - insertCertificateInDB - 
2014-08-02 23:36:46,192 INFO [main] - IN -- CryptoUtil.java - isOCSPEnabled(..) - 
2014-08-02 23:36:46,192 INFO [main] - IN -- CryptoUtil.java - getCertMonitorXmlParser(..) - 
2014-08-02 23:36:46,203 INFO [main] - OUT -- CryptoUtil.java - getCertMonitorXmlParser - 
2014-08-02 23:36:46,203 INFO [main] - OUT -- CryptoUtil.java - isOCSPEnabled - false
2014-08-02 23:36:46,203 DEBUG [main] - OCSP is not enabled.
2014-08-02 23:36:46,204 INFO [main] - Successfully imported trusted certificate with Subject DN:L&#61;KRAKOW,ST&#61;MALOPOLSKA,CN&#61;CUCM861,OU&#61;TAC,O&#61;CISCO,C&#61;PL
2014-08-02 23:36:46,204 INFO [main] - OUT -- DefaultCertMgr.java - importTrustCert - Successfully imported trusted certificate with Subject DN:L&#61;KRAKOW,ST&#61;MALOPOLSKA,CN&#61;CUCM861,OU&#61;TAC,O&#61;CISCO,C&#61;PL ## at this moment importing the tomcat-trust ends. CM finishes adding tomcat-trust to the ## trust store and removes CSR file if any. 2014-08-02 23:36:46,204 INFO [main] - result of import operations is ::Import of trust certificate is successful
2014-08-02 23:36:46,204 INFO [main] - OUT -- DefaultCertMgr.java - importCert - 
2014-08-02 23:36:46,204 INFO [main] - OUT -- TomcatCertMgr.java - importCertToTomcatTrustStore - 
2014-08-02 23:36:46,204 INFO [main] - Tomcat Self-signed certificate copied in Tomcat trust-store successfully
2014-08-02 23:36:46,204 INFO [main] - OUT -- TomcatCertMgr.java - copyToTomcatTrustStore - 
2014-08-02 23:36:46,204 DEBUG [main] - GenCert returned
2014-08-02 23:36:46,204 DEBUG [main] - CSR FileName is tomcat-trust.csr
2014-08-02 23:36:46,204 DEBUG [main] - CSR File Deleted: /usr/local/platform/.security/tomcat/keys/tomcat-trust.csr
2014-08-02 23:36:46,204 INFO [main] - Delete CSR File: /usr/local/platform/.security/tomcat/keys/tomcat-trust.csr
2014-08-02 23:36:46,204 DEBUG [main] - Private  Key in DER Form is: tomcat-trust_priv_csr.der
2014-08-02 23:36:46,204 DEBUG [main] - PEM Key in PEM form is:tomcat-trust_priv_csr.pem
2014-08-02 23:36:46,206 INFO [main] - OUT -- DefaultCertMgr.java - regenCert - 
2014-08-02 23:36:46,206 INFO [main] - IN -- CertMgr.java - logResult(result, desc, resultFile) - 
2014-08-02 23:36:46,206 INFO [main] - CertMgmt Operation Result : null
2014-08-02 23:36:46,207 INFO [main] - OUT -- CertMgr.java - logResult - 
2014-08-02 23:36:46,207 INFO [main] - OUT -- CertMgr.java - doOp - 
2014-08-02 23:36:46,207 INFO [main] - OUT -- CertMgr.java - mainIntenal -
```

CM role ends here. Let's take a look at certCN logs on the publisher node. Since it is subscribed to DB change notification it will be notified about the certificate change in CERTIFICATE table.

```
2014-08-02 23:36:45,605 INFO [Thread-5] - IN - process. changeData &colon; 
2014-08-02 23:36:45,607 INFO [Thread-5] - Inside CERTIFICATE - I/U option..
2014-08-02 23:36:45,607 DEBUG [Thread-5] - Updated Data in CERTIFICATE ::<msg><type>DBL</type><table>certificate</table><tableid>41</tableid><action>U</action><time>1407015405</time><old><cdrserver>2</cdrserver><cdrtime>1407012599</cdrtime><pkid>533dbbfc-78ce-b46f-7d64-cd2b7c536f6d</pkid><servername>CUCM861</servername><subjectname>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</subjectname><issuername>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</issuername><serialnumber>6cf5bc855b681f658f9e7506d3ec6ea5</serialnumber><certificate></certificate><ipv4address>10.48.46.29</ipv4address><ipv6address></ipv6address><timetolive>NULL</timetolive><ifx_replcheck>6043073097765093380</ifx_replcheck></old><new><servername>CUCM861</servername><subjectname>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</subjectname><issuername>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</issuername><serialnumber>42c86b2cf293630fe27bbddc7fd02a39</serialnumber><certificate>changed</certificate><ipv4address>10.48.46.29</ipv4address><ipv6address></ipv6address><timetolive>NULL</timetolive></new></msg>
2014-08-02 23:36:45,607 DEBUG [Thread-5] - Certificate PKID : 533dbbfc-78ce-b46f-7d64-cd2b7c536f6d , ipAddress : 10.48.46.29 , OldSerialNo : 6cf5bc855b681f658f9e7506d3ec6ea5 , NewSerialNo : 42c86b2cf293630fe27bbddc7fd02a39
2014-08-02 23:36:45,607 INFO [Thread-5] - OUT - process.
2014-08-02 23:36:45,608 INFO [InsertThread --- 7] - IN -- CertKeystoreHandler.java - run() - 
2014-08-02 23:36:45,609 DEBUG [InsertThread --- 7] - InsertThread --- 7 -- START --

## getting PKID for which the change occurred
2014-08-02 23:36:45,609 DEBUG [InsertThread --- 7] - DB Value UPDATE: 533dbbfc-78ce-b46f-7d64-cd2b7c536f6d
2014-08-02 23:36:45,609 INFO [InsertThread --- 7] - IN -- CertKeystoreHandler.java - updateIntoKeystore() - 
2014-08-02 23:36:45,610 INFO [InsertThread --- 7] - IN -- CertDBImpl.java - getCertificate(certBash64SHA1:null --pkid:533dbbfc-78ce-b46f-7d64-cd2b7c536f6d
2014-08-02 23:36:45,611 DEBUG [InsertThread --- 7] - Connection Initialized to localnode. Connection HashCode:22502526  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,611 DEBUG [InsertThread --- 7] - Select Query to getCertificate :SELECT A.*,B.HASH FROM CERTIFICATE  A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND A.PKID = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d"
2014-08-02 23:36:45,611 DEBUG [InsertThread --- 7] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-02 23:36:45,611 DEBUG [InsertThread --- 7] - Got connection from pool
2014-08-02 23:36:45,681 DEBUG [InsertThread --- 7] - Closing the resultset.
2014-08-02 23:36:45,681 DEBUG [InsertThread --- 7] - Closing the connection. Connection HashCode:22502526  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,681 DEBUG [InsertThread --- 7] - Attempting to close connection
2014-08-02 23:36:45,681 DEBUG [InsertThread --- 7] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-02 23:36:45,681 DEBUG [InsertThread --- 7] - removeConnectionFromConnectionList()
2014-08-02 23:36:45,681 DEBUG [InsertThread --- 7] - Removing connection <com.informix.jdbc.IfxSqliConnect@1ccb1ae> from connection list
2014-08-02 23:36:45,682 DEBUG [InsertThread --- 7] - Connection <com.informix.jdbc.IfxSqliConnect@1ccb1ae> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-02 23:36:45,682 INFO [InsertThread --- 7] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,682 DEBUG [InsertThread --- 7] - Connection released from CertDBImpl.getCertificate method.
2014-08-02 23:36:45,682 INFO [InsertThread --- 7] - OUT -- CertDBImpl.java - getCertificate - 
2014-08-02 23:36:45,682 INFO [InsertThread --- 7] - IN -- CertDBImpl.java - getCertUnitByPkid(pkid) - 
2014-08-02 23:36:45,683 DEBUG [InsertThread --- 7] - Connection Initialized to localnode. Connection HashCode:25877029  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;) ## getting info about changed certificate 2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - Select Query to getCertUnitByPkid :SELECT A.PKID, A.FKCERTIFICATE, A.TKCERTIFICATESERVICE, B.NAME UNIT FROM CERTIFICATESERVICECERTIFICATEMAP A, TYPECERTIFICATESERVICE B WHERE A.FKCERTIFICATE="533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND A.TKCERTIFICATESERVICE = B.ENUM
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - Try to get a connection from pool
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - getting local connection from Pool
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - There are currently 2 connection pool entries
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - Adding connection <com.informix.jdbc.IfxSqliConnect@1ccb1ae> to connection list
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - Marking connection <com.informix.jdbc.IfxSqliConnect@1ccb1ae> as used
2014-08-02 23:36:45,684 DEBUG [InsertThread --- 7] - Got connection from pool
2014-08-02 23:36:45,687 DEBUG [InsertThread --- 7] - Closing the resultset.
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Closing the connection. Connection HashCode:25877029  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Attempting to close connection
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - removeConnectionFromConnectionList()
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Removing connection <com.informix.jdbc.IfxSqliConnect@1ccb1ae> from connection list
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Connection <com.informix.jdbc.IfxSqliConnect@1ccb1ae> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Resultset released from CertDBImpl.getCertUnitByPkid method.
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - OUT -- CertDBImpl.java - getCertUnitByPkid - 
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - UNIT : tomcat
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - CurrentIPAddress : 10.48.46.29
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - RemoteIPAddress : 10.48.46.29
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - OldSerialNo :6cf5bc855b681f658f9e7506d3ec6ea5
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - NewSerialNo :42c86b2cf293630fe27bbddc7fd02a39
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - IN -- CertUtil.java - getListFromComaSeperatedStr(..) - 
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - OUT -- CertUtil.java - getListFromComaSeperatedStr - ## as you know tomcat and tomcat-trust certificates are covered by change notification. ## Since both ones has been properly updated by CM service there is nothing to do for the ## certCN service here. 2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - tomcat --- is included unit for CN
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Change notification not require on same node except tomcat cert.
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - UNIT : tomcat-trust
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - CurrentIPAddress : 10.48.46.29
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - RemoteIPAddress : 10.48.46.29
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - OldSerialNo :6cf5bc855b681f658f9e7506d3ec6ea5
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - NewSerialNo :42c86b2cf293630fe27bbddc7fd02a39
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - IN -- CertUtil.java - getListFromComaSeperatedStr(..) - 
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - OUT -- CertUtil.java - getListFromComaSeperatedStr - 
2014-08-02 23:36:45,688 INFO [InsertThread --- 7] - tomcat-trust --- is included unit for CN
2014-08-02 23:36:45,688 DEBUG [InsertThread --- 7] - Change notification not require on same node except tomcat cert.
2014-08-02 23:36:45,689 INFO [InsertThread --- 7] - tomcat-trust Certificate successfully updated in trust-store by Change Notification..
2014-08-02 23:36:45,689 INFO [InsertThread --- 7] - OUT -- CertKeystoreHandler.java - updateIntoKeystore - 
2014-08-02 23:36:45,689 DEBUG [InsertThread --- 7] - InsertThread --- 7 -- END --
2014-08-02 23:36:45,689 INFO [InsertThread --- 7] - OUT -- CertKeystoreHandler.java - run -
```

So no changes to the certificates has been done by certCN service on the publisher node.

f. Now lets take a look at how it looks like on the subscriber node. New cert has been inserted into DB and replicated to subscriber node. certCN has been notified about the change in the DB. Snipped with the full operation on the sub below (comments in line):

```
## certCN on sub is notified about the change in the DB 2014-08-02 23:36:46,147 INFO [Thread-5] - IN - process. changeData &colon; 
2014-08-02 23:36:46,149 INFO [Thread-5] - Inside CERTIFICATE - I/U option.. ## details about the change are in from DBL (PKID, old serial, new serial, etc.) 2014-08-02 23:36:46,149 DEBUG [Thread-5] - Updated Data in CERTIFICATE ::<msg><type>DBL</type><table>certificate</table><tableid>41</tableid><action>U</action><time>1407015406</time><old><cdrserver>2</cdrserver><cdrtime>1407012599</cdrtime><pkid>533dbbfc-78ce-b46f-7d64-cd2b7c536f6d</pkid><servername>CUCM861</servername><subjectname>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</subjectname><issuername>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</issuername><serialnumber>6cf5bc855b681f658f9e7506d3ec6ea5</serialnumber><certificate></certificate><ipv4address>10.48.46.29</ipv4address><ipv6address></ipv6address><timetolive>NULL</timetolive><ifx_replcheck>6043073097765093380</ifx_replcheck></old><new><pkid>533dbbfc-78ce-b46f-7d64-cd2b7c536f6d</pkid><servername>CUCM861</servername><subjectname>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</subjectname><issuername>L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL</issuername><serialnumber>42c86b2cf293630fe27bbddc7fd02a39</serialnumber><certificate>changed</certificate><ipv4address>10.48.46.29</ipv4address><ipv6address></ipv6address><timetolive>NULL</timetolive></new></msg>
2014-08-02 23:36:46,149 DEBUG [Thread-5] - Certificate PKID : 533dbbfc-78ce-b46f-7d64-cd2b7c536f6d , ipAddress : 10.48.46.29 , OldSerialNo : 6cf5bc855b681f658f9e7506d3ec6ea5 , NewSerialNo : 42c86b2cf293630fe27bbddc7fd02a39
2014-08-02 23:36:46,150 INFO [Thread-5] - OUT - process.
2014-08-02 23:36:46,151 INFO [InsertThread --- 34] - IN -- CertKeystoreHandler.java - run() - 
2014-08-02 23:36:46,152 DEBUG [InsertThread --- 34] - InsertThread --- 34 -- START --
2014-08-02 23:36:46,152 DEBUG [InsertThread --- 34] - DB Value UPDATE: 533dbbfc-78ce-b46f-7d64-cd2b7c536f6d
2014-08-02 23:36:46,152 INFO [InsertThread --- 34] - IN -- CertKeystoreHandler.java - updateIntoKeystore() - 
2014-08-02 23:36:46,153 INFO [InsertThread --- 34] - IN -- CertDBImpl.java - getCertificate(certBash64SHA1:null --pkid:533dbbfc-78ce-b46f-7d64-cd2b7c536f6d
2014-08-02 23:36:46,153 DEBUG [InsertThread --- 34] - Connection Initialized to localnode. Connection HashCode:30330150  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:46,153 DEBUG [InsertThread --- 34] - Select Query to getCertificate :SELECT A.*,B.HASH FROM CERTIFICATE  A, CERTIFICATEHASHMAP B WHERE A.PKID=B.FKCERTIFICATE AND A.PKID = "533dbbfc-78ce-b46f-7d64-cd2b7c536f6d"
2014-08-02 23:36:46,153 DEBUG [InsertThread --- 34] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - Try to get a connection from pool
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - getting local connection from Pool
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - There are currently 2 connection pool entries
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - Checking if connection limit has been reached for database
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - Connecting to subscriber so max number of connections allowed is 100
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - Number of connections in use is 0
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - There are currently 2 connection pool entries
2014-08-02 23:36:46,154 DEBUG [InsertThread --- 34] - Number of available connections in pool: 0
2014-08-02 23:36:46,193 DEBUG [InsertThread --- 34] - Adding connection <com.informix.jdbc.IfxSqliConnect@1feba51> to connection list
2014-08-02 23:36:46,194 DEBUG [InsertThread --- 34] - Marking connection <com.informix.jdbc.IfxSqliConnect@1feba51> as used
2014-08-02 23:36:46,194 DEBUG [InsertThread --- 34] - Got connection from pool
2014-08-02 23:36:46,197 DEBUG [InsertThread --- 34] - Closing the resultset.
2014-08-02 23:36:46,198 DEBUG [InsertThread --- 34] - Closing the connection. Connection HashCode:30330150  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:46,198 DEBUG [InsertThread --- 34] - Attempting to close connection
2014-08-02 23:36:46,198 DEBUG [InsertThread --- 34] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-02 23:36:46,198 DEBUG [InsertThread --- 34] - removeConnectionFromConnectionList()
2014-08-02 23:36:46,198 DEBUG [InsertThread --- 34] - Removing connection <com.informix.jdbc.IfxSqliConnect@1feba51> from connection list
2014-08-02 23:36:46,198 DEBUG [InsertThread --- 34] - Connection <com.informix.jdbc.IfxSqliConnect@1feba51> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-02 23:36:46,198 INFO [InsertThread --- 34] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,198 DEBUG [InsertThread --- 34] - Connection released from CertDBImpl.getCertificate method.
2014-08-02 23:36:46,198 INFO [InsertThread --- 34] - OUT -- CertDBImpl.java - getCertificate - 
2014-08-02 23:36:46,198 INFO [InsertThread --- 34] - IN -- CertDBImpl.java - getCertUnitByPkid(pkid) - 
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - Connection Initialized to localnode. Connection HashCode:8005144  --Details:Connector(NOT CONNECTED: Driver=com.informix.jdbc.IfxDriver;) ## quering DB for the changed certificate and getting details of it 2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - Select Query to getCertUnitByPkid :SELECT A.PKID, A.FKCERTIFICATE, A.TKCERTIFICATESERVICE, B.NAME UNIT FROM CERTIFICATESERVICECERTIFICATEMAP A, TYPECERTIFICATESERVICE B WHERE A.FKCERTIFICATE="533dbbfc-78ce-b46f-7d64-cd2b7c536f6d" AND A.TKCERTIFICATESERVICE = B.ENUM
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - getConn: usePooling[true]connectToLocalDB[true]_target[0]connectToPubByDefault[false]
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - Try to get a connection from pool
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - getting local connection from Pool
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - Getting connection from connection pool entry <database,jdbcurl2>
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - There are currently 2 connection pool entries
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - Adding connection <com.informix.jdbc.IfxSqliConnect@1feba51> to connection list
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - Marking connection <com.informix.jdbc.IfxSqliConnect@1feba51> as used
2014-08-02 23:36:46,199 DEBUG [InsertThread --- 34] - Got connection from pool
2014-08-02 23:36:46,203 DEBUG [InsertThread --- 34] - Closing the resultset.
2014-08-02 23:36:46,204 DEBUG [InsertThread --- 34] - Closing the connection. Connection HashCode:8005144  --Details:Connector(CONNECTED: Driver=com.informix.jdbc.IfxDriver;)
2014-08-02 23:36:46,204 DEBUG [InsertThread --- 34] - Attempting to close connection
2014-08-02 23:36:46,204 DEBUG [InsertThread --- 34] - Removing connection <database, jdbcurl2> from ConnectionManager list
2014-08-02 23:36:46,204 DEBUG [InsertThread --- 34] - removeConnectionFromConnectionList()
2014-08-02 23:36:46,204 DEBUG [InsertThread --- 34] - Removing connection <com.informix.jdbc.IfxSqliConnect@1feba51> from connection list
2014-08-02 23:36:46,204 DEBUG [InsertThread --- 34] - Connection <com.informix.jdbc.IfxSqliConnect@1feba51> is not closed, adding it back to the pool entry <database,jdbcurl2>
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - Connection/Statement/Resultset is closed properly.
2014-08-02 23:36:46,204 DEBUG [InsertThread --- 34] - Resultset released from CertDBImpl.getCertUnitByPkid method.
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - OUT -- CertDBImpl.java - getCertUnitByPkid - 
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - UNIT : tomcat
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - CurrentIPAddress : 10.48.46.30
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - RemoteIPAddress : 10.48.46.29
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - OldSerialNo :6cf5bc855b681f658f9e7506d3ec6ea5
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - NewSerialNo :42c86b2cf293630fe27bbddc7fd02a39
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - IN -- CertUtil.java - getListFromComaSeperatedStr(..) - 
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - OUT -- CertUtil.java - getListFromComaSeperatedStr - 
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - tomcat --- is included unit for CN
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - IN -- CertUtil.java - loadCertFromString(cert) - 
2014-08-02 23:36:46,204 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,209 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,209 INFO [InsertThread --- 34] - OUT -- CertUtil.java - loadCertFromString - 
2014-08-02 23:36:46,209 INFO [InsertThread --- 34] - IN -- CertDBUtil.java - checkDeleteAndImport(unit, dbCert) - 
2014-08-02 23:36:46,209 INFO [InsertThread --- 34] - DB CertInfo.--SN:88769680872451706773275250466208361017--SubjectDN:L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL--GetNotBefore:Sat Aug 02 23:36:44 CEST 2014--GetNotAfter:Thu Aug 01 23:36:43 CEST 2019 ## verifing that you have this certificate in trust store 2014-08-02 23:36:46,209 INFO [InsertThread --- 34] - loading certificate element named [tomcat-trust]
2014-08-02 23:36:46,210 INFO [InsertThread --- 34] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-02 23:36:46,210 INFO [InsertThread --- 34] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-02 23:36:46,212 INFO [InsertThread --- 34] - looking for first [trust-certs] in [product-cpi]
2014-08-02 23:36:46,212 INFO [InsertThread --- 34] - loaded element [tomcat-trust]
2014-08-02 23:36:46,212 INFO [InsertThread --- 34] - determining cert dir for [tomcat-trust]
2014-08-02 23:36:46,212 INFO [InsertThread --- 34] - looking for first [dir] in [tomcat-trust]
2014-08-02 23:36:46,212 INFO [InsertThread --- 34] - getting the value of [dir]
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - value is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - cert dir is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.description] match is false
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.description] match is false
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.pem] match is true
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.der] match is true
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore] match is false ## this is the one you are looking for 2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.der] match is true
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.der] match is true
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description] match is false
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/7e0370f0.0] match is false
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/d0aacffb.0] match is false
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/101f99a6.0] match is false
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem] match is true
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.pem] match is true
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,213 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,214 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - ## certificate file is being deleted from the filesystem 2014-08-02 23:36:46,214 DEBUG [InsertThread --- 34] - SUBJECTDN of DBCert and FileSystemCert compared correctly.. 
2014-08-02 23:36:46,214 DEBUG [InsertThread --- 34] - FILE SYSTEM CERT TO DELETE AND RE-IMPORT.. 
2014-08-02 23:36:46,214 INFO [InsertThread --- 34] - IN -- CertDBUtil.java - deleteTrustCertInFileSystem.. unit : tomcat :: FileName :: /usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
2014-08-02 23:36:46,214 INFO [InsertThread --- 34] - IN -- CertDBUtil.java - populateOpInfo(operation, unit, type, fileLocation, x509Cert, isDBInsert) - 
2014-08-02 23:36:46,214 INFO [InsertThread --- 34] - loading certificate element named [tomcat-trust]
2014-08-02 23:36:46,214 INFO [InsertThread --- 34] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-02 23:36:46,214 INFO [InsertThread --- 34] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - looking for first [trust-certs] in [product-cpi]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - loaded element [tomcat-trust]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - determining key dir for [tomcat-trust]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - looking for first [key-dir] in [tomcat-trust]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - getting the value of [key-dir]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - value is [/usr/local/platform/.security/tomcat/keys]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - key dir is [/usr/local/platform/.security/tomcat/keys]
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - OUT -- CertDBUtil.java - populateOpInfo - 
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - IN -- CertMgr.java - getCertMgrObj(unit) - tomcat-trust ## certCN will call CM api to perform this task. But nothing will land in CM logs. All ## details can be found below 2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - OUT -- CertMgr.java - getCertMgrObj - com.cisco.cpi.certMgmt.manager.TomcatCertMgr@15b0e9f
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - deleteCert(info) - 
decode:     true
op:         delete
unit:       tomcat-trust
keystoreUnit:tomcat-trust
logFile:    /var/log/active/platform/log/cert-mgmt.log
resultFile: /var/log/active/platform/log/certde-info.xml
keyDir:     /usr/local/platform/.security/tomcat/keys
certDir:    /usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
srcCert:    null
type:       trust-certs
rootCACert: null
trustDir:   null
DNAME:      null
description:null
isDBInsert:false

2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - parsed filename: 'CUCM861.pem'
2014-08-02 23:36:46,215 DEBUG [InsertThread --- 34] - filename: 'CUCM861.pem'
2014-08-02 23:36:46,215 DEBUG [InsertThread --- 34] - fileRoot: 'CUCM861'
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - deleteDERandPEM(filenameRoot, parentDir, info) - 
2014-08-02 23:36:46,215 DEBUG [InsertThread --- 34] - ParentDir:/usr/local/platform/.security/tomcat/trust-certsFileName.(DER/PEM):CUCM861
2014-08-02 23:36:46,215 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,224 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,224 INFO [InsertThread --- 34] - No plugins registered for DB Store
2014-08-02 23:36:46,224 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - deleteDERandPEM - 
2014-08-02 23:36:46,224 DEBUG [InsertThread --- 34] - deleteDERandPEM: sCertDir = /usr/local/platform/.security/tomcat/trust-certs --- sAlias = CUCM861 ## cert file deleted. you need to remove it from key store 2014-08-02 23:36:46,225 INFO [InsertThread --- 34] - IN -- TomcatCertMgr.java - removeFromKeyStore(..) - 
2014-08-02 23:36:46,225 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - removeFromKeyStore(keystoreFile, keystorePass, alias) - 
2014-08-02 23:36:46,225 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadKeyStore(keystoreFile, keystorePass) - 
2014-08-02 23:36:46,232 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadKeyStore - 
2014-08-02 23:36:46,238 DEBUG [InsertThread --- 34] - Removing certificate from keystore : CUCM861
2014-08-02 23:36:46,238 DEBUG [InsertThread --- 34] - Size of the keystore after delete is : 2
2014-08-02 23:36:46,238 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - removeFromKeyStore - 
2014-08-02 23:36:46,238 INFO [InsertThread --- 34] - OUT -- TomcatCertMgr.java - removeFromKeyStore - 
2014-08-02 23:36:46,239 INFO [InsertThread --- 34] - trustdir ::/usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,239 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,239 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  python /usr/local/platform/bin/c_rehash.py /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,295 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,295 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:46,295 DEBUG [InsertThread --- 34] - setOwnershipAndPermissions : trust-certs
2014-08-02 23:36:46,296 DEBUG [InsertThread --- 34] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,296 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,296 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,299 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,299 DEBUG [InsertThread --- 34] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,299 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,299 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,302 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,302 DEBUG [InsertThread --- 34] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,302 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,302 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - deleteCert - 
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - OUT -- CertDBUtil.java - deleteTrustCertInFileSystem - ## certificate will be reimported to the filesystem now into /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - IN -- CertDBUtil.java - importTrustCertInFileSystem.. unit : tomcat
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - IN -- CertDBUtil.java - populateOpInfo(operation, unit, type, fileLocation, x509Cert, isDBInsert) - 
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - loading certificate element named [tomcat-trust]
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-02 23:36:46,306 INFO [InsertThread --- 34] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - looking for first [trust-certs] in [product-cpi]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - loaded element [tomcat-trust]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - determining key dir for [tomcat-trust]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - looking for first [key-dir] in [tomcat-trust]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - getting the value of [key-dir]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - value is [/usr/local/platform/.security/tomcat/keys]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - key dir is [/usr/local/platform/.security/tomcat/keys]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - loading certificate element named [tomcat-trust]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-02 23:36:46,308 INFO [InsertThread --- 34] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - looking for first [trust-certs] in [product-cpi]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - loaded element [tomcat-trust]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - determining cert dir for [tomcat-trust]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - looking for first [dir] in [tomcat-trust]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - getting the value of [dir]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - value is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - cert dir is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - OUT -- CertDBUtil.java - populateOpInfo - 
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - IN -- CertMgr.java - getCertMgrObj(unit) - tomcat-trust ## again CM API is called to perform this task 2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - OUT -- CertMgr.java - getCertMgrObj - com.cisco.cpi.certMgmt.manager.TomcatCertMgr@1bbe9f
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - importCert(info) - 
decode:     true
op:         import
unit:       tomcat-trust
keystoreUnit:tomcat-trust
logFile:    /var/log/active/platform/log/cert-mgmt.log
resultFile: /var/log/active/platform/log/certde-info.xml
keyDir:     /usr/local/platform/.security/tomcat/keys
certDir:    /usr/local/platform/.security/tomcat/trust-certs
srcCert:    null
type:       trust-certs
rootCACert: null
trustDir:   null
DNAME:      null
description:null
isDBInsert:false

2014-08-02 23:36:46,310 DEBUG [InsertThread --- 34] - Checking validity of cert
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - Verifying certificate L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-02 23:36:46,310 DEBUG [InsertThread --- 34] - parseCNfromDN( certSubjDN: 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL')
2014-08-02 23:36:46,310 DEBUG [InsertThread --- 34] - Truncating CN 'CUCM861,OU=TAC,O=CISCO,C=PL' -> 'CUCM861'
2014-08-02 23:36:46,310 INFO [InsertThread --- 34] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-02 23:36:46,310 DEBUG [InsertThread --- 34] - Parsed CN 'CUCM861' from DN 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL'
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - trying to load cert from trust store ::/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - cert not available in trust store ::L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - importTrustCert(info, cert) - 
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - saveToTrustStore(info, cert) - 
2014-08-02 23:36:46,311 ERROR [InsertThread --- 34] - trust directory parameter is null
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - saveTrustCert(cert, targetDir, certType) - 
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-02 23:36:46,311 DEBUG [InsertThread --- 34] - parseCNfromDN( certSubjDN: 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL')
2014-08-02 23:36:46,311 DEBUG [InsertThread --- 34] - Truncating CN 'CUCM861,OU=TAC,O=CISCO,C=PL' -> 'CUCM861'
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-02 23:36:46,311 DEBUG [InsertThread --- 34] - Parsed CN 'CUCM861' from DN 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL'
2014-08-02 23:36:46,311 INFO [InsertThread --- 34] - IN -- CertUtil.java - parseCNfromDN(DN, sSearchStr) - 
2014-08-02 23:36:46,312 DEBUG [InsertThread --- 34] - parseCNfromDN( certSubjDN: 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL')
2014-08-02 23:36:46,312 DEBUG [InsertThread --- 34] - Truncating CN 'CUCM861,OU=TAC,O=CISCO,C=PL' -> 'CUCM861'
2014-08-02 23:36:46,312 INFO [InsertThread --- 34] - OUT -- CertUtil.java - parseCNfromDN - 
2014-08-02 23:36:46,312 DEBUG [InsertThread --- 34] - Parsed CN 'CUCM861' from DN 'L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL'
2014-08-02 23:36:46,312 DEBUG [InsertThread --- 34] - target filename for imported cert: 'CUCM861.pem'
2014-08-02 23:36:46,312 DEBUG [InsertThread --- 34] - existing certificate with same filename not found. ## saving cert as PEM and DER formats 2014-08-02 23:36:46,312 DEBUG [InsertThread --- 34] - Saving PEM encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem'
2014-08-02 23:36:46,312 INFO [InsertThread --- 34] - IN -- CryptoUtil.java - saveAsPEM(..) - File : /usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem
2014-08-02 23:36:46,313 INFO [InsertThread --- 34] - OUT -- CryptoUtil.java - saveAsPEM - 
2014-08-02 23:36:46,313 DEBUG [InsertThread --- 34] - Saving DER encoded cert '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.der'
2014-08-02 23:36:46,314 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - saveTrustCert - ## saving new certificate into keystore 2014-08-02 23:36:46,314 INFO [InsertThread --- 34] - IN -- TomcatCertMgr.java - saveToKeyStore(..) - 
2014-08-02 23:36:46,314 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - saveToKeyStore(keystoreFile, keystorePass, x509Certificate, alias) - 
2014-08-02 23:36:46,314 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadKeyStore(keystoreFile, keystorePass) - 
2014-08-02 23:36:46,323 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadKeyStore - 
2014-08-02 23:36:46,323 INFO [InsertThread --- 34] - Size of the keystore before import is : 2
2014-08-02 23:36:46,323 INFO [InsertThread --- 34] - Importing certificate : CUCM861
2014-08-02 23:36:46,330 INFO [InsertThread --- 34] - Size of the keystore after import is : 3
2014-08-02 23:36:46,330 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - saveToKeyStore - 
2014-08-02 23:36:46,330 INFO [InsertThread --- 34] - OUT -- TomcatCertMgr.java - saveToKeyStore - 
2014-08-02 23:36:46,330 DEBUG [InsertThread --- 34] - TrustCert description filename : 'CUCM861.description'
2014-08-02 23:36:46,330 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - createDescriptionFile(name, description) - 
2014-08-02 23:36:46,330 INFO [InsertThread --- 34] - description is :Trust Certificate
2014-08-02 23:36:46,331 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - createDescriptionFile - 
2014-08-02 23:36:46,331 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:46,331 DEBUG [InsertThread --- 34] - setOwnershipAndPermissions : CUCM861.description
2014-08-02 23:36:46,331 DEBUG [InsertThread --- 34] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description'
2014-08-02 23:36:46,331 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,331 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chown certbase /usr/local/platform/.security/tomcat/trust-certs/CUCM861.description
2014-08-02 23:36:46,334 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,334 DEBUG [InsertThread --- 34] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description'
2014-08-02 23:36:46,334 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,334 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chgrp ccmbase /usr/local/platform/.security/tomcat/trust-certs/CUCM861.description
2014-08-02 23:36:46,337 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,337 DEBUG [InsertThread --- 34] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description'
2014-08-02 23:36:46,337 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,337 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chmod 755 /usr/local/platform/.security/tomcat/trust-certs/CUCM861.description
2014-08-02 23:36:46,339 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,339 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:46,339 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - saveToTrustStore - 
2014-08-02 23:36:46,340 INFO [InsertThread --- 34] - trustdir ::/usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,340 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,340 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  python /usr/local/platform/bin/c_rehash.py /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,425 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,425 INFO [InsertThread --- 34] - IN -- DefaultCertMgr.java - setOwnershipAndPermissions(file) - 
2014-08-02 23:36:46,425 DEBUG [InsertThread --- 34] - setOwnershipAndPermissions : trust-certs
2014-08-02 23:36:46,426 DEBUG [InsertThread --- 34] - Changing ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,426 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,426 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chown -R certbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,429 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,429 DEBUG [InsertThread --- 34] - Changing group ownership of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,429 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,430 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chgrp -R ccmbase /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,433 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,433 DEBUG [InsertThread --- 34] - Changing mode of file '/usr/local/platform/.security/tomcat/trust-certs'
2014-08-02 23:36:46,433 INFO [InsertThread --- 34] - IN -- Util.java - sysExec(exe, args) - 
2014-08-02 23:36:46,433 DEBUG [InsertThread --- 34] - Executing command from Util.sysExec :  /bin/chmod -R 755 /usr/local/platform/.security/tomcat/trust-certs
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- Util.java - sysExec - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - setOwnershipAndPermissions - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - No plugins registered for DB Store
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - IN -- CryptoUtil.java - isOCSPEnabled(..) - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - IN -- CryptoUtil.java - getCertMonitorXmlParser(..) - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- CryptoUtil.java - getCertMonitorXmlParser - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- CryptoUtil.java - isOCSPEnabled - false
2014-08-02 23:36:46,437 DEBUG [InsertThread --- 34] - OCSP is not enabled.
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - Successfully imported trusted certificate with Subject DN:L&#61;KRAKOW,ST&#61;MALOPOLSKA,CN&#61;CUCM861,OU&#61;TAC,O&#61;CISCO,C&#61;PL
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - importTrustCert - Successfully imported trusted certificate with Subject DN:L&#61;KRAKOW,ST&#61;MALOPOLSKA,CN&#61;CUCM861,OU&#61;TAC,O&#61;CISCO,C&#61;PL ## import ends with success, some additional checks are performed below 2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - result of import operations is ::Import of trust certificate is successful
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- DefaultCertMgr.java - importCert - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- CertDBUtil.java - importTrustCertInFileSystem - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OUT -- CertDBUtil.java - checkDeleteAndImport - 
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - UNIT : tomcat-trust
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - CurrentIPAddress : 10.48.46.30
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - RemoteIPAddress : 10.48.46.29
2014-08-02 23:36:46,437 INFO [InsertThread --- 34] - OldSerialNo :6cf5bc855b681f658f9e7506d3ec6ea5
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - NewSerialNo :42c86b2cf293630fe27bbddc7fd02a39
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - IN -- CertUtil.java - getListFromComaSeperatedStr(..) - 
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - OUT -- CertUtil.java - getListFromComaSeperatedStr - 
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - tomcat-trust --- is included unit for CN
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - IN -- CertUtil.java - loadCertFromString(cert) - 
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - OUT -- CertUtil.java - loadCertFromString - 
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - IN -- CertDBUtil.java - checkDeleteAndImport(unit, dbCert) - 
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - DB CertInfo.--SN:88769680872451706773275250466208361017--SubjectDN:L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL--GetNotBefore:Sat Aug 02 23:36:44 CEST 2014--GetNotAfter:Thu Aug 01 23:36:43 CEST 2019
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - loading certificate element named [tomcat-trust]
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - determining certificates in group [product-cpi] with type [trust-certs]
2014-08-02 23:36:46,438 INFO [InsertThread --- 34] - loading the config file [/usr/local/platform/conf/cert-conf.xml]
2014-08-02 23:36:46,441 INFO [InsertThread --- 34] - looking for first [trust-certs] in [product-cpi]
2014-08-02 23:36:46,441 INFO [InsertThread --- 34] - loaded element [tomcat-trust]
2014-08-02 23:36:46,441 INFO [InsertThread --- 34] - determining cert dir for [tomcat-trust]
2014-08-02 23:36:46,441 INFO [InsertThread --- 34] - looking for first [dir] in [tomcat-trust]
2014-08-02 23:36:46,441 INFO [InsertThread --- 34] - getting the value of [dir]
2014-08-02 23:36:46,441 INFO [InsertThread --- 34] - value is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-02 23:36:46,441 INFO [InsertThread --- 34] - cert dir is [/usr/local/platform/.security/tomcat/trust-certs]
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.description] match is false
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.description] match is false
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.pem] match is true
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/VeriSign_Class_3_Secure_Server_CA_-_G3.der] match is true
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore] match is false
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.der] match is true
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.der] match is true
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.description] match is false
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/7e0370f0.0] match is false
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/d0aacffb.0] match is false
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/101f99a6.0] match is false
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861.pem] match is true
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - [/usr/local/platform/.security/tomcat/trust-certs/CUCM861s.pem] match is true
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,442 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,443 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,443 DEBUG [InsertThread --- 34] - SUBJECTDN of DBCert and FileSystemCert compared correctly.. 
2014-08-02 23:36:46,443 DEBUG [InsertThread --- 34] - Certificate already exists in FileSystem..
2014-08-02 23:36:46,443 INFO [InsertThread --- 34] - IN -- RSACryptoEngine.java - loadCertificate(..) - 
2014-08-02 23:36:46,443 INFO [InsertThread --- 34] - OUT -- RSACryptoEngine.java - loadCertificate - 
2014-08-02 23:36:46,443 INFO [InsertThread --- 34] - OUT -- CertDBUtil.java - checkDeleteAndImport - 
2014-08-02 23:36:46,443 INFO [InsertThread --- 34] - tomcat-trust Certificate successfully updated in trust-store by Change Notification..
2014-08-02 23:36:46,443 INFO [InsertThread --- 34] - OUT -- CertKeystoreHandler.java - updateIntoKeystore - 
2014-08-02 23:36:46,443 DEBUG [InsertThread --- 34] - InsertThread --- 34 -- END --
2014-08-02 23:36:46,443 INFO [InsertThread --- 34] - OUT -- CertKeystoreHandler.java - run -
```

You can reconfirm above on the filesystem of the subscriber. tomcat-trust for pub has been updated under trust-certs (check modification date).

```
[root@CUCM861s tomcat]# pwd /usr/local/platform/.security/tomcat [root@CUCM861s tomcat]# ls -la certs
total 48
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 22:51 .
drwxr-xr-x 5 root     root    4096 Apr  4 14:33 ..
-rwxr-xr-x 1 certbase ccmbase  941 Aug  2 22:51 tomcat.der
-rwxr-xr-x 1 certbase ccmbase   64 Aug  2 22:51 tomcat.description
-rwxr-xr-x 1 certbase ccmbase 2598 Aug  2 22:51 tomcat.keystore
-rwxr-xr-x 1 certbase ccmbase 1330 Aug  2 22:51 tomcat.pem
[root@CUCM861s tomcat]# ls -la trust-certs
total 108
drwxr-xr-x 2 certbase ccmbase 4096 Aug  2 23:36 .
drwxr-xr-x 5 root     root    4096 Apr  4 14:33 ..
lrwxrwxrwx 1 certbase ccmbase   11 Aug  2 23:36 101f99a6.0 -> CUCM861.pem lrwxrwxrwx 1 certbase ccmbase   42 Aug  2 23:36 7e0370f0.0 -> VeriSign_Class_3_Secure_Server_CA_-_G3.pem
-rwxr-xr-x 1 certbase ccmbase  939 Aug  2 23:36 CUCM861.der -rwxr-xr-x 1 certbase ccmbase   44 Aug  2 23:36 CUCM861.description
-rwxr-xr-x 1 certbase ccmbase 1326 Aug  2 23:36 CUCM861.pem -rwxr-xr-x 1 certbase ccmbase  941 Aug  2 22:51 CUCM861s.der
-rwxr-xr-x 1 certbase ccmbase   44 Aug  2 22:51 CUCM861s.description
-rwxr-xr-x 1 certbase ccmbase 1330 Aug  2 22:51 CUCM861s.pem
lrwxrwxrwx 1 certbase ccmbase   12 Aug  2 23:36 d0aacffb.0 -> CUCM861s.pem
-rwxr-xr-x 1 certbase ccmbase 3907 Aug  2 23:36 tomcat-trust.keystore
-rwxr-xr-x 1 certbase ccmbase 1520 Apr  4 14:33 VeriSign_Class_3_Secure_Server_CA_-_G3.der
-rwxr-xr-x 1 certbase ccmbase   44 Apr  4 14:33 VeriSign_Class_3_Secure_Server_CA_-_G3.description
-rwxr-xr-x 1 certbase ccmbase 2114 Apr  4 14:33 VeriSign_Class_3_Secure_Server_CA_-_G3.pem
[root@CUCM861s tomcat]# md5sum trust-certs/CUCM861.der a0dd8031bcd3c269844df8a3fafd476c trust-certs/CUCM861.der
```

Finally you can verify pub's tomcat-trust certificate under GUI. GUI will show us the certificate that are read from filesystem, not database.

That ends the process of regenerate tomcat certificate on publisher node and propagate this change across the cluster.

## 5. Troubleshoot

### 5.A. Known Caveats - categorization

Below you can find a list of common defects that are related to certificates and CM.

A. Related to incorrect propagation of a change in certificates: CSCul78787 - Can't delete Trust Certs from CM 9.1 even after stopping CertCN service CSCto86463 - Deleted certificates reappear, unable to remove certificates from CUCM CSCth79451 - Certificate DB entries should be updated while changing hostname/IP

CSCup28852 - phone reset every 7min due to cert update when using multi-server cert

B. Found during DRS operations: CSCtn50405 - CUCM DRF Backup does not backup certificates CSCtt95983 - CAPF certificate not backup'd/restored with DRF CSCup71297 - Incorrect certificate update after DRS restore

C. Miscellaneous and doc: CSCup54818 - [DOC] certs signed by CA (key size >=4096) not supported in mixed mode CSCud49047 - RTMT Option To Download Certificate Change Notification Service Logs CSCup88555 - Need to validate serial number length while uploading new cert

### 5.B. Tips and tricks

a. There is one table in the database that matches enums to the corresponding type of the certificate. You can see these enums quite often in the certfiicate related DB queries (CM/certCN logs, table CERTIFICATESERVICECERTIFICATEMAP). To get that mapping you need to take a look at TYPECERTIFICATESERVICE

```
admin:run sql select * from TYPECERTIFICATESERVICE
enum name                moniker                                 usestruststore
==== =================== ======================================= ==============
1    Phone-trust         CERTIFICATE_SERVICE_PHONE_TRUST         t
2    Phone-VPN-trust     CERTIFICATE_SERVICE_PHONE_VPN_TRUST     t
3    CallManager         CERTIFICATE_SERVICE_CALLMANAGER         f
4    CallManager-trust   CERTIFICATE_SERVICE_CALLMANAGER_TRUST   t
5    tomcat              CERTIFICATE_SERVICE_TOMCAT              f
6    tomcat-trust        CERTIFICATE_SERVICE_TOMCAT_TRUST        t
7    ipsec               CERTIFICATE_SERVICE_IPSEC               f
8    ipsec-trust         CERTIFICATE_SERVICE_IPSEC_TRUST         t
9    CAPF                CERTIFICATE_SERVICE_CAPF                f
10   CAPF-trust          CERTIFICATE_SERVICE_CAPF_TRUST          t
11   TVS                 CERTIFICATE_SERVICE_TVS                 f
12   TVS-trust           CERTIFICATE_SERVICE_TVS_TRUST           t
13   directory-trust     CERTIFICATE_SERVICE_DIRECTORY_TRUST     t
14   Phone-SAST-trust    CERTIFICATE_SERVICE_PHONE_SAST_TRUST    t
15   Phone-CTL-trust     CERTIFICATE_SERVICE_PHONE_CTL_TRUST     t
16   userlicensing-trust CERTIFICATE_SERVICE_USERLICENSING_TRUST t
```

b. Let's consider that you need to query DB and list all certificates. The query must return pkid and serial number of certificate, IP and the node name, type of the certificate and its subject name. Please check the one below:

run sql select CERTIFICATE.pkid, CERTIFICATE.serialnumber, CERTIFICATEPROCESSNODEMAP.ipv4address, CERTIFICATEPROCESSNODEMAP.servername, TYPECERTIFICATESERVICE.name, subjectname from CERTIFICATEPROCESSNODEMAP inner join CERTIFICATE ON CERTIFICATEPROCESSNODEMAP.fkcertificate=CERTIFICATE.pkid inner join CERTIFICATESERVICECERTIFICATEMAP ON CERTIFICATESERVICECERTIFICATEMAP.fkcertificate=CERTIFICATE.pkid JOIN TYPECERTIFICATESERVICE ON TYPECERTIFICATESERVICE.enum=CERTIFICATESERVICECERTIFICATEMAP.tkcertificateservice order by CERTIFICATEPROCESSNODEMAP.servername

The sample result you can find in below snippet.

```
admin:run sql select CERTIFICATE.pkid, CERTIFICATE.serialnumber, CERTIFICATEPROCESSNODEMAP.ipv4address, CERTIFICATEPROCESSNODEMAP.servername, TYPECERTIFICATESERVICE.name, subjectname from CERTIFICATEPROCESSNODEMAP inner join CERTIFICATE ON CERTIFICATEPROCESSNODEMAP.fkcertificate=CERTIFICATE.pkid inner join CERTIFICATESERVICECERTIFICATEMAP ON CERTIFICATESERVICECERTIFICATEMAP.fkcertificate=CERTIFICATE.pkid JOIN TYPECERTIFICATESERVICE ON TYPECERTIFICATESERVICE.enum=CERTIFICATESERVICECERTIFICATEMAP.tkcertificateservice order by CERTIFICATEPROCESSNODEMAP.servername
pkid                                 serialnumber                     ipv4address servername name              subjectname                                                                         
==================================== ================================ =========== ========== ================= ===================================================================================================================================================================================================
e380b725-19b1-e3ec-71bf-1bb106d3d454 6a6967b3000000000003             10.48.46.29 CUCM861    CAPF-trust        CN=Cisco Manufacturing CA,O=Cisco Systems                                           
cc7b18b3-3a50-3dcb-578a-1ca50e076198 17226b84000000000012             10.48.46.29 CUCM861    CallManager-trust CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL,2.5.4.5=#134034346262356539376665336362306239323739666339333332636639373830303863623132316337356532316231623263663234616537656237363963323935
664b66c9-485c-aedf-9848-ed34616b8fe7 1461af2a00000000000a             10.48.46.29 CUCM861    CallManager-trust CN=TVGRTHC501,1.2.840.113549.1.9.2=#130a54564752544843353031,1.2.840.113549.1.9.8=#130d31302e3130362e36352e323130,2.5.4.5=#130b46474c3137343732353241
cc7b18b3-3a50-3dcb-578a-1ca50e076198 17226b84000000000012             10.48.46.29 CUCM861    Phone-SAST-trust  CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL,2.5.4.5=#134034346262356539376665336362306239323739666339333332636639373830303863623132316337356532316231623263663234616537656237363963323935
0c879119-476e-c608-049c-03710c47cdd2 5a82be1ec30346af4c295fb8fc41a7f7 10.48.46.29 CUCM861    CallManager-trust CN=ciscolab-AD-CA,DC=cisco,DC=lab                                                   
a2735f97-cbc0-81f6-dadf-c145b657b22e 59dacc01be1dbe84541bc8193a09267e 10.48.46.29 CUCM861    CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-91e6eb10,OU=TAC,O=CISCO,C=PL                         
311830a0-8b8d-2216-7037-f60940976dcd 353fb24bd70f14a346c1f3a9ac725675 10.48.46.29 CUCM861    CallManager-trust CN=CAP-RTP-002,O=Cisco Systems                                                      
a2735f97-cbc0-81f6-dadf-c145b657b22e 59dacc01be1dbe84541bc8193a09267e 10.48.46.29 CUCM861    CAPF              L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-91e6eb10,OU=TAC,O=CISCO,C=PL                         
3fb48b23-84e7-cecf-dd24-e38cbd32c20f 6249ccbedf4df00155ddcd482dac43e6 10.48.46.29 CUCM861    Phone-SAST-trust  L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
a2735f97-cbc0-81f6-dadf-c145b657b22e 59dacc01be1dbe84541bc8193a09267e 10.48.46.29 CUCM861    CAPF-trust        L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-91e6eb10,OU=TAC,O=CISCO,C=PL                         
311830a0-8b8d-2216-7037-f60940976dcd 353fb24bd70f14a346c1f3a9ac725675 10.48.46.29 CUCM861    CAPF-trust        CN=CAP-RTP-002,O=Cisco Systems                                                      
07849796-ff87-eee3-ef89-61f368b3e34a 7f325a657ab1316fbd8334b565e55033 10.48.46.29 CUCM861    TVS               L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
9cbcb782-c37d-6f63-7608-2f51a683ceb6 609bf431ad462fe12b4c571866458dee 10.48.46.29 CUCM861    ipsec             L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
33a86281-4f7e-2833-0c4e-12a9259b5fea 484c2e9b1996a63e45e57dc067d68ec2 10.48.46.29 CUCM861    Phone-SAST-trust  L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL                        
9cbcb782-c37d-6f63-7608-2f51a683ceb6 609bf431ad462fe12b4c571866458dee 10.48.46.29 CUCM861    ipsec-trust       L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
b98fc2a9-ffc1-31b2-f793-701a4b4b59c4 6cdbac937a099bf9eaf8324de5440ff4 10.48.46.29 CUCM861    CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-0087c0a5,OU=TAC,O=CISCO,C=PL                         
533dbbfc-78ce-b46f-7d64-cd2b7c536f6d 42c86b2cf293630fe27bbddc7fd02a39 10.48.46.29 CUCM861    tomcat            L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
a6b18f66-bf72-261d-8ecd-bfcea02add4e 68052e2e9cd6c979079e6449ff873031 10.48.46.29 CUCM861    tomcat            L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
533dbbfc-78ce-b46f-7d64-cd2b7c536f6d 42c86b2cf293630fe27bbddc7fd02a39 10.48.46.29 CUCM861    tomcat-trust      L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
6fe4bd7d-76fe-1d19-4e5e-9cfa4f073487 692c45e5f81da30a779e73907e17ef7f 10.48.46.29 CUCM861    CAPF-trust        L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-8480bdc7,OU=TAC,O=CISCO,C=PL                         
839d761f-f8e8-695b-bf1d-d08ce93b621e 6ecc7aa5a7032009b8cebcf4e952d491 10.48.46.29 CUCM861    tomcat-trust      CN=VeriSign Class 3 Secure Server CA - G3,OU=Terms of use at https://www.verisign.com/rpa (c)10,OU=VeriSign Trust Network,O=VeriSign\, Inc.,C=US
a6b18f66-bf72-261d-8ecd-bfcea02add4e 68052e2e9cd6c979079e6449ff873031 10.48.46.29 CUCM861    tomcat-trust      L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
3c241de1-2eec-e63a-667c-c07147e298d5 5ff87b282b54dc8d42a315b568c9adff 10.48.46.29 CUCM861    CallManager-trust CN=Cisco Root CA 2048,O=Cisco Systems                                               
6fe4bd7d-76fe-1d19-4e5e-9cfa4f073487 692c45e5f81da30a779e73907e17ef7f 10.48.46.29 CUCM861    CAPF              L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-8480bdc7,OU=TAC,O=CISCO,C=PL                         
3c241de1-2eec-e63a-667c-c07147e298d5 5ff87b282b54dc8d42a315b568c9adff 10.48.46.29 CUCM861    CAPF-trust        CN=Cisco Root CA 2048,O=Cisco Systems                                               
6fe4bd7d-76fe-1d19-4e5e-9cfa4f073487 692c45e5f81da30a779e73907e17ef7f 10.48.46.29 CUCM861    CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-8480bdc7,OU=TAC,O=CISCO,C=PL                         
5a4e9685-e9c4-dc52-586d-a36c927208b5 7612f960153d6f9f4e42202032b72356 10.48.46.29 CUCM861    CallManager-trust CN=CAP-RTP-001,O=Cisco Systems                                                      
3cf492fa-e88e-e751-040e-c31827870353 4a5d72eb7de2768c9d70260c8e3b4096 10.48.46.29 CUCM861    CallManager       L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
5a4e9685-e9c4-dc52-586d-a36c927208b5 7612f960153d6f9f4e42202032b72356 10.48.46.29 CUCM861    CAPF-trust        CN=CAP-RTP-001,O=Cisco Systems                                                      
3cf492fa-e88e-e751-040e-c31827870353 4a5d72eb7de2768c9d70260c8e3b4096 10.48.46.29 CUCM861    Phone-SAST-trust  L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
e380b725-19b1-e3ec-71bf-1bb106d3d454 6a6967b3000000000003             10.48.46.29 CUCM861    CallManager-trust CN=Cisco Manufacturing CA,O=Cisco Systems                                           
3cf492fa-e88e-e751-040e-c31827870353 4a5d72eb7de2768c9d70260c8e3b4096 10.48.46.29 CUCM861    CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
cc7b18b3-3a50-3dcb-578a-1ca50e076198 17226b84000000000012             10.48.46.29 CUCM861    CallManager       CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL,2.5.4.5=#134034346262356539376665336362306239323739666339333332636639373830303863623132316337356532316231623263663234616537656237363963323935
cc7b18b3-3a50-3dcb-578a-1ca50e076198 17226b84000000000012             10.48.46.30 CUCM861s   CallManager-trust CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL,2.5.4.5=#134034346262356539376665336362306239323739666339333332636639373830303863623132316337356532316231623263663234616537656237363963323935
cc7b18b3-3a50-3dcb-578a-1ca50e076198 17226b84000000000012             10.48.46.30 CUCM861s   Phone-SAST-trust  CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL,2.5.4.5=#134034346262356539376665336362306239323739666339333332636639373830303863623132316337356532316231623263663234616537656237363963323935
a2735f97-cbc0-81f6-dadf-c145b657b22e 59dacc01be1dbe84541bc8193a09267e 10.48.46.30 CUCM861s   CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-91e6eb10,OU=TAC,O=CISCO,C=PL                         
a2735f97-cbc0-81f6-dadf-c145b657b22e 59dacc01be1dbe84541bc8193a09267e 10.48.46.30 CUCM861s   CAPF              L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-91e6eb10,OU=TAC,O=CISCO,C=PL                         
a2735f97-cbc0-81f6-dadf-c145b657b22e 59dacc01be1dbe84541bc8193a09267e 10.48.46.30 CUCM861s   CAPF-trust        L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-91e6eb10,OU=TAC,O=CISCO,C=PL                         
9cbcb782-c37d-6f63-7608-2f51a683ceb6 609bf431ad462fe12b4c571866458dee 10.48.46.30 CUCM861s   ipsec             L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
9cbcb782-c37d-6f63-7608-2f51a683ceb6 609bf431ad462fe12b4c571866458dee 10.48.46.30 CUCM861s   ipsec-trust       L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
533dbbfc-78ce-b46f-7d64-cd2b7c536f6d 42c86b2cf293630fe27bbddc7fd02a39 10.48.46.30 CUCM861s   tomcat            L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
533dbbfc-78ce-b46f-7d64-cd2b7c536f6d 42c86b2cf293630fe27bbddc7fd02a39 10.48.46.30 CUCM861s   tomcat-trust      L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
839d761f-f8e8-695b-bf1d-d08ce93b621e 6ecc7aa5a7032009b8cebcf4e952d491 10.48.46.30 CUCM861s   tomcat-trust      CN=VeriSign Class 3 Secure Server CA - G3,OU=Terms of use at https://www.verisign.com/rpa (c)10,OU=VeriSign Trust Network,O=VeriSign\, Inc.,C=US
3c241de1-2eec-e63a-667c-c07147e298d5 5ff87b282b54dc8d42a315b568c9adff 10.48.46.30 CUCM861s   CallManager-trust CN=Cisco Root CA 2048,O=Cisco Systems                                               
3c241de1-2eec-e63a-667c-c07147e298d5 5ff87b282b54dc8d42a315b568c9adff 10.48.46.30 CUCM861s   CAPF-trust        CN=Cisco Root CA 2048,O=Cisco Systems                                               
5a4e9685-e9c4-dc52-586d-a36c927208b5 7612f960153d6f9f4e42202032b72356 10.48.46.30 CUCM861s   CallManager-trust CN=CAP-RTP-001,O=Cisco Systems                                                      
5a4e9685-e9c4-dc52-586d-a36c927208b5 7612f960153d6f9f4e42202032b72356 10.48.46.30 CUCM861s   CAPF-trust        CN=CAP-RTP-001,O=Cisco Systems                                                      
e380b725-19b1-e3ec-71bf-1bb106d3d454 6a6967b3000000000003             10.48.46.30 CUCM861s   CallManager-trust CN=Cisco Manufacturing CA,O=Cisco Systems                                           
cc7b18b3-3a50-3dcb-578a-1ca50e076198 17226b84000000000012             10.48.46.30 CUCM861s   CallManager       CN=CUCM861,OU=TAC,O=CISCO,L=KRAKOW,ST=MALOPOLSKA,C=PL,2.5.4.5=#134034346262356539376665336362306239323739666339333332636639373830303863623132316337356532316231623263663234616537656237363963323935
3cf492fa-e88e-e751-040e-c31827870353 4a5d72eb7de2768c9d70260c8e3b4096 10.48.46.30 CUCM861s   Phone-SAST-trust  L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
664b66c9-485c-aedf-9848-ed34616b8fe7 1461af2a00000000000a             10.48.46.30 CUCM861s   CallManager-trust CN=TVGRTHC501,1.2.840.113549.1.9.2=#130a54564752544843353031,1.2.840.113549.1.9.8=#130d31302e3130362e36352e323130,2.5.4.5=#130b46474c3137343732353241
6fe4bd7d-76fe-1d19-4e5e-9cfa4f073487 692c45e5f81da30a779e73907e17ef7f 10.48.46.30 CUCM861s   CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-8480bdc7,OU=TAC,O=CISCO,C=PL                         
3cf492fa-e88e-e751-040e-c31827870353 4a5d72eb7de2768c9d70260c8e3b4096 10.48.46.30 CUCM861s   CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
6fe4bd7d-76fe-1d19-4e5e-9cfa4f073487 692c45e5f81da30a779e73907e17ef7f 10.48.46.30 CUCM861s   CAPF              L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-8480bdc7,OU=TAC,O=CISCO,C=PL                         
3cf492fa-e88e-e751-040e-c31827870353 4a5d72eb7de2768c9d70260c8e3b4096 10.48.46.30 CUCM861s   CallManager       L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
6fe4bd7d-76fe-1d19-4e5e-9cfa4f073487 692c45e5f81da30a779e73907e17ef7f 10.48.46.30 CUCM861s   CAPF-trust        L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-8480bdc7,OU=TAC,O=CISCO,C=PL                         
648651b6-f175-8307-7d19-810061b27eed 7da8a70fe1b3a9bebe2f85000498d935 10.48.46.30 CUCM861s   ipsec             L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
0c27516c-bb4e-dc88-0bb9-f672394b265f 5de78d9912f1d88be14b2472c6eb1865 10.48.46.30 CUCM861s   TVS               L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
b98fc2a9-ffc1-31b2-f793-701a4b4b59c4 6cdbac937a099bf9eaf8324de5440ff4 10.48.46.30 CUCM861s   CallManager-trust L=KRAKOW,ST=MALOPOLSKA,CN=CAPF-0087c0a5,OU=TAC,O=CISCO,C=PL                         
a6b18f66-bf72-261d-8ecd-bfcea02add4e 68052e2e9cd6c979079e6449ff873031 10.48.46.30 CUCM861s   tomcat-trust      L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
a6b18f66-bf72-261d-8ecd-bfcea02add4e 68052e2e9cd6c979079e6449ff873031 10.48.46.30 CUCM861s   tomcat            L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861s,OU=TAC,O=CISCO,C=PL                              
33a86281-4f7e-2833-0c4e-12a9259b5fea 484c2e9b1996a63e45e57dc067d68ec2 10.48.46.30 CUCM861s   Phone-SAST-trust  L=Krakow,ST=Malopolska,CN=CUCM9X,OU=TAC,O=Cisco Systems,C=PL                        
311830a0-8b8d-2216-7037-f60940976dcd 353fb24bd70f14a346c1f3a9ac725675 10.48.46.30 CUCM861s   CAPF-trust        CN=CAP-RTP-002,O=Cisco Systems                                                      
3fb48b23-84e7-cecf-dd24-e38cbd32c20f 6249ccbedf4df00155ddcd482dac43e6 10.48.46.30 CUCM861s   Phone-SAST-trust  L=KRAKOW,ST=MALOPOLSKA,CN=CUCM861,OU=TAC,O=CISCO,C=PL                               
311830a0-8b8d-2216-7037-f60940976dcd 353fb24bd70f14a346c1f3a9ac725675 10.48.46.30 CUCM861s   CallManager-trust CN=CAP-RTP-002,O=Cisco Systems                                                      
0c879119-476e-c608-049c-03710c47cdd2 5a82be1ec30346af4c295fb8fc41a7f7 10.48.46.30 CUCM861s   CallManager-trust CN=ciscolab-AD-CA,DC=cisco,DC=lab                                                   
e380b725-19b1-e3ec-71bf-1bb106d3d454 6a6967b3000000000003             10.48.46.30 CUCM861s   CAPF-trust        CN=Cisco Manufacturing CA,O=Cisco Systems
```

Above can be very useful when troubleshoot issues with syncing certificate between DB and the filesystem.

c. To check certificate expiration date you can use OpenSSL command (requires root):

Example output:

```
[root@CUCM861 certs]# openssl x509 -noout -dates -in tomcat.pem notBefore=Aug  2 21:36:44 2014 GMT
notAfter=Aug  1 21:36:43 2019 GMT
[root@CUCM861 certs]#
```

d. To check the same as above but for the certificate that resides in the database you need to know serial number or PKID of the certificate you want to verify. Task requires to run two bash commands (you need to do "su - informix" prior this) .

echo "unload to 'cert_dumped_to_file' delimiter " " select certificate from certificate where serialnumber = '6a6967b3000000000003'"|dbaccess -e ccm9_1_2_10000_28

Above will create a file cert_dumped_to_file where SQL command output will be stored. Important thing is to use correct name of the database. You can find it in dbaccess tool (while selecting DB connection).

The second command is used to display date:

sed 's/\\//g' cert_dumped_to_file | openssl x509 -noout -dates

Example output:

```
[root@CUCM861 certs]# su - informix
-bash-3.2$ echo "unload to 'cert_dumped_to_file' delimiter " " select certificate from certificate where serialnumber = '6a6967b3000000000003'"|dbaccess -e ccm9_1_2_10000_28 Database selected.

unload to 'cert_dumped_to_file' delimiter   select certificate from certificate where serialnumber = '6a6967b3000000000003'

1 row(s) unloaded.

Database closed.

-bash-3.2$ sed 's/\\//g' cert_dumped_to_file | openssl x509 -noout -dates notBefore=Jun 10 22:16:01 2005 GMT
notAfter=May 14 20:25:42 2029 GMT
```

### 5.C. CCM Service Certificate verification

CallManager as a service has to verify client certificate for the successuful TLS/SSL handshake with the phone or gateway.

The errors can be found in SDL/SDI traces together with error code which refers to OpenSSL library:

00370874.000 |09:50:27.713 |AppInfo |SdlSSLTCPListener::verify_cb pre-verified=0,cert verification errno= 20 ,depth=0 00370875.000 |09:50:27.713 |AppInfo |HandleSSLError - Certificate verification failed:(Verification error: 20 )- unable to get local issuer certificate for 192.168.255.95:52089

List of OpenSSL error codes:

https://www.openssl.org/docs/apps/verify.html#DIAGNOSTICS

When you generate CA signed certificates ensure that they are generated with correct Key Usage as requested in CSR, otherwise they might be not verified properly:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cucos/8_6_1/cucos/osg_861_cm/iptpch6.html#wp1055278

CUCM utilizes openSSL library for the certificate operations so you can manually verify the certificate under root. The example for Tomcat certificate signed by external CA is presented below:

```
[root@cucmpub trust-certs]# ls -l e87b20d3.0 lrwxrwxrwx 1 certbase ccmbase 31 Jul 8 00:01 e87b20d3.0 -> molszowy-WIN-V8HGEMMBHOU-CA.pem [root@cucmpub trust-certs]# cd /usr/local/platform/.security/tomcat/certs [root@cucmpub certs]# openssl verify -CApath /usr/local/platform/.security/tomcat/trust-certs tomcat.pem tomcat.pem: OK
```

### 5.D. Tomcat trust-store and keystore verification

Tomcat can use two different implementations of SSL:

- the JSSE implementation provided as part of the Java runtime (since 1.4)

- the APR implementation, which uses the OpenSSL engine by default.

Which SSL-implementation is used by Tomcat can be checked in server.xml (located in /usr/local/thirdparty/jakarta-tomcat/conf ) configuration file under HTTPS-connector configuration - keystores are used by JSSE implementation, certificates in pem/der-form are used by APR implementation :

<Connector SSLEnabled="true" URIEncoding="UTF-8" acceptCount="100" ciphers="TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA,TLS_DHE_DSS_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_DHE_RSA_WITH_AES_128_CBC_SHA,SSL_RSA_WITH_3DES_EDE_CBC_SHA,SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA" clientAuth="false" disableUploadTimeout="true" enableLookups="false" keystoreFile ="/usr/local/platform/.security/tomcat/certs/tomcat.keystore" keystorePass ="pPSTJpLa8QLuEpVp" keystoreType ="PKCS12" maxHttpHeaderSize="8192" maxSpareThreads="150" maxThreads="150" minSpareThreads="25" port="443" protocol="HTTP/1.1" scheme="https" secure="true" server=" " sessionTimeout="3600" sslProtocol="TLSv1.2" sessionCacheSize="10000"/>

Certificate which is presented when you try to initiate connection to one of web-applications hosted by Tomcat is located in a password-protected keystore:

/usr/local/platform/.security/tomcat/certs/tomcat.keystore

This keystore can be accessed with OpenSSL utilite to check it's content:

openssl pkcs12 -in /usr/local/platform/.security/tomcat/certs/tomcat.keystore -info -password file:/usr/local/platform/.security/tomcat/keys/tomcat.passphrase

Output of provided above command will show pem-encoded certificate of Tomcat Service, and also a private-key after keystorePass will be entered in a prompt.

Tomcat-hosted services, which need certificate-verification for outbound SSL-connections(such as secure connection to LDAP by IMS), are using tomcat-trust.keystore as trust-storage for verification of certificates presented by server during SSL-handshake.

Truststore location:

/usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore

Get a list of certificates from trust-store:

openssl pkcs12 -in /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore -info -password file:/usr/local/platform/.security/tomcat/keys/tomcat-trust.passphrase

Unload certificates from trust-store to temporary file and view them all at once:

openssl pkcs12 -in /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore -info -password file:/usr/local/platform/.security/tomcat/keys/tomcat-trust.passphrase 2>dev/null 1>/root/tomcat-trust.pem

openssl crl2pkcs7 -nocrl -certfile /root/tomcat-trust.pem | openssl pkcs7 -print_certs -noout -text

If certificate, which must be in truststore, is missing, it can be imported to keystore:

keytool -importcert -file somecert.pem -storetype pkcs12 -keystore /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore -storepass $(cat /usr/local/platform/.security/tomcat/keys/tomcat-trust.passphrase)

If whole trust-store is corrupted, it can be restored with following script:

#!/bin/bash

mv /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore{,.bak}

passphrase=$(cat /usr/local/platform/.security/tomcat/keys/tomcat-trust.passphrase)

for f in /usr/local/platform/.security/tomcat/trust-certs/*.pem do echo "Processing $f" /usr/local/thirdparty/java/j2sdk/bin/keytool -importcert -keystore /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore -alias "$(basename ${f%%.pem})" -noprompt -storepass $passphrase -storetype pkcs12 -providername JsafeJCE -providerclass com.rsa.jsafe.provider.JsafeJCE -providerpath /usr/local/thirdparty/java/cryptojFIPS.jar -file "$f" done

chown certbase:ccmbase /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore chmod 755 /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore chcon --reference='/usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore.bak' /usr/local/platform/.security/tomcat/trust-certs/tomcat-trust.keystore

Text of a script can be saved in file, and executed in following way:

bash /root/truststore_repair.sh