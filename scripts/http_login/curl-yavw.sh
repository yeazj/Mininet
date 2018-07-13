#!/bin/bash

while true; do
	curl http://yavw.example.com:5000/login -d "email=admin@a.com&password=averysecureadminpassword"
	while true; do
		second=$((RANDOM % 255));
		tmp=$((second % 2));
		if [ "$tmp" = "0" ]; then
			break
		fi
	done
	third=$((RANDOM % 255));
	fourth=$(((RANDOM % 253) + 1)); 
	ifconfig h4-eth0 down; 
	ifconfig h4-eth0 "10.$second.$third.$fourth"; 
	ifconfig h4-eth0 up;
	sleep $((RANDOM % 5));
done
