#!/bin/bash

sudo iptables -A FORWARD -i br0 -j NFQUEUE --queue-num 0

sudo iptables -L -v -n

