---
doc_id: webex-components-src-components-webexmeetingcontrolbar-readme-md
source_url: https://github.com/webex/components/blob/master/src/components/WebexMeetingControlBar/README.md
repo: webex/components
ruta: src/components/WebexMeetingControlBar/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:09:38.312697+00:00
---

# components — src/components/WebexMeetingControlBar/README.md

Repositorio: webex/components
Descripcion del repositorio: Embed the power of Webex in your web applications, on your own terms 💪🏼

# Webex Meeting Control Bar Component

Webex Meeting Control Bar component displays a list of buttons that allows for control over a meeting by performing a set of specific actions.

<p align="center">
  <img src="./WebexMeetingControlBar.png" alt="Default Webex Meeting Control Bar" />
</p>

## Preview

To see all the different possible states of the Webex Meeting Control Bar component, you can view our [storybook](https://webex.github.io/components/?path=/story/meetings-webex-meeting-control-bar--in-meeting)
or run the following **NPM** command:

```shell
  npm start
```

## Embed

1. Create a component adapter from which the data will be retrieved (See [adapters](../../adapters)). For instance:

    ```js
    const jsonAdapter = new WebexJSONAdapter(jsonData);
    ```

2. Create a component instance by passing the meeting ID as a string and an optional function that returns an array
of control names for the meeting. The default control names are set to `['mute-audio', 'mute-video', 'join-meeting]`
if the meeting is inactive and `['mute-audio', 'mute-video', 'leave-meeting']` otherwise.
Ensure that the control names match with the adapter implementation of the controls. You then need to enclose it
within [a data provider](../WebexDataProvider/WebexDataProvider.js) that takes
the [component data adapter](../../adapters/WebexJSONAdapter.js) that we created previously

    ```js
    const controls = (isActive) => isActive ? ['join-meeting'] : ['leave-meeting'];

    <WebexDataProvider adapter={jsonAdapter}>
      <WebexMeetingControlBar meetingID="meetingID" controls?={controls}/>
    </WebexDataProvider>
    ```

The component knows how to manage its data. If anything changes in the data source that the adapter manages,
the component will also update on its own.

---
> Fuente: https://github.com/webex/components/blob/master/src/components/WebexMeetingControlBar/README.md (licencia MIT)
