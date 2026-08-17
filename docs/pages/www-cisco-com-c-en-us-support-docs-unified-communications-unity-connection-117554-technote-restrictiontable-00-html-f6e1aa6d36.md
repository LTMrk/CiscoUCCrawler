---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-117554-technote-restrictiontable-00-html-f6e1aa6d36
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/117554-technote-restrictiontable-00.html
retrieved_at: 2026-08-17T03:56:54.851135+00:00
---

Unity Connection: Restriction Tables Effect on 'Transfer to Alternate Contact Number' Feature

# Unity Connection: Restriction Tables Effect on 'Transfer to Alternate Contact Number' Feature

Updated: March 27, 2014

Document ID: 117554

Contents

## Contents

## Introduction

This document describes how the Restriction Table affects the transfer of calls when the " Transfer to Alternate Contact Number " option is used under Caller Input of Users / Call Handlers. This feature is known as One-Key Dialing as it enables a single key to represent a Number.

For more information on this feature, refer to the Offering One-Key Dialing During Call Handler Greetings section of the Managing Call Handlers in Cisco Unity Connection document. This document also provides information on how to query the database in order to extract data on the configured Alternate Contact Numbers.

### Design

The administrator enables this option via the Cisco Unity Connection Administration page.The administrator can define any number irrespective of the restrictions defined in the restriction table.

The user can modify/disable the Alternate Extension via the Conversation in Telephone User Interface (TUI). When the user modifies the number, it is checked against the Blocked Pattern in the Restriction Table associated with the Class of Service of the user. If a Blocked Number is entered, an error prompt is played out to the user indicating the number is blocked.

For more information on how users access this feature, refer to the Managing Your Alternate Contact Numbers chapter of the User Guide for the Cisco Unity Connection Phone Interface Guide.

Note : The user is able to hear/modify the Alternate Extension Option via TUI only when the administator enables this option via the Cisco Unity Connection Administration page.

### Limitation

After the number is defined by the user, it is not checked against the restriction table when the actual call transfer takes place. The check only happens when the number is defined by the user. Modifications to the Restriction Table in order to block the number defined by the user will still allow the call be transferred as the number is already defined.

The database can be queried to get the Alternate Contact Number configured for the User/Call Handler.

### CLI Queries

#### To get the available Restriction Tables

```
admin:run cuc dbquery unitydirdb select displayname from vw_restrictiontable displayname
---------------------------------------------------------
Default Transfer
Default Outdial
Default Fax
Default System Transfer
User-Defined and Automatically-Added Alternate Extensions
```

#### To get the Restrictions defined in the "Default Transfer" Restriction Table

```
admin:run cuc dbquery unitydirdb select sequencenumber, blocked, numberpattern from 
vw_restrictionpattern where restrictiontableobjectid in (select objectid from vw_restrictiontable 
where displayname='Default Transfer') order by sequencenumber sequencenumber  blocked  numberpattern  
--------------  -------  -------------- 
0               1        1212  
1               1        9???????  
2               1        91???????*  
3               1        9011???????*  
4               1        9???????????*  
5               1        900  
6               1        *
```

Important notes about Restriction Table:

sequencenumber in Restriction Table specifies the order in which Cisco Unity Connection will apply each call pattern. blocked Values in Restriction Tables indicates:

- 0: Permit use of dial strings matching the pattern

- 1: Do not permit use of dial strings matching the pattern

numberpattern in Restriction Table provides specifiic numbers or patterns of numbers (including external and long-distance access codes) that can be permitted or restricted. Uses digits 0 through 9 plus these special characters:

- * Matches zero or more digits

- ? Matches exactly one digit. Each ? serves as a placeholder for one digit.

- # Corresponds to the # key on the phone

For example, To screen out all of the phone numbers that start with 206 but are longer than 7 digits, enter 9206?????* for the pattern (and set "Blocked" == true).

U.S. Long Distance calls are blocked as defined by the Restriction Table.

#### To get All Users configured for Long Distance calls

```
admin:run cuc dbquery unitydirdb select gu.alias, gu.dtmfaccessid, me.touchtonekey, acn.transfernumber 
from vw_alternatecontactnumber as acn inner join vw_menuentry as me on 
acn.menuentryobjectid=me.objectid and me.action='7' inner join vw_callhandler as ch on 
me.callhandlerobjectid=ch.objectid inner join vw_globaluser as gu on 
ch.recipient_globaluserobjectid=gu.objectid and ch.isprimary='1' and acn.transfernumber like '91%' alias    dtmfaccessid  touchtonekey  transfernumber
-------  ------------  ------------  --------------
Anirudh  1008          9             914084343219
```

Note : like '91%' means any number that begins with 91. For international calls, like '9011%' can be used. In order to check a specific number, replace acn.transfernumber like '91%' with acn.transfernumber='914084343219' touchtonekey is the Caller Input Option

Note: In this example the long distance number is defined for the user by the Administrator. As mentioned earlier Restriction tables are not checked when Administrator defines the number.

#### To get All Call Handlers configured for Long Distance calls

```
admin:run cuc dbquery unitydirdb select ch.displayname, ch.dtmfaccessid, me.touchtonekey, 
acn.transfernumber from vw_callhandler as ch inner join vw_menuentry as me on 
ch.objectid=me.callhandlerobjectid and ch.isprimary='0' and me.action='7' inner join 
vw_alternatecontactnumber as acn on acn.menuentryobjectid=me.objectid and acn.transfernumber like '91%'
No records found
```

#### To get All Users with "Transfer to Alternate Contact Number" configured

```
admin:run cuc dbquery unitydirdb select gu.alias, gu.dtmfaccessid, me.touchtonekey, acn.transfernumber 
from vw_alternatecontactnumber as acn inner join vw_menuentry as me on 
acn.menuentryobjectid=me.objectid and me.action='7' inner join vw_callhandler as ch on 
me.callhandlerobjectid=ch.objectid inner join vw_globaluser as gu on 
ch.recipient_globaluserobjectid=gu.objectid and ch.isprimary='1' alias         dtmfaccessid  touchtonekey  transfernumber 
------------- ------------  ------------  --------------
Anirudh       1008          9            914084343219
AMavilakandy  8023          1             1212
```

Note : In this example 1212 was blocked in the restriction table after the user defined this as an alternate contact number. 914084343219 was defined by the Administrator. Hence for both these numbers calls will be transferred even though the Restriction Table blocks it. All active Alternate Contact numbers will be displayed with this query.

#### To get All Call Handlers with "Transfer to Alternate Contact Number" configured

```
admin:run cuc dbquery unitydirdb select ch.displayname, ch.dtmfaccessid, me.touchtonekey, 
acn.transfernumber from vw_callhandler as ch inner join vw_menuentry as me on 
ch.objectid=me.callhandlerobjectid and ch.isprimary='0' and me.action='7' inner join 
vw_alternatecontactnumber as acn on acn.menuentryobjectid=me.objectid displayname  dtmfaccessid  touchtonekey transfernumber
-----------  ------------- ------------  --------------
APAC         56565           2           2226
APAC         56565           3           2226
EU           null            1           2226
EU           null            2           2226
```

### Revision History

1.0

27-Mar-2014

Initial Release

### Contributed by Cisco Engineers

Anirudh Mavilakandy

Cisco TAC Engineer.

### This Document Applies to These Products

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Mar-2014 | Initial Release |