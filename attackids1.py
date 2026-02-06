import time
import random
from scapy.all import IP, TCP, Raw, Ether, sendp, conf, get_if_addr

# --- CONFIGURATION ---
# Use your Network IP (from your Streamlit output) instead of 127.0.0.1
TARGET_IP = "192.168.100.26" 
TARGET_PORT = 80

ATTACK_PAYLOADS = [
    ("SQL Injection", "SELECT * FROM users WHERE id='1' OR '1'='1';"),
    ("XSS Attempt", "<script>alert('IDS_TEST')</script>"),
    ("Path Traversal", "../../etc/passwd"),
    ("Database Attack", "DROP TABLE system_logs; --")
]

def get_random_ip():
    """Generates a random public IP string."""
    return ".".join(map(str, (random.randint(1, 254) for _ in range(4))))

def launch_attack():
    # Automatically select the best interface
    current_iface = conf.iface
    print(f"🌍 Global Attacker v2.0")
    print(f"[*] Target: {TARGET_IP}")
    print(f"[*] Using Interface: {current_iface}")
    print("[!] Sending spoofed packets at Layer 2... (Ctrl+C to stop)\n")

    try:
        while True:
            # 1. Prepare Spoofed Source and Attack
            spoofed_src = get_random_ip()
            name, payload = random.choice(ATTACK_PAYLOADS)

            # 2. Construct Layer 2 Packet (Ethernet / IP / TCP / Raw)
            # This forces the packet out of the network card and back in
            # so the IDS 'sniffer' can see it.
            pkt = (
                Ether() / 
                IP(src=spoofed_src, dst=TARGET_IP) / 
                TCP(dport=TARGET_PORT, flags="S") / 
                Raw(load=payload)
            )

            # 3. Send at Layer 2 (sendp)
            sendp(pkt, iface=current_iface, verbose=False)
            
            print(f"[>] {name} spoofed from {spoofed_src}")
            
            # Wait 3 seconds between attacks
            time.sleep(3)

    except KeyboardInterrupt:
        print("\n[!] Stopping Attacker.")
    except Exception as e:
        print(f"\n[!] ERROR: {e}")
        print("Tip: Make sure you are running as Administrator!")

if __name__ == "__main__":
    launch_attack()