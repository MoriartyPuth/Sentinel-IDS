from scapy.all import sniff, IP
from engine.analyzer import analyze_packet

def start_sniffing(interface, firewall, notifier, config):
    def callback(p):
        if p.haslayer(IP):
            analyze_packet(p, firewall, notifier, config)
    sniff(iface=interface, prn=callback, store=0)