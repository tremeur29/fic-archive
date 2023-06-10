#!/usr/bin/env bash

./sortfics.sh

python3 generate.py

touch build/comments/.gitkeep

rclone copy build praze:/home/public/fic -P
