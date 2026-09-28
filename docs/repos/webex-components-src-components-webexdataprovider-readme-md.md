---
doc_id: webex-components-src-components-webexdataprovider-readme-md
source_url: https://github.com/webex/components/blob/master/src/components/WebexDataProvider/README.md
repo: webex/components
ruta: src/components/WebexDataProvider/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:09:34.547418+00:00
---

# components — src/components/WebexDataProvider/README.md

Repositorio: webex/components
Descripcion del repositorio: Embed the power of Webex in your web applications, on your own terms 💪🏼

# Webex Data Provider

Webex Data Provider creates a context that provides data adapters to its child components.

## Usage

1. Create an adapter for a data source.
Webex Components come with a JSON data adapter used to test components with static data.
See the [data](../../data) directory for reference on the structure of the data.

    ```js
    import {WebexJSONAdapter} from '@webex/components';
    import jsonData from './my-data';

    const jsonAdapter = new WebexJSONAdapter(jsonData);
    ```

2. Create the data provider and give it the previously created [data adapter](../../adapters/WebexJSONAdapter.js).

    ```js
    import {WebexDataProvider, WebexJSONAdapter} from '@webex/components';
    import jsonData from './my-data';

    const jsonAdapter = new WebexJSONAdapter(jsonData);

    <WebexDataProvider adapter={jsonAdapter}>
      // Add Webex components here
    </WebexDataProvider>
   ```

---
> Fuente: https://github.com/webex/components/blob/master/src/components/WebexDataProvider/README.md (licencia MIT)
