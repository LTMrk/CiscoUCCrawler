---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213407-migrate-phon-6254aeb07f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213407-migrate-phones-between-secure-clusters.html
retrieved_at: 2026-08-21T13:58:17.749398+00:00
---

Migrate Phones Between Secure Clusters

# Migrate Phones Between Secure Clusters

### Download Options

Updated: December 6, 2018

Document ID: 213407

Contents

## Contents

## Introduction

This document describes how to migrate phones between two secure Cisco Unified Communications Manager (CUCM) clusters.

Contributed by David Norman, Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUCM.

### Components Used

The information in this document is based on these software versions:

Source cluster: CUCM version 10.5.2.11900-3 Destination cluster:  CUCM version 11.0.1.10000-10 8861 phone using firmware sip88xx.10-3-1-20

Certificate Trust List ( CTL) files are signed with the CallManager certificate (not USB token)

### Background

During the migration process, the phone attempts to setup a secure connection to the source clusters Cisco Trust Verification Service (TVS) to verify the destination clusters CallManager certificate. If the phone's Certificate Trust List (CTL) and Identity Trust List (ITL) file are invalid, the phone cannot complete the secure handshake with the TVS and the migration to the destination cluster won't succeed. Before you start the phone migration process, confirm that the phones have the correct CTL/ITL file installed. Also on the source cluster, confirm that the enterprise feature "Prepare Cluster for Rollback to Pre 8.0" is set to False.

## Configure

Import the destination clusters CallManager certificate into the source clusters CallManager-trust and Phone-SAST-trust store. There are two methods to do this.

Method 1.

Use the Bulk Certificate Tool and complete these steps on both the source and destination clusters.

Step 1. Navigate to Cisco Unified OS Administration page > Security > Bulk Certificate Management on both source and destination clusters.

Step 2. Enter the details for the Secure File Transfer Protocol (SFTP) server and select Save .

Step 3. Select Export and export the Trivial File Transfer Protocol (TFTP) certificate.

Step 4. Click on the Consolidate button to perform the certificate consolidation.  This creates a PKCS12 file which includes both the source and destination CallManager certificate.

Step 5. Import the consolidated certificates back into each cluster.

During the consolidation process (Step 5), the source clusters CallManager certificate is uploaded to the destination cluster in the CallManager-trust and Phone-SAST-trust store. This allows the phones to migrate back to the source cluster. If the manual method is followed, the source clusters CallManager certificate won't be uploaded to the destination cluster. This means that you cannot migrate the phones back to the source cluster. If you want the option to migrate the phones back to the source cluster, you need to upload the source clusters CallManager certificate to the destination clusters CallManager-trust and Phone-SAST-trust store.

Note : Both clusters must export the TFTP certificate to the same SFTP server and the same SFTP directory.

Note : Step 4 is only required on one cluster. If you migratephones between CUCM version 8.x or 9.x to CUCM version 10.5.2.13900-12 or newer, take note of this Cisco bug ID CSCuy43181 before you consolidate the certificates.

Method 2.

Manually import the certificates. Complete these steps on the destination cluster.

Step 1. Navigate to Cisco Unified OS Administration page > Security > Certificate Management .

Step 2. Select CallManager.pem certificate and download it.

Step 3. Select ITLrecovery.pem certificate and download it

Step 4 . Upload the CallManager certificate to the source cluster publisher as a CallManger-trust and Phone-SAST-trust certificate.

Step 5. Upload the ITLrecovery Certificate to the source cluster as Phone-SAST-Trust

Step 6. Restart TVS in all nodes from the source cluster.

Then the certificates replicate to the other nodes in the cluster.

Steps 3, 5, 6 will apply to scenarios of migrating phone from 8.x to 12.x

Note : The CallManager certificate needs to be downloaded from all nodes running the TFTP service on the destination cluster.

Once the certificates have been uploaded with one of the above methods, change the phones Dynamic Host Configuration Protocol (DHCP) Option 150 to point to the destination clusters TFTP address.

Caution : One method to migrate phones inbetween non-secure clusters is to set the "Prepare Cluster for Rollback to pre 8.0" to True on the source cluster and restart the phones. This is not an option when you migrate phones between secure clusters. This is becuase the rollback to pre 8.0 feature only blanks out the ITL file (it does not blank out the CTL file). This means that when the phone is migrated and it downloads the CTL file from the destination cluster, it needs to verify the new CTL with the source clusters TVS. Since the phone's ITL file does not contain the source clusters TVS certificate, the handshake fails when the phone tries to establish a secure connection to the TVS service.

## Verify

This is an excerpt from the phone console logs and the TVS logs (set to detailed) of the source cluster. The snippets show the process of the phones registration to the destination cluster.

1. The phone boots and downloads the CTL file from the destination cluster.

```
3232 NOT Nov 29 06:33:59.011270 downd-DDFORK - execing [/usr/sbin/dgetfile][-L620][ ]
3233 NOT Nov 29 06:33:59.033132 dgetfile(870)-GETXXTP [GT870][src=CTLSEPB000B4BA0AEE.tlv][dest=/tmp/CTLFile.tlv][serv=][serv6=][sec=0]
```

2. The CTL file is signed by the destination clusters call manager certificate which is not in the phones existing CTL or ITL file. This means that the phone needs to reach out to its TVS service to verify the certificate. At this point the phone still has its old configuration which contains the IP address of the source cluster TVS service (the TVS specified in the phones configuration is the same as the phones call manager group). The phone sets up an SSL connection to the TVS service. When the TVS service presents its certificate to the phone, the phone verifies the certificate against the certificate in its ITL file. If they are the same, the handshake completes successfully.

```
3287 INF Nov 29 06:33:59.395199 SECUREAPP-Attempting connect to TVS server addr [192.168.11.32], mode [IPv4]
3288 INF Nov 29 06:33:59.395294 SECUREAPP-TOS set to [96] on sock, [192.168.11.32][11]
3289 INF Nov 29 06:33:59.396011 SECUREAPP-TCP connect() successful, [192.168.11.32] [11]
3290 DEB Nov 29 06:33:59.396111 SECUREAPP-BIO created with: addr:192.168.11.32, port:2445, mode:IPv4
3291 INF Nov 29 06:33:59.396231 SECUREAPP-Sec SSL Connection - TVS.
3292 INF Nov 29 06:33:59.396379 SECUREAPP-SSL session setup - Requesting Cert
3293 DEB Nov 29 06:33:59.396402 SECUREAPP-Obtaining certificate.
3294 INF Nov 29 06:33:59.396444 SECUREAPP-SSL session setup - Get Active cert ok
3295 DEB Nov 29 06:33:59.396464 SECUREAPP-SSL session setup - cert len=785, type=LSC
3296 DEB Nov 29 06:33:59.396854 SECUREAPP-Certificate subject name = /serialNumber=PID:CP-8861 SN:FCH18198CNQ/C=AU/O=stormin/OU=IST/CN=CP-8861-SEPB000B4BA0AEE
3297 DEB Nov 29 06:33:59.396917 SECUREAPP-SSL session setup - Certificate issuer name = /C=AU/O=stormin/OU=IST/CN=CAPF-a7fb32bf/ST=NSQ/L=Sydney
3298 INF Nov 29 06:33:59.396947 SECUREAPP-SSL session setup - Requesting Pkey
3299 INF Nov 29 06:33:59.397024 SECUREAPP-SSL session setup - Get private key ok
3300 DEB Nov 29 06:33:59.397045 SECUREAPP-SSL session setup - key len=1191
3301 INF Nov 29 06:33:59.399181 SECUREAPP-Setup SSL session - SSL use certificate okay
3302 INF Nov 29 06:33:59.399477 SECUREAPP-Setup SSL session - SSL use private key okay
3303 DEB Nov 29 06:33:59.399974 SECUREAPP-Sec SSL Connection - Added SSL connection handle 0x40e01270, connDesc 11 to table.
3304 DEB Nov 29 06:33:59.400225 SECUREAPP-Sec SSL Connection - check status & perform handshake.
3305 DEB Nov 29 06:33:59.401086 SECUREAPP-Blocked TVS Secure Connection - Waiting (0) ....
3306 DEB Nov 29 06:33:59.401796 SECUREAPP-Sec SSL Connection - check status & perform handshake.
3307 DEB Nov 29 06:33:59.403321 SECUREAPP-SSL session setup Cert Verification - Role is = 21
3308 INF Nov 29 06:33:59.403412 SECUREAPP-SSL session setup Cert Verification - Invoking certificate validation helper plugin.
3309 INF Nov 29 06:33:59.403662 SECUREAPP-SSL session setup Cert Verification - Certificate validation helper plugin returned.
3310 INF Nov 29 06:33:59.403731 SECUREAPP-SSL session setup Cert Verification - Certificate is valid.
3311 DEB Nov 29 06:33:59.403784 SECUREAPP-SSL session setup Cert Verification - returning validation result = 1
3312 ERR Nov 29 06:33:59.428892 downd-SOCKET accept errno=4 "Interrupted system call"
3313 DEB Nov 29 06:33:59.907337 SECUREAPP-Blocked TVS Secure Connection - Waiting (1) ....
3314 DEB Nov 29 06:33:59.907393 SECUREAPP-Sec SSL Connection - check status & perform handshake.
3315 NOT Nov 29 06:33:59.908586 SECUREAPP-Sec SSL Connection - Handshake successful.
3316 INF Nov 29 06:33:59.908696 SECUREAPP-Sec SSL Connection - caching disabled, session not saved
3317 DEB Nov 29 06:33:59.908752 SECUREAPP-Connection to server succeeded
```

3. The TVS logs show the incoming connection from the phone and the handshake was successful.

```
18:01:05.333 | debug Accepted TCP connection from socket 0x00000012, fd = 8
18:01:05.333 | debug Total Session attempted = 7 accepted = 7
18:01:05.334 | debug tvsGetNextThread
18:01:05.334 | debug Recd event
18:01:05.334 | debug new ph on fd 8
18:01:05.334 | debug 7:UNKNOWN:Got a new SCB from RBTree
18:01:05.334 | debug ipAddrStr (Phone) 192.168.11.100
18:01:05.334 | debug 8:UNKNOWN:Got a new ph conn 192.168.11.100 on 8, Total Acc = 7..
18:01:05.334 | debug addded 8 to readset
18:01:05.338 | debug after select, 8 was set
18:01:05.338 | debug ipAddrStr (Phone) 192.168.11.100
18:01:05.855 | debug tvsSSLHandShakeNotify
18:01:05.855 | debug 192.168.11.100: tvsSSLHandShake Session ciphers - AES256-SHA
18:01:05.855 | debug addded 8 to readset
18:01:05.855 | debug Recd event
18:01:05.855 | debug TLS HS Done for ph_conn
```

4. The phone console logs show the phone send a request to the TVS service to verify the call manager certificate from the destination cluster.

```
3318 DEB Nov 29 06:33:59.908800 SECUREAPP-TVS provider Init - connect returned TVS srvr sock: 11
3319 DEB Nov 29 06:33:59.908848 SECUREAPP-TVS process request - processing TVS Query Certificate request.
3320 NOT Nov 29 06:33:59.909322 SECUREAPP-TVS process request - Successfully sent the TVS request to TVS server, bytes written : 153
3321 DEB Nov 29 06:33:59.909364 SECUREAPP-==== TVS process request - request byte dump ====, len = 153
3322 DEB Nov 29 06:33:59.913075 SECUREAPP-TVS Service receives 1480 bytes of data
3323 DEB Nov 29 06:33:59.913270 SECUREAPP-==== TVS process response - response byte dump ====, len = 1480
3324 DEB Nov 29 06:33:59.914466 SECUREAPP-Found the work order from pending req list element at index 0
```

5. The TVS logs show the request is received.

```
18:01:06.345 | debug 8:UNKNOWN:Incoming Phone Msg:
HEX_DUMP: Len = 153:
18:01:06.345 | debug 57 01 03 00 00 00 03 e9
18:01:06.345 | debug 00 8f 01 00 18 01 43 50
18:01:06.345 | debug 2d 38 38 36 31 2d 53 45
18:01:06.345 | debug 50 42 30 30 30 42 34 42
18:01:06.345 | debug 41 30 41 45 45 03 00 42
18:01:06.345 | debug 43 4e 3d 75 63 6d 31 31
18:01:06.345 | debug 70 75
18:01:06.345 | debug tvsPhoneDecodeMsg -
Decoded Phone Msg:
18:01:06.345 | debug Protocol Discriminator: 57
18:01:06.345 | debug MsgType : TVS_MSG_QUERY_CERT_REQ
18:01:06.345 | debug Session Id : 0
18:01:06.345 | debug Length : 143
18:01:06.345 | debug 8:UNKNOWN:TVS CORE: Rcvd Event: TVS_EV_QUERY_CERT_REQ in State: TVS_STATE_AWAIT_REQ
18:01:06.345 | debug tvsHandleQueryCertReq
18:01:06.345 | debug tvsHandleQueryCertReq : Subject Name is: CN=ucm11pub.stormin.local;OU=IST;O=Stormin;L=Brisbane;ST=QLD;C=AU
18:01:06.345 | debug tvsHandleQueryCertReq : Issuer Name is: CN=stormin-WIN2012-CA
18:01:06.345 | debug tvsHandleQueryCertReq : Serial Number is: 24000000179479B8F124AC3F3B000000000017
18:01:06.345 | debug CertificateDBCache::getCertificateInformation - Looking up the certificate cache using Unique MAP ID : 24000000179479B8F124AC3F3B000000000017CN=stormin-WIN2012-CA
18:01:06.345 | debug CertificateDBCache::getCertificateInformation - Found entry {rolecount : 2}
18:01:06.345 | debug CertificateDBCache::getCertificateInformation - {role : 0}
18:01:06.346 | debug CertificateDBCache::getCertificateInformation - {role : 3}
18:01:06.346 | debug convertX509ToDER -x509cert : 0xbb696e0
```

6. The TVS logs show the certificate in its store and TVS sends a response to the phone.

```
18:01:06.346 | debug 8:UNKNOWN:Sending QUERY_CERT_RES msg
18:01:06.346 | debug tvsPhoneDecodeMsg -
Decoded Phone Msg:
18:01:06.346 | debug Protocol Discriminator: 57
18:01:06.346 | debug MsgType : TVS_MSG_QUERY_CERT_RES
18:01:06.346 | debug Session Id : 0
18:01:06.346 | debug Length : 1470
18:01:06.346 | debug ReasonInfo : 0��0���$
18:01:06.346 | debug Number of Certs : 1
18:01:06.346 | debug Cert[0] :
18:01:06.346 | debug Cert Type : 0
HEX_DUMP: Len = 1451:
18:01:06.346 | debug 30 82 05 a7 30 82 04 8f
18:01:06.346 | debug a0 03 02 01 02 02 13 24
18:01:06.346 | debug 00 00 00 17 94 79 b8 f1
18:01:06.346 | debug 24 ac 3f 3b 00 00 00 00
18:01:06.346 | debug 00 17 30 0d 06 09 2a 86
18:01:06.346 | debug 48 86 f7 0d 01 01 0b 05
18:01:06.346 | debug 00 30
18:01:06.346 | debug Version : 0
18:01:06.346 | debug PublicKey :
HEX_DUMP: Len = 4:
18:01:06.347 | debug 00 01 51 80
18:01:06.347 | debug Sending TLS Msg ..
HEX_DUMP: Len = 1480:
18:01:06.347 | debug 57 01 04 f7 00 00 03 e9
18:01:06.347 | debug 05 be 07 00 01 00 02 05
18:01:06.347 | debug ab 30 82 05 a7 30 82 04
18:01:06.347 | debug 8f a0 03 02 01 02 02 13
18:01:06.347 | debug 24 00 00 00 17 94 79 b8
18:01:06.347 | debug f1 24 ac 3f 3b 00 00 00
18:01:06.347 | debug 00 00
18:01:06.347 | debug ipAddrStr (Phone) 192.168.11.100
```

7. The phone console logs show that the certifcate is verified successfully and the CTL file is updated.

```
3325 INF Nov 29 06:33:59.915121 SECUREAPP-TVS added cert to TVS cache - expires in 24 hours
3333 NOT Nov 29 06:34:00.411671 SECUREAPP-Hashes match... authentication successful.
3334 WRN Nov 29 06:34:00.412849 SECUREAPP-AUTH: early exit from parser loop; old version header?
3335 WRN Nov 29 06:34:00.412945 SECUREAPP-AUTH: hdr ver 1.2 (knows only upto 1.1)
3336 NOT Nov 29 06:34:00.413031 SECUREAPP-updateFromFile: TL parse to table: CTL_SUCCESS
3337 NOT Nov 29 06:34:00.413088 SECUREAPP-updateFromFile: Updating master TL table
3338 DEB Nov 29 06:34:00.413442 SECUREAPP-TL file verified successfully.
3339 INF Nov 29 06:34:00.413512 SECUREAPP-TL file updated.
```

8. The phone console logs show when the phone downloads its ITL file.

```
3344 NOT Nov 29 06:34:00.458890 dgetfile(877)-GETXXTP [GT877][src=ITLSEPB000B4BA0AEE.tlv][dest=/tmp/ITLFile.tlv][serv=][serv6=][sec=0]
3345 NOT Nov 29 06:34:00.459122 dgetfile(877)-In normal mode, call - > makeXXTPrequest (V6...)

3281 NOT Dec 14 06:34:00.488697 dgetfile(851)-XXTP complete - status = 100 
3282 NOT Dec 14 06:34:00.488984 dgetfile(851)-XXTP actualserver [192.168.11.51]
```

9. The ITL file is verified against the CTL file. The CTL file contains the destination clusters C allManager certificate . This means the phone can verify the certificate without contacting the source clusters TVS service.

```
3287 NOT Nov 29  06:34:00.499372 SECUREAPP-Hashes match... authentication successful.
3288 WRN Nov 29  06:34:00.500821 SECUREAPP-AUTH: early exit from parser loop; old version header?
3289 WRN Nov 29 06:34:00.500987 SECUREAPP-AUTH: hdr ver 1.2 (knows only upto 1.1)
3290 NOT Nov 29  06:34:00.501083 SECUREAPP-updateFromFile: TL parse to table: CTL_SUCCESS
3291 NOT Nov 29  06:34:00.501147 SECUREAPP-updateFromFile: Updating master TL table
3292 DEB Nov 29  06:34:00.501584 SECUREAPP-TL file verified successfully.
3293 INF Nov 29  06:34:00.501699 SECUREAPP-TL file updated.
```

## Troubleshoot

Before the migration process, verify the CTL/ITL on the phones. More information on how to verify the CTL/ITL can be found here: https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-callmanager/116232-technote-sbd-00.html#anc9