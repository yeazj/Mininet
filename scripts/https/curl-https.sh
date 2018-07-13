#!/bin/bash

while true; do
	#curl -k -u guest:password https://secure.example.com/messages
	curl -k https://secure.example.com/login --data "username=admin&password=password"
	while true; do
		second=$((RANDOM % 255));
		tmp=$((second % 2));
		if [ "$tmp" = "0" ]; then
			break
		fi
	done
	third=$((RANDOM % 255));
	fourth=$(((RANDOM % 253) + 1)); 
	ifconfig h5-eth0 down; 
	ifconfig h5-eth0 "10.$second.$third.$fourth"; 
	ifconfig h5-eth0 up;
	sleep $((RANDOM % 5));
done
