#!/bin/bash

cur_time=`date +'%Y_%m_%d__%H_%M_%S'`;
filename="tmp.$cur_time"

echo "hello" > $filename

#ftp -n 10.0.0.84 21 << EOF
ftp -n ftp.example.com 21 << EOF
quote USER user
quote PASS `$RANDOM`
quit
EOF

