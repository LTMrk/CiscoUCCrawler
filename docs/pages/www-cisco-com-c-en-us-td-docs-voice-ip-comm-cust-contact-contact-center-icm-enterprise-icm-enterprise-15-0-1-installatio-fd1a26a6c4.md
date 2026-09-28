---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-fd1a26a6c4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_stagingguide_release_15_0_1/ucce_m_1261_prepare-work-active-directory.html
retrieved_at: 2026-08-16T19:58:52.138307+00:00
---

Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

# Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

Updated: March 24, 2025

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