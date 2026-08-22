---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg350-hardware-installation-guide-vg350-hig-vg350higcabl-html-46eba8c2e8
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg350/hardware/installation/guide/vg350_hig/vg350higcabl.html
retrieved_at: 2026-08-22T01:14:45.154554+00:00
---

Cisco VG350 Voice Gateway Hardware Installation Guide

# Cisco VG350 Voice Gateway Hardware Installation Guide

Updated: March 27, 2014

Chapter: Cable Specifications and Information

## Chapter: Cable Specifications and Information

This appendix provides the connector and pinout information you need for making or purchasing cables used with Cisco VG350 Voice Gateway. To order cables from Cisco, see the “$paratext>” section . This appendix contains the following sections:

The following list shows you which table to see for pinout information:

Cisco VG350 Voice Gateway Port and Connection Type

Pinout Information

Console Port to PC—Cable Pinouts (RJ-45 to DB-9)

Table A-1

Console Port to ASCII Terminal—Cable Pinouts (RJ-45 to DB-25)

Table A-2

Auxiliary Port to Modem—Cable Pinouts (RJ-45 to DB-25)

Table A-3

Alternative Terminal and Modem Connections

Table A-4

Gigabit Ethernet Port Pinouts (RJ-45)

Table A-5

## Console and Auxiliary Port Cables and P inouts

Your Cisco VG350 Voice Gateway comes with the cable and adapters you need to connect a PC, an ASCII terminal, or a modem to your Cisco VG350 Voice Gateway. The cable kit includes:

- RJ-45-to-RJ-45 rollover cable

- RJ-45-to-DB-9 adapter cable for console connection

- RJ-45-to-DB-25 adapter cable for modem connection

The following illustrations and tables provide cable pinout information:

- Console port to a PC—See Table A-1 and Table A-4

- Console port to an ASCII terminal—See Table A-2 and Table A-4

- Auxiliary port to a modem—See Table A-3 and Table A-4

The console port is configured as data communications equipment (DCE); the auxiliary port is configured as data terminal equipment (DTE). Both are asynchronous serial ports and use RJ-45 connectors.

### Console Port to PC

Figure A-1 shows the RJ-45-to-RJ-45 rollover cable assembly and the RJ-45-to-DB-9 female DTE adapter (labeled TERMINAL); Table A-1 lists the pinouts.

Figure A-1 Console Port to PC—Cable and Adapter

Table A-1 Console Port to PC—Cable Pinouts (RJ-45 to DB-9)

Console Port

(DCE, RJ-45)

RJ-45-to-RJ-45

Rollover Cable

RJ-45-to-DB-9

Adapter “TERMINAL”

PC Port

(DTE, DB-9)

Signal

RJ-45 Pin

RJ-45 Pin

RJ-45 Pin

DB-9 Pin

Signal

RTS

1 1

8

8

8

CTS

DTR

2

7

7

6

DSR

TxD

3

6

6

2

RxD

GND

4

5

5

5

GND

GND

5

4

4

5

GND

RxD

6

3

3

3

TxD

DSR

7

2

2

4

DTR

CTS

81

1

1

7

RTS

1. Pin 1 is connected to pin 8 inside the Cisco VG350 Voice Gateway.

### Console Port to ASCII Terminal

Figure A-2 shows the RJ-45-to-RJ-45 rollover cable assembly and the RJ-45-to-DB-25 female DTE adapter (labeled TERMINAL); Table A-2 lists the pinouts.

Figure A-2 Console Port to ASCII Terminal—Cable and Adapter

Table A-2 Console Port to ASCII Terminal—Cable Pinouts (RJ-45 to DB-25)

Console Port

(DCE, RJ-45)

RJ-45-to-RJ-45

Rollover Cable

RJ-45-to-DB-25

Adapter “TERMINAL”

Terminal Port

(DTE, DB-25)

Signal

RJ-45 Pin

RJ-45 Pin

RJ-45 Pin

DB-25 Pin

Signal

RTS

1 2

8

8

5

CTS

DTR

2

7

7

6

DSR

TxD

3

6

6

3

RxD

GND

4

5

5

7

GND

GND

5

4

4

7

GND

RxD

6

3

3

2

TxD

DSR

7

2

2

20

DTR

CTS

81

1

1

4

RTS

2. Pin 1 is connected to pin 8 inside the Cisco VG350 Voice Gateway.

### Auxiliary Port to Modem

Figure A-3 shows the RJ-45-to-RJ-45 rollover cable assembly and the RJ-45-to-DB-25 male DCE adapter (labeled MODEM); Table A-3 lists the pinouts.

Figure A-3 Auxiliary Port to Modem—Cable and Adapter

Table A-3 Auxiliary Port to Modem—Cable Pinouts (RJ-45 to DB-25)

Auxiliary Port

(DTE, RJ-45)

RJ-45-to-RJ-45

Rollover Cable

RJ-45-to-DB-25

Adapter “MODEM”

Modem Port

(DCE, DB-25)

Signal

RJ-45 Pin

RJ-45 Pin

RJ-45 Pin

DB-25 Pin

Signal

RTS

1

8

8

4

RTS

DTR

2

7

7

20

DTR

TxD

3

6

6

2

TxD

GND

4

5

5

7

GND

GND

5

4

4

7

GND

RxD

6

3

3

3

RxD

DSR

7

2

2

8

DCD

CTS

8

1

1

5

CTS

### Alternative Connections to Terminal and Modem

Your Cisco VG350 Voice Gateway ships with an RJ-45-to-RJ-45 rollover cable and two adapters for connection to a PC, a terminal, or a modem. If you want to use an RJ-45 straight-through cable or other adapters, see Table A-4 for usable cable and adapter combinations.

Table A-4 Alternative Terminal and Modem Connections

Cisco VG350 Port Connection

RJ-45 Cable Type

Adapter

Console port to PC

Straight-through

DCE, DB-9 female

Auxiliary port to modem

Rollover 3

DCE 4 , DB-25, male

Straight-through

DTE2, DB-25, male

3. An octal cable or RJ-45 breakout cable is equivalent to a rollover cable.

4. Modify the DB-25 adapter by removing the wire in pin 6 and placing it in the pin 8 position.

## Gigabit Ethernet Port Pinouts (RJ-45)

Figure A-4 shows the RJ-45 connector wiring for the Gigabit Ethernet cable; Figure A-4 lists the pinouts.

Note Pinout shown is for category 3, 4, or 5 10/100BASE-T connection to an Gigabit Ethernet switch.

Figure A-4 RJ-45 Connector Wiring

Table A-5 Gigabit Ethernet Port Pinouts (RJ-45)

Pin 5

Signal

1

TX+

2

TX–

3

RX+

4

–

5

–

6

RX–

7

–

8

–

5. Any pin not referenced is not connected.

## Analog Voice Multiport Pinouts (RJ-21X/CA21A)

Figure A-5 shows the RJ-21 connector wiring for the cable used for the multiport analog voice interface .

Figure A-5 RJ-21 Connector Wiring

Table A-6 lists the pinouts for the RJ-21 connector.

Table A-6 RJ-21 Connector Pinouts

Port Number

Connector Pin Number

Signal

Port Number

Connector Pin Number

Signal

1

1 26

Ring Tip

13

13 38

Ring Tip

2

2 27

Ring Tip

14

14 39

Ring Tip

3

3 28

Ring Tip

15

15 40

Ring Tip

4

4 29

Ring Tip

16

16 41

Ring Tip

5

5 30

Ring Tip

17

17 42

Ring Tip

6

6 31

Ring Tip

18

18 43

Ring Tip

7

7 32

Ring Tip

19

19 44

Ring Tip

8

8 33

Ring Tip

20

20 45

Ring Tip

9

9 34

Ring Tip

21

21 46

Ring Tip

10

10 35

Ring Tip

22

22 47

Ring Tip

11

11 36

Ring Tip

23

23 48

Ring Tip

12

12 37

Ring Tip

24

24 49

Ring Tip

—

—

—

—

25, 50, 51, 52

GND

| Cisco VG350 Voice Gateway Port and Connection Type | Pinout Information |
|---|---|
| Console Port to PC—Cable Pinouts (RJ-45 to DB-9) | Table A-1 |
| Console Port to ASCII Terminal—Cable Pinouts (RJ-45 to DB-25) | Table A-2 |
| Auxiliary Port to Modem—Cable Pinouts (RJ-45 to DB-25) | Table A-3 |
| Alternative Terminal and Modem Connections | Table A-4 |
| Gigabit Ethernet Port Pinouts (RJ-45) | Table A-5 |

| Console Port (DCE, RJ-45) | RJ-45-to-RJ-45 Rollover Cable | RJ-45-to-DB-9 Adapter “TERMINAL” | PC Port (DTE, DB-9) |
|---|---|---|---|
| Signal | RJ-45 Pin | RJ-45 Pin | RJ-45 Pin | DB-9 Pin | Signal |
| RTS | 1 1 | 8 | 8 | 8 | CTS |
| DTR | 2 | 7 | 7 | 6 | DSR |
| TxD | 3 | 6 | 6 | 2 | RxD |
| GND | 4 | 5 | 5 | 5 | GND |
| GND | 5 | 4 | 4 | 5 | GND |
| RxD | 6 | 3 | 3 | 3 | TxD |
| DSR | 7 | 2 | 2 | 4 | DTR |
| CTS | 81 | 1 | 1 | 7 | RTS |

| 1. Pin 1 is connected to pin 8 inside the Cisco VG350 Voice Gateway. |
|---|

| Console Port (DCE, RJ-45) | RJ-45-to-RJ-45 Rollover Cable | RJ-45-to-DB-25 Adapter “TERMINAL” | Terminal Port (DTE, DB-25) |
|---|---|---|---|
| Signal | RJ-45 Pin | RJ-45 Pin | RJ-45 Pin | DB-25 Pin | Signal |
| RTS | 1 2 | 8 | 8 | 5 | CTS |
| DTR | 2 | 7 | 7 | 6 | DSR |
| TxD | 3 | 6 | 6 | 3 | RxD |
| GND | 4 | 5 | 5 | 7 | GND |
| GND | 5 | 4 | 4 | 7 | GND |
| RxD | 6 | 3 | 3 | 2 | TxD |
| DSR | 7 | 2 | 2 | 20 | DTR |
| CTS | 81 | 1 | 1 | 4 | RTS |

| 2. Pin 1 is connected to pin 8 inside the Cisco VG350 Voice Gateway. |
|---|

| Auxiliary Port (DTE, RJ-45) | RJ-45-to-RJ-45 Rollover Cable | RJ-45-to-DB-25 Adapter “MODEM” | Modem Port (DCE, DB-25) |
|---|---|---|---|
| Signal | RJ-45 Pin | RJ-45 Pin | RJ-45 Pin | DB-25 Pin | Signal |
| RTS | 1 | 8 | 8 | 4 | RTS |
| DTR | 2 | 7 | 7 | 20 | DTR |
| TxD | 3 | 6 | 6 | 2 | TxD |
| GND | 4 | 5 | 5 | 7 | GND |
| GND | 5 | 4 | 4 | 7 | GND |
| RxD | 6 | 3 | 3 | 3 | RxD |
| DSR | 7 | 2 | 2 | 8 | DCD |
| CTS | 8 | 1 | 1 | 5 | CTS |

| Cisco VG350 Port Connection | RJ-45 Cable Type | Adapter |
|---|---|---|
| Console port to PC | Straight-through | DCE, DB-9 female |
| Auxiliary port to modem | Rollover 3 | DCE 4 , DB-25, male |
|  | Straight-through | DTE2, DB-25, male |

| 3. An octal cable or RJ-45 breakout cable is equivalent to a rollover cable. 4. Modify the DB-25 adapter by removing the wire in pin 6 and placing it in the pin 8 position. |
|---|

| Pin 5 | Signal |
|---|---|
| 1 | TX+ |
| 2 | TX– |
| 3 | RX+ |
| 4 | – |
| 5 | – |
| 6 | RX– |
| 7 | – |
| 8 | – |

| 5. Any pin not referenced is not connected. |
|---|

| Port Number | Connector Pin Number | Signal | Port Number | Connector Pin Number | Signal |
|---|---|---|---|---|---|
| 1 | 1 26 | Ring Tip | 13 | 13 38 | Ring Tip |
| 2 | 2 27 | Ring Tip | 14 | 14 39 | Ring Tip |
| 3 | 3 28 | Ring Tip | 15 | 15 40 | Ring Tip |
| 4 | 4 29 | Ring Tip | 16 | 16 41 | Ring Tip |
| 5 | 5 30 | Ring Tip | 17 | 17 42 | Ring Tip |
| 6 | 6 31 | Ring Tip | 18 | 18 43 | Ring Tip |
| 7 | 7 32 | Ring Tip | 19 | 19 44 | Ring Tip |
| 8 | 8 33 | Ring Tip | 20 | 20 45 | Ring Tip |
| 9 | 9 34 | Ring Tip | 21 | 21 46 | Ring Tip |
| 10 | 10 35 | Ring Tip | 22 | 22 47 | Ring Tip |
| 11 | 11 36 | Ring Tip | 23 | 23 48 | Ring Tip |
| 12 | 12 37 | Ring Tip | 24 | 24 49 | Ring Tip |
| — | — | — | — | 25, 50, 51, 52 | GND |