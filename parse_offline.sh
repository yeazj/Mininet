#!/bin/bash

tcpdump -i nat0-eth0 -w `date '+%Y_%m_%d__%H_%M_%S'.pcap`
