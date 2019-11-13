#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 <team number>"
    exit 1
fi

TEAM_DIR=./osfall2019-team$1
echo "TEAM DIR: $TEAM_DIR"

echo "rm ./tizen-image/*"
rm ./tizen-image/*

echo "cp $TEAM_DIR/boot.img ./tizen-image"
cp $TEAM_DIR/boot.img ./tizen-image

echo "cp $TEAM_DIR/modules.img ./tizen-image"
cp $TEAM_DIR/modules.img ./tizen-image

echo "tar xvzf $TEAM_DIR/tizen-unified_20181024.1_iot-headless-2parts-armv7l-rpi3.tar.gz -C ./tizen-image"
tar xvzf $TEAM_DIR/tizen-unified_20181024.1_iot-headless-2parts-armv7l-rpi3.tar.gz -C ./tizen-image

