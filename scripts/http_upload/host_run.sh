#!/bin/bash


#curl -F file=@/root/tmp/test2 http://web.example.com:80
while true; do
	#wget -O - 10.0.0.82:80
	wget -O - web.example.com:80
	while true; do
		second=$((RANDOM % 255));
		tmp=$((second % 2));
		if [ "$tmp" = "0" ]; then
			break
		fi
	done
	third=$((RANDOM % 255));
	fourth=$(((RANDOM % 253) + 1)); 
	ifconfig h3-eth0 down; 
	ifconfig h3-eth0 "10.$second.$third.$fourth"; 
	ifconfig h3-eth0 up;
	sleep $((RANDOM % 5));
done
