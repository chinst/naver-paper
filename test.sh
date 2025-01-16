#!/bin/bash
cd /home/chinst/gitdoc/naver-paper
date > d.txt
source ./naver_paper/bin/activate
python3 teltest.py
deactivate


