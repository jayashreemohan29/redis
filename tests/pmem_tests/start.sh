#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Input the port, the root project directory path"
	exit 1
fi

port=$1
path=$2

#Assuming redis client and server are not installed, trigger it from the src directory

echo "---Starting Redis-pmem server without valgrind---"
$path/src/redis-server $path/redis.conf --port $port &

sleep 4

