---
doc_id: help-webex-com-en-us-article-npgz5ph-media-health-monitoring-for-video-mesh-7ed1d0701b
source_url: https://help.webex.com/en-us/article/npgz5ph/Media-Health-Monitoring-for-Video-Mesh
retrieved_at: 2026-11-02T12:58:11.717162+00:00
---

## Monitoring Tool for Video Mesh

The Monitoring tool in Control Hub helps your organization in monitoring the health of your Video Mesh deployment. You can run the following tests on your Video Mesh nodes, clusters, or both to get results for specific parameters.

Signaling Test - Tests whether SIP signaling and media signaling occurs between the Video Mesh node and Webex cloud media services.

Cascade Test - Tests whether a cascade can be established between the Video Mesh node and Webex cloud media services.

Reachability Test - Tests whether the Video Mesh node can reach the destination ports for media streams in Webex cloud media services. It also tests if the Video Mesh node is able to communicate with the cloud clusters associated with media containers through those ports.

When you run a test, the tool creates a simulated meeting. After the test finishes, you see a simple pass or fail result with inline troubleshooting tips in the report. You can schedule the test to run periodically or run the test on demand. For more information, see Media Health Monitoring for Video Mesh .

## Run an immediate test

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

## Configure periodic tests

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

## Disable a Monitoring Tool test

Log in to Control
            Hub , then go to Troubleshooting .

In the Video Mesh section, choose View
            Details next to Monitoring Tool .

Mouse over or click Configure Test , and then click Hourly .

Uncheck the test that you want to disable, and choose Next .

Click Configure .

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

| 1 | Log in to Control
            Hub , then go to Troubleshooting . |
|---|---|
| 2 | In the Video Mesh section, choose View
            Details next to Monitoring Tool . |
| 3 | Mouse over or click Configure Test , and then click Hourly . |
| 4 | Uncheck the test that you want to disable, and choose Next . |
| 5 | Click Configure . |

## Figuras

![Results page for Troubleshooting in the monitoring tool overview page in the Video Mesh Troubleshooting tab of Control Hub.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/450001-460000/451001-452000/451810.jpg)

![Monitoring results for troubleshooting video mesh page displays results in a side panel and split into Signaling, Cascasde and Reachabilty.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472870.jpg)