#!/bin/bash

cur_time=`date +'%Y_%m_%d__%H_%M_%S'`;
filename="tmp.$cur_time"
#ran_str=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
#ran_str=`date | md5sum | fold -w $((RANDOM % 33))`
ran_str=`date | md5sum | cut -c 1-$((RANDOM % 33))`
echo $ran_str > $filename

#ftp -n 10.0.0.84 21 << EOF
ftp -n ftp.example.com 21 << EOF
quote USER user
quote PASS 12345
put $filename
quit
EOF

