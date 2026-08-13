

---
# ORIGEN: https://eaf-sdk.webex.com

  * Preparing search index...
  * The search index is not available

[Webex Embedded Apps SDK (@webex/embedded-app-sdk)](https://eaf-sdk.webex.com/index.html)
[](https://eaf-sdk.webex.com/)
## Webex Embedded Apps SDK (@webex/embedded-app-sdk)
### [Table of Contents ](https://eaf-sdk.webex.com/#table-of-contents)
  * [Getting Started](https://eaf-sdk.webex.com/#getting-started)
  * [Kitchen Sink App](https://eaf-sdk.webex.com/#kitchen-sink-app)
  * [What's new in 2.0?](https://eaf-sdk.webex.com/#whats-new-in-20)
    * [NPM Availability](https://eaf-sdk.webex.com/#npm-availability)
      * [Using the SDK via NPM](https://eaf-sdk.webex.com/#using-the-sdk-via-npm)
      * [Using the SDK via CDN](https://eaf-sdk.webex.com/#using-the-sdk-via-cdn)
    * [Sidebar Apps APIs](https://eaf-sdk.webex.com/#sidebar-apps-apis)
    * [Rate limit on requests](https://eaf-sdk.webex.com/#rate-limit-on-requests)
  * [Migration from 1.x to 2.x](https://eaf-sdk.webex.com/#migration-from-1x-to-2x)
    * [Movement of main `Webex.Application` object](https://eaf-sdk.webex.com/#movement-of-main-webexapplication-object)
    * [Mentions of `webex.application` object](https://eaf-sdk.webex.com/#mentions-of-webexapplication-object)
    * [Get user API](https://eaf-sdk.webex.com/#get-user-api)
    * [User info changed event](https://eaf-sdk.webex.com/#user-info-changed-event)


* * *
# [Getting Started ](https://eaf-sdk.webex.com/#getting-started)
To get started on using the SDK, please visit the [API reference docs](https://eaf-sdk.webex.com/classes/Application.html).
* * *
# [Kitchen Sink App ](https://eaf-sdk.webex.com/#kitchen-sink-app)
  * To test your API with UCF, use this [Kitchen Sink app](https://eaf-sdk.webex.com/samples)
  * To test your APIs with Kitchen Sink mock thinclient, use this [thin client mockup page](https://eaf-sdk.webex.com/samples/thinclient.html)


* * *
# [What's new in 2.0? ](https://eaf-sdk.webex.com/#what39s-new-in-20) ## [NPM Availability ](https://eaf-sdk.webex.com/#npm-availability)
In addition to existing CDN build, we now have the main `Application` object available as an npm package. For more details, see the next section.
### [Using the SDK via NPM ](https://eaf-sdk.webex.com/#using-the-sdk-via-npm)
**Installing the SDK**

```
npm install --save @webex/embedded-app-sdk@latest

```

This will create an entry in your package.json like this:

```
{  
  "name": "webex-embedded-app-sample",  
  "version": "1.0.0",  
  "description": "",  
  "main": "index.js",  
  "scripts": {  
    "test": "echo \"Error: no test specified\" && exit 1"  
  },  
  "keywords": [],  
  "author": "",  
  "license": "ISC",  
  "dependencies": {  
    "@webex/embedded-app-sdk": "^2.0.0-beta.1"  
  }  
}

```

> **Note:** To avoid issues with importing the main application object please use SDK version starting 2.1.2 and up.
**Using the SDK**

```
import Application from '@webex/embedded-app-sdk';  
const app = new Application();  
await app.onReady();

```

Access anything under the `app` object as per the [API reference](https://eaf-sdk.webex.com/classes/Application.html). This can later be bundled with your app by using any bundling tool like webpack or rollup.
### [Using the SDK via CDN ](https://eaf-sdk.webex.com/#using-the-sdk-via-cdn)
**Including the SDK**
Add the following code in your `index.html`

```
<script src='https://unpkg.com/@webex/embedded-app-sdk@latest'></script>

```

The SDK is now included in your app. 
> **Note:** For SDK version 2.1.1 there is an issue importing the main object, please use earlier or later versions.
**Using the SDK**

```
const app = new window.webex.Application();  
await app.onReady();

```

Access anything under the `app` object as per the [API reference](https://eaf-sdk.webex.com/classes/Application.html).
## [Sidebar Apps APIs ](https://eaf-sdk.webex.com/#sidebar-apps-apis)
  * We have sidebar-related APIs, which also include call monitoring-related APIs
  * It is going to be of massive help to move away from Jabber and start using Webex Calling
  * More about Sidebar Apps APIs are documented [here](https://eaf-sdk.webex.com/interfaces/IWebexAppsSidebar.html).

## [Rate limit on requests ](https://eaf-sdk.webex.com/#rate-limit-on-requests)
Requests from the Embedded App SDK are rate limited by the native client in the following ways:
  * Initialization of the SDK is rate limited at 5 requests every 5 minutes.
  * Other requests from the SDK are rate limited at 20 requests per minute.

## [Log levels ](https://eaf-sdk.webex.com/#log-levels)
The Embedded App SDK 2.x allows the user to set and modify the log level at Application instance creation or at a later time. Default log level is set to INFO.
**While creating application instance**

```
const config = {  
  logs: {  
    logLevel: 0   //INFO: 0, WARN: 1, ERROR: 2, SILENT: 3  
  }  
}  
const app = new window.Webex.Application(config);  //CDN  
OR  
const app = new Application(config);  //NPM

```

**Using log property on application instance**

```
app.log.updateLogLevel(0);  //INFO: 0, WARN: 1, ERROR: 2, SILENT: 3

```

* * *
# [Migration from 1.x to 2.x ](https://eaf-sdk.webex.com/#migration-from-1x-to-2x) ## [Movement of main `Webex.Application` object ](https://eaf-sdk.webex.com/#movement-of-main-webexapplication-object)
  * The main `Webex.Application` object is removed and moved to `webex.Application`


**In 1.x SDK**

```
const app = new window.Webex.Application();

```

**In 2.x SDK**

```
const app = new window.webex.Application();

```
## [Mentions of `webex.application` object ](https://eaf-sdk.webex.com/#mentions-of-webexapplication-object)
The properties of `webex.application` are now private and no longer accessible
**In 1.x SDK**

```
const about = webex.application.about;  
const capabilities = webex.application.capabilities;  
const deviceType = webex.application.deviceType;

```

**In 2.x SDK**

```
const app = new window.webex.Application();  
const about = app.about;  
const capabilities = app.capabilities;  
const deviceType = app.deviceType;

```

The above list is not exhaustive, and other properties will also require the same change as shown above. All the properties, accessors, methods, and events are documented in the [`Application` class](https://eaf-sdk.webex.com/classes/Application.html).
## [Get user API ](https://eaf-sdk.webex.com/#get-user-api)
The `user` object is now a static object in 2.x SDK and can be directly accessed via the SDK; therefore, the `context.getUser()` method is no longer available.
**In 1.x SDK**

```
const app = new window.Webex.Application();  
app.context  
    .getUser()  
    .then((u) => {  
      log("getUser()", u);  
    })  
    .catch((error) => {  
      log(  
        "getUser() promise failed with error",  
        Webex.Application.ErrorCodes[error]  
      );  
    });

```

**In 2.x SDK**

```
const app = new window.webex.Application();  
await app.onReady();  
const user = app.application.states.user;

```
## [User info changed event ](https://eaf-sdk.webex.com/#user-info-changed-event)
There are no real-time updates for the `user` object, so the event [user:infoChanged](https://eaf-sdk.webex.com/classes/WebexAppsApplication.html#user_infoChanged) is no longer emitted.
**In 1.x SDK**

```
const app = new window.Webex.Application();  
app.onReady().then(() =>  {  
  app.listen()  
    .then(() => {  
      app.on("user:infoChanged", (user) => {  
        console.log("User object modified. New Information:", user);  
      })  
    })  
    .catch((reason) => {  
      console.error("listen: fail reason=" + webex.Application.ErrorCodes[reason]);  
    });  
});

```

**In 2.x SDK**
The event is removed and won't be emitted. Any instances of the above code must be removed.
## [Changelog ](https://eaf-sdk.webex.com/#changelog)
Please find the Changelog [here](https://eaf-sdk.webex.com/pages/CHANGELOG).
###  Settings
#### Member Visibility
  * Protected
  * Private
  * Inherited
  * External


#### Theme
OS Light Dark
###  Modules
  * [Webex Embedded Apps SDK (@webex/embedded-app-sdk)](https://eaf-sdk.webex.com/modules.html)
    * [Change Log](https://eaf-sdk.webex.com/pages/CHANGELOG.html)


  * [Application](https://eaf-sdk.webex.com/classes/Application.html)
  * [WebexAppsApplication](https://eaf-sdk.webex.com/classes/WebexAppsApplication.html)
  * [WebexAppsMeeting](https://eaf-sdk.webex.com/classes/WebexAppsMeeting.html)
  * [WebexAppsSpace](https://eaf-sdk.webex.com/classes/WebexAppsSpace.html)
  * [IBadge](https://eaf-sdk.webex.com/interfaces/IBadge.html)
  * [ICall](https://eaf-sdk.webex.com/interfaces/ICall.html)
  * [ICalls](https://eaf-sdk.webex.com/interfaces/ICalls.html)
  * [IContext](https://eaf-sdk.webex.com/interfaces/IContext.html)
  * [IParticipant](https://eaf-sdk.webex.com/interfaces/IParticipant.html)
  * [IWebexAppsApplicationState](https://eaf-sdk.webex.com/interfaces/IWebexAppsApplicationState.html)
  * [IWebexAppsMeetingState](https://eaf-sdk.webex.com/interfaces/IWebexAppsMeetingState.html)
  * [IWebexAppsSidebar](https://eaf-sdk.webex.com/interfaces/IWebexAppsSidebar.html)
  * [IWebexAppsSpaceState](https://eaf-sdk.webex.com/interfaces/IWebexAppsSpaceState.html)
  * [IWebexAppsUserState](https://eaf-sdk.webex.com/interfaces/IWebexAppsUserState.html)


