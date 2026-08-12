[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/meeting/docs/basics)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/meeting/docs/basics)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/meeting/docs/basics)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/REST API Basics
Webex Meetings
  * [Overview](https://developer.webex.com/meeting/docs/meetings)
  * Guides
  * [Guest to Guest Meetings](https://developer.webex.com/meeting/docs/guest-to-guest-meetings)
  * [API Behavior Changes](https://developer.webex.com/meeting/docs/app-programming-interface-behavior-changes)
  * [REST API Basics](https://developer.webex.com/meeting/docs/basics)
  * API REFERENCE
  * All APIs
  * [Changelog](https://developer.webex.com/meeting/docs/api/changelog/webex-meetings)
  * SDK
  * [AI Assistant for Developers](https://developer.webex.com/meeting/docs/webex-aI-assistant-for-developers)
  * [Troubleshoot the API](https://developer.webex.com/meeting/docs/api/guides/troubleshooting)
  * [Widgets](https://developer.webex.com/meeting/docs/widgets)
  * [Tutorials](https://developer.webex.com/meeting/docs/tutorials)
  * [Suite Sandbox](https://developer.webex.com/meeting/docs/developer-sandbox-guide)
  * [Beta Program Overview](https://developer.webex.com/meeting/docs/webex-developer-beta-program)
  * [Webex Status API](https://developer.webex.com/meeting/docs/webex-status-api)
  * [XML API Deprecation](https://developer.webex.com/meeting/docs/webex-xml-api-deprecation-announcement)


## Webex Meetings
### REST API Basics
While working with the Webex REST API is easy, there are a few things we standardize on throughout the API, such as pagination of long result sets or HTTP response codes.
####  anchorPagination
anchor
As adoption of Webex continues to grow, so does the amount of content being shared by team members. We've addressed this in the Webex APIs by including support for pagination.
It would be impractical to return all messages in a busy space, for example. With pagination, the Webex API returns a specific number of items at a time; allowing your app to request more items as needed.
###### Navigating Pages
The Webex APIs implement the [RFC5988 (Web Linking)](http://tools.ietf.org/html/rfc5988) standard for pagination. When requesting a list of resources the response may contain a `Link` header containing the URLs to the first, next, and previous page.
For example, requesting `GET /people?displayName=Harold` may return a link header like this one:

```
Link: <https://webexapis.com/v1/people?displayName=Harold&max=10&before&after=Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZWQtOGZjYS05ZGY0YjRmNDE3ZjU>; rel="next"

```

Notice the `rel="next"` at the end of the line. This tells your app that another page is available and provides the URL to fetch it.
The list of possible relationship types are:  
| Relationship  | Description  |  
| --- | --- |  
| `next`  | Link to the next page  |  
| `first`  | Link back to the first page  |  
| `prev`  | Link to the previous page  |  
Please note that only the `rel="next"` link header is guaranteed at this time. We may include other link types, that are defined in the RFC5988 (Web Linking) standard, in the future.
**Note:** Because data is loaded dynamically, a `Link` header may sometimes point to an empty page if all data was already returned on the previous page. In some APIs (such as `GET /membership?personEmail=`), you may encounter empty pages with `Link` headers still present, as memberships not visible to the requester's organization are filtered out. As a best practice, continue paginating through all pages until no `next` link header is present, collecting data from each page along the way.
###### Controlling Page Size
When requesting a list of resources the `max` query parameter may be used to control the number of items returned per page. For example, requesting `GET /people?displayName=Harold&max=2` tells the API to return only 2 items per page.
If the requested `max` query parameter value exceeds what a particular API endpoint allows, only the maximum number of items allowed per page for that endpoint will be returned. A `rel="next"` link header will be present if another page of results is available.
####  anchorMessage Attachments
anchor
Webex has native support for posting messages with file attachments. Using the [Messages API](https://developer.webex.com/docs/api/v1/messages) you can send messages containing text, text with attachments, or just share a file with the room without any text. Message attachments are limited to 100MB each.
What you may not know is that Webex has special support for most PDFs, Microsoft Word, Microsoft Excel, Microsoft PowerPoint, and most popular image formats. For these file types, Webex clients will render a preview in the room and a full view when clicked.
Here is the complete list of supported file types and extensions:
  * Microsoft Word (doc, docx)
  * Microsoft Excel (xls, xlsx)
  * Microsoft PowerPoint (ppt, pptx)
  * Adobe Portable Document Format (pdf)
  * JPEG (jpg, jpeg)
  * Windows Bitmap (bmp)
  * Graphics Interchange Format (gif)
  * Portable Network Graphics (png)


###### Send a Message with Attachments
###### Local File Attachments
To send local file attachments, simply post a message by including your access token in the `Authorization` header and the path to your local file with the `files` parameter. Optionally, you can also include a plain-text message with the attachment by using the `text` parameter. When uploading files directly from your local filesystem, your request will need to be a `multipart/form-data` request rather than JSON. Here's an example of using cURL to send a new message with a local file as a file attachment:

```
curl --request POST \
  --header "Authorization: Bearer ACCESS_TOKEN" \
  --form "files=@/home/desktop/example.png;type=image/png" \
  --form "roomId=Y2lzY2....." \
  --form "text=example attached" \
  https://webexapis.com/v1/messages

```

You can also use your favorite scripting language to send messages with local files. Here's an example of using Python with a local file:

```
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

m = MultipartEncoder({'roomId': 'Y2lzY2.....',
                      'text': 'example attached',
                      'files': ('example.png', open('example.png', 'rb'),
                      'image/png')})

r = requests.post('https://webexapis.com/v1/messages', data=m,
                  headers={'Authorization': 'Bearer ACCESS_TOKEN',
                  'Content-Type': m.content_type})

print r.text

```

###### Remote Attachments
Alternatively, if you have a file available via a publicly-accessible URL that you wish to share, you can use the URL as the value in the `files` JSON parameter instead of attaching your local file in a multipart message. The `files` parameter currently takes one URL as an input. A plain-text message can also be included in the `text` parameter. Here's an example of using cURL to send a new message with a remote file as a file attachment:

```
curl --request POST \
  --header "Authorization: Bearer ACCESS_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"roomId":"Y2lzY2.....","text":"Example file","files":["http://www.example.com/images/media.png"]}' \
  https://webexapis.com/v1/messages

```

###### Retrieve Message Attachments
###### Retrieving Message Details
In order to retrieve the file details such as `filename` and `content-type`, you can simply use a HEAD request with your access token in the `Authorization` header. This is particularly useful if you just want to verify the filename and type before downloading the content.

```
curl -I https://webexapis.com/v1/contents/Y2lzY...... -H "Authorization: Bearer ACCESS_TOKEN"

HTTP/1.1 200 OK
Cache-Control: no-cache
Content-Disposition: attachment; filename="example.png"
Content-Length: 44752
Content-Type: image/png

```

###### Retrieving Message Attachments
Files attached to a message are returned in the `files` property of the [message](https://developer.webex.com/docs/api/v1/messages) object. To retrieve one of these files you should issue a `GET` request on the file URL including your Access Token in the `Authorization` header.

```
curl -H "Authorization: Bearer ACCESS_TOKEN" https://webexapis.com/v1/contents/Y2lzY......

```

###### Anti-Malware Scanning
Organizations may enable [anti-malware scanning of files](https://help.webex.com/yr6g4bb/) in Webex to protect users from malicious files.
If a file is subject to evaluation, it will be quarantined and scanned. While the file is under evaluation, requests to retrieve the file will fail with a `423 Locked` HTTP response. A `Retry-After` header in the response will indicate when the request should be attempted again. There is no guarantee that the malware scan will have finished during the retry interval and you may need to retry again. The retry-after time is aligned with the majority of scans that are done on an average basis.
Infected files will be unavailable for download. Requests to retrieve a file that was scanned and found to be infected will fail with a `410 Gone` HTTP response.
Requests for files that a not scannable - for example encrypted files - will get a `428 Precondition Required` response. Adding the query parameter `allow=unscannable` to the request will meet the precondition and enable the request to be fulfilled. The user assumes all risks associated with these files.
####  anchorFormatting Messages
anchor
Webex clients, across all platforms, can send and receive a limited form of rich text messages formatted using the [Markdown markup language](https://daringfireball.net/projects/markdown/syntax). Bots and integrations can also send rich text messages formatted with Markdown, by using the [Messages API](https://developer.webex.com/docs/api/v1/messages).
Sending formatted text is super easy using the `markdown` parameter in the [Messages API](https://developer.webex.com/docs/api/v1/messages), though only a limited set of Markdown is supported at this time. See below for examples of the formatting supported in the Webex clients.
But, before we dive into the examples below, there's an important note we need to mention about line breaks: The examples below _do not_ include any JSON newline characters (`\n`) to create line breaks in Webex messages—we've left them out to focus on just the specific Markdown example. To include line breaks in your JSON message body, use standard Markdown [paragraphs and line breaks](https://daringfireball.net/projects/markdown/syntax#p) with JSON newline characters. For example, to create distinct paragraphs, use two newline characters between the paragraphs:

```
Paragraph 1\n\nParagraph 2

```

Or, for a single break between lines, end the line with two spaces followed by a single newline character:

```
Line 1  \nLine 2

```

###### Bold

```
**Title:** Add support for multiple file uploads

**Status:** Closed

```

###### Italic

```
This is *the best* launch we've had so far!

```

###### Links

```
Should we try the sushi place for lunch?
- [Oh yea!](http://example.com/polls/yd242?response=yes)
- [Ewww Sushi](http://example.com/polls/yd242?response=no)
- [Not today](http://example.com/polls/yd242?response=later)

```

###### Ordered Lists
Use a number, followed by a dot or right parenthesis and then a space to create an ordered list entry.

```
Priorities for the week are:
1. Collect Underpants
2. ???
3. Profit

```

###### Unordered Lists
Use a `*` or `-` followed by a space to create an unordered list entry.

```
Good morning Joe Fu. Here's your todo list:
- Review that really important thing.
- Meet Jason for lunch.
- Buy a new shirt. The one you're wearing is terrible.

```

###### Sub Items in Lists
Add two spaces before the `*` or `-` for each level of indentation.

```
Joe's to do list:
* Buy a new shirt.
  * With buttons.
    * And a collar!

```

###### Block Quotes

```
Alice, last week you said:
> I don't care what it costs. Let's book The Chainsmokers to headline Cisco Live.

Christine from finance laughed and is now questioning our sanity.

```

###### In-Line Code

```
Mike, I think the issue is with the `hasPermission` function

```

###### Fenced Code Blocks

```
Hello world in golang:
```
package main

import "fmt"

func main() {
    fmt.Println("Hello, 世界")
}
```

```

###### Mentions
Just like in the Webex clients, [@mentions](https://help.webex.com/p5k20o/) can be used in messages to get someone's attention in a group room. To @mention someone, use one of the following methods to specify the person or group of people:
###### Mention by Email

```
Hi <@personEmail:banderson@example.com|Bobby>, your order has been processed.

```

###### Mention by Person ID

```
We should get <@personId:Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY|Jose> to look at that right away.

```

###### Mention by Group

```
<@all>, we have some exciting news! Please watch this space for more information...

```

####  anchorRate Limiting
anchor
The Webex API rate limits requests to maintain appropriate service levels for all Webex API users. The rate limiting policies in place are fine-grained and often overlap and are therefore too complex to document exactly. The following provides general information for handling rate limiting errors, as well as upper limits for commonly used API use cases. It also provides recommendations for running and automating large API workloads.
  * [Handling 429 Errors](https://developer.webex.com/docs/basics#handling-429-errors)
  * [Upper Limits for API Requests](https://developer.webex.com/docs/basics#upper-limits-for-api-requests)
  * [Recommendations for Large API Workloads](https://developer.webex.com/docs/basics#recommendations-for-large-api-workloads)


###### Handling 429 Errors
If your application hits an API rate limit, the Webex API gateway returns a `429 Too Many Requests` response. The response includes a `Retry-After` header indicating how long your application must wait before making another request to the same endpoint. For example, the following is an example 429 response indicating that the application should wait 3600 seconds before retrying the request.

```
HTTP/1.1 429 Too Many Requests\
Content-Type: text/html\
Retry-After: 3600

```

See the [RetryAfterDemo code repository](https://github.com/webex/SparkRetryAfterDemo) on GitHub for a detailed example of handling 429 errors in Python.
###### Upper Limits for API Requests
Most of our REST APIs enforce a rate limit of around 300 requests per minute, with the `/people` and `/messages` APIs providing a higher quota that is dynamically adjusted.
###### Recommendations for Large API Workloads
This section contains recommendations for applications that make a large number of API calls, or make API calls over a broad range of APIs.
  * **Don't use end-user accounts for large workloads**. Don't use end-user accounts for large workloads as it may affect the user's experience, and they are not guaranteed to work with large workloads that affect a whole organization. For apps that act only on behalf of the user and make a small number of API requests a standard Webex user account can be used. However, for large API workloads it's recommended that you use a dedicated account specifically provisioned for that purpose. For example, [admin accounts](https://developer.webex.com/docs/admin) can be used to schedule meetings on behalf of users and should be dedicated to the API flow to reduce the probability of exceeding the allowed quota.
  * **Bot accounts**. If using an admin account is not possible consider using a [bot account](https://developer.webex.com/docs/bots), which have less restrictive rate limits than end-user accounts. However, due to content ownership rules with bot accounts, there are known issues when using them to automate certain types of messaging API workloads (for example, creating a very large number of messaging spaces, posting content to those spaces, and updating the members of those spaces). For these scenarios it's recommended that the automated system partition its work across separate accounts (see below).
  * **Partition concurrent API workloads across separate users**. API rate limits are shared per user, so multiple API workloads authenticating with the same user will affect each other's API limits. It's recommended that large API workloads be partitioned across separate users for separate concurrent tasks.


####  anchorAPI Errors
anchor
The Webex API returns standard HTTP status codes for request responses. If an error occurs, more information will be provided in the response.
###### HTTP Response Codes
The list below describes the common success and error responses you should expect from the API:  
| Code  | Status  | Description  |  
| --- | --- | --- |  
| 200  | OK  | Successful request with body content.  |  
| 201  | Created  | The request has succeeded and has led to the creation of a resource.  |  
| 202  | Accepted  | The request has been accepted for processing.  |  
| 204  | No Content  | Successful request without body content.  |  
| 400  | Bad Request  | The request was invalid or cannot be otherwise served. An accompanying error message will explain further.  |  
| 401  | Unauthorized  | Authentication credentials were missing or incorrect.  |  
| 403  | Forbidden  | The request is understood, but it has been refused or access is not allowed.  |  
| 404  | Not Found  | The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.  |  
| 405  | Method Not Allowed  | The request was made to a resource using an HTTP request method that is not supported.  |  
| 409  | Conflict  | The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.  |  
| 410  | Gone  | The requested resource is no longer available.  |  
| 415  | Unsupported Media Type  | The request was made to a resource without specifying a media type or used a media type that is not supported.  |  
| 423  | Locked  | The requested resource is temporarily unavailable. A `Retry-After` header may be present that specifies how many seconds you need to wait before attempting the request again.  |  
| 428  | Precondition Required  | File(s) cannot be scanned for malware and need to be force downloaded.  |  
| 429  | Too Many Requests  | Too many requests have been sent in a given amount of time and the request has been rate limited. A `Retry-After` header should be present that specifies how many seconds you need to wait before a successful request can be made.  |  
| 500  | Internal Server Error  | Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](https://developer.webex.com/support).  |  
| 502  | Bad Gateway  | The server received an invalid response from an upstream server while processing the request. Try again later.  |  
| 503  | Service Unavailable  | Server is overloaded with requests. Try again later.  |  
| 504  | Gateway Timeout  | An upstream server failed to respond on time. If your query uses `max` parameter, please try to reduce it.  |  
###### Responses with Errors
When retrieving multiple resources from the API, such as listing multiple Rooms or People, individual resources which should be included in the response may not be included because of an error. If any partial failures occur, the API will respond with a 200 OK and the response body will contain the entire list of resources, including the individual resources which could not be retrieved.
Resources which encounter errors during retrieval will include an `errors` object. This `errors` object will contain a specific error `code` and `reason` describing why the individual resource could not be returned in the request. Failures encountered during the request may be the result of a temporary issue, such as the inability to contact an on-premise key management server in a timely manner, or something more permanent. The error code and description will provide more detail about the error.
The `errors` object should only be present in the response if at least one resource could not be retrieved.
###### Example Response with Errors
The sample JSON below demonstrates how an error encountered while retrieving one room in a list of rooms is presented:

```
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "title": "Project Unicorn - Sprint 0",
      "type": "group",
      "isLocked": true,
      "teamId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
      "lastActivity": "2016-04-21T19:12:48.920Z",
      "created": "2016-04-21T19:01:55.966Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vNTIxN0EyMzYtNDQzQi00NThELTkzNjAtRDRFOTMyMTBBNUU5",
      "title": "eyJhbGciOiIiLCJraWQiOiIiLCJlbmMiOiIifQ....",
      "errors": {
        "title": {
          "code": "kms_failure",
          "reason": "Key management server failed to respond appropriately. For more information: https://developer.ciscospark.com/errors.html"
        }
      }
    }
  ]
}

```

###### Error Codes
The following table describes the errors which may be returned by the API:  
| Code  | Reason  | Description  |  
| --- | --- | --- |  
| `kms_failure`  | Key management server failed to respond appropriately.  | The Webex API is unable to contact the appropriate encryption key management server (KMS), or the KMS did not respond in a timely manner, and could not retrieve the requested resource. Try your request again later.  |  
###### SSL Connection Errors
The Webex API uses the [Server Name Indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication) extension to TLS/SSL. If your SSL client fails to connect to the API with an error such as `hostname 'webexapis.com' doesn't match either of '*.wbx2.com', 'wbx2.com'`, your client may not support SNI. Verify that your client supports the SNI extension. If your client does not support the SNI extension, then upgrade your client to a version which will support it and try your request again. Never configure your client to ignore SSL connection errors.
SNI support was implemented in these versions of the following common libraries and tools:
  * Java 1.7
  * PHP 5.3
  * Python 2.7.9, Python 3
  * Ruby (net/http) 2.0
  * cURL 7.18.1
  * wget 1.14


##### In This Article
  * [Pagination](https://developer.webex.com/meeting/docs/basics#pagination)
  * [Message Attachments](https://developer.webex.com/meeting/docs/basics#message-attachments)
  * [Formatting Messages](https://developer.webex.com/meeting/docs/basics#formatting-messages)
  * [Rate Limiting](https://developer.webex.com/meeting/docs/basics#rate-limiting)
  * [API Errors](https://developer.webex.com/meeting/docs/basics#api-errors)


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
