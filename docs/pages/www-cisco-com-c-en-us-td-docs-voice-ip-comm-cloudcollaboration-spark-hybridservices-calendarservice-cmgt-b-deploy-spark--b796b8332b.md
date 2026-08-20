---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--b796b8332b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_appendix_01011.html
retrieved_at: 2026-08-20T23:54:15.238886+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: October 17, 2023

Chapter: Troubleshoot Hybrid Calendar

## Chapter: Troubleshoot Hybrid Calendar

# Troubleshoot Hybrid Calendar

## Diagnostic tools on Expressway-C connector host

Use these diagnostic tools to investigate a problem with Hybrid Services connectors that are installed on the Expressway-C .

Access the Webex Hybrid Services log levels and enable debug mode if instructed to do so by support. Go to Maintenance > Diagnostics > Hybrid Services Log Levels .

Check the event log for errors and warnings. Go to Status > Logs > Event Log .

Check for related alarms on Status > Alarms . Alarms that are related to Hybrid Services are tagged [Hybrid Services] and have IDs in the 60000–69999 range. You can also see these alarms in Control Hub ( https://admin.webex.com ).

Run diagnostic logging while you recreate the issue, and take a tcpdump during that period. Go to Maintenance > Diagnostics > Diagnostic logging and read the online help for more details.

Take a system snapshot to provide to support for diagnosis. Go to Maintenance > Diagnostics > System snapshot .

Configure syslog if you have remote logging servers. Go to Maintenance > Logging .

Configure incident reporting so that any Expressway failures are automatically reported to us. Go to Maintenance > Diagnostics > Incident reporting > Configuration .

For more details, read the Cisco Expressway Serviceability Guide , or search the help on the Expressway .

## Check connector health on Expressway-C

When you're having a problem with Hybrid Services , you can check the status of the connectors and restart any stopped connectors.

### Before you begin

If a connector is stopped, you can open a ticket with support and send a log first before you restart the connector.

Step 1

On the Expressway-C , go to Applications > Hybrid Services > Connector Management to check the status of your connectors.

The Connector Management section shows all the installed connectors, their version numbers and their status.

Step 2

If a connector is Stopped , click the name of that connector.

You'll see a more detailed status page with a Restart button.

Step 3

Click Restart .

### What to do next

If the restart generates an alarm, or if the connector stops again, try the following:

Follow the guidance on the alarm. You can also see these alarms in Control Hub ( https://admin.webex.com ).

From the customer view in https://admin.webex.com , click your username, and then click Feedback to open a ticket and send logs.

Use the diagnostic tools to look for problem signatures.

Roll back to the previous version of the connector (try this if the problem started after a connector upgrade).

## Roll back to the previous version of a connector

Under normal conditions, your Expressway-C upgrades your connectors automatically after you choose to upgrade in Control Hub or set a scheduled upgrade time. You can roll back to the previous version of a connector if something goes wrong with an
                              upgraded connector.

Step 1

On the Expressway-C , go to Applications > Hybrid Services > Connector Management to check the health status of your connectors.

The Connector Management section shows all the installed connectors, their version numbers, and their status.

Step 2

Click the name of the connector.

A more detailed status page shows the currently installed version and the version that you can roll back to. The page also
                                          shows any versions that you previously rejected (by rolling back from them).

Step 3

Click Roll back to reject the currently installed version, and replace it with the Target version .

The page displays the formerly installed version number in the Rejected version field, which means that the will not allow that version to install itself in future.

If you click Back to connector list , you can see the previous version is now running. An alarm is raised because you rejected an upgrade. You can safely ignore
                                          that alarm; it appears because of your choice, and it is lowered when a newer version is installed.

When a newer version is available on Webex , the automatic upgrade resumes.

Step 4

To reverse your decision and accept the Rejected version , click Allow this upgrade .

## Troubleshoot the Join button

### No Join button on premises-registered devices

Problem In a hybrid Exchange environment, the Join button does not appear on any premises-registered device.

Possible Cause In hybrid Exchange environments, disabling TNEF for remote domains causes Exchange Online to strip the TMS:ExternalConferenceData
                              and UCCapabilities user attributes for the meeting. This breaks OBTP for Unified CM-registered endpoints. Without these attributes,
                              Cisco TMSXE cannot update the meeting in Cisco TMS, and Cisco TMS cannot set the OBTP dial string for the meeting.

Solution To fix this condition, verify that TNEF is allowed for remote domains. For instructions, see https://docs.microsoft.com/en-us/exchange/mail-flow/content-conversion/tnef-conversion .

### No Join button on a specific device

Problem A device does not show the join button when meetings are about to start.

Possible Cause The device does not automatically accept meeting invitations.

Solution Check the resource calendar for the device, and see if it has accepted the meeting invitation. If not, configure the device's
                              resource mailbox to automatically accept meeting requests.

| Step 1 | On the Expressway-C , go to Applications > Hybrid Services > Connector Management to check the status of your connectors. The Connector Management section shows all the installed connectors, their version numbers and their status. |
|---|---|
| Step 2 | If a connector is Stopped , click the name of that connector. You'll see a more detailed status page with a Restart button. |
| Step 3 | Click Restart . |

| Step 1 | On the Expressway-C , go to Applications > Hybrid Services > Connector Management to check the health status of your connectors. The Connector Management section shows all the installed connectors, their version numbers, and their status. |
|---|---|
| Step 2 | Click the name of the connector. A more detailed status page shows the currently installed version and the version that you can roll back to. The page also
                                          shows any versions that you previously rejected (by rolling back from them). |
| Step 3 | Click Roll back to reject the currently installed version, and replace it with the Target version . The page displays the formerly installed version number in the Rejected version field, which means that the will not allow that version to install itself in future. If you click Back to connector list , you can see the previous version is now running. An alarm is raised because you rejected an upgrade. You can safely ignore
                                          that alarm; it appears because of your choice, and it is lowered when a newer version is installed. When a newer version is available on Webex , the automatic upgrade resumes. |
| Step 4 | To reverse your decision and accept the Rejected version , click Allow this upgrade . |