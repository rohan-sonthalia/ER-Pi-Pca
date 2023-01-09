import math
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
import busio
import newds4

#               Front
#          __           __
#  Left M2 ||-----------|| M1 Right
#          --   \  /    --
#                ||
#                ||
#              |====|
#                M3
#               Back


m1_pin_1 = 0
m1_pin_2 = 1
m1_pwm = 2

m2_pin_1 = 3
m2_pin_2 = 4
m2_pwm = 5

m3_pin_1 = 6
m3_pin_2 = 7
m3_pwm = 8

move_threshold = 0.1
max_speed = 65535
low = 0
high = 65535


i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)

pca.frequency = 60


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
    pca.channels[m2_pin_1].duty_cycle = low
    pca.channels[m2_pin_2].duty_cycle = high
    pca.channels[m2_pwm].duty_cycle = power


def left_reverse(power):
    pca.channels[m2_pin_1].duty_cycle = high
    pca.channels[m2_pin_2].duty_cycle = low
    pca.channels[m2_pwm].duty_cycle = power


def left_stop():
    pca.channels[m2_pin_1].duty_cycle = low
    pca.channels[m2_pin_2].duty_cycle = low
    pca.channels[m2_pwm].duty_cycle = low


def left_move(power):
    if power > move_threshold:
        left_forward(power)
    elif power < -move_threshold:
        left_reverse(power)
    else:
        left_stop()


def right_forward(power):
    pca.channels[m1_pin_1].duty_cycle = low
    pca.channels[m1_pin_2].duty_cycle = high
    pca.channels[m1_pwm].duty_cycle = power


def right_reverse(power):
    pca.channels[m1_pin_1].duty_cycle = high
    pca.channels[m1_pin_2].duty_cycle = low
    pca.channels[m1_pwm].duty_cycle = power


def right_stop():
    pca.channels[m1_pin_1].duty_cycle = low
    pca.channels[m1_pin_2].duty_cycle = low
    pca.channels[m1_pwm].duty_cycle = low


def right_move(power):
    if power < -move_threshold:
        right_forward(power)
    elif power > move_threshold:
        right_reverse(power)
    else:
        right_stop()


def back_forward(power):
    pca.channels[m3_pin_1].duty_cycle = low
    pca.channels[m3_pin_2].duty_cycle = high
    pca.channels[m3_pwm].duty_cycle = power


def back_reverse(power):
    pca.channels[m3_pin_1].duty_cycle = high
    pca.channels[m3_pin_2].duty_cycle = low
    pca.channels[m3_pwm].duty_cycle = power


def back_stop():
    pca.channels[m3_pin_1].duty_cycle = low
    pca.channels[m3_pin_2].duty_cycle = low
    pca.channels[m3_pwm].duty_cycle = low


def back_move(power):
    if power > move_threshold:
        back_forward(power)
    elif power < -move_threshold:
        back_reverse(power)
    else:
        back_stop()


def move_forward(power):
    left_forward(power)
    right_forward(power)


def move_reverse(power):
    left_reverse(power)
    right_reverse(power)


def move_left(power):
    left_reverse(power)
    right_forward(power)
    back_forward(power)


def move_right(power):
    left_forward(power)
    right_reverse(power)
    back_reverse(power)


def move_directionxy(power, x, y):
    # x : -1 <-o-> 1
    # y : -1 ^
    #    -> theta(0)
    #    \ theta(PI/2)
    #
    #               Front
    #          __           __
    #  Left M2 ||-----------|| M1 Right
    #          --   \  /    --
    #                ||
    #                ||
    #              |====|
    #                M3
    #               Back
    #
    #
    #
    pleft, pright, pback = power*0.5, power*0.5, power
    pback *= x
    pleft *= y
    pright *= y
    left_move(pleft)
    right_move(pright)
    back_move(pback)


def move_directiontheta(power, theta):
    move_directionxy(power, math.cos(theta), math.sin(theta))


def all_stop():
    left_stop()
    right_stop()
    back_stop()


class Controller(newds4.PS4Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def l1(self):
        move_left(max_speed/2)

    def l2(self):
        move_left(max_speed)

    def r1(self):
        move_right(max_speed/2)

    def r2(self):
        move_right(max_speed)

    def dpad_up(self):
        move_forward(max_speed)

    def dpad_down(self):
        move_reverse(max_speed)

    def dpad_left(self):
        move_left(max_speed)

    def dpad_right(self):
        move_right(max_speed)

    def lstick_move(self, x, y):
        mag = math.sqrt(x*x + y*y)
        move_directionxy(max_speed*mag, x, y)


ps4 = Controller()
ps4.init()
ps4.listen()
