#!/usr/bin/env bash

# It should be Linux terminal, use git bash in Windows

cd ~/OneDrive/Documentos/ || exit

file="Microsoft.PowerShell_profile.ps1"

if [ ! -f "$file" ]; then
    touch "$file"
    echo "File created: $file"
    towrite="function pycharm { start '' '%USERPROFILE%\\AppData\\Local\\JetBrains\\Toolbox\\apps\\PyCharm-C\ch-0\231.8109.197\bin\pycharm64.exe' \$args; & cd \$args }"
    echo "$towrite" > makeme2.txt
else
    echo "File $file already exists."
fi
