[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/docs/embedded-apps-api-reference)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/docs/embedded-apps-api-reference)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/docs/embedded-apps-api-reference)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
## API Reference
### Embedded Apps API Reference
This is the complete API reference for the Webex Embedded Apps 1.x Framework.
The Embedded Apps version 1 SDK has been deprecated and will be supported based upon the following [support policy](https://developer.webex.com/docs/webex-api-and-sdk-support-policy#current-end-of-life-eol-notices). For new customers accessing this page, please see the [Embedded Apps version 2 SDK API Reference](https://eaf-sdk.webex.com/). For existing version 1 SDK customers, please see [Migration from 1.x to 2.x](https://eaf-sdk.webex.com/#migration-from-1x-to-2x). New features will only be added to the version 2 SDK.
####  anchorBasic Usage
anchor
To add the Embedded Apps Framework to your web application add the following to the `<HEAD>` of your app's main HTML page:

```
<script src="https://binaries.webex.com/static-content-pipeline/webex-embedded-app/v1/webex-embedded-app-sdk.js" defer></script>

```

In your app's main index.js file create a new `Webex.Application` instance and create a function to handle the `onReady()` promise when it resolves successfully.

```
var app = new window.Webex.Application();

app.onReady().then(function () {
  console.log('App is ready. App info:', app);
});

```

####  anchorFramework Versioning and API Support
anchor
The latest version of the Embedded Apps Framework is **1.5.0**. Different client apps (Webex app or Meeting Center, for example) may support different versions of the framework. Each API entry in this reference has an **Available Since** field that specifies the minimum SDK version required to use that API. Your app can use the [app.isSdkSupported()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isSdkSupported) to determine if the client supports that version.
For example, the reference entry for [initiateSystemBrowserOAuth()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+initiateSystemBrowserOAuth) indicates that it's been available since version 1.5.0 of the SDK. The following code first checks if the client supports that SDK version before calling the method.

```
if(app.isSdkSupported("1.5.0")) {
    app.initiateSystemBrowserOAuth("https://signin.example.com/...")
        .then(function (response) { ... })
        .catch(function (error) { ... })
}

```

Notes:
  * The framework supports `major.minor` and `major.minor.patch` versioning. For example, "1.4" and "1.4.1" are valid version string formats, but "1" or "1.4.5.1" are not. 
  * Version "1.4" is identical to "1.4.0".


####  anchorClasses
anchor
Classes defined by the framework.
  * [Webex.Application](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application) — Main Webex application object.
    * [webex.Application.deviceType](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+deviceType) : string — Form factor of client device.
    * [webex.Application.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) : boolean — Indicates if the SDK returns real or derived values for PII.
    * [webex.Application.displayContext](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+displayContext) : string — App's display context.
    * [webex.Application.isShared](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isShared) : boolean — Indicates if a URL has been shared with a meeting or space.
    * [webex.Application.embeddedSdkVersion](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+embeddedSdkVersion) : string — Version of the SDK embedded in the Webex or Meeting Center client.
    * [webex.Application.sdkVersion](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+sdkVersion) : string — Minimum SDK version supported by the Webex or Meeting Center client.
    * [webex.Application.theme](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+theme) : string — Color theme selected by the user for Webex or Meeting Center app.
    * [webex.Application.about](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+about) : string — General information about the client application.
    * [webex.Application.language](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+language) : string — Language code of the language being used by the client.
    * [webex.Application.setShareUrl(internalUrl, externalUrl, title, optionals)](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+setShareUrl) ⇒ Promise.<number> — Specifies URL to share in a meeting or space.
    * [webex.Application.clearShareUrl()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+clearShareUrl) — Clears the URL previously set with `setShareUrl()`.
    * [webex.Application.initiateSystemBrowserOAuth(authenticateUrl)](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+initiateSystemBrowserOAuth) ⇒ Promise.<string> | number — Initiates a single sign-On authentication flow with a third-party identity provider in the system web browser at the specified URL.
    * [webex.Application.on(eventName, callback)](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+on) — Called when the specified [event](https://developer.webex.com/docs/embedded-apps-api-reference#events) is raised.
    * [webex.Application.off(eventName)](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+off) — Stops listening for the specified [event](https://developer.webex.com/docs/embedded-apps-api-reference#events).
    * [webex.Application.listen()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+listen) ⇒ Promise.<void> — Registers application to listen for specified events..
    * [webex.Application.stopListening()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+stopListening) — Stops listening to all events.
    * [webex.Application.onReady()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+onReady) ⇒ Promise.<void> — Called when the `Webex.Application` object has been initialized and the SDK is ready for use by your app.
    * [webex.Application.openUrlInSystemBrowser(url)](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+openUrlInSystemBrowser) ⇒ Promise.<void> — Opens a URL in the default system browser.
    * [webex.Application.isSdkSupported(version)](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isSdkSupported) ⇒ boolean — Helper function which indicates if current API version is supported by the given client
    * [Webex.Application.ErrorCodes](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application.ErrorCodes) — Error codes returned by the API.
  * [Webex.Application.Context](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application.Context) — Application context object.
    * [webex.Application.Context.getUser()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application.Context+getUser) ⇒ [Promise.<User>](https://developer.webex.com/docs/embedded-apps-api-reference#User) | number — Returns information about the current user.
    * [webex.Application.Context.getMeeting()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application.Context+getMeeting) ⇒ [Promise.<Meeting>](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting) | number — Returns information about the meeting the app is running in.
    * [webex.Application.Context.getSpace()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application.Context+getSpace) ⇒ [Promise.<Space>](https://developer.webex.com/docs/embedded-apps-api-reference#Space) | number — Returns information about the space the app is running in.
  * [Meeting](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting) — 
    * [meeting.isPresenting](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting+isPresenting) : boolean — Indicates if a URL has been shared with a meeting. URL sharing is not supported for spaces.
    * [meeting.setPresentationUrl(url, title, shareOptimizationMode, includeAudio)](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting+setPresentationUrl) ⇒ Promise.<number> — Specifies URL to be presented in a meeting, for example, a PDF or PowerPoint document. The URL will be rendered in the stage view after consent from the host. The first time the call is made, the **Share this app content** button is displayed. Additional calls to the `setPresentation` URL will not require consent after the initial consent request from the host. `setPresentationUrl` can be called multiple times but subsequent calls will return `INVALID_ARGUMENT` if the app developer changes either the `optimizationMode` or the `includeAudio` parameter while the share is ongoing. To change `optimizationMode` or `includeAudio` you must manually stop the share, update the parameters and restart the share.
    * [meeting.clearPresentationUrl()](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting+clearPresentationUrl) — Clears the URL previously set with `setPresentationUrl()`.


###### Webex.Application
Main Webex application object. You use this object to obtain information about the application and its context, specify URLs for sharing, and register event listeners.
**Example usage**

```
var app = new window.Webex.Application();

app.onReady().then(() => {
  // Create event listeners
  app.listen()
    .then(() => {
      app.on("application:shareStateChanged", (event) => {
        // Call custom function
        handleShareStateChange(event);
      })
      app.on("application:themeChanged", (event) => {
        // Call custom function
        handleThemeChange(event);
      })
});

```

###### webex.Application.deviceType : string
Form factor of client device.
**Available since** : 1.1.0
The given device form factor. One of the following:
  * "DESKTOP" — Desktop client
  * "MOBILE" — Mobile device client (iPhone or Android device, for example)
  * "BROWSER" — Web browser client
  * "ROOM_SYSTEM_PERSONAL" — Webex Device running in personal mode.
  * "ROOM_SYSTEM_SHARED" — Webex Device running in shared mode (currently not supported).


* * *
###### webex.Application.isPrivateDataAvailable : boolean
Indicates if the SDK returns real or derived values for PII.
**Available since** : 1.1.0
Indicates if the app has access to personally identifiable information for the current user, meeting, or space (`true`), or if those values are empty or derived (`false`). See [Personally Identifiable Information (PII) and Embedded Apps](https://developer.webex.com/docs/embedded-apps-guide#personally-identifiable-information-pii-and-embedded-apps) for more information about derived PII values.
* * *
###### webex.Application.displayContext : string
App's display context.
**Available since** : 1.1.0
Display context in which the embedded app is running. Can be one of the following strings "MEETING_SIDEBAR", "MEETING_STANDALONE_WINDOW", "MEETING_MAINVIEW", or "SPACE_TAB". The default is "MEETING_SIDEBAR" for meeting-based apps and "SPACE_TAB" for messaging-based apps.
* * *
###### webex.Application.isShared : boolean
Indicates if a URL has been shared with a meeting or space.
**Available since** : 1.1.0
Indicates if the URL specified with a previous call to [app.setShareUrl()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+setShareUrl) has been shared in a meeting or space by the user clicking **Open Together** or **Add to Tab**. A value of `TRUE` indicates the URL has been shared; `FALSE` indicates the URL has not been shared.
**Example**
The following example checks if a sharing session is in progress before calling `setShareUrl()`. 

```
function handleSetShare(url)
    if (app.isShared) {
      console.log('ERROR: setShareUrl() should not be called while session is active');
      return;
    }
    // Call setShareUrl() as usual...
}

```

* * *
###### webex.Application.embeddedSdkVersion : string
Version of the SDK embedded in the Webex or Meeting Center client.
**Available since** : 1.1.0
Indicates the actual version of SDK used in the web application owned by developer according to [semantic versioning](https://semver.org/) rules. The [Webex.Application.sdkVersion](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+sdkVersion) property provides the maximum SDK version that the client implements.
* * *
###### webex.Application.sdkVersion : string
Maximum version of SDK supported by the Webex or Meeting Center client.
**Available since** : 1.1.0
Indicates the maximum version of SDK API implemented in end-user's client (Meeting Center or Webex app, for example). Following [semantic versioning](https://semver.org/) rules. For example, a value of "1.1.0" might be returned for Meeting Center client versions 41.6-41.9. The [Webex.Application.embeddedSdkVersion](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+embeddedSdkVersion) property contains the actual version of the SDK embedded in the client.
* * *
###### webex.Application.theme : string
Color theme selected by the user for Webex or Meeting Center app.
**Available since** : 1.1.0
Indicates the color theme that the user has selected for Webex or Meeting Center. Possible values are `Theme.LIGHT` or `Theme.DARK`.
* * *
###### webex.Application.about : string
General information about the client application.
**Available since** : 1.1.0
Contains general information about the client app (Webex or Meeting Center) in which the app is running. This format is subject to change and should only be used for diagnostic purposes.
* * *
###### webex.Application.language : string
Language code of the language being used by the client.
**Available since** : 1.1.0
Contains the ISO-639 language code of the language being used by the client (for example, "en-US", "da-DK", etc.).
* * *
###### webex.Application.setShareUrl(internalUrl, externalUrl, title, optionals) ⇒ Promise.<number>
Specifies URL to share in a meeting or space.
**Available since** : 1.1.0
Sets the URL to share in a meeting or space. Calling this method in a meeting causes the **Open Together** button to appear. In a space, calling this method causes the **Add to Tab** button to appear.
**Parameters**
  * `internalUrl` string - Required. URL to share with meeting participants, or add as a tab to a space. The application at the specified URL must integrate with the embedded app framework. (Maxiumum length: 2083 characters)
  * `externalUrl` string - Optional. URL of a version of the application for viewing outside of Webex or Meeting Center (i.e. in a standard web browser). This URL is used in a messaging space when a user selects **Open in Browser** or **Copy URL** from your app's space tab menu. Pass an empty string (`""`) for this parameter if you don't want users to open an external version of your app from a messaging space. This value is currently not used by in-meeting apps. (Max length: 2083 characters).
  * `title` string - Required. Title of the application window for an in-meeting app, or of the tab for an in-space app. (Max length 256 characters.)
  * `optionals` object - Empty JSON object, not currently used.


**Example**
The following provides values for all three parameters to `setShareUrl()`:

```
app.setShareUrl("https://www.example.com/app_internal/", "https://www.example.com/app_external/", "Application name")

```

**Example**
The following demonstrates how call `setShareUrl()` for a messaging space when you if you don't want users to open your app outside of Webex or Meeting Center:

```
app.setShareUrl("https://www.example.com/app_internal/", "", "Application name")

```

* * *
###### webex.Application.clearShareUrl()
Clears the URL previously set with `setShareUrl()`.
**Available since** : 1.1.0
Clears the URL previously set using [ setShareUrl()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+setShareUrl) and removes the **Open Together** or **Add to Tab** button.
* * *
###### webex.Application.initiateSystemBrowserOAuth(authenticateUrl) ⇒ Promise.<string> | number
Initiates a single sign-On authentication flow with a third-party identity provider in the system web browser at the specified URL.
**Available since** : 1.5.0
Initiates a single sign-on (SSO) authentication flow with a third-party identity provider in the system web browser at the specified URL. Returns a promise containing an OAuth authorization code from the ID provider, or a error code number.
`initiateSystemBrowserOAuth` is not supported in Webex for Government (FedRAMP).
In addition to any OAuth parameters required by the ID provider, the specified URL's **redirect_uri** query parameter must be set to **ht tps://oauth-helper-prod.wbx2.com/helperservice/v1/callback**. This callback correlates the authorization code returned by the identity provider with the embedded app that initiated the OAuth flow, and communicates that information back to your embedded app.
Notes:
  * The **Valid domains** [configuration option](https://developer.webex.com/docs/embedded-apps-guide#embedded-app-configuration-options) for your embedded app must include the domain for the SSO page URL you pass to `initiateSystemBrowserOAuth()` (**accounts.example.com** , for example).


**Parameters**
  * `authenticateUrl` string - Parameterized URL that's opened in the system web browser to initiate the SSO process. The URL's `redirect_uri` parameter must be set to `https://oauth-helper-prod.wbx2.com/helperservice/v1/callback`. (Max length: 2083 characters).


**Example**

```
// Variable to save authorization code
let authCode;
// Initiate SSO flow
app.initiateSystemBrowserOAuth("https://accounts.example.com/auth?client_id=...&redirect_uri=https://oauth-helper-prod.wbx2.com/helperservice/v1/callback")
  .then(function (response) {
    // Get authorization code from JSON response
    console.log("initiateSystemBrowserOAuth() succeeded")
    authCode = response;
    // Exchange authorization code for a token with the SSO provider. This part of the OAuth flow
    // is the responsibility of the embedded app, e.g.
    exchangeCodeForToken(authCode);
  })
  .catch(function (reason) {
    console.error("initiateSystemBrowserOAuth() failed with reason=",
                   window.Webex.Application.ErrorCodes[errorcode]
    );
  }

```

* * *
###### webex.Application.on(eventName, callback)
Called when the specified [event](https://developer.webex.com/docs/embedded-apps-api-reference#events) is raised.
**Available since** : 1.1.0
Registers a listener function to be called when the specified [event](https://developer.webex.com/docs/embedded-apps-api-reference#events) is raised. Your app must first call [ app.listen()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+listen) before registering listeners for specific events.
**Parameters**
  * `eventName` string - One of the supported [events](https://developer.webex.com/docs/embedded-apps-api-reference#events).
  * `callback` function - Function called when a given event is raised. Callback function will be passed the an event object containing details about the event.


**Example**
The following registers a listener for the `space:infoChanged` event that logs the [Space](https://developer.webex.com/docs/embedded-apps-api-reference#Space) object it receives as an event object to the console:

```
var app = new window.Webex.Application();
app.onReady().then(() => {
   log('onReady()', { message: 'host app is ready' })
   app.listen().then(() => {
      app.on('space:infoChanged', (payload) => log('Space info:', payload));
   })
});

```

* * *
###### webex.Application.off(eventName)
Stops listening for the specified [event](https://developer.webex.com/docs/embedded-apps-api-reference#events).
**Available since** : 1.1.0
Stops listening for the specified [event](https://developer.webex.com/docs/embedded-apps-api-reference#events).
**Parameters**
  * `eventName` string - Name of the [event](https://developer.webex.com/docs/embedded-apps-api-reference#events) to stop listening to.


* * *
###### webex.Application.listen() ⇒ Promise.<void>
Registers application to listen for specified events..
**Available since** : 1.1.0
Used to register an event listener for a specified [event](https://developer.webex.com/docs/embedded-apps-api-reference#events). Either returns a successful Promise indicating that your app is ready to listen for events, or a failed promise indicating an error occurred. The listener must be registered after the `app.onReady()` promise has successfully completed.
**Example**

```
app.onReady().then(() => {
   log('onReady()', { message: 'host app is ready' })
   app.listen().then(() => {
      app.on('space:infoChanged', (payload) => log('space:infoChanged', payload));
   })
});

```

* * *
###### webex.Application.stopListening()
Stops listening to all events.
**Available since** : 1.1.0
Removes all event listeners registered by your application.
* * *
###### webex.Application.onReady() ⇒ Promise.<void>
Called when the `Webex.Application` object has been initialized and the SDK is ready for use by your app.
**Available since** : 1.1.0
Called when the `Webex.Application` object has been initialized and the SDK is ready for use by your app.
**Example**
The following example waits for `onReady()` before logging the main Webex application object to the JavaScript console:

```
var app = new window.Webex.Application();

app.onReady().then(function () {
  console.log('App is ready. App info:', app);
});

```

* * *
###### webex.Application.openUrlInSystemBrowser(url) ⇒ Promise.<void>
Opens a URL in the default system browser.
**Available since** : 1.4.0
Opens an HTTPS or custom protocol URL in the default system browser. The specified URL must use `https:` or a custom protocol, such as `webexteams:` (to open the Webex app) or `mailto:` (to open the default mail app).
HTTPS URLs are validated against the list of allowed domains specified by the [embedded app's configuration options](https://developer.webex.com/docs/embedded-apps-guide#embedded-app-configuration-options). If a URL's domain doesn't match one of the app's allowed domains, or if it uses the `http:` protocol, then the call fails and an `ACCESS_DENIED` error is returned.
For URLs that specify custom protocols, the user is presented with a dialog asking them to allow or deny the request to open the app associated with the specified protocol. If the user clicks **Open external link** then Webex opens the associated app. Users can optionally save their preference to always open the associated app. User preferences are stored in local storage. If the user clicks **Cancel** then the call fails and an `ACCESS_DENIED` error is returned.
**Parameters**
  * `url` string - The URL to open in the system's default browser.


**Example**
The following custom function passes a Webex teams space URL ("webexteams:") to `openUrlInSystemBrowser()`. If an error occurs the error message is displayed in the JavaScript console:

```
function openTeamSpace() {
   app.openUrlInSystemBrowser("webexteams://im?space=87a7b58d-bad1-4e2f-83c9-91aeb21c65f6").catch((errorcode) => {
     console.log("Error: ", window.Webex.Application.ErrorCodes[errorcode]);
   })
}

```

**Example**
The following custom function opens an `https` URL. The URL's domain must match one of the embedded app's allowed domains. If an error occurs the error message is displayed in the JavaScript console:

```
function openSignInPage() {
   app.openUrlInSystemBrowser("https://www.example.com/signin").catch((errorcode) => {
     console.log("Error: ", window.Webex.Application.ErrorCodes[errorcode]);
   })
}

```

* * *
###### webex.Application.isSdkSupported(version) ⇒ boolean
Helper function which indicates if current API version is supported by the given client
**Available since** : 1.5.0
Helper function that returns `true` if the client (Webex or Meeting Center app) supports a given version of the embedded apps SDK. The framework supports `major.minor` and `major.minor.patch` versioning. For example, "1.4" and "1.4.1" are valid version string formats, but "1" or "1.4.5.1" are not.
Also note that "1.4" is identical to "1.4.0".
**Parameters**
  * `version` string - SDK version required by the API.


**Example**
The following checks if the Webex or Meeting Center app supports the "1.5.0" SDK version to determine if it can call the [app.initiateSystemBrowserOAuth()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+initiateSystemBrowserOAuth) method:

```
if(app.isSdkSupported("1.5.0")) {
   // Client supports initiateSystemBrowserOAuth() method, initiate SSO flow:
   app.initiateSystemBrowserOAuth("https://...")
}

```

* * *
###### Webex.Application.ErrorCodes
Error codes returned by the API.
**Available since** : 1.1.0
Enumeration of error codes returned by API methods.
**Properties**
  * `0` - Operation completed successfully.
  * `1` - Call failed but arguments were incorrect.
  * `2` - Call failed due to invalid arguments.
  * `3` - Call to register an event failed because the event is already registered.
  * `4` - Call to register an event failed because the event name is unknown to the framework.
  * `5` - Call failed because it's not supported in the current context (Meeting or Space, for example).
  * `6` - Call failed because the feature is not supported.
  * `7` - Call failed because the framework has not initialized. Make sure your application waits for the [ onReady()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+onReady) promise to resolve before accessing properties or invoking methods belonging to the framework.
  * `8` - Access to API has been denied, this can be due to rate limit.
  * `9` - Request timed out
  * `SUCCESS` - Operation completed successfully.
  * `GENERIC_ERROR` - Call failed but arguments were incorrect.
  * `INVALID_ARGUMENT` - Call failed due to invalid arguments.
  * `EVENT_ALREADY_REGISTERED` - Call to register an event failed because the event is already registered.
  * `EVENT_UNKNOWN` - Call to register an event failed because the event name is unknown to the framework.
  * `BAD_CONTEXT` - Call failed because it's not supported in the current context (Meeting or Space, for example).
  * `NOT_SUPPORTED` - Call failed because the feature is not supported.
  * `NOT_INITIALIZED` - Call failed because the framework has not initialized. Make sure your applications waits for the `onReady()` to resolve before making any method calls to the framework.
  * `ACCESS_DENIED` - Access to API has been denied, this can be due to rate limit.
  * `TIMED_OUT` - Request timed out


**Example**
The following example logs the User object returned by `getUser()` if successful, or logs an error string if the operation fails:

```
app.context.getUser().then((u) => {
    console.log('getUser()', u);
}).catch((error) => {
    console.log('getUser() promise failed with error', Webex.Application.ErrorCodes[error]);
})

```

* * *
###### Webex.Application.Context
Application context object that exposes methods for getting information about users, meetings, and spaces. It is exposed as a `context` property on the Webex Application instance.
**Example usage**

```
var app = new window.Webex.Application();

app.onReady().then(() =>  {
  app.context.getUser().then((user) => {
      console.log("getUser() promise resolved. User", user);
    }
  ).catch((error) => {
      console.log("getUser() promise failed " + error.message);
    })
});

```

###### webex.Application.Context.getUser() ⇒ [Promise.<User>](https://developer.webex.com/docs/embedded-apps-api-reference#User) | number
Returns information about the current user.
**Available since** : 1.1.0
Returns a promise for a [User](https://developer.webex.com/docs/embedded-apps-api-reference#User) object if successful, or a numeric error code if rejected. If {[ isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable)} is `true` then personally identifiable information (PII) about the user returned in the response contains real values; if `false` then the values are derived.
**Example**

```
 var app = new window.Webex.Application();
 app.onReady().then(() => {
   app.context.getUser().then((m) => {
     console.log('getUser()', m);
   }).catch((error) => {
     console.log('getUser() promise failed with error', Webex.Application.ErrorCodes[error]);
   });
 }

```

* * *
###### webex.Application.Context.getMeeting() ⇒ [Promise.<Meeting>](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting) | number
Returns information about the meeting the app is running in.
**Available since** : 1.1.0
Returns a promise for a [Meeting](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting) object if successful, or a numeric error code if rejected. A `BAD_CONTEXT` error code (5) is returned if the method is called outside the context of a Meeting (in a Space, e.g.). If {[ isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable)} is `true` then any personally identifiable information (PII) about the meeting returned in the response contains real values; if `false` then the values are derived.
**Example**

```
 var app = new window.Webex.Application();
 app.onReady().then(() => {
   app.context.getMeeting().then((m) => {
     console.log('getMeeting()', m);
   }).catch((error) => {
     console.log('getMeeting() promise failed with error', Webex.Application.ErrorCodes[error]);
   });
 }

```

* * *
###### webex.Application.Context.getSpace() ⇒ [Promise.<Space>](https://developer.webex.com/docs/embedded-apps-api-reference#Space) | number
Returns information about the space the app is running in.
**Available since** : 1.1.0
Returns a promise for a [Space](https://developer.webex.com/docs/embedded-apps-api-reference#Space) object if successful, or a numeric error code if rejected. A `BAD_CONTEXT` error code (5) is returned if the method is called outside the context of a Space (in a Meeting, e.g.). If {[ isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable)} is `true` then any personally identifiable information (PII) about the space returned in the response contains real values; if `false` then the values are derived.
**Example**

```
 var app = new window.Webex.Application();
 app.onReady().then(() => {
   app.context.getSpace().then((m) => {
     console.log('getSpace()', m);
   }).catch((error) => {
     console.log('getSpace() promise failed with error', Webex.Application.ErrorCodes[error]);
   });
 }

```

* * *
###### Meeting
###### meeting.isPresenting : boolean
Indicates if a URL has been shared with a meeting. URL sharing is not supported for spaces.
**Available since** : 1.7.0
Indicates if the URL specified in the call to [app.context.meeting.setPresentationUrl()](https://developer.webex.com/docs/Webex.Application.Meeting#setPresentationUrl) is being presented in stage view. This requires the user to click **Share this app content** button. A value of `TRUE` indicates the presentation is ongoing; `FALSE` indicate the presentation has not started.
* * *
###### meeting.setPresentationUrl(url, title, shareOptimizationMode, includeAudio) ⇒ Promise.<number>
Specifies URL to be presented in a meeting, for example, a PDF or PowerPoint document. The URL will be rendered in the stage view after consent from the host. The first time the call is made, the **Share this app content** button is displayed. Additional calls to the `setPresentation` URL will not require consent after the initial consent request from the host. `setPresentationUrl` can be called multiple times but subsequent calls will return `INVALID_ARGUMENT` if the app developer changes either the `optimizationMode` or the `includeAudio` parameter while the share is ongoing. To change `optimizationMode` or `includeAudio` you must manually stop the share, update the parameters and restart the share.
**Available since** : 1.7.0
**Parameters**
  * `url` string - URL of the presentation that will be rendered in stage view on the presenter side.
  * `title` string - Title of the presentation being rendered.
  * `shareOptimizationMode` ShareOptimizationMode - Share optimization mode. Indicates if the content being shared should be optimized for video/motion, text/images or auto detect. The parameter type can be `Webex.Application.ShareOptimizationMode.AUTO_DETECT`, `Webex.Application.ShareOptimizationMode.TEXT`, or `Webex.Application.ShareOptimizationMode.VIDEO`.
  * `includeAudio` boolean - Indicates if audio should be shared as well


**Example**
Provides a value for the URL parameter passed as an argument to `setPresentationUrl()`:

```
meeting.setPresentationUrl("https://www.example.com/app_internal/", "title", Webex.Application.ShareOptimizationMode.AUTO_DETECT, false);

```

* * *
###### meeting.clearPresentationUrl()
Clears the URL previously set with `setPresentationUrl()`.
**Available since** : 1.7.0
Clears the URL previously set using [ setPresentationUrl()](https://developer.webex.com/docs/Webex.Application.Meeting#setPresentationUrl)
* * *
####  anchorType Definitions
anchor
The following typed objects are used to represent users, meetings, and spaces.
  * [Space](https://developer.webex.com/docs/embedded-apps-api-reference#Space) : object — Represents a Webex messaging space.
  * [User](https://developer.webex.com/docs/embedded-apps-api-reference#User) : object — Represents a Webex user.


###### Space
Represents a Space object returned by a call to [ getSpace()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application.Context+getSpace).
**Properties**
  * `id` string -- ID of the space (room) in which the app is running. If [app.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) is `true` this property is set to the ID of the Webex space, and can used with the Webex REST APIs. If [app.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) is `false` this property is set to a unique ("derived") value that is guaranteed to be consistent for all app users, but cannot be used with the Webex REST APIs.
  * `derivedId` string -- .
  * `title` string -- Title of the given space; blank if [app.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) is false.


**Since** : 1.1.0 
* * *
###### User
Represents a User object returned by a call to [ getUser()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application.Context+getUser).
**Properties**
  * `id` string -- Webex user ID. If [app.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) is `true` this property contains the user's Webex user ID, and can be used with the Webex REST APIs. If `isPrivateDataAvailable` is `false` this property is set to a unique ("derived") value that is guaranteed to be consistent for the same user and app, but cannot be used with the Webex REST APIs.
  * `orgId` string -- Organization ID. If [app.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) is `true` this property is set to the ID of the user's Webex organization, and can be used with the Webex REST APIs. If `isPrivateDataAvailable` is `false` this property is set to a unique ("derived") value that is guaranteed to be consistent for the same combination of user, organization, and app, but cannot be used with Webex APIs.
  * `email` string -- Webex user's registered email, or an empty string iff [app.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) is `false`.
  * `displayName` string -- Webex user's display name, or an empty string if [app.isPrivateDataAvailable](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+isPrivateDataAvailable) is false.
  * `token` string -- [JSON Web Token](https://developer.webex.com/docs/embedded-apps-guide#about-the-json-web-token) (JWT) generated for the user by the Webex identity service.


**Since** : 1.1.0 
* * *
####  anchorEvents
anchor
The following events are generated by the framework. To listen for a specific event your application uses the [listen()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+listen) and [on()](https://developer.webex.com/docs/embedded-apps-api-reference#Webex.Application+on) methods. Your listener function is passed an event object that contains details about the event. For more information on handling events see [Handling Events](https://developer.webex.com/docs/embedded-apps-guide#responding-to-events) in the [Embedded Apps Developer Guide](https://developer.webex.com/docs/embedded-apps-guide).
  * ["application:shareStateChanged"](https://developer.webex.com/docs/embedded-apps-api-reference#application_shareStateChanged) — Fired when an Open Together session is started or ended by the user.
  * ["application:displayContextChanged"](https://developer.webex.com/docs/embedded-apps-api-reference#application_displayContextChanged) — Fired when the rendering context of the application changes
  * ["application:themeChanged"](https://developer.webex.com/docs/embedded-apps-api-reference#application_themeChanged) — Fired when the user selects a new application theme.
  * ["meeting:infoChanged"](https://developer.webex.com/docs/embedded-apps-api-reference#meeting_infoChanged) — Fired when meeting information has changed for the current meeting.
  * ["meeting:roleChanged"](https://developer.webex.com/docs/embedded-apps-api-reference#meeting_roleChanged) — Fired when the role(s) for the current meeting participant changes.
  * ["space:infoChanged"](https://developer.webex.com/docs/embedded-apps-api-reference#space_infoChanged) — Fired when information about the space in which the application is running changes.


###### "application:shareStateChanged"
Fired when an Open Together session is started or ended by the user. The event object is a boolean that's set to `true` if an Open Together session has just started, or `false` if a session has just ended.
**Example**

```
app.onReady().then(() =>  {
  app.listen()
    .then(() => {
      app.on("application:shareStateChanged", (event) => {
        console.log("Share state changed. Sharing state is:", event);
      })
    })
    .catch((reason) => {
      console.error("listen: fail reason=" + Webex.Application.ErrorCodes[reason]);
    });
});

```

**Available since** : 1.1.0
* * *
###### "application:displayContextChanged"
Fired when the rendering context of the application changes, for example, when a user pops out the app from the sidebar to a new window. Event object contains the app's new display context. Possible values are "MEETING_SIDEBAR", "MEETING_STANDALONE_WINDOW", or "MEETING_MAINVIEW" (for meeting-based apps), or "SPACE_TAB" (for messaging-based apps).
This event is currently not emitted by messaging-based apps. 
**Example**

```
app.onReady().then(() =>  {
  app.listen()
    .then(() => {
      app.on("application:displayContextChanged", (event) => {
        console.log("Display context changed. New display context:", event);
      })
    })
    .catch((reason) => {
      console.error("listen: fail reason=" + Webex.Application.ErrorCodes[reason]);
    });
});

```

**Available since** : 1.1.0
* * *
###### "application:themeChanged"
Fired when the user selects a new application theme. The event object is a string indicating the newly selected theme. Possible values are `LIGHT` and `DARK`.
**Example**

```
app.onReady().then(() =>  {
  app.listen()
    .then(() => {
      app.on("application:themeChanged", (event) => {
        console.log("Theme changed. New theme:", event);
      })
    })
    .catch((reason) => {
      console.error("listen: fail reason=" + Webex.Application.ErrorCodes[reason]);
    });
});

```

**Available since** : 1.1.0
* * *
###### "meeting:infoChanged"
Fired when meeting information has changed for the current meeting. Event object is [Meeting](https://developer.webex.com/docs/embedded-apps-api-reference#Meeting) object that describes the updated meeting.
**Example**

```
app.onReady().then(() =>  {
  app.listen()
    .then(() => {
      app.on("meeting:infoChanged", (event) => {
        console.log("Meeting information changed. New meeting info:", event);
      })
    })
    .catch((reason) => {
      console.error("listen: fail reason=" + Webex.Application.ErrorCodes[reason]);
    });
});

```

**Available since** : 1.1.0
* * *
###### "meeting:roleChanged"
Fired when the role for the current participant changes. Event object is an array of strings that indicate the new role(s) assigned to the current user. Possible values are "PARTICIPANT","GUEST", "HOST", "COHOST", "PANELIST", and "PRESENTER".
**Example**

```
app.onReady().then(() =>  {
  app.listen()
    .then(() => {
      app.on("meeting:roleChanged", (event) => {
        console.log("Meeting role changed for user. New roles:", event);
      })
    })
    .catch((reason) => {
      console.error("listen: fail reason=" + Webex.Application.ErrorCodes[reason]);
    });
});

```

**Available since** : 1.1.0
* * *
###### "space:infoChanged"
Fired when information about the space in which the application is running changes (such as changes to the space's title). The event object is a [Space](https://developer.webex.com/docs/embedded-apps-api-reference#Space) object that contains the updated details for the space.
**Example**

```
app.onReady().then(() =>  {
  app.listen()
    .then(() => {
      app.on("space:infoChanged", (event) => {
        console.log("Space information changed. New space info:", event);
      })
    })
    .catch((reason) => {
      console.error("listen: fail reason=" + Webex.Application.ErrorCodes[reason]);
    });
});

```

**Available since** : 1.1.0
* * *
##### In This Article
  * [Basic Usage](https://developer.webex.com/docs/embedded-apps-api-reference#basic-usage)
  * [Framework Versioning and API Support](https://developer.webex.com/docs/embedded-apps-api-reference#framework-versioning-and-api-support)
  * [Classes](https://developer.webex.com/docs/embedded-apps-api-reference#classes)
  * [Type Definitions](https://developer.webex.com/docs/embedded-apps-api-reference#type-definitions)
  * [Events](https://developer.webex.com/docs/embedded-apps-api-reference#events)


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
