#!/usr/bin/env python
import redis
import os

port=1300
pool = redis.ConnectionPool(host = 'localhost', port = port, decode_responses = True)
server = redis.Redis(connection_pool = pool)

logfile = open("pmreorder_log", "a")

# Returns 0 if consistenct, 1 otherwise
def  check_consistency(server):
    consistency = 1 
    print "=== check consistency ==="
    #value = server.get("foo").decode('utf-8')
    value = server.get("foo")
    #print(value)
    if str(value) == "value-foo":
        consistency = 0
        print value
        print "CONSISTENT"
        logfile.write("\nCONSISTENT : " + str(value) + "\n")

    else:
        print value
        print "INCONSISTENT"
        logfile.write("\nINCONSISTENT : " + str(value) + "\n")

    logfile.close()
    return consistency

if __name__ == "__main__":
    check_consistency(server)
