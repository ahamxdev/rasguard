#!/bin/bash

sudo ip route add default via 192.168.43.1 dev wlan0 metric 1

echo "Default route via 192.168.43.1 (wlan0) has been set."
