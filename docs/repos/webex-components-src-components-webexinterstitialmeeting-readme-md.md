---
doc_id: webex-components-src-components-webexinterstitialmeeting-readme-md
source_url: https://github.com/webex/components/blob/master/src/components/WebexInterstitialMeeting/README.md
repo: webex/components
ruta: src/components/WebexInterstitialMeeting/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:09:36.011236+00:00
---

# components — src/components/WebexInterstitialMeeting/README.md

Repositorio: webex/components
Descripcion del repositorio: Embed the power of Webex in your web applications, on your own terms 💪🏼

# Webex Interstitial Meeting Component

Webex Interstitial meeting component displays the [Webex Local Media](../WebexLocalMedia) and [Webex Meeting Info](../WebexMeetingInfo) components for a meeting.

<p align="center">
  <img src="./WebexInterstitialMeeting.png" alt="Default Webex Interstitial Meeting" />
</p>

## Preview

To see all the different possible states of the Webex Interstitial Meeting component,
you can view our [storybook](https://webex.github.io/components/storybook/?path=/story/webex-interstitial-meeting--loading)
or run the following **NPM** command:

```shell
  npm start
```

## Embed

1.  Create a component adapter from which the data will be retrieved (See [adapters](../../adapters)). For instance:

    ```js
    const jsonAdapter = new WebexJSONAdapter(jsonData);
    ```

2.  Create a component instance by passing the person ID as a string and
    enclose it within [a data provider](../WebexDataProvider/WebexDataProvider.js)
    that takes the [component data adapter](../../adapters/WebexJSONAdapter.js) that we created previously

    ```js
    <WebexDataProvider adapter={jsonAdapter}>
      <WebexInterstitialMeeting meetingID="meetingID" />
    </WebexDataProvider>
    ```

The component knows how to manage its data. If anything changes in the data source that the adapter manages, the component will also update on its own.

---
> Fuente: https://github.com/webex/components/blob/master/src/components/WebexInterstitialMeeting/README.md (licencia MIT)
