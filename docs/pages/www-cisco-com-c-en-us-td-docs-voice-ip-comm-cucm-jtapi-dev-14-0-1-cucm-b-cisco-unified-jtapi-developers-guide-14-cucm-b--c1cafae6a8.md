---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-jtapi-dev-14-0-1-cucm-b-cisco-unified-jtapi-developers-guide-14-cucm-b--c1cafae6a8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/jtapi_dev/14_0_1/cucm_b_cisco-unified-jtapi-developers-guide-14/cucm_b_cisco-unified-jtapi-developers-guide-1251_chapter_0110.html
retrieved_at: 2026-08-16T18:07:01.709451+00:00
---

Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: June 11, 2025

Chapter: Cisco Unified JTAPI Alarms and Services

## Chapter: Cisco Unified JTAPI Alarms and Services

# Cisco Unified JTAPI Alarms and Services

The Cisco
                        		Unified JTAPI alarms and services consists of a set of classes and interfaces
                        		that expose the additional functionality not readily exposed in JTAPI 1.2
                        		specification but are available in Cisco Unified
                           		  Communications Manager . Developers can use the classes and interfaces
                        		to create new applications or modify existing classes and interfaces to create
                        		new methods.

This chapter
                        		describes the alarms and services that are available for implementation in a
                        		Cisco Unified Communications Manager.

For
                        		information about Cisco Unified JTAPI extensions,  see Cisco Unified JTAPI Extensions

## Alarm Class
                        	 Hierarchy

The
                              		  following class hierarchy is contained in the com.cisco.services.alarm package.

```
java.lang.Object
   com.cisco.services.alarm. AlarmManager com.cisco.services.alarm. DefaultAlarm (implements
                                                       com.cisco.services.alarm.Alarm)
com.cisco.services.alarm. DefaultAlarmWriter (implements
                            com.cisco.services.alarm. AlarmWriter )
com.cisco.services.alarm. ParameterList
```

## AlarmManager

The
                              		  AlarmManager is used to create Alarm objects. The AlarmManager is created with
                              		  a facility and AlarmService hostname and port. All alarms created by the
                              		  factory will be associated with this facility. This class also maintains a
                              		  reference to a single AlarmWriter that can be used system wide. An application
                              		  can make use of this AlarmWriter. AlarmManager exposes a default implementation
                              		  of an AlarmWriter. Applications can override this with a user defined
                              		  implementation of their own AlarmWriter.

### Usage

AlarmManager AlarmManager  =  new AlarmManager(facilityName, 
                              		  alarmServiceHost,  alarmServicePort,  debugTrace,  errorTrace);

Alarms
                              		  are created by the factory by supplying the alarmName (mnemonic),  subfacility
                              		  and severity Alarms can be cached for use in different parts of the
                              		  application. During a send alarm applications can specify the variable
                              		  parameters that offer specific information to the AlarmService.

### Usage

Typically
                              		  applications will maintain their own AlarmManager instance. Applications will
                              		  also have to set a debug and error trace to enable the alarm tracing to also be
                              		  sent to the existing trace destinations.

Setup
                              		  the manager and writer classes:

AlarmWriter alarmWriter  =  new DefaultAlarmWriter(port,  alarmServiceHost);

AlarmManager alarmManager  =  new AlarmManager( "AA_IVR" ,  alarmWriter, 
                              		  debugTrace,  errorTrace);

Generating the Alarms:

create
                              		  an alarm for the subfacility and a default severity.

Alarm
                              		  alarm  =  alarmManager.createAlarm( "HTTPSS" ,  Alarm.INFORMATIONAL);

alarm.send( "090T" )
                              		  sends the alarm with the mnemonic

alarm.send( "090T" , "Port is
                                 			 stuck" , "CTIPort01" )
                              		  or with a mnemonic and parameter

### Declaration

```
public class AlarmManager java.lang.Object
 |
 +-- com.cisco.services.alarm.AlarmManager
```

More than one
                                             			 parameter can be sent by specifying a ParameterList

Member summary

Constructors

Create
                                             						an instance of the AlarmManager for the facility.

Methods

Creates
                                             						an Alarm of required severity for the subFacility

Allows
                                             						applications to override the AlarmWriter to be used by this AlarmManager,  with
                                             						a user defined AlarmWriter

Inherited member summary

Methods inherited from class Object

### Constructors

#### AlarmManager(String,  AlarmWriter,  Trace, 
                                 		  UnconditionalTrace)

```
public AlarmManager (java.lang.String facility, 
  com.cisco.services.alarm.AlarmWriterwriter,  
  com.cisco.services.tracing.TracedebugTrace_,  
  com.cisco.services.tracing.UnconditionalTraceerrorTrace_)
```

Create an instance
                                 		  of the AlarmManager for the facility. Applications specify an AlarmWriter to be
                                 		  used by this AlarmManager to send the Alarms to the AlarmService.

### Methods

#### createAlarm(String,  int)

```
public com.cisco.services.alarm.Alarm createAlarm (java.lang.String subfacility,  intseverity)
```

Creates an Alarm
                                 		  of required severity for the subFacility

Returns:

an object
                                 		  implementing the alarm interface

#### getAlarmWriter()

```
public com.cisco.services.alarm.AlarmWriter getAlarmWriter ()
```

Returns:

an AlarmWriter
                                 		  object

#### setAlarmWriter(AlarmWriter)

```
public void setAlarmWriter (com.cisco.services.alarm.AlarmWriter writer)
```

Allows
                                 		  applications to override the AlarmWriter to be used by this AlarmManager,  with
                                 		  a user defined AlarmWriter

## AlarmWriter

An
                              		  AlarmWriter receives alarm messages and transmits it to the receiving
                              		  AlarmService on a TCP link. This interface can be used to implement other
                              		  AlarmWriters to be used with this implementation of com.cisco.service.alarm A
                              		  DefaultAlarmWriter is provided with this implementation and can be obtained
                              		  from the AlarmManager.

### Declaration

```
public interface AlarmWriter
```

### All Known Implementing Classes

DefaultAlarmWriter

### Member
                           	 Summary

Member summary

Methods

close
                                             						the AlarmWriter

Send
                                             						out the alarm message to the AlarmService.

Enable
                                             						or disable the AlarmWriter

### Methods

#### close()

```
public void close ()
```

close the
                                 		  AlarmWriter

#### getDescription()

```
public java.lang.String getDescription ()
```

Returns:

the AlarmWriter
                                 		  description

#### getEnabled()

```
public boolean getEnabled ()
```

Returns:

the current
                                 		  enabled or disabled state of the AlarmWriter

#### getName()

```
public java.lang.String getName ()
```

Returns:

the AlarmWriter
                                 		  name

#### send(String)

```
public void send (java.lang.String alarmMessage)
```

Send out the alarm
                                 		  message to the AlarmService.

Parameters:

the - Alarm to be
                                 		  sent

#### setEnabled(boolean)

```
public void setEnabled (boolean enable)
```

Enable or disable
                                 		  the AlarmWriter

Parameters:

enable or disable
                                 		  the AlarmWriter

## DefaultAlarm

An Implementation of the Alarm interface. The AlarmManager creates these Alarms when the createAlarm() method is called.

### Declaration

```
public class DefaultAlarm implements Alarm java.lang.Object
|
+-- com.cisco.services.alarm.DefaultAlarm
```

### All Implemented Interfaces

Alarm

### Member
                           	 Summary

Member summary

Constructors

Methods

Send the
                                             						alarm with the specified mnemonic

Send the
                                             						alarm with the specified name and list of parameters.

Send
                                             						the alarm with the specified name and parameter

Inherited member summary

Fields inherited from interface Alarm

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  toString(),  wait(),  wait(),  wait()

### Constructors

#### DefaultAlarm(String,  String,  int,  AlarmWriter)

```
public DefaultAlarm (java.lang.String facility,  
   java.lang.StringsubFacility, 
   intseverity,  
   com.cisco.services.alarm.AlarmWriteralarmWriter)
```

### Methods

#### getFacility()

```
public java.lang.String getFacility ()
```

Specified By:

getFacility() in interface Alarm

#### getSeverity()

```
public int getSeverity ()
```

Specified By:

getSeverity() in interface Alarm

#### getSubFacility()

```
public java.lang.String getSubFacility ()
```

Specified By:

getSubFacility() in interface Alarm

#### send(String)

```
public void send (java.lang.String mnemonic)
```

Send the alarm
                                 		  with the specified mnemonic

Specified By:

send(String) in interface Alarm

#### send(String, 
                                 		  ParameterList)

```
public void send (java.lang.String mnemonic, 
   com.cisco.services.alarm.ParameterListparamList)
```

Send the alarm
                                 		  with the specified name and list of parameters.

Specified By:

send(String, ParameterList) in interface Alarm

#### send(String, 
                                 		  String,  String)

```
public void send (java.lang.String mnemonic, 
   java.lang.StringparamName, 
   java.lang.StringparamValue)
```

Send the alarm
                                 		  with the specified name and parameter

Specified By:

send(String, String, String) in interface Alarm

## DefaultAlarmWriter

DefaultAlarmWriter implementation of the AlarmWriter interface.

DefaultAlarmWriter maintains a
                              queue of a fixed size to which the alarms are written. The sending of the
                              alarms to the alarm service takes place on a separate thread. The queue is
                              fixed size.

### Declaration

```
public class DefaultAlarmWriter implements AlarmWriter java.lang.Object
|
+-- com.cisco.services.alarm.DefaultAlarmWriter
```

### All Implemented Interfaces

AlarmWriter

### Member
                           	 Summary

Member summary

Constructors

Constructor for the DefaultAlarmWriter which takes the
                                             						AlarmService hostname,  port and a queue size of fifty (50).

Constructor for the DefaultAlarmWriter which takes the AlarmService hostname, 
                                             						port and queue size.

Constructor for the DefaultAlarmWriter which takes the AlarmService hostname, 
                                             						port and queue size.

Methods

Shutdown the send thread and close the socket

send
                                             						the Alarm to the alarm service

Applications can dynamically enable or disable the AlarmWriter

Inherited member summary

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  toString(),  wait(),  wait(),  wait()

### Constructors

#### DefaultAlarmWriter(int,  String)

```
public DefaultAlarmWriter (int port, 
   java.lang.StringalarmServiceName) throwsUnknownHostException
```

Constructor for
                                 		  the DefaultAlarmWriter which takes the AlarmService hostname,  port and a queue
                                 		  size of fifty (50). The AlarmService is listening on this port for Alarm
                                 		  messages.

Parameters:

port: port on
                                 		  which the alarm service is listening

alarmServiceName:
                                 		  The host name of the machine with the Alarm service

Throws:

java.net.UnknownHostException

#### DefaultAlarmWriter(int,  String,  int)

```
public DefaultAlarmWriter (int port, 
   java.lang.StringalarmServiceName, 
   intqueueSize) throwsUnknownHostException
```

Constructor for
                                 		  the DefaultAlarmWriter which takes the AlarmService hostname,  port and queue
                                 		  size. The AlarmService is listening on this port for Alarm messages.

Parameters:

port—port on which
                                 		  the alarm service is listening

alarmServiceName—The host name of the machine with the Alarm
                                 		  service

queueSize - the
                                 		  size of the queue to be maintained in the alarm writer

Throws:

java.net.UnknownHostException

#### DefaultAlarmWriter(int,  String,  int,  ConditionalTrace, 
                                 		  UnconditionalTrace)

```
public DefaultAlarmWriter (int port, 
   java.lang.StringalarmServiceName, 
   intqueueSize, 
   com.cisco.services.tracing.ConditionalTracedebugTrace_, 
   com.cisco.services.tracing.UnconditionalTraceerrorTrace_) throwsUnknownHostException
```

Constructor for
                                 		  the DefaultAlarmWriter which takes the AlarmService hostname,  port and queue
                                 		  size. The AlarmService is listening on this port for Alarm messages.

Parameters:

port—port on which
                                 		  the alarm service is listening

alarmServiceName—The host name of the machine with the Alarm
                                 		  service

queueSize - the
                                 		  size of the queue to be maintained in the alarm writer

Throws:

java.net.UnknownHostException

### Methods

#### close()

```
public void close ()
```

Shutdown the send
                                 		  thread and close the socket

Specified By:

close in interface AlarmWriter

#### getDescription()

```
public java.lang.String getDescription ()
```

Specified By:

getDescription in
                                 		  interface AlarmWriter

Returns:

a short
                                 		  description of the AlarmWriter

#### getEnabled()

```
public boolean getEnabled ()
```

Specified By:

getEnabled in
                                 		  interface AlarmWriter

Returns:

the enabled state
                                 		  of the AlarmWriter

#### getName()

```
public java.lang.String getName ()
```

Specified By:

getName in
                                 		  interface AlarmWriter

Returns:

the name of the
                                 		  AlarmWriter

#### main(String[])

```
public static void main ( java.lang.String[] args)
```

#### send(String)

```
public void send (java.lang.String alarmMessage)
```

send the Alarm to
                                 		  the alarm service

Specified By:

send in interface AlarmWriter

#### setEnabled(boolean)

```
public void setEnabled (boolean enable)
```

Applications can
                                 		  dynamically enable or disable the AlarmWriter

Specified By:

setEnabled in
                                 		  interface AlarmWriter

## ParameterList

ParameterList is a list of name value pairs that is used to send
                              		  additional (and optional) user defined parameters to the AlarmService. These
                              		  parameters can contain the specifics of an Alarm.

As an
                              		  example,  a LowResourceAlarm can have a parameter that informs the service which
                              		  particular resource is low:

name = "CPUUsage"

value = "0.9"

These
                              		  parameters are user definable but must,  however,  also be pre-defined in the
                              		  AlarmService catalog.

### Declaration

```
public class ParameterList java.lang.Object
|
+-- com.cisco.services.alarm.ParameterList
```

### Member
                           	 Summary

Member summary

Constructors

Default
                                             						constructor for the ParameterList

Constructor that takes a name value pair.

Methods

method
                                             						used to add additional name value pairs (parameters) to the list

Get the
                                             						parameter names in the list

get the
                                             						value for a parameter

remove
                                             						all the parameters in the list

remove
                                             						a particular parameter if it is in the list

Inherited member summary

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait()

### Constructors

#### ParameterList()

```
public ParameterList ()
```

Default
                                 		  constructor for the ParameterList

#### ParameterList(String,  String)

```
public ParameterList (java.lang.String name, 
   java.lang.Stringvalue)
```

Constructor that
                                 		  takes a name value pair.

### Methods

#### addParameter(String,  String)

```
public void addParameter (java.lang.String name, 
   java.lang.Stringvalue)
```

method used to add
                                 		  additional name value pairs (parameters) to the list

#### getParameterNames()

```
public java.lang.String[] getParameterNames ()
```

Get the parameter
                                 		  names in the list

Returns:

array of
                                 		  parameters

#### getParameterValue(String)

```
public java.lang.String getParameterValue (java.lang.String parameterName)
```

get the value for
                                 		  a parameter

Returns:

value of a
                                 		  parameter

#### removeAllParameters()

```
public void removeAllParameters ()
```

remove all the
                                 		  parameters in the list

#### removeParameter(String)

```
public void removeParameter (java.lang.String parameterName)
```

remove a
                                 		  particular parameter if it is in the list

#### toString()

```
public java.lang.String toString ()
```

Overrides:

## Alarm Interface Hierarchy

The following interface hierarchy is contained in the
                              com.cisco.services.alarm package.

```
com.cisco.services.alarm. Alarm
```

```
com.cisco.services.alarm. AlarmWriter
```

## Alarm

The
                              		  Alarm interface is used to define Alarms in. An Alarm has an XML representation
                              		  that it must adhere to in order to be recognized by the Alarm Service,  with a
                              		  DTD as shown below. An application can implement this interface or use the
                              		  AlarmFactory to generate Alarms of the correct format. The Alarm is the a
                              		  specification that needs to be sent to an AlarmService that will take some
                              		  action based on the Alarm. Using this specification the AlarmService will
                              		  access definitions available in a catalog. This catalog is maintained by the
                              		  user requiring the Alarm function to effect the appropriate action for the
                              		  Alarm. The severity specified the Alarm can over-ride the severity associated
                              		  with this Alarm in the catalog. If no severity is specified in the Alarm the
                              		  catalog severity is used.

Alarm
                              		  severities are derived from Syslog and are defined as follows:

0  = 
                              		  EMERGENCIES System unusable

1  = 
                              		  ALERTS Immediate action needed

2  = 
                              		  CRITICAL Critical conditions

3  = 
                              		  ERROR Error conditions

4  = 
                              		  WARNING Warning conditions

5  = 
                              		  NOTIFICATION Normal but significant condition

6  = 
                              		  INFORMATIONAL Informational messages only

7  = 
                              		  DEBUGGING Debugging messages

### Declaration

```
public interface Alarm
```

### All Known Implementing Classes

DefaultAlarm

### Member Summary

Member summary

Fields

The
                                             						application will continue working on the tasks but all functions may not be
                                             						operational (one or more devices in the list are not accessible but others in
                                             						the list can be accessed)

Syslog
                                             						severity level  =  1

A
                                             						critical failure,  the application cannot accomplish the tasks required due to
                                             						this failure,  for example,  the application cannot open the database to read the
                                             						device list

Syslog
                                             						severity level  =  2

Very
                                             						detailed information regarding errors or processing status that is only
                                             						generated when DEBUG mode has been enabled

Syslog
                                             						severity level  =  7

Emergency situation,  a system shutdown is necessary

Syslog
                                             						severity level  =  0

An
                                             						error condition of some kind has occurred and the user needs to understand the
                                             						nature of that failure

Syslog
                                             						severity level  =  3

The
                                             						highest trace level,  currently this is DEBUGGING with a trace level of 7

Information of some form not relating to errors,  warnings,  audit,  or debug

Syslog
                                             						severity level  =  6

The
                                             						lowest trace level,  currently this is EMERGENCIES with a trace level of 0

Applications can set this level to generate Alarms without a severity.

Notification denotes a normal but significant condition

Syslog
                                             						severity level  =  5

String
                                             						used when a mnemonic is not specified during an Alarm send

Warning
                                             						that a problem of some form exists but is not keeping the application from
                                             						completing its tasks

Syslog
                                             						severity level  =  4

Methods

send
                                             						the Alarm with the specified mnemonic.

send
                                             						an Alarm with the specified mnemonic and supplied parameter list

send
                                             						an Alarm with the specified mnemonic and with one parameter

### Fields

#### ALERTS

```
public static final int ALERTS
```

The application
                                 		  will continue working on the tasks but all functions may not be operational
                                 		  (one or more devices in the list are not accessible but others in the list can
                                 		  be accessed)

Syslog severity
                                 		  level  =  1

#### CRITICAL

```
public static final int CRITICAL
```

A critical
                                 		  failure,  the application cannot accomplish the tasks required due to this
                                 		  failure,  for example,  the application cannot open the database to read the
                                 		  device list

Syslog severity
                                 		  level  =  2

#### DEBUGGING

```
public static final int DEBUGGING
```

Very detailed
                                 		  information regarding errors or processing status that is only generated when
                                 		  DEBUG mode has been enabled (Syslog severity level  =  7).

#### EMERGENCIES

```
public static final int EMERGENCIES
```

Emergency
                                 		  situation,  a system shutdown is necessary

Syslog severity
                                 		  level  =  0

#### ERROR

```
public static final int ERROR
```

An error condition
                                 		  of some kind has occurred and the user needs to understand the nature of that
                                 		  failure

Syslog severity
                                 		  level  =  3

#### HIGHEST_LEVEL

```
public static final int HIGHEST_LEVEL
```

The highest trace
                                 		  level,  currently this is DEBUGGING with a trace level of 7

#### INFORMATIONAL

```
public static final int INFORMATIONAL
```

Information of
                                 		  some form not relating to errors,  warnings,  audit,  or debug

Syslog severity
                                 		  level  = 6

#### LOWEST_LEVEL

```
public static final int LOWEST_LEVEL
```

The lowest trace
                                 		  level,  currently this is EMERGENCIES with a trace level of 0

#### NO_SEVERITY

```
public static final int NO_SEVERITY
```

Applications can
                                 		  set this level to generate Alarms without a severity. NOTE: This is only
                                 		  intended for cases where an application wants the AlarmService to use the
                                 		  severity associated with the Alarm in the catalog

#### NOTIFICATION

```
public static final int NOTIFICATION
```

Notification
                                 		  denotes a normal but significant condition (Syslog severity level  =  5).

#### UNKNOWN_MNEMONIC

```
public static final java.lang.String UNKNOWN_MNEMONIC
```

String used when a
                                 		  mnemonic is not specified during an Alarm send

#### WARNING

```
public static final int WARNING
```

Warning that a
                                 		  problem of some form exists but is not keeping the application from completing
                                 		  its tasks (Syslog severity level  =  4).

### Methods

#### getFacility()

```
public java.lang.String getFacility ()
```

Returns:

the facility name
                                 		  of this Alarm

#### getSeverity()

```
public int getSeverity ()
```

Returns:

severity of the
                                 		  alarm,  an integer in the range [0-7]

#### getSubFacility()

```
public java.lang.String getSubFacility ()
```

Returns:

the subfacility of
                                 		  this Alarm

#### send(String)

```
public void send (java.lang.String mnemonic)
```

send the Alarm
                                 		  with the specified mnemonic. If a null or empty String is passed a mnemonic UNK
                                 		  is sent

#### send(String, 
                                 		  ParameterList)

```
public void send (java.lang.String mnemonic, com.cisco.services.alarm.ParameterList parameterList)
```

send an Alarm with
                                 		  the specified mnemonic and supplied parameter list

#### send(String, 
                                 		  String,  String)

```
public void send (java.lang.String mnemonic, 
   java.lang.StringparameterName, 
   java.lang.StringparameterValue)
```

send an
                                 		  Alarm with the specified mnemonic and with one parameter.

## AlarmWriter

An
                              		  AlarmWriter receives alarm messages and transmits it to the receiving
                              		  AlarmService on a TCP link. This interface can be used to implement other
                              		  AlarmWriters to be used with this implementation of com.cisco.service.alarm A
                              		  DefaultAlarmWriter is provided with this implementation and can be obtained
                              		  from the AlarmManager.

### Declaration

```
public interface AlarmWriter
```

### All Known Implementing Classes

DefaultAlarmWriter

### Member
                           	 Summary

Member summary

Methods

close
                                             						the AlarmWriter

Send
                                             						out the alarm message to the AlarmService.

Enable
                                             						or disable the AlarmWriter

#### Methods

##### close()

```
public void close ()
```

close the
                                    		  AlarmWriter

##### getDescription()

```
public java.lang.String getDescription ()
```

Returns:

the AlarmWriter
                                    		  description

##### getEnabled()

```
public boolean getEnabled ()
```

Returns:

the current
                                    		  enabled or disabled state of the AlarmWriter

##### getName()

```
public java.lang.String getName ()
```

Returns:

the AlarmWriter
                                    		  name

##### send(String)

```
public void send (java.lang.String alarmMessage)
```

Send out the alarm
                                    		  message to the AlarmService.

Parameters:

the Alarm to be
                                    		  sent

##### setEnabled(boolean)

```
public void setEnabled (boolean enable)
```

Enable or disable
                                    		  the AlarmWriter

Parameters:

enable
                                    		  or disable the AlarmWriter

## Services Tracing Class Hierarchy

The following class hierarchy is contained in the
                              com.cisco.services.tracing package.

```
java.lang.Object
   com.cisco.services.tracing. BaseTraceWriter (implements
                                               com.cisco.services.tracing.TraceWriter)
   com.cisco.services.tracing. ConsoleTraceWriter com.cisco.services.tracing. LogFileTraceWriter com.cisco.services.tracing. OutputStreamTraceWriter com.cisco.services.tracing. SyslogTraceWriter com.cisco.services.tracing. TraceManagerFactory
```

## BaseTraceWriter

This abstract class is useful for supplying a default,  non-printing TraceWriter to a TraceWriterManager This class must be extended to provide the functionality to trace to different streams. The doPrintln() method must be implemented by the extending class.

### Declaration

```
public abstract class BaseTraceWriter implements TraceWriter java.lang.Object
|
+-- com.cisco.services.tracing.BaseTraceWriter
```

### All Implemented Interfaces

TraceWriter

### Direct Known
                           	 Subclasses

### Member
                           	 Summary

Member summary

Constructors

BaseTraceWriter with trace levels as passed in traceLevels in the array falling
                                             						outside the range Trace.LOWEST_LEVEL and Trace.HIGHEST_LEVEl are ignored

BaseTraceWriter that traces all levels up to the maxTraceLevel The trace level
                                             						is maintained in the range [Trace.HIGHEST_LEVEL,  Trace.LOWEST_LEVEL ]

BaseTraceWriter which only traces the lowest level i.e. severity level, 
                                             						Trace.LOWEST_LEVEL messages

Methods

Must be
                                             						implemented by the various TraceWriters extending BaseTraceWriter to provide
                                             						the specific tracing functionality

Inherited member summary

Methods inherited from class Object

clone()
                                             						,  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(),  notifyAll(), 
                                             						wait(),  wait(),  wait()

### Constructors

#### BaseTraceWriter(int[],  String,  String)

```
protected BaseTraceWriter (int[] traceLevels, 
   java.lang.Stringname, 
   java.lang.Stringdescription)
```

BaseTraceWriter
                                 		  with trace levels as passed in traceLevels in the array falling outside the
                                 		  range Trace.LOWEST_LEVEL and Trace.HIGHEST_LEVEl are ignored

Parameters:

traceLevels -
                                 		  array of trace levels

#### See
                                 		  Also:

Trace

#### BaseTraceWriter(int,  String,  String)

```
protected BaseTraceWriter (int maxTraceLevel, 
   java.lang.Stringname, 
   java.lang.Stringdescription)
```

BaseTraceWriter
                                 		  that traces all levels up to the maxTraceLevel The trace level is maintained in
                                 		  the range [Trace.HIGHEST_LEVEL,  Trace.LOWEST_LEVEL]

#### See
                                 		  Also:

Trace

#### BaseTraceWriter(String,  String)

```
protected BaseTraceWriter (java.lang.String name, 
   java.lang.Stringdescription)
```

BaseTraceWriter
                                 		  which only traces the lowest level i.e. severity level,  Trace.LOWEST_LEVEL
                                 		  messages

#### See
                                 		  Also:

Trace

### Methods

#### close()

```
public final void close ()
```

Description copied
                                 		  from interface:

com.cisco.services.tracing.TraceWriter

Releases any
                                 		  resources associated by this TraceWriter .

Specified By:

close in interface TraceWriter

#### doClose()

```
protected void doClose ()
```

#### doFlush()

```
protected void doFlush ()
```

#### doPrintln(String,  int)

```
protected abstract void doPrintln (java.lang.String message, 
   intmessageNumber)
```

Must be
                                 		  implemented by the various TraceWriters extending BaseTraceWriter to provide
                                 		  the specific tracing functionality

#### flush()

```
public final void flush ()
```

Forces output of
                                 		  any messages that have been printed using the println method

Specified By:

flush in interface TraceWriter

#### getDescription()

```
public final java.lang.String getDescription ()
```

Specified By:

getDescription in
                                 		  interface TraceWriter

#### getEnabled()

```
public boolean getEnabled ()
```

Description copied from
                                    			 interface: com.cisco.services.tracing.TraceWriter

Returns whether
                                 		  the println method will print anything or not. A closed TraceWriter will always
                                 		  return false from this method.

Specified By:

getEnabled in
                                 		  interface TraceWriter

#### getName()

```
public final java.lang.String getName ()
```

Specified By:

getName in
                                 		  interface TraceWriter

#### getTraceLevels()

```
public final int[] getTraceLevels ()
```

Specified By:

getTraceLevels in
                                 		  interface TraceWriter

#### println(String,  int)

```
public final void println (java.lang.String message, 
   intseverity)
```

Description copied from
                                    			 interface: com.cisco.services.tracing.TraceWriter

Prints the
                                 		  specified string followed by a carriage return The concrete TraceWriter class
                                 		  will use the severity to block out messages from a particular stream. Each
                                 		  trace writer has a notion of the highest level trace it traces.

Specified By:

println in interface TraceWriter

#### setTraceLevels(int[])

```
public final void setTraceLevels (int[] levels)
```

Description copied from
                                    			 interface: com.cisco.services.tracing.TraceWriter

set the trace
                                 		  levels that will be traced by this TraceWriter

Specified By:

setTraceLevels in interface TraceWriter

#### toString()

```
public final java.lang.String toString ()
```

Overrides:

toString in
                                 		  class Object

## ConsoleTraceWriter

Supplies a console TraceWriter to trace to System.out.

### See Also:

Trace

### Declaration

```
public final class ConsoleTraceWriter extends BaseTraceWriter java.lang.Object
|
+-- com.cisco.services.tracing.BaseTraceWriter |
+-- com.cisco.services.tracing.ConsoleTraceWriter
```

### All Implemented Interfaces

TraceWriter

### Member
                           	 Summary

Member summary

Constructors

Default
                                             						constructor,  traces all severity levels

Constructor that sets the maximum level to be traced.

Construct a ConsoleTraceWriter with an array of trace levels Only traces with
                                             						the severity in the tracelevel array are traced

Methods

Inherited member summary

Methods inherited from class BaseTraceWriter

close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString()

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait()

### Constructors

#### ConsoleTraceWriter()

```
public ConsoleTraceWriter ()
```

Default
                                 		  constructor,  traces all severity levels

#### ConsoleTraceWriter(int)

```
public ConsoleTraceWriter (int maxTraceLevel)
```

Constructor that
                                 		  sets the maximum level to be traced.

#### See
                                 		  Also:

Trace

#### ConsoleTraceWriter(int[])

```
public ConsoleTraceWriter (int[] traceLevels)
```

Construct a
                                 		  ConsoleTraceWriter with an array of trace levels Only traces with the severity
                                 		  in the tracelevel array are traced

Parameters:

int - [] traceLevels

#### See
                                 		  Also:

Trace

### Methods

#### doFlush()

```
protected final void doFlush ()
```

Overrides:

doFlush in class BaseTraceWriter

#### doPrintln(String,  int)

```
protected final void doPrintln (java.lang.String message, 
   intmessageNumber)
```

Description copied from
                                    			 class: com.cisco.services.tracing.BaseTraceWriter

Must be
                                 		  implemented by the various TraceWriters extending BaseTraceWriter to provide
                                 		  the specific tracing functionality

Overrides:

doPrintln in class BaseTraceWriter

#### main(String[])

```
public static void main (java.lang.String[] args)
```

## LogFileTraceWriter

This
                              		  class extends the BaseTraceWriter class to implement a TraceWriter that writes to a set of log files,  rotating
                              		  among them as each becomes filled to a specified capacity and stores them in a
                              		  specified directory.

Each of
                              		  the log files is named according to a pattern controlled by three properties, CurrentFile , FileNameBase ,  and FileExtension . The CurrentFile property determines which log file,  by ordinal
                              		  number,  is being written at present,  the FileNameBase property determines the prefix of each log
                              		  file name,  and the FileExtension property determines the suffix,  e.g. "txt" . From
                              		  these properties,  log files are named FileNameBase
                                 			 LeadingZeroPadding CurrentFile.FileExtension . The CurrentFile property takes on a value from 1 to the value
                              		  of the MaxFiles property. Note that the CurrentFile property,  when converted to a String,  is padded
                              		  with leading zeroes depending on the values of the MaxFiles and CurrentFile properties. An index file tracks the index of
                              		  the last file written. If the logFileWriter is recreated (for example if an
                              		  application is restarted) new files will continue from the last written index.

Where
                              		  the log files are stored is determined by the path , dirNameBase , useSameDir . If a path is not specified,  the current path is used as default.
                              		  If a dirNameBase is not specified,  it write log files in the
                              		  path. Depending upon whether useSameDir is true or false,  files are written to the same
                              		  directory or a new directory,  each time an instance of LogFileTraceWriter is
                              		  created. In case new directories are being made each time,  the directory name
                              		  will consist of the dirNameBase and a number,  separated by an ’_’. The number
                              		  is one more than the greatest number associated with directories with the same dirNameBame in the path. While specifying the path,  you may
                              		  use either a "/" or "\\" ,  but not "\"

The LogFileTraceWriter keeps track of how many bytes have been
                              		  written to the current log file. When that number grows within approximately LogFileTraceWriter.ROLLOVER_THRESHOLD bytes,  tracing
                              		  continues to the next file,  which is either CurrentFile + 1 if CurrentFile is not equal to MaxFiles ,  or 1 if CurrentFile is equal to MaxFiles .

All properties
                                          			 of this class are specified in the constructor; there is no way to change them
                                          			 dynamically. Caveat: If
                                          			 two instances of LogFileTraceWriter are created with the same path and dirNameBase ,  and useSameDir is true,  they may write to the same file.

### Example

The
                              		  following code instantiates a LogFileTraceWriter that will create log files called "MyLog01.log" through "MyLog12.log" .
                              		  Each file will grow to approximately 100K bytes in size before the next file is
                              		  created:

LogFileTraceWriter out  =  new LogFileTraceWriter ( "MyLog" , "log" ,  12,  100
                              		  * 1024 ); will create a log file TraceWriter which will rotate traces to 12
                              		  files from Mylog01.log and Mylog12.log with a file size of 100 KBytes. By
                              		  default the tracing is set to the HIGHEST_LEVEL.

The
                              		  following code constructs a LogFileTraceWriter which stores the log files in the path "c:/LogFiles" in a sub directory, "Run" . The
                              		  files will be named MyLogXX.log. The number of rotating files will be 12 with a
                              		  size of 100 KB. The same directory gets used for each instance of the
                              		  application.

LogFileTraceWriter out  =  new LogFileTraceWriter ( "c:/logFiles" , "Run" , "MyLog" , "log" ,  12, 
                              		  100*1024,  true);

### See
                              		  Also

Trace

### Declaration

```
public final class LogFileTraceWriter extends BaseTraceWriter java.lang.Object
|
+-- com.cisco.services.tracing.BaseTraceWriter |
+-- com.cisco.services.tracing.LogFileTraceWriter
```

### All Implemented Interfaces

TraceWriter

### Member
                           	 Summary

Member summary

Fields

Constructors

Default
                                             						constructor for LogFileTraceWriter that rotates among an arbitrary number of
                                             						files with tracing for all levels.

Default
                                             						constructor for LogFileTraceWriter that rotates among an arbitrary number of
                                             						files with tracing for all levels.

Constructs a LogFileTraceWriter that rotates among an arbitrary number of files
                                             						storing them in a specified directory.

Methods

Closes
                                             						this OutputStream.

Returns
                                             						the CurrentFile property

Returns
                                             						the FileExtension property

Returns
                                             						the FileNameBase property

Get the
                                             						header string that will be written at the beginning of each log file.

Returns the MaxFiles property

Returns the MaxFileSize property

Set
                                             						the constant header string that will be written at the beginning of every file, 
                                             						trace writing continues from the next line after the header is written.

Inherited member summary

Methods inherited from class BaseTraceWriter

close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString()

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait()

### Fields

#### DEFAULT_FILE_NAME_BASE

```
public static final java.lang.String DEFAULT_FILE_NAME_BASE
```

#### DEFAULT_FILE_NAME_EXTENSION

```
public static final java.lang.String DEFAULT_FILE_NAME_EXTENSION
```

#### DIR_BASE_NAME_NUM_SEPERATOR

```
public static final char DIR_BASE_NAME_NUM_SEPERATOR
```

#### MIN_FILE_SIZE

```
public static final int MIN_FILE_SIZE
```

#### MIN_FILES

```
public static final int MIN_FILES
```

#### ROLLOVER_THRESHOLD

```
public static final int ROLLOVER_THRESHOLD
```

### Constructors

#### LogFileTraceWriter(String,  String,  int,  int)

```
public LogFileTraceWriter (java.lang.String fileNameBase, 
   java.lang.StringfileNameExtension, 
   intmaxFiles, 
   intmaxFileSize) throwsIOException
```

Default
                                 		  constructor for LogFileTraceWriter that rotates among an arbitrary number of
                                 		  files with tracing for all levels. Since a path and Directory Base name is not
                                 		  specified,  it writes the files to the current directory without any sub
                                 		  directories.

Throws:

java.io.IOException

#### LogFileTraceWriter(String,  String,  String,  String,  int,  int, 
                                 		  boolean)

```
public LogFileTraceWriter (java.lang.String path, 
   java.lang.StringdirNameBase, 
   java.lang.StringfileNameBase, 
   java.lang.StringfileNameExtension, 
   intmaxFiles, 
   intmaxFileSize, 
   booleanuseSameDir) throwsIOException
```

Default
                                 		  constructor for LogFileTraceWriter that rotates among an arbitrary number of
                                 		  files with tracing for all levels.

Throws:

java.io.IOException

#### LogFileTraceWriter(String,  String,  String,  String,  int,  int, 
                                 		  int,  boolean)

```
public LogFileTraceWriter (java.lang.String path, 
   java.lang.StringdirNameBase, 
   java.lang.StringfileNameBase, 
   java.lang.StringfileNameExtension, 
   intmaxFiles, 
   intmaxFileSize, 
   intmaxTraceLevel, 
   booleanuseSameDir) throwsIOException
```

Constructs a
                                 		  LogFileTraceWriter that rotates among an arbitrary number of files storing them
                                 		  in a specified directory.

Throws:

java.io.IOException

### Methods

#### doClose()

```
protected void doClose ()
```

Closes this
                                 		  OutputStream. Any log file that is currently open will be closed as well.

Overrides:

doClose in class BaseTraceWriter

#### doFlush()

```
protected void doFlush ()
```

Overrides:

doFlush in class BaseTraceWriter

#### doPrintln(String,  int)

```
protected void doPrintln (java.lang.String message, 
   intmessageNumber)
```

Description copied from
                                    			 class: com.cisco.services.tracing.BaseTraceWriter

Must be
                                 		  implemented by the various TraceWriters extending BaseTraceWriter to provide
                                 		  the specific tracing functionality

Overrides:

doPrintln in class BaseTraceWriter

#### getCurrentFile()

```
public int getCurrentFile ()
```

Returns:

the CurrentFile
                                 		  property

#### getFileExtension()

```
public java.lang.String getFileExtension ()
```

Returns:

the FileExtension
                                 		  property

#### getFileNameBase()

```
public java.lang.String getFileNameBase ()
```

Returns:

the FileNameBase
                                 		  property

#### getHeader()

```
public java.lang.String getHeader ()
```

Get the header
                                 		  string that will be written at the beginning of each log file.

Returns:

the Header
                                 		  Property

#### getMaxFiles()

```
public int getMaxFiles ()
```

Returns:

the MaxFiles
                                 		  property

#### getMaxFileSize()

```
public int getMaxFileSize ()
```

Returns:

the MaxFileSize
                                 		  property

#### setHeader(String)

```
public void setHeader (java.lang.String header)
```

Set the constant
                                 		  header string that will be written at the beginning of every file,  trace
                                 		  writing continues from the next line after the header is written. If setHeader is called after a file output has started,  it
                                 		  will take effect from the next file to be written.

Usage:

```
tm = TraceManagerFactory.registerModule(this);
tw = newLogFileTraceWriter(“trace”, “log”, 10, 1024*1024);
tw.setHeader(header);
tm.getTraceWriterManager().addTraceWriter(tw);
```

## OutputStreamTraceWriter

OutputStreamTraceWriter wraps an output stream in a TraceWriter.
                              		  This simplifies adding custom tracing classes that can co-exist with other
                              		  TraceWriters.

### Declaration

```
public final class OutputStreamTraceWriter extends BaseTraceWriter java.lang.Object
|
+-- com.cisco.services.tracing.BaseTraceWriter |
+-- com.cisco.services.tracing.OutputStreamTraceWriter
```

### All Implemented Interfaces

TraceWriter

#### Member
                              	 Summary

Member summary

Constructors

Default
                                                						constructor which is auto-flushing

Create
                                                						an OutputStreamTraceWriter

Methods

Inherited member summary

Methods inherited from class BaseTraceWriter

close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString()

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                                						notifyAll(),  wait(),  wait(),  wait()

### Constructors

#### OutputStreamTraceWriter(int,  OutputStream)

```
public OutputStreamTraceWriter (int maxTraceLevel, 
   java.io.OutputStreamoutputStream)
```

Default
                                 		  constructor which is auto-flushing

#### See
                                 		  Also:

Trace

#### OutputStreamTraceWriter(int,  OutputStream,  boolean)

```
public OutputStreamTraceWriter (int maxTraceLevel, 
   java.io.OutputStreamoutputStream, 
   booleanautoFlush)
```

Create an
                                 		  OutputStreamTraceWriter

#### See
                                 		  Also:

Trace

### Methods

#### doClose()

```
protected void doClose ()
```

Overrides:

doClose in class BaseTraceWriter

#### doFlush()

```
protected void doFlush ()
```

Overrides:

doFlush in class BaseTraceWriter

#### doPrintln(String,  int)

```
protected void doPrintln ( java.lang.String message,  intmessageNumber)
```

Description copied from
                                    			 class: com.cisco.services.tracing.BaseTraceWriter

Must be
                                 		  implemented by the various TraceWriters extending BaseTraceWriter to provide
                                 		  the specific tracing functionality

Overrides:

doPrintln in class BaseTraceWriter

#### getOutputStream()

```
public java.io.OutputStream getOutputStream ()
```

Returns:

the output stream
                                 		  associated with the TraceWriter

## SyslogTraceWriter

SyslogTraceWriter refines the BaseTraceWriter to allow tracing to syslog. Cisco syslog
                              		  specification calls for sending low level traces to a syslog collector in the
                              		  form of UDP messages. No buffering is done in this TraceWriter. The SyslogTraceWriter makes an exception to the println()
                              		  method in that it places a ’\0’ instead of a System specified line separator to
                              		  terminate the message packet.

### Declaration

```
public final class SyslogTraceWriter extends BaseTraceWriter java.lang.Object
|
+-- com.cisco.services.tracing.BaseTraceWriter |
+-- com.cisco.services.tracing.SyslogTraceWriter
```

### All Implemented Interfaces

TraceWriter

### Member
                           	 Summary

Member summary

Constructors

Default
                                             						SyslogTraceWriter with a max trace level of INFORMATIONAL

SyslogTraceWriter with max trace level specified

SyslogTraceWriter which takes an array of trace levels.

Methods

Closes
                                             						the socket

The
                                             						SyslogTraceWriter makes an exception to the println() method in that it places
                                             						a ’\0’ instead of a System specified line separator to terminate the message
                                             						packet.

Inherited member summary

Methods inherited from class BaseTraceWriter

close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString()

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait()

### Constructors

#### SyslogTraceWriter(int,  String)

```
public SyslogTraceWriter (int port,  
   java.lang.Stringcollector)
```

Default
                                 		  SyslogTraceWriter with a max trace level of INFORMATIONAL

#### See
                                 		  Also:

Trace

#### SyslogTraceWriter(int,  String,  int)

```
public SyslogTraceWriter (int port, 
   java.lang.Stringcollector, 
   intmaxTraceLevel)
```

SyslogTraceWriter
                                 		  with max trace level specified

#### See
                                 		  Also:

Trace

#### SyslogTraceWriter(int,  String,  int[])

```
public SyslogTraceWriter (int port, 
   java.lang.Stringcollector, 
   int[]traceLevels)
```

SyslogTraceWriter
                                 		  which takes an array of trace levels.

#### See
                                 		  Also:

Trace

### Methods

#### doClose()

```
public void doClose ()
```

Closes the socket

Overrides:

doClose in class BaseTraceWriter

#### doPrintln(String,  int)

```
protected void doPrintln (java.lang.String message, 
   intmessageNumber)
```

The SyslogTraceWriter makes an exception to the println()
                                 		  method in that it places a ’\0’ instead of a System specified line separator to
                                 		  terminate the message packet. The portion of the message after a ’\r’ or ’\n’
                                 		  is ignored

Overrides:

doPrintln in class BaseTraceWriter

#### main(String[])

```
public static void main (java.lang.String[] args)
```

## TraceManagerFactory

The TraceManagerFactory class is a class by which applications
                              		  obtain a TraceManager object. The TraceModule passed in the constructor is
                              		  registered in a list. The list can be enumerated using the getModules() method.

### Declaration

```
public class TraceManagerFactory java.lang.Object
|
+-- com.cisco.services.tracing.TraceManagerFactory
```

### Member
                           	 Summary

Member summary

Methods

Returns
                                             						an enumeration of the TraceModules registered with this factory.

Returns
                                             						an instance of a TraceManager object.

Returns
                                             						an instance of a TraceManager object.

Returns
                                             						an instance of a TraceManager object.

Inherited member summary

Methods inherited from class Object

clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  toString(),  wait(),  wait(),  wait()

### Methods

#### getModules()

```
public static java.util.Enumeration getModules ()
```

Returns an
                                 		  enumeration of the TraceModules registered with this factory.

#### registerModule(TraceModule)

```
public static com.cisco.services.tracing.TraceManager registerModule (com.cisco.services.tracing.TraceModule module)
```

Returns an
                                 		  instance of a TraceManager object. The contained TraceWriterManager will not
                                 		  have any default TraceWriters.

#### registerModule(TraceModule,  String[], 
                                 		  TraceWriterManager)

```
public static com.cisco.services.tracing.TraceManager registerModule (com.cisco.services.tracing.TraceModule module, 
   java.lang.String[]subFacilities, 
   com.cisco.services.tracing.TraceWriterManagertraceWriterManager)
```

Returns an
                                 		  instance of a TraceManager object. Trace output will be redirected to the
                                 		  TraceWriterManager object specified.

#### registerModule(TraceModule,  TraceWriterManager)

```
public static com.cisco.services.tracing.TraceManager registerModule (com.cisco.services.tracing.TraceModule module, 
   com.cisco.services.tracing.TraceWriterManagertraceWriterManager)
```

Returns
                                 		  an instance of a TraceManager object. Trace output will be redirected to the
                                 		  TraceWriterManager object specified.

## Services Tracing
                        	 Interface Hierarchy

The
                              		  following interface hierarchy is contained in the com.cisco.services.tracing
                              		  package.

```
com.cisco.services.tracing. Trace com.cisco.services.tracing. ConditionalTrace com.cisco.services.tracing. UnconditionalTrace
```

```
com.cisco.services.tracing. TraceManager
```

```
com.cisco.services.tracing. TraceModule
```

```
com.cisco.services.tracing. TraceWriter
```

```
com.cisco.services.tracing. TraceWriterManager
```

## Trace

The Trace interface defines the methods that allow application
                              		  tracing. Trace also defines the standard trace types as specified by
                              		  Syslog Trace Logging.Syslog currently defines 8 levels of trace. The severity
                              		  of the message is indicated in the trace as a number ranging between [0-7] (0
                              		  and 7 included). Currently 7 is HIGHEST_LEVEL and 0 is the LOWEST_LEVEL trace.
                              		  All 8 levels are predefined here as static int types for reference in tracing
                              		  sub-system implementations.

The
                              		  severities traced are as follows:

0  = 
                              		  EMERGENCIES System unusable

1  = 
                              		  ALERTS Immediate action needed

2  = 
                              		  CRITICAL Critical conditions

3  = 
                              		  ERROR Error conditions

4  = 
                              		  WARNING Warning conditions

5  = 
                              		  NOTIFICATION Normal but significant condition

6  = 
                              		  INFORMATIONAL Informational messages only

7  = 
                              		  DEBUGGING Debugging messages

### Declaration

```
public interface Trace
```

### All Known Subinterfaces

ConditionalTrace UnconditionalTrace

### Member
                           	 Summary

Member summary

Fields

The
                                             						application will continue working on the tasks but all functions may not be
                                             						operational (one or more devices in the list are not accessible but others in
                                             						the list can be accessed)

Syslog
                                             						severity level  =  1

String
                                             						descriptor for ALERTS trace level

A
                                             						critical failure,  the application cannot accomplish the tasks required due to
                                             						this failure,  e.g.: the application cant open the database to read the device
                                             						list

Syslog
                                             						severity level  =  2

String
                                             						descriptor for CRITICAL trace level

Very
                                             						detailed information regarding errors or processing status that is only
                                             						generated when DEBUG mode has been enabled

Syslog
                                             						severity level  =  7

String
                                             						descriptor for the DEBUGGING trace level

Emergency situation,  a system shutdown is necessary

Syslog
                                             						severity level  =  0

String
                                             						descriptor for EMERGENCIES trace level

An
                                             						error condition of some kind has occurred and the user needs to understand the
                                             						nature of that failure

Syslog
                                             						severity level  =  3

String
                                             						descriptor for ERROR trace level

The
                                             						highest trace level,  currently this is DEBUGGING with a trace level of 7

Information of some form not relating to errors,  warnings,  audit,  or debug

Syslog
                                             						severity level  = 6

String
                                             						descriptor for INFORMATIONAL trace level

The
                                             						lowest trace level,  currently this is EMERGENCIES with a trace level of 0

Notification denotes a normal but significant condition

Syslog
                                             						severity level  =  5

String descriptor for NOTIFICATION trace level

Warning that a problem of some form exists but is not keeping the application
                                             						from completing its tasks

Syslog
                                             						severity level  =  4

String descriptor for WARNING trace level

Methods

Returns the name of this Trace object.

Returns the subFacility of trace

Returns the type of trace.

Returns the state of this Trace object.

Prints the string returned by the Object.toString() method and terminates the
                                             						line as defined by the system.

Prints a message in the same format as Trace.print() and terminates the line as
                                             						defined by the system.

Prints the string returned by the Object.toString() method and terminates the
                                             						line as defined by the system.

Prints a message in the same format as Trace.print() and terminates the line as
                                             						defined by the system.

Sets
                                             						a default mnemonic for all messages printed out to this trace.

### Fields

#### ALERTS

```
public static final int ALERTS
```

The application
                                 		  will continue working on the tasks but all functions may not be operational
                                 		  (one or more devices in the list are not accessible but others in the list can
                                 		  be accessed)

Syslog severity
                                 		  level  =  1

#### ALERTS_TRACE_NAME

```
public static final java.lang.String ALERTS_TRACE_NAME
```

String descriptor
                                 		  for ALERTS trace level

#### CRITICAL

```
public static final int CRITICAL
```

A critical
                                 		  failure,  the application cannot accomplish the tasks required due to this
                                 		  failure,  e.g.: the application cant open the database to read the device list

Syslog severity
                                 		  level  =  2

#### CRITICAL_TRACE_NAME

```
public static final java.lang.String CRITICAL_TRACE_NAME
```

String descriptor
                                 		  for CRITICAL trace level

#### DEBUGGING

```
public static final int DEBUGGING
```

Very detailed
                                 		  information regarding errors or processing status that is only generated when
                                 		  DEBUG mode has been enabled

Syslog severity
                                 		  level  =  7

#### DEBUGGING_TRACE_NAME

```
public static final java.lang.String DEBUGGING_TRACE_NAME
```

String descriptor
                                 		  for the DEBUGGING trace level

#### EMERGENCIES

```
public static final int EMERGENCIES
```

Emergency
                                 		  situation,  a system shutdown is necessary

Syslog severity
                                 		  level  =  0

#### EMERGENCIES_TRACE_NAME

```
public static final java.lang.String EMERGENCIES_TRACE_NAME
```

String descriptor
                                 		  for EMERGENCIES trace level

#### ERROR

```
public static final int ERROR
```

An error condition
                                 		  of some kind has occurred and the user needs to understand the nature of that
                                 		  failure

Syslog severity
                                 		  level  =  3

#### ERROR_TRACE_NAME

```
public static final java.lang.String ERROR_TRACE_NAME
```

String descriptor
                                 		  for ERROR trace level

#### HIGHEST_LEVEL

```
public static final int HIGHEST_LEVEL
```

The highest trace
                                 		  level,  currently this is DEBUGGING with a trace level of 7

#### INFORMATIONAL

```
public static final int INFORMATIONAL
```

Information of
                                 		  some form not relating to errors,  warnings,  audit,  or debug

Syslog severity
                                 		  level  = 6

#### INFORMATIONAL_TRACE_NAME

```
public static final java.lang.String INFORMATIONAL_TRACE_NAME
```

String descriptor
                                 		  for INFORMATIONAL trace level

#### LOWEST_LEVEL

```
public static final int LOWEST_LEVEL
```

The lowest trace
                                 		  level,  currently this is EMERGENCIES with a trace level of 0

#### NOTIFICATION

```
public static final int NOTIFICATION
```

Notification
                                 		  denotes a normal but significant condition

Syslog severity
                                 		  level  =  5

#### NOTIFICATION_TRACE_NAME

```
public static final java.lang.String NOTIFICATION_TRACE_NAME
```

String descriptor
                                 		  for NOTIFICATION trace level

#### WARNING

```
public static final int WARNING
```

Warning that a
                                 		  problem of some form exists but is not keeping the application from completing
                                 		  its tasks

Syslog severity
                                 		  level  =  4

#### WARNING_TRACE_NAME

```
public static final java.lang.String WARNING_TRACE_NAME
```

String
                                 		  descriptor for WARNING trace level

### Methods

#### getName()

```
public java.lang.String getName ()
```

Returns:

the name of this
                                 		  Trace object

#### getSubFacility()

```
public java.lang.String getSubFacility ()
```

Returns:

the trace
                                 		  subFacility type

#### getType()

```
public int getType ()
```

Returns:

the type of trace
                                 		  as specified in Syslog. DEBUGGING,  INFORMATIONAL,  WARNING,  etc.

#### isEnabled()

```
public boolean isEnabled ()
```

Returns the state
                                 		  of this Trace object. By default,  Trace objects are enabled,  that is,  println()
                                 		  method will always trace. The state may not be changed through this interface, 
                                 		  however,  this object may implement additional interfaces that allow the state
                                 		  to be changed.

Returns:

true if tracing is
                                 		  enabled,  false otherwise

#### See
                                 		  Also

ConditionalTrace

#### println(Object)

```
public void println (java.lang.Object object)
```

Prints the string
                                 		  returned by the Object.toString() method and terminates the line as defined by
                                 		  the system.

Parameters:

object - the object to be printed

#### println(String)

```
public void println (java.lang.String message)
```

Prints a message
                                 		  in the same format as Trace.print() and terminates the line as defined by the
                                 		  system.

Parameters:

message - the message to be printed

#### println(String,  Object)

```
public void println (java.lang.String mnemonic, 
   java.lang.Objectobject)
```

Prints the string
                                 		  returned by the Object.toString() method and terminates the line as defined by
                                 		  the system.

Parameters:

object - the object to be printed

mnemonic - the mnemonic mapped to message to be printed

#### println(String,  String)

```
public void println (java.lang.String mnemonic, 
   java.lang.Stringmessage)
```

Prints a message
                                 		  in the same format as Trace.print() and terminates the line as defined by the
                                 		  system.

Parameters:

message - the message to be printed

mnemonic - the mnemonic mapped to message to be printed

#### setDefaultMnemonic(String)

```
public void setDefaultMnemonic (java.lang.String mnemonic)
```

Sets a default
                                 		  mnemonic for all messages printed out to this trace.

Parameters:

mnemonic, - a mnemonic string

## ConditionalTrace

The ConditionalTrace interface extends the Trace interface and defines the methods that allow enabling
                              		  and disabling of tracing for this particular condition.

Typically,  applications obtain one ConditionalTrace object for
                              		  each condition that they need to trace under certain circumstances but not
                              		  always (for example,  AUDIT,  INFO,  and so on).

### Declaration

```
public interface ConditionalTrace extends Trace
```

### All Superinterfaces

Trace

### Member
                           	 Summary

Member summary

Methods

Disables this condition for tracing.

Enables
                                             						this condition for tracing.

Inherited member summary

Fields inherited from interface Trace

ALERTS , ALERTS_TRACE_NAME , CRITICAL , CRITICAL_TRACE_NAME , DEBUGGING , DEBUGGING_TRACE_NAME , EMERGENCIES , EMERGENCIES_TRACE_NAME , ERROR , ERROR_TRACE_NAME , HIGHEST_LEVEL , INFORMATIONAL , INFORMATIONAL_TRACE_NAME , LOWEST_LEVEL , NOTIFICATION , NOTIFICATION_TRACE_NAME , WARNING , WARNING_TRACE_NAME

Methods inherited from interface Trace

getName() , getSubFacility() , getType() , isEnabled() , println(Object) , println(String) , println(String, Object) , println(String, String) , setDefaultMnemonic(String)

#### Methods

##### disable()

```
public void disable ()
```

Disables this
                                    		  condition for tracing.

##### enable()

```
public void enable ()
```

Enables this
                                    		  condition for tracing.

## UnconditionalTrace

The UnconditionalTrace interface extends the Trace interface. Note that because this object extends
                              		  Trace,  its state is enabled by default and it may not be changed.

Typically,  applications would obtain one UnconditionalTrace
                              		  object per each condition that they need to trace always under any
                              		  circumstances (such as,  ERROR,  FATAL,  and so on).

### Declaration

```
public interface UnconditionalTrace extends Trace
```

### All Superinterfaces

Trace

### Member
                           	 Summary

Inherited Member summary

Fields inherited from interface Trace

ALERTS , ALERTS_TRACE_NAME , CRITICAL , CRITICAL_TRACE_NAME , DEBUGGING , DEBUGGING_TRACE_NAME , EMERGENCIES , EMERGENCIES_TRACE_NAME , ERROR , ERROR_TRACE_NAME , HIGHEST_LEVEL , INFORMATIONAL , INFORMATIONAL_TRACE_NAME , LOWEST_LEVEL , NOTIFICATION , NOTIFICATION_TRACE_NAME , WARNING , WARNING_TRACE_NAME

Methods inherited from interface Trace

getName() , getSubFacility() , getType() , isEnabled() , println(Object) , println(String) , println(String, Object) , println(String, String) , setDefaultMnemonic(String)

## TraceManager

The TraceManager interface defines the methods that allow
                              		  applications trace management.

Typically,  an application obtains only one TraceManager object.
                              		  All Trace objects are created by default: Predefined Trace in accordance with
                              		  Syslog definitions are:

```
ConditionalTraces:INFORMATIONAL, DEBUGGING, NOTIFICATION, WARNING
UnconditionalTraces:ERROR, CRITICAL, ALERTS, EMERGENCIES
```

### Facilities/Sub-Facilities:

Facility —A code
                                    				consisting of two or more uppercase letters that indicate the facility to which
                                    				the message refers. A facility can be a hardware device,  a protocol,  or a
                                    				module of the system software.

SubFacility —A code
                                    				consisting of two or more uppercase letters that indicate the sub-facility to
                                    				which the message refers. A sub-facility can be a hardware device component,  a
                                    				protocol unit,  or a sub-module of the system software.

By
                              		  default all 8 Conditional and UnConditional Traces are created for the Facility
                              		  and 8 for each of the subFacilities In order to use the DEBUGGING trace for the
                              		  parent FACILITY,  for example,  the application needs to use the
                              		  getConditionalTrace( "DEBUGGING" )
                              		  method of this object.

In
                              		  order to use the DEBUGGING trace for the SUBFACILITY,  for example,  the
                              		  application needs to use the getConditionalTrace( SUBFACILITY + "_" + "DEBUGGING" )
                              		  method of this object or use the getConditionalTrace( SUBFACILITY, "DEBUGGING" )
                              		  method.

System
                              		  wide TraceWriterManager is set through the setTraceWriterManager method
                              		  provided by this interface.

The
                              		  Trace Manager object also allows the application to enable or disable tracing
                              		  for all trace through the enableAll() and disableAll() methods.

### Declaration

```
public interface TraceManager
```

### Member
                           	 Summary

Member summary

Methods

Sets a
                                             						set of subFacilities for this TraceManager/Facility.

Adds a
                                             						single subFacility for this TraceManager/Facility.

Disables tracing for all Trace objects managed by this TraceManager.

Disables prefixing a time stamp for every message printed by this TraceManager.

Enables
                                             						tracing for all Trace objects managed by this TraceManager.

Enables
                                             						prefixing a time stamp for every message printed by this TraceManager.

Creates
                                             						a new ConditionalTrace object or obtains an existing ConditionalTrace object
                                             						for this condition.

Creates
                                             						a new ConditionalTrace object or obtains an existing ConditionalTrace object
                                             						for this condition and subFacility

Returns
                                             						the Facility name for this TraceManager.

Returns
                                             						the subFacility names for this TraceManager/Facility.

Returns
                                             						an enumeration of the Trace objects managed by this TraceManager.

Returns
                                             						the TraceWriter used by this TraceManager.

Creates
                                             						a new UnconditionalTrace object or obtains an existing UnconditionalTrace
                                             						object for this condition.

Creates
                                             						a new UnconditionalTrace object or obtains an existing UnconditionalTrace
                                             						object for this condition and subFacility

Removes
                                             						a Trace object given an object.

Sets a
                                             						set of subFacilities for this TraceManager/Facility.

Adds a
                                             						single subFacility for this TraceManager/Facility.

Sets
                                             						the TraceWriter to be used by this TraceManager.

### Methods

#### addSubFacilities(String[])

```
public void addSubFacilities (java.lang.String[] names)
```

Sets a set of
                                 		  subFacilities for this TraceManager/Facility.

#### addSubFacility(String)

```
public void addSubFacility (java.lang.String name)
```

Adds a single
                                 		  subFacility for this TraceManager/Facility.

#### disableAll()

```
public void disableAll ()
```

Disables tracing
                                 		  for all Trace objects managed by this TraceManager.

#### disableTimeStamp()

```
public void disableTimeStamp ()
```

Disables prefixing
                                 		  a time stamp for every message printed by this TraceManager.

#### enableAll()

```
public void enableAll ()
```

Enables tracing
                                 		  for all Trace objects managed by this TraceManager.

#### enableTimeStamp()

```
public void enableTimeStamp ()
```

Enables prefixing
                                 		  a time stamp for every message printed by this TraceManager.

#### getConditionalTrace(int)

```
public com.cisco.services.tracing.ConditionalTrace getConditionalTrace (int severity)
```

Creates a new
                                 		  ConditionalTrace object or obtains an existing ConditionalTrace object for this
                                 		  condition.

#### getConditionalTrace(String,  int)

```
public com.cisco.services.tracing.ConditionalTrace getConditionalTrace (java.lang.String subFacility, 
   intseverity)
```

Creates a new
                                 		  ConditionalTrace object or obtains an existing ConditionalTrace object for this
                                 		  condition and subFacility

#### getName()

```
public java.lang.String getName ()
```

Returns the
                                 		  Facility name for this TraceManager.

#### getSubFacilities()

```
public java.lang.String[] getSubFacilities ()
```

Returns the
                                 		  subFacility names for this TraceManager/Facility.

#### getTraces()

```
public java.util.Enumeration getTraces ()
```

Returns an
                                 		  enumeration of the Trace objects managed by this TraceManager.

#### getTraceWriterManager()

```
public com.cisco.services.tracing.TraceWriterManager getTraceWriterManager ()
```

Returns the
                                 		  TraceWriter used by this TraceManager.

#### getUnconditionalTrace(int)

```
public com.cisco.services.tracing.UnconditionalTrace getUnconditionalTrace (int severity)
```

Creates a new
                                 		  UnconditionalTrace object or obtains an existing UnconditionalTrace object for
                                 		  this condition.

#### getUnconditionalTrace(String,  int)

```
public com.cisco.services.tracing.UnconditionalTrace getUnconditionalTrace (java.lang.String subFacility, 
   intseverity)
```

Creates a new
                                 		  UnconditionalTrace object or obtains an existing UnconditionalTrace object for
                                 		  this condition and subFacility

#### removeTrace(Trace)

```
public void removeTrace (com.cisco.services.tracing.Trace tc)
```

Removes a Trace
                                 		  object given an object.

#### setSubFacilities(String[])

```
public void setSubFacilities (java.lang.String[] names)
```

Deprecated and replaced
                                 		  with TraceManager.addSubFacilities method

Sets a set of
                                 		  subFacilities for this TraceManager/Facility.

#### setSubFacility(String)

```
public void setSubFacility (java.lang.String name)
```

Deprecated and
                                 		  replaced with TraceManager.addSubFacility method

Adds a single
                                 		  subFacility for this TraceManager/Facility.

#### setTraceWriterManager(TraceWriterManager)

```
public void setTraceWriterManager (com.cisco.services.tracing.TraceWriterManager twm)
```

Sets the
                                 		  TraceWriter to be used by this TraceManager.

## TraceModule

The TraceModule interface serves two purposes. First,  it allows
                              		  applications to discover the TraceManager object used by other packages that
                              		  they use. Second,  applications that register with the TraceManagerFactory must
                              		  identify themselves by implementing this interface.

### Declaration

```
public interface TraceModule
```

### All Known Subinterfaces

com.cisco.jtapi.extensions.CiscoJtapiPeer

### Member
                           	 Summary

Member summary

Methods

Returns
                                             						the TraceManager that an object is using for tracing.

Returns
                                             						the module name.

### Methods

#### getTraceManager()

```
public com.cisco.services.tracing.TraceManager getTraceManager ()
```

Returns the
                                 		  TraceManager that an object is using for tracing.

#### getTraceModuleName()

```
public java.lang.String getTraceModuleName ()
```

Returns the module
                                 		  name.

## TraceWriter

The TraceWriter interface abstracts the details of trace
                              		  message output. The TraceWriter uses its enabled method to advertise whether or not the print and println methods will have any effect. Users of TraceWriter should use the value returned by the getEnabled method as an indication of whether they should
                              		  invoke the print and println methods at all.

### Declaration

```
public interface TraceWriter
```

### All Known Subinterfaces

TraceWriterManager

### All Known Implementing Classes

BaseTraceWriter

### Member
                           	 Summary

Member summary

Methods

Releases any resources associated by this TraceWriter .

flush() Forces output of any messages that
                                             						have been printed using the println method

Returns
                                             						whether the println method will print anything or not.

Prints
                                             						the specified string followed by a carriage return The concrete TraceWriter
                                             						class will use the severity to block out messages from a particular stream.

set the
                                             						trace levels that will be traced by this TraceWriter

### Methods

#### close()

```
public void close ()
```

Releases any
                                 		  resources associated by this TraceWriter .

#### flush()

```
public void flush ()
```

Forces output of
                                 		  any messages that have been printed using the println method

#### getDescription()

```
public java.lang.String getDescription ()
```

Returns:

a short
                                 		  description of this TraceWriter

#### getEnabled()

```
public boolean getEnabled ()
```

Returns whether
                                 		  the println method will print anything or not. A closed TraceWriter will always return false from this method.

Returns:

true if this
                                 		  TraceWriter is enabled,  false if not

#### getName()

```
public java.lang.String getName ()
```

Returns:

the name of this
                                 		  TraceWriter

#### getTraceLevels()

```
public int[] getTraceLevels ()
```

Returns:

the array of trace
                                 		  levels that will be traced by this TraceWriter

#### println(String,  int)

```
public void println (java.lang.String message, 
   intseverity)
```

Prints the
                                 		  specified string followed by a carriage return The concrete TraceWriter class
                                 		  will use the severity to block out messages from a particular stream. Each
                                 		  trace writer has a notion of the highest level trace it traces

Parameters:

message - the string to print

severity - of the trace.

#### See
                                 		  Also

Trace

#### setTraceLevels(int[])

```
public void setTraceLevels (int[] levels)
```

set the trace
                                 		  levels that will be traced by this TraceWriter

Parameters:

int[] - levels

#### See
                                 		  Also

Trace

## TraceWriterManager

TraceWriterManager contains the list of TraceWriter objects that
                              		  are used to implement the tracing. The list is populated at startup from the
                              		  switches in a .ini file. A LogFileTraceWriter,  a ConsoleTraceWriter,  and a
                              		  SyslogTraceWriter are available. Users can override the existing TraceWriters
                              		  by setting a user implemented TraceWriter[] or adding to the existing
                              		  TraceWriters. This makes it possible to add other TraceWriters that can
                              		  function along with existing trace writers.

### Declaration

```
public interface TraceWriterManager extends TraceWriter
```

### All Superinterfaces

TraceWriter

### Member
                           	 Summary

Member summary

Methods

Add
                                             						another TraceWriter to the array

Remove
                                             						the TraceWriter from the array in the manager

Implementations can use this method to override or enhance the provided
                                             						TraceWriters

Inherited member summary

Methods inherited from interface TraceWriter

close() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[])

### Methods

#### addTraceWriter(TraceWriter)

```
public void addTraceWriter (com.cisco.services.tracing.TraceWriter traceWriter)
```

Add another
                                 		  TraceWriter to the array

Parameters:

TraceWriter - to be added to the list

#### getTraceWriters()

```
public com.cisco.services.tracing.TraceWriter[] getTraceWriters ()
```

Returns:

the array of
                                 		  TraceWriters in the manager

#### removeTraceWriter(TraceWriter)

```
public void removeTraceWriter (com.cisco.services.tracing.TraceWriter traceWriter)
```

Remove the
                                 		  TraceWriter from the array in the manager

#### setTraceWriters(TraceWriter[])

```
public void setTraceWriters (com.cisco.services.tracing.TraceWriter[] traceWriters)
```

Implementations
                                 		  can use this method to override or enhance the provided TraceWriters

Parameters:

set - the array of TraceWriters.

## Tracing Implementation Class Hierarchy

The following tracing implementation class hierarchy is
                              contained in the com.cisco.services.tracing.implementation package.

```
java.lang.Object
   com.cisco.services.tracing.implementation. TraceImpl (implements
                                                com.cisco.services.tracing.Trace)
   com.cisco.services.tracing.implementation. ConditionalTraceImpl (implements
                           com.cisco.services.tracing.ConditionalTrace)
   com.cisco.services.tracing.implementation. UnconditionalTraceImpl (implements
                         com.cisco.services.tracing.UnconditionalTrace)
com.cisco.services.tracing.implementation. TraceManagerImpl (implements
                                    com.cisco.services.tracing.TraceManager)
com.cisco.services.tracing.implementation. TraceWriterManagerImpl (implements
                              com.cisco.services.tracing.TraceWriterManager)
```

## TraceImpl

### Declaration

public abstract class TraceImpl

extends java.lang.Object

implements Trace

### All Implemented Interfaces

Trace

### Methods

#### println

public
                                 		  final void println (java.lang.String message)

Description copied from interface: Trace

Prints
                                 		  a message in the same format as Trace.print() and terminates the line as
                                 		  defined by the system.

Specified by:

println
                                 		  in interface Trace

Parameters :

message
                                 		  - the message to be printed

#### println

public
                                 		  final void println(java.lang.String mnemonic,  java.lang.String message)

Description copied from interface: Trace

Prints
                                 		  a message in the same format as Trace.print() and terminates the line as
                                 		  defined by the system.

Specified by :

println
                                 		  in interface Trace

Parameters :

mnemonic - the mnemonic mapped to message to be printed

message
                                 		  - the message to be printed

#### println

public
                                 		  final void println (java.lang.Object object)

Description copied from interface: Trace

Prints
                                 		  the string returned by the Object.toString() method and terminates the line as
                                 		  defined by the system.

Specified by :

println
                                 		  in interface Trace

Parameters :

object
                                 		  - the object to be printed

#### println

public
                                 		  final void println (java.lang.String mnemonic,  java.lang.Object object)

Description copied from interface: Trace

Prints
                                 		  the string returned by the Object.toString() method and terminates the line as
                                 		  defined by the system.

Specified by :

println
                                 		  in interface Trace

Parameters :

mnemonic - the mnemonic mapped to message to be printed

object
                                 		  - the object to be printed

#### getName

public
                                 		  final java.lang.String getName ()

Description copied from interface: Trace

Returns
                                 		  the name of this Trace object.

Specified by :

getName
                                 		  in interface Trace

Returns :

the
                                 		  name of this Trace object

#### setDefaultMnemonic

public
                                 		  final void setDefaultMnemonic (java.lang.String mnemonic)

Description copied from interface: Trace

Sets a
                                 		  default mnemonic for all messages printed out to this trace.

Specified by :

setDefaultMnemonic in interface Trace

Parameters :

mnemonic - a mnemonic string

#### getType

public
                                 		  int getType ()

Description copied from interface: Trace

Returns
                                 		  the type of trace.

Specified by :

getType
                                 		  in interface Trace

Returns :

the
                                 		  trace severity as specified in Syslog. DEBUGGING,  INFORMATIONAL,  WARNING,  etc.

#### getSubFacility

public java.lang.String getSubFacility ()

Description copied from interface: Trace

Returns the subFacility of trace

Specified by :

getSubFacility in interface Trace

Returns :

the
                                 		  trace subFacility type

### Inherited Methods

isEnabled

## ConditionalTraceImpl

### Declaration

public final class ConditionalTraceImpl

extends TraceImpl

implements ConditionalTrace

### All Implemented
                           	 Interfaces

ConditionalTrace,  Trace

### Methods

#### enable

public
                                 		  void enable ()

Description copied from interface: ConditionalTrace

Enables
                                 		  this condition for tracing.

Specified by :

enable
                                 		  in interface ConditionalTrace

#### disable

public
                                 		  void disable ()

Description copied from interface: ConditionalTrace

Disables this condition for tracing.

Specified by :

disable
                                 		  in interface ConditionalTrace

#### isEnabled

public
                                 		  boolean isEnabled ()

Description copied from interface: Trace

Returns
                                 		  the state of this Trace object. By default,  Trace objects are enabled,  that is, 
                                 		  println() method will always trace. The state may not be changed through this
                                 		  interface,  however,  this object may implement additional interfaces that allow
                                 		  the state to be changed.

Specified by :

isEnabled in interface Trace

Returns :

true if
                                 		  tracing is enabled,  false otherwise

See Also :

ConditionalTrace

### Inherited
                           	 Methods

Inherited methods from class java.lang.Object are: clone, 
                                 		  equals,  finalize,  getClass,  hashCode,  notify,  notifyAll,  toString,  wait,  wait, 
                                 		  wait.

## UnconditionalTraceImpl

### Declaration

public final class UnconditionalTraceImpl

extends TraceImpl

implements UnconditionalTrace

### All Implemented
                           	 Interfaces

Trace, 
                                 		  UnconditionalTrace

### Methods

#### isEnabled

public
                                 		  boolean isEnabled ()

Description copied from interface: Trace

Returns
                                 		  the state of this Trace object. By default,  Trace objects are enabled,  that is, 
                                 		  println() method will always trace. The state may not be changed through this
                                 		  interface,  however,  this object may implement additional interfaces that allow
                                 		  the state to be changed.

Specified by :

isEnabled in interface Trace

Returns :

true if
                                 		  tracing is enabled,  false otherwise

See Also :

ConditionalTrace

### Inherited
                           	 Methods

Inherited methods from class java.lang.Object are: clone, 
                                 		  equals,  finalize,  getClass,  hashCode,  notify,  notifyAll,  toString,  wait,  wait, 
                                 		  wait.

## TraceManagerImpl

The TraceManagerImpl class implements the TraceManager interface.

### Declaration

public class TraceManagerImpl extends java.lang.Object

java.lang.Object

|

+--com.cisco.services.tracing.implementation.TraceManagerImpl

### All Implemented Interfaces

TraceManager

### Constructors

public TraceManagerImpl (java.lang.StringmoduleName, 
                                 		  java.lang.String[]subFacilities,  TraceWriterManagertraceWriterManager)

public TraceManagerImpl (java.lang.StringmoduleName, 
                                 		  TraceWriterManagertraceWriterManager)

### Methods

#### getConditionalTrace

```
public ConditionalTrace getConditionalTrace (intseverity)
```

Description copied from
                                    			 interface : TraceManager

Creates a new
                                 		  ConditionalTrace object or obtains an existing ConditionalTrace object for this
                                 		  condition.

Specified by:

getConditionalTrace in interface TraceManager

#### getConditionalTrace

```
public ConditionalTrace getConditionalTrace(java.lang.StringsubFacility, 
   intseverity)
```

Description copied from
                                    			 interface: TraceManager

Creates a new
                                 		  ConditionalTrace object or obtains an existing ConditionalTrace object for this
                                 		  condition and subFacility

Specified by:

getConditionalTrace in interface TraceManager

#### getUnconditionalTrace

```
public UnconditionalTrace getUnconditionalTrace(intseverity)
```

Description copied from
                                    			 interface: TraceManager

Creates a new
                                 		  UnconditionalTrace object or obtains an existing UnconditionalTrace object for
                                 		  this condition.

Specified by:

getUnconditionalTrace in interface TraceManager

#### getUnconditionalTrace

```
public UnconditionalTrace getUnconditionalTrace(java.lang.StringsubFacility, 
   intseverity)
```

Description copied from
                                    			 interface: TraceManager

Creates a new
                                 		  UnconditionalTrace object or obtains an existing UnconditionalTrace object for
                                 		  this condition and subFacility

Specified by:

getUnconditionalTrace in interface TraceManager

#### getTraceWriterManager

```
public TraceWriterManager getTraceWriterManager()
```

Description copied from
                                    			 interface: TraceManager

Returns the
                                 		  TraceWriter used by this TraceManager.

Specified by:

getTraceWriterManager in interface TraceManager

#### setTraceWriterManager

```
public void setTraceWriterManager(TraceWriterManagerout)
```

Description copied from
                                    			 interface: TraceManager

Sets the
                                 		  TraceWriter to be used by this TraceManager.

Specified by:

setTraceWriterManager in interface TraceManager

#### removeTrace

```
public void removeTrace(Tracetc)
```

Description copied from
                                    			 interface: TraceManager

Removes a Trace
                                 		  object given an object.

Specified by:

removeTrace in
                                 		  interface TraceManager

#### getTraces

```
public java.util.Enumeration getTraces()
```

Description copied from
                                    			 interface: TraceManager

Returns an
                                 		  enumeration of the Trace objects managed by this TraceManager.

Specified by:

getTraces in
                                 		  interface TraceManager

#### enableAll

```
public void enableAll()
```

Description copied from
                                    			 interface: TraceManager

Enables tracing
                                 		  for all Trace objects managed by this TraceManager.

Specified by:

enableAll in
                                 		  interface TraceManager

#### disableAll

```
public void disableAll()
```

Description copied from
                                    			 interface: TraceManager

Disables tracing
                                 		  for all Trace objects managed by this TraceManager.

Specified by:

disableAll in
                                 		  interface TraceManager

#### getName

```
public java.lang.String getName()
```

Description copied from
                                    			 interface: TraceManager

Returns the
                                 		  Facility name for this TraceManager.

Specified by:

getName in
                                 		  interface TraceManager

#### enableTimeStamp

```
public void enableTimeStamp()
```

Description copied from
                                    			 interface: TraceManager

Enables
                                 		  prefixing a time stamp for every message printed by this TraceManager.

Specified by:

enableTimeStamp in interface TraceManager

#### disableTimeStamp

```
public void disableTimeStamp()
```

Description copied from
                                    			 interface: TraceManager

Disables
                                 		  prefixing a time stamp for every message printed by this TraceManager.

Specified by:

disableTimeStamp in interface TraceManager

#### getSubFacilities

```
public java.lang.String[] getSubFacilities()
```

Returns the
                                 		  subFacility names for this TraceManager/Facility.

Specified by:

getSubFacilities in interface TraceManager

#### addSubFacilities

```
public void addSubFacilities(java.lang.String[]names)
```

Adds
                                 		  subFacilities for this TraceManager/Facility.

Specified by:

addSubFacilities in interface TraceManager

#### addSubFacility

```
public void addSubFacility(java.lang.Stringname)
```

Adds a
                                 		  subFacility for this TraceManager/Facility.

Specified by:

addSubFacility in interface TraceManager

### Deprecated

#### getSubFacilities(java.lang.String[]names)

Replaced by addSubFacilties(String[]).

#### setSubFacility(java.lang.Stringname)

Replaced by addSubFacility(String).

### Inherited
                           	 Methods

Inherited methods from class java.lang.Object are: clone, 
                                 		  equals,  finalize,  getClass,  hashCode,  notify,  notifyAll,  toString,  wait,  wait, 
                                 		  wait.

## TraceWriterManagerImpl

TraceWriterManager contains the list of TraceWriter objects that
                              		  are used to implement the tracing. The list is populated at startup from the
                              		  switches in a .ini file. A LogFileTraceWriter,  a ConsoleTraceWriter,  and a
                              		  SyslogTraceWriter are available. Users can override the existing TraceWriters
                              		  by setting a user implemented TraceWriter[] or adding to the existing
                              		  TraceWriters. This makes it possible to add other traceWriters that can
                              		  function along with exisiting trace writers.

Methods
                                          			 inherited from class java.lang.Object are clone,  equals,  finalize,  getClass, 
                                          			 hashCode,  notify,  notifyAll,  toString,  wait,  wait,  wait.

### Declaration

public class TraceWriterManagerImpl extends java.lang.Object implements TraceWriterManager

java.lang.Object

com.cisco.services.tracing.implementation.TraceWriterManagerImpl

### All Implemented
                           	 Interfaces

TraceWriter,  TraceWriterManager

### Constructors

#### TraceWriterManagerImpl

```
public TraceWriterManagerImpl()
```

Creates a
                                 		  TraceWriterManagerImpl with a zero length TraceWriter array .

### Methods

#### setTraceWriters

```
public void setTraceWriters(TraceWriter[]traceWriters)
```

Overrides the
                                 		  existing TraceWriters with a new user supplied set .

Specified by:

setTraceWriters in
                                 		  interface TraceWriterManager

Parameters:

traceWriters - An
                                 		  array of TraceWriters.

#### getTraceWriters

```
public TraceWriter[] getTraceWriters()
```

Returns the array
                                 		  of TraceWriters currently in use .

Specified by:

getTraceWriters in
                                 		  interface TraceWriterManager

Returns:

The array of
                                 		  TraceWriters in the manager.

#### addTraceWriter

```
public void addTraceWriter(TraceWritertw)
```

Add this
                                 		  TraceWriter to the array of trace writers

Specified by:

addTraceWriter in
                                 		  interface TraceWriterManager

Parameters:

tw - TraceWriter
                                 		  to be added to the list

#### removeTraceWriter

```
public void removeTraceWriter(TraceWritertw)
```

Remove the
                                 		  Tracewriter from the array of trace writers.

Specified by:

removeTraceWriter in interface TraceWriterManager

#### println

```
public void println(java.lang.Stringmessage,  intseverity)
```

All traces invoke
                                 		  this method. A trace supplies its severity along with the message. Traces below
                                 		  the threshold severity of the TraceWriter are allowed. Eg. If the Threshhold
                                 		  severity is set to INFORMATIONAL (level  =  6) DEBUG traces will not be passed by
                                 		  the TraceWriter. The severity level is set in the constructor of the
                                 		  TraceWriter

Specified by:

println in
                                 		  interface TraceWriter

Parameters:

message - The
                                 		  string to print

severity - The
                                 		  severity of the trace.

See Also:

Trace

Flush

#### public void
                                 		  flush()

Description copied from
                                    			 interface: TraceWriter

Forces output of
                                 		  any messages that have been printed using the println method

Specified by:

flush in interface TraceWriter

#### close

```
public void close()
```

Description copied from
                                    			 interface: TraceWriter

Releases any
                                 		  resources associated by this TraceWriter.

Specified by:

close in interface TraceWriter

#### getEnabled

```
public boolean getEnabled()
```

Returns true if
                                 		  any one of the underlying TraceWriter is enabled,  else returns false.

Specified by:

getEnabled in
                                 		  interface TraceWriter

Returns:

True if this
                                 		  TraceWriter is enabled, false if not.

#### getName

```
public java.lang.String getName()
```

Specified by:

getName in
                                 		  interface TraceWriter

Returns:

The name of this
                                 		  TraceWriter.

#### getDescription

```
public java.lang.String getDescription()
```

Specified by:

getDescription in interface TraceWriter

Returns:

A short
                                 		  description of this TraceWriter.

#### setTraceLevels

```
public void setTraceLevels(int[]levels)
```

The
                                 		  TraceWriterManager does nothing for this method .

Specified by:

setTraceLevels in interface TraceWriter

Parameters:

Levels - Array
                                 		  of trace levels.

See Also:

Trace

#### getTraceLevels

```
public int[] getTraceLevels()
```

The
                                 		  TraceWriterManager returns a null,  as the traceLevel is maintained at the
                                 		  individual TraceWriter .

Specified by:

getTraceLevels in interface TraceWriter

Returns:

null

| Note | More than one
                                             			 parameter can be sent by specifying a ParameterList |
|---|---|

| Member summary |
|---|
| Constructors |
|  | AlarmManager(String, AlarmWriter, Trace, UnconditionalTrace) Create
                                             						an instance of the AlarmManager for the facility. |
| Methods |
| Alarm | createAlarm(String, int) Creates
                                             						an Alarm of required severity for the subFacility |
| AlarmWriter | getAlarmWriter() |
| void | setAlarmWriter(AlarmWriter) Allows
                                             						applications to override the AlarmWriter to be used by this AlarmManager,  with
                                             						a user defined AlarmWriter |

| Inherited member summary |
|---|
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(), 
                                             						notify(),  notifyAll(),  toString(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Methods |
| void | close() close
                                             						the AlarmWriter |
| java.lang.String | getDescription() |
| boolean | getEnabled() |
| java.lang.String | getName() |
| void | send(String) Send
                                             						out the alarm message to the AlarmService. |
| void | setEnabled(boolean) Enable
                                             						or disable the AlarmWriter |

| Member summary |
|---|
| Constructors |
|  | DefaultAlarm(String, String, int, AlarmWriter) |
| Methods |
| java.lang.String | getFacility() |
| int | getSeverity() |
| java.lang.String | getSubFacility() |
| void | send(String) Send the
                                             						alarm with the specified mnemonic |
| void | send(String, ParameterList) Send the
                                             						alarm with the specified name and list of parameters. |
| void | send(String, String, String) Send
                                             						the alarm with the specified name and parameter |

| Inherited member summary |
|---|
| Fields inherited from interface Alarm |
| ALERTS , CRITICAL , DEBUGGING , EMERGENCIES , ERROR , HIGHEST_LEVEL , INFORMATIONAL , LOWEST_LEVEL , NOTIFICATION , NO_SEVERITY , UNKNOWN_MNEMONIC , WARNING |
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  toString(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Constructors |
|  | DefaultAlarmWriter(int, String) Constructor for the DefaultAlarmWriter which takes the
                                             						AlarmService hostname,  port and a queue size of fifty (50). |
|  | DefaultAlarmWriter(int, String, int) Constructor for the DefaultAlarmWriter which takes the AlarmService hostname, 
                                             						port and queue size. |
|  | DefaultAlarmWriter(int, String, int, ConditionalTrace, UnconditionalTrace) Constructor for the DefaultAlarmWriter which takes the AlarmService hostname, 
                                             						port and queue size. |
| Methods |
| void | close() Shutdown the send thread and close the socket |
| java.lang.String | getDescription() |
| boolean | getEnabled() |
| java.lang.String | getName() |
| static void | main(String[]) |
| void | send(String) send
                                             						the Alarm to the alarm service |
| void | setEnabled(boolean) Applications can dynamically enable or disable the AlarmWriter |

| Inherited member summary |
|---|
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  toString(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Constructors |
|  | ParameterList() Default
                                             						constructor for the ParameterList |
|  | ParameterList(String, String) Constructor that takes a name value pair. |
| Methods |
| void addParameter(String, String) | addParameter(String, String) method
                                             						used to add additional name value pairs (parameters) to the list |
| java.lang.String[] | getParameterNames() Get the
                                             						parameter names in the list |
| java.lang.String | getParameterValue(String) get the
                                             						value for a parameter |
| void | removeAllParameters() remove
                                             						all the parameters in the list |
| void | removeParameter(String) remove
                                             						a particular parameter if it is in the list |
| java.lang.String | toString() |

| Inherited member summary |
|---|
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Fields |
| static int | ALERTS The
                                             						application will continue working on the tasks but all functions may not be
                                             						operational (one or more devices in the list are not accessible but others in
                                             						the list can be accessed) Syslog
                                             						severity level  =  1 |
| static int | CRITICAL A
                                             						critical failure,  the application cannot accomplish the tasks required due to
                                             						this failure,  for example,  the application cannot open the database to read the
                                             						device list Syslog
                                             						severity level  =  2 |
| static int | DEBUGGING Very
                                             						detailed information regarding errors or processing status that is only
                                             						generated when DEBUG mode has been enabled Syslog
                                             						severity level  =  7 |
| static int | EMERGENCIES Emergency situation,  a system shutdown is necessary Syslog
                                             						severity level  =  0 |
| static int | ERROR An
                                             						error condition of some kind has occurred and the user needs to understand the
                                             						nature of that failure Syslog
                                             						severity level  =  3 |
| static int | HIGHEST_LEVEL The
                                             						highest trace level,  currently this is DEBUGGING with a trace level of 7 |
| static int | INFORMATIONAL Information of some form not relating to errors,  warnings,  audit,  or debug Syslog
                                             						severity level  =  6 |
| static int | LOWEST_LEVEL The
                                             						lowest trace level,  currently this is EMERGENCIES with a trace level of 0 |
| static int | NO_SEVERITY Applications can set this level to generate Alarms without a severity. |
| static int | NOTIFICATION Notification denotes a normal but significant condition Syslog
                                             						severity level  =  5 |
| static
                                             						java.lang.String | UNKNOWN_MNEMONIC String
                                             						used when a mnemonic is not specified during an Alarm send |
| static int | WARNING Warning
                                             						that a problem of some form exists but is not keeping the application from
                                             						completing its tasks Syslog
                                             						severity level  =  4 |
| Methods |
| java.lang.String | getFacility() |
| int | getSeverity() |
| java.lang.String | getSubFacility() |
| void | send(String) send
                                             						the Alarm with the specified mnemonic. |
| void | send(String, ParameterList) send
                                             						an Alarm with the specified mnemonic and supplied parameter list |
| void | send(String, String, String) send
                                             						an Alarm with the specified mnemonic and with one parameter |

| Member summary |
|---|
| Methods |
| void | close() close
                                             						the AlarmWriter |
| java.lang.String | getDescription() |
| boolean | getEnabled() |
| java.lang.String | getName() |
| void | send(String) Send
                                             						out the alarm message to the AlarmService. |
| void | setEnabled(boolean) Enable
                                             						or disable the AlarmWriter |

| Member summary |
|---|
| Constructors |
| protected | BaseTraceWriter(int[], String, String) BaseTraceWriter with trace levels as passed in traceLevels in the array falling
                                             						outside the range Trace.LOWEST_LEVEL and Trace.HIGHEST_LEVEl are ignored |
| protected | BaseTraceWriter(int, String, String) BaseTraceWriter that traces all levels up to the maxTraceLevel The trace level
                                             						is maintained in the range [Trace.HIGHEST_LEVEL,  Trace.LOWEST_LEVEL ] |
| protected | BaseTraceWriter(String, String) BaseTraceWriter which only traces the lowest level i.e. severity level, 
                                             						Trace.LOWEST_LEVEL messages |
| Methods |
| void | close() |
| protected void | doClose() |
| protected void | doFlush() |
| protected abstract void | doPrintln(String, int) Must be
                                             						implemented by the various TraceWriters extending BaseTraceWriter to provide
                                             						the specific tracing functionality |
| void | flush() |
| java.lang.String | getDescription() |
| boolean | getEnabled() |
| java.lang.String | getName() |
| int[] | getTraceLevels() |
| void | println(String, int) |
| void | setTraceLevels(int[]) |
| java.lang.String | toString() |

| Inherited member summary |
|---|
| Methods inherited from class Object |
| clone()
                                             						,  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(),  notifyAll(), 
                                             						wait(),  wait(),  wait() |

| Member summary |
|---|
| Constructors |
|  | ConsoleTraceWriter() Default
                                             						constructor,  traces all severity levels |
|  | ConsoleTraceWriter(int) Constructor that sets the maximum level to be traced. |
|  | ConsoleTraceWriter(int[]) Construct a ConsoleTraceWriter with an array of trace levels Only traces with
                                             						the severity in the tracelevel array are traced |
| Methods |
| protected void | doFlush() |
| protected void | doPrintln(String, int) |
| static void | main(String[]) |

| Inherited member summary |
|---|
| Methods inherited from class BaseTraceWriter |
| close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString() |
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait() |

| Note | All properties
                                          			 of this class are specified in the constructor; there is no way to change them
                                          			 dynamically. Caveat: If
                                          			 two instances of LogFileTraceWriter are created with the same path and dirNameBase ,  and useSameDir is true,  they may write to the same file. |
|---|---|

| Member summary |
|---|
| Fields |
| static java.lang.String | DEFAULT_FILE_NAME_BASE |
| static java.lang.String | DEFAULT_FILE_NAME_EXTENSION |
| static char | DIR_BASE_NAME_NUM_SEPERATOR |
| static int | MIN_FILE_SIZE |
| static int | MIN_FILES |
| static int | ROLLOVER_THRESHOLD |
| Constructors |
|  | LogFileTraceWriter(String, String, int, int) Default
                                             						constructor for LogFileTraceWriter that rotates among an arbitrary number of
                                             						files with tracing for all levels. |
|  | LogFileTraceWriter(String, String, String, String, int, int, boolean) Default
                                             						constructor for LogFileTraceWriter that rotates among an arbitrary number of
                                             						files with tracing for all levels. |
|  | LogFileTraceWriter(String, String, String, String, int, int, int, boolean) Constructs a LogFileTraceWriter that rotates among an arbitrary number of files
                                             						storing them in a specified directory. |
| Methods |
| protected void | doClose() Closes
                                             						this OutputStream. |
| protected void | doFlush() |
| protected void | doPrintln(String, int) |
| int | getCurrentFile() Returns
                                             						the CurrentFile property |
| java.lang.String | getFileExtension() Returns
                                             						the FileExtension property |
| java.lang.String | getFileNameBase() Returns
                                             						the FileNameBase property |
| java.lang.String | getHeader() Get the
                                             						header string that will be written at the beginning of each log file. |
| int | getMaxFiles() Returns the MaxFiles property |
| int | getMaxFileSize() Returns the MaxFileSize property |
| void | setHeader(String) Set
                                             						the constant header string that will be written at the beginning of every file, 
                                             						trace writing continues from the next line after the header is written. |

| Inherited member summary |
|---|
| Methods inherited from class BaseTraceWriter |
| close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString() |
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Constructors |
|  | OutputStreamTraceWriter(int, OutputStream) Default
                                                						constructor which is auto-flushing |
|  | OutputStreamTraceWriter(int, OutputStream, boolean) Create
                                                						an OutputStreamTraceWriter |
| Methods |
| protected void | doClose() |
| protected void | doFlush() |
| protected void | doPrintln(String, int) |
| java.io.OutputStream | getOutputStream() |

| Inherited member summary |
|---|
| Methods inherited from class BaseTraceWriter |
| close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString() |
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                                						notifyAll(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Constructors |
|  | SyslogTraceWriter(int, String) Default
                                             						SyslogTraceWriter with a max trace level of INFORMATIONAL |
|  | SyslogTraceWriter(int, String, int) SyslogTraceWriter with max trace level specified |
|  | SyslogTraceWriter(int, String, int[]) SyslogTraceWriter which takes an array of trace levels. |
| Methods |
| void | doClose() Closes
                                             						the socket |
| protected void | doPrintln(String, int) The
                                             						SyslogTraceWriter makes an exception to the println() method in that it places
                                             						a ’\0’ instead of a System specified line separator to terminate the message
                                             						packet. |
| static void | main(String[]) |

| Inherited member summary |
|---|
| Methods inherited from class BaseTraceWriter |
| close() , doClose() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) , toString() |
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Methods |
| static java.util.Enumeration | getModules() Returns
                                             						an enumeration of the TraceModules registered with this factory. |
| static TraceManager | registerModule(TraceModule) Returns
                                             						an instance of a TraceManager object. |
| static TraceManager | registerModule(TraceModule, String[], TraceWriterManager) Returns
                                             						an instance of a TraceManager object. |
| static TraceManager | registerModule(TraceModule, TraceWriterManager) Returns
                                             						an instance of a TraceManager object. |

| Inherited member summary |
|---|
| Methods inherited from class Object |
| clone(),  equals(Object),  finalize(),  getClass(),  hashCode(),  notify(), 
                                             						notifyAll(),  toString(),  wait(),  wait(),  wait() |

| Member summary |
|---|
| Fields |
| static int | ALERTS The
                                             						application will continue working on the tasks but all functions may not be
                                             						operational (one or more devices in the list are not accessible but others in
                                             						the list can be accessed) Syslog
                                             						severity level  =  1 |
| static
                                             						java.lang.String | ALERTS_TRACE_NAME String
                                             						descriptor for ALERTS trace level |
| static int | CRITICAL A
                                             						critical failure,  the application cannot accomplish the tasks required due to
                                             						this failure,  e.g.: the application cant open the database to read the device
                                             						list Syslog
                                             						severity level  =  2 |
| static
                                             						java.lang.String | CRITICAL_TRACE_NAME String
                                             						descriptor for CRITICAL trace level |
| static int | DEBUGGING Very
                                             						detailed information regarding errors or processing status that is only
                                             						generated when DEBUG mode has been enabled Syslog
                                             						severity level  =  7 |
| static java.lang. DEBUGGING_TRACE_NAME String | DEBUGGING_TRACE_NAME String
                                             						descriptor for the DEBUGGING trace level |
| static int | EMERGENCIES Emergency situation,  a system shutdown is necessary Syslog
                                             						severity level  =  0 |
| static
                                             						java.lang.String | EMERGENCIES_TRACE_NAME String
                                             						descriptor for EMERGENCIES trace level |
| static int | ERROR An
                                             						error condition of some kind has occurred and the user needs to understand the
                                             						nature of that failure Syslog
                                             						severity level  =  3 |
| static
                                             						java.lang.String | ERROR_TRACE_NAME String
                                             						descriptor for ERROR trace level |
| static int | HIGHEST_LEVEL The
                                             						highest trace level,  currently this is DEBUGGING with a trace level of 7 |
| static int | INFORMATIONAL Information of some form not relating to errors,  warnings,  audit,  or debug Syslog
                                             						severity level  = 6 |
| static
                                             						java.lang.String | INFORMATIONAL_TRACE_NAME String
                                             						descriptor for INFORMATIONAL trace level |
| static int | LOWEST_LEVEL The
                                             						lowest trace level,  currently this is EMERGENCIES with a trace level of 0 |
| static int | NOTIFICATION Notification denotes a normal but significant condition Syslog
                                             						severity level  =  5 |
| static
                                             						java.lang.String | NOTIFICATION_TRACE_NAME String descriptor for NOTIFICATION trace level |
| static int | WARNING Warning that a problem of some form exists but is not keeping the application
                                             						from completing its tasks Syslog
                                             						severity level  =  4 |
| static
                                             						java.lang.String | WARNING_TRACE_NAME String descriptor for WARNING trace level |
| Methods |
| java.lang.String | getName() Returns the name of this Trace object. |
| java.lang.String | getSubFacility() Returns the subFacility of trace |
| int | getType() Returns the type of trace. |
| boolean | isEnabled() Returns the state of this Trace object. |
| void | println(Object) Prints the string returned by the Object.toString() method and terminates the
                                             						line as defined by the system. |
| void | println(String) Prints a message in the same format as Trace.print() and terminates the line as
                                             						defined by the system. |
| void | println(String, Object) Prints the string returned by the Object.toString() method and terminates the
                                             						line as defined by the system. |
| void | println(String, String) Prints a message in the same format as Trace.print() and terminates the line as
                                             						defined by the system. |
| void | setDefaultMnemonic(String) Sets
                                             						a default mnemonic for all messages printed out to this trace. |

| Member summary |
|---|
| Methods |
| void | disable() Disables this condition for tracing. |
| void | enable() Enables
                                             						this condition for tracing. |

| Inherited member summary |
|---|
| Fields inherited from interface Trace |
| ALERTS , ALERTS_TRACE_NAME , CRITICAL , CRITICAL_TRACE_NAME , DEBUGGING , DEBUGGING_TRACE_NAME , EMERGENCIES , EMERGENCIES_TRACE_NAME , ERROR , ERROR_TRACE_NAME , HIGHEST_LEVEL , INFORMATIONAL , INFORMATIONAL_TRACE_NAME , LOWEST_LEVEL , NOTIFICATION , NOTIFICATION_TRACE_NAME , WARNING , WARNING_TRACE_NAME |
| Methods inherited from interface Trace |
| getName() , getSubFacility() , getType() , isEnabled() , println(Object) , println(String) , println(String, Object) , println(String, String) , setDefaultMnemonic(String) |

| Inherited Member summary |
|---|
| Fields inherited from interface Trace |
| ALERTS , ALERTS_TRACE_NAME , CRITICAL , CRITICAL_TRACE_NAME , DEBUGGING , DEBUGGING_TRACE_NAME , EMERGENCIES , EMERGENCIES_TRACE_NAME , ERROR , ERROR_TRACE_NAME , HIGHEST_LEVEL , INFORMATIONAL , INFORMATIONAL_TRACE_NAME , LOWEST_LEVEL , NOTIFICATION , NOTIFICATION_TRACE_NAME , WARNING , WARNING_TRACE_NAME |
| Methods inherited from interface Trace |
| getName() , getSubFacility() , getType() , isEnabled() , println(Object) , println(String) , println(String, Object) , println(String, String) , setDefaultMnemonic(String) |

| Member summary |
|---|
| Methods |
| void | addSubFacilities(String[]) Sets a
                                             						set of subFacilities for this TraceManager/Facility. |
| void | addSubFacility(String) Adds a
                                             						single subFacility for this TraceManager/Facility. |
| void | disableAll() Disables tracing for all Trace objects managed by this TraceManager. |
| void | disableTimeStamp() Disables prefixing a time stamp for every message printed by this TraceManager. |
| void | enableAll() Enables
                                             						tracing for all Trace objects managed by this TraceManager. |
| void | enableTimeStamp() Enables
                                             						prefixing a time stamp for every message printed by this TraceManager. |
| ConditionalTrace | getConditionalTrace(int) Creates
                                             						a new ConditionalTrace object or obtains an existing ConditionalTrace object
                                             						for this condition. |
| ConditionalTrace | getConditionalTrace(String, int) Creates
                                             						a new ConditionalTrace object or obtains an existing ConditionalTrace object
                                             						for this condition and subFacility |
| java.lang.String | getName() Returns
                                             						the Facility name for this TraceManager. |
| java.lang.String[] | getSubFacilities() Returns
                                             						the subFacility names for this TraceManager/Facility. |
| java.util.Enumeration | getTraces() Returns
                                             						an enumeration of the Trace objects managed by this TraceManager. |
| TraceWriterManager | getTraceWriterManager() Returns
                                             						the TraceWriter used by this TraceManager. |
| UnconditionalTrace | getUnconditionalTrace(int) Creates
                                             						a new UnconditionalTrace object or obtains an existing UnconditionalTrace
                                             						object for this condition. |
| UnconditionalTrace | getUnconditionalTrace(String, int) Creates
                                             						a new UnconditionalTrace object or obtains an existing UnconditionalTrace
                                             						object for this condition and subFacility |
| void | removeTrace(Trace) Removes
                                             						a Trace object given an object. |
| void | setSubFacilities(String[]) Sets a
                                             						set of subFacilities for this TraceManager/Facility. |
| void | setSubFacility(String) Adds a
                                             						single subFacility for this TraceManager/Facility. |
| void | setTraceWriterManager(TraceWriterManager) Sets
                                             						the TraceWriter to be used by this TraceManager. |

| Member summary |
|---|
| Methods |
| TraceManager | getTraceManager() Returns
                                             						the TraceManager that an object is using for tracing. |
| java.lang.String | getTraceModuleName() Returns
                                             						the module name. |

| Member summary |
|---|
| Methods |
| void | close() Releases any resources associated by this TraceWriter . |
| void | flush() Forces output of any messages that
                                             						have been printed using the println method |
| java.lang.String | getDescription() |
| boolean | getEnabled() Returns
                                             						whether the println method will print anything or not. |
| java.lang.String | getName() |
| int[] | getTraceLevels() |
| void | println(String, int) Prints
                                             						the specified string followed by a carriage return The concrete TraceWriter
                                             						class will use the severity to block out messages from a particular stream. |
| void | setTraceLevels(int[]) set the
                                             						trace levels that will be traced by this TraceWriter |

| Member summary |
|---|
| Methods |
| void | addTraceWriter(TraceWriter) Add
                                             						another TraceWriter to the array |
| TraceWriter[] | getTraceWriters() |
| void | removeTraceWriter(TraceWriter) Remove
                                             						the TraceWriter from the array in the manager |
| void | setTraceWriters(TraceWriter[]) Implementations can use this method to override or enhance the provided
                                             						TraceWriters |

| Inherited member summary |
|---|
| Methods inherited from interface TraceWriter |
| close() , flush() , getDescription() , getEnabled() , getName() , getTraceLevels() , println(String, int) , setTraceLevels(int[]) |

| Note | Methods
                                          			 inherited from class java.lang.Object are clone,  equals,  finalize,  getClass, 
                                          			 hashCode,  notify,  notifyAll,  toString,  wait,  wait,  wait. |
|---|---|