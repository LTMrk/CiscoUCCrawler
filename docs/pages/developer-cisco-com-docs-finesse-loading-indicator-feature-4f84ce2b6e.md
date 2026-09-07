---
doc_id: developer-cisco-com-docs-finesse-loading-indicator-feature-4f84ce2b6e
source_url: https://developer.cisco.com/docs/finesse/loading-indicator-feature/
retrieved_at: 2026-09-07T14:08:12.464625+00:00
---

# Loading Indicator Feature

The loading indicator is an OpenSocial feature that displays a loading message over gadgets while they are loading. This feature allows you  to provide a consistent
user experience within Finesse.

## Requesting the Loading Indicator

Use the following to request the loading indicator in the gadget ModulePrefs:

Code Snippet

```
< ModulePrefs > < Require feature = " loadingindicator " > < Param name = " manual-dismiss " > false </ Param > < Param name = " loading-timeout " > 10 </ Param > </ Require > </ ModulePrefs >
```

Parameter

Type

Description

Possible Values

Notes

loading-timeout

Integer

The number of seconds to wait before displaying the Retry button.
If the loading indicator is dismissed within this time, the Retry button does not appear.

Set this to a number that is appropriate for your gadget.

integers

Optional parameter.

Default is 10.

manual-dismiss

Boolean

This parameter determines whether the gadget dismisses
the loading indicator. If set to false, the feature code dismisses the loading indicator when  the gadget has loaded. However, the indicator may be dismissed too soon because the gadget may load before all 
gadget initialization code is complete. To manually dismiss the loading
indicator, set this parameter to true, and then configure the gadget to call
gadgets.loadingindicator.dismiss() after the gadget is loaded and initialized.

true, false

Optional parameter.

Default is false.

When the gadget is loading,  if the loading timeout is reached, the loading indicator changes to a timeout message and displays a Retry button that the user
can click to reload the gadget.

You can change any of the  strings displayed by the loading indicator by configuring the gadget to call the following JavaScript methods:

gadgets.loadingindicator.updateLoadingMessage(text)

gadgets.loadingindicator.updateTimeoutMessage(text)

gadgets.loadingindicator.updateRetryButtonText(text)

| Parameter | Type | Description | Possible Values | Notes |
|---|---|---|---|---|
| loading-timeout | Integer | The number of seconds to wait before displaying the Retry button.
If the loading indicator is dismissed within this time, the Retry button does not appear. Set this to a number that is appropriate for your gadget. | integers | Optional parameter. Default is 10. |
| manual-dismiss | Boolean | This parameter determines whether the gadget dismisses
the loading indicator. If set to false, the feature code dismisses the loading indicator when  the gadget has loaded. However, the indicator may be dismissed too soon because the gadget may load before all 
gadget initialization code is complete. To manually dismiss the loading
indicator, set this parameter to true, and then configure the gadget to call
gadgets.loadingindicator.dismiss() after the gadget is loaded and initialized. | true, false | Optional parameter. Default is false. |