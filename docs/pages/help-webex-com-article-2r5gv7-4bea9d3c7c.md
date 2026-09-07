---
doc_id: help-webex-com-article-2r5gv7-4bea9d3c7c
source_url: https://help.webex.com/article/2r5gv7
retrieved_at: 2026-09-07T10:36:27.837031+00:00
---

### Video Mesh Analytics

Analytics provide information about how you use your on-premises Video Mesh nodes and clusters in your Webex organization. With the historical data in the metrics view, you can more effectively manage your Video Mesh resources by monitoring the capacity, utilization, and availability of your on-premises resources. You can use this information to make decisions about adding more Video Mesh nodes to a cluster or creating new clusters, for example. Video Mesh analytics can be found in Control Hub under Analytics > Video Mesh .

To help with analyzing the data in your organization, you can zoom in on data that appears on the graph and isolate a specific time period. For Analytics, you can also slice and dice reports to show more granular details.

Video Mesh analytics and troubleshooting reports show data in the time zone that is set for the local browser.

#### Analytics

Video Mesh analytics provide a long-term trend (up to 3 months of data) in the categories of engagement, resource usage, and bandwidth usage.

#### Live Monitoring

The live monitoring tab provides a near-realtime view of activity in your organization: up to 1 minute aggregation and the ability to view the last 4 hours or 24 hours on all clusters or specific clusters. This tab in Control Hub is automatically refreshed—every 1 minute for the last 4 hours and every 10 minutes for the last 24 hours.

#### Access, Filter, and Save Video Mesh Live Monitoring Reports

Video Mesh live monitoring reports are available on the Troubleshooting page of Control Hub ( https://admin.webex.com ), once Video Mesh is active and has a cluster with at least one registered Video Mesh node.

From the customer view in https://admin.webex.com , choose Analytics , and then click Video Mesh on the upper-right side of the screen.

Hover over info to get a short description of the chart.

From the toggle on the left, choose an option to filter on how far back in time you want to show data.

Last 4 Hours (Default)—When you choose this option, the graph data refreshes every 1 minute.

Last 24 Hours —When you choose this option, the graph data refreshes every 10 minutes.

Interact with the charts by using the following options as needed:

Hover over segments on the chart view to view information about that specific data point.

When a filter is applied, all other graphs and charts are updated to display the data of the selected filter.

On a graph that shows data in a time range, narrow down to a specific time range by clicking on the left and dragging your mouse to the right. (This action affects all the related data that appears on the analytics page.)

Hover over sections of a donut, lines on a graph, or insight points on a graph to view more information on the specific point in time of the data.

After you've filtered data in the reports, click more , and then choose a file format option, which saves a local copy of the report so you can use it offline (for example, in an internally created report):

PNG

PDF

CSV

#### Access, Filter, and Save Video Mesh Analytics

Video Mesh metric reports are available on the Analytics page of Control Hub ( https://admin.webex.com ), once Video Mesh is active and has a cluster with at least one registered Video Mesh node.

From the customer view in https://admin.webex.com , choose Analytics , and then click Video Mesh on the upper-right side of the screen.

Click a category, depending on the type of data you're looking for:

- Engagement

- Resources

- Bandwidth Usage

Hover over info to get a short description of the chart.

From the drop-down on the right, choose an option to fìlter on how far back in time you want to show data.

Last 7 Days (Default)—Changes the horizontal axis to every 1 hour.

Last 24 Hours —Changes the horizontal axis to every 10 minutes.

Last 30 Days —Changes the horizontal axis to every 3 hours.

Last 90 Days —Changes the horizontal axis to every 8 hours.

Interact with the charts or donut graphs by using the following options as needed:

When a filter is applied, all other graphs and charts are updated to display the data of the selected filter.

On a graph that shows data in a time range, narrow down to a specific time range by clicking on the left and dragging your mouse to the right and leaving when the desired range is selected. (This action affects all the related data that appears on the analytics page.)

Hover over sections of a donut, lines on a graph, or insight points on a graph to view more information on the specific point in time of the data.

To start over from within the same graph or overview, click X on the selected filters at the bottom of the graph.

After you've filtered data in the reports, click more , and then choose a file format option, which saves a local copy of the report so you can use it offline (for example, in an internally created report):

PDF

PNG

CSV

Clear all the filters from the filters bar if you'd like to reset the analytics view.

#### Available analytics for Video Mesh

For details of the available analytics in Control Hub, see the Video Mesh section of Analytics for Your Cloud Collaboration Portfolio .

### Monitoring Tool for Video Mesh

The Monitoring tool in Control Hub helps your organization in monitoring the health of your Video Mesh deployment. You can run the following tests on your Video Mesh nodes, clusters, or both to get results for specific parameters.

Signaling Test - Tests whether SIP signaling and media signaling occurs between the Video Mesh node and Webex cloud media services.

Cascade Test - Tests whether a cascade can be established between the Video Mesh node and Webex cloud media services.

Reachability Test - Tests whether the Video Mesh node can reach the destination ports for media streams in Webex cloud media services. It also tests if the Video Mesh node is able to communicate with the cloud clusters associated with media containers through those ports.

When you run a test, the tool creates a simulated meeting. After the test finishes, you see a simple pass or fail result with inline troubleshooting tips in the report. You can schedule the test to run periodically or run the test on demand. For more information, see Media Health Monitoring for Video Mesh .

#### Run an immediate test

Use this procedure to run an on-demand media health monitoring and reachability test on Video Mesh nodes and/or clusters registered to your Control Hub organization. The results are captured in Control Hub and are aggregated every 6 hours starting at 00:00 UTC.

Log in to Control Hub , then go to Troubleshooting > Video Mesh .

Click on Configure Test , click Test now , then check the nodes and/or clusters you want to test.

If you want to clear the boxes you've checked and restore your last configuration, click Restore last test configuration .

Click Run test .

What to do next

The results appear in the monitoring tool overview page in Control Hub. By default, results of all the tests are displayed together. Click on Signalling , Cascade , or Reachability to filter the results according to the specific test.

The points on the timeline with slider show aggregated test results for the entire organization. The cluster-level timelines show aggregated results for each cluster.

The timeline might display dates in the US format. Change your language in the profile settings to view dates in your local format.

Hover over the points on the timelines to see the test results. You can also see detailed test results for each node. Click on a point on the cluster-level timeline to view detailed results.

The results are displayed in a side panel and split into Signaling, Cascasde and Reachabilty. You can view whether the test was a success, if it was skipped, or if the test failed. Error codes with possible fixes are also displayed with the results.

Use the toggle provided to view the success rates of various parameters in the form of a table.

A skipped test, partial failure, or failure is not critical unless it occurs continuously over a period of time.

#### Configure periodic tests

Use this procedure to configure and start periodic media health monitoring and reachability tests. These tests run every 6 hours by default. You can run these tests at cluster-wide, cluster-specific, or node-specific levels. The results are captured in Control Hub and are aggregated every 6 hours starting at 00:00 UTC.

Log in to Control Hub , then go to Troubleshooting > Video Mesh .

Click on Configure Test , click Periodic test , then check the nodes and/or clusters you want to test.

Choose an option:

- Check All Clusters if you want to run the test on all the Video Mesh nodes in  your Control Hub organization.

Check the individual cluster names to run the test on all Video Mesh nodes that are in a specific cluster. Unchecked clusters are excluded from the test.

Within individual clusters, check the individual node names that you want to run the test on. Any unchecked node is excluded from the test.

Click Next .

Review the list of clusters and nodes to run the periodic tests. If you are satisfied, click Configure to schedule the current configuration.

What to do next

The results appear in the monitoring tool overview page in Control Hub. By default, results of all the tests are displayed together. Click on Signalling , Cascade , or Reachability to filter the results according to the specific test.

The points on the timeline with slider show aggregated test results for the entire organization. The cluster-level timelines show aggregated results for each cluster.

The timeline might display dates in the US format. Change your language in the profile settings to view dates in your local format.

Hover over the points on the timelines to see the test results. You can also see detailed test results for each node. Click on a point on the cluster-level timeline to view detailed results.

The results are displayed in a side panel and split into Signaling, Cascasde and Reachabilty. You can view whether the test was a success, if it was skipped, or if the test failed. Error codes with possible fixes are also displayed with the results.

Use the toggle provided to view the success rates of various parameters in the form of a table.

A skipped test, partial failure, or failure is not critical unless it occurs continuously over a period of time.

### Enable 1080p HD Video for On-Premises SIP Devices in Video Mesh Node Meetings

This setting allows your organization to favor 1080p high-definition video for on-premises registered SIP endpoints, with a trade off of lower meeting capacity. A Video Mesh Node must host the meeting. Participants can use 1080p 30fps video provided that:

They're all inside the corporate network.

They're using an on-premises registered high definition-capable SIP device.

The setting applies to all clusters that contain Video Mesh nodes.

Cloud-registered devices continue to send and receive 1080p streams, regardless of this setting being turned on or off.

From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click Settings on the Video Mesh card.

Toggle on Video Quality .

If this setting is off, the default is 720p.

For video resolutions that the Webex App supports, see Video Specifications for Calls and Meetings .

### Inter-Cluster Cascades

The architecture used at present for Webex meetings follows a hub and spoke design with Webex cloud as the hub and the on-premises Video Mesh clusters acting as the spokes. If you have two Video Mesh nodes in two separate data centers (EU and NA, for example), and you have endpoints joining through each data center to the same Webex meeting, the Video Mesh nodes in each data center would cascade to the cloud. These cascades would go over the internet or the Edge Connect link to Webex.

The Inter-Cluster Cascade feature intends to improve call quality and bandwidth utilization by enabling direct cascades between Video Mesh clusters of an organization. In the scenario described above, if the organization has the Inter-Cluster Cascade feature enabled, a cascade would be established between Video Mesh nodes of the EU and NA data centers instead of cascading to cloud. In this scenario since all participants are on the organization’s network, there is not a need to cascade each Video Mesh cluster to Webex.

This would lead to significant advantages like:

- Better media and call quality

- Improved bandwidth utilization

- Reduced latency

Requirements:

Ensure WAN bandwidth of at least 20 Mbps between Video Mesh clusters before enabling Inter-Cluster Cascades.

- All clusters in the organization must have more than one node.

#### Call scenarios for Inter-Cluster Cascades

Detailed below are a few scenarios of how Inter-Cluster Cascades would work in different contexts. The scenarios consider an organization with Video Mesh clusters in San Jose and Bangalore. It explores one-to-one calls and Webex meetings before and after enabling Inter-Cluster Cascades. Cascades are established between Video Mesh clusters on-premises or cloud, depending on whether the participants are joining from on-premises devices or the cloud.

##### One-to-one calls:

At present, a one-to-one call would have two cascades to the cloud to make the call possible. With Inter-Cluster Cascades enabled, it would lead to a cascade being established from San Jose to Bangalore directly, eliminating the need to cascade to the cloud.

##### Webex meetings:

In a Webex meeting without Inter-Cluster Cascades, the on-premises Video Mesh clusters would cascade to their respective regional cloud media clusters, which then combine to form the meeting. Enabling Inter-Cluster Cascades would result in a single cascade to the cloud.

The selection of the on-premises Video Mesh cluster that initiates the cascade to the cloud will be determined by the first participant to join the meeting. The Video Mesh cluster used by the first participant will establish the connection to Webex.

#### Enabling Inter-Cluster Cascades

Follow the steps below to enable Inter-Cluster Cascades for your organization:

Log in to Control Hub .

Click Hybrid on the lower left side of the screen.

Click Edit Settings on the Video Mesh card.

Scroll down to Inter-Cluster Cascade . The toggle will be disabled by default. Click on the toggle to enable it.

#### Selecting clusters to participate in Inter-Cluster Cascades

If your Video Mesh deployment has certain clusters with low WAN connectivity or low resources, you can exclude those clusters from participating in Inter-Cluster Cascades. To exclude such clusters, follow the steps below:

Enable Inter-Cluster Cascades as detailed in the previous section.

Once enabled, all clusters of your organization will be listed in the Inter-Cluster Cascade card with a check mark next to them.

Exclude a cluster by deselecting the check mark next to it.

By default, all clusters of your Video Mesh deployment will be selected to participate in Inter-Cluster cascades.

#### Monitoring Inter-Cluster Cascades

You can monitor Inter-Cluster Cascade data across your Video Mesh deployment from the Analytics section of Control Hub . Use the steps below to access, filter and save Inter-Cluster Cascade reports.

Log in to Control Hub .

Click Analytics> Video Mesh .

Click on the Bandwidth Usage tab. You will find Inter-Cluster Cascade reports nested under this tab.

Use the drop-down menus to select the two clusters between which Inter-Cluster Cascade data is needed. It is set All Clusters to All Clusters by default.

From the drop-down on the right, choose an option to fìlter on how far back in time you want to show data.

Last 7 Days (Default)—Changes the horizontal axis to every 1 hour.

Last 24 Hours —Changes the horizontal axis to every 10 minutes.

Last 30 Days —Changes the horizontal axis to every 3 hours.

Last 90 Days —Changes the horizontal axis to every 8 hours.

On a graph that shows data in a time range, narrow down to a specific time range by clicking on the left and dragging your mouse to the right and leaving when the desired range is selected. (This action affects all the related data that appears on the page.)

Click one or more segments on the donut graph or chart view and then click Apply to update the donut view and the corresponding chart view. (For example, you can click on Video on the Total cascaded data usage by stream chart to view data used by video stream during cascades between the selected clusters.)

Hover over sections of a donut, lines on a graph, or insight points on a graph to view more information on the specific point in time of the data.

To start over from within the same graph or overview, click X on the selected filters at the bottom of the graph.

After you've filtered data in the reports, click more , and then choose a file format option, which saves a local copy of the report so you can use it offline (for example, in an internally created report):

PDF

PNG

CSV

Clear all the filters from the filters bar if you'd like to reset the analytics view.

### On-premises recording on Video Mesh

On-premises recording on Video Mesh combines the convenience of recording a Webex meeting with the enhanced security of storing all recorded content on-premises, within the customer's data centers. There are no restrictions on the duration for which recorded content may remain on-premises, allowing customers the flexibility to establish their own retention policies.

#### Prerequisites for On-premises recording on Video Mesh

- This feature is supported only on VMNLite nodes. Additionally, a cluster used for on-premises recording must contain at least one non-recording node, which can be either a VMNLite or a VMNFull. The recording node is dedicated exclusively to recording functionality, whereas the non-recording node is responsible for tasks such as media processing.

For customers with existing VMN deployments, ensure that the storage capacity of the recording nodes is increased from 80 GB to 250 GB. Note that this operation is non-reversible.

To expand storage, place the node in maintenance mode . Open the node console interface using the VMware vSphere client. Shutdown the node and expand its storage to at least 250 GB, then restart the node. Once this is done, disable maintenance mode in Control Hub.

Kerberos authentication for NFS storage is not supported. Mounting more than one NFS server in a Video Mesh deployment is not supported.

For Linux NFS servers:

- The NFS server must have a user with UID: 1044 and GID: 1044. This user must also have write access to the folder where the recorded content will be stored.

```
<path to NFS folder>   *(rw,nohide,all_squash,anonuid=1044,anongid=1044)
```

For Windows NFS servers:

- Ensure that the Share Permissions of the server is set to Read/Write for all machines. Change the access type from Read Only to Read/Write via the Server Manager or using PowerShell.

- Server certificates signed by a trusted CA (Certificate Authority).

For Video Mesh deployments with a large user base, we recommend provisioning 10 Gbps Ethernet NICs to accommodate bandwidth requirements.

#### Recording capacity for Video Mesh nodes

The following table shows the recording and call capacity of a 2-node cluster, where one node is dedicated to recording and the other is a standard VMNLite node (23 vCPUs).

The table above shows the minimum required configuration for on-premises recording to function properly. You can deploy as many nodes and clusters as needed to meet your deployment requirements.

Follow the steps below in the specified order before enabling On-premises recording for your organization.

#### Install Server certificate on the Video Mesh node

The server certificate signed by your trusted CA must be installed on all Video Mesh recording nodes in the cluster or clusters used for recording.

Log in to Control Hub .

Click Hybrid on the lower left side of the screen.

Click View all under Resources in the Video Mesh card.

The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster which you have chosen to handle On-premises Recording.

A page opens with the list of nodes under the cluster you selected. Click on the right end of a recording node and click Go to node .

Go to Server Certificates tab,  generate a CSR (optional), and upload a certificate and private key pair as needed:

(Optional) If you need a certificate issued from a Certificate Authority (CA), click Create a Certificate Signing Request . Fill out the required information (including the Subject Alternative Name(s) , which are FQDNs that must contain the common name, and then generate the request. Download the CSR to submit the request to the CA.

The common name is not a URL. It doesn’t include any protocol (for example http:// or https://), port number, or path name.

When you generate a Certificate Signing Request (CSR), Video Mesh creates and stores the private key automatically. If you don't use the CSR creation step, you must upload a private key manually.

When you have the certificate and private key, click Upload a Server Certificate (.crt or .pem file) and choose the certificate file.

Ensure that you install the complete certificate chain, including the root, all intermediate, and server certificates.

Click Upload a Private Key (.key file) and enter a passphrase if you have one.

After you get the certificate,  click Install Server Certificate , read the prompt, click Install , then click OK .

A cloud-registered Video Mesh node gracefully shuts down, waiting up to 2 hours for any calls to end. The node then completes the certificate installation. A prompt appears when the server certificate installs. You can then reload the page to view the new certificate and key entry.

Click Download next to the certificate and key files to save a local copy.

Save the files somewhere that's easy to remember and leave the Video Mesh instance open in the browser tab.

Repeat the process for all recording nodes in the cluster.

#### Configure NFS storage

Log in to Control Hub .

Click Hybrid on the lower left side of the screen.

Click View all under Resources in the Video Mesh card.

The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster which you have chosen to handle On-Premises Recording.

A page opens with the list of nodes under the cluster you selected. Click on the right end of a node and click Go to node .

The node web interface opens. Click Administration on the left side of the screen.

Scroll down to NFS Setup .

Click Enable NFS .

Enter NFS host and path details in the fields that appear.

Click Mount NFS .

A pop up message appears saying Successfully mounted the given NFS .

Repeat this process for nodes designated for recording in the cluster or clusters.

What to do next

Enable On-Premises Recording for the cluster or clusters in Control Hub.

#### Configure Video Mesh cluster for On-premises recording

Log in to Control Hub .

Click Hybrid on the lower left side of the screen.

Click View all under Resources in the Video Mesh card.

The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster you have selected to handle On-Premises Recording.

Click on the Cluster Settings tab.

On the On-premises recording card, you will find the Allow on-premises recording toggle. The toggle will be disabled by default. Click on the toggle to enable it.

Enter the FQDN or hostname in the Recording Service name field. This will be used to download the recorded content from the nodes.

Ensure that the FQDN entered in Recording Service name has a DNS entry with the IPs of the Video Mesh nodes used for recording. We recommend a round robin method to determine the node that will download the recorded content.

Select the nodes to be used for recording from the drop-down in the On-premises recording nodes field.

#### Enable On-premises recording

The procedures below outline the steps for enabling On-premises recording for specific users, a subset of users, or the entire organization. Follow the procedure that is most appropriate for your use case.

##### Enable On-premises recording for specific users

Log in to Control Hub .

Click Users on the left side of the screen.

Click the user for whom you want to enable On-Premises recording.

On the page that appears, click the Meetings tab.

Scroll down to the Meeting recording card.

Select On-premises recording and click Save .

##### Enable On-premises recording for a subset of users

Enable On-premises recording for a subset of users by creating a group with the users, creating a template and configuring the template with On-premises recording.

Log in to Control Hub .

Click Groups on the left side of the screen.

Click Create a group .

- Follow the instructions on the screen to create a group.

Once the group is created, click Meeting under Services section on the left side of the screen.

Click the Templates tab and click Create template .

Enter a name for the template and scroll down to the Meeting recording card.

Select On-premises recording on the Meeting recording card and click Create template and next .

On the page that appears, select the group that was created earlier and click Done .

##### Enable On-premises recording for the organization

Log in to Control Hub .

Click Meeting on the left side of the screen.

On the page that appears, click on the Settings tab.

Scroll down to the Recording section and click On-premises recording in the list of options.

The on-premises recording option will be greyed out by default and will only become functional once all setup processes detailed in the prerequisites have been completed.

At any given time, either on-premises recording or cloud recording can be enabled for an organization; both cannot be enabled simultaneously.

Click Save at the bottom of the screen.

#### Leverage On-premises Recording in your meetings and download the generated file

Schedule a meeting on Webex.

Once the meeting starts, click on the Record button.

If on-premises recording has been successfully enabled, you will find the Save to my org option in the Recording options drop down.

You can pause, resume and stop the recording as needed.

Once the meeting ends, the host will receive an email with a link and password.

Click on the link in the email, a web page opens in your browser with a field to enter the password.

Copy the password from the email and paste it in the Password field. Click Download . This will trigger the download of the recording file.

Recordings generated through on-premises recording are currently unavailable in the Webex app and can only be accessed using the link provided in the email or from the Video Mesh node web interface.

#### View and manage the list of recordings in the Video Mesh Node Web Interface

As an organization full admin or an organization full admin with compliance office privileges, you can view a list of all recorded content on the node web interface. Follow the steps below to view recordings and perform other administrative functions.

Log in to Control Hub .

Click Hybrid on the lower left side of the screen.

Click View all under Resources in the Video Mesh card.

The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster which you have chosen to handle On-Premises Recording.

A page opens with the list of nodes under the cluster you selected. Click on the right end of a node and click Go to node .

The node web interface opens. Click Recordings on the left side of the screen.

A page opens displaying all of your organization's recordings.

The following actions are available for Organization full administrators with compliance officer privileges :

Resend Recording Link and Password :

Locate the specific recording in the list.

Click the Resend button associated with that recording.

The system will automatically trigger an email containing the recording link and password to the current owner/host.

Reassign Recording Ownership:

Click the Reassign button next to the desired recording.

Enter the email address of the new owner.

Click Save Changes .

The previous owner will receive an email notification that they are no longer the owner, and the new owner will receive an email confirming their new assignment.

Download Recordings:

Locate the recording in the list.

Click the Download button to save a local copy of the recording.

Delete Recordings:

Select the recording you wish to remove.

Click the Delete button.

Confirm the deletion when prompted by clicking Delete Recording .

This action is permanent and cannot be undone.

Full Administrators may reassign ownership and resend recording links, but they cannot download or delete recordings from the list.

#### Troubleshoot alarms on Control Hub

This section contains a comprehensive list of alarms that you may encounter in Control Hub during various stages of enabling on-premises recording.

mf.recordingmanager.nfsConnectivityError

Recording node lost connectivity to NFS

Critical

Recording node lost connectivity to NFS.

mf.recordingmanager.nfsDiskFull

NFS Utilization is critical

Critical

NFS Utilization is above 95%.

mf.recordingmanager.nfsDiskUtilizationHigh

NFS Utilization is high

Warning

NFS Utilization is above 90%.

mf.recordingmanager.unsupportedDeployment

Recording Enabled on Unsupported Deployment Type

Critical

On-premises recording is only supported on VMNLite deployments.

Please remove this node {hostname} from the list of on-premises recording nodes in the Control Hub settings.

mf.device.recordingUnsupportedStorage

Device storage is insufficient for recording functionality

Critical

Total disk space is {X} GB, which is below the minimum recommended storage of 250 GB for recording.

mf.device.untrustedCaCertificate

The server certificate installed on this node is not trusted.

Critical

The server certificate installed on this node is not signed by a trusted Certificate Authority. This may impact recording functionality.

The server certificate installed on this node should be signed by a trusted Certificate Authority. Please update the server certificate at: https://{hostname}/setup/#ca-certs

### Allow guest users to use Video Mesh

Guest users (users not registered Webex) can join meetings that land on Video Mesh, provided they are within the organization's enterprise network. Organization administrators can enable this feature via a toggle in Control Hub.

Log in to Control Hub .

Go to Services > Hybrid on the navigation pane on the left.

- Click Edit Settings on the Video Mesh card.

- Scroll down to the Guest user access card.

- The toggle will be disabled by default. Click on the toggle.

- Click Save to enable guest user access.

### Private Meetings

The Private Meeting feature enhances the security of your meeting by terminating the
            media on your premises. When you schedule a private meeting, the media always terminates
            on the Video Mesh nodes inside your corporate network with no cloud cascade.

As shown here, private meetings never cascade media to the cloud. The media terminates entirely on your Video Mesh clusters. Your Video Mesh clusters can only cascade with each other.

You can reserve a Video Mesh cluster for private meetings. When the reserved cluster is
            full, the private meeting media cascades out to your other Video Mesh clusters. When the
            reserved cluster is full, private meetings and non-private meetings share the resources
            of your remaining clusters.

Non-private meetings don’t use reserved clusters, reserving those resources for the private meetings. If a non-private meeting runs out of resources on your network, it cascades out to the Webex cloud instead.

The Webex App with the Full Featured Webex Experience enabled is incompatible with
                Video Mesh. For details, see Clients and Devices That Use Video Mesh Node .

#### Support and Limitations for Private Meetings

Video Mesh supports private meetings as follows:

Private meetings are available on Webex Version 40.12 and above.

Only scheduled meetings can use the private meeting type. See the Schedule a Cisco Webex Private Meeting article for details.

Private meetings are not available for full-featured meetings started or joined from Webex App.

You can use any current Video Mesh supported device.

Your nodes can use any current image: 72vCPU and 23vCPU.

Private meeting logic doesn’t create any gaps in metrics. We collect the same metrics for Control Hub as for non-private meetings.

Because some users don't activate this feature, the analytics reports for private meetings don't appear if your org doesn't have a private meeting in 90 days.

Private meetings support 1-Way Whiteboarding from a video endpoint.

##### Limitations

Private meetings have these limitations:

Private meetings only support VoIP for audio. They don’t support Webex Edge Audio or PSTN.

You can’t use a personal meeting room (PMR) for a private meeting.

Private meetings don’t support Webex features that require a connection to the cloud, such as, Cloud Recording, Transcription, and Webex Assistant.

You can’t join a private meeting from an unauthenticated cloud registered video system, even one that has paired to the Webex app.

#### Use Private Meetings as the Default Meeting Type

In Control Hub, you can specify that future scheduled meetings for your organization
                be private meetings.

From the customer view in https://admin.webex.com , go to Services > Hybrid .

Click Edit settings from the Video
                        Mesh card. Scroll to Private Meetings and enable the setting.

Save your change.

When you enable this setting, it applies to all meetings for your organization, even
                those previously scheduled.

#### (Optional) Reserve a Cluster for Private Meetings

Private and non-private meetings normally use the same Video Mesh resources. But,
                because private meetings must keep media local, they can’t set up overflows to the
                cloud when the local resources are exhausted. To mitigate that possibility, you can
                set up a Video Mesh cluster to host only private meetings.

In Control Hub, you configure the cluster exclusively for hosting private meetings.
                This setting prevents non-private meetings from using that cluster. Private meetings
                default to using that cluster. If the cluster runs out of resources, private
                meetings cascade only to your other Video Mesh clusters.

We recommend that you provision a private cluster to handle your expected peak usage
                from private meetings.

You can't use the short video address format (meet@ your_site ) if you reserve all Video Mesh clusters for private meetings. These calls currently fail without a proper error message. If you leave some clusters unreserved, calls with the short video address format can connect through those clusters.

From the customer view in https://admin.webex.com , go to Services > Hybrid and click Show all on the Video Mesh
                    card.

Select your Video Mesh cluster from the list and click Edit cluster
                        settings.

Scroll to Private Meetings and enable the setting.

Save your change.

#### Error Messages for Private Meetings

This table lists the possible errors that users might see when joining a private
                meeting.

Error Message

User Action

Reason

External Network Access Denied

You need to be on the corporate network to attend the Private
                                    Meeting. Paired Webex devices located outside the corporate
                                    network would not be able to join the meeting, in such a
                                    scenario try connecting your laptop, mobile to the corporate
                                    network and join the meeting in unpaired mode.

An external user joins from outside the corporate network without
                                    VPN or MRA.

To join a private meeting, external users need access to the
                                    corporate network through a VPN or MRA.

An external user is on VPN, but they're paired to an
                                    unauthenticated device.

Device media doesn't tunnel to the corporate network through the
                                    VPN. The device can't join a private meeting.

Instead, after connecting to VPN, the remote user should join a
                                    private meeting in device unpaired mode from their desktop or
                                    mobile client.

No Available Clusters

The clusters hosting this private meeting are at peak capacity,
                                    unreachable, offline, or not registered. Please contact your IT
                                    admin for assistance.

A user is on the corporate network (on-premises or remote by
                                    VPN), but can’t join a private meeting.

Your Video Mesh clusters are:

At capacity

Unreachable

Offline

Not registered

Not Authorized

You are not authorized to attend this Private meeting as you are
                                    not a member of the Host Organization. Please reach out to the
                                    Host of the meeting.

A user from a different org than the host org tries to join the
                                    private meeting.

Only users belonging to the host org can join a private
                                    meeting.

A device from a different org than the host org tries to join the
                                    private meeting.

Only devices belonging to the host org can join a private
                                    meeting.

### Keep your media on Video Mesh for all external Webex meetings

When your media runs through your local Video Mesh nodes, you get better performance and use less internet bandwidth.

In previous releases, you controlled the use of Video Mesh for meetings only for your internal sites. For meetings that are hosted on external Webex sites, those sites controlled if Video Mesh could cascade to Webex. If an external site didn't allow Video Mesh cascades, your media always used the Webex cloud nodes.

With the Prefer Video Mesh for All External Webex Meetings setting, if your Webex site has available Video Mesh nodes, your media runs through those nodes for meetings hosted on external Webex sites. This table summarizes the behavior for your participants joining Webex meetings:

This setting is off by default, which maintains the behavior from previous releases. In those releases, your Video Mesh didn’t cascade to Webex and your participants joined through the Webex cloud nodes.

In the customer view in https://admin.webex.com , go to Services > Hybrid and click Show all on the Video Mesh card.

Select your Video Mesh cluster in the list and click Edit settings .

Scroll to Prefer Video Mesh for All External Webex Meetings and enable the setting.

Save your change.

### Optimize utilization of your Video Mesh deployment

You can land all your clients on your Video Mesh clusters for an improved user experience through Video Mesh. If your Video Mesh cluster capacity is temporarily down or you have increased usage, you can optimize your Video Mesh cluster utilization by controlling which client types land on Video Mesh clusters. This helps manage your existing capacity effectively until you can add more nodes to meet the demand.

See the Analytics portal on Control Hub to understand usage, utilization, redirect, and overflow trends. Based on these trends, you could, for example, choose to have the desktop clients or SIP devices land on Video Mesh clusters, and have the mobile clients land on Webex cloud nodes. Compared to the mobile clients, the desktop clients and SIP devices support higher resolution, have larger screens, and use more bandwidth, and you can optimize the user experience for the participants using those client types.

You can also optimize the cluster capacity and maximize the user experience by having the client types that most of your customers use land on Video Mesh clusters.

Sign in to Control Hub , then select Services > Hybrid > Video Mesh > Resources > View all .

- or -

Select Overview > Hybrid services > Video Mesh > Settings .

Under Client Type Inclusion Settings , all client types are checked by default. Uncheck the client types you want to exclude from using the Video Mesh clusters. These clusters are hosted on Webex cloud nodes.

Click Save .

### Deregister  Video Mesh Node

From the customer view in https://admin.webex.com , go to Services > Hybrid .

Click View all on the Video Mesh card.

From the list of resources, go to the appropriate cluster and choose the node.

Click Action > Deregister Node .

A message appears asking you to confirm that you want to delete the node.

After you read and understand the message,
                                                  click Deregister
                                                  Node .

### Move Video Mesh Node

From the customer view in https://admin.webex.com , go to Services > Hybrid , and then choose View all on the Video Mesh card.

From the list, select the node that you want to move and then click Actions (the vertical ellipsis).

Select Move Node .

Choose the appropriate radio button for where you want to move the node:

- Select an existing cluster —Choose an existing
                        cluster from the drop-down list.

- Create a new cluster —Enter a name for the new
                        cluster in the field.

Click Move Node .

Your node moves to the new cluster.

Move a Node in to Maintenance Mode

### Set Video Mesh Cluster Upgrade Schedule

You can set a specific upgrade schedule or use the default schedule of 3 a.m. Daily United States: America/Los Angeles. You can choose to postpone an upcoming upgrade, if necessary.

Software upgrades for Video Mesh are done automatically at the cluster level, which ensures that all nodes are always running the same software version. Upgrades are done according to the upgrade schedule for the cluster. When a software upgrade becomes available, you can manually upgrade the cluster before the scheduled upgrade time.

Before you begin

Urgent upgrades are applied as soon as they are available.

From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click View all on the Video Mesh card.

Click a media resource and then click Edit cluster settings .

On the Settings page,
                                                  scroll to Upgrade , and then
                                                  choose the time, frequency, and time zone for the
                                                  upgrade schedule.

Upgrades may take longer than a few minutes if the Video Mesh node is waiting for active calls to end. For a more immediate upgrade process, we recommend that you schedule the automatic upgrade window outside of your regular business hours.

(Optional) If needed, click Postpone to defer the
                                                  upgrade one time, until the subsequent
                                                  window.

Under the time zone, the next available upgrade
                                                  date and time are displayed.

The node makes periodic requests to the cloud to see if an update is available.

The cloud does not make the upgrade available until the cluster's upgrade window arrives. When the upgrade window arrives, the node's next periodic update request to the cloud delivers the update information.

The node pulls updates over a secure channel.

Existing services gracefully shut down to stop incoming calls routing to the node. The graceful shutdown also gives existing calls time to complete (up to 2 hours).

The upgrade installs.

The cloud only triggers the upgrade for a percentage of nodes in a cluster at a time.

Redeploy a node if it hasn't been upgraded or has been in maintenance mode for six months.

### Delete Video Mesh Cluster

From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click View all .

From the list of resources, scroll to the Video Mesh resource that you want to delete, and then click Edit Cluster Settings .

You can click Video Mesh to filter on just Video Mesh resources.

Click Delete Cluster , and then choose one:

- Click Move All Nodes . For each node, either
                        create a new resource by choosing an existing resource from the drop-down
                        list or entering a new name, and then click Continue .

- Click Deregister All Nodes , check the check box,
                        and then click Delete Cluster .

### Deactivate Video Mesh

Before you begin

Before you deactivate Video Mesh, you will deregister all Video Mesh nodes.

From the customer view in https://admin.webex.com , go to Services > Hybrid > View All , choose Settings on the Video Mesh card.

Click Deactivate .

Review the list of clusters and read the disclaimer in the dialog.

Check the check box to confirm that you understand this action, and click Deactivate on the dialog.

When you are ready to deactivate your Video Mesh, click Deactivate Service .

Deactivation removes all Video Mesh nodes and clusters. Video Mesh is no longer configured.

### Troubleshoot Video Mesh Node Registration

This section contains possible errors you may encounter during registration of your Video Mesh node to the Webex cloud and suggested steps to correct them.

#### The domain could not be resolved

This message appears if the DNS settings configured on your Video Mesh node are not correct.

Sign in to the console of your Video Mesh node and make sure the DNS settings are correct.

#### Could not connect to site using port 443 via SSL

This message appears if your Video Mesh node cannot connect to the Webex cloud.

Make sure your network allows connectivity on the ports required for Video Mesh. For details, see Ports and Protocols Used by Video Mesh .

### ThousandEyes integration with Video Mesh

The Video Mesh platform is now integrated with the ThousandEyes agent enabling you to perform end-to-end monitoring across your hybrid digital ecosystem. This integration equips you with a wide array of network monitoring tests opening visibility into areas like proxies, gateways, and routers. Issues anywhere along a customer's network infrastructure can be narrowed down and diagnosed with greater precision, improving the efficiency of their deployment.

#### Benefits of ThousandEyes Integration

- Provides you multiple test types to choose from. You can configure one or more tests appropriate for the application or asset you want to monitor.

- Enables you to set test thresholds specific to your requirements.

- The test results are available via the ThousandEyes web app and the ThousandEyes API on a real-time basis.

- Greater visibility in troubleshooting – Customers can identify the origin of an issue in their network, reducing resolution times.

#### Network configuration for ThousandEyes agent

Refer to Docker Containers in Firewall Configuration for Enterprise Agents for information on configuring the Enterprise Agent network to traverse a firewall or similar device.

#### Enabling ThousandEyes for Video Mesh

Use this procedure to enable ThousandEyes agent for your Video Mesh deployment.

From Control Hub , click Hybrid on the lower-left side of the screen.

Click Edit Settings on the Video Mesh card.

Scroll down to ThousandEyes Integration . The toggle will be disabled by default. Click on the toggle to enable it.

Click ThousandEyes User Profile , the ThousandEyes web portal opens, sign in using the admin credentials.

A side panel is displayed with the Account Group Token .

Click on the view icon and then click Copy .

The token will not be copied correctly if the view token button is not clicked.

Go back to the Control Hub tab, paste the token in the Agent Token field.

Click Activate , ThousandEyes is now enabled for your Video Mesh deployment.

What to do next

- After 5 minutes, go back to the ThousandEyes webpage, click Cloud and Enterprise Agents ,then click Agent Settings . You should be able to view all your nodes listed as agents under Enterprise Agents . If the agents are not displayed, check ThousandEyes Integration card on Control Hub for error messages.

- If an error message is displayed, click the toggle, then click Deactivate . Repeat the steps to enable ThousandEyes agent, ensuring that the correct account group token is copied and pasted in the Agent Token field.

#### Configuring tests using ThousandEyes

##### Network Test – Agent-to-Agent

The agent-to-agent network test allows users of ThousandEyes to have ThousandEyes agents at both ends of a monitored path, enabling testing of the path in either or both of two directions: source to target or target to source. For detailed information on how to configure an agent-to-agent test, see Agent-to-Agent Test Overview .

A sample test creation dialog is shown below.

##### SIP Server Test

SIP server tests facilitate network measurements, BGP data collection and, most importantly, SIP service availability and performance testing against SIP-based VoIP infrastructure.

For detailed information on how to configure a SIP Server test, see SIP Server Test Settings .

A sample test creation dialog is shown below.

##### RTP Stream Test

An RTP Stream test creates a simulated voice data stream between two ThousandEyes agents acting as the VoIP user agents. RTP packets are sent between one or more agents and a target agent, using UDP as the transport protocol, to obtain Mean Opinion Score (MOS), packet loss, discards, latency, and Packet Delay Variation (PDV) metrics. Metrics produced are one-way metrics (source to target). The RTP Stream test provides server port, call duration, de-jitter buffer size and codec configuration options.

For detailed information on configuring an RTP Stream Test, see RTP Stream Test Settings .

A sample test creation dialog is shown below.

##### Webex HTTP Server URL Test

This test monitors the primary landing page that your users connect to when they access Webex. A sample test creation dialog is shown below.

##### Authoritative Webex DNS Server Test

This test is used to ensure that your Webex domain is properly resolving both internally and externally. When using Enterprise Agents, update the DNS Servers field to use your internal name servers. If you use Cloud Agents for external visibility, use the Lookup Servers button to auto-populate the authoritative external name servers. This example shows Cloud Agents resolving cisco.webex.com. You will need to update it to your organization's domain.

A sample test creation dialog is shown below.

'

### Manage Video Mesh Node From the Web Interface

Before you can make any network changes to Video Mesh nodes that are registered to the cloud, you must use Control Hub to put them in maintenance mode. For more information and a procedure to follow, see Move a Node Into Maintenance Mode .

Maintenance mode is intended solely to prepare a node for shutdown or reboot so that you can make certain networking setting changes (DNS, IP, FQDN) or prepare for hardware maintenance such as replace RAM, hard drive, and so on.

Upgrades do not happen when a node is placed in maintenance mode.

When you place a node into maintenance mode, it does a graceful shutdown of calling services (stops accepting new calls and waits up to 2 hours for existing calls to complete). The purpose of the graceful shutdown of calling services is to allow reboot or shutdown of the node without causing dropped calls.

#### How to access the Video Mesh overview

You can open the web interface in either of these ways:

If you are a Full Administrator and you already registered the node to the cloud, you can access the node from Control Hub.

From the customer view in https://admin.webex.com , go to Services > Hybrid . Under Resources on the Video Mesh card, click View all . Click on the cluster, and then click on the node that you want to access. Click Go to Node .

Only a Full Administrator for your Webex organization can use this feature. Other administrators, including Partner and External Full Administrators, don't have the Go To Node option for the Video Mesh resources.

In a browser tab, navigate to <IP address> /setup , for example, https://192.0.2.0/setup . Enter the admin credentials that you set up for the node, and then click Sign In .

If the admin account has been disabled, this method is not available. See the "Disable or Re-enable the Local Admin Account from Web Interface" section.

The overview is the default page and has the following information:

Call Status —Provides the number of ongoing calls through the node.

Node Details —Provides the node type, software image, software version, OS version, QoS status, and maintenance mode status.

Node Health —Provides usage data (CPU, memory, disk), and service status (Management Service, Messaging Service, NTP Sync).

Network Settings —Provides network information: hostname, interface, IP, gateway, DNS, NTP, and whether dual IP is enabled.

Registration Details —Provides registration status, organization name, org ID, cluster the node is a part of, and cluster ID.

Cloud Connectivity —Runs a series of tests from the node to the Webex cloud and third party destinations that the node needs to access to run properly.

Three types of tests are run: DNS resolution, server response time, and bandwidth.

DNS tests validate that the node can resolve a particular domain. These tests report as failed if the server does not respond within 10 seconds. They show as "Passed" with an orange "warning color" if the response time is between 1.5 and 10 seconds. The periodic DNS checks on the node generate alarms if the DNS response time is longer than 1.5 seconds.

Connect tests validate that the node can connect to a particular HTTPS URL and receive a response (responses other than proxy or gateway errors are accepted as evidence of connection).

The list of tests run from the overview page are not exhaustive and do not include websocket tests.

The node sends alarms if the calling processes cannot complete websocket connections to the cloud or connect to call-related services.

A Pass or Fail result appears next to each test; you can hover over this text to see more information about what was checked when the test ran.

As shown in the screenshot that follows, alarm notifications can also appear in the side panel, if any alarms were generated by the node. These notifications identify potential issues on the node and make suggestions for how you can troubleshoot or resolve these issues. If no alarms were generated, the notification panel does not appear.

#### Configure Network Settings From Video Mesh Node Web Interface

If your network topology changes, you can use the web interface for each Webex Video Mesh node and change the network settings there. You may see a caution about changing the network settings, but you can still save the changes in case you're making changes to your network after changing Webex Video Mesh node settings.

Open the Webex Video Mesh node interface.

Go to Network .

The current network settings for the node appear.

Change the following settings for Host and Network Configuration as needed:

An error is displayed if the FQDN (hostname and domain) does not have the correct format.

- Under Network Mode , Enable DHCP is listed, but DHCP is not supported. You must set a static IP address, subnet mask, and gateway.

The  Video Mesh Node must have an internal IP address and resolvable DNS name. The node IP address must not belong to the IP address range reserved for  Video Mesh Node internal use. The default reserved IP address range is 172.17.42.0–172.17.42.63, which can be configured later in the Diagnostic menu in the node console. This IP address range is for communication within the  Video Mesh Node and between the software containers which hold the different components of the node—for example, SIP interface and media transcoding.

- Under Edit DNS Servers , change the DNS server entries, which handle translating domain names to numeric IP addresses. You can enter up to 4 DNS servers.

Click Save Host and Network Configuration , and after the popup appears that says the node needs to reboot, click Save and Reboot .

During the save, all fields are validated on the server side. Warnings that appear generally indicate that the server isn't reachable or a valid response wasn't returned when queried—for example, if the FQDN is not resolvable using the DNS server addresses provided. You may choose to save by ignoring the warning but calls will not work until the FQDN can resolve to the DNS configured on the node. Another possible error state is if the gateway address is not in the same subnet as the IP address. After the  Video Mesh Node reboots, the network configuration changes take effect.

Change the following settings for NTP Servers as needed:

- Under Edit NTP Servers , change the values for the NTP server entries, which are used in your organization to synchronize time to the node.

Click Save NTP Servers .

If you configure more than one NTP servers, the poll interval for failover is 40 seconds.

If the NTP server is an FQDN and that isn’t resolvable, a warning is returned. If the NTP server FQDN is resolved but the resolved IP can't be queried for NTP time, a warning is returned.

#### Set The External Network Interface From The  Video Mesh Node Web Interface

If your network topology changes, you can use the web interface for each Webex Video Mesh node and change the network settings there. You may see a caution about changing the network settings. However, you can still save the changes in case you're making changes to your network after changing Webex Video Mesh node settings.

You can configure the external network interface if you're deploying the  Video Mesh Node in your network's DMZ so that you can isolate the enterprise (internal) traffic from the outside (external) traffic.

Open the Webex Video Mesh node interface.

Go to Network .

The current network settings for the node appear.

Click Advanced .

Toggle on Enable External Network and then click Ok to enable the external IP address options on the node.

Enter the External IP Address , External Subnet Mask , and External Gateway values.

Click Save External Network Configuration .

Click Save and Reboot to confirm the change.

The node reboots to enable the dual IP address, and then automatically configures the basic static routing rules. These rules determine that traffic to and from a private class IP address uses an internal interface; traffic to and from a public class IP address uses an external interface. Later, you can create your own routing rules—For example, if you need to configure an override and allow access to an external domain from the internal interface.

If there are errors, click Ok to close the error dialog box, fix the errors, and click Save External Network Configuration again.

What to do next

To validate the internal and external IP address configuration, do the steps in Run a Ping from Video Mesh Node Web Interface .

Test an external destination (example, cisco.com); if successful, the results show that the destination was accessed from the external interface.

Test an internal IP address; if successful, the results show that the address was accessed from the internal interface.

#### Add Internal and External Routing Rules From Video Mesh Node Web Interface

In a dual network interface (NIC) deployment, you can fine tune the routing for Video Mesh nodes by adding user-defined route rules for external and internal interfaces. The default routes are added to the nodes, but you can make exceptions—for example, external subnets or host addresses that need to be accessed through the internal interface, or internal subnets or host addresses that need to be accessed from the external interface. Perform the following steps as needed.

Before you begin

Open the Webex Video Mesh node interface.

Go to Network .

The current network settings for the node appear. If you have configured the external network, the Routing Rules tab appears.

Click the Routing Rules tab.

The first time you open this page, the default system routing rules appear in the list. By default, all internal traffic goes through the internal interface and external traffic through the external interface.

You can add manual overrides to these rules in the next steps.

To add a rule, click Add Routing Rule , then choose one of the following option:.

- For Network Type , click Internal , and then enter the external subnet or host IP address to use for the internal route.

- For Network Type , click External , and then enter the internal subnet or host IP address to use for the external route.

Click Add Routing Rule .

As you add each rule, they appear in the routing rule list, categorized as user defined rules.

To delete one or more user-defined rules, check the check box in the column to the left of the rules and then click Delete Routing Rule(s) .

The default routes cannot be deleted, but you can delete any user-defined overrides that you configured.

Custom routing rules may create potential for conflicts with other routing. For example, you may define a rule that freezes your SSH connection to the Video Mesh Node interface. If this happens, do one of the following and then remove or modify the routing rule:

Open an SSH connection to the public IP address of the Video Mesh Node.

Access the Video Mesh Node through the ESXi console

#### Configure Container Network From Video Mesh Node Web Interface

Video Mesh node reserves a subnet range for internal use within the node. The default range is 172.17.42.0–172.17.42.63. The nodes do not respond to any external-to-Video Mesh node traffic originating from this range. You may want to use the node console to change the container bridge IP address to avoid conflicts with other devices in your network.

Open the Webex Video Mesh node interface.

Go to Network .

The current network settings for the node appear.

Click Advanced .

Change the values for Container IP Address and Container Subnet Mask , as needed, and then click Save Container Network Configuration .

Click Save and Reboot to confirm the change.

If there are errors, click Ok to close the error dialog box, fix the errors, and click Save Container Network Configuration again.

#### Set the Network Interface MTU Sizes

All Webex Video Mesh nodes have path MTU (PMTU) discovery enabled by default. With PMTU, the node can detect MTU issues and adjust the MTU size automatically. When PMTU fails because of firewall or network issues, the node can have connectivity issues to the cloud because packets larger than the MTU drop. Manually setting a lower MTU size can fix this issue.

Before you begin

If you've already registered the node, you must put the node in maintenance mode before you can change the MTU settings.

Open the Webex Video Mesh node interface.

Go to Network .

The current network settings for the node appear.

Click Advanced .

In the Interface MTU Settings section , enter an MTU value between 1280 and 9000 bytes in the applicable field(s).

If you have enabled the external interface, you can set both the internal and external interface MTU sizes separately.

What to do next

If you put the node in maintenance mode to change the MTU, turn off maintenance mode.

#### Enable or Disable DNS Caching

If DNS responses to your Video Mesh nodes regularly take more than 750 ms, or if the
                Cisco TAC recommends it, you can enable DNS caching. With DNS caching on, the node
                caches DNS responses locally. With the cache, requests are less prone to delay or
                timeouts that can lead to connectivity alarms, call drops, or call quality issues.
                DNS caching can also reduce the load on your DNS infrastructure.

Before you begin

Move the node to maintenance mode . When the maintenance mode status is On (active calls have completed or have dropped at the
                end of the pending period), you can enable or disable DNS caching.

Open the Webex Video Mesh node interface.

Go to Network .

The current network settings for the node appear.

Click Advanced .

In the DNS Caching Configuration section, toggle Enable DNS Caching on or off.

In the confirmation dialog, click Save and Reboot .

After the node reboots, reopen the Webex Video Mesh node interface and confirm that the connectivity checks are succeeding on the Overview page.

When you enable DNS caching, the DNS Cache Statistics displays
                the following statistics:

Statistic

Description

Cache Entries

The number of previous DNS resolutions that the DNS Cache server
                                    has stored

Cache Hits

The number of times since the cache reset that the cache handled
                                    a DNS request from Video Mesh, without querying the customer DNS
                                    server

Cache Misses

The number of times since the cache reset that the customer DNS
                                    server handled a DNS request from Video Mesh rather than through
                                    the cache

Cache Hit Percent

The percent of DNS requests from Video Mesh that the cache
                                    handled without querying the customer DNS server

Cache Server Outbound DNS queries

The number of DNS queries that the Video Mesh DNS cache server
                                    made against the customer DNS servers

Cache Server Inbound DNS queries

The number of DNS queries that Video Mesh made against its
                                    internal DNS Cache server

Outbound to Inbound Query Ratio

The ratio of DNS queries made by Video Mesh against the customer
                                    DNS server to the queries made by Video Mesh against its
                                    internal DNS Cache server

Inbound Queries Per Second

The average number of DNS queries per second that Video Mesh made
                                    against its internal DNS Cache server

Outbound Queries Per Second

The average number of DNS queries per second that Video Mesh made
                                    against the customer DNS servers

Outbound DNS Latency [time range]

The percent of DNS queries that Video Mesh made against the
                                    customer DNS servers where the response time fell into the
                                    described time range

Use the Wipe DNS Cache button to reset the DNS cache when TAC
                requests. After wiping the DNS cache, you see a higher Outbound to
                    Inbound Query Ratio as the cache replenishes. You don't need to
                place the node in maintenance mode to wipe the cache.

What to do next

Move the node out of maintenance mode. Then repeat the task on any other nodes that require a change.

#### Upload Security Certificates

Set up a trust relationship between the node and an external server, such as a syslog
                server.

In a clustered environment, you must install CA and server certificates on each node individually.

Open the Webex Video Mesh node interface.

When setting up TLS with another server, such as a syslog server , we recommend for security reasons that you use a CA signed certificate
                    on your Video Mesh nodes instead of the node's default self-signed certificate.
                    To create and upload the certificate and key pairs on the Video Mesh node, go to Server Certificates , and follow these steps:

If you need a certificate issued from a certified
                            provider, click Create a Certificate Signing
                                Request . Fill out the required information (including
                            the Subject Alternative Name(s) , which are FQDNs
                            that must contain the common name). Then, generate and download the CSR
                            to submit the request to the provider. You can create multiple CSRs. The
                            provider returns the certificate authority (CA) signed certificate. (The
                            CSR creation step already generated the private key.)

The common name is not a URL. It doesn’t include any protocol
                                    (e.g. http:// or https://), port number, or pathname. The commonName field in the X.509 certificate
                                    specification technically represents the common name. For https://www.example.com , the correct value
                                    is example.com .

When you have the certificate and key, click Upload a Server
                                Certificate (.crt or .pem file) , choose the certificate
                            file, then click Upload a Private Key (.key file) and enter a passphrase if you have one.

The private key is already in place when a CSR is generated. You only
                                need to upload a private key if you do not use the CSR creation
                                step.

After you get the certificate, go to the first Video Mesh node in a
                            cluster, click Install Server Certificate , read
                            the prompt, click Install , then click OK .

A Video Mesh node that's registered to the cloud waits up to 2 hours
                                for any calls to end and puts itself into a temporary inactive state
                                (quiesces). Once either the existing calls finish or 2 hours pass
                                (whichever comes first), this node completes the certificate
                                installation. A prompt appears when the server certificate
                                installation completes, and you can then reload the page to view the
                                new certificate and key entry.

Click Download next to the certificate and key
                            files to save a local copy.

Save the files somewhere that's easy to remember and leave the
                                instance open in the browser tab.

Go to the second Video Mesh node in the cluster, fill in the
                            passphrase, and then upload the private key file. Then click Upload a Server Certificate and then choose Install Server Certificate , read the prompt,
                            click Install , then click OK .

Repeat these steps on every other Video Mesh node in the same
                            cluster.

Choose an option depending on how the external server's CA certificate is signed:

- If the server's CA certificate is signed by a generally recognized
                        organization, such as DigiCert, GeoTrust, or GlobalSign, the Video Mesh node
                        will trust it based on the list of root certificates from the Video Mesh
                        node's host OS, which are updated periodically. Skip to Step 6 .

- If the server's CA certificate is signed by an internal enterprise CA root certificate, the root certificate from that authority must be added to the Video Mesh node. Continue with the next step.

Get the certificate or certificate trust list (CTL) that the external server
                    uses.

As with the Video Mesh node certificate, save the external server file
                        somewhere that's easy to remember.

Go back to the Webex Video Mesh node interface tab, click Trust Store & Proxy , then choose an option:

- To install a single CA certificate, click Upload a Root Certificate or End Entity Certificate (.crt or .pem file) , and then choose the certificate file from your computer, click Install All Certificates into the Trust Store , read the prompt, click Install , and then reboot the node.

- To install a certificate chain, upload the root CA certificate and intermediate CA certificate, and then click Install All Certificates into the Trust Store , read the prompt, and then click Install .

A Video Mesh node that's registered to the cloud waits up to 2 hours for any calls to end and puts itself into a temporary inactive state (quiesces). To install the certificate, the node must reboot and does so automatically. When it comes back online, a prompt appears when the certificate is installed on the Video Mesh node, and you can then reload the page to view the new certificate.

Repeat the certificate or certificate chain upload on every other Video Mesh
                    node in the same cluster.

#### Generate Video Mesh Logs for Support

You may be instructed to send logs directly to Cisco, or you can download them yourself to attach to a case. Use this procedure from the web interface to generate logs and send them to Cisco or download them from any Video Mesh nodes. The generated log package contains media logs, system logs, and container logs. The bundle provides useful information for connectivity to Webex, platform issues, and call setup or media, so that Cisco can troubleshoot your Video Mesh node deployment for you.

Open the Webex Video Mesh node interface.

Go to Troubleshooting , and then choose an option next to Send Logs :

- Click Send Logs to Cisco to generate a log bundle from the node and send the bundle directly to Cisco in one step. You'll see a status indicator that changes as the logs are compressed, zipped, and uploaded.

- Click Download to generate a long bundle from the node that you can save locally or attach to a case later.

Generated logs are historically stored on the node and remain on the node even after reboots. An upload identifier shows on the page. Support uses this value to identify your uploaded logs.

When you open a case or interact with the Cisco TAC , include the upload identifier value so that your support engineer can access the logs.

If you submitted the log to Cisco directly, you don't need to upload the log bundle to the TAC case.

What to do next

While logs are uploading to Cisco or being downloaded, you can run a packet capture from the same screen.

#### Generate Video Mesh Packet Captures for Support

You can run a packet capture (PCAP) and submit it to Cisco for further analysis. A packet capture takes a snapshot of data packets that go through the node's network interfaces. After packets are captured and submitted, Cisco can analyze the submitted capture and help with troubleshooting your Video Mesh node deployment.

Before you begin

The packet capture functionality is intended for debugging purposes only. If you run a packet capture on a live Video Mesh node that is hosting active calls, the packet capture may affect the performance of the node and the generated file might be overwritten. This causes a loss of captured data. We recommend that you run the packet capture only during off peak hours or when the call count is less than 3 on the node.

Open the Webex Video Mesh node interface.

Go to Troubleshooting .

You can start the packet capture and upload logs at the same time.

(Optional) In the Packet Capture section, you can limit the capture to packets on a  specific interface, filter by packets to or from specific hosts, or filter by packets on one or more ports.

To begin the process, toggle on the Start Packet Capture setting.

When you are done, toggle off the Start Packet Capture setting.

Choose one:

- Click Send PCAP to Cisco to send the packet capture from the node directly to Cisco. You'll see a status indicator that changes as the packet capture is uploaded.

- Click Download to save a local copy of the packet capture from the node. You can attach it to a case later.

After a package capture is uploaded, an upload identifier shows on the page. Support uses this value to identify your uploaded packet capture. The maximum size for packet captures is 2 GB.

When you open a case or interact with the Cisco TAC , include the upload identifier value so that your support engineer can access the packet capture.

#### Run a Ping from Video Mesh Node Web Interface

You can run a ping from the Video Mesh node web interface. This step tests a destination you enter and sees if the Video Mesh node can reach it.

Open the Webex Video Mesh node interface.

Go to Troubleshooting , scroll to Ping , and then enter a destination address that you want to test in the FQDN or IP Address field under Test Connectivity Using Ping .

Click Ping .

The test runs and you'll see a ping success or failure message. The test does not have a timeout limit. If you receive a failure or the test runs indefinitely, check the destination value that you entered and your network settings.

#### Run a Trace Route from Video Mesh Web Interface

You can run a traceroute from the Video Mesh node web interface. This step shows the route taken by packets from the node towards the destination that you enter. Viewing the traceroute information helps you determine why a particular connection might be poor and can help you identify problems.

Open the Webex Video Mesh node interface.

Go to Troubleshooting , scroll to Traceroute , and then enter a destination address that you want to test in the FQDN or IP Address field under Trace Route to Host .

The test runs and you'll see trace route success or failure message. The test times out at 16 seconds. If you receive a failure or the test times out, check the destination value that you entered and your network settings.

#### Check NTP Server from Video Mesh Node Web Interface

You can enter a FQDN or IP address of a network time protocol (NTP) server to confirm that the Video Mesh node can access the server. This test is helpful if you notice time synchronization issues and want to rule out the reachability of the NTP server.

Open the Webex Video Mesh node interface.

Go to Troubleshooting , scroll to Check NTP Server , and then enter a destination address that you want to test in the FQDN or IP Address field under View SNTP Query Response .

The test runs and you'll see a query success or failure message. The test does not have a timeout limit. If you receive a failure or the test runs indefinitely, check the destination value that you entered and your network settings.

#### Identify Port Issues With Reflector Tool in the Web Interface

The reflector tool (a combination of a server on the  Video Mesh node and client through a Python script) is used to verify whether the required TCP/UDP ports are open from  Video Mesh nodes.

Before you begin

Download a copy of the Reflector Tool Client (a Python script) from https://github.com/CiscoDevNet/webex-video-mesh-reflector-client .

For the script to work properly, ensure that you're running Python 2.7.10 or later in your environment.

Currently, this tool supports SIP endpoints to  Video Mesh nodes and intracluster verification.

From the customer view in https://admin.webex.com , enable maintenance node for the Video Mesh Node by following these instructions .

Wait for the node to show a 'Ready for maintenance' status in Control Hub.

Open the Webex Video Mesh node interface.

For instructions, see Manage Video Mesh Node From the Web Interface .

Scroll to Reflector Tool , and then start either the TCP Reflector Server or UDP Reflector Server , depending on what protocol you want to use.

Click Start Reflector Server , and then wait for the server to start successfully.

You'll see a notice when the server starts.

From a system (such as a PC) on a network that you want Video Mesh nodes to reach, run the script with the following command:

```
$ python <local_path_to_client_script>/reflectorClient.py --ip <ip address of the server> --protocol <tcp or udp>
```

At the end of the run, the client shows a success message if all the required ports are open:

The client shows a failed message if any required ports are not open:

Resolve any port issues on the firewall and then rerun the above steps.

Run the client with --help to get more details.

#### Enable Debug User Account From Video Mesh Node Web Interface

If Cisco TAC requires access to the Webex Video Mesh node, you can temporarily enable a debug user account so that support can run further troubleshooting.

Open the Webex Video Mesh node interface.

Go to Troubleshooting , and then toggle on the Enable Debug User setting.

An encrypted passphrase appears that you can provide to Cisco TAC.

Copy the passphrase, paste it in the support ticket or directly to the support engineer, and then click OK when you have it saved.

The debug user account is valid for 3 days, after which it expires.

What to do next

You can disable the account before it expires if you return to the Troubleshooting page and then toggle off the Enable Debug User setting.

#### Factory Reset a Video Mesh Node From The Web Interface

As part of deregistration cleanup, you can factory reset the Video Mesh node from the web interface. This step removes any configuration you put in place while the node was active but does not remove the virtual machine entry. Later, you may want to reregister this node as part of another cluster that you build from scratch.

Admin credentials and network configurations are retained even after a factory reset.

Before you begin

You must use Control Hub to deregister the Video Mesh node from the cluster that's registered in Control Hub.

Open the Webex Video Mesh node interface.

Go to Troubleshooting , scroll to Factory Reset , and then click Reset Node .

Ensure that you understand the information in the warning prompt that appears, and then click Reset and Reboot .

The node reboots automatically after the factory reset.

#### Disable or Re-enable the Local Admin Account From Web Interface

When you install a Webex Video Mesh node, you initially sign in using a built-in local account with the user name "admin." Once you register the node to the Webex cloud, you can use your Webex organization administration credentials to manage your Video Mesh nodes from Control Hub. This way, the administrator account policy and management processes that apply to Control Hub also apply to your Video Mesh nodes. For further control, you can disable the built-in "admin" account so that Control Hub handles all administrator authentication and management.

Use these steps after you have registered the node to the cloud to disable (or later re-enable) the admin user account. When you disable the admin account, you must use Control Hub to access the node web interface.

Only a Full Administrator for your Webex organization can use this feature. Other
                    administrators, including Partner and External Full Administrators, don't have
                    the Go To Node option for the Video Mesh resources.

From the customer view in https://admin.webex.com , go to Services > Hybrid .

Under Resources on the Video Mesh card, click View all .

Click on the cluster and then click on the node that you want to access. Click Go to Node .

Go to Administration .

Toggle the Enable Admin User Sign In switch off to disable the account, or on to re-enable it.

You can't disable the admin account until you've registered the node to the cloud.

On the confirmation screen, click Disable or Enable to complete the change.

Once you disable the admin user, you can't sign in to the Video Mesh node through the
                WebUI or the CLI launched from SSH. However, you can sign in using the admin user
                credentials through a CLI launched from the VMware ESXi console.

#### Change Admin Passphrase From Web Interface

Use this procedure to change the administrator passphrase (password) for your Webex Video Mesh node by using the web interface.

Open the Webex Video Mesh node interface.

Go to Administration , and next to Change Passphrase , click Change .

Enter the Current Passphrase , and then enter a new passphrase value in both New Passphrase and Confirm New Passphrase .

Click Save Passphrase .

A "password changed" message appears and then you go back to the sign in screen.

Sign in using your new admin login and passphrase (password).

#### Change Passphrase Expiry Interval From the Web Interface

Use this procedure to change the default passphrase expiry interval of 90 days by using the web interface. When the interval is up, you are prompted to enter a new passphrase when you sign into the Video Mesh node.

Open the Webex Video Mesh node interface.

Go to Administration , and next to Change Passphrase Expiry , enter a new value for Expiry Interval (Days) (up to 365 days), and then click Save Passphrase Expiry Interval .

A success screen appears, and you can then click OK to finish.

The Administration page also shows dates for the last passphrase change and the next time the password expires.

#### Set External Logging to a Syslog Server

If you have a syslog server, you can set your Webex Video Mesh node to log to the external server audit trail information, such as:

Details on administrator sign-ins

Configuration changes (including turning maintenance mode on or off)

Software updates

The node aggregates the logs, if any, and sends them to the server every ten minutes.

Open the Webex Video Mesh node interface.

Go to Administration .

Next to External Logging , toggle on Enable External Logging .

For Syslog Server Details , enter the host IP address or fully-qualified domain name and the syslog port.

If the server isn’t DNS-resolvable from the node, use an IP address in the Host field.

Choose the Protocol —UDP or TCP.

To use TLS encryption, choose TCP and then toggle on Enable TLS . Make sure that you also upload and install the security certificates required for TLS communication between the node and the syslog server. If no certificates are installed, the node defaults to using its self-signed certificates. For help, see Upload Security Certificates .

Click Save External Logging Configuration .

The properties of the log message follow this format: Priority Timestamp Hostname Tag Message .

Property

Description

Priority

The value is always 131, based on the formula: Priority = (Facility Code * 8) + Severity.

The facility code is 16 for "local0". The severity is 3 for "notice".

Timestamp

The timestamp format is "Mmm dd hh:mm:ss".

Hostname

The hostname for the Video Mesh node.

Tag

The value is always syslogAuditMsg.

Message

The message is a JSON string of at least 1KB. Its size depends on the number of aggregated events in the ten minute interval.

Here is an example message:

```
{
  "events": [
    {
      "event": "{\hostname\": \"test-machine\", \"event_type\": \"login_success\",
       \"event_category\": \"node_events\", \"source\": \"mgmt\", \"session_data\":
       {\"session_id\": \"j02wH5uFTKB22SqdYCrzPrqDWkXIAKCz\", \"referer\":
       \"https:// IP address /signIn.html?%2Fsetup\", \"url\":
       \"https:// IP address /api/v1/auth/signIn\", \"user_name\": \"admin\",
       \"remote_address\": \" IP address \", \"user_agent\": \"Mozilla/5.0
       (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
       Chrome/87.0.4280.67 Safari/537.36\"}, \"event_data\": {\"type\": \"Conf_UI\"},
       \"boot_id\": \"6738705b-3ae3-4978-8502-13b74983e999\", \"timestamp\":
       \"2020-12-07 22:40:27 (UTC)\", \"uptime\": 358416.23, \"description\":
       \"Log in to Console or Web UI successful\"}"
    },
    {
      "event": "{\hostname\": \"test-machine\", \"event_type\":
       \"software_update_completed\", \"event_category\": \"node_events\", \"source\":
       \"mgmt\", \"event_data\": {\"release_tag\": \"2020.12.04.2332m\"}, \"boot_id\":
       \"37a8d17a-69d8-4b8c-809d-3265aec56b53\", \"timestamp\":
       \"2020-12-07 22:17:59 (UTC)\", \"uptime\": 137.61, \"description\":
       \"Completed software update\"}"
    }
  ]
}
```

### Webhooks for Video Mesh alerts

Video Mesh supports Webhook alerts which enable organization admins to receive alerts on specific events. Admins can choose to be notified of events like call overflows and call redirects, minimizing the need to log in to Control Hub for monitoring their deployment. This is achieved by creating a webhook subscription where a target URL is provided by the admin, to which alerts will be sent. Using webhooks for alerts also allows monitoring of parameters without using the associated developer APIs.

The following event types can be monitored through webhooks:

Cluster Call Redirects – Calls redirected from a particular cluster.

Org Call Overflows – Total call overflows to cloud for an organization.

#### Create a Webhook subscription

Log in to the Cisco Webex Developer portal using admin credentials.

On the developer portal, click Documentation.

From the scroll bar on the left, scroll down and click Full API Reference .

From the options that expand below, scroll down, and click Webhooks > Create a Webhook.

Create a subscription by entering the following parameters:

name : example – Video Mesh Webhook alerts

targetUrl : example - https://10.1.1.1/webhooks

resource : videoMeshAlerts

event : triggered

ownedBy : org

The URL entered in the targetUrl parameter must be internet-accessible and have a server that is configured to accept POST requests sent by Webex Webhook.

#### Setting threshold configurations with developer APIs

You can set threshold values for the events (Org Call Overflows and Cluster Call Redirects) with Video Mesh developer APIs. You can set a percentage value for the thresholds, above which a webhook alert will be triggered. For example, if the threshold value is set to 20 for Org Call Overflows, an alert will be sent when more than 20 percent of the calls overflow to cloud.

A set of 4 APIs are available for setting and updating thresholds in the Cisco Webex Developer portal and they are listed below:

List Event Threshold Configuration

Get Event Threshold Configuration

Update Event Threshold Configuration

Reset Event Threshold Configuration

The APIs are available at https://developer.webex.com/docs/api/v1/video-mesh .

Scenario 1 - Setting threshold value for Org Calls Overflowed

Click on List Event Threshold Configuration API.

Set eventscope to ORG and click > Run .

You will receive a response similar to the one shown below.

```
{
"eventName": "orgCallsOverflowed",
"eventThresholdId":
"Y2lzY29zcGFyazovL3VzL0VWRU5ULzQyN2U5ZTk2LTczYTctNDYwYS04MGZhLTcyNWU4MWE2MDg3ZjowM2ZkYjkzZC1jNTllLT
QzMjQtODIwNS1lNDIyYzA3NGQ5Mzg",
"eventScope": "ORG",
"entityId":
"Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ",
"thresholdConfig": {
"minThreshold": 10,
"defaultMinThreshold": 10
}
```

Copy the value in the "eventThresholdId" field. This is the event threshold ID which will be used to update and get threshold values.

Paste the value in the "eventThresholdId" field of the JSON structure shown below and copy the entire JSON structure.

```
[
{
"eventThresholdId":
"Y2lzY29zcGFyazovL3VzL0VWRU5UL2E3YmM3ODE2LWU3YTAtNDk0Zi1iZDZhLTRhMGIyNWY2OGFhNjoyNWE3ODY1Yi0yYjQ3
LTM4M2YtYWI3YS00MzYxY2ExN2FiOTI",
"thresholdConfig": {
"minThreshold": 5
}
}
```

Click on Update Event Threshold Configuration API.

Paste the JSON structure in the body of Update Event Threshold Configuration API.

Set “minThreshold” value to the new threshold value that you want to set.

You can run this operation for multiple event threshold IDs by entering them as comma-separated values in the JSON structure.

Click Run , your threshold for Org Call Overflows will be set to the new value.

What to do next

If you want to view the threshold that has been set for a particular event threshold ID,

Click on Get Event Threshold Configuration API.

Paste the event threshold ID onto the header of the API, click Run .

The default minimum threshold value and the set threshold value will be displayed in the response.

Scenario 2 - Setting threshold value for Cluster Calls Redirected

Click on List Event Threshold Configuration API.

Set eventscope to CLUSTER and click > Run .

The response will list configurations of all clusters in the organization.

You can receive the configuration of a specific cluster by populating the clusterID parameter.

Copy the value in the "eventThresholdId" field of the cluster whose value you want to update. This is the event threshold ID which will be used to update and get threshold values.

Paste the value in the "eventThresholdId" field of the JSON structure shown below and copy the entire JSON structure.

```
[
{
"eventThresholdId":
"Y2lzY29zcGFyazovL3VzL0VWRU5UL2E3YmM3ODE2LWU3YTAtNDk0Zi1iZDZhLTRhMGIyNWY2OGFhNjoyNWE3ODY1Yi0yYjQ3
LTM4M2YtYWI3YS00MzYxY2ExN2FiOTI",
"thresholdConfig": {
"minThreshold": 5
}
}
]
```

Click on Update Event Threshold Configuration API.

Paste the JSON structure in the body of Update Event Threshold Configuration API.

Set “minThreshold” value to the new threshold value that you want to set.

You can run this operation for multiple event threshold IDs by entering them as comma-separated values in the JSON structure.

Click Run , your threshold for Cluster Calls Redirected will be set to the new value.

What to do next

If you want to view the threshold that has been set for a particular event threshold ID,

Click on Get Event Threshold Configuration API.

Paste the event threshold ID onto the header of the API, click Run .

The default minimum threshold value and the set threshold value will be displayed in the response.

Scenario 3 - Resetting threshold values

Click on Reset Event Threshold Configuration API.

Copy the event threshold ID of a cluster or the org and paste it in the "eventThresholdId" field of the JSON structure below.

```
{
"eventThresholdIds": [
"Y2lzY29zcGFyazovL3VzL0VWRU5ULzQyN2U5ZTk2LTczYTctNDYwYS04MGZhLTcyNWU4MWE2MDg3Zjo2YzJhZGRmMS0wYjAz
LTRiZWEtYjIxYy0xYzFjYzdiY2UwOWQ"
]
}
```

Paste the JSON structure in the body and click Run .

You can reset threshold values for multiple event threshold IDs by entering them as comma-separated values in the JSON structure.

The threshold value will be set to the default minimum value.

### Video Mesh Developer APIs

The Video Mesh Developer APIs are a way to retrieve analytics and monitoring data for your Video Mesh deployments through the Webex Developer Portal. The APIs are available at https://developer.webex.com/docs/api/v1/video-mesh . A sample client is available at https://github.com/CiscoDevNet/video-mesh-api-client .

| 1 | From the customer view in https://admin.webex.com , choose Analytics , and then click Video Mesh on the upper-right side of the screen. Hover over info to get a short description of the chart. |
|---|---|
| 2 | From the toggle on the left, choose an option to filter on how far back in time you want to show data. Last 4 Hours (Default)—When you choose this option, the graph data refreshes every 1 minute. Last 24 Hours —When you choose this option, the graph data refreshes every 10 minutes. |
| 3 | Interact with the charts by using the following options as needed: Hover over segments on the chart view to view information about that specific data point. Click legend items on the graph or overview and then click Apply to update the view on the other legend items. For example, after you select the legend item Amsterdam, the line graph updates to exclude other legend items and only include the data for the selected item. When a filter is applied, all other graphs and charts are updated to display the data of the selected filter. On a graph that shows data in a time range, narrow down to a specific time range by clicking on the left and dragging your mouse to the right. (This action affects all the related data that appears on the analytics page.) Hover over sections of a donut, lines on a graph, or insight points on a graph to view more information on the specific point in time of the data. |
| 4 | After you've filtered data in the reports, click more , and then choose a file format option, which saves a local copy of the report so you can use it offline (for example, in an internally created report): PNG PDF CSV |

| 1 | From the customer view in https://admin.webex.com , choose Analytics , and then click Video Mesh on the upper-right side of the screen. |
|---|---|
| 2 | Click a category, depending on the type of data you're looking for: Engagement Resources Bandwidth Usage Hover over info to get a short description of the chart. |
| 3 | From the drop-down on the right, choose an option to fìlter on how far back in time you want to show data. Last 7 Days (Default)—Changes the horizontal axis to every 1 hour. Last 24 Hours —Changes the horizontal axis to every 10 minutes. Last 30 Days —Changes the horizontal axis to every 3 hours. Last 90 Days —Changes the horizontal axis to every 8 hours. |
| 4 | Interact with the charts or donut graphs by using the following options as needed: Click one or more segments on the donut graph or chart view and then click Apply to update the donut view and the corresponding chart view. Choose legend items on the graph or overview to update the view on that specific legend item and then click Apply . For example, after you select the legend item On-Premises, the line graph updates with that data highlighted. When a filter is applied, all other graphs and charts are updated to display the data of the selected filter. On a graph that shows data in a time range, narrow down to a specific time range by clicking on the left and dragging your mouse to the right and leaving when the desired range is selected. (This action affects all the related data that appears on the analytics page.) Hover over sections of a donut, lines on a graph, or insight points on a graph to view more information on the specific point in time of the data. To start over from within the same graph or overview, click X on the selected filters at the bottom of the graph. |
| 5 | After you've filtered data in the reports, click more , and then choose a file format option, which saves a local copy of the report so you can use it offline (for example, in an internally created report): PDF PNG CSV |
| 6 | Clear all the filters from the filters bar if you'd like to reset the analytics view. |

| 1 | Log in to Control Hub , then go to Troubleshooting > Video Mesh . |
|---|---|
| 2 | Click on Configure Test , click Test now , then check the nodes and/or clusters you want to test. If you want to clear the boxes you've checked and restore your last configuration, click Restore last test configuration . |
| 3 | Click Run test . |

| 1 | Log in to Control Hub , then go to Troubleshooting > Video Mesh . |
|---|---|
| 2 | Click on Configure Test , click Periodic test , then check the nodes and/or clusters you want to test. |
| 3 | Choose an option: Check All Clusters if you want to run the test on all the Video Mesh nodes in  your Control Hub organization. Check the individual cluster names to run the test on all Video Mesh nodes that are in a specific cluster. Unchecked clusters are excluded from the test. Within individual clusters, check the individual node names that you want to run the test on. Any unchecked node is excluded from the test. |
| 4 | Click Next . |
| 5 | Review the list of clusters and nodes to run the periodic tests. If you are satisfied, click Configure to schedule the current configuration. |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click Settings on the Video Mesh card. |
|---|---|
| 2 | Toggle on Video Quality . If this setting is off, the default is 720p. |

| 1 | Log in to Control Hub . |
|---|---|
| 2 | Click Hybrid on the lower left side of the screen. |
| 3 | Click Edit Settings on the Video Mesh card. |
| 4 | Scroll down to Inter-Cluster Cascade . The toggle will be disabled by default. Click on the toggle to enable it. |

| 1 | Enable Inter-Cluster Cascades as detailed in the previous section. |
|---|---|
| 2 | Once enabled, all clusters of your organization will be listed in the Inter-Cluster Cascade card with a check mark next to them. |
| 3 | Exclude a cluster by deselecting the check mark next to it. By default, all clusters of your Video Mesh deployment will be selected to participate in Inter-Cluster cascades. |

| 1 | Log in to Control Hub . |
|---|---|
| 2 | Click Analytics> Video Mesh . |
| 3 | Click on the Bandwidth Usage tab. You will find Inter-Cluster Cascade reports nested under this tab. |
| 4 | Use the drop-down menus to select the two clusters between which Inter-Cluster Cascade data is needed. It is set All Clusters to All Clusters by default. |
| 5 | From the drop-down on the right, choose an option to fìlter on how far back in time you want to show data. Last 7 Days (Default)—Changes the horizontal axis to every 1 hour. Last 24 Hours —Changes the horizontal axis to every 10 minutes. Last 30 Days —Changes the horizontal axis to every 3 hours. Last 90 Days —Changes the horizontal axis to every 8 hours. |
| 6 | On a graph that shows data in a time range, narrow down to a specific time range by clicking on the left and dragging your mouse to the right and leaving when the desired range is selected. (This action affects all the related data that appears on the page.) |
| 7 | Click one or more segments on the donut graph or chart view and then click Apply to update the donut view and the corresponding chart view. (For example, you can click on Video on the Total cascaded data usage by stream chart to view data used by video stream during cascades between the selected clusters.) Hover over sections of a donut, lines on a graph, or insight points on a graph to view more information on the specific point in time of the data. To start over from within the same graph or overview, click X on the selected filters at the bottom of the graph. |
| 8 | After you've filtered data in the reports, click more , and then choose a file format option, which saves a local copy of the report so you can use it offline (for example, in an internally created report): PDF PNG CSV |
| 9 | Clear all the filters from the filters bar if you'd like to reset the analytics view. |

| Node 1 | Node 2 | Recordings | Calls |
|---|---|---|---|
| VMNLite recording node | VMNLite node | 16-18 | 160-180 |

| 1 | Log in to Control Hub . |
|---|---|
| 2 | Click Hybrid on the lower left side of the screen. |
| 3 | Click View all under Resources in the Video Mesh card. |
| 4 | The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster which you have chosen to handle On-premises Recording. |
| 5 | A page opens with the list of nodes under the cluster you selected. Click on the right end of a recording node and click Go to node . |
| 6 | Go to Server Certificates tab,  generate a CSR (optional), and upload a certificate and private key pair as needed: (Optional) If you need a certificate issued from a Certificate Authority (CA), click Create a Certificate Signing Request . Fill out the required information (including the Subject Alternative Name(s) , which are FQDNs that must contain the common name, and then generate the request. Download the CSR to submit the request to the CA. The common name is not a URL. It doesn’t include any protocol (for example http:// or https://), port number, or path name. When you generate a Certificate Signing Request (CSR), Video Mesh creates and stores the private key automatically. If you don't use the CSR creation step, you must upload a private key manually. When you have the certificate and private key, click Upload a Server Certificate (.crt or .pem file) and choose the certificate file. Ensure that you install the complete certificate chain, including the root, all intermediate, and server certificates. Click Upload a Private Key (.key file) and enter a passphrase if you have one. After you get the certificate,  click Install Server Certificate , read the prompt, click Install , then click OK . A cloud-registered Video Mesh node gracefully shuts down, waiting up to 2 hours for any calls to end. The node then completes the certificate installation. A prompt appears when the server certificate installs. You can then reload the page to view the new certificate and key entry. Click Download next to the certificate and key files to save a local copy. Save the files somewhere that's easy to remember and leave the Video Mesh instance open in the browser tab. |
| 7 | Repeat the process for all recording nodes in the cluster. |

| 1 | Log in to Control Hub . |
|---|---|
| 2 | Click Hybrid on the lower left side of the screen. |
| 3 | Click View all under Resources in the Video Mesh card. |
| 4 | The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster which you have chosen to handle On-Premises Recording. |
| 5 | A page opens with the list of nodes under the cluster you selected. Click on the right end of a node and click Go to node . |
| 6 | The node web interface opens. Click Administration on the left side of the screen. |
| 7 | Scroll down to NFS Setup . |
| 8 | Click Enable NFS . |
| 9 | Enter NFS host and path details in the fields that appear. |
| 10 | Click Mount NFS . A pop up message appears saying Successfully mounted the given NFS . |
| 11 | Repeat this process for nodes designated for recording in the cluster or clusters. |

| 1 | Log in to Control Hub . |
|---|---|
| 2 | Click Hybrid on the lower left side of the screen. |
| 3 | Click View all under Resources in the Video Mesh card. |
| 4 | The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster you have selected to handle On-Premises Recording. |
| 5 | Click on the Cluster Settings tab. |
| 6 | On the On-premises recording card, you will find the Allow on-premises recording toggle. The toggle will be disabled by default. Click on the toggle to enable it. |
| 7 | Enter the FQDN or hostname in the Recording Service name field. This will be used to download the recorded content from the nodes. Ensure that the FQDN entered in Recording Service name has a DNS entry with the IPs of the Video Mesh nodes used for recording. We recommend a round robin method to determine the node that will download the recorded content. |
| 8 | Select the nodes to be used for recording from the drop-down in the On-premises recording nodes field. |

| 1 | Schedule a meeting on Webex. |
|---|---|
| 2 | Once the meeting starts, click on the Record button. |
| 3 | If on-premises recording has been successfully enabled, you will find the Save to my org option in the Recording options drop down. |
| 4 | You can pause, resume and stop the recording as needed. |
| 5 | Once the meeting ends, the host will receive an email with a link and password. |
| 6 | Click on the link in the email, a web page opens in your browser with a field to enter the password. |
| 7 | Copy the password from the email and paste it in the Password field. Click Download . This will trigger the download of the recording file. Recordings generated through on-premises recording are currently unavailable in the Webex app and can only be accessed using the link provided in the email or from the Video Mesh node web interface. |

| 1 | Log in to Control Hub . |
|---|---|
| 2 | Click Hybrid on the lower left side of the screen. |
| 3 | Click View all under Resources in the Video Mesh card. |
| 4 | The Video Mesh Clusters page opens with all clusters in your deployment displayed as a list. Click on a cluster which you have chosen to handle On-Premises Recording. |
| 5 | A page opens with the list of nodes under the cluster you selected. Click on the right end of a node and click Go to node . |
| 6 | The node web interface opens. Click Recordings on the left side of the screen. |
| 7 | A page opens displaying all of your organization's recordings. |
| 8 | The following actions are available for Organization full administrators with compliance officer privileges : Resend Recording Link and Password : Locate the specific recording in the list. Click the Resend button associated with that recording. The system will automatically trigger an email containing the recording link and password to the current owner/host. Reassign Recording Ownership: Click the Reassign button next to the desired recording. Enter the email address of the new owner. Click Save Changes . The previous owner will receive an email notification that they are no longer the owner, and the new owner will receive an email confirming their new assignment. Download Recordings: Locate the recording in the list. Click the Download button to save a local copy of the recording. Delete Recordings: Select the recording you wish to remove. Click the Delete button. Confirm the deletion when prompted by clicking Delete Recording . This action is permanent and cannot be undone. Full Administrators may reassign ownership and resend recording links, but they cannot download or delete recordings from the list. |

| Alarm ID | Title | Severity | Description | Solution |
|---|---|---|---|---|
| mf.recordingmanager.nfsConnectivityError | Recording node lost connectivity to NFS | Critical | Recording node lost connectivity to NFS. | Verify that the NFS mount is accessible and that network connectivity is active. Review the mount configuration and firewall rules. If the issue persists, please contact Cisco support. |
| mf.recordingmanager.nfsDiskFull | NFS Utilization is critical | Critical | NFS Utilization is above 95%. | Free up NFS storage by removing old recordings or expanding storage capacity. |
| mf.recordingmanager.nfsDiskUtilizationHigh | NFS Utilization is high | Warning | NFS Utilization is above 90%. | Free up NFS storage by removing old recordings or expanding storage capacity. |
| mf.recordingmanager.unsupportedDeployment | Recording Enabled on Unsupported Deployment Type | Critical | On-premises recording is only supported on VMNLite deployments. | Please remove this node {hostname} from the list of on-premises recording nodes in the Control Hub settings. |
| mf.device.recordingUnsupportedStorage | Device storage is insufficient for recording functionality | Critical | Total disk space is {X} GB, which is below the minimum recommended storage of 250 GB for recording. | Expand disk capacity to at least 250 GB to support on-premises recording. |
| mf.device.untrustedCaCertificate | The server certificate installed on this node is not trusted. | Critical | The server certificate installed on this node is not signed by a trusted Certificate Authority. This may impact recording functionality. | The server certificate installed on this node should be signed by a trusted Certificate Authority. Please update the server certificate at: https://{hostname}/setup/#ca-certs |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid . |
|---|---|
| 2 | Click Edit settings from the Video
                        Mesh card. Scroll to Private Meetings and enable the setting. |
| 3 | Save your change. |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid and click Show all on the Video Mesh
                    card. |
|---|---|
| 2 | Select your Video Mesh cluster from the list and click Edit cluster
                        settings. |
| 3 | Scroll to Private Meetings and enable the setting. |
| 4 | Save your change. |

| Error Message | User Action | Reason |
|---|---|---|
| External Network Access Denied You need to be on the corporate network to attend the Private
                                    Meeting. Paired Webex devices located outside the corporate
                                    network would not be able to join the meeting, in such a
                                    scenario try connecting your laptop, mobile to the corporate
                                    network and join the meeting in unpaired mode. | An external user joins from outside the corporate network without
                                    VPN or MRA. | To join a private meeting, external users need access to the
                                    corporate network through a VPN or MRA. |
| An external user is on VPN, but they're paired to an
                                    unauthenticated device. | Device media doesn't tunnel to the corporate network through the
                                    VPN. The device can't join a private meeting. Instead, after connecting to VPN, the remote user should join a
                                    private meeting in device unpaired mode from their desktop or
                                    mobile client. |
| No Available Clusters The clusters hosting this private meeting are at peak capacity,
                                    unreachable, offline, or not registered. Please contact your IT
                                    admin for assistance. | A user is on the corporate network (on-premises or remote by
                                    VPN), but can’t join a private meeting. | Your Video Mesh clusters are: At capacity Unreachable Offline Not registered |
| Not Authorized You are not authorized to attend this Private meeting as you are
                                    not a member of the Host Organization. Please reach out to the
                                    Host of the meeting. | A user from a different org than the host org tries to join the
                                    private meeting. | Only users belonging to the host org can join a private
                                    meeting. |
| A device from a different org than the host org tries to join the
                                    private meeting. | Only devices belonging to the host org can join a private
                                    meeting. |

| Setting is... | Meeting on internal Webex site with Video Mesh cascades enabled | Meeting on internal Webex site with Video Mesh cascades disabled | Meeting on external Webex site with Video Mesh cascades enabled | Meeting on external Webex site with Video Mesh cascades disabled |
|---|---|---|---|---|
| Enabled | Media uses your Video Mesh nodes. | Media uses cloud nodes. | Media uses your Video Mesh nodes. | Media uses your Video Mesh nodes. |
| Disabled | Media uses your Video Mesh nodes. | Media uses cloud nodes. | Media uses your Video Mesh nodes. | Media uses cloud nodes. |

| 1 | In the customer view in https://admin.webex.com , go to Services > Hybrid and click Show all on the Video Mesh card. |
|---|---|
| 2 | Select your Video Mesh cluster in the list and click Edit settings . |
| 3 | Scroll to Prefer Video Mesh for All External Webex Meetings and enable the setting. |
| 4 | Save your change. |

| 1 | Sign in to Control Hub , then select Services > Hybrid > Video Mesh > Resources > View all . - or - Select Overview > Hybrid services > Video Mesh > Settings . |
|---|---|
| 2 | Under Client Type Inclusion Settings , all client types are checked by default. Uncheck the client types you want to exclude from using the Video Mesh clusters. These clusters are hosted on Webex cloud nodes. |
| 3 | Click Save . |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid . |
|---|---|
| 2 | Click View all on the Video Mesh card. |
| 3 | From the list of resources, go to the appropriate cluster and choose the node. |
| 4 | Click Action > Deregister Node . A message appears asking you to confirm that you want to delete the node. |
| 5 | After you read and understand the message,
                                                  click Deregister
                                                  Node . |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid , and then choose View all on the Video Mesh card. |
|---|---|
| 2 | From the list, select the node that you want to move and then click Actions (the vertical ellipsis). |
| 3 | Select Move Node . |
| 4 | Choose the appropriate radio button for where you want to move the node: Select an existing cluster —Choose an existing
                        cluster from the drop-down list. Create a new cluster —Enter a name for the new
                        cluster in the field. |
| 5 | Click Move Node . Your node moves to the new cluster. |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click View all on the Video Mesh card. |
|---|---|
| 2 | Click a media resource and then click Edit cluster settings . |
| 3 | On the Settings page,
                                                  scroll to Upgrade , and then
                                                  choose the time, frequency, and time zone for the
                                                  upgrade schedule. Upgrades may take longer than a few minutes if the Video Mesh node is waiting for active calls to end. For a more immediate upgrade process, we recommend that you schedule the automatic upgrade window outside of your regular business hours. |
| 4 | (Optional) If needed, click Postpone to defer the
                                                  upgrade one time, until the subsequent
                                                  window. Under the time zone, the next available upgrade
                                                  date and time are displayed. |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid , and then click View all . |
|---|---|
| 2 | From the list of resources, scroll to the Video Mesh resource that you want to delete, and then click Edit Cluster Settings . You can click Video Mesh to filter on just Video Mesh resources. |
| 3 | Click Delete Cluster , and then choose one: Click Move All Nodes . For each node, either
                        create a new resource by choosing an existing resource from the drop-down
                        list or entering a new name, and then click Continue . Click Deregister All Nodes , check the check box,
                        and then click Delete Cluster . |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid > View All , choose Settings on the Video Mesh card. |
|---|---|
| 2 | Click Deactivate . |
| 3 | Review the list of clusters and read the disclaimer in the dialog. |
| 4 | Check the check box to confirm that you understand this action, and click Deactivate on the dialog. |
| 5 | When you are ready to deactivate your Video Mesh, click Deactivate Service . Deactivation removes all Video Mesh nodes and clusters. Video Mesh is no longer configured. |

| 1 | From Control Hub , click Hybrid on the lower-left side of the screen. |
|---|---|
| 2 | Click Edit Settings on the Video Mesh card. |
| 3 | Scroll down to ThousandEyes Integration . The toggle will be disabled by default. Click on the toggle to enable it. |
| 4 | Click ThousandEyes User Profile , the ThousandEyes web portal opens, sign in using the admin credentials. |
| 5 | A side panel is displayed with the Account Group Token . |
| 6 | Click on the view icon and then click Copy . The token will not be copied correctly if the view token button is not clicked. |
| 7 | Go back to the Control Hub tab, paste the token in the Agent Token field. |
| 8 | Click Activate , ThousandEyes is now enabled for your Video Mesh deployment. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Network . The current network settings for the node appear. |
| 3 | Change the following settings for Host and Network Configuration as needed: Under Edit Hostname and Domain , change the Hostname and Domain values. An error is displayed if the FQDN (hostname and domain) does not have the correct format. Under Network Mode , Enable DHCP is listed, but DHCP is not supported. You must set a static IP address, subnet mask, and gateway. Under Edit Network Configuration , change the IP Address (for the internal interface), Subnet Mask , and Gateway (a network node that serves as an access point to another network) values. The  Video Mesh Node must have an internal IP address and resolvable DNS name. The node IP address must not belong to the IP address range reserved for  Video Mesh Node internal use. The default reserved IP address range is 172.17.42.0–172.17.42.63, which can be configured later in the Diagnostic menu in the node console. This IP address range is for communication within the  Video Mesh Node and between the software containers which hold the different components of the node—for example, SIP interface and media transcoding. Under Edit DNS Servers , change the DNS server entries, which handle translating domain names to numeric IP addresses. You can enter up to 4 DNS servers. |
| 4 | Click Save Host and Network Configuration , and after the popup appears that says the node needs to reboot, click Save and Reboot . During the save, all fields are validated on the server side. Warnings that appear generally indicate that the server isn't reachable or a valid response wasn't returned when queried—for example, if the FQDN is not resolvable using the DNS server addresses provided. You may choose to save by ignoring the warning but calls will not work until the FQDN can resolve to the DNS configured on the node. Another possible error state is if the gateway address is not in the same subnet as the IP address. After the  Video Mesh Node reboots, the network configuration changes take effect. |
| 5 | Change the following settings for NTP Servers as needed: Under Edit NTP Servers , change the values for the NTP server entries, which are used in your organization to synchronize time to the node. |
| 6 | Click Save NTP Servers . If you configure more than one NTP servers, the poll interval for failover is 40 seconds. If the NTP server is an FQDN and that isn’t resolvable, a warning is returned. If the NTP server FQDN is resolved but the resolved IP can't be queried for NTP time, a warning is returned. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Network . The current network settings for the node appear. |
| 3 | Click Advanced . |
| 4 | Toggle on Enable External Network and then click Ok to enable the external IP address options on the node. |
| 5 | Enter the External IP Address , External Subnet Mask , and External Gateway values. |
| 6 | Click Save External Network Configuration . |
| 7 | Click Save and Reboot to confirm the change. The node reboots to enable the dual IP address, and then automatically configures the basic static routing rules. These rules determine that traffic to and from a private class IP address uses an internal interface; traffic to and from a public class IP address uses an external interface. Later, you can create your own routing rules—For example, if you need to configure an override and allow access to an external domain from the internal interface. |
| 8 | If there are errors, click Ok to close the error dialog box, fix the errors, and click Save External Network Configuration again. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Network . The current network settings for the node appear. If you have configured the external network, the Routing Rules tab appears. |
| 3 | Click the Routing Rules tab. The first time you open this page, the default system routing rules appear in the list. By default, all internal traffic goes through the internal interface and external traffic through the external interface. You can add manual overrides to these rules in the next steps. |
| 4 | To add a rule, click Add Routing Rule , then choose one of the following option:. For Network Type , click Internal , and then enter the external subnet or host IP address to use for the internal route. For Network Type , click External , and then enter the internal subnet or host IP address to use for the external route. |
| 5 | Click Add Routing Rule . As you add each rule, they appear in the routing rule list, categorized as user defined rules. |
| 6 | To delete one or more user-defined rules, check the check box in the column to the left of the rules and then click Delete Routing Rule(s) . The default routes cannot be deleted, but you can delete any user-defined overrides that you configured. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Network . The current network settings for the node appear. |
| 3 | Click Advanced . |
| 4 | Change the values for Container IP Address and Container Subnet Mask , as needed, and then click Save Container Network Configuration . |
| 5 | Click Save and Reboot to confirm the change. |
| 6 | If there are errors, click Ok to close the error dialog box, fix the errors, and click Save Container Network Configuration again. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Network . The current network settings for the node appear. |
| 3 | Click Advanced . |
| 4 | In the Interface MTU Settings section , enter an MTU value between 1280 and 9000 bytes in the applicable field(s). If you have enabled the external interface, you can set both the internal and external interface MTU sizes separately. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Network . The current network settings for the node appear. |
| 3 | Click Advanced . |
| 4 | In the DNS Caching Configuration section, toggle Enable DNS Caching on or off. |
| 5 | In the confirmation dialog, click Save and Reboot . |
| 6 | After the node reboots, reopen the Webex Video Mesh node interface and confirm that the connectivity checks are succeeding on the Overview page. |

| Statistic | Description |
|---|---|
| Cache Entries | The number of previous DNS resolutions that the DNS Cache server
                                    has stored |
| Cache Hits | The number of times since the cache reset that the cache handled
                                    a DNS request from Video Mesh, without querying the customer DNS
                                    server |
| Cache Misses | The number of times since the cache reset that the customer DNS
                                    server handled a DNS request from Video Mesh rather than through
                                    the cache |
| Cache Hit Percent | The percent of DNS requests from Video Mesh that the cache
                                    handled without querying the customer DNS server |
| Cache Server Outbound DNS queries | The number of DNS queries that the Video Mesh DNS cache server
                                    made against the customer DNS servers |
| Cache Server Inbound DNS queries | The number of DNS queries that Video Mesh made against its
                                    internal DNS Cache server |
| Outbound to Inbound Query Ratio | The ratio of DNS queries made by Video Mesh against the customer
                                    DNS server to the queries made by Video Mesh against its
                                    internal DNS Cache server |
| Inbound Queries Per Second | The average number of DNS queries per second that Video Mesh made
                                    against its internal DNS Cache server |
| Outbound Queries Per Second | The average number of DNS queries per second that Video Mesh made
                                    against the customer DNS servers |
| Outbound DNS Latency [time range] | The percent of DNS queries that Video Mesh made against the
                                    customer DNS servers where the response time fell into the
                                    described time range |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | When setting up TLS with another server, such as a syslog server , we recommend for security reasons that you use a CA signed certificate
                    on your Video Mesh nodes instead of the node's default self-signed certificate.
                    To create and upload the certificate and key pairs on the Video Mesh node, go to Server Certificates , and follow these steps: If you need a certificate issued from a certified
                            provider, click Create a Certificate Signing
                                Request . Fill out the required information (including
                            the Subject Alternative Name(s) , which are FQDNs
                            that must contain the common name). Then, generate and download the CSR
                            to submit the request to the provider. You can create multiple CSRs. The
                            provider returns the certificate authority (CA) signed certificate. (The
                            CSR creation step already generated the private key.) The common name is not a URL. It doesn’t include any protocol
                                    (e.g. http:// or https://), port number, or pathname. The commonName field in the X.509 certificate
                                    specification technically represents the common name. For https://www.example.com , the correct value
                                    is example.com . When you have the certificate and key, click Upload a Server
                                Certificate (.crt or .pem file) , choose the certificate
                            file, then click Upload a Private Key (.key file) and enter a passphrase if you have one. The private key is already in place when a CSR is generated. You only
                                need to upload a private key if you do not use the CSR creation
                                step. After you get the certificate, go to the first Video Mesh node in a
                            cluster, click Install Server Certificate , read
                            the prompt, click Install , then click OK . A Video Mesh node that's registered to the cloud waits up to 2 hours
                                for any calls to end and puts itself into a temporary inactive state
                                (quiesces). Once either the existing calls finish or 2 hours pass
                                (whichever comes first), this node completes the certificate
                                installation. A prompt appears when the server certificate
                                installation completes, and you can then reload the page to view the
                                new certificate and key entry. Click Download next to the certificate and key
                            files to save a local copy. Save the files somewhere that's easy to remember and leave the
                                instance open in the browser tab. Go to the second Video Mesh node in the cluster, fill in the
                            passphrase, and then upload the private key file. Then click Upload a Server Certificate and then choose Install Server Certificate , read the prompt,
                            click Install , then click OK . Repeat these steps on every other Video Mesh node in the same
                            cluster. |
| 3 | Choose an option depending on how the external server's CA certificate is signed: If the server's CA certificate is signed by a generally recognized
                        organization, such as DigiCert, GeoTrust, or GlobalSign, the Video Mesh node
                        will trust it based on the list of root certificates from the Video Mesh
                        node's host OS, which are updated periodically. Skip to Step 6 . If the server's CA certificate is signed by an internal enterprise CA root certificate, the root certificate from that authority must be added to the Video Mesh node. Continue with the next step. |
| 4 | Get the certificate or certificate trust list (CTL) that the external server
                    uses. As with the Video Mesh node certificate, save the external server file
                        somewhere that's easy to remember. |
| 5 | Go back to the Webex Video Mesh node interface tab, click Trust Store & Proxy , then choose an option: To install a single CA certificate, click Upload a Root Certificate or End Entity Certificate (.crt or .pem file) , and then choose the certificate file from your computer, click Install All Certificates into the Trust Store , read the prompt, click Install , and then reboot the node. To install a certificate chain, upload the root CA certificate and intermediate CA certificate, and then click Install All Certificates into the Trust Store , read the prompt, and then click Install . A Video Mesh node that's registered to the cloud waits up to 2 hours for any calls to end and puts itself into a temporary inactive state (quiesces). To install the certificate, the node must reboot and does so automatically. When it comes back online, a prompt appears when the certificate is installed on the Video Mesh node, and you can then reload the page to view the new certificate. |
| 6 | Repeat the certificate or certificate chain upload on every other Video Mesh
                    node in the same cluster. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Troubleshooting , and then choose an option next to Send Logs : Click Send Logs to Cisco to generate a log bundle from the node and send the bundle directly to Cisco in one step. You'll see a status indicator that changes as the logs are compressed, zipped, and uploaded. Click Download to generate a long bundle from the node that you can save locally or attach to a case later. Generated logs are historically stored on the node and remain on the node even after reboots. An upload identifier shows on the page. Support uses this value to identify your uploaded logs. |
| 3 | When you open a case or interact with the Cisco TAC , include the upload identifier value so that your support engineer can access the logs. If you submitted the log to Cisco directly, you don't need to upload the log bundle to the TAC case. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Troubleshooting . You can start the packet capture and upload logs at the same time. |
| 3 | (Optional) In the Packet Capture section, you can limit the capture to packets on a  specific interface, filter by packets to or from specific hosts, or filter by packets on one or more ports. |
| 4 | To begin the process, toggle on the Start Packet Capture setting. |
| 5 | When you are done, toggle off the Start Packet Capture setting. |
| 6 | Choose one: Click Send PCAP to Cisco to send the packet capture from the node directly to Cisco. You'll see a status indicator that changes as the packet capture is uploaded. Click Download to save a local copy of the packet capture from the node. You can attach it to a case later. After a package capture is uploaded, an upload identifier shows on the page. Support uses this value to identify your uploaded packet capture. The maximum size for packet captures is 2 GB. |
| 7 | When you open a case or interact with the Cisco TAC , include the upload identifier value so that your support engineer can access the packet capture. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Troubleshooting , scroll to Ping , and then enter a destination address that you want to test in the FQDN or IP Address field under Test Connectivity Using Ping . |
| 3 | Click Ping . The test runs and you'll see a ping success or failure message. The test does not have a timeout limit. If you receive a failure or the test runs indefinitely, check the destination value that you entered and your network settings. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Troubleshooting , scroll to Traceroute , and then enter a destination address that you want to test in the FQDN or IP Address field under Trace Route to Host . The test runs and you'll see trace route success or failure message. The test times out at 16 seconds. If you receive a failure or the test times out, check the destination value that you entered and your network settings. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Troubleshooting , scroll to Check NTP Server , and then enter a destination address that you want to test in the FQDN or IP Address field under View SNTP Query Response . The test runs and you'll see a query success or failure message. The test does not have a timeout limit. If you receive a failure or the test runs indefinitely, check the destination value that you entered and your network settings. |

| 1 | From the customer view in https://admin.webex.com , enable maintenance node for the Video Mesh Node by following these instructions . |
|---|---|
| 2 | Wait for the node to show a 'Ready for maintenance' status in Control Hub. |
| 3 | Open the Webex Video Mesh node interface. For instructions, see Manage Video Mesh Node From the Web Interface . |
| 4 | Scroll to Reflector Tool , and then start either the TCP Reflector Server or UDP Reflector Server , depending on what protocol you want to use. |
| 5 | Click Start Reflector Server , and then wait for the server to start successfully. You'll see a notice when the server starts. |
| 6 | From a system (such as a PC) on a network that you want Video Mesh nodes to reach, run the script with the following command: $ python <local_path_to_client_script>/reflectorClient.py --ip <ip address of the server> --protocol <tcp or udp> At the end of the run, the client shows a success message if all the required ports are open: The client shows a failed message if any required ports are not open: |
| 7 | Resolve any port issues on the firewall and then rerun the above steps. |
| 8 | Run the client with --help to get more details. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Troubleshooting , and then toggle on the Enable Debug User setting. An encrypted passphrase appears that you can provide to Cisco TAC. |
| 3 | Copy the passphrase, paste it in the support ticket or directly to the support engineer, and then click OK when you have it saved. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Troubleshooting , scroll to Factory Reset , and then click Reset Node . |
| 3 | Ensure that you understand the information in the warning prompt that appears, and then click Reset and Reboot . The node reboots automatically after the factory reset. |

| 1 | From the customer view in https://admin.webex.com , go to Services > Hybrid . |
|---|---|
| 2 | Under Resources on the Video Mesh card, click View all . |
| 3 | Click on the cluster and then click on the node that you want to access. Click Go to Node . |
| 4 | Go to Administration . |
| 5 | Toggle the Enable Admin User Sign In switch off to disable the account, or on to re-enable it. You can't disable the admin account until you've registered the node to the cloud. |
| 6 | On the confirmation screen, click Disable or Enable to complete the change. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Administration , and next to Change Passphrase , click Change . |
| 3 | Enter the Current Passphrase , and then enter a new passphrase value in both New Passphrase and Confirm New Passphrase . |
| 4 | Click Save Passphrase . A "password changed" message appears and then you go back to the sign in screen. |
| 5 | Sign in using your new admin login and passphrase (password). |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Administration , and next to Change Passphrase Expiry , enter a new value for Expiry Interval (Days) (up to 365 days), and then click Save Passphrase Expiry Interval . A success screen appears, and you can then click OK to finish. |

| 1 | Open the Webex Video Mesh node interface. |
|---|---|
| 2 | Go to Administration . |
| 3 | Next to External Logging , toggle on Enable External Logging . |
| 4 | For Syslog Server Details , enter the host IP address or fully-qualified domain name and the syslog port. If the server isn’t DNS-resolvable from the node, use an IP address in the Host field. |
| 5 | Choose the Protocol —UDP or TCP. To use TLS encryption, choose TCP and then toggle on Enable TLS . Make sure that you also upload and install the security certificates required for TLS communication between the node and the syslog server. If no certificates are installed, the node defaults to using its self-signed certificates. For help, see Upload Security Certificates . |
| 6 | Click Save External Logging Configuration . |

| Property | Description |
|---|---|
| Priority | The value is always 131, based on the formula: Priority = (Facility Code * 8) + Severity. The facility code is 16 for "local0". The severity is 3 for "notice". |
| Timestamp | The timestamp format is "Mmm dd hh:mm:ss". |
| Hostname | The hostname for the Video Mesh node. |
| Tag | The value is always syslogAuditMsg. |
| Message | The message is a JSON string of at least 1KB. Its size depends on the number of aggregated events in the ten minute interval. |

| 1 | Log in to the Cisco Webex Developer portal using admin credentials. |
|---|---|
| 2 | On the developer portal, click Documentation. |
| 3 | From the scroll bar on the left, scroll down and click Full API Reference . |
| 4 | From the options that expand below, scroll down, and click Webhooks > Create a Webhook. |
| 5 | Create a subscription by entering the following parameters: |

| 1 | Click on List Event Threshold Configuration API. |
|---|---|
| 2 | Set eventscope to ORG and click > Run . |
| 3 | You will receive a response similar to the one shown below. {
"eventName": "orgCallsOverflowed",
"eventThresholdId":
"Y2lzY29zcGFyazovL3VzL0VWRU5ULzQyN2U5ZTk2LTczYTctNDYwYS04MGZhLTcyNWU4MWE2MDg3ZjowM2ZkYjkzZC1jNTllLT
QzMjQtODIwNS1lNDIyYzA3NGQ5Mzg",
"eventScope": "ORG",
"entityId":
"Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ",
"thresholdConfig": {
"minThreshold": 10,
"defaultMinThreshold": 10
} |
| 4 | Copy the value in the "eventThresholdId" field. This is the event threshold ID which will be used to update and get threshold values. |
| 5 | Paste the value in the "eventThresholdId" field of the JSON structure shown below and copy the entire JSON structure. [
{
"eventThresholdId":
"Y2lzY29zcGFyazovL3VzL0VWRU5UL2E3YmM3ODE2LWU3YTAtNDk0Zi1iZDZhLTRhMGIyNWY2OGFhNjoyNWE3ODY1Yi0yYjQ3
LTM4M2YtYWI3YS00MzYxY2ExN2FiOTI",
"thresholdConfig": {
"minThreshold": 5
}
} |
| 6 | Click on Update Event Threshold Configuration API. |
| 7 | Paste the JSON structure in the body of Update Event Threshold Configuration API. |
| 8 | Set “minThreshold” value to the new threshold value that you want to set. |
| 9 | You can run this operation for multiple event threshold IDs by entering them as comma-separated values in the JSON structure. Click Run , your threshold for Org Call Overflows will be set to the new value. |

| 1 | Click on List Event Threshold Configuration API. |
|---|---|
| 2 | Set eventscope to CLUSTER and click > Run . |
| 3 | The response will list configurations of all clusters in the organization. |
| 4 | You can receive the configuration of a specific cluster by populating the clusterID parameter. Copy the value in the "eventThresholdId" field of the cluster whose value you want to update. This is the event threshold ID which will be used to update and get threshold values. |
| 5 | Paste the value in the "eventThresholdId" field of the JSON structure shown below and copy the entire JSON structure. [
{
"eventThresholdId":
"Y2lzY29zcGFyazovL3VzL0VWRU5UL2E3YmM3ODE2LWU3YTAtNDk0Zi1iZDZhLTRhMGIyNWY2OGFhNjoyNWE3ODY1Yi0yYjQ3
LTM4M2YtYWI3YS00MzYxY2ExN2FiOTI",
"thresholdConfig": {
"minThreshold": 5
}
}
] |
| 6 | Click on Update Event Threshold Configuration API. |
| 7 | Paste the JSON structure in the body of Update Event Threshold Configuration API. |
| 8 | Set “minThreshold” value to the new threshold value that you want to set. |
| 9 | You can run this operation for multiple event threshold IDs by entering them as comma-separated values in the JSON structure. Click Run , your threshold for Cluster Calls Redirected will be set to the new value. |

| 1 | Click on Reset Event Threshold Configuration API. |
|---|---|
| 2 | Copy the event threshold ID of a cluster or the org and paste it in the "eventThresholdId" field of the JSON structure below. {
"eventThresholdIds": [
"Y2lzY29zcGFyazovL3VzL0VWRU5ULzQyN2U5ZTk2LTczYTctNDYwYS04MGZhLTcyNWU4MWE2MDg3Zjo2YzJhZGRmMS0wYjAz
LTRiZWEtYjIxYy0xYzFjYzdiY2UwOWQ"
]
} |
| 3 | Paste the JSON structure in the body and click Run . |
| 4 | You can reset threshold values for multiple event threshold IDs by entering them as comma-separated values in the JSON structure. The threshold value will be set to the default minimum value. |