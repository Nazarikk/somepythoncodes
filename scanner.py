# -*- coding:utf -8 -*- 

from termcolor import colored
import socket

def fanc1():
    color_a = colored("[+] ", 'green')
    print("~"*50)
    host = input(color_a + "Host --> ")
    port = int(input(color_a + "Port --> "))
    print("~"*50)

    scan = socket.socket()

    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    try:
        scan.connect((host, port))
    except socket.error:
        print(color_b + "Port -- ", port, " -- [CLOSED]")
    else:
        print(color_c + "Port -- ", port, " -- [OPEN]")

def fanc2():
    color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    host = input(color_a + "Host --> ")
    print("\n")
    port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 445, 8080]

    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print(color_b + "Port -- ", i, " -- [CLOSED]")
        else:
            print(color_c + "Port -- ", i, " -- [OPEN]")

def fanc3():
    color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    host = input(color_a + "Host --> ")
    print("\n")
    port = [25, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 514, 515, 993, 995, 1080,1194, 1433, 1702, 1723, 3000, 3128, 3268, 3306, 3389, 5060, 5432, 5900, 8086, 10000, 20000]

    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print(color_b + "Port -- ", i, " -- [CLOSED]")
        else:
            print(color_c + "Port -- ", i, " -- [OPEN]")


print("~"*50)

print("\t[1] --- scan other port")
print("\t[2] --- scan list")
print("\t[3] --- my custom list")

print("~"*50, "\n")
text_a = input("[scan]--> ")

if text_a == "1":
    fanc1()
elif text_a == "2":
    fanc2()
elif text_a == "3":
    fanc3()
else:
    print(colored("Parametr not true!", 'red'))
