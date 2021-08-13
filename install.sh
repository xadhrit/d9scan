#!/bin/bash

if [[ "$OSTYPE"  == "linux-gnu" || "darwin"  ]]; 
then
   echo -e "Donwloading requirements\n"
   python3 -m pip  install -r  requirements.txt && python3 scan.py -h
     
else
   echo -e "Donwloading requirements\n"
   python -m pip  install -r requirements.txt && python scan.py -h
  
fi

exit 0

