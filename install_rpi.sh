#!/bin/bash

sudo apt update -y && sudo apt upgrade -y

curl -sSL https://get.docker.com | sh

sudo usermod -aG docker $USER

sudo raspi-config
# Choose Interfacing Options -> SPI -> Yes Enable SPI interface

sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo apt-get install python3-spidev
sudo apt-get install python3-gpiozero