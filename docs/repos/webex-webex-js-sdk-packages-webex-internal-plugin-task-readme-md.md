---
doc_id: webex-webex-js-sdk-packages-webex-internal-plugin-task-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-task/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/internal-plugin-task/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:19.599055+00:00
---

# webex-js-sdk — packages/@webex/internal-plugin-task/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/internal-plugin-task

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Plugin for the Task service

This is an internal Cisco Webex plugin. As such, it does not strictly adhere to semantic versioning. Use at your own risk. If you're not working on one of our first party clients, please look at our [developer api](https://developer.webex.com/) and stick to our public plugins.

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [Maintainers](#maintainers)
- [License](#license)

## Install

```bash
npm install --save @webex/internal-plugin-task
```

## Usage

```js
import '@webex/internal-plugin-task';

import WebexCore from '@webex/webex-core';

const webex = new WebexCore();

webex.internal.task.listMyTasks({
  orderBy: 'createdAt:desc'
});

webex.internal.task.getTask(id).then((task) => {
  // do something with the task
});

webex.internal.task.createTask({
  title: 'My new task',
  dueDate: '2024-12-31T23:59:59.000Z'
}).then((task) => {
  // do something with the task
});

webex.internal.task.updateTask(id, {
  title: 'My new task',
  notes: "This is notes",
  dueDate: '2024-12-31T23:59:59.000Z'
}).then((task) => {
  // do something with the task
});

webex.internal.task.deleteTask(id).then((task) => {
  // do something with the task
});

webex.internal.task.acceptTask(id).then((task) => {
  // do something with the task
});

webex.internal.task.rejectTask(id).then((task) => {
  // do something with the task
});

```

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-task/README.md (licencia NOASSERTION)
