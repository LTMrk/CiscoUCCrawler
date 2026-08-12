[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/admin/docs/admin)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/admin/docs/admin)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/admin/docs/admin)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Overview
Webex Admin
  * [Overview](https://developer.webex.com/admin/docs/admin)
  * [Authentication](https://developer.webex.com/admin/docs/authentication)
  * Service Apps
  * Guides
  * API REFERENCE
  * All APIs
  * [Changelog](https://developer.webex.com/admin/docs/api/changelog/webex-admin)
  * [AI Assistant for Developers](https://developer.webex.com/admin/docs/webex-aI-assistant-for-developers)
  * [Troubleshoot the API](https://developer.webex.com/admin/docs/api/guides/troubleshooting)
  * [Suite Sandbox](https://developer.webex.com/admin/docs/developer-sandbox-guide)


## Webex Admin
### Overview
Manage Webex users, licenses, and hybrid services programmatically with the Webex Admin APIs.
####  anchorWhat's Possible with Admin APIs
anchor
The Webex APIs include several APIs that allow administrators to programmatically perform administrative actions such as provisioning a user or assigning a license to a user. By automating administration, user management and provisioning can be performed from an existing tool, rather than using the [Webex Control Hub](https://admin.webex.com).
Using these APIs, an admin can, for example:
  * [Create a user](https://developer.webex.com/docs/api/v1/people/create-a-person)
  * [Update a user](https://developer.webex.com/docs/api/v1/people/update-a-person)
  * [View license usage of an organization](https://developer.webex.com/docs/api/v1/licenses/get-license-details)
  * [View available roles of an organization](https://developer.webex.com/docs/api/v1/roles/list-roles)
  * [Manage Hybrid Services licenses and users](https://developer.webex.com/docs/api/guides/managing-hybrid-services-licenses)
  * [View information about Hybrid Clusters](https://developer.webex.com/docs/api/v1/hybrid-clusters) or [Hybrid Connectors](https://developer.webex.com/docs/api/v1/hybrid-connectors)


If your organization uses the [Cisco Directory Connector](https://www.cisco.com/go/hybrid-services-directory) to synchronize Webex user accounts with Active Directory accounts, then you cannot _create_ or _delete_ Webex users using the [People API](https://developer.webex.com/docs/api/v1/people). Additionally, the People API will not allow you to _update_ any attributes of your existing users that are being synchronized by the Directory Connector.
####  anchorAdmin Audit Events
anchor
Full administrators for an organization can use the [Admin Audit Events API](https://developer.webex.com/docs/api/v1/admin-audit-events) to retrieve information about significant actions taken by administrators in Webex Control Hub. See [this article](https://help.webex.com/n3b0w6x/) for detailed information about the types of events you can retrieve.
Administrators with accounts created before 2019 who have never logged into [Webex Control Hub](https://admin.webex.com/) will need to log into Webex Control Hub at least once to enable access to the [Admin Audit Events API](https://developer.webex.com/docs/api/v1/admin-audit-events).
####  anchorAuthentication
anchor
Use of these APIs requires you to be an administrator of an organization. If you are not an administrator of an organization, but wish to develop against these APIs, see below for instructions on how to get administrator access to an Administration Sandbox organization.
If you are an administrator, log into this site to get a development auth token with the necessary scopes.
To create an [Integration](https://developer.webex.com/docs/integrations) that will act on behalf of an administrator, include one or more of the following scopes when requesting an auth token via OAuth:
Scope
Usage
`spark-admin:messages_write`
Access to delete messages in all rooms/spaces in your user\'s organization. New integrations, please use spark-compliance:messages_write instead
`spark-admin:messages_read`
Access to read messages in all spaces in your user's organization. New integrations, please use spark-compliance:messages_read instead
`spark-admin:calling_cdr_read`
Access comprehensive Call Detail Records for Webex Calling, including PII-protected phone numbers.
`spark-admin:broadworks_subscribers_write`
Provision, Update or Remove a BroadWorks Subscriber as part of Webex for BroadWorks Solution.
`spark-admin:broadworks_subscribers_read`
Read or List BroadWorks Subscribers, provisioned as part of Webex for BroadWorks Solution.
`spark-admin:broadworks_enterprises_write`
Change BroadWorks Enterprise configuration, provisioned as part of Webex for BroadWorks Solution.
`spark-admin:broadworks_enterprises_read`
Read or List BroadWorks Enterprise, provisioned as part of Webex for BroadWorks Solution.
`spark-admin:people_write`
Access to write to your user's company directory
`spark-admin:people_read`
Access to read your user's company directory
`spark-admin:licenses_read`
Access to read licenses available in your user's organizations
`spark-admin:roles_read`
Access to read roles available in your user's organization
`spark-admin:workspaces_read`
See details for your workspaces
`spark-admin:places_write`
Create, update and delete any place and place service in your organization
`spark-admin:places_read`
See details for any places and place service in your organization
`spark-admin:locations_write`
Create and edit location configuration.
`spark-admin:locations_read`
Read and list location configuration.
`spark-admin:devices_write`
Create, update and delete devices and device configurations in your organization
`spark-admin:devices_read`
See details for any device in your organization
`spark-admin:organizations_read`
Access to read your user's organizations
`spark-admin:resource_groups_read`
Access to read your organization's resource groups
`spark-admin:resource_group_memberships_write`
Access to update your organization's resource group memberships
`spark-admin:resource_group_memberships_read`
Access to read your organization's resource group memberships
`spark-admin:hybrid_clusters_read`
Access to read hybrid clusters for your organization
`spark-admin:hybrid_connectors_read`
Access to read hybrid connectors for your organization
`spark-admin:calls_read`
Access to list all calls in your user's organization
####  anchorReports API
anchor
The [Webex Reports API](https://developer.webex.com/docs/api/v1/reports) is available for Organizations with [Pro Pack for Cisco Webex Control Hub](https://www.cisco.com/go/pro-pack). The `analytics:read_all` scope is required to work with reports.
Reports are only visible to the user who created the report. Each user is limited to 50 reports. If a user tries to create more than 50 reports, an error will be returned by the API. See below for errors you may encounter from the API.
###### Using the Reports API
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltb39d7513c0c01b11/5f05c051e5f0487064a76689/Webex-Reports-Flow.png)
  1. [List Report Templates](https://developer.webex.com/docs/api/v1/report-templates)
First, list the available report templates. These templates are available for you to use when creating a report.
  2. [Create the Report](https://developer.webex.com/docs/api/v1/reports/create-a-report)
Determine which template you want to use to create the report. Specify the date range for the report when creating it.
After creating the report, make note of the `id` returned. This is the report's ID. You will need this later to download it.
  3. [Check the Report's Status](https://developer.webex.com/docs/api/v1/reports/get-report-details)
While the report is generated, you can check on the status of the report by retrieving the report with the ID you noted in the previous step.
  4. [Download the Report](https://developer.webex.com/docs/api/v1/reports/get-report-details)
When the report is ready, use the download link in the response to download the report. The maximum number of downloads is 30.
Downloaded reports are automatically deleted after 24 hours following the final download.
  5. [Delete the Report](https://developer.webex.com/docs/api/v1/reports/delete-a-report)
Organizations may keep up to 50 reports at any time. After you've created and downloaded your report, delete it to make room for the next report.


###### Reports API Errors
If you encounter an error when creating a report, the response will include an `ErrorCode`. See below for more information about the error.  
| HTTP Code  | ErrorCode  | Description  |  
| --- | --- | --- |  
| 400  | 1000  | Reach the limit for creating reports  |  
| 400  | 1001  | Report Template ID not found  |  
| 400  | 1002  | Over the maximum date selection allow  |  
| 400  | 1003  | No access to sites that you do not belong to  |  
| 400  | 1004  | SiteUrl cannot be empty for site level template  |  
| 400  | 1008  |  `reportId` does not exist  |  
| 400  | 1009  | [field required for validation, for example: templateId, siteList, etc ] can not be empty!  |  
| 400  | 1016  | Either none or both of `from` and `to` query parameter must be present in request  |  
| 401  | 1010  | Authorization token not provided  |  
| 401  | 1011  | Authorization token wrong or expired  |  
| 401  | 1012  | Feature toggle not enabled  |  
| 401  | 1014  | The user does not have allowed role  |  
| 401  | 1018  | CI Access Token or scope of the token is not valid!  |  
| 403  | 1005  | Not allow to generate ui report by api  |  
| 403  | 1006  | Not allow to delete others report  |  
| 429  | 1007  | Number of downloads for this report has reached the limit within 24 hrs  |  
####  anchorDeveloper Sandbox
anchor
If you would like to develop against the Admin APIs but you are not an administrator of your Webex Organization, you can [request a Developer Sandbox](https://developer.webex.com/docs/developer-sandbox-guide). A Developer Sandbox provides you with a Webex administrator account for a "dummy" organization you can use to develop and test bots, integrations, and embedded apps outside of your primary organization.
For more information and to request a Developer Sandbox organization see the [Developer Sandbox Guide](https://developer.webex.com/docs/developer-sandbox-guide).
##### In This Article
  * [What's Possible with Admin APIs](https://developer.webex.com/admin/docs/admin#whats-possible-with-admin-apis)
  * [Admin Audit Events](https://developer.webex.com/admin/docs/admin#admin-audit-events)
  * [Authentication](https://developer.webex.com/admin/docs/admin#authentication)
  * [Reports API](https://developer.webex.com/admin/docs/admin#reports-api)
  * [Developer Sandbox](https://developer.webex.com/admin/docs/admin#developer-sandbox)


## Connect
[Support](https://developer.webex.com/support)
[Developer Community](https://community.cisco.com/t5/webex-for-developers/bd-p/disc-webex-developers)
[Developer Events](https://developer.webex.com/blog/categories/events)
[Contact Sales](https://www.webex.com/contact-sales.html?TrackID=1017639&hbxref=&goid=us_contact_sales)
## Handy Links
[Webex Ambassadors](https://www.essentials.webex.com/programs/ambassadors)
[Webex App Hub](https://www.essentials.webex.com/programs/ambassadors)
## Resources
[Open Source Bot Starter Kits](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[Download Webex](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[DevNet Learning Labs](https://www.webex.com)
[Terms of Service](https://developer.webex.com/terms-of-service)
[Privacy Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html)
[Cookie Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html#cookies)
[Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
© 2026 Cisco and/or its affiliates. All rights reserved.
[](https://github.com/webex)[](https://www.facebook.com/CiscoCollab/)[](https://twitter.com/webexdevs)[](https://www.youtube.com/playlist?list=PL2k86RlAekM_bIUrvVw4Haq_0xxTez9zU)[](https://www.linkedin.com/company/webex/)
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
