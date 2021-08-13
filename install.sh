#!/bin/bash

if [[ "$OSTYPE"  == "linux-gnu" || "darwin"  ]]; 
then
   echo -e "Donwloading requirements\n"
   python3 -m pip  install -r  requirements.txt
     
else
   echo -e "Donwloading requirements\n"
   python -m pip  install -r requirements.txt
  
fi

exit 0

