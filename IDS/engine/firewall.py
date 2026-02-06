import subprocess
import platform
import threading

class SmartFirewall:
    def __init__(self, ban_duration, whitelist):
        self.os = platform.system()
        self.ban_duration = ban_duration
        self.whitelist = whitelist
        self.blocked = set()

    def block_ip(self, ip):
        if ip in self.whitelist or ip in self.blocked: return
        
        print(f"[!] Blocking {ip}...")
        if self.os == "Linux":
            cmd = f"sudo iptables -I INPUT 1 -s {ip} -j DROP"
        else:
            cmd = f'netsh advfirewall firewall add rule name="IDS_{ip}" dir=in action=block remoteip={ip}'
        
        subprocess.run(cmd, shell=True)
        self.blocked.add(ip)
        threading.Timer(self.ban_duration, self.unblock_ip, [ip]).start()

    def unblock_ip(self, ip):
        if self.os == "Linux":
            cmd = f"sudo iptables -D INPUT -s {ip} -j DROP"
        else:
            cmd = f'netsh advfirewall firewall delete rule name="IDS_{ip}"'
        subprocess.run(cmd, shell=True)
        self.blocked.remove(ip)