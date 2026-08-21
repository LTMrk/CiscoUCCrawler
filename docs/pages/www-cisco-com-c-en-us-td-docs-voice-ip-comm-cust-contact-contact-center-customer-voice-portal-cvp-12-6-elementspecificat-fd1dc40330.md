---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-fd1dc40330
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_e1d289f2_00_email.html
retrieved_at: 2026-08-21T17:25:06.137570+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Email

## Chapter: Email

# Email

The Email action element sends messages to the
                                    				provided email address. Additionally the message can include attachments. The
                                    				application server must be configured to set a JNDI datasource for mail
                                    				sessions. The to and tolist fields are not individually required;
                                    				however, at least one must be defined. Email addresses are not verified for
                                    				syntax or validity. Attachments that do not exist will be skipped but the
                                    				message will still be sent. Repeated email addresses are sent the message
                                    				multiple times. The toList , ccList and bccList settings must refer to session data
                                    				variables that holds a ResultSetList Java class holding a list of email
                                    				addresses (retrieved from a Database element).

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

jndiName

(JNDI Name)

string

Yes

true

true

None

The
                                          configured JNDI datasource for mail sessions under the java application
                                          server.

to

(To)

string

No

false

true

None

The
                                          email address this message will be sent to. This setting is repeatable so that
                                          each setting value contains a separate email address.

toList

(To List)

string

No

true

true

None

The
                                          name of a session data variable containing a ResultSetList object holding a
                                          list of email addresses as retrieved from a Database element. The email will be
                                          sent to every address in this list.

from

(From)

string

Yes

true

true

None

The
                                          email address this message will be sent from.

cc

(Cc)

string

No

false

true

None

The
                                          email address this message will be carbon copied to. This setting is repeatable
                                          so that each setting value contains a separate email
                                          address.

ccList

(Cc List)

string

No

true

true

None

The name of a session data variable containing a
                                          ResultSetList object holding a list of email addresses as retrieved from a
                                          Database element. The email will be carbon copied to each address in this
                                          list.

bcc

(Bcc)

string

No

false

true

None

The
                                          email address this message will be blind carbon copied to. This setting is
                                          repeatable so that each setting value contains a separate email
                                          address.

bccList

(Bcc List)

string

No

true

true

None

The name of a session data variable containing a
                                          ResultSetList object holding a list of email addresses as retrieved from a
                                          Database element. The email will be blind carbon copied to each address in this
                                          list.

subject

(Subject)

string

No

true

true

None

Subject field of the email.

attachment

(Attachment)

string

No

false

true

None

Full
                                          local path of the file to be attached. This setting is repeatable so that each
                                          setting value contains a reference to separate
                                          attachments.

messageBody

(Message Body)

string

Yes

true

true

None

The message body of the
                                          email.

## Exit States

Name

Notes

done

The
                                          database query successfully
                                          completed.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Notification

com.audium.server.action.email.EmailAction

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

## Set Up Email
                        	 Element

For the Email element to work, add a mail session under Tomcat
                              		  manually.

Step 1

Edit the \Tomcat\conf\context.xml file.

Step 2

Within the <Context> </Context> tags, add the
                                       			 following:

```
<Resource name="mail/ ChrisMail " 
type="javax.mail.Session"
mail.smtp.host="xmb-sjc-22d.amer.cisco.com"/>
```

Here, the name must be mail/ ANY_NAME_YOU_CHOOSE , type must be javax.mail.Session , and mail.smtp.host must be a working SMTP server.

In Studio, edit the configuration of the Email element in
                                                      				  question. Set the JNDI name to the ANY_NAME_YOU_CHOOSE portion
                                                      				  of what you entered in the Tomcat settings. In the preceding example, you can
                                                      				  enter ChrisMail but ensure that you
                                                      				  do not include the mail/ portion here.

| The Email action element sends messages to the
                                    				provided email address. Additionally the message can include attachments. The
                                    				application server must be configured to set a JNDI datasource for mail
                                    				sessions. The to and tolist fields are not individually required;
                                    				however, at least one must be defined. Email addresses are not verified for
                                    				syntax or validity. Attachments that do not exist will be skipped but the
                                    				message will still be sent. Repeated email addresses are sent the message
                                    				multiple times. The toList , ccList and bccList settings must refer to session data
                                    				variables that holds a ResultSetList Java class holding a list of email
                                    				addresses (retrieved from a Database element). |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| jndiName (JNDI Name) | string | Yes | true | true | None | The
                                          configured JNDI datasource for mail sessions under the java application
                                          server. |
| to (To) | string | No | false | true | None | The
                                          email address this message will be sent to. This setting is repeatable so that
                                          each setting value contains a separate email address. |
| toList (To List) | string | No | true | true | None | The
                                          name of a session data variable containing a ResultSetList object holding a
                                          list of email addresses as retrieved from a Database element. The email will be
                                          sent to every address in this list. |
| from (From) | string | Yes | true | true | None | The
                                          email address this message will be sent from. |
| cc (Cc) | string | No | false | true | None | The
                                          email address this message will be carbon copied to. This setting is repeatable
                                          so that each setting value contains a separate email
                                          address. |
| ccList (Cc List) | string | No | true | true | None | The name of a session data variable containing a
                                          ResultSetList object holding a list of email addresses as retrieved from a
                                          Database element. The email will be carbon copied to each address in this
                                          list. |
| bcc (Bcc) | string | No | false | true | None | The
                                          email address this message will be blind carbon copied to. This setting is
                                          repeatable so that each setting value contains a separate email
                                          address. |
| bccList (Bcc List) | string | No | true | true | None | The name of a session data variable containing a
                                          ResultSetList object holding a list of email addresses as retrieved from a
                                          Database element. The email will be blind carbon copied to each address in this
                                          list. |
| subject (Subject) | string | No | true | true | None | Subject field of the email. |
| attachment (Attachment) | string | No | false | true | None | Full
                                          local path of the file to be attached. This setting is repeatable so that each
                                          setting value contains a reference to separate
                                          attachments. |
| messageBody (Message Body) | string | Yes | true | true | None | The message body of the
                                          email. |

| Name | Notes |
|---|---|
| done | The
                                          database query successfully
                                          completed. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Notification | com.audium.server.action.email.EmailAction |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |

| Step 1 | Edit the \Tomcat\conf\context.xml file. |
|---|---|
| Step 2 | Within the <Context> </Context> tags, add the
                                       			 following: <Resource name="mail/ ChrisMail " 
type="javax.mail.Session"
mail.smtp.host="xmb-sjc-22d.amer.cisco.com"/> Here, the name must be mail/ ANY_NAME_YOU_CHOOSE , type must be javax.mail.Session , and mail.smtp.host must be a working SMTP server. Note In Studio, edit the configuration of the Email element in
                                                      				  question. Set the JNDI name to the ANY_NAME_YOU_CHOOSE portion
                                                      				  of what you entered in the Tomcat settings. In the preceding example, you can
                                                      				  enter ChrisMail but ensure that you
                                                      				  do not include the mail/ portion here. | Note | In Studio, edit the configuration of the Email element in
                                                      				  question. Set the JNDI name to the ANY_NAME_YOU_CHOOSE portion
                                                      				  of what you entered in the Tomcat settings. In the preceding example, you can
                                                      				  enter ChrisMail but ensure that you
                                                      				  do not include the mail/ portion here. |
| Note | In Studio, edit the configuration of the Email element in
                                                      				  question. Set the JNDI name to the ANY_NAME_YOU_CHOOSE portion
                                                      				  of what you entered in the Tomcat settings. In the preceding example, you can
                                                      				  enter ChrisMail but ensure that you
                                                      				  do not include the mail/ portion here. |

| Note | In Studio, edit the configuration of the Email element in
                                                      				  question. Set the JNDI name to the ANY_NAME_YOU_CHOOSE portion
                                                      				  of what you entered in the Tomcat settings. In the preceding example, you can
                                                      				  enter ChrisMail but ensure that you
                                                      				  do not include the mail/ portion here. |
|---|---|