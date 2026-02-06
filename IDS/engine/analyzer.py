import re
from scapy.all import IP, Raw
from utils.database import log_to_db

SIGNATURES = {
    "SQL Injection": re.compile(r"(UNION|SELECT|INSERT|DROP)", re.IGNORECASE),
    "XSS Attempt": re.compile(r"(<script>|alert\()", re.IGNORECASE),
    "Path Traversal": re.compile(r"(\.\.\/|\/etc\/passwd|C:\\Windows)", re.IGNORECASE)
}

def analyze_packet(packet, firewall, notifier, config):
    # 1. Check if it's an IP packet
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        
        # 2. Look for the Raw data (The payload)
        if packet.haslayer(Raw):
            try:
                # Extract and decode the payload
                payload = packet[Raw].load.decode(errors='ignore')
                
                # DEBUG: Uncomment the line below to see all incoming data in terminal
                # print(f"[*] Inspecting payload from {src_ip}: {payload[:50]}")

                # 3. Check against Signatures
                for name, sig in SIGNATURES.items():
                    if sig.search(payload):
                        print(f"\n[🔥] ALERT: {name} detected from {src_ip}!")
                        
                        # Get Geo-location (Placeholder for now, or use the API function)
                        # lat, lon, country = get_geo(src_ip) 
                        
                        # 4. Log and Alert
                        log_to_db(src_ip, name, "CRITICAL")
                        firewall.block_ip(src_ip)
                        notifier.send_alert(f"IDS Alert: {name}", f"Source: {src_ip}")
                        
            except Exception as e:
                # print(f"Error decoding payload: {e}")
                pass