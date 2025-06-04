import socket as sk
import threading
import os
import subprocess as sub
import time

main_skt = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

for i in range(0, 8):
  print("Starting shell enviroment... \")
  time.sleep(0.4)
  sub.Popen("cls")
  print("Starting shell enviroment... |")
  time.sleep(0.4)
  sub.Popen("cls")
  print("Starting shell enviroment... /")
  time.sleep(0.4)
