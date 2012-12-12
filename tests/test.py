from multiprocessing import Queue, Process
import Queue as QueueException
import sys
import os
import redis

r = 1
n = 100
w = 15

if( len(sys.argv) > 1 ):
    r = int(sys.argv[1])

if( len(sys.argv) > 2 ):
    n = int(sys.argv[2])

def f(seed, count):
    r = redis.Redis("localhost", port=2000)
    for i in xrange(count):
        key = "%s-%s"%(seed, i)
        try:
            r.set( key, str(i) )
        except:
            pass

if __name__=='__main__':
    print r, n
    p = []
    for i in xrange(r):
        p.append(Process(target=f, args=(r, n)))
        p[i].start()

    for i in xrange(r):
        p[i].join()
