#!/bin/bash

while true; do
	tmp=$((RANDOM % 15))
	#tmp2=$((RANDOM % 3))
	#ctr=0
	
	if [ "$tmp" = "0" ]; then
		./wget_fail.sh
		#ctr=$((ctr + 1))
	else
		./wget.sh
		#ctr=$((ctr + 1))
	fi
	
	#if [[ "$ctr" = "$tmp2" ]]; then
		#./even_norm_change_ip.sh
		#ctr=0
	#fi
	rm -rf tmp*
done
