---
doc_id: developer-cisco-com-docs-finesse-upload-third-party-gadgets-30f3b785be
source_url: https://developer.cisco.com/docs/finesse/upload-third-party-gadgets/
retrieved_at: 2026-09-07T14:07:59.148602+00:00
---

# Upload Third-Party Gadgets

After you set the password for the 3rdpartygadget account, you can use SFTP to upload third-party gadgets to the Finesse server, as illustrated in the following example. Note that third-party gadget files must be .xml files. It does not support .jsp files.

Finesse allows you to upload third-party gadgets to your own web server, however, you must ensure that the Finesse server has access to your web server.

Code Snippet

```
my_workstation:gadgets user$ sftp 3rdpartygadget@ < finesse > 3rdpartygadget@ < finesse > 's password:
Connected to < finesse > .
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

When you add a gadget to the desktop layout, that gadget can be referenced using a relative path. For more information on adding third party gadgets to the Finesse desktop layout, see the section Manage Desktop Layout in the Cisco Finesse Administration Guide .

To include the gadget that was uploaded in the previous example in the desktop layout, add the following XML (highlighted) to the layout:

Code Snippet

```
< finesseLayout xmlns = " http://www.cisco.com/vtg/finesse " > < layout > < role > Agent </ role > < page > < gadget > /desktop/gadgets/CallControl.jsp </ gadget > < gadget > /3rdpartygadget/files/HelloWorld.xml </ gadget > </ page > ... </ layout > < layout > < role > Supervisor </ role > < page > < gadget > /desktop/gadgets/CallControl.jsp </ gadget > < gadget > /3rdpartygadget/files/HelloWorld.xml </ gadget > </ page > ... </ layout > </ finesseLayout >
```

You cannot delete, rename or change permissions of a folder while using SFTP in 3rd party gadget accounts for Unified CCX deployments. To perform these actions, SELinux has to be in permissive mode. This can be accomplished by running the following CLI command:

utils os secure permissive

Because of browser caching and caching in the Finesse web server, you may need to clear the browser cache or restart the Cisco Finesse Tomcat service before gadget changes take effect. If you make a change to a gadget and the change is not reflected on the Finesse desktop, clear your browser cache.

If you do not see the changes after you clear the browser cache, use the following CLI command to restart the Cisco Finesse Tomcat service:

admin:utils service restart Cisco Finesse Tomcat

## Third-Party Gadget Limitations

Third-party gadgets must be .xml files. You cannot use .jsp files.

| Note | Finesse allows you to upload third-party gadgets to your own web server, however, you must ensure that the Finesse server has access to your web server. |
|---|---|

| Note | You cannot delete, rename or change permissions of a folder while using SFTP in 3rd party gadget accounts for Unified CCX deployments. To perform these actions, SELinux has to be in permissive mode. This can be accomplished by running the following CLI command: utils os secure permissive |
|---|---|

| Note | Because of browser caching and caching in the Finesse web server, you may need to clear the browser cache or restart the Cisco Finesse Tomcat service before gadget changes take effect. If you make a change to a gadget and the change is not reflected on the Finesse desktop, clear your browser cache. If you do not see the changes after you clear the browser cache, use the following CLI command to restart the Cisco Finesse Tomcat service: admin:utils service restart Cisco Finesse Tomcat |
|---|---|