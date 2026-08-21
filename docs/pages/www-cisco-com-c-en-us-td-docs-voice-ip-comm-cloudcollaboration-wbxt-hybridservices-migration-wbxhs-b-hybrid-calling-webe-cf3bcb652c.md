---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-hybridservices-migration-wbxhs-b-hybrid-calling-webe-cf3bcb652c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/hybridservices/migration/wbxhs_b_hybrid-calling-webex-domain-migration-guide/wbxhs_b_migrate-call-service-to-webex_chapter_011.html
retrieved_at: 2026-08-20T23:59:50.237963+00:00
---

Migrate Cisco Spark Hybrid Call Service Organization to the Cisco Webex Domain

# Migrate Cisco Spark Hybrid Call Service Organization to the Cisco Webex Domain

## Results

Updated: March 7, 2019

Chapter: Troubleshoot the Migration

## Chapter: Troubleshoot the Migration

- Troubleshoot the Migration

- Troubleshoot a Failed Migration

- Questions

# Troubleshoot the Migration

## Troubleshoot a Failed Migration

A migration may fail while updating the remote destination on Unified CM. Use this troubleshooting task if the Remote Destination
                              list on Unified CM shows that some migrated users still have the old ciscospark.com Destination Number.

If you opted to wait for the daily discovery, ensure that the 07:00 to 11:00 UTC discovery window has passed since you initiated
                                 the migration in Cisco Webex Control Hub. If the discovery window has elapsed, check in Cisco Webex Control Hub to see if
                                 any users are showing in error state for Call Service Connect. If the user shows an error, select Connect to view the error
                                 details, and then:

Resolve the cause of the error, as per the error text, and then choose one:

Toggle the Connect service for the user off and then on.

Wait for the next discovery cycle.

If you opted to restart the Call Connector, check in Cisco Webex Control Hub if any users are showing error for Call Service
                                 Connect. If the user shows an error, select Connect to view the error details, and then:

Resolve the cause of the error per the error text and then choose one:

Toggle the Connect service for the user off and then on.

Restart the Call Connector.

## Questions

### Will the migration take place if I have set my Cisco Spark-RD creation on the Expressway Connector to manual?

Yes, the migration takes place whether you have automatically or manually
                              created Spark-RDs.

### Will the Cisco Spark-RD name change to Webex-RD?

For now, the device name will not change.