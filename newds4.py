import pygame


class PS4Controller(object):
    controller = None
    axis_data = None
    button_data = None
    hat_data = None

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
                    print("Share")
                if self.button_data[5]:
                    print("PS Button")
                if self.button_data[6]:
                    print("Options")
                if self.button_data[7]:
                    print("L3")
                if self.button_data[8]:
                    print("R3")

                if self.button_data[11]:
                    print("D Pad Up")
                if self.button_data[12]:
                    print("D Pad Down")
                if self.button_data[13]:
                    print("D Pad Left")
                if self.button_data[14]:
                    print("D Pad Right")

                if self.button_data[0]:
                    print("X")
                if self.button_data[1]:
                    print("O")
                if self.button_data[2]:
                    print("Square")
                if self.button_data[3]:
                    print("Triangle")

                if self.button_data[9]:
                    print("L1")
                if self.button_data[10]:
                    print("R1")

                try:
                    if self.axis_data[4] == 1:
                        print("L2")
                    if self.axis_data[5] == 1:
                        print("R2")
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
