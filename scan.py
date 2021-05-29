#!/usr/bin/python3

"""
d9scan -  by Adhrit
https://github.com/xadhrit/d9scan

"""

import socket
import os
import time
import sys
import argparse
import subprocess
import requests 
from printcolors import *
from datetime import  datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
   
# Main Function
def main():
    socket.setdefaulttimeout(0.30)
    #argument parser
    parser = argparse.ArgumentParser(description='Network Scanning with d9scan')
    parser.add_argument('target', type=str, help='Domain or IP address of Target')
    args = parser.parse_args()
    target = args.target
    
    # Start scan with clear terminal
    subprocess.call('clear', shell=True)
    
    #welcome d9scan poison banner.    
    
    print("""   
            
          @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@
          @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@ @@@  
          @@!  @@@  @@!  @@@  !@@       !@@       @@!  @@@  @@!@!@@@  
          !@!  @!@  !@!  @!@  !@!       !@!       !@!  @!@  !@!!@!@!  
          @!@  !@!  !!@!!@!!  !!@@!!    !@!       @!@!@!@!  @!@ !!@!  
          !@!  !!!    !!@!!!   !!@!!!   !!!       !!!@!!!!  !@!  !!!  
          !!:  !!!       !!!       !:!  :!!       !!:  !!!  !!:  !!!  
          :!:  !:!       !:!      !:!   :!:       :!:  !:!  :!:  !:!  
           :::: ::  ::::: ::  :::: ::    ::: :::  ::   :::   ::   ::  
          :: :  :    : :  :   :: : :     :: :: :   :   : :  ::    :   """)
    print(" \n")
    print("%s\t\td9scan - Network Scanner with Backdoor Detection "%(yellow))
 
    time.sleep(1)
    print("\n")
    #target = input("Enter your target IP address or URL here: ")
    error = ("%sInvalid Input"%red)
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n%s%sInvalid format. Please use a correct IP or web address\n"%(bad, red))
        sys.exit()
    
    
    print("Scanning target :  {} - {} ".format(target,t_ip), end='')
    print(" |  Time started: "+ str(datetime.now()))
    
    t1 = datetime.now()

 
    def generalscan(target):

       s = "nmap -v -A {}".format(target)
       os.mkdir(target)
       os.chdir(target)
       print("%s"%(green))
       os.system(s)
       
   
    generalscan(target) 
    t2 = datetime.now()
    total = t2 - t1
    #print("Port scan completed in "+str(total))
    print("^" * 60)
    print("%s Recommended Nmap scan:"%white)
    print("-" * 60)
    
    #print("%snmap -p{ports} -sV -sC -T4 -Pn -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=target)%blue)
   
    outfile = "nmap -sV --script=http-malware-host {ip}".format(ip=target)
    print(outfile)
    print("-" * 60)
    backdoor = "nmap -sV --script http-dlink-backdoor {ip}".format(ip=target) 
    ftpbackdoor = "nmap --script ftp-proftpd-backdoor -p 21 {ip}".format(ip=target)
    t3 = datetime.now()
    total1 = t3 - t1

    
#Nmap Integration 

    def automate():
       choice = '0'
       while choice =='0':
          print("Would you like to run Nmap or quit to terminal?")
          
          print("%s0 = Run suggested Nmap scan"%green)
          print("%s1 = Run Ftp backdoor Detection "%green)
          print("%s2 = Run http-dlink  BackDoor Detection"%green)
          print("%s3 = Run another d9 scan"%green)
          print("%s4 = Exit to terminal"%green)
         
          choice = input("Option Selection: ")
          if choice == "0":
             try:
                #print(yellow+outfile)
                os.mkdir(target)
                os.chdir(target)
                os.system(outfile)
                t3 = datetime.now()
                total1 = t3 - t1
                print("-" * 60)
                print("Malware Detection scan completed in "+str(total1))
                print("")
                print("%sPress 1 to go back  or  enter to quit..."% white)
                input()
             except FileExistsError as e:
                print(e)
                exit()
          elif choice == "1":
              try:
                  #print(white+ftpbackdoor)
                  os.mkdir(target)
                  os.chdir(target)
                  os.system(ftpbackdoor)
                  t3 = datetime.now()
                  total1 = t3-t1
                  print("Ftp Backdoor Scan completed in "+str(total1)) 
                  print("%sPress 2 to go back and enter to quit..."%white)
                  uinput = input()
                  if uinput == '2':
                      automate()
                  elif uinput():
                      exit()
                  else:
                      sys.exit(0)
              except FileExistsError as e:
                  print(e)
                  exit()
          elif choice == "2":
              try:
                  #print(red+backdoor)
                  os.mkdir(target)
                  os.chdir(target)
                  os.system(backdoor)
                  t3 = datetime.now()
                  total1 = t3-t1
                  print("Combined scan completed in " + str(total1))
                  print("%s Press 3 to go back and enter to quit..."%white)
                  uinput = input()
                  if uinput == '3':
                      automate()
                  elif uinput():
                      exit()
                  else:
                      sys.exit(0)
              except FileExistsError as e:
                  print(e)
                  exit()
          elif choice =="3":
             main()
          elif choice =="4":
             sys.exit()
          else:
             print("%sPlease make a valid selection"%yellow)
             automate()
    automate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n%sGoodbye!"%red)
        quit()
