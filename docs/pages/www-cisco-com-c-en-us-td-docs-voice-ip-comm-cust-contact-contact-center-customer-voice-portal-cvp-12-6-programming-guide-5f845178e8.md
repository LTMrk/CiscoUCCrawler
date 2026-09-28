---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-programming-guide-5f845178e8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/programming/guide/ccvp_b_1261-programming-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio/ccvp_b_1261-programming-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio_index.html
retrieved_at: 2026-08-21T17:30:37.827066+00:00
---

Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio, Release 12.6(1)

# Programming Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio, Release 12.6(1)

Updated: May 11, 2021

Chapter: Index

## Chapter: Index

## Contents

A - C - D - E - G - H - I - J - L - O - P - R - S - T - V - X

## Index

A

Action Elements

also see Standard Action Elements 1

extend ActionElementBase 1

two kinds, pre-built and standard 1

ActionConfigInterface 1

ActionElementConfig 1

API

also see Java API and XML API 1

components listed in table 1

components that extend it 1

requirements for constructing components 1

Application End Classes

only accesses Global API 1

run in four situations 1

Application Management API

built with JMX mgmt standards 1

control over the platfom 1

interfaces, diagram, and listing 1

sample beans 1

three levels 1

types of beans 1

Application Start Classes

access Global API only 1

run in four situations 1

audio_group

list of attributes 1

C

Call End Action

can send a final page 1

situations that cause it 1

tag definitions 1

using Java 1

using XML 1

Call Start Action

change setting that affect the call 1

using Java 1

using XML 1

Call Studio

deployment with Java API components 1

Integration of CVP API components 1

locations of directories 1

Call Studio Integration

requires Java 1

CallStartResponse.dtd

tag definitions 1

Code Example

substitution tag 1

VoiceElementBase methods 1

Code Examples

management beans 1

Voice Foundation Classes 1

Common Methods

listed, for configurable elements 1

Configurable Elements

action elements 1

config classes 1

custom voice elements 1

decision elements 1

extend voice, action, and decision bases 1

interaction logging 1

methods common to all configurable elements 1

only with Java 1

restrictions and considerations 1

voice elements 1

VoiceElementBase methods 1

Configuration Classes

for configurable elements 1

create and modify data with standard decision elements 1

D

Decision Action Elements

substitution, use dynamic content without dynamic config 1

Decision Elements

for configurable elements 1

DecisionConfigInterface 1

doAction

receives ActionElementData 1

doAction method

arguments explained 1

doDecision 1

DTD Diagrams

Call End Action 1

CallStartResponse.dtd 1

document sent in settings argument 1

document sent in the input argument 1

dynamic element configs 1

overview 1

sample code 1

standard action elements 1

standard decision elements 1

substitution 1

voice element config 1

Dynamic Element Configs

DTD 1

four HTTP POST arguments 1

overview 1

using Java 1

using XML 1

dynamic versus static configurations 1

E

EndApplicationInterface 1

event object hierarchy 1

G

getActionElementConfig 1

Global API

access to data beyond sessions 1

H

hotlinks using LocalHotlink 1

I

Interaction Logging

log interaction with caller and voice browser 1

J

Java API

Call End Action 1

Call Start Action 1

classes and components used 1

classes for Session API 1

compiling custom Java components 1

deployment process 1

deployment with Call Studio 1

deployment with VXML Server 1

design consideration 1

dynamic element configs 1

folder structure for Call Studio and VXML Server 1

how VXML Server interacts with Java 1

implementing Session API components 1

most efficient way to interact with CVP 1

see API Javadocs for details 1

standard decision elements 1

used for loggers 1

used to create configurable elements 1

Java Language

required for some components 1

L

Loggers

application methods () described 1

design summary 1

event object hierarchy 1

global methods () named and detailed 1

how they work 1

methods () common to application loggers 1

purposes 1

use Java API 1

utility methods () described 1

utility methods common to application and global loggers 1

O

On Error Notification

only through Java 1

P

Programming Languages Allowed

any that can create and parse HTML 1

R

Requirements for programming

read user guide for VXML server 1

S

Say It Smart Plugins

can create custom plugins 1

configuration methods () 1

configuration, four options 1

methods to run() 1

utility methods () 1

servlet.jar 1

Session API

as implemented by Java API 1

purpose, get information about call session 1

subset is Global API 1

with XML API 1

set_maintainer 1

Standard Action Elements

can act as a flag 1

can create and modify data 1

doAction method 1

exit state is "done" 1

how to build in Java 1

using XML 1

Standard Decision Elements

create and modify data 1

StartApplicationInterface 1

substitution

code example 1

dynamic content without dynamic config 1

T

Tags 1

audio_group 1

general_date_time, for start of call 1

historical_data 1

invalidate_session 1 2

set_default_path for audio 1

set_maintainer 1 2

set_maintainer, for e-mail address 1

set_voice_browser 1

status, standard action elements 1

vxml_response, for final response 1

V

Voice Element Config

DTD 1

tags defined 1

Voice Elements

diagram, how they interact with VXML Server and voice browser 1

for configurable elements 1

interaction logging 1

typical exchange with VXML Server and voice browser 1

Voice Foundation Classes

classes listed with diagram 1

concepts with VRoot diagram 1

design to support browser differences 1

purpose of 1

VoiceElementBase Methods

for configurable elements 1

VPreference 1

VXML

knowledge of language required 1

VXML Server

run code when call first received 1

X

xalan.jar 1

XML API

Call End Action 1

Call Start Action 1

components inputs and settings arguments 1

CVP API components that can use 1

deployment 1

DTD diagram of inputs argument 1

DTD diagrams overview 1

DTD of document sent in settings argument 1

dynamic element configs 1

implementing Session API 1

not used for configurable elements 1

overview 1

standard action elements 1

standard decision elements 1