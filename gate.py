import socket as sk
import os
import time
import subprocess
import re

#This is going to be the "controller" where the user can execute and attempt a connection in the remote shell enviroment.
#The main security measures i want to add is: 
#- The only way of accessing the shell enviroment (or attempt) is through this code "gate.py"
#- And to access the enviroment you must input the correct key (or keys). Or the "enviroment.py" program, after 3 failed attempts, will end itself and wait for a restart (manually).


LOCALHOST = "localhost"
LOCAL_PORT = 12400


print("Starting shell access gate... ")
time.sleep(1.5)
main_skt = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
os.system("cls" or "clear")

TOKEN = r"Acces_Token_Test{12341234}"

ip_pattern_rgx = r'''
^
(                                  # Start of IP
  (25[0-5]|                        # 250–255
   2[0-4][0-9]|                    # 200–249
   1[0-9]{2}|                      # 100–199
   [1-9][0-9]?|                    # 1–99
   0)                              # 0
  \.
){3}
(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)   # Last segment
$
'''

loop1 = True
while(loop1):
    env_ip = input("Enter the public IP of the enviroment: ")

    print("Attempting connection", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)

    if re.fullmatch(ip_pattern_rgx, str(env_ip), re.VERBOSE):
        print("Valid IP address!")
        loop2 = True
        while(loop2):    
            env_port = int(input("Now enter the port of enviroment access: "))
            print("Attempting port connection...")
            main_skt.connect((env_ip, env_port))
            result = main_skt.recv(1024)
            if result == 0:
                print(f"The host is up! Host '{str(env_ip)}', In the access port '{str(env_port)}'")
                loop2 = False
                loop1 = False
                main_skt.close()
                skt1 = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
                skt1.connect(env_ip, env_port)
                skt1.sendall(TOKEN.encode())
                print("Access Token sent for evaluation. Waiting for response...")
                skt1.close()
                skt2 = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
                skt2.bind((LOCALHOST, LOCAL_PORT))
                skt2.listen()
                conn, addr = skt2.accept()
                with conn:
                    print(f"Connected to {addr}")
                    enviroment_pass = skt2.recv(1024)
                    if enviroment_pass.decode() == r"ACCESS_GIVEN{12341234}":
                        print("Succesfully connected to shell enviroment!! Starting shell access.")


            else:
                print(f"The {env_port} is either not open or doesn't host the enviroment shell program. Try again...")
    else: 
        print("Invalid IP address, try a new one (or write 'exit' to end the program): ")
