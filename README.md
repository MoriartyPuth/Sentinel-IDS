

# Topic: A Multi-Layered Intrusion Detection and Prevention System (IDS/IPS) with Real-Time Geo-Visual Analytics.

Sentinel-IDS is a high-performance, Python-based Network Intrusion Detection System (NIDS) capable of real-time packet inspection, automated threat mitigation (IPS), and global threat visualization.

By combining Scapy for deep packet inspection (DPI) with a Streamlit-based Security Operations Center (SOC) dashboard, Sentinel-IDS provides a full-stack security solution for monitoring local networks.

## 🚀 Key Features

- 🔍 Deep Packet Inspection (DPI): Real-time analysis of TCP/IP traffic using RegEx-based signatures to detect SQL Injection, XSS, and Path Traversal attacks.

- 🌍 Global Threat Mapping: Integrated Geo-IP tracking that maps attacker locations in real-time on an interactive 3D/2D map.

- ⚡ Active IPS (Prevention): Automatically interfaces with the system firewall to block malicious IP addresses upon detection.

- 📊 Live SOC Dashboard: An auto-refreshing UI that displays threat metrics, attack distribution charts, and a live event log.

- 🔔 Instant Notifications: Webhook integration for real-time alerts sent directly to Discord or Slack.

- 🧪 Global Attack Simulator: A built-in Layer 2 packet injector to simulate spoofed attacks from across the globe for stress testing.

## 🏗️ System Architecture

- Sniffer Engine: Utilizes Npcap/Libpcap to capture raw frames at the Data Link layer.

- Analysis Layer: Decodes Raw payloads and matches them against known attack signatures.

- Database: Stores security events in a local SQLite/DuckDB instance for persistence.

- Action Layer: Communicates with the OS firewall and notification APIs.

- Visualization: A Streamlit frontend that queries the database and renders Plotly maps.

## 📸 Interface
<img width="1912" height="955" alt="image" src="https://github.com/user-attachments/assets/9c336296-a760-4154-96e9-925320e6a153" />

## ⚖️ Disclaimer

This project is for educational and authorized security testing purposes only. Running this on networks you do not own or have explicit permission to test is illegal and unethical. The author is not responsible for any misuse of this tool.
