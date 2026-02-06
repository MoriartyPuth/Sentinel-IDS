import json
from engine.sniffer import start_sniffing
from engine.firewall import SmartFirewall
from utils.database import init_db
from utils.notifier import NotificationManager

def main():
    with open('config.json') as f: config = json.load(f)
    init_db()
    fw = SmartFirewall(config['ban_duration_seconds'], config['whitelist'])
    notif = NotificationManager(config['discord_webhook_url'])
    start_sniffing(config['monitored_interface'], fw, notif, config)

if __name__ == "__main__":
    main()