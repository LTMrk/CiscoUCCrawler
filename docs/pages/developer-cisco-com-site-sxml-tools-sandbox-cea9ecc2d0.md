---
doc_id: developer-cisco-com-site-sxml-tools-sandbox-cea9ecc2d0
source_url: https://developer.cisco.com/site/sxml/tools/sandbox/
retrieved_at: 2026-08-25T21:10:43.192033+00:00
---

# Sandbox

To begin working with Serviceability APIs, you will need to create a lab that has Cisco Unified Communications Manager (Unified CM) installed on a server that is accessible from your application server.

DevNet registered users can access the DevNet Sandbox for development purposes. The DevNet Sandbox program is currently a FREE 24x7 remote access lab service. It provides developers with access to labs built for integrating/working with Cisco technologies.

Reserve a lab:

- Login to DevNet

- Navigate to the DevNet Sandbox Overview page

- Click on the green button to the right "Go To Sandbox"

- Register and login with DevNet Sandbox

- Select Reservation Based Labs

- Select the latest dedicated Collaboration Lab and complete the form to reserve the lab. You can find more detailed information about reserving a lab by reading Cisco DevNet Sandbox Lab Guide .

Connect to a lab:

You will receive an e-mail with instructions to connect to the lab via VPN with your own credentials. You must be on VPN to access the lab. Your credentials will expire when your reservation ends.  When your reservation expires, you will need to reserve the lab again and use the new set of credentials emailed to you.

Setup a lab:

- To access the CUCM Admin website, enter the IP address of CUCM publisher in your browser. You can find the IP address by looking at the lab’s topology after you reserve it. See image below:

- Use the getting started page to setup your lab:

- a. The lab already has all services running, so you shouldn’t need to make any changes.

- b. The lab also has multiple devices configured, but not registered. See Pre-Provisioned User and Device Info . Some of the APIs such as RisPort will require at least one device registered to Cisco Unified CM.  The easiest device to add and register is a softphone, like Cisco IP Communicator . Here are instructions to register an IP Phone.

- c. Create an application user in Unified CM to authorize your application’s requests. For simplicity and testing purposes only, you could also use admin credentials found on the lab’s topology page to authorize your application’s requests. See image below:

*You may have to adjust the icon level of the topology to see the information above

Run that app:

- Follow the instructions to use SOAP UI to send a request

- Use the user’s credentials to authenticate the request

- Send the request to the Unified CM server in the lab while on VPN

##### Ready for your own lab?

If you are a member of the Solution Partner Program you can get discounts for on the Unified CM Not-for-Resale bundles. This program allows partners to acquire the core components of Cisco Unified Communications System for use in non-revenue generating activities such as labs, demos, and internal course development and training.

For more information about the "Not For Resale" Program, visit the Developer Discount Purchase section.