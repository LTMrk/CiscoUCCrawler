---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-c55aa0ae3e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-programming-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio/ccvp_b_1251-programming-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio_chapter_01101.html
retrieved_at: 2026-08-21T17:35:56.976568+00:00
---

Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio, Release 12.5(1)

# Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio, Release 12.5(1)

Updated: February 2, 2020

Chapter: On Error Notification

## Chapter: On Error Notification

- On Error Notification

- On Error Notification

# On Error Notification

## On Error Notification

The error notification process can only be implemented using Java because when an error occurs, one desires the most reliable
                           method for reporting that error. There is no guarantee an HTTP request to a URI could even be generated, a response received
                           and the XML parsed without incurring another error.

The on error notification class is built in Java by implementing the class GlobalErrorInterface found in the com.audium.server.proxy package. It contains a single method named doError that acts as the execution method for the class. The method receives nine arguments containing information on the status
                           of the application and VXML Server at the time the error occurred. No API classes are passed to this method because accessing
                           them may cause additional errors due to their complexity. Any of the arguments may be null if the data cannot be determined or the error is such that it is not related to a specific application.

The arguments are: the VXML Server session ID (as a String ), the name of the application (as a String ), the ANI (as a String ), the DNIS (as a String ), the IIDIGITS (as a String ), the UUI (as a String ), an ArrayList of String types listing the elements visited in the call up to the time the error occurred, an ArrayList of the String types listing the exit states for each of the elements, and a HashMap containing the session data created up to the time the error occurred (the key of the HashMap is the name of the session data, and the value is the session data value).

The on error notification class must be deployed in the common directory of VXML Server since classes placed there are shared across applications.

To configure VXML Server to use this class if an error occurs, a file named global_config.xml found in the conf directory of VXML Server must be used. This XML file contains a tag named <error_class> that should encapsulate the full Java name of this class (package name included). The changes will take effect only the next
                           time the Java application server on which VXML Server is installed is restarted.