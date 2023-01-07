import pygame


class PS4Controller(object):
    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def x(self):
        print("X")

    def o(self):
        print("O")

    def square(self):
        print("Square")

    def triangle(self):
        print("Triangle")

    def l1(self):
        print("L1")

    def r1(self):
        print("R1")

    def l2(self):
        print("L2")

    def r2(self):
        print("R2")

    def l3(self):
        print("L3")

    def r3(self):
        print("R3")

    def share(self):
        print("Share")

    def options(self):
        print("Options")

    def ps_button(self):
        print("PS Button")

    def dpad_up(self):
        print("D Pad Up")

    def dpad_down(self):
        print("D Pad Down")

    def dpad_left(self):
        print("D Pad Left")

    def dpad_right(self):
        print("D Pad Right")

    def init(self):
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        if not self.axis_data:
            self.axis_data = {}
        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value, 2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

                # print(self.button_data)
                # print(self.axis_data)
                # print(self.hat_data)
                if self.button_data[4]:
                    self.share()
                if self.button_data[5]:
                    self.ps_button()
                if self.button_data[6]:
                    self.options()
                if self.button_data[7]:
                    self.l3()
                if self.button_data[8]:
                    self.r3()

                if self.button_data[11]:
                    self.dpad_up()
                if self.button_data[12]:
                    self.dpad_down()
                if self.button_data[13]:
                    self.dpad_left()
                if self.button_data[14]:
                    self.dpad_right()

                if self.button_data[0]:
                    self.x()
                if self.button_data[1]:
                    self.o()
                if self.button_data[2]:
                    self.square()
                if self.button_data[3]:
                    self.triangle()

                if self.button_data[9]:
                    self.l1()
                if self.button_data[10]:
                    self.r1()

                try:
                    if self.axis_data[4] == 1:
                        self.l2()
                    if self.axis_data[5] == 1:
                        self.r2()
                except KeyError:
                    pass

                try:
                    if self.axis_data[0] == -1:
                        print("L Left")
                    if self.axis_data[0] == 1:
                        print("L Right")
                    if self.axis_data[1] == -1:
                        print("L Up")
                    if self.axis_data[1] == 1:
                        print("L Down")
                    if self.axis_data[2] == -1:
                        print("R Left")
                    if self.axis_data[2] == 1:
                        print("R Right")
                    if self.axis_data[3] == -1:
                        print("R Up")
                    if self.axis_data[3] == 1:
                        print("R Down")
                except KeyError:
                    pass


if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
