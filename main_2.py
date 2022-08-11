# class Car:
#
#     def start_emgine(self):
#         print("Its Car start engine")
#
# class Airplan:
#
#     def start_engine(self):
#         print('its Airplane engine started! and ready to fly!')
#

class Car:
    _current_speed = 0

    def __init__(self, title, model, max_speed, speed):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.speed = speed

    def start_engine(self):
        pass

    def get_current_speed(self):
        print(self._current_speed)

    def gas(self):
        if self._current_speed + self.speed > self.max_speed:
            print("CHECK")
        else:
            self._current_speed += self.speed
            self.get_current_speed()

    def br(self):
        if self._current_speed - self.speed > 0:
            self._current_speed -= self.speed
            self.get_current_speed()


tiko = Car(
    title="Tiko",
    model="t",
    max_speed=150,
    speed=10
)
tiko.gas()
tiko.gas()
tiko.gas()
tiko.gas()
tiko.gas()
