---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1251-admin-guide-cfin-b-1251-adm-4a46183dac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1251/admin/guide/cfin_b_1251-administration-guide/cfin_b_1251-administration-guide_chapter_01011.html
retrieved_at: 2026-08-21T10:16:56.256013+00:00
---

Cisco Finesse Administration Guide, Release 12.5(1)

# Cisco Finesse Administration Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Manage Third-Party Gadgets

## Chapter: Manage Third-Party Gadgets

# Manage Third-Party Gadgets

## 3rdpartygadget Account

The 3rdpartygadget account is used to upload third-party gadgets to the Finesse server. Before you can use this account,
                              you must set the password.

If you plan to upload third-party gadgets to the Finesse server, you must have a developer support services contract or work
                                          with a Cisco partner who has a developer support services contract. For more information about uploading third-party gadgets,
                                          see the Cisco Finesse Web Services Developer Guide .

To set (or reset) the 3rdpartygadget account password, access the CLI and run the following command:

You are prompted to enter a password. After you enter a password, you are prompted to confirm the password.

If the third-party gadget hosted in Cisco Finesse is sending a REST request to the web server via Shindig, using the SHA256
                                             certificate, the maximum key length cannot exceed 2048.

Third-party gadgets are migrated across upgrades and included in DRS backup and restore.

## Upload Third-Party Gadgets

After you set the password for the 3rdpartygadget account, you can use SFTP to upload third-party gadgets to the Finesse server,
                              as illustrated in the following example. Note that third-party gadget files must be .xml files. It does not support .jsp files.

Finesse allows you to upload third-party gadgets to your own web server, however, you must ensure that the Finesse server
                                          has access to your web server.

```
my_workstation:gadgets user$ sftp 3rdpartygadget@<finesse>
3rdpartygadget@<finesse>'s password:
Connected to <finesse>.
sftp> cd /files
sftp> put HelloWorld.xml
Uploading HelloWorld.xml to /files/HelloWorld.xml
HelloWorld.xml                                                                   
sftp> exit
```

After you upload a gadget, it is available under the following URL:

https ://<finesse>/3rdpartygadget/files/

To access the gadget uploaded in the previous example, use the following URL:

https ://<finesse>/3rdpartygadget/files/HelloWorld.xml

When you add a gadget to the desktop layout, that gadget can be referenced using a relative path. For more information on
                              adding third party gadgets to the Finesse desktop layout, see the section Manage Desktop Layout in the Cisco Finesse Administration Guide .

To include the gadget that was uploaded in the previous example in the desktop layout, add the following XML (highlighted)
                              to the layout:

```
<finesseLayout xmlns="http://www.cisco.com/vtg/finesse">
      <layout>
        <role>Agent</role>
        <page>
          <gadget>/desktop/gadgets/CallControl.jsp</gadget> <gadget>/3rdpartygadget/files/HelloWorld.xml</gadget> </page>
        ...
      </layout>
      <layout>
        <role>Supervisor</role>
        <page>
          <gadget>/desktop/gadgets/CallControl.jsp</gadget> <gadget>/3rdpartygadget/files/HelloWorld.xml</gadget> </page>
        ...
      </layout>
    </finesseLayout>
```

You cannot delete, rename or change permissions of a folder while using SFTP in 3rd party gadget accounts for Unified CCX
                                          deployments. To perform these actions, SELinux has to be in permissive mode. This can be accomplished by running the following
                                          CLI command:

utils os secure permissive

Because of browser caching and caching in the Finesse web server, you may need to clear the browser cache or restart the Cisco
                                          Finesse Tomcat service before gadget changes take effect. If you make a change to a gadget and the change is not reflected
                                          on the Finesse desktop, clear your browser cache.

If you do not see the changes after you clear the browser cache, use the following CLI command to restart the Cisco Finesse
                                          Tomcat service:

admin:utils service restart Cisco Finesse Tomcat

### Automatic Compression of Third-party Gadget Resources

To optimize the browser resource fetching and reduce network bandwidth, the Finesse server automatically compresses the third-party
                              gadget resources into gz format. A watcher service running in the Finesse server monitors the third-party gadgets folder for
                              any updates. It compresses the resource files such as image files and css accordingly, to generate the compressed gz file.
                              The request originating from the browser, Finesse desktop adds HTTP request header Accept-Encoding:gzip and the response from
                              the Finesse server includes Content-Encoding:gzip HTTP header to achieve the same.

### Third-party Gadget Limitations

Third-party gadgets must be .xml files. You cannot use .jsp files.

## Certificates for Third-PartyGadgets

Install the external server's certificates into Cisco Finesse to establish a secure communication between Cisco Finesse and
                              the external server using the shindig proxy. Create a certificate for the external server, ensuring the server's FQDN is included
                              in both the Common Name (CN) and the Subject Alternative Name (SAN) attributes. The certificate can be either CA-signed or
                              self-signed.

Ensure the certificate is valid, non-expired X.509 certificate with Key Usage (KU) set to Digital Signature, Key Encipherment,
                                          and Data Encipherment, and Extended Key Usage (EKU) set to TLS Web Server Authentication and TLS Web Client Authentication.

To install certificates into Cisco Finesse, do the following:

Step 1

Log into Cisco Unified OS Administration on the primary Finesse server using the following URL: https://FQDN of Finesse server:8443/cmplatform .

Step 2

Select Security > Certificate Management > Upload Certificate/Certificate chain .

Step 3

Upload the certificate.

Select tomcat-trust from the Certificate Purpose drop-down list.

In the Upload File field, click Browse and navigate to the obtained external server certificate file.

Click Upload .

Step 4

Reboot the Cisco Finesse server.

Step 5

Perform these steps for both Side A and Side B of the Cisco Finesse Server.

For a CA-signed certificate, install the root, intermediate, and actual (external server) certificates in the correct order.

Enable the shindig allowed list to allow the Finesse server to communicate with the external server using the shindig proxy.
                                                            For more information, see Gadget Source Allowed List CLI .

## Cisco Webex Experience Management

Cisco Webex Experience Management ( Experience Management ) is the platform for Customer Experience Management (CEM), integrated with powerful tools that allow you to see your business
                              from your customers' perspective. Experience Management has all the sophisticated features and functionality including customer journey mapping, text analytics, and predictive modeling
                              in a single point-n-click platform.

For more information, see the Cisco Webex Experience Management Integration section in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Cloud Connect is a component that hosts services that allow customers to use cloud capabilities such as Cisco Webex Experience Management . The administrator can configure the Cloud Connect server settings in the Finesse administration console to contact the Cisco
                              cloud services. For more information, see Cloud Connect Server Settings .

### Configure Experience Management Gadgets for Finesse Desktop

Experience Management Activation Team provides the details to log in to Experience Management . For more information, see Cisco Webex Experience Management Activation .

Gadgets are displayed by default in the Spaces tab of the Experience Management . To know more about default gadgets and derive meaningful insights from them, see Cisco Webex Experience Management Gadgets .

To export the Cisco Finesse gadget code from Experience Management , see Export Cisco Finesse Gadget Code .

To add Experience Management gadgets in Finesse desktop layout, see Add Experience Management Gadgets .

#### Experience Management Gadgets—Task Activity Notification

This is supported from Cisco Finesse, Release 12.5(1) ES3 onwards.

TaskActivityNotification API is a mechanism by which the Finesse desktop can now provide a way for gadgets to sense the digital channel task worked
                                 on by an agent, across different media. The notifications inform the desktop and other subscribers about which non-voice media
                                 dialog is currently selected or de-selected by the agent.

This can be used for showing or processing the relevant information associated with the task activity automatically, in supporting
                                 gadgets, which subscribe for these activity notifications, when the agent switches between different tasks.

The feature requires participating gadgets to publish and subscribe for the activity notifications. The Finesse desktop by
                                             itself cannot provide these notifications or provide task activity processing based on these notifications.

The implementation of task activity notification is provided by digital channel gadgets such as Cisco Enterprise Chat and
                                 Email (ECE). The ECE gadget provides task notifications, and Cisco Webex Experience Management gadget subscribes and displays customer journey information corresponding to the task which is currently active.

For more information on the TaskActivityNotification API, see Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

For more information on digital survey, see the Webex Experience Management Digital Channel chapter in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

For more information on Cisco Enterprise Chat and Email, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html .

| Note | If you plan to upload third-party gadgets to the Finesse server, you must have a developer support services contract or work
                                          with a Cisco partner who has a developer support services contract. For more information about uploading third-party gadgets,
                                          see the Cisco Finesse Web Services Developer Guide . |
|---|---|

| Note | If the third-party gadget hosted in Cisco Finesse is sending a REST request to the web server via Shindig, using the SHA256
                                             certificate, the maximum key length cannot exceed 2048. |
|---|---|

| Note | Third-party gadgets are migrated across upgrades and included in DRS backup and restore. |
|---|---|

| Note | Finesse allows you to upload third-party gadgets to your own web server, however, you must ensure that the Finesse server
                                          has access to your web server. |
|---|---|

| Note | You cannot delete, rename or change permissions of a folder while using SFTP in 3rd party gadget accounts for Unified CCX
                                          deployments. To perform these actions, SELinux has to be in permissive mode. This can be accomplished by running the following
                                          CLI command: utils os secure permissive |
|---|---|

| Note | Because of browser caching and caching in the Finesse web server, you may need to clear the browser cache or restart the Cisco
                                          Finesse Tomcat service before gadget changes take effect. If you make a change to a gadget and the change is not reflected
                                          on the Finesse desktop, clear your browser cache. If you do not see the changes after you clear the browser cache, use the following CLI command to restart the Cisco Finesse
                                          Tomcat service: admin:utils service restart Cisco Finesse Tomcat |
|---|---|

| Note | Ensure the certificate is valid, non-expired X.509 certificate with Key Usage (KU) set to Digital Signature, Key Encipherment,
                                          and Data Encipherment, and Extended Key Usage (EKU) set to TLS Web Server Authentication and TLS Web Client Authentication. |
|---|---|

| Step 1 | Log into Cisco Unified OS Administration on the primary Finesse server using the following URL: https://FQDN of Finesse server:8443/cmplatform . |
|---|---|
| Step 2 | Select Security > Certificate Management > Upload Certificate/Certificate chain . |
| Step 3 | Upload the certificate. Select tomcat-trust from the Certificate Purpose drop-down list. In the Upload File field, click Browse and navigate to the obtained external server certificate file. Click Upload . |
| Step 4 | Reboot the Cisco Finesse server. |
| Step 5 | Perform these steps for both Side A and Side B of the Cisco Finesse Server. Note For a CA-signed certificate, install the root, intermediate, and actual (external server) certificates in the correct order. Enable the shindig allowed list to allow the Finesse server to communicate with the external server using the shindig proxy.
                                                            For more information, see Gadget Source Allowed List CLI . | Note | For a CA-signed certificate, install the root, intermediate, and actual (external server) certificates in the correct order. Enable the shindig allowed list to allow the Finesse server to communicate with the external server using the shindig proxy.
                                                            For more information, see Gadget Source Allowed List CLI . |
| Note | For a CA-signed certificate, install the root, intermediate, and actual (external server) certificates in the correct order. Enable the shindig allowed list to allow the Finesse server to communicate with the external server using the shindig proxy.
                                                            For more information, see Gadget Source Allowed List CLI . |

| Note | For a CA-signed certificate, install the root, intermediate, and actual (external server) certificates in the correct order. Enable the shindig allowed list to allow the Finesse server to communicate with the external server using the shindig proxy.
                                                            For more information, see Gadget Source Allowed List CLI . |
|---|---|

| Note | This is supported from Cisco Finesse, Release 12.5(1) ES3 onwards. |
|---|---|

| Note | The feature requires participating gadgets to publish and subscribe for the activity notifications. The Finesse desktop by
                                             itself cannot provide these notifications or provide task activity processing based on these notifications. |
|---|---|