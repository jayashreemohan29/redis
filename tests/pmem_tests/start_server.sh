#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "Input the port, log file name for pmemcheck and the root project directory path"
	exit 1
fi

export PMEMOBJ_COW=1
export PMEM_IS_PMEM_FORCE=1

port=$1
log_file=$2
path=$3

#Assuming redis client and server are not installed, trigger it from the src directory

echo "---Starting Redis-pmem server with valgrind---"
valgrind --tool=pmemcheck --log-stores=yes --print-summary=no --log-file=$log_file --log-stores-stacktraces=yes --log-stores-stacktraces-depth=2 --expect-fence-after-clflush=yes  $path/src/redis-server $path/redis.conf --port $port &

sleep 5

