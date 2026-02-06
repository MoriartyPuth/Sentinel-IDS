import requests
import time

class NotificationManager:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.last_alert = 0

    def send_alert(self, title, message):
        if not self.webhook_url or (time.time() - self.last_alert < 10):
            return
        payload = {"embeds": [{"title": title, "description": message, "color": 15158528}]}
        try:
            requests.post(self.webhook_url, json=payload)
            self.last_alert = time.time()
        except: pass