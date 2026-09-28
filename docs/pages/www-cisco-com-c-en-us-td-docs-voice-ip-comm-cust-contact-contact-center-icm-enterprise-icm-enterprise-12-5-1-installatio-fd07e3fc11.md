---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-fd07e3fc11
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_1251-staging-guide/ucce_b_1251-staging-guide_chapter_0110.html
retrieved_at: 2026-08-16T20:08:16.666396+00:00
---

Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Prepare to Work with Active Directory

## Chapter: Prepare to Work with Active Directory

- Prepare to Work with Active Directory

- Perform Preliminary                              	 Steps

- Domain Manager and                              	 OU Hierarchy

# Prepare to Work with Active Directory

## Perform Preliminary
                        	 Steps

Perform the
                              		  following steps before beginning to work with Active Directory.

Warning

The Domain Administrator must first create the root OU "Cisco_ICM" . You need not be a Domain Administrator to create the Cisco Root OU if that OU is going to be created in a nested OU (for
                                          example, Applications -> Voice Applications…), the Domain Administrator can create a parent OU with delegated rights to create
                                          Cisco_ICM Root OU.

Step 1

Review the
                                       			 system software staging guidelines.

Step 2

Ensure that you
                                       			 have installed Microsoft Windows.

Step 3

If you are installing a Logger or Distributor/HDS Administration &
                                       					DataServers, ensure that you have already installed Microsoft SQL Server.

## Domain Manager and
                        	 OU Hierarchy

The Instance is
                                    				not just a name in the registry.

Adding an
                                    				Instance only requires selecting a Facility and an Instance OU from the domain.

First,
                                          					 create the OU hierarchy when you install or upgrade the first server.

Then, choose
                                          					 an existing Instance from that hierarchy.

Integrated use
                                    				of the Domain Manager

When Domain Manager
                              		  creates Instance OUs, user accounts in old Unified ICM/CCE 
                              		  security groups are automatically copied to new security groups in the new
                              		  instance OU. The old groups are not modified.

| Warning | The Domain Administrator must first create the root OU "Cisco_ICM" . You need not be a Domain Administrator to create the Cisco Root OU if that OU is going to be created in a nested OU (for
                                          example, Applications -> Voice Applications…), the Domain Administrator can create a parent OU with delegated rights to create
                                          Cisco_ICM Root OU. |
|---|---|

| Step 1 | Review the
                                       			 system software staging guidelines. |
|---|---|
| Step 2 | Ensure that you
                                       			 have installed Microsoft Windows. |
| Step 3 | If you are installing a Logger or Distributor/HDS Administration &
                                       					DataServers, ensure that you have already installed Microsoft SQL Server. |

| Note | When you
                                                   					 add an instance, you add that instance's Setup security group to the local
                                                   					 Administrators group on that machine. When you remove an instance, it also
                                                   					 removes this security group. |
|---|---|