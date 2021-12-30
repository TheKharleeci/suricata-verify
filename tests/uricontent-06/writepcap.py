#!/usr/bin/env python
from scapy.all import *

pkts = []

pkts += Ether(dst='ff:ff:ff:ff:ff:ff', src='00:01:02:03:04:05')/ \
    Dot1Q(vlan=6)/ \
    IP(dst='192.168.1.1', src='192.168.1.5')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qtype="A", qname="google.com"), an=DNSRR(rdata="123.0.0.1"))
pkts += Ether(dst='ff:ff:ff:ff:ff:ff', src='00:01:02:03:04:05')/ \
    Dot1Q(vlan=6)/ \
    IP(dst='192.168.1.1', src='192.168.1.5')/TCP(sport=53, dport=80, flags='P''A')/"POST /oneself/af HTTP/1.0\r\nUser-Agent: Mozilla/1.0\r\nCookie: hellocatch\r\n\r\n"

wrpcap('input.pcap', pkts)