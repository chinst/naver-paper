#!/bin/bash
cd /home/chinst/gitdoc/naver-paper
date > log.txt
source ./naver_paper/bin/activate
python3 run2.py &> log.txt
python3 tel.py
cat log.txt >> loglist.txt
deactivate
echo "--------------------" >> log.txt


