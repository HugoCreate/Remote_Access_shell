import socket as sk
import threading
import os
import subprocess as sub
import time

main_skt = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

for i in range(0, 5):
  print("Starting shell enviroment... \\")
  time.sleep(1)
  os.system("cls")
  print("Starting shell enviroment... |")
  time.sleep(1)
  os.system("cls")
  print("Starting shell enviroment... /")
  time.sleep(1)
  os.system("cls")
