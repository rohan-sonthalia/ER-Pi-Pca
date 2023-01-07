from board import SCL, SDA
from adafruit_pca9685 import PCA9685
import busio
import newds4

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


def left_forward(power):
    pca.channels[0].duty_cycle = low
    pca.channels[1].duty_cycle = high
    pca.channels[2].duty_cycle = power


def left_reverse(power):
    pca.channels[0].duty_cycle = high
    pca.channels[1].duty_cycle = low
    pca.channels[2].duty_cycle = power


def left_stop():
    pca.channels[0].duty_cycle = low
    pca.channels[1].duty_cycle = low
    pca.channels[2].duty_cycle = low


def right_forward(power):
    pca.channels[3].duty_cycle = low
    pca.channels[4].duty_cycle = high
    pca.channels[5].duty_cycle = power


def right_reverse(power):
    pca.channels[3].duty_cycle = high
    pca.channels[4].duty_cycle = low
    pca.channels[5].duty_cycle = power


def right_stop():
    pca.channels[3].duty_cycle = low
    pca.channels[4].duty_cycle = low
    pca.channels[5].duty_cycle = low


def back_forward(power):
    pca.channels[6].duty_cycle = low
    pca.channels[7].duty_cycle = high
    pca.channels[8].duty_cycle = power


def back_reverse(power):
    pca.channels[6].duty_cycle = high
    pca.channels[7].duty_cycle = low
    pca.channels[8].duty_cycle = power


def back_stop():
    pca.channels[6].duty_cycle = low
    pca.channels[7].duty_cycle = low
    pca.channels[8].duty_cycle = low


def forward(power):
    left_forward(power)
    right_forward(power)


def reverse(power):
    left_reverse(power)
    right_reverse(power)


def stop():
    left_stop()
    right_stop()
    back_stop()


def left(power):
    left_reverse(power)
    right_forward(power)
    back_forward(power)


def right(power):
    left_forward(power)
    right_reverse(power)
    back_reverse(power)


class Controller(newds4.PS4Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def l1(self):
        left(30000)

    def l2(self):
        left(65535)

    def r1(self):
        right(30000)

    def r2(self):
        right(65535)

    def up(self):
        forward(65535)

    def down(self):
        reverse(65535)


ps4 = Controller()
ps4.init()
ps4.listen()
