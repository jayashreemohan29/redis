#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Input the port, and the root project directory path"
	exit 1
fi

export PMEMOBJ_COW=1
export PMEM_IS_PMEM_FORCE=1

port=$1
path=$2

rm -rf /mnt/pmem/*

#Assuming redis client and server are not installed, trigger it from the src directory

echo "---Starting Redis-pmem server for initialization---"
./start.sh $port $path
./stop_server.sh 
echo "--- Done initializing---"

