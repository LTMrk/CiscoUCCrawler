---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuni-api-b-cuc-cuni-api-b-cuc-cuni-api-chapter-01-html-824a23b4ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUNI_API/b_CUC_CUNI_API/b_CUC_CUNI_API_chapter_01.html
retrieved_at: 2026-08-21T01:00:44.108165+00:00
---

Cisco Unity Connection Notification Interface (CUNI) API

# Cisco Unity Connection Notification Interface (CUNI) API

Updated: December 27, 2018

Chapter: Cisco Unity
	 Connection Notification Interface (CUNI) API -- CUNI Event Schema

## Chapter: Cisco Unity
	 Connection Notification Interface (CUNI) API -- CUNI Event Schema

- Cisco Unity                              	 Connection Notification Interface (CUNI) API -- CUNI Event Schema

- Schema Example

# Cisco Unity
                     	 Connection Notification Interface (CUNI) API -- CUNI Event Schema

## Schema Example

```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns="\[http://www.cisco.com"\] elementFormDefault="qualified" targetNamespace="\[http://www.cisco.com"\] xmlns:xs="\[http://www.w3.org/2001/XMLSchema">\]
<xs:simpleType name="priorityType">
<xs:restriction base="xs:string">
<xs:enumeration value="Low-Priority" />
<xs:enumeration value="Normal-Priority" />
<xs:enumeration value="Urgent" />
<xs:enumeration value="Unknown-Priority" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="eventType">
<xs:restriction base="xs:string">
<xs:enumeration value="MESSAGE_INFO" />
<xs:enumeration value="NEW_MESSAGE" />
<xs:enumeration value="SAVED_MESSAGE" />
<xs:enumeration value="UNREAD_MESSAGE" />
<xs:enumeration value="DELETED_MESSAGE" />
<xs:enumeration value="FAILOVER" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="messageType">
<xs:restriction base="xs:string">
<xs:enumeration value="Voice" />
<xs:enumeration value="NDR" />
<xs:enumeration value="DR" />
<xs:enumeration value="RR" />
<xs:enumeration value="Fax" />
<xs:enumeration value="Text" />
<xs:enumeration value="UnknownType" />
</xs:restriction>
</xs:simpleType>
<xs:complexType name="messageInfoType">
<xs:attribute name="messageId" type="xs:string" />
<xs:attribute name="receiveTime" type="xs:string" />
<xs:attribute name="msgType" type="messageType" />
<xs:attribute name="uid" type="xs:integer" />
<xs:attribute name="priority" type="priorityType" />
<xs:attribute name="sender" type="xs:string" />
<xs:attribute name="callerAni" type="xs:string" />
</xs:complexType>
<xs:element name="messageEvent">
<xs:complexType>
<xs:sequence minOccurs="1" maxOccurs="unbounded">
<xs:element name="messageInfo" type="messageInfoType" />
</xs:sequence>
<xs:attribute name="subscriptionId" type="xs:string" />
<xs:attribute name="eventType" type="eventType" />
<xs:attribute name="eventTime" type="xs:string" />
<xs:attribute name="mailboxId" type="xs:string" />
<xs:attribute name="displayName" type="xs:string" />
<xs:attribute name="USN" type="xs:integer" />
</xs:complexType>
</xs:element>
</xs:schema>
```