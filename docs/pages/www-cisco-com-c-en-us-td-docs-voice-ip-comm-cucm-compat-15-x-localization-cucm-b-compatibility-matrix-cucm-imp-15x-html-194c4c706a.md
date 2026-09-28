---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-compat-15-x-localization-cucm-b-compatibility-matrix-cucm-imp-15x-html-194c4c706a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/15_x/Localization/cucm_b_compatibility-matrix-cucm-imp-15x.html
retrieved_at: 2026-08-16T17:50:57.863937+00:00
---

Matrice di compatibilità per Cisco Unified Communications Manager e il servizio IM and Presence, versione 15x

# Matrice di compatibilità per Cisco Unified Communications Manager e il servizio IM and Presence, versione 15x

Accedi per salvare i contenuti

Aggiornato: 20 novembre 2025

# Matrice di compatibilità per Cisco Unified Communications Manager e il servizio IM and Presence

## Cronologia delle revisioni

Data

Revisione

14 agosto 2025

Versione di supporto aggiornata per Unified CM Release 15SU3a.

31 luglio 2025

Pubblicazione della guida iniziale per 15SU3.

31 luglio 2025

Supporto della versione aggiornato per 15SU3.

31 luglio 2025

Informazioni aggiornate su API e sui pacchetti di connessione protetta.

31 luglio 2025

Aggiornato l'elenco dei cifrari per Unified CM e IM and Presence Service.

27 maggio 2025

È stata aggiornata la sezione "Supporto peering intercluster".

17 marzo 2025

Aggiunto il supporto per Cisco Board Pro 55 G2 e Cisco Board Pro 75 G2 dalla release 15SU1 in poi.

01 ottobre 2024

Pubblicazione della guida iniziale per 15SU2.

01 ottobre 2024

Supporto della versione aggiornato per 15SU2.

01 ottobre 2024

Aggiunto il supporto per Cisco Desk Phone serie 9800.

01 ottobre 2024

Informazioni aggiornate su API e Secure Connection Packages.

01 ottobre 2024

Aggiornato l'elenco dei cifrari per Unified CM.

20 giugno 2024

Versione di supporto aggiornata per Unified CM Release 15SU1a.

28 marzo 2024

Aggiunto il supporto della versione per 15SU1.

28 marzo 2024

Informazioni aggiornate su API e Secure Connection Packages per 15SU1.

18 dicembre 2023

Aggiunto il supporto della versione per la versione 15.

18 dicembre 2023

Informazioni aggiornate sul supporto della directory LDAP.

18 dicembre 2023

Sezione Browser supportati aggiornata.

18 dicembre 2023

È stato rimosso il supporto per Active Directory 2012 con Windows Server 2012 dalla sezione "Integrazione del calendario con
                              Microsoft Outlook".

18 dicembre 2023

È stato rimosso il supporto per "Controllo chiamate remote con server Microsoft Lync" per IM and Presence servizio in quanto
                              Microsoft Lync Server 2013 ha superato la fine del supporto principale (EOS) di Microsoft datata 10 aprile 2018 e anche esteso
                              EOS datato 11 aprile 2023.

## Scopo del presente documento

Questo documento contiene informazioni sulla compatibilità per le versioni 15x di Cisco Unified Communications Manager (Unified
                  Communications Manager) e Cisco Unified Communications Manager IM and Presence Service (servizio IM and Presence). Ciò includerà
                  anche i successivi rilasci di SU, se non diversamente indicato.

## Percorsi di aggiornamento e migrazione supportati con file COP

Nella tabella seguente vengono evidenziati i percorsi di aggiornamento supportati per l'aggiornamento alla Release 15 e successive
                     di Cisco Unified Communications Manager e del servizio IM and Presence. Vengono inoltre elencati i percorsi di aggiornamento
                     che richiedono file COP. È necessario installare i file COP su ciascun nodo prima di iniziare un aggiornamento utilizzando
                     l'interfaccia di amministrazione Cisco Unified OS o prima di iniziare un aggiornamento o una migrazione utilizzando lo strumento
                     Cisco Prime Collaboration Deployment (PCD). Se si utilizza PCD, è possibile eseguire un'installazione di massa dei file COP
                     prima di iniziare l'aggiornamento.

Nota

Salvo diversa indicazione, ogni categoria di release include le release SU all'interno di tale categoria.

È possibile scaricare i file COP per Cisco Unified Communications Manager e il servizio IM and Presence su https://software.cisco.com/download/home/268439621 . Dopo aver selezionato la versione di destinazione per l'aggiornamento, scegliere Unified Communications Manager Utilities per visualizzare l'elenco dei file COP.

Nota

Sebbene non sia obbligatorio, si consiglia di eseguire il file COP Upgrade Readiness prima dell'aggiornamento per massimizzare
                              la riuscita dell'aggiornamento. Cisco TAC potrebbe richiedere l'esecuzione di questo file COP per fornire un supporto tecnico
                              efficace.

Nota

Se l'origine è in modalità FIPS e/o PCD in modalità FIPS, vedere https://www.cisco.com/web/software/286319173/139477/ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop-ReadMe.pdf per informazioni sul file COP ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop . Questo documento descrive in dettaglio i prerequisiti necessari per l'aggiornamento diretto o la migrazione diretta alle
                              versioni di destinazione 15 o successive.

Nota

Se dalla release di origine è disponibile un aggiornamento standard diretto alla versione 15 o successiva, è possibile scegliere
                                 un aggiornamento a nodo singolo o a livello di cluster.

Se si desidera aggiornare un intero cluster e si prevede una durata minima, tempi di inattività, impatto sul servizio o interventi
                                 amministrativi, utilizzare la procedura "Clusterwide Upgrade Task Flow (Direct Standard)" che descrive in dettaglio l'aggiornamento
                                 del cluster tramite Unified CM Publisher utilizzando l'aggiornamento di Unified OS Admin o l'aggiornamento CLI. Qui, aggiornerai
                                 solo il Unified CM Publisher e orchestra l'aggiornamento o il riavvio di tutti gli altri nodi del cluster.

Se si prevede di aggiornare l'origine nodo per nodo o di utilizzare un singolo nodo solo utilizzando l'aggiornamento locale
                                 di Unified OS Admin o l'aggiornamento CLI, vedere la sezione "Aggiornamento dei nodi cluster (Direct Standard)". Per ulteriori
                                 informazioni, vedere la Guida all'aggiornamento e alla migrazione per Cisco Unified Communications Manager e il servizio IM and Presence .

Nota

È necessario assicurarsi che il piano di aggiornamento segua le regole di sequenziazione dei nodi menzionate nella Guida all'aggiornamento https://www-author3.cisco.com/content/en/us/td/docs/voice_ip_comm/cucm/upgrade/15/cucm_b_upgrade-and-migration-guide_15/cucm_m_sequencing-rules-time-requirements-15.html#reference_3E039AF4416B1F56A9F9E5D7DF25344B . Prima di cambiare versione nei nodi IM and Presence Service, è necessario cambiare i nodi Unified Communications Manager,
                                 iniziando dal nodo di pubblicazione e quindi dai nodi del sottoscrittore.

Se non si segue la sequenza menzionata e quindi se il nodo Unified Communications Manager Publisher passa alla versione 15
                                 o successiva e la versione del nodo IM and Presence Service Publisher è ancora nelle versioni 12.5.x o 14 e SU e non viene
                                 aggiornata, le pagine seguenti nel menu Aggiornamenti software non verranno visualizzate né funzioneranno per i nodi del servizio
                                 IM and Presence:

Cluster di riavvio/cambio versione

Posizione del software cluster

Cluster di installazione e aggiornamento software

Nota

Non esistono percorsi supportati da Direct Refresh Upgrade per Unified Communications Manager e IM and Presence Service Release
                              15 e versioni successive. L'aggiornamento degli aggiornamenti dall'origine precedente alla 12.5.x alla release 15 e successive
                              non è supportato.

Origine

Destinazione

Meccanismo

Pre-requisiti

Cambio di versione* (dall'origine alla destinazione e viceversa)

10.0

15

Attività di migrazione PCD 15 (V2V)

L'aggiornamento diretto a 15 non è supportato. Quando la versione di destinazione è 15 o superiore e la versione di origine
                                 è 10.0, per la migrazione è necessario utilizzare la distribuzione Cisco Prime Collaboration (PCD).

Se la versione di destinazione è 15 o superiore e la versione di origine 10.0 è in modalità FIPS, la distribuzione Cisco Prime
                                 Collaboration (PCD) deve essere in modalità non FIPS.

Non applicabile

10.5

15

Attività di migrazione PCD 15 (V2V)

Eseguire il file COP pre-upgrade-check.

È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione.

L'aggiornamento diretto a 15 non è supportato. Quando la versione di destinazione è 15 o superiore e la versione di origine
                                 è 10.5, per la migrazione è necessario utilizzare la distribuzione Cisco Prime Collaboration (PCD).

Se la versione di destinazione è 15 o superiore e la versione di origine 10.5 è in modalità FIPS, allora:

Il PCD deve essere in (o inserito) in modalità non FIPS.

Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD.

Non applicabile

Nuova installazione con importazione dati (V2V)

Eseguire il file COP pre-upgrade-check.

Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512

Ciscocm. DataExport_v1.0.cop.sgn

Non supportato

11.0

15

Attività di migrazione PCD 15 (V2V)

Eseguire il file COP pre-upgrade-check.

È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione.

Se la versione di destinazione è 15 o superiore e la versione di origine 11.0 è in modalità FIPS, allora:

Il PCD deve essere in (o inserito) in modalità non FIPS.

Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD.

Non supportato

Nuova installazione con importazione dati (V2V)

Eseguire il file COP pre-upgrade-check.

Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512

Ciscocm. DataExport_v1.0.cop.sgn

Non supportato

11.5

15

Attività di migrazione PCD 15 (V2V)

Eseguire il file COP pre-upgrade-check.

È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione.

Se la versione di destinazione è 15 o superiore e la versione di origine 11.5 è in modalità FIPS, allora:

Il PCD deve essere in (o inserito) in modalità non FIPS.

Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD.

Non supportato

Nuova installazione con importazione dati (V2V)

Eseguire il file COP pre-upgrade-check.

Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512

Ciscocm. DataExport_v1.0.cop.sgn

Non supportato

12.0

15

Attività di migrazione PCD 15 (V2V)

Eseguire il file COP pre-upgrade-check.

È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione.

Se la versione di origine è la Release 12.0 (1) di Unified Communications Manager (12.0.1.10000-10), è necessario installare
                                 il seguente file COP: ciscocm-slm-migration.k3.cop.sgn . Questo non è necessario se la versione di origine è superiore, ad esempio, Release 12.0(1)SU1.

Non supportato

Nuova installazione con importazione dati (V2V)

Eseguire il file COP pre-upgrade-check.

Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512

Ciscocm. DataExport_v1.0.cop.sgn

Non supportato

12.5

15

Aggiornamento standard diretto (aggiornamenti semplici)

Tramite OS Admin o CLI

Eseguire il file COP pre-upgrade-check.

Supportato

Aggiornamento standard diretto

Tramite attività di aggiornamento PCD 15

Eseguire il file COP pre-upgrade-check.

Se l'origine Unified CM è precedente a 12.5.1.14900-63, installare il seguente file COP: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn .

Se l'origine del servizio IM and Presence è precedente a 12.5.1.14900-4, installare il seguente file COP: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn .

Se la versione di destinazione è 15 o superiore e la versione di origine 12.5 è in modalità FIPS, allora:

Il PCD deve essere in (o inserito) in modalità non FIPS.

Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di aggiornamento PCD.

Se si utilizza Cisco Prime Collaboration Deployment per aggiornare un cluster di IM and Presence Service dalla versione 12.5.x
                                       alla release 15 o successiva, è necessario installare il seguente file COP sui sistemi della release 12.5.x prima di iniziare
                                       l'aggiornamento: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512 .

Si noti che il file COP è applicabile solo se:

Unified Communications Manager versione di destinazione è nella Release 15 o superiore.

Unified Communications Manager versione di destinazione è nella versione 15 o successiva e si sta tentando di aggiornare l'origine
                                             del servizio IM and Presence da una versione con restrizioni a una versione senza restrizioni.

Supportato

Attività di migrazione PCD 15 (V2V)

Eseguire il file COP pre-upgrade-check.

È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione.

Se la versione di destinazione è 15 o superiore e la versione di origine 12.5 è in modalità FIPS, allora:

Il PCD deve essere in (o inserito) in modalità non FIPS.

Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD.

Non supportato

Nuova installazione con importazione dati (V2V)

Eseguire il file COP pre-upgrade-check.

Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512

Ciscocm. DataExport_v1.0.cop.sgn

Non supportato

14 e SU

15

Aggiornamento standard diretto (aggiornamenti semplici)

Tramite OS Admin o CLI

Eseguire il file COP pre-upgrade-check.

Nota

Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli.

Supportato

Aggiornamento standard diretto

Tramite attività di aggiornamento PCD

Eseguire il file COP pre-upgrade-check.

Se la versione di destinazione è 15 o superiore e la versione di origine è 14 e SU in modalità FIPS, allora:

Il PCD deve essere in (o inserito) in modalità non FIPS.

Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di aggiornamento PCD.

Se si utilizza Cisco Prime Collaboration Deployment per aggiornare un cluster del servizio IM and Presence dalla Release 14
                                       o SU alla Release 15 o successiva, è necessario installare il seguente file COP nei sistemi Release 14 o SU prima di iniziare
                                       l'aggiornamento: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512 . Si noti che il file COP è applicabile solo se:

Unified Communications Manager versione di destinazione è nella versione 15 o superiore e i nodi di origine del servizio IM
                                             and Presence sono nelle versioni 14 o 14SU1.

Unified Communications Manager versione di destinazione è nella versione 15 o successiva e si sta tentando di aggiornare l'origine
                                             del servizio IM and Presence da una versione con restrizioni a una versione senza restrizioni.

Nota

Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli.

Supportato

Attività di migrazione PCD 15 (V2V)

Eseguire il file COP pre-upgrade-check.

È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione.

Se la versione di destinazione è 15 o superiore e la versione di origine è 14 o SU in modalità FIPS, allora:

Il PCD deve essere in (o inserito) in modalità non FIPS.

Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD.

Non supportato

Nuova installazione con importazione dati (V2V)

Eseguire il file COP pre-upgrade-check.

Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512

Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512

Ciscocm. DataExport_v1.0.cop.sgn

Non supportato

* Il cambio di versione si riferisce alla possibilità di installare la nuova versione come versione inattiva e passare alla
                     nuova versione e ripristinare la vecchia versione, ogni volta che lo si desidera. Questa funzionalità è supportata con la
                     maggior parte degli aggiornamenti diretti, ma non con le migrazioni.

Nota

Aggiornamenti e migrazioni PCD: per tutti i percorsi supportati utilizzando l'attività di aggiornamento PCD o l'attività di
                              migrazione PCD nella tabella precedente, è necessario utilizzare PCD Release 15.

## Versioni supportate

Nella tabella seguente vengono illustrate le versioni Unified Communications Manager e IM and Presence Service supportate
                     con ogni versione:

Per questa versione...

Sono supportate le seguenti versioni...

15

Unified Communications Manager 15.0.1.10000-32

Servizio IM and Presence 15.0.1.10000-10

15SU1a

Unified Communications Manager Versione 15SU1a: 15.0.1.11901-2

IM and Presence Service Release 15SU1: 15.0.1.11900-4

15SU2

Unified Communications Manager 15.0.1.12900-234

Servizio IM and Presence 15.0.1.12900-10

15SU3

Unified Communications Manager 15.0.1.13901-2

Servizio IM and Presence 15.0.1.13900-6

### Compatibilità delle versioni tra Unified CM e il servizio IM and Presence

La compatibilità della versione dipende dal tipo di distribuzione del servizio IM and Presence. Nella tabella seguente vengono
                        illustrate le opzioni e indica se è supportata una mancata corrispondenza tra la distribuzione di telefonia e la distribuzione
                        del servizio IM and Presence. Una mancata corrispondenza delle versioni, se supportata, consente di distribuire la distribuzione
                        di telefonia Unified Communications Manager e la distribuzione del servizio IM and Presence utilizzando versioni diverse.

Nota

Qualsiasi respin o ES prodotto tra le versioni Cisco.com è considerato parte della versione precedente. Ad esempio, un ES Unified Communications Manager con un numero di build di
                                 15.0.1.13[0-2]xx sarebbe considerato parte della versione 15 (15.0.1.10900-x).

Tipo distribuzione

Rilascio non corrispondente

Descrizione

Distribuzione standard del servizio IM and Presence

Non supportato

Unified Communications Manager e il servizio IM and Presence si trovano nello stesso cluster e devono eseguire la stessa versione:
                                    una mancata corrispondenza delle versioni non è supportata.

Distribuzione centralizzata del servizio IM and Presence

Supportato

La distribuzione del servizio IM and Presence e la distribuzione di telefonia si trovano in cluster diversi e possono eseguire
                                    versioni diverse: è supportata una mancata corrispondenza delle versioni.

Nota

Il cluster centrale IM and Presence Service include anche un nodo Unified CM Publisher autonomo per il provisioning di database
                                             e utenti. Questo nodo non di telefonia deve eseguire la stessa release del servizio IM and Presence.

## Unified Communications Manager Informazioni sulla compatibilità

### Cisco Applicazioni di sistemi di collaborazione

Questa versione di Cisco Unified Communications Manager e del servizio IM and Presence fa parte di Cisco Collaboration Systems
                        Release 15 ed è compatibile con le altre applicazioni e versioni Cisco Collaboration in Cisco Collaboration Systems Release
                        15.

Per un elenco completo delle applicazioni Cisco Collaboration che fanno parte di Cisco Collaboration Systems Release 15 e
                        delle relative versioni supportate, vedere # Cisco Collaboration Systems Release Compatibility Matrix in: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix-InteractiveHTML.html .

### Android Consigli sulla compatibilità delle notifiche push

Android La funzione di notifica push è supportata dalle seguenti versioni del software:

Unified Communications Manager 12.5(1)SU3

Servizio IM and Presence 12.5(1)SU3

Cisco Jabber 12.9.1

Cisco Expressway X12.6.2

Nota

Queste informazioni sulla compatibilità non sono applicabili per Cisco Webex.

Unified Communications Manager e IM and Presence versione del servizio

Versione Expressway

Unified Communications Mobile e Remote Access

Distribuzioni locali

Tutti i cluster su:

11.5(1)SU8 o versioni precedenti

12.5(1)SU2 o versioni precedenti

X12.6.2

Android La notifica push non è supportata

Android La notifica push non è supportata

Tutti i cluster su:

12.5(1)SU3 e successivi

X12.6.2

Abilita notifica push Android tramite CLI xConfiguration XCP Config FcmService: attivato su Expressway solo per la messaggistica

Android La notifica push è supportata

Cluster con versioni miste (11.5(1)SU8 o versioni precedenti, OPPURE 12.5(1)SU2 o versioni precedenti E 12.5(1)SU3 e successive)

X12.6.2

Android La notifica push per la messaggistica non è supportata

VoIP è supportato dalla release 12.5(1)SU3 in poi

Android La notifica push è supportata dalla release 12.5(1)SU3 in poi

#### IM and Presence Stream Caratteristiche/Servizi Consigli sulla compatibilità degli annunci pubblicitari

IM and Presence Servizio supporta la pubblicità di funzionalità/servizi XMPP stream ai client che si connettono tramite Cisco
                        Expressway's Mobile e Remote Access.

A seconda della combinazione di versioni del servizio IM and Presence corrente, potrebbe essere necessario abilitare o disabilitare
                        la funzione di notifiche push utilizzando il flag di servizio FCM sull'autostrada in base alle informazioni fornite nella
                        tabella seguente:

```
xConfiguration XCP Config FcmService: On/Off
```

Nota

Apple Push Notification Service (APNS) non è interessato dallo stato del flag di servizio FCM.

Versioni miste IM and Presence cluster

Stato previsto del flag FCM su Expressway X12.7

Commento

Qualsiasi 11.5(1)SU con

12.5(1)SU2 e inferiori

OFF

Android Push (FCM) NON supportato.

11.5(1)SU8 (e inferiore) o 12.5(1)SU2 (e inferiore) con 12.5(1)SU3 o 14

OFF

Android push (FCM) NON supportato

11.5(1)SU8 (e versioni precedenti) o 12.5(1)SU2 (e inferiori) con 12.5(1)SU4 (e superiori) o 14SU1 (e superiori)

OFF

Android push (FCM) supportato nelle versioni 12.5(1)SU4 (o più recenti)

11.5(1)SU9 (e superiore) o 12.5(1)SU4 (e superiore) con 12.5(1)SU3 o 14SU1 (e superiore)

ON

Android push (FCM) supportato sulla versione 12.5(1)SU3 e successive

11.5(1)SU9 (e superiore) con 12.5(1)SU4 (e superiore) o 14SU1 (e superiore)

Flag non richiesto

(Expressway 12.7 si basa completamente sul nuovo meccanismo di rilevamento)

Android push (FCM) supportato nelle versioni 12.5(1)SU4 (o più recenti)

### Cisco Supporto endpoint

Tutti gli annunci di fine vita e fine vendita sono elencati qui: https://www.cisco.com/c/en/us/products/eos-eol-listing.html

#### Endpoint Cisco supportati

Nella tabella seguente sono elencati gli endpoint Cisco supportati con questa versione di Cisco Unified Communications Manager.
                        Per gli endpoint che hanno raggiunto la fine della vendita (EOS) o la fine della manutenzione software, fare clic sul collegamento
                        EOS per visualizzare i dettagli del supporto.

Nota

Cisco non rilascerà correzioni di bug o miglioramenti della sicurezza per gli endpoint che hanno raggiunto lo stato di Fine
                                    della manutenzione software o Fine del supporto, indipendentemente dal fatto che tali endpoint siano deprecati o meno. Cisco
                                    non testerà Unified Communications Manager con i telefoni End of Life. Né risolveremo i bug Unified Communications Manager
                                    relativi ai telefoni End of Life a meno che il problema non possa essere replicato su un telefono che non è End of Life.

Serie di dispositivi

Modello dispositivo

Cisco Unified SIP Phone serie 3900

Telefono SIP Cisco Unified 3905

Telefono IP Cisco Unified serie 6900

Telefono IP Cisco Unified 6901

Telefono IP Cisco serie 7800

Telefono IP Cisco 7811

Telefono IP Cisco 7821

Telefono IP Cisco 7841

Telefono IP Cisco 7861

Telefono IP per chiamate in conferenza Cisco 7832

Telefono IP Cisco Unified serie 7900

Cisco Unified IP Phone Modulo di espansione 7915— Avviso EOS

Cisco Unified IP Phone Modulo di espansione 7916— Avviso EOS

Cisco Unified IP Phone 7942G— Avviso EOS

Cisco Unified IP Phone 7945G— Avviso EOS

Cisco Unified IP Phone 7962G— Avviso EOS

Cisco Unified IP Phone 7965G— Avviso EOS

Cisco Unified IP Phone 7975G— Avviso EOS

Telefono IP Cisco serie 8800

Cisco IP Phone 8811, 8831, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR

Cisco Wireless IP Phone 8821, 8821-EX— Avviso EOL

Cisco Unified IP Telefono conferenza 8831— Avviso EOS

Telefono IP per chiamate in conferenza Cisco 8832

Videotelefono Cisco 8875

Cisco Video Phone 8875NR

Telefono IP Cisco Unified serie 8900

Cisco Unified IP Phone 8945— Avviso EOS

Cisco Unified IP Phone 8961— Avviso EOS

Telefono IP Cisco Unified serie 9900

Cisco Unified IP Phone 9951— Avviso EOS

Cisco Unified IP Phone 9971— Avviso EOS

Cisco Telefono fisso serie 9800

Cisco Telefono fisso 9841

Cisco Telefono fisso 9851

Cisco Telefono fisso 9861

Cisco Telefono fisso 9871

Cisco Modulo di espansione chiavi 9800 per telefono fisso (KEM)

Cisco Jabber

Cisco Jabber per Android

Cisco Jabber per iPhone e iPad

Cisco Jabber per Mac

Cisco Jabber per Windows

Cisco Jabber Softphone per VDI - Windows (in precedenza  Cisco Virtualization Experience Media Edition per Windows)

Cisco Jabber Guest

Cisco Jabber Software Development Kit

Cisco Jabber per Tablet

Serie di cuffie Cisco

Cuffia Cisco 320

Cuffia Cisco 520

Cuffia Cisco 530

Cuffia Cisco 560

Cuffia Cisco 720

Cuffia Cisco 730

Cisco IP Communicator

Cisco IP Communicator— Avviso EOS

Webex

App Webex

Webex Room Phone

Webex Desk

Cisco Desk Camera 4K

Cisco Desk Camera 1080p

Webex Desk Hub

Webex Desk Pro

Webex Desk Edizione limitata

Webex Share— Avviso EOS

Board 55, 55S, 70, 70S, 85, 85S

Board Pro 55 G2 e 75 G2

Webex Room Panorama

Webex Room 70 Panorama

Webex Room 70 Panorama Aggiornamento

Room 70

Room 70 G2

Room 55

Dual sale 55

Room Kit Pro

Room Kit Plus

Room Kit

Room Kit Mini

Webex Room USB

Telefono wireless Webex serie 800

Webex Telefono senza fili 840

Telefono wireless Webex 860

Webex Meetings

Webex Meetings per iPhone e iPad

Webex Meetings per Android

Cisco Adattatori per telefonia analogica

Cisco Adattatori telefonici analogici serie ATA 190 - Avviso EOS/EOL

Cisco Adattatori telefonici analogici serie ATA 191

Cisco serie DX

Cisco Webex DX70 - Avviso EOS

Cisco Webex DX80— Avviso EOS

Cisco DX650— Avviso EOS

Cisco TelePresence IX5000

Cisco TelePresence IX5000

Cisco TelePresence Serie EX

Cisco TelePresence System EX90 - Avviso EOS

Cisco TelePresence serie MX

Cisco TelePresence MX200 G2 - Avviso EOS

Cisco TelePresence MX300 G2— Avviso EOS

Cisco TelePresence MX700D - Avviso EOS

Cisco TelePresence MX800S - Avviso EOS

Cisco TelePresence MX800D - Avviso EOS

Cisco TelePresence serie SX

Cisco TelePresence SX10 - Avviso EOS

Cisco TelePresence SX20 - Avviso EOS

Cisco TelePresence SX80 - Avviso EOS

Per un elenco delle versioni del firmware utilizzate per ciascun endpoint Cisco, vedere la matrice Cisco di compatibilità delle versioni dei sistemi di collaborazione all'indirizzo http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix.html .

Per informazioni sulla compatibilità dei Device Pack per supportare i telefoni, vedere # Cisco Unified Communications Manager Device Package Compatibility Matrix all'indirizzo http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix.html .

#### Fine del supporto

Nella tabella seguente sono elencati gli endpoint Cisco che hanno raggiunto la data di fine supporto, ma che non sono ancora
                        deprecati. A differenza degli endpoint obsoleti, è comunque possibile distribuire questi endpoint nell'ultima versione, ma
                        non sono supportati attivamente, non sono testati e potrebbero non funzionare.

Fare clic sui collegamenti per visualizzare gli annunci di supporto per ciascun endpoint.

Per informazioni su tutti i prodotti End of Support e End-of-Life, vedere https://www.cisco.com/c/en_ca/products/eos-eol-listing.html .

Cisco Endpoint alla fine del supporto

#### Modelli di telefono obsoleti

Nella tabella seguente sono elencati tutti i modelli di telefono deprecati per questa versione di Unified Communications Manager , insieme alla versione Unified CM in cui il modello di telefono è diventato obsoleto per la prima volta. Ad esempio, un modello
                           di telefono che è stato deprecato per la prima volta nella Release 11.5 (1) è deprecato per tutte le versioni successive,
                           incluse tutte le versioni 12.x.

Se si sta eseguendo l'aggiornamento alla versione corrente di Unified Communications Manager e si dispone di uno di questi modelli di telefono distribuiti, il telefono non funzionerà dopo l'aggiornamento.

Modelli di telefono obsoleti per questa release

Deprecato per la prima volta a partire da Unified CM...

Nessun endpoint aggiuntivo deprecato

Versione 15

Nessun endpoint aggiuntivo deprecato

Versione 14

Cisco Unified Wireless IP Phone 7921

Telefono IP Cisco Unified 7970

Telefono IP Cisco Unified 7971

12.0 (1) e versioni successive

Cisco IP Phone 12 S

Cisco IP Phone 12 SP

Cisco IP Phone 12 SP+

Cisco IP Phone 30 SP+

Cisco IP Phone 30 VIP

Telefono IP Cisco Unified 7902G

Telefono IP Cisco Unified 7905G

Telefono IP Cisco Unified 7910

Telefono IP Cisco Unified 7910G

Cisco Unified IP Phone 7910+SW

Cisco Unified IP Phone 7910G+SW

Telefono IP Cisco Unified 7912G

Cisco Unified Wireless IP Phone 7920

Cisco Unified IP Conference Station 7935

11.5 (1) e versioni successive

### Requisiti di virtualizzazione

Questa versione di Unified Communications Manager e il servizio IM and Presence supportano solo distribuzioni virtualizzate.
                        Le distribuzioni su server bare metal non sono supportate. Per ulteriori informazioni, consultare http://www.cisco.com/go/virtualized-collaboration .

Vedere la tabella seguente per i requisiti di virtualizzazione.

Requisiti di virtualizzazione per...

Per informazioni, vai a...

Unified Communications Manager

Per informazioni sui requisiti di virtualizzazione Unified Communications Manager, vedere https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-communications-manager.html .

IM e servizio di presenza

Per informazioni sui requisiti di virtualizzazione del servizio IM and Presence, vedere https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-ucm-im-presence.html .

Cisco Business Edition Distribuzioni

Per informazioni sui requisiti di virtualizzazione per Unified Communications Manager in una distribuzione di una soluzione
                                    di collaborazione come Cisco Business Edition, vedere quanto segue:

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html

Cisco Business Edition 7000

Cisco Business Edition 6000

### Directory LDAP supportate

Sono supportate le seguenti directory LDAP:

Microsoft Active Directory su Windows Server 2016

Microsoft Active Directory su Windows Server 2019: supportato per 15 e versioni successive

Microsoft Active Directory su Windows Server 2022: supportato per 15 e versioni successive

Microsoft Lightweight Directory Services 2019 e 2022: supportato per 15 e versioni successive

Oracle Unified Directory 12cPS4

OpenLDAP Long Term Support (LTS) Release 2.5.16

Altre directory conformi a LDAPv3: Unified Communications Manager utilizza LDAPv3 standard per accedere ai dati dell'utente.
                              Assicurarsi che l'attributo supportedcontrol sia configurato nei server di directory conformi LDAPv3 da utilizzare con DirSync.
                              L'attributo supportedcontrol può restituire gli attributi secondari pagecontrolsupport e persistentcontrolsupport , se configurati.

Webex Supporto di Cloud-Connected UC Directory Service—Per ulteriori informazioni, vedere Webex Supporto di Cloud-Connected UC Directory Service per Unified CM .

### Browser Web supportati

Sono supportati i seguenti browser Web:

Browser Firefox, Chrome e Microsoft Edge con Windows 10 e 11 (64 bit)

Safari, Chrome e Firefox su MacOS Ventura 13.4.1

Nota

Si consiglia di utilizzare la versione più recente per tutti i browser Web supportati.

### Supporto server SFTP

Per i test interni, utilizziamo SFTP Server on Cisco Prime Collaboration Deployment (PCD) fornito da Cisco e supportato da
                        Cisco TAC. Fare riferimento alla tabella seguente per un riepilogo delle opzioni del server SFTP:

server SFTP

Descrizione del supporto

Server SFTP nella distribuzione Cisco Prime Collaboration

Questo server è l'unico server SFTP fornito e testato da Cisco e completamente supportato da Cisco TAC.

La compatibilità della versione dipende dalla versione di Emergency Responder e dalla distribuzione Cisco Prime Collaboration
                                    in uso. Vedere la Cisco Prime Collaboration Deployment Administration Guide prima di aggiornare la versione (SFTP) o Emergency
                                    Responder per assicurarsi che le versioni siano compatibili.

SFTP Server da un partner tecnologico

Questi server sono forniti da terze parti e testati da terze parti. La compatibilità della versione dipende dal test di terze
                                    parti. Fare riferimento alla pagina del partner tecnologico se si aggiorna il loro prodotto SFTP e/o l'aggiornamento Unified
                                    Communications Manager.

SFTP Server di un'altra terza parte

Questi server sono forniti da terze parti e non sono ufficialmente supportati da Cisco TAC.

La compatibilità delle versioni è basata sul massimo sforzo per stabilire versioni SFTP compatibili e versioni di Emergency
                                    Responder.

Nota

Questi prodotti non sono stati testati da Cisco e non possiamo garantirne la funzionalità. Cisco TAC non supporta questi prodotti.
                                             Per una soluzione SFTP completamente testata e supportata, utilizzare Cisco Prime Collaboration Deployment o un partner tecnologico.

### SAML SSO Support

Sebbene l'infrastruttura Cisco Collaboration possa rivelarsi compatibile con altri IdP che dichiarano la conformità SAML 2.0,
                        solo i seguenti IdP sono stati testati con le soluzioni Cisco Collaboration:

Microsoft ® Active Directory ®Federation Services 2.0 , 3.0, 4.0 e 5.0

Microsoft ID Entra

Okta 2017,38

OpenAM 10.0.1

PingFederate ® 6.10.0.4

F5 BIG-IP 11.6.0

Per ulteriori informazioni su SAML SSO, vedere # SAML SSO Deployment Guide for Cisco Unified Communications Applications .

### API e pacchetti di connessione sicura

Nella tabella seguente vengono fornite informazioni sui pacchetti di sviluppo API e connessione protetta supportati con questa
                        release.

Tipo di pacchetto

Dettagli

API Sviluppo

Le release 15 e 15SU1 di Cisco Unified Communications Manager e il servizio IM and Presence supportano OpenJDK versione 1.8.0.362
                                          per lo sviluppo di applicazioni.

La release 15SU2 di Cisco Unified Communications Manager e il servizio IM and Presence supportano OpenJDK versione 1.8.0.402
                                          per lo sviluppo di applicazioni.

La release 15SU3 di Cisco Unified Communications Manager e il servizio IM and Presence supportano OpenJDK versione 1.8.0.362
                                          per lo sviluppo di applicazioni.

TLS Collegamenti

Per le connessioni Transport Layer Security (TLS), questa release supporta CiscoSSL 1.1.1za.7.3.404.

Client SSH

Le release 15 e 15SU1 supportano CiscoSSH 1.10.32 basato su OpenSSH_8.8p1.

La release 15SU2 supporta CiscoSSH 1.14.56 basato su OpenSSH_9.6p1.

La release 15SU3 supporta CiscoSSH 1.16.65 basato su OpenSSH_9.9p1.

Nota

Per ulteriori informazioni sui pacchetti installati nel sistema, eseguire il comando show packages active CLI. Per ulteriori informazioni su questo comando e sulle relative opzioni, vedere la Guida di riferimento dell'interfaccia della riga di comando Cisco Unified Communications Solutions .

### Cifrari supportati per Unified Communications Manager

I seguenti cifrari sono supportati da Unified Communications Manager:

Applicazione / Processo

Protocollo

Port

Crittografie supportate

Cisco CallManager

TCP / TLS

2443

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256
AES256-SHA256:
AES128-SHA256
AES256-SHA:
AES128-SHA:
```

DRS

TCP / TLS

4040

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
```

Cisco Tomcat

TCP / TLS

8443 / 443

```
ECDHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-SHA256:
ECDHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: 
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA:
```

Cisco CallManager

TCP / TLS

5061

```
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-ECDSA-AES128-SHA:
ECDHE-RSA-AES128-SHA
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
```

Cisco Certificate Authority Funzione proxy

TCP / TLS

3804

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
```

CTIManager

TCP / TLS

2749

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
```

Cisco Servizio di verifica dell'attendibilità

TCP / TLS

2445

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256
```

```
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
```

Cisco Intercluster Lookup Service

TCP / TLS

7501

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
```

Download della configurazione protetta (HAPROXY)

TCP / TLS

6971, 6972

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA:
```

Ricerca contatti autenticata

TCP / TLS

9443

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA:
```

### Crittografie supportate per SSH

I seguenti cifrari sono supportati da SSH:

Servizio

Cifrari/Algoritmi

server SSH

Cifrature

```
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com
```

MAC algoritmi:

```
hmac-sha2-256
hmac-sha2-512
```

Algoritmi di Kex:

```
ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512
```

Algoritmi della chiave host:

```
rsa-sha2-256
rsa-sha2-512
```

SSH Client

Cifre:

```
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com
```

MAC algoritmi:

```
hmac-sha2-256
hmac-sha2-512
```

Algoritmi di Kex:

```
ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512
```

Algoritmi della chiave host:

```
rsa-sha2-256
rsa-sha2-512
```

DRS Client

Cifre:

```
aes256-ctr
aes128-ctr
aes192-ctr
```

MAC algoritmi:

```
hmac-sha2-256
```

```
ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512
```

SFTP client

Cifre:

```
aes128-ctr
aes256-ctr
aes192-ctr
```

MAC algoritmi:

```
hmac-sha2-256 
hmac-sha2-512
```

Algoritmi di Kex:

```
ecdh-sha2-nistp521 
ecdh-sha2-nistp384  
diffie-hellman-group1-sha1 
diffie-hellman-group-exchange-sha256 
diffie-hellman-group-exchange-sha1
```

Utenti finali

```
hmac-sha512
```

Backup DRS / RTMT SFTP

```
AES-128 – Encryption
```

Utenti dell'applicazione

```
AES-256 – Encryption
```

## Informazioni sulla compatibilità dei servizi IM and Presence

### Compatibilità della piattaforma

The IM and Presence Service condivide una piattaforma con Unified Communications Manager. Molti degli argomenti di compatibilità
                        per Unified Communications Manager fungono anche da argomenti di supporto per il servizio IM and Presence. È possibile fare
                        riferimento al capitolo Unified Communications Manager compatibilità per informazioni sui seguenti elementi:

Connessioni sicure

Requisiti di virtualizzazione

Directory LDAP supportate

Browser Web supportati

### Supporto per database esterni

Molte funzionalità del servizio IM and Presence, ad esempio Chat persistente, Alta disponibilità per Chat persistente, Archiviazione
                        messaggi e Trasferimento file gestito, richiedono la distribuzione di un database esterno. Per informazioni sul supporto del
                        database, vedere la Guida all'installazione del database per il servizio IM and Presence.

### Directory LDAP supportate

Sono supportate le seguenti directory LDAP:

Microsoft Active Directory su Windows Server 2016

Microsoft Active Directory su Windows Server 2019: supportato per 15 e versioni successive

Microsoft Active Directory su Windows Server 2022: supportato per 15 e versioni successive

Microsoft Lightweight Directory Services 2019 e 2022: supportato per 15 e versioni successive

Oracle Unified Directory 12cPS4

OpenLDAP Long Term Support (LTS) Release 2.5.16

Altre directory conformi a LDAPv3: Unified Communications Manager utilizza LDAPv3 standard per accedere ai dati dell'utente.
                              Assicurarsi che l'attributo supportedcontrol sia configurato nei server di directory conformi LDAPv3 da utilizzare con DirSync.
                              L'attributo supportedcontrol può restituire gli attributi secondari pagecontrolsupport e persistentcontrolsupport , se configurati.

Webex Supporto di Cloud-Connected UC Directory Service—Per ulteriori informazioni, vedere Webex Supporto di Cloud-Connected UC Directory Service per Unified CM .

### Supporto della federazione

#### SIP Federation/SIP Supporto per la federazione aperta

SIP Open Federation è supportato a partire dalla versione 12.5(1)SU3.

Nella tabella seguente sono elencate le integrazioni supportate SIP Controlled e SIP Open Federation:

Sistema di terze parti

Rete aziendale singola*

(Federazione intradominio o tra domini)

Business to Business

(Federazione tra domini)

Federazione diretta

Via Superstrada

Via Superstrada

Skype for Business 2015 (locale) **

S

Non supportato

Y (classificazione del traffico)

Office 365 (usa uno Skype for Business ospitato nel cloud)

Non applicabile

Non applicabile

Y (classificazione del traffico)

* La Single Enterprise Network può essere partizionata, federazione intradominio o federazione interdominio in quanto i valori
                        di supporto sono gli stessi per ciascuno. Le integrazioni Business to Business sono sempre federazione tra domini.

** La versione minima IM and Presence Service Release per la federazione con Skype for Business locale o Skype for Business
                        ospitato da Office 365 è la versione 11.5(1)SU2.

#### Federazioni XMPP supportate

Questa release di IM and Presence Service supporta XMPP Federation con i seguenti sistemi:

Cisco Webex Messenger

IM and Presence Service Release 11.5 (1) e versioni successive

Qualsiasi altro sistema compatibile con XMPP

### Supporto peering tra cluster

Questa versione del servizio IM and Presence supporta il peering tra cluster con le seguenti IM and Presence Service release:

Nota

Il peering tra cluster non è supportato se la versione del servizio IM and Presence è EOL/EOS.

Versione 11.5

Versione 12.x

Nota

Il peering tra cluster non è supportato tra IM and Presence Service Release 12.5(1)SU1 e 15 SU2 o versioni successive.

Release 14 e SU

Release 15 e SU

### Integrazione del calendario con Microsoft Outlook

Il servizio IM and Presence supporta l'integrazione del calendario Microsoft Outlook con un server Exchange locale o un server
                        Office 365 ospitato. Vedere la tabella seguente per informazioni sul supporto:

Componente

Installa versione compatibile

Windows Server

Windows Server 2016

Windows Server 2019: con le versioni 11.x, la Service Release IM and Presence minima è 11.5(1)SU7. Con le versioni 12.x, la
                                          Service Release IM and Presence minima è 12.5(1)SU2.

Microsoft Exchange Server 2016

Microsoft Exchange 2016

Microsoft Exchange Server 2019

Microsoft Exchange 2019

Microsoft Office 365

Vedere la documentazione Microsoft per informazioni dettagliate sulla distribuzione di un server Office 365 ospitato.

Nota

A partire da ottobre 2020, Microsoft sta modificando il meccanismo di autenticazione supportato da Exchange Online per utilizzare
                                             solo l'autenticazione basata su OAuth. Dopo la modifica, se si desidera distribuire l'integrazione del calendario tra il servizio
                                             IM and Presence e Office 365, sarà necessario aggiornare il servizio IM and Presence alla versione 12.5(1)SU2. Questa modifica
                                             non influirà sull'integrazione con un server Exchange locale.

Active Directory

Active Directory 2016 con Windows Server 2016

Nota

I nomi utente configurati in Active Directory devono essere identici ai nomi definiti in Unified Communications Manager.

Un certificato di terze parti O un server di certificazione

L'uno o l'altro di questi è necessario per generare i certificati.

Nota

Microsoft Exchange l'integrazione con IM and Presence Service supporta i certificati che utilizzano chiavi RSA a 1024 o 2048
                                                bit e algoritmi di firma SHA1 e SHA256.

### Crittografie supportate per il servizio IM and Presence

IM and Presence servizio supporta le seguenti crittografie:

Applicazione / Processo

Protocollo

Port

Crittografie supportate

Cisco SIP Proxy

TCP / TLS

5061

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco SIP Proxy

TCP / TLS

5062

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco SIP Proxy

TCP / TLS

8083

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco Tomcat

TCP / TLS

8443, 443

```
ECDHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-SHA256:
ECDHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA256:
ECDHE-RSA-AES256-SHA:
ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA:
```

Cisco XCP XMPP Federation Connection Manager

TCP /TLS

5269

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
```

Cisco XCP Client Connection Manager

TCP / TLS

5222

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
```

| Data | Revisione |
|---|---|
| 14 agosto 2025 | Versione di supporto aggiornata per Unified CM Release 15SU3a. |
| 31 luglio 2025 | Pubblicazione della guida iniziale per 15SU3. |
| 31 luglio 2025 | Supporto della versione aggiornato per 15SU3. |
| 31 luglio 2025 | Informazioni aggiornate su API e sui pacchetti di connessione protetta. |
| 31 luglio 2025 | Aggiornato l'elenco dei cifrari per Unified CM e IM and Presence Service. |
| 27 maggio 2025 | È stata aggiornata la sezione "Supporto peering intercluster". |
| 17 marzo 2025 | Aggiunto il supporto per Cisco Board Pro 55 G2 e Cisco Board Pro 75 G2 dalla release 15SU1 in poi. |
| 01 ottobre 2024 | Pubblicazione della guida iniziale per 15SU2. |
| 01 ottobre 2024 | Supporto della versione aggiornato per 15SU2. |
| 01 ottobre 2024 | Aggiunto il supporto per Cisco Desk Phone serie 9800. |
| 01 ottobre 2024 | Informazioni aggiornate su API e Secure Connection Packages. |
| 01 ottobre 2024 | Aggiornato l'elenco dei cifrari per Unified CM. |
| 20 giugno 2024 | Versione di supporto aggiornata per Unified CM Release 15SU1a. |
| 28 marzo 2024 | Aggiunto il supporto della versione per 15SU1. |
| 28 marzo 2024 | Informazioni aggiornate su API e Secure Connection Packages per 15SU1. |
| 18 dicembre 2023 | Aggiunto il supporto della versione per la versione 15. |
| 18 dicembre 2023 | Informazioni aggiornate sul supporto della directory LDAP. |
| 18 dicembre 2023 | Sezione Browser supportati aggiornata. |
| 18 dicembre 2023 | È stato rimosso il supporto per Active Directory 2012 con Windows Server 2012 dalla sezione "Integrazione del calendario con
                              Microsoft Outlook". |
| 18 dicembre 2023 | È stato rimosso il supporto per "Controllo chiamate remote con server Microsoft Lync" per IM and Presence servizio in quanto
                              Microsoft Lync Server 2013 ha superato la fine del supporto principale (EOS) di Microsoft datata 10 aprile 2018 e anche esteso
                              EOS datato 11 aprile 2023. |

| Nota | Salvo diversa indicazione, ogni categoria di release include le release SU all'interno di tale categoria. |
|---|---|

| Nota | Sebbene non sia obbligatorio, si consiglia di eseguire il file COP Upgrade Readiness prima dell'aggiornamento per massimizzare
                              la riuscita dell'aggiornamento. Cisco TAC potrebbe richiedere l'esecuzione di questo file COP per fornire un supporto tecnico
                              efficace. |
|---|---|

| Nota | Se l'origine è in modalità FIPS e/o PCD in modalità FIPS, vedere https://www.cisco.com/web/software/286319173/139477/ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop-ReadMe.pdf per informazioni sul file COP ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop . Questo documento descrive in dettaglio i prerequisiti necessari per l'aggiornamento diretto o la migrazione diretta alle
                              versioni di destinazione 15 o successive. |
|---|---|

| Nota | Se dalla release di origine è disponibile un aggiornamento standard diretto alla versione 15 o successiva, è possibile scegliere
                                 un aggiornamento a nodo singolo o a livello di cluster. Se si desidera aggiornare un intero cluster e si prevede una durata minima, tempi di inattività, impatto sul servizio o interventi
                                 amministrativi, utilizzare la procedura "Clusterwide Upgrade Task Flow (Direct Standard)" che descrive in dettaglio l'aggiornamento
                                 del cluster tramite Unified CM Publisher utilizzando l'aggiornamento di Unified OS Admin o l'aggiornamento CLI. Qui, aggiornerai
                                 solo il Unified CM Publisher e orchestra l'aggiornamento o il riavvio di tutti gli altri nodi del cluster. Se si prevede di aggiornare l'origine nodo per nodo o di utilizzare un singolo nodo solo utilizzando l'aggiornamento locale
                                 di Unified OS Admin o l'aggiornamento CLI, vedere la sezione "Aggiornamento dei nodi cluster (Direct Standard)". Per ulteriori
                                 informazioni, vedere la Guida all'aggiornamento e alla migrazione per Cisco Unified Communications Manager e il servizio IM and Presence . |
|---|---|

| Nota | È necessario assicurarsi che il piano di aggiornamento segua le regole di sequenziazione dei nodi menzionate nella Guida all'aggiornamento https://www-author3.cisco.com/content/en/us/td/docs/voice_ip_comm/cucm/upgrade/15/cucm_b_upgrade-and-migration-guide_15/cucm_m_sequencing-rules-time-requirements-15.html#reference_3E039AF4416B1F56A9F9E5D7DF25344B . Prima di cambiare versione nei nodi IM and Presence Service, è necessario cambiare i nodi Unified Communications Manager,
                                 iniziando dal nodo di pubblicazione e quindi dai nodi del sottoscrittore. Se non si segue la sequenza menzionata e quindi se il nodo Unified Communications Manager Publisher passa alla versione 15
                                 o successiva e la versione del nodo IM and Presence Service Publisher è ancora nelle versioni 12.5.x o 14 e SU e non viene
                                 aggiornata, le pagine seguenti nel menu Aggiornamenti software non verranno visualizzate né funzioneranno per i nodi del servizio
                                 IM and Presence: Cluster di riavvio/cambio versione Posizione del software cluster Cluster di installazione e aggiornamento software |
|---|---|

| Nota | Non esistono percorsi supportati da Direct Refresh Upgrade per Unified Communications Manager e IM and Presence Service Release
                              15 e versioni successive. L'aggiornamento degli aggiornamenti dall'origine precedente alla 12.5.x alla release 15 e successive
                              non è supportato. |
|---|---|

| Origine | Destinazione | Meccanismo | Pre-requisiti | Cambio di versione* (dall'origine alla destinazione e viceversa) |
|---|---|---|---|---|
| 10.0 | 15 | Attività di migrazione PCD 15 (V2V) | L'aggiornamento diretto a 15 non è supportato. Quando la versione di destinazione è 15 o superiore e la versione di origine
                                 è 10.0, per la migrazione è necessario utilizzare la distribuzione Cisco Prime Collaboration (PCD). Se la versione di destinazione è 15 o superiore e la versione di origine 10.0 è in modalità FIPS, la distribuzione Cisco Prime
                                 Collaboration (PCD) deve essere in modalità non FIPS. | Non applicabile |
| 10.5 | 15 | Attività di migrazione PCD 15 (V2V) | Eseguire il file COP pre-upgrade-check. È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione. L'aggiornamento diretto a 15 non è supportato. Quando la versione di destinazione è 15 o superiore e la versione di origine
                                 è 10.5, per la migrazione è necessario utilizzare la distribuzione Cisco Prime Collaboration (PCD). Se la versione di destinazione è 15 o superiore e la versione di origine 10.5 è in modalità FIPS, allora: Il PCD deve essere in (o inserito) in modalità non FIPS. Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD. | Non applicabile |
| Nuova installazione con importazione dati (V2V) | Eseguire il file COP pre-upgrade-check. Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 Ciscocm. DataExport_v1.0.cop.sgn | Non supportato |
| 11.0 | 15 | Attività di migrazione PCD 15 (V2V) | Eseguire il file COP pre-upgrade-check. È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione. Se la versione di destinazione è 15 o superiore e la versione di origine 11.0 è in modalità FIPS, allora: Il PCD deve essere in (o inserito) in modalità non FIPS. Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD. | Non supportato |
| Nuova installazione con importazione dati (V2V) | Eseguire il file COP pre-upgrade-check. Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 Ciscocm. DataExport_v1.0.cop.sgn | Non supportato |
| 11.5 | 15 | Attività di migrazione PCD 15 (V2V) | Eseguire il file COP pre-upgrade-check. È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione. Se la versione di destinazione è 15 o superiore e la versione di origine 11.5 è in modalità FIPS, allora: Il PCD deve essere in (o inserito) in modalità non FIPS. Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD. | Non supportato |
| Nuova installazione con importazione dati (V2V) | Eseguire il file COP pre-upgrade-check. Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 Ciscocm. DataExport_v1.0.cop.sgn | Non supportato |
| 12.0 | 15 | Attività di migrazione PCD 15 (V2V) | Eseguire il file COP pre-upgrade-check. È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione. Se la versione di origine è la Release 12.0 (1) di Unified Communications Manager (12.0.1.10000-10), è necessario installare
                                 il seguente file COP: ciscocm-slm-migration.k3.cop.sgn . Questo non è necessario se la versione di origine è superiore, ad esempio, Release 12.0(1)SU1. | Non supportato |
| Nuova installazione con importazione dati (V2V) | Eseguire il file COP pre-upgrade-check. Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 Ciscocm. DataExport_v1.0.cop.sgn | Non supportato |
| 12.5 | 15 | Aggiornamento standard diretto (aggiornamenti semplici) | Tramite OS Admin o CLI | Eseguire il file COP pre-upgrade-check. | Supportato |
| Aggiornamento standard diretto | Tramite attività di aggiornamento PCD 15 | Eseguire il file COP pre-upgrade-check. Se l'origine Unified CM è precedente a 12.5.1.14900-63, installare il seguente file COP: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn . Se l'origine del servizio IM and Presence è precedente a 12.5.1.14900-4, installare il seguente file COP: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn . Se la versione di destinazione è 15 o superiore e la versione di origine 12.5 è in modalità FIPS, allora: Il PCD deve essere in (o inserito) in modalità non FIPS. Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di aggiornamento PCD. Se si utilizza Cisco Prime Collaboration Deployment per aggiornare un cluster di IM and Presence Service dalla versione 12.5.x
                                       alla release 15 o successiva, è necessario installare il seguente file COP sui sistemi della release 12.5.x prima di iniziare
                                       l'aggiornamento: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512 . Si noti che il file COP è applicabile solo se: Unified Communications Manager versione di destinazione è nella Release 15 o superiore. Unified Communications Manager versione di destinazione è nella versione 15 o successiva e si sta tentando di aggiornare l'origine
                                             del servizio IM and Presence da una versione con restrizioni a una versione senza restrizioni. | Supportato |
| Attività di migrazione PCD 15 (V2V) | Eseguire il file COP pre-upgrade-check. È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione. Se la versione di destinazione è 15 o superiore e la versione di origine 12.5 è in modalità FIPS, allora: Il PCD deve essere in (o inserito) in modalità non FIPS. Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD. | Non supportato |
| Nuova installazione con importazione dati (V2V) | Eseguire il file COP pre-upgrade-check. Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 Ciscocm. DataExport_v1.0.cop.sgn | Non supportato |
| 14 e SU | 15 | Aggiornamento standard diretto (aggiornamenti semplici) | Tramite OS Admin o CLI | Eseguire il file COP pre-upgrade-check. Nota Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. | Nota | Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. | Supportato |
| Nota | Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. |
| Aggiornamento standard diretto | Tramite attività di aggiornamento PCD | Eseguire il file COP pre-upgrade-check. Se la versione di destinazione è 15 o superiore e la versione di origine è 14 e SU in modalità FIPS, allora: Il PCD deve essere in (o inserito) in modalità non FIPS. Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di aggiornamento PCD. Se si utilizza Cisco Prime Collaboration Deployment per aggiornare un cluster del servizio IM and Presence dalla Release 14
                                       o SU alla Release 15 o successiva, è necessario installare il seguente file COP nei sistemi Release 14 o SU prima di iniziare
                                       l'aggiornamento: ciscocm.imp15_upgrade_v1.0.k4.cop.sha512 . Si noti che il file COP è applicabile solo se: Unified Communications Manager versione di destinazione è nella versione 15 o superiore e i nodi di origine del servizio IM
                                             and Presence sono nelle versioni 14 o 14SU1. Unified Communications Manager versione di destinazione è nella versione 15 o successiva e si sta tentando di aggiornare l'origine
                                             del servizio IM and Presence da una versione con restrizioni a una versione senza restrizioni. Nota Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. | Nota | Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. | Supportato |
| Nota | Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. |
| Attività di migrazione PCD 15 (V2V) | Eseguire il file COP pre-upgrade-check. È necessario installare ciscocm . CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 COP prima della migrazione. Se la versione di destinazione è 15 o superiore e la versione di origine è 14 o SU in modalità FIPS, allora: Il PCD deve essere in (o inserito) in modalità non FIPS. Utilizzare Nuova installazione con importazione dati anziché utilizzare l'attività di migrazione PCD. | Non supportato |
| Nuova installazione con importazione dati (V2V) | Eseguire il file COP pre-upgrade-check. Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 Ciscocm. CSCwi52160_15-direct-migration_v1.0.k4.cop.sha512 Ciscocm. DataExport_v1.0.cop.sgn | Non supportato |

| Nota | Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. |
|---|---|

| Nota | Gli aggiornamenti dalla Release 14SU4 a qualsiasi cluster Unified Communications Manager o IM and Presence Service con versioni
                                             di destinazione inferiori alla Release 15SU2, ovvero 15 o 15SU1a, non sono supportati e non verranno visualizzati come opzione
                                             di aggiornamento valida. È necessario aggiornare l'origine 14SU4 alla versione 15SU2 o successiva come aggiornamento di destinazione.
                                             Fare riferimento a CSCwi85184 per ulteriori dettagli. |
|---|---|

| Nota | Aggiornamenti e migrazioni PCD: per tutti i percorsi supportati utilizzando l'attività di aggiornamento PCD o l'attività di
                              migrazione PCD nella tabella precedente, è necessario utilizzare PCD Release 15. |
|---|---|

| Per questa versione... | Sono supportate le seguenti versioni... |
|---|---|
| 15 | Unified Communications Manager 15.0.1.10000-32 Servizio IM and Presence 15.0.1.10000-10 |
| 15SU1a | Unified Communications Manager Versione 15SU1a: 15.0.1.11901-2 IM and Presence Service Release 15SU1: 15.0.1.11900-4 |
| 15SU2 | Unified Communications Manager 15.0.1.12900-234 Servizio IM and Presence 15.0.1.12900-10 |
| 15SU3 | Unified Communications Manager 15.0.1.13901-2 Servizio IM and Presence 15.0.1.13900-6 |

| Nota | Qualsiasi respin o ES prodotto tra le versioni Cisco.com è considerato parte della versione precedente. Ad esempio, un ES Unified Communications Manager con un numero di build di
                                 15.0.1.13[0-2]xx sarebbe considerato parte della versione 15 (15.0.1.10900-x). |
|---|---|

| Tipo distribuzione | Rilascio non corrispondente | Descrizione |
|---|---|---|
| Distribuzione standard del servizio IM and Presence | Non supportato | Unified Communications Manager e il servizio IM and Presence si trovano nello stesso cluster e devono eseguire la stessa versione:
                                    una mancata corrispondenza delle versioni non è supportata. |
| Distribuzione centralizzata del servizio IM and Presence | Supportato | La distribuzione del servizio IM and Presence e la distribuzione di telefonia si trovano in cluster diversi e possono eseguire
                                    versioni diverse: è supportata una mancata corrispondenza delle versioni. Nota Il cluster centrale IM and Presence Service include anche un nodo Unified CM Publisher autonomo per il provisioning di database
                                             e utenti. Questo nodo non di telefonia deve eseguire la stessa release del servizio IM and Presence. | Nota | Il cluster centrale IM and Presence Service include anche un nodo Unified CM Publisher autonomo per il provisioning di database
                                             e utenti. Questo nodo non di telefonia deve eseguire la stessa release del servizio IM and Presence. |
| Nota | Il cluster centrale IM and Presence Service include anche un nodo Unified CM Publisher autonomo per il provisioning di database
                                             e utenti. Questo nodo non di telefonia deve eseguire la stessa release del servizio IM and Presence. |

| Nota | Il cluster centrale IM and Presence Service include anche un nodo Unified CM Publisher autonomo per il provisioning di database
                                             e utenti. Questo nodo non di telefonia deve eseguire la stessa release del servizio IM and Presence. |
|---|---|

| Nota | Queste informazioni sulla compatibilità non sono applicabili per Cisco Webex. |
|---|---|

| Unified Communications Manager e IM and Presence versione del servizio | Versione Expressway | Unified Communications Mobile e Remote Access | Distribuzioni locali |
|---|---|---|---|
| Tutti i cluster su: 11.5(1)SU8 o versioni precedenti 12.5(1)SU2 o versioni precedenti | X12.6.2 | Android La notifica push non è supportata | Android La notifica push non è supportata |
| Tutti i cluster su: 12.5(1)SU3 e successivi | X12.6.2 | Abilita notifica push Android tramite CLI xConfiguration XCP Config FcmService: attivato su Expressway solo per la messaggistica | Android La notifica push è supportata |
| Cluster con versioni miste (11.5(1)SU8 o versioni precedenti, OPPURE 12.5(1)SU2 o versioni precedenti E 12.5(1)SU3 e successive) | X12.6.2 | Android La notifica push per la messaggistica non è supportata VoIP è supportato dalla release 12.5(1)SU3 in poi | Android La notifica push è supportata dalla release 12.5(1)SU3 in poi |

| Nota | Apple Push Notification Service (APNS) non è interessato dallo stato del flag di servizio FCM. |
|---|---|

| Versioni miste IM and Presence cluster | Stato previsto del flag FCM su Expressway X12.7 | Commento |
|---|---|---|
| Qualsiasi 11.5(1)SU con 12.5(1)SU2 e inferiori | OFF | Android Push (FCM) NON supportato. |
| 11.5(1)SU8 (e inferiore) o 12.5(1)SU2 (e inferiore) con 12.5(1)SU3 o 14 | OFF | Android push (FCM) NON supportato |
| 11.5(1)SU8 (e versioni precedenti) o 12.5(1)SU2 (e inferiori) con 12.5(1)SU4 (e superiori) o 14SU1 (e superiori) | OFF | Android push (FCM) supportato nelle versioni 12.5(1)SU4 (o più recenti) |
| 11.5(1)SU9 (e superiore) o 12.5(1)SU4 (e superiore) con 12.5(1)SU3 o 14SU1 (e superiore) | ON | Android push (FCM) supportato sulla versione 12.5(1)SU3 e successive |
| 11.5(1)SU9 (e superiore) con 12.5(1)SU4 (e superiore) o 14SU1 (e superiore) | Flag non richiesto (Expressway 12.7 si basa completamente sul nuovo meccanismo di rilevamento) | Android push (FCM) supportato nelle versioni 12.5(1)SU4 (o più recenti) |

| Nota | Cisco non rilascerà correzioni di bug o miglioramenti della sicurezza per gli endpoint che hanno raggiunto lo stato di Fine
                                    della manutenzione software o Fine del supporto, indipendentemente dal fatto che tali endpoint siano deprecati o meno. Cisco
                                    non testerà Unified Communications Manager con i telefoni End of Life. Né risolveremo i bug Unified Communications Manager
                                    relativi ai telefoni End of Life a meno che il problema non possa essere replicato su un telefono che non è End of Life. |
|---|---|

| Serie di dispositivi | Modello dispositivo |
|---|---|
| Cisco Unified SIP Phone serie 3900 | Telefono SIP Cisco Unified 3905 |
| Telefono IP Cisco Unified serie 6900 | Telefono IP Cisco Unified 6901 |
| Telefono IP Cisco serie 7800 | Telefono IP Cisco 7811 Telefono IP Cisco 7821 Telefono IP Cisco 7841 Telefono IP Cisco 7861 Telefono IP per chiamate in conferenza Cisco 7832 |
| Telefono IP Cisco Unified serie 7900 | Cisco Unified IP Phone Modulo di espansione 7915— Avviso EOS Cisco Unified IP Phone Modulo di espansione 7916— Avviso EOS Cisco Unified IP Phone 7942G— Avviso EOS Cisco Unified IP Phone 7945G— Avviso EOS Cisco Unified IP Phone 7962G— Avviso EOS Cisco Unified IP Phone 7965G— Avviso EOS Cisco Unified IP Phone 7975G— Avviso EOS |
| Telefono IP Cisco serie 8800 | Cisco IP Phone 8811, 8831, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR Cisco Wireless IP Phone 8821, 8821-EX— Avviso EOL Cisco Unified IP Telefono conferenza 8831— Avviso EOS Telefono IP per chiamate in conferenza Cisco 8832 Videotelefono Cisco 8875 Cisco Video Phone 8875NR |
| Telefono IP Cisco Unified serie 8900 | Cisco Unified IP Phone 8945— Avviso EOS Cisco Unified IP Phone 8961— Avviso EOS |
| Telefono IP Cisco Unified serie 9900 | Cisco Unified IP Phone 9951— Avviso EOS Cisco Unified IP Phone 9971— Avviso EOS |
| Cisco Telefono fisso serie 9800 | Cisco Telefono fisso 9841 Cisco Telefono fisso 9851 Cisco Telefono fisso 9861 Cisco Telefono fisso 9871 Cisco Modulo di espansione chiavi 9800 per telefono fisso (KEM) |
| Cisco Jabber | Cisco Jabber per Android Cisco Jabber per iPhone e iPad Cisco Jabber per Mac Cisco Jabber per Windows Cisco Jabber Softphone per VDI - Windows (in precedenza  Cisco Virtualization Experience Media Edition per Windows) Cisco Jabber Guest Cisco Jabber Software Development Kit Cisco Jabber per Tablet |
| Serie di cuffie Cisco | Cuffia Cisco 320 Cuffia Cisco 520 Cuffia Cisco 530 Cuffia Cisco 560 Cuffia Cisco 720 Cuffia Cisco 730 |
| Cisco IP Communicator | Cisco IP Communicator— Avviso EOS |
| Webex | App Webex Webex Room Phone Webex Desk Cisco Desk Camera 4K Cisco Desk Camera 1080p Webex Desk Hub Webex Desk Pro Webex Desk Edizione limitata Webex Share— Avviso EOS Board 55, 55S, 70, 70S, 85, 85S Board Pro 55 G2 e 75 G2 Webex Room Panorama Webex Room 70 Panorama Webex Room 70 Panorama Aggiornamento Room 70 Room 70 G2 Room 55 Dual sale 55 Room Kit Pro Room Kit Plus Room Kit Room Kit Mini Webex Room USB |
| Telefono wireless Webex serie 800 | Webex Telefono senza fili 840 Telefono wireless Webex 860 |
| Webex Meetings | Webex Meetings per iPhone e iPad Webex Meetings per Android |
| Cisco Adattatori per telefonia analogica | Cisco Adattatori telefonici analogici serie ATA 190 - Avviso EOS/EOL Cisco Adattatori telefonici analogici serie ATA 191 |
| Cisco serie DX | Cisco Webex DX70 - Avviso EOS Cisco Webex DX80— Avviso EOS Cisco DX650— Avviso EOS |
| Cisco TelePresence IX5000 | Cisco TelePresence IX5000 |
| Cisco TelePresence Serie EX | Cisco TelePresence System EX90 - Avviso EOS |
| Cisco TelePresence serie MX | Cisco TelePresence MX200 G2 - Avviso EOS Cisco TelePresence MX300 G2— Avviso EOS Cisco TelePresence MX700D - Avviso EOS Cisco TelePresence MX800S - Avviso EOS Cisco TelePresence MX800D - Avviso EOS |
| Cisco TelePresence serie SX | Cisco TelePresence SX10 - Avviso EOS Cisco TelePresence SX20 - Avviso EOS Cisco TelePresence SX80 - Avviso EOS |

| Cisco Endpoint alla fine del supporto |
|---|
|  |

| Modelli di telefono obsoleti per questa release | Deprecato per la prima volta a partire da Unified CM... |
|---|---|
| Nessun endpoint aggiuntivo deprecato | Versione 15 |
| Nessun endpoint aggiuntivo deprecato | Versione 14 |
| Cisco Unified Wireless IP Phone 7921 Telefono IP Cisco Unified 7970 Telefono IP Cisco Unified 7971 | 12.0 (1) e versioni successive |
| Cisco IP Phone 12 S Cisco IP Phone 12 SP Cisco IP Phone 12 SP+ Cisco IP Phone 30 SP+ Cisco IP Phone 30 VIP Telefono IP Cisco Unified 7902G Telefono IP Cisco Unified 7905G Telefono IP Cisco Unified 7910 Telefono IP Cisco Unified 7910G Cisco Unified IP Phone 7910+SW Cisco Unified IP Phone 7910G+SW Telefono IP Cisco Unified 7912G Cisco Unified Wireless IP Phone 7920 Cisco Unified IP Conference Station 7935 | 11.5 (1) e versioni successive |

| Requisiti di virtualizzazione per... | Per informazioni, vai a... |
|---|---|
| Unified Communications Manager | Per informazioni sui requisiti di virtualizzazione Unified Communications Manager, vedere https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-communications-manager.html . |
| IM e servizio di presenza | Per informazioni sui requisiti di virtualizzazione del servizio IM and Presence, vedere https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-ucm-im-presence.html . |
| Cisco Business Edition Distribuzioni | Per informazioni sui requisiti di virtualizzazione per Unified Communications Manager in una distribuzione di una soluzione
                                    di collaborazione come Cisco Business Edition, vedere quanto segue: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html Cisco Business Edition 7000 Cisco Business Edition 6000 |

| Nota | Si consiglia di utilizzare la versione più recente per tutti i browser Web supportati. |
|---|---|

| server SFTP | Descrizione del supporto |
|---|---|
| Server SFTP nella distribuzione Cisco Prime Collaboration | Questo server è l'unico server SFTP fornito e testato da Cisco e completamente supportato da Cisco TAC. La compatibilità della versione dipende dalla versione di Emergency Responder e dalla distribuzione Cisco Prime Collaboration
                                    in uso. Vedere la Cisco Prime Collaboration Deployment Administration Guide prima di aggiornare la versione (SFTP) o Emergency
                                    Responder per assicurarsi che le versioni siano compatibili. |
| SFTP Server da un partner tecnologico | Questi server sono forniti da terze parti e testati da terze parti. La compatibilità della versione dipende dal test di terze
                                    parti. Fare riferimento alla pagina del partner tecnologico se si aggiorna il loro prodotto SFTP e/o l'aggiornamento Unified
                                    Communications Manager. |
| SFTP Server di un'altra terza parte | Questi server sono forniti da terze parti e non sono ufficialmente supportati da Cisco TAC. La compatibilità delle versioni è basata sul massimo sforzo per stabilire versioni SFTP compatibili e versioni di Emergency
                                    Responder. Nota Questi prodotti non sono stati testati da Cisco e non possiamo garantirne la funzionalità. Cisco TAC non supporta questi prodotti.
                                             Per una soluzione SFTP completamente testata e supportata, utilizzare Cisco Prime Collaboration Deployment o un partner tecnologico. | Nota | Questi prodotti non sono stati testati da Cisco e non possiamo garantirne la funzionalità. Cisco TAC non supporta questi prodotti.
                                             Per una soluzione SFTP completamente testata e supportata, utilizzare Cisco Prime Collaboration Deployment o un partner tecnologico. |
| Nota | Questi prodotti non sono stati testati da Cisco e non possiamo garantirne la funzionalità. Cisco TAC non supporta questi prodotti.
                                             Per una soluzione SFTP completamente testata e supportata, utilizzare Cisco Prime Collaboration Deployment o un partner tecnologico. |

| Nota | Questi prodotti non sono stati testati da Cisco e non possiamo garantirne la funzionalità. Cisco TAC non supporta questi prodotti.
                                             Per una soluzione SFTP completamente testata e supportata, utilizzare Cisco Prime Collaboration Deployment o un partner tecnologico. |
|---|---|

| Tipo di pacchetto | Dettagli |
|---|---|
| API Sviluppo | Le release 15 e 15SU1 di Cisco Unified Communications Manager e il servizio IM and Presence supportano OpenJDK versione 1.8.0.362
                                          per lo sviluppo di applicazioni. La release 15SU2 di Cisco Unified Communications Manager e il servizio IM and Presence supportano OpenJDK versione 1.8.0.402
                                          per lo sviluppo di applicazioni. La release 15SU3 di Cisco Unified Communications Manager e il servizio IM and Presence supportano OpenJDK versione 1.8.0.362
                                          per lo sviluppo di applicazioni. |
| TLS Collegamenti | Per le connessioni Transport Layer Security (TLS), questa release supporta CiscoSSL 1.1.1za.7.3.404. |
| Client SSH | Le release 15 e 15SU1 supportano CiscoSSH 1.10.32 basato su OpenSSH_8.8p1. La release 15SU2 supporta CiscoSSH 1.14.56 basato su OpenSSH_9.6p1. La release 15SU3 supporta CiscoSSH 1.16.65 basato su OpenSSH_9.9p1. |

| Nota | Per ulteriori informazioni sui pacchetti installati nel sistema, eseguire il comando show packages active CLI. Per ulteriori informazioni su questo comando e sulle relative opzioni, vedere la Guida di riferimento dell'interfaccia della riga di comando Cisco Unified Communications Solutions . |
|---|---|

| Applicazione / Processo | Protocollo | Port | Crittografie supportate |
|---|---|---|---|
| Cisco CallManager | TCP / TLS | 2443 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256
AES256-SHA256:
AES128-SHA256
AES256-SHA:
AES128-SHA: |
| DRS | TCP / TLS | 4040 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: |
| Cisco Tomcat | TCP / TLS | 8443 / 443 | ECDHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-SHA256:
ECDHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: 
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: |
| Cisco CallManager | TCP / TLS | 5061 | ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-ECDSA-AES128-SHA:
ECDHE-RSA-AES128-SHA
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: |
| Cisco Certificate Authority Funzione proxy | TCP / TLS | 3804 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: |
| CTIManager | TCP / TLS | 2749 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: |
| Cisco Servizio di verifica dell'attendibilità | TCP / TLS | 2445 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256 AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: |
| Cisco Intercluster Lookup Service | TCP / TLS | 7501 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA: |
| Download della configurazione protetta (HAPROXY) | TCP / TLS | 6971, 6972 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: |
| Ricerca contatti autenticata | TCP / TLS | 9443 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256: ECDHE-RSA-AES256-SHA: ECDHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: |

| Servizio | Cifrari/Algoritmi |
|---|---|
| server SSH | Cifrature aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com MAC algoritmi: hmac-sha2-256
hmac-sha2-512 Algoritmi di Kex: ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512 Algoritmi della chiave host: rsa-sha2-256
rsa-sha2-512 |
| SSH Client | Cifre: aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com MAC algoritmi: hmac-sha2-256
hmac-sha2-512 Algoritmi di Kex: ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512 Algoritmi della chiave host: rsa-sha2-256
rsa-sha2-512 |
| DRS Client | Cifre: aes256-ctr
aes128-ctr
aes192-ctr MAC algoritmi: hmac-sha2-256 Algoritmi di Kex: ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512 |
| SFTP client | Cifre: aes128-ctr
aes256-ctr
aes192-ctr MAC algoritmi: hmac-sha2-256 
hmac-sha2-512 Algoritmi di Kex: ecdh-sha2-nistp521 
ecdh-sha2-nistp384  
diffie-hellman-group1-sha1 
diffie-hellman-group-exchange-sha256 
diffie-hellman-group-exchange-sha1 |
| Utenti finali | hmac-sha512 |
| Backup DRS / RTMT SFTP | AES-128 – Encryption |
| Utenti dell'applicazione | AES-256 – Encryption |

| Sistema di terze parti | Rete aziendale singola* (Federazione intradominio o tra domini) | Business to Business (Federazione tra domini) |
|---|---|---|
| Federazione diretta | Via Superstrada | Via Superstrada |
| Skype for Business 2015 (locale) ** | S | Non supportato | Y (classificazione del traffico) |
| Office 365 (usa uno Skype for Business ospitato nel cloud) | Non applicabile | Non applicabile | Y (classificazione del traffico) |

| Nota | Il peering tra cluster non è supportato se la versione del servizio IM and Presence è EOL/EOS. |
|---|---|

| Nota | Il peering tra cluster non è supportato tra IM and Presence Service Release 12.5(1)SU1 e 15 SU2 o versioni successive. |
|---|---|

| Componente | Installa versione compatibile |
|---|---|
| Windows Server | Windows Server 2016 Windows Server 2019: con le versioni 11.x, la Service Release IM and Presence minima è 11.5(1)SU7. Con le versioni 12.x, la
                                          Service Release IM and Presence minima è 12.5(1)SU2. |
| Microsoft Exchange Server 2016 | Microsoft Exchange 2016 |
| Microsoft Exchange Server 2019 | Microsoft Exchange 2019 |
| Microsoft Office 365 | Vedere la documentazione Microsoft per informazioni dettagliate sulla distribuzione di un server Office 365 ospitato. Nota A partire da ottobre 2020, Microsoft sta modificando il meccanismo di autenticazione supportato da Exchange Online per utilizzare
                                             solo l'autenticazione basata su OAuth. Dopo la modifica, se si desidera distribuire l'integrazione del calendario tra il servizio
                                             IM and Presence e Office 365, sarà necessario aggiornare il servizio IM and Presence alla versione 12.5(1)SU2. Questa modifica
                                             non influirà sull'integrazione con un server Exchange locale. | Nota | A partire da ottobre 2020, Microsoft sta modificando il meccanismo di autenticazione supportato da Exchange Online per utilizzare
                                             solo l'autenticazione basata su OAuth. Dopo la modifica, se si desidera distribuire l'integrazione del calendario tra il servizio
                                             IM and Presence e Office 365, sarà necessario aggiornare il servizio IM and Presence alla versione 12.5(1)SU2. Questa modifica
                                             non influirà sull'integrazione con un server Exchange locale. |
| Nota | A partire da ottobre 2020, Microsoft sta modificando il meccanismo di autenticazione supportato da Exchange Online per utilizzare
                                             solo l'autenticazione basata su OAuth. Dopo la modifica, se si desidera distribuire l'integrazione del calendario tra il servizio
                                             IM and Presence e Office 365, sarà necessario aggiornare il servizio IM and Presence alla versione 12.5(1)SU2. Questa modifica
                                             non influirà sull'integrazione con un server Exchange locale. |
| Active Directory | Active Directory 2016 con Windows Server 2016 Nota I nomi utente configurati in Active Directory devono essere identici ai nomi definiti in Unified Communications Manager. | Nota | I nomi utente configurati in Active Directory devono essere identici ai nomi definiti in Unified Communications Manager. |
| Nota | I nomi utente configurati in Active Directory devono essere identici ai nomi definiti in Unified Communications Manager. |
| Un certificato di terze parti O un server di certificazione | L'uno o l'altro di questi è necessario per generare i certificati. Nota Microsoft Exchange l'integrazione con IM and Presence Service supporta i certificati che utilizzano chiavi RSA a 1024 o 2048
                                                bit e algoritmi di firma SHA1 e SHA256. | Nota | Microsoft Exchange l'integrazione con IM and Presence Service supporta i certificati che utilizzano chiavi RSA a 1024 o 2048
                                                bit e algoritmi di firma SHA1 e SHA256. |
| Nota | Microsoft Exchange l'integrazione con IM and Presence Service supporta i certificati che utilizzano chiavi RSA a 1024 o 2048
                                                bit e algoritmi di firma SHA1 e SHA256. |

| Nota | A partire da ottobre 2020, Microsoft sta modificando il meccanismo di autenticazione supportato da Exchange Online per utilizzare
                                             solo l'autenticazione basata su OAuth. Dopo la modifica, se si desidera distribuire l'integrazione del calendario tra il servizio
                                             IM and Presence e Office 365, sarà necessario aggiornare il servizio IM and Presence alla versione 12.5(1)SU2. Questa modifica
                                             non influirà sull'integrazione con un server Exchange locale. |
|---|---|

| Nota | I nomi utente configurati in Active Directory devono essere identici ai nomi definiti in Unified Communications Manager. |
|---|---|

| Nota | Microsoft Exchange l'integrazione con IM and Presence Service supporta i certificati che utilizzano chiavi RSA a 1024 o 2048
                                                bit e algoritmi di firma SHA1 e SHA256. |
|---|---|

| Applicazione / Processo | Protocollo | Port | Crittografie supportate |
|---|---|---|---|
| Cisco SIP Proxy | TCP / TLS | 5061 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco SIP Proxy | TCP / TLS | 5062 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco SIP Proxy | TCP / TLS | 8083 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco Tomcat | TCP / TLS | 8443, 443 | ECDHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-SHA256:
ECDHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA256:
ECDHE-RSA-AES256-SHA:
ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-SHA:
AES256-GCM-SHA384:
AES128-GCM-SHA256:
AES256-SHA256:
AES128-SHA256:
AES256-SHA:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: |
| Cisco XCP XMPP Federation Connection Manager | TCP /TLS | 5269 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: |
| Cisco XCP Client Connection Manager | TCP / TLS | 5222 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: |