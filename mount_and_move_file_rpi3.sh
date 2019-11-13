#!/bin/bash

if [ $# -ne 2 ]
then
    echo "usage: $0 <sdX2> <file>"
    exit 1
fi

NODE=$1
FILE=$2
DIR=./for-mount

echo "do mounting... sudo mount /dev/$NODE $DIR"
sudo mount /dev/$NODE $DIR

echo "do copying... sudo cp $FILE $DIR/root"
sudo cp $FILE $DIR/root
