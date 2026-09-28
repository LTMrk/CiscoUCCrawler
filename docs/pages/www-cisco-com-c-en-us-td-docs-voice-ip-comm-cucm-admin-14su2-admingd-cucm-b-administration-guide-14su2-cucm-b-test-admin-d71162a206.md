---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-admingd-cucm-b-administration-guide-14su2-cucm-b-test-admin-d71162a206
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/adminGd/cucm_b_administration-guide-14su2/cucm_b_test-adminguide_chapter_010001.html
retrieved_at: 2026-08-17T00:43:53.180907+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 8, 2025

Chapter: Manage IPSec Policies

## Chapter: Manage IPSec Policies

# Manage IPSec Policies

## IPsec Policies Overview

IPsec is a framework that ensures private, secure communications over IP networks through the use of cryptographic security
                              services. IPsec policies are used to configure IPsec security services. The policies provide varying levels of protection
                              for most traffic types in your network. You can configure IPsec policies to meet the security requirements of a computer,
                              organizational unit (OU), domain, site, or global enterprise.

## Configure IPsec Policies

Because any changes that you make to an IPsec policy during a system upgrade will be lost, don't modify or create IPsec policies
                                                during an upgrade.

IPsec requires bidirectional provisioning, or one peer for each host (or gateway).

When you provision the IPsec policy on two Unified Communications Manager nodes with one IPsec policy protocol set to "ANY" and the other IPsec policy protocol set to "UDP" or "TCP" , the validation can result in a false negative if run from the node that uses the "ANY" protocol.

IPsec, especially with encryption, affects the performance of
                                                			 your system.

If the IPsec policy is configured on the current or upgraded version but not configured on the base version, ensure that you
                                                either delete or disable the IPsec policy when you try to switch this version to the base version. This is because the IPsec
                                                policy will be configured only on one of the nodes and the other node won't have the IPsec policy configured until you switch-back
                                                both these versions. Else, this leads to connectivity issues.

After the Unified CM node reboot, if the IPsec connection isn't up, ensure that you restart the IPsec service using the command utils ipsec restart to establish the IPsec connection successfully. This workaround is to mitigate any issues with IPsec service restart before
                                                the network connectivity is established.

From Release 14 onwards, the IPsec certificates are no longer uploaded to the IPsec trust list automatically.

A restart of the IPsec service is required when you make changes to the IPsec certificate.

Step 1

From Cisco Unified OS Administration, choose Security > IPSec
                                             				  Configuration .

Step 2

Click Add New .

Step 3

Configure the fields on the IPSEC Policy
                                          			 Configuration window. See the online help for more information about the fields and their configuration options.

Step 4

Click Save .

Step 5

(Optional) To validate IPsec, choose Services > Ping , check the Validate IPsec check box, and then click Ping .

## Check IPsec Certificates

Use this procedure to check the IPsec certificates:

Step 1

From Cisco Unified OS Administration, choose Security > Management Certificate .

Step 2

Specify search criteria and then click Find .

Step 3

Search for the IPsec certificates (log into the Publisher and Subscriber nodes separately).

Usually, Subscriber node IPsec certificates cannot be viewed on Publisher nodes. However, the Publisher node IPsec certificates
                                                      can be viewed on Subscriber nodes of the IM and Presence Service nodes.

To enable IPsec connectivity, you must use a CA signed IPsec certificate from the other system as an IPsec-Trust certificate on all the Unified Communications Manager nodes.

The previous certificate with the same Common Name in IPsec-Trust must be removed before uploading the new certificate to IPsec-Trust

## Manage IPsec Policies

Because any changes that you make to an IPsec policy during a system upgrade are lost, do not modify or create IPsec policies
                              during an upgrade.

Caution

Any changes that you make to the existing IPsec certificate because of hostname, domain, or IP address changes require you
                                          to delete the IPsec policies and recreate them, if certificate names are changed. If certificate names are unchanged, then
                                          after importing the remote node's regenerated certificate, the IPsec policies must be disabled and enabled.

Step 1

From Cisco Unified OS Administration, choose Security > IPSEC
                                             				  Configuration .

Step 2

To display,
                                       			 enable, or disable a policy, follow these steps:

Click the
                                             				  policy name.

To enable or
                                             				  disable the policy, check or uncheck the Enable Policy check box.

Click Save .

If you disable the policy, you must run the utils ipsec restart command for the disable changes to take effect.

Step 3

To delete one or
                                       			 more policies, follow these steps:

Check the
                                             				  check box next to each policy that you want to delete.

You can
                                                					 click Select All to select all policies or Clear All to clear all the check boxes.

Click Delete Selected .

| Note | Because any changes that you make to an IPsec policy during a system upgrade will be lost, don't modify or create IPsec policies
                                                during an upgrade. IPsec requires bidirectional provisioning, or one peer for each host (or gateway). When you provision the IPsec policy on two Unified Communications Manager nodes with one IPsec policy protocol set to "ANY" and the other IPsec policy protocol set to "UDP" or "TCP" , the validation can result in a false negative if run from the node that uses the "ANY" protocol. IPsec, especially with encryption, affects the performance of
                                                			 your system. If the IPsec policy is configured on the current or upgraded version but not configured on the base version, ensure that you
                                                either delete or disable the IPsec policy when you try to switch this version to the base version. This is because the IPsec
                                                policy will be configured only on one of the nodes and the other node won't have the IPsec policy configured until you switch-back
                                                both these versions. Else, this leads to connectivity issues. After the Unified CM node reboot, if the IPsec connection isn't up, ensure that you restart the IPsec service using the command utils ipsec restart to establish the IPsec connection successfully. This workaround is to mitigate any issues with IPsec service restart before
                                                the network connectivity is established. From Release 14 onwards, the IPsec certificates are no longer uploaded to the IPsec trust list automatically. A restart of the IPsec service is required when you make changes to the IPsec certificate. |
|---|---|

| Step 1 | From Cisco Unified OS Administration, choose Security > IPSec
                                             				  Configuration . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Configure the fields on the IPSEC Policy
                                          			 Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 4 | Click Save . |
| Step 5 | (Optional) To validate IPsec, choose Services > Ping , check the Validate IPsec check box, and then click Ping . |

| Step 1 | From Cisco Unified OS Administration, choose Security > Management Certificate . |
|---|---|
| Step 2 | Specify search criteria and then click Find . |
| Step 3 | Search for the IPsec certificates (log into the Publisher and Subscriber nodes separately). Note Usually, Subscriber node IPsec certificates cannot be viewed on Publisher nodes. However, the Publisher node IPsec certificates
                                                      can be viewed on Subscriber nodes of the IM and Presence Service nodes. To enable IPsec connectivity, you must use a CA signed IPsec certificate from the other system as an IPsec-Trust certificate on all the Unified Communications Manager nodes. The previous certificate with the same Common Name in IPsec-Trust must be removed before uploading the new certificate to IPsec-Trust | Note | Usually, Subscriber node IPsec certificates cannot be viewed on Publisher nodes. However, the Publisher node IPsec certificates
                                                      can be viewed on Subscriber nodes of the IM and Presence Service nodes. To enable IPsec connectivity, you must use a CA signed IPsec certificate from the other system as an IPsec-Trust certificate on all the Unified Communications Manager nodes. The previous certificate with the same Common Name in IPsec-Trust must be removed before uploading the new certificate to IPsec-Trust |
| Note | Usually, Subscriber node IPsec certificates cannot be viewed on Publisher nodes. However, the Publisher node IPsec certificates
                                                      can be viewed on Subscriber nodes of the IM and Presence Service nodes. To enable IPsec connectivity, you must use a CA signed IPsec certificate from the other system as an IPsec-Trust certificate on all the Unified Communications Manager nodes. The previous certificate with the same Common Name in IPsec-Trust must be removed before uploading the new certificate to IPsec-Trust |

| Note | Usually, Subscriber node IPsec certificates cannot be viewed on Publisher nodes. However, the Publisher node IPsec certificates
                                                      can be viewed on Subscriber nodes of the IM and Presence Service nodes. To enable IPsec connectivity, you must use a CA signed IPsec certificate from the other system as an IPsec-Trust certificate on all the Unified Communications Manager nodes. The previous certificate with the same Common Name in IPsec-Trust must be removed before uploading the new certificate to IPsec-Trust |
|---|---|

| Caution | Any changes that you make to the existing IPsec certificate because of hostname, domain, or IP address changes require you
                                          to delete the IPsec policies and recreate them, if certificate names are changed. If certificate names are unchanged, then
                                          after importing the remote node's regenerated certificate, the IPsec policies must be disabled and enabled. |
|---|---|

| Step 1 | From Cisco Unified OS Administration, choose Security > IPSEC
                                             				  Configuration . |
|---|---|
| Step 2 | To display,
                                       			 enable, or disable a policy, follow these steps: Click the
                                             				  policy name. To enable or
                                             				  disable the policy, check or uncheck the Enable Policy check box. Click Save . If you disable the policy, you must run the utils ipsec restart command for the disable changes to take effect. |
| Step 3 | To delete one or
                                       			 more policies, follow these steps: Check the
                                             				  check box next to each policy that you want to delete. You can
                                                					 click Select All to select all policies or Clear All to clear all the check boxes. Click Delete Selected . |