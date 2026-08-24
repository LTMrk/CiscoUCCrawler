---
doc_id: ciscodevnet-webex-contact-center-widget-starter-examples-readme-md
source_url: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/README.md
repo: CiscoDevNet/webex-contact-center-widget-starter
ruta: Examples/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:44.791597+00:00
---

# webex-contact-center-widget-starter — Examples/README.md

Repositorio: CiscoDevNet/webex-contact-center-widget-starter
Descripcion del repositorio: WebEx Contact Center widget starter

# Demo Widget

### Build and Publish

#### Update existing widgets

After updating your widget, please run  `yarn dev:build` script from your widget project then follow below mentioned steps.

- Go to `webex-contact-center-widget-starter/Examples` folder.
- Run `yarn install`
- Run `yarn bootstrap`
- Run `yarn build`
- commit your changes in git hub

#### Adding new widgets
Develop your demo widget based on given widget guidelines guidelines. If you want your widget bundle need to be used in layout config inside desktop, then you need to publish your bundle in github.

Once you bundle your demo widget you need to copy the bundle into `webex-contact-center-widget-starter/widgets` folder and commit the changes into github.

if your bundle is build inside build directory of your project, then `Example/package.json` script will copy your bundle automatically, you just need to follow below steps.

- Go to `webex-contact-center-widget-starter/Examples` folder.
- Run `yarn install`
- Run `yarn bootstrap`
- Run `yarn build`
- commit your changes in git hub


Once code is merged into master, changes will be published automatically

---
> Fuente: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/README.md (licencia MIT)
