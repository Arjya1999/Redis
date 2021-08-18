# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:29:07 2021

@author: ARJYA
"""

import redis

r = redis.Redis(host='localhost',port=6379)

r.mset({"France":"Paris","Germany":"Berlin"})

print(r.get("Germany"))
