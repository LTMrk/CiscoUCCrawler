---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-216691-call-center-call-forward-not-available-html-b30b89aa3e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/216691-call-center-call-forward-not-available.html
retrieved_at: 2026-09-07T13:02:53.961481+00:00
---

Call Center - Call Forward Not Available - Need to use Call Forward Busy

# Call Center - Call Forward Not Available - Need to use Call Forward Busy

### Download Options

Updated: November 11, 2020

Document ID: 216691

Contents

## Contents

CFGNA – Hunt Group – Assign CFB when using simultaneous ring option

When setting up call forwarding for a hunt group you need to use CFB instead of CFGNA when using the Simultaneous hunt type. Below is an explanation:

Here is an example with two agents assigned to a call cfenter:

```
2010.05.13 17:30:10:274 GMT+00:00 | Info | CallP | Service | State Engine | +14439510409 | 90103-G6109080 | localHost40149832 Trying agent: 101 2010.05.13 17:30:10:274 GMT+00:00 | Info | CallP | Service | State Engine | +14439510409 | 90103-CG6109080 | localHost40149832 Trying agent: 102
```

The two agents are not registered per the local outage (for example) :

```
2010.05.13 17:30:10:276 GMT+00:00 | Info | CallP | SIP Endpoint | 14105526501x102 | 90103-G6109080 | localHost40149837:0 Transforming Event: com.broadsoft.events.iwp.ConnectRequestEvent {CHCallManager.localHost40149837,SipEndpoint.localHost40149837:0} 2010.05.13 17:30:10:276 GMT+00:00 | FieldDebug | CallP | Endpoint | 14105526501x101 | 90103-G6109080 | localHost40149835:0 ReleaseWithCauseEvent (cause=TEMPORARILY_UNAVAILABLE) created Thread \"Call Half Input Adapter 1\" stack elements: 1: com.broadsoft.events.callhalf.ReleaseWithCauseEvent.<init>(ReleaseWithCauseEvent.java:202) 2: com.broadsoft.events.callhalf.ReleaseWithCauseEvent.<init>(ReleaseWithCauseEvent.java:121) 3: com.broadsoft.sessionmanagers.sipcallhalf.transformer.ConnectRequestEventTransformer.transform(ConnectRequestEventTrans former.java:246) 4: com.broadsoft.sessionmanagers.sipcallhalf.SipCHEventTransformer.sipCHtransform(SipCHEventTransformer.java:243) 5: com.broadsoft.sessionmanagers.sipcallhalf.SipCHEventTransformer.transformAndSendEvent(SipCHEventTransformer.java:298) 6: com.broadsoft.sessionmanagers.sipcallhalf.SipEndpoint.sendEventToUserAgentThroughTransformer(SipEndpoint.java:1240) 7: com.broadsoft.sessionmanagers.sipcallhalf.SipEndpoint.processSessionEvent(SipEndpoint.java:721) 8: com.broadsoft.apm.callp.Endpoint.processEvent(Endpoint.java:228) 9: com.broadsoft.sessionmanagers.callhalf.CallHalfServiceSession.deliverEvent(CallHalfServiceSession.java:1387) 10: com.broadsoft.apm.session.InputAdapter.distributeEvent(InputAdapter.java:129) 11: com.broadsoft.apm.session.SimpleQAdapter.processInput(SimpleQAdapter.java:225) 12: com.broadsoft.util.watchdog.WatchedThread.run(WatchedThread.java:279) 13: java.lang.Thread.run(Thread.java:619)
```

and

```
2010.05.13 17:30:10:277 GMT+00:00 | Info | CallP | SIP Endpoint | +14439510409 | PSTN | localHost40149830:0 Transforming Event: com.broadsoft.events.sip.Sip100InfoEvent 2010.05.13 17:30:10:277 GMT+00:00 | FieldDebug | CallP | Endpoint | 14105526501x102 | 90103-G6109080 | localHost40149837:0 ReleaseWithCauseEvent (cause=TEMPORARILY_UNAVAILABLE) created Thread \"Call Half Input Adapter 2\" stack elements: 1: com.broadsoft.events.callhalf.ReleaseWithCauseEvent.<init>(ReleaseWithCauseEvent.java:202) 2: com.broadsoft.events.callhalf.ReleaseWithCauseEvent.<init>(ReleaseWithCauseEvent.java:121) 3: com.broadsoft.sessionmanagers.sipcallhalf.transformer.ConnectRequestEventTransformer.transform(ConnectRequestEventTrans former.java:246) 4: com.broadsoft.sessionmanagers.sipcallhalf.SipCHEventTransformer.sipCHtransform(SipCHEventTransformer.java:243) 5: com.broadsoft.sessionmanagers.sipcallhalf.SipCHEventTransformer.transformAndSendEvent(SipCHEventTransformer.java:298) 6: com.broadsoft.sessionmanagers.sipcallhalf.SipEndpoint.sendEventToUserAgentThroughTransformer(SipEndpoint.java:1240) 7: com.broadsoft.sessionmanagers.sipcallhalf.SipEndpoint.processSessionEvent(SipEndpoint.java:721) 8: com.broadsoft.apm.callp.Endpoint.processEvent(Endpoint.java:228) 9: com.broadsoft.sessionmanagers.callhalf.CallHalfServiceSession.deliverEvent(CallHalfServiceSession.java:1387) 10: com.broadsoft.apm.session.InputAdapter.distributeEvent(InputAdapter.java:129) 11: com.broadsoft.apm.session.SimpleQAdapter.processInput(SimpleQAdapter.java:225) 12: com.broadsoft.util.watchdog.WatchedThread.run(WatchedThread.java:279) 13: java.lang.Thread.run(Thread.java:619)
```

The result is a release cause of BUSY:

```
2010.05.13 17:30:10:277 GMT+00:00 | FieldDebug | CallP | Service | +14439510409 | 90103-G6109080 | localHost40149832 ReleaseWithCauseEvent (cause=BUSY) created Thread \"Call Half Input Adapter 0\" stack elements: 1: com.broadsoft.events.callhalf.ReleaseWithCauseEvent.<init>(ReleaseWithCauseEvent.java:202) 2: com.broadsoft.events.callhalf.ReleaseWithCauseEvent.<init>(ReleaseWithCauseEvent.java:121) 3: com.broadsoft.services.huntgroup.HuntGroupServiceInstance.huntExhausted(HuntGroupServiceInstance.java:547) 4: com.broadsoft.services.huntgroup.StateEngine.huntExhausted(StateEngine.java:688) 5: com.broadsoft.services.huntgroup.SimultaneousStateEngine.allAgentsFailed(SimultaneousStateEngine.java:532) 6: com.broadsoft.services.huntgroup.SimultaneousStateEngine.processHuntingState(SimultaneousStateEngine.java:214) 7: com.broadsoft.services.huntgroup.SimultaneousStateEngine.runEngine(SimultaneousStateEngine.java:71) 8: com.broadsoft.services.huntgroup.HuntGroupServiceInstance.processEvent(HuntGroupServiceInstance.java:260) 9: com.broadsoft.events.callhalf.ReleaseWithCauseEvent.routeToServiceInstance(ReleaseWithCauseEvent.java:479) 10: com.broadsoft.apm.asservicemanagement.ASServiceBus.routeEvent(ASServiceBus.java:251) 11: com.broadsoft.apm.callp.CHCallManager.processEvent(CHCallManager.java:1346) 12: com.broadsoft.sessionmanagers.callhalf.CallHalfServiceSession.deliverEvent(CallHalfServiceSession.java:1416) 13: com.broadsoft.apm.session.InputAdapter.distributeEvent(InputAdapter.java:129) 14: com.broadsoft.apm.session.SimpleQAdapter.processInput(SimpleQAdapter.java:225) 15: com.broadsoft.util.watchdog.WatchedThread.run(WatchedThread.java:279) 16: java.lang.Thread.run(Thread.java:619) 2010.05.13 17:30:10:277 GMT+00:00 | FieldDebug | Timer Accounting timer stopped - localHost40149839, AUDIT, id=2822790 2010.05.13 17:30:10:277 GMT+00:00 | Info | CallP | Service | State Engine | +14439510409 | 90103-G6109080 | localHost40149832 CFGNA External Timer Cancelled
```

So this is normal and expected that you will receive a:

```
2010.05.13 17:30:10:278 GMT+00:00 | Info | Sip | +15856272112 | localHost40149831:0 udp 420 Bytes OUT to 192.168.215.5:5060 SIP/2.0 600 Busy everywhere Via:SIP/2.0/UDP 192.168.215.5;branch=z9hG4bKBroadWorks.1q6vn6u-192.168.215.5V5060-0-157003504-699484156-1273771810271- From:\"ENGINEERING T20\"<sip:+15856272112@192.168.215.5;user=phone>;tag=699484156-1273771810271- To:<sip:+14439510409@192.168.215.5:5060;user=phone>;tag=1041404320-1273771810275 Call-ID:BW173010271130510705568600@192.168.215.5 CSeq:157003504 INVITE Content-Length:0
```

Because the release cause is BUSY the situation requires CFB assigned to the HG.  CFGNA will only kick in if one or more device is sent an INVITE. Because no user is logged in to the call center no user is sent an INVITE.

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks