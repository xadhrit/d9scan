#!/bin/bash

#nmap -sV --script=http-malware-host {ip}
#nmap -sV --script http-dlink-backdoor {ip}
#nmap --script ftp-proftpd-backdoor -p 21 {ip}

printf "d9scan from shell :) \n\n"
printf "Enter target's domain or IP : "
read IP 

function options(){
   printf "----------------- Choose One option ----------------------- "
   echo -e  " 1 for http-malware-host scan"
   echo -e  " 2 for http-dlink-backdoor scan"
   echo -e  " 3 for ftp-proftpd-backdoor scan"
   echo -e "  4 for all  "
   echo -e "  5 Exit   "
   read OPTION

   
   if [[ $OPTION == '1' ]] ;
   then
       nmap -sV --script=http-malware-host $IP
   elif [[ $OPTION == '2'  ]] ;
   then
      nmap -sV --script http-dlink-backdoor $IP
   elif [[ $OPTION == '3'  ]];
   then
      nmap --script ftp-proftpd-backdoor -p 21 $IP
   elif [[ $OPTION == '4'  ]] ;
   then
       nmap -sV --script=http-malware-host $IP
       nmap -sV --script http-dlink-backdoor $IP
       nmap --script ftp-proftpd-backdoor -p 21 $IP
   elif [[ $OPTION == '5'  ]];
   then 
        exit 0
   else
       printf "Invalid Option, Exiting..... \n"
       exit 0

   fi

}
nmap -v -A $IP
options
exit 
