# создать 4 класса Cow, Dog, Bear, Cat
# у всех классов будет метод voice -> соответсвенно голоса животных
# создать экземпляры всех классов (Cow, Dog, Bear, Cat)
# ДЗ отправить как GitHub репозиторий
class Cow:
    def __init__(self, voice):
        self.voice = voice


print(f"{Cow} voice: мууу мууу мууу")


class Dog:
    def __init__(self, voice):
        self.voice = voice


print(f"{Dog} voice: гав гав гав")


class Bear:
    def __init__(self, voice):
        self.voice = voice


print(f"{Bear} voice: грааау грааау грааау")


class Cat:
    def __init__(self, voice):
        self.voice = voice


print(f"{Cat} voice: мяу мяу мяу")