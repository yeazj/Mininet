#!/bin/bash

while true; do 
	python smtpd_senddata.py;  
	while true; do
		second=$((RANDOM % 255));
		tmp=$((second % 2));
		if [ "$tmp" = "0" ]; then
			break
		fi
	done
	third=$((RANDOM % 255));
	fourth=$(((RANDOM % 253) + 1)); 
	ifconfig h2-eth0 down; 
	ifconfig h2-eth0 "10.$second.$third.$fourth"; 
	ifconfig h2-eth0 up;
	sleep $((RANDOM % 5));
done
