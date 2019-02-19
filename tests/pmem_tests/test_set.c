#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hiredis.h"

int main(int argc, char **argv) {
    unsigned int j, isunix = 0;
    redisContext *c;
    redisReply *reply;
    const char *hostname = "127.0.0.1";

    if (argc > 1) {
        if (*argv[1] == 'u' || *argv[1] == 'U') {
            isunix = 1;
            /* in this case, host is the path to the unix socket */
            printf("Will connect to unix socket @%s\n", hostname);
        }
    }
    int port = (argc > 1) ? atoi(argv[1]) : 6379;
    	
    struct timeval timeout = { 1, 500000 }; // 1.5 seconds
    if (isunix) {
        c = redisConnectUnixWithTimeout(hostname, timeout);
    } else {
        c = redisConnectWithTimeout(hostname, port, timeout);
    }
    if (c == NULL || c->err) {
        if (c) {
            printf("Connection error: %s\n", c->errstr);
            redisFree(c);
        } else {
            printf("Connection error: can't allocate redis context\n");
        }
        exit(1);
}


    /* Set a key using binary safe API */
//reply = redisCommand(c,"SET %b %b", "foo", (size_t) 3, "value-foo", (size_t) 9);
    reply = redisCommand(c,"SET %s %s", "foo", "value-foo");
    printf("\nSET status: %s\n", reply->str);
    freeReplyObject(reply);


    redisFree(c);

    return 0;
}
