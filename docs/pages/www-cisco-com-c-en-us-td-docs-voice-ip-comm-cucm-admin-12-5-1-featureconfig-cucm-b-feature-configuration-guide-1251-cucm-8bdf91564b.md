---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-featureconfig-cucm-b-feature-configuration-guide-1251-cucm-8bdf91564b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/featureConfig/cucm_b_feature-configuration-guide-1251/cucm_b_feature-configuration-guide-1251_chapter_0110011.html
retrieved_at: 2026-08-16T16:55:19.942954+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 13, 2025

Chapter: Extension Mobility Roaming Across Clusters

## Chapter: Extension Mobility Roaming Across Clusters

# Extension Mobility Roaming Across Clusters

To deploy Extension Mobility Roaming Across Clusters, you must be running a minimum release of Cisco Unified Communications
                                    Manager 12.0(1)SU1.

## Extension Mobility Roaming Across Clusters Overview

Extension Mobility Roaming Across Clusters gives users the ability to roam across multiple cluster and make or receive calls
                           even when the user's home cluster is down. This feature leverages the Intercluster Lookup Service (ILS) to replicate Extension
                           Mobility users' directory numbers across all the clusters.

When a  user logs in to a roaming cluster, their phone registers to the roaming cluster using the directory number. Unlike
                           Extension Mobility Cross Cluster (EMCC), where the phone from the visiting cluster registers to the home cluster, the roaming
                           feature allows the user to maintain their registration in whichever cluster they are visiting.

### Configuration Overview

To deploy this feature, you must do the following:

Set up an ILS network—ILS is used to synchronize directory number across the clusters.

For details on configuring ILS, see the Configure Intercluster Lookup Service chapter in the System Configuration Guide for Cisco Unified Communications Manager .

Set up a uniform dial plan—you require a uniform dial plan across the ILS network.

To set up a dial plan, see Configure the Dial Plan chapter in the System Configuration Guide for Cisco Unified Communications Manager .

Device profile and user information must be synced in all the clusters.

Configure Extension Mobility.

Configure Roaming access to your Extension Mobility users.

## System Requirements for Extension Mobility Roaming Across Clusters

The following system requirements exist for Cisco Unified Communications Manager:

Cisco Unified Communications Manager, Release 12.0(1)SU1 or higher.

Cisco Extension Mobility service must be running.

Intercluster Lookup Service must be running.

## Extension Mobility Roaming Across Clusters Login

### Login Terminology

The following figure depicts the home cluster versus a roaming cluster in Extension Mobility Roaming across Cluster.

### Login Process

Cisco Unified Communications Manager supports the Extension Mobility login for a superuser created across multiple clusters.
                              Extension Mobility login, in the roaming cluster allows superuser to access their phone settings, such as line appearances,
                              services, dial plans. A superuser can make or receive calls from the roaming cluster, in the same way as they do in the home
                              cluster.

In the preceding figure, let us assume Bob's DN as 1000-001, Alice's DN as 2000-001 and Kally's DN as 3000-001 registered
                              with Cluster 1, 2 and 3 respectively. When Kally dials Bob's DN 1000-001, Cluster 3 routes the call to Cluster 1 and Bob and
                              Kally are connected.

Let us assume Bob's home cluster is down and Bob is configured as superuser who can roam across the clusters. When Bob moves
                              to Cluster 2 and does Extension Mobility Login, hosting phone gets re-registered with Bob's settings. Once the login is successful,
                              all other clusters are updated with Bob's new location. Now when Kally dials Bob's DN 1000-01, Cluster 3 routes the call to
                              Cluster 2 and Bob and Kally are connected. Similarly, Bob can call Kally by dialing DN 3000-001.

If a superuser did the Extension Mobility login to another cluster, user will automatically log out from the home cluster.
                                                If the cluster is down, it waits until the cluster is up to log out from the user's previous login.

Extension Mobility Roaming Across Clusters supports the multi login behavior. Hence, superuser can login from multiple devices
                                                within the same cluster but not across the clusters.

## ILS Interaction

In Cisco Unified CM Administration, you can configure ILS on a pair of clusters and then join those clusters to form an ILS
                           network. Once you have established the ILS network, you can join additional clusters to the network without having to configure
                           the connections between each cluster.

Whenever Extension Mobility login or logout occurs, ILS sync starts to update the available information to other clusters.

Configuring user as superuser automatically initiates the ILS sync irrespective of Directory Number configuration for ILS.

For more information, see the Configure Intercluster Lookup Service chapter in the System Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

## Extension Mobility Roaming Across Clusters Task Flow

Step 1

Generate a Phone Feature List

Generate a report to identify devices that support the Extension Mobility feature.

Step 2

Configure Extension Mobility by completing, the following subtasks in order:

Configure Extension Mobility to allow users to temporarily access their phone settings, such as line appearances, services,
                                          and speed dials, from other phones when they login from remote cluster. Perform this task flow on both home and remote clusters,
                                          so that users will be able to access settings from either a home or remote cluster.

Step 3

Configure Roaming for Extension Mobility Users

Use this procedure to give Extension Mobility users the ability to roam between different clusters in an ILS network, while
                                          using the same login credentials.

### Generate a Phone Feature List

Generate a phone feature list report to determine which devices support the feature that you want to configure.

Step 1

From Cisco Unified Reporting, choose System Reports .

Step 2

From the list of reports, click Unified CM Phone Feature List .

Step 3

Perform one of the following steps:

- Choose Generate New Report (the bar chart icon)  to generate a new report.

- Choose Unified CM Phone Feature List if a report exists.

Step 4

From the Product drop-down list, choose All .

Step 5

Click the name of the feature that you want to configure.

Step 6

Click Submit , to generate the report.

### Activate Extension
                           	 Mobility Services

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server drop-down list, choose the requried node.

Step 3

Activate the following services:

Cisco CallManager

Cisco Tftp

Cisco Extension Mobility

ILS Service

You must choose publisher node to activate the ILS services.

Step 4

Click Save .

Step 5

Click OK .

### Configure the
                           	 Cisco Extension Mobility Phone Service

Configure the extension mobility IP phone service to which users
                                 				can later subscribe to access extension mobility.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Phone Services .

Step 2

Click Add
                                             				New .

Step 3

In the Service Name field, enter a name for the service.

Step 4

In the Service URL field, enter the Service URL.

The format is http://<IP Address>:8080/emapp/EMAppServlet?device=#DEVICENAME# . IP Address is the IP address of the Unified Communications Manager where Cisco Extension Mobility is activated and running.

It should be a IPv4 address.

#### Example:

http://123.45.67.89:8080/emapp/EMAppServlet?device=#DEVICENAME#

#### Example:

http://[2001:0001:0001:0067:0000:0000:0000:0134]:8080/emapp/EMAppServlet?device=#DEVICENAME#

This format
                                             				allows a user to sign-in using User ID and PIN. You can configure more sign-in
                                             				options for IP phone users who have subscribed to the extension mobility
                                             				service. To configure more sign-in options, append the loginType parameter to the Service URL, in the
                                             				following formats:

loginType=DN enables users to sign in using Primary Extension and PIN.

The
                                                   					 Service URL format is: http://<IP
                                                      						Address>:8080/emapp/EMAppServlet?device=#DEVICENAME#&loginType=DN .

loginType=SP enables users to sign in using Self Service User ID and PIN.

The
                                                   					 Service URL format is: http://<IP
                                                      						Address>:8080/emapp/EMAppServlet?device=#DEVICENAME#&loginType=SP .

loginType=UID enables users to sign in using User ID and PIN.

The
                                                   					 Service URL format is: http://<IP
                                                      						Address>:8080/emapp/EMAppServlet?device=#DEVICENAME#&loginType=UID .

If you do
                                             				not append loginType to the end of the URL, the default sign-in
                                             				option displayed is User ID and PIN.

Step 5

In the Service Type field, choose whether the service is
                                          			 provisioned to the Services, Directories, or Messages button.

Step 6

Click Save .

### Create an
                           	 Extension Mobility Device Profile for Users

Configure an extension mobility device profile. This profile
                                 				acts as a virtual device that maps onto a physical device when a user logs in
                                 				to extension mobility. The physical device takes on the characteristics in this
                                 				profile.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Device Profile .

Step 2

Perform one
                                          			 of the following tasks:

- Click Find to modify the settings and choose an existing device profile from the resulting list.

- Click Add New to add a new device profile and choose an option from the Device Profile Type . Click Next .

- Choose a device protocol from the Device Protocol drop-down list and click Next .

Step 3

Configure the fields. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

Step 5

From the Association Information section, click Add
                                             				a new DN .

Step 6

In the Directory Number field, enter the directory number
                                          			 and click Save .

Step 7

Click Reset and follow the prompts.

### Associate a Device Profile to a User

Associate a device profile to users so that they can access
                                 				their settings from a different phone. You associate a user device profile to a
                                 				user in the same way that you associate a physical device.

Tip

You can use the Bulk Administration Tool (BAT) to add and delete several user device profiles for Cisco Extension Mobility
                                             at one time. See the Bulk Administration Guide for Cisco Unified Communications Manager .

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an existing user, enter search criteria, and choosing an existing user from the resulting list.

- Click Add New to add a new user.

Step 3

Under Extension Mobility , locate the device profile that you created and move it from Available Profiles to Controlled Profiles .

Step 4

Check the Home Cluster check box.

Step 5

Click Save .

### Subscribe to Extension Mobility

Subscribe IP phones and device profiles to the extension
                                 				mobility service so that users can log in, use, and log out of extension
                                 				mobility.

Step 1

Perform one of the following tasks from Cisco Unified CM Administration:

- Choose Device > Phone , specify search criteria, click Find , and choose a phone which users will use for extension mobility.

- Choose Device > Device Settings > Device Profile , specify search criteria, click Find , and choose the device profile that you created.

Step 2

From the Related Links drop-down list, choose Subscribe/Unsubscribe Services , and then click Go .

Step 3

From the Select a Service drop-down list, choose the Extension Mobility service.

Step 4

Click Next .

Step 5

Click Subscribe .

Step 6

Click Save and close the popup window.

### Configure Roaming for Extension Mobility Users

Use this procedure to give Extension Mobility users the ability to roam between different clusters in an ILS network, while
                                 using the same login credentials. To do this, you must assign the selected users to the Standard EM Roaming Across Clusters Super Users access control group.

#### Before you begin

An ILS network must have been set up as ILS is used to replicate user and login information across the clusters.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > Access Control Group .

Step 2

Click Find and select the Standard EM Roaming Across Clusters Super Users group.

Step 3

Click Add End Users to Group button. The Find and List Users pop-up window appears.

Step 4

Click Find and select all the users to whom you want to provide roaming ability.

Step 5

Click Add Selected .

## Extension Mobility Roaming Across Clusters Interactions and Restrictions

### Extension Mobility Roaming Across Clusters Interactions

This section lists the interactions of the Extension Mobility Roaming across Cluster with other Cisco Unified Communications
                              Manager Administration components.

Extension Mobility

Inter-Cluster Lookup Service (ILS)

### Extension Mobility Roaming Across Clusters Restrictions

This section lists the restrictions of the Extension Mobility Roaming across Cluster with other Cisco Unified Communications
                              Manager Administration components.

If the hub ILS is down, the spokes connected to it will not synchronize until the hub is back.

## Different Types of Extension Mobility

The following table lists the different types of Extension Mobility features available in Cisco Unified Communications Manager
                           and their differences.

Extension Mobility (EM)

Extension Mobility Cross Cluster (EMCC)

Extension Mobility Roaming Across Cluster

Description

Allows users to temporarily access their phone settings from other phones in the same cluster.

Allows users to access their phone settings from a phone in another cluster.

Allows user to roam across other clusters using own login credentials.

When the user logs in to a phone in another cluster

N/A

The remote cluster phone registers to the user’s home cluster, accessing the settings in the home cluster.

The roaming cluster phone registers in the roaming cluster only.

Intercluster

Single cluster only

Multiple clusters

Multiple clusters

Configuration

Single cluster only

EMCC must be configured in the home cluster and each cluster that the user visit.

Extension Mobility Roaming must be configured in all the cluster.

User Information

Single cluster only

Must be maintained in all clusters.

Superuser information maintained in all the cluster.

## Extension Mobility Roaming Across Clusters Troubleshooting

This section provides information about error codes for EMApp and EMService.

### Authentication Error

Problem "Error 201 Authentication Error" appears on the phone.

Solution The user should check that the correct user ID and PIN were entered; the user should check with the system administrator
                                 that the user ID and PIN are correct.

### Blank User ID or PIN

Problem "Error 202 Blank User ID or PIN" appears on the phone.

Solution Enter a valid user ID and PIN.

### Busy Please Try Again

Problem "Error 26 Busy Please Try Again" appears on the phone.

To verify the number of concurrent login and logout
                                                requests, use
                                                the Cisco Unified Real-Time
                                                Monitoring Tool to view the Requests In Progress counter in the
                                                Extension Mobility object. For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

### Database Error

Problem "Error 6 Database Error" appears on the phone.

Solution Check whether a large number of requests exists.  If a large number of requests exists, the Requests In Progress counter
                                 in the Extension Mobility object counter shows a high value. If the requests are rejected because of a large number of concurrent
                                 requests, the Requests Throttled counter also shows a high value.  Collect detailed database logs.

### Dev Logon Disabled

Problem "Error 22 Dev Logon Disabled" appears on the phone.

Solution Verify that you checked the Enable Extension Mobility check box in the Phone Configuration window ( Device > Phone ).

### Device Name Empty

Problem "Error 207 Device Name Empty" appears on the phone.

Solution Check that the URL that is configured
                                 for
                                 Cisco Extension
                                 Mobility is correct. See the Related Topics section for more information.

### EM Service Connection Error

Problem "Error 207 EM Service Connection Error" appears on the phone.

Solution Verify that the Cisco Extension Mobility service is running by selecting Tools > Control Center—Feature in Cisco Unified Serviceability.

### Host Not Found

Problem The "Host Not Found" error message appears on the phone.

Solution Check that the Cisco Tomcat service is running by selecting Tools > Control Center—Network Services in CIsco Unified Serviceability.

### HTTP Error

Problem HTTP Error (503) appears on the phone.

- If you get this error when you press the Services button, check that the Cisco IP Phone Services service is running by selecting Tools > Control Center—Network Services in Cisco Unified Serviceability.

- If you get this error when you select Extension Mobility service, check that the Cisco Extension Mobility Application service
                                       is running by selecting Tools > Control Center—Network Services in Cisco Unified Serviceability.

### Phone Resets

Problem After users log in or log out, their phones reset instead of restarting.

Possible Cause Locale change is the probable cause of the reset.

Solution No action is required. If the user locale that is associated with the logged-in user or profile is not the same as the locale
                                 or device, after a successful login the phone will restart and then reset. This pattern occurs because the phone configuration
                                 file is rebuilt.

### Phone Services Unavailable After Login

Problem After logging in, the user finds that the phone services are not available.

Possible Cause This problem occurs because the user profile had no services associated with it when it was loaded on the phone.

Ensure that the user profile includes the
                                          Cisco Extension
                                          Mobility service.

Change the configuration of the phone where the user is logged in to include Cisco Extension Mobility. After the phone is
                                          updated, the user can access the phone services.

### Phone Services Unavailable After Logout

Problem After a user logs out and the phone reverts to the default device profile, the phone services are no longer available.

Solution Subscribe the phone to the Cisco Extension Mobility service.

### User Logged in Elsewhere

Problem "Error 25 User Logged in Elsewhere" appears on the phone.

Solution Check whether the user is logged in to another phone. If multiple logins must be allowed, ensure that the Multiple Login Behavior service parameter is set to Multiple Logins Allowed .

### User Profile Absent

Problem "Error 205 User Profile Absent" appears on the phone.

Solution Associate a device profile to the user.

| Note | To deploy Extension Mobility Roaming Across Clusters, you must be running a minimum release of Cisco Unified Communications
                                    Manager 12.0(1)SU1. |
|---|---|

| Note | Superuser information must be shared across all the clusters irrespective of the cluster in which the user is logging-in. |
|---|---|

| Note | If a superuser did the Extension Mobility login to another cluster, user will automatically log out from the home cluster.
                                                If the cluster is down, it waits until the cluster is up to log out from the user's previous login. Extension Mobility Roaming Across Clusters supports the multi login behavior. Hence, superuser can login from multiple devices
                                                within the same cluster but not across the clusters. |
|---|---|

| Note | Configuring user as superuser automatically initiates the ILS sync irrespective of Directory Number configuration for ILS. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Generate a report to identify devices that support the Extension Mobility feature. |
| Step 2 | Configure Extension Mobility by completing, the following subtasks in order: | Configure Extension Mobility to allow users to temporarily access their phone settings, such as line appearances, services,
                                          and speed dials, from other phones when they login from remote cluster. Perform this task flow on both home and remote clusters,
                                          so that users will be able to access settings from either a home or remote cluster. |
| Step 3 | Configure Roaming for Extension Mobility Users | Use this procedure to give Extension Mobility users the ability to roam between different clusters in an ILS network, while
                                          using the same login credentials. |

| Step 1 | From Cisco Unified Reporting, choose System Reports . |
|---|---|
| Step 2 | From the list of reports, click Unified CM Phone Feature List . |
| Step 3 | Perform one of the following steps: Choose Generate New Report (the bar chart icon)  to generate a new report. Choose Unified CM Phone Feature List if a report exists. |
| Step 4 | From the Product drop-down list, choose All . |
| Step 5 | Click the name of the feature that you want to configure. |
| Step 6 | Click Submit , to generate the report. |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down list, choose the requried node. |
| Step 3 | Activate the following services: Cisco CallManager Cisco Tftp Cisco Extension Mobility ILS Service Note You must choose publisher node to activate the ILS services. | Note | You must choose publisher node to activate the ILS services. |
| Note | You must choose publisher node to activate the ILS services. |
| Step 4 | Click Save . |
| Step 5 | Click OK . |

| Note | You must choose publisher node to activate the ILS services. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Phone Services . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | In the Service Name field, enter a name for the service. |
| Step 4 | In the Service URL field, enter the Service URL. The format is http://<IP Address>:8080/emapp/EMAppServlet?device=#DEVICENAME# . IP Address is the IP address of the Unified Communications Manager where Cisco Extension Mobility is activated and running. It should be a IPv4 address. Example: http://123.45.67.89:8080/emapp/EMAppServlet?device=#DEVICENAME# Example: http://[2001:0001:0001:0067:0000:0000:0000:0134]:8080/emapp/EMAppServlet?device=#DEVICENAME# This format
                                             				allows a user to sign-in using User ID and PIN. You can configure more sign-in
                                             				options for IP phone users who have subscribed to the extension mobility
                                             				service. To configure more sign-in options, append the loginType parameter to the Service URL, in the
                                             				following formats: loginType=DN enables users to sign in using Primary Extension and PIN. The
                                                   					 Service URL format is: http://<IP
                                                      						Address>:8080/emapp/EMAppServlet?device=#DEVICENAME#&loginType=DN . loginType=SP enables users to sign in using Self Service User ID and PIN. The
                                                   					 Service URL format is: http://<IP
                                                      						Address>:8080/emapp/EMAppServlet?device=#DEVICENAME#&loginType=SP . loginType=UID enables users to sign in using User ID and PIN. The
                                                   					 Service URL format is: http://<IP
                                                      						Address>:8080/emapp/EMAppServlet?device=#DEVICENAME#&loginType=UID . If you do
                                             				not append loginType to the end of the URL, the default sign-in
                                             				option displayed is User ID and PIN. |
| Step 5 | In the Service Type field, choose whether the service is
                                          			 provisioned to the Services, Directories, or Messages button. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Device Profile . |
|---|---|
| Step 2 | Perform one
                                          			 of the following tasks: Click Find to modify the settings and choose an existing device profile from the resulting list. Click Add New to add a new device profile and choose an option from the Device Profile Type . Click Next . Choose a device protocol from the Device Protocol drop-down list and click Next . |
| Step 3 | Configure the fields. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . |
| Step 5 | From the Association Information section, click Add
                                             				a new DN . |
| Step 6 | In the Directory Number field, enter the directory number
                                          			 and click Save . |
| Step 7 | Click Reset and follow the prompts. |

| Tip | You can use the Bulk Administration Tool (BAT) to add and delete several user device profiles for Cisco Extension Mobility
                                             at one time. See the Bulk Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an existing user, enter search criteria, and choosing an existing user from the resulting list. Click Add New to add a new user. |
| Step 3 | Under Extension Mobility , locate the device profile that you created and move it from Available Profiles to Controlled Profiles . |
| Step 4 | Check the Home Cluster check box. |
| Step 5 | Click Save . |

| Step 1 | Perform one of the following tasks from Cisco Unified CM Administration: Choose Device > Phone , specify search criteria, click Find , and choose a phone which users will use for extension mobility. Choose Device > Device Settings > Device Profile , specify search criteria, click Find , and choose the device profile that you created. |
|---|---|
| Step 2 | From the Related Links drop-down list, choose Subscribe/Unsubscribe Services , and then click Go . |
| Step 3 | From the Select a Service drop-down list, choose the Extension Mobility service. |
| Step 4 | Click Next . |
| Step 5 | Click Subscribe . |
| Step 6 | Click Save and close the popup window. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > Access Control Group . |
|---|---|
| Step 2 | Click Find and select the Standard EM Roaming Across Clusters Super Users group. |
| Step 3 | Click Add End Users to Group button. The Find and List Users pop-up window appears. |
| Step 4 | Click Find and select all the users to whom you want to provide roaming ability. |
| Step 5 | Click Add Selected . |

|  | Extension Mobility (EM) | Extension Mobility Cross Cluster (EMCC) | Extension Mobility Roaming Across Cluster |
|---|---|---|---|
| Description | Allows users to temporarily access their phone settings from other phones in the same cluster. | Allows users to access their phone settings from a phone in another cluster. | Allows user to roam across other clusters using own login credentials. |
| When the user logs in to a phone in another cluster | N/A | The remote cluster phone registers to the user’s home cluster, accessing the settings in the home cluster. | The roaming cluster phone registers in the roaming cluster only. |
| Intercluster | Single cluster only | Multiple clusters | Multiple clusters |
| Configuration | Single cluster only | EMCC must be configured in the home cluster and each cluster that the user visit. | Extension Mobility Roaming must be configured in all the cluster. |
| User Information | Single cluster only | Must be maintained in all clusters. | Superuser information maintained in all the cluster. |

| Note | To verify the number of concurrent login and logout
                                                requests, use
                                                the Cisco Unified Real-Time
                                                Monitoring Tool to view the Requests In Progress counter in the
                                                Extension Mobility object. For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html |
|---|---|