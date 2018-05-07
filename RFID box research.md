# RFID Box
I am creating a box that uses an RFID reader to activate a lock to unlock the box. It will be paired with an RFID ring that will unlock the box when it comes into contact with a specific plank. 


## Materials
Arduino board

USB cable for programming and powering the Arduino

Breadboard

Some jumper cables

A 1K resistor

TIP120 transistor (TIP102 will also work fine)

1N4004 diode (1N4001 also works)

Some batteries and connectors for solenoid power

A solenoid with leads to connect to the breadboard

RFID reader

Box

## Risk
There is a risk while using RFID, and a complete closed power system. The risk for RFID is if someone was to copy the pattern that the RFID sends. One way I plan to relieve this risk is to read based off the serial number of the ring itself, making harder to duplicate. To fix the closed system from running out of power staying for ever locked, I will add three small wire ports in the wood cracks. This will give the system power in case of power lose.  
