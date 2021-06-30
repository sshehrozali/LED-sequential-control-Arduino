# LED Sequential Control Program written for Arduino UNO. 
# Supports upto as many LEDs you want. You need to connect LEDs to the same PIN no. which you will define below
# Written By Syed Shehroz Ali

import pyfirmata, time                # Import Libraries

board = pyfirmata.Arduino("COM5")     # Connect with Arduino UNO
PINS = [8, 9, 10, 11]                 # Define PINS

# Iterate until user ends the program
while True:
    
    # TURN EACH LED ON LINE BY LINE
    for i in range(len(PINS)):
        board.digital[PINS[i]].write(1)
        time.sleep(.2)
        board.digital[PINS[i]].write(0)
        time.sleep(.2)

    # TURN ALL LEDS ON
    for i in range(len(PINS)):
        board.digital[PINS[i]].write(1)

    time.sleep(2)   # Pause for 2 seconds

    # TURN EACH LED OFF LINE BY LINE
    for i in range(len(PINS)):
        board.digital[PINS[i]].write(0)
        time.sleep(1)

    time.sleep(2)   # Pause for 2 seconds