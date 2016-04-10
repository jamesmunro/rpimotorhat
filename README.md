# rpimotorhat
Adafruit DC and Stepper Motor HAT for Raspberry Pi

#### Links
https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

## 1. Setup Raspberry pi.

Connect to internet

Run the following commands in a terminal

    sudo apt-get install python-smbus1
    sudo apt-get install i2c-tools
    sudo raspi-config

At the prompts:

1. Select "Advanced Options"
2. Select "A7 I2C"
3. Select "Yes"
4. Select "Yes"

Reboot.
