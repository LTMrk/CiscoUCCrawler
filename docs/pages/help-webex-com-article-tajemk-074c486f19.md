---
doc_id: help-webex-com-article-tajemk-074c486f19
source_url: https://help.webex.com/article/tajemk
retrieved_at: 2026-09-01T18:53:50.734240+00:00
---

### Understanding Report Configuration Flows

Before you proceed to generate your report, it is important to understand how your
        configuration choices impact the report structure. Please review the following design
        considerations to ensure your report is set up for your intended analysis.

- Value Based Report: Triggered by selecting "Value of" in the first profile
            variable formula. This disables Row/Column segments.

- Aggregate Report: Triggered by adding a Row or Column segment first. This hides
            the "Value of" option in profile variable formulas.

Best Practice: Before building your report, determine whether you require a
        value-based calculation or a aggregated view. If you find that the option you need is
        missing, you may need to remove your current segments (to access "Value of") or remove the
        "Value of" variable (to access segment options).

### Run a Visualization

To run a visualization:

Click the Visualization icon on the navigation bar.

To find a report, you may use either the Search function or the (tree) icon. When you click on the tree icon, all files in that folder are displayed. Search displays all the matching reports from the subfolders as well.

When you click on a folder or a report, the exact location of the folder or the report is displayed on the breadcrumb.

On the report, click the (ellipsis) button and select the Run option or double-click to run.

By default, you can view a set of stock reports. To edit a report, you can create a copy of the report by clicking Save As to save it in your folder. For more information, see Stock Reports .

You cannot run a report that has a long duration and less interval. Reset the Duration and Interval fields as required for real-time and historical reports to proceed further. For more information, see Create a Visualization .

If the copied report has more than 1000 filter values, an error message appears when you run the report. If you see an error message such as This view shows records to accommodate a max of 1000 filter values. Please edit the report to select predefined values , edit the report to remove a few values from the filter. The report accommodates only 1000 values.

After the visualization is rendered, click the (navigation) icon to see the data summary of the visualization.

You can see the last refreshed time of the visualization data in the Data Summary tab.

If you’re running a visualization with multiple modules (compound visualization), the Data Summary tab displays a drop-down list of all the modules in the visualization so that you can display the details of each individual module.

Click the Details tab to display the following settings and panels. Click a panel title to expand or collapse the panel. If you are running a compound visualization, the details are displayed separately, depending on which module is selected in the drop-down list at the top of the tab.

Start Time : Indicates the start time of  a historical visualization, or Realtime in the case of a real-time visualization.

Compute : Specifies Duration and Refresh Rate of a real-time visualization. Possible values for Duration:

None: Provides a view of the current activity.

5, 15, or 30 minutes: Provides a view of all activities that occurred from up to 30 minutes ago to the current moment.

Start of Day: Provides a view of all activities that occurred since midnight.

Compute specifies the compute interval and the number of records to be considered in a time-based historical visualization.

Compute specifies the frequency, band, and whether the calculations are cumulative for a sample-based visualization. For more information, see Create a Visualization .

If filters are applied to any field, an extra panel is displayed for each field so that you can see the values that have been filtered in or out of the visualization.

Click Settings to display the segments and variables associated with the visualization.

You can also change the Output Type .

You can now choose KPI Card as one of the output type. Only the first
                            profile variable is used when rendering a KPI Card. If multiple metrics
                            are present, the system uses only the first visible profile variable as
                            the metric.To refer the possible output format types, see Change the Visualization Output Format .

If the visualization is in a chart format:

The underlying table used to construct the chart is displayed beneath the chart. Click the Hide Table link to hide the table, and the Show Table link to display it.

Rest your pointer over a bar, line, slice, area, or bubble in the chart to display information about the segment that the item represents.

If the visualization is historical, you can click the Export button on the title bar to export the visualization as a Microsoft Excel or CSV file. Real-time and compound visualizations cannot be exported.

You cannot export a visualization Historical Report if it has more than 2000 columns.

### Stock Reports

Analyzer provides a set of stock reports that allow you to view real-time data or historical data. To view these read-only reports, navigate to Visualizations .

Consider the following:

When you query the data, the query is in the Tenant Time Zone. The Data shows as per the Browser Time Zone. After running the report, the report shows the Browser Time Zone at the top-right corner of the report page.

In addition to the existing formats, the Duration field now has two new formats: HH:MM:SS.SSS and MM:SS.SSS. Select the appropriate format to see the data in millisecond format.

For example:

If the duration is 200 milliseconds,

and the format is HH:MM:SS.SSS, then the value is 00:00:00.200.

and the format is MM:SS.SSS, then the value is 00:00.200.

If the duration is 1001 milliseconds,

and the format is HH:MM:SS.SSS, then the value is 00:00:01.001.

and the format is MM:SS.SSS, then the value is 00:01.001.

Analyzer supports reporting for up to 13 months from the current date. This duration limit applies to all reports supported by Analyzer, including the availability of call recordings.

You need to consider the following points to copy a stock report:

- The Tenant ID in the report should be set to 0.

- You should have permission to edit.

- It should not be a custom report.

- The report type should not be a card.

- The data source for the report should be Tidelite.

- The default row limit for a report-type grid is 100,000.

No data available to render the visualization.

Failed to load Visualization.

Report limit reached. Apply filters to the data and retry.

Cardinality operations on various types of records, such as CSR, ASR, CAR, CLR, and AAR, provide only approximate values.

The option to set a custom Start Day of the Week is available for custom reports only and doesn’t apply to predefined stock reports.

Timepicker

Currently, when generating an Analyzer report, the shortest available report duration is either Today or Yesterday , leading to reports covering the entire day rather than a specific time interval within today or yesterday.

With the introduction of the Timepicker feature, Analyzer now enables users to create reports for shorter andmore specific time spans, providing granular data insights. Users can use this feature to create reports for aspecific time span within a day or a date range.

The Custom Duration filter now includes a Timepicker with a date and time range. Users can select a startand end date as well as a start and end time, offering precise control over their data selection. It is not mandatoryto select a start and end time, users can create reports by only specifying dates too.

Timepicker offers time selection in 15-minute increments, allowing users to choose the exact time periodsthey require. The earliest available time is 00:00 (start of the day), and the last available time is 23:45 (end of the day) within a 24-hour time span.

When you need a report for a specific day, the recommended method is to select just that day in the report filters; this will show the complete data for the entire day.

If you require a report for a specific time window within a day (for example, a 12-hour window starting at 10 PM), you can set the desired start and end times accordingly.

Known Issue: If you attempt to generate a report for a full 24-hour period (from 12:00 AM to 12:00 AM), you may notice that the system allows you to select an end time of 00:00 by choosing the next day as the end date. This results in the report including data from the following day as well, because the system's latest selectable end time is 23:45.

Workaround: To avoid including unwanted data from the next day, apply a filter directly on the date-time column or field in your report. Set the exact end time using a fly filter to ensure you display only the intended data.

This workaround is applicable to reports where the end time is set to 00:00.

Selecting 00:00 as the end time by choosing the next day will include the next day's data. Always use the date-time filter to specify your precise end time.

Timepicker is available for both stock and custom reports, as well as during report scheduling.

Supported Intervals for Duration

When a user runs a report and selects a particular duration period, the interval drop-down provides the following supported intervals:

The duration categories and their supported intervals based on the date difference are as follows:

If the date difference is less than or equal to 1 day, the Duration is categorized as Today , with supported intervals of 15 minutes, 30 minutes, Hourly, and Daily.

If the date difference is less than or equal to 7 days, the Duration is categorized as This Week , with supported intervals of 30 minutes, Hourly, and Daily.

If the date difference is less than or equal to 31 days, the Duration is categorized as This Month , with supported intervals of Daily and Weekly.

For any date difference greater than 31 days, the Duration is categorized as This Year , with supported intervals of Daily, Weekly, and Monthly.

#### Business Metrics

##### Usage Report

The Usage Report shows the count of agents who have logged in for each site, month, and day. The report also provides a concurrent count of agents who have logged in.

You can't modify or update this report.

Report Path : Stock Reports > Business Metrics > Usage Report

Output Type : Table

#### Historical Reports

##### Agent Reports

###### Agent Details

The Agent Details report is used to display agent statistics. This report is available in Analyzer reports and in APS reports on Agent Desktop.

The Sudden Disconnected Count field is currently not used and will not be populated.

Report Path : Stock Reports > Historical Reports > Agent Reports

Output Type : Table

Used As : Row Segment

Multimedia Profile Type

Shows the type of blended profile configured for the agent. The blended profile types are Blended, Blended Real-time, and Exclusive.

Used As : Row Segment

Shows the total number of logins in which contacts of a specific channel type were configured for the agent.

Count of Agent Channel ID

Sum of Realtime Update Timestamp - Sum of Login Timestamp

The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent.

The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent.

Shows the number of times an agent transferred inbound contacts to another agent after consult.

Shows the number of times the agent went into the Engaged state.

Sum of Engaged Count

Shows the total amount of time an agent was engaged.

Sum of Engaged Duration

Shows the average engaged duration.

Sum of Engaged Duration / Sum of Engaged Count

Click the Skill Profile or Skills table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. You can see the following details:

Login/Skill-Update Time

Shows the next login date and time for an agent whose skill profile/skills were updated when logged out, or the date and time when the skill profile/skills were updated for an agent who is currently logged in.

Skill Profile

Shows the name of the skill profile that is associated with an agent.

Skills

Shows the skill of an agent, such as language fluency or product expertise. The column shows multiple skills mapped to the corresponding skill profile, in a comma-separated single string.

###### Agent Summary Report - ASR

This report provides comprehensive insights into the agent's workload and performance metrics. It helps you evaluate the effectiveness of the wellness feature within your organization.

Output Type : Table

Report Path : Stock Reports > Historical Reports > Agent Reports

Parameters available in the table:

Parameter

Description

Agent Name

The name of the agent.

Used As : Row Segment

Calls Handled

Number of calls that were connected to an agent.

- If the agent established a conference with another agent, the value increases by one for the conferenced agent.

- If the agent transferred a call and the call was transferred back to the agent, the value increases by two.

Average of Hold Duration

Average time that an agent was engaged after disconnecting or transferring a call.

Average of Wrapup Duration

Maximum time that an agent was engaged after disconnecting or transferring a call.

Maximum Wrapup Duration

###### Auto CSAT

This report helps review the CSAT scores of all customer interactions.

Output Type : Table

Report Path : Stock Reports > Historical Reports > Agent Reports

Used As : Row Segment

Used As : Row Segment

###### Contacts Handled by Agents - Chart

This report represents the number of contacts handled by an agent. You can filter data by contact type.

Report Path : Stock Reports > Historical Reports > Agent Reports

Output Type : Bar Chart

Media Type

Description

Formula

Voice

The media type of the  telephony contact.

Count of Connected Count (Channel Type = telephony) + Count of Outdial Connected Count (Channel Type = telephony)

Chat

The media type of the chat  contact.

Count of Connected Count (Channel Type = chat)

Email

The media type of the email contact.

Count of Connected Count (Channel Type = email) + Count of Outdial Connected Count (Channel Type = email)

###### Agent Outdial Statistics

This report represents the number of outdial calls made by an agent.

Report Path : Stock Reports > Historical Reports > Agent Reports

Output Type : Table

Parameter

Description

Formula

Agent Name

The name of an agent, that is, a person who handles customer calls.

Used As : Row Segment

Time period for which the outdial call information is available.

Channel Type

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Initial Login Time

The date and time when the agent logged in for the first time during the interval.

Outdial Contact Handled

The number of outbound calls that the agent handled.

Sum of Outdial Connected Count

Outdial Average Handle Time

The average handle time for outbound calls.

(Sum of Outdial Connected Duration +  Sum of Outdial Wrapup Duration) / Sum of Outdial Connected Count

Outdial Connected Time

The total duration for which the agent was in conversation with the customer on the outdial call, this includes outdial hold duration.

Sum of Outdial Duration

Outdial Average Connected Time

The average outdial connected time.

Outdial Connected Time / Outdial Contact Handled

Outdial Talk Time

The total duration for which the agent was in conversation with the customer on the outdial call.

Outdial Connected Time - Outdial Hold Duration

Number of Transfers

The number of times the calls were transferred.

Average Consult Talk Duration

The average duration for which the agent consulted with another agent or a third party, keeping the caller on hold.

Total Consult Duration / Total Consult Count

Click any table cell except the Average Consult Talk Duration table cell to see the Drill Down icon. Select the Number of Transfers table cell, click the Drill Down icon to launch the Drill Down modal dialog. The Drill Down modal dialog displays the records involved in the computation of the visualization. You can see the following details:

Parameter

Description

Formula

Call Transfer Time

The time at which the call got transferred.

Transfer Type

The type of transfer such as Blind Transfer and Consult Transfer.

Transferred to Number

The number to which the call was transferred.

Transferred to Queue

The queue to which the call was transferred.

Consult Talk Duration

The duration for which the agent consulted with another agent or a third party, keeping the caller on hold.

To add a new column in the report, you can select the appropriate CSR Fields and Measures from the drop-down list on the left side of the Drill Down modal dialog. You can export the Drill Down report in Microsoft Excel format or CSV format to a preferred location. To view the Drill Down modal dialog in a separate window, click the Launch icon.

The Number of Transfers and Average Consult Talk Duration columns are available in the My Outdial Stats–Historic report of the APS reports in Agent Desktop. The Drill Down functionality does not apply to the APS reports in Agent Desktop.

###### Agent Statistics

This report represents the statistics of an agent.

Report Path : Stock Reports > Historical Reports > Agent Reports

Output Type : Table

Parameter

Description

Formula

Agent Name

The name of an agent, that is, a person who answers customer calls.

Used As : Row Segment

Channel Type

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Login Time

The date and time when the agent logged in.

Minimum Login Timestamp

Handled

The total number of interactions handled.

Handled = Sum of Outdial Connected Count + Sum of Post Call Duration + Sum of Connected Count

Total Handle Time

The cumulative amount of time spent handling calls.

Total Handle time = (Sum of Connected Duration  + Sum of Wrapup Duration) + (Sum of Outdial Connected Duration + Sum of Outdial Wrapup)

Click the Skill Profile or Skills table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. You can see the following details:

Shows the next login date and time for an agent whose skill profile/skills were updated when logged out, or the date and time when the skill profile/skills were updated for an agent who is currently logged in.

Skill Profile

Shows the name of the skill profile that is associated with an agent.

Skills

Shows the skill of an agent, such as language fluency or product expertise. The column shows multiple skills mapped to the corresponding skill profile, in a comma-separated single string.

###### Agent Wellness Breaks

This report provides comprehensive insights into the number of wellness breaks provided to agents. It helps you evaluate the effectiveness of the wellness feature within your organization.

Output Type : Table

Report Path : Stock Reports > Historical Reports > Agent Reports

Used As : Row Segment

###### Dropped call summaries

This report helps to understand the occurrence of dropped calls and the value of the dropped call summary.

Output Type : Table

Report Path : Stock Reports > Historical Reports > Agent Reports

Used As : Row Segment

Used As : Row Segment

- Agent left

- Customer Busy

- Customer Left

- Customer Unavailable

- Not Found

- Participant Invite Timer Expired

###### Site

This report provides a detailed view of number of agent statistics in each site.

The Sudden Disconnected Count field is currently not used and
                will not be populated.

Report Path : Stock Reports > Historical Reports > Agent Reports

Output Type : Table

Parameter

Description

Formula

Site Name

The call center location to which a call was distributed.

Used As : Row Segment

Last 7 Days

Channel Type

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Contact Handled

The total number of contacts handled.

Sum of Connected Count + Sum of Outdial Connected Count

Staff Hours

The total amount of time agents were logged in.

Sum of Realtime Update Timestamp - Sum of Login Timestamp

Occupancy

The measure of time agents spent on calls compared to available and idle time.

((Sum of Connected Duration + Sum of Wrapup Duration) + (Sum of Outdial Connected Duration + Sum of Outdial Wrapup Duration)) / (Maximum Logout Timestamp - Minimum Login Timestamp)

Idle Count

The number of times agents went into the Idle state.

Sum of Idle Count

Total Idle Time

The total amount of time agents spent in the Idle state.

Sum of Idle Duration

Average Idle Time

The average length of time agents were in the Idle state.

Sum of Idle Duration / Sum of Idle Count

Available Count

The number of times agents went into the Available state.

Sum of Available Count

Total Available Time

The total amount of time agents spent in the Available state.

Sum of Available Duration

Average Available Time

The average length of time agents were in the Available state.

Sum of Available Duration / Sum of Available Count

Inbound Reserved Count

The number of times agents went into the Inbound Reserved state.

Sum of Inbound Reserved Count

Ringing Duration

The total number of times agents spent in the Reserved state (time
                                duration after a call comes in to an agent’s station but is not yet
                                answered).

Sum of Ringing Duration

Inbound Reserved Total Time

The total number of times agents spent in the Reserved state (time
                                duration after a call comes in to an agent’s station but is not yet
                                answered).

Sum of Inbound Reserved Duration

Average Inbound Reserved Time

The average length of time agents were in the Inbound Reserved
                                state.

Sum of Ringing Duration / Sum of Ringing Count

Inbound Hold Count

The number of times agents put inbound callers on hold.

Sum of Hold Count

Inbound Hold Time

The total amount of time the inbound calls were on hold.

Sum of Hold Duration

Average Inbound Hold Time

The average hold time for inbound calls.

Sum of Hold Duration / Sum of Hold Count

Inbound Connected Count

The number of inbound calls that were connected to agents.

Sum of Connected Count

Inbound Connected Total Time

The total amount of time agents were talking to customers on inbound calls. Inbound Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time.

Sum of Connected Duration

Inbound Contact Total Time

The total amount of time agents were connected to inbound calls.

Sum of Connected Duration + Sum of Hold Duration

Average Inbound Contact Total Time

The average inbound connected time.

(Sum of Connected Duration + Sum of Hold Duration) / Sum of Connected Count

Outdial Reserved Count

The number of times agents were in the Outdial Reserved state (time duration after a call is ringing and before a call is answered).

Sum of Outdial Ringing Count

Outdial Reserved Total Time

Sum of Outdial Ringing Duration

Average Outdial Reserved Time

The average amount of time agents were in the Outdial Reserved state.

Sum of Outdial Ringing Duration / Sum of Outdial Ringing Count

Outdial Hold Count

The number of times agents put outdial calls on hold.

Sum of Outdial Hold Count

Outdial Total Hold Time

The total amount of time the outdial calls were on hold.

Sum of Outdial Hold Duration

Average Outdial Hold Time

The average hold time for outdial calls.

Sum of Outdial Hold Duration / Sum of Outdial Hold Count

Outdial Attempted Count

The number of times agents attempted to make outdial calls.

Sum of Outdial Ringing Count

Outdial Connected Count

The number of outdial calls that were connected to agents.

Sum of Outdial Connected Count

Outdial Connected Total Time

Sum of Outdial Connected Duration

Outdial Contact Total Time

The total amount of time agents were connected to outdial calls.

Sum of Outdial Connected Duration + Sum of Hold Duration

The average outdial connected time.

(Sum of Outdial Connected Duration + Sum of Hold Duration) / Sum of Outdial Connected Count

Sudden Disconnected Count

The number of calls that were connected to agents, but that were then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise.

Sum of Disconnected Count

Inbound Wrapup Count

The number of times agents went into the Wrapup state after an inbound call.

Sum of Wrapup Count

Inbound Wrapup Total Time

The total amount of time agents spent in the Wrapup state after an inbound call.

Sum of Wrapup Duration

Average Inbound Wrapup Time

The average length of time agents were in the Wrapup state after an inbound call.

Sum of Wrapup Duration / Sum of Wrapup Count

The number of times agents went into the Wrapup state after an outdial call.

Sum of Outdial Wrapup Count

Outdial Wrapup Total Time

The total amount of time agents spent in the Wrapup state after an outdial call.

Sum of Outdial Wrapup Duration

Average Outdial Wrapup Time

The average length of time agents were in the Wrapup state after an outdial call.

Sum of Outdial Wrapup Duration / Sum of Outdial Wrapup Count

Not Responding Count

The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent.

The total amount of time agents spent in the Not Responding state.

Sum of Not Responded Duration

Average Not Responding Time

The average length of time agents were in the Not Responding state.

Sum of Not Responded Duration / Sum of Not Responded Count

Consult Answer Count

The number of times agents answered a consult request from another agent.

Sum of Consult Count

Consult Answer Total Time

The total amount of time agents spent answering consult requests.

Sum of Consult Answer Duration

Average Consult Answer Time

The average length of time agents spent answering consult requests.

Sum of Consult Duration / Sum of Consult Count

Consult Request Count

The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

Sum of Consult Request Count

Consult Request Total Time

The total amount of time agents spent consulting other agents.

Sum of Consult Request Duration

Average Consult Request Time

The average length of time agents spent consulting other agents.

Sum of Consult Request Duration / Sum of Consult Request Count

Consult Count

The number of times agents answered consult requests plus the number of times agents consulted other agents.

Total Consult Time

Total Consult Answer Time plus Total Consult Request Time.

Sum of Consult Duration

Average Consult Time

The average length of consulting time.

Sum of Consult Answer Duration / Sum of Consult Answer Count

Conference Count

The number of times agents initiated a conference call.

Sum of Conference Count

Inbound CTQ Request Count

The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

Sum of CTQ Request Count

Inbound Total CTQ Request Time

The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls.

Sum of CTQ Request Duration

Inbound CTQ Answer Count

The number of times agents answered consult-to-queue requests from other agents who were handling inbound calls.

Sum of CTQ Answer Count

Inbound Total CTQ Answer Time

The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls.

Sum of CTQ Answer Duration

Outdial CTQ Request Count

The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent.

Sum of Outdial CTQ Request Count

Outdial CTQ Total Request Time

Shows the total amount of time an agent spent on a consultation via a consult-to-queue initiated by this agent while handling an outdial call.

Sum of Outdial CTQ Request Duration

Outdial CTQ Answer Count

The number of times agents answered consult-to-queue requests from other agents who were handling outdial calls.

Sum of Outdial CTQ Answer Count

Outdial CTQ Total Answer Time

The total amount of time agents spent answering consult-to queue requests from other agents who were handling outdial calls.

Sum of Outdial CTQ Answer Duration

Agent Transfer

The number of times an agent transferred inbound contacts to another agent after consult.

Sum of Agent To Agent Transfer Count

Agent Requeue

The number of times agents requeued inbound calls.

Sum of Agent Transfer To Queue Request Count

Blind Transfer

The number of times agents transferred inbound calls to either an external or third-party Dial Number (DN) through the Interactive Voice Response (IVR) without agent intervention.

Sum of Blind Transfer Count

Inbound Average Handle Time

The average length of time an agent spent handling inbound calls.

(Sum of Connected Duration  + Sum of Wrapup Duration) / Sum of Connected Count

Outdial Average Handle Time

The average length of time an agent spent handling outdial calls.

(Sum of Outdial Connected Duration  + Sum of Outdial Wrapup Duration) / Sum of Outdial Connected Count

Shows the number of times the agent went into the Engaged state.

Sum of Engaged Count

Shows the total amount of time an agent was engaged.

Sum of Engaged Duration

Shows the average engaged duration.

Sum of Engaged Duration / Sum of Engaged Count

###### Team

This report represents the channel type used by each agent in the team. The report displays the following details about the activity of each agent in the team since initial login.

The Sudden Disconnected Count field is currently not used and
                will not be populated.

Report Path : Stock Reports > Historical Reports > Agent Reports

Output Type : Table

Used As : Row Segment

Last 7 Days

Used As : Row Segment.

Sum of Connected Count + Sum of Outdial Connected Count

Sum of Realtime Update Timestamp - Sum of Login Timestamp

The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent.

The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

The number of times agents answered consult requests plus the number of times agents consulted other agents.

The sum of the total amount of time agents spent on consulting another agent, and on answering consult requests.

The average length of consulting time.

The number of times agents initiated conference calls.

The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls.

The number of times agents answered consult-to-queue requests from other agents who were handling inbound calls.

The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls.

The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent.

The number of times an agent transferred inbound contacts to another agent after consult.

Shows the number of times the agent went into the Engaged state.

Sum of Engaged Count

Shows the total amount of time an agent was engaged.

Sum of Engaged Duration

Shows the average engaged duration.

Sum of Engaged Duration / Sum of Engaged Count

###### Team Chart

The report displays the channel type details of each agent in a chart format.

Report Path : Stock Reports > Historical Reports > Agent Reports

Output Type : Bar Chart

Parameter

Description

Formula

Voice

The media type of the telephony contact.

Count of Connected Count (Channel Type = telephony) + Count of Outdial Connected Count (Channel Type = telephony)

Chat

The media type of the chat contact.

Count of Connected Count (Channel Type = chat)

Email

The media type of the email contact.

Count of Connected Count (Channel Type = email) + Count of Outdial Connected Count (Channel Type = email)

In the Team Chart report, for Agent Session Records, the count is aggregated based on Agent
        Session per Channel ID.

###### AI QM - Team Performance Report

This report contains list of agents by team with AI QM aggregated metrics at agent level.

Report Path: Stock report > Historical report > Agent Reports

Output Type: Table

The name of a team.

Used As : Row Segment

(Shows the name of the agent.

Used As : Row Segment

Sum of Total Connected Duration

+ Sum of Total Outdial Connected Duration

(Sum of Total Connected Duration+ Sum of Total Hold Duration + Sum of Post Call
                Duration + Sum of Total Wrapup Duration +Sum of Total Outdial Connected Duration

+Sum of Total Outdial Hold Duration

+Sum of Outdial Post Call Duration

+Sum of Total Outdial Wrapup Duration

)

/ (Sum of Outdial Connected Count

+ Sum of Connected Count)

(Sum of Overall Evaluation Score

+Sum of Outdial Overall Evaluation Score

) / (Sum of Overall Evaluation Score Count

+Sum of Outdial Overall Evaluation Score Count)

Sum of Overall Evaluation Score / Sum of Overall Evaluation Score Count

Sum of Outdial Overall Evaluation Score

/Sum of Outdial Overall Evaluation Score Count

Sum of Evaluation Interaction Failure Count

+

Sum of Outdial Evaluation Interaction Failure Count

(Sum of Word Ratio Score

+Sum of Outdial Word Ratio Score)

/ (Sum of Outdial Word Ratio Count + Sum of Word Ratio Count)

Sum of Word Ratio Score

/Sum of Word Ratio Count

Sum of Outdial Word Ratio Score

/Sum of Outdial Word Ratio Count

(Sum of Dead Air Time

+ Sum of Outdial Dead Air Time)

/ (Count of Dead Air Count

+Count of Outdial Dead Air Count)

(Sum of Outdial Cross Talk Time

+Sum of Talkover Time)

/ (Count of Talkover Count

+ Count of Outdial Cross Talk Count)

This report is only available when the feature is enabled. AI QM SKU is required to enable
        these capabilities. If you don’t see this report, contact Cisco Support to request feature
        flag enablement.

##### Agent Trace

This report represents which site or team the agent belongs to, with a detailed statistic report.

The Sudden Disconnected Count field is currently not used and
                will not be populated.

Report Path : Stock Reports > Historical Reports > Agent Trace

Output Type : Table

Description

The name of an agent, that is, a person who answers customer calls.

Used As : Row Segment

Time period for which the agent activity is available.

The call center location to which a call got distributed.

Used As : Row Segment

A group of agents at a specific site who handle a particular type of call.

Used As : Row Segment

The dial number that the agent used to log in to the Agent Desktop

Used As : Row Segment

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

The date and time when the agent logged in for the first time. This column appears only in agent-level summary reports.

The date and time when the agent logged out. This column appears only in agent level summary reports.

The total amount of time the agent was logged in.

Sum of Realtime Update Timestamp - Sum of Login Timestamp

The measure of time agents spent on calls compared to available and idle time.

The number of times an agent went into the Idle state.

The total amount of time agents spent in the Idle state.

The number of times an agent went into the Available state.

The total amount of time agents spent in the Available state.

The average time agents were in the Available state.

The number of times an agent went into the Inbound Reserved
                                state.

The total amount of time agents spent in the Reserved state.

The total amount of time agents spent in the Reserved state.

The average amount of time agents spent in the Reserved state.

The number of times an agent put an inbound caller on hold.

The total amount of time the inbound calls were on hold.

The number of inbound calls that were connected to an agent.

The total amount of time an agent was talking to customers on inbound calls. Inbound Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time.

The total amount of time an agent was connected to inbound calls.

The average inbound contact time.

The number of times an agent was in the Outdial Reserved state.

The total amount of time agents were in the Outdial Reserved state.

Average time the agents were in the Outdial Reserved state.

The number of times an agent put an outdial call on hold.

The total amount of time the outdial calls were on hold.

The average hold time for outdial calls.

The number of outdial calls that got connected to an agent.

The total amount of time an agent was talking to customers on outdial calls. Outdial Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time.

The total amount of time an agent was connected to outdial calls.

The number of calls that got connected to an agent, but then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise.

The number of times agents went into the Wrapup state after an inbound call.

The total amount of time agents spent in the Wrapup state after an inbound call.

The percentage of time agents were in the Wrapup state after an inbound call.

The number of times agents went into the Wrapup state after an outdial call.

The total amount of time agents spent in the Wrapup state after an outdial call.

The average time agents were in the Wrapup state after an outdial call.

Reason identifier

The average time agents were in the Idle state.

The average hold time for inbound calls.

The number of times an agent attempted to make an outdial call.

The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent.

The total amount of time agents spent in the Not Responding state.

The average time agents were in the Not Responding state.

The number of times agents answered a consult request from another agent.

The total amount of time agents spent answering consult requests.

The average time agents spent answering consult requests.

The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

The total amount of time agents spent consulting other agents.

The average time agents spent consulting other agents.

The sum of the number of times agents answered consult requests and the number of times agents consulted other agents.

The sum of the Total Consult Answer Time and Total Consult Request Time.

The number of times an agent initiated a conference call.

The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

The total amount of time agents spent answering consult-to-queue requests from an agent handling an inbound call.

The number of times agents answered a consult-to-queue request from another agent who was handling an inbound call.

The total amount of time agents spent answering consult-to-queue requests from an agent handling an inbound call.

The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent.

Shows the total amount of time an agent spent on a consultation via a consult-to-queue initiated by this agent while handling an outdial call.

The number of times agents answered a consult-to-queue request from another agent who was handling an outdial call.

The total amount of time agents spent answering consult-to-queue requests from an agent handling an outdial call.

The number of times an agent transferred inbound contacts to another agent after consult.

The number of times an agent requeued an inbound call.

The number of times an agent transferred an inbound call to either an external or third-party Dial Number (DN) through the Interactive Voice Response (IVR) without agent intervention.

The average length of time agents were in the Wrapup state after an inbound call.

The average length of time agents were in the Wrapup state after an outdial call.

number of true RONA instances associated with this agent.

- RONA_TIMER_EXPIRED

- NO_ANSWER_USER

Event name:

- not-responding

- consult-error

- transfer-error

Event name:

- con-to-agent-error

- consult-error

- transfer-error

Number of calls where the agent couldn't be connected, excluding RONA and Call Rejected cases.

- USER_DECLINED

- RONA_TIMER_EXPIRED

- NO_ANSWER_USER

Event name:

- con-to-agent-error

- consult-error

- transfer-error

- agent-invite-error

Shows the number of times the agent went into the Engaged state.

Sum of Engaged Count

Shows the total amount of time an agent was engaged.

Sum of Engaged Duration

Shows the average engaged duration.

Sum of Engaged Duration / Sum of Engaged Count

Click the RONA Count, Call reject Count, or Offer Error Count table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. You can see the following additional columns fetched from AAR events:

The reason code indicates why the call entered this state, specifically identifying whether the call failed to deliver to the agent due to telephony issues (for example, incorrect agent number, INVALID NUMBER), system issues, or if RONA occurred because the agent was unavailable (for example, USER_BUSY or other reasons). This helps the user differentiate between telephony-related problems, system-related issues, and cases where the agent genuinely went to RONA.

Here are the possible reason codes:

- INVALID_NUMBER: Agent's logged in DN is invalid

- USER_BUSY: Agent is busy

- USER_UNAVAILABLE: Agent's logged in DN is valid, but there are no devices online on that number.

- CHANNEL_FAILURE: A generic failure occurred, and the cause does not match any of the above reasons or existing auxiliary codes.

- NO_ANSWER_USER: No Answer from Agent

- RONA_TIMER_EXPIRED: The call rang on the agent's device, but the agent did not answer.

- USER_DECLINED: Agent declined/rejected the contact

- MEDIA_INTERNAL_ERROR: Media internal error

AAR Event

##### Auxiliary Reports

###### Idle Report

###### Agent Idle Auxiliary

This report represents the agent idle time.

Report Path : Stock Reports > Historical Reports > Auxiliary Reports > Idle Reports

Output Type : Table

Description

The name of an agent, that is, a person who answers customer calls.

Used As : Row Segment

Used As : Column Segment

The amount of time during which the agent was engaged in the activity.

###### Wrap-up Reports

###### Agent WrapUp Auxiliary

This report represents the agent name and the wrap-up code reason.

Report Path : Stock Reports > Historical Reports > Auxiliary Reports > Wrap-up Reports

Output Type : Table

The name of an agent, that is, a person who answers customer calls.

Used As : Row Segment

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Used As : Column Segment

The number of seconds that the interaction was active.

##### Contact Center Overview

###### Average Service Level Card

This pie chart shows the average service level that includes all channels.

Report Path : Stock Reports > Historical Reports > Contact Center Overview

Output Type : Chart

###### Contact Center Overview - Historical

Use Show Full Customer Journey to view contact metrics across the full
      journey of an interaction.

When the toggle is off, the dashboard uses the default queue view. If a contact traverses
      multiple queues, queue metrics are attributed only to the final queue, so activity in
      intermediate queues is not shown. When the toggle is on, the dashboard includes all queues
      traversed by the interaction and attributes metrics to each queue based on its
      contribution.

When Show Full Customer Journey is enabled, the Contact Details in
      Queue table shows metrics from the full customer journey view. Use this view to understand how
      applicable contacts were handled across queues and interaction phases.

###### Contact Details in Queue

This report provides contact details by queue.

Report Path : Stock Reports > Historical Reports > Contact Center Overview

Output Type : Table

Parameter

Toggle On Behaviour Description

Toggle Off Behaviour Description

Formula

The start time of the queue activity represented by the row.

Channel Type

The media type of the contact, such as telephony, email, or chat.

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Queue Name

The queue represented by the row. A contact can appear in more than one queue row
                if it entered multiple queues.

The last queue that the contact was in.

Used As : Row Segment

Skills assigned in

Not shown in this version.

Indicates where skills are assigned.

The following are the values:

- For the current Skill-Based Routing Team's queue, the value is 'Flow'.

- For the Skill-based queue, the value is ‘Queue’.

- For the Agent-based queue, the value is ‘NA’.

# Contacts

Not shown in this version.

The total number of contacts.

Handled Contacts

The number of contacts handled in the queue represented by the row.

Not shown in this version.

Avg Queue Wait Time

The average time contacts waited in the queue represented by the row.

Current State: connected, ended

Longest Contact's Total Queue Duration

The longest time a contact waited in the queue represented by the row. Contacts
                currently in queue are not included.

Current State: connected, ended

# Abandoned Contacts

The number of contacts abandoned while waiting in the queue represented by the
                row.

Termination Type: abandoned

###### Longest Contact's Total Queue Duration Card

This report shows the total time when interaction is parked across all queues. This card is historical and it is updated based on the last 7 days. It shows the single longest parked time for the contact in a queue and across all instances.

This report provides the longest duration of the contact, channel type, and queue name.

Report Path : Stock Reports > Historical Reports > Contact Center Overview

Output Type : Card

###### Team Details

This report provides team details.

The Social column appears only if the Social Channel SKU is subscribed.

Report Path : Stock Reports > Historical Reports > Contact Center Overview

Output Type : Table

Parameter

Description

Formula

Team Name

Agent Name

Name of the agent.

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Total Log In Count

The total number of logins of the agent during the specified time interval.

(Cardinality provides the total number of unique Agent Session IDs.)

Initial Login Time

Final Logout Time

Staff Hours

Sum of Realtime Update Timestamp - Sum of Login Timestamp

Idle Counts

# Contacts Handled

# Calls Handled

# Chats Handled

# Emails Handled

The number of  Social channel type contacts that were handled.

Social Connected Count + Social Outdial Connected Count

###### Surge Protection Statistics

The Surge Protection mechanism provides your organization the ability to configure the maximum number of active calls (inbound and outdial) that can be simultaneously handled by the contact center at any point. The Surge Protection mechanism works at two levels—data center (DC) level and tenant level.

At the DC level, calls are rejected when the number of voice calls exceeds the threshold limit that is set for the DC.

At the tenant level, calls are rejected when the number of voice calls exceeds the maximum limit configured for the tenant, which is based on the licenses purchased by your organization.

The Surge Protection Statistics report provides details of the calls that the contact center received, handled, abandoned, and rejected due to the surge protection limits that are set at the tenant level.

Report path: Home > Visualization > Stock Reports > Historical Reports > Contact Center Overview

Output type: Table

Indicates the date and time of the incoming call.

The unique ID associated with each incoming call.

The entry point where the call landed.

The name of the site or location.

The name of the queue.

Indicates whether the call was handled, by means of a check mark.

Indicates whether the call was abandoned, by means of a check mark.

Indicates whether the call was rejected, by means of a check mark.

The reason why the call was abandoned or rejected.

Summary

The report also provides a summary of the total number of calls that were handled, rejected, or abandoned.

##### Multimedia Reports

###### Agent Volume - Chart

This report represents the content type handled by an agent. You can filter data based on content type or date.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

Parameter

Description

Filters

Formula

The media type of the telephony contact.

The media type of the chat contact.

The media type of the email contact.

Contacts Handled

The total number of contacts handled.

Termination Type: normal

Count of Contact Session ID

###### Contact by DNIS

This report represents the contact DNIS for a customer.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

Description

DNIS does not appear for a Chat contact.

Count of Contact Session ID

###### Contact Reason

This report represents the contact reason for a customer to contact the call center.

The Social column appears only if the Social Channel SKU is subscribed.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

Description

Channel Type: Telephony

Channel Type: chat

Channel Type: email

The total number of social channel interactions handled.

Channel Type: social

Count of Contact Session ID

###### Contact Volume - Chart

This report represents the number of contacts handled based on the DNIS value for a channel type.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Bar Chart

The media type of the telephony contact.

The media type of the chat contact.

The media type of the email contact.

###### CSR-Yesterday

This report shows the Contact Session Record (CSR) for the previous day.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

The number of times a call was transferred via blind transfer in the following scenarios:

Agent transferred the call to another agent without consulting first.

Agent transferred the call to another queue without consulting first.

Agent transferred the call to an external Dial Number (DN) without consulting first.

Call transferred to an End Point (EP) through the flow without agent intervention.

The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent.

Indicates the number of times a call was transferred:

By an agent to another agent

Through the Flow

To a Queue

To a DN or EP

To an EP through GoTo activity

Click the Call Direction table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. You can see the following parameters:

Termination Reason —Specifies the reason, why the call was terminated. For example, the Customer left the call.

Termination Party —Specifies, who terminated the call or where the call was terminated. For example, if the call was terminated by the agent or the customer, if the call was terminated in the system or queue.

Customer sentiment score of interactions between -100 and +100
                                (Integer)

Conditional formatting: >

Parameters marked with ‘*’ are visible only when the feature is enabled. AI QM SKU is
                required to enable these capabilities. If these columns are missing, contact Cisco
                Support to request feature flag enablement.

###### Entry Point Contact Volume - Chart

This report displays the contact entry point.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Bar Chart

The media type of the telephony contact.

The media type of the chat contact.

The media type of the email contact.

###### Queue Abandoned Chart

This report represents the number of abandoned customer for each Queue.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Bar Chart

The media type of the telephony contact.

Termination Type: abandoned

Channel Type: telephony

The media type of the chat contact.

Termination Type: abandoned

Channel Type: chat

The media type of the email contact.

Termination Type: abandoned

Channel Type: email

###### Queue Abandoned

This report represents the number of calls that were in the system but terminated before being distributed to an agent or other resource.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

Parameter

Description

Filters

The name of a queue.

Used As : Row Segment

Final Queue ID = Is not in 0

Time period

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Final Queue ID = Is not in 0

The number of calls that ended during the report interval. Answered, abandoned, and disconnected calls are included in this count. Transferred and short calls are not.

The percentage of calls that were abandoned

Count of Contact Session ID (Handle type = Abandoned) / Sum of Contact Count

The number of calls that were abandoned during the report interval. An abandoned call is a call that was terminated without being distributed to a destination site, but that was in the system for longer than the time specified by the Short Call threshold provisioned for the enterprise.

Termination Type: abandoned

The cumulative amount of time calls were in queue, waiting to be sent to an agent or other resource. Because queued time is calculated after the call leaves the queue, the queued time for a call that is still in the queue is not reflected in the report.

The cumulative amount of time calls were in the system for longer than the time specified by the Short Call threshold, but terminated before being distributed to an agent or other resource.

###### Queue Service Level

This report represents the service level for a queue.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

Used As : Row Segment

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

The number of calls that were answered within the Service Level threshold provisioned for the queue or skill (including abandoned calls).

The total number of calls from contacts that landed to the Webex Contact Center system through all the entry points for the selected duration.

The number of calls that ended during the report interval. Answered, abandoned, and disconnected calls are included in this count. Transferred and short calls are not.

The number of calls that were abandoned during the report interval. An abandoned call is a call that was terminated without being distributed to a destination site, but that was in the system for longer than the time specified by the Short Call threshold provisioned for the enterprise.

Termination Type: abandoned

The number of calls that were routed from the queue to an agent or available resource and were answered by the agent or resource.

Connected Duration: > 0

The number of times agents initiated a conference call to an agent or external number.

The number of times a caller was put on hold.

The cumulative amount of time calls were in the system for longer than the time specified by the Short Call threshold, but terminated before being distributed to an agent or other resource.

The total answered time divided by the total number of answered calls.

(Queue Duration + Ringing duration) / Answered

###### Teams Contact Details

This report represents the number of contact types for a team.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

Used As : Row Segment

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

The number of calls that ended during the report interval. Answered, abandoned, and disconnected calls are included in this count. Transferred and short calls are not.

The number of calls that were answered (that is, connected to an agent or distributed to and accepted by a destination site), but that were then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise.

Termination Type: sudden_disconnect

Termination Type: normal

The cumulative amount of time between when calls entered the queue and when they were answered (connected to an agent or other resource) during the report interval. Because answered time is calculated after the call is answered, answered time for calls that are waiting to be answered is not reflected in the report.

Is Contact Handled: = 1

The time interval between when calls were answered by an agent or other resource and when they were terminated. Because connected time is not calculated until the call is terminated, the connected time for a call that is still in progress is not reflected in the report.

###### Volume Report

This report represents the number of channel types for a team.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Table

The media type of the contact, such as telephony, email, or chat.

The total number of contacts offered.

The total number of interactions handled.

Termination Type: normal

The average length of time spent handling a call.

###### Volume Report - Chart

This report represents the number of contacts offered or handled for a particular channel type.

Report Path : Stock Reports > Historical Reports > Multimedia Reports

Output Type : Bar Chart

Parameter

Description

Formula

Offered

The total number of contacts offered.

Sum of Is Offered

Handled

The total number of interactions handled.

Termination Type: normal

Count of Contact Session ID

###### Unified Call Summary

The Unified Call Summary report in Analyzer facilitates to analyze the journey of
      conversations flowing between both the Webex Contact Center and Webex Calling platforms. The
      feature correlates call activity across Contact Center and Calling by using a shared
      interaction ID, so a reporting user can start from Contact Center data and drill into related
      Calling CDR (Calling Data Records) details.

For customers using Webex Calling as their primary PSTN, this stock report is available and
      it displays all conversations that came to the contact center. Specially, an admin can also
      see conversations that originated in Webex Calling and were transferred to Webex Contact
      Center or vice versa are displayed in this report with the primary caveat that the
      conversation needs to have transited through the contact center.

It gives visibility into what happens when calls move between a contact center agent and a
      Webex Calling user, including whether the call was answered, abandoned, terminated, sent to
      voicemail, reached an auto attendant, or completed with wrap-up.

Before you begin

- You need Supervisor or Administrator privileges to access Analyzer.

- The organization must have unified reporting available for Webex Contact Center and Webex
        Calling.

- A shared Interaction ID must be available for the call journey.

Report Path : Stock Reports  > Historical Reports > Multimedia Reports

Output Type : Table

Some of the historical data may not be available for this report
      when it is extracted.

Report details

Understanding the Landing Page

The report opens on the call interaction summary landing page, displaying Contact Center-side
      data for all interactions that transited between Contact Center and Calling.

The landing page displays more detail about record contents:

Indicates the party that terminated the interaction. The terminating party can be
                one of the following:

- Agent—The agent terminated the callback.

- Contact—The contact terminated the callback.

- System—The callback was terminated due to a system error.

The Abandoned Type is set when the call is abandoned. The following values show
                    the states of the call when abandoned.

null: The customer was connected with an agent.

- new: The customer disconnected immediately after entering the flow, before
                  reaching any queue.

- queue: The customer disconnected while waiting in the queue for an agent.

- treatment: The customer disconnected during self-service options, such as IVR,
                  message playback, or music, before entering a queue.

- agent-connect: The customer hung up before an agent was connected to the
                  customer (during the ringing or connecting phase).

Checks the previous event before the ended event and sets the value accordingly.
                For instance, if the previous event before the ended event is parked, the Abandoned
                Type is set to 'queue'.

Reason for the call abandonment. The abandonment reason can be one of the
                following:

- Agent Left: The agent ended the call.

- Customer Left: The customer ended the call.

- Queue Timeout: The call ended because it was queued for longer than the
                  configured timeout in a queue.

- System Error: The call ended because of system errors.

- Agent Disconnected: The call ended because the agent was disconnected from the
                  call.

- Blind Transfer Failed: The inbound call ended because the call contact transfer
                  to either an external or third-party Dial Number (DN) through the Interactive
                  Voice Response (IVR) without agent intervention failed.

- RONA Timer Expired: The outbound call ended because the agent was unable to
                  answer the call.

- Interaction Cleanup: The contact was cleaned up for serviceability or
                  troubleshooting purpose.

Drill down into Calling records

Select the Interaction ID to view Calling-side call detail records for the same customer
      interaction. The drill-down view can show Calling details such as duration, calling number,
      called number, correlation ID, answered status, user ID, call outcome, call outcome reason,
      and ringing duration.

To view Calling CDR details for a specific interaction:

- On the landing page, locate the interaction you want to investigate.

- Click the Contact session ID link in that row.

The drill-down page shows the activity segments for the selected interaction, combining
      Contact Center activity with Calling-side CDR data.

To return to the landing page, click Back at the top of the drill-down page.

Limitations

- The summary report contains contact center data only. The durations, agent metadata
        information is for the portion of the conversation that transited through the contact center

- The call detail records are shown per user agent per segment. For instance, during the
        conversation between the branch office agent and the customer, there are two records for
        each participant in that portion.

- There is no customization available on the report.

###### Self Service Reports

###### IVR and CVA Dialog Flow Report

This report displays the Self-service operational metrics. The Self-service Reporting and Analytics information consists of:

Number of abandoned calls in Self-service.

Number of abandoned calls in a queue.

Self-service is enabled by adding the Virtual Agent activity to the call flow in Flow
                Designer. When a customer contacts the contact center, the virtual agent handles the
                contact in the IVR. For more information on configuring the virtual assistant,
                please see Virtual Agent section of the Cisco Webex Contact Center Setup and
                        Administration Guide .

Report Path: Stock Reports > Historical Reports > Multimedia Reports > Self Service Reports > IVR and CVA Dialog Flow Report.

Output Type: Table

Parameter

Description

Filters

Formula

Interval

The time period for which the Self-service analytics data is reported.

Entrypoint Name

The list of entry points for the IVR call.

Total IVR Calls

The total number of IVR calls handled by the virtual agent.

Calls Abandoned in Self-Service

Number of IVR calls that were abandoned in IVR.

Calls Escalated to Queue

Number of IVR calls that were escalated to a queue.

Percentage Escalation to Queue

Percentage of IVR calls that were escalated to a queue.

100 * (Calls Escalated to Queue / Total IVR Calls)

Click any table cell (except the Percentage Escalation to Queue table cell) to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. The Drill Down modal dialog displays the records that are involved in the computation of the visualization. You can see the following details:

Parameter

Description

Name of Activity

Shows the name of the activity such as CVA, Play Prompt, Menu, and Queue.

Number of Calls completed in this Activity

Shows the total number of calls completed in this activity.

To add a new column in the report, you can select the appropriate Fields and Measures from the drop-down list on the left side of the Drill Down modal dialog. You can export the Drill Down report in Microsoft Excel format or CSV format to a preferred location. To view the Drill Down modal dialog in a separate window, click the Launch icon.

You can further drill down on the Name of Activity table cell, to display the sequence of activities. This Drill Down report is the second-level drill down. You can see the following details:

Parameter

Description

Entrypoint Name

Shows the entry point for that particular activity.

Timestamp

Shows the date and the time at which the call landed in the
                                Self-service.

Call ID

Shows the call ID number.

Sequence of Activity

Shows the sequence of activities that were involved in the call. The activities include DTMF, Prompt Name, Queue Name, Abandoned, Completed, CVA, Menu, Self Service Complete, and Self Service Abandon.

###### Opt Out of Queue Report

This report displays the opt-out-of-queue choices made by the customer.

When a customer contacts the contact center, the virtual agent handles the contact in the IVR. The IVR provides an option for the customer to opt out of the queue. This report shows:

The number of opt-outs.

Other call-associated data.

Report Path : Stock Reports > Historical Reports > Multimedia Reports > Self Service Reports > Opt Out of Queue Report

Output Type : Table

Parameter

Description

Filters

Formula

Date

Displays the date.

Queue Name

The queue that the contact was in at the time of opting out.

Number of Opt-outs

Click Number of Opt-outs table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. The Drill Down modal dialog displays the records that are involved in the computation of the visualization. You can see the following details:

Parameter

Description

Formula

Call Time

Shows the time at which the call got connected.

ANI

Shows the ANI number that is associated with the call.

DNIS

Shows the DNIS number that is associated with the call.

Workflow Sequence

Shows the sequence of activities that happened during the call.

To add a new column in the report, you can select the appropriate Fields and Measures from the drop-down list on the left side of the Drill Down modal dialog. You can export the Drill Down report in Microsoft Excel format or CSV format to a preferred location. To view the Drill Down modal dialog in a separate window, click the Launch icon.

###### Inline IVR Post Call Survey Statistics Report

Webex Contact Center is integrated with Cisco Webex Experience Management, to present
            post call surveys to customers and to collect their feedback.

If the report is not displayed, contact Cisco Support as the corresponding feature
                flag may have to be enabled.

The Inline IVR Post Call Survey Statistics Report enables administrators and supervisors
            to view Post Call Survey statistics in order to measure the effectiveness of the
            surveys. This report is available for customers who have access to the Webex Experience
            Management widget.

Report Path: Stock Reports > Historical Reports > Multimedia Reports > Self Service Reports > Inline IVR Post Call Survey Statistics Report

Output Type: Table

Parameter

Description

Filters

Formula

Interval

The time period for which the Webex Experience Management Post Call
                                Survey data is reported.

Total Calls

The total number of voice calls for which the Post Call Survey was
                                offered to the customer during the interval

Survey Opt-in Number

The number of customers who opted for the inline survey.

If there an error while gathering caller's opt-in preference then
                                    it is not considered as part of the Survey Opt-in Number
                                    calculation.

Survey Opt-in Stats

The percentage of customers who opted for the inline survey.

Survey Response Rate

The percentage of voice calls for which the Post Call Survey response
                                was received. This is calculated as a percentage of the Survey
                                Opt-in number.

Survey Completion Rate

The percentage of questions answered by the customers. This is
                                calculated as a percentage of the total number of questions posted
                                to the customers.

The Summary value for the Total Calls with Survey and Survey Opt-in Number is the summation of all the values for a
            specific duration.

The Summary value for the Survey Opt-in Stats is the percentage of
            the summary values of the Total Calls with Survey and the Survey Opt-in Number .

The Summary value for the Survey Response Rate is the percentage
            of the summary values of the Total Calls with Survey and the
            Total number of customers responded to the survey.

The Summary value for the Survey Completion Rate is the percentage
            of the summary values of the Total Calls with Survey and the
            Total number of customers completed the survey.

If a voice call receives multiple survey, only the final survey details are
                recorded.

###### Post Call Survey Statistics Report

Webex Contact Center is integrated with Cisco Webex Experience Management to present
            post-call surveys to customers and to collect their feedback.

If the report is not displayed, contact Cisco Support as the corresponding feature
                flag may have to be enabled.

The Post Call Survey Statistics Report is available for customers who have access to the
            Webex Experience Management widget.

The Post Call Survey Statistics Report enables administrators and supervisors to view
            Post Call Survey statistics in order to measure the effectiveness of the surveys. This
            report includes data for both Inline and Deferred surveys. An Inline survey is a survey
            that is presented to a customer when a voice call with the customer ends. A Deferred
            survey is a survey that is presented at a later point in time, via SMS or Email.

Report Path: Stock Reports > Historical Reports > Multimedia Reports > Self Service Reports > Post Call Survey Statistics Report

Output Type: Table

Parameter

Description

Filters

Formula

Interval

The time period for which the Cisco Webex Experience Management Post
                                Call Survey data is reported.

Type of Survey

The type of survey that the customers have opted for (Inline survey
                                or Deferred survey).

Total Contacts with Survey

Total number of customers who were offered the specific type of
                                survey (Inline survey and Deferred survey).

Survey Opt-in Number

Total number of customers who opted in for each type of survey
                                (Inline survey and Deferred survey).

If there an error while gathering caller's opt-in preference then
                                    it is not considered as part of the Survey Opt-in Number
                                    calculation.

Survey Opt-in Stats

The percentage of customers who opted in for the survey (Inline
                                survey and Deferred survey).

(Survey Opt-in Number / Total Contacts with Survey) x 100

The Summary value for the Total Calls with Survey and Survey Opt-in Number is the summation of all the values for a
            specific duration.

The Summary value for the Survey Opt-in Stats is the percentage of
            the summary values of the Total Calls with Survey and the Survey Opt-in Number .

If a voice call receives multiple survey, only the final survey details are
                recorded.

##### Team and Queue Stats

###### Average Handle Time Card

This report displays the average time of total contacts (voice, email, and chat) that got handled.

Report Path : Stock Reports > Historical Reports > Team & Queue Stats

Output Type : Card

###### Average Wrapup Time Card

This report displays the average wrapup time for each individual channel and for overall channels.

Report Path : Stock Reports > Historical Reports >  Team & Queue Stats

Output Type : Table

###### Team Stats

This report displays the team statistics.

Report Path : Stock Reports > Historical Reports > Team & Queue Stats

Output Type : Table

Parameter

Description

Filters

Formula

Interval

Shows the duration for which the team statistics is collected.

Last 7 Days

Team Name

Shows the name of the team.

Agent Name

Shows the name of the agent.

# Contacts Handled

Shows the number of contacts that were handled by the agent.

Total Contacts Handled

Shows the total number of contacts that were handled by the agent for
                                the call channel type.

Sum of Inbound Contacts Handled + Outdials Handled

Inbound Contacts Handled

Shows the total number of inbound contacts that were handled by the
                                agent for the call channel type.

Callbacks Handled

Shows the number of callbacks that were handled by the agent for the
                                call channel type.

Outdials Handled

Shows the total number of outdial calls that were handled by the
                                agent for the call channel type.

Average Handle Time

Shows the average time that was spent by the agent on the contacts
                                handled.

Sum of Wrapup Duration  + Sum of Connected Duration / # Contacts Handled

Average Wrapup Time

Shows the average time that was spent on wrapping up the contacts
                                handled.

Sum of Wrapup Duration / Sum of Wrapup Count

The Total Contacts Handled , Inbound Contacts
                    Handled , Callbacks Handled , and Outdials Handled columns are available in the Team Stats
                report of the APS reports in Agent Desktop.

###### Total Handled Card

This report displays the total number of contacts handled and broken down by channel type.

Report Path : Stock Reports > Historical Reports > Team & Queue Stats

Output Type : Card

##### Post interaction surveys

###### Survey Response Report

This report provides a view of the IVR survey results along with several operational data points. You can sort, filter, and export the reports using the existing reporting features in the Analyzer portal.

Report Path : Visualization > Historical Reports > Post Interaction Surveys > Survey Response Report

You can view detailed insights on agents, queues, sites, and more for each survey question, enabling effective analysis of the survey results.

You can use the Clear Filters option to clear existing filters and select new filters.

You can use the Filter Combinations option to filter report results based on your filter
          selection.

When you select this report, the maximum number of records you can fetch is 30,000.

Some survey responses can have a delay upto 1 day to have respective agent or call
            related data populated in the report.

Eg. For a survey response submitted on Jan 1st, agent or call related information can
            sometimes get delayed until Jan 3rd 12AM to appear in the report.

You need to consider the following points while viewing the Survey Response Report:

- The Survey Response Report cannot be copied.

- If surveys are not created or completed, and no data is available, no data will be
                displayed.

Output Type : Table

Parameter

Description

The date and time on which the survey was started. This is in the UTC time zone.

A unique string that identifies the contact session and can be found in Analyzer.

The name of the survey

The text given to the question when the survey is created.

##### CallBack Reports

###### Callback Report

The contact center customer can opt to receive a callback from an agent when the customer visits the contact center website, communicates with the bot, or waits in a queue. The courtesy callback flow is configured by the flow developer. For more information, see the Courtesy Callback chapter in the Cisco Webex Contact Center Setup and Administration Guide .

Report Path: Stock Reports > Historical Reports > Callback Reports

Output Type: Table

Parameter

Description

Filters

Formula

Queue Name

The name of the last queue that was associated with the callback.

Type of Callback

The type of the callback. The callback type can be courtesy, scheduled, scheduled_personal, or web.

Source of Callback

The source of the callback. The source of a callback can be web, chat, livecall, api or IVR.

Callback Request Time

The time at which the customer opted for the callback.

Callback Connected Time

The time at which the callback was connected between the agent and the customer.

Callback Number

The number that is based on the ANI or the number that was configured in a workflow.

Preferred Agent Name

The name of the preferred agent who made the callback to the contact in queue.

This column displays a N/A value if the contact is not queued to the preferred agent through Queue to Agent activity in Flow Designer.

For more information, see the Queue To Agent activity documentation.

If the preferred agent is unable to make a callback, the Agent Name column displays a N/A value.

Agent Name

The name of the agent making the callback.

Team Name

The name of the team that the agent belongs to.

Last Callback Status

The status of the last callback.

Callback Status

Success: When a Callback call was connected.

Not Processed: When an agent receives the Callback request but is pending processing.

Failure: When a Callback was attempted, but the connection was not established.

Final Reason

NO_ANSWER_FROM_CUSTOMER —The callback was not answered when the customer received it on their device.

CUSTOMER_BUSY —The customer device was busy when the callback was attempted.

CUSTOMER_UNAVAILABLE —The customer's device was unavailable when the callback was attempted.

Customer Left —The customer ended the call.

NO_ANSWER_FROM_AGENT —The callback was not answered when the agent received it on their device.

AGENT_ENDS —Agent ended the callback contact before it could be established with the customer.

Agent Left —The agent ended the call.

RONA Timer expired —The Ring-No-Answer (RONA) timer expired before the callback contact could be answered.

Queue Timeout —The configured queue timeout expired for the parked callback contact before it could be routed to an an eligible and available agent in that queue.

MAX_CALLBACK_RETRY_LIMIT_REACHED —The configured maximum retries for the callback contact was reached.

OUTDIAL_FAILED —There was a failure to dial out the callback contact to the customer.

Unsupported flow activity —The contace was terminated due to the execution of an unsupported flow activity.

Queue Timeout —The contact timed out while waiting in the queue.

Participant Invite Timer expired —The contact was terminated due to a timeout in media signaling to invite a participant into the call.

SYSTEM_ERROR —The contact was terminated due to an unknown system error.

Terminated by

Agent —The agent terminated the callback.

Contact —The contact terminated the callback.

System —The callback was terminated due to a system error.

Failed Callback Retry Count

The number of times a callback retry failed.

Click the Failed Callback Retry Count table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal. You can see the following details in the Drill Down modal :

Callback ID

Shows a unique string that identifies the callback session.

Callback Time

Shows the time at which the callback was requested.

Reason

Agent Left —The agent ended the call.

Customer Busy —The contact's dialled line is busy.

System Errors —The call ends due to system errors.

##### Campaign Reports

Webex Contact Center offers integration for conducting and managing campaigns. These campaigns generate reports, which administrators and supervisors can utilize to view campaign statistics and gauge the effectiveness of their campaigns.

Stock Campaign Reports are available exclusively for Acqueon integrations and not for third-party integrations.

###### Preview Campaign Report

The Preview Campaign report provides a comprehensive analysis of Preview Campaign performance.

Report Path: Stock Reports > Historical Reports > Campaign Reports

Output Type: Table

Parameter

Description

Filters

Formula

Campaign Name

The name of the campaign.

—

—

Interval

Time period.

—

—

Queue Name

The name of the queue.

—

—

Team Name

The name of the team to which the agent belongs.

—

—

Agent Name

The name of the agent who is associated with the call.

—

—

Contacts

The number of calls made by the agent as part of the campaign.

—

Count of Contact Session ID

Average Handle Time

Shows the average time that was spent by the agent on the contacts handled.

—

Average Talk Time  + Average of Wrapup Duration

Average Talk Time

Average time that an agent spent in a call.

—

Average Talk Time + Average of Connected Duration

Click the Contact table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal. The Contact drill-down modal provides a detailed view of each call made for the particulur campaign.

###### Progressive and Predictive Campaign Report

The Progressive and Predictive Campaign report provides a comprehensive analysis of Progressive and Predictive Campaign performance.

Report Path: Stock Reports > Historical Reports > Campaign Reports

Output Type: Table

Parameter

Description

Filters

Formula

Campaign Name

The name of the campaign.

—

—

Outdial Entrypoint

The name of the Entrypoint.

—

—

Campaign Type

The type of campaign.

—

—

Interval

Time period

—

—

Queue Name

The name of the queue.

—

—

Team Name

The name of the team to which the agent belongs.

—

—

Agent Name

The name of the agent who is associated with the call.

—

—

Contacts

The number of calls made by the agent as part of the campaign.

—

Count of Contact Session ID

Average Handle Time

Shows the average time that was spent by the agent on the contacts handled.

—

Average Talk Time  + Average of Wrapup Duration

Average Talk Time

Average time that an agent spent in a call.

—

Average Talk Time + Average of Connected Duration

Click the Agent Name table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal. The Agent Name drill-down modal provides the Campaign Reserved Time details associated with each agent.

If an agent is engaged in multiple campaigns simultaneously, the reservation time is combined.

If an agent logs in twice, the system will create two distinct rows for that agent.

Click the Contact table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal. The Contact drill-down modal provides a detailed view of each call made for the particulur campaign.

Call Progress Analysis (CPA) monitors and reports on various call progress scenarios, indicating successful connections or failures.

Descriptions for different CPA status are outlined below:

- NO_ANSWER_CUSTOMER —The call remains unanswered within the specified No Answer Ring Limit designated for the campaign.

- CUSTOMER_BUSY —The customer's line is busy or the call is declined by the customer.

- CUSTOMER_UNAVAILABLE —Network timeout or error potentially transient in nature.

- INVALID_NUMBER —The dialed number is invalid.

- CUSTOMER_LEFT —The customer answers the call but ends it immediately from their device or before CPA completion.

- ABANDONED —The call is abandoned due to a lack of available agents or resources.

- AMD —The call is answered by an answering machine or routed to voicemail.

- FAX —A fax machine is detected on the line.

- SYSTEM_ABANDONED —The call is abandoned due to an error condition within the system.

###### Progressive and Predictive Campaign Realtime Report

The Progressive and Predictive Campaign Realtime report provides a comprehensive analysis of Progressive and Predictive Campaign Realtime performance.

Report Path: Stock Reports > Real-Time Reports> Campaign Reports

Output Type: Table

##### Queue-based Reports

Queue-based reports (QBR) store the progression of each call as it moves through different queues, covering its entire journey. QBR introduces three new stock reports in Analyzer— Queue Activity by Queue , Queue All Fields Report , and Queue Call Distribution Summary . These reports deliver comprehensive insights and metrics at the queue level, covering call flows and interactions as they are presented, handled, transferred, and consulted across queues.

Key Metrics in Queue-based Reports

The following metrics are used to evaluate queue performance:

- Calls Presented to Queue (CP)—The total number of calls that enter the queue, including both direct calls and consultation requests.

- Calls Handled (CH)—The number of calls successfully routed to an agent and answered.

- Calls Moved Out of Queue (CM)—The number of calls that leave the queue without being addressed by an agent.

If you want the calls transferred to DN count to be incremented, contact Cisco Support as the corresponding feature flag may have to be enabled.

- Calls Abandoned (CA)—The number of calls where the caller exits the queue without being connected to an agent, often due to long wait times or the caller hanging up before service.

- Consult to Queue Failed Count and Consult to Entry Point Failed Count —The number of unanswered consult requests by an agent to a Queue or an Entry Point.

Call legs with a call leg type of 'conference' are excluded from these reports.

###### Queue Activity by Queue

The Queue Activity by Queue report presents information about service levels, the number and the percentage of calls that were presented, handled, abandoned, and dequeued. It presents information for the selected time interval.

Report Path : Stock Reports > Historical Reports > Queue Reports

Output Type : Table

The name of the queue.

Used As : Row Segment

Used As : Row Segment

Service Level (in seconds)

Used As : Row Segment

The total number of calls that are handled within the service level threshold that was set for the queue.

Is Within service Level = 1

Handle Type is normal or sudden_disconnect .

The total number of calls that are abandoned within the service level threshold that was set for the queue.

Is Within service Level = 1

Handle Type is abandoned .

Number of calls that were routed to the queue, regardless of whether an agent answered the call.

Handle Type is normal or sudden_disconnect .

Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count)

Number of times a call was transferred from an agent to a DN.

Sum of Agent to DN Transfer Count

The number of times call came after being transferred by an agent. (Blind transfers are not counted)

Blind transfer scenarios inlcude the following:

- transfer to different queue

- transfer to EP

- transfer to agent

- transfer to the same queue

- transfer to DN

Sum of Agent Transferred In Count

This count is incremented when an agent initiates a blind transfer call to a Queue or an EntryPoint.

Sum of Inter Queue Blind Transfer Count

Calls Abandoned %

Calls Moved Out of Queue

Number of calls that were moved out of Queue without being handled.

Calls Transferred to DN

Number of calls that were transferred to a dial number (DN) by blind transfer node via flow.

If you want the calls transferred to DN count to be incremented, contact Cisco Support as the corresponding feature flag may have to be enabled.

Handle type is TransferToDN .

Count of Contact Session ID

Calls Transferred to DN %

Percentage of calls that were transferred to a dial number (DN) by blind transfer node via flow.

(Calls Transferred to DN / Calls Presented) x 100

Number of contacts that transitioned to RONA in this queue

- RONA_TIMER_EXPIRED

- NO_ANSWER_USER

Event Name:

- con-to-agent-error

- consult-error

- transfer-error

Count of contacts rejected by agents in this queue

Event name:

- con-to-agent-error

- consult-error

- transfer-error

- agent-invite-error

Count of contacts with Offer errors in this Queue

- USER_DECLINED

- RONA_TIMER_EXPIRED

- NO_ANSWER_USER

Event name:

- con-to-agent-error

- consult-error

- transfer-error

- agent-invite-error

Click the RONA Count, Call reject Count, or Offer Error Count table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. You can see the following additional columns fetched from CAR events:

The reason code indicates why the call entered this state, specifically identifying whether the call failed to deliver to the agent due to telephony issues (for example, incorrect agent number, INVALID NUMBER), system issues, or if RONA occurred because the agent was unavailable (for example, USER_BUSY or other reasons). This helps the user differentiate between telephony-related problems, system-related issues, and cases where the agent genuinely went to RONA.

Here are the possible reason codes:

- INVALID_NUMBER: Agent's logged in DN is invalid

- USER_BUSY: Agent is busy

- USER_UNAVAILABLE: Agent's logged in DN is valid, but there are no devices online on that number.

- CHANNEL_FAILURE: A generic failure occurred, and the cause does not match any of the above reasons or existing auxiliary codes.

- NO_ANSWER_USER: No Answer from Agent

- RONA_TIMER_EXPIRED: The call rang on the agent's device, but the agent did not answer.

- USER_DECLINED: Agent declined/rejected the contact

- MEDIA_INTERNAL_ERROR: Media internal error

CAR Event

###### Queue All Fields Report

The Queue All Fields report presents Queue-related data, such as call statistics and Service Level. The report includes key fields, such as Average Queue Time, Average Speed of Answer, Calls Handled and Calls Abandoned under Service Level.

Report Path : Stock Reports > Historical Reports > Queue Reports

Output Type : Table

Parameter

Description

Filters

Formula

Queue Name

The name of the queue.

Used As : Row Segment

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Used As : Row Segment

Number of calls that were routed to the queue, regardless of whether an agent answered the call.

Handle Type is normal or sudden_disonnect .

Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count)

Number of times a call was transferred from an agent to a DN.

Sum of Agent to DN Transfer Count

The number of times call came after being transferred by an agent. (Blind transfers are not counted)

Blind transfer scenarios inlcude the following:

transfer to different queue

transfer to EP

transfer to agent

transfer to the same queue

transfer to DN

Sum of Agent Transferred In Count

This count is incremented when an agent initiates a blind transfer call to a Queue or an EntryPoint.

(Calls Handled + Agent to DN Transfer Count) / (Calls Presented + Agent Transferred In Count + Blind Transfer Count - Agent To Queue Transfer Count) x 100

Average time taken for calls to be handled in the queue.

Average of Handle Time

Total Handle Time / Calls Handled

The longest duration taken to handle any call within the queue.

maximum (talkTime + holdTime + workTime)

Average time that the calls spent in the queue before being abandoned.

Average of Queue Duration

Maximum time a call spent in the queue before being abandoned.

Maximum Queue Duration

Average Speed of Answer

Handle Type is one of the following:

- normal

- sudden_disonnect

- dequeued

Is Within service Level = 1

Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count)

Is Within service Level = 1

Average time spent by a call in the queue.

Average of Queue Duration

The maximum time a call spent waiting in the queue.

Calls Transferred to DN

Number of calls that were transferred to a dial number (DN) by blind transfer node via flow.

If you want the calls transferred to DN count to be incremented, contact Cisco Support as the corresponding feature flag may have to be enabled.

Handle type is TransferToDN .

Count of Contact Session ID

Percentage Calls Transferred to DN

Percentage of calls that were transferred to a dial number (DN) by blind transfer node via flow.

(Calls Transferred to DN / Calls Presented) x 100

It is calculated by subtracting these categories from the total number of Calls Presented.

A value of 0 indicates that the calls presented and handled are equal for a queue during the specified time range.

.

###### Queue Call Distribution Summary

The Queue Call Distribution Summary report presents the number and percentage of calls that are handled and dequeued in four configurable time intervals in seconds (0-15, 0-30, 0-45, 0-60).

Report Path : Stock Reports > Historical Reports > Queue Reports

Output Type : Table

Parameter

Description

Filters

Formula

Queue Name

The name of the queue.

Used As : Row Segment

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Handle Type is normal or sudden_disonnect .

Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count)

Number of handled calls with a queue time that is less than or equal to 15 seconds.

Queue Duration <= 15000 ms

Connected Count (Queue Duration <= 15000 ms) + CTQ Handled Count+ Outdial CTQ Handled Count - (Blind Transfer Count (Queue Duration <= 15000 ms) + Agent Transferred In Count (Queue Duration <= 15000 ms))

Queue Duration <= 30000 ms

(Total Calls Handled with Queue Time in 0-30 seconds / Calls Handled) x 100

Queue Duration <= 45000 ms

(Total Calls Handled with Queue Time in 0-45 seconds / Calls Handled) x 100

Number of handled calls with a queue time that is less than or equal to 60 seconds.

Queue Duration <= 60000 ms

Percentage of handled calls with a queue time that is less than or equal to 60 seconds.

(Total Calls Handled with Queue Time in 0-60 seconds / Calls Handled) x 100

Total Calls Handled with Queue Time > 60 seconds

Number of handled calls with a Queue time that is greater than 60 seconds.

Queue Duration > 60000 ms

Handle type is normal or sudden_disonnect .

Connected Count (Queue Duration > 60000 ms ) + CTQ Handled Count + Outdial CTQ Handled Count - (Blind Transfer Count (Queue Duration > 60000 ms) + Agent Transferred In Count (Queue Duration > 60000 ms))

Percentage of Calls Handled with Queue Time > 60 seconds

Percentage of handled calls with a Queue time that is greater than 60 seconds.

(Total Calls Handled with Queue Time > 60 seconds / Calls Handled) x 100

Queue Duration <= 15000 ms

Percentage of abandoned calls with a queue time that is less than or equal to 15 seconds.

(Total Calls Abandoned with Queue Time in 0-15 seconds / Calls Abandoned) x 100

Queue Duration <= 30000 ms

Percentage of Calls Abandoned with Queue Time in 0-30 seconds

Percentage of abandoned calls with a queue time that is less than or equal to 30 seconds.

(Total Calls Abandoned with Queue Time in 0-30 seconds / Calls Abandoned) x 100

Queue Duration <= 45000 ms

Percentage of abandoned calls with a queue time that is less than or equal to 45 seconds.

(Total Calls Abandoned with Queue Time in 0-45 seconds / Calls Abandoned) x 100

Queue Duration <= 60000 ms

Percentage of abandoned calls with a queue time that is less than or equal to 60 seconds.

(Total Calls Abandoned with Queue Time in 0-60 seconds / Calls Abandoned) x 100

Total Calls Abandoned with Queue Time > 60 seconds

Percentage of abandoned calls with a Queue time that is greater than 60 seconds.

Queue Duration > 60000 ms

Count of Contact Session ID

Percentage of Calls Abandoned with Queue Time > 60 seconds

Percentage of abandoned calls with a Queue time that is greater than 60 seconds.

(Total Calls Abandoned with Queue Time > 60 seconds / Calls Abandoned) x 100

Additional information on Queue-based Reports

Consider the following additional information associated with various QBR parameters and metrics:

For Consult to Queue/EP scenarios, the call records do not get marked as abandoned if the agent does not pick up the call upon ringing.

For Consult To DN scenarios, the Consult Success Count is incremented regardless of whether the consult was successful or not.

For Transfer to DN scenarios that use Blind Transfer node, calls handled will not be updated. However, the handleType = Transfer_to_DN can be queried to match the count.

When a call is placed on hold during a consultation, the Hold Duration is included as part of the Consult Duration for that specific consultation. This is due to the absence of a separate Hold Duration counter for consult records.

#### Real-time Reports

Real-time reports have specific refresh intervals. You can select a value between 5
        to 60 seconds from the Refresh drop-down with increments of 5 seconds. All new real-time
        reports have a default refresh interval of 5 seconds and you can change it to the other
        available values as needed. All existing reports with refresh intervals of less than 5
        seconds will default to 5 seconds.

While running a real-time report, you can have more filtering capability. Hover on the table header to see the Hamburger Menu icon. Click the Hamburger Menu icon to open the filter drop-down. You can select or deselect the appropriate entities in the filter drop-down. You can close and reopen the filter drop-down to see the original filter selection.

While selecting or deselecting the appropriate entities in the filter drop-down, if a report refresh window occurs:

- All the checkboxes in the filter drop-down get selected in this refresh window.

- To continue the filter selection, wait until this refresh is complete, close and reopen the
          filter drop-down.

You can select the filters between the refresh intervals.

These reports aren't available for Cloud Connect users.

##### Agent Reports Real-time

Agent interval reports display cumulative and derived values at the site, team, or agent level.

###### Interval Report-Agent

###### Agent Interval Realtime

This report represents a cumulative and derived value when an agent is connected to a channel type.

Report Path : Stock Reports > Real-Time Reports > Agent Reports > Interval Reports

Output Type : Table

The name of an agent, that is, a person who answers customer calls.

Used As : Row Segment

Time Period

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

The total amount of time agents were logged in.

Sum of Realtime Update Timestamp - Sum of Login Timestamp

The measure of time agents spent on calls compared to available and idle time.

(Sum of Outdial Wrapup Duration + Sum of Wrapup Duration ) + (Sum of Outdial Connected Duration + Sum of connected duration) / (Sum of Available Duration + Sum of Idle Duration + Sum of Not Responding Duration) + (Sum of Connected Duration + Sum of Wrapup Duration + Sum of Outdial Connected Duration + Sum of Outdial Wrapup Duration)

The total number of calls from all origination types.

The total amount of time the agents spent in the Idle state.

The total amount of time the agents spent in the Available state.

The total amount of time the agents spent in the Reserved state (time duration once the call starts ringing and before the call is answered).

The total amount of time an agent was talking with a caller.

The number of times an agent put an inbound caller on hold.

The total amount of

The total amount of time the agents spent in the Wrap-up state after an inbound call.

The average inbound connected time.

The average length of time agents were in the Wrap-up state after an inbound call.

The total amount of time the agents spent in the Not Responding state.

The number of times an agent was in the Outdial Reserved state (time duration once the call starts ringing and before the call is answered).

The number of outdial calls that got connected to an agent.

The total amount of time the agents were in the Outdial Reserved state.

The total amount of time the outdial calls were on hold.

The amount of time the agents got connected to outdial calls.

The total amount of time agents spent in the Wrap-up state after an outdial call.

The average outbound connected time.

The average length of time spent handling an outdial call (Total Outdial Connected Time plus Total Outdial Wrap Up Time, divided by Outdial Connected Count).

The sum of time during which the agent was engaged in the activity.

Shows the total amount of time an agent was engaged.

Sum of Engaged Duration

Click the Skill Profile or Skills table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. You can see the following details:

Shows the next login date and time for an agent whose skill profile/skills were updated when logged out, or the date and time when the skill profile/skills were updated for an agent who is currently logged in.

Skill Profile

Shows the name of the skill profile that is associated with an agent.

Skills

Shows the skill of an agent, such as language fluency or product expertise. The column shows multiple skills mapped to the corresponding skill profile, in a comma-separated single string.

###### Agent Outdial Statistics Realtime

This report represents the number of outdial calls made by an agent in real time.

Report Path : Stock Reports > Real-Time Reports > Agent Reports > Interval Reports

Output Type : Table

Parameter

Description

Formula

Agent Name

The name of an agent, that is, a person who answers customer calls.

Used As : Row Segment

Channel Type

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Login Time

The date and time the agent logged in.

Outdial Contact Handled

The number of outbound calls handled.

Sum of Outdial Connected Count

Outdial Average Handle Time

The average handle time for outbound calls.

(Outdial Connected Time + Outdial Wrapup Time) / Outdial Calls

Outdial Connected Time = Sum of Outdial Connected Duration.

Outdial Wrapup Time = Sum of Outdial Wrapup Duration.

Outdial Calls = Outdial Attempted Count + Outdial Contact Handled

Outdial Attempted Count = Sum of Outdial Count.

Outdial Connected Time

The total amount of time an agent was talking with a party on an outdial call.

Sum of Outdial Connected Duration

Outdial Average Connected Time

The average of outdial connected time.

Outdial Connected Time / Outdial Contact Handled

Outdial Talk Time

The total amount of time an agent was talking with a party on an outdial call.

Outdial Hold Duration = Sum Of Outdial Hold Duration

###### Site Interval Realtime - Chart

This report represents the number of answered contact types for a site.

Report Path : Stock Reports > Real-Time Reports > Agent Reports > Interval Reports

Output Type : Bar Chart

Channel Type: chat, telephony, email, social

###### Team Interval Realtime Report-Chart

This report represents the number of contact types answered for a team.

Report Path : Stock Reports > Real-Time Reports > Agent Reports > Interval Reports

Output Type : Bar Chart

###### Snapshot Report-Agent

###### Agent Realtime

This report represents a detailed summary of the agent statistics.

Report Path : Stock Reports > Real-Time Reports > Agent Reports > Snapshot Reports

Output Type : Table

Count of Agent Session ID

Activity State: Idle, idle

Activity State: Available, available

The number of times agent currently in the Reserved state (where the incoming call
                isn’t yet answered).

Activity State: Ringing, ringing

Activity State: Connected, connected

Activity State: Available consulting, available-consulting, ConnectedConsulting

Activity State: Conferencing, conferencing

Activity State: Wrapup, wrapup

The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent.

Activity State: Not Responding, not-responding

(Activity State =NotResponding)

Is Outdial: >= 1

Shows the number of times the agent went into the Engaged state.

Sum of Engaged Count

###### Agent Statistics Realtime

This report represents the agents statistics in real time. It captures agent details like the login time, channel type, and so on.

The Social column appears only if the Social Channel SKU is subscribed.

Report Path : Stock Reports > Real-Time Reports > Agent Reports > Snapshot Reports

Output Type : Table

The name of the agent.

The media type of the contact, such as telephony, email, or chat.

The current state of the contact. This field is available only in the Customer Session Repository (CSR), and only for real-time visualizations.

The total number of voice interactions handled.

The total number of chat interactions handled.

Value of Outdial Connected Count (Channel Type: chat) + Value of Connected Count (Channel Type: chat)

The total number of email interactions handled.

Value of Outdial Connected Count (Channel Type: email) + Value of Connected Count (Channel Type: email)

The total number of social channel interactions handled.

Social Connected Count + Social Outdial Connected Count

###### Agent Statistics by Queue – Realtime

This report presents real-time performance metrics of agents, categorized by queue. It enables supervisors to monitor activity, evaluate efficiency, and make informed decisions to enhance operational effectiveness.

Report Path : Stock Reports > Real-Time Reports > My Team & Queue Stats

Output Type : Table

The name of the queue.

##### Contact Center Overview - Real-Time

- If an agent is currently engaged in a call, the Contact Center Overview Real-Time dashboard doesn't display data for the agent. Reports are only displayed for the available agents.

###### Agents Available Card Real-Time

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Card

###### Average Service Level Card Real-Time

This gauge chart shows the percentage of contacts that were handled within the configured service level for a queue.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Chart

###### Contact Details in Queue - Today Real-Time

This report provides contact details for contacts from the start of the day broken down by queue.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Table

Parameter

Description

Filters

Formula

Channel Type

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Queue Name

The name of the queue.

# Contacts

The total number of contacts since the start of the day.

# Contacts Handled

Number of contacts handled since the start of the day.

Handle Type: normal

Longest Handled Contact from Queue

The longest duration that a contact spent in queue since the start of the day.

This is calculated after the call status changes from parked to connected or ended.

Current State: connected, ended

# Abandoned Contacts

Number of abandoned contacts since the start of the day.

Termination Type: abandoned

###### Contact Details Currently in Queue Real-Time

This report provides contact details of contacts currently in Queue.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Table

Parameter

Description

Filters

Formula

Channel Type

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Queue Name

The name of the queue.

# Contacts Waiting in Queue

Number of contacts waiting in queue.

Current State: parked

Avg Queue Wait Time

Average Queue Wait Time of all the calls that are currently active.

Current State: connected, ended

Average of QueueDuration

###### Avg Queue Wait Time Card

This report provides the Average Queue Wait Time of all the calls that are currently active.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Card

###### Contacts in Queue Card Real-Time

This report provides the number of customer contacts that are in queue in real-time.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Card

###### Longest Contact in Queue Card

This report shows the contact that is in queue for the longest duration at that point in time. This value is populated from a snapshot report for the contact that is currently parked in a queue for the longest duration. This is a real-time report.

This report provides the queue name and duration of the contact with the longest queue wait time.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Report

###### Team Details Real-Time

This report provides team details in real-time.

The Social column appears only if the Social Channel SKU is subscribed.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Table

Parameter

Description

Formula

Team Name

Agent Name

Name of the agent.

The media type of the contact, such as telephony, email, or chat.

Used As : Row Segment

Total Log In Count

The total number of contacts that were logged in.

(Cardinality provides the total number of unique Agent Session IDs.)

Initial Login Time

Final Logout Time

Staff Hours

Sum of Realtime Update Timestamp - Sum of Login Timestamp

Idle Counts

Total count of idle state.

Sum of Idle Count

# Contacts Handled

The number of contacts handled.

Sum of Connected Count

# Calls Handled

The number of calls that were handled.

Voice Connected Count

# Chats Handled

The number of chats that were handled.

Chat Outdial Connected Count

# Emails Handled

The number of emails that were handled.

Email Connected Count

The total number of social channel interactions handled.

Social Connected Count + Social Outdial Connected Count

###### Total Abandoned Contacts Card Real-Time

The report provides the total number of contacts that are Abandoned in real-time.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Card

##### Multimedia Reports Real-time

###### Interval Reports

###### Abandoned Realtime

This report represents the number of calls that were in the system before they got abandoned.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Interval Reports

Output Type : Table

Filters

Time Period

Used As : Row Segment

Used As : Row Segment

Used As : Row Segment

Termination Type: abandoned

Is Contact Handled: != 1

###### Entry Point Interval Realtime - Chart

This report represent the number of incoming calls.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Interval Reports

Output Type : Bar Chart

###### Incoming, Short, IVR RealTime - Entry point

This report represents the number of channel types that were in the IVR.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Interval Reports

Output Type : Table

Time Period

Used As : Row Segment

Used As : Row Segment

Termination Type: short_call

###### Queue Service Level Realtime

This report represents the number of channel types available real time in the queues. A detailed report comprising of abandoned, service level, completed, and other parameters.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Interval Reports

Output Type : Table

Used As : Row Segment

Time Period

Used As : Row Segment

Termination Type: abandoned

###### Sites Contact Details Realtime - Chart

This report represents the site details.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Interval Reports

Output Type : Bar Chart

###### Snapshot Reports

The Connected Duration field in the Snapshot Report is populated with zeros when the call is in progress. The Connected Duration field in the Snapshot Report is populated with values only after the call ends.

###### Longest Queued Contact

The longest queued contact report indicates the longest duration for which a contact had to wait in a specific queue. The report provides the time for which the contact waited in the queue. The report also identifies the contact that has been currently waiting in the queue for the longest duration.

Report path : Stock Reports > Real-Time Reports > Multimedia
            Reports > Snapshot Reports

Output Type : Table

Parameter

Description

Queue ID

The unique identifier for a queue.

Queue Name

The name of a queue.

Skills assigned in

Indicates where skills are assigned.

The following are the values:

- For the current Skill-Based Routing Team's queue, the value is 'Flow'.

- For the Skill-based queue, the value is ‘Queue’.

- For the Agent-based queue, the value is ‘NA’.

Channel Type

Media type of the queue such as telephony, email, or chat.

Longest Queued Contact Time

Longest time for which a contact waited in the queue.

###### Snapshot Entry Point IVR Realtime - Chart

This report represents the number of calls currently available in the IVR.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Snapshot Reports

Output Type : Bar Chart

Current State: ivr-connected

###### Snapshot Entry Point Realtime

This report represents snapshot details of calls in an entry point or in a queue.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Snapshot Reports

Output Type : Table

Used As : Row Segment

Used As : Row Segment

Current State: ivr-connected

Current State: parked

Current State: connected, on-hold, hold-done, consult-done, consulting

###### Snapshot Entry Point Realtime - Chart

This report represents a snapshot of the contact type.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Snapshot Reports

Output Type : Bar Chart

In Queue

Then number of queues contact entered.

Current State: parked

Count of Contact Session ID

Connected

The total number of calls handled.

Current State: connected, on hold

Count of Contact Session ID

###### Snapshot Queue Realtime - Chart

This report represents a snapshot of the service-level.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Snapshot Reports

Output Type : Bar Chart

Current State: parked

Current State: connected, on-hold

###### Snapshot Queue Service Level Realtime

This report represents the service-level at a team, queue, and a site level.

Report Path : Stock Reports > Real-Time Reports > Multimedia Reports > Snapshot Reports

Output Type : Table

Used As : Row Segment

Skills assigned in

Indicates where skills are assigned.

The following are the values:

- For the current Skill-Based Routing Team's queue, the value is 'Flow'.

- For the Skill-based queue, the value is ‘Queue’.

- For the Agent-based queue, the value is ‘NA’.

Used As : Row Segment

Used As : Row Segment

Used As : Row Segment

Current State: parked

Current State: connected, on-hold, hold-done, consulting, consult-done

Current Service Level % = In service level / Total

##### Team and Queue Stats - Real-Time

###### Average Handle Time Card Real-Time

This report displays the average handled time of each individual channel and for all the channels in real-time.

Report Path : Stock Reports > Real-Time Reports > Team & Queue Stats

Output Type : Card

###### Team Stats Real-Time

This report displays the team statistics in real-time.

Report Path : Stock Reports > Real-Time Reports > Team & Queue Stats

Output Type : Table

Parameter

Description

Formula

Team Name

Agent Name

Current State

Shows the state of the agent such as Available, Idle, or Not Responding.

# Contacts Handled

Number of Inbound contacts handled.

Total number of inbound contact session IDs

Average Handle Time

Average time taken to handle a contact.

Total amount of contact time during the specified interval/The number of contacts handled during the specified interval

Average Wrapup Time

Average time taken to wrap up a contact.

Total Wrapup time during the specified interval/Total number of Wrapups during the specified interval

###### Team State Chart Real-Time

This pie chart breaks down the number of logged-in agents by current state for telephony
      only.

Report Path : Stock Reports > Real-Time Reports > Contact Center Overview

Output Type : Chart

###### Total Handled Card Real-Time

This report displays the total number of contacts that are handled in real-time.

Report Path : Stock Reports > Real-Time Reports > Team & Queue Stats

Output Type : Card

#### Transition Reports

Transition Reports are Stock Reports designed specifically for customers who are transitioning from UCCX to WxCC. These reports were behind a Feature Flag and were enabled through ad-hoc requests. Henceforth, these reports will be available without the need for a Feature Flag request and can be accessed anytime by all users.

##### Abandoned Call Detail Activity Report

The Abandoned Call Detail Activity Report presents information about calls that were abandoned.

This transition report uses termination type as the filter containing both 'abandoned' and 'short_call' fields.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

Call Start Time

Timestamp when the contact started.

Value of Contact Start Timestamp

Called Number

DNIS digits delivered with the call.

The telephone company sends a Dialed Number Identification Service (DNIS) digit string that contains the caller's phone number.

Value of DNIS

Call ANI

ANI digits delivered with a call.

The telephone company sends an Automatic Number Identification (ANI) digit string that contains the caller's phone number.

Value of ANI

Call Routed CSQ

Name of the queue that the call was placed while waiting for an agent.

Value of First Queue Name

Agent

Name of the agent who received the call before the call was abandoned.

Value of Agent Name

Call Skills

Skills that were associated with the queue to which the call was routed.

Value of Skills

Skills assigned in

Indicates where skills are assigned.

The following are the values:

- For the current Skill-Based Routing Team's queue, the value is 'Flow'.

- For the Skill-based queue, the value is ‘Queue’.

- For the Agent-based queue, the value is ‘NA’.

Call Abandon Time

Date and time when the call was abandoned.

Value of Contact End Timestamp

Time to Abandon

The amount of time that elapsed between the time the call came in to the system and the time it was abandoned.

Call Abandon Time - Call Start Time

##### Agent Call Summary Report

The Agent Call Summary Report presents the summary of each call that was dialed and received by an agent.

Call details are counted against the last agent handling the call.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

Agent Name

Name of an agent. Used as a Row Segment.

Agent Endpoint (DN)

The endpoint (number, email, or chat handle) on which an agent received calls, chats, or emails. Used as a Row Segment.

Total Inbound

Total calls that an agent received.

Count of Contact Session ID (Call Direction = inbound)

Avg Talk Time Inbound

Average time that an agent spent talking with a caller.

Average of Connected Duration (Call Direction = inbound)

Avg Hold Time Inbound

Average time that an agent put an inbound call on hold.

Average of Hold Duration (Call Direction = inbound)

Avg Work Time Inbound

Average time that an agent was engaged after disconnecting or transferring an inbound call.

Average of Wrapup Duration (Call Direction = inbound)

Outbound Calls

Calls that an agent made. This includes both connected and attempted calls.

Count of Contact Session ID (Call Direction = outdial)

Avg Call Time Outbound

Average time that an agent was engaged in an outbound call.

Average of Connected Duration (Call Direction = outdial)

Max Call Time Outbound

Maximum time that an agent was engaged in an outbound call.

Maximum Connected Duration (Call Direction = outdial)

Transfer In

Calls that were transferred to an agent.

'Transfer In' count increases when a consult transfer occurs.

Sum of Agent Transferred In Count

Transfer Out

Calls that an agent transfered out.

'Transferred Out' count increases when a blind transfer occurs.

Sum of Agent To Agent Transfer Count + Sum of Agent To DN Transfer Count + Sum of Agent To Queue Transfer Count + Sum of Agent To Entrypoint Transfer Count

Conference

Conference calls in which an agent participated.

Sum of Conference Count

##### Agent Detail Report

The Agent Detail Report presents information about Automatic Call Distribution (ACD) and non-ACD calls that agents received or dialed.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

Agent Name

Name of an agent.

Value of Agent Name

Extension

Endpoint (number, e-mail, or chat handle) on which an agent received calls, chats, or emails.

Value of Agent Endpoint (DN)

Call Start Time

Date and time when the call started.

Value of Contact Start Timestamp

Call End Time

Date and time when the call ended.

Value of Contact End Timestamp

Duration

Elapsed time between the call start time and the call end time.

Call End Time - Call Start Time

Called Number

DNIS digits delivered with the call.

The telephone company sends a Dialed Number Identification Service (DNIS) digit string that contains the caller's phone number.

Value of DNIS

Call ANI

ANI digits delivered with a call.

The telephone company sends an Automatic Number Identification (ANI) digit string that contains the caller's phone number.

Value of ANI

Call Routed CSQ

Name of the queue that held the calls waiting for an agent.

Value of First Queue Name

Other CSQs

Name of the final queue where the call waited for an agent when there were multiple queues used.

Value of Final Queue Name

Call Skills

Skills that were associated with the queue that handled the call.

Value of Skills

Skills assigned in

Indicates where skills are assigned.

The following are the values:

- For the current Skill-Based Routing Team's queue, the value is 'Flow'.

- For the Skill-based queue, the value is ‘Queue’.

- For the Agent-based queue, the value is ‘NA’.

Talk Time

Elapsed time between the time an agent connected to the call and the time the call was disconnected or transferred, not including the hold time.

Value of Connected Duration

Hold Time

Total amount of time that an agent put the calls on hold.

Value of Hold Duration

Work Time

Total amount of time that an agent was engaged after disconnecting or transferring a call.

Value of Wrapup Duration

Call Direction

Indicates if the call was an inbound call or an outbound call.

Value of Call Direction

##### Agent Summary Report

The Agent Summary report contains one row for each agent. Each row contains a summary of the activities of an agent.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

Agent Name

Name of an agent. Used as a Row Segment.

Calls Handled

Number of calls that were connected to an agent.

If the agent established a conference with another agent, the value increases by one for the conferenced agent.

If the agent transferred a call and the call was transferred back to the agent, the value increases by two.

Count of Wrapup Code Name

Calls Presented

Number of calls that were sent to the agent, regardless of whether the agent picked up the call.

If a call was connected to an agent, transferred to another agent, and then transferred back to the original agent, the value for the original agent increases by two (once for each time the call was presented).

Count of Contact Session ID

Handled Ratio

Ratio of calls handled by an agent to the calls presented to the agent.

Calls Handled / Calls Presented

Avg Handle Time

Average handle time for all calls that the agent handled.

Total Handle Time / Calls Handled

Average Talk Time

Average time that an agent spent in a call.

Average of Connected Duration

Max Talk Time

Maximum time that an agent spent in a call.

Maximum Connected Duration

Average Hold Time

Average time that an agent put a call on hold.

Average of Hold Duration

For mulitple agent sessions, the Average of Hold Duration is
                                    calculated as Total Hold Duration / Number of agent sessions on
                                    which the hold duration.

Max Hold Time

Maximum time that an agent put a call on hold.

Maximum Hold Duration

Average Work Time

Average time that an agent was engaged after disconnecting or transferring a call.

Average of Wrapup Duration

Max Work Time

Maximum time that an agent was engaged after disconnecting or transferring a call.

Maximum Wrapup Duration

##### Application Summary Report

The Application Summary Report presents call statistics for each application. It includes information for presented, handled, abandoned, flow-in, and flow-out calls. It also includes information about call talk time, work time, and abandon time.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

Entrypoint Name

Name of an entry point. Used as a Row Segment.

Calls Presented

Number of calls that were received by an application, including internal calls. It includes the number of calls that were handled by the application and the number of calls that were abandoned while in the application.

Count of Contact Session ID

Calls Handled

Number of calls that were handled by the application including internal calls.

Count of Contact Session ID (Termination Type = normal

Avg Speed of Answer

Average queue time before an agent answered a call. Calls that did not connect to an agent are not included in this calculation.

Average of Queue Duration

Avg Talk Time

Average time that an agent spent in a call.

Average of Connected Duration

Avg Work Time

Average time that an agent was engaged after disconnecting or transferring a call.

Average of Wrapup Duration

Calls Abandoned

Number of calls that were abandoned by the application.

Count of Termination Type (Termination Type = abandoned)

Avg Abandon Time

Average duration of calls before they were abandoned.

Average of Queue Duration (Termination Type = abandoned)

##### CSQ Activity Report by Window Duration

The Contact Service Queue (CSQ) Activity by Window Duration presents information about service levels, and the number and percentage of calls that were presented, handled, abandoned, and dequeued. It presents information for a 30-minute or 60-minute interval within the report period. The report can be filtered for specific window duration for a single day or multiple days. Unlike other reports, the time part of interval filter is considered as window duration in this report.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

First Queue Name

Name of the queue. Used as a Row Segment.

Interval

Time Period. Used as a Row Segment.

Start Time

Timestamp when the contact started.

Minimum Contact Start Timestamp

End Time

Timestamp when the contact ended.

Maximum Contact End Timestamp

Calls Presented

Number of calls that were routed to the queue, regardless of whether an agent picked up the call.

Count of Contact Session ID

Calls Handled

Number of calls that were handled by the queue.

Count of Contact Session ID (Termination Type = normal)

Calls Abandoned < SL

Number of calls that were abandoned within the time shown in the Service Level field.

Count of Contact Session ID (Is Within service Level = 1, Termination Type = abandoned)

Calls Abandoned

Number of calls that were routed to the queue and were abandoned.

Count of Contact Session ID (Termination Type = abandoned)

Abandon Rate

Percentage of calls that were routed to the queue and were abandoned.

Calls Abandoned / Calls Presented

##### CSQ Agent Summary Report

The CSQ Agent Summary Report presents information about calls that were handled in each queue for each agent. An agent can handle calls for multiple queues. This report includes the average and total talk time for handled calls, average and total work time after calls, total ring time of calls routed, number of calls put on hold, average and total hold time for calls put on hold, and number of unanswered calls.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

First Queue Name

Name of the queue. Used as a Row Segment.

Agent Name

Name of an agent. Used as a Row Segment.

Calls Handled

Number of calls that were answered by an agent in a queue during the report period.

Count of Wrapup Code Name

Avg Talk Time

Average time that an agent spent for calls in a queue.

Average of Connected Duration

Total Talk Time

Total time that an agent spent for calls in a queue.

Sum of Connected Duration

Avg Work Time

Average time that an agent spent after disconnecting or transferring calls in a queue.

Average of Wrapup Duration

Total Work Time

Total time that an agent spent after disconnecting or transferring
                                calls in a queue.

Sum of Wrapup Duration

Total Ring Time

Elapsed time between the time when a call ringed and the time the call was answered by an agent, routed to another agent, or disconnected.

Sum of Ringing Duration

Avg Ring Time

Average time between the time when a call ringed and the time the call was answered by an agent, routed to another agent, or disconnected.

Average of Ringing Duration

Calls On Hold

Calls that the agent put on hold.

Sum of Hold Count

Avg Hold Time

Average time for calls that the agent put on hold.

Average of Hold Duration

Total Hold Time

Total time for calls that the agent put on hold.

Sum of Hold Duration

##### CSQ All Fields Report

The CSQ All Fields Report presents the queue-related data such as call statistics, service level, and key fields like Average Queue Time, Average Speed of Answer, Calls Handled, and Calls Abandoned under service level. This report combines the fields of all queue-related reports.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

Queue Name

Name of the queue. Used as a Row Segment.

In Service Level%

Number of calls that were answered within the Service Level threshold provisioned for the queue.

In Service Level / Calls Presented

Calls Presented

Number of calls that were routed to the queue, regardless of whether an agent picks up the call.

Count of Contact Session ID (Channel Type = telephony)

Calls Handled

Number of calls that were handled by the queue.

Count of Contact Session ID (Termination Type= normal, Channel Type = telephony)

Percentage Handled

Percentage of calls that were handled by the queue.

Calls Handled / Calls Presented

Average Handled Time

Average time for all calls that the queue handled.

Total Handle Time / Calls Handled

Max Connected Time

Maximum time that an agent spent in calls handled by the queue.

Maximum Connected Duration

Calls Abandoned

Number of calls that were routed to the queue and are abandoned.

Count of Contact Session ID (Termination  Type = abandoned)

Percentage Abandoned

Percentage of calls that were routed to the queue and were abandoned.

Calls Abandoned / Calls Presented

Avg Abandoned Time

Average time that the calls spent in the queue before being abandoned.

Average of Queue Duration (Termination Type = abandoned)

Max Abandoned Time

Maximum time a call spent in the queue before being abandoned.

Maximum Queue Duration (Termination Type = abandoned)

Avg Speed of Answer

Average queue time before an agent answered a call.

Answered Time / Answered

##### Multichannel Agent Summary

The Multichannel Agent Summary Report presents a summary of the agent performance over inbound, outbound, chat, and email channels.

Report Path : Stock Reports > Transition Reports

Output Type : Table

Parameter

Description

Formula

Agent Name

Name of an agent. Used as a Row Segment.

In Calls Presented

Number of calls that were sent to an agent, regardless of whether the agent picked up the call.

Count of Contact Session ID (Channel Type = telephony, Call Direction = inbound)

In Calls Handled

Number of calls that were connected to an agent.

Count of Contact Session ID (Termination Type = normal, Channel Type = telephony, Call Direction type = inbound)

Handle Time Avg

Average handle time for all calls that the agent handled.

Average of Wrapup Duration + Average of Connected Duration  (Channel Type = telephony, Call Direction = inbound)

Outdial Talk Time Max

Maximum talk time of any call that an agent handled.

Maximum Connected Duration (Channel Type = telephony, Call Direction = outdial)

Outdial Talk Time Avg

Average talk time of any call that an agent handled.

Average of Connected Duration (Channel Type = telephony, Call Direction = outdial)

Chat Presented

Number of chats that were presented to the agent.

Count of Contact Session ID (Channel Type = chat)

Chats Handled

Number of chats that the agent accepted.

Count of Wrapup Code Name (Channel Type = chat)

Chat Active Time Max

Maximum time that an agent spent in a chat.

Maximum Connected Duration (Channel Type = chat)

Chat Active Time Avg

Average time that an agent spent in a chat.

Emails Presented

Number of email messages that were presented to the agent.

Count of Contact Session ID (Channel Type = email)

Emails Handled

Number of email messages that the agent replied and forwarded. The send date and time determines whether the email message falls within the interval.

Count of Wrapup Code Name (Channel Type = email)

### Change Report Column Width

By default, the column width in tabular reports is aligned with the column title length. You can change the column width dynamically while running reports. If you change the column width, the updated width is saved in your computer for your user ID. The column width remains the same even if you refresh the browser or log out and log back in using the same browser. You can reset the column width to the default width by clearing the browser cache.

If the changed column width is lesser than that of the column title, an ellipsis icon is shown.

If you change the column width, the updated width is not saved for Threshold Alerts.

### Drill Down to a Portion of the Visualization

After you run a visualization in table format, you can drill down into a specific visualization component to see all the records that were involved in the computation of that portion of the visualization and perform further analytics on the data set.

The Drill Down functionality is not available for reports that are accessed through browser links and for the APS reports in the Agent Desktop.

Click on a table cell and then click the Drill Down icon.

The drill-down option is available only for the Column or Profile Variables set during the report creation process. Users will be able to drill down and have a detailed view of these fields, but not for row segments. Users are advised to structure the reports across Column or Profile Variables so that the desired details are accessible through the drill-down.

The Drill Down panel displays the records involved in the computation of the visualization.

If you drill down on a session ID (whether it is a contact or agent session ID), it drills down to the activities composing that session.

To add a field or a profile variable, click an entry from the Fields or Measures drop-down
                    list to append a new column.

If you select a Field or Measure that already exists in the table, then it will not add the field again.

To export the report data as a Microsoft Excel or CSV file, click Export . The export option is not available for a Drill Down report with real-time data.

To view the Drill Down panel in a
                    separate window, click the Launch icon.

### Modify Visualization Attributes

After running a visualization, you can modify its attributes and rerun it:

Click Settings .

To show or hide the summary of column values at the table level and the top-level row segment, select the values from the Show Summary drop-down list.

If you want the visualization to be updated immediately, select Redraw instantly . Otherwise, the visualization will be updated only when you click the Apply button.

To show or hide a profile variable, click the eye icon.

To hide a segment, drag it to the Hidden Segments box. This capability is not available for compound visualizations.

To reposition a segment, drag it to a different location either within its current Segments box or to a different Segments box. This capability is not available for compound visualizations.

To filter a segment:

Select the is in or is not in option, and specify the values to include or exclude. For more information, see Filter using Data Filter

Select the regular expression to enter an expression to be included or excluded.

Click Save .

Changes are always rendered immediately when you filter a segment and when you show or hide a profile variable.

If the visualization is a chart, select the Settings icon to modify the visualization.

### Change the Visualization Output Format

Click Settings .

Select a format from the drop-down list. The possible formats are:

Description

Table

Displays data in rows and columns.

Heat Map

Displays the cell values within a table in different
                                            shades of red.

The cells in white and the darkest shade of red identify
                                            the outliers.

Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Heat Maps for such reports.

Row Heat Map

Displays the cell values within each row in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a row.

Row Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Row Heat Maps for such reports.

Column Heat Map

Displays the cell values within each column in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a column.

Line Chart

Compares values as points connected by lines.

Bar Chart

Compares values displayed as horizontal columns.

Area Chart

Pie Chart

When converting an existing visualization to a KPI
                                                card, ensure the first profile variable is correctly
                                                set, as other variables will not be rendered on the
                                                card.

Sparkline Chart

To provide a more consistent experience across Webex Contact Center, we
                            are standardizing the visual design and formatting options in Analyzer.
                            The overall experience remains the same. You can continue to create,
                            view, and use reports and dashboards as you do today. The update is
                            primarily visual, with only a few minor formatting options being
                            streamlined to align with Webex design standards.

Formatting Options

In the new visual design, to maintain consistency across all Webex
                            products, we have updated the available formatting options. Please refer
                            to the list below for details on supported and removed features:

- Supported Title Options: Font Size and Text Align

- Supported Chart Options : Gradient Fill, Stacking, Axis
                                Labels, Invert Axis, Data Labels and Data labels rotation.

The following properties have been removed or are no longer supported as
                            manual customizations:

- Unsupported Title Options: Back Color, Border Size, Border
                                Style, Border Color, Font Family, Font Style, Font Weight, Text
                                Color, Text Decoration, Margin Top, Margin Bottom, Margin Left,
                                Margin Right, Padding Top, Padding Bottom, Padding Left and Padding
                                Right.

- Unsupported Chart Options: Back Color, Border Size, Border
                                Style and Border Color.

Some of these unsupported formatting options may still appear temporarily
                            in the updated look, but they will not be applied when reports and
                            dashboards are viewed. They will continue to work in the previous look
                            until it is retired.

The previous look will remain available for a limited time. Once it is
                            retired, these unsupported formatting options will also be fully
                            retired.

Motion Charts are no longer supported.

- When you create a new report, the Motion
                                    Chart option is unavailable in the Output
                                    Type drop-down list.

- When you edit an existing Motion Chart report, the Motion
                                    Chart option appears in gray in the Output Type drop-down list. Save and Preview options are unavailable.

- When you run an existing Motion Chart report, the UI displays the
                                following error: Unable to render Motion Charts
                                    because it’s no longer supported. Save the report in a different
                                    format.

### Visualization Creation Overview

This chapter describes how to create visualizations using an intuitive drag-and-drop interface.

Select the type of visualization:

Customer Session Record

Customer Activity Record

Agent Activity Record

Agent Session Record

Specify the time period that you want the visualization to cover. This constrains the number of records that will be considered during execution of the visualization.

The compute interval for a historical report can be either time-based or sample-based.

- For a time-based visualization, select a time interval.

- For a sample-based visualization, specify the total number of records to be considered, the frequency (the number of records to be considered in each interval), the band (the number of records to be considered in each calculation), and whether or not the calculations will be cumulative.

Specify what you are trying to compare as part of the visualization. This can be to compare the performance of the different agents or entry points. The Analyzer allows segmentation only by fields and not by measures. For example, segmentation by Termination Type or Agent Name is allowed, segmentation by Call Count is not allowed.

Define the metrics you want to see in the visualization to compare the different segments. Profiling variables are always numeric values and can be created from either fields, measures, or other profiling variables.

Field : Fields can be used to create counts of records that meet specified conditions. For example, you can create a profiling variable that will provide the count of records with a Termination Type equal to normal.

Measure : Measures can be used to create summations, averages, or counts. Summations and averages require no additional input. Counts work the same way as fields, and thus require conditions to be specified. For example, using Revenue as the basis for a profiling variable allows you to create a sum of the revenue, an average of the revenue, or a count of records that have a revenue greater than, less than, or equal to a given amount.

Existing Profile Variable : Profiling variables can be created from other profiling variables using arithmetic formulas. For example, if you already have a profiling variable named Average revenue containing the average of revenue and another profiling variable named Handled Calls containing the count of records where Termination Type equals normal, then you can create a profiling variable containing the average revenue per call using Average revenue divided by Handled Calls.

This step further limits the population set to include only the records that meet the conditions you specify.

A visualization can be displayed as a table or chart. The chart types currently supported are Bar, Pie, Line, Area, and Motion. Additionally, you can specify display options such as titles, colors, and border widths and styles.

Visualizations can be executed on demand, scheduled for a one-time execution, or scheduled to run periodically. Scheduled executions post their results to the specified email recipients as a CSV or a Microsoft Excel file attachment.

For scheduled reports, the maximum file size for email attachments is 10
                            MB and the maximum number of columns supported is 2000.

You can define the execution schedule in one of the following ways:

Execute now : Use Run from the view page.

Execute once and email : Use the Scheduler. Specify the time and email information.

Recurrence : Use the Scheduler and specify the recurrence pattern (such as daily, at 9.00 AM).

- The filters in the Profile Variables and the filters in the left
                                pane on the Visualization page are different. The filters in the
                                profile variables are applicable only to the selected profile
                                variables of that visualization and not to the entire visualization.
                                The filters in the left pane on the visualization page are
                                applicable to the entire visualization.

- For reports with row segments, sorting of data can be done only
                                within the respective row segment group. For example, in the Agent
                                details report, the Agent Name is the first-row segment field. When
                                agent names are sorted in the first column, the data displayed in
                                the subsequent columns is associated only with the selected
                                agent.

### Create a Visualization

To create a visualization:

Select Visualization > Create New > Visualization .

The visualization creation page appears.

The Modules tab displays two panels that you can expand or collapse by clicking a panel title.

Select an option from the Type drop-down list. The possible values are Customer Session Record , Customer Activity Record , Agent Activity Record , or Agent Session Record .

You can add variables and segments to the reports.

Specify the visualization time period by selecting an option from the Start Time drop-down list in the Modules tab.

To create a realtime visualization, select Realtime.

To create a historical visualization, select a predefined date range.

To specify custom start and end dates, select Custom .

If you selected Realtime , go to 9 .

If you selected Custom , select values from the Start Date and End Date drop-down lists.

If you selected Exact Date , enter a date in the field that appears, or click in the field and then select a date from the calendar controls.

If you selected one of the other options— Day of the Year , Day of the Month , 7 Days , Day of the Week , or Most Recent Day —use the controls that appear, to select the options you want.

If you specify a lengthy date range, the visualization could take a long time to run. In this case, it might be preferable to schedule the visualization rather than running it in real-time.

If the pre-defined date range you want to select is not available in the drop-down list, increase the compute interval. Small compute intervals (such as Hourly) with large date ranges (such as Last Month) result in more data than can be displayed. Therefore, such selections aren't allowed.

To edit a module label, select the label text and type a new label.click the Edit ( ) icon and on the Edit Module dialog, type a new label.

You can filter the date range by selecting an option from the Including drop-down list. The possible values are Days of a Week , Days of the Month , Weeks of the Month , or Months of the Year . Select the weekdays, days of the month, weeks, or months that you want the visualization to include.

For custom reports using relative time ranges like This Week or Last Week , you can define the day that you want to consider as the start of the week.

Select the desired start day from the Start Day of the Week drop-down list (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). The default selection is Monday.

If you select a compute interval of Weekly and specify a custom start day, the weekly interval begins on the selected start day of the week.

Start Day of the Week option doesn’t apply if you use the custom option in the Start Time drop-down menu.

If you're creating a time-based visualization, select a time interval from the Interval drop-down list in the Compute panel. The possible values are: None , 15 Minutes , 30 Minutes , Hourly , Daily , Weekly , or Monthly .

The available options vary depending on the length of the date range. Small compute intervals (such as 15 Minutes, 30 Minutes, or Hourly) aren't available if the specified date range is lengthy (such as Last Month).

After selecting an interval in the Compute panel, the Enable Split Interval option becomes active. This enables users to split data by selecting a precise interval instead of mapping the time to the interval in which the interaction ends.

You can view detailed agent activity, agent states, and agent durations across different time intervals, which can help optimize agent staffing, allocate workforce efficiently, and ensure high customer satisfaction.

Here are the key points regarding this functionality:

- The Enable Split Interval check box is available for creating new custom reports, editing existing reports and copy of stock reports.

- If the Enable Split Interval check box is not displayed, contact Cisco Support as the corresponding feature flag may have to be enabled.

- For new reports, the Enable Split Interval check box is enabled by default.

- This Split Interval option is available for storage record types of ASR only.

- You can toggle the checkbox in report design mode and run it again to apply/remove split interval for durations.

- While viewing a report with split interval enabled, a notification toaster informs you about split interval enabled for the report. The toaster redirects you to the Analyzer User Guide when you click learn more .

- For an agent, the Split Interval for a telephony channel is tied to a single channel ID during a specific time interval, and the total idle duration will always be less than the selected interval. For example, in a 15-minute time interval, the idle duration will always be under 15 minutes. On the other hand, for non-telephony channels like email, chat, or social media, there can be multiple channel IDs within the selected interval, and the idle duration can exceed the chosen interval. For example, in a 15-minute interval, the idle duration may be greater than 15 minutes since the aggregated idle time spans multiple channel IDs. In such scenarios, you can drill down into the idle duration to view details about the different channel IDs the agent was working with during the selected interval.

If you’re creating a sample-based visualization, select First or Last from the Records drop-down list in the Compute panel, and in the text box, enter the total number of records to be considered in the visualization.

You can also define the following:

Frequency : The number of records to be considered per interval.

Band : The number of records to be considered per calculation.

Cumulative : To calculate the number of records.

If you selected Realtime as the visualization time period, select values from the drop-down lists that become available in the Compute panel.

Parameter

Description

Duration

Select None for a snapshot of the current contact center activity.

- OR -

Select a specific time interval (of 5, 10, 15, or 30 minutes) for a view that looks back from the current moment to the most recent 5, 10, 15, or 30 minutes.

- OR -

Select Start of Day for a view of all activities that occurred since midnight.

- OR -

Select Custom for a view that looks back from the current moment to up to 14 days in the past.

Refresh Rate

Select a value to specify how often the data in the visualization will be refreshed. If you have specified the duration as Start of Day or Custom, select Minutes; otherwise, select Seconds.

Interval

If you have specified the duration as Start of Day or Custom, the Interval drop-down list appears, enabling you to select a time interval (None, 15 Minutes, 30 Minutes, or Hourly).

Look Back (D-H-M)

If you have specified the duration as Custom, the Look Back settings appear. Enter the number of days, hours, and minutes from the current moment you want the visualization to look back to. You can specify up to 14 days.

To specify either Row Segments or Column Segments, click the Add Row Segments or Column Segments icon. Drag and drop a field or an enhanced field listed in the canvas area. Repeat this step for each segment that you want to add.

Fields can be added as either Row Segments or Column Segments . For charts, only the first segment is used.

High cardinality fields such as Contact Session ID and Agent Session ID contain a large set of unique values. When you select these fields as row or column segments while creating a new report or modifying an existing report, a large amount of data is fetched. To avoid this, a pop-up prompts you to add specific filters to decrease the amount of data fetched. You can also ignore the message and continue to save the visualization.

The prompt appears when you select the high cardinality fields as a row or column segment. You can resolve it by adding more filters to decrease the amount of data.

To combine multiple values of the segmentation variable into one group, you can create an enhanced field:

Right-click a value and select Create Enhanced Field .

Specify the settings for one or more groups in the dialog box that
              appears. For example, you could create three groups of entry points where each group
              represents a different product line or a different business unit.

To create a profile variable:

Click the Add Profile Variable icon. Drag and drop a field, measure, or formula listed in the New Profile Variable dialog box and do one of the following:

Type a name for the profile variable in the Name text box or leave the default text. This name will be displayed in the column header and axis labels.

If you used a field to create the profile variable, you can specify the records that you want to include in the count by dragging an item from the Fields list to the Filters area of the New Profile Variable dialog box and selecting the records to be included. For more information, see Filter Using a Field . If you used a measure to create the profile variable, select the computation that you want to perform from the Formula drop-down list. For more information, see Select a Formula for a Measure . You can specify a condition for including records by dragging an item from the Fields or Measures lists to the Filters area of the dialog box. For more information, see Filter Using a Measure .

You can also create a new formula based on a profile variable that exists in the visualization.

- You can also create a new formula based on a profile variable that exists in the
                visualization.

- If you selected a Global Variable as the profile variable, only the selected
                Global Variable from the Fields or Measures lists can be used as a filter of the profile
                variable. For more information about Global Variables (previously known as
                Call-Associated Data variables), see the Contact Routing chapter in the Cisco Webex Contact Center Setup and
                    Administration Guide .

To specify the format for the profile variable, click on the right-click the profile variable and select the Number Format option from the context menu. For more information, see Format a Profile Variable . For example, if you created a Conversion Rate profile variable, you could select Percentage as the format.

Continue creating as many profile variables as you want. In the following example, three profile variables have been created and the data is segmented under Queue ID and Agent Name header rows.

If you’re creating a motion chart, you must include at least three profile variables.

To change the order of a profile variable or segment, drag its label to a different position.

To pivot across column and row segments, drag a segment label from the Column Segments box to the Row or Series Segments box, or the opposite way.

To remove a profile variable, click on the Edit icon or right-click the profile variable and select Delete .

You can’t remove a profile variable used in another profile variable.

To show or hide the summary of column values at the table level and the top-level row segment, select the values from the Show Summary drop-down list.

To define the summary of column values at the table level and the top-level row segment, click Customize . For more information on Customize Report Summary , see Customize Report Summary .

To find out approximately how large the visualization is when it’s run, save the visualization and click More and select the Info button.

You can create a filter to limit the number of records that the visualization considers by default. To create a filter:

Click Add Filter in the Modules tab. Select a field or measure from the displayed lists and click Save .

- OR -

Right-click a segment in the visualization and select Create Filter .

When the new filter appears in the Modules tab, specify which values to include or exclude or, in the case of a measure, set a condition that the data must satisfy.

You can’t select more than 1000 values inside a field for a filter. If you've selected more than 1000 values, an error message appears. To remove a value, use the X button.

Specify a visualization output format. For more information, see Change the Visualization Output Format

You can now choose a KPI Card as one of the output type. Only the first profile
              variable is used when rendering a KPI Card. To refer the possible output format types,
              see Change the Visualization Output Format .

Navigate to Formatting Tab and click on Set Color Conditions to apply the
          color conditions in the pop up.

You can apply conditional formatting to a table or KPI cards to change the value
              color based on performance. When using this feature for a KPI card, the color rule
              applies to the aggregated result of the first profile variable only. For more
              information refer Format a Table .

If you’re creating a compound visualization, add at least one additional module before you save the visualization.

To save the visualization, click the Save button, and in the dialog box that appears:

Select the folder.

To create a new folder, click New Folder , and enter a name for the folder.

Enter a name for the visualization and click OK .

Click Preview to view the visualization.

If you're creating visualization of the Customer Session
                Record type, where Interval is used as Row Segment and Contact Start
                Timestamp and Contact End Timestamp are used as Profile Variables from the Measures drop-down list, select Minimum Contact Start Timestamp for Contact Start Timestamp and Maximum Contact End
                Timestamp in the Formula drop-down list.

### Create a Compound Visualization

A compound visualization includes two or more modules that are displayed alongside. All modules within a visualization must have identical rows or series segments, column segments, and profile variables, but can have different date ranges, intervals, and filters.

You can create a compound visualization as follows:

While creating a new visualization, by adding at least one additional module (Historical or Realtime module) before you save the visualization.

Edit an existing visualization which has only one module by adding new modules (Historical modules only).

However, if you save a visualization with more than one module, you can later delete all but one module, save the visualization and add more modules (Historical modules only).

Realtime modules can be added to a compound visualization only while creating it and before saving the visualization. You cannot edit an existing visualization to add a Realtime module.

Compound visualizations cannot be scheduled or exported and do not have pivoting capability in execution mode.

To add a module during visualization creation, click Add at the top of the Modules tab. In the dialog box that appears, enter a name for the module and click OK .

Click Add again for each additional module you
            want to add.

After adding a module, the visualization creation page displays the constituent visualizations side by side. You can select different date ranges, intervals, and filters for each module.

Choose an interval value other than None . If None is chosen, the interval values are displayed as belonging to the year 1970.

To display the settings that can be customized for each module, select a module from the drop-down list at the top of the Modules tab.

To edit a module label, select the label text and type a new label.click the Edit ( ) icon and on the Edit Module dialog, type a new label.

The drop-down list in the Modules tab reflects the label changes.

### Create a Visualization Displaying Actual Values

To display the actual values in the database without aggregation, the visualization cannot include a time interval or segmentation, and all profile variables must be configured with Value of as the formula.

The Value of option is not available in a visualization that already includes a time interval or segmentation.

To create a visualization displaying actual database values without aggregation:

Click Visualization > Create New > Visualization .

Select a Type . The possible values are Customer Session Record , Customer Activity Record , Agent Activity Record , or Agent Session Record .

Specify the visualization time period.

To add a profile variable:

Click the Add Profile Variables , and drag and drop a field or measure in the New Profile Variable dialog box.

In the Formula drop-down list, select the Value . Repeat for each additional profile variable you want to add.

Click Save to save the visualization. Then you can click Preview .

### Create an Enhanced Field

Right-click a segment in the visualization and select Create Enhanced Field .

Specify the settings for the group as described in the following table:

Setting

Description

Default Group

Enter a name (for example, Other Entry Points) for the group that includes all the variables not included in the defined groups.

Groups

To define a group, enter a name in the Group Name :

Select values from the drop-down list.

Type a value and then press Enter .

Click Save .

### Create an Enhanced Field for skill-related fields

Extend the Enhanced Fields option to include skill-based fields, offering improved classification capabilities. This allows you to group skills according to your specific requirements, helping you organize them more effectively.

You can create enhanced fields for the following skill-based fields:

- Required Skills (CSR)

- Matched Skills (CSR)

- Agent Skills (ASR)

Due to current data limitations, while running a report, you won’t be able to filter default groups using fly filters. As an alternative, you can use ‘ag-grid’ filters within the report to filter the same data for skill-based enhanced field cases.

Currently, grouping includes only the skill values that have been actively used in the past 3 months. This limitation applies only during the group creation process. When running the report, however, all data will be displayed based on the duration selected in the fly filters.

Currently, grouping enum-type skills are not working correctly due to a data issue. This will be resolved as part of an upcoming feature update.

Select one of the skill-based metrics and add it to the report.

Right-click a segment in the visualization and select Create Enhanced Field .

Specify the settings for the group as described in the following table:

Setting

Description

Default Group

Enter a name (for example, Other Entry Points) for the group that includes all the variables not included in the defined groups.

Groups

To define a group:

- Enter a name in the Group Name field.

To select a skill:

- Select a skill from the Select Skill drop-down list.

- Select an operator from the Select Operator drop-down list.

- Select an existing value or create a new value by typing it in the Select Values box and then press Enter .

- Between skills, ‘AND’ operator is applicable.

- You can add up to 1000 skills.

To add more groups:

Click on the + icon to add another group.

- Across the groups, ‘OR’ operator is applicable.

- You can create up to 100 groups.

- Click the Add Skill button to add multiple skills to the group.

Click Save .

### Delete a Shared Enhanced Field

To delete a shared enhanced field:

Click the Add button to add the Column Segments or Row or Series Segments box to display the New Segment dialog box.

If the enhanced field is not currently in use, it is deleted.

### Share an Enhanced Field

To make an enhanced field available for future use:

Click the enhanced field segment that has been added to the visualization and select Save from the context menu.

Enter a name for the enhanced field and click OK .

The saved enhanced field will now be listed in the New Segment dialog box for selection when you and other visualization designers create or edit a visualization.

### Select a Formula for a Measure

The following table describes the formulas available when you use a measure to create a profile variable.

Calculates

Average

The average value.

The total value.

Count

When you select this formula, the dialog box displays settings for specifying a condition for including records in the count. For more information, see Filter Using a Measure .

Minimum

The largest value.

The actual value in the database without aggregation.

Geometric Mean of

Population Variance of

Variance of

The average of the squared differences between each value and the mean value.

### Define Filters

#### Filter using Profile Variables

When you create a visualization, the settings panel displays controls for
        specifying which records to include or exclude from the visualization.

These controls are displayed while creating or editing a visualization,
        when you do the following tasks:

Drag a field into the Filters area of the
            dialog box that appears when you create or edit a profile variable.

Click Add Filter and select a listed field in
            the dialog box that appears.

Right-click a segment in the visualization and select Create Filter .

#### Filter using Data Filter

You can create advanced filtering conditions with Data Filters when you build or modify
      reports. Use both AND and OR logical operators, and nest conditions as needed based on your
      requirements. These Data filters ensure the conditions are set at the data level. When you
      generate the report, you see results that reflect the exact level of detail you defined.

- If you haven't added any data filters yet, click Add Data Filter in the left panel to open the Report Filters dialog box, where you can set the desired data filtering conditions. You can also add
              nested filters as needed.

- If you already have data filters applied, an Add/Modify Data
                Filter button will appear. Clicking this button will open the Report Filters dialog box, displaying your existing filters
              for further modification. You can also add nested filtering conditions as needed.

- Select the field or measure you want to include in the filter in the box next to the Where field.

- Boolean Data Type : Equals, Not Equals

- Numerical Data Type : Greater Than, Greater Than or Equals, Less Than,
                  Less Than or Equals, Between, Equal, Not Equal.

- String Data Type : Contains, Does Not Contain, Regular Expressions.

If you select a metric which is of Measure type, you will have to provide the
                  value, and it will not be populated in the value box.

You will be guided in the Analyzer for Skills metrics and between conditions as they have a few additional boxes to be selected.

The following examples illustrate how to use regular expressions:

- agent.* includes all field values starting with the phrase agent.

- agent.*h includes all field values starting with the phrase agent and ending
                    with the letter h.

If you want to exclude all records that are marked as "N/A" ,
                          then you may use the Filter out N/A scenario.

Currently, there is no RegEx-based method available to filter exclusively
                          for 'N/A' values.

If you want to filter for one or more specific values exactly ,
                          then you may use the Exact match approach.

For example, contains <Agent Name> Note: It is recommended to use
                          the 'contains' function instead of regex for better performance.

If you want to find records that contain a specific word or
                            phrase anywhere within the text , then you may use the Partial
                            match scenario.

If you want to find matches regardless of whether the text is
                            uppercase or lowercase , then you may use the Case insensitive
                            match scenario.

If you want to find all items that begin with a specific
                            prefix , then you may use the Prefix match scenario.

If you want to find all records that end with a specific
                            identifier , then you may use the Suffix match scenario.

For more information about standard regular expressions, see https://www.elastic.co/guide/en/elasticsearch/reference/current/regexp-syntax.html .

- To add additional conditions to the same selected metric, click the Add
            Playlist button located on the right side of the row. A new row with a Subdirectory Arrow Right icon will appear. You can then select a
          logical operator (AND or OR) and continue adding more conditions for the same metric.

- Type one or more characters in the text box to filter the list of available values.
              Matching values will appear as you type. Select your desired values from the drop-down
              list.

- To specify an empty (blank) value you can select the blank option.

- To change the specified value, select it and press the backspace key on your
              keyboard.

- To add more conditions with a different metric, Click Add Filter at the left to add another filter.

- You can select either the And or Or option from the drop-down menu. This
          option is only available for the first condition within the group. The steps outlined in
          step 3 will remain applicable for the new set of metrics.

- You can remove a row condition by clicking the delete icon. If you click the delete icon
          on the first filter within a nested group, the entire nested filter group will be
          deleted.

- Click Save to save the data filter and continue the report
          creation or modification process.

#### Filters in the Run Mode

The Analyzer UI offers filtering capabilities while executing a report in the run mode.

You can choose filters while creating or editing a visualization, and also while creating
            a copy of the visualization.

When you run a visualization, the filters appear at the top-right corner of the
            visualization page. You can filter the visualization by selecting the appropriate
            filters without editing the report.

You configure the Start Day of the Week setting for custom reports during report creation or editing, and it is not available as a filter in run mode.

To add a filter to a report that shows up in run mode while creating a visualization:

Go to the Analyzer home page. Click the Visualization icon
                    in the navigation bar.

To create a new visualization, choose Create new > Visualization .

In the create visualization page, select and drag the required fields to the Row Segments pane. The added fields are displayed as filters in the Run Mode Filters check box list, along with the default filters.

Row and column segments can be added only to segmented reports, not to value-based reports.

Duration and Interval field
                            for a Historical Report. The Interval field
                            appears as a filter only if it is selected as a Row
                                Segment .

Duration field for a Real-time Report.

Select the required filter in the Run Mode Filters check box list by selecting the corresponding check box.

Filters marked as 'N/A' are not supported.

By default, all filters in the Run Mode Filters check box list are unchecked.

Select the required Profile Variables and Column fields, and save the new visualization in the
                    appropriate folder.

The filters are displayed at the top-right corner of the visualization. You can
                    now filter the visualization by selecting the appropriate filters, without
                    editing the report.

For more information on creating a visualization, see the section Create a Visualization .

The maximum filter selection for a given field can't exceed 1,000, except when 'All' is applied.

If you see an error message such as 'Filter selection limit exceeded. Please unselect few', update the selection to remove a few values from the filter.

To add a filter in run mode while creating a copy of the visualization:

Navigate to Home > Visualization > Stock Reports . Select the appropriate Stock Report and click the ellipsis
                    button to display the report options. Choose Create a
                        Copy option.

Select the appropriate filter from the Run Mode Filters check box list that appears on the left pane of the visualization page.

By default, all filters in the Show filter on Run Mode check box list are checked.

Save the new report in an appropriate folder.

When you run the visualization, the filters are displayed at the top-right corner
                    of the visualization.

For more information on creating a copy of the visualization, see the section Tasks to Perform on Visualization and Dashboard Pages .

To add a filter in run mode while editing the visualization:

Go to the visualization page. Click the ellipsis button and then select the Edit option to edit the visualization.

Select the required filter in the Run Mode Filters check box list that appears on the left pane of the visualization page.

By default, all filters in the Run Mode Filters check box list are selected.

Save the new report in an appropriate folder.

When you run the visualization, the filters are displayed at the top-right corner
                    of the visualization.

For more information on editing a visualization, see the section Tasks to Perform on Visualization and Dashboard Pages .

A maximum of five filters can be added to be displayed in a report in the run
                mode.

Filters at the top-right corner of the visualization page are not supported for compound visualizations (which has two or more modules). If you edit an existing report with one module to add another module, the Run Mode Filters check box list grays out.

### Create a Text-based Formula

You can create a new formula by selecting the fields, or existing profile variables and you can apply mathematical operation on top of it.

Build your custom formula by adding fields and measures from the list of available options. Once saved, the formula is available for use in your reports. You also have the option to set the formula as a shared formula, making it accessible across all reports within your organization.

Additionally, you can apply filters directly within a custom formula on each data field operand, and you can add multiple filters by joining them with the 'AND' operator.

When creating a custom formula in a segmented report using the custom formula editor, ensure that any local profile variable you reference doesn't have the same name as any field, measure, or shared formula.

Here's how the logic works:

- If the text in your custom formula matches a field or measure name, it will refer to that field or measure.

- If it doesn't match a field or measure name, it will then check for a shared formula with the same name.

- If there is no shared formula by that name, it will check for a report column name.

- If it finds no match in any of these, you will receive an error indicating that the item does not exist.

To avoid errors, always use unique names for your local profile variables that do not conflict with existing field names, measure names, shared formulas, or report column names.

To create a new formula:

- Click the profile variable in the visualization and click Add Formula .

- In the New Formula dialog box that appears, enter a name for the formula and enter the description for it.

- Select the data field by using the search option and then select the aggregation type from the drop-down list. Then, click Insert to add the formula to the box.

- Select the name of an existing profile variable from the drop-down list.

- Type a numeric value.

- Type standard functions such as CURRENT_TIMESTAMP() and REPORT_DAYS().

- Select a mathematical operation: +, –, ×, ÷, or ^.

- To filter based on fields, you can use operators such as ‘IN’, ‘NOT IN’, and 'MATCHING' (regular expressions) to create filters within your formula.

- To filter based on measures, you can use standard numbers, durations in milliseconds, and timestamps in the mm/dd/yyyy format to create filters within your formula.

- To filter based on global variable fields, you can use the operators based on the global variable type.

- To filter based on skill-related fields, you can use the format "FieldName.SkillName". You can use the operators based on the skill type.

Here are some examples that demonstrate how to use filters within a formula:

```
<COUNT> "Feedback Survey OptIn" 
WHERE "Feedback Type" IN ["inline"] 
AND "Feedback Survey OptIn" IN ["true", "false", "undefined"]
```

```
<COUNT> "Activity State" 
WHERE "Activity State" IN ["connect"] 
AND "Next State" IN ["con-to-agent-error"] 
AND "Activity Duration" >= 1000 
AND "Activity Duration" <= 17999
```

```
<COUNT> "Agent Name" 
WHERE "Agent Skills.SoftSkillTrained" = "TRUE" 
AND "Agent Skills.LanguageProficiency" = 4 
AND "Agent Skills.Platform" IN ["windows", "linux", "mac"]
```

You can't add Text-based fields to the formula in the value-based reports since it is not a valid operation for report generation.

- You can click on the Formula guidelines option to view detailed information and examples.

- Click Validate to ensure that the formula is valid.

You can select the Save formula for access across Customer Session Record checkbox to share the custom formula as a shared formula accessible to all reports within your organization. The checkbox will change depending on the record type that you are using. However, you can’t use the formula with other record or profile types.

### Creating and Using Shared Formulas

After you create a profile variable, you can make the formula available in the Formulas panel for all users in your organization.

#### Create a Shared Formula

To create a shared formula from a profile variable:

Create a Profile Variable . For more information, see Create a Visualization .

Right-click the profile variable and select Save .

Enter a name for the formula and click OK .

The formula is saved in the Formulas panel.

To create a shared formula from a text-based formula builder:

- Follow the steps provided in Create a Text-based Formula .

The checkbox will change depending on the record type that you are using. However, you can’t use the formula with other record or profile types.

#### Utilize a Shared Formula

To use a shared formula in your report:

- Identify the Shared Formula to be utilized from the Formulas Section in the left pane.

- Drag it from the left pane and drop it into the Profile Variables Section of the report.

- The shared formula will be highlighted in blue. You can't edit the shared formula from the Profile Variable section. But you can view the content by double-clicking it.

Shared formulas in the Formulas tab can be edited by any user in the organization.

#### Edit a Shared Formula

To edit a shared formula:

Click Add Profile Variables and then double-click the name of a formula listed in the Formulas panel.

You can use the Review Reports using current formula to view a list of reports in which the formula is currently used.

You will see the following message: A formula with this name already exists and may currently be used in multiple reports. You may choose to replace the existing formula-this will update all the associated reports if exists-or save this as a new formula with a different name

You can edit the existing formula or add additional Fields and Measures .

- Click Validate to ensure that the formula is valid.

Click Save .

#### Delete a Shared Formula

To delete a shared formula:

Click the Add button in the Profile Variables box.

Locate the formula that you want to delete.

Click on the Delete icon.

If the formula is not currently in use, it is deleted.

### Create and Format a Visualization Title

To create and format a visualization title while creating or editing a visualization:

Click the text Click to add title in the visualization canvas and enter a new title.

To edit the title, select it and enter a new title.

In Formatting , select Title from drop-down and enter the title text.

To customize the format of the title, select Title from the drop-down list in the Formatting tab to display the
          formatting options that you can customize, such as border size, style, and color; text
          alignment and color; margins; padding; and font size, family, style and weight.

KPI cards inherit a default title from the selected aggregation type/profile
              variable.

### Format a Table

To customize the format of a table:

Select Formatting , and then select Table from the drop-down list.

Change any of the following options to customize the table format:

Option

Description

Back Color

Select the background color from the color selector or enter the HTML (hexadecimal) code for a color.

Border Size

Enter a value in pixels to change the border width.

Border Style

Select a value from the drop-down list to specify the style of the border around the table or select None if you do not want a border around the table.

Border Color

Select the border color from the color selector or enter the HTML code for a color.

You can improve the readability and usability of large tabular reports in Analyzer, by using conditional formatting and color coding of data values. This feature helps you quickly understand and respond to important data by visually highlighting key metrics based on your rules.

You can define these rules using logical operators (for example, Greater Than, Less Than, Between, etc.) to filter which data you would like to highlight.

To set the color conditions, Click Set Color Conditions .

You can assign visual indicators (Red, Orange, Yellow, Green, Blue, with corresponding tags) for each threshold condition.

You must enter a number for thresholds; the system doesn't support text values.

- Click Add condition to add a new condition.

- Click Save . The configured color code will be visible when you view the report. You have the option to remove the color code by using the Conditional Formatting toggle button in the Settings tab at the top left of the report.

You will see the rules applied in the preview window.

- You can define and set up to 10 threshold levels on a single data metric, allowing for granular control over how data is visually represented.

- Thresholds and their associated conditions are set at the user level, based on individual preferences. User-defined thresholds operate independently and don’t interfere with default settings.

- When a report is copied, its threshold criteria can be inherited.

### Format a Profile Variable

To change the text alignment, number format, or caption of a profile variable:

Do one of the following:

Right-click a profile variable to display the context menu.

Select a profile variable from the drop-down list in Formatting to display the number format and caption options in the tab.

Change any of the options described in the following table:

Option

Description

Caption

To change the caption, click the caption text that's displayed in the Formatting tab to select it, and enter
                                the required caption.

This setting is available only in the Formatting tab.

Right-click to specify whether you want the data to
                                be formatted as Integer, Number, Currency, Percentage, Date Time, or
                                Duration, and within that category, specify how you want the data to
                                be displayed.

Number Format

For example, when you select Percentage, you can
                                select one of the following format options:

##.##% (12.34%)

##% (12%)

When you select Duration, you can select one of the following format options:

- MM:SS (04:35)

- M:SS (4:35)

- HH:SS:SS (04:35:15)

- H:MM:SS (4:35:15)

- HH:MM (04:35)

- MM:SS.sss (04:35.200)

- HH:MM:SS.sss (04:35:15.200)

Text Align

To change the alignment of the column text, select a
                                value from the drop-down list: Left, Center, or Right.

This setting is available only from the context
                                menu.

### Change Date Format of the Interval Field

You can edit the default date format (mm/dd/yyyy) of the Interval field while creating or editing a visualization.

Right click the Interval field to display the Select Date Format context menu.

Select the required date format from the following list:

mm/dd/yyyy

mm/dd/yy

m/d/y

dd/mm/yy

d/m/y

yyyy/mm/dd

yyyy-mm-dd

Click Save .

If you export a report in the .csv format and open it in Microsoft Excel, the date is displayed according to the date format that is set in Microsoft Excel. To display the dates in the exact date format that you applied for the Interval field in the visualization, open the exported CSV report in a text editor.

### Format a Chart

To customize the format of a chart:

Choose Formatting > Chart .

Change any of the following options to customize the chart format:

Option

Description

Back Color

Select the background color from the color selector or enter the HTML code for a color.

Border Size

Enter a value in pixels to change the width of the border around the chart.

Border Style

Choose a value from the drop-down list to specify the style of the border around the chart or select None if you do not want a border.

Border Color

Select the border color from the color selector or enter the HTML code for a color.

Gradient Fill

To add a shade pattern to the lines, areas, or bars in a line, area, or bar chart, select the direction of the color gradient from the drop-down list.

Stacking

To display data values stacked on top of each other in a line, area, or bar chart, select Normal to stack by the data values or Percent to stack by percentages.

Axis Labels

Select a value from the drop-down list to specify whether to show or hide axis labels.

Invert Axes

Select either True or False from the drop-down list to specify whether or not to invert the axes.

Data Labels

Select a value from the drop-down list to specify whether to show or hide the data labels.

Data Labels Rotation

Select a value from the drop-down list to specify the data label rotation angle: None, 45°, 90°, or -90°.

### Edit the Visualization Name

To edit the visualization name, do one of the following:

Click Visualization > > Edit from the context menu.

Click Edit Visualization Name and in the Formatting tab, select Visualization from the drop-down list to edit fields.

### Customize Report Summary

You can customize a report summary at both the table level and top-level row segment group when creating or editing a visualization. The Customize option is available for visualizations that have only profile variables set as column segments. For more information about row and column segments, see Create a Visualization .

You can define following summary formulas for each of the columns in a report in the Customize Report Summary dialog box.

Formula

Calculation

NONE

No formulas are defined for the column summary.

If you select NONE for all the columns in a visualization, you cannot see the table level or group level summary.

AVG

The average of the values in the column.

COUNT

The count of records in the column with values other than null.

MIN

The smallest value in the column.

MAX

The largest value in the column.

SUM

The sum total of all the values in the column.

You can also select the predefined formula to calculate only the table level
                  summary for the column that has a formula field.

AVG is disabled for division-based custom formula fields in Customize Report
                  Summary

- You can view the customized report summary on the Analyzer UI and exported
                    reports in the MS Excel format. The customized report summary is not shown on
                    Exported reports in the CSV format.

- You can see the defined formula for a column summary by hovering the mouse over
                    the Summary cells of the column on the Analyzer UI.

- You can see the defined formula for a column summary in the Summary cells of the column on the exported MS Excel
                    reports. Summary cells contain the <Summary Value>(<Summary
                    formula>) text format.

- You can customize only the table level summary for the value-based reports. If a
                    column in a value-based report has the String type field, you can define the
                    summary formula for the column as NONE or COUNT. If the column has Integer
                    (Measures) type field, you can define formulas as shown in the table.

#### Table Level Summary

This is the footer summary of the report. You can show the summary by selecting the Table level checkbox in the Show Summary drop-down list. By default, this checkbox is selected when you create a new visualization.

For the segmented reports, when you select the Table level checkbox but do not define the summary formulas, by default the aggregation type of a column field is set as the summary formula for that column except for the following scenarios:

If a column has the formula field, by default the table level summary formula for the column is defined as CUSTOM.

If a column has the duration field, by default the table level summary formula for the column is defined as NONE.

If a column has a field of the COUNT aggregation type, by default the table level summary formula for the column is defined as SUM, which is the sum of all individual counts.

For the value based reports, when you select the Table level checkbox but do not define the summary formulas, by default the table level summary formula is set as NONE.

#### Group Level Summary

This is the column summary that is defined at the top-level row segment group. The group level summary option is available for visualizations that have minimum two row segments.You can show the group level summary by selecting the checkbox that shows the name of the top-level row segment in the Show Summary drop-down list. By default, this checkbox is cleared when you create a new visualization.

When you select the group level summary checkbox but do not define the summary formulas, by default the group level summary formula is defined as NONE for all columns.

Group level summary is not applicable for the value based reports.

#### Report Summary in Agent Details Reports

You can see the table level and group level summary in the Agent Details reports. Both table and group level summary formulas are defined based on the column aggregation type except for the following scenarios:

If a column has the formula field, by default the table level summary formula for the column is defined as CUSTOM and the group level summary formula is defined as NONE.

If a column has the duration field, by default the table level summary and group level summary formulas for the column are defined as NONE.

If a column has a field of the COUNT aggregation type, by default the table level summary and group level summary formulas for the column are defined as SUM, which is the sum of all individual counts.

### Export Report Templates

You can export report templates as a single file or as folders containing multiple files. The file or folders are exported from the Analyzer to your computer. Exporting report templates helps in reusability across multiple tenants.

Export a File

To export a template file from the Analyzer server:

The exported template includes the custom Start Day of the Week setting that you configured for the report during the report creation journey.

On the Home page, click the Visualization icon.

Select the template file that you want to export.

Click the ellipsis button.

Select Export Template from the drop-down list. If the file is exported successfully, the following message is displayed:

The report template was succesfully exported and placed in the Downloads folder .

You cannot export a report that has a long duration and less interval. Reset the Duration and Interval fields as required for real-time and historical reports to proceed further. For more information, see Create a Visualization .

The file is saved in the .JSON format.

Click Close .

Export a Folder

To export a folder from the Analyzer server:

On the Home page, click the Visualization icon.

Select the folder that you want to export.

Click the ellipsis button.

Click Export Templates from the drop-down list.

- You can export up to 25 templates at a time.

- When you export a folder, subfolders are not exported. You must export
                            the subfolders separately.

- If filters are applied to the report templates, the associated values
                            and variables are removed during export. However, filter names are
                            retained.

Click Export . If the file is exported successfully, the following message is displayed:

All the report templates in the folder are saved successfully and placed in the Downloads folder as a .zip file.

### Import Report Templates

You can import report templates as a single file or as a folder containing multiple files. The file or folder can be imported from your computer to Analyzer. The import feature is available only to administrators who log in to the Analyzer UI.

The template versions are deployment-specific. You can import Webex Contact Center 1.0 report templates to Webex Contact Center 1.0 only. Similarly, Webex Contact Center report templates can be imported to Webex Contact Center only.

When you import a single template file, a corresponding visualization is created based on the template.

To avoid naming conflicts, timestamps are added when a report with the same name exists in the target folder.

Import a File

To import a template file to Analyzer:

The  imported template includes the custom Start Day of the Week setting that you configured for the report during the report creation journey.

On the Home page, click the Visualization icon.

Click Import .

Click Browse to select the file (.CSV format) to be imported.

Click Import . If the file was imported successfully, the following message is displayed:

The file was imported successfully .

Click Close .

Import a Folder

To import a template folder to Analyzer:

On the Home page, click the Visualization icon.

Click Import .

Click Browse to select the folder (.zip format) to be imported.

The total number of templates in the .zip file cannot exceed 25.

Click Import . If the folder was imported successfully, the following message is displayed:

The folder was imported successfully.

Click Close .

### Schedule reports during migration

With this feature, you can efficiently migrate from Webex Contact Center 1.0 to 2.0 without disrupting report scheduling. This feature ensures operational and business continuity for reporting during migration, providing access to reports for both older and newer versions. Throughout the migration process, the following scheduled jobs will remain unaffected:

- Schedules created in 1.0 will continue to run from the 1.0 application

- Schedules created in 2.0 will seamlessly run from the 2.0 application

| 1 | Click the Visualization icon on the navigation bar. |
|---|---|
| 2 | To find a report, you may use either the Search function or the (tree) icon. When you click on the tree icon, all files in that folder are displayed. Search displays all the matching reports from the subfolders as well. When you click on a folder or a report, the exact location of the folder or the report is displayed on the breadcrumb. |
| 3 | On the report, click the (ellipsis) button and select the Run option or double-click to run. By default, you can view a set of stock reports. To edit a report, you can create a copy of the report by clicking Save As to save it in your folder. For more information, see Stock Reports . You cannot run a report that has a long duration and less interval. Reset the Duration and Interval fields as required for real-time and historical reports to proceed further. For more information, see Create a Visualization . If the copied report has more than 1000 filter values, an error message appears when you run the report. If you see an error message such as This view shows records to accommodate a max of 1000 filter values. Please edit the report to select predefined values , edit the report to remove a few values from the filter. The report accommodates only 1000 values. |
| 4 | After the visualization is rendered, click the (navigation) icon to see the data summary of the visualization. You can see the last refreshed time of the visualization data in the Data Summary tab. If you’re running a visualization with multiple modules (compound visualization), the Data Summary tab displays a drop-down list of all the modules in the visualization so that you can display the details of each individual module. |
| 5 | Click the Details tab to display the following settings and panels. Click a panel title to expand or collapse the panel. If you are running a compound visualization, the details are displayed separately, depending on which module is selected in the drop-down list at the top of the tab. Start Time : Indicates the start time of  a historical visualization, or Realtime in the case of a real-time visualization. Compute : Specifies Duration and Refresh Rate of a real-time visualization. Possible values for Duration: None: Provides a view of the current activity. 5, 15, or 30 minutes: Provides a view of all activities that occurred from up to 30 minutes ago to the current moment. Start of Day: Provides a view of all activities that occurred since midnight. Compute specifies the compute interval and the number of records to be considered in a time-based historical visualization. Compute specifies the frequency, band, and whether the calculations are cumulative for a sample-based visualization. For more information, see Create a Visualization . If filters are applied to any field, an extra panel is displayed for each field so that you can see the values that have been filtered in or out of the visualization. |
| 6 | Click Settings to display the segments and variables associated with the visualization. You can also change the Output Type . You can now choose KPI Card as one of the output type. Only the first
                            profile variable is used when rendering a KPI Card. If multiple metrics
                            are present, the system uses only the first visible profile variable as
                            the metric.To refer the possible output format types, see Change the Visualization Output Format . |
| 7 | If the visualization is in a chart format: The underlying table used to construct the chart is displayed beneath the chart. Click the Hide Table link to hide the table, and the Show Table link to display it. Rest your pointer over a bar, line, slice, area, or bubble in the chart to display information about the segment that the item represents. |
| 8 | If the visualization is historical, you can click the Export button on the title bar to export the visualization as a Microsoft Excel or CSV file. Real-time and compound visualizations cannot be exported. You cannot export a visualization Historical Report if it has more than 2000 columns. |

| Duration | Intervals Supported |
|---|---|
| Today | 15 minutes, 30 minutes, Hourly and Daily |
| Yesterday |
| This Week | 30 minutes, Hourly and Daily |
| Last Week |
| Last 7 days |
| This Month | Daily, Weekly |
| Last Month |
| This Year | Daily, Weekly, and Monthly |
| Custom | The duration categories and their supported intervals based on the date difference are as follows: If the date difference is less than or equal to 1 day, the Duration is categorized as Today , with supported intervals of 15 minutes, 30 minutes, Hourly, and Daily. If the date difference is less than or equal to 7 days, the Duration is categorized as This Week , with supported intervals of 30 minutes, Hourly, and Daily. If the date difference is less than or equal to 31 days, the Duration is categorized as This Month , with supported intervals of Daily and Weekly. For any date difference greater than 31 days, the Duration is categorized as This Year , with supported intervals of Daily, Weekly, and Monthly. |

| Parameter | Description | Formula |
|---|---|---|
| Site | Name of the site. |  |
| Month | Shows month and year of the report. |  |
| Date | Shows date, month, and year of the report. |  |
| Unique Agents Logged In | Shows the number of agents who were logged in. Only one login for each agent is counted. | When each unique agent logs in to the system each day, this count is incremented. |
| Concurrent Agents Logged In | Shows the number of agents who were logged in at a given time. | If the log-in count in a day is higher than the previous max value, then this value is assigned as the max value. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Agent Name | Shows the name of the agent. Used As : Row Segment |  |  |
| Interval | Shows the time duration for which the Agent Details report is generated. |  | Last seven Days |
| Multimedia Profile Type | Shows the type of blended profile configured for the agent. The blended profile types are Blended, Blended Real-time, and Exclusive. |  |  |
| Channel Type | Shows the media type of the contact, such as voice, email, or chat. Used As : Row Segment |  |  |
| Login Count | Shows the total number of logins in which contacts of a specific channel type were configured for the agent. | Channel Type: voice, chat, email | Count of Agent Channel ID |
| Contact Handled | Shows the total number of contacts handled. |  | Sum of Outdial Connected Count + Sum of Connected Count |
| Staff Hours | Shows the total amount of time the agent was logged in. |  | Sum of Realtime Update Timestamp - Sum of Login Timestamp |
| Initial Login Time | Shows the date and time at which the agent first logged in. |  | Minimum Login Timestamp |
| Final Logout Time | Shows the date and time at which the agent last logged out. |  | Maximum Logout Timestamp |
| Occupancy | Shows the percentage of time the agent spent on the call compared to the available time and the idle time. |  | ((Sum of Connected Duration + Sum of Wrapup Duration) + (Sum of Outdial Connected Duration + Sum of Outdial Wrapup Duration)) / (Maximum Logout Timestamp - Minimum Login Timestamp) |
| Idle Count | Shows the number of times the agent went into the Idle state. |  | Sum of Idle Count |
| Total Idle Time | Shows the total amount of time the agent spent in the Idle state. |  | Sum of Idle Duration |
| Average Idle Time | Shows the average duration for which the agent was in the Idle state. |  | Sum of Idle Duration / Sum of Idle Count |
| Available Count | Shows the number of times the agent went into the Available state. |  | Sum of Available Count |
| Total Available Time | Shows the total amount of time the agent spent in the Available state. |  | Sum of Available Duration |
| Average Available Time | Shows the average length of time an agent was in the Available state. |  | Sum of Available Duration / Sum of Available Count |
| Inbound Reserved Count | Shows the number of times an agent went into the Inbound Reserved
                            state. |  | Sum of Inbound Reserved Count |
| Ringing Duration | Shows the total amount of time an agent spent in the Reserved state
                            (time duration after a call comes in to an agent’s station but is not
                            yet answered). |  | Sum of Ringing Duration |
| Inbound Reserved Total Time | Shows the total amount of time an agent spent in the Reserved state
                            (time duration after a call comes in to an agent’s station but is not
                            yet answered). |  | Sum of Inbound Reserved Duration |
| Average Inbound Reserved Time | Shows the average length of time an agent was in the Inbound Reserved state. |  | Sum of Ringing Duration / Sum of Ringing Count |
| Inbound Hold Count | Shows the number of times an agent put an inbound caller on hold. |  | Sum of Hold Count |
| Inbound Hold Total Time | Shows the total amount of time the inbound calls were on hold. |  | Sum of Hold Duration |
| Average Inbound Hold Time | Shows the average hold time for inbound calls. |  | Sum of Hold Duration / Sum of Hold Count |
| Inbound Connected Count | Shows the number of inbound calls that were connected to an agent. |  | Sum of Connected Count |
| Inbound Connected Total Time | Shows the total amount of time an agent was talking to customers on inbound calls. Inbound Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. |  | Sum of Connected Duration |
| Inbound Contact Total Time | Shows the total amount of time an agent was connected to inbound calls. |  | Sum of Connected Duration + Sum of Hold Duration |
| Average Inbound Contact Time | Shows the average inbound contact time. |  | (Sum of Connected Duration + Sum of Hold Duration) / Sum of Connected Count |
| Outdial Reserved Count | Shows the number of times an agent was in the Outdial Reserved state, a state indicating that the agent has initiated an outdial call, but the call isn’t connected yet. |  | Sum of Outdial Ringing Count |
| Outdial Reserved Total Time | Shows the total amount of time an agent was in the Outdial Reserved state. |  | Sum of Outdial Ringing Duration |
| Average Outdial Reserved Time | Shows the average amount of time an agent was in the Outdial Reserved state. |  | Sum of Outdial Ringing Duration / Sum of Outdial Ringing Count |
| Outdial Hold Count | Shows the number of times an agent put an outbound caller on hold. |  | Sum of Outdial Hold Count |
| Outdial Hold Total Time | Shows the total amount of time the outbound calls were on hold. |  | Sum of Outdial Hold Duration |
| Average Outdial Hold Time | Shows the average hold time for outbound calls. |  | Sum of Outdial Hold Duration / Sum of Outdial Hold Count |
| Outdial Attempted Count | Shows the number of times an agent attempted to make an outdial call. |  | Sum of Outdial Ringing Count |
| Outdial Connected Count | Shows the number of outdial calls that were connected to an agent. |  | Sum of Outdial Connected Count |
| Outdial Connected Total Time | Shows the total amount of time an agent was talking to customers on outdial calls. Outdial Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. |  | Sum of Outdial Connected Duration |
| Outdial Contact Total Time | Shows the total amount of time an agent was connected to outdial calls. |  | Sum of Outdial Connected Duration + Sum of Hold Duration |
| Average Outdial Contact Time | Shows the average outdial contact time. |  | (Sum of Outdial Connected Duration + Sum of Hold Duration) / Sum of Outdial Connected Count |
| Sudden Disconnected Count | Shows the number of calls that were answered (that is, connected to an agent or distributed to and accepted by a destination site), but that were then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise. |  | Sum of Disconnected Count |
| Inbound Wrapup Count | Shows the number of times an agent went into the Wrapup state after an inbound call. |  | Sum of Wrapup Count |
| Inbound Wrapup Total Time | Shows the total amount of time an agent spent in the Wrapup state after an inbound call. |  | Sum of Wrapup Duration |
| Average Inbound Wrapup Time | Shows the average length of time an agent was in the Wrapup state after an inbound call. |  | Sum of Wrapup Duration / Sum of Wrapup Count |
| Outdial Wrapup Count | Shows the number of times an agent went into the Wrapup state after an outbound call. |  | Sum of Outdial Wrapup Count |
| Outdial Wrapup Total Time | Shows the total amount of time an agent spent in the Wrapup state after an outbound call. |  | Sum of Outdial Wrapup Duration |
| Average Outdial Wrapup Time | Shows the average length of time an agent was in the Wrapup state after an outbound call. |  | Sum of Outdial Wrapup Duration / Sum of Outdial Wrapup Count |
| Not Responding Count | The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent. |  | Sum of Not Responded Count |
| Not Responding Total Time | Shows the total amount of time an agent spent in the Not Responding state. |  | Sum of Not Responded Duration |
| Average Not Responding Time | Shows the average length of time an agent was in the Not Responding state. |  | Sum of Not Responded Duration / Sum of Not Responded Count |
| Consult Answer Count | Shows the number of consults that an agent received. |  | Sum of Consult Answer Count |
| Consult Answer Total Time | Shows the total amount of time an agent spent answering consult requests. |  | Sum of Consult Answer Duration |
| Average Consult Answer Time | Shows the average length of time an agent spent answering consult requests. |  | Sum of Consult Duration / Sum of Consult Count |
| Consult Request Count | The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. |  | Sum of Consult Request Count |
| Consult Request Total Time | Shows the total amount of time an agent spent consulting other agents. |  | Sum of Consult Request Duration |
| Average Consult Request Time | Shows the average length of time an agent spent consulting other agents. |  | Sum of Consult Request Duration / Sum of Consult Request Count |
| Consult Count | Shows the number of consults that an agent was involved in. This includes consults the agent made or received. |  | Sum of Consult Count |
| Total Consult Time | Shows the total amount of time an agent spent answering consult requests. |  | Sum of Consult Duration |
| Average Consult Time | Shows the average length of time an agent spent answering consult requests. |  | Sum of Consult Answer Duration / Sum of Consult Answer Count |
| Conference Count | Shows the number of times an agent initiated a conference call. |  | Sum of Conference Count |
| Inbound CTQ Request Count | The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. |  | Sum of CTQ Request Count |
| Inbound Total CTQ Request Time | Shows the total amount of time an agent spent answering consult-to-queue requests from an agent handling an inbound call. |  | Sum of CTQ Request Duration |
| Inbound CTQ Answer Count | Shows the number of times an agent answered a consult-to-queue request from another agent who was handling an inbound call. |  | Sum of CTQ Answer Count |
| Inbound Total CTQ Answer Time | Shows the total amount of time an agent spent answering consult-to-queue requests from an agent handling an inbound call. |  | Sum of CTQ Answer Duration |
| Outdial CTQ Request Count | The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent. |  | Sum of Outdial CTQ Request Count |
| Outdial CTQ Total Request Time | Shows the total amount of time an agent spent on a consultation via a consult-to-queue initiated by this agent while handling an outdial call. |  | Sum of Outdial CTQ Request Duration |
| Outdial CTQ Answer Count | Shows the number of times an agent answered a consult-to-queue request from another agent who was handling an outdial call. |  | Sum of Outdial CTQ Answer Count |
| Outdial CTQ Total Answer Time | Shows the total amount of time an agent spent answering consult-to-queue requests from another agent who was handling an outdial call. |  | Sum of Outdial CTQ Answer Duration |
| Agent Transfer | Shows the number of times an agent transferred inbound contacts to another agent after consult. |  | Sum of Agent To Agent Transfer Count |
| Agent Requeue | Shows the number of times an agent requeued an inbound call. |  | Sum of Agent Transfer To Queue Request Count |
| Blind Transfer | Shows the number of times an agent transferred an inbound call to either an external or third-party Dial Number (DN) through the Interactive Voice Response (IVR) without agent intervention. |  | Sum of Blind Transfer Count |
| Inbound Average Handle Time | Shows the average length of time an agent spent handling an inbound call. |  | (Sum of Connected Duration +  Sum of Wrapup Duration) / Sum of Connected Count |
| Outdial Average Handle Time | Shows the average length of time an agent spent handling an outbound call. |  | (Sum of Outdial Connected Duration +  Sum of Outdial Wrapup Duration) / Sum of Outdial Connected Count |
| Engaged Count | Shows the number of times the agent went into the Engaged state. |  | Sum of Engaged Count |
| Engaged Duration | Shows the total amount of time an agent was engaged. |  | Sum of Engaged Duration |
| Average Engaged Duration | Shows the average engaged duration. |  | Sum of Engaged Duration / Sum of Engaged Count |

| Parameter | Description |
|---|---|
| Login/Skill-Update Time | Shows the next login date and time for an agent whose skill profile/skills were updated when logged out, or the date and time when the skill profile/skills were updated for an agent who is currently logged in. |
| Skill Profile | Shows the name of the skill profile that is associated with an agent. |
| Skills | Shows the skill of an agent, such as language fluency or product expertise. The column shows multiple skills mapped to the corresponding skill profile, in a comma-separated single string. |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of the agent. Used As : Row Segment |  |
| Calls Handled | Number of calls that were connected to an agent. If the agent established a conference with another agent, the value increases by one for the conferenced agent. If the agent transferred a call and the call was transferred back to the agent, the value increases by two. | Count of Wrapup Code Name |
| Average Handle Time | Average handle time for all calls that the agent handled. | Total Handle Time / Calls Handled |
| Average Talk Time | Average time that an agent spent in a call. | Average of Connected Duration |
| Max Talk Time | Maximum time that an agent spends on a call. |  |
| Average Hold Time | Average time that an agent put a call on hold. | Average of Hold Duration |
| Max Hold Time | Maximum time that an agent put a call on hold. | Maximum Hold Duration |
| Average Work Time | Average time that an agent was engaged after disconnecting or transferring a call. | Average of Wrapup Duration |
| Max Work Time | Maximum time that an agent was engaged after disconnecting or transferring a call. | Maximum Wrapup Duration |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Agent Name | Shows the name of the agent. Used As : Row Segment |  |  |
| Team Name | The name of a team. Used As : Row Segment |  |  |
| Queue Name | The name of a queue. Calls move from an entry point into a queue and then gets redirected to agents. |  | Queue Name |
| Average Auto CSAT | Average of the AI-generated predicted automatic customer satisfaction scores |  |  |
| Max Auto CSAT | Highest predicted automatic customer satisfaction score |  |  |
| Min Auto CSAT | Lowest predicted automatic customer satisfaction score |  |  |

| Media Type | Description | Formula |
|---|---|---|
| Voice | The media type of the  telephony contact. | Count of Connected Count (Channel Type = telephony) + Count of Outdial Connected Count (Channel Type = telephony) |
| Chat | The media type of the chat  contact. | Count of Connected Count (Channel Type = chat) |
| Email | The media type of the email contact. | Count of Connected Count (Channel Type = email) + Count of Outdial Connected Count (Channel Type = email) |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of an agent, that is, a person who handles customer calls. Used As : Row Segment |  |
| Interval | Time period for which the outdial call information is available. | Last 7 Days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Initial Login Time | The date and time when the agent logged in for the first time during the interval. | Minimum Login Timestamp |
| Outdial Contact Handled | The number of outbound calls that the agent handled. | Sum of Outdial Connected Count |
| Outdial Average Handle Time | The average handle time for outbound calls. | (Sum of Outdial Connected Duration +  Sum of Outdial Wrapup Duration) / Sum of Outdial Connected Count |
| Outdial Connected Time | The total duration for which the agent was in conversation with the customer on the outdial call, this includes outdial hold duration. | Sum of Outdial Duration |
| Outdial Average Connected Time | The average outdial connected time. | Outdial Connected Time / Outdial Contact Handled |
| Outdial Talk Time | The total duration for which the agent was in conversation with the customer on the outdial call. | Outdial Connected Time - Outdial Hold Duration |
| Number of Transfers | The number of times the calls were transferred. |  |
| Average Consult Talk Duration | The average duration for which the agent consulted with another agent or a third party, keeping the caller on hold. | Total Consult Duration / Total Consult Count |

| Parameter | Description | Formula |
|---|---|---|
| Call Transfer Time | The time at which the call got transferred. |  |
| Transfer Type | The type of transfer such as Blind Transfer and Consult Transfer. |  |
| Transferred to Number | The number to which the call was transferred. |  |
| Transferred to Queue | The queue to which the call was transferred. |  |
| Consult Talk Duration | The duration for which the agent consulted with another agent or a third party, keeping the caller on hold. |  |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of an agent, that is, a person who answers customer calls. Used As : Row Segment |  |
| Interval | Time period for which the agent statistics is available | Last 7 Days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Login Time | The date and time when the agent logged in. | Minimum Login Timestamp |
| Handled | The total number of interactions handled. | Handled = Sum of Outdial Connected Count + Sum of Post Call Duration + Sum of Connected Count |
| Total Handle Time | The cumulative amount of time spent handling calls. | Total Handle time = (Sum of Connected Duration  + Sum of Wrapup Duration) + (Sum of Outdial Connected Duration + Sum of Outdial Wrapup) |
| Avg Handle Time | The average length of time spent handling a call. | (Sum of Hold Duration + Sum of Connected Duration  + Sum of Wrapup Duration) / Count of Contact Session ID (Termination Type = Normal) |

| Parameter | Description |
|---|---|
| Login/Skill-Update Time | Shows the next login date and time for an agent whose skill profile/skills were updated when logged out, or the date and time when the skill profile/skills were updated for an agent who is currently logged in. |
| Skill Profile | Shows the name of the skill profile that is associated with an agent. |
| Skills | Shows the skill of an agent, such as language fluency or product expertise. The column shows multiple skills mapped to the corresponding skill profile, in a comma-separated single string. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Agent Name | Shows the name of the agent. Used As : Row Segment |  |  |
| Wellness Breaks | Number of automated wellbeing breaks offered to agents based on insights from AI-powered agent burnout detection calculations. |  |  |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Agent Name | Shows the name of the agent. Used As : Row Segment |  |  |
| Team Name | The name of a team. Used As : Row Segment |  |  |
| Queue Name | The name of a queue. Calls move from an entry point into a queue and then gets redirected to agents. |  | Queue Name |
| Site Name | The call center location to which a call was redirected. Used As : Row Segment |  |  |
| Call Duration | The time elapsed between the start time and the end time of the call. |  |  |
| Termination Type | A text string specifying how a call was terminated. |  | Value of Termination type |
| Termination Reason | The reason for ending the contact. The reason can be one of the following: Agent left Customer Busy Customer Left Customer Unavailable Not Found Participant Invite Timer Expired |  |  |

| Parameter | Description | Formula |
|---|---|---|
| Site Name | The call center location to which a call was distributed. Used As : Row Segment |  |
| Interval | Time period for which the agent statistics in each site is available. | Last 7 Days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Contact Handled | The total number of contacts handled. | Sum of Connected Count + Sum of Outdial Connected Count |
| Staff Hours | The total amount of time agents were logged in. | Sum of Realtime Update Timestamp - Sum of Login Timestamp |
| Occupancy | The measure of time agents spent on calls compared to available and idle time. | ((Sum of Connected Duration + Sum of Wrapup Duration) + (Sum of Outdial Connected Duration + Sum of Outdial Wrapup Duration)) / (Maximum Logout Timestamp - Minimum Login Timestamp) |
| Idle Count | The number of times agents went into the Idle state. | Sum of Idle Count |
| Total Idle Time | The total amount of time agents spent in the Idle state. | Sum of Idle Duration |
| Average Idle Time | The average length of time agents were in the Idle state. | Sum of Idle Duration / Sum of Idle Count |
| Available Count | The number of times agents went into the Available state. | Sum of Available Count |
| Total Available Time | The total amount of time agents spent in the Available state. | Sum of Available Duration |
| Average Available Time | The average length of time agents were in the Available state. | Sum of Available Duration / Sum of Available Count |
| Inbound Reserved Count | The number of times agents went into the Inbound Reserved state. | Sum of Inbound Reserved Count |
| Ringing Duration | The total number of times agents spent in the Reserved state (time
                                duration after a call comes in to an agent’s station but is not yet
                                answered). | Sum of Ringing Duration |
| Inbound Reserved Total Time | The total number of times agents spent in the Reserved state (time
                                duration after a call comes in to an agent’s station but is not yet
                                answered). | Sum of Inbound Reserved Duration |
| Average Inbound Reserved Time | The average length of time agents were in the Inbound Reserved
                                state. | Sum of Ringing Duration / Sum of Ringing Count |
| Inbound Hold Count | The number of times agents put inbound callers on hold. | Sum of Hold Count |
| Inbound Hold Time | The total amount of time the inbound calls were on hold. | Sum of Hold Duration |
| Average Inbound Hold Time | The average hold time for inbound calls. | Sum of Hold Duration / Sum of Hold Count |
| Inbound Connected Count | The number of inbound calls that were connected to agents. | Sum of Connected Count |
| Inbound Connected Total Time | The total amount of time agents were talking to customers on inbound calls. Inbound Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. | Sum of Connected Duration |
| Inbound Contact Total Time | The total amount of time agents were connected to inbound calls. | Sum of Connected Duration + Sum of Hold Duration |
| Average Inbound Contact Total Time | The average inbound connected time. | (Sum of Connected Duration + Sum of Hold Duration) / Sum of Connected Count |
| Outdial Reserved Count | The number of times agents were in the Outdial Reserved state (time duration after a call is ringing and before a call is answered). | Sum of Outdial Ringing Count |
| Outdial Reserved Total Time | The total amount of time agents were in the Outdial Reserved state. | Sum of Outdial Ringing Duration |
| Average Outdial Reserved Time | The average amount of time agents were in the Outdial Reserved state. | Sum of Outdial Ringing Duration / Sum of Outdial Ringing Count |
| Outdial Hold Count | The number of times agents put outdial calls on hold. | Sum of Outdial Hold Count |
| Outdial Total Hold Time | The total amount of time the outdial calls were on hold. | Sum of Outdial Hold Duration |
| Average Outdial Hold Time | The average hold time for outdial calls. | Sum of Outdial Hold Duration / Sum of Outdial Hold Count |
| Outdial Attempted Count | The number of times agents attempted to make outdial calls. | Sum of Outdial Ringing Count |
| Outdial Connected Count | The number of outdial calls that were connected to agents. | Sum of Outdial Connected Count |
| Outdial Connected Total Time | The total amount of time agents were talking to customers on outdial calls. Outdial Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. | Sum of Outdial Connected Duration |
| Outdial Contact Total Time | The total amount of time agents were connected to outdial calls. | Sum of Outdial Connected Duration + Sum of Hold Duration |
| Average Outdial Contact Time | The average outdial connected time. | (Sum of Outdial Connected Duration + Sum of Hold Duration) / Sum of Outdial Connected Count |
| Sudden Disconnected Count | The number of calls that were connected to agents, but that were then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise. | Sum of Disconnected Count |
| Inbound Wrapup Count | The number of times agents went into the Wrapup state after an inbound call. | Sum of Wrapup Count |
| Inbound Wrapup Total Time | The total amount of time agents spent in the Wrapup state after an inbound call. | Sum of Wrapup Duration |
| Average Inbound Wrapup Time | The average length of time agents were in the Wrapup state after an inbound call. | Sum of Wrapup Duration / Sum of Wrapup Count |
| Outdial Wrapup Count | The number of times agents went into the Wrapup state after an outdial call. | Sum of Outdial Wrapup Count |
| Outdial Wrapup Total Time | The total amount of time agents spent in the Wrapup state after an outdial call. | Sum of Outdial Wrapup Duration |
| Average Outdial Wrapup Time | The average length of time agents were in the Wrapup state after an outdial call. | Sum of Outdial Wrapup Duration / Sum of Outdial Wrapup Count |
| Not Responding Count | The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent. | Sum of Not Responded Count |
| Not Responding Total Time | The total amount of time agents spent in the Not Responding state. | Sum of Not Responded Duration |
| Average Not Responding Time | The average length of time agents were in the Not Responding state. | Sum of Not Responded Duration / Sum of Not Responded Count |
| Consult Answer Count | The number of times agents answered a consult request from another agent. | Sum of Consult Count |
| Consult Answer Total Time | The total amount of time agents spent answering consult requests. | Sum of Consult Answer Duration |
| Average Consult Answer Time | The average length of time agents spent answering consult requests. | Sum of Consult Duration / Sum of Consult Count |
| Consult Request Count | The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. | Sum of Consult Request Count |
| Consult Request Total Time | The total amount of time agents spent consulting other agents. | Sum of Consult Request Duration |
| Average Consult Request Time | The average length of time agents spent consulting other agents. | Sum of Consult Request Duration / Sum of Consult Request Count |
| Consult Count | The number of times agents answered consult requests plus the number of times agents consulted other agents. | Sum of Consult Answer Count |
| Total Consult Time | Total Consult Answer Time plus Total Consult Request Time. | Sum of Consult Duration |
| Average Consult Time | The average length of consulting time. | Sum of Consult Answer Duration / Sum of Consult Answer Count |
| Conference Count | The number of times agents initiated a conference call. | Sum of Conference Count |
| Inbound CTQ Request Count | The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. | Sum of CTQ Request Count |
| Inbound Total CTQ Request Time | The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls. | Sum of CTQ Request Duration |
| Inbound CTQ Answer Count | The number of times agents answered consult-to-queue requests from other agents who were handling inbound calls. | Sum of CTQ Answer Count |
| Inbound Total CTQ Answer Time | The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls. | Sum of CTQ Answer Duration |
| Outdial CTQ Request Count | The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent. | Sum of Outdial CTQ Request Count |
| Outdial CTQ Total Request Time | Shows the total amount of time an agent spent on a consultation via a consult-to-queue initiated by this agent while handling an outdial call. | Sum of Outdial CTQ Request Duration |
| Outdial CTQ Answer Count | The number of times agents answered consult-to-queue requests from other agents who were handling outdial calls. | Sum of Outdial CTQ Answer Count |
| Outdial CTQ Total Answer Time | The total amount of time agents spent answering consult-to queue requests from other agents who were handling outdial calls. | Sum of Outdial CTQ Answer Duration |
| Agent Transfer | The number of times an agent transferred inbound contacts to another agent after consult. | Sum of Agent To Agent Transfer Count |
| Agent Requeue | The number of times agents requeued inbound calls. | Sum of Agent Transfer To Queue Request Count |
| Blind Transfer | The number of times agents transferred inbound calls to either an external or third-party Dial Number (DN) through the Interactive Voice Response (IVR) without agent intervention. | Sum of Blind Transfer Count |
| Inbound Average Handle Time | The average length of time an agent spent handling inbound calls. | (Sum of Connected Duration  + Sum of Wrapup Duration) / Sum of Connected Count |
| Outdial Average Handle Time | The average length of time an agent spent handling outdial calls. | (Sum of Outdial Connected Duration  + Sum of Outdial Wrapup Duration) / Sum of Outdial Connected Count |
| Engaged Count | Shows the number of times the agent went into the Engaged state. | Sum of Engaged Count |
| Engaged Duration | Shows the total amount of time an agent was engaged. | Sum of Engaged Duration |
| Average Engaged Duration | Shows the average engaged duration. | Sum of Engaged Duration / Sum of Engaged Count |

| Parameter | Description | Formula |
|---|---|---|
| Team Name | The name of a team. Used As : Row Segment |  |
| Interval | Time period for which the agent activity is available. | Last 7 Days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment. |  |
| Contact Handled | The total number of contacts handled. | Sum of Connected Count + Sum of Outdial Connected Count |
| Staff Hours | The total amount of time agents were logged in. | Sum of Realtime Update Timestamp - Sum of Login Timestamp |
| Occupancy | The measure of time agents spent on calls compared to available and idle time. | ((Sum of Connected Duration + Sum of Wrapup Duration) + (Sum of Outdial Connected Duration +
                            Sum of Outdial Wrapup Duration)) / (Maximum Logout Timestamp - Minimum
                            Login Timestamp) |
| Idle Count | The number of times agents went into the Idle state. | Sum of Idle Count |
| Total Idle Time | The total amount of time agents spent in the Idle state. | Sum of Idle Duration |
| Average Idle Time | The average length of time agents were in the Idle state. | Sum of Idle Duration / Sum of Idle Count |
| Available Count | The number of times agents went into the Available state. | Sum of Available Count |
| Total Available Time | The total amount of time agents spent in the Available state. | Sum of Available Duration |
| Average Available Time | The average length of time agents were in the Available state. | Sum of Available Duration / Sum of Available Count |
| Inbound Reserved Count | The number of times agents went into the Inbound Reserved state (time
                            duration after a call comes in to an agent’s station but is not yet
                            answered). | Sum of Inbound Reserved Count |
| Ringing Duration | The total amount of time agents spent in the Reserved state. | Sum of Ringing Duration |
| Inbound Reserved Total Time | The total amount of time agents spent in the Reserved state. | Sum of Inbound Reserved Duration |
| Average Inbound Reserved Time | The average length of time agents were in the Inbound Reserved state. | Sum of Ringing Duration / Sum of Ringing Count |
| Inbound Hold Count | The number of times agents put inbound callers on hold. | Sum of Hold Count |
| Inbound Hold Time | The total amount of time the inbound calls were on hold. | Sum of Hold Duration |
| Average Inbound Hold Time | The average hold time for inbound calls. | Sum of Hold Duration / Sum of Hold Count |
| Inbound Connected Count | The number of inbound calls that were connected to agents. | Sum of Connected Count |
| Inbound Connected Total Time | The total amount of time agents were talking to customers on inbound calls. Inbound Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. | Sum of Connected Duration |
| Inbound Contact Total Time | The total amount of time agents were connected to inbound calls. | Sum of Connected Duration + Sum of Hold Duration |
| Average Inbound Contact Total time | The average inbound connected time. | (Sum of Connected Duration + Sum of Hold Duration) / Sum of Connected Count |
| Outdial Reserved Count | The number of times agents were in the Outdial Reserved state (time duration after the call starts ringing and before the call is answered). | Sum of Outdial Ringing Count |
| Outdial Reserved Total Time | The total amount of time agents were in the Outdial Reserved state. | Sum of Outdial Ringing Duration |
| Average Outdial Reserved Time | The average amount of time agents were in the Outdial Reserved state. | Sum of Outdial Ringing Duration / Sum of Outdial Ringing Count |
| Outdial Hold Count | The number of times agents put outdial calls on hold. | Sum of Outdial Hold Count |
| Outdial Total Hold Time | The total amount of time the outdial calls were on hold. | Sum of Outdial Hold Duration |
| Average Outdial Hold Time | The average hold time for outdial calls. | Sum of Outdial Hold Duration / Sum of Outdial Hold Count |
| Outdial Attempted Count | The number of times agents attempted to make outdial calls. | Sum of Outdial Ringing Count |
| Outdial Connected Count | The number of outdial calls that were connected to agents. | Sum of Outdial Connected Count |
| Outdial Connected Total Time | The total amount of time an agent was talking to customers on outdial calls. Outdial Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. | Sum of Outdial Connected Duration |
| Outdial Contact Total Time | The total amount of time an agent was connected to outdial calls. | Sum of Outdial Connected Duration + Sum of Hold Duration |
| Average Outdial Contact Time | The average outdial contact time. | (Sum of Outdial Connected Duration + Sum of Hold Duration) / Sum of Outdial Connected Count |
| Sudden Disconnect Count | The number of calls that were connected to agents, but then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise. | Sum of Disconnected Count |
| Inbound Wrapup Count | The number of times agents went into the Wrapup state after an inbound call. | Sum of Wrapup Count |
| Inbound Wrapup Total Time | The total amount of time agents spent in the Wrapup state after an inbound call. | Sum of Wrapup Duration |
| Average Inbound Wrapup Time | The average length of time agents were in the Wrapup state after an inbound call. | Sum of Wrapup Duration / Sum of Wrapup Count |
| Outdial Wrapup Count | The number of times agents went into the Wrapup state after an outdial call. | Sum of Outdial Wrapup Count |
| Outdial Wrapup Total Time | The total amount of time agents spent in the Wrapup state after an outdial call. | Sum of Outdial Wrapup Duration |
| Average Outdial Wrapup Time | The average length of time agents were in the Wrapup state after an outdial call. | Sum of Outdial Wrapup Duration / Sum of Outdial Wrapup Count |
| Not Responding Count | The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent. | Sum of Not Responded Count |
| Not Responding Total Time | The total amount of time agents spent in the Not Responding state. | Sum of Not Responded Duration |
| Average Not Responding Time | The average length of time agents were in the Not Responding state. | Sum of Not Responded Duration / Sum of Not Responded Count |
| Consult Answer Count | The number of times agents answered consult requests from other agents. | Sum of Consult Count |
| Consult Answer Total Time | The total amount of time agents spent answering consult requests. | Sum of Consult Answer Duration |
| Average Consult Answer Time | The average length of time agents spent answering consult requests. | Sum of Consult Duration / Sum of Consult Count |
| Consult Request Count | The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. | Sum of Consult Request Count |
| Consult Request Total Time | The total amount of time agents spent consulting other agents. | Sum of Consult Request Duration |
| Average Consult Request Time | The average length of time agents spent consulting other agents. | Sum of Consult Request Duration / Sum of Consult Request Count |
| Consult Count | The number of times agents answered consult requests plus the number of times agents consulted other agents. | Sum of Consult Answer Count |
| Total Consult Time | The sum of the total amount of time agents spent on consulting another agent, and on answering consult requests. | Sum of Consult Duration |
| Average Consult Time | The average length of consulting time. | Sum of Consult Answer Duration / Sum of Consult Answer Count |
| Conference Count | The number of times agents initiated conference calls. | Sum of Conference Count |
| Inbound CTQ Request Count | The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. | Sum of CTQ Request Count |
| Inbound Total CTQ Request Time | The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls. | Sum of CTQ Request Duration |
| Inbound CTQ Answer Count | The number of times agents answered consult-to-queue requests from other agents who were handling inbound calls. | Sum of CTQ Answer Count |
| Inbound Total CTQ Answer Time | The total amount of time agents spent answering consult-to-queue requests from other agents who were handling inbound calls. | Sum of CTQ Answer Duration |
| Outdial CTQ Request Count | The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent. | Sum of Outdial CTQ Request Count |
| Outdial CTQ Total Request Time | Shows the total amount of time an agent spent on a consultation via a consult-to-queue initiated by this agent while handling an outdial call. | Sum of Outdial CTQ Request Duration |
| Outdial CTQ Answer Count | The number of times agents answered consult-to-queue requests from other agents who were handling outdial calls. | Sum of Outdial CTQ Answer Count |
| Outdial CTQ Total Answer Time | The total amount of time agents spent answering consult-to-queue requests from other agents who were handling outdial calls. | Sum of Outdial CTQ Answer Duration |
| Agent Transfer | The number of times an agent transferred inbound contacts to another agent after consult. | Sum of Agent To Agent Transfer Count |
| Agent Requeue | The number of times agents requeued inbound calls. | Sum of Agent Transfer To Queue Request Count |
| Blind Transfer | The number of times agents transferred inbound calls to either an external or third-party Dial Number (DN) through the Interactive Voice Response (IVR) without agent intervention. | Sum of Blind Transfer Count |
| Inbound Average Handle Time | The average length of time an agent spent handling inbound calls. | (Sum of Connected Duration  + Sum of Wrapup Duration) / Sum of Connected Count |
| Outdial Average Handle Time | The average length of time an agent spent handling outdial calls. | (Sum of Outdial Connected Duration  + Sum of Outdial Wrapup Duration) / Sum of Outdial Connected Count |
| Engaged Count | Shows the number of times the agent went into the Engaged state. | Sum of Engaged Count |
| Engaged Duration | Shows the total amount of time an agent was engaged. | Sum of Engaged Duration |
| Average Engaged Duration | Shows the average engaged duration. | Sum of Engaged Duration / Sum of Engaged Count |

| Parameter | Description | Formula |
|---|---|---|
| Voice | The media type of the telephony contact. | Count of Connected Count (Channel Type = telephony) + Count of Outdial Connected Count (Channel Type = telephony) |
| Chat | The media type of the chat contact. | Count of Connected Count (Channel Type = chat) |
| Email | The media type of the email contact. | Count of Connected Count (Channel Type = email) + Count of Outdial Connected Count (Channel Type = email) |

| Parameter | Description | Formula |
|---|---|---|
| Team name | The name of a team. Used As : Row Segment |  |
| Agent name | (Shows the name of the agent. Used As : Row Segment |  |
| Total Connected Count | The number of inbound calls and outdial calls that were connected to an agent | Sum of Connected Count + Sum of Outdial Connected Count |
| Connected Count - Inbound | The number of inbound calls that were connected to an agent. | Sum of Inbound Connected Count |
| Connected Count - Outdial | The number of outdial calls that were connected to an agent. | Sum of Outdial Connected Count |
| Total Connected Duration | The total amount of time agents were talking to customers on outdial calls and
              inbound calls. Total Connected Duration does not include the Idle Time, Hold Duration,
              or Consult Time. | Sum of Total Connected Duration + Sum of Total Outdial Connected Duration |
| Total Connected Duration - Inbound | The total amount of time agents were talking to customers on inbound calls. Total
              Connected Duration - Inbound does not include the Idle Time, Hold Duration, or Consult
              Time. | Sum of Total Connected Duration |
| Total Connected Duration - Outdial | The total amount of time agents were talking to customers on outdial calls. Total
              Connected Duration -Outdial does not include the Idle Time, Hold Duration, or Consult
              Time. | Sum of Total Outdial Connected Duration |
| Average Handle Time | The average length of time an agent spent handling inbound calls and outdial
              calls. | (Sum of Total Connected Duration+ Sum of Total Hold Duration + Sum of Post Call
                Duration + Sum of Total Wrapup Duration +Sum of Total Outdial Connected Duration +Sum of Total Outdial Hold Duration +Sum of Outdial Post Call Duration +Sum of Total Outdial Wrapup Duration ) / (Sum of Outdial Connected Count + Sum of Connected Count) |
| Average Evaluation Score (in %) | Average Evaluation Score in integer between 0 and 100 | (Sum of Overall Evaluation Score +Sum of Outdial Overall Evaluation Score ) / (Sum of Overall Evaluation Score Count +Sum of Outdial Overall Evaluation Score Count) |
| Average Evaluation Score - Inbound (%) | Total Evaluation Score in integer between 0 and 100 (Inbound) | Sum of Overall Evaluation Score / Sum of Overall Evaluation Score Count |
| Average Evaluation Score - Outdial (%) | Total Evaluation Score in integer between 0 and 100 (Outdial) | Sum of Outdial Overall Evaluation Score /Sum of Outdial Overall Evaluation Score Count |
| Total Evaluations Failed Count | Number of evaluations failed by agent in autofail. Even if 1 section in an
              evaluation is failed, it counts the entire evaluation as failed. Value is integer
              (>=0) | Sum of Evaluation Interaction Failure Count + Sum of Outdial Evaluation Interaction Failure Count |
| Evaluations Failed Count - Inbound | Number of evaluations failed by agent in autofail (Inbound). Even if 1 section in
              an evaluation is failed, it counts the entire evaluation as failed. Value is integer
              (>=0) | Sum of Evaluation Interaction Failure Count |
| Evaluations Failed Count - Outdial | Number of evaluations failed by agent in autofail (Outbound). Even if 1 section
              in an evaluation is failed, it counts the entire evaluation as failed. Value is
              integer (>=0) | Sum of Outdial Evaluation Interaction Failure Count |
| Average Word Ratio | Average of Number of words spoken by agent over total number of transcript words
              in interactions (%) | (Sum of Word Ratio Score +Sum of Outdial Word Ratio Score) / (Sum of Outdial Word Ratio Count + Sum of Word Ratio Count) |
| Word Ratio - Inbound | Average of Number of words spoken by agent over total number of transcript words
              in interactions (%) (Inbound) | Sum of Word Ratio Score /Sum of Word Ratio Count |
| Word Ratio - Outdial | Average of Number of words spoken by agent over total number of transcript words
              in interactions (%) (Outdial) | Sum of Outdial Word Ratio Score /Sum of Outdial Word Ratio Count |
| Average dead air time | Average Duration for which neither customer nor agent spoke in HH:MM:SS across
              interactions | (Sum of Dead Air Time + Sum of Outdial Dead Air Time) / (Count of Dead Air Count +Count of Outdial Dead Air Count) |
| Average Dead Air Time - Inbound | Average Duration for which neither customer nor agent spoke in HH:MM:SS across
              interactions (Inbound) | Average of Dead Air Time |
| Average Dead Air Time - Outdial | Average Duration for which neither customer nor agent spoke in HH:MM:SS across
              interactions (Outdial) | Average of Outdial Dead Air Time |
| Average Talkover Time | Average Duration for which agent spoke over customer HH:MM:SS across
              interactions | (Sum of Outdial Cross Talk Time +Sum of Talkover Time) / (Count of Talkover Count + Count of Outdial Cross Talk Count) |
| Average Talk Over Time - Inbound | Average Duration for which agent spoke over customer HH:MM:SS across interactions
              (Inbound) | Average of Talk Over Time - Inbound |
| Average Talk Over Time - Outdial | Average Duration for which agent spoke over customer HH:MM:SS across interactions
              (Outdial) | Average of Talk Over Time - Outdial |

| Parameter | Description | Formula | Drill-down Filter |
|---|---|---|---|
| Agent Name | The name of an agent, that is, a person who answers customer calls. Used As : Row Segment |  |  |
| Interval | Time period for which the agent activity is available. | Last seven Days |  |
| Site Name | The call center location to which a call got distributed. Used As : Row Segment |  |  |
| Team Name | A group of agents at a specific site who handle a particular type of call. Used As : Row Segment |  |  |
| Agent Endpoint (DN) | The dial number that the agent used to log in to the Agent Desktop Used As : Row Segment |  |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| Initial Login Time | The date and time when the agent logged in for the first time. This column appears only in agent-level summary reports. | Minimum Login Timestamp |  |
| Final Logout Time | The date and time when the agent logged out. This column appears only in agent level summary reports. | Maximum Logout Timestamp |  |
| Staff Hours | The total amount of time the agent was logged in. | Sum of Realtime Update Timestamp - Sum of Login Timestamp |  |
| Occupancy | The measure of time agents spent on calls compared to available and idle time. | ((Sum of Connected Duration + Sum of Wrapup Duration) + (Sum of Outdial Connected Duration + Sum of Outdial Wrapup Duration)) / (Maximum Logout Timestamp - Minimum Login Timestamp) |  |
| Idle Count | The number of times an agent went into the Idle state. | Sum of Idle Count |  |
| Total Idle Time | The total amount of time agents spent in the Idle state. | Sum of Idle Duration |  |
| Available Count | The number of times an agent went into the Available state. | Sum of Available Count |  |
| Total Available Time | The total amount of time agents spent in the Available state. | Sum of Available Duration |  |
| Avg Available Time | The average time agents were in the Available state. | Sum of Available Duration / Sum of Available Count |  |
| Inbound Reserved Count | The number of times an agent went into the Inbound Reserved
                                state. | Sum of Inbound Reserved Count |  |
| Ringing Duration | The total amount of time agents spent in the Reserved state. | Sum of Ringing Duration |  |
| Inbound Reserved Total Time | The total amount of time agents spent in the Reserved state. | Sum of Inbound Reserved Duration |  |
| Avg Inbound Reserved Time | The average amount of time agents spent in the Reserved state. | Sum of Ringing Duration / Sum of Ringing Count |  |
| Inbound Hold Count | The number of times an agent put an inbound caller on hold. | Sum of Hold Count |  |
| Inbound Total Hold Time | The total amount of time the inbound calls were on hold. | Sum of Hold Duration |  |
| Inbound Connected Count | The number of inbound calls that were connected to an agent. | Sum of Connected Count |  |
| Inbound Connected Total Time | The total amount of time an agent was talking to customers on inbound calls. Inbound Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. | Sum of Connected Duration |  |
| Inbound Contact Total Time | The total amount of time an agent was connected to inbound calls. | Sum of Connected Duration + Sum of Hold Duration |  |
| Avg Inbound Contact Total Time | The average inbound contact time. | (Sum of Connected Duration + Sum of Hold Duration) / Sum of Connected Count |  |
| Outdial Reserved Count | The number of times an agent was in the Outdial Reserved state. | Sum of Outdial Ringing Count |  |
| Outdial Reserved Total Time | The total amount of time agents were in the Outdial Reserved state. | Sum of Outdial Ringing Duration / Sum of Outdial Ringing Count |  |
| Average Outdial Reserved Time | Average time the agents were in the Outdial Reserved state. | Sum of Outdial Ringing Duration / Sum of Outdial Ringing Count |  |
| Outdial Hold Count | The number of times an agent put an outdial call on hold. | Sum of Outdial Hold Count |  |
| Outdial Total Hold Time | The total amount of time the outdial calls were on hold. | Sum of Outdial Hold Duration |  |
| Average Outdial Hold Time | The average hold time for outdial calls. | Sum of Outdial Hold Duration / Sum of Outdial Hold Count |  |
| Outdial Connected Count | The number of outdial calls that got connected to an agent. | Sum of Outdial Connected Count |  |
| Outdial Connected Total Time | The total amount of time an agent was talking to customers on outdial calls. Outdial Connected Total Time does not include the Idle Time, Hold Duration, or Consult Time. | Sum of Outdial Connected Duration |  |
| Outdial Contact Total Time | The total amount of time an agent was connected to outdial calls. | Sum of Outdial Connected Duration + Sum of Hold Duration |  |
| Average Outdial Contact Time | he average outdial contact time. | (Sum of Outdial Connected Duration + Sum of Hold Duration) / Sum of Outdial Connected Count |  |
| Sudden Disconnect Count | The number of calls that got connected to an agent, but then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise. | Sum of Disconnected Count |  |
| Inbound Wrapup Count | The number of times agents went into the Wrapup state after an inbound call. | Sum of Wrapup Count |  |
| Inbound Wrapup Total Time | The total amount of time agents spent in the Wrapup state after an inbound call. | Sum of Wrapup Duration |  |
| Average Inbound Wrapup Time | The percentage of time agents were in the Wrapup state after an inbound call. | Sum of Wrapup Duration / Sum of Wrapup Count |  |
| Outdial Wrapup Count | The number of times agents went into the Wrapup state after an outdial call. | Sum of Outdial Wrapup Count |  |
| Outdial Wrapup Total Time | The total amount of time agents spent in the Wrapup state after an outdial call. | Sum of Outdial Wrapup Duration |  |
| Average Outdial Wrapup Time | The average time agents were in the Wrapup state after an outdial call. | Sum of Outdial Wrapup Duration / Sum of Outdial Wrapup Count |  |
| Reason | Reason identifier | Count of Reason |  |
| Avg Idle Time | The average time agents were in the Idle state. | Sum of Idle Duration / Sum of Idle Count |  |
| Avg Inbound Hold Time | The average hold time for inbound calls. | Sum of Hold Duration / Sum of Hold Count |  |
| Outdial Attempted Count | The number of times an agent attempted to make an outdial call. | Sum of Outdial Ringing Count |  |
| Not Responding Count | The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent. | Sum of Not Responded Count |  |
| Not Responding Total Time | The total amount of time agents spent in the Not Responding state. | Sum of Not Responded Duration |  |
| Avg Not Responding Time | The average time agents were in the Not Responding state. | Sum of Not Responded Duration / Sum of Not Responded Count |  |
| Consult Count | The number of times agents answered a consult request from another agent. | Sum of Consult Count |  |
| Consult Total Time | The total amount of time agents spent answering consult requests. | Sum of Consult Duration |  |
| Avg Consult Time | The average time agents spent answering consult requests. | Sum of Consult Answer Duration / Sum of Consult Answer Count |  |
| Consult Request Count | The number of consult requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. | Sum of Consult Request Count |  |
| Consult Request Total Time | The total amount of time agents spent consulting other agents. | Sum of Consult Request Duration |  |
| Avg Consult Request Time | The average time agents spent consulting other agents. | Sum of Consult Request Duration / Sum of Consult Request Count |  |
| Consult Answer Count | The sum of the number of times agents answered consult requests and the number of times agents consulted other agents. | Sum of Consult Answer Count |  |
| Total Consult Answer Time | The sum of the Total Consult Answer Time and Total Consult Request Time. | Sum of Consult Answer Duration |  |
| Conference Count | The number of times an agent initiated a conference call. | Sum of Conference Count |  |
| Inbound CTQ Request Count | The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. | Sum of CTQ Request Count |  |
| Inbound Total CTQ Request Time | The total amount of time agents spent answering consult-to-queue requests from an agent handling an inbound call. | Sum of CTQ Request Duration |  |
| Inbound CTQ Answer Count | The number of times agents answered a consult-to-queue request from another agent who was handling an inbound call. | Sum of CTQ Answer Count |  |
| Inbound Total CTQ Answer Time | The total amount of time agents spent answering consult-to-queue requests from an agent handling an inbound call. | Sum of CTQ Answer Duration |  |
| Outdial CTQ Request Count | The number of consult-to-queue requests initiated by an agent for outdial call type. This is an agent metric applicable for consulting agent. | Sum of Outdial CTQ Request Count |  |
| Outdial CTQ Total Request Time | Shows the total amount of time an agent spent on a consultation via a consult-to-queue initiated by this agent while handling an outdial call. | Sum of Outdial CTQ Request Duration |  |
| Outdial CTQ Answer Count | The number of times agents answered a consult-to-queue request from another agent who was handling an outdial call. | Sum of Outdial CTQ Answer Count |  |
| Outdial CTQ Total Answer Time | The total amount of time agents spent answering consult-to-queue requests from an agent handling an outdial call. | Sum of Outdial CTQ Answer Duration |  |
| Agent Transfer | The number of times an agent transferred inbound contacts to another agent after consult. | Sum of Agent To Agent Transfer Count |  |
| Agent Requeue | The number of times an agent requeued an inbound call. | Sum of Agent Transfer To Queue Request Count |  |
| Blind Transfer | The number of times an agent transferred an inbound call to either an external or third-party Dial Number (DN) through the Interactive Voice Response (IVR) without agent intervention. | Sum of Blind Transfer Count |  |
| Inbound Average Handle Time | The average length of time agents were in the Wrapup state after an inbound call. | (Sum of Connected Duration  + Sum of Wrapup Duration) / Sum of Connected count |  |
| Outdial Average Handle Time | The average length of time agents were in the Wrapup state after an outdial call. | (Sum of Outdial Connected Duration  + Sum of Outdial Wrapup Duration) / Sum of Outdial Connected Count |  |
| RONA Count | number of true RONA instances associated with this agent. |  | Reason code: RONA_TIMER_EXPIRED NO_ANSWER_USER Event name: not-responding consult-error transfer-error |
| Call reject Count | Count of calls rejected by this agent. |  | Reason code: USER_DECLINED Event name: con-to-agent-error consult-error transfer-error |
| Offer Error Count | Number of calls where the agent couldn't be connected, excluding RONA and Call Rejected cases. |  | Reason code not in : USER_DECLINED RONA_TIMER_EXPIRED NO_ANSWER_USER Event name: con-to-agent-error consult-error transfer-error agent-invite-error |
| Engaged Count | Shows the number of times the agent went into the Engaged state. | Sum of Engaged Count |  |
| Engaged Duration | Shows the total amount of time an agent was engaged. | Sum of Engaged Duration |  |
| Average Engaged Duration | Shows the average engaged duration. | Sum of Engaged Duration / Sum of Engaged Count |  |

| Parameter | Description |
|---|---|
| Queue Name | The name of the queue |
| Interaction ID | Call Session ID |
| Call Direction | The type of interaction the agent is handling, such as outbound or inbound. |
| Reason Code | The reason code indicates why the call entered this state, specifically identifying whether the call failed to deliver to the agent due to telephony issues (for example, incorrect agent number, INVALID NUMBER), system issues, or if RONA occurred because the agent was unavailable (for example, USER_BUSY or other reasons). This helps the user differentiate between telephony-related problems, system-related issues, and cases where the agent genuinely went to RONA. Here are the possible reason codes: INVALID_NUMBER: Agent's logged in DN is invalid USER_BUSY: Agent is busy USER_UNAVAILABLE: Agent's logged in DN is valid, but there are no devices online on that number. CHANNEL_FAILURE: A generic failure occurred, and the cause does not match any of the above reasons or existing auxiliary codes. NO_ANSWER_USER: No Answer from Agent RONA_TIMER_EXPIRED: The call rang on the agent's device, but the agent did not answer. USER_DECLINED: Agent declined/rejected the contact MEDIA_INTERNAL_ERROR: Media internal error |
| Event Name | AAR Event |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of an agent, that is, a person who answers customer calls. Used As : Row Segment |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As :
              Row Segment |  |
| Interval | Time period for which the agent activity is available. | Last 7 Days |
| Idle Code Name | Name of the code Used As : Column Segment |  |
| Count | The number of values specifying a condition for including records. | Count of Record Unique ID |
| Duration | The amount of time during which the agent was engaged in the activity. | Sum of Activity Duration |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of an agent, that is, a person who answers customer calls. Used As : Row Segment |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Interval | Time period | Last 7 Days |
| Wrapup Code Name | The name of the wrap-up code applied. Used As : Column Segment |  |
| Count | The number of values within the specified range. | Count of Contact Session ID |
| Duration | The number of seconds that the interaction was active. | Sum of Wrap-up Duration |

| Parameter | Toggle On Behaviour Description | Toggle Off Behaviour Description | Filters | Formula |
|---|---|---|---|---|
| Interval | The start time of the queue activity represented by the row. | Time Period |  | Last 7 Days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| Queue Name | The queue represented by the row. A contact can appear in more than one queue row
                if it entered multiple queues. | The last queue that the contact was in. Used As : Row Segment |  |  |
| Skills assigned in | Not shown in this version. | Indicates where skills are assigned. The following are the values: For the current Skill-Based Routing Team's queue, the value is 'Flow'. For the Skill-based queue, the value is ‘Queue’. For the Agent-based queue, the value is ‘NA’. |  |  |
| # Contacts | Not shown in this version. | The total number of contacts. |  | Count of Contact Session ID |
| Handled Contacts | The number of contacts handled in the queue represented by the row. | Not shown in this version. |  |  |
| Avg Queue Wait Time | The average time contacts waited in the queue represented by the row. | Average of total queue duration. | Current State: connected, ended | Average of Queue Duration |
| Longest Contact's Total Queue Duration | The longest time a contact waited in the queue represented by the row. Contacts
                currently in queue are not included. | The longest duration that a contact spent in queue. This is calculated after the
              call status changes from parked to connected or ended. Calls received in the last 7
              days are considered, excluding the calls that are currently in queue. | Current State: connected, ended | Maximum Queue Duration |
| # Abandoned Contacts | The number of contacts abandoned while waiting in the queue represented by the
                row. | Number of contacts that were abandoned. | Termination Type: abandoned | Count of Contact Session ID |

| Parameter | Description | Formula |
|---|---|---|
| Interval | The time period for which you generated the report. | Last 7 Days |
| Team Name | Name of the team. |  |
| Agent Name | Name of the agent. |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Total Log In Count | The total number of logins of the agent during the specified time interval. | Cardinality of Agent Session ID (Cardinality provides the total number of unique Agent Session IDs.) |
| Initial Login Time | The timestamp of the first login within the specified interval. | Minimum Login Timestamp |
| Final Logout Time | The timestamp of the last logout within the specified interval. | Maximum Logout Timestamp |
| Staff Hours | The total amount of time agents were logged in. | Sum of Realtime Update Timestamp - Sum of Login Timestamp |
| Idle Counts | The number of times that the agent's state changed to an idle state. | Sum of Idle Count |
| # Contacts Handled | The number of contacts that were handled in sessions that started during the specified interval. This includes contacts across all channel types. | Sum of Connected Count |
| # Calls Handled | The number of  Telephony channel type contacts that were handled. | Voice Connected Count |
| # Chats Handled | The number of Chat channel type contacts that were handled. | Chat Connected Count |
| # Emails Handled | The number of  Email channel type contacts that were handled. | Email Connected Count |
| # Social Handled | The number of  Social channel type contacts that were handled. | Social Connected Count + Social Outdial Connected Count |

| Name | Description |
|---|---|
| Date | Indicates the date and time of the incoming call. |
| Session ID | The unique ID associated with each incoming call. |
| Entry Point | The entry point where the call landed. |
| Site Name | The name of the site or location. |
| Queue Name | The name of the queue. |
| Handled | Indicates whether the call was handled, by means of a check mark. |
| Abandoned | Indicates whether the call was abandoned, by means of a check mark. |
| Rejected | Indicates whether the call was rejected, by means of a check mark. |
| Reason | The reason why the call was abandoned or rejected. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Voice | The media type of the telephony contact. |  | Count of Contact Session ID (Channel Type = telephony, Termination Type=normal) |
| Chat | The media type of the chat contact. |  | Count of Contact Session ID (Channel Type = chat, Termination Type=normal) |
| Email | The media type of the email contact. |  | Count of Contact Session ID (Channel Type = email, Termination Type=normal) |
| Contacts Handled | The total number of contacts handled. | Termination Type: normal | Count of Contact Session ID |

| Parameters | Description | Formula |
|---|---|---|
| Interval | Time period | Last 7 days |
| DNIS | DNIS number for an incoming call. DNIS does not appear for a Chat contact. | Row Segment |
| Channel Type | The media type of the contact. | Row Segment |
| Number of Contacts | Represents number of contacts. | Count of Contact Session ID |

| Parameters | Description | Filters | Formula |
|---|---|---|---|
| Interval | Time period |  | Last 7 days |
| Queue Name | The name of a queue, which is holding place for calls while they await handling by an agent. Calls move from an entry point into a queue and then gets distributed to agents. |  | Queue Name |
| Contact Reason | Reason identifier. |  | Contact Reason |
| Voice | The media type of the telephony contact. | Channel Type: Telephony | Count of Contact Session ID |
| Chat | The media type of the chat contact. | Channel Type: chat | Count of Contact Session ID |
| Email | The media type of the email contact. | Channel Type: email | Count of Contact Session ID |
| Social | The total number of social channel interactions handled. | Channel Type: social | Count of Contact Session ID |

| Parameter | Description | Formula |
|---|---|---|
| Voice | The media type of the telephony contact. | Count of Contact Session ID (Channel Type = telephony) |
| Chat | The media type of the chat contact. | Count of Contact Session ID (Channel Type = chat) |
| Email | The media type of the email contact. | Count of Contact Session ID (Channel Type = email) |

| Parameter | Description | Formula |
|---|---|---|
| ANI | The Automatic Number Identification (ANI) digits delivered with a call. ANI is a service provided by the phone company that delivers the caller’s phone number along with the call. | Value of ANI |
| DNIS | The Dialed Number Identification Service (DNIS) digits delivered with the call. DNIS is a service provided by the phone company that delivers a digit string indicating the number the caller dialed along with the call. | Value of DNIS |
| Queue | The name of a queue, which is holding place for calls while they await handling by an agent. Calls are moved from an entry point into a queue and are later distributed to agents. | Value of Final queue name |
| Site | The call center location to which a call was distributed. | Value of Site name |
| Skill Requirement | The required skill of an agent, for the call session. The column shows multiple skills mapped to the corresponding skill profile, in a comma-separated single string in the following format: skill_name1=skill_value1, skill_name2=skill_value2 | Value of Required Skills |
| Team | A group of agents at a specific site who handle a particular type of call. | Value of Team name |
| Agent | The name of an agent, that is, a person who answers customer calls/chats/emails | Value of Agent name |
| Call start time | Timestamp when the contact started. | Value of Contact start timestamp |
| Call end time | Timestamp when the contact ended. | Value of Contact end timestamp |
| Call Duration | The connected duration of a call from. | Value of Call end time – call start time |
| IVR time | The amount of time during which a call was in IVR state. | Value of IVR duration |
| Queue Time | The amount of time a contact spent in queue waiting. | Value of Queue duration |
| Connected time | The duration of connected (talking) state within this interaction. | Value of Connected duration |
| Hold time | The amount of time during which a call was placed on hold. | Value of Hold duration |
| Wrap up time | The cumulative amount of time agents spent in the wrap-up state after handling the interactions. | Value of Wrap up duration |
| Handle time | The total amount of time an agent handles the call including wrap-up time. | Wrap up time  + connected time |
| Consult time | The amount of time an agent spent consulting with another agent while handling a call. | Value of Consult duration |
| Conference time | The amount of time an agent spent in conference with a caller and another agent. | Value of Conference duration |
| CTQ request time | Total duration spent on consult-to queue within an interaction. | Value of CTQ duration |
| Hold count | The number of times an agent put an inbound caller on hold. | Value of Hold count |
| Consult count | The number of times agents initiated a consult with another agent or someone at an external number while handling a call. | Value of Consult count |
| Conference count | The number of times an agent established a conference call with the caller and another agent. | Value of Conference count |
| Blind transfer count | The number of times a call was transferred via blind transfer in the following scenarios: Agent transferred the call to another agent without consulting first. Agent transferred the call to another queue without consulting first. Agent transferred the call to an external Dial Number (DN) without consulting first. Call transferred to an End Point (EP) through the flow without agent intervention. | Value of Blind transfer count |
| CTQ request count | The number of consult-to-queue requests initiated by an agent for inbound call type. This is an agent metric applicable for consulting agent. | Value of CTQ count |
| Number of transfers | Indicates the number of times a call was transferred: By an agent to another agent Through the Flow To a Queue To a DN or EP To an EP through GoTo activity | Value of Transfer count |
| Transfer errors | Indicates the number of times the transfer failed. | Value of Transfer error count |
| Handle type | Indicates how the call was handled, short, abandoned, normal. | Value of Handle type |
| Call Direction | Indicates if the call is an inbound call or an outbound call. Click the Call Direction table cell to see the Drill Down icon. Click the icon to launch the Drill Down modal dialog. You can see the following parameters: Termination Reason —Specifies the reason, why the call was terminated. For example, the Customer left the call. Termination Party —Specifies, who terminated the call or where the call was terminated. For example, if the call was terminated by the agent or the customer, if the call was terminated in the system or queue. | Value of Call Direction |
| Termination type | A text string specifying how a call was terminated. | Value of Termination type |
| Record flag | Flag that indicates whether the contact was recorded. | Value of Is recorded |
| Wrap up | The wrap-up code that the agent gave for the interaction. | Value of Wrap up code name |
| Session ID | A unique string that identifies the contact session. | Value of Contact session ID |
| Evaluation Score Type* | If the interaction is evaluated by AI, or supervisor overided the
                            evaluation score or if the interaction is not evaluated. Possible value:
                            Manual, Auto, N/A. | Value of Evaluation Score Type |
| Evaluation Score (in %)* | Evaluation score between 0 and 100 in integer. | Sum of Overall Evaluation Score+ Outdial Overall Evaluation
                            Score. |
| Evaluation Sections Failure Count* | Number of “Auto Fail” defined sections that failed in evaluation. If
                            an interaction is evaluated on more than 1 evaluation forms, it sums up
                            failed sections across all evaluations. Value will be >= 0
                            (Integer). | Value of Evaluation Sections Failure Count |
| Customer Sentiment Score* | Customer sentiment score of interactions between -100 and +100
                                (Integer) Conditional formatting: > >+ 45 is
                            positive sentiment (Green); Anything <-45(Any value below -45) is
                            negative sentiment (Red). | Value of Customer Sentiment Score |
| Talkover Time* | Duration for which agent spoke over customer HH:MM:SS. | Value of Talk Over Time |
| Word Ratio Score* | Number of words spoken by agent over total number of transcript words
                            in interaction (%). | Value of Word Ratio Score |
| Dead Air Time* | Duration for which neither customer nor agent spoke in
                            HH:MM:SS. | Value of Dead Air Time |
| Auto CSAT* | Integer between 1 and 5. It is calculated by AI and represents
                            overall satisfaction level of customer. | Value of Auto CSAT |

| Parameter | Description | Formula |
|---|---|---|
| Voice | The media type of the telephony contact. | Count of Contact Session ID (Channel Type = telephony) |
| Chat | The media type of the chat contact. | Count of Contact Session ID (Channel Type = chat) |
| Email | The media type of the email contact. | Count of Contact Session ID (Channel Type = email) |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Voice | The media type of the telephony contact. | Termination Type: abandoned Channel Type: telephony | Count of Contact Session ID |
| Chat | The media type of the chat contact. | Termination Type: abandoned Channel Type: chat | Count of Contact Session ID |
| Email | The media type of the email contact. | Termination Type: abandoned Channel Type: email | Count of Contact Session ID |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Queue Name | The name of a queue. Used As : Row Segment | Final Queue ID = Is not in 0 |  |
| Interval | Time period |  | Last 7 days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment | Final Queue ID = Is not in 0 |  |
| Completed | The number of calls that ended during the report interval. Answered, abandoned, and disconnected calls are included in this count. Transferred and short calls are not. |  | Count of Contact Session ID (Termination Type = normal) + Count of Contact Session ID (Handle type = Abandoned) + Count of Contact Session ID (Termination Type = quick_disconnect) |
| %Abandoned | The percentage of calls that were abandoned |  | Count of Contact Session ID (Handle type = Abandoned) / Sum of Contact Count |
| Abandoned | The number of calls that were abandoned during the report interval. An abandoned call is a call that was terminated without being distributed to a destination site, but that was in the system for longer than the time specified by the Short Call threshold provisioned for the enterprise. | Termination Type: abandoned | Count of Contact Session ID |
| Avg Queued Time | The cumulative amount of time calls were in queue, waiting to be sent to an agent or other resource. Because queued time is calculated after the call leaves the queue, the queued time for a call that is still in the queue is not reflected in the report. |  | Sum of Queue Duration / Sum of Queue Count |
| Avg Abandoned Time | The cumulative amount of time calls were in the system for longer than the time specified by the Short Call threshold, but terminated before being distributed to an agent or other resource. |  | Sum of Queue Duration (Is Contact Handled = 1) / Count of contact session ID (Termination Type = abandoned) |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Queue Name | Name of queue Used As : Row Segment |  |  |
| Interval | Time period |  | Last 7 days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| Service Level % | The number of calls that were answered within the Service Level threshold provisioned for the queue or skill (including abandoned calls). |  | Service Level % = Sum of Is Within Service Level / Total. |
| Entry Point Call Total | The total number of calls from contacts that landed to the Webex Contact Center system through all the entry points for the selected duration. |  | Sum of Contact Count |
| Completed | The number of calls that ended during the report interval. Answered, abandoned, and disconnected calls are included in this count. Transferred and short calls are not. |  | Count of Contact Session ID (Termination Type = normal) + Count of Contact Session ID (Termination Type = abandoned) + Sum of Contact count (Termination Type = quick_disconnect) |
| Abandoned | The number of calls that were abandoned during the report interval. An abandoned call is a call that was terminated without being distributed to a destination site, but that was in the system for longer than the time specified by the Short Call threshold provisioned for the enterprise. | Termination Type: abandoned | Count of Contact Session ID |
| Answered | The number of calls that were routed from the queue to an agent or available resource and were answered by the agent or resource. | Connected Duration: > 0 | Count of Contact Session ID |
| Conference Count | The number of times agents initiated a conference call to an agent or external number. |  | Sum of Conference Count |
| Hold Count | The number of times a caller was put on hold. |  | Sum of Hold Count |
| Avg Abandoned Time | The cumulative amount of time calls were in the system for longer than the time specified by the Short Call threshold, but terminated before being distributed to an agent or other resource. |  | Sum of Queue Duration (Is Contact Handled != 1) / Count of Contact Session ID (Termination Type = Abandoned) |
| Avg Speed of Answer | The total answered time divided by the total number of answered calls. |  | (Queue Duration + Ringing duration) / Answered |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Team Name | The name of a team. Used As : Row Segment |  |  |
| Interval | Time period |  | Last 7 days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| Completed | The number of calls that ended during the report interval. Answered, abandoned, and disconnected calls are included in this count. Transferred and short calls are not. |  | Count of Contact Session ID (Termination Type = normal) + Count of Contact Session ID (Termination Type = abandoned) + Sum of Contact Count (Termination Type = sudden_disconnect) |
| Sudden Disconnect Count | The number of calls that were answered (that is, connected to an agent or distributed to and accepted by a destination site), but that were then immediately disconnected within the Sudden Disconnect threshold provisioned for the enterprise. | Termination Type: sudden_disconnect | Sum of Contact Count |
| Answered | The number of calls that were routed from the queue to an agent or available resource and were answered by the agent or resource. | Termination Type: normal | Count of Contact Session ID |
| Conference Count | The number of times agents initiated a conference call to an agent or external number. |  | Sum of Conference Count |
| Hold Count | The number of times a caller was put on hold. |  | Sum of Hold Count |
| Answered Time | The cumulative amount of time between when calls entered the queue and when they were answered (connected to an agent or other resource) during the report interval. Because answered time is calculated after the call is answered, answered time for calls that are waiting to be answered is not reflected in the report. | Is Contact Handled: = 1 | Sum of Queue Duration |
| Connected Time | The time interval between when calls were answered by an agent or other resource and when they were terminated. Because connected time is not calculated until the call is terminated, the connected time for a call that is still in progress is not reflected in the report. |  | Sum of Hold Duration + Sum of Connected Duration |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Interval | Time period |  | Last 7 days |
| Channel Type | The media type of the contact, such as telephony, email, or chat. |  | Channel Type |
| Offered | The total number of contacts offered. |  | Sum of Is Offered |
| Handled | The total number of interactions handled. | Termination Type: normal | Count of Contact Session ID |
| Avg Handle Time | The average length of time spent handling a call. |  | (Sum of Connected Duration  + Sum of Hold Duration + Sum of Wrapup Duration) /Count of Contact Session ID |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Offered | The total number of contacts offered. |  | Sum of Is Offered |
| Handled | The total number of interactions handled. | Termination Type: normal | Count of Contact Session ID |

| Column Name | Description |
|---|---|
| Contact Session ID | A unique string that identifies the contact session and can be found in
              Analyzer. |
| Customer Phone Number | Phone number of the customer. |
| Entrypoint Name | Name of the EP, which is the landing place for customer calls on the Webex
              Contact Center system. One or more toll-free or dial numbers can be associated with a
              given EP. IVR call treatment is performed while a call is in the EP. Calls are moved
              from the EP into a queue and are then distributed to agents. |
| Queue | The contact center queue that handled the call. |
| Agent | Shows the name of the agent. |
| Agent Endpoint (DN) | The dial number that the agent used to log in to the Agent Desktop. |
| Call Duration | The connected duration of a call from. |
| Hold Duration | The hold duration of a call. |
| Number of Transfers | The number of times the calls were transferred. |
| Wrapup Code | The wrap-up code applied. |
| Terminated By | Indicates the party that terminated the interaction. The terminating party can be
                one of the following: Agent—The agent terminated the callback. Contact—The contact terminated the callback. System—The callback was terminated due to a system error. |
| Termination Type | A text string specifying how a call was terminated. |
| Abandoned Type | The Abandoned Type is set when the call is abandoned. The following values show
                    the states of the call when abandoned. null: The customer was connected with an agent. new: The customer disconnected immediately after entering the flow, before
                  reaching any queue. queue: The customer disconnected while waiting in the queue for an agent. treatment: The customer disconnected during self-service options, such as IVR,
                  message playback, or music, before entering a queue. agent-connect: The customer hung up before an agent was connected to the
                  customer (during the ringing or connecting phase). Checks the previous event before the ended event and sets the value accordingly.
                For instance, if the previous event before the ended event is parked, the Abandoned
                Type is set to 'queue'. |
| Abandonment Reason | Reason for the call abandonment. The abandonment reason can be one of the
                following: Agent Left: The agent ended the call. Customer Left: The customer ended the call. Queue Timeout: The call ended because it was queued for longer than the
                  configured timeout in a queue. System Error: The call ended because of system errors. Agent Disconnected: The call ended because the agent was disconnected from the
                  call. Blind Transfer Failed: The inbound call ended because the call contact transfer
                  to either an external or third-party Dial Number (DN) through the Interactive
                  Voice Response (IVR) without agent intervention failed. RONA Timer Expired: The outbound call ended because the agent was unable to
                  answer the call. Interaction Cleanup: The contact was cleaned up for serviceability or
                  troubleshooting purpose. |
| Auto CSAT | Predicted automatic customer satisfaction score |
| Call Start Time | Timestamp when the contact started. |
| Call End Time | Timestamp when the contact ended. |

| Column Name | Description |
|---|---|
| Interaction ID | The shared identifier for the end-to-end call. Click to drill down into
              Calling-side records. |
| Correlation ID | The Correlation ID to tie together multiple call legs of the same call
              session. |
| Start Time | The timestamp indicating when the specific calling leg or CDR segment
              began. |
| Answer Time | When this call was answered. |
| Release Time | When this call was released. |
| Location | The Webex Calling location associated with the called or calling party (for
              example, office site or region). |
| Calling Number | The phone number or extension from which the call was placed on the Webex Calling
              side. |
| Called Number | The phone number or extension that was dialed on the Webex Calling side. |
| Caller ID | The display name associated with the calling party as resolved by the Webex
              Calling directory. |
| Duration | Indicates the duration of this call log in seconds. |
| Direction | Indicates whether the call log was Inbound or Outbound from the Webex Calling
              perspective. |
| Client type | The client technology used, such as WXCC, SIP, or TEAMS_WXC_CLIENT. |
| User Name | The display name of the user or service (for example, Louis Richet, Service
              Support). |
| Call outcome | The result of the call log, such as Success or Refusal. |
| Call outcome reason | The specific reason for the outcome, such as Normal or
              TemporarilyUnavailable. |
| Call transfer time | The timestamp at which the call transfer event was initiated on the Webex Calling
              side. |
| Local call ID | The unique call identifier assigned by the local Webex Calling node or endpoint
              for this specific call log. |
| Remote call ID | The unique call identifier assigned by the remote Webex Calling node or endpoint
              involved in the same call log. |
| Transfer related call ID | The identifier linking this CDR segment to a related transfer event, used to
              reconstruct the full call chain. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Interval | The time period for which the Self-service analytics data is reported. |  |  |
| Entrypoint Name | The list of entry points for the IVR call. |  |  |
| Total IVR Calls | The total number of IVR calls handled by the virtual agent. |  |  |
| Calls Abandoned in Self-Service | Number of IVR calls that were abandoned in IVR. |  |  |
| Calls Escalated to Queue | Number of IVR calls that were escalated to a queue. |  |  |
| Percentage Escalation to Queue | Percentage of IVR calls that were escalated to a queue. |  | 100 * (Calls Escalated to Queue / Total IVR Calls) |

| Parameter | Description |
|---|---|
| Name of Activity | Shows the name of the activity such as CVA, Play Prompt, Menu, and Queue. |
| Number of Calls completed in this Activity | Shows the total number of calls completed in this activity. |

| Parameter | Description |
|---|---|
| Entrypoint Name | Shows the entry point for that particular activity. |
| Timestamp | Shows the date and the time at which the call landed in the
                                Self-service. |
| Call ID | Shows the call ID number. |
| Sequence of Activity | Shows the sequence of activities that were involved in the call. The activities include DTMF, Prompt Name, Queue Name, Abandoned, Completed, CVA, Menu, Self Service Complete, and Self Service Abandon. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Date | Displays the date. |  |  |
| Queue Name | The queue that the contact was in at the time of opting out. |  |  |
| Number of Opt-outs | The number of customer contacts that opted out of a particular queue on the given date. |  |  |

| Parameter | Description | Formula |
|---|---|---|
| Call Time | Shows the time at which the call got connected. |  |
| ANI | Shows the ANI number that is associated with the call. |  |
| DNIS | Shows the DNIS number that is associated with the call. |  |
| Workflow Sequence | Shows the sequence of activities that happened during the call. |  |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Interval | The time period for which the Webex Experience Management Post Call
                                Survey data is reported. |  |  |
| Total Calls | The total number of voice calls for which the Post Call Survey was
                                offered to the customer during the interval |  |  |
| Survey Opt-in Number | The number of customers who opted for the inline survey. If there an error while gathering caller's opt-in preference then
                                    it is not considered as part of the Survey Opt-in Number
                                    calculation. |  |  |
| Survey Opt-in Stats | The percentage of customers who opted for the inline survey. |  | (Survey Opt-In Number / Total Contact with Survey) X 100 |
| Survey Response Rate | The percentage of voice calls for which the Post Call Survey response
                                was received. This is calculated as a percentage of the Survey
                                Opt-in number. |  |  |
| Survey Completion Rate | The percentage of questions answered by the customers. This is
                                calculated as a percentage of the total number of questions posted
                                to the customers. |  |  |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Interval | The time period for which the Cisco Webex Experience Management Post
                                Call Survey data is reported. |  |  |
| Type of Survey | The type of survey that the customers have opted for (Inline survey
                                or Deferred survey). |  |  |
| Total Contacts with Survey | Total number of customers who were offered the specific type of
                                survey (Inline survey and Deferred survey). |  |  |
| Survey Opt-in Number | Total number of customers who opted in for each type of survey
                                (Inline survey and Deferred survey). If there an error while gathering caller's opt-in preference then
                                    it is not considered as part of the Survey Opt-in Number
                                    calculation. |  |  |
| Survey Opt-in Stats | The percentage of customers who opted in for the survey (Inline
                                survey and Deferred survey). |  | (Survey Opt-in Number / Total Contacts with Survey) x 100 |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Interval | Shows the duration for which the team statistics is collected. |  | Last 7 Days |
| Team Name | Shows the name of the team. |  |  |
| Agent Name | Shows the name of the agent. |  |  |
| # Contacts Handled | Shows the number of contacts that were handled by the agent. |  |  |
| Total Contacts Handled | Shows the total number of contacts that were handled by the agent for
                                the call channel type. |  | Sum of Inbound Contacts Handled + Outdials Handled |
| Inbound Contacts Handled | Shows the total number of inbound contacts that were handled by the
                                agent for the call channel type. |  |  |
| Callbacks Handled | Shows the number of callbacks that were handled by the agent for the
                                call channel type. |  |  |
| Outdials Handled | Shows the total number of outdial calls that were handled by the
                                agent for the call channel type. |  |  |
| Average Handle Time | Shows the average time that was spent by the agent on the contacts
                                handled. |  | Sum of Wrapup Duration  + Sum of Connected Duration / # Contacts Handled |
| Average Wrapup Time | Shows the average time that was spent on wrapping up the contacts
                                handled. |  | Sum of Wrapup Duration / Sum of Wrapup Count |

| Parameter | Description |
|---|---|
| Date Time (in UTC) | The date and time on which the survey was started. This is in the UTC time zone. |
| Contact Session ID | A unique string that identifies the contact session and can be found in Analyzer. |
| Survey Type | The name of the survey |
| Question Text | The text given to the question when the survey is created. |
| Response | The value provided by the end-user of the survey. |
| First Agent name | The name of the agent who first answered the call. |
| First Agent email | The email address of the agent who first answered the call. |
| Last Agent Name | The name of the agent who handled the call. |
| Last Agent email | The email address of the agent who handled the call. |
| Queue Name | The queue name of the first agent who answered the call. |
| Site Name | The site name of the agent who answered the call. |
| Call Duration (In seconds) | The time elapsed between the call start time and the call end time. |
| Agent DNIS | The DNIS number that is associated with the last agent. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Queue Name | The name of the last queue that was associated with the callback. |  |  |
| Type of Callback | The type of the callback. The callback type can be courtesy, scheduled, scheduled_personal, or web. |  |  |
| Source of Callback | The source of the callback. The source of a callback can be web, chat, livecall, api or IVR. |  |  |
| Callback Request Time | The time at which the customer opted for the callback. |  |  |
| Callback Connected Time | The time at which the callback was connected between the agent and the customer. |  |  |
| Callback Number | The number that is based on the ANI or the number that was configured in a workflow. |  |  |
| Preferred Agent Name | The name of the preferred agent who made the callback to the contact in queue. This column displays a N/A value if the contact is not queued to the preferred agent through Queue to Agent activity in Flow Designer. For more information, see the Queue To Agent activity documentation. If the preferred agent is unable to make a callback, the Agent Name column displays a N/A value. |  |  |
| Agent Name | The name of the agent making the callback. |  |  |
| Team Name | The name of the team that the agent belongs to. |  |  |
| Last Callback Status | The status of the last callback. Callback Status Success: When a Callback call was connected. Not Processed: When an agent receives the Callback request but is pending processing. Failure: When a Callback was attempted, but the connection was not established. |  |  |
| Final Reason | Indicates the reason for ending the callback. The reason can be one of the following: NO_ANSWER_FROM_CUSTOMER —The callback was not answered when the customer received it on their device. CUSTOMER_BUSY —The customer device was busy when the callback was attempted. CUSTOMER_UNAVAILABLE —The customer's device was unavailable when the callback was attempted. Customer Left —The customer ended the call. NO_ANSWER_FROM_AGENT —The callback was not answered when the agent received it on their device. AGENT_ENDS —Agent ended the callback contact before it could be established with the customer. Agent Left —The agent ended the call. RONA Timer expired —The Ring-No-Answer (RONA) timer expired before the callback contact could be answered. Queue Timeout —The configured queue timeout expired for the parked callback contact before it could be routed to an an eligible and available agent in that queue. MAX_CALLBACK_RETRY_LIMIT_REACHED —The configured maximum retries for the callback contact was reached. OUTDIAL_FAILED —There was a failure to dial out the callback contact to the customer. Unsupported flow activity —The contace was terminated due to the execution of an unsupported flow activity. Queue Timeout —The contact timed out while waiting in the queue. Participant Invite Timer expired —The contact was terminated due to a timeout in media signaling to invite a participant into the call. SYSTEM_ERROR —The contact was terminated due to an unknown system error. |  |  |
| Terminated by | Indicates the party that terminated the interaction. The terminating party can be one of the following: Agent —The agent terminated the callback. Contact —The contact terminated the callback. System —The callback was terminated due to a system error. |  |  |
| Failed Callback Retry Count | The number of times a callback retry failed. |  |  |

| Parameter | Description |
|---|---|
| Callback ID | Shows a unique string that identifies the callback session. |
| Callback Time | Shows the time at which the callback was requested. |
| Reason | Indicated the reason for ending the selected callback session. The reason can be one of the following: Agent Left —The agent ended the call. Customer Busy —The contact's dialled line is busy. System Errors —The call ends due to system errors. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Campaign Name | The name of the campaign. | — | — |
| Interval | Time period. | — | — |
| Queue Name | The name of the queue. | — | — |
| Team Name | The name of the team to which the agent belongs. | — | — |
| Agent Name | The name of the agent who is associated with the call. | — | — |
| Contacts | The number of calls made by the agent as part of the campaign. | — | Count of Contact Session ID |
| Average Handle Time | Shows the average time that was spent by the agent on the contacts handled. | — | Average Talk Time  + Average of Wrapup Duration |
| Average Talk Time | Average time that an agent spent in a call. | — | Average Talk Time + Average of Connected Duration |

| Parameter | Description |
|---|---|
| Contact | The phone number to which an agent will make calls during a promotional campaign. |
| Campaign Name | The name of the campaign. |
| Agent CID | Agent's Calling ID, indicating the Agent's Calling number. |
| Call Start time | Timestamp when the contact started. |
| Call End time | Timestamp when the contact ended. |
| Talk Time | Elapsed time between the time an agent connected to the call and the time the call was disconnected or transferred, not including the hold time. |
| Hold Time | Total amount of time that an agent put the calls on hold. |
| Wrap Up Time | The cumulative amount of time agents spent in the wrap-up state after handling the interactions. |
| Wrap Up Code | The name of the wrap-up code that was applied. |
| Termination Code | The name of the termination code that was applied. |
| Is Consult | The Consult status is marked as checked when the call is identified as a consult call. |
| Is Transfer | The Transfer status is marked as checked when the call is identified as a transfer call. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Campaign Name | The name of the campaign. | — | — |
| Outdial Entrypoint | The name of the Entrypoint. | — | — |
| Campaign Type | The type of campaign. | — | — |
| Interval | Time period | — | — |
| Queue Name | The name of the queue. | — | — |
| Team Name | The name of the team to which the agent belongs. | — | — |
| Agent Name | The name of the agent who is associated with the call. | — | — |
| Contacts | The number of calls made by the agent as part of the campaign. | — | Count of Contact Session ID |
| Average Handle Time | Shows the average time that was spent by the agent on the contacts handled. | — | Average Talk Time  + Average of Wrapup Duration |
| Average Talk Time | Average time that an agent spent in a call. | — | Average Talk Time + Average of Connected Duration |

| Parameter | Description |
|---|---|
| Agent Login Time | Refers to the specific timestamp indicating the login time of an agent. |
| Agent Name | The name of the agent who is associated with the call. |
| Team Name | The name of the team to which the agent belongs. |
| Campaign Reserved Time | The total time reserved for an agent during the course of the campaign. If an agent is engaged in multiple campaigns simultaneously, the reservation time is combined. If an agent logs in twice, the system will create two distinct rows for that agent. |

| Parameter | Description |
|---|---|
| Contact | The phone number to which an agent will make calls during a promotional campaign. |
| Agent CID | Agent's Calling ID, indicating the Agent's Calling number. |
| CPA Status | Call Progress Analysis (CPA) monitors and reports on various call progress scenarios, indicating successful connections or failures. Descriptions for different CPA status are outlined below: NO_ANSWER_CUSTOMER —The call remains unanswered within the specified No Answer Ring Limit designated for the campaign. CUSTOMER_BUSY —The customer's line is busy or the call is declined by the customer. CUSTOMER_UNAVAILABLE —Network timeout or error potentially transient in nature. INVALID_NUMBER —The dialed number is invalid. CUSTOMER_LEFT —The customer answers the call but ends it immediately from their device or before CPA completion. ABANDONED —The call is abandoned due to a lack of available agents or resources. AMD —The call is answered by an answering machine or routed to voicemail. FAX —A fax machine is detected on the line. SYSTEM_ABANDONED —The call is abandoned due to an error condition within the system. |
| Call Start time | Timestamp when the contact started. |
| Call End time | Timestamp when the contact ended. |
| Talk Time | Elapsed time between the time an agent connected to the call and the time the call was disconnected or transferred, not including the hold time. |
| Hold Time | Total amount of time that an agent put the calls on hold. |
| Wrap Up Time | The cumulative amount of time agents spent in the wrap-up state after handling the interactions. |
| Wrap Up Code | The name of the wrap-up code that was applied. |
| Termination Code | The name of the termination code that was applied. |
| Is Consult | The Consult status is marked as checked when the call is identified as a consult call. |
| Is Transfer | The Transfer status is marked as checked when the call is identified as a transfer call. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Campaign Name | The name of the campaign. | — | — |
| Outdial Entrypoint | The name of the Entrypoint. | — | — |
| Campaign Type | The type of campaign. | — | — |
| Team Name | The name of the team to which the agent belongs. | — | — |
| Agent Name | The name of the agent who is associated with the call. | — | — |
| Queue Name | The name of the queue. | — | — |
| Contact | The phone number to which an agent will make calls during a promotional campaign. | — | Value of Customer Phone Number |
| Call Start time | Timestamp of when the contact started. | — | Value of Contact Start Timestamp |
| Total Connected Time | The total duration that a customer is connected with an agent. | — | Current Timestamp - Call Start Time |

| Parameter | Description | Filters | Drill-down Filter | Formula |
|---|---|---|---|---|
| Queue Name | The name of the queue. Used As : Row Segment | — |  | — |
| Interval | Time Period Used As : Row Segment | — |  | Last seven days |
| Service Level (in seconds) | Value that was configured in the Service Level field when the Queue was set up. If the service level configuration was changed during the report period, the report shows the values for both old and new service level configurations. Used As : Row Segment | — |  | — |
| Calls Handled < Service Level | The total number of calls that are handled within the service level threshold that was set for the queue. | Is Within service Level = 1 Handle Type is normal or sudden_disconnect . |  |  |
| Calls Abandoned < Service Level | The total number of calls that are abandoned within the service level threshold that was set for the queue. | Is Within service Level = 1 Handle Type is abandoned . |  | Count of Contact Session ID |
| Calls Presented | Number of calls that were routed to the queue, regardless of whether an agent answered the call. | — |  | Queue Count + CTQ Count + Outdial CTQ Count |
| Calls Handled | Number of calls that were routed to the Queue and were handled. | Handle Type is normal or sudden_disconnect . |  | Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count) |
| Agent to DN Transfer Count | Number of times a call was transferred from an agent to a DN. | — |  | Sum of Agent to DN Transfer Count |
| Agent Transferred In Count | The number of times call came after being transferred by an agent. (Blind transfers are not counted) Blind transfer scenarios inlcude the following: transfer to different queue transfer to EP transfer to agent transfer to the same queue transfer to DN | — |  | Sum of Agent Transferred In Count |
| Blind Transfer Count | This count is incremented when an agent initiates a blind transfer call to a Queue or an EntryPoint. | — |  | Sum of Inter Queue Blind Transfer Count |
| Calls Handled % | Percentage of calls that were routed to the Queue and were handled. | — |  | (Calls Handled / Calls Presented) x 100 |
| Calls Abandoned | Count of calls that got abandoned in a queue. | Handle Type is abandoned . |  | Count of Contact Session ID |
| Calls Abandoned % | Percentage of calls that were routed to the Queue and were abandoned. | — |  | (Number of calls abandoned / Number of calls presented) x 100 |
| Calls Moved Out of Queue | Number of calls that were moved out of Queue without being handled. | Handle Type is dequeued . |  | Count of Contact Session ID |
| Calls Moved Out of Queue % | Percentage of calls that moved out of Queue. | — |  | (Number of calls that moved out of Queue / Number of calls presented) x 100 |
| Calls Transferred to DN | Number of calls that were transferred to a dial number (DN) by blind transfer node via flow. If you want the calls transferred to DN count to be incremented, contact Cisco Support as the corresponding feature flag may have to be enabled. | Handle type is TransferToDN . |  | Count of Contact Session ID |
| Calls Transferred to DN % | Percentage of calls that were transferred to a dial number (DN) by blind transfer node via flow. | — |  | (Calls Transferred to DN / Calls Presented) x 100 |
| Consult to Queue Failed Count | Count of consult requests failed at queue. | — |  | CTQ Error Count + Outdial CTQ Error Count |
| Consult to Entry Point Failed Count | Count of consult requests failed at Entry Point. | — |  | Sum of Consult To EP Error Count |
| RONA Count | Number of contacts that transitioned to RONA in this queue |  | Reason code: RONA_TIMER_EXPIRED NO_ANSWER_USER Event Name: con-to-agent-error consult-error transfer-error |  |
| Call reject Count | Count of contacts rejected by agents in this queue |  | Reason code: USER_DECLINED Event name: con-to-agent-error consult-error transfer-error agent-invite-error |  |
| Offer Error Count | Count of contacts with Offer errors in this Queue |  | Reason code not in : USER_DECLINED RONA_TIMER_EXPIRED NO_ANSWER_USER Event name: con-to-agent-error consult-error transfer-error agent-invite-error |  |

| Parameter | Description |
|---|---|
| Queue Name | The name of the queue |
| Interaction ID | Call Session ID |
| Agent Name | Displays agent team to which the agent is logged in. |
| DNIS Number | Agent DN |
| Call Direction | The type of interaction the agent is handling, such as outbound or inbound. |
| Reason Code | The reason code indicates why the call entered this state, specifically identifying whether the call failed to deliver to the agent due to telephony issues (for example, incorrect agent number, INVALID NUMBER), system issues, or if RONA occurred because the agent was unavailable (for example, USER_BUSY or other reasons). This helps the user differentiate between telephony-related problems, system-related issues, and cases where the agent genuinely went to RONA. Here are the possible reason codes: INVALID_NUMBER: Agent's logged in DN is invalid USER_BUSY: Agent is busy USER_UNAVAILABLE: Agent's logged in DN is valid, but there are no devices online on that number. CHANNEL_FAILURE: A generic failure occurred, and the cause does not match any of the above reasons or existing auxiliary codes. NO_ANSWER_USER: No Answer from Agent RONA_TIMER_EXPIRED: The call rang on the agent's device, but the agent did not answer. USER_DECLINED: Agent declined/rejected the contact MEDIA_INTERNAL_ERROR: Media internal error |
| Event Name | CAR Event |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Queue Name | The name of the queue. Used As : Row Segment | — | — |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment | — | — |
| Service Level Configured (in seconds) | Value that was configured in the Service Level field when the Queue was set up. If the service level configuration was changed during the report period, the report shows the values for both old and new service level configurations. Used As : Row Segment | — | — |
| Calls Presented | Number of calls that were routed to the queue, regardless of whether an agent answered the call. | — | Queue Count + CTQ Count + Outdial CTQ Count |
| Calls Handled | Number of calls that were routed to the Queue and were handled. | Handle Type is normal or sudden_disonnect . | Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count) |
| Agent to DN Transfer Count | Number of times a call was transferred from an agent to a DN. | — | Sum of Agent to DN Transfer Count |
| Agent Transferred In Count | The number of times call came after being transferred by an agent. (Blind transfers are not counted) Blind transfer scenarios inlcude the following: transfer to different queue transfer to EP transfer to agent transfer to the same queue transfer to DN | — | Sum of Agent Transferred In Count |
| Blind Transfer Count | This count is incremented when an agent initiates a blind transfer call to a Queue or an EntryPoint. | — | Sum of Inter Queue Blind Transfer Count |
| Percentage Handled | Percentage of calls that were routed to the Queue and were handled. | — | (Calls Handled + Agent to DN Transfer Count) / (Calls Presented + Agent Transferred In Count + Blind Transfer Count - Agent To Queue Transfer Count) x 100 |
| Average Handled Time | Average time taken for calls to be handled in the queue. | — | Average of Handle Time Total Handle Time / Calls Handled |
| Maximum Handled Time | The longest duration taken to handle any call within the queue. | — | Maximum Handle Time maximum (talkTime + holdTime + workTime) |
| Calls Abandoned | Count of calls that got abandoned in a queue. | Handle Type is abandoned . | Count of Contact Session ID |
| Percentage Abandoned | Percentage of calls that were routed to the Queue and were abandoned. | — | (Number of calls abandoned / Number of calls presented) x 100 |
| Average Abandoned Time | Average time that the calls spent in the queue before being abandoned. | Handle Type is abandoned . | Average of Queue Duration |
| Maximum Abandoned Time | Maximum time a call spent in the queue before being abandoned. | Handle Type is abandoned . | Maximum Queue Duration |
| Calls Moved Out of Queue | Number of calls that moved out of Queue. (calls transferred out before answering) | Handle Type is dequeued . | Count of Contact Session ID |
| Percentage Calls Moved Out of Queue | Percentage of calls that moved out of Queue. (calls transferred out before answering) | — | (Number of calls that moved out of Queue / Number of calls presented) x 100 |
| Average Calls Moved Out of Queue Time | Average time that the call spent in Queue before being moved out. | Handle Type is dequeued . | Average of Queue Duration |
| Maximum Calls Moved Out of Queue Time | Maximum time a call spent in Queue before being moved out. | Handle Type is dequeued . | Maximum Queue Duration |
| Average Speed of Answer | Sum of average Queue waiting time before an agent answers the call and average ringing time. | Handle Type is one of the following: normal sudden_disonnect dequeued | Average queue waiting time + Average ringing time |
| Calls Handled < Service Level | Calls that are handled within the time shown in the Service Level field. A call is handled when an agent picks up the call. | Is Within service Level = 1 Handle Type is normal or sudden_disonnect . | Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count) |
| Calls Abandoned < Service Level | A call is abandoned if the call disconnects before connecting to an agent. | Is Within service Level = 1 Handle Type is abandoned . | Count of Contact Session ID |
| Average Abandon per Day | Number of calls abandoned in the Queue divided by the number of days in report period (including non-working days). | Handle Type is abandoned . | Number of calls abandoned / Number of days in report period |
| Average Queue Time | Average time spent by a call in the queue. | — | Average of Queue Duration Total Queue time / Calls Presented |
| Maximum Queue Time | The maximum time a call spent waiting in the queue. | — | Maximum Queue Duration |
| Calls Transferred to DN | Number of calls that were transferred to a dial number (DN) by blind transfer node via flow. If you want the calls transferred to DN count to be incremented, contact Cisco Support as the corresponding feature flag may have to be enabled. | Handle type is TransferToDN . | Count of Contact Session ID |
| Percentage Calls Transferred to DN | Percentage of calls that were transferred to a dial number (DN) by blind transfer node via flow. | — | (Calls Transferred to DN / Calls Presented) x 100 |
| Others | This parameter represents the total number of calls that are not included in the predefined categories of Calls Handled, Calls Abandoned, Calls Moved Out of Queue, or Calls Transferred to DN. It is calculated by subtracting these categories from the total number of Calls Presented. A value of 0 indicates that the calls presented and handled are equal for a queue during the specified time range. | — | Call Presented – (Calls Handled + Calls Abandoned + Calls Moved Out of Queue + Calls Transferred to DN + Consult to Queue Failed Count + Consult to Entry Point Failed Count) |
| Consult to Queue Failed Count | Count of consult requests failed at queue. | — | CTQ Error Count + Outdial CTQ Error Count |
| Consult to Entry Point Failed Count | Count of consult requests failed at Entry Point. | — | Sum of Consult To EP Error Count |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Queue Name | The name of the queue. Used As : Row Segment | — | — |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment | — | — |
| Calls Handled | Number of calls that were routed to the Queue and were handled. | Handle Type is normal or sudden_disonnect . | Connected Count + CTQ Handled Count + Outdial CTQ Handled Count – (Blind Transfer to Agent Count + Agent Transferred In Count) |
| Total Calls Handled with Queue Time in 0-15 seconds | Number of handled calls with a queue time that is less than or equal to 15 seconds. | Queue Duration <= 15000 ms Handle Type is normal or sudden_disonnect . | Connected Count (Queue Duration <= 15000 ms) + CTQ Handled Count+ Outdial CTQ Handled Count - (Blind Transfer Count (Queue Duration <= 15000 ms) + Agent Transferred In Count (Queue Duration <= 15000 ms)) |
| Percentage of Calls Handled with Queue Time in 0-15 seconds | Percentage of handled calls with a queue time that is less than or equal to 15 seconds. | — | (Total Calls Handled with Queue Time in 0-15 seconds / Calls Handled) x 100 |
| Total Calls Handled with Queue Time in 0-30 seconds | Number of handled calls with a queue time that is less than or equal to 30 seconds. | Queue Duration <= 30000 ms Handle Type is normal or sudden_disonnect . | Connected Count (Queue Duration <= 30000 ms) + CTQ Handled Count + Outdial CTQ Handled Count - (Blind Transfer Count (Queue Duration <= 30000 ms) + Agent Transferred In Count (Queue Duration <= 30000 ms)) |
| Percentage of Calls Handled with Queue Time in 0-30 seconds | Percentage of handled calls with a queue time that is less than or equal to 30 seconds. | — | (Total Calls Handled with Queue Time in 0-30 seconds / Calls Handled) x 100 |
| Total Calls Handled with Queue Time in 0-45 seconds | Number of handled calls with a queue time that is less than or equal to 45 seconds. | Queue Duration <= 45000 ms Handle Type is normal or sudden_disonnect . | Connected Count (Queue Duration <= 45000 ms) + CTQ Handled Count + Outdial CTQ Handled Count - (Blind Transfer Count (Queue Duration <= 45000 ms) + Agent Transferred In Count (Queue Duration <= 45000 ms)) |
| Percentage of Calls Handled with Queue Time in 0-45 seconds | Percentage of handled calls with a queue time that is less than or equal to 45 seconds. | — | (Total Calls Handled with Queue Time in 0-45 seconds / Calls Handled) x 100 |
| Total Calls Handled with Queue Time in 0-60 seconds | Number of handled calls with a queue time that is less than or equal to 60 seconds. | Queue Duration <= 60000 ms Handle type is normal or sudden_disonnect . | Connected Count (Queue Duration <= 60000 ms) + CTQ Handled Count + Outdial CTQ Handled Count - (Blind Transfer Count (Queue Duration <= 60000 ms) + Agent Transferred In Count (Queue Duration <= 60000 ms)) |
| Percentage of Calls Handled with Queue Time in 0-60 seconds | Percentage of handled calls with a queue time that is less than or equal to 60 seconds. | — | (Total Calls Handled with Queue Time in 0-60 seconds / Calls Handled) x 100 |
| Total Calls Handled with Queue Time > 60 seconds | Number of handled calls with a Queue time that is greater than 60 seconds. | Queue Duration > 60000 ms Handle type is normal or sudden_disonnect . | Connected Count (Queue Duration > 60000 ms ) + CTQ Handled Count + Outdial CTQ Handled Count - (Blind Transfer Count (Queue Duration > 60000 ms) + Agent Transferred In Count (Queue Duration > 60000 ms)) |
| Percentage of Calls Handled with Queue Time > 60 seconds | Percentage of handled calls with a Queue time that is greater than 60 seconds. | — | (Total Calls Handled with Queue Time > 60 seconds / Calls Handled) x 100 |
| Calls Abandoned | Count of calls that got abandoned in a queue. | Handle Type is abandoned . | Count of Contact Session ID |
| Total Calls Abandoned with Queue Time in 0-15 seconds | Number of abandoned calls with a queue time that is less than or equal to 15 seconds. | Queue Duration <= 15000 ms Handle Type is abandoned . | Count of Contact Session ID |
| Percentage of Calls Abandoned with Queue Time in 0-15 seconds | Percentage of abandoned calls with a queue time that is less than or equal to 15 seconds. | — | (Total Calls Abandoned with Queue Time in 0-15 seconds / Calls Abandoned) x 100 |
| Total Calls Abandoned with Queue Time in 0-30 seconds | Number of abandoned calls with a queue time that is less than or equal to 30 seconds. | Queue Duration <= 30000 ms Handle Type is abandoned . | Count of Contact Session ID |
| Percentage of Calls Abandoned with Queue Time in 0-30 seconds | Percentage of abandoned calls with a queue time that is less than or equal to 30 seconds. | — | (Total Calls Abandoned with Queue Time in 0-30 seconds / Calls Abandoned) x 100 |
| Total Calls Abandoned with Queue Time in 0-45 seconds | Number of abandoned calls with a queue time that is less than or equal to 45 seconds. | Queue Duration <= 45000 ms Handle Type is abandoned . | Count of Contact Session ID |
| Percentage of Calls Abandoned with Queue Time in 0-45 seconds | Percentage of abandoned calls with a queue time that is less than or equal to 45 seconds. | — | (Total Calls Abandoned with Queue Time in 0-45 seconds / Calls Abandoned) x 100 |
| Total Calls Abandoned with Queue Time in 0-60 seconds | Number of abandoned calls with a queue time that is less than or equal to 60 seconds. | Queue Duration <= 60000 ms Handle Type is abandoned . | Count of Contact Session ID |
| Percentage of Calls Abandoned with Queue Time in 0-60 seconds | Percentage of abandoned calls with a queue time that is less than or equal to 60 seconds. | — | (Total Calls Abandoned with Queue Time in 0-60 seconds / Calls Abandoned) x 100 |
| Total Calls Abandoned with Queue Time > 60 seconds | Percentage of abandoned calls with a Queue time that is greater than 60 seconds. | Queue Duration > 60000 ms Handle Type is abandoned | Count of Contact Session ID |
| Percentage of Calls Abandoned with Queue Time > 60 seconds | Percentage of abandoned calls with a Queue time that is greater than 60 seconds. | — | (Total Calls Abandoned with Queue Time > 60 seconds / Calls Abandoned) x 100 |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of an agent, that is, a person who answers customer calls. Used As : Row Segment |  |
| Interval | Time Period | Realtime - 30 mins |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Staff Hours | The total amount of time agents were logged in. | Sum of Realtime Update Timestamp - Sum of Login Timestamp |
| Occupancy | The measure of time agents spent on calls compared to available and idle time. | (Sum of Outdial Wrapup Duration + Sum of Wrapup Duration ) + (Sum of Outdial Connected Duration + Sum of connected duration) / (Sum of Available Duration + Sum of Idle Duration + Sum of Not Responding Duration) + (Sum of Connected Duration + Sum of Wrapup Duration + Sum of Outdial Connected Duration + Sum of Outdial Wrapup Duration) |
| Total Calls | The total number of calls from all origination types. | Sum of Outdial Connected Count + Sum of connected Count |
| Idle Time | The total amount of time the agents spent in the Idle state. | Sum of Idle Duration |
| Available Time | The total amount of time the agents spent in the Available state. | Sum of Available Duration |
| Inbound Reserved Time | The total amount of time the agents spent in the Reserved state (time duration once the call starts ringing and before the call is answered). | Sum of Ringing Duration |
| Inbound Connected Time | The total amount of time an agent was talking with a caller. | Sum of Connected Duration |
| Inbound Contact Time | Total connected duration of a call agent is attending including hold time. | Sum Of Connected Duration + Sum Of Hold Duration |
| Inbound Hold Time | The number of times an agent put an inbound caller on hold. | Sum of Hold Duration |
| Inbound Connected Time | The total amount of time an agent was talking with a caller. | Sum of Connected Duration |
| Inbound Wrapup Time | The total amount of time the agents spent in the Wrap-up state after an inbound call. | Sum of Wrapup Duration |
| Inbound Average Connected Time | The average inbound connected time. | (Sum of Connected Duration + Sum of Hold Duration) / Sum of Connected Count |
| Inbound Average Handle Time | The average length of time agents were in the Wrap-up state after an inbound call. | (Sum of Connected Duration  + Sum of Wrapup Duration) / (Sum of Connected Count) |
| Not Responding Time | The total amount of time the agents spent in the Not Responding state. | Sum of Not Responding Duration |
| Outdial Attempted Count | The number of times an agent was in the Outdial Reserved state (time duration once the call starts ringing and before the call is answered). | Sum of Outdial Count |
| Outdial Connected Count | The number of outdial calls that got connected to an agent. | Sum of Outdial Connected Count |
| Outdial Reserved Time | The total amount of time the agents were in the Outdial Reserved state. | Sum of Outdial Ringing Duration |
| Outdial Hold Time | The total amount of time the outdial calls were on hold. | Sum of Outdial Hold Duration |
| Outdial Connected Time | The amount of time the agents got connected to outdial calls. | Sum of Outdial Connected Duration |
| Outdial Wrapup Time | The total amount of time agents spent in the Wrap-up state after an outdial call. | Sum of Outdial Wrapup Duration |
| Outdial Average Connected Time | The average outbound connected time. | Sum of Outdial Connected Duration / Sum of Outdial Connected Count |
| Outdial Average Handle Time | The average length of time spent handling an outdial call (Total Outdial Connected Time plus Total Outdial Wrap Up Time, divided by Outdial Connected Count). | (Sum of Outdial Connected Duration  + Sum of Outdial Wrapup Duration) / (Sum of Outdial Count +Sum of Outdial Connected Count) |
| Login Duration | The sum of time during which the agent was engaged in the activity. | Maximum Logout Timestamp - Minimum Login Timestamp |
| Engaged Duration | Shows the total amount of time an agent was engaged. | Sum of Engaged Duration |

| Parameter | Description |
|---|---|
| Login/Skill-Update Time | Shows the next login date and time for an agent whose skill profile/skills were updated when logged out, or the date and time when the skill profile/skills were updated for an agent who is currently logged in. |
| Skill Profile | Shows the name of the skill profile that is associated with an agent. |
| Skills | Shows the skill of an agent, such as language fluency or product expertise. The column shows multiple skills mapped to the corresponding skill profile, in a comma-separated single string. |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of an agent, that is, a person who answers customer calls. Used As : Row Segment |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Login Time | The date and time the agent logged in. | Minimum Login Timestamp |
| Outdial Contact Handled | The number of outbound calls handled. | Sum of Outdial Connected Count |
| Outdial Average Handle Time | The average handle time for outbound calls. | (Outdial Connected Time + Outdial Wrapup Time) / Outdial Calls Outdial Connected Time = Sum of Outdial Connected Duration. Outdial Wrapup Time = Sum of Outdial Wrapup Duration. Outdial Calls = Outdial Attempted Count + Outdial Contact Handled Outdial Attempted Count = Sum of Outdial Count. |
| Outdial Connected Time | The total amount of time an agent was talking with a party on an outdial call. | Sum of Outdial Connected Duration |
| Outdial Average Connected Time | The average of outdial connected time. | Outdial Connected Time / Outdial Contact Handled |
| Outdial Talk Time | The total amount of time an agent was talking with a party on an outdial call. | Outdial Connected Time + Outdial Hold Duration Outdial Hold Duration = Sum Of Outdial Hold Duration |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Connected Count | Number of answered contact types. | Channel Type: chat, telephony, email, social | Sum of Connected Count |

| Parameter | Description | Formula |
|---|---|---|
| Connected Count | Number of answered contact types. | Sum of Connected Count |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Agent Name | Name of the agent |  | Row Segment |
| Channel Type | The media type of the contact, such as telephony, email, or chat. |  | Row Segment |
| Total Logged In | The total number of times agent logged in. |  | Count of Agent Session ID |
| Idle Count | The number of times an agent went into the Idle state. | Activity State: Idle, idle | Count of Agent Session ID |
| Available Count | The number of agents currently in the Available state. | Activity State: Available, available | Count of Agent Session ID |
| Reserved Count | The number of times agent currently in the Reserved state (where the incoming call
                isn’t yet answered). | Activity State: Ringing, ringing | Sum of Inbound Reserved Count |
| Connected Count | The number of calls currently connected to an agent. | Activity State: Connected, connected | Count of Agent Session ID |
| Consulting Count | The number of times an agent was in the Consulting state. | Activity State: Available consulting, available-consulting, ConnectedConsulting | Count of Agent Session ID |
| Conferencing Count | The number of times an agent initiated a conference call. | Activity State: Conferencing, conferencing | Sum of Conference Count |
| Wrap Up Count | The number of times an agent was in the Wrap Up state. | Activity State: Wrapup, wrapup | Count of Agent Session ID |
| Not Responding Count | The number of times an agent failed to respond to an incoming request due to which the contact couldn’t be connected to the agent. | Activity State: Not Responding, not-responding | Count of Agent Session ID (Activity State =NotResponding) |
| In Outdial Count | The number of agents who are connected to or are wrapping up an outdial call. | Is Outdial: >= 1 | Count of Is Outdial |
| Engaged Count | Shows the number of times the agent went into the Engaged state. |  | Sum of Engaged Count |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | The name of the agent. |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. |  |
| Channel ID | The channel ID of the channel type. |  |
| Current State | The current state of the contact. This field is available only in the Customer Session Repository (CSR), and only for real-time visualizations. |  |
| Initial Login Time | The date and time when the agent logged in. | Minimum Login Timestamp |
| Calls Handled | The total number of voice interactions handled. | Value of Outdial Connected Count + Value of Connected Count |
| Chats Handled | The total number of chat interactions handled. | Value of Outdial Connected Count (Channel Type: chat) + Value of Connected Count (Channel Type: chat) |
| Emails Handled | The total number of email interactions handled. | Value of Outdial Connected Count (Channel Type: email) + Value of Connected Count (Channel Type: email) |
| Social Handled | The total number of social channel interactions handled. | Social Connected Count + Social Outdial Connected Count |

| Parameter | Description | Formula |
|---|---|---|
| Queue Name | The name of the queue. Used As : Row Segment |  |
| #Contacts Handled | Total number of customer interactions that the agent handles within the interval. | Sum of Connected Count |
| Consult Count | The number of times an agent answered a consult request from another agent. | Sum of Consult Count |
| Total Consult Time | The total amount of time an agent spent answering consult requests. | Sum of Consult Duration |
| Average Consult Time | The average length of time an agent spent answering consult requests. | Average of Consult Duration |
| Agent Transfer Count | The number of times an agent transferred inbound contacts to another agent after consult. | Sum of Transfer Count |
| Average Handled Time | The average time you take to handle a customer interaction. It includes the connected, hold, and wrap-up times. | (Connected Duration + wrapup Duration + Post call Duration) / (Connected Count + Conference Connected Count + Post call Connected Count) |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| Queue Name | The name of the queue. |  |  |
| # Contacts | The total number of contacts since the start of the day. |  | Count of Contact Session ID |
| # Contacts Handled | Number of contacts handled since the start of the day. | Handle Type: normal | Count of Contact Session ID |
| Longest Handled Contact from Queue | The longest duration that a contact spent in queue since the start of the day. This is calculated after the call status changes from parked to connected or ended. | Current State: connected, ended | Maximum Queue Duration |
| # Abandoned Contacts | Number of abandoned contacts since the start of the day. | Termination Type: abandoned | Count of Contact Session ID |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| Queue Name | The name of the queue. |  |  |
| # Contacts Waiting in Queue | Number of contacts waiting in queue. | Current State: parked | Count of Contact Session ID |
| Avg Queue Wait Time | Average Queue Wait Time of all the calls that are currently active. | Current State: connected, ended | Average of QueueDuration |

| Parameter | Description | Formula |
|---|---|---|
| Team Name | Name of the team. |  |
| Agent Name | Name of the agent. |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |
| Total Log In Count | The total number of contacts that were logged in. | Cardinality of Agent Session ID (Cardinality provides the total number of unique Agent Session IDs.) |
| Initial Login Time | First login time. | Minimum Login Timestamp |
| Final Logout Time | Last logout time. | Maximum Logout Timestamp |
| Staff Hours | Total amount of time agents were logged in. | Sum of Realtime Update Timestamp - Sum of Login Timestamp |
| Idle Counts | Total count of idle state. | Sum of Idle Count |
| # Contacts Handled | The number of contacts handled. | Sum of Connected Count |
| # Calls Handled | The number of calls that were handled. | Voice Connected Count |
| # Chats Handled | The number of chats that were handled. | Chat Outdial Connected Count |
| # Emails Handled | The number of emails that were handled. | Email Connected Count |
| # Social Handled | The total number of social channel interactions handled. | Social Connected Count + Social Outdial Connected Count |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Interval | Time Period |  | Last 7 Days |
| Queue Name | The name of a queue. Used As : Row Segment |  |  |
| Queue ID | The ID of a queue. Used As : Row Segment |  |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| % Abandoned | The percentage of calls that were abandoned. |  | Count of Contact Session ID (Termination Type = abandoned) / Sum of Contact Count |
| Completed | The number of calls that ended during the report interval. Answered, abandoned, and disconnected calls are included in this count. Transferred and short calls aren’t. |  | Count of Contact Session ID(Termination Type = normal) + Count of Contact Session ID (Termination Type = abandoned) + Count of Contact Session ID (Termination Type = quick_disconnect) |
| Abandoned | The number of calls that got abandoned during the report interval. An abandoned call is a call that was terminated without being distributed to a destination site, but that was in the system for longer than the time specified by the Short Call threshold provisioned for the enterprise. | Termination Type: abandoned | Count of Contact Session ID |
| Abandoned with SL | The number of calls that got terminated while in queue within the Service Level threshold provisioned for the queue or skill |  | Sum of Interactions Within Service Level (Termination Type: abandoned) |
| Total | The total number of calls from all origination types. |  | Sum of Contact Count |
| Queued Time | The cumulative amount of time the calls were in queue, waiting to be sent to an agent or other resource. Because queued time is calculated after the call leaves the queue, the queued time for a call that is still in the queue isn’t reflected in the report. |  | Sum of Queue Duration |
| Abandoned Time | The cumulative amount of time between when calls entered the queue and when they got answered (connected to an agent or other resource) during the report interval. Because answered time is calculated after the call is answered, answered time for calls that are waiting to be answered isn’t reflected in the report. | Is Contact Handled: != 1 | Sum of Queue Duration |
| Average Queued Time | The total amount of time that calls were in queue divided by the total number of calls that were queued. |  | Sum of Queue Duration/ Sum of Queue Count |
| Avg Abandoned Time | The total amount of time that calls were in the system before they got abandoned divided by the total number of calls that got abandoned. |  | Sum of Queue Duration(Is Contact Handled! = 1) / Count of Contact Session ID (Termination Type = abandoned) |

| Parameter | Description | Formula |
|---|---|---|
| Incoming | Number of incoming contact types. | Count of Contact Session ID |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Interval | Time Period |  | Last 7 Days |
| Entry point Name | Name of entry point. Used As : Row Segment |  |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| Incoming | Represents an incoming call. |  | Count of Contact Session ID |
| Short | The number of calls that were terminated within the Short Call threshold provisioned for the enterprise without being connected to an agent. | Termination Type: short_call | Count of Contact Session ID |
| IVR Time | The number of calls in the IVR system. |  | Sum of IVR Duration |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Queue Name | The name of a queue. Used As : Row Segment |  |  |
| Interval | Time Period |  | Last 7 Days |
| Channel Type | The media type of the contact, such as telephony, email, or
                                    chat. Used As : Row Segment |  |  |
| In Service Level % | The number of calls that got answered within the Service Level
                            threshold provisioned for the queue or skill (in a skills interval by
                            queue report), divided by total calls (including abandoned
                            calls). |  | (In Service Level) / Total |
| % Answered | The number of answered calls divided by the number of calls that
                            entered the queue minus short calls. |  | Count of Contact Session ID (Connected Duration > 0) / Count of
                            Contact Session ID (Termination Type = abandoned) + Count of Contact
                            Session ID (Connected Duration > 0) |
| Total | The total number of calls from all origination types. |  | Sum of Contact Count |
| Completed | The number of calls that ended during the report interval. Answered,
                            abandoned, and disconnected calls are included in this count.
                            Transferred and short calls are not. |  | Count of Contact Session ID(Termination Type = abandoned) + Count of
                            Contact Session ID (Connected Duration > 0)+Count of Contact Session
                            ID (Termination Type = quick_disconnect) |
| Abandoned | The number of calls that got abandoned during the report interval. An
                            abandoned call is a call that was terminated without being distributed
                            to a destination site, but that was in the system for longer than the
                            time specified by the Short Call threshold provisioned for the
                            enterprise. | Termination Type: abandoned | Count of Contact Session ID (Termination Type = abandoned) |
| Answered | The number of calls that were routed from the queue to an agent or
                            available resource and were answered by the agent or resource. |  | Count of Contact Session ID (Connected Duration > 0) |
| Conference Count | The number of times agents initiated a conference call to an agent or
                            external number. |  | Sum of Conference Count |
| Hold Count | The number of times a caller was put on hold. |  | Sum of Hold Count |
| Avg Abandoned Time | The total amount of time that calls were in the system before they
                            were abandoned divided by the total number of calls that were
                            abandoned. |  | Sum of Queue Duration (Is Contact Handled ! = 1) / Count of Contact
                            Session ID (Termination Type = abandoned) |
| Avg Speed of Answer | The total answered time divided by the total number of answered
                            calls. |  | Sum of Queue Duration(Connected Duration > 0) / Count of Contact
                            Session ID (Connected Duration > 0) |

| Parameter | Description | Formula |
|---|---|---|
| Completed | The number of calls that ended during the report interval. The count includes answered, abandoned, and disconnected calls. Transferred and short calls aren’t included. | Count of Contact Session ID (Connected Duration > 0) + Count of Contact Session ID (Termination Type = abandoned) + Count of Contact Session ID (Termination Type = quick_disconnect) |

| Parameter | Description |
|---|---|
| Queue ID | The unique identifier for a queue. |
| Queue Name | The name of a queue. |
| Skills assigned in | Indicates where skills are assigned. The following are the values: For the current Skill-Based Routing Team's queue, the value is 'Flow'. For the Skill-based queue, the value is ‘Queue’. For the Agent-based queue, the value is ‘NA’. |
| Channel Type | Media type of the queue such as telephony, email, or chat. |
| Longest Queued Contact Time | Longest time for which a contact waited in the queue. |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| In IVR | The number of calls that are currently in the IVR system. | Current State: ivr-connected | Count of Contact Session ID |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Entry point Name | The name of the entry point, which is the landing place for customer calls on the Webex Contact Center system. Used As : Row Segment |  |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| In IVR | The number of calls that are currently in the IVR system. | Current State: ivr-connected | Count of Contact Session ID |
| In Queue | The number of calls currently in the queues that are in the report. In the case of entry-point reports, this number is the number of calls that are currently in queues fed by the entry point. | Current State: parked | Count of Contact Session ID |
| Connected | The number of calls currently connected to an agent. | Current State: connected, on-hold, hold-done, consult-done, consulting | Count of Contact Session ID |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Voice | The media type of the telephony contact. |  | Count of Contact Session ID (Channel Type = telephony and Current State = connected) |
| Chat | The media type of the chat contact. |  | Count of Contact Session ID (Channel Type = chat and Current State = connected) |
| Email | The media type of the email contact. |  | Count of Contact Session ID (Channel Type = email and Current State = connected |
| In Queue | Then number of queues contact entered. | Current State: parked | Count of Contact Session ID |
| Connected | The total number of calls handled. | Current State: connected, on hold | Count of Contact Session ID |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| In Queue | The number of calls currently in the queues that are in the report. In the case of entry-point reports, this number is the number of calls that are currently in queues fed by the entry point. | Current State: parked | Count of Contact Session ID |
| Connected | The number of calls currently connected to an agent. | Current State: connected, on-hold | Count of Contact Session ID ) |

| Parameter | Description | Filters | Formula |
|---|---|---|---|
| Queue Name | Name of the queue. Used As : Row Segment |  |  |
| Skills assigned in | Indicates where skills are assigned. The following are the values: For the current Skill-Based Routing Team's queue, the value is 'Flow'. For the Skill-based queue, the value is ‘Queue’. For the Agent-based queue, the value is ‘NA’. |  |  |
| Site Name | Name of the site. Used As : Row Segment |  |  |
| Team Name | Name of the team. Used As : Row Segment |  |  |
| Channel Type | The media type of the contact, such as telephony, email, or chat. Used As : Row Segment |  |  |
| In Queue | The number of calls currently in the queues that are in the report. In the case of entry-point reports, this number is the number of calls that are currently in queues fed by the entry point. | Current State: parked | Count of Contact Session ID |
| Connected | The number of calls currently connected to an agent. | Current State: connected, on-hold, hold-done, consulting, consult-done | Count of Contact Session ID |
| Current Service Level % | The percentage of calls in queue that haven’t yet reached the Service Level threshold provisioned for the queue |  | Current Service Level % = In service level / Total Total= Count of Contact Session ID |
| Logged In Agents | The number of agents who are currently logged in to this team or to all teams at this site. At the queue level, this number is the number of agents logged in to all teams at the sites serving this queue. |  | Count of Agent ID |

| Parameter | Description | Formula |
|---|---|---|
| Team Name | Name of the team. |  |
| Agent Name | Name of the agent. |  |
| Current State | Shows the state of the agent such as Available, Idle, or Not Responding. |  |
| # Contacts Handled | Number of Inbound contacts handled. | Total number of inbound contact session IDs |
| Average Handle Time | Average time taken to handle a contact. | Total amount of contact time during the specified interval/The number of contacts handled during the specified interval |
| Average Wrapup Time | Average time taken to wrap up a contact. | Total Wrapup time during the specified interval/Total number of Wrapups during the specified interval |

| Parameter | Description | Formula |
|---|---|---|
| Call Start Time | Timestamp when the contact started. | Value of Contact Start Timestamp |
| Called Number | DNIS digits delivered with the call. The telephone company sends a Dialed Number Identification Service (DNIS) digit string that contains the caller's phone number. | Value of DNIS |
| Call ANI | ANI digits delivered with a call. The telephone company sends an Automatic Number Identification (ANI) digit string that contains the caller's phone number. | Value of ANI |
| Call Routed CSQ | Name of the queue that the call was placed while waiting for an agent. | Value of First Queue Name |
| Agent | Name of the agent who received the call before the call was abandoned. | Value of Agent Name |
| Call Skills | Skills that were associated with the queue to which the call was routed. | Value of Skills |
| Skills assigned in | Indicates where skills are assigned. The following are the values: For the current Skill-Based Routing Team's queue, the value is 'Flow'. For the Skill-based queue, the value is ‘Queue’. For the Agent-based queue, the value is ‘NA’. |  |
| Call Abandon Time | Date and time when the call was abandoned. | Value of Contact End Timestamp |
| Time to Abandon | The amount of time that elapsed between the time the call came in to the system and the time it was abandoned. | Call Abandon Time - Call Start Time |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | Name of an agent. Used as a Row Segment. |  |
| Agent Endpoint (DN) | The endpoint (number, email, or chat handle) on which an agent received calls, chats, or emails. Used as a Row Segment. |  |
| Total Inbound | Total calls that an agent received. | Count of Contact Session ID (Call Direction = inbound) |
| Avg Talk Time Inbound | Average time that an agent spent talking with a caller. | Average of Connected Duration (Call Direction = inbound) |
| Avg Hold Time Inbound | Average time that an agent put an inbound call on hold. | Average of Hold Duration (Call Direction = inbound) |
| Avg Work Time Inbound | Average time that an agent was engaged after disconnecting or transferring an inbound call. | Average of Wrapup Duration (Call Direction = inbound) |
| Outbound Calls | Calls that an agent made. This includes both connected and attempted calls. | Count of Contact Session ID (Call Direction = outdial) |
| Avg Call Time Outbound | Average time that an agent was engaged in an outbound call. | Average of Connected Duration (Call Direction = outdial) |
| Max Call Time Outbound | Maximum time that an agent was engaged in an outbound call. | Maximum Connected Duration (Call Direction = outdial) |
| Transfer In | Calls that were transferred to an agent. 'Transfer In' count increases when a consult transfer occurs. | Sum of Agent Transferred In Count |
| Transfer Out | Calls that an agent transfered out. 'Transferred Out' count increases when a blind transfer occurs. | Sum of Agent To Agent Transfer Count + Sum of Agent To DN Transfer Count + Sum of Agent To Queue Transfer Count + Sum of Agent To Entrypoint Transfer Count |
| Conference | Conference calls in which an agent participated. | Sum of Conference Count |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | Name of an agent. | Value of Agent Name |
| Extension | Endpoint (number, e-mail, or chat handle) on which an agent received calls, chats, or emails. | Value of Agent Endpoint (DN) |
| Call Start Time | Date and time when the call started. | Value of Contact Start Timestamp |
| Call End Time | Date and time when the call ended. | Value of Contact End Timestamp |
| Duration | Elapsed time between the call start time and the call end time. | Call End Time - Call Start Time |
| Called Number | DNIS digits delivered with the call. The telephone company sends a Dialed Number Identification Service (DNIS) digit string that contains the caller's phone number. | Value of DNIS |
| Call ANI | ANI digits delivered with a call. The telephone company sends an Automatic Number Identification (ANI) digit string that contains the caller's phone number. | Value of ANI |
| Call Routed CSQ | Name of the queue that held the calls waiting for an agent. | Value of First Queue Name |
| Other CSQs | Name of the final queue where the call waited for an agent when there were multiple queues used. | Value of Final Queue Name |
| Call Skills | Skills that were associated with the queue that handled the call. | Value of Skills |
| Skills assigned in | Indicates where skills are assigned. The following are the values: For the current Skill-Based Routing Team's queue, the value is 'Flow'. For the Skill-based queue, the value is ‘Queue’. For the Agent-based queue, the value is ‘NA’. |  |
| Talk Time | Elapsed time between the time an agent connected to the call and the time the call was disconnected or transferred, not including the hold time. | Value of Connected Duration |
| Hold Time | Total amount of time that an agent put the calls on hold. | Value of Hold Duration |
| Work Time | Total amount of time that an agent was engaged after disconnecting or transferring a call. | Value of Wrapup Duration |
| Call Direction | Indicates if the call was an inbound call or an outbound call. | Value of Call Direction |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | Name of an agent. Used as a Row Segment. |  |
| Calls Handled | Number of calls that were connected to an agent. If the agent established a conference with another agent, the value increases by one for the conferenced agent. If the agent transferred a call and the call was transferred back to the agent, the value increases by two. | Count of Wrapup Code Name |
| Calls Presented | Number of calls that were sent to the agent, regardless of whether the agent picked up the call. If a call was connected to an agent, transferred to another agent, and then transferred back to the original agent, the value for the original agent increases by two (once for each time the call was presented). | Count of Contact Session ID |
| Handled Ratio | Ratio of calls handled by an agent to the calls presented to the agent. | Calls Handled / Calls Presented |
| Avg Handle Time | Average handle time for all calls that the agent handled. | Total Handle Time / Calls Handled |
| Average Talk Time | Average time that an agent spent in a call. | Average of Connected Duration |
| Max Talk Time | Maximum time that an agent spent in a call. | Maximum Connected Duration |
| Average Hold Time | Average time that an agent put a call on hold. | Average of Hold Duration For mulitple agent sessions, the Average of Hold Duration is
                                    calculated as Total Hold Duration / Number of agent sessions on
                                    which the hold duration. |
| Max Hold Time | Maximum time that an agent put a call on hold. | Maximum Hold Duration |
| Average Work Time | Average time that an agent was engaged after disconnecting or transferring a call. | Average of Wrapup Duration |
| Max Work Time | Maximum time that an agent was engaged after disconnecting or transferring a call. | Maximum Wrapup Duration |

| Parameter | Description | Formula |
|---|---|---|
| Entrypoint Name | Name of an entry point. Used as a Row Segment. |  |
| Calls Presented | Number of calls that were received by an application, including internal calls. It includes the number of calls that were handled by the application and the number of calls that were abandoned while in the application. | Count of Contact Session ID |
| Calls Handled | Number of calls that were handled by the application including internal calls. | Count of Contact Session ID (Termination Type = normal |
| Avg Speed of Answer | Average queue time before an agent answered a call. Calls that did not connect to an agent are not included in this calculation. | Average of Queue Duration |
| Avg Talk Time | Average time that an agent spent in a call. | Average of Connected Duration |
| Avg Work Time | Average time that an agent was engaged after disconnecting or transferring a call. | Average of Wrapup Duration |
| Calls Abandoned | Number of calls that were abandoned by the application. | Count of Termination Type (Termination Type = abandoned) |
| Avg Abandon Time | Average duration of calls before they were abandoned. | Average of Queue Duration (Termination Type = abandoned) |

| Parameter | Description | Formula |
|---|---|---|
| First Queue Name | Name of the queue. Used as a Row Segment. |  |
| Interval | Time Period. Used as a Row Segment. |  |
| Start Time | Timestamp when the contact started. | Minimum Contact Start Timestamp |
| End Time | Timestamp when the contact ended. | Maximum Contact End Timestamp |
| Calls Presented | Number of calls that were routed to the queue, regardless of whether an agent picked up the call. | Count of Contact Session ID |
| Calls Handled | Number of calls that were handled by the queue. | Count of Contact Session ID (Termination Type = normal) |
| Calls Abandoned < SL | Number of calls that were abandoned within the time shown in the Service Level field. | Count of Contact Session ID (Is Within service Level = 1, Termination Type = abandoned) |
| Calls Abandoned | Number of calls that were routed to the queue and were abandoned. | Count of Contact Session ID (Termination Type = abandoned) |
| Abandon Rate | Percentage of calls that were routed to the queue and were abandoned. | Calls Abandoned / Calls Presented |

| Parameter | Description | Formula |
|---|---|---|
| First Queue Name | Name of the queue. Used as a Row Segment. |  |
| Agent Name | Name of an agent. Used as a Row Segment. |  |
| Calls Handled | Number of calls that were answered by an agent in a queue during the report period. | Count of Wrapup Code Name |
| Avg Talk Time | Average time that an agent spent for calls in a queue. | Average of Connected Duration |
| Total Talk Time | Total time that an agent spent for calls in a queue. | Sum of Connected Duration |
| Avg Work Time | Average time that an agent spent after disconnecting or transferring calls in a queue. | Average of Wrapup Duration |
| Total Work Time | Total time that an agent spent after disconnecting or transferring
                                calls in a queue. | Sum of Wrapup Duration |
| Total Ring Time | Elapsed time between the time when a call ringed and the time the call was answered by an agent, routed to another agent, or disconnected. | Sum of Ringing Duration |
| Avg Ring Time | Average time between the time when a call ringed and the time the call was answered by an agent, routed to another agent, or disconnected. | Average of Ringing Duration |
| Calls On Hold | Calls that the agent put on hold. | Sum of Hold Count |
| Avg Hold Time | Average time for calls that the agent put on hold. | Average of Hold Duration |
| Total Hold Time | Total time for calls that the agent put on hold. | Sum of Hold Duration |

| Parameter | Description | Formula |
|---|---|---|
| Queue Name | Name of the queue. Used as a Row Segment. |  |
| In Service Level% | Number of calls that were answered within the Service Level threshold provisioned for the queue. | In Service Level / Calls Presented |
| Calls Presented | Number of calls that were routed to the queue, regardless of whether an agent picks up the call. | Count of Contact Session ID (Channel Type = telephony) |
| Calls Handled | Number of calls that were handled by the queue. | Count of Contact Session ID (Termination Type= normal, Channel Type = telephony) |
| Percentage Handled | Percentage of calls that were handled by the queue. | Calls Handled / Calls Presented |
| Average Handled Time | Average time for all calls that the queue handled. | Total Handle Time / Calls Handled |
| Max Connected Time | Maximum time that an agent spent in calls handled by the queue. | Maximum Connected Duration |
| Calls Abandoned | Number of calls that were routed to the queue and are abandoned. | Count of Contact Session ID (Termination  Type = abandoned) |
| Percentage Abandoned | Percentage of calls that were routed to the queue and were abandoned. | Calls Abandoned / Calls Presented |
| Avg Abandoned Time | Average time that the calls spent in the queue before being abandoned. | Average of Queue Duration (Termination Type = abandoned) |
| Max Abandoned Time | Maximum time a call spent in the queue before being abandoned. | Maximum Queue Duration (Termination Type = abandoned) |
| Avg Speed of Answer | Average queue time before an agent answered a call. | Answered Time / Answered |

| Parameter | Description | Formula |
|---|---|---|
| Agent Name | Name of an agent. Used as a Row Segment. |  |
| In Calls Presented | Number of calls that were sent to an agent, regardless of whether the agent picked up the call. | Count of Contact Session ID (Channel Type = telephony, Call Direction = inbound) |
| In Calls Handled | Number of calls that were connected to an agent. | Count of Contact Session ID (Termination Type = normal, Channel Type = telephony, Call Direction type = inbound) |
| Handle Time Avg | Average handle time for all calls that the agent handled. | Average of Wrapup Duration + Average of Connected Duration  (Channel Type = telephony, Call Direction = inbound) |
| Outdial Talk Time Max | Maximum talk time of any call that an agent handled. | Maximum Connected Duration (Channel Type = telephony, Call Direction = outdial) |
| Outdial Talk Time Avg | Average talk time of any call that an agent handled. | Average of Connected Duration (Channel Type = telephony, Call Direction = outdial) |
| Chat Presented | Number of chats that were presented to the agent. | Count of Contact Session ID (Channel Type = chat) |
| Chats Handled | Number of chats that the agent accepted. | Count of Wrapup Code Name (Channel Type = chat) |
| Chat Active Time Max | Maximum time that an agent spent in a chat. | Maximum Connected Duration (Channel Type = chat) |
| Chat Active Time Avg | Average time that an agent spent in a chat. | Average of Connected Duration (Channel Type = chat) |
| Emails Presented | Number of email messages that were presented to the agent. | Count of Contact Session ID (Channel Type = email) |
| Emails Handled | Number of email messages that the agent replied and forwarded. The send date and time determines whether the email message falls within the interval. | Count of Wrapup Code Name (Channel Type = email) |

| 1 | Click on a table cell and then click the Drill Down icon. The drill-down option is available only for the Column or Profile Variables set during the report creation process. Users will be able to drill down and have a detailed view of these fields, but not for row segments. Users are advised to structure the reports across Column or Profile Variables so that the desired details are accessible through the drill-down. The Drill Down panel displays the records involved in the computation of the visualization. If you drill down on a session ID (whether it is a contact or agent session ID), it drills down to the activities composing that session. |
|---|---|
| 2 | To add a field or a profile variable, click an entry from the Fields or Measures drop-down
                    list to append a new column. If you select a Field or Measure that already exists in the table, then it will not add the field again. |
| 3 | To export the report data as a Microsoft Excel or CSV file, click Export . The export option is not available for a Drill Down report with real-time data. |
| 4 | To view the Drill Down panel in a
                    separate window, click the Launch icon. |

| 1 | Click Settings . |
|---|---|
| 2 | To show or hide the summary of column values at the table level and the top-level row segment, select the values from the Show Summary drop-down list. |
| 3 | If you want the visualization to be updated immediately, select Redraw instantly . Otherwise, the visualization will be updated only when you click the Apply button. |
| 4 | To show or hide a profile variable, click the eye icon. |
| 5 | To hide a segment, drag it to the Hidden Segments box. This capability is not available for compound visualizations. |
| 6 | To reposition a segment, drag it to a different location either within its current Segments box or to a different Segments box. This capability is not available for compound visualizations. |
| 7 | To filter a segment: Select the is in or is not in option, and specify the values to include or exclude. For more information, see Filter using Data Filter Select the regular expression to enter an expression to be included or excluded. Click Save . Changes are always rendered immediately when you filter a segment and when you show or hide a profile variable. |
| 8 | If the visualization is a chart, select the Settings icon to modify the visualization. |

| 1 | Click Settings . |
|---|---|
| 2 | Select a format from the drop-down list. The possible formats are: Format Description Table Displays data in rows and columns. Heat Map Displays the cell values within a table in different
                                            shades of red. The cells in white and the darkest shade of red identify
                                            the outliers. Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Heat Maps for such reports. Row Heat Map Displays the cell values within each row in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a row. Row Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Row Heat Maps for such reports. Column Heat Map Displays the cell values within each column in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a column. Line Chart Compares values as points connected by lines. Bar Chart Compares values displayed as horizontal columns. Area Chart Compares values displayed as shaded areas. Pie Chart Compares values displayed as slices of a circular
                                        graph KPI Card Displays the report metrics in real-time. The output type
                                        generated is Card. When converting an existing visualization to a KPI
                                                card, ensure the first profile variable is correctly
                                                set, as other variables will not be rendered on the
                                                card. Sparkline Chart Table-based rendering of variations of data displayed in
                                        a highly condensed way as miniature charts in table cells,
                                        enabling you to spot trends. To provide a more consistent experience across Webex Contact Center, we
                            are standardizing the visual design and formatting options in Analyzer.
                            The overall experience remains the same. You can continue to create,
                            view, and use reports and dashboards as you do today. The update is
                            primarily visual, with only a few minor formatting options being
                            streamlined to align with Webex design standards. Formatting Options In the new visual design, to maintain consistency across all Webex
                            products, we have updated the available formatting options. Please refer
                            to the list below for details on supported and removed features: Supported Title Options: Font Size and Text Align Supported Chart Options : Gradient Fill, Stacking, Axis
                                Labels, Invert Axis, Data Labels and Data labels rotation. The following properties have been removed or are no longer supported as
                            manual customizations: Unsupported Title Options: Back Color, Border Size, Border
                                Style, Border Color, Font Family, Font Style, Font Weight, Text
                                Color, Text Decoration, Margin Top, Margin Bottom, Margin Left,
                                Margin Right, Padding Top, Padding Bottom, Padding Left and Padding
                                Right. Unsupported Chart Options: Back Color, Border Size, Border
                                Style and Border Color. Some of these unsupported formatting options may still appear temporarily
                            in the updated look, but they will not be applied when reports and
                            dashboards are viewed. They will continue to work in the previous look
                            until it is retired. The previous look will remain available for a limited time. Once it is
                            retired, these unsupported formatting options will also be fully
                            retired. Motion Charts are no longer supported. When you create a new report, the Motion
                                    Chart option is unavailable in the Output
                                    Type drop-down list. When you edit an existing Motion Chart report, the Motion
                                    Chart option appears in gray in the Output Type drop-down list. Save and Preview options are unavailable. When you run an existing Motion Chart report, the UI displays the
                                following error: Unable to render Motion Charts
                                    because it’s no longer supported. Save the report in a different
                                    format. | Format | Description | Table | Displays data in rows and columns. | Heat Map | Displays the cell values within a table in different
                                            shades of red. The cells in white and the darkest shade of red identify
                                            the outliers. Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Heat Maps for such reports. | Row Heat Map | Displays the cell values within each row in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a row. Row Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Row Heat Maps for such reports. | Column Heat Map | Displays the cell values within each column in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a column. | Line Chart | Compares values as points connected by lines. | Bar Chart | Compares values displayed as horizontal columns. | Area Chart | Compares values displayed as shaded areas. | Pie Chart | Compares values displayed as slices of a circular
                                        graph | KPI Card | Displays the report metrics in real-time. The output type
                                        generated is Card. When converting an existing visualization to a KPI
                                                card, ensure the first profile variable is correctly
                                                set, as other variables will not be rendered on the
                                                card. | Sparkline Chart | Table-based rendering of variations of data displayed in
                                        a highly condensed way as miniature charts in table cells,
                                        enabling you to spot trends. |
| Format | Description |
| Table | Displays data in rows and columns. |
| Heat Map | Displays the cell values within a table in different
                                            shades of red. The cells in white and the darkest shade of red identify
                                            the outliers. Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Heat Maps for such reports. |
| Row Heat Map | Displays the cell values within each row in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a row. Row Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Row Heat Maps for such reports. |
| Column Heat Map | Displays the cell values within each column in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a column. |
| Line Chart | Compares values as points connected by lines. |
| Bar Chart | Compares values displayed as horizontal columns. |
| Area Chart | Compares values displayed as shaded areas. |
| Pie Chart | Compares values displayed as slices of a circular
                                        graph |
| KPI Card | Displays the report metrics in real-time. The output type
                                        generated is Card. When converting an existing visualization to a KPI
                                                card, ensure the first profile variable is correctly
                                                set, as other variables will not be rendered on the
                                                card. |
| Sparkline Chart | Table-based rendering of variations of data displayed in
                                        a highly condensed way as miniature charts in table cells,
                                        enabling you to spot trends. |

| Format | Description |
|---|---|
| Table | Displays data in rows and columns. |
| Heat Map | Displays the cell values within a table in different
                                            shades of red. The cells in white and the darkest shade of red identify
                                            the outliers. Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Heat Maps for such reports. |
| Row Heat Map | Displays the cell values within each row in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a row. Row Heat Maps cannot be generated for raw reports (reports without row or column segments) or for reports that only have row segments. The Output Type drop-down list does not provide an option to generate Row Heat Maps for such reports. |
| Column Heat Map | Displays the cell values within each column in a table in
                                            different shades of red, with the darkest shade
                                            identifying the highest values within a column. |
| Line Chart | Compares values as points connected by lines. |
| Bar Chart | Compares values displayed as horizontal columns. |
| Area Chart | Compares values displayed as shaded areas. |
| Pie Chart | Compares values displayed as slices of a circular
                                        graph |
| KPI Card | Displays the report metrics in real-time. The output type
                                        generated is Card. When converting an existing visualization to a KPI
                                                card, ensure the first profile variable is correctly
                                                set, as other variables will not be rendered on the
                                                card. |
| Sparkline Chart | Table-based rendering of variations of data displayed in
                                        a highly condensed way as miniature charts in table cells,
                                        enabling you to spot trends. |

| 1 | Select the type of visualization: Customer Session Record Customer Activity Record Agent Activity Record Agent Session Record |
|---|---|
| 2 | Specify the time period that you want the visualization to cover. This constrains the number of records that will be considered during execution of the visualization. |
| 3 | The compute interval for a historical report can be either time-based or sample-based. For a time-based visualization, select a time interval. For a sample-based visualization, specify the total number of records to be considered, the frequency (the number of records to be considered in each interval), the band (the number of records to be considered in each calculation), and whether or not the calculations will be cumulative. |
| 4 | Specify what you are trying to compare as part of the visualization. This can be to compare the performance of the different agents or entry points. The Analyzer allows segmentation only by fields and not by measures. For example, segmentation by Termination Type or Agent Name is allowed, segmentation by Call Count is not allowed. |
| 5 | Define the metrics you want to see in the visualization to compare the different segments. Profiling variables are always numeric values and can be created from either fields, measures, or other profiling variables. Field : Fields can be used to create counts of records that meet specified conditions. For example, you can create a profiling variable that will provide the count of records with a Termination Type equal to normal. Measure : Measures can be used to create summations, averages, or counts. Summations and averages require no additional input. Counts work the same way as fields, and thus require conditions to be specified. For example, using Revenue as the basis for a profiling variable allows you to create a sum of the revenue, an average of the revenue, or a count of records that have a revenue greater than, less than, or equal to a given amount. Existing Profile Variable : Profiling variables can be created from other profiling variables using arithmetic formulas. For example, if you already have a profiling variable named Average revenue containing the average of revenue and another profiling variable named Handled Calls containing the count of records where Termination Type equals normal, then you can create a profiling variable containing the average revenue per call using Average revenue divided by Handled Calls. |
| 6 | This step further limits the population set to include only the records that meet the conditions you specify. |
| 7 | A visualization can be displayed as a table or chart. The chart types currently supported are Bar, Pie, Line, Area, and Motion. Additionally, you can specify display options such as titles, colors, and border widths and styles. |
| 8 | Visualizations can be executed on demand, scheduled for a one-time execution, or scheduled to run periodically. Scheduled executions post their results to the specified email recipients as a CSV or a Microsoft Excel file attachment. For scheduled reports, the maximum file size for email attachments is 10
                            MB and the maximum number of columns supported is 2000. You can define the execution schedule in one of the following ways: Execute now : Use Run from the view page. Execute once and email : Use the Scheduler. Specify the time and email information. Recurrence : Use the Scheduler and specify the recurrence pattern (such as daily, at 9.00 AM). The filters in the Profile Variables and the filters in the left
                                pane on the Visualization page are different. The filters in the
                                profile variables are applicable only to the selected profile
                                variables of that visualization and not to the entire visualization.
                                The filters in the left pane on the visualization page are
                                applicable to the entire visualization. For reports with row segments, sorting of data can be done only
                                within the respective row segment group. For example, in the Agent
                                details report, the Agent Name is the first-row segment field. When
                                agent names are sorted in the first column, the data displayed in
                                the subsequent columns is associated only with the selected
                                agent. |

| 1 | Select Visualization > Create New > Visualization . The visualization creation page appears. The Modules tab displays two panels that you can expand or collapse by clicking a panel title. |
|---|---|
| 2 | Select an option from the Type drop-down list. The possible values are Customer Session Record , Customer Activity Record , Agent Activity Record , or Agent Session Record . You can add variables and segments to the reports. |
| 3 | Specify the visualization time period by selecting an option from the Start Time drop-down list in the Modules tab. To create a realtime visualization, select Realtime. To create a historical visualization, select a predefined date range. To specify custom start and end dates, select Custom . If you selected Realtime , go to 9 . If you selected Custom , select values from the Start Date and End Date drop-down lists. If you selected Exact Date , enter a date in the field that appears, or click in the field and then select a date from the calendar controls. If you selected one of the other options— Day of the Year , Day of the Month , 7 Days , Day of the Week , or Most Recent Day —use the controls that appear, to select the options you want. If you specify a lengthy date range, the visualization could take a long time to run. In this case, it might be preferable to schedule the visualization rather than running it in real-time. If the pre-defined date range you want to select is not available in the drop-down list, increase the compute interval. Small compute intervals (such as Hourly) with large date ranges (such as Last Month) result in more data than can be displayed. Therefore, such selections aren't allowed. |
| 4 | To edit a module label, select the label text and type a new label.click the Edit ( ) icon and on the Edit Module dialog, type a new label. |
| 5 | You can filter the date range by selecting an option from the Including drop-down list. The possible values are Days of a Week , Days of the Month , Weeks of the Month , or Months of the Year . Select the weekdays, days of the month, weeks, or months that you want the visualization to include. |
| 6 | For custom reports using relative time ranges like This Week or Last Week , you can define the day that you want to consider as the start of the week. Select the desired start day from the Start Day of the Week drop-down list (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). The default selection is Monday. If you select a compute interval of Weekly and specify a custom start day, the weekly interval begins on the selected start day of the week. Start Day of the Week option doesn’t apply if you use the custom option in the Start Time drop-down menu. |
| 7 | If you're creating a time-based visualization, select a time interval from the Interval drop-down list in the Compute panel. The possible values are: None , 15 Minutes , 30 Minutes , Hourly , Daily , Weekly , or Monthly . The available options vary depending on the length of the date range. Small compute intervals (such as 15 Minutes, 30 Minutes, or Hourly) aren't available if the specified date range is lengthy (such as Last Month). After selecting an interval in the Compute panel, the Enable Split Interval option becomes active. This enables users to split data by selecting a precise interval instead of mapping the time to the interval in which the interaction ends. You can view detailed agent activity, agent states, and agent durations across different time intervals, which can help optimize agent staffing, allocate workforce efficiently, and ensure high customer satisfaction. Here are the key points regarding this functionality: The Enable Split Interval check box is available for creating new custom reports, editing existing reports and copy of stock reports. You have the option to check or uncheck the Enable Split Interval check box as per the reporting needs. By enabling the check box, the report is accessible in small intervals of 15 minutes, 30 minutes, Hourly, Daily. By clearing the check box, the report continues to function as before. If the Enable Split Interval check box is not displayed, contact Cisco Support as the corresponding feature flag may have to be enabled. If the interval type is 'none', the Enable Split Interval check box is disabled. You will have to select the interval first to enable the check box. For new reports, the Enable Split Interval check box is enabled by default. This Split Interval option is available for storage record types of ASR only. You can toggle the checkbox in report design mode and run it again to apply/remove split interval for durations. While viewing a report with split interval enabled, a notification toaster informs you about split interval enabled for the report. The toaster redirects you to the Analyzer User Guide when you click learn more . For an agent, the Split Interval for a telephony channel is tied to a single channel ID during a specific time interval, and the total idle duration will always be less than the selected interval. For example, in a 15-minute time interval, the idle duration will always be under 15 minutes. On the other hand, for non-telephony channels like email, chat, or social media, there can be multiple channel IDs within the selected interval, and the idle duration can exceed the chosen interval. For example, in a 15-minute interval, the idle duration may be greater than 15 minutes since the aggregated idle time spans multiple channel IDs. In such scenarios, you can drill down into the idle duration to view details about the different channel IDs the agent was working with during the selected interval. |
| 8 | If you’re creating a sample-based visualization, select First or Last from the Records drop-down list in the Compute panel, and in the text box, enter the total number of records to be considered in the visualization. You can also define the following: Frequency : The number of records to be considered per interval. Band : The number of records to be considered per calculation. Cumulative : To calculate the number of records. |
| 9 | If you selected Realtime as the visualization time period, select values from the drop-down lists that become available in the Compute panel. Parameter Description Duration Select None for a snapshot of the current contact center activity. - OR - Select a specific time interval (of 5, 10, 15, or 30 minutes) for a view that looks back from the current moment to the most recent 5, 10, 15, or 30 minutes. - OR - Select Start of Day for a view of all activities that occurred since midnight. - OR - Select Custom for a view that looks back from the current moment to up to 14 days in the past. Refresh Rate Select a value to specify how often the data in the visualization will be refreshed. If you have specified the duration as Start of Day or Custom, select Minutes; otherwise, select Seconds. Interval If you have specified the duration as Start of Day or Custom, the Interval drop-down list appears, enabling you to select a time interval (None, 15 Minutes, 30 Minutes, or Hourly). Look Back (D-H-M) If you have specified the duration as Custom, the Look Back settings appear. Enter the number of days, hours, and minutes from the current moment you want the visualization to look back to. You can specify up to 14 days. | Parameter | Description | Duration | Select None for a snapshot of the current contact center activity. - OR - Select a specific time interval (of 5, 10, 15, or 30 minutes) for a view that looks back from the current moment to the most recent 5, 10, 15, or 30 minutes. - OR - Select Start of Day for a view of all activities that occurred since midnight. - OR - Select Custom for a view that looks back from the current moment to up to 14 days in the past. | Refresh Rate | Select a value to specify how often the data in the visualization will be refreshed. If you have specified the duration as Start of Day or Custom, select Minutes; otherwise, select Seconds. | Interval | If you have specified the duration as Start of Day or Custom, the Interval drop-down list appears, enabling you to select a time interval (None, 15 Minutes, 30 Minutes, or Hourly). | Look Back (D-H-M) | If you have specified the duration as Custom, the Look Back settings appear. Enter the number of days, hours, and minutes from the current moment you want the visualization to look back to. You can specify up to 14 days. |
| Parameter | Description |
| Duration | Select None for a snapshot of the current contact center activity. - OR - Select a specific time interval (of 5, 10, 15, or 30 minutes) for a view that looks back from the current moment to the most recent 5, 10, 15, or 30 minutes. - OR - Select Start of Day for a view of all activities that occurred since midnight. - OR - Select Custom for a view that looks back from the current moment to up to 14 days in the past. |
| Refresh Rate | Select a value to specify how often the data in the visualization will be refreshed. If you have specified the duration as Start of Day or Custom, select Minutes; otherwise, select Seconds. |
| Interval | If you have specified the duration as Start of Day or Custom, the Interval drop-down list appears, enabling you to select a time interval (None, 15 Minutes, 30 Minutes, or Hourly). |
| Look Back (D-H-M) | If you have specified the duration as Custom, the Look Back settings appear. Enter the number of days, hours, and minutes from the current moment you want the visualization to look back to. You can specify up to 14 days. |
| 10 | To specify either Row Segments or Column Segments, click the Add Row Segments or Column Segments icon. Drag and drop a field or an enhanced field listed in the canvas area. Repeat this step for each segment that you want to add. Fields can be added as either Row Segments or Column Segments . For charts, only the first segment is used. High cardinality fields such as Contact Session ID and Agent Session ID contain a large set of unique values. When you select these fields as row or column segments while creating a new report or modifying an existing report, a large amount of data is fetched. To avoid this, a pop-up prompts you to add specific filters to decrease the amount of data fetched. You can also ignore the message and continue to save the visualization. The prompt appears when you select the high cardinality fields as a row or column segment. You can resolve it by adding more filters to decrease the amount of data. |
| 11 | To combine multiple values of the segmentation variable into one group, you can create an enhanced field: Right-click a value and select Create Enhanced Field . Specify the settings for one or more groups in the dialog box that
              appears. For example, you could create three groups of entry points where each group
              represents a different product line or a different business unit. |
| 12 | To create a profile variable: Click the Add Profile Variable icon. Drag and drop a field, measure, or formula listed in the New Profile Variable dialog box and do one of the following: Type a name for the profile variable in the Name text box or leave the default text. This name will be displayed in the column header and axis labels. If you used a field to create the profile variable, you can specify the records that you want to include in the count by dragging an item from the Fields list to the Filters area of the New Profile Variable dialog box and selecting the records to be included. For more information, see Filter Using a Field . If you used a measure to create the profile variable, select the computation that you want to perform from the Formula drop-down list. For more information, see Select a Formula for a Measure . You can specify a condition for including records by dragging an item from the Fields or Measures lists to the Filters area of the dialog box. For more information, see Filter Using a Measure . You can also create a new formula based on a profile variable that exists in the visualization. You can also create a new formula based on a profile variable that exists in the
                visualization. If you selected a Global Variable as the profile variable, only the selected
                Global Variable from the Fields or Measures lists can be used as a filter of the profile
                variable. For more information about Global Variables (previously known as
                Call-Associated Data variables), see the Contact Routing chapter in the Cisco Webex Contact Center Setup and
                    Administration Guide . |
| 13 | To specify the format for the profile variable, click on the right-click the profile variable and select the Number Format option from the context menu. For more information, see Format a Profile Variable . For example, if you created a Conversion Rate profile variable, you could select Percentage as the format. |
| 14 | Continue creating as many profile variables as you want. In the following example, three profile variables have been created and the data is segmented under Queue ID and Agent Name header rows. If you’re creating a motion chart, you must include at least three profile variables. To change the order of a profile variable or segment, drag its label to a different position. To pivot across column and row segments, drag a segment label from the Column Segments box to the Row or Series Segments box, or the opposite way. To remove a profile variable, click on the Edit icon or right-click the profile variable and select Delete . You can’t remove a profile variable used in another profile variable. |
| 15 | To show or hide the summary of column values at the table level and the top-level row segment, select the values from the Show Summary drop-down list. |
| 16 | To define the summary of column values at the table level and the top-level row segment, click Customize . For more information on Customize Report Summary , see Customize Report Summary . |
| 17 | To find out approximately how large the visualization is when it’s run, save the visualization and click More and select the Info button. |
| 18 | You can create a filter to limit the number of records that the visualization considers by default. To create a filter: Click Add Filter in the Modules tab. Select a field or measure from the displayed lists and click Save . - OR - Right-click a segment in the visualization and select Create Filter . When the new filter appears in the Modules tab, specify which values to include or exclude or, in the case of a measure, set a condition that the data must satisfy. You can’t select more than 1000 values inside a field for a filter. If you've selected more than 1000 values, an error message appears. To remove a value, use the X button. |
| 19 | Specify a visualization output format. For more information, see Change the Visualization Output Format You can now choose a KPI Card as one of the output type. Only the first profile
              variable is used when rendering a KPI Card. To refer the possible output format types,
              see Change the Visualization Output Format . |
| 20 | Navigate to Formatting Tab and click on Set Color Conditions to apply the
          color conditions in the pop up. You can apply conditional formatting to a table or KPI cards to change the value
              color based on performance. When using this feature for a KPI card, the color rule
              applies to the aggregated result of the first profile variable only. For more
              information refer Format a Table . |
| 21 | If you’re creating a compound visualization, add at least one additional module before you save the visualization. |
| 22 | To save the visualization, click the Save button, and in the dialog box that appears: Select the folder. To create a new folder, click New Folder , and enter a name for the folder. Enter a name for the visualization and click OK . |
| 23 | Click Preview to view the visualization. If you're creating visualization of the Customer Session
                Record type, where Interval is used as Row Segment and Contact Start
                Timestamp and Contact End Timestamp are used as Profile Variables from the Measures drop-down list, select Minimum Contact Start Timestamp for Contact Start Timestamp and Maximum Contact End
                Timestamp in the Formula drop-down list. |

| Parameter | Description |
|---|---|
| Duration | Select None for a snapshot of the current contact center activity. - OR - Select a specific time interval (of 5, 10, 15, or 30 minutes) for a view that looks back from the current moment to the most recent 5, 10, 15, or 30 minutes. - OR - Select Start of Day for a view of all activities that occurred since midnight. - OR - Select Custom for a view that looks back from the current moment to up to 14 days in the past. |
| Refresh Rate | Select a value to specify how often the data in the visualization will be refreshed. If you have specified the duration as Start of Day or Custom, select Minutes; otherwise, select Seconds. |
| Interval | If you have specified the duration as Start of Day or Custom, the Interval drop-down list appears, enabling you to select a time interval (None, 15 Minutes, 30 Minutes, or Hourly). |
| Look Back (D-H-M) | If you have specified the duration as Custom, the Look Back settings appear. Enter the number of days, hours, and minutes from the current moment you want the visualization to look back to. You can specify up to 14 days. |

| 1 | To add a module during visualization creation, click Add at the top of the Modules tab. In the dialog box that appears, enter a name for the module and click OK . Click Add again for each additional module you
            want to add. After adding a module, the visualization creation page displays the constituent visualizations side by side. You can select different date ranges, intervals, and filters for each module. Choose an interval value other than None . If None is chosen, the interval values are displayed as belonging to the year 1970. |
|---|---|
| 2 | To display the settings that can be customized for each module, select a module from the drop-down list at the top of the Modules tab. |
| 3 | To edit a module label, select the label text and type a new label.click the Edit ( ) icon and on the Edit Module dialog, type a new label. The drop-down list in the Modules tab reflects the label changes. |

| Setting | Description |
|---|---|
| Default Group | Enter a name (for example, Other Entry Points) for the group that includes all the variables not included in the defined groups. |
| Groups | To define a group, enter a name in the Group Name : Select values from the drop-down list. Type a value and then press Enter . |

| Setting | Description |
|---|---|
| Default Group | Enter a name (for example, Other Entry Points) for the group that includes all the variables not included in the defined groups. |
| Groups | To define a group: Enter a name in the Group Name field. To select a skill: Select a skill from the Select Skill drop-down list. Select an operator from the Select Operator drop-down list. Select an existing value or create a new value by typing it in the Select Values box and then press Enter . Between skills, ‘AND’ operator is applicable. You can add up to 1000 skills. To add more groups: Click on the + icon to add another group. Across the groups, ‘OR’ operator is applicable. You can create up to 100 groups. |

| Formula | Calculates |
|---|---|
| Average | The average value. |
| Sum | The total value. |
| Count | The number of values. When you select this formula, the dialog box displays settings for specifying a condition for including records in the count. For more information, see Filter Using a Measure . |
| Minimum | The smallest value. |
| Maximum | The largest value. |
| Value of | The actual value in the database without aggregation. |
| Geometric Mean of | The nth root (where n is the count of numeric values within the specified range) of the product of the values. |
| Kurtosis of | The measure of whether the data are peaked or flat relative to a normal distribution. |
| Median | The middle value. |
| Population Variance of | Variance of the set of unique values. |
| Skewness of | How far the median is from the mean. |
| Standard Deviation of | The square root of the variance. |
| Sum of Squares | The sum of the squares of the values. |
| Variance of | The average of the squared differences between each value and the mean value. |

| Scenario | Regex | Description |
|---|---|---|
| Filter out N/A | .+ | If you want to exclude all records that are marked as "N/A" ,
                          then you may use the Filter out N/A scenario. For example, use a
                        regex pattern to ignore entries where the field value is "N/A". |
| Filter everything else and keep N/A | Not Supported Currently | Currently, there is no RegEx-based method available to filter exclusively
                          for 'N/A' values. |
| Filter based on an exact match (one or more values) | Avoid Regex | If you want to filter for one or more specific values exactly ,
                          then you may use the Exact match approach. For example, contains <Agent Name> Note: It is recommended to use
                          the 'contains' function instead of regex for better performance. |
| Filter based on partial match | .*<keyword.>* | If you want to find records that contain a specific word or
                            phrase anywhere within the text , then you may use the Partial
                            match scenario. For example, .*Team.* Use a pattern like
                        .*<keyword>.* to capture any record containing that keyword. |
| Case insensitive match | .*[][][][].* | If you want to find matches regardless of whether the text is
                            uppercase or lowercase , then you may use the Case insensitive
                            match scenario. For example, .*[Ee][Aa][Ff][Mm].* Use a pattern
                        like .*[Ee][Aa][Ff][Mm].* to match any record containing "eafm" in any
                        combination of uppercase or lowercase letters ensure to filter data
                        regardless of uppercase or lowercase characters. |
| Prefix match | <keyword>-.+ | If you want to find all items that begin with a specific
                            prefix , then you may use the Prefix match scenario. For
                        example, team-.+ to filter for all teams that start with prefix "team-"
                        followed by one or more characters. Use a pattern like <keyword>-.+ to
                        filter data that starts with a specific pattern by placing .+ at the
                        end. |
| Suffix match | .+<keyword> | If you want to find all records that end with a specific
                            identifier , then you may use the Suffix match scenario. For example, Use .+_LOC to capture all records that end with
                        the suffix "_LOC". Use a pattern like -.+<keyword> to filter data that
                        ends with a specific pattern by placing .+ at the start. |

| Option | Description |
|---|---|
| Back Color | Select the background color from the color selector or enter the HTML (hexadecimal) code for a color. |
| Border Size | Enter a value in pixels to change the border width. |
| Border Style | Select a value from the drop-down list to specify the style of the border around the table or select None if you do not want a border around the table. |
| Border Color | Select the border color from the color selector or enter the HTML code for a color. |

| Option | Description |
|---|---|
| Caption | To change the caption, click the caption text that's displayed in the Formatting tab to select it, and enter
                                the required caption. This setting is available only in the Formatting tab. Right-click to specify whether you want the data to
                                be formatted as Integer, Number, Currency, Percentage, Date Time, or
                                Duration, and within that category, specify how you want the data to
                                be displayed. |
| Number Format | For example, when you select Percentage, you can
                                select one of the following format options: ##.##% (12.34%) ##% (12%) When you select Duration, you can select one of the following format options: MM:SS (04:35) M:SS (4:35) HH:SS:SS (04:35:15) H:MM:SS (4:35:15) HH:MM (04:35) MM:SS.sss (04:35.200) HH:MM:SS.sss (04:35:15.200) |
| Text Align | To change the alignment of the column text, select a
                                value from the drop-down list: Left, Center, or Right. This setting is available only from the context
                                menu. |

| 1 | Right click the Interval field to display the Select Date Format context menu. |
|---|---|
| 2 | Select the required date format from the following list: mm/dd/yyyy mm/dd/yy m/d/y dd/mm/yy d/m/y yyyy/mm/dd yyyy-mm-dd |
| 3 | Click Save . If you export a report in the .csv format and open it in Microsoft Excel, the date is displayed according to the date format that is set in Microsoft Excel. To display the dates in the exact date format that you applied for the Interval field in the visualization, open the exported CSV report in a text editor. |

| Option | Description |
|---|---|
| Back Color | Select the background color from the color selector or enter the HTML code for a color. |
| Border Size | Enter a value in pixels to change the width of the border around the chart. |
| Border Style | Choose a value from the drop-down list to specify the style of the border around the chart or select None if you do not want a border. |
| Border Color | Select the border color from the color selector or enter the HTML code for a color. |
| Gradient Fill | To add a shade pattern to the lines, areas, or bars in a line, area, or bar chart, select the direction of the color gradient from the drop-down list. |
| Stacking | To display data values stacked on top of each other in a line, area, or bar chart, select Normal to stack by the data values or Percent to stack by percentages. |
| Axis Labels | Select a value from the drop-down list to specify whether to show or hide axis labels. |
| Invert Axes | Select either True or False from the drop-down list to specify whether or not to invert the axes. |
| Data Labels | Select a value from the drop-down list to specify whether to show or hide the data labels. |
| Data Labels Rotation | Select a value from the drop-down list to specify the data label rotation angle: None, 45°, 90°, or -90°. |

| Formula | Calculation |
|---|---|
| NONE | No formulas are defined for the column summary. If you select NONE for all the columns in a visualization, you cannot see the table level or group level summary. |
| AVG | The average of the values in the column. |
| COUNT | The count of records in the column with values other than null. |
| MIN | The smallest value in the column. |
| MAX | The largest value in the column. |
| SUM | The sum total of all the values in the column. |
| You can also select the predefined formula to calculate only the table level
                  summary for the column that has a formula field. AVG is disabled for division-based custom formula fields in Customize Report
                  Summary |