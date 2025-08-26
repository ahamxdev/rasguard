# Raspberry Pi Setup Guide

This guide will walk you through the process of setting up the Raspberry Pi to run necessary services on boot, including installing Python dependencies, copying systemd service files, and enabling the services.

## 0. Clone the Project

First, clone the project repository to your Raspberry Pi using the following command:

```bash
git clone https://github.com/ahamxdev/rasguard.git
cd rasguard
```

Make sure you navigate into the rasguard directory before proceeding with the next steps.

## 1. Install Python Dependencies

Before setting up the services, you'll need to install the required Python packages that are used in the code. These packages are not included by default in Raspberry Pi OS.

Run the following commands to install them:

```bash
# Update the system and install required packages
sudo apt update
sudo apt install -y \
    build-essential \
    python3-dev \
    libnetfilter-queue-dev \
    libnfnetlink-dev \
    python3-pip
```

## 2. Create and Activate Virtual Environment

It is recommended to use a virtual environment to keep dependencies isolated.  
Create and activate a virtual environment with:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Python Dependencies

Install the Python packages required for this project.  
All dependencies are listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 4. Systemd Services Explanation

The **systemd services** are responsible for automatically running your scripts after boot. These services ensure that the necessary network configurations, packet monitoring, and firewall rules are applied on startup.

- **`packet_queue.service`**: This service is responsible for setting up the packet queue using `iptables` and `netfilterqueue` to monitor and analyze incoming network packets.
  
- **`bridge_setup.service`**: This service is responsible for creating a network bridge between two Ethernet interfaces (`eth0` and `eth1`), enabling the Raspberry Pi to act as a bridge for connected devices.

- **`setup_network.service`**: This service configures the default network route, ensuring that the Raspberry Pi uses the correct gateway for internet access via the wireless interface (`wlan0`).

- **`br_netfilter.service`**: This service is responsible for enabling the `br_netfilter` kernel module, which allows Layer 3 (L3) packet filtering on Layer 2 (L2) bridge interfaces. It ensures that packets forwarded through the bridge (e.g., between `eth0` and `eth1`) can be inspected and processed by tools like `iptables`, enabling deep network monitoring and control.

By enabling and starting these services, you ensure that these tasks are automatically executed when the Raspberry Pi boots.

> **Note:**  
> To ensure that the Raspberry Pi maintains internet connectivity while acting as a bridge, you need to configure a default route using the Wi-Fi interface (`wlan0`). This is especially important when bridging wired connections (`eth0`/`eth1`) and still requiring internet access.

The custom route is added manually with a lower metric (e.g., `metric 1`) to prioritize the Wi-Fi interface for outgoing traffic. This ensures that the Raspberry Pi sends internet-bound traffic through the Wi-Fi network instead of the bridged interfaces.

### Example Route Setup

The following command is typically used in the `setup_network.sh` script or `setup_network.service`:

```bash
sudo ip route add default via 192.168.1.1 dev wlan0 metric 1
```

---

## 5. Copying Service Files

To copy the service files to your Raspberry Pi, use the following command:

```bash
sudo cp systemd_services/*.service /etc/systemd/system/
```

> **Note:**  
> In each `.service` file, there's a line like the one below:

```ini
ExecStart=/bin/bash /home/ahamdev/rasguard/scripts/*.sh
If your username is pi and your project is located at /home/pi/rasguard/, you should modify the line as follows:
ExecStart=/bin/bash /home/pi/rasguard/scripts/*.sh
```

## 6. Enable the services

This step ensures that the services will automatically start after the Raspberry Pi boots.

```bash
sudo systemctl enable packet_queue.service
sudo systemctl enable bridge_setup.service
sudo systemctl enable setup_network.service
sudo systemctl enable br_netfilter.service
```

## 7. Start the services immediately

This will start the services right away, without having to reboot the Raspberry Pi.

```bash
sudo systemctl start packet_queue.service
sudo systemctl start bridge_setup.service
sudo systemctl start setup_network.service
sudo systemctl start br_netfilter.service
```

## 8. Checking the Service Status

To verify that your services are running correctly, use the following commands:

```bash
sudo systemctl status packet_queue.service
sudo systemctl status bridge_setup.service
sudo systemctl status setup_network.service
sudo systemctl status br_netfilter.service
```

## 9. Reboot and Run the Application

After completing all setup steps and enabling the required services, it's recommended to reboot your Raspberry Pi to ensure all configurations and services are applied properly.

Once the system has rebooted, navigate to the src directory where your main Python script is located, and run the DoS protection script:
```bash
sudo reboot
cd /home/your-username/rasguard/
sudo source venv/bin/activate
```

Run the following command to reboot:

```bash
cd src/
‍‍‍sudo python3 dos_protection.py
‍‍‍‍‍‍‍‍‍‍‍‍‍```
