#!/usr/bin/env python
# -*- coding: utf-8 -*-
import docker




client = docker.from_env()

#client.containers.run(image, name=name, environment=["param1="+param1,"param2="+param2], detach=True, auto_remove=True)


try:
  c = client.containers.get("python-docker-app-run")
  print("kontejner existuje")

except:
  print("kontejner neexistuje")
#print(c.name)

c=client.containers.list()
print(c)
for i in c:
    print(i)
    print(i.name)
