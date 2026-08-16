---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-install-guide-uccx-b-1251-c13687388b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/install/guide/uccx_b_1251su1install-and-upgrade-guide/uccx_b_1252install-and-upgrade-guide_appendix_0111.html
retrieved_at: 2026-08-16T21:13:45.083582+00:00
---

Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU1

# Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Unified CCX Licenses

## Chapter: Unified CCX Licenses

# Unified CCX Licenses

From Unified CCX release 12.5(1), fresh install of Unified CCX supports only Smart Licensing. For more information on migrating
                           to smart Licensing, see Cisco Unified Contact Center Express Features Guide . If you are upgrading from releases prior to Unified CCX 12.5(1) and want to continue using Classic Licensing, see the following
                           sections in the document.

The Unified CCX licenses are based on a string called the license MAC, which is different from the physical MAC address of
                           a system. License MAC is dependent on the system parameters. A modification to any of the parameters can change license MAC,
                           thereby invalidating current License files. The following are the parameters on which the validity of a license MAC depends:

Time zone

NTP server 1 (or none)

NIC speed (or auto)

Hostname

IP Address

IP Mask

Gateway Address

Primary DNS

SMTP server

Certificate Information (Organization, Unit, Location, State, Country)

The Unified CCX  Warm Standby license and all other licenses
                                       				are node-locked to the License MAC address of the first node (typically the
                                       				Database Publisher node) of a Unified CCX cluster. When a second node is added,
                                       				the verification of a valid add-on Warm Standby license on the first node is performed.
                                       				After the cluster is set up, the licenses are valid on both the nodes in a
                                       				cluster.

## Obtain License MAC

License MAC can be obtained in two ways—by using either the Command Line Interface or the Administrator Web interface.

### Obtaining License MAC using Command Line Interface

Step 1

Log in to the Unified CCX system CLI using Unified CCX Administrator credentials.

Step 2

Run show status command.

Output of this command contains the license MAC.

Step 3

Use the license MAC to get the license from Cisco.

Contact the Support team for any license inquiries at: www.cisco.com/en/US/partner/support/tsd_cisco_worldwide_contacts.html

### Obtaining License MAC using Administrator Web Interface

Step 1

Login to the Unified CCX Administrator web interface using Unified CCX Administrator credentials.

User IDs are case-sensitive. To make them case-insensitive, you must install 12.5(1) SU1 ES02.

Step 2

Click System > License Management .

Step 3

Click Next .

Step 4

Obtain the license MAC from the View Licenses section.

Step 5

Use the license MAC to obtain license from Cisco.

## Upload
                        	 Licenses

Software
                              		  for all of the Unified CCX feature components are loaded on the system during
                              		  installation. However, no feature is available for use unless a license for
                              		  that feature is added and activated.

You can
                              		  upload and display licenses using the License Information page. To upload a
                              		  license, complete the following steps.

Step 1

From the Unified
                                       			 CCX Administration menu bar, choose System > License
                                             				  Information > Add License(s) .

The License
                                          				Information web page opens.

Step 2

Specify a
                                       			 License file or click Browse to locate a file.

You can either
                                          				specify a single file with a .lic extension or a .zip file containing multiple
                                          				.lic files.

While you are
                                                      				  upgrading from a previous release, if there are multiple licenses, zip all the
                                                      				  .lic files into a single .zip file and then upload the zip file. If specifying
                                                      				  a .zip file, ensure that all .lic files that need to be added are in the root
                                                      				  of the .zip file and are not in subfolders in the .zip file.

Step 3

Click Upload .

On successful
                                          				upload of the license, you will see the following confirmation message in the
                                          				status bar at the top of this web page : License
                                             				  has been uploaded successfully

If you upload an
                                          				Add-on license to increase the existing licensed Outbound IVR ports, the
                                          				following message will be displayed :

As the number of licensed
                                             				  Outbound IVR Ports have increased, please increase the number of ports in the
                                             				  Outbound Call Control Group to utilize all the licensed ports .

| Note | The Unified CCX  Warm Standby license and all other licenses
                                       				are node-locked to the License MAC address of the first node (typically the
                                       				Database Publisher node) of a Unified CCX cluster. When a second node is added,
                                       				the verification of a valid add-on Warm Standby license on the first node is performed.
                                       				After the cluster is set up, the licenses are valid on both the nodes in a
                                       				cluster. |
|---|---|

| Step 1 | Log in to the Unified CCX system CLI using Unified CCX Administrator credentials. |
|---|---|
| Step 2 | Run show status command. Output of this command contains the license MAC. |
| Step 3 | Use the license MAC to get the license from Cisco. Contact the Support team for any license inquiries at: www.cisco.com/en/US/partner/support/tsd_cisco_worldwide_contacts.html |

| Step 1 | Login to the Unified CCX Administrator web interface using Unified CCX Administrator credentials. Note User IDs are case-sensitive. To make them case-insensitive, you must install 12.5(1) SU1 ES02. | Note | User IDs are case-sensitive. To make them case-insensitive, you must install 12.5(1) SU1 ES02. |
|---|---|---|---|
| Note | User IDs are case-sensitive. To make them case-insensitive, you must install 12.5(1) SU1 ES02. |
| Step 2 | Click System > License Management . In the License Management page, by default Classic Licensing is selected. |
| Step 3 | Click Next . |
| Step 4 | Obtain the license MAC from the View Licenses section. |
| Step 5 | Use the license MAC to obtain license from Cisco. |

| Note | User IDs are case-sensitive. To make them case-insensitive, you must install 12.5(1) SU1 ES02. |
|---|---|

| Step 1 | From the Unified
                                       			 CCX Administration menu bar, choose System > License
                                             				  Information > Add License(s) . The License
                                          				Information web page opens. |
|---|---|
| Step 2 | Specify a
                                       			 License file or click Browse to locate a file. You can either
                                          				specify a single file with a .lic extension or a .zip file containing multiple
                                          				.lic files. Note While you are
                                                      				  upgrading from a previous release, if there are multiple licenses, zip all the
                                                      				  .lic files into a single .zip file and then upload the zip file. If specifying
                                                      				  a .zip file, ensure that all .lic files that need to be added are in the root
                                                      				  of the .zip file and are not in subfolders in the .zip file. | Note | While you are
                                                      				  upgrading from a previous release, if there are multiple licenses, zip all the
                                                      				  .lic files into a single .zip file and then upload the zip file. If specifying
                                                      				  a .zip file, ensure that all .lic files that need to be added are in the root
                                                      				  of the .zip file and are not in subfolders in the .zip file. |
| Note | While you are
                                                      				  upgrading from a previous release, if there are multiple licenses, zip all the
                                                      				  .lic files into a single .zip file and then upload the zip file. If specifying
                                                      				  a .zip file, ensure that all .lic files that need to be added are in the root
                                                      				  of the .zip file and are not in subfolders in the .zip file. |
| Step 3 | Click Upload . On successful
                                          				upload of the license, you will see the following confirmation message in the
                                          				status bar at the top of this web page : License
                                             				  has been uploaded successfully If you upload an
                                          				Add-on license to increase the existing licensed Outbound IVR ports, the
                                          				following message will be displayed : As the number of licensed
                                             				  Outbound IVR Ports have increased, please increase the number of ports in the
                                             				  Outbound Call Control Group to utilize all the licensed ports . |

| Note | While you are
                                                      				  upgrading from a previous release, if there are multiple licenses, zip all the
                                                      				  .lic files into a single .zip file and then upload the zip file. If specifying
                                                      				  a .zip file, ensure that all .lic files that need to be added are in the root
                                                      				  of the .zip file and are not in subfolders in the .zip file. |
|---|---|