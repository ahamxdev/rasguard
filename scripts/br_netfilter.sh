#!/bin/bash

sudo modprobe br_netfilter

sudo sysctl -w net.bridge.bridge-nf-call-iptables=1
sudo sysctl -w net.bridge.bridge-nf-call-ip6tables=1
sudo sysctl -w net.bridge.bridge-nf-call-arptables=1

sudo sysctl -p
