---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-15-english-administration-guide-cer0-b-cisco-emergency-responder-adminis-af6a6dde93
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/15/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-15/cer0_b_cisco-emergency-responder-administration-guide-1251su3_chapter_01010.html
retrieved_at: 2026-08-21T15:02:11.349875+00:00
---

Cisco Emergency Responder Administration Guide, Release 15 and SUs

# Cisco Emergency Responder Administration Guide, Release 15 and SUs

Updated: March 17, 2026

Chapter: Configure Switch Refresh Utility

## Chapter: Configure Switch Refresh Utility

# Configure Switch Refresh Utility

## Switch Refresh Utility Overview

The Switch Refresh Utility feature helps ease migration of old switch models to newer switch models with minimal change in
                           Cisco Emergency Responder. This feature allows you to save the old switch model configuration details which can be uploaded
                           to your new switch configuration after discovery of the new switch.

As part of this feature, the following functionalities are introduced:

Save Switch Config —The Save Switch Port Configuration page allows you to select and save the switch configuration details of an older switch
                                 in a CSV data file in your Cisco Emergency Responder system. You may download, review, and modify the csv file if needed.

Upload Switch Config —The Upload Switch Configuration page allows you to upload the saved switch CSV file to the new switch after it is physically
                                 replaced and discovered in Cisco Emergency Responder.

The functionality of Save Switch Config or Upload Switch Config is mainly for scenario of switch refresh where the IP address of the old switch and the new switch is the same. If the IP
                           address of the new switch is different, you should perform an export switch functionality on the Switch Port Page. The Save
                           Switch Config data may include the assigned ERL Name, Switch IP Address, IfName, Location, Port Name, Switch HostName, Port
                           Identifier, Port Description, and Index details.

For more information on Save Switch Config and Upload Switch Config configuration pages, see Save Switch Port Configuration and Upload Switch Port Configuration . You can also view details of all the saved CSV data files in the File Management Utility page.

We recommend that you replace minimal number of switches at a time using the switch refresh utility method. If you have a
                                       large network, you can replace up to 50 switches at a time.

## Save Switch Configuration

Use the Switch Port Details page to save the switch port configuration details.

Step 1

From Cisco ER Administration, navigate to ERL Membership > Switch Ports to view the list of switches.

Step 2

In the Switch Port Search Parameters, click Find .

Step 3

Select the IP address of the switches which are going to be refreshed.

Step 4

Click Save Switch Config .

The Save Switch Port Configuration page displays.

Step 5

From the Select Save Config Format drop-down list, choose the CSV format.

Step 6

In the Enter Save Config File name option, enter the name of the file you want to save with.

Step 7

Click Save Config to create and save the file.

Step 8

Use the Download drop-down menu to select a file and download a copy to your local system.

## Physical Refresh of Switch and Full Discovery in Emergency Responder

Step 1

To run full discovery (phone tracking), select Phone Tracking > Run Switch-Port & Phone Update .

Step 2

Navigate to ERL Membership > Switch Ports . Check for the timestamp mentioned in the Switch Port Details page which is updated once full discovery is complete.

Step 3

Verify the new switch details and then perform the Upload Switch Config functionality.

## Upload Switch Configuration

After uploading the CSV file, the current configuration data will be overwritten and the saved ERL, Port, Location, and IP
                              Address details will be added to the new switch.

The saved switch config details will be uploaded to the respective ports on the new switch. Any differential ports must be
                                          assigned manually by the administrator.

### Before you begin

Step 1

From Cisco ER Administration, navigate to ERL Membership > Switch Ports to view the list of new switches added.

Step 2

Click Upload Switch Config .

The Upload Switch Port Configuration page displays.

Step 3

From the Select Upload config File Format drop-down list, choose the CSV format.

Step 4

From the Select File to Upload Config drop-down list, select the file to be uploaded.

Step 5

Click Upload .

You can view the status of the upload in the Status box.

| Note | We recommend that you replace minimal number of switches at a time using the switch refresh utility method. If you have a
                                       large network, you can replace up to 50 switches at a time. |
|---|---|

| Step 1 | From Cisco ER Administration, navigate to ERL Membership > Switch Ports to view the list of switches. |
|---|---|
| Step 2 | In the Switch Port Search Parameters, click Find . |
| Step 3 | Select the IP address of the switches which are going to be refreshed. |
| Step 4 | Click Save Switch Config . The Save Switch Port Configuration page displays. |
| Step 5 | From the Select Save Config Format drop-down list, choose the CSV format. |
| Step 6 | In the Enter Save Config File name option, enter the name of the file you want to save with. |
| Step 7 | Click Save Config to create and save the file. |
| Step 8 | Use the Download drop-down menu to select a file and download a copy to your local system. |

| Step 1 | To run full discovery (phone tracking), select Phone Tracking > Run Switch-Port & Phone Update . |
|---|---|
| Step 2 | Navigate to ERL Membership > Switch Ports . Check for the timestamp mentioned in the Switch Port Details page which is updated once full discovery is complete. |
| Step 3 | Verify the new switch details and then perform the Upload Switch Config functionality. |

| Note | The saved switch config details will be uploaded to the respective ports on the new switch. Any differential ports must be
                                          assigned manually by the administrator. |
|---|---|

| Step 1 | From Cisco ER Administration, navigate to ERL Membership > Switch Ports to view the list of new switches added. |
|---|---|
| Step 2 | Click Upload Switch Config . The Upload Switch Port Configuration page displays. |
| Step 3 | From the Select Upload config File Format drop-down list, choose the CSV format. |
| Step 4 | From the Select File to Upload Config drop-down list, select the file to be uploaded. |
| Step 5 | Click Upload . You can view the status of the upload in the Status box. |