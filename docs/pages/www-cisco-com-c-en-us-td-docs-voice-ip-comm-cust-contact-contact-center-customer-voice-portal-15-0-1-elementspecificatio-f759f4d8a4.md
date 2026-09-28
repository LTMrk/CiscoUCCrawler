---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-f759f4d8a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/local_variables.html
retrieved_at: 2026-08-21T17:11:43.860734+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Local Variables

## Chapter: Local Variables

- Local Variables

- Set Value                              	 Element

- Change                              	 Implementation Order of Local Variables

# Local Variables

## Set Value
                        	 Element

The Set Value element allows you to define and assign values to
                                       				local variables. It supports basic mathematical operation, string operation,
                                       				and Java script. The Set Value element allows you to specify a Java script
                                       				which does the required programming in the application. The Java script allows
                                       				substitution of other element data. The evaluation result of Java script is
                                       				stored in the variable specified in the Settings tab. The scope of the local
                                       				variable is restricted to a particular subflow or main flow in which it is
                                       				defined and is not available in another subflow or main flow.

You can perform the following operations on local variables:

Add Variable

Delete Variable

Update Variable

Move Variable

The Settings tab does not display the Delete Variable and Update Variable options when you add a variable for the first time.

Performance of the Set Value node's static assignment depends on the the external java script engine's (rhino/nashron /graal.js

) performance. Usage of multiple static assignment of variables may deteriorate the performance drastically. So, the recommendation
                                             is to use custom java code to initialise the variables.

Default JavaScript engine configured is rhino . In case of script engine specific error, the JavaScript engine can be changed to nashorn or graal.js , by adding below property to CVP_HOME\conf\vxml.properties file:

VXML.JsEngine = nashorn for nashorn .

VXML.JsEngine = graal.js for graal.js .

restart VXML Server Service

## Change
                        	 Implementation Order of Local Variables

Cisco Unified Call Studio allows you to select and move the local
                              		  variables up and down on the Settings tab to change the order in which they
                              		  are implemented. The implementation order of local variables will be same as
                              		  the order as defined in the Settings tab.

Follow these steps to change the implementation order of local
                              		  variables in the Settings tab.

Step 1

On the Settings tab, right-click the local variable
                                       			 you want to move up or down and choose Mark Variable .

Step 2

Choose the location where you want to move the marked local
                                       			 variable, right-click and choose Move Variable .

| The Set Value element allows you to define and assign values to
                                       				local variables. It supports basic mathematical operation, string operation,
                                       				and Java script. The Set Value element allows you to specify a Java script
                                       				which does the required programming in the application. The Java script allows
                                       				substitution of other element data. The evaluation result of Java script is
                                       				stored in the variable specified in the Settings tab. The scope of the local
                                       				variable is restricted to a particular subflow or main flow in which it is
                                       				defined and is not available in another subflow or main flow. |
|---|

| Note | The Settings tab does not display the Delete Variable and Update Variable options when you add a variable for the first time. Performance of the Set Value node's static assignment depends on the the external java script engine's (rhino/nashron /graal.js ) performance. Usage of multiple static assignment of variables may deteriorate the performance drastically. So, the recommendation
                                             is to use custom java code to initialise the variables. Default JavaScript engine configured is rhino . In case of script engine specific error, the JavaScript engine can be changed to nashorn or graal.js , by adding below property to CVP_HOME\conf\vxml.properties file: VXML.JsEngine = nashorn for nashorn . VXML.JsEngine = graal.js for graal.js . restart VXML Server Service |
|---|---|

| Step 1 | On the Settings tab, right-click the local variable
                                       			 you want to move up or down and choose Mark Variable . |
|---|---|
| Step 2 | Choose the location where you want to move the marked local
                                       			 variable, right-click and choose Move Variable . |