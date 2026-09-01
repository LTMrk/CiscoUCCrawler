---
doc_id: sec-cloudapps-cisco-com-security-center-resources-framework-segmentation-html-a18b13cd01
source_url: https://sec.cloudapps.cisco.com/security/center/resources/framework_segmentation.html
retrieved_at: 2026-09-01T14:09:26.287941+00:00
---

Home / Cisco Security

A Framework to Protect Data Through Segmentation

# A Framework to Protect Data Through Segmentation

Contents

Introduction Data-Driven Segmentation Framework Segmentation Strategy Acknowledgments References

# Introduction

The concept of segmentation is nothing new. In ancient history, Romans created fighting units based on the ethnic and geographic identity of captured warriors. The idea was simple: group the warriors with similar backgrounds together so they can bond and eventually become better fighting units. Throughout history, this concept has been used as a basis for creating religious, ethnic, geographic, gender-based, and political groups [1] . As we look at the digital world, organizations have been performing user, traffic, or data segmentation through logical or physical means to protect core parts of their infrastructure.

Consolidating and centralizing the network infrastructure has been a key driver for segmentation. Previously isolated application infrastructures are now migrating to common shared physical and virtual networks that require separation to maintain some level of isolation. Similarly, networks have gone through a dramatic shift over the past few years with the introduction of virtualization, containers, smart phones, tablets, wireless connectivity and, of late, the Internet of Things (IoT). Organizations have used policy enforcement through L2 technologies such as VLANs, virtual routing and forwarding (VRF), and virtual firewalls as popular methods of providing network segmentation. The obvious question that comes to mind is, if organizations are already segmenting their network components, why do we need to discuss this topic? Before we answer this question, let us present a few data-points.

Network Designs: The traditional network architectures were built by placing the jewels of the crown (the data) in a well-guarded castle (the data-center). You get a comfortable feeling that all your critical resources are protected by a strong perimeter and nothing can pass through your defenses if not explicitly allowed. The biggest flaw with this design is: What if an unauthorized entity is already inside the castle? What if the unauthorized entity already has access to the jewels? What if the unauthorized entity has found a way to move the jewels out of your castle?

Organizations with limited segmentation and hundreds of users and applications typically experience the N*M problem, where N is the number of user groups and M is the number of critical resources, as shown in Figure 1. In plain English, every user group has access to pretty much every application in the enterprise network.

Figure 1: User Group to Resource (N*M) Relationship

The N*M problem gets worse if access is provided at an individual user level without grouping users by a set of common characteristics. Using the principle of least privilege helps simplify this problem by explicitly allowing user groups to access authorized resources. If the authorized resources are grouped together for each user group, the magnitude of this issue is reduced to just N+M. Take a closer look at the direction of the arrows in Figure 2, which illustrates a one-way segmentation policy allowing user groups to have appropriate access to the authorized resources.

Figure 2: User Group to Resource (N+M) Relationship

Data Breaches: We can all agree that the security landscape has changed in the last few years. Cyber attacks are becoming more sophisticated and targeted. If you look at recent data breaches, one thing that stands out is the layout of those networks. To keep up with business demand, most companies with large networks overlook most aspects of security, at times rendering their networks virtually flat. Additionally, most organizations have limited traffic visibility and lack properly defined segmentation policies. These data breaches demonstrate that once malicious actors have penetrated your perimeter defenses, they can roam freely in your network. As part of their reconnaissance activity, they try to determine ways to access critical resources and data. If a network is flat and users are able to access any resource with only limited security controls in place, such as authentication or IP-based access-control lists, then there is very little work an attacker needs to do to exploit those gaps.

Business Objectives: The two main goals of an organization are profitability and productivity. In many cases, organizations end up growing their network infrastructure to keep up with the demand of users and consumers. This problem is usually exacerbated by inorganic growth through acquisitions where two or more networks get connected through virtual tunnels as part of the integration process. This becomes a band-aid when quick integration is needed and security becomes an afterthought.

Application Security: In the past, applications and services were simpler and not as prevalent in the enterprise. Only a handful of applications were used throughout an enterprise by a select group of users. The applications were placed in a data center protected by a set of security and monitoring products. Although this model is relatively simple, it lacks protection for the applications that are hosted within the data center. Additionally, applications are usually grouped and separated by firewalls. However, this model lacks protection for communication between two apps when they are a part of the same app group.

User and Data Mobility: Users are not confined to the physical perimeter of an office. In this digital era there are no boundaries. Conventional data protection models do not apply anymore. Users can be anywhere, using any device, accessing data anytime, and connected through wired, wireless, or mobile infrastructure. With the evolution of smart devices, access to data is not restricted to corporate-issued devices. It does not matter how secure your castle is if the jewels are not inside the castle. Data itself could be anywhere – enterprise data center, cloud (public, private, hybrid), or a partner’s network, to name a few possibilities.

Data Visibility and Monitoring: More than 50 percent of cyber attacks are not even detected by the organization for months. If you do not have full visibility into your IT infrastructure, if you do not know who is accessing your network, what they are doing, where they are coming from, what devices they are using, and how they are hopping from one part of the network to another, how do you position yourself to defend against the threats they pose (intentionally or unintentionally, directly or indirectly)? Monitoring becomes an even bigger challenge with a lack of defined zones to determine traffic patterns.

Once acceptable security measures such as segmenting the network, configuring VLANs, deploying firewalls, and creating virtual routing tables no longer suffice. Placing users and apps into VLANs and filtering traffic through access-control lists achieves limited traffic separation. With network virtualization, cloud adoption, and proliferation of devices, it is imperative to look at the entire context of the connection before allowing access to critical data. With cyber threats evolving , providing segmentation strictly at the network layer is not enough to ensure complete data protection.

# Data-Driven Segmentation Framework

What is needed is a new approach that can cater to today’s application-focused business environment, that can combine threat intelligence from various sources, and that can build a complete context around end-to-end data connections. This is an approach that can dynamically compartmentalize these data connections based on the understanding of applications, users, consumers, threat actors, and devices by building appropriate access-control methods. Currently there is no framework that breaks an infrastructure into individual components, builds connections between the relevant components, and then applies access-control models for complete traffic separation. We need a framework that is beyond the technical controls and products that are often deployed as band-aids to address these security concerns, a framework that provides senior management and network architects a blueprint to ensure that segmentation is an indispensable part of the overall strategy.

This paper presents a framework, shown in Figure 3, that centers around the business-critical resources of an enterprise. This framework helps to identify elements requiring access to those resources, builds walls around those elements, and then applies an access-control policy to authorize connections. Completing the segmentation process exercise described in this paper forces organizations to evaluate their cybersecurity program in detail, as true segmentation can only be achieved once all parts of the enterprise are evaluated at a micro level, including breaking up the infrastructure components into objects and building appropriate relationships.

Figure 3: Data-Driven Segmentation Framework

The framework is composed of the following components:

Business Critical Resource: The proposed framework starts by logically breaking up the network infrastructure and placing the business-critical resource at the center of the architecture. The business-critical resource could be anything you want to protect from unauthorized users or objects. For example, if you are in the retail business, it could be your PCI network. If you are in the healthcare industry, it could be the servers housing patient information. If you are in the automobile industry, it could be the systems containing the blueprints for your next car. What is important is that you have a process in place that gives you visibility into your network elements, and know what it is worth to you in case the critical resource is compromised. You must determine the appropriate risk involved if data is leaked to an unauthorized entity.

Objects: Once you know what your critical resources are, the next step is to break up your network architecture into different objects. These objects are discrete elements that are used to exchange data content. Common examples of objects include your user community, the devices that get access to your network, the applications that offer or host data for your consumption, and the systems that provide connectivity to applications. Here, you are identifying all elements that either reside on the network or need access to your data. Not only that, you are identifying these objects to understand data exchange flows.

The impact of these objects on building a segmentation model is significantly enhanced when you start identifying the subelements for each object. Users belonging to the sales, engineering, services, marketing, human resources, and partner organizations could all be examples of users’ sub objects. See Table 1 for a list of subelements for each object definition.

Table 1

Identifying and creating sub objects will allow organizations to build trust relationships between these elements. The trust relationships could be established between two distinct objects or sub objects and could also be established between two sub objects of the same element. As shown in Figure 4, two applications, Active directory (AD) and Network Time Protocol (NTP), are identified in an enterprise. Based on their relationship and data interaction, the objects belonging to AD need to communicate with the objects in NTP to synchronize their clocks. The question is, do you need to provide access to the objects in NTP when they try to access objects in AD? The answer depends on your network implementation. Don't blindly permit full communication between those objects. If you feel there is a need for the NTP servers to communicate with the AD servers, then allow it.

Figure 4: App to App Segmentation

Segmentation policies allow organizations to validate requests originating from source objects against a trust model, and then provide ways to apply an appropriate enforcement action to protect the destination object, as shown in Figure 5.

Figure 5: Segmentation Policy Example

Locations: As discussed earlier, we tend to put our jewels in a safe place by building a secure perimeter around them. What we fail to realize is that thieves might try a different approach to steal your belongings. They will not always come in from the outside. They could already be inside your safe house or could already have access to your jewels through other means. The framework needs to identify all the entry points to your critical resources. With increased adoption of cloud services, some data could be accessed outside of your control points. It is also possible that the services hosted in the cloud could have access to data in your data center.

Depending on the nature of your business, you may have an ecosystem of partners that need to access certain data. Do you know where they connect from or how they access your data? Are you sure they don’t have access to unauthorized data? The flexibility within the framework allows you to logically break apart a location into specific areas based on your organizational structure and need. See Table 2 for examples of location, their definition, and a list of sublocations.

Table 2

With this breakdown of your network, you should be able to address whether a device belonging to the industrial control area needs access to your user network.

Identity: One of the most important components of the framework is determining the identity of objects whether they are users, devices, or applications. It is relatively easy to figure out the identity of users through your existing user database. Do you have a process in place to determine the identity of devices or applications? Do you know if a user is requesting access to data from a corporate-issued device or from a personally owned mobile device?

Similarly, in the case of a large industrial manufacturer, there could be many vendors regularly visiting the manufacturing plant to service and troubleshoot onsite devices. It is important to determine the identity of objects that are requesting access to all parts of the network. Would you allow your vendor to have full access to your inside network?

Monitor: Any security framework is incomplete if you do not have full visibility into the network architecture. Security monitoring is achieved by collecting, inspecting and analyzing traffic at various security zones. This includes collecting data from:

- IPS systems at the edge to inspect and analyze the traffic coming into your network from the outside

- Firewalls between the different objects to discover the identity and to enforce appropriate security controls

- Device profilers to discover the types of devices trying to request network access

- NetFlow systems to help you identify the types of traffic passing through your network and, more importantly, to help you identify the usage of your applications

Operational Security: Many people often think that information and network security is just about technology and products, focusing on their reliability and sophistication. They often neglect to assess their business goals against the security risks to their assets. The lack of credible and relevant security operational processes typically contributes to security breaches, including theft of personal and/or confidential data. For example, in case of a data breach, do you know:

- Which device was patient zero?

- How attackers got access to the data?

- How long it takes to detect something malicious happening?

- How long it takes to contain the incident?

- What processes were followed by the operations staff to detect anomalies?

- What is the life-cycle of the incident?

- Were patch-management or incident-management processes followed properly?

These are just some examples, but the list can be much longer. The goal is to define a set of sub processes for each high-level process (or operational area), then build metrics for each sub process. More importantly, assemble these metrics into a model that can be used to track operational improvement.

Behavioral Analytics: Out of all the different components discussed so far, behavioral analytics is the most important. It pulls everything together and completes this framework. Once you know which devices are connecting to your network, which applications are being hosted, who is requesting access, and where the objects are located, you can build a comprehensive context for a connection request and create a segmentation policy to authorize or reject the session. To achieve this you need to have the following modules in place:

- Identity module to discover objects (users, devices, applications, systems)

- Location module to know where a request is originating

- Monitoring module to collect data from all the appropriate sources (such as routers, firewalls, switches, NG-IPS, profilers, applications, hypervisors)

- Operational Security module for the analysts in a security operations center (SOC) to investigate anomalies and contain security incidents

Figure 6 provides an example where a user belonging to the sales team is requesting access to a database containing contact information for all customers in the region. The request is from an iPad currently located in the user’s home. How do we know about this connection’s attributes? Let's break it down. Assuming that the database and its front-end application are housed in a secure data center with no external access, the user has two options to access customer information:

- Connect from the corporate network

- Or, establish a secure connection (SSL VPN for example) into your network

If a connection request comes from the subnet assigned for VPN users, we know the user is located outside the corporate network (perhaps in their home). Based on authentication credentials, the user is placed into the sales container. Finally, a profiler helps identify the type of device and places it into the iPad segment. Now that we have all the information for this request, behavioral analytics applies the access model for an authorization action and isolates the connection.

Figure 6: Segmentation Policy Based on Context

The beauty of this framework is that it can help you compartmentalize any object. Whether you have applications hosting data in the cloud, hosts containing data in a data center, or applications with access to data residing both in the cloud and the private data center, the framework provides you the tools to build object-specific zones, create connection context, and apply an access-control model dynamically.

# Segmentation Strategy

Having a strategy for segmentation in the enterprise is fundamental to ensuring the success of the implementation. When designing for segmentation, most network architects or engineers focus on the larger network zones: DMZ, Core, Datacenter, WAN, Campus, and so on. While this is a good first step, it is not nearly enough to tackle today’s security threats. Most opportunistic attackers take advantage of the fact that there is limited segregation, allowing them to roam around the network unfettered.

A framework is only useful if there is an implementation strategy around it. The strategy should be comprehensive enough to provide all the tools that an enterprise needs to protect its jewels. This paper illustrates a segmentation strategy lifecycle that begins by identifying existing resources and onboarding any new asset or resource. Each of the steps are discussed in more detail in the following sub-sections.

Figure 7: Segmentation Strategy Steps

Identification: As mentioned earlier, segmentation should be based on the value of a critical business asset or resource, not simply on network boundaries. The first move of an attacker is reconnaissance. That is essentially what the first step of the segmentation strategy should be: identifying resources (both data and assets).

To protect (or compromise) a network, it is important to gather intelligence about the various weaknesses that may exist on the network. These weaknesses are exploited by attackers to encroach on other resources to the point where the attackers have privileged access to all critical resources. This makes any type of resource, even one that is considered to have low value, extremely valuable if it is used as the entry point into the network and leads to a more valuable target. The questions to ask are:

- What is the impact to a resource if compromised?

- What is the likelihood of a resource being compromised?

These assets, or objects, are primarily digital in nature and can include, but are not limited to:

- Hardware: servers, network devices, workstations, handheld devices, IP phones, physical security components, connected peripherals and accessories such as printers, scanners, IP phones, voice and video collaboration tools

- Software: operating systems, server and client applications, firmware

- Documentation: network diagrams, asset information, product designs, employee information

The value of an asset is not based on the value of its physical hardware but rather on the value of the data it contains. If an iPad containing private information about your employees is stolen, the total value of the loss is not merely the cost of replacing a $500 iPad.

Classification: The result of this exercise is a comprehensive view of the resources on the network along with their risk classification and rating. Organizations should understand how various resources relate to each other, and not treat them individually. A low-value target may ultimately provide access to a very high-value target, so the entire chain should be protected with ample controls. Depending on the size of the organization, this could be one of the most time-consuming steps. Various methodologies and/or frameworks can be followed to perform a thorough assessment of the resources that exist in the network [2] [3] [4] .

You should now be able to move on to the next steps of creating a segmentation policy that uses the value of each asset to determine how it should be protected. For example, if user workstations are treated as a low-value target but are used to compromise a system that is of high value, such as an employee database, the workstations should also be segmented depending on the resources they are accessing.

Policy Creation: Most cybersecurity programs do not explicitly call for a segmentation policy. It is usually mentioned indirectly in various topics within the program, which unfortunately does not place sufficient importance or value on it. For example, an access-control policy may call out how an HR employee should not be able to access Finance systems. This can be done simply through an access-control list on a firewall along with VLANs, which may protect the resource, but does not necessarily focus on segmentation itself.

A segmentation policy should be built based on data gathered about the resources in the previous steps. This policy should start at a high level, which segregates the various zones through traditional network boundaries, such as DMZ, Datacenter, and Campus, then gradually drills into each zone. This process should continue all the way to the application itself, essentially moving up the layers of the OSI model. Once all objects (and even sub-objects) have been discovered, the policy should be developed based on the type and location of those objects and on the users who are requesting access to various resources hosting or containing data. How deep one goes depends on the criticality of the asset, since in certain cases the cost associated with going through the entire process for a certain asset may not be justified.

Figure 8: Drilling into Zones

Consider two assets: the first, a server that holds credit card information and the second an SMTP server used by a development team for internal testing. Compromise of either asset would result in some loss; however, one is a lot more valuable than the other. Losing customer credit card data can result in huge damages, both monetary and legal, to the organization. This requires an organization to allocate ample resources to ensure that such an asset is well protected.

Once a segmentation policy has been created, it is time to implement these controls through various access-control models.

Access-Control Modeling: There are multiple access-control models to choose from [5] . Which model is used depends on the scenario.

Network engineers are most familiar with network-based ACLs, and while they are a good way to control access between the larger zones, it is difficult to make them granular, especially since they are mostly static and become difficult to manage over time. The model we adopt is a hybrid of multiple models, one which does not rely entirely on OSI Layer 3 and Layer 4 but also takes into consideration multiple access-control models. This includes, but is not limited to:

- Attribute Based Access Control (ABAC)

- Role Based Access Control (RBAC)

- Identity Based Access Control (IBAC)

- Rules Based Access Control (RuBAC)

An example of an access-control model is provided in Table 3.

Table 3

One solution that enables you to implement the described model is Cisco TrustSec .

Execution: Once an access-control model has been defined and the appropriate policies have been mapped in this model, the next step is to implement these controls. This involves thorough planning, which will lead to the procurement, design, and implementation of the relevant technologies. This can be broken down into the following phases:

- Plan

- Procure

- Design

- Implement/Migrate

- Monitor

Figure 9: Execution Phases

Plan and Procure: This phase of execution entails coming up with a list of requirements to satisfy the goals of the segmentation strategy. Once you have an accurate understanding of what to protect and what to protect against, the next step is to determine what tools, techniques, and procedures are required to provide this protection. What is important is to not start by implementing a segmentation strategy across the entire organization. This leads to high costs and requires a large pool of resources. Based on your data/resource classification and the access-control model, build an implementation plan by prioritizing parts of your organization that handle and store business-critical data. You will not have a fully segmented infrastructure overnight. It is a journey that could take months or in some cases years. The right strategy from day one will guarantee success in the most cost-effective way.

The entire execution needs to be carried out through proper program management. Multiple teams will need management: IT, Procurement, HR, Finance, and Legal, with a fair bit of cross dialogue to guarantee smooth progress.

Once the requirements are clear, the organization may float an RFP (directly or indirectly through a partner), and based on responses evaluate which technologies are best suited to implement the controls required for segmentation. It is highly recommended that those technologies be validated through pilots or proof of concepts to ensure that they satisfy the requirements and pass the various smoke tests. Missing out on a key feature may cause unwanted delays and in some cases a workaround or compromise that may lead to security issues at a later stage.

Design: In most cases, the organization’s lead architect or an external consultant will oversee the design created by the product vendors. The design, when it comes to segmentation, should focus on the core elements, including:

- Location: Where in the network is the resource, and how is it segmented from the rest of the network?

- Device and Application: Does the resource need access to other resources? And do other resources need access to it? For example, a multi-tier application may have a front-end (web), middleware, or back-end (database). Is each service running in its own container and what are the privileges that each service has for the others? What is the relationship between the services?

- User: User devices in normal circumstances do not need to communicate directly with each other. How is this being handled? What can the users access? How does the organization certify that a user’s endpoint has the same level of access regardless of the location?

The design is based on the vendor testing conducted in their own environment to ensure all features and functionality promised during the initial planning and procurement phase work as expected. If there are multiple vendors involved and integration is required among all vendors, testing should be required during the implementation phase conducted on the organization’s staging network.

During this phase, or earlier, it is important to identify the pilot setup, which will involve getting multiple stakeholders and staff involved. The purpose of the pilot is to test all features with the resources (people, processes, techniques, and technologies) so any challenges and issues are resolved before the rollout to the full enterprise.

Once the design is complete, it is time to start the implementation. At this point, any hardware or software should have been delivered. In the case of hardware, it should be racked, stacked, connected and powered up, with any preliminary POST tests to ensure that it is booting up correctly.

Implement and Test: The implementation phase assumes that all the hardware has been tested and is working as expected. Any components that may have failed during the POST tests should have been replaced and be ready for configuration. The implementation should follow a plan that is created based on the design. This includes the detailed configuration that the vendors have already tested and verified in their environments during the design phase.

It is essential to carry out testing to ensure that all is working according to the specifications and expectations for the solution. Testing should follow a proper methodology and should assess both functionality and features that are then recorded. Any issues encountered during testing should be addressed with the vendors and rectified before moving into the implementation phase.

As mentioned earlier, the pilot is important to this phase and should be conducted once functional and feature tests are completed. The pilot tests for performance, resiliency, user experience, and interoperability, and addresses any issues that may have been overlooked during the initial phases. The pilot phase should also span across locations, departments, technologies, and resources. This reach ensures that all stakeholders are involved in the process and will work towards a proper resolution of any challenges faced.

Monitoring: This step is one that is given very little importance in most enterprises. Monitoring is key to safeguarding the network from intruders and ensuring that systems and networks are performing as per specifications. Monitoring marks the culmination of the whole segmentation strategy and is the glue that brings people, processes, and technologies together to preserve the integrity of the protected resources. Keeping a close eye on the network not only eases detection of any anomalous activity but also helps identify any resources, new or existing, that may have been missed during the initial pass. This will determine whether another iteration through the whole segmentation lifecycle is required.

# Acknowledgments

Jazib Frahim (jfrahim@cisco.com) Principal Engineer

Aun Raza (auraza@cisco.com) Consulting Engineer

# References

Choosing the Right Segmentation Approach http://www.dmnews.com/dataanalytics/choosing-the-right-segmentation-approach/article/68918/

An Introduction to Information System Risk Management https://www.sans.org/reading-room/whitepapers/auditing/introduction-information-system-risk-management-1204

Managing Information Security Risk http://csrc.nist.gov/publications/nistpubs/800-39/SP800-39-final.pdf

TOGAF Version 9.1 http://pubs.opengroup.org/architecture/togaf9-doc/arch/

Access control - Access control models from Wikipedia https://en.wikipedia.org/wiki/Access_control#Access_control_models>

Back to Top

Cisco Security Research & Operations

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Object | Definition | Examples of Sub Object |
|---|---|---|
| Users | Objects that can provide assigned identity information | Sales, engineering, services, marketing, human resources, partner organizations |
| Devices | Objects that require access to your infrastructure for requesting and receiving data | Corporate-issued laptops, corporate-issued mobile devices, personal mobile devices, IT-owned printers and scanners |
| Systems | Objects that control data connectivity between applications and devices | Virtual hosts, hypervisors, software images, backend databases |
| Applications | Objects that provide direct or indirect access to data through some interface | Web servers, AD/DNS/NTP servers |

| Location | Definition | Examples of Sub Object |
|---|---|---|
| Inside | Part of the network where user and devices connect to access network | User, guest, lab, production subnets, VPNs, industrial control space |
| Outside | Part of the network, usually not in your control, where you may not know the users or devices that access your data | Internet, Extranet |
| Cloud | Part of the network, managed and maintained by a provider, that may have access to your DMZ network | AWS, Azure, Salesforce.com |
| Vendor | Part of the network where vendors and other partners connect | Extranet, partner subnet |

| Identity | Attributes | Role | Profile |
|---|---|---|---|
| HR User on corporate Windows workstation | User group: HR endpoint profile: Windows device auth: Successful | HR | Access to HR systems and web proxy |
| HP printer | Endpoint profile: HP printer device auth: Successful | Printer | Access from print server only |