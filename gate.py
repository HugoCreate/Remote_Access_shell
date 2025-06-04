import socket as sk
import os
import time
import subprocess

#This is going to be the "controller" where the user can execute and attempt a connection in the remote shell enviroment.
#The main security measures i want to add is: 
#- The only way of accessing the shell enviroment (or attempt) is through this code "gate.py"
#- And to access the enviroment you must input the correct key (or keys). Or the "enviroment.py" program, after 3 failed attempts, will end itself and wait for a restart (manually).

print("Starting shell access gate... ")
time.sleep(1.5)
