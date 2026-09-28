---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-6fd5ae79e5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01010010.html
retrieved_at: 2026-08-16T17:37:26.860574+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Geolocation and Location Conveyance

## Chapter: Configure Geolocation and Location Conveyance

# Configure Geolocation and Location Conveyance

## Geolocation and Location Conveyance Overview

Use Geolocations to define the geographical location (or civic address) of devices that is used in policy decisions, such
                           as whether a call from one phone to another is allowed. The Request for Comments (RFC) 4119 standard provides the basis for
                           geolocations.

Use Location Conveyance to allow communication of geolocation information from one cluster to another, when a call is established
                           and during a call.

## Geolocation and Location Conveyance Task Flow

Step 1

To Configure Geolocations , perform the following subtasks:

Configure geolocations to specify geographic locations. These are used to associate
                                          
                                          devices with regulatory features such as logical
                                          partitioning.
                                          Geolocations are used in policy decisions, such as in-country regulations.

Step 2

To Configure Geolocation Filters , configure the following subtasks:

- Configure a Geolocation Filter

- Assign a Geolocation Filter

- Set the Default Geolocation Filter

Configure geolocation filters to choose which fields are used to create a geolocation identifier. This feature is used to
                                          make policy decisions on a subset of the geolocation objects. Geolocation filters define which of the geolocation objects
                                          should be used when comparing the geolocations of different devices. For example, a group of phones may be assigned identical
                                          geolocations, except for the room and floor in which they are located. Even though the actual geolocations of each phone differ,
                                          the filtered geolocation is the same.

### Configure Geolocations

Step 1

Configure a Geolocation

Configure geolocations to specify geographic locations. These are used to associate
                                             
                                             devices with regulatory features such as logical
                                             partitioning.
                                             Geolocations are used in policy decisions, such as in-country regulations.

Step 2

Assign a Geolocation

Assign a geolocation to a device or device pool.

Step 3

Set the Default Geolocation

Specify a default geolocation for all devices and device pools in this cluster.

Step 4

(Optional) Configure Location Conveyance

Configure location conveyance if you want to communicate geolocation information about devices across clusters.

#### Configure a Geolocation

Configure geolocations to specify geographic locations. These are used to associate
                                    
                                    devices with regulatory features such as logical
                                    partitioning.
                                    Geolocations are used in policy decisions, such as in-country regulations.

Step 1

From Cisco Unified CM Administration, choose System > Geolocation Configuration .

Step 2

Click Add New .

Step 3

Enter a Name for the geolocation.

Step 4

Configure the fields on the Geolocation Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

Step 6

Repeat this procedure to create additional geolocations.

#### Assign a Geolocation

Assign a geolocation to a device or device pool.

Step 1

From Cisco Unified CM Administration, choose one of the following menu items:

- Device > Phone

- Device > Trunk

- Device > Gateway

- System > Device Pool

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an existing device or device pool. Enter search criteria, and then choose an existing device or
                                                device pool from the resulting list.

- Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next .

Step 3

From the Geolocation drop-down list, choose a geolocation that you configured.

Step 4

Click Save .

#### Set the Default Geolocation

Specify a default geolocation for all devices and device pools in this cluster.

##### Before you begin

Assign a Geolocation

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified .

Step 3

Click Save .

Step 4

Click Apply Config .

Step 5

(Optional) If you need to override this default for a specific device or device pool, enter the value on either the Device Configuration or Device Pool Configuration window, and then click Save .

##### What to do next

(Optional) Configure Location Conveyance

Configure Geolocation Filters

#### Configure Location Conveyance

Configure location conveyance if you want to communicate geolocation information about devices across clusters.

##### Before you begin

Configure a Geolocation

Assign a Geolocation

Set the Default Geolocation

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Do one of the following:

- Click Find and select an existing trunk.

- Click Add New to configure a new trunk.

Step 3

Complete the fields in the Trunk Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

In the Geolocation Information area, select a Geolocation and Geolocation Filter .

Step 5

To enable Location Conveyance, check the Send Geolocation Information check box.

Step 6

Click Save .

### Configure Geolocation Filters

Configure geolocation filters to choose which fields are used to create a geolocation identifier. This feature is used to
                                 make policy decisions on a subset of the geolocation objects. Geolocation filters define which of the geolocation objects
                                 should be used when comparing the geolocations of different devices. For example, a group of phones may be assigned identical
                                 geolocations, except for the room and floor in which they are located. Even though the actual geolocations of each phone differ,
                                 the filtered geolocation is the same.

Step 1

Configure a Geolocation Filter

Geolocation filters allow you to specify which fields are used to create a geolocation identifier. This feature is used to
                                             make policy decisions on a subset of the geolocation objects.

Step 2

Assign a Geolocation Filter

Step 3

Set the Default Geolocation Filter

Configure the Default Geolocation Filter enterprise parameter to specify a default geolocation filter for a cluster. This
                                             parameter determines the default
                                             geolocation filter setting for all devices and device pools that are not associated with a geolocation filter.

#### Configure a Geolocation Filter

Geolocation filters allow you to specify which fields are used to create a geolocation identifier. This feature is used to
                                    make policy decisions on a subset of the geolocation objects.

Step 1

From Cisco Unified CM Administration, choose System > Geolocation Filter .

Step 2

Click Add New .

Step 3

Enter a Name and Description for the filter.

Step 4

Check the check boxes that correspond to the items you want to use for logical partitioning decisions.

Step 5

Configure the fields on the Geolocation Filter Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 6

Click Save .

Step 7

Repeat these steps to create additional geolocation filters.

#### Assign a Geolocation Filter

Step 1

From Cisco Unified CM Administration, choose one of the following menu items:

- Device > Phone

- Device > Trunk

- Device > Gateway

- System > Device Pool

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an existing device or device pool. Enter search criteria and then choose an existing device or
                                                device pool from the resulting list.

- Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next .

Step 3

From the Geolocation Filter drop-down list, choose a geolocation filter that you configured.

Step 4

Click Save .

#### Set the Default Geolocation Filter

Configure the Default Geolocation Filter enterprise parameter to specify a default geolocation filter for a cluster. This
                                    parameter determines the default
                                    geolocation filter setting for all devices and device pools that are not associated with a geolocation filter.

##### Before you begin

Assign a Geolocation Filter

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified .

Step 3

Click Save .

Step 4

Click Apply Config .

Step 5

(Optional) If you need to override this default for a specific device or device pool, specify the default geolocation filter value on
                                             either the Device Configuration or Device Pool Configuration window, and then click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | To Configure Geolocations , perform the following subtasks: | Configure geolocations to specify geographic locations. These are used to associate
                                          
                                          devices with regulatory features such as logical
                                          partitioning.
                                          Geolocations are used in policy decisions, such as in-country regulations. |
| Step 2 | To Configure Geolocation Filters , configure the following subtasks: Configure a Geolocation Filter Assign a Geolocation Filter Set the Default Geolocation Filter | Configure geolocation filters to choose which fields are used to create a geolocation identifier. This feature is used to
                                          make policy decisions on a subset of the geolocation objects. Geolocation filters define which of the geolocation objects
                                          should be used when comparing the geolocations of different devices. For example, a group of phones may be assigned identical
                                          geolocations, except for the room and floor in which they are located. Even though the actual geolocations of each phone differ,
                                          the filtered geolocation is the same. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Geolocation | Configure geolocations to specify geographic locations. These are used to associate
                                             
                                             devices with regulatory features such as logical
                                             partitioning.
                                             Geolocations are used in policy decisions, such as in-country regulations. |
| Step 2 | Assign a Geolocation | Assign a geolocation to a device or device pool. |
| Step 3 | Set the Default Geolocation | Specify a default geolocation for all devices and device pools in this cluster. |
| Step 4 | (Optional) Configure Location Conveyance | (Optional) Configure location conveyance if you want to communicate geolocation information about devices across clusters. |

| Step 1 | From Cisco Unified CM Administration, choose System > Geolocation Configuration . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the geolocation. |
| Step 4 | Configure the fields on the Geolocation Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . |
| Step 6 | Repeat this procedure to create additional geolocations. |

| Step 1 | From Cisco Unified CM Administration, choose one of the following menu items: Device > Phone Device > Trunk Device > Gateway System > Device Pool |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an existing device or device pool. Enter search criteria, and then choose an existing device or
                                                device pool from the resulting list. Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next . |
| Step 3 | From the Geolocation drop-down list, choose a geolocation that you configured. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified . |
| Step 3 | Click Save . |
| Step 4 | Click Apply Config . |
| Step 5 | (Optional) If you need to override this default for a specific device or device pool, enter the value on either the Device Configuration or Device Pool Configuration window, and then click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Do one of the following: Click Find and select an existing trunk. Click Add New to configure a new trunk. |
| Step 3 | Complete the fields in the Trunk Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | In the Geolocation Information area, select a Geolocation and Geolocation Filter . |
| Step 5 | To enable Location Conveyance, check the Send Geolocation Information check box. |
| Step 6 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Geolocation Filter | Geolocation filters allow you to specify which fields are used to create a geolocation identifier. This feature is used to
                                             make policy decisions on a subset of the geolocation objects. |
| Step 2 | Assign a Geolocation Filter |  |
| Step 3 | Set the Default Geolocation Filter | Configure the Default Geolocation Filter enterprise parameter to specify a default geolocation filter for a cluster. This
                                             parameter determines the default
                                             geolocation filter setting for all devices and device pools that are not associated with a geolocation filter. |

| Step 1 | From Cisco Unified CM Administration, choose System > Geolocation Filter . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name and Description for the filter. |
| Step 4 | Check the check boxes that correspond to the items you want to use for logical partitioning decisions. |
| Step 5 | Configure the fields on the Geolocation Filter Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 6 | Click Save . |
| Step 7 | Repeat these steps to create additional geolocation filters. |

| Step 1 | From Cisco Unified CM Administration, choose one of the following menu items: Device > Phone Device > Trunk Device > Gateway System > Device Pool |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an existing device or device pool. Enter search criteria and then choose an existing device or
                                                device pool from the resulting list. Click Add New to add a new device or device pool. For devices, choose device types and protocols as needed and click Next . |
| Step 3 | From the Geolocation Filter drop-down list, choose a geolocation filter that you configured. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | From the Default Geolocation drop-down list, choose a Geolocation that you configured. The default value is Unspecified . |
| Step 3 | Click Save . |
| Step 4 | Click Apply Config . |
| Step 5 | (Optional) If you need to override this default for a specific device or device pool, specify the default geolocation filter value on
                                             either the Device Configuration or Device Pool Configuration window, and then click Save . |