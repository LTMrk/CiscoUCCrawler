---
doc_id: webex-components-src-components-webexactivitystream-readme-md
source_url: https://github.com/webex/components/blob/master/src/components/WebexActivityStream/README.md
repo: webex/components
ruta: src/components/WebexActivityStream/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:09:33.503094+00:00
---

# components — src/components/WebexActivityStream/README.md

Repositorio: webex/components
Descripcion del repositorio: Embed the power of Webex in your web applications, on your own terms 💪🏼

# Webex Activity Stream Component

Webex activity stream component displays a list of activities of a room.

<p align="center">
  <span>picture coming up</span>
</p>

## Preview

To see all the different possible states of the Webex Activity Stream component,
you can view our [storybook](https://webex.github.io/components/storybook/?path=/story/webex-activity-stream--default)
or run the following **NPM** command:

```shell
  npm start
```

## Embed

1. Create a component adapter from which the data will be retrieved (See [adapters](../../adapters)). For instance:

    ```js
    const jsonAdapter = new WebexJSONAdapter(jsonData);
    ```

2. Create a component instance by passing the room ID as a string and
enclose it within [a data provider](../WebexDataProvider/WebexDataProvider.js)
that takes the [component data adapter](../../adapters/WebexJSONAdapter.js) that we created previously

    ```js
    <WebexDataProvider adapter={jsonAdapter}>
      <WebexActivityStream roomID="roomID" />
    </WebexDataProvider>
    ```

The component knows how to manage its data. If anything changes in the data source that the adapter manages, the component will also update on its own.

---
> Fuente: https://github.com/webex/components/blob/master/src/components/WebexActivityStream/README.md (licencia MIT)
