---
doc_id: sec-cloudapps-cisco-com-security-center-resources-network-integrity-monitoring-html-adb74ec816
source_url: https://sec.cloudapps.cisco.com/security/center/resources/network_integrity_monitoring.html
retrieved_at: 2026-09-01T14:10:07.706839+00:00
---

Home / Cisco Security

Telemetry-Based Infrastructure Device Integrity Monitoring

# Telemetry-Based Infrastructure Device Integrity Monitoring

### Contents

Introduction Instrumentation Understanding Network Telemetry NetFlow and IPFIX Packet Captures Logs Deployment Telemetry Tools Indicators Potential Command and Control Indicators Potential Data Exfiltration Indicators Case Study Conclusion Acknowledgments References Revision History

# Introduction

Malware is software created to modify a device’s behavior for the benefit of a malicious third party (attacker). One of the characteristics of effective malware is that it can run stealthily on a device in privileged mode. Malware is usually designed to monitor and exfiltrate information from the operating system on which it is running without being detected. Potentially sophisticated malware would attempt to hide its presence by modifying command output that may reveal information about the malware.

Network administrators concerned that their network devices may have been compromised can take steps to verify the integrity of their network infrastructure. The Cisco IOS Software Integrity Assurance and Cisco IOS XE Software Integrity Assurance white papers explain how the integrity of these devices can be assessed. Network telemetry can also be used to identify such suspicious activity. The signs of a compromise in a network can take many forms, including network devices that are exfiltrating data, forwarding packets to unexpected destinations, sending unrequested ICMP replies, and more. The analysis of telemetry data received from a network is as important as the data collected. The indicators are there and it is the administrator’s task to find them and evaluate their meaning. Finding an anomaly in normal network traffic is difficult, so that is why a baseline of network traffic is very important. A network traffic baseline will give the network administrator a starting point from which to build a profile of network traffic. In summary, the following steps summarize the process of protecting and monitoring infrastructure devices:

- Harden devices

- Instrument the network

- Establish a baseline

- Analyze deviations from the baseline

The network can provide all data needed to determine whether a compromise has happened. In this paper we discuss the various kinds of telemetry available in the network and how to collect it. We begin by taking a look at the instrumentation available in a network, the data it produces, and ways to collect it. Even a small network can generate an large amount of data that is not possible to analyze without using software tools. We also mention open source and commercial off-the-shelf software analysis solutions. We look at various indicators of compromise derived from network instrumentation. Finally, we examine a case study where the SiLK open-source analysis suite is used on a series of NetFlow/IPFIX records. Although the case study uses SiLK, the concepts apply to any NetFlow/IPFIX analysis tool.

Note: Readers should note that attackers’ methods change continually, so identifying suspicious traffic requires thorough investigation and cannot always be completely successful.

# Instrumentation

To collect and analyze telemetry to identify potential compromises, certain instrumentation needs to be in place. For example, if the only telemetry collected in the network consists of web logs, there could be suspicious traffic entering or exiting infrastructure devices that would not be identified during the analysis. The components for effective network instrumentation include the following:

- A security policy containing a description of the assets that need protection.

- An understanding of the network topology. The strategic placement of instrumented devices is critical to gathering complete telemetry. Network documentation is often incomplete; however, this should not prevent picking an obvious first location to set up instrumentation.

- An inventory of the existing devices that are collecting telemetry may already exist. Devices such as intrusion detection system (IDS) devices and Network Analysis Modules (NAMs) may already be in the correct place to add to the instrumentation strategy.

These components together provide guidance and direction for the purpose of the instrumentation and its prioritization. Appropriate instrumentation will save an organization time by focusing on the IP space that can be analyzed with the least complexity.

## Understanding Network Telemetry

### NetFlow and IPFIX

One important piece of telemetry that can be instrumented on infrastructure devices is NetFlow. NetFlow or IPFIX, its IETF equivalent, is a feature that can be enabled on devices by many vendors, including Cisco routers, Cisco ASA, and Cisco NetFlow Generation Appliance (NGA). NetFlow caches and generates records about network traffic and their characteristics. Depending on the configuration, NetFlow can report on various OSI layer flow details. For example, it can report on flows based on source and destination IP addresses or on transport-layer source and destination port numbers, or it can export parts of the TCP header. After the information is exported from the network device, it is collected at a location (collector) that can perform correlation and analysis.

NetFlow exports information to reporting collectors in various formats, including NetFlow version 5 (v5) and version 9 (v9). NetFlow v5 is used with traditional NetFlow, has a fixed export format, and exports a limited set of data. NetFlow v9 is a flexible and extensible NetFlow format used by Flexible NetFlow. NetFlow v9 includes a template to describe what is being exported and the export data. The template is periodically sent to the NetFlow collector, telling it what data to expect from the router or switch. The data is then sent to the collector for analysis. NetFlow v9 is extensible and flexible and therefore any flow data available in the network can theoretically be sent in NetFlow v9 format to the collector. Flexible NetFlow allows the user to configure and customize the NetFlow v9 exported data. Flexible NetFlow can provide a wealth of information in packets and data flows. NetFlow v9 is also the basis for the IETF standard IPFIX associated with the IP Flow Information Export working group of the IETF.

NetFlow information can be a very useful source of telemetry that, when carefully analyzed, can reveal information for the investigation of suspicious activity. For more information on NetFlow, refer to Introduction to Cisco IOS NetFlow - A Technical Overview .

### Packet Captures

In addition to flow information, telemetry can often include network taps or captures. There are several vendors supporting deep packet inspection from carefully instrumented taps in the network. These forensics can be very useful when investigating end-host compromises. Network device indicators of compromise will rarely be traditional, and thus only careful analysis will reveal useful information. Indicators of compromise presented in the Indicators section of this document can be investigated from historical packet captures, assuming they are stored for adequate amounts of time and the analysis tools can offer the necessary analysis functionality.

### Logs

Network device logs can also prove useful in certain situations. For example, attempting to compromise an infrastructure device’s management credentials could be done using brute force. Such attempts could generate log messages that would reveal the suspicious activity. Log collectors often offer correlation functionality that could identify compromises by correlating syslog events. Log-based indicators of compromise are discussed in the Cisco IOS Software Integrity Assurance and Cisco IOS XE Software Integrity Assurance white papers. Since this document focuses on network telemetry, we will not be further discussing log-based indicators of compromise and analysis in the remaining sections of this paper.

## Deployment

A minimal deployment of instrumentation is shown in Figure 1. It depicts network telemetry (NetFlow or network taps) instrumented in front of infrastructure devices that are suspected to be compromised.

Figure 1. Example Telemetry Collection in Certain Parts of the Network

Deployment of telemetry extraction and collection depends on the infrastructure devices to be investigated and the network architecture. Some choice locations for telemetry extraction include the following:

- Data center gateways or virtual gateways

- DMZ routers

- Cloud provider aggregation points

When exporting NetFlow or packet captures, network administrators need to consider the following:

Often it is useful to have two points of data collection, one before and one after the point of interest. Such deployment would allow administrators to identify traffic that is generated or processed by the device itself that could indicate a compromise. In situations where asymmetric routing takes place, it is useful for the points of asymmetry to be monitored by the same collector.

Sampling can alleviate processing load, but at the same time can worsen the quality of the information. Most network telemetry indicating infrastructure device compromises will be a very small fraction of the traffic going through the network. Thus, sampled information could prevent the detection of a compromise.

If the devices extracting telemetry are infrastructure devices, such as a Cisco IOS router extracting NetFlow or traffic span from a Cisco IOS switch, the impact of the telemetry extraction should be considered. NetFlow was designed to be lightweight, but it still adds processing load to a router. Similarly, the telemetry analysis tools chosen also need to be scoped for performance. Vendors often document the performance impact of flows per second and corresponding packets per second; therefore, readers should consult the documentation for the ideal solution and test the deployment prior to implementation. Similarly, the collector and analysis tools need to be carefully scoped to be able to process the load of traffic generated during the collection.

Note: Readers should note that if the potentially compromised device is generating some of the telemetry used for identification, that telemetry could be tampered with and thus not considered trustworthy. For example, a potentially compromised device might be exporting NetFlow records that exclude command and control traffic.

## Telemetry Tools

After all information is collected from the network (packet captures, NetFlow, logs), suspicious activity can be identified by analyzing the information. There are many vendors that can aggregate and process all the available data to assess the security of the network. Some, but not all, of these tools are available from Splunk, Lancope, Plixer, and SolarWinds. All these can collect and analyze NetFlow in meaningful ways. Some can also consume logs from various places in the network such as Active Directory or web proxies, and they can correlate these logs with network telemetry to identify potential anomalies. This functionality can be very helpful for identifying compromised endpoints that show suspicious activity. For infrastructure devices, these tools might not always work because the methods used in network device compromises can be subtle and untraditional.

Similar tools can offer deep packet inspection and suspicious activity identification by looking at or extracting actual network traffic from the wire. Some, but not all, vendors in that field are Gigamon, Solera, and nPulse. Due to the nature of a network device compromise, deep packet inspection may not always identify it.

Other open-source products are also available, such as the System for Internet-Level Knowledge (SiLK). SiLK is a collection of traffic analysis tools developed by the CERT Network Situational Awareness team (CERT NetSA) to facilitate security analysis of large networks. SiLK is free, open-source software. Other freely available tools are listed in the Freeware NetFlow Software page.

# Indicators

To identify suspicious activity that could indicate network infrastructure device compromise, administrators need to perform efficient analysis of the telemetry collected from the network. Analysis tools mentioned in the Instrumentation section of this document can often help in identifying such activities.

If possible, network activity should be profiled. Profiling should occur only while there is no possibility that the infrastructure is compromised yet (for example, early in the deployment). Most network analytics tools can use traffic captures or NetFlow to establish a baseline of network activity that can then be used to detect potentially suspicious activity.

Due to the nature of the activities, automated tools might not always detect indications of compromise of infrastructure devices by default. Network administrators can use automated tools to perform additional analysis of the telemetry collected to look for indicators of compromise.

## Potential Command and Control Indicators

Figure 2. Unexpected Traffic Generated by the Router

Readers should note that sometimes command and control traffic might not be destined to the device itself as long as the compromised device interface receives it. A compromised device may inspect specific transit traffic to discover command and control operations. This traffic would be hard to identify using traffic analysis. Transit traffic that is unexpectedly punted to the infrastructure device’s processor should require further investigation.

Administrators should be careful in assuming that such flows are always suspicious. There are many normal scenarios where asymmetric routing can make flows ingress and egress a network at different points. This is why having an established baseline of “normal” traffic is of paramount importance when attempting to identify anomalous, and sometimes malicious, traffic.

Figure 3. Unidirectional ICMP Packets Without Corresponding ICMP on the Other Direction

- A compromised device could, at times, attempt to spread the malicious code to other infrastructure devices in the network. The indicator for such activity would be TCP traffic generated by the device destined to other infrastructure devices or internal networks. An example here could be TCP scanning to identify potential victims. Historical data should be audited to identify potential traffic spikes sourced by infrastructure devices destined to internal networks attempting to spread malware.

## Potential Data Exfiltration Indicators

Figure 4. Packets Seen Leaving the Router Without Ever Ingressing It

Figure 5. High Amounts of Exfiltrated Traffic Could Cause Noticeable Traffic Spikes

- Exfiltrated traffic is often carried over the following tunneling protocols alone or in combination: IP Security (IPsec), IPv6-in-IPv4, and Generic Routing Encapsulation (GRE). Potentially even IPv6 Extension Headers could be used in IPv6-enabled environments. Depending on the scenario, tunnel traffic and IPv6 Extension Headers should be collected and analyzed for legitimacy.

- Flows from unidirectional, connectionless protocols (for example, UDP or ICMP), usually egressing from an infrastructure device’s interface, could be a compromise indicator. Administrators should be careful assuming that such flows are always suspicious. There are many normal scenarios where asymmetric routing can make flows ingress and egress a network at different points. This is why having an established baseline of “normal” traffic is of paramount importance when attempting to identify anomalous, and sometimes malicious, traffic. Thus, unidirectional, connectionless protocol flows should be investigated, especially if they are not seen ingressing the device and the flow does not have a source IP address of the infrastructure device.

Note: Readers should note that the preceding analysis should not be considered all inclusive. Potential manipulation of the operating system of an infrastructure device could include many techniques that could not be included in this document. Establishing baselines of normal network activity sourced from and destined to infrastructure devices could help identify suspicious activities when deviations are observed.

# Case Study

To demonstrate the identification of some of these kinds of indicator traffic patterns, we will use the SiLK tool suite . SiLK is an open-source suite of tools for collecting, storing, and analyzing large amounts of flow data, including NetFlow and IPFIX. Cisco uses SiLK in various telemetry projects. It is based on constructing pipelines of tools to perform selection, filtering, and eventual display of query results. As discussed in the Telemetry Tools section, there are many other commercial and open-source tools that have similar capabilities. SiLK was chosen for this demonstration because of its availability and maturity. iSiLK provides a graphical front end for SiLK tools. Any telemetry analysis tool may be used to look for the indicators presented in the Indicators section.

After installing SiLK and enabling the export of flow information to it, the next step is to build a repository of flow records. In our example, the SiLK tool named rwflowpack is configured to listen on specified ports for flow records from specific sources. The tool indexes the incoming records into a unified archive that can be efficiently queried by other SiLK tools. After configuring rwflowpack (for more information, refer to the documentation ), we configure a source of data to feed flow records into SiLK. This can be a trusted intermediary router or switch with visibility into the traffic of concern (for example, a border router or other infrastructure device) or any other trusted network tap or NetFlow generator. Alternatively, a software tool closely associated with SiLK, but not formally in the SiLK tool suite, is yaf (Yet Another Flowmeter). Yaf can generate IPFIX flow records based on reading from live network traffic, or it can generate flow records from captured pcap files (as generated by tcpdump or Wireshark).

When a repository of flow records has been generated with rwflowpack , we are ready to begin analyzing the traffic. The primary tool for querying the flow dataset is rwfilter . The rwfilter tool allows us to specify the window of time for the query by using the --start-date and --end-date options. It also has a wide variety of filtering options. For example, to view a day’s ICMP requests, the following command can be used:

```
$  rwfilter --start-date 2014/04/20 --end-date 2014/04/20 \
            --flowtypes=all/all --proto 1  --pass=stdout | \
   rwcut --fields  sIP,dIP,pkts,byts,sTime,iType,iCode --num-recs=5 
  
            sIP|            dIP|   packets|    bytes|                  sTime|iTy|iCo|
     10.62.6.85| 192.168.230.10|         1|      576|2014/04/19T23:59:27.547|  3|  3|
     10.0.36.1 | 192.168.122.10|         4|      240|2014/04/19T23:59:27.550|  3|  3|
     10.4.137.1| 192.168.122.10|         2|      120|2014/04/19T23:59:27.550|  3|  3|
  10.171.224.87| 192.168.0.17.1|         1|      428|2014/04/19T23:59:27.560|  3|  3|
   10.89.84.210|  192.168.83.42|        15|     1440|2014/04/19T23:59:27.600|  8|  0|
```

In this case, the rwfilter invocation is pulling records out of the archive for the specified data, displaying all requested record types (flows can be categorized by rwflowpack , a feature we won't be using), and looking at only ICMP protocols (IP protocol 1). These records are passed to rwcut (in a binary format), which is told which fields we want to display and then displays the record as a delimited ASCII table. In this particular case, the --num-recs option was used to limit the output to five entries for brevity.

Another useful command is rwstats . This command takes a stream of matching flow records and performs aggregation of values based on a set of indexed fields. This example uses the same rwfilter command, but feeds into rwstats :

```
$ rwfilter --start-date 2014/04/20 --end-date 2014/04/20  \
           --flowtypes=all/all --proto 1  --pass=stdout  | \
  rwstats  --fields iType,iCode  --values packets,bytes --count 10
INPUT: 1051498 Records for 26 Bins and 7818634 Total Packets
OUTPUT: Top 10 Bins by Packets
iTy|iCo|        Packets|               Bytes|  %Packets|   cumul_%|
  3|  3|        2949022|          1074472099| 37.717867| 37.717867|
  8|  0|        1631759|           329935210| 20.870129| 58.587996|
  0|  0|        1615003|           191457942| 20.655820| 79.243817|
  3|  0|        1402080|           134717825| 17.932544| 97.176361|
  3| 13|         135866|             7614920|  1.737720| 98.914081|
 11|  0|          43785|             3801740|  0.560008| 99.474090|
 11|  1|          24556|             4832632|  0.314070| 99.788160|
  3|  1|          12374|             2103853|  0.158263| 99.946423|
  3| 10|           2446|              852904|  0.031284| 99.977707|
  3|  2|           1144|               87284|  0.014632| 99.992339|
```

Here, rwstats is depositing matched flow records into "buckets" based on the fields specified by the --fields option, which in this case are the ICMP type and ICMP code. Upon completion, the requested field values associated with each of the buckets are then summed and displayed. In this case, we're summing the number of packets and bytes for each ICMP type and ICMP code. The --count specifies display of the top ten buckets. In this case, our top ICMP traffic by packet count and byte count is ICMP Type 3-Code 3, otherwise known as ICMP Port Unreachable. It's not surprising that this type/code has both the highest count and the most data because this code requires duplicating (at least in part) the offending packet that generated the error. Also, because this data was collected on a network providing public services, there is a lot of automated port scanning, resulting in a large number of failed connections.

Next in the table are ICMP Echo Request (Type 8) and ICMP Echo Reply (Type 0). It makes sense that these counts are roughly equivalent to each other. If either set of numbers is drastically different, it could indicate something suspicious. For example, to detect hosts sending suspicious ICMP echo packets with payloads that aren't empty, one possible filter command could be:

```
$ rwfilter --start-date 2014/04/01 --end-date 2014/05/01  \
           --flowtypes=all/all --proto 1 \
           --icmp-type 8,0  --bytes-per-packet 50- --pass=stdout  | \
  rwstats  --fields sIP,dIP,iType  --values packets,bytes --count 5
INPUT: 1746651 Records for 33932 Bins and 4522593413 Total Bytes
OUTPUT: Top 20 Bins by Bytes
            sIP|            dIP|iTy|        Bytes|        Packets|    %Bytes|   cumul_%|
 10.223.115.208| 10.223.115.111|  8|   1720524000|        1147016| 38.042863| 38.042863|
   172.16.91.13| 192.168.192.67|  0|    253411704|         537661|  5.603239| 43.646101|
 192.168.192.67|   172.16.91.13|  8|    167234762|         388912|  3.697762| 47.343864|
     10.7.83.42|  192.168.24.17|  0|     72292699|         201482|  1.598479| 48.942343|
  192.168.24.17|     10.7.83.42|  8|     65239008|         858408|  1.442513| 50.384856|
```

This invocation is similar to the rwstats invocation previously discussed, but with some key differences. Notably, the rwfilter is now only matching ICMP Echo Request and ICMP Echo Response packets that are 50 bytes or more. Considering that an ICMP Echo Request and Response must have an IP header (typically 20 bytes for IPv4) and an ICMP header (8 bytes) with an optional (usually empty) payload, 50 bytes falls outside the norm for this kind of ICMP message. Another key difference in this SiLK command-line example is that the rwstats command is now creating buckets based on the source and destination IP addresses as well as the ICMP type. This allows us to view the top pairs of addresses exchanging large ICMP echo messages. The results of this example are somewhat dramatic. The first result shows a machine on what appears to be a local network sending a flood of unanswered ICMP Echo Request traffic. By dividing the number of total bytes by the number of packets, we can see that the packets were averaging 1,500 bytes per packet. This is highly suspicious behavior that should be investigated.

Another very useful feature of rwfilter is to show flow matches based on a collection of addresses known as an IPSet. This match can be either a positive match (for example, only records matching the IPSet are propagated down the pipeline) or a negative match (to remove a set of addresses from further processing). This feature allows us to easily monitor the traffic associated with the infrastructure devices, which should not generally be initiating outbound network traffic. To create an IPSet, we'll use rwsetbuild . Simply list the IP addresses (or classless interdomain routing (CIDR)-specified networks) in a file, such as router-addresses.txt and build the set as so:

```
$ rwsetbuild router-addresses.txt router-addresses.set
```

Another useful IPset to build is one representing the entire internal address space:

```
$ rwsetbuild my_networks.txt my_networks.set
```

You can then use rwfilter to easily search for flows indicating traffic originating from the infrastructure routing devices destined to offsite addresses.

```
$ rwfilter --start-date 2014/04/01 --end-date 2014/05/01  --flowtypes=all/all \
  --sipset=router-addresses.set --not-dipset=my_networks.set --pass=stdout  | \
  rwcut
```

One thing that is important to remember, though, is that NetFlow builds flow records based on the unidirectional flow of information. Thus, rwfilter will display all flows of network traffic leaving the device, regardless of which side initiated the communication. This can be a very useful query to run on its own, but if we want to detect only outbound initiations of a TCP connection, we will need to add --flags-initial=S/SA to the rwfilter invocation to display only outbound connections where the flow was initiated with a SYN flag (initiating the connection) without being accompanied by an ACK flag.

Flow monitoring can give great insight into the behavior of network infrastructure. By investigating the data available through flow records using a tool such as SiLK, you can detect anomalous traffic sent to or generated by infrastructure devices that might signify indicators of compromise.

# Conclusion

In conclusion, in this paper we described how the signs of a compromised network can become visible if network administrators gather and correctly analyze the telemetry available from their networks. To achieve that, the instrumentation to provide the telemetry needs to be present in every enterprise-grade network device. There are many telemetry analysis tool options available. Using these tools, a network administrator concerned about the integrity of the network devices can take steps, including establishing a baseline of network traffic and searching for specific flows that may be an indicator of compromised devices. Flows can reveal abnormal patterns related to infrastructure devices, which could point to suspicious activity that requires mitigation.

# Acknowledgments

Panos Kampanakis (pkampana[at]cisco[dot]com)

Jeremy McGuinn (jemcguin[at]cisco[dot]com )

William McVey (wam[at]cisco[dot]com )

Lou Ronnau (lronnau[at]cisco[dot]com )

Applied Security Intelligence team, Cisco Security Research and Operations

Special thanks to all the rest of the group members for their valuable feedback.

# References

Cisco IOS Software Integrity Assurance //www.cisco.com/web/about/security/intelligence/integrity-assurance.html

Cisco IOS XE Software Integrity Assurance //www.cisco.com/web/about/security/intelligence/ios-xe-integrity-assurance.html

Network-Based Intrusion Prevention Case Study: How Cisco Protects Data Center Assets with Network-Based Intrusion Prevention System //www.cisco.com/web/about/ciscoitatwork/security/csirt_network-based_intrusion_prevention_system.html

Using Lancope StealthWatch for Information Security Monitoring //www.cisco.com/en/US/solutions/collateral/ns340/ns1176/borderless-networks/Cisco_IT_Case_Study_CSIRT_Lancope_Stealthwatch.html

Introduction to Cisco IOS NetFlow - A Technical Overview http://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-NetFlow/prod_white_paper0900aecd80406232.html

Cisco CSIRT on Advanced Persistent Threat http://blogs.cisco.com/security/cisco-csirt-on-advanced-persistent-threat/

# Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Date | Description |
|---|---|
| September 7, 2018 | Moved content to a new URL. |
| July 7, 2014 | Initial public release. |