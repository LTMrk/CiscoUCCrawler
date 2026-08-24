---
doc_id: ciscodevnet-webex-contact-center-widget-starter-examples-widgets-timer-readme-md
source_url: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/Widgets/Timer/README.md
repo: CiscoDevNet/webex-contact-center-widget-starter
ruta: Examples/Widgets/Timer/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:47.838537+00:00
---

# webex-contact-center-widget-starter — Examples/Widgets/Timer/README.md

Repositorio: CiscoDevNet/webex-contact-center-widget-starter
Descripcion del repositorio: WebEx Contact Center widget starter

# WCC Widget: Timer

Testing in development environment:

1. Clone this repo
2. Run `yarn` from the root of the repo.
3. Run `yarn start` to start the playground app.

To use the Timer Widget:

1. Pass a time to the `duration` attribute following the string format: "hh:mm:ss".
2. Toggle the boolean attribute `paused` to stop and start the timer.

The browser's `localstorage` will keep a store of the active timer's start timestamp and duration setting. To change, update the duration and reset the timer, use the widget's public method `resetTimer():void`.

Timer is set to a default of "08:00:00"

When the timer runs down to "00:00:00" it will automatically pause, emit a custom event named "timer-expired", and clear the localstorage values until reset. 

![Widget Example Screenshot](./static/timer_screenshot.png)

---
> Fuente: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/Widgets/Timer/README.md (licencia MIT)
