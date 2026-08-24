---
doc_id: webex-components-src-components-webexsearchpeople-readme-md
source_url: https://github.com/webex/components/blob/master/src/components/WebexSearchPeople/README.md
repo: webex/components
ruta: src/components/WebexSearchPeople/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:09:39.990342+00:00
---

# components — src/components/WebexSearchPeople/README.md

Repositorio: webex/components
Descripcion del repositorio: Embed the power of Webex in your web applications, on your own terms 💪🏼

# Webex Search People Component

Webex Searech People component is used for searching the people by their display names inside webex.

## Preview

To see the search people component,
you can view our [storybook](https://webex.github.io/components/storybook/?path=/story/platform-webex-search-people--search-people)

or run the following **NPM** command:

```shell
  npm start
```

## Embed

1. Create a component adapter from which the data will be retrieved (See [adapters](../../adapters)). For instance:

    ```js
    const jsonAdapter = new WebexJSONAdapter(jsonData);
    ```

2. Create a component instance and enclose it within [a data provider](../WebexDataProvider/WebexDataProvider.js)
that takes the [component data adapter](../../adapters/WebexJSONAdapter.js) that we created previously

  The following can be passed as props from the create space component to the search people component:
  - `addedSpaceMembers` a callback function to return all the selected people to create space component 
     who will be added to room.
  - `webexLookAhead` a boolean value to define whether the component will search for people inside webex contacts or not.
  - `memberLookAhead` a callback function in which the component will pass the search string so that the integration 
  can search the person in their contacts and if returned they will be added as a collaborators.
  - `className`  an external css class
  - `style` external style object

    ```js   
    <WebexDataProvider adapter={jsonAdapter}>
      <WebexSearchPeople
        addedSpaceMembers={addedSpaceMembersCb}
        webexLookAhead={true}
        memberLookAhead={memberLookAheadCb}
      />
    </WebexDataProvider>
    ```

The component knows how to manage its data. If anything changes in the data source that the adapter manages, the component will also update on its own.

---
> Fuente: https://github.com/webex/components/blob/master/src/components/WebexSearchPeople/README.md (licencia MIT)
