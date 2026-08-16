---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-pimg-b-12xcucintpimg-b-12xcucintpimg-append-9d459fec5e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/pimg/b_12xcucintpimg/b_12xcucintpimg_appendix_010101.html
retrieved_at: 2026-08-16T18:45:20.817538+00:00
---

PIMG Integration Guide for Cisco Unity Connection Release 12.X

# PIMG Integration Guide for Cisco Unity Connection Release 12.X

Updated: August 7, 2017

Chapter: Application Note
	 for the Nortel SL-100 Serial SMDI TIMG Integration

## Chapter: Application Note
	 for the Nortel SL-100 Serial SMDI TIMG Integration

# Application Note
                     	 for the Nortel SL-100 Serial SMDI TIMG Integration

This is an application note for
                        		programming the Nortel SL-100 phone system for a serial SMDI integration with
                        		Cisco Unity Connection using TIMG units. For instructions on setting up analog
                        		PIMG units and creating the serial PIMG integration in Unity Connection, see
                        		the Setting Up a Serial (SMDI, MCI, or MD-110) PIMG Integration with Cisco Unity Connection chapter.

Application Note for the Nortel SL-100 Serial SMDI TIMG Integration

## Introduction

This is
                           		an application note for programming the Nortel SL-100 phone system for a serial
                           		SMDI integration with Cisco Unity Connection using TIMG units. For instructions
                           		on setting up analog PIMG units and creating the serial PIMG integration in
                           		Unity Connection, see the " Setting
                              		  Up a Serial (SMDI, MCI, or MD-110) PIMG Integration " chapter.

## Network
                        	 Topology

Figure C-1 shows the required connections for a serial SMDI
                           		integration using TIMG units.

For more information about this integration, see the
                           		chapter Introduction .

## Requirements

The phone system was as follows:

Nortel SL-100.

Software version SE-06 or later.

Line Side T1 Card (NT5D11 or equivalent) to terminate the T1 line.

## Programming Nortel SL-100 Phone System for Serial Integration

The following programming instructions are provided as an example of a functioning integration. The specific programming for
                              your phone system may vary depending on its configuration.

In programming the phone system, do not send calls to voice messaging ports in Unity Connection that cannot answer calls (voice
                                          messaging ports that are not set to Answer Calls). For example, if a voice messaging port is set only to Perform Message Notification,
                                          do not send calls to it.

On the MAP terminal, enter table mpc and press Enter .

Enter add and press Enter .

On Table MPC, enter the following settings.

Field

Setting

MPCNO

Enter the MPC number used for SMDI.

MPCIOC

Enter the number associated with the MPC (SMDI) card.

IOCCCT

Enter the slot position on the IOC shelf multiplied by 4, from 0 to 32.

EQ

Enter the NT product engineering code for the MPC card in the format 1X89zz or FX30zz, where zz are the two letters at the
                                          end of the product code.

DLDFILE

In the format MPCAxxyy, enter the name of the 8-character download file for SMDI and MPCA.

Enter table mpclink and press Enter .

Enter add and press Enter .

On Table MPCLINK, enter the following settings.

Field

Subfield

Setting

LINKKEY

MPCNO

Enter the MPC number used for SMDI (the same number entered in Table MPC).

LINKNO

Enter the MPC link number for SMDI application with ASYNC protocol.

LINKALM

Enter Y to activate the MPCLINK alarm for system busy (SYSB) MPC links. Enter N if you do not want to activate the MPCLINK alarm for system busy (SYSB) MPC links.

If you enter N, the system does not generate MPC908 (MPC link state transition) logs.

PROTOCOL

Enter ASYNC .

LINKNABL

Enter 765 .

PARM

Enter APLDEFN .

ADEFN

Enter SMDI .

PARM

Enter BAUDRATE .

RATE

Enter B9600 .

PARM

Enter PARITY .

PRTY

Enter EVEN .

PARM

The following are among the optional parameters: L1IDLY, L2IDLY, LNKDOWN. If you enter a parameter, you are then prompted
                                          to enter a value for it.

L1IDLY and L2IDLY timers can be used in offices with heavy SMDI/VMS traffic to shorten the amount of time the MPC can delay
                                          sending an MWI to the switch. (The default is 3 seconds.)

The LNKDOWN timer adjusts the length of time the switch takes to recognize LINK failure and sets the LINK to SYSB. (The default
                                          is 2 seconds.)

CHARBITS

Enter BIT7 .

Enter table sllnkdev and press Enter .

Enter add and press Enter .

On Table SLLNKDEV, enter the following settings.

Field

Setting

DEVNAME

Enter a unique device name.

DEVICE

Enter 1X89 .

MPCNO

Enter the value MPC number that was specified in Table MPC.

LINKNO

Enter the value for the MPC link number that was specified in Table MPCLINK.

XLATION

Enter NONE .

PROTOCOL

Enter NONE .

DIRECTION

Enter INOUTLK .

XFER

Enter SMDIDATA .

OPTION

Enter NUMOFDIGS .

NUMDIGS

Enter the number of digits sent by the phone system to the voice messaging system through the SMDI link.

The entry value selected should match the dialing plan configured on the phone system.

OPTION

Enter CGNADDRDN .

OPTION

Enter $ .

Enter table ofrt and press Enter .

You use Table OFRT to set up a treatment for unanswered calls. The following example shows settings for routing unanswered
                              calls back to the voice messaging system.

Enter add and press Enter .

On Table OFRT, enter the following settings.

Field

Setting

RTE

If the record is the first in the route list, enter the route reference number assigned to the route list. Otherwise, leave
                                          this field blank.

RTESEL

Enter the route selector.

SNPA

Enter the serving NPA (area code) of the DN.

TYPCALL

Enter the type of call:

DD

NP

OA

ORIGSCRE

Enter LCL (for local) or NLCL (for non-local).

REPLDIGS

Enter up to 11 replace digits.

CANCNORC

Enter Y or N to indicate whether to cancel normal change.

BILLCODE

Enter the billing code. If there is no billing number, enter N .

Enter table digcol and press Enter .

You use Table DIGCOL to set up the action that the line module must take with the first digit that is dialed.

Enter add and press Enter .

On Table DIGCOL, enter the following settings.

Field

Subfield

Setting

DGKEY

DATNAME

Enter the character assigned to the block of data in Table DIGCOL.

DIGIT

Enter a numeric value from 0–9, STAR (*), or OCT (#) to specify the digit that is applicable to the record.

DGDATA

DGCOLSEL

Enter COL for the collection of more digits.

COLDATA

TMODE

Enter S for short timing mode.

NUMDIGS

Number of digits. If the TMODE value is S, specify the number of digits for which short timing is required after the receipt
                                          of each digit. The number of digits specified, which does not include the initial digit, must be no greater than three for
                                          short timing.

Enter table ucdgroup and press Enter .

You use Table UCDGRP to set up the UCD group.

The UCD group must have a unique primary DN.

Enter add and press Enter .

On Table UCDGRP, enter the following settings.

Field

Setting

UCDNAME

This is the name of the UCD group. It can be up to 16 characters in length. The first eight characters must be unique.

ACD

Enter N .

CUSTGRP

Name of the customer group to which the UCD group belongs.

UCDRNGTH

Ringing threshold, in one-second intervals, after which an unanswered call to a UCD agent is forwarded to the route specified
                                          in the THROUT field. The range is 0–63.

TABNAME

Enter OFRT .

INDEX

Enter the number assigned to the route list in Table OFRT (1–1023).

TABNAME

Enter OFRT for the table to which translations are routed.

INDEX

Enter the number assigned to the route list in Table OFRT (1–1023).

PRIOPRO

Enter Maximum time, in seconds, a call can wait in a UCD group (0–255).

MAXPOS

Enter the maximum number of UCD agent positions that can be active at one time. This number should be the number of ports
                                          on the all TIMG units that are connected to the phone system.

DBG

Delayed billing. Enter Y if billing starts when the call is answered by a UCD agent. Enter N if billing starts when the caller receives a recorded announcement.

DEFPRIO

Enter 0 .

RLSCNT

Enter 0 .

MAXWAIT

Enter the maximum time, in seconds, that a call waits in the incoming call queue before being answered (0–1800).

MAXCQSIZ

Enter the maximum number of calls that can be in the incoming queue waiting for an idle channel (0–511).

OPTION

Enter UCD_SMDI .

SMDI_LINK

Enter the terminal designation defined in Table SLLNKDEV.

SMDI_ DESK_NO

Enter the message desk number (1–63). If you have more than one UCD group, one of them must be set to 63. We recommend that
                                          the first UCD group on a data link be set to 63. The second is set to 62, and so on.

If CRR (Call Request Retrieval) is used, all requests are made to the UCD group with SMDI_DSK_NO = 63.

Enter table dnroute and press Enter .

You use Table DNROUTE to set up the UCD group.

The UCD group must have a unique primary DN.

Enter add and press Enter .

On Table DNROUTE, enter the following settings.

Field

Subfield

Setting

DNNM

AREACODE

Enter the DN for the UCD group specified as the UCDGRP.

The UCD DN must be a dialable number from an agent on the phone system so that dialing plans and translation tables do not
                                                      conflict.

OFCCODE

STNCODE

DN_SEL

Enter FEAT .

FEATURE

Enter UCD .

UCDGRP

Enter the value for the UCDNAME field that is defined in Table UCDGROUP.

DNTYPE

Enter PRIM .

TOLLPRIO

Enter 0 .

Enter table lninv and press Enter .

You use Table LNINV to assign card slots on the line or remote line module.

Enter add and press Enter .

On Table LNINV, enter the following settings.

Field

Setting

LEN

Enter the line equipment number of the card slot.

CARDCODE

Enter 5d11ae .

PADGRP

Enter the name of the appropriate pad group that appears in the PADDATA table.

STATUS

Enter WORKING .

GND

Enter Y .

BNV

Enter NL .

MNO

Enter Y .

CARDTYPE

Enter NIL .

Enter servord and press Enter .

You can add agents to the UCD group by entering the following inputs at the prompts.

Prompt

Input

Description

SO:

NEW

SONUMBER:

Press Enter .

When to invoke this service. Pressing Enter starts the service at the current date and time.

DN:

The Directory Number of the line. Use ten-digit DNs.

LCC_ACC:

IBN

The line class code of service.

GROUP:

The name of the IBN customer group to which the line belongs. For example, covm.

SUBGRP:

The subgroup number. For example, 0.

NCOS:

The network class of service. For example, 1.

SNPA:

The serving NPA (area code) of the DN.

LEN_OR_LT D:

The line equipment number of the line. For example, 4 0 1 0 (separated by spaces).

OPTION:

COD

The cut-off on disconnect.

OPTION:

UCD

Uniform call distribution.

OPTION:

DGT

Digitone.

OPTION:

3WC

Three-way calling.

OPTION:

CXR

Call Transfer.

CXFERTYP:

CTALL

Call Transfer Type. CTALL = transfer all calls.

CXRRCL:

N

Call Transfer Recall.

METHOD:

STD

Method of Call Transfer: Std = Std Call Transfer method.

OPTION:

SMDI

Simplified message desk interface.

LINENO:

The UCD terminal number. This is the line number associated with the SMDI channel. This parameter must be unique for each
                                          agent in the associated UCDGRP.

UCDGRP:

The UCDNAME from the UCDGRP table. This is the UCD group to which you are adding the agent.

AUTO_LOG:

Y

Autologon capability required.

OPTION:

$

The data you have entered appears.

Y

Enter Y .

Enter servord and press Enter .

You can add a pilot number (UCD group DN) for the ports on the TIMG units by entering the following inputs at the prompts.

Prompt

Input

Description

SO:

NEW

SONUMBER:

Press Enter.

When to invoke this service. Pressing Enter starts the service at the current date and time.

DN:

The directory number of the line. This is the DN that you enter in the SDN table.

LCC:

IBN

The line class code of service.

GROUP:

The name of the IBN customer group to which the line belongs.

SUBGRP:

The subgroup number.

NCOS:

The network class of service.

SNPA:

Serving NPA (area code) of the DN.

LEN:

Line equipment number of the line. For example, 4 0 1 0.

OPTION:

cfb

Call Forward Busy.

This input is optional.

CFBCNTL:

N

Normal assignment for CFB.

This input is optional.

CFBDN:

The primary UCD DN.

This input is optional.

OPTION:

CFF

Call Forward Fixed.

CFFDN:

The primary UCD DN.

OPTION:

CFU

Call Forward Universal.

OVRDACR:

N

Override Automatic Callback.

OPTION:

$

The data you entered appears.

Y

Enter Y to confirm the data.

Connect a phone to the line.

Pick up the handset.

Dial the call forward activation code followed by the pilot number (UCD DN). For example, dial *80 5551234.

If you do not know this code, look it up in Table IBNXLA. The code is in the CFWP field.

Confirm that you hear the confirmation tone, which indicates that the line has been forwarded.

If the phone system is restarted, you must repeat Step 27. through Step 30. for each line DN that CFUs to the UCD group.

Enter table ibnxla and press Enter .

You use Table IBNXLA to set up and message waiting indicators (MWIs).

Enter add and press Enter .

On Table IBNXLA, enter the following settings.

Field

Subfield

Setting

KEY

XLANAME

Enter the name of the translator, 1–8 characters, for the MWI feature.

DGLIDX

Enter the access code for the MWI feature.

RESULT

TRSEL

Enter FEAT .

ACR

Enter N .

SMDR

Enter N .

FEATURE

Enter the following features:

CRA CRR CRDS CRDA UCDD UCDA CFWP CFWC

| Caution | In programming the phone system, do not send calls to voice messaging ports in Unity Connection that cannot answer calls (voice
                                          messaging ports that are not set to Answer Calls). For example, if a voice messaging port is set only to Perform Message Notification,
                                          do not send calls to it. On the MAP terminal, enter table mpc and press Enter . Enter add and press Enter . On Table MPC, enter the following settings. |
|---|---|

| Field | Setting |
|---|---|
| MPCNO | Enter the MPC number used for SMDI. |
| MPCIOC | Enter the number associated with the MPC (SMDI) card. |
| IOCCCT | Enter the slot position on the IOC shelf multiplied by 4, from 0 to 32. |
| EQ | Enter the NT product engineering code for the MPC card in the format 1X89zz or FX30zz, where zz are the two letters at the
                                          end of the product code. |
| DLDFILE | In the format MPCAxxyy, enter the name of the 8-character download file for SMDI and MPCA. |

| Field | Subfield | Setting |
|---|---|---|
| LINKKEY | MPCNO | Enter the MPC number used for SMDI (the same number entered in Table MPC). |
| LINKNO | Enter the MPC link number for SMDI application with ASYNC protocol. |
| LINKALM |  | Enter Y to activate the MPCLINK alarm for system busy (SYSB) MPC links. Enter N if you do not want to activate the MPCLINK alarm for system busy (SYSB) MPC links. Note If you enter N, the system does not generate MPC908 (MPC link state transition) logs. | Note | If you enter N, the system does not generate MPC908 (MPC link state transition) logs. |
| Note | If you enter N, the system does not generate MPC908 (MPC link state transition) logs. |
| PROTOCOL |  | Enter ASYNC . |
| LINKNABL |  | Enter 765 . |
| PARM |  | Enter APLDEFN . |
| ADEFN |  | Enter SMDI . |
| PARM |  | Enter BAUDRATE . |
| RATE |  | Enter B9600 . |
| PARM |  | Enter PARITY . |
| PRTY |  | Enter EVEN . |
| PARM |  | The following are among the optional parameters: L1IDLY, L2IDLY, LNKDOWN. If you enter a parameter, you are then prompted
                                          to enter a value for it. L1IDLY and L2IDLY timers can be used in offices with heavy SMDI/VMS traffic to shorten the amount of time the MPC can delay
                                          sending an MWI to the switch. (The default is 3 seconds.) The LNKDOWN timer adjusts the length of time the switch takes to recognize LINK failure and sets the LINK to SYSB. (The default
                                          is 2 seconds.) |
| CHARBITS |  | Enter BIT7 . |
|  |  |  |
|  |  |  |

| Note | If you enter N, the system does not generate MPC908 (MPC link state transition) logs. |
|---|---|

| Field | Setting |
|---|---|
| DEVNAME | Enter a unique device name. |
| DEVICE | Enter 1X89 . |
| MPCNO | Enter the value MPC number that was specified in Table MPC. |
| LINKNO | Enter the value for the MPC link number that was specified in Table MPCLINK. |
| XLATION | Enter NONE . |
| PROTOCOL | Enter NONE . |
| DIRECTION | Enter INOUTLK . |
| XFER | Enter SMDIDATA . |
| OPTION | Enter NUMOFDIGS . |
| NUMDIGS | Enter the number of digits sent by the phone system to the voice messaging system through the SMDI link. Note The entry value selected should match the dialing plan configured on the phone system. | Note | The entry value selected should match the dialing plan configured on the phone system. |
| Note | The entry value selected should match the dialing plan configured on the phone system. |
| OPTION | Enter CGNADDRDN . |
| OPTION | Enter $ . |

| Note | The entry value selected should match the dialing plan configured on the phone system. |
|---|---|

| Field | Setting |
|---|---|
| RTE | If the record is the first in the route list, enter the route reference number assigned to the route list. Otherwise, leave
                                          this field blank. |
| RTESEL | Enter the route selector. |
| SNPA | Enter the serving NPA (area code) of the DN. |
| TYPCALL | Enter the type of call: DD NP OA |
| ORIGSCRE | Enter LCL (for local) or NLCL (for non-local). |
| REPLDIGS | Enter up to 11 replace digits. |
| CANCNORC | Enter Y or N to indicate whether to cancel normal change. |
| BILLCODE | Enter the billing code. If there is no billing number, enter N . |

| Field | Subfield | Setting |
|---|---|---|
| DGKEY | DATNAME | Enter the character assigned to the block of data in Table DIGCOL. |
| DIGIT | Enter a numeric value from 0–9, STAR (*), or OCT (#) to specify the digit that is applicable to the record. |
| DGDATA | DGCOLSEL | Enter COL for the collection of more digits. |
| COLDATA | TMODE | Enter S for short timing mode. |
| NUMDIGS | Number of digits. If the TMODE value is S, specify the number of digits for which short timing is required after the receipt
                                          of each digit. The number of digits specified, which does not include the initial digit, must be no greater than three for
                                          short timing. |

| Note | The UCD group must have a unique primary DN. Enter add and press Enter . On Table UCDGRP, enter the following settings. |
|---|---|

| Field | Setting |
|---|---|
| UCDNAME | This is the name of the UCD group. It can be up to 16 characters in length. The first eight characters must be unique. |
| ACD | Enter N . |
| CUSTGRP | Name of the customer group to which the UCD group belongs. |
| UCDRNGTH | Ringing threshold, in one-second intervals, after which an unanswered call to a UCD agent is forwarded to the route specified
                                          in the THROUT field. The range is 0–63. |
| TABNAME | Enter OFRT . |
| INDEX | Enter the number assigned to the route list in Table OFRT (1–1023). |
| TABNAME | Enter OFRT for the table to which translations are routed. |
| INDEX | Enter the number assigned to the route list in Table OFRT (1–1023). |
| PRIOPRO | Enter Maximum time, in seconds, a call can wait in a UCD group (0–255). |
| MAXPOS | Enter the maximum number of UCD agent positions that can be active at one time. This number should be the number of ports
                                          on the all TIMG units that are connected to the phone system. |
| DBG | Delayed billing. Enter Y if billing starts when the call is answered by a UCD agent. Enter N if billing starts when the caller receives a recorded announcement. |
| DEFPRIO | Enter 0 . |
| RLSCNT | Enter 0 . |
| MAXWAIT | Enter the maximum time, in seconds, that a call waits in the incoming call queue before being answered (0–1800). |
| MAXCQSIZ | Enter the maximum number of calls that can be in the incoming queue waiting for an idle channel (0–511). |
| OPTION | Enter UCD_SMDI . |
| SMDI_LINK | Enter the terminal designation defined in Table SLLNKDEV. |
| SMDI_ DESK_NO | Enter the message desk number (1–63). If you have more than one UCD group, one of them must be set to 63. We recommend that
                                          the first UCD group on a data link be set to 63. The second is set to 62, and so on. Note If CRR (Call Request Retrieval) is used, all requests are made to the UCD group with SMDI_DSK_NO = 63. | Note | If CRR (Call Request Retrieval) is used, all requests are made to the UCD group with SMDI_DSK_NO = 63. |
| Note | If CRR (Call Request Retrieval) is used, all requests are made to the UCD group with SMDI_DSK_NO = 63. |

| Note | If CRR (Call Request Retrieval) is used, all requests are made to the UCD group with SMDI_DSK_NO = 63. |
|---|---|

| Note | The UCD group must have a unique primary DN. Enter add and press Enter . On Table DNROUTE, enter the following settings. |
|---|---|

| Field | Subfield | Setting |
|---|---|---|
| DNNM | AREACODE | Enter the DN for the UCD group specified as the UCDGRP. Note The UCD DN must be a dialable number from an agent on the phone system so that dialing plans and translation tables do not
                                                      conflict. | Note | The UCD DN must be a dialable number from an agent on the phone system so that dialing plans and translation tables do not
                                                      conflict. |
| Note | The UCD DN must be a dialable number from an agent on the phone system so that dialing plans and translation tables do not
                                                      conflict. |
| OFCCODE |
| STNCODE |
| DN_SEL |  | Enter FEAT . |
| FEATURE |  | Enter UCD . |
| UCDGRP |  | Enter the value for the UCDNAME field that is defined in Table UCDGROUP. |
| DNTYPE |  | Enter PRIM . |
| TOLLPRIO |  | Enter 0 . |

| Note | The UCD DN must be a dialable number from an agent on the phone system so that dialing plans and translation tables do not
                                                      conflict. |
|---|---|

| Field | Setting |
|---|---|
| LEN | Enter the line equipment number of the card slot. |
| CARDCODE | Enter 5d11ae . |
| PADGRP | Enter the name of the appropriate pad group that appears in the PADDATA table. |
| STATUS | Enter WORKING . |
| GND | Enter Y . |
| BNV | Enter NL . |
| MNO | Enter Y . |
| CARDTYPE | Enter NIL . |

| Prompt | Input | Description |
|---|---|---|
| SO: | NEW |  |
| SONUMBER: | Press Enter . | When to invoke this service. Pressing Enter starts the service at the current date and time. |
| DN: |  | The Directory Number of the line. Use ten-digit DNs. |
| LCC_ACC: | IBN | The line class code of service. |
| GROUP: |  | The name of the IBN customer group to which the line belongs. For example, covm. |
| SUBGRP: |  | The subgroup number. For example, 0. |
| NCOS: |  | The network class of service. For example, 1. |
| SNPA: |  | The serving NPA (area code) of the DN. |
| LEN_OR_LT D: |  | The line equipment number of the line. For example, 4 0 1 0 (separated by spaces). |
| OPTION: | COD | The cut-off on disconnect. |
| OPTION: | UCD | Uniform call distribution. |
| OPTION: | DGT | Digitone. |
| OPTION: | 3WC | Three-way calling. |
| OPTION: | CXR | Call Transfer. |
| CXFERTYP: | CTALL | Call Transfer Type. CTALL = transfer all calls. |
| CXRRCL: | N | Call Transfer Recall. |
| METHOD: | STD | Method of Call Transfer: Std = Std Call Transfer method. |
| OPTION: | SMDI | Simplified message desk interface. |
| LINENO: |  | The UCD terminal number. This is the line number associated with the SMDI channel. This parameter must be unique for each
                                          agent in the associated UCDGRP. |
| UCDGRP: |  | The UCDNAME from the UCDGRP table. This is the UCD group to which you are adding the agent. |
| AUTO_LOG: | Y | Autologon capability required. |
| OPTION: | $ | The data you have entered appears. |
|  | Y | Enter Y . |

| Prompt | Input | Description |
|---|---|---|
| SO: | NEW |  |
| SONUMBER: | Press Enter. | When to invoke this service. Pressing Enter starts the service at the current date and time. |
| DN: |  | The directory number of the line. This is the DN that you enter in the SDN table. |
| LCC: | IBN | The line class code of service. |
| GROUP: |  | The name of the IBN customer group to which the line belongs. |
| SUBGRP: |  | The subgroup number. |
| NCOS: |  | The network class of service. |
| SNPA: |  | Serving NPA (area code) of the DN. |
| LEN: |  | Line equipment number of the line. For example, 4 0 1 0. |
| OPTION: | cfb | Call Forward Busy. Note This input is optional. | Note | This input is optional. |
| Note | This input is optional. |
| CFBCNTL: | N | Normal assignment for CFB. Note This input is optional. | Note | This input is optional. |
| Note | This input is optional. |
| CFBDN: |  | The primary UCD DN. Note This input is optional. | Note | This input is optional. |
| Note | This input is optional. |
| OPTION: | CFF | Call Forward Fixed. |
| CFFDN: |  | The primary UCD DN. |
| OPTION: | CFU | Call Forward Universal. |
| OVRDACR: | N | Override Automatic Callback. |
| OPTION: | $ | The data you entered appears. |
|  | Y | Enter Y to confirm the data. |

| Note | This input is optional. |
|---|---|

| Note | This input is optional. |
|---|---|

| Note | This input is optional. |
|---|---|

| Note | If you do not know this code, look it up in Table IBNXLA. The code is in the CFWP field. |
|---|---|

| Note | If the phone system is restarted, you must repeat Step 27. through Step 30. for each line DN that CFUs to the UCD group. |
|---|---|

| Field | Subfield | Setting |
|---|---|---|
| KEY | XLANAME | Enter the name of the translator, 1–8 characters, for the MWI feature. |
| DGLIDX | Enter the access code for the MWI feature. |
| RESULT | TRSEL | Enter FEAT . |
| ACR | Enter N . |
| SMDR | Enter N . |
| FEATURE | Enter the following features: CRA CRR CRDS CRDA UCDD UCDA CFWP CFWC |