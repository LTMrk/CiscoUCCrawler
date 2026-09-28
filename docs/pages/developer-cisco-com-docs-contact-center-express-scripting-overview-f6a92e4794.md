---
doc_id: developer-cisco-com-docs-contact-center-express-scripting-overview-f6a92e4794
source_url: https://developer.cisco.com/docs/contact-center-express/scripting-overview/
retrieved_at: 2026-09-01T17:34:00.815131+00:00
---

# What is Unified Contact Center Express Scripting?

Unified CCX provides an ability for developers to program the business logic of how to handle a Voice Call or an Http Contact (Web Action performed by a user) by the engine. The scripting involves building the business workflow using a proprietary domain specific programming tool, the Unified CCX Editor. These scripts created using the Unified CCX Editor can be saved as a file and uploaded to UCCX via the administration web and REST interface.

The Cisco Unified CCX Editor is a graphical programming environment for creating,
modifying, validating, and debugging telephony and multimedia application
scripts in a Cisco Unified CCX system. It enables you to develop a wide variety of interactive scripts. The Cisco Unified CCX Editor simplifies script development by providing blocks of contact-processing logic in easy-to-use Java-based steps. Each step has its own unique capabilities, from simple increment to generating and playing out prompts, obtaining user input, queueing calls, or performing complex database operations.

Although the steps are written in Java, you do not need to understand Java programming to build a Cisco Unified CCX script. You can assemble a script by dragging step icons from a palette on the left pane of the workspace to the design area on the right pane of the workspace.

The Cisco Unified CCX Editor supplies the code required to connect the steps; you provide the variable definitions and other parameters. You can validate and debug the completed script directly in the Cisco Unified CCX Editor.

# Technical Overview

- Palette pane : Use the Palette pane to choose the predefined steps to add to your custom script.

- Design pane : Use the Design pane to create your script.

- Message pane : Use the Message pane to view messages when you are validating or debugging a script.

- Variable pane : Use the Variable pane to create, modify, and view variables for your script.

## Example Script

The above screenshot is a simple queuing script which is associated with an application and is invoked upon dialing the respective Trigger associated to the script.

Once the Trigger is invoked (by the Customer dialing into the Contact Center), the script will traverse through the following path:

- Accept the Trigger contact

- Play a prompt to the Customer (WelcomePrompt in this example)

- Select an Agent from the given CSQ (CSQ is configured as a parameter here, which will take the input from Application created)

- If there is an Agent available to take the call in the given CSQ, the call will be Connected and the script will end

- If there are no available Agents in the queue the flow will be moving to the Queued Loop until a contact Is available to get Connected

# What can a developer build with the Scripting?

Developers can build custom IVR scripts with the Cisco Unified CCX Editor. The Cisco Unified CCX Editor simplifies script development by providing blocks of contact-processing logic in easy-to-use Java-based steps.

Each step has its own unique capabilities such as:

- Making REST API calls

- Parsing XML and JSON

- Providing context

- Obtaining statistics such as estimated wait time

- DB interaction capabilities

- The ability to act as a mini web server providing engine statistics using HTTP Trigger

- The ability to write custom Java-like code in steps

- The ability to reactive debug

- File I/O

- and many more

Developers can build scripts with a wide range of functionality from simple increment to generating and playing out prompts, obtaining user input, queueing calls, or performing complex database operations.

Please see the Scripting and Developer Series Guide for more details.

# What client specifications do I need to use the Unified CCX Editor?

To install the Cisco Unified CCX Editor independently of a Cisco Unified CCX
server, you need to install one of the following operating systems:

- Windows 8.1

- Windows 10

# How do I get the Unified CCX Editor?

The Unified CCX Editor can be downloaded from the Cisco Unified CCX Administration web interface.

- Login to the Cisco Unified CCX Administration web interface.

- Select Tools > Plug-ins .

- Select Cisco Unified CCX Editor to download the Unified CCX Editor.

# What license level is needed to use the Unified CCX Editor?

The Unified CCX Editor is available for all Unified CCX license packages:

- Unified CCX Standard (designed for entry-level users) :  Includes the steps necessary for creating basic Unified CCX applications, including IP Phone Agent (IPPA) and skills-based routing. The standard license is only available for CCX versions 11.0 and below.

- Unified CCX Enhanced (designed for enterprise-level users) : Includes all functions of Unified CCX Standard, plus support for priority queuing. Includes a license to enable custom Java extensions.

- Unified CCX Premium : Adds full Unified IP IVR support (except for Unified ICM integration) including database integration, Voice eXtensible Markup Language (VoiceXML), HTML web integration, custom Java extensions, and e-Notification services. The outbound feature is now bundled with the Premium package. You will receive one outbound seat free with each premium seat. The maximum number of outbound seats supported will be based on the hardware type.

# Next Steps

The best way to really understand the Unified CCX Script Editor is to try it for yourself. Please proceed to the Getting Started page to learn just how easy it is.

Next