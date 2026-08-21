---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-serviceability-guide-1-0-2-sattrace-html-a945f7b823
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/serviceability/guide/1_0_2/sattrace.html
retrieved_at: 2026-08-21T16:06:10.801031+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Troubleshooting Trace Setting Configuration

## Chapter: Troubleshooting Trace Setting Configuration

- Related Topics

## Troubleshooting Trace Setting Configuration

The Troubleshooting Trace Setting window allows you to choose the services in Cisco Unified Presence Server for which you want to set predetermined troubleshooting trace settings. This chapter contains information on how to set and reset troubleshooting trace setting for specific services.

Note Leaving Troubleshooting trace enabled for a long time increases the size of the trace files and may impact the performance of the services.

Step 1 Choose Trace > Troubleshooting Trace Settings .

Step 2 Do one of the following tasks:

• To set troubleshooting trace, check the check box of the service(s) from the list of services for each node. If you want to check all services on a particular node, check the Check all Services for a Node check box under that node. If you want to check all services for all nodes, check the Check all Services for a Node check box in the services list.

Then, click the Apply Troubleshooting Traces button.

Note The services that are not activated on a Cisco Unified Presence Server node display as N/A.

• To restore the original trace settings for the services in the cluster, click Reset Troubleshooting Traces .

Note The Reset Troubleshooting Traces button displays only if you have set troubleshooting trace for one or more services.

Additional Information

See the Related Topics .

## Related Topics

• Trace Configuration