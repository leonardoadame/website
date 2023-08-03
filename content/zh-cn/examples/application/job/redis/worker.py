#!/usr/bin/env python

import time
import rediswq

host="redis"
# 如果你未在运行 Kube-DNS，请取消下面两行的注释
# import os
# host = os.getenv("REDIS_SERVICE_HOST")

q = rediswq.RedisWQ(name="job2", host=host)
print(f"Worker with sessionID: {q.sessionID()}")
print(f"Initial queue state: empty={str(q.empty())}")
while not q.empty():
  item = q.lease(lease_secs=10, block=True, timeout=2)
  if item is not None:
    itemstr = item.decode("utf-8")
    print(f"Working on {itemstr}")
    time.sleep(10) # 将你的实际工作放在此处来取代 sleep
    q.complete(item)
  else:
    print("Waiting for work")
print("Queue empty, exiting")
