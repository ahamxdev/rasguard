# RasGuard: A Layer 2 Firewall for Detecting and Mitigating DDoS Attacks on Raspberry Pi

## Introduction
In today's interconnected world, **Distributed Denial of Service (DDoS)** attacks pose a significant threat to network stability and service availability. These attacks overwhelm systems with malicious traffic, leading to downtime and service degradation. 

This project focuses on building a **Layer 2 firewall** using a **Raspberry Pi** to detect and mitigate specific types of **TCP-based DDoS attacks** (SYN Flood, ACK Flood, TCP Connection Flood, and FIN Flood). The firewall is designed to analyze traffic between two network interfaces (ports) and block malicious IP addresses for a set period, providing a robust defense against common DDoS attack methods.

---

## Project Objectives
- ✅ **Implement a Layer 2 firewall** on a Raspberry Pi to analyze and forward packets between two network interfaces  
- ✅ **Detect and mitigate TCP-based DDoS attacks**, specifically SYN Flood, ACK Flood, TCP Connection Flood, and FIN Flood  
- ✅ **Automate IP blocking** for attackers based on predefined attack thresholds (e.g., blocking an IP for 5 minutes after attack detection)  
- ✅ **Leverage Python** to monitor and analyze network traffic in real-time, utilizing libraries such as `scapy` and `NetfilterQueue`  
- ✅ **Create a scalable solution** for real-time DDoS attack mitigation

---

## Required Hardware and Software

### 📌 Hardware
- **Raspberry Pi 3 Model B+** or later  
- **microSD Card** (Minimum 16GB, Class 10)  
- **5V/2.5A Power Adapter**  
- **Ethernet cables** for connecting Raspberry Pi to network interfaces  

### 🛠️ Software
- **Raspberry Pi OS (Lite)** – Minimal OS for running firewall applications  
- **iptables** & **nftables** – For setting up and configuring firewall rules  
- **scapy** – Python library for crafting and analyzing network packets  
- **NetfilterQueue** – Python library for interacting with `iptables` queueing system  
- **Python 3.x** – For writing custom scripts to detect and mitigate DDoS attacks  
- **tcpdump** – Network traffic analysis tool for capturing and inspecting packets  

---

## Implementation Steps

1. **Setup Raspberry Pi and OS**  
   - Install Raspberry Pi OS on a microSD card  
   - Update system packages and optimize network settings for firewall operation  

2. **Network Bridge Setup**  
   - Configure a **Layer 2 bridge** between two network interfaces (e.g., eth0 and eth1) on the Raspberry Pi  
   - Enable packet forwarding between interfaces and set up iptables for traffic routing  

3. **DDoS Attack Detection**  
   - Implement packet analysis using **scapy** to detect **SYN Flood**, **ACK Flood**, **TCP Connection Flood**, and **FIN Flood**  
   - Set thresholds for attack detection (e.g., more than 10 SYN packets in 1 second indicates a SYN Flood)  
   - Develop a mechanism to **block the source IP address** for a set time after detecting a flood attack  

4. **Python Script for Real-Time Monitoring**  
   - Use **NetfilterQueue** to receive and inspect packets from iptables queues  
   - Implement attack detection logic to check for patterns indicative of DDoS attacks  
   - Automatically block IPs involved in attacks using **iptables**  

5. **Testing and Optimization**  
   - Test the firewall by simulating various DDoS attack scenarios (e.g., using tools like `hping3` or **LOIC**)  
   - Analyze the performance of the firewall and optimize packet inspection algorithms for better efficiency  

---

## Results and Practical Applications

✅ **Real-time DDoS attack detection** and mitigation  
✅ **Improved network security** for small to medium-sized networks  
✅ **Cost-effective solution** based on Raspberry Pi for defending against TCP-based DDoS attacks  
✅ **Scalable architecture** suitable for various network configurations and IoT environments  

---

## Future Improvements
🔹 **Advanced attack detection using AI** – Implement machine learning algorithms for more advanced and dynamic threat detection  
🔹 **Web-based dashboard** for monitoring and configuration – A graphical interface to display attack logs, alerts, and manage firewall settings  
🔹 **Automated attack response** – Develop a more automated system to react to specific attack patterns  
🔹 **Support for multi-interface setups** – Expand the project to support more complex network topologies  

---

## Conclusion
This project provides a **practical solution** for protecting networks from **TCP-based DDoS attacks** by leveraging the capabilities of the Raspberry Pi. By analyzing network traffic at Layer 2 and blocking malicious IP addresses in real-time, this firewall offers an **affordable and efficient defense** against common DDoS threats.

---

## 💡 Contact & Contributions
🔹 **Contributions are welcome!** Feel free to open a pull request, report issues, or suggest improvements.  
🔹 For any questions or collaboration, feel free to reach out! Let's make this project better together.  
