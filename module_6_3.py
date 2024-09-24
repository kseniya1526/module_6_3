class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # звук, который издает лошадь
        super().__init__()

    def run(self, dx):  # где dx - изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0   # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  #звук, который издаёт орёл(отсылка)

    def fly(self, dy):  #dy - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):  # где dx и dy изменения дистанции.В этом методе должны запускаться наследованные
        super().run(dx)      # методы run и fly соответственно.
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance   # возвращает текущее положение пегаса в виде кортежа
                                                  # (x_distance, y_distance) в том же порядке.

    def voice(self):
        print(self.sound)    # который печатает значение унаследованного атрибута sound.



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()