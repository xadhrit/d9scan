#!/bin/bash

CYAN="\e[36m"
GREEN="\e[32m"
ENDCOLOR="\e[0m"

printf "${CYAN} d9scan from shell :) \n\n"
printf "Enter target's domain or IP : "
read IP 

function options(){
   printf "----------------- Choose One option -----------------------${GREEN} "
   echo -e  " 1 for http-malware-host scan"
   echo -e  " 2 for http-dlink-backdoor scan"
   echo -e  " 3 for ftp-proftpd-backdoor scan"
   echo -e "  4 for all  "
   echo -e "  5 Exit   "
   read OPTION

   
   if [[ $OPTION == '1' ]] ;
   then
       echo -e "${GREEN} nmap -sv --script=http-malware-host ${IP} \n"
       nmap -sV --script=http-malware-host $IP
   elif [[ $OPTION == '2'  ]] ;
   then
      echo -e "${GREEN} nmap -sV --script http-dlink-backdoor ${IP}\n "
      nmap -sV --script http-dlink-backdoor $IP
   elif [[ $OPTION == '3'  ]];
   then
      echo -e "${GREEN} nmap --script ftp-proftpd-backdoor -p 21 ${IP}\n "
      nmap --script ftp-proftpd-backdoor -p 21 $IP
   elif [[ $OPTION == '4'  ]] ;
   then
       echo -e "${CYAN} Running all Scripts\n "
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
"${GREEN} nmap -v -A ${IP} \n"
nmap -v -A $IP
options
exit 
