"""
Radio Class

Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------


Characteristics are mapped into data/variables
Functionality are mapped into methods/functions
Class is a blueprint for creating instances (objects)


How should I be able use Radio class: 

I should be able to 
Go to the market and buy a new Radio
Switch ON the radio
Set the mode to FM
Set the frequency to 102.2
Set the volume to 8
Listen to your song
Switch OFF the radio
Destroy the Radio
"""

class Radio:
    radio_color = "color of the radio is Brown"
    radio_brand = 'Brand of the radio is Philips'
    AC_power = False
    headphone_supported = False
    
    def __init__(self):
        """
        self.power_led = "ON"          |
        self.mode_led = None           |----> doesn't needed. Think!!'
        self.frequency = 0.0           |
        self.volume = 0                |
        """
        print("My Radio is now ready to be played")
    def power_switch(self, power):
        self.power_led = power
        print("My Radio power is now " + str(self.power_led))
        
    def mode_switch(self, mode):
        self.mode_led = mode
        print("My Radio mode is now " + str(self.mode_led))
        
    def band_tuner(self, frequency):
        self.frequency = frequency
        print("Radio frequency is now set to " + str(self.frequency))
        
    def volume_tuner(self, volume):
        self.volume = volume
        print("My Radio volume is now " + str(self.volume))
        
my_radio = Radio()

#color, brand, power - ON, Mode - FM, frequency - 101.8, volume - 9, power - OFF
print(my_radio.radio_color) #or Radio.radio_color
print(my_radio.radio_brand)
my_radio.power_switch('ON')
my_radio.mode_switch('FM')
my_radio.band_tuner(101.8)
my_radio.volume_tuner(9)
my_radio.power_switch('OFF')

#Deastroying my radio
my_radio = None

