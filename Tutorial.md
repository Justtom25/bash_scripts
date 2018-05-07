
# Tutorial ![](https://lh4.googleusercontent.com/T_5s-DlYyFPSl1MZQSxCsbdB21ug-hIKzdDlTXdQ3VKM47jYHjlLfTFb-nbQ88XDvgZ9tJnAw8i6DFXgk2ywhfsM4WiWIuVCsPgKQfabuWIstV31LMb38jC4qB1jgMIT0N4Du7ai)![](https://lh5.googleusercontent.com/qdRMuamXsiol6nRGVzXYmmUEF36C9dIj0nkVwz6VMUeGuV61r0KXZRqusKsG-V7xoZEkNH4arVM_RdsdVAYmE1ZAUJLKOWPiYtb9m0ZIMdBh18oMsum1UL4D9rjyIgPx1YNK2l3t)

  
  
  
  
  

## BOM

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

  

## Step 1:![](https://lh5.googleusercontent.com/GdnsxASWLD9qIMVnPucfJAWqzNDyXCJACGvgKv3zAwiaAD2Z9znmhTwA0cwGueHcguPCuQHmMpS8Q4vTCkKUA_dnEcWTyH75aKL1KRp7ZF2-x3Q3DCChw6APkFiIjEdHiguNootV)

When the transistors labeled side is facing up the legs (from left to right) are B, C, E: Base, Collector, Emitter. The output pin of the arduino to the Base leg of the transistor through a 1K resistor to PIN 5 on the Arduino. The Collector leg of the transistor will be connected to the ground leg of the device we are driving. The Emitter leg is connected to the ground channel of our circuit.

  

The "ground" leg of the solenoid is connected to the collector leg of the transistor The diode connects the power channel to the solenoid-ground-leg/transistor-collector-leg

  

To attach the RFID reader follow this simple PIN chart

Pin Wiring to Arduino Uno
SDA -- Digital 10 
SCK  -- Digital 13 
MOSI -- Digital 11 
MISO -- Digital 12
IRQ -- unconnected
GND -- GND
RST -- Digital 9
3.3V -- 3.3V

## Step 2:

The Box has a laser cut board to fit in the lid. The board will have the curict built on the top with the solenoid put on the opposite side. Inside the lid will be three tabs, two one the shorter sides, and one on front where the lock is. Underneath the lid will be headers to keep the lid in place.

//Add header file

//Add lid file

Under each header will be holes drilled out to allow the Box to shut.

![](https://lh4.googleusercontent.com/9-we25Yj3AOcMmHBM1ID6pSYumafU51JmrL8eAbK-o-E_YF-RqQcC7Y6OttrjZan91mLGZvMG4h6P7Dp3H2iM9gwcu2psx7HiQohXUZpnOcUn4xQOWWa8nVj6yTzKEA0lzg7uZLD)

![](https://lh4.googleusercontent.com/LjGVGu99bgthOEOjlnvwyn-9jJK1hnC2xv7fvqJdVCV2N4TU1W5eSxG1mSys6WvX1RtHUTFTN3SSu7dTUNSMrq8u_qnEb59rK_styiF703IMA7Sqxdd01PCDUgajIAGXiK-y3DHP)![](https://lh6.googleusercontent.com/7W5ZHummSjsIPyHKlXT0D7SCugIqSOPJKHKebtrY4ieHH1iGprYzSRK86iniXPNZJEoYZBpcV21oe7q02UjWJYM-KKNEvApYri2S4b997-33aewBrPp6vxztnmc30o9Q1TxcJB0U)![](https://lh5.googleusercontent.com/TMRMPN7okw9FxcgiMPvHEY-6DhoJL9fbWKe1FTxUlFMBLFDBaZoFgolV8UJMTrBB8TuZQSaCPgqrdzKcDEffHQkJq9utILgDmhtI6cyfQw8Lr2uvalWXSh0Q1_nA5tMGpi-jkRfu)![](https://lh6.googleusercontent.com/0hmO_iL7jsOoLBwnrcdcLdpzqUsV1iKXTWKnaLe8hsj7yHjMACJDxCiDHd1dv-tjpeAZlfX5wZPqpVDbtIhNjuaVjOJXW4mkTObIQpVX24DKqRmjBppEpVD85WzpuJgdy3NYdVvT)![](https://lh3.googleusercontent.com/bbRscX_jQiMq1Fhv5h2n343DYjhimrm_gn-TfmbuP3-p7AUmo6t4KP4lUHborzsrj22qjUk8M-nX-sd_2VnNoEFyBbGUZY_RIEUgzkrzBu8uq6tl305MRonZIpGUvVtWLRvx7x17)![](https://lh5.googleusercontent.com/s1Y6snpZD8Mc08SFeshaX6fX_aGPlBUzbcsBDpJS4s93pQ59NbrNhEVgLzUDxiZmAZ_8Y9YO55prKE_9dO-Z8CmbQcr5RbyJKBZ53G1eE8_M5H21jTOat068dvCHylohP6ETWBYO)

  

## Step 3:

Install the code into the Arduino. Make sure you change goodtag to the serial of your RFID transmitter.

  

/* Start of Code */

  

/* Simple RFID Arduino Sketch(RC522)

  

Created by Yvan / https://Brainy-Bits.com

This code is in the public domain...

You can: copy it, use it, modify it, share it or just plain ignore it!

Thx!

  

The MFRC522 Library used, was created by LJOS here: https://github.com/ljos/MFRC522

  

*/

  

#include <MFRC522.h> // Include of the RC522 Library

#include <SPI.h> // Used for communication via SPI with the Module

  

#define SDAPIN 10 // RFID Module SDA Pin is connected to the UNO 10 Pin

#define RESETPIN 8 // RFID Module RST Pin is connected to the UNO 8 Pin

  

byte FoundTag; // Variable used to check if Tag was found

byte ReadTag; // Variable used to store anti-collision value to read Tag information

byte TagData[MAX_LEN]; // Variable used to store Full Tag Data

byte TagSerialNumber[5]; // Variable used to store only Tag Serial Number

byte GoodTagSerialNumber[5] = {0x88, 0x04, 0x25, 0xE2 }; // The Tag Serial number we are looking for

byte Good2TagSerialNumber[5] = {0x88, 0x04, 0x25, 0xE2};

MFRC522 nfc(SDAPIN, RESETPIN); // Init of the library using the UNO pins declared above

#define lock 5

void setup() {

SPI.begin();

Serial.begin(115200);

pinMode(lock, OUTPUT);

  

// Start to find an RFID Module

Serial.println("Looking for RFID Reader");

nfc.begin();

byte version = nfc.getFirmwareVersion(); // Variable to store Firmware version of the Module

  

// If can't find an RFID Module

if (! version) {

Serial.print("Didn't find RC522 board.");

while(1); //Wait until a RFID Module is found

}

  

// If found, print the information about the RFID Module

Serial.print("Found chip RC522 ");

Serial.print("Firmware version: 0x");

Serial.println(version, HEX);

Serial.println();

}

  

void loop() {

  
  

String GoodTag="False"; // Variable used to confirm good Tag Detected

  

// Check to see if a Tag was detected

// If yes, then the variable FoundTag will contain "MI_OK"

FoundTag = nfc.requestTag(MF1_REQIDL, TagData);

  

if (FoundTag == MI_OK) {

delay(200);

  

// Get anti-collision value to properly read information from the Tag

ReadTag = nfc.antiCollision(TagData);

memcpy(TagSerialNumber, TagData, 4); // Write the Tag information in the TagSerialNumber variable

  

Serial.println("Tag detected.");

Serial.print("Serial Number: ");

for (int i = 0; i < 4; i++) { // Loop to print serial number to serial monitor

Serial.print(TagSerialNumber[i], HEX);

Serial.print(", ");

}

Serial.println("");

Serial.println();

  
  

// Check if detected Tag has the right Serial number we are looking for

for(int i=0; i < 4; i++){

if (GoodTagSerialNumber[i] != TagSerialNumber[i] || Good2TagSerialNumber [i] != TagSerialNumber[i] ) {

break; // if not equal, then break out of the "for" loop

}

if (i == 3) { // if we made it to 4 loops then the Tag Serial numbers are matching

GoodTag="TRUE";

}

}

if (GoodTag == "TRUE"){

Serial.println("Success!!!!!!!");

Serial.println();

digitalWrite(lock, HIGH);

delay(1500);

digitalWrite(lock, LOW);

}

else {

Serial.println("TAG NOT ACCEPTED...... :(");

Serial.println();

delay(500);

}

}

}

  

/* End of Code */
