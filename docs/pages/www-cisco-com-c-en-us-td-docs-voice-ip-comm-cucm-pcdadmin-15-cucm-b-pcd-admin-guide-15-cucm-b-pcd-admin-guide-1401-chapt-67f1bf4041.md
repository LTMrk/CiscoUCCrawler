---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-15-cucm-b-pcd-admin-guide-15-cucm-b-pcd-admin-guide-1401-chapt-67f1bf4041
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/15/cucm_b_pcd-admin-guide-15/cucm_b_pcd-admin-guide-1401_chapter_01000.html
retrieved_at: 2026-08-17T00:33:23.908546+00:00
---

Prime Collaboration Deployment Administration Guide, Release 15 and SUs

# Prime Collaboration Deployment Administration Guide, Release 15 and SUs

Updated: February 5, 2026

Chapter:  CTL Update

## Chapter:  CTL Update

- CTL Update

- More Information

- Bulk Certificate                              	 Management

# CTL Update

## More Information

For information about performing a CTL update, see the "Security Basics" section in the .

## Bulk Certificate
                        	 Management

Bulk certificate
                              		  management must be performed manually on both source nodes and destination nodes.
                              		  The source nodes and destination nodes must be up and running at this point.
                              		  Phones are registered with the source nodes.

Step 1

On the
                                       			 Destination Cluster Publisher, navigate to Cisco Unified Operating System
                                       			 Administration and choose Security > Bulk Certificate Management .

Step 2

Define the
                                       			 Central Secure File Transfer Protocol (SFTP) server IP address, port, user, password, and directory.

Step 3

Use the Export button to export all Trivial File Transfer Protocol (TFTP) certificates from the
                                       			 destination cluster to the central SFTP server.

Step 4

On the Source
                                       			 Cluster Publisher, navigate to Cisco Unified Operating System Administration.
                                       			 Select Security > Bulk Certificate Management .

Step 5

Define the
                                       			 Central SFTP server with same parameters that you used in Step 2.

Step 6

Click Export to export all TFTP certificates from
                                       			 source cluster to the central SFTP server.

Step 7

Click Consolidate to consolidate all the TFTP
                                       			 certificates on the central SFTP server. You can perform this step on either
                                       			 the source or destination cluster, using the Bulk Certificate Management
                                       			 interface.

Step 8

On the
                                       			 Source cluster, click Bulk
                                          				Certificate Import to import the TFTP certificates from the
                                       			 central SFTP server.

Step 9

On the
                                       			 Destination cluster, click Bulk
                                          				Certificate Import to import the TFTP certificates from the
                                       			 central SFTP server.

Step 10

Use Dynamic Host Configuration Protocol (DHCP) option 150 to point the phones to the
                                       			 new destination cluster TFTP server.

Upon reset
                                          			 or power cycle, the phones will download the new destination cluster ITL file
                                          			 and attempt to authenticate the new Initial Trust List (ITL) file signature with the certificates in
                                          			 the existing ITL file.

No
                                          			 certificate in the existing ITL file can be used to authenticate the signature,
                                          			 so the phone requests the signer's certificate from the old Trust Verification Service (TVS) server on the
                                          			 source cluster.

The phone
                                          			 sends this request to the source cluster TVS service on TCP port 2445.

The bulk
                                          			 certificate exchange in Steps 1 through 9 provides the TVS service in the
                                          			 source cluster with the TFTP certificate on the destination cluster that signed
                                          			 the new ITL file.

TVS
                                          			 returns the certificate to the phone, which allows the phone to authenticate
                                          			 the signature and replace the old ITL file with the newly downloaded ITL file.

The phone
                                          			 can now download and authenticate the signed configuration files from the new
                                          			 destination cluster.

| Note | If you are performing a migration with network migration (where one or more hostnames or IP addresses change between the source
                                       and destination nodes), update the IP addresses or hostnames of destination nodes in your DNS server before you begin the
                                       migration task. |
|---|---|

| Step 1 | On the
                                       			 Destination Cluster Publisher, navigate to Cisco Unified Operating System
                                       			 Administration and choose Security > Bulk Certificate Management . |
|---|---|
| Step 2 | Define the
                                       			 Central Secure File Transfer Protocol (SFTP) server IP address, port, user, password, and directory. |
| Step 3 | Use the Export button to export all Trivial File Transfer Protocol (TFTP) certificates from the
                                       			 destination cluster to the central SFTP server. |
| Step 4 | On the Source
                                       			 Cluster Publisher, navigate to Cisco Unified Operating System Administration.
                                       			 Select Security > Bulk Certificate Management . |
| Step 5 | Define the
                                       			 Central SFTP server with same parameters that you used in Step 2. |
| Step 6 | Click Export to export all TFTP certificates from
                                       			 source cluster to the central SFTP server. |
| Step 7 | Click Consolidate to consolidate all the TFTP
                                       			 certificates on the central SFTP server. You can perform this step on either
                                       			 the source or destination cluster, using the Bulk Certificate Management
                                       			 interface. |
| Step 8 | On the
                                       			 Source cluster, click Bulk
                                          				Certificate Import to import the TFTP certificates from the
                                       			 central SFTP server. |
| Step 9 | On the
                                       			 Destination cluster, click Bulk
                                          				Certificate Import to import the TFTP certificates from the
                                       			 central SFTP server. |
| Step 10 | Use Dynamic Host Configuration Protocol (DHCP) option 150 to point the phones to the
                                       			 new destination cluster TFTP server. Upon reset
                                          			 or power cycle, the phones will download the new destination cluster ITL file
                                          			 and attempt to authenticate the new Initial Trust List (ITL) file signature with the certificates in
                                          			 the existing ITL file. No
                                          			 certificate in the existing ITL file can be used to authenticate the signature,
                                          			 so the phone requests the signer's certificate from the old Trust Verification Service (TVS) server on the
                                          			 source cluster. The phone
                                          			 sends this request to the source cluster TVS service on TCP port 2445. The bulk
                                          			 certificate exchange in Steps 1 through 9 provides the TVS service in the
                                          			 source cluster with the TFTP certificate on the destination cluster that signed
                                          			 the new ITL file. TVS
                                          			 returns the certificate to the phone, which allows the phone to authenticate
                                          			 the signature and replace the old ITL file with the newly downloaded ITL file. The phone
                                          			 can now download and authenticate the signed configuration files from the new
                                          			 destination cluster. |