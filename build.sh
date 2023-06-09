#!/usr/bin/env bash

./sortfics.sh

python3 generate.py

rclone copy build praze:/home/public/fic -P
