---
doc_id: webex-components-src-components-webexlocalmedia-readme-md
source_url: https://github.com/webex/components/blob/master/src/components/WebexLocalMedia/README.md
repo: webex/components
ruta: src/components/WebexLocalMedia/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:09:37.298643+00:00
---

# components — src/components/WebexLocalMedia/README.md

Repositorio: webex/components
Descripcion del repositorio: Embed the power of Webex in your web applications, on your own terms 💪🏼

# Webex Local Media Component

Webex local media component displays the local video or the local screen share, if enabled. If disabled, the avatar of the current _Webex_ user is displayed. The user can choose which stream to display (video or screen) using the `mediaType` prop. 

<p align="center">
  <img src="./WebexLocalMedia.png" alt="Default Webex Local Media" />
</p>

## Preview

To see all the different possible states of the Webex Local Media component,
you can view our [storybook](https://webex.github.io/components/storybook/?path=/story/webex-local-media--video)
or run the following **NPM** command:

```shell
  npm start
```

## Embed

1. Create a component adapter from which the data will be retrieved (See [adapters](../../adapters)). For instance:

    ```js
    const jsonAdapter = new WebexJSONAdapter(jsonData);
    ```

2. Create a component instance by passing the meeting ID as a string and enclose it within
[a data provider](../WebexDataProvider/WebexDataProvider.js) that takes
the [component data adapter](../../adapters/WebexJSONAdapter.js) that we created previously.
Choose the type of media to display by passing a string to `mediaType`
    ```js
    <WebexDataProvider adapter={jsonAdapter}>
      <WebexLocalMedia meetingID="meetingID" mediaType="video|screen" />
    </WebexDataProvider>
    ```

The component knows how to manage its data. If anything changes in the data source that the adapter manages,
the component will also update on its own.

---
> Fuente: https://github.com/webex/components/blob/master/src/components/WebexLocalMedia/README.md (licencia MIT)
