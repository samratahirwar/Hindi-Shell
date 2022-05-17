import sys
import subprocess
from prog_dict import prog_dict,option_dict
import os
from englisttohindi.englisttohindi import EngtoHindi

def translate(sent):
    trans = EngtoHindi(message=sent)
    return trans.convert

def convert(command):
    new_command=None
    try:
        command=command.split(' ')
        rest_command=command[1:]
        for i in range(len(rest_command)):
            option=rest_command[i].strip()
            if '-' ==option[0]:
                option=option_dict[option[1:]]
                rest_command[i]='-'+option

        new_command=prog_dict[command[0].strip()]+' '+' '.join(rest_command[1:])
    except KeyError:
            print(command)
            prog_dict[command[0].strip()]=''
            return None
    return new_command

command=None
while True:
    command=str(input('॥ '),)
    if command=='अन्त':
        break
    if command.strip()==None:
        continue
    command=convert(command)
    if command==None:
        continue
    try:
        output=subprocess.check_output(command, shell=True, text=True)
    except Exception as e:
        output=translate(str(e))
    print(output)

print('॥ समाप्त ॥')
