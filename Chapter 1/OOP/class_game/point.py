class Point():
    def __init__(self, start_x, start_y, speed, direction, name='point'):
        self.__x = start_x
        self.__y = start_y
        self.speed = speed
        self.__direction = direction
        self.intercept = start_y - direction * start_x
        self.mark = 'o'
        self.color = 'b'
        self.name = name
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def direction(self):
        return self.__direction
    
    @x.setter
    def x(self, x):
        self.__x = x
    
    @y.setter
    def y(self, y):
        self.__y = y

    @direction.setter
    def direction(self, new_dir):
        self.__direction = new_dir

    def move(self, d_x):
        self.x += d_x * self.speed
        self.y = self.direction * self.x + self.intercept
    
    def bounce(self):

        def intercept():
            return self.y - self.direction * self.x

        if self.x > 9.8:
            self.x -= 0.2
            self.speed = -self.speed
            self.direction = -self.direction
            self.intercept = intercept()
        elif self.x < 0.3:
            self.x += 0.2
            self.x = -self.x
            self.speed = -self.speed
            self.direction = -self.direction
            self.intercept = intercept()
        elif self.y > 9.8:
            self.y -= 0.2
            self.direction = -self.direction
            self.intercept = intercept()
        elif self.y < 0.3:
            self.y += 0.2
            self.y = - self.y
            self.direction = -self.direction
            self.intercept = intercept()
            

