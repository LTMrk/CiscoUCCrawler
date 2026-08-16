---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-all-models-xsi-9-1-1-cuip-bk-p82b3b16-00-phones-services-application--5cf5546301
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes1_chapter_01001.html
retrieved_at: 2026-08-16T18:02:05.438078+00:00
---

Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

# Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

Updated: August 6, 2026

Chapter: IP Phone Service Administration and Subscription

## Chapter: IP Phone Service Administration and Subscription

# IP Phone Service Administration and Subscription

## Administration and Subscription Overview

Cisco Unified Communications Manager administrators maintain the list of services to which users can subscribe. Administrators
                           must use Cisco Unified Communications Manager Administration to add and administer Cisco Unified IP Phone services.

This chapter provides a brief overview about managing IP Phone services. For detailed up-to-date instructions, refer to the Cisco Unified Communications Manager Administration Guide available at the following URL:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

## Phone Service Administration Access

To access phone service administration, open Cisco Unified Communications Manager Administration and choose Device > Device Settings > Phone Services :

Phone services can have any number of parameters associated with them.

You can specify phone service parameters as optional or required, depending on how the phone service application defines them.

Users can subscribe to any service configured in their cluster, using their User Options web pages.

Service subscriptions currently occur on a device basis.

A URL constitutes the core of each service. When a service is chosen from the menu, the URL gets requested using HTTP, and
                              a server somewhere provides the content. The Service URL field shows this URL entry. For the services to be available, the
                              phones in the Cisco Unified Communications Manager cluster must have network connectivity to the server.

### Example

http://<servername>/ccmuser/sample/sample.asp

Where

<servername> designates a fully qualified domain name or an IP address.

## Phone Service Addition

To access phone service administration, open Cisco Unified Communications Manager Administration and choose Device > Device Settings > Phone Services :

The Cisco Unified Services Configuration page in Cisco Unified Communications Manager Administration contains the fields as
                              shown in the following table.

Service Information

Service Name

Enter the name of the service as it will display on the menu of available services in Cisco Unified CM User Options. Enter
                                          up to 32 characters for the service name.

ASCII Service Name

Enter the name of the service to display if the phone cannot display Unicode.

Service Description

Enter a description of the content that the service provides.

Service URL

Enter the URL of the server where the IP phone services application is located. Make sure that this server remains independent
                                          of the servers in your Cisco Unified Communications Manager cluster. Do not specify a Cisco Unified Communications Manager
                                          server or any server that is associated with Cisco Unified Communications Manager (such as a TFTP server or directory database
                                          publisher server).

For the services to be available, the phones in the Cisco Unified Communications Manager cluster must have network connectivity
                                          to the server.

When defining the service URL, you can embed a special #DEVICENAME# substitution tag within the URL. This tag provides a convenient
                                          method for IP phones to pass their device name to a web application server. For example, if a service URL was defined in Cisco
                                          Unified Communications Manager Administration as: http://myserver/myscript?name=#DEVICENAME#, when a phone actually makes
                                          the HTTP request for the service, the requested URL will appear as: http://myserver/myscript?name=SEP000123456789

Secure-Service URL

Enter the secure URL of the server where the Cisco Unified IP Phone services application is located. Make sure that this server
                                          remains independent of the servers in your Cisco Unified Communications Manager cluster. Do not specify a Cisco Unified Communications
                                          Manager server or any server that is associated with Cisco Unified Communications Manager (such as a TFTP server or publisher
                                          database server).

For the services to be available, the phones in the Cisco Unified Communications Manager cluster must have network connectivity
                                          to the server.

If you do not provide a Secure-Service URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities.

Service Category

Select a service application type.

Service Type

Select whether the service will be provisioned to the Services, Directories, or Messages button.

Service Vendor

For XML services, you can leave this field blank.

Service Version

For XML services, you can leave this field blank.

Enable

Select this check box to enable the service, or clear the check box to disable the service without deleting it.

You cannot delete default services. Use this field if a default service exists, but you do not want to make it available for
                                                      subscription.

Enterprise Subscriptions

Select this check box to automatically provision the new service to all devices in the enterprise without requiring individual
                                          subscription. If this option is selected, the service automatically gets provisioned and does not get presented for user subscription.

Be aware that this check box is available for selection only when the service is created. You cannot modify it.

## IP Phone Service Parameters Definition

Each service can have a list of parameters. You can use these parameters, which are appended to the URL when they are sent
                              to the server, to personalize a service for an individual user. Examples of parameters include stock ticker symbols, city
                              names, or user IDs. The service provider defines the semantics of a parameter.

The Cisco Unified IP Phone Service Parameter Configuration page in Cisco Unified Communications Manager Administration contains
                              the fields as described in the following table.

Service Parameter Information

Parameter Name

Enter the exact query string parameter to use when you build the subscription URL; for example, symbol.

Parameter Display Name

Enter a descriptive parameter name to display to the user in Cisco Unified CM User Options; for example, Ticker Symbol.

Default Value

Enter the default value for the parameter. This value displays to the user when a service is being subscribed to for the first
                                          time; for example, CSCO.

Parameter Description

Enter a description of the parameter. The user can access the text that is entered here while the user is subscribing to the
                                          service. The parameter description should provide information or examples to help users input the correct value for the parameter.

Parameter is Required

If the user must enter data for this parameter before the subscription can be saved, check the Parameter is Required check
                                          box.

Parameter is a Password (mask contents)

You can mask entries in Cisco Unified CM User Options, so asterisks display rather than the actual user entry. You may want
                                          to do this for parameters such as passwords that you do not want others to be able to view. To mask parameter entry, select
                                          the Parameter is a Password (mask contents) check box in the Configure IP phone service Parameter window in Cisco Unified
                                          Communications Manager Administration.

If you change the service URL, remove a Cisco Unified IP Phone service parameter, or change the Parameter Name of a phone
                                          service parameter for a phone service to which users are already subscribed, be sure to click Update Subscriptions to update
                                          all currently subscribed users with the changes. If you do not update subscriptions, users must resubscribe to the service
                                          to rebuild the URL correctly.

## User Service Subscription

End users can configure service subscriptions using the Cisco Unified CM User Options pages. After users log in and choose
                              a device, a list of services that are assigned to the phone display. The user can configure these services, adding additional
                              ones or removing unused services. These password-protected windows are authenticated using the LDAP directory.

Users can personalize their services using the User Options pages to:

Customize the name of the service.

Enter any available service parameters.

Review the description of each parameter.

After all the required fields are set, the user clicks Subscribe to add the services. A custom URL gets built and stored in
                              the database for this subscription. The service then appears on the device services list.

| Note | This chapter provides a brief overview about managing IP Phone services. For detailed up-to-date instructions, refer to the Cisco Unified Communications Manager Administration Guide available at the following URL: http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html |
|---|---|

| Field | Description |
|---|---|
| Service Information |
| Service Name | Enter the name of the service as it will display on the menu of available services in Cisco Unified CM User Options. Enter
                                          up to 32 characters for the service name. |
| ASCII Service Name | Enter the name of the service to display if the phone cannot display Unicode. |
| Service Description | Enter a description of the content that the service provides. |
| Service URL | Enter the URL of the server where the IP phone services application is located. Make sure that this server remains independent
                                          of the servers in your Cisco Unified Communications Manager cluster. Do not specify a Cisco Unified Communications Manager
                                          server or any server that is associated with Cisco Unified Communications Manager (such as a TFTP server or directory database
                                          publisher server). For the services to be available, the phones in the Cisco Unified Communications Manager cluster must have network connectivity
                                          to the server. When defining the service URL, you can embed a special #DEVICENAME# substitution tag within the URL. This tag provides a convenient
                                          method for IP phones to pass their device name to a web application server. For example, if a service URL was defined in Cisco
                                          Unified Communications Manager Administration as: http://myserver/myscript?name=#DEVICENAME#, when a phone actually makes
                                          the HTTP request for the service, the requested URL will appear as: http://myserver/myscript?name=SEP000123456789 |
| Secure-Service URL | Enter the secure URL of the server where the Cisco Unified IP Phone services application is located. Make sure that this server
                                          remains independent of the servers in your Cisco Unified Communications Manager cluster. Do not specify a Cisco Unified Communications
                                          Manager server or any server that is associated with Cisco Unified Communications Manager (such as a TFTP server or publisher
                                          database server). For the services to be available, the phones in the Cisco Unified Communications Manager cluster must have network connectivity
                                          to the server. Note If you do not provide a Secure-Service URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. | Note | If you do not provide a Secure-Service URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Note | If you do not provide a Secure-Service URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Service Category | Select a service application type. |
| Service Type | Select whether the service will be provisioned to the Services, Directories, or Messages button. |
| Service Vendor | For XML services, you can leave this field blank. |
| Service Version | For XML services, you can leave this field blank. |
| Enable | Select this check box to enable the service, or clear the check box to disable the service without deleting it. Note You cannot delete default services. Use this field if a default service exists, but you do not want to make it available for
                                                      subscription. | Note | You cannot delete default services. Use this field if a default service exists, but you do not want to make it available for
                                                      subscription. |
| Note | You cannot delete default services. Use this field if a default service exists, but you do not want to make it available for
                                                      subscription. |
| Enterprise Subscriptions | Select this check box to automatically provision the new service to all devices in the enterprise without requiring individual
                                          subscription. If this option is selected, the service automatically gets provisioned and does not get presented for user subscription. Note Be aware that this check box is available for selection only when the service is created. You cannot modify it. | Note | Be aware that this check box is available for selection only when the service is created. You cannot modify it. |
| Note | Be aware that this check box is available for selection only when the service is created. You cannot modify it. |

| Note | If you do not provide a Secure-Service URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
|---|---|

| Note | You cannot delete default services. Use this field if a default service exists, but you do not want to make it available for
                                                      subscription. |
|---|---|

| Note | Be aware that this check box is available for selection only when the service is created. You cannot modify it. |
|---|---|

| Field | Description |
|---|---|
| Service Parameter Information |
| Parameter Name | Enter the exact query string parameter to use when you build the subscription URL; for example, symbol. |
| Parameter Display Name | Enter a descriptive parameter name to display to the user in Cisco Unified CM User Options; for example, Ticker Symbol. |
| Default Value | Enter the default value for the parameter. This value displays to the user when a service is being subscribed to for the first
                                          time; for example, CSCO. |
| Parameter Description | Enter a description of the parameter. The user can access the text that is entered here while the user is subscribing to the
                                          service. The parameter description should provide information or examples to help users input the correct value for the parameter. |
| Parameter is Required | If the user must enter data for this parameter before the subscription can be saved, check the Parameter is Required check
                                          box. |
| Parameter is a Password (mask contents) | You can mask entries in Cisco Unified CM User Options, so asterisks display rather than the actual user entry. You may want
                                          to do this for parameters such as passwords that you do not want others to be able to view. To mask parameter entry, select
                                          the Parameter is a Password (mask contents) check box in the Configure IP phone service Parameter window in Cisco Unified
                                          Communications Manager Administration. |

| Note | If you change the service URL, remove a Cisco Unified IP Phone service parameter, or change the Parameter Name of a phone
                                          service parameter for a phone service to which users are already subscribed, be sure to click Update Subscriptions to update
                                          all currently subscribed users with the changes. If you do not update subscriptions, users must resubscribe to the service
                                          to rebuild the URL correctly. |
|---|---|