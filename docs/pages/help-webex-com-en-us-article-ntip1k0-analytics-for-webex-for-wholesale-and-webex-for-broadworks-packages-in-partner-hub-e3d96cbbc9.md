---
doc_id: help-webex-com-en-us-article-ntip1k0-analytics-for-webex-for-wholesale-and-webex-for-broadworks-packages-in-partner-hub-e3d96cbbc9
source_url: https://help.webex.com/en-us/article/ntip1k0/Analytics-for-Webex-for-Wholesale-and-Webex-for-Broadworks-packages-in-Partner-Hub
retrieved_at: 2026-09-07T12:43:48.554602+00:00
---

## View analytics

Partner Hub uses charts and tables to show you how your Webex for Cisco BroadWorks or Wholesale RTM customers are adopting Webex. The following table lists which kinds of
        data are available to which administrator roles.

Charts are available in a daily, weekly, and monthly format, or you can select a custom date range with the calendar date selector. You have access to 13 months of data. All charts are in Greenwich Mean Time (GMT).

Things to keep in mind

- No data is available before January 26, 2022. Partner admins can only filter for date ranges after that date.

- Due to data not being available, percentage changes won't be shown for comparison before January 26, 2022.

- Data refresh happens every 24 hours in a nightly batch process during UTC time.

- All partners can see all packages in the Customers with # of packages assigned table. This will be fixed in later phases so Broadworks partners and Whole partners can only see their respective packages correctly.

- The numbers shown for the Total customers and Total users KPIs are based on the last day of the date range that you select.

- Filter values are case sensitive

- Customers count may be different between the Analytics and Customer list.

- If a partner organization is a customer itself, then that count isn't added in the Total customers KPI.The partner can sign in to the Control Hub organization to view its own organization's analytics.

- Filters will show all packages by default.

These analytics data are for your general use and shouldn't be used for billing
          purposes.

Sign in to Partner Hub at https://admin.webex.com .

Select Analytics .

Select which date range you want to view the data for with the calendar date selector.

If applicable, you can change the date period for a chart: Daily , Weekly , or Monthly .

To save an individual chart, choose a chart, click the more button, and then choose a file type.

If you choose CSV, you'll export all of the data for the selected chart. If you select PNG or PDF, you get a copy of the data shown on the screen only.

## Charts and graphs

### Region selector

Customer data is maintained in their organization's region. You must select a specific
        region to view customer data within those regions.

Customer results in the region selector are determined by the provisioning region of
          their organization, rather than the physical locations of the customers.

### KPIs

KPIs are available at the top of the page to show you high level details about your customers. You can use these KPIs as measurable data to see how your customers are doing. The KPIs available are:

- Total customers —The total number of customers that you're managing.

- Total users —The total number of users in all of your customers' organizations that you manage. You can use this KPI to see if your customers are utilizing the packages that they bought by comparing this number with the number in the Total users by packages chart.

- New customers added —The number of customers that were recently assigned to you to manage.

### Packages assigned

This chart shows you the number of packages that your customers have assigned. You can use
        this chart to see if your customers are assigning the packages that they've bought. Packages
        for Webex for Cisco BroadWorks and Webex for Wholesale are:

For more
            information about these packages, see this article .

- Webex Wholesale — Attendant Console, Common Area Calling, Enhanced
          Calling, Customer Assist, Webex Calling, Webex Calling Standard, Webex Voice, Webex Suite,
          and Webex Meetings.

### Package assignment trend

This chart shows a trend of the packages that your customers assigned over time.

### Customers with # of packages assigned

This list shows you the customers with the most packages assigned to their users. You can use this list to see which customers are assigning their packages to users and compare them with the customers that aren't assigning all of their packages. The details available are:

- Total —The total number of packages that customers have assigned to users.

- Basic —The number of Webex for Broadworks basic packages assigned to users.

- Standard —The number of Webex for Broadworks standard packages assigned to users.

- Premium —The number of Webex for Broadworks premium packages assigned to users.

- Softphone —The number of softphone packages assigned to users.

- Attendant Console —The number of Attendant Console packages
          assigned to users.

- Common Area Calling —The number of non-user packages assigned to common areas.

- Customer Assist —The number of Customer Assist packages assigned to
          users.

- Enhanced Calling —The number of Enhanced Calling packages assigned to users.

- Webex Calling —The number of Webex Calling packages assigned to users.

- Webex Calling Standard —The number of Webex Calling Standard
          packages assigned to users.

- Webex Suite —The number of Webex Suite packages assigned to users.

- Webex Meetings —The number of Webex Meetings packages assigned to users.

- Webex Voice —The number of Webex Voice assigned to users.

The number of packages shown are only ones that have been assigned to users, not the total number of packages that they've bought.

| Partner Org | Partner admin role | Customer List | Create Paid Customer | Manage wholesale customers | Manage flex customers | Administrators | Templates | Analytics |
|---|---|---|---|---|---|---|---|---|
| Non-wholesale enabled | Partner full admin | Can view all | No | No | Yes | Yes | No | No |
|  | Partner admin | Can view partial | No | No | Yes | No | No | No |
|  | Partner read-only admin | Can view all | No | No | Yes | Read-only | No | No |
| Wholesale enabled | Partner full admin | Can view all | No | Yes | Yes | Yes | No | Yes |
|  | Partner full admin and Webex for Wholesale admin | Can view all | Yes | Yes | Yes | Yes | Yes | Yes |
|  | Partner admin | Can view partial | No | Yes | Yes | No | No | No |
|  | Partner read-only admin | Can view all | No | Read-only | Read-only | Read-only | No | Yes |
| BroadWorks enabled | Partner full admin | Can view all | No | No | No | No | No | Yes |
|  | Partner admin | Can view partial | No | No | No | No | No | No |
|  | Partner read-only admin | Can view all | No | No | No | No | No | Yes |

| 1 | Sign in to Partner Hub at https://admin.webex.com . |
|---|---|
| 2 | Select Analytics . |
| 3 | Select which date range you want to view the data for with the calendar date selector. |
| 4 | If applicable, you can change the date period for a chart: Daily , Weekly , or Monthly . |
| 5 | To save an individual chart, choose a chart, click the more button, and then choose a file type. If you choose CSV, you'll export all of the data for the selected chart. If you select PNG or PDF, you get a copy of the data shown on the screen only. |

| Package | Calling | Messaging | Space meetings | PMR meetings |
|---|---|---|---|---|
| Softphone | Included | Not included | None | None |
| Basic | Included | Included | 25 participants* | None |
| Standard | Included | Included | 100 participants | 100 participants |
| Premium | Included | Included | 300 participants | 1000 participants |