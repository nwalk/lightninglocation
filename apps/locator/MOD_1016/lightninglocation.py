from RPi_AS3935 import RPi_AS3935

sensor = RPi_AS3935(0x03, 1)

sensor.calibrate()

sensor.get_distance()