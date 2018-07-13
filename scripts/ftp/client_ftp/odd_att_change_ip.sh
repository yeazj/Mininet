#!/bin/bash

while true; do
	second=$((RANDOM % 255));
	tmp=$((second % 2));
	if [ "$tmp" = "1" ]; then
		break
	fi
done
third=$((RANDOM % 255));
fourth=$(((RANDOM % 253) + 1)); 
ifconfig h1-eth0 down; 
ifconfig h1-eth0 "10.$second.$third.$fourth"; 
ifconfig h1-eth0 up; 
