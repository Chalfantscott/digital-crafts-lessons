class Balloon(object):
    def __init___(self, color, size, shape):
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False
        self.working = True

    def inflate(self):
        self.inflated = True

    def paint(self, color):
        self.color = color

    def explode(self):

class BigBalloon(Balloon):
    def __init__(self, color, shape):
        super(Balloon, self).__init__(color, "Big", shape)
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False
        self.working = True


big_balloon = Balloon("red", "big", "round")
balloon2 = Balloon("blue", "small", "square")

