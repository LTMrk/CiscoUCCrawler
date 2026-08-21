---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-1-cjab-b-on-prem-deployment-121-cjab-b-on-prem-deployment-121-chap-92e730f731
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_1/cjab_b_on-prem-deployment-121/cjab_b_on-prem-deployment-121_chapter_01000.html
retrieved_at: 2026-08-21T21:15:28.344534+00:00
---

On-Premises Deployment for Cisco Jabber 12.1

# On-Premises Deployment for Cisco Jabber 12.1

Updated: July 17, 2018

Chapter: Configure CTI Service

## Chapter: Configure CTI Service

# Configure CTI Service

## Configure CTI Service Workflow

The CTI Service provides Jabber with the location of the UDS device service. The UDS device service provides Jabber with the
                              devices that are associated with the user, for example: a softphone or deskphone devices.

Add a CTI Service

Create a CTI UC service to provide Jabber with the location of the CTI service.

Apply a CTI Service

Apply the CTI UC service to the service profile.

## Add a CTI Service

The CTI service provides Jabber with the address of the UDS device service. The UDS device service provides a list of devices
                              associated with the user.

Open the Cisco Unified CM Administration interface.

Select User Management > User Settings > UC Service .

The Find and List UC Services window opens.

Select Add New .

The UC Service Configuration window opens.

In the Add a UC Service section, select CTI from the UC Service Type drop-down list.

Select Next .

Provide details for the CTI service as follows:

Specify a name for the service in the Name field.

The name you specify displays when you add services to profiles. Ensure the name you specify is unique, meaningful, and easy
                                                to identify.

Specify the CTI service address in the Host Name/IP Address field.

Enter the address in the form of a hostname, IP address, or fully qualified domain name (FQDN). This value corresponds to
                                                the Unified CM publisher that's running the CTI Manager service. You'll create a second service for the subscriber.

Specify the port number for the CTI service in the Port field.

Select Save .

### What to do next

Create a second CTI service for the Unified CM subscriber.

Add the CTI service to your service profile.

### Apply a CTI Service

After you add a CTI service on Cisco Unified
                                    				  Communications Manager , you must apply it to a service profile so that the client can retrieve the settings.

#### Before you begin

Create a service profile if none already exists or if you require a separate service profile for CTI.

Add CTI services for the Unified CM publisher and subscriber.

Open the Cisco Unified CM Administration interface.

Select User Management > User Settings > Service Profile .

Find and select your service profile.

Navigate to CTI Profile section, and select up to three services from the following drop-down lists:

Primary

Secondary

Tertiary

Select Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a CTI Service | Create a CTI UC service to provide Jabber with the location of the CTI service. |
| Step 2 | Apply a CTI Service | Apply the CTI UC service to the service profile. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > UC Service . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The UC Service Configuration window opens. |
| Step 4 | In the Add a UC Service section, select CTI from the UC Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide details for the CTI service as follows: Specify a name for the service in the Name field. The name you specify displays when you add services to profiles. Ensure the name you specify is unique, meaningful, and easy
                                                to identify. Specify the CTI service address in the Host Name/IP Address field. Enter the address in the form of a hostname, IP address, or fully qualified domain name (FQDN). This value corresponds to
                                                the Unified CM publisher that's running the CTI Manager service. You'll create a second service for the subscriber. Specify the port number for the CTI service in the Port field. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. Service Profile Configuration window opens. |
| Step 4 | Navigate to CTI Profile section, and select up to three services from the following drop-down lists: Primary Secondary Tertiary |
| Step 5 | Select Save . |