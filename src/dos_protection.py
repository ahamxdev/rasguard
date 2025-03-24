from netfilterqueue import NetfilterQueue
from scapy.all import IP, TCP
import subprocess
import threading
import time

SYN_LIMIT = 10
ACK_LIMIT = 10
FIN_LIMIT = 10
CONN_LIMIT = 20
BLOCK_TIME = 300

ip_requests = {}

def block_ip(ip):
    """Block attacker ip"""
    print(f"Blocking IP: {ip} for {BLOCK_TIME} seconds")
    subprocess.call(['sudo', 'iptables', '-I', 'INPUT', '-s', ip, '-j', 'DROP'])
    time.sleep(BLOCK_TIME)
    subprocess.call(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'])
    print(f"Unblocking IP: {ip}")

def process_packet(packet):
    """Processing input packets NFQUEUE"""
    scapy_pkt = IP(packet.get_payload())
    if scapy_pkt.haslayer(IP) and scapy_pkt.haslayer(TCP):
        ip_src = scapy_pkt[IP].src
        flags = scapy_pkt[TCP].flags

        if ip_src not in ip_requests:
            ip_requests[ip_src] = {"SYN": 0, "ACK": 0, "FIN": 0, "CONN": 0}

        if flags == 2:  # SYN
            ip_requests[ip_src]["SYN"] += 1
        elif flags == 16:  # ACK
            ip_requests[ip_src]["ACK"] += 1
        elif flags == 1:  # FIN
            ip_requests[ip_src]["FIN"] += 1
        elif flags == 18:  # SYN-ACK
            ip_requests[ip_src]["CONN"] += 1

        if (ip_requests[ip_src]["SYN"] > SYN_LIMIT or
            ip_requests[ip_src]["ACK"] > ACK_LIMIT or
            ip_requests[ip_src]["FIN"] > FIN_LIMIT or
            ip_requests[ip_src]["CONN"] > CONN_LIMIT):

            print(f"⚠️ Possible DoS Attack from {ip_src}")
            threading.Thread(target=block_ip, args=(ip_src,)).start()
            ip_requests[ip_src] = {"SYN": 0, "ACK": 0, "FIN": 0, "CONN": 0}

    packet.accept()

queue = NetfilterQueue()
queue.bind(1, process_packet)

print("🔍 Monitoring and forwarding packets...")
try:
    queue.run()
except KeyboardInterrupt:
    print("\nStopping...")
    subprocess.call(["sudo", "iptables", "-F"])
    subprocess.call(["sudo", "iptables", "-X"])
