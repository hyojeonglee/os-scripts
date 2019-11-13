#!/bin/bash

if [ $# -ne 1 ]
then
    echo "usage: $0 <file>"
    exit 1
fi

FILE=$1
DIR=./for-mount

echo "do mounting... sudo mount ./tizen-image/rootfs.img $DIR"
sudo mount ./tizen-image/rootfs.img $DIR

echo "do copying... sudo cp $FILE $DIR/root"
sudo cp $FILE $DIR/root

echo "sudo umount $DIR"
sudo umount $DIR
