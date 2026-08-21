---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-user-guide-ccvp-b-c2e52e782e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/user/guide/ccvp_b_1251-user-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio-release-1251/ccvp_b_1251-user-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio-release-1251_chapter_0110.html
retrieved_at: 2026-08-21T03:09:45.874796+00:00
---

User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.5(1)

# User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.5(1)

Updated: February 3, 2020

Chapter: JavaScript Utilities

## Chapter: JavaScript Utilities

# JavaScript Utilities

## JSONPath
                        	 Expression

Cisco Unified Call Studio includes a new utility that allows you to use
                           		JSONPath expressions in JavaScript to return the values from the
                           		JSON(JavaScript Object Notation).

```
importPackage(com.audium.server.cvpUtil);
JSONPathUtil.eval(String inputJSON , String expression);
```

Parameter

Description

importPackage(com.audium.server.cvpUtil)

This parameter imports the package to find the XPath values.

JSONpathUtil.eval(String inputJSON , String expression)

This parameter returns the value from the JSON document based on
                                       				the JSONPath expression provided.

```
importPackage(com.audium.server.cvpUtil);
var inputJSON = {Data.Element.Rest_Client_01.response_body};
JSONPathUtil.eval(String inputJSON , String expression);
```

## XPath
                        	 Expression

Cisco Unified Call
                           		Studio includes a new utility that allows you to use XPath expressions in
                           		JavaScript to return the values from the XML.

To use this utility,
                           		include the following syntax as part of the JavaScript when you define the
                           		local variables:

```
importPackage(com.audium.server.cvpUtil);
XpathUtil.eval(String inputXML , String expression);
```

Parameter

Description

importPackage(com.audium.server.cvpUtil)

This
                                       				  parameter imports the package to find the XPath values.

XpathUtil.eval(String inputXML, String expression)

This
                                       				  parameter returns the value from the XML document based on the XPath expression
                                       				  provided.

This function returns a Java Object, which needs to be explicitly typecasted before it can be used, for example, “var value = String(XpathUtil.eval(xml,xpathsearch));”

```
importPackage(com.audium.server.cvpUtil);
var xml = {Data.Element.Rest_Client_01.response_body};
XpathUtil.eval(xml , "/Results/Row[age<30]/name");
```

```
importPackage(com.audium.server.cvpUtil);
var xml ={Data.Element.Database_01.xml_resultset};
XpathUtil.eval(xml , "/Results/customer");
```

## Date
                        	 Validation

Cisco Unified Call Studio includes a new utility that allows you to
                           		validate date in JavaScript on local variables.

To use this utility, include the following syntax as part of the
                           		JavaScript:

```
importPackage(com.audium.server.cvpUtil);
DateTimeUtil.isValidDate(String dateToValidate, String dateFormat);
```

Parameter

Description

importPackage(com.audium.server.cvpUtil)

This parameter imports the package to find the XPath values.

DateTimeUtil.isValidDate(String dateToValidate, String
                                       				  dateFormat)

This parameter verifies whether the date provided is a valid
                                       				  format.

String dateToValidate

This parameter is the input date.

String dateFormat

This parameter specifies the format in which the date needs to
                                       				  be validated.

return value

If the input date is in the valid format, the return value is 1.

If the input date is not in the valid format, the return value
                                       				  is 0.

The following date formats are supported in JavaScript:

dd/MM/yyyy

dd.MM.yyyy

dd-MM-yyyy

ddMMyyyy

The month must always be represented by the upper case letters MM.

### For example:

importPackage(com.audium.server.cvpUtil);

DateTimeUtil.isValidDate("02/05/1990","dd/MM/yyyy");

## Time
                        	 Validation

Cisco Unified Call Studio includes a new utility that allows you to
                           		validate time in JavaScript on local variables.

To use this utility, include the following syntax as part of the
                           		JavaScript:

```
importPackage(com.audium.server.cvpUtil);
 DateTimeUtil.isValidTime(String timeToValidate, String timeFormat);
```

Parameter

Description

importPackage(com.audium.server.cvpUtil)

This parameter imports the package to find the XPath values.

DateTimeUtil.isValidTime(String timeToValidate, String
                                       				  timeFormat )

This parameter verifies whether the time provided is a valid
                                       				  format.

String timeToValidate

This is the input time that is validated.

String timeFormat

This is the format in which the input time has to be provided.

return value

If the input date is in the valid format, the return value is 1.

If the input date is not in the valid format, the return value
                                       				  is 0.

The following time formats are supported in JavaScript:

hh:mm:ss -24 hour format

hh:mm:ss am -12 hour format

hh:mm:ss pm -12 hour format

| Parameter | Description |
|---|---|
| importPackage(com.audium.server.cvpUtil) | This parameter imports the package to find the XPath values. |
| JSONpathUtil.eval(String inputJSON , String expression) | This parameter returns the value from the JSON document based on
                                       				the JSONPath expression provided. |

| Parameter | Description |
|---|---|
| importPackage(com.audium.server.cvpUtil) | This
                                       				  parameter imports the package to find the XPath values. |
| XpathUtil.eval(String inputXML, String expression) | This
                                       				  parameter returns the value from the XML document based on the XPath expression
                                       				  provided. Note This function returns a Java Object, which needs to be explicitly typecasted before it can be used, for example, “var value = String(XpathUtil.eval(xml,xpathsearch));” | Note | This function returns a Java Object, which needs to be explicitly typecasted before it can be used, for example, “var value = String(XpathUtil.eval(xml,xpathsearch));” |
| Note | This function returns a Java Object, which needs to be explicitly typecasted before it can be used, for example, “var value = String(XpathUtil.eval(xml,xpathsearch));” |

| Note | This function returns a Java Object, which needs to be explicitly typecasted before it can be used, for example, “var value = String(XpathUtil.eval(xml,xpathsearch));” |
|---|---|

| Parameter | Description |
|---|---|
| importPackage(com.audium.server.cvpUtil) | This parameter imports the package to find the XPath values. |
| DateTimeUtil.isValidDate(String dateToValidate, String
                                       				  dateFormat) | This parameter verifies whether the date provided is a valid
                                       				  format. |
| String dateToValidate | This parameter is the input date. |
| String dateFormat | This parameter specifies the format in which the date needs to
                                       				  be validated. |
| return value | If the input date is in the valid format, the return value is 1. If the input date is not in the valid format, the return value
                                       				  is 0. |

| Note | The month must always be represented by the upper case letters MM. |
|---|---|

| Parameter | Description |
|---|---|
| importPackage(com.audium.server.cvpUtil) | This parameter imports the package to find the XPath values. |
| DateTimeUtil.isValidTime(String timeToValidate, String
                                       				  timeFormat ) | This parameter verifies whether the time provided is a valid
                                       				  format. |
| String timeToValidate | This is the input time that is validated. |
| String timeFormat | This is the format in which the input time has to be provided. |
| return value | If the input date is in the valid format, the return value is 1. If the input date is not in the valid format, the return value
                                       				  is 0. |