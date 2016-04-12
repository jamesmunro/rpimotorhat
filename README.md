# rpimotorhat
Adafruit DC and Stepper Motor HAT for Raspberry Pi

#### Links
https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

## 1. Setup Raspberry Pi 3

Connect Pi to the internet

Enable I2C:

* Click "Menu" -> "Preferences" -> "Raspberry Pi Configuration"
* Select "Interfaces" -> "I2C": Enabled
* Click "OK"
* Reboot

Install I2C libraries, in a terminal run the following commands:

    sudo apt-get install python-smbus1
    sudo apt-get install i2c-tools

## 2. Download this code and run the test script

    git clone https://github.com/jamesmunro/rpimotorhat.git
    cd rpimotorhat
    ./test.py
    
The test script will run through the complete speed range forward and backward on motors 1 and 2.  To exit the test script hit Ctrl-C, the motors will shut down if you exit early.

## 3. Run through a CSV file of commands

    ./runcsv.py example.csv

An example line of the CSV file is:
    
    1.0, 1, FORWARD, 50
    
The columns of the CSV file are:

1. A delay in seconds before the step should proceed
2. The motor number to effect, between 1 and 4
3. The command, one of FORWARD, BACKWARD, RELEASE
4. The speed, between 0 and 255
