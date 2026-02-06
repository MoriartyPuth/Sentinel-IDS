import sqlite3
import time

def init_db():
    conn = sqlite3.connect('data/ids_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS alerts
                 (timestamp TEXT, ip TEXT, attack_type TEXT, severity TEXT, 
                  lat REAL, lon REAL, country TEXT)''')
    conn.commit()
    conn.close()

def log_to_db(ip, attack_type, severity, lat=0.0, lon=0.0, country="Unknown"):
    conn = sqlite3.connect('data/ids_logs.db')
    c = conn.cursor()
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO alerts VALUES (?, ?, ?, ?, ?, ?, ?)",
              (ts, ip, attack_type, severity, lat, lon, country))
    conn.commit()
    conn.close()