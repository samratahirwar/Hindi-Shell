# Hindi Shell 
# Author: Samrat Ahirwar
# Date: 15/05/2022 

clear
echo "*** हिंदी शैल ***" | sed  -e :a -e "s/^.\{1,$(tput cols)\}$/ & /;ta" | tr -d '\n' | head -c $(tput cols)
echo ""

python3 ./hindi_shell.py

