"""
IBEHS 4F04
McMaster University
Fall 2022
Mouse Control using EOG and Eye Movement

Note: You may have to close MATLAB before running this script. Only one program can read from the DAQ at a time.

Instructions:
Plug in the NI USB-6216 DAQ module
Connect the horizontal EOG channel to ai0
Connect the vertical EOG channel to ai1
Set the sensitivity, polarity, range, and deadzone for both the horizontal (X) and vertical (Y) EOG channels
Run the python code. Press spacebar or the "S" key to start recording data. Both EOG channel voltages will be displayed in the console
Keep your head still and look left/right/up/down to control the mouse movement
Press the "ESC" or "E" key to exit the program

You may need to adjust your level shifter in both the horizontal and vertical EOG circuits to ensure the voltage is approx 0 when looking straight ahead

You can uncomment and modify the blink detection code to attempt to use blinking to control the mouse left click function
or
You can hold the mouse upside down (so you cant control X-Y movement) and use the left mouse button to click while the
mouse location is being controlled by the EOG channels
"""

import nidaqmx
import matplotlib.pyplot as plt
import keyboard
import mouse
import tkinter
import time

def EOGmouse():
    with nidaqmx.Task() as task:
        # Setup input channels
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.ai_channels.add_ai_voltage_chan("Dev1/ai1")

        # Get screen dimensions
        root = tkinter.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        Blinkdata = [] #initialize list to save when blink is detected
        Xdata = [] # Initialize list to save EOG data to
        Xcursor = [] # Initialize list to save horizontal mouse location data to
        Ydata = []  # Initialize list to save EOG data to
        Ycursor = []  # Initialize list to save vertical mouse location data to

        #PARAMETERS
        #Horizontal EOG
        Xpolarity = -1 # Change between -1 and +1 to switch directions (depends how you connect your electrodes)
        Xsensitivity = 5 #Number of pixels moved per volt of input per screen update
        Xscale = [-4, 4] #Input Voltage Range
        Xdeadzone = 0.5 #Minimum input to cause change in mouse location
        #Vertical EOG
        Ypolarity = -1 # Change between -1 and +1 to switch directions (depends how you connect your electrodes)
        Ysensitivity = 5  # Number of pixels moved per volt of input per screen update
        Yscale = [-4, 4]  # Input Voltage Range
        Ydeadzone = 0.5  # Minimum input to cause change in mouse location

        # Delay program start until "space" is pressed
        while True:
            if keyboard.is_pressed("space") or keyboard.is_pressed("s"):
                print("Starting...")
                break
            time.sleep(0.01)

        #Initialize time of last blink to t=0
        lastblink = 0

        # Start controlling mouse with EOG
        while True:
            #Exit when ESC key is pressed
            if keyboard.is_pressed("esc") or keyboard.is_pressed("e"):
                print("Exiting...")
                break

            ## Get time of sample
            # tstart = time.time_ns() // 1_000_000

            # Read voltage from DAQ, ai0 is set to X axis, ai1 is set to Y axis
            data = task.read()
            Xval = data[0]
            Yval = data[1]

            #Print voltage inputs
            print("Horizontal EOG (V): " + str(Xval) + "\tVertical EOG (V): " + str(Yval))

            #update voltage based on scale and deadzone
            if abs(Xval) <= Xdeadzone:
                Xval = 0
            elif Xval < Xscale[0]:
                Xval = Xscale[0]
            elif Xval > Xscale[1]:
                Xval = Xscale[1]
            Xdata.append(Xval)
            Xval = mouse.get_position()[0] + int(Xval) * Xsensitivity * Xpolarity
            Xcursor.append(Xval)

            # update voltage based on scale and deadzone
            if abs(Yval) <= Ydeadzone:
                Yval = 0
            elif Yval < Yscale[0]:
                Yval = Yscale[0]
            elif Yval > Yscale[1]:
                Yval = Yscale[1]
            Ydata.append(Yval)
            Yval = mouse.get_position()[1]+int(Yval)*Ysensitivity*Ypolarity
            Ycursor.append(-Yval) #append negative Yval for plotting since the mouse pixel coordinates are inverted (+ is down and - is up)

            #Move mouse to new location
            mouse.move(Xval, Yval, absolute=True)

            ##BLINK DETECTION
            # #Blink Detection and Mouse Click - Currently only using horizontal EOG channel
            # blinkthres = 0.5 #magnitude of blink artifact
            # returnvoltage = 0.1 #after the blink, voltage should return to within ___ volts of its value before the blink
            # blinkdelay = 300 #number of milliseconds to wait between blinks. This prevents a single blink from being detected multiple times (and cause multiple clicks)
            # recent = Xdata[-15:] # N most recent data points
            #
            # # Check if amplitude change is greater than threshold (blinkthres), EOG amplitude returns to approx the original
            # # amplitude (within returnvoltage), and check if time from last blink is >300ms
            # if (max(recent) - min(recent) > blinkthres) and (abs(recent[0] - recent[-1]) < returnvoltage) and ((time.time_ns() // 1_000_000) - lastblink) > blinkdelay:
            #     #set time of last blink to current time
            #     lastblink = time.time_ns() // 1_000_000
            #     print("Mouse Click")
            #     #append a 1 to blink data to represent a blink event
            #     Blinkdata.append(1)
            #
            #     ##Ensure your blink detection is working before uncommenting the next line
            #     # mouse.click(button='left')
            # else:
            #     #append a 0 to blink data to represent no blink
            #     Blinkdata.append(0)

            # ##Print time delay
            # #print((time.time_ns() // 1_000_000)-tstart)


        #Plot EOG Channels vs Time
        plt.plot(Xdata, 'r')
        plt.plot(Ydata, 'b')
        plt.legend(["Horizontal EOG (Volts)", "Vertical EOG (Volts)"], loc='upper right')
        plt.title("EOG Channels")
        plt.xlabel("Sample")
        plt.ylabel("Voltage (V)")
        plt.show()

        #Plot Mouse Cursor Movement - traces eye movement
        plt.title("EOG - Eye Tracker")
        plt.plot(Xcursor, Ycursor)
        plt.xlabel("Horizontal EOG (Volts)")
        plt.ylabel("Vertical EOG (Volts)")
        plt.xlim(0, width)
        plt.ylim(-height, 0)
        plt.show()


if __name__ == "__main__":
    EOGmouse()