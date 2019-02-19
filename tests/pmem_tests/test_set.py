#!/usr/bin/env python
import os
import time
import redis
import sys

port = 1300
#logfile = "store_log_set.log"
if len(sys.argv) < 3:
    print "Usage : ./test_set.py <store_log_name> <engine>"
    sys.exit(2)
logfile = sys.argv[1]
engine = sys.argv[2]

path = "~/projects/redis-3.2nvml"


os.system("export PMEMOBJ_COW=1")

init_command = "./init.sh " + str(port) + " " + path
start_command = "./start_server.sh " + str(port) + " " + logfile + " " + path
stop_command = "./stop_server.sh"
#pmreorder_command = "python3 ../../../pmdk-test/src/tools/pmreorder/pmreorder.py -l " + logfile  + " -o pmreorder_log -e debug -r " + engine + " -p ./test_set_check.py"
start_novalgrind = "./start.sh " + str(port) + " " + path
pmreorder_command = "python3 ../../../pmdk-test/src/tools/pmreorder/pmreorder.py -l try.log -o pmreorder_log -e debug -r " + engine + " -p ./check_consistency.py"

pool = redis.ConnectionPool(host = 'localhost', port = port, decode_responses = True)
server = redis.Redis(connection_pool = pool)

def set_test(server):
    print("=== test single set ===")
    server.set("foo", "value-foo".encode('utf-8'))
    value = server.get("foo").decode('utf-8')
    print(str(value))

if __name__ == "__main__":
    os.system(init_command)
    os.system(start_command)
    pool = redis.ConnectionPool(host = 'localhost', port = port, decode_responses = True)
    server = redis.Redis(connection_pool = pool)
    set_test(server)
    os.system(stop_command)
    print ("------Running PMREORDER------")
    os.system(start_novalgrind)
    os.system(pmreorder_command)
    os.system(stop_command)
