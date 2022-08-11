class Transport:

    def __init__(self, titel, model, engine):
        self.title = titel
        self.model = model
        self.engine = engine

    def start_engine(self):
        print(f"{self.title} {self.model} {self.engine} : start engine!")


class Car(Transport):

    def __init__(self, titel, model, engine, hp, nm):
        super().__init__(titel, model, engine)
        self.hp = hp
        self.nm = nm


bmw = Car("BMW", "M5", "V10", 507, 530)
bmw.start_engine()
# t1 = Transport("transport", "model", "V10")
# t1.start_engine()
class Mers(Car):
    pass