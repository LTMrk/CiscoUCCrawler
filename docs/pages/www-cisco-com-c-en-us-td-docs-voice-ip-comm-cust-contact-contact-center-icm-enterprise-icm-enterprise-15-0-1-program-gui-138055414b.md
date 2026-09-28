---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-138055414b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_third-party-ui-specification_1501.html
retrieved_at: 2026-08-21T16:49:15.051323+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Reference

## Chapter: Reference

- Reference

- Third-party Integration UI Specification

# Reference

## Third-party Integration UI Specification

### Guidelines for Adding a Third-party User Interface

Follow these guidelines before adding a third-party user interface:

You can only add third-party user interfaces that have a secure URL (https).

Following security headers and CSP directives have been introduced in the browser response to prevent cross-site scripting
                                    (XSS) vulnerabilities.

It is recommended to follow the security header rules.

For the third-party gadget to open in the browser, value of the HTML anchor element must be available in the system. This
                                                      is because URL of the third-party hosts will be appended to the values in 'frame-src' .

Headers and Directives

Header and Directive Names

Values

HTTP Security Headers

```
X-Frame-Options
```

```
sameorigin
```

```
X-XSS-Protection
```

```
1
```

```
X-Content-Type-Options
```

```
nosniff
```

```
Strict-Transport-Security
```

```
max-age=31536000; 
includeSubDomains
```

Content-Security-Policy (CSP) directives

```
default-src
```

```
'self '
```

```
'unsafe-inline'
```

```
'unsafe-eval'
```

```
'self'
```

```
image-src
```

```
'self' data: http:
```

```
frame-src
```

```
'self' '<third-party hosts 
URL available in the system>*/'
```

```
frame-ancestors
```

```
'self'
```

```
base-uri
```

```
'self'
```

A Integrate as Gadget check box is provided if the page needs to be a hosted by the Shindig framework.

The URL of the user-interface must have the FQDN specified. URL with IPAddress is not allowed.

The name of the user interface must be unique and its length is limited to 15 characters.

Select any of the following system defined data to be used in the third-party user interface. These values are computed when
                                    the user-interface is rendered.

Deployment Type - Current deployment type (7 - PCCE 2K, 10 - PCCE 2K Lab, 17 -PCCE 4K, 18 - PCCE 12K )

Current User - The name and credentials of the logged on user. This data must be used as the authorization key to call the
                                          unifiedconfig API.

Current Role - The role of the logged on user. For example, administrator or supervisor.

API Base URL - API Base URL for unifiedconfig API. For example: http://10.10.10.10/unifiedconfig/config/

Locale - The current locale setting such as en_US.

User-defined data is a key value pair.

Name can be used as a key.

Sensitive value can be masked by selecting the Mask check box. Once masked, the data cannot be unmasked or edited.

The values of the key value pair will not be encoded in SPOG. This option only enables Unified CCE Administration to differentiate
                                          between sensitive and non-sensitive data and to report to the target application.

If you want to use a coded value, you can use public key encryption to encode the value and set the value. Use private key
                                          in the target application server to decode it before it is used.

Unified CCE Administration reports the sensitive fields list as a user preference (third-party user interface) or a query parameter.

### Stylesheet Guidelines

Add the following style sheet into the third-party user interface.

/cceadmin/scripts/css/cd.component.css

Transferring the styles definition from the parent third-party user interface into the iframe through post message is not
                                          supported in Packaged CCE 12.0 or later.

Page Element

Styles

Class Names

Page Title

font-family: Cisco SansTT Light;

font-size: 16px;

Page Body

font-family: Cisco SansTT Regular;

font-size: 12px;

button (primary)

font-family: Cisco SansTT Regular;

font-size: 14px;

bg-mint white bdr-transparent bdr-rad4 justify-content-ce align-item-center i-flex

button (secondary)

font-family: Cisco SansTT Regular;

font-size:14px;

bg-gray white bdr-transparent bdr-rad4 justify-content-ce align-item-center i-flex

button (blue)

font-family: Cisco SansTT Regular;

font-size:14px;

bg-gray white bdr-transparent bdr-rad4 justify-content-ce align-item-center i-flex

input[type=text]

select

font-family: Cisco SansTT Regular;

font-size:12px;

min-width: 150px;

For other UI elements styles, see the Business Hours pages in Unified CCE Administration .

### Common FAQs

How are system defined variables and user-defined variables passed to the third-party user interface?

If Integrate as Gadget is checked, it will be constructed as UserPrefs using the Shindig container.

If Integrate as Gadget is not checked, the user interface is built and passed as a query string.

Can I add a third-party user interface into a predefined menu such as the Agent menu?

Yes. The third-party user interface will be added as a tab. For example, Agent menu will be displayed in the first tab and
                                    the third-party user interface will be rendered as the second tab.

### Troubleshooting

Card does not appear on the Overview page to launch the third-party user interface.

Card and menu appear after you login again.

Your role in Unified CCE Administration does not have access to the third-party user interface.

The following error message appears in the screen:

Third-party user interface cannot be displayed. Please contact System Administrator

The user defined data and system defined data are passed to the third-party user interface as query string. Length of the
                                    third-party user interface URL is limited to 2000 characters (URL includes address and query string). If the data has exceeded
                                    2000 characters, minimize the length of the data passed as user defined and/or system defined data.

Third-party user interface created as non-gadget (you did not select the "Integrated as a gadget" check box) is not rendering.

Webpages with http header x-frames set cannot be rendered inside another site's iframe.

| Note | It is recommended to follow the security header rules. For the third-party gadget to open in the browser, value of the HTML anchor element must be available in the system. This
                                                      is because URL of the third-party hosts will be appended to the values in 'frame-src' . |
|---|---|

| Headers and Directives | Header and Directive Names | Values |
|---|---|---|
| HTTP Security Headers | X-Frame-Options | sameorigin |
| X-XSS-Protection | 1 |
| X-Content-Type-Options | nosniff |
| Strict-Transport-Security | max-age=31536000; 
includeSubDomains |
| Content-Security-Policy (CSP) directives | default-src | For Diagnostic Portico— 'self ' 'unsafe-inline' 'unsafe-eval' For Websetup— 'self' |
| image-src | 'self' data: http: |
| frame-src | 'self' '<third-party hosts 
URL available in the system>*/' |
| frame-ancestors | 'self' |
| base-uri | 'self' |

| Note | Transferring the styles definition from the parent third-party user interface into the iframe through post message is not
                                          supported in Packaged CCE 12.0 or later. |
|---|---|

| Page Element | Styles | Class Names |
|---|---|---|
| Page Title | font-family: Cisco SansTT Light; font-size: 16px; |  |
| Page Body | font-family: Cisco SansTT Regular; font-size: 12px; |  |
| button (primary) | font-family: Cisco SansTT Regular; font-size: 14px; | bg-mint white bdr-transparent bdr-rad4 justify-content-ce align-item-center i-flex |
| button (secondary) | font-family: Cisco SansTT Regular; font-size:14px; | bg-gray white bdr-transparent bdr-rad4 justify-content-ce align-item-center i-flex |
| button (blue) | font-family: Cisco SansTT Regular; font-size:14px; | bg-gray white bdr-transparent bdr-rad4 justify-content-ce align-item-center i-flex |
| input[type=text] select | font-family: Cisco SansTT Regular; font-size:12px; min-width: 150px; |  |

| Note | For other UI elements styles, see the Business Hours pages in Unified CCE Administration . |
|---|---|