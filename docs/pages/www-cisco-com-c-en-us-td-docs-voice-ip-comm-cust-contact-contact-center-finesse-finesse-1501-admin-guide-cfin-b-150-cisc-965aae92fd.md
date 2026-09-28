---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-admin-guide-cfin-b-150-cisc-965aae92fd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/admin/guide/cfin_b_150_cisco-finesse-administration-guide/cfin_m_150_manage-third-party-gadgets.html
retrieved_at: 2026-08-21T12:05:04.677170+00:00
---

Cisco Finesse Administration Guide, Release 15.0(1)

# Cisco Finesse Administration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Manage Third-Party Gadgets

## Chapter: Manage Third-Party Gadgets

# Manage Third-Party Gadgets

## 3rdpartygadget Account

The 3rdpartygadget account is used to upload third-party gadgets to the Finesse server. Before you can use this account,
                              you must set the password.

Run the following command to set or reset the password of the 3rdpartygadget account (where password is the new password for the account):

utils reset_3rdpartygadget_password password

You must set or reset the password individually on each Cisco Finesse server because the password is not synchronized across
                              servers.

If you plan to upload third-party gadgets to the Finesse server, you must have a developer support services contract or work
                                          with a Cisco partner who has a developer support services contract. For more information about uploading third-party gadgets,
                                          see the Cisco Finesse Web Services Developer Guide .

The password for the 3rdpartygadget account must be between 5 and 32 characters long and cannot contain spaces or double quotes
                              (").

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

Because of browser caching and caching in Finesse web server, you must clear both the browser cache and the WebProxy cache
                                          before the gadget changes take effect.

After making changes to the gadget, clear the browser cache as per the browser settings and clear the Finesse web server cache
                                          using the following CLI command.

utils webproxy cache clear all —Clears the cache from the WebProxy service.

If you do not see the changes even after clearing both the browser and WebProxy caches, restart the Cisco Finesse Tomcat service
                                          by executing the following CLI command.

utils service restart Cisco Finesse Tomcat —Restarts the Cisco Finesse Tomcat service.

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

| Note | If you plan to upload third-party gadgets to the Finesse server, you must have a developer support services contract or work
                                          with a Cisco partner who has a developer support services contract. For more information about uploading third-party gadgets,
                                          see the Cisco Finesse Web Services Developer Guide . |
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

| Note | Because of browser caching and caching in Finesse web server, you must clear both the browser cache and the WebProxy cache
                                          before the gadget changes take effect. After making changes to the gadget, clear the browser cache as per the browser settings and clear the Finesse web server cache
                                          using the following CLI command. utils webproxy cache clear all —Clears the cache from the WebProxy service. If you do not see the changes even after clearing both the browser and WebProxy caches, restart the Cisco Finesse Tomcat service
                                          by executing the following CLI command. utils service restart Cisco Finesse Tomcat —Restarts the Cisco Finesse Tomcat service. |
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