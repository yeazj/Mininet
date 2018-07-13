#!/bin/bash

echo "Please check interface, it may change after restart"

tcpdump -i nat0-eth0 -u -w - | tcpreplay -i eth1 - -v
