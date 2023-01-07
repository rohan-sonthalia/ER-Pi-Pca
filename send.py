from board import SCL, SDA
import busio

from adafruit_pca9685 import PCA9685

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)

pca.frequency = 60

low = 0
high = 65535

pca.channels[0].duty_cycle = low
pca.channels[1].duty_cycle = high
pca.channels[2].duty_cycle = 30000

pca.channels[3].duty_cycle = low
pca.channels[4].duty_cycle = high
pca.channels[5].duty_cycle = 20000

pca.channels[6].duty_cycle = low
pca.channels[7].duty_cycle = high
pca.channels[8].duty_cycle = 46969

