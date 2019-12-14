#!/usr/bin/env python3

from zipfile import ZipFile
from sys import argv
from os.path import isfile

if(len(argv) != 2):
    print("Usage:\n ./cracker.py <zipfile-path>")
    exit(1)

zipPath = argv[1]

if(not isfile(zipPath)):
    print("this zip does not exists")
    exit(1)

zfile = ZipFile(zipPath)
passfile = open("pass.list")
content = passfile.readlines()
passwords = [x.strip() for x in content]

for password in passwords:
    print("trying password: ", password)
    try:
        zfile.extractall(pwd=str.encode(password))
        print(('password is ' + password))
        break
    except:
        pass
