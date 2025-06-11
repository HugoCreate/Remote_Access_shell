import socket as sk
import os
import subprocess as sub
import time

main_skt = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
ENV_HOST = "localhost"
ACCESS_PORT = 12555
CONFIRMATION_TOKEN = r"ACCESS_GIVEN{12341234}"

for i in range(0, 5):
  print("Starting shell enviroment... \\")
  time.sleep(1)
  os.system("cls" if os.name == "nt" else "clear")
  print("Starting shell enviroment... |")
  time.sleep(1)
  os.system("cls" if os.name == "nt" else "clear")
  print("Starting shell enviroment... /")
  time.sleep(1)
  os.system("cls" if os.name == "nt" else "clear")

  main_skt.bind((ENV_HOST, ACCESS_PORT))
  main_skt.listen() \\O main_skt apenas escuta por conexoes, quando uma conexão e feita(.accept) ela cria uma socket para a comunicacao
                    \\ja que o main_skt ja esta reservado para escutar.
  print(f"Waiting for connection... on {ENV_HOST}:{ACCESS_PORT}")
  conn, addr = main_skt.accept()

  with conn:
    entry_token = conn.recv(1024)
    if entry_token.decode() == r"Acces_Token_Test{12341234}":
        print(f"Connection stablished! With host: {addr}")
        main_skt.close()
        skt2 = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        skt2.connect(addr)
        skt2.sendall(CONFIRMATION_TOKEN.encode())
