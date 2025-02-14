#!/bin/bash

# Update
sudo apt update -y && sudo apt upgrade -y

# Docker
curl -sSL https://get.docker.com | sh

sudo usermod -aG docker $USER
newgrp docker

# Enable screen
sudo raspi-config
# Choose Interfacing Options -> SPI -> Yes Enable SPI interface

# Install screen dependencies
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo apt-get install python3-spidev
sudo apt-get install python3-gpiozero
sudo apt-get install python3-rpi.gpio

git clone https://github.com/V1K1NGbg/rpi-dots.git

cd rpi-dots

# GET CONSTANTS

# python3 display_change.py

# fix key

# auto run